# Exact identity recovery only

Executed 2026-10-04; exact title leads TokenSeek 2601.19739 and Video-KTR 2601.19686. No conference scan. OpenReview notes Br1uoB0Jiy / p0sDIEsYG3 are concrete identity leads, but API2 returned ChallengeRequiredError HTTP403; forum redirected browser verification. Search relative dates are discovery, not precise public timestamps. DART was not found as ICLR; its current official repo says EMNLP26, which does not by itself imply earlier public paper. Therefore do not assign a 2025 first-public date to any of these merely from conference naming.

Published as a conference paper at ICLR 2026 (https://openreview.net/pdf?id=Br1uoB0Jiy)
citeturn28112search0 [wordlim: 200] Published: 7 months ago; TOKENSEEK: MEMORY EFFICIENT FINE TUNING VIA ... or improving the efficiency of gradient updates and optimizer states to alleviate the training memory
Published as a conference paper at ICLR 2026
TOKENSEEK: MEMORY EFFICIENT FINE TUNING VIA
INSTANCE-AWARE TOKEN DITCHING
Runjia Zeng1, Qifan Wang2, Qiang Guan3, Ruixiang Tang4,
Lifu Huang5, Zhenting Wang6, Xueling Zhang1, Cheng Han7, Dongfang Liu1†
1Rochester Institute of Technology
2Meta AI
3Kent State University
4Rutgers University
5UC Davis
6Accenture
7University of Missouri-Kansas City
†Corresponding author
ABSTRACT
Fine-tuning has been regarded as a de facto approach for adapting large language
models (LLMs) to downstream tasks. However, the high training memory consump-
tion inherited from LLMs makes this process generally inefficient. Among existing
memory efficient approaches, activation-related optimization has proven particu-
larly effective, as activations consistently dominate overall memory consumption.
Although prior arts offer various activation optimization strategies, they typically
adopt a uniform yet inflexible strategy across all instance. This data-agnostic nature
ultimately results in ineffective and unstable fine tuning. To solve this problem,
we propose TOKENSEEK, a universal plugin solution that is suitable for various
Transformer-based models through instance-aware token seeking and ditching. TO-
KENSEEK achieves significant fine-tuning memory savings (e.g., requiring only 2.8
GB, 14.8% of the original memory on Llama3.2 1B) with on-par or even superior
performance. Furthermore, our interpretable token seeking process reveals the
underlying factors behind its effectiveness, offering valuable insights for future
research on token efficiency fine-tuning. Homepage: runjia.tech/iclr_tokenseek.
1
INTRODUCTION
53
TokenSeek (Ours)
III.Activations
I. Parameters
II. Gradients &
Optimizer States
- w/ LoHa
- w/ QLoRA
52
87%
50%
TokenTune (Random)
2%
51
- w/ LoHa
- w/ QLoRA
Loss (3%)
Performance
LoHa
12%
50
Gradients (3%)
Optimizer
11%
38%
QLoRA
Loss (2%)
Optimizer
(24%)
(5%)
Gradients
Baseline
(12%)
100%
10%
40
Memory
Batch Size: 1
Batch Size: 8
(a) Training Memory Breakdown of Llama3 8B
(b) Performance-Memory Comparison
Figure 1: Motivation behind TOKENSEEK and its preliminary comparison. (a) Breakdown
of training memory under different batch side settings, revealing that activations are the primary
bottleneck in training memory consumption. (b) Effective and efficient TOKENSEEK (ours) vs.
concurrent arts in performance and memory consumption on Llama3.2 1B (detailed results in Tab. 1)
“Pretrain-then-Finetune” paradigm (Liu et al., 2024a; Yang et al., 2024; Grattafiori et al., 2024) has
been regarded as a de facto approach for downstream task adaptation, leveraging the knowledge
acquired during pre-training. However, fine tuning large language models (LLMs) still imposes
significant memory demands arising from multiple components (Zhang & Su, 2025; Rajbhandari
et al., 2020) as showin in Fig. 1 (a), including the model I. parameters, II. gradients and optimizer
states, and intermediate III. activations. Current works optimize training memory usage by targeting
different components. Parameter-Efficient Fine-Tuning (PEFT) (Zeng et al., 2024; Han et al., 2023;
2024) reduces the number of tunable parameters required for adapting large models (component I).
Optimizer-Efficient Fine-Tuning (Rajbhandari et al., 2020; Anil et al., 2019) focuses on partitioning
or improving the efficiency of gradient updates and optimizer states to alleviate the training memory
burden (component II). Memory-Efficient Fine-Tuning (MEFT) (Simoulin et al., 2024; Dettmers
et al., 2023) , on the other hand, improves memory efficiency by recomputing, compressing, or
1--------------------------------------------------------------------------------
Published as a conference paper at ICLR 2026 (https://openreview.net/pdf/f56e3e12fdd2c60cd7a7b3b3f162a5a820942cf5.pdf)
citeturn28112search1 [wordlim: 200] Published: 7 months ago; The key insight behind TOKENSEEK is that not all training tokens within LLMs contribute equally to model fine-tuning, known as token redundancy.Token redundancy has long been recognized as a fundamental challenge to LLM efficiency (Hou et al., 2022), drawing increasing research attention across various domains, including efficient chain-of-thought reasoning (Xia et al., 2025) and prompt optimization (Li et al., 2023).This observation greatly inspires us to explore the potential of memory-efficient fine-tuning by reducing token redundancy.
Published as a conference paper at ICLR 2026

<visual_element id="e1">
Figure 2: Overview of TOKENSEEK (ours) vs. TOKENTUNE frameworks.

(a) Instance-aware Token Seeking
- Legend: purple hollow circle = Requires grad; gray hollow circle = Does Not Require grad.
- Left green dashed panel contains two main regions:
  - Context Information
  - Gradient Information
- Top token row feeds into the panel; arrows indicate forward and backward flow.
- Inside Context Information: a Transformer block on the left, a token matrix in the center, and another Transformer block labeled “Transformer L₁” near the middle-right.
- Inside Gradient Information: a vertical token stack, a dotted/boxed gradient path, and a right-side block labeled “Transformer Lₙ”.
- Bottom label: “Token Evaluation: ○ = α + β ○” (with colored symbols indicating a weighted evaluation of tokens).
- Caption under panel: “(a) Instance-aware Token Seeking”.

(b) Efficient Token Ditching
- Top legend: “Forward → Backward”.
- A top token row points down to “Token Selection”.
- Below are token rows and a dashed box containing “Transformer Layer L₁” and “Transformer Layer Lₙ”.
- Caption under panel: “(b) Efficient Token Ditching”.

(c) TokenTune
- Right pink dashed panel.
- Top row labeled “Random Selection”.
- Middle text in red: “Data-agnostic!”
- A small prompt-like box says: “There are [blank] of two balls [blank] be [blank] ?”
- Bold text: “Can’t learn anything!”
- Red text at bottom: “Unstable! Ineffective!”
- Caption under panel: “(c) TokenTune”.
</visual_element>

Figure 2: Overview of TOKENSEEK (ours) vs. TOKENTUNE frameworks. (a) Instance-aware token seeking using context and gradient information (see §3.2.1 and Eq. 5). (b) Efficient token ditching (see §3.2.2). (c) TOKENTUNE for random token selection (see analysis in Tab. 1 and §4.3).

and applying the differentiation rules along with the chain rule, we can decompose the gradient with respect to the weight in the first layer in simplicity as:

\[
\frac{\partial \mathcal{L}}{\partial W^{(1)}} = \frac{\partial \mathcal{L}}{\partial z^{(L)}} \left(\prod_{\ell=2}^{L} \frac{\partial z^{(\ell)}}{\partial z^{(\ell-1)}}\right)\frac{\partial z^{(1)}}{\partial W^{(1)}}.
\tag{1}
\]

\[
\frac{\partial z^{(\ell)}}{\partial z^{(\ell-1)}} = \frac{\partial z^{(\ell)}}{\partial a^{(\ell)}} \frac{\partial a^{(\ell)}}{\partial z^{(\ell-1)}} = \sigma'(a^{(\ell)})\, W^{(\ell)}.
\tag{2}
\]

The computation of the back-prop term \(\sigma'(a^{(\ell)})\, W^{(\ell)}\) requires the intermediate value \(a^{(\ell)}\) to further evaluate \(\sigma'(a^{(\ell)})\). By caching each pre-activation \(a^{(\ell)}\) during the forward pass, the model can avoid recomputing to obtain these intermediates, thereby efficiently forming the full chain of derivatives.

**The Reason of Large Activations.** Current Transformer-based LLMs follow this rule to store activations during backpropagation. Taking DeepSeek-v3 (Liu et al., 2024a; Zhang & Su, 2025) as an example, the activations in each layer have a space complexity of \((B n_h s^2 + BsH)\), where \(B\) is the batch size, \(n_h\) is the number of attention heads, \(s\) is the sequence length, and \(H\) is the hidden dimension. The space complexity required for activations significantly outweighs that of the weights \((B n_h s^2 + BsH \gg H^2\) given \(B = 1, n_h = 128, s = 4096\) and \(H = 7168\) (Zhang & Su, 2025)).

3.2  TOKENSEEK

3.2.1  INSTANCE-AWARE TOKEN SEEKING

The key insight behind TOKENSEEK is that not all training tokens within LLMs contribute equally to model fine-tuning, known as token redundancy. Token redundancy has long been recognized as a fundamental challenge to LLM efficiency (Hou et al., 2022), drawing increasing research attention across various domains, including efficient chain-of-thought reasoning (Xia et al., 2025) and prompt optimization (Li et al., 2023). This observation greatly inspires us to explore the potential of memory-efficient fine-tuning by reducing token redundancy. Then the critical problem turns to determine the importances of each token. Here, we propose a comprehensive evaluation of tokens by leveraging both context and gradient information captured within Transformer blocks (see Fig. 2 (a)).

➤ **Context Information.** Most LLMs are built upon the Transformer architecture, which fundamentally relies on the attention mechanism (Vaswani et al., 2017). The attention maps in decoder layers directly reflect the importance of each token in context, thereby guiding and shaping the transformation process. More specifically, given input embeddings \(t \in \mathbb{R}^{n \times d}\), we first project them into queries and keys with learnable matrices \(W^Q, W^K \in \mathbb{R}^{d \times d}\) to obtain \(Q = tW^Q,\ \ K = tW^K\). We then form the attention scores and apply a causal mask for language modeling, computing \(A = \mathrm{softmax}(\mathrm{mask}(QK^T/\sqrt{d_k}))\). Each entry \(A_{ij}\) denotes the attention weight from token \(i\) to token \(j\). Owing to the row-wise softmax normalization, each row \(A_i\) forms a probability distribution over all tokens, capturing how much attention token \(i\) allocates to others. Conversely, each column

4

Published as a conference paper at ICLR 2026 (https://openreview.net/pdf/8f15dee2110b601c702e7ee50fbb2254ee7e726f.pdf)
citeturn28114search12 [wordlim: 200] Published: 7 months ago; Published as a conference paper at ICLR 2026 ... Unlike prior methods that impose coarse, global temporal constraints (Feng et al., 2025; Dang et al., 2025) or rely solely on entropy-based token selection (Wang et al., 2025b), Video-KTR explicitly models token sensitivity to visual and temporal perturbations, updating only critical tokens. ... 2) Video-KTR achieves SOTA performance on multiple video reasoning benchmarks, including 42.7% on Video-Holmes dataset—matching GPT-4o and significantly outperforming existing open-source baselines.
Moreover, many approaches fail to ensure fine-grained semantic alignment between visual inputs and output tokens. Without explicit modeling of modality-specific dependencies, models underutilize visual evidence and over-rely on linguistic priors (Wang et al., 2025d; Li et al., 2025b), increasing hallucination risks. Even token-level RL prioritizing high-uncertainty tokens via entropy (Wang et al., 2025b) often lack modality awareness, limiting their ability to capture visual–temporal dependencies. The absence of precise token-level correspondence across modalities not only reduces reasoning accuracy but also limits interpretability.

To address these challenges, we propose **Video-KTR**, a modality-aware policy shaping framework for token-level optimization in video reasoning. Unlike prior methods that impose coarse, global temporal constraints (Feng et al., 2025; Dang et al., 2025) or rely solely on entropy-based token selection (Wang et al., 2025b), Video-KTR explicitly models token sensitivity to visual and temporal perturbations, updating only critical tokens. We categorize these tokens as: (1) *visual-aware tokens*, identified via counterfactual masking to capture reliance on perceptual input; (2) *temporal-aware tokens*, detected through frame shuffling to reflect sensitivity to temporal order and causality; and (3) *high-entropy tokens*, characterized by predictive uncertainty, complementing the first two categories. This selective updating focuses learning capacity on the most informative reasoning steps, reducing interference from redundant tokens. As a result, Video-KTR significantly enhances both accuracy and integrated multimodal reasoning in complex video tasks.

To assess Video-KTR, we conduct extensive experiments on representative video reasoning benchmarks. Results demonstrate SOTA or highly competitive performance across datasets. On Video-Holmes, our method achieves an overall accuracy of 42.7%, surpassing GPT-4o (42.0%). Moreover, ablation experiments show that modality-aware token attribution, selective reinforcement learning, and targeted perturbation jointly enhance the exploitation of visual and temporal cues. These findings confirm that Video-KTR’s fine-grained, token-level optimization provides an effective and interpretable approach to advancing video reasoning.

**Our contributions** are twofold: 1) We employ counterfactual analysis to unveil modality-sensitive critical tokens in video reasoning, and propose Video-KTR tailored for token-level optimization in video reasoning tasks. To the best of our knowledge, this is the first work to integrate modality-aware token selection into RL for video reasoning. 2) Video-KTR achieves SOTA performance on multiple video reasoning benchmarks, including 42.7% on Video-Holmes dataset—matching GPT-4o and significantly outperforming existing open-source baselines. Ablation studies confirm the effectiveness of our modality-attribution signals, token selection strategy, and framework design, alongside the robustness and generalizability of Video-KTR.

2  RELATED WORK

Reinforcement learning has emerged as a powerful paradigm for enhancing the reasoning abilities of LLMs (OpenAI, 2024; DeepSeek-AI, 2025; Yang et al., 2025), while GRPO (Shao et al., 2024) and its variants are particularly influential in optimizing outcome-level correctness. Upon these advances, RL has been increasingly extended to multimodal LLMs (Wang et al., 2025c; Huang et al., 2025; Leng et al., 2025; Meng et al., 2025; Yuan et al., 2025; Zhang et al., 2025; Chen et al., 2025a). However, these methods re---------------------------------------------------------------------------------
Under review as a conference paper at ICLR 2026 (https://openreview.net/pdf/bb337c066b2afde34451bb693ac3be5a62d8c187.pdf)
citeturn28114search13 [wordlim: 200] Published: 10 months ago; Under review as a conference paper at ICLR 2026 ... Figure 1: Overview diagram of the Video-KTR framework.
Under review as a conference paper at ICLR 2026

<visual_element id="e1">
Figure 1: Overview diagram of the Video-KTR framework. At the top, a video clip and the question “Which principle is introduced first in the video?” are fed into a Policy Model, producing Rollout / Original Rollout Tokens. An arrow labeled “Update with Important Tokens” leads to “Joint modeling of visual, temporal, and uncertainty signals.” The lower panel contains three modules: “Vision-Aware Counterfactual Reasoning,” “Temporal-Aware Counterfactual Reasoning,” and “Uncertainty-Aware – Entropy Analysis.” The visual module shows a masked video and token-pair logits shift calculation with “Visual-Aware Tokens: Exclude Tokens.” The temporal module shows shifted frames and token-pair logits shift calculation with “Temporal-Aware Tokens: Exclude Tokens.” The uncertainty module shows a token sequence with “High-Entropy Tokens: Exclude Tokens.”
</visual_element>

Figure 1: Overview of the Video-KTR framework. The model identifies key tokens based on entropy, visual, and temporal signals, and updates only those tokens during reinforcement learning.

3  METHODOLOGY

Recent RL work for Video-MLLMs (Feng et al., 2025; Chen et al., 2025b) mainly relies on coarse sequence-level rewards or simple token-level heuristics that capture only predictive uncertainty, without modeling video-specific structures like visual–temporal coherence or causal dependencies. In this work, we propose **Video-KTR**, a modality-aware policy shaping framework (Figure 1) that performs fine-grained RL through token-level attribution. We use counterfactual analysis to identify tokens conditioned on visual cues and temporal order, and exploit predictive entropy to detect reasoning-critical tokens. By selectively updating these tokens, Video-KTR amplifies reasoning-sensitive signals, improving both accuracy and interpretability.

3.1  MULTI-PERSPECTIVE TOKEN IMPORTANCE ANALYSIS

A central challenge in video reasoning is identifying which outputs truly rely on visual or temporal cues. --------------------------------------------------------------------------------
Video-KTR: Reinforcing Video Reasoning via Key Token Attribution (https://arxiv.org/abs/2601.19686)
citeturn28114academia14 [wordlim: 200] Published: 8 months ago; Date: Tue Jan 27 15:02:23 2026 ... By reinforcing only these key tokens, Video-KTR focuses learning on semantically informative, modality-sensitive content while filtering out low-value tokens.
Title: Video-KTR: Reinforcing Video Reasoning via Key Token Attribution
Authors: Ziyue Wang, Sheng Jin, Zhongrong Zuo, Jiawei Wu, Han Qiu, Qi She, Hao Zhang, Xudong Jiang
Date: Tue Jan 27 15:02:23 2026

Reinforcement learning (RL) has shown strong potential for enhancing reasoning in multimodal large language models, yet existing video reasoning methods often rely on coarse sequence-level rewards or single-factor token selection, neglecting fine-grained links among visual inputs, temporal dynamics, and linguistic outputs, limiting both accuracy and interpretability. We propose Video-KTR, a modality-aware policy shaping framework that performs selective, token-level RL by combining three attribution signals: (1) visual-aware tokens identified via counterfactual masking to reveal perceptual dependence; (2) temporal-aware tokens detected through frame shuffling to expose temporal sensitivity; and (3) high-entropy tokens signaling predictive uncertainty. By reinforcing only these key tokens, Video-KTR focuses learning on semantically informative, modality-sensitive content while filtering out low-value tokens. Across five challenging benchmarks, Video-KTR achieves state-of-the-art or highly competitive results, achieving 42.7\% on Video-Holmes (surpassing GPT-4o) with consistent gains on both reasoning and general video understanding tasks. Ablation studies verify the complementary roles of the attribution signals and the robustness of targeted token-level updates. Overall, Video-KTR improves accuracy and interpretability, offering a simple, drop-in extension to RL for complex video reasoning. Our code and models are available at https://github.com/zywang0104/Video-KTR.--------------------------------------------------------------------------------
GitHub - fvliang/DART: Official Implementation of DART (DART: Low-Latency Parallel Drafting with Continuity-Aware Tree Pruning for Speculative Decoding, EMNLP26). · GitHub (https://github.com/fvliang/DART)
citeturn28114search0 [wordlim: 200] Crawled: 2 weeks ago; DART is a new speculative decoding approach for Large Language Models (LLMs) inference, which is inspired by diffusion-based Large Language Models (dLLMs).

fvliang / DART Public

  * Notifications You must be signed in to change notification settings
  * Fork 3
  * Star

  * Code
  * Issues 3
  * Pull requests 0
  * Actions
  * Projects
  * Security and quality 0
  * Insights

## Latest commit

 

## History

30 Commits

## Folders and files

Name  | Name  | Last commit message  | Last commit date
--- | --- | --- | ---
dart.egg-info  | dart.egg-info  |    |  
dart  | dart  |    |  
figs  | figs  |    |  
third_party  | third_party  |    |  
.gitignore  | .gitignore  |    |  
.python-version  | .python-version  |    |  
LICENSE  | LICENSE  |    |  
README.md  | README.md  |    |  
main.py  | main.py  |    |  
pyproject.toml  | pyproject.toml  |    |  
uv.lock  | uv.lock  |    |  

### DART: Low-Latency Parallel Drafting with Continuity-Aware Tree Pruning for Speculative Decoding

[Paper of DART]

* * *

## Overview

DART is a new speculative decoding approach for Large Language Models (LLMs) inference, which is inspired by diffusion-based Large Language Models (dLLMs). DART surpasses EAGLE3 by 30% on average, achieving up to 65% improvement on certain code-centric workloads.

DART's drafting requires only a single forward pass of a single transformer layer and a fast cpp-based tree search to build the draft token tree, resulting in extremely low drafting cost while preserving relatively high $\tau$ (Average Acceptance Length).

## Citation

If you find DART useful in your research, please cite:
    
    @article{liu2026dart,
      title={DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference},
      author={Liu, Fuliang and Li, Xue and Zhao, Ketai and Gao, Yinxi and Zhou, Ziyan and Zhang, Zhonghui and Wang, Zhibin and Dou, Wanchun and Zhong, Sheng and Tian, Chen},
      journal={arXiv preprint arXiv:2601.19278},
      year={2026}
    }

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## About

Official Implementation of DART (DART: Low-Latency Parallel Drafting with Continuity-Aware Tree Pruning for Speculative Decoding, EMNLP26).

arxiv.org/abs/2601.19278

### Topics

large-language-modelsllm-inferencespeculative-decoding--------------------------------------------------------------------------------
DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference (https://arxiv.org/abs/2601.19278)
citeturn28114academia15 [wordlim: 200] Published: 8 months ago; Inspired by diffusion-based large language models (dLLMs), we propose DART, which leverages parallel generation to reduce drafting latency.
Title: DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference
Authors: Fuliang Liu, Xue Li, Ketai Zhao, Yinxi Gao, Ziyan Zhou, Zhonghui Zhang, Zhibin Wang, Wanchun Dou, Sheng Zhong, Chen Tian
Date: Tue Jan 27 07:04:24 2026

Speculative decoding is an effective and lossless approach for accelerating LLM inference. However, existing widely adopted model-based draft designs, such as EAGLE3, improve accuracy at the cost of multi-step autoregressive inference, resulting in high drafting latency and ultimately rendering the drafting stage itself a performance bottleneck. Inspired by diffusion-based large language models (dLLMs), we propose DART, which leverages parallel generation to reduce drafting latency. DART predicts logits for multiple future masked positions in parallel within a single forward pass based on hidden states of the target model, thereby eliminating autoregressive rollouts in the draft model while preserving a lightweight design. Based on these parallel logit predictions, we further introduce an efficient tree pruning algorithm that constructs high-quality draft token trees with N-gram-enforced semantic continuity. DART substantially reduces draft-stage overhead while preserving high draft accuracy, leading to significantly improved end-to-end decoding speed. Experimental results demonstrate that DART achieves a 2.03x--3.44x wall-clock time speedup across multiple datasets, surpassing EAGLE3 by 30% on average and offering a practical speculative decoding framework. Code is released at https://github.com/fvliang/DART.--------------------------------------------------------------------------------
Layer Verification Accelerates Speculative Tree Decoding (https://openreview.net/pdf/861a0763f6dd43acb432b81a5145443a8b0eeb1b.pdf)
citeturn28114search16 [wordlim: 200] Published: 4 months ago; In this section, we briefly review prior research on speculative decoding. ... Recently, parallel and diffusion-inspired drafters such as DART
A second line of work reduces or removes the need for a separate draft language model. Medusa (Cai et al., 2024) augments
the target model with multiple lightweight prediction heads; Hydra (Ankner et al., 2024) improves this head-based paradigm
by making draft heads sequentially dependent. Self-speculative methods instead reuse the target model itself, for example
by exiting at early layers and then verifying or correcting with the remaining layers (Elhoushi et al., 2024).
A third line focuses on the structure and efficiency of the draft itself. SEQUOIA (Chen et al., 2024) and adaptive-tree
methods (Wang et al., 2025) optimize draft-tree topology. Recently, parallel and diffusion-inspired drafters such as DART
(Liu et al., 2026) and DFlash (Chen et al., 2026) aim to reduce draft-stage latency by predicting multiple future positions in
parallel.
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
10--------------------------------------------------------------------------------
GitHub - zywang0104/Video-KTR · GitHub (https://github.com/zywang0104/Video-KTR)
citeturn28114search1 [wordlim: 200] Published: 8 months ago; Crawled: 2 months ago; Open more actions menu ... [📖 Paper]   [🤗 Video-KTR-7B-model] ...     @misc{wang2026videoktrreinforcingvideoreasoning,
> It identifies and amplifies critical visual--temporal tokens via selective gradient reinforcement, significantly improving video reasoning performance.

[📖 Paper]   [🤗 Video-KTR-7B-model]

[2026.01.26] 🎉Our work is accepted by ICLR 2026.

## 🌟 Highlights

  * 🚀 State-of-the-art performance on multiple video reasoning benchmarks (Video-Holmes, VideoMMMU, MMVU, VideoMME)
  * 🎯 Key Token Reinforcement (KTR): amplifies signal on high-entropy / visual-aware / temporal-aware tokens
  * 🔍 Better temporal and causal reasoning demonstrated by detailed case studies

Video-KTR improves video reasoning by identifying truly critical reasoning tokens. We use counterfactual probing (masking images or shuffling frames) to find

  * 👀 visual-aware tokens
  * ⏰ temporal-aware tokens
  * and apply entropy filtering to select uncertain but informative tokens.

During training, non-critical tokens are masked, and gradients are reinforced only on key tokens, enabling more stable and accurate temporal–causal reasoning.
    bash ../scripts/run_grpo_video_ktr.sh

* * *

## 🖍 Inference & Evaluation

Run evaluation on Video-Holmes / VideoMMMU / MMVU:
    
    bash ./src/eval_bench.sh

For infernce on a single example, you may use:
    
    python ./src/inference_example.py

* * *

## 📑 Citation

If you find our work helpful for your research, please consider citing our work.
    
    @misc{wang2026videoktrreinforcingvideoreasoning,
          title={Video-KTR: Reinforcing Video Reasoning via Key Token Attribution}, 
          author={Ziyue Wang and Sheng Jin and Zhongrong Zuo and Jiawei Wu and Han Qiu and Qi She and Hao Zhang and Xudong Jiang},
          year={2026},
          eprint={2601.19686},
          archivePrefix={arXiv},
          primaryClass={cs.CV},
          url={https://arxiv.org/abs/2601.19686}, 
    }

## About

No description, website, or topics provided.

### Resources

Readme

Activity

### Stars

11 stars

### Watchers

0 watching

### Forks

1 fork

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.--------------------------------------------------------------------------------
Accelerating Speculative Decoding with Block Diffusion Draft Trees (https://stagecons.app/?_=%2Fpdf%2F2604.12989%23sd0fmajmZdr%2FB3z7XN%2BOVL4%3D)
citeturn28114search17 [wordlim: 200] Published: 5 months ago; In Workshop on Large Language Model (LLM) Agents, ICLR, 2024. ... Dart: Diffusion-inspired speculative decoding for
Lott.
Recursive speculative decoding: Accelerating LLM inference via sampling without
replacement. In Workshop on Large Language Model (LLM) Agents, ICLR, 2024.
[9] Yunfan Xiong, Ruoyu Zhang, Yanzeng Li, and Lei Zou. Dyspec: Faster speculative decoding
with dynamic token tree structure. World Wide Web, 28(3):36, 2025.
[10] Xupeng Miao, Gabriele Oliaro, Zhihao Zhang, Xinhao Cheng, Zeyu Wang, Zhengxin Zhang, Rae
Ying Yee Wong, Alan Zhu, Lijie Yang, Xiaoxiang Shi, Chunan Shi, Zhuoming Chen, Daiyaan
Arfeen, Reyna Abhyankar, and Zhihao Jia. Specinfer: Accelerating large language model
serving with tree-based speculative inference and verification. ACM International Conference
on Architectural Support for Programming Languages and Operating Systems, 2023.
[11] Tianle Cai, Yuhong Li, Zhengyang Geng, Hongwu Peng, Jason D. Lee, Deming Chen, and Tri
Dao. Medusa: Simple LLM inference acceleration framework with multiple decoding heads. In
International Conference on Machine Learning, 2024.
[12] Yuhui Li, Fangyun Wei, Chao Zhang, and Hongyang Zhang. EAGLE: Speculative sampling
requires rethinking feature uncertainty. In International Conference on Machine Learning,
2024.
[13] Yuhui Li, Fangyun Wei, Chao Zhang, and Hongyang Zhang. Eagle-2: Faster inference of
language models with dynamic draft trees. In Conference on empirical methods in natural
language processing, pages 7421–7432, 2024.
[14] Zihao An, Huajun Bai, Ziqiong Liu, Dong Li, and Emad Barsoum. PARD: Accelerating LLM
inference with low-cost PARallel draft model adaptation. In International Conference on
Learning Representations, 2026.
[15] Fuliang Liu, Xue Li, Ketai Zhao, Yinxi Gao, Ziyan Zhou, Zhonghui Zhang, Zhibin Wang,
Wanchun Dou, Sheng Zhong, and Chen Tian. Dart: Diffusion-inspired speculative decoding for
fast llm inference. arXiv preprint arXiv:2601.19278, 2026.
[16] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang
Gao, Chengen Huang, Chenxu Lv, Chujie Zheng, Dayiheng Liu, Fan Zhou, Fei Huang, Feng
13--------------------------------------------------------------------------------
dblp: Xue Li 0024 (https://dblp.org/pid/181/2710-24.html)
citeturn28114search2 [wordlim: 200] Crawled: last month;       * electronic edition @ usenix.org (open access) ... DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference.
      * CiteSeerX
      * PubPeer

    * share record

      * Bluesky
      * Reddit
      * BibSonomy
      * LinkedIn

persistent URL:

      * https://dblp.org/rec/journals/corr/abs-2601-19278

Fuliang Liu, Xue Li, Ketai Zhao, Yinxi Gao, Ziyan Zhou, Zhonghui Zhang, Zhibin Wang, Wanchun Dou, Sheng Zhong, Chen Tian:
DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference. CoRR abs/2601.19278 (2026)
  * Image: Informal and Other Publications

[i13]

    * view

      * electronic edition via DOI (open access)
      * details & citations

authority control:

      *  

    * export record

      * BibTeX
      * RIS
      * RDF N-Triples
      * RDF Turtle
      * RDF/XML
      * XML
      * plain text

dblp key:

      * journals/corr/abs-2604-25899

    * ask others

      * Google
      * Google Scholar
      * Semantic Scholar
      * Internet Archive Scholar
      * CiteSeerX
      * PubPeer

--------------------------------------------------------------------------------
dblp: Zhonghui Zhang (https://dblp.org/pid/30/8494.html)
citeturn28114search3 [wordlim: 200] Crawled: 3 months ago; DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference. ...       * electronic edition via DOI (open access)

# Zhonghui Zhang

  * export bibliography

    * BibTeX
    * RIS
    * RDF N-Triples
    * RDF Turtle
    * RDF/XML
    * XML
    * RSS

dblp key:

    * homepages/30/8494

  * ask others

    * Google
    * Google Scholar
    * Semantic Scholar
    * Internet Archive Scholar
    * CiteSeerX
    * ORCID

  * share bibliography

    * Bluesky
    * Reddit
    * BibSonomy
    * LinkedIn

persistent URL:

    * https://dblp.org/pid/30/8494

  * help us

    * How can I correct errors in dblp?

## Person information

## Refine list

Image: note

refinements active!

zoomed in on ?? of ?? records

Imagedismiss all constraints

view refined list in

Imagedblp search

showing all ?? records

## 2020 – today

see FAQ


persistent URL:

      * https://dblp.org/rec/journals/corr/abs-2601-19278

Fuliang Liu, Xue Li, Ketai Zhao, Yinxi Gao, Ziyan Zhou, Zhonghui Zhang, Zhibin Wang, Wanchun Dou, Sheng Zhong, Chen Tian:
DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference. CoRR abs/2601.19278 (2026)
  * Image: Informal and Other Publications

[i5]

    * view

      * electronic edition via DOI (open access)
      * details & citations

--------------------------------------------------------------------------------
Video-KTR: Reinforcing Video Reasoning via Key Token Attribution | ZHANG HAO (https://26hzhang.github.io/publication/videoktr/)
citeturn28114search4 [wordlim: 200] Published: 9 months ago; Crawled: 3 weeks ago; January, 2026 ... By reinforcing only these key tokens, Video-KTR focuses learning on semantically informative, modality-sensitive content while filtering out low-value tokens.

# Video-KTR: Reinforcing Video Reasoning via Key Token Attribution

Ziyue Wang, Sheng Jin, Zhongrong Zuo, Jiawei Wu, Han Qiu, Qi She, Hao Zhang, Xudong Jiang

January, 2026

Preprint PDF Cite Code 📌ICLR'26

Image

### Abstract

Reinforcement learning (RL) has shown strong potential for enhancing reasoning in multimodal large language models, yet existing video reasoning methods often rely on coarse sequence-level rewards or single-factor token selection, neglecting fine-grained links among visual inputs, temporal dynamics, and linguistic outputs, limiting both accuracy and interpretability. We propose Video-KTR, a modality-aware policy shaping framework that performs selective, token-level RL by combining three attribution signals: (1) visual-aware tokens identified via counterfactual masking to reveal perceptual dependence; (2) temporal-aware tokens detected through frame shuffling to expose temporal sensitivity; and (3) high-entropy tokens signaling predictive uncertainty. By reinforcing only these key tokens, Video-KTR focuses learning on semantically informative, modality-sensitive content while filtering out low-value tokens. Across five challenging benchmarks, Video-KTR achieves state-of-the-art or highly competitive results, achieving 42.7% on Video-Holmes (surpassing GPT-4o) with consistent gains on both reasoning and general video understanding tasks. Ablation studies verify the complementary roles of the attribution signals and the robustness of targeted token-level updates. Overall, Video-KTR improves accuracy and interpretability, offering a simple, drop-in extension to RL for complex video reasoning.

Type

Conference paper

Publication

The Fourteenth International Conference on Learning Representations

##### Cite
    
    ``

Copy Download--------------------------------------------------------------------------------
dblp: Zhibin Wang 0002 (https://dblp.org/pid/67/1237-2.html)
citeturn28114search5 [wordlim: 200] Published: 4 weeks ago; Crawled: 4 weeks ago;       * electronic edition via DOI (open access) ... DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference.
      * Semantic Scholar
      * Internet Archive Scholar
      * CiteSeerX
      * PubPeer

    * share record

      * Bluesky
      * Reddit
      * BibSonomy
      * LinkedIn

persistent URL:

      * https://dblp.org/rec/journals/corr/abs-2601-19278

Fuliang Liu, Xue Li, Ketai Zhao, Yinxi Gao, Ziyan Zhou, Zhonghui Zhang, Zhibin Wang, Wanchun Dou, Sheng Zhong, Chen Tian:
DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference. CoRR abs/2601.19278 (2026)
  * Image: Informal and Other Publications

[i16]

    * view

      * electronic edition via DOI (open access)
      * details & citations
--------------------------------------------------------------------------------
dblp: Han Qiu 0019 (https://dblp.org/pid/428/0005)
citeturn28114search6 [wordlim: 200] Published: 5 months ago; Crawled: 5 months ago;   * 2026 ...       * electronic edition via DOI (open access) ... Video-KTR: Reinforcing Video Reasoning via Key Token Attribution.
      * Semantic Scholar
      * Internet Archive Scholar
      * CiteSeerX
      * PubPeer

    * share record

      * Bluesky
      * Reddit
      * BibSonomy
      * LinkedIn

persistent URL:

      * https://dblp.org/rec/journals/corr/abs-2601-19686

Ziyue Wang, Sheng Jin, Zhongrong Zuo, Jiawei Wu, Han Qiu, Qi She, Hao Zhang, Xudong Jiang:
Video-KTR: Reinforcing Video Reasoning via Key Token Attribution. CoRR abs/2601.19686 (2026)

## Coauthor Index

see FAQ

  * What is the meaning of the colors in the coauthor index?
  * How does dblp detect coauthor communities?

1

Xudong Jiang

[i1]

2

Sheng Jin

[i1]

3

Qi She

[i1]

4

Ziyue Wang

[i1]

5

Jiawei Wu

[i1]

6

Hao Zhang

[i1]

7

Zhongrong Zuo

[i1]

last updated on 2026-04-23 00:16 CEST by the dblp team

 all metadata released as open data under CC0 1.0 license--------------------------------------------------------------------------------
[Paper Note] Video-KTR: Reinforcing Video Reasoning via Key Token Attribution (https://en.papernotes.org/ICLR2026/video_understanding/video-ktr_reinforcing_video_reasoning_via_key_token_attribution/)
citeturn28114search7 [wordlim: 200] Crawled: 2 months ago; [ICLR 2026][Video Understanding][Video Reasoning] Ours proposes Video-KTR, a modality-aware policy shaping framework that identifies three types of key tokens—visual-aware, temporal-sensitive, and high-entropy—through counterfactual analysis.

[ICLR 2026][Video Understanding][Video Reasoning] Ours proposes Video-KTR, a modality-aware policy shaping framework that identifies three types of key tokens—visual-aware, temporal-sensitive, and high-entropy—through counterfactual analysis. By performing selective reinforcement learning updates only on these tokens, the method achieves SOTA performance on multiple video reasoning benchmarks (42.7% on Video-Holmes, surpassing GPT-4o).

Tags: ICLR 2026 · Video Understanding · Video Reasoning · Reinforcement Learning · Token Attribution · Multimodal LLM · GRPO

ICLR 2026 Video Understanding Video Reasoning Reinforcement Learning Token Attribution Multimodal LLM GRPO

# Video-KTR: Reinforcing Video Reasoning via Key Token Attribution¶

Conference: ICLR 2026
arXiv: 2601.19686
Area: Video Understanding
Keywords: Video Reasoning, Reinforcement Learning, Token Attribution, Multimodal LLM, GRPO

## TL;DR¶

Ours proposes Video-KTR, a modality-aware policy shaping framework that identifies three types of key tokens—visual-aware, temporal-sensitive, and high-entropy—through counterfactual analysis. --------------------------------------------------------------------------------
dblp: Sheng Zhong 0002 (https://dblp.uni-trier.de/pid/53/4506-2.html?view=by-type)
citeturn28114search8 [wordlim: 200] Published: last month; Crawled: last month; DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference. ...       * electronic edition via DOI (open access)
dblp key:

      * journals/corr/abs-2601-19278

    * ask others

      * Google
      * Google Scholar
      * Semantic Scholar
      * Internet Archive Scholar
      * CiteSeerX
      * PubPeer

    * share record

      * Bluesky
      * Reddit
      * BibSonomy
      * LinkedIn

persistent URL:

      * https://dblp.org/rec/journals/corr/abs-2601-19278

Fuliang Liu, Xue Li, Ketai Zhao, Yinxi Gao, Ziyan Zhou, Zhonghui Zhang, Zhibin Wang, Wanchun Dou, Sheng Zhong, Chen Tian:
DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference. CoRR abs/2601.19278 (2026)
--------------------------------------------------------------------------------
Video-KTR: Reinforcing Video Reasoning via Key Token Attribution | Computing Research Repository | DeepDyve (https://www.deepdyve.com/lp/arxiv/video-ktr-reinforcing-video-reasoning-via-key-token-attribution-dsUv2lSoR1)
citeturn28114search9 [wordlim: 200] Published: 8 months ago; Crawled: 3 months ago; # Video-KTR: Reinforcing Video Reasoning via Key Token Attribution ... Computing Research Repository·Jan 27, 2026
--------------------------------------------------------------------------------
ICLR 2026 Schedule (https://iclr.cc/virtual/2026/calendar)
citeturn28114search10 [wordlim: 200] Published: 5 months ago; Crawled: 6 months ago; Video-KTR: Reinforcing Video Reasoning via Key Token Attribution
--------------------------------------------------------------------------------
dblp: Zhongrong Zuo (https://dblp.uni-trier.de/pid/203/0857.html)
citeturn28114search11 [wordlim: 200] Published: 3 months ago; Crawled: 2 months ago; Video-KTR: Reinforcing Video Reasoning via Key Token Attribution.CoRR abs/2601.19686 (2026) ...       * electronic edition via DOI (open access)
--------------------------------------------------------------------------------
Published as a conference paper at ICLR 2026 (https://payshopp.net/?_=%2Fpdf%2F2601.19686%23oiIsiUa7YGXxkxUiKzZPY60%3D)
citeturn28114search18 [wordlim: 200] Published: 7 months ago; Published as a conference paper at ICLR 2026 ... 2.8 | 2-4 52.0 | 3-5 | 4-Video Vanill 3.0 | 5--KTR a GRPO 52.3
--------------------------------------------------------------------------------
DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference (https://www.znakschoola.ru/?_=%2Fpdf%2F2601.19278%23UE7DkG0PaBHZOakR54g1Wl8%3D)
citeturn28114search19 [wordlim: 200] Published: 7 months ago; DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference
--------------------------------------------------------------------------------
Frame Differential On-Policy Self-Distillation for Video Reasoning (https://arxiv.org/abs/2609.39021)
citeturn28114academia20 [wordlim: 200] Published: 3 days ago; Date: Wed Sep 30 05:25:59 2026 ... Across Qwen2.5-VL-7B and Qwen3-VL-4B on six video reasoning benchmarks, FD-OPSD yields higher overall average performance than the strongest corresponding GRPO, T-GRPO, or Video-KTR baselines across the 16, 32, and 64 frame evaluation settings.


Verifying your browser | OpenReview (https://openreview.net/forum?id=Br1uoB0Jiy)
citeturn28115view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://openreview.net/forum?id=Br1uoB0Jiy","lineno":null}); Redirected to URL: https://openreview.net/challenge?redirect=/forum?id%3DBr1uoB0Jiy; Total lines: 9
L0: # Verifying your browser
L1: 
L2: ## Complete the check below to continue to OpenReview
L3: 
L4: Please complete the verification above.
L5: 
L6: Have an OpenReview account? cite0†Sign in to skip this check.
L7: 
L8: cite1†OpenReview — Open Peer Review. Open Publishing. Open Access.
--------------------------------------------------------------------------------
ICLR 2026 Schedule (https://iclr.cc/virtual/2026/calendar)
citeturn28115view1 [wordlim: 200] Crawled: 7 months ago; Content type: text/html; Source: open({"ref_id":"https://iclr.cc/virtual/2026/calendar","lineno":null}); Total lines: 1080
L0: cite0†Skip to yearly menu bar cite1†Skip to main content L1: ## Main Navigation
L2: 
L3: cite2†  L4: 
L5:   * ICLR
L6:     * cite3† Help/FAQ  L7: 
L8: * * *
L9: 
L10:     * cite4† Contact ICLR  L11: 
L12: * * *
L13: 
L14:     * cite5† Downloads  L15: 
L16: * * *
L17: 
L18:     * cite6† ICLR Blog †blog.iclr.cc L19: 
L20: * * *
L21: 
L22:     * cite7† Code of Conduct  L23: 
L24: * * *
L25: 
L26:     * cite8† Privacy Policy  L27: 
L28: * * *
L29: 
L30:     * cite9† Create Profile  L31: 
L32: * * *
L33: 
L34:     * cite10† Reset Password  L35: 
L36: * * *
L37: 
L38:     * cite11† Journal To Conference Track  L39: 
L40: * * *
L41: 
L42:     * cite12† Diversity & Inclusion  L43: 
L44: * * *
L45: 
L46:     * cite13† Proceedings at OpenReview †openreview.net L47: 
L48: * * *
L49: 
L50:     * cite14† Future Meetings  L51: * * *
L52: 
L53:     * cite15† Press  L54: 
L55: * * *
L56: 
L57:     * cite16† Exhibitor Information  L58: 
L59: * * *
L60: 
L61:     * cite17† ICLR Twitter †twitter.com L62: 
L63: * * *
L64: 
L65:     * cite18† About ICLR  L66:   * cite19† My Stuff  L67: 
L68: cite20† Login L69: 
L70:   * Select Year: (2026)
L71:     * cite21†2026  L72: 
L73: * * *
L74: 
L75:     * cite22†2025  L76: 
L77: * * *
L78: 
L79:     * cite23†2024  L80: 
L81: * * *
L82: 
L83:     * cite24†2023  L84: 
L85: * * *
L86: 
L87:     * cite25†2022  L88: 
L89: * * *
L90: 
L91:     * cite26†2021  L92: 
L93: * * *
L94: 
L95:     * cite27†2020  L96: 
L97: * * *
L98: 
L99:     * cite28†2019  L100: 
L101: * * *
L102: 
L103:     * cite29†2018  L104: 
L105: * * *
L106: 
L107:     * cite30†2017  L108: 
L109: * * *
L110: 
L111:     * cite31†2016  L112: 
L113: * * *
L114:     * cite32†2015  L115: 
L116: * * *
L117: 
L118:     * cite33†2014  L119: 
L120: * * *
L121: 
L122:     * cite34†2013  L123:   * cite35† Getting Started  L124:   * cite36† Schedule  L125:   * Main Conference
L126:     * cite37† Invited Talks  L127: 
L128: * * *
L129: 
L130:     * cite38† Awards  L131: 
L132: * * *
L133: 
L134:     * cite39† Papers  L135: 
L136: * * *
L137: 
L138:     * cite40† In-person Orals  L139: 
L140: * * *
L141: 
L142:     * cite41† Blog Track Posters  L143:   * cite42† Workshops  L144:   * Community
L145:     * cite43† Town Hall  L146: 
L147: * * *
L148: 
L149:     * cite44† Socials  L150:   * cite45† Sponsors  L151:   * cite46† Organizers  L152:   * cite47†  L153:   * Help
L154:     * Getting Started
L155: 
L156:   Show Detail
L157: cite36†Schedule cite48†Thu  cite49†Fri  cite50†Sat  cite51†Sun  cite52†Mon  L158: 
L159: Timezone: America/Sao_Paulo
L160: 
L161: Filter Events   Oral Session Poster Session Workshop
L162: 
L163:  Filter Rooms:
L164: 
L165: THU 23 APR
L166: 
L167: 10:30 a.m.
L168: 
L169: cite53†Oral Session 1A [10:30-12:00]  L170: 
L171: Oral s 10:30-11:40
L172: 
L173: [10:30] Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling
L174: 
L175: [10:42] $\mathbf{T^3}$: Reducing Belief Deviation in Reinforcement Learning for Active Reasoning
L176: [10:54] MemAgent: Reshaping Long-Context LLM with Multi-Conv RL-based Memory Agent
L177: 
L178: [11:06] Verifying Chain-of-Thought Reasoning via its Computational Graph
L179: 
L180: [11:18] Revela: Dense Retriever Learning via Language Modeling
L181: 
L182: [11:30] RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format
L183: 
L184: (ends 12:00 PM)
L185: 
L186: cite54†Oral Session 1B [10:30-12:00]  L187: 
L188: Oral s 10:30-11:52
L189: [10:30] Half-order Fine-Tuning for Diffusion Model: A Recursive Likelihood Ratio Optimizer
L190: 
L191: [10:42] Improving Diffusion Models for Class-imbalanced Training Data via Capacity Manipulation
L192: 
L193: [10:54] Let Features Decide Their Own Solvers: Hybrid Feature Caching for Diffusion Transformers
L194: 
L195: [11:06] DiffusionNFT: Online Diffusion Reinforcement with Forward Process
L196: 
L197: [11:18] Universal Inverse Distillation for Matching Models with Real-Data Supervision (No GANs)
L198: [11:30] GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models
L199: 
L200: [11:42] Neon: Negative Extrapolation From Self-Training Improves Image Generation
L201: 
L202: (ends 12:00 PM)
L203: 
L204: cite55†Oral Session 1C [10:30-12:00]  L205: 
L206: Oral s 10:30-11:16
L207: 
L208: [10:30] Mastering Sparse CUDA Generation through Pretrained Models and Deep Reinforcement Learning
L209: 
L210: [10:42] RefineStat: Efficient Exploration for Probabilistic Program Synthesis
L211: [10:54] Huxley-G\"odel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine
L212: 
L213: [11:06] TileLang: Bridge Programmability and Performance in Modern Neural Kernels
L214: 
L215: (ends 12:00 PM)
L216: 
L217: cite56†Oral Session 1D [10:30-12:00]  L218: 
L219: Oral s 10:30-11:52
L220: 
L221: [10:30] One for Two: A Unified Framework for Imbalanced Graph Classification via Dynamic Balanced Prototype
L222: 
L223: [10:42] Compactness and Consistency: A Conjoint Framework for Deep Graph Clustering
L224: [10:54] Actions Speak Louder than Prompts: A Large-Scale Study of LLMs for Graph Inference
L225: 
L226: [11:06] Multi-Domain Transferable Graph Gluing for Building Graph Foundation Models
L227: 
L228: [11:18] Modality-free Graph In-context Alignment
L229: 
L230: [11:30] Learning with Dual-level Noisy Correspondence for Multi-modal Entity Alignment
L231: 
L232: [11:42] Exchangeability of GNN Representations with Applications to Graph Retrieval
L233: 
L234: (ends 12:00 PM)
L235: 
L236: cite57†Oral Session 1E [10:30-12:00]  L237: 
L238: Oral s 10:30-11:52
L239: [10:30] Information Shapes Koopman Representation
L240: 
L241: [10:42] On The Surprising Effectiveness of a Single Global Merging in Decentralized Learning
L242: 
L243: [10:54] Similarity-aware Non-Convex Federated Optimization
L244: 
L245: [11:06] On the Wasserstein Geodesic Principal Component Analysis of probability measures
L246: 
L247: [11:18] Fast Escape, Slow Convergence: Learning Dynamics of Phase Retrieval under Power-Law Data
L248: 
L249: [11:30] Hyperparameter Trajectory Inference with Conditional Lagrangian Optimal Transport
L250: [11:42] Gaussian certified unlearning in high dimensions: A hypothesis testing approach
L251: 
L252: (ends 12:00 PM)
L253: 
L254: cite58†Oral Session 1F [10:30-12:00]  L255: 
L256: Oral s 10:30-11:52
L257: 
L258: [10:30] Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models
L259: 
L260: [10:42] Invisible Safety Threat: Malicious Finetuning for LLM via Steganography
L261: 
L262: [10:54] The Shape of Adversarial Influence: Characterizing LLM Latent Spaces with Persistent Homology
L263: [11:06] Watch your steps: Dormant Adversarial Behaviors that Activate upon LLM Finetuning
L264: 
L265: [11:18] LLM Fingerprinting via Semantically Conditioned Watermarks
L266: 
L267: [11:30] Steering the Herd: A Framework for LLM-based Control of Social Learning
L268: 
L269: [11:42] Every Language Model Has a Forgery-Resistant Signature
L270: 
L271: (ends 12:00 PM)
L272: 
L273: cite59†Poster Session 1 [10:30-1:00]  L274: 
L275: (ends 1:00 PM)
L276: 
L277: 3:15 p.m.
L278: 
L279: cite60†Oral Session 2A [3:15-4:45]  L280: 
L281: Oral s 3:15-4:37
L282: [3:15] LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning
L283: 
L284: [3:27] EmotionThinker: Prosody-Aware Reinforcement Learning for Explainable Speech Emotion Reasoning
L285: 
L286: [3:39] Token-Importance Guided Direct Preference Optimization
L287: 
L288: [3:51] P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling
L289: 
L290: [4:03] Reasoning without Training: Your Base Model is Smarter Than You Think
L291: 
L292: [4:15] LoongRL: Reinforcement Learning for Advanced Reasoning over Long Contexts
L293: [4:27] Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training
L294: 
L295: (ends 4:45 PM)
L296: 
L297: cite61†Oral Session 2B [3:15-4:45]  L298: 
L299: Oral s 3:15-4:37
L300: 
L301: [3:15] High-dimensional Analysis of Synthetic Data Selection
L302: 
L303: [3:27] How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability
L304: 
L305: [3:39] Sequences of Logits Reveal the Low Rank Structure of Language Models
L306: 
L307: [3:51] Intrinsic Entropy of Context Length Scaling in LLMs
L308: [4:03] From Markov to Laplace: How Mamba In-Context Learns Markov Chains
L309: 
L310: [4:15] The Coverage Principle: How Pre-Training Enables Post-Training
L311: 
L312: [4:27] Quantitative Bounds for Length Generalization in Transformers
L313: 
L314: (ends 4:45 PM)
L315: 
L316: cite62†Oral Session 2C [3:15-4:45]  L317: 
L318: Oral s 3:15-4:37
L319: 
L320: [3:15] Reasoning as Representation: Rethinking Visual Reinforcement Learning in Image Quality Assessment
L321: 
L322: [3:27] Veritas: Generalizable Deepfake Detection via Pattern-Aware Reasoning
L323: [3:39] On the Generalization Capacities of MLLMs for Spatial Intelligence
L324: 
L325: [3:51] DepthLM: Metric Depth from Vision Language Models
L326: 
L327: [4:03] FlashVID: Efficient Video Large Language Models via Training-free Tree-based Spatiotemporal Token Merging
L328: 
L329: [4:15] Multimodal Aligned Semantic Knowledge for Unpaired Image-text Matching
L330: 
L331: [4:27] Vid-LLM: A Compact Video-based 3D Multimodal LLM with Reconstruction–Reasoning Synergy
L332: 
L333: (ends 4:45 PM)
L334: 
L335: cite63†Oral Session 2D [3:15-4:45]  L336: 
L337: Oral s 3:15-4:37
L338: [3:15] Beyond Prompt-Induced Lies: Investigating LLM Deception on Benign Prompts
L339: 
L340: [3:27] Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort
L341: 
L342: [3:39] LLMs Get Lost In Multi-Turn Conversation
L343: 
L344: [3:51] How Reliable is Language Model Micro-Benchmarking?
L345: 
L346: [4:03] AdAEM: An Adaptively and Automated Extensible Evaluation Method of LLMs' Value Difference
L347: 
L348: [4:15] What's In My Human Feedback? Learning Interpretable Descriptions of Preference Data
L349: [4:27] EigenBench: A Comparative Behavioral Measure of Value Alignment
L350: 
L351: (ends 4:45 PM)
L352: 
L353: cite64†Oral Session 2E [3:15-4:45]  L354: 
L355: Oral s 3:15-4:37
L356: 
L357: [3:15] Generative Human Geometry Distribution
L358: 
L359: [3:27] Depth Anything 3: Recovering the Visual Space from Any Views
L360: 
L361: [3:39] Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator
L362: 
L363: [3:51] Monocular Normal Estimation via Shading Sequence Estimation
L364: 
L365: [4:03] Radiometrically Consistent Gaussian Surfels for Inverse Rendering
L366: [4:15] True Self-Supervised Novel View Synthesis is Transferable
L367: 
L368: [4:27] cadrille: Multi-modal CAD Reconstruction with Reinforcement Learning
L369: 
L370: (ends 4:45 PM)
L371: 
L372: cite65†Oral Session 2F [3:15-4:45]  L373: 
L374: Oral s 3:15-4:37
L375: 
L376: [3:15] Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning
L377: 
L378: [3:27] Probabilistic Kernel Function for Fast Angle Testing
L379: 
L380: [3:39] Differentially Private Domain Discovery
L381: [3:51] Causal Structure Learning in Hawkes Processes with Complex Latent Confounder Networks
L382: 
L383: [4:03] Temporal Sparse Autoencoders: Leveraging the Sequential Nature of Language for Interpretability
L384: 
L385: [4:15] A Representer Theorem for Hawkes Processes via Penalized Least Squares Minimization
L386: 
L387: [4:27] Cross-Domain Lossy Compression via Rate- and Classification-Constrained Optimal Transport
L388: 
L389: (ends 4:45 PM)
L390: 
L391: cite66†Poster Session 2 [3:15-5:45]  L392: 
L393: (ends 5:45 PM)
L394: 
L395: FRI 24 APR
L396: 
L397: 10:30 a.m.
L398: cite67†Oral Session 3A [10:30-12:00]  L399: 
L400: Oral s 10:30-11:52
L401: 
L402: [10:30] ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data
L403: 
L404: [10:42] Shoot First, Ask Questions Later? Building Rational Agents that Explore and Act Like People
L405: 
L406: [10:54] In-The-Flow Agentic System Optimization for Effective Planning and Tool Use
L407: 
L408: [11:06] Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments
L409: [11:18] AgentGym-RL: An Open-Source Framework to Train LLM Agents for Long-Horizon Decision Making via Multi-Turn RL
L410: 
L411: [11:30] GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
L412: 
L413: [11:42] Speculative Actions: A Lossless Framework for Faster AI Agents
L414: 
L415: (ends 12:00 PM)
L416: 
L417: cite68†Oral Session 3B [10:30-12:00]  L418: 
L419: Oral s 10:30-11:52
L420: 
L421: [10:30] Locality-aware Parallel Decoding for Efficient Autoregressive Image Generation
L422: [10:42] SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer
L423: 
L424: [10:54] Partition Generative Modeling: Masked Modeling Without Masks
L425: 
L426: [11:06] NextStep-1: Toward Autoregressive Image Generation with Continuous Tokens at Scale
L427: 
L428: [11:18] TTSDS2: Resources and Benchmark for Evaluating Human-Quality Text to Speech Systems
L429: 
L430: [11:30] VibeVoice: Expressive Podcast Generation with Next-Token Diffusion
L431: [11:42] UALM: Unified Audio Language Model for Understanding, Generation and Reasoning
L432: 
L433: (ends 12:00 PM)
L434: 
L435: cite69†Oral Session 3C [10:30-12:00]  L436: 
L437: Oral s 10:30-11:52
L438: 
L439: [10:30] Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation
L440: 
L441: [10:42] WSM: Decay-Free Learning Rate Schedule via Checkpoint Merging for LLM Pre-training
L442: 
L443: [10:54] Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks
L444: [11:06] How Learning Rate Decay Wastes Your Best Data in Curriculum-Based LLM Pretraining
L445: 
L446: [11:18] In-Place Test-Time Training
L447: 
L448: [11:30] Softmax Transformers are Turing-Complete
L449: 
L450: [11:42] Pre-training under infinite compute
L451: 
L452: (ends 12:00 PM)
L453: 
L454: cite70†Oral Session 3D [10:30-12:00]  L455: 
L456: Oral s 10:30-11:28
L457: 
L458: [10:30] MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Models for Embodied Task Planning
L459: 
L460: [10:42] Generative Universal Verifier as Multimodal Meta-Reasoner
L461: [10:54] Visual Planning: Let's Think Only with Images
L462: 
L463: [11:06] MC-Search: Evaluating and Enhancing Multimodal Agentic Search with Structured Long Reasoning Chains
L464: 
L465: [11:18] Omni-Reward: Towards Generalist Omni-Modal Reward Modeling with Free-Form Preferences
L466: 
L467: (ends 12:00 PM)
L468: 
L469: cite71†Oral Session 3E [10:30-12:00]  L470: 
L471: Oral s 10:30-11:40
L472: 
L473: [10:30] The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm
L474: [10:42] Temporal superposition and feature geometry of RNNs under memory demands
L475: 
L476: [10:54] Scaling Laws and Spectra of Shallow Neural Networks in the Feature Learning Regime
L477: 
L478: [11:06] Efficient Resource-Constrained Training of Vision Transformers via Subspace Optimization
L479: 
L480: [11:18] Why Low-Precision Transformer Training Fails: An Analysis on Flash Attention
L481: 
L482: [11:30] HATSolver: Learning Gröbner Bases with Hierarchical Attention Transformers
L483: 
L484: (ends 12:00 PM)
L485: 
L486: cite72†Oral Session 3F [10:30-12:00]  L487: Oral s 10:30-11:40
L488: 
L489: [10:30] Extending Sequence Length is Not All You Need: Effective Integration of Multimodal Signals for Gene Expression Prediction
L490: 
L491: [10:42] Premise Selection for a Lean Hammer
L492: 
L493: [10:54] Exploring Synthesizable Chemical Space with Iterative Pathway Refinements
L494: 
L495: [11:06] mCLM: A Modular Chemical Language Model that Generates Functional and Makeable Molecules
L496: 
L497: [11:18] It's All Just Vectorization: einx, a Universal Notation for Tensor Operations
L498: [11:30] Exploratory Causal Inference in SAEnce
L499: 
L500: (ends 12:00 PM)
L501: 
L502: cite73†Poster Session 3 [10:30-1:00]  L503: 
L504: (ends 1:00 PM)
L505: 
L506: 3:15 p.m.
L507: 
L508: cite74†Oral Session 4A [3:15-4:45]  L509: 
L510: Oral s 3:15-4:25
L511: 
L512: [3:15] ThinKV: Thought-Adaptive KV Cache Compression for Efficient Reasoning Models
L513: 
L514: [3:27] MrRoPE: Mixed-radix Rotary Position Embedding
L515: 
L516: [3:39] Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss
L517: 
L518: [3:51] FlashRNN: Unlocking Parallel Training of Nonlinear RNNs for Large Language Models
L519: [4:03] Mamba-3: Improved Sequence Modeling using State Space Principles
L520: 
L521: [4:15] Energy-Based Transformers are Scalable Learners and Thinkers
L522: 
L523: (ends 4:45 PM)
L524: 
L525: cite75†Oral Session 4B [3:15-4:45]  L526: 
L527: Oral s 3:15-4:37
L528: 
L529: [3:15] WoW!: World Models in a Closed-Loop World
L530: 
L531: [3:27] Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling
L532: 
L533: [3:39] Exploratory Diffusion Model for Unsupervised Reinforcement Learning
L534: [3:51] Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation
L535: 
L536: [4:03] Rodrigues Network for Learning Robot Actions
L537: 
L538: [4:15] Pareto-Conditioned Diffusion Models for Offline Multi-Objective Optimization
L539: 
L540: [4:27] Compositional Diffusion with Guided search for Long-Horizon Planning
L541: 
L542: (ends 4:45 PM)
L543: 
L544: cite76†Oral Session 4C [3:15-4:45]  L545: 
L546: Oral s 3:15-4:37
L547: 
L548: [3:15] Learning to See Before Seeing: Demystifying LLM Visual Priors from Language Pre-training
L549: [3:27] Hallucination Begins Where Saliency Drops
L550: 
L551: [3:39] Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs
L552: 
L553: [3:51] MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction
L554: 
L555: [4:03] Seeing Through the Brain: New Insights from Decoding Visual Stimuli with fMRI
L556: 
L557: [4:15] WAVE: Learning Unified & Versatile Audio-Visual Embeddings with Multimodal LLM
L558: 
L559: [4:27] Visual symbolic mechanisms: Emergent symbol processing in Vision Language Models
L560: 
L561: (ends 4:45 PM)
L562: cite77†Oral Session 4D [3:15-4:45]  L563: 
L564: Oral s 3:15-4:25
L565: 
L566: [3:15] SWINGARENA: Adversarial Programming Arena for Long-context GitHub Issue Solving
L567: 
L568: [3:27] BIRD-INTERACT: Re-imagining Text-to-SQL Evaluation via Lens of Dynamic Interactions
L569: 
L570: [3:39] EditBench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits
L571: 
L572: [3:51] Agent Data Protocol
L573: 
L574: [4:03] AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite
L575: [4:15] MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science
L576: 
L577: (ends 4:45 PM)
L578: 
L579: cite78†Oral Session 4E [3:15-4:45]  L580: 
L581: Oral s 3:15-4:01
L582: 
L583: [3:15] OpenThoughts: Data Recipes for Reasoning Models
L584: 
L585: [3:27] FRABench and UFEval: Unified Fine-grained Evaluation with Task and Aspect Generalization
L586: 
L587: [3:39] SimuHome: A Temporal- and Environment-Aware Benchmark for Smart Home LLM Agents
L588: [3:51] Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training
L589: 
L590: (ends 4:45 PM)
L591: 
L592: cite79†Poster Session 4 [3:15-5:45]  L593: 
L594: (ends 5:45 PM)
L595: 
L596: SAT 25 APR
L597: 
L598: 10:30 a.m.
L599: 
L600: cite80†Oral Session 5A [10:30-12:00]  L601: 
L602: Oral s 10:30-11:52
L603: 
L604: [10:30] Diffusion Language Model Knows the Answer Before It Decodes
L605: 
L606: [10:42] On the Reasoning Abilities of Masked Diffusion Language Models
L607: 
L608: [10:54] Planner Aware Path Learning in Diffusion Language Models Training
L609: [11:06] Global Resolution: Optimal Multi-Draft Speculative Sampling via Convex Optimization
L610: 
L611: [11:18] Overcoming Joint Intractability with Lossless Hierarchical Speculative Decoding
L612: 
L613: [11:30] $p\textrm{-less}$ Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding
L614: 
L615: [11:42] Latent Speech-Text Transformer
L616: 
L617: (ends 12:00 PM)
L618: 
L619: cite81†Oral Session 5B [10:30-12:00]  L620: 
L621: Oral s 10:30-11:52
L622: 
L623: [10:30] Stable Video Infinity: Infinite-Length Video Generation with Error Recycling
L624: [10:42] Instilling an Active Mind in Avatars via Cognitive Simulation
L625: 
L626: [10:54] FlashWorld: High-quality 3D Scene Generation within Seconds
L627: 
L628: [11:06] MotionStream: Real-Time Video Generation with Interactive Motion Controls
L629: 
L630: [11:18] EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning
L631: 
L632: [11:30] $PhyWorldBench$: A Comprehensive Evaluation of Physical Realism in Text-to-Video Models
L633: 
L634: [11:42] TRACE: Your Diffusion Model is Secretly an Instance Edge Detector
L635: 
L636: (ends 12:00 PM)
L637: cite82†Oral Session 5C [10:30-12:00]  L638: 
L639: Oral s 10:30-11:52
L640: 
L641: [10:30] Semi-Supervised Preference Optimization with Limited Feedback
L642: 
L643: [10:42] TROLL: Trust Regions Improve Reinforcement Learning for Large Language Models
L644: 
L645: [10:54] Multiplayer Nash Preference Optimization
L646: 
L647: [11:06] The Art of Scaling Reinforcement Learning Compute for LLMs
L648: 
L649: [11:18] To Infinity and Beyond: Tool-Use Unlocks Length Generalization in State Space Models
L650: [11:30] SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety
L651: 
L652: [11:42] Why DPO is a Misspecified Estimator and How to Fix It
L653: 
L654: (ends 12:00 PM)
L655: 
L656: cite83†Oral Session 5D [10:30-12:00]  L657: 
L658: Oral s 10:30-11:52
L659: 
L660: [10:30] Difficult Examples Hurt Unsupervised Contrastive Learning: A Theoretical Perspective
L661: 
L662: [10:42] Characterizing the Discrete Geometry of ReLU Networks
L663: 
L664: [10:54] InfoNCE Induces Gaussian Distribution
L665: 
L666: [11:06] Navigating the Latent Space Dynamics of Neural Models
L667: [11:18] Overparametrization bends the landscape: BBP transitions at initialization in simple Neural Networks
L668: 
L669: [11:30] Addressing divergent representations from causal interventions on neural networks
L670: 
L671: [11:42] FIRE: Frobenius-Isometry Reinitialization for Balancing the Stability–Plasticity Tradeoff
L672: 
L673: (ends 12:00 PM)
L674: 
L675: cite84†Oral Session 5E [10:30-12:00]  L676: 
--------------------------------------------------------------------------------
ICLR 2026 Schedule (https://iclr.cc/virtual/2026/calendar)
citeturn28115view2 [wordlim: 200] Crawled: 7 months ago; Content type: text/html; Source: find({"ref_id":"https://iclr.cc/virtual/2026/calendar","pattern":"Video-KTR"}); Total lines: 1080
No matching text found for "Video-KTR"

Published as a conference paper at ICLR 2026 (https://openreview.net/pdf?id=p0sDIEsYG3)
citeturn28116search0 [wordlim: 200] Published: 4 months ago; Open-Source MLLMs ... Video-KTR
Published as a conference paper at ICLR 2026
Table 1: Performance comparison across reasoning-oriented and general-purpose video benchmarks,
where * indicates scores evaluated by ourselves.
Models
Size # Frames
Video Reasoning Benchmark
Video General Benchmark
Video-Holmes VideoMMMU MMVU(mc) TempCompass VideoMME
Proprietary MLLMs
GPT-4o
–
–
42.0
61.2
75.4
73.8
71.9
GPT-5
–
–
46.7∗
84.6
82.6∗
83.3∗
86.7
Gemini-1.5-Pro
–
–
41.3
53.4
71.2
67.1
75.0
Gemini-2.5-Pro
–
–
45.0
83.6
78.4∗
84.3∗
84.3
Open-Source MLLMs
LLaVA-OV
7B
64
–
33.8
49.2
64.2
58.2
VILA-1.5
8B
64
–
33.8
49.2
58.8
58.2
Qwen2.5-VL
7B
–
27.8
47.4
59.2
67.9
65.1
Video-R1
7B
32
36.5
52.3
63.8
73.2
59.3
Video-RTS
7B
51.2
40.7
52.7
66.4
–
63.0
TW-GRPO
7B
16
32.9
51.3
65.8
73.3
55.1
SFT Models
Qwen2.5-VL-SFT
7B
16
31.7
47.4
61.3
69.2
52.8
32
33.9
49.4
63.5
69.9
55.4
64
33.7
49.4
61.6
70.0
58.8
Video-KTR
7B
16
40.7
51.3
65.7
73.3
57.3
32
41.6
52.6
65.9
73.4
60.3
64
42.7
53.1
66.6
73.5
62.5
Benchmarks.
To comprehensively assess the performance of Video-KTR, we select five chal-
lenging video benchmarks: (1) reasoning-oriented benchmarks, including Video-Holmes (Cheng
et al., 2025), VideoMMMU (Hu et al., 2025), and MMVU (Zhao et al., 2025), to assess the tem-
poral, causal, and knowledge-intensive reasoning capability of MLLMs; (2) general understanding
benchmarks, including TempCompass (Liu et al., 2024) and VideoMME (Fu et al., 2025). Note
Video-Holmes is a newly established benchmark that poses significant challenges, requiring models
to integrate dispersed narrative cues from suspenseful short films and perform complex deductive
reasoning beyond basic visual recognition.
Baselines.
We compare Video-KTR against a diverse set of baselines, encompassing both general-
purpose and reasoning-oriented MLLMs of similar size: LLaVA-OneVision (LLaVA-OV; Li et al.
(2025a)), VILA-1.5 (Liu et al., 2025), Qwen2.5-VL (Bai et al., 2025), Video-R1 (Feng et al., 2025),
Video-RTS (Wang et al., 2025d), and TW-GRPO (Dang et al., 2025).
4.2
RESULTS AND ANALYSIS
Comparison with state-of-the-art models.
We evaluate Video-KTR against a diverse set of video
reasoning models on three reasoning and two general video understanding benchmarks. Reported
in Table 1, Video-KTR consistently achieves state-of-the-art results. On Video-Holmes—which
targets high-level temporal and social reasoning in short films—our model attains 42.7%, surpass-
ing all open-source baselines and closely matching proprietary models like GPT-5 (OpenAI (2025);
46.7%) and Gemini-2.5-Pro (Comanici et al. (2025); 45.0%). On knowledge-intensive benchmarks,
i.e., MMVU(mc) and VideoMMMU, Video-KTR achieves 66.6% and 53.1%, respectively, high-
lighting its strength in complex reasoning. Video-KTR also delivers competitive performance on
general video understanding, showing that improved reasoning does not compromise broad compre-
hension. Notably, accuracy increases steadily with more input frames (16 to 64), underscoring the
scalability and robustness of our token-aware RL for longer temporal sequences.
Research Question (RQ1): How effective is Video-KTR compared with other video RL meth-
ods?
To isolate the effect of training data and recipe, we conduct a controlled study where all
6--------------------------------------------------------------------------------
Under review as a conference paper at ICLR 2026 (https://openreview.net/pdf/bb337c066b2afde34451bb693ac3be5a62d8c187.pdf)
citeturn28116search1 [wordlim: 200] Published: 10 months ago; Under review as a conference paper at ICLR 2026VIDEO-KTR: REINFORCING VIDEO REASONING VIA KEY TOKEN ATTRIBUTION
Under review as a conference paper at ICLR 2026

VIDEO-KTR: REINFORCING VIDEO REASONING VIA KEY TOKEN ATTRIBUTION

Anonymous authors  
Paper under double-blind review

ABSTRACT

Reinforcement learning (RL) has shown strong potential for enhancing reasoning in multimodal large language models, yet existing video reasoning methods often rely on coarse sequence-level rewards or single-factor token selection, neglecting fine-grained links among visual inputs, temporal dynamics, and linguistic outputs, limiting both accuracy and interpretability. We propose Video-KTR, a modality-aware policy shaping framework that performs selective, token-level RL by combining three attribution signals: (1) visual-aware tokens identified via counterfactual masking to reveal perceptual dependence; (2) temporal-aware tokens detected through frame shuffling to expose temporal sensitivity; and (3) high-entropy tokens signaling predictive uncertainty. By reinforcing only these key tokens, Video-KTR focuses learning on semantically informative, modality-sensitive content while filtering out low-value tokens. Across five challenging benchmarks, Video-KTR achieves state-of-the-art or highly competitive results—42.7% on Video-Holmes (surpassing GPT-4o)—with consistent gains on both reasoning and general video understanding tasks. Ablation studies verify the complementary roles of the attribution signals and the robustness of targeted token-level updates. Overall, Video-KTR improves accuracy and interpretability, offering a simple, drop-in extension to RL for complex video reasoning.

1 INTRODUCTION

Reinforcement learning (RL) has emerged as a powerful paradigm for enhancing long-chain reasoning in large language models (LLMs) (OpenAI, 2024; DeepSeek-AI, 2025; Yang et al., 2025). In particular, GRPO (Shao et al., 2024) exhibits strong performance on complex reasoning tasks. Building on this success, RL has been extended to multimodal LLMs (MLLMs), achieving notable gains on visual understanding through sample diversification (Wang et al., 2025a; Leng et al., 2025), tailored reward design (Tan et al., 2025; Shen et al., 2025), and advanced optimization strategies (Deng et al., 2025; Zhang et al., 2025a; Dang et al., 2025). Yet, these advances primarily target static images, leaving video reasoning comparatively underexplored. Recent work mitigates this gap by integrating temporal supervision, e.g., contrasting predictions on ordered and shuffled frames, to strengthen temporal sensitivity (Feng et al., 2025), and by embedding spatio-temporal priors into reward mechanisms to better align spatial grounding with temporal ordering (Li et al., 2025; Sun et al., 2025). Other studies build RL-driven tool agents capable of decomposing and solving long-form video queries (Tian et al., 2025), as well as scalable reward designs that adapt to video complexity via difficulty-aware or temporally robust objectives (Park et al., 2025; Chen et al., 2025b).

However, video reasoning still struggles to accurately model temporal dynamics and exploit visual cues. Many approaches overlook explicit temporal dependencies and causal structures—essential for effective reasoning (Tian et al., 2025; Huang et al., 2025). Some methods (Feng et al., 2025) introduce temporal-specific constraints, such as penalizing predictions on shuffled frames, yet these rely on coarse global assumptions. This design ignores tasks solvable by static cues, introducing optimization noise that may hinder training.--------------------------------------------------------------------------------
Under review as a conference paper at ICLR 2026 (https://openreview.net/pdf/52b2a9ecc22a78a74ba17f311cdda23e104aae61.pdf)
citeturn28116search2 [wordlim: 200] Published: 11 months ago; Under review as a conference paper at ICLR 2026 ... Open-Source MLLMs ... Video-KTR
Under review as a conference paper at ICLR 2026
Table 1: Performance comparison across video reasoning and general video benchmarks.
Models
Size # Frames
Video Reasoning Benchmark
Video General Benchmark
235
236
237
238
Video-Holmes VideoMMMU MMVU(mc) TempCompass VideoMME
Proprietary MLLMs
GPT-4o
–
–
42.0
61.2
75.4
73.8
71.9
Gemini-1.5-Pro
–
–
41.3
53.4
71.2
67.1
75.0
239
240
241
242
243
244
Open-Source MLLMs
LLaVA-OV
7B
64
–
33.8
49.2
64.2
58.2
VILA-1.5
8B
64
–
33.8
49.2
58.8
58.2
Qwen2.5-VL
7B
–
27.8
47.4
59.2
67.9
65.1
Video-R1
7B
32
36.5
52.3
63.8
73.2
59.3
Video-RTS
7B
51.2
40.7
52.7
66.4
–
63.0
TW-GRPO
7B
16
32.9
51.3
65.8
73.3
55.1
245
246
247
248
249
250
SFT Models
Qwen2.5-VL-SFT
7B
16
31.7
47.4
61.3
69.2
52.8
32
33.9
49.4
63.5
69.9
55.4
64
33.7
49.4
61.6
70.0
58.8
251
252
253
254
255
Video-KTR
7B
16
40.7
51.3
65.7
73.3
57.3
32
41.6
52.6
65.9
73.4
60.3
64
42.7
53.1
66.6
73.5
62.5
(β) is configured at 0.4; and 8 responses are sampled for each prompt with a temperature of 1.0. During
inference, we may extend the maximum frames to 64 with a maximum resolution of 256 × 28 × 28.
256
257
258
259
260
261
262
263
264
265
266
267
Benchmarks.
To comprehensively assess the performance of Video-KTR, we select five challenging video
benchmarks: (1) reasoning-oriented benchmarks, including Video-Holmes (Cheng et al., 2025), VideoM-
MMU (Hu et al., 2025), and MMVU (Zhao et al., 2025), to assess the temporal, causal, and knowledge-
intensive reasoning capability of MLLMs; (2) general understanding benchmarks, including TempCom-
pass (Liu et al., 2024) and VideoMME (Fu et al., 2025).
Note Video-Holmes is a newly established
benchmark that poses significant challenges, requiring models to integrate dispersed narrative cues from
suspenseful short films and perform complex deductive reasoning beyond basic visual recognition.
Baselines.
We compare Video-KTR against a diverse set of baselines, encompassing both general-purpose
and reasoning-oriented MLLMs of similar size: LLaVA-OneVision (LLaVA-OV; Li et al. (2024)), VILA-
1.5 (Liu et al., 2025), Qwen2.5-VL (Bai et al., 2025), Video-R1 (Feng et al., 2025), Video-RTS (Wang et al.,
2025d), and TW-GRPO (Dang et al., 2025).
268
269
270
271
272
273
4.2
RESULTS AND ANALYSIS
274
275
276
277
278
279
280
281
Comparison with state-of-the-art models.
We evaluate Video-KTR against a diverse set of video rea-
soning models on three reasoning and two general video understanding benchmarks. Reported in Table 1,
Video-KTR consistently achieves state-of-the-art results. On Video-Holmes—which targets high-level tem-
poral and social reasoning in short films—our model attains 42.7%, surpassing all open-source baselines and
closely matching proprietary models like GPT-4o (OpenAI (2024a); 42.0%) and Gemini-1.5-Pro (Gemini
(2024); 41.3%). On knowledge-intensive benchmarks, i.e., MMVU(mc) and VideoMMMU, Video-KTR
achieves 66.6% and 53.1%, respectively, highlighting its strength in complex reasoning. Video-KTR also
6--------------------------------------------------------------------------------
Internal Error ()
citeturn28116view0 [wordlim: 200] Source: open({"ref_id":"https://api2.openreview.net/notes?id=Br1uoB0Jiy","lineno":null}); Total lines: 1
L0: URL https://api2.openreview.net/notes?id=Br1uoB0Jiy is not accessible via this tool.

