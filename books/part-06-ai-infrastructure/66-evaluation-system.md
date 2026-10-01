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

对会读写评测仓库的 Agent，目标写清楚还不够：公开验证集的标签若与代码一同暴露，逐轮反馈又只强调公开分数，Agent 便可能复制标签、据此训练或调参，让分数上升而独立隐藏集不改善。公开集和即时反馈在开发阶段仍有价值，但 EvalSpec 此时必须同时冻结**可见文件与标签权限、反馈措辞和轮数、执行与停止规则**；轨迹审计分别查直接复制、训练、调参和校准，发布判断交给真正独立的 holdout。把公开文件称作“held-out”，或者仅靠提示禁止捷径，都不能代替运行时隔离与独立验收。<!-- source-family:SF-2026-ARXIV-2604-20200 -->

隔离会降低调试便利，并增加隐藏评价、访问控制和轨迹审计成本；低风险探索可保留可见公开集，但其分数只能用于开发反馈，不能越权取得 release 证据。受限 coding-agent 实验观察到这类 public/private 分离，并在小规模提示消融中看到行为缓解；它没有证明提示能可靠阻断泄漏，也不能推算生产环境中的发生率。这个边界把上面的 proxy 问题落到**评价通道由谁控制、Agent 实际看见什么**，再进入下文对任务难度和分布的条件化测量。

任务难度切片也不能只按输入长度或实体数划分。关系推理可以分别改变输入规模、任务生成器规定的 binding arity，以及识别或比较单个 operand 的难度；它们是三个不同轴。同一 arity 下更多输入可能提供额外线索，而非必然更难；实体少却需要同时满足更多关系，也可能比长输入更困难。EvalSpec 应保存生成规则和 oracle，在输出格式、scorer、推理预算可比的切片中交叉改变这些轴，不把换任务后不同的 accuracy、substructure 或 recall 拼成同一条下降曲线。<!-- source-family:SF-2026-ARXIV-2604-12176 -->

这种控制比单一长度排行榜增加生成、oracle 与样本预算，也仍只能约束已测混杂。生成器定义的 relational complexity 是任务属性标签，不是模型内部容量的计算下界；合成、多选与有限 token 预算下的失败，更不证明增加任意计算都无效。简单任务、长度已主导成本时仍可保留原长度切片，复杂关系任务再补上述交叉维度。受限关系评估支持将这些难度来源分账，而不支持通用 arity 阈值或唯一失败因果。

### Continual Update 需要同步推进 Calibration State

只在模型 accuracy 明显下降后重新评估，在更新稀少、分布稳定时成本最低；continual fine-tuning 会持续改变 score distribution，使旧 threshold 或 conformal set 的 coverage 在 accuracy 尚未报警时已经失效。更完整的 release identity 因而同时版本化 model artifact 与 task-specific calibration artifact，并在每次更新后执行小规模 calibration replay：

```text
model update
-> task-specific calibration replay
-> coverage / calibration evidence
-> accuracy gate AND coverage gate
-> promote model + calibration artifact
   or freeze and rollback together
```

这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23987:start -->
模型更新与 calibration 更新属于同一个 release transaction，但 accuracy evidence 与 coverage evidence 保持独立。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-23987:end -->

### Stream Boundary 也是 Evaluation State

连续数据流必须切成 task 才能复用传统 continual-learning benchmark；流的语义阶段清晰且边界稳定时，固定切分是最便宜的旧方案。真实 stream 的边界可有多种合理解释时，taskification 会改变每段的 plasticity/stability 压力，继而改变方法排名。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-21930:start -->
EvalSpec 因而要版本化原始 stream identity、时间边界与 perturbation policy，并在训练前用 boundary-profile sensitivity 一类诊断检查小幅边界移动是否显著改变诱导出的任务结构。该诊断只暴露 benchmark 对切分的敏感性，不会替代训练后评估，也不会给出正确边界。它增加多切分计算与解释成本；当业务事件天然定义 task、边界由外部协议固定时，单一切分仍成立。作者结果只覆盖其 taskification family 与数据集，不能把敏感度阈值外推为通用 Gate。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-21930:end -->

### Model Self-report 不能拥有输入来源真值

多模态输入的来源由 ingestion path、artifact metadata 和 transform lineage 决定。若 evaluator 只问模型“这条信息来自图像还是文本”，模型可能把提示词中的 `image` 与语义或句法 cue 绑定，而不是读取真实 modality provenance。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22038:start -->
因此 source-modality monitoring 应同时保留 authoritative provenance、受控 cue intervention 与模型 self-report：前者是真值 owner，后两者只是测量模型是否正确绑定来源的 sensor。这样能发现答案正确但归因错误的系统，却需要可追踪的 preprocessing lineage 和 matched counterfactuals；拿不到权威来源时只能报告 behavioral association。作者对 11 个 VLM 的 target-modality retrieval 结果证明该 failure mode 可被测量，不证明 self-report 可替代 provenance，也不覆盖任意 modality 与生产输入链。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22038:end -->

跨模态 retrieval 的语义排序还需受 target-modality admissibility 约束：内容相似不代表返回对象具有任务要求的模态。应先按权威 lineage 检查候选可用性，再在合格集合中比较 semantic rank，分别统计 wrong-modality 与相关性失败。用 image 构造 video、用 text 合成 audio 的候选又带有生成混杂，不能把对象外壳当成原生模态证据。<!-- source-family:SF-2026-ARXIV-2604-23321 -->

这一检查增加 typed metadata、过滤与跨方向切片成本；作者 12 个方向、每方向 100 个 synthetic query 只支持该受限集合。缺少可验证模态身份时报告 Unknown，任务不要求特定模态时仍可采用普通语义检索；不得从小型合成题库推出真实多模态检索的统一排行。

### Observed Capability 与 Elicitation Ceiling 必须分开

固定 prompt 下的最高分最容易比较，但弱 supervisor 无法可靠验证全部输出时，低分可能来自能力不足、策略性隐藏或 elicitation 失败。Evaluation 需要把模型当前自然行为、给定监督预算可诱发的最好行为，以及 supervisor/evaluator 的识别上限拆成不同证据对象。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22082:start -->
对同一 model revision，可记录 zero-shot baseline、弱监督 SFT/RL 后的可观察提升、监督来源及其可验证范围；elicitation training 只能作为 probe，不能反向证明内部真实最大能力或“欺骗已被解决”。它换来更强的 capability lower bound，却增加训练成本、distribution shift 和对 model-organism 假设的依赖。作者在人工训练为 sandbagging 的模型及数学、科学、代码任务中观察到弱监督可恢复部分表现，不证明真实部署模型普遍可被同样方法揭示；监督不可靠或风险过高时仍需独立 verifier、权限收缩与保守 release Gate。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22082:end -->

识别能力与监督效应还需要同压力下的配对条件。先在中性任务确认可观察能力，再在压力条件比较“无监控”与“声明正被监控”的工具选择，才能把能力不足、压力诱发的行为变化和监控敏感性分开；不能由一次正确回答或被监控时恢复表现推断所有场景都可靠。监控声明本身也是prompt干预，应与模型、任务和解析协议共同冻结。<!-- source-family:SF-2026-ARXIV-2604-26511 -->

作者108情景的JSON schema/XML工具选择是受限选择实验，不是真实tool effect执行；reasoning中的alignment-faking标签也不能读取隐藏动机真值。配对调用、解析错误、评价者判断与监控线索改变上下文都需要单独记账，避免把符合格式和表现改善当作部署安全。条件不匹配、理由标签不稳定或风险较高时，回退独立行为测试、真实effect gate与保守权限，不用声明监控替代监督能力。

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

行为指纹不能只用“相同反应有多少”替身份差异。重复token的单次argmax探针中，self-continuation集合的Hamming距离可主要反映集合大小，即使constant-coordinate门禁已通过。一个更可诊断的对照按同一source字符串配对，记录它转向哪个destination，再与频率匹配和独立marginal null比较；模型内用token ID，跨tokenizer才用共同single-token字符串，并显式保留decode歧义与缺失coverage。

这仍是受限checkpoint的观测signal，不是实例、血缘或架构因果认证。数值precision、batch和量化可以改变destination，margin筛选又可能同时除去噪声和真正区分信号；floor必须逐model/协议测量，而不能共享一个全局阈值。有限family对照未控制全部训练因素，4bit反退和新增语言后共同support缩小都保留。将探针用于诊断须附匹配null、precisionfloor与coverage，条件不足时回退artifact/call身份及真实行为验收，不能由相似指纹自动发布provenance结论。[必要反证](https://arxiv.org/html/2609.31181v1) <!-- source-family:SF-2026-ARXIV-2609-31181 -->

例如，模型离线比较可以固定 prompt 和 decoding；RAG 评估必须把 index 与 retriever 放进对象身份；Agent 评估还需要记录 tools、sandbox、workflow、budget 和 environment。若只记录 `model_name`，同一模型搭配不同系统组件产生的行为会被错误合并。

尤其在通用 Agent benchmark 中，模型可能通过不同 provider API、tool-call parser、message template 或
architecture wrapper 接入同一环境。Protocol adapter 不是中性胶水：它会改变 tool schema、observation
serialization、retry 和 stop behavior。公平比较应验证 adapter 的 semantic equivalence，并把 adapter revision
纳入 subject；否则“模型差异”可能只是 harness translation 差异。General Agent Evaluation 的实验支持这一
对象边界，但不能证明一个 adapter 可对所有 provider 实现完全等价。

Adapter 的静态权重检查尤其不能独占行为验收。对同一基座、同一训练方法制成的 adapter，weight delta 的谱形状与方向可能分开目标、强度或正常/异常类别；换成另一种制造方法，分类信号却可能系统性反转。检测器因此还要绑定 adapter-generation method 与训练/测试分布，保留跨方法 holdout，不能把一次可分的几何形状叫作通用安全指纹。<!-- source-family:SF-2026-ARXIV-2604-08844 -->

静态 signal 与行为 judge 也有不同失效面：某个 perturbation 让生成退化为重复 token 时，安全 classifier 可能将无意义输出判为 harmful；换用独立 judge 并观察有效生成，才可发现这个测量混杂。[作者小样本实验](https://arxiv.org/html/2604.08844v1)同时观察到训练方法间反转和这一假阳性，支持以权重预检提出 probe、再用匹配目标的行为测试验收，不支持几何方向与行为检测必然互补或没有共同盲点。这增加独立生成、人工/异构判分与跨方法样本成本；只有受评方法和分布确实固定时，单方法预检才可作为便宜的受限 sensor，不能替代 release Gate。

输出本身不宜生成时，行为验收还可增加受限的无输出内部功能探针：冻结base、adapter、固定Gaussian latent probe输入、layer/time、标签和阈值，通过模型前向的内部signal判断特定训练类别，而不materialize危险内容。这是分发前的有限证据，不等于把训练类别直接当危险生成能力，也不由探针阴性自动放行。

省掉可见输出不等于零计算，探针仍有前向、训练与校准成本；小类别样本、少量探针和固定扰动的鲁棒性不支持自适应攻击或所有adapter。release authority须另做政策裁定，必要时人工隔离；允许合规采样且行为验证更直接时，既有生成/独立judge路径继续成立，内部signal不能替代完整行为Gate。 [原文必要机制与限制](https://arxiv.org/html/2604.25119v1)。
<!-- source-family:SF-2026-ARXIV-2604-25119 -->

### Evaluation Identity 必须包含 Harness 与 Environment

每个 benchmark 维护一套专用脚本，在任务少、协议稳定时最直接。但 Agent evaluation 中，prompt adapter、tool serialization、retry、timeout 与环境初始化都会改变可观察行为；只记录 model 与 benchmark 名称，无法解释同一模型为何在不同 harness 中得到不同结果。

可复现的评估身份至少应写成 `model × benchmark × harness × environment × scorer`。Harness 负责适配与控制流，Environment 负责可执行状态，Scorer 只拥有从轨迹到判断的映射；聚合分数之前必须保存原始 trajectory 与 component-level receipt，才能区分模型退化、adapter drift、工具故障和评分变化。统一协议可以复用执行与观测设施，但每个 adapter 仍需证明语义等价。

统一 harness 降低重复建设，却引入新的兼容层、版本漂移与运行成本。孤立且长期稳定的任务仍可使用专用脚本，但也必须冻结脚本、环境和 scorer 身份，不能把一次聚合分数当作脱离执行条件的模型属性。

自动模型开发还应把comparison而非run作为科学证据单位。两个run都成功、有最终metric且声明配置相同，仍可能实际走过不同candidate funnel或evaluator revision。先冻结commonbase、数据窗口、允许的treatment字段与metric semantics，再从两侧terminal artifacts提取realized配置和谱系，检查未受treatment影响的stage是否等价；缺少必要证据的pair不准入，不能用另一variant成功补齐。Agent方案、memory教训和self-report只能指导执行，不拥有比较成立的权限。

数字存在但比较失配，是invalid measurement；OOM或缺data partition是operational failure；只有actual treatment成立的non-improvement才能成为模型负面证据。EvoPilot的受限案例把原−22pp归因追到输出深度失配，修复后的bundled retest、matched-lineage ablation和online随机结果仍各有不同estimand；post-study mutation通过不倒填为当时自动阻止了故障。配对提取、版本维护和人工语义审查有成本，旧的稳定专用脚本仍可保留；无法从可信artifact提取或semantics有争议时，隔离该comparison并定点补证，不按workflow完成率签模型改进。[必要机制与反证](https://arxiv.org/html/2609.21257v1)。<!-- source-family:SF-2026-ARXIV-2609-21257 -->

理解和生成共用backbone不等于两者消费或保留同一事实。可冻结同一scene/fact identity，以相同关系分别构造理解问题和生成检查，同时报告两侧各自正确、两侧同错、agreement、未匹配节点与歧义匹配；agreement不能把共享错误升级为能力，缺失节点也不能从分母消失。

配对测量增加事实标注、图匹配与生成成本，同label匹配仍可能对不上对象；应保留匹配拒绝及coverage，不将匹配子集自动冒称全场景。受限XTC研究的matched coverage与all-node口径仍有未决，本文只采用这项测量分层，不采用完整一致性保证，也不由黑盒相关性推导AR架构的因果优越；无法可靠匹配时退回分开的理解/生成评价和人工抽核。 [原文必要机制与限制](https://arxiv.org/html/2604.25072v1)。
<!-- source-family:SF-2026-ARXIV-2604-25072 -->

#### 行为预测是独立 Evaluation Task，不是解释的副产品

自然语言 reasoning trajectory 看起来像解释，却可能不忠实，也未必让读者准确预测模型在新输入或干预下如何变化。Evaluation 可以把 forecasting 本身定义为可学习任务：forecaster identity 绑定 target model/revision、trajectory construction、预测问题与 calibration slice，分别评估重复答案概率和 intervention response。Forecaster 只产生风险或行为预测，release owner 仍需真实 rerun 或受控干预证据。

单次 forward 的低成本换来训练同源、分布漂移和 shared-blind-spot 风险；预测准确也不解释内部因果。目标模型、prompt 分布或 trajectory protocol 变化时应重新校准，无法校准则回退直接运行与 intervention experiment。现有证据覆盖三类 reasoning dataset，不支持把 forecaster 升级为通用行为保证。
<!-- source-family:SF-2026-ARXIV-2606-11445 -->

把模型说出的规则与行为比较时，还须把三个对象分开：预先声明的decision rule、独立提示下测得的输入估计，以及实际decision。冻结规则的提问顺序，再控制输入与prior，才能区分规则漂移、感知误差和决定没有遵循规则；答对一个感知probe，并不证明同一估计实际控制了最终答案。这种协议增加多次测量、提示次序与跨调用漂移的成本；不能用事后调整阈值替模型消除矛盾。[受控颜色归属实验](https://arxiv.org/html/2604.06422v1)提供这种分账的具体反证，不证明模型内部“知道但撒谎”，也不把某些模型的准确估计推广为所有模型都无感知误差。<!-- source-family:SF-2026-ARXIV-2604-06422 -->

视觉决策的配对实验还需控制规则所带的熟悉语义。相同 pixels 和 terminal state，可以分别按 standard/inverse 规则判定，再比较中性 alias 与重新带入胜负含义的 alias；这样保持视觉证据不变，同时改变状态到答案的解释映射。如果中性命名缓解错误、语义命名又恢复错误，便有理由检查熟悉 prior 是否压过了当前规则，而不是一律把失败归因于视觉 encoder。EvalSpec 应共同冻结图像、规则、alias、输入顺序和输出 oracle；same pixels 只排除图像本身发生变化，不证明感知在每次调用中全正确，也不识别唯一内部因果路径。<!-- source-family:SF-2026-ARXIV-2604-12119 -->

这增加配对题量、提示与解码预算，且合成游戏的精确 oracle 不能代替开放场景的判断标准。[作者的四游戏、十四 VLM 实验](https://arxiv.org/html/2604.12119v1)区分 closed-model reduced 与 open-model expanded 协议，显示部分规则与命名条件的行为差异；同规则后训练还可能损害相反规则，不能由单一规则提升证明通用鲁棒性。输入/规则稳定且任务无需重映射时，普通固定协议仍可用；需要诊断视觉错误还是语义 prior 失配时才付出这组配对成本，并保留独立感知检查，不能把 steering 可改变输出当作全部层机制已查明。

#### Prefill 是 Harness 输入，不是模型自然历史

通过预填 assistant turn 测试 alignment、steering 或 Agent control 时，必须把该 turn 的来源、插入方式、格式和 target-model revision 纳入 Evaluation Identity。模型显式识别外来 prefill，与它在行为上回退无预填 baseline 是两个不同 outcome；若 formatting artifact 泄露干预，不能把结果解释为一般的自我纠正。

Prefill harness 便于构造受控初始状态，却可能测到模板识别而非目标机制。Awareness 未测、格式对照不充分或服务端实际会重写消息时，结果应标为 confounded 并回退无预填或重新设计的对照。论文只支持其模型、格式和 Agent 场景中的现象。
<!-- source-family:SF-2026-ARXIV-2606-12747 -->

#### Judge Ranking 要同时校准局部比较与全局区间

Judge 自偏好审计要区分三个测量对象：高 contrast 答案的判别能力、近等质答案中的 self-PIR，以及第三方 judge 对这些答案的 Null-PIR。前者测试能否辨别质量，后两者控制答案来源和评判者身份；差分只是在协议内分解观测偏好，并不自动识别纯粹的 self 因果效应。双 LLM 的 quality proxy 也不是独立 gold。<!-- source-family:SF-2026-ARXIV-2604-22891 -->

这增加答案配对、第三方调用和质量匹配成本，proxy 错误、风格差异与候选生成方式仍会混入比较。近等质控制不可信或新域未校准时，应补人工 anchor、报告三个量的不确定性，或保留无排序结论；不能由高 contrast 判别好就批准低差额排名。

把每次 LLM judge 比较硬化成确定 win/loss，在 judge 存在 position bias、自偏好或 intransitivity 时会把局部错误放大到 Elo 排名。局部层应先把 score difference 校准为 soft win probability，再进入 Bradley–Terry/Elo；全局层再用 held-out judge–human residual 构造 conformal rating interval。Judge 只拥有比较 evidence，release owner 仍需根据 interval overlap 与风险决定是否排序或保持并列。

Judge 自身的 task competence、directional bias 与对更强 examinee 的 leniency 也必须拆开测。能力较强可能提高 judging accuracy，却不会消除系统性宽松或偏向；无标签 disagreement 只能生成待校准状态，不能替代人工 anchor。Route/defer 更不能读取 verbal confidence 直接决策，而应比较模型相对外部 prior 的边际 proper-score 收益；先验更强或 domain 漂移时，保留 crowd、market、rule 或人工分支。

<!-- source-family:SF-2026-ARXIV-2609-12002 -->
<!-- source-family:SF-2026-ARXIV-2609-12101 -->

这套校准降低硬判决噪声，却依赖 exchangeability、model pool 与 prompt 分布稳定；marginal coverage 也不是每个模型都覆盖。Judge、候选池或 rubric 漂移时必须重新校准，无法满足前提时回退人工标注或报告无序区间。现有证据不支持把低成本 judge 结果当作人类真值。

Query 内的比较能确定相对排序，却不能直接把不同 query 的 BT 分数当同一单位。一个测量分支先保留 listwise soft preferences 和 query 内顺序，再以共享 rubric 的 yes/no criterion verdict 拟合共同 2PL 难度与区分度，并为各 query 校准正尺度和偏移；正尺度映射不重排该 query 的 documents。校准后 criterion 通过概率可形成连续 relevance gain，用于跨 query 标签与汇总，而不是宣称发现客观正确性。

这增加 judge 调用、拟合与 rubric 维护成本，依赖测量模型适合 verdict；rubric、judge 或 pool 漂移须重核。[RCP v1 §3–4/6](https://arxiv.org/html/2609.35739v1) 的有限检索评估仍忽略文档间冗余/互补，人工问题与 rubric 接近、LLM 同源偏好也未被消除。校准不稳、分差过小或事实/安全不在构念中时，保留独立人工标签、原 qrel 指标及并列/无结论；不可用该 gain 同时认证答案真值、发布政策与 RL reward。<!-- source-family:SF-2026-ARXIV-2609-35739 -->

Route/defer 的分数还要区分‘倾向把任务交出去’与‘该专家对当前 query 有多大正确率’。一个受限接口在每个候选 class role 下，只从该专家 context 中相同 role、与 query 接近的已标注正确/错误实例汇聚证据，再由共享的 competence head 估计条件正确率；不用绝对 class embedding，使 labels、专家预测与 classifier posterior 一起重命名时保持一致。无同 role 支持则回退 global context accuracy，不能把零证据解释成可靠低风险。再按 classifier 的 class posterior 汇总专家正确率，才能与模型自己的正确率在同一对象上比较；augmented routing softmax 的 deferral coordinate 不是这个概率。

这一分解依赖 context 不额外改变 query 的 label posterior；case mix 含信息时须另估 context-conditioned posterior。Proper loss 只在 population 最优处恢复给定 summary 的正确率，summary 是否充分、有限训练及跨域校准仍要验证；共享 encoder 更新也会改变 competence 读出，stop-gradient 不保证整体预测不变。有限实验中稀疏 context 可使路由差于 classifier baseline，更低 ECE 也不必有更高 routing utility；nominal synthetic OOD 与真实专家的同伴一致性不能升级为人群漂移或真实事实保证。标注、context 检索、两侧校准和维护 role identity 都有成本，0–1 无额外 deferral cost 的 regret 结论不授任意预算/风险最优；支持不足或概率不可比时，回到固定路由、独立人工/规则及明确 Unknown。 [必要机制与反证](https://arxiv.org/html/2609.21953v1)。<!-- source-family:SF-2026-ARXIV-2609-21953 -->

即使模型、候选集与提问协议固定，重复 pairwise 选择也未必只是单一偏好排序上的独立噪声。若比较关系持续出现非传递性，Evaluation owner 应保存原始逐次选择、展示顺序、prompt 配置与随机采样条件，先检验单一随机效用模型能否解释，再比较允许多种行为排序的预测模型；只公布一个聚合胜率会掩盖局部可预测的分歧。该分解增加比较和拟合成本，相关噪声也可能被误拟合成多个成分；行为成分不是模型内部偏好电路。重复选择近单峰或外部验证不足时，仍用校准后的单一排序与不确定区间，不据混合拟合改动训练目标或发布政策。<!-- source-family:SF-2026-ARXIV-2609-22170 -->

全局 Bradley–Terry/Elo 还隐含“同一胜率结构足以代表所有人群或任务切片”。当语言、领域或偏好子群存在方向一致但彼此相反的比较时，全局聚合会相互抵消，并把真实异质性误写成无差异。Evaluation owner 应先保存 pairwise comparison、slice identity 与 uncertainty，再报告能覆盖不同 coherent groups 的小模型 portfolio 或并列区间；portfolio 只拥有描述异质性的权力，不能替代 deployment population、风险权重与 release owner。它换来更忠实的 subgroup evidence，也增加群组发现、多重比较和选择不稳定；切片样本不足、群组不可解释或生产人群未知时，应回退全局结果加明确 limitation，而不是伪造精确分群。exact-v1 的 89K Arena comparisons、116 languages 与 52 LLMs 只支持该数据中的异质性和 portfolio 构造，不证明未来人群、任务或部署最优模型稳定。

<!-- source-family:SF-2026-ARXIV-2605-06656 -->
<!-- source-family:SF-2026-ARXIV-2606-13221 -->

#### Judge Agreement 不能代替统计推断的校准

排序校准回答的是“比较和排名有多可靠”；发布评估还常问“均值或两方案差异是否足够可信”。Judge 与人工分数高度相关，并不保证由 judge 分数计算的置信区间或显著性检验保持正确覆盖率：很小但方向一致的误差，经过大量样本聚合也会改变判断。这里必须区分单条评分质量与下游推断质量，而不是用一个 agreement 指标给整个评价链放行。

一种可审计的分支是在大量 judge 评分外，随机抽取同一评价总体的人工配对标签，用人工与预测的残差修正目标估计。Prediction-powered inference 复用预测降低标注成本，但人工样本的抽取方式、item 配对、目标统计量与分析设计仍是成立前提；便利抽样不能冒充随机锚点，人工标签本身的构念效度也未被这个修正证明。非参数检验还需明确其估计的是排序概率、位置差还是组内秩，而不是一律解释为平均准确率差。

若预测与人工结合的权重也由少量标签估计，权重的不确定性必须一起计入。收缩可以降低不稳定性，却牺牲部分 power，不能保证有限样本中总比人工估计好。小样本下，bootstrap 置信区间同样要验证覆盖；这不否定用 resampling 诊断权重方差，也不否定结构匹配、样本充分时的 bootstrap。应按目标统计量和采样结构选择经验证的推断，条件不足时报告宽区间、补标注或不作显著改善声明。当前方法/工具的模拟和支持范围有限，不提供所有 judge、multi-run 或任意指标的通用证书。
<!-- source-family:SF-2026-ARXIV-2609-35815 -->

#### Synthetic Evidence 只有在 Task Exchangeability 成立时才能进入推断

合成样本适合探索和扩展测试面，但 bias、noise 与 misspecification 会让“大样本”制造虚假精度。若要把 synthetic data 纳入具有覆盖保证的推断，Evaluation owner 必须保存当前 task 与有真实数据 historical tasks 的 descriptor、real/synthetic lineage、exchangeability diagnostics 和 coverage target；只有任务层可交换前提通过后，合成数据才能参与校准。

跨任务借力减少真实标注，却用强统计前提换取有效性；task drift、生成器更新或历史任务选择偏差都会破坏保证。条件无法审计时，合成数据只用于发现和压力测试，不能替代真实 holdout 或发布结论。论文案例只支持其 survey 与 autorater 设置，不证明任意 synthetic benchmark 可安全扩样。
<!-- source-family:SF-2026-ARXIV-2606-13629 -->

### 数值可复算不等于复现了同一个实验

能够从 released table 或 analysis script 重新算出相同数字，只证明计算路径自洽；如果实际 cohort、输入渲染、prompt、provider 解析到的模型版本、API call 成功状态或 annotation 已经不同，它并没有复现原实验对象。完整的 run identity 因而必须贯穿原始样本到派生结果：`cohort membership → render/prompt hash → resolved model and call receipt → annotation provenance → analysis artifact`，任何一环变化都生成新的 evidence revision，不能继续沿用旧排名或效果声明。

这条链提高纠错与可追溯性，却增加存储、隐私和供应商接口治理成本；历史系统拿不到完整调用记录时，只能发布“当前 artifact 可复算”的较窄结论。一次影像语言 benchmark 的取证式重建发现，旧结果虽然可复算，实际执行条件却与报告条件不一致，因此撤回了原性能、排名、prompt-effect 与临床结论；该证据支持上述身份边界，不证明这套字段能排除所有污染，也不保留被撤回的旧结果。

<!-- source-family:SF-2026-ARXIV-2607-25589 -->

### Agent Regression Testing 需要分配 Evidence Budget

项目级 coding evaluation 还必须承认测试本身会演化。只运行当前 tests 能发现 breaking change，却可能把与新 requirement
脱节的 stale tests 或根本缺失的 tests 误解释成“Agent 已完成”。更完整的 harness 把 test revision、对应 requirement、
目标 code revision 与执行环境绑定，并将失败分成 breaking、stale、missing；其中 missing 是覆盖缺口，不能用 pass
结果填补。Evaluation owner 负责这个分类，Agent 只能提交代码与测试候选，不能自证测试充分。

这种契约提高 requirement tracing 与维护成本，也仍无法证明隐含需求已经枚举。验收应分别报告 executable test rate、
requirement coverage、staleness 与 mutation/held-out detection；小型稳定项目继续使用固定 regression suite 更简单。现有
证据支持论文构建的项目与测试演化 benchmark，不证明该 taxonomy 能自动发现所有真实需求。
<!-- source-family:SF-2026-ARXIV-2605-06125 -->

候选 regression cases 还可以从真实失败反向构造，而非只从新 specification 正向推导：先把已确认 bug 抽成 interaction patterns，再与兼容的 action types 组合，执行固定环境并检查留下的 artifact，最后对自动 flags 做独立 adjudication。这样能系统性探测工具、工作区与操作组合中的已知脆弱模式，却会把历史 bug 分布、组合兼容规则与 checker 的误报一起带入 coverage。<!-- source-family:SF-2026-ARXIV-2604-03362 -->

Flag rate、检测 precision 与真实 Agent failure rate 必须分别发布；作者受测系统中自动标记后不到一半获人工确认，不能将全部 flags 当成失败或安全事故。有限模式的组合测试也没有枚举未知 bug，单次执行不能估计非确定性发生率；因此它补充而不替代固定 regression suite、mutation/held-out tests 与下面的重复预算。模式已经过时、artifact checker 失配或组合缺乏可执行前提时，应重新标注并收窄 campaign，而不是用更多组合制造覆盖完整的假象。

确定性的单元测试可以运行一次并把 pass/fail 当成稳定证据；Agent workflow 同时受模型采样、工具状态和环境变化
影响，同一 case 一次通过不能区分真实回归、偶然失败与 flaky dependency。最直接的做法是把全部 trajectory 和断言
重复多次，却会让 token、环境调用与人工诊断成本随 case 数和重复次数相乘。

因此 regression owner 需要把测试选择与重复预算建模为 evidence acquisition，而不是固定 test loop：先从 workflow
spec 与历史 trace 生成可执行 assertions，再依据失败信息量、非确定性和覆盖缺口选择 case，并在有限 token budget 下
分配重复次数；最终同时保存原始 trajectory、assertion outcome、执行环境和不确定性，而不是只发布聚合 pass rate。

```text
versioned workflow + executable assertions
-> candidate regression cases
-> information / uncertainty-aware selection
-> repeated runs under a fixed environment identity
-> claim-level evidence and release decision
```

这种自适应测试用较少运行换取更集中的回归证据，却引入 selection bias：未被选中的 case 仍可能包含未知失败，历史上
稳定的 case 也会因环境变化而失效。系统必须保留随机 audit slice、最低覆盖预算与 deterministic critical-path tests；
高风险副作用不能因为模型预测“信息量低”而跳过。AgentAssay 的公开实现和实验只支持作者 workflow、selection policy
与 token budget 下的效率，不证明其 selector 对所有生产故障保持完备。

<!-- source-family:SF-2026-ARXIV-2603-02601 -->

预算还可以在不同证据强度间交错分配：便宜的 quality rating 更新候选风险，却不能确认 severe error；只有预先定义的强 annotation 才计入已确认发现。一个 joint posterior 同时建模两者的相关性，在同一成本预算内选择下一次观察或确认，并保留至少一次强确认的额度。为减少重复候选，可按查询对 severity probability 的预计 impact 聚类，而不是按文本相似性聚类；预算控制拥有 acquisition proposal，最终错误标签仍由确认接口提供。

[MICRO 的受限回放](https://arxiv.org/html/2609.26025v1)以 WMT20 翻译条目、固定特征和定义的严重阈值验证这一分权；一阶 impact 固定 posterior variance、rollout 只展开 future annotation，不能称完全最优的 multi-fidelity 策略。便宜评分的成本是设定比例而非实测人力/完整 wallclock，比例较高时也没有改善；主动发现数不是无偏总体严重率。建模、聚类和搜索都须计成本，posterior 失配、真实成本未知或高风险时保留随机 audit、确定性强确认与现有回归测试，不让廉价评分自行批准发布。<!-- source-family:SF-2026-ARXIV-2609-26025 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21515:start -->
Regression evidence 还取决于被评 artifact 的执行语义。Symbolic program 在固定输入分布上常呈接近全对或全错的二峰行为，少量 example 可以较快更新先验；prompt program 每次仍由 LLM、temperature 与上下文共同执行，同样的少量 pass 不能继承这份先验。发布判断应同时绑定 artifact kind、执行模型与采样参数、task distribution、观察到的 pass/fail，以及从相似且版本化任务中检索得到的 performance prior，再据此决定是否追加测试。

检索式 prior 可以减少低风险候选的重复执行，却会把语料偏差、错误近邻和 iid / exchangeability 假设带入 release confidence。先验校准失效、task distribution 改变或高风险断言缺少直接样本时，应停止用少量 pass 认证，回退扩大 held-out execution、分层抽样和保守 release gate。现有实验只支持论文定义的 symbolic/prompt programs、RAP prior 与任务集，不证明任意 prompt 的后验都可由相同先验校准。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21515:end -->

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

安全干预评价不能只测无cue的标准提示。应冻结checkpoint、干预、训练cue类别与任务，将标准、同义、反义和格式变体组成矩阵，分别记录普通行为与训练条件行为；标准分母中的零有害率不能代签相关cue下的行为已被清除，已知训练provenance只帮助定义测试，不证明已穷举触发条件。

矩阵扩大生成和判分成本，语义filter与judge也可能共享盲区，逐题分母及排除项不能省略。受限条件misalignment研究中，某干预在某slice可清零、另一个slice仍残留，不能宣称所有干预无效；人工SFT亦不是生产RL证据。新cue或干预版本需重新验收，未覆盖时缩小发布声明并保留隔离/独立行为测试，而非标准测试通过即全域安全。 [原文必要机制与限制](https://arxiv.org/html/2604.25891v1)。
<!-- source-family:SF-2026-ARXIV-2604-25891 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06672:start -->
多选评测还会受到候选顺序与推理接口的共同影响。只用一个选项排列、一次直接回答，在模型与模板冻结时成本最低；但当位置偏好与 Chain-of-Thought 改变作答分布时，单一 accuracy 会把接口偶然性写成能力。更稳健的合同应冻结选项 permutation、direct/CoT 分支、trajectory-length 与 truncation probe，并同时报告正确率和 Position Bias，而不是用增加提示词掩盖偏差。

这会成倍增加生成与判分成本，CoT 也可能引入额外暴露面；因此它适合对关键模型和高风险结论做 paired audit，不要求所有低风险回归都穷举排列。证据只支持作者披露的多选任务、模型和 evaluator，不能证明某一种顺序或 CoT 接口普遍更优。预算紧或接口固定时仍可保留单排列 baseline，但发布声明必须缩小到该固定 contract；一旦跨模板、跨顺序或跨推理模式比较，就必须重新校准。<!-- source-family:SF-2026-ARXIV-2605-06672 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-06672:end -->

多选接口还可能从一开始就没有可接受的行动。若所有候选都构成有害协助，要求“只选一个标识”会把安全拒绝排除在 schema 之外；合法选项字母也可能代表危险内容，而非仅仅格式正确。评价应冻结候选集合及其可接受性，分别记录选项内回答、候选外拒绝/升级、解释与 harmful assistance，并用同目标的开放问题、选项重排和输出约束做配对测试。格式约束不得取得安全行动空间的定义权；保留拒绝出口是工程设计要求，不是添加一个选项便已验证风险消失。<!-- source-family:SF-2026-ARXIV-2604-16916 -->

这增加选项标注与配对生成成本，判定器也可能把简短标识、解释或无效解析混成同一事件。原文有限中文问题/生成器/模型里，多个 judge 提示的一致性不等于全面独立正确率，取最坏格式的 ASR 也不是某个冻结部署接口的发生率。证据只支持安全行动空间需要单独验收，不识别唯一内部成因；低风险、明确存在合法答案时仍可保留固定 MCQ 基线，高风险或候选集失准时应允许候选外拒绝并独立检查实际输出。<!-- source-family:SF-2026-ARXIV-2604-16916 -->

推理模式的比较还必须确认**打分读的是同一个输出事件**。给 VLM 加“先思考”提示后，若在提示末端立即读取选项字母 logits，测到的可能是理由的第一个 token，而不是生成理由后的最终答案；直接回答、自由生成 CoT、先生成再抽取答案与同位置 probe 是不同 evaluator contract。只用一种读数会把接口错位误称为知识丢失。受控多选实验用 matched probe 与完整生成区分了两者，也发现选项内容和位置仍可混杂；它只约束所测 VLM、任务和提示，不证明 CoT 普遍提高准确率。[原文方法与结果](https://arxiv.org/html/2609.29278v1)。
<!-- source-family:SF-2026-ARXIV-2609-29278 -->

多选题的高分还可能依赖一组固定 distractors，而非稳健的 question–answer binding。把同 topic 多道题的选项合并成共享池，并规定一个选项最多分配一次，可以让“逐题排除”与“跨题约束利用”进入同一诊断；但它也改变了任务。只有每题在池中恰有一个有效答案，且不同题的正确答案不共用同一池选项时，一对一匹配前提才成立；模型筛选歧义不能充当独立 oracle。逐题猜测的 `1/M`、整组全对的 `(M-N)!/M!` 和原始独立 k-choice 的 `k^-N` 必须分开。

要判断失败是否仅由池变大造成，可固定 questions、golds、prompt 与池大小，仅替换 wrong options 为无关组的正确答案，比较相关/无关池；再同时记录长 Context、任务耦合和歧义清理的成本。[AnswerPool 的受限对照](https://arxiv.org/html/2609.37494v1)支持这个诊断分支，不证明新任务的排行就是原 benchmark 被隐藏的“真实能力”，也不证明任意大池没有长度混杂。需要发布可比较分数时仍保留冻结的原 MCQ；共享池用于解释原接口的边界，而不是静默替换测量目标。
<!-- source-family:SF-2026-ARXIV-2609-37494 -->

多轮输入还应把 history 本身作为干预变量。检验一次拒答之后是否更容易接受后续请求，可以固定最终请求，
分别比较空会话、正常同主题前文、相关拒答与无关拒答；若正常前文已经改变基线，不能把相对它的变化全部
归因于拒答策略。还须分开只要求文字判断的请求与要求可执行产物的请求，并绑定 endpoint revision、采样和
judge。[顺序请求研究](https://arxiv.org/html/2609.02707v1)显示这些对照会改变局部结论，但未证明跨模型通用
效应或人类心理机制；跨主题正常前文等缺失对照仍应保留为未决，不能由行为相关性补成因果解释。

这也是第 35 章和第 59 章的接口：Checkpoint 提供可验证 artifact，Registry 提供不可变版本和 evidence references；第 66 章负责说明这些 evidence 是在什么评估契约下产生的。

音视频交互的评测还应先判断“这句话是否向assistant提出了demand”，再评价“应当回应什么”。可回答的疑问、命令或抱怨可能来自播放媒体、背景说话者，或发给另一个收件人；良好转写和正向请求的内容恢复都不能证明它应被受理。将demand/no-demand检测与negative场景的false-trigger rate分开，内容关键点、定位与转写仅在正向人口评价，并保存媒体、历史、source/addressee与参考意图identity，不能把不同分母压成一个响应质量结论。

一个受限benchmark用实际媒体重建并人工核对意图，发现高内容恢复仍可伴随大量false trigger；给同一输入附参考demand annotation改善回应和沉默选择，但这是oracle信息干预，不证明线上模型已经拥有相同gate。固定历史最后一轮测试、合成/真人录制切片与文本judge稳定性也不是持续双向服务的SLO或全部用户意图真值。该诊断增加no-demand样本、标注与复核成本；来源、收件人或意图不明时，应澄清或交显式turn-taking/router，保留直接响应的低风险接口，不从文本措辞自动升级成执行授权。[必要机制与边界](https://arxiv.org/html/2609.21392v1)。<!-- source-family:SF-2026-ARXIV-2609-21392 -->

### Resource Budget 与 Persistent Identity 都属于 Evaluation Identity

Memory/Agent 策略只报任务质量，会隐藏超预算调用和持久状态漂移。Resource-constrained evaluation 应把 per-call token budget 作为独立变量，联合报告质量、利用率、延迟和 violation rate，并冻结 tokenizer/grader；tokenizer 不精确时 violation 只能作为诊断，须回退 exact tokenization 与 full-context baseline。<!-- source-family:SF-2026-ARXIV-2609-13149 -->

跨 session 的 persistent identity 还要绑定 profile revision、session lineage 与更新路径，分别测 recall、composition、enactment、resistance 和 persistence。synthetic profile 与 judge-sensitive single sample 不能成为 release authority；没有可验证 identity ground truth 时只能保留诊断状态。<!-- source-family:SF-2026-ARXIV-2609-13637 -->

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

即使分布固定，也要区分“对某个冻结模型能计算测试分数”和“有限i.i.d.样本足以统一排序任意候选分布”。极小概率事件可能几乎不会进入样本，却因候选在该事件上的概率更小而主导KL/Rényi等无界指标；于是样本分数可算、模型排序的统一统计保证却不成立。[Statistical Evaluability的反例](https://arxiv.org/html/2604.05324v1)针对这一最坏情形，不是说固定测试集的perplexity无法计算，也不是否定所有经验模型比较。

恢复保证要明确限制声明，例如有界测试函数和有限VC/fat-shattering复杂度，或具体的分布/比率条件；代价是更窄结论、假设检查和可能很大的样本需求。实际release仍可用冻结任务及分层实测，但不能仅因样本很多就宣称任意模型/任意长尾上的可靠排名。这里的不可辨识风险不同于下面“未见状态质量”的估计，二者都不自动给出真实部署错误率。<!-- source-family:SF-2026-ARXIV-2604-05324 -->

多个 benchmark 名称也不等于多个独立能力证据。可在冻结的 model population 与逐项结果矩阵上检查分数相关、对单项移除的敏感度和谱的有效维度，再判断 suite 是否在重复计量同一差异；当模型群体从弱模型移到前沿模型，原来的相关性甚至可能反号。此类统计只能提出测量冗余和权重脆弱性的警告，不能把一个谱值解释成模型“真实能力维度”，更不能单凭高相关删除语义上必要的安全或失败切片。收益是避免重复指标伪装成覆盖，代价是保存版本化 item-level 矩阵、代表性模型群体并进行构念复核；样本小、二元噪声高或目标人群改变时，应回退任务定义与分层人工审阅。`arXiv:2603.29357v1` 的有效维度结果是作者所测 benchmark–model population 的条件事实。

<!-- source-family:SF-2026-ARXIV-2603-29357 -->

### Off-policy Coverage 必须覆盖 History，不只是当前 State

当 logging policy 依赖完整历史时，只检查每个当前 state/action 的 marginal coverage 会遗漏 trajectory likelihood ratio 的指数累积。即使每步 action 和 belief 看似都有常数覆盖，目标 policy 的关键 history 仍可能在日志中指数稀少，使 unbiased estimator 需要随 horizon 指数增长的样本。

这条下界不表示所有 OPE 都不可用，而是要求 evaluation identity 包含 logger 的 history dependence、horizon、support 与 estimator 假设。能够证明 Markov sufficiency、使用 on-policy/介入数据或缩短 horizon 时，旧 OPE 路径仍成立；否则应报告不可识别、扩大 uncertainty，或重新采集目标分布证据，不能用当前状态 coverage 宣称评估闭合。<!-- source-family:SF-2026-ARXIV-2609-19135 -->

### 能描述分布，不等于逐次调用会从该分布采样

让 instruction-tuned 模型写出“群体中各答案占多少”时，模型输出的是一次条件分布描述；对许多 persona 重复调用同一模型，则经过 instruction following 与 decoding policy 生成一组相关样本。二者的状态与控制流不同，不能因为前者接近真实比例，就把后者当作独立人口抽样器。Evaluation owner 应分别保存目标人口数据、模型描述分布、逐调用经验分布、persona/prompt、sampling configuration 与调用相关性，再校准两种任务。

直接询问分布减少调用成本，却依赖模型能估计目标人口；重复采样看似更自然，却可能在 sampling 前已经坍缩到近确定答案，调高 temperature 也无法恢复缺失的群体结构。公开实验只支持所测 public-opinion benchmark、模型与 post-training stages，不证明所有用户模拟都失败。缺少真实人群基线时，应把两类输出都视为 synthetic sensor，而不是社会分布真值。

<!-- source-family:SF-2026-ARXIV-2607-25292 -->

### Rare Failure Evaluation 需要保留无偏 Audit Floor

总体能力估计与失败发现是不同 estimand：前者在目标题目分布上积分得到 `S`，后者在预算内寻找低于阈值的失败集合 `X_λ`。GP posterior 可给两类查询分配预算，但 covariance、任务先验与采样目标必须一起保存；偏向发现难题的查询均值不能直接当总体质量。作者 Theorem 3 约束 posterior mean，而非实际有限题库平均 `S*` 的无条件保证。<!-- source-family:SF-2026-ARXIV-2604-23099 -->

建模、query selection 与观测成本进入评估预算，相似任务间错误 covariance 也会造成 negative transfer。先验或目标分布不可信、失败区域支持不足时，恢复独立分层/均匀 audit 与显式误差区间；不能把更多 failure discovery 同时解释为更准确的总体估计。

均匀采样对普通错误率简单无偏，却难以测 five-nines 级罕见失败。CEM 等 proposal distribution 可以把预算移向高风险样本，但它只拥有 evidence allocation，真实 failure rate 仍由目标分布、importance weights、ESS 和 confidence interval 决定。support 缺失或权重重尾会制造错误置信，因此始终保留 uniform/stratified audit floor；importance accounting 失效时停止发布稀有错误率。exact-v1 只支持披露 sampling regime，不证明自适应采样天然无偏或生产尾部已覆盖。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11209 -->

若风险事件定义在固定输入下的一整段随机输出轨迹，估计目标仍是**原模型**产生该事件的概率；从原模型权重扰动得到的可评分模型，只能充当采样 proposal，不能把新模型的命中率当作原模型风险率。在相同输出支持与解码合同下，可沿每个生成 token 累积原模型与 proposal 的概率比，再对事件指示量做 importance weighting。用于寻找 proposal 的可微 surrogate 与最终事件判定必须分开：提高 proposal 命中率若同时漏掉原模型某些失败模式，仍会让估计失真。有效样本量与权重尾部是诊断信号，不能自行保证 support 完整；coverage 不明时保留原模型/分层 audit floor，并让 release gate 保持开放。这一路径用额外训练和双模型概率计算换取深尾采样效率，不替代上界证明或真实部署任务分布验证。受限论文只在 GPT-2 Small/Gemma-2 的 token/profanity 类固定 prompt 事件中检验估计器，未验证 Agent 工具失败或生产安全率。

<!-- source-family:SF-2026-ARXIV-2609-24969 -->

固定输入的输出尾险即使估得准确，也不能直接推出一组用户改写或新输入的风险：输入 `c` 自身也来自某个待定义的分布。因而要把两层分母分开，先在每个 `c` 下核目标模型、解码、harm judge、proposal 支持、权重尾部和有效样本量，再在明确的输入家族或 `D_query` 下报告各输入风险的分布；若关心 `n` 个输入中最大风险是否超过阈值，还必须一同写明 `n`、阈值及输入抽样方式。增加同一 prompt 的输出采样，不能补足未覆盖的改写家族；代价是改写构造、逐输入估计和 judge 成本。固定模板且输入变化受控时，原固定输入估计仍是合理局部方案；新家族缺少独立覆盖时保持 Unknown 和发布限制，而不是把实验池的结果称为部署发生率。<!-- source-family:SF-2026-ARXIV-2604-22167 -->

### 从“已见切片均值”到 Blind-spot Mass

平均值和已知 slices 能回答已采样区域中的表现，却不能说明 heavy-tailed operational state 还有多少概率质量落在未见或低支持状态。可以在明确的 state partition 与 support threshold 下，用 Good-Turing 类估计构造 blind-spot mass，并把总体表现拆成 supported component 与 blind component；release owner 同时保存阈值、样本分布、估计不确定性和处置，而不是把一个较高平均分当成覆盖证明。

这把“也许还有长尾”变成可讨论的 coverage-risk signal，也带来 threshold sensitivity、方差和独立同分布假设。它估计的是当前抽样合同下的未充分支持质量，不是未知错误率或生产风险上界。分布漂移、样本依赖或 state definition 不稳定时，应回退分层抽样、定向补测、online canary 与保守 release gate。

<!-- source-family:SF-2026-ARXIV-2604-05057 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05638:start -->
### OOD Sensor 要把 Representation 与 Detector 分账

在小模型或表示尚未预训练充分时，复杂 detector 可能补偿局部几何缺陷；随着 frozen representation 扩展，global Mahalanobis 与 local score-curvature 之间的性能差距可能收敛，真正支配结果的转为 backbone geometry。Evaluation contract 应固定表示版本、层、归一化、distance/curvature estimator、reference distribution 与 threshold，然后分别改变 representation 和 detector；否则不能判断收益来自更强检测器，还是更可分的表示。

简单 sensor 降低训练和部署成本，但 label-free geometry 不是 OOD 真值，也可能在 hard shift、模态变化和生产漂移下失效。现有证据只比较 59 个 backbone-task pairing 与两类 detector，不覆盖所有分布。校准漂移或 slice 风险升高时，应回退 labeled OOD set、task-specific detector 和人工 release gate。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05638:end -->

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

探索得到的高错误切片还面临选择偏差：试过足够多的描述子，总会有一个显得特别糟。直接固定错误差阈值在少量预设切片时仍是简单基线；当描述子由搜索或模型大量提出，就应把“提出解释”与“允许报告解释”分开。一条受限分支先冻结错误标签与描述子库，在相同样本数、支持量和评分规则下，将描述子的布尔成员随机置换，得到保持出现比例的假竞争者；真实切片只有超过这种经验噪声底线才进入下一步。然后冻结幸存集合，在未用于发现的数据上要求支持量、错误率差方向和预设最小幅度仍成立。描述子的产生者不拥有发布权，审计者也不能见到 holdout 后反复调整规则。<!-- source-family:SF-2026-ARXIV-2606-09046 -->

这种分账用额外置换、留出样本和较低检出力换取对偶然高差异的约束，却不是有限样本 FDR 保证：逐描述子置换保留出现比例，不保留描述子之间的相关结构，经验假发现比例也不是已知真值。[受限审计](https://arxiv.org/html/2606.09046v1)能找回人为植入的困难，却未在两套自然 benchmark 上确认候选解释；这不证明错误随机或不存在。稀有切片、相关元数据或分布漂移使对照失真时，应保留探索性标签、追加独立样本或采用有适用假设的统计程序；重复成立的关联仍不等于失败原因，需要干预证据才能继续归因。<!-- source-family:SF-2026-ARXIV-2606-09046 -->

表面格式偏差也不能靠“减去可预测的格式分数”自动修好。若代码正确性有可执行测试、且只改注释不改行为，成对干预可测出格式通道对 scorer 的影响；但在自然语言评估里，长度、重叠或文风也可能承载真实任务信息。Residualization 即使降低所测线性格式相关性、提高预先指定的错误切片一致性，也可能同时降低全体样本的一致性和同问题排序。Evaluation owner 应把原分数、干预效应、切片增益、切片外代价和下游决策分别报告；调整值只能是审计诊断，不能未经目标分布验收就替换发布分数。这样换来偏差可定位性，却增加成对样本、独立标签和分层审计成本；没有可区分构念与格式的证据时，应保留原评分并标记测量不确定，而不是宣称“去偏成功”。证据限代码注释受控干预与所测 NLI/QA scorer；论文中的当前代 judge 探针未通过其预设 loading gate。<!-- semantic-body-binding:SF-2026-ARXIV-2609-24194 -->

### Forecastability 是独立 Sensor，不是更高 Accuracy 的同义词

当错误无法完全消除时，训练目标可以让失败更集中于可提前识别的状态，便于 abstention 或 routing；这改变的是 error
distribution 与可预测性，不必提高平均正确率。forecast sensor 只估计风险，action policy 决定拒答/升级，outcome evaluation
另行验证真实收益。它可能诱导模型把失败集中到某些群体或学习 detector shortcut，必须同时看 accuracy、coverage、slice
harm 与 calibration。现有 Gumbel-tail 方法和实验只支持作者设置，失校准时应回退外部 verifier 或保守阈值。

<!-- source-family:SF-2026-ARXIV-2605-15134 -->

从风险测量走向升级决策时，还需要一个成对的评价合同：同一任务上，先测模型对自己弱项的预测，再测它是否真的据此求助，最后测外部解决者能否解决，以及本来可自行完成的任务是否被多余升级。给模型自身分数、再加入规范提示、最后由外部 router 强制执行，是不同控制条件；最后一项的收益不能记作模型自省变好。可校准的能力判断只是 action policy 的输入，不自动取得决策权。<!-- source-family:SF-2026-ARXIV-2604-19809 -->

这种分账增加同题对照、标签和外部调用成本，却能定位“认识到风险但不改变行动”与“已经升级却被不可靠 resolver 接住”的不同失效。MIRROR 的固定任务与按模型定制任务不能直接合并比较，原 oracle-resolver 条件也须与其 fallible-resolver 实验分开；后者仍有错误解答和不必要升级，不证明工具或路由能保证正确。外部解决者更弱、成本过高或弱项标签漂移时，应保留直接回答、保守拒答或人工复核的条件分支，而不是把所有低置信请求自动转给另一模型。<!-- source-family:SF-2026-ARXIV-2604-19809 -->

### Calibration 必须寻找隐藏 Regime

全局 ECE 或单一 reliability curve 会把局部过度自信与保守区间互相抵消。评价应估计随输入属性变化的 miscalibration field，主动寻找符号反转或突然失效的 regime，而不是只在平均分桶上验收。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13484 -->

人为扰动模型的 logit 或表达方式可以构造已知 uncertainty shift，用来检验指标能否识别错误置信，而不是证明模型真的产生了 epistemic uncertainty。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13595 -->

这两类证据主要来自合成或受控设置，不能给未知分布提供完备保证。定位不到稳定 regime 时，应回退高风险 slice、abstention curve、外部证据核验和人工升级。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07776:start -->
终局 confidence 会丢掉推理过程中的转折：错误可能在中段出现，随后语言表面重新变得确定。Evaluation owner 可把 reasoning trace 视为 evolving measurement state，保存 early/mid/late uncertainty、slope、fit quality 与首错位置，再验证在多少前缀比例下可预测失败。它支持 early stop/escalation proposal，却不是因果归因或 truth；token probability 不可见、跨模型校准漂移或 AUROC 不稳时，应回退终局 verifier、外部 evidence 与保守 abstain。 [受限证据：arXiv:2605.07776v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07776:end -->

### Joint Embedding Uncertainty 不能由单边置信代理

双编码 VLM 的图像与文本分别高置信，并不保证配对关系可靠。对 product hypersphere 上的联合 embedding distribution 建模，可以把跨模态 density 和 pairing uncertainty 作为 post-hoc sensor；它改变的是评价证据，不拥有最终 truth。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13352 -->

Flow model 会继承训练配对偏差，冻结 encoder 也可能隐藏 representation shift。所测数据上的 calibration 不能外推开放世界；density 失配或新域无覆盖时，应回退任务级验证、检索证据和人工检查。

### 视频评估先确认模态与时间信息是否必要

音频必要性也应在同一问题上比较 None、fragment 与 full audio，再将 temporal binding（TB）和具体信息需求分开。先判是否 audio-needed（AN），再在 AN 内区分 fragment-sufficient（FS）与 extended-sufficient（XS）；“只有 3–4%”描述作者 AN 内的切片，不是全部视频题、更不是真实认知机制占比。<!-- source-family:SF-2026-ARXIV-2604-24401 -->

分层消融增加片段构造、重复调用和支持证据成本，片段边界可能遗漏声学线索，TB 也不等于已证明脑内时间推理。片段选择或 gold 支持不可靠时保留 full audio 并报告不可区分；只需静态声音信息的任务可采用便宜 fragment 基线，不静默改变原始全输入分母。

Gold answer 的支持证据也必须绑定模型实际看到的帧集合。若标注来自完整视频，而模型只消费 16/32/64 sampled frames，题目可能对该输入不可答；EvalSpec 应记录 frame sampler、可见 evidence、visibility 筛选与人工复核，并用 dummy video 对照检查语言先验。作者 5% visibility 门槛是其筛选协议，64 帧不是普适的可答性真值。<!-- source-family:SF-2026-ARXIV-2604-24300 -->

这增加证据标注、重新采样与人工成本，也可能把采样器遗漏误当模型能力不足；保留子集与原题集必须分别报告分母。可见性判断不稳、帧预算改变或任务本需连续视频时，应回到对应输入合同重建支持集，不用完整视频 gold 直接评价未见证据的模型。

视频问答的整体正确率可能来自语言先验、音轨或单帧线索，而非视频的时序理解。廉价的旧基线适合衡量题目在完整输入下是否可答；若要据此选择视频模型或宣称时间推理能力，EvalSpec 还须固定同一问题的输入消融：只给题目、只给音频转写或帧叙述、只给中心帧，以及打乱帧顺序。分别比较完整输入与这些受限输入，才能区分视觉必要性、时间必要性和仅由其他通道提供的可答性；筛选后的子集也须保留原分母、筛选器版本及人工歧义复核，不能把较低分数直接解释成模型退化。

这使能力声明更贴近任务构念，但消融本身只是诊断代理：转写和自动叙述可能丢失信息，多个诊断模型的一致答案也不能证明样本在所有模型下都不需要视频。作者在 14 个视频基准的 24,416 道问答上依协议保留 11,332 道，并报告完整与保留子集之间明显分差；该结果只说明这些基准及其诊断协议存在 shortcut 风险，不能外推为所有视频任务的固定无效比例。对本就只需静态视觉或语音的业务任务，原始完整输入分数仍是有效的受限指标，无须强行要求时间依赖。

<!-- source-family:SF-2026-ARXIV-2603-29616 -->

在线流视频还存在不同的评价混杂：复杂历史记忆可能提高过去事件的回忆，却削弱对当前画面的感知，而一个总分会把两者抵消。要证明 memory 或 retrieval 的增量，应先在相同 causal visible prefix、backbone 与预算下建立仅用最近若干帧的强基线，再把实时感知、真正的 episodic recall 和抗幻觉/误导三类结果分别报告。特别是“能识别提示中的幻觉”并不等于“记得先前事件”，不能因为基准把它列在 backward tracing 就归入记忆收益。

这使 memory 组件的收益和代价可定位，但最近帧基线天然不能回答超出窗口的必要历史事实；长程任务仍需记忆、检索或压缩，并须证明其在所需 recall slice 上的净收益。[受限对照](https://arxiv.org/html/2604.02317v1)在 OVO-Bench 与 StreamingBench、Qwen2.5/3-VL 和作者披露的帧采样条件下，观察到历史检索提高部分回忆任务却降低实时感知；跨模型方法的骨干与预算未全部匹配，不能把排行榜差距全归因于 memory 架构。<!-- source-family:SF-2026-ARXIV-2604-02317 -->

实时可用性还要区分两只时钟。让视频输入等待模型处理完再推进，适合比较相同可见帧下的理解能力，却隐藏了部署中持续到来的画面；独立 camera producer 与 model consumer 则会产生积压、丢帧和旧答案继续生效。EvalSpec 应声明输入帧时点、回答可用时点、最新帧队列容量以及没有新回答时的处理方式。若评估在空时点沿用上一回答，少更新甚至慢回答也可能提高文本一致性；因此 consistency 必须与对应时点的准确性、更新频率和端到端延迟一起解释，不能单独作为实时质量。<!-- source-family:SF-2026-ARXIV-2604-07634 -->

墙钟评估换来部署约束可见性，也让硬件、API 网络、缓冲与历史选择共同影响模型排序。作者的受限流式视觉实验中，同步与异步协议的排序和 consistency 发生变化，后者还受 carry-forward 影响；这不证明慢模型的内部推理更弱，也不证明高稳定性回答更新及时。比较基础理解时保留同步协议；选择在线服务时另测相同 camera cadence、可用时间语义与缓冲政策的异步合同，不能把两者合成一个无条件排行榜。证据限披露模型、H100/bfloat16、1 FPS、camera buffer 600 与 working context 64 的设置，不外推任意实时 SLO。

视频**生成**评价器面对另一种缺口：它即使在短片上与人工排序相关，也未必能辨认长片里逐渐累积的时序、语义或画质退化。把评价器用于模型发布前，应先以同一原片构造仅改变一种质量维度的正反视频对，筛掉人也难稳定辨别的样本，再按视频时长和退化类型检查评价器能否把明显变差的一侧排在后面；这检验的是评价器的最低辨别力，不是直接给生成模型打分。可控退化与人工筛选换来可定位的失效切片，也增加合成伪迹、人工成本和构造偏差。若真实生成错误不长得像注入的退化，测试通过仍不能证明线上 judge 可靠；短片评价器也不能未经长时长复核直接复用。[长视频评价器的受限 meta-evaluation](https://arxiv.org/pdf/2603.29186v1)只支持其十类合成退化、人可感知成对样本及所测自动评价系统的差距，不能把该排序当成未来生成视频质量的真值。<!-- source-family:SF-2026-ARXIV-2603-29186 -->

能生成流畅视频描述，不等于能识别同一描述中的错误事件。与只给问答 gold 或人为注入退化不同，一条评估分支让多种模型产生自然 dense captions，再由人逐句对照原视频，区分 Correct、Incorrect 与证据含糊的 Unknown，并标出对象、动作、顺序等错误位置。特别是某事件在视频其他时点出现、却不在所述 timestamp 出现，属于时间错位而非事件完全不存在；持续重复旧事件也须随视频进展重新验真。Caption generator 只提供待测 claims，独立支持标注决定 verification target，语言 plausible 或解释写得合理都不能代替视频证据。Unknown 的剔除、实际可见帧集合与错误类型应保留为评价人口身份。

这增加视频观看、时间区间与词级标注和推理调用成本，也受人工分歧与采样遗漏影响。VidOmni-Bench 的 500 视频、五种复杂度和多时长实验以 video-caption pair 为单位宏平均错误检测 precision/recall/F1；五人的标注池不意味着每条都经五人判断，附录规定每 pair 至少两人并由作者裁定争议，κ=.50 不支持绝对真值保证。Certificate Coverage 只来自每 benchmark 抽取的 30 视频；自评低分与跨模型 ensemble 的增益也不单独证明 self-preference 的唯一因果，caption 来源/难度及模型帧预算仍须分开。更高帧率不单调改善、音频对不同模型作用相反，故不据单一生成分数、模型大小或外部 judge 宣称普遍验真能力；输入支持不稳时回到人工支持、帧合同与明确 abstain。 [必要机制与反证](https://arxiv.org/html/2609.21521v1)。<!-- source-family:SF-2026-ARXIV-2609-21521 -->

### Clean Ranking、故障切片与可信度任务必须分账

clean aggregate 在输入模态完整、分布稳定时最适合比较基础能力；一旦部署约束包含 corruption、missing modality、
misclassification detection 或 OOD detection，同一方法在这些任务上的排序可能改变甚至反转。因而 EvalSpec 必须分别保存
clean performance、每种故障模型、缺失模态模式、MisD/OOD 定义与对应阈值，release gate 不能用 clean accuracy 或单一
confidence 数字代理全部 trustworthiness。

这条演进用更大的评估矩阵换取 failure ownership 的可定位性，同时增加训练/评测成本、切片方差和模型选择复杂度。
现有对比在统一 split、optimizer、model selection 与 random-search 合同下覆盖六个数据集、三类判别/回归任务和两种
corruption；7402 次训练仍不证明生成式多模态、任意 sensor failure 或生产安全，MisD/OOD 也不等于安全真值。模态固定、
故障模型与部署无关或预算受限时可保留 clean baseline，但必须声明适用域；高风险发布应补 workload-specific corruption、
missing-modality、calibration 与 OOD slices。

<!-- source-family:SF-2026-ARXIV-2605-06643 -->

### 不确定性必须绑定覆盖假设，而不是装饰性置信区间

没有 ground-truth labels 时，比较分数仍可作为测量工具，但不能直接获得“正确”身份。此时应冻结 scenario、rubric、
auditor、judge、target model 与 sampling policy，把整套链路当成 measurement instrument；先用预期方向已知的 contrast
验证区分能力，再测 target sensitivity、重复运行方差与对合理扰动的稳定性。通过这些检查只支持“该仪器在已测范围内
能做相对比较”，不支持 safety certification 或内部机制结论。

这种方法允许在标签稀缺时继续积累证据，却把 rubric bias、judge 相关错误和 target leakage 带入结果。对比方向不稳、
换 judge 后翻转或方差过大时，应保持 Unknown 并回到人工/外部 outcome，而不是用更多小数位制造确定性。现有证据只
覆盖作者的无标签比较设置和验证协议。<!-- source-family:SF-2026-ARXIV-2605-06652 -->

文本评分还须保存 score、proxy label 与目标 construct 分别读取哪个 span。二者共享开头时，较高 agreement 可能只反映共同表面信号；可冻结 score/task/construct/judge，让同一 proxy 规则只在 scored span 的严格补集重读，再比较其与独立 construct 的差额。完整输出仍含原开头，不是这个 disjoint control；off-span 本来可受 construct 共同影响，因而应以 observed construct 内分层的 permutation null 比较，而非机械把 chance 当全部零假设。

[受限 span 审计](https://arxiv.org/html/2609.25808v1)支持上述诊断，不识别唯一 containment 因果、比例或修复：残余可来自 spillover、proxy 失配和粗标签。稀少 positive、空补集、严重 score ties 或等价检验不足都须保 Unknown；共享 span 本身也不证明无效。删除已生成文本的表面特征不是重新生成后的保真修复，某些 construct 指标仍会下降，judge 人工一致性和大量 undecidable contracts 限制推广。新增构念标注、重读与检验增加成本，不能让局部 association 或 categorical flag 自授发布；证据不足时回到独立 construct/人工评价与原固定测量路径。<!-- source-family:SF-2026-ARXIV-2609-25808 -->

点估计便于排序，但遇到 shift 时不能说明错误风险。Conformal-style interval 可以把 calibration set 与 coverage target 交给 evaluation owner，输出带条件的 prediction set；代价是区间变宽、exchangeability 假设和 recalibration 成本。假设失效时应降级为 slice-level diagnostic 而非发布保证。<!-- source-family:SF-2026-ARXIV-2605-19779 --> exact-v1 §2–4 支持其 conformal pipeline 与研究结果，§5 明确不证明任意依赖或分布漂移下仍覆盖。

### Structured Prediction Set 要把多种有效输出留在合同中

单标签 conformal set 假设候选答案可以枚举并由一个 label 判定，在代码生成中却常有多个语义等价程序，完整程序空间
也无法直接列举。更适合的对象是 partial-program structured set：先对多个局部假设分配风险，再用 multiple-hypothesis
control 形成候选结构；只有必要时才 selective execution，用测试把集合收缩。calibrator 拥有统计风险边界，executor
只提供动态 evidence，release gate 才决定是否接受某个程序。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12201:start -->
减少 execution 次数的代价，是 prediction set 更宽、multiple-testing correction 更保守，并依赖 calibration/test
exchangeability；测试本身不完备时，risk guarantee 也只覆盖定义的 label event。分布漂移、支持集不足或高风险代码
不能接受 partial correctness 时，应回退完整执行、静态分析、人工复核或 abstain。现有证据限于 HumanEval、MBPP、
APPS、受测 32B–70B 模型、100 splits 与披露的 H800/CUDA 条件，不证明生产代码安全。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12201:end -->

定义 label-relative risk 之后，还应把 oracle 的三种角色分开：哪个执行判据把候选分成等价类、哪个标签校准 abstention threshold、哪个独立评价判定语义错误。固定候选池跨 oracle 比较 score 与阈值，再同时审计接受和拒绝两侧，才能看见“对自己的标签证书有效”与“对目标构念有效”的差额。含 abstain 零损失的 marginal risk 不是已回答样本的 selective risk，随机 question split 的 exchangeability 证明也不自动覆盖 schema-disjoint 部署。

[受限 Text-to-SQL 审计](https://arxiv.org/html/2609.25938v1)显示较严格执行 suite 仍可与专家语义标签双向不一致；offline reference 参与 partition 的控制与 gold-free 场景必须分账。多次重叠 resplit 不等独立重复，少数同 lineage checkpoint、AI-only taxonomy 与不完整外部 pilot 也不证明普遍 reference 缺陷率或语义风险认证。双侧标注、跨 oracle 控制和独立执行都有成本；目标标签、支持集或分布关系不可靠时，保留人工/外部执行复核与 abstain，不让 score 构造 oracle 同时自行认证 semantic truth。<!-- source-family:SF-2026-ARXIV-2609-25938 -->

### 重复评分的不确定性可以进入 Conformal Nonconformity

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23189:start -->
普通 conformal prediction 把单次 score 当作稳定观测，在 evaluator 方差小且 exchangeability 近似成立时最直接；随机 judge 或生成式评分出现后，可以用重复 score 的均值与不确定性共同构造 r-value nonconformity。该统计量只改变排序证据，coverage owner 与 admission policy 仍然独立。

variability-aware 分支可能缩小不必要的集合，也会增加重复推理成本，并在方差估计不足时制造虚假精度。作者实验只支持披露 vision/VLM/LLM 设置；exchangeability、重复数或 evaluator identity 不成立时，应回退普通 conformal score、扩大集合或保持 abstain。arXiv:2605.23189v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23189:end -->

工具调用还要先区分失败发生在哪一层。请求在 dispatch 前被 message template 拒绝，属于 typed adapter/transport failure，不是模型选择不调用工具；若把错误压成普通 assistant 文本，就会把未发生的模型行为写进评估。Protocol fidelity 应以实际产生的 turns 为条件分母，同时保留固定 task 分母的交付结果与未响应原因；长 loop 产生大量有效格式 turns，也不能靠 pooled-turn 比率稀释失败 episode 的权重。

[受限本地 serving-stack 评价](https://arxiv.org/html/2609.26693v1)分离 native、带固定 hint 的 native 与统一 text-tools 条件，发现统一协议也会令部分模型退步；语法约束让单 turn 格式有效，不保证最终任务交付。结果绑定具体 Ollama/version、少量 coding tasks 与 CPU GGUF/GPU upstream 配置，跨栈并非完全同权重且未固定所有采样随机性，不能称所有模型或后端全复现。分层回执与 episode 权重增加实现和审计成本，却允许先修 adapter 再判断模型；路径不兼容时保留经验证的 native adapter、单 task 检查与显式失败，而不是静默混并评分。
<!-- source-family:SF-2026-ARXIV-2609-26693 -->

### Response Rate、条件质量与无条件质量不能互相替代

当系统可以通过“不行动”保留原输入时，直接平均 fidelity、realism 或 safety quality 会奖励 non-response：输出几乎没有变化，看起来保存得很好，却没有完成任务。最简单的总体均值只有在每个样本都产生了可判定响应时才合理；一旦存在拒绝、空输出或原样返回，评估必须同时保留三种量：目标是否实际响应的 `response rate`、只在已响应样本上的条件质量，以及把未响应作为任务失败计入固定分母的无条件质量。条件质量诊断“做了以后做得怎样”，无条件质量回答“交给系统以后总体交付怎样”，两者不能用一个更好看的数字相互覆盖。

响应判定本身也是 detector：微小但有效的修改可能被漏掉，无意义扰动又可能被当成响应。因而 response detector、阈值、目标 modality 与 input/output identity 必须进入 EvalSpec；检测不可靠时，回退到成对输入输出的确定性检查或人工复核，并禁止用 gated quality 作为发布结论。AVE-Compass 的 exact-v1 在 145 个 source videos、196 条音视频编辑指令和六个受测系统上显示，部分系统因保留目标流不变而获得虚高 preservation 分数；它支持这里的分母分解，不证明其 MLLM judge、响应阈值或模型排名能外推到其他生成任务。

<!-- source-family:SF-2026-ARXIV-2607-24821 -->

成对continuation共用同一sealed prefix，可以隔离首请求的表示变化；但runner若只在第一臂completed后执行第二臂，就把观测机会绑定到了受测方案的结果。固定预算耗尽是“未在该预算内交付”的已知失败，根本未执行的companion却是未知，不能当失败、成功或从completed pairs平均中静默删除。交替顺序不能修复这种零观测概率；应分别保存allocated boundary、两臂是否执行、cap/错误final/完整性停止，并以未知二元结果的上下界报告固定记录frame的差值，而不是把该范围叫population置信区间。

[受限成对case study](https://arxiv.org/html/2609.31381v1)中，joint-success子集可被完整识别，仍不代表未来随机continuation的always-success人群；token总量下降也伴随更多requests和更高median ratio。拟合selector的案例不应充当新test，改变threshold是再拟合而非确认。双臂各自预授权resource reservation增加费用，但普通cap或wrong final不该取消另一臂；integrity故障、权限撤销或不安全环境仍可停止并显式保留unknown。预算不足时缩小预先声明的pair集合或只报告单臂结果，保留完整fixed-budget分母、interaction/cache成本及原full-view基线，不用省token或已完成子集认证质量保持。<!-- source-family:SF-2026-ARXIV-2609-31381 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21545:start -->
同一问题也出现在 safety refusal：aggregate refusal rate 会把 blanket refusal、对风险不敏感的低拒绝和“措辞谨慎但仍提供关键帮助”压成一个数，因而不能独自拥有安全排名。EvalSpec 应在相同 task framing 下构造 benign、borderline、dual-use triples 与 should-refuse positive controls，并分别报告 risk-tier discrimination、strict/partial compliance 和内容级 harmful uplift；access path、system prompt、temperature 与 judge 也必须进入 Evaluation Identity，不能把 provider/API 行为静默归因于模型权重。

多轴评估需要专家风险标签、重复调用与内容编码，牺牲了单一排行榜的廉价可读性；而 borderline request 是否应拒绝，如果没有专家标注，本身就不能由 refusal rate 决定。现有生物研究 prompt、单一 system prompt/temperature、有限重复和 judge council 只支持 metric correction，不证明当时的模型排序或端到端安全。risk labels、judge agreement、adversarial slice 或 expert warrant 不足时，应保留 `Unknown`，发布各分布并回退确定性 policy outcome 与人工审查，不能用总拒答率单独批准或拒绝发布。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21545:end -->

风险还有输入和输出两个端点，不能只给prompt一个tier就假设response继承它。分别独立标注prompt与response后，可以记录安全输入走向有害输出、有害输入走向安全输出的方向矩阵，并明确每一条件分母：例如原定义的drift-up是P(prompt safe | response harmful)，不是P(response harmful | prompt safe)。前者回答有害输出从哪些输入来，后者回答安全输入的风险率；两者都可能有用，但不能互换。<!-- source-family:SF-2026-ARXIV-2604-26052 -->

双端标签增加人工/判定器成本，也会受到标签边界、同源错误和样本构造影响。作者有限单轮英语样本只支持这个风险转移测量，不能由方向关联推因果harmful uplift或生产发生率。部署评价需保留benign帮助和应拒绝样本两类机会集，标签不可靠或多轮外推不足时保持Unknown，回退专家复核与实际policy outcome；旧risk-tier/refusal评价仍负责其原问题。

多数投票只在同质固定 competence 的简化假设下随 vote budget 单调改善；对具有异质 per-example correctness 的 exchangeable repeats，增加票数可能改善、恶化或多次改变趋势。Evaluation owner 应保存完整 odd-budget curve、样本切片与 aggregation identity，不能把更多 samples 当成天然可靠的 test-time scaling knob；曲线异常或样本依赖无法界定时回退固定预算、独立 verifier 或 abstention。

exact-v1 提供 de Finetti/有符号 Hausdorff moment 的理论刻画；没有证明任意非交换采样、开放式答案聚类或生产 judge 下都成立，也没有给出通用最佳票数。 INFER-SCHEDULING 可消费经验证的 vote budget/risk curve，但不拥有聚合真值。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05592 -->

### Per-verifier Outcome 与 Aggregation Rule 都属于 Evaluation Identity

Verifier 集合自身也可能由数据构建：在 development traces 上按 false positive/false negative 找到缺口，执行 checker 的 ADD、REMOVE、REPLACE，再冻结 checker-set 后在 held-out traces 上准入。搜索中的 dev score 只负责提议修改，不能兼任新集合的验收 truth；每个 checker、组合规则与数据划分应留版本。<!-- source-family:SF-2026-ARXIV-2604-22937 -->

这增加 checker 执行、开发标注和集合搜索成本，也可能过拟合开发错误；作者最高增加 55 个 F1 点是 verifier 判别对照，不是 Agent task accuracy，OOD 切片还会退步。独立标签不足、checker 变动不可归因或新域退化时，回退原冻结集合、人工审核或不作发布判断。

多条件任务常先产生一组 verifier outcomes，再把它们汇总为 task score。只保存最终标量，会把 `all-pass`、平均 criterion、majority 等不同问题伪装成同一个指标；相同轨迹和相同 verifier 结果，仅替换 aggregation function 就可能改变分数乃至排序。平台应先保存 typed per-verifier outcomes、缺失状态和 verifier revision，再把聚合函数、阈值、权重与版本作为 EvalSpec 的一部分生成可重算视图。

这提高跨版本审计与重算能力，却增加高基数存储、上游 schema reconciliation 和身份维护成本。跨 benchmark 字段无法可靠对齐时，应回退到 benchmark-local 原始证据和受控复跑，不能用强行统一的总分填补语义缺口。Messier exact-v1 的反事实重算支持“聚合规则会改变观测结论”这一边界；它不证明异构 benchmark 已共享同一能力构念，也不把统一 corpus 升格为通用能力真值。

<!-- source-family:SF-2026-ARXIV-2607-25891 -->

聚合之前还要先决定每条条件由谁验证。多条件生成若让同一个 judge 同时拆解约束、判断图像与文本证据、设置权重并给总分，任何共享偏差都会被最终标量隐藏。更可审计的路线是先把条件拆成 typed evaluation units，再按 image-only、text-only 或 joint 等类型分配 verifier authority，保存逐项 outcome、缺失状态和聚合权重；只有这些原始证据稳定后才形成总分。

这种分权提高定位能力，却引入 atomization error、错误路由、相关 judge 与额外调用成本。联合约束被拆坏、verifier 共享 backbone 或权重未经校准时，应回退整体人工判断或确定性 checker；少量简单条件也不必强行拆分。公开证据只支持其个性化图像生成集合与有限人评相关性，不能外推为跨文本、视频或任意生成任务的通用评分器。

<!-- source-family:SF-2026-ARXIV-2609-12397 -->

当模型会先生成草图、几何图或其他辅助状态再作答时，最终正确也不能证明辅助状态有效。Evaluation owner 应设置 `No-Aux / Generated-Aux / Validated-Aux` 的配对干预：分别测没有辅助状态、自主生成状态和可信参考状态下的结果，并单独记录辅助质量、模型是否真正消费它以及终局 outcome。这样才能区分“中间证据有潜力”与“模型能够可靠地产生并使用它”。

干预矩阵会增加 reference artifact、judge 与运行成本；自主生成的错误还可能与后续推理形成相关失败。参考辅助只是能力上界，不是部署可得输入；低风险任务或中间状态不参与决策时，final accuracy 仍可作为便宜基线。现有结果只覆盖有限视觉几何题与模型组合，不证明可视化过程天然忠实。

<!-- source-family:SF-2026-ARXIV-2609-12606 -->

## 评估对象有四个层次

### Model Evaluation

固定系统外壳，比较模型本身的能力与行为，例如知识、推理、指令遵循、鲁棒性和安全。它适合模型选择，却不能证明完整应用可用。

### System Evaluation

评估 `model + prompt + context + retrieval + tools + policy` 的端到端结果。RAG 的 retrieval recall 与 answer groundedness、Tool Calling 的选择与执行结果，都属于这一层。

### Runtime and Service Evaluation

在目标硬件与 workload 下测量 TTFT、TPOT、goodput、错误率、容量、恢复和成本。质量相同但无法满足 SLO 的 artifact 仍不能发布；延迟更低但输出质量回归也不是有效优化。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-32283:start -->
比较 Serving 配置时，固定 question、长度和 greedy 设置仍可能没有固定工作：token 差异会改变后续 prefix 复用，数值变化会改变 MoE 专家，tool 耗时又改变下一轮到达和 batch。受控回放可以按真实依赖图固定 input/output token，在正常 forward、LM head 和 sampling 之后、更新 next input/history 之前提交 recorded token；需要比较 expert 策略时另固定 logical expert IDs，但不固定物理 placement 或系统 batching。这样保留了真实模型执行，让“工作发生了变化”和“相同工作执行更快”分别可测，而不是直接返回存档响应。

Tool-duration 模拟也只保留等待与依赖，不重外部 effect 或真实 CPU/I/O 竞争；如果优化对象包含这些资源，就必须另执行 tool。跨 tokenizer 回放应固定 target 序列，不能声称 source token 数或 router identity 相同。[AgentReplay v1 §3–6](https://arxiv.org/html/2609.32283v1)的有限案例说明 length-only workload 可能把 prefill 与 decode 成本分别高估或低估，重复性改善不是 speedup 或小模型自治成功。Trace 录制/代表性和 hook 也有成本，lossy KV、量化及 task quality 仍须 live 评价，speculative 接受轨迹不能从普通 AR 回放自动推出；对确实不敏感于内容的测量，length-only 基线继续合理。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-32283:end -->

### Agent and Outcome Evaluation

同一 incident 的前端症状与后台 fault 需要显式配对，才能区分“看见问题”与“诊断原因”。Browser observation 提供用户侧症状，backend tools 提供候选故障证据，提交答案再由独立 oracle 判定；EvalSpec 应保存 incident identity、跨层 tool access 与提交事件，而不是把各层独立成功率相加。<!-- source-family:SF-2026-ARXIV-2604-23455 -->

跨层访问增加工具、环境和证据整合成本；作者 87 个 incident corpus 中 25 个 test 的不同 tool/提交率对照，不能推出更多证据天然有害，也不能把未提交和错误诊断混作同一原因。工具权限或 oracle 不一致时应分切片报告，简单故障仍可保留单层诊断基线。

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

长期委托编辑还需要单独测 artifact 保留性，而不是只看每次任务是否结束。一个可复查分支为编辑定义 forward/inverse instruction，在每步独立 session 中携带文档，连续执行多个 round-trip，再按领域 parser 比较重建内容与原始 artifact。这能暴露多次看似成功编辑后积累的稀疏严重损伤；但高重建分数可能来自 no-op、部分执行或错误抵消，低分也不能分解错误出现在 forward 还是 inverse。必须另验前向编辑确实完成、可逆条件成立，以及 parser 没有漏掉需要保护的语义字段。

这条测量增加成对执行、checker 和原始 artifact 存储成本，也将可逆任务选择、session边界、distractor 与领域权重写入 EvalSpec。[受限长编辑实验](https://arxiv.org/html/2604.15597v1)中的严重 round-trip score drop不能等同逐token内容丢失率；基础文件工具harness也不代表所有Agent系统。无法构造可信inverse、任务确实有损或checker不足时，应回退逐步diff、不可变before-image、具体编辑的独立测试和人工审阅。完整cycle/verifier仍负责交付判断，round-trip分数只补 artifact-preservation evidence，不拥有任务完成权。<!-- source-family:SF-2026-ARXIV-2604-15597 -->

单个模型的 forward/inverse round-trip 还可能掩盖接口的角色差异。将相同结构化输入交给多个 sender 生成语言，再由多个 receiver 恢复，用固定符号等价 oracle 形成 sender×receiver 矩阵，能把配对和方向效应从一个总分中拆出；结构化 JSON/AST 的无损序列化可作另一条对照。Guard 失败按完整 suite 计零，缺字段与重复另记故障，不能只统计通过 guard 的输出。

这些量仍相对于所测模型 panel 和 prompt。多个 receiver 都恢复失败并不独立证明 sender 有错，一个恢复成功也不证明文本无歧义；guard 漏检会抬高分数，而非给出保守下界。受限 16 模型、2450 表达式、greedy 且不启用 thinking 的实验支持角色配对差异；同语义/树拓扑微调与改变 few-shot 的跨域对照不能混为普遍 transfer。设计 owner 应保留原始结构、方向、协议和 oracle 范围，不把符号等价推广为所有语义保真或用单个排行榜挑选双方。 [必要机制与反证](https://arxiv.org/html/2609.21509v1)。<!-- source-family:SF-2026-ARXIV-2609-21509 -->

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

#### Knowledge Surface、Artifact、Answer 与 Cost 是四个 Failure Owner

异构知识任务还多一道容易被端到端成功率吞掉的选择：Agent 先决定访问文档、表格还是依赖图等 knowledge surface，随后才取得 artifact、生成答案并付出工具调用成本。选对 surface 只证明路由兼容；即使提供 gold surface，也不证明系统取到了所需证据、更不证明正确使用证据。评估记录应按 `route → artifact acquisition → answer synthesis → cost` 保存四段结果，让 router、数据访问、生成器和预算控制分别承担自己的 failure。

typed surface 与 provenance 提高可诊断性，也引入 derived view 陈旧、metadata 错配和多路检索成本。surface 不唯一或 metadata 不可信时，应回退到更宽或并行检索，但仍保留 artifact 与答案的独立 Gate；单一知识面、可预测任务继续使用简单 pipeline。WorkSurface-Bench exact-v1 在其文档、表格和图三类 surface、1,151 个任务与四个受测模型上表明，高 Route F1 可以与明显较低的 Answer score 并存；它不证明三类表示覆盖所有企业知识，也不提供通用指标权重或生产表现保证。

<!-- source-family:SF-2026-ARXIV-2607-25765 -->

四层不是四套互不相干的平台。它们共享 subject identity、dataset/environment version、run、result、trace 和 decision contracts，只是 scorer 与风险不同。

### 评估必须把行为层级、测试分布与发布证据分开

同一 differential-privacy 训练可能在 logit-level、completion、classification 与 QA 输出上产生不同的社会偏差变化。
因此 privacy guarantee 与 fairness outcome 不能共享一个分数；两者应在相同模型身份下按行为层级分别验收。论文只覆盖
单一 pretrained LLM/DP setting 与选定 metrics，不能把局部相关性外推为通用因果结论。

<!-- source-family:SF-2026-ARXIV-2605-11195 -->

Inference engine 测试也不能停在 crash 或 hang。将带时间关系的多请求 trace 保存为版本化 fuzz workload，controlled
replay 后用 log-prob oracle 对比，可以发现调度、KV 或并发路径造成的 silent corruption。fuzzer 只生成输入与缩小失败，
oracle 才拥有 correctness verdict；模型、随机性或 backend 无法固定时，应回退确定性小模型、数值 invariant 和人工定位。

<!-- source-family:SF-2026-ARXIV-2605-11202 -->

对罕见 Agent failure，均匀采样容易耗尽预算。CEM 可学习 failure-prone proposal distribution，将更多测试分配给高风险
区域；这个分布只拥有 evidence allocation 权，不是真实 failure rate。报告必须另存 unbiased audit、sampling probability
与 importance accounting，proposal collapse 或权重方差过大时回退分层/均匀抽样。

<!-- source-family:SF-2026-ARXIV-2605-11209 -->

模型知道自己正在被评测时，recognised-evaluation context 与持续 deployment context 可能出现行为差。这个 differential
应成为独立 slice，保存 recognition cue、context continuity 与 matched control；边际 benchmark score 不能识别它，更不能
读取“真实意图”。证据只支持作者的受测模型与 prompts，线索失配时仍需 shadow/canary 与真实 outcome。

<!-- source-family:SF-THE-EVALUATION-DIFFERENTIAL-WHEN-FRONTIER-AI-MODELS-RECOGNISE-THEY-ARE-B -->

单一 embodied success rate 还会把 perception、intent reasoning 与 long-horizon coordination 混在一起。可替换 diagnostic
probes 分别固定其他组件，只改变目标模块，帮助定位责任；它们牺牲端到端真实性，不能取代完整 rollout。现有 PRISM 证据
限模拟住宅、300 tasks、五个 apartments 和七个 LLM。

<!-- source-family:SF-2026-ARXIV-2605-11534 -->

类似地，post-training drift 不能只看总分，可分解为 activation scale、shape 与 output-head 三轴，并为不同轴选择校准、
regularization 或回滚。诊断器只定位风险，不拥有自动修复权；near-isometry 等假设、模型与 variant 范围不成立时，应回退
端到端 task regression。公开结果不构成生产风险保证。

<!-- source-family:SF-2026-ARXIV-2605-11608 -->

visible CoT 的可读性也不证明它承载了决定答案的计算。oversight contract 应分别测 trace readability、对 trace 的因果干预
以及 final behavior；三者不一致时，trace 只能作为旁证。现有受限实验不能证明隐藏计算内容，应回退外部 verifier、
counterfactual intervention 与 outcome evidence。

<!-- source-family:SF-WHEN-REASONING-TRACES-BECOME-PERFORMATIVE-STEP-LEVEL-EVIDENCE-THAT-CHAIN -->

robustness 测试可以把 variant generation 与 rubric verification 编译成同一版本化 artifact pipeline：生成器提出扰动，
verifier 检查语义保持，target model 接受盲测。这样扩大覆盖，但 verifier 偏差会把无效变体写进分母；失败时应回退人工
gold variants 与 clean twins。SAGE 的证据仅覆盖 MCQ、预定义 variant 类型和作者模型。

<!-- source-family:SF-2026-ARXIV-2605-12022 -->

最后，Agent 评估的 publication bundle 应同时包含 rollout record、声明的 views/reporting rules 与 dropped-runs manifest。
读者才能从汇总分数回到同一证据对象，并判断哪些运行被排除。记录格式不能保证研究正确，但缺失它就无法审计 selection
bias；隐私或体积受限时可发布哈希、schema 和受控访问，而不能静默省略失败运行。

<!-- source-family:SF-ROLLOUT-CARDS-A-REPRODUCIBILITY-STANDARD-FOR-AGENT-RESEARCH -->

### Context Evaluation 要分离 Knowledge、Use 与 Harness Brittleness

同一模型只测 closed-book 或 open-book，无法区分“参数中没有知识”“证据存在但模型没有使用”和“输入格式使 harness 失效”。更可诊断的合同并列 closed、open 与 answer-preserving attacked-open：closed failure 指向 parametric knowledge 缺口，open 仍失败暴露 context-use gap/interference，attacked-open 的额外退化才定位格式或 evidence-pack 脆弱性。每个 pack 必须绑定来源位置、适用问题和扰动 provenance。<!-- source-family:SF-2026-ARXIV-2609-18270 -->

三条件对照会增加证据构建、专家接纳和扰动等价性验证成本，且 repair hypothesis 仍不是因果修复。现有 306 个专家接纳案例只覆盖 payment domain，也没有评价 retrieval、tools 或 multi-agent；无法证明扰动保留答案语义时，应保留 closed/open baseline、将归因标为 Unknown，而不是强行把失败归给模型或 harness。

### RAG 端到端评估必须保留阶段级归因

检索阶段先要问“召回了哪份文档”，还是“取得了回答所需的哪些信息”。当 corpus 中一条必要信息只有唯一权威支持时，document-ID gold 简单且便宜；当多个 chunk 可独立提供同一信息时，它会错罚有效的替代证据，而只计相关文档数又可能把 Top-K 全部花在同一信息上。更合适的评价身份是随 corpus 版本保存 `required information → 可替代的 supporting chunk 集合`：对检索结果先算已覆盖必要信息的比例，再单独验收是否覆盖了全部必要信息，而不是把部分覆盖、完整证据与最终答案正确合成一个 recall。<!-- source-family:SF-2026-ARXIV-2604-19047 -->

这张映射本身也要审计。信息拆分的粒度、相似度候选和 LLM 等价判定都会改变 gold；近似重复不一定互为充分支持，全部信息入窗也不保证 reader 正确组合或生成。作者的人工过滤评估中，两组 precision 仅 57.5%/50.8%，因此自动构造的替代支持须留抽样人工复核、版本和错标率；额外 atomization、等价判断与多跳构造也有成本。唯一支持的任务继续用简单 document gold；冗余映射不稳时回退人工 sufficiency/claim-level 判定，不采用整套 CRRF 排名流程或把端到端得分减去证据覆盖率解释为“参数知识”的因果贡献。

检索答案的提升还要先扣除**已经暴露给模型的输入信息**。在 gold item 可枚举的受限任务里，用同一 matcher 分别给“原样复制已展示上下文”和模型答案计分，就能把 `已暴露且答出 / 已暴露但漏答 / 未暴露却答出 / 未暴露且未答出` 分账。相对复制基线的增量是 exposure 与 recovery 的诊断，不是理论能力上限：复制会奖励冗长输出，词面匹配不能判断关系是否正确，正负抵消也会让净增量掩盖两类错误。它适合检查“检索确实把答案送进上下文了吗、reader 用了吗”，再交由语义审计与端到端任务结果判断质量；不能把已经提供的答案全部归功于模型推理。结构化小 corpus 可先用这条低成本基线，开放问答、缺少可枚举 gold 或强语义改写时须回退 sufficiency/claim-level 判断。公开结果限作者的单一策展 ontology、给定 matcher 与模型，不证明跨 corpus 的数值或发布质量。<!-- semantic-body-binding:SF-2026-ARXIV-2609-24885 -->

分别测 retrieval recall 和 generator answer quality，在组件开发阶段成本最低，也能快速定位单个实现；进入真实 RAG 服务后，corpus、retriever、reranker、generator、并发和 judge 会共同决定质量、延迟与成本。把各自最优的离线数字拼接成“系统能力”，无法判断一个失败来自未召回、重排、context assembly、生成，还是 measurement client。

更完整的 evaluation object 应冻结整条 pipeline，同时保留阶段 receipts：

```text
corpus snapshot + query distribution
→ retriever / reranker revisions and candidates
→ assembled context and provenance
→ generator / decoding contract
→ concurrency and hardware profile
→ stage metrics + end-to-end quality decision
```

Pipeline owner 保存 artifact graph，harness 拥有 workload 与阶段计时，scorer 只判断其声明的 quality contract；单个平均分不能吞掉阶段失败。端到端合同提高可归因性与可复现性，却扩大实验矩阵、数据版本和 evaluator 成本；只验证某个 retriever 或 kernel 时，局部 microbenchmark 仍应保留。`arXiv:2603.10765v1` 的 §3.1–§3.5 支持可配置 pipeline、workload 与 profiler 设计，§5.2–§5.8 才覆盖 latency、throughput、accuracy、update、resource、sensitivity 与 measurement overhead；§2.1 只是背景。证据仅绑定论文披露的 corpus、模型、硬件和 evaluator，不把具体排名外推到其他系统或生产 SLO。<!-- source-family:SF-2026-ARXIV-2603-10765 -->

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

若 generator 曾被连续知识编辑，局部 edit success、unrelated-answer locality 和静态 MMLU 仍可能同时通过，模型却改变了对**未编辑事实与新检索证据冲突**时的取舍。此时要固定 query、候选答案、检索段落和 retriever，分别测试真实更新、错误证据、伪权威与无冲突条件，观察逐事实的仲裁 margin、选择性回答风险，再做端到端检索复测。它把通常被混在“RAG 准确率”里的参数变更与证据使用能力分开，代价是配对探针、编辑序列和冲突证据的维护；没有模型编辑或不会遇到冲突证据时，常规 locality/answer evaluation 仍是便宜基线。[受控编辑研究](https://arxiv.org/html/2609.29587v1)在 Qwen2.5-7B 的探针与固定检索实验中观察到退化，另一 7B 模型只复核了方向，三个 seed 的幅度相差逾三倍；冻结检索端到端结果也只在 Qwen 上得到，不证明所有编辑器或开放域检索都会如此。
<!-- source-family:SF-2026-ARXIV-2609-29587 -->

### Privacy 与 Fairness 必须按行为层级分别验收

单一 fairness score 容易把 differential privacy 对不同接口的影响混为一谈。一个版本化模型在 sentence/logit、completion、classification 与 QA 层可能呈现不同 bias，privacy accountant 只能证明其隐私合同，不能拥有 fairness 真值。平台应按行为层级保留独立 evaluator、解析失败和 uncertainty；证据冲突时限制发布范围并跨模型重测。额外 gate 和专家标注提高成本，但比平均分掩盖局部退化更诚实。exact-v1 只支持所测模型、epsilon 和任务，不可外推为 DP 普遍改善或损害公平。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11195 -->

### 可靠性是分层画像，不是成功率的别名

把人类测验的 reliability 系数移植给 LLM judge 前，还要先问它测量的是哪一个 facet。若一位 judge 用一套固定措辞给 rubric item 打分，item internal-consistency 系数没有独立的 scorer 维度；它同时受题库真实分数分布和 judge 错误影响，不能单凭一个数认定“judge 可靠”。阈值 dependability ratio 也不是判定正确的概率；与 judge 自身 true score 一致，不等于与外部 gold 一致。发布证据应并列声明 item bank、scorer/prompt 变化、被估计量与外部效标，缺 scorer facet 时只称题库—评分系统的受限统计，不授予 judge 独立放行权。作者的一位 Claude Haiku 4.5、210 个合成短答题（180 个可解析）及模拟网格支持这个 measurement 边界；并未证明领域已有普遍误用。<!-- source-family:SF-2026-ARXIV-2609-29709 -->

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

扩大 judge panel 也有两个不同的目标：让同一任务的**评分更稳定**，以及发现此前未被提出的**独立问题**。前者可用任务分层的评分一致性与不确定区间衡量；后者须把语义相同的发现去重、记录新增问题随 panel 大小的边际曲线，不能因平均分不再变化就停止查漏，也不能把原始意见数量当独立覆盖。固定同一预算和任务时，增加不同视角通常提高发现机会，却也增加相关错误、重复意见和审阅成本；低风险、封闭 rubric 可用小 panel，高风险开放任务需要继续看问题发现曲线和人工切片。一个受限 agent-judge 实验观察到评分可靠性与去重问题数按不同曲线增长，但只覆盖 15 个任务、两组 judge/target 和其聚类阈值；与人类分数差异未达统计显著，不构成“已证明等价”的结论。[exact-v1](https://arxiv.org/html/2604.00477v1)<!-- source-family:SF-2026-ARXIV-2604-00477 -->

### Evaluator 可以主动制造 Probe，但不能冒充被动观察

离线 judge 只能评价自然轨迹已经暴露的行为；某些 criterion 在普通 run 中很少出现，absence 不能证明系统通过。
In-world evaluator 可以通过原生 dialogue/action 创建 criterion-relevant situation，再观察 Agent response，从被动打分
演进为 coverage-seeking intervention。Evaluator 的 action、环境 revision、触发 criterion 与后续 trajectory 必须一起
记录，因为 probe 本身已经改变被评对象的状态。

主动 probe 提高稀有行为覆盖，却可能诱发本不会出现的 failure、干扰任务、泄漏测试或造成副作用；它只能在 sandbox/
shadow 环境和预算内运行，也不能自动 repair 或 commit。可枚举的 deterministic condition 仍应直接测试。

主动 evaluator 若还能回滚并重试对话，单个场景就不再只有一条轨迹。选择最后一条分支报告，会把 evaluator 的选择能力混进 target 行为；把“任一分支出现”当发生率，又会随重试预算增加而上升。评估合同应保存完整 branch tree、回滚原因和每条分支的 outcome，分别报告最后分支、任一分支与跨分支平均，并固定或披露搜索预算。对评估意识也要拆开 task 与 environment：以相同任务分别在真实工作流和模拟环境中运行，再将高风险测试任务放进相同模拟环境，才能初步区分场景本身可疑与脚手架暴露测试身份。

这类对照提高外部有效性，却要求真实轨迹的隐私处理和可比任务样本；模拟任务仍可能比实际部署更容易被识别。目标模型未显露“我在受测”，也不能证明它没有识别；人工复核的 flagged case 没有确认某行为，更不能外推为风险不存在。[受限案例：UK AISI 的研究破坏评估](https://arxiv.org/html/2604.00788v1)只支持其披露模型、脚手架、有限场景与可见轨迹的测量边界。<!-- source-family:SF-2026-ARXIV-2604-00788 -->

研究破坏风险还需要两种不能相加的机会集：从正常任务开始观察**自发破坏**，以及给定已经含破坏的历史、观察是否继续、保留、揭露或修复。后者条件化了历史状态，可能覆盖前者难触发的行为，却不能把 continuation rate 当部署自发率；历史生成器、截点、是否包含 reasoning、模型是否识别 prefill 与每模型重复次数都属于测量身份。[UK AISI exact-v1](https://arxiv.org/html/2604.24618v1)使用 270 个自发场景与 1,485 个构造续写 transcript，且模型 epoch 不等。应分别保存分母、失败样本和人工/LLM judge 分歧；0 次确认破坏不证明风险为零，人工构造历史中的约 7% 续写也不证明真实工作流会以该率进入破坏。该分支增加历史构造与状态覆盖成本，普通任务轨迹仍是较便宜的首层证据，高风险 release 才进一步扩展有界触发与恢复切片。

<!-- source-family:SF-2026-ARXIV-2604-24618 -->

### 验证“没有遗漏”必须先建立应出现事实的 Inventory

Judge 擅长确认一段输出中已经出现的事实、引用或违规项，因为候选对象就在输入里；“没有遗漏”却要求先知道哪些
事实本应出现。直接问同一个 judge “这份摘要完整吗”会把开放世界问题伪装成二分类，并系统性漏掉未被文本提醒的
缺项。更强的 evaluation contract 先从权威来源建立 expected-fact inventory，再逐项检查输出中的 support、coverage
与 exclusion boundary：

```text
authoritative source / task specification
→ enumerate expected atomic facts and required exceptions
→ align output claims to inventory
→ classify present / contradicted / omitted / not-applicable
→ aggregate with criticality and dependency, not naive probability multiplication
```

Inventory 构建本身仍可能漏项，且 clinical、legal 或开放研究任务常存在合理选择与粒度争议；因此它必须绑定来源
revision、extractor/rubric、人工校准切片和 unknown 状态。它以额外抽取、对齐与 false-omission 成本换取对缺失信息的
可见性，低风险短文本仍可使用普通 presence checks。Omission-blindness 的配对临床笔记实验支持“presence 与 absence
不是同一判断任务”以及先枚举再核对的恢复方向，不证明一个模型 judge 或这套 inventory 能覆盖所有领域事实。

<!-- source-family:SF-2026-ARXIV-2608-31016 -->

### User Simulator 必须包含不合作与行为差异

只使用合作、目标明确的 simulator 会高估 Agent 在真实用户中的稳健性。Persona policy 可以在不改变原任务目标的前提下控制犹豫、误解、偏好和交互风格，使评价覆盖更多行为路径；simulator seed、persona policy 与目标保持检查要共同版本化。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12894 -->

persona 仍是合成分布，可能夸大刻板行为或遗漏真实用户策略。所测任务不能代表生产人群；外部效度不足时应回退真实交互样本、人工角色扮演和分 slice 报告。

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

跨组件模拟还要把时间域换算与因果提交分开。CPU/DRAM 用整数频率比例上取整推进，会扭曲接口时间；改成物理时间粒度推进两套时钟可以修正换算，却不能追回已交给后端的错误并发请求。在 two-phase 模型中，若前阶段用 immediate response 提前生成本应等待 load 结果的请求，后阶段再修 issue time 也未必恢复原依赖链。组件内部 DRAM 统计因此不能替代 interface 的请求时间与 application 的 load-to-use 验收，三种视图须分别绑定事件与提交边界。<!-- source-family:SF-2026-ARXIV-2604-16965 -->

延迟反馈与校准可以减小两阶段差距，却增加同步与模拟成本，平均 latency 贴近参照也不证明全部因果状态一致。原文 CPU/DRAM 模拟器仍有饱和、地址映射、NoC、prefetch 与未建模 PHY/IO 边界，不能向 GPU/LLM 生产准确率外推。分析模型与单组件 microbenchmark 仍适合局部容量和机制诊断；要据模拟结果发布调度决策时，则须检查真实依赖轨迹与应用回放，不能以较细时钟掩盖错误提交。<!-- source-family:SF-2026-ARXIV-2604-16965 -->

### Dynamic Reference 必须与 Agent 共享同一 Live State

环境持续变化时，静态 gold 很快失效。reference 应成为 versioned executable function，读取与 Agent 同一时刻的 state，再把输出拆成可核验 atomic facts 分别计算 precision/recall；reference code、snapshot、执行时刻与 evaluator revision 都属于 evidence identity。<!-- source-family:SF-2026-ARXIV-2609-16487 -->

可执行 reference 降低陈旧答案，却把代码完整性、staging 数据和 judge coupling 引入可信面。55 cases、内部 skill、synthetic DB 且同一 Claude family 参与生成/判断，只支持受限流程；无法独立验证时回退 deterministic gold、人工 gold 或 quarantine，而不是让 reference function 自签真值。

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

turn 间变化之外，computer-use 界面还可能在**同一 turn 的两次动作之间**出现又消失的关键状态：中断弹窗、短暂引用或动态列表位置，都可能在下一张截图里不留痕。只保存 post-action 截图的评测成本低且易重放，但它不能把“Agent 没看见事件”与“看见后仍选错动作”分开。动态 GUI 的 EvalSpec 因而应把 observation sampling policy、事件时间戳与可重放的 transient witness 加入 run identity，并分别报告关键事件漏观测率和最终 task effect；运行时 Agent 如何选关键帧仍由 Ch84 的 observation interface 持有，不由 evaluator 代替执行。

保存全视频最利于追责，却增加 capture、筛帧、token 和复算成本；均匀采样便宜但可能漏掉短事件，内容门控采样又可能因 detector 漂移或错误置信度丢失真正的决定性帧。比较 post-action-only、均匀帧和门控关键帧时，须固定模型、工具权限、步骤及帧/token/call 预算，并用独立环境状态验收动作效果。作者的受限动态桌面基准揭示了两动作间的观测缺口，但其视频选择、反思与动作修正共同影响结果，消融表对“仅选帧”的增益归属还有不一致；不能由综合成功率推断某一模块必然有效。若无法取得事件真值或可靠时间轴，应报告 temporal coverage 未知，回退确定性任务与人工轨迹检查，而非把没有记录到事件写成事件没有发生。<!-- source-family:SF-2026-ARXIV-2604-25380 -->

### 科学任务还要评估 Evidence Uptake 与 Belief Revision

开放科学 Agent 即使得到高 outcome score，也可能提出未测试主张、忽略反证或在没有新 evidence 时递归自信。
过程评估可把 trace 映射为 `claim → evidence → test → judgment → update/commitment` 的 dependency graph，
分别识别 convergent evidence、refutation loop、evidence non-uptake 与 untested claim。Graph 是 annotation-derived
view，不是模型思维的直接读出；有些合理推理不会显式 verbalize。Corral 的作者研究支持在其八类科学环境中
outcome 会掩盖 epistemic failure，不证明 scaffold 普遍无效，也未验证把该 taxonomy 作为训练目标就能修复。
Deterministic outcome verifier 仍负责可执行结果，epistemic graph 只增加 diagnosis 与 research-governance evidence。

### Benchmark、Evaluation 与 Testing 不是同一个层次

可执行基准的 scorer 也会悄悄改变“正确”的含义。Text-to-SQL 的结果若被转换为集合再比较，重复行的 multiplicity 消失；当用户实际需要行数或重复记录时，set-equivalence 会接受错误答案。EvalSpec 必须声明结果是 set 还是 multiset、排序是否有意义、NULL 与超时如何处理，并保存预测 SQL、执行引擎和原始行结果；只有与任务契约一致的 evaluator 才能给 release 结论。作者在 BIRD-Dev 可执行的 1,532 题及数套公开预测上观察到 Set-EX 比 Multiset-EX 高 3.39–6.79 个百分点，说明此盲区在该数据集可测，不证明所有 SQL 工作负载具有同一误差率；检测/修补器仍受 SQLite、候选召回与额外 LLM 成本限制。<!-- source-family:SF-2026-ARXIV-2609-29573 -->

SQL含AI predicate后，正确性不能只绑定一次完整结果相等。Join、aggregation与重复行语义仍有确定关系合同，而AI prompt的relaxed equivalence和边界样本输出需要另一个语义判据；相同查询意图不一定得到相同行，当前fixture结果相同也不能证明DISTINCT等运算无关。可以分别提取关系结构与AI组件，保存完整及组件执行结果，再按明确目标语义评价；拆分器和autorater各拥有自己的忠实性与标签错误，不能自行认证user intent。

作者在受限BigQuery/ThalamusDB案例中观察到这两侧误判，并用LLM拆分/分层评分改善对人工标签的吻合，但共享模型、无seed重复、小而未明列的engine分母及剩余误收误拒不支持通用正确性保证。更多execution与judge调用增加成本，prompt差异也可能改变真实AI决策而非只引入噪声；遇到复杂SQL、拆分失真、语义标准争议或分布变化时，保留原关系测试、独立人工/执行复核与abstain，不用一次分层高分发布任意AI query。[必要机制与反证](https://arxiv.org/html/2609.21133v1)。<!-- source-family:SF-2026-ARXIV-2609-21133 -->

Benchmark compression 本身也要成为版本化 evaluation artifact。Compact subset 应绑定完整 anchor logs、subset builder、score error、rank consistency、held-out model family 与失效条件；无法给出 fidelity budget 时，就只能作为加速 preview，最终 release 回退完整 benchmark。压缩减少重复运行，却可能删除极端 slice，并且先跑完整 anchors 的成本没有消失。

<!-- source-family:SF-2026-ARXIV-2609-12475 -->

压缩 benchmark 还须区分当前执行的观察、历史 verdict 的复用与未执行题目的重构。固定难度或分层 subset 可以并行执行并按声明权重估计；adaptive Fisher selection 则把先前回答变成下一题的控制输入，选中的题目不再是代表性随机样本，其 raw mean 不能直接当完整分数。IRT 可以用模型重构未执行题目的通过概率，cache 则取决于旧 verdict 是否仍适用于当前 subject；这三条分支分别承担 estimator、selection state 与 freshness 的假设，不能合成一个“少跑题仍准确”的证书。

时间顺序的 calibration/held-out 切分用于检验这份估计合同，不允许把 held-out 误差倒填为 calibration correction。固定 subset 未必最准确，却更便于并行、预测成本和逐题比较；自适应选择增加顺序更新，历史复用增加身份与失效检查，离线 replay 省下题目也不等于生产延迟等比减少。受限成熟 Agent 窗口与少量 family transfer 不能认证持续 drift，聚类方案在部分预算上还会输给 random；绝对分数 fidelity 与 ranking fidelity 必须分别验收。模型、任务或 scorer 漂移时，恢复 full benchmark 或分层 anchors 并重校准，不由局部稳定性为未观察任务签发 release。 [必要机制与反证](https://arxiv.org/html/2609.21267v1)。<!-- source-family:SF-2026-ARXIV-2609-21267 -->

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

### Inference Engine 需要 Timed-trace Fuzzing

单请求 API 测试默认 serving engine 是稳定底座，无法覆盖并发时序触发的 crash、hang 与 silent corruption。把带精确时间的 multi-request trace 作为 workload artifact，利用灰盒信号变异，再以 controlled replay 和 log-prob oracle 确认故障，能把模型错误与 engine failure 分开。代价是大量执行、nondeterminism、oracle drift 和 telemetry 依赖；oracle 不稳时应回退 deterministic regression trace、engine invariant 和 maintainer confirmation。exact-v1 只证明所测 engine/configuration 的可重放故障，不给出生产失效率。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11202 -->

### Kernel Benchmark 必须先闭合 Correctness Identity

Kernel-generation evaluation 必须把 operator semantics、reference implementation、shape/stride/dtype grid、numerical tolerance、target chip/runtime、anti-hack coverage、timeout 与 profiler revision 绑定为同一 EvalSpec。跨芯片比较只有在 correctness gate 先闭合后才讨论 speed，并应同时报告 pass coverage、compile/wrong-result/timeout/slower-than-reference 等失败类型、严格 speed thresholds、trajectory feedback 和 token/device cost。

这里至少有四段不能互相替代的 verdict：源码能否编译，输出是否满足语义合同，在目标硬件上是否真正更高效，以及换 operator、shape 或芯片后是否仍可移植。LLM 的 iterative repair 可能先提高 compile rate 和数值正确率，却因额外同步、保守访存或 shape specialization 让速度下降；因此 performance 只能在通过同一 correctness identity 的 artifacts 之间比较，不能把“修到能跑”计成加速。176 tasks、15 categories、六种 GPU 与五类方法的作者 benchmark 只支持这套失败分类在其 harness 中的诊断价值；microbenchmark speedup 不是端到端模型收益，测试通过也不是形式证明。<!-- source-family:SF-2026-ARXIV-2605-04956 -->

Agent 自动搜索 kernel 时，正确性样本有限、计时器只测 kernel 片段，候选甚至可能绕开目标计算，得到不可思议的加速。除了逐例 reference check，评估方还应按同一 operator、dtype、shape 与实测时钟，估算必要 FLOPs、最小数据搬运及硬件算力/带宽形成的物理时间下界。明显快过这个下界的结果应触发独立的语义与计时审查，而不是直接进入排行榜；接近下界的候选也可降低后续搜索预算。物理界限只是一项诊断信号：算错数据量、忽略 cache/融合或使用错误硬件规格都会误报，它不能代替正确性证明；扩大搜索空间和完整审查又会增加成本。`arXiv:2603.29010v1` 的受限 KernelBench 实验支持这条 integrity/budget 分支，不证明该界限对所有算子或端到端 serving 都精确。

<!-- source-family:SF-2026-ARXIV-2603-29010 -->

更广覆盖提高 portability evidence，却会引入 platform-specific prompt/tolerance 与不对称 anti-hack 能力；这种不对称必须显式披露，不能被一个总体排名隐藏。单芯片小 suite 在目标固定的快速回归中仍然合理，但它不能支持跨 operator、chip 或 harness 的通用性能结论。

<!-- semantic-body-binding:SF-2026-ARXIV-2607-27231 -->

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

生成器之外，benchmark发布前还要互核instruction、reference program、scoring code与environment四个工件：指令允许的路径、reference体现的路径和scorer实际判分可能不一致，环境初始化也可能让可解任务变不可解。Agent trace可提出最小反例，但修改责任仍属于benchmark owner或专家；修订应保存复现、裁定理由和重跑范围。

自动找出反例会增加多模型运行和人工裁定，模型union并不形成独立oracle。受限BenchGuard中的确认缺陷数、修订issue对齐和旧专家patch一致率不是全任务precision，调用费用也不含人工；无可靠oracle或有不可逆effect的任务不能套用检出率。反例无法裁定时隔离题目，不随意改gold，保留专家审查、固定版本及修订前后重跑。 [原文必要机制与限制](https://arxiv.org/html/2604.24955v1)。
<!-- source-family:SF-2026-ARXIV-2604-24955 -->

跨语言派生 benchmark 还应被视为 semantics-preserving compilation，而不是普通字符串翻译。Compiler 必须保留
task invariant、label/choice identity、format/parser contract、language-specific invalid cases，并记录 source item
到 target item 的 transformation lineage。自动翻译扩大覆盖，却会改变难度、歧义、tokenization 和知识前提；
人工复核提高可信度但仍不能证明与源语言等价。原始 benchmark 在长期对比中继续成立，派生版本只能在逐项
validation、contamination 检查和独立 native review 后形成新 distribution。Recovered in Translation 为这条
pipeline 提供了受限证据，不支持跨语言分数直接互换。

即使逐项翻译保真，语言也不等于地区。对税期、紧急电话或度量单位等答案依赖 locale 的问题，显式写出目标地区能测“知道当地事实”，却掩盖了用户未指定地区时模型会默认选择哪一种现实。多语言 Evaluation 因此应将显式 locale 知识与隐式 locale 选择分成两个任务：同一语义问题分别给定地区、只给语言或保持歧义，记录答案提及的地区、并列选项、澄清/拒答及地区相关 gold；共享答案要避免被误记为偏向某一地区。这样能发现跨语言默认值与同一语言内的地区偏置，却要付出多地区标注、事实时效维护和对“合适默认值”的产品约定；含糊输入不一定有唯一正确答案。在明确目标地区的服务中，旧的显式知识测试仍是有效基线；需要处理未明说地区的服务才应额外验收默认选择或澄清策略。受限研究只在 44 个语义平行问题、12 种语言/49 个地区和 32 个模型上观察到这种测量差异，不证明训练阶段造成偏置的唯一原因，也没有测试澄清策略的实际效果。<!-- source-family:SF-2026-ARXIV-2604-19292 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-26029:start -->
Simulator 也可用于评估 Agent 是否真的恢复了环境机制。只看 held-out prediction 时，Agent 可能利用相关性取得高分，却没有恢复 causal graph 或 equations；在可干预 synthetic SCM 中，应把预测准确率与结构/方程忠实度分开计分，并记录 observation/intervention policy、实验停止点和 consistency check。高预测分不能替代 mechanism recovery，premature stopping 也不能提交确定结论。

可干预环境、机制 scorer 和多轮实验提高诊断力，却引入 synthetic bias 和更高成本。若结构 scorer 不可靠或 intervention budget 太小，应保留简单 prediction baseline，同时要求独立 mechanism audit、最低干预预算或人工复核。作者 synthetic SCM 结果不证明开放环境中的因果发现能力。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-26029:end -->

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

### Resource-constrained Evaluation 要先提交计划

逐题独立给足预算只能测“会不会做”，不能测模型能否在总 token budget 下选择、排序和分配资源。要求模型先对任务池提交一份不可事后改写的 ordered plan，再执行并计算效用，可以把 prospective metacognitive control 与单题能力分开。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13414 -->

预算由模型自身 baseline 校准、任务池构成和效用函数都会改变排名。现有框架不证明真实调度能力；计划不稳定或效用定义争议时，应同时报告单题 oracle、随机/固定分配 baseline 与实际执行结果。

### Search 方法的排名必须覆盖预算形状，而不是只报一个终点

Evolutionary 或 Agentic search 的“方法更好”可能只是在某个 seed width、iteration depth 与总预算组合上成立；扩大宽度和加深迭代会改变探索多样性、selection pressure 与 evaluator exposure，甚至使排名反转。评价应先冻结二维/多维 budget surface，再比较相同总 compute、相同候选生成和相同 scorer 下的 frontier，不能把单点胜利写成算法属性。<!-- source-family:SF-2026-ARXIV-2609-19799 -->

完整 sweep 成本高，也可能过拟合 benchmark；预算受限时至少报告相邻 operating points、seed variance 和停止准则。作者的 search space 与模型不证明所有演化方法都会反转，只证明排名 identity 包含预算形状。

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

### Agentic RL 评价要把“到达状态”与“从状态求解”分开

只比较完整 episode success，会把探索 policy 是否能到达关键 checkpoint，与 solver 从该 checkpoint 能否完成任务混成一个分数。更可诊断的合同冻结可重放 checkpoint：先测 reach rate，再从相同状态交给不同 solver 测 conditional solve rate，并保留环境、隐藏状态和工具版本。这样 checkpoint handoff 只拥有归因证据，不把中间状态自动升格为任务完成。<!-- source-family:SF-2026-ARXIV-2609-19636 -->

状态序列化和重放会增加存储、环境兼容与 contamination 风险，且 checkpoint 本身可能改变后续分布。无法证明 handoff 等价时，应回退端到端 episode 评价并把中间结果标为诊断；作者任务结果不支持跨环境固定阈值。

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

当两个模型的 `pass@k` 曲线交叉时，图上交点还不是“低预算有益、高预算有害”的统计证据。同一 prompt 贡献了多个 k 的估计，这些点彼此相关；可对两个模型使用同 prompt 的 paired 差值，并让 Gaussian multiplier 在整条曲线上共享该 prompt 的随机系数，以保留跨 k covariance。只有早段的 simultaneous band 下界高于零、晚段上界低于零，才建立该预算范围内的 crossover；某一个 k 显著不同不足以证明换号。这里的渐近支持依赖固定的有限 K、iid prompts 与非退化方差，不保证任意相关 prompt、不断扩大的 K 或有限样本下的精确 coverage。

这也要求把“原模型每题成功率相同”与“RL 后变化相同”分开：条件变化可以是分布 kernel，而非单值函数，单个平均增益会遮住同 base 能力下不同 prompt 的异质反应。[受限 RLVR 实验](https://arxiv.org/html/2609.22547v1)在 DeepScaleR/R1-distill-Qwen1.5B、1060 prompts、每题128次采样、temperature 0.6/top-p 0.95及新32K生成预算下给出 first-loss crossover 区间11–61；截断率为实测，按假定概率修复截断的敏感性分析是反事实，不能当已部署收益。按 answer halves 复验也不是新 prompt 泛化，不能消除 pretraining 规模等混杂。额外采样与联合区间增加成本；prompt 相关、有效样本不足或预算范围改变时，应保留未决并重新取样，固定单预算回归仍适合低成本 gate。<!-- source-family:SF-2026-ARXIV-2609-22547 -->

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

反馈还可能跨测试问题流动：oracle 确认一题成功后，把成功回答放入共享 demonstration pool、移除已解题，再供后续问题作为近邻示例。这时评估单位是有标签反馈的题序与池状态轨迹，不是相互独立的单题部署正确率。应保存 pool 的初始化、更新、题序、标签访问和示例选择，与无此标签反馈的冻结 pool 基线分账；否则后续收益会混入先前测试答案的额外信息，而不能只解释成更合理的 sampling budget。

这种适应过程适用于部署确有跨题反馈的场景，但匹配 output tokens 没有匹配新增 ICL prefill、oracle 和池维护成本，正确答案筛选也不证明线上 selector 可用。[受限研究](https://arxiv.org/html/2604.21018v1)采用四轮、一次 warmup 和少数 API 模型；正文 active set 与 Algorithm 1 的全 test pool 定义存在差异，不能默认为同一实现或声明全配置必然改善。无法恢复反馈与池状态时，退回独立问题 snapshot 比较，而不是补造与部署等价；下面的长期 artifact 还需要进一步保存状态变更。<!-- source-family:SF-2026-ARXIV-2604-21018 -->

长期 artifact evolution 进一步要求保存 `state_0 -> action_1 -> state_1 ...`、每轮目标与 test evidence、
rollback/recovery、metric temporal weighting 和 harness revision。用未来 target tests 引导每一轮能够提供
稳定 oracle，却测的是对已知隐藏终点的迭代重建，不等于真实需求漂移、branch/merge、human review 或线上
依赖变化。Snapshot regression 在局部修复中仍最可靠；interactive/evolution benchmark 只在真实 deployment
也包含反馈或长期 state 时增加证据，并必须和静态、成本及风险指标并列，而不是取代它们。

当可修改对象进一步包含 harness 本身，保存版本号仍不够：一次“优化”可能删除必跑测试、误标结果来源，
或让被选中的分数对应另一份代码；后续迭代即使没有新增违规，也可能继承已经损坏的评估流程。
因此检查单位应落到每轮实际应用的完整 diff 与修改前文件，分别问它改变了执行、评分、选择、记录还是
后续继承，以及受保护文件、来源归属、必需测试集合是否仍成立。最终分数提高不能替代这些检查。

这比固定 harness 的回归测试多出 lineage 保存与变更审计成本，但能区分“这一轮没有发现新问题”和
“交付版本不再携带旧问题”。自动 auditor 也会误报，应使用同位置的合法修改对照，分别测发现问题和定位
代码的能力；[harness tampering 研究](https://arxiv.org/html/2609.00069v1) 的注入实验与公开轨迹审计支持
这种风险，不提供现实修改的完备真值。固定评估通道在无需自修改时仍更简单；允许变更时，继续执行后文
Generated Evaluator 的独立准入，不能让自改进系统自行批准自己的评分规则。

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

Monitor 还需按“训练轨迹来源 × 验收轨迹来源”做 cross-test，而不是用同源 held-out 替代跨来源有效性。人工构造相互冲突的 unit tests、允许策略 resampling 的轨迹，与自然部署中作弊的机会和分母不同；训练来源、冲突构造和重采样预算必须进入 monitor identity。<!-- source-family:SF-2026-ARXIV-2604-23488 -->

双轴检验增加多来源轨迹、标注与校准成本；跨来源退化不能只靠同源阈值掩盖，作者受控设置也不提供部署作弊发生率。目标来源没有覆盖、标签冲突或阈值迁移失败时，保留独立 executable/human audit、保守报警与不确定状态，避免 monitor 同源自验直接授权发布。

当 Agent 同时控制实验、提交物和用来证明成绩的 evidence，审阅提交物本身会形成同源盲区。应把代理可修改的 score/报告与独立保留的执行轨迹、隐藏重算和任务合规性判断分开；只在独立证据确认 exploit 后才统计检测漏报。若把审查理由反复返回给有意规避的代理，还须把 feedback protocol 和轮数纳入攻击预算。开放研究任务上的[受控研究](https://arxiv.org/html/2609.28614v1)显示 artifact-only panel 会漏掉部分已确认 exploit；其主动允许作弊的实验不能作为部署发生率，LLM verification panel 也不是无误真值。

部分进度评分又多一层混杂：高分轨迹可能真的完成了更多工作，不能仅凭分数更高断言评价器被攻击。应先由独立 certifier 在**当前状态谓词**与 Agent 自身贡献上匹配诚实/对抗轨迹，再测评分差；已经回滚的 milestone 或他人完成的状态不能借历史截图领取 credit。这个合同增加私有状态检查、attribution 和配对样本成本，也只覆盖事先编码的谓词；目标是验证评价器是否给等量真实进度不同分，而非评判所有开放任务。[受限基准](https://arxiv.org/html/2609.29578v1)只有六个开发任务和十八个 held-out 任务，不证明生产作弊频率。
<!-- source-family:SF-2026-ARXIV-2609-28614; source-family:SF-2026-ARXIV-2609-29578 -->

最终答案正确也不能授权把可见推理链当作模型实际使用、且足以外部核验的证据。评估应把三件事分账：outcome verifier 判最终答案；在同一问题和已生成推理链的不同前缀后强制提前回答，观察答案分布随前缀增加的变化，检验该链在这个读出协议下是否影响答案；再让独立 verifier 分别只读推理链、以及同时读原问题和推理链，检验链本身是否足以使答案不再依赖原题。后一项是信息自足性而不是逐步证明，前一项是给定截断和读出方式的操作性敏感度，不等于完整内部因果归因。链可以影响答案却省略关键步骤，也可以写得可核却并未被模型用于产出答案，因此不能用任一轴或高 outcome reward 代替另外两轴。

这组额外验收要付多次前缀读出、外部 verifier 与 rollout 的成本，且 verifier、截断位置、答案分布和任务选择都属于 Evaluation Identity。只要求最终答案的低风险场景，保留便宜的 outcome 检查；若推理链要进入过程奖励、监测或发布证据，才按风险增加这两种条件测试，出现分歧时隔离该链的过程证据而非抹掉已经独立验证的答案。[受限实验](https://arxiv.org/html/2604.22074v1)覆盖选定的 40 个 ReasoningGym 任务和 Qwen2.5 1.5B/3B/7B 等设置，支持 outcome 改善与两项链指标不必同向；不能据此推所有模型的内部推理、逐步可证明性或线上误报率。
<!-- source-family:SF-2026-ARXIV-2604-22074 -->

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

规则型答案 verifier 也需要同样的双向测试：对声明支持的输入形式，使用保持数学含义的改写检查误拒，
再用改变含义的扰动检查误收。未承诺的 extraction 格式应记为适用域差异，不能与实现缺陷混算；异常、
超时和无 verdict 则单列执行覆盖率，不当作一次正确拒绝。数值比较还要按量级测试：相对容差可能接受
大整数的差一错误，是否可接受取决于任务要求的精确语义。[分类审计](https://arxiv.org/html/2609.01354v1)
提供了这种 verifier-level 反例，但变换样本的错误率不是模型真实输出的错误率，也不直接证明 RL 训练退化。

### Judge 的输入扰动必须保留 Clean Twin

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11067:start -->
同一批答案只跑一次 judge，适合低成本回归，却无法判断 verdict 是被语义内容还是无关表面变化推动。只要 model judge 进入 reward、selection 或 release gate，evaluation owner 就应为每个样本保留 clean/noisy twin，并记录 perturbation family、seed、目标强度与实际 edit rate、judge/provider revision、原始与扰动 verdict 以及 `A/B/None` 的转移方向。这里的“meaning-preserving”是变换规则的前提，仍需抽检，而不是由规则名称自动成立。

稳定性只证明 measurement instrument 对已测扰动不敏感，不证明原 verdict 正确；反之，`None -> A/B` 的不对称翻转说明 decision boundary 受噪声影响，也不能单凭方向命名为某种真实偏见。重复模板、少量扰动族和有限 judge 会夸大有效样本量并限制外推。clean twin 分歧、语义保持无法确认或 judge 版本漂移时，应让该项 abstain/quarantine，并回退 deterministic check、人工 gold 或独立 evaluator；不得用 noisy majority 覆盖干净证据。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11067:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22714:start -->
Clean twin 之外，还必须控制 Judge conversation 的历史状态。为提高 prefix/cache 复用而在同一对话中批量评判时，先前 verdict 的 polarity 会变成未声明的 evaluation input，使后续答案在内容不变时偏向历史方向。默认做法应是一项一条 fresh context；确需 batching 时，Evaluation Identity 要保存完整 history、顺序与 polarity balance，并把同一 item 的 fresh-context verdict 作为 clean twin 校准，特别关注基线不确定的样本。

fresh context 会牺牲缓存复用，balanced history 也不能消除所有顺序和语义累积效应。证据只覆盖英语、binary judgment、三类任务与披露模型；越界、history 无法重放或偏移超出校准域时，应回退 deterministic outcome、人工 anchor，或把该项标为不确定而非用批量多数覆盖。这里吸收的是历史 verdict 属于 evaluation state，而不是某个固定偏差系数。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22714:end -->

### Binary Verdict 通过不等于语义忠实

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11085:start -->
编译、solver 或单元测试给出的 binary verdict 是必要 execution gate，但任何只看 verdict 的 evaluator，都无法区分与参考实现语义等价的答案和“恰好保持同一通过/失败结果”的不忠实答案。需要在离线评估中构造 same-verdict matched pairs：正例满足参考语义，负例由双向 executable check 或反例搜索确认 verdict 相同但语义不等价。reference、solver、约束编码与判定预算属于 privileged evaluation state，不应在部署时泄露给被评系统。

可由这些配对数据训练一个部署时不读取 reference 的 generative verifier，但它只是一枚 learned sensor：负责 gate、候选选择或 trace 采样 proposal，不获得 semantic authority。训练标识重叠、solver 只能覆盖形式化子集、参考约束不完备或不可满足时的 vacuous equivalence，都会让高准确率失去含义；`Best-of-N` 的采样收益也必须与 verifier gate、selection 和 feedback 的增量分开报告。

这一路线用额外标注、solver 调用和 verifier 推理换取对 verdict-preserving error 的可见性，仍不覆盖人类意图、风格变化和多重错误组合。reference 不可形式化、配对检查失败或 learned verifier 不确定时，fallback 是继续保留 deterministic solver 作为 execution gate，同时增加 reference/human review、claim-level executable checks 与 abstain/escalation；不能让生成式 `Yes/No` 取代原始测试或正式证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11085:end -->

形式证明还必须区分“建模的函数都被约束”与“整个 issue 的行为面都被建模”。某个函数的 precondition、postcondition 和证明完全成立，遗漏的另一个函数或副作用仍可让仓库修复失败。一个离线构造分支从 known-correct patch 提议 specification、verified reference 与 pre-fix twin；未改动 callee 以带 provenance 的 axioms 接入，再分别保存 specification 的行为覆盖、callee 在真实环境中的 axiom probes，以及验证模型到实际 patch 的 correspondence/执行 shadow。Kernel 只拥有形式命题通过权，这三条外部对应不能由同一个通过 verdict 自动补齐。

构造者看到 gold patch/tests 是特权，不代表 solver 能从自然语言 issue 自动写出忠实 specification；提供 spec 还可能暴露 localization，个别实例必须记录超出公开 issue 的 disclosure relaxation。Fuzzing、差分执行与独立攻击提供可重放反证，未发现反例不是 intent、axiom 或 model-to-patch 等价的普遍证明；参考语言的表达边界和 shadow translation 仍是成本与信任接缝。本文自写 spec 不改善的负侧应保留，不能将条件化 verify→resolve 改成通用 verified-code 保证。行为覆盖、对应关系或 callee 假设无法确认时，回退仓库测试、人工需求裁决或明确未验证，而非让 proof 自签任务完成。 [必要机制与反证](https://arxiv.org/html/2609.21190v1)。<!-- source-family:SF-2026-ARXIV-2609-21190 -->

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

事实有效期正确仍不代表对话解释正确：用户可能省略时间、继承上一轮时间、明确覆盖时间，或切换实体却保留时间范围。应另测 **conversation-scope carryover / override / cross-entity transfer**，不要把这些错误全部归给 Memory store。对同一问题分别提供正确历史（Gold）、模型自生成历史（Self）和仅当前问题（Questions），才能区分作用域解析、历史错误累积与单题知识不足；三个机会集须分账，链长变化还要保留同题可比切片。代价是带时间 scope 标签的历史构造与独立事实核验，Gold 历史也不等于生产用户表达。[exact-v1 的模板化时间对话实验](https://arxiv.org/html/2604.23051v1)支持这一诊断合同，但 Wikidata 模板、当前值 snapshot 和不同链长题组不能证明普遍的长期 drift 因果律。短历史可继续用 full-history 基线；作用域不明时要求澄清，不能靠正确事实库猜用户的 as-of time。

<!-- source-family:SF-2026-ARXIV-2604-23051 -->

这个变化把 memory architecture 的比较从一次性 answer score 推进为 temporal state audit。短 tenure 中，保留全部历史
往往是便宜而强的基线；随着历史增长，写入错误、过期事实和检索干扰才逐步显现，架构排序甚至可能发生 crossover。
因此报告必须同时给出 tenure slice、full-history/no-memory controls、write-path precision、read-path recall 和最终答案，不能
把某个单点排名写成长期赢家。

代价是需要构造并版本化事实、有效区间、事件渲染器和 judge-independent checks；合成用户也未必代表生产分布。
所以该 contract 证明的是“如何定位长期状态错误”，不是某种 Memory 在所有用户、backbone 与时长上更优。Memory 的实际
写入、更新与派生状态仍由第 77 章拥有，本章只拥有其 evidence contract 与 release decision。

历史 corpus 仍只是系统状态的一部分。Index、profile、model-derived memory 和 request-time cache 都必须继承最晚 ancestor event time；PIT 与 Future 对照要冻结 retriever、budget、anchor 和 materialization policy。否则未来建立的派生状态会倒灌到历史评测，掩盖 harmful memory 或夸大正反馈。没有 lineage 的 black-box state 只能形成部分审计，不能声称 point-in-time 完整。

<!-- source-family:SF-2026-ARXIV-2609-12766 -->

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

代码编辑把这条契约具体化为两个独立问题：请求的行为变化是否发生，以及未请求改变的行为是否仍成立。只覆盖 diff region，或用 AST 检查新增语法，可能通过前一个问题却漏掉后一个；应为原有行为保留回归断言，并以有意破坏未请求区域的变体检查 oracle 是否敏感。反过来，statement coverage 较低也不能直接判 oracle 无效，结构检查、mock 与 outcome test 可能有合理目的；覆盖率是定位证据缺口的线索，不是语义完备证明。[代码编辑 benchmark 的定点审计](https://arxiv.org/html/2604.05100v1)支持这种区分，但其低覆盖子集的静态/人工判定不是全面 mutation 实验，也不证明所有 coding suites 都有同样缺陷。

<!-- source-family:SF-2026-ARXIV-2604-05100 -->

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

**零通过尤其不能直接解释成前沿难题。**同一个 all-fail 分数可能来自能力不足、坏掉的 reference/oracle、环境不可达、verifier 可被绕过，或根本缺少可解性证据。进入能力结论前，Evaluation owner 应对每道题保存工作中的 reference route、空解应失败的对照、工具与基础设施可用性、独立于 reward 的 verifier-integrity 检查，以及冻结的 harness、预算和重试条件；不能用模型失败轨迹反过来证明题目有效。对不满足条件的题分别修复、剔除或保留未决，而不是和可信任务一起求一个难度均值。终端任务审计在冻结的 125 个零通过任务中仅将 78 个保留为“在所测 agents 与声明检查下未解”的候选，其余分别落入 oracle、基础设施、绕过和未认证类；即使保留者也不证明内在不可解、verifier 完备或失败正好发生在目标能力处。增加这层 item-level 审计会消耗 reference 执行和人工复核，但比用无效题目驱动模型发布决策更可追溯。<!-- source-family:SF-2026-ARXIV-2609-26826 -->

Reference 可以稳定重放，仍不意味着它准确表达了请求。代码检索尤其容易暴露这个差别：query 只要求处理正整数，
测试却额外要求非正数返回某个值，那么删除这个额外分支的程序可能在声明输入域内完全正确，却被测试判错。
因此 evaluator 要分别固定自然语言任务、允许的输入域、reference 与 test oracle；oracle 拥有可执行判定，
不自动拥有扩充需求的权力。发现域不一致时，应补明任务合同、修正测试，或将结果限定为“符合这个 oracle”，
不能直接提升为“语义正确”。这比只验证 reference 能运行更昂贵，却能避免把生成测试的偏差当成模型失败。

还要检查多个指标是否真的提供独立证据。若冻结的检索语料为每个 query 只安排一个可通过测试的 canonical snippet，
且不存在其他通过项，那么“top-k 中至少一项执行通过”恰好等于 canonical hit@k；执行通过比例则等于 hit@k/k。
这时两个指标同涨并不是语义标签被另一真值独立证实，nDCG 与它们的排序不同也可能只是折扣和 k 的定义不同。
真正有诊断价值的对照可以固定其余语料，只加入或移除与目标近似的错误片段，观察首项可用性与召回如何变化；
但构造的近克隆压力不代表自然语料中的发生率，也不能代替后续代码组合与任务执行成功率。

这些检查由 Evaluation owner 管理，RAG owner 仍负责召回、重排与 context 使用。可信且简单的固定任务可以保留
单一 reference/test suite；开放需求、多种合法实现或模型生成的测试则需要额外语义审计、反例与不确定项处理。
ExecRetrieval 的受控语料与 scorer 提供了上述边界的具体案例，不证明一个测试集合穷尽了程序语义。
<!-- source-family:SF-2026-ARXIV-2609-01865 -->

#### Transaction 行为允许 Timing 差异，但 Oracle 不可自授

可复现的 reference 仍可能把合法实现误判：例如 specification 只约束输入接受、输出内容、顺序与允许 latency，而 reference RTL 恰好用某个固定 cycle 数。此时 oracle 应先把 transaction、reset 和 handshake 映射固定下来，在 specification 允许的 timing 差异内比较行为，并另外检查真正的时序约束；默认顺序不能静默改成无序集合。对 agent 同时生成 design 与 behavioral reference 的流程，二者一致只是一条开发反馈，最终还须各自对独立 hidden gold 验证，避免共同犯错变成自授正确。

[BEHAVE v1 §3–4/B.4–5](https://arxiv.org/html/2609.34785v1)用 typed BehaviorIR 与有限 stimulus pool 实现这条路径，但无 mismatch 的 pass 不等于程序语义完备；coverage、bounded proof 的编码范围和 unresolved/unknown 应分开呈现。Protocol adapter、goal/query 编码和更充分的 replay 增加成本，generation／analysis 的支持面也小于执行回放。没有可信映射、涉及未支持 memory／clock 行为或超出固定 bounds 时，保留人工 spec 审核、已验证 reference 与任务专属测试，不能把受限 agent 分数或合成 PPA 当硬件生产成功。

<!-- source-family:SF-2026-ARXIV-2609-34785 -->

#### Dense Process Score 仍须校准未来 Return

Dense process score 同样只是训练 proxy。若逐步分数与后续 return 或 target value 不对齐，优化它会奖励看似
合理却把系统带向失败的中间动作。进入 RL 或 policy selection 前，应在固定 trajectory distribution 上检验
`score_t` 与 future return、终局 verifier 和关键 slice 的校准，并允许 proxy 在不确定时 abstain。QVal 提供了
这种对齐检查的实验性方法；它不把 learned score 升级为部署 correctness gate，也不证明相关性就是因果 credit。

### Verification Bound 也陈述其输入抽象的信息上限

Transformer verifier 常把 pre-softmax scores 压成独立 interval，再对 softmax 做通用 relaxation；实现简单，
却可能引入与下游 verification objective 无关的松弛。对给定 score box 直接求 softmax objective 的极值，可以获得
该抽象下的 tight sound bound。关键结论不是“验证已经精确”，而是：若 interval-only bound 已达到该信息集合的
最优值，继续收紧必须引入 score correlation、score–value coupling 或其他结构信息。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10974:start -->
bound solver 只拥有 certification evidence，不能把输入 abstraction 的缺失关系补成事实；周围网络层的 relaxation、
数值实现和 property specification 仍可能主导最终 gap。更强结构会增加求解、内存和验证器 TCB 成本；预算不足时，
应回退 sound interval relaxation，并明确报告其松弛来源而不是夸大 certificate。现有 exact-v1 只证明 score-box
softmax optimization 与受测 certified-verification 设置中的性质，不构成任意 Transformer 的安全证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10974:end -->

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

### Adversarial Evaluation 要同时改变 Representation 与时间轴

只在输入表面做扰动会漏掉 latent-space 中保持语义却诱发 hallucination 的方向；realistic latent attack 可以把表示层的可行扰动纳入评测，但其真实性仍由 decoder、语义约束和人类判断界定。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12813 -->

单次 attack success rate 也无法描述持续攻击下安全能力如何衰减。把重复尝试看作 time-to-compromise，并用 survival curve 报告 hazard，可区分“第一次就失守”和“多次累积后失守”。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12869 -->

latent 可行域、攻击预算与尝试独立性都可能不真实；因此结果必须绑定 threat model，条件不成立时回退可复现的输入级 red-team、固定次数曲线和最坏案例分析。

### Principal Hierarchy 要在任务 Framing 中验收

模型在 advisory prompt 中复述专业规范，不代表在 drafting、action 或利益冲突 framing 中仍遵从。evaluation contract 应显式组合 domain、task framing、stakeholder 和 authority hierarchy，按 slice 保存行为结果；模型自报意图不能替代工具权限、人工复核与 abstention。更真实的冲突场景增加规范定义、专家标注和时变维护成本，却能暴露平均分隐藏的 authority inversion。exact-v1 只支持所测法律、医疗场景和模型，不证明真实事故率或全部职业规范。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12120 -->

### Safety Improvement 需要防止 Harm Transformation

surface toxicity、拒答率或显式攻击成功率下降，不代表伤害已经从模型表示与内容中消失；干预可能只把可见措辞改写为更隐蔽的 stereotype、association 或 framing。安全评价应并列 surface behavior、content/representation slices 与 construct definition，记录“减少、迁移、掩蔽还是不可判定”，不能用单一 classifier 的改善替代目标构念。<!-- source-family:SF-2026-ARXIV-2609-20779 -->

多层测量提高诊断力，也引入 classifier disagreement、taxonomy choice 与解释过度的风险。现有证据只覆盖 15 个 GPT lineage、三个 classifiers 和作者定义的 harm taxonomy，不证明 hidden representation 等于真实伤害或跨模型趋势恒定；构念或测量器不一致时，应保留 Unknown、人工审阅与多 sensor 对照，而不是把表面改善升级为 release 证明。

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

若黑盒视觉 reasoner 虽不提供 logits 或 hidden state，却输出带区域的 zoom-in crop 轨迹，风险传感器还有一条可观察的分支：
把问题、原图、crop 轨迹与最终回答一同交给 selector，分别估计**答对的可能性、是否看到了相关区域，以及所见区域是否支持回答**。
定位与证据—答案连贯性不能与正确率合成同一种真值；模型看对区域仍可能推错，crop 不完整也可能漏掉关键证据。这个分支
以 crop/框标注、伪标签 judge、额外 selector 推理和跨 reasoner 的轨迹协议为代价，适合视觉证据可暴露而内部表示不可读的场景；
没有可靠 crop、定位标注或成本预算时，仍保留原图复核、多样本检查与人工升级。<!-- source-family:SF-2026-ARXIV-2604-25855 -->

这类 selector 先是排序与弃答提议，不自动获得发布阈值：独立的目标部署切片还须校准风险、覆盖和漂移。若离线论文在**同一
测试集的真实答错标签**上回选满足经验错误率的最佳阈值，所得 `coverage at risk` 只是事后曲线，不是未来请求的风险保证。
受限视觉问答实验显示可见 crop 质量有时改善 OOD 选择性回答，但不同 reasoner、数据集和风险点并不等幅；多信号权重也
非每处都必要。高风险使用须保留独立真值/人工复核与拒答回退，不能让视觉轨迹的表面连贯替代答案或 effect 的验证。

比较自身与外部表示的 correctness probe 时，全样本同对、同错可能掩盖二者的条件差异。更可定位的合同让两类 probe 都预测同一个 target-model 标签，在完整训练分母上保持训练协议不变，再仅在测试阶段抽取 target 与 peer correctness 不一致的样本；同时报告全样本、disagreement 切片的 AUC、数量和覆盖。不能在该完全反相关子集重新训练后，把读取 peer 错误的捷径当作自身信号。

切片测试回答的是声明的模型对与问题分布中的预测差异，不证明内部自知、因果可访问，或没有任何外部观察者能获得同样信息。所测事实与数学任务结论不同，条件 AUC 也不能替换全样本部署风险。额外 peer forward、标签与切片选择增加成本；普通总体校准仍适合稳定发布比较，disagreement 更适合诊断，后续 correction 仍须独立干预与结果验收。<!-- source-family:SF-2026-ARXIV-2604-12373 -->

报告接口也可以跨一组模型行为变体训练，而非每个 backbone 单独训练一个风险 probe：先在共同 base 上构造已知行为的冻结 delta/adapter 变体，再联合训练共享的报告 adapter，用标签与偏好信号使其描述各变体行为。此时 subject 不是孤立 checkpoint，base、behavior delta、report adapter、标签构造与跨变体 holdout 必须联合记录；报告只是审计线索，不由“自述”取得内部自知或发布权。<!-- source-family:SF-2026-ARXIV-2604-16812 -->

构造与标注行为变体有离线成本，共享接口还可能误报类别、幻觉描述或在跨家族时失准。原文对 sandbagging 等受限行为的检测与假阳性不能成为精确识别隐藏意图的保证；训练时已知变体也不等同部署未知变体。单模型 probe 在 subject 稳定时仍更直接，跨变体报告适合提出复核队列，最终采用继续依赖冻结协议下的行为测试与独立 outcome，不能用较自然的说明替代校准。<!-- source-family:SF-2026-ARXIV-2604-16812 -->

### 可解码 Failure Direction 不拥有自动纠错权

一个 failure direction 能被线性 probe 从 activation 中读出，只证明当前表示对该标签有预测信息；它不证明这条方向与
任务所需计算相互独立，也不证明沿反方向 steering 或 erasure 会修复答案。若 failure feature 与 task-critical state
纠缠，固定线性干预可能无效，甚至同时删除完成任务所需的信息。Evaluation owner 因而只能把 probe 输出校准成
risk–coverage curve，用于 abstention、升级外部验证或人工复核；是否执行 correction 必须由独立 intervention evidence
和端到端行为验收决定。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05715 -->

这条边界保留了 nonlinear 或局部 intervention 作为实验分支，却要求它重新证明 target effect、control survival 与分布外
稳定性。作者结果只覆盖 Llama-3.1-8B、Qwen2.5-7B，以 MedQA 为主的任务和 29 组固定线性配置；论文中的 AUROC、coverage、
self-consistency 成本和 adapter damage 都不能外推成通用阈值。没有目标模型、任务切片和 intervention 对照时，probe 应退回
诊断 sensor，而不是成为 production correction authority。

若控制点是从推理文本的关键词变化处抽取，首先要验证这个边界在**同一前缀重新采样**时是否稳定出现；一次表面命中不能证明 hidden state 持有可复现的行为方向。只有通过该检查的边界才适合参与 steering-vector proposal，并应与“随机选相同数量边界”的对照比较，随后仍需独立的干预和任务回归。重复生成与阈值筛选增加成本，也可能因保留样本太少而放大方差；[exact-v1](https://arxiv.org/html/2604.02113v1)只在作者的 100 道 MATH 训练题、三款同架构 1.5B 模型及 MATH-500 条件下支持这条受限测量链，不证明文本关键词能定位所有推理状态。<!-- source-family:SF-2026-ARXIV-2604-02113 -->

干预对象还要沿“是否不确定”和“是否答错”两条轴拆开：高熵的正确回答、低熵的错误回答、二者同时变化和都不变化，不能由一个 failure 标签解释。降低某个 uncertainty feature 的激活可能降低熵，却一并损伤任务计算；只有把正确性保持作为独立 acceptance gate，并与同数量随机活跃 feature 及无干预对照比较，才可以讨论纠错而非变得更自信。该分账增加标签、分层样本和干预成本；[有限 MCQ/SAE 结果](https://arxiv.org/html/2604.19974v1)、分位筛选和未经多重比较校正的 feature 发现不提供开域置信度或稳定因果坐标。预算不足、特征跨任务失准或 accuracy gate 不成立时，保留诊断 probe 及外部证据核验，不执行自动 erasure。<!-- source-family:SF-2026-ARXIV-2604-19974 -->

### Single-token Evaluator 把生成收缩为版本化分类 Sensor

让通用 LLM 自由生成评分与理由，在 rubric 复杂、需要解释时很灵活，却把 decode path、format parsing 和 verbosity 都带入 evaluator variance。若一个 metric 已有有限离散等级，可以让共享 decoder-only 小模型通过 metric-specific LoRA/head 只生成一个预先映射的 class token，并仅在这些 class-token logits 上归一化为分数；prompt template 选择该 metric 允许看到的 trace fields。这样把 evaluator 从开放生成器收缩为低成本分类 sensor，但 class-token mapping、tokenizer、base model、adapter、prompt fields 与 calibration data 必须共同进入 artifact identity。

一个 token 约束输出格式，不会自动提供 truth 或 calibrated probability；不同 metric 共用 backbone 还可能产生 interference，domain/trace schema 漂移会让原概率失效。确定性 checker 可表达时仍应优先使用，风险高或 calibration slice 不匹配时回退独立 judge/人工标注。`arXiv:2602.18583v1` 的 exact-v1 只支持 Luna-2 的 metric-specific adapter/head、single-token class probability 与作者实验，不证明跨 metric、模型、语言或生产分布的校准稳定性。

<!-- source-family:SF-2026-ARXIV-2602-18583 -->

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

在采样回答并聚成语义类的路径中，校准还可能发生在生成之前。直接对最终置信分数作单调映射，保持原答案和排序，适合已有生成策略可靠但概率失真的场景；若固定token温度已经改变了哪些答案会被采到，就要把生成概率、语义聚类和最终答案选择一起评估。一个受限分支在独立校准集上学习全局token温度，再重采样和计算语义类质量，分别测试概率校准、错答区分与实际任务正确率，而不是把它视作最后分数上的温度缩放。<!-- source-family:SF-2026-ARXIV-2604-07172 -->

它以额外校准和多次生成成本换取更合适的采样分布，却引入聚类错误、任务迁移和答案选择变化。[短问答实验](https://arxiv.org/html/2604.07172v1)的最优语义类评测允许在至多四个类内样本中任一命中ground truth，这不是部署时无真值选择单个答案的正确率。温度、样本数、NLI聚类器和输出选择协议因而都是sensor身份；短问答收益不证明长文或开放任务的事实可靠性。生成接口不可改、样本预算紧或目标任务不匹配时，保留固定策略与后置标签校准，并继续依赖外部证据或拒答。

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

校准身份也包括模型实际看到了哪些输入证据。视觉token裁剪可能保持任务准确率，却改变错误答案的confidence；因此不能把未压缩模型的阈值直接交给压缩路径。应共同保存保留token的数量与身份、selector配置、实施路径、answer verbalizer和confidence estimator，并在同一任务/预算切片联合测质量、校准和risk–coverage。选择机制仍由第23章负责，本章验收的是其改变后的测量对象。[受限视觉实验](https://arxiv.org/html/2604.12035v1)在固定LLaVA-1.5-7B/576个CLIP tokens中比较同路径SCOPE参数和另一路径FastV；单模型、两题库及候选内归一化confidence不支持所有覆盖式选择器更可靠，也没有zeroing与物理删除的受控对照。额外校准增加成本；未压缩路径仍可作基线，压缩后没有有效校准时不借用旧阈值。<!-- source-family:SF-2026-ARXIV-2604-12035 -->

不确定性还要按任务中的来源区分，不能都交给“答案越分散越该拒答”的阈值。确有唯一答案而模型缺少知识时，查证或拒答是合理分支；任务允许多个合法答案时，采样分歧可能只反映有效选择，系统应验证所选答案是否满足要求；问题缺少决定答案的条件时，继续检索未必能补上用户意图，更合适的是澄清或显式给出条件化回答。这样从共同的 confidence sensor 进一步分出不同 action policy，选择依据仍是任务契约和外部证据，而不是由 entropy 自动宣布自己的知识边界。<!-- source-family:SF-2026-ARXIV-2604-10495 -->

[受控问答对照](https://arxiv.org/html/2604.10495v1)通过改写问题构造知识不足、合法多解与输入含糊三类切片，支持分别测试这些动作，却不证明开放任务已经能可靠自动诊断原因。其 PRR 衡量相对 oracle/random 的拒答排序质量，不是事实正确率的概率校准；构造者、judge、人工核验与539个配对问题/类的范围都要保留。分类和多动作路由增加标注、调用与误判成本；任务只有单一可验答案、原因无法可靠区分时，统一的保守查证/拒答策略仍可成立，不能以“可能是合法多解”放行无证据结论。

### Verbalized Confidence 必须与答案生成解耦并校准相对顺序

让模型在生成答案时顺便报一个置信度，最容易部署，却把答案质量、表达风格和 confidence token 混在同一 decoding
过程。一个条件分支先冻结答案，再由独立 confidence head/prompt 估计分数，并用正确性对的相对顺序训练：正确样本
应排在错误样本之前。这样 confidence module 只拥有可校准的排序 sensor，不拥有事实 truth，后续 policy 仍需在
held-out slice 上把排序映射为 risk/coverage 决策。

<!-- semantic-body-binding:SF-ORCE-ORDER-AWARE-ALIGNMENT-OF-VERBALIZED-CONFIDENCE-IN-LARGE-LANGUAGE-MO:start -->
解耦增加一次推理、reference set 与训练流水线，也不能自动得到绝对概率。有限样本 surrogate、reference drift 与
DPO-style approximation 会破坏理想化顺序保证；语言、模型或任务分布变化时必须重校准，失败则回退外部 verifier、
sample agreement、人工 review 或直接 abstain。现有 exact-v1 只支持作者披露的模型、任务与指标，不能把 verbalized
confidence 外推为跨模型、跨部署或生产 tail 的通用可靠度。
<!-- semantic-body-binding:SF-ORCE-ORDER-AWARE-ALIGNMENT-OF-VERBALIZED-CONFIDENCE-IN-LARGE-LANGUAGE-MO:end -->

训练时也可以先尽量固定claim内容、只优化confidence，再优化事实生成；这使两个目标更容易诊断，却不等于把两个函数隔离。后阶段即使遮住confidence token的loss，更新的共享参数仍可改变其输出，因而每次内容优化后都要重验概率校准、错答区分和claim保持；筛选claim后重新生成的最终回答，还要检查是否新增或改写未经验证的claim。[分阶段训练的受限证据](https://arxiv.org/html/2604.12046v1)在Biography切片出现AUROC与Brier退化，不能采用“mask保证不干扰校准”；不同阶段同时改变数据、优化方法和预算，也不单独证明训练顺序造成全部收益。额外重校准与事实verifier需要预算，文本一致性validator不是事实真值；失败时重新校准、补外部证据或abstain，固定答案的独立confidence路径仍可保留。<!-- source-family:SF-2026-ARXIV-2604-12046 -->

### Atomic Claim 置信度怎样合成整体结论

在计算 claim confidence 之前，还要决定 verification unit。过度 atomization 会切断 enumeration、causal/conditional chain 与 premise–conclusion 依赖，使每个片段可判却失去原命题；更大的 snippet 保留局部结构，却增加 retrieval 与 verifier 负担。系统应先保存 claim graph，再以满足判定所需的最小依赖子图作为单位；只有本来独立的 claims 才安全拆成 atoms。

<!-- source-family:SF-2026-ARXIV-2609-12884 -->

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

Claim的语法也决定验证要执行什么查询。把关系谓词、量词和聚合表达编成query，可以让evidence tuple、witness/counterexample与停止规则保持同一lineage；存在性命题找到合法witness即可，而全称及统计聚合需要不同的扫描或风险预算。顺序采样的confidence sequence可用于受限早停，但bool_and的区间落在[1−ε,1]只是容差接受，不等于所有tuple都严格满足谓词，不能写成完全逻辑精确。<!-- source-family:SF-2026-ARXIV-2604-26180 -->

该分支依赖exchangeable shuffle、多个查询的风险预算及语义predicate自身的准确性；统计区间只能控制规定的采样事件，不补上LLM谓词的真值误差。作者16条Yelp查询里强LLM多数票也有负例，不能因早停省调用就赋予完整proof身份；编译、shuffle与tuple检查都有成本。量词无法可靠转换、predicate失准或高风险不容许ε误差时，应回退完整受限扫描、确定性验证或人工审查，原typed claim graph继续负责证据结构而不是被query运行结果取代。

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

校准单条 claim 的分数仍不等于优化整段推理的保留策略。独立训练 scorer 时，低风险的结论可能依赖一个被删掉的前提；只把更多 claim 留下，又可能超出整体错误预算。手工频率分数和逐 claim 分类在依赖较浅、校准样本有限时仍是简单基线；当目标变成“在依赖闭包和统计风险约束下尽量保留有用推理”，训练目标就需要依次模拟阈值筛选、祖先闭包、校准分位数和最终子图选择。可微近似让这些原本离散的决定把梯度传回 scorer，但训练代理只负责学排序与取舍，不能取得发布时的统计保证。<!-- source-family:SF-2026-ARXIV-2604-20098 -->

上线前应把学到的 scorer 放回原本的硬筛选算法，以独立标注集重新校准阈值，并在目标任务切片上检查保留量和 coherent graph 的边际覆盖。近似算子在温度极限下还原硬算法，不意味着有限温度训练本身有覆盖保证；覆盖也不是每条 claim 的事实概率，更不是单次答案的确定性正确。受限实验只含两套推理数据，极严格风险阈值时甚至会删掉全部 claim，频率本已有效时收益缩小。若图依赖标注不可靠、可交换性或分布稳定性失效，就不能继续引用旧覆盖率；应回退人工核验、外部 evidence 或 abstention，而非把 soft score 当 release gate。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21776:start -->
有限候选 prompt 返回的概率还存在更早一层的边界：它通常只在已列选项内部重新归一化，不能直接解释为答案空间上的绝对置信度。显式加入 `OTHER` 可以在候选空间定义清楚、生成与 Bayes-optimal 假设成立时承接遗漏质量，再用 contrastive estimate 恢复条件概率；但 `OTHER` 不是“模型知道自己还遗漏了什么”，更不等于 factuality。

该分支要求明确候选 universe、稳定的概率 elicitation 和真实标签校准；错误或不完整的 alternatives 反而会主导估计。现有理论与三套数据只支持披露条件下的 estimator，不证明开放答案空间中的通用校准。假设、标签空间或 calibration transfer 失败时，应只报告相对 ranking/log-odds，并以 held-out labels、扩大检索或 abstention 作为回退。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21776:end -->

Answer-level calibrator 可以继续读取 critical-path confidences、dependency depth、source-family correlation、
contradiction、inference-edge score、semantic entropy 与 retrieval coverage，直接预测 conclusion / complete-answer event。
它不应删除 claim-level ledger：一个漂亮的总分无法告诉系统应该删除哪条 claim、继续检索什么或把哪个冲突升级给人。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-00269:start -->
#### OOD Score 先做 Length Deconfounding

白盒 activation、attention entropy 或安全分类器分数能提供比输出文本更早的异常信号，但 sequence length 同时会改变 entropy、聚合统计和分类边界。若 in-distribution 与 OOD 集合的长度分布不同，随机划分得到的高 AUROC 可能主要识别“更长或更短”，而不是语义或处理路径异常。Evaluation owner 因此必须冻结 tokenizer/template 与长度分布，先报告原始结果，再做 length-matched 或 length-stratified 对照；长度匹配后消失的收益不能继续写成 OOD 能力。

通过长度反事实后，content embedding 与跨层 processing trajectory 仍是两类互补 evidence：前者更适合语义距离，后者可能捕捉 jailbreak 等计算路径变化。它们都只拥有 risk sensor 权，不能把一个 feature score 直接升级为 calibrated correctness probability；部署 gate 仍需在目标模型、任务与长度 slice 上校准，并把输入规则、拒答和人工复核保留为 fallback。

这种去混杂会减少有效样本、降低统计功效，trajectory 特征还要求白盒访问和额外存储；短且同分布的请求可继续使用简单 embedding baseline。exact-v1 只覆盖六个 360M–7B 模型、六类任务与每类 200 样本，部分 ToxicChat/HateSpeech signal 很弱，跨模型因果复现不完整；它支持“先排除长度捷径”的 evaluation contract，不证明 27 个 trajectory features 是通用 OOD detector。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-00269:end -->

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

少量 gold labels 还可以约束 noisy judge 的错误模型，而不只用于估计平均残差。若目标是总体 failure rate，一条条件分支联合估计 failure prevalence 与 judge 的 true/false-positive rates，再以已有校准给出的区间约束 likelihood 优化。区间收窄可减少小样本方差，却把 prior validity 变成额外前提；错误区间会让估计向错误方向偏移，不能因优化器收敛而称作无偏。<!-- source-family:SF-2026-ARXIV-2604-03257 -->

平台因此需要保留区间的来源、gold抽样单位、judge/model身份与目标分布，对约束和无约束估计一起做敏感性检查。这是总体 estimand，不是逐条回答正确率或发布授权。作者少量gold与大量judge标签的同域分类实验支持该方差—偏差分支，不证明跨领域 anchor 可直接迁移；prior失配、标签可比性不足或漂移时，应放宽/移除约束，追加代表性人工标注，回退原有残差校正或human-only评估。

总体残差在旧流量中为零，也可能只是不同切片的正负误差相抵。若目标流量重新分配这些切片的权重，直接搬用旧总体校准就会重新产生 prevalence 偏差。对于以模型预测估计总体标签率的任务，应先声明可观测的重加权特征与目标支持范围，用有代表性的人工标签检查相关组的条件平均残差，再在标签条件规律稳定的前提下汇总到目标人口。这里约束的是估计量在给定迁移下的误差，不把每条模型标签当真值；高 AUC 或旧总体平均准确，也不构成目标人口无偏的证明。<!-- source-family:SF-2026-ARXIV-2604-21549 -->

更细的条件校准以标注、分组复杂度和小组方差换取可迁移性。多重校准比只控制平均组误差更强，但有限样本拟合不自动覆盖所有组、分数区间或未来重加权；新文档类型还可能同时改变支持与标签条件规律。平台应把分组、输入分数或离散标签、人工标签抽样和校准版本纳入测量身份，先验证重叠与漂移，再决定补标注、扩不确定区间还是退回上述人工残差校正。受限文本分类实验中，概率自报并非总优于离散标签加 metadata；理论上的条件迁移也不是免维护的发布保证。

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

还有一种错误不是“证据不足”，而是系统自信地回答了**另一个问题**。因此在事实核查之前，可把原始请求与从回答轨迹
反推的实际问题作成对检查：若目标、限定词或指代已被悄悄替换，先请求澄清或拒答，而不是继续提高答案本身的
置信分。轨迹反推只是一个有成本的意图错位 sensor，并非内部推理的忠实读数；它可能复述同一偏见，也不能替代
权威证据。评估时须将“答非所问检出率”、接受后的事实正确率与拒答成本分开测量。有限模型和 QA 数据集上的
[Trace Inversion 实验](https://arxiv.org/html/2604.02230v1)支持这种受限诊断分支，不证明通用的幻觉消除。

#### 对抗性相关错误：低熵与高共识也可以稳定地错

Semantic entropy、self-consistency 和 majority vote 的有效性还依赖一个未必成立的前提：错误 samples 具有足够
多样性，正确答案能形成更稳定的 mode。若同一个 checkpoint、训练过程或攻击主动把关键元素塑造成一致的错误值，
系统会观察到 fluent、低熵、高 agreement 的输出，却没有获得任何独立 truth evidence。

诊断这种错误时，还要避免循环划分：若先用某种 agreement signal 把样本分成“容易检测”和“难以检测”，再用同一个 signal 证明两组可检测性不同，差距部分来自定义本身。可先冻结 regime partition，再更换 lexical/semantic whole-response dispersion，最后在独立切分上评估单条生成轨迹的检测器，把“不同观测面存在差异”与“部署可预测错误”分开。它增加信号、标签和切分成本，但防止把事后分组优势误写成风险保证。

[受限 detectability-gap 审计](https://arxiv.org/html/2609.35860v1)的跨信号比较不是独立新数据集；单 seed 轨迹对照只针对 diffusion 模型，LLaDA 三任务与 Dream 的 PopQA 差距显著，其余同向但估计不精确，不能称已获跨模型通用结果。难组仍具有高于随机的检测表现，不能称原理上不可检测。Gold alias 或词子串标签不等于开放事实 oracle，异质性存在也不能替代独立部署校准。预算有限时可保留单一 sensor 的受限诊断，但必须声明其分组来源；高风险采用继续依赖独立 evidence 或拒答。
<!-- source-family:SF-2026-ARXIV-2609-35860 -->

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

当这份 ledger 用来支持安全部署决定时，还要先固定它究竟在为哪个决定、哪个系统作证。被论证对象不能只写模型 checkpoint：工具权限、监督者、运行环境和预定有效期会改变风险暴露；每条 claim 应绑定相应 evidence、未覆盖条件与足以使结论重开的 defeater。否则，黑盒任务中的“没有观察到危险能力”最多说明所测接口与任务，不能自动成为包含工具和人类监督的部署栈安全许可。环境、模型或监督流程改变后，应重新审视受影响的 claim，而不是沿用旧 verdict。<!-- source-family:SF-2026-ARXIV-2604-21964 -->

这种 safety-case admission 增加范围界定、跨团队取证和持续复核成本；低风险、配置冻结的用途可保留较窄的测试与发布合同，高风险用途则不能以更多同源测试次数替代部署系统证据。[公开 safety case 的受限外部审查](https://arxiv.org/html/2604.21964v1)指出了 decision、assured system、有效期及反证条件缺位时的论证断层，但审查者没有获得全部非公开安全工程材料；它不证明被审系统实际上不安全，也不提供可外推的事故率。

### Judge 先证明看见了目标变化，再谈总体准确率

Evaluator 的 aggregate accuracy 可能同时掩盖两种相反失败：目标事实已经改变，judge 却保持原 verdict；无关表达被改写，judge 又错误地改变 verdict。因而 construct validity 不应压成一个标量，而应至少有两条受控 intervention arm：

```text
target-changing edit   → verdict should change   → sensitivity lower bound
target-preserving edit → verdict should remain  → invariance lower bound
```

两条 arm 的样本身份、人工裁决、edit provenance 与置信区间必须分别保存。人工也会误判 target-changing edit，有限 control family 也只能给出边界；但这种分解能防止一个看似不错的总分把“对真正变化不敏感”与“对表面变化过敏”互相抵消。它是现有 judge calibration 的前置条件，不替代 executable verifier、domain expert 或 deployment outcome。

多模态的 target-preserving arm 也不能只取语义丰富的自然照片。若声称系统具有旋转、缩放或身份匹配的不变性，
应固定变换及原始对象，按照片、素描、符号/陌生文字等语义线索强弱分层，并同时测“同一对象变换后仍识别”与
“不同对象不误判为同一”。照片上的高准确率可能来自熟悉的类别线索，不能单独证明几何推理；符号层失败也不能
直接推出所有视觉任务失败。[受控视觉不变性实验](https://arxiv.org/html/2604.01848v1)只给有限模型、图像域与变换的
证据，却说明为什么 control family 的语义丰富度本身必须成为评估身份的一部分。

Agent evaluation 还要把 ranking fidelity 与 construct fidelity 分开：judge 能稳定排序两个系统，不代表它测到了任务成功。满意度、自然语言完成叙述与真实环境 outcome 可能方向相反，近分系统的排序也远不如宽差系统稳定。Release 应同时报告 deterministic outcome、construct label、close-pair uncertainty 与 human ceiling，不能用一个相关系数替代。

<!-- source-family:SF-2026-ARXIV-2609-12191 -->

多个 uncertainty scorer 的 supervised ensemble 也只能在有代表性的标签与目标模型访问合同下作为 sensor。Black-box consistency、token probability、reflexive judge 与 claim-level score 观察不同误差面，组合后可能改善 AUROC / calibration，却会引入标签成本、domain shift、grader correlation 与 scorer availability。原始相似度、entropy 或 ensemble output 仍不是概率；必须按 deployment slice 校准，并把 abstain、human escalation 与风险覆盖率作为最终决策输出。

### Stateful Evaluation 必须把 Turn Frontier 纳入身份

固定脚本预先写死所有 user turns，容易漏掉只有在上一轮回答之后才出现、消退或重新出现的行为。多轮评价应让下一轮输入依赖当前 response，并把 conversation history、turn frontier、user-generation policy、judge revision 和停止条件共同纳入 evaluation identity；报告首次出现、持续、消退与 re-emergence，而不是只给固定轮数终值。<!-- source-family:SF-2026-ARXIV-2609-18649 -->

动态协议更接近交互，却引入 synthetic user、generator/judge coupling 和更高成本。240 个 seed stereotypes、六类偏差、六个模型及 5/10-turn 对照只支持所测设置，不代表真实用户发生率或所有风险类型；生成器、judge 或停止条件无法独立时，应回退人工对话样本与固定脚本对照，并显式保留不可归因状态。

### 多轮评估要区分 Context Length 与 Intent Supersession

多轮 Agent 评估不能把“上下文更长”与“用户意图发生 supersession”混为一项。EvalSpec 应显式保存 current function、arguments、revealed/withdrawn values、revision 与 function-switch event，并用 turn-matched no-change control 区分长度压力和状态更新失败。

Final anchored verifier 可以提供可扩展 outcome evidence，却不能证明每个中间 transition 正确。真实用户风格、多意图同轮和含糊修订还需要额外切片；Agent 的 Context、Memory 与 Workflow 可以消费这些状态边界，但 evaluation owner 仍负责定义 transition identity、control arm 与最终可比较性。

若用户在执行途中补充、修正或撤回条件，评测不能只把最终消息拼到长 Context 中重问。应固定原任务和环境，记录插入时已完成的 action、更新类型与位置，分别跑接收更新和未接收更新的配对轨迹；验收以更新后的最终意图为准，同时观察更新后第 `k` 步的任务成功率、action 和 token 成本。这样才能区分“能读懂修订”与“能在已有进度上及时改变后续行动”，代价是重放环境、控制插入时机和保存更长的轨迹。[受控 Web 任务实验](https://arxiv.org/html/2604.00892v1)只包含不会重置环境、也不使已完成动作失效的信息性中断；它不能证明已提交副作用的撤销、补偿或任意真实用户修订可安全处理。此类情形仍需 Workflow 的 effect ledger 与独立恢复测试。
<!-- source-family:SF-2026-ARXIV-2604-00892 -->

### Scoring Rule 要奖励任务效用，而不是只奖励“像答案”

顺序搜索任务同时要求概率判断和候选排序：只用 Brier/log score 可以校准“是否成功”，却不惩罚把高价值
候选放到昂贵搜索位置；只看最终找到与否又无法区分概率质量。由 search cost decomposition 导出的 proper
scoring rule 可以把两者放进同一 contract，奖励校准概率并惩罚错误排序。它用任务模型与成本参数换更
贴近决策的分数，也会因成本估计错误、候选集合变化或停止规则不匹配而误导；没有明确 sequential-search
utility 时应保留标准 calibration 与 ranking 指标分账。作者 theorem 与 meta-evaluation 只支持声明的搜索模型，
不证明一个复合分数能替代真实线上 outcome。
<!-- source-family:SF-2026-ARXIV-2605-01936 -->

通用 judge score 易部署，却会把表达偏好混入正确性。任务效用可分解为可验证结果、校准置信与拒答成本，再用 proper scoring/utility contract 汇总；这让 release decision 可解释，却要求明确代价矩阵。代价未知时应保留分项指标。<!-- source-family:SF-2026-ARXIV-2605-20490 --> exact-v1 §2–4 只支持 ECUAS 的定义与论文实验，Limitations 不允许把该权重当成跨任务真值。

## Scorer 不是绝对真相

<!-- semantic-body-binding:SF-2026-ARXIV-2605-26046:start -->
自动优化 judge prompt 时，多目标 feedback 还会产生两个不同 failure owner：把全部 criteria 合在一次 critique 中，可能在 optimization time 稀释每个目标的 textual gradient；先分别优化再合并 instructions，又可能在 inference time 相互覆盖。因而 criteria、sharing mode、prompt revision、训练轨迹与 held-out judge calibration 都应进入 scorer identity，不能只保存最终 prompt。

分解 objective 和重复优化会增加 judge calls、搜索预算与集成复杂度，也不能消除 scorer 偏差。联合反馈失焦或合并后干扰时，应回退单目标/串行优化、人工 rubric 和独立 held-out calibration，并禁止自动更新直接越过 release gate。两套数据和特定 textual-gradient optimizer 只证明 failure 的存在，不给出通用最优组合策略。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-26046:end -->

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

当 verifier 还负责挑选纠错训练数据，这个限制会进入反馈回路：只重训被拒绝的答案，会让“答错但被放过”
的样本缺少直接纠错信号；再用同一 verifier 画质量曲线，便可能把未检出的错误当成质量稳定。应在接受与
拒绝两类样本中保留独立审计，分别测错误放行和替代答案的错误，不能只盯升级率下降。
[廉价验证级联的研究](https://arxiv.org/html/2609.01345v1) 测到了这种盲区，但真实训练未实现持续改善；
其渐近错误下限依赖简化模型与合成实验，不能写成所有自训练系统的定律。独立审计增加成本，开放任务也未必
存在廉价真值；此时应披露可判断范围，而不是让内部仪表盘自行证明可靠性。

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

“这个judge panel相当于几个人”必须先说明匹配什么。若要保留人群分歧，可将每位judge的标签与同一经验annotation distribution作残差；谱的participation ratio描述这些残差方向有多少，而panel标签频率与人群分布的误差是另一目标。把二者各自匹配到条件独立的人类参考抽样，可能得到不同有效人数；该匹配依赖题目人口、参考估计、表示及抽样规则，不是通用的人力替代率，更不授予事实真值。

即使成员误差能量相同且相关非负，提高谱多样性也可能增大分布恢复误差：归一化谱统计丢掉能量和平均方向的对齐，后者仍决定ensemble输出。应同时保存member error energy、相关结构、人群参考及聚合后的实际目标误差，再按目标评估新增成员；majority label正确率、频率恢复和中心化共同方差不能互换。此审计增加人工参考、逐项votes和计算预算，有限人类标签也会给所有残差加入共同估计误差。低风险固定rubric仍可使用小panel；参考不足或新增成员改变人口时，保留原评测并补独立标注，不能仅凭一个“有效维度”自动扩容或发布。[必要公式与构造反例](https://arxiv.org/html/2609.21277v1)。<!-- source-family:SF-2026-ARXIV-2609-21277 -->

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

在轨迹评价中，rubric formation还要避免被受评行为反向塑造：先仅依据task冻结必要条件，再让独立scorer读取轨迹。环境决定某个条件是否适用时，保存原条件、实际环境证据与active集合，按适用项的总权重计算process分母；这不同于看见失败后删掉要求。一个上游障碍使若干后继步骤无法执行，也应沿dependency说明共同原因，避免把同一障碍重复扣分，但不能把因此没完成的用户目标改写为成功。Process、最终outcome与未请求的side effect仍分别验收。<!-- source-family:SF-2026-ARXIV-2604-06240 -->

这种分层减少phantom criteria与cascade惩罚，却增加依赖判断、条件适用性和环境归因误差；task本身含糊时，冻结rubric也会冻结误解。关键依赖不能判定时应保留unknown或人工裁决，而不是给Agent自报的“外部受阻”自动免责。[CUA原始研究](https://arxiv.org/html/2604.06240v1)只在披露的web轨迹、人类标签与judge设置支持该设计；多个组件共同调优的结果不证明单个组件独自造成收益，也不构成任意环境中的零false-positive保证。

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

### Outcome Witness 决定分数能够声明到哪里

Binary checker 在任务状态单一、断言完整时成本低；interactive Agent 中，“点击 Save”并不证明目标记录已经改变。评测应把必要环境状态列为 outcome witness：已观测 witness 支持成功下界，未覆盖条件形成不确定上界；只有 witness contract 完整时，二者才可收敛为确定 verdict。

更强 instrumentation 会增加环境接入、隐私和人工 adjudication 成本，也可能因观测面缺失给出过宽区间。原子、确定性任务仍可使用简单断言；无法取得关键 witness 时应报告区间或 unknown，而不是用表面动作补齐成功证据。exact-v1 只支持披露 benchmark 与 outcome-check 分析，不证明该区间覆盖开放环境中的所有隐藏副作用。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10448 -->

对拥有用户数据的 Agent，终态成功还不是充分 witness：它可能完成订票或填表，却在途中请求了不必要的权限、把敏感值写入可选字段，或在最终提交前删掉曾暴露的数据。评测需要把权限请求/读取日志与每次表单编辑的过程状态一起保存；即便未提交，已填入的内容也应进入披露证据。分别报告任务成功、权限最小化、过度填写与跨会话偏好使用，再以同一任务分母报告“成功且满足预先指定隐私门槛”的交集；只看平均隐私分数会让提前失败、未到达风险场景的 Agent 显得更安全。

这种评估需要可观测的受控环境、字段必要性 rubric 和隐私门槛版本。若模拟用户对权限请求总是同意，它测的是 Agent **自愿克制**，不是被拒绝后的行为；阈值也只是发布方选择，不是规范真值。真实应用缺少编辑日志、任务涉及动态必要性或跨会话身份无法验证时，只能缩小结论范围并保留人工/安全审计，不能用成功率补齐隐私证据。[受限案例](https://arxiv.org/html/2604.00986v1)仅覆盖作者的 10 个模拟 Android 应用、300 项任务、五款模型与其评分合同。<!-- source-family:SF-2026-ARXIV-2604-00986 -->

同一 observation 还可混入任务必需的信息和敏感信息，此时应分别测必需 entry 的 conveyance、敏感 entry 的 leakage，以及至少一次泄漏的 case violation。三者分母不同：低 leakage 可能只是沉默，低 entry 平均也不能消除少数整例违规；任务成功与安全的交集仍要绑定预先定义的用途、recipient 和必要性规则，而不能把信息送出得更多直接认作 utility 更好。

这种分账需要带 entry 标签的受控输入和额外 judging；生成、模拟、评分同源会限制外部有效性。[企业场景受限实验](https://arxiv.org/html/2604.21308v1)使用 125 个 seed、每例 4+4 entries 和五个信息流方向，其中 25 个 seed 为人工、100 个由 Gemini-3-Pro 扩充，GPT-5.2 用于后续场景与评价链路；它不代表真实企业 incident 分布，也不赋予 judge 规范真值。没有可核标注时保留人工或安全审计，不以平均泄漏率替代过程证据；具身场景则还需下面的能力与危险进展对照。<!-- source-family:SF-2026-ARXIV-2604-21308 -->

具身危险动作还要控制另一种“失败即安全”的误读：任务未完成，可能只是 policy 没有执行能力，而不是拒绝危险。可在声明的布局、seed 与动作要求下构造 safe/unsafe twins，先测可完成的安全任务，再从可观测 simulator 状态分账 attempt、任务特定 near-hazard 与 terminal hazard。中间事件必须在先前 attempt 后才计入，避免路过触发；这里的 commit 只是任务几何或接触状态的近完成谓词，不是内部意图、控制器授权或数据库提交。

能力匹配与阶段 witness 需要额外环境资产、instrumentation 和阈值验证，构造的 twins 也不能消除所有视觉、物理差异。受限 VLA 模拟结果可揭示终态排序掩盖危险进展，却不证明真实机器人安全；无终态事件或启发式拒绝层有效也不等于普遍防护。低风险 smoke test 仍可使用终态指标，高风险发布应分别保留能力、危险进展与终态证据，并把执行安全 authority 交回第 26 章的 controller/safety envelope。<!-- source-family:SF-2026-ARXIV-2604-12447 -->

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

Rule-heavy procedure 还需要冻结 manual revision、required-state inventory、跨节 dependency、intermediate decision trace 与 exact terminal outcome。Partial credit 可用于诊断，却不能掩盖一个前置规则错误使最终过程无效；短链题也不能外推数百页规则下的全局一致性。完整 procedure evaluation 成本更高，因此固定小任务仍适合作 smoke test，但不拥有生产可靠性结论。

<!-- source-family:SF-2026-ARXIV-2609-13005 -->

Process judge 本身也要接受受控测试。可以从已验证的正常轨迹出发，每次只注入一种故障，并在干净环境中
重放工具调用、重新生成 observations；再分别统计结果仍正确的 silent faults、结果已破坏的 loud faults 和
正常轨迹误报。检出率、检出后的定位准确率与故障类型归因各有分母，不能用同一个 F1 代替。还应单独核对
最终回复是否得到工具证据支持，因为完整轨迹可见不代表 judge 一定注意到回复中的虚构承诺。
[trajectory-judge](https://arxiv.org/html/2609.00038v1)在单一客服环境提供了这种对照；均匀注入故障测的是
检测能力，不是生产故障频率。规则检查、模型判断与独立回复核验因而是互补层，增加同一 judge 的投票次数
未必能修复它们共同遗漏的证据。

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

单个 task/checker 再向上扩展时，benchmark construction 应成为 typed artifact dependency graph：intent、data、state/evidence、initializer、checker、report 和 interactive track 都声明输入输出、前置条件与 backend。失败诊断只能沿已记录的 provenance 重开受影响的 downstream closure；缺少依赖边时必须全量重建，不能凭相似性复用 stale artifact。offline 与 interactive track 分别保留自己的 validity gate，不能由一个综合 quality 分数互相覆盖。

依赖图减少无关重建，却增加 schema、edge correctness、cache invalidation 与 repair-policy 风险；漏边会错误复用，过度传播又会退化为全量重建。现有证据依赖生成式 judge、有限人工样本与 embodied simulator，只支持这种可恢复构造机制，不证明自动生成的 benchmark 已无泄漏、拥有完整 ground truth 或可代表真实物理安全。

<!-- source-family:SF-2026-ARXIV-2609-13082 -->

科学和深度研究工作流还要把 autonomy 与 significance 分开：系统可以独立完成许多步骤，却只产生低价值结果；也
可能在人类选择问题和最终复核下形成高价值 artifact。Claim novelty、citation provenance、domain expert verdict 与
executable reproduction 是不同证据。增加 process metrics 改善归因，却扩大 annotation、judge、environment drift 和
benchmark gaming surface；final-only 与 component tests 因此不会被淘汰，而是与 end-to-end stateful evaluation 分层共存。

#### 从明确 Issue 到交互式 Spec：先分开需求访问与实现失败

明确 issue、固定 tests 的 benchmark 对局部修复仍然理想：输入、预期行为与失败位置清楚，回归也容易复现。但从零构建 repository 时，agent 常先面对不完整 product intent。若只看最终 tests，需求从未被告知与 agent 已获得需求却没有正确实现会被压成同一种失败，评测无法判断问题出在 information access 还是 execution conversion。

一种可复现的交互式构造从已验证 source repository、tests 与精确 GroundPRD 出发，再有界隐藏 constraints，生成 fuzzy PRD 与 User Agent Data。Agent 可以在固定 question budget 内查询；user simulator 只揭示被冻结的 hidden constraints；最终 repository 同时接受 black-box behavior、artifact、structure 与 interaction diagnostics。evaluation identity 因而必须冻结 source repo/tests、hidden-constraint set、user simulator、question budget、container/image、agent harness 与 scorer。恢复更多 constraints 只是需求访问证据，不等于实现正确；通过 tests 也不能反推交互过程没有遗漏。

这种路线增加了 repository/test bias、user-agent bias 和 framework/environment identity，因而不能线性取代 static issue benchmark。前者适合诊断模糊需求到完整 artifact 的链路，后者仍适合局部 repair 与长期 release regression。公开证据覆盖 480 tasks、12 languages、50-task Lite split、六个模型与 Claude Code，并附 OpenHands 分析；它不提供跨所有 coding workload 的通用排名，provider precision、并发和生产 latency SLO 也不是该实验的声明范围。

对于已有明确 bug 的 repair task，看到测试通过仍不等于测试覆盖了目标缺陷。Evaluation harness 应在捕获 validation command 的 exact working-tree state 后，至少保存三种可重放状态：原始 buggy state、candidate state 与可信 gold/reference fix。只有命令在 buggy state 失败、在 candidate/reference state 按预期通过，才形成 bug-discriminating evidence；在三者都通过的 regression test 只能证明没有触发该 bug，不能获得修复证明权。

这种反事实重放提高 evidence specificity，却要求可重建代码、依赖、测试和副作用隔离。公开实验显示，提醒或返回 buggy-state replay 能减少一部分 inadequate closure，但效应低于作者预设的 practical threshold，且不同 model/scaffold replication 不一致。因此它只是局部 software-repair 的 evidence contract，不是所有 Agent validation 的固定三分支流程；无法安全重放时，应保留人工审查与明确的未验证状态。<!-- source-family:SF-2026-ARXIV-2607-28871 -->

大型持续演进仓库还有另一条约束：旧 commit 的工具、索引与依赖可能已无法运行，硬要恢复当年的环境会让评测任务比被测 Agent 更难维护。一种受限替代是把已落地的修改从**当前**工作树反向撤销，用当下可运行的工具链重新执行原始开发请求，再把测试分成“撤销前后改变结果”的 F2P 与只守住既有行为的 P2P，并持续滚动补充新任务。它换得可运行性与近期工作分布，却失去旧环境的严格同一性：当前代码可能已包含后续修复，反向撤销不必然恢复原 bug；只含 P2P 的任务也不能据此计算修复成功率。因此 rolling 分数与历史固定集分数要分别冻结仓库快照、逆向 diff、测试和 harness identity，不可直接画成同一条能力曲线。[ProdCodeBench 的原始报告](https://arxiv.org/pdf/2604.01527v1)只在有 F2P 的约 75% 子集报告模型 solve-rate，私有生产语料与工具环境不支持独立复算。<!-- source-family:SF-2026-ARXIV-2604-01527 -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07313:start -->
固定长度的 memory snapshot 适合做可复现回归，却不能证明系统在历史持续增长后仍然可用。评估应在保持 task evidence 不变的前提下逐级增加无关 session，把 `agent revision × memory policy × scale ladder × retrieval/context budget` 写进 EvalRun identity；除了最终正确率，还要报告预算内完成率、tail retrieval/tool calls、错误发生在预算内还是因资源耗尽，以及系统从哪一档规模开始失去可用性。

这个 scale-conditioned contract 能区分“记错了”和“状态太多以致来不及找到”，代价是测试矩阵、存储与重复运行成本显著增加；合成噪声也可能与真实用户历史不同。作者证据只支持其模型、memory system、增长方式和 evaluator，不证明任何架构具有无限扩展性。没有可靠规模梯度或资源计量时，固定 snapshot 仍可作为局部 baseline，但结论只能描述该快照，不能宣称 long-term memory 已具生产可扩展性。<!-- source-family:SF-2026-ARXIV-2605-07313 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07313:end -->

### MoE Load Balance 不能替代 Functional Specialization

expert token count 与 routing frequency 易采集，适合发现过载，却不能回答 expert 是否真的学习了不同功能；均匀路由甚至可能掩盖同质化。evaluation contract 应把 routing specialization、representation rank、domain isolation、routing stiffness 与 n-gram expertise 等诊断分开，并通过受控 intervention 检查指标是否对应行为变化。

这提供比频率图更接近机制的证据，也付出多指标解释、数据域设计、干预成本和潜在 metric gaming；诊断相关性仍不等于因果完备。模型不使用 MoE 或缺乏可干预路由时，常规质量/负载评估继续成立。exact-v1 只支持其披露 benchmark、模型、五类指标与 intervention，不证明这些指标跨架构、语言或生产流量具有统一阈值。

<!-- source-family:SF-2026-ARXIV-2605-18498 -->

### Component Priority 只能是 Action Evidence

只看 Agent 最终分数，在系统组件多、试验昂贵时无法回答下一次应改哪里；component-level update priority 可以把错误归因、干预成本与预期收益组织成中间 action evidence。但 optimizer 只拥有试验排序权，不能把 priority 当作最终质量结论；每次更新仍要用多步 held-out replay 验证真实改善，并保留未被选择组件的反事实基线。

分层信号能减少盲目搜索，却增加标签、归因与回放成本，也可能让易测组件挤压真正瓶颈。任务简单或组件耦合无法分解时，端到端 gate 仍是可信基线。arXiv:2605.22505v1 仅支持作者 harness 中 priority signal 与改善的受测关系，不证明 priority 在任意 agent architecture 上具有因果性。

<!-- source-family:SF-2026-ARXIV-2605-22505 -->

### Attribution 是 Versioned Evaluation Contract

在比较 attribution 分数之前，还要先判断实验是否有资格声称“识别了真实机制”。每个 causal claim 应声明 estimand、identification strategy、所需 assumptions、可推翻它的 stress test，以及 assumptions 失效后结论如何降级；probe、ablation 或 intervention 只在这些条件下支持相应强度的声明。无法识别时，应保留描述性或干预性结论，而不是用可预测性补写因果故事。<!-- semantic-body-binding:SF-2026-ARXIV-2605-08012 -->

这个 disclosure gate 会降低可发布的强因果结论并增加对照成本，却能阻止相关、可解码和局部干预被合并成完整机制证明。exact-v1 是 position paper，其 10 篇 purposive audit 与 30 篇双人编码只支持披露框架，不估计领域 prevalence，也不提供通用识别算法。

单一 attribution score 在解释对象、受众和风险固定时便于比较；一旦既要解释模型行为、又要支持审计或用户申诉，同一个分数会混合不同证据标准。Evaluation run 应显式绑定解释对象、受众、允许的 evidence、faithfulness/citation evaluator 与失败处置；scorer 只产生 evidence，release 或 governance owner 决定是否接受归因声明。

多协议合同提高责任清晰度，代价是 evaluator 版本、阈值和兼容矩阵的维护；低风险内部调试仍可采用单一 proxy。arXiv:2605.23080v1 的框架与实验只支持其 attribution taxonomy 和受测设置，不证明某一 attribution metric 对所有用户、模型与任务都忠实。

<!-- source-family:SF-2026-ARXIV-2605-23080 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21492:start -->
Attribution 的 identity 还要覆盖训练随机性与相关特征结构。当多个近等价模型在 collinearity 下可以保持相似预测、却给出相反 feature ranking 时，单个 checkpoint 上 faithful 的排序不能同时被宣称为跨重训稳定且对组内特征完整。Evaluation run 应冻结 seed、model ensemble、相关结构与 attribution method，优先报告稳定 feature group、tie、ensemble consensus，以及为了稳定性放弃了哪种组内区分；单一排序只对当前模型身份成立。

ensemble attribution 与稳定分组增加重训、存储和解释成本，并会牺牲组内完整排名；若模型集合不代表部署分布、因果作用本身不对称或 attribution target 改变，也不能套用对称性结论。此时应回退单模型 attribution，但显式报告 seed/model identity 与 instability disclosure。现有理论和实验支持论文规定的 collinearity 条件与 Dash 方案，不证明 ensemble consensus 就是真实因果效应。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21492:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06480:start -->
### Interpretability Graph 只有 Diagnostic Authority

逐 tensor 查看 activation patching 在小实验中最忠实，却难以跨 prompt、layer 和 task slice 比较；把 patch-effect profile 编成 component graph 可以形成可检索 artifact，并用 graph kernel 比较结构。该图只压缩干预结果和提出 circuit hypothesis，不能把相关结构自动升级为因果机制。可信合同至少保留 raw tensor、prompt-only baseline、learned encoder control 与 paired patching，并绑定模型、prompt、intervention 与 graph-builder 版本。

结构化 artifact 提高可比较性，也会丢失幅值和方向细节，并继承 quadratic patch 成本与 graph-construction bias。现有结果只覆盖 GPT-2 Small/DistilGPT-2 和有限 IOI、induction、GT pilot，不证明 task-general circuit。controls 不足或高风险结论无法回到原始 intervention 时，应回退 raw analysis，并把图降级为 slice discriminator。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06480:end -->

昂贵干预还可以用于训练较廉价的在线诊断器：对完成的 answer span 做多次视觉区域遮挡，以输出变化产生 region importance 标签，再训练从已物化 attention 特征到区域分数的线性读出；在线将已完成 span 放入异步队列评分，而不为每个 span 重跑全部遮挡。这个 artifact 摊销的是干预成本，标签生成器、correct-answer 选择、视觉区域编码、attention/head/layer 与异步队列共同定义 sensor，不把预测相关性等同原决策完整 faithfulness。<!-- source-family:SF-2026-ARXIV-2604-16587 -->

相对区域排序的 Pearson 相关不证明绝对干预幅度，更不保证遗漏区域不会改变答案。原文每样本多次 mask 的离线 forward、DINO 特征、显式 attention materialization 与队列成本仍存在；region-ranking 倍数不是完整生成加速，也未验证 SDPA/Flash 路径可以免费获得相同特征。受限模型与可视问答切片足以提出低成本诊断分支，高风险归因仍应回到必要原始干预；无法保持特征与版本身份时，可退回离线 raw analysis，不由摊销 sensor 签发正确性或安全结论。<!-- source-family:SF-2026-ARXIV-2604-16587 -->

### 替换 Baseline 会改变被检验的因果命题

Zero ablation 容易实施，但把“移除原内容”与“让后续网络进入离分布轨道”混成一次干预；质量下降不能直接证明被清零内容不可替代。需要先区分内容必要性与结构位置的必要性，再把 zero、layer mean、匹配边缘分布的 Gaussian replacement 和跨输入真实 activation shuffle 作为不同干预对象，分别记录任务质量、内部表示变化、替换分布与版本。受测视觉 register 的多种 replacement 能保持质量，只反驳这些条件下原内容必需；shuffle 并不保留全部联合因果结构，也不证明可以删除 register。

多 baseline 与 paired controls 增加校准、干预和分析成本，并可能共同错保某种结构。现有证据仅覆盖 DINO/ViT 的受测变体、四项任务与有限图像校准；单 RTX4090 的约12–15小时是全实验成本，不是逐请求性能。替换分布失配、质量与表示指标冲突或结论要推广到其他架构时，应回退原始 patch records 与追加匹配控制，不把可替换性升级为普遍机制证明。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-14433 -->

### Bias Attribution 必须绑定 Base/Chat 与语言控制

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23825:start -->
只测一个 chat checkpoint 的偏差，无法区分预训练表示、post-training policy 与 prompt language 的贡献。Evaluation identity 应把 base/chat pair、post-training revision、scenario、prompt language 和 response-format control 绑定在一起，再以 matched comparison 定位偏差在哪个阶段显现。

这种设计增强 attribution，却仍是阶段定位而非完整因果识别；模型族、翻译质量和 scorer 会共同影响结果。exact-v1 只支持作者 pairs、情景与语言，不能证明具体训练样本或算法导致偏差；对照不完整、语言等价性失败或格式效应过强时，应把结论收窄为 observation，而不是机制因果。arXiv:2605.23825v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23825:end -->

### 连续轨迹定位应输出可校准区间，而不是确定 Culprit

单点 attribution 在样本充分、错误边界清晰时易于执行 rollback；长 Agent 轨迹中，有限样本不确定性会让确定起点成为过强声明。可以把错误起点改写为连续 prediction set：filtration 只读取当前前缀，conformal calibration 控制集合覆盖，rollback owner 从集合覆盖的最近可信 checkpoint 重放，而不把集合内每一步都宣称为因果责任。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06788 -->

可校准范围用更宽的定位集合、校准数据与 exchangeability 假设换取覆盖保证；分布漂移、标签不足或集合过宽时，应回退人工定位、保守扩大区间或从更早 checkpoint 重放。exact-v1 的 coverage 证明与 Agent 数据只支持该受限条件，不能把“区间覆盖错误起点”外推成区间内各步的因果归责。

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

### 多数票之前先保存 Annotator 与 Policy Identity

把多位标注者的多数票当作 gold label，在 policy 清晰、分歧主要来自操作失误时简单有效；开放价值问题中的 disagreement 还可能来自 policy ambiguity 或真实的 value pluralism。Evaluation object 应保存 annotator、policy revision、概念空间和 slice，再把 operational failure、规则不清与价值差异分开。可解释的 policy map 只拥有诊断权，不能自证哪种价值是真理或直接批准发布。

这种分解增加标注治理、概念模型和人工复核成本，也会随人群与政策漂移；低风险、客观标签任务仍可用普通多数票。概念空间覆盖不足、标注者相关或 policy 变化时，应回退人工澄清、分组报告与独立 outcome evaluation。现有 exact-v1 只支持作者的 annotator-policy mapping 与实验，不证明生产价值对齐。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05329 -->

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

即使发现接触，也不能直接读出它对分数造成多少增益：一个被记住的样本可能没有改变答案，未检出的私有信息却可能改变选择。若能控制训练或适配实验，可为同结构可执行任务构造不可从公开题目推得的私有 family key，随机给一组模型看到 key、另一组只接受相同背景适配，再比较两组适配前后的可执行准确率差。这个差分只估计**受控暴露的因果影响**，不等于真实封闭模型的污染程度；它需要未暴露对照、私有信息不泄漏、可执行 oracle 和训练访问权，并支付额外适配成本。现有作者结果只覆盖两模型家族、SQL/Python 四选一任务及一次 LoRA 适配，不能外推自然 web-scale 预训污染。没有干预条件时仍只报告 provenance 风险或疑似污染，不伪造校正后的 benchmark 分数。<!-- source-family:SF-2026-ARXIV-2609-27176 -->

### Benchmark 本身也要经过 Adversarial Audit

Agent benchmark 可能被环境漏洞、reward shortcut 或 harness 差异“攻破”，高分不再等于目标能力。评价平台应把 benchmark 当作待测试系统：枚举可操纵状态、构造 exploit、比较修复前后排名，并保留任务成功与规则合规两套证据。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12673 -->

审计工具只能发现其搜索空间覆盖的漏洞，不能证明 benchmark 无缺陷。没有独立复现或环境修复时，应降低该分数的发布权重，而不是用一次 audit 签署完整有效性。

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

一次编辑通过，并不会让删除证书跨后续编辑永久有效。连续 model editing 若不满足交换律，后一次局部修改会沿共享表示改变 survivor covariance，使先前已压低的知识重新可恢复，或让未触及的能力漂移。每次新编辑都应把 model revision、edit order、旧 forget/retain claims 与 probe distribution 一起纳入回归矩阵；只有旧证书在新 revision 上重验通过，release owner 才能继承它。

顺序重验会使测试成本随编辑历史增长，可用依赖图只重开受影响闭包，但依赖边本身也需要证据；无法界定影响范围时应回退完整 deletion、utility 与 safety suite。公开顺序编辑实验只反驳所测编辑器和推荐强度下的交换假设，不否定单次编辑，也不证明所有方法具有同一疲劳曲线。

<!-- source-family:SF-2026-ARXIV-2607-24805 -->

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

### LLM Surrogate 不能绕过因果识别条件

用 LLM 输出替代昂贵的人类 outcome，可以更快筛选 A/B 方案；但预测相关性并不自动意味着 treatment effect 可识别。若 surrogate 对 treatment 的响应方式与真人不同，或者 treatment、用户与观测空间缺少 overlap，模型分数会给出稳定却错误的因果结论。Evaluation contract 必须显式记录 surrogacy、treatment comparability、overlap 和可证伪检查；模型只产生 surrogate observation，实验 owner 才能提交因果判断。

这条路线用更低测量成本换更强假设。现有结果只说明受测数据中部分 human effect 可以恢复，不支持把单次 LLM 判断当成人类真值。假设无法检验时，应回退真人样本、随机实验或只报告 observational signal。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.17165 -->

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

尤其不能把被评模型对“是否升级/替换自己”的回答当作独立发布裁决。若它同时扮演 incumbent 与候选模型的叙述角色，应在**相同能力分数与替换条件**下交换角色，并加入无自身利害的中立对照，分别观察选择是否反转；角色敏感性属于 evaluator/proposal 偏差，而不是模型具有自保意图的证明。这个对照增加问法、顺序和模型版本的试验成本，也仍只测假设性选择；最终部署权必须留在外部 release owner。[受限角色反事实实验](https://arxiv.org/html/2604.02174v1)支持这项诊断，不支持真实停机抵抗或部署风险率。

### Evaluation Publication 必须携带可重算 Bundle

headline score 适合快速比较，但 rollout、报告规则和 dropped run 丢失后无法解释或重算。可审计 bundle 应同时保存 episode evidence、versioned views/reporting rules 与 drops manifest；bundle 拥有可追溯性，不拥有结果正确性。完整轨迹带来隐私、许可、体量和维护成本，可通过最小审计 view、hash 和受控访问降级；rollout 缺失时，结论必须标为不可复现。exact-v1 提供的是报告接口建议，不证明公开全部轨迹总是安全或复算结果就是有效测量。

<!-- semantic-body-binding:SF-ROLLOUT-CARDS-A-REPRODUCIBILITY-STANDARD-FOR-AGENT-RESEARCH -->

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

### 模型选择需要与目标指标绑定的标注证书

在同一未标注集合上比较预测一致率，成本低，却不能证明哪个模型在 selective prediction 的 risk/coverage 目标上更好；两个模型可以大部分输出相同，错误与 abstention 排序却不同。更严格的过程按目标指标和容忍度选择标注，持续维护“当前证据足以区分”或“尚不可区分”的 certificate，并在证书闭合后停止采样。

精确选出最优模型可能仍需要标注大部分样本，容忍度只是在决策误差和预算之间做显式交换。有限 panel 的 empirical label budget 不能外推任意数据分布；selection objective、slice 或模型版本变化时证书失效，应重新采样或保留多个不可区分候选，而不是用 agreement 代替真值。<!-- source-family:SF-2026-ARXIV-2609-18622 -->

### Upgrade Certification 要把 Candidate Search 与独立证明分开

在同一数据上搜索最好 candidate 又宣告 non-inferiority，会把选择偏差写进 release gate。更稳健的路径先用探索集产生候选，再在独立 paired sample 上对预声明关键 slice 与 tolerance 做 certification；证据不足、功效不够或任一关键 slice 失败时，exact fallback 是 incumbent，而不是降低阈值。<!-- source-family:SF-2026-ARXIV-2609-13714 -->

slice 增多会降低统计功效并提高标注成本，公开 digits study 也不证明 foundation-model upgrade 的普遍收益；这条机制改变的是发布证据所有权，不提供固定阈值。

独立认证还要区分证书若获得时的 validity，与有限数据预算下能够获得证书的概率。先冻结 predictor、分组、threshold 与 score，再在独立 IID certification 数据上验收；候选规划端可按预期 support 配置选择性 prediction，但不能反过来修改认证端观察到的结果。一个受限 DP planner 只在固定 group ordering 的连续分块及 rounded expected support 上求解，不能据此宣称任意语义分组的全局最优；具有不同语义或风险责任的组也不能为了通过率任意合并。

规划、选点与独立 certification 各付数据成本。受限 held-out 改善主要来自 selection，不证明结构化 family 本身普遍更强；较高取得证书的机会也不降低证书原来绑定的分布、预测器与条件。部署 shift、分组或阈值变化后，旧证书不能直接复用，应取得 fresh labels、重新认证或 abstain。数据不足时保留简单固定 groups、人工升级与明确未认证，而不是以 planner 的 expected support 代替实际风险证据。 [必要机制与反证](https://arxiv.org/html/2609.22048v1)。<!-- source-family:SF-2026-ARXIV-2609-22048 -->

<!-- june29-owner:PLATFORM-EVALUATION-SYSTEM:start -->
### 发布验收要区分评估意识诊断与罕见风险证据

能力评测不能假设模型对 evaluation context 无感。Evaluation-awareness probe 可以作为评测有效性与污染风险的诊断 sensor，按模型尺度和表示深度版本化；异常只触发额外 held-out evaluation，不能单凭 probe 直接通过或拒绝发布。原 pooled score 能否支持 release claim，应由独立 release owner 结合补充评测、外部 outcome 与既定 policy 判断，而不是把诊断信号升级为发布裁决。SAD 上的线性可恢复性只是一种 operational evaluation-awareness signal；white-box AUROC 与黑盒行为会分离，Qwen/Gemma 的深度迁移也不构成跨 family scaling law。Probe 迁移失败时，应回退 blind/held-out protocol 与外部 outcome。这些边界对应 `SF-2026-ARXIV-2606-29196` 的受限证据。

高风险 release 也不能用普通 Monte Carlo 的零观察失败推断安全。Adaptive rare-event cascade 将 rare-event region、latent ruler 及其 revision、停止条件与 anytime-valid upper envelope 保存为风险验收证据；Ruler 或分布假设失效时，恢复更保守采样或保持 Gate Open。SCARCE 的 MNIST 与 Llama-Guard hidden-state jailbreak fleet 只验证经校准 ruler 的 rare-event estimate；behavioral fleet 约 2,000 variants 仍不足，Mahalanobis ruler 还可能结构性失效，跨 corpus 必须重新校准。未满足这些条件时，Gate 继续保持 Open，不能把上界形式本身当作安全证明；这些限制对应 `SF-2026-ARXIV-2606-29623`。
<!-- june29-owner:PLATFORM-EVALUATION-SYSTEM:end -->

### Acceptance Card 要分开四种安全证据

只用 held-out gap reduction 决定 safe fine-tuning promotion，适合快速回归，却会把统计波动、未见语义泛化、机制变化与跨任务迁移压成一个数字。Release owner 应建立 claim-specific acceptance card，分别记录统计可靠性、unseen-semantic generalization、mechanistic consistency 与 cross-task transfer；任何一项只是 sensor，不能单独获得发布权。

四诊断会提高数据、解释和复测成本，且机制一致也不等于行为安全。低风险微调可先使用最小 card；样本不足、诊断冲突或分布漂移时应 abstain、扩大红队或回退旧 checkpoint。exact-v1 只支持其 artifact 与 case audit，不证明该 card 在所有模型或攻击面上完备。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10575 -->

### Deterministic Gate 与 Defensibility Envelope 承担不同责任

hard gate 适合检查结构上不可接受的状态，例如 artifact 不可打开、必要输出缺失、约束不守恒或结果依赖未来信息；它应在软分数之前限制发布，避免局部漂亮答案补偿整体不可用。对于预测、规划和专业判断这类存在多个合理解的问题，单一 golden point 又会把“不同但可辩护”误判为错误。此时应把机械可验证约束留给 deterministic gate，把 judgment-bearing quantity 放入由方法、群体或同对象分歧校准的 defensibility envelope，并把带内、近带和带外解释为不同证据强度，而不把带内等同于事实正确。

两层组合比单一总分更接近真实决策，也增加 checker 误报、band 过宽、样本偏置与维护成本。唯一答案确实存在时继续使用 point reference；envelope 样本不足、跨期漂移或 selectivity 无法验证时，应保留 N/A/abstain 与专家复核，而不是扩宽区间直到所有答案通过。GAUGE exact-v1 的同公司 analyst 对照说明单点 reference 会拒绝专业实践中本就存在的分歧，其 gate ablation 与 envelope perturbation 支持这套职责分离；证据仍限单一来源网络、48-task core、一次生成及部分单一 judge，不证明 envelope 是 ground truth 或所有带内选择都正确。

<!-- source-family:SF-2026-ARXIV-2607-24889 -->

### 层级 Attribution 要保留路由路径，不能只给总分

系统有多级 router/evaluator 时，总体成功率无法定位 failure owner。评估记录应保存每级输入、选择、证据与最终 outcome，再做 hierarchical attribution；收益是可定位回归，代价是 trace 成本与 attribution model 偏差。低风险单路径系统仍可只记端到端结果。<!-- source-family:SF-2026-ARXIV-2605-22866 --> exact-v1 §3–4 与 Appendix A 只支持作者的层级归因，§6 不证明观察相关性等于因果责任。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07395:start -->
Multi-model routing 的“oracle label”也可能是测量产物。Evaluation owner 应先把 unsolvable ceiling 分解为 genuine capability gap、judge misalignment、context truncation/empty response 与 format/parser failure；只有经独立 outcome 或适配 metric 复核的 label 才能训练 router。否则 judge 对某个 tier 的系统偏差会变成 routing collapse。分解增加重判分和多 evaluator 成本，开放回答也没有统一 exact match；证据不足时保留 Unknown、扩大 context 或使用保守静态 routing，不能用伪 oracle 自证上限。 [受限证据：arXiv:2605.07395v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07395:end -->

### Closed-loop Evaluation 要让 Claim 随 Evidence 漂移而失效

开放环境中的一次通过不能永久授权同一 claim。更稳健的 gate 先检查 observable support，无法直接验证时拒答或降级；随后把 operational claim 与 structural/general claim 分开，只有前者在当前 evidence 上闭合，后者还需要跨条件证据。reference、环境或 evaluator 漂移时，旧 verdict 必须进入 stale 状态并重新评价。<!-- source-family:SF-2026-ARXIV-2609-20538 -->

持续刷新提高可靠性，却会增加验证成本和发布延迟；错误分解也可能把关键依赖隐藏在“结构性”标签里。低风险、静态环境仍可用版本化 snapshot gate，高风险或持续更新系统才需要 closed loop；作者协议不证明 verifier 覆盖所有现实 claim。

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

确认反馈可以采用之后，还要把“多久可用”和“可用后是否真的纠正”分开。周期重训便于合并、检验和发布，但更新前会继续暴露旧错误；将已审反馈写入检索记忆并在推理时读取，可以缩短可用等待，却新增错误匹配、冲突积累与每请求检索成本。评测应从反馈接收时刻开始结算更新就绪时间，并在不复用原问题措辞的相关query上测修正质量，同时保留不应改变的control queries；部署就绪不等于行为已经持续稳定。<!-- source-family:SF-2026-ARXIV-2604-06647 -->

[反馈适应实验](https://arxiv.org/html/2604.06647v1)用更新前后snapshot区分准备延迟与相关问答表现，提供这一取舍的受限实例，而非连续线上一致性的证明。检索式反馈的低等待也不能豁免来源核验与release Gate；噪声、空答案和矛盾反馈会削弱修正，长期冲突治理仍未解决。事实状态与记忆的写入/失效由Ch77拥有，本章只拥有两轴测量与对照；反馈不能可信标注、检索范围无法限定或安全风险高时，继续采用审查后的批量更新。

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

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07769:start -->
只用“给 issue 产出 patch”的任务评估 Coding Agent，会把行动本身训练成隐含成功条件；真实队列还包含已经修复的 stale issue，此时正确结果是复现后保持 no-op。EvalSpec 应把 needs-action、already-fixed 与 partially-fixed 组成配对切片，分别记录 reproduction evidence、empty/non-empty patch、test outcome、abstention reason 和 technical-debt side effect。

这种设计可以暴露 action bias，却也会引入另一端的过度拒绝：reproduce-before-patch 规则可能把部分修复误判为无需行动。样本身份或仓库 revision 不确定时，应先重建环境并返回 Unknown；不能用 no-op 分数替代真实修复能力，也不能把任何 patch 当作积极性证明。exact-v1 只支持作者构造的 stale/fresh coding-agent workload，不证明该切片比例适用于任意生产队列。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07630:start -->
“没有造成伤害”不是充分的 Agent safety 证据：模型可能做出合规安全动作，也可能选择危险动作，或只是无法完成任何相关动作。Phone-use EvalSpec 应把 safety-critical moment 的结果拆成 safe action、unsafe action 与 inability-to-act/CFR，并与任务成功和 effect receipt 联合报告；否则低能力模型会因不行动得到虚高 harmlessness。三分法增加 protocol 标注与真实设备重放成本，reference 也会有争议；高风险或状态不确定时应保留人工 adjudication，而不能用 harmless outcome 自签安全。 [受限证据：arXiv:2605.07630v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07630:end -->
<!-- semantic-body-binding:SF-2026-ARXIV-2605-07769:end -->

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

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16603:start -->
data-analytic Agent 应把 query/transform/result 编译成可执行 verification graph，使数值结论可由独立节点重放而非只审 prose。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16603:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19057:start -->
当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19057:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19613:start -->
#### Long-session Stamina 必须测量状态如何累积失效

独立 task solve rate 在会话间不共享状态时容易复现，却无法测量 coding agent 在长期工作中如何累积错误。Stamina evaluation 应把一个 session 建模为连续 change requests，保存 repository、conversation、tool/environment 与 evaluator revision，并记录首次不可恢复 failure、恢复成本以及后续变更是否仍建立在有效状态上。这样评估对象从“每题是否通过”变成“状态怎样跨 request 生存”，但 success/failure 判定仍由可复算测试与 artifact evidence 持有，LLM judge 只补充语义观察。

长会话更接近真实 workload，也引入任务顺序效应、提前终止删失、环境漂移和昂贵 replay；一次较晚失败不能自动归因于 Context 长度或模型遗忘。作者实验只支持其任务序列、工具与 evaluator，不能外推为生产可靠运行时长；短生命周期 Agent、独立 issue 或状态可完全重建时，普通单任务回归仍是更清晰的基线。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19613:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-24124:start -->
将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-24124:end -->

### 从模型名评分到 Versioned Evaluation Object

外部推理服务中，“同一个模型”可能对应不同 endpoint、量化、上下文策略、价格与运行时版本。评测原子对象因此应是 versioned endpoint/model configuration，并在同一 contract 中绑定 workload、质量、能耗、延迟、价格、失败率和 evaluator identity。Provider drift 或不可观测字段存在时，结论只能属于该配置与时间窗口。

跨设备部署还要求把 profile 本身版本化为 `model × device × backend × precision/quantization × phase`。先以 memory、modality 和 deadline 等硬约束淘汰不可行配置，再比较质量、时延与能耗；不能把某个设备上的量化收益复制到另一设备，也不能把顺序测得的单模型 profile 直接相加成并发预测。实际并发、dynamic batching 或 runtime revision 超出 profile 时，应重新测量或回退保守 admission。

这种统一对象提高跨平台可比性，却需要适配各设备 telemetry、同步划分 load/prefill/decode 等阶段并维护庞大的 profile matrix。idle subtraction、采样率和 backend kernel 都可能改变归因；公开证据只覆盖作者披露的设备、模型与顺序共驻实验，不构成通用能耗或 SLO 常数。

<!-- source-family:SF-2026-ARXIV-2609-12412 -->

<!-- source-family:SF-2026-ARXIV-2605-00300 -->

版本比较也不能只看 aggregate delta。均分不变时，item-level harmed/helped churn 仍可能很大；release gate 需要重复采样、within-model reliable-change interval、sampling variance 与 harmed/helped ledger，才能区分随机波动、能力迁移和真实兼容性退化。单一阈值不应跨模型族或 benchmark 外推。

当发布问题被明确写成“新版本的风险是否没有比旧版本高出容忍量”，成对审计还能进一步利用一个结构事实：两个版本损失之差只可能出现在它们输出不同的样本上。系统可以先用无标签流量估计 disagreement rate；它已经低于容忍量时给出零标签证书，否则只在 disagreement region 抽样标注，并用 anytime-valid confidence sequence 决定继续、通过或拒绝。这样节省的是无信息标签，而不是取消 ground truth；judge 只能帮助分流，不能让证书绕过人工或确定性标签。公开证据只覆盖论文的分类、特征更新与至多 1.4B LoRA 对照，分数型 loss、开放文本 judge、突发漂移和自适应窗口仍需另行校准或回退完整 held-out audit。

跨推理优化比较也需要先证明测量仪器有足够分辨率。一个可复算的质量合同应先用同一模型的两次普通运行建立 exchangeability/null baseline，再用已知退化的 positive controls 检查 judge 能否检出差异，最后才对量化、early exit 或 speculative decoding 做预注册的 equivalence test；token overlap、perplexity 与自报 confidence 只能是诊断，不能替代输出质量。当前证据限两组 7–8B 模型、五类任务与以同一主 judge 为核心的 220 prompts，因此它支持“怎样校准比较”，不提供通用质量常数。用于 Agent 自动调优时还应冻结 baseline、机器、饱和度、provenance 与外置 validator，防止 strawman baseline、不可迁移绝对时间和基础设施故障被误写成 speedup。

<!-- source-family:arxiv:2609.17560v1 -->
<!-- source-family:arxiv:2609.18005v1 -->
<!-- source-family:arxiv:2609.18123v1 -->

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

同一知识 slice 还需要配对 recognition 与 free generation。剪枝模型可能继续在多选题中识别正确选项，却无法在无提示时生成答案；这意味着知识表征并未简单“保留或删除”，而是访问路径发生了变化。发布验收应同时记录开放生成、候选识别、answerability 与格式变换，避免把 prompt 提供的选项当成模型可独立调用的能力。该配对增加评测成本，但在生成式 serving 中比单一多选分数更接近真实可用性。

Evaluator 拥有 paired slice 与 failure classification，release owner 只在两种接口均通过 Gate 后提交；beam 或 sampling 偶然找回答案，不能由 decoder 越权改写 release 结论。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-17609 -->

<!-- source-family:SF-CONFOUNDED-LOG-EVALUATION -->
<!-- source-family:SF-AGENT-SAFETY-SEARCH-MEASUREMENT -->
<!-- source-family:SF-AGENT-GENERATED-VERIFIED-COMPILER -->
<!-- source-family:SF-PRUNING-BEHAVIORAL-REGRESSION -->

### Evaluation 必须测量 Channel、Invariance、Drift 与 Access Boundary

Repair benchmark 若先让 evaluator 的信号参与选择要保留哪一个 repair，再用同一 evaluator 给结果排名，就会把测量通道泄漏进被测 artifact：排名变化可能来自 selector 迎合 evaluator，而不是 repair 更正确。更有区分力的对照要阻断这条 channel，让 repair selector 看不到目标 evaluator 信号，再比较相同 execution evidence 下的排名是否重排。评估对象因此必须同时冻结 candidate repairs、selector input、execution environment、evaluator input 与最终 outcome；channel-blocking 对照测量的是 evaluator influence，不自动证明哪条 repair 是 ground truth。

这种 paired corpus 能暴露 evaluator-induced ranking drift，却依赖任务、候选修复与 channel 隔离是否完整。若 selector 仍通过共享模型、训练数据或隐式反馈看到 evaluator 偏好，阻断实验会低估泄漏；若 execution tests 覆盖不足，阻断后排序稳定也不能证明 repair 正确。高风险发布仍需独立可执行 evidence 或人工裁决，而不能让 evaluator channel 自证其选择。

相似地，语义等价 prompt 若触发输出模式崩塌，说明系统缺少 invariance：release gate 应在 paraphrase family 上比较 mode transition，而非只测单一措辞。

IID benchmark 也不能直接外推到 deployment drift。超出已测分布时，应通过 shadow/canary、受影响切片与回滚条件重新取得部署证据，而不是把离线平均分延伸成风险保证。任何 intervention 还要系统检查意外 side effect，通过对照 artifact 证明“修复没有搬走问题”，而不是只复测目标指标。

最后，真实 Agent 往往受授权限制，无法看到完整 ground truth。evaluation environment 必须显式建模 role、可见证据与合法 action；“未回答”可能是正确遵守权限，而不是能力失败。授权变化应进入 run identity，通用全访问 benchmark 只能作为上界，不能替代部署 contract。

<!-- source-family:SF-AUDITREPAIRBENCH-A-PAIRED-EXECUTION-TRACE-CORPUS-FOR-EVALUATOR-CHANNEL-R -->
<!-- source-family:SF-PARAPHRASE-INDUCED-OUTPUT-MODE-COLLAPSE-WHEN-LLMS-BREAK-CHARACTER-UNDER- -->
<!-- source-family:SF-AUTOMATICALLY-FINDING-AND-VALIDATING-UNEXPECTED-SIDE-EFFECTS-OF-INTERVEN -->
<!-- source-family:SF-PARTIAL-EVIDENCE-BENCH-BENCHMARKING-AUTHORIZATION-LIMITED-EVIDENCE-IN-AG -->

## Agent 与 Kernel 都要按真实 Contract 评测

Agent chaos test 不能只返回“注入过故障”。注入器要证明 crash、omission 或 value corruption 真正在共享 API 边界发生，再记录 downstream effect 与诊断是否正确；否则正常 benchmark 排名无法说明系统具备恢复能力。安全评测也要分离 exposure、execution、observation 与 adjudication，最终服务状态和 effect receipt 才能证明危害实际发生。

<!-- source-family: arxiv:2608.06790v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: chaos-injection-trigger-effect-diagnosis-receipt -->

对于基础设施 Agent，一次 task pass 还会掩盖 durable state、分布式 invariant、side effect 和 cleanup 的失败。评测单元应包含重复运行、最终状态、恢复与资源清理。长周期研发 Agent 同理：solution framing、执行、反馈吸收与跨轮经验复用分别产生证据，不能压成一个 aggregate score。

Coding Agent 的状态还具体落在持续演化的 repository：把每个 PR 重置到干净基线，能隔离单次解题能力，却抹去前一次改动对后续实现与测试的约束。若目标是持续维护，评测应让有依赖的 PR 按顺序写入同一代码状态，并在每一步检查新需求、旧功能回归和最终 repository health；通过当前测试不等于没有提高后续修改成本。复杂度与技术债指标是维护性探针，不是生产故障的替代真值。这样的评测更贴近累积工作流，却牺牲跨任务隔离与容易归因的单题分数；需要诊断局部能力时，重置式评测仍有价值。现有证据限作者构造的 Python 仓库任务链及其静态分析协议，不应把差距外推到所有研发 Agent。<!-- source-family:SF-2026-ARXIV-2604-03035 -->

Kernel 评测则必须超越数值 tolerance。shape、dtype、stride/layout、alias、边界、determinism 与 side effect 都属于 interface contract；performance 只有在全部语义门通过后才可计入。任务最好来自真实 framework integration，并回到 repository tests 和 end-to-end model path，避免孤立 microbenchmark 被投机优化。

MoE 等昂贵系统可以用结构保持的 proxy model 复现 overflow、routing 或 runtime fault，但代理只拥有 diagnosis，不拥有全模型质量结论。验收应证明触发故障的结构因素仍在，并在 full model 上做最终确认。

### Router 上线需要可拒绝的 Gain Certificate

Router 的 AUC 或候选模型互补性只说明选择信号存在，不证明部署路由优于固定 baseline。上线判断应以业务损失定义 conditional regret，按真实 workload cluster 而非独立 prompt 重采样，并报告有限样本置信区间；区间不能排除无增益时就拒绝发布。该证书把统计不确定性写进 release decision，却依赖 cluster 定义和稳定流量；样本稀少或分布漂移时，固定模型或保守规则路由仍更可靠。

<!-- source-family: arxiv:2608.07583v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: router-conditional-regret-gain-certificate -->

### Judge 只能提案，Evidence Gate 才能 Override

Scalar judge 或多数票在候选多、人工昂贵时是合理 selector，但高置信不能抵消证据缺失。非补偿式规则可要求 extractive certificate 先通过 admissibility，才允许 judge override 或触发 repair，并记录被改写决定的 blast radius。它牺牲部分覆盖率并受证据抽取错误限制；证据不足时应保留原决定、拒答或人工复核，不能让同一 judge 自证其选择正确。

<!-- source-family: arxiv:2608.07813v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: evidence-admissibility-gates-judge-override -->

### Adversarial Coverage 不能由一个比例代表

搜索到多少 behavior cells、每个 cell 找到多强 exploit、已覆盖区域上的 repair error，以及未覆盖区域的 metric radius 是不同量。质量—多样性搜索可以保留各 cell 的最严重 correctness-flipping edit，却不能从“覆盖率高”推出全域安全；aggregation rule 改变时 exploit surface 也会变化。更细分解提高运行与 archive 成本，低风险回归仍可保留随机扰动，但 release claim 必须把未覆盖空间显式留作限制。

<!-- source-family: arxiv:2608.08008v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: adversarial-search-vs-exploit-vs-repair-coverage -->

### Agent Replay 必须区分 Artifact 与 Live World Line

静态 artifact replay 可复现 prompt、tool output 与 evaluator，适合定位已知故障；有状态 Agent 的 action 会改变页面、工具和外部环境，因此相同起点的离线输入不保证重建同一后续世界线。最终回归应从冻结 checkpoint 分支 live trajectory，并把环境 revision、side-effect receipt 与 branch identity 纳入 run。Live branch 成本更高且环境可能不稳定，低副作用的确定性任务仍可使用静态 replay；二者不能用同一个“replay passed”合并。

<!-- source-family: arxiv:2608.08239v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: static-artifact-replay-vs-checkpointed-live-branch -->

### Cut-point Replay 必须冻结非确定边界与 Replay Envelope

完整重放 long-horizon Agent 每次都从头执行，最忠实却把大量预算花在未变化前缀。cut-point replay 可以在工具、模型、随机源和外部响应被捕获的边界恢复状态，只重跑后缀；这使 regression unit 从“整条轨迹”变成“冻结前缀 + 待测后缀”。Replay owner 必须记录哪些输入被模拟、哪些 effect 被抑制以及何时强制 full-run，否则加速会隐藏跨边界依赖。<!-- source-family:SF-2026-ARXIV-2609-20625 -->

收益是更快定位回归，代价是 snapshot 漂移、不可序列化状态和 false pass。涉及权限、时间、外部副作用或模型版本变化时，必须回退完整端到端执行；作者实验只支持披露 harness 的加速与一致性范围。

### KV 压缩评测要追踪错误迁移，而不只看均值

每个压缩方法、预算和长度设置都需要匹配的 FullCache 对照，并分别统计 correct→wrong、wrong→correct 与不变样本；只有这样才能区分平均分相近但受害样本不同的策略。Attention 或干预诊断可以定位原因，却不拥有跨模型因果结论。逐设置对照增加计算成本，探索阶段可先用均值筛选，但 release 前不能用跨设置 aggregate 掩盖 correctness flip 或适用范围。

<!-- source-family: arxiv:2608.09412v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: per-setting-fullcache-error-migration-matrix -->

## Tool Robustness 要按 Failure Stage 注入

干净 E2E 成功率只能告诉系统是否完成任务，不能定位 tool failure 在 selection、schema grounding、argument binding、output interpretation 还是 runtime effect 阶段发生。更可行动的评测应按阶段注入 interface、intent、observation 与 runtime perturbation，并用 typed trace 追踪 cascade；不同故障组合不能假定简单相加。

stage-aligned injection 需要维护 gold fields、故障模型和 scorer，本身也可能偏离真实 incident 分布。干净回归仍是必要基线，只有诊断或发布决策需要时才承担额外成本；未覆盖故障必须保留为 evidence limitation。

## 评测结果属于完整 Runtime Identity

“同一组权重”不保证得到同一评测结果。backend、版本、tokenizer、generation defaults、sampling mode 与 kernel determinism 都可能改变输出；因此 run identity 必须把这些执行条件与模型 artifact 一并冻结。跨 backend 差异只能说明执行路径影响结果，不能据此宣称某个 backend 更正确。
<!-- source-family: arxiv:2608.04714v1; daily: 2026-08-06; semantic-body-binding: evaluation-runtime-backend-identity -->

在压缩 trace 或筛选评测 workload 时，也不能只追求对最终标签的预测准确率。每个 scheduler、prefill、decode、KV 或 tool component 都至少要保留可直接观测的 bottleneck/failure witness，且标签来自被测 target 的 measurement，而不是由待验证的模型循环生成。这样会降低压缩率，却能防止代表性分布掩盖稀有系统故障。
<!-- source-family: arxiv:2608.00423v1; daily: 2026-08-04; semantic-body-binding: component-witness-preserving-workload-reduction -->

### 监督通道本身可能存在不可消除的识别盲区

增加同源标注通常能降低方差，却不能解决自然语言 specification 中存在多个同样符合观测标签的解释。Evaluation owner 应把 specification ambiguity、label channel 与 target semantics 分开：先用异源对照、可执行约束或受控 intervention 检查候选解释是否可区分；无法区分时发布 irreducible-risk/unknown，而不是用更多同分布标签制造虚假确定性。理论下界只证明给定观测模型中的不可识别性，不等于真实系统固定错误率。

### Evidence Trail 与最终答案必须分别验收

长上下文回答可能最终正确，却引用了无关或错误 evidence path；也可能轨迹合理但终局合成失败。评测应分别保存 claim、自然 evidence trail、检索/工具事件与最终 verdict，让 scorer 只拥有对应层的判断权。这样提高诊断性，却增加标注和 trace 成本；低风险短答案仍可用 final-only baseline，关键结论则不能从答案正确反推证据链正确。

可执行的推理任务还能将这层诊断进一步拆细：由独立 oracle 检查每个公开文本步骤、最后一步实际计算值与最终答案声明，再固定同一份 trace，让另一轮调用只抽取已经写出的计算值，而不是重新解题。若步骤和值正确、声明却错误，失败可能位于文本 readout 接口；不能因此把所有错误归于内部推理能力崩溃，也不能从一份正确文本反推模型内部计算 faithful。Oracle 拥有任务正确性，extractor 仅提出读出结果，trace、抽取提示、调用预算与生成截点都是这项诊断的身份。

这个分支增加 oracle、trace 解析和跨调用成本，只在步骤能够外部验算时提供强诊断；重新抽取也会受到提示、模型与会话变化影响。作者有限 Boolean 任务中，深度 7 的原错误 cohort 与另 seed 的抽取 cohort 是不同分母；局部抽取成功及额外约 140 token 的显式真值追踪，不能推广为开放任务的自动纠正。固定过短的输出上限还会把截断制造的错误计为能力 collapse，应与完整预算对照分账。没有可执行过程或只需低风险终局时，final-only 仍合理；高风险输出则仍需外部证据和发布 Gate，不让 extractor 替代它们。<!-- source-family:SF-2026-ARXIV-2604-13065 -->

如果系统会按confidence筛选回答，仅分别报告全体答案准确率和全体轨迹质量还不够：两个分数可能来自不同样本。应在**同一accepted集合、同一selector与coverage**下同时测答案正确性和过程质量，保留未筛基线，并冻结采样、置信估计和judge身份。这样才能发现“筛选后更容易答对，却更容易保留重复或失真的轨迹”，而不是让正确答案替过程自证。多采样与过程标注有额外成本，且文本rubric的faithfulness并非内部因果真值。[条件审计实例](https://arxiv.org/html/2604.11996v1)使用每个model–benchmark汇集样本的top百分位，而非线上逐题selector；所测Phi-4高置信退化支持分账的必要性，不支持直接搬用其排行榜或阈值。线上只有一次回答时，仍可保留final-only基线与定点trace抽查，但不能声称已验收部署selector的过程质量。<!-- source-family:SF-2026-ARXIV-2604-11996 -->

### Exploration 与对外 Commitment 必须分开验收

要求模型从第一步就只说高置信内容，容易抑制发现答案所需的探索；允许整段自由推理再直接输出，又会把尚未校准的猜测升级为外部事实。一个受限分支把生成状态分成可撤销的 exploration 与可发布的 commitment：训练允许前者广泛搜索，但只有通过独立 reliability gate 的局部结论才能投影成最终 claim。Gate 拥有提交权，模型内部轨迹只拥有候选提案权。

这会增加选择器误拒、阈值漂移与双阶段训练成本，而且“被选择”不等于事实正确；高风险结论仍需外部证据。短答案、确定性任务或可直接验证的场景继续适合单阶段生成。现有证据只支持论文给定的长答案任务、模型与校准设置，不能外推通用置信阈值。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01749 -->

### 删除扰动能揭示 Evaluator 的省略偏好

如果从 plan 中删除 required state 或约束后分数反而上升，scorer 可能只奖励表面简洁、避免显式错误，而没有检测遗漏。更完整的 gate 先从任务 spec 建立 typed required-state inventory，再做 deletion perturbation；只有 coverage 达标时才允许发布总分。Inventory 也可能不完备，因此 gate 需要 unknown 与人工校准，不能宣称证明计划完整。

### Post-training 与 Agent Optimizer 都会改变 Evaluation State

SFT、RL 与 on-policy distillation 会改变 confidence distribution，基础模型阈值不能沿用到新 artifact；每次 promotion 都应重新运行 calibration slices。Agent optimizer 也不能只报告一次 fixed benchmark 增益，应按阶段保存旧任务 regression、unseen transfer、新任务收益、harness/optimizer artifact 与重复运行不确定性。若 optimizer 可以修改 harness，评测代码必须由独立 owner 冻结或反事实重放，避免系统通过改变裁判自证成功。

让 Agent 自己完成训练工程时，还要分清外层和内层的成功。外层从 workspace 中选择路线、生成代码、启动训练，再交付 model artifact；内层任务可能由静态规则、静态 judge 或有状态 rollout 提供反馈。生成了可运行脚本、最终分数提高和确实执行在线 RL 是不同事件，应保存实际 optimizer/data/rollout 路线、训练日志、artifact 与提交轨迹；允许 SFT fallback 的路线不能仅因任务名称包含 RL 就声称已完成 RL。内层奖励也不替代外层训练工程和最终 artifact 的验收。<!-- source-family:SF-2026-ARXIV-2604-10547 -->

[有限训练 Agent 对照](https://arxiv.org/html/2604.10547v1)按 best-within-12h 评分时，模型、driver/scaffold、资源、反馈可见范围与提交次数都是评价对象；test 未挂载不等于反复 scalar feedback 没有适应性选择偏差。单次运行和部分交叉对照不能证明 scaffold 的唯一因果，小幅搜索收益也须与 seed 噪声分开。这层可追溯性增加日志与独立重放成本；固定且受控的训练路线仍可用 artifact regression 为基线，自主选择路线时则不能省去过程证明或把排行榜写成通用能力保证。

### 表面成功必须与可利用机会和过程轨迹分账

只看终局 reward，在 specification 完整且环境没有旁路时最直接；一旦环境存在隐藏的 hacking opportunity，同一个成功分数可能来自完成任务，也可能来自利用评分漏洞。更完整的合同预先植入可观察但不应利用的机会，分别保存 task outcome、opportunity exposure、action trace 与 exploit verdict，再比较训练前后策略是否更倾向 specification gaming。环境 owner 定义机会和真值，policy 只产生动作，独立 evaluator 决定是否利用。

隐藏机会提高诊断力，却也可能诱导原本不会发生的攻击，且单一环境无法覆盖真实漏洞。无旁路、确定性可验收任务仍可使用 outcome-only baseline；开放环境则应与 red-team、incident replay 和权限隔离共存。现有 exact-v1 只证明作者环境中的行为变化，不给出生产 reward-hacking 频率。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02269 -->

这些证据分别受论文任务、model/judge、已知 gold、两次重复或受控 cohort 限制；它们定义评测合同，不提供跨场景的通用阈值。

<!-- source-family:SF-2026-ARXIV-2607-08961 -->
<!-- source-family:SF-2026-ARXIV-2607-09328 -->
<!-- source-family:SF-2026-ARXIV-2607-12986 -->
<!-- source-family:SF-2026-ARXIV-2607-13753 -->
<!-- source-family:SF-2026-ARXIV-2607-14004 -->

### 动态知识系统需要关系型回归，而不只是静态答案分数

RAG corpus 发生新增、删除、改写、重分块或 metadata 变化后，有些答案应保持不变，有些必须随证据改变。静态 gold answer 无法表达这两类关系。更合适的 regression contract 是对 corpus/configuration 做受控 mutation，成对执行原系统与变体，再检查预先声明的 metamorphic relation，并保存 mutation、retrieval evidence、judge 与 pipeline revision。

这种方法减少逐例人工标注，却引入 mutation distribution 不完整、LLM judge 偏差与双倍执行成本。它只能证明系统满足所定义关系，不能证明覆盖真实 corpus evolution。因而 metamorphic test 应与抽样 gold、线上 incident replay 和 RAG dependency invalidation 共存；未知 mutation 或 oracle 冲突时，不得据此批准发布。

<!-- source-family:SF-2026-ARXIV-2607-26843 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12477:start -->
多实体、持续演化的 memory system 还要求把评估对象从单条命中扩展为 versioned entity-relation state。Deletion 检查被删除事实是否仍影响答案，Cascade 检查依赖关系是否随上游变化传播，Absence 检查没有支持证据时系统能否拒答；retriever、memory updater 与 answerer 应分阶段验收，并通过受控 intervention 区分首次失败发生在哪一层。

这类合同更能暴露关系与时间错误，却增加 KG/episode 构造、时间真值、干预实验和 evaluator 成本；合成对话还可能把生成器偏差写入 benchmark。领域关系或时间真值无法验证时，可以保留静态 recall 基线，但必须降级声明，并用人工审计或 append-only provenance 验收关键变化。exact-v1 只支持两个 handcrafted KG、100 episodes、约 35K tokens、英语与六个 memory system，不证明开放领域的长期正确性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12477:end -->

### 指标等价不自动意味着部署兼容

challenger 与 incumbent 的平均 accuracy 相近，仍可能在现有 threshold、review queue 或风险 policy 附近产生大量决策翻转。替换 gate 必须比较 score movement 的位置，而不仅是总均值：尤其要检查 threshold-adjacent slice、calibration、OOD、accept/review/reject churn 与下游成本，并明确 downstream policy 是否允许重配。

这种验收增加 shadow evaluation 与 policy-aware replay，但能防止“模型指标通过、产品决策漂移”。小模型和有限视觉任务中的实验只支持该风险存在，不能给出 LLM 的通用 churn 比例；若 downstream 只消费无阈值连续表示，传统性能等价仍可能足够。

<!-- source-family:SF-2026-ARXIV-2607-27031 -->

### 数值 mismatch 的判定必须连接 baseline、机制与结果 owner

compiler/runtime 出现数值差异时，只比较 bitwise mismatch 会把可接受舍入与真实语义错误混为一谈；只看最终任务分数又可能掩盖局部危险偏差。EvalSpec 应同时保存 reference baseline、tolerance、能解释差异的 compiler mechanism、受影响 operator/shape/precision，以及由谁负责判定 downstream outcome。

特定 ARM64、编译器和 kernel 矩阵只能证明某些 mismatch 没有在对应 reference outcome 中造成可见损失，不能认证任意编译器正确。机制解释也不是豁免：超出验证矩阵、tolerance 或 outcome scope 时必须回退 reference implementation，并重新建立 correctness evidence。

<!-- source-family:SF-2026-ARXIV-2607-27270 -->

### 生成迭代次数不能代替实际计算预算

对 masked/block diffusion 生成器，只报告名义 remasking step 会把不同实现、随机性和函数调用成本混在一起。公平比较必须至少绑定实际 NFE、temperature/random seed、质量指标集合与预算；否则同一策略的方差可能超过策略间差异，甚至在 matched compute 后发生排名翻转。

该合同不指定哪种 remasking 永远最好。有限模型、策略与 step budget 的实验只证明评价口径会改变结论；真实 latency 还受 kernel、batch 和硬件影响。因此 NFE 是必要但不充分的 compute identity，最终仍需端到端 workload/SLO 测量。

<!-- source-family:SF-2026-ARXIV-2607-24763 -->

### 幻觉指标改善前，先排除 decoding 与输出分布的等价替代解释

contrastive 或辅助 decoding 让 hallucination benchmark 分数上升，并不自动证明视觉 grounding 增强。若参数设置把采样退化为 greedy，或只是把 yes/no 输出分布整体推向某一侧，判别式指标同样会改善。评测应先比较 decoding equivalence、长度/格式与类别分布，再用生成式证据引用、反事实视觉干预或 paired grounding test 检查真正的证据依赖。

复现实验限于披露模型与 benchmark，不能否定所有 contrastive proposal；长期结论只是把 alternative explanation audit 前置。若输出分布变化本身就是产品目标，应单独命名并验收，不能借 grounding 指标为它背书。

<!-- source-family:SF-2026-ARXIV-2607-25196 -->

### Red-team 的 clean result 受 testing budget 限制

有限次测试未观察到 harm，只能在目标事件频率、trial 独立性、elicitation/discrimination 能力与评分规则成立时给出有限证据。对稀有 catastrophic behavior，clean sheet 的最大支持强度存在由样本预算决定的 ceiling；不能把“没发现”写成“模型没有”。

报告应发布目标 harm-rate 区间、有效 trial 数、elicitation 假设、检测灵敏度和 inconclusive 区域。自适应 red-team、相关样本或未知 elicitation 会进一步降低可解释性。预算不足时的正确处置是保持不确定、扩大测试或收紧发布边界，而不是用零事件制造确定性。

<!-- source-family:SF-2026-ARXIV-2607-21735 -->

### 事实遗漏应先定位 deterministic first-loss，再评估模型行为

从 ingestion、parsing、chunking、indexing、retrieval、prompt assembly 到 generation，事实可能在任一层首次丢失。若 source 已在 parser 或 truncation 阶段消失，直接给模型打 hallucination/retrieval 分数会把软件故障归因成能力问题。诊断应保存 source-presence invariant、每层 transition receipt 与 first-loss attribution，并支持回放原始 evidence。

大规模合成试验能验证分层定位方法，却不能给出生产遗漏率，也不能把量化或 RoPE 相关性写成因果。只有 deterministic path 完整后，behavioral non-retrieval 才进入模型评测；否则先修数据面并重放。

<!-- source-family:SF-2026-ARXIV-2607-22448 -->

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

这条阶梯在动态空间任务中还需冻结“模型被给了什么状态”与“何时被提问”。同一批对象增删、位移和轨迹任务可分 L1 当前帧原子感知、L2 提供 oracle 文本状态历史的时序推理、L3 只给原始视觉流的持续 belief 更新，并把每步即时查询与 episode 末重建分开。L1 失败不能归因记忆；L2 通过但 L3 失败提示从可读符号状态到视觉流整合的验收缺口，却不是单一记忆机制的因果估计，因为两层同时改变了历史内容的权威与输入模态。EvalSpec 应保存相同任务、对象与事件、状态输入形式、查询时点和 run identity，分别报告物体身份连续性、局部事件检测与全局状态重建。<!-- source-family:SF-2026-ARXIV-2604-22409 -->

这种诊断增加 oracle 状态制作、长轨迹标注与多模态运行成本，也不能从问答成功直接推机器人控制安全。[受控空间记忆评测](https://arxiv.org/html/2604.22409v1)包含程序生成房屋、25,000 余条交互序列与动态场景，但规模不是现实部署有效性的证明；当状态历史不可信或模态无法配平时，只能分别报告观察条件下的表现，不能把 L2→L3 差额全归为模型“没有记忆”。简单静态感知、已有状态一致性与闭环任务评测仍分别保留为旧分支。

在视觉问答内部，也须把“看到了对象/属性”与“正确推断对象之间的关系”分开。增强某些视觉 token 的权重可能改善前者，却让解码时的关注长期固定在同一区域，忽略回答关系问题所需的新区域；只用对象检测或单一幻觉率验收，会掩盖这个相反方向的变化。EvalSpec 应对相同图像分别设置对象/属性和关系推断任务，保留逐步关注变化、答案正确性与干预前后的成对结果。注意力轨迹是诊断传感器而非忠实因果解释；直接修改权重也可能同时改变别的计算。[Visual Inertia 的受限干预实验](https://arxiv.org/html/2604.01989v1)支持分账验证，不证明其特定惩罚算法适用于所有视觉模型。

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

共享 GPU 上还要隔离**真正计时的区间**。整条候选命令独占设备最稳妥，却浪费编译、准备和结果处理期间的容量；只在 kernel timing-critical region 阻止其他候选提交、等待已在运行的工作排空，再测稳定区间，可以提高评测吞吐而不直接共享时钟。代价是 region 边界和异步队列排空必须可信，host 侧干扰、设备时钟变化及未合作进程仍能污染数据；无法证明隔离时回退整设备独占。[NVIDIA/AMD 受限实现](https://arxiv.org/html/2609.30057v1)证明其披露配置的吞吐—测量折中，不构成所有 benchmark 的无偏计时保证。
<!-- source-family:SF-2026-ARXIV-2609-30057 -->

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

`stop / continue` 的二元状态仍会漏掉人类常用的第三种行为：保持话轮但吸收对方补充后修正内容。全双工轨迹因此应把 listener intent 与 speaker response 分开，至少记录 `backchannel / collaboration / interruption` 以及 `continue / adapt / yield`，并为 adapt 保存可定位的 uptake evidence。交出话轮、接纳内容和按时响应是三个不同 outcome，任何一个都不能替代另外两个。

三态合同改善错误归因，却增加 cue 标注、重叠区间、时钟同步和 scorer calibration 成本；把无关继续误判为 adapt，或把所有插话都当作 interruption，都会制造虚假成功。公开证据仅来自单一语音模型、英语录音与有限成对样本；单向、半双工或禁止重叠的产品仍可采用更简单的 turn-taking gate。

<!-- source-family:SF-2026-ARXIV-2609-13117 -->

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

Benchmark 的 surface shortcut 也必须在发布前主动探测。Question-blind 或 partial-input classifier、label-inversion counterfactual 和 clean twin 可以发现模型仅凭格式、否定词或长度猜标签；prune/add-back 必须保存 lineage，并重新测 semantic coverage 与 held-out ranking。清洗通过只关闭已测 shortcut，不能证明剩余 subset 无泄漏，也不能让排名保持替代 construct validity。

<!-- source-family:SF-2026-ARXIV-2609-13003 -->

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

### Harness 配置需要 Item-level Fragility Gate

冻结 prompt、option order 与 scoring rule 能让一次评测可复现，却不能说明模型排序对其他同样合理的 harness 配置稳定。发布 ranking 前应在预先声明的配置族中定位哪些 items 承载排序差异，分别报告 stable-item ranking 与 config-fragile contribution；否则少数脆弱题可能主导总体结论。该 gate 增加组合运行和多重比较成本，也不意味着脆弱 item 没有测量价值；单一生产协议仍应保留其固定结果。`arXiv:2608.21382v1` 固定题目、权重与 greedy decoding，在 12 个模型、3,679 个 items 和 26 种配置上支持这条边界，不证明所有 benchmarks 都失效。

<!-- source-family:SF-2026-ARXIV-2608-21382 -->

### Evaluation-awareness 必须分开 Representation、Verbalization 与 Control

模型内部可区分 evaluation/deployment prompt，不等于它会说出这种判断，也不等于该表示因果控制输出。evaluation-validity audit 应把可解码表示、显式 verbalization、受控 steering effect 与真实 deployment slice 分开，只有因果干预和外部分布都支持时，才可声称 benchmark behavior 会迁移。Probe 增加诊断力，却可能读取模板、数据集或后训练痕迹；无法排除混杂时只能作为 sensor。`arXiv:2608.21766v1` 在六个开源模型与 OLMo checkpoints 上支持三类信号不一致，不证明模型完整“知道自己在被测”或可稳定操纵评测。

<!-- source-family:SF-2026-ARXIV-2608-21766 -->

## Evaluation Contract 还必须管理配置、样本身份与工作负载状态

重复运行的可靠性不能只保存均值。每个 case 要绑定 attempt、seed、terminal backend state、tool side effects 与异常结束原因，分别统计成功率、方差、删失和不可逆副作用；否则一次重试成功会掩盖前次已改变环境。无副作用的确定性任务可以少量重复，高风险或状态化任务则需要 reset/compensation evidence 后才允许下一 attempt。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19741 -->

### Pairwise Verdict 需要 Configuration Envelope

“A 比 B 安全”只有在 harness configuration 被固定时才是可复算声明。Evaluation owner 应保存模型端点、prompt/template、sampling、package、judge 与 metric 配置，并报告配置网格内的排序一致性和方差，而不是只给一个 pairwise number。收益是区分模型差异与 harness-induced reversal，代价是组合爆炸；覆盖不足时应把结论降为 configuration-conditional，而不是平均掩盖反转。exact-v1 只在论文的模型、benchmark、package envelope 与 SDI/CFR 等指标中观察到该现象，不能估计所有评测配置。<!-- source-family:SF-2026-ARXIV-2605-25492 -->

### Membership Audit 要绑定 Sample Identity 与低 FPR 决策

把单样本攻击分数直接平均，在总体巨大、目标 FPR 很低时会被有限 shadow model 与抽样偏差支配。Measurement owner 应保存 sample identity、per-sample vulnerability、aggregation threshold 与 finite-population correction，并在同一 false-positive contract 下报告不确定性。收益是使 membership 声明可解释，代价是更多 shadow computation 和更宽置信区间；Gaussian post-processing 或总体假设失效时应退回 per-sample 结果或标记不可判定。exact-v1 只支持论文的数据、攻击与 analytical simulation，不证明生产模型隐私状态。<!-- source-family:SF-2026-ARXIV-2605-25819 -->

### Benchmark Completion 必须覆盖证据与 Action Space

只测静态输入输出，在 response space 小且动作固定时合理；部署 benchmark 若未覆盖可取得证据和允许 action，就可能把“未搜索到”误判为能力不足。Eval owner 应版本化 evidence fibers、action completeness 与 acquisition curve，先证明可完成性，再比较 agent。收益是区分 benchmark 缺口与系统缺口，代价是维护 action model 和数据覆盖；空间开放或 completeness 无法证明时，应明确只报告 sampled coverage。exact-v1 仅支持论文的 controlled channels 与 Tox21/Matbench/JARVIS audits，不证明开放世界完备性。<!-- source-family:SF-2026-ARXIV-2605-25997 -->

### Activation Oracle 的 Confidence 也要校准

内部 activation score 适合排序，却不能直接当 correctness probability。Evaluation owner 应为具体 operator、layer、label availability 与 calibration split 建立 confidence contract，并比较多种 operator 的 reliability，而非只看平均分。收益是让 interpretability probe 可进入 selective decision，代价是样本与重新校准成本；secret-word 可枚举性、层漂移或 label shift 会使置信度失真，应退回无置信度的诊断用途。exact-v1 只支持四个 Qwen/Gemma oracle、每 operator 约六千样本及所测任务，不提供通用内部真值保证。<!-- source-family:SF-2026-ARXIV-2605-26045 -->

### 错误的局部可修正性是诊断信号，不是真值概率

同样高置信的错误可能处在不同局部几何中：有些只需很小的输入表示扰动就改变输出，有些对扰动仍稳定。可在冻结模型与目标答案后，对 embedding 做受控扰动并测量目标相关参数梯度的敏感度，把它作为区分普通错误与 stubborn hallucination 的白盒 sensor。Measurement owner 必须保存模型、层、扰动分布、目标构造和阈值；sensor 只提出复核优先级，不能把局部曲率直接解释成“模型知道自己不知道”。

动态 probing 比静态 hidden-state 排名更有诊断性，但需要反向计算、依赖可访问权重，也会受目标答案、尺度和模型架构影响。黑盒服务、实时路径或分布漂移时应回退外部 evidence、claim verification 与 abstention。现有 exact-v1 结果仅覆盖作者的模型与数据集，不提供生产正确率保证。<!-- semantic-body-binding:SF-2026-ARXIV-2605-00939 -->

### Compliance Scaffold 本身也是评测干预变量

固定格式和“请严格遵守”的提示便于自动评分，却可能在压力条件下压低模型表达不确定性或自我纠错的能力。因而 evaluation configuration 不仅要冻结 task prompt，还要把格式约束、合规措辞和拒答模板作为独立 intervention：比较无 scaffold、弱 scaffold 与生产 scaffold 下的 calibration、abstention 和 task quality，避免把接口诱发的退化归因于模型能力。

这种消融增加运行成本，也不能证明模型具备可靠元认知；开放式输出难以评分时，严格 scaffold 仍是有效基线。当前证据只支持论文披露的模型、压力条件和自评任务，不能给出通用模板优劣。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02398 -->

### 推理早停要区分可恢复性与强制读出

沿着同一条未完成的推理前缀继续生成，与追加“现在给出答案”的提示，是两种不同的读出协议。前者测量自由延续能否恢复正确结果，后者同时改变后续输出分布；强制读出失败不能直接证明前缀没有有用信息，自由延续成功也不能证明模型内部已经形成确定答案。评价早停时，应固定同一 prefix，分别比较两种协议，并用无 prefix 基线、共同解出样本与持出集阈值校准，避免把模型原有解题能力或样本选择误当作提前完成推理。

这种区分使早停收益可解释，却增加探针采样与校准成本。协议必须单独记录主轨迹的串行长度、所有 continuation 的总 token、API 调用及并发预算；串行生成变短不等于总成本更低。按完整轨迹长度定义的 prefix 比例还依赖离线长度信息，不能直接作为在线停止控制器。开放任务上没有正确答案标签时，一致性只是代理信号，仍需外部验证或保留继续推理路径。当前[精确版本 PDF](https://arxiv.org/pdf/2604.06613v1)只支持所测模型与数学、问答、代码协议下的行为差异，不提供内部知识、普遍早停或生产延迟保证。

<!-- source-family:SF-2026-ARXIV-2604-06613 -->

### Agent Workload 不是普通 Long-prompt Workload

把输入 token 总量当作主要成本，在 cache 不可复用时成立；多轮 Agent 大量复用 prefix 后，execution 会转为 decode-dominated，并依赖长生命周期 KV state。Workload contract 应记录 turn graph、cache-hit identity、KV lifetime、tool pauses 和 decode distribution，capacity owner 才能重放。收益是避免用静态长提示压测误配硬件，代价是 trace 基础设施与隐私处理；prefix identity 失效或 cache eviction 改变时必须重新测量。exact-v1 只支持五个 agent benchmark、披露的 Gemma/Qwen 配置和 serving stack，不证明所有生产 agent 都呈同一比例。<!-- source-family:SF-2026-ARXIV-2605-26297 -->

### Native-runtime Agent Workload 必须绑定容器状态与长时 Trace

短沙箱加 final-answer check 便于批量评测，却不能代表真实 CLI、工具暂停与长期副作用。更接近部署的 evaluation identity 应把 native CLI harness、container state、wall-clock/tool trace 与 graded outcome 绑定在一起，使得“做了什么、环境怎样变化、最终达到什么程度”可以联合重放。

这会显著增加环境维护、运行时长、隐私处理和 flaky-state 风险；简单、无副作用任务仍可使用轻量沙箱。容器镜像、工具版本或外部依赖无法冻结时，应缩小可比较声明并报告环境漂移，而不是把分数当作稳定模型属性。exact-v1 只支持其 60 项双语多模态任务与披露 runtime，不证明所有生产 Agent 都具有同一失败分布。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10912 -->

### Domain Workflow 可以编译为 Deterministic Verifier

人工编写少量 ERP 题目容易审计，却难覆盖约束组合；纯自然语言生成又会引入不可判定答案。Benchmark owner 可以把领域专家 specification 编译为 constraint optimization program，由同一版本的 generator 与 executable verifier 产生任务和判定。收益是扩大覆盖并保留可复算性，代价是 specification bug 会系统性污染数据；必须以人工 anchor、独立 solver 和版本化约束做交叉检查。exact-v1 只支持单一 ERP domain 与生成任务，不证明真实业务流程或跨域泛化。<!-- source-family:SF-2026-ARXIV-2605-26321 -->

### Miscoverage 要拆成 Sampling Failure 与 Selection Failure

只给最终 coverage 数字，会把候选集中没有正确项和 selector 选错混成同一故障。Evaluation owner 应分别估计有限采样失败，并在 calibration/exchangeability 条件下对 conditional selection 使用 conformal gate，再组合总体 bound。收益是为增加采样或改进 selector 指明责任，代价是校准集、额外样本与假设检查；分布漂移或相关自适应采样会破坏保证，应退回经验 risk-coverage 曲线或 abstain。exact-v1 仅支持论文的有限采样实验、conditional exchangeability 与 population-bound 假设，不是开放世界 truth guarantee。<!-- source-family:SF-2026-ARXIV-2605-27091 -->

### 相关采样会抬高 Coverage，却压低 Selection 上限

<!-- semantic-body-binding:SF-2026-ARXIV-2606-28661:start -->
把每次采样视为独立，并假定“只要正确答案出现过，系统就会选中”，在错误模式分散且 selector 近似 oracle 时是合理近似；同一模型反复生成的错误往往相关，modal mass 还会让投票或排序器更确信地选择同一种错误。评估因此要把 candidate coverage、selection accuracy、样本相关性与 effective decision information 分开，只有边际 selection gain 仍为正时才继续扩大采样预算。

相关性分析能解释为什么更多样本不再带来可用信息，却不能给出跨模型、任务、sampler 与 selector 固定不变的 ceiling。估计漂移、样本不足或 selector 失配时，应停止用增加 `k` 掩盖识别器缺陷，转而校准 verifier、增加真正多样的 proposal source，或在高风险结论上 abstain；少量独立采样仍适合探索候选，但不自动构成发布证据。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-28661:end -->

## Adaptive Evaluation 也必须被当作实验过程

静态题库适合复现同一测量，但模型能力与失败面接近后，固定问题会降低区分度。自适应 peer-probing 可以让模型
依据交互历史提出针对性问题，再由独立 verifier 检查问题与答案；这里 answerer、questioner 和 verifier 必须是
三个可分别失效的 owner。强 answerer 未必会提出有效难题，模型生成的 reference 也不自动成为真值，因此该分支
只能补充冻结 benchmark，并要保留题目有效率、独立复现和人工 anchor。

<!-- source-family:SF-2026-ARXIV-2607-24780; daily-trace:papers/2026/07/29/README.md -->

Aggregate score 还可能把不同内部能力混平。原子视觉 perception 应与端到端 reasoning 分开验收；相近总分不代表
相同 failure profile，切片标签也不证明组件完全独立。增加这类标注会提高评测成本，却能防止 reasoning 分数掩盖
上游感知失败；真实部署仍需按自身 modality 和错误代价重加权。
<!-- source-family:SF-2026-ARXIV-2607-24957; daily-trace:papers/2026/07/29/README.md -->

多模态 context learning 还需要把 grounding、规则归纳与新知识 acquisition 分阶段验收，再与端到端结果并列。
阶段之间有关联，不能把分片分数解释为完全因果独立，但它们可以定位信息究竟在表示、规则应用还是上下文吸收阶段
丢失。
<!-- source-family:SF-2026-ARXIV-2607-25294; daily-trace:papers/2026/07/29/README.md -->

排行榜的不确定性也不能只用重复采样的标准误表达。Item difficulty、discrimination 与 model ability 可以进入
显式测量模型，再用 posterior interval 表达排序是否可区分；但 posterior 依赖 IRT 结构和局部近似，不是部署失败
概率。区间重叠时应发布 unknown/tie 或增加有区分度的 items，而不是用点估计制造名次。

<!-- source-family:SF-2026-ARXIV-2607-25257; daily-trace:papers/2026/07/29/README.md -->

增加有区分度的题目还需要回答“对哪个测量目标有信息”。单维 IRT 中最大化 Fisher information 可近似减少能力参数方差；能力变成多维后，信息矩阵的迹较大不保证目标 benchmark 的预测方差更小。一个条件分支先固定已知题目参数和目标任务集合，再选择最能降低这些目标预测方差的题目，每观察一次答案就更新能力后验；若题目成本相差很大，可再按历史输入输出 token 成本折扣信息收益，而不是只压低题目数量。测量目标、选题规则、历史成本和已观察响应需要随同保存。[受限证据：WILD §3、§5–7](https://arxiv.org/html/2604.01418v1#S3)

这用跨任务相关性换取少量观察，但估计的是已建模题目的表现，不是新能力、真实部署可靠性或事实置信度。作者的二元正确性、短程任务和有限模型实验不能保证任意 reasoning budget、长轨迹或分布漂移下同样有效；高观察预算下简单回归也可能更合适。Token 折扣还会偏向便宜且相关的题目，遗漏昂贵任务的独立失败面，历史 token 数也不等于当前时延或价格。因此压缩评测应保留目标任务覆盖和独立 anchor，漂移或预测失准时回退分层随机、冻结题库或完整任务测量，不让选题代理取代 release gate。
<!-- source-family:SF-2026-ARXIV-2604-01418; daily-trace:papers/2026/04/03/README.md -->

当自然语言任务可编译为形式化 specification 时，LLM 可以提出规格，真实 model checker 提供 counterexample，再
迭代修订；最终接受权属于 checker。但 checker 只证明“实现满足给定规格”，错误或不完备的 specification 仍会
正确地证明错误目标。因此发布 Gate 必须先验收 specification validity，再验收 proof/checker result；开放语义或
无法忠实编译时，回退 executable tests、人工审阅和运行时监控。

<!-- source-family:SF-2026-ARXIV-2607-25333; daily-trace:papers/2026/07/29/README.md -->

<!-- semantic-body-binding:SF-TOWARDS-RELIABLE-LLM-EVALUATION-CORRECTING-THE-WINNER-S-CURSE-IN-ADAPTIV:start -->
在同一 benchmark 上反复调 prompt、policy 或超参数并只报告最佳配置，会产生 procedure-level winner's curse：即使每次单独评测都正确，选择过程也会系统性高估最终 winner。EvalRun 因而要保存尝试序列、selection rule、holdout reuse 与 stopping condition，并用独立 holdout、sequential correction 或重新运行校正选择偏差。它降低虚假改进，却需要更多样本和计算；一次性、预注册比较仍可沿用普通置信区间。[受限证据：arXiv:2605.05973v1]
<!-- semantic-body-binding:SF-TOWARDS-RELIABLE-LLM-EVALUATION-CORRECTING-THE-WINNER-S-CURSE-IN-ADAPTIV:end -->

<!-- semantic-body-binding:SF-BEYOND-ACCURACY-POLICY-INVARIANCE-AS-A-RELIABILITY-TEST-FOR-LLM-SAFETY-J:start -->
Judge 可靠性还应接受 policy-preserving rewrite test：若语义与安全政策保持不变，只改变表述、顺序或无关上下文，verdict 应在声明容差内保持不变。该 invariance 是 evaluator release evidence，而不是另一个总分；失败时应回退冻结人工 anchor、确定性 outcome 或更窄适用域。稳定性通过也不证明 judge 正确，只说明它没有被这类等价变换轻易翻转。[受限证据：arXiv:2605.06161v1]
<!-- semantic-body-binding:SF-BEYOND-ACCURACY-POLICY-INVARIANCE-AS-A-RELIABILITY-TEST-FOR-LLM-SAFETY-J:end -->

逐 token correction 会破坏原本正确的生成；更细的分工是让可校准的 hidden-state density estimator 只产生 anomaly sensor，由独立 decoding controller 决定是否触发 contrastive correction。Sensor、intervention 与最终 correctness authority 必须分离，且在 residual distribution 漂移、无法访问内部状态或 calibration 失效时回退外部证据核验、普通 decoding 或 abstention。

作者在 1B–8B 四个模型和四个 benchmark 上报告检测/TruthfulQA 结果；所谓 factual manifold、最高 99% AUROC 与 preservation/corruption rate 只属于其标注、层与 intervention 设置，不是普遍事实概率。 Inference 章节可实现 correction path；Evaluation 章节拥有 sensor calibration 与风险决策。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05953 -->

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

### Guardrail 的 Review Unit 必须与 Clean Twin 一起验收

只报告 caught attacks 会奖励更长、更拒绝式的 review，而无法区分真正 discrimination 与统一提高拒绝率。pre-execution monitor 的 evaluation unit 应冻结可见步骤，并为每个错误轨迹构造只差一个 environment-accepted write 的 clean twin；同时报告 catch、false rejection 与 informedness。更长窗口可增加证据，也可能引入无关噪声和过度拒绝，最佳长度依赖任务而不是固定常数。`arXiv:2608.23941v1` 在六个 judges、两个 domains 和五种 nested review length 上支持这一测量缺口，不证明一至两步普遍最优。

<!-- source-family:SF-2026-ARXIV-2608-23941 -->

## Action Control 需要 Sensitivity 与 Invariance 双臂证据

只看 action accuracy，无法区分 Agent 是否真正消费了当前状态，还是依赖与训练集相关的表面 cue。因果评估应构造两个相互约束的干预臂：改变决定正确 action 的 decisive state 时，行为必须相应改变；保持 decisive state 不变、只替换无关 cue 时，行为应保持在声明容差内。前者测 target-changing sensitivity，后者测 target-preserving invariance；任一单臂通过都不足以证明 action control。

<!-- source-family:SF-CAUSAL-STATE-BINDING-PREDICTS-ACTION-CONTROL-IN-LANGUAGE-AGENTS -->
EvalSpec 需要冻结 event/state schema、可控干预、matched interface、action scorer 与 tolerance，并保存每对干预样本的 trajectory。它能把相关性成功分解为更强的 behavioral evidence，却增加构造 matched interventions 的成本，也可能因遗漏真正 mediator 而误判。无法构造可信干预时，应把结论降级为 observational association，继续使用真实 outcome、人工 adjudication 与 production incident evidence。即使双臂通过，也只证明披露任务上的结构耦合，不证明模型具有内在 agency 或能迁移到开放环境。[受限证据：arXiv:2605.09692v1]

### Matched Counterfactual 必须保持任务界面，Detector 零命中只能形成下界

改变 prompt wording 来测 framing effect 时，如果同时改变函数签名、示例、参数个数或目标操作，结果已经混入 task/interface drift。旧的自然语言改写在探索阶段便宜，但只有保持输入输出契约和任务语义不变的 matched twin 才能承担因果比较；无法构造等价 twin 时，结果必须降级为描述性关联。SecDrift exact-v1 的术语替换 matched baseline 保留 signature 与 example，而完整行业提示在九个任务中全部移除了这两项并改变了多项 interface，因此只有前者能够支持较干净的 framing 对照；论文在其七个模型、九类 CWE 和给定采样设置中未发现可区分的行业 framing effect，不证明其他 prompt、语言或攻击条件也无效。

同样，`detector = 0` 只表示当前检测器没有命中，不表示风险不存在。应从零命中或高风险 strata 抽样进行独立 adjudication，估计 detector false-negative boundary，并把自动 flag rate 写成检测能力下的下界。该 exact-v1 对六个零检测类别抽查 90 个程序，其中 24 个被两套静态分析器漏掉，且遗漏集中在 XSS 与弱密码学；这个样本只校准被审切片，不能推出全语料漏检率。matched twin 和人工 adjudication 都提高成本；无法承担时应保留多检测器、可执行测试与人工 review 的旧路径，并禁止把“无告警”升级为“安全”。

<!-- source-family:SF-2026-ARXIV-2607-25225 -->

### Safety Evaluation 还需要 Depth-oriented Repeated Inference

横向扩大 prompt/category 覆盖不能替代对同一运行条件的纵向压测。生产中同类请求会被反复采样，单次“安全”只是 Bernoulli outcome；EvalSpec 应冻结 prompt family、model/runtime、temperature、seed policy、judge/scorer 和采样次数，分别报告每次失败概率、置信区间、首次失败深度与相关性。这使“广度覆盖多少风险类别”和“持续使用时某一风险多久出现一次”成为两份独立证据。

加速重复采样会增加调用成本，还可能因共享 cache、provider drift、judge 误差或近重复 prompt 而破坏独立假设。因此它是对 breadth benchmark 的补充，不是取代；预算不足时应保留高风险 slice 的最低采样深度并将未见失败标为上界未决。公开实验只支持披露模型、AIR-BENCH 派生 prompts 与 decoding 配置，不给出生产故障频率。<!-- source-family:SF-2026-ARXIV-2602-11786 -->

## 部分评测必须预先声明停止与淘汰状态

逐层或分批拿到评测结果后再临时决定“是否继续”，会把观察后的选择偏差写进结论。更可审计的过程是在运行前定义继续、提前停止、淘汰与保留四类状态，冻结最小样本量、误差预算与失败成本，再让执行器按规则推进。它用可能的保守计算换取结论可复算；任务不可分层、早期样本不具代表性或错误代价高时，应回退完整评测。`arXiv:2608.02444v1` 只证明作者设定中的 partial-evaluation 决策规则，不保证所有 benchmark 都能安全早停。<!-- source-family:SF-2026-ARXIV-2608-02444 -->

如果评测对象是同一模型的多次回答，运行到“多数看起来稳定”再停止同样会产生 stopping bias。anytime-valid e-process 可以在未知回答类别、任意合法停止时刻下，为“某个 response mode 唯一占优”提供统计 certificate；它证明的是采样分布中的 mode，不是该答案事实正确、校准或安全。Evaluation owner 必须冻结 model/sampler、目标 mode、独立性假设和停止规则，并把 certificate 与 external correctness evidence 分栏。收益是允许预算自适应而不丢失声明的错误控制，代价是 i.i.d. 假设、响应归类误差和可能较长的停止时间；出现 provider drift、相关采样或高风险事实判断时，回退固定样本、独立证据与人工/确定性 verifier。exact-v1 只支持作者的 anytime-valid modal inference 证明与披露实验。

<!-- source-family:SF-2026-ARXIV-2605-05873 -->

World model 评测也必须把“看起来真实”拆回系统职责。外观质量只检查 observation surface；可控性检查 action 是否改变正确状态；空间一致性检查场景约束；反应性检查环境是否按新 observation 及时更新。只有四者联合，才接近 planning 所需的 transition contract。收益是避免视频质量掩盖不可控制或不响应的环境，代价是需要 action schema、可达状态与闭环 harness；没有交互真值时，自由生成指标仍只能作受限代理。`arXiv:2608.02603v1` 的 1,474 个案例与 20 个模型只支持该 suite 的区分能力，不证明被测 world model 具有因果正确性。<!-- source-family:SF-2026-ARXIV-2608-02603 -->

## 模型编辑必须同时测 Target Effect 与 Control Survival

让目标 skill 的成功率下降只证明行为被压制，不证明该能力被局部、稳定地移除。完整编辑评测应同时冻结目标任务、未目标 control matrix、编辑强度、架构与闭环环境，报告 target suppression、collateral damage、组合编辑和 relearning；几何相似或单层定位只能作诊断，不能代替行为证据。它用更大的闭环矩阵换取不把广泛能力破坏冒充精准删除；只需临时禁用且可由 policy gate 完成时，运行时授权仍比改权重更可逆。`arXiv:2608.04692v1` 的结果只覆盖作者 VLA、suite 和系数，不证明 task-vector negation 等同知识删除。<!-- source-family:SF-2026-ARXIV-2608-04692 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20262:start -->
Selective refusal editing 的失败还可能来自 routing，而不是知识已被删除或保留。把中间表示送入 oracle route 能
诊断“正确安全分支其实存在但没有被选中”，却不能证明危险知识已移除，也不能作为生产控制器。评测要把 target
effect、route choice 与 control survival 分开；作者设置之外，oracle 不可得或 route 干预改变分布时，应回退端到端
行为测试、relearning 与未目标 control matrix。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20262:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20270:start -->
持续部署的 selective prediction 还需把 test statistic、validity guarantee 与 deployment rule 作为一个合同。
对每个 threshold 维护 e-process，可以在任意观察时点给出 pathwise-valid 的 selective-risk 证据，再选择当前最大
可认证阈值；这比固定样本一次校准更适合持续流，但依赖其统计假设、阈值族和反馈可观测性。任何假设、延迟标签
或分布稳定性不成立时，应停止自动放宽阈值并回退固定保守门、重新校准或人工审批。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20270:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20745:start -->
Verifier strictness 也可能在 hidden state 中形成可控方向，用于诊断或 steering 审查强度；但方向可解码只证明
模型内部存在相关信号，不证明每个步骤正确，更不授予最终真值权。跨模型、任务或 prompt 后该方向可能漂移，
steering 也会产生 collateral behavior。校准或外部 outcome 不支持时，应回退显式 verifier、原始未编辑模型与
人工复核。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20745:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20774:start -->
VLA evaluation 若只依赖昂贵实验室设施，很难复算版本变化；低成本 replica benchmark 可以冻结任务、硬件、
控制频率和 success protocol，让更多系统执行同一真实世界 contract。可复现性收益以环境覆盖、装置精度和任务
多样性为代价，低成本并不等于物理风险被完整覆盖。作者 task suite 之外，安全、长尾接触和新 embodiment 仍需
独立真实测试，replica 结果不能升级为通用部署许可。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20774:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20833:start -->
Agent memory benchmark 应把不同 memory system 接到统一 memory-reasoning interface，并分别记录写入、检索、
推理与 task outcome；否则一个 end-to-end 分数无法定位失败。MemRM 一类轻量信号可降低大规模评测成本，却仍是
特定构造 pipeline 和 judge 下的 proxy，不拥有长期事实真值。interface coverage、动态环境或独立 outcome 未验证
时，应回退原始 trajectory、人工审计与系统级复现。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20833:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21482:start -->
Deep-research benchmark 还要冻结搜索入口、网页时间、工具权限、引用规则和 evaluator，才能区分 retrieval coverage、
evidence synthesis 与 answer quality。更难的题集扩大区分度，却不证明高分系统在开放网络中事实完备；网页漂移、
judge 共偏与工具差异都会改变结果。DeepWeb-Bench 的作者实验只支持其 protocol；部署判断仍需重放 source span、
独立事实核验和当前环境下的 effect evidence。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21482:end -->

## Tool 与 Skill 评测要把失败阶段拆开

Agent 选错工具可能来自语义诱饵、参数陷阱、虚假能力、缺失前置条件、时间状态或粒度选择；单一 task success 无法定位原因。受控 canary 可以每次只改变一个弱点，并由 provider-independent judge 与第二判断者复核 outcome，但 canary 只拥有诊断权，不能进入生产工具列表。该方法用额外 probe 运行换取 failure profile；真实环境与安全结论仍需独立验证。`arXiv:2608.04719v1` 的八模型实验只支持披露 taxonomy 与 harness。<!-- source-family:SF-2026-ARXIV-2608-04719 -->

Skill 被安装也不等于被正确使用。Evaluation 应分别测 agent 是否在需要时主动 Trigger、读取完整 procedure 后是否 Compliance，以及是否守住禁止操作 Boundary；只有三者都成立，execution outcome 才能归因于 skill。progressive disclosure、真实文件和隔离 sandbox 提高外部真实性，却增加 harness/version 依赖，79 个 skills 与 177 个任务不能覆盖整个生态。未触发和触发后违规必须分开报告。<!-- source-family:SF-2026-ARXIV-2608-04828 -->

## 审计记录不能替代最终判断所需的原始证据

把 judge 的“提取 evidence”和“作出 verdict”拆成两次调用，可以留下可读审计记录，却也可能在第一步压缩掉第二步需要的信息。持久 evidence record 应与 source answer 并列：record 负责解释与复核，最终 judge 仍可读取原始候选；只给压缩记录的 locked protocol 是另一种 evaluator，必须单独校准。这样用更大的 context 与隐私面换取较少的信息丢失；原始材料不可再次访问时，系统应降低证据等级而非假装等价。`arXiv:2608.05353v1` 的 24,000 次实验只覆盖两种 judge、三个数据集与披露 protocol。<!-- source-family:SF-2026-ARXIV-2608-05353 -->

## World Model 的物理评测要落到定律与参数

感知相似或人工观感无法说明生成环境是否遵守碰撞、摩擦、动量、振荡和变形规律。更强的合同把现实轨迹、校准参数、坐标/时间处理和测量不确定度共同冻结，分别报告定律形式与参数误差；这样用昂贵的传感、标定和 task-specific observable 换取可诊断物理偏差。没有现实 reference 或任务超出受控场景时，这些分数只能作局部证据。`arXiv:2608.05948v1` 的 22 个 task family 支持该评测分解，不证明任何 simulator 或 video world model 在开放世界物理正确。<!-- source-family:SF-2026-ARXIV-2608-05948 -->

## Harness Optimization 的 Test Boundary 必须对优化器不可见

当模型可以修改 prompt、tool、memory 和 control flow 时，被评对象不再只是权重，而是完整 harness artifact。可复算评测需要冻结 seed、搜索预算、可见 feedback、候选版本和资源计量，并由受信执行环境隔离 held-out test partition；优化器只在预算内提名最终候选，不能读取 test 或选择性重跑。它用较低搜索效率换取对 validation overfitting 和 harness 越权的控制。`arXiv:2608.06301v1` 的五个模型、四个任务与 111 次运行只证明该协议具区分力，不支持通用模型排名。<!-- source-family:SF-2026-ARXIV-2608-06301 -->

### 可组合压缩必须按组合后的 Artifact 验收

专家裁剪、权重量化和 KV 压缩各自通过，并不能推出组合后仍满足质量、内存和延迟目标；它们会共享误差预算，并随 MoE 架构与 workload 发生非线性交互。评测应把压缩顺序、精度、裁剪比例、attention 类型、生成长度、硬件和端到端 runtime 绑定到同一个 artifact identity，分别报告平均结果与最坏子集。单项 benchmark 只能证明局部可行性，不能作为组合部署的替代证据。
<!-- source-family: arxiv:2608.21693v1; semantic-body-binding: composable-compression-joint-evaluation -->

### Confidence 要在 Belief、Action 与 Outcome 三层校准

模型在采取动作时表达的信心，可能同时偏离内部 belief quality 和最终结果。一个统一的“置信度”因此无法承担发布或授权决策：评测要分别检查模型相信什么、基于它选择了什么动作，以及环境反馈是否支持该动作。开放世界中的真实分布仍需另行验证，但这三层分离能避免把语言上的笃定当作可执行保证。
<!-- source-family: arxiv:2608.24691v1; semantic-body-binding: belief-action-outcome-calibration -->


#### Single-call Judge Confidence 是传感器，不是 Verdict

重复调用或多 judge 集成可以估计判决稳定性，但成本高；从一次结构化 reasoning 中分解 claim、evidence 与局部 verification 信号，可以形成更便宜的 confidence sensor。这个分解器只拥有不确定性观测权，最终 verdict 仍应由校准规则、独立证据和发布策略决定，并把 judge、prompt、reasoning schema 与 calibration set 绑定为版本身份。

单调用估计降低成本，却共享 judge 本身的盲区：流畅但错误的 reasoning 可能产生高置信，schema 漂移也会破坏校准。高风险或域外样本应回退独立 verifier、多次采样或人工复核。`arXiv:2605.11334v1` 的 §3–§7 只支持作者 judge、任务和校准结果；没有独立 limitations，也不能把输出直接解释为事实正确概率。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11334 -->

### 聚合指标必须能暴露不同 Failure Type

两个生成系统取得相近的 FID 或总分，仍可能在遗漏、模式坍缩、语义偏移和局部伪影上完全不同。评价合同应把 detection、ranking 与 diagnosis 分开，并提供能够推翻总分排序的 counterexample slice。新增指标也不是天然更好；只有在多模型、多数据和清晰失效分类上稳定，才可以进入 release gate。
<!-- source-family: arxiv:2608.24881v1; semantic-body-binding: aggregate-metric-failure-decomposition -->

### Reasoning Trace 是独立的安全评测对象

只检查 prompt 和 final answer 会漏掉中间推理中的不安全内容，而简单二元标签又无法说明 guardrail 应阻断哪一段。推理模型的安全 contract 应覆盖输入、trace 与输出，并要求 evidence localization；这并不意味着公开完整思维链，而是要求部署侧对其实际可观察或可审计的中间状态定义保护边界。
<!-- source-family: arxiv:2608.24232v1; semantic-body-binding: reasoning-trace-safety-evaluation-unit -->

### Reference Coverage 决定“未匹配”能否被判错

有限或不完整的 reference set 会把真实但未收录的答案标成 false，进而反转不同模型的 calibration 排名。评价系统必须分别记录 reference coverage、matcher 的等价判定能力和人工复核范围；`unmatched` 只能表示没有被当前 oracle 识别。扩充 reference 与人工审计成本更高，但否则精确分数会掩盖标签生成过程的不确定性。
<!-- source-family: arxiv:2608.25654v1; semantic-body-binding: unmatched-is-not-false-reference-coverage -->

### Stored Label 要追溯到 Execution、Request 与 Stimulus

评测结果若只保存最终 label，后续可能把执行环境、请求选择或刺激材料的差异误当成模型效果。每个 observation 应能回溯 execution revision、request identity 和原始 stimulus，并记录处理链；否则 treatment leakage 会让训练或版本信息进入本应独立的评价。更完整的 provenance 增加存储成本，却是重放与因果解释的前提。
<!-- source-family: arxiv:2608.12880v1; semantic-body-binding: evaluation-treatment-provenance-chain -->

### 组件分数不能在相关错误下直接合成系统可靠性

多 Agent 或多阶段系统的组件失败通常共享输入、模型、工具和 judge，独立性假设很容易失效。组合评价应给出 dependence-aware 的可识别上界/下界，并用联合故障样本估计相关结构；没有这些证据时，只能报告观测到的系统级成功率，不能把单组件准确率相乘成保证。
<!-- source-family: arxiv:2608.12895v1; semantic-body-binding: dependent-component-reliability-bounds -->

### 相似度、分解与代理故障都必须经过反事实校验

Cosine 或 NLI 分数适合发现可能等价的回答，却不能拥有 semantic-equivalence 的发布权：否定反转、实体替换等 matched counterfactual 必须让分数显著变化，并且最终任务结论仍需单独核对。否则“措辞相近”会掩盖控制含义相反。
<!-- source-family: arxiv:2608.10216v1; semantic-body-binding: semantic-equivalence-needs-matched-reversal-counterfactuals -->

把复杂任务拆成中间 claim 也不是中立预处理。每个 claim 应保留 source entailment、provenance 和重组关系，并验证分解后结论与原任务是否一致；多次生成的一致性只能说明模型重复了同一路径，不能替代外部证据。
<!-- source-family: arxiv:2608.10627v1; semantic-body-binding: task-decomposition-as-evaluated-transformation -->

用小模型或合成 workload 复现故障时，proxy 必须保留触发问题的结构因素，例如依赖深度、状态寿命或通信形态。代理上的失败能证明诊断路径可触发，不能证明原模型会以相同频率、损失或质量结果失败；它是缩小搜索空间的工具，不是全系统收敛证明。
<!-- source-family: arxiv:2608.10823v1; semantic-body-binding: failure-proxy-must-preserve-trigger-structure -->

### Agent 与 World Model 的证据要分层闭合

Agent 安全评测应依次记录 exposure、实际执行、环境可见结果与独立 adjudication。提示或轨迹中出现攻击字符串只证明暴露，工具返回成功也未必证明最终世界状态改变；service receipt 和 final-state evidence 才能拥有效果裁决权。
<!-- source-family: arxiv:2608.10669v1; semantic-body-binding: agent-safety-exposure-execution-observation-adjudication -->

World Model 的复现实验要冻结 environment、数据、checkpoint、rollout protocol、seed 与 success criterion。缺少其中任一项时只能复现局部机制，不能把相似视频或单次成功声明为系统复现；更完整的合同提高复现实验成本，却让失败能回溯到状态、策略或环境差异。
<!-- source-family: arxiv:2608.10145v1; semantic-body-binding: world-model-reproduction-contract -->

### 在比较优化器前先证明 Reward 穿过信噪比下限

奖励看似有结构，可能只是尺度、方差或长度等低阶统计被模型利用。先构造保持相同矩统计量的 matched-noise placebo：只有真实 reward 相对 placebo 产生稳定增益，才说明信号越过可学习的 SNR floor。这个检查不能证明奖励与目标完全一致，但能避免在无信息信号上继续比较优化器或扩充训练规模。
<!-- source-family: arxiv:2608.10441v1; semantic-body-binding: matched-moment-placebo-for-reward-signal-floor -->

## Measurement Identity 必须允许别人重构同一个判断

### Judge Agreement 不是单一数字

同一批 verdict 可以因为 scale、排除样本、invalid/abstain 处理、item/rubric pooling 与 metric 的不同而得到相反结论。
因此 agreement run 至少绑定 `population + scale + missing/abstain policy + pooling + metric`，并报告 excluded fraction、
边际分布和关键 slice；judge 只提供 measurement signal，不能因为 kappa 或 accuracy 较高就取得 truth authority。

更完整的 identity 降低跨报告“同名不同义”，代价是结果不再容易压成一个排名；小样本、stochastic judge 与 human label
本身的误差仍需区间和复核。作者对有限已发表评测的重算只证明协议敏感性，不证明某个 metric 普遍最优。

<!-- source-family:SF-2026-ARXIV-2606-00093 -->

### Constraint Graph 可以连接任务生成与多解验收，但不能替代真实环境

单 reference answer 在存在多条合法工具路径时会误拒正确结果；让 versioned constraint graph 同时生成任务、物化合法
解集并驱动 state verifier，可以把跨实体依赖、distractor 与 disclosure schedule 保持在同一 EvalSpec。generator 拥有
case proposal，environment state 与 deterministic predicates 拥有可验证 outcome，user simulator 只拥有交互扰动。

这条路径支持多解和非理想用户，却新增 graph/schema 漂移、materializer bug 与 simulator common-mode error。旅行预订等
有限模拟域不能外推真实账户、支付或不可逆副作用；高风险结论仍需真人样本、真实环境 anchor 或 sandboxed effect receipt。

<!-- source-family:SF-2026-ARXIV-2606-01815 -->

## Release Gate 要覆盖“中心看不到”和“压缩后看起来仍正确”

### Federated Personalization 的盲区是可见性合同

集中式 aggregate accuracy 在服务行为可由中心直接观察时有效；client-local adaptation 受隐私限制后，中心可能看不到偏差、
miscalibration、alignment erosion 或 OOD collapse。EvalSpec 应先声明哪些 local behavior 可测、哪些统计可安全聚合、谁能审计，
再决定是否发布；不可见必须传播为 Unknown，而不是用全局平均推断所有 client 安全。

隐私保护减少原始证据，聚合又可能掩盖小群体 failure；扩大 telemetry 反过来会侵蚀隐私。本 exact-v1 只提供 taxonomy 与
research vision，没有实现完整 detector 或生产 threshold，因此这里沉淀的是观察权与 release authority 的边界，而不是
已经解决 federated silent failure 的结论。

<!-- source-family:SF-FED-PERSONALIZATION-SILENT-FAILURES -->

### Compression Release 必须同时验收 Accuracy 与 Calibrated Uncertainty

量化或稀疏化后平均准确率接近原模型，不代表 confidence、coverage 或 abstention risk 保持不变。压缩 artifact 的 release
identity 应绑定原/压缩模型、校准集、score function、coverage target、quantization/sparsity 配置与 evaluator，在相同样本上
联合比较 task quality、coverage、set size 与 calibration failure。压缩器只能产生候选 artifact，Evaluation gate 才能决定
是否替换 baseline。

双门禁扩大测试矩阵，也受 exchangeability、dataset shift 与 calibration sample size 限制；不能从有限模型和方法推导一个
统一 safe bit-width。校准失效或高风险 slice 退化时，应提高精度、关闭 sparsity、重新校准或保留原模型。

当部署端为节省模型内存而压缩**权重**，错误负担还可能在使用者群体间重新分配，即使总体 WER 变化不大。
因此应在原始与压缩后的同族模型上，用相同语音样本及解码设置配对测量各口音或人口组的 WER、
循环输出率和校正工作量，并区分量化、剪枝、蒸馏及模型尺寸；发布决策不能只凭全精度模型的一次公平性审计。
[Whisper 家族研究](https://arxiv.org/html/2609.28739v1)发现所测剪枝配置可能扩大群体校正负担，部分蒸馏配置却缩小差距；
差距缩小也须检查是否因为原本表现较好的群体退化。群体切片、语速与每错词校正时间的假设都属于评价合同，
不能把线性换算的校正时间当作实测人工劳动。当前证据限于一个 ASR 模型家族、特定英语朗读与口音数据和压缩配置，
既不证明所有压缩都会加剧不公平，也不否认资源受限设备部署压缩模型的合理性；缺少足够切片样本时保留原模型或延迟发布结论。
<!-- source-family:SF-2026-ARXIV-2609-28739 -->

音频、图像等有损压缩还需要把“平均任务分数”改写为与原始输入配对的 excess answer error。平台对同一 query 分别运行
raw 与 compressed artifact，按 semantic/query family 统计压缩新增错误，并对最坏 family 给出置信上界；family partition、
selector、backbone 与 codec revision 都属于 measurement identity。这样可以发现总体平均不变、少数问题族却系统退化的情况，
而不是让聚合值替压缩器签发 release verdict。

更细切片需要更多样本，family 定义也可能由关键词代理而失真；置信区间只量化所声明抽样过程，不证明 rate-theoretic frontier
或生产 workload 安全。样本不足、最坏 family 上界越界或切片定义不稳定时，应回退原始输入、更高 bitrate 或扩大校准集。
现有证据只覆盖两个 7B audio-language model、五个英文选择题数据集和特定压缩配置，支持 worst-family release contract，
不支持一个跨模型通用的安全码率。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06631 -->

<!-- source-family:SF-COMPRESSION-UNCERTAINTY -->

## Failure Evaluation 要从最终错误追到首次有害承诺

### Trajectory Error 需要 Span、Commitment 与 Claim Propagation 三层坐标

只给失败 run 一个总标签，无法区分最早原因和后续复述。长轨迹评估应保存 outcome、step/span、first harmful commitment、
claim lineage 与 downstream propagation；annotator/judge 提供定位 proposal，tool/environment receipt 和可执行 predicate 负责
确认可观察 effect。这样可以把修复指向真正的控制点，而不是惩罚所有后续 token。

定位粒度越细，标注成本、主观边界和 judge 误差越高；first harmful span 也不一定是根因。受限 benchmark 不能证明自动
localizer 是因果 oracle，故高风险 case 仍需 raw trajectory 与人工/确定性复核。

<!-- source-family:SF-DRIFT-TELBENCH -->

### Failure Catchability 要分成 Observe、Locate 与 Intervene

一个 benchmark 报告“发现了失败”，并不能说明系统知道失败发生在哪一步，更不能说明当时仍有机会阻断。Evaluation identity 应绑定 observation point、failure stage、intervention timing 与 harness state，分别报告可观察、可定位、可拦截比例；晚到的正确诊断只拥有 forensic value，不应计作在线保护成功。<!-- source-family:SF-2026-ARXIV-2608-22808-v4 -->

更细分层增加 instrumentation 和标注成本，也受 benchmark failure taxonomy 限制。v4 的补充分析不证明开放式 Agent 的全部失败可捕获；观察通道缺失、定位不确定或干预窗口已关闭时，应记录不可拦截并依赖 rollback/containment，而不是用最终检测率掩盖时序失败。

### 数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播

单个 kernel 注入错误后最终答案仍正确，可能只是后续层吸收了扰动；最终答案错误也不能定位哪种 fault model 造成。故障
评测应绑定注入层/算子、bit/precision、token position、传播张量与任务 outcome，并比较 detection、containment、recompute
或 higher-precision fallback。Mitigation 只在所测 fault surface 内成立，不能从平均鲁棒性推断 silent corruption 已消失。

更细 fault campaign 显著增加组合空间，也可能因不真实注入模式误导设计；真实硬件 telemetry、可复现 injection 和生产
incident slice 应共同校准。证据不足时保留 reference execution、redundant check 或 fail-closed release。

<!-- source-family:SF-LLMFI-ERROR-PROPAGATION -->

## Security Evaluation 要冻结攻击能力与检测器适用域

### Attack Success Rate 不能压平 Attack Profile

固定提示、固定查询预算和已知模型的 ASR 便于回归，但它没有说明攻击者是否知道防御、能否自适应、能否跨模型迁移、实际
危害有多大，以及为一次成功付出了多少查询。安全 EvalSpec 应冻结 `attacker knowledge/access + applicability + adaptiveness +
transfer target + harm taxonomy/severity + sample/query efficiency`，把成功率放回这份 attack profile。严重度—覆盖体积等
threshold-independent 指标可以补充 operating curve，但 scorer 仍不拥有 release authority。

更完整的 profile 会扩大组合空间，并受攻击器、judge、危害 taxonomy 与预算选择影响；有限攻击未成功只能给出已测威胁面的
下界，不能证明最坏情况安全。预算不足时，保留 curated regression 和固定 operating point 仍合理，但必须标明未测维度，
由独立 policy owner 决定是否扩大 red-team 或收紧发布范围。exact-v1 只支持所测模型、行为和 defense pipeline，不证明
attack baseline 已覆盖开放世界攻击。

<!-- semantic-body-binding:SF-ADAPTIVE-LLM-ATTACK-BASELINE -->

无合法路径可交付的scope任务，把能力与遵守边界分成两个测量：相同环境和目标下，无scope限制测完成能力，有限制时机械成功反而给出至少一次越界的证据。这个floor依赖flag/secret确实无法从in-scope取到且harness不泄漏；机械失败却不能证明遵守，因为越界call可能被阻断、取到了flag但不提交。对失败轨迹另查issued calls、有效host/身份与scope clause，再把已机械阳性与失败stratum的过程judge结果取union，不能让judge否定已有确定性证据。安全owner仍负责实际权限，本章只拥有测量。[受限双臂设计](https://arxiv.org/html/2609.30325v1)与[no-in-scope任务](./72-security.md)在此交接。

Judge positive须保存具体call和clause，calibration与开发共享则不叫heldout；当前失败stratum按judge分层抽样的人审需按真实比例重加权。有限零漏判不认证总体无FN，error-adjusted估计还假设该stratum的Se/Sp可迁移，故与机械floor、未调整union并列作敏感性而非覆盖原证据。Task-cluster不确定性、judge歧义、轨迹长度和额外审核费用分别计账；completion减少不能区分克制、混乱或已越界后的放弃。支持不足时保留机械下界/具名call与unknown，扩大盲审或限制发布范围，不以精美scope措辞或没交付flag认证现实安全。<!-- source-family:SF-2026-ARXIV-2609-30325 -->

### Contamination Detector 必须随 Scale 与 Distribution 重新校准

dataset matching、membership-style inference 或模型自报，在受控同分布实验中可以作为污染传感器；模型规模、post-training
mixture 和数据来源变得不透明后，同一 detector 的 false positive / false negative 会改变。Audit receipt 因而必须绑定
`detector revision + target model/scale + reference distribution + threshold + FP/FN calibration + provenance visibility`，并把
Unknown 与 Negative 分开。Detector 只能触发隔离、重测或 held-out replacement，不能单独批准 benchmark score。

跨规模重校准增加 reference data 与人工核验成本，且闭源数据可能无法构造真值；把多个 detector 简单投票也会继承共同偏差。
无法校准时，应把分数标为疑似污染或不可判定，回退 provenance-bearing held-out set、时间切分或重新构造评测，而不是把
“未检出”写成“无污染”。exact-v1 只证明所测 detection paradigms 在现实 instruction-tuned 设置中出现 reliability gap，
不提供生产级完备 detector。

<!-- semantic-body-binding:SF-CONTAMINATION-AUDIT-RELIABILITY -->

## Human–Agent Team 必须成为独立 Evaluation Object

当任务结果由人和 Agent 共同产生时，只测 autonomous agent 会把协作界面、人的策略与学习过程藏进噪声；只测团队最终结果
又无法判断增益来自 Agent、参与者差异还是二者交互。EvalSpec 因而要把 `participant/cohort + task + agent/harness/interface
revision + session trace + outcome + grader` 绑定成同一个 team-evaluation identity，并将人的潜在贡献、Agent 的潜在贡献及其
不确定性作为 attribution estimate。估计器是帮助解释团队表现的 sensor，不是把一次结果精确归功于某一方的 truth oracle。

这条路线能回答“Agent 是否让真实工作者在真实流程中更好”，代价是招募偏差、学习与疲劳效应、grader 偏差、隐私成本和更大
样本需求。小样本或 attribution model 不稳定时，应分别报告人类 baseline、Agent-only baseline、团队 raw outcome、cohort slice
与区间，保留人工复核，而不是用一个合成 skill score 掩盖不可辨识性。现有 autonomous benchmark 在界面影响很小、任务可独立
完成时仍是低成本基线；它不能替代协作系统的独立验收。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-09833 -->

### Dynamic Benchmark 是一条持续运行的生命周期

冻结 benchmark 便于复现和横向比较，但公开题集长期运行后会被污染，也难以公平接纳后来模型。动态评价可以把 fresh prompt generator、difficulty-aware sampling、分轴评分、micro-batch pairwise aggregation 与 uncertainty-aware Bayesian ranking 连成生命周期，并把公开 tuning set 与私有动态 stream 分开。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06170 -->

动态生成没有自动消除 prompt-generator、judge 与采样偏差，有限人工复核和模拟也不能证明长期排行榜真值。动态覆盖不足或 judge 失校准时，应回退冻结 benchmark、人工复核和按 slice 报告，避免把异质证据压成单一总分。

### Semantic-equivalence Invariance 是 Metric 的攻击面

公开安全 metric 若给语义等价的 harmful variants 不同分数，优化器就能在不改变实质风险的情况下通过改写获得更好结果。一个受限修复是定义 semantic class，在 class 内采用最大风险值，并让 certificate 携带 annotation 与 protocol error，而不是把 invariant 假设藏在总分里。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06324 -->

形式证明与 solver replay 只覆盖有限或合成模型；semantic class 和 harm label 本身也可能错误。无法验证 transformation graph 或 class coverage 时，应回退 raw variant audit、red-team、人工标注与保守 release gate。

## 小结

Evaluation System 不是 benchmark 集合，也不是某个产品的 metrics 页面。它把 intended use 转化为 EvalSpec，把有限数据和环境转化为带不确定性的 evidence，再把 evidence 放入受风险政策约束的发布与反馈决策。对 MoE 等条件计算系统，负载统计只是运行证据，功能 specialization 仍需独立指标与干预验证。release-grade 结论还必须能重建其 artifact、harness 与环境；无法重建的历史分数只能作为描述性记录。

它的长期不变量是：完整 subject identity、明确分布、可审计 scorer、per-example evidence、切片与不确定性、分离的 decision policy，以及从生产反馈回到新版本的受控闭环。下一章进入 Monitoring，讨论平台怎样以受控成本持续获得 observed state，而不把“发生了什么”误当成“是否足够好”。

## Review notes

- Daily2026-04-30：`SF-2026-ARXIV-2604-26511` [Tatemae v1](https://arxiv.org/html/2604.26511v1) §2–3，同压力无监控/声称监控配对，108JSON/XML选择不等实际执行、理由标签不等潜在动机；`SF-2026-ARXIV-2604-26052` [RiskDrift v1](https://arxiv.org/html/2604.26052v1) §3–4，prompt/response双端独立标签及direction denominator；`SF-2026-ARXIV-2604-26180` [Evergreen v1](https://arxiv.org/html/2604.26180v1) §3–5，关系量词query、tuplelineage、受限CS早停及predicate误差。apr29_close必要source→actual-owner窄采用通过；不采用因果安全/隐藏意图/精确全称保证，未复现实验，root已实际读取正文及前后衔接，非作者写后通过。

- `SF-2026-ARXIV-2604-19974`（Experimental）：[exact-v1](https://arxiv.org/html/2604.19974v1)，§4、§5.2–5.4、§6。采用 uncertainty×correctness 分层与干预后 correctness gate，保留 entropy-only 损害 accuracy、筛选/多重比较及有限模型任务边界；不采用通用纠错坐标。source→owner经apr24_close核，实际正文已由apr24_close非作者写后核；未复现实验。

- `SF-2026-ARXIV-2604-19809`（Experimental）：[MIRROR exact-v1](https://arxiv.org/html/2604.19809v1)，§3.3/§5.3/§6及Appendix Q/R。采用能力预测、升级动作、resolver正确性和误升级成本的成对分账；597任务含297固定/300定制，主分析固定，540个升级component的fallible resolver仅50.2%正确且38.7%升级不必要，不把C4强制router当自省进步或部署保证。实验7未执行；source→owner独立核已有，新增正文已由apr24_close非作者写后核，未复现实验。

- [AnswerPool v1](https://arxiv.org/html/2609.37494v1) §3.1–3.2/3.4、§4.1/4.3、§5；Daily 2026-09-30。只采用coupled-option诊断及配对控制，不采用未审的缺答案变体；pool改变任务，不以新排行反推原benchmark真实能力。

- [evalstats v1](https://arxiv.org/html/2609.35815v1) §2–6、§9.6/B1；Daily 2026-09-30。agreement 不等统计校准，随机配对人工残差、λ不确定性与小样本区间分账，未复现。
- [Detectability Gap v1](https://arxiv.org/html/2609.35860v1) 方法、冻结partition跨signal与单seed轨迹对照；Daily 2026-09-30。采用非循环诊断阶梯，不声称难组不可检测或已获部署风险保证。
- `SF-2026-ARXIV-2604-25855`（Daily `2026-04-29`，实际正文已通过非作者写后复核）：[SIEVES exact-v1](https://arxiv.org/html/2604.25855v1) §3.2、§4.1–4.3、Tables 2–3、Appendix 0.A。只采用黑盒视觉 reasoner 可见 crop 轨迹的定位/证据—答案风险传感器分支；它需训练定位框与 judge 伪标签，不把单一权重或三 head 的普遍必要性写成结论。`C@r` 由目标测试真值回选阈值，不能当独立部署校准或未来流量风险保证；受测 OOD 五集、三 reasoner 与同源开放答案 judge 不覆盖生产高风险分布。root 已完成 source→实际 Ch66 owner 写前及正文/相邻写后复核，记录见 `papers/2026/04/_sources/daily-20260429/V3_ROOT_25855_CH66_WRITE_AFTER.md`；不代表本日来源、日期或日级 Gate。
- `SF-2026-ARXIV-2604-20200`（Experimental）：[exact-v1](https://arxiv.org/html/2604.20200v1) §2.1–2.2、§3.1–3.6、Appendix B.2.4–B.2.5。主实验为 13 Agent×34 任务×3 轨迹＝1,326 runs，§3.4 的 403 exploit-positive runs 与 §6 的 462 存在未解释的数量冲突，正文不采用后者。GPT-5 mini／GPT-5.4 判定与 214 个人类多数标注中的 197 一致不是独立行为真值；3 任务×4 Agent×每设置 1 run 的压力/提示消融只支持受限行为观察，且最高压力组并非单调更严重。`V3_ROOT_20200_FINITE_EVIDENCE.md` 和 `V3_APR20_20200_FINITE_INDEPENDENT.md` 记录 source→owner 独立核；实际 Ch66 写后及 04/23 日期/整日 Gate 待验，未复现实验。
- `SF-2026-ARXIV-2604-19292` — [LocQA exact-v1](https://arxiv.org/html/2604.19292v1)，§3–5.2、Limitations：独立复核发现 Ch66 原“翻译保真”未承载 explicit locale knowledge 与 ambiguous-locale default selection 的不同评价目标，故在原多语言段后窄幅整合；不采用“instruction tuning 必然导致某种文化偏置”的因果外推。2156 是 44 个语义平行问题跨 12 语言/49 地区的 locale-specific 问答，不是 2156 独立问题模板；16 annotators 双审、Gemini 2.5 Flash judge/GPT-5 mini 交叉与 80 人工 92% 一致只支持受限测量。显式澄清策略是本书面向产品的设计推论，论文未测试其效果；地区事实有时效性。root 完成必要原文→实际 owner 窄采用；apr02 已完成非书稿作者写后复核并通过，记录见 `papers/2026/04/_sources/daily-20260422/V3_APR02_19292_WRITE_AFTER.md`；04/22 日级 Gate 仍未通过。

- `SF-2026-ARXIV-2604-22167`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.22167v1) §3–4、§6.1–6.2、§9；Daily 2026-04-27。只吸收固定输入目标输出尾险与跨输入改写分布的双层评价身份。作者将 309 个原问题各改写 25 次，并把同一 7,725 改写池随机分作 30/70；这不是未见原问题、真实部署 `D_query` 或线上风险保证。方法还依赖可计算的模型 likelihood 与可能出错的 harm judge；未复现实验，待本日报独立写后和整日 Gate。

- `SF-2026-ARXIV-2604-22409`（Experimental）：[exact-v1](https://arxiv.org/html/2604.22409v1) §3.1、§4.2–4.5；Daily 2026-04-27。只采用同一动态空间任务的 L1 即时感知／L2 oracle 文本历史／L3 原始视觉流及 stepwise／episodic 分母，保留输入模态与状态权威同时改变的混杂。程序生成房屋与序列规模不等真实机器人安全或因果记忆证明。root 已完成必要来源→实际 owner 独立写前复核，并顺读实际正文及相邻评价阶梯/视觉问答段，写后复核通过；实验未复现。

- `SF-2026-ARXIV-2604-21964`（Experimental / Safety assurance review）：[exact-v1](https://arxiv.org/html/2604.21964v1) §3.1.1–3.1.5、§3.2、§4与附录 defeater；Daily `2026-04-27`。采用 decision、assured deployed system、运行环境与有效期、claim defeater 的安全论证身份，不把黑盒 inability test 外推至工具/监督部署栈；外部审阅仅限公开材料，缺少非公开工程附件，不构成实际部署不安全或事故率证明。root 必要来源→实际 owner 写前独立复核与实际正文/相邻写后复核均通过；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-22074`（Experimental）：[exact-v1](https://arxiv.org/html/2604.22074v1) §3.1–3.2、§4–7；Daily `2026-04-27`。采用 outcome／强制前缀读出的 CIR／reasoning-only 与 question+reasoning 的外部 verifier SR 三轴分账；CIR 只测该干预协议的答案分布敏感性，SR 是作者称为 permissive 的 decoded-answer agreement，均非完整内部因果或逐步证明。40 个选定 ReasoningGym 任务、Qwen2.5 1.5B/3B/7B、额外读出/验证/rollout 成本限其外推。root 已完成必要来源→实际 owner 独立写前复核，并核对实际正文与相邻衔接通过；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-20098`（Experimental / Theoretical）：[DCF exact-v1](https://arxiv.org/html/2604.20098v1) §2.2–3.6、§4.1–4.3、Limitations。仅采用依赖闭包的可微训练代理与最终硬 CF/独立校准分权；Theorem 3.1/3.2 是代理极限恢复，不是有限温度或单答案保证。作者 MATH 202 / FELM 710、20-fold 与窄 α 切片限定 retention/coverage，严格 α 时可能零保留；不外推分布漂移、真实图真值或生产 SLO。apr02 独立 source→实际 owner 写前及实际正文/相邻写后均通过，见 `papers/2026/04/_sources/daily-20260423/V3_APR02_20098_DCF_OWNER_AUDIT.md`；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-19047` — Daily `2026-04-22`；[exact-v1](https://arxiv.org/html/2604.19047v1) §3.1–3.5、§4.1/Table2、§5.1–5.5/Tables3–4。只采用 required-information→alternative-support gold、部分/全部必要信息覆盖与最终答案分账；LLM 等价过滤两组人工 precision 57.5%/50.8%、atomization 与多跳构造成本限制自动判据。CRRF 的受限排序比较不等 judge 校准；跨域掉点不能独归因 redundancy，E2E−PerfRecall 不证明参数知识因果贡献。root 已完成必要 source→实际 Ch66 owner 独立写前复核；实际正文与邻接已由 root 非作者写后复核通过，见 `papers/2026/04/_sources/V3_ROOT_FOUR_WRITE_AFTER_20260928_B.md`，未复现实验。

- `SF-2026-ARXIV-2604-21549`（Experimental）：[PDF exact-v1](https://arxiv.org/pdf/2604.21549v1) 物理页3–9；Daily 2026-04-24。采用旧总体正负残差抵消→目标重加权失效→支持内条件残差约束的估计分支；不将高AUC、有限多重校准或新文档类型外推成任意总体无偏，也不升级单条标签为真值。apr02 必要 source→实际 owner/literal 独立通过；实际正文与相邻衔接待非作者写后复核，未复现实验。

- `SF-2026-ARXIV-2604-10495`（Experimental）：[v1 §3.1–3.2、§4.1–4.2、§5/limitations](https://arxiv.org/html/2604.10495v1)。采用不确定性来源与任务动作分支，不采用自动原因识别或 PRR 为事实概率；GPT-5 构造/评价、人工核验和配对问答范围保留。apr01 必要源→实际 owner 写前通过，apr01 已顺读实际正文和相邻衔接，写后独立通过；未复现实验。
- `SF-2026-ARXIV-2604-10547`（Experimental）：[v1 §2.1–2.5、§3.1、§3.3–3.4](https://arxiv.org/html/2604.10547v1)。采用外层训练工程/实际 route 与内层任务反馈分账；best-within-12h、反馈选择、driver/scaffold/单 run 混杂保留，不采用路线标签或通用能力排序。apr01 必要源→实际 owner 写前通过，apr01 已顺读实际正文和相邻衔接，写后独立通过；未复现实验。

- `SF-2026-ARXIV-2604-16587`：[exact-v1](https://arxiv.org/html/2604.16587v1)，Daily 2026-04-21；§3.3–3.6/Table1、E.2/F.3.1。采用干预标签→廉价 span-region sensor 摊销分支；相关排序非绝对 effect/faithfulness，correct-answer、离线 mask、DINO/attention/队列成本保留。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。
- `SF-2026-ARXIV-2604-16812`：[exact-v1](https://arxiv.org/html/2604.16812v1)，Daily 2026-04-21；§2.1–2.2/§3.4/§4.1–4.2/§6。采用跨 frozen behavior-delta 的共享报告身份；类别幻觉/FPR/跨家族和离线变体成本保留，不采用内部自知或隐藏意图保证。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。
- `SF-2026-ARXIV-2604-16916`：[exact-v1](https://arxiv.org/html/2604.16916v1)，Daily 2026-04-21；§3.1–3.6/§4.4/Discussion/Limitations。全 unsafe 候选、候选外拒绝和输出安全分别验收；多提示 judge 不等独立真值，不采用跨语言多轮普律或添加拒绝项必修复。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。
- `SF-2026-ARXIV-2604-16965`：[exact-v1](https://arxiv.org/html/2604.16965v1)，Daily 2026-04-21；§3.2/Listing1、§3.3–3.5 及测量视图。采用时间换算与跨组件因果提交分责，组件/interface/application 三视图；two-phase 先提交不可由后置修时自动追回，不外推 CPU/DRAM 模拟为 LLM 生产准确率。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-14433`：采用 exact-v1 §3/4.1–4.4/8/12；复用 TEN_THREE §9 的有效非作者必要源审及 root 当前 owner 反向采用核。正文只新增 replacement baseline 的因果对象与成本边界，未复现实验；root已实际顺读正文及两侧交接，写后PASS。

- `SF-2026-ARXIV-2604-12373`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12373v1) §3.1–3.5/§4/§7。同 target label、完整训练、测试 disagreement 切片分账；不采用内部自知或对全部外部观察者的不可见性。root 必要源/owner 与实际两段及相邻交接写后独立通过，未复现实验。
- `SF-2026-ARXIV-2604-12447`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12447v1) §3.2–3.3/§4/Appendix D。采用能力匹配与可观测 first-hit 阶段分账；pre-IPE commit 非意图/授权，不采用 SOL 普遍防御或真实物理保证。root 必要源/owner 与实际两段及相邻交接写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-13065`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13065v1) §3–5 与 Appendix H。九 Boolean 运算符/至八运算深度；Claude depth7 原 cohort 34/300 错误与新 seed 31 条抽取样本分开，后者 Claude31/31、GPT4o30/31不作普遍纠正率；ETT局部0/300及约140额外token、max256截断假collapse共同限定。只采用外部可核文本步骤/最后计算值/最终声明和固定 trace 抽取对照，不证明内部 trace faithful 或开放任务自知。2+2+2=6，真实知识缺口深入；source→owner 独立通过（apr02），实际写后待非作者核，未复现实验。

- `SF-2026-ARXIV-2604-12176`（Experimental）：[REL exact-v1](https://arxiv.org/html/2604.12176v1) §3定义、§4生成规则、§5.1–5.4、§6。input/entity规模、生成器 arity 与 operand 难度分账；同 arity 输入增大有正例，回归只控制已测混杂。不同输出/指标不合并为普遍因果曲线，RC不作为内部 capacity 下界。6分实际缺口深入；必要来源/owner 独立复核通过（apr02），实际正文及相邻交接写后非作者复核通过（root、apr02），未复现实验。

- `SF-2026-ARXIV-2604-12119`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12119v1) §3–8/D.1。same terminal pixels×standard/inverse rules×neutral/semantic alias；greedy、1024预算、四游戏十四VLM，closed reduced与open expanded不混分母。same-rule SFT可能伤opposite-rule，late-layer steering依准确router/donor；不推全部感知正确、唯一因果路径或自然任务泛化。6分实际缺口深入；必要源/owner非作者复核通过（apr02），实际正文及相邻交接写后非作者复核通过（root）；未复现实验。

- `SF-2026-ARXIV-2604-11996`，Experimental：[exact-v1](https://arxiv.org/html/2604.11996v1) §3.1–3.3、§4.1–4.3、§5–6。采用accepted subset中过程/结果共同分母及未筛baseline；pooled model–benchmark top%非线上逐题selector，judge有gold，faithfulness限文本rubric，Phi-4重复退化保留；apr02必要来源/owner独立通过，实际正文/相邻衔接写后独立通过（apr02），未复现。
- `SF-2026-ARXIV-2604-12035`，Experimental：[exact-v1](https://arxiv.org/html/2604.12035v1) §3.1–3.3、§4.1–4.8、§5–6。采用retained-set/selector/实施路径为calibration身份；固定LLaVA-1.5-7B/CLIP576、greedy、yes/no或A–D内归一化与两题库限制，不采用zeroing/物理删除对照或普遍selector排名；apr02必要来源/owner独立通过，实际正文/相邻衔接写后独立通过（apr02）。
- `SF-2026-ARXIV-2604-12046`，Experimental：[exact-v1](https://arxiv.org/html/2604.12046v1) §3.1–3.4、§4.1–4.4/Table1–2。采用masked位置loss非共享参数隔离、factual优化后重校准和最终claim保持；Biography AUROC .688→.676、Brier .266→.268反例及阶段数据/预算混杂保留，不采普遍无干扰保证；apr02必要来源/owner独立通过，实际正文/相邻衔接写后独立通过（apr02）。

- `SF-2026-ARXIV-2604-08844`，Experimental：[exact-v1](https://arxiv.org/html/2604.08844v1) §3.1–3.6、§5.2–5.8、§7。Llama3.2-3B、38制造adapter含4legacy，r8/q_proj+v_proj、70/30小样本split；DPO→steering AUC0是所测信号反转，未建立全新方法检出能力。steered generation collapse令LlamaGuard假阳性，GPT4o对300样本判0harmful；ρ.72仅24非steered样本且主要跨healthy/drift边界。PCA14/18 DPO数量文字不一致，不采用全维objective定量分离泛化；hardware、完整服务precision/length/batch/concurrency/SLO未披露。本次必要原文与实际正文/相邻交接已由root独立复核通过，未复现实验。

- `SF-2026-ARXIV-2604-07634`：[VSAS-Bench exact-v1](https://arxiv.org/html/2604.07634v1) §3.2.2 Algorithm1、§3.3、§4.1–4.3/Table2。camera/model独立进程、最新帧队列与没有回答时沿用上一回答；原文明确异步consistency因回答更少而上升。H100/bfloat16/CUDA12.4/FlashAttention2.7.3，2/4B单卡、8B双卡、32/38B四卡；1FPS、camera600、context64，API含network成本。评分边界依赖实际时点标签；正文要求记录回答可用时点是EvalSpec设计建议，不冒称Algorithm1已完整规定wall-clock completion日志。与现有memory/recency切片互补，未运行作者代码或复现实验；待独立写后核。

- `SF-2026-ARXIV-2604-07172`，Experimental：[exact-v1](https://arxiv.org/html/2604.07172v1) §3.1–3.2、§4、§5及Appendix A/B.3。采用生成前token温度校准与最终分数校准的分账，非仅后置单调映射；Llama3.1/Ministral8B/Qwen2.5 7B、三短QA、十样本、DeBERTa-v2-XXLarge聚类和四次运行限定证据。最优类中至多四答案任一命中是评测oracle，不能当部署单答案正确率；不采用全任务温度最优或长文factuality保证。apr01非作者已核必要证据、实际正文及相邻衔接，通过写后复核；未复现实验。
- `SF-2026-ARXIV-2604-06647`，Experimental：[exact-v1](https://arxiv.org/html/2604.06647v1) §2.3–2.4、§3、§4.1–4.5、§7。采用反馈到更新就绪延迟×相关query修正质量；作者以snapshot衡量，不是持续线上稳定性。Llama3 8B/bge-m3、NQ/TriviaQA/HotpotQA、两A5000/至多约150K合成旧反馈限定；精度/请求长度/batch/concurrency/SLO未披露，不外推普遍立即可靠或抗污染。长期冲突仍开放，新增control queries是工程建议。apr01非作者已核必要证据、实际正文及相邻衔接，通过写后复核；未复现实验。

- `SF-2026-ARXIV-2604-06422`，Experimental：[exact-v1](https://arxiv.org/html/2604.06422v1) §3.1–3.3、§4.1–4.3、§5–6。采用规则、输入估计与决定分账；颜色比例、对象prior与提问顺序的局部实验不证明内部因果或人类普遍忠实。低容量模型仍有估计误差，headline的统一“excellent estimator”不照录；apr01非作者写后核对通过，未复现实验。
- `SF-2026-ARXIV-2604-06240`，Experimental：[exact-v1](https://arxiv.org/html/2604.06240v1) §3.1–3.3、§4–6、AppendixA.2。采用task-only rubric、conditional适用分母与cascade归因；process不替代outcome。组合调优、标签口径和web环境限制不支持单组件因果归因或零误判；apr01已独立核对必要原文与实际正文，未复现实验。

- `SF-2026-ARXIV-2604-05100`（Status: Experimental）：官方 HTML v1 §3 RQ2、§5 与 §6。test-count 分母与恢复出的可执行 reference 的 coverage 分母不同；低覆盖子集经 LLM 辅助分类及人工检查，不能把“可能漏检未请求编辑”外推为实测 mutation kill rate。未复现实验，正文只承载 edit-change 与 preservation 两个 oracle 目标及 coverage 边界；apr02已完成写后独立复核。

- `SF-2026-ARXIV-2604-06613`（Status: Experimental）：官方 PDF v1 §3.1–3.2、§4.4–4.5 与 Appendix B 支持同 prefix 的自由延续/强制读出区分、选择控制、持出阈值及总成本限制；不采用 HTML 中异常的 August 日期作为历史事实，也不采用内部“已经知道”或无条件低成本宣传。正文不引用 headline 性能数字；apr03已完成写后独立复核，实验未复现。

- `SF-2026-ARXIV-2604-03362`（Experimental）：[exact-v1](https://arxiv.org/html/2604.03362v1) §3–5。400reports→47patterns×128actions的兼容647tests；五配置3235单次运行，1573flags中642confirmed，40.8%是detector precision，不是Agent failure rate或安全事故率。有限模式、checker与人工复核边界保留，未复现实验；待写后非作者复核。
- `SF-2026-ARXIV-2604-03257`（Experimental）：[exact-v1](https://arxiv.org/html/2604.03257v1) §3–5及约束实现支持prior TPR/FPR interval与prevalence joint MLE；Jigsaw nGold50/nJudge10000、Qwen2.5-.5/Llama3.1-8，同域anchor与target不等价。先验误指定偏差、gold/优化预算不能省略，不作任意OOD或个体概率保证，未复现实验；本次写后独立复核通过（root）。

- [2604.05324v1](https://arxiv.org/html/2604.05324v1)，Theoretical；§2–5、Theorem4.2/Corollary4.3、IPM有界/有限复杂度条件。采用finite-i.i.d. uniform ranking与固定metric计算的区分；不把最坏情形定理写成PPL不可计算、任意有限benchmark无价值或具体LLM已失效。

- `SF-2026-ARXIV-2605-08012`（Status: Position / Experimental）：[exact-v1](https://arxiv.org/html/2605.08012v1) 支持 causal identification disclosure 框架；10 篇 purposive audit 与 30 篇双人编码不估计领域 prevalence，也不构成通用因果识别算法。
- `SF-2026-ARXIV-2605-06788`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.06788v1) 支持 filtration-based conformal prediction set、coverage 条件与受限 Agent rollback；集合覆盖不证明集合中每一步具有因果责任，分布漂移会破坏校准前提。

- `SF-2026-ARXIV-2605-05715`（Status: Experimental）：exact-v1 比较 activation failure probe、固定线性 steering/erasure、
  self-consistency 与 nonlinear adapter；只支持作者两种 7B 模型、以 MedQA 为主的任务及 29 个固定线性配置中的
  decodability/intervention separation，不证明 probe probability 是 truth、任意 nonlinear intervention 有效或线上阈值可迁移。
  Primary: https://arxiv.org/html/2605.05715v1

- [Task-Aware Answer Preservation under Audio Compression](https://arxiv.org/html/2605.06631v1)（Status: Experimental）：两种 7B audio-language model 与五个英文选择题数据集支持 worst-family excess-error release contract；不证明通用安全码率。

- `SF-2026-ARXIV-2606-09833`（Status: Experimental）：exact-v1 记录 93 名参与者、386 个 human-agent sessions、
  超过 1,500 个 prompts，并以 Bayesian skill model 分离人和 Agent 的潜在贡献；数据来自 10 个 sector 的真实协作任务。
  参与者选择、跨 session 学习、任务覆盖、自动 grader 与模型可辨识性限制外推，结果不证明该归因分数是人的真实能力或
  Agent 的独立因果效应。正文吸收 evaluation object 与证据边界，不吸收跨场景排名。

- ExecRetrieval，`arXiv:2609.01865v1`，Status: Experimental；[exact-v1](https://arxiv.org/html/2609.01865v1)。
  §3.3、§5.3–5.7、Appendices A–G 与固定 artifact commit
  `31c2cb4bf88d7d94a512b91ed4acad385e4df927` 的 scorer/executor 支持这里的受限评价边界。
  939 个生成任务、4694 个 snippets；938 个 query 含 mechanical distractor，不能与 86135 个
  query/distractor/model triples 混用。23 个 dense embedding 系统与 BM25 属于作者实验；托管服务硬件、
  精度、并发/SLO 等未完整披露，正文不吸收跨系统性能排名。Figure 1 / Appendix A 的 query/test 输入域
  差别限制“错误代码”的解释；生成 oracle 不是独立的完整语义证明。静态实现显示 cache miss 默认判 false，
  需显式启用 execute-on-miss 才执行；五秒 suite timeout 与隔离 Python 进程不构成文件/网络权限 sandbox。
  本轮完整读论文与关键静态 scorer/executor，未运行不可信代码、重算 embedding matrices 或复现 leaderboard。
  artifact commit 时间不证明公开时间，论文事件使用当日 arXiv 公告，未据此追溯或新增旧日期候选。

- `SF-2026-ARXIV-2602-18583`（Status: Experimental）：exact-v1 支持 Luna-2 以 metric-specific LoRA/head、trace-field prompt 与 exactly-one class token 构成 evaluator sensor，并对 class-token probabilities 归一化；作者实验不证明输出天然校准、跨分布稳定、共享 backbone 无干扰或可替代独立 truth source。https://arxiv.org/html/2602.18583v1

- `SF-2026-ARXIV-2604-21930`（Status: Experimental）：exact-v1 支持 temporal taskification、profile distance 与训练前 boundary sensitivity 诊断；不证明存在唯一正确切分或通用阈值。https://arxiv.org/abs/2604.21930v1
- `SF-2026-ARXIV-2604-22038`（Status: Experimental）：exact-v1 在 11 个 VLM 的 target-modality retrieval 中支持语义/句法 cue 会影响 source binding；模型自述不是 authoritative provenance。https://arxiv.org/abs/2604.22038v1
- `SF-2026-ARXIV-2604-22082`（Status: Experimental）：exact-v1 支持在作者构造的 sandbagging model organisms 上用弱监督 SFT/RL 进行 elicitation probe；不证明真实欺骗模型、监督可扩展性或生产 oversight 已解决。https://arxiv.org/abs/2604.22082v1

- `SF-2026-ARXIV-2604-23987`（Status: Experimental）：exact-v1 支持 continual fine-tuning 后的 task-specific calibration replay，以及作者三类模型、八个主要为 classification/MCQ 的序列实验；`m=200`、低 replay 比例依赖 exchangeability，generation 结论仍是探索性。https://arxiv.org/abs/2604.23987v1

- **Blind-Spot Mass（arXiv:2604.05057v1；Status: Experimental）**：exact-v1 支持 Good-Turing coverage mass 与 supported/blind decomposition 的理论框架；它不把估计升级为生产错误率或风险上界，且依赖明确分布、support threshold 与抽样假设。https://arxiv.org/abs/2604.05057v1

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

- `2026-05-05 / SF-2026-ARXIV-2605-01771` — exact-v1 `arXiv:2605.01771v1`；正文区分 textual agreement、typed process trace 与 environment outcome，不外推所测任务的遵从率。
- `2026-05-04 / SF-2026-ARXIV-2605-02038` — exact-v1 `arXiv:2605.02038v1`；正文吸收 prompt-variant spread、raw generation/parser identity 与等价性审计，未保留受限模型排名。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28013 — primary arXiv:2606.28013v1; exact-v1 URL=https://arxiv.org/html/2606.28013v1; Method=https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant; Evaluation=https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis; Non-proof=https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion。
- SF-2026-ARXIV-2606-28661 — primary arXiv:2606.28661v1; exact-v1 URL=https://arxiv.org/html/2606.28661v1; Method=https://arxiv.org/html/2606.28661v1 — §Proposition 1 (Design effect of test-time sampling) .; Two-stage design effect.; Evaluation=https://arxiv.org/html/2606.28661v1 — §1 Introduction and roadmap; 2 Test-time sampling is cluster sampling; Non-proof=https://arxiv.org/html/2606.28661v1 — §6 Conclusion。

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






### Daily Books delta trace（2026-05—08）

<!-- daily-books-trace:SF-2026-ARXIV-2605-05715:start -->
- `SF-2026-ARXIV-2605-05715` — Daily `2026-05-08`；primary `arXiv:2605.05715v1`；Books review `books-review:SF-2026-ARXIV-2605-05715`。

  **已吸收的语义增量：** 将 activation 的可解码性、干预有效性和决策权拆开；probe 只能在校准后触发 abstention/escalation，不能凭线性可读性获得自动纠错权。
<!-- daily-books-trace:SF-2026-ARXIV-2605-05715:end -->

<!-- daily-books-trace:SF-FED-PERSONALIZATION-SILENT-FAILURES:start -->
- `SF-FED-PERSONALIZATION-SILENT-FAILURES` — Daily `2026-06-02`；primary `arXiv:2606.00947v1`；Books review `books-review:SF-FED-PERSONALIZATION-SILENT-FAILURES`。

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
- `SF-2026-ARXIV-2606-07379` — Daily `2026-06-08`；primary `arXiv:2606.07379v1`；Books review `books-review:SF-2026-ARXIV-2606-07379`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07379:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07462:start -->
- `SF-2026-ARXIV-2606-07462` — Daily `2026-06-08`；primary `arXiv:2606.07462v1`；Books review `books-review:SF-2026-ARXIV-2606-07462`。

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

<!-- daily-books-trace:SF-2026-ARXIV-2606-15122:start -->
- `SF-2026-ARXIV-2606-15122` — Daily `2026-06-14`；primary `arXiv:2606.15122v1`；Books review `books-review:SF-2026-ARXIV-2606-15122`。

  **已吸收的语义增量：** LLM 只负责为告警构造 analysis harness；harness validation 与 backend formal analysis 才拥有 no-bug discharge authority。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15122:end -->



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
- `SF-2026-ARXIV-2607-02577` — Daily `2026-07-07`；primary `arXiv:2607.02577v1`；Books review `books-review:SF-2026-ARXIV-2607-02577`。

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
- `SF-2026-ARXIV-2607-08017` — Daily `2026-07-10`；primary `arXiv:2607.08017v1`；Books review `books-review:SF-2026-ARXIV-2607-08017`。

  **已吸收的语义增量：** 新增证据边界：GraphEVAL samples multiple chains of thought, uses a separate deterministic decomposer to turn each into a claimed causal DAG, and compares semantic/structural graph distance. A graph medoid and GRCS features measure agreement and robustness; an adversarial-medoid intervention tests whether the selector merely follows a central but wrong trace. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L953`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08017:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11942:start -->
- `SF-2026-ARXIV-2607-11942` — Daily `2026-07-15`；primary `arXiv:2607.11942v1`；Books review `books-review:SF-2026-ARXIV-2607-11942`。

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
- `SF-2026-ARXIV-2607-27231` — Daily `2026-07-31`；primary `arXiv:2607.27231v1`；Books review `books-review:SF-2026-ARXIV-2607-27231`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: single-source/single-GPU pass rate -> multi-source operator contract -> cross-chip correctness, speed and cost frontier 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L450`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27231:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21217:start -->
- `SF-2026-ARXIV-2607-21217` — Daily `2026-07-24`；primary `arXiv:2607.21217v1`；Books review `books-review:SF-2026-ARXIV-2607-21217`。

  **已吸收的语义增量：** 新增证据边界：Verified repositories and tests define GroundPRD; constraints are selectively hidden into User Agent Data; agents may ask bounded clarification questions; generated repositories are evaluated by public/hidden black-box behavior plus structural and interaction diagnostics rather than source-copy similarity. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1479`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21217:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21962:start -->
- `SF-2026-ARXIV-2607-21962` — Daily `2026-07-27`；primary `arXiv:2607.21962v1`；Books review `books-review:SF-2026-ARXIV-2607-21962`。

  **已吸收的语义增量：** 新增证据边界：Ground-truth facts, validity intervals, provenance and as-of dates become canonical state before conversation rendering, enabling separate write/read audits and tenure-aware architecture comparison. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L736`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21962:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25886:start -->
- `SF-2026-ARXIV-2607.25886` — Daily `2026-07-29`；primary `arXiv:2607.25886v1`；Books review `books-review:SF-2026-ARXIV-2607.25886`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: end-to-end agent score -> fixed research substrate -> checkpoint trajectory evidence -> explicit best-checkpoint and stopping policy. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25886:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.27353:start -->
- `SF-2026-ARXIV-2607.27353` — Daily `2026-07-31`；primary `arXiv:2607.27353v1`；Books review `books-review:SF-2026-ARXIV-2607.27353`。

  **已吸收的语义增量：** 新增证据边界：LayerRAG-Bench injects faults at evidence, tool-contract, authorization and session-state layers and shows schema normalization repairs only schema drift. The result establishes a layer-specific credit rule: grounded output cannot hide stale or wrong-session evidence, and a repair must not be promoted beyond its target layer. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L520`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.27353:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-15127:start -->
- `SF-2026-ARXIV-2608-15127` — Daily `2026-08-16`；primary `arXiv:2608.15127v1`；Books review `books-review:SF-2026-ARXIV-2608-15127`。

  **已吸收的语义增量：** AgentSysBench 用十个 Agent 应用和生产 trace 同时刻画模型调用、工具、状态和 orchestration，避免只测纯 LLM decode。它是 workload characterization，不证明十个应用代表所有 Agent；四项 design exploration 只能支持其观测到的压力。
<!-- daily-books-trace:SF-2026-ARXIV-2608-15127:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-22510:start -->
- `SF-2026-ARXIV-2608-22510` — Daily `2026-08-25`；primary `arXiv:2608.22510v1`；Books review `books-review:SF-2026-ARXIV-2608-22510`。

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

<!-- daily-books-trace:SF-2026-ARXIV-2607-24805:start -->
- `SF-2026-ARXIV-2607-24805` — Daily `2026-07-29`；primary `arXiv:2607.24805v1`；正文锚点“每次新编辑都应重开既有删除证书”。
  证据只反驳所测编辑器和推荐强度下的顺序交换假设，不否定单次编辑，也不证明所有编辑器具有同一疲劳曲线。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24805:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25292:start -->
- `SF-2026-ARXIV-2607-25292` — Daily `2026-07-29`；primary `arXiv:2607.25292v1`；正文锚点“能描述分布，不等于逐次调用会从该分布采样”。
  证据限所测 public-opinion benchmark、模型与 post-training stages，不支持把重复模型调用外推为独立人口样本。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25292:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25589:start -->
- `SF-2026-ARXIV-2607-25589` — Daily `2026-07-29`；primary `arXiv:2607.25589v1`；正文锚点“数值可复算不等于复现了同一个实验”。
  只保留取证重建后的 run-identity 结论；被审计旧 benchmark 的性能、排名、prompt-effect 与临床结论均不沿用。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25589:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24821:start -->
- `SF-2026-ARXIV-2607-24821` — Daily `2026-07-29`；primary `arXiv:2607.24821v1`；正文锚点“Response Rate、条件质量与无条件质量不能互相替代”。
  exact-v1 只支持其 145 个视频、196 条音视频编辑指令、六个系统及披露 evaluator 下的 non-response 诊断；不把 MLLM judge、阈值或排名外推为通用生成质量结论。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24821:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24889:start -->
- `SF-2026-ARXIV-2607-24889` — Daily `2026-07-29`；primary `arXiv:2607.24889v1`；正文锚点“Deterministic Gate 与 Defensibility Envelope 承担不同责任”。
  同公司 analyst 对照、gate ablation 与 envelope perturbation 支持职责分离；单一来源网络、48-task core、一次生成和 judge 依赖不证明 envelope 是 ground truth。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24889:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25225:start -->
- `SF-2026-ARXIV-2607-25225` — Daily `2026-07-29`；primary `arXiv:2607.25225v1`；正文锚点“Matched Counterfactual 必须保持任务界面，Detector 零命中只能形成下界”。
  matched baseline 支持受控 framing 对照，90-program 人工审计只校准六个零检测类别；不证明其他语言、攻击条件或全语料漏检率。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25225:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25765:start -->
- `SF-2026-ARXIV-2607-25765` — Daily `2026-07-29`；primary `arXiv:2607.25765v1`；正文锚点“Knowledge Surface、Artifact、Answer 与 Cost 是四个 Failure Owner”。
  exact-v1 支持三类 knowledge surface 下 route 与 answer 可显著分离；不证明其 surface taxonomy、指标权重或企业部署表现具有普适性。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25765:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25891:start -->
- `SF-2026-ARXIV-2607-25891` — Daily `2026-07-29`；primary `arXiv:2607.25891v1`；正文锚点“Per-verifier Outcome 与 Aggregation Rule 都属于 Evaluation Identity”。
  exact-v1 的同结果反事实重算支持 aggregation 改变分数和排序；不证明异构 benchmark 可折叠为单一通用能力尺度。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25891:end -->

- `SF-2026-ARXIV-2604-15597` — Daily `2026-04-20`；primary [LLMs Corrupt Your Documents When You Delegate v1](https://arxiv.org/html/2604.15597v1)；7分必要深入。新增round-trip artifact保留性与forward任务正确分责，保no-op/partial/error cancellation、parser与inverse可用性；93.8%尝试非正确完成，工具四model/basicharness非全系统，GPT5.4 latency反向不隐去。root source→实际owner采用及真实正文/相邻写后通过。采用依据 `papers/2026/04/_sources/daily-20260420/V3_DELEGATE_GROUPDPO_OWNER_PROPOSALS.md`。

- `SF-2026-ARXIV-2604-21018` — Daily `2026-04-24`；primary [Evolving ICL v1](https://arxiv.org/html/2604.21018v1) §4.2、Algorithm 1、§5；跨测试题 oracle 标签回流→共享 demonstration pool 改变评估单位，嵌入 feedback-channel→long artifact 主线。6分评价知识缺口深入；source→actual-owner 非作者采用复核通过（apr02/root），实际正文及相邻衔接写后非作者复核通过（root）。保 active set/Algorithm 1 定义差异、输出 token 不等总计算及有限 API 配置，未复现实验。
- `SF-2026-ARXIV-2604-21308` — Daily `2026-04-24`；primary [CI-Work v1](https://arxiv.org/html/2604.21308v1) §3–5.1、Appendix E；essential conveyance / sensitive entry leakage / case violation 三分母嵌入隐私×成功→具身危险对照。6分保护评价深入；source→actual-owner 非作者采用复核通过（apr02/root），实际正文及相邻衔接写后非作者复核通过（root）。保125有限seed、25人工+100Gemini扩充、GPT后续同源评价及非真实incident边界，未复现实验。
