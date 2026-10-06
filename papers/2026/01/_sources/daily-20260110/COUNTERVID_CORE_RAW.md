# Actual exact-v1 primary HTML

CounterVid: Counterfactual Video Generation forMitigating Action and Temporal Hallucinations in Video-Language Models (https://arxiv.org/html/2601.04778v1)
citeturn26798view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04778v1","lineno":null}); Total lines: 348
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:   4. cite8†3 Proposed Method L19:     1. cite9†3.1 Task Definition and Preference Data L20:     2. cite10†3.2 Counterfactual Video Generation Pipeline L21:     3. cite11†3.3 Task and Preference Construction L22:       1. cite12†3.3.1 Preference Pairs for Action Recognition L23:       2. cite13†3.3.2 Preference Pairs for Temporal Ordering L24:     4. cite14†3.4 The MixDPO Alignment Framework L25:   5. cite15†4 Experiments L26:     1. cite16†4.1 Experimental Setup L27:     2. cite17†4.2 Data Quality Evaluation L28:     3. cite18†4.3 Experimental Results L29:     4. cite19†4.4 Qualitative Analysis L30:   6. cite20†5 Conclusion L31:   7. cite21†References L32:   8. cite22†A Additional Implementation and Training Details L33:   9. cite23†B Evaluation Benchmarks Details L34:     1. cite24†B.1 Video Hallucination Benchmarks L35:     2. cite25†B.2 General Video Understanding Benchmarks L36:   10. cite26†C Generation Pipeline Prompts L37: cite27†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L38: 
L39: arXiv:2601.04778v1 [cs.CV] 08 Jan 2026
L40: # CounterVid: Counterfactual Video Generation for
L41: Mitigating Action and Temporal Hallucinations in Video-Language Models
L42: Tobia Poppi Affiliation: University of Modena and Reggio Emilia, Italy Affiliation:  University of Pisa, Italy Affiliation: Amazon Prime Video Affiliation: {name.surname}@unimore.it Affiliation: {name.surname}@phd.unipi.it Affiliation: {tobipop, burauzke, amanmega, lporto, kesslerg, imyzyang, floschi}@amazon.com Affiliation: Amazon Prime Video Affiliation: University of Modena and Reggio Emilia Affiliation: University of Pisa {tobipop,burauzke,amanmega,lporto,kesslerg,imyzyang,floschi}@amazon.com, Email: name.surname@unimore.it    Burak Uzkent Affiliation: University of Modena and Reggio Emilia, Italy Affiliation: {name.surname}@unimore.it Affiliation: Amazon Prime Video Email: name.surname@phd.unipi.it    Amanmeet Garg Affiliation: University of Modena and Reggio Emilia, Italy Affiliation: {name.surname}@unimore.it Affiliation: Amazon Prime Video    Lucas Porto Affiliation: University of Modena and Reggio Emilia, Italy Affiliation: {name.surname}@unimore.it Affiliation: Amazon Prime Video    Garin Kessler Affiliation: University of Modena and Reggio Emilia, Italy Affiliation: {name.surname}@unimore.it Affiliation: Amazon Prime Video    Yezhou Yang Affiliation: University of Modena and Reggio Emilia, Italy Affiliation: {name.surname}@unimore.it Affiliation: Amazon Prime Video    Marcella Cornia Affiliation:  University of Pisa, Italy Affiliation: {name.surname}@phd.unipi.it Affiliation: University of Modena and Reggio Emilia    Lorenzo Baraldi Affiliation:  University of Pisa, Italy Affiliation: {name.surname}@phd.unipi.it Affiliation: University of Modena and Reggio Emilia    Rita Cucchiara Affiliation:  University of Pisa, Italy Affiliation: {name.surname}@phd.unipi.it Affiliation: University of Modena and Reggio Emilia    Florian Schiffers Affiliation:  Affiliation: University of Modena and Reggio Emilia, Italy Affiliation: {name.surname}@unimore.it Affiliation: Amazon Prime Video
L43: ###### Abstract
L44: Video-language models (VLMs) achieve strong multimodal understanding but remain prone to hallucinations, especially when reasoning about actions and temporal order. Existing mitigation strategies, such as textual filtering or random video perturbations, often fail to address the root cause: over-reliance on language priors rather than fine-grained visual dynamics.
L45: We propose a scalable framework for counterfactual video generation that synthesizes videos differing only in actions or temporal structure while preserving scene context. Our pipeline combines multimodal LLMs for action proposal and editing guidance with diffusion-based image and video models to generate semantic hard negatives at scale. Using this framework, we build CounterVid, a synthetic dataset of $\sim$26k preference pairs targeting action recognition and temporal reasoning.
L46: We further introduce MixDPO, a unified Direct Preference Optimization approach that jointly leverages textual and visual preferences. Fine-tuning Qwen2.5-VL with MixDPO yields consistent improvements, notably in temporal ordering, and transfers effectively to standard video hallucination benchmarks. Code and models will be made publicly available.
L47: ## 1 Introduction
L48: Large-scale video-language models (VLMs) cite28†Liu et al. (2023) ; cite29†Liu et al. (2024b) ; cite30†Chen et al. (2024) ; cite31†Zhu et al. (2023) have demonstrated strong performance on open-ended video understanding tasks cite32†Maaz et al. (2024) ; cite33†Ding et al. (2024) ; cite34†Li et al. (2023) ; cite35†Lin et al. (2024) ; cite36†Liu et al. (2024c) ; cite37†Zhang et al. (2024b) .
L49: Despite this progress, these models remain susceptible to hallucinations, producing responses that are not supported by visual evidence cite38†Liu et al. (2024a) ; cite39†Wang et al. (2024b) ; cite40†Bai et al. (2024) L50: Video hallucinations manifest in diverse forms, ranging from static appearance errors, such as describing nonexistent objects or misidentifying attributes, to dynamic failures caused by incorrect temporal understanding. Recent studies cite39†Wang et al. (2024b) ; cite41†Li et al. (2025a) show that modern VLMs often confuse visually similar actions or infer event sequences from language priors rather than observed motion.
L51: For example, a model may correctly recognize objects and scenes yet incorrectly assert that an action occurred, or assume a typical order of events even when contradicted by the video. Notably, such errors persist even in strong instruction-tuned models, highlighting limitations beyond surface-level reasoning.
L52: Motivated by these observations, we focus on two critical and under-explored failure modes: semantic action misidentification and incorrect inference of event order. Existing approaches address video hallucination by introducing additional supervision, either through architectural modifications cite42†Ma et al. (2024) ; cite43†Zhang et al. (2024a) or preference-based learning cite44†Rafailov et al. (2023) ; cite45†Ding et al. (2025) .
L53: However, many existing methods rely on negative samples obtained via random perturbations, such as frame shuffling. While such perturbations disrupt temporal coherence, they rarely produce semantic counterfactuals, i.e.videos that preserve scene context while differing meaningfully in actions or event order. Consequently, models may succeed by exploiting low-level artifacts or static cues, rather than learning fine-grained action dynamics cite46†Huang et al. (2018) .
L54: To overcome the above mentioned limitations, we introduce a scalable framework for counterfactual video generation that explicitly targets action and temporal understanding. Instead of random augmentations, our approach constructs videos that differ only in their underlying action trajectories while preserving scene identity. The proposed pipeline integrates complementary generative components: multimodal LLMs cite47†Minaee et al. (2024) ; cite48†Caffagni et al.
L55: (2024) for proposing plausible alternative actions and structured edits, image editing models for synthesizing action-completion frames cite49†Wu et al. (2025) ; cite50†Black Forest Labs (2025) , and image-to-video diffusion models cite51†Wan Team et al. (2025) for generating temporally coherent clips. This modular design disentangles semantic reasoning from visual synthesis, while enabling precise control over the generated counterfactuals.
L56: Using this framework, we compile CounterVid, a large-scale dataset of approximately 26k preference pairs composed entirely of synthetic videos with controlled action variations. From each anchor scene, we generate multiple action-consistent clips and construct preference pairs targeting both action recognition and temporal ordering, spanning free-form, binary, and structured formats.
L57: These data support two complementary supervision signals: textual preferences, contrasting grounded and hallucinated answers under fixed visual input, and visual preferences, contrasting correct and counterfactual videos under fixed textual input.
L58: We leverage these signals through MixDPO, a unified Direct Preference Optimization (DPO) cite44†Rafailov et al. (2023) framework integrating textual and visual supervision. By jointly promoting output grounding and sensitivity to visual evidence, our approach directly targets the mechanisms underlying video hallucination. Experiments show that fine-tuning Qwen2.5-VL cite52†Bai et al.
L59: (2025) with MixDPO yields substantial improvements in action recognition and temporal ordering, generalizing to established benchmarks such as EventHallusion cite43†Zhang et al. (2024a) and VidHalluc cite41†Li et al. (2025a) .
L60: Contributions. Our contributions are threefold:
L61: 
L62:   * •
L63: 
L64: We introduce a modular counterfactual video generation pipeline that combines language-guided action proposal with diffusion-based generation to produce semantic hard negatives at scale.
L65: 
L66:   * •
L67: 
L68: We construct CounterVid, a synthetic preference dataset designed to expose action and temporal hallucinations under controlled visual context.
L69: 
L70:   * •
L71: We present MixDPO, a unified preference-based alignment framework that jointly leverages textual and visual supervision to improve grounding and temporal sensitivity in VLMs; our code and models will be made publicly available.
L72: ## 2 Related Work
L73: Video Hallucinations. Recent works have shown that VLMs frequently generate hallucinated outputs that are not grounded in visual evidence, despite strong performance on standard video understanding benchmarks cite40†Bai et al. (2024) ; cite38†Liu et al. (2024a) ; cite39†Wang et al. (2024b) . VideoHallucer cite39†Wang et al. (2024b) provides an initial taxonomy, distinguishing intrinsic hallucinations (e.g., describing nonexistent objects) from extrinsic ones caused by unsupported reasoning.
L74: Subsequent studies emphasize temporal understanding as a particularly vulnerable dimension: models often confuse visually similar actions or infer event order from language priors rather than observed motion cite41†Li et al. (2025a) ; cite43†Zhang et al. (2024a) . Together, these works indicate that action recognition and temporal reasoning remain central challenges for VLMs.
L75: Architectural and Decoding Strategies. Several approaches mitigate hallucinations by strengthening visual grounding through architectural or inference-time interventions. VISTA-LLAMA cite42†Ma et al. (2024) enforces balanced attention over visual and textual tokens to reduce the tendency to ignore video input. Decoding-based methods cite43†Zhang et al. (2024a) ; cite53†Leng et al. (2024) , instead, counteract language priors by contrasting outputs generated from original and degraded or manipulated visual inputs.
L76: Self-refinement strategies, including Volcano cite54†Lee et al. (2024) , further encourage models to verify and revise predictions against visual evidence cite55†Wang et al. (2025) ; cite56†Guo et al. (2025) . While effective, these methods typically require custom architectures, additional inference passes, or specialized decoding schemes, which can limit scalability.
L77: Preference-Based Alignment. A different line of work reduces hallucinations through preference-based alignment. In the image domain, V-DPO cite57†Xie et al. (2024) and mDPO cite58†Wang et al. (2024a) extend DPO cite44†Rafailov et al. (2023) with both output-level preferences (same input, different answers) and input-level preferences (different inputs, same query). In the video domain, PaMi-VDPO cite45†Ding et al.
L78: (2025) constructs preference pairs using video augmentations such as frame shuffling, cropping, and temporal reversal, while related studies apply preference optimization on synthetic videos to reduce commonsense and physics-related hallucinations cite59†Li et al. (2025b) .
L79: cite60†Image: Refer to caption Figure 1: Overview of the counterfactual generation framework. Starting from a real video-caption pair, we extract a representative keyframe with a shared embedding space model, propose multiple alternative actions with a multimodal LLM, synthesize one counterfactual video per proposed action via image editing and image-to-video generation, and finally compose preference pairs for action recognition and temporal ordering.
L80: Despite their effectiveness, augmentation-based approaches are limited by the source content: random perturbations can disrupt temporal coherence but rarely produce counterfactuals that preserve scene context while varying actions or event order. As noted in cite45†Ding et al. (2025) , the most informative negatives are visually similar yet semantically distinct, which simple augmentations cannot reliably generate.
L81: Our work addresses this gap by synthesizing content-aware counterfactual videos with controlled action and temporal variations, and by jointly leveraging visual and textual preferences to promote visual grounding over language priors.
L82: ## 3 Proposed Method
L83: 
L84: We propose a scalable framework that (i) synthesizes counterfactual videos that differ only in action dynamics while preserving scene context, and (ii) aligns a VLM using a unified preference objective that couples textual and visual supervision.
L85: ### 3.1 Task Definition and Preference Data
L86: Video QA with Hallucinations. Let $V$ denote a video clip, $Q$ a question, and $A$ a free-form textual answer. A VLM with parameters $\theta$ defines a conditional distribution $\pi_{\theta}(A\,|\,V,Q)$. A hallucination occurs when $A$ is not supported by the visual evidence in $V$, despite being linguistically plausible.
L87: We focus on two dynamic failure modes: (i) action recognition (misidentifying the action in an otherwise correct response) and (ii) temporal ordering (incorrectly inferring the order/causality of multiple events).
L88: Preference Supervision. Our training signal consists of pairwise preferences of the form $(x,y^{+},y^{-})$ or ($x^{+},x^{-},y)$, where $x$ is the multimodal context, $y$ is the response, and the $+$ and $-$ apexes indicate preferred and rejected alternatives. We construct two complementary preference types.
L89: 
L90: Textual Preferences (t-pref). For a fixed context $x=(V,Q)$, we prefer a grounded answer $A^{+}$ over a hallucinated answer $A^{-}$:
L91: 
L92:  | $$(x,y^{+},y^{-})=\big((V,Q),A^{+},A^{-}\big).$$  |  | (1)
L93: Visual Preferences (v-pref). For a fixed text pair $(Q,A)$, we prefer the correct visual context over a counterfactual one:
L94: 
L95:  | $$(x^{+},x^{-},y)=\big((V^{+},Q),(V^{-},Q),A\big),$$  |  | (2)
L96: 
L97: where $V^{+}$ and $V^{-}$ depict different actions (or different action sequences) under nearly identical scene context. This directly penalizes “blind” generation, where $\pi_{\theta}(A\,|\,V^{+},Q)\approx\pi_{\theta}(A\,|\,V^{-},Q)$.
L98: ### 3.2 Counterfactual Video Generation Pipeline
L99: We start from a large collection of real video–caption pairs $(V^{\text{real}},C^{\text{real}})$ and use them only to extract an anchor frame; all preference videos are synthetic. Given one anchor frame, we synthesize a set of $N$ action videos $\mathcal{G}=\{(V_{i},C_{i})\}_{i=1}^{N}$ that share the same static context (scene, objects, viewpoint) but differ in the action dynamics. These generated videos form the basis for both action-recognition and temporal-ordering preference pairs.
L100: An overview of the generation pipeline is shown in Figure cite61†1 , and we elaborate on each part in the following sections.
L101: ① Keyframe Extraction. For each real pair $(V^{\text{real}},C^{\text{real}})$, we select a representative keyframe $I^{\text{start}}$ that best matches the caption and provides a stable starting state for editing and generation. We use a coarse-to-fine retrieval approach using a shared embedding space model cite62†Zhai et al. (2023) : (i) coarse sampling at 2 fps to identify a high-alignment temporal neighborhood, and (ii) refined sampling at 12 fps within that neighborhood to choose the final keyframe.
L102: We compute caption-frame similarity by averaging over multiple spatial crops (center/left/right) to reduce sensitivity to framing and to better capture the global scene.
L103: ② Action Proposal and Filtering. Conditioned on the keyframe $I^{\text{start}}$ and the original caption $C^{\text{real}}$, we prompt a multimodal LLM (i.e., Claude cite63†Anthropic (2025) ) to propose $N$ alternative actions $\{C_{i}\}_{i=1}^{N}$ that are: (i) plausible given the scene state in $I^{\text{start}}$, (ii) distinct from each other (to ensure hard negatives), and (iii) visually expressible within a short clip.
L104: We then filter proposals using the same LLM with explicit criteria for realism, safety, and action clarity (prompt templates in the Appendix).
L105: ③ Action Video Generation. For each action caption $C_{i}$, we generate an end frame $I_{i}^{\text{end}}$ depicting the completion of the action starting from $I^{\text{start}}$. We first convert $C_{i}$ into structured editing instructions, then apply an image editing model cite49†Wu et al. (2025) to obtain $I_{i}^{\text{end}}$.
L106: Because image editing can introduce semantic drift and artifacts, we employ an iterative refinement loop: after each attempt, the multimodal LLM evaluates whether $I_{i}^{\text{end}}$ matches the intended action and preserves the scene identity; if not, it revises the editing prompt.
L107: Finally, we synthesize a temporally coherent video $V_{i}$ with an image-to-video model cite51†Wan Team et al. (2025) conditioned on $(I_{0},I_{i}^{\text{end}},C_{i})$. This yields a set of action-consistent clips $\{V_{i}\}_{i=1}^{N}$ that share the same context by construction (same anchor frame) and differ in the action trajectory.
L108: ### 3.3 Task and Preference Construction
L109: After generation, we discard $(V^{\text{real}},C^{\text{real}})$, and construct samples for CounterVid exclusively from the generated set $\mathcal{G}=\{(V_{i},C_{i})\}_{i=1}^{N}$ obtained from the same anchor frame. Preference pairs are generated for different target capabilities (i.e., action recognition and temporal ordering) and in different formats (free-form, binary, and multiple choice or order list depending on the sample type).
L110: In the following, let $Q_{\text{act}}$ denote a generic action query (e.g., “What action is shown?”) and let $\mathcal{C}=\{C_{i}\}_{i=1}^{N}$ be the set of action captions proposed for the anchor.
L111: #### 3.3.1 Preference Pairs for Action Recognition
L112: 
L113: In action recognition, we employ a single generated clip $V_{i}$ and ask the model to identify its action. To generate t-pref pairs, we keep the input context fixed, $x=(V_{i},Q_{\text{act}})$, and contrast a grounded caption with a plausible but incorrect one sampled from the same anchor set:
L114: 
L115:  | $$A^{+}=C_{i},\;A^{-}=C_{j},\;j\sim\text{Unif}(\{1..N\}\setminus i).$$  |  | (3)
L116: For v-pref pairs, we fix the text pair $(Q_{\text{act}},A=C_{i})$ and swap the video, so that the same answer is correct for one clip and false for the other:
L117: 
L118:  | $$(V^{+},V^{-})=(V_{i},V_{j}),\;j\sim\text{Unif}(\{1..N\}\setminus i).$$  |  | (4)
L119: Formats. Free-form uses $Q_{\text{act}}$ with $A$ as caption. Binary choice presents one candidate and asks whether it matches the video. Multiple choice presents the candidate set $\mathcal{C}$, and the answer is the correct option index. In all cases, the preferred/rejected elements are defined via Eq. (cite64†3 ) or Eq. (cite65†4 ).
L120: #### 3.3.2 Preference Pairs for Temporal Ordering
L121: 
L122: Temporal ordering evaluates temporal understanding under minimal contextual change. Both chosen and rejected sequences are formed by concatenating generated clips from the same anchor frame.
L123: Sequence Construction. We sample $K$ distinct actions $\{i_{1},\dots,i_{K}\}\subset\{1..N\}$ and concatenate the corresponding clips $S=[V_{i_{1}};V_{i_{2}};\dots;V_{i_{K}}]$, where $[\cdot;\cdot]$ denotes temporal concatenation. We define a chosen order $S^{+}$ as a canonical ordering of the sampled actions (the proposer listing order), and a rejected order $S^{-}$ by applying a non-identity random permutation.
L124: Preference Pairs Generation. For t-pref pairs, we keep the context fixed, $x=(S^{+},Q_{\text{seq}})$, and contrast a grounded description with a hallucinated one obtained by caption swaps within the same anchor set. For v-pref pairs, we fix the textual target to the correct order and swap the visual evidence between $S^{+}$ and $S^{-}$. This directly enforces that the model assigns a higher likelihood to the correct ordering when the underlying clips are permuted but visually similar in context.
L125: Formats. Free-form uses $Q_{\text{seq}}$ with $A$ as an ordered list of actions. Binary choice presents a candidate ordering and asks whether it matches the video sequence. Order list presents the unordered action set and requires the model to output the correct temporal order as a sequence of indices.
L126: 
L127: Representative generated preference pairs from CounterVid are shown in Figure cite66†2 .
L128: cite67†Image: Refer to caption Figure 2: Qualitative examples from CounterVid, illustrating action recognition and temporal ordering samples across multiple-choice, order-list, binary, and free-form formats. All videos and answers are generated.
L129: ### 3.4 The MixDPO Alignment Framework
L130: 
L131: We fine-tune a base VLM with a unified preference objective that combines textual and visual signals. Our goal is not only to improve answer quality, but to increase input sensitivity: answers should change when the visual evidence changes.
L132: Preliminaries. DPO cite44†Rafailov et al. (2023) optimizes a policy (i.e., the video-language model being fine-tuned) $\pi_{\theta}$ given preference pairs $(x,y^{+},y^{-})$ without an explicit reward model. Let $\pi_{\text{ref}}$ be a frozen reference model, DPO defines an implicit reward as the log-likelihood ratio between the trainable policy and the reference model: $r_{\theta}(x,y)=\log\frac{\pi_{\theta}(y|x)}{\pi_{\text{ref}}(y|x)}$. The overall DPO objective is then defined as:
L133:  | $$\mathcal{L}_{\text{DPO}}=-\mathbb{E}\left[\log\sigma\left(\beta\left(r_{\theta}(x,y^{+})-r_{\theta}(x,y^{-})\right)\right)\right],$$  |  | (5)
L134: 
L135: where $\sigma$ is the sigmoid, and $\beta$ controls the strength of the deviation from $\pi_{\text{ref}}$.
L136: 
L137: Unified MixDPO for Hallucination Mitigation. As multimodal hallucination often stems from the model ignoring the visual context, we define a unified loss that integrates two complementary signals built on the two aforementioned preference types:
L138:  | $$\mathcal{L}_{\text{MixDPO}}(\theta)=\mathcal{L}_{\text{t-pref}}(\theta)+\lambda\mathcal{L}_{\text{v-pref}}(\theta).$$  |  | (6)
L139: 
L140: Here, we set $\lambda=1$ to balance the gradients between answer discrimination and visual grounding.
L141: 
L142: Textual Preference Loss. We force the model to sharpen its probability distribution over the correct tokens while suppressing plausible but visually unsupported sequences. Formally, given a textual preference triple $\big((V,Q),A^{+},A^{-}\big)$, we define
L143:  | $$\begin{split}\mathcal{L}_{\text{t-pref}}=-\mathbb{E}\Big[\log\sigma\big(\beta(r_{\theta}((V,Q),A^{+})-\\
L144: r_{\theta}((V,Q),A^{-}))\big)\Big].\end{split}$$  |  | (7)
L145: 
L146: In CounterVid, $A^{-}$ is constructed as an action-caption swap from the same anchor set, yielding a fluent but visually unsupported alternative, directly targeting language-prior guessing.
L147: 
L148: Visual Preference Loss. For a visual preference tuple $\big((V^{+},Q),A,(V^{-},Q),A\big)$, we define
L149:  | $$\begin{split}\mathcal{L}_{\text{v-pref}}=-\mathbb{E}\Big[\log\sigma\big(\beta(r_{\theta}((V^{+},Q),A)\\
L150: -r_{\theta}((V^{-},Q),A))\big)\Big].\end{split}$$  |  | (8)
L151: 
L152: This term explicitly enforces that the same answer $A$ should be assigned a high likelihood only under the correct visual evidence. When a model ignores video input, the two likelihoods become similar; maximizing their margin forces the policy to attend to discriminative temporal cues.
L153: Minimizing $\mathcal{L}_{\text{MixDPO}}$ teaches the model both (i) output grounding (prefer grounded over hallucinated answers under fixed video) and (ii) input sensitivity (prefer the correct video over a counterfactual under fixed text), which is essential for mitigating temporal hallucinations in VLMs.
L154: ## 4 Experiments
L155: ### 4.1 Experimental Setup
L156: CounterVid Details. The final version of CounterVid consists of 26,167 preference pairs spanning action recognition and temporal ordering, used to optimize VLMs with MixDPO. Action recognition includes 12,919 samples, distributed across free-form (4,416), binary-choice (4,416), and multiple-choice (4,087) formats. Temporal ordering consists of 13,248 samples, evenly split among free-form, order-list, and binary-choice queries (4,416 each).
L157: We maintain a consistent preference ratio of 70% visual preferences (v-pref) and 30% textual preferences (t-pref). In addition to training data, we curate 2,910 held-out samples for benchmarking VLMs under the same evaluation settings.
L158: Data Generation Settings. We generate counterfactual videos using the pipeline described in Sec. cite10†3.2 . Anchor frames and real captions are selected from the PE Video Dataset (PVD) cite68†Bolya et al. (2025) , from which we only select clips shorter than 10 seconds, which are likely to contain a single action. Keyframe extraction is performed with SigLIP-SO400M cite62†Zhai et al. (2023) . Action proposal and filtering use Claude-4-Sonnet cite63†Anthropic (2025) .
L159: End-frame generation is carried out via Qwen-Image-Edit cite49†Wu et al. (2025) with an iterative refinement loop (up to $N{=}5$ attempts) to ensure action correctness and scene consistency. Final videos are synthesized using Wan2.2-I2V-14B cite51†Wan Team et al. (2025) , producing clips of approximately three seconds at 680$\times$384 resolution. Additional details are provided in the Appendix.
L160: Baselines. We evaluate MixDPO on two backbone sizes, Qwen2.5-VL-3B and Qwen2.5-VL-7B cite52†Bai et al. (2025) , and compare against the following baselines to isolate the contribution of each component. Base corresponds to the respective Qwen2.5-VL backbone without preference-based fine-tuning. SFT fine-tunes the same backbone on the original PVD captions cite68†Bolya et al. (2025) , controlling for dataset domain effects. T-pref-DPO applies DPO cite44†Rafailov et al.
L161: (2023) using only textual preference (output-swap) pairs, isolating the effect of answer-level supervision. Our full method, MixDPO, jointly optimizes visual and textual preferences on top of the same backbone.
L162: Evaluation Benchmarks. We evaluate our method on a held-out evaluation set from CounterVid and a set of established video hallucination benchmarks. Specifically, we conduct experiments on VideoHallucer cite39†Wang et al. (2024b) , VidHalluc cite41†Li et al. (2025a) , EventHallusion cite43†Zhang et al. (2024a) , and VideoHallu cite59†Li et al. (2025b) , which cover hallucinations related to object existence, action recognition, temporal ordering, and event-level reasoning.
L163: To verify that hallucination mitigation does not degrade general video understanding, we additionally evaluate on VideoMME cite69†Fu et al. (2025) , NExT-QA cite70†Xiao et al. (2021) , and TempCompass cite71†Liu et al. (2024d) . Further details on evaluation benchmarks and settings are provided in the Appendix.
L164: Task Type  | Good  | Wrong  | Ambig.  | Bad Qual.
L165: --- | --- | --- | --- | ---
L166: Free-Form (88)  | 64.8%  | 12.5%  | 17.0%  | 5.7%
L167: Binary Choice (84)  | 69.0%  | 15.5%  | 8.3%  | 7.1%
L168: Multiple Choice (37)  | 78.4%  | 8.1%  | 5.4%  | 8.1%
L169: Order List (35)  | 62.9%  | 11.4%  | 17.1%  | 8.6%
L170: 
L171: Table 1: Human evaluation results by task format. Multiple-choice samples exhibit the highest label reliability, while free-form and temporal ordering formats show higher ambiguity due to task complexity.
L172: ### 4.2 Data Quality Evaluation
L173: 
L174: To assess the quality of the automatically generated CounterVid, we conduct a human evaluation on a representative subset of the held-out split. The evaluation focuses on two aspects: (i) the correctness of preference labels (i.e., whether the chosen video provides stronger visual support for the answer than the rejected one), and (ii) the visual quality of the generated counterfactual videos.
L175: Evaluation Protocol. We randomly sample 244 examples from the held-out set ($\approx$8.4% of 2,910 samples), with proportional coverage across task formats: free-form description (36.1%), binary choice (34.4%), multiple choice (15.2%), and order list (14.3%). Each sample is independently reviewed by four evaluators, who inspect the generated videos together with the associated questions and answers.
L176: Evaluators assign one of four labels: good (preference labels are correct and visual quality is sufficient), wrong (labels are inconsistent with the visual evidence), ambiguous (the distinction between chosen and rejected is unclear or the question is underspecified), or bad visual quality (artifacts or inconsistencies prevent reliable judgment).
L177: Results and Analysis. Table cite72†1 reports results by task format. Overall, 68% of the evaluated samples are labeled as good, indicating that the majority of preference pairs are both semantically correct and visually interpretable. The fraction of samples with poor visual quality is limited (7%), suggesting that the image-to-video diffusion model produces videos suitable for preference learning.
L178: Multiple-choice samples achieve the highest reliability (78.4% good), likely due to the constrained answer space. In contrast, free-form and order-list formats exhibit higher ambiguity rates (17.0% and 17.1%, respectively), the inherent difficulty of evaluating open-ended descriptions and complex sequences, where the distinction between correct and incorrect ordering can sometimes be subtle.
L179: Binary-choice questions show a slightly higher rate of incorrect labels (15.5%), indicating sensitivity to minor mismatches between the generated visual edits and question phrasing. Despite this noise, the overall data quality is sufficient to provide a strong training signal, as evidenced in our main results.


# Necessary evaluation return (not all appended references reviewed)

CounterVid: Counterfactual Video Generation forMitigating Action and Temporal Hallucinations in Video-Language Models (https://arxiv.org/html/2601.04778v1)
citeturn26807view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04778v1","lineno":154}); Total lines: 348
L99: We start from a large collection of real video–caption pairs $(V^{\text{real}},C^{\text{real}})$ and use them only to extract an anchor frame; all preference videos are synthetic. Given one anchor frame, we synthesize a set of $N$ action videos $\mathcal{G}=\{(V_{i},C_{i})\}_{i=1}^{N}$ that share the same static context (scene, objects, viewpoint) but differ in the action dynamics. These generated videos form the basis for both action-recognition and temporal-ordering preference pairs.
L100: An overview of the generation pipeline is shown in Figure cite61†1 , and we elaborate on each part in the following sections.
L101: ① Keyframe Extraction. For each real pair $(V^{\text{real}},C^{\text{real}})$, we select a representative keyframe $I^{\text{start}}$ that best matches the caption and provides a stable starting state for editing and generation. We use a coarse-to-fine retrieval approach using a shared embedding space model cite62†Zhai et al. (2023) : (i) coarse sampling at 2 fps to identify a high-alignment temporal neighborhood, and (ii) refined sampling at 12 fps within that neighborhood to choose the final keyframe.
L102: We compute caption-frame similarity by averaging over multiple spatial crops (center/left/right) to reduce sensitivity to framing and to better capture the global scene.
L103: ② Action Proposal and Filtering. Conditioned on the keyframe $I^{\text{start}}$ and the original caption $C^{\text{real}}$, we prompt a multimodal LLM (i.e., Claude cite63†Anthropic (2025) ) to propose $N$ alternative actions $\{C_{i}\}_{i=1}^{N}$ that are: (i) plausible given the scene state in $I^{\text{start}}$, (ii) distinct from each other (to ensure hard negatives), and (iii) visually expressible within a short clip.
L104: We then filter proposals using the same LLM with explicit criteria for realism, safety, and action clarity (prompt templates in the Appendix).
L105: ③ Action Video Generation. For each action caption $C_{i}$, we generate an end frame $I_{i}^{\text{end}}$ depicting the completion of the action starting from $I^{\text{start}}$. We first convert $C_{i}$ into structured editing instructions, then apply an image editing model cite49†Wu et al. (2025) to obtain $I_{i}^{\text{end}}$.
L106: Because image editing can introduce semantic drift and artifacts, we employ an iterative refinement loop: after each attempt, the multimodal LLM evaluates whether $I_{i}^{\text{end}}$ matches the intended action and preserves the scene identity; if not, it revises the editing prompt.
L107: Finally, we synthesize a temporally coherent video $V_{i}$ with an image-to-video model cite51†Wan Team et al. (2025) conditioned on $(I_{0},I_{i}^{\text{end}},C_{i})$. This yields a set of action-consistent clips $\{V_{i}\}_{i=1}^{N}$ that share the same context by construction (same anchor frame) and differ in the action trajectory.
L108: ### 3.3 Task and Preference Construction
L109: After generation, we discard $(V^{\text{real}},C^{\text{real}})$, and construct samples for CounterVid exclusively from the generated set $\mathcal{G}=\{(V_{i},C_{i})\}_{i=1}^{N}$ obtained from the same anchor frame. Preference pairs are generated for different target capabilities (i.e., action recognition and temporal ordering) and in different formats (free-form, binary, and multiple choice or order list depending on the sample type).
L110: In the following, let $Q_{\text{act}}$ denote a generic action query (e.g., “What action is shown?”) and let $\mathcal{C}=\{C_{i}\}_{i=1}^{N}$ be the set of action captions proposed for the anchor.
L111: #### 3.3.1 Preference Pairs for Action Recognition
L112: 
L113: In action recognition, we employ a single generated clip $V_{i}$ and ask the model to identify its action. To generate t-pref pairs, we keep the input context fixed, $x=(V_{i},Q_{\text{act}})$, and contrast a grounded caption with a plausible but incorrect one sampled from the same anchor set:
L114: 
L115:  | $$A^{+}=C_{i},\;A^{-}=C_{j},\;j\sim\text{Unif}(\{1..N\}\setminus i).$$  |  | (3)
L116: For v-pref pairs, we fix the text pair $(Q_{\text{act}},A=C_{i})$ and swap the video, so that the same answer is correct for one clip and false for the other:
L117: 
L118:  | $$(V^{+},V^{-})=(V_{i},V_{j}),\;j\sim\text{Unif}(\{1..N\}\setminus i).$$  |  | (4)
L119: Formats. Free-form uses $Q_{\text{act}}$ with $A$ as caption. Binary choice presents one candidate and asks whether it matches the video. Multiple choice presents the candidate set $\mathcal{C}$, and the answer is the correct option index. In all cases, the preferred/rejected elements are defined via Eq. (cite64†3 ) or Eq. (cite65†4 ).
L120: #### 3.3.2 Preference Pairs for Temporal Ordering
L121: 
L122: Temporal ordering evaluates temporal understanding under minimal contextual change. Both chosen and rejected sequences are formed by concatenating generated clips from the same anchor frame.
L123: Sequence Construction. We sample $K$ distinct actions $\{i_{1},\dots,i_{K}\}\subset\{1..N\}$ and concatenate the corresponding clips $S=[V_{i_{1}};V_{i_{2}};\dots;V_{i_{K}}]$, where $[\cdot;\cdot]$ denotes temporal concatenation. We define a chosen order $S^{+}$ as a canonical ordering of the sampled actions (the proposer listing order), and a rejected order $S^{-}$ by applying a non-identity random permutation.
L124: Preference Pairs Generation. For t-pref pairs, we keep the context fixed, $x=(S^{+},Q_{\text{seq}})$, and contrast a grounded description with a hallucinated one obtained by caption swaps within the same anchor set. For v-pref pairs, we fix the textual target to the correct order and swap the visual evidence between $S^{+}$ and $S^{-}$. This directly enforces that the model assigns a higher likelihood to the correct ordering when the underlying clips are permuted but visually similar in context.
L125: Formats. Free-form uses $Q_{\text{seq}}$ with $A$ as an ordered list of actions. Binary choice presents a candidate ordering and asks whether it matches the video sequence. Order list presents the unordered action set and requires the model to output the correct temporal order as a sequence of indices.
L126: 
L127: Representative generated preference pairs from CounterVid are shown in Figure cite66†2 .
L128: cite67†Image: Refer to caption Figure 2: Qualitative examples from CounterVid, illustrating action recognition and temporal ordering samples across multiple-choice, order-list, binary, and free-form formats. All videos and answers are generated.
L129: ### 3.4 The MixDPO Alignment Framework
L130: 
L131: We fine-tune a base VLM with a unified preference objective that combines textual and visual signals. Our goal is not only to improve answer quality, but to increase input sensitivity: answers should change when the visual evidence changes.
L132: Preliminaries. DPO cite44†Rafailov et al. (2023) optimizes a policy (i.e., the video-language model being fine-tuned) $\pi_{\theta}$ given preference pairs $(x,y^{+},y^{-})$ without an explicit reward model. Let $\pi_{\text{ref}}$ be a frozen reference model, DPO defines an implicit reward as the log-likelihood ratio between the trainable policy and the reference model: $r_{\theta}(x,y)=\log\frac{\pi_{\theta}(y|x)}{\pi_{\text{ref}}(y|x)}$. The overall DPO objective is then defined as:
L133:  | $$\mathcal{L}_{\text{DPO}}=-\mathbb{E}\left[\log\sigma\left(\beta\left(r_{\theta}(x,y^{+})-r_{\theta}(x,y^{-})\right)\right)\right],$$  |  | (5)
L134: 
L135: where $\sigma$ is the sigmoid, and $\beta$ controls the strength of the deviation from $\pi_{\text{ref}}$.
L136: 
L137: Unified MixDPO for Hallucination Mitigation. As multimodal hallucination often stems from the model ignoring the visual context, we define a unified loss that integrates two complementary signals built on the two aforementioned preference types:
L138:  | $$\mathcal{L}_{\text{MixDPO}}(\theta)=\mathcal{L}_{\text{t-pref}}(\theta)+\lambda\mathcal{L}_{\text{v-pref}}(\theta).$$  |  | (6)
L139: 
L140: Here, we set $\lambda=1$ to balance the gradients between answer discrimination and visual grounding.
L141: 
L142: Textual Preference Loss. We force the model to sharpen its probability distribution over the correct tokens while suppressing plausible but visually unsupported sequences. Formally, given a textual preference triple $\big((V,Q),A^{+},A^{-}\big)$, we define
L143:  | $$\begin{split}\mathcal{L}_{\text{t-pref}}=-\mathbb{E}\Big[\log\sigma\big(\beta(r_{\theta}((V,Q),A^{+})-\\
L144: r_{\theta}((V,Q),A^{-}))\big)\Big].\end{split}$$  |  | (7)
L145: 
L146: In CounterVid, $A^{-}$ is constructed as an action-caption swap from the same anchor set, yielding a fluent but visually unsupported alternative, directly targeting language-prior guessing.
L147: 
L148: Visual Preference Loss. For a visual preference tuple $\big((V^{+},Q),A,(V^{-},Q),A\big)$, we define
L149:  | $$\begin{split}\mathcal{L}_{\text{v-pref}}=-\mathbb{E}\Big[\log\sigma\big(\beta(r_{\theta}((V^{+},Q),A)\\
L150: -r_{\theta}((V^{-},Q),A))\big)\Big].\end{split}$$  |  | (8)
L151: 
L152: This term explicitly enforces that the same answer $A$ should be assigned a high likelihood only under the correct visual evidence. When a model ignores video input, the two likelihoods become similar; maximizing their margin forces the policy to attend to discriminative temporal cues.
L153: Minimizing $\mathcal{L}_{\text{MixDPO}}$ teaches the model both (i) output grounding (prefer grounded over hallucinated answers under fixed video) and (ii) input sensitivity (prefer the correct video over a counterfactual under fixed text), which is essential for mitigating temporal hallucinations in VLMs.
L154: ## 4 Experiments
L155: ### 4.1 Experimental Setup
L156: CounterVid Details. The final version of CounterVid consists of 26,167 preference pairs spanning action recognition and temporal ordering, used to optimize VLMs with MixDPO. Action recognition includes 12,919 samples, distributed across free-form (4,416), binary-choice (4,416), and multiple-choice (4,087) formats. Temporal ordering consists of 13,248 samples, evenly split among free-form, order-list, and binary-choice queries (4,416 each).
L157: We maintain a consistent preference ratio of 70% visual preferences (v-pref) and 30% textual preferences (t-pref). In addition to training data, we curate 2,910 held-out samples for benchmarking VLMs under the same evaluation settings.
L158: Data Generation Settings. We generate counterfactual videos using the pipeline described in Sec. cite10†3.2 . Anchor frames and real captions are selected from the PE Video Dataset (PVD) cite68†Bolya et al. (2025) , from which we only select clips shorter than 10 seconds, which are likely to contain a single action. Keyframe extraction is performed with SigLIP-SO400M cite62†Zhai et al. (2023) . Action proposal and filtering use Claude-4-Sonnet cite63†Anthropic (2025) .
L159: End-frame generation is carried out via Qwen-Image-Edit cite49†Wu et al. (2025) with an iterative refinement loop (up to $N{=}5$ attempts) to ensure action correctness and scene consistency. Final videos are synthesized using Wan2.2-I2V-14B cite51†Wan Team et al. (2025) , producing clips of approximately three seconds at 680$\times$384 resolution. Additional details are provided in the Appendix.
L160: Baselines. We evaluate MixDPO on two backbone sizes, Qwen2.5-VL-3B and Qwen2.5-VL-7B cite52†Bai et al. (2025) , and compare against the following baselines to isolate the contribution of each component. Base corresponds to the respective Qwen2.5-VL backbone without preference-based fine-tuning. SFT fine-tunes the same backbone on the original PVD captions cite68†Bolya et al. (2025) , controlling for dataset domain effects. T-pref-DPO applies DPO cite44†Rafailov et al.
L161: (2023) using only textual preference (output-swap) pairs, isolating the effect of answer-level supervision. Our full method, MixDPO, jointly optimizes visual and textual preferences on top of the same backbone.
L162: Evaluation Benchmarks. We evaluate our method on a held-out evaluation set from CounterVid and a set of established video hallucination benchmarks. Specifically, we conduct experiments on VideoHallucer cite39†Wang et al. (2024b) , VidHalluc cite41†Li et al. (2025a) , EventHallusion cite43†Zhang et al. (2024a) , and VideoHallu cite59†Li et al. (2025b) , which cover hallucinations related to object existence, action recognition, temporal ordering, and event-level reasoning.
L163: To verify that hallucination mitigation does not degrade general video understanding, we additionally evaluate on VideoMME cite69†Fu et al. (2025) , NExT-QA cite70†Xiao et al. (2021) , and TempCompass cite71†Liu et al. (2024d) . Further details on evaluation benchmarks and settings are provided in the Appendix.
L164: Task Type  | Good  | Wrong  | Ambig.  | Bad Qual.
L165: --- | --- | --- | --- | ---
L166: Free-Form (88)  | 64.8%  | 12.5%  | 17.0%  | 5.7%
L167: Binary Choice (84)  | 69.0%  | 15.5%  | 8.3%  | 7.1%
L168: Multiple Choice (37)  | 78.4%  | 8.1%  | 5.4%  | 8.1%
L169: Order List (35)  | 62.9%  | 11.4%  | 17.1%  | 8.6%
L170: 
L171: Table 1: Human evaluation results by task format. Multiple-choice samples exhibit the highest label reliability, while free-form and temporal ordering formats show higher ambiguity due to task complexity.
L172: ### 4.2 Data Quality Evaluation
L173: 
L174: To assess the quality of the automatically generated CounterVid, we conduct a human evaluation on a representative subset of the held-out split. The evaluation focuses on two aspects: (i) the correctness of preference labels (i.e., whether the chosen video provides stronger visual support for the answer than the rejected one), and (ii) the visual quality of the generated counterfactual videos.
L175: Evaluation Protocol. We randomly sample 244 examples from the held-out set ($\approx$8.4% of 2,910 samples), with proportional coverage across task formats: free-form description (36.1%), binary choice (34.4%), multiple choice (15.2%), and order list (14.3%). Each sample is independently reviewed by four evaluators, who inspect the generated videos together with the associated questions and answers.
L176: Evaluators assign one of four labels: good (preference labels are correct and visual quality is sufficient), wrong (labels are inconsistent with the visual evidence), ambiguous (the distinction between chosen and rejected is unclear or the question is underspecified), or bad visual quality (artifacts or inconsistencies prevent reliable judgment).
L177: Results and Analysis. Table cite72†1 reports results by task format. Overall, 68% of the evaluated samples are labeled as good, indicating that the majority of preference pairs are both semantically correct and visually interpretable. The fraction of samples with poor visual quality is limited (7%), suggesting that the image-to-video diffusion model produces videos suitable for preference learning.
L178: Multiple-choice samples achieve the highest reliability (78.4% good), likely due to the constrained answer space. In contrast, free-form and order-list formats exhibit higher ambiguity rates (17.0% and 17.1%, respectively), the inherent difficulty of evaluating open-ended descriptions and complex sequences, where the distinction between correct and incorrect ordering can sometimes be subtle.
L179: Binary-choice questions show a slightly higher rate of incorrect labels (15.5%), indicating sensitivity to minor mismatches between the generated visual edits and question phrasing. Despite this noise, the overall data quality is sufficient to provide a strong training signal, as evidenced in our main results.
L180:  |  | Temporal Ord.  |  | Action Rec.  |
L181: Model  |  | FF  | OL  | BC  |  | FF  | MC  | BC  | Avg
L182: --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L183: Qwen-2.5-VL-3B  |  |  |  |  |  |  |
L184: Base  |  | 29.8  | 1.6  | 48.9  |  | 28.0  | 48.4  | 64.6  | 36.9
L185: SFT  |  | 29.4  | 2.0  | 47.9  |  | 27.2  | 51.9  | 65.2  | 37.2
L186: T-pref-DPO  |  | 32.2  | 15.7  | 56.0  |  | 29.6  | 58.7  | 69.5  | 43.6
L187: MixDPO (Ours)  |  | 31.0  | 16.7  | 64.0  |  | 29.5  | 60.0  | 70.3  | 45.2
L188: Qwen-2.5-VL-7B  |  |  |  |  |  |  |
L189: Base  |  | 70.3  | 16.5  | 57.8  |  | 55.1  | 68.6  | 78.2  | 57.8
L190: SFT  |  | 69.3  | 14.9  | 55.9  |  | 55.3  | 67.7  | 79.2  | 57.1
L191: T-pref-DPO  |  | 72.2  | 37.1  | 67.4  |  | 56.0  | 70.8  | 79.8  | 63.9
L192: MixDPO (Ours)  |  | 72.2  | 43.8  | 72.7  |  | 56.3  | 71.2  | 80.7  | 66.2
L193: Table 2: CounterVid held-out benchmark results. Accuracy (%) on temporal ordering and action recognition tasks. FF: free-form; BC: binary choice; OL: order list; MC: multiple choice. MixDPO yields consistent improvements, with the largest gains on temporal ordering tasks where visual grounding is critical.
L194: ### 4.3 Experimental Results
L195: CounterVid Benchmark. Table cite73†2 reports results on the held-out CounterVid benchmark. For the 3B model, MixDPO improves average accuracy from 36.9% (base) to 45.2% (+8.3pp), while the 7B variant increases from 57.8% to 66.2% (+8.4pp). The largest gains are observed on temporal ordering tasks, where correct predictions require sensitivity to changes in visual evidence. For 3B, order-list accuracy increases from 1.6% to 16.7% and binary temporal accuracy from 48.9% to 64.0%.
L196: For 7B, order-list performance improves from 16.5% to 43.8%. Action recognition also shows consistent gains across formats, with binary choice reaching 70.3% (3B) and 80.7% (7B).
L197: The SFT baseline yields minimal or negative changes (e.g., -0.7pp on average for the 7B model), indicating that exposure to PVD captions alone is insufficient. The T-pref-DPO ablation improves over the base model but trails MixDPO by 1.6-2.3pp on average. While this gap may appear modest, a task-level breakdown reveals that visual preferences contribute most strongly on temporal ordering tasks.
L198: In particular, MixDPO substantially outperforms T-pref-DPO on order-list and binary temporal questions (e.g., 37.1% vs. 43.8% and 67.4% vs. 72.7% on the 7B model), where input-level conditioning is essential. In contrast, action recognition tasks (especially in constrained formats) show smaller differences, suggesting that these tasks can often be addressed through improved answer discrimination from textual preferences alone.
L199: Overall, these results suggest that textual preferences primarily improve answer discrimination for a fixed video, while visual preferences are critical for enforcing sensitivity to changes in visual evidence and achieving robust temporal grounding.
L200: cite74†Image: Refer to caption Figure 3: Qualitative examples of hallucination correction on the VidHalluc benchmark. Compared to the base and text-only preference models, MixDPO produces responses that better align with the visual evidence, particularly in cases involving temporal reasoning.
L201:  |  | EventHal  | VidHal  | VideoHal  | VideoHcr
L202: Model  |  | (Avg)  | (TSH)  | (Overall)  | (Avg)
L203: --- | --- | --- | --- | --- | ---
L204: Qwen-2.5-VL-3B  |  |  |
L205: Base  |  | 59.4  | 78.5  | 35.1  | 52.6
L206: SFT  |  | 59.9  | 81.5  | 35.2  | 52.1
L207: T-pref-DPO  |  | 64.3  | 80.0  | 36.3  | 53.6
L208: MixDPO (Ours)  |  | 64.4  | 80.0  | 37.9  | 54.6
L209: Qwen-2.5-VL-7B  |  |  |
L210: Base (Instruct)  |  | 70.1  | 82.7  | 38.2  | 54.1
L211: SFT  |  | 66.7  | 82.7  | 39.0  | 53.9
L212: T-pref-DPO  |  | 72.7  | 87.8  | 39.8  | 55.1
L213: MixDPO (Ours)  |  | 72.5  | 90.5  | 39.3  | 55.7
L214: Table 3: Performance on established hallucination benchmarks. Accuracy (%) across event-level, temporal, and content-based hallucination evaluations. MixDPO shows consistent improvements across multiple real-world benchmarks.
L215: Established Hallucination Benchmarks. Table cite75†3 reports results on four established benchmarks for video hallucination evaluation. On EventHallusion, MixDPO improves the 3B model from 59.4% to 64.4% (+5.0pp) and reaches 72.5% on the 7B model, indicating reduced reliance on language priors for event reasoning. VidHalluc, which evaluates temporal sequence hallucination (TSH), shows the largest gains, with the 7B model improving from 82.7% to 90.5% (+7.8pp).
L216: VideoHallu and VideoHallucer also show consistent improvements (e.g., 35.1% to 37.9% on VideoHallu for 3B, and up to 55.7% on VideoHallucer for 7B), suggesting broader reductions in hallucinations beyond temporal ordering. Across all benchmarks, the SFT baseline yields limited or inconsistent gains, while T-pref-DPO improves over the base model but consistently achieves lower performance than MixDPO.
L217: These results further highlight the importance of visual preference learning for mitigating hallucinations that arise from incorrect temporal and event-level reasoning.
L218: General Video Understanding. Table cite76†4 reports results on general benchmarks. On VideoMME, results are preserved across both model sizes, indicating that preference-based alignment does not degrade general video understanding. On NExT-QA, which focuses on causal and temporal action reasoning, the 3B model improves in multiple-choice accuracy from 75.2% to 76.7%, while the 7B model maintains the baseline performance. Notably, TempCompass shows the most consistent improvements.
L219: For the 3B model, accuracy increases across both multiple-choice and binary-choice formats. For the 7B model, caption matching improves substantially, from 76.2% to 80.2%. These gains indicate improved temporal commonsense reasoning and event consistency, aligning with the improvements observed on our temporal ordering benchmark. Overall, these results confirm that MixDPO enhances temporal reasoning while preserving general multimodal understanding.
L220: ### 4.4 Qualitative Analysis
L221: Figure cite77†3 presents qualitative results on the VidHalluc benchmark. In these examples, both the base model and the text-only preference model generate incorrect predictions despite visual evidence to the contrary, often favoring plausible but unsupported actions or event sequences. In contrast, MixDPO produces responses that are more consistent with the video content, correcting hallucinations related to both action recognition and temporal ordering.
L222: Beyond correcting explicit errors, we observe that MixDPO exhibits more cautious behavior when the visual evidence is ambiguous or partially occluded, avoiding confident but unsupported claims. This qualitative behavior complements the quantitative results, suggesting that mixed visual and textual preference learning improves both visual grounding and robustness to temporal hallucinations.
L223:  |  | NExT-QA  | TempCompass
L224: --- | --- | --- | ---
L225: Model  | VideoMME  | MC  | OE  | MC  | BC  | CM
L226: --- | --- | --- | --- | --- | --- | ---
L227: Qwen-2.5-VL-3B  |  |  |  |  |  |
L228: Base  | 57.8  | 75.2  | 29.4  | 65.8  | 68.4  | 76.2
L229: SFT  | 57.5  | 76.4  | 29.8  | 66.2  | 68.2  | 76.1
L230: T-Pref-DPO  | 57.4  | 76.8  | 29.6  | 66.8  | 69.0  | 77.5
L231: MixDPO (ours)  | 57.8  | 76.7  | 29.7  | 67.0  | 69.6  | 77.2
L232: Qwen-2.5-VL-7B  |  |  |  |  |  |
L233: Base  | 61.4  | 74.7  | 32.2  | 73.2  | 75.5  | 76.2
L234: SFT  | 61.5  | 75.5  | 32.2  | 73.4  | 75.6  | 79.6
L235: T-Pref-DPO  | 61.4  | 75.1  | 32.2  | 73.4  | 75.8  | 77.6
L236: MixDPO (ours)  | 61.5  | 74.9  | 32.2  | 73.7  | 75.9  | 80.2
L237: Table 4: Performance on general video understanding benchmarks. Accuracy (%) on VideoMME, NExT-QA, and TempCompass. MC: multiple choice; OE: open-ended; BC: binary choice; CM: caption matching. MixDPO preserves video understanding performance while yielding consistent gains on temporal reasoning.
L238: ## 5 Conclusion
L239: We presented a scalable framework for mitigating hallucinations in VLMs by coupling counterfactual video generation with unified preference-based alignment. By synthesizing semantic hard negatives that preserve scene context while varying action dynamics, our approach directly targets action misidentification and temporal ordering errors that commonly arise from over-reliance on language priors.
L240: The resulting dataset, CounterVid, and the proposed MixDPO alignment framework enable effective training without human annotation, yielding improvements on action recognition and temporal reasoning benchmarks while preserving general video understanding performance.
L241: Beyond the presented results, this work highlights the promise of modular, generative counterfactual data as a practical mechanism for improving visual grounding in VLMs, and we hope it encourages further exploration of counterfactual generation for building more robust and trustworthy multimodal models.
L242: ## Limitations
L243: While our approach achieves strong performance, several aspects offer opportunities for future extension and refinement. First, the evaluation mechanisms used for action proposal filtering and video generation could be further refined, for example, through more comprehensive sanity checks, to increase the proportion of high-quality samples in the final dataset.
L244: Second, the quality of the generated counterfactuals depends on the underlying generative models, and is expected to improve as image and video generation methods continue to advance. Third, our current counterfactuals focus on short-term actions ($<2\,\mathrm{s}$); extending the framework to longer and more complex temporal structures remains an important direction.
L245: Finally, we adopt parameter-efficient fine-tuning by freezing the vision encoder; while full end-to-end training may further enhance sensitivity to fine-grained visual cues, it incurs substantially higher computational cost and optimization complexity, which we leave for future exploration.
L246: ## Ethical Considerations
L247: The ability to synthesize context-aware alternative actions via our counterfactual generation framework is a dual-use technology; while designed for model alignment, it could potentially be repurposed to create misinformation or deceptive video content. We acknowledge that releasing our methodology and code inherently carries this risk, yet we prioritize the scientific necessity of addressing the widespread problem of VLM hallucinations.
L248: Furthermore, because our framework relies on large-scale generative models, the resulting synthetic data may inherit underlying biases or stereotypes present in training sets of those models. Finally, we note the environmental impact of this work, as the synthesis of approximately 26k preference pairs required roughly 3,000 GPU-hours.
L249: By providing our code to the community, we enable other researchers to build upon our findings and alignment methodology without the immediate need for redundant, large-scale computational trials.
L250: ## References
L251:   * Anthropic (2025) Anthropic System Card: Claude Opus 4 & Claude Sonnet 4. External Links: cite78†Link†www-cdn.anthropic.com Cited by: cite79†§3.2 , cite80†§4.1 .
L252:   * Bai et al. (2025) S. Bai, K. Chen, X. Liu, J. Wang, W. Ge, S. Song, K. Dang, P. Wang, S. Wang, J. Tang, H. Zhong, Y. Zhu, M. Yang, Z. Li, J. Wan, P. Wang, W. Ding, Z. Fu, Y. Xu, J. Ye, X. Zhang, T. Xie, Z. Cheng, H. Zhang, Z. Yang, H. Xu, and J. Lin Qwen2.5-VL Technical Report. arXiv preprint arXiv:2502.13923. Cited by: cite81†§1 , cite82†§4.1 .
L253:   * Bai et al. (2024) Z. Bai, P. Wang, T. Xiao, T. He, Z. Han, Z. Zhang, and M. Z. Shou Hallucination of Multimodal Large Language Models: A Survey. arXiv preprint arXiv:2404.18930. Cited by: cite83†§1 , cite84†§2 .
L254:   * Black Forest Labs (2025) Black Forest Labs FLUX. 1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space. arXiv preprint arXiv:2506.15742. Cited by: cite85†§1 .
L255:   * Bolya et al. (2025) D. Bolya, P. Huang, P. Sun, J. H. Cho, A. Madotto, C. Wei, T. Ma, J. Zhi, J. Rajasegaran, H. Rasheed, J. Wang, M. Monteiro, H. Xu, S. Dong, N. Ravi, D. Li, P. Dollár, and C. Feichtenhofer Perception Encoder: The best visual embeddings are not at the output of the network. arXiv preprint arXiv:2504.13181. Cited by: cite80†§4.1 , cite82†§4.1 .
L256:   * Caffagni et al. (2024) D. Caffagni, F. Cocchi, L. Barsellotti, N. Moratelli, S. Sarto, L. Baraldi, L. Baraldi, M. Cornia, and R. Cucchiara The Revolution of Multimodal Large Language Models: A Survey. In ACL Findings, Cited by: cite85†§1 .

