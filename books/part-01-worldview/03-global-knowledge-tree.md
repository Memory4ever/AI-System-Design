# 第3章 AI System 全局知识树

**Knowledge Tree:** Part I 世界观：AI 为什么会发展成今天这样
**Stable Knowledge Node ID:** `WORLDVIEW-KNOWLEDGE-TREE`
**Legacy Chapter:** Ch3
**Status:** Draft

**Roadmap Intent:** 建立 Data、Training、Model、Inference、Serving、Scheduling、Observability、Evaluation、Agent 的全局地图。

## 本章要回答的问题

面对一个新模型、新论文或新框架，怎样判断它位于 AI System 的哪一层，解决什么长期问题，又会把瓶颈推向哪里？

第 1 章说明了为什么不能把 AI System 缩减为模型部署，第 2 章说明了模型能力如何在历史中迁移。本章进一步给出全书的坐标系：**AI System 应同时用正式阅读与所有权主干、系统原语横线理解；前者确定一个问题由哪个 Part 主要展开，后者回答 compute、memory、communication、scheduling 与 state 怎样穿过多个阶段。**

知识树的目的不是收纳更多名词，而是保持问题边界稳定。产品会更名，框架会替换，最佳实践会变化；数据如何形成能力、能力如何被交付、昂贵资源如何被调度、概率输出如何被评估、动作如何被约束，这些问题不会随工具变化而消失。

## 为什么“模型 + API”不是一张足够的地图

假设团队已经训练出一个 checkpoint，并用推理引擎暴露了 HTTP API。从产品演示看，系统似乎只剩三层：

```text
Application -> API -> Model
```

这张图能解释一次成功调用，却解释不了生产中的失败。

当回答质量下降时，原因可能是训练数据变化、checkpoint 回归、prompt 变化、retrieval 失败、上下文截断、sampling 参数变化，也可能是业务输入已经偏离离线评估分布。只看 API 层，无法判断应该修数据、训练、评估还是运行时。

当延迟上升时，原因可能是长 prompt 增多、KV Cache 容量不足、batch 形态恶化、GPU placement 不合理、网关排队或工具调用变慢。只看模型层，无法解释端到端路径。

当成本失控时，团队需要回答的不只是“用了多少张 GPU”，而是训练和在线推理分别消耗了什么资源，容量是否转化为有效吞吐，哪个模型版本、租户和业务在产生费用，以及质量提升是否值得额外成本。

当模型开始调用工具时，API 图更会遗漏状态、权限、重试、补偿、审计和环境反馈。此时一次请求已经不是一次纯函数计算，而是一个可能持续多步、改变外部状态的运行过程。

因此，失败不在于这张图是假的，而在于它把最需要设计的部分压缩掉了。更有用的知识树必须能回答四类问题：能力从哪里来，能力怎样被交付，系统怎样被控制，以及模型怎样进入行动闭环。

## 第一类系统责任：能力如何被生产

模型能力不是写进代码的规则，而是数据、架构、目标函数和优化过程共同形成的结果。能力生产链可以先压缩为：

```text
Data -> Training -> Checkpoint -> Evaluation
```

`Data` 不只是对象存储中的文件。它包含来源、许可、清洗、去重、标注、采样、配比、版本和血缘。数据分布决定模型接触了什么经验，目标函数决定哪些误差会被惩罚，训练系统则把这些选择转化为参数更新。

`Training` 不只是运行一个脚本。可复现训练需要固定代码、配置、数据版本、随机性、硬件拓扑和依赖；规模扩大后，还要处理并行策略、通信、容错、checkpoint 和资源调度。

`Checkpoint` 是能力的载体，但不是孤立二进制。它需要模型结构、tokenizer、训练配置、权重格式、许可证、评估结果和部署约束等元数据，才能被正确比较、加载、回滚和审计。

`Evaluation` 不是生产完成后的附属测试，而是决定“什么算能力”的控制信号。没有与业务风险相匹配的评估，训练 loss 下降只说明目标函数上的经验误差变化，不能证明模型更适合真实系统。

这条链路对应全书的 Part II 和 Part IV：Part II 解释能力载体内部如何计算，Part IV 解释数据和优化如何产生、调整与保存能力。

## 第二类系统责任：能力如何被交付

一个 checkpoint 只有被运行、调度并接入请求路径，才会成为用户可感知的能力。能力交付链可以写成：

```text
Registry -> Runtime -> Serving -> Gateway -> Client
                 |          |
                 +-> state <-+
```

`Registry` 管理模型版本、元数据、来源、审批和阶段状态。它回答“应该交付哪一个模型”，而不是执行矩阵计算。

`Runtime` 把模型结构、权重和硬件变成可执行的 token 计算过程。对 LLM 而言，它要管理 Prefill、Decode、KV Cache、batching、并行和显存。runtime 的职责是高效执行模型，不等于完整的服务生命周期管理。

`Serving` 管理副本、部署、扩缩容、健康检查、流量切换和请求生命周期。它可以调用某种 runtime，但二者不能混为一谈：同一种 runtime 可以被不同 Serving 系统承载，同一种 Serving 抽象也可以接入不同 runtime。

`Gateway` 处理统一入口、认证、限流、路由、协议、租户和部分策略。它能保护服务边界，却不能替代模型评估或底层 token 调度。

`Client` 看到的是端到端结果，因此系统最终要对完整路径负责，而不是只对 GPU kernel 或 HTTP 状态码负责。

交付链中最关键的新变化是运行时状态。传统无状态请求可以较容易地迁移和重试；LLM 生成依赖 KV Cache，长对话依赖 context，Agent 又会引入 memory、工具结果和任务状态。状态越多，调度、容错和隔离越不能只按“请求数”设计。

这条链路主要对应 Part V 和 Part VI：Part V 解释推理 runtime 如何工作，Part VI 解释它如何被组织成可复用、可治理的平台能力。

## 第三类系统责任：控制面如何形成闭环

只有生产和交付，没有控制闭环，系统会不断积累不可见的质量、成本和风险。控制与治理不是末端的一层，而是穿过所有链路的横切面：

```text
             Evaluation
                 |
Data -> Training -> Model -> Runtime -> Serving -> Feedback
  ^              |          |          |          |
  +--------------+----------+----------+----------+

Cross-cutting constraints:
Scheduling / Observability / Cost / Security / Governance
```

`Scheduling` 决定训练任务、批推理和在线 Serving 如何获得 GPU、网络、存储和队列优先级。它既是资源控制，也是业务优先级的物理实现。

`Observability` 记录系统发生了什么，包括 metrics、logs、traces、模型版本、prompt/context、token 使用和工具调用。可观测性提供事实，但不会自动判断输出是否正确。

`Evaluation` 判断模型或系统行为是否满足目标。离线评估适合可复现比较，在线评估反映真实流量，但会受到反馈偏差、用户差异和实验风险影响。两者需要互相校验。第 66 章将把这一职责展开为独立 Evaluation System：同时版本化被评估对象、数据或环境、scorer 与运行证据，再由风险政策决定是否发布、回滚或继续调查。

`Cost` 把 GPU 时间、显存占用、存储、网络和工程复杂度映射到业务约束。低单价不一定意味着低总成本；高吞吐也不一定意味着高有效产出，只有满足质量和 SLO 的请求才构成有意义的 goodput。

`Security` 与 `Governance` 决定数据能否使用、模型能否发布、租户能访问什么、动作是否越权、变更能否审计。能力越开放，硬边界越重要。

`Feedback` 把线上结果送回评估、数据、prompt、retrieval、训练或产品策略。它不是“把用户数据都拿去再训练”，而是先识别问题属于哪一层，再选择风险最小、验证成本最低的修正路径。

控制面的核心是比较目标与事实，并驱动受控变更。可以把它抽象为：

```text
desired objective
      |
      v
observe -> evaluate deviation -> decide -> act -> observe again
```

如果缺少其中任何一步，所谓平台就容易退化成工具门户：可以提交任务、部署模型，却不能证明系统正朝正确方向运行。

## 第四类系统责任：Agent 把生成变成行动

普通模型服务的闭环通常在答案返回后结束。Agent 则把模型放入持续与环境交互的运行过程：

```text
Goal -> Context -> Model decision -> Tool action -> Observation
  ^                                                |
  +---------------- state / memory / feedback -----+
```

模型在这里提供语义判断和候选行动，但完整能力来自模型与外部系统的组合。`Context` 暴露当前任务信息，`Tool` 提供行动接口，`Memory` 保留跨步骤或跨会话状态，`Workflow` 约束执行顺序，`Observation` 把环境变化送回下一轮决策。

朴素方案是让模型自由生成工具名和参数，并不断执行到它宣布完成。失败之处在于：语言上合理的行动不一定有权限，工具返回不一定可信，重试可能产生重复副作用，长链路中的一个错误可能被后续步骤放大。

因此 Agent 不是模型层上方的一块 UI，而是新的运行时系统。它至少需要结构化工具契约、权限最小化、状态持久化、幂等与补偿、预算和终止条件、trace、评估以及人工接管边界。Part VII 将专门展开这些问题。

## 一张可操作的全局地图

四类系统责任可以合并为下面的知识树：

```text
Capability Production
  Data -> Training -> Checkpoint -> Evaluation
             |             |
             v             v
Capability Delivery
  Registry -> Runtime -> Serving -> Gateway -> User
                 |
                 v
Agent Runtime
  Context -> Model -> Tool -> Environment -> Observation
      ^                                      |
      +------------- State / Memory ----------+

Cross-cutting Control
  Scheduling | Observability | Evaluation | Feedback
  Cost | Security | Multi-tenancy | Governance
```

这不是部署拓扑。真实系统可以把多个节点放进一个进程，也可以把一个节点拆成很多服务。知识树描述的是职责与长期问题，产品架构图描述的是某个组织在特定约束下如何落地这些职责。

区分二者很重要。例如，小团队可以用一个服务同时承担 Registry、Serving 和 Gateway 的部分职责，但这不代表这些问题相同；规模扩大后，它们的生命周期、权限和扩展方式通常会分离。反过来，大平台可能有很多控制器和服务，却仍然缺少有效 Evaluation 闭环。组件数量不能证明知识树完整。

## 七个 Part 如何落在树上

| Part | 主要问题 | 在全局树中的位置 |
| --- | --- | --- |
| Part I 世界观 | 为什么出现这些问题，如何组织它们 | 建立全局坐标系与边界 |
| Part II 模型 | 一个 token 如何经过模型变成输出 | Model mechanism 与 runtime state 的来源 |
| Part III 多模态、生成与世界模型 | 表示如何跨越 modality，并进入环境预测和物理行动 | Representation、generation、world state 与 action contract |
| Part IV Training System | 数据和优化如何产生、调整模型能力 | Capability Production |
| Part V Inference System | 模型如何在硬件约束下高效生成 | Runtime 与 token-level scheduling |
| Part VI AI Infrastructure | 多团队如何复用、交付、评估和治理能力 | Serving、Evaluation、platform control 与 cross-cutting concerns |
| Part VII Agent | 模型如何在状态与权限边界内执行任务 | Agent Runtime 与 environment feedback loop |

章节之间不是简单流水线关系。Part II 的 KV Cache 机制会直接约束 Part V 的显存管理；Part IV 的 checkpoint 格式会约束 runtime 加载；Part V 的延迟和成本会影响 Part VI 的容量治理；Part VII 的工具调用会反过来要求 Part VI 提供权限、trace 和审计。知识树的价值，正是让这些跨层约束可见。

## 第二个坐标轴：系统原语怎样跨越 Part

七个 Part 按阅读顺序与主要责任边界组织，适合作为从前到后的正式主干。Part I 提供元层坐标，Part II～VII 沿 Model、Multimodal/World/Action、Training、Inference、Infrastructure、Agent 展开。但只沿这条轴阅读，容易把 GPU memory、collective、scheduler 或 runtime state 误认为某个阶段的局部细节。它们实际上会在不同对象和时间尺度上反复出现。

因此全书增加第二个坐标轴：

| 系统原语 | 稳定问题 | 跨 Part 变化 |
| --- | --- | --- |
| Compute | 怎样把目标函数和模型语义映射成有效硬件工作 | 从矩阵与 Attention，扩展到并行算子、kernel、batch 与设备利用 |
| Memory | 哪些状态应驻留、复用、分片、迁移、持久化或淘汰 | 从参数与 activation，扩展到 KV、artifact、Context 和 Agent state |
| Communication | 谁与谁交换什么，在什么语义、算法和拓扑下完成 | 从 rank collective，扩展到 tensor、token、KV block 与异构数据路径 |
| Scheduling | 谁在何时获得有限资源或执行机会 | 从 pipeline slot，扩展到 token iteration、GPU placement 与 workflow action |
| State | 怎样保持 identity、version、ownership、ordering 与恢复边界 | 从 checkpoint，扩展到 request、cache、deployment、memory 和 workflow |

Memory 与 State 可能作用于同一对象，但问题不同：Memory 关心 bytes 的 placement、capacity、movement、retention 与 eviction；State 关心这些 bytes 的 identity、ownership、version、validity、commit 与 recovery。KV block 可以在 HBM、CPU 或 storage 间迁移，这是 Memory；哪一个 request、model revision 和 generation 可以消费它，则是 State。

两条轴的关系不是把一章复制到多个目录，而是确定“主要 owner”和“跨层约束”：

```text
formal reading / ownership axis:
  Part I: Worldview and coordinate system
  Part II-VII:
    Model -> Multimodal/World/Action -> Training
          -> Inference -> Infrastructure -> Agent

horizontal lenses:
  Compute | Memory | Communication | Scheduling | State
```

例如，第 36 章拥有分布式训练的通信基础，第 37～40 章解释并行机制怎样消费 collective；第 52、55 章则重新面对通信，但对象变成分布式推理中的 KV state。它们共享 latency、bandwidth、topology 和 completion 等原理，却不应合并成一个不分语义的“通信平台”。

这套双轴结构也提供两种阅读方式：

- **顺序阅读**：沿七个 Part 建立端到端 AI System。
- **主题阅读**：沿 Compute、Memory、Communication、Scheduling 或 State 追踪同一约束如何迁移。

第二种方式是索引和推理工具，不是另一套相互竞争的目录。

## 演化关系不能只画箭头

把旧技术与新技术连接起来很有价值，但箭头可能表达完全不同的关系。正式书稿必须至少区分：

1. **Direct Evolution**：新设计明确继承、扩展或替换旧设计。
2. **Layering / Dependency**：两个机制位于不同层并组合工作。
3. **Principle Reuse**：不同系统面对相似约束，复用 paging、pipeline、locality 等原则。
4. **Explanatory Analogy**：类比帮助形成直觉，但不证明历史继承或实现等价。

例如，PagedAttention 对 virtual memory 的 paging 思想属于明确的 principle reuse；KV Cache 并不是 CPU Cache 的直接后代。MPI、NCCL、UCC 与 NIXL 也不构成一条简单替代链：它们分别暴露并行编程、collective、统一 group communication 和异构 point-to-point data movement 等不同责任。

“系统考古”的目标不是为每个新技术寻找一个看起来相似的祖先，而是识别哪些约束没有变、哪些对象已经改变，以及新的抽象把旧问题推到了哪一层。

## 如何给一个新技术定位

遇到新框架或论文时，可以依次问七个问题。

第一，它直接改变的对象是什么：数据、参数、计算图、模型状态、请求、资源、评估信号，还是外部动作？对象决定它首先落在哪一层。

第二，它处于能力生产还是能力交付路径？训练加速与推理加速都可能使用量化或并行，但目标、状态和失败模式不同，不能因为术语相同就放在同一节点。

第三，它属于 data plane 还是 control plane？真正执行矩阵计算、传输 token、调用工具的是 data plane；决定部署、调度、路由、策略和版本的是 control plane。很多系统同时包含两者，需要分别分析。

第四，它优化什么指标，约束什么指标？吞吐、TTFT、TPOT、训练时间、显存、质量、可用性、成本和安全不能被一个“更快”概括。没有 workload 和约束条件的性能结论不能直接迁移。

第五，它引入了什么新状态和新耦合？例如 KV Cache 优化可能提高容量，却增加调度复杂度；自动工具调用扩大能力，却增加权限与恢复问题。

第六，如果移除产品名，它解决的问题是否仍然存在？如果答案是否定的，它可能只是短期集成细节；如果答案是肯定的，就可以把它挂到稳定知识树节点上，再比较不同实现。

第七，它与已有节点是什么关系：直接演化、分层依赖、原理复用还是解释类比？只有回答这一点，历史叙事才不会把并列层次误写成产品替代。

以 PagedAttention 为例，它首先作用于推理 runtime 的 KV Cache 内存管理，优化的是在显存约束下的有效容量与批处理机会，并把页表映射和调度协同引入系统。它不是 Serving 生命周期，也不是 GPU 集群 placement。以 KServe 为例，它主要位于 Serving 与平台控制面，解决声明式生命周期和 Runtime 抽象；它不会替代底层 attention kernel。这样的定位比记住功能列表更稳定。

## 设计边界与常见误区

第一，不要把知识树画成严格单向流水线。Evaluation 既发生在训练后，也发生在上线前、运行中和变更后；Feedback 可能回到数据、prompt、retrieval、模型或策略。真实 AI System 是带反馈的图。

第二，不要用组织边界代替技术边界。训练团队、平台团队和业务团队如何分工是组织选择，不代表 Data、Runtime、Serving、Evaluation 的职责可以混淆。

第三，不要把所有横切问题都包装成独立平台。统一能力可以减少重复，但每增加一个平台层都会增加接口、状态和协调成本。只有当复用、治理或规模收益大于抽象成本时，平台化才成立。

第四，不要把 framework taxonomy 当作知识树。一个框架可能跨越多个节点，一个节点也可能由多个框架协作完成。强行一一对应会遮蔽真正的接口和责任边界。

第五，不要让全局地图替代局部机制。知识树告诉我们去哪里找问题，却不能替代 Attention 数学、分布式通信、KV Cache 容量模型或安全策略。后续章节会向下展开这些机制。

## 本章在知识树中的位置

本章是全书的导航层。第 1 章建立学习 AI System 的必要性，第 2 章解释能力范式为何迁移，本章把迁移后出现的问题组织为稳定节点。第 4～8 章会补足能力产生的模型直觉，第 9 章会解释支撑能力的系统形态如何演化，第 10 章再用长期约束检验这张树是否仍然有效。

读完本章后，后续每一章都应能回答两件事：它改变了全局树中的哪个对象，以及它通过什么代价改善了什么约束。如果无法回答，这个知识点很可能还没有被真正放进 AI System。

## 自检问题

1. 为什么 `Application -> API -> Model` 能解释 demo，却不能解释生产故障？
2. 能力生产链与能力交付链分别管理什么对象？Checkpoint 和 Registry 为什么不是同一概念？
3. Runtime、Serving、Gateway 的职责边界是什么？
4. 为什么 Evaluation 既属于能力生产闭环，也属于线上控制闭环？
5. 正式阅读与所有权主干、生命周期阶段、系统原语横线分别回答什么问题？
6. 为什么 Communication 或 Memory 不适合直接替换 Training、Inference 等 Part？
7. Agent 相比普通模型 Serving 新增了哪些状态和责任边界？
8. 为什么知识树不是产品架构图，也不是组织架构图？
9. Direct Evolution、Layering、Principle Reuse 和 Analogy 有什么区别？
10. 选择一个你熟悉的 AI 框架，用“对象、路径、平面、指标、状态、长期问题、关系类型”七个问题重新定位它。

## 小结

AI System 的全局地图不是模型周围组件的清单，而是两组相互正交的坐标。七个 Part 构成正式阅读与章节所有权主干，其中 Part I 建立坐标，Part II～VII 展开 Model、Multimodal/World/Action、Training、Inference、Infrastructure 与 Agent；四类系统责任解释能力生产、交付、控制与行动，系统原语横线则回答 Compute、Memory、Communication、Scheduling 与 State 怎样反复约束这些阶段。

七个 Part 是唯一正式目录，横向主线负责导航和比较。以后技术栈变化时，我们不需要重建世界观，只需要判断新设计改变了哪个对象、缓解了哪个瓶颈、引入了什么状态和 trade-off，以及它与旧设计究竟是演化、分层、原理复用还是类比。这正是知识树比工具清单更有长期价值的原因。

## Review notes

本章有意保持在职责和问题层，不展开具体框架部署，也不重复第 1 章对 AI System 必要性的论证。本轮结构 Review 增加生命周期与系统原语的双轴知识树，并把技术连接区分为 direct evolution、layering、principle reuse 与 analogy。后续 Review 应检查两条轴能否容纳新增章节、术语边界是否一致，以及主题阅读路径是否仍指向明确的章节 owner。

优先核验入口：

- D. Sculley et al., "Hidden Technical Debt in Machine Learning Systems", 2015: https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html
- Denis Baylor et al., "TFX: A TensorFlow-Based Production-Scale Machine Learning Platform", 2017: https://research.google/pubs/tfx-a-tensorflow-based-production-scale-machine-learning-platform/
- Martin Abadi et al., "TensorFlow: A System for Large-Scale Machine Learning", 2016: https://research.google/pubs/tensorflow-a-system-for-large-scale-machine-learning/
- Ashish Vaswani et al., "Attention Is All You Need", 2017: https://arxiv.org/abs/1706.03762
- Shunyu Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", 2022: https://arxiv.org/abs/2210.03629
