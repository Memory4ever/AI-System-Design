# Exact-v1 primary cached excerpts — 2601.19634

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Original response 1: adpointnew0

AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation (https://arxiv.org/html/2601.19634v1)
citeturn28178view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19634v1","pattern":"Action-Aware"}); Total lines: 400
No matching text found for "Action-Aware"--------------------------------------------------------------------------------


## Original response 2: adpointnew0

AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation (https://arxiv.org/html/2601.19634v1)
citeturn28178view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19634v1","pattern":"3.2"}); Total lines: 400
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†2.1 Vision-Language-Action Models L19:     2. cite9†2.2 Efficient VLA Strategies L20:   4. cite10†3 Method L21:     1. cite11†3.1 Overview L22:     2. cite12†3.2 Action-Context-aware Unified Routing L23:     3. cite13†3.3 From Unified Gating to Practical Speedups L24:     4. cite14†3.4 Optimization L25:   5. cite15†4 Experiment L26:     1. cite16†4.1 Experimental Setup L27:     2. cite17†4.2 Comparison with State-of-the-Art L28:     3. cite18†4.3 Ablation Study L29:     4. cite19†4.4 More Exploration L30:   6. cite20†5 Conclusion L31:   7. cite21†References L32: cite22†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L33: 
L34: arXiv:2601.19634v1 [cs.RO] 27 Jan 2026
L35: # AC^{2}-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation
L36: Wenda Yu Affiliation: Tongji University Email: yu_wenda@126.com    Tianshi Wang ^{†}^{†}thanks: Corresponding author. Affiliation: Tongji University Email: tswang0116@163.com    Fengling Li Affiliation: University of Technology Sydney Email: fenglingli2023@gmail.com    Jingjing Li Affiliation: University of Electronic Science and Technology of China Email:
L37: lijin117@yeah.net    Lei Zhu Affiliation: Tongji University Email: leizhu0608@gmail.com
L38: ###### Abstract
L39: Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet their closed-loop deployment is hindered by the high latency and compute cost of repeatedly running large vision-language backbones at every timestep. We observe that VLA inference exhibits structured redundancies across temporal, spatial, and depth dimensions, and that most existing efficiency methods ignore action context, despite its central role in embodied tasks.
L40: To address this gap, we propose Action-Context-aware Adaptive Computation for VLA models (AC^{2}-VLA), a unified framework that conditions computation on current visual observations, language instructions, and previous action states. Based on this action-centric context, AC^{2}-VLA adaptively performs cognition reuse across timesteps, token pruning, and selective execution of model components within a unified mechanism.
L41: To train the adaptive policy, we introduce an action-guided self-distillation scheme that preserves the behavior of the dense VLA policy while enabling structured sparsification that transfers across tasks and settings. Extensive experiments on robotic manipulation benchmarks show that AC^{2}-VLA achieves up to a 1.79$\times$ speedup while reducing FLOPs to 29.4% of the dense baseline, with comparable task success. Source codes can be found at cite23†https://github.com/SunnyYWD/AC-2-VLA†github.com .
L42: ## 1 Introduction
L43: 
L44: cite24†Image: Refer to caption Figure 1: Comparison of efficient VLA computation strategies. Existing methods typically apply cache reuse, token pruning, or layer skipping based on visual or heuristic cues in an uncoordinated manner, resulting in action-context-agnostic efficiency. In contrast, AC^{2}-VLA leverages action context to jointly gate cache reuse, token pruning, and layer skipping for action-context-aware efficiency.
L45: Recent progress in vision-language foundation models and large-scale robot datasets such as Open X-Embodiment [cite25†15 ] have accelerated the development of generalist Vision-Language-Action (VLA) models. In closed-loop embodied tasks, these models must deliver low-latency decisions with stable closed-loop control over long-horizon tasks.
L46: Representative methods such as RT-2 [cite26†3 ] and OpenVLA [cite27†8 ] demonstrate that large multimodal backbones can follow language instructions and generalize to diverse tasks. More recent policies such as CogACT [cite28†9 ] further improve control by generating expressive action trajectories via diffusion-based modeling.
L47: However, deploying these models remains challenging because inference repeatedly executes a computationally expensive vision-language backbone at every control step, resulting in high latency and compute cost, reducing control frequency, and compromising real-time responsiveness in dynamic environments.
L48: To mitigate these deployment challenges, recent work has explored various efficiency mechanisms for VLA models. Static compression methods such as pruning [cite29†21 ] and quantization [cite30†6 ] reduce model size but cannot adapt to changing task complexity. Dynamic computation techniques, including token pruning [cite31†18 ] and layer skipping [cite32†22 ], adjust compute online, while caching approaches such as VLA-Cache [cite33†20 ] exploit temporal redundancy by reusing features across adjacent timesteps.
L49: Despite these advances, most existing methods make compute allocation decisions primarily based on visual cues, which can be suboptimal for robot manipulation. In embodied tasks, visual complexity does not necessarily correlate with control difficulty: visually simple scenes may require full-capacity reasoning for precise interactions, while visually complex transit phases may allow more aggressive pruning.
L50: Based on this insight, we present Action-Context-aware Adaptive Computation for VLA models (AC^{2}-VLA), as illustrated in Fig. cite34†1 . AC^{2}-VLA dynamically allocates computation along the temporal, spatial, and depth dimensions, guided by the action-centric context that is directly relevant to embodied tasks.
L74: cite45†Image: Refer to caption Figure 2: Overview of the proposed AC^{2}-VLA. At each timestep, the model builds an action-prior condition $\mathbf{c}_{t}$ from the current observation, instruction, and action context, and uses a unified router to generate token pruning, layer skipping, and cache reuse gates, enabling efficient computation and low-latency control.
L75: ## 3 Method
L76: ### 3.1 Overview
L77: 
L78: Given a visual observation $x_{t}$ and a language instruction $u$, a VLA model predicts an action chunk $\mathbf{a}_{t:t+H}$ with horizon $H$. We consider a generic VLA pipeline that factorizes action generation into a multimodal backbone and an action head:
L79: 
L80:  | $$\mathbf{z}_{t}=f_{\mathrm{VLM}}(x_{t},u),\qquad\mathbf{a}_{t:t+H}\sim p_{\phi}(\mathbf{a}\mid\mathbf{z}_{t}).$$  |  | (1)
L81: Here, $p_{\phi}$ can be instantiated as an autoregressive decoder or a diffusion/flow-based trajectory generator, depending on the underlying VLA policy.
L82: 
L83: In real-time deployment, inference is bottlenecked by repeatedly executing the VLM backbone at every control step. We observe structured computation redundancies along three complementary axes:
L84: 
L85:   1. (i)
L86: 
L87: Temporal redundancy: backbone representations can be reused across adjacent timesteps;
L88: 
L89:   2. (ii)
L90: Spatial redundancy: only a subset of vision tokens is necessary for action prediction;
L91: 
L92:   3. (iii)
L93: 
L94: Depth redundancy: executing fewer backbone layers often suffices with minimal performance loss.
L95: To exploit these redundancies within a unified mechanism, AC^{2}-VLA introduces an action-prior router, as shown in Fig. cite46†2 . At each timestep, conditioned on the action-centric context $\mathbf{c}_{t}$, an action-prior router generates a set of computation gates for temporal reuse, spatial token selection, and depth-wise conditional execution:
L96:  | $\displaystyle\mathbf{p}_{t}=$  | $\displaystyle[p^{\mathrm{cache}}_{t};\ \mathbf{p}^{\mathrm{topk}}_{t};\ \mathbf{p}^{\mathrm{lay}}_{t}],$  |  | (2)
L97:  | $\displaystyle p^{\mathrm{cache}}_{t}\in[0,1],$  | $\displaystyle\mathbf{p}^{\mathrm{topk}}_{t}\in[0,1]^{N_{v}},\ \ \ \ \mathbf{p}^{\mathrm{lay}}_{t}\in[0,1]^{L},$  |
L98: where $N_{v}$ and $L$ denote the numbers of vision tokens and transformer layers, respectively. The cache gate $p^{\mathrm{cache}}_{t}$ determines whether to reuse cached backbone representations, while $\mathbf{p}^{\mathrm{topk}}_{t}$ and $\mathbf{p}^{\mathrm{lay}}_{t}$ control token pruning and conditional layer execution. We train the router via teacher-student distillation with lightweight regularization to preserve dense-policy behavior under structured sparsification.
L99: Overall, AC^{2}-VLA jointly optimizes temporal reuse, token selection, and conditional layer execution, enabling efficient inference for closed-loop robotic manipulation.
L100: ### 3.2 Action-Context-aware Unified Routing
L101: AC^{2}-VLA is driven by an action-prior condition vector $\mathbf{c}_{t}$ that explicitly encodes the robot’s action context. In closed-loop control, the next action distribution is strongly shaped by the ongoing motion state, making the previous action $\mathbf{a}_{t-1}$ a natural and inexpensive prior for allocating computation. We therefore use $\mathbf{a}_{t-1}$, parameterized consistently with the action head, as the primary routing signal.
L102: When no previous action is available at the first step, we set $\mathbf{a}_{t-1}=\mathbf{0}$ and rely on lightweight visual and instruction summaries to generate initial gates.
L103: Let $\mathbf{V}_{t}\in\mathbb{R}^{N_{v}\times d_{v}}$ denote per-token vision features, and we summarize them with a mean-max mixture:
L104: 
L105:  | $$\mathbf{s}^{v}_{t}=\tfrac{1}{2}\!\left(\mathrm{MeanPool}(\mathbf{V}_{t})+\mathrm{MaxPool}(\mathbf{V}_{t})\right).$$  |  | (3)
L106: 
L107: For language, we avoid an additional full forward by pooling embedded instruction tokens $\mathbf{E}_{t}\in\mathbb{R}^{T\times d}$:
L108:  | $$\mathbf{s}^{u}_{t}=\tfrac{1}{2}\!\left(\mathbf{E}_{t}[\ell_{t}]+\mathrm{MeanPool}(\mathbf{E}_{t})\right),$$  |  | (4)
L109: 
L110: where $\ell_{t}$ denotes the last valid token index under the attention mask when available, otherwise we use mean pooling.
L111: We embed the action-head step index $\tau_{t}$ with a sinusoidal encoder $\mathbf{e}(\tau_{t})$, which captures the internal generation progress of the action head. When reuse is enabled, we additionally include a cache-state cue $\mathbf{s}^{c}_{t}$ encoding the quantized action-delta proxy used for cache keying, together with compact cache statistics and an availability probe. All inputs are projected to a shared hidden size and fused by an MLP:
L112:  | $\displaystyle\mathbf{c}_{t}=f_{\mathrm{fuse}}($  | $\displaystyle\psi_{a}(\mathbf{a}_{t-1}),\ \psi_{v}(\mathbf{s}^{v}_{t}),\ \psi_{u}(\mathbf{s}^{u}_{t}),$  |  | (5)
L113:  |  | $\displaystyle\psi_{\tau}(\mathbf{e}(\tau_{t})),\ \psi_{c}(\mathbf{s}^{c}_{t})).$  |
L114: 
L115: In implementation, vision tokens and pooled summaries are detached before entering the router to prevent gradients from flowing into heavyweight backbone components through the routing pathway.
L116: Given $\mathbf{c}_{t}$, the router predicts three gate families: a reuse probability $p^{\mathrm{cache}}_{t}$, token keep scores $\mathbf{p}^{\mathrm{topk}}_{t}$, and layer execution gates $\mathbf{p}^{\mathrm{lay}}_{t}$. We detail each gate in the following.
L117: 
L118: Cache reuse gate. We predict a scalar reuse probability:
L119: 
L120:  | $$p^{\mathrm{cache}}_{t}=\sigma(\frac{\mathbf{w}^{\top}\mathbf{c}_{t}+b}{T_{\mathrm{cache}}}),$$  |  | (6)
L121: where $T_{\mathrm{cache}}$ controls gate sharpness. A high $p^{\mathrm{cache}}_{t}$ indicates a reuse request, while an actual reuse occurs only when the cache lookup succeeds.
L122: 
L123: Token pruning gate. For each vision token $\mathbf{v}_{t,i}$, we predict its keep score via action-conditioned matching:
L124: 
L125:  | $$p^{\mathrm{topk}}_{t,i}=\sigma(\langle W_{v}\mathbf{v}_{t,i},\ W_{c}\mathbf{c}_{t}\rangle+\gamma\,g_{t,i}),$$  |  | (7)
L126: where $g_{t,i}$ is an optional lightweight bias such as a geometric prior derived from the current observation. During inference, tokens are compacted by keeping the top-ranked ones according to $p^{\mathrm{topk}}_{t,i}$.
L127: 
L128: Layer skipping gate. We predict per-layer execution probabilities:
L129: 
L130:  | $$p^{\mathrm{lay}}_{t,\ell}=\sigma((W_{\ell}\mathbf{c}_{t}+\mathbf{b}_{\ell})_{\ell}),\qquad\ell=1,\dots,L,$$  |  | (8)
L131: with bias initialization that favors near-dense execution early in training. At runtime, transformer blocks with low $p^{\mathrm{lay}}_{t,\ell}$ are conditionally bypassed to reduce depth-wise computation.
L132: ### 3.3 From Unified Gating to Practical Speedups
L133: 
L134: We next describe how the unified gates translate into practical inference speedups in AC^{2}-VLA, through feature reuse across timesteps, spatial token pruning with compaction, and depth-wise conditional execution. Algorithm cite47†1 summarizes the resulting inference-time procedure.
L135: Cache reuse. When the router predicts a high reuse probability $p^{\mathrm{cache}}_{t}$, we attempt to bypass the expensive multimodal backbone forward by querying a cognition cache. Specifically, we build a compact and robust cache key that captures both motion continuity and visual consistency. We first pool the vision tokens:
L136: 
L137:  | $$\bar{\mathbf{v}}_{t}=\mathrm{MeanPool}(\mathbf{V}_{t}),$$  |  | (9)
L138: 
L139: and form the cache key as
L140:  | $$k_{t}=(\mathrm{Quant}(\lVert\Delta\mathbf{a}_{t}\rVert),\ \mathrm{Hash}(\bar{\mathbf{v}}_{t})),$$  |  | (10)
L141: 
L142: where $\mathrm{Quant}(\lVert\Delta\mathbf{a}_{t}\rVert)$ is an action-delta norm proxy, and $\mathrm{Hash}(\bar{\mathbf{v}}_{t})$ is a lightweight vision hash for state matching. The robust hash normalizes $\bar{\mathbf{v}}_{t}$, applies a fixed random projection, and quantizes before hashing.
L143: We distinguish a reuse request from an actual cache hit $h_{t}\in\{0,1\}$. When a hit occurs, we directly reuse the cached multimodal representation $\mathbf{z}_{t}$ and skip the VLM backbone forward, otherwise we compute $\mathbf{z}_{t}=f_{\mathrm{VLM}}(x_{t},u)$ as usual. To keep cache population consistent with the router’s intent, we only write back the newly computed $\mathbf{z}_{t}$ when reuse was requested but the lookup missed.
L144: Token Pruning. Token gating determines which vision tokens should be retained. To obtain real wall-clock speedups beyond attention masking, we perform token pruning by physically removing pruned tokens and shortening the transformer sequence. Let $\mathbf{m}_{t}\in\{0,1\}^{N_{v}}$ denote the keep mask. Compaction produces
L164: where $F_{\ell}(\cdot)$ denotes the $\ell$-th transformer block and $\alpha_{t,\ell}\in[0,1]$ is the layer gate derived from $p^{\mathrm{lay}}_{t,\ell}$. During training, $\alpha_{t,\ell}$ remains soft; at inference, it is binarized so that inactive samples bypass the layer entirely.
L165: 
L166: For efficient execution, active samples are dynamically grouped into a sub-batch to run $F_{\ell}(\cdot)$, and the results are scattered back to the full batch.
L167: 
L168: Algorithm 1 AC^{2}-VLA inference for a single control step $t$
L169: Input: visual observation $x_{t}$, instruction $u$, previous action $\mathbf{a}_{t-1}$, step index $\tau_{t}$, cache $\mathcal{C}$
L170: Output: action chunk $\mathbf{a}_{t:t+H}$
L171: 
L172: 1:  $\mathbf{V}_{t}\leftarrow f_{\mathrm{vis}}(x_{t})$; $\bar{\mathbf{v}}_{t}\leftarrow\mathrm{MeanPool}(\mathbf{V}_{t})$
L173: 
L174: 2:  $\mathbf{s}^{v}_{t}\leftarrow\tfrac{1}{2}(\mathrm{MeanPool}(\mathbf{V}_{t})+\mathrm{MaxPool}(\mathbf{V}_{t}))$
L175: 
L176: 3:  $\mathbf{s}^{u}_{t}\leftarrow\mathrm{EmbedPool}(u)$
L177: 4:  $\mathbf{c}_{t}\leftarrow f_{\mathrm{fuse}}(\psi_{a}(\mathbf{a}_{t-1}),\psi_{v}(\mathbf{s}^{v}_{t}),\psi_{u}(\mathbf{s}^{u}_{t}),\psi_{\tau}(\mathbf{e}(\tau_{t})),\psi_{c}(\mathbf{s}^{c}_{t}))$
L178: 
L179: 5:  $(p^{\mathrm{cache}}_{t},\mathbf{p}^{\mathrm{topk}}_{t},\mathbf{p}^{\mathrm{lay}}_{t})\leftarrow\mathcal{R}(\mathbf{c}_{t})$
L180: 
L181: 6:  $h_{t}\leftarrow 0$
L182: 
L183: 7:  if ReuseReq$(p^{\mathrm{cache}}_{t})$ then
L184: 
L185: 8:   $\Delta\mathbf{a}_{t}\leftarrow\mathrm{DeltaProxy}(\mathbf{a}_{t-1})$
L186: 9:   $k_{t}\leftarrow(\mathrm{Quant}(\|\Delta\mathbf{a}_{t}\|),\,\mathrm{Hash}(\bar{\mathbf{v}}_{t}))$
L187: 
L188: 10:   $(h_{t},\mathbf{z}_{t})\leftarrow\mathcal{C}.\mathrm{Get}(k_{t})$
L189: 
L190: 11:  end if
L191: 
L192: 12:  if $h_{t}=0$ then
L193: 
L194: 13:   $\mathbf{m}_{t}\leftarrow\mathrm{TopKMask}(\mathbf{p}^{\mathrm{topk}}_{t})$; $\mathbf{g}_{t}\leftarrow\mathrm{BinGate}(\mathbf{p}^{\mathrm{lay}}_{t})$
L195: 
L196: 14:   $(\tilde{\mathbf{V}}_{t},\boldsymbol{\pi}_{t},N_{v}^{\mathrm{orig}})\leftarrow\mathrm{Compact}(\mathbf{V}_{t},\mathbf{m}_{t})$
L197: 15:   $\mathrm{pos}_{t}\leftarrow\mathrm{RoPEAlign}(\boldsymbol{\pi}_{t},N_{v}^{\mathrm{orig}})$
L198: 
L199: 16:   $\mathbf{z}_{t}\leftarrow f_{\mathrm{VLM}}(x_{t},u;\tilde{\mathbf{V}}_{t},\mathrm{pos}_{t},\mathbf{g}_{t})$
L200: 
L201: 17:   if ReuseReq$(p^{\mathrm{cache}}_{t})$ then
L202: 
L203: 18:    $\mathcal{C}.\mathrm{Put}(k_{t},\mathbf{z}_{t})$ {write back only on request & miss}
L204: 
L205: 19:   end if
L206: 
L207: 20:  end if
L208: 
L209: 21:  $\mathbf{a}_{t:t+H}\leftarrow p_{\phi}(\mathbf{a}\mid\mathbf{z}_{t};\tau_{t})$
L210: 
L211: 22:  return $\mathbf{a}_{t:t+H}$
L212:   Google Robot  |   Method  |   Success Rate ($\uparrow$)
L213:   PickCan  |   MoveNear  |   Drawer  |   DrawerApple  |   Average
L214:      Visual Matching  |   RT-1  |   85.7%  |   44.2%  |   73.0%  |   6.5%  |   52.4%
L215:   RT-1-X  |   56.7%  |   31.7%  |   59.7%  |   21.3%  |   42.4%
L216:   RT-2-X  |   78.7%  |   77.9%  |   25.0%  |   3.7%  |   46.3%
L217:   Octo-Base  |   17.0%  |   4.2%  |   22.7%  |   0.0%  |   11.0%
L218:   OpenVLA  |   18.0%  |   56.3%  |   63.0%  |   0.0%  |   34.3%
L219:   CogACT  |   91.3%  |   85.0%  |   71.8%  |   50.9%  |   74.8%
L220:   AC^{2}-VLA  |   97.2%  |   82.7%  |   80.6%  |   46.8%  |   76.8%
L221:      Variant Aggregation  |   RT-1  |   89.8%  |   50.0%  |   32.3%  |   2.6%  |   43.7%
L222:   RT-1-X  |   49.0%  |   32.3%  |   29.4%  |   10.1%  |   30.2%
L223:   RT-2-X  |   82.3%  |   79.2%  |   35.3%  |   20.6%  |   54.4%
L224:   Octo-Base  |   0.6%  |   3.1%  |   1.1%  |   0.0%  |   1.2%
L225:   OpenVLA  |   60.8%  |   67.7%  |   28.8%  |   0.0%  |   39.3%
L226:   CogACT  |   89.6%  |   80.8%  |   28.3%  |   46.6%  |   61.3%
L227:   AC^{2}-VLA  |   88.7%  |   84.4%  |   28.2%  |   45.1%  |   61.6%
L228: Table 1: Google Robot success rates on SIMPLER under two evaluation settings. Most baseline results are reported by CogACT, and we add the AC^{2}-VLA row by evaluating our method under the same protocol.
L229: ### 3.4 Optimization
L230: 
L231: We train the router to preserve dense-policy behavior under sparse execution with:
L232: 
L233:  | $$\mathcal{L}=\mathcal{L}_{distill}+\mathcal{L}_{reg}+\mathcal{L}_{temp}.$$  |  | (16)
L234: 
L235: Action-guided self-distillation. We use a teacher-student scheme, where the teacher runs the dense policy and the student executes routed sparse inference, including cache reuse, token pruning, and layer skipping. We distill both action outputs and cognition features:
L236:  | $$\mathcal{L}_{distill}=\lambda_{\epsilon}\big\lVert\hat{\boldsymbol{\epsilon}}^{stu}-\hat{\boldsymbol{\epsilon}}^{tea}\big\rVert_{2}^{2}+\lambda_{z}\mathcal{D}\!\left(\mathbf{z}^{stu}_{t},\mathbf{z}^{tea}_{t}\right).$$  |  | (17)
L237: 
L238: where $\hat{\boldsymbol{\epsilon}}$ denotes the action prediction, and $\mathbf{z}_{t}$ is the backbone representation. $\lambda_{\epsilon}$ and $\lambda_{z}$ control the relative weights, and $\mathcal{D}(\cdot,\cdot)$ is a feature-matching distance.
L239: Regularization and temporal smoothing. We add $\mathcal{L}_{reg}$ to enforce target token/layer budgets and supervise the reuse gate, and $\mathcal{L}_{temp}$ to penalize abrupt changes in gating decisions across timesteps for stable closed-loop control.
L240: WidowX Robot  | Method  | Success Rate ($\uparrow$)
L241: Put Spoon on Towel  | Put Carrot on Plate  | Stack Cube  | Put Eggplant in Basket  | Average
L242: SIMPLER Visual Matching  | RT-1-X  | 0.0%  | 4.2%  | 0.0%  | 0.0%  | 1.1%
L243: Octo-Base  | 15.8%  | 12.5%  | 0.0%  | 41.7%  | 17.5%
L244: Octo-Small  | 41.7%  | 8.2%  | 0.0%  | 56.7%  | 26.7%
L245: OpenVLA  | 4.2%  | 0.0%  | 0.0%  | 12.5%  | 4.2%
L246: CogACT  | 71.7%  | 50.8%  | 15.0%  | 67.5%  | 51.3%
L247: AC^{2}-VLA  | 71.2%  | 58.0%  | 14.8%  | 74.0%  | 54.5%
L248: Table 2: WidowX Visual Matching success rates on SIMPLER. Most baseline results are reported by CogACT, and we add the AC^{2}-VLA row by evaluating our method under the same protocol.
L249: ## 4 Experiment
L250: ### 4.1 Experimental Setup
L251: 
L252: Backbones. We build AC^{2}-VLA on CogACT [cite28†9 ], a diffusion-based VLA model with a Prismatic-7B vision-language backbone and a DiT-Base action head. To isolate routing effects, we freeze the pre-trained vision and language backbones and optimize only the lightweight routing modules, while keeping the action head unchanged with 8 denoising steps.
L253: Implementation Details. All experiments are conducted on a node with NVIDIA RTX 5090 GPUs. We initialize from the CogACT-Base checkpoint [cite28†9 ] and train on the Bridge subset of Open X-Embodiment [cite25†15 ] for 3,000 steps using AdamW with batch size 48 and learning rate $1\times 10^{-6}$. We use an action horizon of $H=15$ with 8 diffusion steps. Unless noted otherwise, AC^{2}-VLA enables action distillation, sets the maximum token pruning ratio to 0.6, and uses a cache reuse threshold of 0.2.
L254: Benchmarks. We evaluate on SIMPLER [cite48†11 ], a high-fidelity simulation benchmark for robotic manipulation that aims to narrow the real-to-sim gap. We report results on two robot embodiments under three protocols:
L255: 
L256:   * •
L257: 
L258: Google Robot Visual Matching: Tests generalization in visually matched real-world conditions on tasks including Pick Coke Can, Move Near, Open/Close Drawer, and Place Apple.
L259: 
L260:   * •
L261: Google Robot Variant Aggregation: Introduces variations in background, lighting, and distractors, providing a more challenging robustness setting.
L262: 
L263:   * •
L264: 
L265: WidowX Visual Matching: Evaluates fine-grained manipulation on WidowX with tasks including Put Spoon on Towel, Put Carrot on Plate, Stack Cube, and Put Eggplant in Basket.
L266: Following standard SIMPLER protocols, we use 3 Hz control with 513 Hz simulation for Google Robot and 5 Hz control with 500 Hz simulation for WidowX. Episodes are capped at 80 steps for Google Robot and 120 steps for WidowX to penalize inefficient or stalled behaviors.
L267: Setting  | Method  | Success Rate ($\uparrow$)  | Speed-up ($\uparrow$)  | FLOPs ($\downarrow$)
L268: PickCan  | MoveNear  | Drawer  | DrawerApple  | Average
L269: Visual Matching  | CogACT  | 91.3%  | 85.0%  | 71.8%  | 50.9%  | 74.8%  | 1.00$\times$  | 100.0%
L270: VLA-Cache  | 92.0%  | 83.3%  | 70.5%  | 51.6%  | 74.4%  | 1.36$\times$  | 80.1%
L271: EfficientVLA  | 95.3%  | 83.3%  | 70.3%  | 56.5%  | 76.4%  | 1.59$\times$  | 45.1%
L272: FastV  | 92.6%  | 81.4%  | 69.8%  | 52.4%  | 74.1%  | 1.21$\times$  | 42.0%
L273: MoLe-VLA  | 86.4%  | 80.2%  | 70.6%  | 50.4%  | 71.9%  | 1.53$\times$  | 47.4%
L274: AC^{2}-VLA  | 97.2%  | 82.7%  | 80.6%  | 46.8%  | 76.8%  | 1.79$\times$  | 29.4%
L275: Variant Aggregation  | CogACT  | 89.6%  | 80.8%  | 28.3%  | 46.6%  | 61.3%  | 1.00$\times$  | 100.0%
L276: VLA-Cache  | 91.7%  | 79.3%  | 32.5%  | 45.8%  | 62.3%  | 1.37$\times$  | 82.6%
L277: EfficientVLA  | 94.8%  | 77.6%  | 28.4%  | 51.9%  | 63.2%  | 1.57$\times$  | 45.1%
L278: FastV  | 91.4%  | 78.6%  | 27.6%  | 50.6%  | 62.1%  | 1.19$\times$  | 42.0%

