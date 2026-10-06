# Exact-v1 necessary evaluation — 2601.19634

## jan29_three196_evaluation

AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation (https://arxiv.org/html/2601.19634v1)
citeturn28508view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19634v1","lineno":200}); Total lines: 400
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


## jan29_three196_settings

AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation (https://arxiv.org/html/2601.19634v1)
citeturn28511view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19634v1","lineno":253}); Total lines: 400
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
L279: MoLe-VLA  | 89.2%  | 79.5%  | 29.9%  | 46.2%  | 61.2%  | 1.49$\times$  | 46.3%
L280: AC^{2}-VLA  | 88.7%  | 84.4%  | 28.2%  | 45.1%  | 61.6%  | 1.67$\times$  | 34.7%
L281: Table 3: Comparison with efficiency-oriented VLA methods on SIMPLER across two settings.
L282: Baselines. We compare AC^{2}-VLA with two groups of baselines: generalist dense VLA policies and efficiency-oriented methods.
L283: 
L284: Generalist VLA Models: We report results for RT-1 [cite35†4 ], RT-2-X [cite26†3 ], Octo [cite49†14 ], OpenVLA [cite27†8 ], and our backbone CogACT [cite28†9 ] in full precision, which serve as dense upper bounds on task success.
L285: Efficiency-Oriented Methods: We include representative acceleration approaches, including VLA-Cache [cite33†20 ] for temporal reuse, EfficientVLA [cite29†21 ] for static pruning, MoLe-VLA [cite32†22 ] for conditional layer skipping via mixture-of-layers routing, and FastV [cite50†5 ] as a lightweight pruning baseline. These comparisons characterize the trade-off between compute efficiency, measured by FLOPs and latency, and manipulation success across diverse tasks.
L286: ### 4.2 Comparison with State-of-the-Art
L287: 
L288: We compare AC^{2}-VLA on SIMPLER, reporting task success in Tables cite51†1 and cite52†2 and the speed–accuracy trade-off in Table cite53†3 .
L289: Task Performance. AC^{2}-VLA achieves strong control performance across evaluation protocols. On Google Robot Visual Matching, it reaches 76.8% average success, outperforming the dense CogACT baseline at 74.8% and larger models such as RT-2-X at 46.3%. Gains are most pronounced on precision-critical tasks, e.g., Drawer Opening improves from 71.8% to 80.6%, suggesting that action-prior-guided sparsification helps suppress distractors and stabilizes decision making.
L290: On Variant Aggregation, AC^{2}-VLA matches the full-precision baseline with 61.6% versus 61.3%, while consistently surpassing RT-1 and OpenVLA.
L291: Efficiency and Computational Cost. AC^{2}-VLA substantially reduces the inference cost of CogACT. As shown in Table cite53†3 , it uses 29.4% of the original FLOPs, yielding a 1.79$\times$ wall-clock speedup. Notably, this acceleration does not compromise performance and even improves success over dense CogACT, indicating that the removed computation largely corresponds to redundant or distracting features for closed-loop control.
L292: 
L293: Figure 3: Adaptive layer execution and cache reuse over time.
L294: cite54†Image: Refer to caption L295: 
L296: cite55†Image: Refer to caption L297: 
L298: Figure 4: Left: input observation. Right: visualization of token-level importance predicted by the action-conditioned router, highlighting regions relevant to the current manipulation stage while suppressing distractors. The highlighted regions adapt with the action context, focusing computation on interaction-critical areas. Figure 5: Pareto frontier for token pruning and layer skipping on the SIMPLER benchmark.
L299: ### 4.3 Ablation Study
L300: We ablate AC^{2}-VLA on SIMPLER Google Robot Visual Matching to validate key design choices. We focus on the three efficiency axes controlled by the router, namely token pruning, layer skipping, and cognition reuse, and analyze their interaction under comparable budgets. Ablation results are summarized in Table cite56†4 . We observe that each component provides complementary benefits, and the full model achieves the best speed-accuracy trade-off when all three axes are jointly enabled:
L301: 
L302:   * •


## jan29_three196_counter

AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation (https://arxiv.org/html/2601.19634v1)
citeturn28512view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19634v1","lineno":301}); Total lines: 400
L286: ### 4.2 Comparison with State-of-the-Art
L287: 
L288: We compare AC^{2}-VLA on SIMPLER, reporting task success in Tables cite51†1 and cite52†2 and the speed–accuracy trade-off in Table cite53†3 .
L289: Task Performance. AC^{2}-VLA achieves strong control performance across evaluation protocols. On Google Robot Visual Matching, it reaches 76.8% average success, outperforming the dense CogACT baseline at 74.8% and larger models such as RT-2-X at 46.3%. Gains are most pronounced on precision-critical tasks, e.g., Drawer Opening improves from 71.8% to 80.6%, suggesting that action-prior-guided sparsification helps suppress distractors and stabilizes decision making.
L290: On Variant Aggregation, AC^{2}-VLA matches the full-precision baseline with 61.6% versus 61.3%, while consistently surpassing RT-1 and OpenVLA.
L291: Efficiency and Computational Cost. AC^{2}-VLA substantially reduces the inference cost of CogACT. As shown in Table cite53†3 , it uses 29.4% of the original FLOPs, yielding a 1.79$\times$ wall-clock speedup. Notably, this acceleration does not compromise performance and even improves success over dense CogACT, indicating that the removed computation largely corresponds to redundant or distracting features for closed-loop control.
L292: 
L293: Figure 3: Adaptive layer execution and cache reuse over time.
L294: cite54†Image: Refer to caption L295: 
L296: cite55†Image: Refer to caption L297: 
L298: Figure 4: Left: input observation. Right: visualization of token-level importance predicted by the action-conditioned router, highlighting regions relevant to the current manipulation stage while suppressing distractors. The highlighted regions adapt with the action context, focusing computation on interaction-critical areas. Figure 5: Pareto frontier for token pruning and layer skipping on the SIMPLER benchmark.
L299: ### 4.3 Ablation Study
L300: We ablate AC^{2}-VLA on SIMPLER Google Robot Visual Matching to validate key design choices. We focus on the three efficiency axes controlled by the router, namely token pruning, layer skipping, and cognition reuse, and analyze their interaction under comparable budgets. Ablation results are summarized in Table cite56†4 . We observe that each component provides complementary benefits, and the full model achieves the best speed-accuracy trade-off when all three axes are jointly enabled:
L301: 
L302:   * •
L303: Cache reuse. Without cognition reuse, success drops to 70.5% and speedup decreases to 1.66$\times$, suggesting that temporal reuse improves both efficiency and closed-loop stability. Fig. cite57†3 illustrates adaptive layer execution and cache hit behavior over time.
L304: 
L305:   * •
L306: 
L307: Token pruning. Removing token pruning reduces speedup to 1.52$\times$, showing that spatial sparsification contributes most to acceleration. Fig. cite58†4 visualizes the token-level routing patterns.
L308: 
L309:   * •
L310: Layer routing. Disabling layer routing drops the success rate to 67.4% under similar FLOPs, indicating that conditional depth execution helps retain high-level reasoning while reducing compute.
L311: 
L312:   * •
L313: 
L314: Full model. AC^{2}-VLA attains 76.8% success while delivering a 1.79$\times$ speedup, demonstrating the effectiveness of jointly leveraging spatial, depth-wise, and temporal redundancies.
L315: ### 4.4 More Exploration
L316: 
L317: Beyond component ablations, we further analyze the hyperparameter space and emergent behaviors of AC^{2}-VLA, focusing on the joint sparsity trade-off and the effect of cognition caching on closed-loop stability.
L318: Token-layer sparsity and the efficiency-accuracy trade-off. We perform a grid search over the token keep ratio $r_{topk}$ and the executed layer count $N_{lay}$, as shown in Fig. cite59†5 . The results exhibit a clear Pareto frontier, where $r_{topk}=0.4$ and $N_{lay}=28$ achieves the best trade-off, reaching 1.79$\times$ speedup with 76.8% success. This suggests that many visual tokens are dispensable, while sufficient depth remains important for reasoning over the retained tokens.
L319: When cache reuse improves robustness beyond speed. Interestingly, cache reuse can improve robustness in addition to reducing compute. As shown in Table cite60†5 , setting the cache threshold to $\tau_{cache}=0.2$ yields 87.1% success, outperforming the dense baseline by +12.3%.
L320: We attribute this gain to improved temporal consistency: standard per-frame inference can amplify high-frequency visual noise and induce action jitter, whereas reusing $\mathbf{z}_{t}$ when the action context is stable effectively smooths decision making and stabilizes control.
L321: Sensitivity to key hyper-parameters. We next vary the token keep ratio and the maximum executed depth to examine how accuracy degrades under more aggressive sparsification.
L322: 
L323:   * •
L324: 
L325: Token sparsity. Performance remains stable down to $r_{topk}=0.4$, but collapses at $r_{topk}=0.2$ with 33.3% success, indicating a minimum visual information requirement for manipulation.
L326: 
L327:   * •
L328: Depth. The policy remains competitive with $N_{lay}=28$ at 77.3% success, while reducing below 24 layers causes a sharp drop, suggesting that sufficient depth is critical for complex tasks.
L329: Configuration  | Success Rate ($\uparrow$)  | Speed-up ($\uparrow$)  | FLOPs ($\downarrow$)
L330: Dense baseline  | 74.8%  | 1.00$\times$  | 100.0%
L331: Full AC^{2}-VLA  | 76.8%  | 1.79$\times$  | 29.4%
L332: No cache reuse, $\tau_{cache}=1.0$  | 70.5%  | 1.66$\times$  | 38.6%
L333: Without layer routing  | 67.4%  | 1.68$\times$  | 29.4%
L334: Without token pruning  | 72.7%  | 1.52$\times$  | 66.8%
L335: 
L336: Table 4: Component ablation on SIMPLER Google Robot Visual Matching. Speed-up is measured relative to the dense baseline.
L337: Sweep  | Value  | Success Rate ($\uparrow$)  | Speed-up ($\uparrow$)  | FLOPs ($\downarrow$)
L338: Token keep ratio $r_{topk}$  | 0.2  | 33.3%  | 1.69$\times$  | 25.8%
L339: 0.3  | 56.1%  | 1.66$\times$  | 34.7%
L340: 0.4  | 68.9%  | 1.63$\times$  | 44.1%
L341: 0.6  | 78.8%  | 1.47$\times$  | 62.5%
L342: 0.8  | 81.1%  | 1.26$\times$  | 81.0%
L343: Kept layers $N_{lay}$  | 22  | 69.7%  | 1.51$\times$  | 68.8%
L344: 24  | 73.5%  | 1.46$\times$  | 75.0%
L345: 26  | 78.0%  | 1.41$\times$  | 81.2%
L346: 28  | 77.3%  | 1.37$\times$  | 87.5%
L347: 30  | 80.3%  | 1.33$\times$  | 93.8%
L348: Cache threshold $\tau_{cache}$  | 0.00  | 82.6%  | 1.53$\times$  | 64.8%
L349: 0.05  | 81.1%  | 1.52$\times$  | 65.8%
L350: 0.10  | 77.3%  | 1.54$\times$  | 63.4%
L351: 0.20  | 87.1%  | 1.53$\times$  | 63.4%
L352: 0.30  | 78.8%  | 1.51$\times$  | 66.3%
L353: 0.40  | 79.5%  | 1.52$\times$  | 64.9%
L354: Table 5: Sensitivity sweeps on SIMPLER Google Robot Visual Matching, varying one efficiency component at a time with the other two disabled.


## jan29_three196_cost

AC2-VLA: Action-Context-Aware Adaptive Computation in Vision-Language-Action Models for Efficient Robotic Manipulation (https://arxiv.org/html/2601.19634v1)
citeturn28513view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19634v1","lineno":355}); Total lines: 400
L321: Sensitivity to key hyper-parameters. We next vary the token keep ratio and the maximum executed depth to examine how accuracy degrades under more aggressive sparsification.
L322: 
L323:   * •
L324: 
L325: Token sparsity. Performance remains stable down to $r_{topk}=0.4$, but collapses at $r_{topk}=0.2$ with 33.3% success, indicating a minimum visual information requirement for manipulation.
L326: 
L327:   * •
L328: Depth. The policy remains competitive with $N_{lay}=28$ at 77.3% success, while reducing below 24 layers causes a sharp drop, suggesting that sufficient depth is critical for complex tasks.
L329: Configuration  | Success Rate ($\uparrow$)  | Speed-up ($\uparrow$)  | FLOPs ($\downarrow$)
L330: Dense baseline  | 74.8%  | 1.00$\times$  | 100.0%
L331: Full AC^{2}-VLA  | 76.8%  | 1.79$\times$  | 29.4%
L332: No cache reuse, $\tau_{cache}=1.0$  | 70.5%  | 1.66$\times$  | 38.6%
L333: Without layer routing  | 67.4%  | 1.68$\times$  | 29.4%
L334: Without token pruning  | 72.7%  | 1.52$\times$  | 66.8%
L335: 
L336: Table 4: Component ablation on SIMPLER Google Robot Visual Matching. Speed-up is measured relative to the dense baseline.
L337: Sweep  | Value  | Success Rate ($\uparrow$)  | Speed-up ($\uparrow$)  | FLOPs ($\downarrow$)
L338: Token keep ratio $r_{topk}$  | 0.2  | 33.3%  | 1.69$\times$  | 25.8%
L339: 0.3  | 56.1%  | 1.66$\times$  | 34.7%
L340: 0.4  | 68.9%  | 1.63$\times$  | 44.1%
L341: 0.6  | 78.8%  | 1.47$\times$  | 62.5%
L342: 0.8  | 81.1%  | 1.26$\times$  | 81.0%
L343: Kept layers $N_{lay}$  | 22  | 69.7%  | 1.51$\times$  | 68.8%
L344: 24  | 73.5%  | 1.46$\times$  | 75.0%
L345: 26  | 78.0%  | 1.41$\times$  | 81.2%
L346: 28  | 77.3%  | 1.37$\times$  | 87.5%
L347: 30  | 80.3%  | 1.33$\times$  | 93.8%
L348: Cache threshold $\tau_{cache}$  | 0.00  | 82.6%  | 1.53$\times$  | 64.8%
L349: 0.05  | 81.1%  | 1.52$\times$  | 65.8%
L350: 0.10  | 77.3%  | 1.54$\times$  | 63.4%
L351: 0.20  | 87.1%  | 1.53$\times$  | 63.4%
L352: 0.30  | 78.8%  | 1.51$\times$  | 66.3%
L353: 0.40  | 79.5%  | 1.52$\times$  | 64.9%
L354: Table 5: Sensitivity sweeps on SIMPLER Google Robot Visual Matching, varying one efficiency component at a time with the other two disabled.
L355: ## 5 Conclusion
L356: We present AC^{2}-VLA, an action-context-aware framework for efficient Vision-Language-Action inference. By introducing a unified router that allocates computation across spatial, depth, and temporal dimensions based on the robot’s manipulation state, AC^{2}-VLA addresses the limitations of efficiency methods driven solely by visual complexity and enables adaptive closed-loop control.
L357: Experiments on the SIMPLER benchmark demonstrate a superior efficiency–accuracy trade-off, achieving a 1.79$\times$ speedup and reducing FLOPs to 29.4% of the dense baseline while improving task success. These results indicate that action-guided sparsification acts as both an efficiency mechanism and a regularizer, suppressing visual distractors and promoting temporal consistency.
L358: Overall, AC^{2}-VLA suggests that aligning computation with action is a more effective paradigm for embodied intelligence than static compression, and points toward adaptive inference as a key ingredient for scalable generalist robot policies.
L359: ## References
L360:   * [1] K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. R. Equi, C. Finn, N. Fusai, M. Y. Galliker, D. Ghosh, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, L. Ke, D. LeBlanc, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, A. Z. Ren, L. X. Shi, L. Smith, J. T. Springenberg, K. Stachowicz, J. Tanner, Q. Vuong, H. Walke, A. Walling, H. Wang, L. Yu, and U. Zhilinsky (2025) $\pi_{0.5}$: a vision-language-action model with open-world generalization.
L361: In Proceedings of The 9th Conference on Robot Learning, J. Lim, S. Song, and H. Park (Eds.), Proceedings of Machine Learning Research, Vol. 305, pp. 17–40. External Links: cite61†Link†proceedings.mlr.press Cited by: cite62†§2.1 .
L362:   * [2] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, L. Ke, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, L. X. Shi, J. Tanner, Q. Vuong, A. Walling, H. Wang, and U. Zhilinsky (2024) $\pi_{0}$: a vision-language-action flow model for general robot control. arXiv preprint arXiv:2410.24164. External Links: cite63†Document†dx.doi.org , cite64†Link Cited by: cite62†§2.1 .
L363:   * [3] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess, A. Dubey, C. Finn, P. Florence, C. Fu, M. Gonzalez Arenas, K. Gopalakrishnan, K. Han, K. Hausman, A. Herzog, J. Hsu, B. Ichter, A. Irpan, N. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, I. Leal, L. Lee, T. E. Lee, S. Levine, Y. Lu, H. Michalewski, I. Mordatch, K. Pertsch, K. Rao, K. Reymann, M. Ryoo, G. Salazar, P. Sanketi, P. Sermanet, J. Singh, A. Singh, R. Soricut, H. Tran, V. Vanhoucke, Q. Vuong, A.
L364: Wahid, S. Welker, P. Wohlhart, J. Wu, F. Xia, T. Xiao, P. Xu, S. Xu, T. Yu, and B. Zitkovich (2023) RT-2: vision-language-action models transfer web knowledge to robotic control. arXiv preprint arXiv:2307.15818. External Links: cite65†Document†dx.doi.org , cite66†Link Cited by: cite67†§1 , cite62†§2.1 , cite68†§4.1 .
L365:   * [4] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, T. Jackson, S. Jesmonth, N. J. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, I. Leal, K. Lee, S. Levine, Y. Lu, U. Malla, D. Manjunath, I. Mordatch, O. Nachum, C. Parada, J. Peralta, E. Perez, K. Pertsch, J. Quiambao, K. Rao, M. Ryoo, G. Salazar, P. Sanketi, K. Sayed, J. Singh, S. Sontakke, A. Stone, C. Tan, H. Tran, V. Vanhoucke, S. Vega, Q. Vuong, F.

