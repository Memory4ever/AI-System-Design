# 第8章 大模型为什么会产生智能

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
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

## Post-training 把通用预测器塑造成可用接口

预训练数据包含网页、代码、对话、文档等多种文本。一个只做 next-token prediction 的 base model 擅长续写，却不天然知道“用户问题应被直接回答”“危险请求应拒绝”或“输出必须满足某个 schema”。

Instruction tuning、SFT 和 preference-based post-training 使用更接近产品交互的数据与目标，改变模型在给定指令下选择什么行为。它们通常不是从零创造全部知识，而是选择、重组和强化预训练已形成的能力，使模型更容易按照任务接口工作。

这解释了为什么参数规模和 pretraining loss 相近的模型，最终可用性仍可能差异很大。能力表现来自 base model、post-training、system prompt、context、sampling 和外部系统的组合。

也要保持边界：本章不展开 SFT、RLHF、DPO 或 GRPO 的优化机制，它们属于 Part III。这里仅说明 post-training 是“广泛潜在能力”变成“可调用行为”的关键条件，并且可能同时改善可用性、压制某些能力或引入新的偏好偏差。

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

工具也放大风险。模型可能选择错误工具、生成错误参数、相信恶意 observation、重复执行有副作用操作或越过权限。Tool use 证明语言模型可以参与行动闭环，不证明它能独立承担开放环境中的可靠控制。权限、schema、幂等、确认、trace 和补偿属于 Part VI 的 Agent runtime。

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

这条链不反向证明“出现能力，所以某条 scaling law 必然成立”。也不把工具调用等同于完整 Agent。Part III 会展开 post-training，Part VI 会展开 Context、Tool Calling、Planning、Memory 和 Agent Platform。

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

## 小结

大模型的广泛能力并非来自 next-token prediction 之外的神秘目标，而是来自这个统一目标在大规模、多样数据上的要求：为了持续降低预测误差，模型需要形成可复用的语言、知识和任务结构表示。规模、Transformer、context 与 post-training 又让这些表示更容易被调用和组合。

但能力是有条件的。emergence 受指标影响，tool use 把模型能力变成系统能力的同时也放大风险，流畅输出更不等于稳定可靠。AI System 的责任，是把“模型有时能够做到”转化为“系统在明确边界内可以被信任地做到”。

## Review notes

本章使用 operational capabilities 讨论“智能”，不对意识作结论，也不把 next-token prediction 描述为必然学得真实世界模型。后续 Review 应持续分离 base model、post-training、in-context behavior 与 tool-augmented system 四种能力来源，并在新增 emergence 案例时同时检查指标连续性和反方证据。

优先核验入口：

- Tom B. Brown et al., "Language Models are Few-Shot Learners", 2020: https://arxiv.org/abs/2005.14165
- Jason Wei et al., "Emergent Abilities of Large Language Models", 2022: https://arxiv.org/abs/2206.07682
- Rylan Schaeffer, Brando Miranda, Sanmi Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?", 2023: https://arxiv.org/abs/2304.15004
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Shunyu Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", 2022: https://arxiv.org/abs/2210.03629
- Shivam Garg et al., "What Can Transformers Learn In-Context? A Case Study of Simple Function Classes", 2022: https://arxiv.org/abs/2208.01066
