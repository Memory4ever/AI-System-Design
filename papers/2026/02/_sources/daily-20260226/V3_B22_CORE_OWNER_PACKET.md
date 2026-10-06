# B22 — 六项必要原证 / actual owner；本次独立复核已落实

2026-10-06 feb26_close_oct06 非原packet作者实际重新定位各raw全部pID，无缺失；20370原§3.3p8全构造、20567原Eq41/52 TeX与spectral身份、20585原Definition4/§3.1、20646原Eq23 conditional bias/fourth moment式另核。actualCh4capacity/优化/泛化及表达效率、Ch26命令/latent/更新时钟、Ch36共识条件、Ch23本次已移161–163的formation/readout/routing、Ch28Update/Numerical与trace分别核。20517/20646具体已有覆盖；20370/20624/20585受限构造/输出诊断/分布条件仅报告，不复制有限recipe或授其它proof；20567具体uniform时间常数/非正规矩阵条件不足隔离显式稳定/泛化rate，保有限经验与重开材料。不自修λ/公式、不改Books，原费用/人口/反侧/ND保留，未运行artifact/复现，非日级验收。

## 2602.20370v1
https://arxiv.org/html/2602.20370v1

S3.SS1.p5.1 | In particular, in the case that K=\Omega^{n} we have that (13) holds with d_{\text{intrinsic}}=nd . Under the mild assumption that n\geq 4 we have that nd\geq 2d+2 for all d , and so Corollary 3.1 implies that on the class of \alpha -Hölder continuous functions in dimension D=dn , Deep Sets matches up to a logarithmic factor the optimal approximation rates for general ReLU MLPs (see for instance Siegel (2023); Yarotsky (2018); Shen et al. (2022)). This indicates that there is no loss of expressivity when using the Deep Sets architecture to enforce permutation invariance.

S3.SS3.p5.1 | We now show that a Transformer Network (Definition 4) can be constructed to compute the expression \rho\left(\Phi(x_{i}),\sum_{j\in[n]\setminus\{i\}}\Phi(x_{j})\right) from Corollary 3.2. We follow the constructive proof from Alberti et al. (2023) (Appendix B), modifying it to compute the ‘omit-one’ sum directly. The target expression is \rho(\Phi(x_{i}),\Sigma_{\Phi}^{\setminus i}) , where \Sigma_{\Phi}^{\setminus i}=\sum_{j\neq i}\Phi(x_{j}) .

S3.SS3.p8.6 | Let Z_{i}=[1,x_{i},\Phi(x_{i}),\Sigma_{\Phi}-\Phi(x_{i})] be this resulting vector. This vector Z_{i} contains both the ‘self’ embedding \Phi(x_{i}) and the ‘omit-one’ sum \Sigma_{\Phi}^{\setminus i}=\Sigma_{\Phi}-\Phi(x_{i}) .

## 2602.20517v1
https://arxiv.org/html/2602.20517v1

S3.SS2.SSS2.p3.1 | The training process for the inner speech generator implements a learning-based internalization of linguistic structure. Central to this process is the use of vision-language models (VLMs) to provide external linguistic scaffolding. The VLMs generate initial descriptive characterizations of demonstrated behaviors, providing explicit linguistic structure that serves as training targets for the CVAE. We model the agent’s inner speech m as linguistic descriptions of behavior. For each demonstration in our dataset, we obtain a sequence of T images (\mathbf{I}^{(i)}_{1},\mathbf{I}^{(i)}_{2},\cdots,\mathbf{I}^{(i)}_{T}) , which are converted into a GIF where T is the task horizon. We then use a VLM to generate descriptive external speech that characterizes the behavior by passing k=8 randomly picked GIFs with the prompt:

S3.SS2.SSS2.p7.1 | Algorithm 2 (Appendix A): Simulation. During simulation, the agent must generate its own inner speech based on its ongoing behavior. To enable this, we use the CVAE decoder \Psi_{\text{dec}} to generate the inner speech given the images of the past actions. We employ the W-step update cycle described in Section 3.1.3 for this purpose. We also wait for t_{0} timesteps before the first generation. Thus, starting from a null speech of m\leftarrow 0 , a new inner speech is generated periodically using \Psi_{\text{dec}} after every W timesteps starting from t=t_{0} . The framework enables explicit control over agent behavior through linguistic prompts, realizing the linguistic controllability aspect of the theoretical framework. The description \mathcal{B} of the desired behavior overrides the initial inner speech from m\leftarrow\mathbf{0} to m\leftarrow\mathcal{B} . The agent then continues its periodic updates to be consistent with the trained inner motivation space.

S4.SS2.SSS3.p3.1 | Vision-language model. We study the effect of changing the VLM from GPT-4o to o4-mini, 4o-mini, and Qwen (Qwen2.5-VL-72B-Instruct). Figures 4(c) and 4(d) show that GPT-4o gives the best success rate compared with other VLMs, followed closely by the open-source Qwen model. Surprisingly, we find o4-mini to lack in success rate even though its descriptions lead to the most diversity (highest entropy). We believe this is due to the CLIP model failing to distinguish the nuanced behaviors generated using o4-mini. More importantly, we find that in all cases, MIMIC outperforms the BC model in success rate and often increases the base entropy in all cases except Qwen. This is likely due to a lack of diversity in Qwen generated descriptions of the dataset.

A6.p2.1 | Inference. Let T_{CVAE} and T_{diff} denote one forward pass through the CVAE and diffusion models, respectively. Over a simulation horizon H with window size W , we perform H diffusion passes and H/W CVAE passes, yielding a total complexity of O(HT_{diff}+H/WT_{CVAE}) ). Since both are vision-conditioned with similar runtimes and H>H/W , the diffusion term dominates. So, MIMIC adds no inference overhead.

## 2602.20567v1
https://arxiv.org/html/2602.20567v1

S6.p2.1 | Several directions remain open for future investigation. First, extending the current analysis to more general non-convex settings beyond the PŁ condition would further broaden the applicability of the theory. Second, it would be of interest to study adaptive or time-varying communication topologies, where the imbalance and spectral properties evolve over time. Finally, incorporating additional practical considerations such as communication compression, quantization, or partial participation into the stability-based framework may provide deeper insight into the generalization behavior of decentralized learning systems in realistic environments and large-scale deployments.

A2.SS2.p2.1 | Let \lambda be the spectral radius of \bm{H} , which satisfies \lambda0 such that, for the induced \infty -norm,

A2.SS2.p9.2 | where we used that \sum_{s=0}^{t-1}\gamma_{s}\leq\sum_{s=0}^{t-1}\lambda^{t-s}\gamma_{s}/(\min_{1\leq k\leq t}\lambda^{k}) and absorbed into C^{\prime} .

B.2 Eq41/52 原 TeX，中心限定问题而非自修：
\|\bm{H}^{t}\|_{\infty}\leq C_{H}\lambda^{t},\quad\forall t\geq 0.
\sum_{s=0}^{t-1}\gamma_{s}\leq\sum_{s=0}^{t-1}\lambda^{t-s}\gamma_{s}/(\min_{1\leq k\leq t}\lambda^{k})

## 2602.20624v1
https://arxiv.org/html/2602.20624v1

Sx2.SSx1.p2.1 | The CREMA-D dataset includes videos of actors expressing specific emotions (i.e., happy, neutral, sad, angry, disgust, and fear) against a green screen with synchronized audio. It offers a multi-layered annotation structure: the intended emotion (the emotion actors were instructed to display, single-label) and perceived emotions labeled by humans across three conditions: multimodal-perceived (original video with audio), visual-perceived (video-only without audio), and audio-perceived (audio-only without video). Perceived emotion labels are multiple when multiple emotions receive equal vote counts. Each sample was rated by an average of 9.8 annotators, with over 95% of samples receiving at least 8 independent evaluations. The dataset includes 7,442 samples frm 91 actors, all of which were used in our experiments.

Sx2.SSx2.SSSx1.p4.1 | We then apply a systematic prompt-based perturbation strategy (Khanmohammadi et al., 2025), in which models are instructed to perform classification while being explicitly prohibited from selecting subsets of emotion labels (removing one, two, three, or four labels at a time). This procedure reveals a hierarchical structure of error attractors: when preferred labels are removed, models consistently fall back to secondary or tertiary choices rather than redistributing errors uniformly.

Sx2.SSx2.SSSx2.p2.1 | For Qwen2.5, Face+Voice errors closely track those of Face-only input, whereas Voice-only errors exhibit distinct, weaker attraction patterns. For Gemma 3n, this asymmetry is even more pronounced: although Voice-only inference shows extremely strong Neutral bias under failure, this bias is almost entirely absent from Face+Voice inference, which instead mirrors Face-only behavior. In effect, the presence of video information suppresses, rather than integrates, the bias structure induced by audio.

Sx3.SSx1.p2.3 | where connectivity a_{ij}^{(\sigma)} and a_{ij}^{(\sigma,\sigma^{\prime})} encode structural constraints imposed to the semantic network. Based on observations that token representations in LLMs exhibit highly organized structures characterized by small-world topology (Geshkovski et al., 2023; Geshkovski et al., 2025; Bruno et al., 2025; Liu et al., 2025), the connectivity is modeled using a Watts–Strogatz network with rewiring probability p=0.01 and degree k=10 . Within the structural constraints, the oscillators interact with attention weights

## 2602.20585v1
https://arxiv.org/html/2602.20585v1

Thmdefinition4.p1.1 | Let \mathcal{X} be a measurable space. Fix a measure \mu_{0} on \mathcal{X} and a non-decreasing function \rho:[0,1]\to\mathbb{R}_{+} with \lim_{\epsilon\to 0}\rho(\epsilon)=0 . A family of distributions \mathcal{U} on \mathcal{X} is said to be (\mu_{0},\rho) -generalized smoothed if for any distribution \mu\in\mathcal{U} and measurable set A\subseteq\mathcal{X} ,

S3.SS1.p2.1 | It is easy to see that generalized smoothness implies existence of uniform covers for all VC classes. Indeed, if \mathcal{U} is generalized smooth with respect to some reference measure \mu_{0} and tolerance function \rho , then for any \epsilon>0 , using a covering for \mathcal{F} under \mu_{0} at scale \delta=\rho^{-1}(\epsilon) yields a uniform cover at scale \epsilon for all distributions in \mathcal{U} . We record this formally as Lemma 20.

S3.SS1.p3.1 | A distribution class admitting uniform covers for a class \mathcal{F} is also sufficient for achieving low regret if the adversary is oblivious and the distribution class \mathcal{U} is known. Indeed, as observed in [23], a standard Hedge algorithm run on the uniform cover \mathcal{F}_{\epsilon} ensures regret at most \epsilon T+O(\sqrt{T\log|\mathcal{F}_{\epsilon}|}) against any oblivious \mathcal{U} -constrained adversary. But, to the best of our knowledge, there is no known direct way to extend this to the adaptive adversaries setting or the case when \mathcal{U} is unknown, without using the machinery of the coupling lemma introduced by [22] (which requires stronger assumption on the distribution class than just uniform covers).

Definition4 完整原 TeX：
\displaystyle\mu(A)\leq\rho(\mu_{0}(A))\quad\text{for all measurable sets }A.

## 2602.20646v1
https://arxiv.org/html/2602.20646v1

S3.SS3.p4.1 | We emphasize that Assumption 3 is not an algorithmic constraint: throughout the paper we analyze the plain SGD update in (5d) without projection or clipping. That said, Assumption 3 can be interpreted locally: it suffices for the stated regularity bounds to hold on a compact region containing the iterates and intermediate states visited during training. Such compactness can arise, for example, from finite data combined with bounded parameter regimes, explicit projection to a compact set, or standard clipping/normalization practices. Our goal is to isolate the effect of forward/backward perturbations; incorporating such safeguards would only strengthen stability in practice. Finally, we make the following assumption of the Polyak-Łojasiewicz (PL) condition [47] for \ell(\boldsymbol{w}) :

S4.p6.1 | Lemma 2 bounds the second moment of the bias introduced by forward perturbations. Specifically, the squared deviation of the conditional expected gradient is controlled by two terms: the squared norm of the expected forward error \mathbb{E}^{\mathcal{G}_{i-1}}_{t}[\tilde{y}_{i-1}^{(t)}-y_{i-1}^{(t)}] and the fourth moment of the forward error \tilde{y}_{i-1}^{(t)}-y_{i-1}^{(t)} . Building on this result, we derive an upper bound for the second moment of the overall bias as follows.

S7.SS2.SSS1.p3.1 | For zero-mean forward perturbations, however, the behavior depends on the perturbation magnitude. Figure 4 (left) indicates that for small perturbation levels the stable gradient norm still decreases with \gamma , but once the forward perturbation magnitude becomes non-negligible (e.g., \sigma_{f}\geq 0.5 ), the stable gradient norm saturates at a nonzero plateau even as \gamma\to 0 . This plateau is further corroborated by the trajectories in Figure 3 (left) under \sigma_{f}=1.0 , where shrinking \gamma yields little improvement. This behavior illustrates the forward/backward asymmetry in Remark 4 (see also Remark 3): unless the forward perturbations satisfy the stricter decay conditions in Corollary 1, the bound predicts a non-vanishing plateau even as \gamma\to 0 .

Theorem2 Eq23 的原 TeX两侧；条件均值与fourth moment分开：
\displaystyle
\displaystyle\mathbb{E}\left[\left\|\mathbb{E}_{t}[\tilde{\boldsymbol{u}}^{(t)}-\boldsymbol{u}^{(t)}]\right\|^{2}\right]
\displaystyle\leq
\displaystyle\sum_{i=1}^{N-1}C_{\delta_{i}}^{b}\mathbb{E}\left[\left\|\mathbb{E}^{\mathcal{G}_{i}}_{t}[\delta_{i}^{(t)}]\right\|^{2}\right]+\sum_{i=1}^{N-1}\tilde{C}_{\delta_{i}}^{b}\mathbb{E}\left[\left\|\delta_{i}^{(t)}\right\|^{4}\right]+\sum_{i=1}^{N-1}C^{b}_{\varepsilon_{i+1}}\mathbb{E}\left[\left\|\mathbb{E}_{t}^{\mathcal{H}_{i+1}}[\varepsilon_{i+1}^{(t)}]\right\|^{2}\right]

## actual owner — books/part-01-worldview/04-why-models-learn.md

L41–47:
神经网络“能够学习”至少包含三个不同命题。

第一是 **representation capacity**：模型函数族里是否存在一个足够好的函数。Universal Approximation 一类结果讨论的是特定条件下的表示能力。它说明某些网络可以逼近一类函数，但不告诉我们需要多少参数、多少数据，也不保证训练算法能找到那组参数。

第二是 **optimization**：从当前参数出发，算法能否在可接受时间和资源内找到低训练损失区域。一个好解存在，不代表梯度下降一定到达；loss surface、初始化、数值精度、batch 噪声和学习率都会影响路径。

第三是 **generalization**：训练集上的低误差能否延续到未见样本。即使模型把训练集完全记住，经验风险也可以很低，但真实业务分布上的风险仍可能很高。

L342–348:
最完整的结论是：

> 线性层负责变换坐标，非线性让不同输入进入不同的局部计算区域，从而赋予网络通用函数逼近能力；深度再把这些非线性变换组织成可复用的层级组合，使某些复杂函数能够以远少于浅层网络的参数和计算来表达。

这条结论只关闭 representation-capacity 问题。梯度能否穿过深度、optimizer 能否找到解，属于本章前述
backpropagation/optimization 与第 17、28 章的稳定性问题；这些参数最终形成什么表示、为何泛化或失败，则由
下一章接手。

## actual owner — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

L139–143:
层级接口还需选择命令的抽象级别：语言 subgoal、目标像素点和 gripper/motion trace 对低层策略施加不同约束，并非把同一文字换一种编码。High-level 提议命令类型与内容，low-level 按该类型结合当前观测生成动作；[Steerable VLA 的受限机制](https://arxiv.org/html/2602.13193v1)提示要分别验收语义、空间 grounding、运动条件与更新时钟，像素点不自动成为 metric waypoint，更不取得安全 authority。人工 oracle 至少2秒一次的接口、外部 Gemini 的历史/推理和额外坐标调用都计入预算；oracle steering 与部分 progress credit 不是自主 episode success，也不能把不同调用周期和 reasoning budget 合为纯命令类型因果。部分任务与不推理基线反退、trace 分支部署不足时，保留可信语言命令、短 horizon policy、低层 controller 或人工接管，不从随机命令混训批准任意 abstraction switch。 <!-- source-family:SF-2026-ARXIV-2602-13193 -->

层级规划也可不在部署时解码整段文字计划，而把计划压入少量 latent，再给动作网络一个专门的消费接口。一个受限训练分支先由 teacher 的高低 reward 轨迹训练 student：latent 经 verbalizer 重建文字，在 warmup 后冻结 verbalizer，以偏好训练 latent，并加入答案特征与空间 waypoint 的辅助监督。动作适配阶段冻结 student，由其 spatial tokens 的早层 key/value 经投影作为 action cross-attention 的条件。文字 readback 是训练辅助目标，不证明 latent 忠实承载推理原因；投影的 KV 是跨模型 conditioning，也不是共享一份 autoregressive cache。<!-- source-family:SF-2026-ARXIV-2601-09708 -->

这一分支把文本解码成本前移到训练，部署可省去 verbalizer，但动作 policy、fresh observation 与 controller 的验收仍不能省略。Teacher 偏好、verbalizer 训练、空间监督和环境专门 action fine-tuning 都增加成本；latent 数量和选用层也需目标负载校准。作者的 LIBERO/RoboTwin 模拟控制与真实视频 QA 检查不同对象，QA 不等于实机动作成功或安全；7B 的部分 QA slice 退步，模型平均延迟也不包含已证的完整控制 deadline。计划条件失真、动作回归或成本不合算时，保留文本 teacher 的可审计计划、observation-only policy 与原低层 controller，不能以 latent 可读或更短授权执行。

## actual owner — books/part-04-training-system/36-distributed-training.md

L79–87:
该选择用参数多样性换额外优化状态与一致性复杂度，周期平均仍有通信，恢复不一致也会改变后续轨迹。证据只来自单推荐任务、单 epoch 设置，不证明 LLM 收敛或任意同步间隔有效；质量漂移、状态无法恢复或协调成本超过收益时，回退共同参数点的同步 SGD 或有明确 local-gradient 合同的 Local SGD。

去中心化的 adaptive local updates 还要明确通信的共识对象。每个节点可以保留自己的 momentum、二阶矩与本地参数，连续推进若干步后，只发送相对于已重构模型估计的压缩差值；邻居据此更新各自的模型估计，再作 gossip correction。被压缩的是模型重建增量，不是一个共同 Adam 的原始梯度；节点的 optimizer history 与邻居共识估计因此是两组需要分别恢复的状态。Checkpoint 必须绑定本地步数、moments、重建估计、compressor 与 mixing revision，否则只恢复参数会改变下一轮更新。

这减少同步与传输，却叠加 local drift、压缩误差和拓扑混合误差；有偏但 contractive 的压缩器也只有在相应假设下可用。作者的有界、独立无偏随机梯度、固定连通 mixing、特定 adaptive 参数及步长条件不覆盖任意 Adam、动态故障网络或重尾梯度。小型 GPT 的四 A100 与 CPU 视觉实验支持受限可执行性，通信轮数或字节节省不等于生产 wall-clock 加速。收敛偏离、估计不同步或恢复无法保持身份时，应缩短 local interval、减弱压缩或回退同步完整状态；下一章的 tensor partition 不能替本协议证明 optimizer 等价。

<!-- source-family:SF-2026-ARXIV-2604-09970 -->

另一种通信对象是可由共同随机种子重建的零阶更新，而非压缩模型差值。各节点共享初始化与 RNG 合同，仅传种子、标量方向导数及消息身份；收到未见消息就传播，并且每个节点只应用一次同一系数的扰动更新。连通且可靠送达、种子重建一致并完成去重时，所有更新最终以相同权重进入各节点，区别于 gossip 反复混合时的权重变化；这不保证任意时刻参数相同，延迟期间本地梯度仍在不同参数点求得。若扰动在共同低秩坐标中生成，还可先汇总坐标内标量再重建更新，减少逐消息应用的计算。消息日志、已应用集合、种子/初始化、低秩基及刷新轮次应进入 checkpoint/replay，不能仅恢复最终参数。[受限 SeedFlood 对照](https://arxiv.org/html/2602.18181v1#S3.SS3)的低维 payload 不等于全网成本与模型大小无关：转发跳数、重复包、参数重建和低秩刷新仍付费，延迟与 rank 设置也有反侧；FO 500 与 ZO 5000 步的局部比较及更新微基准不认证同预算训练提速。RNG 失配、丢包/replay 不完整、延迟漂移或低秩偏差失控时，保留同步完整更新、可靠日志恢复与有界 local steps，不由最终送达共识推出收敛或部署收益。<!-- source-family:SF-2026-ARXIV-2602-18181 -->

## actual owner — books/part-03-multimodal-world-models/23-multimodal-representation.md

L154–157:

没有专用连续 encoder，也不意味着感知计算消失了：它可能在共同 backbone 内逐层形成可读表示。这里应分别测试表示 formation、后续 readout 和跨模态 routing，而不是凭某层线性 probe 或几何相似就把它命名为完整 encoder。对固定任务/层/模态的扰动，可检查该局部表示是否为所测输出所需；necessary readout 与足以替代全部感知计算、删 token 或提前退出仍是不同命题。

[Virtual Encoders 的精确 v2 证据](https://arxiv.org/html/2609.26513v2)含有限 concept probe 与两个模型的单层 Gaussian 扰动、特定 yes/no 判定；没有 activation patching 的充分性验证，PCA 子空间定义也未证明 rotation 的因果作用。新增 probe、干预强度与多重比较有成本，音频/其他模型上的相关观察不能外推共同层号或部署可省计算。证据不支持时保持功能解释的 Unknown，继续 dedicated encoder + projector、完整视觉读路径和独立任务回归，不让 native 标签代替分段验收。<!-- source-family:SF-2026-ARXIV-2609-26513 -->

## actual owner — books/part-04-training-system/28-pretraining.md

L1315–1325:

| 信号层 | 主要观测 | 能支持的结论 | 不能单独证明 |
| --- | --- | --- | --- |
| Objective | training/validation loss、per-domain loss、PPL | 当前 objective 在声明的数据与 mask 上是否改善，是否出现过拟合或 domain divergence | 事实性、指令遵循、安全与产品任务质量 |
| Update | gradient norm、update-to-weight ratio、clipping frequency、optimizer moments | 是否存在爆炸、消失、异常 step 或 group-wise update 失衡 | 梯度方向是否代表正确数据与目标 |
| Numerical | non-finite count、loss scale、overflow/underflow、skipped step、activation/logit range | mixed-precision path 是否还能产生有限、可执行的 update | 有限数值是否与高精度 reference 足够等价 |
| Data | source/domain mix、effective tokens、duplication、length、mask、batch identity | 实际消费分布是否符合 data contract，异常 loss 能否定位到样本 | 数据本身是否无偏、真实、合法或覆盖部署长尾 |
| System | step time、tokens/s、memory、collective、straggler、ECC/Xid、retry | 计算是否持续推进，故障或降速来自哪个 runtime/resource path | 高 utilization 是否产生正确的参数轨迹 |
| Evaluation | held-out loss、capability/safety suites、sample review、scaling probe | 中间 checkpoint 的可观察能力、回退与趋势 | 未测分布上的最终泛化，或未来规模必然延续当前趋势 |

这些信号必须按 `run / checkpoint / step / data batch / rank` 对齐。一次 loss spike 与同一步的 gradient spike、异常 batch、loss-scale backoff、collective retry 或 device error 相关联，才可能把“现象同时发生”推进到可检验的根因假设。只看全局平均会把单个 domain、layer、rank 或 expert 的退化稀释掉；只看最细粒度指标又会产生噪声和监控成本，因此应保留 global trend、分层 slice 与按事件下钻三档视图。
