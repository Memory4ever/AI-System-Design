# Exact-v1 primary cached excerpts — 2601.19089

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Original response 1: stdnext2head

EPAS: Efficient Training with Progressive Activation Sharing (https://arxiv.org/html/2601.19089v1)
citeturn28349view2 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19089v1","lineno":null}); Total lines: 305


## Original response 2: stdnext2core

EPAS: Efficient Training with Progressive Activation Sharing (https://arxiv.org/html/2601.19089v1)
citeturn28352view2 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"turn28349view2","lineno":50}); Total lines: 305
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract. L16:   2. cite6†1 Introduction L17:   3. cite7†2 Progressive Activation Sharing L18:     1. cite8†2.1 Switchable Activation Sharing Decoder L19:     2. cite9†2.2 Progressive Activation Sharing L20:     3. cite10†2.3 Applications L21:   4. cite11†3 Experiments L22:     1. cite12†3.1 Training efficiency L23:     2. cite13†3.2 Inference efficiency L24:     3. cite14†3.3 Language Model Evaluations L25:     4. cite15†3.4 Ablation Experiment L26:   5. cite16†4 Related Works L27:   6. cite17†5 Conclusion L28:   7. cite18†References L29: 
L30: cite19†License: CC BY 4.0†info.arxiv.org L31: arXiv:2601.19089v1 [cs.LG] 27 Jan 2026
L32: 
L33: ^{1}^{1} 1 This is a preprint of a paper accepted at the 39th Canadian Conference on Artificial Intelligence (Canadian AI 2026).
L34: # EPAS: Efficient Training with Progressive Activation Sharing
L35: ###### Abstract.
L36: We present a novel method for E fficient training with P rogressive A ctivation S haring (EPAS). This method bridges progressive training paradigm with the phenomenon of redundant $QK$ (or $KV$) activations across deeper layers of transformers. EPAS gradually grows a sharing region during training by switching decoder layers to activation sharing mode. This results in throughput increase due to reduced compute.
L37: To utilize deeper layer redundancy, the sharing region starts from the deep end of the model and grows towards the shallow end. The EPAS trained models allow for variable region lengths of activation sharing for different compute budgets during inference.
L38: Empirical evaluations with $QK$ activation sharing in LLaMA models ranging from 125M to 7B parameters show up to an 11.1% improvement in training throughput and up to a 29% improvement in inference throughput while maintaining similar loss curve to the baseline models.
L39: Furthermore, applying EPAS in continual pretraining to transform TinyLLaMA into an attention-sharing model yields up to a 10% improvement in average accuracy over state-of-the-art methods, emphasizing the significance of progressive training in cross layer activation sharing models.
L40: ###### keywords
L41: 
L42: Keywords: Low Resource NLP, LLM efficiency, efficient inference, parameter-efficient-training, Many-in-one model.
L43: 
L44: Rezaul Karim\upstairs\affilone,*, Maryam Dialameh\upstairs\affilone\affiltwo, Yang Liu\upstairs\affilone, Boxing Chen\upstairs\affilone, Walid Ahmed\upstairs\affilone
L45: \upstairs\affilone Ascend Team, Huawei Technologies, Toronto, Canada
L46: \upstairs\affiltwo Department of Mechanical and Mechatronics Engineering, University of Waterloo, Canada
L47: \emails\upstairs
L48: *rezaul.karim3@huawei.com
L49: ## 1. Introduction
L50: Recent research in computational efficiency of Transformers has focused on efficient pretraining [cite20†20 ], continual learning [cite21†48 ], fine-tuning [cite22†47 , cite23†31 , cite24†14 ] and inference [cite25†2 , cite26†42 ]. However, holistic approaches to efficient training and inference remains underexplored as evident from large accuracy-efficiency trade-offs in this direction [cite27†27 , cite28†35 ].
L51: Surprisingly, large transformer models are found to compute redundant activations across deeper layers [cite29†29 , cite30†4 , cite31†22 , cite32†37 , cite33†33 ]. Therefore, as a promising yet less explored direction, we focus on utilizing redundancy phenomenon towards an unified efficiency solution to training and inference with minimal tradeoffs to accuracy.
L52: Deeper layers of transformer models have been found to exhibit redundancy in activations of the attention block across layers. For example, multiple deeper layers are found to compute mostly similar attention scores [cite29†29 , cite34†44 , cite35†32 ]. Hence, recent methods reuse $QK$ or $KV$ activations across layers to enhance computational efficiency. These approaches are generally known as activation sharing.
L53: Attention sharing approaches compute only the value ($V$) and reuse the computed attention score directly from a previous layer to make the model compute efficient [cite29†29 , cite34†44 , cite35†32 ]. Since the attention score from the previous layer is not directly available in block factoring-based efficient attention algorithms, such as Flash-Attention [cite36†8 , cite37†9 ], an alternative approach shares $QK$ across layers [cite38†34 ].
L54: Meanwhile, some other approaches have proposed to compute the query ($Q$) and reuse ($KV$) from a previous layer [cite30†4 , cite39†36 ]. The sharing of $QK$ offers greater computational savings, while sharing $KV$ has greater impact in reducing inference memory footprint.
L55: State-of-the-art activation sharing approaches enhance efficiency mostly by sharing activations across the layers of trained models during the inference [cite29†29 ] or follow model distillation [cite38†34 ]. Few models incorporate efficient design from the training phase, and those that do primarily focus on optimizing inference efficiency while overlooking training efficiency [cite39†36 ].
L56: Since efficiency in both training and inference presents diverse design challenges, there is a growing need for a simple, holistic solution that addresses both aspects.
L57: In another direction, efforts for efficient training has presented methods for progressive growth [cite40†15 , cite41†41 , cite42†26 ], progressive layer drop [cite43†45 ], and progressive dataset complexity [cite44†28 ]. Conversely, efficient inference approaches have focused on model pruning [cite45†7 ], distillation [cite46†43 ], progressive low-rank decomposition [cite47†19 ] and step-by-step distillation [cite48†24 , cite49†30 , cite50†23 ].
L58: From a broader perspective, the progressive modification of model during training has proven superior to directly training the modified architecture, often with an additional advantage of many-in-one models [cite51†6 ].
L59: Figure 1. Left: Overall solution from efficient training to inference using EPAS. Right: TinyLLaMA [cite52†46 ] model FLOPs reduction and train/inference throughput improvement expanding $QK$ activation sharing to 25% and 50% of the layers.
L60: The proposed progressive activation sharing combines progressive training and efficient inference in a unified training method for activation sharing models as shown a high level abstraction in Figure cite53†1 . This method allows for utilizing redundancy observed in deeper layers from early phases of training while preserving model accuracy. It improves pretraining throughput to reduce time to accuracy and derives a family of efficient models from a single end-to-end training process.
L61: Additionally, it enables flexible transformation of pretrained models into activation sharing models through a single, efficient continual pretraining process without requiring multiple rounds of knowledge distillation. Instead of sharing activations during inference of a pretrained model, an activation-sharing region is progressively expanded during pretraining or continual pretraining. This makes computation lighter as training progresses.
L62: This hot switching to activation sharing during training is achieved through a switchable decoder block that can conditionally reuse activation. The training algorithm uses a scheduler that toggles activation-sharing at configured intervals, progressively expanding the sharing block to improve training efficiency. The key contributions are:
L63:   * •
L64: 
L65: EPAS enables faster training and flexible efficient model configurations during inference.
L66: 
L67:   * •
L68: 
L69: EPAS transforms pretrained models into efficient ones through continual pretraining, eliminating the need for knowledge distillation.
L70: 
L71:   * •
L72: 
L73: The proposed method achieved superior training and inference throughput while maintaining accuracy on par with baseline.
L74: ## 2. Progressive Activation Sharing
L75: The proposed E fficient training with P rogressive A ctivation S haring (EPAS) method builds transformer models using the proposed switchable activation sharing decoder layer as building block. This decoder layer is a simple yet elegant extension that incorporates conditional activation sharing into the standard decoder layer. The term activation sharing generally refers to reusing some shared $QK$ or $KV$ activations from an early layer.
L76: This help to reduce the computation of somewhat redundant activations in the deeper parts of the model. At a high level, the proposed progressive activation sharing involves gradually growing the number of layers using activation sharing and hence increasing the throughput. In the following, we discuss the details of the newly designed decoder layer and the progressive training algorithm.
L77: ### 2.1. Switchable Activation Sharing Decoder


## Original response 3: epascoreread

EPAS: Efficient Training with Progressive Activation Sharing (https://arxiv.org/html/2601.19089v1)
citeturn28365view0 [wordlim: 200] Crawled: 3 days ago; Content type: text/html; Source: open({"ref_id":"turn28349view2","lineno":77}); Total lines: 305
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract. L16:   2. cite6†1 Introduction L17:   3. cite7†2 Progressive Activation Sharing L18:     1. cite8†2.1 Switchable Activation Sharing Decoder L19:     2. cite9†2.2 Progressive Activation Sharing L20:     3. cite10†2.3 Applications L21:   4. cite11†3 Experiments L22:     1. cite12†3.1 Training efficiency L23:     2. cite13†3.2 Inference efficiency L24:     3. cite14†3.3 Language Model Evaluations L25:     4. cite15†3.4 Ablation Experiment L26:   5. cite16†4 Related Works L27:   6. cite17†5 Conclusion L28:   7. cite18†References L29: 
L30: cite19†License: CC BY 4.0†info.arxiv.org L31: arXiv:2601.19089v1 [cs.LG] 27 Jan 2026
L32: 
L33: ^{1}^{1} 1 This is a preprint of a paper accepted at the 39th Canadian Conference on Artificial Intelligence (Canadian AI 2026).
L34: # EPAS: Efficient Training with Progressive Activation Sharing
L35: ###### Abstract.
L36: We present a novel method for E fficient training with P rogressive A ctivation S haring (EPAS). This method bridges progressive training paradigm with the phenomenon of redundant $QK$ (or $KV$) activations across deeper layers of transformers. EPAS gradually grows a sharing region during training by switching decoder layers to activation sharing mode. This results in throughput increase due to reduced compute.
L37: To utilize deeper layer redundancy, the sharing region starts from the deep end of the model and grows towards the shallow end. The EPAS trained models allow for variable region lengths of activation sharing for different compute budgets during inference.
L38: Empirical evaluations with $QK$ activation sharing in LLaMA models ranging from 125M to 7B parameters show up to an 11.1% improvement in training throughput and up to a 29% improvement in inference throughput while maintaining similar loss curve to the baseline models.
L39: Furthermore, applying EPAS in continual pretraining to transform TinyLLaMA into an attention-sharing model yields up to a 10% improvement in average accuracy over state-of-the-art methods, emphasizing the significance of progressive training in cross layer activation sharing models.
L40: ###### keywords
L41: 
L42: Keywords: Low Resource NLP, LLM efficiency, efficient inference, parameter-efficient-training, Many-in-one model.
L43: 
L44: Rezaul Karim\upstairs\affilone,*, Maryam Dialameh\upstairs\affilone\affiltwo, Yang Liu\upstairs\affilone, Boxing Chen\upstairs\affilone, Walid Ahmed\upstairs\affilone
L45: \upstairs\affilone Ascend Team, Huawei Technologies, Toronto, Canada
L46: \upstairs\affiltwo Department of Mechanical and Mechatronics Engineering, University of Waterloo, Canada
L47: \emails\upstairs
L48: *rezaul.karim3@huawei.com
L49: ## 1. Introduction
L50: Recent research in computational efficiency of Transformers has focused on efficient pretraining [cite20†20 ], continual learning [cite21†48 ], fine-tuning [cite22†47 , cite23†31 , cite24†14 ] and inference [cite25†2 , cite26†42 ]. However, holistic approaches to efficient training and inference remains underexplored as evident from large accuracy-efficiency trade-offs in this direction [cite27†27 , cite28†35 ].
L51: Surprisingly, large transformer models are found to compute redundant activations across deeper layers [cite29†29 , cite30†4 , cite31†22 , cite32†37 , cite33†33 ]. Therefore, as a promising yet less explored direction, we focus on utilizing redundancy phenomenon towards an unified efficiency solution to training and inference with minimal tradeoffs to accuracy.
L52: Deeper layers of transformer models have been found to exhibit redundancy in activations of the attention block across layers. For example, multiple deeper layers are found to compute mostly similar attention scores [cite29†29 , cite34†44 , cite35†32 ]. Hence, recent methods reuse $QK$ or $KV$ activations across layers to enhance computational efficiency. These approaches are generally known as activation sharing.
L53: Attention sharing approaches compute only the value ($V$) and reuse the computed attention score directly from a previous layer to make the model compute efficient [cite29†29 , cite34†44 , cite35†32 ]. Since the attention score from the previous layer is not directly available in block factoring-based efficient attention algorithms, such as Flash-Attention [cite36†8 , cite37†9 ], an alternative approach shares $QK$ across layers [cite38†34 ].
L54: Meanwhile, some other approaches have proposed to compute the query ($Q$) and reuse ($KV$) from a previous layer [cite30†4 , cite39†36 ]. The sharing of $QK$ offers greater computational savings, while sharing $KV$ has greater impact in reducing inference memory footprint.
L55: State-of-the-art activation sharing approaches enhance efficiency mostly by sharing activations across the layers of trained models during the inference [cite29†29 ] or follow model distillation [cite38†34 ]. Few models incorporate efficient design from the training phase, and those that do primarily focus on optimizing inference efficiency while overlooking training efficiency [cite39†36 ].
L56: Since efficiency in both training and inference presents diverse design challenges, there is a growing need for a simple, holistic solution that addresses both aspects.
L57: In another direction, efforts for efficient training has presented methods for progressive growth [cite40†15 , cite41†41 , cite42†26 ], progressive layer drop [cite43†45 ], and progressive dataset complexity [cite44†28 ]. Conversely, efficient inference approaches have focused on model pruning [cite45†7 ], distillation [cite46†43 ], progressive low-rank decomposition [cite47†19 ] and step-by-step distillation [cite48†24 , cite49†30 , cite50†23 ].
L58: From a broader perspective, the progressive modification of model during training has proven superior to directly training the modified architecture, often with an additional advantage of many-in-one models [cite51†6 ].
L59: Figure 1. Left: Overall solution from efficient training to inference using EPAS. Right: TinyLLaMA [cite52†46 ] model FLOPs reduction and train/inference throughput improvement expanding $QK$ activation sharing to 25% and 50% of the layers.
L60: The proposed progressive activation sharing combines progressive training and efficient inference in a unified training method for activation sharing models as shown a high level abstraction in Figure cite53†1 . This method allows for utilizing redundancy observed in deeper layers from early phases of training while preserving model accuracy. It improves pretraining throughput to reduce time to accuracy and derives a family of efficient models from a single end-to-end training process.
L61: Additionally, it enables flexible transformation of pretrained models into activation sharing models through a single, efficient continual pretraining process without requiring multiple rounds of knowledge distillation. Instead of sharing activations during inference of a pretrained model, an activation-sharing region is progressively expanded during pretraining or continual pretraining. This makes computation lighter as training progresses.
L62: This hot switching to activation sharing during training is achieved through a switchable decoder block that can conditionally reuse activation. The training algorithm uses a scheduler that toggles activation-sharing at configured intervals, progressively expanding the sharing block to improve training efficiency. The key contributions are:
L63:   * •
L64: 
L65: EPAS enables faster training and flexible efficient model configurations during inference.
L66: 
L67:   * •
L68: 
L69: EPAS transforms pretrained models into efficient ones through continual pretraining, eliminating the need for knowledge distillation.
L70: 
L71:   * •
L72: 
L73: The proposed method achieved superior training and inference throughput while maintaining accuracy on par with baseline.
L74: ## 2. Progressive Activation Sharing
L75: The proposed E fficient training with P rogressive A ctivation S haring (EPAS) method builds transformer models using the proposed switchable activation sharing decoder layer as building block. This decoder layer is a simple yet elegant extension that incorporates conditional activation sharing into the standard decoder layer. The term activation sharing generally refers to reusing some shared $QK$ or $KV$ activations from an early layer.
L76: This help to reduce the computation of somewhat redundant activations in the deeper parts of the model. At a high level, the proposed progressive activation sharing involves gradually growing the number of layers using activation sharing and hence increasing the throughput. In the following, we discuss the details of the newly designed decoder layer and the progressive training algorithm.
L77: ### 2.1. Switchable Activation Sharing Decoder
L78: The hot switching of decoder layers to activation sharing mode during the progress of training is performed by switching a conditional branching of computation in the decoder layer. A pictorial illustration of this decoder extension, with a particular example of attention sharing, is presented in Figure cite54†2 . This example demonstrates sharing of $Q,~K$ to make attention sharing compatible with Flash-Attention. The extension is quite simple without requiring any additional parameters.
L79: Hence, the modified architecture can reuse previously trained parameters for continual pretraining or post-training. This decoder simply branches out to either reuse some selected activations from a previous layer or to compute with current layer’s own parameters. The most conventional activation sharing models use either attention scores, or $QK$, or $KV$ as the set of activations for this purpose.
L80: Figure 2. The Switchable Activation Sharing Decoder with an example of attention sharing ($Q,K$). This decoder layer extends conventional transformer decoder layer by adding a conditional switching branch to reuse $Q_{i-1},K_{i-1}$ from previous layer instead of computing in current layer(left branch inside dashed box). When not using activation sharing mode, the computation follows the right branch as like convention decoder layer.
L81: ### 2.2. Progressive Activation Sharing
L82: 
L83: The progressive activation sharing approach aims to gradually expand the activation sharing region by switching decoder layers to activation sharing mode throughout the training steps. The growing of sharing layers follows a deterministic sharing strategy. The rationale behind deterministic sharing is to ensure that shared layers continuously grow, ultimately resulting in a model requiring fewer FLOPs than baseline during the inference.
L84: Initially, training begins with all of the $L$ layers of a model, $M$, in compute mode. At this stage the model works like a conventional transformer model [cite55†40 ]. A target sharing region, $S$, defines a list of layers that will progressively transition into activation sharing mode. We found that selecting a set of deeper layers and activated sharing sequentially from deep to shallow layers works well in this scenario.
L85: Over the course of $T$ training steps, a group of $B$ layers at the deep end of $S$ is switched to activation sharing mode at every interval of $I$ training steps. Rather than enabling activation sharing of the whole sharing region from the beginning of training, the method gradually expands the sharing region by gently allowing the model to adapt to activation sharing. Following this training strategy, it ends up with a target model of a predefined maximum activation sharing region.
L86: The steps are depicted with a schematic example in Figure cite56†3 .
L87: In this proposed activation sharing scheme, the layer immediately before the sharing region shares its activations with the layers in sharing group. During the forward pass, if a layer detects that its subsequent layer is in sharing mode, it populates an activation cache with a selected set of activations, $A$. This progressive activation sharing method is compatible with sharing attention scores, $QK$, or $KV$.
L88: The trained model benefits from reduced model FLOPs by leveraging the last state of the activation sharing group. Algorithm cite57†1 presents the progressive activation sharing training algorithm instantiated with $QK$ sharing; the adaptation to other forms of activation sharing, such as $KV$ sharing is straightforward.
L89: (a) Baseline
L90: 
L91: (b) Begin activation sharing
L92: 
L93: (c) Grow sharing region
L94: 
L95: (d) Activation sharing model
L96: Figure 3. An example of EPAS training approach. Beginning with all $L$ layers in compute-mode (e.g., 5 layers here), a region of $B$ layers transition into sharing-mode ( e.g., 1 layer here) at every $I$ step intervals. The progressive growth continues till maximum $S$ layers (e.g., 3 layers here) are in sharing mode. The trained model can be used either all layer in compute mode or up to $S$ layers in activation sharing mode.
L97: 
L98: Algorithm 1 Progressive Activation Sharing
L99: 1: Input: Model, $M$, Interval, $I$, Target Sharing Layers, $S_{c}$, Sharing Region Growth Size $B$
L100: 
L101: 2: Output: Trained model $M$
L102: 
L103: 3: $L$: Layers in Base Model
L104: 
L105: 4: $T$: Training Steps
L106: 
L107: 5: $S$: Layers currently in sharing mode
L108: 
L109: 6: assert $(B\geq 1\And|S_{c}|\geq 1)$
L110: 
L111: 7: assert $(|S_{c}|\mod B=0)$
L112: 
L113: 8: $C\leftarrow[]$, $S\leftarrow[]$
L114: 
L115: 9: for $t=1$ to $T$ do
L116: 
L117: 10:   for $i=0$ to $|L|-1$ do
L118: 
L119: 11:    if $L[i]\in S$ then
L120: 
L121: 12:      $Q_{i},K_{i}\leftarrow Q_{i-1},~K_{i-1}$ from $C$
L122: 
L123: 13:      Compute $V_{i}$
L124: 14:    else
L125: 
L126: 15:      Compute $Q_{i},~K_{i},V_{i}$
L127: 
L128: 16:    end if
L129: 
L130: 17:    Do the rest of the computations
L131: 
L132: 18:    if $L[i+1]$ has sharing on then
L133: 
L134: 19:      $C\leftarrow$ $Q_{i},K_{i}$
L135: 
L136: 20:    end if
L137: 
L138: 21:   end for
L139: 
L140: 22:   if $t\%I==0\And|S_{c}|\geq B$ then
L141: 
L142: 23:    $L_{c}\leftarrow$ pop last $B$ element from $S_{c}$
L143: 
L144: 24:    $S\leftarrow L_{c}+S$ $\triangleright$ Append beginning
L145: 
L146: 25:   end if
L147: 
L148: 26: end for
L149: 
L150: 27: return $M$
L151: ### 2.3. Applications
L152: Progressively growing the sharing block during training gradually reduces model FLOPs and increases training throughput (tokens/sec). This results in reduced training time and cost, while the gradual change in the computation graph allows for training stability. EPAS enhances computational resource utilization and improves pretraining efficiency by minimizing redundant activations, thereby achieving a balanced trade-off between efficiency and model performance.
L153: EPAS can also transform existing pretrained models into activation-sharing architectures while used in continual pretraining setting. Moreover, continual pretraining with EPAS enables flexible sub-network selection during inference, allowing a single end to end training on a small dataset to derive a family of efficient models. This eliminates the need for complex multi-model training or repeated distillation.
L154: During the inference phase, the activation sharing models trained with EPAS can achieve superior throughput compared to baseline models while maintaining similar performance. Attention score sharing, or $QK$ sharing, reduces computational overhead and minimizes $KV$ cache memory requirement as the sharing layers only need to cache $V$. Conversely, $KV$ sharing saves more memory as it eliminates the need to cache both K and V in the sharing layers while offering less computational reduction.
L155: In either of the case, the inference process becomes faster and more resource-efficient compared to baseline model.
L156: ## 3. Experiments
L157: To demonstrate the efficacy of EPAS, we considered $QK$ sharing as a particular instance of activation sharing. The experiments integrate EPAS with open-source transformer-based LLM. In particular, we perform extensive experiment with TinyLLaMA-1.1B [cite52†46 ] as our primary baseline and then further extend our empirical analysis with more LlaMA-based models [cite58†38 , cite59†39 ] ranging from 125M to 7B parameters.
L158: We used a small subset of the open-source SlimPajama-627B dataset for the pretraining and continual pretraining experiments [cite60†11 ]. Since our pretraining experiment is focused on efficiency analysis and comparing training dynamics for small number of training steps rather than training till convergence, this set up is sufficient for the intended purpose.
L159: The empirical analysis compared training and inference efficiency as well as learning capacity during training. We measure theoretical FLOPs reduction, training throughput (tokens/sec) and inference throughput (tokens/sec). For evaluation of transformed pretrained model with continual pretraining setup of EPAS, we used lm-eval-harness [cite61†13 ]. Furthermore, to compare the efficiency across diverse devices, experiments are conducted on Nvidia V100 GPU, Ascend 910A NPU, and Ascend 910B NPU.
L160: Furthermore, we present extensive ablation study for critical understanding and justification of our findings and corresponding design choices. While the proposed method is compatible to share various activations, for the scope of this research we limit empirical analysis on attention sharing only. In particular, we used cross-layer query and key ($QK$) sharing so that the method is compatible with Flash-Attention [cite36†8 , cite37†9 ].
L161: ### 3.1. Training efficiency
L162: To empirically assess training efficiency, we conduct model FLOPs and training throughput analysis by scaling model sizes from 125M to 7B following LLaMA architectures. Although EPAS presents a generalized training algorithm to train activation sharing architecture, we demonstrate for the example of half of the layers in final sharing mode following recent trends [cite39†36 ].
L163: Table cite62†2 summarizes the reduction of theoretical model FLOPs for each of the model when sharing $QK$ across second half of the layers. We observe up to 8% FLOPs reduction with this configuration. Table cite62†2 presents the improvement in training tokens/second with a distributed training setup on 8 V100 GPU. The models show up to 11% train throughput improvement with the above configuration.
L164: Model  | Model FLOPs/sample (TF)
L165: Baseline  | Q/K-Sharing  | Reduction(%)
L166: 125M  | 1.81  | 1.72  | 4.9%
L167: 1.1B  | 14.98  | 14.34  | 4.3%
L168: 3B  | 41.41  | 38.39  | 7.3%
L169: 7B  | 85.62  | 79.21  | 8.1%
L170: Table 1. Model FLOPs per sample in Terra-FLOPs (TF) for baseline versus $QK$ sharing of 50% of the layers.
L171: Model  | Train Tokens/sec
L172: Baseline  | Q/K-Sharing  | Improvement(%)
L173: 125M  | 15458.9  | 17143.1  | 10.8%
L174: 1.1B  | 3850.2  | 4259.8  | 11.1%
L175: 3B  | 1783.1  | 1961.3  | 10.9%
L176: 7B  | 1259.8  | 1367.9  | 8.6%
L177: Table 2. Model size scaling and training efficiency of $QK$ sharing on V100 GPU with distributed training setup.
L178: Figure 4. Smoothed loss versus time while scaling model sizes across LLaMA models with $125M$, $1.1B$, and $3B$ parameters. $QK$ sharing models trained with EPAS also exhibit slightly faster convergence during training in addition to have higher throughput during inference.
L179: Device Name Device Spec Single Device Distributed (8 Device) Baseline Q/K Sharing Improvement(%) Baseline Q/K Sharing Improvement(%) V100 GPU 32GB, 125 TF 4079.6 4423.6 10.8% 3850.2 4259.8 11.1% 910A NPU 32GB, 278 TF 4321.3 4874.2 12.8% 4788.2 5246.9 9.57% 910B NPU 64GB, 378 TF 11354.1 12443.7 9.6% 12902.1 13844.5 7.3%
L180: Table 3. Empirical evidence of training efficiency comparing throughput (tokens/sec) across different hardware for activation sharing ($QK$) in the second half of the layers of the TinyLLaMA model.
L181: We further investigated the learning capacity of activation sharing model when trained with EPAS compared to training baseline model without activation sharing. This experiment was conducted for $0.25M$ tokens per step for $4000$ steps resulting in a total of $1B$ tokens. We consider this setup sufficient for comparing the training dynamics of the baseline and activation sharing models by analyzing loss curves without conducting a full LM benchmark evaluation similar to recent literature [cite39†36 ].
L182: We observe that EPAS has lower loss at equal time and needs less time to achieve equal loss as baseline. We present a loss curve comparison for scaling analysis of training w/ and w/o EPAS in Figure cite63†4 . The comparison of train loss vs. time shows faster training and convergence with EPAS while maintaining similar loss curve pattern as the baseline.
L183: This is particularly evident from the observation that at any given time during training, EPAS shows a lower loss, especially in the early phases of training.
L184: The results in Table cite64†4 compare the total training time and the final validation loss after training. The findings show that EPAS significantly speeds up training, while the difference in final validation loss remains negligibly small (less than 0.05), indicating faster convergence without sacrificing accuracy or increasing the risk of overfitting.
L185: Model  | Train Time (hh:mm:ss)  | Validation Loss
L186: 125M (w/o EPAS)  | 00:54:12  | 3.74
L187: 125M (w/ EPAS)  | 00:50:50  | 3.79
L188: 1.1B (w/o EPAS)  | 03:07:18  | 3.19
L189: 1.1B (w/ EPAS)  | 02:56:33  | 3.22
L190: 3B (w/o EPAS)  | 06:02:46  | 3.06
L191: 3B (w/ EPAS)  | 05:39:11  | 3.09
L192: 7B (w/o EPAS)  | 11:09:26  | 2.99
L193: 7B (w/ EPAS)  | 10:25:17  | 3.04
L194: Table 4. Total time and final validation loss for several LLaMA models of varying parameter sizes, demonstrating that EPAS training is significantly faster with a negligible difference in final validation loss.
L195: 
L196: .
L197: We also considered extending our experiments for various hardware types. For this cross hardware experiment, we fix a model (TinyLLaMA) and perform the same analysis across various hardware. Table cite65†3 presents the observation of training efficiency across different hardware categories. The table shows a negligibly minor variation in train throughput improvement while changing hardware.
L198: In particular, the $QK$ sharing model still maintains 8-10% train throughput improvement across the three types of hardware. This evidence further justifies that activation sharing makes a generic efficiency improvement on model’s computation that persists across varieties of device specs.
L199: Model Inference Throughput(tok/sec) Baseline 25% Sharing 50% Sharing 125M 63.8 78.3 (22.7%) 82.4 (29.2%) 1.1B 39.1 42.9 (9.7%) 44.8 (14.6%) 3B 38.1 40.9 (7.3%) 43.2 (13.4%) 7B 24.46 25.27 (3.3%) 26.03 (6.4%)
L200: 
L201: Table 5. Inference throughput on V100 GPU with $QK$ sharing on 25% and 50% of the layer in sharing mode.
L202: ### 3.2. Inference efficiency
L203: We compare the generation throughput in terms of tokens/sec to measure the inference efficiency improvement of the proposed method. Since models trained with EPAS present a flexible architecture that can be used with various number of activation sharing layers during inference, we present inference throughput for sharing $QK$ activations for 25% and 50% of the layers. For example, LLaMA1.1B has 22 layers, hence 25% and 50% indicates 5 and 11 layers in sharing mode respectively.
L204: We observe a 3–22% improvement in generation throughput when sharing 25% of the layers, and a 6–30% improvement when sharing 50% of the layers across different models. The results are summarized Table cite66†5 .
L205: Model WG PIQA BoolQ ARC-C ARC-E OBQA HS SciQ LM(oa) LM(std) RTE Average w/o EPAS (No Sharing) 59.12 73.56 56.09 32.68 55.51 36.80 61.45 84.20 56.70 50.55 57.04 56.70 w/ EPAS (No Sharing) 58.25 73.01 63.33 31.57 56.44 36.20 58.17 85.90 56.10 52.45 56.32 57.07 w/o EPAS (Sharing 3/22)$\dagger$ 60.14 73.50 48.41 32.25 53.91 37.40 60.48 75.80 25.00 23.17 47.65 48.88 w/ EPAS (Sharing 3/22) 59.27 73.07 62.72 33.02 56.14 36.20 58.72 83.60 49.97 47.80 52.35 55.71 w/o EPAS (Sharing 5/22)$\dagger$ 55.64 67.03 48.41 27.13 42.55 31.00 51.51 75.80 25.00 23.17 47.65 44.99 w/ EPAS (Sharing 5/22) 58.02 73.18 60.70 31.23 55.85 36.00 57.95 83.10 47.58 44.69 50.90 54.47
L206: Table 6. Evaluation of multiple inference configurations from a single trained model. The EPAS model uses continual pretraining with a target sharing region of five layers while varied sharing region length during inference. $\dagger$ represents our re-implementation of  [cite29†29 ] for smaller model for various $QK$ sharing settings.
L207: ### 3.3. Language Model Evaluations
L208: We consider to evaluate model trained with EPAS in a continual pretraining setup to transform base models to attention-sharing models. We follow this direction due to the resource intensity of pretraining from scratch. For fair comparison, we also do continual pretraining on base models with same dateset.
L209: This experiment begins with a pretrained checkpoint and follows continual pretraining with progressively growing the activation sharing block from the deep end of the model towards the shallow end gradually growing one large activation sharing region. No additional sophisticated training approaches, e.g., knowledge distillation or additional auxiliary loss computation are used. In particular, we consider a pretrained TinyLLaMA model as baseline.
L210: Due to limited resources we constrain the activation sharing block to grow up to 25% of the model depth( e.g., 5 out of 22 layers). The training is done in a distributed setup of 8 device with a batch size 8 per device and gradient accumulation steps 16 to match the effective token per step being equal to the baseline pretraining configuration ( e.g., $8\times 8\times 16\times 2048=2M$). The training is run for $2K$ steps resulting in total $4$ billion tokens.
L211: We use the lm-eval-harness [cite61†13 ] for evaluating the models on LM benchmarks.
L212: The checkpoint from continual pretraining with EPAS is evaluated against applying inference time attention sharing, known as Beyond-KV-Cache [cite29†29 ] under various activation sharing configurations. We first compare the baseline and EPAS trained model with both of the models in full-compute mode. Then, we compare by using three and five layers in sharing mode. We observe that the model trained without EPAS shows a large drop in accuracy when evaluated with sharing mode.
L213: In contrast, EPAS trained model can retain most of the accuracy in attention sharing mode. When using five layers in sharing mode for both of the models, the EPAS trained model shows around 10% higher accuracy. The results are presented in Table cite67†6 , where each row pair shares the same activation sharing configuration.
L214: Full model evaluation during inference without activation sharing improves accuracy in the EPAS-trained model. As expected, baseline accuracy declines more rapidly as additional layers are included in the sharing block. In contrast, the EPAS-trained model maintains robust accuracy as the activation sharing block expands. Notably, with a $QK$ sharing block size of five layers ( 25% of model depth), the EPAS-trained model outperforms the baseline by approximately 12%.
L215: These findings highlight EPAS’s effectiveness in preserving accuracy while progressively sharing activations, offering a robust approach for efficient transformer model training and inference.
L216: Model PIQA WG BoolQ OBQA HS Excluding last layer 73.29 58.01 52.94 36.00 58.66 Including last layer 73.39 59.12 56.51 36.80 59.11
L217: 
L218: Table 7. LM benchmark evaluation of continual pretraining reveals a minor difference between including or excluding the last layer in activation sharing.
L219: ### 3.4. Ablation Experiment
L220: Impact of Last Layer. Recent research presents diverging perspectives on activation sharing regarding the role of the final layer. One approach argues for excluding the last layer or retaining it solely during inference due to its distinct attention pattern [cite29†29 ], while an alternative view supports its inclusion within the activation-sharing block [cite39†36 ].
L221: To assess the optimal configuration, we conducted an analysis using continual pretraining of TinyLLaMA with EPAS, evaluating LM benchmark performance on a small dataset under two conditions: exclusion versus inclusion of the last layer within sharing blocks. As summarized in Table cite68†7 , the results indicate minimal performance differences, with a slight advantage observed when incorporating the last layer during training. Consequently, we adopt this strategy in our approach.
L222: Single vs. Multiple Sharing Block. Recent approaches of attention, $Q,~K$ and $K,~V$ sharing demonstrate two distinct methodologies for applying activation sharing across multiple layers. One line of research advocates for small activation-sharing blocks [cite34†44 , cite38†34 ] while others argue that such fine-grained partitioning adds unnecessary complexity and computational overhead per block and favors instead a large activation-sharing block in the deeper end of the model [cite39†36 ].
L223: To examine the trade-off between simplicity and computational efficiency, we conduct a comparative experiment with an equal number of layers in activation reuse mode for TinyLLaMA. One setup employs three groups of two activation-reusing layers, while the computationally equivalent model with a single block arranges three activation-reusing layers sequentially, as schematically depicted in Fig. cite69†5 .
L224: Results in Table cite70†8 consistently show superior performance with a single large activation-sharing block, attributed to deeper-layer sharing. This trend holds across training settings with and without EPAS. Adhering to Occam’s razor, we favor the simplicity of a single large sharing block, as additional complexity yields no clear advantage.
L225: Figure 5. Schematic illustration of layer grouping: multiple small blocks versus a single large block. The colors indicate compute- and sharing-mode. The number of layers shown is for illustrative purposes; both approaches can accommodate a variable number of layers.
L226: 
L227: Model PIQA WG BoolQ OBQA HS MB (w/o EPAS) 72.25 58.01 49.02 36.20 60.15 SB (w/o EPAS) 73.50 60.14 48.41 37.40 60.84 MB (w/ EPAS) 73.67 57.93 60.06 36.40 58.28 SB (w/ EPAS) 73.45 58.41 60.31 37.00 58.55
L228: Table 8. Results comparing using a single large sharing block (SB) vs. multiple small sharing blocks (MB)
L229: ## 4. Related Works

