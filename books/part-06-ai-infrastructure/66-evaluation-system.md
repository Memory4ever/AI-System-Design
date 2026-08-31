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

## HTTP 成功只是质量判断的第一道门

传统服务的 `error rate` 通常把 timeout、连接失败、`5xx`、进程异常或显式 schema failure 记为错误。这些信号回答执行路径是否完成，却看不见一个语法正常、HTTP `200` 的答案是否事实错误、遗漏关键条件、违反策略或没有完成业务任务。

AI System 至少需要区分五种成功事件：

| 层次 | 成功条件 | 典型失败 |
| --- | --- | --- |
| Transport / Runtime | 请求完成，模型和依赖没有显式异常 | timeout、OOM、tool transport error |
| Contract | 输出满足 schema、stop、引用与协议约束 | JSON 无效、错误 tool arguments、流未正确终止 |
| Semantic Quality | 内容正确、相关、grounded，并遵循 instruction | hallucination、错误推理、忽略 evidence |
| Policy / Safety | 行为满足权限、安全、隐私与合规边界 | 越权动作、敏感数据泄漏、危险建议 |
| Outcome | 用户或环境中的任务结果达到 intended use | 工单未解决、代码未通过、外部状态修改错误 |

生产意义上的成功更接近这些事件的交集：

```text
delivered_success
= runtime_success
  AND contract_success
  AND quality_success
  AND policy_success
  AND outcome_success
```

某些任务无法为每个请求即时获得 ground truth，因此不能简单把语义错误重新编码成另一个实时 `error_rate`。平台通常组合离线标注集、规则与 deterministic checks、抽样 human review、judge、用户反馈和延迟到达的业务 outcome，并为不同证据保留 provenance 与不确定性。高风险 policy failure 还应作为 hard gate，而不是被大量正常请求在平均值中抵消。

第 67 章可以持续观察 transport/runtime errors 和已产出的质量信号趋势；本章负责定义 semantic success 的口径、样本与决策边界。两者共享 request、model、prompt、retriever、tool 与 environment identity，但不能用可观测性代替规范性判断。

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

### Evaluation Identity 必须包含 Harness 与 Environment

每个 benchmark 维护一套专用脚本，在任务少、协议稳定时最直接。但 Agent evaluation 中，prompt adapter、tool serialization、retry、timeout 与环境初始化都会改变可观察行为；只记录 model 与 benchmark 名称，无法解释同一模型为何在不同 harness 中得到不同结果。

可复现的评估身份至少应写成 `model × benchmark × harness × environment × scorer`。Harness 负责适配与控制流，Environment 负责可执行状态，Scorer 只拥有从轨迹到判断的映射；聚合分数之前必须保存原始 trajectory 与 component-level receipt，才能区分模型退化、adapter drift、工具故障和评分变化。统一协议可以复用执行与观测设施，但每个 adapter 仍需证明语义等价。

统一 harness 降低重复建设，却引入新的兼容层、版本漂移与运行成本。孤立且长期稳定的任务仍可使用专用脚本，但也必须冻结脚本、环境和 scorer 身份，不能把一次聚合分数当作脱离执行条件的模型属性。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-01771:start -->
同一条要求也适用于**过程指令**。模型在最终文本中承诺“已查证”“按步骤执行”只是一条 self-report；若任务要求调用指定工具、保存证据或遵守操作顺序，评估必须观察真实 tool-call trace、环境 affordance 和 effect receipt。只看回答内容的 observer 永远无法区分真实执行与流畅叙述。

```text
process contract + enabled affordances
→ typed action/tool trace
→ environment transition and receipts
→ process-compliance metrics
→ final outcome judgment
```

收紧环境可以阻止不合规路径，却可能让 benchmark 退化为过度脚本化；开放环境更接近部署，却增加替代合法路径和 verifier false reject。因此 process compliance 与 outcome success 必须分开报告，文本 agreement 只作 sensor。选定任务、工具和 provider API 的实验不能外推成所有模型的通用遵从率。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-01771:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-02038:start -->
Prompt 变化也属于 evaluation distribution，而不是报告中的装饰。单一模板在接口稳定时复现成本最低，却会把 parser、措辞和 verbal-confidence format 的偶然性误算成模型能力。可靠性审计应为同一 task family 保留多个语义等价 prompt variants、原始 generations、解析状态和按 variant 的 spread；只有在统一 normalization 后，才聚合 accuracy 或 calibration。

variant 数量增加会抬高推理成本，也可能引入并不等价的改写。因而模板必须有等价性审计，invalid parse 与 abstain 不能默认成错或对。作者的英语多选、1–8B 模型和单一 runtime 结果只说明单 prompt 会隐藏所测条件下的波动，不证明任意开放任务都需要相同数量的 variants。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-02038:end -->

这也是第 35 章和第 59 章的接口：Checkpoint 提供可验证 artifact，Registry 提供不可变版本和 evidence references；第 66 章负责说明这些 evidence 是在什么评估契约下产生的。

### Backend 是 Evaluation Identity 的一部分

同一模型与数据集并不保证同一结论：kernel、precision、decoding 与 harness backend 会改变可观察输出。最简单的单 backend 跑分在环境冻结时合理；跨 backend 发布时，run identity 必须记录执行路径并先做 paired reproducibility check。它换来可解释的结果差异，却增加重复运行成本；差异低于预先声明容差时可保留单 backend。<!-- source-family:SF-2026-ARXIV-2605-19537 --> exact-v1 §3–4 只证明作者比较中的 backend delta，§5 不支持外推为所有 runtime 的固定偏差。

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

### 不确定性必须绑定覆盖假设，而不是装饰性置信区间

点估计便于排序，但遇到 shift 时不能说明错误风险。Conformal-style interval 可以把 calibration set 与 coverage target 交给 evaluation owner，输出带条件的 prediction set；代价是区间变宽、exchangeability 假设和 recalibration 成本。假设失效时应降级为 slice-level diagnostic 而非发布保证。<!-- source-family:SF-2026-ARXIV-2605-19779 --> exact-v1 §2–4 支持其 conformal pipeline 与研究结果，§5 明确不证明任意依赖或分布漂移下仍覆盖。

## 评估对象有四个层次

### Model Evaluation

固定系统外壳，比较模型本身的能力与行为，例如知识、推理、指令遵循、鲁棒性和安全。它适合模型选择，却不能证明完整应用可用。

### System Evaluation

评估 `model + prompt + context + retrieval + tools + policy` 的端到端结果。RAG 的 retrieval recall 与 answer groundedness、Tool Calling 的选择与执行结果，都属于这一层。

### Runtime and Service Evaluation

在目标硬件与 workload 下测量 TTFT、TPOT、goodput、错误率、容量、恢复和成本。质量相同但无法满足 SLO 的 artifact 仍不能发布；延迟更低但输出质量回归也不是有效优化。

### Agent and Outcome Evaluation

#### 从 Final Pass 扩展到 Trajectory、Cycle 与 Checkpoint Decision

<!-- semantic-body-binding:SF-AGENTLENS-REVEALING-THE-LUCKY-PASS-PROBLEM-IN-SWE-AGENT-EVALUATION:start -->
一次通过可能来自脆弱搜索路径、偶然 tool result 或不可复现环境；评估因此要保存尝试分布、关键 action、失败恢复和
重复运行，而不能把 lucky pass 与稳定能力等价。收益是能区分 capability 与 reliability，代价是更多 sandbox 成本和
run-state 存储；确定性短任务仍可用单次执行。作者结果只覆盖其 SWE-Agent、repository 与 harness。
<!-- semantic-body-binding:SF-AGENTLENS-REVEALING-THE-LUCKY-PASS-PROBLEM-IN-SWE-AGENT-EVALUATION:end -->

<!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:start -->
把 issue localization、patch、test、review 与交付拆成孤立 benchmark，会让下游成功掩盖上游 handoff failure。
Full-cycle evaluation 应冻结 repository/environment identity，逐阶段保存 artifact 与 executable verifier receipt，
同时报告 isolated competence 与 end-to-end completion。它提高现实性，却扩大环境故障和 judge 误差；单机制研究
仍需要隔离阶段 baseline。有限 repository 与执行 judge 不构成通用软件工程自治证明。
<!-- semantic-body-binding:SF-SWE-CYCLE-BENCHMARKING-CODE-AGENTS-ACROSS-THE-COMPLETE-ISSUE-RESOLUTION-:end -->

<!-- semantic-body-binding:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:start -->
late-stage checkpoint 差异接近 evaluator noise 时，按单个平均分取最大值会选择偶然赢家。更稳健的 release decision
先用 pointwise floor 排除明显不合格，再做 listwise ranking 与 pairwise refinement，并把稳定性和评估不确定性写入
选择记录。它用更多 judge 调用换较低 selection variance；judge 相关偏差或分布漂移时必须回退独立任务测试和人工复核。
<!-- semantic-body-binding:SF-ROBUST-CHECKPOINT-SELECTION-FOR-MULTIMODAL-LLMS-VIA-AGENTIC-EVALUATION-A:end -->

<!-- semantic-body-binding:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:start -->
Judge 给出的理由不能仅因与标签一致就当作 faithful evidence。Blind、Truth、Flip、Placebo 与 Reveal-after 等 cue
intervention 可分离 outcome anchoring、rationale anchoring 与 explanation drift；evaluation owner 保存 intervention
identity 和 tie-aware metrics，ranking 只消费已校准结果。新增成本是多臂实验和 cue-specific 外推边界；它能发现
rationalization bias，不证明隐藏推理或真实因果链已被恢复。
<!-- semantic-body-binding:SF-FAITHFUL-OR-FABRICATED-A-CAUSAL-FRAMEWORK-FOR-RATIONALIZATION-BIAS-IN-LL:end -->

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

### Evaluator 可以主动制造 Probe，但不能冒充被动观察

离线 judge 只能评价自然轨迹已经暴露的行为；某些 criterion 在普通 run 中很少出现，absence 不能证明系统通过。
In-world evaluator 可以通过原生 dialogue/action 创建 criterion-relevant situation，再观察 Agent response，从被动打分
演进为 coverage-seeking intervention。Evaluator 的 action、环境 revision、触发 criterion 与后续 trajectory 必须一起
记录，因为 probe 本身已经改变被评对象的状态。

主动 probe 提高稀有行为覆盖，却可能诱发本不会出现的 failure、干扰任务、泄漏测试或造成副作用；它只能在 sandbox/
shadow 环境和预算内运行，也不能自动 repair 或 commit。可枚举的 deterministic condition 仍应直接测试。

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

### 从直接 Grid Search 到 Floor-first Diagnosis

即使已有 simulator，也不应把所有候选直接送入昂贵的真机 sweep。随着 MoE、长 Context、并行布局和
拓扑组合增多，单个“吞吐很低”的结果既昂贵又缺少因果解释。更稳健的证据路线先为目标 artifact、runtime
与 hardware revision 建立资源向量：权重与 KV 字节、FLOPs、通信字节与消息数、容量约束，以及经实测校准的
带宽和启动延迟。由此计算 optimistic overlap floor 与 no-overlap floor，再识别随 batch/concurrency 变化的
第一道 binding wall：

```text
versioned resource vector + calibrated hardware profile
→ optimistic / no-overlap lower bounds
→ first binding wall and impossible-SLO rejection
→ observed steady-state service time / floor residual
→ profiler only for material unexplained residual
→ final silicon replay and tail-SLO validation
```

这个 floor 只拥有诊断下界，不拥有可实现性能。它可以廉价排除不可能满足的 SLO，并判断 overlap 优化最多
还有多少空间，却看不到 queueing、host/control-plane、allocator、failure recovery 与实现损耗。用 P50 engine
service time 解释 residual、再用 P99 验证服务 SLO，也不能把两种统计量混成同一结论。校准数据、union/capacity
假设和 software revision 一旦变化，旧 floor 必须失效；否则“理论下界”会伪装成错误的部署预测。

因此三类旧方案仍然共存：小搜索空间可直接真机 sweep；状态交互复杂但候选很多时由 simulator 预筛；资源
瓶颈尚不明确时先做 floor-first triage。作者在特定 MoE、16 张 H20 和披露并发档位上的案例只证明这条诊断
链可执行，不提供跨模型、精度、拓扑或生产流量的通用速度常数。

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

### Kernel Benchmark 必须先闭合 Correctness Identity

Kernel-generation evaluation 必须把 operator semantics、reference implementation、shape/stride/dtype grid、numerical tolerance、target chip/runtime、anti-hack coverage、timeout 与 profiler revision 绑定为同一 EvalSpec。跨芯片比较只有在 correctness gate 先闭合后才讨论 speed，并应同时报告 pass coverage、严格 speed thresholds、trajectory feedback 和 token/device cost。

更广覆盖提高 portability evidence，却会引入 platform-specific prompt/tolerance 与不对称 anti-hack 能力；这种不对称必须显式披露，不能被一个总体排名隐藏。单芯片小 suite 在目标固定的快速回归中仍然合理，但它不能支持跨 operator、chip 或 harness 的通用性能结论。

#### Bit-exact Replay 可以脱离同型硬件，但不能脱离数值路径身份

在同型 accelerator 上重放 inference，最容易把 bitwise mismatch 定位为 artifact 或 runtime drift；硬件已经不可用、
跨 GPU generation 复核或第三方只能获得软件环境时，这个旧前提不再成立。条件分支是在软件中复现被披露的 tensor-core
arithmetic、reduction order、rounding 与 router path，以 exact model/runtime input 重算 reference bits。Evaluation owner
必须冻结 model、weights、operator coverage、dtype、kernel/arithmetic model、input、emulator revision 和 expected digest；
emulator 只拥有 replay evidence，不能接管 production execution 或把“相同输出”升级为硬件相同。

这种路线用较慢的软件执行和更窄的 operation coverage，换取无需同型硬件的确定性复核；主要 failure mode 是 unsupported op、未建模 kernel、
编译器变化或 router tie-breaking 都会制造 false mismatch 或 false assurance。可用原硬件、只需容差正确性或 emulator coverage
不足时，真实设备 replay 与 tolerance-based test 仍应并列保留。`arXiv:2606.00279v1` 的 §3.1、§4.1 与 §3.2、§4.4
只支持作者披露 GPU variants、模型和算术路径上的 bit-exact software emulation；§5 不证明它覆盖任意 operator，也不构成
security attestation、性能等价或未测硬件的保证。

<!-- source-family:SF-2026-ARXIV-2606-00279 -->

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

### Cross-layer Evaluation 不允许下游成功掩盖上游故障

只看最终答案在单层模型任务上成本最低；Agent 系统把 evidence retrieval、tool contract、authorization、session
state 和 response generation 串在一起后，最终成功可能只是下游模型绕过了一个上游缺陷。反过来，一个失败也不能
自动归因给最后的生成器。可定位的评估需要沿 owner boundary 注入和判定故障：

```text
evidence identity / freshness fault
→ tool-schema or execution-contract fault
→ authorization fault
→ session / tenant-state fault
→ final answer and environment outcome
```

每层都应保存注入点、expected invariant、局部 observation 与 repair scope。Schema normalization 只能修复 schema
drift；它不能让陈旧 evidence 变新，也不能把错误 session 变成正确主体。下游 grounded-looking output 因而不能给上游
all-clear，某个 repair 在目标层有效也不能被宣传成端到端通用防护。这种分层增加 fault matrix、运行成本和 attribution
规则；低风险、短链 workflow 仍可先使用 end-to-end smoke test，但 release gate 至少要覆盖高代价 failure boundary，
并同时报告局部故障是否被发现、是否被错误掩盖以及最终副作用。

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

同一条 workflow 在静态 trace replay 与真实环境中会形成不同 request prefix：Tool 返回值、失败重试和分支选择会改变后续 Context。若 benchmark 只重放固定 token 序列，它能隔离 serving regression，却不能验证 runtime 面对动态步骤时的 batching、cache 与 admission。更完整的合同保留真实 step prefix，并在受控环境中执行 Tool，再分别报告静态与 live 轨道：

```text
versioned task and environment
→ real step prefix + tool execution
→ dynamic request stream
→ serving SLO and workflow outcome
```

Live 轨道提高 workload fidelity，也引入环境漂移、不可复现副作用和更高成本；静态 replay 仍适合回归与因果定位。两者不能合并成一个分数，且环境成功不证明模型策略正确，模型完成任务也不能掩盖 serving SLO 违约。

<!-- source-family:SF-2026-ARXIV-2605-18859 -->

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

### Process Reward Model 成为 Sensor 前，先测试 Transformation Stability

直接在原始 reasoning traces 上测 PRM accuracy，在输入格式和错误形态稳定时是必要 baseline；一旦 PRM 被用于 dense reward、
搜索剪枝或 release gate，语义保持的改写、局部重排和对抗扰动可能改变分数却不改变正确性，原始集上的平均指标便不足以
授权它成为 load-bearing sensor。Evaluation owner 应把 transformation family、semantic-equivalence oracle、PRM revision、score
shift、false-positive/false-negative、mitigation 与未覆盖 slice 绑定为同一 receipt；PRM 只提供过程信号，独立 outcome
verifier 和 release authority 保留最终判断。

Stress test 扩大了已知攻击面覆盖，却新增 transformation generator bias、等价性误判、重复查询成本和对 test suite 的
过拟合；通过已知扰动也不证明开放分布鲁棒。固定格式、低风险辅助排序或 outcome verifier 足够强时，原始 benchmark
仍是便宜分支；高风险使用则应在 mitigation 后重测并保留 abstain/降级为非权威 signal。`arXiv:2606.00437v1` 的 §3、
§4 只支持 EST-PRM 对作者所测 PRM、transformations 与 mitigation 的 vulnerability analysis；§7/Limitations 不证明
所有 PRM 共享同一失效模式，也不证明 stress-test pass 等于生产安全。

<!-- source-family:SF-2026-ARXIV-2606-00437 -->

## 从答案评分到可执行证据

<!-- daily-20260621:platform-evaluation-system:start -->
### 语言能耗、迁移基线与 threshold resolution

把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。 Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。 selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。

**Trade-off、failure、共存与回退。** 绝对能耗硬件相关；没有闭源模型，翻译 prompt 不是 native usage，作者将观测 gap 定义为可能的下界而非普遍常数。 HAT 依赖 benchmark hardness 与 source/target choice；三套 benchmark 不代表生成、方言或部署流量。 三 benchmark 与 black-box classification 不证明生成/agent risk；更细阈值不自动校准，重复查询还引入相关样本与成本。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendations and downstream effects`。
- `SF-2026-ARXIV-2606-21954` — primary `arXiv:2606.21954v1`；exact-v1 URL=`https://arxiv.org/html/2606.21954v1`；Method=`https://arxiv.org/html/2606.21954v1 — §4 Proposed XLT Metric: HAT Score; §4.1 Transfer Profile and HAT Score`；Evaluation=`https://arxiv.org/html/2606.21954v1 — §5 Experimental Details; §6 Results`；Non-proof=`https://arxiv.org/html/2606.21954v1 — §8 Limitations`。
- `SF-2026-ARXIV-2606-22179` — primary `arXiv:2606.22179v1`；exact-v1 URL=`https://arxiv.org/html/2606.22179v1`；Method=`https://arxiv.org/html/2606.22179v1 — §3 Problem Setup; §4 Confidence Constructions`；Evaluation=`https://arxiv.org/html/2606.22179v1 — §5 Experiments; §5.1 Setup`；Non-proof=`https://arxiv.org/html/2606.22179v1 — §7 Limitations; §6 Deployment Recommendations`。
<!-- daily-20260621:platform-evaluation-system:end -->

当系统输出代码、漏洞利用、实验方案或可交付文档时，只检查自然语言答案会把最重要的失败留在评估之外。更强的演进路线是：

```text
static answer / multiple choice
→ structured artifact
→ executable verifier or simulator
→ controlled environment interaction
→ outcome、side effect 与 recovery evidence
```

### Longitudinal State：事实必须先于对话，读写路径必须分开审计

对长期 Memory，只把一段 conversation 当作 ground truth 在短历史里很便宜，也适合 smoke test；但它把“当时有效的事实”、
“后来失效的事实”和“系统最终渲染出的对话”混成同一对象。历史变长后，正确答案取决于 query 的 as-of time，错误还可能
发生在写入、更新、检索或生成中的任何一层。更完整的 evaluation object 应先建立 canonical fact ledger：

```text
fact + validity interval + provenance
→ rendered events / conversations
→ as-of-date query
→ memory write audit
→ retrieval / read audit
→ answer and abstention evidence across tenure
```

这个变化把 memory architecture 的比较从一次性 answer score 推进为 temporal state audit。短 tenure 中，保留全部历史
往往是便宜而强的基线；随着历史增长，写入错误、过期事实和检索干扰才逐步显现，架构排序甚至可能发生 crossover。
因此报告必须同时给出 tenure slice、full-history/no-memory controls、write-path precision、read-path recall 和最终答案，不能
把某个单点排名写成长期赢家。

代价是需要构造并版本化事实、有效区间、事件渲染器和 judge-independent checks；合成用户也未必代表生产分布。
所以该 contract 证明的是“如何定位长期状态错误”，不是某种 Memory 在所有用户、backbone 与时长上更优。Memory 的实际
写入、更新与派生状态仍由第 77 章拥有，本章只拥有其 evidence contract 与 release decision。

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

### Compound Artifact 需要 Preservation Contract

对会修改结构化 artifact 的 Agent，final message 不能成为 outcome authority。EvalSpec 应冻结输入 artifact、允许工具、content/format/structure predicates、必须保持不变的区域以及 final artifact checksum；verifier 还需用人工一致性切片和 deliberate mutations 审计自身。这样可以区分“目标内容正确”与“无关区域被破坏”，也能把 failure 定位到具体 predicate 或 mutation。

该路线获得可复算结果与 failure localization，却把 task-spec completeness 和 verifier bugs 变成新的测量风险。Predicate 无法覆盖开放语义时，专家抽检仍是最终 residual owner；通过当前 verifier 只证明当前冻结 contract，没有证明 artifact 在任意下游环境都等价可用。

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

### Deterministic-first 不是拒绝 Judge，而是限制它的权限

Tool-calling benchmark 常在两种 scorer 间摇摆。严格字符串、trajectory 或 state matcher 可复算，却可能拒绝
语义正确的替代路径；LLM judge 能理解开放表达，却会出现 rubric drift、unsupported completion 和重复运行方差。
两者不是“旧 evaluator 与新 evaluator”的线性替代，而应按可验证性分权：

```text
typed tool call + arguments
→ deterministic schema / authorization / state-transition gates
→ executable outcome evidence
→ restricted semantic judge only for residual ambiguity
→ abstain or human adjudication
```

Deterministic gate 只拥有可由 schema、database、tool result 或环境 invariant 证明的 verdict；它不能锁死唯一合法
trajectory。Judge 也只能读取完整 trace 与明确 rubric，不能用流畅 final answer 覆盖缺失 action 或 unchanged bad
state。所有分支都要保存 task/evaluator revision、raw trajectory、tool I/O、environment snapshot、per-gate verdict、
retry 与 final adjudication，才能区分 Agent failure 与 evaluator failure。

这个 layered evaluator 仍需反向被评估：对 expert-reviewed sample 计算 disagreement，重复 stochastic judge run，
报告 slice 与方差，并把 repaired annotation/harness 当作 versioned artifact。2026 年一项 tool-calling validity audit
为这些 failure modes 和 deterministic-first restricted fallback 提供受限证据；它覆盖的是选定 benchmark/model
配置，而且 v1 的 Harness artifact 尚未给出 versioned release，因此不能把作者 agreement 数字写成通用可靠性。
开放语义占主导或 state 不可观察时，human/model judge 仍必要；高风险、可程序验证的 side effect 则不能被 judge
“理解正确”所替代。

### 攻击预算是一条风险曲线，不是 ASR@1

安全评估若只测一次采样，会低估攻击者重复尝试的能力；直接穷举大 `N` 又昂贵。更完整的 subject 是
`model/sampler/attack distribution/budget`，输出应是带 uncertainty 的 `risk(N)` 或达到风险阈值所需预算，
而不是把小样本最大值当作模型固有属性。统计外推依赖 exchangeability、分布拟合和 benign/unbreakable
mixture；自适应攻击、并行相关性或 sampler drift 会破坏这些假设。高风险区仍需实际大预算验证，模型、
sampling policy 或 attack corpus 改变后必须重估。

### Security Agent 评估是一条 Cost-Success-Refusal Curve

Security Agent 的一次成功率不能说明部署价值：更强配置可能通过更多尝试、昂贵模型或更宽 tool policy 获得成功，也可能因 provider refusal 无法执行本来具备的能力。EvalRun 因而要把 outcome、attempt/epoch budget、API/tool cost、refusal/abstain、runtime policy 与 task contamination 放在同一 operating curve 上。

Offensive 与 defensive workload 还不能共享一个 success 定义。CTF 的可验证 flag、incident investigation 的累积得分、错误 action 的副作用与人工恢复成本必须分别记录，再由 intended use 决定 gate。公开任务可能进入训练数据；仅比较不同 provider/model 的观测矩阵也不是随机实验，不能把价格、policy 或 scaffold 差异因果归于 base model。

这条曲线增加 run 数、价格版本和 contamination audit 成本，却能避免把 peak score 当成唯一结论。小规模内部回归仍可使用固定预算单点，只要不外推为完整部署边界。Cybench/BOTS 的作者实验支持这一评估对象模型，不提供任意生产安全 Agent 的通用排名。

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

### 从 Raw Score 到可定位、可校准的 Claim Sensor

一个 sequence-level confidence 把实体、关系、数字和修饰条件压进同一标量，无法告诉系统应该检索哪条 evidence，
也容易让多数低风险 token 掩盖少数关键错误。更细的分支先识别 typed semantic spans，再对每条 claim 产生可校准
的风险信号；多次采样形成的支持关系还可以蒸馏为单次前向 probe，以降低在线成本。

```text
generated answer
→ typed semantic spans / atomic claims
→ model-specific uncertainty sensor
→ deployment-slice calibration and risk-coverage curve
→ evidence retrieval, abstention or human review
```

该 probe 是传感器，不是真值概率。它需要标签或 judge 产生训练目标，依赖内部 hidden state，通常还要为不同 backbone
分别训练，并继承 judge、Wikipedia 与领域分布偏差。低预测风险仍可能是 confident error；外部 evidence、可执行
verifier 和高风险人工裁决继续拥有最终权威。无法取得内部状态或 calibration slice 漂移时，多样本检查与显式检索
仍是更稳健但更昂贵的分支。

### Reasoning Graph Agreement 仍是 Sensor，不是 Truth

多次推理文本可以先拆成 claim/relation graph，再用 versioned embedding 与 graph distance 衡量拓扑一致性，并选择
medoid 作为代表轨迹。这比 token overlap 更接近语义结构，也能暴露局部矛盾；但多个样本可能因为同一模型、prompt
或错误 premise 而高度一致地犯错。

```text
sampled reasoning paths + sampling identity
→ claim/relation graph construction
→ versioned graph embedding and distance
→ agreement / medoid sensor
→ calibration against labels, tools or executable evidence
→ accept, verify or abstain
```

Graph parser、relation schema、embedding model、sample count 与 distance threshold 都进入 EvalSpec。原始 agreement
不是 probability，更不是 truth；只有在 deployment slice 上对独立 ground truth 校准后，才可以支持 risk threshold。
任务有确定 solver、数据库或可执行 verifier 时，它们继续拥有更高证据权；graph agreement 适合决定“哪里值得继续
查证”，不适合直接放行结论。

### 从语义等价到蕴含与互斥根

Semantic Entropy 能合并同义改写，却会把蕴含层级和互相矛盾的高层假设都当成普通多样性。更细的 sensor branch 可以先将采样答案聚成语义类，再构造 implication DAG，把概率质量归并到 maximal roots，并用 roots 之间的 incompatibility 调整不确定性。它回答的是“样本是否集中在兼容的高层假设”，不是“哪个答案为真”。

NLI/parser、采样模型、样本数与 normalization 都属于 sensor identity；pairwise graph 带来 `O(n²)` 成本，短问答上的校准不能外推到长文、代码或线上 abstention。逻辑图之后仍需外部 evidence、claim verifier 与 policy threshold。

### Calibration Slice 必须包含 Language × Model Scale × Estimator Contract

只按领域报告一个 calibration 数字，会隐藏 estimator 在不同生成语言、模型家族/规模和 access contract 下的排名
反转。白盒 probe、token probability、自报告 confidence 与 sample agreement 观察的对象不同，不能共享同一阈值：

```text
claim type + domain
+ generation language
+ model family / scale
+ estimator access contract
→ calibrated operating point for the deployment slice
```

切到 English reasoning 可能改善某个 uncertainty metric，却违反用户语言和信息保真要求；MCQA 通过确定 label 降低
judge ambiguity，也不证明 open-ended factual claim 已校准。小 slice 方差大、维护成本高，但合并异质 slice 得到的
漂亮平均值没有发布意义。样本不足时应扩大不确定区间或 abstain，而不是借用另一语言或另一模型的阈值。

### Atomic Claim 置信度怎样合成整体结论

Claim-level verification 解决了“长答案把真假混在一个总分里”的问题，却自然带来下一问：如果每条 atomic
claim 都只有 `90%`，答案越长，整体置信度是否必然越来越低？答案取决于系统究竟估计哪个事件，以及 claims
之间是什么逻辑和错误关系。

首先必须分开三个 estimand：

```text
factual precision:
  随机抽一条 claim，它被 evidence 支持的概率/比例

all-claims-correct:
  这次回答中每一条 claim 都正确

conclusion-correct:
  用户真正依赖的核心结论成立
```

FActScore 类指标主要估计 factual precision；它不能直接解释为整段文本无错的概率。辅助年份、示例或背景细节
错误，也不一定推翻核心结论；反过来，一个关键 premise 错误，哪怕其余十条都正确，也可能让 conclusion 失效。

#### 只有独立且全部必要时才能直接相乘

令经过 calibration 的 claim confidence 为：

```text
q_i = P(c_i correct | evidence, verifier, deployment slice)
```

若 `n` 条 claims 全部是必要条件，并且错误相互独立，才有：

```text
P(all correct) = product_i q_i
```

十条独立的 `0.9` 会得到 `0.9^10 ≈ 0.349`。这不是 calibration 失败，而是“完全无错”这个事件随 claim 数量
变严格。真实 claims 通常不独立：同一论文版本读错，会让多条 claim 一起错；同一 generator/judge 的盲点也会形成
相关 false acceptance。一般联合概率应写成：

```text
P(c_1,...,c_n)
= P(c_1)
  * P(c_2 | c_1)
  * ...
  * P(c_n | c_1,...,c_(n-1))
```

若完全不知道依赖结构，只凭各自 `q_i`，联合概率只能落在很宽的边界内：

```text
max(0, sum_i q_i - (n-1))
<= P(all correct)
<= min_i q_i
```

所以机械乘法可能过度保守，机械平均又可能掩盖一个致命错误。`min(q_i)` 可以作为 critical-claim hard gate，
但它也不是自动得到的 answer probability。

#### Claim Graph 必须保存逻辑职责与共同来源

Typed claim graph 需要在 `supports` 之外增加：

```text
critical-premise
supporting-detail
derived-conclusion
alternative-evidence-path
contradicts
depends-on
shared-source-family / shared-verifier
```

对一个 derived conclusion，premises 正确仍不保证推导正确，因此推理边本身也需要 evidence：

```text
r_e = P(conclusion follows | required premises are correct)
```

简单 critical path 可以估计为：

```text
P(conclusion correct)
≈ P(required premises jointly correct) * r_e
```

若两条真正独立的 evidence paths 都能单独支持同一结论，关系是 logical OR，而不是 AND；冗余证据可以提高
robustness。但官方 Blog、新闻转载和社区摘要若都来自同一论文，只是一个 Source Family，不能作为三条独立路径。
Source digest、版本、作者/机构、引用 lineage 与 verifier family 必须用于相关性分组。

#### Raw Score 只有经过标签校准才是概率

检索相似度、NLI entailment、judge score、semantic entropy、`P(True)` 和 source count 都只是 features。可以为每条
claim 构造：

```text
z_i = [
  support_score,
  contradiction_score,
  retrieval_margin,
  independent_source_family_count,
  authority / freshness,
  semantic_entropy,
  self-evaluation P(True) / P(IK),
  model or verifier disagreement,
  OOD score
]
```

然后在有可靠 correctness labels、且与 deployment slices 匹配的 calibration set 上学习：

```text
q_i = Calibrator(z_i)
```

Calibrator 可以是 logistic/temperature/isotonic 等简单映射；重点不是模型复杂度，而是独立 calibration/test split、
subject/verifier identity 与 reliability。预测为 `0.8` 的 claim cohort 应约有 `80%` 在声明 verifier 下正确；否则
`0.8` 只是排序分数。还应报告 Brier/ECE、AUROC/AUPRC 和 risk–coverage curve，并按 domain、language、freshness、
risk 与 source availability 切片。Distribution 或 verifier 变化后必须重校准。

Answer-level calibrator 可以继续读取 critical-path confidences、dependency depth、source-family correlation、
contradiction、inference-edge score、semantic entropy 与 retrieval coverage，直接预测 conclusion / complete-answer event。
它不应删除 claim-level ledger：一个漂亮的总分无法告诉系统应该删除哪条 claim、继续检索什么或把哪个冲突升级给人。

#### 自动 Metric 不必冒充人工判断，也可以用来减少人工样本

`auto-only` 用规模换偏差，`human-only` 用可信度换成本；二者不是只能二选一。若目标是估计一个系统总体质量或两个系统
的 population-level 差异，可把大量自动 metric 视为廉价但有偏的辅助变量，再用同分布抽取的少量人工标签估计并校正
这份偏差。Prediction-powered inference 一类方法因此改变的是 estimator，而不是把 metric 升级为 ground truth：

```text
large unlabeled population + automatic scores
+ smaller representative human-labeled sample
→ estimate metric residual / correction
→ bias-corrected population estimate + confidence interval
```

这条路线获得更高 statistical power 或更少 annotation，却新增 sample-design、metric/human correlated error、
distribution drift 与 interval interpretation 责任。Paired design、unpaired design、parametric 或 non-parametric procedure
不是可互换实现；必须冻结抽样单位、target estimand、配对关系和缺失标签策略。区间描述的是声明 population 与假设下的
系统级估计，不是单条回答正确概率，也不能授权单次高风险 action。Metric 与人工 residual 的关系在新 domain、模型或
prompt distribution 上失效后，必须重新标注和校准；样本很小、目标不可稳定标注或错误高度相关时，保守的人工评估仍成立。

#### Confidence 最终服务于 Risk–Coverage Decision

系统不需要所有回答都达到 `100%`；它需要在错误和拒答之间做显式决策。若错误回答代价为 `C_wrong`，拒答/
转人工代价为 `C_abstain`，回答的简化期望损失为：

```text
Loss(answer)  = (1 - q_answer) * C_wrong
Loss(abstain) = C_abstain
```

只有当：

```text
q_answer > 1 - C_abstain / C_wrong
```

才值得直接回答。高风险场景提高 threshold，并把 critical claims 交给 executable verifier / expert；低风险探索可接受
较低 threshold。若要求整篇 critical claims 的 family-wise error 不超过 `delta`，union bound 给出保守预算：

```text
P(any critical claim wrong)
<= sum_i (1 - q_i)
```

它会推动系统减少不必要 claims，而不是无限堆砌“有 90% 把握”的细节。Conformal prediction 可以在 calibration
distribution 与 exchangeability 等假设下，为候选集合或 component 提供 coverage guarantee；distribution shift、错误
acceptability function 或 correlated adaptive sampling 仍会破坏解释，不能写成开放世界 truth guarantee。

最终可靠路径是：

```text
answer draft
→ atomic claims + criticality / dependency graph
→ authoritative retrieval and source-family dedup
→ support / contradict / insufficient evidence
→ semantic / model / verifier uncertainty
→ claim and conclusion calibration
→ answer / omit detail / retrieve more / ask / abstain / escalate
```

这条链把“模型感觉自己知道”降级为一个 feature，把 evidence 与 verifier 提升为独立 authority，再由风险政策决定
coverage。真正要优化的不是让 confidence 数字看起来更高，而是在相同 coverage 下减少 false answers，或在相同
risk 下回答更多问题。

#### 对抗性相关错误：低熵与高共识也可以稳定地错

Semantic entropy、self-consistency 和 majority vote 的有效性还依赖一个未必成立的前提：错误 samples 具有足够
多样性，正确答案能形成更稳定的 mode。若同一个 checkpoint、训练过程或攻击主动把关键元素塑造成一致的错误值，
系统会观察到 fluent、低熵、高 agreement 的输出，却没有获得任何独立 truth evidence。

```text
same model / checkpoint family
→ correlated false mode
→ repeated samples agree
→ confidence estimator reads stability
→ stability is misclassified as correctness
```

这不是简单增加 `N` 能修复的问题。更多同源 samples 只会更精确地估计被塑造后的错误分布；让同类模型互审也可能
共享相同盲点。Evaluation 必须把“自然错误下校准有效”与“对抗性或分布改变后仍有效”分开，并至少记录：

```text
generator / checkpoint / training lineage
selector and verifier family
independent ground-truth coverage by critical element
unverified element count and correlation group
accepted-correct / accepted-wrong / abstain
```

Fool's Gold 的作者实验以 safety-removal 后的 open-weight artifact 构造一致错误分布，为这条 epistemic boundary
提供受限证据：在其“攻击者没有领域 expert、真实 reference 或 retrieval-verified source”的 threat model 中，重复
采样、consensus 和若干 label-free observation surface 不能稳定区分 decoy 与正确答案。本文不吸收其 defensive-
deception recipe，也不把 chemical/biological 结果外推；模型、judge、single-expert audit、escape tail、repair erosion
和 threat coverage 都限制了结论。

长期设计结论只有一条：**没有独立 ground truth 时，同源一致性只能支持 distribution description，不能支持 truth
acceptance。** Partial verifier 也必须按 critical elements 报告 coverage；平均验证一部分细节不能掩盖一个未验证的
致命 claim。可执行 verifier、权威 evidence、独立专家或 abstention 仍是高风险结论的最终分支。

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

### Judge 先证明看见了目标变化，再谈总体准确率

Evaluator 的 aggregate accuracy 可能同时掩盖两种相反失败：目标事实已经改变，judge 却保持原 verdict；无关表达被改写，judge 又错误地改变 verdict。因而 construct validity 不应压成一个标量，而应至少有两条受控 intervention arm：

```text
target-changing edit   → verdict should change   → sensitivity lower bound
target-preserving edit → verdict should remain  → invariance lower bound
```

两条 arm 的样本身份、人工裁决、edit provenance 与置信区间必须分别保存。人工也会误判 target-changing edit，有限 control family 也只能给出边界；但这种分解能防止一个看似不错的总分把“对真正变化不敏感”与“对表面变化过敏”互相抵消。它是现有 judge calibration 的前置条件，不替代 executable verifier、domain expert 或 deployment outcome。

多个 uncertainty scorer 的 supervised ensemble 也只能在有代表性的标签与目标模型访问合同下作为 sensor。Black-box consistency、token probability、reflexive judge 与 claim-level score 观察不同误差面，组合后可能改善 AUROC / calibration，却会引入标签成本、domain shift、grader correlation 与 scorer availability。原始相似度、entropy 或 ensemble output 仍不是概率；必须按 deployment slice 校准，并把 abstain、human escalation 与风险覆盖率作为最终决策输出。

### 多轮评估要区分 Context Length 与 Intent Supersession

多轮 Agent 评估不能把“上下文更长”与“用户意图发生 supersession”混为一项。EvalSpec 应显式保存 current function、arguments、revealed/withdrawn values、revision 与 function-switch event，并用 turn-matched no-change control 区分长度压力和状态更新失败。

Final anchored verifier 可以提供可扩展 outcome evidence，却不能证明每个中间 transition 正确。真实用户风格、多意图同轮和含糊修订还需要额外切片；Agent 的 Context、Memory 与 Workflow 可以消费这些状态边界，但 evaluation owner 仍负责定义 transition identity、control arm 与最终可比较性。

### Scoring Rule 要奖励任务效用，而不是只奖励“像答案”

通用 judge score 易部署，却会把表达偏好混入正确性。任务效用可分解为可验证结果、校准置信与拒答成本，再用 proper scoring/utility contract 汇总；这让 release decision 可解释，却要求明确代价矩阵。代价未知时应保留分项指标。<!-- source-family:SF-2026-ARXIV-2605-20490 --> exact-v1 §2–4 只支持 ECUAS 的定义与论文实验，Limitations 不允许把该权重当成跨任务真值。

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

多模态生成还提供一条低训练成本分支：冻结一个 image-conditioned reader，用目标 prompt 在生成图像条件下的
log-likelihood 作为 **read-back reward sensor**。它测量的是“该 evaluator 能否从图像恢复提示语义”，不是人类
偏好、事实正确、物理一致或安全。Evaluator model、tokenizer、prompt template、normalization 与 image transform
都必须进入 run identity，并与 aesthetic、safety、artifact、physics 等独立 evidence 并列。

该 sensor 免去单独训练 reward model，却继承 reader 的语言先验和视觉盲点；policy 进入训练回路后还可能学会
制造对 reader 友好、对人或真实世界无意义的捷径。因此必须保留独立 holdout、policy-shift red team、跨 evaluator
迁移与停止条件。开放式语义对齐可把它当廉价 proposal score；涉及高风险内容、细粒度视觉质量或可执行物理状态
时，专门 verifier 与人工裁决仍拥有最终 gate。

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

评估“研究 Agent”时还要进一步冻结 training、serving、sandbox、evaluator 与 budget，只让 Agent 拥有明确的
data-strategy 决策权；否则一次性能变化无法归因于研究能力。每轮 checkpoint 都应作为不可变 evidence，final
checkpoint 不能默认等于 best checkpoint，因为反馈驱动的搜索可能越过峰值后退化。Controlled substrate 用较低
生态真实性换取更清楚的归因；通过后仍要在开放栈复验，并把 stop rule、checkpoint selector 与 EvalSpec 一起版本化。

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

#### 从明确 Issue 到交互式 Spec：先分开需求访问与实现失败

明确 issue、固定 tests 的 benchmark 对局部修复仍然理想：输入、预期行为与失败位置清楚，回归也容易复现。但从零构建 repository 时，agent 常先面对不完整 product intent。若只看最终 tests，需求从未被告知与 agent 已获得需求却没有正确实现会被压成同一种失败，评测无法判断问题出在 information access 还是 execution conversion。

一种可复现的交互式构造从已验证 source repository、tests 与精确 GroundPRD 出发，再有界隐藏 constraints，生成 fuzzy PRD 与 User Agent Data。Agent 可以在固定 question budget 内查询；user simulator 只揭示被冻结的 hidden constraints；最终 repository 同时接受 black-box behavior、artifact、structure 与 interaction diagnostics。evaluation identity 因而必须冻结 source repo/tests、hidden-constraint set、user simulator、question budget、container/image、agent harness 与 scorer。恢复更多 constraints 只是需求访问证据，不等于实现正确；通过 tests 也不能反推交互过程没有遗漏。

这种路线增加了 repository/test bias、user-agent bias 和 framework/environment identity，因而不能线性取代 static issue benchmark。前者适合诊断模糊需求到完整 artifact 的链路，后者仍适合局部 repair 与长期 release regression。公开证据覆盖 480 tasks、12 languages、50-task Lite split、六个模型与 Claude Code，并附 OpenHands 分析；它不提供跨所有 coding workload 的通用排名，provider precision、并发和生产 latency SLO 也不是该实验的声明范围。

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

### 可复用状态的评估必须冻结 Visibility / Commit Boundary

Matched budget 仍可能比较了不同问题。一次性 request-owned cache 可以在看到当前 query 后选择要保留的状态；共享
prefix 或可复用 KV 必须在未来 query 到达前 commit。若 benchmark 允许后者提前看到 query，它测到的是 relevance
selection，不是 reusable information retention。两种方案都合理，但不能共享同一 leaderboard 结论。

评估系统因此要把 state commit 时可见的信息写进 EvalRun identity，并同时冻结 model、tokenizer-expanded length、
attention backend、implementation revision、budget 与 decoding contract。除目标方法外，还要有 uncompressed 与
简单 start/recent 等 controls；用 paired records 和 uncertainty 检查 method gap，再单独测量 backend、tokenizer
overflow、OOM refill 与 harness 变化：

```text
deployment visibility / commit boundary
→ matched model, tokenizer, backend, revision and budget
→ query-aware vs query-agnostic protocol split
→ uncompressed + trivial controls
→ paired uncertainty and confound measurement
→ publish, qualify or withdraw ranking
```

更严格的合同会牺牲一部分“所有方法都能跑”的可比性：某些 compressor 只能在特定 backend 或可见性条件下工作。
但当 harness/backend effect 与 method gap 同量级、tokenizer 后长度越过模型边界，或实现无法遵守生产 commit 语义时，
正确动作是撤回或限定 ranking，而不是继续输出精确名次。这不否定 query-aware 的 one-shot cache；它只阻止把其收益
外推到 query-agnostic reusable state。KV 生命周期与压缩机制由第 45 章拥有，本章拥有比较声明能否成立。

### MoE Load Balance 不能替代 Functional Specialization

expert token count 与 routing frequency 易采集，适合发现过载，却不能回答 expert 是否真的学习了不同功能；均匀路由甚至可能掩盖同质化。evaluation contract 应把 routing specialization、representation rank、domain isolation、routing stiffness 与 n-gram expertise 等诊断分开，并通过受控 intervention 检查指标是否对应行为变化。

这提供比频率图更接近机制的证据，也付出多指标解释、数据域设计、干预成本和潜在 metric gaming；诊断相关性仍不等于因果完备。模型不使用 MoE 或缺乏可干预路由时，常规质量/负载评估继续成立。exact-v1 只支持其披露 benchmark、模型、五类指标与 intervention，不证明这些指标跨架构、语言或生产流量具有统一阈值。

<!-- source-family:SF-2026-ARXIV-2605-18498 -->

### Component Priority 只能是 Action Evidence

只看 Agent 最终分数，在系统组件多、试验昂贵时无法回答下一次应改哪里；component-level update priority 可以把错误归因、干预成本与预期收益组织成中间 action evidence。但 optimizer 只拥有试验排序权，不能把 priority 当作最终质量结论；每次更新仍要用多步 held-out replay 验证真实改善，并保留未被选择组件的反事实基线。

分层信号能减少盲目搜索，却增加标签、归因与回放成本，也可能让易测组件挤压真正瓶颈。任务简单或组件耦合无法分解时，端到端 gate 仍是可信基线。arXiv:2605.22505v1 仅支持作者 harness 中 priority signal 与改善的受测关系，不证明 priority 在任意 agent architecture 上具有因果性。

<!-- source-family:SF-2026-ARXIV-2605-22505 -->

### Attribution 是 Versioned Evaluation Contract

单一 attribution score 在解释对象、受众和风险固定时便于比较；一旦既要解释模型行为、又要支持审计或用户申诉，同一个分数会混合不同证据标准。Evaluation run 应显式绑定解释对象、受众、允许的 evidence、faithfulness/citation evaluator 与失败处置；scorer 只产生 evidence，release 或 governance owner 决定是否接受归因声明。

多协议合同提高责任清晰度，代价是 evaluator 版本、阈值和兼容矩阵的维护；低风险内部调试仍可采用单一 proxy。arXiv:2605.23080v1 的框架与实验只支持其 attribution taxonomy 和受测设置，不证明某一 attribution metric 对所有用户、模型与任务都忠实。

<!-- source-family:SF-2026-ARXIV-2605-23080 -->

## Evaluation Identity 还必须覆盖测量路径、工作负载与规范目标

Evaluation 的结果不只可能被 scorer 改写；在结果进入 scorer 之前，client 如何施压、输入如何构造、规范如何拆成可测试命题，都可能改变最终结论。三者因此应依次进入 EvalRun identity，而不是作为“生成数据的脚本细节”留在报告之外。

### Benchmark Client 也是 Measurement Instrument

单进程、asyncio client 在低并发时路径短、复现容易；并发升高后，client 自己的 event loop、连接池和请求队列可能先饱和，服务端收到的 arrival process 已经不是声明的 workload。此时 TTFT、TPOT 或吞吐下降不能直接归因给 engine。measurement owner 应冻结 client architecture、进程/连接数、load-generation policy、clock 和 client-side queue telemetry，再由独立 server trace 确认请求何时真正到达。

这能区分 generator saturation 与 server saturation，却增加分布式 load generator、时钟对齐和结果合并成本；generator 过度并行还可能把网络或协调层变成新瓶颈。低并发 correctness smoke test 仍可使用简单 client；高并发容量结论则应在 client queue 出现前降级或重跑。`arXiv:2605.24217v1` 的 §3 与 §4 支持作者识别并评估的单进程排队偏差，§5 不证明每个 benchmark client、网络或生产拓扑都有相同瓶颈。

<!-- source-family:SF-2026-ARXIV-2605-24217 -->

### Long-context Reasoning 要冻结 Position、Content 与 Length

固定长度和 filler，只移动 target，适合隔离位置效应；只增长长度，则适合观察容量边界。真实 reasoning benchmark 同时改变 target position、intervening content 与 context length 时，若不把三者联合版本化，所谓“context rot”可能只是题目难度、干扰语义或位置分布变化。dataset owner 应发布可复算的 factor grid，harness owner 固定 tokenizer 后长度与 packing，scorer 只评价冻结任务，不得在运行中重采样这些坐标。

联合设计提高归因力，却扩大样本矩阵、成本和多重比较风险；受测模型、任务或 filler family 变化后还要重新校准。只需验证一个确定性最大长度或特定位置回归时，单因素测试仍更直接。`arXiv:2605.23170v1` 的 §3 与 §4 支持作者在九个模型、GSM8K 与 ARC-Challenge 上的三因素受控评估，§7 不证明该失效形态跨任务、语言或所有长上下文架构成立。

<!-- source-family:SF-2026-ARXIV-2605-23170 -->

### 长篇 Policy 要先编译成 Versioned Atomic Tenets

人工按整份 constitution 或 system card 给一个总体合规分数，在规范短、风险低时成本最低；规范变长且多轮交互会组合触发条款后，总分无法指出是哪条义务、哪个版本或哪段对话失守。更可审计的路径是由 policy owner 冻结发布版本，evaluation compiler 把它分解为带来源位置的 atomic tenets，再生成多轮对抗场景、保存完整 transcript，并由与生成器分离的 validator 回到原条款确认 finding；release owner 最后决定接受、修复或豁免。

这种编译让 failure 可定位和回归，却引入 tenet 漏拆、语义重叠、adversarial generator 偏差、validator 同源偏差和高昂人工复核。规范很短、条款可由确定性 rule 直接检查时，静态 checklist 仍合理；高风险 finding 还需人工与真实 deployment control 复核。`arXiv:2605.24229v1` 的 §3 至 §5 支持作者对已发布规范的 atomic-tenet 与多轮审计流程，§6 不证明其条款抽取完备、evaluator 无偏或结果等同真实部署安全。

<!-- source-family:SF-2026-ARXIV-2605-24229 -->

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

### “不再回答”不是 Deletion Evidence

用目标问题的准确率、输出概率或 refusal rate 验证 suppression，在目标只是阻止某类输出时成本低且合理；但当系统声称已经从训练所得能力中删除指定 forget set 时，同一现象也可能来自拒答层、输出过滤或局部 model edit。此时“模型不再给出原答案”不能证明训练影响已经消失，evaluation contract 必须把可验证对象从单次输出改为相对重训练参照的、数据集定义的删除命题：

```text
training dataset D + forget set F + training procedure / revision
→ provenance-bearing reference: Train(D \ F)
→ candidate: Unlearn(Theta_D, F)
→ explicit distance / tolerance on a frozen behavior distribution
→ retain-utility checks + adversarial recovery and derived-capability probes
→ deletion-qualified verdict or suppression / editing-only verdict
```

其中 dataset owner 负责 `D`、`F`、训练过程与 reference provenance；evaluation owner 负责 distance、probe distribution、容差和 verdict；单个 scorer 只计算被冻结的观测，不能自行把拒答升级成 deletion claim。这样能把“控制可见输出”与“移除训练影响”分开，也能发现原答案被压制、推导能力却仍可恢复的 failure。代价是 reference retraining 昂贵且受随机性影响，distance 和 threat model 的选择也会改变结论；把一个随机种子的 reference 当作唯一真值、只测原句而不测派生能力，或把 retain-set 中重新学到的能力归因于 forget set，都会制造错误保证。

当 provenance-bearing retrain reference 不可构建、reference 本身不唯一或恢复 probes 覆盖不足时，系统仍可把 suppression、editing 或 policy alignment 作为有用目标继续评估，但应发布对应的受限指标，不宣称 dataset-defined deletion。`arXiv:2606.27379v1` 的 §2 与 §4–§5 支持上述定义、参照和派生能力检查；§3 只分析现有 benchmark、metric 与对抗恢复证据，§6 及附录 A–B 还保留了 reference 可行性、policy removal 与 deletion 的区别以及多模态扩展边界。它是一篇 evaluation-contract position paper，不提供新的 unlearning system、公开 artifact 或可外推的通用删除成功率。

<!-- source-family:SF-2026-ARXIV-2606-27379 -->

### Open-world Evaluation 必须重复发生，而不是一次验收

封闭 benchmark 在环境静态时可复现；工具、网页与事实持续变化后，一次 snapshot 会把过期知识误当能力。Evaluation owner 应维护 recurring probes、environment revision 与 change receipt，并区分模型退化和世界改变。收益是发现时效性 failure，成本是维护基准与重标注；静态数学/代码任务仍可沿用固定集。<!-- source-family:SF-2026-ARXIV-2605-20520 --> exact-v1 §2–3 只证明论文的 open-world protocol，§2.4 不支持所有领域的更新频率。

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

### Generated Evaluator 先成为 Artifact，才能成为 Scorer

Agent 数量少、任务协议稳定时，由领域 owner 手写 EvalSpec、metric 与 deterministic verifier，虽然扩展慢，却最容易审计，也仍是合理基线。任务、framework 与 requirement 快速分化后，生成器可以从 source、需求和 execution trace 提议 evaluation plan、metric code、trace parser、dependencies 与 report；约束也随之改变：这些输出不能因“代码已生成”或“第一次运行成功”就获得评分权，而要作为独立的 versioned evaluator artifact，绑定 generator、input/trace schema、适用域、依赖、代码与 report revision。

Evaluator admission 应保存一条不可跳步的状态链：`draft → executable → non-vacuous → meta-evaluated → admitted`。生成器只拥有 proposal；execution harness 在干净环境中重建依赖、消费声明的 trace 并产出 `Eval@1` receipt；evaluation owner 用空输入、已知正反例和 deliberate mutation 检查 parser、metric 与 report 是否真正区分目标 failure，而不是恒定返回、静默丢字段或只复述 requirement；独立 meta-evaluator、确定性 anchor 与人工样本再核对 construct validity、scope expansion 和 disagreement。只有 admitted revision 才能参与 candidate promotion 的 evidence bundle，release owner 仍独占 promote、hold 或 rollback 的 commit authority，不能让生成器用自己生成的 evaluator 自证候选通过。

这条链以更少的逐任务手写工作换取可复用 evaluation skills、运行轨迹覆盖和更清楚的 evaluator-failure 定位，但新增 instrumentation、trace storage、dependency sandbox、meta-evaluation 延迟与人工标注成本。常见 failure 包括 plan-code drift、跨 framework API 不兼容、trace schema 缺字段、metric 可运行但 vacuous、judge 与人工对 construct 的理解不一致，以及 generator、meta-evaluator 和被测 Agent 的 common-mode bias。低规模稳定任务继续沿用人工 EvalSpec 与 deterministic verifier；任一 admission gate 失败、证据冲突或适用域漂移时，应回退人工/既有 verifier、修复后生成新 revision，或将结果降为诊断 signal，而不是参与 promotion。

`arXiv:2605.11378v1` 的 §2、§3.1–§3.3、§4.1–§4.4 与 Appendix A 只支持作者六阶段 EvalAgent、evaluation-skill package、AgentEvalBench/meta-evaluation 和 20 个 Agent × 两类 requirement 的实验；§6 与 §4.4 还把证据限制在 Claude-family backbone、预收集 trace、62.5%–65.0% first-run executability 和主观 meta-evaluation。它不证明自动生成 evaluator 等同 ground truth、能跨 framework 直接执行、上述 admission gate 足以保证 construct validity，或 production promotion 可以取消人工与可执行 verifier；论文命名了代码仓库，但未披露本次证据所用的 immutable commit。

<!-- source-family:SF-AN-EMPIRICAL-STUDY-OF-AUTOMATING-AGENT-EVALUATION -->

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

### 层级 Attribution 要保留路由路径，不能只给总分

系统有多级 router/evaluator 时，总体成功率无法定位 failure owner。评估记录应保存每级输入、选择、证据与最终 outcome，再做 hierarchical attribution；收益是可定位回归，代价是 trace 成本与 attribution model 偏差。低风险单路径系统仍可只记端到端结果。<!-- source-family:SF-2026-ARXIV-2605-22866 --> exact-v1 §3–4 与 Appendix A 只支持作者的层级归因，§6 不证明观察相关性等于因果责任。

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

<!-- source-family:SF-2026-ARXIV-2605-27789 -->

同一个 judge 在输入证据量、答案长度或呈现顺序不同的情况下可能改变偏好，因此“换了 judge 后结论一致”也不足以证明比较稳健。更可审计的比较要冻结 evidence budget 与 answer budget，随机化顺序，按相关样本/任务 cluster 估计不确定性，并在预注册假设上用第二个独立 judge 或人工子集复核。它用更多调用、标注与统计复杂度换取较少的长度偏差和伪独立样本；两个 judge 共享训练偏差时仍会一致地错。低风险快速筛选可以保留单 judge，高风险上线或模型排序则不能把单次 win rate 当作普遍质量事实。

**Online-only。** 认为真实流量自动产生真实结论。替代方案是把 offline control、shadow、canary 与持续线上观测组合起来。

**Metric-to-production automation。** 一个阈值直接移动 `production` alias。替代方案是让 gate 同时检查 identity、quality、safety、SLO、cost 与 exception policy。

**Store-results-without-contract。** 保存一堆 metrics，却没有 dataset、scorer、environment 和 subject identity。替代方案是把 Evaluation Run 作为不可变证据对象。

**Eval-set overfitting。** 反复根据同一 hidden set 调 prompt 或模型，使它逐渐成为训练信号。替代方案是分离 development、regression 与 held-out suites，并控制访问和刷新策略。

**Transition ledger without a measured null。** 用一次 greedy decode 比较 checkpoint 前后，把 sampling、batching、
长度截断或 grader 波动制造的状态翻转写成“能力获得/丢失”。替代方案是把 frozen/no-op subject 通过完全相同的
pipeline 多次运行，对每个 transition statistic 单独测 noise floor；以 pooled baseline 和 multiple-testing control
做 per-item 判断，并预先计算 transition-level power。平均准确率稳定不意味着 item ledger 的 null 为零。

这个 control 还必须记录每个 checkpoint 的 completion length、truncation、sampling/batching config 与 seed。同一
token cap 下更啰嗦但最终正确的轨迹可能被误写为能力退化；三次训练 seed 中任意一次反转结论，都说明单 seed
comparison 没有足够 authority。Measured null 只能界定当前 model、harness、sampling budget 下的 detection floor，
不能把“在 pass@k 中未到达”升级为模型分布绝不支持，也不能由短 LoRA/self-training run 否定更长训练方案。

<!-- source-family:SF-2026-ARXIV-2605-27712 -->

序列中每一步的置信度还必须遵守时间边界。离线分析若用完整轨迹训练 belief estimator，再回填早期 checkpoint，容易让未来 evidence 泄漏进过去的置信度；得到的 calibration 看似更好，却不能在线复现。Prefix-safe contract 要求第 (t) 步的 belief 只读取当时可见的 prefix，并把 probability calibration 与 candidate ranking 分开：前者回答概率是否可信，后者回答候选排序是否有用。

这种时间切片会减少训练可用信息并提高每步标注/存储成本，但能避免不可部署的 hindsight score。完整轨迹分析仍适合事后诊断，不能直接拥有在线 stop/commit authority；只有 prefix-safe、按 checkpoint 评估并报告 calibration error 的估计器，才可参与运行时阈值决策。现有结果属于披露任务与轨迹的实验性证据，不证明跨领域 calibration 自动迁移。

## 工程实践：从最小可信闭环开始

### Agent 评估必须声明 Runtime Coverage

纯 LLM benchmark 主要测 prompt→completion；Agent workload 还包含工具、状态、orchestration、重试和 runtime policy。评估对象应从 model alias 扩展为 `model + runtime + tool/environment generation`，并用 typed trace 说明哪些路径真正执行。生产 trace 或十几个应用可以暴露新压力，但只是 workload characterization，不能证明样本代表全部 Agent。

为降低反复调参污染，holdout 还应冻结，场景与 runtime coverage 一起版本化，并通过多次运行区分随机波动。Trace coverage 改善可诊断性，却不等于 evaluator 覆盖全部语义错误；场景代表性、隐藏副作用和 judge 漏检仍需独立审计。

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

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14000:start -->
autoformalization不能以kernel acceptance作为唯一质量gate；还应审计semantic faithfulness、Mathlib reuse与cross-file reuse。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-14000:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16603:start -->
data-analytic Agent 应把 query/transform/result 编译成可执行 verification graph，使数值结论可由独立节点重放而非只审 prose。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16603:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19057:start -->
当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19057:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19613:start -->
coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19613:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24124:start -->
将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24124:end -->

### 从模型名评分到 Versioned Evaluation Object

外部推理服务中，“同一个模型”可能对应不同 endpoint、量化、上下文策略、价格与运行时版本。评测原子对象因此应是 versioned endpoint/model configuration，并在同一 contract 中绑定 workload、质量、能耗、延迟、价格、失败率和 evaluator identity。Provider drift 或不可观测字段存在时，结论只能属于该配置与时间窗口。

<!-- source-family:SF-2026-ARXIV-2605-00300 -->

版本比较也不能只看 aggregate delta。均分不变时，item-level harmed/helped churn 仍可能很大；release gate 需要重复采样、within-model reliable-change interval、sampling variance 与 harmed/helped ledger，才能区分随机波动、能力迁移和真实兼容性退化。单一阈值不应跨模型族或 benchmark 外推。

<!-- source-family:SF-2026-ARXIV-2604-27405 -->

Prompt interface 同样属于评测身份。跨模型比较要区分 frozen common-prompt contract 与 per-model optimized deployment contract：前者测统一接口下的可比性，后者测各自最佳可部署能力。混用两者会把 prompt mismatch 误归因给权重，或把额外 search budget 隐藏在模型排名中。

<!-- source-family:SF-2026-ARXIV-2604-27637 -->

当被测对象是 code agent 时，verifier 也不是附属脚本。Special-judge synthesis、test-case parallelism、multi-node sandbox、配置化 suite 与失败重放共同决定 reward truth、吞吐与复现边界；generated judge、sandbox policy 和任务覆盖必须版本化，不能由一次通过推导任意程序正确。

<!-- source-family:SF-2026-ARXIV-2604-27467 -->

Simulator 则必须拆成两个可能冲突的 contract：behavioral realism 回答“像不像真实用户”，tester reliability 回答“能否保持系统相对判断”。二者应共享 canonical session schema、loss accounting 与 applicability metadata，但分别出账；有限语言、用户群与 simulator family 的相关性不证明生产迁移。

<!-- source-family:SF-2026-ARXIV-2604-27878 -->

### Evaluation Object 必须携带依赖图、时间与可复现条件

Workspace Agent 的任务不是在互相独立的附件上答题，而是在文件依赖图中读取、修改并保持跨文件不变量。Evaluation object 因而必须保存初始 workspace、依赖边、允许与禁止的 mutation、终态判定和副作用；只比较最终文本会漏掉错误读取、隐式破坏和未授权写入。真实 workspace 提高部署相关性，却增加 fixture 版本、reset 和 judge 维护成本，静态 QA 仍适合隔离单步理解能力。

<!-- source-family:SF-2026-ARXIV-2605-03596 -->

只保存原始 source code 与 environment，能够最忠实地重跑同一实现，却会把“问题是什么”和“当时怎样解”锁在一起，
依赖变化后也难区分任务漂移与实现腐化。Declarative Task Contract 可把问题描述、资源、输入输出、metric、执行条件
和 candidate solution 分离：benchmark owner 版本化 task spec，Agent 只提交候选，harness/verifier 依据 contract
决定接受。它支持独立实现和跨时间复现，但要承担 schema 表达力不足、自动抽取错误、环境缺失与 verifier common-mode
failure；无法完整声明的任务必须保留 reference code/container、回归测试和人工 adjudication。

这里的“可复现”只表示在声明条件下可重建判定过程，不自动证明两个实现语义等价。exact-v1 的证据只覆盖 Croissant
Tasks vocab、论文实验与其局限讨论；Agent 生成的 reproduction 不证明 schema 完备，也不能外推所有 benchmark。

<!-- source-family:SF-2026-ARXIV-2605-29786 -->

能力结果还必须绑定时间。模型 release、elicitation、tool scaffold 和评测日期之间的 frontier lag，会让一个当时正确的测量被误读为当前系统能力；因此 release-grade 结果不能只写模型名和分数，而要作为带版本与日期的 immutable evaluation object。对 frontier safety claim，机构权威和 venue 也不能替代可复现条件：至少需要 artifact、配置、运行预算、evaluator 与独立 rerun 边界。

<!-- source-family:SF-2026-ARXIV-2605-04135 -->

这份可复现性不是免费的：平台要长期保存 artifact、harness、依赖、环境和原始 receipt，维护迁移路径，并为独立 rerun 支付算力与人工 adjudication。artifact 过期、依赖消失或 evaluator 无法重建时，结果必须标为 stale/unreproducible，不能继续充当 release gate。轻量的“模型名、日期、分数”记录在低风险趋势浏览或历史索引中仍然有价值，但只能描述当时观测，不得支持当前能力、安全或上线结论；关键条件无法公开时同样降级为受限 evidence。[受限证据：arXiv:2605.03596v1、2605.04135v1、2605.08192v1]

<!-- source-family:SF-2026-ARXIV-2605-08192 -->

### 从“可观测结果”到可发布结论，还需要识别与证明边界

生产日志天然带有历史策略、用户选择和环境变化造成的 confounding。把日志直接喂给 evaluator，只能得到相关性描述，不能自动回答“换一个策略会怎样”。evaluation run 必须先声明证据角色：`OBS` 负责描述，`EXP` 通过随机化或可辩护干预支持因果估计，`SIM` 只在 fidelity contract 内提供反事实。多轮 Agent 还要重建 mediator 与 state transition；缺失这些条件时，结论应降级为 observational signal，而不是 release-grade causal claim。

安全评估同样不能只靠固定采样。search-based route 可以冻结 deployment config，在 likelihood budget 内复用 prefix cache、做 chunked search，并报告找到的 failure mass 与尚未覆盖的 residual mass。它擅长发现低概率但结构化的失败，代价是搜索策略本身会改变被观察分布；因此必须与随机 sampling 并列，不能把“没有搜到”解释为“没有风险”。

当 Agent 生成 compiler、kernel 或其他可执行 artifact 时，信任路径需要分层。tests 暴露环境与实现 mismatch，translation certificate 由独立 checker 验证语义保持，machine proof 只覆盖被形式化的 theorem；parser、spec、toolchain 与硬件仍是未验证边界。任一层失败时回退为不发布或使用已知实现，而不是让上游模型的自信接管 release authority。

压缩模型的 release gate 也不能停留在平均 perplexity。必须比较 dense 与 pruned 模型的 item-level transition、fairness/calibration slices，并在真实 sparse kernel、存储格式和目标硬件上验证收益。结构稀疏只有在实现路径实际消费它时才是系统优化；否则只是参数模式变化。旧的平均指标仍可作早期 guardrail，但不能独自承担上线决定。

<!-- source-family:SF-CONFOUNDED-LOG-EVALUATION -->
<!-- source-family:SF-AGENT-SAFETY-SEARCH-MEASUREMENT -->
<!-- source-family:SF-AGENT-GENERATED-VERIFIED-COMPILER -->
<!-- source-family:SF-PRUNING-BEHAVIORAL-REGRESSION -->

### Evaluation 必须测量 Channel、Invariance、Drift 与 Access Boundary

Agent repair 的 execution trace 与 evaluator channel 可能对同一结果给出不同结论。评估对象必须同时冻结 artifact、执行环境、trace schema、judge input 与最终 outcome；channel disagreement 需要单独报告，而不能被一个总分吞掉。相似地，语义等价 prompt 若触发输出模式崩塌，说明系统缺少 invariance：release gate 应在 paraphrase family 上比较 mode transition，而非只测单一措辞。

IID benchmark 也不能直接外推到 deployment drift。Jacobian-sensitive 或局部敏感度 bound 可以把输入变化与风险增量关联，但只在邻域、光滑性和估计误差成立时有效；超出校准域就应触发 shadow/canary 或拒绝结论。任何 intervention 还要系统检查意外 side effect，通过受影响切片、对照 artifact 与回滚条件证明“修复没有搬走问题”，而不是只复测目标指标。

最后，真实 Agent 往往受授权限制，无法看到完整 ground truth。evaluation environment 必须显式建模 role、可见证据与合法 action；“未回答”可能是正确遵守权限，而不是能力失败。授权变化应进入 run identity，通用全访问 benchmark 只能作为上界，不能替代部署 contract。

<!-- source-family:SF-AUDITREPAIRBENCH-A-PAIRED-EXECUTION-TRACE-CORPUS-FOR-EVALUATOR-CHANNEL-R -->
<!-- source-family:SF-PARAPHRASE-INDUCED-OUTPUT-MODE-COLLAPSE-WHEN-LLMS-BREAK-CHARACTER-UNDER- -->
<!-- source-family:SF-JACOBIAN-VELOCITY-BOUNDS-FOR-DEPLOYMENT-RISK-UNDER-COVARIATE-DRIFT -->
<!-- source-family:SF-AUTOMATICALLY-FINDING-AND-VALIDATING-UNEXPECTED-SIDE-EFFECTS-OF-INTERVEN -->
<!-- source-family:SF-PARTIAL-EVIDENCE-BENCH-BENCHMARKING-AUTHORIZATION-LIMITED-EVIDENCE-IN-AG -->

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

### 先定位候选，再决定或拒答

当 evaluator 直接在所有标签或答案中选一个类别时，单一置信分数混合了两个错误：正确候选可能根本没有进入
可见集合，或候选已经正确但最终 selector 选错。更可审计的链路先构造带 coverage contract 的 shortlist，再
对 shortlist 做校准选择，并允许 abstain：

```text
raw candidates
→ conformal localization set
→ calibrated selector
→ decide | abstain | human escalation
```

Coverage 保证依赖 calibration/test exchangeability，只是有限样本下的 marginal guarantee；selector 的多次采样、
few-shot prompt 与 calibration revision 都必须进入 EvalSpec。分布漂移、高风险 slice 或 shortlist 为空时必须拒答，
不能把“集合很小”解释成事实真值。

视觉 rubric 的 criteria provenance、component weight、prefix localization 与 judge revision 也要独立记录。细粒度
credit 改善错误定位，却引入自动 rubric 偏差、模糊 prefix 对齐和同族 judge 偏置；最终 release gate 仍需独立
人工或可执行证据。多语言能力评估还必须把 interface language 与 reasoning language 拆成两个 factor，并用
role-swapped/self-play 或 matched task 控制 first-player 与规则差异；“英文推理改善”不是跨模型语言层级定律。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22474 -->
把 factual verification 从所有 claim 同成本复核改为 claim-risk/uncertainty 驱动的资源分配；阈值、coverage 与 verification latency 必须联合验收。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；March-2022 Wikipedia、FactScore 和 T4/256-token 生成条件限定结论；uncertainty score 未校准时不能拥有 release authority。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22633 -->
把 verbal confidence 与内部冲突分开：模型可高置信输出但隐藏 state 对相反命题均有支持，evaluation 需要独立测 conflict geometry 和 resolution behavior。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；representation probe 是诊断，不证明因果使用；不能直接成为 release gate。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22719 -->
forecast benchmark 必须按 decision-time 可获得输入冻结，并以 walk-forward 防止 later-data leakage；nowcast revision 也要成为 dataset version。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；样本小、统计功效不足且金融 domain 特定；结果不能证明生产 alpha，只证明 leakage-aware protocol。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22737 -->
stateful Agent evaluation 可由确定性 environment transition、predicate 与 event log 计算 GroundEval，而不是让 LLM judge 重新解释完整轨迹。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；context mode 可观测性更弱，确定性 evaluator 也只覆盖已编码 predicate；未编码目标不会自动出现。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

### Agent Kernel Evaluation 要把隐藏 Shape 与运行回执分开

固定公开 shape 容易复现 kernel correctness 和速度，却会诱导 Agent 针对已知 case 过拟合。更完整的 benchmark 冻结 task/harness revision，在隐藏 shape、dtype 与硬件目标上执行候选 kernel，同时保存 compile、correctness、runtime 和失败回执。Agent 只提出优化，harness 拥有 correctness 与测量边界。

隐藏任务提高 generalization 证据，却降低可调试性并增加硬件噪声；公开回归集仍用于开发，隐藏集只承担发布判断。作者 benchmark 不能证明未覆盖 operator、driver 或 GPU 上的泛化。

<!-- source-family:SF-2026-ARXIV-2605-16819 -->

### Counterfactual Localization 只能定位风险转折，不能读取真实意图

只标最终 deceptive outcome 无法知道轨迹何时越过可恢复边界。可固定每个 sentence prefix、重复采样 continuation，估计该前缀后进入危险结果的条件概率，再定位显著跃迁；这是一种因果干预式诊断，而不是从单条 CoT 读取内在意图。

重采样增加成本且受 generator、环境和 judge 影响；语言 cue 跨环境漂移时，内部 transition feature 也只能作为受限 sensor。高风险系统仍需外部行为、authorization 和 stop policy，不能由定位器单独授权或定罪。

<!-- source-family:SF-2026-ARXIV-2605-17113 -->

### Training 与 Inference Simulator 需要共享配置身份

分离的训练/推理 simulator 适合局部容量规划，但会让 model graph、parallelism、hardware、network 和 runtime assumptions 漂移。统一 simulator 应以同一版本化配置生成两类事件，并分别对真实 trace 校准，才能让 what-if 结果可比较。

统一模型提高复用，却扩大误差传播和校准负担；作者平均预测误差只属于其配置空间，不覆盖 data-dependent kernel、故障恢复或生产 tail。早期规划可用 simulator，发布仍需真实 hardware replay/canary。

<!-- source-family:SF-2026-ARXIV-2605-17164 -->

### 多语言 Safety 需要分解 Aggregate Failure

总体 jailbreak rate 会混合模型安全韧性、prompt 难度、语言处理难度和 concept-language 特异差距。分层 latent-variable/IRT 分析可把这些因素作为不同参数估计，使数据补强和 guardrail 修复指向具体 failure slice。

分解依赖题目可比性、标注和模型假设；参数可辨识不等于真实因果，低资源语言的小样本还会放大不确定性。原始逐语言 outcome、攻击类型和置信区间必须保留，聚合指标继续承担趋势监控，但不能独自证明公平或安全。

<!-- source-family:SF-2026-ARXIV-2605-17173 -->

### Duplex Agent Evaluation 要联合测 Timing 与 Content

离线评估完整回答适合单轮文本；双向实时 Agent 的价值还取决于何时打断、等待、追问和响应。Evaluation 应重放或运行 versioned event stream，同时对响应内容、turn alignment、interrupt handling 与 latency window 评分。

联合合同更接近交互体验，却引入时钟同步、网络抖动和环境不可重复；content 正确不能覆盖错过行动窗口，低延迟也不能覆盖错误结论。开发期仍可分开测 ASR/LLM/TTS，发布时再用端到端 duplex trajectory 收束。

现有 exact-v1 只在其 §3 定义的 duplex tasks、turn/interrupt protocol 与 §4 披露的模型端点上验证这套联合评分；它不证明未披露硬件、网络、并发或开放对话中的 latency/content 分布。因而基准结果只能校准 evaluation contract，不能直接成为生产 SLO。

<!-- source-family:SF-2026-ARXIV-2605-17360 -->

## 从“有结果”到可追责、可干预的 Evidence

### 表征审计必须先消除模板混淆，再谈因果

把不同提示的 activation 直接拼成矩阵，容易把 template、长度和 mean-direction shift 当成目标概念。可信的 activation audit 应先固定 prompt contract、中心化或显式建模均值方向，再报告 effective rank 等描述量，最后用 intervention 或 causal ablation 检查该方向是否真正控制输出。收益是把“可分”与“可干预”分开，代价是实验矩阵扩大且结论更局部；只做线性 probe 可作为发现工具，不能成为 release claim。

<!-- source-family:SF-2026-ARXIV-2605-24583 -->

### Explainability 的 Release Claim 存在不可兼得边界

复杂环境、高任务性能、面向人的简洁解释与完全忠实的内部描述通常不能同时保证。平台因此不应把一个 explanation score 当成统一证明，而应声明它优化了 fidelity、completeness、comprehensibility 或 coverage 中的哪些维度，以及牺牲了什么。收益是避免把可读叙述冒充因果证据，代价是需要多种解释 artifact 和不同消费者 gate；低风险、简单模型中，局部可读解释仍可能充分。理论边界不意味着所有解释都无用，只限制可作出的联合保证。

<!-- source-family:SF-2026-ARXIV-2605-24727 -->

### 长轨迹评分必须处理提前终止与删失

把任务成功率直接平均，默认每条轨迹都观察到同一终点；超时、预算耗尽或安全中止会把未知未来混成失败。trajectory evaluator 应把终止原因、观察 horizon 与 censoring policy 写入 evaluation object，并采用满足 properness 的评分规则，使模型不能通过提前退出操纵分数。收益是跨策略比较更可信，代价是需要生存/删失假设和更复杂的不确定性报告；在固定短 horizon 且无中止时，普通成功率仍足够。现有理论与实验不证明任何单一 proper score 能覆盖所有任务价值。

<!-- source-family:SF-2026-ARXIV-2605-24756 -->

### 污染校正需要主动干预，而不是事后猜测

看到异常高分后再估计 benchmark contamination，无法区分记忆、能力和数据生态。更强的协议在可控训练副本中按已知比例注入样本，拟合 contamination–response curve，再把目标 run 映射到带不确定性的校正区间。它把污染从传闻变成可复现实验，但需要训练数据写权限与未污染 counterfactual，闭源模型通常不具备这些条件；此时只能报告疑似污染而不能伪造校正分。现有证据仅覆盖披露模型与五类 benchmark。

<!-- source-family:SF-2026-ARXIV-2605-24818 -->

### Safety Policy 可以编译成可追踪测试，但不能自动获得完备性

人工逐条写 jailbreak 测试在 policy 较小时合理，policy 演进后容易留下未覆盖路径。将自然语言规则编译为形式化 predicate 与 semantic graph，可以从未覆盖边生成带 policy revision、path identity 和 expected outcome 的测试候选；evaluator 仍负责验证翻译和执行结果。收益是覆盖可追踪，代价是 policy-to-logic 错译和图爆炸；多轮状态或规则歧义较高时仍需人工设计。当前证据只覆盖静态单轮场景，不能证明测试生成完备。

<!-- source-family:SF-2026-ARXIV-2605-24883 -->

### Rubric 与 Pairwise Preference 是不同测量算子

绝对 rubric score 给出可解释维度，却要求评分者稳定使用刻度；pairwise preference 降低尺度负担，却只提供相对次序并受候选集合影响。评估系统应在同一受控质量阶梯上比较两者的一致性、区分力和成本，而不是把它们当成可互换标签。低样本或需要具体缺陷说明时 rubric 仍有价值，大规模排序可优先 pairwise；混合 trade-off 必须保留原始判断。现有实验主要来自法律文本，不能规定所有领域的 evaluator 形式。

<!-- source-family:SF-2026-ARXIV-2605-25240 -->

### Benchmark 相关性应分解共同构念与生态噪声

多个 leaderboard 同涨不等于它们测量同一能力：模型家族、训练数据、提交策略和 task-specific variance 都会制造相关。latent measurement model 可把共同因子、任务特异方差与元数据效应分开，帮助 release owner 判断“能力变化”还是“评测生态变化”；代价是模型可辨识、样本代表性和时间稳定性假设。原始逐 benchmark 结果必须保留，latent factor 只能作为解释层。现有证据是一轮六 benchmark 的观察性快照，不构成因果能力本体。

<!-- source-family:SF-2026-ARXIV-2605-25272 -->

## 从机制演进到系统设计

Evaluation 从单一 benchmark 分数演进为版本化的决策证据系统。首先冻结 subject、dataset/environment、metric/judge 和 run identity；随后对 calibration、slice、uncertainty 与复现参数建模；当评估成本或开放任务使完整真值不可得时，再引入顺序检验、受控子集、可执行 predicate、typed reasoning trace 或 abstention。

更自动的 evaluator 能扩大覆盖，却会引入 judge bias、leakage、aggregation degrees of freedom、相关样本和未编码目标。任何分数只有在其 EvalSpec 和适用分布内成立，release authority 必须独立于产生分数的模型；低功效、漂移或 oracle 不完整时结论应为 inconclusive，而不是强行排序。人工评审、完整 benchmark 和真实 environment outcome始终作为高风险 fallback。

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
19. Factual precision、all-claims-correct 与 conclusion-correct 为什么不能共用一个分数？
20. 为什么只有在 claims 独立且全部必要时才能机械相乘置信度？
21. Source Family、dependency edge 与 inference-edge confidence 怎样改变结论的联合概率？
22. 为什么 calibration 最终必须与 risk–coverage 和 abstention policy 一起验收？
23. 为什么低 semantic entropy、高 self-consistency 在 adversarially correlated distribution 中仍不能成为 truth evidence？
24. 为什么低 HTTP error rate 不能证明模型输出质量满足 intended use？

## Evaluation Contract 还必须管理配置、样本身份与工作负载状态

### Pairwise Verdict 需要 Configuration Envelope

“A 比 B 安全”只有在 harness configuration 被固定时才是可复算声明。Evaluation owner 应保存模型端点、prompt/template、sampling、package、judge 与 metric 配置，并报告配置网格内的排序一致性和方差，而不是只给一个 pairwise number。收益是区分模型差异与 harness-induced reversal，代价是组合爆炸；覆盖不足时应把结论降为 configuration-conditional，而不是平均掩盖反转。exact-v1 只在论文的模型、benchmark、package envelope 与 SDI/CFR 等指标中观察到该现象，不能估计所有评测配置。<!-- source-family:SF-2026-ARXIV-2605-25492 -->

### Membership Audit 要绑定 Sample Identity 与低 FPR 决策

把单样本攻击分数直接平均，在总体巨大、目标 FPR 很低时会被有限 shadow model 与抽样偏差支配。Measurement owner 应保存 sample identity、per-sample vulnerability、aggregation threshold 与 finite-population correction，并在同一 false-positive contract 下报告不确定性。收益是使 membership 声明可解释，代价是更多 shadow computation 和更宽置信区间；Gaussian post-processing 或总体假设失效时应退回 per-sample 结果或标记不可判定。exact-v1 只支持论文的数据、攻击与 analytical simulation，不证明生产模型隐私状态。<!-- source-family:SF-2026-ARXIV-2605-25819 -->

### Benchmark Completion 必须覆盖证据与 Action Space

只测静态输入输出，在 response space 小且动作固定时合理；部署 benchmark 若未覆盖可取得证据和允许 action，就可能把“未搜索到”误判为能力不足。Eval owner 应版本化 evidence fibers、action completeness 与 acquisition curve，先证明可完成性，再比较 agent。收益是区分 benchmark 缺口与系统缺口，代价是维护 action model 和数据覆盖；空间开放或 completeness 无法证明时，应明确只报告 sampled coverage。exact-v1 仅支持论文的 controlled channels 与 Tox21/Matbench/JARVIS audits，不证明开放世界完备性。<!-- source-family:SF-2026-ARXIV-2605-25997 -->

### Activation Oracle 的 Confidence 也要校准

内部 activation score 适合排序，却不能直接当 correctness probability。Evaluation owner 应为具体 operator、layer、label availability 与 calibration split 建立 confidence contract，并比较多种 operator 的 reliability，而非只看平均分。收益是让 interpretability probe 可进入 selective decision，代价是样本与重新校准成本；secret-word 可枚举性、层漂移或 label shift 会使置信度失真，应退回无置信度的诊断用途。exact-v1 只支持四个 Qwen/Gemma oracle、每 operator 约六千样本及所测任务，不提供通用内部真值保证。<!-- source-family:SF-2026-ARXIV-2605-26045 -->

### Agent Workload 不是普通 Long-prompt Workload

把输入 token 总量当作主要成本，在 cache 不可复用时成立；多轮 Agent 大量复用 prefix 后，execution 会转为 decode-dominated，并依赖长生命周期 KV state。Workload contract 应记录 turn graph、cache-hit identity、KV lifetime、tool pauses 和 decode distribution，capacity owner 才能重放。收益是避免用静态长提示压测误配硬件，代价是 trace 基础设施与隐私处理；prefix identity 失效或 cache eviction 改变时必须重新测量。exact-v1 只支持五个 agent benchmark、披露的 Gemma/Qwen 配置和 serving stack，不证明所有生产 agent 都呈同一比例。<!-- source-family:SF-2026-ARXIV-2605-26297 -->

### Domain Workflow 可以编译为 Deterministic Verifier

人工编写少量 ERP 题目容易审计，却难覆盖约束组合；纯自然语言生成又会引入不可判定答案。Benchmark owner 可以把领域专家 specification 编译为 constraint optimization program，由同一版本的 generator 与 executable verifier 产生任务和判定。收益是扩大覆盖并保留可复算性，代价是 specification bug 会系统性污染数据；必须以人工 anchor、独立 solver 和版本化约束做交叉检查。exact-v1 只支持单一 ERP domain 与生成任务，不证明真实业务流程或跨域泛化。<!-- source-family:SF-2026-ARXIV-2605-26321 -->

### Miscoverage 要拆成 Sampling Failure 与 Selection Failure

只给最终 coverage 数字，会把候选集中没有正确项和 selector 选错混成同一故障。Evaluation owner 应分别估计有限采样失败，并在 calibration/exchangeability 条件下对 conditional selection 使用 conformal gate，再组合总体 bound。收益是为增加采样或改进 selector 指明责任，代价是校准集、额外样本与假设检查；分布漂移或相关自适应采样会破坏保证，应退回经验 risk-coverage 曲线或 abstain。exact-v1 仅支持论文的有限采样实验、conditional exchangeability 与 population-bound 假设，不是开放世界 truth guarantee。<!-- source-family:SF-2026-ARXIV-2605-27091 -->

## Adaptive Evaluation 也必须被当作实验过程

<!-- semantic-body-binding:SF-TOWARDS-RELIABLE-LLM-EVALUATION-CORRECTING-THE-WINNER-S-CURSE-IN-ADAPTIV:start -->
在同一 benchmark 上反复调 prompt、policy 或超参数并只报告最佳配置，会产生 procedure-level winner's curse：即使每次单独评测都正确，选择过程也会系统性高估最终 winner。EvalRun 因而要保存尝试序列、selection rule、holdout reuse 与 stopping condition，并用独立 holdout、sequential correction 或重新运行校正选择偏差。它降低虚假改进，却需要更多样本和计算；一次性、预注册比较仍可沿用普通置信区间。[受限证据：arXiv:2605.05973v1]
<!-- semantic-body-binding:SF-TOWARDS-RELIABLE-LLM-EVALUATION-CORRECTING-THE-WINNER-S-CURSE-IN-ADAPTIV:end -->

<!-- semantic-body-binding:SF-BEYOND-ACCURACY-POLICY-INVARIANCE-AS-A-RELIABILITY-TEST-FOR-LLM-SAFETY-J:start -->
Judge 可靠性还应接受 policy-preserving rewrite test：若语义与安全政策保持不变，只改变表述、顺序或无关上下文，verdict 应在声明容差内保持不变。该 invariance 是 evaluator release evidence，而不是另一个总分；失败时应回退冻结人工 anchor、确定性 outcome 或更窄适用域。稳定性通过也不证明 judge 正确，只说明它没有被这类等价变换轻易翻转。[受限证据：arXiv:2605.06161v1]
<!-- semantic-body-binding:SF-BEYOND-ACCURACY-POLICY-INVARIANCE-AS-A-RELIABILITY-TEST-FOR-LLM-SAFETY-J:end -->

## Evidence Chain 与在线干预

普通复现实验保存代码、配置和分数，在协作规模较小时已经有价值；当论文数字、执行环境与发布 artifact 由不同主体持有，仅保存最终表格无法证明某次计算确实发生，也无法阻止事后替换。更强的 evidence chain 把代码身份、输入与配置、实际执行、输出摘要和签名收据绑定到同一 run identity，使结果具备 nonrepudiation。它增加密钥、attestation 与长期验证成本，也不能证明实验设计本身正确；低风险探索仍可使用普通 provenance，高影响结论才需要签名链。[受限证据：arXiv:2605.08586v1]

<!-- source-family:SF-2026-ARXIV-2605-08586 -->

评测“AI 是否发现了新方法”还必须限制系统可编辑的范围，冻结 evaluator、training knobs 与强基线，并检查收益能否跨 scale 保持。否则 Agent 可能只是在调参、修改 harness 或利用 evaluator 缺口。这个 contract 降低虚假 discovery，却提高复现成本并可能压制合理搜索空间；开放探索可以保留宽 scope，但不能直接获得“新机制已成立”的发布权威。[受限证据：arXiv:2605.08678v1]

<!-- source-family:SF-2026-ARXIV-2605-08678 -->

长轨迹的 post-hoc attribution 能解释失败，却无法在错误传播前阻断它。进入在线运行后，auditor 只能读取当前 prefix，并在 earliest decisive error 出现时选择继续或告警；alarm time、false-positive cost、可观察 prefix 和 downstream propagation 因而成为 EvalSpec。在线审计获得干预机会，代价是未来信息不可见、误报会中断正确轨迹；低风险离线分析仍适合 post-hoc 路径。[受限证据：arXiv:2605.08715v1]

<!-- source-family:SF-2026-ARXIV-2605-08715 -->

Embodied evaluation 也不能把“环境任务已经完成”和“Agent 正确地结束并承诺完成”压成一个分数。world completion、stop decision、terminal statement 与证据充分性应分别记录；这能暴露执行成功但停止失败、或无证据承诺成功的系统错误，却增加 terminal-state annotation 与 judge 依赖。确定性 simulator 可直接检查时仍优先使用环境谓词，开放世界则保留人工 adjudication。[受限证据：arXiv:2605.08747v1]

<!-- source-family:SF-2026-ARXIV-2605-08747 -->

在 edge federated fine-tuning 中，final accuracy 或 simulation 只能证明算法在给定抽象下有效，不能证明真实设备可部署。evaluation contract 至少联合 quality-under-budget、cost-to-target、真实设备 resource/energy 与 perturbation robustness；它把“达到精度”提升为“在约束内稳定达到精度”，但扩大测试矩阵并降低跨设备可比性。早期算法筛选仍可用 simulation，只能标记为 feasibility evidence。[受限证据：arXiv:2605.08636v1]

<!-- source-family:SF-2026-ARXIV-2605-08636 -->

多轮 jailbreak 比较若各自拥有不同 turn、retry、interaction、strategy-generation 和 judge budget，最终 ASR 不具可比性。可复现 harness 应把 strategy、prompt generation、refinement 与 flow control 拆成可组合模块，并冻结每层 budget 与 revision。模块化提高归因与公平性，却可能限制真实攻击的自适应空间；开放红队仍可采用更宽预算，但不得与固定合同的 benchmark 排名混算。[受限证据：arXiv:2605.11002v1]

<!-- source-family:SF-2026-ARXIV-2605-11002 -->

## Action Control 需要 Sensitivity 与 Invariance 双臂证据

只看 action accuracy，无法区分 Agent 是否真正消费了当前状态，还是依赖与训练集相关的表面 cue。因果评估应构造两个相互约束的干预臂：改变决定正确 action 的 decisive state 时，行为必须相应改变；保持 decisive state 不变、只替换无关 cue 时，行为应保持在声明容差内。前者测 target-changing sensitivity，后者测 target-preserving invariance；任一单臂通过都不足以证明 action control。

<!-- source-family:SF-CAUSAL-STATE-BINDING-PREDICTS-ACTION-CONTROL-IN-LANGUAGE-AGENTS -->
EvalSpec 需要冻结 event/state schema、可控干预、matched interface、action scorer 与 tolerance，并保存每对干预样本的 trajectory。它能把相关性成功分解为更强的 behavioral evidence，却增加构造 matched interventions 的成本，也可能因遗漏真正 mediator 而误判。无法构造可信干预时，应把结论降级为 observational association，继续使用真实 outcome、人工 adjudication 与 production incident evidence。即使双臂通过，也只证明披露任务上的结构耦合，不证明模型具有内在 agency 或能迁移到开放环境。[受限证据：arXiv:2605.09692v1]

## 小结

Evaluation System 不是 benchmark 集合，也不是某个产品的 metrics 页面。它把 intended use 转化为 EvalSpec，把有限数据和环境转化为带不确定性的 evidence，再把 evidence 放入受风险政策约束的发布与反馈决策。对 MoE 等条件计算系统，负载统计只是运行证据，功能 specialization 仍需独立指标与干预验证。release-grade 结论还必须能重建其 artifact、harness 与环境；无法重建的历史分数只能作为描述性记录。

它的长期不变量是：完整 subject identity、明确分布、可审计 scorer、per-example evidence、切片与不确定性、分离的 decision policy，以及从生产反馈回到新版本的受控闭环。下一章进入 Monitoring，讨论平台怎样以受控成本持续获得 observed state，而不把“发生了什么”误当成“是否足够好”。

## Review notes

- Online Agent-as-a-Judge（arXiv:2606.08200v1；Status: Experimental）：用于区分 passive scoring 与 in-world coverage-seeking intervention；evaluator action 改变 trajectory，不能当作自然发生率或生产 repair authority。https://arxiv.org/html/2606.08200v1

- `SF-2026-ARXIV-2606-22474` — primary `arXiv:2606.22474v1`；Method=`arXiv:2606.22474v1 §3 FACTOR Method`；Evaluation=`arXiv:2606.22474v1 §4 Experiments`；Non-proof=`arXiv:2606.22474v1 §5 Limitations and Conclusion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-22633` — primary `arXiv:2606.22633v1`；Method=`arXiv:2606.22633v1 §2 Method`；Evaluation=`arXiv:2606.22633v1 §3 Experiments and Results`；Non-proof=`arXiv:2606.22633v1 §Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-22719` — primary `arXiv:2606.22719v1`；Method=`arXiv:2606.22719v1 §3 Method`；Evaluation=`arXiv:2606.22719v1 §4 Results`；Non-proof=`arXiv:2606.22719v1 §5 Discussion — Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-22737` — primary `arXiv:2606.22737v1`；Method=`arXiv:2606.22737v1 §3 GroundEval Framework`；Evaluation=`arXiv:2606.22737v1 §5 Evaluation`；Non-proof=`arXiv:2606.22737v1 §10 Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Prediction-Powered Evaluation and Meta-Evaluation（automatic metric as variance-reduction signal；Status: Experimental）：
  https://arxiv.org/abs/2608.26638v1
  - 证据边界：论文在六个 WMT 数据集上支持有限人工标签与大量自动分数的 bias-corrected system comparison；
    结论依赖抽样、配对、metric residual 与分布假设，不提供单样本 correctness probability，也不证明跨任务通用节省率。

- Localize-Then-Decide Guarantees for LLM Judgments（conformal shortlist + calibrated abstention；
  Status: Experimental）：https://arxiv.org/abs/2608.25824v1
- V-Rubrics（atomic visual criteria + component/prefix-localized reward；Status: Experimental）：
  https://arxiv.org/abs/2608.25580v1
- Skill Issue（interface language × reasoning language evaluation；Status: Experimental）：
  https://arxiv.org/abs/2608.25832v1
  - 证据边界：三项研究分别绑定 preference judging、Qwen3-VL 与 3–4B 多语言 self-play；exchangeability、
    judge bias、tokenization、重复采样成本和 domain shift 均需在 deployment slice 重新校准。

- LayerRAG-Bench（evidence/tool/authorization/session-state 分层故障注入与 repair-scope attribution；Status: Experimental）:
  https://arxiv.org/abs/2607.27353v1

- Ground Truth First（arXiv:2607.21962v1；Status: Experimental）：https://arxiv.org/html/2607.21962v1
  - 证据边界：支持 synthetic longitudinal corpus 中的 fact-validity-first contract、write/read 分离审计与 tenure crossover；不证明任一 memory architecture 在真实用户、任意 backbone 或无限历史上普遍最优。

- ICAE-Bench（arXiv:2607.21217v1；Status: Experimental；artifact commit `cda0ad681e484c69a7f437f991d2ee81c313020a`）：https://arxiv.org/html/2607.21217v1
  - 证据边界：支持 GroundPRD→hidden constraints→bounded clarification→black-box repository verification；不支持把 Lite 或特定 framework 结果外推为通用 coding-agent 排名。

- DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations（arXiv:2607.19865v1；Status: Experimental）：https://arxiv.org/html/2607.19865v1
  - 证据边界：支持已发布任务与 mutation 上的 artifact-state evaluation 和 verifier fidelity；不证明 predicate 完整、与专家审查语义等价，或更高 pass rate 能跨 harness 迁移。
- KernelGenBench: A Multi-Source and Multi-Chip Benchmark for LLM-based Kernel Generation（arXiv:2607.27231v1；Status: Experimental）：https://arxiv.org/html/2607.27231v1
  - 证据边界：支持已发布 benchmark contract 及其披露的模型与硬件运行；不证明生产 kernel correctness、通用 tolerance、anti-hack coverage 不等时的公平比较，或模型排名可跨 operator、chip 与 harness 迁移。
- LLMs Get Lost in Evolving User Intent（arXiv:2607.20734v1；Status: Experimental）：https://arxiv.org/html/2607.20734v1
  - 证据边界：支持 synthetic final-anchor 合同中的性能退化和 transition diagnosis；不证明真实用户中的发生率、memory 单独即可修复 intent tracking，或初步 RL 结果可泛化。

- AgentCompass: A Unified Evaluation Infrastructure for Agent Capabilities（harness/environment/scorer identity；Status: Experimental）:
  https://arxiv.org/abs/2607.13705v1

- Logic graph uncertainty（reasoning-graph agreement sensor；Status: Experimental）:
  https://arxiv.org/abs/2607.08017v1

- SpanUQ（typed semantic spans 与 model-specific uncertainty probe；Status: Experimental）:
  https://arxiv.org/abs/2607.05721v1
- Estimating Uncertainty from Reasoning Across Languages and Model Scales（multilingual calibration slices；Status: Experimental）:
  https://arxiv.org/abs/2607.06327v1

- Think Before You Grid-Search（floor-first serving diagnosis；Status: Experimental）:
  https://arxiv.org/abs/2607.05876v1

- AgentSysBench（model/tool/state/orchestration workload characterization；Status: Experimental）: https://arxiv.org/abs/2608.15127
- ClawProBench（runtime-aware typed traces and frozen holdouts；Status: Experimental）: https://arxiv.org/abs/2608.22510

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

- Evidence boundary：MLflow 只作为 metadata/evidence implementation；公开 benchmark 与论文结果只用于说明
  measurement problems，不外推为当前模型或生产系统的通用结论。正文已经拥有从 runtime success 到 outcome
  success 的证据阶梯及其 canonical owner。

Primary research：

- Percy Liang et al., "Holistic Evaluation of Language Models", 2022: https://arxiv.org/abs/2211.09110
- Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", 2023: https://arxiv.org/abs/2306.05685
- Sewon Min et al., "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation", 2023:
  https://arxiv.org/abs/2305.14251
- Luyu Gao et al., "RARR: Researching and Revising What Language Models Say", 2022:
  https://arxiv.org/abs/2210.08726
- Saurav Kadavath et al., "Language Models (Mostly) Know What They Know", 2022:
  https://arxiv.org/abs/2207.05221
- Lorenz Kuhn, Yarin Gal, Sebastian Farquhar, "Semantic Uncertainty", 2023:
  https://arxiv.org/abs/2302.09664
- Chuan Guo et al., "On Calibration of Modern Neural Networks", 2017:
  https://arxiv.org/abs/1706.04599
- Victor Quach et al., "Conformal Language Modeling", 2023:
  https://arxiv.org/abs/2306.10193
- Mark Russinovich, "Fool's Gold: Defensive Deception Against Safety-Removal Attacks on Open-Weight Models", 2026
  （Status: Experimental / Security-sensitive evidence boundary）: https://arxiv.org/abs/2608.17202
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
- RSIBench-Data（冻结 substrate、隔离 data-strategy decision、保留 checkpoint trajectory；Status: Experimental）:
  https://arxiv.org/abs/2607.25886v1

- Business Arena（stateful counterfactual evaluation；Status: Experimental）:
  https://arxiv.org/abs/2608.08621
- How Query Visibility Changes KV-Cache Compression Rankings（matched-budget audit；Status: Experimental）：
  https://arxiv.org/abs/2607.11942v1
- SpectraReward（frozen multimodal read-back reward sensor；Status: Experimental）:
  https://arxiv.org/abs/2607.11886v1
- Vero（repository-level implementation + proof artifact evaluation；No Change / Experimental evidence）:
  https://arxiv.org/abs/2608.13522
- Phantom Gains（transition ledger 的 measured-null audit；Status: Experimental）:
  https://arxiv.org/abs/2608.20290
- Beyond Success Rate（cost-aware offensive/defensive security-agent evaluation）:
  https://arxiv.org/abs/2607.15263
- Beyond Semantic Equivalence（implication/incompatibility graph uncertainty sensor；Status: Experimental；受限问答校准，不证明 truth）:
  https://arxiv.org/abs/2607.16868v1

### Daily integration evidence trace

- `2026-05-04 / SF-2026-ARXIV-2605-01771` — exact-v1 `arXiv:2605.01771v1`；正文区分 textual agreement、typed process trace 与 environment outcome，不外推所测任务的遵从率。
- `2026-05-04 / SF-2026-ARXIV-2605-02038` — exact-v1 `arXiv:2605.02038v1`；正文吸收 prompt-variant spread、raw generation/parser identity 与等价性审计，未保留受限模型排名。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28013 — primary arXiv:2606.28013v1; exact-v1 URL=https://arxiv.org/html/2606.28013v1; Method=https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant; Evaluation=https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis; Non-proof=https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion。
- SF-2026-ARXIV-2606-28661 — primary arXiv:2606.28661v1; exact-v1 URL=https://arxiv.org/html/2606.28661v1; Method=https://arxiv.org/html/2606.28661v1 — §Proposition 1 (Design effect of test-time sampling) .; Two-stage design effect.; Evaluation=https://arxiv.org/html/2606.28661v1 — §1 Introduction and roadmap; 2 Test-time sampling is cluster sampling; Non-proof=https://arxiv.org/html/2606.28661v1 — §6 Conclusion。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-29038 — primary arXiv:2606.29038v1; exact-v1 URL=https://arxiv.org/html/2606.29038v1; Method=https://arxiv.org/html/2606.29038v1 — §2 Pipeline Architecture and Metric Aggregation Divergence; 2.4 Positioning: Pipeline Architecture as Unregistered Degrees of Freedom; Evaluation=https://arxiv.org/html/2606.29038v1 — §3.2 Controlled Aggregation Experiment (EA-2); Appendix A Experiment Parameters; Non-proof=https://arxiv.org/html/2606.29038v1 — §Metric Aggregation Divergence: A Hidden Validity Threat in Agent-Based Policy Optimization and a Contractual Remedy; 6 Discussion; 7 Limitations and Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22783` — primary `arXiv:2606.22783v1`; Method=`arXiv:2606.22783v1 — §3 Method; §A.4 The Dilemma of Construction and Verification; §A.4.1 Construction Difficulty`; Evaluation=`arXiv:2606.22783v1 — §Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints; §3.1 Evaluation Paradox; §3.3 Asymptotic Analysis`; non-proof=`arXiv:2606.22783v1 — §5 Conclusion; §A.6 Conclusion: Returning to the Origin of Difficulty; §C.8 Conclusion: Validating Computational Irreducibility`; fallback=该 family 的 failure pressure 是：We break this paradox by shifting the evaluation paradigm from simulating a messy reality to constructing computationally pure challenges. 披露的 evaluation signal 是：Evaluating the exhaustive search capabilities of large language models (LLMs) is plagued by a fundamental paradox: verifying completeness requires complete ground truth, yet high-entropy enumeration tasks make such ground truth impossible for humans to create. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22826` — primary `arXiv:2606.22826v1`; Method=`arXiv:2606.22826v1 — §3 Method; §3.3 Subset Construction`; Evaluation=`arXiv:2606.22826v1 — §MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration; §Appendix D Threshold Sensitivity Analysis; §Appendix E GPU Evaluation Speedup Breakdown`; non-proof=`arXiv:2606.22826v1 — §6 Conclusion`; fallback=该 family 的 failure pressure 是：Existing subset selection methods reduce this cost but depend on large calibration pools or learned prediction layers. 披露的 evaluation signal 是：Evaluating LLMs across many model variants -- quantized, fine-tuned, or deployment-specific -- requires running large benchmarks repeatedly, a process that can take tens of hours per model on edge hardware such as NPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24074: `arXiv:2606.24074v1`; exact-v1 URL=`https://arxiv.org/html/2606.24074v1`; Method=`https://arxiv.org/html/2606.24074v1 — §3 Reliability Certification Setup; 4 Constructing a Certification SOTM`; Evaluation=`https://arxiv.org/html/2606.24074v1 — §5 A Matching Reliability Certification Lower Bound`; Non-proof=`只证明给定 reliability gap、binary correctness oracle 与 small-error leading order；不证明开放式 judge 标签、分布漂移或任意非独立 query 下仍满足同一界。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24081: `arXiv:2606.24081v1`; exact-v1 URL=`https://arxiv.org/html/2606.24081v1`; Method=`https://arxiv.org/html/2606.24081v1 — §3 PixJail Framework; 3.2 Attack Module; 3.3 Evaluation Pipeline; 3.4 Memory Updates`; Evaluation=`https://arxiv.org/html/2606.24081v1 — §4 Experiments; 4.1 Data, Models and Metrics; 4.3 Main Results`; Non-proof=`11 种 attack、4 个 victim 与论文匹配配置不证明未知 attack 自动复现；prompt/heuristic memory update 及 closed-source safety filter 仍是黑盒边界。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24124: `arXiv:2606.24124v1`; exact-v1 URL=`https://arxiv.org/html/2606.24124v1`; Method=`https://arxiv.org/html/2606.24124v1 — §3 DSL for Reasoning Trace Formalization; 4 Structured Verification`; Evaluation=`https://arxiv.org/html/2606.24124v1 — §5 Evaluation; E Standalone Verification on ProcessBench`; Non-proof=`逐步验证成本随 trace 线性增长，semantic deduction 仍依赖 LLM audit，inference schema library 有限；三类 benchmark 不证明任意开放域推理。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24996: `arXiv:2606.24996v1`; exact-v1 URL=`https://arxiv.org/html/2606.24996v1`; Method=`https://arxiv.org/html/2606.24996v1 — §2 Results: Two Roles for the Certification Protocol`; Evaluation=`https://arxiv.org/html/2606.24996v1 — §A Report-Card and Gate Procedure; C/D Robustness Controls`; Non-proof=`证据来自 forecasting candidate families 与两个 locked interface；不证明所有 task metric 或业务成本可被同一 gate 捕获，underpowered audit 只能给 inconclusive。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25487**：Primary `arXiv:2606.25487v1`；Method `https://arxiv.org/html/2606.25487v1 — §3 Setup; Appendix A Prompts, wrappers, and attack configuration`；Evaluation `https://arxiv.org/html/2606.25487v1 — §4 Results; 4.1 Calibration against human labels; 4.3 white-box attack`；未证明边界 `https://arxiv.org/html/2606.25487v1 — §6 Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25622**：Primary `arXiv:2606.25622v1`；Method `https://arxiv.org/html/2606.25622v1 — §IV Theoretical Framework: MAS Architecture and Experimental Setup`；Evaluation `https://arxiv.org/html/2606.25622v1 — §V Results & Discussion`；未证明边界 `https://arxiv.org/html/2606.25622v1 — §VI Limitations & Future Work`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25760**：Primary `arXiv:2606.25760v1`；Method `https://arxiv.org/html/2606.25760v1 — §3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks`；Evaluation `https://arxiv.org/html/2606.25760v1 — §4 UQ Generalizes Selectively; 5 Graded Error and Calibration`；未证明边界 `https://arxiv.org/html/2606.25760v1 — §A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25782**：Primary `arXiv:2606.25782v1`；Method `https://arxiv.org/html/2606.25782v1 — §2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel`；Evaluation `https://arxiv.org/html/2606.25782v1 — §5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs`；未证明边界 `https://arxiv.org/html/2606.25782v1 — §OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26071**：Primary `arXiv:2606.26071v1`；Method `https://arxiv.org/html/2606.26071v1 — §4 Protocol and Methods; 5 Environments; 7 Methodological Insights`；Evaluation `https://arxiv.org/html/2606.26071v1 — §6 Case Studies; 8 Recommendations`；未证明边界 `https://arxiv.org/html/2606.26071v1 — §10 Limitations and Future Work; negative-results and confounding boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26185**：Primary `arXiv:2606.26185v1`；Method `https://arxiv.org/html/2606.26185v1 — §Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation`；Evaluation `https://arxiv.org/html/2606.26185v1 — §Cross-temperature, repeat-run and judge-agreement evaluation`；未证明边界 `https://arxiv.org/html/2606.26185v1 — §Temperature control is necessary but not sufficient; prompt/model/vendor drift remains`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26300**：Primary `arXiv:2606.26300v1`；Method `https://arxiv.org/html/2606.26300v1 — §Verification Horizon formulation for coding-agent rewards`；Evaluation `https://arxiv.org/html/2606.26300v1 — §Reward-verification experiments across coding horizons`；未证明边界 `https://arxiv.org/html/2606.26300v1 — §No universal reward verifier; longer horizons and hidden environment state remain`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26429**：Primary `arXiv:2606.26429v1`；Method `https://arxiv.org/html/2606.26429v1 — §DualEval joint model-item calibration`；Evaluation `https://arxiv.org/html/2606.26429v1 — §Unified LLM evaluation experiments and calibration analysis`；未证明边界 `https://arxiv.org/html/2606.26429v1 — §Joint calibration assumes the evaluated item/model pool; new distributions require refitting`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26456**：Primary `arXiv:2606.26456v1`；Method `https://arxiv.org/html/2606.26456v1 — §Safety-Aware Mutation Testing proposal and interaction-aware mutant model`；Evaluation `https://arxiv.org/html/2606.26456v1 — §Simulation-based ADS testing protocol and proposed adequacy criterion`；未证明边界 `https://arxiv.org/html/2606.26456v1 — §Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26492**：Primary `arXiv:2606.26492v1`；Method `https://arxiv.org/html/2606.26492v1 — §Within-program versus leave-program-out diagnostic design`；Evaluation `https://arxiv.org/html/2606.26492v1 — §DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis`；未证明边界 `https://arxiv.org/html/2606.26492v1 — §Fault-injected programs and studied diagnosers do not prove production root-cause validity`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29196`；Method `https://arxiv.org/html/2606.29196v1 — §2 Evaluation-Awareness Representations; scale-dependent probe construction`；Evaluation `https://arxiv.org/html/2606.29196v1 — §3 Experimental Setup; 4 Results`；未证明边界 `https://arxiv.org/html/2606.29196v1 — §5 Discussion`。

Review note：`SF-2026-ARXIV-2606-29623`；Method `https://arxiv.org/html/2606.29623v1 — §3 Data-Driven Subset Simulation; 4 Theoretical Guarantees; C Martingale Theory for SCARCE`；Evaluation `https://arxiv.org/html/2606.29623v1 — §5.1 Experiment Setup; 6.1 Experiment Setup; 6.2 Simulation Results`；未证明边界 `https://arxiv.org/html/2606.29623v1 — §7 Conclusion, Limitations, and Extensions; E LLM Transfer Challenges`。

### Source-family integration record

<!-- daily-20260627:PLATFORM-EVALUATION-SYSTEM:start -->
### Owner-merged minimal durable delta

Evaluation 必须分开 generator 能产生什么，与 release selector 能可靠识别什么。对 formalization，type acceptance 与 semantic equivalence 是两个独立 signal；对 repeated sampling，answer coverage 与 selection accuracy 必须分报，并显式记录 correlation/modal ceiling。增加 sample budget 不能修复无法识别已覆盖答案的 oracle 或 selector。

### Trade-off、failure、fallback 与 coexistence

Semantic judge 与 selector 都可能错误或相关；uncovered/undecidable 必须保持 Unknown，高风险分歧交回独立 verification 或人工。

<!-- daily-20260627:PLATFORM-EVALUATION-SYSTEM:end -->

<!-- daily-20260628:PLATFORM-EVALUATION-SYSTEM:start -->
### Owner-merged minimal durable delta

同一个 outcome metric 若在 optimizer、evaluator 与 champion selector 中分别重写，候选即使不变也会发生 selection inversion。Evaluation owner 应发布版本化 callable metric contract，让所有阶段消费同一 extraction/aggregation artifact，并保存 raw trajectory、contract revision 与可重算 verdict。

### Trade-off、failure、fallback 与 coexistence

一个 canonical metric 不能修复错误目标或缺失 trajectory；contract migration 也会改变历史可比性。Schema/semantics 不兼容时 Gate 保持 Open，并用旧 revision 对 raw evidence 重算。

<!-- daily-20260628:PLATFORM-EVALUATION-SYSTEM:end -->

<!-- recovered-daily-20260623:PLATFORM-EVALUATION-SYSTEM:start -->
### 2026-06-23 evidence integration — PLATFORM-EVALUATION-SYSTEM

相邻章 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22783**：Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints 的 exact-v1 机制为：We introduce VERITAS (Verifiable Traversal Assessment for Search), a framework built on the principle of computationally irreducible constraints. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 该 family 的 failure pressure 是：We break this paradox by shifting the evaluation paradigm from simulating a messy reality to constructing computationally pure challenges. 披露的 evaluation signal 是：Evaluating the exhaustive search capabilities of large language models (LLMs) is plagued by a fundamental paradox: verifying completeness requires complete ground truth, yet high-entropy enumeration tasks make such ground truth impossible for humans to create. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-22826**：MINCE: Shrinking LLM Evaluation Datasets via Few-Model Monte Carlo Calibration 的 exact-v1 机制为：We introduce MINCE (Monte Carlo Informed N-sizing for Compact Evaluation), which uses Monte Carlo simulation over per-item logs from a small set of calibration models to find the minimum subset size that bounds accuracy drift and then fixes a randomly sampled subset at that size, with no prediction layer needed. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 该 family 的 failure pressure 是：Existing subset selection methods reduce this cost but depend on large calibration pools or learned prediction layers. 披露的 evaluation signal 是：Evaluating LLMs across many model variants -- quantized, fine-tuned, or deployment-specific -- requires running large benchmarks repeatedly, a process that can take tens of hours per model on edge hardware such as NPUs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:PLATFORM-EVALUATION-SYSTEM:end -->

<!-- recovered-daily-20260624:PLATFORM-EVALUATION-SYSTEM:start -->
### 2026-06-24 evidence integration — PLATFORM-EVALUATION-SYSTEM

相邻章 `books/part-06-ai-infrastructure/67-monitoring.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24074**：把一次性 benchmark 分数改成带双侧错误界、逐 token 成本和停止阈值的 SPRT certification；certifier 持有 query/score/log-likelihood state，跨阈值才发布 reliable/unreliable verdict。 只证明给定 reliability gap、binary correctness oracle 与 small-error leading order；不证明开放式 judge 标签、分布漂移或任意非独立 query 下仍满足同一界。
- **SF-2026-ARXIV-2606-24081**：把 T2I jailbreak 的 prompt-only 比较升级为 paper-to-pipeline contract：attack module、victim、filter、multimodal judge、配置、日志与版本 artifact 共同成为可复现状态。 11 种 attack、4 个 victim 与论文匹配配置不证明未知 attack 自动复现；prompt/heuristic memory update 及 closed-source safety filter 仍是黑盒边界。
- **SF-2026-ARXIV-2606-24124**：将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。 逐步验证成本随 trace 线性增长，semantic deduction 仍依赖 LLM audit，inference schema library 有限；三类 benchmark 不证明任意开放域推理。
- **SF-2026-ARXIV-2606-24996**：deployment-facing leaderboard claim 必须经过 interface lock、clean positive anchor、native negative control、power/false-promotion 与 first-failing-gate report card；任一 gate 失败即禁止发布 selection inversion。 证据来自 forecasting candidate families 与两个 locked interface；不证明所有 task metric 或业务成本可被同一 gate 捕获，underpowered audit 只能给 inconclusive。

<!-- recovered-daily-20260624:PLATFORM-EVALUATION-SYSTEM:end -->

<!-- recovered-daily-20260625:PLATFORM-EVALUATION-SYSTEM:start -->
### 2026-06-25 evidence integration — PLATFORM-EVALUATION-SYSTEM

- **SF-2026-ARXIV-2606-25487**：`3 Setup; Appendix A Prompts, wrappers, and attack configuration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `6 Limitations` 是 `How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring` 的 source-specific 反例/局限边界；若运行条件离开 `4 Results; 4.1 Calibration against human labels; 4.3 white-box attack` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25622**：`IV Theoretical Framework: MAS Architecture and Experimental Setup` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `VI Limitations & Future Work` 是 `Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz` 的 source-specific 反例/局限边界；若运行条件离开 `V Results & Discussion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25760**：`3 Benchmark and Evaluation Protocol; 7 Inductive-Conformal Click Disks` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `A4 Out-of-distribution analysis; A5 Methods deferred; A25 vendor protocol details` 是 `Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets` 的 source-specific 反例/局限边界；若运行条件离开 `4 UQ Generalizes Selectively; 5 Graded Error and Calibration` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25782**：`2 Dataset; 3 Adversarial Attack Methodology; 4 Safety Judge Panel` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `OOD holdout and multi-turn attack boundary; 0.B Inference Throughput and Latency` 是 `Do Encoders Suffice? A Systematic Comparison of Encoder and Decoder Safety Judges for LLM Adversarial Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation Protocol; 6 Results; 6.3 Cost and Latency Trade-offs` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26071**：`4 Protocol and Methods; 5 Environments; 7 Methodological Insights` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `10 Limitations and Future Work; negative-results and confounding boundary` 是 `Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment` 的 source-specific 反例/局限边界；若运行条件离开 `6 Case Studies; 8 Recommendations` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26185**：`Temperature-control and reproducibility protocol for LLM-as-judge safety evaluation` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Temperature control is necessary but not sufficient; prompt/model/vendor drift remains` 是 `Necessary but Not Sufficient: Temperature Control and Reproducibility in LLM-as-Judge Safety Evaluations` 的 source-specific 反例/局限边界；若运行条件离开 `Cross-temperature, repeat-run and judge-agreement evaluation` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26300**：`Verification Horizon formulation for coding-agent rewards` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `No universal reward verifier; longer horizons and hidden environment state remain` 是 `The Verification Horizon: No Silver Bullet for Coding Agent Rewards` 的 source-specific 反例/局限边界；若运行条件离开 `Reward-verification experiments across coding horizons` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26429**：`DualEval joint model-item calibration` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Joint calibration assumes the evaluated item/model pool; new distributions require refitting` 是 `DualEval: Joint Model-Item Calibration for Unified LLM Evaluation` 的 source-specific 反例/局限边界；若运行条件离开 `Unified LLM evaluation experiments and calibration analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26456**：`Safety-Aware Mutation Testing proposal and interaction-aware mutant model` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Vision paper: no completed empirical stop-rule validation; ADS component/fault model is provisional` 是 `Towards Safety-Aware Mutation Testing for Autonomous Driving Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Simulation-based ADS testing protocol and proposed adequacy criterion` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26492**：`Within-program versus leave-program-out diagnostic design` 所定义的源特定机制用于把校准、误差分层、停止条件或复现参数提升为 release gate 的显式状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Fault-injected programs and studied diagnosers do not prove production root-cause validity` 是 `Evaluation-Strategy Gap in Fault Diagnosis of Deep Learning Programs` 的 source-specific 反例/局限边界；若运行条件离开 `DynFault: 5,542 traces from 38 DL programs; balanced-accuracy gap analysis` 的验证域，`PLATFORM-EVALUATION-SYSTEM` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:PLATFORM-EVALUATION-SYSTEM:end -->

<!-- june29-owner:PLATFORM-EVALUATION-SYSTEM:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29196`、`SF-2026-ARXIV-2606-29623`）。** 现有 Evaluation 正文管理 dataset/model/evaluator/metric/release 分权，却未把模型识别 evaluation context 的内部 signal 作为 benchmark 污染诊断，并限制其只能触发额外评测。 现有 Evaluation 正文要求 slice、校准与反例，但缺少在零失败观测下以 adaptive rare-event cascade、ruler revision 与 anytime-valid upper envelope持有风险证据。 因此本次把这些增量合并到同一知识 owner：能力评测不能假设模型对 evaluation context 无感；evaluation-awareness probe 必须作为 contamination sensor，按模型尺度和表示深度版本化，并在异常时阻止 pooled score 直接取得 release authority。Probe 迁移失败时回退 blind/held-out protocol 与外部 outcome。 高风险 release 不能用普通 Monte Carlo 的零观察失败推断安全；SCARCE 类 cascade 将 rare-event region、latent ruler、停止条件与概率上界保存为验收证据。Ruler/分布假设失效时恢复更保守采样或保持 Gate Open。 共同代价与回退边界是：SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，且 Qwen/Gemma 的深度迁移不构成跨 family scaling law。异常只触发额外 held-out evaluation，不授予直接拒绝权。 MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；论文明确指出 behavioral fleet 约 2,000 variants 仍不足、Mahalanobis ruler 可结构性失效，跨 corpus 必须重新校准。否则 Gate 保持 Open。

<!-- june29-owner:PLATFORM-EVALUATION-SYSTEM:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-FED-PERSONALIZATION-SILENT-FAILURES:start -->
- `SF-FED-PERSONALIZATION-SILENT-FAILURES` — Daily `2026-06-01`；primary `arXiv:2606.00947v1`；Books review `books-review:SF-FED-PERSONALIZATION-SILENT-FAILURES`。

  **已吸收的语义增量：** Federated foundation-model personalization makes client-level behavior inaccessible to a central observer, so bias, miscalibration, fairness collapse, adaptation misalignment, out-of-domain degradation, and alignment erosion can pass ordinary aggregate acceptance; the durable delta is a privacy-preserving behavioral-evaluation contract that assigns what may be observed, aggregated, audited, and used for release. 证据边界：This exact-v1 paper is a taxonomy and research vision rather than an implemented monitor or newly executed benchmark; it does not establish complete detectors, production thresholds, or that privacy-preserving statistics can identify every client-local failure without weakening privacy.
<!-- daily-books-trace:SF-FED-PERSONALIZATION-SILENT-FAILURES:end -->

<!-- daily-books-trace:SF-COMPRESSION-UNCERTAINTY:start -->
- `SF-COMPRESSION-UNCERTAINTY` — Daily `2026-06-02`；primary `arXiv:2606.01850v1`；Books review `books-review:SF-COMPRESSION-UNCERTAINTY`。

  **已吸收的语义增量：** 压缩评估通常只比较 accuracy/perplexity，却可能遗漏置信集合扩大与 selective-risk 变化。
<!-- daily-books-trace:SF-COMPRESSION-UNCERTAINTY:end -->

<!-- daily-books-trace:SF-DRIFT-TELBENCH:start -->
- `SF-DRIFT-TELBENCH` — Daily `2026-06-02`；primary `arXiv:2606.02060v1`；Books review `books-review:SF-DRIFT-TELBENCH`。

  **已吸收的语义增量：** 补 outcome→span→first harmful commitment→claim propagation。
<!-- daily-books-trace:SF-DRIFT-TELBENCH:end -->

<!-- daily-books-trace:SF-LLMFI-ERROR-PROPAGATION:start -->
- `SF-LLMFI-ERROR-PROPAGATION` — Daily `2026-06-02`；primary `arXiv:2606.02430v1`；Books review `books-review:SF-LLMFI-ERROR-PROPAGATION`。

  **已吸收的语义增量：** 补 LLM inference 中 layer/operation/token/task 的 propagation chain 与 mitigation evidence boundary。
<!-- daily-books-trace:SF-LLMFI-ERROR-PROPAGATION:end -->

<!-- daily-books-trace:SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION:start -->
- `SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION` — Daily `2026-06-03`；primary `arXiv:2607.01251v1`；Books review `books-review:SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION`。

  **已吸收的语义增量：** §3: consultants may revise beliefs and answers, isolate a disputed crux and converge; the weaker judge verifies the terminal consensus/crux instead of arbitrating fixed adversarial positions. Boundary: Results depend on at least one initially correct consultant, generally instruction-following consultants, filtered natural disagreements and API-hosted models; dishonest collusion and both-wrong starts are not solved.
<!-- daily-books-trace:SF-COLLABORATIVE-DISAGREEMENT-RESOLUTION:end -->

<!-- daily-books-trace:SF-CONTAMINATION-AUDIT-RELIABILITY:start -->
- `SF-CONTAMINATION-AUDIT-RELIABILITY` — Daily `2026-06-03`；primary `arXiv:2606.03305v1`；Books review `books-review:SF-CONTAMINATION-AUDIT-RELIABILITY`。

  **已吸收的语义增量：** In our experiments, we use the following methods: Post-Hoc Dataset Inference, LLM Dataset Inference, and CoDeC, which are described in this section. This method [ 20 ] builds on membership inference attacks, but shifts the unit of analysis from individual samples to datasets . For LLMs, a single-sample MIA is often too noisy to be reliably useful: many sequences are “easy” (low loss) even if they were never seen during training, and the membership signal for any particular example becomes faint as models scale. Boundary: In this work, we examined the reliability of contamination detection methods by moving from the controlled settings of prior literature to the realistic, "in-the-wild" regime of modern instruction-tuned models 2 2 2 https://anonymous.4open.science/r/reliability-gap-benchmark-auditing/README.md . We stress-tested three leading detection paradigms against the complexities of post-training mixtures and opaque data provenance. Our findings reveal that the transition from academic validation to practical auditing is fraught with challenges: The I.I.D.
<!-- daily-books-trace:SF-CONTAMINATION-AUDIT-RELIABILITY:end -->

<!-- daily-books-trace:SF-JUDGE-SUBSPACE-ALIGNMENT:start -->
- `SF-JUDGE-SUBSPACE-ALIGNMENT` — Daily `2026-06-03`；primary `arXiv:2606.03043v1`；Books review `books-review:SF-JUDGE-SUBSPACE-ALIGNMENT`。

  **已吸收的语义增量：** The paper represents judge score matrices geometrically and compares score spread, effective rank, principal angles to the human subspace and stacked judge-human correlations, separating inter-LLM consensus from alignment to human evaluation axes. Boundary: The measured geometry is conditional on the selected community datasets, rubrics, languages, judge prompts and human pools; strong consensus or subspace angle is diagnostic evidence and does not prove general judge bias, causal alignment failure or every deployment's evaluation quality.
<!-- daily-books-trace:SF-JUDGE-SUBSPACE-ALIGNMENT:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07379:start -->
- `SF-2026-ARXIV-2606-07379` — Daily `2026-06-06`；primary `arXiv:2606.07379v1`；Books review `books-review:SF-2026-ARXIV-2606-07379`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07379:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07462:start -->
- `SF-2026-ARXIV-2606-07462` — Daily `2026-06-06`；primary `arXiv:2606.07462v1`；Books review `books-review:SF-2026-ARXIV-2606-07462`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07462:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07783:start -->
- `SF-2026-ARXIV-2606-07783` — Daily `2026-06-06`；primary `arXiv:2606.07783v1`；Books review `books-review:SF-2026-ARXIV-2606-07783`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07783:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07822:start -->
- `SF-2026-ARXIV-2606-07822` — Daily `2026-06-06`；primary `arXiv:2606.07822v1`；Books review `books-review:SF-2026-ARXIV-2606-07822`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07822:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07834:start -->
- `SF-2026-ARXIV-2606-07834` — Daily `2026-06-06`；primary `arXiv:2606.07834v1`；Books review `books-review:SF-2026-ARXIV-2606-07834`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07834:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07874:start -->
- `SF-2026-ARXIV-2606-07874` — Daily `2026-06-06`；primary `arXiv:2606.07874v1`；Books review `books-review:SF-2026-ARXIV-2606-07874`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07874:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08960:start -->
- `SF-2026-ARXIV-2606-08960` — Daily `2026-06-09`；primary `arXiv:2606.08960v1`；Books review `books-review:SF-2026-ARXIV-2606-08960`。

  **已吸收的语义增量：** benchmark verifier 应通过 hacker→fixer→solver 的闭环迭代：攻击发现 exploit、修补拒绝 exploit、solver 防止补丁把合法解一并拒绝。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08960:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09809:start -->
- `SF-2026-ARXIV-2606-09809` — Daily `2026-06-09`；primary `arXiv:2606.09809v1`；Books review `books-review:SF-2026-ARXIV-2606-09809`。

  **已吸收的语义增量：** Evaluation result 需要把 benchmark metadata、run data 与 model metadata 组合成可追踪 record，并按读者呈现 reproducibility、completeness、provenance/risk 与 score comparability。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09809:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11686:start -->
- `SF-2026-ARXIV-2606-11686` — Daily `2026-06-11`；primary `arXiv:2606.11686v1`；Books review `books-review:SF-2026-ARXIV-2606-11686`。

  **已吸收的语义增量：** 生产 Agent 的 deterministic scaffold 应按 ontology/intent/routing/decomposition/escalation/safety/memory 分层，用 no-LLM regression-locked slices 阻止 aggregate pass rate 掩盖局部回归。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11686:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13044:start -->
- `SF-2026-ARXIV-2606-13044` — Daily `2026-06-12`；primary `arXiv:2606.13044v1`；Books review `books-review:SF-2026-ARXIV-2606-13044`。

  **已吸收的语义增量：** AI reviewer release gate 必须加入 evidence-invariant presentation counterfactual，防止固定方法/结果仅靠 framing 改写评分
<!-- daily-books-trace:SF-2026-ARXIV-2606-13044:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13221:start -->
- `SF-2026-ARXIV-2606-13221` — Daily `2026-06-12`；primary `arXiv:2606.13221v1`；Books review `books-review:SF-2026-ARXIV-2606-13221`。

  **已吸收的语义增量：** LLM-judge ranking 需要先把 per-battle score difference校准为 win probability，再对 judge-human Elo residual做 split-conformal interval
<!-- daily-books-trace:SF-2026-ARXIV-2606-13221:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13608:start -->
- `SF-2026-ARXIV-2606-13608` — Daily `2026-06-12`；primary `arXiv:2606.13608v1`；Books review `books-review:SF-2026-ARXIV-2606-13608`。

  **已吸收的语义增量：** Agent benchmark 应把 task/environment/evaluator protocol做成可部署 assessment contract，并保存run identity、submission与verdict lineage
<!-- daily-books-trace:SF-2026-ARXIV-2606-13608:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13904:start -->
- `SF-2026-ARXIV-2606-13904` — Daily `2026-06-12`；primary `arXiv:2606.13904v1`；Books review `books-review:SF-2026-ARXIV-2606-13904`。

  **已吸收的语义增量：** data-lake QA Agent 应通过gold source sequence、sanitized subquestion与idealized tool ablation把search/planning/analysis/action-policy failure分开
<!-- daily-books-trace:SF-2026-ARXIV-2606-13904:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14000:start -->
- `SF-2026-ARXIV-2606-14000` — Daily `2026-06-12`；primary `arXiv:2606.14000v1`；Books review `books-review:SF-2026-ARXIV-2606-14000`。

  **已吸收的语义增量：** autoformalization不能以kernel acceptance作为唯一质量gate；还应审计semantic faithfulness、Mathlib reuse与cross-file reuse
<!-- daily-books-trace:SF-2026-ARXIV-2606-14000:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15122:start -->
- `SF-2026-ARXIV-2606-15122` — Daily `2026-06-14`；primary `arXiv:2606.15122v1`；Books review `books-review:SF-2026-ARXIV-2606-15122`。

  **已吸收的语义增量：** LLM 只负责为告警构造 analysis harness；harness validation 与 backend formal analysis 才拥有 no-bug discharge authority。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15122:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15153:start -->
- `SF-2026-ARXIV-2606-15153` — Daily `2026-06-14`；primary `arXiv:2606.15153v1`；Books review `books-review:SF-2026-ARXIV-2606-15153`。

  **已吸收的语义增量：** selective risk control 必须同时审计 confidence-bound tightness 与 exchangeability；group shift 时应按组重校准并显式支付 coverage cost。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15153:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15258:start -->
- `SF-2026-ARXIV-2606-15258` — Daily `2026-06-14`；primary `arXiv:2606.15258v1`；Books review `books-review:SF-2026-ARXIV-2606-15258`。

  **已吸收的语义增量：** step-level proof evaluation 应遮蔽真实 proof step、保留必要上下文并以重复 judge/人审校验等价性，避免从最终答案反推每步正确。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15258:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15306:start -->
- `SF-2026-ARXIV-2606-15306` — Daily `2026-06-14`；primary `arXiv:2606.15306v1`；Books review `books-review:SF-2026-ARXIV-2606-15306`。

  **已吸收的语义增量：** 跨任务 experiential learning 需要共享 ground-truth latent 的可控环境，分别测 adaptation neglect、breakdown、miscalibration 与 exploration/exploitation。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15306:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15345:start -->
- `SF-2026-ARXIV-2606-15345` — Daily `2026-06-14`；primary `arXiv:2606.15345v1`；Books review `books-review:SF-2026-ARXIV-2606-15345`。

  **已吸收的语义增量：** 跨语言 deep-research 评测要把 retriever recall、agent evidence integration、citation precision 与 calibration 分开，避免端到端分数吞掉 bottleneck。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15345:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15385:start -->
- `SF-2026-ARXIV-2606-15385` — Daily `2026-06-14`；primary `arXiv:2606.15385v1`；Books review `books-review:SF-2026-ARXIV-2606-15385`。

  **已吸收的语义增量：** Agent RL 评测必须分开 observed proxy reward 与 hidden task reward；更强 exploration、credit assignment 或 entropy 不能修复错误规格。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15385:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15474:start -->
- `SF-2026-ARXIV-2606-15474` — Daily `2026-06-14`；primary `arXiv:2606.15474v1`；Books review `books-review:SF-2026-ARXIV-2606-15474`。

  **已吸收的语义增量：** 持续评测必须用固定人标 anchor 与第二条 anytime-valid e-process 区分 system drift 和 judge drift，并让 anchor race 快于主告警。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15474:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15608:start -->
- `SF-2026-ARXIV-2606-15608` — Daily `2026-06-15`；primary `arXiv:2606.15608v1`；Books review `books-review:SF-2026-ARXIV-2606-15608`。

  **已吸收的语义增量：** 多模态judge的release gate应包含score-inflation adversary、binary-semantic induction与proxy-manifold transfer测试
<!-- daily-books-trace:SF-2026-ARXIV-2606-15608:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15610:start -->
- `SF-2026-ARXIV-2606-15610` — Daily `2026-06-15`；primary `arXiv:2606.15610v1`；Books review `books-review:SF-2026-ARXIV-2606-15610`。

  **已吸收的语义增量：** LLM judge应作为measurement instrument发布datasheet，分别量dark current、surface cross-sensitivity、position false preference、target sensitivity与criterion
<!-- daily-books-trace:SF-2026-ARXIV-2606-15610:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15834:start -->
- `SF-2026-ARXIV-2606-15834` — Daily `2026-06-15`；primary `arXiv:2606.15834v1`；Books review `books-review:SF-2026-ARXIV-2606-15834`。

  **已吸收的语义增量：** AI-evolved system promotion必须用baseline-vs-candidate differential oracle搜索correctness/runtime/memory/quality反例，而不能只接受训练/公开workload score
<!-- daily-books-trace:SF-2026-ARXIV-2606-15834:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15841:start -->
- `SF-2026-ARXIV-2606-15841` — Daily `2026-06-15`；primary `arXiv:2606.15841v1`；Books review `books-review:SF-2026-ARXIV-2606-15841`。

  **已吸收的语义增量：** budgeted verifier allocation不能假设proxy score跨cost strata可比；需先诊断heteroskedastic discriminability再决定global或stratified threshold
<!-- daily-books-trace:SF-2026-ARXIV-2606-15841:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15964:start -->
- `SF-2026-ARXIV-2606-15964` — Daily `2026-06-15`；primary `arXiv:2606.15964v1`；Books review `books-review:SF-2026-ARXIV-2606-15964`。

  **已吸收的语义增量：** prompt/domain shift下conformal risk control需显式检测drift、更新calibration window并在保证失效时abstain，而不能继承旧coverage
<!-- daily-books-trace:SF-2026-ARXIV-2606-15964:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16000:start -->
- `SF-2026-ARXIV-2606-16000` — Daily `2026-06-15`；primary `arXiv:2606.16000v1`；Books review `books-review:SF-2026-ARXIV-2606-16000`。

  **已吸收的语义增量：** AutoML Agent pre-deployment gate应以组织内sandbox、hidden executable validators、evaluator-private labels、workflow state与reproducible final artifact共同验收
<!-- daily-books-trace:SF-2026-ARXIV-2606-16000:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16062:start -->
- `SF-2026-ARXIV-2606-16062` — Daily `2026-06-15`；primary `arXiv:2606.16062v1`；Books review `books-review:SF-2026-ARXIV-2606-16062`。

  **已吸收的语义增量：** code RL task在进入训练前必须审计hackability，并让generated test先通过gold-sanity gate再交给LLM judge与promotion loop
<!-- daily-books-trace:SF-2026-ARXIV-2606-16062:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16190:start -->
- `SF-2026-ARXIV-2606-16190` — Daily `2026-06-16`；primary `arXiv:2606.16190v1`；Books review `books-review:SF-2026-ARXIV-2606-16190`。

  **已吸收的语义增量：** edge-model Agent 的验收对象是 model+firmware+真实硬件闭环；compile/flash/measure 证据不能由模拟器 reward 代替
<!-- daily-books-trace:SF-2026-ARXIV-2606-16190:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16511:start -->
- `SF-2026-ARXIV-2606-16511` — Daily `2026-06-16`；primary `arXiv:2606.16511v1`；Books review `books-review:SF-2026-ARXIV-2606-16511`。

  **已吸收的语义增量：** frontier evaluation 的 tail-shape claim 必须先做 threshold/grid/sample-size sensitivity 与 false-positive diagnosis，再允许外推极端风险
<!-- daily-books-trace:SF-2026-ARXIV-2606-16511:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16541:start -->
- `SF-2026-ARXIV-2606-16541` — Daily `2026-06-16`；primary `arXiv:2606.16541v1`；Books review `books-review:SF-2026-ARXIV-2606-16541`。

  **已吸收的语义增量：** natural-language 到 formal statement 的 kernel acceptance 只证明语法/可解；release gate 还需双向语义等价证据与 counterexample search
<!-- daily-books-trace:SF-2026-ARXIV-2606-16541:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16603:start -->
- `SF-2026-ARXIV-2606-16603` — Daily `2026-06-16`；primary `arXiv:2606.16603v1`；Books review `books-review:SF-2026-ARXIV-2606-16603`。

  **已吸收的语义增量：** data-analytic Agent 应把 query/transform/result 编译成可执行 verification graph，使数值结论可由独立节点重放而非只审 prose
<!-- daily-books-trace:SF-2026-ARXIV-2606-16603:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16605:start -->
- `SF-2026-ARXIV-2606-16605` — Daily `2026-06-16`；primary `arXiv:2606.16605v1`；Books review `books-review:SF-2026-ARXIV-2606-16605`。

  **已吸收的语义增量：** world-model robustness benchmark 应冻结 perturbation budget、closed-loop controller 与 horizon，并区分 perception drift、dynamics error 与 return collapse
<!-- daily-books-trace:SF-2026-ARXIV-2606-16605:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16682:start -->
- `SF-2026-ARXIV-2606-16682` — Daily `2026-06-16`；primary `arXiv:2606.16682v1`；Books review `books-review:SF-2026-ARXIV-2606-16682`。

  **已吸收的语义增量：** self-evolving multimodal Agent 的 evaluator 会发生 cross-modal preference contagion；promotion 必须保留 modality-specific holdout 与 evaluator version
<!-- daily-books-trace:SF-2026-ARXIV-2606-16682:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16748:start -->
- `SF-2026-ARXIV-2606-16748` — Daily `2026-06-16`；primary `arXiv:2606.16748v1`；Books review `books-review:SF-2026-ARXIV-2606-16748`。

  **已吸收的语义增量：** computer-use benchmark 应提供跨应用一致的持久 persona、resettable desktop 与 visible-side-effect rubric，而非空账户单 app task
<!-- daily-books-trace:SF-2026-ARXIV-2606-16748:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17005:start -->
- `SF-2026-ARXIV-2606-17005` — Daily `2026-06-16`；primary `arXiv:2606.17005v1`；Books review `books-review:SF-2026-ARXIV-2606-17005`。

  **已吸收的语义增量：** 公开 frontier eval archive 应保存 trial-level uncertainty、selection process 与 decision rule，使 Bayesian update 与发布决策可被重算
<!-- daily-books-trace:SF-2026-ARXIV-2606-17005:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17029:start -->
- `SF-2026-ARXIV-2606-17029` — Daily `2026-06-16`；primary `arXiv:2606.17029v1`；Books review `books-review:SF-2026-ARXIV-2606-17029`。

  **已吸收的语义增量：** deep-research RL 的 rubric 应展开为 evidence tree，让 citation support、coverage 与 synthesis 分层给 reward，避免单一 judge score
<!-- daily-books-trace:SF-2026-ARXIV-2606-17029:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17283:start -->
- `SF-2026-ARXIV-2606-17283` — Daily `2026-06-16`；primary `arXiv:2606.17283v1`；Books review `books-review:SF-2026-ARXIV-2606-17283`。

  **已吸收的语义增量：** vulnerability benchmark 应绑定可构建 source revision、trigger、oracle 与 reproducible container，使检测/修复结果可重放
<!-- daily-books-trace:SF-2026-ARXIV-2606-17283:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17383:start -->
- `SF-2026-ARXIV-2606-17383` — Daily `2026-06-16`；primary `arXiv:2606.17383v1`；Books review `books-review:SF-2026-ARXIV-2606-17383`。

  **已吸收的语义增量：** Agentic AI model validation 应分别检查 belief-state filter、forecast transition 与 policy action，并以 POMDP identity 绑定三层误差
<!-- daily-books-trace:SF-2026-ARXIV-2606-17383:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20695:start -->
- `SF-2026-ARXIV-2606-20695` — Daily `2026-06-16`；primary `arXiv:2606.20695v1`；Books review `books-review:SF-2026-ARXIV-2606-20695`。

  **已吸收的语义增量：** MAS coordination gain 必须与 paired single-Agent run 和 noise floor 比较，避免把 sampling variance 当协作收益
<!-- daily-books-trace:SF-2026-ARXIV-2606-20695:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17546:start -->
- `SF-2026-ARXIV-2606-17546` — Daily `2026-06-17`；primary `arXiv:2606.17546v1`；Books review `books-review:SF-2026-ARXIV-2606-17546`。

  **已吸收的语义增量：** Self-evolving Agent 的 EvalSpec 应冻结 train/validation/ID-OOD test/replay/cost views、evolution schedule、snapshot 与 update lineage，final snapshot 不得代表 best snapshot。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17546:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17609:start -->
- `SF-2026-ARXIV-2606-17609` — Daily `2026-06-17`；primary `arXiv:2606.17609v1`；Books review `books-review:SF-2026-ARXIV-2606-17609`。

  **已吸收的语义增量：** 压缩/剪枝模型 release 不能只看 multiple-choice recognition；同一知识 slice 必须加入 open-generation、answerability 与形式变化对照，区分识别保留和生成失效。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17609:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17819:start -->
- `SF-2026-ARXIV-2606-17819` — Daily `2026-06-17`；primary `arXiv:2606.17819v1`；Books review `books-review:SF-2026-ARXIV-2606-17819`。

  **已吸收的语义增量：** Skill evaluation 必须固定 base agent、skill artifact/version、activation condition、no-skill control 与 task-family slice，才能把 skill value 与模型/任务难度分离。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17819:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17930:start -->
- `SF-2026-ARXIV-2606-17930` — Daily `2026-06-17`；primary `arXiv:2606.17930v1`；Books review `books-review:SF-2026-ARXIV-2606-17930`。

  **已吸收的语义增量：** Frontier capability 必须报告为 inference-compute curve，并冻结 serial/parallel allocation、submission次数、feedback、compaction 与 matched budget；单点分数不能比较 generations。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17930:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18168:start -->
- `SF-2026-ARXIV-2606-18168` — Daily `2026-06-17`；primary `arXiv:2606.18168v1`；Books review `books-review:SF-2026-ARXIV-2606-18168`。

  **已吸收的语义增量：** Agent-authored tests 的 verifier strength 不能用“创建 test 文件”代理；release gate 应解析 assertion/oracle signal、执行路径与 failure discriminativeness。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18168:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18356:start -->
- `SF-2026-ARXIV-2606-18356` — Daily `2026-06-17`；primary `arXiv:2606.18356v1`；Books review `books-review:SF-2026-ARXIV-2606-18356`。

  **已吸收的语义增量：** Agent security EvalSpec 必须分开 semantic compromise、artifact-visible harm evidence 与 sandbox-observed state/tool harm，并保持各自 denominator 和 matched identity。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18356:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18467:start -->
- `SF-2026-ARXIV-2606-18467` — Daily `2026-06-17`；primary `arXiv:2606.18467v1`；Books review `books-review:SF-2026-ARXIV-2606-18467`。

  **已吸收的语义增量：** Tool/retrieval trajectory release 可把 step risk校准为 trajectory conformal acceptance，并用 supermartingale anytime alarm监测运行中超界；drift时必须重校准或 abstain。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18467:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20708:start -->
- `SF-2026-ARXIV-2606-20708` — Daily `2026-06-17`；primary `arXiv:2606.20708v1`；Books review `books-review:SF-2026-ARXIV-2606-20708`。

  **已吸收的语义增量：** User simulator不能只匹配对话流畅度；应以真实 consequential outcome校准 decision fidelity，并单独测量disengagement/走开行为，否则模拟用户会系统性过度合作。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20708:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20724:start -->
- `SF-2026-ARXIV-2606-20724` — Daily `2026-06-17`；primary `arXiv:2606.20724v1`；Books review `books-review:SF-2026-ARXIV-2606-20724`。

  **已吸收的语义增量：** Web Agent 的 finish signal与 correctness必须分离；trace审计需识别 search loop、premature partial termination和cross-source synthesis collapse，并冻结并行探索拓扑。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20724:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19057:start -->
- `SF-2026-ARXIV-2606-19057` — Daily `2026-06-18`；primary `arXiv:2606.19057v1`；Books review `books-review:SF-2026-ARXIV-2606-19057`。

  **已吸收的语义增量：** 当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19057:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19613:start -->
- `SF-2026-ARXIV-2606-19613` — Daily `2026-06-18`；primary `arXiv:2606.19613v1`；Books review `books-review:SF-2026-ARXIV-2606-19613`。

  **已吸收的语义增量：** coding-agent evaluation 应把一次长 session 建模为连续 change requests，并观察首次不可恢复失败，而不是把独立 task solve rate 当 stamina。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19613:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20736:start -->
- `SF-2026-ARXIV-2606-20736` — Daily `2026-06-18`；primary `arXiv:2606.20736v1`；Books review `books-review:SF-2026-ARXIV-2606-20736`。

  **已吸收的语义增量：** 受污染 benchmark 可把 answer-bearing visual key 变成运行时随机生成、human-validated edit slot，并保留 construction-grounded label。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20736:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19704:start -->
- `SF-2026-ARXIV-2606-19704` — Daily `2026-06-19`；primary `arXiv:2606.19704v1`；Books review `books-review:SF-2026-ARXIV-2606-19704`。

  **已吸收的语义增量：** `Beyond Static Leaderboards: Predictive Validity for the Evaluation of LLM Agents` 路由到 `PLATFORM-EVALUATION-SYSTEM`：它不再用单次 aggregate mean 排名决定发布，而要求 evaluation owner 保存 configuration identity，并以 in-sample/OOD rank correlation、judge-independent trajectory verifier 和持久 benchmark transport 判断配置能否外推；旧 leaderboard 可保留为观测列，不能继续拥有 release 决策。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19704:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19714:start -->
- `SF-2026-ARXIV-2606-19714` — Daily `2026-06-19`；primary `arXiv:2606.19714v1`；Books review `books-review:SF-2026-ARXIV-2606-19714`。

  **已吸收的语义增量：** `AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge Auditing` 路由到 `PLATFORM-EVALUATION-SYSTEM`：AURA 把 judge trust 作为可更新隐状态：人类只验证 uncertainty 高的 pair，refinement 将已验证的一致性信号传播到其余比较，再更新下一轮采样；evaluation owner 而非 judge 独占抽样、停止和审计轨迹。其代价是传播错误会放大初始偏差，需保留随机抽检和预算耗尽时的原始 judge/human fallback。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19714:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20536:start -->
- `SF-2026-ARXIV-2606-20536` — Daily `2026-06-19`；primary `arXiv:2606.20536v1`；Books review `books-review:SF-2026-ARXIV-2606-20536`。

  **已吸收的语义增量：** `The FID Lottery: Quantifying Hidden Randomness in Generative-Model Evaluation` 路由到 `PLATFORM-EVALUATION-SYSTEM`：FID 验收从单次 seed 分数改为显式训练 seed×生成 seed 分布与置信区间；evaluation owner 保存随机性来源，release 依据分布而非最好一次。增加重复成本，预算不足时至少报告 seed sensitivity 而非隐藏。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20536:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20820:start -->
- `SF-2026-ARXIV-2606-20820` — Daily `2026-06-19`；primary `arXiv:2606.20820v1`；Books review `books-review:SF-2026-ARXIV-2606-20820`。

  **已吸收的语义增量：** `CELEUS: Certifiable and Efficient LLM Evaluation via E-Processes` 路由到 `PLATFORM-EVALUATION-SYSTEM`：Celeus 用 e-process 构造 anytime-valid CI：sampler 依据 uncertainty 选样，surrogate 估计未评样本，evaluation scheduler 可在任意时间按 CI width 停止而保持 coverage；surrogate 失配时回退均匀抽样/有限总体界。代价是 i.i.d./有限池假设与校准开销。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20820:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20873:start -->
- `SF-2026-ARXIV-2606-20873` — Daily `2026-06-19`；primary `arXiv:2606.20873v1`；Books review `books-review:SF-2026-ARXIV-2606-20873`。

  **已吸收的语义增量：** `SciLens: Multi-modal Scientific Claim Verification with Agentic Entailment and Grounding` 路由到 `PLATFORM-EVALUATION-SYSTEM`：SciLens 将科学 claim 分成 empirical/background atoms，再按 table cell/arithmetic 或 figure panel/axis/legend 建 witness，只有全部核心 atom entail 才支持；verifier 拥有 evidence graph，VLM 不能直接二分类。无法定位 witness 时 abstain。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20873:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21389:start -->
- `SF-2026-ARXIV-2606-21389` — Daily `2026-06-20`；primary `arXiv:2606.21389v1`；Books review `books-review:SF-2026-ARXIV-2606-21389`。

  **已吸收的语义增量：** 生产 SIEM telemetry 转研究 artifact 时必须保留时间与 entity consistency，同时声明 anonymization 的 privacy-utility boundary 而非声称形式匿名
<!-- daily-books-trace:SF-2026-ARXIV-2606-21389:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21584:start -->
- `SF-2026-ARXIV-2606-21584` — Daily `2026-06-20`；primary `arXiv:2606.21584v1`；Books review `books-review:SF-2026-ARXIV-2606-21584`。

  **已吸收的语义增量：** deployment threshold 必须从开发集冻结并在目标分布报告 HTER；test-set oracle EER 会隐藏真实 false-reject/false-accept failure
<!-- daily-books-trace:SF-2026-ARXIV-2606-21584:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21678:start -->
- `SF-2026-ARXIV-2606-21678` — Daily `2026-06-20`；primary `arXiv:2606.21678v1`；Books review `books-review:SF-2026-ARXIV-2606-21678`。

  **已吸收的语义增量：** 从 internal representation 可解码出答案不证明 reasoning faithful；diagnostic ladder 要区分 decodability、causal use 与输出行为
<!-- daily-books-trace:SF-2026-ARXIV-2606-21678:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-02577:start -->
- `SF-2026-ARXIV-2607-02577` — Daily `2026-07-01`；primary `arXiv:2607.02577v1`；Books review `books-review:SF-2026-ARXIV-2607-02577`。

  **已吸收的语义增量：** 新增证据边界：Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L844`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-02577:end -->

<!-- daily-books-trace:SF-2026-JUDGE-DELTA-VALIDITY:start -->
- `SF-2026-JUDGE-DELTA-VALIDITY` — Daily `2026-08-26`；primary `arXiv:2608.24419v1`；Books review `books-review:SF-2026-JUDGE-DELTA-VALIDITY`。

  **已吸收的语义增量：** 新增 target-changing sensitivity 与 target-preserving invariance 双臂 contract。
<!-- daily-books-trace:SF-2026-JUDGE-DELTA-VALIDITY:end -->

<!-- daily-books-trace:SF-2026-UQ-ENSEMBLES:start -->
- `SF-2026-UQ-ENSEMBLES` — Daily `2026-08-26`；primary `arXiv:2608.24492v1`；Books review `books-review:SF-2026-UQ-ENSEMBLES`。

  **已吸收的语义增量：** 新增 scorer diversity、domain shift、risk-coverage、abstain 与 human escalation 边界。
<!-- daily-books-trace:SF-2026-UQ-ENSEMBLES:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08200:start -->
- `SF-2026-ARXIV-2606-08200` — Daily `2026-06-07`；primary `arXiv:2606.08200v1`；Books review `books-review:SF-2026-ARXIV-2606-08200`。

  **已吸收的语义增量：** An in-world evaluator actively creates criterion-relevant situations through native dialogue/action, changing evaluation from passive trajectory scoring to coverage-seeking intervention. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08200:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21869:start -->
- `SF-2026-ARXIV-2606-21869` — Daily `2026-06-21`；primary `arXiv:2606.21869v1`；Books review `books-review:SF-2026-ARXIV-2606-21869`。

  **已吸收的语义增量：** 把每语言生成能耗与 accuracy、tokenization expansion 分开记录；evaluation/model card 需声明 per-language energy，而不能用英语平均值代表多语言部署。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21869:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21954:start -->
- `SF-2026-ARXIV-2606-21954` — Daily `2026-06-21`；primary `arXiv:2606.21954v1`；Books review `books-review:SF-2026-ARXIV-2606-21954`。

  **已吸收的语义增量：** Hardness Adjusted Transfer 以 target performance 相对 source-language ability 校正，避免把 source accuracy 提升误报成 cross-lingual transfer 进步。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21954:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22179:start -->
- `SF-2026-ARXIV-2606-22179` — Daily `2026-06-21`；primary `arXiv:2606.22179v1`；Books review `books-review:SF-2026-ARXIV-2606-22179`。

  **已吸收的语义增量：** selective prediction 除 calibration/ranking 还要报告 score granularity：可用阈值数量决定 operator 能选择多少风险工作点；多查询扩大分辨率但增加成本且可能伤害强模型排序。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22179:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-05721:start -->
- `SF-2026-ARXIV-2607-05721` — Daily `2026-07-08`；primary `arXiv:2607.05721v1`；Books review `books-review:SF-2026-ARXIV-2607-05721`。

  **已吸收的语义增量：** 新增证据边界：Move uncertainty from token noise or one sequence score to typed semantic spans, distilling multi-sample claim support into a single-pass probe while preserving an explicit external-verification boundary. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L934; books/part-06-ai-infrastructure/66-evaluation-system.md#L996`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-05721:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-05876:start -->
- `SF-2026-ARXIV-2607-05876` — Daily `2026-07-08`；primary `arXiv:2607.05876v1`；Books review `books-review:SF-2026-ARXIV-2607-05876`。

  **已吸收的语义增量：** 新增证据边界：Replace immediate grid search with a versioned resource vector for weight/KV bytes, FLOPs, communication bytes/messages and capacity; compute optimistic and no-overlap bounds, identify the first binding wall as load changes, compare observed steady-state service time against the bound, and open a profiler only when the residual is material. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L373`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-05876:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06327:start -->
- `SF-2026-ARXIV-2607-06327` — Daily `2026-07-08`；primary `arXiv:2607.06327v1`；Books review `books-review:SF-2026-ARXIV-2607-06327`。

  **已吸收的语义增量：** 新增证据边界：Make uncertainty calibration slice-aware not only by domain, but by generation language, model scale/family and estimator access contract; method rankings can reverse across these slices. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L979`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06327:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-08017:start -->
- `SF-2026-ARXIV-2607-08017` — Daily `2026-07-09`；primary `arXiv:2607.08017v1`；Books review `books-review:SF-2026-ARXIV-2607-08017`。

  **已吸收的语义增量：** 新增证据边界：GraphEVAL samples multiple chains of thought, uses a separate deterministic decomposer to turn each into a claimed causal DAG, and compares semantic/structural graph distance. A graph medoid and GRCS features measure agreement and robustness; an adversarial-medoid intervention tests whether the selector merely follows a central but wrong trace. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L953`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08017:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11942:start -->
- `SF-2026-ARXIV-2607-11942` — Daily `2026-07-12`；primary `arXiv:2607.11942v1`；Books review `books-review:SF-2026-ARXIV-2607-11942`。

  **已吸收的语义增量：** 新增证据边界：Freeze identical models, instances, compression budgets and decoding; vary only whether the query is visible at compression time; compare each method against several trivial start/recent baselines with paired bootstrap; keep the attention backend fixed; run uncompressed and backend controls; quarantine tokenizer-invalid rows; withdraw rankings whose method requires a backend with a measured effect larger than method gaps. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1506`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11942:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11886:start -->
- `SF-2026-ARXIV-2607-11886` — Daily `2026-07-14`；primary `arXiv:2607.11886v1`；Books review `books-review:SF-2026-ARXIV-2607-11886`。

  **已吸收的语义增量：** 新增证据边界：SpectraReward treats a pretrained MLLM as a zero-shot reward by scoring how likely it is to read the original prompt back from an image; Self-SpectraReward adds self-reconstruction/spectral features without training a dedicated reward model. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11886:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13705:start -->
- `SF-2026-ARXIV-2607-13705` — Daily `2026-07-16`；primary `arXiv:2607.13705v1`；Books review `books-review:SF-2026-ARXIV-2607-13705`。

  **已吸收的语义增量：** 新增证据边界：Evaluation identity expands to model × benchmark × harness × environment × scorer with trajectories retained before aggregation. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13705:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-15263:start -->
- `SF-2026-ARXIV-2607-15263` — Daily `2026-07-17`；primary `arXiv:2607.15263v1`；Books review `books-review:SF-2026-ARXIV-2607-15263`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: peak security success -> workload-specific success/cost/refusal operating curves with contamination controls 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-15263:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16868:start -->
- `SF-2026-ARXIV-2607-16868` — Daily `2026-07-19`；primary `arXiv:2607.16868v1`；Books review `books-review:SF-2026-ARXIV-2607-16868`。

  **已吸收的语义增量：** 新增证据边界：Sampled answers are first collapsed into semantic classes, then organized by implication and incompatibility; probability mass at maximal roots yields an uncertainty sensor that distinguishes paraphrase diversity from mutually exclusive hypotheses. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16868:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-19865:start -->
- `SF-2026-ARXIV-2607-19865` — Daily `2026-07-23`；primary `arXiv:2607.19865v1`；Books review `books-review:SF-2026-ARXIV-2607-19865`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: final-answer judge -> executable artifact-state predicates plus preservation invariants and verifier-fidelity audit 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L778`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-19865:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-20734:start -->
- `SF-2026-ARXIV-2607-20734` — Daily `2026-07-23`；primary `arXiv:2607.20734v1`；Books review `books-review:SF-2026-ARXIV-2607-20734`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: static single-turn task -> versioned intent-state transitions -> final anchored verifier plus transition-specific diagnostics 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1225`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-20734:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27231:start -->
- `SF-2026-ARXIV-2607-27231` — Daily `2026-07-23`；primary `arXiv:2607.27231v1`；Books review `books-review:SF-2026-ARXIV-2607-27231`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: single-source/single-GPU pass rate -> multi-source operator contract -> cross-chip correctness, speed and cost frontier 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L450`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27231:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21217:start -->
- `SF-2026-ARXIV-2607-21217` — Daily `2026-07-24`；primary `arXiv:2607.21217v1`；Books review `books-review:SF-2026-ARXIV-2607-21217`。

  **已吸收的语义增量：** 新增证据边界：Verified repositories and tests define GroundPRD; constraints are selectively hidden into User Agent Data; agents may ask bounded clarification questions; generated repositories are evaluated by public/hidden black-box behavior plus structural and interaction diagnostics rather than source-copy similarity. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1479`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21217:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21962:start -->
- `SF-2026-ARXIV-2607-21962` — Daily `2026-07-25`；primary `arXiv:2607.21962v1`；Books review `books-review:SF-2026-ARXIV-2607-21962`。

  **已吸收的语义增量：** 新增证据边界：Ground-truth facts, validity intervals, provenance and as-of dates become canonical state before conversation rendering, enabling separate write/read audits and tenure-aware architecture comparison. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L736`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21962:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25886:start -->
- `SF-2026-ARXIV-2607.25886` — Daily `2026-07-29`；primary `arXiv:2607.25886v1`；Books review `books-review:SF-2026-ARXIV-2607.25886`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: end-to-end agent score -> fixed research substrate -> checkpoint trajectory evidence -> explicit best-checkpoint and stopping policy. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25886:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.27353:start -->
- `SF-2026-ARXIV-2607.27353` — Daily `2026-07-30`；primary `arXiv:2607.27353v1`；Books review `books-review:SF-2026-ARXIV-2607.27353`。

  **已吸收的语义增量：** 新增证据边界：LayerRAG-Bench injects faults at evidence, tool-contract, authorization and session-state layers and shows schema normalization repairs only schema drift. The result establishes a layer-specific credit rule: grounded output cannot hide stale or wrong-session evidence, and a repair must not be promoted beyond its target layer. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L520`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.27353:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-15127:start -->
- `SF-2026-ARXIV-2608-15127` — Daily `2026-08-16`；primary `arXiv:2608.15127v1`；Books review `books-review:SF-2026-ARXIV-2608-15127`。

  **已吸收的语义增量：** AgentSysBench 用十个 Agent 应用和生产 trace 同时刻画模型调用、工具、状态和 orchestration，避免只测纯 LLM decode。它是 workload characterization，不证明十个应用代表所有 Agent；四项 design exploration 只能支持其观测到的压力。
<!-- daily-books-trace:SF-2026-ARXIV-2608-15127:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-22510:start -->
- `SF-2026-ARXIV-2608-22510` — Daily `2026-08-24`；primary `arXiv:2608.22510v1`；Books review `books-review:SF-2026-ARXIV-2608-22510`。

  **已吸收的语义增量：** ClawProBench 要求声明 model+runtime，使用 102 个场景、冻结 holdout、typed trace 与三次运行，试图区分 Agent 能力与 harness/runtime 覆盖。它改进的是评估合同，不是模型智能的独立度量；场景代表性和 evaluator 漏检仍需保留。
<!-- daily-books-trace:SF-2026-ARXIV-2608-22510:end -->

<!-- daily-books-trace:SF-2026-LOCALIZE-DECIDE:start -->
- `SF-2026-LOCALIZE-DECIDE` — Daily `2026-08-27`；primary `arXiv:2608.25824v1`；Books review `books-review:SF-2026-LOCALIZE-DECIDE`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：先用 conformal prediction 产生高概率包含 human-preferred answer 的 shortlist，再在 shortlist 内 calibrated decide-or-abstain；并保留边界：保证依赖 exchangeability 与校准分布；不是模型自知，也不覆盖分布漂移或 judge 攻击。 相邻章节对读：books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L132。Scheduler 处理 resource choice，Monitoring 处理 aggregate signals；calibrated uncertainty guarantee 与 abstention contract 属于 Evaluation。
<!-- daily-books-trace:SF-2026-LOCALIZE-DECIDE:end -->

<!-- daily-books-trace:SF-2026-SKILL-ISSUE:start -->
- `SF-2026-SKILL-ISSUE` — Daily `2026-08-27`；primary `arXiv:2608.25832v1`；Books review `books-review:SF-2026-SKILL-ISSUE`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：同模型 self-play 固定 game/rules/state/action，仅改变双方界面语言并交换角色；另把 interface language 与 reasoning language 分离；并保留边界：仅小模型与八语言；self-play 测相对强弱而非绝对部署质量，translation/tokenization 仍是混杂因素。 相邻章节对读：books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L18。相邻章不定义 counterfactual benchmark distribution；语言变量隔离与结果边界属于 Evaluation。
<!-- daily-books-trace:SF-2026-SKILL-ISSUE:end -->

<!-- daily-books-trace:SF-2026-V-RUBRICS:start -->
- `SF-2026-V-RUBRICS` — Daily `2026-08-27`；primary `arXiv:2608.25580v1`；Books review `books-review:SF-2026-V-RUBRICS`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：把答案拆成 VF/RC/IF atomic rubrics，并在有证据 span 时进行 component-wise、prefix-localized credit assignment；并保留边界：rubric 由 Gemini-3-Pro 标注且继承其偏差；不外推其他模型、领域或无 reference 的开放任务。 相邻章节对读：books/part-06-ai-infrastructure/65-kai-scheduler.md#L48;books/part-06-ai-infrastructure/67-monitoring.md#L18。Scheduler 拥有 placement，Monitoring 拥有 runtime signals；rubric schema、credit assignment 与 evaluator bias 属于 Evaluation。
<!-- daily-books-trace:SF-2026-V-RUBRICS:end -->

<!-- daily-books-trace:SF-2026-PREDICTION-POWERED-EVAL:start -->
- `SF-2026-PREDICTION-POWERED-EVAL` — Daily `2026-08-28`；primary `arXiv:2608.26638v1`；Books review `books-review:SF-2026-PREDICTION-POWERED-EVAL`。

  **已吸收的语义增量：** 补足 bias-corrected population estimate 与区间合同。
<!-- daily-books-trace:SF-2026-PREDICTION-POWERED-EVAL:end -->
