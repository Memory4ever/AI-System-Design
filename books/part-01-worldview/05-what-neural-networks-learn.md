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

## 什么叫“好的表示”

一个表示是否好，不能脱离任务和约束判断。对某个任务有用的表示，可能主动消除另一个任务需要的信息。

可以从三个角度理解。

第一是 **separation**。原始空间中纠缠的样本，经过变换后可能更容易被简单决策边界区分。例如最终分类头只需线性变换，就能利用前面层已经组织好的特征。

第二是 **invariance**。对任务无关的变化，表示应尽量稳定。例如图像轻微平移不应改变对象类别；同义改写不应完全改变语义判断。但不变性过强也会丢失细节，所以它必须服务于具体目标。

第三是 **compositional usefulness**。中间特征应能被后续层组合，支持更复杂的判断。单个特征未必对应完整概念，它的价值可能只体现在与上下文中的其他特征共同计算时。

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

当匹配时，模型能用有限样本捕捉可复用规律；不匹配时，模型可能依赖 shortcut。例如训练图像中背景与标签高度相关，模型可能学习背景而不是对象。它在同分布测试集上表现良好，换背景后却失败。

即使训练目标显式鼓励类间表示分离，也未必固定这些方向在部署环境中的标签意义。受限的coding-rate反例里，稳定特征与环境相关特征都能映射到两条正交方向；当环境相关性反转，编码目标和表示的边缘分布可以不变，固定source classifier却把原先常正确的对应关系读反。要求一个coding operator在多个训练环境都最优，也只约束几何变换的inner目标，不能单独保证encoder的预测关系稳定；目标几何、固定读出和跨环境质量仍需分别验收。

这条反证必须保留精度与支持边界：在正噪声、完整source支持的有限模型中，失败encoder只是任意接近全局最优，精确最优配合不受限的source-optimal classifier反而可保持零目标误差；精确最优也全错的例子改变了支持域。同支持域还允许罕见输入变成主流，不能冒充小shift保证。构造证明的是coding近最优不足，不证明真实优化器一定选该解；额外class-conditional稳定假设、语义保持干预或跨环境验证都有成本，未验证时仍回退切片、反事实和真实OOD行为测试。 [必要机制与边界](https://arxiv.org/html/2609.21001v1) <!-- source-family:SF-2026-ARXIV-2609-21001 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21692:start -->
这个判断还可以获得一个更具体、但适用范围更窄的几何解释：若任务的数据空间近似为规则的紧致流形，模型已经充分优化，并且某类变换确实保持任务语义，那么数据流形与训练后模型预测空间之间的 representation gap 会受到任务 intrinsic dimension 支配。此时，equivariance 不只是架构偏好；它相当于把一个观测样本扩展为一组语义等价样本，从而降低需要由有限数据覆盖的有效维度。这解释了为什么与任务对称性匹配的表示可能改善样本效率，也把“归纳偏置有效”进一步落实为“它减少了哪些自由度”。

不过，这个量只拥有几何诊断权，不能接管泛化验收权。它依赖渐近样本、流形与群作用、充分优化等强假设，生成模型推导还集中于 DDIM 或线性高斯设置；估计过程本身也可能需要多个样本规模和多次模型拟合。若真实数据不存在所假设的对称性，或 intrinsic-dimension 估计与实际分布外表现不一致，就应回退到切片、反事实、held-out 与 distribution-shift evaluation，而不是把 representation gap 当作任意现代网络的通用 generalization error。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21692:end -->

因此，“模型学到了正确特征”不能只靠总体 accuracy 证明。需要构造切片、反事实、扰动和跨分布评估，检查模型究竟利用了什么相关性。

表示诊断还要区分“固定一种表示后训练读出”与“用同一批样本选择表示再训练读出”。对一种受限Brownian kernel head，固定表示的activation mass给出经验复杂度的尺度；即使表示从该样本学来，这个条件化的经验恒等式仍成立。问题出在把它直接升级为整个选择过程的泛化界：候选表示的supremum必须保留，候选threshold traces可以增加选择自由度。一个等mass有限构造中，每个固定候选的复杂度随样本数下降，整族复杂度却不下降；因此压低同一mass不等于消除了选择成本。

这条边界属于Brownian terminal geometry及披露的ReLU、head norm和trace-envelope条件，不是任意Transformer的风险公式；最坏经验容量也不是minimax预测误差。若表示与head使用同一数据选型，必须记录候选族与选型数据，另做selection-aware分析或独立held-out验证；选择成本的测量与额外数据有代价。受限实验只展示固定mass下的union gap，冻结特征上的小幅head收益不能代替端到端学习证明；约束未核时保留普通训练、数据切分和任务验收，不把一个低复杂度诊断自动当成泛化证书。 [必要机制与边界](https://arxiv.org/html/2609.21422v1) <!-- source-family:SF-2026-ARXIV-2609-21422 -->

## 记忆与泛化不是简单对立

一个常见二分是：模型要么记忆训练数据，要么学习可泛化规律。实际网络可能同时做两件事。

高频、结构稳定的模式可以被压缩成共享特征；稀有或不规则样本可能通过更局部的参数配置被记住。甚至同一输出既依赖通用模式，也依赖训练中见过的特定关联。

可以从压缩视角形成直觉：如果许多样本共享结构，用一套可复用计算解释它们比逐个存储更经济；如果样本没有明显共享结构，过参数化模型仍可能拟合它们。这个直觉有助于理解表示，但不是对所有神经网络泛化的完整定理。

这个视角还把闭卷事实错误拆成两个不能互相替代的问题：模型可能从未观察到相关事实，也可能观察过，却在有限参数容量中只能有损保存。前者是 coverage failure，增加相关数据或检索更直接；后者是 compression distortion，单纯重复相同事实未必消除，需要更多有效容量、更可压缩的结构、外部可寻址记忆，或在回答前允许检索与拒答。二者都会表现成“答错”，却要求不同补救；因此不能由最终准确率反推知识从未进入训练，也不能把扩大数据覆盖当作参数记忆无损的保证。

一个均匀随机事实映射下的 rate-distortion 下界只证明这种可分离失效在其假设中必然存在，不是现实 LLM 幻觉率公式。真实语言具有共享结构，模型还会使用上下文、推理、后训练和外部工具；这些机制可以改变有效压缩率或绕过闭卷回忆，但不会让有限参数自动获得“我是否可靠记住此事实”的校准能力。生产系统仍应把 retrieval、claim verification 与 abstention 作为独立证据路径。<!-- source-family:SF-2026-ARXIV-2609-12111 -->

判断泛化必须回到未见数据和部署分布。训练误差、validation 误差、数据去重、污染检查、时间切分和分布外评估分别回答不同问题。benchmark 得分高也可能来自训练数据污染或测试集与真实场景不一致。

对于生成模型，记忆还涉及隐私与版权风险。模型能够逐字复现某些训练片段，不等于全部知识都以逐字数据库形式存储；反过来，表示是分布式的也不意味着不会泄露具体样本。二者必须通过实证测试区分。

## 分布式表示与 Superposition

如果每个可解释特征都占据一个独立坐标，理解网络会容易很多。但网络的表示维度有限，潜在有用特征可能远多于维度，而且很多特征不会同时激活。模型可以让多个特征共享表示方向，以更高效地利用容量，这种现象常用 superposition 描述。

它带来一个 trade-off：共享可以提高表示容量，却增加干扰和解释难度。单个神经元可能是 polysemantic 的，一个概念也可能分布在多个方向上。通过 probing、activation patching、feature visualization 或 sparse decomposition 可以获得证据，但这些方法观察的是模型行为的某个投影，不应轻易升级为完整因果解释。

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

多句话中同一实体还可能承担不同关系，因此仅记录“哪个实体”不足以确定属性该绑定到哪里。一种受限的机制假说把地址拆为 entity 与 relation 两个索引：在受控文本中，先用属性 token 的 activation 拟合索引，再沿拟合的子空间替换或扰动，检验输出是否跟随指定绑定变化。这比只凭语义相似或角色标签多了一步局部使用证据；但拟合出的 cell 不证明网络拥有物理表格、唯一符号地址或开放任务上的稳定读写协议。<!-- source-family:SF-2026-ARXIV-2604-19052 -->

同一关系结构跨语境也未必沿用同一读出坐标。作者在有限合成域中观察到原投影跨 context 退化，而根据相同索引的 activation 差拟合 translation 后，部分读出得以恢复；这种校准需要配对数据，也受上下文和干预范围约束。因此，可迁移几何、局部行为作用与任务泛化须分别验收；坐标失配或 patch 连带影响其他功能时，应回退行为测试和原模型，不能把 probe 升级为通用编辑器。

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

Jacobian-adjusted lens 一类方法提供了一个具体例子：它不直接把中间 activation 投影到
最终词表，而是用该 activation 对后续 residual 的局部 Jacobian 近似 layer-to-output
影响，再配合 activation swap、ablation 或 modulation 检查候选方向是否被计算使用。
这个方法的重要性不在于给出又一种“可视化”，而在于把 readout 与 intervention 放进同一
实验链。其局部一阶近似、跨 context averaging、token-indexed representation 与模型范围
仍限制外推，因此它是证据阶梯的实例，不是模型内部知识的最终字典。

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

探针能从某层表示中解码出属性，只说明该属性与当前表示相关；它不证明对应知识集中在一个可移除模块，也不证明干预该方向会按预期改变行为。训练样本的混合粒度会把多个因素共同压进参数，因此模块性必须靠删除、替换和跨分布干预验证。探针仍适合发现候选结构，但在因果证据缺失时，只能拥有诊断权，不能拥有模型编辑或发布决策权。
<!-- source-family: arxiv:2608.10214v1; semantic-body-binding: probe-decodability-versus-modular-control -->

## 小结

神经网络学到的不是可直接翻阅的规则表，而是分布在参数与激活中的计算结构。它把输入映射到为训练目标服务的表示空间，在其中放大有用差异、压缩部分无关变化，并让后续层更容易完成任务。

这种能力既来自数据中的规律，也来自架构和优化的偏好。它可以表现为泛化，也可以夹带记忆、偏差和 shortcut；它能在训练分布上工作，也可能在 distribution shift 下迅速失效。理解这些边界，是把模型指标连接到 Evaluation、Observability 和数据反馈闭环的前提。

### 可解释标签不是 Feature Identity

Sparse autoencoder 把 activation 分解为稀疏 feature，短自然语言标签便于人理解；但当标签空间远小于 feature 空间时，不同 feature 会发生 descriptive collision。传统 detection score 只检查“看到解释能否预测 feature 是否激活”，即使多个 feature 共享解释和相近激活分布也可能同时得高分，因此可读解释不能独自拥有 feature identity。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12874 -->

更可靠的解释合同应同时记录 collision rate、激活差异、干预结果与未能区分的候选 feature。这样增加了标注和因果验证成本，也仍可能受评估语料覆盖限制；无法通过区分性与干预复核时，应回退到 activation statistics 和具体输入实例，不用标签替代机制。exact-v1 证据限于所用 SAE、标注语料和自动解释评价，不能证明自然语言标签能唯一指代内部概念。

### 行为方向可能早于 Post-training 形成

把 persona 或高层行为全部归因于 alignment 数据，会忽略 pretraining 已经形成的可复用表示方向。沿训练 checkpoint 追踪 residual directions 的受限实验显示，一些 persona-like directions 在早期预训练便出现，并能迁移到同家族的 post-trained checkpoint；后训练更像重塑其可访问性和表达强度，而不一定从零写入行为。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13329 -->

线性可解码和 steering 效果仍不等于单一方向拥有完整因果控制，跨模型与跨数据配方也未证明。系统上应把 pretraining data provenance、checkpoint lineage 与 post-training intervention 分开审计；方向不能稳定复现时，回退行为级 evaluation，不据 representation probe 推断模型“拥有某种人格”。

## Review notes

- `SF-2026-ARXIV-2604-19052`：[exact-v1](https://arxiv.org/html/2604.19052v1) §3.1–3.3/Eqs2–6/Figures2–9，Daily 2026-04-22。采用 entity×relation 索引及跨 context 有限 translation 的受限机制分支；属性 token 拟合、PLS/patch 和受控合成域只支持局部可读与行为作用，不证明物理表格、唯一符号地址或开放 LLM 泛化。root 必要来源→当前 Ch5 owner 写前、实际正文及相邻论证写后非作者复核均通过；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-18907`（Experimental）：[Gradient-Based Program Synthesis with Neurally Interpreted Languages exact-v1](https://arxiv.org/html/2604.18907v1) §3.1–3.4/§4.1–4.5；采用训练期 primitive/codebook 与共享循环 executor、测试时冻结执行器并优化 program latent 的职责分支，不采唯一符号真值、无界长度或通用 LLM 编程能力。受控 Shift/Composition、DeepCoder/LPN 比较与多起点/梯度搜索成本限制外推；root 必要 source→Ch5 采用及实际正文写后独立复核通过，复核时纠正“连续身份”与端到端对照措辞，未复现实验。

- `SF-2026-ARXIV-2604-13082`：[exact-v1](https://arxiv.org/html/2604.13082v1)，Daily 2026-04-16；必要证据 §4.1/§5.2 的 encoder/decoder 移植、冻结与 rewind，§5.3–5.5/§6 的编码、表征失败和任务迁移边界。仅采用模块诊断区分表示形成与读出失败，不采用 2.75× 为总训练成本收益或普遍 decoder 瓶颈。root 有限 source→owner 与本次实际写后独立复核通过，未复现实验。
- `SF-2026-ARXIV-2604-13694`：[exact-v1](https://arxiv.org/html/2604.13694v1)，Daily 2026-04-16；必要证据 III-A–D、IV 与 V Scope，采用 matched-checkpoint anchor 恢复与 activation 中继分责，再用输出 KL/IFEval 单独核行为；保留 same architecture/fixed input/matched anchor、Q/O 与同一 MLP neuron gate/up/down 粒度、梯度筛选与实际替换验收及六代表任务范围。不是唯一知识来源或全模型通则。root 有限 source→owner 与修正后的实际正文/相邻论证写后独立复核通过，未复现实验。

- `SF-2026-ARXIV-2604-12151`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12151v1) Roman III、IV.1–IV.7、V。有限 stationary Markov 链与两层模型；统计归纳/任务取回、训练竞争/表示容量两层区分，task vector 可在足够容量下泛化。patch 非完整唯一 circuit，不外推开放 LLM 阈值。6分实际缺口深入；必要来源/owner 独立复核通过（apr02），实际正文及相邻交接写后非作者复核通过（root、apr02），未复现实验。

- 2026-09-01 角色绑定的受限解释：<https://arxiv.org/html/2608.29034v1> §2–3/7 与 <https://arxiv.org/html/2608.29530v1> §3/6–9。人工 role、受控任务与有限替换不证明表示唯一；生成 token 等原 forward 仍保留，DISCOVER 的组合 holdout 不等于 target 预训练未见。正文不采神经/符号的哲学定论。

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
