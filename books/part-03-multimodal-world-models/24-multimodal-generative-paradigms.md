# 第24章 多模态生成范式

**Knowledge Tree:** Part III 多模态、生成与世界模型：从跨模态表示到物理行动
**Stable Knowledge Node ID:** `MULTIMODAL-GENERATIVE-PARADIGMS`
**Legacy Chapter:** N/A
**Status:** Draft

**Roadmap Intent:** 从概率分解与状态提交出发，比较 Autoregressive、Diffusion、Masked/Block Diffusion 与混合 proposal-correction，而不是用单项 benchmark 宣布范式替代。

## 本章要回答的问题

为什么文本生成长期以 Autoregressive 为主，而图像和视频大量采用 Diffusion？Masked Diffusion 为什么能并行生成多个 token，却带来 mutable output、cache invalidation 和 streaming 难题？Block Diffusion、draft tree 和 correction loop 是同一条路线吗？

本章的核心判断是：**生成范式的差别首先是概率分解、状态可变性与 commit protocol 的差别，随后才表现为 kernel、cache 和 latency 差别。**“一次生成更多 token”不自动等于更快；“允许修正”也不自动等于更准。必须把 proposal work、verification/correction、memory、并发和输出提交一起计算。

## 从一个共同问题开始

给定条件 `c`，系统要从分布 `p(x | c)` 产生样本。不同范式选择不同的计算路径。

Autoregressive factorization：

```text
p(x | c) = Π_t p(x_t | x_<t, c)
```

Diffusion 或 masked generation 则定义一系列从噪声或未知状态到数据的 transition：

```text
x_T -> x_{T-1} -> ... -> x_0
```

两者都可能使用 Transformer，也都可能生成文本、图像或视频。真正不同的是：每步条件是什么，哪些位置可以并行改变，何时把中间状态视为最终输出。

## 为什么 Autoregressive 是合理起点

AR 将复杂联合分布拆成条件概率乘积。训练可以 teacher forcing，并行计算所有位置的 loss；推理必须依次确定 token。它的稳定优势包括：

- 与文本天然顺序一致；
- 输出 append-only，适合 streaming；
- 历史 KV 可缓存；
- 每步概率和停止条件清楚；
- target model 直接拥有最终分布。

代价是 serial depth 至少与输出长度相关。即使每步 matrix operation 高度并行，下一个 token 仍等待前一个 token 确定。图像或视频使用 raster-order AR 时，这种任意顺序还可能让局部相关性被迫经过很长路径。

### 视频 AR 可以分离帧内精确路由与跨帧记忆

对视频把所有历史 token 放进同一个 softmax，最忠实但跨帧成本随序列迅速增长；只保留压缩 recurrent state 又可能丢失当前帧细节。一个分层分支让帧内 token 继续使用 exact local softmax，同时以 linear recurrent memory 承载跨帧历史。关键的状态边界是：同一帧的所有 token 都读取相同的 pre-update memory，只有 clean forward 完成后才提交下一帧 state；否则帧内并行会被隐式执行顺序污染。

这条路径以更低跨帧成本换 memory drift、历史细节损失和新的 clean-pass commit 纪律。长程一致性不足、状态异常或任务依赖精细历史时，应回退 full attention、短窗口重算或两者混合。现有证据只支持作者的视频模型与受测数据，不证明 linear memory 能替代任意视频历史，也不授权 runtime 偷改帧边界。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-16579:start -->
视频自回归可以让帧内 softmax 保持精确，而把跨帧历史演进成在 clean pass 后提交的 recurrent memory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-16579:end -->

## Diffusion：用迭代修正换并行状态更新

连续 diffusion 从噪声逐步 denoise；离散或 masked diffusion 从 mask/noise state 逐步恢复 token。每轮可以同时更新许多位置，因此 serial steps 不必等于 token 数。

它的优势不是“完全并行”，而是把串行维度从 output length 改成 denoising/refinement steps。代价包括：

- 多轮 full or block forward；
- 中间状态可变，cache reuse 更困难；
- streaming 前必须定义哪些 token 已 committed；
- 迭代 schedule 会影响质量、延迟和稳定性；
- likelihood、sampling exactness 和 stop condition 可能更复杂。

图像和视频往往容忍整体画面同时从粗到细修正，且用户不要求逐像素 streaming，因此 diffusion 的系统契约较自然。文本要求稳定前缀和低延迟流式输出，mutable tokens 的成本更明显。

非自回归文本生成也不必只在离散 token 上做 observation denoising。分层连续 latent diffusion 先由 Text VAE 建立稳定 text↔latent artifact，再由 block-causal DiT transport global semantic prior，最后由 conditional decoder 完成 local token realization；这把 global organization 与 surface realization 分成两个可独立失败的状态。收益是语义压缩与跨连续模态路线，代价是 VAE information loss、两阶段训练/版本耦合和额外 decoder；重构或 scaling gate 失败时回退 token AR/离散 diffusion。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07933:start -->
把 Text VAE、latent diffusion 和 token decoder 分阶段冻结训练最容易定位失败；端到端 joint training 能让表示与生成共同适配，却也可能让 encoder 缩放、diffusion loss 和 decoder reconstruction 相互追逐而 collapse。训练 artifact 应保存 encoder/diffusion/decoder revisions、diffusion-to-encoder warmup、decoder noise、loss weights 与 time sampling，并分别验收 reconstruction、latent smoothness、PPL/diversity 和 NFE。任一阶段不稳时回退 staged freeze、离散 diffusion 或 AR，不能用单一生成分数掩盖表示塌缩。 [受限证据：arXiv:2605.07933v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07933:end -->

证据覆盖 8 个 benchmark、严格匹配的约 2B AR/LLaDA baselines 与至约 2000 EFLOPs scaling；不证明更大规模、真实 serving latency、质量等价或统一多模态能力。MULTIMODAL-REPRESENTATION 提供 latent identity；本章拥有 generation factorization。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06548 -->

从成熟 AR checkpoint 转向 masked diffusion 时，表示能力与生成顺序不必同时从零学习。一个受限迁移路径冻结 AR teacher，用逐层 representation alignment 保留已有表示几何，同时让 student 通过 masked-denoising objective 重学可修订的 generation path。teacher 只拥有表示目标，diffusion objective 与 sampler 拥有新路径；表示接近不能授予行为等价或输出提交权。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06885 -->

这条路径以 teacher compute、同构架构耦合和 alignment/objective 冲突换较低的数据重学成本。架构不同、表示失配或质量 Gate 失败时，应回退普通 diffusion continued training 或保留 AR。exact-v1 只覆盖同构 Qwen3 0.6B/1.7B/4B、作者代码任务和 0.8B/50B 数据条件，不证明跨架构迁移或 diffusion 普遍替代 AR。

### Timestep Embedding 也是可写入的控制通道

Diffusion scheduler 通常把 timestep 当成公开、无害的去噪坐标；若该 embedding 可被外部组件替换或调制，
它也能成为绕过普通内容输入的隐蔽信息通道。控制面因此必须把 scheduler、timestep encoder 与其参数
纳入 artifact identity，限制可写主体，并在 provenance/audit 中记录实际 embedding 路径。这个边界可以
同时用于防止隐蔽注入与声明生成来源，却增加签名、兼容与运行时校验成本；封闭、固定 scheduler 的离线
pipeline 仍可保持简单配置。现有证明与实验只说明受测 diffusion 架构存在该通道，不证明任意模型都可
可靠隐藏或检测信息。
<!-- source-family:SF-2026-ARXIV-2605-00935 -->

### Continuous 与 Discrete Flow 的等价是有条件的

把 continuous flow 与 categorical discrete flow 分开设计，在通常情况下是合理的：前者在连续状态中学习 velocity field，后者直接规定 token state 的转移与提交。但在一组严格条件下，两者可以建立可检查的接口。若 target 是 one-hot categorical state，source 按位置乘积分解且对坐标置换对称，不在 tie 或 threshold 上分配概率质量；同时 lifted coupling 与 position-wise argmax 兼容，并满足给定初始类别后的条件独立，那么 continuous convex interpolation 经 argmax 投影，会诱导出 discrete convex-interpolant conditional path。

这条 duality 的关键并不是“连续与离散本来相同”，而是揭示了 **source geometry 会改变 categorical transition 的有效时间**。连续 source 中任意两个坐标的 gap distribution 决定离散路径的 effective coefficient：Gaussian source 的类别切换会随 vocabulary 增大而延后，bounded uniform source 的时间尺度由 support width 控制，而 centered negative-exponential source 的对应表达式不显式依赖 vocabulary size。于是 source law 不再只是采样实现细节；它必须与 coupling、schedule、vocabulary 和训练 revision 一同成为 generation artifact，schedule calibration 也必须针对这组 identity 完成。

状态与控制权仍需分清。source、coupling 与 schedule 拥有“何时跨过类别边界”的条件路径；learned vector field 拥有实际 transport；sampler 与 runtime 拥有数值求解、token revision 和 commit。数学上的 path equivalence 不允许 runtime 把未校准的 source 替换成另一个 source，也不证明两个 learned marginal dynamics 会自然一致。破坏乘积分解、置换对称、无 tie、argmax-compatible lift 或 coefficient matching 中任一条件，定理就不能继续充当接口保证；bounded source 还可能在 continuous endpoint 之前使 discrete coefficient 饱和，迫使 velocity 的有效区间重新限定。

因此，采用新 source 或 schedule 的收益是可以显式控制类别转移 timing，代价是增加 source/coupling/schedule 的版本耦合、重新训练或校准以及 sampler compatibility 验证。已经围绕 Gaussian source 或既有 schedule 训练并验收的模型仍应保留原路径；不满足上述假设、需要 mask-source 语义，或无法证明替换后 vector field 与 commit 行为兼容时，也应回退原 source 与 schedule。现有证据给出了条件定理和证明，但经验部分只有 OpenWebText 上 10K-step 的 single run 与小型 toy trajectory；它不证明某种 source 的生成质量普遍更高，也不证明训练稳定性、吞吐或 serving SLO 获益。

<!-- source-family:SF-2026-ARXIV-2609-10863 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11311:start -->
Source identity 不只约束单个样本的 marginal，也约束一批样本怎样共同覆盖可能结果。Independent Gaussian seeds 在单图生成和故障隔离时最简单；若目标是让同一 prompt 的 gallery 在保持每张图 `N(0,I)` marginal 不变的同时扩大相互差异，可以显式设计 batch-level joint noise coupling。Coupling owner 只决定初始样本间的相关结构，denoiser 与 sampler 仍拥有单样本生成路径，gallery evaluator 才判断 diversity 是否值得采用。

联合 coupling 用批间依赖、额外采样状态和校准成本换多样性控制，也会降低复现与 failure isolation。当前证据只覆盖 SD1.5、SDXL、SD3、2,000 个 COCO prompts、三图 gallery 和作者指标，不证明其他 sampler、gallery size 或生产 SLO。单图、强复现、独立故障边界或 coupling 未校准时，应回退 independent seeds。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11311:end -->

## Masked generation：未知位置与已知位置

masked model 维护部分可见序列：

```text
known tokens + [MASK] positions
```

每轮对多个 mask 产生预测，再按 confidence 或 schedule 提交一部分。保守 schedule 一次只接纳少量高置信 token，质量更稳但并行收益有限；激进 schedule 接纳更多 token，早期错误会成为后续条件。

这解释了一个关键演进：

```text
只填充未知位置
→ 高并行填充暴露误差累积
→ 允许重写已生成 token
→ 显式训练 proposal + correction
```

后一步没有否定保守 unmask。它用更多训练与推理 work、mutable state 和提交复杂度换取更激进的并行 operating point。

### 局部条件重采样可以复用预训练语言分布

从均匀 corruption 重新训练 masked diffusion，能够让训练目标与多轮修正完全对齐，但会放弃成熟 causal 或 masked LM 已经学到的条件分布。另一条受限分支把单位置 mask-infilling 看成局部 transition：每一步固定其余 token，只重新采样一个或一组位置；预训练 LM 提供条件分布或 energy proxy，Glauber-style sampler 通过反复局部 revision 逼近由这些条件共同定义的序列分布。<!-- semantic-body-binding:SF-2026-ARXIV-2605-04291 -->

这里改变的是 generation path，而不是凭空获得新的语言真值。模型只拥有局部 proposal，sampler 拥有位置选择、transition schedule 与 provisional state，runtime 仍拥有停止与外部 commit。复用已有权重可降低从零学习条件分布的门槛，却把成本移到更多 NFE、混合时间、mutable cache 和收敛诊断；有限步输出不等于已经到达 stationary distribution。受限证据还包含显著训练算力，未覆盖 streaming 与生产端到端 SLO。低延迟、append-only 或无法验证混合质量时，causal AR 仍是更可靠的回退路径。

### AR 权重可以成为 Masked Diffusion 的兼容起点

从零训练 masked language model，attention pattern 与初始化都为双向修正服务，接口清楚但无法复用成熟 AR checkpoint；直接把整段序列改成双向可见，又会让 observed prompt 变成可修改状态并破坏 causal condition。兼容分支可以保留 prompt 内的 causal attention，只让 masked target 内部双向交互：prompt 仍是冻结条件，target 才拥有 provisional、可反复修正的 token state。

```text
observed prompt: causal and immutable
masked target: bidirectional and revisable
→ iterative target refinement
→ declared target commit
```

这使 AR initialization 能迁移到 diffusion training，但代价是 attention mask 的训练—推理差异、多轮 forward 与 target cache 的可变性。受限的 matched GPT-2 Medium/WikiText 实验只说明它优于对应 diffusion baseline；同规模 fine-tuned AR 仍更强，超过 512 tokens 与远域迁移还会退化。因此它是 AR→masked diffusion 的兼容桥，而不是 diffusion 已取代 AR 的证据。长文本、严格 streaming 或域外稳定性优先时，应回退 causal AR；只有 target revision 的质量与端到端成本都重新验收后才采用该分支。

<!-- source-family:SF-2026-ARXIV-2607-25157 -->

### Equilibrium Layer 把深度从训练图移到推理求解状态

视觉 AR 堆叠固定层数时，训练 activation memory 与推理计算深度一起增长；隐式 equilibrium layer
把重复变换表达为固定点，只保存求解所需状态，并允许部署时选择迭代预算。它获得训练内存与推理
深度的部分解耦，却把代价转移到固定点收敛、implicit differentiation、停止阈值与每个样本不同的
迭代次数。求解不收敛、延迟尾部不可接受或硬件更适合静态图时，应回退固定深度网络。作者视觉任务
结果只支持披露模型与求解器，不能证明 equilibrium 结构普遍改善视觉 AR 质量或生产吞吐。
<!-- source-family:SF-2026-ARXIV-2605-01220 -->

## Editable tokens 与 commit boundary

“并行解码”不能由模型名称或一次 forward 更新的位置数推断。对 masked diffusion LM，应从 sampler 的实际 accept events 重建 token 何时进入不可再改状态；同一步若同时接受多个位置，这些 token 之间可能只有 block-level 偏序，而不存在可解释的逐 token 生成顺序。于是 sampler revision、accept rule、commit granularity 与可见输出顺序都属于 generation artifact；把观测 block size 当成模型固有因果顺序，会给缓存、流式输出和审计制造虚假依赖。

这种追踪增加事件记录和分析成本，且单一 checkpoint、sampler 与有限任务上的 commit 行为不能代表整个 diffusion family。若下游严格依赖全序、输出具有不可逆副作用或 sampler 无法暴露 accept event，应延迟外部提交或回退自回归路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14620 -->

### 并行与少步生成必须声明依赖、轨迹和状态边界

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:start -->
固定数量地同时提交 masked positions，默认这些变量之间的依赖足够弱；这在规则任务中简单，却会把强相关位置
过早冻结。一个受限分支从 hidden states 一次估计 pairwise conditional mutual information，构造依赖图，再只
并行提交相互影响较小的变量。它用额外估计器和图调度换取更有依据的并行度，但 MI 误差、图阈值和未建模高阶
依赖会造成错误 commit。Sudoku 与蛋白任务只证明作者设置；依赖估计或一致性检查失败时，应回退更小 block、
更多 refinement step 或逐位置提交。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20187:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20199:start -->
连续 diffusion language model 的弯曲轨迹需要较多 function evaluations；flow-matching 微调可以把现有路径拉直，
让 sampler 用更少步接近同一终点。这里改变的是 trajectory geometry 和 solver budget，不是免费减少计算：额外
训练、直线路径的近似误差与任务分布漂移都要计入。比较必须同时冻结训练预算、NFE、解码器和质量指标；作者的
question generation、simplification 与 paraphrase 结果不支持通用文本生成。少步质量退化时应回退原 solver 或
增加 NFE。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20199:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20235:start -->
score singularity 提供另一种两阶段解释：先沿强法向分量把高维样本压向低维 manifold，再沿流形细化密度；在
给定正则与几何假设下，样本复杂度可以由 intrinsic dimension 而不是 ambient dimension 主导。收益是把生成难度
拆成 reach-manifold 与 model-on-manifold，代价是奇异 score、数值刚性和 manifold 假设都进入 solver contract。
Stacked-MNIST、CelebA 变体与分子实验不能证明真实多模态分布满足这些假设；假设或积分稳定性不成立时，应回退
常规 score model、显式正则与经验 solver validation。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20235:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20547:start -->
当目标从静态 marginal 扩展到 time-dependent latent process，训练对象还要声明“匹配哪个状态转移”。
Generator matching 通过 pushforward generator 定义 conditional objective，并在给定 regularity 条件下证明它与
marginal objective 具有相同参数梯度。它提供的是目标等价的理论接口，不是生产实现或任意过程的稳定性保证；
正则条件、链式 rotational generator 或数值实现无法验证时，应回退已知的固定端点 flow/diffusion objective。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20547:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20946:start -->
语音生成还可把 speech token 与内部 reasoning token 交错到同一训练序列，使模型在发声单元之间保留可学习的
中间状态。它改变 token type、时间戳、可见性和 commit cadence，却不证明内部 reasoning 等于事实正确或可解释
因果；隐藏 token 泄漏、音频延迟和状态错位会成为新失败面。作者任务与模型之外，应保留不暴露中间状态的普通
speech generation，并让外部 verifier 而非 reasoning token 拥有正确性判断。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20946:end -->

### Self-revision：并行位置必须在 Commit 前保持可撤销

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25820:start -->
并行解码若只按单 token confidence 选择同一步提交位置，可能把视觉上指向同一区域的冗余 token 一起锁死。一个多模态分支用 token-image attention overlap 构造 Visual Redundancy Index，再优先提交 grounding 互补的位置。这个指标只拥有 selection proposal：attention overlap 不是因果 grounding，也不能证明 token 语义正确。

读取 attention 与组合选择会增加 runtime 和调度开销，信号失配还可能漏掉文本依赖或把关键同区域 token 误判为冗余。此时应回退 confidence top-k、减小并行 K、允许重开，或使用顺序 AR/完整迭代。作者 backbone 与任务范围只支持这一选择策略，不证明它对所有多模态生成都更快或更准。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25820:end -->

#### 用跨步分布不稳定性分配 Revision Budget

每一步重算所有未提交 token 最容易保持算法对称，却把相同计算花在已经稳定和仍剧烈变化的位置。一个选择性分支比较相邻 denoising step 的 top-K 分布，只重新开放高动态 token，并通过自对比重掩码把计算集中到不稳定区域。Sampler 拥有 refresh proposal，commit policy 仍决定哪些位置不可再改。

Top-K 差异只是稳定性代理，可能漏掉排序不变但概率显著漂移的错误，也会引入阈值和额外状态。短序列、并行硬件充足或 exact trajectory 更重要时，全量 revision 仍是可靠基线；现有 exact-v1 结果只支持作者模型、步数与数据集。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01373 -->

普通 masked diffusion 把位置从 mask 变成 token 后往往视为已解码；早期错误随后只能被其他位置条件化放大。
让已预测位置继续以 confidence-weighted token/mask 表示参与后续 denoising，可形成 provisional state，直到 block
稳定或达到阈值才 commit：

```text
self-generated noisy state
→ parallel provisional tokens + confidence
→ repeated revision
→ convergence / threshold gate
→ block commit
```

Runtime trick 不足以保证模型会修正自己的错误；training distribution 必须包含 self-generated noise。它新增
threshold calibration、oscillation、block 内最慢请求 barrier、KV/graph invalidation 和 stream rollback。标准 AR
在 exact left-to-right commit、低并发或模型未匹配 revision training 时仍然合理。DMax 是 Experimental 分支，
其 batch-1 双卡结果不能写成 serving goodput。

### 生成 Workflow 也可以被训练进 Intermediate State

复杂视觉生成可以从 one-shot prompt→image 演进为 plan→draft→inspect→refine；若 intermediate scene graph、
text plan、draft 与 correction 都进入训练对象，模型学习的是显式 workflow state，而不只是最终像素。它可能提高
约束可诊断性，却引入 plan/pixel inconsistency、self-critic correlation、更多生成步与错误 verbalization。
简单 prompt、强基础 generator 或 latency-sensitive workload 仍应 one-shot。Think in Strokes 的作者结果只支持
其 scene-graph/data contract，不证明 verbal plan 等于可解释因果或跨 modality 通用。

若生成器可以把 token 从 A 改成 B，runtime 必须区分：

```text
provisional state  模型仍可修改
committed output    已对用户、工具或下游产生承诺
```

还要把“持久条件副本”与这两者分开：一种迭代生成分支会保存选中的 clean-token 假设并持续覆盖后续 denoiser 输入，但底层 noisy state 仍可变化，最终输出也重新读出，而不是直接复制该假设。它用较稳定的上下文协调并行位置，代价是错误假设持续影响后续步骤；条件保留时间、底层可修改状态与外部输出提交必须分别定义，不能因算法称其为 commitment 就提前向用户承诺。

在 UI 内部重绘一幅图通常安全；已流式发送的文本、已触发的 tool call 或已执行的 robot action 无法简单改写。于是模型机制会向系统传播：

- token revision 是否需要 retract protocol；
- radix/KV cache 怎样 invalidation；
- stop sequence 在 provisional state 中是否生效；
- request cancellation 如何清理多轮状态；
- batching 时不同 correction cadence 如何保持公平。

因此可编辑生成不是 Decoder 的一个小优化，而是新的 state machine。

实时多模态生成还可能把统一模型拆成 state-preserving deployment pipeline，而不是重新拆回互不相干的模型。
一个 thinker 保留 encoder、language/environment update、decoder 与 authoritative KV slices，performer 只执行下一
audio/video latent 的 flow solver；两者交换同一历史状态与上一生成单元，以一拍流水重叠理解和生成：

```text
multimodal observation and shared causal state
→ thinker updates semantic/world/KV state
→ performer generates next media latent
→ timestamped handoff and backpressure
→ commit visible unit or recover both sides
```

这条路线改变的是 deployment ownership，不证明模块化 pipeline 已过时。Overlap 可降低受限系统中的 model-side
latency，却新增 KV/version consistency、跨模态时钟、双侧 partial failure、backpressure 与 rolling error。Wan-
Streamer 只为其作者模型与未完整披露硬件合同提供实验性证据；低流量、严格单步一致性或不能容忍跨 stage
恢复复杂度时，串行统一模型或独立模块仍合理。

## Block Diffusion：局部自回归与块内并行

Block Diffusion 把序列分成 blocks。block 之间保持 causal order，block 内用 masked/refinement steps 并行生成：

```text
block_1 -> block_2 -> ...
within block_k: iterative parallel refinement
```

它试图在两种范式之间取 Pareto 点：保留 block-level prefix/cache 和部分 streaming，同时减少 token-level serial steps。新的 trade-off 是 block size：

- 小 block 接近 AR，cache 和 commit 简单，并行收益小；
- 大 block 并行机会更多，但 correction、verification、memory 和首块延迟增加。

固定 block size 只是策略之一。工作负载变化时，最优 size 可能依赖 entropy、prompt、硬件、batch 和 SLO。

### Block Boundary 也可以成为受约束的生成状态

固定 block 在静态 shape kernel、短输出和低调度复杂度优先时仍是稳健基线；不同语义步骤长度差异很大时，同一 block size 会让简单段过度迭代、复杂段过早 commit。一个 learned-boundary 分支允许 decoder 提出可验证的 block-end，runtime 冻结 boundary 与 policy revision 后再提交；训练可以用 entropy trajectory 做辅助 shaping，但任务 outcome 或独立 verifier 仍拥有正确性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02263 -->

动态边界用更贴合语义步骤的并行度换 variable-length scheduling、cache/rollback 复杂度、reward hacking 与错误自信。边际 entropy 下降既不等于推理正确，也不等于步骤结束；未校准、开放生成或部署并发使收益不稳定时，应回退固定 block。exact-v1 只支持作者 reasoning benchmark 与后训练设置，不能证明动态 block 在所有 workload 更快。

## Draft、Verify 与 Correct 不是同一件事

### 跨分辨率 Draft 需要显式 Semantic Lock

图像或视频始终在高分辨率状态上迭代，最容易保持统一语义，却会把大量计算浪费在已经稳定的区域。另一条分支先生成低分辨率 draft，由独立验证器标记语义稳定区域并冻结 semantic lock，只对未锁定区域恢复高分辨率 state 继续计算。低分辨率状态拥有 proposal，不拥有最终像素真值；lock 必须绑定尺度、区域、验证器和可重开条件。

这用验证和跨尺度映射成本换 selective compute，也可能把早期错误锁死或在边界产生不连续。细节密集、全局结构持续变化或验证器不可靠时，应回退全分辨率迭代或允许全局 rollback。现有 exact-v1 只证明作者 workload 下的质量/计算权衡。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02152 -->

### Draft + exact verification

speculative decoding 允许便宜 drafter 提议 token，再由 target 验证。若 acceptance rule 正确，可以保持 target distribution。它的目标是减少昂贵 target serial steps，不改变 target 的输出语义。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-14305:start -->
对 masked diffusion，target distribution 本身也必须先定义清楚：若同一 corrupted input 上的 clean positions 被独立预测，
posterior factorization error 会让并行位置组合成不一致结果；prefix-conditioned clean-token factorization 改变的是 target
distribution construction。其上的 speculative verifier 只负责更快地采样并保持该 target，不能把“目标如何分解”和“目标如何
加速”合并为一个 correctness owner。prefix 依赖增加串行性和实现复杂度；收益不稳定或 verifier contract 不完整时，应回退
普通 DLLM target、较小 block 或完整 target sampling。exact-v1 只支持作者 Method 与实验，不证明所有 DLLM 都需要同一分解。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-14305:end -->

### Correction

correction 允许同一模型或 corrector 修改已经可见的 provisional tokens。它可能改善质量，但不天然保持某个 AR target distribution，也可能振荡或破坏正确 token。

### Diffusion Bridge 可以替换局部层，但不能冒充独立语言模型

<!-- semantic-body-binding:SF-2026-ARXIV-2605-14368:start -->
直接把完整 Transformer 改成 diffusion LM 会同时改变表示、生成目标与 runtime，难以判断收益来自哪里。一个受限分支先用
geometry proxy 选择 diffusion-friendly hidden interface，再以 conditional diffusion bridge 替换 lower layers；保留的
suffix 与 LM head 继续负责 token recovery。bridge 拥有中间表示 proposal，不拥有最终语言分布。它减少重建范围，却增加
bridge size/depth/compute 与 suffix coupling；几何 proxy 失配、接口漂移或恢复质量下降时，应回退原 Transformer 或更浅
replacement。exact-v1 的结果不证明 standalone diffusion LM，也不支持跨 backbone 无损替换。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-14368:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09603:start -->
普通 masked diffusion 只把尚未决定的位置从 mask 变成 token，因而一旦早期错误被 unmask，后续步骤通常只能在其周围继续填充。显式 edit state 把这条不可逆路径改成“并行 proposal → insertion/deletion/replacement proposal → refinement 验证 → commit”：corrector 可以重开已经可见的位置，但 runtime 仍拥有版本、预算和最终提交权。

可撤销修正提高了错误恢复能力，却增加训练目标、编辑步骤、状态对齐和不收敛风险；它也不自动保持某个自回归 target distribution。现有结果只支持作者披露的语言模型、任务和 evaluator，不能外推为所有 diffusion LM 的质量保证。编辑振荡、延迟预算紧或 exactness 要求高时，应回退保守 mask schedule、限制 revision 次数，或直接使用 AR。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09603:end -->

### Tree proposal

一次 draft pass 可以产生多个未来位置的 marginals，并据此构造 candidate tree。target 用 tree attention 一次验证多条前缀。这里需要区分 draft surrogate probability 与 target path probability；前者适合分配 node budget，不等于后者。

三者可以组合，却拥有不同 correctness contract：

```text
draft owns proposal breadth
target owns accept/reject semantics
corrector owns mutable refinement
runtime owns commit, rollback and KV compaction
```

### Diffusion Constrained Decoding 必须验证“仍可完成”，而不只是当前合法

自回归生成每次只提交下一个 token，因此 grammar-constrained decoding 可以从当前 parser state 枚举合法后继；
masked diffusion 同时为多个位置提出分布，若只检查刚填入的 token 是否局部合法，provisional sequence 仍可能进入
再也无法补全为合法句子的死状态。约束变化后，admission 需要从“当前 token 合法”推进为“加入该 token 后，剩余
mask 仍存在至少一条可完成路径”。

一种受限分支是在每轮 proposal 时利用所有位置的并行分布做 lookahead：diffusion model 只拥有候选概率，grammar
automaton 拥有语言状态与可达性，verifier 决定 proposal 是否保留，runtime 仍独占最终 commit。这样保留了并行
proposal，却新增 lookahead search、grammar 编译、长度/终止状态和 mask ordering；grammar 复杂、可达性检查昂贵
或目标不是形式语言时，延后到完整 block 验证或使用自回归 constrained decoding 仍更简单。exact-v1 只在四个
dLLM 与三个 benchmark 上支持 syntactic-completability 机制，不证明语义正确、任意 CFG 的成本或生产尾延迟。

<!-- source-family:SF-2026-ARXIV-2602-00612 -->

## 从 Specialist Head 到 Typed Unified Generation

分类、检测、分割、深度与多视角几何传统上各自使用专用 head、loss 和 decoder。这一结构在单任务、固定输出
shape 与严格延迟下仍最强：类型约束直接写在 architecture 中，非法输出空间较小。但能力数增多后，每个新任务
都带来独立训练、部署和评估接口，跨任务知识也难以共享。

统一生成不是简单把所有 target 转成字符串，而是把类型边界从专用 head 移到 versioned sample contract：

```text
visual inputs
+ task and output-schema instruction
→ native text / image / mixed provisional response
→ deterministic typed decoder
→ boxes | masks | dense maps | camera records
→ task-specific invariant and evaluator
```

生成模型拥有 provisional response，schema/parser 拥有从 token 或 image record 到 typed object 的 commit，
下游 evaluator 仍按任务语义判定 correctness。共享 generator 因而可以复用 representation 与训练数据，但不会
消除 modality-specific codec、coordinate frame、mask topology 或 camera convention。reserved token、parser 与
annotation conversion revision 必须进入 artifact identity；否则同一 checkpoint 在不同 decoder 下会产生不同
系统行为。

这条路线用接口复用和 cross-task transfer 换来 parser/schema drift、invalid output、coordinate quantization、
pseudo-label provenance 和 capability interference。专用 head 在硬实时、强校准 dense output 或安全关键几何中
仍然合理；统一生成适合任务族持续扩展且 typed decoder 可严格验证的场景。作者跨多个视觉任务的结果只支持
其转换数据与 evaluator 合同，不证明一种 response representation 对所有视觉 workload 都最优。

### Any-to-any AR 把 Modality Type 移入同一生成序列

Typed unified generation 仍可保留不同任务的输出 decoder；更进一步的 any-to-any AR 分支把每种模态都编码为 decoder-only sequence，使图像、文本、音频或其他离散表示既可成为条件，也可成为下一段输出，而不为每个方向增加独立 head 和 loss。Checkpoint 拥有 modality tokenizer/codec、type delimiter、sequence order 与共享 decoder；runtime 拥有 typed segment 的状态和提交边界，下游 decoder 仍验证每种输出的可解释格式。

共享 factorization 减少任务接口分裂，并允许 chained generation 把一种模态的 provisional output 再作为另一模态的条件；但这不是独立 self-verification，因为两次生成共享权重、输入和误差。统一参数会引入 modality interference，长媒体 token 也会放大序列成本、KV residency 与调度不公平。某一模态需要强校准专用 head、codec 失配或共享训练造成负迁移时，应保留 specialist model/head；现有 exact-v1 只支持作者任务中的 specialist/multitask 对比与 chained generation，不证明所有模态共享表示或损失最优。

<!-- source-family:SF-2026-ARXIV-2607-25948 -->

### 理解能力可以监督生成表示，但不能兼任生成真值

共享生成器减少任务接口分裂，却不保证 noised generative representation 保留了理解任务需要的语义。一个有条件的
训练分支冻结已有 understanding expert，让它从生成路径的中间表示重述 caption 或回归视觉特征，使理解目标的梯度
进入 generator；semantic re-caption、prompt masking 与 metaquery 则用于减少目标 token 泄漏和简单复制条件。
这里 frozen expert 只拥有 gradient proposal，最终生成质量仍由与其独立的任务 evaluator 判定。

这种 layering 用既有理解先验换更强的语义约束，也会把 captioner 或 visual encoder 的偏差蒸馏进生成器，并可能与
像素细节目标发生梯度冲突。现有证据限于 BAGEL-7B、5K iterations 以及作者的图像生成/编辑数据与 judge；PCA
可视化不构成因果证明，也没有覆盖视频、音频或生产 serving。理解先验失配、发生 supervision leakage 或 specialist
质量更稳定时，应回退 generation-only objective、独立理解/生成模型或更窄的辅助损失。

<!-- source-family:SF-2026-ARXIV-2605-05781 -->

### Discrete Causal State 与 Continuous Flow State 可以交错，但不能混成一个身份

Any-to-any AR 把模态都放进同一离散序列，接口最统一，也便于沿 causal order 复用语言推理状态；它的代价是连续视觉变换必须先离散化，媒体 token 又会拉长 generation path。另一条条件分支不是把 VLM 与 flow 串成两个互不相知的模型，而是在层间交错两种状态：causal language stream 保留离散条件和推理顺序，invertible flow stream 维护连续视觉变换，crossing skip connection 只负责交换表示。

这种结构减少两阶段 pipeline 的语义断点，却把 checkpoint identity 扩展为 `shared causal mask + flow depth + vertical connection + staged-training revision`；任一侧升级都会改变联合目标、跨流 cache 与生成状态，不能只复用另一个 stream 的验收结果。共享表示还会引入 modality interference 与训练阶段耦合。理解或生成任务不需要共享状态、两侧校准失败，或升级后无法重做联合验收时，专用模型和显式两阶段 pipeline 仍是更稳健的回退。

[受限证据](https://arxiv.org/html/2605.08029v1)只支持作者架构、分阶段训练与所测理解/生成基准；统一 NLL 不证明所有任务共享 backbone 最优，也不提供生产 serving latency、跨流 cache invalidation 或故障恢复结论。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08029 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20316:start -->
从头联合训练不是获得双向生成的唯一入口。已有 text-to-image checkpoint 在 image prior 值得保留、数据与算力受限时，
可以冻结 text encoder，只用 LoRA 与新增 text heads 把 `image time` 和 `text time` 分开；text→image、image→text、
joint generation 与 partial-text completion 由此成为同一二维时间状态空间里的不同轨迹，而不是把两种状态压成一个
timestep。Checkpoint identity 也随之扩展为 base revision、LoRA、text head、双时间 schedule 与 token insertion
规则。

薄适配降低训练成本，却把两条时间轴、跨模态接口和 schedule compatibility 变成新的故障面；小数据也不足以补齐
外部知识与复杂 VQA。分辨率、数据或 text task 越出验证域时，应回退单向生成器配独立 caption/VQA 模型，或进行
完整 multimodal pretraining。现有 evidence 只支持 exact-v1 的 matched-LoRA、有限 SD3/FLUX 与 joint/VQA 设置，
不证明这种迁移合同可替代大规模统一训练。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20316:end -->

### Exploration 是训练计算轴，不是新的生成真值

单一监督 target 最容易复现，也避免额外 candidate generation；当同一条件存在多个合理 mode 时，它却可能把一次
任意匹配当成唯一正确路径。另一条训练分支为同一输入生成多个候选匹配，按预先声明的 scorer 选择其中一个再更新
模型，使训练更接近推理时的 mode commitment：

```text
condition + target set
→ sample multiple candidate matches
→ score under frozen matching contract
→ select one training trajectory
→ update generator
```

这让 exploration 成为除模型规模和每样本计算之外的第三条训练计算轴，但没有创造更可靠的 ground truth。候选数增加
会线性或超线性放大生成与筛选成本，选择器偏差还会把某种 mode 固化成训练偏好。固定单匹配在数据近单峰、预算紧或
scorer 不可信时仍合理；多候选探索只在候选多样性、selection contract 和单位训练预算收益一起验证时成立。作者的
受限 scaling curve 不能证明它会普遍替代 AR、diffusion 或 masked generation，只说明 training-time sampling policy
本身也需要被版本化和计量。

## 一个统一的成本模型

端到端时间不能只数模型 forward 次数：

```text
T_total = T_queue
        + T_encode
        + T_proposal
        + T_verify_or_correct
        + T_state_management
        + T_decode_output
```

吞吐也不能只报告 tokens/s。对于 mutable generation，应同时报告：

- committed tokens/s，而非 provisional updates/s；
- quality 在同一 scorer 下是否等价；
- block/tree/correction 使用的额外 memory；
- batch、concurrency、length、precision、hardware；
- TTFT、inter-token latency 或最终 completion latency；
- rollback、cache compaction 和 scheduler overhead。

### Parallel Progress 与 Active Compute 是两条独立成本轴

Block denoising 每次参数读取可以推进多个 token，因此主要减少串行 NFE；结构化稀疏或 spike execution 则尝试减少一次 forward 中真正活跃的 channel/operation。两者组合时，成本模型必须同时记录每次迭代提交多少有效 token，以及硬件实际执行多少 active traffic。只报告 NFE 会忽略一次 forward 的工作量，只报告 sparsity 也会忽略多轮 denoising 和状态管理。

一个受限 neuromorphic 分支用 token-level roofline 区分 memory-bound 与 compute-bound：参数读取占主导时，多 token progress 可摊薄搬运；可跳过的 inactive channels 足够多且硬件真正利用时，稀疏才减少计算或访问。它用训练目标、spike representation 与专用硬件耦合换 active traffic，不能把作者翻译任务中的能量或吞吐外推普通 GPU，更不能把 NFE 减少写成端到端 SLO。若稀疏利用不足、fallback kernel 更慢或设备不支持跳过，应回退普通 block diffusion；append-only streaming 仍可回退 AR。

<!-- source-family:SF-2026-ARXIV-2607-24841 -->

### Output Decoder 是独立的版本化 Generation Artifact

只统计 latent denoiser 或 token generator，在 decoder 轻量、输出分辨率固定时足以近似端到端成本；视频生成中，VAE decoder 可能独自占据显著 latency 与 memory bandwidth，且它的结构、压缩率和精度会改变最终画面。generation identity 因此不能止于主模型 checkpoint：latent shape/scale、decoder revision、operator/kernel、precision、resolution 与 frame count 必须一起进入 artifact 和 evaluation contract。主生成器拥有 latent proposal，decoder 拥有 latent-to-output transform，只有最终媒体通过质量和格式 gate 后才算 committed output。

channel pruning、operator replacement 与 distillation 可以缩短 decode，却会引入重建误差、时序闪烁、分辨率/帧数外推失效和硬件特化；主模型质量不变也不能证明最终输出等价。decoder 不是瓶颈、质量容忍度低或运行条件离校准域很远时，应保留原 decoder 或逐级 fallback。优化必须报告完整 pipeline latency 与最终质量，而不能把 decoder microbenchmark 当成整个生成系统加速。

<!-- SF-2026-ARXIV-2602-19161 -->

如果论文为每个 dataset 事后选择最佳 tree budget，它证明“存在有效 operating point”，不等于已经给出线上 controller。

## 文本、图像和视频为何不能共享一套性能结论

文本通常要求 prefix correctness、streaming 和 stop/tool semantics；图像更关心最终 sample quality，允许整幅反复修正；视频还要保持 temporal consistency，单次 token 数和 decoder cost 很高。

因此同一个生成范式在不同 modality 上的瓶颈不同：

| Workload | 主要提交边界 | 常见主瓶颈 |
| --- | --- | --- |
| 文本 | prefix / token | serial decode、KV、streaming correctness |
| 图像 | final image / preview stage | denoising steps、latent decoder、resolution |
| 视频 | clip / frame window | temporal state、3D attention、decode bandwidth |
| action | action chunk / control deadline | freshness、safety、不可逆副作用 |

不能从图像 diffusion 的并行性推断文本 serving 也会同样加速，更不能把 video quality 当作 action correctness。

## Training / Inference mismatch

AR teacher forcing 训练看到正确前缀，推理看到自己的历史输出；diffusion training 看到人工 noise/mask distribution，推理看到由模型 schedule 产生的中间状态。两者都有 exposure mismatch，只是形式不同。

proposal-correction training 会显式生成错误中间状态，让模型学习修正。但 synthetic error 是否覆盖真实 rollout error，仍取决于 corruption process。过强 corruption 可能让模型学会恢复不现实噪声，过弱 corruption 又无法处理 aggressive decoding 的错误。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22765:start -->
离散 diffusion 的 artifact 也不能只由 corruption marginal 标识。同一个 clean-data prediction 经 bridge plug-in、marginalization / denoiser 或 score parameterization，可以对应不同的 reverse target；把 uniform process 提升到 absorbing-state representation，理论上可能保留 joint law，却仍改变 network target、loss conversion 与 sampling operations。因而可复现身份至少要联合版本化 corruption marginal、parameterization、loss conversion 和 sampler，不能把“forward noise 相同”当成训练与推理等价。

这种重参数化能暴露更清晰的 target、remasking 或 predictor-corrector 路径，却增加 auxiliary state、corrector steps、conversion 与 learned posterior approximation error。理论 joint-law 等价不意味着 factorized learned sampler 精确，也不证明某种 UDM/MDM 在其他 workload 上普遍更优。转换、假设或近似无法核验时，应冻结并回退原 denoiser/sampler pair，以完整 quality-cost frontier 而不是单一 objective 或 step 数比较方案。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22765:end -->

Diffusion 的 supervision granularity 也不应被默认为全程固定。高噪声阶段主要恢复全局布局，低噪声阶段才逐步承载
局部纹理；始终对齐同一个 teacher layer 或尺度，会把非平稳生成过程压成静态目标。一条受限分支让 router 根据
SNR/timestep 选择粗到细的 representation guidance，但 router 只拥有指导尺度，不拥有最终 sample correctness。

动态 guidance 用额外 teacher features、router state 和训练复杂度换更匹配的监督；冻结 VAE 的层级未必对应另一种
backbone 或 modality，router 也可能学到数据集特有 shortcut。无法验证分层特征和时序匹配时，静态 alignment 或
无额外 representation supervision 仍是更可复现的基线。现有证据只覆盖指定 SiT、VAE 与图像数据集，不证明该
粒度演进可直接迁移到文本、视频或所有 diffusion 模型。

<!-- source-family:SF-2026-ARXIV-2605-03317 -->

因此，直接把已有 sampler 的步数调小，与专门训练少步生成器不是同一个优化。后一条分支可让冻结 teacher 评价 student 自己走到的中间状态，再把纠正信号用于训练指定步数的 student；它用离线 teacher/critic 计算和额外模型版本换较短的在线轨迹，但没有消除分布偏移，换步数也未必还能复用同一 student。比较时必须同时记录训练成本、实际网络求值次数及在线质量：一步更新可能包含额外预测或 guidance forward，不能把 step 数直接当 latency。

## Cache、rollback 与 exactness

### Block Cache 可以从历史条目演进为固定大小的递归状态

Block diffusion 先完成一个 block、再让后续 block 读取已提交历史，使 cache 与流式提交重新可用；若历史仍由 attention K/V 表示，cache 容量和每步读取成本仍随上下文线性增长。另一条分支把已提交 block 写入 state-space mixer 的递归状态，并在训练时使用与该状态更新一致的 block-causal objective。这样 cache 不再保存所有历史条目，而保存固定大小的 sufficient-state proposal；相对于同一受训计算，它可以是 exact state transition，而不是部署时临时加入的近似淘汰。

常数大小只约束 state footprint，不保证信息无损、无限长度泛化或所有任务质量不变。模型必须在有限 state 中压缩历史，训练目标、mixer、block size 与 state revision 共同成为 artifact identity；需要逐项引用原文或任意历史细节时，attention cache 仍可能更可靠。作者的 3B 模型、300B-token 训练与最长 256k 测试支持其 attention/Mamba/hybrid 对照，不证明固定状态会普遍替代 KV，也不能把单流或受测 batch 吞吐外推生产 SLO。<!-- source-family:SF-2026-ARXIV-2609-11998 -->

### Commitment Policy 可以从未来稳定轨迹学习

固定置信阈值或 block schedule 假设所有 token 的收敛速度相似。对于迭代修正生成，可以从完整去噪轨迹标注“该位置何时之后不再变化”，训练 token-local controller 预测 commitment，并用动态 threshold 决定冻结位置。它把 commit owner 从静态规则变为受限 learned policy，可减少无效更新；代价是监督依赖未来轨迹、分布漂移会导致过早锁定，且 rollback 更复杂。若 controller 未校准，原有保守固定 schedule 仍是 fallback。现有证据只覆盖冻结模型上的 plug-in 控制器，不证明其保持自回归式 exactness。

视频轨迹的错误还具有时间局部性：若 verifier 能定位首个失败时刻，从最近已验证的 clean prefix 重新生成后缀，通常比每次回到根节点重采样更节省预算。Search controller 持有 prefix lineage、verifier receipt 与 restart budget；生成模型只提出新的 suffix，不能把未验证前缀自行标成稳定状态。

Temporal backtracking 的收益依赖错误可定位且任意前缀可继续生成。Verifier 误判会固化坏状态，前缀恢复也可能需要额外训练；因此定位不可靠、状态无法恢复或轨迹依赖高度全局时，应回退 root-level best-of-N。受限导航和机器人视频任务上的 matched-budget 结果，不构成通用视频质量或物理正确性保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.13861 -->

<!-- source-family:SF-2026-ARXIV-2605-24697 -->

AR append-only KV 最容易复用。block 或 editable generation 若修改早期 token，受影响的 attention state 必须重算或版本化。一个安全的 cache key 至少包含：

```text
model + tokenizer/codec + prompt prefix
+ generation algorithm + block/revision identity
+ adapter/quantization + position policy
```

speculative exactness 只在 acceptance/sampling rule 与 target distribution 对齐时成立。浮点 kernel、quantization 或 logit processor 差异也可能让“理论 exact”与具体 runtime 的 bitwise 路径不同。生产系统应区分 distributional correctness、deterministic replay 和 semantic quality。

diffusion trajectory 还存在另一类 cache：在相邻 denoising state 变化足够小时，复用完整 denoiser output。它不是 AR KV Cache 的 exact historical state，而是带 error budget 的 approximation。一个可治理的复用 policy 至少同时拥有：

```text
model / sampler / conditioning identity
sensitivity calibration profile
latent displacement and timestep gap
quality tolerance
max consecutive reuse / max staleness
cached output and refresh anchor
```

固定 skip schedule 在 workload 稳定、控制面简单时仍合理；sample-sensitive policy 可以把实际 trajectory displacement 纳入决策，却增加 calibration drift、一阶近似误差和局部小误差累积。NFE reduction 也不能直接等同端到端 latency 或 goodput。更长期的方向是让局部 sensitivity 成为 global error-budget scheduler 的输入，而不是让每一步 threshold 独立决定全部质量预算。

比“整层复用或整层刷新”更细的一条分支，是预测下一 denoising step 中哪些 token/patch state 会显著变化，
只重算这部分 mutable set，并保留一小组动态 sink 维持全局信息流。它把 cache policy 从固定 spatial mask
推进为 trajectory-conditioned refresh：selection 由当前 latent/confidence 产生，refresh 后必须更新对应 cache
version，未选位置只能在校准误差预算内复用。

这种机制新增 selector cost、变化位置漏检、sink 漂移、irregular gather 与不同请求 mutable-set shape 的 batching
损失。模型 confidence 不是 cache-validity probability；作者在 diffusion LM 上的实验也不能外推到 append-only
AR Decode。固定全刷新在 step 数少、变化广泛或 exactness 优先时仍是基线；固定 mask 在 shape 稳定、graph
capture 重要时更容易工程化。


#### 逐属性 Commitment 把 Steering 时机变成状态

统一 timestep 施加 steering 的前提，是各属性在去噪轨迹中的形成速度近似一致；它简单、可复算，也不会额外引入属性控制器。离散 diffusion 同时承担内容、风格与安全属性后，这个前提会失效：过早干预尚未稳定的属性会破坏流畅性，过晚干预又失去控制窗口。更稳妥的接口是由只读 probe 估计每个属性的 commitment 进度，再由调度器选择干预时点；probe 只提供观测，不能直接冻结 token 或越过最终生成策略。

逐属性 schedule 用额外探测、校准和轨迹监督换取更细的可控性，也新增 probe 漂移、属性耦合和干预相互覆盖等 failure mode。属性少且形成时机稳定时，统一 schedule 仍是更便宜的基线；校准不足时应回退保守晚干预。`arXiv:2605.10971v1` 的 §3–§5 与 Appendix F 只支持作者的离散 diffusion、属性与延迟设置，不证明这一时序控制可无损迁移到任意生成模型。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10971 -->

### Cache 误差是沿生成轨迹演化的状态

把 diffusion cache 的误差看成每个 site 的固定 representation mismatch，适合静态校准，却忽略先前修正会改变后续输入。trajectory-consistent calibration 沿 corrected history 逐步估计 site-local prior，使 cache 决策读取当前生成轨迹而非一次性误差表；收益是减少累计偏差，代价是离线 prior、prompt 分布和采样 schedule 共同进入 artifact identity。prior 漂移或未覆盖 cache policy 时应回退 base cache 或 full computation。现有证据只覆盖披露图像模型、H800 与采样路径，不能外推在线并发或分布外 prompt。

<!-- source-family:SF-2026-ARXIV-2605-24870 -->

视频生成还可以让 refresh policy 读取 token 的运动强度：静止区域延长复用，运动边界更频繁重算，
从而把固定 cache interval 改成内容条件化的误差预算。motion estimator 只拥有 recompute proposal，
生成器输出与质量 Gate 仍拥有提交权；估计偏差会在快速运动、遮挡或镜头切换处累积，因此需要最大
复用步数和 full-recompute fallback。它用额外运动估计、分支调度与 cache metadata 换减少重算，
只适用于作者受测的自回归视频生成路径，不等同于任意视频模型的无损 cache。
<!-- source-family:SF-2026-ARXIV-2605-01725 -->

固定 cache schedule 还假设不同 sample 与 timestep 对误差同样敏感；当生成难度和 denoising phase 变化时，这会在简单样本上浪费重算、在高敏感 step 上累积偏差。另一分支把 `reuse / recompute` 建模为 trajectory-conditioned sequential decision，并将 policy 与轻量 error corrector 分开：前者分配计算，后者只修正已选择复用的状态。二者必须共享 state/step identity、quality budget 与 fallback frontier，不能用 policy confidence 代替 correctness。

学习式 cache control 用额外训练、policy drift 与 corrector bias 换取 sample/timestep 自适应；prompt 分布、sampler 或 backbone 变化后需要重新验收。事件时证据覆盖 FLUX.1-dev、DiT 与 CogVideoX 的作者配置，不能把 headline speedup 外推为生产并发收益；低流量、短 trajectory 或校准不足时，固定 schedule 和 full recompute 仍是更可验证的基线。<!-- source-family:SF-2026-ARXIV-2607-29398 -->

### Diffusion Serving 不能直接复用 AR Token Queue

AR serving 的 ready unit 通常是“某请求的下一个 token”；masked diffusion 在同一 denoising step 共同更新多个位置，step difficulty、收敛进度和 CPU dispatch 成为新的状态。Batching 的收益来自多个请求共享一次 step forward，而不是把它们简单塞进同一 token queue；admission 需要同时约束 mask ratio、remaining steps、output budget 与 quality policy。它提高并行机会，却引入 step-level straggler、批间不同步和 dispatch overhead；短输出或单请求时，普通逐请求执行可能更简单。`arXiv:2608.23807v1` 的 LLaDA-8B + D2F LoRA、单 H200、GSM8K/HumanEval 只支持该 operating point，不能证明质量对任意 batch 都不变。

<!-- source-family:SF-2026-ARXIV-2608-23807 -->

## Scheduling：并行机会也需要被分配

更大 block、更多 tree nodes 或更多 correction loops可能提高单请求进度，也会占用更多 verification compute 和 workspace。高并发下，scheduler 可能更愿意服务多个小请求，而不是让一个请求扩展巨大 tree。

因此 generation policy 应暴露预算：

```text
proposal budget
verification budget
mutable window
deadline
quality / exactness requirement
```

model 产生 confidence，runtime 根据 queue、memory 和 SLO 选择 operating point。把 threshold 或 tree size 固定在模型代码里，会让系统失去跨工作负载调度能力。

### 先定位真正承载语义的生成窗口，再讨论动态调度

把每一个 denoising step 都视为同等重要，最容易实现和复现，也能避免误删关键计算；它的代价是即使某些阶段几乎不依赖条件输入或全局交互，系统仍支付完整 guidance 与通信成本。一个更谨慎的演进不是直接学习“哪些 step 可以跳过”，而是先把 conditional/unconditional score gap 与 global/approximately-local score gap 当作诊断信号，再用 windowed intervention 检查：只在某段时间移除 conditioning 或全局交互时，最终语义和结构究竟何时显著受损。

这类 critical-window 证据可以帮助划分阶段预算，却不授予 runtime 自动跳过计算的正确性。诊断 owner 只提出“哪些窗口可能 load-bearing”，scheduler 仍须绑定 sampler、模型、分辨率、condition identity 与质量门来选择计划；窗口漂移、局部算子并不真正局部、或条件之间存在耦合时，应回退全程计算。现有结果只覆盖 ImageNet DiT-XL 与 SD3-medium，且截断 attention 只是近似 local denoiser；两个 critical window 的接近是受测配置中的经验观察，不是所有 diffusion trajectory 的普适定理。<!-- source-family:SF-2026-ARXIV-2605-04830 -->

图像或视频 diffusion 还可以把 patch granularity 变成 trajectory policy：早期或低变化阶段使用 coarse patch，细节阶段回到 fine patch。这里必须分开两层：artifact 先通过训练获得多种 patch shape 的语义能力，runtime 才能依据 latent history 和 threshold 选择 shape。“选择规则在 test time 运行”不等于整个方案 training-free。

这种 adaptive granularity 减少单请求 token 数，也新增 latent-history state、threshold calibration、shape switching 与多分支 artifact identity；不同请求选择不同 shape 时，还可能破坏 batching、graph capture 与 kernel reuse。固定 fine patch 在 worst-case detail、可预测 shape 和成熟 kernel 场景仍成立。若论文的 threshold table、hardware、precision 或配置记录相互矛盾，Books 只能吸收机制与 failure mode，不能吸收精确 speedup。

### Conditional Guidance 把 Diffusion 并行策略变成逐 Step 状态

空间 patch data parallel 容易在边界引入 artifact 和 All-Gather，固定 pipeline parallel 又会让跨 step 的旧估计累积；
它们在并行形态固定、分辨率和拓扑稳定时仍是可预测基线。conditional diffusion 同时计算 conditional 与
unconditional denoising path 后，多出一条与图像 patch 不同的切分轴：两个 path 可以分到不同设备，随后再合成
guidance update；当两条 path 的 denoising discrepancy 随 step 改变时，runtime 还可以在 condition-based data
parallel 与 pipeline schedule 之间有界切换。

这使 parallel policy 必须绑定 denoising step、latent revision、conditional/unconditional branch identity、discrepancy
metric、threshold、GPU topology 与切换 epoch。model 产生两条 denoising state，scheduler 只提出 parallel plan，
runtime 在 step boundary 同步后 commit；任一 branch 缺失或版本不一致都不能继续合成。收益来自利用原本已存在的
guidance 分支，而不是免费减少模型计算；代价是双分支同步、metric calibration、切换 barrier、额外通信和随机
轨迹下的抖动。discrepancy 不稳定、单 GPU、无 classifier-free guidance 或固定计划更易捕获 graph 时，应回退静态
data/pipeline 或单设备执行。作者结果只覆盖 SDXL、SD3 与其双 RTX 3090 配置，不能外推其他模型、并发或 SLO。

<!-- source-family:SF-2026-ARXIV-2602-21760 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22050:start -->
生成完成后再运行 copy detector 并重试，在检测器可靠、重跑成本可接受时最容易隔离状态；固定 guidance、prompt 或 latent 调整也保持控制面简单，却不能随当前 trajectory 的异常强度变化。若目标是保留当前 denoising path、同时更早压制潜在复制，可以从 clean reference prompts 为每个 timestep 与模型版本冻结 latent update、latent norm 和 reconstructed initial-latent 的经验区域。Sensor 只报告轨迹偏离强度，sampler controller 才能按预先定义的 mild/strong policy 对 provisional state 做有界 rescale；独立 copy、provenance 与 privacy gate 仍拥有最终 acceptance。

这条路径避免每次 abort-and-regenerate，却增加 reference distribution、threshold、逐 step 状态与漂移风险：正常但稀有的样本可能被压回均值，不呈相同动力学的复制又可能漏过。Out-of-region 不是训练记录身份，in-region 也不证明安全，更不证明权重已经删除数据。Reference coverage、false-positive rate、copy audit、semantic fidelity 或 scheduler transfer 失败时，应停用 adaptive projection，回退 detect-then-retry、已验证静态 sampler、独立来源检查或训练侧 filtering/unlearning。现有证据只覆盖论文披露的 Stable Diffusion、sampler、校准集与 SSCD-style 指标。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22050:end -->
<!-- source-family:SF-2026-ARXIV-2605-22050 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07701:start -->
固定 classifier-free guidance scale 在任务和各去噪阶段的控制需求近似稳定时最容易复现；离散文本 diffusion 中，过强 guidance 会牺牲流畅性与多样性，过弱又无法满足任务约束，而且合适强度会随 provisional state 改变。可把每一步的 scale 视为有界 action，让 policy 读取当前 diffusion state，在 task-level reward 下学习 guidance trajectory；sampler 仍拥有 token revision 与 commit，policy 只提议控制量。

该分支用额外策略训练、状态编码和 reward coupling 换 task/step 自适应，也新增 policy drift、terminal-reward shortcut 与不可解释的早期锁定。任务、sampler 或 reward revision 改变而未重新校准时，应回退固定 CFG 或保守 heuristic schedule。exact-v1 的结果只支持作者所测离散 diffusion 任务，不证明动态 guidance 会取代固定 guidance。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07701:end -->

#### Guidance 可以前移到 Prior，但误差会集中到初始状态

标准 classifier-free guidance 在每个 velocity evaluation 都运行条件与无条件分支，语义清楚但网络求值翻倍。条件 prior 分支把 guidance control 前移到初始噪声分布的均值/方差，用小型 prior 完成一次 steering 后执行单 pass sampling；runtime 由此减少 forward count，却把条件逼近误差集中到 prior artifact、guidance scale 与 sampler identity。

这种替代只在一阶近似和校准范围内接近标准 CFG，并新增 prior 漂移与初始偏差难以逐步修正的风险。guidance scale 越界或质量下降时，应回退 dual-pass CFG，两者可按 workload 共存。`arXiv:2605.06124v1` 的实验限于 MNIST、CIFAR、ImageNet 256、U-Net/DiT-B/2 与单 RTX4090；作者延迟不能外推生产并发或 tail SLO。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06124 -->

### 从一次生成到 Plan → Generate → Validate → Retry

Autoregressive media generation 的状态机不能永远停留在“给定 prefix，继续采样”。当输出同时受内容、时序、
韵律、音色或安全约束时，直接生成仍然合理：路径短、延迟低，也不需要维护额外控制状态；它的边界是错误
往往要到完整 artifact 产生后才暴露，局部修复又可能破坏其他约束。

一种 `Layering / Dependency` 演进是先生成可检查的 plan，再生成高带宽 token，最后用独立 validator 决定
commit、bounded retry 或 fallback：

```text
request + locale / speaker / policy identity
→ content / timing / control plan
→ autoregressive media tokens
→ acoustic / semantic / policy validation
→ commit | regenerate with diagnosis | fallback
```

音频生成提供了另一条层级分支：粗粒度 acoustic token 由 AR 路径负责长程结构与条件一致性，细粒度
token 再用固定步数并行补全局部质感。它把“所有声学细节都串行生成”改成 coarse commit 与 fine
refinement 两级状态，用更低串行深度换取 tokenizer 层级、跨层对齐和并行补全误差。结构错误必须回退
重生成 coarse stream；只修细节不能挽救节奏或语义。作者 human arena 与消融只支持其模型、tokenizer
和音乐任务，不证明该 factorization 可直接迁移到语音、任意采样率或生产延迟。
<!-- source-family:SF-2026-ARXIV-2605-01790 -->

这里的 plan 是 provisional control state，不是模型已经正确理解约束的证明；validator 也必须拥有版本、阈值、
false-positive/false-negative 与覆盖范围。Retry 若复用同一错误 plan 只会重复失败，若完全重建则增加 latency、
compute 和 output variance；streaming 一旦播放前缀，rollback boundary 还会变成用户可见协议。小模型、低风险、
严格 latency 或 validator 不可靠时，direct generation 与简单 post-filter 仍然成立。

Amazon 的 LLM-based TTS 工程材料支持“显式计划、生成后检查与有限重试可组成一条工程路径”，但没有公开
可复现实验 artifact、模型内部实现、并发或 tail-SLO contract；因此这里只吸收状态机，不外推质量数字或
内部机制。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-13006:start -->
在 video diffusion 中，plan 还可以从生成前说明书演进为生成中的 addressable revision state。VLM 先把对象、动作、深度和运动强度编译为 kinematic conditions；迭代优化阶段再用 object-centric gradient routing，只向当前主动对象对应的 latent 区域传播修正，尽量不扰动被动环境。Planner 拥有 provisional physical constraints，gradient router 只拥有局部更新 proposal，base generator 产生候选 trajectory，独立 validator 才决定修改是否可以 commit；“被 mask 的区域没有更新”不等于真实环境必然静止。

这条分支以推理期 backprop、VLM/API 调用、mask 对齐和更多显存换取局部可控性。Plan 错误与 gradient routing 错误会形成共因，过窄 mask 会冻结本应变化的环境，过宽 mask 又退化为全局重写；keyframe 增加还会累积规划误差。低约束、短视频或 latency 优先时，direct generation 仍是合理基线。Physics-aware video generation exact-v1 的组件消融和受限人评只支持给定基座、3–5 个 keyframes 与 PhysGenBench 下的局部机制，不证明系统获得一般物理定律、复杂接触正确性或实时生产能力。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-13006:end -->

### 长视频窗口中的频谱责任分工

扩大生成窗口通常试图直接换取全局一致性，但它也可能使 attention feature 的奇异谱过度集中，让低频结构压制局部细节。一个条件化分支是把全局低秩 guidance 与局部高秩 reconstruction 分责：前者约束跨窗口的长程结构，后者恢复窗口内的细粒度变化，从而避免预先把表示硬拆成“appearance”和“motion”。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06509 -->

这个分工依赖谱集中确实是主要故障来源。现有证据只覆盖 Wan2.1、LTX-Video 和作者的评价设置，SVD 成本、复杂镜头运动及跨 backbone 稳定性仍未证明。谱假设不成立或质量收益不足时，应回退 overlap/local-window、显式 feature partition，或以训练方式获得的长视频机制，而不是把频谱修复当作统一答案。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06924:start -->
长视频不能只把上一段末帧当下一段条件；一旦主体离场再出现、环境发生非线性变化，open-loop chaining 会把早期误差持续放大。生成 runtime 可为每段执行 `retrieve → synthesize → frame/video-level refine → update`，由版本化 multimodal memory 保存实体、环境与叙事进展，mode controller 只在已声明的 extrapolation/interpolation 分支中选择，最终 clip gate 才提交可见段。它用额外生成、检索与 self-review 换长程一致性，也会继承同源 evaluator 偏差、memory drift 和 mode-switch 错误；状态不可信或预算不足时回退短段、固定模式、人工 storyboard 或整段重生成。 [受限证据：arXiv:2605.06924v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-06924:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20476:start -->
当整段 conditioning 与 anchor 可预先确定时，还可以把左到右的 `K` 段 critical path 改成 sparse-to-dense
anchored tree：先生成稀疏锚点，再在相邻 anchor 之间分层并行 infill，使串行深度接近层级数，并把单次误差约束在
anchor-bounded span。它不是 rolling memory 的无条件升级；rolling path 适合条件逐步到达和在线 streaming，
anchored tree 则要求未来边界可知、双向 infill 可靠。

层级并行减少 horizon-compounding drift，却会让坏 anchor 污染整个子树；弱 motion guidance、动态镜头、多镜头和
纯 text-to-video 也未满足当前证据前提。Anchor quality 或 continuity Gate 失败时，应回退短窗 AR、overlap
refinement、整段重生成或人工 storyboard。exact-v1 只支持 Wan2.1+VACE 的五类 condition 与 LTX-2.3 静态镜头
实验，不证明任意长视频都获得同样关键路径缩短或一致性收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20476:end -->

## 失败模式与旧方案适用边界

### Error amplification

并行接受多个相互条件化不足的 token，会让一次错误污染整个 block。保守 AR 或小 block 在错误代价高时仍合理。

### Correction oscillation

corrector 反复在多个 token 之间切换，耗尽预算且无法形成 commit。需要最大 revision 次数、置信滞回或 verifier。

### Cache inconsistency

token 已修改而 KV、radix tree 或 downstream parser 未失效，产生隐蔽的错误状态。

### Oracle policy

实验离线选择最佳 threshold/budget，线上没有相同信息。应单独验证 controller，而非沿用 oracle 上界。

### Framework mismatch

tree mask 落到较慢 kernel、dynamic shape 破坏 graph capture，算法减少 steps 却增加 wall time。旧的单路径 AR 在成熟 kernel、高并发和短输出下可能更快。

## 工程实践

选择生成范式时按顺序回答：

1. 输出何时产生不可撤销副作用？
2. 质量目标要求 exact target distribution，还是允许新的 learned distribution？
3. workload 更看重 TTFT、streaming cadence 还是 final completion？
4. 硬件和 runtime 是否支持 block/tree mask、dynamic shape 与 KV compaction？
5. proposal/correction 的额外计算能否被 acceptance 或并行进度偿还？
6. policy 是固定参数、模型置信度控制，还是 scheduler 预算控制？
7. Evaluation 是否使用 committed output 和完整 workload contract？

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-27732:start -->
Diffusion-LM 可用 asymmetric bidirectional sidecar 提供受控右上下文，同时让主干保留可缓存的单向状态。它以额外 sidecar 参数和融合开销换 parallel correction；若右上下文收益抵不过 cache invalidation 和迭代成本，仍回到纯 AR 或无缓存的双向分支。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-27732:end -->

### Distributional Distance 可以成为受限训练目标

Fréchet 类表示距离通常用于训练后评估，因为 batch 内同时估计 population statistics 与反向传播会带来偏差和不稳定。把统计 population 与 gradient batch 解耦后，它可以成为直接 distribution-matching loss，但需要维护 estimator state，并继承 representation encoder 的语义偏差。该路线适合明确表示空间与分布目标的生成 workload；它不证明 perceptual alignment，也不能从图像结果外推所有模态，样本级 likelihood 或任务损失仍是重要共存分支。

<!-- source-family:SF-2026-ARXIV-2604-28190 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-12691:start -->
图像编辑进一步要求把“执行目标指令”和“保留未指定上下文”拆成不同训练状态。只优化 text–image alignment 会鼓励模型重画整幅图，只优化 source similarity 又会阻止必要修改；一个受限分支分别编码 instruction、source image 与 source spatial latent，再让冻结 VLM 从目标图像产生 descriptive anchor，由可训练 aligner 比较生成图与 anchor 的 token distribution，把语义残差经低噪声单步估计传回 generator。VLM 只提供 training-time gradient proposal，generator 保留生成权，独立 evaluator 才判断编辑是否成功；anchor 不能凭自身输出成为视觉真值。

这样可以在不增加线上 verifier 的情况下前移语义约束，却增加冻结模型偏差、单步梯度近似、训练显存和 identity-preservation 冲突。关系词、组合约束或 anchor 遗漏会把错误方向稳定地写入生成器；局部几何明确时，pixel/perceptual loss 仍更直接。IABEdit exact-v1 的 RealEdit/MagicBrush 对照支持该责任分解在受测设置中的可行性，但部分感知指标并非最优，且论文训练 FLOPs 的绝对值与百分比互相冲突，因此成本数字不得进入长期结论。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-12691:end -->

### 固定长度 Diffusion 把长度预测变成 Admission 决策

自回归生成可以逐 token 停止，固定长度 diffusion LM 却需要在去噪开始前分配响应槽位；因此 length predictor 实际上拥有一次 admission-time compute budget。预测偏长会浪费并行迭代，预测偏短则可能截断语义并触发扩容或整段重试，破坏原本的延迟优势。动态长度只有在预测开销、重试策略和 SLO 一起计入时才成立；长度高度不确定或输出必须完整时，保守上界或自回归分支仍更可靠。[受限证据：arXiv:2605.04215v1]

<!-- source-family:SF-2026-ARXIV-2605-04215 -->

若生成中再插入槽位，旧位置与新画布的坐标映射、画布版本和 logits 必须一起绑定；比较分布时需明确哪些旧未决位置可比较，提交只能使用被选画布对应的预测，不能把旧画布 logits 当作新状态。以平均分布差异决定是否扩容是带额外 forward 与对齐成本的启发式，既不保证每个位置不变，也不保证原生成分布或最终延迟不变；固定画布仍是状态简单、容易验证的共存方案。

固定画布中若同一个 EOS 同时表达“语义已经结束”和“剩余位置只是 padding”，训练会把内容终止与空间占位混为一个状态。独立的 VOID token 可以让 sampler 先管理空白槽位，再让 EOS 专注语义提交；length/admission、denoising 与 final commit 因而拥有不同 owner。它以新增 token、objective 和 runtime compatibility 换更清楚的终止语义，不能从单一 masked-diffusion 实验外推所有生成范式；自回归逐 token 终止仍是更自然的共存分支。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.17999 -->

## 加速不能静默改变生成轨迹

缓存或跳步加速在多模态 Diffusion 中会复用旧的视觉与文本状态。旧状态足够接近时，它减少重复计算；随着轨迹推进，stale state 会让加速输出与未加速模型系统性分叉。因而“更快但 benchmark 仍可用”并不等于语义等价，运行时还要测量 state freshness、输出 agreement 与 refresh cost。

这形成一个明确的控制分支：短 refresh interval 提高一致性却回收较少计算，长 interval 提高速度却扩大漂移。控制器只能把 confidence 当刷新信号，不能当 correctness certificate；漂移超过预算时回退完整 refresh。该分支属于 iterative refinement，不应外推到具有不同状态语义的自回归 Decode。

### 加速后的输出必须与未加速轨迹建立一致性边界

缓存或跳步能减少 diffusion 的重复计算，但“最终观感尚可”不能证明它仍在执行同一生成过程：stale visual state 与已生成文本状态可能把内容推向另一条轨迹。运行时应把 refresh interval、state revision 与同模型 full-compute 输出的一致性作为联合验收量；缩短 refresh 可以提高一致性，却会交还一部分加速收益。该检查只约束近似分支的语义漂移，不保证两个随机样本逐点相同；一致性或 freshness 超界时应恢复更密集刷新或全量重算，固定 schedule 在分布稳定时仍是可预测基线。
<!-- source-family: arxiv:2607.29079v1; daily: 2026-08-03; semantic-body-binding: accelerated-generation-state-agreement -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22723:start -->
Gaussian DDPM 只匹配 reverse mean 时，会保留沿完整生成路径累积的 covariance error；在论文假设下，匹配 full reverse covariance 可改善离散 path KL 的收敛阶。显式协方差不可承受时，matrix-free Lanczos 用 covariance-vector products 近似所需矩阵函数，以更多算子调用换取无需构造完整矩阵。Sampler owner 必须把 covariance estimator、Lanczos iteration、residual tolerance 与 step schedule 共同版本化。

更好的理论阶数不等于真实数据上的感知质量或低延迟收益，Lanczos iteration 还引入计算和数值误差。exact-v1 的 Gaussian/score regularity、图像任务和受测设置不能外推到任意 diffusion workload；假设、residual 或端到端质量不满足时，应回退 mean-only sampler、更多 steps 或对角/低秩 covariance，并保留 full-compute reference trajectory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22723:end -->

### 已 Finalize 的 diffusion block 也可能需要可控重开

block diffusion 把局部结果 finalize 后可以并行推进后续计算，但早期错误会被后续 Context 固化。需要编辑时，不能直接覆盖 token 而保留依赖它的 cache/state；正确演进是 `reopen -> invalidate dependent KV/state -> refine -> reverify -> recommit`，并让 commit revision 成为下游 identity。

可重开提高纠错能力，却增加回滚范围、重复计算和并发一致性。只有 verifier 发现的收益超过 invalidation 成本时才启动；低风险生成或依赖扇出很大时，重新生成整个 suffix 仍更简单可靠。

<!-- source-family:SF-2026-ARXIV-2607-22663 -->

## 本章在知识树中的位置

第18章解释 Decoder Only AR，第20章解释 token sampling；本章把 AR 放进更宽的生成范式树，并拥有 mutable generation、block refinement 与 commit boundary。第25章只在生成状态同时表达 action-conditioned environment transition 时才称其为 World Model。

训练 objective 归 Part IV；线上 KV、batching、speculative verification 与 scheduler 分别由 Ch45～48、Ch56 拥有。本章定义它们要执行的 generation semantics，而不重复框架实现。

## 从机制演进到系统设计

生成范式的演进不是 AR 被 Diffusion 线性取代，而是 factorization、并行度与 correction authority 的重新分配。AR 每次提交一个 token，状态简单但串行；masked、block 或 diffusion 路线并行提出多个 provisional positions，再以迭代修正换吞吐。混合方案进一步把 proposal、verification、rollback 和 commit 拆开。

并行生成只有在质量合同、cache invalidation 和停止规则都被版本化后才成立。它获得并行度，却增加迭代次数、临时状态、拒绝/回滚以及训练—推理 mismatch；短输出、严格 exactness 或 correction 成本高时，AR 仍可能更优。图像、视频和文本的 evaluator、长度与硬件路径不同，不能共享未经条件化的性能结论。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22370 -->
长视频生成不能无限复制完整历史 KV；按 prompt-history 相关性选择可读历史，把 cache budget、selection error 与 continuity 绑定同一运行时状态。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只覆盖受测长单镜头生成；selection miss 会破坏长期一致性，不能外推到可交互 world state。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 面试与自检问题

1. 为什么 diffusion 的 serial steps 少于 token 数仍不保证更快？
2. masked generation 中 provisional 与 committed token 有何区别？
3. Block Diffusion 如何在 AR 与 full-sequence diffusion 之间取舍？
4. correction 与 exact speculative verification 的 correctness contract 有何不同？
5. 为什么 draft marginal 不能当作 target path probability？
6. mutable token 会怎样影响 KV cache 和 streaming？
7. 一个离线 best-budget benchmark 为什么不等于线上 controller？
8. 哪些场景下 append-only AR 仍是更好的工程选择？

## Research Outlook

下一阶段压力是让 generation policy 成为 runtime 可控制对象：根据 entropy、queue、memory、deadline 和 output side effect 动态选择 block、proposal、correction 与 commit；同时建立跨 runtime 可复现的 committed-goodput 与 exactness 测试。

## Refinement 位置也可以成为条件计算状态

在并行 refinement 中，不同位置距离稳定状态的远近不同，继续给所有 token 相同 expert budget 会把计算浪费在已经收敛的位置。条件计算可以读取 block-relative position、当前 refinement step 与收敛 frontier，为未稳定位置分配更多专家容量；它没有改变最终 commit owner，却把“还需要多少计算”从固定超参变成运行时状态。收益是减少无效计算，代价是训练—推理联合校准、router 抖动和调度复杂度；短轨迹、负载稳定或状态估计不可靠时，固定预算仍是可验证基线。`arXiv:2608.01784v1` 只支持作者 Diffusion-MoE 配置，不能外推为所有生成模型的通用加速。<!-- source-family:SF-2026-ARXIV-2608-01784 -->

## Few-step Distillation 要在 Student 实际访问的状态上验收

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06376:start -->
### Continuous Schedule 用 Coverage 换掉固定 Anchor 的盲区

离散 distribution matching 在少量固定时刻对齐，训练和实现都简单；few-step student 实际访问的 off-trajectory state 可能落在 anchor 之间，形成 truncation drift。Continuous-time 分支随机采样轨迹长度，并让 student velocity 在非锚点状态上对齐目标分布，把“覆盖了哪些状态”变成训练合同的一部分，而不是只增加一个更强 loss。

更连续的 coverage 减少固定 anchor 盲区，却提高状态采样、稳定性与校准成本。现有结果只覆盖 SD3-Medium、Longcat-Image、作者 metrics 与 few-step setting，不证明其他 modality、backbone 或生产 latency。off-trajectory state 不可靠或训练发散时，应回退 discrete DMD、consistency distillation 或增加 sampling steps。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06376:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07924:start -->
Few-step flow distillation 不一定受 student capacity 限制；若 teacher trajectory 用盲目随机 midpoint 构造，target 本身就可能偏离高质量路径。训练端可让冻结 teacher 生成多个 midpoint candidate，再由仅训练期可见的 energy navigator 选择 target，student runtime 不携带该 navigator。它用额外 teacher/energy compute 换更好的低 NFE trajectory，也会继承 energy bias 并压低 diversity；tau、teacher、energy 与 source distribution 必须进入训练身份，entropy 或任务质量越界时回退普通 DFM trajectory、更多 sampling steps 或统一 distillation。 [受限证据：arXiv:2605.07924v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07924:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09536:start -->
统一 trajectory distillation 把所有时间间隔视为同一种误差，在 denoising dynamics 平稳时简单；但相邻时刻的局部变化与跨越较远时刻的全局变化可能需要不同监督。Temporal-aware 分支从冻结 teacher trajectory 中构造 privileged targets，再按时间距离分配蒸馏目标；训练 artifact 保存 teacher、trajectory 和时间策略，runtime 只选择已经通过质量—速度验收的 operating mode。

更少采样步数是以 teacher rollout、轨迹偏差和额外训练成本换来的，远近状态划分错误还可能同时伤害速度和质量。现有证据仅覆盖作者模型、数据、实现与 evaluator，不证明跨任务、硬件、长度或生产尾延迟的普遍收益。Student 轨迹离开校准区域、diversity 下降或目标任务改变时，应回退原始 diffusion steps 或统一 distillation。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09536:end -->

把多个 teacher step 压成一个 student transition 时，离线 teacher trajectory 是合理起点，但 student 的早期并行提交会改变后续 context，使真实状态逐步离开监督分布。更稳妥的 on-policy 分支从 student 自己生成的 partial state 出发，由冻结 teacher 提出 outcome-aligned future candidates，并只提交仍保持 rollout outcome 的最长前缀；验证失败就缩短 transition。收益是减少 function evaluations，代价是在线采样、teacher 计算与一致性判定误差；高风险或状态漂移明显时，多步 refinement 仍是正确性基线。`arXiv:2608.02942v1` 只在作者数学和代码 benchmark 上支持该质量—效率前沿。<!-- source-family:SF-2026-ARXIV-2608-02942 -->

另一条离线分支不直接预测最终 clean sample，而让 student 一次提出多个连续 denoising transitions，并拟合 teacher trajectory 的 mean velocity。它把 sequential denoise 改成 multi-step proposal，避免每个被压缩 step 都依赖 JVP 或 finite difference；scheduler 可以选择少量 student evaluations，但仍必须把 proposal 看作有损近似，而不是 exact 跳步。

受限实验在披露的 LTX、Wan 与 Qwen-Image 设置中支持 4–8 NFE 的质量—diversity operating points，却不证明 NFE 等于 wall time、data-free distillation 跨域稳定或 mode collapse 已消失。发布 gate 应联合比较真实 latency、峰值内存、sample diversity、目标质量和失败时回退原始多步 denoiser；分布漂移、diversity 下降或 student 轨迹越界时，多步 teacher sampler 仍是正确 fallback。

<!-- source-family:SF-2026-ARXIV-2607-26004 -->

## 双向生成中的 Cache 是可变状态，不是只读前缀

diffusion 或 masked refinement 会反复修改序列两侧，传统只追加 KV cache 的不变量不再成立。复用稳定 affix 可以减少重算，但 request-specific anchor 与被更新位置必须重新计算，并把 timestep、mask 和版本纳入 cache identity。错误地沿用自回归前缀语义会产生静默污染；保守全重算仍是低复用或高变化率下的正确基线。
<!-- source-family: arxiv:2608.26140v1; semantic-body-binding: bidirectional-affix-cache-mutability -->

进一步的近似分支只复用 token identity 已冻结的 prompt K/V，并以 response state neighborhood 与 decoder margin 判断可变区域是否仍可复用。Prompt reuse 因而是受状态距离约束的 proposal，不是 AR 式 exact prefix：mutable response 必须刷新，越界就回退 full refresh。它用距离估计与误差校准换取较少重算，也会引入阈值漂移和静默近似误差；高风险输出或 state 快速变化时，完整刷新仍是基线。

<!-- source-family: arxiv:2608.08086v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: reversible-response-cache-state-neighborhood -->

## Object Permanence 与 Addressable History 是两个 Gate

视频生成能够在短片段中维持对象外观，不代表系统拥有可寻址、可更新的长期环境状态。环形或有界历史机制可以扩展可引用的过去，但仍需分别验证对象身份持续性和历史容量；两者都通过，也不能自动推出 action-conditioned causal transition。它是生成状态管理的进化，不应被误写成完整 world model。
<!-- source-family: arxiv:2608.26794v1; semantic-body-binding: video-object-permanence-vs-history-capacity -->

## Transparency 不是单一的“可解释程度”

可读 token bottleneck 或可干预中间变量只提供 variable transparency：我们能命名并操纵某些状态。它不自动给出 algorithmic transparency，因为并行去噪或多步 refinement 的实际计算路径仍可能很深；也不自动给出 safety monitorability，因为可观察变量未必对危险行为具有稳定、可校准的因果关系。生成系统应分别记录变量接口、有效串行深度和安全 sensor contract，不能用其中一项替代另外两项。

显式中间变量便于 probe 与控制，却可能增加架构约束、额外 step 和错误解释；更短的可观察路径也不保证语义忠实。纯 AR 或 opaque diffusion 在只要求输出质量、且外部 verifier 足够时仍可成立。现有证据只为特定 diffusion language model 提供 opaque serial-depth 的界与局部 probe，架构和训练各自造成多少透明度仍未分离，因此不能外推为通用安全优势。
<!-- source-family:SF-2026-ARXIV-2606-20560 -->

## Reflection

生成范式不是从“串行”走向“并行”的单向进步史。系统用并行草拟换来了 mutable state，用修正换来了额外 forward，用更大候选空间换来了 verification 和 memory。真正的演进，是让这些成本与输出承诺被显式管理。

### Early convergence 与 high confidence 不是同一个 Commit 证据

并行去噪最初常用当前位置的边际置信度决定是否提前提交；它便宜，却把“这一步很确定”误写成“后续步骤不会再改变”。约束变化是多个位置共同修正时，单点高置信仍可能被后续条件关系推翻。更严格的 runtime 可以追踪一个 token 在连续 denoising steps 中是否已经稳定，把 early-convergence signal 与边际 confidence 联合用于 provisional-to-committed transition。

这会减少不必要的更新，却增加跨步状态、滞回阈值与误提交风险；稳定检测仍不是联合分布正确性的证明。检测不可靠、输出有外部副作用或 exactness 优先时，应延后到 block verifier 或完整 denoising 结束再 commit。该分支补充本章的 mutable-state 路线，不宣称它普遍优于 confidence schedule。[受限证据：arXiv:2605.10980v1]

多个位置各自具有高边际置信度，也不保证它们组成的 joint configuration 一致。一个受限分支在 commit 前加入 pairwise compatibility，并以 mean-field / fixed-point 更新修正各位置的 marginal score；它减少“单点都合理、组合却冲突”的并行提交，但增加二阶计算，且 pairwise 近似仍看不到高阶依赖。短 block、依赖弱或额外校正成本超过并行收益时，保守顺序提交与 target block verification 仍更清楚。作者在特定 discrete diffusion reasoning/code 任务上的结果只支持该近似的局部质量—延迟取舍，不提供通用 joint correctness。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15805 -->

<!-- source-family:SF-2026-ARXIV-2605-10980 -->

### 训练表示与部署表示可以分离，但迁移上限必须显式

latent diffusion 借助 VAE 降低训练与推理成本，却让生成质量受 latent bottleneck 和 decoder 约束。一个替代分支用
latent teacher 生成合成图像训练 pixel-space generator，部署时移除 VAE；这把 latent model 从在线执行组件改成训练数据
producer，pixel model 才拥有最终生成状态。收益是解除线上 codec 约束，代价是 synthetic source 的质量上限、额外生成
成本与 teacher bias。teacher 覆盖不足或高分辨率细节未通过独立验收时，应保留 latent pipeline 或混合真实数据；
现有证据仅覆盖作者的 1024/4K 设置与受测 teacher。

<!-- source-family:SF-2026-ARXIV-2605-12013 -->

### 生成范式差异要拆成 Objective 与 Commit Policy

AR 与 masked diffusion 的输出差异不能全部归因于“单向或双向”训练目标。受控对照把 objective 与 confidence-based remasking 分开后表明，双向目标和迭代 commit policy 会分别改变 token entropy 与错误修正路径；因此比较生成范式时必须冻结模型规模、训练数据与采样预算，再单独改变其中一个状态。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12522 -->

这些观察只覆盖所测语言模型和 evaluator，不证明某种范式普遍更有创造力或更可靠。无法隔离变量时，应回退端到端质量、延迟和 exactness 合同，不从文本风格反推内部机制。

### Masked Diffusion 的训练预算可以按 Locality 重分配

均匀采样 mask pattern 简单且无偏，但会反复训练相距很远、条件信息薄弱的位置。语言具有局部依赖时，可以重分配预测位置与可见 context，使每次更新更常覆盖有信息的邻域，从而改善同预算下的训练效率。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13026 -->

这种加速依赖 locality bias，可能削弱远程依赖和全局一致性。现有实验不能证明任意语言或长上下文任务都受益；长程 slice 回归时，应回退均匀 mask、混合采样或显式增加远程依赖样本。

### Iterative Generation 允许安全状态被重新 Mask

AR token 一经提交便只能在后续补救，而 masked diffusion 的中间 token 仍是可修改状态。安全 sensor 可以在 denoising step 间对 latent steering，并把高风险或低置信位置重新 mask 后再生成；这把防护从一次输入/输出过滤推进为逐步 proposal-correction loop。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13043 -->

安全 sensor 的误报会造成反复 remask、质量下降或无法终止，漏报则仍会提交有害序列。证据只支持所测模型、攻击和 evaluator；校准漂移或迭代超预算时，应回退独立输入/输出 policy gate，并保留最大重试次数和拒绝路径。

### 关联记忆模块不能跨模态直接外推

Hash-keyed O(1) associative memory 在文本中可能为重复局部 token pattern 提供捷径，但受控负结果显示，它移入 AR 图像生成后未必承担同样的 retrieval 功能。图像 token 的局部重复、顺序结构与语义身份不同，模块名称相同不代表机制角色相同。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13179 -->

这是一条反外推证据而不是“Engram 永远无效”的结论。若新模态上没有 retrieval ablation、命中率与生成质量的共同证据，应保留普通 Transformer 路径，不以文本任务收益批准图像系统复杂度。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20309:start -->
但“不能直接外推”也不等于视觉关联记忆没有可行边界。一条更窄的路径把 exact n-gram registry 当作显式地址，只在
匹配 span 时向冻结生成 backbone 注入 concept residual；no-trigger 路径完全不激活该分支。这样，trigger registry、
concept adapter 与 activation record 共同形成可审计的 personalization state，而不是把记忆能力归因于整个模型。

显式 lexical address 换来局部激活和便宜模块化，也把 tokenizer 兼容、组合 trigger 冲突与 registry provenance
带入生成合同；初步视频结果仍不能证明跨帧身份稳定。未命中、跨 tokenizer 或视频一致性失败时，应关闭 memory
branch，回退冻结生成器、普通 LoRA/adapter 或更强视觉状态注入。现有证据只覆盖 exact-v1 的 SD1.5/SD3.5、初步
Wan2.2 与定性小样本，没有与 DreamBooth/LoRA 做 matched benchmark。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20309:end -->

### Latent Reuse 受 Subspace Shift 约束

复用已有 diffusion latent space 可以节省重新训练 encoder 的成本，但新数据若离开原 latent subspace，或噪声沿不受支持方向增长，denoiser 会在错误几何上拟合。可拒绝的复用合同应测量 subspace overlap、shift 与噪声，而不是只比较重建样例。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13448 -->

理论边界只覆盖论文假设与合成/受限分布，不能给出所有真实数据的阈值。shift 指标或 downstream quality 失效时，应重新训练表示、扩大 latent capacity，或回退像素/原表示空间。

### Any-step Flow Map 把步数变成运行时状态

固定少步 distillation 为某个 step count 优化，部署改变延迟预算时常需另一套 student。Any-step flow-map distillation 学习非相邻时间间的映射，使运行时可按预算选择跳转长度；获得的是可调 latency-quality frontier，代价是跨多种步长训练并维护跳转一致性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13724 -->

任意步数并不保证任意 schedule 都稳定，长跳转会放大误差。视频 diffusion 的现有证据不外推其他模型或生产尾延迟；质量或一致性越界时，应增加 steps、回退固定 student 或完整 solver。

### 少步生成的 Diversity Control 可以进入内部表示，但不能绕过质量 Gate

单步或少步 diffusion 丢失了多步 trajectory 中反复注入随机性的接口。受限分支可在 student 实际访问的 activation geometry 中寻找 PCA 方向并施加定向扰动，使 diversity control 从采样时刻移入内部表示。扰动器只拥有候选多样性，生成模型仍拥有输出，独立 evaluator 决定 fidelity 是否可接受。它增加方向校准、存储、层选择和 distribution drift 风险；几何失配或扰动破坏 alignment 时，应关闭该分支并回退原 student、多步 sampler 或外部 best-of-N。exact-v1 只支持作者模型和指标下的 diversity-fidelity Pareto，不证明存在通用 diffusion manifold 或端到端时延优势。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11494 -->

### 复杂视觉生成需要显式 Plan、Predicate 与 Retry Budget

一次生成在对象、计数、属性和关系较多时难以同时满足全部约束。更可控的路径先把 prompt 编译为 typed visual program，再由 verifier 对每个 predicate 产生 evidence，controller 据失败类型选择局部 edit 或 resample；program 拥有待满足合同，verifier 不拥有事实真值，最终 acceptance 仍由独立 gate 提交。可定位修复换来 parse error、verifier blind spot、循环和额外生成成本；错误 program 还会稳定优化错误目标。无法可靠分解或验收时，应回退 single-pass/best-of-N、人工检查和最大 retry/cost budget。exact-v1 只证明披露 predicate 与 benchmark 范围，不覆盖开放世界事实和任意 prompt。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11722 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06667:start -->
### Camera 与 Motion Condition 可以在 Denoising 中分阶段交接

固定 camera 或 pose-only control 在单主体、镜头简单时更稳定；同时强加 pose 与 depth 到所有 denoising step，可能在后期把局部运动和高频细节过度约束。一个条件分支让早期 pose+depth 锁定 global geometry，后期只保留 pose，使 camera/depth control 在粗结构收敛后交还给 motion/detail generator。Condition scheduler 只拥有约束强度，生成状态仍由 denoiser 更新，独立几何与运动 gate 决定是否接受。

分阶段控制改善相机遵循与动作自由度的取舍，也会引入 pose/depth 校准误差、切换时刻敏感、遮挡和多角色冲突。现有证据只覆盖固定 backbone、作者 benchmark 与 human preference，不证明真实 3D consistency。输入对齐或 schedule 失稳时，应回退 pose-only、固定 camera 或训练式 controller。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06667:end -->

### Diffusion RL 的 Credit 可以沿 Denoising Trajectory 分配，但 Reward 仍须可验证

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15458:start -->
只对最终视频打分的 RL 在 evaluator 可靠、生成步数少时实现简单，却无法指出哪一段 denoising trajectory 破坏了全局结构。SDE-GRPO 把 flow/diffusion 采样写成随机轨迹，在组内比较结果并将 credit 分配回中间步骤；对 maze、FlowFree、Sokoban 这类可由程序验证的任务，还可提高早期步骤的权重，因为全局布局通常先于局部纹理形成。sampler 拥有生成 trajectory，reward program 拥有任务判定，step schedule 只拥有 credit weighting。

更密 credit 以额外 rollout、轨迹存储和方差估计为代价；早期加权会牺牲局部质量，并可能让模型利用 verifier 漏洞。exact-v1 的 §4.1–4.3、§5.1–5.4、§6.1–6.3、§7 与 Appendix C.1 只支持这些程序可验证任务，不证明开放视频语义或人类偏好同样可分解。reward 不可验证、trajectory 成本过高或局部质量回归时，应回退监督训练、固定 schedule 或仅在终态使用独立 evaluator。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15458:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22967:start -->
长 denoising trajectory 的端到端反传保留完整依赖，却让显存和计算随展开长度增长。Learned relay state 可以在
阶段边界压缩前段信息，再对后段执行 truncated BPTT；它把优化压力从保存全部状态转成维护 relay-interface
fidelity 与 stage revision。收益是有界反传窗口，代价是未编码依赖丢失、阶段兼容和额外 relay compute。作者
实验不证明任意 diffusion process 都能无损截断；relay validation 或跨阶段一致性失败时，应回退 full backprop、
更短 unroll，或使用可检查的静态显式 state。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22967:end -->

### Velocity Decomposition 以周期性 Full Forward 约束近似误差

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23381:start -->
每个 denoising step 完整前向最容易保证状态一致，却重复计算变化缓慢的分量；velocity-decomposition 分支在周期性 full-forward anchor 之间估计中间 step，把 anchor interval 与估计状态写入 sampler identity。近似只拥有 proposal，误差 Gate 决定是否继续复用。

减少前向次数会换来累积误差、interval 调参与分布漂移。exact-v1 只支持作者模型、schedule 和测量；误差超界、场景变化过快或质量回归时，应缩短 interval，最终回退完整 denoise。arXiv:2605.23381v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23381:end -->

### SDE-consistent RL 必须绑定 Exploration 与 Finite-step Transition

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23522:start -->
只优化 ODE 或终态 reward 时路径简单，但不能显式控制随机 exploration；SDE-consistent 分支把 exploration schedule、有限步 transition 和 reward rollout 共同版本化，使训练采用的随机过程与实际 sampler 更一致。Reward 仍只评价披露目标，不能替代生成正确性的独立 Gate。

随机轨迹提高探索，却增加方差、稳定性和近似误差。exact-v1 只支持作者假设、sampler 与实验；transition 近似失真、方差失控或质量退化时，应回退 ODE、既有 sampler 或监督训练。arXiv:2605.23522v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23522:end -->

### 连续 Latent 与离散 Token 需要分别拥有版本

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23605:start -->
纯 masked diffusion 直接在 token state 上修正，接口单一但可能承担过重的全局组织；latent-augmented 分支先由 autoencoder 压缩，再用 latent prior 与 few-step distillation 生成全局状态，最后由 discrete decoder 还原 token。AE、prior、distillation 和 decoder 是可独立失败的 artifact，不能合并成一个模型版本。

分层表示减少部分生成步数，却会新增 reconstruction loss、跨阶段漂移和 decoder 幻觉。作者实验不证明连续 latent 对所有文本任务更优；latent 失真、decoder 不忠实或联合校准失败时，应回退纯 masked diffusion、更多 steps 或自回归解码。arXiv:2605.23605v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23605:end -->

### Entity-centric Video Memory 把对象身份与帧历史分离

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23610:start -->
保留完整 frame history 在短视频中最可靠，长度增加后成本随时间增长；entity-centric 分支用 entity ID、latent patches、update budget 与 shot script 维护可寻址对象状态。它解决“对象是谁、何时更新”，不等于已经证明物理世界的因果一致性。

稀疏对象记忆降低历史成本，却会引入 identity swap、关系丢失和脚本先验偏差。exact-v1 只支持作者视频与 evaluation；对象身份不稳、关系回归或场景超出脚本时，应回退 keyframe/full-frame history 或扩大可见窗口。arXiv:2605.23610v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23610:end -->

### Pixel Diffusion Decoder 需要独立的重建与预算 Gate

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23902:start -->
VAE decoder 在 latent 表示稳定时便宜，但高分辨率细节可能受固定重建器限制；generative pixel decoder 可以把 latent revision、sigma-aware conditioning、pixel sampler 与 early termination 写成独立 decode artifact。停止规则只提出完成候选，重建质量和预算 Gate 决定是否提交。

生成式 decoder 提高细节自由度，却增加采样成本、随机性与高分辨率稳定性风险。作者实验只支持披露模型与最高分辨率条件；重建、时延或内存越界时，应回退 VAE decoder、cascade 或较低分辨率路径。arXiv:2605.23902v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23902:end -->

### Metric-geometry Reward 只能提出几何改进方向

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23903:start -->
单一视觉 reward 容易混合 rotation、translation 与外观质量；metric-geometry 分支把几何分量分账，并让 3D estimator 产生 reward proposal。Estimator 不拥有真实几何，最终仍需传感器、可执行约束或独立几何 Gate。

更细 reward 改善 credit assignment，却可能被 generator 利用 estimator 漏洞，或在域外相机和场景上失配。exact-v1 只支持作者数据、GRPO 和 estimator；sensor 不可靠、几何回归或 reward hacking 出现时，应回退 SFT、确定性几何检查或不启用该 reward。arXiv:2605.23903v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23903:end -->

## Review notes

- `SF-2026-ARXIV-2605-04291`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.04291v1) 支持用预训练 causal/masked LM 的条件分布定义 Glauber-style 局部重采样，并以多轮 revision 换取全局纠正；有限步 sampler 不证明 stationary convergence，训练/NFE 成本、streaming 与生产 SLO 也未被普遍证明。
- `SF-2026-ARXIV-2605-06885`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.06885v1) 支持在同构 Qwen3 模型和作者代码任务中以逐层表示对齐辅助 AR→masked-diffusion 迁移；不证明行为等价、跨架构迁移或普遍质量优势。

- 2026-09-01 可变 canvas 的状态绑定：<https://arxiv.org/html/2608.30922v1> §3.2、Algorithm 与 C–F。平均 JS 不覆盖已提交/新增位置，不构成无损证明；always-expand 对照同时改变判定和 expanded forward，不能隔离 JS 判定因果。三模型四任务及 MI210 测量不外推生产 SLO。

- `SF-2026-ARXIV-2609-04531`，Status: Experimental：exact-v1 §2.4、§3.1/3.3、§5与B.5支持student中间轨迹监督及按K分别训练的少步分支。仅采用公开代码生成设置下的机制；不采用任意权重下稳定反向映射保证，也不把K、NFE与wall-time等同。https://arxiv.org/html/2609.04531v1

- `SF-2026-ARXIV-2602-00612`（Status: Experimental）：primary=`arXiv:2602.00612v1`；Method=`§3 Methodology`；Evaluation=`§4.1 Benchmark`；Non-proof=`§7 Conclusion`。证据只支持 dLLM 在所测 CFG benchmark 中用并行位置分布做 lookahead、拒绝不可完成 proposal；不证明语义正确、任意 grammar 复杂度或生产延迟。
- `SF-2026-ARXIV-2602-21760`（Status: Experimental）：primary=`arXiv:2602.21760v1`；Method=`§4.2 Hybrid Parallel Inference Framework；§4.3 Adaptive Switching via Denoising Discrepancy`；Evaluation=`§5.2 Main Results`；Non-proof=`§5.3 Ablation Study`。证据绑定 SDXL/SD3、作者实现与双 RTX 3090，不证明其他 diffusion family、拓扑、并发和 tail-SLO。

- `SF-2026-ARXIV-2602-19161`（Status: Experimental）：exact-v1 的 §3.1～3.3 定义 VAE decoder pruning、operator optimization 与三阶段 distillation，§4.1～4.3 及 Appendix B.2～B.3 给出作者质量、消融与 pipeline latency，§5/Impact Statement 不证明跨 decoder、分辨率、frame count、硬件或端到端生成等价。https://arxiv.org/html/2602.19161v1

- `SF-2026-ARXIV-2606-22370` — primary `arXiv:2606.22370v1`；Method=`arXiv:2606.22370v1 §3 Method`；Evaluation=`arXiv:2606.22370v1 §4 Experiments`；Non-proof=`arXiv:2606.22370v1 §5 Conclusion and long-single-shot scope`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Vision as Unified Multimodal Generation（typed unified output contract；Status: Experimental）:
  https://arxiv.org/abs/2607.06560v1
- Explorative Modeling（多候选匹配与 selection-conditioned training；Status: Experimental）:
  https://arxiv.org/abs/2607.27372v1

- Amazon Science TTS planning/validation engineering evidence（Status: Experimental；Artifact Not Available）:
  https://www.amazon.science/blog/improving-quality-and-robustness-in-llm-based-text-to-speech-systems
- DMax（self-revising diffusion decode；Status: Experimental）: https://arxiv.org/abs/2604.08302
- Think in Strokes（interleaved visual generation workflow；Status: Experimental）:
  https://arxiv.org/abs/2604.04746

LLaDA2.1 与 ProSeCo 支持“并行草拟暴露错误累积后，引入 editable/correction state”的相邻分支；DDTree 支持“一次 block-diffusion marginal breadth 可用于构造受预算约束的验证树”；Multi-Block Diffusion 仅作为实验性 block-level 分支。Focus-dLLM 支持“预测下一步会变化的位置 → selective state refresh + dynamic sink preservation”的受限 cache 分支，但其 confidence 不是 cache-validity 概率，也不能外推到 AR Decode。DDiT 支持“multi-shape artifact 先于 adaptive runtime policy”的受限机制，但 threshold 表与两组 headline speedup contract 存在内部矛盾，精确收益保持 `Disputed`。SenCache 支持 sensitivity-bounded approximation cache 的受限分支，但其 calibration、quality metric 与单硬件 latency contract 不能外推到生产 serving。这些工作均不证明 Diffusion 会普遍替代 AR。

dLLM framework 进一步说明，统一软件抽象不等于抹平生成语义。跨 MDLM、BD3LM 或其他 diffusion-LM pipeline
复用 API 时，可交付 artifact 仍需绑定 sampler、noise/remask schedule、parallel commit ordering、EOS/padding、
cache approximation 与 framework revision；否则同名 checkpoint 在两个 runtime 中可能不是同一生成过程。
框架减少 recipe duplication，却新增 adapter semantic drift 与默认参数误用。原作者 pipeline 在新 objective、
特殊 post-processing 或框架尚未覆盖的机制上继续合理；本章吸收的是 generative-process artifact identity，
不把 dLLM 的作者结果外推为 diffusion-LM 的通用收益。

- Focus-dLLM（confidence-guided mutable-state refresh；Status: Experimental）: https://arxiv.org/abs/2602.02159

- LLaDA2.1: https://arxiv.org/abs/2602.08676
- ProSeCo: https://arxiv.org/abs/2602.11590
- DDTree: https://arxiv.org/abs/2604.12989
- Multi-Block Diffusion Language Models: https://arxiv.org/abs/2606.29215
- Wan-Streamer（state-preserving thinker/performer pipeline；Status: Experimental）:
  https://arxiv.org/abs/2606.25041
- Diffusion Templates: https://arxiv.org/abs/2604.24351
- DDiT: https://arxiv.org/abs/2602.16968
- SenCache: https://arxiv.org/abs/2602.24208
- dLLM framework（generative-process artifact identity；Status: Experimental）:
  https://arxiv.org/abs/2602.22661

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27732 — primary arXiv:2606.27732v1; exact-v1 URL=https://arxiv.org/html/2606.27732v1; Method=https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference; Evaluation=https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks; Non-proof=https://arxiv.org/html/2606.27732v1 — §5 Conclusion。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-13426:start -->
- `SF-2026-ARXIV-2606-13426` — Daily `2026-06-12`；primary `arXiv:2606.13426v1`；Books review `books-review:SF-2026-ARXIV-2606-13426`。

  **已吸收的语义增量：** diffusion model 的 speculative block proposal 必须由 target-model block verifier统一 commit/rollback，才能把并行候选与 exact output distribution 分开
<!-- daily-books-trace:SF-2026-ARXIV-2606-13426:end -->

- `arXiv:2609.01043v1`（2026-09-02 Daily）：[§4.1、Appendix A](https://arxiv.org/html/2609.01043v1)支持 input-overlay-only 与 mutable noisy state、final argmax 的区别；stored label 不直接复制到输出。§4.2–4.3的oracle/条件独立理论不认证 learned sampler 闭环无偏，§5及Appendix D的GenPPL/entropy排序不等任务正确率或线上latency；仅吸收三类state/commit接口边界。

<!-- daily-books-trace:SF-2026-ARXIV-2606-13496:start -->
- `SF-2026-ARXIV-2606-13496` — Daily `2026-06-12`；primary `arXiv:2606.13496v1`；Books review `books-review:SF-2026-ARXIV-2606-13496`。

  **已吸收的语义增量：** diffusion serving cache 应把 denoising step、state identity 与误差预算绑定，在 step-level reuse 与 recompute 间动态选择
<!-- daily-books-trace:SF-2026-ARXIV-2606-13496:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15805:start -->
- `SF-2026-ARXIV-2606-15805` — Daily `2026-06-15`；primary `arXiv:2606.15805v1`；Books review `books-review:SF-2026-ARXIV-2606-15805`。

  **已吸收的语义增量：** discrete diffusion并行commit需用pairwise compatibility修正marginal confidence，避免独立高置信token组成冲突configuration
<!-- daily-books-trace:SF-2026-ARXIV-2606-15805:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06560:start -->
- `SF-2026-ARXIV-2607-06560` — Daily `2026-07-08`；primary `arXiv:2607.06560v1`；Books review `books-review:SF-2026-ARXIV-2607-06560`。

  **已吸收的语义增量：** 新增证据边界：Convert heterogeneous annotations into a shared sample contract—visual inputs, natural-language task/schema instruction, and a text/image/mixed response that can be deterministically decoded back into boxes, masks, dense maps or camera records—so one generative model can learn many vision tasks without task-specific heads. 该 delta 已进入 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L183`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06560:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.27372:start -->
- `SF-2026-ARXIV-2607.27372` — Daily `2026-07-31`；primary `arXiv:2607.27372v1`；Books review `books-review:SF-2026-ARXIV-2607.27372`。

  **已吸收的语义增量：** 新增证据边界：Explorative Modeling factors the training loop over multiple candidate matches and trains on the selected match, making sampling during training closer to inference-time mode commitment. Exploration becomes a third compute axis, but multiplies candidate-generation cost and introduces selection bias; author scaling curves do not prove a universal replacement for AR or diffusion. 该 delta 已进入 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L211`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.27372:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24841:start -->
- `SF-2026-ARXIV-2607-24841` — Daily `2026-07-29`；primary `arXiv:2607.24841v1`；正文锚点“Parallel Progress 与 Active Compute 是两条独立成本轴”。
  证据限翻译任务与作者 neuromorphic setting，不支持跨平台能量、普通 GPU 或生产 SLO 外推。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24841:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25157:start -->
- `SF-2026-ARXIV-2607-25157` — Daily `2026-07-29`；primary `arXiv:2607.25157v1`；正文锚点“AR 权重可以成为 Masked Diffusion 的兼容起点”。
  证据限 matched GPT-2 Medium/WikiText 与所测长度/迁移设置；同规模 tuned AR 仍更强，不支持替代结论。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25157:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25948:start -->
- `SF-2026-ARXIV-2607-25948` — Daily `2026-07-29`；primary `arXiv:2607.25948v1`；正文锚点“Any-to-any AR 把 Modality Type 移入同一生成序列”。
  证据限作者任务中的 specialist/multitask 与 chained-generation 对比；自生成跨模态评分不是独立 verifier。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25948:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-26004:start -->
- `SF-2026-ARXIV-2607-26004` — Daily `2026-07-29`；primary `arXiv:2607.26004v1`；正文锚点“Few-step Distillation 要在 Student 实际访问的状态上验收”中的 multi-step proposal 分支。
  证据限作者披露模型与 4–8 NFE 设置；NFE 不等 wall time，也不证明跨域稳定或消除 mode collapse。
<!-- daily-books-trace:SF-2026-ARXIV-2607-26004:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2605-02263:start -->
- `SF-2026-ARXIV-2605-02263` — Daily `2026-05-05`；primary `arXiv:2605.02263v1`；Books review `books-review:SF-2026-ARXIV-2605-02263`。

  **写回边界：** fixed block size 增加 learned-boundary 条件分支，但 boundary 只是待 runtime 冻结和验证的 proposal；entropy trajectory 不证明 correctness，静态 shape 或阈值失配时仍使用固定 block。
<!-- daily-books-trace:SF-2026-ARXIV-2605-02263:end -->
