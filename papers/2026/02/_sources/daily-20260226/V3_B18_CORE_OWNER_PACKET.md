# B18 — 八项必要原证 / actual owner；本次独核及actual POST安全终态

2026-10-06 feb26_close_oct06非原packet作者逐项定点读取上述必要原段，所引pID从各exact-v1 raw重新定位，无缺失；21185原CORE Eq11/12与A1.2、21189 Eq2和原TeX weighted-agreement/反侧单独核。实际Ch49 recurrent/layout与collective、Ch26 subgoal/action、Ch31 exploration proxy/step effect、Ch33去std估计器、Ch76 query proposal、Ch23 spatial primitive state分别核：21144/21157/21158/21172/21175具体已有覆盖，21186受限feature-prediction recipe仅报告。21185与21189真实差额root授窄锁后已写Ch24/Ch31，actual正文/完整邻接/自身末注root非写入者POST通过，已同步安全终态。原方法/费用/分母/反侧及ND保留；未运行artifact/复现，非日级验收。

## 2602.21144v1
https://arxiv.org/html/2602.21144v1

S4.SS1.p3.1 | However, what to store in the SSM cache is not a trivial question under TP. The reusable context in SSMs is not a Transformer KV cache; instead it consists of (a) the compact per-layer SSM state produced after processing the prompt, and (b) a short convolution history used by the causal depthwise convolution. Our SSM cache stores exactly these objects, and under TP it is sharded by channels (hidden-feature dimensions) so that each GPU stores only the cache entries for the channels it owns. This ensures cache reads/writes stay GPU-local and prevents the cache itself from adding extra inter-GPU synchronization during decoding to reconstruct the context.

S4.SS3.p3.1 | This packing is convenient on a single GPU, but it is not TP-friendly because the packed tensor implicitly assumes a fixed contiguous layout, whereas TP needs a partitioning that depends on the chosen TP degree. If we TP-shard the packed SSM_parameters tensor naively, each rank can receive partial slices of multiple logical fields, forcing either time-consuming reassembly collectives or extra layout transforms before invoking the fused kernel.

S4.SS3.p4.1 | To avoid this, we explicitly unpack the logical fields required by the fused SSM kernel and apply a TP-aware placement that keeps the state update GPU-local. Specifically, we shard \Delta with channels (it is token-dependent, the largest stream, and dominates activation-side memory), while ensuring that all remaining quantities required to advance the SSM state for the owned channels are locally available on every rank when the fused kernel runs. In our implementation, this means token-dependent terms such as B and C are produced locally from the local activations, while per-channel learned parameters such as A and D are replicated (or stored) locally as needed. This layout allows each rank to execute the SSM update using the same fused kernel on contiguous local shards without any communication inside the SSM path, and it eliminates an otherwise required collective that would be needed to reconstruct packed parameter slices prior to the SSM operation.

S5.SS3.SSS3.p7.1 | In summary, while TP increases throughput by enabling larger feasible batch sizes (via parameter/activation sharding) and by distributing the per-token compute across GPUs, its marginal benefit tapers as runs approach fundamental compute/memory limits and as fixed collective overheads become a larger fraction of each step. This behavior is consistent with classic strong-scaling limits: as the non-parallelizable and synchronization components grow in relative cost, speedups saturate (and can even regress) despite adding more parallel resources [24, 25]. This interpretation is consistent with the slight plateauing in Figures 5 and 4 at larger output lengths.

S5.SS4.p2.1 | We first quantify the accuracy impact by comparing model outputs against the non-quantized model using agreement-based metrics (Top-1 token match and Top-k overlap). Note that the GPU choice (A6000 or A100) does not impact the model accuracy. Table I shows that our quantized AllReduce incurs only small output perturbations: the next-token prediction under quantization matches the non-quantized version \sim 98% of the time and the Top-5 candidate set overlaps \sim 99% of the time, suggesting that quantization rarely changes the model’s preferred token and typically only perturbs the ranking among close-probability alternatives (reflected in the stricter Top-5 exact ordering match of 87–89% across models). These results align with the established view that low-precision communication is a favorable tradeoff when communication becomes a bottleneck [18, 19, 20].

## 2602.21157v1
https://arxiv.org/html/2602.21157v1

S3.SS2.p2.1 | The switching mechanism between modalities is explicitly controlled via special tokens. By default, the model operates as an auto-regressive planner; however, the generation of specific tokens (e.g., \langle\text{visual\_start}\rangle or \langle\text{action\_start}\rangle ) triggers the routing of hidden states to the visual generation expert or the action prediction expert, respectively. In order to manage the information flow among experts, we implement a carefully structured masking strategy within the shared self-attention. As illustrated in Figure 4, a causal mask is applied to textual tokens to enforce autoregressive generation. Conversely, visual tokens employ bidirectional attention within each frame to capture global spatial dependencies, while maintaining causal masking for interactions across frames or modalities. Crucially, to prevent information leakage, noise tokens are restricted from attending to their corresponding ground-truth targets. Furthermore, all other tokens are masked from attending to noise tokens, ensuring they only aggregate information from valid non-noise contexts.

S3.SS3.p1.1 | To support the generation of intermediate textual reasoning trace \mathbf{r} and visual subgoal \hat{\mathbf{o}}_{t+h} , we construct an automatic pipeline to synthesize EM-CoT data from raw robot trajectories at scale. As shown in Figure 2, the pipeline operates in three phases. Firstly, we translate continuous low-level actions into high-level motion primitives via rule-based matching following Belkhale et al. (2024). Secondly, we utilize a large-scale Vision-Language Model (Qwen3-VL (Bai et al., 2025)) to augment the trajectory with dense textual reasoning, including task narratives and subtask decomposition. Finally, the terminal frame of each subtask is designated as its corresponding visual subgoal, providing a sparse supervision signal that effectively lowers the learning difficulty. This process yields a high-quality dataset \mathcal{D}_{\text{ft}} where every trajectory is augmented with aligned textual reasoning \mathbf{r} and visual goals \hat{\mathbf{o}} , enabling the supervision of the intermediate steps defined in Eq. (1)-(2). See Appendix B for more details on this pipeline, including the pseudo code and tailored prompt used in each phase.

S4.SS3.p2.1 | Effectiveness of the versatile pre-training. As depicted in Panel A, the full versatile pre-training utilizing all three diverse datasets demonstrates unparalleled effectiveness, consistently achieving the highest performance metrics. Conversely, even the selective removal of a single data modality, such as visual generation data (w/o V), leads to a significant degradation in performance, particularly on hard tasks (over 50% reduction). Further progressive exclusion of textual (w/o V+T) and action prediction data (w/o V+T+A) results in a continuously worsening performance trajectory. Notably, without any pre-training (w/o V+T+A), the model’s performance falls to a complete 0% on hard tasks, demonstrating that pre-training is an absolutely foundational requirement for establishing the core competencies necessary to tackle complex problems. Collectively, these findings underscore the indispensable and complementary roles of the versatile pre-training step.

## 2602.21158v1
https://arxiv.org/html/2602.21158v1

S3.SS2.SSS0.Px2.p1.1 | To capture overall uncertainty across a trajectory \tau , we adopt an exponentially discounted aggregation, assigning greater weight to later steps, which often determine final success: U(\tau)=\frac{\sum_{t=1}^{T}\lambda^{T-t}u^{\text{step}}_{t}}{\sum_{t=1}^{T}\lambda^{T-t}},

S3.SS3.SSS0.Px1.p1.2 | where w_{t} is a step-dependent weight and \hat{u}^{\text{step}}_{t} denotes the normalized step uncertainty. In our settings, w_{t} is set to 0.95 to keep failure rewards informative but always smaller than the success rewards.

S4.SS3.SSS0.Px2.p1.1 | We also explore different ways of incorporating uncertainty into the reward function, as summarized in Table 3. The Negative variant replaces rewards in failure cases with negative values, aiming to penalize uncertain or ineffective actions. The Exponential variant, on the other hand, attenuates rewards for successful trajectories according to their uncertainty level, encouraging the model to be more confident when success is achieved. Formally, the exponential formulation is defined as:

原reward公式 L658–660:
\tilde{r}_{t}^{\text{step}}=\begin{cases}\mathbf{1}[\text{fail}]\cdot w_{t}\,\hat{u}^{\text{step}}_{t},&\text{if fail},\\
r_{t},&\text{otherwise},\end{cases}
(1)

原reward公式 L695–697:
\tilde{r}^{\text{traj}}=\begin{cases}U(\tau),&\text{if fail},\\
r,&\text{otherwise}.\end{cases}
(2)

## 2602.21172v1
https://arxiv.org/html/2602.21172v1

S4.SS2.p1.2 | Here, r(o_{i}\mid x) is the reward for sample i given input x , G is the group size, and \mathrm{std} denotes the standard deviation across the group. Recent studies have shown that this formulation unintentionally favors groups with low reward variance [29]. When the standard deviation of the reward within the group is small (i.e., NoRD-base, being a weak SFT model, produces groups with high intra-group variance during the GRPO rollout for the majority of samples ( Fig. 2). Dr. GRPO mitigates difficulty bias by removing the standard deviation term from the group relative advantage, enabling more effective optimization of weak policies. Notably, while other variants like VD-GRPO [39] preserve absolute reward magnitudes to balance objective priorities (e.g., safety vs. comfort), Dr. GRPO ensures that ’hard’ scenarios contribute a sufficient gradient signal. Additionally, we employ DAPO-style asymmetric clipping to prevent entropy collapse during RL training and follow Liu et al. [29] by not using KL-divergence regularization. The resulting Dr. GRPO post-training objective is given by:

S7.p1.1 | We present a component-wise breakdown of Tab. 1 in Tab. 4. Except for Ego Progress, Dr. GRPO significantly outperforms GRPO. As shown in the training and validation curves in Fig. 11, both GRPO and Dr. GRPO improve over time; however, GRPO consistently lags behind Dr. GRPO. To further illustrate this, we visualize the change in mean PDM scores of the group, relative to the SFT model (step 0), across different variance groups in Fig. 10. The variance groups are defined based on intra-group tertiles. Our analysis reveals that:

## 2602.21175v1
https://arxiv.org/html/2602.21175v1

S2.SS2.p2.1 | To achieve this, we implement h using a generative large language model ( \mathtt{LLM} ). However, simply training the \mathtt{LLM} on image descriptions is insufficient, since it cannot guarantee that retrieval results satisfy user expectations of quality. Instead, we partition the textual descriptions into non-overlapped quality levels \mathcal{C} that reflect different image quality categories. We then finetune the \mathtt{LLM} with these quality levels, enabling it to generate query completions conditioned on quality preferences. This yields the formulation of our quality-controllable retrieval (QCR) :

S4.SS4.p1.1 | To achieve quality control in retrieval, the model should be tailored to the specific dataset, as different datasets exhibit varying quality characteristics. To illustrate this, we conduct cross-dataset retrieval experiments. Specifically, we evaluate retrieval quality on MS-COCO using queries completed by the model finetuned on Flickr2.4M. In Table 4, we assess FT-CoCa and FT-Blip2, which are finetuned on descriptions generated by CoCa and Blip2, respectively. The results indicate that both models achieve higher aesthetic scores as quality conditions improve, suggesting that aesthetically relevant semantic cues may be universal across natural images. Nevertheless, they consistently exhibit low relevance across all quality conditions. This limitation stems from the dataset mismatch between the query completion and image retrieval stages, since the two datasets encode different semantic information. See Appendix A.3 for additional analysis and results.

## 2602.21185v1
https://arxiv.org/html/2602.21185v1

S3.p1.2 | where \kappa_{t}\in[0,1] and \Psi_{1}(.|{\mathbf{x}}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}})=\text{Cat}(.|{\mathbf{\bm{\pi}}}) , with \bm{\pi}={\mathbf{m}} for MDMs and \bm{\pi}={\bm{1}}/K for USDMs. (11) is thus a linear combination of the forward process (1) and the reverse posteriors (2, 3) of standard discrete diffusion models. We therefore refer to these as superposition posteriors, or simply \Psi -posteriors.

S5.SS2.SSS0.Px3.p1.1 | In Table 1, we compare the multiple-choice question (MCQ) accuracy of Duo, \text{Duo}^{++} , MDLM (Sahoo et al., 2024), and an autoregressive transformer (1M training steps with a batch size of 512 on OWT, same hyperparameters as MDLM) using the lm-eval-harness suite (Gao et al., 2024) ; details in Suppl. C.3). We find that \text{Duo}^{++} achieves an accuracy similar to that of Duo, despite requiring 25% less training GPU-hours. However, it trails MDLM on most tasks, consistent with its higher perplexity.

A1.SS2.SSS0.Px3.p1.2 | Specifically, (1) hold by (16), (2) by the induction hypothesis, (3) by definition of the \Psi -posteriors, (4) by distributing {\color[rgb]{0.043,0.3242,0.5898}q_{t}}(\tilde{{\mathbf{z}}}_{t}^{\color[rgb]{0.4688,0.4688,0.4688}\ell}|{\mathbf{x}}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}}) , (5) by definition of marginal probability (first term), and by observing that \sum_{\tilde{{\mathbf{z}}}_{t}^{\color[rgb]{0.4688,0.4688,0.4688}\ell}}{\color[rgb]{0.043,0.3242,0.5898}q_{t}}(\tilde{{\mathbf{z}}}_{t}^{\color[rgb]{0.4688,0.4688,0.4688}\ell}|{\mathbf{x}}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}})=1 since {\color[rgb]{0.043,0.3242,0.5898}q_{t}} is normalized. This concludes the inductive step, and shows that the \Psi -posteriors have the correct marginal.

原Eq11/12 L2317:
\displaystyle\Psi_{s|t}(.|{\mathbf{x}}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}},{\mathbf{z}}_{t}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}})=\kappa_{t}{{q_{s|t}}}(.|{\mathbf{z}}_{t}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}},{\mathbf{x}}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}})+(1-\kappa_{t}){\color[rgb]{0.043,0.3242,0.5898}q_{s}}(.|{\mathbf{x}}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}});\;\forall\ell\in[L]

原Eq11/12 L2664:
\displaystyle[\Psi^{\theta}_{s|t}(.|{\mathbf{z}}_{t})]^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}}=\kappa_{t}{\color[rgb]{0.043,0.3242,0.5898}{q_{s|t}}}(.|{\mathbf{z}}_{t}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}},\mathbf{x}_{\theta}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}}({\mathbf{z}}_{t},t))+(1-\kappa_{t})\left[\alpha_{s}{\color[rgb]{0.043,0.3242,0.5898}q_{0|t}}(.|{\mathbf{z}}_{t}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}},\mathbf{x}_{\theta}^{{\color[rgb]{0.4688,0.4688,0.4688}\ell}}({\mathbf{z}}_{t},t))+(1-\alpha_{s})\bm{\pi}\right].

## 2602.21186v1
https://arxiv.org/html/2602.21186v1

S3.SS2.SSS0.Px1.p1.1 | A critical prerequisite for PSFM is the construction of a canonical spatial feature field f where context features \boldsymbol{F}_{c} and target features \boldsymbol{F}_{t} are spatially aligned. To achieve this, we introduce an Asymmetric View Aggregator, which effectively adapts the pre-trained VGGT [34] to extract spatially-aligned features using its powerful global attention mechanism. We employ an asymmetric attention masking strategy in the global attention layers of VGGT to strictly prevent information leakage from target views to context views. Given a batch of context views C and target views T , we construct a view mask \boldsymbol{M}\in\{0,-\infty\}^{L\times L} applied to the attention logits, where L denotes the total sequence length. Specifically, target views are allowed to attend to all views ( C\cup T ), whereas context views are restricted to attending only to other context views. Formally, for a query patch from view i and a key patch from view j :

S3.SS2.SSS0.Px2.p1.1 | The Spa3R Encoder E_{\phi} is a Transformer designed to encapsulate the context features \boldsymbol{F}_{c} into a compact representation \boldsymbol{z}\in\mathbb{R}^{N_{q}\times D} . We initialize N_{q} learnable query embeddings \boldsymbol{q} . These queries are concatenated with the context features \boldsymbol{F}_{c} into a single sequence and processed through Transformer layers to iteratively refine the queries by aggregating information from the context, yielding the final spatial representation \boldsymbol{z} :

S3.SS2.SSS0.Px3.p1.1 | The Spa3R Decoder D_{\theta} synthesizes the target features \hat{\boldsymbol{F}}_{t} conditioned on the spatial latent \boldsymbol{z} and the target camera pose \boldsymbol{v}_{t} . This process involves two key geometric mechanisms: ray-based querying and relative 3D positional encoding. First, to encode the embeddings of the target view frustum, we generate camera-space ray directions \boldsymbol{d} for each homogeneous pixel coordinate \tilde{\boldsymbol{u}} using the estimated intrinsics \boldsymbol{K} :

S4.SS4.SSS0.Px5.p1.1 | We investigate the mechanism for conditioning the decoder on the target viewpoint. We compare the Plücker [27] coordinate embedding, an absolute pose encoding widely used in neural rendering, against the relative positional encoding provided by PRoPE [22]. As shown in Tab. 7, PRoPE outperforms Plücker coordinates by a notable margin of +1.0%. We attribute this performance gap to the inherent limitations of absolute pose encodings, which can be sensitive to variations in scene scale and coordinate origin shifts. In contrast, PRoPE injects the relative geometric transformation between context and target views directly into the attention weights, leading to more robust and geometrically consistent feature synthesis across diverse viewpoints.

## 2602.21189v1
https://arxiv.org/html/2602.21189v1

原CORE L816–816:
\nabla J_{k}(\theta)=\mathbb{E}_{x\sim\mathcal{D}}[w_{k}(p_{\theta}(x))\nabla p_{\theta}(x)]\,,w_{k}(p):=k(1-p)^{k-1},

原CORE L9491–9496:
\par\noindent{\ref{distrib-shift} Prompt distribution shift: pass@$k$ reweights prompts.}
Recalling that the weights $w_{k,\theta}(x)$ are nonnegative, define the reweighted prompt distribution:
\begin{equation*}\tilde{\mathcal{D}}_{k,\theta}(dx)\,\propto w_{k,\theta}(x)\mathcal{D}(dx)\,,\end{equation*}
inducing the expectation $\mathbb{E}_{\tilde{\mathcal{D}}_{k,\theta}}[f(x)]=\frac{\mathbb{E}_{\mathcal{D}}[w_{k,\theta}(x)f(x)]}{\mathbb{E}_{\mathcal{D}}[w_{k,\theta}(x)]}$ for any measurable function $f$ of the prompt random variable\penalty\ $x$. Note that the distribution $\tilde{\mathcal{D}}_{k,\theta}$ places higher mass on prompts with smaller success probability $p_{\theta}(x)$ (hard prompts) since $w_{k,\theta}(x)$ is decreasing in $p_{\theta}(x).$ Therefore, we can rewrite \eqref{eq:conflict-1} as follows:
\begin{equation}\langle\nabla J_{k}(\theta),\nabla J_{1}(\theta)\rangle=\mathbb{E}_{\mathcal{D}}[w_{k,\theta}(x)]\cdot\mathbb{E}_{\tilde{\mathcal{D}}_{k,\theta}}[a_{\theta}(x)]\,,\end{equation}
and since $\mathbb{E}_{\mathcal{D}}[w_{k,\theta}(x)]>0$ (as $w_{k,\theta}(x)\geq 0$ and not equal to zero a.e.), we obtain the following equivalence between $\langle\nabla J_{k}(\theta),\nabla J_{1}(\theta)\rangle<0$ and $\mathbb{E}_{\tilde{\mathcal{D}}_{k,\theta}}[a_{\theta}(x)]<0\,.$

原CORE L9527–9530:
\begin{corollary}Let Assumption\penalty\ \ref{as:E-LS} hold. Suppose that $q_{\theta}>0$ and let $k\geq 2.$ Then for any $\theta\in\mathbb{R}^{d},$
$\langle\nabla J_{k}(\theta),\nabla J_{1}(\theta)\rangle\leq-\delta(\theta)$ where $\delta(\theta):=mW_{-}(k,\theta)-G^{2}W_{+}(k,\theta)$. If in addition $\delta(\theta)<0$, then $\langle\nabla J_{k}(\theta),\nabla J_{1}(\theta)\rangle\leq-\delta(\theta)<0\,.$
\end{corollary}
\par\noindent{Discussion of assumption.} Note that the assumption $q_{\theta}>0$ is necessary for gradient conflict. Indeed, if instead we have for instance for almost every $x\in\mathcal{X},a_{\theta}(x)\geq 0$, then it follows from \eqref{eq:conflict-1} that $\langle\nabla J_{k}(\theta),\nabla J_{1}(\theta)\rangle\geq 0$ as the weights $w_{k,\theta}(x)$ are also always nonnegative. Negative agreement score is a necessary condition for gradient conflict.

原CORE L9552–9555:
We run experiments with two reasoning models: DeepSeek-R1-Distill-Llama-8B and DeepSeek-R1-Distill-Qwen-7B.
\par\noindent{Pass@$k$ gradient computation.} For computational efficiency, we compute pass@1 gradients with respect to policy parameters in the language model's final hidden layer (dimension $d=4096$ for Llama-8B, $d=3584$ for Qwen-7B). We compute pass@$k$ gradients using Monte Carlo estimates based on \eqref{eq:pass@k-grad} and pass@$k$ estimates developed in prior work \cite[citep]{(\@@bibref{AuthorsPhrase1Year}{walder-karkhanis25neurips,chen-et-al21eval-llms-code}{\@@citephrase{, }}{})}.
\par\noindent{Setup.} We create filtered data sets $\mathcal{D}_{\delta_{1},\delta_{2}}$ of prompts and responses with varying difficulty thresholds $(\delta_{1},\delta_{2})$ consisting of
(i) hard prompts ($p_{\theta}(x_{i})<\delta_{2}$) and (ii) easy prompts ($p_{\theta}(x_{i})>\delta_{1}$). We test 7 combinations with $\delta_{1}\in\{0.80,0.85,0.90\}$ and $\delta_{2}\in\{0.05,0.10,0.15\}$. For each combination, we compute estimates of the agreement scores\penalty\ $a_{\theta}(x)$ as defined in \eqref{eq:alignment-score}, pass@$k$ weights\penalty\ $w_{k,\theta}(x)$ (see \eqref{eq:pass@k-weights-formula}) and estimated average weighted agreement scores over prompts, which correspond to pass@$k$ and pass@1 gradient inner product as shown in Proposition\penalty\ \ref{prop:grad-conflict}.

原CORE L9710–9710:
&=J_{k}(\theta)+\eta\|\nabla J_{k}(\theta)\|^{2}-\frac{L_{k}\eta^{2}}{2}\|\nabla J_{k}(\theta)\|^{2}\\

原CORE L9713–9713:
\par\noindent{Sampling configuration.} For each problem, we generate $k=32$ independent responses using temperature sampling with temperature $T=0.7$ and nucleus sampling with $p=0.95$. Responses are evaluated using exact match against ground truth answers and binary rewards indicate correctness.

## actual owner — books/part-05-inference-system/49-tensorrt-llm.md

L392–402:
序列形式的算子在 Training/Prefill 阶段便于并行，Decode 若每个 token 都从片外重新装载完整历史或递归状态，瓶颈首先是 state traffic，而不是算术单元。状态可放入片上容量时，一个专用分支把 recurrent state 变成长寿命对象，并围绕单 token update dependency 组织 dataflow；每步只搬运新输入和必要输出：

```text
versioned recurrent state layout
→ keep authoritative state on chip
→ ingest one-token inputs
→ execute dependent update stages
→ atomically publish next state and output
```

Executor 拥有 state layout、lifetime 与 commit frontier，kernel 只推进一次合法更新。它减少片外带宽，却受片上容量、固定布局与 operator coverage 限制；短序列、状态过大或模型经常变化时，通用外存路径仍更灵活。`arXiv:2603.05931v1` 只在 §IV-E System Overview、§VI-E Ablation Analysis 与 §VIII Conclusion 所披露的 FPGA、算子和精度上支持这条边界，不证明 GPU 或其他线性 Attention 有相同比例收益。<!-- source-family:SF-2026-ARXIV-2603-05931 -->

L234–236:
MoE 的 collective layout 还与 attention 的 TP/DP、expert 的 TP/EP 和 pipeline 切分共同决定可用 overlap。固定并行组与库 All-to-All 在拓扑稳定时最容易验证；跨节点带宽弱于节点内互连时，可以按隐维度重排 dispatch 为节点间分片移动后节点内 AllGather，将 combine 拆成异步节点间 All-to-All 与节点内 ReduceScatter、top-k 加权组合。这样暴露可独立等待的搬运/归约依赖，再由 joint planner 比较模型 shape、并行度、拓扑和 layer placement，而不是先分别选好 attention 与 expert 计划。[MixServe exact-v1 §III](https://arxiv.org/html/2601.08800v1) 提供这条分解；通信轮数阶数降低不是总工作或端到端延迟保证。

额外 temporary buffers、重排、节点内 gather/reduce 和真实 completion 依赖必须进入计划成本。相同 DP/EP 的“平衡”也不是硬件无关最优点：作者 §IV-C 的 Ascend910B 对照偏好 DP=EP，而 H20 对照偏好 DP<EP；sync/async 消融只支持其局部 overlap。不同 backend 的候选空间和执行路径不能拼成统一因果倍率，有限两/四节点负载也不授生产 SLO。Profile 陈旧、workspace 不足或没有可隐藏的通信时，回退固定库 collective/更保守并行映射；模型 expert routing 的语义仍由第21章拥有，本章仅解释其可执行布局与依赖。

## actual owner — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

L133–135:
单一生成器直接输出长轨迹，接口简单，却会把抽象目标、局部动力学与实时修正压在同一采样过程。层级分支可以让 high-level diffusion 提议 subgoal，把它投影为 versioned latent target，再由 low-level rectified-flow policy 生成短轨迹，最后交给 MPC、inverse dynamics 与 safety controller 验收。高层只拥有目标 proposal，低层只拥有 trajectory proposal，真实 action commit 仍在控制器。

分层获得更长 horizon 和局部重规划能力，也引入 subgoal projection error、RSSM/representation drift、两级延迟与接口失配。缺少成功/失败 demonstration、inverse dynamics 不可靠或 deadline 不允许两级生成时，应回退短 horizon reactive policy、传统 planner 或人工控制。exact-v1 证据限其 demonstration、RSSM、模拟及少量真实试验，不证明开放世界安全、任意 embodiment 迁移或端到端尾延迟。

## actual owner — books/part-04-training-system/31-rlhf.md

L414–416:
多数采样后投票在答案可离散比较时是低成本 baseline，但 pass@k 上升可能来自已有正确 mode 被更频繁抽中，而不是 policy 学到新能力。训练 owner 应把迁移结果拆成 `capability expansion`、`distribution sharpening` 与 `mode extinction`；当重复自训练开始消灭少数但有效的轨迹时，TTRL-style guard 可以冻结或降权高灭绝风险更新。收益是避免把表面成功率误读成能力增长，代价是额外 rollout、mode tracking 和 guard threshold；短任务、单一可验证答案或分布稳定时，普通 majority vote 仍成立。

<!-- source-family:SF-2026-ARXIV-2605-19444 -->

L955–957:
在线 preference learning 的 exploration 也不能只依赖当前 policy 的瞬时不确定性。历史样本覆盖、observer disagreement 与旧策略误差可以提供更稳定的 prior，再用当前观测修正 exploration budget。这样能把查询集中到高信息区域，但会引入历史分布滞后；发生 policy shift 时必须重置或降权旧不确定性，保留均匀探索作为覆盖 fallback。

tool-integrated trajectory 的 terminal reward 往往把多个动作混成一个结果。step-level credit 应绑定可观察 effect、状态变化与 verifier receipt，再决定哪些 turn 进入更新。没有外部 verifier 时，一条弱监督分支从某个 turn state 采样多条 future answers，按语义答案聚类，再把各 cluster 的 probability mass 与可靠性估计组成 outcome-potential distribution；相邻 turn 的 potential delta 只表示“后续答案分布是否向更可靠的 cluster 移动”，不是该动作的真实因果 credit。Cluster 边界、future-sampling budget 和 reliability estimator 都会改变信号，开放答案或同义归并不稳时，应回退 terminal outcome 或可执行 subgoal verifier。

## actual owner — books/part-04-training-system/33-grpo.md

L558–565:
Dr. GRPO 重新检查 estimator 本身：原 GRPO 的 group reward standard-deviation normalization 会按各 prompt
的组内 reward dispersion 反向缩放更新，而按实际 response length 归一化会引入长度相关权重。其做法是
去除这两项，并以固定 generation budget 作为 loss normalization，希望恢复更接近无偏 Monte Carlo 的
policy-gradient estimator。代价是原本由标准化吸收的 reward-scale 差异重新暴露给 batch composition 和
optimizer。它与 DAPO 的 token-level reduction 不是可以无条件叠加的两个“技巧”，而是在回答**一个 token、
一个 response 还是一个
固定采样预算应成为统计单位**。


## actual owner — books/part-07-agent/76-rag.md

L73–75:
Query-side 也有一个容易错位的选择：同一 information need 可以写成多个 query variant，但服务端往往只能按预算先选一个执行。离线检索分数更高的改写不必给出更有用的答案；因此选择器要冻结原问题、候选改写集合、目标 retriever/index 与后续 reader，在真实执行前用受限 query 特征提出 variant，再分别验收排名／召回和答案支持／效用。它只拥有查询表达的 proposal，不因预测分数高就替检索结果赋予事实权威，也不能把 oracle 最优改写当成线上可得输入。<!-- source-family:SF-2026-ARXIV-2604-22661 -->

这条分支可能省去并行执行全部改写，却增加 predictor、训练标签和错误选一的机会成本；若选择器本身比多路检索更贵，或答案需要互补证据，就应回退固定 query、受预算约束的多改写融合或直接取证。受控 TREC-RAG 2024 的 BM25／dense、top-5 reader 与 nugget 评价显示，nDCG-optimal 的 variant 与答案效用可错位，甚至不保证优于某些简单 pre-retrieval predictor；但它没有给出匹配完整生成成本的生产比较，也不证明某一种 QPP 策略普遍最优。Document-side 结构修复与 answer-side 证据核验仍由各自 owner 承担。

## actual owner — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

L422–427:

后一步没有否定保守 unmask。它用更多训练与推理 work、mutable state 和提交复杂度换取更激进的并行 operating point。

重写位置还可以承担临时工作空间，不只是修复错误。一个受限理论例子要求采样长度n的均匀even-parity bit序列，而不是给定输入计算parity：第一轮生成n-1个独立临时变量y，并固定末位y为0；第二轮把各位置改写为相邻y的XOR（首位与初始0异或）。临时变量由相邻输出共享，最终序列因此具有偶校验相关性；每轮given当前可见状态的位置预测仍条件独立，相关性不是一次独立填充凭空产生的。若一经揭示就永久冻结，同一位置便不能先保存这种中间符号、再成为最终输出。

[该构造及下界](https://arxiv.org/html/2512.25014v1)只比较L=n、没有额外CoT工作空间、predictor与揭示选择器都是固定深度/poly-size AC0 circuit的exact sampler：冻结路径不能常数轮采样该分布，允许revision的路径可两轮完成。这不是任意Transformer或近似分布的下界。一般circuit的空间复用构造又需O(log d)深度的每步控制，目标深度d增长时不能称作固定深度；迭代轮数、工作空间、每轮全序列计算与硬件墙钟必须分账。重写还增加状态版本、训练覆盖和对外commit成本；无法训练可靠的中间状态、需要尽早流式发布或预算不足时，保守unmask与AR仍合理，理论存在性不证明实际模型学会了构造或服务更快。<!-- source-family:SF-2026-ARXIV-2512-25014 -->

## actual owner — books/part-03-multimodal-world-models/23-multimodal-representation.md

L876–878:
先由独立 3D reconstruction pipeline 生成 mesh，再把结果作为多模态模型的只读输入，职责清楚且容易单独验证；当任务要求多轮理解、生成和局部编辑保持同一几何身份时，stateless sidecar 会丢失跨轮 mesh state。另一条分支把 3D primitives/mesh 表示纳入统一 token contract，并让 modality-specific experts 共享同一 identity 与 revision。

它提高跨任务连续性，却增加 tokenizer/mesh discretization、长 Context、几何一致性和编辑回滚成本。模型拥有 proposal，不拥有物理几何真值；identity 保持和生成 fidelity 也不能证明真实世界尺度或可执行性。单次重建、精确 CAD 或安全关键几何仍应由专用工具与确定性验证承担。
