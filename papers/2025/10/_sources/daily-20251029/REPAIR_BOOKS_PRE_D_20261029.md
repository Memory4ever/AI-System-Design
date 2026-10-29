# D4整体PRE · 2025-10-29

仅R40四项实际长期差额。Writer已逐项自读下列完整正文/独立marker/本人注及磁盘实际完整必要两肩；未SAVE，申请sole整体PRE，不以marker替正文或授全章。

## 22993 · books/part-07-agent/74-prompt.md

### 完整新增

示例还可能只监督单个skill，而目标要求未知的skill组合；此时多给单skill示例不保证能辨识组合接口，甚至会把学习规则推向错误组合。可将单步identity显式交给learner，分别检验单skill准确率与未见组合的结果。[受限skill-composition分析](https://arxiv.org/html/2510.22993v1)在有限假设类、特定分布可辨识与存在学习规则的条件下给出这种区别，不证明真实Transformer会执行该规则，也不把某个logarithmic示例关系搬成通用ICL定律。小模型对照仍受任务与训练人口限制，step提示还改变输入信息和长度；示例制备、结构标注、组合验证与完整推理均付费。组合identity不可得、语义或净收益不稳时，保留少量完整任务示例、原选择器与独立终局核验，不从单skill学会或更多examples批准任意组合能力。
<!-- source-family:SF-2025-ARXIV-2510-22993 -->

### 本人注

- `SF-2025-ARXIV-2510-22993`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40实际gap补单skill监督与组合接口可辨识性，不重复已有示例数量/主题互补/teaching utility；理论权限不外推真实模型。

### 自读判断

按R40实际gap补单skill监督与组合接口可辨识性，不重复已有示例数量/主题互补/teaching utility；理论权限不外推真实模型。

### 实际前肩

示例数量也应作为待验预算，而不是越多越好的容量旋钮：在同一模型、标签协议与选择方法下，分别比较少量和更多示例的任务结果，并把宏平均与按类频率加权的指标分开。[受限需求分类对照](https://arxiv.org/html/2509.13196v1#S4)中，部分模型随示例增加而退步，另一些模型或指标仍改善，因此不能把某个最优数量、8B门槛或TF-IDF选择推广成通用规则。示例检索、数量搜索和更长输入都付费；转折点、标签或模型版本改变时，重新做独立回归，保留短固定示例与原选择器，不用更多上下文代替目标任务验收。
<!-- source-family:SF-2025-ARXIV-2509-13196 -->

固定示例数之后，还要决定几条示例是否提供互补信息，而不只分别像当前query。一条[受限主题覆盖分支](https://arxiv.org/html/2509.12451v1#S3)先为训练候选标主题并学习覆盖预测器，再用有标签候选上的zero-shot正确率形成模型知识proxy，逐次选择能补当前主题缺口的示例；这让标签制备、候选池和模型版本成为选择器身份。预测topic不是完整语义集合，正确率加权也不是内部知识真值，累计mean-embedding的增量不保证非负，知识为零时的归一化更不能默补成可靠规则。应以独立任务结果验收选择而非只看coverage分数，并计GPT标注、全池zero-shot、预测器训练、超参搜索与最终输入费用；有限分类对照中的检索阶段提速不代表全链更便宜。主题代理、模型版本或任务回归失配时，保留相似检索、随机/固定示例和较短prompt，不以覆盖更广替代真实答案验收。
<!-- source-family:SF-2025-ARXIV-2509-12451 -->

示例本题答对，还不等它适合教下一题。可以先让同一批候选轨迹分别作为其他题的示例，以后续解题效用选择可复用轨迹，而不只按原题reward排序。[CodeAdapt的受限分支](https://arxiv.org/html/2510.20909v1#S3)因此把单题正确、跨题teaching utility和最终任务质量分开；相同base但不同版本的生成器与learner不构成完全同模型对照，数学切片也存在原reward排序更好。效用依赖下游任务人口、示例顺序与consumer版本，不能固化为轨迹本身的永久质量。全候选/失败重试、跨题验证、工具和最终prompt都计费；少输出token不等整条选择更便宜。跨题收益或全费不稳时，保留原题reward、固定少量示例、相似检索与独立答案verifier，不由正确轨迹批准通用教学价值。

<!-- source-family:SF-2025-ARXIV-2510-20909 -->

### 实际后肩

**Schema** 缩小可接受输出空间。JSON Schema、grammar 或 enum constrained decoding 能保证部分句法，却不能保证字段事实正确、参数被授权或业务操作安全。

一个稳健接口将三者分离，并在模型外验证：

```text
model output
→ parse
→ schema validation
→ semantic/business validation
→ authorization
→ execution or rejection
```

## Chain of Thought 的边界

Chain-of-Thought demonstrations 在特定模型和任务上可改善多步推理，这是经验结论，不是模型一定暴露真实内部因果过程的证明。

生产系统更应关心可验证 intermediate state：计划节点、tool arguments、retrieved evidence、test result。隐藏或压缩自由文本 reasoning，可以降低泄露、成本和脆弱依赖；不能把一段流畅解释当作正确性证据。

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-20909`：Daily2025-10-28补Oct27；exact-v1§3–4/限制必要、2+1+2=5，R14受限Evidence通过。仅跨题示例utility与本题reward分责，保跨版本/AIME反侧与全部候选验证费，不采普遍省时或正确教学保证；未核实现/复现。完整PRE/SAVE/全自读/sole actualPOST按同日canonical实际层，不预签。

## 23487 · books/part-07-agent/81-workflow.md

### 完整新增

上下文组织还决定能用哪一种理想计算模型描述workflow。固定有限alphabet与常量大小的可辨状态，可抽象为finite automaton；严格LIFO且frame alphabet有限的递归记忆，可对应pushdown automaton；只有理想无界且可反复读写的memory才进入Turing-machine层级。[受限acceptor-language分析](https://arxiv.org/html/2510.23487v1)比较的是确定/非确定接受器识别的语言，忽略具体输出和概率，不是实际Agent任务成功、策略最优或现实无限算力证明。有限context与实现中的摘要会改变抽象，模型调用也不自动成为可靠transition oracle；状态/栈接口、预算、解析与恢复都要检验并付费。假设不合时，回到显式有限workflow、bounded frames和独立结果检查，不由理论表达能力批准工具权限、无错执行或可终止性。
<!-- source-family:SF-2025-ARXIV-2510-23487 -->

### 本人注

- `SF-2025-ARXIV-2510-23487`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40真实memory-discipline gap，仅exact-v1 acceptor层级与假设；不回填后版概率trace或认证真实ReAct。

### 自读判断

按R40真实memory-discipline gap，仅exact-v1 acceptor层级与假设；不回填后版概率trace或认证真实ReAct。

### 实际前肩

适合 model-driven 的部分：

- interpreting ambiguous intent；
- drafting content；
- proposing plans/tool arguments；
- ranking alternatives；
- diagnosing unstructured failure。

这种组合既保留模型灵活性，又让业务不变量可测试。

程序与模型的边界还可以落到每个函数调用：caller 保存循环、必经检查与终止预算，模型只返回受声明 schema 约束的候选；活动调用读取祖先 frames，已完成子树向上交回摘要，完整 trace 另存而不每次重放全部历史。[受限 call-scoped 设计](https://arxiv.org/html/2606.15874v1#S3)将执行结构与本次可见上下文对应起来，但模型返回值仍会影响程序分支，类型解析成功也不保证判断正确。摘要仍可能丢信息，父层积累的子调用返回、frame 大小与递归深度都须独立限制，不能只凭 DAG 名称签出按深度恒定的 token 预算。调用、摘要、trace 驻留、重试与测试全计费；自生成函数通过现有 tests 也不授全域正确或新的 effect 权限。结构、返回证据或预算不合时，保留固定 scaffold、较完整原文和人工/独立 verifier，必要时停止递归；可探索节点的灵活性不替 caller 的执行、恢复与提交责任。
<!-- source-family:SF-2026-ARXIV-2606-15874 -->

### 实际后肩

### 从一次性脚本到平台拥有的可编辑 DAG

自由代码生成适合探索新算子与一次性任务，因为它不要求平台预先拥有完整 operator catalog；但当结果需要被复用、可视化、协作编辑与恢复时，script 不再是足够的状态载体。更稳健的演进是让平台拥有带版本的 canonical DAG，Agent 只提交 typed mutation，backend 在 commit 前验证 schema、引用与无环性，executor 再用 run evidence 验证语义结果，visual editor 与 chat 只呈现同一 graph identity。

这条路线用 operator 生态约束换取可编辑性、审计与恢复；未知算子和短期探索仍可保留脚本分支。Skills 只是可更新的派生操作指南，既不拥有 DAG，也不能绕过平台验证。

当 workflow 由多个并发参与者执行，单个全局图合法还不保证各参与者知道何时走同一分支。一条受限编译路径先把动作、消息和拥有者的 if/while 写成全局协议，再投影成各 lifeline 的局部程序；分支拥有者向需要继续执行的参与者发送专用控制 tag，接收方据此进入对应 continuation。控制消息拥有的是结构选择信息，不是用户授权或工具结果真值；去掉它们后再比较原协议的消息序列，才能避免把新增协调误作业务动作。<!-- source-family:SF-2026-ARXIV-2604-17612 -->

[MSC/ZipperGen v1 的必要条件](https://arxiv.org/html/2604.17612v1)限定有限参与者、可靠有序且无界 FIFO、可执行的类型正确局部函数，以及循环终止等前提。其有限完整执行的 partial correctness 与“前缀存在完整扩展”，不等于任意 runtime fairness、真实 LLM/tool 一定返回或任务成功；超时与不返回仍需平台处理。Projection、广播、队列和多模型调用付费，生成的子流程也须先验证/投影再显式返回结果；结构隔离不是 OS sandbox 或 side effect exactly-once。假设不能成立或实际调用失败时，保留显式 workflow、预算/超时和人工升级，不由 deadlock-free 名称跳过执行证据。<!-- source-family:SF-2026-ARXIV-2604-17612 -->

### Template、Realized Graph 与 Trace 不是同一个对象

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-21407`：Daily2025-10-28补Oct27；R19必要/R25实际gap，2+1+2=5。仅fail/success population与repair/quality预算分责，保pre/post-synthesis人口/非全同预算和工具全费，不扩RTL应用树；未运行实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。

## 22235 · books/part-07-agent/82-multi-agent.md

### 完整新增

图的合并/拆回也可能由物理关系变化触发，而非只由任务拆分决定：当一个载体携带另一个robot时，可暂把两者推理节点并入共同决策图；分离后恢复各自节点，并显式保存成员能力、观测和状态身份。[CGoT的受限模拟](https://arxiv.org/html/2510.22235v1)只展示两车两robot环境的可行性，不证明任意规模调度或分布式一致性；carry关系本身不完成权限、依赖和effect的合并协议。应先声明谁可提出合并、哪些状态可读写、拆回时如何交还未完依赖，并保原成员/拓扑revision与动作trace。关系识别、规划、状态传输与失联恢复都付费，已发生的物理effect不能靠拆图撤销；关系或语义无法确认时，保小型固定图、显式handoff与外部动作验收，不让节点合一冒充安全控制或可靠共识。
<!-- source-family:SF-2025-ARXIV-2510-22235 -->

### 本人注

- `SF-2025-ARXIV-2510-22235`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40真差额，physical carry触发图merge/split与身份保留；不重复create/clone/archive生命周期，不授一致性或控制安全。

### 自读判断

按R40真差额，physical carry触发图merge/split与身份保留；不重复create/clone/archive生命周期，不授一致性或控制安全。

### 实际前肩

通信mode还可以与“这轮联系谁”分开学习：角色/近期状态先给各有向pair打分，mode决定全量或选择性的broadcast/receive，选择性分支再按eligible候选的相对分数取零个或多个伙伴，而非固定top-k。[受限CTDE分支](https://arxiv.org/html/2610.25851v1#S3)只在训练用全局state和既成有向邻域构造非负mixing；比较本轮候选action时固定predecisioncontext，所选mode只决定下一轮图，才可由各localQ的greedy选择最大化这份learnedjointQ，不认证真实return最优。退出通信可保solo答案而停止后续参与，off则省当前调用；调度feature仍读取其他成员表示，不能把不用centralmixer说成完全无通信。有限三角色对照保模型/提示/round，token减少仍不免训练、pair打分、图维护与最终aggregation，经验gain阈值也不是信息论或统计证书。伙伴资格、时序或质量/预算漂移时，保留固定小图/原协议与独立结果验收，不由attention、单调mixer或少轮次批准任意规模可靠协作。<!-- source-family:SF-2026-ARXIV-2610-25851 -->

## Topology 从部署前选择演进到运行时有界修复

运行时 adaptation 不只包括修图，也包括受预算约束的 fan-out。Orchestrator 可以依据任务分解、预计并行 critical path 与当前 worker outcome，选择是否实例化子 Agent、分配多少分支及何时合并；但控制对象必须是 typed dependency graph 和 budget，不是“让模型自由召唤更多模型”。

学习 fan-out 或只更新 orchestrator、冻结 executors，可以降低训练与 credit assignment 复杂度，却会让 executor 能力变化、共享工具状态和合并错误变成 distribution shift。静态 worker count 在预算可预测、任务强耦合或 side effect 多时继续成立；动态 topology 只有在分解收益可观测、子任务权限隔离且合并有 verifier 时才值得采用。

### 实际后肩

运行时创建还要分开三种生命周期：可复用的 agent metadata/object pool、每次调用的临时 execution clone，以及能够恢复的 execution-memory archive。一个分支先按模型、指令、工具与初始记忆注册配置，调用时克隆对象执行，结束后删除 clone，历史仍由独立记忆组件持有；删除执行对象不等于清空证据，也不等于 durable workflow checkpoint 或已回滚外部 effect。并行调用的共享 message board 可用写锁及每个 Agent 的读取 cursor 只投递新差量，但这只控制消息读写，不认证内容真实、工具权限或副作用隔离。[原始有限机制与对照](https://arxiv.org/html/2602.16891v1)中的拓扑/摘要联合消融不识别单独动态 create 的收益，容器与图记忆也不授全面安全；生命周期拆分增加 clone、状态索引、恢复与消息同步费用，配置不可追溯、恢复证据不足或调用预算不稳时，保留固定小型 worker pool、显式 typed handoff 与第81章的执行控制。<!-- source-family:SF-2026-ARXIV-2602-16891 -->

运行中的子 Agent 也不必等完成或报错后才重建：它可以在局部障碍出现时暂停，提交 progress/uncertainty、修改请求和支持该请求的 tool evidence；orchestrator 决定是否改 subgoal、context、tools 或剩余预算，将 revision 作为 observation 记入原 local trajectory 后继续，或显式终止。这保留执行连续性，却增加通信、版本与全局责任协调；请求本身不授权扩大用户范围或工具权限。反馈还可用于学习 delegation，但应先区分原配置失配与后来外生要求变化，仅把可归因的 hint 用作训练期 self-teacher，最终 outcome 仍单独监督。[POrchestra 的有限对照](https://arxiv.org/html/2610.13485v1)只执行一个 active 子 Agent，非并发协调或普遍成本最优保证；反馈不可靠、任务稳定或副作用强时，固定配置与有界返回交接仍合理。<!-- source-family:SF-2026-ARXIV-2610-13485 -->

有界fan-out还要区分已启动、provider已ready、仍在运行与结果已验收的数量。只按启动数放大批次，可能在首次限流前堆出大量尚未ready的工作；一种限定实现正常期先启动5项，再每700ms加入一项，首次provider限流后停止ramp，以ready数量初始化并收缩容量，随后在容量与等待时刻允许时逐项启动。Kimi Code 0.12的rate-limit phase优先重试同一agent，再处理resume或新任务，用3/6/12秒递增等待与约3分钟无新限流后的探测增容，换取较少重复初始化；正常ramp本身不以active数量硬封顶，这套规则不是最优配额、生产SLO或预算安全证明。<!-- source-family:SF-KIMI-CODE-0-12 -->

批次Join也不应把取消改写为“所有工作都未发生”：结果槽保留原输入顺序与已完成输出，将已开始但未完的任务和从未启动的任务分别标为aborted/started与aborted/not_started，已知agent身份可用于后续resume；单任务timeout只终止该任务，剩余唯一任务持续限流则可终态失败而非无限重试。Swarm mode中的自动审批仅针对AgentSwarm工具，不等于子任务工具权限豁免。它增加队列、退避与部分结果状态，但不证明队列持久性、crash重放、effect回滚或模型返回即正确；高风险任务仍需原有能力边界、预算验收与独立verifier，配额不可观测时保留静态小批次或串行fallback。<!-- source-family:SF-KIMI-CODE-0-12 -->

Task-topology matching 最初通常发生在运行前：根据 decomposability、evidence independence
与 tool coupling，在 singleton、star、tree、chain 或 debate 中选一个结构。这个方案仍然
合理，因为 topology 稳定、容易复现，且不会让控制面在执行中不断改写责任关系。

静态结构也可复用搜索资产，而不必对每个目标任务从头搜索。把来源任务的搜索轨迹凝成带版本的operator-level结构启发H与node间输出contract C，可以在新任务上提出待编译的topology；来源搜索只产生proposal，H来自优/劣轨迹，C可来自中间得分却最终解析失败的轨迹；目标任务仍须做结构检查、真实执行与结果验收。task族、模型、提示、contract与来源搜索预算都应随资产保存。

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-22422`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R36新差额，从有限policy表到population/meanfield关系；与后邻持续驱动项拟合不同，保模拟/实跑权限与反侧，不授大群体必失配。

## 22622 · books/part-06-ai-infrastructure/66-evaluation-system.md

### 完整新增

多模态伪造检测还应按生成pipeline交叉迁移，而不只报一个合并真假分数：在A类伪迹上训练后迁移B，与B迁移A可能不对称；两类伪迹叠加时，一个更显著线索也可能支配detector。对声明能接收缺失模态的模型，可mask音频或视频作诊断，但须重新按仍可见模态定义标签，不能将只在被遮模态造假的样本继续当可见fake。[受限DeepfakeBench-MM对照](https://arxiv.org/html/2510.22622v1)支持这套测量分解，不以t-SNE聚类定位唯一因果机制，也不授未见pipeline或真实全视频的安全率。数据生成、压缩/后处理、split、mask政策与各模态label必须绑定；制备、重复训练、全部迁移和独立人工核验都付费。标签支持、缺模态接口或外推不合时，保原单pipeline切片、分模态结果与Unknown，不由联合准确率批准所有身份/内容真值。
<!-- source-family:SF-2025-ARXIV-2510-22622 -->

### 本人注

- `SF-2025-ARXIV-2510-22622`：Daily2025-10-29补窗；复用sole已成exact-v1必要支持/反侧，writer已实际读具体结论与owner差额，未核代码或复现。按R40真差额补迁移非互逆、叠加伪迹支配及mask后重定label，区别已有普通模态消融。

### 自读判断

按R40真差额补迁移非互逆、叠加伪迹支配及mask后重定label，区别已有普通模态消融。

### 实际前肩

[DriveSpatial的有限驾驶评价](https://arxiv.org/html/2605.23176v1#S3)提供这种支持约束实例，但GT/HDMap或LiDAR boxes生成的BEV只是privileged诊断，排除construction题后的收益不等可部署感知改进。不限回放的人类mini子集、模型固定输入/greedy与不同来源人口也不能拼成同预算全量能力差或因果瓶颈。坐标统一、metadata人审、图/QA制备、采帧及全部推理评价均付费；track/可见性、来源或题目支持不足时，保留原视图、分项几何任务和人工核查，不由跨view高分批准真实驾驶或闭环安全。<!-- source-family:SF-2026-ARXIV-2605-23176 -->

几何对象固定后，还须确认不同depiction是否让模型看到了同一任务证据：video、diagram、加入description和以description替图是不同input政策，文本代理不会自动取得原视觉真值或同信息预算。按步骤/任务分列这些条件，能发现某类对齐收益与另一类步骤判断退步并存；[受限跨depiction对照](https://arxiv.org/html/2604.00913v1)中description对D2有益而T1/T3可退，不能由aggregate winner批准统一替换。人工description核验、解析失败计错、匹配样本与额外推理均计成本；CKA接近零和局部attention变化不证明视觉信息不可恢复或encoder瓶颈因果。任务支持或文字真实性未验时保留原video/diagram、分项测量与人工检查，不把文本更强升级为普遍视觉失明。
<!-- source-family:SF-2026-ARXIV-2604-00913 -->

任务要从局部视觉材料学习规则时，还应将 teaching evidence 与待解决的 test state 分开干预：先保留原图，只补 test state 的文字 oracle，再补 teaching evidence，最后才比较纯文字；指向正确页面与裁掉其他页面也是两种不同输入政策。[MMCL 的有限诊断](https://arxiv.org/html/2605.12703v1)只在以合成任务为主的可转换子集做这些对照，文字还经过额外整理，不由收益唯一归因感知，也不外推全部多模态任务能被无损 textualize。Manual pointer 可以提高 rubric 满足却仍不通过整题，crop 也可能损失必要上下文，因此应同时保留严格完成率、分项质量和原任务人口。只看 rubric/文本的 judge 与错误分类器不能独立回原图认证 oracle；跨 judge 一致和四类标签仍不是错误因果真值。材料制备、oracle 人审、额外 API/agent recheck 与重复评估都计费，scaffold 在不同模型上可反退；子集、文字支持或净预算不合适时，保留原图全上下文与独立核验，不以更干净输入的高分签发通用视觉理解或部署改进。<!-- source-family:SF-2026-ARXIV-2605-12703 -->

自我视角视频问答还可固定同一帧预算，分别提供 oracle 与预测的 where/when 提示，区分“证据已被指出仍答错”与“定位器先选错”；时间窗口、对象文字与画面标记应分项比较，而不把所有提示并成一种增强输入。[受限定位诊断](https://arxiv.org/html/2605.15342v1)中预测圆圈可低于无提示，oracle 收益也不证明部署已会找到证据。人工轨迹、对象绑定与分割插值须保不同来源，未绑定部分或模型派生 mask 不能统称逐帧真值；人工全片不限时与模型固定采帧更不是同预算对照。理由分数若只比较 reference/student 文本，仍不认证模型实际看到了相应过程，人工标注也不抹去多模型筛选的先验。全视频制备、人审、定位/分割、额外推理与评分均计费；提示支持、对象身份或回答质量退化时，保完整原输入、无提示基线与独立视频核查，不由更高 oracle 分数签发真实时空理解或可部署改进。<!-- source-family:SF-2026-ARXIV-2605-15342 -->

### 实际后肩

### 视频评估先确认模态与时间信息是否必要

视频摘要的“保留了多少信息”与“写出的内容是否忠实”也是不同对象。全文视频评价成本高，只比较文本相似度又难兼容文字与 keyframe 混合摘要；一条受限分支先生成固定的详细 caption 作为文本 proxy，再比较同一 scorer 在原视频和摘要条件下恢复 caption 关键词的 log-likelihood 差。它测量固定 caption、关键词和 VLM 下的信息保留代理，允许在这些身份不变时比较摘要格式，不是原始视频的完整 mutual information，也不证明 caption 覆盖了全部事实。把摘要视为原视频子集的推导假设不适用于任意 hallucinated summary；更换 scorer 或 captioner 后须重新校准，不能直接拿分数作跨模型排名。<!-- source-family:SF-2026-ARXIV-2601-09851 -->

这个 sensor 增加 caption、关键词提取与概率评分调用，摘要 token 变少不等于完整请求路径更快。ViSIL 在受限视频任务与人类问答中观察到 proxy 分数和可用性的关联，尚非摘要提高答案的因果保证；其错误扰动实验又显示，增加 keyframes 可让人更容易忽略文本错误，视觉错位也能误导自动 judge。因而信息保留、逐 claim 的视频支持和错误发现能力须分别验收，不能由前者授予事实忠实或无幻觉保证。概率接口缺失、来源 caption 可疑或支持含糊时，应回到完整输入、人工核验或明确 Unknown；音频与跨分布可靠性仍需单独证据。[必要机制与直接反侧](https://arxiv.org/html/2601.09851v1)见 §3.3–3.4、§4–5。

音频必要性也应在同一问题上比较 None、fragment 与 full audio，再将 temporal binding（TB）和具体信息需求分开。先判是否 audio-needed（AN），再在 AN 内区分 fragment-sufficient（FS）与 extended-sufficient（XS）；“只有 3–4%”描述作者 AN 内的切片，不是全部视频题、更不是真实认知机制占比。<!-- source-family:SF-2026-ARXIV-2604-24401 -->

分层消融增加片段构造、重复调用和支持证据成本，片段边界可能遗漏声学线索，TB 也不等于已证明脑内时间推理。片段选择或 gold 支持不可靠时保留 full audio 并报告不可区分；只需静态声音信息的任务可采用便宜 fragment 基线，不静默改变原始全输入分母。

Gold answer 的支持证据也必须绑定模型实际看到的帧集合。若标注来自完整视频，而模型只消费 16/32/64 sampled frames，题目可能对该输入不可答；EvalSpec 应记录 frame sampler、可见 evidence、visibility 筛选与人工复核，并用 dummy video 对照检查语言先验。作者 5% visibility 门槛是其筛选协议，64 帧不是普适的可答性真值。<!-- source-family:SF-2026-ARXIV-2604-24300 -->

### 实际注尾（保留）

- `SF-2025-ARXIV-2510-22922`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R37新差额人审interface改变测量能力，保错误人口/语义转换/无显著时间差，接human evidence后而非新列产品界面。
- `SF-2025-ARXIV-2510-22371`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R36真实gap，仅lookahead-v-path长度及输出合同，接三轴难度前后，不引入额外Methods/未读普遍复杂度证明。
- `SF-2025-ARXIV-2510-22931`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R37实际gap，domain mixture/confusion correction与已有配置mixture不同；不照录符号不闭reject式，不授任意漂移coverage。
- `SF-2025-ARXIV-2510-22775`：Daily2025-10-29补窗；精确v1必要支持/直接反侧已读，未核代码或复现。按R37实际gap，新增group互见+离线execution标签移交online reward；不让免线上执行偷换无测试/最终正确。
