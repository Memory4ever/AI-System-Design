# 第5章 神经网络到底学到了什么

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Stable Knowledge Node ID:** `WORLDVIEW-REPRESENTATION`
**Legacy Chapter:** Ch5
**Status:** Draft

**Roadmap Intent:** 理解特征、表示空间、分布、泛化和归纳偏置。

## 本章要回答的问题

训练把大量数值参数更新到了某个低损失区域。那些参数里究竟有什么？模型是在存储样本、提取规则、建立世界模型，还是以另一种方式组织经验？

本章的中心命题是：**神经网络学到的是服务于训练目标的分布式表示与计算特征，而不是一套可以逐条读取的人类知识库。**这些表示由数据分布、架构的 inductive bias、优化路径和目标函数共同塑造，既可能支持泛化，也可能包含记忆、偏差和脆弱相关性。

## 从“每个神经元存一条知识”开始

最直观的想象，是把网络看成数据库：某个神经元识别边缘，某个神经元识别猫，某组参数存储一条事实。这个类比有少量启发性，因为网络内部确实可能出现对某些概念敏感的方向或单元，但作为总体解释会失败。

先看一个神经元实际做了什么。对输入表示 `h`，第 `i` 个神经元通常只计算一个标量：

```text
a_i = sigma(w_i^T h + b_i)
```

其中 `w_i` 是该单元的输入权重，`b_i` 是 bias，`sigma` 是非线性函数。这个标量没有数据库里的 key、schema、唯一事实类型或稳定地址。它只有放回前后层连接和当前输入后，才获得计算意义。

更直接的反例来自神经元置换。设一层为 `h = sigma(Wx + b)`，下一层读出 `z = Uh`。若用置换矩阵 `P` 重新排列隐藏单元，并同步改写：

```text
W' = P W
b' = P b
U' = U P^(-1)
```

因为 element-wise activation 与置换相容，新的网络得到 `h' = P h`，但最终仍有 `U'h' = Uh`。模型函数完全不变，所谓“第 137 个神经元存储某条知识”的地址却已经改变。更一般的表示基底变化也会产生类似问题：坐标是实现选择，不天然是语义身份。

其次，模型通常通过分布式表示完成计算。同一概念可能依赖许多参数、activation directions 和跨层路径，因此删除一个单元未必删除对应行为；反过来，一个单元也可能参与多个特征，修改它会连带影响看似无关的输出。后文的 superposition 会解释网络为何可能让多个特征共享有限表示维度。

最后，知识表现不只来自静态参数，还来自参数对当前输入执行出的动态状态。事实回忆、指代消解或上下文规则，往往需要 tokenization、embedding、Attention、MLP 与 output projection 共同完成。即使某个 activation 能预测概念标签，也只说明信息可被读出；只有受控干预进一步改变了下游行为，才能开始支持“模型实际使用了它”的因果主张。

因此，更稳健的问题不是“这条知识存在哪个参数”，而是：模型把输入映射到了怎样的 feature direction、subspace 与 computation path，这些表示支持了什么后续计算，又在哪些输入分布上成立。单个可解释神经元可以是真实现象，但不足以把整个网络还原成逐条寻址的知识数据库。

## 表示是为后续计算服务的中间状态

把网络写成多层复合函数：

```text
h_0 = x
h_l = phi_l(h_(l-1); theta_l),  l = 1, ..., L
y_hat = g(h_L)
```

其中：

- `x` 是输入；
- `h_l` 是第 `l` 层形成的 representation；
- `phi_l` 是该层参数化变换；
- `theta_l` 是该层参数；
- `L` 是层数；
- `g` 把最终表示映射为预测 `y_hat`。

`h_l` 不是对输入的中立描述。它保留什么、丢弃什么，由最终训练目标反向决定。如果两个输入差异不会影响 loss，模型没有必然动力保留这种差异；如果某种微小模式能稳定降低 loss，它就可能被放大，即使人类认为它无关紧要。

Representation learning 的关键收益，是让系统不必完全依赖手工特征。模型可以把原始输入逐层变换为更适合任务的坐标系。图像模型可能从局部纹理逐步组合出形状和对象，语言模型可能从 token 与局部搭配逐步形成句法、语义和任务相关状态。这里的“层级”是常见经验图景，不意味着每一层都对应唯一、整齐的人类概念。

当不同规则能解释同一输入序列时，共享的可读几何更不能直接签发一个唯一状态。[受控规则混合实验](https://arxiv.org/html/2602.23164v1)让同一棋步在两种更新规则下产生不同棋盘：跨规则 probe 和 steering 可以共享部分方向，但选择规则与恢复状态仍是两个计算接口。某混合模型中，game-ID干预改变合法下一步，却不明显恢复下游board-state读出；另一种罕见歧义人口要在较早层干预，才同时改善状态与输出。它支持按冲突输入检验“表示怎样被消费”，不证明大型语言模型统一在某层存储世界。Procrustes对probe参数的高一致性是拟合后的局部几何，随机对齐也有非零基线；单seed、不同单/混合数据量不授通用迁移。训练、probe与白盒干预均付费；共享方向失效时保留显式规则/状态、黑盒任务对照与更细干预，不以几何相似替代实际状态验收。<!-- source-family:SF-2026-ARXIV-2602-23164 -->

## 什么叫“好的表示”

一个表示是否好，不能脱离任务和约束判断。对某个任务有用的表示，可能主动消除另一个任务需要的信息。

可以从三个角度理解。

第一是 **separation**。原始空间中纠缠的样本，经过变换后可能更容易被简单决策边界区分。例如最终分类头只需线性变换，就能利用前面层已经组织好的特征。

第二是 **invariance**。对任务无关的变化，表示应尽量稳定。例如图像轻微平移不应改变对象类别；同义改写不应完全改变语义判断。但不变性过强也会丢失细节，所以它必须服务于具体目标。

第三是 **compositional usefulness**。中间特征应能被后续层组合，支持更复杂的判断。单个特征未必对应完整概念，它的价值可能只体现在与上下文中的其他特征共同计算时。

可组合的接口也可以先通过受控的共享因素形成，而不由单个任务的高准确率直接推定。一条[有限图像通信学习分支](https://arxiv.org/html/2601.10169v1)由 Oracle 将共享同一概念的多个 target 放在一起，先学单概念的离散 codebook，再用同一接口组合已见概念来描述未见组合；测试的新颖性是 known concepts 的新搭配，不是自动发现新概念。单 target 仍可能支持游戏成功，却缺少相应组合性；非组合 Qrc（QR-code）数据上初始化可退步，部分任务继续 composition 训练也不如只完成第一阶段后的 zero-shot，因而不能把“离散码本”或“两阶段”当充分保证。Oracle 的因素划分、预设词表大小与消息长度 l 已提供先验，bag-of-words 消费还没有解决重复概念或任意变长；它不等同于人类语义词典。第一阶段训练、码本初始化、validation checkpoint 选择和多 seed 检验均付费，zero-shot 只省去额外组合训练；因素假设或任务质量不成立时保留普通端到端学习与独立行为测试，而不将局部组合成功外推为通用 LLM 能力。<!-- source-family:SF-2026-ARXIV-2601-10169 -->

当新任务需要重新组合已学操作时，组合性还涉及“学习什么、测试时搜索什么”的分工：一条受限路径在训练期学可复用 primitive 的离散 codebook 与共享递归 executor，面对新的输入输出例子时冻结 executor，只优化 program latent 来选择执行序列。它与不显式学习程序序列的端到端模型、或外部符号程序加确定性验证并存；神经解释器的可微搜索换来额外训练与每题多起点/梯度搜索成本，也不证明 latent 是唯一的人类可读程序。受测证据仅是作者构造的有限 program-synthesis 语言与 Shift/Composition 类任务：能否表达目标程序、搜索预算和最终行为正确性仍要分别验收，不能外推到任意长度或通用 LLM 编程。<!-- source-family:SF-2026-ARXIV-2604-18907 -->

任务表示在测试时可被优化，不表示模型已经归纳并执行了新规则。若backbone与task embedding同时变化，embedding可能迁出训练坐标而backbone仍靠自身改动解题；一个可诊断的替代分支先固定backbone只适配embedding，让任务定位发生在共同接口，再冻结该embedding更新backbone。这样能分别检查表示中可读的规则与后续执行适配，代价是两阶段搜索和额外测试训练，不把近邻检索当唯一规则身份。

规则标签或可控generator允许分别测probe与最终任务；重复train任务的检索仍含记忆，概念标签也未必定义完整算法。受限网格实验中，漂亮的embedding几何可支持已训练范围插值，却不能自动叠加未学操作或外推新位移，逐pair成功也不保证整任务所有pairs通过。因而应保留冻结接口、严格任务结果和训练覆盖检查；预算或规则未知时沿用joint适配/直接执行验证，不由线性可读或二维图授予OOD泛化。 [必要机制与反证](https://arxiv.org/html/2609.21181v1)。<!-- source-family:SF-2026-ARXIV-2609-21181 -->

组合性还要区分可表达的计算与有限训练轨迹中可学的长度泛化。某个架构可模拟计算机，不表示固定有限alphabet、标准位置形式的C-RASP[Pos]计算语言与特定理想learner下，短CoT样本足以恢复任意更长执行；负结果必须绑定这些条件，不能由少量合成任务否定所有Transformer的可学性。

改变trace表示也会改变学习问题：显式signpost或只记录value changes可以提供不同的正条件，却新增标记规则、状态更新和轨迹构造成本。理想可增长alphabet的证明不是现实tokenizer无限新增token，受限合成实验只检验约两倍长度，S5约1.7倍，训练random offset又已暴露测试位置/标识；这些对照不是无界可靠性。部署长度超出已验范围时，应保留长度上限、独立执行/结果验证或明确状态机器，而不以表达能力代替学习证据。 [原文必要机制与限制](https://arxiv.org/html/2604.25800v1)。
<!-- source-family:SF-2026-ARXIV-2604-25800 -->

可表达正确规则仍不足以保证训练会选择它，输入可见性本身也在限定学习问题。同一份递归执行轨迹可以让模型读完整trace，或每步只读当前子任务frame、返回时仅交回结果；若真实目标确实只由该frame决定，后一种观测约束就排除了对外部trace线索的依赖。受限MDL反例中，比正确局部规则更短的完整trace shortcut可以拟合训练，却在熟悉子任务换了外层context时答错；单纯扩大覆盖、保留可表达性，不会自动消除这种选择偏好。

该保证只覆盖训练已见的局部context所形成的等价集合，不覆盖全新子问题，更不等于现实optimizer执行MDL或递归普遍胜过CoT。若局部frame已丢掉定义答案的必要信息，隔离本身会失败；若parent payload仍能反解隐藏shortcut，分帧也未切断它。受测合成任务的多frame训练、position窗口和训练步数并非全compute匹配，长frame仍会退步；需要跨任务的信息时仍保留完整context，但应另测周边context干预、实际结果和必要信息边界，并计入stack/runtime与轨迹构造成本。 [必要机制与反证](https://arxiv.org/pdf/2609.20831v1)。<!-- source-family:SF-2026-ARXIV-2609-20831 -->

有限轨迹还要区分答案正确与遵循指定算法。把终端 decoder 提前用于中间表示，可以检验答案何时可读，却不证明模型已经执行终止，也不能仅凭早解认定它采用了另一种算法；须连同参考中间状态和训练 hint 误差，核验所声称的执行路径。受控排序案例中，终态信息很早可读而参考轨迹尚未完成，说明终态成功不能单独为算法 faithfulness 背书。

一条更受约束的学习分支将 scalar 交换与离散控制分开，每步把控制投回有限状态再继续，但局部合法转换仍依赖全局 inner-loop 终止信息的形成和监督。显式比较器、预设 chain/code 与虚拟全局节点都是先验，不是模型自行发现的通用算法；去掉全局监督，作者同架构连训练长度也失败。有限长度的 autoregressive test 因而不等于无界可靠执行，teacher-forced 训练也须单独记录。需要可认证步骤或未验长度时，保留确定解释器与独立轨迹/结果检查。[必要方法与消融](https://arxiv.org/html/2609.31114v1) <!-- source-family:SF-2026-ARXIV-2609-31114 -->

这些标准都不是绝对属性。训练目标定义了什么差异重要，架构定义了哪些组合容易表达，数据决定模型实际见到哪些变化。

## 数据分布决定模型能学到哪种世界

训练样本通常假设来自某个分布 `P_train(x, y)`。模型在训练时最直接优化的是该分布有限采样上的经验风险。部署时面对的却是 `P_deploy(x, y)`。

当二者接近时，训练中发现的规律更可能延续；当二者不同，表示可能失效：

```text
P_train(x, y) != P_deploy(x, y)
```

这种差异统称 distribution shift，但具体原因可以不同。

- 输入分布变化：用户语言、设备、场景或长度发生变化。
- 标签关系变化：同一输入对应的业务规则或偏好改变。
- 选择偏差：训练数据只覆盖容易收集的人群或成功案例。
- 反馈回路：模型上线后的决策改变了之后可观察到的数据。
- 对抗适应：外部参与者主动寻找模型弱点。

模型不能从未观察、未表示、未通过目标函数约束的信息中凭空获得可靠规律。大规模数据扩大覆盖面，却不会自动消除许可、偏差、过时、重复和稀有事件不足的问题。

从 AI System 角度看，Data 不是训练前的一次性输入，而是模型世界边界的配置。数据血缘、切片评估、漂移监控和反馈治理因此属于能力质量，而不只是数据工程卫生。

## Inductive bias：为什么有限数据仍可能产生泛化

有限样本通常对应很多都能拟合训练集的函数。模型最终选择哪一个，需要某种偏好，这就是 inductive bias。

偏好可以来自多个位置：

- 架构，例如卷积偏好局部和平移共享，序列模型规定信息怎样流动；
- 优化，例如初始化、gradient descent 和 regularization 会偏向某些解；
- 数据增强，把希望保持不变的变换显式加入训练；
- 目标函数，决定哪些错误更昂贵；
- 参数共享，使同一计算规则在不同位置或样本复用；
- 上下文与后训练，进一步塑造模型在运行时表现出的行为。

Inductive bias 不是坏事。没有任何偏好，模型无法从有限经验中选择可推广的解释。真正的问题是偏好是否与部署环境的结构匹配。

参数共享也不是“少些参数便自然泛化更好”。展开后的 RNN 与非共享 DNN 可以只差权重复用，但其训练后表示还取决于监督出现在哪些 timesteps、信号强度与优化统计。[受限的统一 kernel 分析](https://arxiv.org/pdf/2602.15593v1)在 μP、大宽度、MSE/weight decay 及独立噪声 SGLD 的平稳 Bayesian posterior 条件下，保留 RNN 跨时间 covariance，DNN 则具有时间对角 mask；弱学习信号下二者可无区别，端点监督的预测模式也可能相同、仅尺度不同。匹配顺序 teacher 的监督才显示共享规则帮助未监督时刻插值，不能外推任意任务或普通有限时间 SGD；短线性链相变亦不是所有网络的阈值公式。求解与采样增加成本，表示相关性没有替代 held-out 时序质量。监督结构或这些条件不匹配时，应保留非共享模型、实际训练对照与分布外验收，而不由架构相似或共享名称决定替换。<!-- source-family:SF-2026-ARXIV-2602-15593 -->

当匹配时，模型能用有限样本捕捉可复用规律；不匹配时，模型可能依赖 shortcut。例如训练图像中背景与标签高度相关，模型可能学习背景而不是对象。它在同分布测试集上表现良好，换背景后却失败。

增强保留原标签，也不自动保留输入条件下的最优目标。设干净输入为 `x`、标签为 `f(x)`，训练实际观察的是加噪后的 `z = x ⊕ noise`；给定 `z` 的 Bayes 最优预测不必等于干净目标 `f(z)`。uniform 输入、iid bitflip 和高噪声的合成布尔函数反例中，接近最优的 noisy loss 仍可伴随较差 clean accuracy；这不证明真实 LLM 必然失败，也不否定确实保持任务语义的增强。[受限目标错配证据](https://arxiv.org/html/2602.08695v1)因此支持一个工程诊断推断：分别验收 noisy 与 clean 目标，先核增强的不变性，必要时回退干净数据与切片验证，而不是仅由有噪训练成功认定模型学到了原规律。额外评测有成本；这里不采用原文方向相互冲突的 sensitivity 罚项补救。<!-- source-family:SF-2026-ARXIV-2602-08695 -->

即使训练目标显式鼓励类间表示分离，也未必固定这些方向在部署环境中的标签意义。受限的coding-rate反例里，稳定特征与环境相关特征都能映射到两条正交方向；当环境相关性反转，编码目标和表示的边缘分布可以不变，固定source classifier却把原先常正确的对应关系读反。要求一个coding operator在多个训练环境都最优，也只约束几何变换的inner目标，不能单独保证encoder的预测关系稳定；目标几何、固定读出和跨环境质量仍需分别验收。

这条反证必须保留精度与支持边界：在正噪声、完整source支持的有限模型中，失败encoder只是任意接近全局最优，精确最优配合不受限的source-optimal classifier反而可保持零目标误差；精确最优也全错的例子改变了支持域。同支持域还允许罕见输入变成主流，不能冒充小shift保证。构造证明的是coding近最优不足，不证明真实优化器一定选该解；额外class-conditional稳定假设、语义保持干预或跨环境验证都有成本，未验证时仍回退切片、反事实和真实OOD行为测试。 [必要机制与边界](https://arxiv.org/html/2609.21001v1) <!-- source-family:SF-2026-ARXIV-2609-21001 -->

部署输入适配也面对这个问题。一条替代分支冻结原 classifier，只在测试时训练 input de-corruptor，使目标特征的高维几何 quantile 靠近保存的 source reference；CPU feature bank 与 snapshot center 汇集跨 batch 的目标人口。这把更新对象从分类器权重移到输入恢复，但边缘分布匹配仍可能交换类别，不保证 class-conditional 关系或标签语义被恢复，也不是 source-data-free 的无状态适配。<!-- source-family:SF-2026-ARXIV-2601-11022 -->

[必要机制与反侧](https://arxiv.org/html/2601.11022v1)在受限图像 corruption 上支持局部收益；相关理论还依赖 reconstructability、identifiability、分布 regularity 与局部良好初始化。适配器、source reference、跨 batch memory 与 quantile 计算均付费；作者披露的 H100、CIFAR100C/ResNet18、10k source features与batch128设置中，6.2M de-corruptor使peak memory从765到1429MB、每epoch从1.44到2.03s，不能写成冻结模型就无额外成本，也不是生产 inference SLO。分布或类别关系无法核实、状态污染或费用不合算时，保留原 classifier、输入质量切片与其他经独立验收的适配路径，不由匹配几何替最终任务签发保证。

训练两种增强视图的一致性，也可以把 agreement channel 与最终交付的表示分开。一条受限 self-distillation 分支让 EMA teacher 把投影 logits 阈值化为逐 bit target，student 用 BCE 拟合这些目标；连续、归一化的 pre-binary logits 再由 covariance log-determinant 正则约束，并可周期性重置投影 head。二值通道只组织训练监督，交付的 backbone 仍是连续表示，不是把全部语义压成固定 bit code，也不同于推理 artifact 的量化。 [必要机制与目标对照](https://arxiv.org/html/2602.09764v1)。<!-- source-family:SF-2026-ARXIV-2602-09764 -->

这把 target 离散化、逐 bit agreement 与表示分散程度变成不同可检验对象，而不是由 log-determinant 直接认证离散熵或互信息最优：student 实际还读取另一视图，不能假定仅由其 bit 表示恢复 teacher。受限同框架对照支持 BCE 接口，却显示更多 bits、更频繁 reset 不必更好，soft target 也可接近 hard target；effective rank 不是真实语义因子独立性的证明。额外 teacher、投影、正则与 reset 均付费，目标 collapse、跨环境失配或预算不合算时保留连续 self-distillation、原 head 与独立任务/OOD 验收，不让训练 channel 取得最终语义权。<!-- source-family:SF-2026-ARXIV-2602-09764 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21692:start -->
这个判断还可以获得一个更具体、但适用范围更窄的几何解释：若任务的数据空间近似为规则的紧致流形，模型已经充分优化，并且某类变换确实保持任务语义，那么数据流形与训练后模型预测空间之间的 representation gap 会受到任务 intrinsic dimension 支配。此时，equivariance 不只是架构偏好；它相当于把一个观测样本扩展为一组语义等价样本，从而降低需要由有限数据覆盖的有效维度。这解释了为什么与任务对称性匹配的表示可能改善样本效率，也把“归纳偏置有效”进一步落实为“它减少了哪些自由度”。

不过，这个量只拥有几何诊断权，不能接管泛化验收权。它依赖渐近样本、流形与群作用、充分优化等强假设，生成模型推导还集中于 DDIM 或线性高斯设置；估计过程本身也可能需要多个样本规模和多次模型拟合。若真实数据不存在所假设的对称性，或 intrinsic-dimension 估计与实际分布外表现不一致，就应回退到切片、反事实、held-out 与 distribution-shift evaluation，而不是把 representation gap 当作任意现代网络的通用 generalization error。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21692:end -->

因此，“模型学到了正确特征”不能只靠总体 accuracy 证明。需要构造切片、反事实、扰动和跨分布评估，检查模型究竟利用了什么相关性。

两个模型预测接近，也不必来自两者绝对误差都小。一条[受限midpoint分析](https://arxiv.org/html/2602.23360v1)在同分布MSE下定义预测平方差D与population risk：D=2(R1+R2−2Rmid)。若两模型均为函数族Fn上ε近population最优，且扩展族F2n可表达两预测的midpoint，则D≤4(R(Fn)−R(F2n)+ε)。ReLU DAG的闭包是把两计算图并排后平均输出，不是平均权重；强凸扩展要求prediction-space loss的曲率，也不是参数目标强凸。它把agreement关联到扩容可改善的风险差，而不认证truth：两个恒零模型面对标签一仍可D=0。普通SGD的低empirical loss没有验证population近最优，logits交叉熵也不具全域统一强凸。核这些前提与midpoint/扩容对照需额外模型和数据；前提不可核或分布变化时，保留真实错误率、独立held-out与OOD验收，不由agreement自动认定泛化。<!-- source-family:SF-2026-ARXIV-2602-23360 -->

表示诊断还要区分“固定一种表示后训练读出”与“用同一批样本选择表示再训练读出”。对一种受限Brownian kernel head，固定表示的activation mass给出经验复杂度的尺度；即使表示从该样本学来，这个条件化的经验恒等式仍成立。问题出在把它直接升级为整个选择过程的泛化界：候选表示的supremum必须保留，候选threshold traces可以增加选择自由度。一个等mass有限构造中，每个固定候选的复杂度随样本数下降，整族复杂度却不下降；因此压低同一mass不等于消除了选择成本。

这条边界属于Brownian terminal geometry及披露的ReLU、head norm和trace-envelope条件，不是任意Transformer的风险公式；最坏经验容量也不是minimax预测误差。若表示与head使用同一数据选型，必须记录候选族与选型数据，另做selection-aware分析或独立held-out验证；选择成本的测量与额外数据有代价。受限实验只展示固定mass下的union gap，冻结特征上的小幅head收益不能代替端到端学习证明；约束未核时保留普通训练、数据切分和任务验收，不把一个低复杂度诊断自动当成泛化证书。 [必要机制与边界](https://arxiv.org/html/2609.21422v1) <!-- source-family:SF-2026-ARXIV-2609-21422 -->

## 记忆与泛化不是简单对立

一个常见二分是：模型要么记忆训练数据，要么学习可泛化规律。实际网络可能同时做两件事。

高频、结构稳定的模式可以被压缩成共享特征；稀有或不规则样本可能通过更局部的参数配置被记住。甚至同一输出既依赖通用模式，也依赖训练中见过的特定关联。

可以从压缩视角形成直觉：如果许多样本共享结构，用一套可复用计算解释它们比逐个存储更经济；如果样本没有明显共享结构，过参数化模型仍可能拟合它们。这个直觉有助于理解表示，但不是对所有神经网络泛化的完整定理。

结构容易压缩，也不等于它对应真实规则。若错误各自需要不同例外，共享的正确规律可能更经济；若假规则本身简洁而一致，预测目标仍可能把它压成可复用计算。在一组[受控数学语料](https://arxiv.org/pdf/2603.11749v1)中，同一问题配对比较正确与错误 completion 的 NLL：随机错误下模型较常偏向正确答案，换成一致但错误的规则后则接近随机选择；假规则占比增大还会让这种选择偏向错误。它支持把“学到稳定结构”与“结构为真”分开，不证明现代大模型只按压缩率决定事实，也不把理想 description-length 直觉当作有限梯度训练的定理。

检查这种现象时，先固定要比较的对象：语料整体平均 loss 混合了频率、共同题型与文本长度，同题、同 prompt 下的 completion 比较才直接检验当前候选偏好；两者可以给出相反方向。配对比较仍要记录错误族、held-out 人口、长度处理与训练 seeds，较小显著性数值不消除训练不确定性，固定训练步数的尺寸趋势也不是同计算预算的 scaling law。更复杂的错误族须匹配自己的测试分布，不能借另一个规则族放大效果。新的语料构造、训练与验证均付费；缺少独立事实依据时，应保留外部检查、检索或拒答，不让低 NLL、规则一致或模型间 agreement 获得 truth 权。<!-- source-family:SF-2026-ARXIV-2603-11749 -->

这个视角还把闭卷事实错误拆成两个不能互相替代的问题：模型可能从未观察到相关事实，也可能观察过，却在有限参数容量中只能有损保存。前者是 coverage failure，增加相关数据或检索更直接；后者是 compression distortion，单纯重复相同事实未必消除，需要更多有效容量、更可压缩的结构、外部可寻址记忆，或在回答前允许检索与拒答。二者都会表现成“答错”，却要求不同补救；因此不能由最终准确率反推知识从未进入训练，也不能把扩大数据覆盖当作参数记忆无损的保证。

一个均匀随机事实映射下的 rate-distortion 下界只证明这种可分离失效在其假设中必然存在，不是现实 LLM 幻觉率公式。真实语言具有共享结构，模型还会使用上下文、推理、后训练和外部工具；这些机制可以改变有效压缩率或绕过闭卷回忆，但不会让有限参数自动获得“我是否可靠记住此事实”的校准能力。生产系统仍应把 retrieval、claim verification 与 abstention 作为独立证据路径。<!-- source-family:SF-2026-ARXIV-2609-12111 -->

判断泛化必须回到未见数据和部署分布。训练误差、validation 误差、数据去重、污染检查、时间切分和分布外评估分别回答不同问题。benchmark 得分高也可能来自训练数据污染或测试集与真实场景不一致。

对于生成模型，记忆还涉及隐私与版权风险。模型能够逐字复现某些训练片段，不等于全部知识都以逐字数据库形式存储；反过来，表示是分布式的也不意味着不会泄露具体样本。二者必须通过实证测试区分。

## 分布式表示与 Superposition

如果每个可解释特征都占据一个独立坐标，理解网络会容易很多。但网络的表示维度有限，潜在有用特征可能远多于维度，而且很多特征不会同时激活。模型可以让多个特征共享表示方向，以更高效地利用容量，这种现象常用 superposition 描述。

它带来一个 trade-off：共享可以提高表示容量，却增加干扰和解释难度。单个神经元可能是 polysemantic 的，一个概念也可能分布在多个方向上。通过 probing、activation patching、feature visualization 或 sparse decomposition 可以获得证据，但这些方法观察的是模型行为的某个投影，不应轻易升级为完整因果解释。

这里还要区分线性编码与线性访问。设输入特征为至多有 `k` 个非零分量的 `z∈[-1,1]^m`，表示是 `f=Az∈R^d`；这只约束编码方式。若再要求同一个线性 reader `Bᵀ` 对所有这样的输入都满足 `‖BᵀAz−z‖∞<ε`，就增加了统一恢复合同。允许非线性解码的压缩感知可以在 `O(k log(m/k))` 维度构造精确恢复；固定误差 ε 的线性恢复则有 `O_ε(k² log m)` 上界，以及在 `ε>√5 k^(3/2)/√m` 条件下的 `Ω_ε((k²/log k) log(m/k))` 下界。两界仍有对数差距，不能写成精确相等，但已说明压缩后的信息存在，不自动授予同样维度预算下的线性读取。

因此解释或设计 readout 时，应同时声明 reader 的函数类别、输入覆盖与允许误差，而不只统计可表示的方向数。干扰取决于 representation 方向 `a_j` 与 probe 方向 `b_i` 的交叉内积，不要求两组方向各自都正交；统一恢复连续幅值也不同于只在部分输入上做阈值分类。更强访问合同会增加维度、校准和核验成本，probe 失败却不能反推模型没有表示该信息。上述界属于明确的稀疏特征形式模型，不估计真实 LLM 的 feature 数，也不保证换成非线性 reader 就一定有效；假设或预算未成立时，保留局部 probe 的诊断角色与实际任务验证。[必要定义与容量边界](https://arxiv.org/html/2602.11246v1#S1.SS2)。<!-- source-family:SF-2026-ARXIV-2602-11246 -->

如果目标还包括让内部计算更容易拆解，另一条分支是把约束前移到训练，而不只分析已经形成的 dense 表示：训练时迫使大量连接权重为零，让网络在较少的连接中组织计算。这与事后用 sparse decomposition 提取特征不同，也不证明一个神经元只承担一种知识。在受限的简单算法任务中，可以继续剪除连接，检查留下的小 circuit 是否仍能完成任务，再删除其中关键边检验失效；这种充分性与必要性只相对于具体任务和干预成立，不证明它是唯一实现或完整解释。

连接约束又把能力、解释性和成本放到同一个选择中。固定模型规模下，更强稀疏可能损害能力；扩大模型可以改善所测能力—解释性前沿，却不等于等算力收益，更不保证更低的训练或部署成本。[稀疏网络的早期公开实验](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/)只解释了小模型的一部分简单行为，复杂计算仍有未解释部分。因此 dense 模型与事后分析继续是有效路径；只有解释需求足以承担容量及实现代价时，才值得考虑训练时连接约束，不能从局部 circuit 清晰直接推出前沿模型的可解释性或安全保证。
<!-- source-family:SF-2025-OPENAI-SPARSE-CIRCUITS -->

<!-- source-family:SF-2026-ARXIV-2605-00842:start -->
这种干扰不只发生在推理时，也会进入参数更新。若两个功能特征在共享表示空间中并不正交，针对其中一个方向的微调梯度就可能沿几何相似性同时放大另一个方向；原本为了节省维度而成立的 superposition，因而把“只修改目标行为”的局部假设改成了耦合更新问题。它解释了为什么窄任务数据可能在训练 loss 正常下降时，引起表面无关的行为变化，也说明只监控目标任务 accuracy 或参数距离不足以拥有微调安全结论。

这个机制把微调验收从单任务改成受影响行为集合：训练系统应保存数据、checkpoint 与更新范围，在提交新 artifact 前重跑目标能力和关键安全切片；几何邻近或 SAE feature 可以用于定位风险样本和提出诊断，却不能单独证明因果或替代行为回归。现有证据只在 Gemma、Llama 与 gpt-oss 的若干开放模型上，以共享 SAE basis、cosine similarity 和 LLM judge 检验局部几何假设；它没有证明所有表示都遵循同一坐标、所有邻近特征都会共同更新，或几何过滤能跨模型稳定校准。信号失配时，应回到隔离或移除可疑数据、缩小更新范围并执行完整安全回归，而不是把一个可解释性 proxy 升级为自动发布门禁。
<!-- source-family:SF-2026-ARXIV-2605-00842:end -->

共享方向带来的干扰还取决于 readout 是否只能做线性叠加。线性 readout 会把非目标特征的投影一起带入，
因而存在随共享密度上升的 cross-talk floor；在一类递归 superposition 模型中，引入非线性 threshold
可以在每层重新压低小幅串扰、保留显著信号，相当于重置下一层看到的噪声底。它用阈值选择带来的
不可微边界、校准敏感性和弱信号丢失，换取比纯线性递归更大的可分离容量；特征近似正交、表示稀疏或
需要保留连续幅值时，线性 readout 仍是更稳妥的基线。该结论来自特定形式模型与有限 empirical context，
不证明真实 LLM 普遍执行同一 threshold-reset 算法。
<!-- source-family:SF-2026-ARXIV-2605-01192 -->

深层非线性网络也不能只用“总深度越大越容易逃离 saddle”解释优化。一类理论结果把逃逸条件收紧到
具有瓶颈尺度的非线性层数及其 imbalance，而不是所有层的简单计数：额外层若没有改变有效瓶颈与局部
几何，可能只增加路径长度，并不提供新的逃逸方向。这个判断提醒系统把 architecture shape、activation
class 与局部曲率一起记录；它不构成对任意 Transformer loss landscape 的普遍定理，假设不满足时仍应
依赖实际 curvature、gradient 与多 seed 训练证据。
<!-- source-family:SF-2026-ARXIV-2605-01288 -->

共享概念方向还不足以表达关系：同样包含“老师”和“摄影师”，谁跟随谁仍取决于施事与受事的绑定。分布式表示可以同时编码 filler 与 role，例如用各项张量积之和表达绑定；在角色向量独立等条件下可以解绑定，但这只是一种解释模型，不意味着网络实际执行了张量积程序。冻结表示的拟合、角色干预与局部替换可以检验这种结构是否可用，代价是人工角色方案与近似误差；表征可组合也不保证模型在新任务上行为可组合泛化。

完成同一关系题，也可能走位置捷径而非内容绑定。一个有界诊断先配对原题与 counterfactual：保留内容、改变位置，再保留位置、替换内容，沿对应 activation 做 interchange intervention，观察答案跟随哪一种变化；probe 与 knockout 只是辅助定位，后期可读出答案的层不一定是最早执行绑定的层。这把“模型会答题”推进为对替代计算路径的检验，不能仅凭可解码角色标签断言使用了抽象绑定。[必要配对干预](https://arxiv.org/html/2602.15183v1)只在有限合成 color→shape→item 任务及小模型训练中支持这一区分。<!-- source-family:SF-2026-ARXIV-2602-15183 -->

内容路径的出现也不能单独归功于加入图像。该研究的视觉 curriculum 同时涉及噪声前置训练、feature-grounding 辅助目标、混合比例、词表与训练预算变化；合成 OOD 的局部改善因此是整个训练 bundle 的证据，不是 image-only 的唯一因果。部分分支发散被剔除，noise/text 路线也改善外推，跨大模型 checkpoint 的相关性还未控制训练差异。配对干预、额外 encoder 与训练均有成本；当任务、位置分布或可访问长度改变，应重新验收内容替换与位置替换，保留原 role/filler 解释和行为测试，不许把局部 content binding 签成任意长度、任意任务的泛化保证。

线性化结构还有一种不同于内容相似的地址信号：在序列化表格中，查询先绑定行列 header，随后可以利用分隔符携带的序数位置定位 cell；同一个答案依赖语义绑定与结构定位，不意味着二者由同一组 head 或同一层完成。[受限合成表对照](https://arxiv.org/html/2602.08548v1#S4)中，delimiter 坐标较早可被线性读出，新增分隔符与等长度无分隔字符对定位的影响不同，提示结构边界不应被 token 距离替代；这不是精确计数器或语义完全退出的证明。局部 activation 差方向还能推动 column 选择，但其 layer、token span、校准表、offset 和幅度均属干预身份，normalized logit effect 不等正确率，向量相加也不能签发任意位置可靠性。Probe、配对标记干预与行为回归需要额外样本和费用；格式、尺寸或内容改变时应重新核结构/语义两条路径及非目标损害，保留原模型、明确表格 parser 或独立结果验证，不把可读 ordinal 表示升级为通用 table 执行器。<!-- source-family:SF-2026-ARXIV-2602-08548 -->

多句话中同一实体还可能承担不同关系，因此仅记录“哪个实体”不足以确定属性该绑定到哪里。一种受限的机制假说把地址拆为 entity 与 relation 两个索引：在受控文本中，先用属性 token 的 activation 拟合索引，再沿拟合的子空间替换或扰动，检验输出是否跟随指定绑定变化。这比只凭语义相似或角色标签多了一步局部使用证据；但拟合出的 cell 不证明网络拥有物理表格、唯一符号地址或开放任务上的稳定读写协议。<!-- source-family:SF-2026-ARXIV-2604-19052 -->

同一关系结构跨语境也未必沿用同一读出坐标。作者在有限合成域中观察到原投影跨 context 退化，而根据相同索引的 activation 差拟合 translation 后，部分读出得以恢复；这种校准需要配对数据，也受上下文和干预范围约束。因此，可迁移几何、局部行为作用与任务泛化须分别验收；坐标失配或 patch 连带影响其他功能时，应回退行为测试和原模型，不能把 probe 升级为通用编辑器。

读出坐标会漂移，还不等于控制方向一定失效；反过来，在一种 context 内有效的 steering 也不能直接移植到另一种 context。一个受限检验先在答案生成前的 token 上拟合预测 Yes/No 的方向，再冻结该方向，比较空 context 与完整对话中的干预效果：同样的方向在一组主题对话后改变了输出偏置的极性，在另一组对话中却保持原来的作用。因此方向、层、token 位置、拟合数据与 context revision 必须共同成为干预身份，不能用一次长对话成功认证跨语境可移植性。<!-- source-family:SF-2026-ARXIV-2601-20834 -->

这里的干预方向不同于答案生成后的 factuality probe，不能把两项结果拼成“读出的事实概念拥有同一因果作用”，更不证明意识、信念或参数知识发生改变。[必要对照](https://arxiv.org/html/2601.20834v1)只有少量对话和概念，模型、层选择与问题集合限制其范围，内部变化机制仍未建立。配对 context、行为测试和强度校准增加调用成本；上下文身份改变或效果极性未重新验收时，应停止沿旧方向控制，回退原模型与外部行为级验证，不能仅翻转 probe 阈值后继续当作通用编辑器。

表示方向的长度与夹角还未必对应行为分布的改变。若输出由 softmax 定义，同一隐藏向量的欧氏移动与输出 KL 预算是两个对象；可以以 log-normalizer 的 Bregman 几何描述后者，把各 token 的 unembedding 按当前概率求期望作为 dual 坐标。在固定且准确的 linear probe、指定目标 hyperplane、约束 minimizer 存在等条件下，最小 forward-KL 的 dual 位移沿 probe 方向；只有初点和整条目标 hyperplane 都满足相应 concept-factorizability，使目标概率项在约束集合内固定时，才可进一步解释为最小 off-target KL。这里的“最小”不表示 off-target 完全不变，也不能把 expected-unembedding 的匹配解释成整个概率分布的线性混合。[必要信息几何条件](https://arxiv.org/html/2602.15293v1)因此限定的是一条控制分支，不把所有欧氏 steering 宣判为错误。<!-- source-family:SF-2026-ARXIV-2602-15293 -->

这条几何分支增加 covariance Hessian 的估计与求解成本，dual 坐标还受 unembedding convex hull 可达性限制；数值低秩、regularized Newton 与步长归一化只近似理想路径，不能沿用精确 minimizer 的保证。受限实验中，probe 在测试样本可分，沿 steering 路径的同一 probe projection 却未保持相同目标 logit，显示最关键的目标超平面假设可能失配；结果还依赖筛过的 context、token pair、词表截断与路径停止规则，不授任意语义控制或生产延迟。目标不足、非目标损害或求解费用不合算时，应保留独立行为回归和已校准的原路径；counterfactual mass 稳定时，原 Euclidean 分支也有成立条件，不能用新坐标替代实证验收。

单一数据域的probe跨域失效，并不能推出不存在共享表示；联合多个域训练得到的读出方向，也不能推出每个域都使用同一条控制方向。可以先在联合域拟合方向、投影其线性可读部分，再在剩余表示上拟合各域方向，检验一般、部分共享与特定方向是否并存。比较两个probe时，若activation高度各向异性，普通Euclidean夹角还会被几乎不变化的维度干扰；按目标分布covariance重加权的夹角更接近该分布下的读出对齐，但依赖目标样本与估计质量，不是未知域上的truth证书。<!-- source-family:SF-2026-ARXIV-2602-20273 -->

这条读出分支仍需独立行为反侧：[有限truthfulness实验](https://arxiv.org/html/2602.20273v1#S8)中，多域方向可读出一般信息，却在事实问答的log-probability干预中不如部分特定域方向；效果主要是强化本来正确答案的相对置信，不是可靠把错误答案改对。概念投影未必完整擦除、模型生成标签会有偏差，线性分析也不覆盖新欺骗类型。多域标注、covariance估计与逐条件干预增加成本；目标数据不足、方向移植未验收或非目标行为受损时，保留原probe诊断与外部行为验证，不把monitor升级为通用控制器。

表示的有效维度也只是测量量，而非性能证书。把unembedding奇异值归一化后，用谱熵定义effective rank，可以诊断输出方向是否集中；但训练batch、weight decay与learning-rate schedule会同时改变该几何与优化结果。要判断rank是否解释能力，至少在相同模型、数据与训练配置内比较，并把ID loss、迁移、量化鲁棒性分别测量，不能把“更高rank”直接设成训练或发布目标。<!-- source-family:SF-2026-ARXIV-2602-20433 -->

[有限小模型对照](https://arxiv.org/html/2602.20433v1#S4)中，大batch或较弱annealing能保留高rank却未改善loss，weight decay的收益随模型规模改变；量化脆弱性也不服从一个通用rank阈值。这些是训练条件下的反例，不证明直接改变rank一定无效或所有层/大模型都相同。记录谱量、训练revision与额外测量成本，配置漂移或行为评价冲突时回退实际任务loss与独立验证，仍保留几何sensor用于诊断，而不让它替性能或因果验收。

还可以只约束原 activation 空间中的长度，而不直接优化输出 KL。固定 additive edit 同时改变方向与范数；若要把二者的作用拆开，可以先由配对样本的均值差确定单位目标方向，再将当前 activation 归一化，沿球面插值转向目标，最后恢复原范数。这样保留的是一个几何量，不是输出分布、真值或全部功能；它与前面的 output-KL 分支是不同约束下的替代路径，不能互相继承保证。<!-- source-family:SF-2026-ARXIV-2602-08169 -->

是否干预还可与干预强度分开：用相反方向的球面 prototype 给出局部分数，再按阈值选择哪些 activation 进入旋转路径。但 prototype 分数不是已校准的真假概率，方向、层、token population 与 context 仍要共同绑定，配对样本、阈值搜索和逐 token 白盒计算也有成本。[有限球面 steering 对照](https://arxiv.org/html/2602.08169v1#S3)中，TruthfulQA 的选择题与生成评价并非全面同向，保范数的强干预仍可损害信息量；base 与 instruction 模型也不能合并为同一 operating point。因此必须联合检查候选答案 likelihood、生成真值与信息量，不能以 norm 不变签发“无损控制”。方向或 gate 失配、非目标行为退步时，回退原模型与已校准的行为验证，既保留 additive 路径，也不由局部结果推断所有 context 中与 ICL 正交。

尤其要区分三种结论：

```text
correlation: an activation co-occurs with a concept
prediction: an activation can predict a concept label
causation: changing the activation changes model behavior as claimed
```

线性 probe 能从表示中读出信息，不一定证明模型在原任务中使用了该信息；干预某个方向导致输出变化，也需要排除连带影响。可解释性不是给每个参数命名，而是建立可复现、可反驳的内部机制证据。

### 从可读出到机制：证据应逐级变强

内部分析至少要区分一条证据阶梯：

```text
behavioral correlation
→ decodability
→ localized intervention
→ downstream behavioral change
→ cross-context / cross-model replication
```

前两层可以发现“某种信息存在于 activation 中”，却没有证明原始 forward path 依赖它。
更强的主张需要在控制混杂因素的前提下修改候选表示，并观察预期的 downstream computation
或行为是否随之改变；即使如此，单个 prompt、单个模型家族或局部线性近似上的效果仍不是
完整机制。

除了观察 activation 共现，还可以问：在当前解附近轻微改变学习压力，哪些表示会一起响应？一条局部诊断分支围绕已有权重建立带温度的 localized posterior，用采样权重下 observable 与“单 token loss 减总体 loss”的负协方差估计 susceptibility。这里 observable 可以是 activation，也可以是 loss；差额在于把 token 的相对学习压力与内部响应联系起来，而不只是从固定 activation 中解码标签。未知真实数据分布的 mode-pair 展开提供解释，但这些模态并非实验中直接测得，协方差估计也不是已经逐 token 重训完成的真实干预。

温度、局部范围、采样混合、数据 population 与归一化都改变诊断对象；SGLD 采样、构建 token 响应图及聚类还增加成本。[局部响应研究](https://arxiv.org/html/2601.12703v1#S2)在受限 Pythia 实验中观察到同一 token 按功能分开、不同 token 按功能聚合，但跨模型尺度及 SAE 的比较并不是一一功能定位，更不证明唯一 causal circuit。它因此补充了证据阶梯的候选发现分支；采样不稳、归一化敏感或需要行为因果判断时，仍回到 activation/probe 基线与受控干预，不能把响应簇作为内部机制的最终字典。<!-- source-family:SF-2026-ARXIV-2601-12703 -->

这条证据阶梯也适用于模型自己的解释。问模型“你刚才在想什么”，得到的仍是生成文本，不是直接读取的内部计算记录；准确的描述可能来自训练中学到的说法，也可能只是根据已经说出的内容反推。要检验描述是否依赖内部状态，可以保持可见输入不变，在指定层注入概念方向，再比较无干预、随机概念及不同注入时机的报告。若模型在说出该概念之前就识别到变化，而且仍能正确复述原输入，才获得了比自述可信更窄的证据：这次报告使用了某种内部信息，而不是单纯抄读输入或事后解释输出。

这种诊断增加配对试验、层与强度搜索以及独立评价的成本，还可能被提示方式、输出偏置和干预损伤混淆。[受控概念注入研究](https://transformer-circuits.pub/2025/introspection/index.html)在部分 Claude 模型上发现了这种局部能力，但多数试验仍失败，也没有直接定位完整的元认知表示。因而局部自述与内部状态之间的因果联系，不等于自然任务中可靠的自我审计，更不证明意识或全部解释真实。条件失配时，仍应回到外部行为测试和受控干预，而不能让模型为自己的计算过程签发正确性证明。<!-- source-family:SF-2025-ANTHROPIC-INTROSPECTION -->

局部干预还须说明后续计算有没有重新采样。一条受限路径固定已经实现的 prefix 与 continuation，只在 receiver 的 Attention 中遮住候选 trace span，再测 next-token 分布怎样变化；它隔离的是“在这条续写上，哪段历史被当前读路径使用”，不等于删除后重新 rollout 会产生什么答案。以固定 stride 切 span、按 entropy/JS 选接收位置可能偏向更显著的局部效应，因而需保留匹配随机位置对照、候选选择与额外 forward 成本。[DRTC 的有限 reasoning 对照](https://arxiv.org/html/2602.15332v1#S4)支持读路径依赖，却没有证明该 span 对最终正确性必要或有益；存在替代路线、模板或选择分布变化时，仍应重新生成并独立检查行为结果，不能把固定续写的因果测量升格为整条 reasoning 的正确性证书。<!-- source-family:SF-2026-ARXIV-2602-15332 -->

Jacobian-adjusted lens 一类方法提供了一个具体例子：它不直接把中间 activation 投影到
最终词表，而是用该 activation 对后续 residual 的局部 Jacobian 近似 layer-to-output
影响，再配合 activation swap、ablation 或 modulation 检查候选方向是否被计算使用。
这个方法的重要性不在于给出又一种“可视化”，而在于把 readout 与 intervention 放进同一
实验链。其局部一阶近似、跨 context averaging、token-indexed representation 与模型范围
仍限制外推，因此它是证据阶梯的实例，不是模型内部知识的最终字典。

局部edge归因还必须能组成真正可执行的子网络。只保留top-K高分edge可能切断input→output路径；一个受限构建先把候选edge补成完整路径，再分别保留该子网和移除它，检验行为充分性与必要性。[有限GNN机制实验](https://arxiv.org/html/2602.21442v1)还显示，高OOD成功可共享另一个任务的shortcut读出，并不证明两个独立算法。配对输入、归因积分、路径构建与retain/remove运行均增加成本，probe人口和平均分数也可隐藏差异；原部分fidelity公式方向有问题，不能以其headline替代实际干预结果。条件或路径不成立时保留完整网络、多控制和独立行为验证，不把可解码或高分电路称为唯一最小因果程序。<!-- source-family:SF-2026-ARXIV-2602-21442 -->

### 信息存在、可读与被使用是三个不同命题

表示中的“可读”必须拆成三层：信息存在、独立 reader 能解码、模型行为实际使用该信息。让 verbalizer 与 reconstructor 共同训练并以 reconstruction 评分，可能形成只在二者之间有效的 private code；高 reconstruction 因而不能证明具体自然语言 claim grounded。

更强的 contract 是用外部 ground-truth target 约束 decodability，并由与训练 reader 独立的 fresh probe 审计。它减少训练 reader 与表示共同作弊的循环性，却仍受 probe drift、目标遗漏和 correlation≠causation 限制；因果使用仍必须回到 intervention 与 downstream behavior。

“Probe 读对、模型答错”还要分清 output scores 与最终选择。Candidate logits 可能完整保留标签信息，argmax 却选错；例如标签为0/1、某个 logit 随标签变化但始终低于另一常量，外部 reader 能读出标签而 argmax 恒定。检验最终表示到 logits 是否丢信息，应在同一 held-out trial、匹配 decoder 能力与校准下比较 state decoder 和 score decoder，不把 probe 对比错误答案的差距直接命名为 readout information loss。

即使 probe-guided steering 修复部分错误，也不证明原路径用了该方向，或修复率的变化只来自表示改善。需同时记录损害原正确答案、oracle/probe/wrong-target配对结果，以及目标质量和干预敏感性；旧 probe 与新 checkpoint 不兼容也不能自动叫信息消失。受限 binding 对照未在晚 checkpoint 检出 state 相对 logits 的优势，computed-state 对照又受表面信息和错误样本数限制，因此不外推为 Agent 漏动作的因果解释。协议失配或样本不足时，保留普通输出与行为验收，不把解释性 probe 当自动修复授权。[必要反证与评价](https://arxiv.org/html/2609.31401v1) <!-- source-family:SF-2026-ARXIV-2609-31401 -->

行为长期停滞时，还需要定位学习链中哪一段受阻，而不是把低准确率直接解释成“表示尚未形成”。在可拆分的 encoder–decoder 中，可以把成熟 encoder 接到新 decoder，反向移植 decoder 作对照，再冻结 encoder、重置或回退 decoder 后继续训练：前者检验既有表示是否足以支持新的读出，后者检验原读出路径是否成为瓶颈。受控算术任务上的这些干预能支持“结构已出现、行为尚未取用”的局部诊断，但不证明任意模型的停滞都来自 decoder，也不把获得成熟 encoder 的前期训练算作零成本。

这条诊断增加模块移植、训练轨迹和多 seed 对照的成本，模块接口、编码方式与样本覆盖也会改变结果；表征退化时，冻结成熟模块并不能补救，某任务形成的结构也可能无法迁移到另一任务。旧的端到端训练与 probe 因而仍是基线：先用读出和干预区分形成、访问与使用失败，再决定补数据、修表示或训练访问路径，不能只凭一个加速比例替换整个训练方案。<!-- source-family:SF-2026-ARXIV-2604-13082 -->

后训练改变行为后，“哪些参数改动足以恢复所测内部状态”与“哪条 activation 路径传递了变化”是两个不同问题。在架构相同、输入固定、比较 anchor 匹配的两个 checkpoint 之间，可将候选参数单元从后训练模型移植回基础模型，先检验它是否恢复所测 anchor 状态，再独立核对相应行为；activation relay 则检查差异怎样沿运行中的计算传递。内部恢复不等于端到端行为已恢复。Attention 的 Q/O 单元与同一 MLP neuron 的 gate/up/down 参数对应不同干预粒度，梯度可用于缩小候选，却不能替代实际参数替换、输出分布和行为任务的分别验收。

参数替换得到的是相对于这对 checkpoint、输入与干预粒度的充分性证据，不是唯一知识源头或所有行为的通用定位；现有检验只在六个代表任务上支持稳定性。模块间冗余、交互及改变输入后的失效仍需单独检查，局部恢复也可能损害其他任务。它因此补充而不替代 activation patching、黑盒行为评测与更细干预；将 source-level 参数差异与运行期中继分账，才能避免把“在某层看到信号”误写成“知识唯一存储于该层”。<!-- source-family:SF-2026-ARXIV-2604-13694 -->

行为不能取用已学事实时，也不一定只能继续补知识。训练期 augmentation 把预期的逆关系或组合答案提前写进样本，在查询结构稳定时直接有效；另一分支训练模型在推理时召回、组合和自验参数知识，将额外计算放在访问路径上。受控实验先用 SFT 写入事实，再以答案条件化的 teacher traces 启动 thinking，并用 correctness feedback 训练：所测 Gemini 2.5 Flash 在只经历事实学习、未经历该 thinking/RL 训练的新知识上仍能改善部分潜在推导。这是访问策略迁移的证据，不是任意未见知识都会自动泛化。<!-- source-family:SF-2026-ARXIV-2604-01430 -->

尤其不能把“生成候选后按正向关系自验”写成“学会直接求逆”。纯逆关系没有可组合中间路径，成功仍依赖先提出正确实体及可靠自验；单次成功率低于把完整事实放入上下文的 ICL 对照，多次尝试的 pass@N 也不等于部署时能识别正确答案。Thinking 增加训练和生成成本，自验还可能重复参数中的错误；稳定关系可继续用显式 augmentation，事实可检索时保留外部证据路径，而不能用更长推理代替事实核验。

### 解释模型也有自己的 Faithfulness Budget

当研究者用 sparse features、transcoder 或 attribution graph 替代原模型的一部分计算时，
得到的是一个 **解释用 replacement model**，不是原模型本身。它至少引入四类差距：feature
dictionary 无法重构的 error nodes、未被替换的 attention/QK path、为可读性做的 graph pruning，
以及人类对 features 和 supernodes 的命名。图更小、更可读，通常意味着保留的计算更不完整。

因此 circuit evidence 应同时报告：replacement reconstruction error、pruning threshold 与 graph
completeness、在原模型上的 intervention，以及 prompt/model selection 范围。若干选定案例能被
干预复现，只能证明方法在这些 cases 中生成了可检验 hypothesis；不能推出整张图完整、feature
label 唯一，或模型普遍按该叙述“思考”。旧的 probe、activation patching 和黑盒行为评测仍然
成立：它们成本更低、回答的问题不同，并且可以用来交叉检查 replacement model 的盲区。

在这一预算内，选择电路还可用原模型输出约束联合门控，而非逐次手工构造corrupted input：对node/edge activation插入sigmoid门，把削弱的部分换成batch均值/方差Gaussian噪声，联合拟合output-KL，再按阈值保留组件。[IBCircuit v1](https://arxiv.org/html/2602.22581v1)支持这一受限经验分支，不是“无噪声”或唯一因果电路；其评价仍使用corrupted activation patch，任务分数与输出fidelity亦不同。所写Eq9的负A进入log未定义，Eq28也不等于逐项Gaussian KL之和，完整IB/闭式保证不采用，更不据此指控未核代码。有限GPT-2的IOI/Greater-Than对照中，ACDC在部分低node范围更强，增大正则会损害KL。门训练、阈值搜索及评测付费，hardware/precision未披露；只采用可核的局部控制结果，目标或干预失配时回退原patching、完整模型和黑盒行为验收。<!-- source-family:SF-2026-ARXIV-2602-22581 -->

紧凑子空间还应同时满足“由所测输入激活”与“对指定输出有影响”，不能只按activation方差选方向。一条[任务条件core提取分支](https://arxiv.org/html/2602.22600v1)用中心化activation矩阵H和task-output Jacobian J的交互HJᵀ做SVD，再映回activation span，以keep/remove/flip分别验充分性、必要性和方向控制。跨seed原坐标可以近乎正交而具有相近task spectra，几何比较与干预角色因而分开。该core绑定样本、输出定义、rank阈值与选层；GPT-2末层语法的线性readout可直接生成一维轴，不能证明所有内部语法算法唯一一维，其他全维consensus删除后也未普遍崩溃。提取使用全部测试activations，不冒充独立held-out发现；Jacobian/activation、rank搜索和每token多次steering均付费。任务人口、输出或干预有效性变化时，保留普通probe、原activation patching与完整模型任务对照，不以core一致性认证真实语义。<!-- source-family:SF-2026-ARXIV-2602-22600 -->

有限案例上的 circuit 干预还可扩展为有明确输入域的验证规格：在参考输入的扰动球内，要求同一输入上的子电路与完整模型维持规定的输出 logit-gap；可达 activation patching 则从另一个合法输入计算被替换部分的状态，再把所保留的路径与参考输入组合。这里双输入与可达状态的约束不能换成任意 activation box，sound verifier 的证书也只覆盖指定范数、半径、输出关系与干预算子，不认证外部事实或唯一真实机制。贪心搜索要得到 subset-minimal，还需该规格对扩张子电路单调；可达集合的拼接闭包是额外充分条件，不是所有网络默认满足的性质，截断 hitting-set 搜索只给大小下界，所得电路仍须验证。[受限小网络验证](https://arxiv.org/html/2602.16823v1)的 neuron/filter 粒度与运行时间不能外推为 LLM 可扩展性；规格不适用、验证超时或单调条件不明时，保留有限案例 patching 与完整模型行为检验，而不把未获证书等同于没有有效电路。<!-- source-family:SF-2026-ARXIV-2602-16823 -->

干预目标本身也要保留算子的竞争关系。用某条 Query–Key 路径的线性相对贡献筛 circuit，在快速定位时是合理代理；移除部分计算后，Softmax 的同一 row 分母和其他 key 的权重却都会改变，代理下降不等于原 attention 权重同样下降。一条更受控的分支重算移除后的 score 与整 row Softmax，以实际 counterfactual weight 变化作为选择目标，再追溯 upstream components；竞争 key 的负贡献不能仅因符号被抹去。这增加反事实前向和方向分解成本，按阈值贪心删减也不认证全局最小或唯一 circuit。所测正确 IOI prompts 中，不同结构可沿替代路线完成任务，自动解释/fuzz 得分仍非真实 feature；目标、prompt 人口或干预有效性变化时，保留原 activation patching、黑盒行为与完整模型对照，不由更小的图取得普遍机制证书。<!-- source-family:SF-2026-ARXIV-2602-13483 -->

重构与稀疏目标合理地要求 dictionary 保留输入、限制激活容量，却没有直接要求同一 feature 激活的样本在外部语义空间中一致。一条可选分支是固定外部 encoder，用它的单位向量 $h_n$ 定义样本相似性，再把这种一致性作为辅助目标，而非事后标签。设某 feature 的归一化激活为 $a_n$，累积 $u=\sum_n a_n$、$v=\sum_n a_n^2$、$w=\sum_n a_nh_n$，则 pairwise cosine 加权均值的分子、分母分别等于 $(\|w\|^2-v)/2$ 与 $(u^2-v)/2$。这消去了显式样本对：对 $B$ 个样本、$M$ 个 features、$d$ 维外部表示，聚合算术成本为 $O(BdM)$，并需维护 $d\times M$ 统计。因而可以在保留原重构/稀疏目标的同时，加上带权重 $\lambda$ 的“1 减有效 batch scores 均值”。这是[外部一致性辅助训练的一种具体实现](https://arxiv.org/html/2602.12403v1)，不是学到了真实 feature 的证书。<!-- source-family:SF-2026-ARXIV-2602-12403 -->

这条分支把外部 encoder 的语义偏好带进了 dictionary，必须保留 encoder、激活归一化范围、batch population 与 $\lambda$ 的身份。数值为零的分母对应无有效共同激活，应从均值中排除；batch proxy 不自动等于全数据目标的无偏梯度，预提取 embedding、min–max 准备与统计驻留也不是免费成本。更高一致性可能只来自更窄的激活覆盖，或付出重构下降；应在匹配数据、稀疏度与训练预算下，同时检查 held-out reconstruction、coverage、独立 probe 和原模型干预，不能拿外部空间的自洽代替原模型因果。当一致性收益依赖 encoder 偏差、覆盖收缩或不合适的正则权重时，保留普通 SAE 与仅事后评价的分支，再用下面的随机/冻结基线检查额外学习贡献。

解释用 dictionary 的评价还要问：这些成绩究竟增加了多少由学习得到的 feature alignment？仅优化重构并得到可读标签，甚至在局部干预任务上有效，都可能不足以回答它。一个可执行的 null test 是固定随机初始化的 decoder 方向而继续训练 encoder，反向固定 encoder 而训练 decoder，或限制 decoder 只能在接近初始化的角度内变化，再与同数据、字典规模、稀疏度和训练预算的完整模型比较。这里随机或冻结的只是部分组件，soft-frozen 仍能学习，因而不是“完全随机、未经训练的模型”。大字典中的偶然相关与其他可训练组件都可能承担任务收益；应将重构、标签预测、sparse probing 与实际 feature recovery 分账，比较额外学习贡献，而不是让任何一个高分自行签发内部机制证书。

[受限的 SAE null-baseline 检验](https://arxiv.org/html/2602.14111v1)在独立激活的合成 feature 数据上，发现较高 explained variance 可以伴随很少的 ground-truth 方向恢复；在所测 Gemma/Llama 层与标准 SAE 中，部分冻结基线也保有可读性、probe 和 RAVEL 编辑能力。RAVEL 还另训干预 mask，soft-frozen 方向并非完全不变，所以编辑效用既不证明字典方向全是随机，也不证明它恢复了唯一真实 feature。建立这些基线增加训练、字典规模控制和评价成本；合成独立激活、有限模型层与代理任务不能外推 transcoders、crosscoders 或所有 SAE 无用。无法超过合适 null baseline 时，保留局部操作价值并收窄 feature-learning 解释，继续用原模型干预与独立行为检验，而不把学习失败与模型没有相应能力混为一谈。<!-- source-family:SF-2026-ARXIV-2602-14111 -->

局部操作价值还取决于如何构造干预方向。凭 feature 名称选少数方向，或对两个完整 prompt 的 activation 求均值差，都会混入不同 token 与上下文组成。一条更受控的分支固定同一个 semantic core，比较它单独出现与放入不同 wrapper 时的对应 token：在配对差值上统计筛选、排序 SAE features，再选择修改的 feature 数量与强度。[同 core 的上下文对照](https://arxiv.org/html/2602.12418v1)因此回答“这组上下文变化下哪些方向有操作价值”，不是认证 feature 标签、唯一因果方向或所有相关性都可靠；token 边界匹配、model/layer/SAE 与筛选人口必须保留。原文允许边界少量 token 差异，统计阈值与排名也仍是启发式选择。<!-- source-family:SF-2026-ARXIV-2602-12418 -->

修改 sparse latent 时还应避免把 dictionary 的重构误差一并删掉。设原 activation 为 $h$，$z=\mathrm{encode}(h)$，干预得到 $z'$，可用 $h'=\mathrm{decode}(z')+[h-\mathrm{decode}(z)]$ 加回原 residual；于是实际改变只有 $\mathrm{decode}(z')-\mathrm{decode}(z)$，并不意味着原重构误差得到纠正。该分支增加 SAE 编解码、配对校准与参数 sweep 的成本，feature 数量和强度须与任务效用分别验收：所测 jailbreak 缓解伴随 instruction-following 下降，有限 held-out wrapper 不覆盖 adaptive 或 gradient 攻击。全 prompt 均值对照还混有 token 选择差异，不能把全部收益归于 sparse 空间。操作失准时保留原 activation、较弱干预和独立行为检验；模型外的权限与执行控制仍由安全章节负责，不由内部方向签发安全保证。

训练一个能把 activation 翻译成文字的解释器，还会引入标签分布的先验。冻结原模型、只训练 activation adapter，可以让解释更流畅，却不保证描述来自待解释向量：affine map 的 bias 在零输入时仍能生成符合训练标签风格的输出。因此要将 null-input 或 bias-only 输出与真实 activation 条件输出分开比较，先估计解释器默认会说什么，再检查输入究竟增加了哪些可复核信息。<!-- source-family:SF-2026-ARXIV-2602-10352 -->

[必要的零向量对照](https://arxiv.org/html/2602.10352v1)显示 SAE 与 Wikipedia 标签训练出的默认解释不同，bias-alone 也承担大量拟合改善；这些定性样例不是 feature 真实语义或推理因果的证书。训练 adapter、标签审核与原模型干预都有成本，筛选已答对的 bridge 人口还限制泛化。标签或 null 对照失准时，保留原 activation、独立 probe 与行为干预，不能用一个自洽文字解释覆盖 faithfulness 的缺口。

表示是否在最终层保留某类信息，还取决于训练目标把监督放在什么位置、覆盖哪些 token。只预测
被 mask 的局部目标，可能让中间层保留纹理和运动细节，却允许最终层把容量收缩到更利于全局语义
预测的方向；这不等于局部信息从整个网络消失。若下游既需要局部可读出性又需要全局语义，一条
演进分支是扩大 target coverage，并把 self-supervision 放到多个深度：

```text
single final-layer objective
-> masked/local target prediction
-> visible + masked target coverage
-> deep supervision across selected layers
-> layer-wise probe and intervention under matched compute
```

这会缩短早期层到监督信号的路径，也会让 local detail 与 global abstraction 竞争同一表示预算；更密的
loss 还增加 compute、loss weighting 与 optimization coupling。V-JEPA 2.1 的受限消融支持这种目标覆盖与
深度监督可以移动信息在层间的分布，但不能证明 dense objective 普遍更优，也不能把 probe 读出直接当作
下游因果使用。只需要全局语义的模型仍可能受益于较窄目标；需要定位、跟踪或物理控制时，才应把局部
信息保留作为明确 contract，并用 intervention 和 downstream task 验证。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21849:start -->
解释器本身也会遭遇 distribution shift。固定 dictionary 或 replacement model 在训练分布上重构良好，不代表部署 activation 仍落在同一子空间；一种受限修复是在冻结原模型的同时，用无标签部署激活重新适配解释几何。这里 adaptation 只拥有 replacement-model 修复权，重构误差、跨 seed 稳定性、原模型 intervention 与端到端行为共同拥有 faithfulness 判断，不能从适配后的可读 feature 反推唯一机制或稳定语义。

在线适配增加 activation 收集、版本化、污染和跨版本不可比风险。exact-v1 只支持作者的 OOD activation、dictionary 与 circuit attribution 实验，不证明原模型机制在开放分布中已被恢复；若 reconstruction、intervention fidelity 或稳定性未恢复，应把结论降级为相关性观察，回退原 dictionary、多 probe、多 baseline 与原模型行为检验。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21849:end -->

## 表示为何会随上下文改变

在静态特征模型中，人们容易把“表示”理解成每个输入固定对应一个向量。现代序列模型中的 token representation 通常依赖上下文。同一个词出现在不同句子中，经过多层信息交互后会形成不同状态。

这意味着模型能力不仅存在于参数中，也存在于参数对当前 context 执行的计算里。参数定义一种转换规则，activation 表示该规则在当前输入上的运行状态。对 LLM 而言，prompt、检索结果、历史对话和工具 observation 都可能改变后续表示。

Context 至少可以提供两类不同信息：它可以是“当前属于哪项已学任务”的身份线索，让模型取回参数中学过的规律；也可以是当前过程的样本，让模型从这段输入估计规律。例如在有限 Markov 链的受控模型中，一条路径把相邻状态对编码、汇聚成 task vector，再结合当前状态预测；另一条路径从当前序列估计转移统计。前者的记忆是对生成过程的取回，不等于逐条背诵序列，后者也不意味着所有 in-context learning 都执行同一种统计程序。表示的作用因此要连同数据生成过程与查询分布检验，而不能只问“有没有上下文”。<!-- source-family:SF-2026-ARXIV-2604-12151 -->

这两类计算还可能在训练中竞争：某条统计路径先学会泛化，随后更低训练损失的任务取回路径占优，未见任务表现反而下降。但 task vector 并非天生只会记忆；在足够表示维度和 decoder 容量下，同一编码—汇聚—解码结构也能保留统计并泛化。区分训练动力学竞争与容量压缩，才能判断应增加数据多样性、改变表示预算，还是仅延长训练。受限浅层模型中的 patch 干预支持所测路径的作用，不证明完整唯一 circuit，也不能把其 Markov、任务数和容量阈值作为现代 LLM 的普遍规律。部署仍需已知任务与新任务的独立切片；路径解释不替代行为验收。

任务向量还可由外部学习过程形成，而不是直接从当前 context 统计取回。一个受限的四项类比分支冻结 LLM 权重，只优化关系向量的预测 loss 与正则项；面对新 source pair，分别运行带各个已学 basis vector 的模型，再让学习出的 affine combiner 根据其预测分数组合一个向量用于 target query。[FFV 的机制](https://arxiv.org/html/2601.08169v1)因此保留了冻结 base、可训练向量与学习式组合器三种职责，不是“模型权重没动，所以无需训练”。combiner 权重也不是经过证明的 Bayesian posterior 或通用关系代数。<!-- source-family:SF-2026-ARXIV-2601-08169 -->

可组合向量减少对 query 内演示的依赖，却要为每个 basis 做 source-pair forward，并维护向量、注入层与组合器的共同版本；论文配置的118个 basis 与2,430条组合训练类比不能从成本账本消失。独立关系和词对测试仅相对所披露的训练 split 为新，不能证明它们未进入 base 预训练；局部近类比任务也没有显著优势。关系迁移、语义任务或成本验收不成立时，保留普通 prompt、直接演示或 PEFT，不从四项类比成功推导通用抽象推理能力。

本章不展开 Transformer 的具体结构。第 6 章会说明 content-dependent routing 为何使这种上下文化计算更可扩展，Part II 再解释 token、embedding 和 Self Attention 的内部机制。

## 工程上怎样验证模型学到了什么

仅看一个平均指标，无法区分模型学到稳定规律还是脆弱 shortcut。工程评估至少需要多层证据。

第一层是数据切片。按语言、长度、时间、来源、用户群、难度和风险类别拆分指标，避免总体平均掩盖局部失败。

第二层是受控扰动。改变理论上无关的表面特征，或保留表面形式但改变关键语义，观察模型是否遵循预期不变性与敏感性。

第三层是跨分布验证。使用时间后移、来源变化或真实线上流量检查表示能否迁移。随机划分只能验证同一数据池内的泛化。

第四层是内部分析。probe、归因和干预可以生成机制假设，但应与外部行为、消融和重复实验结合。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22417:start -->
归因图若不声明 reference，只能解释当前 input 相对某个隐式 baseline 的差异，不能给出“这个 feature 绝对贡献了多少”。一个可复核的 attribution artifact 至少要冻结 input reference、该 reference 实际诱导的 output baseline、当前 output target、积分 path/step 与 model revision；attributor 分配的是 `F(x)-F(x')`，evaluation 再用 attribution error、受控扰动、干预与行为结果检查，而不是让热力图或人类相似度拥有 causal truth。

显式 reference 使结论可审计，却增加 baseline 构造、path integration 与 variable-output matching 成本；多个同样合理的 reference 也可能产生不同解释。All-zero 只在输入语义和训练分布允许时才可能是便宜基线，不是跨模态的通用“无信息”状态。Reference off-manifold、输出无法稳定匹配或多组 baseline 结论漂移时，应把结果降级为 reference-conditional observation，并回退多 control、perturbation、causal intervention、外部行为与重复实验。现有证据只支持论文披露的 DETR/VGG 案例与误差分析，不证明选定 baseline 中性或归因具有因果唯一性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22417:end -->
<!-- source-family:SF-2026-ARXIV-2605-22417 -->

跨模型比较还要处理表示基底不唯一。同一功能算法可以在不同 hidden basis、宽度或训练随机种子下实现；直接
对齐 neuron 或 coordinate，可能把 basis change 误判成机制差异。一条更强的比较路线是寻找对线性重参数化
不敏感的 functional subspace，再分别测试：该 subspace 是否足以恢复目标行为，移除它是否必然破坏行为。

`sufficiency` 与 `necessity` 不对称：找到一个可工作的共同子空间，不证明它是唯一实现；干预失败也可能来自
projector、probe distribution 或 replacement error。Projector、matching objective、layer/token range、model
revision 和 intervention 必须进入 evidence identity。Invariant Algorithmic Cores 的 synthetic grokking 实验支持
“跨 realization 比较应先处理 basis invariance”这一原则，不证明真实 LLM 已拥有可唯一命名的通用算法模块。

输出分布接近是否也约束内部表示，还取决于输出接口的可识别性。Softmax 对共同 logit 平移不变，所以比较应先固定 centered gauge；一类等维线性 unembedding 结果还要求 label 数大于表示维度、足够强的 general position 和非退化最小奇异值 σmin，才能把 centered-logit distance 转为 representation distance 上界。σmin 很小会使界空泛；仅有预测 KL 小还须每个 label 概率下界 τ>0，τ 接近零时常数可爆炸。这不是大词表 LLM 的无条件线性可读证书。<!-- source-family:SF-2026-ARXIV-2602-15438 -->

概念读出进一步需要该线性映射可由 unembedding 因子化且范数有限；recoverability 仍不证明原模型因果使用了概念。[LogitDistance 的条件定理与对照](https://arxiv.org/html/2602.15438v1#S3)只在有限分类模型、合成任务和人工属性训练的 teacher 上验证，部分 student 概念准确率仍低于 teacher，标签准确率也不全面改善。提取 teacher logits、选择目标与独立读出审计都付费；条件失配时，普通 KL 输出拟合仍有自己的用途，但内部保持须另做 probe、干预和任务验证，不能从预测接近直接签发内部等价。

第五层是线上闭环。持续记录输入分布、输出质量、拒答、工具失败和用户反馈，并把异常关联到模型、数据、prompt、runtime 和版本。Observability 告诉我们变化发生在哪里，Evaluation 才判断变化是否有害。

这些方法也有成本。切片越细，样本数越少；评估越贴近真实业务，复现和标注越困难；内部解释越深入，越容易依赖特定模型版本。平台需要根据风险选择证据强度，而不是追求一套万能 dashboard。

### 文本表示的上限来自输入本身，而不只来自模型容量

更大数据、更强目标和更宽网络可以让模型逼近“从 utterance form 推断 meaning”的最佳规则，却不能恢复输入中没有携带的信息。若同一表面形式在不同外部情境中对应不同意图，那么任何只读取该文本的 featurizer 都面对不可约条件熵；扩参数只能更接近这个上限，不能消除上限。这里的非确定性不是模型“还没学会”，而是 observation contract 不足。

系统因此要把缺失变量作为显式状态补回：对话与环境 Context、可追溯检索、用户确认、工具 observation，或在证据不足时 abstain。代价是隐私、延迟、检索错误和新的 trust boundary；当任务定义本来只依赖文本形式时，纯文本模型仍是更简单的正确基线。`arXiv:2608.28560v1` 给出信息论上界并在人工语言、中文零代词和颜色指称上作有限验证，实验模型不超过 14B；它不证明任意具体回答必然不可知，也不把外部 Context 自动变成真值。

<!-- source-family:SF-2026-ARXIV-2608-28560 -->

## 几种过度解释

第一，“模型学到了人类相同的概念”。相似行为可以由不同内部机制产生。除非有更强证据，否则应说模型形成了对任务有用的表示，而不是断言其概念与人类等同。

第二，“模型只是背诵”。记忆确实存在，但模型也能组合和迁移训练中共享的结构。只用一个标签无法解释不同任务、数据和规模下的行为。

第三，“高维向量天然包含语义”。向量只有在训练目标、数据和后续计算中才有意义。坐标本身不是语义字典。

第四，“可以 probe 出来就代表模型会用”。可读取信息与因果使用不是同一结论。

第五，“同分布 test set 足以证明生产泛化”。真实环境的时间、用户、语言、上下文和反馈机制都可能变化，必须明确外推边界。

### 参数知识更新必须同时验收获得、保留与泛化

一次编辑后能答对目标问法，只证明局部 acquisition；它没有证明知识会跨后续更新保留，更没有证明模型能在不同实体、关系或表达下正确 generalize。参数知识不是可寻址数据库，因此连续更新应被视为时间过程：

```text
ordered updates
-> acquisition at edit time
-> retention after later updates
-> temporal decay
-> cross-instance stability
-> query generalization
```

这种验收比单点成功更昂贵，却能区分“写入失败”“后来遗忘”和“只记住模板”。现有实验证据来自合成或半合成 QA、有限模型与编辑方法，不能推出某一种编辑算法在真实知识流中必然失效。若知识变化频繁、需要可撤销或需要来源证明，外部 versioned memory/RAG 仍比直接改权重更合适；参数编辑只在更新边界清晰且上述维度可持续回归时成立。

<!-- source-family:SF-2026-ARXIV-2607-26455 -->

在继续验收获得、保留与泛化的前提下，编辑也可把保留对象显式放进更新约束。普通 capability loss 的二阶展开若假定 checkpoint 已收敛，可能漏掉非零一阶项；以原模型输出为 reference 的 Bregman divergence 在该 reference 处一阶为零，局部二阶可写为 Gauss–Newton 曲率，再限制更新进入低曲率子空间。[一种受限实现](https://arxiv.org/html/2602.15823v1)用 K-FAC 的分块 Kronecker 近似和阈值矩阵运算避免构造巨大投影矩阵，因而 curvature artifact 必须绑定 reference/checkpoint、保留数据、edited layers、近似与阈值；它不是完整模型的精确非破坏证明。缓存构建、分解、编辑和回归均付费，原 wall-clock 口径未明确全部 offline 成本，不能签端到端普遍加速；有限基准也有单项能力退步。Teacher-forced 编辑成功、自由生成效果与 capability regression 应分别检验，局部近似失配或无法定义可信保留分布时，应回退原模型、外部 versioned memory/RAG 与独立行为测试，不让投影自行批准参数发布。<!-- source-family:SF-2026-ARXIV-2602-15823 -->

## 本章在知识树中的位置

第 4 章解释参数如何被 loss 和 gradient 更新，本章解释这些更新怎样形成任务相关表示，并为什么受到数据分布与 inductive bias 限制。两章关系是：

```text
Optimization asks: how are parameters changed?
Representation asks: what useful computation emerges from those changes?
Generalization asks: where does that computation remain valid?
```

第 6 章将引入 Transformer 作为一种更适合上下文交互和规模化训练的架构，第 7 章讨论扩大数据、参数和算力时 loss 的经验规律，第 8 章再讨论这些表示如何表现为广泛能力。Part IV 的数据与训练章节、第 66 章 Evaluation System 与后续 Observability，都建立在本章的分布边界上。

## 从机制演进到系统设计

模型内部表示从“能重构某个概念”走向“能被独立监督读出并在新 probe 上稳定复现”时，证据强度才真正上升。语言化解释、activation correlation 与 reconstruction score 可以提出候选机制，却不能单独证明模型在任务中使用了该表示；需要把 decodability、intervention、fresh-probe monitoring 与外部行为结果分开。

更强的诊断提高可解释性，也会引入 probe capacity、label leakage 与 observer effect。解释器无法跨分布复现或 intervention 不改变行为时，应回退为相关性证据而不是因果结论；模型学到的表示仍由 data、objective 与 architecture 共同限定。

反过来，干预确实改变答案，也不证明被操控的是格式不变的概念。一个受限 ICL 对照按 activation patching 选择能驱动任务的 heads，再按跨格式的表示相似性选择 concept-consistent heads：前者形成的 Function Vectors 在同格式控制更强，却可能随抽取格式引入外语或多选括号；后者形成的 Concept Vectors 跨格式更一致，绝对增益较小，而且在 zero-shot 或恢复被破坏任务的 patching 中无效，需要 prompt 已包含该概念。这里“能启动任务”“能放大已有概念”和“跨格式保持效果”是不同验收条件，不应由一次成功控制推出统一抽象，也不以 CV 替代 FV。[七类词关系、三种格式与四个 Llama/Qwen 模型的必要对照](https://arxiv.org/html/2602.22424v1)没有确定两类 heads 的训练起源或推理交互；AP/RSA、抽取及跨格式回归都付费。任务格式稳定时原 FV 仍合理，迁移失配时应回原模型与行为检验，而不是只按向量相似度发布控制。<!-- source-family:SF-2026-ARXIV-2602-22424 -->

## 自检问题

1. 为什么把神经网络当作“每个神经元存一条知识”的数据库会失败？
2. 中间表示 `h_l` 为什么不是对输入的中立描述？
3. separation、invariance 和 compositional usefulness 分别描述表示的什么性质？
4. `P_train != P_deploy` 可能由哪些不同机制产生？
5. 为什么 inductive bias 是从有限样本泛化所必需的？
6. shortcut learning 为什么可能在同分布 test set 上不暴露？
7. 记忆与泛化为什么可以同时存在？
8. superposition 提高了什么，又牺牲了什么？
9. correlation、decodability 和 causation 在可解释性中有何区别？
10. 生产系统应怎样组合数据切片、受控扰动、跨分布评估和线上反馈？

### 模型状态里“有知识”不等于当前路径会正确取用

一次失败至少可能来自三层：参数或外部状态没有保存所需知识，路由/注意力没有把它送到当前计算路径，或生成后没有通过 repair 纠正。只用最终准确率无法区分这些原因，也会让“增加知识”“改善路由”和“加强验证”被误当成可互换方案。诊断应分别施加可控干预，确认信息是否存在、是否被访问以及错误是否可修复，再决定训练、结构还是运行时补救。
<!-- source-family: arxiv:2608.12321v1; semantic-body-binding: knowledge-routing-repair-separation -->

### 可读出不等于可拆卸或可控制

预测依赖什么时候能支持因果结构，也需要先声明生成过程，而不是从模型名称取得因果解释权。对于滞后时间序列，在条件外生性、无同期作用、窗口覆盖全部父变量、faithfulness 和正则条件下，真实条件分布对某个历史变量的 score-gradient energy 可以识别对应滞后边；理论允许任何足够拟合该分布的模型，并非 Transformer 专有。只有同方差 Gaussian 等附加条件才把它收窄为条件均值梯度；用 MSE 训练并以 LRP 提取 relevance 又是实践代理，不能把普通 attention 权重或低预测误差直接认证为因果图。[受限理论与仿真](https://arxiv.org/html/2601.05647v1)支持这条条件链，却未解决任意潜在混杂、同期作用与窗口遗漏。拟合、归因校准和图判定均有额外成本；假设不成立或代理不稳时，保留预测/关联诊断，另做受控干预与因果检验，不把模型结构升级为因果保证。
<!-- source-family:SF-2026-ARXIV-2601-05647 -->

方向分离的几何结论也要与行为保留分开。令有限的 protected-direction registry 为矩阵 A，对候选方向 r 作 ridge 拟合 ŵ=(AᵀA+λI)⁻¹Aᵀr，再取残差 r̃=r−Aŵ；当 λ>0 时 normal equation 给出 Aᵀr̃=λŵ，通常不为零，故这是软残差化而非严格 nullspace 投影。即使对所列 span 精确正交，也不保证非线性下游行为不变；registry 漏掉的方向仍无保护。受限编辑研究的 teacher-forced perplexity 与首 token KL 只能验证对应分布代理，不认证自由生成能力或安全保留。拟合与干预增加计算及 registry 维护成本；代理改善而行为回归时，应保留原模型与独立能力/安全回归，不能用几何分离自行签发发布。[必要几何反侧](https://arxiv.org/html/2601.08489v1)。<!-- source-family:SF-2026-ARXIV-2601-08489 -->

探针能从某层表示中解码出属性，只说明该属性与当前表示相关；它不证明对应知识集中在一个可移除模块，也不证明干预该方向会按预期改变行为。训练样本的混合粒度会把多个因素共同压进参数，因此模块性必须靠删除、替换和跨分布干预验证。探针仍适合发现候选结构，但在因果证据缺失时，只能拥有诊断权，不能拥有模型编辑或发布决策权。
<!-- source-family: arxiv:2608.10214v1; semantic-body-binding: probe-decodability-versus-modular-control -->

## 小结

神经网络学到的不是可直接翻阅的规则表，而是分布在参数与激活中的计算结构。它把输入映射到为训练目标服务的表示空间，在其中放大有用差异、压缩部分无关变化，并让后续层更容易完成任务。

这种能力既来自数据中的规律，也来自架构和优化的偏好。它可以表现为泛化，也可以夹带记忆、偏差和 shortcut；它能在训练分布上工作，也可能在 distribution shift 下迅速失效。理解这些边界，是把模型指标连接到 Evaluation、Observability 和数据反馈闭环的前提。

### 可解释标签不是 Feature Identity

Sparse autoencoder 把 activation 分解为稀疏 feature，短自然语言标签便于人理解；但当标签空间远小于 feature 空间时，不同 feature 会发生 descriptive collision。传统 detection score 只检查“看到解释能否预测 feature 是否激活”，即使多个 feature 共享解释和相近激活分布也可能同时得高分，因此可读解释不能独自拥有 feature identity。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12874 -->

更可靠的解释合同应同时记录 collision rate、激活差异、干预结果与未能区分的候选 feature。这样增加了标注和因果验证成本，也仍可能受评估语料覆盖限制；无法通过区分性与干预复核时，应回退到 activation statistics 和具体输入实例，不用标签替代机制。exact-v1 证据限于所用 SAE、标注语料和自动解释评价，不能证明自然语言标签能唯一指代内部概念。

标签若声称 feature 表达的是一个推理概念，还需要比“能预测激活”更强的可证伪条件。一个操作性检验同时要求 specificity——只出现有关 token 而没有该语义时不应激活——与 semantic invariance——语义相同但表达形式改变时仍应激活。先从高激活样本得到解释，再向无关上下文注入这些 token 或构造保持语义的改写，便能分别检查 false positive 与 false negative；这些反例可以推翻一个 feature 的强语义解释，而不是只给解释再取一个更好听的名称。<!-- source-family:SF-2026-ARXIV-2601-05679 -->

[受限 SAE 推理概念检验](https://arxiv.org/html/2601.05679v1)对 196 个候选 feature 的这类检验未找到同时满足条件的“genuine” feature，因而收窄的是所测 SAE、语料、候选选择和判定合同下的解释，不是证明模型没有推理能力或不存在分布式表示。有限上下文可能漏掉真实激活条件，steering 也未给出完整因果控制；生成反例、人工核验与干预都有额外成本。无法满足严格标签合同，应退回具体 activation/input 和行为级评价，不能把一个词相关方向直接登记为内部推理模块。

强概念标签未通过检验，不等于不存在局部可用的行为控制。另一项[受限首步 steering](https://arxiv.org/html/2601.08058v1)先比较 CoT/direct 提示的 SAE 激活，在训练侧用单 feature 干预选择候选，再固定 feature、层和强度于 held-out 问题；注入的是 decoded 改变量加回原 activation，而非把整个 SAE 重构替代原状态。所测 feature 与进入某种生成模式相关，却在固定提示内不可靠地区分答对与答错；这支持操作性 mode-control，不认证 genuine reasoning concept、完整分离或唯一推理模块。SAE、训练侧选择与干预增加成本，某些 direct 输出明显增长，GPQA/CoT 切片还会退步；随机 feature 的多次对照与所选 feature 的单固定 seed 也不是完整公平性与不确定性保证。未形成净质量/成本收益时保留普通提示、原模型和行为测试，不用局部控制结果替强语义解释或部署授权背书。<!-- source-family:SF-2026-ARXIV-2601-08058 -->

### 行为方向可能早于 Post-training 形成

把 persona 或高层行为全部归因于 alignment 数据，会忽略 pretraining 已经形成的可复用表示方向。沿训练 checkpoint 追踪 residual directions 的受限实验显示，一些 persona-like directions 在早期预训练便出现，并能迁移到同家族的 post-trained checkpoint；后训练更像重塑其可访问性和表达强度，而不一定从零写入行为。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13329 -->

线性可解码和 steering 效果仍不等于单一方向拥有完整因果控制，跨模型与跨数据配方也未证明。系统上应把 pretraining data provenance、checkpoint lineage 与 post-training intervention 分开审计；方向不能稳定复现时，回退行为级 evaluation，不据 representation probe 推断模型“拥有某种人格”。

方向本身也是从数据估计的对象。对成对正负例取 activation difference 再求均值，接口简单且在干净样本下合理，但随机无关内容可能缩小方向的 norm，标签交换或协调的另一种行为则可能改变 angle，后者会把干预引向不同的行为。因而方向身份还须包含样本来源、配对/标签、读取层、估计器和干预强度；不能把“还能产生输出变化”当作估计方向仍表达原意。

鲁棒均值或 variance-based pruning 是可比较的缓解分支，不是自动恢复真方向。高维、少样本和相关污染可能不满足理想估计假设，按低 variance 选样甚至可能留下协调 outlier、删掉 inlier；受测模型之间也不都出现同样的非目标行为。清洗、增加样本与逐层/强度搜索都增加成本，验收须同时比较方向 norm/angle、目标及非目标行为和质量回归。无法确认估计稳定时，应保留干净配对数据、原行为级对照或停用该 steering，而不是用一个鲁棒算法名称声明安全控制。<!-- source-family:SF-2026-ARXIV-2603-03206 -->

## Review notes

- `SF-2026-ARXIV-2601-11022` — Daily `2026-01-20`增量；[geometric quantile TTA exact-v1](https://arxiv.org/html/2601.11022v1) §3/4/5、Figure3/Theorem4与必要费用对照。2+1+2=5，frozen classifier/inputadapter/source-reference/CPU-snapshot bank差额深入；边缘匹配不认证类别语义，原coding反证继续共存；保留identifiability/local初始化、memory/time费用，不授source-free或生产SLO。root实际必要原证/owner PRE通过并授窄锁；作者实际正文/完整邻接/本注已顺读，root实际顺读145–157/本注，POST通过，窄锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-21442`：exact-v1 Algorithm1、retain/remove与BFS共享Bellman读出；仅采用可执行连通子网与实际干预，不采用方向冲突的Char headline；未复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。

- `SF-2026-ARXIV-2602-22424` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22424v1) §2–3与§5的直接反侧。3+1+3=7，因果控制与格式不变差额深入；CV 依赖已有 prompt 概念、非 zero-shot 替代、ID/OOD 增益与抽取/回归成本近正文。root 必要原源/actual owner PRE 通过；实际正文、完整邻接与自身末注经 root 非作者 POST 通过，窄锁释放。未核实现/复现，不授日级完成。

- `SF-2025-ANTHROPIC-INTROSPECTION` — Daily `2025-10-30`；采用原研究的 accuracy/grounding/internality 区分、随机概念/注入时机/输入复述对照与必要失败边界；不采用后续修订提示为当日事实，不授完整元认知机制、意识或生产自审保证。root 已核必要原源、现 owner 与 Ch4/6 交接并窄写；Mill 非写入者于 2026-10-05T08:18:27+08:00 实际核两段、前后衔接与末注，写后复核通过，未复现实验。

- `SF-2026-ARXIV-2602-15438` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15438v1) Theorems3.3/3.9/4.3、Eq14/Table2/必要setup。3+1+3=7，条件理论深入；centeredgauge/stronggeneralposition/σmin/τ与线性factorization限制近正文，不授causal使用、任意维度或LLM无条件内部保持。root必要源/actualowner PRE通过；实际正文、邻接及末注root独立POST通过，未核实现或复现。

- `SF-2026-ARXIV-2602-12418` — Daily 2026-02-17；[exact-v1](https://arxiv.org/html/2602.12418v1) §3–5、A.1 与 Limitations。2+1+2=5，matched semantic-core/context contrast 与 latent 修改后加回原 reconstruction residual 的具体 owner 缺口深入；不认证 feature 真值、普遍安全或自适应攻击防御。四个有限模型/SAE 与 wrapper split，CAA token 选择混杂、largest-Llama 局部消融、feature count/strength–utility tradeoff 保留；未复现。root 必要原源/当前 owner 写前通过，root 实际正文/完整邻接/末注非作者 POST 通过，锁释放，不代日级验收。

- `SF-2026-ARXIV-2602-11246`：exact-v1 §1.1–1.2 的统一线性恢复定义与 Theorems 1–3，§2/3 的上下界构造和 §5 Theorem 12/Corollary 13 的不同分类访问条件。采用固定 ε、稀疏连续输入、下界前提及对数差距；不外推真实 LLM 容量、不由 probe 失败认定信息不存在。必要证据与上述两段差额经 root 非作者 PRE 核准，2026-10-04 实际正文及前后衔接、末注 POST 通过；不宣称实现或实验复现。首次公开尚未确认为 2026-02-14 Daily 窗口；此为独立理论核验，不计本日确认候选或本日整合成果，取得此精确版本的官方公告批次或可核首次公开完整区间后仅重开日期归属。

- `SF-2025-OPENAI-SPARSE-CIRCUITS` — Daily 2025-11-14；采用[2025-11-13官方Blog](https://openai.com/index/understanding-neural-networks-through-sparse-circuits/) L45–72明示的训练时连接约束、简单任务剪枝干预与能力/解释性/成本边界。当前链接的2511.13653v1提交于11/17，不冒称Nov13原技术稿；不采用未披露稀疏优化算法、matched FLOPs或前沿安全结论。root已实际核有限原源、Ch5差额与Ch4/6交接并窄写；非写入者Planck于2026-10-04T17:02:54+08:00实际正文、前后邻接及末注POST通过，不代日级完成，未复现。

- `SF-2026-ARXIV-2602-08695` — Daily 2026-02-11；[exact-v1](https://arxiv.org/html/2602.08695v1) §3–5。采用观察 `z=x⊕noise`、监督 `f(x)` 时 noisy 条件目标不同 clean `f(z)` 的受限诊断；uniform/iid bitflip/highnoise/合成布尔函数边界保留，不外推真实LLM必失败。AB/intro/图注的 high-sensitivity penalty 与正文 `-λI` 鼓励高敏感度冲突，remedy 未采用；clean/noisy评测分账明确为系统推断。3+1+3=7，root必要来源与当前owner差额写前通过；root实际正文、前后邻接及末注非作者POST通过，未复现，不代替日级验收。

- `SF-2026-ARXIV-2601-08169` — Daily 2026-01-15；[FFV exact-v1](https://arxiv.org/html/2601.08169v1) §3/Eqs1–3、§4.1–4.3与Limitations。2+1+2=5，冻结base的关系向量与学习affine组合gap深入；不授Bayesian posterior/通用关系代数，zero-shot不等免训练。118basis/source-pair forwards、2,430组合训练、split相对OOD与near任务反侧保留；未复现。root必要源/owner写前通过，root已实际核正文、前后邻接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-05679` — Daily `2026-01-13`；[SAE reasoning-concept exact-v1](https://arxiv.org/html/2601.05679v1) operational specificity/invariance、token injection 与196候选 FP/FN 检验。有限负结果不证明无推理或无分布式表示，不授 steering 因果控制。未复现；root 必要源/当前owner写前通过，root实际新增正文/前后衔接及末注写后复核通过。

- `SF-2026-ARXIV-2603-03206` — Daily 2026-03-05；[exact-v1](https://arxiv.org/html/2603.03206v1) §2–6、配对方向/三类污染与 correlated-outlier 反例、Appendix A 配置。三个模型、800训练/200测试与三次污染采样；layer/强度调参及小样本高维限制保留。采用方向估计身份与 norm/angle 分责，不采用鲁棒 estimator 作为安全保证。6分长期缺口深入；root 已实际对读必要原文、正文与邻接，非作者 POST 通过，未复现。

- `SF-2026-ARXIV-2604-19052`：[exact-v1](https://arxiv.org/html/2604.19052v1) §3.1–3.3/Eqs2–6/Figures2–9，Daily 2026-04-22。采用 entity×relation 索引及跨 context 有限 translation 的受限机制分支；属性 token 拟合、PLS/patch 和受控合成域只支持局部可读与行为作用，不证明物理表格、唯一符号地址或开放 LLM 泛化。root 必要来源→当前 Ch5 owner 写前、实际正文及相邻论证写后非作者复核均通过；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-18907`（Experimental）：[Gradient-Based Program Synthesis with Neurally Interpreted Languages exact-v1](https://arxiv.org/html/2604.18907v1) §3.1–3.4/§4.1–4.5；采用训练期 primitive/codebook 与共享循环 executor、测试时冻结执行器并优化 program latent 的职责分支，不采唯一符号真值、无界长度或通用 LLM 编程能力。受控 Shift/Composition、DeepCoder/LPN 比较与多起点/梯度搜索成本限制外推；root 必要 source→Ch5 采用及实际正文写后独立复核通过，复核时纠正“连续身份”与端到端对照措辞，未复现实验。

- `SF-2026-ARXIV-2604-13082`：[exact-v1](https://arxiv.org/html/2604.13082v1)，Daily 2026-04-16；必要证据 §4.1/§5.2 的 encoder/decoder 移植、冻结与 rewind，§5.3–5.5/§6 的编码、表征失败和任务迁移边界。仅采用模块诊断区分表示形成与读出失败，不采用 2.75× 为总训练成本收益或普遍 decoder 瓶颈。root 有限 source→owner 与本次实际写后独立复核通过，未复现实验。
- `SF-2026-ARXIV-2604-13694`：[exact-v1](https://arxiv.org/html/2604.13694v1)，Daily 2026-04-16；必要证据 III-A–D、IV 与 V Scope，采用 matched-checkpoint anchor 恢复与 activation 中继分责，再用输出 KL/IFEval 单独核行为；保留 same architecture/fixed input/matched anchor、Q/O 与同一 MLP neuron gate/up/down 粒度、梯度筛选与实际替换验收及六代表任务范围。不是唯一知识来源或全模型通则。root 有限 source→owner 与修正后的实际正文/相邻论证写后独立复核通过，未复现实验。

- `SF-2026-ARXIV-2604-12151`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12151v1) Roman III、IV.1–IV.7、V。有限 stationary Markov 链与两层模型；统计归纳/任务取回、训练竞争/表示容量两层区分，task vector 可在足够容量下泛化。patch 非完整唯一 circuit，不外推开放 LLM 阈值。6分实际缺口深入；必要来源/owner 独立复核通过（apr02），实际正文及相邻交接写后非作者复核通过（root、apr02），未复现实验。

- 2026-09-01 角色绑定的受限解释：<https://arxiv.org/html/2608.29034v1> §2–3/7 与 <https://arxiv.org/html/2608.29530v1> §3/6–9。人工 role、受控任务与有限替换不证明表示唯一；生成 token 等原 forward 仍保留，DISCOVER 的组合 holdout 不等于 target 预训练未见。正文不采神经/符号的哲学定论。

- `SF-2026-ARXIV-2601-10169` — Daily `2026-01-17` 增量；[CtD exact-v1](https://arxiv.org/html/2601.10169v1) §2.2–3.3、§4.3、§5.1/Table2/§5.2、AppG/J。2+1+2=5，Oracle 控制 shared-factor 多 target→单概念 codebook→known-concept 新组合消费的具体 gap 受影响深入；单target/Qrc/继续训练反侧、Oracle/l/词表先验与训练/选择成本及普通端到端共存近文。root 非作者实际必要原源/条件公开日期/current说明/Ch5组合性完整邻接PRE通过并授单段窄锁；作者已顺读，root非写入者实际正文72–112完整邻接及本note575 POST PASS、Qrc身份最小修准确，窄锁释放。未核代码/复现实验，不授日级完成。

- Train the Model, Not the Reader: Decodability Supervision for Verifiable Activation Explanations（arXiv:2607.20379v1；Status: Experimental）：https://arxiv.org/html/2607.20379v1
  - 证据边界：支持披露设置中 reconstruction-only scoring 的失败与 RECAP/probe 结果；不证明 neuron-level causal use、完整 semantic legibility、adaptive training 下的安全性，或高 AUC probe 必然产生 faithful language explanation。

本章不重复第 4 章的优化推导，也不把任何可解释性方法描述为已经读取了模型全部知识。自检答案回填用神经元计算与置换不变性说明单元编号为何不是稳定知识地址，并把分析对象收紧为 feature direction、subspace 与 computation path。后续 Review 应继续保持“行为证据、可读出信息、因果机制”三层结论分离，并避免在 Part I 提前展开 Transformer block。

优先核验入口：

- Yoshua Bengio, Aaron Courville, Pascal Vincent, "Representation Learning: A Review and New Perspectives", 2013: https://arxiv.org/abs/1206.5538
- Yann LeCun, Yoshua Bengio, Geoffrey Hinton, "Deep learning", Nature, 2015: https://www.nature.com/articles/nature14539
- Chiyuan Zhang et al., "Understanding deep learning requires rethinking generalization", 2016: https://arxiv.org/abs/1611.03530
- Robert Geirhos et al., "Shortcut Learning in Deep Neural Networks", 2020: https://arxiv.org/abs/2004.07780
- Nelson Elhage et al., "Toy Models of Superposition", 2022: https://transformer-circuits.pub/2022/toy_model/index.html
- Guillaume Alain, Yoshua Bengio, "Understanding intermediate layers using linear classifier probes", 2016: https://arxiv.org/abs/1610.01644
- Gurnee et al., "Verbalizable Representations Form a Global Workspace in Language Models", 2026: https://transformer-circuits.pub/2026/workspace/index.html
- Anthropic, "Circuit Tracing: Revealing Computational Graphs in Language Models", 2025:
  https://transformer-circuits.pub/2025/attribution-graphs/methods.html
- Transformers Converge to Invariant Algorithmic Cores（basis-invariant functional comparison；
  Status: Experimental）: https://arxiv.org/abs/2602.22600

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2607-20379:start -->
- `SF-2026-ARXIV-2607-20379` — Daily `2026-07-23`；primary `arXiv:2607.20379v1`；Books review `books-review:SF-2026-ARXIV-2607-20379`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: reconstruction-scored verbalizer -> independent claim audit -> externally supervised decodability plus fresh-probe monitoring 该 delta 已进入 `books/part-01-worldview/05-what-neural-networks-learn.md#L174`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-20379:end -->

- `SF-2026-ARXIV-2601-05647` — Daily `2026-01-13`；[Transformer causal learner exact-v1](https://arxiv.org/html/2601.05647v1) §3–4.1。原评分保持，具体owner差额深入；采用A1–A4 score-energy条件理论与Gaussian/MSE/LRP收窄；不授attention/架构因果。未运行代码或复现实验；root实际必要源/现owner写前核通过并授窄锁；root已实际核正文/前后邻接及末注，非作者POST通过。

- `SF-2026-ARXIV-2601-08489` — Daily `2026-01-15`；[SRA exact-v1](https://arxiv.org/html/2601.08489v1) §3.3 ridge、§5.1代理评价、§7限制。2+1+2=5，具体soft residual geometry gap深入；不写拒答绕过recipe，不授exact orthogonality、protected行为不变量或能力/安全保留。有限registry、PPL/首tokenKL非行为验收边界保留；未运行代码或复现。root必要原源/现owner差额写前通过并授窄锁，root实际正文/邻接/末注非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08058` — Daily `2026-01-15`；[Latent Feature Interventions exact-v1](https://arxiv.org/html/2601.08058v1) §3.4/Eq10–13、Table1与limitations。2+1+2=5，操作性mode-control与强concept资格分离差额深入；训练侧选择/输出增长/随机对照公平性及GPQA反侧保留，不写绕过recipe。未运行代码或复现实验；root实际必要原源/现owner写前核通过，实际正文与前后邻接非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-09764` — Daily `2026-02-12`；[BITS exact-v1](https://arxiv.org/html/2602.09764v1) §3–5与A Tables9–11。2+1+3=6，具体owner差额深入：teacher-hardbit/student BCE channel≠交付backbone；MI解释不认证，reset/bits反侧和成本近正文；未核实现或复现。必要source独立通过、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2601-20834` — Daily `2026-01-30`；[exact-v1](https://arxiv.org/html/2601.20834v1) §2–4/B.8，2+2+3=7。仅采用before-answer固定steering方向跨context极性可反转的局部条件，与after-answer probe及关系translation分离；非真值、意识/信念或参数知识删除。少量conversation、模型/层选择、机制未明及校准成本近正文。root必要证据与具体owner PRE、实际正文/邻接/末注POST通过，非日级Gate。未核代码或复现。

- `SF-2026-ARXIV-2602-10352` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10352v1) §3–5、Appendix J L922–943；只采trained-interpreter prior/null-input与activation贡献分账，不采标签真值或桥接推理因果；偏置拟合与筛选人口/成本近正文。root必要源与实际owner PRE通过，具体差额受影响深入；实际正文/完整邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-14111` — Daily `2026-02-18`；[SAE Sanity Checks exact-v1](https://arxiv.org/html/2602.14111v1) §3–6。3+1+2=6，设计反证受影响深入；采用 partial-random/frozen null baseline 与 learned alignment/重构/代理及操作价值分账，保留 soft-frozen 可学、RAVEL mask 训练、toy 独立激活与所测标准 SAE/模型层边界，不授普遍无用或唯一真实因果。root 必要源/实际 owner PRE 及实际两段、完整邻接与末注非作者 POST 通过；窄锁释放，日级未验。未运行代码或复现实验。

- `SF-2026-ARXIV-2602-12403` — Daily `2026-02-17`；[MonoLoss exact-v1](https://arxiv.org/html/2602.12403v1) §3/Eqs1–3、§4/Tables1–3、Appendix B/E。2+1+2=5，具体训练目标长期差额受影响深入；采用外部 encoder 一致性作为可选 aux、pairwise→聚合及 batch/coverage/重构/独立干预并验，不授 feature 真值、通用加速或最佳精度保证。root 必要原源与实际 owner PRE、实际两段/完整邻接及末注非作者 POST 通过，窄锁释放，非日级 Gate。未核实现或复现。

- `SF-2026-ARXIV-2602-15293` — Daily `2026-02-19`；[Dual steering exact-v1](https://arxiv.org/html/2602.15293v1) §2–5/Theorem3、AppendixA.1–2/B.1–2/C.1–2。3+1+3=7，必要理论深入；采用softmaxKL/Bregman expected-unembedding几何及准确probe/目标hyperplane/全集合factorizability下minoff-targetKL，不授全部非目标不变、完整分布mixture/OR或通用控制。C2假设失配、covariance/regularizedNewton近似、context与词表截断及成本近正文；mixture子命题具体反例单独隔离不推倒其他有效条件。root必要源/actualowner PRE及实际两段/完整邻接与末注非作者POST通过，窄锁释放；未核实现/复现。

- `SF-2026-ARXIV-2602-15183` — Daily `2026-02-19`；[Seeing to Generalize exact-v1](https://arxiv.org/html/2602.15183v1) §3–6/AppendixD/F。2+1+3=6，binding长期差额受影响深入；采用配对内容/位置干预诊断shortcut与内容路径，不采用任意长度泛化或image-only因果。noise/grounding/mix/词表与预算bundle、剔除分支及大模型相关性边界近正文；root必要源/actualowner PRE及实际两段/完整邻接与末注非作者POST通过，窄锁释放；未核实现/复现。

- `SF-2026-ARXIV-2602-13483` — Daily `2026-02-18`；[ACC++ exact-v1](https://arxiv.org/html/2602.13483v1) §2–4/必要附录。2+1+2=5，具体counterfactual目标差额深入；采用移除后整row Softmax竞争目标，不采用全局最小/唯一circuit、proxy feature真值，正确IOI人口及替代route/费用近正文。root必要源/actualowner PRE通过，实际正文/完整邻接与末注经root非作者POST通过，窄锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-15332` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15332v1) 必要方法、主对照与直接反侧。2+1+2=5，固定realizedprefix/continuation的receiver-only读路径干预，不授rerollout/finalcorrectness因果；fixed stride 与 pivot 选择分清，匹配随机对照与额外forward成本近正文。root必要source/actualowner PRE通过；root实际正文/完整邻接及末注非作者POST通过，窄锁释放，未运行代码或复现，非日级Gate。

- `SF-2026-ARXIV-2602-15823` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15823v1) §3.1–3.3/§4.2/Table1/Fig4/AppE；2+2+2=6，非converged reference的Bregman一阶消去/local GN与KFAC矩阵free近似artifact深入。edited subset、局部近似、offline口径未明、自由生成/单项cap退步与原RAG分支保留，不授全能力保持或E2E加速。root必要源/actual owner PRE通过并授一段窄锁，作者实际正文/完整邻接已顺读，root非作者已实际顺读正文/完整邻接及末注POST通过，窄锁释放；未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-15593` — Daily `2026-02-19`；[exact-PDF-v1](https://arxiv.org/pdf/2602.15593v1) §3.1–3.3/必要Figs2–5；3+1+3=7，posterior temporal kernel的参数共享条件深入。保μP/独立噪声SGLD+weightdecay/大宽度、弱信号与端点无自动优势、teacher匹配及理论/采样成本；不授普通有限SGD或普遍RNN更好。root必要PDF/actual owner PRE通过并授一段窄锁，作者写后完整邻接已顺读，root非作者已实际顺读正文/完整邻接及末注POST通过，窄锁释放；未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-16823` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16823v1) §2/3双输入可达patch规格、§4.3–4.4单调/闭包、§5/7运行与限制。2+1+2=5，具体连续域规格差额定点深入，不授LLM scalable/global-minimal/真实因果。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接/末注已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放，未运行实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-20273` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20273v1) §3–5/7/8/10/11。2+1+3=6具体gap深入。采用联合/特定域方向并存与covariance量尺及读出不授控制反侧；SimpleQA logprob/本来正确置信、目标population covariance、模型生成标签/线性范围及projection非完整擦除近正文。root必要source/actual owner PRE及实际正文233/235、231–265完整邻接及本末注610非作者POST通过，锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-20433` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20433v1) §3–5/AppC。3+1+3=7；训练配置同时塑造谱几何与loss、rank不是性能/因果证书差额深入。108小模型/finite-scale、batch/WD/LR/annealing反例与75M量化反侧、W/finalH范围近正文；不授geometry干预无效或统一rank阈值。root必要源/actual owner PRE及正文237/239、完整231–267/本末注actual POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22581` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22581v1) 必要blocks28–73/82–123/153–171及原包7采用相关控制/反侧；2+1+2=5，Gaussian联合门/output-KL与错误闭式隔离具体差额深入。fresh非原packet作者必要原证/actual owner PRE完成，原有效身份/精确版/命题复用；费用、人口、未证与回退近文。获Ch5窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放；未核artifact/复现，非日级。

- `SF-2026-ARXIV-2602-22600` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22600v1) 必要blocks13–28/51–68/94–116/120–130/143–158及原包8采用相关控制/反侧；2+1+3=6，active×task-sensitive子空间、keep/remove/flip与线性readout/发现人口边界具体差额深入。fresh非原packet作者必要原证/actual owner PRE完成，原有效身份/精确版/命题复用；费用、人口、未证与回退近文。获Ch5窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放；未核artifact/复现，非日级。

- `SF-2026-ARXIV-2602-23164` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23164v1) 必要blocks21–96/107–128及原包20采用相关控制/反侧；2+1+3=6，规则选择与状态恢复分责、几何/干预及混合支持边界具体差额深入。fresh非原packet作者必要原证/actual owner PRE完成，原有效身份/精确版/命题复用；费用、人口、未证与回退近文。获Ch5窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放；未核artifact/复现，非日级。

- `SF-2026-ARXIV-2602-23360` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23360v1) 必要blocks11–18/61–96/218–232/44–45/247–278及原包25采用相关控制/反侧；2+1+3=6，prediction midpoint、population近最优/闭包前提与agreement非truth具体差额深入。fresh非原packet作者必要原证/actual owner PRE完成，原有效身份/精确版/命题复用；费用、人口、未证与回退近文。获Ch5窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放；未核artifact/复现，非日级。
<!-- supplement-20260122-review-note -->

- `SF-2026-ARXIV-2602-08169` — Daily `2026-02-11`增量；[exact-v1](https://arxiv.org/html/2602.08169v1) §3–5及Appendix B/C.1/C.2。2+1+2=5，球面保范数与条件 gate 的具体分支缺口深入；只采用方向/范数/输出分布分账，不采 norm=truth、antipodal 校准概率、普遍 Pareto 或 ICL 正交。两 instruction 模型、TruthfulQA817/两fold及 judge/product 的局部反侧、base 高强度退步近正文；生产硬件/precision/batch/concurrency/SLO 未披露，未核实现或复现。root 实读必要原证与 actual owner/邻接 PRE 通过并授窄锁；作者实际正文/完整邻接顺读，root 非作者实际新正文/完整局部邻接及自身末注 POST 通过，窄锁释放；非日级验收。

- `SF-2026-ARXIV-2601-12703` — Daily `2026-01-22`增量；[Spectroscopy exact-v1](https://arxiv.org/html/2601.12703v1) §2.2–2.3/3/4.1。2+2+3=7；仅采用 tempered/local posterior 的负协方差响应诊断及功能分簇边界，不称真实逐token重训或唯一因果电路；未知q模态是解释，采样/归一化/population成本近正文。root实际必要原源/owner PRE通过并授窄锁；作者实际正文与完整邻接顺读，root非作者actual POST通过，窄锁释放。未核实现或复现，不授日级验收。

- `SF-2026-ARXIV-2602-08548` — Daily `2026-02-11`补查；[Cell Location exact-v1](https://arxiv.org/html/2602.08548v1) §2–6及必要B/C.1–6。2+1+2=5，只采用有限Qwen3-4B合成表下semantic binding与ordinal address分账；probe可读、delimiter/等长度反侧与局部shift不授唯一计数器、精确vector arithmetic或全模型table可靠性。Patch方向文字/Effect与5.2vs5.8反侧不一致隔离，token80/20 probe split不授whole-table OOD，100 heldout校准/α8与额外介入费用保留。root实际必要Source及Ch5/相邻交接PRE通过并授本一段/自身末注窄锁；作者实际正文与完整邻接顺读，root非作者实际225–245完整邻接及自身末注POST通过，窄锁释放。未核artifact或复现，非DAY。

- `SF-2026-ARXIV-2603-11749` — Daily `2026-03-14` 补查；[Compression/consistency exact-v1](https://arxiv.org/pdf/2603.11749v1) 方法/配对Tables1b/2a/3a与直接限制。2+1+2=5，coherent-false与随机错误的受控偏好、paired与corpus测量单位具体差额深入；不采MDL普遍真理、压缩唯一因果、全corpus一致方向或compute-matched scaling，错误族/训练seed/长度资格与外部证据回退近文。mar14_supplement 必要Source/owner/PRE经root实际非准备者复核通过，root窄写两段与本注；mar14_supplement 实际非writer 顺读两段、完整局部邻接和本注 POST通过，窄锁释放，不授DAY。未核代码或复现。
