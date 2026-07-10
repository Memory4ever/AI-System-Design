# 第10章 AI 的未来

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Status:** Draft

**Roadmap Intent:** Agent、个性化模型、世界模型、端侧智能与 AI 平台化。

## 本章要回答的问题

当模型、硬件、数据和产品变化速度都很快时，怎样讨论 AI 的未来而不退化成厂商名单、发布时间表或单一路线预言？哪些约束足够稳定，可以帮助我们判断未来设计？

本章的中心命题是：**未来不是从当前产品向前画一条直线，而是在 compute、memory、energy、latency、privacy、trust 与真实环境反馈等长期约束下，比较多种可能系统形态。**对每个方向，都应依次分析驱动力、可能设计、新瓶颈和关键不确定性。

因此，本章不预测某家公司胜出，也不把研究 demo 写成必然产品。它的任务是用 Part I 建立的知识树，对 Agent、个性化、世界模型、端侧智能和平台化做约束驱动的情景分析。

## 为什么按时间点预测容易失败

朴素的未来叙事通常是：模型继续变大，benchmark 继续提高，某项能力在某年成熟，随后全面替代现有软件。这种叙事忽略了三个事实。

第一，能力曲线不等于部署曲线。一个系统可以在 benchmark 上展示能力，却因成本、延迟、可靠性、数据权利或组织风险无法大规模使用。

第二，技术路径会相互替代。更大的 base model、更多高质量数据、post-training、retrieval、tool use、inference-time search 和专用小模型都可能改善同一任务。约束变化时，最优组合会改变。

第三，未来瓶颈通常来自成功本身。上下文变长会增加 KV Cache 和质量验证压力；Agent 能执行更多动作，会增加权限与责任问题；端侧模型保护部分隐私，却引入设备异构、更新和本地攻击面。

所以更可靠的分析单元不是“哪项产品会流行”，而是：

```text
Driver -> Possible Design -> New Bottleneck -> Uncertainty
```

只要新瓶颈与不确定性没有被写出来，未来判断就还不是系统设计判断。

## 一组不会轻易消失的约束

### Compute

训练、后训练、推理和 Agent 多步执行都会消耗计算。即使单次 FLOPs 成本下降，总需求也可能因模型调用增加而上升。未来设计需要比较训练一次与推理多次、通用模型与专用模型、参数计算与外部工具计算。

### Memory 与数据移动

参数、activation、KV Cache、retrieval index 和 Agent state 都占用不同层级存储。很多 workload 的实际瓶颈不是算术峰值，而是数据能否在显存、内存、网络和存储之间及时移动。模型结构与 runtime 会继续围绕 memory hierarchy 协同设计。

### Energy 与物理基础设施

更多 accelerator 不只意味着采购成本，还涉及电力、散热、机房、供应链和区域容量。energy per useful outcome 会比单纯峰值算力更接近长期约束，但“useful”必须包含质量和业务结果，而不是只统计 token。

### Latency

交互式应用、控制系统和端侧体验有不同延迟上限。可以通过 batching 提高吞吐，却可能增加等待；可以用更强模型减少错误，却可能延长响应。未来系统仍会在 quality、latency 与 cost 之间做 workload-specific 权衡。

### Privacy 与数据权利

个性化需要用户数据，持续学习需要反馈，Agent 需要访问工具与上下文。这些能力与数据最小化、用途限制、地域、删除、审计和用户控制存在天然张力。隐私不是训练完成后加一层脱敏，而是决定数据能在哪里计算和保留。

### Trust

能力越强，错误影响越大。事实性、校准、安全、权限、可解释证据、人工接管和责任分配共同决定系统是否可被信任。更高 benchmark 分数不能自动降低长尾风险。

这些约束不会给出唯一架构，却能排除缺乏闭环的愿景。

## 方向一：Agent 从回答走向长程任务

### 驱动力

LLM 已能把自然语言映射为代码、查询和工具参数。若模型可以在 observation 反馈下持续行动，用户不必手工串联每个软件步骤，AI 能力就从内容生成扩展为任务完成。

### 可能设计

未来 Agent 未必是一个自由循环的大模型。更可能出现分层系统：模型负责不确定的语义判断与计划，workflow 负责稳定步骤，tool runtime 负责权限和执行，memory 保存必要状态，evaluator 或 verifier 检查关键结果。

```text
goal
 -> planner / policy
 -> constrained workflow
 -> typed tool execution
 -> observation and verification
 -> durable task state
```

高风险动作可能要求 deterministic policy 或 human approval，低风险探索允许更开放的模型控制。不同任务会在 autonomy 与 control 之间选择不同位置。

### 新瓶颈

任务越长，单步错误、环境变化和上下文污染越容易累积。工具具有副作用后，retry 不再天然安全；并行 Agent 还会产生共享状态冲突、预算竞争和责任不清。Token throughput 不足以衡量系统，task success、time to completion、recovery、action cost 和 harm 都要进入 Evaluation。

### 不确定性

尚不清楚通用长程 planning 能在多大程度上依靠更强 base model 获得，还是必须通过环境训练、搜索、专用 verifier 与结构化 workflow 组合。也不清楚用户愿意把哪些权限交给自动系统。Agent 的未来首先受可靠性和制度边界限制，而不只是模型能力。

## 方向二：个性化从统一模型走向受控适配

### 驱动力

统一模型服务平均用户，而真实任务依赖个人语言、偏好、历史、组织知识和设备环境。把所有个性信息塞入 prompt 会增加 token、latency 和泄露风险，也难以维护长期状态。

### 可能设计

个性化可以发生在多层：检索用户授权的 memory，动态选择 prompt 或 tool，训练小型 adapter，进行 federated learning，或者在端侧维护局部模型。LoRA 等参数高效方法表明行为适配不一定要求复制全部基础参数；federated learning 则展示了数据留在设备、聚合局部更新的一种路径。

系统可能把稳定通用能力放在共享 base model，把组织与个人差异放在可撤销的 context、memory、adapter 或 policy 中。这样比为每个用户训练完整模型更容易更新和治理。

### 新瓶颈

个性化状态会迅速增加版本数量。平台必须知道某次输出使用了哪个 base、adapter、memory、policy 和数据授权。用户偏好也可能与安全、组织政策或事实正确性冲突。删除权要求系统不仅删除原始记录，还要处理索引、缓存、adapter 与衍生 artifact。

### 不确定性

个性化收益是否值得状态和隐私成本，取决于任务重复度与用户控制需求。Federated learning 减少原始数据集中化，不自动提供完整隐私；更新仍可能泄露信息，还需要 secure aggregation、differential privacy 或其他保护。不同适配层的效果、可撤销性和风险仍需按场景验证。

## 方向三：世界模型从文本关联走向环境预测

### 驱动力

语言描述了世界，却不是世界本身。机器人、自动控制、游戏、科学和交互环境要求系统预测动作之后会发生什么，并在视觉、空间、时间和物理反馈中规划。仅生成语言合理的行动不足以保证环境结果正确。

### 可能设计

World model 可以学习环境状态如何随 action 演化，再让 policy 在模型内部想象候选轨迹。Dreamer 一类工作展示了从学习到的世界模型中改进行为；生成式交互环境研究则探索从视频或动作条件数据形成可交互预测。

未来系统可能组合 multimodal perception、latent dynamics、planning、memory 和 real-world feedback。语言模型负责高层目标与知识，world model 负责环境后果预测，低层 controller 负责实时执行。

### 新瓶颈

预测像素或视频逼真，不等于对行动后果因果正确。模型在常见轨迹上表现良好，仍可能在安全关键长尾上累积误差。真实环境数据昂贵且受限，simulator 又存在 sim-to-real gap。规划在错误世界模型上越深入，可能越自信地走向错误结果。

### 不确定性

世界模型需要多大程度的显式因果结构、物理 inductive bias 和在线适应仍是开放问题。不同领域是否能共享一个通用 world model，还是需要大量专用模型，也没有确定答案。评估必须从视觉质量转向 intervention、long-horizon prediction 与实际控制结果。

## 方向四：端侧智能在云与设备之间重画边界

### 驱动力

云模型具有集中更新和大规模 compute 优势，但网络 latency、离线可用性、云推理成本与敏感数据上传会限制场景。硬件与小模型效率提升，使更多识别、生成和 Agent 子任务有机会在设备执行。

### 可能设计

端侧并不意味着所有计算都本地化。更可能出现 hybrid routing：低延迟、隐私敏感或高频任务在端侧完成；复杂、低频或需要新知识的任务进入云端；中间层根据网络、battery、quality 和 policy 动态选择。

模型侧可能使用小型架构、quantization、distillation、speculative collaboration 与 adapter；系统侧需要 hardware-aware compilation、模型分发、增量更新、设备能力检测和本地缓存。MobileLLM 等研究说明，sub-billion 模型的架构设计本身会显著影响端侧可行性，不能只把云模型按比例缩小。

### 新瓶颈

设备在 memory、thermal、battery 和 accelerator 能力上高度异构。模型更新会受到包大小、网络和版本碎片影响；本地数据与 memory 也会增加设备丢失、恶意应用和物理攻击风险。云端统一 observability 在本地隐私约束下不再成立，故障证据更难收集。

### 不确定性

哪些任务能在可接受质量下完全端侧运行，会随模型与芯片共同变化。Hybrid routing 的收益还依赖网络、调用频率、数据敏感性与云端价格。端侧不是云的终结，而是把 placement 变成按请求、状态和策略动态决定的问题。

## 方向五：AI 平台从工具集合走向能力控制面

### 驱动力

模型、runtime、adapter、数据、评估、Agent 和工具快速增加后，每个团队独立拼接会产生重复集成、不可审计状态和 hidden technical debt。组织需要复用资源、缩短交付时间，并对成本和风险建立统一边界。

### 可能设计

未来平台的稳定核心不应是某个模型或框架，而是对象、契约和控制闭环：

```text
capability specification
-> model / data / runtime selection
-> deployment or task execution
-> observation and evaluation
-> policy-driven iteration
```

平台可以提供统一 identity、artifact metadata、runtime interface、evaluation contract、policy、trace 和 cost attribution；底层执行允许多个训练框架、推理引擎、云与端侧环境共存。

AI 平台也可能从 infrastructure provisioning 向 capability routing 演化：根据质量、latency、cost、privacy 和地域，为请求选择模型、context、tool 与执行位置。此时路由不只是网络流量问题，而是带 Evaluation 约束的决策系统。

### 新瓶颈

统一控制面会增加 blast radius。错误 policy、registry metadata 或 evaluator 可能影响所有团队。抽象更新速度若跟不上模型与 runtime，平台会成为阻力；接口过于开放又无法实现治理。平台还必须证明自己的 ROI，避免把局部团队的简单流程强制变成重型系统。

### 不确定性

哪些对象可以跨模型和业务稳定标准化，哪些必须保留领域特性，仍会持续变化。平台边界也受组织规模影响：同一抽象对百人组织可能必要，对小团队可能过早。判断标准应是是否减少重复状态、形成控制闭环并改善交付结果，而不是 UI 或组件数量。

## 五个方向其实在同一张图里

这些方向不是并列产品赛道。它们会互相组合：个性化 Agent 需要 memory 与权限；端侧 Agent 需要本地工具和云端协同；世界模型可能成为具身 Agent 的环境预测组件；平台控制面则管理模型、adapter、runtime、tool 和 Evaluation。

可以用第 3 章的知识树重新定位：

```text
Capability Production:
  better data, world-model training, personalization updates

Capability Delivery:
  cloud/edge placement, specialized runtime, model routing

Control and Governance:
  privacy, trust, evaluation, cost, policy, audit

Agent Loop:
  context, memory, tool, action, environment feedback
```

未来系统的竞争力很可能不只来自拥有更强模型，而来自能否在这些链路之间建立更短、更可靠的反馈闭环。

## 怎样把未来判断变成可验证假设

面对一个趋势，可以使用以下检查框架。

第一，写出驱动力。是能力不足、成本过高、latency、隐私、数据稀缺，还是用户交互摩擦？

第二，列出至少两个可能设计。若只有一条路线，通常是在复述当前产品而不是分析约束。

第三，指定主指标和硬门槛。比如 task success、energy、p95 latency、privacy budget、human intervention rate，而不是笼统的“更智能”。

第四，写出新状态与故障模式。任何能力增强都会带来需要管理的对象。

第五，定义可证伪条件。哪些实验结果会让我们放弃这条路线？哪些变化会使替代方案更优？

第六，标注时间敏感假设。硬件价格、模型版本和法规会变化；机制与约束可以保留，具体数字要重新核验。

这种方法不能消除不确定性，但能防止把愿景包装成结论。

## 本章在知识树中的位置

本章是 Part I 的收束。第 1～3 章建立为什么需要 AI System 及其全局地图，第 4～8 章解释模型学习、表示、可扩展架构、Scaling 与能力边界，第 9 章回看系统形态如何演化。本章再用长期约束向前检验：无论具体技术怎样变化，能力生产、能力交付、控制治理和 Agent 闭环仍是稳定分析框架。

下一章进入 Part II，从 Tokenizer 开始沿一个 token 的生命周期下钻。未来判断只有建立在具体模型机制和系统成本之上，才不会停留在趋势口号。

## 自检问题

1. 为什么能力曲线不能直接当作部署时间表？
2. “驱动力 → 可能设计 → 新瓶颈 → 不确定性”如何改善趋势分析？
3. compute、memory、energy、latency、privacy、trust 之间有哪些典型冲突？
4. Agent 为什么更可能采用模型与 workflow 混合控制，而非完全自由循环？
5. 个性化状态为什么必须可追踪、可撤销并受数据授权约束？
6. 生成逼真的环境预测为什么不等于因果正确的 world model？
7. 端侧智能为什么更可能形成 hybrid placement，而不是简单替代云？
8. AI 平台的稳定抽象应围绕产品名还是对象与控制闭环？
9. 五个未来方向如何映射回第 3 章的四条主干？
10. 为一个你关注的 AI 趋势写出可证伪条件和会改变结论的约束。

## 小结

讨论 AI 的未来，最重要的不是给出确定时间点，而是保持因果和边界。Agent、个性化、世界模型、端侧智能与平台化都有真实驱动力，也都会产生新的状态、成本、风险和组织问题。

长期可复用的判断来自约束：compute 与 energy 限制可扩展性，memory 与 latency 塑造 runtime，privacy 限制数据流动，trust 决定能力能否进入高风险流程。未来技术会变化，但用这些约束分析能力生产、交付、治理和行动闭环的方法仍然有效。

## Review notes

本章是情景分析，不是预测清单。后续 Review 应重新核验所有时间敏感研究入口，但不因新产品出现就重写主线；只有当驱动力、系统对象或长期约束发生变化时，才调整知识树判断。新增方向必须同时写出替代设计、新瓶颈和可证伪条件。

优先核验入口：

- Shunyu Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", 2022: https://arxiv.org/abs/2210.03629
- John Yang et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", 2024: https://arxiv.org/abs/2405.15793
- Edward J. Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", 2021: https://arxiv.org/abs/2106.09685
- Brendan McMahan et al., "Communication-Efficient Learning of Deep Networks from Decentralized Data", 2017: https://proceedings.mlr.press/v54/mcmahan17a.html
- Danijar Hafner et al., "Mastering Diverse Domains through World Models", 2023: https://arxiv.org/abs/2301.04104
- Jake Bruce et al., "Genie: Generative Interactive Environments", 2024: https://arxiv.org/abs/2402.15391
- Pascale Fung et al., "Embodied AI Agents: Modeling the World", 2025: https://arxiv.org/abs/2506.22355
- Zechun Liu et al., "MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases", 2024: https://arxiv.org/abs/2402.14905
- D. Sculley et al., "Hidden Technical Debt in Machine Learning Systems", 2015: https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
