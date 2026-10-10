# 第28章 Pretraining

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-PRETRAINING`
**Legacy Chapter:** Ch24
**Status:** Draft

**Roadmap Intent:** 大规模预训练如何形成通用语言和世界知识。

## 本章要回答的问题

第 27 章已经把数据构造成 token sequences，Part II 也已经给出 Decoder-only 模型。模型怎样仅通过预测下一个 token 改变数十亿参数？Loss 下降、perplexity、训练 token 数、optimizer step 与能力增长分别是什么关系？梯度异常时，warmup、clipping、adaptive optimizer 与逐层 learning rate 分别能解决什么？为什么一次成功的 Pretraining run 不只是反复调用 `backward()`？

本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`V` 表示 vocabulary size，`theta` 表示模型参数，`z_(b,t)` 表示位置 `(b,t)` 的 logits，`y_(b,t)` 表示对应 target token id，`N` 表示累计参与 loss 的有效 tokens。

## 从随机参数开始会发生什么

训练开始时，Embedding、Attention 和 MLP 参数通常无法产生有意义的条件分布。给定 prefix：

```text
The capital of France is
```

随机模型可能给所有 vocabulary tokens 近似无结构的 logits。数据提供真实后继 token，loss 衡量模型分布与 target 的差距，backpropagation 再把误差信号传回所有相关参数。

单个样本只提供一个局部更新。Pretraining 的能力来自大量不同 contexts 反复约束同一组参数：语法、事实、代码模式、推理模板和文档结构必须在有限参数中形成可复用计算，而不是为每条文本创建独立规则。

这也解释了为什么“训练看过某句话”与“模型可靠掌握其中知识”不是同一命题。出现频率、上下文多样性、参数容量、优化竞争和 Evaluation 方式都会影响结果。

## Next-token objective

第 18 章已经得到 causal factorization：

```text
p_theta(x_1,...,x_T)
= product_(t=1)^T p_theta(x_t | x_<t)
```

训练张量中，位置 `t` 的 logits 用前缀 `x_<=t` 预测 label `x_(t+1)`。对一个有效位置：

```text
p_theta(y | x_<=t) = softmax(z_t)[y]
loss_t = -log p_theta(y | x_<=t)
```

Batch masked loss 可以写成：

```text
L(theta)
= - (1 / sum_(b,t) m_(b,t))
  * sum_(b,t) m_(b,t)
  * log p_theta(y_(b,t) | x_(b,<=t))
```

其中 `m_(b,t)` 为 loss mask。Padding、跨文档边界或不参与监督的位置应为 0。Logits shape 是 `[B,T,V]`，labels 与 mask shape 是 `[B,T]`。

这个 batch mean 还有跨 step 的权重含义。每一步按自己的有效 token 数归一，在 counts 相近时简单稳定；length grouping 让不同 step 的有效 count 明显变化后，均匀累积 batch means 会让不同 token 获得不同的总体优化权重。比较长度课程时，因而要同时固定或记录 token exposure、batch composition、loss normalization 与预算，不能把最早一个 epoch 的改善只归因于短到长的顺序。固定归一量可以作为隔离 weighting 的诊断，但不是默认更优的训练目标。

[受控 speech-token 实验](https://arxiv.org/html/2609.25890v1)在匹配 exposure 后发现部分顺序收益减弱，支持这四种因素分账；AdamW 的历史状态与非线性归一又使梯度尺度不能直接换算成同比例参数更新。证据限受测 speech tokenizer、小模型、八个训练 seeds 与具体预算，不证明文本大模型通用课程。改变 weighting 会引入目标分布和超参数重校准成本；有效 counts 稳定、原 token-weighted 目标已经验证时，既有 masked mean 和普通 shuffled batches 继续成立。
<!-- source-family:SF-2026-ARXIV-2609-25890 -->

普通NTP让每个有效位置都学习原GT，却不区分难拟合的事实续写与可接受的措辞变化。一条受限委派分支以事实标注proxy和当前高loss提出候选位置，把这些位置的训练target改成CALL；其余位置仍学原GT，但在排除CALL后重归一化的分布上计算loss。它改变的是模型学习“自己续写还是请求续填”的目标，不是从高loss直接认证事实错误，也不是证明参数删除了事实知识。训练中的CALL配额与部署时的调用预算是两个验收对象，[pilot对照](https://arxiv.org/html/2602.12005v1)的15%训练target与22%部署budget不能合并为固定线上调用率；cascade返回也可能错误或跨越不同tokenizer的多token边界。Proxy标注、cascade生成、真实结果核验及所有forward都须计费，匹配GT-gradient token数不等于匹配总训练计算；Ignore/Ignorefacts屏蔽目标的对照在匹配forward步数时可失去原训练收益，因此不能把等GT-gradient预算的差额全归因于事实委派。Proxy失配、漏CALL、委派质量或净成本退步时，降低/关闭委派目标，保留普通NTP与独立质量验收，不以局部FactScore或loss代替事实真值。<!-- source-family:SF-2026-ARXIV-2602-12005 -->

### 预测方向与知识可访问方向并不相同

标准NTP沿文本顺序预测，目标明确且可以直接学习语言分布；但训练过“来源实体A对应目标B”，不等于参数在“已知B，查询A”时受到同等约束。问题不是Attention看过哪些token，而是**哪些未知量曾成为需要从其余信息预测的target**。一个有条件的替代分支让来源实体也进入重建目标：MLM直接预测被遮蔽位置，Decoder-only则可把遮蔽文本放入prefix，再对完整续文做NTP。这样改变监督可访问的信息与loss支持，不是仅把causal mask删除。

在[方向检索的受控消融](https://arxiv.org/html/2604.04943v1)中，始终不把来源实体设为预测目标时，反向检索失败；允许来源预测后改善，但MLM还需要相应的其他遮蔽条件。这只证明该来源预测消融可定义的所测关系任务中的目标依赖，不是所有语言知识的必要充分条件。BERT与Gemma、base与instruct的比较也不完全控制模型身份。改善反向答案并不证明形成了方向无关的统一概念：距离和线性probe支持两方向分别索引的解释，却不能排除系统性非线性关系。

重建分支增加样本格式、遮蔽策略和额外训练，可能改变自然语言统计；原NTP在顺序建模和所需查询方向已充分覆盖时仍合理。训练验收应分开“行为能否访问”和“表示是否共享”，不由反向准确率直接宣布知识无损内化。第29章会进一步说明：指令demonstration也通过样本结构与loss mask改变哪些行为得到监督。<!-- source-family:SF-2026-ARXIV-2604-04943 -->

### Future-token 辅助目标改变的是学习路径，不只是标签数量

NTP在每一步都提供明确的局部监督，适合顺序语言建模；但模型能表达某条计算路径，不等于当前loss的梯度能把它学出来。若一个中间答案必须结合后续路径的信息，而teacher-forced前缀又提供容易拟合的局部线索，模型可能优先学习局部续写。一个替代分支从同一真实prefix并行预测多个未来token，让辅助loss约束共享表示；推理仍可只用下一token头。它与顺序串联的MTP模块、以及推理期的speculative验证是不同设计，不能把训练辅助目标的收益直接记为推理加速。

关键不是“多预测几步必然学会规划”，而是辅助目标是否打开了原先难以形成的梯度路径。[一个两层受控模型](https://arxiv.org/html/2604.11912v1)把content与position分块，并固定不同读头读取浅层或深层的content块：浅层future-token loss可以绕过尚未训练好的第二层，先让第一层形成指向前驱位置的模式；随后固定第一层，再由第二层做content matching。这解释了一种表达能力与优化可达性分离的情形。但相应gradient-flow结论依赖零初始化、Toeplitz结构、固定读头和分阶段冻结，并非标准Transformer联合训练必然收敛到该回路的证明；attention图像相似也不能替代开放任务上的因果验证。

因此，是否增加future-token监督，应比较原NTP在哪类依赖上受限、辅助目标改变了哪些梯度和标签支持，以及额外head与loss权重消耗多少训练工作。受限图任务中NTP也能随数据或模型规模改善，有限图实例还可能被记忆；Countdown的best-checkpoint选择与SAT的final-checkpoint评价不能混成统一能力保证，额外头的训练也不等于匹配FLOPs。目标依赖已充分学习、未来标签不可靠或辅助任务与部署目标竞争时，保留NTP仍合理。这里得到的是可检验的优化分支，不是用MTP替代全部next-token训练的结论。<!-- source-family:SF-2026-ARXIV-2604-11912 -->

另一条早期梯度引导分支不增加 future-token 标签，而把已训练小 teacher 的最后层表示作为较大模型早期层的临时辅助目标：按 token 对齐并在需要时投影维度，在 NLL 之外加入负 cosine loss，让其权重随 training steps 衰减至零，再由普通 NTP 继续训练。这里 teacher depth、learner layer 与关闭监督的时间是三个轴，不是“大 teacher 蒸馏小 student”或推理期捷径。[LET exact-v1](https://arxiv.org/html/2602.05393v1)仅支持所测 1.4B/3B/7B、Pile 与 A100 设置；过强辅助权重会退步，teacher 预训练、额外前向与 projector 也要计费，较少收敛 steps 不证明更高 throughput 或总 wall-time 更低。表示相似不是目标能力真值，也不能自动解决 tokenizer/语义错配；引导失配、held-out 退步或成本超过收益时，保留普通 NTP、较低权重或更早关闭监督，旧统一训练路径仍成立。<!-- source-family:SF-2026-ARXIV-2602-05393 -->

未来序列也可以成为 rollout 的辅助目标，而不只增加并行预测头：先对真实序列做 teacher-forced 前向，在分块后的候选位置按平滑 entropy 抽取 prefix，再让当前 policy 续写短序列，将续文 hidden states 与同一 policy 在真实后缀上的 states 做 cosine 比较。这里的参照是模型自身的表示代理，不是外部 teacher 或独立语义真值；同一真实序列里不同 prefix 的 rewards 归一化成一组，也不等于同 prompt 的多次独立 completion。该分支保留完整序列 NTP，再以 GRPO 更新短 rollout，比较的是目标和采样人口的选择，而非 CE 不会定义序列概率。[有限原始对照](https://arxiv.org/html/2602.16704v1)中更长 continuation 并不单调更好；真实后缀前向、prefix 重算和额外生成都需计费，同步数/文本 token 数不等于等 FLOPs，fast-weight 跨截断 prefix 的高效复用也仍有实现压力。表示代理失配、长 rollout 不稳定或预算不合适时，保留普通 NTP、并行 future-token 头或前述外部 teacher 引导，不能由局部收益宣布获得语义规划保证。<!-- source-family:SF-2026-ARXIV-2602-16704 -->

还有一条不生成 future labels、也不调用 teacher 的表示正则分支：在同一次真实序列 forward 的最后层随机取 `s<r<t`，将两段 hidden displacement 的 `1−cos(h_t−h_r,h_r−h_s)` 加入 NTP。它施加局部方向一致 prior，而不是访问未知的“最优语义轨迹”；BOS/EOS 名称相同也不保证真实 hidden state 满足理论端点条件。[Semantic Tube Prediction v1](https://arxiv.org/html/2602.22617v1)的有限五seed对照支持这种辅助目标，不能继承一般 geodesic、no-collapse 或开放语义正确保证。较少 unique samples 配合更多 epochs 仍可消耗相近 token/steps，表示读取、采样与任务相关 λ 搜索同样付费；不新增推理路径不等总训练免费。语言轨迹不满足局部直线 prior、NTP竞争或 held-out 退步时，降低/关闭正则，保留普通 NTP、future-token 或经验证的 teacher 引导。<!-- source-family:SF-2026-ARXIV-2602-22617 -->

表示正则还可沿模型深度定义，而不是只沿 token 序列约束方向：若监督主要从最后 hidden layer 读出，较大转向可能集中在末层；仅惩罚末层角度又可能把转向移到倒二层。一个条件分支把相邻 layers 的 angular change 加权纳入全部层目标，显式选择控制对象与深度权重，而不把角度小等同于语义冗余或训练稳定。[受限 JREG 对照](https://arxiv.org/html/2601.18302v1)支持此控制分支，单任务仍有退步，early-exit实验也不授任意删除层；读取/保存中间状态、额外正则与深度重新调参增加内存和训练费用。权重、层集合、原NTP目标与held-out任务共同验收，几何prior不适配或净成本不值时，降低/关闭正则、保留原训练与真实任务检验，不由layer角度曲线自签表达能力保持。<!-- source-family:SF-2026-ARXIV-2601-18302 -->

### 训练目标可以改变记忆压力，但不是纯记忆开关

同样的语料、架构和更新预算也未必产生同样的记忆—泛化关系，objective本身是一项干预。除普通交叉熵外，可用较低训练温度`tau`定义另一项`CE(softmax(z/tau), y)`，再以`alpha`作两项loss的凸组合。这改变训练梯度，不是生成时的Sampling temperature；两种softmax的梯度相加，也通常不等于某个单一温度的交叉熵。

要判断这项干预是否只是提高训练样本回忆，应在同一模型族内固定数据、优化器和步数，分别测已暴露样本、未暴露样本及生成多样性，再用单温度训练对照。[Memory Dial](https://arxiv.org/html/2604.05074v1)的短继续训练给出这种匹配比较：所测已注入样本的准确率增加，部分held-out指标保持稳定，同时输出更相似。它支持“额外记忆压力可成为实验轴”，不支持`alpha=0`没有记忆、提高`alpha`必然不损泛化或已经把记忆从所有能力中完全分离。

该证据限英语为主的模型、449步、三seed及至多两H100的设置，主要协议主动注入少量评估样本；自然序列与其他语言对照也不等于真实大规模预训练。高置信且正确的logit在小`tau`下梯度可能更快趋零，因此不能把作者的梯度直觉概括为所有高置信样本都被放大。新增双目标与参数扫描消耗训练预算，并可能增加逐字泄漏、降低多样性或改变其他任务；泛化/隐私证据不足时保留普通CE。先看一个局部loss数值，再看它为何不能替代这些独立验收。<!-- source-family:SF-2026-ARXIV-2604-05074 -->

## 一个 token loss 小例子

假设某个位置有三个候选 token：

```text
z = [2,1,0]
softmax(z) ~= [0.665,0.245,0.090]
```

若正确 target 是 token 1：

```text
loss = -log(0.245) ~= 1.407
```

若参数更新后概率变成：

```text
p = [0.25,0.65,0.10]
loss = -log(0.65) ~= 0.431
```

Loss 下降表示模型对这个 target 分配了更高条件概率。它没有说明生成时一定选中该 token，因为 Sampling 仍可能选择其他候选，也没有说明整段回答事实正确。

## Perplexity 能回答什么

### Mean Cross-entropy 也会被重尾 Token 支配

平均交叉熵保留了概率模型的标准训练语义，但少量极高损失 token 会主导曲线，使它在某些阶段与下游质量不同步。评估应同时报告 mean、median 或分位数损失，并检验它们与目标任务在当前数据、模型规模和训练阶段的 concordance；median 不是替代目标，而是定位重尾贡献的诊断传感器。收益是减少对单一平均值的误读，代价是指标选择与早停规则更复杂；分布稳定、异常尾部本就重要时，mean CE 仍是正确聚合。当前证据只展示特定训练轨迹中的失配，不能把 median CE 升格为通用质量指标。

<!-- source-family:SF-2026-ARXIV-2605-24667 -->

若平均 token negative log-likelihood 为 `L`，perplexity 定义为：

```text
PPL = exp(L)
```

它可理解为模型在该数据分布上的平均不确定性尺度。PPL 较低通常表示更好的 token prediction，但比较必须满足：

- 使用相同 tokenizer 与 tokenization。
- 使用相同 Evaluation corpus 和 loss masking。
- 明确是否包含 special tokens、padding 或不同 domains。
- 不把小幅平均差异直接解释成特定能力提升。

不同 tokenizer 会改变 token 粒度，因此跨模型直接比较 PPL 可能没有可比性。PPL 也不能替代事实、代码执行、安全或指令遵循评估。

同一离散音频模型内，也应把 token 人口与任务族拆开。固定总 token/FLOP 后加入更多 acoustic codebooks，会改变相同预算能覆盖的音频时长；再交错 transcript，又改变可学的跨模态读写接口，不能把它们当作语义容量免费扩展。[必要对照与缩放反侧](https://arxiv.org/html/2602.16687v1)在固定 Mimi rate、English mixture 与受测规模下观察到 acoustic 任务获益而部分 semantic 任务退步；all-token NLL 与 ASR/TTS 相关，不表示所有语义任务同步改善，较大规模还出现任务分化或饱和。由这类 NLL 拟合出的 data/model loss-optimum，只约束该 codec、token composition、数据与预算区间，不是通用音频指数，更不等于部署最优；推理成本可让较小模型的 overtraining 更合理。训练 owner 应保存 codebook/rate、各类 token 的暴露与重复、NLL mask，并联合检查语义、声学、跨模态质量和完整成本；tokenizer、数据或 warm-start 条件变化时重新验收，保留 semantic-only、独立任务路径或已验证的 text-first backbone，而不凭一个总 loss 选择统一模型。<!-- source-family:SF-2026-ARXIV-2602-16687 -->

## 目标扩展与训练计算路径

### 更多 Context 可能降低知识写入参数的压力

下一 token 目标只要求利用当前可见信息；当答案能直接从长上下文读取时，模型未必需要把规律内化进 weights。训练系统要区分 context-use 与 parametric internalization，并把数据切分、遮蔽、顺序和目标函数作为共同设计。缩短或打散上下文可能增加内化压力，却会牺牲长程建模与吞吐，不能把“信息更多”直接等同于“参数知识更强”。
<!-- source-family: arxiv:2608.12218v1; semantic-body-binding: context-abundance-parametric-internalization -->

### 从固定 Objective 到 Feedback-guided Self-supervised Update

标准 next-token prediction（NTP）把观测到的一个 token 当作唯一监督目标，适合学习可采样的词面分布，也让 loss 与 PPL 有清晰语义。但同一前缀可能有多个语义近似的合法续写；若任务真正关心某个概念而非固定词形，单一标签会把其余候选压成竞争项。一条受限的目标分支先为当前位置构造上下文相关的等价 token 集，再把 `-log p(observed token | prefix)` 与 `-log sum_{t in set} p(t | prefix)` 插值：前者保留词面概率校准，后者把部分梯度指向共享语义质量。这改变的是训练目标和标签所有权，不是推理时自动拥有概念真值。

等价集本身可能由另一个模型生成，因而会引入教师偏差、歧义和额外数据处理；扩大概念权重也可能改善局部词汇语义指标却损伤全局 token PPL。原 NTP 在缺少可信等价集、需要精确代码/API token 或词面分布本身重要时仍是基线。现有实验只覆盖英语单 token 的完整名词、动词、形容词、Llama 1B/3B/8B 的短继续训练及有限词汇相似度任务，不证明开放推理、指令遵循或全规模预训练受益。<!-- source-family:SF-2026-ARXIV-2603-29123 -->

目标粒度还可从单个词形扩到后续 token 块，而不取消词面监督。[一个有界分支](https://arxiv.org/html/2602.08984v1#S3)把相邻 hidden states 池化成训练 target，用分段 codebook 约束下一块预测的可表达向量，再以各 codebook 的软加权组合辅助逐 token 读出；学习的是内生 latent target，不是外部给定的语义概念，线上仍按 token 自回归。未来块状态只可作训练监督，辅助预测加入 token 前缀的 shift 与边界必须独立验收，不能把 teacher target 当作线上已知。连续 target、codebook 拟合与 token CE 相互耦合，单独加一种 loss 仍可能退步；码本坍塌、插入位置与 gradient detach 规则也改变质量与费用。有限预训练与继续训练支持这种组合目标的局部取舍，不授语义真值、普遍缩放或完整 serving 加速；码本、因果边界或净质量与预算未核时，保留原 NTP、可信等价集与无此旁路的 baseline。<!-- source-family:SF-2026-ARXIV-2602-08984 -->

标准 next-token loss 让模型学习利用前缀，却不直接教它区分“远处有决定性证据”和“远处只是干扰”。在长文档拼接或 distractor-heavy 训练中，一种条件性补充是先用短上下文预测充分性作 gate：只有目标 token 已被局部片段较好解释，且完整前缀带来的增益很小，才把远前缀扰动前后的预测分布拉近；真正依赖远处证据的位置仍保留原始 causal loss。这样改变的是**何时应忽略远处信息的训练信号**，不是缩短可用窗口或强制所有 token 不看远处。

该目标需要额外 clean/corrupt forward、短窗参考预测和 gate 校准。gate 误判会压制真实长程依赖，构造的扰动若改变了语义也不再是无害对照；普通 next-token 训练在上下文干扰少、额外算力不值得或缺少可验证扰动时仍是清晰基线。作者的 0.3B～1B 预训练与五个基础模型的 continued-training、RULER/NoLiMa/HELMET 实验支持受测条件下的选择性抗干扰，不证明开放长文档问答、所有长度或生产推理都受益；长上下文能力的评价边界仍由第 22 章承接。<!-- source-family:SF-2026-ARXIV-2609-27925 -->

扰动一致性还可以不带语义 gate：[一种受限目标](https://arxiv.org/html/2602.08287v1#S6)按给定相关率保留输入 token 或随机替换，训练时对两次前向的输出类别概率内积加奖励。它鼓励输出 agreement，也可能同时推高置信，不能把 random replacement 预设为保义干预；应分别验目标质量、扰动响应与置信分布，而不以更平滑直接签正确性。有限 parity、modular 与极小 WikiText 模型只支持受测正则学习分支，少训练 iterations 不等于少 wall time，额外 corrupt forward 仍需付费。替换会改变目标依赖、置信塌缩或完整质量与净成本退步时，保留原 NTP、上面的条件 gate 与可靠监督，不推广任意 Transformer 稳定保证。<!-- source-family:SF-2026-ARXIV-2602-08287 -->

固定 next-token objective 的优点是反馈来源稳定、覆盖广；SFT/RL 直接使用 labels/verifier，更贴近任务但改变
训练阶段。一条中间分支让少量 downstream examples 只产生 detached gradient direction，用它选择或构造
当前 batch 的 self-supervised target，再由 learner 继续优化 pretraining loss：

```text
feedback batch → detached downstream gradient
candidate self-supervised targets → candidate pretraining gradients
choose target by local gradient alignment
learner updates only on unlabeled batch
```

它把 checkpoint-level data retuning 推进到 step-level objective selection，却不再是无条件 unsupervised：
feedback distribution、designer version 与 alignment approximation 都属于训练 identity。局部 gradient alignment
不保证长期 trajectory，更可能牺牲 general capability；无可信 verifier 或多域冲突强时固定 objective 仍更稳。

另一条实验性反馈分支不选择替代 target，而比较同一 prefix 下 frozen RL reference 与当前 learner 对 observed token 的 log-probability 差，经序列内中心化、sigmoid 与有界 clipping 得到权重，继续优化 weighted NTP。它不是对冻结 base 计算静态分数、全词表蒸馏或在线执行 RL；reference 质量、序列划分、权重变换及 learner checkpoint 都属于目标身份，并支付额外 reference forward。尤其权重含当前参数 θ，而原文未披露 detach：不能因此把它视为 θ 独立的固定目标，或借用 KL 梯度方向等价来保证更新。[受限 mid-training 对照](https://arxiv.org/html/2602.03075v1)仅支持该反馈接口在所测条件中的作者结果，不授通用算力优势或无限自我改进；reference 失配、权重/梯度条件不明或下游能力回退时，固定 NTP 仍是清晰基线。<!-- source-family:SF-2026-ARXIV-2602-03075 -->

### Adaptive Depth：计算量也可以成为训练出的状态

固定层数让每个 token 走相同计算图，最适合 dense batching、kernel fusion 与可预测 latency。若模型将同一
block 重复应用，并学习 token-level exit/continue policy，就能把“多深”从架构常数变成条件计算决策；
再用 latent-step reward 同时约束 accuracy 与 compute，可把 recurrent depth 纳入训练目标。

这条分支用潜在的 token-level compute 节省换来 exit calibration、不同 token 进度、batch divergence、
KV/activation identity 与恢复复杂度。它在作者受限实验中是 `Status: Experimental`，不能据此断言实际
wall-clock 或 energy 一定下降。硬件偏好规则 shape、SLO 要求稳定、exit policy 漂移或缺少专用 kernel 时，
固定深度仍是更好的系统设计。

训练形成的计算轨迹与部署是否共享参数，还应分开选择。一个成长训练分支从浅层起步、复制中间层逐步加深，最终仍保留各层独立权重；它与从头把中层绑为循环 block 并非同一架构合同。受限对照中，成长后的模型也可能在部署时额外复用中层 block，而无需预先以循环方式训练；共同的后层使用与周期性 residual signature 只是这个解释的证据，不证明唯一内部算法。[必要机制与反侧](https://arxiv.org/html/2602.16490v1)同时显示，全共享循环更怕换序，多次额外循环常会退化，math cooldown 的数据来源与所选 block 又改变收益。成长减少早期训练层数，不会免费减少最终参数或串行推理费用；参数量、训练 FLOPs、有效深度及推理预算必须分账。未校准的复用、质量回退或系统时延不合算时，保留原 untied 固定深度；需要明确监督与停止证据时仍用已验证的循环目标或可见 CoT，不凭成长历史任意延长执行。<!-- source-family:SF-2026-ARXIV-2602-16490 -->

多个固定深度模型还可以共用一个 prefix，而不学习逐 token 的 exit：在同一 backbone 的若干深度接入分支 head，用多分支 CE 与随时间变化的权重共同训练，让短分支和长分支对共享层的梯度一起参与。[一个受限 family 分支](https://arxiv.org/html/2602.22543v1)另在冻结旧 backbone 后新增 blocks，把 attention/FFN 的输出投影置零作 identity initialization，只训练新增部分和 head；初始化时函数不变，不等于后续更新仍保留所有旧能力，内部初始化与 replay 也有各自成本。这是静态 shared-prefix family，不是已实现的 adaptive routing 或 learned stop policy。分支冲突、continued pretraining、head、新层训练、共享驻留和部署配置都须分账；小分支总体平均及大分支的部分数学/代码指标低于各自基线，不能由某个 MMLU 改善宣称所有能力密度更高。固定分支质量、共享收益或实际服务预算不成立时，保留独立固定深度模型、原 untied backbone 与已校准 exit policy，不把家族共享当免费训练或推理加速。<!-- source-family:SF-2026-ARXIV-2602-22543 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20613:start -->
层级递归模型还可把长程 credit assignment 拆成多时间尺度 hidden-state update，并用特定 normalization 控制
递归梯度。这类 HRM-style objective 改变了 recurrence depth、state identity 与 optimizer dynamics；论文规模、
数据和 MagicNorm 设置上的收益不证明它是 Transformer 预训练的通用替代。递归状态不稳定、墙钟成本或 matched
baseline 不占优时，应回退固定深度 objective 与常规 normalization。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20613:end -->

### Latent Reasoning 要分开路径优化与表示空间约束

把显式 chain-of-thought 压入连续 latent state，可以缩短可见序列并让中间计算更自由；但“最终答案 loss 能反向传播”不代表每一段 latent trajectory 都获得了有效监督。深路径上的 gradient attenuation 属于 optimization-path failure，而不同 latent step 漂移、坍塌或失去可区分性属于 representation-space failure，两者需要不同传感器和 actuator：前者检查梯度到达与中间目标，后者检查表示几何、可预测性和跨步一致性。

联合监督可能改善可训练性，却增加辅助目标、权重调节与错误 inductive bias；强行让 latent 可解释也可能限制有效内部表示。显式 reasoning、较短 latent path 或只监督终态在任务简单、路径稳定时仍成立。现有证据只覆盖特定 latent-CoT 设置，不是所有隐藏推理架构的收敛定理，也不提供可解释性保证。
<!-- source-family:SF-2026-ARXIV-2606-20075 -->

### Distillation 要分开 Prefix Provenance 与 KL Direction

Teacher-forced SFT、student-prefix DAgger、offline RL 和 on-policy distillation 常被统称为“向 teacher 学习”，但它们分别改变生成 trajectory 的 owner 与 KL 的方向。相同 teacher 在不同 prefix distribution 上给出的 target 不等价，forward/reverse KL 又对 mode coverage 与 mode seeking 有不同压力。

训练合同因此要冻结 prefix provenance、teacher/student revision、KL direction、sampling 与长度 curriculum；KL mixing 或 entropy-gated curriculum只是条件分支。它们用更多控制状态换 accuracy/diversity/compute 的折中，也可能造成 off-policy mismatch 和 coverage collapse；证据不足时回到单一、可重放的 SFT objective。

<!-- source-family:SF-2026-ARXIV-2605-16826 -->

Prefix 和 KL 合同也不能代替训练样本的恢复测量。Student 的总体逐字恢复率比同架构、同数据的 CE baseline 低，仍可能在少数 teacher 可恢复的样本上保留特殊关联；应在同一探针下分别测 teacher、student 与 baseline，并区分总体恢复集合和 teacher∩student 中排除 baseline 后的交集。这个差额提示总体下降不能排除 teacher-specific 的样本传递，却不是样本知识必然来自 teacher 的因果证明：有限前缀、greedy continuation 与 exact-match 门槛会改变可观测集合，也不能涵盖其他抽取路径、总体隐私率或 DP。训练目标拥有这项三路对照；自适应抽取与隐私保障的判断仍交给[安全边界](../part-06-ai-infrastructure/72-security.md)。
<!-- source-family:SF-2026-ARXIV-2601-15394 -->

## 一次 training step 的状态流

最小训练循环是：

```text
data batch [B,T]
-> forward
-> logits [B,T,V]
-> masked cross-entropy
-> backward gradients
-> gradient aggregation / clipping
-> optimizer update
-> scheduler step
-> metrics and checkpoint policy
```

参数更新抽象为：

```text
theta_(s+1) = theta_s - eta_s * update(g_s, optimizer_state_s)
```

`eta_s` 是第 `s` 步 learning rate，`g_s` 是当前或累积梯度。Adam 类 optimizer 还保存梯度的一阶、二阶矩估计，因此训练状态远大于单份权重。

一阶与二阶统计还要声明归一化和时间平滑的先后次序。一条替代分支先估 raw gradient 的 mean 与 residual variance，用它们归一化当前 gradient，再对已归一方向做 momentum；raw-mean buffer 与 normalized-history buffer 是两个状态，不能因共享衰减系数就混为 Adam 的一阶矩。先平滑后归一与先归一后平滑一般不交换，因此改变次序也改变旧统计如何影响当前 update。<!-- source-family:SF-2026-ARXIV-2602-10204 -->

[必要算法与反侧](https://arxiv.org/html/2602.10204v1)只在对称 centered noise、理想条件 mean 等假设下支持其条件 variance 分析，工程 epsilon floor 又与理想零 floor 不同；单步 spike 有界也不授全轨迹稳定，Adam 在相应条件下同样可有界。新增 buffers、归一化和参数搜索要计成本，局部语言模型 loss 区间重叠不证明普遍优越。噪声/统计失准、近零 variance 或质量回归时，保留完整 AdamW 与原 clipping/schedule，不以一个较小 proxy variance 代替训练验收。

第 35 章会说明：若 checkpoint 只保存 `theta` 而不保存 optimizer、scheduler、random state 和 data cursor，通常只能继续做新的 fine-tuning，不能精确恢复原 Pretraining trajectory。

模型结构在训练中扩容时，state contract 还要包含 parameter mapping。简单复制旧单元可以近似保持 forward function，却会把相同 optimizer moments 与 learning-rate schedule 一并复制，导致新单元沿相同梯度轨道形成 symmetry lock。受控扩容需要联合迁移：

```text
old weights + optimizer moments
→ shape-aware parameter mapping
→ activation-scale preservation
→ reset or differentiate new optimizer state
→ asymmetric rewarm for new capacity
→ loss-shock canary and rollback point
```

它用已有训练计算换取延后容量决策，却新增短期 loss shock、parallel-layout migration 与可复现性风险。从头训练在目标形状已知、稳定性优先时仍是清晰基线；“函数近似不变”也不证明 optimizer trajectory 连续。

如果目标是保持已有轨道，而非立即使用新增容量，扩容还存在条件性的等价 continuation 分支。对无 bias 的 MLP 作整数倍宽度复制、按输入复制倍数缩放权重，并联动 SGD learning rate 的输入/输出倍数，可以在相同数据与随机条件下保持函数更新；换成带状态 optimizer 时，迁移还必须匹配 update 的齐次条件。一阶 momentum/exp_avg 随梯度尺度变化，exp_avg_sq 按其平方变化，learning rate、decay 与 epsilon 也要相容。只复制权重或部分 buffers 不构成这份等价合同；条件不满足时，原有 reset、rewarm 与回归 canary 仍合理。

保持对称也意味着重复单元沿同一轨道前进，并未自动使用新容量；按宽度尺度加 noise 是另一个打破对称、允许探索的分支，会重新引入 loss shock。[受限扩容对照](https://arxiv.org/html/2602.10545v1)不能把两种目标合成“无损解锁容量”：窄 MLP/SGD 结论不直接覆盖任意架构，ResNet 的 validation 还存在退步；GPT2 对照的固定扩容后 steps 未计齐 base 训练与 sweep 总成本。mapping、moments、随机/noise revision 和旧训练预算应共同进入恢复与比较合同；轨道失配或质量回归时，回退原 checkpoint、受控 rewarm 或从头训练，而非以较低 training loss 代替最终能力验收。<!-- source-family:SF-2026-ARXIV-2602-10545 -->

### 可复用初始化可以作为预训练约束主动学习

已训 checkpoint 的受控扩容适合已有模型要延后决定容量的场景；若目标 shape 尚不确定且会反复派生，可在预训练时主动学习 transfer interface。一个分支以 `W=ΣT⊗S` 的 Kronecker shared templates 与 size-specific scalers 间接表示权重，用结构化 prefix masks 暴露 depth/width 变化。派生目标先冻结 templates，按 width 截断或重复拼接并初始化 scalers，用少量目标数据适配 scalers，再解除表达约束进入普通训练。此时复用 artifact 是模板及目标重建规则，不是对任意 checkpoint 免费事后分解，也不是零数据迁移或取消目标训练。

主动约束换来多形状复用，却引入表达瓶颈、异构 operator 不兼容与目标重建/校准成本；需要合计预训练、target adaptation 和后续训练，不能用分钟级 scaler 适配代替统一总预算比较。受测 ImageNet、ViT/DiT 与 CNN 初始化不保证任意 LLM 或 operator 的迁移。单一目标已知、模板损害能力或重建不可靠时，从头训练及原 checkpoint mapping/rewarm 路径仍是合理共存与回退方案。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-14769 -->

### Warmstart 是否节省训练，取决于迁移后的 Optimization Gap

从较小 checkpoint 扩容可以复用已有表示，却会改变宽度、深度、参数映射和 optimizer state。只有 warmstart 后到目标 loss 的剩余计算显著小于从头训练，并且扩容没有形成 symmetry lock 或能力回归，才构成真实节省；迁移方法、旧训练预算和新模型最终质量必须一起核算。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13405 -->

受限 scaling 实验不能保证所有架构和规模都受益。目标结构差异过大、迁移后长期停滞或最终质量低于 scratch baseline 时，应回退从头训练，或只复用数据与训练 recipe，而不是继承权重。

### 梯度不存在时，训练必须改写更新接口

反向传播适合几乎处处可微的网络；含离散跳变、硬事件或黑盒算子的模型中，真实梯度可能根本不存在，
继续套用 straight-through estimator 只是引入带偏 proxy。一个条件分支把目标分布与当前输出的差异
写成 optimal-transport 问题，用 forward-only 样本构造参数迁移，并把收敛声明收紧为固定离散分辨率
下的 stationarity。它获得对不可微组件的训练入口，却增加采样、transport 求解和分辨率依赖；可微
近似足够准确或规模化吞吐优先时，标准梯度仍更合适。现有理论与实验只覆盖论文定义的网络和有限
分辨率，不能外推为大模型预训练的通用替代优化器。
<!-- source-family:SF-2026-ARXIV-2605-01928 -->

离散 categorical 变量也可以保留一个可微的采样代理，而不把 hard sample 的导数当真实梯度。对 factorized one-hot 分布加 Gaussian 噪声后，条件 posterior mean 有解析形式；用它驱动有限步 DDIM，得到近似且可微的 transport，再对目标函数求导。这里有三个不同验收对象：posterior denoiser 的闭式计算、有限求解器生成的分布，以及目标梯度估计的偏差；前者精确，不会自动让后两者精确。连续 extension 的选择也会改变梯度代理，即使它们在所有离散顶点上取值相同。<!-- source-family:SF-2026-ARXIV-2601-00781 -->

这个分支把 step grid 与松弛程度加入 estimator identity，每次梯度估计仍只需一次目标函数求值，额外步骤产生的是与该函数无关的 sampler 成本，而非免费更新。在特定 schedule 极限、固定其余 grid 与轨迹极限避开 decision boundary 的前提下，最后时刻趋近零反而使参数 Jacobian 几乎处处趋零；更接近 hard sample 不保证更可用的训练信号。因而应联合比较 bias、variance、目标质量与总成本，保留 straight-through、score-function 或其他已验证松弛；条件不成立或 sampler 成本不值得时回退原估计器，而不是据解析 posterior 宣称通用无偏梯度。

### Gradient Horizon 可以从全局 BP 收缩为受控的 Block-local Objective

全局 backpropagation 让最终 loss 协调所有层，是端到端训练的标准基线；代价是必须保存跨整图 activation，并让深层信用通过完整反向链传播。显存成为首要约束时，可以在 block boundary 增加局部 readout，用局部 objective 与相邻统计训练当前 block，并把 gradient horizon 作为显式配置，而不是把“forward-only”误写成与 BP 等价的优化。

局部目标减少 activation memory，却牺牲跨层协同并引入 label/readout 依赖；不同 block 的 goodness 也未必对应全局任务质量。只在局部 objective、边界 state 和最终 evaluation 都通过时才扩大使用；失配时应增加可反传范围、混合全局 loss 或回退完整 BP。exact-v1 证据限 CNN/VGG、监督分类与作者硬件，不证明该分支可扩展到 Transformer/LLM 预训练、跨设备通信或获得 BP 等价轨迹。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04346 -->

### Dynamic Sparsity 的 Topology Update 也是 Training State Transition

Dense training 或静态 mask 让一组参数持续积累 Adam moments，状态身份简单且恢复路径成熟；dynamic sparse training 周期性 prune / regrow 后，新激活连接没有历史一阶、二阶矩，却若沿用全局 late-training step，首次更新可能远大于成熟参数。此时 loss spike 的 owner 不是 collective，而是 `mask/topology revision + regrowth initialization + local optimizer timestep/moments + learning-rate phase` 这一组训练状态。

一个受限稳定分支是在 regrowth 时重置新参数的 local timestep，并让它们经历独立 linear warm-up；随后再按 density 调整目标 learning rate，以补偿稀疏层有效 fan-in 和 warm-up 带来的保守更新。若目标还包括训练内存，gradient、Adam moments 和 timestep/index metadata 只为 active parameters 保存，并用 block-wise metadata 摊薄索引开销。mask 与 active-index owner 必须和 optimizer-state owner 原子迁移，否则 resume、regrowth 或 checkpoint restore 会把旧 moment 绑到错误连接。

它以 topology/update metadata、稀疏 kernel 适配和局部 schedule 复杂度换取较小的 cold-start spike 与 active-only state；random regrowth、density rule 与 optimizer warm-up 都是需要单独消融的分支，而不是 dynamic sparsity 的通用定理。论文只在 Adam、披露的 LLaMA/C4/OpenWebText、unstructured 与简单 block sparsity 范围内支持该机制，局部 smoothness 分析也不等于全局收敛或实际硬件加速。结构化稀疏未被 kernel 支持、非 Adam optimizer、拓扑变化不值得其控制成本或恢复一致性优先时，应保留 dense training 或静态 sparsity 作为 correctness fallback。

<!-- source-family:SF-2026-ARXIV-2606-00888 -->

稀疏训练还面对另一种约束：optimizer 的连接身份正确，不代表矩阵已经满足硬件支持的物理 pattern。对 FFN 的 forward/backward 六个 GEMM，可以分别选择稀疏 weight 或 activation，而不要求所有算子使用同一稀疏对象。一个受限分支利用 SquaredReLU 的 activation sparsity，将上投影的列离线聚类，再用 token router 和 batch 行重排，让相邻 token 共享可由稀疏 kernel 消费的 pattern；weight 则采用结构化 2:4。这里的列分组、路由和重排拥有执行布局，前述 prune/regrow 与 Adam state 拥有优化轨迹，两者不能用一个 mask revision 混为同一保证。[原始证据](https://arxiv.org/html/2602.06183v1)支持这种 operand 与布局协同，不证明任意自然稀疏 activation 都能直接加速。

训练阶段也不必全程采用同一执行点：dense warmup 后先用 sparse operand 节省候选计算，再留下 dense phase 恢复质量。作者的 LLaMA3-1B/7B、DCLM 与 H200 实验显示恢复预算依模型而变，更激进的 sparse phase 会退步；这不是全任务无损的保证。列聚类、router、packing、行重排以及恢复训练都必须进入总成本，微核测量加 FLOPs/roofline 估算不能替代完整训练墙钟，假定的通信重叠也需另验。pattern 不匹配、布局成本抵消节省或质量恢复不足时，保留 dense training 或已验收的静态稀疏路径，不以预测倍数作发布条件。<!-- source-family:SF-2026-ARXIV-2602-06183 -->

目标若是压缩已有 checkpoint 而非持续 prune/regrow，也可冻结原 θ，只训练组件的确定性非负幅度 mask：forward 用 ReLU(z) 缩放 head/channel 输出，另用退火 retention score s∈[0,1] 估计保留数量，并在后者上施加预算与二值化代价。Forward 幅度可以大于1，不能把它与是否保留的计数混成同一变量；训练后删除零幅度组件、将非零 scale fold进权重，再交 compiler验实际shape/layout。[DDP 的有限对照](https://arxiv.org/html/2603.08065v1)提供这条 mask-only 分支，但有限退火与近似 sparsity不认证每次精确 hard budget，margin separation、阶段求解与STE条件也不授实际全局最优。Dense head/channel 与 MoE expertchannel 的作用域、预算分组、退火/乘子、distillation teacher和最终artifact均须绑定；冻结大权重不使teacher/student双forward免费，也不把规整pattern自动变成kernel收益。Deterministic对照同时改变regularizer/binarization，局部增加mask幅度和KD的收益不授唯一因果或质量无损；更细的layer/expert预算仍可能牺牲质量。全部mask训练、teacher/KD、超参搜索、physical removal/folding、目标backend与独立任务回归均计费；数据、预算或硬layout失配时回dense、较低剪枝或原stochastic mask/恢复训练，由质量与完整runtime验收，不由soft保留数或平均吞吐签发发布。<!-- source-family:SF-2026-ARXIV-2603-08065 -->

### Residual Path 也可以成为随 Depth 与 Time 演化的训练状态

普通 Pre-Norm/Post-Norm 与静态 residual scaling 在第 0 步就决定所有 branch 的参与方式；Learning-rate warmup 则统一控制参数更新幅度。模型更深、更窄或拓扑更敏感时，这两个旋钮未必足以表达“不同深度何时应承担完整变换”。一个实验性分支让 residual branch scale 同时依赖 layer 和 global step：训练早期网络接近 identity，再按明确顺序逐层激活。

```text
layer index + global optimizer step + schedule revision
-> residual scale alpha(layer, step)
-> forward contribution and backward path
-> full branch activation
```

它以延迟深层学习换取早期稳定性，也把 schedule、layer mapping 与 resume step 提升为 checkpoint 语义。恢复到错误 step、改变 layer 编号或没有同步 optimizer state，都会改变实际 training trajectory。过短 schedule 没有隔离效果，过长则可能欠训练深层；浅层优先、等序或反序也不是无关实现细节。

这个分支不会否定 Pre-Norm、受控 Post-Norm、DeepNorm、静态 residual parameterization 或 LR warmup。成熟 recipe、较宽模型和恢复简单性优先时，旧方案仍更合理。长期原则是：**Residual topology 定义可学习路径，schedule 定义路径何时活跃；normalization、initialization、optimizer warmup 与 branch activation 不能互相冒充。**

### 不保留反向图时，更新仍须可复算

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

跨时间 credit 也不一定靠保存展开后的 backward graph。另一条在线分支保留状态对参数的历史影响矩阵，再用本步局部 Jacobian 递推并与即时误差信号相乘；若采用 predictive coding，Jacobian 与误差还在经迭代推断的 hidden state 上求值，而非直接复用 feed-forward 状态。[tPC-RTRL 的受限构造](https://arxiv.org/html/2602.18131v1#S3)把历史影响与当前状态推断分开，不是黑盒零阶估计的直接升级：理想 inference 收敛、预测编码目标与普通 BP 目标的差异，都限定了所谓 exact 的对象；实际近似和推断迭代另需验收。它省去完整时间反向图，却增加 influence state、局部导数与迭代成本，多层扩展也有状态规模压力，不能由在线更新推出低能耗或更快训练。4.3M 参数 LRU、冻结 FastText 的 WikiText-2 和有限翻译对照只支持该条件，预训练词向量曝光、目标与预算差异不被 PPL 吞掉。推断不收敛、影响矩阵过大或质量失败时，BPTT、截断反传与可验证的一阶更新仍合理；确实只能查询 forward score 时，才转向下述零阶分支。<!-- source-family:SF-2026-ARXIV-2602-18131 -->

<!-- source-family:SF-2026-ARXIV-2605-28760 -->

无法或不愿保留 backward graph 时，zeroth-order fine-tuning 可用成对参数扰动的 forward score 估计更新方向；它把训练的主要成本从反向传播转成多次推理。Optimizer owner 仍必须拥有 perturbation seed、objective、direction estimate 与 update commit，推理 runtime 只能作为批量 forward executor，不能因执行请求而取得参数更新权。

这条分支减少 autograd/activation state，却增加估计方差、forward 次数、参数同步和对噪声尺度的敏感性；维度很高或 objective noisy 时可能比反向传播更贵、更不稳定。梯度可得且显存允许时，一阶优化仍是默认；黑盒、低内存或少量可训练参数场景才值得尝试。exact-v1 的系统结果只属于披露模型、任务与硬件，不证明 serving engine 普遍能高效替代训练 runtime。

矩阵参数的零阶估计还可以先选择更新子空间，再决定方向的几何：把扰动限制到低秩投影后的坐标，在那里汇聚有限差分估计、做正交化，然后 lift 回原参数；这不等于先取得全空间 noisy gradient 再套 Muon。[ZO-Muon 的必要方法与对照](https://arxiv.org/html/2602.17155v1)中，单 query 的正交化会丢掉估计的标量幅度，多 query 既改变方向也增加前向数；投影重采样频率同样属于 optimizer state，频繁重采样的反侧不能被固定投影的收益掩盖。所谓 lossless 子空间结论要求真实梯度的 SVD 列空间，并非随机投影的保证。投影、QR/正交近似、rank/query/LR 搜索及前向费用仍在，非矩阵参数另走 MeZO 路径；有限 OPT/Gemma/ViT 任务与不同步数预算不授全面优于一阶方法或实机加速，部分 Gemma 指标仍退步。子空间遗漏、估计方差或搜索成本不合适时，保留普通 MeZO、增加 query 或回到可用的一阶更新。<!-- source-family:SF-2026-ARXIV-2602-17155 -->

若目标本来就可分为独立 expert losses，共享一次 summed loss 会让一个 expert 的 SPSA 估计混入其它 expert 的扰动。改为各自的成对 forward loss，可移除这部分 cross-expert noise；固定平滑可分目标、等大 blocks 和小扰动等假设下，relative variance 可约降至共享估计的 `1/N`。这不是仅把通信状态分片：router、共享表示与参数耦合若仍共同训练，可分性就可能失效。

按数据簇独立训练、冻结共享 head/router 后再 top-k 合并，能获得这种分离，却放弃跨域 jointly learned representation；专家变小还可能降低硬件利用率，大 ensemble 的推理收益也可能耗费更多总训练预算。[SOMA 的 byte-LSTM 对照](https://arxiv.org/html/2609.37899v1)支持独立 loss 的局部降噪，不证明大型耦合 Transformer、稀疏 probes 或所有零阶估计器都满足同一理论比率；seed head 亦有 exact delta-rule，并非全模型纯 ZO。需要联合表征或一阶梯度可得时，保留共享目标/反向传播，不能把分离目标包装成无代价的通用分布式优化。

<!-- source-family:SF-2026-ARXIV-2609-37899; semantic-body-binding:separable-zo-cross-expert-noise-boundary -->

## Optimizer 不是与参数化无关的旋钮

名义 learning rate 也不等于每个样本上的实际移动。一个有条件的诊断把当前 loss 与 proximal surrogate 的最小值之差定义为 stability index `δ = f_current − min(prox-surrogate)`，再在同一参数状态与样本下比较 SGD、Polyak 型步长、归一化更新和 stochastic proximal step。它把 loss model、有效 step 与名义 scale 分开：同点的 index 较小，不表示不同训练轨迹上的最终质量必然更好。非凸时仍可记录这个局部量，但把它转为收敛或 suboptimality 界还需要凸 surrogate 与真实 loss 的全局下模型条件。<!-- source-family:SF-2026-ARXIV-2602-09842 -->

[必要理论与诊断](https://arxiv.org/html/2602.09842v1)中，SPS 还需分账插值常数与 loss lower-bound 的低估误差；NGN 的非负 loss 或凸性本身不保证其平方根 surrogate 是全局下模型。较大的名义步长可在特定归一化/近端结构下产生较小有效移动，却不能据此批准 Adam、momentum 或通用 LLM 配方。ResNet20/CIFAR10 的短训练只提供局部定性反侧，SGD warm-up 也可恢复稳定区；近端子问题求解、index 计算和调参都付费。假设、下界或结构失配时，应保留 tuned SGD/AdamW、warm-up 与现有曲率/质量回归，而不让较低 index 取代 held-out 和完整训练成本验收。

即使 loss 与 validation 接近，表示的几何也未必相同。受限分类训练中，在固定 total weight decay 与 momentum 下改变 coupled/decoupled decay 的分配，会改变类内收拢、类均值结构及 classifier–feature alignment；momentum 对这些量的作用也不只表现为拟合更快。[必要对照与权限](https://arxiv.org/html/2602.16642v1)仅支持 ResNet/VGG、三种图像数据和有限训练网格；训练样本最近类均值判别接近一致，仍可与其他 collapse 指标分离，所以某个几何 proxy 低不能替 held-out quality 签字。固定特征的 SignGD 理论、初始化和步长条件不升级为所有 AdamW 或 LLM 的定律，也不授 NC0 无条件必要性。选择 recipe 时应把 fit、具体几何量和任务质量分账，计入网格调参与诊断成本；不需要该几何目标、条件失配或质量无益时，保留 tuned SGD/AdamW，不能只为更对称的表示改优化器。<!-- source-family:SF-2026-ARXIV-2602-16642 -->

参数化还会改变名义步长的解释：对阶数 `H>2` 的 homogeneous network 与非负 homogeneous loss，单位方向 `v=w/‖w‖` 的有效步长为 `η̃=η‖w‖^(H−2)`。因此保持球面方向步长衰减，可要求名义 η 随训练中的随机范数自适应，而不是独立选择一个固定幂率。[原 SGD stability 分析](https://arxiv.org/html/2602.22936v1)依赖 replacement sampling、球面有界/Lipschitz/近似光滑、沿轨迹高于非零 Bayes loss 下界及训练时长条件；存在一族期望步长的下界，不证明任意 `t^−1/2` 配方或 Transformer CE/AdamW 泛化。另需 PL/strong-growth 的优化结论与未满足其门槛的例子也不借来支持本段。范数观测与调参均有成本，loss/噪声条件失配或质量不稳时，保留 tuned SGD/AdamW、warm-up 与 held-out 回归，球面风险界不替代真实任务验收。<!-- source-family:SF-2026-ARXIV-2602-22936 -->

统一提高更新幅度在各方向压力相近时简单；曲率强烈各向异性时，一条分支从已有 preconditioner/gradient-covariance 提出 sharp 子空间，再在其正交补上提高 drive 与 gradient-damping 系数，而保留 sharp 方向较保守的参数。[LITE v1 §5–6](https://arxiv.org/html/2602.22681v1)的 Muon proxy 与 SOAP eigenspace/soft mask 不是精确 Hessian oracle，有限对照中 uniform 增大系数反而比原 Muon 更差；仅增强 drive 或 damping 也不等联合分支。连续 River/common-eigenbasis 假设不能直接认证 noisy 离散 LLM 更新，较少达到同 loss 的 steps 也不是同 FLOPs/总墙钟。投影近似、阈值、搜索和额外算术付费；方向失配、head敏感或质量反退时，回到原 Muon/SOAP 或已调 AdamW，不把局部谱分配写成所有层都可加速的保证。<!-- source-family:SF-2026-ARXIV-2602-22681 -->

### Optimizer Recipe 也包含数据变换

同名优化器在不同 augmentation、sample mixing、label smoothing 与 gradient spectrum 下并不是同一训练机制。尤其对矩阵型更新，收益可能来自优化器与数据管线共同改变的梯度几何，而非单独的 update rule。可复现 artifact 因此必须绑定 optimizer state、数据变换、loss smoothing 与谱诊断；收益是能解释 recipe portability，代价是实验矩阵扩大。数据分布简单且梯度谱稳定时，较小的 optimizer-only contract 仍可接受。现有比较只约束作者披露的 Muon 配方，不证明某一优化器在所有视觉或语言任务上更优。

<!-- source-family:SF-2026-ARXIV-2605-24770 -->

同样的非独立性也出现在**归一化层与优化器**之间。只在固定优化器下比较 normalizer，或只在固定 normalizer 下比较 optimizer，可能错过二者相乘后的激活饱和：更新规则改变权重增长速度，归一化的非线性若较早进入平坦区，即使 loss 没有崩溃，梯度可用范围和最终质量也会缓慢退化。替换其中任一组件时，训练 owner 应做至少覆盖旧/新两种组合的 matched run，并联合看逐层 activation 分布、饱和比例、weight/update scale、loss 与 held-out quality；不能从一条训练曲线推出每个组件单独的因果收益。联合实验增加预算，调整激活尺度也可能改变原机制；稳定配方可继续用已验证组合，发现饱和时优先回退原 optimizer/normalizer 或做有边界的尺度校准。[一项 1B 参数、1000 步的 3×2 因子实验](https://arxiv.org/pdf/2604.01563v1)支持 Derf 与 Muon 的特定负交互及尺度修复，不证明所有 bounded normalizer、长训或大规模多机模型存在同一失效。<!-- source-family:SF-2026-ARXIV-2604-01563 -->

隐层学习信号也要区分随输入变化的部分与 batch 共享部分。在固定随机反馈把输出误差广播到各层的受限学习规则中，局部外积更新精确包含 covariance 项和 mean teaching×mean activity 项；后者至多 rank one，却可把有界激活推向饱和，削弱输入间变化；若进一步把激活 gate 与输出误差分开，精确式还必须保留 gate–error residual。Readout 拟合先验所需时间又决定这股共享驱动持续多久。忽略 gate–error 相关和上游运动的近似只解释初始阶段，不应成为整个训练或 BP/Transformer 的普遍 collapse 模型。

诊断不能只按 hidden cosine 或参与单元数择 optimizer：特征仍可被独立 reader 解码，幅度缩小却使同一 SGD 读出缓慢；更深 saturation 也可能伴随更快 Adam 学习。减去共享误差、校准 prior 或调整读出时标都须在当前激活、输入均值与 objective 下核验，某些激活中 error centering 反而推高 loss。保留 covariance/方向、信号幅度、任务质量与成本的联合比较，条件失配时回退已验证的普通梯度配方，而不把消除单一 collapse proxy 当训练收益。[必要机制与反例](https://arxiv.org/html/2609.31589v1) <!-- source-family:SF-2026-ARXIV-2609-31589 -->

深度扩展还要求把 **hyperparameter transfer** 与 **feature learning regime** 分开。一个 parameterization 可以让不同 depth 的 activation、gradient 和推荐 learning rate 处于可比较尺度，却仍可能让无限宽极限长期停留在初始化附近；此时 schedule 只是在同一线性化邻域内改变步长，不能凭空恢复跨层 feature learning。

<!-- semantic-body-binding:SF-2025-ARXIV-250501618-COMPLETEP:start -->
更完整的 parameterization contract 同时检查：depth/width 改变后 forward 与 update scale 是否稳定，以及有限训练中 hidden representation 是否实际离开初始化并形成非懒惰特征。前者解决超参数转移，后者决定函数族能否沿训练扩展；二者失败时应先修 initialization、residual scaling 或 parameterization，再讨论 global/layer-wise LR。作者在特定模型形状、recipe 与 Cerebras CS-3 上报告的 12%–34% 只属于该 matched contract，不支持逐层动态 learning rate 的普适方向。成熟参数化在相同深度范围已验证、迁移成本高或 probe 不充分时仍应保留。
<!-- semantic-body-binding:SF-2025-ARXIV-250501618-COMPLETEP:end -->

参数化还要区分“矩阵自身的范数”与 forward 真正使用的尺度。在噪声与 weight decay 主导的受限配置中，前者可能接近平衡，而数据需要的有效尺度并不相同。一条替代分支写成 `W_eff = sW`，或为行列分别引入可学习 multiplier，让矩阵方向与有效尺度分开适应；这不是另一个 learning rate，也不证明所有矩阵都被同一平衡锁死。已有 RMSNorm、attention 或 SSM 内部缩放可能承担部分自由度，应先辨认 placement 与冗余，再决定是否添加参数。

释放尺度又引入新耦合：乘积保持不变的 reciprocal gauge 可让两个因子一大一小，在低精度下失稳；multiplier gradients 若主导 global clip norm，还会连带压小其他矩阵的更新。来源以轻微 decay 和从 norm 统计中排除 multiplier contribution 缓解这些局部问题，不授权所有尺度参数无 decay、永不 clip 或每层统一添加。Falcon-H1-0.5B 的有限预训练及逐配置调参有局部收益，但 LM-head multiplier 和部分任务也退步；额外参数、状态与搜索费用仍在，fold into inference weights 不等总训练免费。保留已验证参数化作为基线，联合检查 forward/update scale、clip group、held-out 质量和完整成本，失配时撤销局部 multiplier，而不是用“可学习”替代稳定性验收。<!-- source-family:SF-2026-ARXIV-2601-04890 -->

同一个函数可以有多组等价参数。例如对低秩分解

```text
W = U V^T
```

任取正交矩阵 `Q`，都有：

```text
(U Q) (V Q)^T = U V^T
```

两组参数表达相同的 `W`，因而在当前 batch 上具有相同 forward、loss 和对 `W` 的函数级梯度；
但这并不保证 optimizer 会走出相同的 `W` trajectory。只有当更新规则对这种 basis change
保持 equivariance，参数更新才会随 `Q` 一起变换，而不会把某个任意的 factor basis 当作额外信号。

这解释了为什么 coordinate-wise preconditioner 不能被视为与模型参数化无关的数值加速器。
Adam 或 RMSProp 分别维护每个坐标的历史尺度；旋转 basis 会重新混合这些坐标，进而改变
preconditioner 和后续路径。相反，普通 Gradient Descent、shared-scalar scaling，或根据
Gram structure 构造的某些更新，可以在相应假设下保留这种对称性。

长期设计结论不是“Adam 错、GD 对”，而是：

```text
training trajectory
= objective + parameterization + initialization
+ optimizer state/update rule + schedule + data order
```

Per-coordinate adaptation 在大规模 Transformer 训练中仍可能因稀疏、异方差梯度与工程成熟度而
合理；保留 parameterization symmetry 也只是某些 implicit-bias 结论可迁移的必要条件，不是更好
generalization 或 low-rank recovery 的充分条件。2026 年一项 matrix-sensing 与小规模 Transformer
研究提供了 basis dependence 的构造性证据，但不能证明 Adam 在一般 LLM Pretraining 中劣于
其他 optimizer。

即使固定参数化，implicit bias 也要说明优化轨迹偏向哪个几何问题，而不是只比较 loss 下降速度。在 smooth homogeneous 的二分类模型、exponential-tail loss 与趋于零但累计时间无穷的 full-batch flow 中，动量更新可在进一步的方向收敛和正 margin 假设下近似相应 norm 的 steepest descent：Muon 对应层矩阵 spectral norm 的最大值，无稳定常数的 Adam 对应参数 l∞ norm，混合更新则由 parameter-group 与学习率配比定义混合 norm。[这一条件分析](https://arxiv.org/html/2602.16340v1)只把极限方向联系到 margin 问题的 KKT 局部驻点，不证明全局最优、泛化优越或方向必然收敛；Adam 另需 ε=0、moment 条件和避免除零的起始梯度假设，Muon 使用精确正交化，非光滑网络还有未验证的 subgradient 条件。生产中的有限步长、随机 mini-batch、AdamW decay、非零 ε 与近似正交化不能直接继承该权限，验证几何还增加对照与长轨迹诊断成本。只有相关假设和实际更新确实匹配，才用 norm 解释轨迹；否则保留成熟 optimizer、实际 held-out 回归和前述状态/schedule 身份，不因一种理想 flow 的 margin 声明替换生产训练方案。<!-- source-family:SF-2026-ARXIV-2602-16340 -->

工程上，使用 factorized weights、structured adapters 或带内部 gauge freedom 的模块时，应把
optimizer、parameter groups、state dtype、initialization 和 schedule 纳入同一实验身份。除训练
loss 外，可以构造保持函数不变的 symmetry twins，检查不同 basis 下的 function-space trajectory、
held-out quality 与 optimizer-state divergence；若差异显著，就不能把参数 basis 当成无关实现细节。

原生低秩预训练还要控制两个 factor **同时更新后的复合移动**，这与上述 basis 对称性是不同的条件。令 `W = A B^T`，`ΔA`、`ΔB` 表示实际参数增量，则 `ΔW = ΔA B^T + A ΔB^T + ΔA ΔB^T`；分别限制 factor 的梯度或名义步长，不会自动限制 `W` 的移动。一个可选分支把两项实际 update 的 spectral norm 都界在 `ρ` 内：`||ΔW||₂ ≤ ρ(||A||₂ + ||B||₂) + ρ²`。只有在 `ρ < 1`、使用真实 factor norms 且两项 update 确实满足该界时，选择 `ρ = η / (||A||₂ + ||B||₂ + 1)` 才足以推出 `||ΔW||₂ ≤ η`。这将局部步幅与当前 factor scale 耦合；它限制的是单次复合参数移动，不是训练收敛、泛化或任意输入的 activation 变化，后者还乘输入范数。<!-- source-family:SF-2026-ARXIV-2602-12429 -->

[必要原生低秩证据](https://arxiv.org/html/2602.12429v1)的实际算法用一次 power iteration 估计 factor norms、五次 Newton–Schulz 近似正交化，因而不能把条件界当成已实现的硬保证：低估 factor norm 或近似 update norm 超出一都会使预算失配。Norm estimation、额外矩阵运算及其 state 要进入 optimizer/checkpoint 身份，同时监测实际 `ΔW`、activation、loss、held-out quality 和完整训练费用；稳定移动也不能补回过小 rank 丢失的容量。近似不可靠时可增加保守校准、显式检查/裁剪复合移动、减小步长，或回退成熟 dense/辅助 full-rank 配方；这些回退仍须各自验证。受测 factor 模型在同 FLOPs 下可有更多 token 暴露，不能由其质量曲线推出同数据收益、所有 dense 训练都稳定，或把算术 FLOPs 节省写成硬件推理 SLO。

另一条实验性分支不是要求 optimizer 对任意 basis 完全不变，而是在每次更新前主动选择更有利的
orthogonal coordinate system：先根据梯度或参数结构估计 rotation，再在旋转空间执行 adaptive update，
最后映射回原参数空间。它试图缓解坐标尺度失衡，但 rotation 本身成为训练状态和计算图的一部分：

```text
gradient / parameter statistics
→ estimate or update orthogonal transform
→ rotate update coordinates
→ apply preconditioned optimizer step
→ inverse map and checkpoint transform state
```

收益与代价必须一起看。更均衡的坐标可能改善特定模型的训练稳定性；额外矩阵运算、通信、transform
初始化、数值误差和跨 world-size checkpoint migration 也会增加。固定 Adam 在其成熟 kernel、状态恢复和
调参经验更重要时仍然合理。作者在有限模型和训练配置上的 loss/benchmark 改善只证明这种 actuator 可行，
不证明某个旋转规则是通用最优 optimizer。

Optimizer state 与 parameter application 也不必总是同一稠密度。Dense Adam 让每个 gradient 同时更新 moments 与
parameters，语义最清楚；实验性 masked-update 路线仍让 dense gradient 进入全部 optimizer state，只随机选择部分
parameter blocks 应用候选 update：

```text
dense gradient
→ dense first/second-moment transition
→ candidate adaptive update
→ block mask and optional alignment damping
→ sparse parameter application
```

若只用 Bernoulli mask 并按保留概率缩放，candidate update 在条件期望上可保持一致；一旦再用 gradient–momentum
alignment 做 damping，就引入了有意 bias。被 mask 的 block 也不是“冻结”：其 moments 已改变，下一步的候选 update
依赖这次 gradient。它可能在特定 heavy-tail/heterogeneous curvature 设置中改变 implicit bias，却没有减少 backward，
也不自动减少 optimizer memory 或通信；mask RNG、block identity、score EMA 与 dense-state/sparse-application 都必须
checkpoint。论文的小模型结果不能证明大规模分布式训练存在 wall-clock 收益，dense update 在实现成熟、景观较均匀或
可复现性优先时仍是基线。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-18999:start -->
归一化 optimizer 还必须把“选择方向”与“选择 step scale”拆开。固定 scale 在几何、训练预算与轨迹半径稳定时仍是
最易复现的基线；这些条件变化后，同一 normalized direction 可能因半径失配而过冲或停滞。一个受限分支保留 Muon
方向作为 proposal，再从已经探索的 trajectory radius、局部下降 certificate，或重新居中的 scalar search 推导
step radius。于是 optimizer owner 不只保存 momentum，还必须把 scale certificate、参数块身份与 checkpoint
transition 一起版本化。

这种自适应半径降低手工 scale sensitivity，却新增 trajectory/certificate state、标量搜索成本和理论假设依赖。
certificate 错误、轨迹爆炸、star-convex 等假设不成立，或搜索成本超过收益时，应回退 tuned fixed-scale Muon、
clipped trust radius 或 AdamW，而不能沿用失效 certificate。现有理论分别受 bounded trajectory、smooth
star-convex、bounded initial sublevel set 与 majorized search 条件约束；实验只覆盖 GPT-124M/WikiText-103、
ViT-Tiny/CIFAR-100 及附录小型配置，不证明大规模或分布式预训练的 wall-clock 优势。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-18999:end -->

归一化方向还要区分理想 sign 与有限数值 map。将每个非零奇值直接变成单位幅度，固定 step 下的小 momentum 不必产生小更新；一个受限分析分支改用 `s/sqrt(s²+ε²)`，让近零奇值的更新逐渐消失。它可写成带正定 preconditioner 的 heavy-ball；ε提供谱下界，却不自动提供轨迹上的上界，更不能由单步有界直接推出全轨迹有界。

相应渐近保证依赖光滑、proper、全局PL、唯一minimum与受限步长/momentum等条件，不能替代普通训练的经验验收；finite Newton–Schulz polynomial与该soft-sign代理也未被证明全局相等。调整数值regularizer会同时改变有效增益和计算路径，有限固定batch诊断中能抑制振荡，不代表正常采样训练、泛化或wall-clock改善。应绑定实际map、regularizer、momentum和schedule做匹配比较，条件失配时保留已验证的Muon/AdamW配方，而不从代理定理签发实现收敛保证。[必要理论与诊断](https://arxiv.org/html/2609.30546v1) <!-- source-family:SF-2026-ARXIV-2609-30546 -->

### 多 Optimizer 组合的次序也是训练状态

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21104:start -->
若一个 step 组合多个 optimizer，更新顺序也会成为训练身份：非交换算子使 `A→B` 与 `B→A` 到达不同参数状态。
HORST 一类 learned composition 可以按局部信号选择顺序，却新增 controller state、额外 probe 与过拟合特定训练段
的风险。作者实验只能支持披露模型与 horizon；顺序收益不能在 matched run 重现时，应回退单一 optimizer 或固定、
可复算的 composition，并把每个子更新与 checkpoint 顺序完整记录。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21104:end -->

### Optimizer State 也必须服从数据与硬件契约

在差分隐私训练中，梯度先经过裁剪与加噪得到 privatized gradient，再进入 temporal filter；过滤后的 DP noise 随后参与 AdamW 的一阶、二阶矩估计。若二阶矩仍直接扣除未经过滤的 DP noise variance，优化器就会错误校正 filter 已经改写的噪声贡献。Filter-aware innovation bias correction 针对这一 filtered-noise contribution 做校准，但依赖过滤器与噪声模型被准确记录；模型失配时，保守的 DP-SGD 或重新校准仍是必要 fallback，而不能因为 loss 下降就假定隐私与收敛同时成立。

<!-- source-family:SF-2026-ARXIV-2605-03425 -->

DP 裁剪之前也有另一层可控压力：conditioning 的少数极端 gain 触发全体 per-example gradient 同比缩小时，未产生尖峰的坐标也会损失更新。一条前向分支先将 condition 投影到 L2 球，再以 tanh 限定 AdaLN shift/scale/gate，后续仍执行原 DP-SGD 裁剪与加噪。[DP-aware AdaLN-Zero v1 §3–4](https://arxiv.org/html/2602.22610v1)的匹配 C/σ 对照中 clipping 频率近似未变，改善主要是尾部严重度而非普遍减少裁剪；两个敏感度上界之比也不是实际敏感度比。它不能代替邻接定义与 privacy accountant，rolling windows 更不自动拥有用户级 DP。前向限幅会丢 conditioning 信息，bound 搜索、训练和独立隐私/质量检查均有费用；条件失配或效用退步时，保留普通 DP-SGD 或重校限幅，不因相同 noise multiplier 签发更强 privacy 保证。<!-- source-family:SF-2026-ARXIV-2602-22610 -->

硬件误差还可能进入更新方向，而不只是梯度的随机噪声：analog in-memory training 的正负 pulse 响应不对称时，器件 symmetry point 不等于 loss 的驻点。先估计并静态零移位在器件稳定、校准预算足够时合理；在线分支则用 analog 辅助状态 `P` 和 digital EMA `Q` 跟踪偏移，让梯度在 `W+γc(P−Q)` 的混合坐标求值，其中 `c` 是翻转符号的 chopper，而不是只在主阵列 `W` 上求梯度。EMA、符号、参考点和周期同步因而属于同一 optimizer state；额外 analog 副本可减少频繁 programming，却增加阵列、读写与同步成本。[受限动态校准对照](https://arxiv.org/html/2602.21321v1)只支持 AIHWKit 模拟中披露的响应/噪声、MNIST 及部分 analog ResNet 设置，各方法调参并不完全相同；pulse 数也不含完整 IO/能耗。强凸、响应与梯度条件下的理论不能迁作任意神经网络收敛证书。器件模型、追踪或质量验收失配时，保留静态校准、原更新或数字训练，不能由更少校准 pulse 直接承诺端到端节能。<!-- source-family:SF-2026-ARXIV-2602-21321 -->

低秩分解也只有映射到硬件支持的执行结构时才会产生真实吞吐。将低秩参数化与 2:4 structured activation sparsity 联合设计，可能同时降低算术与内存成本；代价是稀疏模式、kernel 可用性和精度恢复一起成为训练 artifact 的一部分。没有对应 kernel 或 workload 不能维持结构稀疏时，普通 dense/low-rank 训练仍可能更快。

<!-- source-family:SF-2026-ARXIV-2605-03667 -->

最后，非平稳目标会暴露 optimizer memory 的差异：Adam 的自适应矩帮助快速跟踪，却也会把旧阶段统计带入新阶段；SGD 忘得更快，但在噪声和尺度不均衡时适应较慢。因此 optimizer 选择不是“谁普遍更好”，而是 drift rate、投影约束、阶段边界与状态重置策略的联合决定。[受限证据：arXiv:2605.04269v1]

<!-- source-family:SF-2026-ARXIV-2605-04269 -->

非平稳梯度也可以显式保留一个有限窗口，而非只维护 EMA：保存最近 W 个梯度组成 G，以未中心化的 GGᵀ/W 提议方向尺度，再用带正阻尼的逆算子重加权当前梯度。它不是已识别的 Hessian；低特征值方向只是相对少被压低，当前梯度若已位于窗口 span 中，变换不会凭空产生新方向。Woodbury 将求解移到 W 维系统，仍需 O(dW) 的完整梯度存储、Gram 构造与同步，不能把小系统维度当全部 optimizer memory。[ARROW 的有限 ViT 对照](https://arxiv.org/html/2603.07787v1)只支持已知 task identity 的任务流；诊断流与 disjoint evaluation 分开，AAT 和表示 rank 不替代独立旧任务保持，更新块和阻尼共同变化也不授唯一因果。Window、warm-up、阻尼、作用块与 reset 都进入 optimizer/checkpoint identity，调参、窗口维护和额外求解计费；方向陈旧、噪声放大或保持—质量回归时，保留已验证的 SGD/AdamW、较小更新或 replay，不由低秩名称授无费用或普遍恢复可塑性。<!-- source-family:SF-2026-ARXIV-2603-07787 -->

### Conditional Parameters 需要不同的优化状态

Dense 参数几乎每步都收到梯度，而 routed expert 只在被选中时更新。直接把无状态或当步归一化方法套到 expert matrix，会丢掉条件梯度跨 step 的时间信息；保留 temporal smoothing 能在减少 optimizer state 的同时维持方向稳定。router、dense backbone 与 expert 因而可以采用不同状态配置，但小规模诊断不能证明这种分配普遍优于完整 AdamW，稳定性越界时仍应回退高保真状态。

生成 factorization 也会改变 compute-optimal 配方。Diffusion MoE 的 learning rate、nominal batch、model–data allocation 与 expert pool scaling 不应直接复制自回归经验；应在固定 activated capacity 下重新 sweep objective、optimizer、数据量与 routed capacity。作者单一规模结果只说明存在 Alternative Branch，不证明 Diffusion 或更大 expert pool 总是更优。

#### 生成因子分解改变最优训练配方

把 AR 的 learning rate、batch、model-data ratio 和 expert-pool 配方直接搬给 diffusion MoE，隐含假设两者的梯度噪声、token credit assignment 与 routed capacity 相同；生成因子分解变化后，这个假设不再成立。训练设计应在固定 activated compute 下联合 sweep optimizer、数据预算、batch 与 expert capacity，并报告 Pareto frontier，而不是用单一模型点宣称某范式更优。重新搜索增加训练成本，且结果依赖 tokenizer、数据和目标；缺少足够预算时，沿用已稳定的 AR 或 dense 配方仍是合理基线。
<!-- source-family: arxiv:2608.03457v1; daily: 2026-08-05; semantic-body-binding: objective-specific-compute-optimal-training-recipe -->

#### 条件专家梯度需要保留跨 Step 的时间信号

Dense 参数几乎每步接收更新，routed expert 却只在被选中时产生稀疏、条件化梯度；因此把无状态矩阵归一化直接套到 expert weight，可能把偶发路由尖峰误当稳定方向。减少 optimizer state 时，至少应为 expert gradient 保留跨 step 的一阶 temporal smoothing，并分别观察 router 与 expert 的稳定性。这样能降低 full coordinate-wise state 的内存成本，却引入平滑窗口和冷专家滞后；规模、路由分布或稳定性未覆盖时，应回退 AdamW/dense-style 参考而非宣称普遍替代。
<!-- source-family: arxiv:2608.04407v1; daily: 2026-08-06; semantic-body-binding: routed-expert-gradient-temporal-state -->

### Optimizer State Allocation 也应服从参数角色

Uniform Adam 为每个参数维护同构的一阶、二阶状态，语义清楚、kernel 成熟，在参数统计相近且 memory 可接受时仍是基线。MoE 改变的是参数角色与 activation frequency：dense backbone 持续更新，experts 稀疏且按 routing 命中，router 参数少却直接控制流量。

因而一个实验性分支是按角色分配 optimizer state：backbone 保留 momentum 与 factored variance，experts 只保留 factored variance，router 保留更精确统计；共同的 write-back/rounding contract 仍需一致。它把 optimizer memory 从总参数数目的固定倍数改成结构感知预算，却新增 parameter-group policy、factorization bias、checkpoint migration 和对 gradient sparsity 的依赖。

它与 ZeRO/offload 是正交关系：本章决定保存哪些统计，Ch39 决定这些统计物理放在哪里。现有证据来自单个浅层 MoE、短训练与大多单 seed，不能写成 universal optimizer；结构均匀、factored covariance 假设不成立或恢复简单性优先时，完整 Adam 仍更合理。

降低optimizer辅助state不只是在同一二阶统计上换存储布局，还可改变统计控制的方程。梯度平方的行/列因子通常缩放parameter更新；另一条受限路线用完整momentum的平方行/列统计形成rank-one friction，先阻尼momentum再推进参数，而非把它当作梯度preconditioner。它只压缩friction tensor，完整momentum仍驻留，非矩阵参数也需独立state；因子、数值guard与子更新次序一并属于checkpoint身份。

[低秩friction的受限结果](https://arxiv.org/html/2609.30342v1)在小型语言/视觉任务中支持接近full-friction的质量及更小辅助state，不代表全部训练显存减半或普遍胜Adam。strong-convex连续时间保证与离散随机训练分开，γ=0的经验选择不能继承positive damping的指数率；防零regularizer甚至改变理论渐近幂次。Factor近似、额外elementwise操作和更宽超参数搜索需计入费用，单seed大端点、视觉退步与无端到端计时均保留；先按实际momentum/因子结构和heldout质量做匹配验收，规模或动态假设失配时保留完整AdamW、原factoredvariance与成熟恢复路径。 <!-- source-family:SF-2026-ARXIV-2609-30342 -->

Embedding 的大词表还提供另一种状态压缩边界：全矩阵 Adam 二阶统计保存每个 token、每个维度的尺度；若改用 sign momentum，可以保留完整 `V×d` momentum，仅把额外的幅度控制压成按 column 共享的 `d` 维状态。具体分支先对词表行求每个维度的 mean absolute gradient，再比较瞬时和 EMA 统计与各自 RMS，将两种相对缩放及 1 取最小值，用它阻尼同一维度的 sign step。于是省下的是逐 token 二阶状态，不是所有 optimizer state；一个高幅度维度影响全列，也不等于获得逐 token 自适应。<!-- source-family:SF-2026-ARXIV-2604-07663 -->

这种共享统计以更小状态换取跨 token 混合偏差和稀有 token 被共同阻尼的风险，仍须保存 momentum、统计、parameter-group identity 与 schedule。将每个缩放限制在 `[0,1]` 只保证不放大该 sign step，不证明方向与真实梯度对齐或必然收敛；dense 参数所用更新范数也会改变组合结果。作者有限预训练中，纯 stateless 与纯 sign-adaptive 两条路线都明显退步，embedding/dense 混合才有效，而且一项中等规模结果仍由全参数 Lion 略胜。这支持按角色联合验收尺度与状态预算，不支持普遍替换 AdamW；梯度异质性不能由共享 column 统计刻画、质量回归或恢复复杂性优先时，保留完整逐坐标统计更稳妥。

低 bit moment 还有独立于参数角色的误差边界：state-space rounding 无偏，不保证递推后的 adaptive preconditioner 稳定。二阶状态落在 zero 邻格时，小梯度与分母的非线性可放大下一步更新误差，因此 rounding 可以改在当前 preconditioner space 进行，或以非零 floor 避免零状态。前者可能引入 state bias，后者也改变数值方程；应以真实 update 递推而非 moment 的低失真单独判断。<!-- source-family:SF-2026-ARXIV-2610-12444 -->

[受限 4-bit AdamW 分析](https://arxiv.org/html/2610.12444v1)的 scalar 理论有特定梯度与光滑性前提，不授任意 LLM 收敛；实验又同时涉及 format、rounding、block size 与 LM-head recipe，改善不能唯一归因一项设计。BF16/FP32 master、小至2.7B语言模型的 paired-seed loss-gap 改善不等 loss 下降同百分比，更不等全部训练显存或速度改善。Checkpoint 须保存格式、floor、rounding 和参数组；质量、递推稳定性或恢复失配时，成熟 FP32 moments 仍是基线，物理 offload 则交由 Ch39。

### Whitening 的收益取决于 Gradient Spectrum 所在 Regime

对所有方向做统一 spectral whitening，在 pretraining gradient 较高信噪、需要扩大探索时可能比逐元素更新更有效；跨模态 action module 的低秩梯度或 RLVR 的低 SNR 会改变约束：放大 tail directions 可能同时放大噪声，并破坏先前 head specialization。Optimizer 因而不能只拥有一个“更均匀”的变换，而要让 spectrum estimator、module identity 与 training phase 共同决定是否 whitening、保留高频方向或回退通用 update。

这种 regime-aware policy 用额外 eigenspectrum 估计、阈值和 module-specific state 换稳定性；估计陈旧或 rank/SNR 判错会抑制有用探索。纯 pretraining、gradient spectrum 稳定或缺少可靠 module telemetry 时，统一 baseline 仍更容易复现。`arXiv:2605.19282v1` 的 §3–§5 只支持其 spectral failure analysis、high-pass remedy 及 VLA/RLVR experiments，Appendix M 不证明该策略跨模型、规模与训练阶段普遍成立。

同样的正交化算子，前后接入逐元素 variance modulation 也不是同一更新：先按动量偏差的 EMA variance 调制矩阵，再作 Newton–Schulz 正交化，会改变算子看到的方向；先正交化再逐元素缩放，则改变已输出的几何，二者不能当作可交换的全局 learning-rate 调节。[受限预训练对照](https://arxiv.org/html/2601.14603v1)支持把 modulation order 与 variance state 纳入 optimizer identity，但新增完整 variance buffer、噪声统计与超参数校准；小 batch 的一组配置仍退步，达到目标 loss 所需步数也不等于墙钟或总资源改善。因而应在相同数据、batch、目标质量及预算下验收这一分支；噪声估计失准、额外状态不值得或质量回归时，保留已验证的 Muon/AdamW，而不由局部收敛曲线升级为通用替代。<!-- source-family:SF-2026-ARXIV-2601-14603 -->

预条件化还可以保留矩阵两侧的相关结构，而不只逐元素调制：从历史梯度积累 row/column Gram 统计，周期更新带阻尼的谱基，在变换后的坐标中对动量作双边缩放与近似 polar 更新，再映回原参数空间。若两侧因子固定且正定，可以明确声明加权 operator-norm 的局部线性约束；它不同于二次型的 Frobenius 球，也不表示历史统计等于真实 Hessian。近似正交化、动量、较温和的谱指数和映回后的范数 graft 又改变实际一步，不能将理想线性子问题的最优性转成完整训练下降或稳定保证。

两侧几何增加状态和刷新责任：小谱值的负幂会放大噪声，trace 归一与 damping 控制的是数值尺度，陈旧 basis 和过强校正仍可能失配。逻辑矩阵轴、EMA、阻尼/指数、basis 更新期与 graft 半径应随 optimizer/checkpoint 保存，单侧近似减少的是一份预条件统计与分解，而非整个训练成本减半。[必要方法与直接反侧](https://arxiv.org/html/2603.09697v1)只支持有限小型 GPT-2 预训练中的这条分支；更强谱校正与不控制原空间幅度均有退步，作者 step-to-loss 与局部 timing 也不授通用 Pareto 或免费二阶更新。统计、eigensystem、坐标变换、正交化、搜索和恢复均计费；谱噪声、陈旧几何或质量—成本失配时，保留已验证的 Muon/AdamW、单侧近似或下文更简单的幅度控制，不把新几何静默覆盖成熟基线。<!-- source-family:SF-2026-ARXIV-2603-09697 -->

正交化之后的幅度控制也可以不保存完整逐元素 variance。一条受限分支对 momentum 的全矩阵 Frobenius 范数维护标量一、二阶统计，再缩放正交化方向；scalar 缩放保留该方向的相对几何。另一分支按 column 范数维护向量统计，把截断后的对角尺度右乘在正交化结果上，因而不再保持严格的统一正交几何；这与前一分支的逐元素 modulation order、完整方差 buffer 均不同。[受限 GPT-2 预训练结果](https://arxiv.org/html/2602.17080v1)还同时缩放 weight decay，并为不同方法搜索不同 learning-rate 范围，不能将所有差额唯一归因于尺度统计。Exact-orthogonal 理论所需的 smoothness/无偏噪声条件与有限 Newton–Schulz 实验应分开，有限 val-loss 改善也不是种子不确定性或墙钟收益的证明。Optimizer/checkpoint 须共同标识统计维度、EMA、clamp、矩阵方向、decay 与非矩阵参数的 AdamW；额外统计、正交化、搜索和恢复费用仍存在。Column 异质性或数值 guard 不可靠、几何目标失配或质量—成本不改善时，保留已验证的 Muon/AdamW 或先前 full-variance 分支，而不是把更少状态写成免费且普适的自适应。<!-- source-family:SF-2026-ARXIV-2602-17080 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08933:start -->
Full-matrix Muon 把一个参数矩阵作为统一几何块，在梯度结构相近时最简单；attention heads 的梯度若近似满秩且相互独立，按稳定 head group 分块 whitening 可以提高单位 norm cost 的下降收益。相反，当不同 heads 的更新落在对齐的低秩子空间，过度切分会重复支付范数和正交化成本。分组因此不是无条件加速：optimizer artifact 必须绑定逻辑参数块、grouping revision 和恢复语义，训练 Gate 同时验收 loss trajectory 与稳定性。

分块路径用更多正交化、重排和静态分组漂移换潜在收敛收益；融合张量的物理 layout 也不能反过来偷换数学分组。当前证据只覆盖作者的小模型、数据和 grouping 实验，不证明大规模预训练或其他硬件上的普遍优势。梯度子空间高度对齐、分组诊断不可靠或正交化成为瓶颈时，应回退 full-matrix Muon 或 AdamW。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-08933:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11181:start -->
Matrix-aware update 的价值不能由“精确求解全局几何”这一句话解释。反例显示，随机或反转 singular spectrum 仍可能保留相近收益，因此更可检验的分解应分别观测：更新是否抑制极端 spectrum、与梯度方向的 alignment、给定 norm 下的 descent potential，以及 step size 是否与该几何匹配。Optimizer 名称只标识一套 proposal；training Gate 必须在 matched budget 下比较 update norm、loss trajectory 与 noise regime，不能从 LMO 形式直接推出性能原因。

这项纠错收窄的是因果解释，不是否定所有 matrix-aware optimizer。现有理论和诊断主要依赖 random-feature model，实验只覆盖单一 GPT-2 architecture，不能外推为 Kaon 或其他部署的推荐。若分解指标无法复现、模型结构改变或额外谱诊断成本过高，应回退 matched-budget AdamW/Muon 基线，并把未解释收益保留为经验事实而非全局几何定理。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11181:end -->

<!-- source-family:SF-2026-ARXIV-2605-19282 -->

### Matrix-aware Step 可以与 Sign Step 按成本交替

Muon-style matrix update 保留二维参数块的几何结构，却要支付正交化/矩阵运算成本；sign-based update 便宜、稳定，但丢失部分方向结构。若 workload 同时受迭代成本和几何质量约束，optimizer controller 可以在两类 step 间按固定、可重放 schedule 交替：parameter-block owner 保持同一权重语义，optimizer artifact 记录 step type、state transition 与 checkpoint compatibility。

这里的参数块首先是数学上的 operator 边界，而不一定是 kernel 为吞吐拼成的 fused tensor：把多个 head、Q/K/V 或 gate/up 矩阵合在一起正交化，会改变奇异方向与依形状确定的更新尺度，不能视为单纯等价的布局优化。按声明的逻辑块拆分更新再合回物理布局，需支付重排、分布式重建与块元数据成本；不适合矩阵更新的标量、向量或特定模块仍可使用通用优化器，而不是把所有二维张量交给同一路径。

交替减少平均高成本 step，却引入 schedule、两套 state interaction 与恢复复杂度；比例选择错误可能同时失去 Muon 收益与 sign simplicity。小模型、矩阵开销不显著或结构假设不成立时，单一 AdamW/sign path 仍更合适。`arXiv:2605.19811v1` 的 §3–§5 只支持其 optimizer geometry、alternating spectral/sign descent 与所测 language-model runs，§6 不证明更低平均 iteration cost 等价于跨 workload 更优收敛。

<!-- source-family:SF-2026-ARXIV-2605-19811 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-19619:start -->
另一条分支不是按固定 schedule 交替，而是把 gradient spectrum 当作 proposal sensor：minimum singular-value gap
足够时采用 orthogonalized direction；gap 接近或穿越阈值、其 stability bound 恶化时，切换到 momentum-SGD
direction。这样做以部分 matrix-aware progress 换取条件性的 stability/generalization 保证；optimizer owner 必须
保存 threshold、每步 branch decision、momentum 与 checkpoint identity，不能把混合轨迹伪装成同一 Muon recipe。

条件正交化新增 SVD/Newton-Schulz 成本、threshold calibration、分支抖动和双轨迹恢复复杂度。gap estimate 噪声大、
理论假设无法验证、阈值频繁抖动或 matrix path 没有 wall-clock 收益时，应回退明确版本化的 pure Muon、SGDM 或
AdamW，并保留 matched-budget 比较。exact-v1 的结论只在论文假设下成立，实验也仅覆盖 Qwen3-0.6B/WikiText-103
与 YOLO26m；其 Introduction 有一处与 abstract、Table 1 和定理方向相反的文字错误，不能据此扩大结论。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-19619:end -->

#### Sign Step 的优势取决于范数几何与噪声结构

保留梯度幅度的 SGD/AdamW 是通用基线：当梯度的相对尺度包含有效曲率或置信信息、噪声相关且稠密时，直接丢掉幅度
没有理由更好。SignSGD 则把每个坐标压成方向，只在另一套问题几何下得到不同优势：以 `ell_1` stationarity 衡量进展、
loss 满足 `ell_infinity` smoothness，且噪声近似逐坐标可分并稀疏时，幅度可能主要携带噪声，而 sign 仍能稳定提供方向。
矩阵版本可把相同问题扩到 Muon 一类结构化方向，但这不是“sign optimizer 普遍优于 SGD”的排名。

这条分支把 optimizer selection 从名称选择改成可验证的 contract：训练 artifact 需要记录目标 stationarity norm、
smoothness/noise 假设、参数块身份、实际 update spectrum 与失效诊断。收益是能在特定高维稀疏噪声 regime 中避免让
不可靠幅度支配更新；代价是丢失 magnitude information，并对相关噪声、稠密噪声和错误范数假设非常敏感。假设未被
观测支持、模型结构不匹配或稳定恢复优先时，应继续使用 magnitude-aware optimizer。现有理论结论受其假设约束，
实验也仅覆盖 GPT-2-small 124M、10K steps 的设置，不能外推到生产规模预训练。

<!-- source-family:SF-2026-ARXIV-2605-06615 -->

确定性 sign 便宜，却把不同幅度映成同一方向。一种受限随机分支在逐坐标正包络 `G_i` 覆盖更新幅度 `|v_i|` 时，先加 `G_i·U[-1,1]` 再取 sign，使更新的期望等于 `v_i/G_i`，而不是原梯度无偏。实践中 `v` 可以是 momentum，包络可以由历史 absolute max 构成；这会同时改变预条件几何、状态与方差，zero handling、尺度状态和随机状态也必须进入恢复契约。加噪本身不是收敛保证，理论无 momentum 的投影过程不能与实践 EMA 算法直接等同。<!-- source-family:SF-2026-ARXIV-2604-15416 -->

代价是采样与包络状态、有限步方差及尺度估计依赖。它在粗粒度 FP8 state 实验中可以避开平方梯度先 underflow 的路径，但对照仍保留 BF16 master/nonlinear，AdamW 失败绑定 E5M2 梯度、E4M3 state 和特定 GPT-2 运行，不意味着所有 FP8 AdamW 必然失败。条件不满足、历史包络过于保守或质量/总成本验收无收益时，高精度 state 与 AdamW/SGD 仍是合理回退。[StoSignSGD](https://arxiv.org/html/2604.15416v1)的范数、矩及有界条件和局部实验不构成大模型通用加速或普遍排名。

### 预条件更新还要满足参数可行域

更新方向与范数几何确定后，若参数还须留在半径受限的集合中，先做 adaptive step、再按当前加权度量投影会增加求解成本。另一分支把可行性放入 FTRL 正则化：累积梯度 `m_k` 与由 `δ²I` 初始化的正定统计 `S_k`（`δ>0`），在指定结构空间 `H` 及其诱导范数 `ρ` 下，用 `x_{k+1} = -R [proj_H(out(m_k)) + S_k]^(-1/2) m_k` 直接产生位于 `ρ` 半径 R 球内的迭代点。这里 `out` 是向量外积对应的算子；矩阵参数先按所选算子空间解释，不是对参数矩阵随意做逐元素平方。“免投影”省掉的是昂贵的加权参数可行域投影，结构投影和逆平方根计算仍在。

这种分支以累计状态、矩阵计算和特定范数/正则条件换取可行性及理论 regret 边界；不能仅因初始正则量 δ 在证明中可取很小，就认为有限精度求解仍稳定。加速凸优化还可累计相邻位置的随机梯度差而非单点梯度平方，但每步需要额外梯度查询，依赖凸性、光滑性及噪声条件；非凸分析得到的是 `(γ,ε)` 分布意义的近似驻点：存在均值为输出点的分布，其平均 `ρ` 距离不超过 γ、平均梯度的 `ρ*` 范数不超过 ε。这不保证输出点自身梯度小，更不是全局最优或大模型 loss 的必然下降。`arXiv:2604.02505v1` §2–4 未提供大模型训练吞吐或质量实验。可行域并非真实训练要求、假设不成立或矩阵代价过高时，AdamW/SGD、裁剪或较简单的投影基线仍更合适。<!-- source-family:SF-2026-ARXIV-2604-02505 -->

### Optimizer Update 要尊重参数块的对称性

统一逐元素 optimizer 简单、通用，在参数重参数化不改变功能时却可能给等价模型状态不同更新。embedding、LM head、SwiGLU block 与 MoE router 拥有不同 symmetry group；symmetry-compatible update 要求梯度变换与参数块对称性 equivariant，使 optimizer action 不依赖任意坐标表示。

收益是把架构不变量纳入更新规则；代价是块类型识别、额外矩阵/统计计算和错误 symmetry assumption。没有可靠结构元数据或收益不足时，AdamW 等通用基线仍更稳妥。exact-v1 只在其披露参数块、模型、训练 recipe 与实验中支持结论，不证明一个更新规则跨规模、数据和所有架构普遍更优。

<!-- source-family:SF-2026-ARXIV-2605-18106 -->

### Optimizer 也在选择参数空间中的方向尺度

把所有参数共享一个标量 learning rate，隐含假设是不同更新方向对 loss 的敏感度相近。深层 Transformer
并不满足这个假设：少数主导奇异方向可能对过大步长非常敏感，大量 bulk directions 却仍可承受更积极的
更新。逐参数自适应方法、矩阵正交化更新和统一标量步长因此不是简单的“谁更先进”，而是在估计不同粒度的
可行 update geometry。

loss 与 gradient norm 只能说明“训练正在怎样变化”，不一定能区分表示退化、batch 几何变化与可学习信号不足。把分层 activation covariance 和 per-sample gradient matrix 的奇异谱作为诊断，可观察同一 loss 下 batch size 或深度如何重排有效方向，并在较早阶段提出 token-efficiency 风险；但 spectrum 只是 sensor，不拥有学习率或停止权。它需要额外的 per-sample 统计、SVD 成本与尺度校准，谱形也可能随数据、optimizer、normalization 和 checkpoint 漂移；估计噪声大或训练规模超出校准范围时，应回退 loss、update ratio、held-out quality 与小规模 matched run 的联合基线。exact-v1 只覆盖作者 12/36/48 层受控 NanoGPT 家族及其 early-prediction 实验，不证明谱能跨架构预测最终质量。

<!-- source-family:SF-2026-ARXIV-2605-05683 -->

谱诊断还必须区分随输入与训练阶段变化的 activation transient 和跨 checkpoint 保留的 weight persistent structure。相似的谱形不意味着主导方向相同，更不能把某次 activation 中的方向直接迁移为以后权重剪枝或更新的固定坐标；传感器读数、方向估计与实际干预应分别留存，并用 matched run 检查方向是否仍有效。<!-- source-family:SF-2026-ARXIV-2604-22778 -->

这条分支增加 activation/weight 配对采样、谱分解和方向漂移验证成本。作者设置中的 random-pruning 反例及谱形 warmup 比标准初始化差 42.7% 的结果说明“谱显著”本身不足以授权干预；42.7% 是该设置的表现差额，不是失败率或跨架构常数。方向不稳、统计不足或早期 warmup 尚未形成可靠表示时，继续普通训练并依赖 loss、质量和更新尺度基线更稳妥。

一个实验性分支先用小规模 probe 估计各层更新谱，再把主导方向与 bulk directions 分开分配 step scale：

```text
layer-local gradient/update matrix
→ event-time spectral probe
→ head / bulk sensitivity estimate
→ bounded directional step allocation
→ loss-spike, update-ratio and downstream checks
```

它解决的是统一步长在不同谱方向上的过保守或过激，不是证明每层都应有独立、持续变化的 learning rate。
收益需要用相同 token budget、batch、precision、warmup、clipping 与 optimizer state 做 matched comparison；新增代价是
probe 成本、谱估计噪声、层间尺度漂移与更多控制状态。模型规模、数据分布或训练阶段改变后，旧谱先验必须重估；
当训练稳定、可观测性不足或控制复杂度超过收益时，统一 schedule 仍是更可靠的 baseline。

### Optimizer 的不变量必须匹配参数块角色

Adam 或 Muon 的 additive update 同时改变矩阵方向与 singular spectrum；若某些参数块的谱应保持，左右 orthogonal transformation 可以只优化几何方向而固定谱。optimizer 只拥有坐标变换 proposal，training objective 和 held-out evidence 决定这个 invariant 是否仍合理。固定谱可提高受限训练稳定性，却增加矩阵变换成本，并可能禁止任务真正需要的 spectrum adaptation；数值近似也会破坏严格正交。出现瓶颈时应回退 AdamW、Muon 或混合 optimizer，按参数角色、梯度谱和 loss trajectory 决策。exact-v1 不证明固定谱普遍最优、超大模型效率或更好泛化。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12492 -->

固定全部 singular spectrum 比只约束最大增益更强。若目标是让 weight 和每步 update 的谱尺度都满足宽度参数化要求，初始化时的缩放并不能自动保证整个训练时间轴。一个更窄的约束分支保留权重唯一最大奇异值 `S` 及方向 `u₁,v₁`，把更新限制到两侧正交补：`u₁ᵀΔ=0, Δv₁=0, ||Δ||₂≤1`。对 `W_new=W−ηSΔ`，只有在非负步长满足 `ηS≤S−σ₂(W)` 时，原最大方向保持且其余方向不能超过 S；这允许其他奇异值变化，不是前述固定全谱变换，也不单凭谱尺度证明 feature learning 或超参数转移。<!-- source-family:SF-2026-ARXIV-2601-01306 -->

该分支增加主奇异方向估计、投影和矩阵更新成本；方向估计及有限数值运算也须核验是否真满足约束。超宽或近简并矩阵的谱隙可能很小，使允许步长过于保守；再把更新后权重直接 rescale 回半径 S 虽可控制 weight norm，却同时改变实际净更新，不能继承“weight 与 update 双约束始终满足”的保证。应分别记录 width、谱隙、步长、估计精度和是否进入 rescale 分支，以实际 loss、更新尺度与 held-out transfer 验收。条件失配或约束阻碍所需表示变化时，保留较简单的 Muon/AdamW、显式归一化与邻近规模调参，而非从参数化公式签发免调参保证。

另一条约束分支只要求瞬时更新沿谱范数球面切向：最大奇异值唯一、该处可微时，用主方向形成法向 `Θ=u₁v₁ᵀ`，再对 `msign(M+λΘ)` 求标量根，使其与 Θ 的 Frobenius 内积为零。这是[一阶切向约束](https://arxiv.org/html/2601.08393v1)，不是上面双侧正交补加谱隙条件的有限步 exact invariant；有限 additive step 后仍需径向校正。作者实现把校正安排在下一步更新之前，不能由这种安排授予每一中间时刻或更新后权重都严格在球面上。<!-- source-family:SF-2026-ARXIV-2601-08393 -->

主方向估计、matrix-sign 近似和求根容差又把解析切向变成数值近似；近简并谱、根求解或校正误差需要随矩阵形状与 precision 检查。该分支用额外计算换取方向选择：在作者 B200 的有限 dense 模型配置中，优化实现仍比 Muon 单步更慢，较少训练步数不直接等于较少墙钟时间；只径向校正的 MuonSphere 是更便宜的对照，局部部分质量指标也不逊于完整求根。应把更新、校正、总成本与 held-out 质量分账；约束无净收益或数值不可靠时，保留 MuonSphere、Muon/AdamW 和匹配预算调参，而不宣称谱约束普遍稳定或免 weight decay。

### Architecture 变化后，Maximal-update Scaling 也必须重推

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15290:start -->
把 MHA 改成 GQA 后继续沿用满秩矩阵假设与旧学习率，最容易维持工程连续性，却可能把 head repetition、非满秩投影和深度变化产生的尺度偏移误判为架构收益。一个更严格的参数化先用适配非满秩权重的 modified spectral norm 描述有效 operator scale，再据此导出 GQA repetition、depth 与 weight-decay 的 maximal-update scaling。参数化 owner 只给出可迁移的初始化/学习率 proposal，真实训练曲线仍拥有验收权。

这提高小规模到目标规模 transfer 的可解释性，却依赖模型形状、coordinate checks 与推导假设；公式错误会表现为 activation/update scale 漂移，而不是立即报错。exact-v1 只支持 §3 推导、§4 与 Appendix B 的所测形状，且 Appendix B.2 已给出某类 coordinate check 的失败边界。架构超出校准域、rank 假设不成立或训练信号冲突时，应回退邻近规模 sweep，而不是把 μP 公式当作免调参保证。<!-- source-family:SF-2026-ARXIV-2605-15290 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15290:end -->

## Batch、tokens 与 optimizer steps 不是同一计量

设每个 optimizer step 的 global batch 为 `B_global`，有效平均 sequence tokens 为 `T_eff`：

```text
tokens_per_step ~= B_global * T_eff
N ~= steps * tokens_per_step
```

若存在 padding、packing、loss mask 或变长 sequences，`T_eff` 应按实际参与 loss 的 token 数计算，而不是配置中的 `T_max`。

增大 batch 可以提高矩阵规模和并行效率，也会减少固定 token budget 下的 optimizer steps，并改变梯度噪声与 learning-rate 选择。Gradient accumulation 可以在不一次放入全部 samples 的情况下形成更大 effective batch，但不能消除多次 forward/backward 的计算。

从本章开始，Part IV 统一使用 `B_micro` 表示每个 data-parallel rank
一次 forward/backward 接收的 micro-batch，使用
`gradient_accumulation_steps` 和 `data_parallel_degree` 表示另外两个乘数。
张量 shape 中的 `B` 仍表示当前实际输入张量的 batch 维度。完整关系在第
36 章展开：

```text
B_global = B_micro * gradient_accumulation_steps * data_parallel_degree
```

硬件实际执行的 batch 与优化过程对应的时间尺度，还可以在受控范围内分开选择；这不是把 micro-batch 改名为 effective batch。一条 SDE 近似分支同时重参数化 AdamW 的 learning rate、两个 beta 与 epsilon，让不同 physical global batch 对应某个 virtual batch/steps 过程；固定 token horizon 下，两者仍服从 tokens=sequence length×virtual batch×virtual steps。[受限 masked-diffusion sweep](https://arxiv.org/html/2602.21472v1)只在经 loss 校准的 critical batch 以内支持这种近似，超过临界仍会因离散化步数不足退化。模型、token horizon、schedule 或 optimizer 变化必须重验，不能把一个 fitted drift–horizon 系数升级成通用规律，也不能用 exp(ELBO) 等同生成质量。提高每设备 batch 可以减少小 batch 的闲置、改善利用率；增加节点以缩短墙钟则可能付出通信和较低 FLOP 效率，超过 critical batch 才是前述离散化退化边界；pilot 搜索、配套 optimizer state 和 tokenizer 费用亦不消失。近似/质量或集群预算失配时，保留普通固定 recipe 与 accumulation，并以相同数据/质量目标比较更新及总成本，不由相同 token 数宣称 trajectory 等价。<!-- source-family:SF-2026-ARXIV-2602-21472 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21573:start -->
训练效率也不能只用单步 FLOPs 或模型大小表示。每一步消费多少计算、batch 中有多少可用监督信息，以及达到同一质量目标需要多少步，三者共同决定 quality-per-update。对 text-to-image 训练，稠密 caption、混合分辨率与宽高比 packing、文本/图像表示选择可以同时改变这一分母；更小的单步成本若需要更多低信息 update，并不一定更高效。

这种联合设计以 caption 生成、异构样本 packing、预处理和更强 encoder/VAE 成本换取收敛效率，也很难从组件 bundle 中识别单项因果贡献。现有 exact-v1 只支持作者披露的模型、数据和比较基线；其计算比例不能外推为通用配方。若 matched-budget 收敛未改善，应回退较简单的数据与架构 recipe，并用受控 ablation 分别测量每个组件。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21573:end -->

### 多模态大 Batch 的方差冲突需要进入 Optimizer State

<!-- semantic-body-binding:SF-2026-ARXIV-2605-16165:start -->
统一 next-token objective 在模态梯度方向相近、batch 较小时可以共用一个优化器统计；大 batch 下，文本与视觉梯度的方差和曲率可能竞争，简单累积会让一方的噪声尺度主导更新。ML-FOP-SOAP 先用 Fisher/曲率近似投影冲突分量，再通过 hierarchical folding 聚合 gradient-accumulation micro-steps，使模态方差校正成为显式 optimizer state，而不是藏在全局 learning rate 中。

projection 只拥有更新方向 proposal，训练 loss、held-out capability 与稳定性 gate 才能提交新 checkpoint。该分支付出 Fisher 与 tensor-preconditioner 近似、额外状态和 folding 误差；模态分布变化时，旧统计也会过期。exact-v1 只支持 §3.1–3.5、Janus/Emu3 与作者 batch/实验，不证明所有多模态模型都受同一冲突支配。小 batch、单模态主导、曲率估计不稳或额外成本超过收益时，应回退标准累积、per-block clipping 或已验证的 first-order optimizer。<!-- source-family:SF-2026-ARXIV-2605-16165 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-16165:end -->

投影能减少梯度方向冲突，仍不等于冲突量已被校准为任务取舍的诊断器。应先固定 probe、任务人口与训练 identity，把训练早期量预测最终双任务能力和同一 checkpoint 的相关分开；同 run 多个 checkpoint 不能当独立重复。再核操作是否确实改变所声明 proxy，并单独观察 held-out 双轴，而不是把 proxy 下降当 checkpoint 质量通过。生成失败可能主导 norm ratio 的相关，限制到已掌握生成的配置后，这个量的含义会改变；自洽输出也可能只是坍缩后的简单世界。

GridUMM 的受限共享 decoder 审计中，干预后方向冲突下降、任务均值仍在 seed 噪声内变化，说明该 proxy 并不自动承载所测任务的改善方向；projection 还改变 norm，raw 梯度会重新适应，不能据此宣布所有功能冲突或优化器机制无效。合成 grammar、生成较早饱和、有限三 seed 与 method 简化都限制外推，生产模型须重做 proxy–outcome 校准。固定 probe、额外 backward、干预 sweep 和独立任务评价付费；无法证明有效性时保留成熟 joint training 或已验收 optimizer，以 held-out 能力/成本与稳定性验收，不由低冲突自签收益。[必要机制与反证](https://arxiv.org/html/2609.38465v1)。<!-- source-family:SF-2026-ARXIV-2609-38465 -->

在线串流没有可重排 batch 时，连续样本的强相关会让短时更新重复同一方向；辅助预测又可能与 RL 目标竞争。一个受限分支用时间平滑的梯度方向提出正交补更新，再把辅助目标经过其 optimizer 得到的实际 update 投影到 RL 实际 update 的正交空间；两个投影分别约束历史重复与跨目标作用，不能只投影 raw 辅助 gradient 后就假定带状态 optimizer 仍相容。小的连续轨迹 window 与 momentum 仍是保存状态，不是零 memory 或全 IID。[所测 streaming RL 对照](https://arxiv.org/html/2602.09396v1)有 Atari 任务退步，raw-EMA 文字与 projected-history 算法不一致，不继承精确配方或 IID 保证；额外 gradient、历史与 projection 费用也未让 CPU 普遍更快。相关性、辅助目标支持或 optimizer 身份失配，下游质量退步时，保留普通 joint optimizer、原 online learner 与独立能力回归，不把低冲突 proxy 授成收益。<!-- source-family:SF-2026-ARXIV-2602-09396 -->

### 聚合梯度与逐样本残差是不同的更新坐标

SGD 从 batch 的总 loss 得到一个更新方向，最容易并行；若要在同一步分别改善各样本残差，同一个聚合梯度却不足以恢复全部逐样本条件。局部线性化提供另一分支：记残差向量为 `r`，其对 `P` 个参数的 Jacobian 为 `M ∈ R^(B×P)`，在近似 `r_new ≈ r + M Δθ` 内，用 `Δθ = -η M⁺r` 求最小二乘、最小范数更新。过参数化时，直接处理 `B×P` 矩阵可以避开参数平方的完整度量矩阵；截断 SVD 的 rank 与相对奇异值阈值则同时控制保留方向、放大误差和求解成本。这不是 Muon 对参数梯度矩阵做极分解的同义写法。<!-- source-family:SF-2026-ARXIV-2604-01279 -->

代价从大度量矩阵转向逐样本 Jacobian 的内存与谱求解，局部近似也要求 step 不能越过有效区域；截掉方向可能丢掉必要条件，保留很小的奇异值又会放大噪声。一般非负 loss 转为有效残差时，幂指数 κ 会改变更新语义，不能把平方残差的推导直接当作任意 cross-entropy 的精确自然梯度保证。小型回归/分类实验尚未证明大模型预训练收益；把多个样本聚成粗条件可省内存，却逐渐回到聚合梯度，参数分批的理想节省也未在通用 autograd 中验证。大规模稳定训练仍可采用 AdamW/SGD，只有残差结构与质量、时间、显存联合对照支持时才启用此分支。

这种局部坐标还会随参数更新而变化，所以加入动量时必须说明保留的是参数位移还是函数变化。普通 parameter momentum 直接沿用旧参数方向，在局部几何变化缓慢时简单合理；函数空间分支先用旧 tangent 表示上一步函数 momentum，再以当前与旧 tangent 的 cross-Gram 将其投影到当前 tangent，用当前 Gram 的逆或伪逆求回参数坐标，最后合并当前自然梯度更新。这是对历史方向的重新表示，不是直接给参数动量换名称，也不是精确无误差的全局几何保证。<!-- source-family:SF-2026-ARXIV-2604-15554 -->

显式 cross-Gram 增加旧导数状态、矩阵估计与谱求解成本；有限差分可以用两次 forward 的函数差近似旧函数方向、避免保存完整旧 Jacobian，而直接复用参数动量仅在两步 tangent 映射近似恒等时合理。小型回归/分类对照中的迭代减少不等 wall-clock 同比改善，近似版本有更慢和发散反例；截断、regularization、步长与动量系数都影响稳定。若估计噪声、显存或额外计算抵消收益，应回退无动量 NGD 或稳定的 AdamW/SGD；现有证据不证明大模型随机 minibatch 训练加速。

局部 Jacobian 不一定要解完整的逐样本逆问题。在线更新若已选定 SGD 或 RMSProp 方向，可以先规定某个输出——例如当前采样动作的 log-prob——希望改变多少，再用该方向上的局部导数估计一个标量步长；普通 learning rate 管参数位移，这个分支试图管输出变化的单位。带 eligibility trace 时，目标还涉及衰减历史的输出变化，不能把它当作当前单样本残差。它只给既定方向定局部尺度，不修正方向本身，也不是前述 batch 伪逆的廉价等价物。<!-- source-family:SF-2026-ARXIV-2604-19033 -->

这项选择适用于受测 streaming RL 的条件讨论，而不是大模型预训练的默认 optimizer：方向导数接近零会使步长不稳，action-dependent 缩放可能改变期望更新方向，局部线性式也会在较大步长或漂移的 trace 上失准。典型 log-prob 变化不构成 hard KL cap、无偏 policy gradient 或安全保证；额外导数与 trace 状态也要计入成本。无法稳定校准输出单位时，回退常规 AdamW/SGD 与独立行为评估。

### Preconditioner 与 Gradient 共享 Batch 时会改变估计语义

用同一 minibatch 同时估计 gradient 与 curvature/preconditioner，状态简单、吞吐高，在 batch 足够大且预条件变化平缓时仍合理；但二者的统计耦合会产生 coupling bias，而 inverse/root 等非线性即使输入估计无偏也会产生 inversion bias。Cross-fit 把两类估计分到独立 microbatch，variance correction 再校正非线性偏差，因此 data cursor、microbatch identity、preconditioner revision 与 correction state 都要进入 optimizer/checkpoint 账本。

收益是更清楚的估计边界，代价是额外样本、内存、同步与估计方差；小模型或一阶优化已经稳定时，普通同批估计仍更简单。`arXiv:2605.20756v1` 的 §5、§7.1、Appendix A 与 §6–§7 实验只支持其估计器；§8–§9、Appendix C 不证明校正对所有矩阵预条件器或大模型都带来净收益。

<!-- source-family:SF-2026-ARXIV-2605-20756 -->

### Effective Learning Rate 是第一层坐标，不是完整控制器

Nominal learning rate 相同但参数范数不同，实际相对更新尺度仍可能不同；许多 schedule/norm-control 组合可先用 `ELR = LR / ||theta||` 描述 loss dynamics。它提供一个比裸 LR 更可比较的全局坐标，却不能取代 layer/group-specific gradient geometry、optimizer state 与时间尺度：ELR 相同仍可能在不同方向、精度或条件参数上产生不同更新。实践上先监控全局与分组 ELR，再在梯度 SNR、trust ratio 或稳定性证据支持时细化。`arXiv:2608.24814v1` 的 optimizer、architecture、dataset、scale 与 norm-control ablation 支持部分 trajectory collapse，不证明单一标量是所有层的充分状态。

<!-- source-family:SF-2026-ARXIV-2608-24814 -->

## Learning-rate schedule 为什么决定训练轨迹

固定过大的 learning rate 可能让 loss 发散，过小则浪费计算。大模型训练常使用 warmup 后 decay 的 schedule：

```text
warmup -> peak learning rate -> decay
```

Warmup 让 optimizer states 和 activation scale 在早期逐步建立；decay 则在后期降低更新幅度。具体 schedule 不是普适定律，必须与 optimizer、batch、模型规模和 token budget 一起解释。

Schedule 还没有独自定义训练最终交付的权重：直接返回最后一步，或在训练结束将该点与近期 checkpoint 均值插值，是不同的 estimator。终态 shrinkage averaging 只改变返回 artifact，不反向改变已经执行的 optimizer 轨迹；局部 PSD 二次模型中的 lag 与噪声协方差说明为什么 cooldown 与插值系数可能交互，不能推出任意非凸训练的通用最优系数。因此同一数据顺序和预算下应同时比较 schedule × returned estimator，而非把终态平均的收益都算给学习率。

这个选择增加 checkpoint 保存、间隔/窗口/系数搜索与组合权重的验收成本，部署组合也不等于可原样恢复 optimizer state。[TSA 的受限预训练对照](https://arxiv.org/html/2609.25482v1)含小规模配对 seed 与 AdamW 检查，较深模型的 combined recipe、少量 CORE 合格结果并未隔离所有配方或运行吞吐差异；不支持普适训练加速和统一最优系数。预算不足、checkpoint 不兼容或组合验证失败时，raw endpoint 与常规 decay 仍合理；恢复状态完整性继续由第 35 章负责。<!-- source-family:SF-2026-ARXIV-2609-25482 -->

预训练的收敛目标与后续适配性还可能对同一 schedule 提出不同要求。选择 base checkpoint 时，不能只比较预训练 loss，再假设相同 SFT loss 表示保留了相同能力：在受控的 1B 级微调实验中，较大 SFT learning rate 可以在达到近似相同任务 loss 时产生更大的参数漂移和更差的分布外表现；另一些预训练 checkpoint 的 cooldown 与参数扰动后的输出 KL 敏感性同时上升。前者是适配更新尺度的对照，后者只是 checkpoint 轨迹上的相关证据，输出 KL 也是 sharpness proxy，不是完整 Hessian。不能将二者连成“预训练 decay 必然造成遗忘”的因果链。<!-- source-family:SF-2026-ARXIV-2604-13627 -->

因此可把 **base checkpoint × SFT update scale** 作为联合验收坐标：在可比任务预算下记录参数漂移、任务拟合与 held-out retention，再决定用哪一阶段的 checkpoint 及多小的适配更新；第 29 章承接监督轨迹和遗忘验证。这个试验矩阵增加微调与评估成本，扰动指标也随模型和任务变化；作者主要 1B–3B 实验尚未重训不同 annealing 来建立预训练因果，也不足以普遍取消 decay。预训练收敛优先、后训练不敏感或缺少可靠迁移对照时，原有 warmup–decay 与保守 SFT learning rate 仍是合理基线。

同一联合验收还可以把 pretraining weight decay 作为独立控制轴，而不是只挑 base perplexity 最低的模型。在架构、数据、token-per-parameter 预算与其余训练配置固定时扫描 decay，再用固定的 SFT 配方比较后续任务，能够检验“拟合当前分布”与“容易适配新任务”是否偏好同一配置。[受限语言模型对照](https://arxiv.org/html/2602.11137v1)中，两种目标的最优点确实可以不同；这支持分开选择目标，不支持统一增大 decay，或把不同模型、预算与数据源的曲线合成一个塑性定律。

这个控制轴增加预训练候选、微调与评估成本，也可能先损害 base quality。部分基线复用旧训练，少量配置的相关系数对移除一个点敏感，表示 rank 或可分性诊断不提供唯一因果解释；固定 SFT epoch 更不等于所有任务 token/FLOPs 相同。因而要绑定 decay、训练预算、checkpoint 与 SFT 评价协议，并保留完整质量与搜索费用；base 收敛优先、下游目标不稳定或预算不足时，成熟固定 decay 与保守适配仍合理。第 29 章继续负责监督人口、遗忘与迁移验收。<!-- source-family:SF-2026-ARXIV-2602-11137 -->

Gradient clipping 通过限制 gradient norm 缓解极端 update：

```text
g <- g * min(1, max_norm / ||g||)
```

它可以避免单次异常梯度破坏训练，却也可能隐藏数据异常、数值 overflow 或不合适的 learning rate。平台应同时观测 unclipped norm、clipping frequency 和 loss behavior。

<!-- june29-owner:TRAIN-PRETRAINING:start -->
### 换规模时，学习率外推也需要适用域

在相近架构和预算内复用学习率配方，可以减少昂贵的 sweep；但 width、depth、token budget 与 schedule 同时变化后，裸 learning rate 不再代表相同的更新行为。将这些变化压成一条幂律，可能把局部拟合误当成跨尺度规律。一个补充诊断是比较相邻 step 的归一化权重位移 `||ŵ(t+1) - ŵ(t)||`：它描述实际方向变化，不等同于前面作为控制坐标的 `LR / ||theta||`，也不能忽略 optimizer state。

因此外推配方应连同模型形状、训练数据量、optimizer 与 schedule 一起保存，并在目标尺度附近留出校准预算。受限实验中，最优裸 LR 的 log-linear 关系出现曲率，effective-update 与 data-axis 外推在部分设置更稳定；这没有证明一个通用迁移公式。证据限 GPT-2-style 22M–707M、FineWeb 5B–100B tokens、WSD 与 AdamW/AdamH。更复杂的测量和局部 sweep 增加成本，超出已测域时应重新校准，而不是沿拟合曲线盲推；配方与尺度基本不变时，既有 warmup–decay 仍是简单基线。<!-- source-family:SF-2026-ARXIV-2606-29158 -->
<!-- june29-owner:TRAIN-PRETRAINING:end -->

### 不知道训练终点时，Schedule 不能依赖准确 Horizon

Cosine decay 在总 token budget 预先冻结时简单有效；持续训练、资源波动或数据增量让终点变化后，schedule 会因错误 horizon 过早衰减或在续训时产生不连续。horizon-free 分支让当前 step size 由已观察训练状态和预定义无终点规律决定，使停止点变化不必重写完整轨迹。

代价是少了“临近确定终点主动收敛”的先验，噪声、warmup 与 weight decay 仍需联合调节；它也不保证在任意 budget 上优于 tuned cosine。固定预算、可重复大训练继续适合 horizon-aware schedule，开放式 continual pretraining 才更需要该分支。

<!-- source-family:SF-2026-ARXIV-2607-10959 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-19095:start -->
horizon-free 也不能只删除 decay schedule。当训练可随时停止且 batch 规模改变 gradient norm 时，schedule-free 分支需要把 interpolation、averaged iterate、weight decay 与 adaptive step 一起纳入 optimizer identity；checkpoint 必须保存这些不可由当前权重重算的状态。它获得的是较平滑的 anytime trajectory，而不是“无需调度器”的普适最优性。

代价是平均轨迹、norm weighting 与 checkpoint selection 更复杂，并可能在短 run 或验证域外规模上劣于明确退火。总预算稳定、最终 tail 已知时，WSD、cosine 或显式 tail averaging 仍更容易复现。论文的相对收益只绑定其模型、token/parameter ratio 和披露配置，不能外推到任意架构、数据、硬件或训练预算。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-19095:end -->

### Dropout Schedule 也是 Training State

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21648:start -->
固定 dropout 在所有阶段施加相同扰动，简单且易复现；但早期表示形成与后期收敛面对的 noise budget 不同。把 dropout rate 纳入 training state，允许前期较强正则、后期降低优化噪声，不过 schedule revision、当前 step 与恢复位置也必须进入 checkpoint identity，不能只保存一个最终 rate。

时变 schedule 增加调参和恢复状态，已有收益又受 mean-field edge-of-chaos 假设及作者 MLP/ViT 实验约束，并未证明同一 optimum 能迁移到 LLM 预训练。激活类别、架构或 matched-budget 验证不成立时，常量 dropout 或 no-dropout 仍是更稳妥的基线。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21648:end -->

### 每层是否需要不同或动态的 Learning Rate

先把“这一层实际更新了多少”写清楚。对第 `l` 个 parameter group，可抽象为：

```text
Delta_theta_l(s)
= - eta_global(s)
  * m_l(s)
  * P_l(optimizer_state_s, g_l)
```

- `eta_global(s)` 是全局 warmup / peak / decay schedule。
- `m_l(s)` 是可选的 layer/group multiplier；可以固定，也可以随 step 变化。
- `P_l(...)` 是 optimizer 根据 gradient 与 moments 产生的 preconditioned update。Adam 的 coordinate-wise adaptation
  已经让不同参数获得不同 effective step，但它不等于显式的 layer-wise learning rate。

所以“每层用同一个 learning rate”通常只是指共享 `eta_global`；真实 `Delta_theta` 早已因 gradient、Adam moments、
parameter norm、weight decay 和 clipping 而不同。是否再增加 `m_l(s)`，应由 update evidence 决定，而不是看到深度
增加就默认启用。

#### 四种经常被混淆的策略

**Global schedule。** 所有 groups 共享 warmup 与 decay，最易复现，也让 update 的时间边界一致。它在标准
Pretraining recipe、架构/初始化已稳定时通常是首选。

**Optimizer adaptation。** Adam 用一阶、二阶 moments 按坐标缩放 update，主要应对 noisy、sparse 或异方差
gradient；它不会恢复在 backward path 中已经消失的信号，也不保证各层 update-to-weight ratio 合理。

**Layer-wise / parameter-group multiplier。** Fine-tuning 中可以让靠近输入的 pretrained layers 使用较小 multiplier，
让新 task head 或上层更快适应；ULMFiT 的 discriminative fine-tuning 是这类思想的早期实例。它的理由是保留可迁移
表示并减轻 catastrophic forgetting，不是“低层梯度天然更容易爆炸”。在从零 Pretraining 中，不存在脱离架构和
数据的通用“越深 learning rate 越大/越小”规律。

**Layer-wise trust ratio。** LARS/LAMB 根据 parameter norm 与候选 update norm 形成 group/tensor-level ratio，最初用于
large-batch training 的尺度失衡。LARS 在其 CNN workload 有效，但 LAMB 论文也明确指出 LARS 在 BERT 等 Attention
模型上并不一致；这正说明 layer-wise adaptation 是 optimizer/workload branch，不是普适深度修复。

另外，第 17 章的 residual scale、gate、DeepNorm，以及本章前述 `alpha(layer, step)` progressive residual warmup，
改变的是 forward contribution 与 backward path。它们即使也依赖 layer 和 step，也不能被称为 per-layer learning rate。

#### 哪些情况下值得引入 `m_l(s)`

至少出现以下一种可重复证据时，才值得进入实验：

- Fine-tuning 中底层出现 collateral drift，而上层/新 head 明显欠适配。
- 新增或扩容参数的 optimizer state 从零开始，需要独立 rewarm；旧参数仍应保持小 update。
- Large-batch 下不同 parameter groups 的 update-to-weight ratio 跨多个数量级，并与收敛问题相关。
- 特定层的 gradient/update 长期被 clipping 或 precision floor 主导，且已排除数据、mask、loss reduction 和
  architecture 问题。
- Ablation 表明固定 multiplier 或 trust ratio 在 held-out quality、稳定性和 wall-clock 上优于只调 global schedule。

不应只根据 gradient norm 大小设 learning rate。若 `||g_l||` 小是因为 layer 已接近局部最优，强行放大会增加噪声；
若是因为 upstream Jacobian 已让 signal 消失，放大 optimizer step 只会放大残余噪声；若 parameter scale 本身较小，
绝对 update 小也可能已有很大的相对变化。更有意义的观测是：

```text
gradient_rms_l
update_rms_l
parameter_rms_l
update_to_weight_l = update_rms_l / (parameter_rms_l + epsilon)
clipping_fraction_l
overflow_or_underflow_l
held_out_delta by layer/group ablation
```

#### 动态逐层控制带来的新状态

让 `m_l(s)` 根据在线 gradient 或 validation signal 自动变化，会把 controller 变成训练状态：

```text
layer identity + global step
+ controller statistics / EMA / thresholds
+ multiplier history and bounds
+ optimizer moments and scheduler phase
```

这些状态必须进入 checkpoint，并在 DP/TP/PP ranks 上一致。否则 resume、reshard 或 layer renumbering 会静默改变
trajectory。Controller 还可能追逐 noisy batch、在 layers 间振荡、补偿错误 objective，或因 validation feedback delay
形成过时决策。固定 parameter groups 在证据不足、恢复/复算优先时更安全；动态策略应有 multiplier bounds、更新
cadence、holdout gate、rollback 与“退回 global schedule”的 fallback。

结论可以浓缩为：

```text
先修 gradient path / initialization / normalization
→ 再修 data, loss reduction and precision
→ 选择 global LR + warmup/decay + clipping guard
→ 检查 optimizer 与 per-layer update evidence
→ 最后才实验 fixed 或 dynamic layer multipliers
```

逐层 learning rate 是 update actuator，不是深层网络稳定性的第一性原理答案。

### Module-wise Gradient SNR 是诊断信号，不是默认学习率配方

<!-- semantic-body-binding:SF-REVEALING-MODULAR-GRADIENT-NOISE-IMBALANCE-IN-LLMS-CALIBRATING-ADAM-VIA-:start -->
全局 learning rate 与 Adam 的逐参数自适应在大多数稳定训练中足够清楚；当不同 module 的 gradient signal-to-noise ratio 长期失衡，统一 schedule 可能让高噪声模块反复消耗更新预算。此时可以把 module-wise SNR 作为是否启用 group LR multiplier 的诊断输入：先证明失衡稳定存在，再对受影响模块有界调整，并把 estimator、window、module grouping 与 optimizer state 写入 checkpoint identity。

这个 actuator 可能减少无效更新，却增加估计噪声、跨阶段漂移和更多控制状态；低 SNR 也可能是数据稀缺或目标冲突的症状，不能只靠降低 LR 掩盖。估计未校准、训练阶段快速变化或收益不显著时，回退全局 schedule 与 Adam 基线。[受限证据：arXiv:2605.05794v1]
<!-- semantic-body-binding:SF-REVEALING-MODULAR-GRADIENT-NOISE-IMBALANCE-IN-LLMS-CALIBRATING-ADAM-VIA-:end -->

### Gradient Clipping 的正确边界与顺序

Global-norm clipping 将所有参与参数视为一个拼接向量并按同一比例缩放；per-group clipping 会改变不同 groups 的
相对方向。两者都应记录 aggregation scope、norm type、threshold 与 clipping frequency。Distributed training 中，
必须先明确 gradient 是 local、ReduceScatter shard 还是已经完成 DP reduction 的 global semantic gradient，否则
“相同 max norm”并不代表相同 update。

Mixed precision 下若 loss 被 scale，clipping 必须作用于 unscaled gradients；PyTorch AMP 官方示例也要求先
`unscale_` 再 `clip_grad_norm_`，随后才执行 optimizer step。否则 threshold 实际约束的是人为放大的 gradient。

```text
backward on scaled loss
→ aggregate / accumulate under declared semantics
→ unscale gradients
→ measure unclipped norm and non-finite state
→ clip if needed
→ optimizer step
→ scheduler step
```

Clipping 适合阻止少数异常 step 破坏 checkpoint；若长期高频触发，应降低到根因诊断，而不是继续把 threshold 调小。

#### 从 Vector Norm 进入 Matrix Spectrum

<!-- semantic-body-binding:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:start -->
Global-norm clipping 假设异常主要表现为整体 update magnitude；当少数数据 outlier 只放大 weight-gradient matrix 的
几个主奇异方向时，统一缩放会同时压低大量稳定方向。Spectral clipping 保留 singular directions，只钳制超过阈值
的 leading singular values，因此把 actuator 从“整个向量”细化为“矩阵的主放大模式”。阈值与 randomized truncated
SVD 近似都成为 optimizer-side state，必须记录 cadence、rank、误差和额外 kernel cost。

它获得的是更有选择性的异常抑制，不是自动更好的收敛；低秩假设失效、谱估计滞后或矩阵很小时，分解成本和近似
误差可能超过收益。频繁触发仍要求回查数据、loss、precision 与 optimizer 根因。Global norm 在通用、低开销和
分布式聚合语义清晰时继续作为默认 guard，spectral 分支只在可观测的低秩谱异常与端到端训练证据同时成立时启用。
<!-- semantic-body-binding:SF-GRADIENT-CLIPPING-BEYOND-VECTOR-NORMS-A-SPECTRAL-APPROACH-FOR-MATRIX-VAL:end -->

## Mixed precision 为什么不是简单改 dtype

### 原生低比特训练可以来自参数几何，而不只是额外缩放补丁

传统低精度训练常以 per-tensor scale、Hadamard rotation 或更高精度 master state 修补动态范围，这在既有架构不可改时
最合理。另一条路线先约束网络参数与激活的几何，使关键向量落在受控 hypersphere 上，再让 NVFP4 等窄格式直接承载
forward/backward 的主要数值路径。变化的不是一个 dtype 开关，而是 architecture、normalization、optimizer transform、
block scale 与硬件 kernel 的联合身份。

这种共设计减少额外变换，却锁定参数化和目标格式，并把长程误差累积、异常 layer 与 optimizer state 精度变成新的
failure mode。验收必须绑定模型规模、训练 horizon、格式、scale 粒度、optimizer、硬件和最终质量；现有 exact-v1
证据只覆盖作者公开配置，不能推出任意 Transformer 都能“原生 4-bit”。已有 BF16/FP8 recipe 在架构冻结、稳定性优先
或 kernel 未覆盖时仍是可靠 fallback。<!-- source-family:SF-2026-ARXIV-2605-06067 -->

FP16、BF16 或更低精度可以减少 memory、communication bytes 并利用专用硬件，但训练需要维持数值范围和累积精度。

系统可能使用：

- 低精度参数或计算。
- 更高精度 master weights 或 optimizer states。
- FP32 accumulation。
- Dynamic loss scaling，尤其用于 FP16 underflow 风险。

所以“模型以 BF16 训练”并不能唯一确定每份状态的 dtype。Checkpoint、optimizer memory 估算和 collective bytes 都必须基于实际 precision policy。

进一步压缩 master 与 moments 时，两类误差应分开：BF16 权重外另存按该权重 ULP 半区间归一化的 signed residual，帮助累积弱更新；momentum 则先 absmax-normalize 后做 softsign companding，variance 先 sqrt 再分组整数化，以把 bin 分辨率分配到实际状态分布。每步局部重建、普通更新、重新编码，并非改变 AdamW objective 或无损保存 FP32。[FlashOptim v1 §3–5](https://arxiv.org/html/2602.23349v1)的有限 matched-control 支持状态分布影响稳定性，但梯度精度亦不同，optimizer-step 变快不等全训吞吐，部分配置直接更慢。Residual、两个 group scales、padding 与 checkpoint 都须进账，FSDP 只通信 BF16 不使 local residual 消失；零组处理、signed 编码与极弱更新仍需验证，伪码没有给全输入保证。Activation 主导或敏感任务下节省可变小，量化/解码/融合与回归费均在；恢复身份、状态精度或质量不稳时，关闭压缩或保留 FP32 master/较高精度 moments，而非从整数位数自签训练恢复等价。<!-- source-family:SF-2026-ARXIV-2602-23349 -->

统一旋转仍隐含一个额外假设：每次 GEMM 的异常值都沿同一方向分布。Forward、weight gradient 与 input gradient 的左右操作数不同，row-wise/column-wise outlier 也不同；沿内积维做 Hadamard 混合可能平滑一种组合，却对另一种无效。一个更细的条件分支先校准每条计算路径的异常方向，再选择旋转、将少量异常行/列抽到高精度支路、或对敏感组合保留完整 BF16，最后把低精度 residual 与高精度 correction 合并。数值 owner 拥有校准与精度选择，kernel 只执行该策略，不能为吞吐静默改变它。

选择性高精度换取更小量化误差，却增加索引、搬运、融合与校准状态；早期 pattern 稳定不保证训练全程或新架构不变。MXFP4 的受限证据来自 C4、1B～8B Llama/Instella 与 AMD CDNA4 实现，固定提取预算未做充分 sweep，不能推出任意精度、硬件或训练 horizon 都保持 BF16 质量。异常方向变化或 fused kernel 未覆盖时，回退重新校准、统一保守策略或 BF16 比坚持最低 bit-width 更合理。[操作数方向、混合支路与实现限制](https://arxiv.org/html/2604.02525v1#S5)

### Precision Policy 应沿误差传播路径分区

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25966:start -->
Precision policy 还与 learning-rate schedule 和模型规模耦合，不能把“低比特训练需要更长 warmdown”写成普遍规则。一个 factorial study 在匹配训练预算下未观察到 FP16、INT8、INT6 需要不同 schedule，却在 INT4、约五千万参数以上看到从 noise-dominated 到明确 warmdown preference 的边界。长期结论不是某个阈值本身，而是 bit-width、model size、optimizer/data 和 schedule 必须共同组成训练 identity。

定位这种交互需要 matched seeds 和大规模 sweep；数据、optimizer、训练长度或更大模型变化都可能移动边界。只有在已验证 cells 才能复用高精度 schedule，越界时应回退 precision-specific local sweep 和保守高精度 recipe。作者的小模型范围不能证明 frontier-scale QAT 的最优日程。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25966:end -->

训练中的 operator 即使都表现为 GEMM，也不具有相同的误差容忍度。Forward activation 的局部误差只需
在当前输出尺度下足够小；backward 中的弱信号还会被后续乘法、跨层传播、optimizer accumulation 和漫长
训练 horizon 反复放大。因而更可靠的问题不是“这个模型用几 bit”，而是：

```text
tensor / sub-expression identity
+ numerical scale and sensitivity
+ upstream quantization error
+ downstream amplification path
+ accumulation and optimizer horizon
+ batch-noise floor
-> precision / scaling / accumulation policy
```

Attention backward 提供了一个受限但有解释力的例子。若 softmax 输出为 `P`，上游梯度为 `dP`，其
score gradient 具有如下结构：

```text
dS = P * (dP - row_sum(P * dP))
```

这里的减法会抵消共同分量，`dS` 可能远小于 `P` 或 `dP`。若在产生这个微小差值之前就粗粒度量化
`dP`，量化噪声可能超过真实信号，再经 `dQ`、`dK` 路径放大。一个 sensitivity-aware policy 可以让前向
`Q/K/V/P` 使用更低精度，同时对关键的 `dP` 或 accumulation 保留较高精度，并只量化已经完成敏感
变换后的子路径。这里的长期原则是 **precision boundary 要跟随误差形成的位置**，不是任何一组固定
dtype 或 kernel 配方。

数值变换也必须与数学不变量一起验证。例如 softmax score gradient 的 row sum 为零，可以支撑某些只
改变公共分量的平滑变换；对另一 operand 做表面相似的 smoothing，若需要额外 correction，就可能重新
注入量化噪声。不能因两个输入都进入同一次矩阵乘就假设它们有对称的处理空间。

不变量还会被跨 forward/backward 的保存值破坏，而不只是当前 operand 的精度太低。高精度实现可用 forward output 与上游梯度求得 softmax backward 的公共抵消项；量化 forward output 后，这个 saved delta 未必等于 backward 当前使用的 `row_sum(P*dP_hat)`。若仍沿用旧值，即使梯度 matmul 本身可执行，也会留下非零公共残差。用当前 contraction 重算 matched delta，把抵消项与实际 `dP_hat` 绑定，恢复的是再量化之前的 zero-row-sum，而不是消除全部 FP8 误差。

该修复增加 reduction/recompute 与 kernel 融合负担，证明仍要求归一化 `P`、前后同一 `V` 及明确 rounding 条件；`dS` 后续量化可以再次留下 residual。[Delta-Matching 的原生 FP8 attention-core 实验](https://arxiv.org/html/2609.37852v1)说明小模型、短训练或较低 learning rate 可掩盖 stale-delta 累积，不证明所有 optimizer/架构都收敛。其 kernel-only 计时排除了输入量化和 autograd wrapper，须与端到端训练成本分账；不能稳定复现 contraction identity 时，成熟 BF16/FP32 backward 仍是正确回退。

<!-- source-family:SF-2026-ARXIV-2609-37852; semantic-body-binding:forward-backward-matched-softmax-delta -->

Kernel 吞吐只有在 trajectory invariant 基本成立后才有意义。至少应同时比较 full-precision reference、
loss/gradient divergence、长 horizon 收敛、不同 sequence length、batch 与 optimizer 设置，以及端到端
step time。更大的 batch 可能用 gradient noise 掩盖量化误差，较短 run 也可能来不及暴露累计偏差；这两者
都不能证明低比特路径在更大模型或更长训练中稳定。全精度 backward 在敏感信号尚未定位、复现成本可
接受或训练失败代价很高时仍是合理旧方案；常规 mixed precision 适合已有成熟 scaling/accumulation 的
算子；sensitivity-aware 分区则用更复杂的 kernel、scale metadata 和验证矩阵换取进一步压缩。

Block-scaled low-bit training 还要求把 **scale format、scale lifecycle 与 tensor role** 一起设计。Block scale
只表示非负幅度时，可以把 signed format 中不会使用的 sign bit 改作 exponent range；这扩大可表示范围，却不会
提高重叠区间内的相对精度。局部 block scale 仍要与 tensor-level reference、amax refresh horizon、headroom、
二维 weight scaling 和 block granularity 配合，否则更宽 codebook 仍可能被过期 reference 或不一致的两个 GEMM
视图抵消。对 `dY` 采用 stochastic rounding 可以在理想随机实现中保留小梯度的期望值，但不等于 weights、
activations、scale codes 或任意 tensor 都应使用同一 rounding policy。

Delayed scale 是跨 step 的执行状态，不是学得的模型参数；训练恢复和推理初始化必须显式记录或重建其 cache、
refresh cadence 与输入顺序。更宽的 unsigned scale 可以减少 rotation、全局重标定或高精度尾层的需求，但是否删去
这些旧保护要由 matched long-horizon trajectory 与实际硬件路径分别证明。现有
[UE5M3 FP4 预训练证据](https://arxiv.org/html/2609.02846v1)来自单一 8B、188.7B-token 轨迹且 UE5M3 GEMM
由软件 emulator 实现；原生 Blackwell 对照仍执行 E4M3，报告的吞吐变化又同时移除了 RHT、扩大 FP4 layer
coverage，并排除了 data、optimizer 与 distributed cost。因此 BF16 或成熟 native E4M3 recipe 在硬件不支持、
scale state 难以复现或稳定性证据不足时仍是正确 fallback，不能把 emulator 稳定性写成端到端加速。

低比特误差也可能不是少数孤立 outlier，而是沿 token 方向共享的 coherent mean。直接用 block extreme 定标
简单、容易映射硬件；SVD/whitening 能分离 dominant direction，却很难进入每步训练热路径。一条较窄的结构
分解是先把 activation 或 output gradient 写成 shared mean 与 residual，再分别量化和累积：

```text
X = broadcast(mean(X)) + residual(X)
-> quantize mean and residual under separate scales
-> reconstruct GEMM from residual and cross terms
```

它通过改变 quantizer 所见 distribution 保存 long-tail variation，却新增 mean reduction、subtraction、额外
cross terms 与融合要求；microbatch/sequence composition 改变时，mean 本身也是漂移状态。Averis 的受限实验
支持这种 source-aware split 在其 FP4 training graph 中缩小数值差距，不证明 column mean 是所有层、模型与训练
阶段的 dominant error，也没有公开硬件吞吐合同。Vanilla FP4 在偏置弱时更简单，FP8/BF16 在同步成本、
实现成熟度或失败代价优先时继续成立；是否采用分解必须同时看 convergence 与 end-to-end step time。

### 低精度 block scale 必须在 forward/backward 视图间保持身份

同一矩阵在 forward 与 backward 中常以转置视图参与 GEMM。若 FP4 block partition 随存储视图重新切分，同一数值会得到不同 scale state，训练图便不再拥有一致的量化语义。二维 block scale、稳定的 scale identity 与明确 rounding rule 可以减少这种 transposition mismatch。

这类机制增加 metadata、layout 约束和 kernel 复杂度；有限训练轨迹也不能证明任意模型、optimizer 或原生硬件都稳定。正确性 gate 应成对检查两个 GEMM 视图、gradient/optimizer 误差与 loss stability，超界时回退 FP8/BF16，而不是仅凭低比特 forward 成功批准全链路训练。

<!-- source-family:SF-2026-ARXIV-2607-24953 -->

### 低比特 Training Graph：无偏不等于免费

保留高精度 master weights 最容易维持 optimizer trajectory，却让静态状态继续主导显存；直接删除 master
copy 可以降内存，但持续 rounding bias 会进入 momentum 并累积。两条实验性分支分别处理这种误差：

```text
quantized weight update
→ feed quantization residual into optimizer momentum

FP4 forward/backward
→ stochastic rounding
→ rotate and rescale backward operands
→ keep gradient estimator approximately unbiased
```

前者复用 optimizer state 承载 error feedback，新增 state semantics 与 checkpoint compatibility；后者把
rotation、microscale、re-quantization 和 hardware tile constraint 纳入 computation graph，小矩阵可能被
overhead 吞没。无偏 estimator 只约束期望误差，不自动证明有限训练 horizon、任意 optimizer 或终局质量；
BF16/FP8 在 debug、旧硬件、小矩阵或 accuracy-first 场景仍成立。低比特证据必须同时绑定 forward、
backward、optimizer state、rounding、硬件和端到端收敛，不能只报 tensor-core peak。

#### 低精度 Optimizer State 需要保持完整基底

直接把二阶 preconditioner 压到低精度，在小状态或条件数温和时能节省显存；大模型训练中，量化后的 basis 缺失会让更新方向失真。Optimizer owner 可以重参数化 preconditioner：用被更新的 basis vector 与未改变的向量共同维持完整基底，再以 BF16 存储。收益是降低状态开销并保留方向结构，代价是 basis 维护、正交误差和实现复杂度；数值漂移或 tested regime 外的谱结构会使收益失效，应回退到更高精度状态或更简单 optimizer。exact-v1 只支持论文五组实验和 Appendix C 的限制，不证明所有模型、硬件与长训练 horizon 的稳定性。<!-- source-family:SF-2026-ARXIV-2605-26327 -->

#### Optimizer State 的量化误差会沿时间累积

低比特 optimizer state 不是一次静态压缩。Adam 的一阶、二阶状态是跨 step 的 EMA；量化器每次读写都会改变下一次 update 的输入，因此同样的 tensor reconstruction error 可能产生两类不同的动态失败。

<!-- semantic-body-binding:SF-2025-SOLO:start -->
当 magnitude-like EMA 采用只表达非负值的粗粒度编码时，历史大值可能让新产生的小信号长期落在量化格以下；当 signed momentum 过粗时，误差又可能翻转或放大方向，逐步累积为 update variance。因而 state format、momentum coefficient、scale update、zero handling 与 checkpoint restore 必须共同成为 optimizer identity，而不能只报告“2-bit state”。Log quantization 与 precision-specific momentum 是一种受限修复：它用更复杂的编码、kernel 和迁移语义换取较低 state memory；作者实验不覆盖所有 optimizer、长周期训练、分布式恢复或任意数值格式。训练规模较小、稳定性优先或无法验证长 horizon 时，高精度 optimizer state 仍是 canonical baseline。
<!-- semantic-body-binding:SF-2025-SOLO:end -->

#### 量化前可以训练 Gauge，而不改写原 Objective

量化困难不仅取决于数值大小，也取决于在等价表示中选择了哪个 basis。某些成对正交变换在 full precision 下保持 Transformer 输出不变，却会因 element-wise quantization 不与 rotation 对易而产生不同误差。

训练期可以用 stop-gradient 的 outlier proxy 只更新 gauge/basis，让 LM weights 仍由原 objective 更新。这样把“改变模型学什么”与“选择更适合量化的等价表示”分开，却新增 optimizer/export state、MLP runtime transform 与 kernel compatibility。短 continued-training 的 fake-quantization 结果只支持机制可行，不证明 full pretraining、真实 low-bit kernel 或 serving 加速。

## Activation checkpointing 移动了什么瓶颈

Backpropagation 需要 forward activations。全部保留会占据大量显存；activation checkpointing 只保存部分边界，backward 时重新计算中间 activations：

```text
less saved activation memory
<-> more recomputation FLOPs
```

它减少的不是 parameters、gradients 或 optimizer states。第 39 章 ZeRO 主要处理 model-state redundancy，两者解决不同 memory categories，可以组合。

Checkpoint 这个词在这里容易混淆：activation checkpointing 是计算图重算策略；第 35 章的 training checkpoint 是持久化恢复状态。

静态 activation checkpointing 预先决定保存边界，在线 rematerialization 则在容量压力下按 tensor 的重算成本、大小和最近使用选择 victim；一次逐出会改变后来重算与再次逐出的历史。因此“给更多 memory 应该单调更快、更可行”不能直接作为在线策略的验收假设。受控 trace 中，相邻预算可以让几乎同一批 tensor 被反复逐出的次数骤增；另一些预算改变执行历史，使当前 pinned storages 加 pending allocation 超过容量，而所有合法 victim 已为空。

这些反例来自固定 simrd runtime 的 deterministic trace，不是完整 GPU／LLM 训练实测，也不证明所有 rematerialization 都有同一病因。局部删去 score 因子消除某段切换，不等于通用 repair；重算开销、live/pinned frontier 与 eviction history 应随预算一起记录，在压力区间作有限细粒度检查，而不以两点 benchmark 或全域二分假定单调可行边界。实际 runtime 无法验证成本和容量时，保留静态保存／重算计划或更保守预算；第35章的持久恢复状态仍不由这条策略替代。[DTR 的必要机制与限制](https://arxiv.org/pdf/2609.31250) <!-- source-family:SF-2026-ARXIV-2609-31250 -->

## Scaling 不是只增加参数

第 7 章已经说明 Scaling Laws 是经验规律。Pretraining 需要同时分配：

```text
model parameters
training tokens
compute budget
data quality and mixture
```

只增大参数而训练 tokens 不足，模型可能 undertrained；只增加重复低质量 tokens，也不会获得与独立高质量数据相同的收益。Compute-optimal 分配是特定模型家族、数据和预算下的经验决策，不是永恒常数。

循环复用权重进一步把**独立参数容量**与**实际执行深度**拆开：相同有效 block 数下，重复一组参数可以减少权重驻留，却仍要执行多轮 block 与反向传播。固定训练 FLOPs 时，宽度和可消费 tokens 也会随之改变；因此不能只把共享后的参数量代入 dense 的参数—数据分配公式，而应在声明的循环结构、输入注入和执行预算下重新拟合质量前沿。模型 checkpoint 拥有共享关系，训练系统拥有每轮 activation、梯度和 token/FLOP 总账；服务内存下降不等于训练或推理时间下降。<!-- source-family:SF-2026-ARXIV-2604-21106 -->

[受限 iso-depth 对照](https://arxiv.org/pdf/2604.21106v1)固定二十个有效 block、使用 full BPTT，并在六档预算中比较宽度与数据分配。116 次运行得到的共享容量指数只是该实验范围的拟合，所测 dense 前沿仍占优；原文没有证明 truncated BPTT 或另一种循环连接会消除差距，也未给出匹配 wall-clock 的普遍结论。权重内存确为约束时可继续比较复用分支；知识容量或训练效率优先、循环带来较长关键路径时应保留 dense baseline。第 17/18 章解释循环执行的模型状态，本章只负责训练预算与质量前沿的判断。

### 模型压缩的 Baseline 必须绑定训练预算与可执行粒度

从大模型剪枝可以复用已有表示，直接训练较小 dense 模型则拥有更简单的 artifact 和执行路径；若二者消费的追加训练 tokens、初始化来源和数据顺序不同，只比较最终精度会把压缩机制与额外训练预算混在一起。公平比较至少要冻结 parent lineage、目标尺寸、训练 token budget、mask/granularity 与 optimizer recipe，再把质量 Gate 和硬件执行 Gate 分开。

细粒度稀疏可能在相同 token budget 下保留更多质量，却未必被目标 kernel 消费；结构化剪枝更容易产生速度收益，也可能删除更有用的容量。Training run 只证明压缩后的模型质量，runtime owner 仍需在目标硬件上证明 latency、memory 和 SLO 改善。缺少稳定 sparse kernel、训练预算无法匹配或质量回归超界时，直接训练 dense small model 仍是可验证 fallback；单一模型族和剪枝比例不能推出通用最优路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.14150 -->

多尺寸压缩还要分开 child initialization 与 teacher identity。一个 cascade 分支从 parent 剪枝后做 short-context continual distillation，再以这份 short checkpoint 初始化更小 child；当前尺寸的 long-context continuation 是独立交付分支，不成为下一尺寸的默认 parent。各尺寸仍可使用同一原始大 teacher，不能把链式初始化误写成逐代换 teacher。这样数据顺序、短/长上下文预算与 parent checkpoint 都进入 lineage，而不只登记最终模型尺寸。<!-- source-family:SF-2026-ARXIV-2601-08584 -->

受限配方证明这条交付路径可用，不证明 cascade 总 compute 优于 one-shot pruning 或从头训练；完整 parent、追加 tokens 与 FLOPs 未作匹配。Teacher 越强也不必在每个阶段越好：预训练蒸馏与后训练中观察到不同的 teacher 选择反例，不能把单项能力排名当成通用教师效用。需要按训练阶段、目标数据与预算验证 teacher/student 配对；长上下文恢复失效、父模型成本无法承担或质量回归时，保留固定 teacher、直接训练较小 dense 或更保守的压缩路径。

### Low-rank Pretraining 不能只用 Perplexity 验收

低秩参数、梯度或 optimizer state 可显著降低预训练内存，但相同 perplexity 可能对应不同的表示几何和频谱容量。验收应同时观察有效 rank、谱能量、梯度子空间、训练稳定性与 downstream transfer，判断约束是在去除冗余还是切掉后续能力所需方向。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13652 -->

几何指标仍是代理，所测低秩方法与规模也不代表 frontier pretraining。谱容量不足、迁移任务回归或优化不稳定时，应提高 rank、只压缩部分状态，或回退 full-rank training。

### 结构化剪枝后的恢复不能只依赖短程 Fine-tuning

对 VLA 等长链模型做 width/depth pruning，可以降低部署成本，却会同时切断中间表示和动作生成所依赖的层间契约。一个受限恢复分支在剪枝前缓存 teacher hidden states，剪枝后以离线 representation matching 修复 student，再进入任务 fine-tuning；这样减少在线 rollout/data 依赖，但 recovery objective、移除轴与目标 kernel 必须共同版本化。<!-- source-family:SF-2026-ARXIV-2609-19579 -->

离线 hidden-state 对齐不证明行为等价，也可能把 teacher 的偏差和过度拟合一起蒸馏。width 与 depth removal 会产生不同失效形态，最终 promotion 仍需任务回归、目标硬件执行和真机 release gate。现有证据限 CogACT/LIBERO 与一套 6DoF 真机；对齐失效、任务回归或执行路径不兼容时，应回退更保守剪枝、保留关键层或未剪枝 checkpoint。

### 数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账

<!-- semantic-body-binding:SF-SPARSE-REPEATED-TRAINING:start -->
经典 compute-optimal 分配隐含一个近似前提：新增训练 tokens 仍带来足够的新信息。语料受限后，同一批 unique tokens 会被重复消费；此时把训练 token 总量继续当作独立数据，会把记忆化收益、数据饱和与模型容量混成一个轴。更完整的实验身份应同时冻结 unique-token volume、repetition count、effective parameters、sparsity、数据质量和 optimizer/schedule，再比较同一预算下增加模型、增加重复轮次或改变稀疏度的边际收益。

这条分支把“稀疏模型能容纳更多参数”与“重复数据还能提供多少新信号”放进同一 data-saturation boundary。它能避免直接套用 dense Chinchilla 分配或把理论 FLOPs 节省解释成真实硬件收益，却增加 scaling-law 拟合、语料多样性估计和跨配置 sweep 成本。拟合范围之外、token 质量改变、optimizer 或稀疏 kernel 改变时，原最优点必须重新校准；unique data 充足、重复率低或稀疏执行没有硬件支持时，普通 dense scaling 与单次语料遍历仍是更清楚的基线。现有 exact-v1 证据只覆盖论文披露的模型尺度、语料、稀疏过程和 compute regime，不证明 frontier-scale mixture 或生产硬件效率。
<!-- semantic-body-binding:SF-SPARSE-REPEATED-TRAINING:end -->

Pretraining loss 曲线还不能直接解释具体能力。某些能力只在合适 prompting、post-training 或 Evaluation 中显现；另一些平均 loss 改进可能集中在高频简单 tokens。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-06888:start -->
数据受限的预训练会反复消费同一 token，普通 scaling law 因而不再只由总 token 数决定。Masked-input regularization 把重复样本的一部分输入随机遮蔽，以降低记忆化并改变 compute/data 最优点；证据只覆盖作者固定 architecture、optimizer、至多 1.4B 参数和 400M unique tokens，不能外推为任意重复率下的通用最优策略。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-06888:end -->

### Scaling-law Pilot 也是有预算的实验调度

预先跑固定网格再拟合 scaling law，在候选规模少、单次实验便宜且目标区间接近观测区间时最透明。实验成本随规模快速增长后，pilot 本身已经是一项预算分配：不同 run 成本不同，对高成本 target region 的外推信息量也不同。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22753:start -->
一种条件分支把待跑配置、成本、当前拟合后验与目标区域写成 versioned experiment state，在剩余预算内比较候选对目标区的预期信息增益，并按实验成本折减后选择下一项，再用新结果更新选择策略；不能只选绝对不确定性降幅最大的 run。Scheduler 只拥有实验 proposal；训练结果、拟合模型和独立 holdout 共同决定 scaling-law artifact 是否可用。它能把预算集中到单位成本信息量较高的 runs，却依赖不确定性校准、候选池与成本 proxy，且一次或近视选择可能错过更好的组合。后验不可信、目标区改变或需要审计可比性时应回退预定义 grid。作者只在其 scaling-law tasks 与 mixture approximation 下展示效果，不证明可安全规划任意大模型训练。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22753:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21486:start -->
超参数从小规模向大规模迁移，不能只看一次最优值是否接近。更完整的 transfer contract 同时检查 scaling-law fit、
对 extrapolation error 的鲁棒性，以及所选 parameterization 在极限尺度留下的 loss penalty；weight decay、训练长度
和 compute-optimal allocation 也要作为联合变量。它增加多尺度 probe 与拟合成本，且仍依赖作者的模型族和实验
范围。拟合不稳或目标规模越出观测区间时，应回退目标尺度小网格、保守 schedule 和在线 canary，而不是把一条
经验缩放规则永久固化。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21486:end -->

#### Probe 饱和后，Fragility 只能补充诊断

线性 probe accuracy 在训练早期饱和，不代表表示停止演进；它可能只是分类边界已经可分，却没有反映 margin 与冗余继续变化。可以逐层注入 activation noise，测量 probe accuracy 崩溃的临界点，把 fragility 作为补充 sensor。跨层比较必须按各层 activation RMS 归一化，否则幅值差会伪装成鲁棒性；同层随训练比较则可保留 raw threshold。

噪声诊断增加 forward 成本，也依赖 probe、noise family 和阈值选择；更稳不等于下游能力更强。它只拥有训练过程的诊断权，不能单独提交 checkpoint 质量，必须与原 probe、迁移任务和最终 Evaluation 共存。现有证据限作者模型和训练轨迹，不提供跨架构的统一阈值。
<!-- source-family:SF-2026-ARXIV-2606-11375 -->

### Training Budget 与 Test-time Compute 必须放进同一生命周期目标

传统 early stopping 只观察 validation curve，并隐含假设部署时每个请求只产生一个答案。这个旧方案在
single-pass latency 严格、部署量大或没有可靠 verifier 时最清楚。若部署允许对同一问题采样多个候选并搜索或
验证，模型 checkpoint 与 test-time budget 就共同决定任务质量：较早停止训练可能以更高的每请求推理成本
补回部分差距。

```text
choose checkpoint c and test-time budget K
to satisfy quality and latency constraints
while minimizing
training_compute(c) + deployment_volume * inference_compute(c, K)
```

这不是“少训练一定更省”。Learning-curve 与 `K`-quality curve 都是估计；Pass@K 只说明候选集合覆盖，
不等于 selector 能稳定产出一个正确答案。Verifier、并行 sampling capacity、output length、tail latency、
refresh frequency 和 deployment volume 变化后，原先的 break-even 会移动。高流量长期服务通常会把节省的
一次性训练 FLOPs 重新付给推理；低频专用模型、训练极贵且可并行验证的任务则可能采用另一 operating point。

TTC-aware early-stopping 的预印本在有限模型、checkpoint 和代码/数学 benchmark 上展示了联合选择的可行性；
它没有证明其 curve family 能外推到更大模型或开放任务。长期结论是：**early-stop decision 必须携带预期部署
workload，而不是只携带 validation loss；上线后也要用实际 query volume、K、quality 与 SLO 重算生命周期账本。**

### Activation Sparsity 可能来自 Optimizer–Activation Coupling

把激活稀疏视作架构或数据的静态性质，会忽略初始化阶段的方向性更新。正偏激活配合标准 loss 时，权重可能出现系统性 negative drift，逐步把更多 unit 推入非激活区，并在少数剩余路径形成 spike。

这条解释要求联合观察 activation distribution、weight drift、gradient 与 optimizer state；它不是“负漂移总是有害”或默认正则收益。初始化、activation、normalization 或 objective 改变后机制可能消失；证据不匹配时回到常规稳定性诊断，而不是机械修正权重符号。

它相对只看 loss/gradient norm 的收益，是把异常进一步定位为可检查的 optimizer–activation coupling，从而决定应调整初始化、激活、归一化还是更新规则；代价是额外采集分层 activation/weight/optimizer 统计，并引入可能干扰训练的诊断或 actuator。现有 exact-v1 只覆盖其形式化例子与披露的 architecture、initialization、activation 和 optimizer 实验，不证明其他组合存在同方向漂移，也不提供通用在线控制器。

<!-- source-family:SF-2026-ARXIV-2605-17659 -->

### Regularization 必须匹配 Deployment Shift 的方向

不知道部署偏移方向时，均匀分散的正则化是合理 baseline，因为它不押注某一脆弱轴；如果 shift direction 已被可靠观测，matched penalty 才能把容量集中到真正变化的子空间。Training run identity 因而要绑定 shift hypothesis、penalty axis、estimator revision 与 held-out shift set，不能只记录一个正则系数。

定向约束可能降低 residual error，却会在轴选错时制造新的 residual floor，并增加估计与调参成本；未知或快速变化的分布应回退 even-spread baseline。arXiv:2605.22800v1 的理论和深网实验只支持论文假设与受测设置，不构成所有架构和真实部署偏移下的普遍定理。

<!-- source-family:SF-2026-ARXIV-2605-22800 -->

## 训练稳定性是多层系统问题

Loss spike 或 NaN 可能来自：

- 异常或极长 data batch。
- Learning rate、initialization 或 optimizer 配置。
- Low-precision overflow/underflow。
- Collective、硬件或 silent data corruption。

- 恢复 checkpoint 后状态不一致。
- 不同 ranks 读取到不同 batch 或参数。

因此监控不能只有平均 loss。至少应关联：

- Per-domain loss、token throughput 和 data source。
- Learning rate、gradient norm、clipping 与 overflow。
- GPU memory、step time、straggler 与 collective time。
- Skipped steps、retries、hardware errors。
- Checkpoint save/restore validation。

训练平台的价值，是把模型信号、数据身份与系统信号放在同一条 timeline 上。

### Activation Pattern 可以预警训练状态，但不能单独控制 Optimizer

loss 与 accuracy 从训练外部观察结果，常在层内结构已经恶化后才出现明显信号。逐层 activation statistic 可以作为 label-free early sensor，提前提出 schedule、regularization 或暂停建议；optimizer controller 与 held-out evidence 仍拥有 commit authority。它用统计与校准开销换更早可见性，也可能把坏的稳定点误判为健康，架构变化还会使阈值失效。因此应先 shadow 运行，并与 loss、gradient、checkpoint recovery 和外部任务联合判断。exact-v1 只支持“activation 可补充训练状态”，不支持一个通用阈值、自动调参最优或单指标 early stopping。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11570 -->

### 瞬态放大不能只由渐近谱稳定判断

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23476:start -->
只看 update operator 的 eigenvalues 会漏掉 non-normal matrix 在有限步内的 transient amplification：即使渐近
谱稳定，非正交 eigenvectors 仍可能先放大扰动。Eigenvector conditioning 或 pseudospectrum 因而可作为训练
sensor，帮助区分“最终会收敛”和“中途已越出数值/质量边界”；它们不拥有学习率或 checkpoint commit。诊断需要
昂贵矩阵估计且 basis 可能不稳，论文也只给理论构造与小型 two-layer 数值实验，不证明大型 Transformer 收敛或
墙钟收益。成本或稳定性不满足时，应回退 matched update norm、SVD、loss trajectory 与 optimizer baseline。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23476:end -->

相邻 residual-layer states 也可提供局部 operator proposal：对同输入的 X/Y snapshots 采用同一 X-based whitening、拟合 DMD 并过滤高 residual modes，再以 near-unit spectral mass 与 eigenvector conditioning 提出训练风险。该 mass 是所选 rank/阈值下的比例，不是 spectral radius 或校准后的发散概率；同一个局部 operator 还可进入训练 loss，以 unstable penalty 和 near-unit soft target 共同 shaping，而非直接改 optimizer 的矩阵 sign。[RKSP/KSS v1](https://arxiv.org/html/2602.22988v1)在有限 No-Norm、高 LR 和约等额外开销的干预对照中支持这个条件分支，norm sweep 的高 AUC 不保证每种 normalizer 内或新 recipe 都同样可识别，7B forward 统计也不是7B训练获益。Whitening/低秩谱分解、抽层、额外forward/梯度与阈值校准有费用，正常 Pre-LN/RMS 可在高谱量下仍稳定；局部拟合不可靠、non-normal瞬态遗漏或现有配方已稳时，保留 normalization、clipping 与 held-out 回归，不由风险排名自动取得停训/调参权。<!-- source-family:SF-2026-ARXIV-2602-22988 -->

### Regularizer 的作用要沿 Backward Transport 判断

相同 forward penalty 经 output head、tied embedding、MoE router、reduction 与 optimizer 传播后，可能形成完全不同的真实参数更新。选择 z-loss 或其他 regularizer 时，应记录 loss coefficient 只是起点，再检查各 owner 的 gradient transport、scale、clip 与 update ratio；forward loss 变小不能单独证明训练稳定。<!-- source-family:SF-2026-ARXIV-2609-16179 -->

逐路径诊断增加 instrumentation 和调参成本，小模型/低 coefficient 的结果也不构成通用保证。梯度路径无法可靠解释时，应回退已验证的 normalization、clipping 与 conservative coefficient，并由 MoE 章节单独负责 router-specific 更新。

### 稳定训练从经验 Trick 走向显式几何与预算控制

当激活尺度和更新方向只靠 clipping、normalization 等经验规则约束时，训练稳定性往往表现为“换一组超参数就失效”。更可解释的分支是把 activation scale 与 update geometry 写成显式 manifold constraint，使允许的参数移动、数值范围和恢复条件都能被测量。它以额外投影、约束计算和可能受限的可达解空间，换取更清楚的稳定边界；约束与真实 loss geometry 不匹配时必须回退到未约束优化并重新校准，而不是把低 loss 当作约束正确的证明。

同一 optimizer 与同一精度覆盖所有参数块，配置简单、状态迁移清楚，在显存充足或各层梯度统计相近时仍是合理配方。约束变化来自大模型 optimizer state 的显存成本，以及不同 block 在方向稳定性、尺度各向异性、动量需求和量化敏感度上的差异：昂贵状态并不一定要平均分配。一个可选分支是先在 warmup 中稀疏采样各 block 的 gradient stream，把统计量转换为候选配置的 mismatch risk，再在 memory 与 per-step time budget 下求解 block-wise 配置，例如决定哪些 block 保留 momentum、较高精度或更昂贵的 optimizer state。

这里改变的是 **optimizer state 的逐块资源分配**，不是把 optimizer、learning rate 与 regularization 做一般性的 trial-budget 搜索。它能在给定预算下把昂贵状态留给风险更高的 block，却引入 warmup 代表性、risk model 失配、求解开销、phase drift 与在线重分配时的 state inheritance 问题。`arXiv:2605.04711v1` 只在其 vision、language 与 diffusion workloads 中支持这种 memory–quality trade-off，不证明任意长程 LLM 训练都能保持质量；梯度统计不稳定、预算宽松或重配置证据不足时，全局一致且已验证的 optimizer recipe 仍是更稳妥的回退。

### Weight Decay 通过全局参数交互改变 Sharpening

把 weight decay 理解成每个参数独立的局部摩擦，便于解释正则化，却不足以说明深网接近 edge-of-stability 时的曲率演化。更新所有参数的收缩会改变层间尺度与组合函数，进而通过全局交互影响 progressive sharpening；因此“加入 decay 后更稳定”不能只归因于单点 gradient 变小。

这条机制要求把 decay、learning rate、normalization、architecture、loss curvature 与参数范数一起做 matched run。它能解释特定设置中的稳定性变化，却不证明 weight decay 对所有模型都提高稳定性；强 decay 还可能损害拟合或改变最终 function。架构、数据或 optimizer 不匹配时，应回退经验证的原 schedule，并用 loss spike、谱/曲率、update ratio 与下游质量共同判断。

训练后的 decay 还可能改变表示的可读性，而不同时抹去已经学会的计算。固定配方在质量和恢复稳定时仍合理；若需要用线性 reader 做诊断或下游接入，却发现 probe 退化，应先区分信息被丢弃、非线性重编码和任务行为改变。一个受限分支从同一已泛化 checkpoint 继续训练，仅改变 decay，再联合比较任务行为、线性与非线性 reader、参数范数和更新方向。这把 schedule 的目标从“继续提高任务分数”扩展为有条件的表示可读性取舍，而不是看到 probe 降低就补数据或宣布遗忘。<!-- source-family:SF-2026-ARXIV-2604-07380 -->

这种比较增加 reader 与多配方训练成本，也可能牺牲任务质量。[受控的小模型实验](https://arxiv.org/html/2604.07380v1)观察到，降低后期 decay 可以恢复部分线性读出而任务准确率变化较小，但并非严格等价；它不支持大模型通用的“先高后低”配方，也没有证明梯度与 decay 的对齐导致泛化。局部低曲率扰动与移除整个参数投影不是同幅操作，同维数随机对照也不自动匹配移除范数，不能据此把平坦方向判为无功能或唯一因果轴。只有目标任务与独立 reader 的实际收益均可复现时才考虑调整，其他情况保留经过验证的 decay schedule。

Adam 的两个动量时间尺度同样不能被当作彼此独立的经验旋钮。跨模型与任务的扫描观察到，spiky/non-spiky 区域近似由 `1-β₂ = C(1-β₁)` 分隔；简单二次 loss 给出的斜率关系并不匹配，而 superquadratic effective loss 能复现接近线性的 phase boundary。这提供的是诊断坐标：训练 owner 应联合记录 `β₁/β₂`、effective curvature、学习率、normalization、precision 与 spike onset，并用小规模 sweep 找可复现的稳定区域。边界系数随架构和任务改变，作者实验也不证明该直线是通用定律；发现几何失配时仍应回退成熟 recipe、降低 step size、加强 clipping 或重新检查数据/数值异常。

<!-- source-family:arxiv:2609.18314v1 -->

<!-- source-family:SF-2026-ARXIV-2605.16622 -->

<!-- source-family:SF-DEMYSTIFYING-MANIFOLD-CONSTRAINTS-IN-LLM-PRE-TRAINING -->
<!-- source-family:SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR -->

### Architecture Warm-up 只能作为受测曲率压力的 Actuator

固定深度配合 learning-rate warm-up，状态简单且容易恢复，在曲率随训练平稳变化时仍是默认路径；但深度本身也会使预条件后的最大曲率突然上升，此时统一降低 learning rate 会让所有方向一起变慢。一个条件分支用 warm-started power iteration 估计最大 preconditioned Hessian eigenvalue，再逐步启用更深的网络，使 active depth 成为 trainer 持有的版本化状态。

这不是让 curvature sensor 自动掌控训练。Trainer 仍拥有 active-depth 与 optimizer transition，sensor 只提供有边界的风险信号；Hessian-vector product、深度切换和状态迁移会增加计算与恢复复杂度，估计失真还可能掩盖真正发散。小模型、曲率稳定或拓扑切换成本过高时，固定架构加普通 LR warm-up 更合适；现有理论和实验也不能成为所有架构与 optimizer 的通用 recipe。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16768 -->

### Operator-normalized Risk 把异常信号变成有预算的 Recovery Proposal

全局 gradient norm 在训练 recipe 稳定、算子尺度近似可比时，是发现整体爆炸的便宜 sensor；把不同 operator 的 raw norm 直接排序，则会把长期尺度差异误当作风险。更细的 runtime controller 可以让每个 monitored unit 维护自己的历史 baseline：长窗口 ratio 感知相对自身历史的偏离，短窗口 delta ratio 感知突发变化。两者只提交 risk signal；backend 预先声明哪些 operator、branch、block 或 layer 是 recoverable unit，以及各自有哪些低成本与 recovery execution path。

控制器再在 hard recovery budget、阈值与 lock interval 下选择少量高风险单元切换路径，其余单元继续低成本执行。这样改变的是每个 training step 的 execution routing，而不是 loss、numerical format 或 optimizer authority；controller statistics、threshold revision、recovery budget 与实际 route receipt 都必须进入 checkpoint / trace。收益是在少数局部异常出现时避免整步永久升级高精度，代价是额外 norm reduction、history state、route fragmentation，以及异常在不可恢复单元传播时的漏检。

该机制依赖 backend observability、可恢复执行单元和兼容的 recovery implementation；历史均值受污染、风险阈值漂移、budget 过小或频繁 lock 都可能让控制器错过故障或过度回退。论文的结果绑定 activation-quantization、DeepSeek-style mixed-precision 与 LLaMA-2 13B stress settings，不证明跨 backend 的通用低精度稳定性。缺少 operator identity、recovery path 或 matched high-precision canary 时，应继续使用全局 clipping、loss scaling、skip/retry 或整步高精度 fallback。

<!-- source-family:SF-2026-ARXIV-2606-00539 -->

### “训练仍在运行”与“会得到好模型”之间隔着多层证据

超长训练最危险的误判，是把一条平滑下降的 training loss 当成最终质量证明。训练信号更适合作为分层证据：每一层能排除一部分故障，却没有任何单一信号可以提前担保 checkpoint 的产品价值。

| 信号层 | 主要观测 | 能支持的结论 | 不能单独证明 |
| --- | --- | --- | --- |
| Objective | training/validation loss、per-domain loss、PPL | 当前 objective 在声明的数据与 mask 上是否改善，是否出现过拟合或 domain divergence | 事实性、指令遵循、安全与产品任务质量 |
| Update | gradient norm、update-to-weight ratio、clipping frequency、optimizer moments | 是否存在爆炸、消失、异常 step 或 group-wise update 失衡 | 梯度方向是否代表正确数据与目标 |
| Numerical | non-finite count、loss scale、overflow/underflow、skipped step、activation/logit range | mixed-precision path 是否还能产生有限、可执行的 update | 有限数值是否与高精度 reference 足够等价 |
| Data | source/domain mix、effective tokens、duplication、length、mask、batch identity | 实际消费分布是否符合 data contract，异常 loss 能否定位到样本 | 数据本身是否无偏、真实、合法或覆盖部署长尾 |
| System | step time、tokens/s、memory、collective、straggler、ECC/Xid、retry | 计算是否持续推进，故障或降速来自哪个 runtime/resource path | 高 utilization 是否产生正确的参数轨迹 |
| Evaluation | held-out loss、capability/safety suites、sample review、scaling probe | 中间 checkpoint 的可观察能力、回退与趋势 | 未测分布上的最终泛化，或未来规模必然延续当前趋势 |

这些信号必须按 `run / checkpoint / step / data batch / rank` 对齐。一次 loss spike 与同一步的 gradient spike、异常 batch、loss-scale backoff、collective retry 或 device error 相关联，才可能把“现象同时发生”推进到可检验的根因假设。只看全局平均会把单个 domain、layer、rank 或 expert 的退化稀释掉；只看最细粒度指标又会产生噪声和监控成本，因此应保留 global trend、分层 slice 与按事件下钻三档视图。

判断是否值得继续投入剩余训练预算，还需要预先定义 gates，而不是在曲线出现后解释：相对小规模或先前 run 的 loss/token 轨迹是否落在容差带内，held-out quality 是否随 compute 改善，关键能力是否回退，数据与系统异常是否已被解释，最近 checkpoint 是否通过 restore/continuation canary。通过这些 gates 只能说明“当前 trajectory 仍值得继续”，不能证明最终模型一定优秀；最终结论仍属于独立 Evaluation。

### Elastic Recovery 的目标不是“重新跑起来”

超大规模训练把故障恢复从 process restart 提升为 trajectory correctness。若坏掉的 accelerator
被替换、slice 重新划分或 collective group 重建，平台还要回答：重新开始的 step 是否消费了
同一批 tokens，optimizer/scheduler/RNG 是否来自同一提交点，以及疑似 silent corruption 之后
哪些 step 必须回滚。

```text
detect fault or corruption
→ choose last validated commit point
→ restore model / optimizer / scheduler / RNG / data cursor
→ rebuild topology and shards
→ deterministically replay or explicitly start a new trajectory
```

传统的固定 topology checkpoint 仍然合理：它的状态映射简单、恢复路径更容易验证。Elastic
slice replacement 用更高的 resharding、replay 与一致性复杂度，换取长时间训练对频繁硬件故障
的容忍。公开技术报告可以证明这种 resilience contract 已进入 frontier training system，但不能
在没有 checkpoint continuity、data cursor 与 RNG 细节时断言 bitwise exact recovery。第 35 章
拥有持久状态，第 36～41 章拥有 topology/runtime；本章只规定恢复后不能静默改变训练语义。

### 自主训练控制必须被 Safety Envelope 包围

固定 learning-rate schedule、gradient clipping 和人工停机容易复现，也是默认基线；在长时间训练和运行时 stress 下，它们对突发 spike、degraded run 或资源浪费反应较慢。optimizer 之上的 control layer 可以读取 versioned telemetry，提出调低步长、暂停、回滚等 bounded actions，但 action budget、cooldown、approval 与 human override 必须由训练控制面持有。

收益是更快限制损失扩散和无效 compute；代价是 controller 误判、观测延迟、控制振荡以及对 telemetry 的新依赖。证据不足、动作越界或 controller 自身异常时，应恢复静态 recipe/停止训练，而不是自主扩大权限。exact-v1 只支持其披露 simulator/recipe 与 stress runs，不证明真实超大规模训练的稳定性、效率或最优控制策略。

<!-- source-family:SF-2026-ARXIV-2605-19008 -->

### 超多 Epoch 训练会把单一 Checkpoint 演进为模型群体状态

数据充足时，沿一条 optimizer trajectory 持续更新单个 checkpoint，拥有最简单的 lineage、恢复和部署语义；当 unique data 已固定、训练仍要跨越大量 epoch 时，后期 checkpoint 可能只是在同一数据上继续偏移，而不是稳定增加可迁移能力。此时一种实验性分支不急于把历史状态压成最后一个模型，而是在训练过程中冻结多个 snapshot，并把它们视为带 lineage 的 population：后续 snapshot 可从前序成员蒸馏，held-out evidence 决定成员权重，部署侧再按推理预算选择单成员、少量成员组合或蒸馏后的单模型。

```text
unique-data revision + optimizer trajectory
-> immutable population snapshots
-> chain-distillation lineage
-> held-out prior / member admission
-> inference-budget-specific member set
```

这条分支用更多 teacher forward、snapshot 存储、held-out 选择状态和多成员推理成本，换取不把重复 epoch 的全部知识压在一个终点上；它也新增成员相关性、selection overfit、lineage 漂移和 serving 成本失控。population controller 只拥有成员选择，不能把训练集重用或成员一致性当成泛化证明。held-out prior 不稳定、部署预算只允许一次 forward，或成员组合没有超过 matched 单模型时，应回退单 checkpoint，或把群体重新蒸馏成一个可独立验证的模型。

`arXiv:2606.03938v1` 只在 1.8B 模型、100M FineWeb tokens 与披露的高 epoch 设置中支持 snapshot population、chain distillation 和 held-out weighting 的组合；它没有证明 frontier-scale data/model、真实 serving cost 或蒸馏后仍保留全部增益。

<!-- semantic-body-binding:SF-Q0-HYPER-EPOCH-PRETRAINING -->

## Mid-training：能力生产链中的独立阶段

Tool-use mid-training 不应只把 API 文档拼进语料。数据单元需要同时包含 tool schema、调用 proposal、可执行环境 transition、result/receipt 与失败修复，并把模拟或生成轨迹先通过 schema、执行和 outcome verifier；否则模型学到的是看似正确的调用文本。该阶段能在大规模训练中建立 affordance 表示，却不授予运行时权限，真实 effect 仍由 Agent runtime 控制。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20314 -->

把 pretraining 直接接到 SFT/RL，边界清晰且便于归因；但长上下文、特定领域或推理能力若在基础表示中
尚不可达，post-training 往往只能改变行为而难以重建底层能力。Mid-training 在通用预训练之后继续使用
大规模 language-model objective，却有目的地调整数据 mixture、长度或难度，再交给 SFT/RL：

```text
general pretraining
→ targeted mid-training
→ retention / context restoration
→ SFT and outcome-driven specialization
```

它不是一个可随意命名的“中间 checkpoint”。阶段 identity 至少包含入口 checkpoint、数据与长度分布、
objective、token/compute budget、merge/retention policy 及出口 evaluation。定向数据能提高目标能力，也会
造成通用能力回退、污染或难度过滤器过拟合；因此需要与继续通用 pretraining、直接 SFT/RL 做 compute-
matched 对照，并保留 restoration 分支。目标分布小、demonstration 可信时直接 SFT 仍更便宜。

长上下文继续预训练的停点也不能只看一次 Needle-in-a-Haystack（NIAH）命中：定位显眼证据可能很早饱和，而对长距离条件分布的拟合与后续任务仍在变化。训练控制器应在同一 checkpoint 轨迹上同时看长度分层的 held-out perplexity、固定配方的轻量 SFT probe 与检索头等内部诊断，再用目标任务决定是否值得继续；检索头只提供 sensor，不拥有停训 authority。多路监测增加 probe 训练和评测成本，也可能把单一模型的数据配比、长度和指标偏差误当普遍规律。作者的 Hunyuan-A13B、32K→64K、200B-token CPT 支持“NIAH 饱和≠训练收敛”这一受限反例，不提供所有模型共用的 token 停点；短上下文或目标只需简单定位时，NIAH 仍是便宜的 smoke test。<!-- source-family:SF-2026-ARXIV-2604-02650 -->

这里的数据 mixture 通常在训练前固定：方案易复算，但一旦目标权重选错，就要重跑昂贵的 CPT。若几个目标分布
可以从同一基础 checkpoint 分别训练，一条条件分支是先保存各分布的参数更新，再在冻结的开发集上搜索更新
向量的组合权重，最后用独立 holdout 决定采用哪个合成 artifact。它把 mixture 的部分决策权移到训练之后，
让同一批更新可面向不同目标重选，却没有消除各分布模型本身的训练成本，也把参数干扰、额外权重存储和
开发集过拟合带进发布 Gate。分布更新不相容、目标频繁变化或独立验证失败时，预先混合训练仍是更直接的基线。
现有证据只支持作者在 Gemma 3 27B、多语言/数学/代码 CPT 与所测搜索协议下的比较；所谓搜索提速不等于
端到端预训练提速。<!-- source-family:SF-2026-ARXIV-2603-28858 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-02087:start -->
行为规范也可以在这里成为显式训练资产。只在后续 SFT 中提供少量“应该怎样回答”的 demonstration，数据便宜但规则往往欠指定，模型可能把表面动作泛化到错误场景；在 mid-training 先同时学习 spec 的内容、适用条件与 rationale，可以让后续 alignment example 被解释为某个版本化 policy 的实例，而不是孤立答案。

```text
versioned behavior spec corpus
→ mid-training on rule, rationale and boundary cases
→ demonstration / preference alignment
→ held-out conflict and underspecification evaluation
```

spec corpus 由 policy owner 管理，training run 只产生候选 weights；模型理解 rationale 不等于始终遵从，更不等于规则正确。该分支用额外 token、policy version coupling 和 mis-specification/poisoning surface 换更一致的归纳偏置。synthetic specs、有限模型和窄 alignment setting 不能证明普遍价值对齐；规则频繁变化、需要立即撤销或高风险授权时，运行时 policy 与 deterministic enforcement 仍不可替代。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-02087:end -->

### Skill Artifact 是结构化能力数据，不是行为证明

普通语料提供描述，trajectory 提供一次执行过程；带接口、步骤、前后置条件和 reference 的 skill artifact 位于两者之间。
把它加入 targeted pretraining 可以让模型更早接触可组合的能力结构，但 artifact 被读入 weight 不等于能力已在真实环境中
成立。训练 identity 至少还要保存 skill source、license、版本、适用环境、依赖、coverage 与去重关系，并把执行验证留给
后续 SFT/RL/Evaluation：

```text
versioned skill artifact corpus
→ capability-structured pretraining signal
→ trajectory / environment post-training
→ executable evaluation and adoption
```

收益是减少纯自然语言描述与执行轨迹之间的结构缺口；代价是 skill 质量不均、过时接口、数据污染与虚假可执行性。
当 skill corpus 小、provenance 不清或真实 demonstration 充足时，直接用经过验证的轨迹仍更可靠。

### 相同阶段终点不代表相同后续可训练性

Checkpoint 是否适合下一阶段训练，不能只由最终 loss 或 post-SFT benchmark 判定。两个分支即使在 SFT 后几乎同分，只要进入 SFT 前的最后 pretraining window 不同，面对同一 DPO 或 RL update 仍可能沿不同轨迹移动。因此 artifact identity 还要保存 ordered data window、入口 checkpoint、token budget 与后续 update reference，并比较 stage-wise erosion / retention，而不只看终点。

这项结论来自小模型、500M-token 受控 intervention 与特定 refusal 指标，不支持“把某类数据最后训练”的通用 recipe。它增加 lineage、matched downstream update 和能力 retention 的评估成本；在 saturated scale、其他能力或更大模型上必须重新验证。若后续阶段弱、窗口差异可忽略或 lineage 成本过高，按阶段终点评估仍是合理基线。

对于事实少、表述重复的 continued pretraining，另一条分支只扰动 conditioning input，而保持原始 next-token label：以 `s_t` 为目标时，用随机 mask 或 vocabulary replacement 得到的 `s̃_<t` 替代原 prefix，仍优化 `-log p(s_t | s̃_<t)`。这增加同一材料的输入变化，不是把脏文本同时当作新标签，也不是双向 masked-token reconstruction；随机重采样更不保证输入永不重复。它以噪声强度、语义信息损失和额外验证成本换取减少表面依赖的机会，必须检查 held-out 知识、通用能力与任务表现。简单 mask/random 分支不需要生成 paraphrase 的 teacher，但不能推广为所有增强变体都无外部模型；paraphrase 仍可互补。[KItCAT v1 §3–5](https://arxiv.org/html/2609.00082v1)只提供特定语料和模型的 QA-judge 证据，不证明 API 执行正确，也不把估算 FLOPs 当作实际时间收益。

另一个不同目标的分支是让 mid-training objective 从随机 token/span corruption 进一步利用程序结构：先抽取 function、dependency 或
call boundary，再要求模型重建被遮蔽的实现与接口。随机遮蔽在通用语料、解析器不可靠时覆盖更稳；结构感知
reconstruction 在代码依赖可恢复时能把训练压力集中到跨段语义关系：

```text
random token / span corruption
→ syntax-bounded masking
→ dependency-aware function reconstruction
→ behavior post-training and executable evaluation
```

收益是更直接地训练跨函数依赖，代价是 parser、language、teacher、repository sampling 与 corruption policy 都
进入数据/objective identity。重建成功也不等于生成的程序正确，更不证明该 objective 跨语言或跨 domain 优于
next-token baseline；必须保留未见 repository、可执行测试和通用能力 retention。解析失败、自然语言主导或目标
能力可由可信 SFT 提供时，随机 objective 仍是更便宜的旧方案。

### 稀疏长上下文预训练可以在末期恢复为稠密部署 Artifact

全程 dense attention 最接近部署语义，却让长上下文训练承担完整二次成本；永久稀疏又要求推理 runtime 接受不同模型
结构。Training-only 的中间分支可以在大部分训练阶段用多分辨率 Q/K/V 金字塔选择少量位置，经 gather→FlashAttention
→scatter 完成更新，随后在同一 optimizer 与 dataloader identity 下切回 dense SDPA 做 recovery。最终 artifact 恢复
稠密结构，训练期 selection state 和恢复步数则必须进入 run lineage。

它用训练吞吐换来 selection bias、稀疏 kernel/gather 开销和 recovery 不充分风险；末期 dense loss 恢复也不自动证明
所有长上下文能力被恢复。应比较等 token/compute 的 dense baseline，报告选择率、恢复曲线、长上下文切片和目标硬件；
现有证据绑定作者的长上下文模型与 B200 环境，也不覆盖 autoregressive decode。上下文较短、选择开销不可摊销或部署
前无法完成 dense recovery 时，全程 dense 仍更可靠。<!-- source-family:SF-2026-ARXIV-2605-06554 -->

### Tool Affordance 可以在 Mid-training 建立，但不授予 Authority

通用 pretraining 只从文本统计间接学习工具概念，SFT/RL 才看到少量完整调用轨迹。中间分支可以从 API、MCP schema、代码和文档构造 workflow supervision，提前学习 tool selection、argument grounding 与 recovery prior，再交给后训练校正行为。

它减少后训练冷启动，却会固化 synthetic schema、工具分布和文档偏差。learned affordance 只说明模型会提出调用，真实执行仍由 runtime schema、authorization 与 postcondition 决定；数据 provenance 不可靠或目标工具快速变化时，保持到 SFT/RAG 阶段注入更容易更新。

### Continual Pretraining 可以减少 Replay，但不能宣称消除遗忘

replay buffer 通过重看旧样本维持能力，直观且可验收，却增加数据存储、权限和重复计算。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15053:start -->
TFGN 提供的是无 replay、无 task ID/phase boundary 的 internal overlay：forward read 保持 dense，task-driven update signal
被结构性地导向不同 trainable subspaces。它试图在网络内部减少新任务更新对旧能力的干扰，但 overlay 只拥有 update
proposal；最终 checkpoint 仍需分别验收 acquisition、retention 与 transfer。代价是额外 capacity/compute、内部状态身份
和无法独立检查的实现边界，论文还明确说明关键 lever/specification 受 NDA 限制，因此不能把它改写成已公开的“新旧任务
梯度分量分解器”。旧数据可合法保存、内部机制不可审计或 retention 回归时，replay、regularization 与独立 adapter 仍是
更稳妥的 fallback。现有证据只覆盖作者任务与实验设置。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15053:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09608:start -->
顺序 fine-tune 或 replay 默认把新更新视为可以直接累积，在任务相容时清楚且可复现；但同一个 update 相对于当前 model state 的 covariance geometry 可能与既有能力方向冲突。Training owner 因而要把 task update、起始 checkpoint、geometry probe 和校正策略一起版本化，merge Gate 只提交已证明相容或经过约束修正的更新；artifact/rollback 仍由第 35 章接手。

Geometry proxy 提供的是干扰诊断，不是遗忘的普适因果证明；barycenter 或投影校正还会增加计算、探测误差和可塑性损失。现有证据限作者披露的模型、task sequence、optimizer 与 evaluator。冲突估计不稳定、任务确需改变旧子空间或审计成本过高时，应回退 replay、独立 adapter，或保留原 checkpoint 作为可恢复分支。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09608:end -->

保护旧任务方向的梯度投影或 replay 混合，还会与 Adam 的状态更新相互作用。若衰减后的梯度同时进入一阶矩和二阶矩，旧方向的二阶幅度估计也被压低，分母变小可能反而放大该方向的有效步长；“投影更强”因而不等于“旧能力受保护得更好”。训练验收应把原始梯度、实际用于更新方向的梯度、两路 moment 输入和旧任务 retention 分开记录，并用固定一阶矩、只改变二阶分母的对照定位失效，而不是仅看最终平均 perplexity。一个条件性修复让修改后梯度进入一阶矩、原始梯度提供二阶幅度统计，再按新旧梯度子空间重叠调保护强度。<!-- source-family:SF-2026-ARXIV-2604-22407 -->

双路由本身不是通用配方：重叠较高时固定强度保护在作者的受限设置中甚至劣于未保护基线，需要连同 overlap-aware schedule 验收；任务确需改写旧方向、旧梯度不可合法保留或额外低秩基估计/缓存成本不值得时，replay、独立 adapter 或原 Adam 路径仍可作为回退。原文的有效学习率比例来自单方向标量 surrogate 和特定 epsilon 区间，不是逐坐标 Adam 定理；实验只覆盖披露的 256M HOPE 域序列与 7B LoRA 等任务边界，不能保证无边界长期训练、超大模型或其它 optimizer 都受益。<!-- source-family:SF-2026-ARXIV-2604-22407 -->

## Pretraining 没有解决什么

Next-token training 可以形成广泛能力，却不直接规定模型应如何响应用户。互联网文本包含描述、争论、错误和危险行为；“预测文本分布”与“遵循意图”不是同一目标。

因此后续能力生产分成几条路径：

```text
Pretraining  learn broad conditional structure
SFT          imitate desired demonstrations
RLHF/DPO     optimize relative preferences
LoRA         parameterize a cheaper task-specific update
```

这些阶段可以增加、改变或损伤已有行为。Post-training 不是给模型添加一个无风险 UI 层，而是在继续修改参数分布。

## 本章在知识树中的位置

```text
versioned data q(x)
-> causal next-token loss
-> gradients and optimizer state
-> repeated parameter updates
-> pretrained checkpoint
-> SFT / LoRA / preference optimization
```

第 27 章决定训练分布，本章决定基础 objective 与训练循环；第 29 章将目标收窄到指令 demonstrations。第 35～41 章再解释这段循环怎样被持久化并扩展到多 GPU。

在 Compute 横线上，第 14、17 章定义的 operator graph 到这里第一次成为反复执行的 training workload；第 37 章继续把单个 operator step 分布到多个 devices。这个连接属于执行映射的逐层展开，不表示训练 objective 与 Tensor Parallel 是同一层设计。

## 从机制演进到系统设计

预训练优化最初用统一 optimizer 与全局 learning-rate schedule 管理所有参数；规模扩大后，width、depth、token budget、batch、warmup 和参数方向的敏感度发生非线性交互。因而 learning rate 不应按层数机械动态调整，而应先以 matched probe 判断哪些方向或尺度真正触及 stability boundary。

局部 spectral probe 或邻近规模 sweep 可以减少统一步长的过保守与过激，却增加测量噪声、控制状态和额外训练成本。任何外推都必须冻结 data、optimizer、schedule、precision 与 token budget；超出验证尺度时重新校准，而不是把局部幂律当成普遍规律。统一 schedule 在观测不足或收益不覆盖复杂度时仍是 canonical baseline。

## 自检问题

1. Next-token loss 怎样从 `[B,T,V]` logits 与 `[B,T]` labels 得到？
2. 小例子中 target probability 提高为什么会降低 loss？
3. Perplexity 跨 tokenizer 比较为什么可能无效？
4. `B_global`、effective tokens 和 optimizer steps 有何区别？
5. Gradient accumulation 节省了什么，没有节省什么？
6. Warmup、decay 与 gradient clipping 分别约束什么？
7. Mixed precision 为什么不能由一个 dtype 名称完整描述？
8. Activation checkpointing 与 training checkpoint 有什么不同？
9. Loss 下降为什么不直接证明事实可靠或指令遵循？
10. Pretraining 状态为什么不仅包含模型权重？
11. 两组参数表达同一个函数时，为什么 Adam 仍可能产生不同的 function-space trajectory？
12. 为什么 forward output 的量化误差可接受，不代表同一精度也适用于 backward 的弱梯度？
13. 如何区分真正的低比特收敛证据与被 batch noise 或较短 training horizon 掩盖的偏差？
14. 为什么允许 test-time sampling 后，early stopping 必须绑定 deployment volume、verifier 与 SLO？
15. Adam 的 per-coordinate adaptation 为什么不等于显式的逐层 learning rate？
16. 哪些 evidence 才足以支持 fixed 或 dynamic layer multiplier？
17. Mixed precision 与 distributed accumulation 下，gradient clipping 应在什么语义边界执行？
18. Training loss、gradient、数值、数据、系统与 Evaluation 信号分别能排除什么，又不能证明什么？
19. 为什么超长训练的 continue/stop gate 只能判断 trajectory 是否仍值得投入，不能担保最终模型质量？

## 小结

Pretraining 用大规模 next-token prediction 把数据分布转化为参数更新。Cross-entropy 定义局部误差，optimizer 与 schedule 决定更新轨迹，参数块对称性限定哪些更新在重参数化后仍应等价；batch、precision、activation memory 和分布式执行决定这条轨迹能否在可接受成本内完成。

固定 recipe 是可复现基线；长程 stress 下可以增加受 safety envelope 约束的控制层，但它只能提出有界动作，不能替代训练目标与人工 override。预训练 checkpoint 是通用能力底座，不是最终产品行为；它是否可靠还需要独立 Evaluation 与后续训练约束。

## Review notes

- `SF-2026-ARXIV-2603-09697` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09697v1) exact-v1必要§3–6/Algorithm1/A.1–2/C.1；2+1+2=5，双边谱预条件接口差额深入。root实际S3/Alg1/S4/S5/S6/C1、原日期及Ch28 548–577/27、29交接与逐字PRE通过；固定metric LMO不混Frobenius、finite NS/tempering/graft，small-spectrum噪声/初始化与完整费用保留。作者按窄锁写后回对必要原证，root非writer实际顺读新正文、完整局部邻接与本注并回对必要原证，actualPOST通过，窄锁释放，不授全图/代码/复现或DAY。

- `SF-2026-ARXIV-2601-04890`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04890v1) §2–4/§5/Table2及必要B/C。采用矩阵noise–WD norm与learned effective scale分责、gauge/低精度/共享clip耦合；不授μP普遍失效、所有层scale锁死或所有任务改善。Falcon-H1-0.5B、30/240GT与LR search限定，Muon MMLU/LMhead反侧保留，hardware/总wallclock未充分披露。日作者必要证据/实际owner差额PRE，root实际源与参数化完整邻接核后写两段；非写入者 `audit_jan02_root_evidence` 已实际顺读正文、完整邻接和本注，POST通过，未核artifact/复现，非日级完成。

- `SF-2026-ARXIV-2602-22543` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22543v1)，sharedprefix固定depth family/branchCE与zero-output identityinit。2+2+2=6，具体owner差额深入；限制、反侧、完整费用与原分支回退近正文。root实际必要原源/owner PRE通过并授单段窄lease；作者正文/完整邻接/自身末注已顺读，root非作者实际正文/完整邻接/自身末注POST通过。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-18131` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18131v1) §3/Eq12–13、§4.3必要setup/results及多层限制。2+1+2=5，历史influence matrix与inferred-state local Jacobian的时间credit分支差额深入；理想收敛/PC与BP目标、4.3M LRU/frozenFastText曝光与成本条件近正文，不授节能或ZO演进。root必要源/actualowner PRE通过并授窄锁；作者实际正文/完整邻接及自身末注顺读、限定diff-check通过，root非作者实际正文/完整邻接及自身末注POST通过，锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-06183` — Daily `2026-02-10`；[exact-v1](https://arxiv.org/html/2602.06183v1) §3/Algorithms1–3、§3.2、§4、§5.1–5.2及关键表。6=2+2+2标准审阅，root 必要原源与具体 owner 写前核通过；采用 FFN sparse operand/物理 pattern 与 sparse→dense recovery 分工，不采 headline 倍数。微核/roofline 是估算而非完整 training E2E，cluster 距离表述与伪代码差异不作实现核验，Blackwell 搬运优化未实测；root 实际正文/邻接及源注非作者POST通过，日级Gate未授，未复现实验。

- `SF-2026-ARXIV-2601-08393` — Daily 2026-01-15；[SSO exact-v1](https://arxiv.org/html/2601.08393v1) §3/Eqs8–14、§4–7/Table1–3。2+2+2=6，一阶Frobenius切向求根与有限步exact双侧分支gap深入；不授每一时刻严格谱不变量或普遍稳定。下一步前radial校正、数值tol、B200单步成本、MuonSphere反侧保留；未复现。root必要源/owner写前通过，root已实际核正文、前后邻接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-01306`：[Muon++ exact-v1](https://arxiv.org/html/2601.01306v1) §3.1.1、4.2–4.3、5.1–5.2。采用 unique-top、双侧正交补和步长≤谱隙条件下的最大谱范数保持，以及超宽 rescale 改变净更新的边界；未采用 §4.4 的额外统计 recipe，不授普遍 μP transfer、收敛或实测效率。3+1+2=6、具体设计边界深入；root 非作者必要源与 owner 提案复核通过，root 非作者实际正文、邻接与末注写后复核通过；未运行实现。

- `SF-2026-ARXIV-2601-00781`：[ReDGE exact-v1](https://arxiv.org/html/2601.00781v1) §3.2–3.4、§4.1/Runtime、Appendix A.1 的 A1–A2 假设，Daily 2026-01-06，2+1+2=5，因确认离散训练梯度接口知识缺口深入必要命题。只采用解析后验/有限 transport/梯度 proxy 分账及有条件的小时刻退化；每次估计 single f evaluation，增加 f-independent sampler overhead。§4 与 §3/Fig1 schedule 方向冲突不采复现配方，局部运行时间不是通用收益；root 必要源→owner 与实际正文/邻接写后复核通过；未复现实验。

- `SF-2026-ARXIV-2609-37852` — [Delta-Matching v1](https://arxiv.org/html/2609.37852v1) §3/Eq.2/4、§4、Appendix A.4；Daily `2026-09-30`。只整合 stale saved-delta 与当前 backward contraction 的不变量失配；pre-quantization zero-row-sum 不等全部梯度无误差、任意收敛或端到端提速。未复现实验，root非作者实际写后及相邻衔接复核通过。
- `SF-2026-ARXIV-2609-37899` — [SOMA v1](https://arxiv.org/html/2609.37899v1) §3–9/Eq.3–4；Daily `2026-09-30`。独立 objective 消除 cross-expert SPSA noise，以冻结共享部分和表征分离为前提；理论仅 stated separability/smoothness/probe 假设，byte-LSTM 局部实验不外推大 Transformer。未复现实验，root非作者实际写后及相邻衔接复核通过。

- `SF-2026-ARXIV-2604-22407`：[exact-v1](https://arxiv.org/html/2604.22407v1) §3–5、Table 3/6、Limitations；Daily 2026-04-27。保护性梯度修改与 Adam 二阶矩同路造成有效步长反增；固定一阶矩 denominator 控制和高重叠 fixed-OGP 反例均保留，不能把单方向 surrogate 当逐坐标保证。raw-to-second / modified-to-first 需与 overlap-aware schedule、低秩基/缓存成本一同验收；受限 HOPE 域序列与 7B LoRA，不作超大模型和无任务边界保证。root 已通过必要源→当前 owner 采用核，实际正文与相邻交接写后非作者复核亦通过；未复现实验，不代表日级验收。

- `SF-2026-ARXIV-2604-21106`：[official PDF v1](https://arxiv.org/pdf/2604.21106v1) §2–6/App A；Daily 2026-04-24。仅吸收独立参数量与执行深度、训练 FLOPs/tokens 分账及条件性 scaling 前沿。二十个有效 block、full BPTT、六预算/116 runs 和所测 dense 前沿仍优的反例保留；不把局部拟合指数、权重内存降低外推为 wall-clock/SLO 收益。root 已完成必要源→当前 owner 写前及实际正文/相邻衔接的非作者写后复核，通过；未复现实验。

- `SF-2026-ARXIV-2604-19033`：[exact-v1](https://arxiv.org/html/2604.19033v1) §3–6/Eqs. 3–16/Algorithms 1–3、§7.3/7.5–7.7/Tables 1–3；Daily 2026-04-22。仅吸收 streaming RL 中既定更新方向的局部输出步长计量及 trace 单位，与完整 batch-Jacobian 反解分开。分母不稳、action-dependent 方向偏差、大步非线性和受测任务反例保留；不外推 LLM 预训练、hard KL cap 或无偏 policy gradient。未复现实验；root 已对 exact-v1 与本次正文及邻接完成非作者写后复核，通过。

- `SF-2026-ARXIV-2604-15416`：[StoSignSGD v1](https://arxiv.org/html/2604.15416v1)，Daily 2026-04-20；§2/§3.1–3.2、B.2/Table10–12。采用正包络内随机 sign 保留预条件期望；保历史尺度漂移、方差、zero handling 和特定 FP8 state underflow 条件，不采用摘要精确 speedup 或普适理论排名。apr02 必要 source→实际 owner 独立采用通过；root 实际正文与相邻衔接非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-15554`：[Natural gradient descent with momentum v1](https://arxiv.org/html/2604.15554v1)，Daily 2026-04-20；§3.3–3.4/§4.2.1 Eq24–28、§4.2.2 Eq29–30、§4.2.3 Eq31–33、§5.1–5.3/§6。采用变化tangent中的历史函数动量重新投影，不称精确parallel transport；QNHB局部近似、FD/line-search成本及发散反例保留，不恢复PDE领域应用或LLM普遍加速。apr02必要source→当前owner独立采用通过；已实际写入正文，root实际正文与相邻衔接非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-14769`：采用 exact-v1 §III/Eq6–13/IV；复用 NINE_FINAL §4 的有效必要源审和 root 当前 owner 反向采用核。仅增主动模板预训练/目标适配分支，与 checkpoint 扩容共存；未复现，root已实际顺读正文及两侧交接，写后PASS。

- `SF-2026-ARXIV-2604-13627`（Status: Experimental）：官方 exact-v1 §3–5/Limitations；同 SFT loss 的 LR/参数漂移对照与预训练 cooldown/sharpness 相关性分账。后者作者明确未建立因果，未采用普遍避免预训练 decay 建议；实际新增 schedule→SFT 交接两段，待非作者写后核。https://arxiv.org/html/2604.13627v1

- `SF-2026-ARXIV-2604-11912`，Experimental：[exact-v1](https://arxiv.org/html/2604.11912v1) §3–5.3、Limitations、E.1–E.3。采用parallel future-token辅助loss的梯度路径解释，理论限两层disentangled、固定block读头、content零初始化/Toeplitz与两阶段gradient flow；不作sequential MTP、任意联合训练或推理速度保证。有限stargraph/binarytree/Countdown/SAT结果与budget、checkpoint selection边界保留；根任务必要源/owner准入和实际正文/相邻衔接的写后独立复核通过，未复现实验。

- `SF-2026-ARXIV-2604-07663`：[SAGE exact-v1](https://arxiv.org/pdf/2604.07663v1)，核 Algorithm1/§3.1–3.4、§4.1–4.4/Table2/AppA.2。meanabs列共享统计、instant/EMA RMS阻尼、完整momentum仍为O(Vd)，新scale为O(d)；dense Unit-Norm SinkGD另有尺度配对变化，1D使用SAGE/AdamW在设置叙述中并不完全统一，不采用单因素归因。H200、LLaMA270M/.6B/1.3B、6.6B ThePile子集、seq512/global130Ktokens/bfloat16/三seed均值；.6B全参数Lion26.58略优SAGE26.71，Lion-Hybrid为28.73，纯SAGE与纯SinkGD失败。≤1步长不推出方向或stationarity，Theorem3.3只给proof sketch且无此关键桥，不采用通用收敛/安全保证。root已核其余必要原文与正文，本次按其发现修正Lion基线身份，未复现实验。

- `SF-2026-ARXIV-2604-07380`，Experimental：[exact-v1](https://arxiv.org/html/2604.07380v1) §2–6、§9、§10.4。采用同checkpoint后期decay干预与线性/非线性读出、任务行为的分账；150K Dyck/1.5M SCAN、三seed、W=5 attention更新SVD。Table1的WD0与WD1为accuracy .973/.982、linear R² .987/.851，不写行为严格等价。§3.2与Table2的阶段梯度比例不合并；2D移除与小扰动非同幅、随机对照仅同维数，不采普遍grokking因果机制或frontier schedule建议。root非作者对必要原文、实际正文与相邻decay论证核对通过；未复现实验。

- 2026-09-01 optimizer 逻辑块与物理 fusion：<https://arxiv.org/html/2608.30320v1> §3.1。仅采用 fused QKV/GDN head、gate/up 拆合与分模块 optimizer 的受限机制；较高LR stress、小模型消融及大模型生产不是同一对照，不采跨架构稳定性或kernel速度保证。

- `SF-2026-ARXIV-2604-22753`（Status: Experimental）：exact-v1 支持把 scaling-law fitting 写成 heterogeneous-cost、target-region-aware 的 sequential experiment selection；mixture approximation、one-step policy 与 cost proxy 限制其外推。https://arxiv.org/abs/2604.22753v1

- Skill Pretraining（structured capability artifact as mid-training data；Status: Experimental）：
  https://arxiv.org/abs/2608.26563v1
  - 证据边界：作者构造与模型实验支持 skill artifact 作为训练信号；不证明数据中的接口可执行、跨环境迁移或
    可取代真实 trajectory / verifier。

- Spectral Allocation / SAMuon（direction-aware optimizer step allocation；Status: Experimental）：
  https://arxiv.org/abs/2608.25990v1
  - 证据边界：当前证据来自论文披露的 124M、300M、1B 规模和有限 batch/任务；不证明 frontier-scale
    训练、不同架构或任意数据分布都应采用相同 head/bulk profile。

- Final-window pretraining lineage and downstream-update response（matched post-SFT endpoint 不等于同一可训练性；Status: Experimental）：https://arxiv.org/html/2607.25063v1

- GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries（arXiv:2607.20757v1；Status: Experimental）：https://arxiv.org/html/2607.20757v1
  - 证据边界：支持两个模型、短 continued-training 设置中的 learned symmetry basis 与 fake-quantization perplexity；不证明端到端速度、硬件支持、完整预训练稳定性、通用低比特鲁棒性，或 proxy 会最小化真实 quantized loss。

- Structure-aware function reconstruction mid-training（Status: Experimental）:
  https://arxiv.org/abs/2607.12463v1

本章只负责 next-token objective、训练 step、token/batch 计量、optimizer state 与训练稳定性。数据治理留在第 27 章；SFT 和 preference optimization 留在第 29、31～34 章；collective、state sharding 和 framework runtime 留在第 36～41 章。

2026-W10 的 SageBwd 案例用于补全 backward sensitivity、precision boundary 与 convergence contract。
其公开实验仍限于作者的小模型与固定训练设置，相关 repository 也未定位到可核验的独立实现；因此
正文不保留吞吐数字，也不把该 precision partition 写成通用 recipe。

Progressive Residual Warmup 用于补足 residual branch activation 的 `layer × time` 状态与恢复边界；其固定 schedule、训练规模和稳定性结果只作为 Experimental evidence。

本轮训练健康审计把 objective、update、numerical、data、system 与 Evaluation 信号分层，并明确 continue/stop gate 的证明边界；指标集合参考 Megatron Core 当前官方 observability contract，但正文不把某一框架的 metric 名称写成通用标准。

Primary-source 校验入口：

- Diederik P. Kingma, Jimmy Ba, "Adam: A Method for Stochastic Optimization", 2014: https://arxiv.org/abs/1412.6980
- Yang You, Igor Gitman, Boris Ginsburg, "Large Batch Training of Convolutional Networks", 2017（LARS）:
  https://arxiv.org/abs/1708.03888
- Yang You et al., "Large Batch Optimization for Deep Learning: Training BERT in 76 minutes", 2019（LAMB）:
  https://arxiv.org/abs/1904.00962
- Jeremy Howard, Sebastian Ruder, "Universal Language Model Fine-tuning for Text Classification", 2018:
  https://arxiv.org/abs/1801.06146
- PyTorch AMP gradient clipping example:
  https://docs.pytorch.org/docs/stable/notes/amp_examples.html#gradient-clipping
- NVIDIA Megatron Core training metrics（版本化 instrumentation evidence）:
  https://docs.nvidia.com/megatron-core/developer-guide/nightly/user-guide/observability/metrics.html
- Alec Radford et al., "Improving Language Understanding by Generative Pre-Training", 2018: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
- Tom B. Brown et al., "Language Models are Few-Shot Learners", 2020: https://arxiv.org/abs/2005.14165
- Jared Kaplan et al., "Scaling Laws for Neural Language Models", 2020: https://arxiv.org/abs/2001.08361
- Jordan Hoffmann et al., "Training Compute-Optimal Large Language Models", 2022: https://arxiv.org/abs/2203.15556
- Gemini 2.5 Technical Report（training-resilience bounded case）:
  https://arxiv.org/abs/2507.06261
- Devender Singh, "The Loss Does Not See the Basis, but Adam Does"（Status: Experimental）:
  https://arxiv.org/abs/2608.05136
- Jintao Zhang et al., "SageBwd: A Trainable Low-bit Attention", 2026（Status: Experimental；公开实现尚未定位）:
  https://arxiv.org/abs/2603.02170
- Progressive Residual Warmup（Status: Experimental）: https://arxiv.org/abs/2603.05369
- CompleteP（depth-wise HP transfer 与 non-lazy feature learning 的联合 parameterization contract；Status: Experimental）：https://arxiv.org/html/2505.01618v1
  - 证据边界：12%–34% 只属于作者模型形状、training recipe 与 Cerebras CS-3；不推出逐层动态 learning rate 的普适方向。
- SkewAdam / Tiered Optimizer State（exact v1 + event-time commit；Status: Experimental）：https://arxiv.org/html/2607.19058v1
  - 证据边界：6.78B total / 440M active、128 experts、约 81.9M tokens，H200 为主且有 H100/MI300X follow-up；不证明大规模 distributed wall-clock 或普遍收敛。
- FLOP-Efficient Training / TTC-aware Early Stopping（Status: Experimental）:
  https://arxiv.org/abs/2601.01332
- ECO Quantized Training（optimizer-state error feedback；Status: Experimental）:
  https://arxiv.org/abs/2601.22101
- SOLO（低比特 optimizer EMA 的动态误差与 precision-specific momentum；Status: Experimental）：
  https://arxiv.org/html/2505.00347v1
  - 证据边界：受限模型与训练设置中的 2-bit Adam-state 结果不覆盖所有 optimizer、长 horizon、分布式 checkpoint 或故障恢复；高精度 state 仍是稳定性基线。
- Quartet II（FP4 rotation/debiasing computation graph；Status: Experimental）:
  https://arxiv.org/abs/2601.22813
- ARO（optimizer update 的 adaptive rotation；Status: Experimental）:
  https://arxiv.org/abs/2602.09006
- Magma（dense optimizer state + masked parameter application；Status: Experimental）:
  https://arxiv.org/abs/2602.15322
- Learning What to Predict（feedback-guided self-supervised task construction；Status: Experimental）:
  https://arxiv.org/abs/2601.22108
- SPARKLING（state-aware width expansion；Status: Experimental）: https://arxiv.org/abs/2602.02472
- PRISM（targeted mid-training stage contract；Status: Experimental）: https://arxiv.org/abs/2603.17074
- LoopRPT（learned recurrent depth；Status: Experimental）: https://arxiv.org/abs/2603.19714

### Daily integration evidence trace

- `2026-05-04 / SF-2026-ARXIV-2605-02087` — exact-v1 `arXiv:2605.02087v1`；正文吸收 versioned behavior-spec midtraining 与 mis-specification boundary，不替代 runtime policy/enforcement。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29158`；Method `https://arxiv.org/html/2606.29158v1 — §3 Power Laws for Optimal Learning Rates; 6 Explaining Nonlinear Scaling via Implicit Effective Learning Rate Schedule`；Evaluation `https://arxiv.org/html/2606.29158v1 — §4 Experiment Design; 5 Main Results`；未证明边界 `https://arxiv.org/html/2606.29158v1 — §7 Conclusions and Limitations`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-SPARSE-REPEATED-TRAINING:start -->
- `SF-SPARSE-REPEATED-TRAINING` — Daily `2026-06-02`；primary `arXiv:2606.01155v1`；正文锚点“数据受限的 Scaling 必须把 Unique Data 与 Repetition 分账”。

  **已吸收的语义增量：** The sparse data-constrained scaling law jointly models unique-token volume, repetition, effective parameters, and sparsity, so repeated-epoch pretraining must choose model size and sparsity against a data-saturation boundary instead of applying dense Chinchilla allocation or sparsity gains independently. 证据边界：The fitted law is empirical over the disclosed scale, corpus diversity, sparsity process, and compute regime; it does not prove the same optimum for frontier-scale mixtures, changing token quality, optimizer changes, or real hardware efficiency, which the paper explicitly separates from theoretical FLOPs.
<!-- daily-books-trace:SF-SPARSE-REPEATED-TRAINING:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-06888:start -->
- `SF-2026-ARXIV-2606-06888` — Daily `2026-06-08`；primary `arXiv:2606.06888v1`；Books review `books-review:SF-2026-ARXIV-2606-06888`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06888:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11387:start -->
- `SF-2026-ARXIV-2606-11387` — Daily `2026-06-11`；primary `arXiv:2606.11387v1`；Books review `books-review:SF-2026-ARXIV-2606-11387`。

  **已吸收的语义增量：** 在 Pretraining 章节补一段 staged promotion：小实验是扩容决策 receipt，不是大规模结果的缩小版证明；保留 scale inversion 与 distributed-effects failure。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11387:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16768:start -->
- `SF-2026-ARXIV-2606-16768` — Daily `2026-06-16`；primary `arXiv:2606.16768v1`；Books review `books-review:SF-2026-ARXIV-2606-16768`。

  **已吸收的语义增量：** 深 Transformer 稳定训练可把 architecture warm-up 与 optimizer warm-up 分离，使曲率/残差路径逐步启用而非只缩小 learning rate
<!-- daily-books-trace:SF-2026-ARXIV-2606-16768:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21514:start -->
- `SF-2026-ARXIV-2606-21514` — Daily `2026-06-20`；primary `arXiv:2606.21514v1`；Books review `books-review:SF-2026-ARXIV-2606-21514`。

  **已吸收的语义增量：** 深网训练的 river-valley dynamics 要把表示阶段与低曲率收敛阶段区分；统一 learning-rate heuristic 会掩盖 late-stage failure
<!-- daily-books-trace:SF-2026-ARXIV-2606-21514:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-12463:start -->
- `SF-2026-ARXIV-2607-12463` — Daily `2026-07-15`；primary `arXiv:2607.12463v1`；Books review `books-review:SF-2026-ARXIV-2607-12463`。

  **已吸收的语义增量：** 新增证据边界：Program-dependency analysis selects function targets under complexity/inferability criteria; the model reconstructs the missing function with generated rationale before existing agentic post-training. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-12463:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-19058:start -->
- `SF-2026-ARXIV-2607-19058` — Daily `2026-07-22`；primary `arXiv:2607.19058v1`；Books review `books-review:SF-2026-ARXIV-2607-19058`。

  **已吸收的语义增量：** 新增证据边界：SkewAdam keeps momentum plus factored variance for the dense backbone, factored variance without momentum for experts, and exact variance for the router. Parameter role becomes the state-allocation key; this is orthogonal to ZeRO sharding and state quantization. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-19058:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-20757:start -->
- `SF-2026-ARXIV-2607-20757` — Daily `2026-07-23`；primary `arXiv:2607.20757v1`；Books review `books-review:SF-2026-ARXIV-2607-20757`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: post-training/random rotation -> symmetry-preserving learned basis during training -> quantized artifact with explicit runtime transform cost 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L486`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-20757:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25063:start -->
- `SF-2026-ARXIV-2607-25063` — Daily `2026-07-29`；primary `arXiv:2607.25063v1`；Books review `books-review:SF-2026-ARXIV-2607-25063`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: checkpoint identity by weights/loss -> stage endpoint evaluation -> ordered data-window lineage -> matched downstream update and erosion response as part of artifact suitability. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L527`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25063:end -->

<!-- daily-books-trace:SF-2026-SPECTRAL-ALLOCATION:start -->
- `SF-2026-SPECTRAL-ALLOCATION` — Daily `2026-08-27`；primary `arXiv:2608.25990v1`；Books review `books-review:SF-2026-SPECTRAL-ALLOCATION`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：在 held-out data 上按 momentum singular directions 探测 loss-optimal step，区分 volatile head 与 tolerant bulk；SAMuon/SAMuon-lite 对 bulk 放大；并保留边界：仅小到中型模型；静态 spectral prior 在 frontier scale、不同 architecture 与长期稳定性上未证明。 相邻章节对读：books/part-04-training-system/27-data.md#L103;books/part-04-training-system/29-sft.md#L55。Data 拥有 sampling weights，SFT 拥有 conditional demonstration objective；optimizer 的 spectral update geometry 属于 Pretraining。
<!-- daily-books-trace:SF-2026-SPECTRAL-ALLOCATION:end -->

<!-- daily-books-trace:SF-2026-SKILL-PRETRAINING:start -->
- `SF-2026-SKILL-PRETRAINING` — Daily `2026-08-28`；primary `arXiv:2608.26563v1`；Books review `books-review:SF-2026-SKILL-PRETRAINING`。

  **已吸收的语义增量：** 补足 skill artifact 作为结构化 capability data 的边界。
<!-- daily-books-trace:SF-2026-SKILL-PRETRAINING:end -->

- `SF-2026-ARXIV-2602-03075` — Daily `2026-02-05`；[ReMiT exact-v1](https://arxiv.org/html/2602.03075v1) §3/Eq3–6、§5及B.1/Eq15–20、F.2。6分具体gap深入仅采用current/ref observed-token logprob gap、序列中心化与有界weighted-NTP反馈接口。B.1称Zw/H(qw)独立θ而主权重包含current pθ，detach未披露；不采用KL梯度方向等价、冻结base、双teacher或一般降本保证。三backbone/等50B mid-training与有限OLMo迭代只属作者局部条件；未运行代码/复现。root已实际核必要原源/owner及167行正文、150–174邻接与末注，写后POST通过；日级Gate待验。

- `SF-2026-ARXIV-2601-08584` — Daily `2026-01-15`；[Ministral3 exact-v1](https://arxiv.org/html/2601.08584v1) §3.1/Algo1与§5.1。2+2+2=6，cascade short-parent/final-long交付及固定teacher身份gap深入；不授总体compute优于one-shot/从头训练。完整data/FLOP未匹配、预训练与后训练teacher反例保留；未运行代码或复现。root必要原源/现owner写前通过并授窄锁，root已实际核两段正文、前后交接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-14603` — Daily `2026-01-23`；[Variance-Adaptive Muon exact-v1](https://arxiv.org/html/2601.14603v1) §3～5/Appendix A 必要对照；2+1+2=5，pre/post variance modulation 与 NS 非交换具体 gap 深入。只采用更新几何与额外 buffer/校准、小 batch 反侧，不授全规模优势或步数等于墙钟；未核 artifact/复现。root 必要原源/owner 写前通过，实际一段与前后邻接、末注经 root 非作者 POST 通过，窄锁释放；root日级语义验收通过（完成态机器检查见Daily）。

- `SF-2026-ARXIV-2601-15394` — Daily `2026-01-24`；[Memorization Dynamics exact-v1](https://arxiv.org/pdf/2601.15394v1) §2/§3/§6。三路同探针区分总体与 teacher-specific 恢复，主证据是Pythia teacher/student/CE baseline、50-token prefix后50-token greedy exact recovery；不采用teacher-origin因果、任意攻击下的隐私率或DP。原实验未复现、artifact未核；root必要原源及具体差额写前通过，实际正文、前后交接与末注已由root非作者POST通过，窄锁释放；本日日级Gate尚未完成。

- `SF-2026-ARXIV-2602-09842` — Daily `2026-02-12`；[Step-Size Stability exact-v1](https://arxiv.org/html/2602.09842v1) §3–5/Theorems3–4/Lemmas5–7。2+1+3=6，具体δ surrogate index差额深入，仅同state/sample条件比较名义与effective step；NGN global lower-model、SPS插值/下界误差、凸界与非凸定性分清。SGD warm-up及SPP成本保留，不授Adam/LLM通用优势，未复现。root必要source/owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2602-10545` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10545v1) §2.1/Appendix D及§4/F.3必要对照。2+2+2=6，joint lr/state-moment尺度的等价continuation与noise探索分责具体gap深入；仅biasfree MLP/SGD窄条件，不授任意架构或同总token/FLOPs优势，ResNet反侧保留。未运行代码/复现；root必要原源、日期包络与owner PRE通过，实际两段/邻接/末注已由root非作者实际POST通过，窄锁释放，不授日级完成。

- `SF-2026-ARXIV-2602-11137` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.11137v1) §3–4、Appendix A.1–A.2必要配置与反侧。2+2+2=6，decay×base/SFT评价目标的具体选择轴深入；仅同模型/预算与固定SFT配方，旧基线复用、相关不稳、强decay反退及搜索费用保留，不授普遍塑性因果或统一最优λ。root必要原源/owner PRE通过；实际正文/邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级，未复现实验。

- `SF-2026-ARXIV-2602-10204` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10204v1) Alg1/§3–4必要ordering与条件反侧；rawmean/residualvariance与normalized-history分开，idealmean/epsilon/spike界限制保留，不授普遍收敛/零额外state。root必要源与实际owner PRE通过，具体差额受影响深入；实际正文/完整邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-12429` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12429v1) §3/Eq2、§4/Eqs12–16/Alg1与必要B/E；2+2+3=7。仅条件性复合factor update界与coupled radius；真实norm、rho<1、实际update约束和inputnorm缺一不授硬保证，1power/5NS只approx，rank/数据暴露/成本与dense回退保留。 未核artifact或复现；root必要原源/owner PRE通过，实际正文、完整邻接及末注经root非作者POST通过，窄锁释放；不是日级Gate。

- `SF-2026-ARXIV-2602-16340` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16340v1) §2.1–2.4/3.1–3.3/4/5.1–5.2/6–7。2+1+2=5，norm-specific条件KKT权限差额深入；fullbatch flow/decay/smooth homogeneous、T2/A1/ε0/精确Muon与非smooth T3限制保留，KKT非global、不授生产AdamW/LLM优越。root必要source/actual owner PRE通过，作者与root实际正文/完整邻接/自身末注顺读，非作者POST通过，窄锁释放；未复现，非日级验收。

- `SF-2026-ARXIV-2602-16490` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16490v1) §3.1–3.2/4.1–4.2/5.2–5.3及必要intervention协议。2+1+2=5，成长训练轨迹/最终untied与部署循环分账差额深入；signature非唯一因果、重复次数退化、mathsource/选block/费用与固定旧支路保留。root必要原源/actual owner PRE通过并授一段窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放；未复现，非日级验收。

- `SF-2026-ARXIV-2602-16642` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16642v1) §3.1–3.4/4及必要D1–2。2+1+2=5，finite fit/几何分账差额深入；fixed-decay/momentum插值与NC4分离仅受测classifier，不采NC0无条件必要性、SignGD/UFM→actual AdamW/LLM或普遍generalization保证，网格/诊断成本与旧recipe保留。root必要source/actual owner PRE通过；作者及root非作者实际正文/完整邻接/自身末注已顺读，POST通过，锁释放，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16687` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16687v1) §3/4.2/4.3 Table1/5.1–5.2/6.1–6.3与Limitations/A3。2+2+2=6，typed-token人口与NLL loss-optimum差额深入；fixed token/FLOP非同音频时长、semantic/acoustic/crossmodal分账、exponent范围/scale饱和与旧路径近正文，不采普遍audio定律或cold-start必优。root必要source/actual owner PRE通过；作者实际顺读及root正文/完整邻接/自身末注POST通过，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16704` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16704v1) §3.1–3.3、Table6/7、k/c反侧与A1/A4。2+2+2=6，真实prefix rollout与同policy state proxy、跨prefix grouping及保NTP分工差额深入；不授语义真值、等FLOPs或fast-weight免费复用，费用/失配与旧目标就近。root必要source/actual owner PRE通过；作者实际正文/完整邻接顺读，root非作者实际正文/完整邻接/自身末注POST通过，未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17080` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17080v1) §2/标量与column公式、§4/Tables1–2及§5。2+2+2=6，Orth后scalar vs column统计的状态/几何差额深入；column非严格统一正交、decay联合变化、exact理论与NS实验分开，搜索费用/非矩阵state近正文。root必要原源/actual owner PRE通过并授一段/自身末注窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放。未核实现/复现，不授普遍收敛或墙钟加速，非日级验收。

- `SF-2026-ARXIV-2602-17155` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17155v1) §3–4/Eq5/10–13、§5/必要F–G。2+2+2=6，projection-before-orth / query scale / resample state 差额深入；true-gradient SVD 条件、非矩阵路径、预算差异与质量反侧近正文，不采用未经核实的 A100100GB 字段。root 必要源/actual owner PRE 通过并授窄锁；作者实际正文及完整邻接已读，root 非作者实际正文/完整邻接及末注 POST 通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-21321` — Daily `2026-02-27`；[RIDER/E-RIDER exact-v1](https://arxiv.org/html/2602.21321v1) §2–5/B.2/F.1–4。2+2+2=6，SP与loss驻点、mixed-gradient坐标及analog/digital EMA责任差额深入；调参/有限模拟、额外阵列/读写成本及静态/数字回退近文，不授普遍收敛/总能耗。root必要源/actual owner PRE通过授单段窄锁；root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-21472` — Daily `2026-02-27`；[The Design Space of Tri-Modal Masked Diffusion Models exact-v1](https://arxiv.org/html/2602.21472v1)。2+2+2=6，physical/virtual batch与AdamW联合重参数及critical区间差额深入；token horizon/临界方向纠正、schedule变化/通信和FLOP反侧/原recipe回退近文，不授γ普遍law或loss=生成quality。root必要源/actual owner PRE通过并授单段窄锁；作者实际正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-22610` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22610v1) §3–4/blocks44–60、94–109。2+1+3=6，DP前向限幅与tail severity差额；上界比非真实sensitivity比、clipping频率近似不变、rolling-user邻接与accountant责任、condition损失/费用及DP-SGD回退近正文。fresh非旧packet作者独核必要原证及actual owner PRE，身份/精确版/拟采用命题未变结果复用；获Ch28窄锁，作者已实际顺读正文及完整邻接；root非写入者已实际读正文、完整邻接与自身末注POST通过，窄锁释放，未核artifact/复现，不授整日。

- `SF-2026-ARXIV-2602-22617` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22617v1) §3–4/blocks36–47、64–83。2+1+3=6，同forward随机triplet方向prior差额；BOS/EOS非真实端点、五seed/unique samples与total tokens分账、λ/额外状态费用及NTP回退近正文。fresh非旧packet作者独核必要原证及actual owner PRE，身份/精确版/拟采用命题未变结果复用；获Ch28窄锁，作者已实际顺读正文及完整邻接；root非写入者已实际读正文、完整邻接与自身末注POST通过，窄锁释放，未核artifact/复现，不授整日。

- `SF-2026-ARXIV-2602-22681` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22681v1) §5–6/blocks76–113、173–182。2+1+3=6，sharp/flat drive与damping分配差额；preconditioner非Hessian、uniform/单系数反侧、continuous/commonbasis条件及搜索/投影费用与原optimizer回退近正文。fresh非旧packet作者独核必要原证及actual owner PRE，身份/精确版/拟采用命题未变结果复用；获Ch28窄锁，作者已实际顺读正文及完整邻接；root非写入者已实际读正文、完整邻接与自身末注POST通过，窄锁释放，未核artifact/复现，不授整日。

- `SF-2026-ARXIV-2602-22936` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22936v1) §2–3/blocks41–79、171–177。2+1+3=6，homogeneous norm与名义/有效η耦合差额；replacement、球面条件、非零Bayes floor与horizon必要，PL示例隔离、非任意schedule/CE/AdamW及tuned recipe回退近正文。fresh非旧packet作者独核必要原证及actual owner PRE，身份/精确版/拟采用命题未变结果复用；获Ch28窄锁，作者已实际顺读正文及完整邻接；root非写入者已实际读正文、完整邻接与自身末注POST通过，窄锁释放，未核artifact/复现，不授整日。

- `SF-2026-ARXIV-2602-22988` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22988v1) §3–5/blocks56–83、123。2+1+3=6，X-whitening DMD/near-unit shaping差额；conditional风险mass非radius/probability、同费NoNorm有限干预、normalizer内不外推、7B forward非训练、诊断费用与normalization回退近正文。fresh非旧packet作者独核必要原证及actual owner PRE，身份/精确版/拟采用命题未变结果复用；获Ch28窄锁，作者已实际顺读正文及完整邻接；root非写入者已实际读正文、完整邻接与自身末注POST通过，窄锁释放，未核artifact/复现，不授整日。

- `SF-2026-ARXIV-2602-23349` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23349v1) §3–5/blocks37–51、80–92。2+2+3=7，BF16 signed residual与moments companding差额；梯度dtype混杂/step非全训、省费反侧、scales/padding/checkpoint与FSDPlocal identity、极弱更新未证及高精回退近正文。fresh非旧packet作者独核必要原证及actual owner PRE，身份/精确版/拟采用命题未变结果复用；获Ch28窄锁，作者已实际顺读正文及完整邻接；root非写入者已实际读正文、完整邻接与自身末注POST通过，窄锁释放，未核artifact/复现，不授整日。

- 2026-01-28 来源遗漏补查，arXiv:2601.18302v1：本日具名必要 Source 复用；root 实际逐字拟文、对应正文完整局部邻接 PRE 通过后授本段与自身末注窄锁。已写入，resume_20260128_audit 非作者实际正文、完整局部邻接与自身末注 POST 通过，窄锁释放；原直接反侧与费用/失败回退近正文保留，未核 artifact 或复现。<!-- source-family:SF-2026-ARXIV-2601-18302 -->

- `SF-2026-ARXIV-2602-08287` — Daily `2026-02-11`补查；[exact-v1](https://arxiv.org/html/2602.08287v1) §2/4/6/7、Appendix D/J/I.2。2+1+2=5，随机 token 扰动的输出 agreement 与语义 gate 分责；未中心化 moment 不当 covariance，主文 T 符号与 Appendix D 正确式隔离，简化 OU 与有限训练不授任意 Transformer 稳定保证。root实际必要 Source、owner 邻接与逐字 PRE 通过；root非写入者实际154–170完整局部与162措辞短核及自身末注POST通过，Ch28窄锁释放。未核 artifact/复现，不授 DAY。

- `SF-2026-ARXIV-2602-09396` — Daily `2026-02-12` 补遗漏；[exact-v1](https://arxiv.org/html/2602.09396v1) §4.1–4.3、T1与Appendix A Eq8–10/Algorithm1–2和cost。2+1+2=5，串流梯度历史与实际optimizer后aux/RL投影分责gap定点深入。K5小轨迹window/EMA并非零memory或IID；raw-EMA文字与Alg32/33 projected history矛盾隔离，不采用精确更新recipe，Atari退步/strq与orth²配置费用区别近正文。root必要Source与actual owner PRE通过并授一段窄锁；作者已顺读实际新段与完整邻接，root非写入者实际714–731完整局部/新720及自身末注POST通过，Ch28窄锁释放，不授DAY。未核实现/复现，不授大模型预训练默认优化器、端侧免费或部署world model。

- `SF-2026-ARXIV-2602-08984` — Daily `2026-02-11`补查；[exact-v1](https://arxiv.org/html/2602.08984v1) §2–5、必要 Appendix B/E.2–3。2+2+2=6，内生后续块 target、软 codebook 读出与 token CE 并行的接口深入；VQ beta 项对 representation 的非零梯度与 broadcast 周期 k / floor(t/(k−1)) 冲突隔离，不采用实现无 leak 或严格不影响 representation 保证。单 loss 反退、插入位置与训练/推理费用留在采用边界；root 必要 Source 与实际 owner PRE 通过，作者已写与顺读完整邻接，root 非写入者实际145–178完整局部/新158及自身1837末注POST通过，Ch28窄锁释放，不授 DAY。未核 artifact 或复现实验。

- `SF-2026-ARXIV-2602-12005` — Daily `2026-02-14`补查；[LaCy exact-v1](https://arxiv.org/html/2602.12005v1) §3–6、T1–2/F2–7及Fig10直接反侧，2+2+2=6。只采用GT/CALL target与non-CALL重归一化分工；proxy非真值、15%训练≠22%部署、屏蔽对照forward预算与全调用费用/旧NTP回退近正文。非作者必要Source与root逐字actual PRE通过；作者写后顺读，root非writer实际36–85完整邻接/新64与自身1841末注POST通过，Ch28窄锁释放，不授DAY。未核artifact/复现，不授知识删除或cascade事实真值。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2603-07787` — Daily `2026-03-11`补查；[ARROW exact-v1](https://arxiv.org/html/2603.07787v1) 必要原证96–204/264–361/600–655，2+1+2=5；有限gradient窗口、未中心化Gram逆算子和checkpoint接口的owner具体差额深入，不改评分。review_mar11_continue实际必要Source与Ch28 owner/PRE通过，root授516源注后/518标题前单段和本人注窄锁；作者实际480–575完整邻接（输出末段缺口已补）与Ch30/32交接有效复用。Span、非Hessian、O(dW)状态、任务人口和全费用边界近文；作者实际写入，review_mar11_continue非writer实际完整正文/邻接与本人注POST通过，root已释放窄锁，不授DAY、实现核验或复现。

- `SF-2026-ARXIV-2603-08065` — Daily `2026-03-11`补查；[DDP exact-v1](https://arxiv.org/html/2603.08065v1) §2.1–3.3/§5.1–5.5/Table4–8/Alg1/C必要100–224/424–568/807–842/1075–1078；B843–879仅budget/margin入口，T2/3仅必要正文/头，不称全证明/全表。2+2+2=6，forward非负幅度与retention计数双接口的owner差额深入；不采exactbudget/global最优、纯去随机单因果或质量无损。训练预算/实际runtime未全绑定、细预算质量反侧保报告；mask/teacher/KD/search/removal/backend与独立回归全费用及旧路径近文。review_mar11_continue必要Source与actual Ch28 owner/逐字PRE通过，root授完整结构稀疏恢复段后单段+本人注窄锁；作者actual308–346完整邻接、Ch27/29入口及Ch49 507–538交接回对，已落实窄写；review_mar11_continue非writer实际完整正文/邻接及本人注POST通过，root已释放窄锁，不授DAY、artifact核验或复现。
