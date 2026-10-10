# 第8章 大模型为什么会产生智能

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Stable Knowledge Node ID:** `WORLDVIEW-LLM-INTELLIGENCE`
**Legacy Chapter:** Ch8
**Status:** Draft

**Roadmap Intent:** 从预测下一个 token 到涌现能力、上下文学习和工具使用。

## 本章要回答的问题

预测下一个 token 看起来只是局部统计任务，为什么扩大模型、数据和训练后，系统会表现出问答、翻译、代码、少样本学习、规划和工具使用等广泛能力？这些表现为什么仍不能证明意识、真实理解或生产可靠性？

本章使用一个受限而可检验的“智能”定义：**模型在多种任务和新上下文中表现出的 operational capabilities。**中心命题是：next-token prediction 在大规模、多样数据上迫使模型形成可复用的语言与世界结构表示；架构容量、数据覆盖、优化、context 和 post-training 共同把这些表示转化为广泛行为，但能力不等于可靠性，更不能直接推出意识。

## “只是预测下一个 token”少算了什么

自回归语言模型把序列概率分解为：

```text
p(x_1, ..., x_T) = product_(t=1)^T p_theta(x_t | x_<t)
```

其中：

- `x_t` 是第 `t` 个 token；
- `x_<t` 是它之前的 token；
- `theta` 是模型参数；
- `p_theta` 是模型给出的条件概率分布。

训练通常最小化目标 token 的负对数似然：

```text
L(theta) = - sum_t log p_theta(x_t | x_<t)
```

从单个位置看，任务确实只是选择下一个 token。但要在多样文本上持续降低平均误差，模型不能只记住局部 bigram。下一 token 可能取决于语法结构、段落主题、事实关系、说话人意图、代码状态、数学约束或前文定义。

例如，补全一个函数的返回值需要追踪变量和控制流；续写一段证明需要保持前提与结论；回答一条事实问题需要利用训练中形成的关联；模仿一种格式需要从 context 推断当前任务规则。预测接口局部，不意味着完成预测所需的内部计算也只能局部。

更准确的说法是：**next-token prediction 提供统一而密集的训练信号，数据本身决定为了降低这个信号，模型需要压缩哪些结构。**它不会保证模型学到真实因果世界模型，但在覆盖广泛人类文本时，许多语言、知识和任务结构都对预测有用。

## 从表面统计到可复用结构

最朴素的语言模型可以统计短词组频率。它在熟悉局部模式上有效，遇到长距离约束、新组合和开放任务时会迅速稀疏。神经网络则把 token 映射到连续表示，并通过多层上下文计算共享统计强度。

共享表示带来组合能力。不同表面形式如果在训练目标中承担相似作用，可以使用部分共同特征；已学到的语法、语义、代码和文档模式又能在新输入中重新组合。第 5 章已经说明，这些是分布式、任务相关的表示，而不是逐条可读规则。

可以用 compression 建立直觉：逐字记住所有训练文本不是利用数据规律的唯一方式，发现可复用结构能更有效地预测许多样本。模型越有容量、数据越多样、优化越充分，它越可能捕捉低频和高阶规律。

但“压缩”在这里是解释性视角，不代表模型一定构建了正确、简洁或因果的世界模型。错误相关性同样可以降低 loss，互相矛盾的文本也可能共同进入参数。语言中的世界结构只是训练分布的一部分投影。

训练数据没有显式给出某条规则，并不等于它没有提供支持该规则的分布线索；因此稀疏构式的泛化应固定构式、读出和过滤人口，分别测直接正证与剩余线索，而不从某个测试成功推出先天规则或完整语法。[PoSH的受限检验](https://arxiv.org/html/2602.09992v1)在过滤后的幼儿语言/文本上观察到部分泛化，同时部分层级构式仍接近或低于机会水平；加入所测认知bias也没有稳定改善指定目标。这修正的是“缺少直接例子必然无法学习”和“bias必然帮助”的两项强判断，不否定所有bias或认知解释。抽样核查仍发现binding泄漏，训练上下文/预算不完全匹配；过滤、人工核查和配对评价都付费，应保留普通分布学习解释及独立构式测试，不把有限未检出写成整个语料零正证。 <!-- source-family:SF-2026-ARXIV-2602-09992 -->

语法形式与构式意义也不能互相代签。判断句子是否可接受，与判断某个结构约束了怎样的事件或参与者关系，是不同的行为接口；即使采用相同 checkpoint 与 likelihood 读出，两种能力的学习进度仍可能不同。[受限最小对照](https://arxiv.org/html/2602.21978v1)中，OLMo2 的形式可接受性指标较早趋平，构式意义选择仍继续改善；这不是新的普遍 scaling law，也不证明内部已形成可读语法规则。人名/实体互换、虚构词与 base/instruct 对照可帮助诊断词汇依赖，但保留的闭类词、形态和生成器筛选仍影响支持，局部 instruction tuning 也会让部分构式退步。应分别固定形式与意义的任务、读出和候选人口，计入材料生成、人评与模型评分成本；只需要形式检查时，原可接受性基线仍合理，需要意义泛化时则增加独立语义对照，不用一个通过分数替另一个接口验收。
<!-- source-family:SF-2026-ARXIV-2602-21978 -->

## 相关分布能支持因果推演，但不能自动识别干预关系

既然科学论文、历史叙述和日常解释都包含原因、结果与反事实，一个合理的朴素判断是：模型为了预测这些文本，会把其中反复出现的因果结构压缩进可复用表示。这个判断解释了模型为什么能够复述因果知识、补全因果链，甚至在给定规则后执行多步推演；它不能直接推出模型已经从世界中识别出真实因果机制。

关键差异在于，观察到 `X` 时预测 `Y` 与主动改变 `X` 后预测 `Y` 不是同一个问题：

```text
observational relation: P(Y | X)
interventional relation: P(Y | do(X))
```

例如“撑伞”与“地面湿”可以在文本和观察数据中高度相关，但强制人们撑伞并不会让地面变湿；共同原因可能是下雨。多套因果结构可以产生相同或近似的观察分布，所以 next-token loss 即使拟合得很好，也没有提供唯一识别因果方向所需的 intervention、环境变化或结构假设。因果表示研究在明确条件下证明，完美干预数据可以增加 latent causal factors 的可识别性；这个结果说明干预提供了观察数据没有的信息，不证明语言模型天然满足那些识别条件。[Interventional Causal Representation Learning](https://proceedings.mlr.press/v202/ahuja23a.html)

另一方面，文本并非只有未经处理的共现。它记录了人类实验、反事实讨论、程序执行、因果图和干预后的结果。因此语言模型可以继承人类已经整理的因果知识，并在新措辞中组合这些结构。行为研究也观察到模型能够在若干任务上生成正确的因果论证，但同时存在不可预测的 failure mode，且模型处理的是关于数据的文字信息而非实际观测数据。[Causal Reasoning and Large Language Models](https://arxiv.org/abs/2305.00050) 这类结果支持“模型具有条件性的因果推演能力”，仍无法区分它是在稳定使用抽象因果结构，还是识别题型后复现有效的语言模板。

因而 Evaluation 至少要分开三层结论：能否复述训练分布中的因果知识；能否在给定明确 causal graph、干预与反事实规则时正确推演；能否在新环境中通过主动实验发现并持续修正因果结构。CLadder 把关联、干预和反事实查询建立在有 ground truth 的因果图上，显示形式化因果推理仍是困难任务；它衡量的是受控问题上的行为，不是对模型内部表示的完整读取。[CLadder](https://arxiv.org/abs/2312.04350)

这条边界给 AI System 一个清楚的责任划分：语言模型可以提出因果假设、整理先验和生成候选推演，但 simulator、实验、监控数据或真实环境 observation 才能提供干预后的结果，高风险决策还需要独立验证与可回退的 action authority。纯文本模型在知识综合、低风险解释和已知规则推演中仍是合理路径；主动干预昂贵、缓慢且可能危险，也不能被机械要求用于每个问题。第 25 章拥有 action-conditioned World Model 与 intervention fidelity，第 66 章拥有相应 Evaluation contract；本章只界定 next-token 能力何时可以被称为因果推演，以及为什么它不能自动升级为因果发现。

## 为什么规模会扩大能力范围

第 7 章讨论了 loss 随参数、数据和 compute 的经验趋势。把它连接到能力时，需要增加中间机制，而不能直接说“loss 下降所以智能涌现”。

参数增加，函数族可以承载更多特征和更复杂计算；数据增加，模型能观察更多领域、任务形式和组合；compute 增加，优化器有机会把这些经验写入参数；Transformer 的上下文化路由则允许输入中的信息动态交互。

这些因素共同扩大模型可利用的模式集合。某些任务只有在模型同时具备多个子能力时才能完成，例如读懂指令、保持中间状态、调用相关知识并生成正确格式。底层子能力逐渐改善时，端到端任务表现可能在某个区间显著上升。

这仍是统计与计算能力增强，不是一个神秘开关。具体能力何时出现，受到数据是否包含相关结构、tokenizer、架构、prompt、解码和评估方式影响。相同参数规模的模型也可能表现很不同。

## In-context learning 改变了任务接口

GPT-3 使 in-context learning 获得广泛关注：模型参数不更新，只通过 prompt 中的指令或示例，就能改变当前任务行为。

形式上，模型仍计算：

```text
p_theta(output | instruction, examples, query)
```

`theta` 在请求期间固定，变化的是条件上下文。模型可能从示例中推断标签映射、格式、任务类型或局部规律，再按该模式继续生成。

这带来一种新的软件接口：任务的一部分从训练代码和固定模型头移动到了 runtime context。过去需要训练一个分类器的任务，可能通过自然语言说明和少量示例临时定义。

但 in-context learning 不等于参数在请求期间被训练，也不保证模型真正识别了用户意图。它可能依赖表面 pattern、示例顺序、标签词、prompt 模板和预训练中见过的任务格式。要证明某种内部学习算法，需要比 few-shot 得分更强的机制证据。

从系统角度看，context 因此成为运行时状态与质量输入。prompt version、示例选择、retrieval、截断和上下文污染都会影响能力，必须像模型版本一样被评估和观测。

Context 内的“学习”可以是一次 forward 中执行估计程序，不必是参数更新。一条受限构造先按 query 的局部几何拟合 tangent，再在稳定的局部坐标中聚合样本、求回归；ambient cutoff防止投影把远处样本伪装成邻居。这里局部sample mass、维度、smoothness、separation与扰动共同决定可估计尺度，算法还需要结构信息与数值guard，不能把它解释为任意预训练模型已经自动发现同一程序。

要检验 context 内执行了什么估计，可以先选择解析统计量已知的任务，再分开比较输出、内部可解码性与因果控制。一项受限构造在每个 episode 改变 Gaussian 的均值偏移或 variance，用带标签的有限 context 预测新 query；线性任务与二次 energy 任务呈现不同的可读出深度。它比 few-shot 分数提供更多诊断对象，但只对 raw dot-product kernel 作弱相关对照，不能排除 learned/centered kernel；LogitLens 与 OV 对齐仍是相关证据，不是 heads 实际投票或某层唯一必要算法的证明。[原始受限机制](https://arxiv.org/html/2603.10573v1)。<!-- source-family:SF-2026-ARXIV-2603-10573 -->

已知生成任务参数的 oracle 与模型只见有限 context，不拥有同一信息。有限 context 通常留下参数 posterior，正确 predictive ratio 需要对它积分，不能直接把隐藏真参数的 likelihood ratio 当作 context 已完全识别的 Bayes 规则。该实验 variance 任务接近更有信息的 oracle，mean-shift 任务仍有 gap，较大域外 shift 和所测 label-noise 条件下结果退步，增加 context 的所测均值也未改善；没有认证任意 LLM 的通用统计算法。构造 oracle、生成任务、训练与 probe 均付费；进一步确认因果机制还需额外的定点干预预算。部署仍用当前 context/held-out 行为验收，不把高 rank correlation 或低 loss 当作因果机制和普遍最优证书。

构造出可实现的 comparator，与有限pretraining真正选到它，是两个问题。新任务prompt内的样本数限制该函数能被估计多准，独立训练任务数则约束选择程序的泛化；实现误差和near-ERM优化gap仍须另外计入。固定head的存在构造也可能随context增长workspace、width与数值范围；有限实验增加任务数时同时增加更新预算，且模型与理论构造不同。条件失配或无匹配机制证据时，继续以held-out任务和当前context协议验收，不从minimax或存在性定理推出任意LLM可靠学习。[构造与条件](https://arxiv.org/html/2609.31458v1) <!-- source-family:SF-2026-ARXIV-2609-31458 -->

## Post-training 把通用预测器塑造成可用接口

预训练数据包含网页、代码、对话、文档等多种文本。一个只做 next-token prediction 的 base model 擅长续写，却不天然知道“用户问题应被直接回答”“危险请求应拒绝”或“输出必须满足某个 schema”。

Instruction tuning、SFT 和 preference-based post-training 使用更接近产品交互的数据与目标，改变模型在给定指令下选择什么行为。它们通常不是从零创造全部知识，而是选择、重组和强化预训练已形成的能力，使模型更容易按照任务接口工作。

这解释了为什么参数规模和 pretraining loss 相近的模型，最终可用性仍可能差异很大。能力表现来自 base model、post-training、system prompt、context、sampling 和外部系统的组合。

也要保持边界：本章不展开 SFT、RLHF、DPO 或 GRPO 的优化机制，它们属于 Part IV。这里仅说明 post-training 是“广泛潜在能力”变成“可调用行为”的关键条件，并且可能同时改善可用性、压制某些能力或引入新的偏好偏差。

## Emergence：现象、指标与解释必须分开

一些研究把 emergent ability 定义为：小模型表现接近随机，规模超过某一区间后某项任务分数快速提高。这类观察提醒人们，平均 loss 不能完整预测下游行为，也使大模型能力成为重要研究问题。

但“曲线上看起来突然”并不自动证明底层能力发生不连续相变。Schaeffer 等工作指出，若任务采用 exact match、multiple choice accuracy 等非线性或离散指标，平滑改善的底层概率可能被映射成跳变；换用连续评分后，一些 emergence 现象会变得平滑。

这类反驳也不能证明所有新能力都是度量幻觉。某些任务可能涉及组合阈值、搜索、交互或训练分布覆盖变化，模型机制本身也可能发生定性变化。可靠结论需要同时检查：

```text
metric shape
prompt and sampling sensitivity
model family and training data
continuous underlying measures
mechanistic evidence
replication across scales
```

因此本书把 emergence 当作待解释的经验现象集合，而不是统一因果理论。第 7 章的 scaling curve 描述 aggregate loss，第 8 章的能力曲线描述具体任务，两者不能互相替代。

## Tool use 为什么会放大模型能力

纯参数模型受训练截止、上下文、算术精度和内部计算限制。工具可以把部分工作交给更合适的外部系统：检索提供新信息，计算器执行精确运算，代码环境运行程序，业务 API 改变真实状态。

ReAct 一类方法展示了 reasoning trace 与 action/observation 交错的任务形式：模型不必一次生成最终答案，可以根据环境反馈修正后续行动。能力由闭环组合产生：

```text
model policy
  + tool affordance
  + environment feedback
  + runtime control
  = system capability
```

这意味着 benchmark 上的“模型能力”和生产中的“系统能力”必须区分。同一个模型接入不同检索、工具、memory 和 workflow 后，实际覆盖范围会明显变化。

工具也放大风险。模型可能选择错误工具、生成错误参数、相信恶意 observation、重复执行有副作用操作或越过权限。Tool use 证明语言模型可以参与行动闭环，不证明它能独立承担开放环境中的可靠控制。权限、schema、幂等、确认、trace 和补偿属于 Part VII 的 Agent runtime。

## Capability 不等于 Reliability

一个模型“有能力完成任务”，通常指它在某些条件和一定概率下能够成功。生产系统需要的是在目标分布、SLO 和风险边界内稳定成功。

两者之间至少存在六个缺口。

第一，概率性。模型可能在同类输入上给出不同质量结果。

第二，分布变化。训练与 benchmark 覆盖不等于真实用户、最新事实或极端输入。

第三，校准。流畅表达不代表置信度可靠，模型可能在错误时仍然肯定。

第四，组合误差。多步任务中，每步略低于 100% 的成功率会沿链路累积。

第五，对抗输入。prompt injection、数据投毒和工具返回可能利用模型对文本指令的敏感性。

第六，目标错位。模型可能优化“看起来像好答案”，而不是业务真正需要的事实、合规和可执行结果。

所以 Evaluation 需要区分 capability ceiling 与 reliability distribution。可以分别测试 pass@k、单次成功率、最坏切片、校准、鲁棒性、拒答、恢复和成本。允许多次尝试能展示潜在能力，却可能掩盖一次请求的用户体验和资源代价。

显式解释还增加一个独立接口：同一问题换措辞后输出是否一致、答案是否正确，以及解释是否忠实于真实计算，不能共用一个分数。把另一模型的解释去掉答案标签后转给目标模型，可以改善某些任务的一致性，却仍可能稳定地答错；删除标签也没有独立证明解释未携带答案线索。跨模型解释是外部条件，不是内部 reasoning 轨迹的直接读取。<!-- source-family:SF-2026-ARXIV-2601-11517 -->

[受限跨模型解释对照](https://arxiv.org/html/2601.11517v1)在有限 MedCalc 与 instruction tasks 中，Deepseek-R1-Distill-Qwen-1.5B 经 GRPO 后，转移解释给五个模型的平均 pairwise consistency 从0.11到0.39，平均 transfer accuracy却从0.30到0.29；另一个受测模型可同时改善两者，故不能把这种分离写成所有RL设置的规律。逐句多候选与 perplexity 选择增加调用/评分成本，人类感知 rating 也不是实际解题效果。需要正确性或高风险判断时，保留答案验证、无解释/自己解释的匹配对照与独立证据；成本或迁移失配时沿用较简单解释接口，不把“更稳定、更可信的措辞”当作更可靠的模型。

## 能力不等于知道自己知道

把 hallucination 简化成“模型泛化错了”只说对了一部分。Generalization 是把训练中形成的结构应用到未见组合；
hallucination 则是生成结果越过了当前 evidence boundary，却仍以像答案的形式提交。例如模型可以正确泛化论文摘要
的写作结构，却把这套结构用于一篇不存在的论文。形式泛化成功，事实约束失败。

基础语言模型在推理时给出的是：

```text
p_theta(next_token | prompt, generated_history)
```

它不是：

```text
P(claim is true | current world and available evidence)
```

Softmax 对任何输入都会产生总和为 `1` 的 token distribution；weights 也不是一张带 `known / unknown` 字段的知识表。
因此“当前最可能的续写”可以非常集中，却仍然是错误事实。降低 temperature 只会让这个 mode 更稳定，不会把语言
概率自动变成 truth probability。

这不只是“训练语料里有错误”。即使语料中的答案都正确，有限数据也可能不足以区分一个未见答案究竟有效还是只是像真的。一个有边界的理论分析把生成问题转为 Is-It-Valid 二分类：在有限答案空间、同一 prompt 分布和特定的正确/错误混合评价分布下，由模型概率构造的分类器若仍难以区分两者，且概率质量偏差与有效/错误答案数量比足够小，就能给生成错误率提供非平凡下界。这里的概率质量偏差不是“模型对事实正确性的校准”；缺少上述条件，下界可能没有信息，不能改写成所有模型必然以某个比例 hallucinate。始终拒答或只回答可验证问题的系统也不是这项结论的反例，因为它们改变了覆盖范围或分布条件。[条件与证明](https://arxiv.org/html/2509.04664v1#S3.SS2)。<!-- source-family:SF-2025-ARXIV-2509-04664 -->

因此需要分开两个问题：模型是否有足够信息辨别有效答案，以及面对不确定性时系统是否允许它不回答。后者还受评价规则影响：答错与拒答都记零分、猜对记一分时，哪怕只有很小的主观正确概率，猜测也比拒答有更高的期望分数。这说明某种评分规则的激励，不证明模型实际执行了最优决策，也不解释全部幻觉来源。第 66 章负责定义回答、拒答和错误代价的评价契约，本章只据此保留一个能力边界：语言分布学得好、具备正确性信号与愿意按证据行动，不能互相替代。

模型内部仍可能包含与正确性相关的信号。可以读取 answer log-probability、token/sequence entropy，让模型在提出
答案后预测 `P(True)`，或直接预测 `P(IK)`（是否知道）；也可以多次采样，将语义等价答案聚类后计算 semantic
entropy。这些方法支持一个有边界的结论：**模型有时能感知 familiarity、歧义和自身失败风险，但这种自知是需要
训练、格式与 deployment distribution 校准的能力，不是模型天然拥有的 introspection oracle。**

同一个模型产生答案又评价答案时，两者共享 weights、Context 和训练偏差。多个 samples 也可能稳定复现同一流行
误解；低 entropy 只说明分布集中，不说明世界事实正确。[Language Models (Mostly) Know What They Know] 的作者实验
显示 self-evaluation 在若干任务上可扩展，但 `P(IK)` 在新任务上的 calibration 仍困难；TruthfulQA 又说明更强的
文本模仿可以同时学到人类常见错误。二者并不矛盾：内部 risk signal 存在，不代表它在开放世界中已可靠校准。

因此“是否允许回答”必须从模型属性升级为系统决策：

```text
model proposal
→ internal uncertainty signal
→ external retrieval / tool / executable evidence
→ claim-level verification and calibrated risk
→ answer / ask / retrieve more / abstain / escalate
```

模型拥有 proposal，不拥有最终 truth verdict；RAG 拥有 evidence access，不自动拥有 evidence sufficiency；verifier
只能裁决其 specification 覆盖的条件；Evaluation 与业务 policy 才能根据风险决定是否发布。第 20 章解释内部
sampling/confidence，第 76 章解释 external evidence path，第 66 章负责 claim graph、calibration、coverage 与 abstention。

这也解释了为什么“永不 hallucinate”不是开放世界中的可验证承诺。系统能做的是在声明的 corpus、verifier、时间和
风险 slice 内，测量 false-answer / abstention trade-off，并在 evidence 不足时拒绝把 fluent continuation 升级为事实。

### 把 Hypothesis Generation 与 Evaluation 分开

模型能够比较给定候选，并不等于它能够自行枚举出关键假设；在已观察域内更新 posterior，也不等于能在未观察域可靠外推。受限实验表明，给定 hypothesis 的 evaluation、自由 hypothesis generation 与 hypothesis-selective extrapolation 是三个不同接口：候选集合已经提供时表现近似 Bayesian，不能证明遗漏候选时仍会“知道自己不知道”。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05851 -->

这个结论来自 number game、一维整数和有限假设族，不能直接充当通用 LLM 认知理论。它给系统设计的稳定启示是：高风险任务应把 candidate generation、外部枚举、evaluation 与 evidence verification 分开，让任何一个阶段的自信都不能代替其余阶段。

## 关于“理解”和“意识”的边界

模型能够形成有用表示、根据上下文改变行为并解决新任务，这是可观察的工程事实。由此可以研究模型是否建立某种内部世界结构、是否使用因果特征、是否能规划和自我修正。

但行为能力不能单独解决意识或主观体验问题。“生成了像理解者一样的文本”与“具有何种内在体验”不是同一可验证命题。本书关注可观测机制、能力与系统约束，不用当前 benchmark 为意识作结论。

同样，“只是统计”也不是充分反驳。所有机器学习模型都利用统计规律，关键问题是这些规律支持何种可迁移计算、在哪些条件下失效。使用贬义标签不能替代机制分析。

## 对 AI System 的工程含义

第一，模型不是唯一能力边界。数据、post-training、prompt、context、retrieval、tools 和 decoding 共同决定行为，版本管理应覆盖完整配置。

第二，Evaluation 必须贴近任务。Pretraining loss、通用 benchmark 和线上 KPI 各自回答不同问题，需要通过版本和 trace 关联。

第三，context 是可编程但不稳定的运行时状态。长度、顺序、来源、权限和污染都影响结果。

第四，更强 capability 会增加治理需求。能生成代码、调用工具和处理更多领域，也意味着更大的安全、隐私和动作风险面。

第五，系统优化不能牺牲语义。量化、截断、batching、模型路由或 speculative decoding 即使改善 latency，也要重新评估能力和可靠性。

第六，Agent 成功率不能只看最终答案。工具选择、参数、observation、重试、成本和副作用都应进入 trace 与 Evaluation。

## 本章在知识树中的位置

第 6 章给出可扩展架构，第 7 章给出规模与 loss 的经验规律，本章解释为何这些条件加上数据、context 和 post-training 后会表现为广泛 operational capabilities。逻辑方向是：

```text
scalable architecture
-> broader optimization over data and compute
-> richer reusable representations
-> capabilities expressed through context and post-training
-> system capability amplified by tools
```

这条链不反向证明“出现能力，所以某条 scaling law 必然成立”。也不把工具调用等同于完整 Agent。Part IV 会展开 post-training，Part VII 会展开 Context、Tool Calling、Planning、Memory 和 Agent Platform。

### 记住两个事实，不等于学会组合它们

模型可以分别复现 `A→B` 与 `B→C`，却仍在面对 `A→C` 时失败，因为事实存储和可复用推理电路是两个不同 contract。组合成功要求中间实体在不同 context 中保持可对齐表示，并让后续层读取前层构造的 bridge state；若上层只学到训练分布中的 output mapping，原子事实都正确也不会自动产生新的两跳关系。循环或更深计算可以增加复用机会，却也带来状态漂移和额外计算。受控符号与自然语言实验只支持这一故障机制可能存在，不证明真实大模型的所有 multi-hop failure 都有同一原因。

<!-- source-family: arxiv:2608.07261v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: atomic-fact-storage-vs-composable-reasoning-circuit -->

上述 bridge-state 是一条受控的组合机制，不能把探针何时读出实体直接当作原任务的因果计算顺序。若把不同 layer、subject/末 token 的 hidden state 转入另一个解释 prompt，所观察的是该解释接口中的可解码性；raw、按解释相似度过滤的 GF/LF，以及只保留原子事实与组合均答对的 Correct 人口，也不是同一测量对象。[受限多跳观察](https://arxiv.org/html/2601.03542v1)中三、四跳的最终实体可以比中间实体更早被该探针读出，两跳却未见同样反转。这要求比较层顺序时固定位置、解释 prompt、过滤规则与条件人口，而不是据此否定所有逐步组合，或反向证明模型先完成真实 recall 再提取桥状态；概率 recall、Attention/MLP 功能与必要因果 hop 仍需独立干预。旧的受控电路解释继续成立，可读表示与实际使用分开验收，探针失配时回退行为对照和受控干预。<!-- source-family:SF-2026-ARXIV-2601-03542 -->

## 自检问题

1. 为什么 next-token 接口是局部的，却可能要求模型使用长程和高阶结构？
2. “预测迫使模型学习世界结构”为什么只能是有边界的结论？
3. 参数、数据、compute 和架构分别怎样扩大可利用模式的范围？
4. in-context learning 与参数更新有什么区别？
5. post-training 为什么会显著改变同一个 base model 的可用行为？
6. emergence 的跳变可能由哪些度量因素造成？为什么这又不能否定所有定性变化？
7. 模型能力与接入工具后的系统能力有什么区别？
8. capability 和 reliability 应使用哪些不同证据？
9. 为什么多步 Agent 任务会放大单步错误？
10. 哪些问题可以由行为实验回答，哪些问题不能从 benchmark 直接推出？
11. 为什么 token probability 不是 claim correctness probability？
12. 模型的 `P(True)`、`P(IK)` 或 semantic entropy 能支持什么，又不能支持什么？
13. 为什么“是否允许回答”最终是系统 evidence-and-decision contract？

## 小结

大模型的广泛能力并非来自 next-token prediction 之外的神秘目标，而是来自这个统一目标在大规模、多样数据上的要求：为了持续降低预测误差，模型需要形成可复用的语言、知识和任务结构表示。规模、Transformer、context 与 post-training 又让这些表示更容易被调用和组合。

但能力是有条件的。emergence 受指标影响，tool use 把模型能力变成系统能力的同时也放大风险，流畅输出更不等于稳定可靠。AI System 的责任，是把“模型有时能够做到”转化为“系统在明确边界内可以被信任地做到”。

### Context 与 Working Memory 决定可计算的层级深度

规模扩大可以增加模型拟合能力，却不能消除有限可见上下文和有限工作状态的计算边界。在树形 broadcast process 构造出的层级语言中，任务所需依赖深度、可见 context 与显式 reasoning/work memory 之间存在可分析的条件关系：当局部证据不足以恢复上层 latent state 时，仅扩大相同接口的模型并不会自动获得所需信息。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13687 -->

这类结论来自规则树和合成语言，而不是自然语言的完整定律。它的长期意义是把“能力不足”拆成表示容量、可见信息和中间状态三类约束；若 workload 不满足树模型假设，就应回退真实任务的干预实验，而不是把理论 scaling law 当作生产预测。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21488:start -->
当模型反复更新隐状态时，test-time compute 还可以表现为 task-conditioned attractor：额外深度增加同一状态的
迭代次数，额外宽度增加并行初态或候选轨迹，二者都可能让表示更接近某个稳定区域。这解释了部分任务为何能从
depth / breadth scaling 获益，但“轨迹收敛”只说明内部动力学稳定，不说明稳定点对应外部正确答案。

因此系统必须把 latent convergence 与 answer verification 分开。若吸引子对 prompt、初态或分布漂移敏感，或
外部 evaluator 不支持该结论，就回退固定推理预算、显式中间状态和可核验工具；受控模型与任务上的实验不能被
外推为所有 LLM 都能靠更多采样获得可靠推理。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21488:end -->

当额外深度来自对现成模型的一段 frozen blocks 反复应用时，稳定训练过的普通 forward 并不保证该 block 接受循环后的状态仍有效。一条不重训的条件分支先取得普通 forward 在循环边界的参考状态，再缓存循环状态，以均匀平均、参考状态插值或相对参考的加权平均送入下一轮；它改变的是 block 的输入分布，而不是增加参数或认证 hidden state 的真值。[受限 frozen-loop 对照](https://arxiv.org/html/2602.14759v1)中，Gemma2-2B/WinoGrande 的 naive 区间扫描全部反退，而参考插值后部分任务改善；区间在 WinoGrande 选择后固定到其他任务，Gemma 的 ARC-E 仍退，Llama3-8B 响应更不一致。跨模型 normalization 差异没有被独立隔离，插值也不是 valid activation domain 的证书。普通参考 forward、额外 block 应用、状态缓存与区间校准都要付费，multiple-choice option likelihood 的改善不能直接外推自由生成或端到端速度。循环造成分布漂移、质量反退或额外成本无法摊销时，保留普通 forward、较小固定预算或经独立验收的训练式 recurrence。<!-- source-family:SF-2026-ARXIV-2602-14759 -->

增加 latent 轨迹的宽度时，还可以把“更新推理模型”与“学习探索 proposal”分开：冻结既有 backbone 参数，让一个可训练 head 读取当前确定性 hidden state，输出扰动的 diagonal-Gaussian 均值与方差；扰动后的 state 再进入下一轮 recurrence。这样改变的是条件探索分布，不是给 latent thought 建立正确答案 posterior，冻结模型也不意味着 rollout 人口不变。[受限 latent sampling 对照](https://arxiv.org/html/2602.14077v1)在两种 backbone 中显示中高采样预算的 pass@N 改善，但 N=2 有反退，且“至少一个正确”仍需外部识别才能交付。head 训练、多轨迹 forward 与验证均付费；实用实现对每步 log-density 按维取均值，而非 joint density 所需的求和，不能继承 exact trajectory ratio 或无偏 policy gradient 的保证。proposal 失配、有效多样性不足或 selector 不能可靠识别候选时，保留固定 recurrence、固定预算或已校准的简单噪声；可靠性仍由外部答案证据判断，不由 latent 分布名义上的可计算性签发。<!-- source-family:SF-2026-ARXIV-2602-14077 -->

还必须区分中间状态被生成与被后续计算消费。只监督最终答案或最后 latent state，可以留下看似完整的隐式轨迹，却未必让模型使用这些中间结果；答对、增加 latent 长度或轨迹收敛本身都不是计算路径证明。[受限 latent-supervision 对照](https://arxiv.org/html/2602.22441v1)在小模型与合成/增强任务中扰动最后 embedding 后仍保留部分正确输出，但早期 latent 与 KV 仍可访问，故只能诊断末状态接口的有限依赖，不能断言全部 latent 无用；单例 attention 图也不提供唯一因果。混合早期训练阶段可加强中间监督，但不同训练 recipe 和预算尚未完全单因素隔离；多次采样提高 pass@N 与多数答案更差可以同时发生，diversity 不等于已实现 BFS 或可交付正确性。训练暴露、额外轨迹与外部识别都要付费；监督或干预权限不足时，保留显式 CoT、固定预算和可核验工具，并分别验中间状态使用与最终答案，而不采用互相冲突的表格/正文精确收益数字。<!-- source-family:SF-2026-ARXIV-2602-22441 -->

### 涌现可以预警，但预警器不是能力证明

只在某个 checkpoint 首次越过 benchmark 阈值后宣布“涌现”，会把能力形成、指标阈值和事后挑选混在一起。一个更可审计的分支先冻结候选内部机制、anchor、预测区间和 false-alarm gate，再用独立 seed 与后续 checkpoint 检查该信号是否早于行为跃迁出现。这样可以把部分能力跃迁从事后叙事改为带拒绝条件的预测任务，也让“预测失败”成为可记录证据。

代价是需要 seed fleet、连续 checkpoint、预注册和足够多的负对照；内部 head 的形成也可能只是与能力共同变化，而不是能力的充分原因。合成 grokking、诱饵语言和有限公开 checkpoint 上的校准结果不能证明任意新能力都可预测，更不能把预测区间当作发布许可。无法复现 anchor、false-alarm 超界或任务定义漂移时，仍应回到直接行为评价与外部证据。<!-- source-family:SF-2026-ARXIV-2609-19000 -->

## Review notes

- `SF-2026-ARXIV-2601-11517` — Daily `2026-01-20`增量；[explanation transfer exact-v1](https://arxiv.org/html/2601.11517v1) §2/3、Table4与必要AppA2。2+1+2=5，跨模型一致性/正确性/faithfulness接口差额深入；保留一致错、答案去除混杂、GRPO transfer accuracy不升、多候选费用和人评性质，不授忠实解释或高风险可靠性。root实际必要原证/owner PRE通过并授窄锁；作者实际正文/完整邻接/本注已顺读，root实际顺读150–187/本注，POST通过，窄锁释放。未核artifact/复现，非日级验收。

- `SF-2025-ARXIV-2509-04664` — Daily `2025-09-06`；精确 v1 §3.1–3.2、Appendix A 与 §4.1/Appendix E。正文采用有效性分类到生成错误的条件联系，不采用无条件必然幻觉、部署错误率或 truth-calibration 保证；评分激励的完整机制归属 Ch66。必要原文和现有论证已核对，Mendel非写入者实际核正文及完整邻接并通过；未复现实验。

- `SF-2026-ARXIV-2602-14759` — Daily `2026-02-18`；[exact-v1](https://arxiv.org/html/2602.14759v1) §II–IV必要方法与直接反侧。2+1+2=5，frozen-loop参考缓存/插值的条件差额深入；naive扫描全退、WinoGrande区间选择、跨模型/norm混杂、ARC-E与局部MCQ人口保留，不采用有效激活域保证或零成本。root 必要源/actual owner PRE通过；实际正文/完整邻接与本末注经root非作者POST通过，窄锁释放，未核artifact/复现，非日级。

本章使用 operational capabilities 讨论“智能”，不对意识作结论，也不把 next-token prediction 描述为必然学得真实世界模型。后续 Review 应持续分离 base model、post-training、in-context behavior 与 tool-augmented system 四种能力来源，并在新增 emergence 案例时同时检查指标连续性和反方证据。

优先核验入口：

- Tom B. Brown et al., "Language Models are Few-Shot Learners", 2020: https://arxiv.org/abs/2005.14165
- Jason Wei et al., "Emergent Abilities of Large Language Models", 2022: https://arxiv.org/abs/2206.07682
- Rylan Schaeffer, Brando Miranda, Sanmi Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?", 2023: https://arxiv.org/abs/2304.15004
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Shunyu Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", 2022: https://arxiv.org/abs/2210.03629
- Shivam Garg et al., "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes", 2022: https://arxiv.org/abs/2208.01066
- Saurav Kadavath et al., "Language Models (Mostly) Know What They Know", 2022:
  https://arxiv.org/abs/2207.05221
- Lorenz Kuhn, Yarin Gal, Sebastian Farquhar, "Semantic Uncertainty", 2023:
  https://arxiv.org/abs/2302.09664
- Stephanie Lin, Jacob Hilton, Owain Evans, "TruthfulQA", 2021:
  https://arxiv.org/abs/2109.07958
- Stephanie Lin, Jacob Hilton, Owain Evans, "Teaching Models to Express Their Uncertainty in Words", 2022:
  https://arxiv.org/abs/2205.14334
- Kartik Ahuja et al., "Interventional Causal Representation Learning", 2023:
  https://proceedings.mlr.press/v202/ahuja23a.html
- Emre Kiciman et al., "Causal Reasoning and Large Language Models: Opening a New Frontier for Causality", 2023:
  https://arxiv.org/abs/2305.00050
- Zhijing Jin et al., "CLadder: Assessing Causal Reasoning in Language Models", 2023:
  https://arxiv.org/abs/2312.04350

- `SF-2026-ARXIV-2601-03542` — Daily `2026-01-09`；[Layer Order Inversion exact-v1](https://arxiv.org/html/2601.03542v1) §3.1–4.3、Limitations。原2+1+3=6，采用 probe layer/token/解释 prompt/raw-GF-LF/Correct 条件人口与因果 hop 的分账，三四跳反转不否定两跳或所有组合；不采用缺 targeted causal validation 的 recall/Attention 功能解释。未复现；jan01_v3实际必要原源与owner写前通过，并实际顺读正文、前后邻接及源注POST通过；日级Gate未验。

- `SF-2026-ARXIV-2602-14077` — Daily `2026-02-18`；[GTS exact-v1](https://arxiv.org/html/2602.14077v1) §3–5及必要 Appendix A/B。2+1+2=5，冻结 recurrence/可训条件 proposal 的实际差额深入；保留 diagonal family、dim-mean 密度比与 exact joint ratio 区别、N2反侧、pass@N识别与训练/多轨迹费用，不采用无偏或普遍推理改善。正文20k与附录10k预算表述分开，未核代码或复现。root 必要源/actual owner PRE及实际正文/完整邻接与末注POST通过，非日级。

- `SF-2026-ARXIV-2602-22441` — Daily `2026-02-28`；[Latent supervision exact-v1](https://arxiv.org/html/2602.22441v1) §2/4/5、blocks26–32、43–67、73–100。3+1+3=7；末embedding干预保留早latent/KV，计算路径与末答案差额深入；训练混杂、Pass@N/Maj@N反侧与费用近文，Table4/paragraph78冲突数字不采用。root必要原源/actual owner PRE通过并授单段及自身末注窄锁；作者实际正文及完整邻接顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21978` — Daily `2026-02-27`；[CxMP exact-v1](https://arxiv.org/html/2602.21978v1) §3–4/Fig3/5/6/Table3必要控制，2+1+2=5；形式acceptability与constructionmeaning学习/验收不互签差额深入，samecheckpoint/likelihood有限证据、生成器/实体/虚构词支持限制、instruction反侧及材料/人评/评分费用近正文。root必要原源/actual owner PRE及实际正文53/完整邻接37–60与自身末注358非作者POST通过，窄lease释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-09992` — Daily `2026-02-12`补遗漏；[exact-v1](https://arxiv.org/html/2602.09992v1)。本日具名必要方法、关键评价与直接反侧由root独立Source限定通过，actual owner/局部邻接及逐字拟文PRE通过后授窄锁；作者已写最小差额，review_20260214非作者实际新正文、完整局部邻接及本人末注POST通过，窄锁释放，不授DAY。原件与配置/中心争议边界见本日同名前缀review笔记；未核artifact或复现。

- `SF-2026-ARXIV-2603-10573` — Daily `2026-03-13`补查；[exact-v1](https://arxiv.org/html/2603.10573v1) §2–5、T1及B/C必要对照。2+1+2=5，mar13_admission_review非准备者实际Source、Ch8具体差额及收紧PRE通过；root两段融入ICL估计程序与comparator资格交接。只采用局部mean/variance任务、known-parameter oracle权限与相关/因果边界，不采用Eq2为有限context严格Bayes身份，不排除learned kernel。未核artifact或复现；mar13_admission_review非writer实际新增、完整ICL邻接和本人末注POST通过，root回读确认、窄锁释放，不授DAY。
