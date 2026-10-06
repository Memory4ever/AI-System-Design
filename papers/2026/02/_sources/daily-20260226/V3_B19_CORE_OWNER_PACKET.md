# B19 — 八项必要原证 / actual owner；本次独立复核已落实

2026-10-06 feb26_close_oct06 非原packet作者从各exact-v1 raw重新定位全部所引pID，无缺失；20427原§3.2/4、20901原§3.3–3.4、21193原§3.1–3.2/4、21198原§3/4.3/A2、21202原§5/6对照及21204原S5.Ex1–15链另定点核。实际Ch49计划/独立合法性、Ch66难度/oracle/预算、Ch27terminal联合对象与失败混杂、Ch80参数状态生命周期、Ch76固定index预算、Ch22KVB形式条件/scan语义已核：20427/20901/21193/21198/21202/21204具体已有覆盖；21188双轴每步融合与直接qualitative反侧核实，有限人体recipe仅报告。21196已窄纠错并root actualPOST，评分按原2+2+3=7保持，不因纠错降分。原反侧/人口/费用/ND保留，未运行artifact/复现，非日级验收。

## 2602.20427v1
https://arxiv.org/html/2602.20427v1

S3.SS1.p5.1 | By adopting this parameterization, we reduce the number of parameters to be optimized from D\cdot|V| to 2|V| . For a graph with N operators, we only need to optimize two vectors: mean vector ( \boldsymbol{\mu}\in\mathbb{R}^{|V|} ) that determines the central temporal location of each operator, and standard deviation vector ( \boldsymbol{\sigma}\in{\mathbb{R}^{+}}^{|V|} ) that controls the degree of relaxation. During initial stage of optimization, \boldsymbol{\sigma} is typically large to encourage encourages exploration of the schedule space; as optimization processes, \boldsymbol{\sigma} usually converges to small values concentrating the probability mass and effectively hardening the schedule toward a deterministic discrete integer.

S3.SS3.p3.1 | Sampling. To sample a discrete schedule from the continuous representation, we round the mean ( \mu_{i} ) for each operator ( v_{i} ) to its nearest integer. While ALM minimizes expected violations, the resulting rounded schedule may still contain legal conflicts. To ensure the final output is valid, we apply a lightweight greedy algorithm to map illegal schedules to the nearest feasible ones. These legalized schedules are then used to re-initialize the parameters ( \boldsymbol{\mu,\sigma} ) for further optimization (see Appendix A for detailed algorithm).

A1.SS2.p1.1 | Modulo scheduling introduces cyclic constraints due to back-edges. To resolve these, we employ a simple fixed-point relaxation algorithm. Unlike standard topological legalization, this iterative approach repeatedly passes through the graph to resolve back-edge requirements alongside forward dependencies. The process continues until the schedule stabilizes or a maximum iteration threshold (equal to the number of nodes) is reached, signaling a potential recurrence violation or depth overflow. This tries to find a feasible schedule for pipelined execution while not significantly changing the original input. The algorithm is summarized in Algorithm 3.

## 2602.20901v1
https://arxiv.org/html/2602.20901v1

S4.SS2.SSS0.Px1.p1.1 | We adopt five baselines: PhysAgent [15], Chain of Thought (CoT) [60], and three variants of vanilla reasoning with additional inputs of segmentation map (SAM), depth map (Depth Anything V2), or both together. PhysAgent is one of the most advanced methods for enhancing VLMs’ physical commonsense and understanding of the real world. We use GPT-4o as the VLM for all methods, and the number of iterations T in RSGAR is set to 5. The results of all methods on SpatiaLQA are shown in Tab. 4, which shows that RSGAR achieves the best performance among all methods, while CoT attains the second-best result due to its ability to enable more stable reasoning. Other baselines even underperform the vanilla reasoning, indicating that simply incorporating physical priors or visual cues does not contribute to the spatial logical reasoning of VLMs.

S4.SS2.SSS0.Px2.p1.1 | To answer this question, we further analyzed RSGAR from the perspective of the number of steps in the annotated answers. As shown in Tab. 4, although RSGAR shows a slight decrease in performance on samples with fewer answer steps, it significantly improves the performance of VLMs on samples with more answer steps. This suggests that RSGAR can improve VLM performance on complex tasks by explicitly representing the relationships among key objects in the original scene.

## 2602.21188v1
https://arxiv.org/html/2602.21188v1

S3.SS3.p2.1 | To generate a multi-view long video, we sample in both temporal and view dimensions, as shown in Figure 4. In the temporal dimension, the video is partitioned into multiple overlapping long segments, each with T_{\text{long}} frames and N_{\text{short}} views, using a sliding window with T_{\text{ol}} overlapped frames. In the view dimension, the video is partitioned into segments, each containing T_{\text{short}} frames and N_{\text{long}} viewpoints, with N_{\text{ol}} overlapped views. At each denoising timestep t , we process each temporal and view segment as follows:

S3.SS3.p6.1 | At each timestep t , the denoised temporal-dimension latent feature \mathbf{z}_{t}^{\text{ST}} and view-dimension latent feature \mathbf{z}_{t}^{\text{SV}} are weighted combined, which produce the final denoised latent feature \mathbf{z}_{t-1} . We compute the \mathbf{z}_{0} by applying the above denoising process until timestep t=1 , which is then decoded to generate the final long multi-view human video.

S4.SS3.p2.1 | Effectiveness of Sampling Strategy. To validate the effectiveness of our spatial-temporal sampling approach, we conduct a qualitative comparison, as shown in Figure 8. The left image presents results for two adjacent views when only temporal window sampling is applied, where noticeable inconsistencies appear (e.g., the color of the shorts shifts from white to orange). The right image displays results for two adjacent frames when only view window sampling is used, revealing inconsistencies such as the appearance and disappearance of the T-shirt logo. In contrast, our sampling method mitigates these issues, achieving global coherence across the generated sequence. These results demonstrate that our approach effectively addresses the challenge of long-range dependencies in multi-view human video generation, enhancing both visual quality and coherence.

S5.p1.1 | We focus on 4D human video generation of the full body, which may inadvertently introduce artifacts in finer facial regions due to the trade-off between global coherence and local detail. As illustrated in Figure 9, our method occasionally produces distortions in areas such as the nose and lips, where precise geometry and texture are critical for realism. This issue arises because the current framework prioritizes consistent motion and structure across the entire body, potentially underrepresenting high-frequency facial details. A potential solution is to crop the head region and process it separately using a dedicated neural network specialized for facial generation. This modular approach allows finer control and resolution in the facial area, which can then be seamlessly fused with the body output to achieve higher overall visual fidelity.

## 2602.21193v1
https://arxiv.org/html/2602.21193v1

S5.SS4.SSS0.Px1.p1.1 | We investigate a few trajectory filtering strategies discussed in Section 4.4. For dataset adapters (Table 6), while we observe no significant difference on each subset, the no-filter setting yields the highest performance on the full set (9.66%) and is thus adopted. For synthetic tasks (Table 8), the impact is even more substantial: no filtering (12.4%) significantly surpasses both complete-only (6.74%) and success-only (5.06%) strategies. This performance gap suggests that strict filtering is detrimental as it discards over half the available training data. Moreover, retaining unsuccessful trajectories appears to provide valuable supervision, exposing the model to realistic error states and recovery patterns that enhance overall robustness.

S5.SS6.p1.1 | We investigate two SFT curriculum strategies for data mixing: (1) a two-stage curriculum, where we first train on dataset adapters, followed by synthetic task data; and (2) a single-stage strategy, where we train on all datasets concurrently. As demonstrated in Table 9, the two-stage curriculum yields no performance advantage over simple mixed training. Consequently, we adopt the single-stage mixed training strategy for all other experiments in this paper.

## 2602.21196v1
https://arxiv.org/html/2602.21196v1

S3.SS3.p2.1 | Formally, given a model with attention heads H and number of context parallel devices C , UPipe chunks the attention execution into H/U stages, processing U heads per stage. During forward pass, the execution begins by projecting the input X into Q_{U}^{0} , K_{U}^{0} , and V_{U}^{0} i.e., the first U heads. This is followed by inp_all_to_all, resulting in U/C heads per device. Note that U must be divisible by C to ensure that each device processes an integer number of heads. In the next stage, we process the next U heads while reusing the memory buffers from the previous stage (i.e., use Q_{U}^{0} buffers to store Q_{U}^{1} and similarly for other tensors). Therefore, the memory usage remains \mathcal{O(\text{$U$)}} throughout the execution.

S3.SS3.p4.1 | Consider the execution on Device 0: in stage 0, the input X_{0} is projected into the first two heads H_{0} , H_{1} of QKV . Next, inp_all_to_all is performed on H_{0} , H_{1} so that device 0 has H_{0} for the entire sequence. Notice that during all-to-all, we only need buffers for 2 heads (as opposed to 4 heads in DS-Ulysses). We then perform attention on H_{0} , generate output for head 0, and perform out_all_to_all. In the second stage, X_{0} is projected into the next two heads H_{2} , H_{3} . At this point, heads H_{0} , H_{1} are already processed so we reuse their HBM buffers to store H_{2} , H_{3} . Next, we perform all-to-all and similarly reuse the all-to-all buffers from stage-0. For the final output, we initialize the buffers in the beginning and fill them during execution. This avoids the concatentation of individual chunks, which otherwise degrades performance.

S5.SS4.p1.1 | As shown in Figure 6, we perform an ablation study on UPipe’s hyperparameter U i.e., the number of heads processed per stage. It allows memory-runtime tradeoff, where larger U corresponds to more heads processed per stage, resulting in higher memory usage and lower runtime. Conversely, when U=C , UPipe provides maximum memory benefits, at the cost of slight performance degradation due to kernel launch overhead (though at longer context lengths, this overhead is amortized by the increased length as shown in Table 5). We perform the ablation using Llama3-8B on 4 \times H100 GPUs, with a context size of 512K tokens.

## 2602.21198v1
https://arxiv.org/html/2602.21198v1

S3.SS2.SSS1.p4.2 | where the retrospective prompt x_{\text{retro}}^{j} includes: (1) the complete working memory window \mathcal{W}_{t} as context; (2) a historical action a_{j} to be retro-reflected based on the current outcomes; (3) its most recent reflection f^{j}_{\text{recent}} (either f_{e}^{j} from the current working memory \mathcal{W}_{t} if this is the first retrospective evaluation, or f_{r}^{j} from the previous retrospective round and stored in a retro-buffer \mathcal{D}_{\text{retro}} ; and (4) the current observation o_{t+1} . After retro-revision, we update \mathcal{D}_{\text{retro}} and store only the most recent retro-reflection for each action. As \mathcal{W}\cup\mathcal{D}_{\text{retro}} grows larger with actions, we may subsample historical actions if necessary to keep it tractable.

A2.SS1.p2.1 | On average across Long-Horizon Household Tasks and Cupboard Fitting Tasks, we observe a \sim 3\times increase in per-step wall-clock time compared to the vanilla baseline:

A2.SS3.p1.1 | A natural concern is whether the performance gap is merely due to increased wall-clock time. To evaluate this, we construct a time-matched variant where the vanilla baseline receives a 3\times steps budget, matching the approximate inference time of our full model:

## 2602.21202v1
https://arxiv.org/html/2602.21202v1

S5.p1.1 | We now describe Attention-Guided Clustering (AGC), a compression technique designed to maximize the utility of a fixed token budget for document compression in any modality. AGC (shown in Figure 2 (a)) combines three main components: (i) Attention-based Centroid Selection, which utilizes learned universal query tokens to identify semantically salient information; (ii) Hard Clustering, which uses hard assignment to group tokens to reduce redundancy while preserving distinct semantic details; and (iii) Weighted Aggregation, which constructs the final compressed representations by averaging tokens within each cluster weighted by their saliency to mitigate the optimization challenges of hard operations.

S6.SS3.SSS0.Px2.p1.1 | In Table 3, we break down the performance of each method on the ViDoRe topic splits. Comparing the runs with the same training configurations, we see that AGC and H-Pool significantly outperform SeqResize and MemTok. H-Pool and AGC appear to be relatively equivalent, with their averages only differing by 0.002 in nDCG@5. However, when looking at the breakdown by topic, we see that AGC is more stable across domains than H-Pool. We also compare to another learned compression method, MetaEmbed (Xiao et al., 2025). We find that AGC and H-Pool have comparable or better performance to MetaEmbed. This highlights the strengths of both AGC and H-Pool, even when training at smaller scales.88 8 We note that the comparison to MetaEmbed is not 1-to-1 because we are only capable of training at \frac{1}{20} th of the scale.

S6.SS4.SSS0.Px2.p1.1 | In Table 5, we analyze the impact of varying token budgets and the number of appending tokens of AGC on retrieval performance on MSR-VTT. We observe that performance scales positively with both the size of the token budget and the quantity of appending tokens. Notably, even under the most extreme compression setting (a budget of 5), AGC maintains robust performance, outperforming the single dense vector encoder, OmniEmbed-7B, despite using a smaller 3B backbone. When looking at the number of appended query tokens and the budget, we find that it is generally optimal to align the number of appended query tokens and the budget size. Additionally, we see that 32 appended query tokens and a budget of 5 outperforms 5 appended query tokens at the same budget, but we don’t see the same pattern for 128 appended query tokens and 32 budget. This suggests that it is important to avoid a low number of query tokens, but that performance doesn’t necessarily scale to the number of appended query tokens at any budget.

## 2602.21204v1
https://arxiv.org/html/2602.21204v1

S5.Thmtheorem1.p1.1 | Consider a TTT model whose inner-loop function has a linear, bias-free final layer,

S5.Thmtheorem1.p1.2 | where \phi(x;\Theta)\in\mathbb{R}^{D_{\mathrm{h}}} denotes the hidden representation of the inner-loop function with parameters \Theta , and W\in\mathbb{R}^{D_{\mathrm{h}}\times D_{\mathrm{out}}} is the weight matrix of the final layer. Suppose that at step t , the inner loop performs one step of gradient descent on an objective \mathcal{L} with learning rate \eta , using key input k , updating all trainable parameters,

S6.SS1.p8.1 | Results. We progressively apply the above ablations to LaCT on the LLM and NVS tasks, and to ViTTT on the image recognition task, with results summarized in Table 2. Surprisingly, restricting the inner loop to update only the final MLP layer consistently yields the best overall performance across tasks, suggesting that many of the more complex design choices are unnecessary, or even detrimental. Most other components contribute only marginally to performance, with two notable exceptions: deeper MLPs are beneficial for the NVS task, while gradient orthogonalization improves performance on the LLM task. Overall, reducing the full TTT formulation to a basic linear attention operator (Variant 6) results in only minor performance degradation ( +0.4 perplexity on LLM and -0.2 dB on NVS). For the LLM task, Table 2 reports perplexity at 32k sequence length, with results across other lengths shown in Figure 3.

S6.SS2.p2.1 | The key insight is that when weight normalization is removed and only the final-layer parameters are updated, the state update becomes associative. In this setting, the kernel function \phi_{t}(\cdot)\triangleq\phi(\cdot;\Theta_{t}) is static and independent of sequence history, allowing the recurrence in Theorem 5.3 to be computed via a parallel prefix scan rather than sequential token-by-token updates.

S7.p3.1 | Our analysis applies to most current TTT formulations but is limited to settings where the inner-loop final layer is linear and bias-free. Extending these insights to nonlinear final layers, and exploring deeper connections between TTT and modern linear attention mechanisms in both directions, remain important avenues for future work.

原Theorem 5.1–5.3 CORE 830–1512 的完整TeX行：
o=\phi_{t+1}(q)\left(W_{t}+\phi_{t}(k)^{\top}g_{t}(k)\right),\quad g_{t}(k)\triangleq-\eta\,\frac{\partial\mathcal{L}}{\partial f_{t}(k)}.
o=\hat{q}\left(S_{0}+\hat{k}^{\top}\hat{v}\right),
\hat{q}=\phi_{t+1}(q),\quad\hat{k}=\phi_{t}(k),\quad\hat{v}=g_{t}(k),\quad S_{0}=W_{t}.
o_{t}=\hat{q}_{t}\left(S_{0}+\sum_{i=0}^{t}\hat{k}_{i}^{\top}\hat{v}_{i}\right).
\hat{v}_{i}=m_{i}(k_{i})\;\triangleq\;g_{i}(k_{i})\cdot\sum_{j=i}^{t}\beta_{i}^{j}.

## actual owner — books/part-05-inference-system/49-tensorrt-llm.md

L28–30:
扩大搜索空间以后，还要判断哪些局部计划能安全地裁剪。若两个 partial mapping 对未来组合暴露的 tensor tile、dataflow、执行顺序或 backing memory 不同，仅比较当前 latency 与占用就可能删掉后来更好的计划。一个条件分支先按这些接口划分 compatible groups，再在组内保留 Pareto 前沿；中间 tensor 的 reservation 保留整个 lifetime，包括未来尚未确定的消费关系，只有条件充分时才 collapse。资源计数也不能统一相加：同一 branch 内可并存的 reservation 求和，不同互斥 branch 取最大值，未知未来分支不能提前折叠。这是资源 lifetime 的合成条件，不是执行 latency 的串行或并行公式。这让局部裁剪与后续组合共用明确条件，但所谓最优仍仅针对声明的 mapspace 和 cost model，而不是所有可执行 kernel。<!-- source-family:SF-2026-ARXIV-2602-15166 -->

这类搜索还须与目标硬件测量分账。[Fast Fusiest v1](https://arxiv.org/html/2602.15166v1)主要在 TPUv4i-like 解析模型下比较，复用缓存的 baseline 查询时间及给予其他方法更大搜索预算都影响所报速度与质量；它没有证明端到端 GPU serving 加速。接口不兼容、reservation 分支过多或 cost model 偏差较大时，应扩大保留集合或回到已有 backend 的局部 autotune 与实机 profiling，不能凭一个局部 Pareto 标签跳过正确性和质量验收。

L113–115:
异步 copy、tensor-core schedule 与 synchronization 若散落为 imperative side effects，很难证明优化前后同义。更可审计的 compiler contract 以 sequential specification 作为语义与 fallback，把 parallel annotation、unsafe rewrite 与 equivalence check 共同版本化；compiler 只有在证明条件成立时才能提交并行计划。<!-- source-family:SF-2026-ARXIV-2609-16389 -->

这种分权牺牲一部分手工自由并增加证明成本。当前证据限 H100 concrete-size GEMM，且存在 TMA unsafe rewrite、无完整 CUDA semantics；Blackwell、非 CUDA 或动态 shape 必须重新验证，失败时回退顺序/已知 kernel。

## actual owner — books/part-06-ai-infrastructure/66-evaluation-system.md

L132–134:
任务难度切片也不能只按输入长度或实体数划分。关系推理可以分别改变输入规模、任务生成器规定的 binding arity，以及识别或比较单个 operand 的难度；它们是三个不同轴。同一 arity 下更多输入可能提供额外线索，而非必然更难；实体少却需要同时满足更多关系，也可能比长输入更困难。EvalSpec 应保存生成规则和 oracle，在输出格式、scorer、推理预算可比的切片中交叉改变这些轴，不把换任务后不同的 accuracy、substructure 或 recall 拼成同一条下降曲线。<!-- source-family:SF-2026-ARXIV-2604-12176 -->

这种控制比单一长度排行榜增加生成、oracle 与样本预算，也仍只能约束已测混杂。生成器定义的 relational complexity 是任务属性标签，不是模型内部容量的计算下界；合成、多选与有限 token 预算下的失败，更不证明增加任意计算都无效。简单任务、长度已主导成本时仍可保留原长度切片，复杂关系任务再补上述交叉维度。受限关系评估支持将这些难度来源分账，而不支持通用 arity 阈值或唯一失败因果。

## actual owner — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

L85–87:
这条路径以更低跨帧成本换 memory drift、历史细节损失和新的 clean-pass commit 纪律。长程一致性不足、状态异常或任务依赖精细历史时，应回退 full attention、短窗口重算或两者混合。现有证据只支持作者的视频模型与受测数据，不证明 linear memory 能替代任意视频历史，也不授权 runtime 偷改帧边界。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-16579:start -->

L1430–1432:
这一分工可摊销静态新视角视频的生成成本，却新增 count predictor 的训练、稀疏视图生成、重建、affine 坐标对齐及 chunk 衔接成本；affine 拟合不是物理位姿证书，局部 chunk 也不证明全局长程一致。公开 GH200、256²、静态相机视频只支持作者的局部质量/资源取舍：插值时间不能替代包含关键帧与重建的端到端时间，部分 FID 对照退步、无 chunk 的 FVD 也较原生成器更差。动态物体、遮挡空洞、模糊细节或坐标漂移超出该分支时，保留密集相机条件生成、普通 I2V 或真实多视角重建；不能由画质或渲染速度推导物理可信度与生产 SLO。

相机控制与动画内容的时间还应分开：输出frame index描述要交付的序列位置，不等于场景内容所处的动画时间。将source/target各自的camera与animation-time分别编码，时间压缩器再把RGB帧时间映射到latent步，才能表达同一运动的retime与新视角，而不是用一个position index兼任两种控制。该路径依赖temporal warp监督与合成camera×time网格覆盖；估姿和首段尺度对齐只是评价协议，不是绝对metric或真实三维真值。网格构造、时间压缩与条件训练都付费，有限画质/位姿指标不授任意4D一致、persistent world state或生产SLO；时间支持不足、估姿不稳或跨camera对齐失败时，保留原动画时钟、固定相机与单控制分支。<!-- source-family:SF-2026-ARXIV-2512-25075 -->

## actual owner — books/part-04-training-system/27-data.md

L542–560:
Terminal 与 repository 任务进一步说明，训练 row 的最小单位不能只是 instruction/response。可执行能力来自
task intent、初始 filesystem/container state、tool protocol、trajectory 与 verifier 的联合分布；缺少任一项，
“成功样本”都可能只是 harness artifact。数据控制面应保存：

```text
repository / container / dependency snapshot
+ task and hidden verifier identity
+ scaffold / tool schema / policy checkpoint
+ complete success or failure trajectory
+ final artifact and executable outcome
```

失败轨迹可以暴露 recovery signal，却不能因“更难”就天然优于成功轨迹：environment build failure、test
incompleteness 和 agent bug 会混入同一 failure label。诊断结果可以驱动下一轮 source/task/environment quota，
但 diagnostic model 与当前 policy 的 blind spot 也会使 curriculum 追逐噪声。因此闭环应是
`failure attribution → bounded mixture proposal → regenerated executable rows → independent validation`，并保留
固定人工/历史数据作为分布锚。Terminal-capability data engineering、SWE-rebench V2 与 DPE 分别为数据对象、
environment diagnostics 和 diagnostic-driven mixture 提供了实验性证据；它们没有证明某个数据量或失败比例是通用配方。


## actual owner — books/part-04-training-system/36-distributed-training.md

L591–606:
Ulysses-style Context Parallel 用 sequence shard 与 All-to-All 交换 head/sequence views；一次物化全部 heads
在中等长度下 launch 少、控制简单，是合理基线。但当 context 极长时，通信/attention buffer 可能先于 Attention
公式本身成为 OOM 边界。一个条件化分支是按 head chunks 建立小流水：

```text
all-head materialization
→ head-stage partition
→ All-to-All + attention for one stage
→ reuse bounded communication/attention buffers
→ concatenate output heads
```

它用更多 stage、collective launch 和 ordering state 换 memory headroom；chunk 越小，capacity 越好，overhead
通常越高。GQA 还要求 head ordering 与 KV group 复用一致。传统一次性 Ulysses 在 buffer 可承受、短 context 或
希望降低 orchestration cost 时仍成立。Untied Ulysses/UPipe 为这条 memory–throughput trade-off 提供了 H100
实验性证据，不证明其 chunk 大小或长上下文倍率可跨 topology 与 framework 外推。

## actual owner — books/part-07-agent/80-reflection.md

L26–44:
Self-Refine 让同一模型产生 feedback 和 revision；Reflexion 将环境反馈总结为语言并写入 episodic memory。
二者是**不修改权重的 verbal test-time adaptation**，不等同于第 31～34 章的参数训练或 policy optimization。
更激进的分支会在 episode 内把 retrospective feedback 编译成 LoRA/weight update；它仍发生在 test time，
但 ownership 已跨入参数状态，不能继续只称为 Reflection：

```text
trajectory + outcome
→ retrospective diagnosis
→ bounded adaptation dataset / objective
→ ephemeral parameter update
→ validation on next attempt
→ commit, reset or rollback
```

这可能把经验从 Context 内化到 policy，却新增 optimizer state、base/adapter identity、catastrophic drift、
contamination 和 rollback。Verbal reflection 在任务短、风险高或不能验证更新时继续成立；参数 adaptation 只有
在 scope、budget、held-out verifier、reset 和 provenance 明确时才可使用。Reflective Test-Time Planning 的
论文提供了这一边界案例，不证明 episode-level LoRA update 普遍优于语言反馈。


## actual owner — books/part-07-agent/76-rag.md

L411–430:
query；直接保存全部向量提高表达容量，却扩大 storage、memory traffic 和 rerank cost。把一组 vectors 压成固定
预算的代表向量，改变的是 persisted index state，不会让 encoder 无需读取原始 document，也不会让 query-time
reader cost 自动同比下降：

```text
raw multimodal document
→ encoder produces token / patch vectors
→ budgeted compression builds index artifact
→ query late-interaction against compressed state
→ optional source dereference and reader verification
```

压缩率、encoder revision、vector budget、distance rule 与 reconstruction/selection policy 必须进入 index identity。
更小 index 用 recall、rare evidence 和 rebuild cost换容量；single-vector embedding 在吞吐与治理优先时仍合理，
full multi-vector index 在高召回和容量允许时继续成立。Multi-Vector Index Compression 的实验只支持特定模型、
数据集和 budget 下的 frontier，不证明 indexing path 或端到端 latency 等比下降。

固定向量预算还可以按**查询实际需要哪一个 patch**分配，而不只按文档向量的几何密度重建。先用离线 query tokens 估计原始 MaxSim 的胜出频率，将它作为 source marginal；再以 target-balanced 的熵正则 transport 把重要源向量软分配给有限代表槽位，随后用 Lloyd readout 生成压缩向量。在线仍执行固定 compressed MaxSim，不逐次查询重建索引。这把需求校准与在线评分分开：使用 1,000 个 query tokens 可能只对应几十个查询，其分布、backbone 与 encoder revision 必须进入校准及 index identity。<!-- source-family:SF-2026-ARXIV-2609-21018 -->

需求加权增加 query-token 校准、源×槽位 transport 与 readout 成本；软计划的平衡也不保证最后硬 cluster 等大。[MAGIC 的 Proposition 1](https://arxiv.org/html/2609.21018v1)只在 unit document vectors、query norm 不超过 1 且使用真实 population 胜出概率时，约束期望的正向 score decrease，不约束绝对评分误差、分数虚增、排名或召回。估计需求可能漏掉 rare intents，换 backbone 要重建；受限 ColQwen2.5、2,000 页、单 H20 的穷举实验在较宽保留向量预算下仍有切片反退，per-page 构建成本也不能冒充全局字典或端到端 RAG/QPS 成本。验收失败时仍应恢复更大预算、完整多向量索引或 source dereference，而不从这一上界推导任意 query 的证据保全。

## actual owner — books/part-02-model/22-long-context.md

L650–657:
### 先定义写入目标：重建关联还是保留后续行为

先看把写入目标显式化的 test-time training with KV binding：若每步用历史 key/value 定义在线回归
目标并更新 fast weights，在特定假设下其读写可重写为 history-dependent linear Attention。这个等价性解释了
为何它能携带连续计算状态，却不赋予逐事实回读、provenance 或删除语义；当 optimizer、nonlinearity、更新步数
或 binding 假设改变，等价关系也可能失效。普通 KV 在精确 token addressing 时仍合理，外部 Agent Memory 仍由
第77章治理。


L517–519:
这种思想与 LSTM 共享“有限状态需要学习保留和遗忘”的祖先，但 state contract 不同。LSTM 主要维护向量 cell state，并用 input/forget/output gates 做逐维递归更新；DeltaNet 一类机制维护矩阵 fast-weight state，用 Query 读取、用 key-value association 与 prediction error 定向改写。前者更像更新当前序列摘要，后者显式暴露内容寻址的关联结构。两者都把历史压进固定状态，都会碰撞、覆盖和遗忘；Gated DeltaNet 的 chunkwise parallel algorithm 改善的是训练执行路径，不会把有损状态变成完整 token archive。

仿射 scan 的并行条件还允许另一种写入折中。若非线性更新必须读取尚未算出的 `S_(t-1)k_t`，每个 transition 便依赖中间 state；可先用仅依赖已知 input 的短卷积生成 local proxy，再在该 proxy 上迭代形成非线性 residual 分量，将多个 outer products 注入写入项 B，同时保持 A/B 不消费中间 recurrent state。这里 state-independent 是训练侧可预先构造 transition 的接口条件，不是无 input 条件或没有历史；多分量注入的 rank 至多为 L，只有独立方向才达到上界，residual subtraction 也不自动是正交化。<!-- source-family:SF-2026-ARXIV-2602-10796 -->
