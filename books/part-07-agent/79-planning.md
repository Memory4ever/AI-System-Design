# 第79章 Planning

**Knowledge Tree:** Part VII Agent：从回答问题到执行任务
**Stable Knowledge Node ID:** `AGENT-PLANNING`
**Legacy Chapter:** Ch75
**Status:** Draft

**Roadmap Intent:** 复杂任务如何被拆解、排序和执行。

## 本章要回答的问题

Planning 与“先输出步骤列表”有何不同？为什么一个看起来合理的计划在执行中会迅速失效？Agent 应一次规划到底，还是在 observation 后持续 replanning？

本章的核心判断是：**Plan 是关于未来状态转移的可验证假设，应显式表达目标、前置条件、依赖、资源和完成证据；在部分可观测环境中，planning 与 execution 必须通过 observation 反复闭环。**

## Plan 不是解释文本

朴素计划：

```text
1. Analyze
2. Implement
3. Test
```

它没有输入、完成条件、依赖或失败分支，无法驱动 runtime。更可执行的 plan node 包含：

```text
step_id
goal / expected state
preconditions
action or tool class
inputs and dependencies
success evidence
risk / approval class
budget
status
```

自然语言可以描述意图，typed state 承担控制。

## 从目标到状态图

设环境状态为 `s_t`，action 为 `a_t`，observation 为 `o_(t+1)`：

```text
a_t = policy(goal, belief_t, plan_t)
o_(t+1) = environment(s_t, a_t)
belief_(t+1) = update(belief_t, o_(t+1))
```

Agent 通常不能直接观察完整 `s_t`，只能维护 belief/context。计划因此不是确定执行轨迹，而是基于当前信息的 conditional policy。

部分可观测性还要区分三种状态：事实在接口中不可获得、事实可由 tool 查询但尚未查询、以及 observation 已实际进入
当前 Context。把第二种误写成第三种，会让 planner 在没有证据时行动；把第二种误写成第一种，又会漏掉本可通过
observation action 消除的不确定性。因此 plan node 除业务 action 外，还应显式安排何时查询哪些 latent state，记录
query freshness，并让查询成本与行动风险竞争同一预算。稳定的小状态若能被动推送或每轮完整读取，旧的固定
observation schema 更简单，不必强制增加主动监控循环。

当任务分布相对稳定且有独立 validation 时，可以再把**环境先验估计器与行动策略分开**：先估计未观察属性的分布，或继续检索/测试后的成功概率，再把这些估计与行动成本一起交给 selector，而不是让同一次规划直接把自述 confidence 当事实。先验仍不是 observation；它应绑定 estimator、模型、schema 与适用分布，校准样本和额外标注、训练、调用/context 都要计价。[Calibrate-Then-Act 的有限实验](https://arxiv.org/html/2602.16699v1)将 QA confidence 校准或合成文件属性估计传给 policy，但检索质量是全体验证估计、unit-test 返回合成属性真值，reward 改善也伴随部分准确率下降，不能推广为真实工具最佳停止或无损降费。分布漂移或先验失准时，应回到真实 observation、固定 test-first/检索或人工复核；估计器只提出决策依据，不获得环境事实的提交权。<!-- source-family:SF-2026-ARXIV-2602-16699 -->

提示策略的效用也要绑定**目标 policy 的实际执行**：源解法常用某条规则，不表示另一个模型读到该提示后就能完成任务。[受限 strategy-selection 对照](https://arxiv.org/html/2602.22583v1#S3)把问题–策略在固定模型、prompt 和 decoding 下的试用结果作为 utility 监督，再用检索/图特征排序指导；human 与 model source 的优势会随策略/目标模型反转，不能把源频率或“人类方法”直接当可执行性。Beta–Binomial 平滑与后续校准只属于训练/验证人口，adherence judge 的相关性不证明提示因果，correctness judge 也可能共享盲点。源抽取、试用 rollout、图/估计器训练与判分都计费，较短线上输出不等总成本下降；有限模型和任务之外、数据泄漏或校准漂移时保留固定提示、无 guidance 与可验证过程，不让估计器获得最终答案真值权。<!-- source-family:SF-2026-ARXIV-2602-22583 -->

“计划过”也不等于“执行过”。对近期可检验承诺，runtime 应把 target、expected action、deadline/window 与完成证据
写入 typed commitment ledger，再与后续真实 action 和 observation 对齐；窗口内 partial、未执行和被新证据
supersede 必须分开。该 ledger 为 replanning 提供 mismatch evidence，却会增加抽取误差、陈旧承诺与检查开销，
也不能把固定窗口命中率当作完整 planning quality。[长时程 tool-mediated pilot](https://arxiv.org/html/2609.02459v1)
只说明 PMR 与 RAG@10 能暴露“可查询状态未进入 Context”和“自述承诺未落实”两类接口失配；23 次受 playbook
约束的游戏运行、缺少 random/scripted baseline，不能支持模型排名或通用阈值。

### 学习到的 Transition 只能验证候选，不能提交环境事实

<!-- semantic-body-binding:SF-2026-ARXIV-2606-27806:start -->
只让语言模型在同一 Context 中想象 state delta 并继续规划，成本低且能处理开放语义，但一次错误 transition 会被后续步骤当成事实继续传播。条件允许时，可以保留 LLM 的语义 proposal authority，同时让独立的 parametric transition model 估计 action validity、候选 state delta、risk 与 value；两者不一致时，它只能降低候选优先级或触发定点 revision，不能把 provisional transition 提交为外部事实。事实 commit authority 仍属于真实 environment observation 或具有明确契约的 controller。

这条分支用额外模型调用和状态校准换取更早的错误拦截，也会引入共享盲点、distribution shift 和错误否决。状态不可结构化、transition confidence 失准或风险不足以支付校验成本时，纯 LLM planning 仍可用于低风险 proposal；高风险或 OOD 状态则必须回到规则、真实 rollout、tool observation 或人工复核后再推进。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-27806:end -->

缩小 action 分支之前，还要问 partial model 覆盖了哪些任务。task-agnostic language intents 若只保留当前模型认为可行的动作，会把遗漏 intent 永久排除；一个条件分支让 partial-action proposal 与 full-action support 混合，给被遗漏动作保留非零探索机会。这与 transition 是否准确是两个约束：合法、可预测的少量候选不证明固定任务人口已被覆盖，语言提示也不自动形成准确 world model。<!-- source-family:SF-2026-ARXIV-2602-10390 -->

[受限 affordance 分析](https://arxiv.org/html/2602.10390v1)依赖 communicating MDP、deterministic competent planner、固定任务/长度与独立采样等条件，不授任意 LLM 的最优搜索或通用 regret。混合支持和调参增加调用；Pybullet 局部对照中，减少搜索步也可能增加 LLM calls。coverage 失准、任务人口改变或预算不值时，回退 full-action 搜索、真实 observation 和既有短 horizon，不能用剪枝后成功的样本证明被剪动作无用。

即使 transition 可用于比较候选，向前想象多少步仍是另一项决策。固定短 horizon 在模型误差大、状态简单或预算紧时是合理基线；若不同状态需要的 lookahead 不同，可以把步数 $K$ 与 action 一起交给 policy。[一项文本环境实验](https://arxiv.org/html/2601.08955v1)先冻结 world model，以 teacher-forced 专家动作生成 imagined states，再按专家动作 likelihood 减去 $K$ 惩罚构造步数伪标签；action 与 $K$ 两个监督目标 warmup 后，用环境回报与步数代价联合更新两项决策。这里的伪标签最优值只是给定专家路径和模型下的 proxy，不是环境中真实最优 horizon；预测状态仍不能替代实际 observation。<!-- source-family:SF-2026-ARXIV-2601-08955 -->

这条分支使 planning compute 成为 state-conditioned 控制量，但增加 world-model 数据、policy 训练与误差耦合：错误 transition 可诱导错误的 $K$，更大的、未经该 transition 训练的模型也未必改善规划。步数惩罚与 episode token 归一化预算不等于 wall-clock latency、费用或完整训练成本，比较质量时应分别核这些账；原有文本模拟结果不授予物理行动或 OOD 安全。模型失准、额外调用不值得或缺少可校准状态时，应保留 reactive action、固定短 horizon，以及回到真实 tool/environment observation 后再规划的退路。

规划预算也可以在同一 actor 的每个决策步选择 reasoning effort，而不改变 lookahead 或另换 workflow。先固定一条成功的高努力轨迹，再在每个既定 history/observation 下试用有限档位，以复现功能等价 action 的最低档位作局部监督；这个标签只度量指定路径、试验次数和等价判定，既不是任务计算下界，也不认证组合这些局部选择后整条任务仍成功。Router 的 teacher rationale 与 SFT 只是选择器训练，真实 rollout 仍须独立验 trajectory outcome、工具合法性和完整费用。[Ares 的有限对照](https://arxiv.org/html/2603.07915v1)再以 outcome 与成功轨迹的平均档位 penalty 调整选择；档位 penalty 不等累计实际 tokens，失败不受该 cost 惩罚也不授全任务最小总费用。有限重试的零成功不证明任务不可解，筛选人口与 rationale 消融不授全分布保持或唯一内部因果；跨模型与检索任务仍有质量退步。路径采样、三档重试、teacher 标注、router/actor全部调用、训练和工具均计费，token缩短不自动改善墙钟或安全；状态、label或outcome失配时，保留固定已验收努力、原actor与可信tool/task gate，而不让路由预测批准真实effect。<!-- source-family:SF-2026-ARXIV-2603-07915 -->

显式 transition/lookahead 之外，还存在直接预测**自身 policy 条件 return**的理想分支。[AIQI 的必要分析](https://arxiv.org/pdf/2602.23242v1)对完整 history/action 的离散 H-step return 作 Bayesian mixture，不模拟未来 environment；用 N≥H 的 phase-separated augmentation，只在完整奖励已观察后补该 phase return，再以正探索概率和固定 tie-break 选 action。有限 action/observation/reward、奖励[0,1]、折扣γ∈(0,1)，以及每个 mixture 对自身 policy 的真实 conditional return 有正 prior 的 grain-of-truth 都是条件，不是普通 value network 自带的性质。其 asymptotic ε 分析还需足够小的探索/截断误差、足够细的离散级别及 N−H counterfactual buffer；reflective-oracle 闭包不提供有限硬件可部署性、sample complexity 或墙钟效率。旧 policy 日志只让 predictor 学到旧 policy 后续 return，最大化它不等自己后续最优，原 off-policy 存在性反例正限制这种迁移。条件无法核实或只能有限近似时，保留 reactive policy、显式 model/search 与真实 rollout 评价；该理想分支不授近似实验、LLM 或环境事实提交权。<!-- source-family:SF-2026-ARXIV-2602-23242 -->

## Decomposition 的价值与代价

拆分任务可以：

- 降低单步复杂度；
- 暴露可验证 intermediate results；
- 允许并行与不同 tools；
- 提前识别 approval/risk。

过度拆分则增加：

- model/tool calls；
- context growth；
- state handoff error；
- orchestration latency；
- 局部目标偏离整体目标。

拆分粒度应由可验证边界决定，而非步骤越多越“智能”。

## 依赖、并行与 Critical Path

Plan 更接近 DAG/state machine：

```text
collect requirements ─┬→ implementation → tests
                      └→ risk review ────┘
```

无依赖步骤可以并行，但共享资源和副作用仍需 coordination。总时长由 critical path 和 queue/resource constraints 决定，不能简单等于各步平均时间。

并行还会增加 merge/conflict 成本，只有当步骤输出 contract 清晰时才有效。

对于 evidence-acquisition task，并行轴不能简化成“同时开更多搜索”。依赖图应先区分可独立 subquery 与需要
前序证据才能定义的分支，再把有限 search/tool budget 分给 ready nodes：

```text
goal → dependency-aware evidence graph
→ parallel acquisition on ready independent nodes
→ deduplicate / verify / merge at checkpoints
→ open dependent nodes or backtrack
```

并行可缩短 critical path，却会复制 query、Context 和外部配额；错误 observation 还可能同时污染多个分支。
Search More, Think Less 与 LongVideo-R1 分别在网页 evidence 与长视频 active perception 中提供受限案例，
支持“并行 acquisition + hierarchical checkpoint”，不证明宽度越大越好。单链搜索在依赖强、预算小或 verifier
弱时仍更稳。

### Subtask Parallelism 与 Trial Parallelism 解决的不是同一个等待

并行 planning 至少有两条不同的轴。Subtask parallelism 把可独立依赖节点同时展开，收益来自缩短 critical path；trial parallelism 对同一个困难节点运行多个竞争路径，收益来自增加找到可验证解的机会。二者的 state 与 commit 语义不同：

```text
subtask branches: distinct outputs → dependency-aware merge
trial branches: competing outputs → verifier selects or rejects
```

如果只用一种“parallel reasoning”格式，runtime 很难定义谁拥有 budget、哪个 branch 可以取消、何时回收 KV/工具配额、如何把 winner 写回主轨迹。显式 branch type 与 grammar 可以让训练和 serving 识别这两个边界，但会增加 annotation、parser、scheduler 和 reinforcement signal；同源 trial 还会共享盲点。任务不可分、verifier 弱或 action 有副作用时，单路径仍更可靠。

## Replanning 的触发条件

执行 observation 可能显示：

- precondition 不成立；
- tool/API 变化；
- data 缺失或冲突；
- budget 即将耗尽；
- user goal 改变；
- step 失败但存在替代路径。

Runtime 应在这些事件触发 replanning，而不是每一步都从零规划，也不是无条件坚持原计划。Plan version 与 superseded steps 要保留，便于审计。

Replanning 前还要区分两个 failure channel：计划图本身不可行，还是 action 执行偏离了一个本来可行的计划。
前者需要修改依赖、资源或目标；后者应先约束 executor、修正 mismatch，再决定是否废弃 plan：

```text
plan graph + resource / temporal constraints
→ solver or deterministic feasibility check
→ constrained execution with step evidence
→ compare observed transition with planned transition
→ repair execution or version the plan
```

外部 solver 提高可判定约束的一致性，却会把建模错误、离散化和 solver availability 变成新边界；开放世界或
语义目标不能全部形式化。TAPE 的合成任务支持 feasibility/execution-conformance 分离，不证明形式求解器能覆盖
所有 Agent planning。短任务和低副作用场景仍可用轻量 plan + observation-triggered replanning。

若同一 domain 的约束长期重复，每个 query 都重新生成求解代码还会重复支付建模成本。[一条受限分支](https://arxiv.org/html/2601.09097v1)先用示例 query/answer 导出组合参数、约束参数与输出结构，再生成枚举、过滤和交付函数；之后每个 query 只提取参数，消费已编译的 domain artifact，而不改 solver。这样把可变的语义抽取与可复用的确定性执行分开，但确定性只属于已编码约束：参数遗漏、错误 schema 或渲染失真仍会让一个正常运行的 solver 交付错误计划。<!-- source-family:SF-2026-ARXIV-2601-09097 -->

Artifact 应绑定 schema、约束解释、代码与输出版本，除构造示例外还用 held-out query 检查覆盖与失败路径；禁止硬编码的提示和单例 refinement 不证明无过拟合或全域完备。收益须按复用次数摊销 schema/code/refinement 的离线成本，枚举空间过大也可能转成新的资源瓶颈；作者的闭合任务与有限消融不支持把采样/枚举预算改变都归因于单模块。新 domain、参数无法确认或隐藏约束暴露时，应重新建模/版本化 artifact，或回退逐 query 求解、轻量计划和澄清，而非继续套用旧函数。

若需求本身仍在变化，先固定 solver 也可能过早：用户可能尚未决定“哪个群体、哪些字段、按什么口径”才算满足问题。一条关系数据分支把这份解释外化成目标关系集合与其上的答案程序；目标列、语义和群体定义可由用户修订，数据物化则负责用已检索源构造这些关系，最后执行程序得到答案。对表内容不确定时，先查询实际值、分布和结构，再改目标或补来源，而不是让字段名、几条样本或流畅答案暗中决定统计人口。转换依赖图与可重跑脚本使构造过程可检查；它们展示的是已编码操作怎样产生结果，不证明目标忠实于用户、源数据完整或语义生成列真实。

[Pneuma-Seeker 的有限对照](https://arxiv.org/html/2603.10747v1#S7)中，显式目标关系帮助一条多表统计补齐遗漏来源，主动查询也修正了把非空 capital 都当国家首都的筛选；但消融同时改变目标定义与物化责任，两个人工构造的模糊需求案例不认证普遍收敛或用户信任。目标协商、数据检索与探测、物化、模型调用、依赖记录和人工检查都有成本，某些数据集的总时间或内存反而高于直接作答基线。应分别验收目标语义、来源覆盖、程序执行与答案；预算耗尽后的回应也可能仍不完整。目标口径漂移、数据不齐或执行无法可靠确认时，回到澄清、原始数据与简单可检验查询，不让确定性运行替用户确认需求已满足。<!-- source-family:SF-2026-ARXIV-2603-10747 -->

自然语言约束的另一条交接分支，是先声明 predicate 及其 arity，再在这份签名下翻译成形式表达式，而不是一次生成未显式约束的 FOL。声明给后续翻译一个可检查的中间对象；若生成项与签名不一致，可让模型提出 repair，再交由 parser/compiler 与 solver 分别检查结构和已编码约束。模型修复不是编译器，使用的 predicate 都已声明也只说明自一致，不能证明原问题中的实体、关系或量词被忠实表达。[predicate-first 的受限实验](https://arxiv.org/html/2601.09446v1)支持考察这个中间接口，但不授自然语言到形式语义的完整性。<!-- source-family:SF-2026-ARXIV-2601-09446 -->

因此应分开记录签名/arity 检查、可解析或可执行比例、solver 输出与最终语义正确性，并保留过滤前人口；把 solver 成功筛出的训练样本称作可靠语义标签会隐藏模型遗漏。翻译、重喂签名和修复增加 prefill、模型调用与验证成本，输出 token 相近不能证明延迟免费。小模型/数据集切片仍有性能退步，覆盖指标也未消除量词错误；签名不确定、修复循环失控或语义无法形式化时，保留直接翻译后验证、人工澄清或轻量计划，而不让自一致的 formal artifact 自动授权执行。

形式系统不能推出答案时，还可以把“缺什么前提”交给模型提议，而不是让 solver 扩大自己的事实权限：从已可推出的 backbone literals 取少量 antecedents，生成新 commonsense literal，再用模型的常识性与相关性代理筛选，加入候选前提后重试条件推理。SAT 只证明给定全部前提下的 entailment，单条假设各自相容不保证它们与原前提联合一致，更不验证新常识或翻译真实；应另核 joint consistency、来源与语义，模型自评不能认证它自己补入的事实。[受限 ARGOS 对照](https://arxiv.org/html/2601.18595v1)仍有错误翻转与翻译失败，投票 fallback 必须保留 best guess 身份。Literal生成、评分、CoT、prefill和solver共同计价，平均CoT较少不等完整省算，内文阈值/成本冲突不拼精确配方；缺可信前提或预算耗尽时，回原solver、独立澄清与明确Unknown，不由可满足的假设自签正确结论。<!-- source-family:SF-2026-ARXIV-2601-18595 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11225:start -->
Observation-triggered replan 还可以从“重新生成计划”演进为带接受准则的 trajectory refinement：当前已接受轨迹是 versioned incumbent，executor 提供观测，inspector 从 trace 生成 backward discrepancy，evolver 只替换受影响 suffix，verifier 比较新旧轨迹并独占 commit。这样可保留已验证 prefix，并阻止一次看似合理的局部修改静默降低整体计划。

它用额外执行、inspection、版本比较和 verifier 成本换更精确的失败定位；错误 textual gradient 也可能让系统稳定地优化错误方向。工具能力不足、验证不可靠或迭代预算耗尽时，应回退从 checkpoint 全局 replan、保守 retry 或人工接管。exact-v1 只支持 DeepPlanning、GAIA 与作者披露的 token proxy/有限任务；未直接测 latency，也不证明 human-in-the-loop 上界等于 autonomous result。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11225:end -->

## Search-based Planning 的边界

Chain-of-Thought 产生一条路径；Tree of Thoughts 等方法探索多个候选并评价/回溯。搜索可以提高某些任务成功率，却使模型 calls 近似随 branching factor 和 depth 增长：

```text
candidate_nodes ≈ 1 + b + b^2 + ... + b^d
```

Pruning、heuristic、budget 和 verifier quality 决定是否值得。模型自己生成并评分候选可能共享同一盲点，搜索更多不等于可靠性单调提高。

开放环境里，搜索剪枝还须区分“当前前置条件不满足”与“永久不值得探索”。一条[受限规划分支](https://arxiv.org/html/2602.17622v1#S4)把 observation、hypothesis 与 proposed action 保存在外部 typed evidence tree，以预计剩余步数和启发式 difficulty 分配预算；剪掉的分支仍留在树中，新证据或可用凭据改变其 precondition 时重新评价并恢复候选。这里可撤销的是 search-support 决定，不是已发生的世界 effect；LLM 预测 horizon 与经验难度阈值均是排序代理，不授完整性、MCTS soundness或执行授权。Tree／证据传播、重复评价与额外模型调用有费，也可能受外部假证据、遗漏分支和 token预算误导；原三模型／三 trial 的 best-of-three与mean表述不一致、累计组件消融和不同tool接口不能证明reopen单独造成headline成功率，公开walkthrough还限制任务外推。证据未能可信满足前置条件、heuristic失准或预算不值时，应保留更宽搜索、真实observation与独立终局verifier；简单稳定任务继续普通静态剪枝，不从一次未成功授永久排除。<!-- source-family:SF-2026-ARXIV-2602-17622 -->

候选程序不断改写时，反馈还需要可归属的谱系。只按语义相似度检索旧plan或summary，可能把另一条分支的失败误当当前候选已经失败；一个更窄的复用分支让plan/summary与对应parent-ID关联，只在匹配候选谱系时作为下一次改写条件。它保留“这条经验来自哪个程序”的约束，文本summary仍只是对已有执行反馈的解释，不是当前程序的因果事实或正确性证明。<!-- source-family:SF-2026-ARXIV-2512-24077 -->

评价预算也可分层：先用局部fast-fail检查筛掉明显不值得继续的候选，再让完整evaluator决定全任务结果。谱系管理、summary生成与早筛增加状态和调用成本，也可能过度限制跨分支经验迁移；局部通过不授全任务成功，早筛也可能错丢有价值候选。[LoongFlow v1 §4.1.1/Algorithm1/§5.4](https://arxiv.org/html/2512.24077v1)只支持作者程序搜索下的归属与预算机制，不证明summary可靠、科学成绩可迁移或搜索最终找到全局最优。反馈身份不明、代码变化已使经验过期或早筛不可信时，应保留原始执行结果、重新跑完整评价或回退普通宽搜索，而不是把近邻文本当新候选的验收。

从历史解检索出可用操作，还不等于知道它们应以什么顺序执行。对有可靠形式状态与前置条件检查器的任务，可以从检索到的成功 trace 构造操作 precedence graph，把出现频率和先后关系作为当前候选的排序 prior，再由 symbolic executor 检查提议是否可执行。Retrieval 拥有候选支持集，历史图提出顺序偏好，executor 才拥有合法状态转移；历史中常见的边不是当前任务必需的依赖，也不能自行签发最终证明。<!-- source-family:arxiv:2603.04852v1 -->

这用图构建、状态过滤和多次模型调用换取更窄的搜索；检索集过小会直接漏掉必要操作，局部 precedence 又不能保证全局深度一致。[相同逐步执行器的受限对照](https://arxiv.org/pdf/2603.04852v1)在固定模型、形式输入和超时下，检索加图优于仅检索，支持将覆盖与顺序分别验收，但没有评价上游视觉/解析，困难长证明仍会失败。历史库、形式化或前置条件不可靠时，应保留更宽候选、确定性搜索与独立终局 verifier；简单任务继续用直接计划或普通检索，不把 prior 当作开放环境的事实与安全授权。

Search 还要区分训练期 teacher 与运行期 controller。符号 graph search 可以离线为一批问题生成较优 plan，模型再从
这些监督中学习直接提出计划；迭代时只在未覆盖或失败样本上继续搜索并更新训练集。部署是否保留 search，则由
latency、optimality 与 verifier budget 决定，不能因为训练用过 search 就默认线上也支付同样的分支成本。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22221:start -->
Backtracking policy 还必须区分“当前 search state”与“到达该 state 的完整历史”。把整段 trajectory 交给模型保留了 provenance，却可能使两个相同当前状态因为不同历史顺序得到不同回退判断。更稳健的分层是：durable full trace 留给审计和 diagnosis，reactive policy 只消费 canonical current-state block，并用 same-state/different-history transplant 检查不变性。Selective State Attention 或 block-relative position 只改变 action proposal 的输入；search runtime 与 verifier 仍拥有 state transition 和 commit。

隔离历史可以减少伪相关，却增加 state localization、位置处理和训练复杂度，也不解决 state aliasing、隐藏前提或 proactive verification。现有实验只支持其披露的反应式搜索设置，没有证明 current-state text 完备，亦未证明预训练 LLM 能在生产中安全清空上下文。若 state reconstruction 或 aliasing 尚未闭合，应在策略输入之外保留完整轨迹，回退确定性 search checkpoint、显式 backtracking 或外部 verifier，而不是删除唯一的审计依据。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22221:end -->

上述训练期 teacher / 运行期 controller 分层用离线搜索和数据迭代换取更快的 runtime proposal，但会继承 planner domain、搜索启发式与生成计划的偏差。
训练计划通过也不证明开放环境中的 tool effect 正确；运行时 verifier 弱、环境部分可观测或代价可接受时，保留搜索
仍更稳健。现有证据限于 PDDL/Blocksworld/Logistics/Labyrinth/Sokoban 等可判定环境，不覆盖开放世界和不可逆副作用。

<!-- source-family:SF-2026-ARXIV-2605-03625 -->

在部分可观测环境中，固定 branching factor 也会浪费预算：某些节点只有一个可信方向，另一些节点存在
高 epistemic uncertainty。Planner 可以把“请求展开”显式化，并给整棵搜索树共享 leaf budget：

```text
current belief node
→ expose uncertainty / branch request
→ allocate bounded local alternatives
→ execute or simulate observations
→ prune by external evidence
→ return unused budget to global pool
```

自报 uncertainty 不是可信概率，teacher retro-annotation 也可能教会格式而非真实校准；因此 branching request
只能影响候选预算，不能绕过 policy、tool authorization 或 completion evidence。固定单路径在低风险、成本敏感
或 verifier 弱时仍合理；固定宽搜索在可并行且每个分支便宜时更可复算。动态 branching 只有在 uncertainty
calibration、global budget 和 branch-state identity 同时可观测时才有意义。

Tool 本身有价格、延迟或有限调用次数时，planning 还要把 information value 与机会成本放在同一个 belief state。
预先固定“最多 N 次调用”容易复算，却会在简单问题上浪费、在关键分叉前耗尽。Budget-aware planner 可在每一步估计：

```text
belief over task state
+ remaining cost / time / call budget
+ tool price, reliability and expected information gain
→ choose act, ask, verify or stop
→ update belief and remaining budget from observation
```

这不是把未知任务压成精确 knapsack。模型估计的成功概率和 information gain 可能失准，tool pricing、latency 与
version 也会变化；平均成本最优还可能牺牲 worst-case safety 或高价值少数请求。静态 budget 在成本稳定、风险高或
calibration 弱时仍更可靠。动态分配必须保留 hard cap、reserve for verification、stop/fallback policy，并按 task slice
校准实际 utility，而不是让 planner 用自己的主观置信度证明自己值得继续花费。

剩余预算不只是外层 hard cap，也可以成为 tree selection state。固定宽度或并行采样在分支便宜、critic 弱或
低 latency 依赖并行时仍合理；当不同路径共享前缀且 tool/output token 都昂贵时，planner 可以在每个 node 保存
累计 value、访问次数、父子关系和剩余资源，再根据资源收紧程度逐步从探索转向利用：

```text
node value + uncertainty + remaining multi-resource budget
-> widen / deepen / answer / stop
-> execute and observe
-> update path statistics and remaining budget
```

Critic call 自身也消耗 token、latency 与 cache，不能被排除在 budget 外；耗尽预算后强制回答只证明 termination，
不证明 correctness。Budget-Aware Value Tree 的作者实验支持这一控制面在其检索问答中改变 quality/cost frontier，
但其 deterministic positive-delta 等理论假设不适用于开放环境。多工具价格、deadline 与不可逆风险不能压成一个
无量纲比率；高风险或 calibration 弱时仍应使用静态上限、保留 verification reserve，并允许 abstain。

value target 也可以从当前树中的成功证据构造，而不把表示距离自动当作真实进度。一条受限分支将 dialogue-prefix hidden state 以 root 为参照归一后映射到 Poincaré ball，按到 root 与最近 verified-success leaf 的距离比例构造 potential，再让 value head 回归该 target、供 MCTS 选择与有限 latent 聚类剪枝。success leaf 是训练/搜索人口的必要输入，真实终局 outcome 仍决定 backup；没有成功证据或 hidden geometry 失准时，这个比例并不是可调用的 goal oracle。 [必要机制与几何对照](https://arxiv.org/html/2602.09375v1)。<!-- source-family:SF-2026-ARXIV-2602-09375 -->

同预算的有限几何对照支持它作为 value/search 替代接口，不认证语义距离、可靠 progress 或普遍长 horizon 优势。若边上定义 potential 差、随后沿路径聚合成单一 rollout reward，该和会望远镜化为端点差，不能从“dense”标签认定逐 step 真实 credit，也不能自动取得 policy-invariance 保证。树过滤人口、额外生成、tool 与 value 训练都要分账，部分任务仍反退；成功 leaf 稀疏、geometry/value 漂移或预算不足时，保留原 critic、可靠 outcome backup、固定搜索与 verification reserve。<!-- source-family:SF-2026-ARXIV-2602-09375 -->

目标已能用语言表达，也不必让同一个 judge 直接给整段 history 打进度分。另一条搜索评分分支把已观察事实与目标要求分别整理成 object、attribute 和 value：状态随真实 observation 更新，目标解释保留任务来源；再为每个目标实体比较候选实体的 identity 与属性值相似，聚合成可供候选排序的连续 proxy。它把信息抽取、实体/属性对齐与最终打分拆成接口，便于检查哪条要求没有匹配，但 LM 抽取和 relevance filter 仍可能漏事实，历史属性也会陈旧；目标与当前状态更像，不表示目标已经实现。

[受限因子化状态对照](https://arxiv.org/html/2603.09400v1)支持这一替代评分接口，不提供完整约束或环境真值证书。各目标独立选最大相似，可能重复占用同一实体或把不同属性错配；均值也不是全部条件同时满足，须另验对象数量、关系、否定、时序和真实 terminal outcome。轨迹相关型评价不认证绝对 reward 校准，部分非科学文本任务的误差仍高于直接 judge，在线增强又增加候选提案与预测/评分调用，不能单独归结构或继承同预算收益。状态/目标抽取、所有 embedding 比较、候选与 world-model forward、真实工具和回归均计费；匹配失准、事实不可核或预算不足时，保留直接 judge、原 critic、可信 symbolic check 与真实 outcome backup，不让语义 proxy 提交环境事实。<!-- source-family:SF-2026-ARXIV-2603-09400 -->

在离线 goal-conditioned value 学习中，几何还可以约束训练目标，而不仅给树构造 potential。一条分支用随机邻域内 target-network value 的 Monte Carlo 均值，对当前 value 超过允许 cost 偏差的部分施加 one-sided penalty，并与原 TD 目标共用；它避免显式求高阶梯度，却把邻域、表示与 cost 假设引入 critic。[Physics Informed Viscous Value Representations 的受限对照](https://arxiv.org/html/2602.23280v1)中原表示平均34→30，VIB35→45、Dual41→48，不能承袭表示无关改善。hierarchy仍决定可达性：point-stitch-large DualFK30低于EIK55，humanoid-giant HIQLFK4低于EikHIQL68，regularizer不是通用 hierarchy 替代。<!-- source-family:SF-2026-ARXIV-2602-23280 -->

训练、随机邻域估计、64-anchor BFS与表示构造增加费用；四seed支持这些任务的有限对照，15/50 episodes评价口径冲突不合并成总体效应，硬件、精度和墙钟未披露。Gaussian扰动没有有界范数，仅缩小系数不保证从未越界；本处不采用“kinematically valid”、完整PDE最优性或真实物理安全保证，也不据公式猜测实现有bug。表示空间失配、长程stitch退步或费用不合算时，应保留原TD、经核的Eikonal/层级策略和真实outcome验收，不把几何prior当环境oracle。

搜索目标还决定 value 应该累加什么。若一次任务只交付搜索中找到的最好程序，累计所有中间 reward 会偏爱多次一般改善，却不一定选出最终最好结果。一个受限代码优化分支冻结 code generator，只训练 value model；它把历史最好折扣 reward $u$ 加入状态，以未来路径上的最大折扣 reward $\hat G$ 构造 $V(s,u)=\mathbb{E}[\max(u,\hat G)]$，而不是累计 reward 的 sum。这个 best-so-far 状态使 critic 的目标与“预算内交付最好候选”相接，generator 本身并没有因此成为已更新的策略。<!-- source-family:SF-2026-ARXIV-2601-05475 -->

[最大回报 critic 与受限代码评价](https://arxiv.org/html/2601.05475v1#S2)通过单路径采样构造训练目标，再在 beam search 中使用 learned value；搜索分布改变会造成 critic 失配，原对照也包含最大回报目标不如累计目标的配置，不能授通用最优选择。程序 reward 仍依赖真实编译/执行、硬件性能与测试，critic 的自然语言诊断和推断也消耗预算；测试通过不是开放任务的普遍正确性。低预算、critic 校准不足或执行代价吞掉收益时，继续使用直接生成、真实测试与静态搜索上限合理，不能把相同候选数当成相同端到端成本。

跨尝试 replanning 还可以把 planner history 从自然语言反思提升为可审计 path state：operation DAG、结构 prior、
execution count、observed return/error 与 environment revision 分开保存。Macro path 能减少 token-level search，
却会漏掉未建模操作；UCB-like statistics 依赖 reward stationary，derived advice 还可能固化 parser/judge error。
Deep Tabular Research 的受限证据支持 execution feedback 与 path statistics 可以共同驱动 replan，不证明多数投票
消除相关错误。干净 schema/短查询继续适合 direct execution；新颖一次性任务在历史不可靠时应回到 stateless
search，任何跨 query state 都必须防止 tenant 污染和 benchmark-order leakage。

当搜索还会修改策略 prompt、评价 criteria 或全局经验 bank 时，只冻结环境 revision 已不足以维持 path statistics 的同一语义：同一个 action 的 pairwise 胜负、访问次数和累计 value，可能分别来自不同策略与 judge/context 人口。一个受限分支把成对比较转换为相对排序，再让经验反馈参与后续 MCTS 选择；这些胜率不是任务正确概率，prompt 与经验 bank 联合变化的收益也不能归因于 memory 单一机制。[必要方法与反侧](https://arxiv.org/html/2602.04248v1)支持这条经验驱动的搜索分支，而不支持所有指标同时改善。部署时应把策略、judge/criteria、比较样本及 context/bank snapshot 绑定到统计版本，在一段统计积累期间冻结其身份，或对变更前统计失效、重估；这是审计合同的工程推导，不是原实验已验证的通用实现。成对 judging、bank 更新和重新搜索都消耗预算；评价漂移、历史样本不具可比性或剩余预算不足时，回退固定 criteria、独立终局验收与 stateless search，不把旧 UCB value 当作更新后策略的可靠证书。<!-- source-family:SF-2026-ARXIV-2602-04248 -->

### 先校准不确定性，再决定行动、询问或探索

成本感知 planning 的关键并不是让模型输出一个置信度，而是把 prior、可获得 observation、action cost 与错误后果绑定到同一 decision contract：

```text
calibrated prior over task state
+ expected information gain of ask / explore
+ action, delay and failure cost
→ act / ask / gather evidence / defer
→ update belief from an observed outcome
```

合成环境中拟合的 prior 不能直接当作生产概率；cost 也不只是 token 数，还可能包括用户中断、工具价格、延迟与不可逆副作用。因此 expected utility policy 必须受 hard safety override、预算上限和低置信 fallback 约束，并按 deployment slice 重新校准。固定 rule 在样本少、概率失准或风险极高时继续合理；Calibrate-Then-Act 只为受控低维任务中的 uncertainty/cost-conditioned exploration 提供实验性证据，不证明现实 Agent 已获得全局最优行动策略。

### 局部 Replan 后必须回归全部已接受约束

Feedback-conditioned planning 若只修复本轮新暴露的问题，容易破坏先前已满足的 world、user 或 policy constraint。
Planner 因而需要一份带 authority、valid-time 和 provenance 的 cumulative ledger，并在每次 plan revision 后重新
验证全部仍有效 invariants：

```text
new observation / user clarification / policy feedback
→ append or supersede typed constraint
→ produce a new plan revision
→ regression-check every active constraint
→ execute only after global evidence passes
```

Ledger 减少重复违反，却增加 conflict、staleness、token/selection cost 与 oracle dependence；world fact、user
preference 与 immutable policy 也不能由同一 judge 随意改写。一次性 planning 在约束完整稳定、交互预算低时仍
合理。AdaPlanBench 的 text-only household simulator 只支持“terminal constraint-valid 不等于 plan effective”以及
局部 repair 会回归的受限证据，不证明 text plan 已在真实环境成功执行。

Active-constraint ledger 保存已接受的约束，却不能替代尚未解决的澄清承诺。Planner 若已识别缺信息，可以维护带 item ID 的可变 question pool，让每项在提交前获得 asked 或显式 drop disposition；pool 非空时阻止最终提交，避免自由文本计划在后续推理中悄悄遗失问题。这只保证显式 accounting：初始 pool 可能不完整，drop 理由、用户回答与问题映射仍须独立核验，不能把移除视作已获得真值。

持续更新、额外提问和 pool 操作增加用户中断与 token 成本；预算耗尽时应保留 unresolved 项、请求升级或停止，而不是为过门任意 drop。[PlanPool 的受限实验](https://arxiv.org/html/2610.02739v1)的 BIRD 对照限于经 oracle clarification 筛为可解的子集，并由同一模型家族扮演 Agent 与用户；groundedness 是对已标 ambiguity 的映射指标，增强它不必提高执行正确率。条件已齐或用户不允许交互时，一次性计划与独立最终 verifier 仍然合理。<!-- source-family:SF-2026-ARXIV-2610-02739 -->

求助还应把 when 与 how 分开：timeout 或固定失败次数可以决定何时交还人类，一个学习模块则只优化如何描述目标、失败状态与所缺信息，返回指导再由独立 planner 转成上下文或声明的动作。[受限具身分支](https://arxiv.org/html/2602.22546v1)的触发仍是固定规则，学得的求助表达来自 MuSiQue/search 替代反馈的 GRPO，不是 Minecraft 中自主学会求助时机；escape 动作也只是预定义恢复，不能让 human response 自签可执行真值。提高失败阈值会延迟求助，部分难任务因此失败、波动增加；有限任务与有经验参与者的改善不证明所有 Agent 必须交互，信息量、用户分配和重复预算亦未完全隔离。求助训练、用户中断、问答与返回指导的验证都付费，问得更清楚不免除 goal/policy/actuator gate；帮助不可验证或时限不足时，回退 log-only 求助、固定人工 milestone、保守恢复或明确停止，而不是继续消耗重试。<!-- source-family:SF-2026-ARXIV-2602-22546 -->

## Goal、Constraint 与 Policy

用户 goal 不等于无限授权。Planner 必须接收不可变 constraints：

- allowed tools/scopes；
- data/tenant boundary；
- time/token/cost budget；
- approval requirements；
- forbidden side effects；
- SLO/deadline。

模型可以选择满足约束的路径，不能在“任务需要”时自行放宽约束。Policy enforcement 位于 executor/workflow。

### 从 Project Brief 到可验证 Task Contracts

一句 project brief 直接 fan-out 给多个 executors，容易产生重复工作、遗漏、共享 asset 冲突和贡献边界模糊。
自然语言 decomposition 只有在被编译成带 identity 的 task contracts 后，才成为可执行协作接口：

```text
project goal / constraints
→ innovation atoms and dependency lineage
→ compare decomposition strategies
→ task contracts: objective, boundary, owner, inputs, outputs, shared assets, order
→ execution evidence
→ repair graph without silently changing accepted constraints
```

Planner 拥有分解与 dependency graph，executor 只拥有被授予的 task，Workflow 才拥有 durable commit/retry。
Contract 过细会压制探索，过粗则重新引入 overlap；LLM judge 对 coherence 的评分也不能替代 artifact integration。
Project2Task 的 10 个 research briefs 只为该编译结构提供实验性证据，不证明一般科研质量。单人任务、强耦合探索
或目标仍高度不确定时，共享 working session 与少量人工 milestone 仍比过早 taskization 更合理。

## 完成证据与 Verification

每一步需要 machine-checkable evidence，例如 test pass、resource state、signed response、human approval。模型说“已完成”不是完成条件。

对于无法自动验证的开放任务，可使用 rubric、多样化 reviewers、sampled human review 和 uncertainty escalation，但要标明仍是经验判断。

长程任务的 subgoal 不应只是自然语言分解标签，而应成为可验证 milestone：每个 milestone 绑定 expected
state、checker、supersession 和完成证据；环境 observation 触发 replanning，milestone progress 还可作为
受限训练信号。这样把稀疏终局反馈前移，却新增错误 checker、过早终止和为了 milestone 得分而偏离最终目标。
任务短、状态不可可靠检查或 action 不可逆时，少量人工 checkpoint 与 approval 仍比自动细分更稳健。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21260:start -->
对可获得 oracle trajectory 的受控环境，可以把实际 trajectory 与 oracle 的 mismatch 分解为 planning risk：错误
来自目标路径本身、局部 action 偏离，还是误差沿 horizon 传播。这个分解让 verifier 定位哪一段 plan 需要重建，
却依赖 oracle 与环境模型完整；理论上下界和作者环境不证明开放世界任务完成。oracle 不存在、状态部分可观测或
不可逆动作占主导时，应回退真实 outcome、保守 milestone 与人工 approval。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21260:end -->

完整成功计划作为示例在任务同质时直观，却可能让长 trace 隐藏是哪一个局部操作违反约束。可在离线训练题上用独立 oracle 定位第一处违规 transition，仅把函数名、输入与正确输出作为 primitive 示例更新 prompt；测试时仍由模型按 specification 执行，不再提供训练 oracle。它把反馈粒度从整条轨迹收窄为局部 IO，并未给模型真正的可执行实现，也不能用局部示例通过证明 terminal success 或 optimal。Oracle 覆盖、train/test 隔离与示例 budget 需分别保存，状态跟踪或搜索未改对时仍失败；没有可信局部 oracle、任务不可分解或约束相互作用强时，保留 whole-plan 示例、明确 ledger 与独立终局验证。<!-- source-family:SF-2026-ARXIV-2602-00276 -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20122:start -->
ScaffoldAgent 将 deep-research outline 变成可迭代控制状态：每轮按预期 utility 增删/重排子目标，再据证据覆盖继续搜索；planner 拥有 outline version，budget 用尽则冻结当前结构并交给 verifier。代价是 utility 估计会偏向易检索证据。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20122:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20978:start -->
PbD pipeline 不把录制动作平铺给 agent，而先按命名 subgoal 建层级，再保持相同 action sequence 供 planner 消费；demonstration owner 保存 grouping，描述已精确时可回退无示例。代价是人工/自动分段错误。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20978:end -->

### Rollout 预算应投向边际信息，而不是均匀扩树

均匀扩展 search tree 容易在相似分支上重复消耗 tool call。预算受限时，可以把候选 rollout 看成覆盖不同 failure/evidence region 的集合，按边际信息增益选择下一分支。它提高有限预算下的多样性，却依赖相似度与价值估计；代理目标失真会系统性漏掉稀有路径。

因此 selector 必须保留随机探索、预算水位和 coverage receipt。任务小、branching factor 低时，简单 breadth/depth search 仍更透明；只有候选高度冗余时，信息分配才值得承担估计与调度成本。

<!-- source-family:SF-MAXIMIZING-ROLLOUT-INFORMATIVENESS-UNDER-A-FIXED-BUDGET-A-SUBMODULAR-VIE -->

### Planning 能力要区分 Acquisition、Shaping 与 Integration

长程 planning 失败可能是模型从未获得基本 transition 能力，也可能已有能力但搜索/反馈没有塑形，或多个教师/阶段产生不兼容策略。受控环境应分别测：能否学习局部状态转移，额外 feedback 是否改变规划路径，以及不同来源能力合并后是否保持可执行的一致 plan。

这种分解提高诊断力，却依赖环境“物理规律”和任务设计，有限实验不能给出开放世界能力结论。若基础 acquisition 未通过，不应靠更长 search 掩盖；若 integration 冲突，则回退单一已验证 planner/teacher，并在 state-transition 与 outcome 层分别验收。

<!-- source-family:SF-2026-ARXIV-2607-24720 -->

### 环境的排序不应改写用户目标

真实网站即使没有注入恶意指令，也可能通过赞助排序、促销框架、延迟披露价格等机制推动自己的目标。Planner 若把“先看到”误作“用户更想要”，会先改写偏好、再缩小搜索，最后在关键成本尚未核齐时提交不可逆动作。受托决策因此应先冻结用户约束和比较准则，保留候选集合的覆盖证据，并在购买或其他有副作用的 commit 前由独立检查核齐决定性字段；外部页面只提供事实候选，不拥有目标函数。代价是额外探索、页面读取和验证延迟。受控市场基准的 matched-control 对照支持这种 failure path，但其唯一最优商品、固定引导方式和有限跨域测试不能证明一般商业环境的防护效果；低风险、可撤销且目录透明的任务仍可用简短搜索。<!-- source-family:SF-2026-ARXIV-2609-27273 -->

## 本章在知识树中的位置

Tool Calling 定义单次 action contract，Planning 组织多个可能 action。下一章研究 Reflection：当 observation 或 verifier 暴露缺陷时，系统如何产生反馈并修正，而不是无限自我批评。

第25章的 World Model 可以为本章生成 imagined rollouts；第26章的 controller 仍独立拥有 physical action authority。Planner 选择模型内高分轨迹不构成执行许可，必须经过 uncertainty、policy、freshness、safety envelope 与真实 observation reconciliation。

## 从机制演进到系统设计

Planning 从一次性计划文本演进到可执行、可修正的搜索状态。节点要绑定前置条件、环境观察、候选 action、commit point、预算和 verifier；test-time search可以动态扩展候选或分配 thinking time，但只有环境证据才能提交下一状态。

更多搜索提高找到可行路径的机会，却增加延迟、branch explosion、stale observation 和 verifier bias。deadline、风险或工具成本越界时应缩短 horizon、选择保守 plan 或交还 Workflow/人工；固定流程在环境稳定时仍比开放搜索更可预测。

## 自检问题

1. 步骤列表为什么不是可执行 plan？
2. 部分可观测性如何改变 planning？
3. Decomposition 过细会引入什么成本？
4. Replanning 应由哪些事件触发？
5. Tree search 的调用成本怎样增长？
6. 为什么模型不能自行修改 constraints？

## 小结

Planning 把 goal 转成带依赖、前置条件和证据的可修正状态图。它的可靠性来自 execution observations 与外部 constraints，而非计划文本的流畅度。下一章进入反馈和修正。

### Decomposition Language 让计划成为可执行状态机

自由文本计划易生成，却难确定哪一步完成、何时修改目标以及哪些 reasoning threads 可以并行。受约束 decomposition
language 可以把目标、子任务、依赖和 revision 编译成可执行状态，由 planner 提议 graph、executor 提交 transition、goal
owner 批准目标变化。这样提高可重放性，却增加语言设计、token 成本与不适配开放任务的风险；分解不稳定或任务短小时，
简单 ReAct/单循环仍更合适。DOLORES 的证据限四个 reasoning benchmarks、三个模型与作者受控分解。

<!-- source-family:SF-2026-ARXIV-2605-11388 -->

### Tool Graph 可以进入模型表示，但 Runtime 仍拥有 Legality

把完整 tool DAG 每次序列化进 prompt，透明但昂贵，早期选错后也可能进入非法 graph state。静态图可被编码进专用 graph token，并用 on-policy samples 学习当前 policy 的漂移；模型因此更快提出 plan，但 dependency、permission 和 effect commit 仍由外部 workflow/runtime 验证。内部化减少 prompt 搬运，却增加 tokenizer/model coupling、graph versioning、retraining 和错误不可观察性。图动态变化或置信不足时，应回退 external typed DAG、constraint checker 与 stepwise replan。exact-v1 只支持所测静态 tool graph 和 legality 指标，不证明真实工具成功或权限安全。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11706 -->

### 内部 State 只能建议 Planning Mode

低维内部 state 可以作为“探索、执行、复核”模式切换的 sensor，帮助 controller 分配预算；它不拥有答案正确性、工具授权或最终 commit。mode detector、模型 revision、trajectory slice 与外部 verifier 必须共同校准。<!-- source-family:SF-2026-ARXIV-2609-16245 -->

冻结模型和有限 research trajectory 只支持受限可读性；模型特化或误判会把合理探索提前终止。信号不稳时回退显式 workflow、固定预算和外部 verifier。

## Review notes

- `SF-2026-ARXIV-2603-10747` — Daily补查 `2026-03-13`；[Pneuma-Seeker exact-v1](https://arxiv.org/html/2603.10747v1) §3–7与完整Tables1/2。mar13_supplement准备，非准备者mar13_admission_review实际回原证、1+2+2=5/Ch79具体目标关系与答案程序差额、完整编译/predicate/Goal邻接通过；root读完整回执与现章后，仅窄写两段，并将“证明”准确化为“展示”。不借SQL/DAG成熟原理抬分，不采同稿题名差异为新家族或PVLDB模板为发表事实；耗尽强制回应、LLM语义列、组合消融、有限人口及时间/内存反退近文。非writer mar13_admission_review实际顺读新增、完整编译/predicate前后分支和本人末注，并回对必要原证，POST通过；root核回执和当前正文后释放本项窄锁，不授DAY、实际代码/复现或普遍完整性。

2026-03-12增量：2603.09400 exact-v1，采用状态/目标因子化softmatch评分接口，不采用真值、完整约束或普遍规划保证。作者必要§2–4/Table1–2、B/C4/C6；root必要Source/date/逐字PRE通过，实际两段写于LaPha后/Physics-informed前，root非writer已顺读两段、完整局部邻接及本末注并回对有效原证，actualPOST通过。独立max/非injective、Pearson非校准、真实反侧、历史state陈旧与全费用保留；未核全图/代码/复现。<!-- source-family:SF-2026-ARXIV-2603-09400 -->

- `SF-2026-ARXIV-2602-22546` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22546v1)，fixed when/learned how与returned guidance执行权限。2+2+2=6，具体owner差额深入；限制、反侧、完整费用与原分支回退近正文。root实际必要原源/owner PRE通过并授单段窄lease；作者正文/完整邻接/自身末注已顺读，root非作者实际正文/完整邻接/自身末注POST通过。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-05475` — Daily `2026-01-13`；[MaxCode exact-v1](https://arxiv.org/html/2601.05475v1) §2.1/2.3、§3及最大目标不如累计目标的反侧。只采用冻结generator、best-discounted状态与max-value目标；单路径到beam失配、真实执行及critic成本保留，测试不授开放correctness。未复现；root 必要源/当前owner写前通过，root实际新增正文/前后衔接及末注写后复核通过。

- Daily 2026-03-07：[Pri-TPG exact-v1](https://arxiv.org/pdf/2603.04852v1) §3、§4.1/4.3 Tables3/6与§5limitations。Table3同GPT5mini/iterative executor、1400 GT形式输入/600s，RAG72.64与RAG+TPG84.42、Hard22.95与40.98；只采用覆盖≠顺序的受限反证，不采一般推理普胜或真实视觉输入证明能力。K检索支持、多次calls与局部依赖≠全局深度保留；root准入/窄锁已核，作者实际写入，root实际原文/正文及邻接独立POST通过，未复现。

- AdaPlanBench（cumulative constraint ledger；Status: Experimental）: https://arxiv.org/abs/2606.05622

本章不把 hidden reasoning 当作 durable workflow state；第 81 章拥有持久执行和重试。ReAct/Tree of Thoughts 作为经验机制，结论不外推到所有模型和任务。

Primary-source 入口：

- ReAct: https://arxiv.org/abs/2210.03629
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- Chain-of-Thought prompting: https://arxiv.org/abs/2201.11903
- SPARK（uncertainty-triggered bounded branching；Status: Experimental）:
  https://arxiv.org/abs/2601.20209
- DeepPlanning（constraint-rich closed-world planning evaluation）:
  https://arxiv.org/abs/2601.18137
- INTENT（budget-constrained costly-tool planning；Status: Experimental）:
  https://arxiv.org/abs/2602.11541
- Calibrate-Then-Act（prior-calibrated cost-aware exploration；Status: Experimental）:
  https://arxiv.org/abs/2602.16699
- Search More, Think Less（dependency-aware parallel evidence acquisition；Status: Experimental）:
  https://arxiv.org/abs/2602.22675
- LongVideo-R1（hierarchical active-perception planning；Status: Experimental）:
  https://arxiv.org/abs/2602.20913
- TAPE（plan feasibility 与 execution conformance 分层；Status: Experimental）:
  https://arxiv.org/abs/2602.19633
- Subgoal-driven Long-Horizon Agents（verifiable milestones；Status: Experimental）:
  https://arxiv.org/abs/2603.19685
- Project2Task（project brief 到 task contract；Status: Experimental）:
  https://arxiv.org/abs/2608.05225

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-27806 — primary arXiv:2606.27806v1; exact-v1 URL=https://arxiv.org/html/2606.27806v1; Method=https://arxiv.org/html/2606.27806v1 — §Our approach: GILP.; LLM API ecosystem.; 4 Method: Grounded Iterative Language Planning; Evaluation=https://arxiv.org/html/2606.27806v1 — §5 Experiments; Setup.; Cost analysis.; Non-proof=https://arxiv.org/html/2606.27806v1 — §6 Discussion; 7 Limitations; 8 Conclusion。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22948` — primary `arXiv:2606.22948v1`; Method=`arXiv:2606.22948v1 — §5.1 Experimental protocol; §Appendix C Evaluation pool construction`; Evaluation=`arXiv:2606.22948v1 — §4.3 Train/evaluation split; §Appendix C Evaluation pool construction`; non-proof=`arXiv:2606.22948v1 — §6 Conclusion`; fallback=该 family 的 failure pressure 是：As multimodal agents move from interface understanding to real software control, successful trajectory discovery in live desktop environments becomes a key challenge. 披露的 evaluation signal 是：To evaluate robustness under realistic desktop interruptions, we also introduce OSWorld-Noisy, a dynamic benchmark for recoverable desktop interruptions that preserves the original tasks while testing whether agents can refocus, dismiss, wait, or recover under live perturbations. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25274**：Primary `arXiv:2606.25274v1`；Method `https://arxiv.org/html/2606.25274v1 — §3 Problem Definition; 4 Method; 4.2 Candidate Expansion; 4.3 UC-Beam`；Evaluation `https://arxiv.org/html/2606.25274v1 — §5 Experiments; 5.1 Implemented Evidence; 6 Analysis`；未证明边界 `https://arxiv.org/html/2606.25274v1 — §7 Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26463**：Primary `arXiv:2606.26463v1`；Method `https://arxiv.org/html/2606.26463v1 — §Variable-delay real-time RL; lightweight gate selects state-dependent planning budget`；Evaluation `https://arxiv.org/html/2606.26463v1 — §Pac-Man, Tetris, Snake, Speed Hex and Speed Go evaluation`；未证明边界 `https://arxiv.org/html/2606.26463v1 — §Game planners and timing model do not prove benefit under production tool latency or safety deadlines`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-14574:start -->
- `SF-2026-ARXIV-2606-14574` — Daily `2026-06-13`；primary `arXiv:2606.14574v1`；Books review `books-review:SF-2026-ARXIV-2606-14574`。

  **已吸收的语义增量：** Executable planning evaluator 必须让 symbolic world model 区分 immediate precondition failure、latent hazard 与 irreversible failure，并在 action commit 前运行 counterfactual foresight。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14574:end -->


<!-- daily-books-trace:SF-2026-ARXIV-2606-20122:start -->
- `SF-2026-ARXIV-2606-20122` — Daily `2026-06-19`；primary `arXiv:2606.20122v1`；Books review `books-review:SF-2026-ARXIV-2606-20122`。

  **已吸收的语义增量：** `ScaffoldAgent: Utility-Guided Dynamic Outline Optimization for Open-Ended Deep Research` 路由到 `AGENT-PLANNING`：ScaffoldAgent 将 deep-research outline 变成可迭代控制状态：每轮按预期 utility 增删/重排子目标，再据证据覆盖继续搜索；planner 拥有 outline version，budget 用尽则冻结当前结构并交给 verifier。代价是 utility 估计会偏向易检索证据。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20122:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20978:start -->
- `SF-2026-ARXIV-2606-20978` — Daily `2026-06-19`；primary `arXiv:2606.20978v1`；Books review `books-review:SF-2026-ARXIV-2606-20978`。

  **已吸收的语义增量：** `How Should Agents Read Demonstrations? Hierarchical Structure Beats Flat Action Logs` 路由到 `AGENT-PLANNING`：PbD pipeline 不把录制动作平铺给 agent，而先按命名 subgoal 建层级，再保持相同 action sequence 供 planner 消费；demonstration owner 保存 grouping，描述已精确时可回退无示例。代价是人工/自动分段错误。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20978:end -->

<!-- daily-books-trace:SF-2026-PARASON:start -->
- `SF-2026-PARASON` — Daily `2026-08-26`；primary `arXiv:2608.24658v1`；Books review `books-review:SF-2026-PARASON`。

  **已吸收的语义增量：** 新增两类 parallelism 的 merge/cancel/commit、budget ownership 与单路径共存边界。
<!-- daily-books-trace:SF-2026-PARASON:end -->

- `SF-2026-ARXIV-2512-24077` — Daily `2026-01-02`；[LoongFlow exact-v1](https://arxiv.org/html/2512.24077v1) §4.1.1/Algorithm1及§5.4。5分针对具体知识缺口深入受影响机制，采用parent-ID plan/summary反馈归属与fast-fail/full-evaluator分层；不计MAP-Elites/PES组合、Kaggle/科学奖牌，不称文本summary为causal事实。未运行公开代码或复现实验；root非作者已实际核必要原源、两段正文及前后衔接，写后通过。

- `SF-2026-ARXIV-2602-00276` — Daily `2026-02-04`；[L-ICL exact-v1](https://arxiv.org/html/2602.00276v1) §3–4/6。5分针对反馈粒度知识缺口深入受影响接口，只采用training oracle→first-failure函数/输入/正确输出→离线prompt与test无oracle分工。PTP只有spec而非实现，valid/success/optimal分开；Alg1 P0/batch与iterative prose、2k/5k/7k及89%/63%协议表述冲突不拼接为性能点，不授约束或终局保证。未复现实验；root必要原源/当前owner写前通过，root实际正文及前后交接写后通过，日级Gate通过。

- `SF-2026-ARXIV-2602-04248` — Daily `2026-02-06`；[Empirical-MCTS exact-v1](https://arxiv.org/html/2602.04248v1) §3–5/7。原2+2+2=6，具体策略/judge/context变化与MCTS统计绑定gap深入；BT/Borda/Normalized Dominance为相对比较，UCB选择不改写成softmax，Table2非全Pareto。prompt与bank联合变化不授memory单一因果；snapshot/invalidation为工程推导，未称原实现已验证。未运行代码/复现；jan01_v3实际必要原源/owner写前通过，root授窄锁；root实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2601-08955` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.08955v1) §3.1/3.3.1–2、4.3–4.4及Limitations。6分对state-conditioned imagination horizon的具体知识缺口深入，采用teacher-forced expert/冻结WM的伪K→action/K warmup→联合A2C控制分支；likelihood减K罚是proxy，episode token非wallclock/费用/训练成本，未采用通用最优horizon或物理/OOD安全。root实际必要源/owner写前通过，新增两段、transition/Decomposition前后与末注实际非作者POST通过；未运行代码或复现实验。

- `SF-2026-ARXIV-2601-09097` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09097v1) §3.1–3.4/4–6/Table2/Limitations与B/C/E必要片段。6分compiled-domain/每query参数接口具体gap深入；单例校验不授全域完备或无过拟合，建模遗漏、heldout/version与offline摊销成本相邻；sampling/enumeration消融不作单模块归因。root必要源/owner写前通过，root实际两段/前后与末注非作者POST通过，锁释放；未运行artifact或复现。

- `SF-2026-ARXIV-2601-09446` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09446v1) predicate-first方法、LM arity repair、Table2及数据/限制。2+1+2=5，声明签名→translation→repair proposal→parser/solver具体接口gap深入；coverage自一致不授语义faithfulness，过滤人口和多pass prefill成本、反退/回退近正文。未运行代码或复现；root实际必要源/owner写前通过，root实际正文169/171、153–182前后及末注524非作者POST通过，窄锁释放，非日级验收。

- `SF-2026-ARXIV-2602-09375` — Daily `2026-02-12`；[LaPha exact-v1](https://arxiv.org/html/2602.09375v1) §2.1–2.4/3 Table2/A配置。2+2+2=6，具体owner差额深入：root/verified-success potential作value/search；几何非进度，聚合差分非真实stepcredit/一般policy-invariance；未核实现或复现。必要source独立通过、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2602-10390` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10390v1) §3–5 fixed-task-distribution与full-support混合分支；communicating/deterministic/fixed-length条件及调用反退保留，不采用一般epsilon最优/LLM regret保证。root必要源与实际owner PRE通过，具体差额受影响深入；实际正文/完整邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-16699` — Daily `2026-02-20`；[Calibrate-Then-Act exact-v1](https://arxiv.org/html/2602.16699v1) §3、§5 与必要 B/C 配置。2+1+2=5，环境 prior estimator/action selector 接口差额深入；全体检索质量非 query-specific 真值，synthetic unit-test 非任意代码 verifier，discount reward 非费用/SLO，accuracy 反退与校准成本近正文。不采用一般最优停止或无损收益。root 必要源/实际 owner PRE 通过；root非作者实际正文/完整邻接/自身末注 POST通过，窄锁释放；未运行 artifact 或复现。

- `SF-2026-ARXIV-2602-17622` — Daily `2026-02-21`；[What Makes a Good LLM Agent exact-v1](https://arxiv.org/html/2602.17622v1) §4.3–4.4、§5.1/Table6/§6.1。2+2+2=6，typed precondition变更后恢复pruned支持集差额深入；heuristic非sound/complete/授权、mean-best报告冲突/cumulative组件/tool差异、walkthrough与外部假证据/调用费用及宽搜索回退近正文。root必要原源/actualowner PRE授窄锁；作者实际正文/完整邻接/ownnote顺读，root非作者实际195、完整185–207/own548 POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22583` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22583v1) §3–4/必要控制，2+1+2=5；source频率与目标hint可执行性分账，模型/协议绑定、source反转、judge代理及试用/校准全费用近文。fresh非旧作者独核prepared原证与actual owner，root授该窄ownership；作者实际正文/完整邻接顺读，root非作者实际正文、完整邻接及自身末注POST通过，窄锁释放。未核代码/复现，非日级Gate。

- `SF-2026-ARXIV-2602-23242` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/pdf/2602.23242v1)必要pp2～7/§3–4.4，2+1+3=6；fresh非旧作者独核原PDF/actual owner与包26差额，phase-return/理想onpolicy与offpolicy分责深入。grain-of-truth/正prior/探索、τ/M/H/N条件、reflective oracle非部署与旧日志反侧近文；root授Ch79窄ownership，作者实际正文/完整邻接顺读，root非作者实际正文87、完整78–105邻接与自身末注560 POST通过，窄锁释放。未授全appendix证明或有限实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-23280` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23280v1)，2+1+2=5；当前作者非原packet作者必要原源/actual owner具体差额深入，root once准入通过并授窄锁。作者实际正文/完整邻接/自身末注已順读；final_audit非原作者必要原源/actual owner独核通过，root非写入者实际正文/完整邻接/自身末注POST通过，窄锁释放；未核实现/复现，非日级。

- 2026-01-28 来源遗漏补查，arXiv:2601.18595v1：必要 Source 复用本日具名独核，root 实际正文邻接与逐字 PRE 通过后授本段及自身末注窄锁；已写入，resume_20260128_audit 非作者实际正文、完整局部邻接及自身末注 POST 通过（Ch31 段分隔亦已独核），窄锁释放。采用范围、直接反侧与回退近正文保留；未核 artifact/复现。<!-- source-family:SF-2026-ARXIV-2601-18595 -->

- `SF-2026-ARXIV-2603-07915` — Daily `2026-03-11`补查；[Ares exact-v1](https://arxiv.org/html/2603.07915v1) 必要101–177/497–498/640–724/734–803/1070–1096，Table1/2仅正文必要对照。2+2+2=6，step-local effort标签与trajectory outcome/费用的具体差额深入，档位penalty非token总费、筛选/重试/功能等价与effect权限分离、反退/全费用/旧路径近文。review_mar11_continue实际Source/Ch79 owner逐字PRE通过，root授原85完整段后单段+本人注窄锁；作者实际60–110局部（74–100输出缺口已补）与Ch78/80交接已读；新增正文已写，review_mar11_continue非writer实际完整正文/邻接与本人注POST通过，root已释放窄锁，不授DAY、实现核验或复现。
