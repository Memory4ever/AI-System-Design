# 第66章 Evaluation System

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-EVALUATION-SYSTEM`
**Legacy Chapter:** Ch62
**Status:** Draft

**Roadmap Intent:** 定义什么算有效能力，连接评估对象、数据集、scorer、运行证据、发布门禁与线上反馈；MLflow 作为 lifecycle evidence 的实现案例。

## 本章要回答的问题

为什么训练 loss、benchmark 分数、用户点赞和系统 SLO 都不能单独证明一个 AI System “更好”？Evaluation 应评估模型、完整请求路径，还是 Agent trajectory？离线评估、线上实验与生产反馈怎样形成一个可审计的发布控制回路？

本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**

> 时效边界：本章描述长期稳定的评估对象与控制回路，不把某个 benchmark、judge model 或平台 API 当作 Evaluation 的定义。MLflow 的实现映射按 2026 年 7 月官方文档核验；其 classic ML 与 GenAI evaluation 接口仍在演进，生产使用必须锁定实际版本。

为了避免把不同 benchmark 和 scorer 读成横向清单，本章沿四个不可交换的阶段展开：

```text
Claim contract
  intended use / subject / population / failure taxonomy
→ Evidence production
  dataset / environment / execution / artifact / trajectory
→ Measurement inference
  scorer / rater / uncertainty / slices / provenance
→ Decision and feedback
  gate / shadow / canary / release / rollback / next-version input
```

新评测只有改变其中某一阶段的对象、证据或控制权时才进入正文。多一个分数不等于多一层证据；同一证据也不能越过 measurement inference 直接获得发布权威。

## 为什么“选一个分数”不是评估系统

假设团队训练了新模型 `B`，旧模型 `A` 的 benchmark 得分为 78，`B` 为 81。朴素结论是发布 `B`。但这个数字没有回答：

- 测试集是否进入过训练数据？
- 三分提升是否来自某个高频 slice，还是所有关键场景都改善？
- prompt、tokenizer、retriever、runtime 和 sampling 是否与生产一致？
- scorer 测量的是格式、事实、任务成功，还是用户偏好？
- 结果方差有多大，重复运行是否稳定？
- 延迟、成本、安全和少数高风险失败是否恶化？
- benchmark 分布是否仍代表当前生产请求？

再把用户点赞作为标准，也会遇到新问题：愿意反馈的用户不是随机样本；推荐和路由策略改变了谁会看到结果；短期满意不代表事实正确；高风险失败可能数量少，却不能被平均值抵消。

问题不在于分数无用，而在于**任何分数都是在某个对象、分布、环境和测量方法下产生的条件性证据**。丢掉条件，只留下数值，评估就会退化为不可解释的排行榜。

## 从目标到证据，而不是从指标到目标

Evaluation 的起点不是“平台能采集什么 metric”，而是系统希望满足什么目标。可以把链路写成：

```text
intended use and risk
→ evaluation specification
→ dataset / environment
→ system execution
→ scorer / human judgment
→ aggregation and uncertainty
→ decision policy
→ release / rollback / investigation
→ production feedback
```

`intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明：

```text
EvalSpec =
  target behavior
  + eligible population
  + failure taxonomy
  + metrics and scorers
  + slice definitions
  + thresholds / comparison rules
  + uncertainty requirement
  + owner and review policy
```

如果目标没有被写清楚，团队往往会优化最容易计算的 proxy。模型变得更会迎合 judge，却未必更可靠；服务提高吞吐，却可能让 tail latency 和任务完成率下降。这不是模型“作弊”，而是控制系统给出了错误目标。

## 第一个不变量：评估声明必须绑定完整对象

AI System 的行为不只由 weights 决定。一次可复现的评估至少要绑定：

```text
subject_identity =
  model / adapter / tokenizer
  + prompt / policy
  + retriever / index / reranker
  + tool schemas and permissions
  + architecture / protocol adapter
  + runtime / decoding configuration
  + workflow / agent definition
  + environment version
```

不同评估层可以只改变其中一部分，但不能假装其余部分不存在。

例如，模型离线比较可以固定 prompt 和 decoding；RAG 评估必须把 index 与 retriever 放进对象身份；Agent 评估还需要记录 tools、sandbox、workflow、budget 和 environment。若只记录 `model_name`，同一模型搭配不同系统组件产生的行为会被错误合并。

尤其在通用 Agent benchmark 中，模型可能通过不同 provider API、tool-call parser、message template 或
architecture wrapper 接入同一环境。Protocol adapter 不是中性胶水：它会改变 tool schema、observation
serialization、retry 和 stop behavior。公平比较应验证 adapter 的 semantic equivalence，并把 adapter revision
纳入 subject；否则“模型差异”可能只是 harness translation 差异。General Agent Evaluation 的实验支持这一
对象边界，但不能证明一个 adapter 可对所有 provider 实现完全等价。

这也是第 35 章和第 59 章的接口：Checkpoint 提供可验证 artifact，Registry 提供不可变版本和 evidence references；第 66 章负责说明这些 evidence 是在什么评估契约下产生的。

## 第二个不变量：评估结论总是相对于分布

设系统为 \(f\)，部署输入与目标的联合分布为 \(P(x,y)\)，损失函数为 \(\ell\)。真正关心的是部署风险：

\[
R_P(f)=\mathbb{E}_{(x,y)\sim P}[\ell(f(x),y)]
\]

但平台无法直接枚举未来流量，只能在有限 evaluation set \(D=\{(x_i,y_i)\}_{i=1}^{n}\) 上估计：

\[
\hat{R}_D(f)=\frac{1}{n}\sum_{i=1}^{n}\ell(f(x_i),y_i)
\]

从 \(\hat{R}_D\) 推断 \(R_P\) 依赖至少三个假设：

1. 数据没有被训练或调参过程污染；
2. evaluation set 能代表 intended deployment population；
3. scorer 的误差与业务目标之间存在可接受关系。

数据量增大只会降低部分 sampling uncertainty，不能修复错误分布或错误 scorer。一百万条不相关样本不会比一千条关键业务样本更有决定力。

## 平均值、切片与不确定性

总体平均会把局部灾难隐藏在高频正常样本中。Evaluation System 应同时保存 per-example results、总体聚合和关键 slices：

```text
overall
├─ language / region
├─ input length / output length
├─ domain / task
├─ user or tenant class
├─ difficulty
└─ safety / high-impact risk
```

如果一个二元成功指标在 \(n\) 个近似独立样本中的成功率为 \(\hat{p}\)，朴素标准误差可写为：

\[
\operatorname{SE}(\hat{p})\approx
\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
\]

这个式子只提供直觉。真实评估常有同一 prompt 的多次采样、同源数据、用户聚类和时间相关性，样本并非独立同分布。此时应采用与采样结构匹配的 bootstrap、clustered analysis 或重复运行，而不是机械套用置信区间。

切片越细，样本越少、方差越大；切片过粗，又会掩盖风险。平台不应自动生成无限 dashboard，而应由 failure taxonomy 和业务风险决定哪些 slice 是 release-blocking，哪些只用于探索。

## 评估对象有四个层次

### Model Evaluation

固定系统外壳，比较模型本身的能力与行为，例如知识、推理、指令遵循、鲁棒性和安全。它适合模型选择，却不能证明完整应用可用。

### System Evaluation

评估 `model + prompt + context + retrieval + tools + policy` 的端到端结果。RAG 的 retrieval recall 与 answer groundedness、Tool Calling 的选择与执行结果，都属于这一层。

### Runtime and Service Evaluation

在目标硬件与 workload 下测量 TTFT、TPOT、goodput、错误率、容量、恢复和成本。质量相同但无法满足 SLO 的 artifact 仍不能发布；延迟更低但输出质量回归也不是有效优化。

### Agent and Outcome Evaluation

#### Skill 必须在真实 Control Path 中评估

把正确 Skill 强制塞进 Context 只测到 artifact 上界，不测 registry 的 selection、retrieval 与 adaptation。更完整
的 EvalSpec 应逐级增加 distractors、扩大 registry、移除 task-specific artifact，并记录 refinement 的额外探索：

```text
no Skill baseline
→ oracle artifact injection
→ selection among distractors
→ retrieval from production-scale registry
→ adaptation/refinement under missing coverage
```

Refinement 只能重组已有 evidence，不能从缺失知识中创造可靠 procedure；失败还可能低于 no-Skill baseline。
Agentic Skills in the Wild 的作者结果支持这一分层，不支持固定模型排名或特定 registry size 的通用结论。

#### Proactive Agent 必须同时测 Act、Silent 与 Stop

只奖励“主动完成”会驱动 Agent 过度行动；只测 intent recovery 又看不到 rejection 后是否停止。Proactivity 的
operating point 至少包含正确行动、应该沉默时不行动，以及用户拒绝/纠正后的停止。Deterministic side-effect
checks 与 soft preference judge 应分开，simulator identity、hidden profile、feedback history 和 policy revision
都属于 evaluation contract。KnowU-Bench 是 Experimental case；synthetic personas 与小规模 judge calibration
不能代表真实用户人口。

#### Tool 成功要从 Component 扩展到 Information Use 与 Outcome

Schema/action 正确不等于系统正确使用 tool result。Evaluation 应分开 action correctness、redundancy/efficiency、
process quality、information utilization、output evidence 与 domain outcome；component tests 继续负责低成本定位，
trajectory/outcome gate 才决定发布。FinTrace 在其金融工具集上支持这种 ladder，不提供跨域指标权重或通用 judge。

评估多步 trajectory、环境交互和最终副作用。除 final task success 外，还要检查：

- 是否选择了正确工具与参数；
- 是否遵守权限、预算和 approval；
- 中间事实是否可追溯；
- 重试是否产生重复副作用；
- 是否能在失败后恢复或安全停止；
- 成功是否来自环境泄漏或 verifier 缺陷。

四层不是四套互不相干的平台。它们共享 subject identity、dataset/environment version、run、result、trace 和 decision contracts，只是 scorer 与风险不同。

Document Agent 还应把 retrieval、navigation、grounding 与 effort 分开。只报告 final answer accuracy，会让更多
tool calls 掩盖低质量 first action，也无法区分 document miss、page miss、visual parsing、cross-document synthesis
和 answer extraction。一个可诊断 contract 至少保存：

```text
corpus / document snapshot
-> retrieved document and page evidence
-> navigation actions and tool-call budget
-> grounded answer / attribution
-> failure stage, latency and cost
```

Oracle retrieval 分支可以定位瓶颈，却不是生产系统成绩；增加 step budget 可能改善 coverage，也会制造循环与成本
尾部。MADQA 的受限 PDF collection 支持 `accuracy x grounding x effort x failure stage` 比单一正确率更有诊断性，
不证明其语料、模型排名或 tool budget 可外推到企业私有、多语言环境。Corpus 小、retrieval 稳定时 static RAG
仍更可控；多步 Agent 只有在 action trace、evidence provenance 与 refusal/recovery 一起评估时才增加可信度。

### 可靠性是分层画像，不是成功率的别名

平均成功率回答“在这批样本上完成了多少”，却不能回答相同系统在重复运行、扰动、低基线或高后果失败下是否可靠。更完整的 reliability profile 至少应拆开：

```text
capability / average outcome
+ consistency across repeated runs
+ robustness across task and environment perturbations
+ predictability and calibration
+ failure severity and recoverability
```

这些维度不能任意压成一个总分。一个系统可能偶尔完成困难任务，却在同一输入上高度波动；也可能平均分稳定，但少量失败具有不可逆副作用。指标公式、聚合顺序和 implementation revision 都必须成为 scorer identity 的一部分。若修订版纠正了公式，旧结果只能保留为带版本的历史证据，不能静默与新结果拼接。

### Self-report、Behavior Probe 与 Deployment Outcome 是三种证据

模型宣称具有某种 disposition，不等于它在重复、可执行环境中稳定表现该行为；稳定 probe 结果也不等于真实
部署 outcome。评估系统应分别保存 self-report、behavioral episodes 和 environment effects，并记录 prompt、
sampling、tool opportunity 与 policy identity。Behavioral-disposition alignment 研究支持外部 probe 可测量重复
行为模式，但不能把相关性解释为内部人格、因果机制或跨环境稳定性。

Deep Research 进一步要求把 final report 拆成多个 evidence planes：report synthesis quality、claim-level
factuality/provenance、trajectory/process quality 与 environment/tool contract。四者不能平均成一个分数后丢失：
写得完整可能掩盖 unsupported claim，过程看似规范也可能没有真正取得证据。MiroEval 只在其 snapshot、judge
与 tool budget 下支持这种分层；live-web drift、judge calibration 与 trace privacy 仍需要独立治理。

Research Agent 还需要把 final artifact、research progress 与 environment integrity 分开：没有产出最终解，不等于过程中没有形成可复用证据；反过来，拿到高分也可能来自损坏的依赖、污染的 workspace 或 verifier 漏洞。风险评估同样应按 risk family 保存不同 EvalSpec，并进一步区分：

```text
model capability
× elicitation quality
× environment opportunity
× granted permission
× consequence severity
```

这种分解避免把异质风险实验排成统一能力榜，也避免把“在已授权环境中可以执行”误写成“会自主获得权限”。Agent Reliability、ResearchGym 与 frontier-risk framework 为这些边界提供了 2026 年的受限证据；它们的作者分数、特定 judge 和环境结果不构成跨系统常数。

长任务还要求记录 evidence shape，而不仅是 nominal context length。相同 token 数可能来自许多轮简短结构化 observation，也可能来自少数轮高密度 tool log；后者的 decisive fact 更容易被噪声、位置与压缩策略淹没。评测因此至少应把：

```text
turn count / tool-call count
+ observation bytes and evidence density
+ decisive-fact position and redundancy
+ compression / truncation policy
+ final outcome
```

作为同一 run contract。只报告最大支持 turns 会把环境输出形状误写成模型长期能力；只报告总 token 又会丢掉 state transition 次数。AgentLongBench 的受控环境实验为这一区分提供了实验性证据，但不证明其特定长度或模型排名可外推到生产。

### 从 Pass@k 到 Pass^k：能力覆盖与重复可靠性不是同一问题

`Pass@k` 回答多次尝试中是否至少有一次成功，适合搜索和 candidate generation；生产操作还关心同一任务
重复执行是否持续成功。可用 `Pass^k` 表示 k 次都成功，并对同一 task 在 intervention 前后的
reliable↔unreliable transition 做 paired analysis：

```text
task + instruction/evaluator/environment revision
→ k isolated, resettable runs
→ outcome vector rather than only mean
→ conjunction reliability + paired transition
```

降低 temperature 只减少 sampling 随机性，不会消除 environment、instruction、tool 或 evaluator 引起的失败。
固定 plan 可降低行为方差，也可能固化错误；clarification 可减少歧义，也可能泄漏 benchmark oracle。Computer
Use Agent 的重复运行研究只在其 OSWorld、三次重复和指定模型合同下支持该诊断，不证明 `k=3` 满足生产 SLO。
高副作用任务还必须定义 reset、retry budget 与 compensation；成本受限的离线回归仍可保留 single-run metric。

### Judge 从被动 Scorer 演进为有预算的 Evidence Acquisition Policy

开放 search、GUI 与 data-system trajectory 常不能只凭给定 transcript 判真。Judge 可以调用只读 search、
filesystem/database 或 screenshot/accessibility tools 主动取证：

```text
frozen trajectory claim
→ bounded judge tool plan
→ timestamped external observations
→ evidence-backed verdict
→ compare with human / executable authority
```

Judge 只拥有 evidence selection 与 verdict，不拥有 environment truth，也不能用自己的行动修补被评 trajectory。
AJ-Bench 的实验支持 tool access 在其 516 条标注轨迹上提高平均 F1，但约 0.72 F1、network drift、wrong-tool
和“拿到正确证据仍推理错误”说明它不能成为 release oracle。可形式化任务继续优先 deterministic verifier，
高风险争议由 human/domain expert adjudication；active judge 必须记录 credential、budget、tool revision 与副作用。

### Living-world Evaluation：外生变化必须进入 Run Identity

在昂贵 serving stack 上直接搜索配置、routing、KV 或 autoscaling policy，证据最真实却很难穷举；纯 analytical
capacity model 便宜，但看不到 scheduler、queue 与 transfer 的状态交互。中间层可以使用 calibrated discrete-event
digital twin：

```text
versioned production or synthetic arrival trace
→ scheduler/router/KV/worker state simulation
→ candidate Pareto configurations
→ shadow or real-cluster replay
→ canary promotion / rejection
```

Simulator 只拥有候选生成与预筛选，不拥有 deployment truth。其 backend revision、timing profile、event semantics、
calibration window 和 known omissions 必须成为 EvalRun identity；同一 simulator 既优化又裁决会产生 self-confirming
policy。DynoSim 的厂商实验支持 full-stack state replay 比 timing-only model 更能解释其指定 Dynamo workload，
不证明模拟 Pareto、阈值或排名能跨硬件、failure distribution 和软件版本复用。Analytical model、microbenchmark 与
真实集群验证因而是分层共存关系，而不是后一层取消前一层。

静态 episode 便于重置和长期比较；长周期 workflow 中 email、calendar、KB 或文件会在 Agent 休眠时被外部
参与者修改。此时“记住旧状态”与“重新观察真实世界”必须分开测量：

```text
pre-turn authoritative state
→ agent actions and committed effects
→ between-turn exogenous mutation log
→ next-turn observations and decisions
→ post-turn invariant checks
```

ClawMark 的 living-world harness 支持这种 temporal contract，但 deterministic checker 只证明 rubric 可复算，
不证明 rubric 完整或 mutation distribution 代表生产。EvalRun 必须保存 external actor、mutation seed/event、
pre/post state digest、artifact availability 与 reset policy。Frozen suite 继续承担低成本 regression；living suite
用于 temporal drift、silent change 与 writeback correctness，二者不能互相覆盖。

### 科学任务还要评估 Evidence Uptake 与 Belief Revision

开放科学 Agent 即使得到高 outcome score，也可能提出未测试主张、忽略反证或在没有新 evidence 时递归自信。
过程评估可把 trace 映射为 `claim → evidence → test → judgment → update/commitment` 的 dependency graph，
分别识别 convergent evidence、refutation loop、evidence non-uptake 与 untested claim。Graph 是 annotation-derived
view，不是模型思维的直接读出；有些合理推理不会显式 verbalize。Corral 的作者研究支持在其八类科学环境中
outcome 会掩盖 epistemic failure，不证明 scaffold 普遍无效，也未验证把该 taxonomy 作为训练目标就能修复。
Deterministic outcome verifier 仍负责可执行结果，epistemic graph 只增加 diagnosis 与 research-governance evidence。

### Benchmark、Evaluation 与 Testing 不是同一个层次

Benchmark 通常固定一组输入与 scorer，用来比较系统在某个分布上的表现；Evaluation 把这种测量扩展为
带 subject、environment、uncertainty 与 decision policy 的证据过程；Testing 还要指定一个更窄的
行为边界，并声明在给定 fixture、状态和故障条件下必须保持的 invariant。三者可以复用同一套 run
与 evidence 基础设施，但不能互相替代：一个 Agent 在端到端 benchmark 上通过，不代表 tool schema、
memory transition、permission check 或 retry semantics 已分别被测试；反过来，所有 unit tests 通过，
也不能证明动态环境中的长期任务结果。

Agent testing 因此需要从传统的“输入—输出断言”继续扩展：

```text
test boundary and subject identity
+ fixture / initial environment state
+ stimulus and allowed actions
+ expected invariant or oracle
+ observable state transition and side effects
+ failure injection / timeout / retry policy
+ model, tool, workflow and environment versions
```

合理的演进不是用端到端测试覆盖 unit test，而是逐层增加真实交互：确定性的 tool 或 schema unit test
便宜、定位清楚；module test 验证 planning、memory 与多 tool coordination；integration / API test 验证
跨进程与外部依赖；受控 end-to-end、fault injection 和 shadow/canary 再暴露非确定性、权限、性能与真实
副作用。越接近生产，证据相关性越高，但成本、波动、隔离难度和 blast radius 也越大。

Mock 仍然有价值，因为它能控制随机性并精确制造异常；风险在于 mock 掉的恰好是系统最需要验证的
边界。若替换 LLM、tool、network 或外部状态，测试结果只能证明剩余 orchestration 在该 test double
contract 下成立。平台应记录被替换组件，并用少量真实 integration、state-transition 与 failure tests
校验 mock contract 没有漂移。测试充分性也不能只看 code coverage；对 Agent 更有意义的维度包括
tool-selection path、状态转换、delegation、side-effect、failure/recovery 路径和非功能条件。

Tangent 对 Python 开源 Agent 项目的实证研究支持“当前测试仍偏窄”这一观察，但不拥有普遍事实：
其样本受 GitHub、star threshold、框架识别规则与开源可见性限制，工业访谈也集中在同一机构。
因此书稿吸收的是测试边界与证据分层原则，而不是把论文中的比例外推到所有生产 Agent。

### Benchmark 生成器也会塑造被评估的任务人口

真实轨迹或仓库任务提供自然分布，却昂贵、含噪且难以冻结；合成任务可控制覆盖和重放，却会把 generator、
filter、tool rule 与 scorer 的偏好写进 benchmark。生成式 benchmark 不应只保存最终题目，还要保存：

```text
source population and sampling frame
→ generator / transformation recipe
→ filter model and rejection reasons
→ no-tool / trivial-solution checks
→ verifier and answerability contract
→ accepted task population and excluded slices
```

Filter 提高可评分性时，也可能系统性删除长答案、弱工具可解或难以被 judge 解析的任务；post-hoc 单标签
failure taxonomy 则是诊断视图，不是因果 root cause。真实、手工策划与合成 benchmark 应共存，并用交叉执行、
人工抽查和版本化 population report 揭示各自盲区。AgentVista、ISO-Bench 与 SWE-rebench V2 分别提供了 Agent
任务生成、优化 patch 与可执行环境的受限证据，不能把其排行榜外推为开放部署能力。

跨语言派生 benchmark 还应被视为 semantics-preserving compilation，而不是普通字符串翻译。Compiler 必须保留
task invariant、label/choice identity、format/parser contract、language-specific invalid cases，并记录 source item
到 target item 的 transformation lineage。自动翻译扩大覆盖，却会改变难度、歧义、tokenization 和知识前提；
人工复核提高可信度但仍不能证明与源语言等价。原始 benchmark 在长期对比中继续成立，派生版本只能在逐项
validation、contamination 检查和独立 native review 后形成新 distribution。Recovered in Translation 为这条
pipeline 提供了受限证据，不支持跨语言分数直接互换。

### 从 Perfect API 到累积故障：Agent 评测必须控制 Environment Complexity

只验证 tool 名称、schema 与参数 exact match，适合隔离 model 的 function-calling 基础能力；它并没有过时。
但真实 API 还会引入两类正交扰动：specification 可能包含特殊格式、含糊边界、隐含依赖或冗长说明，
execution 则可能返回 warning、无关字段、可绕过的限制或不可恢复错误。此时评测对象不再只是一次调用，
而是 Agent 是否能在不篡改用户意图的前提下识别、恢复或诚实停止。

同一扰动还应至少采用两种 protocol：

```text
isolated protocol
  gold history + one injected complexity
  -> local handling capability

cumulative protocol
  agent-generated history + sequential complexities
  -> error propagation, recovery and stopping behavior
```

Isolated protocol 定位清楚，却切断早期错误对后续 Context 的影响；cumulative protocol 更接近 workflow，
却把 planning、tool selection、environment 与恢复混入同一结果。两者应并列，而不是用后者取代前者。
复杂度注入也必须记录 injection code、初始 environment state、允许 workaround、reference response、judge 与
alternative valid paths；否则 benchmark 可能把 harness 假设误写成 Agent failure。

WildAgtEval 的合成可执行 API 环境为这一区分提供了受限证据，但其场景由模型辅助分配和生成，部分结果
由 model judge 判断，不能代表生产 API 故障频率。正文因此保留 protocol 与 attribution 原则，不保留模型
排名或平均降幅。生产 gate 还必须加入真实流量切片、授权、副作用、latency、cost 与人工恢复证据。

若环境由 LLM 根据 declarative state/rules 动态生成 observation，它位于 mock 与 deterministic simulator 之间：
YAML/schema 使任务状态和 rubric 可检查，语言生成又允许探索隐含需求；代价是 simulator 自身可能违反规则、
泄漏答案或用与被测 Agent 相关的模型制造共同偏差。Run identity 必须绑定 state schema、transition rules、world-
model prompt/checkpoint、seed、consistency tests 和 hidden-state access。Implicit Intelligence 的受控实验支持这种
evidence tier，不把作者的一致性数字写成 deterministic execution guarantee。

### Simulator Fidelity：保留真实 Control Plane 仍不足以等同真实硬件

Runtime what-if evaluation 常在两端取舍：analytical/discrete-event simulator 快、可扩大规模，却容易复制并
简化 scheduler；真实硬件 replay 语义更完整，却昂贵且不适合大量设计搜索。中间路线是直接运行真实
serving control plane，只把 CUDA kernel、collective 和大显存 allocation 替换为预测 duration、barrier 与
virtual state：

```text
real request path + real scheduler/control code
→ intercepted execution calls
→ virtual GPU time and memory
→ predicted kernel / communication duration
→ unchanged control-plane transition
```

这能减少 simulator 与 framework control semantics 的重复实现，但 fidelity 仍由一组前提决定：GPU value
不能回流并改变 host branch，kernel predictor 覆盖目标 model/shape/hardware，collective abstraction 保留必要
同步，virtual memory threshold 不改变 allocation path，CPU/GPU concurrency 与 jitter 也不能被错误抹平。
因此验证单位不应只是平均 latency，而应比较 queue order、admission、batch composition、cache transition、
cancellation/failure path 以及 TTFT/TPOT tail，并按 framework revision 重新校准 predictor。

Revati 说明这种“真实 control plane + 虚拟 execution substrate”在披露的 vLLM/SGLang、模型与 H200 环境中
可以降低实验成本；它不证明 data-dependent kernel、任意 topology 或新 framework version 都保持忠实。
纯 simulator 在尚无可执行 control plane 时仍适合早期搜索，真实 hardware replay 仍是 release evidence。
三者形成 cost/fidelity ladder，而不是后者取代前者。

Simulator identity 还必须覆盖 feedback loop，而不只是一个 hardware profile。LLM Serving 的 request queue、
scheduler choice、memory/network contention 和 operator latency 会互相改变下一事件；若 simulator 只重放固定
kernel 时间，就无法评估 policy 在负载变化后的行为。一个可追溯 simulation run 至少绑定：

```text
workload trace / arrival and length distribution
+ cluster topology and hardware profile
+ runtime / scheduler / cache policy revision
+ operator latency and contention model
+ seed, warm-up, measurement window and SLO
```

Frozen API replay 同样只回答“在记录过的 response 下 Agent 怎样行动”，不覆盖实时交通、天气、服务漂移或
API failure。它适合可复现诊断，online shadow/canary 才拥有 deployment authority。LLMServingSim 2.0 与
MobilityBench 分别提供了 feedback-aware serving simulation 和 domain API replay 的案例；作者 aggregate error
与 benchmark score 均不能证明未见 workload、tail SLO 或现实环境的 fidelity。

### Agent Serving 的容量单位是 Workflow，而不只是 Request

固定 ISL/OSL microbenchmark 能隔离 kernel 与 runtime regression，但 Agent workload 会在多轮请求之间插入
tool think time、动态 prefix、短输出、长 Context 与 bursty phase。此时容量问题不再是“每秒生成多少 token”，
而是“在每个请求都满足 latency/speed SLO 时，可同时维持多少条 active trajectories”：

```text
versioned trajectory phases and dynamic prefixes
+ tool-delay distribution
+ per-request TTFT / output-speed SLO
→ steady-state concurrency search
→ workflow goodput, tail and failure evidence
→ power and cost under an explicit boundary
```

Benchmark owner 拥有 dataset、phase、SLO 与 scorer，被测方拥有 serving configuration，系统运行时拥有
queue/cache/scheduler state。三者不能折叠成一个 hardware score。Replay 提高 workload relevance，却降低
隔离性；private test set 防止 tuning，也削弱第三方 audit；只测 accelerator die/HBM power 又不能代表 host、
network、cooling 与 facility energy。AA-AgentPerf 的 live methodology 支持这种 contract 分解，不证明其
leaderboard revision、vendor tuning 或 replay distribution 等价于生产。Microbenchmark 继续承担定位与回归，
trajectory replay 负责 workload capacity，online shadow/canary 才拥有部署授权。

### Training Benchmark 必须以 Convergence Contract 收束系统优化

单算子吞吐和固定 step time 能定位 kernel/collective bottleneck，却不能证明系统把模型训练到相同结果。
Full-system training benchmark 的 subject 至少是：

```text
model and dataset revision
+ target quality / convergence rule
+ system, framework and precision identity
+ division and allowed optimization policy
+ independent run count and aggregation
```

Clock boundary、evaluation cadence 与 run aggregation 都由 benchmark owner 定义；submitter 拥有 system 与
optimization artifact，reviewer 判断规则合规。加入 MoE workload 是补充 sparse routing、expert imbalance 与
All-to-All 压力，不会让 dense、LoRA、vision 或 recommendation workload 失效。固定规则提高可比性，也会激励
benchmark-specific optimization，并常常遗漏 checkpoint/recovery、power、fabric failure 与长期质量。
MLPerf Training v6.0 为 versioned MoE convergence contract 提供官方案例，不证明跨 division、规模或 workload
的结果可以直接合并，也不能从 submitter narrative 反推某一 kernel 是唯一原因。

### 从 Snapshot 到 Feedback-conditioned Policy：评估对象也会演进

Static benchmark 固定输入与一次输出，最适合低成本回归和可执行 correctness；它没有过时。随着系统能
生成多个候选、主动获取信息或连续修改环境，评估对象才逐层扩展：

```text
single snapshot answer / artifact
-> repeated independent candidates
-> selector over candidate set
-> feedback-conditioned trajectory
-> evolving state sequence with recovery and accumulated debt
```

每一层回答不同问题。Single-run accuracy 测一次决策；`pass@k` 测有限 sampling budget 下候选覆盖率，
不证明 selector 能找到正确候选；interactive run 测 policy 怎样提问、吸收 feedback 和停止；长期 state
sequence 则测早期决策如何影响后续变更、回归与恢复。后者不能用最终 artifact 的 pass/fail 覆盖：两个系统
可能都到达相同终点，却经历不同的失败次数、修复成本、风险暴露和 technical debt。

Computer-use environment 进入长程、多应用和用户交互后，binary completion 还会把“走到哪里失败”压平。
Task-specific checkpoints 可以保存 partial progress，但 checkpoint judge、user simulator、dynamic environment 与
persistent artifact 都是独立 evidence owners：

```text
initial application / user / artifact state
→ action trajectory and cross-app effects
→ checkpoint-specific state assertions
→ dynamic user or environment mutation
→ terminal artifact, safety and recovery evidence
```

更密的 checkpoints 提高诊断力，也可能把 benchmark recipe 泄漏给 policy、奖励表面 progress，或让 model-dependent
judge/simulator 共同偏置分数。OSWorld 2.0 的作者材料支持这种评估对象扩展，不证明其平均 checkpoint 数、task mix
或 simulator 等价于生产桌面。Frozen binary suite 继续用于廉价长期回归；dynamic suite 用于状态漂移和恢复。

Feedback channel 也是 evaluator-owned state，而不是免费的 ground truth：

```text
hidden task / current environment state
-> observation mapping
-> policy question or action
-> judge / environment feedback
-> next policy state and stopping decision
-> final outcome + trajectory evidence
```

Judge 若知道 hidden answer，它既是 scorer 也是 information channel；feedback vocabulary、turn budget、retry、
opponent pool、termination、provider endpoint 与 accumulated context 都会改变可观察能力。只匹配 player tokens
而忽略 judge tokens、environment work、latency 和额外 calls，并不是 compute-matched comparison。更大的
turn budget也可能只鼓励试探或 exploit 某个反馈协议。

长期 artifact evolution 进一步要求保存 `state_0 -> action_1 -> state_1 ...`、每轮目标与 test evidence、
rollback/recovery、metric temporal weighting 和 harness revision。用未来 target tests 引导每一轮能够提供
稳定 oracle，却测的是对已知隐藏终点的迭代重建，不等于真实需求漂移、branch/merge、human review 或线上
依赖变化。Snapshot regression 在局部修复中仍最可靠；interactive/evolution benchmark 只在真实 deployment
也包含反馈或长期 state 时增加证据，并必须和静态、成本及风险指标并列，而不是取代它们。

条件 Workflow 还要求把“答对终点”拆成 branch evidence。若每一层条件为 false 时都应停止，只报告最终答案会把 perception、
predicate execution、path-state tracking 与 stop/continue bias 混成一个数。更可诊断的评估对象是：

```text
typed fact namespace
-> executable predicate
-> verified branch transition or early exit
-> paired minimal counterfactual path
-> path-balanced result and side-effect evidence
```

True/False paired path 能暴露模型在条件失败后仍继续的偏置，却不能证明 visual facts、语言 rendering 或程序 ontology 本身正确。
事实提取者、predicate compiler、translator、branch prior、failure severity 与 API/sampling config 都属于 run identity；模型生成事实
又验证事实时，还存在同源盲点。MM-CondChain 的受限数据支持 depth、predicate complexity 和 stop/continue 可分开诊断，不能
外推为生产 GUI 风险。Atomic benchmark 在只测感知或单条 constraint 时仍合理；真实有副作用的 Workflow 还要加入 action、
recovery、authorization 与 environment transition evidence。

### Reward Hacking 监测要分开 Reference 与可部署观测面

开放任务用 model judge 作为 reward 时，policy 可能发现 judge 的格式、措辞或语义偏好。只看 combined reward
无法区分真实提升、shortcut 首次出现和 exploitation 已饱和；研究阶段可以保留 privileged decomposition，部署
monitor 却通常只能看到 score-bearing trace：

```text
controlled reward decomposition / counterfactual bias
→ reference onset interval
→ judge-blind temporal trace
→ persistent hypothesis + bounded inspection
→ alert
→ independent pause / rollback / reward revision authority
```

Reference judge 仍不是 truth，onset 又依赖 smoothing、threshold 和 shortcut detector；monitor 也不能自行修复
training。Fixed rule 对已知 signature 和高频 guardrail 更便宜，human/executable audit 仍是高风险决策 owner。
CHERRL 的六条受控 hacking runs 支持 discoverability、exploitability 与 onset 可以分开记录，但不提供真实复合偏置、
在线 false-positive、intervention 或跨模型通用性证据。

## 从答案评分到可执行证据

当系统输出代码、漏洞利用、实验方案或可交付文档时，只检查自然语言答案会把最重要的失败留在评估之外。更强的演进路线是：

```text
static answer / multiple choice
→ structured artifact
→ executable verifier or simulator
→ controlled environment interaction
→ outcome、side effect 与 recovery evidence
```

关键变化不是“换一个更难的 benchmark”，而是把 **evaluation object** 从文本扩展为
`artifact + environment + execution trace`。例如 exploit-development 评估只有在隔离环境中
真正编译、运行并触发目标条件，才能区分会描述漏洞与会完成攻击链；N-day 评估还必须版本化
目标软件、补丁可见性、网络权限、时间预算和成功判据。生命科学任务若要求表格、分析结果或
实验设计，也应保存产物并由 task-specific rubric、程序校验与领域专家联合审阅。

这种设计获得更接近真实能力的证据，也引入新的风险：

- verifier 可能不完整、可被 reward hacking，或只验证表面成功；
- sandbox 与真实环境存在差异，环境泄漏会抬高结果；
- 工具、依赖、目标版本和 patch window 改变后，分数不再可直接比较；
- 越接近真实副作用，隔离、伦理审查和人工监督成本越高。

因此，`executable` 不等于 `ground truth`。平台必须把 verifier 本身作为版本化、受测试的
评估组件，并保留失败产物和运行 trace。Anthropic 2026 年的 exploit capability 与 N-day
研究、OpenAI LifeSciBench 可以作为这种演进的受限案例；它们证明相应测试环境中的能力，
不能外推为所有软件、领域或生产环境的通用自主性结论。

专业软件 Workflow 还暴露一个常被 final answer 掩盖的错误：**state/artifact misbinding**。Agent 可能选对
病例却停在错误 series，生成 segmentation 却没有把它注册到正确 volume，或在 rationale 中引用一个并未
成为 viewer 当前状态的结果。更完整的 domain EvalSpec 应把：

```text
full study / source artifact
→ bounded named-tool actions
→ persistent viewer and derived-artifact state
→ canonical answer + coordinates / masks / evidence
→ deterministic evidence gate + replay
```

作为一个整体。Named tools 比 raw script 更易审计，却把 schema coverage、coordinate convention、bridge 和
viewer revision 变成依赖；advanced operator 更多也不保证 workflow 更可靠。静态 2D slice 继续适合廉价
perception regression，成熟 deterministic pipeline 也不必强行 Agent 化。完整医学影像 benchmark 只支持其
公开数据、tool budget 与 hidden reference 下的机制边界，不能替代临床 adjudication 或生产 SLO 证据。

### 从一次通过到 Artifact 的维护强度

`compile/pass` 证明当前 artifact 在当前环境可执行，却不说明测试是否覆盖行为，也不说明后续版本能否
持续维护。代码、Workflow 或配置的 evidence ladder 可以继续向上：

```text
text similarity
→ compile and run
→ coverage delta
→ mutation kill / adversarial perturbation
→ repeated maintenance across revisions
```

每上一层都更接近语义与演进，却更昂贵、更依赖 environment identity。Learned proxy 可以在执行前排序或
筛样，但不能拥有最终 correctness；model judge 也不能替代 compiler/test/mutation state。平台应记录每层
verdict、成本和 abstain，并按风险决定哪些候选必须进入真实执行。静态 snapshot test 在局部回归中仍最清楚，
迭代 maintenance benchmark 只有在产品本身会持续接收变更时才增加外部有效性。

### 先验证 Benchmark 的 Reference Artifact，再比较 Agent

可执行 benchmark 仍可能因为 reference patch、依赖、机器镜像或 scorer 不稳定而产生伪排名。一个 candidate
失败，不一定说明 Agent 能力不足；也可能是 reference artifact 在另一台机器、冷缓存或重新构建后本身不再通过。
因此 benchmark admission 应先独立于被测 Agent 重放 reference：

```text
immutable task + environment revision
→ rebuild and replay reference artifact across machine / round
→ verify deterministic and semantic outcomes
→ estimate infrastructure and scorer variance
→ only then score candidates and aggregate rankings
```

Reference replay 通过也不能证明 task 代表真实 workload，只能关闭“ground truth 自身不可复现”这一类故障。
当分数靠近 release threshold 时，还要报告 task-weight、failure penalty、timeout 与聚合方式的 sensitivity，而不是
把一个 leaderboard total 当成自然常数。固定单机环境在快速回归中仍合理；跨机器 replay 只在 benchmark 要承担
跨系统比较或发布决策时值得支付成本。Performance-Optimization Benchmark Reliability 的作者研究支持这种
reference-first 审计，但不证明其任务集覆盖生产优化分布。

Dense process score 同样只是训练 proxy。若逐步分数与后续 return 或 target value 不对齐，优化它会奖励看似
合理却把系统带向失败的中间动作。进入 RL 或 policy selection 前，应在固定 trajectory distribution 上检验
`score_t` 与 future return、终局 verifier 和关键 slice 的校准，并允许 proxy 在不确定时 abstain。QVal 提供了
这种对齐检查的实验性方法；它不把 learned score 升级为部署 correctness gate，也不证明相关性就是因果 credit。

### 攻击预算是一条风险曲线，不是 ASR@1

安全评估若只测一次采样，会低估攻击者重复尝试的能力；直接穷举大 `N` 又昂贵。更完整的 subject 是
`model/sampler/attack distribution/budget`，输出应是带 uncertainty 的 `risk(N)` 或达到风险阈值所需预算，
而不是把小样本最大值当作模型固有属性。统计外推依赖 exchangeability、分布拟合和 benign/unbreakable
mixture；自适应攻击、并行相关性或 sampler drift 会破坏这些假设。高风险区仍需实际大预算验证，模型、
sampling policy 或 attack corpus 改变后必须重估。

### 从 run-level evidence 到 claim-level provenance

保存一次 run 的输入、代码、日志和结果，只能证明“相关证据存在”，不能自动证明最终报告中
的每个数字、方法描述和结论都由这些证据支持。长 Workflow 还会放大这一断裂：检索摘要先
影响假设，实验结果再经过选择、压缩和写作；只要中间一次映射出错，最终文本可能内部一致，
却已经脱离真正执行过的 artifact。

因此，证据系统还需要从 run 粒度继续细化为 typed claim graph：

```text
claim identity and type
→ declared supporting artifact / source region
→ deterministic or domain-specific verification rule
→ supported / partial / unsupported verdict
→ revision or rejection decision
```

不同 claim 的验证规则并不相同：数值应回溯到带环境和 evaluator identity 的测量记录；方法
描述应映射到实际执行的代码或配置；引用不只要真实存在，还要支持被归因的观点；结论则必须
由前述 evidence 和显式推理共同支撑。这个设计把 `provenance before prose` 作为生成约束，
而不是在报告完成后凭关键词补引用。后验 audit 仍然重要，但它只能发现被检查 taxonomy 覆盖
的断链，不能恢复从未保存的中间状态。

ScientistOne / Chain-of-Evidence 是这一分支的实验性案例。作者系统把文献、实验日志、代码、
分数和 ablation 先组成带 inline evidence tag 的中间表示，再分别执行确定性 grounding、
LLM critic 和 claim verifier，最后才生成并放行正文；其跨系统审计则检查 score
reproduction、specification violation、reference existence 与 method–code alignment。论文
在 75 篇、五类 systems-optimization tasks 上报告了显著完整性差异，但证据边界必须保留：
任务依赖相对确定的 evaluator，baseline adaptation 含人为判断，method–code alignment 仍
使用 model judge，false negatives 未被系统界定，而且“结构完整”不等于“科学结论正确、
新颖或重要”。

这条演进不会替代既有的 run-level lineage：

```text
保存 run / artifact
→ 让结果可重放
→ 为 claim 建立 typed provenance
→ 在发布前验证 claim–evidence mapping
→ 对开放领域保留专家判断和不可自动化边界
```

代价是更细的 artifact identity、schema、storage、verification latency 和治理成本；source
revision、代码重构或数据删除还会使既有 claim 失效。生产平台因此需要记录 evidence digest、
verifier version、verdict reason、supersession 与 retention，而不能只保存一个最终 `pass`。
第 81 章的 Workflow 拥有证据产生与状态转移，本章拥有“这些证据足以支持什么声明”的评估
契约，两者属于 `Layering / Dependency`。

Claim graph 仍可能被同源审查者系统性放行。generator、writer 与 critic 若共享模型家族、Context 或上一轮
verdict，形式上增加 reviewer 数量也不会产生独立 evidence。发布前的 assurance 因而要区分两类 review：

```text
cross-round reviewer: 检查 revision 是否真正修复已知缺口
fresh reviewer:       仅从当前 manuscript、artifact 与 rubric 重新建立 verdict
```

二者都不能自称 truth authority；它们只把 correlated blind spot 暴露为 disagreement、unsupported claim 或
需要专家裁决的 residual。Fresh review 增加成本并可能重复已知工作，cross-round review 又容易被旧结论 anchoring。
低风险、deterministic claim 可由规则验证；开放研究结论则应保留 reviewer identity、可见 Context、disagreement
与最终 decision owner。这样 evidence-to-claim ledger 才是可重放的 assurance state，而不是论文写完后的评分表。

## Scorer 不是绝对真相

不同任务需要不同证据源：

| Scorer | 优势 | 主要失败方式 |
| --- | --- | --- |
| Exact rule / schema | 快、确定、可重复 | 只能测可形式化条件 |
| Executable verifier | 接近真实结果，如 tests、compiler、simulator | verifier 可能不完整或被绕过 |
| Reference-based metric | 易于批量比较 | 多个正确答案时可能误罚 |
| Human judgment | 能理解语境与业务风险 | 贵、慢、有分歧和疲劳 |
| Model judge | 可扩展、可生成理由 | position、style、self-preference 与共享盲点 |
| Production outcome | 最贴近真实价值 | 反馈延迟、混杂因素与实验风险 |

LLM-as-a-Judge 可以降低开放式任务的评估成本，但 judge 也必须被评估。至少需要：

- 固定 judge model、prompt、sampling 和 rubric；
- 用人工或可执行 verifier 校准关键 slices；
- 随机交换候选顺序以检查 position bias；
- 把 judge disagreement 和理由作为 evidence，而不是只保留平均分；
- 防止被评估输出向 judge 注入指令；
- 避免 candidate 与 judge 同源时把 correlated preference 当成独立证据。

“让更强模型打分”是一种 measurement design，不是 ground truth 的替代。

Judge 一旦进入 RL reward loop，评估分布就不再静止。离线 agreement 高，只说明 frozen candidate distribution 上近似某个
reference；训练中的 policy 会主动搜索 judge blind spot，形成 `policy -> judge reward -> policy shift` 的反馈回路。Reasoning、
更长 rubric 或 distillation 可以提高局部一致性，也可能把可利用模式训练得更稳定；它们不能替代目标规范和 adversarial robustness。

因此 reward judge 的验收应加入 policy-shifted red team、独立 holdout oracle、跨 judge transfer、artifact sampling 与停止条件，
并同时观察 training-judge reward 和外部 evidence。Examining Reasoning LLMs-as-Judges 的合成 preference 实验说明 reasoning judge
仍可被策略利用，且 reasoning compute 不能替代 distillation；它不证明所有 reasoning judge 更差，也不证明某公开排行榜失效。
规则、程序或 executable verifier 在可形式化域继续优先；开放域的 model judge 必须保留 disagreement、abstain 和人工升级，而
不能同时独占训练 reward 与 release authority。

### Rater 数量不是常数：先分解方差，再分配预算

“每项需要几位 rater”没有跨任务固定答案。Item difficulty、rater population、同一 rater 的重复测量、criterion
歧义和 aggregation rule 共同决定不确定性。Evaluation owner 应先声明要估计的是 mean、ranking、slice gap
还是 release decision，再用 hierarchical sampling / variance decomposition 决定把新增预算放在更多 items、更多
raters 还是 repeats：

```text
target estimand + acceptable decision error
→ item / rater / repeat variance
→ stratified allocation
→ confidence or posterior uncertainty
→ stop, expand a slice, or escalate to experts
```

更多同质 rater 不能修复 rubric 错误或共同偏差；少量领域专家也未必代表部署人口。固定小 panel 在低风险、
高一致性任务仍然有效，复杂或高风险 slice 才值得动态扩容。Google 的 rater study 是这一预算原则的证据，
不是通用 rater threshold。

Judge 还可能在两个不同目标间切换：预测某个个体/人群会怎样判断，或执行规范性 rubric。前者的 ground truth
应是带 annotator/cohort identity 的**分布**，而不是强迫所有人收敛为一个标签；后者则必须固定 policy、criterion
与 authority。若把群体分歧压成 majority label，模型看似错误也可能只是预测了少数但真实存在的观点：

```text
item + domain / cohort context
→ annotation distribution and disagreement
→ calibrated predictive distribution
→ decision rule chosen for the use case
```

Domain-conditioned critique 再产生 verdict，可以提高可解释性，却会把 critic 和 judge 的相关误差串联起来。
QEDBENCH 与 probabilistic-inference 研究提供了受限证据；它们不证明某个 LLM judge 等同人类总体，也不能把
描述性 population prediction 当成安全、质量或事实判决。

### Rubric Formation、Criterion Execution 与 Ranking 必须分层

复杂开放式判断不能只把一个 rubric 文本塞给 judge。至少有四层可独立失败：

```text
intended use / risk policy
-> rubric formation: 什么条件构成正确或可接受
-> criterion execution: 每条条件在当前 evidence 上是否成立
-> aggregation / ranking: 条件怎样形成 verdict 或 partial order
-> decision policy: verdict 是否足以发布、奖励或升级
```

Rubric formation 遗漏隐含约束、倒置优先级或虚构标准时，更强 judge 与更多 test-time samples 只能更稳定
地执行错误 specification。Criterion execution 又可能误读 evidence、受 position/style 影响，或把 legitimate
alternative 判错。因此 rubric 是有 owner、version、适用域、priority/dependency、holdout 与审批边界的
measurement state，不是 prompt decoration。Human-authored rubric 可作为高质量受控参考，却不是跨组织、
跨时间的绝对 oracle；generated rubric 便宜可扩展，但必须用 hidden holdout、executable checks 与 human
disagreement 审计，不能直接同时成为训练 reward 和公开 release gate。

逐 criterion verification 与全局 ranking 也不是同一能力。一个 judge 可以大体判断每条 constraint，却因
flat averaging、system/user priority、tie、parser fallback 或 pairwise cycle 产生错误全局顺序；也可能偶然排对
结果，却给出错误局部理由。系统应保留：

```text
instruction hierarchy + atomic criteria
+ per-response criterion verdict and evidence
+ missing / invalid / abstain state
+ pairwise edges or partial-order graph
+ aggregation algorithm and parameters
+ semantic matcher / parser identity
```

只由可信 dominance edges 构造 partial order，可以避免强迫标注不存在的 total order；但孤立或不可比较节点
如何处理，本身就是选择政策。Pairwise-to-Elo 或其他全局标量便于排序，却可能隐藏 cycle、intransitivity 与
constraint-level failure。Parser 对缺失项默认通过更会静默抬高分数。因而局部 accuracy、global ranking
consistency、abstention/invalid rate 与 disagreement 应分别报告；安全 must-have、法律约束和 schema
correctness 更适合作 hard constraints，而不是和软偏好做平坦投票。

### Trajectory Judge 必须区分叙述、动作与完成证据

Agent trajectory 比单次答案更难评分，因为 judge 同时看到模型的自述、动作记录、环境状态
和最终产物。最危险的捷径是把 Agent 的“已完成”叙述当作 outcome：一条看起来连贯的轨迹
可能漏做步骤、作用于错误对象，或在最后画面之外留下副作用。

更稳健的 evidence order 是：

```text
agent narrative / rationale
  解释意图，但不是完成证明
→ typed actions and tool results
  证明执行过什么，但不保证目标达成
→ environment transition and artifact
  证明 observed state 怎样改变
→ task-specific completion and side-effect checks
  才能支持 success / fail verdict
```

这不意味着文字 history 无用。对于输入、CLI command 或跨应用意图，screenshots 可能没有
保留决定性信息；judge 需要完整 action history，但必须把 agent-authored text 当成待核验
claim，而不是独立证据。OSReward 的跨平台 trajectory study 与同期公开 benchmark audit
共同暴露了两个互补问题：model judge 容易 false-accept 未完成任务，scripted verifier 也会
false-reject 合法替代路径或继承 broken task。它们支持的是“judge 与 verifier 都要审计”，
不是任一论文的具体错误率可直接外推到生产。

因此二元 accuracy 至少要拆成 success recall 与 failure recall，并按 failure type、平台、
trajectory length 和可验证性切片。高 success recall、低 failure recall 的 lenient judge
会把错误轨迹写成 RL reward 或训练标签；相反，过严 judge 会惩罚正确但非预期的路径。
训练 reward model 前应先以 human-gold 或 executable outcome 校准关键 slices，保存逐例
verdict flips 与 disagreement，并让高风险 false success 进入独立 gate。Ensemble 只有在
错误足够独立时才增加证据；共享输入、模型家族和叙述偏差的多数票不能自动升级为 truth。

评测环境自身也必须成为被验证对象。真实环境的状态转移与副作用最可信，却昂贵、难公开；手工 simulator
可复现，却难覆盖大量领域；LLM-based language simulator 能快速生成多域 tool interaction 和 fault scenarios，
但其 latent state、observation 与 verifier 都可能漂移。演进关系因此不是“用语言模型替代真实环境”，而是：

```text
static answer task
→ deterministic or hand-built interactive simulator
→ configurable language simulator for coverage expansion
→ cross-simulator disagreement and real-environment anchor
```

EvalSpec 必须记录 simulator model/prompt/history/revision、initial state、tool schema、fault policy 与 verifier。
Cross-simulator 排名翻转应被解释为 measurement uncertainty，而不是选择对目标模型最有利的 simulator。
OccuBench/LES 的合成多域实验支持把显式错误与 silent degradation 分开注入，也同时展示 simulator 会发明实体、
遗漏约束；因此它适合早期 coverage 和故障假设生成，不足以证明真实职业能力或高风险 deployment readiness。

任务聚合也不能掩盖 domain slice。按 occupation、domain 或 capability family 分层可以暴露“总体平均正常、
关键 slice 失效”，但职业标签只是采样轴，不是胜任力证书。每个 slice 仍需 domain-expert rubric、deterministic
invariants 与真实环境 anchor；没有这些证据时只报告 benchmark capability，不外推为现实职责授权。

过程评估还需要区分“尚未成功的探索”与“已经造成错误的动作”。如果每个非最优 step 都记为负例，系统会
惩罚必要的信息收集；如果只看最终成功，又无法定位第一次破坏前置条件的 decision。更可审计的 process label
至少保留三值语义与因果位置：

```text
+1  advances a verified subgoal
 0  neutral exploration / insufficient evidence
-1  violates a constraint or causes a verified bad transition

first causal error
-> downstream propagated consequences
-> recovery or terminal failure
```

`first error` 不是第一句看起来奇怪的 reasoning text，而是最早能由 environment state diff、tool result、test
或明确 rubric 证明会改变后续可行性的 transition。后续步骤可能只是传播已有错误，不能重复计算成独立能力
缺陷。AgentProcessBench 的受限实验支持 neutral、causal error 与 propagation 分开能改善诊断，但不证明其
标签就是通用 ground truth；长轨迹的 counterfactual 很难建立，annotator/judge 也可能混淆探索和浪费。终局
verifier 在只关心 outcome 时仍必要，step label 用于定位与训练 credit，二者属于不同 Evidence Level。

这一区分还可以上升到 run-level diagnosis：最终失败可能来自 **exploration error**（没有访问必要证据、工具或
状态），也可能来自 **exploitation error**（已经获得足够信息，却选择或执行了错误动作）。二者需要不同修复：
前者扩大或重排搜索，后者改进决策、verification 或 action policy。分类必须绑定可观察 opportunity set；真实
开放环境中通常不知道完整最优路径，因此“未访问某项”不能自动判为探索错误。对应研究只证明这种分解在其
受控 coding/web harness 中可测，不能把分类器判断当成普遍因果真相。

Simulator fidelity、过程错误和 scorer identity 最终应在同一账本中相交，而不是各自给一个总分。DR3-Eval
这类 deep-research benchmark 进一步要求分别冻结 retrieval corpus、report artifact、sandbox/tool versions、
static/live evidence 边界与 human-validation protocol。YOJO 这类一次编码多个候选的 list-conditioned scorer
可以复用 prompt/media compute，却使 score 依赖候选集合与排列；它输出的是“本列表中的选择证据”，不是可跨
列表缓存的绝对 reward。部署必须保存 candidate IDs、permutation 和 list size，并把 permutation consistency
纳入正确性测试。独立 scorer 在候选异步到达、需要稳定标量或跨 run 缓存时仍更合适。

### 从 Final Answer 到 Artifact、Process 与 Environment Evolution

Final-answer score 成本低、长期可比，适合 release regression；但 Agent 产出代码、科学结论或 Web research
时，相同答案可能来自无效 artifact，不同答案也可能都由合法路径得到。更完整的诊断层次是：

```text
result correctness
→ executable artifact / feature coverage
→ action and subgoal process evidence
→ recovery under injected or cumulative failures
→ asynchronous environment state over time
```

Artifact scorer 应先检查 build、tests、mutation/coverage 与真实执行路径，再讨论风格或 judge 偏好；process scorer
可把 partial progress 表示为 subgoal vector，却不能假设 gold decomposition 是唯一合法 plan。把任务从 desired final
state 反向生成初始故障，有助于得到可验证环境，但 task generator 与 verifier 共享 specification 时会共同漏错。
动态、异步环境还必须冻结 event schedule、simulated time、provider/tool versions、timeout 和重放策略，否则评测的
对象不再只是 Agent policy。

当 application state 可以通过文件、数据库、metadata 或内部 API 检查时，benchmark construction 还可以把顺序
从“先生成任务、最后找 judge”反转为 verifier-first synthesis：

```text
typed inspection endpoint + executable checker
→ checker unit / integration tests
→ generate initializer, instruction and success criteria
→ run fixed calibration trajectories
→ diagnose checker–reference disagreement
→ bounded checker repair without changing task or trajectory
```

Verifier 因而成为需要版本、测试和修复证据的 artifact，而不是 ground truth。固定 trajectory 可以隔离 checker
变化，却也可能诱导 repair 迎合样本；可检查状态会偏向 schema-visible tasks，并遗漏视觉、几何或开放语义。
OpenComputer 的作者系统提供了这条机制的实现证据，不证明 programmatic verdict 总是正确。无法稳定表达
post-state 时，人工/visual judge 仍是必要分支；两者应通过 disagreement slice 互相审计，而不是线性替代。

科学和深度研究工作流还要把 autonomy 与 significance 分开：系统可以独立完成许多步骤，却只产生低价值结果；也
可能在人类选择问题和最终复核下形成高价值 artifact。Claim novelty、citation provenance、domain expert verdict 与
executable reproduction 是不同证据。增加 process metrics 改善归因，却扩大 annotation、judge、environment drift 和
benchmark gaming surface；final-only 与 component tests 因此不会被淘汰，而是与 end-to-end stateful evaluation 分层共存。

### Stateful Counterfactual 必须冻结 Fork Identity

一次从初态跑到终态只能比较 outcome，无法回答某个中间决策若改变，后续业务状态是否仍可恢复。对可 snapshot 的
环境，可以在相同 save point fork 多个 action branch，再把每条 branch 加载到隔离 simulator/runtime 中执行：

```text
authoritative initial state
→ versioned save point
→ matched-budget action branches
→ isolated load / execute / observe
→ compare outcome, side effects and recovery cost
```

Fork 的 identity 至少包含 simulator/runtime revision、clock、RNG、external-service snapshot、principal/credential、
tool schema 与 budget；否则 branch difference 混入环境漂移。Save–fork–load 也不能撤销真实世界副作用，simulator
policy 与 evaluator 若同源还会产生 self-confirming result。Business Arena 的受控商业环境只支持 stateful
counterfactual evaluation 的可行性，不证明现实企业决策、长期用户反应或经济收益。Final-only regression 在低成本
回归中仍必要；真实 shadow/canary 与人类审批继续拥有 deployment evidence。

## Dataset 是受治理的评估资产

Evaluation dataset 不应只是一个 CSV 路径。它至少需要：

```text
dataset identity and digest
source and license / consent
schema and task definition
sampling and slice policy
expected outputs or rubric
contamination checks
creation / refresh time
access and retention policy
```

数据可按用途分层：

- **Frozen benchmark**：用于长期可比，更新慢，但容易与新流量脱节。
- **Golden regression set**：保存生产关键案例，规模小、release-blocking。
- **Slice suites**：验证特定语言、风险、长度或 tenant。
- **Adversarial/red-team set**：主动探索边界，不应只优化平均分。
- **Recent production sample**：提高现实相关性，但要处理隐私、选择偏差与标签延迟。

训练数据和评估数据必须有可查询 provenance。第 27 章负责数据去重、decontamination 与 lineage；本章负责说明污染如何削弱 evaluation claim。一次扫描只能证明“在当前算法和语料视野下未发现匹配”，不能永久证明没有污染。

## Offline、Shadow、Canary 与 Online Evaluation

不同阶段提供不同强度和风险的证据：

| 阶段 | 能回答什么 | 不能证明什么 |
| --- | --- | --- |
| Offline | 可重复比较、回归、切片与受控故障 | 真实流量、用户行为和长期副作用 |
| Replay | 在历史请求上比较新系统 | 当时未记录的状态与反事实用户反应 |
| Shadow | 使用真实流量但不影响用户结果 | 新结果真实展示后的反馈 |
| Canary / A/B | 真实交付条件下的相对影响 | 所有长期和低频风险 |
| Continuous online | 漂移、持续质量与业务结果 | 没有混杂控制时的因果结论 |

这些阶段不是互相替代。Offline 适合在低风险环境快速淘汰明显回归；shadow 验证真实 workload 与系统路径；canary 在受限 blast radius 下验证用户影响；长期线上指标再反馈分布变化。

同样，online 优于 offline 也不是普遍结论。高风险医疗、安全或有不可逆副作用的 Agent action 不能先上线再“观察效果”。越接近真实环境，证据通常越相关，但试验成本和伦理约束也越高。

## Evaluation Run 的平台对象模型

一个可审计的 Evaluation Run 可以抽象为：

```text
EvaluationRun
├─ eval_spec_id
├─ subject_identity
├─ dataset_or_environment_id
├─ executor/runtime identity
├─ scorer identities
├─ per-example results and traces
├─ aggregate metrics and uncertainty
├─ slice results
├─ failures / exclusions
└─ immutable artifacts and timestamps
```

平台还需要把 `Run` 与 `Decision` 分开：

```text
Evaluation evidence
→ policy checks
→ owner / approval / exception
→ promotion, rollback, hold or investigate
```

同一份证据在低风险内部工具上可能允许发布，在高风险外部系统上可能不足。Decision 取决于风险政策，不能反向修改 Run 结果。例外必须有 owner、reason、scope 和 expiry。

## Release Gate 不是一个万能阈值

简单规则可能是：

```text
candidate_overall_score >= baseline
```

它会允许局部高风险回归被总体收益抵消。更完整的 gate 可以组合：

```text
required golden cases pass
AND no blocking safety regression
AND critical slices stay within bounds
AND quality improvement exceeds uncertainty
AND runtime SLO and cost remain acceptable
AND artifact / environment identities are valid
```

不同指标不一定能压缩成单一加权分数。安全底线、法律约束和 schema correctness 更适合作为 hard constraints；质量、成本与延迟可以在约束内做 Pareto comparison。

Gate 还必须区分：

- **absolute threshold**：是否达到最低可用水平；
- **relative regression**：是否比当前 production 更差；
- **non-inferiority**：新系统是否在允许范围内不劣；
- **improvement**：收益是否大于 measurement uncertainty 与切换成本。

## Evaluation 与 Observability 的边界

第 67～69 章的 Metrics、Logs、Traces 回答 observed state：

```text
what happened?
where did time and state go?
which version and request were involved?
```

Evaluation 回答 normative comparison：

```text
did the behavior satisfy the specified objective?
is the evidence strong enough to change production state?
```

二者必须共享 identity，却不能合并。Trace 可以显示 retriever 返回了哪些 documents，但 groundedness scorer 才判断答案是否被证据支持；metric 可以显示 tool error rate 上升，但 evaluation 才判断任务成功与风险是否已不可接受。

Observability 也向 Evaluation 提供样本与 execution evidence，Evaluation 再把质量结果作为 Monitoring 的低频信号或 release policy 输入。这是双向接口，不是上下级替代。

## Feedback 如何进入下一轮，而不污染下一轮

生产闭环可以写为：

```text
production behavior and outcome
→ observe and sample
→ label / score / investigate
→ attribute failure
→ update data, prompt, retrieval, model or policy
→ create a new immutable subject
→ rerun evaluation
→ gated release
```

反馈首先是待验证 evidence，不是直接训练样本。用户投诉可能来自产品误解，点赞可能奖励讨好式回答，Agent 成功也可能利用了环境漏洞。进入数据或 policy 前应记录 consent、source、confidence、scope、dedup 和 review。

归因同样重要。如果失败来自 retrieval，却通过 SFT 改模型，系统可能记住当前知识快照而没有修复索引；如果失败来自 runtime 截断，却修改 prompt，问题会在负载变化后重现。Evaluation System 应保留 component results 与 trace，使修正落到正确知识树节点。

## MLflow 在 Evaluation System 中的位置

MLflow 可以映射 Evaluation System 的部分对象：

```text
Experiment / Run
  → execution identity and metadata

Dataset
  → input identity, digest and lineage

Logged Model / Model Version
  → subject artifact identity

Metrics / Tables / Artifacts / Traces
  → aggregate and per-example evidence
```

这使 MLflow 适合连接训练 run、模型、dataset、evaluation result 与 Registry。它解决的是 metadata、artifact 和查询问题，不自动解决：

- intended use 和 failure taxonomy；
- dataset 是否代表生产分布；
- scorer 是否可靠；
- threshold 是否符合业务风险；
- canary 的因果设计；
- promotion 由谁批准；
- 线上反馈能否进入下一轮数据。

截至 2026 年 7 月，MLflow 官方文档将 classic ML evaluation 与 GenAI evaluation 描述为不同系统，metric/scorer 对象并不互通。这进一步说明产品 API 会演进，而上面的 Evaluation contracts 应保持稳定。

OpenAI Evals、MLflow、内部评测平台或领域 simulator 都可以成为 executor/scorer implementation。工具选择应服从对象、环境、可重复性、成本和治理要求，而不是反过来让工具的数据模型定义评估问题。

## 常见失败方式与替代方案

**Leaderboard-first。** 先选公开 benchmark，再把高分当作产品目标。替代方案是先写 intended use 与 failure taxonomy，再选择或构造 suites。

**Average-only。** 只报告总体均值。替代方案是保存 per-example evidence、关键 slices 和 uncertainty。

**Judge-as-truth。** 用一个 model judge 替代所有人工与 verifier。替代方案是多证据校准、顺序随机化、disagreement 分析和高风险人工复核。

**Online-only。** 认为真实流量自动产生真实结论。替代方案是把 offline control、shadow、canary 与持续线上观测组合起来。

**Metric-to-production automation。** 一个阈值直接移动 `production` alias。替代方案是让 gate 同时检查 identity、quality、safety、SLO、cost 与 exception policy。

**Store-results-without-contract。** 保存一堆 metrics，却没有 dataset、scorer、environment 和 subject identity。替代方案是把 Evaluation Run 作为不可变证据对象。

**Eval-set overfitting。** 反复根据同一 hidden set 调 prompt 或模型，使它逐渐成为训练信号。替代方案是分离 development、regression 与 held-out suites，并控制访问和刷新策略。

## 工程实践：从最小可信闭环开始

一个团队不必一开始建设巨型评估平台。最小可信闭环可以是：

1. 为一个明确 use case 写 EvalSpec 和 failure taxonomy。
2. 建立小型 golden set、关键 risk slices 与数据 provenance。
3. 固定完整 subject identity 和 execution environment。
4. 组合一个确定性 scorer 与一个经校准的人类或 model judge。
5. 保存 per-example result、trace、aggregate 和 uncertainty。
6. 建立 relative regression 与 hard safety gate。
7. 用 shadow 或小流量 canary 验证真实 workload。
8. 把失败归因到 data、model、retrieval、runtime 或 action policy。
9. 新版本重新走同一闭环，不原地覆盖证据。

规模扩大后，再增加 suite registry、分布式 execution、sampling、review queue、policy engine、online joins 和 retention，而不是先做一个功能繁多的 dashboard。

## 本章在知识树中的位置

```text
Part IV
  data / training / checkpoint
                 |
                 v
Part VI
  Registry identity
        ↓
  Evaluation specification and evidence
        ↓
  release decision / feedback
        ↔
  Monitoring / Logging / Trace
        ↓
  Production governance
                 |
                 v
Part VII
  component and trajectory evaluation
```

第 59 章回答“被发布的 artifact 是谁”，本章回答“什么证据足以说明它适合特定用途”。第 67～69 章回答运行中发生了什么，第 73 章把证据接入 readiness、rollout、rollback 与反馈。Part VII 的 RAG、Memory、Tool、Workflow 和 Agent Platform 保留各自的局部 failure modes，但复用本章的 subject、dataset/environment、scorer、run 与 decision contracts。

Part III 把 evidence object 扩展为 modality representation、generated state、world transition 与 physical action。评估必须沿 `perceptual plausibility → temporal/state consistency → action-conditioned prediction → closed-loop outcome → safety` 逐级收紧；低层图像/视频分数不能替代 causal dynamics 或 real-robot evidence。具体模型机制归 Ch23～26，本章只拥有可比较的 EvalSpec、run evidence 与 release decision。

这也闭合了第 3 章的控制回路：

```text
desired objective
→ observe
→ evaluate deviation
→ decide
→ act
→ observe again
```

## 自检问题

1. 为什么 benchmark 分数总是一个条件性结论？
2. EvalSpec 至少需要声明哪些对象与政策？
3. 为什么更多样本不能修复错误分布或错误 scorer？
4. Model、System、Runtime 与 Agent evaluation 的边界是什么？
5. LLM-as-a-Judge 为什么仍需要校准和版本化？
6. Frozen benchmark、golden set、risk slices 与 production sample 各解决什么问题？
7. Offline、shadow、canary 与 online evaluation 为什么不能互相替代？
8. Evaluation Run 为什么必须与 promotion Decision 分离？
9. Observability 与 Evaluation 怎样共享 evidence，又为什么不能合并？
10. 线上反馈进入训练或 prompt 更新前需要哪些治理？
11. MLflow 在 Evaluation System 中解决什么，又不解决什么？
12. Agent evaluation 为什么必须包含 trajectory、environment 和副作用？
13. 为什么 Agent 的完成声明、action history 与 environment outcome 必须分层保存？
14. 为什么保存完整 run artifacts 仍不足以证明报告中的每个 claim？
15. Static、pass@k、interactive 与 state-evolution evaluation 分别测量什么，为什么不能互相替代？
16. 为什么 rubric formation、criterion execution 与 global ranking 必须分别版本化和审计？
17. 为什么 Agent API robustness 应同时使用 isolated 与 cumulative protocol？
18. 复用真实 control plane 的 simulator 还必须验证哪些 execution-substrate 前提？

## 小结

Evaluation System 不是 benchmark 集合，也不是某个产品的 metrics 页面。它把 intended use 转化为 EvalSpec，把有限数据和环境转化为带不确定性的 evidence，再把 evidence 放入受风险政策约束的发布与反馈决策。

它的长期不变量是：完整 subject identity、明确分布、可审计 scorer、per-example evidence、切片与不确定性、分离的 decision policy，以及从生产反馈回到新版本的受控闭环。下一章进入 Monitoring，讨论平台怎样以受控成本持续获得 observed state，而不把“发生了什么”误当成“是否足够好”。

## Review notes

- CHERRL（reward-hacking onset 与 judge-blind temporal audit；Status: Experimental）:
  https://arxiv.org/abs/2606.04923

- DynoSim（scheduler-aware serving digital twin；Official Engineering Evidence）:
  https://developer.nvidia.com/blog/dynosim-simulating-the-pareto-frontier/

- Agentic Skills in the Wild（selection/retrieval/adaptation evaluation；Status: Experimental）:
  https://arxiv.org/abs/2604.04323
- KnowU-Bench（Act/Silent/Stop proactivity EvalSpec；Status: Experimental）: https://arxiv.org/abs/2604.08455
- FinTrace（tool component→trajectory→outcome ladder；Status: Experimental）: https://arxiv.org/abs/2604.10015

- MiroEval（report/claim/process/environment evidence planes；Status: Experimental）:
  https://arxiv.org/abs/2603.28407

本章取代早期以 MLflow 为中心的组织方式。MLflow 仍作为 metadata/evidence implementation 保留，但不再承担知识树 owner。公开 benchmark 和论文结果只用于说明 measurement problems，不被外推为当前模型或生产系统的通用结论。

Primary research：

- Percy Liang et al., "Holistic Evaluation of Language Models", 2022: https://arxiv.org/abs/2211.09110
- Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", 2023: https://arxiv.org/abs/2306.05685
- Xiao Liu et al., "AgentBench: Evaluating LLMs as Agents", 2023: https://arxiv.org/abs/2308.03688
- Carlos E. Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", 2023: https://arxiv.org/abs/2310.06770
- Anthropic, "Measuring LLMs’ ability to develop exploits", 2026:
  https://www.anthropic.com/research/exploit-evals
- Anthropic, "Measuring LLMs' impact on N-day exploits", 2026:
  https://www.anthropic.com/research/n-days
- OpenAI, "Introducing LifeSciBench", 2026: https://openai.com/index/introducing-life-sci-bench/
- OSReward（Status: Experimental；cross-platform trajectory judge audit）:
  https://arxiv.org/abs/2607.28609
- How Benchmarks Mis-Score Computer-Use Agents（Status: Experimental；scripted verifier audit）:
  https://arxiv.org/abs/2607.28367
- ScientistOne / Chain-of-Evidence（Status: Experimental；claim-level provenance 与 integrity
  audit）: https://arxiv.org/abs/2605.26340
- SWE-CI（Status: Experimental；state-evolution evaluation）:
  https://arxiv.org/abs/2603.03823
- Interactive Benchmarks（Status: Experimental；feedback-conditioned policy evaluation）:
  https://arxiv.org/abs/2603.04737
- RubricBench（Status: Experimental；rubric formation/execution split）:
  https://arxiv.org/abs/2603.01562
- IF-RewardBench（Status: Experimental；local verification/global ranking split）:
  https://arxiv.org/abs/2603.04738
- Tangent: An Empirical Study of Testing Practices for LLM-Based Agent Applications（Status:
  Empirical；Python open-source corpus + single-organization practitioner interviews）:
  https://arxiv.org/abs/2608.08413
- Beyond Perfect APIs / WildAgtEval（Status: Experimental；isolated/cumulative API-complexity
  evaluation）: https://arxiv.org/abs/2601.00268
- Revati（Status: Experimental；real-control-plane / virtual-GPU serving emulation）:
  https://arxiv.org/abs/2601.00397
- TAM-Eval（compile/coverage/mutation/maintenance evidence ladder；Status: Experimental）:
  https://arxiv.org/abs/2601.18241
- SABER（Best-of-N adversarial risk estimation；Status: Experimental）:
  https://arxiv.org/abs/2601.22636
- AgentLongBench（turn horizon 与 tool-output evidence shape；Status: Experimental）:
  https://arxiv.org/abs/2601.20730
- FeatureBench（executable feature/artifact evaluation；Status: Experimental）: https://arxiv.org/abs/2602.10975
- CLI-Gym（environment inversion；Status: Experimental）: https://arxiv.org/abs/2602.10999
- Gaia2（dynamic and asynchronous Agent evaluation；Status: Experimental）: https://arxiv.org/abs/2602.11964
- Aletheia / Gemini Deep Think（autonomy 与 significance evidence；Status: Experimental）: https://arxiv.org/abs/2602.10177
- SciAgentGym（scientific tool environment 与 recovery evaluation；Status: Experimental）: https://arxiv.org/abs/2602.12984
- RL-finetuned VLM robustness（外显一致性不等于 modality-grounded evidence；Status: Experimental）: https://arxiv.org/abs/2602.12506
- BrowseComp-V3（result/process/subgoal evaluation；Status: Experimental）: https://arxiv.org/abs/2602.12876
- Towards a Science of AI Agent Reliability（reliability profile 与 metric revision；Status: Experimental）:
  https://arxiv.org/abs/2602.16666
- ResearchGym（result/progress/environment-integrity evidence split；Status: Experimental）:
  https://arxiv.org/abs/2602.15112
- Frontier AI Risk Management Framework in Practice v1.5（heterogeneous risk-family EvalSpec；
  Status: Experimental）: https://arxiv.org/abs/2602.14457
- General Agent Evaluation（model/architecture/protocol-adapter subject identity；Status: Experimental）:
  https://arxiv.org/abs/2602.22953
- ISO-Bench（executable optimization-patch evaluation；Status: Experimental）:
  https://arxiv.org/abs/2602.19594
- MobilityBench（frozen domain-API replay；Status: Experimental）: https://arxiv.org/abs/2602.22638
- LLMServingSim 2.0（feedback-aware serving simulation identity；Status: Experimental）:
  https://arxiv.org/abs/2602.23036
- AA-AgentPerf methodology（live workflow-serving benchmark contract）:
  https://artificialanalysis.ai/methodology/agentperf
- MLPerf Training v6.0（versioned MoE convergence benchmark contract）:
  https://mlcommons.org/2026/06/mlperf-training-v6-0-results/
- OSWorld 2.0（dynamic checkpoint and persistent-state evaluation；Status: Experimental）:
  https://arxiv.org/abs/2606.29537
- Performance-Optimization Benchmark Reliability（reference-artifact replay；Status: Experimental）:
  https://arxiv.org/abs/2607.01211
- QVal（dense proxy 与 future-return alignment；Status: Experimental）:
  https://arxiv.org/abs/2606.32034
- AgentVista（benchmark population construction boundary；Status: Experimental）:
  https://arxiv.org/abs/2602.23166
- QEDBENCH（domain-conditioned critique/verdict；Status: Experimental）: https://arxiv.org/abs/2602.20629
- Humans and LLMs Diverge on Probabilistic Inferences（population-distribution target；Status: Experimental）:
  https://arxiv.org/abs/2602.23546
- Implicit Intelligence（declarative LLM-simulated environment；Status: Experimental）:
  https://arxiv.org/abs/2602.20424
- Recovered in Translation（benchmark translation as semantics-preserving compilation；Status: Experimental）:
  https://arxiv.org/abs/2602.22207
- MedOpenClaw / MedFlow-Bench（Status: Experimental；full-study state/artifact evidence contract）:
  https://arxiv.org/abs/2603.24649

Official specifications and documentation：

- NIST AI RMF 1.0, MEASURE function: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
- MLflow Model Evaluation: https://mlflow.org/docs/latest/ml/evaluation
- MLflow GenAI Evaluation Datasets: https://mlflow.org/docs/latest/genai/datasets/
- MLflow Tracking: https://mlflow.org/docs/latest/tracking

Implementation evidence：

- OpenAI Evals repository: https://github.com/openai/evals
- OpenComputer（verifier-first executable task synthesis；Status: Experimental）:
  https://arxiv.org/abs/2605.19769

- Business Arena（stateful counterfactual evaluation；Status: Experimental）:
  https://arxiv.org/abs/2608.08621
- Vero（repository-level implementation + proof artifact evaluation；No Change / Experimental evidence）:
  https://arxiv.org/abs/2608.13522
