## 2602.20659v1

https://arxiv.org/html/2602.20659v1；精确HTML原paragraph机械摘段（非摘要）：

Temporal integration is performed by a transformer over a recent fixed-length window of the frame encoder representations, providing short-term temporal context. To enable recursion across arbitrarily long horizons, the previous belief state  \mathbf{b}_{t-1}  is pre-pended as a token, allowing the model to condition new evidence on accumulated dynamics-relevant history. This belief token actively conditions temporal attention, biasing integration toward relevant interactions and dynamics rather than simply propagating state. The corresponding output yields an evidence representation  \mathbf{e}_{t} , which summarizes new observations conditioned on the prior belief. To capture uncertainty and branching futures, the model further introduces a stochastic latent variable  z_{t} . The model learns a prior  p(z_{t}\mid\mathbf{b}_{t-1})=\mathcal{N}(\mu_{p},\sigma_{p})  representing predicted uncertainty before observing the next frame, and a posterior  q(z_{t}\mid\mathbf{b}_{t-1},e_{t})=\mathcal{N}(\mu_{q},\sigma_{q})  incorporating new evidence. The deterministic belief is then updated via,

We adopt a vision–language–action framework in which a vision–language model (VLM) is decoupled with a diffusion-based low-level controller. The VLM is queried once per task using the instruction and the initial visual observation to produce an image-conditioned semantic task representation. This vector is projected through a lightweight MLP to obtain a compact intent embedding  \mathbf{I_{t}} , which remains static throughout task execution, since the semantic goal is fixed for a given task.

We evaluate computational efficiency using latency and memory, with all inference measurements performed on one NVIDIA A100 GPU. Figure 4 compares the average episode latency of RB-VLA with prior methods. Since task instructions and semantic goals remain fixed within an episode, RB-VLA queries the VLM only once at the beginning of the task to obtain the intent embedding, and does not re-invoke it during execution. As a result, RB-VLA achieves over five times lower latency than stateless OpenVLA and RT1-X, and is more than three times faster than multi-frame GR00T-N1, which repeatedly processes multiple visual frames. This demonstrates that decoupling semantic grounding from control enables efficient real-time deployment.

We ablate key components by selectively removing them and measuring the drop in average success rate over 40 episodes on the same long-horizon, multi-stage tasks under partial observability. Starting from the full RB-VLA, we evaluate: (i) no frame-encoder targets for training the belief (using only vision embeddings), (ii) deterministic belief without stochastic latent variables, and (iii) no belief–policy conditioning. As shown in Table III, each removal degrades performance, with the lowest performance when belief is decoupled from control (a standard DiT policy) and the highest success achieved by the full RB-VLA. This highlights the need for a dynamics-grounded belief state, since diffusion model alone lacks the dynamics-consistent causal state required for long-horizon, multi-stage behavior.

We deploy RB-VLA on a physical UR5 manipulator under conditions closely matching the UR5 MuJoCo setup used in simulation. The model successfully transfers to real hardware without architectural changes, demonstrating effective sim-to-real transfer. The diffusion policy is further fine-tuned on 100 real-world trajectories to adapt to sensor noise and unmodeled dynamics. Using the learned belief representation, the system achieves reliable long-horizon execution on multi-object pick-and-place tasks under partial observability, maintaining low inference latency and stable closed-loop control despite visual noise and actuation variability. Over 25 real-world trials, RB-VLA achieves 68.0% success rate, successfully completing grasp–transport–place cycles without manual intervention.

## 2602.20662v1

https://arxiv.org/html/2602.20662v1；精确HTML原paragraph机械摘段（非摘要）：

In order to further improve the memory density by leveraging sparsity, we propose a sparsity-aware ROM design by treating the memory content as a simple combinational logic function from input address to one-value bits output rather than a pre-defined physical structure. The output of zero-value bits of input addresses are tied directly ground without generating any logic. Figure 6(d) shows the verilog code snippet of the given example.
This design effectively erases the area cost of all zero-bits of weights. Considering we are targeting on ternary models, the ratio of zero-value bits is extremely high as the zero-valued (represented in ’00’) parameters are the majority. In addition, the +1 and -1 values are encoded in ’01’ and ’10’ in our design to further improve the ratio of zero-value bits.
This design also leverages common sub-expression elimination in EDA tools (Figure 6(c)(d)) to further merge logic and reduce area. In the example, this reduces transistor count from 64 to 28, achieving significant savings.

To implement this efficiently, the LoRA adapter matrices ( A  and  B ) are stored in on-chip SRAM, sharing resources with the KV Cache. We adopt a quantized adapter approach, using ternary weights for the LoRA matrices. Crucially, this adapter path reuses the existing Ternary  \times  FP8 compute arrays within our MVUs, minimizing the additional hardware logic required for flexibility. The outputs from the base path ( h_{base} ) and the adapter path ( h_{lora} ) are then summed in the Vector Unit (VU) to produce the final result.

We measure the overall system performance via cycle-accurate, high-speed simulation using Verilator. We primarily evaluate the performance on the BitNet-2B[36] model, using tasks with varying input and output sequence lengths (e.g., 64, 128, 256, and 512 tokens) to comprehensively measure performance.

Fig 9 also plots the silicon efficiency, measured in synthesized gates per mm2, which reveals a subtle design trade-off. While higher sparsity reduces the absolute number of logic cells required, at extreme levels of sparsity, the increased routing complexity from irregular logic placement can slightly diminish the area gains per gate. Nevertheless, even with this second-order effect, the overall density advantage remains substantial across the entire realistic sparsity range for ternary LLMs. Compared to memories generated by a standard memory compiler on the same technology node, TOM’s ROM density is 5.2x higher than a standard ROM and 3.3x higher than a standard SRAM at a 65% zero-bit ratio.

We also analyzed ROM bank granularity (Fig 10), fixing sparsity at 70% and width at 128. Data density peaks at 15.0 MB/mm2 at a height of 1024. This non-monotonic behavior reflects the synthesis tool’s optimization (e.g., common sub-expression elimination), which finds a ’sweet spot’ at 1024-height, balancing optimization scope against routing complexity.

We analyzed the impact of increasing the maximum context length on TBT (Time-Between-Tokens), area, and power, as shown in Figure 15(b). The TOM architecture possesses inherent computational redundancy when processing Attention. Consequently, TBT does not increase significantly as the context length scales (e.g., up to 2560 tokens). The primary cost of supporting longer contexts is confined to the on-chip SRAM required for the KV Cache. The area and power of this SRAM scale linearly and predictably with the context length, which is an unavoidable trade-off.

## 2602.20666v1

https://arxiv.org/html/2602.20666v1；精确HTML原paragraph机械摘段（非摘要）：

In our experiments on the ShapeNet [8] dataset, we compare our method with several baselines for both box-splitting generation and bounding-box-conditioned shape generation. For box-splitting, we evaluate against a token prediction model and an inpainting approach using an unconditional diffusion model that preserves existing boxes while filling two new ones. Our conditional diffusion model achieves the best performance, while the inpainting baseline shows comparable but slightly inferior results. For bounding-box-conditioned shape generation, we compare with Spice-E [66], which uses Shape-E [66] instead of our 3DShape2VecSet, and with a finetuned version of 3DShape2VecSet [89] that replaces ControlNet with a Gated Mechanism. Our model outperforms these alternatives in both the quality of generated shapes and their alignment with the input bounding boxes.

Our objective is to learn a generative model for sets of 3D bounding boxes as shape abstractions, which capture both a diverse collection of shapes and varying levels of granularity for each shape. To achieve this, we represent an arbitrary 3D shape using hierarchical shape abstractions [55] structured as a binary tree, as illustrated in Figure 2. The root node of the binary tree is a single unit cube that completely encloses any arbitrary shape. As we traverse deeper into the tree, each internal node splits into two child nodes through splitting operation. This operation refines the abstraction by subdividing a chosen box, called the pivot  b_{v} , into two child boxes denoted by  \mathcal{C}(b_{v}) . Formally, at a given split step  s  in the tree structure, we have a set of 3D bounding boxes  \mathcal{B}_{s}=\{b_{i}\}_{i=1}^{N} . Each split step can be expressed as  \mathcal{B}_{s+1}:=\mathcal{B}_{s}\setminus\{b_{v}\}\cup\mathcal{C}(b_{v}) ,
where the coarser pivot box is replaced with two newly generated child boxes with finer details (See Figure 2).
This split process provides progressively more detailed approximations of the input shape. At the finest level of detail, a collection of the leaf nodes in the tree represents the most detailed shape abstraction. This hierarchical representation thus can provide diverse shape abstractions at any level of granularity, from a single coarse cube at the root to a detailed collection of boxes at the leaves.

Our training data consists of hierarchical shape abstractions generated using SMART [55]. Given an initial set of over-segmented bounding boxes  \mathcal{B}_{S}=\{b_{i}\}_{i=1}^{N} , SMART iteratively performs bottom-up merging. In each iteration, it selects two boxes and merges them into a single parent box that tightly encloses the combined region. This parent box serves as a pivot  b_{v}  in our hierarchy, with the two merged boxes becoming its children  \mathcal{C}(b_{v}) .
SMART continues the merging process until reaching to an appropriate number of bounding boxes that best describe the given shape. These boxes are used as the leaf nodes in our binary tree;
refer to Table A4 for the statistics on the number of leaf node boxes. Based on the leaf node boxes (SMART outputs), we further proceed with an iterative merging process until only a single box remains, building the binary tree up to the root. We set the root box to always be a unit cube; all raw shapes are normalized to fit within the unit cube.
Each 3D bounding box  b_{i}=\{c_{i},s_{i},o_{i}\}\in\mathbb{R}^{15}  is parameterized by center  c_{i}\in\mathbb{R}^{3} , side lengths  s_{i}\in\mathbb{R}^{3} , and a flatten orientation matrix  o_{i}\in\mathbb{R}^{9} .

The conditional generation task performed by our Child-Boxes Diffusion can also be seen as a completion task, where missing parts are generated while keeping the given parts fixed. Previous work [45] has demonstrated that the completion task (inpainting for images) can also be achieved using an unconditional diffusion model by combining one-step denoising outputs for the missing parts with forward process outputs for the given parts at each denoising step. We also explore this option by training another diffusion model that uses only the number of bounding boxes as its only condition. The details of this alternative approach are discussed in Section 5.1, where we evaluate it as one of the baselines. While this approach shows comparable performance, it yields slightly inferior results compared to the conditional model.

We presented a box-splitting-based interactive 3D shape generation framework composed of two generative models. The first model, BoxSplitGen, is an autoregressive model that enables the progressive refinement of bounding boxes via splitting. We introduce a pivot classifier and a child-box diffusion model to select which box to split and to generate the two new boxes, respectively. The second model is a box-to-shape generative model that effectively adapts a pre-trained unconditional 3D diffusion model.
We demonstrate that the proposed framework facilitates intuitive 3D generation by mimicking the human imagination process from abstract concepts to detailed structures. Users can split and manipulate bounding boxes to generate aligned 3D shapes, with diversity naturally decreasing as the bounding boxes become fine-grained.

As discussed in Section 3.4 , the noise prediction network of Child-Boxes Diffusion  \boldsymbol{\epsilon}_{\theta}  consists of a Transformer encoder  \mathcal{E}_{\theta}  and a decoder  \mathcal{D}_{\theta} . The encoder consists of  6  self-attention layers with a hidden dimension of  512 . To indicate the pivot box  b_{v}\in\mathcal{B}_{s} , we use a class embedding  \mathbf{e}_{c}\in\mathbb{R}^{|\mathcal{B}_{s}|\times 512}  encoded from an indicator highlighting the pivot box’s index. Additionally, we also encode the number of input boxes  |\mathcal{B}_{s}|  into a cardinality embedding  \mathbf{e}_{d}\in\mathbb{R}^{512} . These two embeddings are added to the output of each self-attention layer, yielding the final encoder output:  \mathbf{h}=\mathcal{E}_{\theta}(\mathcal{B}_{s},b_{v},|\mathcal{B}_{s}|)\in\mathbb{R}^{|\mathcal{B}_{s}|\times 512} . The decoder  \mathcal{D}_{\theta}  has a similar architecture to the encoder, with each self-attention layer followed by a cross-attention layer. The condition latent  \mathbf{h}  is fed as the key and value in every cross-attention layer, while the noisy two child boxes  \mathbf{x}_{t}\in\mathbb{R}^{2\times 15}  are fed as query. We set a learning rate and batch size to  8e^{-4}  and  2048 , respectively. For sampling, we use the DDIM [68] deterministic sampling process with 50 steps.

## Actual owner books/part-03-multimodal-world-models/25-multimodal-world-models.md

### 原文件L402–417
长程交互不能每次从固定窗口重建世界。系统需要保留 object permanence、camera/view change、已发生 action 和环境 revision。但 persistent state 不等于无限累积 memory；旧 belief 可能被新 observation 推翻。

```text
observed fact -> derived belief -> imagined branch
                 ^                 |
                 +-- reconcile ----+
```

每条状态必须带 provenance、timestamp、confidence 和 supersession relation。

仅把过去的 latent 保存下来，还没有说明它如何随视角与对象运动迁移。一条群结构递归分支先把当前 field of view 的表示写入 latent map，再用已知自身动作的逆变换搬运地图；外部对象则由预测的 velocity channels 分别推进，最后从更新后的地图读出下一观测。自身坐标变换与未知对象动态因此不是同一项预测误差，也不能用画面一致把二者合并验收。该构造的等变论证要求完全观测和满足相应群作用的 encoder；三维实现把 encoder 当作等变近似使用，并没有证明真实感知链精确满足它。离散速度、有限地图与确定性 readout 仍限制多模态动态和长程预测，地图状态不能提升为真实 world state 或控制安全保证。它增加地图写入、变换和训练成本；动作、视角或观测条件不可信时，保留短 horizon observation-conditioned prediction，并由新观测重新校正，而不是继续搬运错误状态。<!-- source-family:SF-2026-ARXIV-2601-01075 -->

固定预算还会迫使 memory 在“保存多少范围”与“保存多细”之间选择。累积历史 RGB/latent 容易追溯，但存储随 rollout 增长；固定六个空间与时空 feature planes 则可把新 chunk 增量写入同一张量。覆盖范围扩大时，先按新的 spatial/time bounds warp 旧 features 与 confidence，再以 confidence-weighted pooling 和 residual 融合新观测。张量尺寸保持不变，却意味着同一格点对应更大的空间或时间跨度：**constant feature storage 不等于 constant information resolution**。

该分支用 coarsening、深度/pose 误差与 warp 插值损失换有界 feature memory，且不证明几何辅助状态或整个生成器总内存恒定。复访一致性必须在更大 bounds 和多次写入后单独验收；窄场景、需要精细重访或定位不可靠时，保留完整历史/较高分辨率、分区 memory 或重建仍更合理。[固定六平面的受限实验](https://arxiv.org/html/2609.37690v1)仅支持 Wan2.2 5B、WorldScore/RealEstate10K 等作者配置的表示与写入取舍，不证明物理状态被完整保存。


### 原文件L421–438

传统 video predictor 可以依靠近期 frames 生成连贯画面，在不需要记住被遮挡实体、未可见变量或可逆 action effect 时这很合理。问题是 pixel loss 只监督可见输出；某个状态若暂时不出现在 token 中，更多 denoising 步数也不会自动创造对它的监督。

因而要区分两种表面上都叫“预测下一帧”的系统：

```text
append-only visual context
→ re-derive hidden arrangement from full history

mutable predictive state
→ update hidden arrangement in place
→ carry the revised state across chunks
```

第一条路径简单、与 Transformer KV 自然兼容，短 horizon 和可见状态已足够时仍然应作为 baseline。当任务要求在多个 chunk 之间保存并修改未可见状态时，需要显式 recurrent / fast-weight state，或一个能表达可逆 transition 的状态更新机制。它获得长 horizon state tracking，却引入状态初始化、更新稳定性、checkpoint/recovery 和 model revision compatibility 问题。

这项证据的重要性在于 evaluation contract，而不是某个架构排名：受控 hidden-state intervention 任务把渲染质量与状态追踪拆开。训练 horizon 内拟合、reward prediction 或画面逼真都不能代替跨 horizon 的 intervention fidelity。它也不证明任意 linear attention 或 fast-weight 机制都会成功；有效的是“可修改状态 + 受控干预验证”这个系统契约。


### 原文件L245–264
它减少高维生成成本并可能强化语义状态，却新增 encoder identity、target drift 与 representation collapse。Embedding
接近只证明在给定 encoder metric 下相似，不证明物理状态正确、因果变量完备或 long-horizon rollout 已校准；必须继续
用 action-conditioned outcome、intervention 与 closed-loop task 检查。需要视觉生成、可审计几何或安全关键细节时，
pixel/structured simulator 仍不可替代。作者实验只支持其模型、数据与下游任务中的表示收益，不外推为通用 world model
objective 优越性。

这条分支还必须把“预测未来”与“更强的同帧特征学习”分开验收。在受限的部分可观测导航实验中，保留同一 temporal Transformer、训练步数和随机种子设置，只把 next-step embedding 目标改成 same-step，长记忆任务的收益便明显减弱；因此不能把收益全部归给新增骨干或 anti-collapse 组合。预测未来的监督可能迫使状态保留当前画面之外的历史信息，但代价是额外预测器与目标漂移，且这组消融只支持作者 Rooms 任务中的条件性判断：短时近全观测控制中，较简单的同帧表示或像素重建仍可能足够，不能据此推出真实环境的长期记忆或安全保证。

<!-- source-family:SF-2026-ARXIV-2603-02765 -->

表示目标换成 latent 后仍要问：**监督是否指定了变化发生在时间轴的哪里**。若一段操作只在稀疏 waypoint 上匹配 latent，flow 可以学到端点却在中途冻结物体、临近终点突然跳变；更低的平均 pixel L1 甚至可能奖励“少动”的模糊预测。条件性修复是在训练 rollout 中沿 decoder 路径加入中间帧监督，并与 object motion/temporal concentration 一起评估，使时间结构而非仅端点进入 objective；推理仍可保持原 latent 表示，不必把 decoder 变成动作权威。这增加 rollout 解码与监督成本，错误的像素权重也可能重新诱发外观过拟合。Frozen Flows Forget 只在 ODEWorld/LIBERO 的作者设置中显示该失效与修复，不证明所有 frozen-latent world model 都会丢运动；若状态仅用于静态语义、无需连续动作，稀疏 latent 目标仍可能足够。<!-- source-family:SF-2026-ARXIV-2609-28414 -->

#### Inverse Dynamics 是有前提的 Anti-collapse Regularizer

只靠 observation prediction 还可能保留与行动无关的外观捷径。若相邻 observation 的变化确实由已执行 action 主导，inverse dynamics 可以要求 latent transition 足以恢复 action，从而阻止 constant representation，并优先保存可控信息。这里的 precondition 必须显式成立：部分可观测、behavior-policy 偏置、外力或与 action 无关但任务关键的状态都会让 action 不可唯一恢复。

因此 inverse-dynamics loss 是 action-information anti-collapse regularizer，不是完整 world-state 真值。它应与 observation reconstruction、multi-view consistency 或外部 state sensor 共存；recoverability 失败时回退更完整的预测目标，而不能把无法解释的变化压进动作表示。现有证据只支持作者环境中的机制，不证明真实环境的全部可控与不可控状态都被辨识。
<!-- source-family:SF-2026-ARXIV-2606-20104 -->

当只有前后 observation 而缺少当前阶段的 action label 时，可以进一步把 forward 与 inverse 模型轮换为彼此的冻结反馈：训练 forward 时，以 frozen inverse 对所给 action/描述的恢复 likelihood 奖励生成 transition 的可辨识性；训练 inverse 时，以 frozen forward 对实际后态的 likelihood 奖励所提 action 对观测的解释。两个责任分别是 recoverability 与 observed-data fidelity，不是同一个模型自评就证明真实因果动作。state-only 只描述后续 RL 数据：作者视觉/语言模型先有带标签 warmup，不能把整条训练路线称为无监督动作学习。

## Actual owner books/part-05-inference-system/49-tensorrt-llm.md

### 原文件L55–69
常驻 GPU 上优化 kernel 通常从已加载的权重开始；端侧模型被回收、每次从 flash 重启时，编译图、加载、解包与 prefill 共同决定首 token 关键路径。先物化图并按层重叠加载是合理基线；若 flash 读取仍主导，存储 bit 数可以低于 NPU 原生计算 bit 数，但必须把转换成本一起编入计划。一个条件分支按 NPU 允许的 output-channel 分配存储精度，将可变 bit 权重拆为 1/2/4-bit 片段并交错存储，CPU 用 SIMD 解包成 INT8 再交给 NPU，而不是要求 NPU 直接执行任意低 bit 格式。

更小文件不必然更快：padding 产生 read amplification，过紧编码又可能让解包成为新瓶颈；分配 bit 所优化的局部误差代理也不是端到端质量保证。执行侧把整数 matmul 留给 NPU、其他算子留给 CPU，并在依赖已满足的队列内优先推进较早 prompt chunk，空闲 CPU 只在 NPU 队列足够长时 steal 任务，避免反过来饿死 NPU。收益因此取决于 flash 带宽、prompt 长度、operator placement 和质量门槛，而非压缩比。受限 [EdgeFlow 实现](https://arxiv.org/html/2604.09083v1)还逆向使用 QNN 图格式，新增兼容性风险；平台不匹配、短常驻负载或质量不满足时，原生格式和静态图仍更简单。<!-- source-family:SF-2026-ARXIV-2604-09083 -->

### 静态图可以固定接口，而不必固定每个 Adapter 值

静态 NPU 把算子与 shape 提前编译，按任务分别构图并共享 base 权重是最直接的基线；将所有 adapter 常驻再用选择 mask 切换，则用容量换更少重编译。还有一个窄分支把同尺寸 LoRA 矩阵变成 runtime 输入：固定图保留低秩更新的算子与 placeholder shape，请求只提供对应的 adapter 值。编译计划因而拥有接口、精度与 layout，adapter artifact 拥有具体参数；换值不等于换 shape，也不能把 adapter 训练方式与执行 ABI 混为一谈。<!-- source-family:SF-2026-ARXIV-2604-18655 -->

输入化仍有搬运、显存与后端 operator coverage 的成本。多输出路径共同 prefill 后隔离 suffix 的 KV，是另一项状态条件，不授权任意 adapter 共用 prefix cache；第45章仍负责 base/adapter/KV 身份，第30章负责低秩训练。[受限手机 NPU 实现](https://arxiv.org/html/2604.18655v1)只支持披露的1B/3B模型、固定接口与设备分支，其不同精度配置、相对评分与吞吐算式不能拼成统一加速证明。尺寸、精度或状态不兼容时应重编译、拆成独立图，或回到已验证的通用执行路径；运行时输入并不消除质量和端到端验收。

### 静态图还要容纳不规则 KV 重算

固定 shape 的静态图并不要求选择性 KV 重算只能回到全量 prefill：动态输入可以切成固定容量 chunk，padding 后用 valid mask 排除无效位置，并强制选择真正末 token 以形成生成 logits；选中位置经过 gather、计算与 scatter 更新原 cache。比较 KV deviation 所需的数值范围又与普通 activation 不同，必要时让差值和 Top-K 使用较高精度，而非沿用一套整数校准。此处的 non-prefix 选择性复用仍是近似分支，静态形状适配本身不授予状态等价保证。

各类 token 分别调用图最简单，却可能产生大量半空调用；新 token 总须重算，因而可以在容量与重算比例约束内并入相邻选择性重算图，再按实测 per-call latency 用动态规划选择 chunk 组合。目标是在 padding 与调用的取舍中最小化所测 graph latency，而不只是最大化复用率。[Dynamic Flow, Static Graph v1 §4/7](https://arxiv.org/html/2609.34727v1)的有限 Qualcomm/小模型结果仍有 QA 质量下降，完全复用虽快却更差；线上须计 KV 搬运和 pipeline，离线 graph compilation、profiling 与跨平台重校准则另作摊销。形状或比较精度不支持、质量门失败、收益不足时，保留 exact prefix reuse、full prefill 或已验证的动态 backend。<!-- source-family:SF-2026-ARXIV-2609-34727 -->

## Actual owner books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

### 原文件L33–59

## 为什么 Autoregressive 是合理起点

AR 将复杂联合分布拆成条件概率乘积。训练可以 teacher forcing，并行计算所有位置的 loss；推理必须依次确定 token。它的稳定优势包括：

- 与文本天然顺序一致；
- 输出 append-only，适合 streaming；
- 历史 KV 可缓存；
- 每步概率和停止条件清楚；
- target model 直接拥有最终分布。

代价是 serial depth 至少与输出长度相关。即使每步 matrix operation 高度并行，下一个 token 仍等待前一个 token 确定。图像或视频使用 raster-order AR 时，这种任意顺序还可能让局部相关性被迫经过很长路径。

减少这段 serial depth 的一条分支，是把每步的条件目标从单 token 改成一个 `p×p` patch 的联合分布：跨 patch 仍按 raster-order AR，并以 block-causal mask 组织条件，但 patch 内不再把各 token 当作独立分类抽样。一个 conditional diffusion/flow head 在同一 patch 的 binary-token 空间联合迭代，学习组内依赖；binary bit 的组合数不等实际可用容量，学得的 head 也不认证精确联合采样。[受限 next-patch 对照](https://arxiv.org/pdf/2602.14041v1)支持这条 factorization/预测接口，而非只凭增加并行宽度消除依赖。它用 head 迭代、额外训练与块内计算换更少的外层 AR steps；更大 patch 的吞吐改善可以伴 FID 退步，外 family 的 backbone 或训练不同也不能唯一归因该机制。局部一致性、head 质量或完整费用不满足目标时，应缩小 patch 或保留普通单-token AR，而不是把并行提交直接当作无损加速。<!-- source-family:SF-2026-ARXIV-2602-14041 -->

第 23 章给出了表示的重构和语义契约，本章还必须问一个不同的问题：**这种表示是否容易被当前生成路径逐步预测？**
视觉 encoder 的高维连续 latent 即使能重构图像，单个 latent token 的分布仍可能比低维 VAE latent 难建模。
在 teacher forcing 下，AR 看到真实历史；生成时却要以自己的连续预测作下一步条件，高维误差会随步骤进入后续条件。
因此，重构分数不能替代生成质量、误差滚动或推理成本的验收。

一种受限分支先校准 token 分布，再在训练时扰动真实历史，让预测器练习接住偏离数据流形的前缀；它以更复杂的
表示归一化和训练噪声换生成容错，却不能靠更低训练损失证明最终图像更好。若扰动不匹配真实 rollout、
生成质量仍落后或稳定性优先，沿用重构导向 VAE 仍是合理选择。[RAE-AR 的图像实验](https://arxiv.org/html/2604.01545v1)
只支持所测 encoder、AR 架构、训练设置与指标下的这条表示—生成张力；其消融中归一化单独使用并非总有益，
结果也不证明高维语义 latent 已普遍追平 VAE。<!-- source-family:SF-2026-ARXIV-2604-01545 -->

当 AR 的一步变为预测下一尺度的视觉码时，历史扰动训练还取决于 decoder 实际读取什么。可以扰动已有尺度的 code indices，要求恢复原 top-1 目标；但旧 VAR 的 accumulated-feature 输入不必与统一 decoder 的这项 self-correction 目标兼容。受限对照中该组合退步，直接 residual/code-index 输入则改善，作者把 feature complexity 作为解释假说，而非已识别的唯一原因。因此 tokenizer/codebook、尺度历史、输入表示、扰动及目标必须与 decoder 分别冻结和配对验收，不能由某种 codec 易重构就推断修正训练一定有效。它支付额外训练和输入适配成本；质量或兼容性不足时，保留原 scale-history 输入、普通 teacher forcing 或重新训练，而不授离散码普遍优越。可选的 diffusion refiner 是另一消费分支，可能改局部结构或身份并另付采样成本；理论 FLOPs 比例不能代替同质量的端到端墙钟。<!-- source-family:SF-2026-ARXIV-2601-02204 -->
