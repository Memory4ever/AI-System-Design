# 第82章 Multi-Agent

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-MULTI-AGENT`
**Legacy Chapter:** Ch78
**Status:** Draft

**Roadmap Intent:** 多个智能体之间如何分工、协作和互相校验。

## 本章要回答的问题

为什么创建多个 persona 不自动带来更强能力？Multi-Agent 何时提供并行、专业化或独立校验，何时只放大 token 成本、共识偏差和状态混乱？多个 Agent 的权限与责任如何隔离？

本章的核心判断是：**Multi-Agent 是责任、状态和通信的系统分解，不是角色提示词的数量。只有任务可分解、接口可验证或观察真正独立时，多 Agent 才可能超过单 Agent + Workflow。**

## 先建立单 Agent Baseline

一个模型可以在不同步骤切换 role。把同一模型复制成 planner、coder、reviewer，若它们共享训练分布、Context 和 evidence，错误高度相关。

Multi-Agent 引入额外成本：

```text
total_cost
= model calls
 + inter-agent messages
 + context duplication
 + coordination
 + merge / conflict resolution
 + longer critical path
```

因此应先比较单 Agent、单 Agent + deterministic verifier、单 Agent + parallel tools，再判断多 Agent 是否有增量价值。

这个 baseline 还可以写成一个信息上界：如果所有 agents 只看到同一 evidence、使用等价 policy，且通信与 voting
没有引入新的 observation，那么多跳 delegated decision network 并不会创造额外信息。更精确地说，论文比较的
上界是一个观察同一组 exogenous signals 的理想 centralized Bayes decision maker；结论依赖 bounded loss、
ancillary randomization 在给定 exogenous information 后与目标条件独立，以及 common-evidence 情形不再获得新信息
等假设。它不是在断言受固定 compute、latency 或 context 限制的现实单 Agent 一定能模拟任意 DAG。
Multi-Agent 的正当理由因此不是“讨论带来智慧”，而是
系统确实引入了新的信息、并行环境交互、异构能力、隔离权限或可验证的独立误差：

```text
same evidence + same policy replicas
→ coordination without information gain

independent observation / tool effect / heterogeneous model / authority split
→ explicit message and evidence contract
→ aggregation with provenance
```

集中化可以减少 coordination tax，却也会形成容量、信任和可用性单点；多 Agent 则用通信、合并和一致性成本换
新增信息或责任隔离。若这些增量无法在 equal-budget baseline 中被测量，单 Agent + Workflow 仍应优先。该理论
边界不否定拥有独立 sensors、tools、人审或不同模型的系统，只禁止在同信息、同假设下把同源复述当作信息增益；
它也没有证明真实的固定预算单 Agent 能复现分布式并行所提供的算力、延迟或故障隔离。数值例子不能外推为任意
开放环境中的绝对优劣。<!-- source-family:SF-2026-ARXIV-2603-26993 -->

即使通信引入了真实的独立观察，传了多少信息或通信算子的谱也不足以预测收益：同样的传播强度可能把信号送到决策所读的坐标，也可能把共同噪声放大到该坐标。设计评价应锁定任务读出、通信轮数和参与者切片，分别测 individual、community 与整体聚合结果；群体平均改善不能抵消受影响子群的退化。限制跨社区通信可以减少受测伤害，却也会牺牲信息交换，且校准阈值只是已测条件下的选择规则，不是安全保证。小规模受控通信模型支持这个边界，不证明开放式语言 Agent 的通信拓扑可以仅凭线性响应预测。<!-- semantic-body-binding:SF-2026-ARXIV-2609-23310 -->

## 扩展 Agent 数量之前，先测量 Coordination Tax

Multi-Agent 的技术演进并不是从单 Agent 线性增加副本，而是：

```text
single reasoning locus
→ independent parallel exploration
→ centralized verification
→ decentralized communication
→ task-dependent hybrid topology
```

每一步解决不同边界。Independent 让可分解搜索并行，却缺少跨结果纠错；centralized
verification 截断部分错误传播，但形成 bottleneck；peer communication 提供更多局部信息，
也会分裂全局 Context 并拉长 critical path。旧方案没有被后者否定：顺序约束强、工具密集或
单 Agent baseline 已较高时，统一 Context 往往比协调更重要。

一项覆盖六类交互 benchmark、五种 topology 和三个模型家族的 2026 研究，在固定工具、
prompt 与总 reasoning-token budget 下观察到强烈的 domain dependence：某些可分解任务受益，
顺序规划则显著退化；更密集通信在一定点后主要增加冗余。它支持本章的设计假设，但阈值、
回归系数和具体幅度只属于该实验配置，不能当作通用 scaling law。

比较主体协作之前，还应冻结外围 input hints 与 output rewriter，再分别测主体 agent 和完整 pipeline。最后一次答案加工可能提高 benchmark 分数，却不说明主体 reasoning 因协作改善；[MiroFlow 的同框架对照](https://arxiv.org/html/2602.22808v1)在 GAIA 的 single74.8高于multi71.9，BC/HLE则相反，output-only73.94也高于joint71.9。这给出了分账需求，不识别“顺序任务必退步”的普遍原因。各 node 独立 turn 上限并非相同 global budget，avg@3、默认 toolset 与文本 judge 权限也必须一起保留。<!-- source-family:SF-2026-ARXIV-2602-22808 -->

Input/output processor、handoff、重试与 merge 都支付调用和 critical-path 费用；必要材料未披露完整 API/token/time、精度或端到端 SLO，不能将局部分数提升称净收益。更重模型组合也未一致改善，typed error 与 retry 不保证故障不会级联。外围加工不稳或协调费用超过收益时，应回到冻结 processor 的单 Agent、deterministic verifier 和较小 workflow，而不是把更多节点作为默认升级。

因此架构选择应先测：

```text
decomposability
independence of evidence
tool / environment coupling
single-agent baseline headroom
communication turns and bytes
error absorption / amplification
success per token and critical path
```

关系属于 `Direct Evolution`：把“多 Agent 可能有用”的定性判断推进为可测量的
task-topology matching，同时保留单 Agent、deterministic verifier 和 workflow 作为长期
有效的较小系统。

任务不能拆成互不依赖的子任务，也不意味着多个探索者只能独立跑到终点。若中间改进能由可访问的verifier辨认、状态可转移且接收者仍保留不同搜索方向，可以让不同agent在连续阶段提供突破，再从共同的已核checkpoint继续；这不同于事后从k条完整轨迹选最好一条。把“每个agent完成各阶段后取最小总时长”换成“各阶段分别取最早突破再相加”，只在阶段难度、无损转移和独立续搜假设下才有比较意义，不构成语言Agent的普遍加速定律。

终态有grader不保证中途反馈忠实：局部测试可能确认一个要求，却漏掉整个任务的其他约束；共享一份终态还会失去独立候选的oracle选择机会。受限通信研究里team优于单次，却未超过Terminal-Bench独立best@2，不能仅凭少量trial唯一归因feedback或herding。重复验证、共享artifact锁、模型tokens和容器资源都有成本，prompt要求复核不等harness强制gate；必须保留完整任务验收及资源分账。进展不可辨认、转移改变任务状态或共享使搜索同质化时，独立best-of-k、顺序单agent和显式人工/确定性检查仍是合理分支。 [必要机制与反证](https://arxiv.org/html/2609.21032v1)。<!-- source-family:SF-2026-ARXIV-2609-21032 -->

### Agent 数量应由边际信息价值分配，而不是固定扩容

固定 N 个 agent 易实现；任务异质后，同等预算会让简单分支过度计算、困难分支不足。orchestrator 可根据不确定性、依赖和验证价值逐步分配剩余预算，并保留停止条件。收益是提高单位 token 的有效探索，代价是估计器成本与早停偏差；估计不可信时回退 equal-budget baseline。<!-- source-family:SF-2026-ARXIV-2605-20485 --> exact-v1 §3–5 支持其预算机制，§6 不证明通用任务最优。

## 什么时候分解有意义

常见有效条件：

- 子任务可并行且输出 contract 清晰；
- 需要不同 tools、models、data scopes 或 expertise；
- verifier 与 generator 有相对独立 evidence；
- 需要职责分离或不同 authorization；
- environment 天然包含多个 actors；
- 搜索空间可由多种策略探索。

如果所有 agent 读取同一错误文档、使用同一模型并互相复述，讨论轮数不会创造新证据。

Verifier 的配置还应联合校准两条轴：在单次 agent 调用后还是完整 iteration 后复核，以及 judge 读取当前 step、完整 history 还是摘要。前者改变可介入的控制机会，后者改变证据可见性与 token 成本；摘要可能丢掉跨步依赖，完整 history 也可能混入干扰，不存在普适粒度或越长越好的视图。配置、judge、候选池与搜索预算应共同冻结，再比较实际控制收益及总成本。[有限多 Agent 对照](https://arxiv.org/html/2602.03053v1)的 BestConfiguration 经配置选择且成本不同，不是部署默认的统一最优；某些设置的零成功只描述这些样本与协议，不证明任务 fundamental impossible 或理论能力天花板。judge 域失配、摘要遗漏或复核成本失控时，应保留更简单的固定配置与独立环境验证。<!-- source-family:SF-2026-ARXIV-2602-03053 -->

## 典型拓扑

**Supervisor/Worker**

```text
Supervisor
├─ Worker A
├─ Worker B
└─ Verifier
```

控制简单，但 supervisor 成为 bottleneck 和 single point of interpretation。

固定 routing 与有限 success/failure 状态在任务可枚举时易核验；worker 返回 `success` 却只满足部分要求时，粗状态不足以说明全局义务已经完成。一个协调分支让 orchestrator 根据消息 history 核对仍缺少的语义要求，选择继续询问、收紧原 instruction、替换 worker 或真正 replan，而不是每遇异常就重跑已完成分支。[CORAL 的受限案例](https://arxiv.org/html/2601.09883v1)包括缺失字段、日期边界与代理单位的错误成功标记；这些语义判断仍是 proposal，控制状态、真实 effect 与最终验收继续由 runtime 和独立 verifier 持有。<!-- source-family:SF-2026-ARXIV-2601-09883 -->

这种协调增加消息、全局视图和解释错误成本，不证明生成式调度普遍优于 workflow。作者 GAIA165 验证题中，全强模型配置与 OWL 准确率相同且 token 略多，弱 worker 的异构配置才出现更明显收益；coordinator 角色、提示与协调方式并不完全匹配，case logs 也不是唯一因果消融。保留显式预算、typed handoff 与独立 obligation 检查；任务结构稳定、语义复核不可靠或协调费用失控时，固定流程和确定性验收仍是合理分支。

小组短任务把所有 worker 历史交给 supervisor，最容易保留跨任务依赖；并发任务和 steering 历史变长后，同一个工作视图也会混入与当前问题无关的状态。一条分支不改变团队拓扑，而改变每次协调调用读什么：空闲时只读取有界 status registry；某个 worker 请求协助时，加载其任务、steering 历史与局部产出视图，其他 worker 只留下紧凑状态。普通请求排队，高优先级请求可以先保存当前 steering 状态、切换 focus，结束后回到 registry 并恢复仍未完成的会话。视图组装与切换由 orchestrator runtime 拥有，不等于给 worker 增加权限或让 prompt 构成安全隔离。<!-- source-family:SF-2026-ARXIV-2604-07911 -->

这种选择减少无关上下文竞争，却增加 snapshot 陈旧性、视图重建、跨 worker 证据遗漏和抢占饥饿风险；共享依赖仍需 typed evidence，不能因只看到状态摘要就假定子任务独立。作者的受限研究包含 scripted 场景和 N=3/5、低决策密度的真实 Agent 实验，registry 中他人 ID 被提及也不等于发生有害污染，interrupt 的收益未被独立消融。因而它只是工作视图控制的条件分支，不证明绝对无污染、权限隔离或任意规模质量提升；强耦合任务、当前 worker 状态本身超预算或可恢复证据不足时，完整共享视图、显式交接与不抢占协调仍合理。<!-- source-family:SF-2026-ARXIV-2604-07911 -->

Supervisor 的权力还要按时间范围分层。对当前 run 的 `redirect / abort / retry` 是执行控制；把一条成功轨迹、
prompt、tool recipe 或 harness 交给未来 run 使用，则是能力状态变更。前者可以在预算内快速生效，后者必须经过
独立 verification、lineage 与 admission：

```text
live trace → supervisor redirect / abort → current-run outcome
verified trajectory + provenance → bounded trial → harness promotion → future runs
```

若两者混在一起，一次偶然成功或被污染的 worker output 会跨 run 固化。分层获得在线纠错与经验复用，却新增
promotion queue、artifact version、rollback 和陈旧性；没有可靠 verifier、任务一次性或环境快速变化时，只保留
run-local correction 更安全。跨 run adoption 的平台责任交给第 84 章，当前章只拥有角色和交互拓扑。

**Peer/Debate**

多个 agent 提出或批评候选，再由规则或 judge 选择。适合探索，不保证 majority 正确；同源模型可能形成 correlated consensus。

同题独立采样可以增加候选覆盖，却不必带来独立正确的证据。若每个问题有自己的答案分布，plurality随样本增多趋向该问题的modal答案；只有正确答案是唯一mode时，这条极限才有益。“至少一条正确”的oracle覆盖依赖另一个可靠选择器，不能作为投票已实现的收益。即使given-item样本独立，跨题正确率仍可因题目难度差异相关；不要把这个相关都解释为Agent互相影响，或仅通过温度增加文字变化便宣布偏差被消除。

对连续数值估计，平均可缩小同题采样波动，却留下该题共同bias；全数据平均误差接近零也不证明每题无偏。[受限多Agent scaling证据](https://arxiv.org/html/2609.31563v1)支持分别验收候选覆盖、aggregation选择及item-level偏差，而不把任务taxonomy当普遍人数法则。Answer-first格式、revision推理机会和peer数同时影响结果，扩大团队/异构pool亦有退步；reference噪声、pool后验选择、prompt与总调用成本须分账。若错误mode稳定、选择器不可靠或收益不抵费用，保留single-agent深推理、少量revision和独立可执行verifier，不以共识或平均认证真值。<!-- source-family:SF-2026-ARXIV-2609-31563 -->

反馈协作还要区分 peer 能看到初稿、能交换哪些反馈，以及能否看到别人的修订成品。同题初稿与反馈可见、修订稿不再共享是一条受限分支：它仍允许借鉴与批评，却减少后续轮直接追随同一修订答案的机会。这不是完全盲评，初稿与反馈也可能已传播共同偏差；修订 artifact 的可见性是独立于人数和 judge 选择的控制变量，不能由“多 Agent”标签推断证据独立。<!-- source-family:SF-2026-ARXIV-2601-08003 -->

[受限创意写作对照](https://arxiv.org/html/2601.08003v1)中，增加人数或轮数也会退步；有限科幻题目、少量学生人工核验与模型 judge 不证明任意任务质量或语义新颖性。虽然多 Agent 设置使用相同轮数，单 Agent 的总调用预算并未匹配，反馈、修订与裁决仍付费；文本分布或图式差异亦不是正确性证书。若同质化、judge 偏差或费用无法控制，保留少量独立候选、single-agent revision 与外部 verifier，不把受限反馈隔离升级为普遍优于单 Agent。

**Blackboard/Shared State**

Agent 通过 typed artifacts 和 shared workflow state 协作，而不是无限聊天。可追踪性更强，但需要 concurrency、ownership 和 conflict rules。

**Pipeline**

固定角色顺序，实际更接近 Workflow；不应仅因每步使用模型就称为自主 multi-agent system。

### 执行前的 Resource Algebra 是拓扑准入证书，不是运行时估算的替代

任务图已知且各节点成本可界定时，先启动所有 worker 再观察预算是否耗尽，会把错误拓扑变成不可逆的已花费用。
更稳妥的控制面先把任务复杂度向量映射为带依赖的 DAG，为候选拓扑计算 token、tool call、并发槽位和 critical-path
上界，只有守恒条件成立才允许实例化。Orchestrator 拥有拓扑 proposal，budget owner 签发准入证书，worker 只消费
已分配额度；这样把“能否运行”从生成式判断降为可检查的资源约束。

静态代数依赖 deterministic cost、有限 action space 与可界定 graph depth；工具延迟、重试和模型采样带来随机成本时，
证书只能给出期望或高概率界，仍需 runtime accounting、限额与中止路径。小任务、固定 pipeline 或成本估计不可靠时，
直接使用单 Agent 加硬预算更稳；不能为了得到形式化证书而伪造精确成本。当前证据只支持受限资源模型中的可行性检查，
不证明真实多 Agent workload 的 wall-clock 或质量最优。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05657 -->

拓扑选择还可以细化到边上的协作协议，而不只是选择有哪些节点和连线。固定 chain 或 debate 易复现；当任务需要在不同交接处采用不同反馈方式时，一条受限学习分支分别提出节点所用的模型、边是否存在、边上的 chain/debate/criticism 协议，以及允许这些边的通信 backbone。节点内的 CoT 或 reflection 又是另一层局部策略，不能把它与跨节点通信混成一个“拓扑”标签。[策略条件化路由的局部对照](https://arxiv.org/html/2601.09434v1)支持把这些身份显式分开，以便冻结模型、协议、提示和结构后比较；学习器输出仍是配置 proposal，不获得运行状态或最终结果的验收权。<!-- source-family:SF-2026-ARXIV-2601-09434 -->

Backbone 为 DAG 只限制节点间的依赖，并不证明节点内或双向协议中的 `while` 循环终止；实际 round、调用预算、timeout 和停止路径仍由 runtime 持有，不能补称论文已经实现这些上界。局部随机化组件对照也不是所有配置的等预算因果分解：训练、模型选择、提示 token、完成 token、通信和裁决均有成本，较少完成 token 不等于整个生命周期更便宜。协议搜索、模型变化或内部反馈使成本与输出难以校准时，保留固定 chain/debate、小型 worker pool 或单 Agent 加外部 verifier，而不是把学得的结构视作质量或预算证书。

## Topology 从部署前选择演进到运行时有界修复

运行时 adaptation 不只包括修图，也包括受预算约束的 fan-out。Orchestrator 可以依据任务分解、预计并行 critical path 与当前 worker outcome，选择是否实例化子 Agent、分配多少分支及何时合并；但控制对象必须是 typed dependency graph 和 budget，不是“让模型自由召唤更多模型”。

学习 fan-out 或只更新 orchestrator、冻结 executors，可以降低训练与 credit assignment 复杂度，却会让 executor 能力变化、共享工具状态和合并错误变成 distribution shift。静态 worker count 在预算可预测、任务强耦合或 side effect 多时继续成立；动态 topology 只有在分解收益可观测、子任务权限隔离且合并有 verifier 时才值得采用。

运行时创建还要分开三种生命周期：可复用的 agent metadata/object pool、每次调用的临时 execution clone，以及能够恢复的 execution-memory archive。一个分支先按模型、指令、工具与初始记忆注册配置，调用时克隆对象执行，结束后删除 clone，历史仍由独立记忆组件持有；删除执行对象不等于清空证据，也不等于 durable workflow checkpoint 或已回滚外部 effect。并行调用的共享 message board 可用写锁及每个 Agent 的读取 cursor 只投递新差量，但这只控制消息读写，不认证内容真实、工具权限或副作用隔离。[原始有限机制与对照](https://arxiv.org/html/2602.16891v1)中的拓扑/摘要联合消融不识别单独动态 create 的收益，容器与图记忆也不授全面安全；生命周期拆分增加 clone、状态索引、恢复与消息同步费用，配置不可追溯、恢复证据不足或调用预算不稳时，保留固定小型 worker pool、显式 typed handoff 与第81章的执行控制。<!-- source-family:SF-2026-ARXIV-2602-16891 -->

有界fan-out还要区分已启动、provider已ready、仍在运行与结果已验收的数量。只按启动数放大批次，可能在首次限流前堆出大量尚未ready的工作；一种限定实现正常期先启动5项，再每700ms加入一项，首次provider限流后停止ramp，以ready数量初始化并收缩容量，随后在容量与等待时刻允许时逐项启动。Kimi Code 0.12的rate-limit phase优先重试同一agent，再处理resume或新任务，用3/6/12秒递增等待与约3分钟无新限流后的探测增容，换取较少重复初始化；正常ramp本身不以active数量硬封顶，这套规则不是最优配额、生产SLO或预算安全证明。<!-- source-family:SF-KIMI-CODE-0-12 -->

批次Join也不应把取消改写为“所有工作都未发生”：结果槽保留原输入顺序与已完成输出，将已开始但未完的任务和从未启动的任务分别标为aborted/started与aborted/not_started，已知agent身份可用于后续resume；单任务timeout只终止该任务，剩余唯一任务持续限流则可终态失败而非无限重试。Swarm mode中的自动审批仅针对AgentSwarm工具，不等于子任务工具权限豁免。它增加队列、退避与部分结果状态，但不证明队列持久性、crash重放、effect回滚或模型返回即正确；高风险任务仍需原有能力边界、预算验收与独立verifier，配额不可观测时保留静态小批次或串行fallback。<!-- source-family:SF-KIMI-CODE-0-12 -->

Task-topology matching 最初通常发生在运行前：根据 decomposability、evidence independence
与 tool coupling，在 singleton、star、tree、chain 或 debate 中选一个结构。这个方案仍然
合理，因为 topology 稳定、容易复现，且不会让控制面在执行中不断改写责任关系。

静态结构也可复用搜索资产，而不必对每个目标任务从头搜索。把来源任务的搜索轨迹凝成带版本的operator-level结构启发H与node间输出contract C，可以在新任务上提出待编译的topology；来源搜索只产生proposal，H来自优/劣轨迹，C可来自中间得分却最终解析失败的轨迹；目标任务仍须做结构检查、真实执行与结果验收。task族、模型、提示、contract与来源搜索预算都应随资产保存。

复用降低目标任务的边际搜索成本，却增加跨任务迁移失配和隐藏的前期成本；摊销必须另报来源搜索及可复用任务数，不能把低边际调用费叫作总成本。受限数学/代码测试存在迁移反退，没有验证不可逆effect的开放Agent；分布变化、结构不兼容或缺verifier时，保留人工结构、单Agent或逐任务有界搜索。 [原文必要机制与限制](https://arxiv.org/html/2604.25012v1)。
<!-- source-family:SF-2026-ARXIV-2604-25012 -->

当 long-horizon task 的风险只有在 trace 中暴露时，静态选择会遇到边界：某一 branch
过载、缺少 verifier、并行 action 产生重复副作用，或 agents 在 unresolved issues 尚存时
过早达成共识。此时演进方向不是无限增加 Agent，而是把 topology 作为 versioned runtime
state，允许由可观测 process evidence 触发一次受预算约束的结构修复：

```text
task-conditioned initial topology
→ execute and emit typed relay / evidence / tool trace
→ audit process risk, not hidden benchmark answer
→ propose bounded mutation
→ deterministic structural validation
→ continue from a new topology version
```

修复可以扩展局部分支，也可以只改变通信 edge、插入 critic，或把重复的 state-changing
actions 从 parallel 改为 serialized。后者说明“适应 topology”不是追求更密的 graph，
而是让 communication、visibility、execution order 与 validation path 对应当前 failure。

MANTA 为这条路线提供了单篇预印本证据，但不能证明动态 topology 普遍优于静态 Workflow。
它的实验把 mutation 次数和 agent budget 设为上限，并由 LLM auditor 读取 process trace；
clean trace 仍不保证答案正确，auditor 也可能漏掉 agents 共享的语义错误。生产实现还会新增
topology version、worker context migration、authority transfer、mutation race、replay 与
rollback 成本。因此旧方案继续成立：短任务、强顺序约束、高副作用或 verifier 明确时，
固定 chain / singleton + deterministic checks 往往更安全。动态修复只应由第 81 章的
Workflow controller 提交，Agent 自述不能直接改写 authoritative topology。

动态 topology 之内还有一个更细的控制对象：**这次把子任务交给哪个 peer**。固定 peer 或 greedy 选择在任务短、
能力近似、探索成本高时最容易复算；当 peer 能力随任务类型变化且观测稀疏时，可以把 capability estimate、
uncertainty、task context 与历史 outcome 写成版本化 evidence ledger，再在预算内做 bounded exploration：

```text
task context + peer capability posterior
→ explore or exploit under a declared budget
→ selected peer executes
→ independent outcome evidence updates the ledger
```

Peer selector 只拥有委派决策，不拥有最终求解或 verifier。探索会把一部分请求交给不确定 peer，获得长期信息的
同时增加当下失败、延迟和不公平负载；短任务、不可逆动作或强 SLO 下应缩小探索甚至退回静态路由。该机制也不
证明局部选择能得到联合最优 topology，更不能据少量 peer 实验外推到超大规模多 Agent。

稳定模型池也可以先采用离线路径：用可核验 validation 按任务族分别测 worker 的求解能力与 coordinator 的聚合能力，再把角色相关 profile 交给有界选择器；单模型解题强，不自动意味着它善于消费其他模型结果。[受限角色对照](https://arxiv.org/html/2602.16485v1#S4.SS1)在数学与代码上选出不同 coordinator，其 GT 辅助自评是离线依据，不是线上自报 confidence 或事实、权限保证。固定美元预算换成 provider-specific token cap 也不等于同 token；profile 构造、模型调用、并行等待与合并都计费，异构模型名称不证明错误独立。该研究未充分交代独立 held-out 校准和不确定性，因而只能支持这一角色分账选择，不能授普遍 Pareto 最优。任务短、模型/价格漂移或 profile 不可靠时，单 Agent、固定小池与独立 verifier 仍成立。<!-- source-family:SF-2026-ARXIV-2602-16485 -->

动态协作还可以不等待故障才改拓扑，而按每轮当前信息需求重建有界通信图。各Agent先给行动proposal、信息needs与可选addressee，router用需求与peer观测/记忆的匹配、计划相似及信息互补来分配边；direct address优先但不绕过receiver容量。确定图选择不需要额外LLM planner，却仍消费全局候选metadata、embedding与pair比较；coverage补边若允许超sender预算，成本证书必须保留这个例外。

图只控制这次谁看见哪份proposal，peer reply只是行动选择证据：非空接收集合全部Accept可以省一次本地生成，但missing/reject/counter应回本地决策，不因语义相似或共识取得真实effect授权。Proxifield的受限sim结果显示needs表达与基模型能力、团队规模和permanentdropout会改变选择收益；比较调用预算不等、全局router故障未测，也不证明Byzantine或真实网络可靠性。关键证据丢失、不可逆动作或SLO不允许多轮时，保留固定workflow、可读handoff与独立verifier。 [必要机制与反证](https://arxiv.org/html/2609.20889v1)。<!-- source-family:SF-2026-ARXIV-2609-20889 -->

### 通信预算先区分消息长度与重建成本

传完整解释最容易审计，但接收者若已经拥有很强的先验，短反馈也可能足以让它修正答案。一个受限交互分支让较小模型提出二元问题，较强模型只回 yes/no，再由小模型重建解答；在同一模型、prompt 与确定性生成可重放的前提下，只计算回答方向的 payload 可以得到很小的 bit 数。它不是无损搬运强模型的知识：问题、模型先验和本地重建计算已经提供大量条件信息，双向网络、模型调用与同步成本还要另算。

验收要与等计算的自问自答比较，分离协议结构收益和外部信息收益，并检查答者是否看到了实际部署不可得的参考答案。受限 Claude-family 实验用了这类 privileged reference，部分恢复主要来自自我修订；错误二元反馈和不可确定重放会削弱收益。因而通信 owner 只优化明确的 channel contract，不取得 correctness authority；知识缺口大、开放任务不可判真或审计优先时，完整文本、typed evidence 与独立 verifier 仍更合理。[二元反馈协议、共享先验与评测限制](https://arxiv.org/html/2604.02343v1#S5)

### 接收方可以决定何时停止发送，但要验收后续对话

缩短发送方消息，在接收者需要的信息相近时最容易实施；如果接收者的先验、任务状态不同，同一段完整解释可能对一方必要、对另一方冗余。另一条分支不是继续压缩 payload，而是让接收者在每个固定大小的 chunk 到达后，根据当前消息前缀和对话历史提出 interrupt；运行时收到信号后停止本轮发送，再让接收者应答。接收方拥有是否需要更多信息的 proposal，通信 runtime 拥有实际 halt 与轮次切换，Workflow 仍持有任务状态和副作用授权，不能把停止发送当成任务已完成。

这个选择要按完整后续对话验收，而不是只计算被截去的 token：过早打断可能增加澄清轮次或降低终态质量，省下当前输出也可能使总成本反增。一个受限学习方案从同一前缀分别 rollout“在此打断”与“不打断”的后续对话，用质量不降且总生成 token 减少的条件训练 interrupt decision；它用昂贵的离线分支采样换更便宜的在线判断，但标签依赖所采策略与任务 reward，每个 chunk 的判断也有成本。chunk 越小越灵活，却增加调用、同步和预测开销；token 减少只是作者实验的时延代理，不证明真实网络、批处理与并发条件下的净时延收益。

所测三类任务中的有限模型、三次运行支持这个接收方控制分支，也包含提示词直接打断因过早决策而恶化的反例；主实验只允许一个接收者打断其他发送者，不构成任意并发抢占或开放协作的安全协议。信息不可恢复、发送者执行的是不可逆动作、没有独立终态评价或打断协调成本更高时，保留完整消息、发送方压缩与显式轮次控制仍合理。[接收方打断、完整对话收益与成本边界](https://arxiv.org/html/2604.06452v1#S2)<!-- source-family:SF-2026-ARXIV-2604-06452 -->

并行推理也不一定要发送完整轨迹。若接收者的工作是综合多份独立尝试，发送方可以只保留 conclusion，丢弃中间 reasoning，再由专门训练的 synthesis policy 消费问题和这些短消息；这以丢失推理证据换取可容纳的尝试数量。问题与全部消息仍必须装进接收者窗口，不能把 conclusion compaction 写成恒定成本或无限并行。发送方的结论不是事实授权，综合后的答案仍由任务 evaluator 验收；需要审计因果链或诊断错误时，保留完整轨迹与 typed evidence 更合理。<!-- source-family:SF-2026-ARXIV-2601-05593 -->

综合能力也不能只靠增加票数。一个受限方案用在线/缓存消息训练 synthesis，并筛除平均消息正确率过高、靠多数答案即可解决的训练样本，使接收者学习从不可靠结论中恢复答案；这些筛选和 outcome-based 更新是额外训练成本，不证明中间 reasoning faithful，也不消除共享模型的相关错误。[结论压缩、训练筛选与受限结果](https://arxiv.org/html/2601.05593v1#S2)中的大规模 test-time compute、缓存与总生成 token 不能直接折算为端到端 wall-clock 优势。消息质量过低、全错消息缺少可恢复信息、窗口拥塞或训练分布迁移时，应回退较少完整尝试、独立验证或 abstain，而不是把 synthesis 的一次成功当成任意多数错误可纠正的保证。

### 通信可以压缩成 latent，但 contract 不能一起消失

文本消息可读、可版本化，也容易绑定 evidence；缺点是序列化损失和 token 成本。异构 Agent 若直接交换 latent states，可能保留视觉细节并绕过重复编码，但发送方与接收方模型不同，buffer 本身没有稳定语义。因而 latent channel 至少需要：

```text
sender / receiver model identity
+ codec and schema version
+ modality span and buffer lifecycle
+ fidelity probe and compatibility check
+ text or artifact fallback
+ audit projection and replay identity
```

adapter 数量线性增长不等于 runtime cost 也线性，更不证明 accuracy parity。不可读 embedding 只能作为 proposal channel，不能替代 authoritative task state、approval 或完成证据。Vision Wormhole 提供了异构 VLM 之间传递 image-span latent 的实验机制，但版本、模型组合和 artifact 边界要求它保持 Experimental；文本/typed artifact 在审计、故障恢复和跨版本兼容更重要时继续成立。

图像 span 并不是 latent communication 的唯一对象。语言 Agent 也可以把发送方末层的一段 hidden states 当作
候选消息，再映射到接收方 input-embedding 坐标。直接拷贝 state 或 KV 的问题是坐标系、层数和 norm 都属于
checkpoint；“维度相同”不代表语义兼容。一个 training-free 的受限分支用已生成消息 token 的 receiver
embeddings 作为临时锚点，求几何保持的正交映射，再做 norm calibration 与 vocabulary-neighborhood anchoring：

```text
sender final hidden-state suffix
→ receiver-token anchors for closed-form alignment
→ norm calibration + bounded vocabulary anchoring
→ continuous prefix for receiver
→ downstream task verdict + text fallback
```

这减少了为每个 sender/receiver pair 训练 adapter 的要求，也可能保留序列化前的连续信息；但它没有得到稳定的
跨版本协议。Sender message、receiver tokenizer/embedding、selected suffix、alignment rule、anchor coefficient 与
model revisions 必须共同构成 channel identity。连续 prefix 不可读、难以审计，恶意或漂移 state 还可能绕过文本
policy scan，因此只能作为 proposal / reasoning channel；authoritative facts、delegation、approval、commit 与完成
证据仍应落到 typed artifact 或 Workflow state。StateBridge 的四模型、两 family、顺序四 Agent 实验仅支持该
对齐机制在所列 QA/math/code contract 下可行；没有证明跨任意 architecture、长 workflow、安全 adversary 或模型
升级后仍兼容。文本消息在可解释、重放和治理优先时继续成立，训练 adapter 在固定高流量 model pair 上也仍可能
比每次闭式对齐更稳定。

固定高流量 model pair 还暴露了 sender-only translation 的另一条边界：发送方 state 即使被压缩得很好，也不知道
接收方已经编码了什么、哪一层或哪个位置真正缺信息。于是 latent handoff 可以从“翻译发送方 cache”演进为
“联合读取两侧 cache，再按 receiver position 产生有界 residual”：

```text
sender cache + receiver cache
→ pool and align heterogeneous layer/KV geometry
→ build receiver-aligned cross-layer joint memory
→ each receiver position queries the joint memory
→ gated residual update in receiver-native KV geometry
→ ordinary decoding with typed/text fallback
```

这个变化把 message 从 sender-authored summary 变成 receiver-conditioned proposal。Layer map、joint-memory width、
position query、per-head gate 与 translator checkpoint 都成为 channel identity；zero-initialized residual 可以让未训练
translator 退化为 receiver-only decoding，但不能把训练后的不可读 cache 当作无风险写入。Runtime 还要冻结两侧
model/tokenizer/KV layout、输入 cache provenance 与更新时点；只修改 prefill cache 一次，不应追溯改写后续生成 token
的 cache，也不能越过 Workflow 对事实、授权和 commit 的 owner。

XKV 的作者实验只覆盖三个小模型 family、九个有序 pair、五个 QA datasets、greedy decoding 与单一训练 seed；
它支持“joint state + receiver-position retrieval”在该 contract 下优于 sender-only latent summary，不证明长程协作、
安全对抗、在线模型升级或生产并发中的协议稳定性。固定 pair、重复流量且 token cost 主导时，trained cache translator
可能值得维护；pair 经常变化、审计或恢复优先时，文本/typed artifact 仍是默认路径；无法训练 adapter 时，前述
training-free alignment 仍是另一条受限分支。

发送方的 prompt cache 先压缩再传递时，另一个问题是被淘汰 V 的贡献是否还可由保留 V 表达；这不同于前述接收方条件化翻译。一条 sender-local 分支先去除被删 V 在保留 V 张成空间内的分量，对残差做低秩主子空间与 attention-demand 汇总，再把同一补偿量加到各保留 prompt V，K 保持不变。它试图减少硬淘汰的损失，但正交分解与统一补偿不证明原 attention 输出、信息无损或事实正确。<!-- source-family:SF-2026-ARXIV-2604-13349 -->

[受限 relay 对照](https://arxiv.org/html/2604.13349v1)限 Qwen3-14B、40 latent steps、BF16、单 RTX PRO 6000 Blackwell，rank-8 残差摘要仍有任务/压缩分支退步。实现必须在删除前保有原矩阵并支付 QR/SVD 与统计成本，不能把小传输 payload 当成免费压缩；压缩规则、模型和 cache revision 都须绑定。接收方失配依然归 translator owner，审计或质量失败时回退完整 KV 或 typed/text message；两条路线可组合，但不能互相冒充已完成的兼容性与真实性验证。

协作也不一定先让专家生成消息。一条生成前融合分支让冻结专家分别用自己的 tokenizer 对同一 prompt 做 forward，投影其最后层 pooled hidden states，再由 learned Perceiver latent queries 读取并形成接收 policy 的 soft prefix；训练只更新融合器与 policy adapter，不更新专家。它不同于传递已生成 suffix 的对齐或 joint-KV translator：传输对象是 pre-generation 表示，接收 policy 用 RL 学习如何消费固定数量的 prefix queries。专家、tokenizer、投影器、融合器与 policy revision 共同定义接口，prefix 仍不能代替事实证据或授权。

[受限原始证据](https://arxiv.org/pdf/2602.09173v1)中，专家不 decode 仍须执行全部专家 forward；和只执行 top-1 的 hard router 同生成长度，不等总计算预算。Arithmetic 获益同时伴随 Logic/GSM 退步，attention/reward 随训练变化也有容量偏好混杂；first-token 表示与 last-token 结果近似，不能宣称已证明真实动态任务分工或收益必须来自 prompt-specific reasoning。该分支用于固定专家集合与可训练消费者，增加融合训练、全部前向及不可读接口的审计成本；专家频繁升级、无需多专家或证据恢复优先时，单 policy、选择性调用与 typed/text message 仍合理。<!-- source-family:SF-2026-ARXIV-2602-09173 -->

### Behavioral belief 不等于 authenticated identity

Agent 可从 interaction history 推断 co-player 的响应策略，并据此调整当前 action；这能在重复博弈中形成快速适应，也会产生 strategic shaping、collusion、belief poisoning 和 equilibrium drift。Runtime identity 回答“对方是谁、拥有什么权限”，behavioral belief 只回答“根据有限历史，对方可能怎样行动”，二者必须分开存储和校准。外部 policy 仍定义什么合作可接受，模型不能用预测到的互惠收益自行放宽授权。受控 repeated-game 实验证明 partner diversity 可诱发有限的 in-context adaptation，不证明现实 Agent 会自然合作或隐藏身份更安全。

若风险来自协作者策略轻微偏移，训练时还可引入一个受 KL 约束的辅助 partner adversary：它以降低本 Agent 的回报为目标，但被惩罚偏离正在演化的普通 partner；本 Agent 再针对这一局部邻域更新 PPO。它是训练人口的风险暴露控制，不会认证对方身份，更不会扩大运行期权限；reference 随训练变化，KL 系数也不是任意部署分布的安全证书。附加 adversary、角色采样、rollout 和更新成本需结算，缺乏聚合结构的任务甚至会降低训练表现。合作数学题的双人共同正确与异质未训练 partner 下单 Agent 正确不是同一评价人口；保留普通 self-play/IPPO 与真实部署 partner 检查，不能用受限邻域训练代替开放协作的信任规则。<!-- source-family:SF-2026-ARXIV-2602-21515 -->

在线适应之外，还可以先让模型生成固定策略、检查其可执行性，再在冻结策略池中模拟不同群体组成与组大小；这以编译、筛选和模拟费用换取更大的可检查人口，但可执行不等策略正确，编译失败的选择性剔除也会改变人口。单 Agent 收益或同模型 self-play 不足以说明整体福利，评估还应显式保存用户模仿、策略重采样、mutation 与停止规则，分别报告个体收益和群体结果。[受限 population 证据](https://arxiv.org/html/2602.16662v1#S6)显示选择算子可偏向损害集体结果的策略，也有小组/游戏反例；binary action、固定收益与已知 horizon、无通信及未充分校准的模仿超参限制其解释。它不是在线 belief 更新，更不预测现实迁移成本、用户选择或合作安全；开放协作仍需实际环境验证和外部规则，短小任务可保留既有在线策略与固定小组。<!-- source-family:SF-2026-ARXIV-2602-16662 -->

若策略会在 test time 继续更新，测量人口就不能只是一组固定 action policies：可把初始 interaction history 与固定 adaptation prompt 合成一个 meta-strategy，再冻结候选集、对手抽样、初态和 horizon，估计成对收益及相对该集合的 NE-regret。Uniform-opponent 收益高不等于面对 best response 仍稳定，同策略 self-play 的合作也不等于该人口下没有有利偏离。[受限 meta-game 对照](https://arxiv.org/html/2602.17203v1)在六种 GPT5-mini 配置、四离散价格、40 base-game 初态与 t=50 中得到部分合作均衡代理，但候选策略、API 离散化和信念改变都会改变结论，旧模型停用还使早期结果不能重现。History 中的 plan/insight 更新与固定 prompt 都须保存，模拟、矩阵估计与API调用付费；这不同于固定策略的 mutation/selection，也不预测现实 collusion 或授权合作。人口覆盖或成本不足时，保留冻结小组与实际环境对照，把 behavioral belief 和外部规则继续分权。<!-- source-family:SF-2026-ARXIV-2602-17203 -->

## Message 不是 State

### Coordination State 必须有显式 Owner 与 Commit Transition

靠自然语言消息同步在小组短任务中足够；长工作流会出现重复行动、stale belief 与无主结果。state-oriented runtime 应把任务状态、lease、proposal、commit 与 recovery 交给明确 owner，消息只携带 transition request。收益是可恢复，代价是协议与存储开销；短期无副作用协作仍可保持消息式。<!-- source-family:SF-2026-ARXIV-2605-20563 --> exact-v1 §3–5 与 Appendix E 只支持作者环境，不证明状态机消除了语义误解。

### 间接协作仍要落到 Durable State，而不是共享传闻

参与者不直接通信、只观察共同环境时，stigmergic coordination 可以减少点对点协议；但把任意共享文本或 event log 当作环境事实，会重现 message 的重放、并发覆盖和不一致观察问题。Ledger-state 路径把 proposal 追加到有 schema、顺序与 commit 语义的 durable state，参与者只根据已提交 revision 决策；ledger/schema owner 决定可见性和因果顺序，Agent 只提交 transition proposal。

它获得可追溯的间接协调，代价是一致性延迟、存储/共识成本、schema 演进和错误状态的持久传播。低风险、单 owner 或无需跨域审计的任务继续使用轻量 message 更合适；ledger 不可用、共识成本过高或 schema 无法表达任务语义时，应回退 workflow owner 的集中 commit。公开论文主要提供形式框架，不证明生产吞吐或容错上界。

<!-- source-family:SF-2026-ARXIV-2604-03997 -->

### Latent Communication 只能压缩 Payload，不能隐藏 Identity

文本消息可审计但 token/latency 成本高；共享模型族可传 latent cache 以复用中间表示，但通信 owner 仍须记录发送者、模型 revision、shape、生命周期与 fallback text。收益是减小通信，代价是版本耦合、不可解释和跨模型失配；审计或异构优先时回退显式消息。<!-- source-family:SF-2026-ARXIV-2605-22863 --> exact-v1 §3–4 与 Appendix C 支持其 latent-cache 机制，§5 不证明跨模型互操作或语义等价。

异构 Agent 之间即使都使用 KV，也不能把 sender cache 当作 receiver state。跨模型通信必须经过有版本的 cache transform；identity 至少绑定 sender/receiver model、tokenizer、layer/layout、可见输入和 transform-training revision。Transform 只生成 derived state，receiver 仍拥有最终 reasoning 与 action；context-unaware transfer 需要携带更密的 contextual state，不能假设接收者已看到相同 prompt。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-25422:start -->
当 Agent 通过受限无线链路协作时，token text 与 KV cache 还是两种不同 communication media：前者可审计且跨模型，后者可能减少接收端计算，却依赖共同的 state layout。因而 medium 选择必须与 bandwidth allocation 联合决定，并绑定 sender/receiver model、cache layout、channel state 和端到端 deadline；没有一种 medium 在所有 compute/channel regime 中都占优。

联合优化增加 telemetry、控制和重规划成本，KV 还引入版本耦合与不可解释性。链路或计算状态漂移会让原选择变慢甚至语义不兼容；身份不完整或预测失配时，应回退显式 typed text 与保守带宽，重新建立可验证 handoff。论文数值实验支持这种条件化选择，不证明真实无线环境或任意多 Agent 拓扑的普遍最优性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-25422:end -->

这种对齐减少文本重编码，却增加训练、模型升级耦合、不可解释错误和 cache 形状兼容成本。跨模型校准失败、身份不符或审计要求可读时，应回退文本消息。作者只验证 Qwen3 三种规模的六个方向和有限 benchmark，不证明跨架构、跨 tokenizer 或生产网络下普遍优于文本。
<!-- source-family:SF-2026-ARXIV-2606-13594 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11167:start -->
显式文本 handoff 在异构、审计优先时仍是可解释基线；两个模型若在每个 generation step 通过可训练 interface 双向交换 hidden state，通信 plane 就从异步消息变成 lockstep causal state。Interface 只拥有 payload transform 与 suppression gate，两个 frozen LM 分别拥有自己的生成状态，tool runtime 仍拥有 effect commit；哪一步看到哪段 tool output、何时注入 residual，必须随 causal schedule 一起版本化。

这种 latent coupling 降低文本序列化开销，却可能近似翻倍模型 compute，并新增同步阻塞、不可解释通信、负迁移与 task-specific causal annotation。能力互补不清、因果放置无法证明或审计要求可读时，应回退显式 typed message、异步协作或单模型 tool loop。exact-v1 只支持作者的 calculator/Z3 与有限 GSM8K 分析，不证明跨工具、跨模型或生产 latency 下普遍有益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11167:end -->

### Reward Shaping 必须保持 Conditional Best-response

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23562:start -->
稀疏团队奖励难以提供逐步 credit，dense reward shaping 因而在固定任务和稳定对手下合理；但 learned shaping model 与多智能体 policy 同时更新时，彼此会改变对方看到的环境。只有在固定 opponent policy 条件下保持每个 agent 的 conditional best-response set，才能声称 shaping 没有改变原 equilibrium。Reward learner 只拥有 shaping proposal，policy learner 拥有行为更新，exploration schedule 则必须独立拥有覆盖控制，三者不能由同一个 loss 隐式合并。

该保证依赖固定对手假设，现有实验又只覆盖部分可观测的 multi-agent pathfinding；有限探索与耦合的 policy-reward dynamics 仍可能形成振荡和 reward hacking。检测到循环协调、best-response 漂移或真实 sparse reward 退化时，应增加独立探索、冻结 shaping model，或回退原始 sparse reward。它支持一种受限的 admission contract，不证明动态开放环境中的均衡保持。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23562:end -->

<!-- daily-20260621:agent-multi-agent:start -->
### Pairwise coupling 不能外推 group dynamics

先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。

**Trade-off、failure、共存与回退。** pairwise gamma 不能预测 multi-neighbor 结果且可反向排序；default agents 未自发 backfire，polarization 均为外部诱导，实验舆论任务不等于真实社会。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-22203` — primary `arXiv:2606.22203v1`；exact-v1 URL=`https://arxiv.org/html/2606.22203v1`；Method=`https://arxiv.org/html/2606.22203v1 — §3 The Coupling Gain; §4 Theory`；Evaluation=`https://arxiv.org/html/2606.22203v1 — §5 Experiments and Results`；Non-proof=`https://arxiv.org/html/2606.22203v1 — §6 Limitations; §5.4 context-dependent transfer boundary`。
<!-- daily-20260621:agent-multi-agent:end -->

Agent-to-agent chat 容易混合事实、建议和控制指令。共享状态应区分：

```text
task facts / evidence
proposals
decisions
artifacts
ownership
workflow status
```

Message 作为 event 保留，authoritative state 由 workflow transition 更新。一个 agent 说“B 已完成”不能替代 B 的 signed/verified output。

### 多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要

<!-- semantic-body-binding:SF-2026-ARXIV-2606-02359:start -->
直接拼接一阶邻居消息在团队小、推理链短时最透明；协作扩到多跳后，压平文本会丢失“谁从谁的哪条证据推出了什么”，重复消息又快速耗尽 Context。聚合器可以把跨 hop 的消息表示为有序 evidence DAG：节点保存 claim/evidence，边保存 sender、receiver、hop、dependency 与 revision，再在预算内做 semantic-topological merge。Message transport 拥有 delivery/order，aggregator 只产生 derived view，workflow/verifier 仍决定哪些 claim 能进入最终 commit。

有序合并保留多跳依赖并减少重复 token，却会引入图构建错误、minority evidence 被压缩、consolidation loss 与额外排序成本；更深 receptive field 也不证明消息真实或独立。每次 merge 应记录被省略节点、lineage closure、token budget 与可回读原始消息，冲突或关键依赖丢失时回退 raw-message view、缩短拓扑或交给独立 verifier。作者在无副作用推理 benchmark、有限模型和 topology 上支持该机制，不证明开放网络的 delivery、权限或生产可靠性。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-02359:end -->

### 声明式协议约束 Transition，而不是相信参与者会协调

集中 coordinator 逐条批准消息和动作，在参与者少、流程固定时最容易复算；异步协作扩大后，它会成为串行瓶颈，
而自由消息又无法表达谁有权设置某个属性、哪些动作互斥、哪些组合绝不能发生。协议层可以把 attribute priority、
action conflict 与禁止组合编译为显式的 `sayso / nono / nogo` 一类状态约束，再由 runtime 在提交 transition 前检查
safety 与 liveness。Agent 只提出 emission，protocol owner 持有规则版本，workflow owner 仍持有真实 commit。

声明式协议获得异步性和可检查性，却增加规则冲突、编译覆盖缺口、delivery/identity 假设和版本迁移成本；形式检查
也不能证明消息内容真实，或外部工具副作用已正确执行。规则不可满足、开放网络身份无法核验、Byzantine peer 或工具
副作用超出模型时，应回退串行 coordinator、独立 verifier 或人工仲裁。有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间只支持
协议机制本身，不构成开放生产网络的正确性保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29601 -->

Message edge 还可以有独立的 admission policy。全量转发最透明，却会传播错误与增加 Context；简单 dropout
降低流量但不知道删掉的是噪声还是关键证据。带失败历史的 gate 可以在 receiver 前先 rectify 可修正消息，
再接受或拒绝：

```text
sender proposal + source evidence + edge history
→ rectify proposal without changing authority
→ accept / reject with reason
→ receiver acts under its own policy
→ outcome updates bounded edge memory
```

Gate 只管理 communication，不拥有 shared state 或 action authority。它会新增 false reject、correlated judge、
global reset、stale edge memory 与额外 calls；typed direct handoff 在协议稳定、消息少或错误代价高时仍更可靠。
AgentDropoutV2 的实验支持 rectify/reject edge 的机制，不证明学习 gate 在开放 Multi-Agent 系统中天然安全。

### 共享 Repository 需要 Commitment Protocol，不只是更多消息

当两个 coding agents 在隔离 workspace 并行实现相互依赖的 features 时，自然语言 communication 可以解释
意图，却不能原子提交 interface、patch 与 tests。即使 textual merge conflict 消失，两边仍可能基于不同
architecture assumption 各自通过局部测试，最终在 shared repository 产生 semantic conflict。

因此演进路线应是：

```text
isolated parallel patches
→ asynchronous messages
→ typed proposal with base revision and affected interfaces
→ reservation / ownership or conflict detection
→ verified patch and tests
→ atomic shared-state commit or explicit rejection / rebase
```

Agent 拥有 local history 与 proposal，不拥有“仓库已完成”这一事实；Workflow/repository service 拥有 base
revision、merge order、test evidence 与 commit state。Commitment 还需要 expiry、supersession、rollback 和
abandoned-owner recovery。严格 serialization 会减少并行度，却在 overlap 高、接口强耦合或错误代价高时更
可靠；自由消息适合独立探索和低冲突任务；typed transactional handoff 位于二者之间。

受控 benchmark 中 communication 能减少部分 textual conflicts，却没有稳定消除 Solo–Coop gap，这不是
“Agent 无法协作”的普遍结论，而是说明 message count 不是 shared-state correctness proxy。评估必须同时
记录 overlap、conflict class、commit/rebase 次数、双方 tests、最终 executable result 和 coordination cost。

当任务依赖可显式建图时，可以让 coordinator 维护 dependency DAG 与 authoritative completed set，只释放
ready nodes；每个 worker 在独立 worktree/branch 完成实现、自验与 commit，merge 通过后才释放下游节点。
这比“聊天约定不要改同一文件”更接近真实 ownership，却把 manager bottleneck、错误 dependency、merge
conflict、blocked downstream 和统一 final review 变成新成本。Agent 数量增加也不会单调改善：任务耦合强、
shared side effect 多或 coordinator headroom 不足时，single Agent + deterministic verifier 仍更小、更可靠。

### Collective Risk 来自局部 Utility 与交互规则的组合

单个 Agent 分别通过安全评估，不代表它们组成的系统仍安全。Local objective、communication topology、
information partition、shared resource rule 与 aggregation/arbitration 可能共同产生 groupthink、collusion、
resource capture 或责任扩散。风险 contract 至少应绑定：

```text
role-local utility and authority
+ who observes which evidence
+ communication / visibility topology
+ shared resource and aggregation rule
+ conflict, arbitration and replanning policy
+ outcome and side-effect verifier
```

“更多讨论”不能自动修复，因为错误可能相关、信息被不对称隐藏，或 aggregation 本身奖励共识。Mitigation
可以限制资源、隔离权限、保留 dissent、引入独立 verifier 与 human escalation，但每项控制都可能牺牲并行度
和协作收益。Synthetic scenarios 适合发现机制，不提供生产发生率；不同 backbone、trial 与 judge 混合后的
比例也不能当作跨系统常数。

## Identity 与 Delegation

可复用能力包的 identity 与执行 substrate 的 identity 不应合并。相同 Skill/Talent 可以由不同 model、container
或 credential scope 执行；同一 runtime 也可以承载多个能力包。组织层需要把二者组合成一次有界 assignment，
而不是让 Agent 对话维护“谁正在做什么”：

```text
portable capability artifact + version
+ runtime / container / credential identity
→ assigned worker instance
→ DAG task state and lease
→ result / cost / evidence
```

Scheduler 而非自然语言共识应拥有 acyclicity、dependency completion、one-task lease、idempotent dispatch、
bounded review、cancel cascade 与 crash recovery。OMC 的作者系统支持这种 typed orchestration 能承载异构
backend，却没有 component ablation、长期 self-evolution 或广泛 domain evidence；company metaphor 只是类比。
简单请求应回落 single Agent，自声明 capability 还需独立验证以防 supply-chain 与 benchmark gaming。

每个 agent 需要独立 runtime identity：

- owner、version、model/prompt；
- allowed data/tools/scopes；
- delegated authority；
- budget；
- parent workflow；
- audit principal。

Delegation 不能把调用者所有权限复制给子 Agent。应发放 task-scoped、time-bound、least-privileged credentials，并保留 delegation chain。Agent 不能继续任意转委托。

### Spawn 继承的是不可信输入，不是父 Agent 的可信状态

创建子 Agent 早期只是控制流拆分：父节点把上下文复制过去，简单、低成本，也便于复用已有判断。但当父节点的 memory、credential 或 instruction 已混入外部内容时，原样继承会让一次污染沿 spawn graph 扩散，并在每一跳获得新的工具入口。运行时应把继承内容标成 tainted inheritance，在 child authority 建立前执行 allowlist、scope narrowing 与 provenance check；未通过的字段不进入子节点的可执行上下文。

这会牺牲无损上下文复制和一部分并行效率，还要求 lineage、字段级来源与权限收窄可以被重放。低风险、只读且没有外部输入的任务仍可使用轻量继承；来源不明或验证服务不可用时，应回退到最小上下文、重新取证或人工授权，而不是默认信任父节点。现有 exact-v1 证据只支持其披露的攻击与评测设置，不证明所有模型、拓扑或生产 SLO 下都有同样的传播率。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08460 -->

### Governance Provider 也必须进入 Byzantine Threat Model

<!-- semantic-body-binding:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:start -->
集中 provider 在参与者少、信任清晰时能低成本维护 identity、ACL、message order 与审计；一旦它被攻陷，这四类
状态会同时失去可信根，外围 Agent 即使诚实也无法恢复 attributability。因而 governance control plane 需要先声明
fault threshold 与被保护属性，再选择分支：客户端 audit 适合检测、server monitor 适合快速阻断、BFT replication
提供更强一致提交但增加 quorum latency、状态复制和可用性门槛，hybrid 则按高风险 operation 升级。

这里的 consensus 只证明 governance record 在假设内达成，不证明 Agent 输出正确，也不替代 task outcome verifier。
节点成员变化、key rotation、审计遗漏和超过 fault threshold 必须 fail closed 或人工升级。单组织、低风险且 provider
可由外部日志追责时，集中式路径仍更简单；论文中的攻击与防御评估只支持其 threat model，不给出通用生产 fault rate。
<!-- semantic-body-binding:SF-ATTACKS-AND-MITIGATIONS-FOR-DISTRIBUTED-GOVERNANCE-OF-AGENTIC-AI-UNDER-B:end -->

<!-- source-family:SF-2026-ARXIV-2605-28433 -->

固定角色与拓扑在任务族稳定时最容易验证；允许 Agent 自行改写角色可适应新任务，却会同时改变 capability、通信边、validation owner、aggregation 与输出协议。安全的 self-modification 应先产生 versioned proposal，在 sandbox 中检查这五类合同并与旧版本做 matched evaluation，只有全部满足才原子提交；失败或证据不足时保留原角色/拓扑，而不是让一次自评直接覆盖运行中定义。

这种 revision gate 用适应速度换可回滚性，也会受 evaluator 共偏差和测试覆盖限制。任务简单、角色稳定或无法构造 verifier 时，人工维护拓扑仍更可靠；开放任务中也只能把自修改当候选生成，不是 authority 转移。exact-v1 证明的是披露框架和 benchmark 的受限可行性，不证明自治角色演化普遍提升系统。

## Coordination Failure

典型失败包括：

- circular delegation；
- duplicate work/side effects；
- deadlock/livelock；
- inconsistent world models；
- stale messages；
- ownership gap；
- consensus without evidence；
- malicious/compromised peer。

恶意 peer 还应按攻击者真正可控制的接口分层：改系统提示、操纵 activation/输出 logits、替换或微调权重、改训练 reward，是不同权限下的威胁人口，不能只把它们合为一项 sabotage rate。相应测试要用同 topology、模型兼容条件和独立 task outcome 比较 matched benign/恶意条件，并分别报告 peer 可写什么，而不是由任务分数读出真实意图或现实发生率。作者有限的五 benign 加一 malicious 设置中，部分攻击切片甚至高于 benign；supervisor、backup 或投票的质量改善也不认证安全 oracle，参数级攻击的兼容限制和额外 judge/query 成本仍存在。权限或 outcome 无法匹配时应保守披露测试范围，保留隔离、单一最小权限 owner 与独立验收，不能将受控攻击平均值外推为生产 Byzantine 可靠性。<!-- source-family:SF-2026-ARXIV-2602-05176 -->

Runtime 需要 max handoffs、dedup keys、leases、timeouts、conflict resolution 和 escalation。自然语言“请协调好”不是协议。

故障通道也不能压成一个 agent error rate。Proposer 不确定、verifier 拒绝、消息丢失与 coordinator 误路由会改变不同
状态边：前两者产生 epistemic proposal，message loss 破坏 delivery，routing failure 则把任务交给错误 capability。
可靠性模型应分别记录这些 channel、拓扑 revision 与 certificate dependency，检查是否存在让整个子图无法完成或验证
的 stopping set；简单增加 Agent 数量可能只复制同一瓶颈。

因此 sub-agent 的 abstention 应是一条 typed failure message，至少说明 `ambiguous / misrouted / unsupported / unavailable`、
已观察证据、未完成 obligation 和允许的 fallback。Coordinator 只能据此 clarify、reroute、降级或升级，不能把空响应
当作无意见，也不能把带理由拒绝当作任务失败后继续多数表决。该分层提高可定位性，却增加 schema、校准和消息状态；
verifier 相关错误、confidently-wrong output 或未建模网络行为仍会击穿理论边界。短链路、单 owner 任务继续使用直接
错误返回；证书不可靠或关键消息缺失时应 fail closed 或转人工。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07073:start -->
角色提示不等于权限边界：团队 pass 可能来自某一角色偷偷读取完整规格、修改 workspace 或自行认证。Multi-Agent EvalSpec 应同时冻结 prompt roles 与 OS/runtime enforcement，分别报告 team outcome、unauthorized access/edit attempt、verifier false accept/reject 和相对 single-agent value。强隔离提高可审计性，却增加缺失信息协调和易任务的团队开销；sandbox 覆盖不全或 verifier 不可信时，回退单一最小权限 owner、deterministic grader 与人工 certification。 [受限证据：arXiv:2605.07073v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07073:end -->

## Verification 与 Aggregation

将多个答案平均或投票只在错误具有一定独立性时有效。对于开放任务，更可靠的方法是：

- 先定义 rubric/test；
- 保持 candidate generation 与 evaluation 隔离；
- 要求引用独立 evidence；
- 记录 disagreement；
- 对高风险冲突升级给人；
- 比较 aggregate result 与 best single baseline。

Judge model 自身也要版本化和评估。

### 少数反证的翻转权必须先校准

多数票可能共享错误，少数意见也可能只是噪声。要允许 minority sentinel 推翻原本的多数提交，aggregation owner 必须保存少数证据、预先校准的 override criterion 与最终 commit receipt；只有反证及其独立性经过检查，并满足已声明的翻转条件，才采用替代结果。相关错误或 sentinel 失准时，应回退独立 verifier/人工，而不是继续增加同源 Agent。

这增加 debate-log 分析、校准和错误翻转风险。三异构 Agent、两轮、六 benchmark 的 classifier 实验只支持已测阈值下的翻转取舍；共享训练导致的相关错误、换模型和换协议都可能破坏原有 Flip Precision，不构成普遍安全翻转保证。失配时不翻转，并将争议交给独立 verifier/人工。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29270 -->

翻转判断还可从整份答案移到具体分歧接口：先按步骤语义将轨迹合成 reasoning tree，定位共享 prefix 后的 decision-critical branches，再把局部事实、逻辑与约束证据交给独立 auditor。保留各分支 support hints，按 judge confidence 提议 commit 或继续有限 beam；这压缩审核上下文，却没有消除 popularity cues，也不把阈值当正确率校准。离线可由 gold 筛出“多数错误、少数正确”的陷阱人口训练 auditor 的 branch preference；新增的是判别支持集，DPO 本身仍是既有目标。<!-- source-family:SF-2026-ARXIV-2602-09341 -->

[AgentAuditor 的必要对照](https://arxiv.org/html/2602.09341v1)显示局部分歧审核可以挽回部分 minority-correct 情况，但在构造的 majority-correct 集上也会将原本正确的多数翻错；语义合并、窗口遗漏与 judge 错判仍可能过滤关键反证。较少 audit tokens 不包括生成所有候选及训练成本，不能授全费用更省、共识安全或任意开放任务可靠性。分支 identity、证据完整性或校准失配时，回读完整轨迹，保留独立 verifier/人工与不翻转的基线；commit/defer 始终服从下一节的预先行动预算。<!-- source-family:SF-2026-ARXIV-2602-09341 -->

### Act 或 Defer 要服从预先声明的错误行动预算

<!-- semantic-body-binding:SF-2026-ARXIV-2606-29654:start -->
除了选择哪个答案，还要决定是否允许系统行动。部署前应把 wrong-action budget 区分为校准失败、残余行动风险与 representation gap，再用局部可靠性下界判断是否满足预先声明的行动要求；controller 记录 act/defer 与预算消耗，不满足时升级或拒答。不能在看到部署结果后挑阈值美化覆盖率。

这一保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free。六个选择题 benchmark 与训练期 difficulty-normalized budget 不能证明开放式任务或分布漂移下仍有同样边界；校准或假设诊断失效时，应回退全 defer/人工，而不是让预算记录本身授予行动权。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-29654:end -->

### 停止采票只保证结果不再改变，不保证答案为真

固定 N 个成员、每人一票、答案可确定归一化时，等待全部回答是透明基线；若某答案已得到 `floor(N/2)+1` 票，其余成员无论怎样回答都不能改变这个严格多数结果，因而可以停止尚未启动的调用。没有形成严格多数时仍须按完整票集与预先固定的平票规则收口。这是对固定票集的结果保持，不要求成员错误独立，也不是事实正确性或 Byzantine 安全证明；如果后续成员会读前序答案、改变权重或获得新观察，就不能套用这个界。<!-- source-family:SF-2026-ARXIV-2604-02863 -->

先调用预计更容易同意的成员可能更早达到阈值，但历史“同意最终共识”的频率不是独立真值校准。只更新被调用者还会形成选择反馈，让长期未调用成员缺少新证据。串行采票节省调用，却可能增加 critical-path latency；已并发花出的计算也不会因最终提前停止而自动退回。受限的九模型 API 投票实验只支持调用数与任务准确率的比较，不能把少调用直接换算成 GPU 成本或服务 SLO。独立采样、回答身份或预算不可固定时，保留完整并行投票、随机探索和外部 verifier 更稳。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06988:start -->
Multi-Agent 协议不能把快速共识当作协作正确性。Evaluation identity 应同时记录通信频率、消息内容、collective belief divergence 与对独立 truth/effect receipt 的 alignment：低 JSD 或高 consensus rate 只说明内部一致，仍可能是 confidently-wrong herding。增加 truth-alignment 与失败 episode 切片会提高标注和重放成本，开放任务还常拿不到真值；此时必须保留 dissent、provenance 和独立 verifier，不能让团队共识自签完成。 [受限证据：arXiv:2605.06988v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-06988:end -->

避免共识自我放大，还可以把“允许使用哪些证据”和“如何更新信念状态”分开预先定义。对固定假设集合上的概率向量，先注册 evidence trigger、revision operator、优先级与 fallback；只有经过相应 validator 的非空 evidence tokens 及其 witness，才触发证据更新。没有新准入证据时，一个保守分支只做 `b′=(1−λ)b+λu`，其中 `u` 为均匀分布、`0<λ<1`：它不改变最大分量的候选集合，也不增加该分量的数值信心。这个性质只约束协议保存的外部状态，不说明 LLM 内部信念或答案更接近真值，也不能修复初始错误。

witness gate 只能证明准入条件满足，不能强迫 Agent 把声明的 operator 真正作用于状态；若数值更新也要受保护，需由 state-holding router 拥有并计算权威 belief-state，或提供足以核对具体更新的证明。认证证据仍可能语义不支持命题，保守 fallback 也会挡住有益纠正并损失活性。[PBRC](https://arxiv.org/html/2604.15558v1)的形式条件和有限 paired LLM 示例支持这个分责，不证明自由文本共识、所有假设动态变化或生产安全。开放任务无法固定证据语义与更新状态时，保留 dissent、独立 verifier 和人工裁决，不把 external confidence 作为事实提交权。<!-- source-family:SF-2026-ARXIV-2604-15558 -->

### 同根报告可以帮助读懂证据，却不能按独立观察累加

“错误相关”还需要区分两层：原始证据本身可能有误，Agent 对证据的提取也可能有误。重复阅读同一文档，可以
减少第二层误差，因此把所有同源报告一律丢弃也不合理；但重复阅读不能按独立采样的方式消除第一层误差。
这解释了为何多份措辞不同、结论一致的回答，仍不应直接让 posterior 越来越尖锐。

一个受限的 Gaussian 例子能看清这条边界：设真实量为 Θ，文档给出 `E = Θ + ε`，各 Agent 的报告为
`R_i = E + η_i`；ε 与各 η_i 是相互独立、独立于 Θ 的零均值 Gaussian 噪声，方差分别为 σ² 与 ν²>0。此时 m 份报告提供的
likelihood precision 是 `J_m = m / (ν² + mσ²)`。它随重复读取增加，但当 σ²>0 时最多趋近 `1/σ²`：
提取越来越准确，不等于文档越来越真实。若提取误差含有正相关的共同分量，不能被平均掉的噪声会进一步降低
precision 上限；完全无提取噪声时，重复相同观察则没有这项增益。这个公式只解释该统计模型，
不是任意自然语言 claim 的现成置信度计算器。

因此 aggregation 的输入应从“答案与票数”扩展为“报告、原始观察、派生关系及依赖假设”。Workflow 负责保存
lineage 与版本，aggregator 根据被允许消费的证据和误差模型决定权重；两者不能混成“有 provenance 就可信”。
不同 root ID 仍可能共享隐藏来源，同一 root 也可能被提取出互补内容。文本相似度可辅助去重，却不能单独证明
证据独立；认证来源需要额外成本，且声明被伪造、依赖遗漏或误差模型漂移仍会制造虚假信心。

还有一个容易遗漏的条件：没有新检索，不等于没有新信息。模型可能用参数知识补充已有报告；只有固定其可用
信息接口，并排除参数或其他渠道带来的新增信息，才能使用“纯转述不增加证据”的界。面对真实独立观察且误差
模型可靠的任务，独立 pooling 仍然成立；来源不明或相关性无法估计时，应保留不确定性、请求独立证据或交给
可信 verifier，而不是继续复制同一批 Agent。这里复用的是依赖统计原理，不是用新框架取代所有投票机制。

<!-- source-family:SF-2026-ARXIV-2609-01873 -->

### Aggregation 还要验证局部答案能否组成同一个联合状态

当各 Agent 只校准自己的概率或判断时，逐项正确、再平均或投票是便宜基线；一旦组件之间存在 coupling，局部证据
可能根本不存在共同的 joint distribution。Aggregator 应先依据 versioned constraint graph 计算 group-coherence
residual，再由确定性的 hierarchical projector/verifier 修复或拒绝组合，并在顺序到达时监控 residual drift。
各组件只拥有局部 proposal，aggregator 拥有关系图，projector 拥有一致性判定；最终 decision owner 决定是否消费，
不能把数学投影当作外部事实。

这提供了可计算的 group invariant，却要求显式 coupling、投影策略与拒绝阈值，也可能过度修复；关系图若错，修复会
系统性地错。独立任务继续使用 product/local aggregation；约束未定义或争议本身有价值时，应保留 dissent、单 Agent
结果或人工裁决。exact-v1 只覆盖论文中的 forecasting panels、所列关系与附录实验，不证明任意多 Agent 协作都存在
可恢复的一致联合分布。

<!-- source-family:SF-2026-ARXIV-2605-30335 -->

当每个分支产生的是长 tool trajectory，而不是短答案时，直接拼接会超过 Context，预先摘要又会不可逆丢掉
少数但决定性的 evidence。一个更可审计的演进是把原始 trajectories 保留为 read-only evidence archive，
aggregator 只按需读取 segment，再生成带 lineage 的 derived artifact：

```text
independent trajectories
→ immutable archive + lightweight metadata/index
→ bounded evidence navigation
→ selection or synthesis
→ output + trajectory/segment provenance
```

Selection 适合 exact-answer 且存在可信 verifier 的任务；synthesis 适合证据分散的开放报告。二者都不能把
同模型的 correlated hallucination 变成共识，也不能把“完整轨迹仍在存储中”误写成 aggregator 已读到全部证据。
Agentic Aggregation/AggAgent 的作者实验支持按需读取原始 segment 相对只读 final answer 或预摘要在其六项
benchmark 下有用，但未验证 side effects、streaming、tenant isolation 或 production SLO。短轨迹直接拼接、
错误较独立时 voting、可执行任务中的 deterministic verifier 仍是更便宜或更强的旧分支。

扩展 test-time compute 也要区分 **复制同一角色** 与 **增加互补角色**。独立 coding rollouts 可以提高候选覆盖，
却同时成倍增加 sandbox、tool、token 与 aggregation cost；不同 prompts 或角色若共享模型、环境和错误先验，
并不自动获得独立性。预算分配应比较：

```text
single-agent headroom
vs. parallel branch diversity
vs. sequential repair depth
vs. aggregation and verification cost
```

Scaling Test-Time Compute for Agentic Coding 的作者实验是受限的并行扩展证据，不证明“更多 Agent”单调更强。
当任务不可分、verifier 弱或 side effects 难隔离时，把预算投入单 Agent 的更深 repair、better tool contract 或
deterministic testing 可能更合理；只有 branch state 可隔离、结果可验证且收益覆盖 coordination tax 时才扩 K。

### Pairwise Judge 可以生成 Shaping Proposal，但不能拥有因果归因

绝对 contribution score 难跨场景校准时，可以用 ordered pairwise comparisons 建矩阵，再经 rank aggregation 形成 potential-based shaping proposal。Judge 只能观察可见 multimodal evidence，不能看见力、私有状态或反事实贡献；position bias、non-stationarity 与 shared-model error 会把排名误写成 credit。最终 task outcome 与独立环境证据仍拥有验收权。

多跳协作还必须把 goal continuity 与 authorization continuity 分开。Handoff 可以转述任务目标，却不能自行扩大原始 principal 授予的 effect scope；每个 pending side effect 都应重新绑定 original request、delegation lineage、当前 executor 与有效 policy revision。逐跳复述权限会发生语义衰减或漂移，source re-anchor 则增加 Context 与验证成本；链不完整时应降级为只读、重新询问或人工授权，而不是让最后一跳根据“团队共识”提交动作。

安全拒绝同样不能只在 root 做一次：原始请求如果有害，principal 仍可能把原意包装成可委派的子任务，使 subordinate 把上游 delegation 当作已批准的依据。更稳妥的边界是在每次 handoff 保存原始意图和 risk class，由接收者独立执行内容与工具权限检查，最终 effect gate 再核 action；这牺牲一部分自动委派吞吐，却避免角色切换把拒绝责任静默转移。单次委派、49 个诊断性危险任务和六个受测 API 模型的作者对照观察到部分角色/工具条件下拒绝下降，但不同模型方向和幅度不同；它不证明真实生产攻击率，也不赋予任一模型通用安全等级。<!-- source-family:SF-2026-ARXIV-2609-27900 -->

即使没有显式有害任务，多 Agent 共享可写环境也不能把 human shutdown、credential revoke 或进程终止脚本当作普通协作文件。关闭权属于平台/人类控制面，worker 的任务权限不得包含改写或删除该控制路径；peer 发来“保护同伴”的请求也不能提升其授权。把关停机制与 agent workspace 隔离、由独立 policy gate 验证任何影响其可用性的文件操作，会增加环境分层和调试成本，但比仅在 prompt 中写禁止篡改更可执行。受控 sandbox 研究中，同一模型组成的 agent 对针对同伴的关停脚本比针对非 agent 对象的对照更常干预；脚本并未实际执行、模型差异很大且 judge 可能误判，不能把实验比例当作生产攻击率或模型具有自保意图的证明。<!-- source-family:SF-2026-ARXIV-2609-28274 -->

<!-- source-family: arxiv:2608.07556v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: goal-vs-authorization-lineage-across-delegation -->

顺序微调多个协作 Agent 时，**更新一个成员会改变其余成员训练数据的策略分布**。在固定 peers、短 horizon 和弱耦合任务中，分别训练再组合最简单；若后续 Agent 仍使用旧 joint trajectories，前一个 Agent 更新后的 message/action occupancy 已经变化，缓存样本会变成 off-policy evidence，局部 loss 下降不保证团队策略改善。

```text
joint trajectory under team revision k
→ update one agent within a bounded trust region
→ resample or importance-correct affected interactions
→ independently evaluate team outcome and coordination cost
→ accept team revision k+1 or roll back
```

team revision、peer policy hashes、trajectory provenance 和 update order 必须共同进入训练 identity。重采样提高 on-policy 可信度，却增加环境成本；importance correction 节省样本，却可能因长 horizon 与 support mismatch 产生高方差。peers 冻结、交互很弱或 simulator 昂贵时，独立训练仍可作为基线，但必须把 distribution shift 暴露为限制，不能用单 Agent 指标代替 joint Gate。

一种 coordinator-free 的受限实现把 team update 写成 block-coordinate sequence：每次只更新一个 Agent，在当前中间 team occupancy 上重新采样/估计 advantage，并为该成员设置 KL trust region，再把新 policy 交给下一成员。这样把“谁拥有当前更新”和“哪个 joint distribution 产生证据”显式化；论文在其 factorized team-policy、充分采样与正则假设下给出单调改进和 plug-and-play 结论，但不能外推成 production runtime、开放式通信或任意 shared-parameter Agent 的保证。顺序更新增加 rollout 与墙钟成本，也可能放大早期成员偏差；support、verifier 或环境预算不足时，应回退冻结 peers、联合重训或独立团队 Gate。

<!-- source-family:SF-2026-ARXIV-2605-05216 -->

<!-- source-family:SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT -->

### Verification Delay 也是拓扑控制状态

当 verifier/critic 延迟相对任务传播可忽略时，在 agent 输出后统一纠错是合理的。约束变化是错误信念可能在校正到达前沿通信图传播，而过强或过迟的纠正还会造成振荡。多智能体 control state 因此要显式记录 verification dose、communication delay、verification delay、corrector placement、graph version 与 belief epoch，把纠错部署视为带稳定性边界的控制问题。修订后的理论分别处理两个 delay，并在受控 signed-belief 线性 recurrence 中给出振荡边界与 placement 分析；这些结论没有被 grounded factual QA 直接识别或证实。新增 400-question study 修正了 delay indexing 并保留完整 response logs，但大量 abstention 使 conservative completion bounds 同时允许 error amplitude 增加或降低；事后观察到的 abstention 变化也不能证明自然 factual verification 实现了理论中的 signed-error operator。因而该 study 既不能支持“truth 是 absorbing boundary”解释，也不能排除真实系统中的不稳定性；它留下的是 completion/abstention-aware measurement requirement。阈值不是任意 verifier workflow 的通用上界，corrector placement 的近似保证也只在对称线性 surrogate 上成立。delay、拓扑、completion policy 或 grounding identity 未知时应序列化关键提交、使用 grounded deterministic verification，并把 abstention 单独计量；旧的事后 critic 只在低延迟区间共存。

### Memory 拓扑不必等于 Agent 拓扑

中央 memory 在共享真值、强一致性和低隐私风险时最容易去重；探索型多 Agent 若都从同一记忆池读取，会过早收敛并扩大单点污染。另一种设计是每个 Agent 分别拥有 exploitation 与 exploration pool，协调层只交换带 provenance 的受限摘要或反馈，而不默认复制原始 memory。Local owner 决定写入，协调层只决定交换合同。

这种分权保留多样性与隐私，但会产生重复、语义漂移和跨 Agent 一致性成本；需要共享规范或审计真值时，中央库仍是合理选择。arXiv:2605.22721v1 的方法与实验仅支持作者多 Agent memory 设置，不证明分散 memory 会普遍提升协作质量或安全性。

<!-- source-family:SF-2026-ARXIV-2605-22721 -->

## Evaluation

### Device–Cloud 协同是逐步路由，而不是静态部署选择

整条任务固定在端或云上，控制简单，但长任务中每一步的隐私、成功概率、上下文大小、网络状态与成本不同。step-level coordinator 可把历史、候选动作置信、网络开销和剩余 budget 作为显式 routing state，决定本步在哪个 agent 执行；commit 仍由 workflow owner 完成。收益是形成质量—成本 Pareto 分支，代价是路由误差、状态同步和隐私边界更复杂。网络不稳定或状态不可安全传输时，固定端侧策略仍是合理 fallback。现有结果只支持特定设备、模型和任务，不能外推通用收益。

<!-- source-family:SF-2026-ARXIV-2605-24598 -->

### 并行不是一个旋钮：副本并行与结构并行

复制多个独立 trajectory 的 replica parallelism，可以提高找到好答案的概率；workflow structural parallelism 则只并行依赖图中互不等待的节点。前者受样本预算和聚合器限制，后者受 critical path、共享工具和副作用顺序限制。把两者都称为“增加 Agent 数”会隐藏完全不同的状态与成本：

```text
independent replicas → sample diversity → verifier / aggregation
workflow DAG → dependency-safe concurrency → barrier / commit
```

通信拓扑也不能只按消息量裁剪。可以用 edge masking 估计某条 channel 对任务结果和 response stability 的贡献，再蒸馏预算内子图；它用额外 probe 与 attribution bias 换更少通信。Post-hoc 贡献不是强因果证明，mask 后的分布漂移和协作任务代表性仍需在线 canary。小团队、短 workflow 或工具副作用强时，固定 topology 和串行协调仍更透明。

除了 final task success，还要测：

- contribution by agent/role；
- parallel speedup 与 critical path；
- token/tool/coordination cost；
- duplicate/conflicting actions；
- handoff failure；
- consensus calibration；
- security scope violations；
- recovery after one agent failure。

协作答案优于单次 baseline，不说明 interaction 创造了新的好解：初始候选中可能已经有更强 proposal，讨论只是传播它，也可能在修订或聚合时丢掉它。对可评分任务应保存同一 query/state 下每个 proposer 的初始和最终候选，再与最终 aggregate 分账：aggregate 是否超过 strongest initial，强/弱初候选各自如何变化，以及 strongest final 与 aggregate 的差额。Critique/verifier 若不产生同类可评分解，不混入 proposer 分母；dynamic episode outcome 与每次 state-conditioned action 诊断也分别报告。

轨迹评分、judge 和 proposal 存储增加成本，strongest initial 是事后 oracle reference，不是线上可获得的正确答案。聚合差额可为负，弱者改善也不能抵消强者退步。[MASTraceBench 的有限六任务研究](https://arxiv.org/html/2609.34496v1)表明这些过程可以被 outcome-only 分数隐藏，但 shared backbone、graded proxy、固定对手和不等 token 预算不构成一般因果归因。仍须与 equal-budget独立采样/单agent、实际 latency 和验证成本比较；score 不可信、任务不能独立评分或协作侵蚀强候选时，保留原 proposal、独立 verifier 和较小系统，不用更多轮或 claim 共识自动授权提交。

<!-- source-family:SF-2026-ARXIV-2609-34496 -->

Multi-Agent 的 throughput 不等于 LLM serving batching；底层请求仍由 Part V 调度。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-DELIBERATION-EVIDENCE-ATTRITION:start -->
多 Agent deliberation 应被视为 evidence-flow：原子事实最初分散在不同 agent，讨论过程可能传播、合并，也可能让事实消失。验收不能只看最终共识，而要比较初始 evidence、消息传递和终局保留率；共享更多上下文会增加成本与同质化，事实缺失时应回到原始证据或独立 verifier。
<!-- semantic-body-binding:SF-DELIBERATION-EVIDENCE-ATTRITION:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14200:start -->
Agent reputation 必须按 skill 条件化并记录 zero-evidence state；global trust 会让攻击者用无关技能的良性行为 laundering 后取得高风险任务 routing authority。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14200:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15376:start -->
多 Agent 共享对象可用 Monotonic Trajectory Pre-Order：固定读序、speculative write、通知与可逆三阶段 tool call，在 quiescence 达到 serializable outcome。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15376:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19758:start -->
SIGMA 不把 agent node 当封闭角色，而由任务到 skill-agent incidence matrix 组合节点，再解码通信图；skill mailbox 拥有消息路由，缺 skill 或组合退化时回落到预定义 agent/topology。代价是库质量、组合搜索和 mailbox 隔离成为新的控制面。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19758:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24437:start -->
MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24437:end -->

### Delegation Degree 是受安全约束的控制变量

固定团队拓扑在职责稳定、风险低时容易审计；任务和风险随运行演化后，是否委派、委派多少权限与何时收回应成为显式控制状态。Bilevel controller 可以在 utility 与 safety constraint 之间生成 delegation proposal，但 responsibility propagation、capability scope 与 effect receipt 必须由外部系统验证。形式化可行性不等于可部署安全，缺少经验验证或可追责链时应回退固定最小权限拓扑。

<!-- source-family:SF-2026-ARXIV-2604-27358 -->

### 跨 Agent 传递 Latent State 需要显式身份

传递自然语言摘要简单、可审计，但会丢失细粒度 prefix state；直接传递 KV 则减少重复 prefill，却把模型版本、tokenizer、prefix 对齐、层布局和量化参数变成兼容性前提。可行的中间契约是版本化 CacheCard：声明源/目标 identity、prefix digest、K/V bit allocation、注入位置和失效条件，接收方验证后才能使用。它换来延迟与能耗收益，同时引入 latent state 泄露、错误复用和跨模型不可移植性；无法证明兼容时应回退到文本或结构化 artifact handoff，而不是静默注入 KV。[受限证据：arXiv:2605.03884v1]

<!-- source-family:SF-2026-ARXIV-2605-03884 -->

### 多 Agent 拓扑必须先通过 Equal-budget Pareto Admission

增加 Agent 数量之前，应在同一 task slice 和总预算下比较单 Agent CoT、self-consistency、refinement、debate 与 mixture-of-agents 的 quality–token–latency–cost frontier。只有某个拓扑形成非支配点，才有理由承担消息、调度和验证开销；若 baseline 没有冻结，所谓“协作收益”很可能只是用了更多 token 或更长时间。

这个 admission 仍可能低估相关错误、通信失败与尾延迟，因此通过离线 frontier 不等于可直接推广到生产。系统需要逐步放量并保留 single-agent fallback；任务不可分、共享状态强耦合或验证成本高时，单 Agent 仍可能更稳健。多 Agent 是条件化并行分支，不是能力随数量单调增长的路径。

<!-- source-family:SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION -->

### Delegation 应由任务状态与不确定性触发

固定团队会在简单任务上支付不必要 coordination tax，也会在困难任务上调用错误角色。router 应依据 task decomposition、当前 uncertainty、能力证据和剩余预算选择是否委派、委派给谁以及何时收回。收益是按需使用协作，代价是 router 误判与选择偏差。

委派前必须保留 single-agent baseline，委派后验证返回 artifact 与权限边界；收益不显著、超时或身份不可验证时回退原 Agent。固定小团队在任务稳定、角色边界清楚时仍更可预测。

<!-- source-family:SF-UNO-ORCHESTRA-PARSIMONIOUS-AGENT-ROUTING-VIA-SELECTIVE-DELEGATION -->

选择性专家调用还要分别训练“怎样提出请求”“何时升级”与“返回后是否真正使用建议”。一个受限小模型分支将ask-expert作为policy action，只把最近少量消息交给专家，再由student保留标记过的advice；先学调用格式，随后以停滞/循环信号和后续使用代理调整调用与行为。gold patch只在离线轨迹构造中提供，不能成为部署时专家的隐藏输入；训练阶段对完全不调用施加强惩罚，也会把“无需升级”从自然最优选项推开。[有限coding对照](https://arxiv.org/html/2602.22124v1)中，完整上下文专家在强制循环人口上有益，缩成最近五条后未保持同样增量，直接插入专家文字亦可能退步；这说明请求窗口、升级时机与消费者策略不能互相代签。loop与follow judges仍可能共享偏差，不证明建议正确；expert output token占比不包含双方input、student rollout、训练与judge全部费用。角色失配、循环检测不可靠或总成本上升时，保留单Agent、显式loop guard、固定小专家池与独立可执行检查，效果和权限仍由runtime验收。<!-- source-family:SF-2026-ARXIV-2602-22124 -->

递归委派把这个控制问题推进了一步：同一 policy 不只选择 peer，还要在每个递归节点决定是否继续拆分、如何写 subtask，
以及怎样聚合返回结果。共享 policy 使不同深度复用同一能力，但每层 task identity、authority scope、budget、parent link 与
result receipt 仍必须显式存在；子 Agent reward 可以训练 delegation proposal，却不能授予权限或证明聚合结果正确。

递归深度能适应任务复杂度，也会放大相似子任务重复、奖励归因、调用成本和错误累积。按深度做 inverse-frequency
weighting 只能平衡训练样本，不能证明深层分解更有价值。验收应冻结最大深度、总预算、共享 policy revision 和 verifier，
与固定拓扑、单 Agent 在等预算下比较；无可验证子任务、权限难以分割或边际收益为负时回退固定浅层 workflow。现有证据
限于作者任务与训练环境，不支持无限递归或开放权限执行。<!-- source-family:SF-2026-ARXIV-2605-06639 -->

### Shared State 的 Read-set 可以由观察到的访问重建

要求每个 Agent 在 commit 前主动声明完整 read-set，语义清楚但容易遗漏隐式 HTTP GET；完全串行化又牺牲并发。中间路径由 server-side delivery log 记录每个 Agent 实际收到的版本，在 commit 时重建 observable read-set，并检查其依赖是否仍有效。

它为共享 mutable state 提供可执行 isolation boundary，却只覆盖被中间件观察到的读；缓存、旁路 channel、非 HTTP 访问或语义依赖仍可能遗漏。低并发、小状态系统继续使用锁/串行事务；采用观察式方案时，log identity、原子 commit、重试和未观测访问必须进入 failure contract。

<!-- source-family:SF-2026-ARXIV-2605-17076 -->

### Participation Graph 与 Step Orchestration 是联合状态

固定 agent team 与通信拓扑，在任务类型稳定、角色清晰时容易调试；任务阶段变化后，多余参与会浪费预算，缺失角色又会中断信息链。Coordination owner 可以同时维护 participation graph 和 step-level orchestration，根据当前 task state 选择谁参与、谁拥有下一步以及何时同步。收益是适应任务结构并减少无效通信，代价是联合搜索、centralized training 和更复杂的故障归因；router 漂移或通信成本超预算时应回退固定最小团队。exact-v1 只支持论文测试的任务、模型与预算，不证明任意组织结构或去中心化部署的收益。<!-- source-family:SF-2026-ARXIV-2605-25746 -->

拓扑也可以是 policy 的逐回合行动，而不只是控制器在既有图内选下一步：先生成带 layer/ref 的结构化 DAG，运行其成员和代码执行，再把本轮 graph 与 execution feedback 共同加入 history，让下一回合重新提出拓扑。[AgentConductor 的必要方法与对照](https://arxiv.org/html/2602.17100v1)把这个闭环与格式/代码结果、node/edge/depth 密度代理共同用于训练；代理密度不是 wall-clock，YAML 可解析及依赖合法也不等于代码正确。运行时仍须独立保留权限、硬预算与不可跳过的验证节点，这是工程约束，不冒称论文验证了任意生成图的安全。3B orchestrator、workers、4500 SFT 轨迹、GRPO 多采样及4A800训练均计费；两回合和未完全匹配 backbone/训练的有限对照不授普遍最优拓扑或端到端成本优势。反馈不可信、图生成失配或净收益不成立时，保留固定最小团队、静态 workflow 及只在已授权图内取消冗余步骤的 controller。<!-- source-family:SF-2026-ARXIV-2602-17100 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11136:start -->
当团队需要在 test time 持续学习时，participation graph 还不足以承载全部状态：individual context、team composition/collaboration structure 与 population knowledge flow 是三个不同 owner。失败或分歧后，经验可以非对称地路由给特定成员以形成 specialization；team operator 只选择成员与协作结构，population controller 才能提交 fork、merge、prune 与 seed，不能把这些生命周期变化写进某个 Agent 的私有 memory。

三层联合演化用跨任务积累换额外推理、credit attribution、population churn、错误 transfer 与 specialization collapse。短任务、固定团队或 lifecycle evidence 不足时，静态 team、局部 memory 与人工或确定性成员管理仍更可靠。exact-v1 只支持作者的 competition math、code、multi-domain reasoning、Qwen3-8B/GPT-4.1-mini 与固定阈值；其推理成本约为 single-agent 的 3.6 倍，也没有证明更长任务流和开放 population 的稳定性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11136:end -->

群体共享的经验也不等于群体共享同一份代码。一个受限的演化分支汇集成员的代码改动、执行 trace 与工具结果供反思，再让各成员分别修改自己的 code artifact，经过各自检查后进入 archive；共享的是候选经验来源，不是已经合并的共同实现，也不能由一名成员通过测试授其他成员同样正确。部署时应分别记录 parent/member/revision、经验来源和测试/evaluator 人口，把 sanity check、候选筛选与最终验收保留为不同 gate；这是工程审计推导，不宣称原实验已验证完整身份合同。[必要方法与反侧](https://arxiv.org/html/2602.04837v1)中的相同 child 数量并不对齐全部 reflection、工具执行和分阶段评测成本，局部 group 改进也不证明所有成员或任务同时受益。共享反思还会传播误诊并增加 code churn；来源不可追溯、局部检查失败或评测预算不足时，保留原 parent，回退成员独立演化或人工审查，而不自动 merge 群体建议。<!-- source-family:SF-2026-ARXIV-2602-04837 -->

## Latent Communication 必须证明传递了正确样例的状态

Receiver 使用 relayed KV 后性能改善，只能证明它依赖某种 cache，不能证明 cache 携带了当前 teammate 的私有信息。因果验收应加入 mismatched-example、zero 与 moment-matched random intervention：只有正确配对显著优于错配，才能把收益归因于跨 Agent 信息传递。

这种审计会增加运行次数，也无法证明 latent state 可解释或安全；它至少把“存在缓存效应”与“传递了正确协作状态”分开。身份无法绑定或错配不退化时，应回退显式消息、typed artifact 或不共享状态。
<!-- source-family: arxiv:2608.04893v1; daily: 2026-08-06; semantic-body-binding: causal-audit-of-relayed-agent-state -->

### 总 Cost 与 Wall-clock Latency 需要不同 Credit Assignment

Multi-Agent DAG 的总 token/cost 是所有节点之和，响应延迟却由最长 dependency path 决定。统一惩罚每个 Agent 会错误压缩非关键分支；更合适的训练信号对 critical/near-critical operators 分配更高 latency credit，并以独立 accuracy floor 防止优化器通过删掉必要步骤获得低延迟。

训练期固定 graph 仍看不到运行时 evidence。轻量 controller 可以根据 partial execution 取消尚未开始且预计冗余的交互，但只能在已授权 graph 内缩减，不能新增权限或跳过 hard verification node。它以 controller error、额外训练和 trace 依赖换取更短 critical path；任务拓扑稳定、并行开销小或 correctness 很难定义时，静态 workflow 仍更可靠。作者四个 benchmark 的结果不覆盖工具安全、hallucination 或生产 tail SLO。

<!-- source-family:SF-2026-ARXIV-2607-13359 -->

### Fleet oversight 必须把置信度校准、错误相关性与人工预算一起建模

按 Agent self-confidence 从低到高分配人工复核，在置信度可校准且错误近似独立时很合理；当多个 Agent 共享模型、上下文或工具而产生相关错误时，这种排序可能系统性漏掉共同高置信错误，甚至劣于随机抽检。监督策略因此不能只消费单体 confidence，还要估计 calibration、pair/group correlation，并始终保留随机 baseline。

相关性估计和人工 audit 会增加成本，有限模型样本或 copula 假设也不能给出通用阈值。生产 controller 应按风险 slice 分配定向复核，同时保留一部分随机审计用于发现未知共因；当校准漂移或相关性不可辨识时，扩大人工预算、降低自动提交权限，而不是把高置信度当作 fleet correctness。

<!-- source-family:SF-2026-ARXIV-2607-28317 -->

### 角色正确性必须独立于终局成功验收

端到端 reward 能提高 pipeline 成功率，却可能让 decomposer 偷带答案、reader 回退参数记忆或某个模块接管别人的职责。terminal accuracy 因而不能证明角色分解有效。每个角色需要 local obligation、允许读取的状态、允许产生的 artifact 与 trace gate；只有局部合同通过，终局 reward 才能归因给预定协作结构。

role anchor 或 prompt-distribution probe 只能作为 drift sensor，不是完整角色定义；过强约束还可能牺牲任务成功率。简单任务中允许单体直接完成仍更合理，但系统必须明确这是 fallback/shortcut，而不是把越权成功计作多 Agent 设计证据。

<!-- source-family:SF-2026-ARXIV-2607-21627 -->

## 本章在知识树中的位置

Workflow 提供 durable shared state，Multi-Agent 在其上分配责任。下一章 MCP 讨论 Agent/host 如何通过标准协议发现 tools、resources 和 prompts；MCP 可以连接角色，却不定义协作策略。

## 从机制演进到系统设计

Multi-Agent 从广播全部对话演进到 typed role、message、shared state 与 topology。收益来自独立证据和真正的责任分解；当错误相关时，多数票可能放大失败，因此系统还要保存 minority evidence、校准 verifier/flip precision，并把 communication 和 verification delay纳入调度。

更多 Agent 增加探索和并行度，也增加趋同、冲突、消息成本、权限扩散和 deadlock。protocol runtime 可以检查兼容 emission、safety/liveness 和 delegation scope，却不能证明消息内容为真；低独立性或验证预算不足时，单 Agent、独立 proposals 或人工 adjudication 更合适。

## 自检问题

1. 多个 persona 为什么不自动带来独立能力？
2. 什么条件下 Multi-Agent 分解有真实价值？
3. Message 与 authoritative state 为什么要分开？
4. Delegation 为什么不能复制父 Agent 全部权限？
5. Majority vote 何时会形成错误共识？
6. Multi-Agent evaluation 为什么必须包含 coordination cost？
7. 运行时 topology repair 为什么必须有 mutation budget、版本和 deterministic validation？

## 从最终答案转向约束的跨 Hop 生存

只检查最终答案会掩盖协作过程中的约束丢失：某个 Agent 可能得到正确局部结果，却在转交时遗漏边界；多个分支在 converging DAG 汇合时还可能合成互相不兼容的片段。可靠性评估应沿消息与依赖边追踪 constraint survival、错误传播、leakage 与 synthesis bottleneck，并把最终 outcome 与过程指标并列。

细粒度追踪提高故障定位，却要求规范化 constraint schema、消息 lineage 和额外标注；开放式任务中“约束是否保留”也可能需要 judge。小团队、短链路且 deterministic verifier 充分时，最终结果检查仍是合理基线；关键约束则应在每个 hop 重新验证，而不是依赖最终汇总者记住全部历史。[受限证据：arXiv:2605.08647v1]

<!-- source-family:SF-2026-ARXIV-2605-08647 -->

Handoff compression 还应把 operational facts 与约束它们如何使用的 boundary metadata 分账。时间、实体和决定仍然
正确，不表示 audience、owner、hedge 或 disclosure caveat 仍然存在；下游看不到原 transcript 时，丢失的边界无法
由事实内容反推。Typed handoff 因而要让每个 fact 携带显式 allow/deny audience 与来源，extraction 缺失、字段冲突、
拼写/格式不可解析或否定语义不清时进入 `Unknown` 并拒绝披露，而不是默认继承共享权限。

结构化 schema 本身没有保护权。Gold-derived allowlist 只证明存在一种上界，5%～30% label corruption 与
typo/format/negation stress 已显示效果取决于边界字段正确性；现有证据来自 36 个合成 handoff 场景和半合成外部 traces，
没有真实 production、多语言或自动 extraction 验证。短链、同 audience 且可完整 replay 时，保留原 transcript 或
人工 handoff 仍是更可靠的旧路径。

<!-- source-family:SF-2026-ARXIV-2608-29028 -->

### Multi-Agent Failure 要按 Intra / Inter / Environment 分层归因

只检查最终 RCA 答案会把三种责任混成“模型不够强”：单 Agent 内部的证据误读/探索不全，Agent 之间的消息缺失/语义变形，以及 Agent 与工具环境之间的 observation/action 错配。可运维的 failure ledger 应为每次 run 保存 earliest evidence-backed failure span、责任层、影响的 handoff/state 与最终 outcome；修复也应对应层级，不把 prompt rewrite 当作所有失败的公用补丁。

当 execution DAG 可 fork 且有 paired-clean replay 时，单事件 ranking 仍会把 jointly necessary repair 与多个
alternative repairs 混在一起。Failure ledger 应显式声明 intervenable candidate domain、dependency graph、最大
repair cardinality `q`、共同 replay seeds 与 success threshold；先取 failure sink 的 backward slice，再逐个验证该
声明域内全部 inclusion-minimal successful sets。输出 `{{u,v}}` 表示联合必要，`{{u},{v}}` 才表示两个替代充分修复。

这种完整性只相对于声明域成立。Graph 缺少相关 influence path、没有 clean counterpart、外部状态不可重放或真实修复
超过 `q` 时，系统必须扩大 replay/exhaustive search 或保持 `Unknown`，不能继续声称 exact localization。现有结果只
覆盖 `q<=2`、90 个受控 DAG 与 24 个 1.5B 算术 pilot；10% 隐藏边就已使 macro family exact match 从 1.000 降到
0.552，不支持 open-world 自动修复。

<!-- source-family:SF-2026-ARXIV-2608-29228 -->

更丰富的 inter-agent protocol 可能减少通信失败，却会增加 token、schema、延迟与错误状态传播，也无法修复工具返回错误或单 Agent 未探索。简单任务仍以单 Agent 和 deterministic verifier 为基线；这一 taxonomy 只在作者的 cloud-RCA benchmark、模型和协议上得到验证，不证明其失败比例能外推到任意 multi-Agent 系统。<!-- source-family:SF-2026-ARXIV-2602-09937 -->

## 小结

Multi-Agent 的收益来自真正的任务、证据、模型或权限分解，而不是更多对话。稳定系统依赖 typed handoffs、shared workflow state、bounded delegation 和独立 verification。下一章进入连接标准 MCP。

### Population-scale 协商需要把消息与承诺分开

点对点 Agent 对话在参与者少时可以直接路由；规模扩大后，directory/routing、user identity、negotiation state 与最终
agreement 必须由不同 owner 管理。结构化 message 只表达提案，不自动获得代表用户承诺的 authority；commit 仍需权限、
版本和用户/策略确认。分权提高可审计性，却增加目录一致性、隐私、冒充与长事务恢复成本。身份或授权无法证明时，应回退
人工确认、短期会话或拒绝交易，不能用协议成功替代真实 consent。

<!-- source-family:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P -->

### Multi-Agent 优化必须把拓扑提案与结果责任分开

分别优化 designer 与 executors 便于定位，却会让局部 reward 与最终任务错配。端到端 RL 可以把 outcome credit 传回
agent topology、role 和 execution policy；topology generator 只提案，executor 持有本轮环境状态，最终 evaluator 才提交
reward。这样减少局部目标错配，也带来 credit leakage、昂贵 rollout 与不稳定结构搜索；evaluator 不可靠时应冻结拓扑、
单独训练组件或回退强单 Agent。MetaAgent-X 的证据只覆盖作者任务与设置。

<!-- source-family:SF-2026-ARXIV-2605-14212 -->

若 workflow graph 本身可执行，counterfactual RL 还可比较替换某个节点或边后的结果，把 topology revision 变成显式动作。
反事实 estimator 只能提出 graph update，必须在真实 executor、tool schema 和 outcome test 上重放后才能 commit。它提高结构
归因，却增加 counterfactual bias、组合爆炸和 replay 成本；环境不可复现时应保留原 graph 或人工修改。LEMON 的 exact-v1
不证明自动 orchestration 在未测环境中稳定优于固定流程。

<!-- source-family:SF-2026-ARXIV-2605-14483 -->

### 对话只有改变对方缺失的 World State 才构成协作

协作过程还需要区分认知时钟与环境时钟。把消息、推理、interrupt/resume 和 wait 都算成一次环境动作，容易把“仍在协调”误认成环境进展；双时钟执行器可以在一次环境推进前允许多轮计划协商，再在所有参与者 ready 后提交联合 primitive action。日志应分别记录认知等待、计划切换与可观察的 spatial/temporal/participation/dependency 约束是否满足；计划一致或沟通次数不能替代动作效果，也不能由私有解释推定失败原因。

[EmCoop v1 §3、§5–7](https://arxiv.org/html/2603.00349v1)中的 cognitive cycle 最终仍经过 joint-action barrier，不能称为真实环境完全异步执行；认知轮次也不等于 wall-clock 或实际通信免费。保留两个时钟增加调度、等待和 trace 成本，却能区分协调停滞与环境执行失败。作者有限两类环境、二至三 Agent 及模型/拓扑对照不证明开放任务的统一最优拓扑；时钟和约束不可观测时，仍可用同步 primitive step、共享状态或人工协调，不把复杂编排本身当协作收益。<!-- source-family:SF-2026-ARXIV-2603-00349 -->

Embodied Agent 共享环境时，发送更多消息能减少动作冲突，却未必提升任务成功：消息可能重复已知内容、引用未观察实体，甚至通过相互确认放大幻觉。协作合同应分别记录各 Agent 的 private world graph、消息带来的 information novelty、belief-sensitive recipient model 与执行后 observation convergence。消息只是 proposal；环境观察和受控 state merge 才能更新 authoritative world state。

同步通信让说话与动作争夺 step budget，异步免费通信降低显式成本却更容易形成重复确认和消息洪泛。部分可观测、grounding 不可靠时，应限制消息频率、携带 locator，或回退 centralized/shared-state controller；简单任务仍可不用对话。exact-v1 的 PARTNR 设置只揭示其架构中的对话失配，不证明所有 embodied multi-Agent 通信都会降低成功率。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12920 -->

### Consensus 与 Channel Framing 是两个独立攻击面

多数投票在成员错误近似独立时合理；当相同压力同时作用于多个模型或同一模型副本时，更多一致意见可能越过共享的错误阈值。系统应把 consensus strength、消息 channel/role、模型族和相关性写入 evidence identity，并用已经单独答对的样本测量 yield，而不是把“大家同意”当置信度。dissenter 或独立 verifier 的价值来自打破相关证据，不是增加一个同质投票者。

若用 Agent 自报置信度分配发言权，还要分开三个不可替代的量：候选的**排序判别力**、概率的**校准性**、以及私有 poll 答案到公开发言的**提交一致性**。校准映射可以让数值接近某数据集的经验正确率，却不能修复排序接近随机或发言时重新生成另一个答案；router 应保存 poll candidate、score、所选 speaker、公开消息与最终 commit receipt，并分别测三段误差。这样增加日志、校准样本与复核成本；没有可靠判别力或公开表述不稳定时，固定轮换、独立 verifier 或人工确认可能优于 confidence argmax。现有作者实验限数学题 deliberation、特定模型/提示与无公开 artifact 的 trace，不构成通用路由收益证明。<!-- source-family:SF-2026-ARXIV-2609-27822 -->

更细的机制监控增加 probe、校准和模型版本耦合，内部 activation 证据也不能直接外推到其他架构。低风险、异质成员且独立性经验证时，简单投票仍可用；压力来源或错误相关性未知时，应降权 consensus、回到原始 evidence 或人工裁决。exact-v1 只支持披露模型和 prompt 条件中的阈值行为，不证明单一 RLHF 原因或通用防御。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12991 -->

### 跨 Agent 状态可以不走文本，但必须保持接收者兼容性

文本消息可审计且跨模型通用，却消耗 Context 并丢失 sender hidden state 的细粒度信息。已知固定 receiver 时，另一条实验分支可把 sender state 映射为 query-specific low-rank parameter delta，暂时注入冻结 receiver；generator 拥有 delta proposal，runtime 绑定 receiver architecture、base weights、rank 和生命周期，调用结束即撤销，不能把瞬态权重当成已发布模型。

这种通道减少 token 与部分延迟，却增加不可解释状态、接收者强耦合、训练成本和错误 delta 的广泛影响；receiver 升级、跨供应商协作或需要人工审计时，结构化文本/typed message 仍更可靠。exact-v1 的五个 benchmark 只证明披露配置下的竞争性结果，不证明 latent/weight communication 普遍优于文本、具备安全隔离或可跨模型迁移。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-13839 -->

### 大规模协商必须把 Routing、Identity 与 Commitment 分权

小组内直接传消息在成员和权限固定时足够；参与者扩大后，directory/routing、user identity、negotiation state 和最终 agreement 若混成一层，Agent 会把结构化 offer 误当成代表用户的承诺。exchange 只管理寻址和协议状态，Agent 只提出 offer，用户或授权 policy 保留 commit authority。分权增加目录一致性、认证、消息排序和长事务恢复成本；身份或偏好证据不足时，应回退小组 coordinator、显式 approval 与确定性协商规则。现有 protocol 证据不赋予消息真实 consent，也不证明开放人口规模下的安全性。

<!-- semantic-body-binding:SF-LLM-X-A-SCALABLE-NEGOTIATION-ORIENTED-EXCHANGE-FOR-COMMUNICATION-AMONG-P -->

### Delegation Depth 要同时结算 Root Exposure 与 Handoff Yield

多层 decomposition 可以降低敏感 root state 暴露，却让任务信息在每次 handoff 中损失，并增加 token、latency 与 coordination cost。Topology controller 应用 measured retention、coordination loss、root exposure 与 equal-budget threshold 共同选择深度；完整性风险高时可接受较低 yield，产出率优先且约束弱时 flat/single-agent 仍是默认。<!-- source-family:SF-2026-ARXIV-2609-17464 -->

600 条 production traces、16,082 hops 与 1,012 annotations 的拟合依赖数据选择和定义，不能当普遍因果律。handoff retention 无法稳定估计时，应减少层级并增加显式 verification，而不是继续扩展组织图。

### Supervisor 只有拥有独立 Verifier 时才值得取得 Loop-back Authority

层级 Agent 常让 manager 评论、reject 或要求 revision；若它不能执行独立、可判定的检查，这个 loop 只会增加 token、延迟与 correlated judgment。Topology admission 应先证明 manager 拥有 verifier、合规审批或可检查答案，再授予 reject/revision authority；只能发表意见时，flat/single-agent 是默认 fallback。<!-- source-family:SF-2026-ARXIV-2609-14767 -->

独立验证提高控制力，也会增加重复执行和协调成本。单一 business-intelligence 任务、43 pairs/86 runs 与 judge 偏差不足以证明层级普遍有害；强 verifier 或高风险审批存在时，hierarchy 仍然合理。

### 共享控制变量只能有一个 Commit Arbiter

两个各自正确的 Agent 若同时读取并提交同一控制变量，也可能形成任何单体都不会产生的 recurrent excursion。安全拓扑应把各 Agent 降为 proposal producer，由唯一 arbiter 检查 shared-state feasibility invariant、per-variable dwell 与 deadband，再提交 transition，并记录 proposal、rejection reason 与 committed state。<!-- source-family:SF-2026-ARXIV-2609-18857 -->

Arbitration 用响应速度换稳定性：dwell/deadband 过强会迟滞，过弱仍会振荡，单变量 proposal 也无法表达耦合动作。O-RAN testbed 与特定 proof 不证明同一参数适合所有领域，且冲突下降未改善 protected slice 自身 latency compliance；无法表达或收敛时，应回退 composite coordinator、serial execution、人工控制与 last-known-safe state。

## Review notes

- `SF-2026-ARXIV-2602-21515`：[v1 Eq.8–9 / 受限 partner 与任务对照](https://arxiv.org/html/2602.21515v1)。训练辅助 adversary 对 evolving partner 的 KL 邻域，不是身份/授权或普遍鲁棒保证；Tag 训练下降、GSM 共同正确与异质 partner 人口差异保留。非原 packet 作者必要原证/owner PRE 完成；root已实际顺读正文、完整邻接与自身末注，POST通过，未复现。

- `SF-2026-ARXIV-2602-16485` — Daily `2026-02-20`；[Team of Thoughts exact-v1](https://arxiv.org/html/2602.16485v1) §3/4.1–4.3。2+1+2=5，worker-solving/coordinator-aggregation角色离线校准差额定点深入；GT自评非online confidence，美元预算非同token，profile/不确定性与漂移反侧相邻。不采Pareto/独立先验或性能普遍保证，未核实现或复现；root必要原源/actual owner PRE通过，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放，非日级Gate。

- `SF-2026-ARXIV-2601-09883` — Daily `2026-01-17`；[CORAL exact-v1](https://arxiv.org/html/2601.09883v1) §3、§4.1–4.4/Table2及§5；2+2+2=6，标准必要审阅后具体 owner 差额深入。仅采用 coarse success flag 与 global semantic obligation 分开核验、局部 instruction refinement 而非自动重跑的协调分支；全强配置平局、异构 worker 条件、token 增量与角色/提示未完全匹配保留，不授统一 topology 优势、权限或 effect gate。root 必要源与具体 owner 写前核验通过；root实际正文/前后邻接与此注非作者POST通过，窄锁释放；未复现实验。

- `SF-2026-ARXIV-2602-05176` — Daily `2026-02-07`；[Among Us exact-v1](https://arxiv.org/html/2602.05176v1) §2.1–2.3、攻击/缓解反侧。3+2+2=7，深入仅采攻击控制权分层与matched benign独立outcome人口；5 Qwen7B benign+1恶意/A10040G、parametric兼容限制及部分攻击quality高于benign保留，不授通用防御/意图真值/生产Byzantine。root实际必要源/owner写前通过，正文/邻接及末注root实际非作者POST通过；未运行攻击或复现。

- `SF-2026-ARXIV-2601-05593` — Daily `2026-01-13`；[PaCoRe exact-v1](https://arxiv.org/html/2601.05593v1) §2 conclusion-only compaction、synthesis/filter训练与§3受限评价。消息仍受窗口约束，不授多数纠错、faithful trace 或 wall-clock 保证。未复现；root 必要源/当前owner写前通过，root实际新增正文/前后衔接及末注写后复核通过。

- `SF-2026-ARXIV-2603-00349`：[EmCoop exact-v1](https://arxiv.org/html/2603.00349v1) §3/§5/§6–7；Daily 2026-03-04，2+2+2=6。采用 cognitive/environment 双时钟与可观察约束归因，保留 all-ready joint primitive barrier、有限环境/模型/拓扑和单例 intervention 边界；不采真实全异步、免费通信或统一拓扑优势。作者必要源→owner与相邻 Workflow/MCP 交接实际检查，root非作者必要源→实际正文/邻接POST通过；未复现实验。

- `SF-2026-ARXIV-2604-13349`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13349v1) §4.3 Eq3–9/§5 Table1。sender-local prompt V 的 retained-span残差、PCA/attention-demand摘要及统一backfill，K不变；非receiver translator/无损保证。Qwen3-14B/40latentsteps/BF16/单PRO6000、rank8、H/L退步与原矩阵/QR/SVD成本保留。root必要来源/实际owner采用通过，实际正文待写后非作者复核，未复现实验。
- `SF-2026-ARXIV-2604-07911`：[DACS exact-v1 PDF](https://arxiv.org/pdf/2604.07911v1) §3.1–3.5、§6/7.4。采用registry/focus的working-view分支和保存/恢复steering，不采用权限隔离、global sublinear、任意context总可满足硬预算或绝对零污染。160 scripted+40真实trial，真实Haiku4.5/N3或5/低决策密度；interrupt未单独消融、ID引用指标歧义保留。2+2+2=6、知识缺口深入，root必要原文及实际写后非作者核验通过，未运行实现。

- `SF-2026-ARXIV-2604-06452`（Experimental）：[exact-v1](https://arxiv.org/html/2604.06452v1) §2.1–2.2、§3.2、§4.1–4.4、C.2/C.4–C.6。固定chunk/one-token decision与后续tree rollout是不同成本；主实验100 pictionary、50 synthetic scheduling、100 MMLU-Pro seeds、Llama8/70 listener、三speaker、三trials、temperature0.7。correct/incorrect debate positions为生成的特权初始信息；不外推32.2%或token代理到生产SLO，C.6不一致chunk不等式不采用。未复现；root已独立核必要原文、实际接收方控制三段及通信预算/latent交接，该窄命题写后通过，不代表日级Gate。

- [Retrieval-Conditioned Topology Selection](https://arxiv.org/html/2605.05657v1)（Status: Experimental）：预算守恒证明依赖 deterministic cost、有限 action space 与有界 retrieval depth；随机生产成本仍需 runtime accounting。

- **Epistemic Sybil Resistance（arXiv:2609.01873v1；理论部分的受限解释）**：
  [exact-v1](https://arxiv.org/html/2609.01873v1) §5 支持指定 Gaussian 模型下的同根提取收益边界，§6 讨论
  provenance 与参数知识条件。正文不采用其自然语言置信度估计器、生产安全或普遍性能结论。独立审读发现
  §4.2 的二元 posterior 构造需额外对称误差条件，§8.3 与 Figure 4 的 naive NLL 不一致；后者保持 Disputed，
  未进入本章。代码与冻结输出尚待作者公开；本次没有独立复现实验。

- **Ledger-State Stigmergy（arXiv:2604.03997v1；Status: Experimental）**：exact-v1 支持以 durable ledger state 表达间接 coordination 的形式语义；没有披露可跨 workload 复算的生产吞吐、容错或长期运行证明。https://arxiv.org/abs/2604.03997v1

- PILOT（live supervisor control 与 persistent harness promotion；Status: Experimental）：
  https://arxiv.org/abs/2608.26530v1
  - 证据边界：论文支持作者环境中的在线 redirect/abort 与轨迹固化；不证明弱 supervisor、开放工具环境或
    跨任务长期采用仍安全有效。

- MARS-RA（arXiv:2607.27967v1；Status: Experimental）：https://arxiv.org/html/2607.27967v1
  - 证据边界：exact-v1 支持以 pairwise multimodal judgments、rank aggregation 和 potential shaping 改善作者 multi-agent tasks；不证明排名是 causal contribution，且 position bias、judge error、hidden physical state 与 non-stationarity 仍在边界外。

- Two-Tier Inference-Time Parallelism（replica vs workflow structural parallelism；受限 GAIA 实验）: https://arxiv.org/abs/2608.05791
- E2-Explainer（communication-edge attribution 与 topology distillation；Status: Experimental）: https://arxiv.org/abs/2608.12921
- MACE（uncertainty-aware peer exploration；Status: Experimental）:
  https://arxiv.org/abs/2607.11250v1

本章把 AutoGen/CAMEL 作为多 Agent interaction 的研究入口，不把 framework API 当作系统原理。与第 81 章分责：Workflow 拥有状态，Agents 拥有受限决策角色。

Primary-source 入口：

- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- Generative Agents: https://arxiv.org/abs/2304.03442
- Towards a Science of Scaling Agent Systems: https://arxiv.org/abs/2512.08296
- MANTA（Status: Experimental；trace-triggered bounded topology repair）:
  https://arxiv.org/abs/2607.28527
- CooperBench（shared-repository coordination failure evidence；不构成 Agent 能力上限）:
  https://arxiv.org/abs/2601.13295
- Kimi K2.5 / PARL（learned orchestrator + frozen subagents；作者系统边界）: https://arxiv.org/abs/2602.02276
- WideSeek / WideSeek-R1（dynamic fan-out 与 count-normalized MARL；Status: Experimental）:
  https://arxiv.org/abs/2602.02636
  https://arxiv.org/abs/2602.04634
- AOrchestra（runtime-instantiated executor contract；Status: Experimental）: https://arxiv.org/abs/2602.03786
- Vision Wormhole（heterogeneous latent communication；Status: Experimental）:
  https://arxiv.org/abs/2602.15382
- XKV / Dual-Cache Latent Space Communication（receiver-conditioned joint cache translation；Status: Experimental）:
  https://arxiv.org/abs/2608.20617
- StateBridge（training-free hidden-state alignment；Status: Experimental）:
  https://arxiv.org/abs/2608.13317
- In-context co-player inference（behavioral adaptation 与 strategic shaping；Status: Experimental）:
  https://arxiv.org/abs/2602.16301
- AgentDropoutV2（failure-memory-conditioned message rectify/reject；Status: Experimental）:
  https://arxiv.org/abs/2602.23258
- CAID（branch-and-merge ownership；Status: Experimental）: https://arxiv.org/abs/2603.21489
- Emergent Social Intelligence Risks（collective-risk contract；Status: Experimental）:
  https://arxiv.org/abs/2603.27771

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-27409` — Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement; primary=`arXiv:2606.27409v2`; Method=`arXiv:2606.27409v2 — §3 Model; §4 Stability and the verification dose; §5 Corrector placement for coherence objective; §6 Two coupled delays`; Evaluation=`arXiv:2606.27409v2 — §7.1 Synthetic onset; §7.2 Grounded factual debate: protocol-dependent outcomes; §7.2.1 Expanded factual study with complete response logs; §7.3 Externally controlled signed-error variability`; counterevidence/non-proof locator=`arXiv:2606.27409v2 — §8 Discussion; §9 Limitations; §10 Conclusion`; claim boundary=振荡阈值只属于受控 signed-belief dynamics；400-question factual study 因大量 abstention 而使 conservative completion bounds 同时允许两种变化方向，未识别或证实自然 factual verification 具有同类振荡，也未证明 truth absorbing boundary。对称图、局部线性分析、selected factual samples 与 surrogate placement 不证明任意 topology、Byzantine agent 或非平稳 communication graph 的稳定性。; fallback=delay/graph/completion identity 未知时序列化关键提交、单独报告 abstention，并使用 deterministic verification。

### Daily integration evidence trace

- `2026-05-02 / SF-TEAMTR-MULTIAGENT-OCCUPANCY-SHIFT` — exact-v1 `arXiv:2605.15207v1`；正文吸收 sequential update 后 joint occupancy 失配与重采样/trust-region Gate，不把单 Agent loss 当团队结论。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24437: `arXiv:2606.24437v1`; exact-v1 URL=`https://arxiv.org/html/2606.24437v1`; Method=`https://arxiv.org/html/2606.24437v1 — §4 ReM-MoA; Ranked Reasoning Memory; Diversified Routing`; Evaluation=`https://arxiv.org/html/2606.24437v1 — §5 Experiments; Scaling and Ablations`; Non-proof=`只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-26156: `arXiv:2606.26156v1`; exact-v1 URL=`https://arxiv.org/html/2606.26156v1`; Method=`https://arxiv.org/html/2606.26156v1 — §2 Information Protocols; 3 Kiko Programming Model`; Evaluation=`https://arxiv.org/html/2606.26156v1 — §4 Operational Semantics; protocol-compliance proof`; Non-proof=`2023 AAMAS programming model与语义证明不包含 LLM nondeterminism、tool side effect、Byzantine peer 或大规模 runtime benchmark；不兼容时回退显式 typed state machine。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25514**：Primary `arXiv:2606.25514v1`；Method `https://arxiv.org/html/2606.25514v1 — §2 Adaptive Multi-Agent Issue Resolution; 2.6 Event-Driven Synchronous Communication`；Evaluation `https://arxiv.org/html/2606.25514v1 — §3 Evaluation; 3.2 Analysis of Exclusive Fixes and Failures`；未证明边界 `https://arxiv.org/html/2606.25514v1 — §5 Threats to Validity`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29270`；Method `https://arxiv.org/html/2606.29270v1 — §3 Our Method; 3.3 The Debate Fingerprint; 3.4 Cure Phase: Meta-Classifier and Threshold Strategy`；Evaluation `https://arxiv.org/html/2606.29270v1 — §4 Experiments and Results; 4.1 Datasets and Debate Configuration; 5.5 Multi-Seed Stability`；未证明边界 `https://arxiv.org/html/2606.29270v1 — §6.2 Limitations`。

Review note：`SF-2026-ARXIV-2606-29601`；Method `https://arxiv.org/html/2606.29601v1 — §Approach; sayso, nono and nogo protocol semantics`；Evaluation `https://arxiv.org/html/2606.29601v1 — §6.2 Empirical Results; safety and liveness procedures`；未证明边界 `https://arxiv.org/html/2606.29601v1 — §7 Discussion: Conclusion and Perspectives`。

Review note：`SF-2026-ARXIV-2606-29654`；Method `https://arxiv.org/html/2606.29654v1 — §3 Method; Offline: calibration; Online: k-NN lookup; Stopping rule`；Evaluation `https://arxiv.org/html/2606.29654v1 — §6 Experiments; Benchmarks; Difficulty-normalized deployment budgets; 6.1 Main results`；未证明边界 `https://arxiv.org/html/2606.29654v1 — §7 Discussion and Limitations; H Detailed Assumption Diagnostics; N Failure-case decomposition`。

<!-- june29-owner:AGENT-MULTI-AGENT:start -->
### 2026-06-29 来源范围补记

- `SF-2026-ARXIV-2606-29270`：三异构 Agent、两轮、六 benchmark 的 debate-log classifier；既有记录报告 81.2% Flip Precision，不是无错误或安全保证，共享训练、换模型与换协议均可能破坏校准。
- `SF-2026-ARXIV-2606-29601`：有限 Langshaw examples 到 BSPL tableau 的 safety/liveness 与编译时间；未证明开放网络 delivery、identity、Byzantine role 或工具副作用。
- `SF-2026-ARXIV-2606-29654`：保证依赖 local bias envelope、representation-gap bound 与 calibration split，并非 distribution-free；六个选择题 benchmark 与训练期 difficulty-normalized budget 不覆盖开放式任务或分布漂移。三项的原文定位见上方 source-specific Review notes。

<!-- june29-owner:AGENT-MULTI-AGENT:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-DELIBERATION-EVIDENCE-ATTRITION:start -->
- `SF-DELIBERATION-EVIDENCE-ATTRITION` — Daily `2026-06-03`；primary `arXiv:2606.03032v1`；Books review `books-review:SF-DELIBERATION-EVIDENCE-ATTRITION`。

  **已吸收的语义增量：** We formalize deliberation as an information-flow setting, where a factual background is (1) partially distributed across agents, (2) exchanged through discussion, and (3) evaluated by what survives after interaction. A deliberation object ℐ \mathcal{I} is defined as ℐ = ( ℬ , q ) \mathcal{I}=(\mathcal{B},q) , where ℬ \mathcal{B} denotes the background context and q q denotes the focal issue query. We represent ℬ \mathcal{B} as a set of atomic facts: ℬ = { c 1 , c 2 , … , c m } \mathcal{B}=\{c_{1},c_{2},\dots,c_{m}\} , where each c j c_{j} is a self-contained factual unit. Boundary: where π i \pi_{i} is the underlying LLM, ℬ i ⊆ ℬ \mathcal{B}_{i}\subseteq\mathcal{B} is the agent’s partial evidence, and θ i ∈ { Yes , No } \theta_{i}\in\{\textsc{Yes},\textsc{No}\} is the agent’s prior stance. Perspective selection details are provided in Appendix B.2 . This initialization creates a controlled abstraction of deliberative disagreement.
<!-- daily-books-trace:SF-DELIBERATION-EVIDENCE-ATTRITION:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-05304:start -->
- `SF-2026-ARXIV-2606-05304` — Daily `2026-06-04`；primary `arXiv:2606.05304v1`；Books review `books-review:SF-2026-ARXIV-2606-05304`。

  **已吸收的语义增量：** PACT 把每次 agent output 投影为 public action-state record，再写入 shared history。private reasoning 归各 agent，action/state delta 是公共数据，projection policy 掌握跨 agent 暴露控制。
<!-- daily-books-trace:SF-2026-ARXIV-2606-05304:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07790:start -->
- `SF-2026-ARXIV-2606-07790` — Daily `2026-06-06`；primary `arXiv:2606.07790v1`；Books review `books-review:SF-2026-ARXIV-2606-07790`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07790:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07805:start -->
- `SF-2026-ARXIV-2606-07805` — Daily `2026-06-06`；primary `arXiv:2606.07805v1`；Books review `books-review:SF-2026-ARXIV-2606-07805`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07805:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13733:start -->
- `SF-2026-ARXIV-2606-13733` — Daily `2026-06-12`；primary `arXiv:2606.13733v1`；Books review `books-review:SF-2026-ARXIV-2606-13733`。

  **已吸收的语义增量：** MAS topology必须服从任务constraint graph；bounded communication下 minimum-cut information bottleneck 可决定应重构任务而非增加 agents/messages
<!-- daily-books-trace:SF-2026-ARXIV-2606-13733:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14200:start -->
- `SF-2026-ARXIV-2606-14200` — Daily `2026-06-13`；primary `arXiv:2606.14200v1`；Books review `books-review:SF-2026-ARXIV-2606-14200`。

  **已吸收的语义增量：** Agent reputation 必须按 skill 条件化并记录 zero-evidence state；global trust 会让攻击者用无关技能的良性行为 laundering 后取得高风险任务 routing authority。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14200:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15376:start -->
- `SF-2026-ARXIV-2606-15376` — Daily `2026-06-14`；primary `arXiv:2606.15376v1`；Books review `books-review:SF-2026-ARXIV-2606-15376`。

  **已吸收的语义增量：** 多 Agent 共享对象可用 Monotonic Trajectory Pre-Order：固定读序、speculative write、通知与可逆三阶段 tool call，在 quiescence 达到 serializable outcome。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15376:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16710:start -->
- `SF-2026-ARXIV-2606-16710` — Daily `2026-06-16`；primary `arXiv:2606.16710v1`；Books review `books-review:SF-2026-ARXIV-2606-16710`。

  **已吸收的语义增量：** benign MAS 也会传播 tool/context misinformation；coordinator 应追踪 claim provenance、独立复核与多数意见的相关性
<!-- daily-books-trace:SF-2026-ARXIV-2606-16710:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17182:start -->
- `SF-2026-ARXIV-2606-17182` — Daily `2026-06-16`；primary `arXiv:2606.17182v1`；Books review `books-review:SF-2026-ARXIV-2606-17182`。

  **已吸收的语义增量：** 并发 MAS 需要显式 happens-before、shared-state conflict 与 side-effect serialization，并在运行前后验证 anomaly-free execution
<!-- daily-books-trace:SF-2026-ARXIV-2606-17182:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20701:start -->
- `SF-2026-ARXIV-2606-20701` — Daily `2026-06-16`；primary `arXiv:2606.20701v1`；Books review `books-review:SF-2026-ARXIV-2606-20701`。

  **已吸收的语义增量：** learned-communication MARL 必须识别 Byzantine message 并让 trust state 随 evidence 更新，不能假设 peer channel 全部诚实
<!-- daily-books-trace:SF-2026-ARXIV-2606-20701:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18121:start -->
- `SF-2026-ARXIV-2606-18121` — Daily `2026-06-17`；primary `arXiv:2606.18121v1`；Books review `books-review:SF-2026-ARXIV-2606-18121`。

  **已吸收的语义增量：** 多 Agent reliability 需把 proposer abstention、verifier abstention 与 message loss 作为不可互换的 factor-graph channels，并审计 certificate-stopping set 而非只扩 agent 数。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18121:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19758:start -->
- `SF-2026-ARXIV-2606-19758` — Daily `2026-06-19`；primary `arXiv:2606.19758v1`；Books review `books-review:SF-2026-ARXIV-2606-19758`。

  **已吸收的语义增量：** `SIGMA: Skill-Incidence Graphs for Compositional Multi-Agent Design` 路由到 `AGENT-MULTI-AGENT`：SIGMA 不把 agent node 当封闭角色，而由任务到 skill-agent incidence matrix 组合节点，再解码通信图；skill mailbox 拥有消息路由，缺 skill 或组合退化时回落到预定义 agent/topology。代价是库质量、组合搜索和 mailbox 隔离成为新的控制面。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19758:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20493:start -->
- `SF-2026-ARXIV-2606-20493` — Daily `2026-06-19`；primary `arXiv:2606.20493v1`；Books review `books-review:SF-2026-ARXIV-2606-20493`。

  **已吸收的语义增量：** `Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems` 路由到 `AGENT-MULTI-AGENT`：它把 evaluator preference 看作多-agent 图上的传播状态，要求 evaluation owner 跟踪 judge influence/依赖，而非把 agent votes 当独立样本；检测到 contagion 时使用隔离 judge 或独立 anchor。代价是图估计与额外评审成本。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20493:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21228:start -->
- `SF-2026-ARXIV-2606-21228` — Daily `2026-06-20`；primary `arXiv:2606.21228v1`；Books review `books-review:SF-2026-ARXIV-2606-21228`。

  **已吸收的语义增量：** 多 Agent 系统可用分层 coordinator 与 specialist swarms 扩展任务，但 dispatch、shared artifact 与 verification ownership 不能藏在聊天拓扑中
<!-- daily-books-trace:SF-2026-ARXIV-2606-21228:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22203:start -->
- `SF-2026-ARXIV-2606-22203` — Daily `2026-06-21`；primary `arXiv:2606.22203v1`；Books review `books-review:SF-2026-ARXIV-2606-22203`。

  **已吸收的语义增量：** 先用 counterfactual neighbor perturbation 测 coupling gain，再以 target-interaction modality-matched group coupling 选择 consensus dynamics；随机初值 slope/bias 区分 genuine averaging 与 model prior。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22203:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11250:start -->
- `SF-2026-ARXIV-2607-11250` — Daily `2026-07-14`；primary `arXiv:2607.11250v1`；Books review `books-review:SF-2026-ARXIV-2607-11250`。

  **已吸收的语义增量：** 新增证据边界：MACE casts each agent’s peer choice as an independent contextual bandit and applies relational features plus LinUCB optimism so uncertain but potentially complementary peers are explored. 该 delta 已进入 `books/part-07-agent/82-multi-agent.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11250:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27967:start -->
- `SF-2026-ARXIV-2607-27967` — Daily `2026-07-31`；primary `arXiv:2607.27967v1`；Books review `books-review:SF-2026-ARXIV-2607-27967`。

  **已吸收的语义增量：** 新增证据边界：LMM pairwise comparisons form a matrix; rank aggregation yields contribution credits; potential shaping feeds MAPPO. 该 delta 已进入 `books/part-07-agent/82-multi-agent.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27967:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-05791:start -->
- `SF-2026-ARXIV-2608-05791` — Daily `2026-08-07`；primary `arXiv:2608.05791v1`；Books review `books-review:SF-2026-ARXIV-2608-05791`。

  **已吸收的语义增量：** 论文把多 Agent 并行拆成 replica parallelism 与 workflow structural parallelism：前者复制独立样本，后者利用依赖图内并行。GAIA 范围实验显示两者受不同 critical path 限制；协作语义和工具副作用使它不能简化为增加并发数。
<!-- daily-books-trace:SF-2026-ARXIV-2608-05791:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-12921:start -->
- `SF-2026-ARXIV-2608-12921` — Daily `2026-08-14`；primary `arXiv:2608.12921v1`；Books review `books-review:SF-2026-ARXIV-2608-12921`。

  **已吸收的语义增量：** E2-Explainer 用 Granger-style edge masking 估计 communication channel 对任务结果和 final-response stability 的因果贡献，再把 budgeted subgraph 蒸馏为 amortized explainer。它可用来删减冗余通信，但 post-hoc attribution、mask distribution shift 与协作任务代表性限制了因果解释的强度。
<!-- daily-books-trace:SF-2026-ARXIV-2608-12921:end -->

<!-- daily-books-trace:SF-2026-PILOT-LIVE:start -->
- `SF-2026-PILOT-LIVE` — Daily `2026-08-28`；primary `arXiv:2608.26530v1`；Books review `books-review:SF-2026-PILOT-LIVE`。

  **已吸收的语义增量：** 补足当前 run 控制与未来能力收录的状态分离。
<!-- daily-books-trace:SF-2026-PILOT-LIVE:end -->

- `SF-2026-ARXIV-2604-15558` — Daily `2026-04-20`；primary [PBRC v1](https://arxiv.org/html/2604.15558v1)；7分必要深入。新增 finite external belief-state 的 evidence admissibility/operator enforcement 分责与 social-only 非放大分支；不证明内部信念/真值或所有拓扑。root 必要源→实际owner采用及实际正文/相邻写后复核通过。n3000 paired GPT4o示例中273有益 flips同样被挡，认证非语义真值，保留活性损失。采用依据见 `papers/2026/04/_sources/daily-20260420/V3_PBRC_FACT_OWNER_PROPOSALS.md`。

- `SF-2026-ARXIV-2602-03053` — Daily `2026-02-05`；[MASProVe exact-v1](https://arxiv.org/html/2602.03053v1) §4.2–4.4必要实验。原2+2+2=6，具体gap深入仅采用verification granularity×judge view联合校准；六MAS/GPT5mini/三branch是有限条件。Posthoc BestConfiguration/不同cost、摘要与raw history反侧保留，0/30或0/3不授理论不可能/能力天花板，未复现。root已实际核必要源/owner及118行正文/111–123邻接与末注，POST通过；日级Gate待验。

- `SF-2026-ARXIV-2602-04837` — Daily `2026-02-06`；[Group-Evolving Agents exact-v1](https://arxiv.org/html/2602.04837v1) 必要机制、评测流程与成本反侧。原2+2+2=6，具体group experience/code artifact/member verification gap深入；各成员继承经验并改各自code，不等共享代码自动merge。相同child数不等全cost匹配，sanity/小集筛选/full-evaluator人口分开；不采普遍胜利或无成本协作。identity/archive guard为工程推导，不称原实验已验证；未运行代码/复现。jan01_v3实际必要原源/owner写前通过，root授窄锁；root实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2601-08003` — Daily `2026-01-15`；[LLM Peer Review exact-v1](https://arxiv.org/html/2601.08003v1) §3.5、§5.1–5.3与Limitations。2+2+2=6，具体owner缺口深入；初稿/反馈可见而修订稿不共享，非完全盲；人数/轮数可退步，单Agent调用不等、少量人工/同源judge与反馈修订成本近正文。未运行代码或复现；root实际必要源与具体owner写前核通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2601-09434` — Daily `2026-01-16`；[SCMAS exact-v1](https://arxiv.org/html/2601.09434v1) §3、4.2–4.3及5.3/C2。2+2+2=6，edge-policy具体gap深入；节点、边存在、协议与backbone身份分离，DAG不证明内部while终止，runtime bounds为工程职责而非作者实现。随机组件/训练及全调用成本边界相邻；不采未完整定义的概率公式为精确recipe，未运行代码或复现。root实际必要源/owner写前通过，root实际正文188/190、176–203前后及末注1273非作者POST通过，窄锁释放，非日级验收。

- `SF-2026-ARXIV-2602-09341` — Daily `2026-02-12`；[AgentAuditor exact-v1](https://arxiv.org/html/2602.09341v1) §4.1–4.3、5.1–5.3、6.1–6.6/Table1–5、7/B.1。2+2+2=6，具体 minority-override 接口缺口深入；只采用 CDP local-branch packets 与 GT trap-population preference，support cues、majority-correct反退、未校准 confidence 与 audit-only cost 限制邻近，不授97%共识安全或DPO新目标。root 必要 source→owner 写前通过，实际两段/完整邻接/本末注非作者 POST 通过，窄锁释放；未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-09173` — Daily `2026-02-12`；[exact-v1](https://arxiv.org/pdf/2602.09173v1) §3–4/6 fixed-v1 PDF。具体 owner 差额受影响深入：frozen expert forward→Perceiver softprefix→policy；非动态分工因果，无decode仍全部forward。root 必要原源/具体 owner 写前通过并授窄锁；root 已实际顺读两段、完整邻接与本末注，非作者 POST 通过，窄锁释放。未核代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16891` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16891v1) §3.2–3.4/§4/C3。2+2+2=6，metadata/clone/archive生命周期差额定点深入；不采first/superiority、联合消融因果或Docker/graph安全保证。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接/末注已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放，未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-17100` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17100v1) §2.1/Eq1–7、§2.2–3/T3–4/A1–3。2+2+2=6，graph-as-policy / execution-feedback history 差额深入；schema非正确性、density非墙钟、teacher措辞冲突和训练/worker费用近正文，不授安全或最优拓扑。root必要原源/actual owner PRE通过并授一段/自身末注窄锁；作者实际正文及完整邻接已读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-16662` — Daily `2026-02-20`；[exact-v1](https://arxiv.org/html/2602.16662v1) §4固定策略、§5 self-play、§6 culture与§7直接限制。2+2+2=6，离线策略 population/selection operator 测量身份差额深入；编译筛选偏差、有限游戏与模仿超参、模拟费用/实际环境旧路径近正文。不授现实预测或合作安全；root必要源/actual owner PRE通过并授窄锁，作者正文/完整邻接实际顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未运行实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17203` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17203v1) §3.2–3.3/§4.4–4.4.1/Table4。2+1+2=5，initial history×test-time adaptation 的 meta-game 测量人口差额深入；有限6配置/4价格/40初态/t50、uniform收益与NE-regret分账、API与收益估计费用、旧模型不可复现近正文，不授现实 collusion/安全合作保证。root必要source/actual owner PRE通过并授窄锁，作者实际正文/完整邻接已读，root 非作者实际正文/完整邻接及末注 POST通过，窄锁释放，未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22124` — Daily `2026-02-27`；[exact-v1](https://arxiv.org/html/2602.22124v1) §2–4/Table2–4，2+2+2=6；具体owner差额深入：如何/何时/后续使用专家建议；hardnocall偏置、loop上下文反侧、gold只离线、共享judge与全部费用/单Agent回退近正文。root必要原源/actual owner PRE通过并授窄lease；作者及root非作者已实际顺读正文/完整邻接/自身末注，POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22808` — Daily `2026-02-28`；exact-v1必要blocks26–50/52–56/61–79，2+1+2=5；peripheral processor与主体协作分账具体差额深入。final_audit非原packet作者必要原源/actual owner PRE通过，当前作者复用未变证据并实际读目标近邻，root授窄锁；正文/完整邻接及自身末注已实际顺读，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放，未核实现/复现，非日级Gate。
