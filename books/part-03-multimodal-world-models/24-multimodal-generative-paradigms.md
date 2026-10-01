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

第 23 章给出了表示的重构和语义契约，本章还必须问一个不同的问题：**这种表示是否容易被当前生成路径逐步预测？**
视觉 encoder 的高维连续 latent 即使能重构图像，单个 latent token 的分布仍可能比低维 VAE latent 难建模。
在 teacher forcing 下，AR 看到真实历史；生成时却要以自己的连续预测作下一步条件，高维误差会随步骤进入后续条件。
因此，重构分数不能替代生成质量、误差滚动或推理成本的验收。

一种受限分支先校准 token 分布，再在训练时扰动真实历史，让预测器练习接住偏离数据流形的前缀；它以更复杂的
表示归一化和训练噪声换生成容错，却不能靠更低训练损失证明最终图像更好。若扰动不匹配真实 rollout、
生成质量仍落后或稳定性优先，沿用重构导向 VAE 仍是合理选择。[RAE-AR 的图像实验](https://arxiv.org/html/2604.01545v1)
只支持所测 encoder、AR 架构、训练设置与指标下的这条表示—生成张力；其消融中归一化单独使用并非总有益，
结果也不证明高维语义 latent 已普遍追平 VAE。<!-- source-family:SF-2026-ARXIV-2604-01545 -->

逐 token 概率可预测，还不等于部分 prefix 已能被质量 sensor 辨认。第 23 章的 coarse-to-fine 表示若经训练形成早期全局语义，可以把候选 prefix 重建成中间图，再用 verifier 保留 beam；grid/raster prefix 只覆盖局部，填补后的中间图可能误导评价，更适合完整 Best-of-N，或支付 lookahead 成本后再判断。因此 representation ordering、partial reconstruction 与 search protocol 必须一起选择，不能把任意一维序列称为语义有序。<!-- source-family:SF-2026-ARXIV-2604-15453 -->

这种搜索支付重复 detokenization、branching 与 verifier 成本；NFE 中一次生成和一次评判并不具有相同 wall-clock，多步 flow decoder 的重建甚至可能成为主要瓶颈。更多搜索也可能提高自身 verifier 分而降低外部质量，缺失的语义 prior 不能靠无限搜索预算普遍补回。ordered prefix 不稳定、解码成本无法摊销或 verifier 未在独立指标上验收时，保留普通 AR、完整 Best-of-N 或 grid/lookahead 路径。[SoTo 的受限图像比较](https://arxiv.org/html/2604.15453v1)支持这条选择条件，不证明视频、文本普遍受益，也不证明无需预训练的生成。

### Autoregressive 不必等于 Append-only Final Text

经典 AR 每步直接提交一个 final-order token，因此最容易 streaming 和复用 KV；要在前文中修改内容时，通常只能重新生成。一个条件分支是不再对“最终文本顺序”自回归，而是对可变 canvas 的 edit-history actions 自回归：`INSERT(token)` 写入当前位置，`MOVE(Δ)` 改变 cursor，`STOP` 提交当前 canvas。模型仍然保持单步 next-action interface，却可以回退并在中间插入内容；可修订性因此来自 action/state 表示，不来自并行 denoising。

这条分支使“AR 还是 Diffusion”不再是“只能追加还是能修改”的同义词，但交换的不是免费修订：解码仍在 action space 中串行，移动和冗余编辑会增加步数，训练依赖编辑轨迹，而 mutable canvas 使 prefix KV、可见输出和 rollback 都需要新 identity。当输出必须低延迟流式提交、编辑轨迹难以构造或平均 action count 不能覆盖修订收益时，普通 append-only AR 仍是更强的旧路径。`arXiv:2609.20830v1` 只支持其 cursor-action 机制、小规模 continuation 实验与作者评判协议，不证明大模型质量、长文档 editing、真实 serving latency 或对 diffusion 的普遍优势。

<!-- source-family:SF-2026-ARXIV-2609-20830 -->

### 视频 AR 可以分离帧内精确路由与跨帧记忆

对视频把所有历史 token 放进同一个 softmax，最忠实但跨帧成本随序列迅速增长；只保留压缩 recurrent state 又可能丢失当前帧细节。一个分层分支让帧内 token 继续使用 exact local softmax，同时以 linear recurrent memory 承载跨帧历史。关键的状态边界是：同一帧的所有 token 都读取相同的 pre-update memory，只有 clean forward 完成后才提交下一帧 state；否则帧内并行会被隐式执行顺序污染。

这条路径以更低跨帧成本换 memory drift、历史细节损失和新的 clean-pass commit 纪律。长程一致性不足、状态异常或任务依赖精细历史时，应回退 full attention、短窗口重算或两者混合。现有证据只支持作者的视频模型与受测数据，不证明 linear memory 能替代任意视频历史，也不授权 runtime 偷改帧边界。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-16579:start -->
视频自回归可以让帧内 softmax 保持精确，而把跨帧历史演进成在 clean pass 后提交的 recurrent memory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-16579:end -->

另一条流式视频分支不将所有历史立即压入同一 recurrent memory，而让近期帧保留局部窗口、较远帧在淘汰前先累积进线性 history state；局部窗口还可按 block importance 稀疏计算。状态移交次序是先更新历史统计、再释放原 KV，不能先淘汰后假设记忆已经保留。近期可寻址条目与压缩远期历史承担不同责任，固定大小统计不意味着任意旧帧细节仍可找回，也不是可控环境状态的证明。

把这一结构直接装入尚未形成稳定表示的少步生成器，可能压缩噪声并加剧漂移。因此训练可先用 dense attention 蒸馏，再启用 hybrid history/local paths；训练与推理共同采用相同 temporal position cap，并以同初始 noise 的 teacher rollout 对首步 latent 作正则。这个分支支付额外训练、teacher目标构建和历史近似成本，不是免费缩小窗口。作者 Wan1.3B、单 H100、832×480及30秒定量协议只支持所测质量/执行，长视频展示不证明无限稳定，更强 sparsity 也有退步。精细历史或位置外推验收失败时，应保留更长窗口、dense基线或重新训练；本章拥有生成状态迁移，第25章仍须另验 action-conditioned environment transition。

<!-- source-family:SF-2026-ARXIV-2604-10103 -->

## Diffusion 与 Flow Matching：用迭代更新组织生成状态

连续 diffusion 从噪声逐步 denoise；离散或 masked diffusion 从 mask/noise state 逐步恢复 token。每轮可以同时更新许多位置，因此 serial steps 不必等于 token 数。

它的优势不是“完全并行”，而是把串行维度从 output length 改成 denoising/refinement steps。代价包括：

- 多轮 full or block forward；
- 中间状态可变，cache reuse 更困难；
- streaming 前必须定义哪些 token 已 committed；
- 迭代 schedule 会影响质量、延迟和稳定性；
- likelihood、sampling exactness 和 stop condition 可能更复杂。

图像和视频往往容忍整体画面同时从粗到细修正，且用户不要求逐像素 streaming，因此 diffusion 的系统契约较自然。文本要求稳定前缀和低延迟流式输出，mutable tokens 的成本更明显。

### DDPM：从可采样的加噪过程得到训练目标

先固定数据空间与尺度；第23章决定 x_0 是像素还是 latent，这里把它当作干净样本，c 是条件。DDPM 选择逐步高斯加噪：beta_t 是第 t 步噪声方差，alpha_t = 1-beta_t，alpha_bar_t 是前 t 步 alpha 的乘积。由高斯组合可直接抽样任意噪声层级，无须训练时完整走过前向链：

```text
q(x_t | x_(t-1)) = N(sqrt(alpha_t) x_(t-1), beta_t I)
x_t = sqrt(alpha_bar_t) x_0 + sqrt(1-alpha_bar_t) epsilon
epsilon ~ N(0, I)
L_simple = E_(x_0,c,t,epsilon) ||epsilon - epsilon_theta(x_t,t,c)||^2
```

一次训练更新只需抽数据、时刻和噪声，让网络预测加入的 epsilon。这个常用简化损失对各时刻的权重不同于原始变分界，不能把普通噪声 MSE 直接叫作精确负对数似然。噪声 schedule、时间采样和预测参数化因此共同定义了目标，不是部署时可任意替换的标签。

采样时没有 x_0 可用。网络的噪声预测被换算成反向高斯均值，采样器从近似标准高斯的终态出发，依次更新：

```text
mu_theta = (x_t - beta_t / sqrt(1-alpha_bar_t)
                   * epsilon_theta(x_t,t,c)) / sqrt(alpha_t)
x_(t-1) = mu_theta + sigma_t z
z ~ N(0,I) for t>1; z=0 at the final sampling step
```

sigma_t 和时刻序列属于采样器配置。训练可随机抽一个时刻，不意味着部署能把整条反向链省成一次 forward；跳步、换方差或换求解器都需要重新验收。加噪分布、网络拟合与有限步采样各自可能引入误差，后文的少步、纠偏和缓存都建立在这三个对象已分清的前提上。

固定生成器并不意味着 reference conditioning 可以原样注入。风格与主体特征可能共享方向，直接删除全部 subject subspace 会连同风格一起丢掉；一个替代分支先识别受 style 支持的方向，再从其余内容方向中提议衰减，将细、中、粗粒度 residual 分别送入对应生成尺度，并在汇总后约束总注入范数。这分开了“选择哪些证据”“送到哪里”和“注入多少”三项职责；subspace overlap 只调节衰减，不能被解释为风格与主体已经语义解耦，feature-change cap 也不证明 semantic leakage 为零。

校准集合、reference coverage、子空间估计和注入计算都付费；按主体不同 appearances 构造的集合与一次复用设置之间仍有适配边界，不能假设任意 reference 通用。冻结 SDXL/InstantStyle 的受限对照以 CLIP 差值等代理测泄漏，而非匿名化或安全保证；完全不注入的低泄漏可能同时丢掉风格，收紧 cap 也会损伤主体指标。局部 reference/prompt 与 disjoint stress tests 不替任意生成分布认证，完整运行成本、精度和 SLO 未披露。校准失配或内容/风格回归时，保留普通 prompt、原 adapter 或已验收的更保守过滤，而不由残差范数自签语义保真。 [必要机制与反证](https://arxiv.org/html/2609.21242v1)。<!-- source-family:SF-2026-ARXIV-2609-21242 -->

### Flow Matching：先指定概率路径，再学习移动方向

另一种构造直接规定噪声到数据的概率路径，并回归沿路径移动的 velocity。为避免与上面的 DDPM 时间方向混淆，这里使用 s：s=0 是噪声，s=1 接近数据。取独立噪声 epsilon、干净目标 y 和小的正数 sigma_min，一条易采样的条件路径是：

```text
a_s = 1 - (1-sigma_min) s
X_s = a_s epsilon + s y
u_target = dX_s/ds = y - (1-sigma_min) epsilon
L_CFM = E ||v_theta(X_s,s,c) - u_target||^2
```

sigma_min>0 时终点仍含少量噪声；趋近零才得到常见的噪声—数据直线插值极限。训练知道 y 和 epsilon，所以目标可计算；部署只见当前 x、s 和条件 c。平方回归在给定当前状态后学习条件目标的平均速度，在论文的密度与正则条件下，这与匹配边际概率路径的目标有相同参数梯度，而不是要求模型复原每个训练配对。

生成时从噪声开始积分 `dx/ds = v_theta(x,s,c)`；最简单的 Euler 更新是 `x_(s+ds) ≈ x_s + ds * v_theta(x_s,s,c)`。训练配对走直线，不代表平均后的速度场沿每条生成轨迹也笔直，更不保证一步积分准确。Flow Matching 是训练目标与路径构造，ODE solver 是数值执行方式，两者不是同一个组件。

因此 DDPM 的 noise prediction 与 Flow Matching 的 velocity prediction 不能脱离时间方向、路径和输出参数化互换。二者都把训练回归变成可执行的生成更新，也都留下初始化、近似误差和求值预算。NFE 统计网络求值而不是输出 token；guidance 分支、多阶段 solver、分辨率和 decoder 还会改变一次求值的真实成本。旧的多步采样在质量与预算已验收时仍是基线，少步路线必须说明自己减少了哪一类误差、又接受了什么近似。

### 反向核与训练状态分别约束哪些误差

增加网络容量、优化训练与增加采样步数，并不都在修复同一个误差。单高斯 reverse kernel 是易拟合、易采样的基线；若一步条件分布需要更丰富的形状，可以采用固定高斯 components 与由有限特征驱动的 ReLU logits。在真实 reverse kernel 确实经这些特征分解、密度满足相应正性、连续性与矩等假设时，输出 conditional KL 可以由 terminal 分布不匹配及逐步 mixture/logit 近似误差共同上界。这个分解把 kernel 表达性与初始化分布分开，不是声称所有单高斯模型都有同一个严格误差下界。<!-- source-family:SF-2026-ARXIV-2604-13470 -->

在 exact terminal matching 下的任意精度逼近，是模型类的存在性结论，不证明有限数据、实际优化器或少步预算能找到该模型；仅扩大 mixture 与网络也不会消除上界中的 terminal mismatch 项。更多 components、特征和 logits 带来参数、校准与采样成本，给定特征充分性本身也须另验，高维构造并不解决维数代价。实际选择仍要分别检查训练误差、初始化、求解器与质量/成本；单高斯 kernel、成熟 schedule 或更长 horizon 在其质量预算成立时继续合理，不由表达性定理直接宣布部署优势。

迭代误差还改变训练状态的支持范围。只在 clean sample 的前向加噪状态上训练，在模型 rollout 与训练路径接近时简单有效；若自生成状态逐步偏离，训练可以从当前模型的一次 detached CFG Euler step 构造局部偏轨迹状态，再用同一 noise endpoint 重加噪，监督其 velocity 回到原 clean anchor。这样把纠偏责任前移到训练状态，而不是只修改采样器，或在完整生成后用 terminal reward 评价。

该构造指定了局部训练 target，不证明任意偏轨迹状态都对应唯一 Bayes 真值，也没有覆盖完整推理分布。额外 CFG forward、辅助噪声点与 loss 权重增加训练成本；受限 SD3.5 结果、相同步数和不同适配方式不能当作匹配总 compute，各噪声分支也并非全指标更好。稳定 SFT、求解器改进和 reward-based 后训练各有成立条件；只有偏轨迹纠偏、质量/多样性及净成本在本模型得到独立验收，才采用这种训练 support 扩展，不把它升级为 RL 的替代品。<!-- source-family:SF-2026-ARXIV-2604-12617 -->

若同一图像的各 patch 可以在不同噪声时刻训练，只平衡平均噪声仍可能让几乎每个训练样本含有接近 clean 的局部信息；其他位置利用这份信息时，从纯噪声出发的部署起点就缺少相应训练支持。一条替代采样分支先选择允许的最干净 patch 时刻上界，再在更噪一侧采样其余 patch，而不是只约束均值。这个上界约束训练状态的可用信息，并不表示有限样本里一定有 patch 恰好取到上界。<!-- source-family:SF-2026-ARXIV-2604-19141 -->

训练支持的调整也不自动批准自适应去噪。额外的 difficulty head 只能以速度预测误差提供相对难度代理，让较易 patch 先推进、再与难处对齐；它不是校准的不确定性或最优资源分配真值。受测配置有质量退步，固定 NFE 也不等于相同 wall-clock；head 训练、异步调度和整模型 forward 都须计成本。代理失准或净收益不成立时，统一噪声时刻、同步采样器和原生成路径仍是可核验的回退。

### 连续高斯去噪迁往离散文本时，采样路径也要重验

把 token 映射到连续 embedding 后复用图像 DDPM，保留了成熟的训练目标和采样器，看似只改变数据表示；但若干净数据集中在分离的离散模态，去噪后期的分布会变成多峰。单步均值更新可能把轨迹带到模态之间的低密度区，下一步预测便以训练时少见的状态为条件。失败不一定表示模型从未学到目标 token，也可能来自求解器与离散数据几何不匹配；因此只比较最终 loss 或固定步数不够，还须检查不同噪声阶段的轨迹质量。临界区间取决于噪声 schedule，不能把某篇实验的时间阈值写成通用常数。

一条条件分支是在该区间改用重新从前向噪声分布采样的更新，并在训练中让模型更常见到自己的上一步预测。它能降低错误前缀持续传播的风险，却改变了采样分布：这种更新不是原 DDPM reverse process 的严格求解器，较高正确性可能以多样性下降为代价；self-conditioning 又增加训练成本。若任务重视分布忠实度、已使用更平滑的连续 latent，或质量—多样性验证不通过，原求解器、离散 diffusion 或 AR 仍可能更合适。现有解释来自可测密度的层级玩具模型，文本、代码和蛋白质实验仅验证所测配置；同类更新在受测连续图像任务反而有害，不能外推为通用 diffusion 加速或质量方案。[原始研究](https://arxiv.org/html/2604.02028v1)支持这一受限机制。<!-- source-family:SF-2026-ARXIV-2604-02028 -->

连续score模型还有一个局部敏感性问题：同样大小的score误差，在不同轨迹位置不一定造成同样的终点偏移。对正且光滑的热扩散密度，score `s=∇log p` 的演化对应Burgers型方程；在可作二元分解的模态边界，两个分量的log-ratio给出一个随噪声下降而变陡的tanh界面。对称两高斯的中心边界中，反向时间的局部扰动增长率为 `(a²−σ_τ²)/σ_τ⁴`，只有低于分岔噪声尺度才为正。这个解析例子解释了为何模态选择附近的积分误差可以被放大，也提醒我们不能仅凭平均score误差认定每条生成轨迹同样可靠。<!-- source-family:SF-2026-ARXIV-2604-07404 -->

它提供的是受假设约束的机制解释，不是已经验证的新生产sampler。额外检查局部score变化或在敏感区增加求解步骤会支付诊断/NFE成本；实际网络的近似误差、多个模态交汇和随机反向过程仍需单独验证，不能把对称二元中心轨迹的解析增长率套给全部数据。固定schedule在分布平滑、预算明确且质量已验收时仍合理；几何诊断只有与真实模型的质量、多样性和端到端成本对照成立后，才可用于调整schedule，而不能由理论建议直接宣布加速或无损。

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

条件source还能改变训练与部署的可用信息合同。用目标样本、class或其他κ学习Gaussian source参数，可以让初始状态更贴近终点、降低轨迹曲率；但若κ只在训练时可见，直接部署这个source就无法采样，强KL约束回标准Gaussian又可能失去收益。中间分支在训练时连续插值条件Gaussian与标准Gaussian的**参数**，让同一velocity model见过这段source族；部署有κ时选择插值位置，没有κ时从已训练的标准Gaussian端点出发，不调用条件source预测器。这是训练覆盖的兼容分支，不是任意已训练模型允许换source。<!-- source-family:SF-2026-ARXIV-2604-09181 -->

它用额外source网络、联合训练和插值/KL权重校准换低步数质量，仍受Gaussian形式限制；KL过低或部署插值位置不合适可在较高NFE下退步。[MixFlow的受限实验](https://arxiv.org/html/2604.09181v1)只覆盖CIFAR10及64×64 FFHQ/AFHQ，不证明文本条件、全域覆盖或wall-clock/SLO改善；正文目标与伪代码的KL对象也不能合成一个已验证exact objective。原source已稳定验收、κ缺失而标准Gaussian分支质量未通过，或联合训练成本不合算时，应保留原Gaussian source和多步solver；第49/56章另验执行与调度成本。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11311:start -->
Source identity 不只约束单个样本的 marginal，也约束一批样本怎样共同覆盖可能结果。Independent Gaussian seeds 在单图生成和故障隔离时最简单；若目标是让同一 prompt 的 gallery 在保持每张图 `N(0,I)` marginal 不变的同时扩大相互差异，可以显式设计 batch-level joint noise coupling。Coupling owner 只决定初始样本间的相关结构，denoiser 与 sampler 仍拥有单样本生成路径，gallery evaluator 才判断 diversity 是否值得采用。

联合 coupling 用批间依赖、额外采样状态和校准成本换多样性控制，也会降低复现与 failure isolation。当前证据只覆盖 SD1.5、SDXL、SD3、2,000 个 COCO prompts、三图 gallery 和作者指标，不证明其他 sampler、gallery size 或生产 SLO。单图、强复现、独立故障边界或 coupling 未校准时，应回退 independent seeds。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11311:end -->

### Velocity 目标的混合表示与 Transport 分支身份需要分开

条件平方回归合理地估计局部平均 velocity，普通 marginal FM 并不会因多峰数据而在数学上失效；但在有限容量、少 solver steps 与多峰方向的工程约束下，可以改用 Gaussian-mixture likelihood，以 responsibility 分配 velocity targets。路径还可在每个 token 的起点选择一个 expert，并在整个 transport 中冻结该身份，使“目标怎样表示局部方向”与“这条轨迹由哪个分支承担”分开；这不是每一步重新执行动态 Top-K，也不是换 source 就自动获得兼容性。

混合目标增加 router、experts 与 encoder/decoder 的训练和执行成本，分支不可识别会让责任分配失效；K=1 或大方差也存在退化，当前 dense experts 不能当成第21章稀疏计算收益。`arXiv:2604.15009v1` 的 YAN/MoE-FM 仅覆盖任务微调的约200M/210M模型、单H200/B1/greedy与各方法oracle length，bAbI仍有质量落后；不同模型规模和该长度条件不支持普遍替代AR或服务SLO优势。原目标已验收、分支收益不足或质量回归时，普通FM/AR及更多solver steps继续成立。

<!-- source-family:SF-2026-ARXIV-2604-15009 -->

### 预测空间也可以从 Flat Vocabulary 改为树上的条件分支

离散 diffusion 通常在每个待修订位置预测完整词表，语义最直接，却重复支付大输出 head 的计算和存储。一个条件分支先将 token 组织为树：前向过程从叶子逐级退到祖先，反向过程在当前父节点条件下预测子节点，训练目标按层分解再合成。它改变的是中间状态和去噪路径，不只是为原目标套一个 hierarchical softmax；树、各层 schedule、目标权重和采样步数分配必须作为同一生成 artifact。<!-- source-family:SF-2026-ARXIV-2604-03537 -->

较小 head 能把资源转给 backbone，却把粗层错误、聚类偏差与跨层预算分配引入生成链：过重的粗层 loss 或过多粗层采样步在作者设置中会退步，小模型也没有全面超过既有分支。受限 OpenWebText、512-token 和四张 RTX3090 的结果支持资源重新分配的可能性，不证明大型模型、长上下文或服务尾延迟收益。树的条件划分不稳定、额外层次抵消 head 节省或质量验收失败时，flat vocabulary diffusion 仍是更简单的基线。

## Masked generation：未知位置与已知位置

masked model 维护部分可见序列：

```text
known tokens + [MASK] positions
```

每轮对多个 mask 产生预测，再按 confidence 或 schedule 提交一部分。保守 schedule 一次只接纳少量高置信 token，质量更稳但并行收益有限；激进 schedule 接纳更多 token，早期错误会成为后续条件。

并行提交还要区分 predictor 没学准与 sampler 把联合分布拆开两种误差。即使每个未知位置的条件分布都精确，同一轮在只看已提交 token 的条件下独立填多个位置，仍可能丢失块内依赖。一条受限 tau-leaping 分支按与 token 值独立的随机 ordered partition 分块，将 learning error 与平均条件 total correlation 分开；两者之和上界最终输出 KL，perfect predictor 时 factorization term 等于保留 partition 的 joint KL，不能反推它就是最终 KL 或必然的非零输出误差。依赖 profile 描述随机已揭示集合下的剩余条件相关，并给出 finite-K schedule 的精确 factorization objective，使预算优先分到相关性更强的阶段，而非仅凭 sampler 名称或每轮 token 数选步数。

最优 stationarity 不自动保证唯一解：shooting/bisection 要另有单调条件；profile 随长度一致收敛到连续严格正极限、且使用固定递增光滑 schedule 时，优化只改变 N/K 的 leading constant。特定退化的 exchangeable-mixture profile 才展示同 logarithmic 步数下不同 factorization 阶，不能转成通用 LM 质量定律；随机块大小也不等同固定逐位置计划。完整 profile 要付离线估计与优化成本，模型条件误差、有限样本及 coefficient 差分会污染它，toy exact-target 检查不是已部署语言模型或真实 latency/SLO 证据。profile、独立分块或成本条件不成立时保留原 confidence schedule、固定块或逐位置 sampler，并以实际输出质量、生成预算与墙钟独立验收。 [必要机制与反证](https://arxiv.org/html/2609.21960v1)。<!-- source-family:SF-2026-ARXIV-2609-21960 -->

但“单条路径更稳”与“多次采样能探索不同有效路径”是两个目标。在 self-scoring 且每次提交都满足给定置信门槛的条件下，高置信 gating 会给整条序列的熵设上界：继续提高局部确定性，可能改善一次生成，却压缩多样本搜索的有效分支。若任务要比较多条推理或代码候选，不能只用 `pass@1` 选择 unmask 策略；还应在相同采样预算下检查 `pass@k`、序列多样性与计算成本。一条实验性替代分支不是随机放开所有位置，而是让候选 token 的得分兼顾后续可达的序列空间；精确 lookahead 不可计算时，可用 mean-field 近似提出局部修正并批量采样。它用额外前向计算和近似偏差换探索空间，既不精确采样全局目标，也未在所有受测任务上胜过高置信路径。低预算、单答案质量优先时，保守提交仍合理；不能把[这项研究](https://arxiv.org/html/2604.00375v1)的条件性熵界外推到所有 diffusion decoder 或 AR 生成。<!-- source-family:SF-2026-ARXIV-2604-00375 -->

提交顺序也可以区分“这个位置自身很确定”与“它会影响其余位置的预测”。在给定单层 Softmax、块内 attention 近似不变及已解码位置能代表总体平均等假设下，可由 attention 的列和近似衡量后一种影响，并优先提交高影响位置；这优化的是可计算的近似目标，不是任意多层模型的全局序列 likelihood。并行分支再把低置信位置的最大影响设为动态门槛，只提交超过该门槛的位置，避免用固定数量强行放大并行度。

这仍是有损的解码选择：attention 不是真值或独立性证明，低置信组为空时的实现也需要明确规则。实际融合 kernel 不显式产生整张 attention，因而可在小 sub-block 内提取分数，再跨层与 head 聚合；新增访存、提取成本和子块近似必须计入真实延迟，不能把理论 FLOPs 除峰值算力当实测时间。[受限实验](https://arxiv.org/html/2604.08564v1)中平均任务分数改善，但部分模型/任务的并行分支仍低于其他 sampler，且单 A6000 的 tokens/s 不证明生产并发或 tail-SLO。短任务、严格流式提交或提取成本过高时，原 confidence schedule 与逐位置生成仍合理。<!-- source-family:SF-2026-ARXIV-2604-08564 -->

即使只用 confidence 选位置，也有两个不同的随机控制对象：token temperature 改变一个位置“填什么”的概率分布，position temperature 改变“先填哪里、这一轮提交多少”的分布。前者增大不等于后者也应增大。位置控制可以对 confidence 温度化后无放回抽取固定数量，也可以对每个位置作带阈值的随机接纳；它们改变 reveal order 与并行度，而不是把 confidence 变成正确性概率。需要多样本搜索时，这种分账比用一个温度同时代表内容探索和提交保守程度更清楚。

代价是多一组 schedule/阈值及搜索配置，更多随机位置也可能更早固化错误；候选间最终的 self-consistency 或外部 selector 又是第三个独立验收对象。[受限比较](https://arxiv.org/html/2604.09921v1)只支持 LLaDA-8B/Dream-7B、block32 与长度256等设置，位置随机化并非全部配置都更好；NFE 少不等同 wall-clock 或生产 SLO，四张 A100 上固定72小时的 RL 对照也不是固定更新次数的 sampler 因果实验。低预算、单答案或稳定流式需求下，固定高置信 schedule 仍合理；温度控制与上面的影响排序是可组合的选择，而非保证更高质量的替代定律。<!-- source-family:SF-2026-ARXIV-2604-09921 -->

这解释了一个关键演进：

```text
只填充未知位置
→ 高并行填充暴露误差累积
→ 允许重写已生成 token
→ 显式训练 proposal + correction
```

后一步没有否定保守 unmask。它用更多训练与推理 work、mutable state 和提交复杂度换取更激进的并行 operating point。

允许重写还要解决训练见过哪一种错误。均匀词表替换提供容易生成的噪声，却可能远离模型自己会产生的语言错误；一个条件分支先从 masked input 采样当前模型的预测，再分别在 masked sequence 与 self-predicted sequence 上学习恢复同一干净序列。解码时，已填位置不立即成为硬条件，而是以 top-1 probability 加权 token embedding 与 MASK embedding，并校正混合后的范数；待填位置按从左到右的连续前缀推进，已有位置继续修订。训练噪声来源与中间状态接口因此共同变化，不是只降低 unmask 阈值。<!-- source-family:SF-2026-ARXIV-2604-08302 -->

这种不确定性载体有明确成本与边界：当前模型采样和两类训练输入增加训练工作，self-distilled target 仍可能保留原模型错误；低置信混合也不等于完整词表概率状态。连续两轮 top-1 不变或全位置高置信可以作为 block 的启发式结束条件，却不证明答案正确、原分布等价或全局收敛。作者消融中，未作这种 on-policy 训练的软输入路径失效，而作过训练后，软混合在最激进设置明显优于硬条件；部分高并行切片仍略低于原 checkpoint。质量优先、训练预算不足或 streaming 必须尽早发布时，保守 mask schedule 仍合理；新 checkpoint、软状态规则与停止阈值应作为同一生成 artifact 验收，不能当作无损 speculative decoding。

允许重写之后，下一问题是**在提交前该修正哪里**。只看单条 denoising chain 的 confidence，可能把早期错误锁定为后续共同条件；一条可选的 inference-time 分支让数条不同 reveal order 的路径并行推进，用它们在同一位置的分歧提出待核 span，再在检索到的证据条件下局部 remask、重新生成。路径分歧只拥有“值得复核”的 proposal 权，不能当事实概率；各路径一致也可能一致地错误，最终 claim 仍要由外部证据或拒答 Gate 验收。普通 confidence schedule 在知识稳定、预算紧或低延迟 streaming 时仍更合适。

多路径和局部修正增加峰值显存、检索与输出等待；若证据库过时或 span 定位错误，修正还可能引入新错误。现有 LLaDA-8B/Dream-7B 的 QA 与 hallucination 实验只支持受测 masked diffusion 路径：作者在 exact-match 标签下的检测 AUROC 低于一个训练式基线，换用 LLM judge 标签才高于该基线；四张 H200 上约 1.3× wall-clock 也不等于生产并发/SLO 收益。不能由此推断模型已经“知道自己不知道什么”，或把该机制移植为所有 AR/连续 diffusion 的通用防幻觉器。<!-- source-family:SF-2026-ARXIV-2604-01624 -->

### 生成范式差异要拆成 Objective 与 Commit Policy

AR 与 masked diffusion 的输出差异不能全部归因于“单向或双向”训练目标。受控对照把 objective 与 confidence-based remasking 分开后表明，双向目标和迭代 commit policy 会分别改变 token entropy 与错误修正路径；因此比较生成范式时必须冻结模型规模、训练数据与采样预算，再单独改变其中一个状态。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12522 -->

这些观察只覆盖所测语言模型和 evaluator，不证明某种范式普遍更有创造力或更可靠。无法隔离变量时，应回退端到端质量、延迟和 exactness 合同，不从文本风格反推内部机制。

### 训练反向核也可以引入共享 Route Latent

Objective 与 commit policy分离之后，还需检查训练反向核能表达哪些联合依赖。逐位置 factorized reverse distribution 便宜且可并行，却可能让多个位置独立选出互不相容的 token；另一条分支用离散 route latent 的混合表示反向核，让条件化于 route 的专家分布仍可并行，而对 route 求混合后恢复部分相关性。训练时以可看 clean data 的 posterior router 教给只看 noisy state 的 prior router，推理只使用后者；route 在 token/层级参与计算，并非整条序列固定给一个专家。这也不同于额外训练连续 latent VAE。

离散 route 引入 router matching、straight-through sampling 和专家容量成本；E-MoE 的[§3/§5及Appendix B.3](https://arxiv.org/html/2609.37533v1)中训练为梯度估计保留 top-2 分支，推理前向选择一个 active expert，不等于总参数、FLOPs或 wall-clock只剩一个专家。作者在toy、MNIST与128-token LM1B小模型上的低NFE质量改进，随步数增多会缩小，部分已有 diffusion baseline 和 AR 仍更强；没有真实 LLM reasoning 或生产端到端时延证据。因此 factorized核、保守提交和 AR 仍是容量、路由校准或运行时成本不可接受时的基线，不从 latent 表示能力推导已验证的联合正确性。<!-- source-family:SF-2026-ARXIV-2609-37533 -->

### Uniform Corruption 的目标与 Token Time 是两种训练接口

离散 corruption 的类别也约束 objective。Mask corruption 明确告诉模型哪些位置未知；uniform corruption 则可能把任意位置替换成看起来正常的 token，使同一全局 timestep 难以表达各位置的可靠性。原 reverse-process ELBO 的均匀平滑项在忠实拟合该过程时有其意义，但在少步生成、复用 AR checkpoint 的目标下，过强平滑可能抑制 clean-token 预测。一个受限分支移除该平滑约束，保留抑制错误类别和提高 clean target 的更新，再为每个 token 提供不同的随机 time hint，以其边际均值保持全局时间。hint 是有噪条件，不是暴露真实 corruption 身份的 oracle。

这种选择同时改变训练目标与条件接口，不等于推理时自动获得 self-correction。LUDI 的[方法及对照](https://arxiv.org/html/2609.35817v1)在小模型上隔离 loss 变化，但7B转换还包含 block-causal attention、label shift 与辅助 AR loss，不能把所有收益单归于 loss。理想每步推进 token 数不等于真实加速；端到端推理与 loss operator 的局部提速、显存减少是不同分母，须在相同模型、batch、长度、精度和硬件条件下分别验收，不能由算子或理论并行度替 serving 作保证。原 ELBO、masked objective 与 AR 在过程忠实性、腐化身份不确定或 few-step质量未过 Gate 时继续成立。<!-- source-family:SF-2026-ARXIV-2609-35817 -->

### Masked Diffusion 的训练预算可以按 Locality 重分配

均匀采样 mask pattern 简单且无偏，但会反复训练相距很远、条件信息薄弱的位置。语言具有局部依赖时，可以重分配预测位置与可见 context，使每次更新更常覆盖有信息的邻域，从而改善同预算下的训练效率。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13026 -->

这种加速依赖 locality bias，可能削弱远程依赖和全局一致性。现有实验不能证明任意语言或长上下文任务都受益；长程 slice 回归时，应回退均匀 mask、混合采样或显式增加远程依赖样本。

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

迁移时的 logit 蒸馏也要声明预测对象。AR teacher 的 next-token logits 条件化于 clean causal prefix，并不天然适合学生在腐化 target 的同一位置预测原 token。一个 blockwise 兼容分支先把 AR 模型改造并训练为固定块宽的 diffusion anchor，再让渐进合并后的学生读取与 teacher 相同的 corrupted state，在同位置对齐输出分布。这把兼容性责任落在 teacher 的训练支持、block/mask 与位置映射上，而不是只共享 tokenizer 或复制 checkpoint。<!-- source-family:SF-2026-ARXIV-2604-16514 -->

anchor 训练与多阶段蒸馏增加总预算，block 合并也改变并行读取与修订范围；冻结某个 teacher 不省掉其构造成本。原文固定 block 的多模态对照中 ChartQA 有质量退步，总训练预算没有完全匹配，不能称 AR 权重已经无损转成任意 diffusion 执行。没有相同 corruption/position 支持、长回答或域外质量失准时，应保留已有 AR、较小 block 或重新训练的 masked model；runtime 仍须另验迭代次数与实际时延，训练 logit 对齐不签发生产吞吐。<!-- source-family:SF-2026-ARXIV-2604-16514 -->

### Equilibrium Layer 把深度从训练图移到推理求解状态

视觉 AR 堆叠固定层数时，训练 activation memory 与推理计算深度一起增长；隐式 equilibrium layer
把重复变换表达为固定点，只保存求解所需状态，并允许部署时选择迭代预算。它获得训练内存与推理
深度的部分解耦，却把代价转移到固定点收敛、implicit differentiation、停止阈值与每个样本不同的
迭代次数。求解不收敛、延迟尾部不可接受或硬件更适合静态图时，应回退固定深度网络。作者视觉任务
结果只支持披露模型与求解器，不能证明 equilibrium 结构普遍改善视觉 AR 质量或生产吞吐。
<!-- source-family:SF-2026-ARXIV-2605-01220 -->

共享层也可以显式执行有限次loop，不要求固定点收敛。仅按最大loop数训练时，中间深度的状态未必可直接输出；因此可让同一图的完整深度作teacher，随机选严格中间prefix作student，对teacher预测停止梯度，同时两个分支仍更新共享参数。监督从真实目标逐步转向self-distillation，使较少loop也成为被训练过的输出配置。它改变的是中间深度的监督合同，既不同于implicit differentiation，也不是没有额外head/loss的免费adaptive depth。<!-- source-family:SF-2026-ARXIV-2604-09168 -->

这用训练目标和输出head成本换部署时可选的深度—质量曲线，参数复用却不省去每个loop的实际计算；共享block太小、loop远超训练范围时仍会退步。[ELT受限实证](https://arxiv.org/html/2604.09168v1)的MaskGIT/MAGVIT和DiT、ImageNet/UCF配置支持这种prefix监督，单独一层重复32次仍明显弱于更宽的unique block，不能把重复深度当无限表示容量。需要静态延迟、没有中间输出验收或loop外推失效时，固定深度网络仍合理；runtime必须把unique层数、训练最大loop、实际loop与sampler步骤一起记入生成身份，不能把FLOPs或参数量直接当生产吞吐。

训练有限递归还可以改变状态初始化和监督落点，而不只改变可输出的深度。单步去噪训练从腐化目标恢复答案，却没有直接训练同一转移被连续应用后的结果；一种替代是仍从腐化目标初始化，展开有限 k 次共享转移，只监督窗口末端，并让梯度穿过整个短窗口。它给中间路径提供面向末端恢复的训练压力，与同图完整深度指导中间 prefix 的蒸馏不同，也不要求对完整长轨迹做反传。<!-- source-family:SF-2026-ARXIV-2604-18839 -->

短窗口增加 activation 和多次求值成本，目标腐化也未覆盖推理时所有自生状态，不能由恢复准确率证明模型执行了规划。[受限递归实验](https://arxiv.org/html/2604.18839v1)同时改变模型配置、数据和展开长度，pass@2 与候选选择不等一次调用能力；扰动自身轨迹的 SPRM 分支在一项 7M reARC 对照中还低于原基线。超出训练窗口或状态分布后仍须独立验收，不能从短窗目标推出长程稳定；单步 denoising、固定深度与长轨迹反传分别在成本和任务约束下共存。

## Editable tokens 与 commit boundary

Commit 也可以用 candidate future dependence，而非当前 confidence，作为条件 sensor：同一模型在 No-Future（NF）与 Future-Aware（FA）的预测分布之间比较，future 来自模型自己的候选假设，不是尚未发生的真实 token。窗口、NF/FA 调用、分布距离与可见输出边界要共同版本化；训练截断参数 `α` 不能被误当 runtime confidence threshold。<!-- source-family:SF-2026-ARXIV-2604-23994 -->

候选生成与双条件求值增加成本，错误未来可能让稳定分布仍指向错误答案；cache 或 confidence 选择也有反向切片。受限 block64 实验不保证真实未来正确或外部提交安全；未来假设不稳、预算超界或接口无法延迟 commit 时，回退固定 block、原 confidence/schedule 或自回归路径。

“并行解码”不能由模型名称或一次 forward 更新的位置数推断。对 masked diffusion LM，应从 sampler 的实际 accept events 重建 token 何时进入不可再改状态；同一步若同时接受多个位置，这些 token 之间可能只有 block-level 偏序，而不存在可解释的逐 token 生成顺序。于是 sampler revision、accept rule、commit granularity 与可见输出顺序都属于 generation artifact；把观测 block size 当成模型固有因果顺序，会给缓存、流式输出和审计制造虚假依赖。

这种追踪增加事件记录和分析成本，且单一 checkpoint、sampler 与有限任务上的 commit 行为不能代表整个 diffusion family。若下游严格依赖全序、输出具有不可逆副作用或 sampler 无法暴露 accept event，应延迟外部提交或回退自回归路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14620 -->

Commit记录还必须区分“模型按schedule接受的token”与“外部组件写入的token”。在可暴露中间状态的masked diffusion runtime里，仅有早期refusal或高confidence不足以保证后续路径仍受同一安全条件约束：受限干预实验中，重新mask已接受区域再写入短肯定prefix，能够改变后续生成；但只remask或只写prefix均未取得同样结果，不能简化成“任意编辑都会绕过安全”。这是状态修改权与commit provenance的具体边界，而非黑盒普通用户自动拥有的攻击能力。

因此，generation owner应把允许的repair与不可信状态改写分开，并记录accept event、修改来源与可见输出边界。只检查mask数量不增加，能检测该实验的remask路径，却挡不住不改mask的logit干预，也不能替代输入/输出安全检查；若用重mask作审计，应把诊断forward与真实状态writeback隔离。两种7B/8B模型、固定greedy/linear schedule和单judge的受控结果不证明整个diffusion范式普遍不安全，更不证明作者提出的防御已被验证。第72章继续拥有权限与安全gate；本章只说明可修订生成路径需要怎样的状态边界。<!-- source-family:SF-2026-ARXIV-2604-08557 -->

接受规则还有一条介于单步 confidence 与严格 block 顺序之间的历史分支。只允许当前 block 解码最容易维护依赖；未来 block 的分布可能已稳定时，可以把当前预测分布作为 anchor，与该位置最近若干步的预测分布计算衰减加权 KL，再按一致性阈值提前解除 mask。这与只比较相邻两步不同，新增的状态是逐位置历史分布、anchor 和阈值，而不是凭高 confidence 自动跨 block commit。

历史一致只能说明近期分布接近，不证明答案正确或下一步永不改变；较短 history 或过宽阈值会过早接受，过严阈值则继续支付等待，缓存和 KL 计算也增加成本。[AHD 的受限实验](https://arxiv.org/html/2604.08964v1)及 bounded-embedding 分析支持这一选择分支，不证明生成质量或外部副作用安全；受测模型/任务中的 step 减少更不能直接当任意服务延迟收益。短 history 无法可靠判断、分布漂移或下游依赖固定 block 顺序时，原 block schedule 与延迟外部提交仍是合理回退。<!-- source-family:SF-2026-ARXIV-2604-08964 -->

### 并行与少步生成必须声明依赖、轨迹和状态边界

讨论一步生成之前，还要区分训练样本的插值路径与采样ODE的轨迹。把独立噪声样本和数据样本作直线插值，并不使条件平均速度产生的flow map自动成为直线；在相应正则与矩条件下，普通affine插值要产生精确直流，需要确定性端点coupling，而不是随机独立配对。充分方向还要求该transport的Jacobian满足相应半正定条件，不能将任意确定性coupling称为充分。若流的全加速度确实为零，一次初始速度评价可精确积分；训练出来的近似velocity却仍有估计误差，这不是“训练路径直，所以一NFE无损”的保证。

独立端点也不一概阻止精确直流：非退化Gaussian端点可以加入协方差专门匹配的独立Gaussian辅助噪声，构造零全加速度的条件流；但相同的两段分离uniform混合，在独立端点、连续样本路径和时间上一致Lipschitz速度等条件下已有不可能例子。[存在性与障碍分析](https://arxiv.org/html/2604.15439v1)因此限定的是某类过程的结构可行性，不是所有多峰目标、所有神经生成器或任意维少步算法均不可行。改变coupling、增加前置transport估计或保留弯曲轨迹的多步solver，会改变计算与误差分工；不能确认所用过程满足这些条件时，应保留经验质量—NFE验收与原solver回退，不以定理替代实际训练和部署验证。<!-- source-family:SF-2026-ARXIV-2604-15439 -->

少步蒸馏还要区分“每一步分布匹配”与“多步组合一致”。各噪声水平的局部输出都接近 teacher，仍可能在连续应用更新时漂移；一条条件分支在分布匹配之外，约束直接一步与经过中间时刻的两步更新接近同一终点。它是 learned flow map 的近似组合正则，不是数学上的精确半群保证，也不应把回归一致性单独当作生成质量目标。

少步生成也可只改变 continuous head，而不重新训练条件历史。一个 streaming gesture 分支由 AR backbone 管理 causal history，每个 token 的 flow head 生成连续 motion latent，再交给 VAE decoder；冻结 AR 与 VAE 后，可在缓存的条件上只蒸馏 head。ODE teacher 提供 warmup 目标，distribution matching 的辅助 head 提供后续训练信号。这分开了条件状态更新与连续采样预算，而不是把离散 token 改名成连续量就消除了表达和误差问题。

one-NFE 只计该 head，不包含 AR、decoder、buffer 与条件缓存成本。训练缓存的条件与部署自产生的 motion history 可能失配，须另验 streaming 累积误差及端到端延迟；BEAT2 的受限主 speaker 结果不认证任意角色、时长或实时 SLO，FGD 两表的尺度冲突也不拼接为同一质量点。缓存身份或生成质量不成立时，应刷新条件、增加 head 求值或保留原多步 sampler；较轻 head 不自动获得整个 pipeline 的质量与时延保证。 [必要机制与反证](https://arxiv.org/html/2609.21576v1)。<!-- source-family:SF-2026-ARXIV-2609-21576 -->

少步 action 生成还有一条不同的采样分工：共享网络既学习完整区间的 average velocity，也通过起止时间相同的 diagonal query 学习 instantaneous velocity。先以全局平均场从初始噪声跳到 coarse action，再混入初始噪声（或独立新噪声），以局部 diagonal 场完成修正；两次评价承担不同尺度的误差，而非单纯重复同一 solver。若 re-noise 写为 `alpha*eta+(1-alpha)*coarse`，旧误差被缩小只说明这一步的代数作用，不证明新状态分布等于训练 marginal，也不能从固定区间传播界推出 NFE 越多误差必然指数增长。

[受限双场采样实验](https://arxiv.org/html/2602.13718v2)在同 MeanFlow checkpoint、RoboMimic 每任务100 episodes 下，plain 1/2/4/16 NFE 为78/78/72/60，去掉 re-noise 的配置为24，完整分支约95/95.5，支持这套 global/local 分工而非任意增加步数。重置噪声、双 query 训练与额外局部评价都要付费；Thor 实机共享300 demonstrations、encoder/controller/backbone 的比较仍未完全拆开精度与决策等待的因果影响，19ms动作推理排除了约95ms camera，WM得分也不是成功率，Transport任务还低于两个多步基线。无法保持噪声/时间条件、任务漂移或质量收益不足时，应回退已验证的多步 solver；动作是否安全提交仍由第26章负责。<!-- source-family:SF-2026-ARXIV-2602-13718 -->

AR 视频又把误差带入下一 chunk 的 KV：低步数生成的历史与同一 generator 更密步数的自产生 reference 历史，不是同一 conditioning distribution。训练时混合不同步数的自产生 rollout，并将弱历史条件下的输出关系特征对齐到更密步数的 reference，可以同时覆盖 cache 质量变化和组合误差。代价是额外 rollout、reference 与正则计算，过强一致性也可能压低运动变化。[Salt 的受限实验](https://arxiv.org/html/2604.03118v1#S3)覆盖 Wan 2.1 与 Self Forcing 等视频路线，使用私有 I2V 数据；所测短/长视频指标不证明任意时长稳定、真实 serving SLO 或 cache 成为环境真值。质量退化时增加采样步数、缩短生成 horizon 或恢复原训练配方仍合理。

自产历史与reference的耦合还可以双向训练：共享权重的few-step路径先产生历史，multi-step路径在该历史条件下学习当前真实flow，再以stop-gradient区间位移反教few-step路径。部署仍只运行few-step，但reference已适应部署历史，而不是始终消费另一种teacher-forced历史；history producer、reference与梯度边界必须分别声明。

共享权重不等于训练只有一个模型或没有辅助成本，online fake-score分支、rollout与多步reference都要另计。有限Mutual Forcing消融支持这条耦合，同预算SC/DMD混合目标消融不隔离整个双向loop，也不证明训练全成本匹配，个别同步/语音质量也有反退，更不支持无限视频稳定。耦合失稳或质量收益不覆盖训练成本时，普通teacher forcing、独立蒸馏和已验证的self-forcing配方继续成立。 [原文必要机制与限制](https://arxiv.org/html/2604.25819v1)。
<!-- source-family:SF-2026-ARXIV-2604-25819 -->

训练匹配有误差的历史，还要区分**历史写入质量**与**实际读取集合**。一条原生稀疏 AR 视频分支保留完全去噪的历史为 persistent anchors，local 窗口承载近邻和当前去噪；退出 local 的候选先由 coarse pooling 提名，再在有限 anchor/sink 预算内选择。读取时 persistent 与 local Top-K 进入同一 masked softmax，训练阶段就用这套动态 cache/mask，而非密集训练后才裁去旧历史。pool summary 只有提名权，被丢掉的细节不会因摘要存在而无限可恢复。<!-- source-family:SF-2026-ARXIV-2604-21221 -->

这把有限活跃读取预算变成模型训练责任，却增加 anchor 维护、选择、反向传播和部署 mask 一致性的成本。[受限 Sparse Forcing 对照](https://arxiv.org/html/2604.21221v1)中，移除 persistent 状态可更快却损害质量，短片也有退步切片；Wan 1.3B、有限 20/60 秒生成与 kernel 测量不证明无限长稳定性或完整服务 SLO。动态选择漂移、关键细节丢失时应提高历史预算，必要时回退 full-history/dense 或重新训练；第 49 章再验收具体稀疏 kernel 和 KV 物理驻留，本章只拥有生成训练与状态读取语义。

训练让模型适应有误差的历史之后，推理加速仍要守住写入历史的边界。常见的 DiT 缓存复用相邻去噪步的 block 输出；当每个视频 chunk 只做少数去噪步，步间差异可能太大。这时可改沿相邻 **chunk** 在相同 `(denoising step, block)` 位置复用 residual，并让当前结构与 action 条件共同决定是否重算。复用的是中间计算的近似值，不是已经提交的环境状态；每个 chunk 最终写入持久 KV 的 clean forward 仍须完整计算，以免近似误差成为下个 chunk 的历史条件。<!-- source-family:SF-2026-ARXIV-2604-20289 -->

这条分支以额外 residual/fingerprint 状态和门控计算换取少步生成中的 DiT 工作量，却继承运动突变、长期漂移、动作条件漏检和错误复用的风险。一个受限单模型、短时七相机实验显示：若连 KV 更新也近似计算，画面与全算基线的差异显著扩大；它不提供真实控制安全或更长 horizon 的证明，论文中关于该消融 skip-rate 方向的表文也不一致。分布漂移、行动急变、状态身份不匹配或保真优先时，应强制重算相关 block、缩短复用跨度或退回全算。第 25 章继续负责 action-conditioned 世界状态，第 26 章负责物理动作的安全提交；本章只拥有生成计算缓存与 KV 写入纪律。

<!-- source-family:SF-2026-ARXIV-2604-03118 -->

组合一致性还会改变监督量的合法替换。普通flow matching中，conditional velocity在给定当前状态后的期望等于marginal velocity；这支持单点平方回归，却不意味着把它代入整条轨迹的**全导数平方**后仍是同一目标。展开后还会出现由模型Jacobian和conditional covariance共同决定的项，参数相关，不能简单叫作不影响优化的常数。这是目标函数变化引入的约束，不是conditional flow matching普遍错误。

另一个容易混淆的对象是训练 loss 与样本空间的移动方向。以真实样本吸引、生成样本排斥来提出 drift，可以再用 scalar stop-gradient loss 训练生成器；但这不保证该样本空间向量场等于某个固定势函数的梯度。即使未归一化的径向场可积，依赖当前位置的归一化因子也可能破坏 Jacobian 对称性、引入 curl。保留方向或训练 loss 可计算，都不能单独保证“沿同一个全局目标下降”。

这不是说所有 drift 都不保守：Gaussian kernel 有 score identity，匹配核的替代归一化也能恢复相应 log-density-ratio 势；但生成分布随训练改变、目标侧停止梯度时，每轮的场仍会变化。[原始分析](https://arxiv.org/html/2604.06333v1)支持这些具体对象与条件的区分，MNIST/Fashion 小型 pixel-space 实验不证明修正普遍提高完整生成系统。替换归一化会改变稳定性和训练行为，需与质量、多样性和预算配对验收；原有非保守更新若经验目标已通过验收，或普通 score/flow matching 的条件更清楚，仍可保留，不能仅因可写势函数就批准替换。<!-- source-family:SF-2026-ARXIV-2604-06333 -->

一条有条件的少步训练分支用模型自身marginal velocity构造shortcut，同时保留FM分量维护该估计器。[SnapFlow](https://arxiv.org/html/2604.05656v1)用两步Euler目标避免显式求昂贵全导数，但它仍是数值近似，不是精确flow map；模型预测偏差也会进入自产生目标。额外teacher/shortcut计算和目标混合换少步能力，质量回归时须保留多步solver与原FM训练。其冻结VLM、单A800、30k步与LIBERO重复初态的证据不能推成真实机器人安全或端到端闭环等倍加速；第26章消费动作/环境结果，不重述本节训练目标。<!-- source-family:SF-2026-ARXIV-2604-05656 -->

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

把 guidance 沿估计切向移动，也不意味着有限步仍留在高密度区域：切向位移会经曲率产生二阶法向偏离。一条保留 host prior 的分支把 guidance 拆为法向与切向，按法向的一阶长度和切向的曲率二阶预算共同选步幅，例如用 `r_N + K r_T²/2 ≤ R` 限制允许的 departure；两部分不能靠方向相反就抵消。这个几何预算依赖正则 level set、有效 tubular neighborhood 与受控高阶导数，余项也须保留，不是任意 learned score 下的流形保持定理。共享标量 dual 选择两个方向的幅度，再以实际目标的 Armijo 检查接受步长，几何提案与目标下降是两道验收。

score/Jacobian 只是未知几何的估计；周期性检查后重用 scale，不给中间每一步重新签发 acceptance。局部消融中 Armijo 本身已有明显收益，完整方法更好，但不能把全部收益归给几何投影；Jacobian、curvature 与 line-search 增加内存和时间，改用较少步数的快配置也不等于相同步预算免费改进。图像重建及固定 prompt/seed 的 CFG 对照不证明 exact posterior、语义保证或无限轨迹安全。估计失配、线搜索失败或成本不合算时，应回到 host solver、小步 guidance 或更频繁的实际目标验收，而不让上次接受的尺度越过状态变化继续生效。 [必要机制与反证](https://arxiv.org/html/2609.21251v1)。<!-- source-family:SF-2026-ARXIV-2609-21251 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20547:start -->
当目标从静态 marginal 扩展到 time-dependent latent process，训练对象还要声明“匹配哪个状态转移”。
Generator matching 通过 pushforward generator 定义 conditional objective，并在给定 regularity 条件下证明它与
marginal objective 具有相同参数梯度。它提供的是目标等价的理论接口，不是生产实现或任意过程的稳定性保证；
正则条件、链式 rotational generator 或数值实现无法验证时，应回退已知的固定端点 flow/diffusion objective。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20547:end -->

语音识别消费扩散语言模型时，还须选择它提供的是整句排序还是逐位置分布。对 CTC 的 n-best 候选，masked diffusion 可以用多次扰动后的重建分数作重排；互补 masks 让每个 token 在一对 forward 中都贡献分数，但这些归一化 pseudo-scores 不是精确整句联合 likelihood。若 uniform-state diffusion 在每轮为所有位置给出完整词表分布，则可以用 CTC greedy collapse 后每个 token 对应的首帧、在 non-blank 词表上重归一的声学分布，与该位置的语言分布做 log-linear 融合，再采样下一轮状态。<!-- source-family:SF-2026-ARXIV-2604-14001 -->

两种接口的状态对象不同，不能把重排分数直接塞进位置解码，也不能将首帧对齐启发式和插值权重当作精确 posterior。CTC 对齐、词表、噪声起点、Monte Carlo/denoising 次数共同进入消费合同，额外 forward 与候选预算须计成本。作者的 LibriSpeech、有限模型规模与词表实验中，AR joint decoding 仍更强，不证明普遍低延迟或所有识别任务获益；接口不兼容、预算不足或质量退步时，CTC、AR 融合与只做受限 n-best 重排仍是共存分支，输入声学表示的身份继续由第23章负责。

解码消费合同之外，同一个语音识别模型若要兼顾离线全上下文和流式短右视野，训练时还得决定**让哪一个输出对象在两种可见条件下保持一致**。只在辅助 CTC head 对齐 frame-synchronous posterior，不能替最终 Transducer 的预测负责；受测实验里，这种一致性甚至损害流式 RNNT。一条受限替代分支让同一输入分别通过离线和 chunk-limited 编码，在有效的 `(t,u)` lattice 位置对完整 RNNT 词表分布施加一致性约束。它把跨模式监督放在实际解码分布上，而不是把 CTC 辅助目标当成可互换代理。<!-- source-family:SF-2026-ARXIV-2604-19079 -->

这仍需两种模式前向和 RNNT 训练；现场计算 log-softmax/KL、反向重算只是减少完整 joint 张量物化，不使监督免费。chunk、右上下文和左侧重算共同决定理论等待与真实执行成本，极短右视野下质量仍可退步。作者的受限 FastConformer/英语数据、32 A100 训练与 greedy batch-128 结果支持这一监督对象选择；`C+R` 是理论 latency，不是在线 tail SLO，XL 数据量的表格与正文口径也不能合成一个受控预算。目标分布或成本不合适时，保留独立离线/流式模型、single-mode 训练或辅助 CTC 的原用途，不把“模式一致”升级为普遍最优解。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20946:start -->
语音生成还可把 speech token 与内部 reasoning token 交错到同一训练序列，使模型在发声单元之间保留可学习的
中间状态。它改变 token type、时间戳、可见性和 commit cadence，却不证明内部 reasoning 等于事实正确或可解释
因果；隐藏 token 泄漏、音频延迟和状态错位会成为新失败面。作者任务与模型之外，应保留不暴露中间状态的普通
speech generation，并让外部 verifier 而非 reasoning token 拥有正确性判断。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20946:end -->

交错生成还须问清两种可见输出能否按同一节奏前进。文本 token 与语音 codec token 的编码率不同；固定交错步长或等待强制对齐，会让某一通道被另一通道拖住。一个条件分支把 text 与 speech 放进同一生成序列，并对已生成 prefix 限制累计 speech/text token 比不超过该样本的全局比例，使文本可以先给出可解释前缀，后续语音再跟进。它处理的是输出单位的单调次序，不把逐词文字与声学帧变成精确一一对应；具体比例若依赖完整样本统计，在线未知终点时仍须声明估计或回退，不能凭训练约束直接宣称生产硬保证。

单流布局可减少两条生成轨之间的同步状态，却把 codec、type delimiter、prefix 缓冲、取消与回退放进同一提交合同。受限 [Qwen3.5-Omni exact-v1](https://arxiv.org/html/2604.15804v1) 的 ARIA 采用这样的 prefix-rate 约束，Talker 仍以 RVQ/MTP 与因果 codec 生成波形；Table2 仅给内部 vLLM/compile/CUDA Graph 设置下的 theoretical first-packet latency，且 8 并发时视频首包明显变长。它未单独消融 ARIA，也没有证明在线全局比率已可知、任意语言都低延迟或真实 tail SLO；比率失配、对齐质量不稳或跨模态回退复杂时，固定 chunk / 双 track 的旧分支仍合理。Thinker 与 Talker 的状态交接依然是后文独立的部署问题。<!-- source-family:SF-2026-ARXIV-2604-15804 -->

若任务只需生成语音，另一种粗细分解也不能与 RVQ 的 residual codebook 层级混同。残差 codebook 是同一时间位置上由粗量化到细量化；时间分辨率链先把首个 acoustic codebook 的 token 序列降采样，生成较稀的节奏骨架，再逐级提高 token rate 并在每级做 masked refinement。后一级同时读取前一级结果、文本和说话人条件；共享 decoder 节省参数，却不消除每级迭代、跨级错误传播或条件状态的版本责任。训练时扰动前级 token，只能提高受测扰动下的鲁棒性，不能保证粗节奏错误总能被细级修好。<!-- source-family:SF-2026-ARXIV-2604-19330 -->

这条时间链把一部分局部音素规划移给粗 token，并没有取消总时长估计：作者实际仍用 G2P 与 duration predictor 确定 utterance length，再据此分配各级 mask 序列。一级或独立 semantic→acoustic 的旧路径在短音频、成本敏感或跨级条件不稳时仍合理。作者的有限英文语音实验中，增加时间层级改善部分 WER，但 SeedTTS 大模型切片仍有退步；共享参数量不等总计算、自然度或 streaming SLO 优势，硬件、precision 与真实首包延迟未形成可外推合同。

### Few-step Distillation 要在 Student 实际访问的状态上验收

Student 从 teacher 权重初始化，也不意味着 distillation 后继承相同 memorization：新的 objective、teacher trajectory 与 student 更新会重新分配 near-copy 和泛化。应在蒸馏前后分别记录生成质量、样本相似度及来源证据，不用 SSCD 阈值 0.6 或 p95 当 privacy bound；copy/provenance release gate 仍独立。<!-- source-family:SF-2026-ARXIV-2604-23552 -->

蒸馏、重复样本对照与相似度审计增加训练/评价成本，student SSCD 下降不必保持质量：作者 ImageNet 7k FID 20.14→28.65 为反向例。该有限图像实验及简化谱解释不证明隐私或版权安全；质量退化、复制证据不清或新域迁移时，保留 teacher/多步采样并重新验收，不由加速学生自动继承发布许可。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06376:start -->
#### Continuous Schedule 用 Coverage 换掉固定 Anchor 的盲区

离散 distribution matching 在少量固定时刻对齐，训练和实现都简单；few-step student 实际访问的 off-trajectory state 可能落在 anchor 之间，形成 truncation drift。Continuous-time 分支随机采样轨迹长度，并让 student velocity 在非锚点状态上对齐目标分布，把“覆盖了哪些状态”变成训练合同的一部分，而不是只增加一个更强 loss。

更连续的 coverage 减少固定 anchor 盲区，却提高状态采样、稳定性与校准成本。现有结果只覆盖 SD3-Medium、Longcat-Image、作者 metrics 与 few-step setting，不证明其他 modality、backbone 或生产 latency。off-trajectory state 不可靠或训练发散时，应回退 discrete DMD、consistency distillation 或增加 sampling steps。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06376:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07924:start -->
Few-step flow distillation 不一定受 student capacity 限制；若 teacher trajectory 用盲目随机 midpoint 构造，target 本身就可能偏离高质量路径。训练端可让冻结 teacher 生成多个 midpoint candidate，再由仅训练期可见的 energy navigator 选择 target，student runtime 不携带该 navigator。它用额外 teacher/energy compute 换更好的低 NFE trajectory，也会继承 energy bias 并压低 diversity；tau、teacher、energy 与 source distribution 必须进入训练身份，entropy 或任务质量越界时回退普通 DFM trajectory、更多 sampling steps 或统一 distillation。 [受限证据：arXiv:2605.07924v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07924:end -->

训练期选择 target 时，还要区分 reward 评价的是当前 student 的原始输出，还是将写入监督的构造目标。一个 distribution-matching 分支先从 detached student 输出出发，结合固定 real score 与在线 fake score 构造 implicit regression target，再解码该目标并评分，以评分差调节正负更新。这样让分布匹配负责提出更新方向，让 reward instrument 检查拟采用的目标，而不是用早期 raw sample 的低分直接否定目标；被评分的目标仍不等于最终生成质量的独立真值。<!-- source-family:SF-2026-ARXIV-2604-19009 -->

这一路径用 fake estimator、VAE 解码、target grouping 与额外 reward 调用换取更具体的监督选择，也继承 reward bias、估计器漂移和可解码支持的限制。作者受测 SDXL/SD3 设置并非所有质量指标都胜出，少步 NFE 也不能替代总训练成本或生产延迟。目标偏离支持、质量或多样性回归时，原 distribution matching、普通 reward 后训练与更多步采样仍应并列比较；不能由局部目标评分推断所有梯度冲突已消除。

少步学生的画面质量已可接受时，统一重加噪与均匀critic拟合仍是简单基线；但学生近静止状态上的弱重加噪可能使teacher后验仍靠近静止模式，强运动样本又可能更难被fake-score拟合。可把两条训练压力分开：用当前rollout与paired目标的时间变化亲和度调节base schedule和teacher-specific方向转折prior的混合，再按同noise-bin的预测logFM残差，把mean-one、停止梯度的权重分配给critic loss。前者改变teacher看见的状态，后者只改变已有critic更新内的拟合份额，不改其回归target；评估交互fidelity的表示与预测拟合困难的表示不必相同。

[受限视频蒸馏对照](https://arxiv.org/html/2609.31349v1)把采样和critic重权分别删除，支持这套分工，但方向转折只在exact-flow正则条件下关联posterior变化，不是真实运动证书。亲和度、预测器或归一化未定义时应回退base/uniform；更强noise会伤外观，过强困难权重会伤典型样本。Teacher profiling、paired feature与在线MLP仍有训练费用；相同步数不等总算力，两个planning任务的平均提高主要来自一项，physics评分还可偏好静止输出。换teacher/schedule或超出已测interaction时重估profile、分别验运动/外观与总成本，保留原DMD或更多采样步，物理提交仍由controller负责。<!-- source-family:SF-2026-ARXIV-2609-31349 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09536:start -->
统一 trajectory distillation 把所有时间间隔视为同一种误差，在 denoising dynamics 平稳时简单；但相邻时刻的局部变化与跨越较远时刻的全局变化可能需要不同监督。Temporal-aware 分支从冻结 teacher trajectory 中构造 privileged targets，再按时间距离分配蒸馏目标；训练 artifact 保存 teacher、trajectory 和时间策略，runtime 只选择已经通过质量—速度验收的 operating mode。

更少采样步数是以 teacher rollout、轨迹偏差和额外训练成本换来的，远近状态划分错误还可能同时伤害速度和质量。现有证据仅覆盖作者模型、数据、实现与 evaluator，不证明跨任务、硬件、长度或生产尾延迟的普遍收益。Student 轨迹离开校准区域、diversity 下降或目标任务改变时，应回退原始 diffusion steps 或统一 distillation。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09536:end -->

把多个 teacher step 压成一个 student transition 时，离线 teacher trajectory 是合理起点，但 student 的早期并行提交会改变后续 context，使真实状态逐步离开监督分布。更稳妥的 on-policy 分支从 student 自己生成的 partial state 出发，由冻结 teacher 提出 outcome-aligned future candidates，并只提交仍保持 rollout outcome 的最长前缀；验证失败就缩短 transition。收益是减少 function evaluations，代价是在线采样、teacher 计算与一致性判定误差；高风险或状态漂移明显时，多步 refinement 仍是正确性基线。`arXiv:2608.02942v1` 只在作者数学和代码 benchmark 上支持该质量—效率前沿。<!-- source-family:SF-2026-ARXIV-2608-02942 -->

另一条离线分支不直接预测最终 clean sample，而让 student 一次提出多个连续 denoising transitions，并拟合 teacher trajectory 的 mean velocity。它把 sequential denoise 改成 multi-step proposal，避免每个被压缩 step 都依赖 JVP 或 finite difference；scheduler 可以选择少量 student evaluations，但仍必须把 proposal 看作有损近似，而不是 exact 跳步。

受限实验在披露的 LTX、Wan 与 Qwen-Image 设置中支持 4–8 NFE 的质量—diversity operating points，却不证明 NFE 等于 wall time、data-free distillation 跨域稳定或 mode collapse 已消失。发布 gate 应联合比较真实 latency、峰值内存、sample diversity、目标质量和失败时回退原始多步 denoiser；分布漂移、diversity 下降或 student 轨迹越界时，多步 teacher sampler 仍是正确 fallback。

<!-- source-family:SF-2026-ARXIV-2607-26004 -->

#### Any-step Flow Map 把步数变成运行时状态

固定少步 distillation 为某个 step count 优化，部署改变延迟预算时常需另一套 student。Any-step flow-map distillation 学习非相邻时间间的映射，使运行时可按预算选择跳转长度；获得的是可调 latency-quality frontier，代价是跨多种步长训练并维护跳转一致性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13724 -->

任意步数并不保证任意 schedule 都稳定，长跳转会放大误差。视频 diffusion 的现有证据不外推其他模型或生产尾延迟；质量或一致性越界时，应增加 steps、回退固定 student 或完整 solver。

#### 少步生成的 Diversity Control 可以进入内部表示，但不能绕过质量 Gate

单步或少步 diffusion 丢失了多步 trajectory 中反复注入随机性的接口。受限分支可在 student 实际访问的 activation geometry 中寻找 PCA 方向并施加定向扰动，使 diversity control 从采样时刻移入内部表示。扰动器只拥有候选多样性，生成模型仍拥有输出，独立 evaluator 决定 fidelity 是否可接受。它增加方向校准、存储、层选择和 distribution drift 风险；几何失配或扰动破坏 alignment 时，应关闭该分支并回退原 student、多步 sampler 或外部 best-of-N。exact-v1 只支持作者模型和指标下的 diversity-fidelity Pareto，不证明存在通用 diffusion manifold 或端到端时延优势。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11494 -->

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

#### Iterative Generation 允许安全状态被重新 Mask

AR token 一经提交便只能在后续补救，而 masked diffusion 的中间 token 仍是可修改状态。安全 sensor 可以在 denoising step 间对 latent steering，并把高风险或低置信位置重新 mask 后再生成；这把防护从一次输入/输出过滤推进为逐步 proposal-correction loop。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13043 -->

安全 sensor 的误报会造成反复 remask、质量下降或无法终止，漏报则仍会提交有害序列。证据只支持所测模型、攻击和 evaluator；校准漂移或迭代超预算时，应回退独立输入/输出 policy gate，并保留最大重试次数和拒绝路径。

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

### 因果模型也能学习并行块，但不是无损改变原分布

块内并行不必以双向attention为前提。另一条迁移分支拼接clean与masked序列：clean stream保持普通causal loss，masked位置只看先前clean blocks及本块的因果mask位置，并维持next-token logits的右移对齐。并行块扩大后，可见真实前缀减少；保留clean-stream AR目标便是在训练新路径时继续练习原路径，而不是无需训练的解码加速。

推理按从左到右的置信阈值接纳连续token，至少前进一步；阈值放宽会用不完整块内条件换更少forward，不能像exact speculative verifier那样保持原AR checkpoint分布。单token回退也只是新checkpoint的AR模式。缓存还要区分稳定prefix与mask假设：重算已填块的clean KV再推进，在batch实现中快样本会等待慢样本。于是token/forward的收益可能被额外块计算、cache刷新与同步吃掉；质量或严格streaming优先时仍保留普通AR。

[MARS](https://arxiv.org/html/2604.07023v1)在Qwen2.5-0.5B/7B、greedy短输出上的消融支持上述迁移；clean/masked拼接增加训练成本，较低阈值损伤格式遵循，不同cache粒度与batch也出现慢于AR的配置。相同epoch不意味着相同训练FLOPs，平均benchmark改善不是保分布或通用SLO证明。本章拥有生成目标/commit边界，cache与batch执行再交给推理章节。<!-- source-family:SF-2026-ARXIV-2604-07023 -->

多模态多轮数据还带来一个不能仅靠“块间因果”解决的泄漏边界：一轮回答很短时，固定大小的最后一块可能包含下一轮用户提示；若块内双向读取，这些未来提示便会参与当前回答的预测。因而可见性需要同时绑定 token 的 role、modality 与 turn，而不能只绑定绝对位置或 block 编号。一条迁移分支只腐化 response text，把不变的视觉表示保留在 clean stream，让 noisy block 读取先前 clean context，并在当前 response 结束处截断块；clean stream 仍按 token-causal 目标训练。它既避免跨轮未来信息，又省掉 noisy stream 中重复的视觉表示，但不能由训练期 loss 下降推断开放对话已没有泄漏。

这也解释了为什么已经对齐的 AR VLM 可以直接学习上述生成接口，而不必先把文本 backbone 改成 diffusion、再重建视觉对齐；两条训练路径的初始化知识并不相同，有限预算下直接迁移更好不能证明二者具有相同能力上限。推理中可由 causal 模式先产生首 token，再并行提出余下位置，按 causal 验证的匹配前缀接纳并裁剪 KV；这不是任意采样分布的自动 exactness 证明。[Fast-dVLM 的受限实验](https://arxiv.org/pdf/2604.06832v1)中，长回答质量仍低于原 AR 基线，单 H100、batch 1 的吞吐也不能代替生产 SLO。多轮边界、mask 规则、训练目标与缓存裁剪必须作为同一 artifact 验收；长推理质量或严格因果接口优先时，原 AR 路径仍合理。<!-- source-family:SF-2026-ARXIV-2604-06832 -->

### Block Boundary 也可以成为受约束的生成状态

固定 block 在静态 shape kernel、短输出和低调度复杂度优先时仍是稳健基线；不同语义步骤长度差异很大时，同一 block size 会让简单段过度迭代、复杂段过早 commit。一个 learned-boundary 分支允许 decoder 提出可验证的 block-end，runtime 冻结 boundary 与 policy revision 后再提交；训练可以用 entropy trajectory 做辅助 shaping，但任务 outcome 或独立 verifier 仍拥有正确性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02263 -->

动态边界用更贴合语义步骤的并行度换 variable-length scheduling、cache/rollback 复杂度、reward hacking 与错误自信。边际 entropy 下降既不等于推理正确，也不等于步骤结束；未校准、开放生成或部署并发使收益不稳定时，应回退固定 block。exact-v1 只支持作者 reasoning benchmark 与后训练设置，不能证明动态 block 在所有 workload 更快。

不训练新的 boundary head，也可以把当前置信轨迹用作前瞻范围的 proposal：从已提交及高置信连续前缀之后的第一个低置信位置拟合 confidence cliff，周期性更新 logistic 曲线，再据此选择下一次并行计算的 horizon。这里要分开拟合的 anchor 与实际 commit 阈值；散点位置已接纳不等于连续 cursor 可以跨过未提交位置，边界收紧也仍是任务相关配置。它以拟合、动态 shape 与调度状态换少做无效远端预测，不能把 raw confidence 当作正确性或授予新边界自由提交的权限。

[PACE-dLLM 的理论与受限评价](https://arxiv.org/html/2609.26249v1)进一步限定了这条分支：oracle yield 要求单调 eligibility probability、独立同分布的轨迹形状与截断饱和收益，理论中的概率并不是运行时拟合使用的 raw confidence；更大的固定块也可能取得相同 oracle NFE。单 H100、batch 1、固定生成长度且关闭部分 KV 优化的对照只隔离 decoding 规则，Dream 分支甚至更慢，不能据此证明完整 stack、所有长度或质量目标都受益。平坦、非单调或退化拟合应按已声明的边界回退固定块/单 token 路径；任务正确性 Gate 与端到端延迟验收仍独立于 horizon proposal。<!-- source-family:SF-2026-ARXIV-2609-26249 -->

## Draft、Verify 与 Correct 不是同一件事

### 跨分辨率 Draft 需要显式 Semantic Lock

图像或视频始终在高分辨率状态上迭代，最容易保持统一语义，却会把大量计算浪费在已经稳定的区域。另一条分支先生成低分辨率 draft，由独立验证器标记语义稳定区域并冻结 semantic lock，只对未锁定区域恢复高分辨率 state 继续计算。低分辨率状态拥有 proposal，不拥有最终像素真值；lock 必须绑定尺度、区域、验证器和可重开条件。

这用验证和跨尺度映射成本换 selective compute，也可能把早期错误锁死或在边界产生不连续。细节密集、全局结构持续变化或验证器不可靠时，应回退全分辨率迭代或允许全局 rollback。现有 exact-v1 只证明作者 workload 下的质量/计算权衡。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02152 -->

跨尺度还有一条不锁定最终像素的preview分支：先用低分辨率状态筛选seed或prompt，选好后重新运行标准高分辨率生成，而非把LR结果上采样后继续当作完整HR轨迹。它要求检查downsampler `D` 与velocity是否近似可交换；不成立时，用短窗口缓存的HR velocity校正LR更新，selector与correction共同决定预览能否保留有用语义。<!-- source-family:SF-2026-ARXIV-2604-09227 -->

这把大量候选的HR成本换成有条件的LR筛选，却增加downsampler选择、早期HR计算和缓存漂移；commutator小是局部近似，不是完整HR等价或任意flow天生scale-compliant。[受限Flux/SD3.5实验](https://arxiv.org/html/2604.09227v1)以A100上的quality、LR/HR相似和实测latency比较，不能把预览速度直接当最终图像交付速度。细节影响选择、近似失效或筛选成本不合算时，直接HR采样仍合理；选择结果也不能跳过最终HR质量验收。

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

跨模态共享训练仍有一个更具体的缺口：分别学会 text→image、image→3D，不保证前者生成的图像能被后者一致重构。成对数据充足、完整三模态数据稀缺时，可以先训练独立条件任务，再加入带已知 camera pose 的 view tokens 和交错的 text→image→3D→posed image 序列，让后续模态读取同一 prefix 中的前序状态。共享 backbone 可以保留 conditioning/generation 双流与各模态 output heads；“统一”不要求抹去每种 codec 和输出分布。

这条分支用额外的成组数据、长序列与梯度耦合换取跨模态一致性约束，仍须检查 synthetic data 偏差、几何重构和任务间干扰。[Omni123](https://arxiv.org/html/2604.02289v1#S4.SS5)的 2.2B、256 H100 训练案例在预训练后仍使用三模态及六视角成组数据，不是“仅凭成对数据就证明闭环一致性”；作者所测生成/编辑结果也没有分离训练配比与架构的全部因果贡献。数据或算力不足、某一方向质量更重要时，独立条件模型和显式转换仍是合理分支。

<!-- source-family:SF-2026-ARXIV-2604-02289 -->

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

### Refinement 位置也可以成为条件计算状态

在并行 refinement 中，不同位置距离稳定状态的远近不同，继续给所有 token 相同 expert budget 会把计算浪费在已经收敛的位置。条件计算可以读取 block-relative position、当前 refinement step 与收敛 frontier，为未稳定位置分配更多专家容量；它没有改变最终 commit owner，却把“还需要多少计算”从固定超参变成运行时状态。收益是减少无效计算，代价是训练—推理联合校准、router 抖动和调度复杂度；短轨迹、负载稳定或状态估计不可靠时，固定预算仍是可验证基线。`arXiv:2608.01784v1` 只支持作者 Diffusion-MoE 配置，不能外推为所有生成模型的通用加速。<!-- source-family:SF-2026-ARXIV-2608-01784 -->

latent可以不只由神经denoiser产生：已知几何、材质类型、光源和相机时，物理模拟也能提出待解码的特征。不过VAE通道包含有符号值、边缘强调和非辐射式遮挡响应，不能把RGB能量规则原样搬入。一个受限分支在同一scene中拟合有符号transport及额外响应，再由单view训练的residualrefiner修补latent与几何buffers对应的误差；几何/光照控制属于scene接口，最终颜色与细节仍由refiner/decoder决定，不是latent值获得物理真值。

该分工把模拟约束与codec残差分开，却要支付每scene校准、path sampling和refiner训练；未知scene重建及跨scene泛化未验证。线性latent估计无偏不保证非线性refine/decode后的RGB无偏，错误响应式也不能冒充物理保真。受限equal-error例在latent终点省时、解码RGB却因decoder更慢，因此必须先声明输出终点；细节混叠、极端光源或换codec失败时保留RGBpathtracing后encode、重新校准scene或原神经生成分支，不由局部render速度授予端到端优势。 [必要机制与反证](https://arxiv.org/html/2609.21054v1)。<!-- source-family:SF-2026-ARXIV-2609-21054 -->

### Output Decoder 是独立的版本化 Generation Artifact

只统计 latent denoiser 或 token generator，在 decoder 轻量、输出分辨率固定时足以近似端到端成本；视频生成中，VAE decoder 可能独自占据显著 latency 与 memory bandwidth，且它的结构、压缩率和精度会改变最终画面。generation identity 因此不能止于主模型 checkpoint：latent shape/scale、decoder revision、operator/kernel、precision、resolution 与 frame count 必须一起进入 artifact 和 evaluation contract。主生成器拥有 latent proposal，decoder 拥有 latent-to-output transform，只有最终媒体通过质量和格式 gate 后才算 committed output。

channel pruning、operator replacement 与 distillation 可以缩短 decode，却会引入重建误差、时序闪烁、分辨率/帧数外推失效和硬件特化；主模型质量不变也不能证明最终输出等价。decoder 不是瓶颈、质量容忍度低或运行条件离校准域很远时，应保留原 decoder 或逐级 fallback。优化必须报告完整 pipeline latency 与最终质量，而不能把 decoder microbenchmark 当成整个生成系统加速。

<!-- SF-2026-ARXIV-2602-19161 -->

如果论文为每个 dataset 事后选择最佳 tree budget，它证明“存在有效 operating point”，不等于已经给出线上 controller。

### Pixel Diffusion Decoder 需要独立的重建与预算 Gate

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23902:start -->
VAE decoder 在 latent 表示稳定时便宜，但高分辨率细节可能受固定重建器限制；generative pixel decoder 可以把 latent revision、sigma-aware conditioning、pixel sampler 与 early termination 写成独立 decode artifact。停止规则只提出完成候选，重建质量和预算 Gate 决定是否提交。

生成式 decoder 提高细节自由度，却增加采样成本、随机性与高分辨率稳定性风险。作者实验只支持披露模型与最高分辨率条件；重建、时延或内存越界时，应回退 VAE decoder、cascade 或较低分辨率路径。arXiv:2605.23902v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23902:end -->

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

## Training / Inference mismatch

AR teacher forcing 训练看到正确前缀，推理看到自己的历史输出；diffusion training 看到人工 noise/mask distribution，推理看到由模型 schedule 产生的中间状态。两者都有 exposure mismatch，只是形式不同。

视频序列变长后，还要区分**模型看到的历史窗口**和**本步参与优化的窗口**。直接缩短训练片段、生成时只用上一块作条件，可以降低训练成本，却改变了模型学习与使用的依赖。另一条分支保留优化窗口之前的完整真实历史作为前向条件，对这些历史表示停止梯度，只在随机、重叠的局部窗口计算目标；推理仍按完整历史进行标准 AR。这减少反传范围，而不是宣称长程依赖已经消失。<!-- source-family:SF-2026-ARXIV-2604-07402 -->

这种局部优化仍会改变哪些位置获得更新，也不会消除 rollout error。作者的视频实验中，局部目标单独使用仍明显弱于完整训练；增加首帧窗口采样和相邻表示差异惩罚后，才改善受测质量。惩罚轨迹上相邻表示的距离不等于约束网络 Jacobian，更不能证明全局 Lipschitz 稳定。重叠窗口、采样分布与连续性权重成为新的训练状态，过度平滑也会损失运动变化。只有在任务质量、时间一致性和真实训练成本同时验收时，才值得采用这一分支；短视频、强长程依赖或收益不稳定时，完整序列训练仍是更透明的基线。

proposal-correction training 会显式生成错误中间状态，让模型学习修正。但 synthetic error 是否覆盖真实 rollout error，仍取决于 corruption process。过强 corruption 可能让模型学会恢复不现实噪声，过弱 corruption 又无法处理 aggressive decoding 的错误。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22765:start -->
离散 diffusion 的 artifact 也不能只由 corruption marginal 标识。同一个 clean-data prediction 经 bridge plug-in、marginalization / denoiser 或 score parameterization，可以对应不同的 reverse target；把 uniform process 提升到 absorbing-state representation，理论上可能保留 joint law，却仍改变 network target、loss conversion 与 sampling operations。因而可复现身份至少要联合版本化 corruption marginal、parameterization、loss conversion 和 sampler，不能把“forward noise 相同”当成训练与推理等价。

这种重参数化能暴露更清晰的 target、remasking 或 predictor-corrector 路径，却增加 auxiliary state、corrector steps、conversion 与 learned posterior approximation error。理论 joint-law 等价不意味着 factorized learned sampler 精确，也不证明某种 UDM/MDM 在其他 workload 上普遍更优。转换、假设或近似无法核验时，应冻结并回退原 denoiser/sampler pair，以完整 quality-cost frontier 而不是单一 objective 或 step 数比较方案。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22765:end -->

反向离散过程还可把“何时离开当前状态”与“离开后去哪里”分开参数化。CTMC的off-diagonal rate写成exit rate λ与destination分布r的乘积；相应path-space KL可以分成Poisson timing误差，加上真实exit rate加权的categorical direction误差。可训练conditional surrogate与marginal目标保一阶梯度，需要forward量不依赖参数、reverse rates正且可微以及微分积分交换等条件；这不自动保证有限训练稳定或神经网络找到全局解。absorbing-mask特例中rate由noise schedule固定，才退化为熟悉的masked-token交叉熵；uniform corruption允许重复跳转，两者不能因同叫diffusion就共用训练与sampler假设。

这条分解让模型分别学习转移强度与去向，却增加一个rate head以及rate—步长校准责任。Euler需要λΔt≤1才能形成合法跳转/停留概率；τ-leaping一次时间步可抽取多个jump，并在新状态重新计算destination，因而时间步数不等network evaluations。[受限离散生成研究](https://arxiv.org/html/2604.15694v1)的163M、长度512与统一Gemma-2评分仅提供其TinyStories/OWT质量证据，有限样本genPPL不天然成为数学上界，更不证明线上延迟或所有模型优越。OWT主表与附录的sampler披露不一致，不能补造统一协议或据此归因方法排名；rate或概率合法性无法验证、质量—真实成本不改善时，应增加时间分辨率或回退已验证的mask/schedule与原denoiser，而不是只按step数宣布加速。<!-- source-family:SF-2026-ARXIV-2604-15694 -->

有了局部转移接口，后训练仍不必全部转成轨迹上的 policy gradient。终态序列 likelihood 难算时，一条有条件的替代从冻结 base 的终态样本和 reward 出发，用指数 reward 权重形成 masked 中间状态的条件矩，再匹配局部 unmask posterior；mask hazard 将局部误差连接到受条件的终态 KL。这样需要共同标识 base 条件律、corruption schedule、reward 与样本 buffer，而不是直接照搬 AR token ratio：Training 负责 reward/KL 目标，本章负责终点重加权如何成为局部生成目标。<!-- source-family:SF-2026-ARXIV-2604-18739 -->

该匹配依赖相应条件期望；有限优化、近似 base posterior、旧 buffer 或 confidence reveal 都不自动继承理论结果。control variate 条件无偏也不意味着任意 reward 和系数下每个样本 target 都是合法概率，采用前须核非负性和实际 loss 接口。[受限 tilt-matching 实验](https://arxiv.org/html/2604.18739v1)的 LLaDA8B、LoRA、block32 与 8H100 训练只支持指定任务分支，MATH/GSM 仍弱于一项比较方法，过强倾斜会退步。额外 rollout、中间 mask 状态与优化不能省略计账；条件目标不可靠或质量回归时，原 masked objective、固定 guidance 与已验证的轨迹 RL 仍是可解释的共存方案。

Diffusion 的 supervision granularity 也不应被默认为全程固定。高噪声阶段主要恢复全局布局，低噪声阶段才逐步承载
局部纹理；始终对齐同一个 teacher layer 或尺度，会把非平稳生成过程压成静态目标。一条受限分支让 router 根据
SNR/timestep 选择粗到细的 representation guidance，但 router 只拥有指导尺度，不拥有最终 sample correctness。

动态 guidance 用额外 teacher features、router state 和训练复杂度换更匹配的监督；冻结 VAE 的层级未必对应另一种
backbone 或 modality，router 也可能学到数据集特有 shortcut。无法验证分层特征和时序匹配时，静态 alignment 或
无额外 representation supervision 仍是更可复现的基线。现有证据只覆盖指定 SiT、VAE 与图像数据集，不证明该
粒度演进可直接迁移到文本、视频或所有 diffusion 模型。

<!-- source-family:SF-2026-ARXIV-2605-03317 -->

因此，直接把已有 sampler 的步数调小，与专门训练少步生成器不是同一个优化。后一条分支可让冻结 teacher 评价 student 自己走到的中间状态，再把纠正信号用于训练指定步数的 student；它用离线 teacher/critic 计算和额外模型版本换较短的在线轨迹，但没有消除分布偏移，换步数也未必还能复用同一 student。比较时必须同时记录训练成本、实际网络求值次数及在线质量：一步更新可能包含额外预测或 guidance forward，不能把 step 数直接当 latency。

### 训练表示与部署表示可以分离，但迁移上限必须显式

latent diffusion 借助 VAE 降低训练与推理成本，却让生成质量受 latent bottleneck 和 decoder 约束。一个替代分支用
latent teacher 生成合成图像训练 pixel-space generator，部署时移除 VAE；这把 latent model 从在线执行组件改成训练数据
producer，pixel model 才拥有最终生成状态。收益是解除线上 codec 约束，代价是 synthetic source 的质量上限、额外生成
成本与 teacher bias。teacher 覆盖不足或高分辨率细节未通过独立验收时，应保留 latent pipeline 或混合真实数据；
现有证据仅覆盖作者的 1024/4K 设置与受测 teacher。

<!-- source-family:SF-2026-ARXIV-2605-12013 -->

### Latent Reuse 受 Subspace Shift 约束

复用已有 diffusion latent space 可以节省重新训练 encoder 的成本，但新数据若离开原 latent subspace，或噪声沿不受支持方向增长，denoiser 会在错误几何上拟合。可拒绝的复用合同应测量 subspace overlap、shift 与噪声，而不是只比较重建样例。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13448 -->

理论边界只覆盖论文假设与合成/受限分布，不能给出所有真实数据的阈值。shift 指标或 downstream quality 失效时，应重新训练表示、扩大 latent capacity，或回退像素/原表示空间。

### 连续 Latent 与离散 Token 需要分别拥有版本

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23605:start -->
纯 masked diffusion 直接在 token state 上修正，接口单一但可能承担过重的全局组织；latent-augmented 分支先由 autoencoder 压缩，再用 latent prior 与 few-step distillation 生成全局状态，最后由 discrete decoder 还原 token。AE、prior、distillation 和 decoder 是可独立失败的 artifact，不能合并成一个模型版本。

分层表示减少部分生成步数，却会新增 reconstruction loss、跨阶段漂移和 decoder 幻觉。作者实验不证明连续 latent 对所有文本任务更优；latent 失真、decoder 不忠实或联合校准失败时，应回退纯 masked diffusion、更多 steps 或自回归解码。arXiv:2605.23605v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23605:end -->

## Cache、rollback 与 exactness

### 双向生成中的 Cache 是可变状态，不是只读前缀

diffusion 或 masked refinement 会反复修改序列两侧，传统只追加 KV cache 的不变量不再成立。复用稳定 affix 可以减少重算，但 request-specific anchor 与被更新位置必须重新计算，并把 timestep、mask 和版本纳入 cache identity。错误地沿用自回归前缀语义会产生静默污染；保守全重算仍是低复用或高变化率下的正确基线。
<!-- source-family: arxiv:2608.26140v1; semantic-body-binding: bidirectional-affix-cache-mutability -->

进一步的近似分支只复用 token identity 已冻结的 prompt K/V，并以 response state neighborhood 与 decoder margin 判断可变区域是否仍可复用。Prompt reuse 因而是受状态距离约束的 proposal，不是 AR 式 exact prefix：mutable response 必须刷新，越界就回退 full refresh。它用距离估计与误差校准换取较少重算，也会引入阈值漂移和静默近似误差；高风险输出或 state 快速变化时，完整刷新仍是基线。

<!-- source-family: arxiv:2608.08086v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: reversible-response-cache-state-neighborhood -->

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

Diffusion 与编辑模型还要进一步区分“持续变化的 sample state”和“整条去噪轨迹不变的 condition prefix”。当
single-stream DiT 以 token-causal mask 表示文本/指令、以 chunk-level mask 表示条件图像，并保证后续 noisy image
只能读取这个静态前缀时，runtime 可以只在首个 denoising step materialize condition K/V，之后复用该前缀；这不是
近似跳过 denoiser，而是利用 mask contract 中已经存在的不变依赖。收益是减少重复 condition compute，代价是 cache
identity 必须同时绑定 model/codec revision、mask layout、condition 顺序、分辨率、sampler/timestep 与 adapter；任一
条件、局部编辑标记或版本变化却继续复用，都会把旧条件静默带入新 trajectory。无法证明这些身份完全相同时，安全
回退仍是每一步重新计算 condition context。当前原始证据只公开作者架构与实现说明，缺少可外推的硬件、并发、SLO
与独立性能复现，因此只支持这一依赖与失效合同，不支持普遍速度或质量优势。

<!-- source-family:SF-2026-QWEN-QWEN-IMAGE-2.1 -->

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


#### Early convergence 与 high confidence 不是同一个 Commit 证据

并行去噪最初常用当前位置的边际置信度决定是否提前提交；它便宜，却把“这一步很确定”误写成“后续步骤不会再改变”。约束变化是多个位置共同修正时，单点高置信仍可能被后续条件关系推翻。更严格的 runtime 可以追踪一个 token 在连续 denoising steps 中是否已经稳定，把 early-convergence signal 与边际 confidence 联合用于 provisional-to-committed transition。

这会减少不必要的更新，却增加跨步状态、滞回阈值与误提交风险；稳定检测仍不是联合分布正确性的证明。检测不可靠、输出有外部副作用或 exactness 优先时，应延后到 block verifier 或完整 denoising 结束再 commit。该分支补充本章的 mutable-state 路线，不宣称它普遍优于 confidence schedule。[受限证据：arXiv:2605.10980v1]

多个位置各自具有高边际置信度，也不保证它们组成的 joint configuration 一致。一个受限分支在 commit 前加入 pairwise compatibility，并以 mean-field / fixed-point 更新修正各位置的 marginal score；它减少“单点都合理、组合却冲突”的并行提交，但增加二阶计算，且 pairwise 近似仍看不到高阶依赖。短 block、依赖弱或额外校正成本超过并行收益时，保守顺序提交与 target block verification 仍更清楚。作者在特定 discrete diffusion reasoning/code 任务上的结果只支持该近似的局部质量—延迟取舍，不提供通用 joint correctness。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15805 -->

跨 denoising steps 的稳定还可以和**同一次 forward 的层内稳定**分开。后者比较末层候选在之前若干层是否持续一致，并检查 confidence 是否回落；它减少候选不稳定性，却仍不知道上游未定 token 会不会改变联合答案。一个左到右的提交策略因此再累计当前位置之前、尚未被本轮选择的 masked positions 的熵，只在这个 unresolved-context budget 内接纳候选。累计范围包含未通过候选筛选的位置，而不只是准备同时提交的集合；高置信 token 也不豁免该预算，没有位置通过时再回退局部窗口内的单点提交。

这把单点 confidence、层内 persistence 和上游条件不确定性作为不同观测，而不是 joint correctness 证明。RPD 的[§3–4对照](https://arxiv.org/html/2609.36452v1)支持受测 diffusion LM 的质量—解码时间取舍，但 block变体没有同一全局熵规则，最快配置也并非总是完整策略；减少 NFE 不保证更高 TPS，某些任务完整策略仍慢于 Fast-dLLM。强依赖超出左到右熵proxy、阈值漂移或 verifier 要求 exactness 时，应保留保守顺序或完整 block verification。<!-- source-family:SF-2026-ARXIV-2609-36452 -->

<!-- source-family:SF-2026-ARXIV-2605-10980 -->

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

### Velocity Decomposition 以周期性 Full Forward 约束近似误差

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23381:start -->
每个 denoising step 完整前向最容易保证状态一致，却重复计算变化缓慢的分量；velocity-decomposition 分支在周期性 full-forward anchor 之间估计中间 step，把 anchor interval 与估计状态写入 sampler identity。近似只拥有 proposal，误差 Gate 决定是否继续复用。

减少前向次数会换来累积误差、interval 调参与分布漂移。exact-v1 只支持作者模型、schedule 和测量；误差超界、场景变化过快或质量回归时，应缩短 interval，最终回退完整 denoise。arXiv:2605.23381v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23381:end -->

### Diffusion Serving 不能直接复用 AR Token Queue

AR serving 的 ready unit 通常是“某请求的下一个 token”；masked diffusion 在同一 denoising step 共同更新多个位置，step difficulty、收敛进度和 CPU dispatch 成为新的状态。Batching 的收益来自多个请求共享一次 step forward，而不是把它们简单塞进同一 token queue；admission 需要同时约束 mask ratio、remaining steps、output budget 与 quality policy。它提高并行机会，却引入 step-level straggler、批间不同步和 dispatch overhead；短输出或单请求时，普通逐请求执行可能更简单。`arXiv:2608.23807v1` 的 LLaDA-8B + D2F LoRA、单 H200、GSM8K/HumanEval 只支持该 operating point，不能证明质量对任意 batch 都不变。

<!-- source-family:SF-2026-ARXIV-2608-23807 -->

视频编辑还面临另一种迁移：离线双向 diffusion 能看到完整片段，直播编辑只能读到当前及历史帧。直接把离线编辑分支接到因果 backbone，会让源视频跨帧条件偷看未来，且两种 backbone 的 feature space 不一定对齐。一条受限路线先冻结生成 backbone，让控制分支按帧独立编码输入，并将控制更新方向与双向→因果转换的主导方向分离；这样学到的编辑条件才有机会转移到流式模型，而不是把整个视频编辑器重新训练一遍。收益是重用离线控制能力，代价是受限的跨帧条件表达、特征正交近似和转移后的时间一致性风险。已知未来全片、质量优先时，原双向编辑仍更适合；严格实时且原模型表征不兼容时，专门训练因果编辑器仍可能更可靠。单 H100 的作者流式速度只属于其任务与配置，不构成生产帧率保证。<!-- semantic-body-binding:SF-2026-ARXIV-2609-24788 -->

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

运动condition还能同时改变不同模态的生成初态与控制输入。仅把同一文字prompt送给video/audio两支，实现简单，却未规定二者的运动时序为何一致；一个条件分支把同一2D轨迹用于视频局部flow endpoint，同时把position、velocity和acceleration等运动量送入音频condition。首帧latent沿轨迹搬运，运动区外仍从Gaussian出发；sparse轨迹区以soft mask和区域均衡loss避免被背景面积稀释，音频gate控制初始干扰。<!-- source-family:SF-2026-ARXIV-2604-09057 -->

共享运动状态换同步控制，却引入trajectory抽取、latent搬运、区域权重和双模态训练耦合。[受限AV实验](https://arxiv.org/html/2604.09057v1)的video-only和audio-only配置在不同指标各有优势，joint不全面最好；2D tracking和motion/audio相关也不证明物体质量、接触、3D动力学或空间声学真值。轨迹有误、场景不支持latent搬运或单模态质量优先时，独立生成和原noise prior仍可保留；物理反馈由World Model/Embodied章节另外验收，不能从同步画面直接推断可执行世界。

多事件视频还有另一种时间错配：把叙事拆成逐段短prompt，动作更容易出现，却会在分段生成与拼接时丢主体和背景的连续性；保留完整prompt，则同一帧的视觉query可能同时读取几个互不相干的动作。若事件区间已给定或可粗略规划，一条条件分支保留完整文本作为共同context，只在较早去噪阶段调整cross-attention：由subject词的注意力估计运动区域，使该区域内属于当前帧区间的query强化对应event tokens、削弱其他event tokens，未归入事件的文本仍作全局条件。这是**条件消费的时序路由**，不是删除其他文字、重写生成状态，也不是让attention map取得物体位置真值。<!-- source-family:SF-2026-ARXIV-2604-19473 -->

局部bias减少多事件干扰，却依赖事件分段、subject词定位和运动mask；分段错位会把正确动作压错时间，背景或多主体被误mask也会破坏一致性。它还增加attention探测与规划调用，受限Wan/CogVideoX实验的作者评分和单A100、81帧时间比较不能外推生产并发、物理可信度或tail SLO；多prompt基线生成帧数也不严格相同。无法可靠分段、mask不稳或成本/质量验收不通过时，保留无bias的完整prompt、短段生成或人工时间脚本，不能把局部路由当作视频生成的统一默认值。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06667:start -->
### Camera 与 Motion Condition 可以在 Denoising 中分阶段交接

固定 camera 或 pose-only control 在单主体、镜头简单时更稳定；同时强加 pose 与 depth 到所有 denoising step，可能在后期把局部运动和高频细节过度约束。一个条件分支让早期 pose+depth 锁定 global geometry，后期只保留 pose，使 camera/depth control 在粗结构收敛后交还给 motion/detail generator。Condition scheduler 只拥有约束强度，生成状态仍由 denoiser 更新，独立几何与运动 gate 决定是否接受。

分阶段控制改善相机遵循与动作自由度的取舍，也会引入 pose/depth 校准误差、切换时刻敏感、遮挡和多角色冲突。现有证据只覆盖固定 backbone、作者 benchmark 与 human preference，不证明真实 3D consistency。输入对齐或 schedule 失稳时，应回退 pose-only、固定 camera 或训练式 controller。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06667:end -->

## 生成后训练：轨迹概率、反馈与信用分配

控制 guidance 不等于更新生成器；后者必须先把采样路径上的概率、评价对象和信用分配说清楚。这里保留生成过程的语义边界，PPO/GRPO 等优化规则与训练系统实现交给 Part IV。

### Reward 更新需要先定义采样路径上的 Policy

调节 guidance 是在既有生成器外选择控制量；直接更新离散 flow 的 rate model 则需要另一种概率接口。它输出转移速率，并不直接给出最终样本的 likelihood，因而不能照搬 AR 的最终序列 ratio。一条分支先把当前时间和离散状态作为内层 MDP 的 state，将下一状态作为 action；在合法 Euler 步长下，跳转概率为 rate×步长，留在原状态的概率为一减去总离开概率。这样 policy 拥有的是一步转移概率，terminal reward 才评价完整样本，policy gradient 可沿实际采样轨迹计算，而不必先估计难算的终态 marginal。<!-- source-family:SF-2026-ARXIV-2604-06491 -->

代价是额外 rollout、reference 计算、轨迹方差与步长耦合；概率非负和归一化不成立时，这条接口本身就无效。离散轨迹上的目标等价不意味着连续时间过程无离散误差，路径约束也不自动等于终态分布约束。[原始方法](https://arxiv.org/html/2604.06491v1)提供这种构造，经验验证仅为特定DNA生成与代理reward，不支持文本质量、物理有效性或服务SLO；本章只吸收一般概率接口，不开展AI for Science领域路线。缺少可靠reward或质量回归不通过时，预训练flow与固定guidance仍是基线；PPO/GRPO的更新规则由Training章节拥有。

### 融合逆条件分布不等于融合模型参数

多个目标各自训练后，组合接口还可以是同一reference下的局部reverse conditional，而不是平均参数或随机换模型。共同reference policy、相同KL温度、各base达到局部step surrogate最优、Gaussian逆条件以及非负归一化权重成立时，weighted product可由precision加权均值/方差闭合。这个闭式只说明局部概率接口；它不是原terminal-reward RL的全局最优证书，也不允许省略reference、variance与所优化目标的兼容性检查。

`arXiv:2604.14379v1` 的 MSDDA 经验base用DPOK，没有证明达到全部surrogate最优条件；各base每步仍要执行，无新训练不等无推理开销。受限SD1.5/DrawBench颜色及新组合prompts、每prompt32seeds和ImageReward/VILA评价中，w=.8的一项reward .65低于CoDe .66，不能据不完整执行配置宣称全面支配或生产秒数优势。Reference/温度不兼容、局部Gaussian近似失效或额外求值不合算时，单个已验收模型与原固定guidance仍是透明的共存路径；最终样本质量需独立验收，不能由融合定理代替。

<!-- source-family:SF-2026-ARXIV-2604-14379 -->

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

### SDE-consistent RL 必须绑定 Exploration 与 Finite-step Transition

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23522:start -->
只优化 ODE 或终态 reward 时路径简单，但不能显式控制随机 exploration；SDE-consistent 分支把 exploration schedule、有限步 transition 和 reward rollout 共同版本化，使训练采用的随机过程与实际 sampler 更一致。Reward 仍只评价披露目标，不能替代生成正确性的独立 Gate。

随机轨迹提高探索，却增加方差、稳定性和近似误差。exact-v1 只支持作者假设、sampler 与实验；transition 近似失真、方差失控或质量退化时，应回退 ODE、既有 sampler 或监督训练。arXiv:2605.23522v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23522:end -->

### Metric-geometry Reward 只能提出几何改进方向

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23903:start -->
单一视觉 reward 容易混合 rotation、translation 与外观质量；metric-geometry 分支把几何分量分账，并让 3D estimator 产生 reward proposal。Estimator 不拥有真实几何，最终仍需传感器、可执行约束或独立几何 Gate。

更细 reward 改善 credit assignment，却可能被 generator 利用 estimator 漏洞，或在域外相机和场景上失配。exact-v1 只支持作者数据、GRPO 和 estimator；sensor 不可靠、几何回归或 reward hacking 出现时，应回退 SFT、确定性几何检查或不启用该 reward。arXiv:2605.23903v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23903:end -->

## 从一次生成到 Plan → Generate → Validate → Retry

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

触发重试与消费诊断内容也必须分开验收。判定“不满足”后重新采样，可能只因换了随机样本就改善，而没有按 rationale 修改目标区域；因此应在原请求不变时，有界扰动诊断中的关键语义，观察修改是否随内容改变。一种受限路径先把请求拆成可检查的视觉 tuples，再将逐项判定转为明确 edit 指令，以包含反馈和局部纠正的监督训练建立消费接口；judge 提供的观察仍不是独立视觉真值。<!-- source-family:SF-2026-ARXIV-2604-13491 -->

这增加 tuple 形成、VQA、反馈、训练与 edit 调用的成本，也会把同源 judge 的错误传给纠正器。作者对选中“不满足”样本的整体分数在扰动前后持平，不能证明每个样本都绕过 rationale；显式反馈的轮次与颜色切片也并非全面更好。故局部修正须同时检查原请求、未指定区域保持和真实结果，不能让反馈生成者自授成功；诊断不稳、编辑破坏其他约束或预算紧张时，保留全图重生成、直接生成及外部检查，而不是强迫每次继续自反思。

图像修正还必须先选择保留合同：edit要保留特定像素资产、对象或身份，regeneration可以只保留语义意图并重新生成。后一分支可让模型消费ViT提取的初始图像语义和原prompt，而不沿用原VAE像素latent或中间edit instruction；相应input/initial/final triplet训练也应匹配重生目标，不把它在语义任务上的收益转写成像素或identity保持保证。

删去原像素条件可能减少其局部束缚，却增加身份漂移和资产丢失，视觉encoder仍可能漏掉细节。受限RvR benchmark支持特定重生分支，不证明所有编辑优越，数据生成、训练和多步采样也不能称免费。需要精确资产保持、mask局部修改或可审计差异时，原edit/inpainting与独立保持性验收继续合理。 [原文必要机制与限制](https://arxiv.org/html/2604.25636v1)。
<!-- source-family:SF-2026-ARXIV-2604-25636 -->

同一个生成中的纠正 proposal 还可能需要与候选选择使用不同目标。理解分支从当前 look-ahead 图像与用户请求提出 `c_ideal`，经 CLIP 图文相似度损失、decoder 与 look-ahead 的梯度生成有界 latent 修正；之后不默认最后一次修正最好，而以原始 `c_user` 对推进后的候选重新评分。这把内部理想描述的生成权与用户请求下的选择目标分开，但二者仍可能共享同一表征偏差，CLIP 不是独立真值，梯度链式项也不自动构成正交或流形投影。<!-- source-family:SF-2026-ARXIV-2604-13540 -->

候选选择能够拒绝过度修正，却不能消除理解错误或评分盲区；额外理解 forward、look-ahead、decoder backprop 和多候选评分都在 critical path 上。作者 H800 上的受限生成实验存在更多迭代及 counting/position 切片退步，不能以“无需重训”称免费，也不保证内部目标与原请求始终一致。原请求独立验收、修改预算与可撤销状态须保留；信号不可靠或成本不合算时，回退普通 sampler、固定 guidance 或外部选择，训练期 anchor 与此推理期 proposal 不混为同一责任。

Amazon 的 LLM-based TTS 工程材料支持“显式计划、生成后检查与有限重试可组成一条工程路径”，但没有公开
可复现实验 artifact、模型内部实现、并发或 tail-SLO contract；因此这里只吸收状态机，不外推质量数字或
内部机制。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-13006:start -->
在 video diffusion 中，plan 还可以从生成前说明书演进为生成中的 addressable revision state。VLM 先把对象、动作、深度和运动强度编译为 kinematic conditions；迭代优化阶段再用 object-centric gradient routing，只向当前主动对象对应的 latent 区域传播修正，尽量不扰动被动环境。Planner 拥有 provisional physical constraints，gradient router 只拥有局部更新 proposal，base generator 产生候选 trajectory，独立 validator 才决定修改是否可以 commit；“被 mask 的区域没有更新”不等于真实环境必然静止。

这条分支以推理期 backprop、VLM/API 调用、mask 对齐和更多显存换取局部可控性。Plan 错误与 gradient routing 错误会形成共因，过窄 mask 会冻结本应变化的环境，过宽 mask 又退化为全局重写；keyframe 增加还会累积规划误差。低约束、短视频或 latency 优先时，direct generation 仍是合理基线。Physics-aware video generation exact-v1 的组件消融和受限人评只支持给定基座、3–5 个 keyframes 与 PhysGenBench 下的局部机制，不证明系统获得一般物理定律、复杂接触正确性或实时生产能力。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-13006:end -->

可控视频中的 kinematic plan 还要区分并行分量、时间串接与离散接触，不能把多个动作名称直接当作可相加的物理定律。一个受限生成分支先把文字分成 motion sequence 与数值/定性参数，再由各运动模块提出同一初始状态下的位移；作用于不相交状态分量时可相加，顺序动作则以上段终态作为下段初态，接触时另用有质量条件的跃迁模块重置状态。轨迹再指导视频 latent 的局部旋转/缩放与有界混合；文字解析、动力学候选与外观生成拥有不同的误差来源，不由渲染流畅补齐参数或接触正确性。

这种可组合接口限定在二维、少量运动类别与简单两体接触。平移/旋转存在滚动约束时独立相加仅是近似，稠密接触、关节链与超范围动力学不获保证；从一个跟踪轨迹选择近似 prior 并正则微调也不能识别通用物理法则。受限评价中，运动 invariant 可较稳定而轨迹误差已经爆增，较远结构偏移与部分早期窗口外推明显失败，因此应把 invariant、轨迹和视觉质量分开验收。解析、tracking、prior 搜索、适配与 latent 调制都付费，公开视频的派生轨迹也不是无误差真值；耦合强、标注/参数不可靠或预算不足时，回到可信 simulator/人工轨迹、较简单运动条件或普通生成，不从局部一致性分数签发物理保真。 [必要机制与反证](https://arxiv.org/html/2609.21455v1)。<!-- source-family:SF-2026-ARXIV-2609-21455 -->

### 复杂视觉生成需要显式 Plan、Predicate 与 Retry Budget

一次生成在对象、计数、属性和关系较多时难以同时满足全部约束。更可控的路径先把 prompt 编译为 typed visual program，再由 verifier 对每个 predicate 产生 evidence，controller 据失败类型选择局部 edit 或 resample；program 拥有待满足合同，verifier 不拥有事实真值，最终 acceptance 仍由独立 gate 提交。可定位修复换来 parse error、verifier blind spot、循环和额外生成成本；错误 program 还会稳定优化错误目标。无法可靠分解或验收时，应回退 single-pass/best-of-N、人工检查和最大 retry/cost budget。exact-v1 只证明披露 predicate 与 benchmark 范围，不覆盖开放世界事实和任意 prompt。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11722 -->

### Generator 作为工具时，生成状态仍需外部选择与验证

图像生成器可以把视觉 state 变换为新的 observation proposal，支持后续比较或推理；但图像质量与任务正确性不是同一变量。生成器只拥有 proposal，selector/verifier 必须检查几何、语义和目标约束后才提交下一状态。<!-- source-family:SF-2026-ARXIV-2609-16409 -->

多 sample 与验证提高覆盖，也增加延迟和选择错误，生成幻觉还可能被后续推理放大。六项任务与特定模型不证明通用视觉 reasoning 改善；校验不足时回退固定视觉工具、原始 observation 或文本推理。

## 长视频：历史身份、连续性与可读范围

短片质量、长时一致性、可寻址历史与可交互世界状态是不同的验收对象。下面的分支先约束生成器能读回什么，再讨论跨窗口修复；它们不能替第25章完成环境转移验证。

### Object Permanence 与 Addressable History 是两个 Gate

视频生成能够在短片段中维持对象外观，不代表系统拥有可寻址、可更新的长期环境状态。环形或有界历史机制可以扩展可引用的过去，但仍需分别验证对象身份持续性和历史容量；两者都通过，也不能自动推出 action-conditioned causal transition。它是生成状态管理的进化，不应被误写成完整 world model。
<!-- source-family: arxiv:2608.26794v1; semantic-body-binding: video-object-permanence-vs-history-capacity -->

### Entity-centric Video Memory 把对象身份与帧历史分离

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23610:start -->
保留完整 frame history 在短视频中最可靠，长度增加后成本随时间增长；entity-centric 分支用 entity ID、latent patches、update budget 与 shot script 维护可寻址对象状态。它解决“对象是谁、何时更新”，不等于已经证明物理世界的因果一致性。

稀疏对象记忆降低历史成本，却会引入 identity swap、关系丢失和脚本先验偏差。exact-v1 只支持作者视频与 evaluation；对象身份不稳、关系回归或场景超出脚本时，应回退 keyframe/full-frame history 或扩大可见窗口。arXiv:2605.23610v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23610:end -->

### 长视频历史选择需要有限预算与遗漏检查

<!-- body-source:SF-2026-ARXIV-2606-22370 -->
长视频生成不能无限复制完整历史 KV；按 prompt-history 相关性选择可读历史，把 cache budget、selection error 与 continuity 绑定同一运行时状态。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只覆盖受测长单镜头生成；selection miss 会破坏长期一致性，不能外推到可交互 world state。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

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

### Transparency 不是单一的“可解释程度”

可读 token bottleneck 或可干预中间变量只提供 variable transparency：我们能命名并操纵某些状态。它不自动给出 algorithmic transparency，因为并行去噪或多步 refinement 的实际计算路径仍可能很深；也不自动给出 safety monitorability，因为可观察变量未必对危险行为具有稳定、可校准的因果关系。生成系统应分别记录变量接口、有效串行深度和安全 sensor contract，不能用其中一项替代另外两项。

显式中间变量便于 probe 与控制，却可能增加架构约束、额外 step 和错误解释；更短的可观察路径也不保证语义忠实。纯 AR 或 opaque diffusion 在只要求输出质量、且外部 verifier 足够时仍可成立。现有证据只为特定 diffusion language model 提供 opaque serial-depth 的界与局部 probe，架构和训练各自造成多少透明度仍未分离，因此不能外推为通用安全优势。
<!-- source-family:SF-2026-ARXIV-2606-20560 -->

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

### 离散编辑的概率引导与量化修复不是同一道验收

不重训编辑目标也可以利用预训练离散VAR的source状态：先保留source coarse scales，再沿 `onehot(source)−softmax(prediction)` 的概率方向对target logits加nudging，以source/target两次cross-attention passes的差构造编辑mask。Mask外以更强source nudging约束保留，再可对量化残差做局部codebook投影与修复；它分开了目标编辑、区域保持与离散重建职责，不是source/target logits等值混合、通用精确CFG或背景无损保证。Style edit会关闭refinement，因此量化修复也不是所有编辑模式的固定步骤。

Mask、额外passes与refinement都有成本，错误mask和codebook误差还会损伤背景，应分别验收编辑语义与重建保持。`arXiv:2604.14591v1` 的SWITTI/512–1024受测PIE/COCO/OpenImages中，PIE512 inversion/forward各.41秒不表示其余成本为零；20ms mask统计只single-image/sM=9，SSIM86.80低于TurboEdit91.59，跨backbone指标不能证明普遍更快更好或受控范式加速。GPU/precision/batch/concurrency/SLO在必要设置未披露，不能补造；mask失配、重建退步或预算不合算时，原生成器、显式source约束或其他已验收编辑路线仍合理。

<!-- source-family:SF-2026-ARXIV-2604-14591 -->

source-token 约束可以保留未指定区域，却也会把原运动的细纹理带入新视频；并非约束越强就越忠实。离散 coarse-to-fine 分支直接编码 source、缓存 source 条件下指定 token 的概率，在 edit-pass 比较同一 token 的支持变化，再与 edit argmax 竞争；attention 与 scale 只调局部保留容忍度，不拥有区域真值。较早 scale 固定结构，较晚 scale 撤除 source 约束让细节重生，这不同于对全部 logits 做固定 nudging 或重新反演连续轨迹。

这要付 source forward、概率/attention 缓存和校准成本，也可能因错误 anchor 或释放过早损伤保留区域。前一 scale residual 可以提议最后高分辨率 scale 的计算 mask，被剪 token 仍进入输出头而非变成已经验证的内容；同预算随机剪枝对照支持局部选择，但更快配置仍有质量下降。固定 backbone/seed/短片对照不认证任意编辑或完整请求 SLO；大结构变化、mask 失配或质量回归时，回原生成器、显式局部编辑/inpainting 或更高保留预算，不由 two-pass 提速授背景无损。 [必要机制与反证](https://arxiv.org/html/2609.21268v1)。<!-- source-family:SF-2026-ARXIV-2609-21268 -->

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

量化又会把当前去噪器输出的偏差写入多步 solver 的历史。只修当前输出，仍可能让它与已有history不一致；另一分支把solver需要的整段输出window作为待估state，以平滑轨迹外推作prior、当前量化输出作observation，递归更新当前及历史entry，再把posterior mean交原solver。目标是同一量化轨迹 latent x 处的 full-precision denoiser 输出，不是原始 full-precision 整条采样轨迹；它不把采样latent改为环境真state，也不改变原solver的数值更新定义。开头history不足时只返回有效entry、降低外推阶数，不能填造过去观察。<!-- source-family:SF-2026-ARXIV-2609-21407 -->

这条路径支付offline FP/quantized配对校准、posterior state与在线filter成本。按step/channel聚合并逐element修正省掉crosschannel/spatial covariance，却依赖这种共享统计关系；非Gaussian的LMMSE结论还需要有限二阶矩、噪声相互/时间不相关并与初始state不相关等条件，不是任意量化误差下的Bayesian保证。作者W4A4/20步和两种solver结果主要测对FP生成的分布差，不保证真实质量，部分ImageReward退步且UniPC有cell不最优；单image BF16 CPU-offload比较也不能证明普遍加速。0.25 MiB仅校准统计量，不是完整运行峰值；校准总成本与生产SLO未披露。校准轨迹与部署状态偏离、滤波失稳或成本不值得时，保留原quantized solver、更高精度/密集求值及local correction；既有freshness/完整reference仍负责一致性验收。[必要模型与反证](https://arxiv.org/html/2609.21407v1)。

### 已 Finalize 的 diffusion block 也可能需要可控重开

block diffusion 把局部结果 finalize 后可以并行推进后续计算，但早期错误会被后续 Context 固化。需要编辑时，不能直接覆盖 token 而保留依赖它的 cache/state；正确演进是 `reopen -> invalidate dependent KV/state -> refine -> reverify -> recommit`，并让 commit revision 成为下游 identity。

可重开提高纠错能力，却增加回滚范围、重复计算和并发一致性。只有 verifier 发现的收益超过 invalidation 成本时才启动；低风险生成或依赖扇出很大时，重新生成整个 suffix 仍更简单可靠。

<!-- source-family:SF-2026-ARXIV-2607-22663 -->

## 本章在知识树中的位置

第18章解释 Decoder Only AR，第20章解释 token sampling；本章把 AR 放进更宽的生成范式树，并拥有 mutable generation、block refinement 与 commit boundary。第25章只在生成状态同时表达 action-conditioned environment transition 时才称其为 World Model。

本章拥有加噪/概率路径、noise/velocity 预测目标与 sampler 的对应关系，因为它们共同定义 generation semantics；Part IV 第28章接手如何优化这些目标及训练稳定性，后训练章节接手反馈驱动的参数更新。线上 KV、batching、speculative verification 与 scheduler 分别由 Ch45～48、Ch56 拥有，本章不重复其框架实现。

## 从机制演进到系统设计

生成范式的演进不是 AR 被 Diffusion 线性取代，而是 factorization、并行度与 correction authority 的重新分配。AR 每次提交一个 token，状态简单但串行；masked、block 或 diffusion 路线并行提出多个 provisional positions，再以迭代修正换吞吐。混合方案进一步把 proposal、verification、rollback 和 commit 拆开。

并行生成只有在质量合同、cache invalidation 和停止规则都被版本化后才成立。它获得并行度，却增加迭代次数、临时状态、拒绝/回滚以及训练—推理 mismatch；短输出、严格 exactness 或 correction 成本高时，AR 仍可能更优。图像、视频和文本的 evaluator、长度与硬件路径不同，不能共享未经条件化的性能结论。

## 面试与自检问题

1. 为什么 diffusion 的 serial steps 少于 token 数仍不保证更快？
2. masked generation 中 provisional 与 committed token 有何区别？
3. Block Diffusion 如何在 AR 与 full-sequence diffusion 之间取舍？
4. correction 与 exact speculative verification 的 correctness contract 有何不同？
5. 为什么 draft marginal 不能当作 target path probability？
6. mutable token 会怎样影响 KV cache 和 streaming？
7. 一个离线 best-budget benchmark 为什么不等于线上 controller？
8. 哪些场景下 append-only AR 仍是更好的工程选择？
9. DDPM 的前向加噪、noise-prediction loss 和反向采样均值如何相接，哪个对象在部署时不可见？
10. Flow Matching 的条件直线路径为什么不保证部署时一 NFE 精确生成？

## Research Outlook

下一阶段压力是让 generation policy 成为 runtime 可控制对象：根据 entropy、queue、memory、deadline 和 output side effect 动态选择 block、proposal、correction 与 commit；同时建立跨 runtime 可复现的 committed-goodput 与 exactness 测试。

## Reflection

生成范式不是从“串行”走向“并行”的单向进步史。系统用并行草拟换来了 mutable state，用修正换来了额外 forward，用更大候选空间换来了 verification 和 memory。真正的演进，是让这些成本与输出承诺被显式管理。

## Review notes

- Daily 2026-09-30，Experimental：[LUDI v1](https://arxiv.org/html/2609.35817v1) §3–4、[RPD v1](https://arxiv.org/html/2609.36452v1) §2–4/Tables1–2、[E-MoE v1](https://arxiv.org/html/2609.37533v1) §3/Eqs5–11/§5/AppendixB.3。分别只吸收 uniform objective与token-time接口、同pass层内稳定＋unresolved-context提交、离散route混合核及train/infer router边界；受测模型与局部成本不外推生产，未认证全文定理或复现实验。sep30_evidence_check必要来源审阅并写入，实际正文/相邻衔接待root非作者写后复核，不能自验通过。

- **生成基础桥核验：** DDPM 采用 [arXiv:2006.11239v2](https://arxiv.org/abs/2006.11239v2) §2–3，重点核对 Eq.(4)、(11)、(12)、(14) 与 Algorithm 1/2 的加噪、损失权重和采样接口；正文以条件 c 扩展无条件记号，不引入其性能结果。Flow Matching 采用 [arXiv:2210.02747v2](https://arxiv.org/abs/2210.02747v2) §2–4，重点核对 CFM 梯度等价条件、Eq.(14)、(20)–(23) 的 Gaussian 条件路径与 ODE；正文用 s 区别 DDPM 的时间方向，并保留 sigma_min>0 的终点近似。本次仅核这些基础命题及与相邻段落的交接；既有案例的来源标记和实验边界保留，不声称全章来源均已重新事实审阅。

- `SF-2026-ARXIV-2604-19009`：[exact-v1](https://arxiv.org/html/2604.19009v1) §3.1–3.3/Eqs1–7/Alg1、§4.1–4.4/Tables1–4，Daily 2026-04-22。采用 detached student→fixed real/online fake score→implicit regression target→VAE 解码 reward 的训练监督接口，而非 reward 直接证明原输出或目标梯度正确。SDXL/SD3 的非全胜指标、target grouping/fake estimator/reward 成本及 NFE 非总 compute 保留。root 必要来源→Ch24 写前、实际正文及邻接写后非作者复核均通过；未复现实验，不代替整日报 Gate。
- `SF-2026-ARXIV-2604-19141`：[exact-v1](https://arxiv.org/html/2604.19141v1) §3.1–3.3/Eqs3–4、§4.1–4.4/Figures3–4/7–8/Tables1–2、AppA.1/B.1–B.2，Daily 2026-04-22。采用 patch 噪声时刻上界与平均噪声不同的训练支持条件，difficulty head 是误差代理而非校准不确定性；有限质量退步、head/异步管理成本及固定 NFE 非 wall-clock 保留。root 必要来源→Ch24 写前、实际正文及邻接写后非作者复核均通过；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-21221`：[exact-v1](https://arxiv.org/html/2604.21221v1) §3.1–3.5、§4.1–4.5/Tables 1–3；Daily 2026-04-24。仅吸收训练期内生 persistent/local 稀疏读取和 masked-softmax 状态合同，coarse pool 不保证被删历史可恢复。Wan 1.3B、有限时长与移除 persistent 的速度—质量反向保留；不外推无限生成或完整线上 SLO。root 已完成必要源→当前 owner 写前复核，且实际正文与相邻衔接写后非作者复核通过；未复现实验。

- `SF-2026-ARXIV-2604-19079` — Daily `2026-04-22`；[exact-v1](https://arxiv.org/html/2604.19079v1) §2.1–2.4/Eq1–5、§3.1–3.4、§4/Tables1–2。仅采用两种可见 context 下最终 RNNT `(t,u)` 完整词表分布一致性与辅助 CTC 反向证据；双模式前向、现场 loss/recompute、0.16s 退步、32 A100/128M/120k 小时范围保留。XL 的表格240k与正文280k口径未合并，`C+R` 是理论等待而非 tail SLO；root 已完成必要来源→当前 Ch24 owner 独立写前复核，实际正文/邻接已由 root 非作者写后复核通过，见 papers/2026/04/_sources/V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md，未复现实验。

- `SF-2026-ARXIV-2604-19330` — Daily `2026-04-22`；[exact-v1](https://arxiv.org/html/2604.19330v1) III-A/B Eq1/Fig2、IV-A–G/TablesI–V。采用时间降采样首 codebook 链与 RVQ residual-codebook 层级的区别，仍保 G2P+duration predictor 的总长度责任、逐级 masked passes/前级噪声/成本及 SeedTTS 局部退步；参数共享不证明 total compute、首包或自然度普遍更好。root 已完成必要来源→当前 Ch24 owner 独立写前复核，实际正文/邻接已由 root 非作者写后复核通过，见 papers/2026/04/_sources/V3_ROOT_CH24_TWO_WRITE_AFTER_20260928.md，未复现实验。

- `SF-2026-ARXIV-2604-20289`（Experimental，部分 Disputed）：[exact-v1](https://arxiv.org/html/2604.20289v1) §2–5/Table1–3，Daily 2026-04-23。采用跨chunk按 `(step,block)` residual 缓存与 clean KV-update pass 强制全算；只支持作者 X-World、四步、七相机12 FPS、13段约22秒同分布轨迹、单 Zhenwu 810E PPU/BF16 DiT 部分。VAE/I/O/跨设备与端到端SLO未测；Table3移除KV保护的PSNR 53.384→21.461虽提示受限污染，但skip 71.3%→62.8% 与§4.2“增加约9个百分点”矛盾，隔离后者及由其导出的比较。apr20_resume已完成非作者 source→当前 Ch24 owner及实际正文/相邻段写后复核（`daily-20260423/V3_APR20_LAST_TWO_INDEPENDENT.md`），未复现实验。

- `SF-2026-ARXIV-2604-19473` — Daily `2026-04-22`；[exact-v1](https://arxiv.org/html/2604.19473v1) §3.2–3.4/Eq1–11、§4.1–4.4/Tables1–4。采用完整prompt下 frame×subject/event interval 的受限 cross-attention bias，不把attention mask、GPT-4o评分或物理连贯性当独立真值；时段可由用户/GPT-4o-mini/均分给出，T2V早20%与I2V早40%去噪受测。Wan2.2 StoryEval 48.3→56.2，单独EAM为51.9；单A100、480×832/81帧846→863s含平均2.65s分段调用，multi-prompt帧数约81×事件数不严格匹配。precision、batch、concurrency、tail SLO未披露；root已完成必要来源→当前owner写前及实际正文/相邻衔接写后独立复核，见本日 `V3_ROOT_19473_WRITE_AFTER.md`，未复现实验。

- `SF-2026-ARXIV-2604-15804` — Daily `2026-04-20`；[exact-v1](https://arxiv.org/html/2604.15804v1) §2.4–2.5 / Tables1–2。ARIA 只为单流 text/speech prefix-rate 提供受限机制；输入 video 约160ms temporal-ID、AuT 6.25Hz/40M 小时属不同表示或训练分支，不把全部质量或延迟归 ARIA。Table2 Flash 音频/视频 1 并发235/426ms、8 并发352/1625ms，Plus 为435/651→955/1980ms，均 theoretical；硬件/precision/完整队列 SLO、ARIA 单独消融与在线全局比率取得方式未披露。不采用跨模型/语言全胜或生产保证。root 必要 source→实际 owner 写前通过，且已核 apr20_resume 的实际正文、相邻交接与本条证据边界，非作者写后复核通过；未复现实验。

- `SF-2026-ARXIV-2604-18739` — Apr22；[exact-v1](https://arxiv.org/html/2604.18739v1) §3.1–3.3/Eqs11–19、§4.3–4.4。terminal 指数倾斜→局部条件匹配，base/schedule/buffer 假设、sample target 非自动 simplex、有限训练/质量成本边界已入正文；root 写前必要来源与真实 owner 采用、实际正文与相邻衔接非作者写后均通过，未复现。
- `SF-2026-ARXIV-2604-18839` — Apr22；[exact-v1](https://arxiv.org/html/2604.18839v1) §3.1–3.3/Eq6–7、§4.4–4.5/Table1。腐化 target→短递归窗末端监督不同于 prefix distill；SPRM 退步、配置/数据/候选混杂与长程未证保留。root 写前必要来源与实际 owner 采用、实际正文与相邻衔接非作者写后均通过，未复现。

- `SF-2026-ARXIV-2604-15439` — Daily2026-04-20；[v1](https://arxiv.org/html/2604.15439v1) Def1–4/P1–C4/T5/T6/C12及P10必要反例。random affine sample与conditional ODE直流区分进入并行/少步主线；充分方向PSD Jacobian、Gaussian特调辅助噪声及两个分离uniform混合的有限no-go条件保留，不外推任意多峰/全维。root必要source→actual owner窄采用及实际正文/相邻写后通过，非日Gate。
- `SF-2026-ARXIV-2604-15694` — Daily2026-04-20；[v1](https://arxiv.org/html/2604.15694v1) §4.1/P4.8/absorbing特例、§4.2/AppD两sampler及§5必要评价。Poisson timing+真实rate加权destination进入joint artifact链；conditional/marginal一阶假设、Euler合法性与τstep不等NFE保留。163M/512/TinyStories/OWT、Gemma2 finite-sample genPPL不是数学上界，OWT协议分歧不补造；hardware/precision/batch/SLO未披露。root写前及实际正文/相邻写后通过，不称复现或日级完成。

- `SF-2026-ARXIV-2604-15453`：[SoTo v1](https://arxiv.org/html/2604.15453v1)，Daily 2026-04-20；§3–5.5/§7、D.3、E.4、G。采用 ordered prefix→partial reconstruction→beam 的条件分支，保留 matched 2D 比较、NFE≠时间、detokenization 成本及 verifier hacking/弱 prior 反例；不采用 Appendix B 全局界。apr02 必要 source→实际 owner 独立采用通过；root 实际正文与相邻衔接非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-16514`：[exact-v1](https://arxiv.org/html/2604.16514v1)，Daily 2026-04-21；§3.1–3.2/Algorithm1、Table4。采用 AR next-token 与 same-position corrupted-state 蒸馏的监督支持区分；固定 block anchor、多阶段预算与 ChartQA 反例保留，不采用普遍无损迁移或训练 compute 匹配。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-10103`，Experimental：[exact-v1](https://arxiv.org/html/2604.10103v1) §3.2–3.5、§4.1及主表。采用evicted-only线性history与local窗口分责、evict前移交、dense→hybrid训练和position/teacher-target身份；不推无损无限记忆、causal world model或任意负载SLO。apr02必要来源→实际owner及真实正文/相邻衔接写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-13470`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13470v1) §2.3、§3.1–3.4、§4 Proposition4.1/Theorem4.2/Remark4.3；采用 reverse-kernel 表达性、逐步近似与 terminal mismatch 分层，保留有限特征/正则假设、exact matching 与高维成本，不把上界项当所有架构严格下界或可学/部署优势。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。
- `SF-2026-ARXIV-2604-13491`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13491v1) §3.2/Table2、§4、§6.2/Table5/AppendixA.3；采用 retry trigger 与 rationale 内容消费分离，368/2212选中No整体.82持平不推逐例bypass；显式反馈、第三轮与颜色反例及VQA/edit成本保留。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。
- `SF-2026-ARXIV-2604-13540`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13540v1) §4.2–4.3/Eq6–12、§5.1/5.4；采用 CLIP(c_ideal) 梯度 proposal 与 CLIP(c_user) 选择目标分开，不采用正交projection/独立truth/免费；H800、look-ahead/backprop、多候选及K5和任务切片退步保留。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。
- `SF-2026-ARXIV-2604-14001`（Experimental）：[exact-v1](https://arxiv.org/html/2604.14001v1) §3.1–3.2/Eq4–8、§4；采用 MDLM 互补mask pseudo-score 重排与USDM dense vocab/首CTC帧非blank归一融合分离，不冒充精确joint likelihood/posterior；LibriSpeech有限架构/词表、MC/NFE成本与AR joint更强保留。root本轮必要源→实际owner采用通过；本次实际正文与相邻交接已由 root 非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-15009`（Experimental）：[YAN/MoE-FM v1](https://arxiv.org/html/2604.15009v1)，Daily `2026-04-17`。采用§3.1–3.2/Eq4–6/§4–5/Table1的mixture likelihood responsibility与起点冻结token transport分支；普通FM非数学无效、dense非稀疏、退化/oracle length/bAbI反例保留。复用 `V3_ORDINARY_TEN_TWO_INDEPENDENT_AUDIT.md` §7及root当前必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-14379`（Experimental）：[MSDDA v1](https://arxiv.org/html/2604.14379v1)，Daily `2026-04-17`。采用§4.1/Eq3/§4.2 Theorem1/Eq6–7/§5的局部reverse conditional融合接口；共同reference/KL/Gaussian/surrogate最优条件、DPOK未证最优、多base执行与reward退步保留。复用 `V3_ORDINARY_TEN_THREE_INDEPENDENT_AUDIT.md` §8及root当前必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-14591`（Experimental）：[Masked Logit Nudging v1](https://arxiv.org/html/2604.14591v1)，Daily `2026-04-17`。采用§3.2/Eq6、§3.3/Eq9、§3.4、§4/Table1及§6.1.1/Table4的source概率方向加logits、两pass mask及局部codebook修复；style关refinement、非CFG/无损、mask成本/SSIM退步保留。apr01旧转传收据不是新审阅或原附件；root本轮已定点重开官方必要原文/实际Ch24交接，必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。

- `SF-2026-ARXIV-2604-09921`，Experimental：[exact-v1](https://arxiv.org/html/2604.09921v1) §2.2、§3.1–3.2、§4.1–4.3、§6；采用 token/position sampling 分责，不采用一般并行正确性。理想化 anchor/fork 与 TLC K=1 的证明不外推，precision、线上 batch/concurrency/SLO 未完整披露；NFE、固定时长训练与最终 selector 分账。apr01 必要源/真实 owner 提案及实际正文与相邻交接的写后独立核验通过。

- `SF-2026-ARXIV-2604-12617`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12617v1) §2.3 Eq6–12/Algorithm1、§3.1–3.5。采用 own detached 单步与 same-noise clean-anchor 纠偏训练；不采用唯一 Bayes 真值、完整 inference support 或同总 compute 优势。root 必要源/owner 与实际两段及相邻交接写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-09227`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09227v1) §3 Eq4–11/Alg1、§4–5/AppendixB。D–velocity commutator与stored HR局部修正；preview筛seed/prompt后HR重跑，不是LR上采样exact续算。Flux1dev/SD3.5L、A100、PixArt30K随机5000prompts（2–1885chars）、受测500轨迹；5step局部cosine不作普适solver/交付SLO保证，precision/batch/生产并发SLO未披露。6分gap深入，必要源/owner非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。
- `SF-2026-ARXIV-2604-09057`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09057v1) Methods、Tables2–5/AppendixF–G/Limitations。video轨迹搬运endpoint+soft mask/等区域loss，audio8D kinematics conditioning，2D非物理因果。Ovi720×720/5s、32A100/bf16、batch32/30ksteps、50代表视频；单模态与joint指标各有反例，生产并发/SLO未披露。6分gap深入，必要源/owner非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03）；未复现实验。

- `SF-2026-ARXIV-2604-09168`，Experimental：[exact-v1](https://arxiv.org/html/2604.09168v1) §3 ILSD/Eq1–2、§4.1–4.2/Figure8与Limitations。同图full-depth target stop-grad，中间prefix共享θ；ImageNet256/UCF16×128×128、codebook1024、270epochs，DiT SD1.4VAE/batch512/500k/512DDPM/CFG3。N1×L32 FID10.30、超过Lmax退步限制‘任意深度’，硬件/precision/生产SLO Not Disclosed，不宣称无额外训练成本或NFE即wall-clock。未复现实验；本次必要来源、实际正文及相邻论证的非作者独立复核通过（root）。
- `SF-2026-ARXIV-2604-09181`，Experimental：[exact-v1](https://arxiv.org/html/2604.09181v1) §3–4/Alg1–2、§5/§6.1–6.2。Gaussian μ/Σ参数连续插值而非Bernoulli二分量抽样；κ=x1仅训练可见时部署standardGaussian。低β对高NFE有反收益，FFHQ4NFE不全面更好；Eq5与Alg1 KL对象不同，不采用exact目标一致性保证。CIFAR10/FFHQ/AFHQ64、作者FID/NFE；硬件/precision/生产SLO Not Disclosed，不推NFE等于latency。未复现实验；本次必要来源、实际正文及相邻论证的非作者独立复核通过（root）。

- `SF-2026-ARXIV-2604-08564`，Experimental：[exact-v1](https://arxiv.org/html/2604.08564v1) §3.1–3.2、§4、Table1/§5.1–5.5。column-sum order 的证明依赖单层与固定 attention 近似；实际取 sub-block 并平均层/head。Fast-dLLM-v2 1.5B/7B、LLaDA1.5-8B，单 A6000、GSM8K/MATH/HumanEval/MBPP；1.5B Parallel MATH31.02低于Confidence32.24，7B Parallel MATH51.88低于Entropy51.92。precision、输入输出长度、batch、并发与生产SLO在采用证据中未披露；峰值FLOPs估算不当实测成本。本次必要原文与实际正文/相邻交接已由root独立复核通过；未复现实验。

- DMax（Status: Experimental，SF-2026-ARXIV-2604-08302）：[exact-v1](https://arxiv.org/html/2604.08302v1) §3.1–3.2 Eq3–10/Algorithm1、§4.1–4.3/Table1–3。采用 on-policy 错误噪声、soft token/MASK 输入与启发式停止的耦合，不采用原分布保持/全局收敛/事实正确保证。LLaDA-2.0-mini，训练八H200、两epoch、batch8、block32，0.7M math/1M code self-distillation；推理两H200 TP、batch1、generation2048，precision/生产并发/SLO未披露。Table3软路径未OPUT为0%，OPUT后最激进soft约90.4%而hard68.2%；部分Table1切片低于原checkpoint，TPF与TPS分开。作者必要源和实际正文已核，待root非作者写后；未复现实验。

- `SF-2026-ARXIV-2604-08964`，Experimental：[exact-v1](https://arxiv.org/html/2604.08964v1) §3.3/Eq4–7、§4.1/阈值与history消融、AppD/E。current-distribution anchor→历史加权KL→future-block unlock；bounded embeddings 的过去分布接近不证明未来正确。LLaDA-8B/1.5 默认256 generation/32 block、history6，MMaDA/DIFFA另测；default阈值0.01与消融0.02最佳属不同设置，不能写成统一recipe。DIFFA Wildvoice2.76<2.80，非全部任务质量改善。hardware/precision/batch/concurrency/tail-SLO未在所采用证据披露，不采用通用latency倍率。root 已完成必要原文与实际正文/相邻链路的写后独立复核，通过，本地实验未复现。

- `SF-2026-ARXIV-2604-06333`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.06333v1) §2–5/§6 支持 sample-space drift 的归一化与可积性条件；不否认参数空间 scalar surrogate loss，不采用固定全局下降或普遍质量增益保证。必要原文、实际正文及相邻衔接的非作者复核通过（root），不代表整日报验收。

- `SF-2026-ARXIV-2604-08557`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.08557v1) §3–4、§6/Limitations。v1 TrajHijack只支持可观察/修改中间denoising状态的white-box威胁模型；LLaDA-8B-Instruct/Dream-7B-Instruct，64步，greedy与deterministic linear schedule，HarmBench159及固定50行为消融，Claude Sonnet单judge。两组件各自0%不等于组合无效，gradient增强反而退步；monotonic mask check只是定义性挡该路径，其他防御属建议未验证。模型/硬件/精度/生产并发/SLO不能从ASR外推；未复现实验，本次写后独立复核通过（root）。

- `SF-2026-ARXIV-2604-07404`，理论受限：[exact-v1](https://arxiv.org/html/2604.07404v1) §4/§5.4/§6.1–6.3/§7.1/§11.2–11.3。采用heat→score/Burgers与指定positive smooth binary decomposition的局部界面解释、对称Gaussian中心反向扰动增长；`τ=σ_noise²/2`、`σ_τ²=σ_0²+2τ`，不是物理时间或所有轨迹全局Lyapunov保证。恒等式与局部积分必要式已核，不把非高斯数值示例、机器精度identity检查当trained模型实验；没有对真实U-Net/多模态生成验证新的adaptive sampler或速度质量收益，三模态junction/learnedcurl/stochastic correction仍未闭合。正文“平均score误差不足以逐轨迹保证”是基于局部敏感性的设计推断，不是作者报告的MSE比较实验。2+1+2=5因知识缺口深入，未运行实现，待root独立写后复核。

- `SF-2026-ARXIV-2604-07402`（Experimental）：[exact-v1](https://arxiv.org/html/2604.07402v1) §4.1–4.4、§5.2、§6.1–6.2 与 Appendix D/E。正文采用完整历史条件与局部 loss/gradient 的分离，不采用 Eq10 的全局 Lipschitz/误差保证。实验限 OmniTokenizer、110/343M、17帧256²、四张A100与作者视频数据；Table2 的 Local-Opt 单独质量退化、窗口重叠与连续性权重反证均保留，未复现实验。

- `SF-2026-ARXIV-2604-06491`，Experimental：[exact-v1](https://arxiv.org/html/2604.06491v1) §3.4、§4.1–4.3、§5及§7。采用合法Euler一步概率构造inner MDP的接口，不采用普适terminal-TV或无误差保证；DNA代理评价不证明大模型文本、真实功能或生产收益。apr01已独立核对必要原文与实际正文；未复现实验。

- [MARS 2604.07023v1](https://arxiv.org/html/2604.07023v1)，Experimental；§3.1–3.4、Tables2–5、Limitations与AppendixA。采用causal双流训练、AR-loss保留及近似连续接纳；1/B为干净上下文位置的计数proxy，不是能力保证。Table2所谓compute-matched只匹配epoch，AppendixA披露MARS每阶段约两倍H200-hours；速度表固定GSM8K256题、Qwen2.5-7B、τ=.95、batch4/8/16，推理GPU数未独立说明，不外推生产并发。

- `SF-2026-ARXIV-2604-06832`（Experimental）：[官方 PDF v1](https://arxiv.org/pdf/2604.06832v1) §3.2–3.4/Figure3、§4.1–4.5/Tables1–2。采用 response-only corruption、clean-only vision、turn-end truncation 与 causal 验证/KV 裁剪的接口分支。Qwen2.5-VL-3B、block curriculum 2→32、两项 CE 权重均0.5；单 H100 batch1，优化路径含 SGLang/W8A8 FP8，不将该优化吞吐当未量化 baseline 的通用收益。短回答平均 MDM73.3/AR74.0，MMMU-Pro-V 长回答21.4/26.3，spec24.6，不能称无损。两路径采用已对齐VLM与text-only LLM不同初始化，所谓相同ceiling仅作者假设。本轮必要正文和实际上下文已作者核对，待root非作者写后复核；未复现实验。

- `SF-2026-ARXIV-2604-03537`（Experimental）：[exact-v1](https://arxiv.org/html/2604.03537v1) §3.1–3.4、§4、Tables1–2 与 level-weight/step 消融。仅层内过程具所述 CTMC 解释，跨层阈值有奇点；overall ELBO按层求和。head节省后模型深度重配不是所有变量不变的比较，small/base结果有例外，粗层权重/步数不是越大越好。未复现实验；本次写后独立复核通过（root）。

- [2604.05656v1](https://arxiv.org/html/2604.05656v1)，Theoretical / Experimental；§3.3–3.4及§4、AppendixF。采用conditional/marginal替换在不同目标下的边界与有限步shortcut；不沿用全文中无条件的“方差处处非零”或真实机器人加速推测，FM仍保留，LIBERO模拟和推理计时分账。

- `SF-2026-ARXIV-2604-01624`，Status: Experimental：[exact-v1 §3–6 与 Limitations](https://arxiv.org/html/2604.01624v1) 用随机 reveal order 的跨链分歧定位、证据条件局部 remask；只测试 LLaDA-8B/Dream-7B 与作者 QA/RAGTruth 协议。LLaDA 的 EM-AUROC 76.4 低于 DynHD 84.2，LLM-judge 重标后才为 86.5；8 链在 4×H200 的约 1.3× wall-clock 伴随约 1.67× 峰值显存，不证明开放域真值置信或生产 SLO。

- Qwen-Image-2.1（Status: Experimental）：[官方发布与仓库](https://github.com/QwenLM/Qwen-Image-2.1)披露 32 层 single-stream DiT、token-causal / chunk-level mixed mask，以及 condition image 与 instruction 的 prefix KV reuse；只采用由公开架构直接支持的 cache identity 与 invalidation 合同。作者页面没有完整披露可比较的 hardware、batch/concurrency、SLO、独立复现与不确定性，因而不采用 headline quality/performance 结论。

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
