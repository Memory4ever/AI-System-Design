# 第72章 Security

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-SECURITY`
**Legacy Chapter:** Ch68
**Status:** Draft

**Roadmap Intent:** 模型、数据、API、Prompt、工具调用的安全边界。

## 本章要回答的问题

AI Platform 的安全为什么不止 API authentication？数据、训练、artifact、runtime、Prompt 与工具调用形成了哪些新 trust boundaries？如何避免把模型输出当成可信指令？

本章的核心判断是：**AI security 是贯穿 capability production、delivery 与 action 的风险管理。平台必须识别资产、主体、数据流和信任转换，并用 provenance、least privilege、isolation、validation 与 audit 建立纵深防御。**

## 从资产与信任边界开始

需要保护的资产包括：

- source data、labels 与 user context；
- code、images、dependencies 与 credentials；
- checkpoints、adapters、tokenizers 与 prompts；
- registry metadata、evaluation 与 approvals；
- GPU nodes、runtime memory 与 KV Cache；
- APIs、tools、business systems 与 audit evidence。

主体包括用户、service accounts、controllers、training code、model server、model output 和 external tools。模型生成的文本不是可信主体，也不应自动获得调用者全部权限。

## 生命周期威胁

```text
Data
  poisoning, leakage, license/provenance failure

Training
  untrusted code, secret exposure, compromised dependency

Artifact
  overwrite, substitution, unsafe deserialization, model theft

Serving
  auth bypass, DoS, side channel, data exfiltration

LLM/Agent
  prompt injection, insecure output handling, excessive agency
```

单一 WAF 无法覆盖这条链。每次从一层向下一层传递，都需要验证 identity、integrity 和 authorization。

## 隐私检测是 Policy-bound Sensor，不是安全判决

把 PII/secret detector 放到 ingestion、training corpus、retrieval、logging 或分享路径之前，
可以减少敏感数据进入后续系统。但它的正确系统位置是 **候选敏感 span 的 sensor**：

```text
untrusted text
→ policy/version-bound detector
→ candidate spans + classes + confidence
→ local policy decision
→ mask / remove / pseudonymize / review
→ audit and downstream minimization
```

检测模型的 label taxonomy、decision boundary 和 operating point 决定它能看见什么。漏检会
暴露数据，过度遮蔽则可能删除审计、医疗或法律判断需要的上下文；语言、地域、文档格式和
新 credential pattern 都会导致 distribution shift。因此，本地运行能缩小原文离开边界的
范围，却不能把未命中的文本证明为匿名，也不能替代 consent、retention、access control 或
合规判断。

OpenAI Privacy Filter 的 model card 明确把该模型限定为 data-minimization/redaction aid，
而非 anonymization 或 compliance guarantee。这一案例的长期结论是：**privacy filter 必须
绑定组织策略、目标分布、校准版本和人工升级路径**；默认阈值和作者 benchmark 不得外推为
任意 tenant、语言或高风险场景的安全保证。

Learned anonymization policy 进一步把 detector、rewrite 与 utility 放进一个经验优化回路：给定某类 attacker、
downstream task 和文本分布，选择删改哪些 span 以形成 privacy/utility Pareto。它可以比固定 redact rule 更适应
上下文，却不能提供 Differential Privacy 的跨攻击者数学保证。其 identity 至少包含 attacker model、utility
metric、task/data distribution、rewrite policy、threshold 和 human escalation。Attacker、语言或用途变化后，
旧 operating point 可能失效；生成式 rewrite 还可能改变事实或制造新敏感线索。确定性规则在强格式、法规字段
或低延迟路径中继续成立。Adaptive Text Anonymization 的实验只支持其所测 contract，不应被写成 DP 或
compliance guarantee。

### 从独立 Span 到关系感知的本地 Sanitization

独立 span detector 在规则字段、固定 credential pattern 或低延迟路径中仍然合理，但它容易漏掉**关系推断**：姓名、
机构、罕见职责或时间线单独看都不敏感，组合后却可能唯一指向某人。关系感知分支把本地 sanitization 组织为：

```text
candidate sensitive spans
→ contextual leakage nodes
→ pairwise utility / leakage edges
→ local constrained selection
→ opaque placeholders sent across boundary
→ consistency-gated restoration on client
```

原文、graph、selection policy 和 restoration mapping 都由 client security boundary 拥有；cloud model 只看到不透明
placeholder。Restoration 必须校验 placeholder identity、数量、位置和 mutation，任何未知、丢失或重复 token 都应
fail closed，而不能“尽量猜回”。该机制用图构建、`O(n·k)` 邻接筛选、utility loss 和 estimator calibration 换取对
组合泄漏的覆盖；single-turn、固定 attacker 或有限 pairwise graph 不能证明对 adaptive attacker、长会话或外部知识
的完备防护。Regex/NER 继续承担确定性基线，生成式 rewrite 处理更强语义改写，DP 则拥有发布级数学边界；三者是
分层与替代分支，不应被一个 sanitization 分数合并。

## Differential Privacy 先定义被保护对象，再选择机制

PII redaction 尝试识别内容；Differential Privacy（DP）则限制相邻数据集变化对已发布结果
分布的影响。抽象地，若相邻数据集 `D` 与 `D'` 只相差一个被保护单元，随机机制 `M` 满足：

```text
Pr[M(D) in S] <= exp(epsilon) * Pr[M(D') in S] + delta
```

`epsilon`、`delta` 只有在 adjacency、privacy unit、sampling、composition 与 accountant 都
明确时才有意义。“使用了 DP”不是独立安全结论。特别是同一用户可能贡献多条对话：
example-level DP 限制单条记录影响，user-level DP 才限制该用户全部记录的联合影响，后者
通常需要更强 clipping/contribution bound 与更多 noise。

2025 年几项工作形成了一条有价值的 `Layering / Dependency`，不是互相替代：

| 发布对象 | 被保护单元与机制位置 | 获得什么 | 新增代价 |
| --- | --- | --- | --- |
| Synthetic data | private prediction 在 token aggregation 时消费 budget | 下游可复用 DP output | 可发布数量受 budget 限制，生成昂贵 |
| Fine-tuned model | user-level clipping、sampling 与 noisy update | 模型发布不强依赖单个用户 | contribution bound 丢数据，noise 损失 utility |
| Training runtime | distributed clipping/noise/accounting/auditing | 把数学机制落实到并行训练 | shard、microbatch、padding 和随机数都进入正确性边界 |
| Usage insights | DP clustering/keyword extraction 后再由 LLM summarization | 发布总体使用模式 | 小群体信号和稀有主题可能被抑制 |

Inference-time private prediction 适合只需有限 synthetic outputs、又不希望私有训练 target
model 的场景；私有 fine-tuning 有较高固定成本，却可重复服务更多请求。JAX-Privacy 之类的
runtime 把 clipping、noise、accounting 和 canary auditing 组合起来，但 library correctness
不自动证明调用方选择了正确 privacy unit 或 composition。Usage analytics 则利用
post-processing：先把敏感数据压到 DP output，再让非私有 LLM 解释该 output；LLM 不会增加
前序 DP budget，却可能产生错误解释，因此 accuracy/evaluation 仍然独立存在。

完整 DP production contract 至少包含：

```text
privacy unit / adjacency
+ contribution bound and clipping
+ epsilon, delta and accountant version
+ sampling and composition scope
+ distributed implementation equivalence
+ empirical audit / canaries
+ utility slices and release policy
```

DP 限制单个单位对输出的可辨识影响，不会自动阻止数据 poisoning、保证群体公平、删除输出
中的公开事实，或替代 access control、retention 与 incident response。它是一种可组合的发布
边界，而不是安全体系的总开关。

### Privacy Accountant 必须与真实实现同构

把 DP-SGD 抽象为“Poisson sample → per-example clip → sum → Gaussian noise”便于分析；生产实现可能改变抽样、聚合顺序、归一化、空 batch 或 clipping 位置，使真实随机机制不再等于 accountant 假设。此时报告的 `epsilon` 并不会自动继承到实现。

```text
privacy unit and adjacency
→ executable sampling / clipping / aggregation path
→ mechanism-conformance test
→ matched accountant
→ empirical audit and release gate
```

Conformance 检查增加实现约束、审计和性能成本，却是数学保证落地的必要条件；经验攻击未发现泄漏也不能修复错误证明。实现与标准机制无法证明等价时，应使用针对真实机制的保守 accountant、修正实现或停止 privacy claim，而不能以训练 utility 正常作为替代证据。

<!-- source-family:SF-2026-ARXIV-2605-15648 -->

### Hidden State Release 不天然位于 Privacy 与 Utility 的中间地带

把中间表示视为“比原始输入安全、比最终输出有用”的折中，在下游任务与攻击面固定时容易成立；只要 hidden state 仍保留任务信息，它也可能保留敏感属性。Release owner 必须先声明允许的下游能力、攻击者知识与撤销边界，再在 architecture co-design、受限查询接口或不发布之间选择，不能只提高噪声后宣称安全。

受限接口减少泄漏面，却牺牲通用复用并增加服务成本；高信任同域 pipeline 可在隔离边界内共享，跨租户或公开发布则应采用更强 gate。arXiv:2605.24042v1 的分析与实验只支持其表示和攻击设置，不证明任意噪声阈值都能同时保持隐私与任务效用。

<!-- source-family:SF-2026-ARXIV-2605-24042 -->

## Capability Access Control 可以前移到训练状态

常见防线位于模型输出之后：refusal、classifier、gateway policy 和 tool authorization。
这些机制仍然必要，但它们管理的是“已有能力何时可以被调用”，没有改变能力已经分布在
base weights 中这一事实。另一条实验性分支，是在训练阶段改变敏感知识的 state ownership。

`Gradient-Routed Auxiliary Modules (GRAM)` 提供了一个受限案例：模型在通用数据上更新
共享参数；遇到已标注的敏感类别时，冻结共享参数，只让对应 auxiliary module 接收更新。
部署时保留或移除 module，以近似不同的 data-filtered model variants。

```text
output-time control
  refusal / classifier / policy
  -> 成本低、可快速更新
  -> 能力仍在共享 weights 中，存在 bypass 风险

separate filtered models
  -> state boundary 最清晰
  -> 每个能力组合都要独立训练和治理

training-time modular isolation
  -> 一次训练产生可组合 capability modules
  -> 依赖数据标签、gradient routing 与 module integrity
  -> 新增组合泄漏、共享表示旁路和 artifact provenance 风险
```

这条路线与 MoE 只有 `Explanatory Analogy`：二者都使用模块与路由，但 MoE 的 owner 是
条件计算和容量，GRAM 的 owner 是哪些参数可以从哪类数据学习。作者实验覆盖 50M～5B
参数且明确标记为 preliminary，尚未用于 Anthropic production models；更大的绝对模型
即使“移除”某类 module，仍可能凭通用知识保留相关能力。因此它不能替代输出时 policy、
最小权限工具边界或独立 evaluation。

MoE 还引入另一类与 availability 不同的安全边界：**routing 本身可能成为攻击面**。普通故障分析关心 expert overload、drop 或通信失败；主动输入优化则可能在输出仍流畅时，把 token 流量引向较少承担 safety behavior 的 expert path。于是安全回归不能只测最终 refusal rate，还要把 router revision、top-k policy、expert assignment distribution 与 safety slice 绑定，检测输入扰动下异常的 routing drift。

router telemetry 只是 sensor，不能据单次 expert attribution 删除 expert 或放行输出；专家功能会重叠，相关性也不等于因果。最终输出 policy、tool authorization 和 safe-commit Gate 仍保留。密集模型、固定路由或没有可解释 expert identity 的 runtime 可以继续只做端到端对抗评测；只有 routing signal 可复算且能在独立安全切片中重现时，才把它用于诊断和 canary，而不是新建一条未经证明的安全 authority。

<!-- source-family:SF-ROUTEHIJACK-MOE-SAFETY-ROUTING -->

训练数据过滤也可以前移 capability boundary，但粒度不同。Document removal 改变整段分布；token-level
loss mask 可以保留上下文、只阻断目标位置的梯度；token removal 更强，却会破坏 syntax 与 distribution。
三者都依赖 relevance classifier，不能从“被标成敏感”推出该 token 对能力具有完整因果贡献，也不能阻止
tool/in-context 重新获得能力。Classifier、mask policy、training revision 与 held-out capability evaluation
必须绑定；output policy 和 tool authorization 仍不可删除。该路线保持 `Status: Experimental`。

安全数据闭环还可由当前 policy 生成 adversarial candidates，再由独立 guard / outcome policy 筛选后进入训练。它能把静态红队集扩展到当前模型暴露的 failure frontier，却同时制造 self-confirmation 风险：generator 与 guard 若共享模型家族、prompt 或表示盲点，可能一致地把危险样本标成安全；只保留通过 guard 的样本还会隐藏 false negative。因而 generated sample、generator checkpoint、guard version、policy taxonomy、人工复核切片和最终 deployment gate 必须分开保存。该机制适合作为受控 data augmentation，不能取代 output-time enforcement 或独立 red-team evaluation。

### Policy-as-Data：可更新规则与模型判断必须分开版本化

把安全规则写死在 model weights 或应用代码中，会让 policy 更新分别等待训练与部署；让一个
safeguard model 在运行时读取 policy text，则可以把“当前规则”作为显式输入，对 content 或
action 产生分类/解释。它获得更快的规则迭代和多 policy reuse，却把 policy wording、context
length、prompt injection、reasoning faithfulness 与 fallback 带进 security critical path。

```text
policy artifact + untrusted content
→ safeguard inference
→ typed decision + evidence
→ deterministic authorization / enforcement
```

关键边界是最后一步：model verdict 是 policy-bound sensor，不是 authority。Gateway、tool executor
或 workflow 仍应执行确定性 deny/allow、最小权限和人工升级；policy artifact 也必须有 immutable
version、owner、测试集、生效范围、rollback 与 cache key。静态 classifier 在规则稳定、低延迟或
高可预测性场景仍更合理。gpt-oss-safeguard 是该模式的 Research Preview 案例，其公开评测不能
证明开放权重 safeguard 在所有语言、攻击或本地微调后仍保持同一安全边界。

## 从“文本是否恶意”到“谁获得了行为控制权”

Prompt injection 的困难不只在于恶意内容难分类。检索文档、工具描述或 memory 中的一段中性文本，也可能在模型推理时成为 behavior-guiding instruction。只做入口分类会遗漏这种运行时影响；只看 attention 或模型自述又会把相关性误当成因果和授权。

更完整的纵深防御把三个阶段分开：

```text
retrieval set
→ source/consensus sensor filters suspicious evidence
→ runtime influence locator proposes behavior-guiding spans
→ authority registry adjudicates whether that source may issue instructions
→ step guard checks proposed action before execution
→ deterministic tool policy owns allow / deny / approval
```

这不是三个互相替代的 classifier。Retrieval consensus 依赖 honest-majority 与 representation separation，面对多数污染或可查询 surrogate 会失效；attention-derived locator 是可迁移 sensor，不证明某个 span 在因果上决定了动作；learned step guard 受 synthetic taxonomy、teacher bias、false positive 与 adaptive adversary 限制。它们的收益是把污染入口、推理影响和执行动作分层定位，代价是更多 false reject、版本化 authority registry、额外 latency 与 cross-layer disagreement。

旧的静态规则在强格式、低延迟和已知攻击中仍合理；高风险 action 仍必须由 scope、approval、idempotency 与 sandbox 约束。模型 sensor 可以触发降权、重新检索、询问或人工升级，但不能自行授予来源 authority，也不能成为最终 authorization owner。

### 多 Agent Cascade 需要跨 Channel 的 Influence Graph

逐条扫描 message 或只在最终 action 上做 policy check，在通信拓扑固定、传播链短时简单有效；当一个污染信号经 message、shared memory、delegation 与 tool result 多次改写后，单 channel 告警既无法说明起点，也无法判断哪个 Agent 正在放大影响。运行时可以维护带 revision 的 cross-channel influence graph：各 channel adapter 只提交 observation，causal monitor 关联传播路径并提出 suspect source / edge，security policy 仍独立决定隔离、降权或阻断，不能把统计 attribution 当作 authorization。

这种路径以在线 trace、跨 channel identity 与 attribution 误差换来 cascade 的更早定位；漏记边、共同上游或自适应通信会产生错误因果图，监控本身也可能成为额外延迟与隐私面。低风险、无共享状态或单 Agent 流程仍可使用局部 guard；证据不一致时应保留原 trace、隔离可疑传播并升级人工分析。`arXiv:2605.19240v1` 的 §4.1–4.4 与 §5 只支持其披露的 causal monitoring 与 detection/attribution evaluation，§7 明确其限制；它不证明开放拓扑中的因果完备性或生产阻断效果。

<!-- source-family:SF-2026-ARXIV-2605-19240 -->

## Safety Evaluation 的单位是 Run，不只是 Prompt

单轮 text test 便宜、确定、适合快速 regression；隔离某一 image/audio encoder 的单模态 test 也有助于
定位边界。它们没有失效。但当 policy state 跨 turn 累积，输入又经过 TTS、rendering、codec、vision/OCR
或 provider adapter 转换时，`(prompt, response)` 已不足以标识攻击面。完整 evaluation subject 应是 run：

```text
goal / threat category / strategy revision
+ conversation and attempt history
+ turn / retry / backtrack budget
+ modality sequence and media artifact digests
+ transform / codec / rendering revisions
+ target model, API and provider-policy identity
+ attacker / judge identities and prompts
+ per-turn verdict, stop reason and final outcome
```

从 single-turn text、isolated multimodal 或 multi-turn text，演进到 run-centric multimodal campaign，获得的是
transition-level attribution：哪一次表示变换、反馈或重试之后 policy 发生变化。新增代价包括有害 media 的
access/retention/deletion、campaign resume correctness、cache poisoning、provider drift、judge injection 与更高
成本。只保存最终 attack-success rate 会丢掉这些 state，也无法重放或修复失败路径。

Run-centric 仍不自动给出因果结论。若 single-turn 使用 direct goal，而 multi-turn 同时改变 prompt、history、
sampling 和 backtracking，差异属于完整 workflow，不能单独归因于“多轮压力”。若 modality order 没有随机化、
缺少 same-content paired control，turn 后的变化也不能证明 representation transition 必然破坏 alignment。
Hard/soft 或多级 compliance taxonomy 能保留 partial leakage，却仍需 severity、actionability、false-positive/
negative 与 human disagreement；同一模型同时充当 attacker 与 judge 还会产生相关误差。

因此三种旧设计继续共存：single-turn deterministic suites 做高频回归，isolated-modality tests 定位 encoder/
filter，human red team 探索新语义风险，automated run campaign 扩大 state-transition coverage。任何一项都不应
单独承担 release verdict；第 66 章保存 EvalSpec 与 scorer contract，第 73 章再把证据接入 gate 与 rollback。

### Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate

只评最终 vulnerability answer 能快速比较模型，却会把偶然猜中、未授权 tool use、敏感信息外泄和真正完成证据收集混在一起。对可执行 security agent，更稳妥的 run identity 要冻结 sandbox、工具集合、redaction rule、success predicate 与 grounding check，并逐步保存 proposal、tool receipt 与最终判断；模型只拥有分析与 action proposal，harness 才拥有成功判定和泄漏审查。

完整 trace 提高可复算性，也增加日志敏感性、parser 版本和 benchmark-specific overfitting；固定工具又可能低估真实环境中的适应能力。快速的答案级 suite 仍适合早期筛选，高风险 release 才升级到 trace replay 与人工复核。`arXiv:2605.19722v1` 的 §3–§5 仅在 30 个本地 vulnerability-analysis tasks、固定工具和所列模型上支持该协议，§6 不支持把结果外推为通用 Agent 安全能力或现实攻击成功率。

<!-- source-family:SF-2026-ARXIV-2605-19722 -->

### Containment 不能只看最终是否发生攻击

Run-centric evaluation 还需要把暴露后的 containment 拆成可定位阶段：不可信内容被读取、影响沿 Memory 或 delegation 传播、模型提出高风险 action、policy 授权，以及 executor 实际 commit。只比较最终 attack-success，会把“同样没有恶意提交”误当成相同行为，也可能奖励通过阻断全部合法工作获得的表面安全。

因此 trace 应同时保存 provenance graph、proposal / authorization / commit 与 authorized-tainted utility。它用更高的 parser、policy、scenario 和 normalization 版本管理成本，换取对传播与阻断位置的可追溯判断。未观察到 commit 仍只是受测 scenario 下的证据，不能升级为防御完备证明；第 66 章继续拥有 EvalSpec 与 scorer identity，本章只拥有风险阶段、authority 与 effect boundary。

### CoT Monitor 是 Policy-bound Sensor，不是 Authority

显式 reasoning channel 可以为 monitor 提供比 final answer 更多的 surface signal，但必须分开四个命题：

```text
channel controllability
  模型能否按指令改写 reasoning surface

surface monitorability
  monitor 能否从该 surface 识别某类风险

faithfulness
  surface 是否反映真正影响 action 的 computation

outcome safety
  最终 proposal / action / side effect 是否被阻断或验证
```

模型难以按 prompt 删除关键词、改变格式或隐藏信息，只能削弱一种主动 surface manipulation 路径；它不
证明 CoT 完整、忠实、可解释，也不证明危险 action 不会出现。相反，能够控制 CoT 也可能服务合法压缩、
隐私或格式需求，不能直接等同于欺骗能力。Proxy grader 的关键词、字符串、channel parser、长度、provider
template 与 aggregation 都会影响结果，低 compliance 还可能混合任务难度和 instruction following。

Threat model 还必须包含 attempt opportunity。单次成功率很低，在多次独立尝试、逐次 feedback、更长 token
budget 或更多 tool actions 下，至少一次成功的风险仍会放大。生产应版本化 parser/grader、attempt/feedback
budget 与 action verifier，并把 CoT signal 与 output inspection、least privilege、sandbox、typed authorization、
executable outcome checks 和 incident response 组合。即使 monitor 判断“安全”，它也不能授予工具权限或绕过
确定性 policy；这与前面的 privacy detector、safeguard model 都遵循同一 sensor/authority 分离原则。

### Test-time Training 会创建新的安全 Revision

推理期参数保持只读时，部署前安全验收可以绑定固定 artifact；test-time training 让线上输入持续改变后续行为，原安全结论不再自动继承。Adaptation loop 只能提出 update，独立 safety gate 必须保存 base/adapted revision、触发输入、更新预算与行为差异，并在 commit 前复验，失败时回滚到最近可信 checkpoint。

在线适应获得分布修复能力，却引入累积 guardrail erosion、攻击者投毒与不可复现漂移；无法隔离更新或提供 rollback 时应关闭参数写入，仅使用外部 memory/RAG。arXiv:2605.22984v1 的机制和实验只支持作者 test-time training 设置，不证明其防护覆盖开放输入或长期攻击。

<!-- source-family:SF-2026-ARXIV-2605-22984 -->

## Supply-chain Integrity

### Requirement 也是 Versioned Untrusted Supply-chain Input

当需求来自有权限的内部 maintainer、约束单一，且安全不变量已经固化在模板与测试中时，把 issue 视为可信意图，再用普通 code review 与 SAST 筛查实现风险，是成本较低且合理的旧路径。外部 contributor 或 mixed-trust 来源改变了这个前提：功能、易用性、实现方式或性能取舍等显式要求，可能在功能测试仍通过时压过模型依赖的隐式安全惯例。因此 requirement admission 必须把原始文本、提交主体与来源、revision、受影响资产、显式目标、继承的 security invariants 和允许的 trade-off 一起版本化；requirement 不再只是自然语言入口，而是进入 AI coding pipeline 的不可信供应链 artifact。

控制权不能随 prompt 一并交给 coding model。模型只拥有 code proposal；security policy owner 定义不变量与 exception 规则，CI 以确定性功能测试、安全回归测试和 static analysis 执行检查并生成 receipt，repository owner 审阅 requirement revision、proposal、双重验证结果与 exception 后，才拥有 merge 或 revert authority。若 proposal 同时改写 policy、安全测试或 approved template，这些变化必须进入独立审批，而不能用“测试已通过”自证。这样可以阻止显式 usability objective 静默覆盖安全约束，并把每次合并追溯到授权它的 requirement revision；代价是规范与测试维护、额外 CI 延迟、false reject，以及 requirement、policy 与 tests 之间的漂移。

这条链仍可能因安全假设不完整、Analyzer/Judge 或静态规则盲区、动态 payload 未覆盖、模型同时迎合代码与测试，或受 benchmark 过拟合而失效。低风险且来源可信的内部改动可继续与普通 review/SAST 路径共存；外部或高风险需求在不变量无法表达、验证结果冲突或 provenance 缺失时，应 fail closed 到人工 security review、确定性测试与 static analysis，并优先回退 approved secure template，而不是降低 merge gate。`arXiv:2605.10133v1` 的 §3.1–§4.3、§5.1–§5.4 与 Appendix B.1/E 只支持其 75 个场景、25 个 CWE、四个模型及已披露攻击生成与验证协议中的 functionality-preserving security regression；它不证明所有请求都恶意、所有 coding model 都会失败、内部因果机制已确定，或上述 policy/CI 防线有效，且当时不可获得不可变的 repository、dataset 与 payload revision。

<!-- source-family:SF-2026-ARXIV-2605-10133 -->

### Optimization Pass 也是新的 Security Revision

可信 base weights 经过量化、剪枝或其他 optimization pass 后，旧路径直接复用源模型的安全结论在变换可证明等价、且威胁模型不关心数值扰动时仍然合理；一旦变换可能重新暴露 trigger behavior，目标 artifact 就必须拥有独立 revision。Optimizer 与 Serving pipeline 只拥有变换 proposal，独立 integrity gate 才能比较变换前后的触发行为并决定 release。

这条 gate 增加了双版本测试、触发集治理和误报成本，也可能遗漏未知 trigger；失败时应回退未优化 artifact 或阻止发布，而不是用平均质量指标覆盖安全回归。`arXiv:2605.20641v1` 的 §3 机制与 §4 实验只支持其优化后 trigger re-emergence 合同；Appendix C 不证明所有量化、剪枝或模型家族都会复现同一攻击。

<!-- source-family:SF-2026-ARXIV-2605-20641 -->

### 可组合 Prompt 也是 Versioned Supply-chain Artifact

Adapter、model weight 与 executable package 容易被识别为供应链对象；可热插拔 prompt、soft prompt 或视觉 prompt 往往被当作无害配置。在 prompt 只做静态模板且无外部来源时，这个简化合理；当 prompt component 可下载、拼接并在运行时改变模型功能时，它已经拥有 artifact identity、producer、依赖、compatibility 与 activation scope，必须经过 admission、签名与可回滚版本管理。

动态 prompt 的风险不只来自单项恶意内容，还来自多个看似正常 component 的 functional fusion。扫描单文件或复用 adapter 安全结论会漏掉组合行为；组合测试又带来状态空间膨胀和 false positive。低权限、本地固定 prompt 仍可采用较轻审查；跨租户 marketplace 或高权限 Agent 应 fail closed 到已批准组合。`arXiv:2605.19478v1` 的 §4–§7 只支持其 ViT/VPT threat model、dynamic-prompt fusion 与 pruning/transfer experiments，§8 不证明所有文本 prompt、adapter 或生产生态都同样可攻击。

<!-- source-family:SF-2026-ARXIV-2605-19478 -->

### Embedding 也是可执行数据供应链的一部分

<!-- semantic-body-binding:SF-VECTORSMUGGLE-STEGANOGRAPHIC-EXFILTRATION-IN-EMBEDDING-STORES-AND-A-CRYP:start -->
向量入库若只校验文本与维度，拥有 ingestion 写权限的主体可以在保持近邻行为大致正常的同时，把 payload 编码进 embedding 的扰动、旋转、缩放或分片。因而 provenance 要绑定 source content、encoder revision、canonical embedding digest 与 index admission；查询和导出也要按 tenant/purpose 限制。Cryptographic binding 能发现未授权 post-embedding mutation，却不证明 encoder 本身可信，也不覆盖合法源中携带的恶意语义。代价是重编码、签名和迁移成本；封闭、只读 index 仍可用较简单的构建期校验。
<!-- semantic-body-binding:SF-VECTORSMUGGLE-STEGANOGRAPHIC-EXFILTRATION-IN-EMBEDDING-STORES-AND-A-CRYP:end -->

Artifact contract 应包含：

```text
source revision
builder identity
build parameters
materials/dependencies
artifact digest
signature / attestation
verification policy
```

SLSA 将 provenance 定义为可验证的“何时、何地、如何由谁生产”。平台可以要求 image、runtime engine 与模型 bundle 在 admission/load 前验证 digest 和 attestations。

签名只证明某身份签过，不证明内容安全；仍需 vulnerability scan、policy review、sandbox 和 runtime restrictions。

### 已披露漏洞要沿 Design Lineage 搜索变体

按 repository 或 CVE 精确字符串修复，在实现独立、复用少时成本最低；AI infrastructure 常复制相似 loader、conversion、serving 与 agent workflow，同一设计缺陷可能以不同 API、文件名和数据流重新出现。安全 owner 因而要保存 vulnerability 的 reference behavior、关键 data/control flow 与 affected preconditions，再在相关 repository lineage 中做 variant search；scanner 只产生候选，代码 owner 与可执行 test 才能确认修复。

这种跨仓库检查扩大召回，却会引入相似设计的误报、版本漂移与维护成本；没有共享 lineage 或语义条件不成立时，精确 dependency scan 仍更可靠。`arXiv:2605.20051v1` 的 §3–§5 只支持其 reference-driven detection 与受测 AI-infra repositories，§6 明确 false-positive boundary；它不证明相似代码一定共享漏洞，也不证明扫描已经覆盖私有 fork。

<!-- source-family:SF-2026-ARXIV-2605-20051 -->

供应链事件还说明，artifact signing 只是路径中的一个 checkpoint。攻击可能从 upstream package 进入 developer
endpoint，再取得 repository credential、污染 source/release，最后迫使客户端升级或撤销证书。恢复 contract 应覆盖：

```text
dependency / developer endpoint compromise
→ credential and repository exposure
→ artifact and signature scope assessment
→ revoke / rotate / rebuild from trusted materials
→ forced client upgrade or deployment quarantine
→ post-incident provenance and residual-risk review
```

只删除恶意 package 不能收回已泄漏 credential；只旋转 signing certificate 也不能证明旧客户端已退出。
OpenAI 对 TanStack npm incident 的公开响应为这条 end-to-end path 提供官方案例，但公开页面不是完整 forensic
report，因此不能用于推断全部 root cause、受影响人口或控制有效性。

生成内容的 provenance 也不能由单一 watermark 承担。可剥离的标准 metadata 适合声明 producer、edit chain
与签名；较耐变换的 embedded signal 可以在 metadata 丢失后提供弱关联；public verifier 再把 signal 映射到
可解释 verdict：

```text
signed content metadata
+ transformation-robust embedded signal
→ public verification with model/signal revision
→ positive, negative or inconclusive evidence
```

三者是互补层，不是重复保险。Metadata 可被剥离，watermark 有 false positive/negative、压缩与跨模型迁移边界；
尤其 negative result 只说明当前 verifier 未检测到已知 signal，不能证明内容不是 AI 生成。OpenAI 的
C2PA/SynthID layered provenance 是官方工程案例，不构成对所有生成器、编辑链或对抗变换的完整认证。

<!-- source-family:SF-2026-ARXIV-2605-28632 -->

Watermark 的信任根还早于输出统计：若生成时的 entropy source、PRNG/seed state 或 sampling hook 被操纵，攻击者可能保持甚至增强表面 watermark，同时改变其真实 provenance。因而发布 artifact 必须绑定并尽可能 attest PRNG implementation、seed derivation、sampling configuration 与 key scope，output detector 只验证该配置下的统计证据，不能独自证明生成链未被篡改。

这会提高密钥管理、可复现性和硬件/runtime 绑定成本；完全公开 seed 又可能削弱抗移除能力。低风险内容仍可把 watermark 当辅助信号，高风险 provenance 需要签名 metadata、artifact identity 与执行 attestation 共同承担。exact-v1 的 seed-layer attack 只证明该攻击面存在，不证明所有 watermark scheme 或生产 sampler 同样易受影响。

当模型服务跨不可信 host、accelerator 或网络执行时，artifact 签名也不够：调用方还需要确认“指定 model/
runtime 在允许环境中处理了这个 request，并返回了与 request 绑定的结果”。可以把它建模为概率审计而不是
每 token 全量验证：

```text
request digest + model/runtime identity + policy epoch
→ execution commitment / attested boundary
→ sampled challenge or consistency evidence
→ typed audit verdict with false-accept / false-reject budget
```

TEE/attestation 只保护声明的 boundary，不证明模型质量、host I/O、side effect 或所有 accelerator computation；
sampling 又以审计成本换 detection probability。CPU-only trusted boundary、commitment state、nonce/replay
protection 与 failure policy 都必须显式。IMMACULATE 的作者实验提供了 service-integrity 机制证据，但其 threat
model、硬件条件与未公开生产 artifact 不支持通用 latency 或完整性保证。

### Intermediate-state Canary 是 Integrity Sensor，不是 Eviction Authority

Artifact 签名和 final-output check 能证明加载对象或发现最终错误，却不能在不可信 pipeline stage 之间定位哪一段改写了状态。一个 challenge-response 分支是由 verifier 持有 versioned canary 与受信 reference activation，在 live fp16 执行时比较每个 shard 的 intermediate state，并按校准 noise envelope 输出 suspect evidence。

这样把完整性观测推进到状态边界，但 detector 仍只是 sensor：它不能独自证明恶意意图，也不能越权驱逐 peer；eviction、retry 或冗余执行仍由 policy gate、attestation 与 failure budget 决定。reference 预计算与保存增加存储和版本成本，真实异构 nondeterminism 未必服从模拟噪声，adaptive attacker 还可能识别 canary 或将扰动压到检测阈值下。

稳定可信集群中，端到端校验可能更便宜；不可信协作环境则需要 canary、redundancy、attestation 与抽样审计共存。

## 从 Trace 检查到受限状态空间验证

### Conversation Continuation 必须先验证 Grounding State

<!-- semantic-body-binding:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:start -->
多轮对话中，后续生成可能在过期前提、未确认工具结果或已撤销事实上继续推导。Runtime verifier 可把可引用 claims、observation revision 与 unresolved contradictions 维护为有界 grounding state，在 continuation 前线性检查依赖是否仍成立。它能阻止部分 stale-premise propagation，却依赖抽取完整性，也不能证明新答案为真；未解析自然语言、开放世界事实或冲突无法消解时应 abstain、检索或人工升级。小规模场景结果不能外推为通用事实验证率。
<!-- semantic-body-binding:SF-GROUNDED-CONTINUATION-A-LINEAR-TIME-RUNTIME-VERIFIER-FOR-LLM-CONVERSATIO:end -->

Trace test 能证明某次运行没有触发已知坏路径，不能证明所有可达状态都满足 temporal safety。若 Agent 的工具、
schema 与状态转移可以被有限化，可把 deployment 写成 relational transition system，用 temporal property 描述
“审批前不得提交”“撤销后凭据不可再用”等不变量，再对 quotient state space 做 model checking。

```text
versioned tool semantics + bounded operational state
→ canonical state identity / symmetry reduction
→ temporal safety property
→ reachable-state verification
→ runtime monitor for assumptions that may drift
```

形式证明的强度来自假设，而不是数学符号本身。Bounded active domain、identifier-renaming equivariance、有限 tool
semantics 与可枚举 transition 一旦被 schema evolution、外部副作用、概率 policy 或无限对象打破，证明便不覆盖真实
系统。Formal Verification of Agentic Systems 提供这一受限分支的理论证据，不证明任意 LLM Agent 可验证；trace、
simulation、canary 与 incident evidence 因而继续存在。

## 从 Scalar Confidence 到 Safe-commit Certificate

即使状态空间无法完整验证，高风险 action 也不应只凭一个“置信度”提交。运行时可以从 observation、Memory 与 tool
evidence 构造一组仍 plausible 的 worlds；只有 action 在全部 retained worlds 中满足 safety predicate 时才颁发
commit certificate。若没有可认证 action，先选择低副作用 probe 缩小集合，预算耗尽后 abstain、escalate 或 defer：

```text
authorized evidence → plausible-world support
→ all-world safety check
→ certified commit | bounded probe | defer / human approval
```

Certificate 不替代 IAM、sandbox、审批或 compensation。它依赖可校准 support、准确 safety map 与可枚举 outcome；
world/action 数增长会放大成本，stale 或 poisoned memory 也可能使 support 错误收缩。SafeCommit 的小型 simulator
只支持该控制结构，不证明生产规模与 coverage。规则清晰时 deterministic policy 更强；无法列举 plausible worlds
或副作用不可逆时，human approval 仍是必要旧分支。

## 模型文件与训练代码是不可信输入

某些 serialization format 加载时可执行代码；remote code、custom ops 和 notebook image 都可能突破数据边界。平台应：

- 优先使用数据型安全格式；
- 将转换放在隔离 builder；
- 禁止默认执行 remote code；
- 最小化 service account 与 network egress；
- 扫描依赖并固定 digest；
- 对高风险 workload 使用 sandbox/专用节点。

“模型来自内部 bucket”不等于可信，内部 account 也可能被滥用。

## Prompt Injection 与 Tool Boundary

Prompt injection 的根因不是“模型没有听 system prompt”，而是系统把不可信内容与高权限指令放入同一个模型上下文，再把输出当作 action。

安全边界应位于工具执行器：

```text
model proposes action
→ typed schema validation
→ policy and authorization
→ parameter/content validation
→ optional human approval
→ least-privileged execution
→ result filtering and audit
```

第 78 章会展开 Tool Calling 机制；本章只冻结平台控制：模型不能授予自己权限，检索内容不能改变 authorization，敏感操作必须有独立 policy decision。

### Search Query 本身也是 Public Egress Action

传统 research Agent 常把最终回答当作唯一输出面：本地文档进入 Context 后，模型可以先生成公开 Web query，最后再由
response filter 删除敏感文字。约束变化在于 query 已经离开 private boundary；即使最终答案干净，关键词、实体组合或
多跳检索顺序也可能泄露本地 evidence。Query planner 因而只能提出带 provenance 的 search intent，privacy/egress
owner 在发送前按 principal、document sensitivity、query digest 和目的做 admission，必要时 redact、改写、转私有索引、
请求审批或 fail closed；search provider 的 receipt 记录实际公开的内容，不能由最后一层 moderation 代替。

前置 gate 用检索召回率、额外 latency 与 false reject 换取可控制的公开出口；主要 failure mode 是漏掉组合式或跨多次查询的泄漏，
过度改写又会使任务不可答。纯公开资料、无 private context 或完全私有的 search backend 仍可使用较简单路径，但混合
private/public research 必须累计 query-family exposure，而不是逐条孤立判断。`arXiv:2605.30727v1` 的 §6 与 Appendix C
只支持 MosaicLeaks 的 1,001 个披露 multi-hop tasks 和所测 Agent 的 query leakage；§8 不证明所有 deep-research Agent
都会以相同比例泄漏，也不证明单一过滤策略足以消除风险。

<!-- source-family:SF-2026-ARXIV-2605-30727 -->

<!-- source-family:SF-2026-ARXIV-2605-26542 -->

逐次 tool call 都通过权限检查，仍不代表跨调用链安全：第一步合法读取出的敏感 value，可能在第二步被送进同样合法但不应接收它的 sink，形成 permission laundering。更强的 contract 把 authority 绑定到数据 value、允许的 transformation 与 sink，并规定跨调用只能单调收紧，不能由中间 Agent 重新扩大。Policy engine 拥有授权与衰减规则，tool runtime 只执行经过 capability/label 检查的调用，workflow trace 保存 authority provenance。

这种 information-flow enforcement 用 label propagation、跨工具 schema 和拒绝率换来端到端约束；隐式通道、错误标注和过度保守的衰减仍会造成泄露或阻断。工具少、数据不敏感且调用链固定时，传统 per-call RBAC 仍更简单；一旦数据会跨 Agent、跨存储与外部 egress 流动，就不能把每个局部合法推导成整体合法。

<!-- source-family:SF-2026-ARXIV-2605-26754 -->

RAG 的另一条边界问题是让未信任文档同时拥有“提供事实”和“影响合成指令”的权力。直接把原文拼进 prompt 在封闭知识库中最便宜，却会让注入文本进入与系统指令相同的语言通道。可审计的隔离路径先在低权限域抽取 atomic claim、来源位置与类型，再由 deterministic policy/validator 过滤；高权限合成器只消费通过审计的 claims，不消费原始指令性 prose。

这个分层牺牲原文细节、召回率和一次调用成本，并把 claim extractor/validator 变成新的攻击面；高风险任务还要保留原文隔离查看与人工升级。可信、小规模文档集可继续直接检索，但跨租户、开放 Web 或能触发外部动作时，应把 provenance-bearing claim boundary 当作最小安全单元，而不是依赖模型自行忽略恶意文本。

### Pre-guard 可以前移，但最终 Authority 不能前移给 Draft Model

在 target model 生成后再做 moderation，语义信息最完整，却已经支付全部推理成本，也可能让流式输出提前暴露。利用 jailbreak transferability 的 pre-guard 可以先由较小 draft/safeguard model 检查 prompt，并在高风险时阻断或升级；它改变的是 sensor 的时机与成本，不改变 target gateway 对最终 admission 的所有权。

前移检测减少部分无效 target inference，但新增 model mismatch、transfer failure、对抗绕过与 false reject；draft verdict 不能证明 target 一定安全或危险。低流量、高歧义或需要完整 response context 的场景仍应保留 post-generation guard；高风险 action 继续由 deterministic policy 与 approval 控制。`arXiv:2605.19321v1` 的 §3 与 §6 只支持其 draft-model pre-guard、jailbreak 与 latency experiments，§7 不证明跨模型 transfer 在开放攻击中稳定，也不允许把作者延迟结果外推到其他硬件或并发条件。

<!-- source-family:SF-2026-ARXIV-2605-19321 -->

RAG 还扩大了 privacy unit：攻击者不一定要恢复文档内容，也可能通过黑盒查询判断某条记录是否属于检索 corpus。该结论不能只绑定 generator model；retriever、index revision、chunking、reranker、prompt assembly、query budget 和返回的 citation/score 共同定义攻击协议。因而 corpus membership audit 应以完整 retriever–generator path 为对象，折叠重复查询，按 tenant/record privacy unit 评估，并把未披露字段写成 unknown。

只做生成模型 membership test 会漏掉 retrieval score 与引用信号，只关闭分数又可能由输出差异泄漏。限制查询、最小化返回、访问控制、分租户 index 与必要时的 DP 是分层防线；它们用可观测性和 utility 换较小泄漏面，但不产生零泄漏保证。公开 corpus、低敏感检索或无需黑盒暴露的内部批处理仍可采用更简单的访问控制与审计。

<!-- source-family:SF-EMIA-RAG-CORPUS-MEMBERSHIP-INFERENCE -->

同一个 physical index 被多个 account 共享时，privacy unit 还不能停在单账户 query budget。若攻击者能够让多个账户对同一记录发起相关查询，再把 score、citation 或输出差异合并，逐账户均未越界仍可能形成跨账户 membership evidence。Index owner 必须记录 shared-index identity 与 collusion group hypothesis，privacy accountant 按 record / tenant policy 合并相关 exposure；authorization owner 仍先过滤候选，不能由 ranker 自行决定谁可联合观察。

<!-- source-family:SF-2026-ARXIV-2605-27825 -->

Agent memory 又把 membership privacy 从静态 corpus 扩展为运行时状态：同一事实可能被多轮压缩、合并并在后续 query 中反复暴露，攻击者还可用相关 probe 聚合弱信号。审计必须绑定 memory revision、black/gray/white-box access、query-family identity 与相关性假设，并把 parametric prior 与 memory-induced response delta 分开；否则“模型本来就知道”会被误写成记忆泄漏，反之亦然。

这类审计用更多对照查询、隐私预算和状态快照换取可定位性，也会再次消耗敏感状态并产生 false positive。公开、短期、无个体信息的 scratch memory 可继续使用普通访问控制；持久化、跨 session 或用户可识别 memory 则应成为独立 privacy unit。exact-v1 只支持其声明的攻击协议和模型/数据设置，不证明任意 Agent memory 都可被同样恢复。

跨账户 accounting 降低组合泄漏，却需要 identity linkage、相关性假设和更严格 rate limit，也可能误伤合法团队协作。真正物理隔离、公开 corpus 或无可观察检索信号时，单账户审计仍可成立。`arXiv:2605.19847v1` 的 §2–§5 只支持其 same-index collusion threat model、privacy audit 与 retrieval protocol，§7.1 明确没有覆盖 generation；它不证明所有共享 RAG 都已泄漏，也不提供零泄漏保证。

<!-- source-family:SF-2026-ARXIV-2605-19847 -->

Live Agent 还会跨 email、chat、filesystem、shell、cron 和 Memory 重建“谁在说话、什么是规则、动作是否已经
发生”。自然语言 display name、对话 persona 或 self-report 都不能承担这三种事实：

```text
authenticated principal and delegated scope
+ immutable policy / instruction generation
+ authoritative postcondition from the effect-owning service
```

外部内容进入 Context 后仍是 untrusted data；模型把它写进 mutable memory/instructions，也不能使其升级为 policy。
同理，Agent 声称“邮件已发送”必须由邮件服务 receipt/outcome 证实。更强 authentication、least privilege、
approval 与 typed audience/resource 会增加交互和降低自治流畅度，但高权限 persistent Agent 不能用便利性换掉这些
边界。Agents of Chaos 只证明相应 failure mode 可在其开放式高权限 live lab 出现，不提供模型总体攻击率，也不能
把运行中配置和人工干预归因成 foundation-model 单一缺陷。

<!-- source-family:SF-2026-ARXIV-2605-28201 -->

交互结束也不是 prompt injection 的自然终点。攻击内容一旦被写入 session context、长期 memory 或可复用 skill，可能在之后的良性 query 才触发；只做当前 response moderation 会把 dormant payload 当成已消失。持久状态因此必须在写入时保存 origin、trust/taint 与 policy generation，在每次读取或执行前按当前 principal、工具权限和目的重新验证，过期或来源不明时 quarantine、降权或删除。

双时点检查增加 metadata、读放大和误拒绝，也无法证明模型不会从看似无害内容中重新推导恶意行为。无持久状态、只读会话仍可把边界放在一次请求；跨会话 Agent 则必须让 state owner 而非生成模型拥有 admission 与撤销。作者实验只证明披露 persistence path 中的延迟触发，不给出所有 memory/skill runtime 的通用攻击率。

### Memory Origin Confusion：Reasoning Claim 低于 Effect Receipt

Memory 还会把不可信内容包装成“过去已经推理过的内部经验”。一条 remembered completion claim 即使包含完整
reasoning，也不等于 action 已真实发生；多个从同一伪造 memory 派生的 Agent 结论，也不是多份独立证据。
高风险执行前必须回到 effect owner：

```text
remembered reasoning / completion claim
→ dereference source, tool and effect receipt
→ collapse descendants sharing the same provenance family
→ validate current principal, policy and exact action digest
→ execute or accept postcondition only from the effect-owning service
```

Lexical filter、reasoning-consistency guard 或 model judge 可以作为 detection sensor，却不拥有 truth authority。
它们可能降低某类 forged-reasoning attack 的命中率，但无法修复已被污染的 authoritative state，也不能替代
typed effect receipt。该路线增加 provenance graph、receipt retention 与 effect-time latency；低风险 advisory
memory 可继续使用较轻检查，高权限或不可逆 action 则必须 fail closed、abstain 或请求人工确认。

现有作者实验支持具体 memory-origin confusion 与同源放大 failure mode，不覆盖 system prompt/weights compromise、
multi-Agent 长链传播或真实生产 EHR 风险；没有公开 artifact 也限制独立复现。因此正文只吸收
`reasoning claim < authoritative effect receipt` 与 lineage collapse 的安全合同。

### Shared Memory 必须同时通过 Utility、ACL 与 Forgetting Gate

单用户 Memory 只优化“以后能否找回有用信息”尚可成立；多 principal deployment 中，同一 memory item 还要
回答谁可见、授权是否已变化、删除后哪些 derived/index/cache 副本仍存活。把 retrieval relevance 当作唯一
score，会让高相关但越权的内容进入 Context；只从主 store 删除，又可能被 embedding index、summary、backup
或历史 response 恢复。

```text
memory item + source principal / purpose / consent
→ ACL-filtered candidate set
→ utility ranking inside authorized scope
→ write / supersede / forget event
→ delete-chain closure across derived replicas
→ leak, utility and recovery evidence
```

Authorization owner 必须先于 ranker 缩小候选域，Memory lifecycle owner 记录 delete/supersession，index/cache
owners 回报 propagation，audit 只验证证据而不复活已删除内容。ACL-aware retrieval 可能牺牲 recall，active
forgetting 又与 incident recovery 和合规留存冲突；两者必须由 purpose-specific policy 解决。GateMem 的作者
benchmark 揭示 utility-only memory 的这一缺口，但自动 judge 与 synthetic principals 不证明现实法律删除或
所有隐式泄漏已覆盖。

### Agent 自己的 Instruction、Config 与 Memory 也是受保护资产

Self-hosted Agent 往往能合法读写自己的 workspace；传统 file permission 可以阻止陌生主体，却无法判断同一
Agent 的合法 syscall 是否正在破坏 instruction、configuration 或 durable memory。安全面因而要从“谁能写”
扩展到“这次写是否符合当前 workload 和 semantic intent”：

```text
stable self-state cells → immutable / least-writable policy
mutable memory cells → workload-conditioned telemetry and anomaly evidence
high-risk mutation → semantic authorization / approval
all durable cells → versioned backup, recovery and post-restore verification
```

OS telemetry 只能看到操作与时序，不拥有 Agent intent；semantic detector 也可能把正常自修改误报为攻击。
某些 mutation 在系统调用层与正常行为不可区分，必须依赖更高层 workflow invariant、human approval 或恢复点。
静态 ACL 仍适合 instruction/config 等低变更层，动态检测只用于确实需要写入的层。Self-State Attacks 的论文
提供 threat matrix 与受控 traces，不证明其 detector 覆盖生产 workload，也不允许 Memory backup 绕过删除政策。

#### Harness Backdoor 把单次写入变成跨 Run 控制状态

当前 run 内检查 prompt、tool call 与 workspace mutation，在会话结束即清空、配置不可写时边界清楚；可持久化 harness
允许一次良性任务把 payload 写入 instruction、config、hook 或 memory，后续 run 才在特定 trigger 下接管行为。防线因此
不能只判断“这次写是否合法”，还要为每个 durable control cell 保存 writer principal、source provenance、content digest、
policy generation、activation predicate 与生命周期，并在 load/trigger 前重新 admission。State owner 拥有 publish、quarantine、
revocation 与 rollback；Agent 只能提出 mutation，不能凭后续运行中的自我解释让旧写入升级为可信 policy。

这条跨 run provenance chain 用 registry、扫描、canary 与恢复点成本换取对 dormant control state 的可定位性；signature scan
会漏掉语义触发器，semantic detector 又可能误报正常自动化，备份还必须服从删除与 tenant isolation。不可变 harness、
ephemeral sandbox 或每次从 signed image 重建时，旧的启动完整性路径仍更简单；允许 self-modification 时则要在异常触发后
能撤销整个 write lineage。`arXiv:2605.31042v1` 的 §3.1 与 §4 只支持 ClawTrojan 所定义的 local harness、multi-step
trojan benchmark 与攻击链；§7/Limitations 不证明其检测覆盖生产 workload，也不提供所有 agent runtime 的攻击率。

<!-- source-family:SF-2026-ARXIV-2605-31042 -->

受保护对象还包括“从行为可重建”的 skill。即使 prompt、源码和 artifact 从未直接泄露，攻击者也可能通过受控任务
和输出反馈逼近隐藏策略。因而保密合同要同时约束 artifact access 与 behavioral query surface：按 principal/task 限制
调用范围、记录 query budget、检测 canary/重复探测，并对导出的替代 artifact 单独治理。它用可用性与调试自由换取较低
behavioral leakage；开放公共能力或低价值 skill 不值得承担同等限制。受限实验只证明攻击面存在，不能把黑盒输出相似度
自动认定为源码、权重或完整能力被复制。

### Canonical Action 与 Effect-time Authorization

IAM/RBAC 定义 principal 能做什么，gateway 控制入口，tool-local validation 检查业务状态，sandbox 限制
capability；这些边界都继续成立。Agent 通过不同 protocol/framework、retry 和并发产生效果相同但语法不同
的 action 后，还需要一个位于真实副作用之前的共同 identity 与 authorization gate：

```text
untrusted model intent
→ canonical typed action: actor / target / operation / resource / parameters
→ digest action and bind policy version + authoritative state digest
→ PERMIT | DEFER | DENY
→ signed, short-lived or single-use decision artifact
→ executor verifies exact action digest immediately before effect
→ record outcome / compensation separately
```

Canonicalizer 只规范 schema 内的 action，不证明它忠实表达 latent intent 或现实后果；policy owner 拥有规则，
authoritative service 提供 state，governor 拥有 decision ledger，executor 只能消费与实际 action digest 匹配的
有效 artifact。Policy/state 变化、过期、撤销、重复 single-use 或 governor timeout 必须重新评估、defer 或
fail closed。Authorization record 证明“当时为何允许”，不等于远端 tool 已 commit，也不替代 outcome、
reconciliation 和 compensation evidence。

该层新增 schema evolution、semantic alias/collision、TOCTOU、key rotation、revocation propagation、ledger
hotspot 和 control-plane availability。直接 tool-local authorization 在单一协议、小系统或状态变化极快时
仍更简单；跨 region exactly-once 也不能由 signed decision artifact 自动获得。当前论文只有 synthetic 单机
harness、无公开 artifact，故此机制保持 `Status: Emerging`，正文不采纳其 latency 或 coverage 数字。

<!-- semantic-body-binding:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:start -->
支付协议把这条链再延伸到异步结算：HTTP 请求完成授权不等于链上付款已经 final，链上 receipt 也不必然与
原始 action、resource 和 response 唯一绑定。若授权、请求 digest、payer/payee、amount、nonce、expiry、
settlement status 与最终副作用分属不同组件，重放、错绑和“已服务未付款 / 已付款未服务”都会落在组件缝隙。
因此 payment executor 必须在 effect-time 验证同一 canonical action identity，并把 service outcome 与 settlement
receipt 分别记录、最终 reconciliation。同步、低价值且由单一可信 provider 结算时，简单 request-local payment
仍可成立；跨链或外部 settlement 则以更高延迟、补偿状态和争议处理换取开放性。受限攻击实验只证明这些边界
可能被利用，不证明所有实现均存在同样漏洞。
<!-- semantic-body-binding:SF-FIVE-ATTACKS-ON-X402-AGENTIC-PAYMENT-PROTOCOL:end -->

### 局部合理动作会累积成有害轨迹

<!-- semantic-body-binding:SF-FINDING-THE-WEAKEST-LINK-ADVERSARIAL-ATTACK-AGAINST-MULTI-AGENT-COMMUNIC:start -->
Multi-Agent policy 即使每个节点健壮，也可能被单个关键 message、agent 或 timestep 的小扰动击穿。Jacobian/gradient 分析可定位高敏感通信边，供 red-team 与 isolation proposal 使用；它是 white-box sensor，不是生产攻击概率或自动封禁依据。系统应绑定 message provenance、认证、rate/shape limits 和 outcome monitor；误差相关或 access 不足时回退确定性 schema、冗余 channel 与最小委派。
<!-- semantic-body-binding:SF-FINDING-THE-WEAKEST-LINK-ADVERSARIAL-ATTACK-AGAINST-MULTI-AGENT-COMMUNIC:end -->

Computer-use Agent 的风险经常不在单个 prompt 或单次 tool call：读取、筛选、组合、上传等动作各自可能合理，
组合后才跨越 harm boundary。安全系统因此需要把 threat category、user authority、environment snapshot、每次
canonical action/effect 与最终 side effect 串成 sequence-level evidence：

```text
prompt / intent sensor
→ action-level policy check
→ cumulative effect state
→ trajectory-level harm verifier
→ stop / approval / compensation / incident record
```

这不会淘汰 prompt guard 和 model refusal；它们仍是廉价前置过滤。新增的 trajectory judge 也不能单独成为
authority：同源 judge、无 benign calibration、缺少 deterministic side-effect verifier 时，可能把复杂但正常的
automation 误报为攻击，或漏掉跨步骤组合风险。完整 trajectory retention 还扩大隐私和敏感 payload 暴露面。
AgentHazard 的作者 benchmark 支持“harm 的评估单位应扩展到 run”，但不提供任意生产环境的通用 incident rate。

循环 Agent 还要求风险状态跨 iteration 保留。每轮只审查当前 prompt/action 会让早期污染、反复试探或逐步 capability
accumulation 在 reset 后消失；更强的 harness 应维护不可由 Agent 自行清零的 trajectory risk state，并让 decay、session
boundary、人工解除和恢复成为显式 policy。Non-decaying state 减少“洗白历史”的空间，却会累积误报、阻塞长期任务并扩大
敏感 trace 留存；低风险短任务仍可使用有界窗口。Learned monitor 只提供 sensor evidence，最终 stop/permit 仍由独立 policy
与 executor 拥有。

多 Agent 委派把这条链再推进一步：有害目标可能被拆成多个局部合理的子任务，单节点重新做 prompt
classification 仍看不见跨节点累积的语义。运行时需要把 source、delegation、memory write 与 irreversible
sink 组织成带 provenance 的信息流，在 sink 前重建跨节点上下文，再由确定性 policy 决定是否允许 commit。
这用额外图状态、标注误差和重建延迟换取跨委派风险可见性；semantic taint 仍只是 sensor input，不替代
capability isolation，也不能授权 LLM 自己拥有最终安全判决。

### Permission Graph 是授权 Proposal，确定性 Authorizer 才拥有 Commit

<!-- semantic-body-binding:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:start -->
静态角色可以直接授予长期权限；governed mutation 跨多个 sovereign domain 时，更严格的分支由签名 proposal、policy facts、approval、environment attestation 与前序 outcome 共同推导一次 execution authority。Verifier 只对完整 artifact graph 计算 allow/deny，executor 仅消费与 action digest 匹配的短期 capability。收益是把权限来源变成可复核证明，代价是 proof graph、key lifecycle、revocation 和 control-plane availability；证明只覆盖已编码规则，不证明现实后果。单域稳定操作仍可使用传统 RBAC，缺 artifact 或规则冲突时必须 defer/fail closed。
<!-- semantic-body-binding:SF-VERIFIABLE-AGENTIC-INFRASTRUCTURE-PROOF-DERIVED-AUTHORIZATION-FOR-SOVERE:end -->

静态 RBAC 在主体、资源和操作集合稳定时最容易审计；Agent 动态组合工具与多步任务后，权限需求往往先以自然语言
出现。直接让模型输出 allow/deny 看似省去 policy engineering，却把解释、证据和最终授权交给同一概率组件。更安全的
分层是把模型限制在 policy compilation 的 proposal 阶段：

```text
task intent + tool/resource metadata
→ typed permission intermediate representation
→ evidence-backed principal/resource/action graph
→ deterministic policy or SMT authorizer
→ gateway commit / deny / require approval
```

图和 IR 让缺失 binding、冲突 policy 与权限传播可以被检查，但它们不是权限真值；模型漏掉的约束、过期 evidence、
solver 不可用和 gateway 绕行都会产生新的 failure mode。低风险、固定工具集继续适合手写 least-privilege policy；
动态工作流可以使用模型辅助生成候选图，但 authorizer 必须 fail closed、保存 policy/evidence revision，并让实际 executor
只接受带授权 receipt 的 canonical action。

### 从 Host-local Sensor 到独立基础设施安全面

Host agent 容易部署、能理解 application semantics，在 host 仍可信时是合理起点；一旦 host 本身成为攻击对象，
sensor、telemetry 与 enforcement 共享同一 failure domain，攻击者可能同时篡改行为和证据。DPU/独立基础设施处理器
可以把部分观测与 deterministic enforcement 移出 host：

```text
attested infrastructure sensor
→ bounded DMA / network / storage observation
→ versioned deterministic policy
→ alert or enforce outside the host
→ correlate with host and application evidence
```

隔离面不等于可信终点。DMA scope、kernel-layout decoder、DPU firmware/root of trust、policy synchronization、
forensic retention 与 fail-open/fail-closed 都需要独立治理；DPU compromise 还会形成更大的 correlated blast radius。
Host EDR 继续拥有 application semantics，外置 plane 提供 tamper resistance，二者应联合而非替代。NVIDIA DOCA
材料证明了产品接口和声明的分层，但没有证明不可绕过，也没有给出可外推的性能或 false-positive contract。

### 分布式训练把检测对象从单机流量扩展为跨时空谱系

以单台主机、单个机房或大规模同步集群为检测单元，在训练集中且流量持续时成本低、信号也直接；低频同步和
pipeline-parallel DiLoCo 一类机制却允许多个低于单点阈值的节点长期协同，使任何一个 sensor 都像普通 workload。
治理证据面因此要聚合 chip/cluster identity、注册关系、时间窗口、同步谱系与供应链记录，再对跨节点关联行为做
阈值判断。Host 与 network detector 只是传感器；独立 governance plane 拥有 identity correlation、ledger 与告警
状态，模型或作业不能用自报用途覆盖这些记录。

这种聚合可缩小 split-cluster blind spot，但会增加身份关联、隐私、留存、误报和执法成本；带宽模式也可能被规避，
从模拟或特定训练机制观察到的信号不能外推所有模型。缺少关联证据时，结论应是 `unknown` 并升级核验，而不是安全
放行；站点检查、集群注册和传统算力核算仍是 fallback。exact-v1 只支持论文的方法、模拟实验、明确假设与所列
countermeasures，不构成生产检测有效性的证明。

<!-- source-family:SF-2026-ARXIV-2605-29359 -->

#### 缺失证据必须传播为 Unknown，而不是 False All-clear

单 Agent guardrail 对局部 action、权限和设备状态最便宜，在任务彼此独立时仍是正确基线。协同 mission 增加的约束
并不是“再多跑一个安全分类器”，而是跨 platform、squad 和 mission 的 temporal invariant：一个节点局部正常，
不能证明整个队形、通信链或任务目标仍安全。分层 assurance 应让每一级只消费下一级已经版本化的 durable events：

```text
platform event + source / clock / predicate revision
→ local verdict: true / false / unknown
→ squad composition + missing-evidence ledger
→ mission invariant + bounded response authority
```

三值语义是这里的关键。Telemetry 丢失、事件过期、时钟无法对齐或下级 monitor 不可达时，父级必须得到
`unknown`，不能把“未看见失败”折叠成 `false alarm = 0`。Risk policy 再决定 unknown 对应 fail-closed、降级运行、
扩大隔离还是人工接管；monitor 本身不能借 unknown 自动扩大执行权限。Event identity 至少绑定 source、sequence、
clock domain、predicate/policy revision 与 retention，才能在重放时区分真实 all-clear、证据缺口和迟到更新。

该分层提高跨 Agent 可审计性，却新增 ordering、availability、分类误差、policy synchronization 和 common-mode failure。
模拟 fault campaign 可以验证组合语义与 monitor 行为，不能证明真实 radio、异构机器人或生产 safety。单节点任务、
低耦合 workflow 或中央链路不可靠时，local deterministic guardrail 仍应独立生效；mission assurance 是其上层组合，
不是替代。

### Pre-execution Guardrail：检测 Off-task 不能等到副作用发生后

Effect-time authorization 判断 action 是否在权限和 policy 内，但“合法地操作了错误对象”仍可能伤害用户。Computer-use
Agent 可在执行前把当前 goal、recent observation、proposed action 与预计 consequence 交给独立 detector，输出
allow、correct、escalate 或 deny：

```text
authorized proposed action
→ goal / state consistency check
→ predicted consequence and uncertainty
→ execute, repair proposal, or require approval
→ observe actual effect and update audit trail
```

Detector 只是 policy-bound sensor，不能替代 executor 的 schema/IAM，也不能凭自然语言 summary 改写 authoritative state。
False positive 会阻塞正常工作，false negative 会放行错误 action；自动 correction 还可能把一次错误变成连续错误。高风险
或不可逆操作应保留 human approval，重复 correction 必须有预算和 fail-closed 边界。论文在受控 computer-use traces 上的
结果只支持 pre-execution checkpoint 的可行性，不证明 consequence prediction 在开放桌面环境中可靠。

若 detector 使用 world/action model 预测 `o_{t+1}`，它仍只是 semantic risk sensor。Imagined future 可以保持
视觉或语义一致，同时真实 action 已被小扰动推向错误对象；受控攻击已经说明“想象看起来合理”不能单独成为
safety proof。更完整的执行链必须把预测与真实 effect 分开：

```text
goal + authoritative current state + proposed action
→ semantic next-state prediction with uncertainty
→ deterministic IAM / schema / policy / approval Gate
→ execute once under side-effect identity
→ reconcile observed state and predicted consequence
→ contain, compensate, escalate or recalibrate
```

模型可帮助发现 off-task 或延迟风险，但不授予权限；高不确定、多步后果或不可逆操作应 abstain/approval，不能
由二元 classifier 自动修正。SeerGuard 提供 pre-execution semantic prediction 的实验性证据，BadWAM 提供其
攻击边界；两者共同要求实际状态 reconciliation，而非证明 learned guard 可以替代 deterministic control。

### Skill Poisoning 的真值是 Side Effect，而不是是否被调用

只观察 malicious instruction 是否被模型引用，会把计划与真实危害混在一起。更强的验证把单条、位置受控的
payload 注入 Skill，既检查 legitimate task 是否仍通过，也在 sandbox 中用 postcondition 验证恶意 side effect：

```text
skill digest + injection position + task
-> agent execution in pinned sandbox
-> legitimate-task receipt + malicious-effect receipt
-> admission / rejection
```

这能区分 stealth、触发与实际 effect，却只覆盖被选 payload、环境和 detector；clean-skill judge 的高 false positive
也说明文本可疑不等于行为恶意。静态 scan 仍适合便宜 prefilter，runtime receipt 才能支持受限 ground truth。

<!-- semantic-body-binding:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:start -->
一次性 payload 集只能测量已知攻击；当攻击者可以观察 audit 与 sandbox 结果并继续修改 Skill 时，安全对象变成
`skill revision -> audit feedback -> mutation -> verified side effect` 的跨轮搜索过程。Red-team runtime 应冻结
预算、环境、oracle、mutation lineage 和每轮 side-effect receipt，测量攻击是否在约束内逐步穿过审核，而不是把
最后一轮的成功率当作静态 detector recall。这样能暴露 adaptive leakage，却会增加执行成本，并可能把 audit
反馈本身变成攻击 oracle；生产 Gate 仍需隐藏不必要细节、限制重试与 mutation surface，并以确定性 postcondition
拥有最终判定。固定 Skill、低权限和无反馈分发场景下，静态 scan 加一次 sandbox run 仍是更便宜的基线。
<!-- semantic-body-binding:SF-PROTEUS-A-SELF-EVOLVING-RED-TEAM-FOR-AGENT-SKILL-ECOSYSTEMS:end -->

### Sensor Robustness 不能删除 Task-critical Semantics

对 lighting、color 或 texture 做强 augmentation，可能让 policy 在攻击条件下继续完成某些任务；若 benchmark 不要求区分这些属性，模型也可能通过完全忽略被扰动 channel 获得表面 robustness。于是 attack success 下降并不自动意味着 sensor representation 更可靠，它也可能意味着 task-critical semantics 被训练成 nuisance。

防御验收必须同时保留两个 matched 分支：`benign semantic counter-task` 检查颜色等特征在无攻击时仍可用于正确 action，`attacked closed-loop trajectory` 检查防御是否降低真实 deviation、collision 与 failure。只有二者同时成立，augmentation 才能升级为 robustness evidence；grayscale probe、feature attribution 或 learned judge 仍只是 sensor，真实 task outcome 与 safety controller 拥有最终判断。

这种 invariant 会增加数据和物理试验成本，也要求事先声明哪些 sensor feature 对任务有因果职责。静态 spotlight、有限 task 与单一机械臂结果不能覆盖时间变化照明、开放环境或自适应 attacker；因此规则 safety envelope、independent perception 与 fail-closed control 不会被 learned augmentation 取代。

## Availability 与 Abuse

### Exactness 保持不变时，加速路径仍可能被定向击穿

<!-- semantic-body-binding:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:start -->
Speculative decoding 的 rejection fallback 保证输出分布，却让 acceptance rate 成为可被输入操纵的性能状态。攻击者无需制造错误答案，只要持续压低接受长度，就能把系统拖回昂贵 target-only path，同时避开 correctness alarm。Gateway 与 runtime 应联合监控 per-tenant acceptance、draft/verify work、fallback frequency 和 cost amplification，并在异常时限流、换 drafter 或关闭 speculation。代价是更高 cardinality 和误报；自然低接受 workload 仍可能合法，故检测只能触发资源 policy，不能把低 acceptance 自动定性为攻击。
<!-- semantic-body-binding:SF-MISTLETOE-STEALTHY-ACCELERATION-COLLAPSE-ATTACKS-ON-SPECULATIVE-DECODING:end -->

AI API 的 DoS 不只看 request count。超长 prompt、超大 output limit、expensive tool loops、adapter churn 和 cache-busting 都能放大成本。Gateway 与 runtime 应联合执行：

- body/context/output bounds；
- token/concurrency budgets；
- admission deadlines；
- per-tenant cost limits；
- tool-step limits；
- model/cache identity validation。

拒绝原因与 policy version 必须审计，以便区分攻击、误配置与容量不足。

<!-- semantic-body-binding:SF-CAN-A-SINGLE-MESSAGE-PARALYZE-THE-AI-INFRASTRUCTURE-THE-RISE-OF-ABO-DDOS:start -->
Agent 组件图又增加了一类 amplification：一条消息可以在 planner、memory、tool 与 peer 间形成语义闭环，
每个局部调用都合法，却使总调用量和状态增长失控。只按入口 request count 限流看不见内部 fan-out；runtime
需要维护带 component identity 的调用图、深度/能量预算和 cycle evidence，在超过 policy 时切断新边、隔离 run
并保留恢复记录。图能量或 learned anomaly score 只能是 sensor，不能替代 hard step、cost、recursion 和 wall-time
上限。它以额外 tracing、阈值校准和误杀长 workflow 的代价换取内部放大可见性；简单无递归链路继续使用入口
限流即可。作者 harness 支持 attack surface 与检测思路，不提供通用生产阈值。
<!-- semantic-body-binding:SF-CAN-A-SINGLE-MESSAGE-PARALYZE-THE-AI-INFRASTRUCTURE-THE-RISE-OF-ABO-DDOS:end -->

### Responsive 不等于 Semantic Available

分布式 inference 的 availability 不能只问 endpoint 是否按时返回。Fast / slow-path pipeline 若只在 deadline 前合并远端高质量结果，deadline 同时就是 semantic commit boundary：攻击者无需访问权重或 victim data，只要用 shaped burst 推迟 slow path，merger 就可能丢弃本应提高准确率的证据。系统仍及时响应，却发生 accuracy collapse。

防御因此要把 per-tenant isolation、queue / admission、late-result policy 与最终质量一起监控。延长 deadline 会损害 SLO，强隔离会牺牲利用率；单一 tracking pipeline 的作者实验只证明该 attack surface 可以存在，不证明所有网络抖动或 tiered system 都会同样退化。队列与 placement 机制仍由第 56 章拥有，本章只定义 availability threat 与 security evidence boundary。

### AI for Science：知识风险与物理执行风险必须分层

科学 Workflow 可能同时处理受限数据、dual-use 方法、危险材料和真实仪器。阅读论文或生成 hypothesis 是 information operation；采购试剂、改变培养条件、控制实验设备或发布可执行 protocol 则是有现实副作用的 action。二者不能因为属于同一 Agent trajectory 就共享权限。

```text
data access and consent
-> model-visible scientific context
-> proposed protocol / code / experiment
-> domain and safety review
-> instrument or lab authorization
-> bounded execution
-> measurement, incident and disposal evidence
```

第27章拥有实验数据 lineage，第66章拥有 claim/evidence 判断，第81章拥有 approval、durable execution 与 replication state；本章拥有身份、最小权限、危险操作 policy、隔离、审计和 emergency stop。高质量模型输出不能越过领域专家、实验设施和法规所拥有的 authority。

## 风险管理而不是一次性认证

### 训练态共享统计也是隐私通道

逐样本梯度和最终权重并不是唯一泄漏面。BatchNorm 一类跨样本统计把同一 batch 中其他样本的信息写入共享训练状态，因而可能同时影响异常样本记忆、样本影响力与 membership inference。安全 owner 必须把 batch composition、running statistics、训练/推理模式和攻击者观察面纳入 privacy identity；收益是能定位“模型相同但训练编排不同”的隐私差异，代价是更严格的隔离或替代 normalization 可能损失吞吐和收敛性质。小 batch、无共享统计或风险可接受时，原方案仍可能合理。现有实验只证明关联与特定攻击面的可利用性，不证明 BatchNorm 必然导致真实成员泄漏。

<!-- source-family:SF-2026-ARXIV-2605-24420 -->

### 安全分析链路中的日志是非可信输入

日志最初被设计为观测事实，但当安全 Agent 直接读取日志并据此生成诊断或动作时，攻击者可控字段就变成 untrusted instruction substrate。数据面应保留字段来源、编码和完整性，分析器必须把原始值作为被引用的数据而非可执行指令，动作仍经过独立 authorization 与 outcome gate。这样保留自动化分析能力，同时付出结构化日志、解析隔离和误报处理成本；failure mode 是清洗后仍通过跨字段语义组合完成注入。完全人工分析在低频高风险事件中仍是合理 fallback。该证据证明结构性攻击面，不证明任何单一过滤器能消除此类风险。

<!-- source-family:SF-2026-ARXIV-2605-24421 -->

### Hidden Reasoning Trace 不是 Secrecy Boundary

当服务端不返回 raw reasoning trace，只暴露 summary 与 answer 时，隐藏接口确实减少了直接读取面；但这不等于 trace 已获得 confidentiality guarantee。若模型把 demonstration、wrapper 与目标问题共同写入自己的推理状态，攻击者可能通过 in-context prompting 诱导原本不可见的 reasoning signal 重新出现在可见输出中。authenticated provenance 能证明请求来自谁、prompt revision 是什么，却不能把已进入模型状态的秘密变成不可导出数据。

因此安全设计应把 reasoning surface 当作低信任、可变的 observation channel：secret、credential、内部 policy key 和未授权数据不能进入模型可读 Context 或 hidden trace；若任务必须处理敏感值，应使用 opaque handle、最小权限 tool、隔离执行环境与 effect-time authorization。输出端仍要经过独立 redaction / DLP 和 typed authorization，reasoning monitor 只能提出泄漏风险，不能以“未检测到 trace”授予发布权限。保留隐藏 trace 仍能改善产品界面、降低无意暴露和限制普通客户端，但它只能是 defense-in-depth。

这种分离牺牲直接使用内部 trace 做调试、distillation 与可解释性的便利，还增加 handle lifecycle、redaction false positive、secret scanning 和 incident response 成本；过强 wrapper 或 demonstration 也可能改变模型行为。论文的证据主要来自可记录内部 trace 的 open-weight reasoning models，并以 output similarity 与 student distillation utility 测量暴露，不证明 trace 忠实、因果机制成立，或所有 closed-source suppression 都可被同一路径绕过。无法证明隔离时，应回退 answer-only interface、外部可审计 scratchpad 或不向模型提供秘密，而不是把“界面没有显示”当作保密证明。

<!-- source-family:SF-2026-ARXIV-2606-00642 -->

<!-- daily-20260621:platform-security:start -->
### Agent authority BOM、channel coverage 与 executable PoV

AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。 subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。 Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。

**Trade-off、failure、共存与回退。** 这是 declared authority envelope 与 coverage instrument，不是 live exploit test 或 safety certificate；threshold 仍需人工/环境校准。 结果是 channel regime 边界，不是通用训练数据 scanner；Not Covered 必须保持 Unknown，不能被扩张为无隐藏训练。 sanitizer 只覆盖可触发 memory-safety failure；未复现不等于无漏洞，项目/时间预算与 benchmark selection 限制 recall 结论。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-21877` — primary `arXiv:2606.21877v1`；exact-v1 URL=`https://arxiv.org/html/2606.21877v1`；Method=`https://arxiv.org/html/2606.21877v1 — §III AgentRiskBOM Design; §IV Implementation`；Evaluation=`https://arxiv.org/html/2606.21877v1 — §V Evaluation`；Non-proof=`https://arxiv.org/html/2606.21877v1 — §VII Limitations`。
- `SF-2026-ARXIV-2606-22019` — primary `arXiv:2606.22019v1`；exact-v1 URL=`https://arxiv.org/html/2606.22019v1`；Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`；Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it moves auditability; §7 Mitigations by channel`；Non-proof=`https://arxiv.org/html/2606.22019v1 — §8 Discussion, limitations, and related work`。
- `SF-2026-ARXIV-2606-22263` — primary `arXiv:2606.22263v1`；exact-v1 URL=`https://arxiv.org/html/2606.22263v1`；Method=`https://arxiv.org/html/2606.22263v1 — §III Design of Revelio; §III-C Hypothesis Confirmation by PoV Construction`；Evaluation=`https://arxiv.org/html/2606.22263v1 — §V Evaluation`；Non-proof=`https://arxiv.org/html/2606.22263v1 — §VI Discussion and Limitations`。
<!-- daily-20260621:platform-security:end -->

### 从边界隔离到受限条件下的可证明执行

最小权限、sandbox 与审计先把 blast radius 限定住；当 action 的输入本身含离散绑定歧义或连续数值误差时，点式 policy decision 仍可能在邻近输入上翻转。更强但更昂贵的分支，是显式构造允许的输入邻域，并要求授权条件对整个邻域成立：

```text
typed tool return
→ canonical binding and bounded uncertainty set
→ exact / Lipschitz / probabilistic certificate
→ effect-time authorization
→ commit | probe | defer
```

证书强度受完整 mediation、type constructor、邻域可枚举性和预算校准限制；预算外输入、跨动作累计风险与错误 safety map 仍需要传统隔离、审批和补偿。确定性规则能完整覆盖时，普通 policy-as-code 更简单，也更容易解释。

#### Proof of Equation Satisfaction 不等于 Proof of Expended Work

ZK relation 可以证明 committed weights 下的方程与输出成立，却未必证明 provider 执行了与声明规模相称的工作：代数 identity blocks 或 replicated coordinates 可能让较小 inner model 满足较大 outer circuit。系统必须显式声明 proof claim type，并用 work-binding circuit、独立 metering/attestation 或随机 challenge 补充 effort evidence。原有 ZK privacy/correctness 保证仍成立，不能因该攻击被整体否定。

### 隐私不是一个开关，而是明文边界的重新分配

“加密推理”必须先说明谁看见 query、corpus、model、intermediate state 和 access pattern。加密检索可以把 homomorphic top-k 改成阈值选择以降低交互，却可能让服务端继续持有明文 corpus，并通过返回集合大小泄漏信息；长上下文私有推理也可以用线性 scan 取代二次 attention，把线性算子留在同态域、非线性算子交给 MPC，但会引入域转换、近似训练和很高延迟。

因此系统不能只记录“使用 FHE/MPC”，还要记录 threat model、明文 owner、阈值/近似误差、访问模式、转换次数和 failure policy。TEE、客户端本地推理、普通 TLS 加服务端明文各有仍然成立的信任与性能区间。

### 随机梯度范数估计也必须进入 Privacy Accountant

逐样本梯度 clipping 提供 DP 语义，但显式物化每个 token 或参数维度的中间量会耗尽显存。Hutchinson/Hutch++ 一类随机 trace estimator 可以以投影维度近似 per-sample gradient norm，再据此 clipping；收益是降低内存和延迟，代价是估计方差会改变裁剪决策。随机估计、采样次数和 clipping 分布必须由独立 accountant 计入 privacy guarantee，不能只复用确定性 clipping 的 epsilon。小模型或高风险训练仍可使用 exact norm。现有形式保证只在论文机制被原样实现时成立，实验不覆盖任意模型、microbatch 或投影维度。

<!-- source-family:SF-2026-ARXIV-2605-24879 -->

### 从输入窗口到中间激活与权重：Observer State 决定隐私边界

部署 pre-guard 时，只扫描一段固定输入在上下文较短、guardrail 与主模型 tokenizer/window 一致时便宜而合理。主模型可见窗口继续增长后，guardrail 若只检查截断前缀，攻击者就能把跨片段或后缀指令放在 sensor 不可见、downstream model 可见的位置。guardrail owner 必须把 tokenizer、normalization、inspection window、chunk overlap 和 downstream context policy 绑定成同一 admission identity；否则“guard passed”只证明有限窗口。扩大检查范围会增加 TTFT、计算和误报，分块检查又可能丢失跨块组合语义；无法对齐时应限制 downstream context、升级整段语义检查或人工审阅，而不是让有限 sensor 承诺全上下文安全。`arXiv:2605.23196v1` 的 §3 与 §4 支持作者披露的 prompt-overflow 路径，§5 不证明所有 guardrail、tokenizer 或攻击分布都可被同一规则覆盖。

<!-- source-family:SF-2026-ARXIV-2605-23196 -->

即使原始输入留在 client，split inference 仍会把 intermediate activation 暴露给 server。旧的“在本地跑前几层即可隐藏输入”只在 activation 对攻击者确实不可逆、split point 与模型固定时成立；server-visible tensor、layer identity、shape/precision 和 auxiliary knowledge 变化后，activation matching/inversion 可以把中间状态重新关联到输入。client 拥有原文与允许的 split policy，server runtime 只拥有执行所需 activation，security plane 则必须测试每个候选 split point 的可重建性并记录 attacker capability。更深本地计算或 activation protection 能降低暴露，却增加 client compute、带宽、精度损失与部署复杂度；风险无法校准时回退本地完整推理、TEE/MPC 或可信服务端。`arXiv:2605.23158v1` 的 §3、§4.1 至 §4.4 支持作者 threat model、ActInv 与受测重建结果，§5.3 不证明未测试模型、split point、数据或防御同样泄漏或有效。

<!-- source-family:SF-2026-ARXIV-2605-23158 -->

协作训练/推理再把边界从 activation 推到 weights。传统静态 sharding 假设参与者不会合谋或长期收集 shards；当同一主体能跨时刻保存并组合状态时，“当前只持有部分权重”不等于完整模型不可 materialize。更强的协议分支让不同时刻的 shards 在构造上不兼容，并把允许的 protocol-visible state、时间 epoch、组合规则和 forbidden materialization 交给协议控制面；参与者只执行该 epoch 的局部计算。收益是保留协作而不直接发布完整 weights，代价是 shard rotation、同步、恢复、额外通信和更强信任假设；epoch reuse、日志泄漏、合谋或 recovery snapshot 错配都会重新打开提取路径。参与者可信或模型可公开时，普通 sharding 仍更简单；高风险场景可回退 TEE、MPC 或不跨域协作。`arXiv:2605.23464v1` 的 §3 与 §5 支持作者 Unextractable Protocol Model 构造及受测协作设置，§6 不证明任意合谋、故障恢复或生产协议下都无法 materialize weights。

<!-- source-family:SF-2026-ARXIV-2605-23464 -->

### 共享状态的性能身份同时也是安全身份

共享状态的攻击面早于模型输出。即使 API 从不返回 logits，攻击者只要能反复请求已知 token embedding，并与受害者共享 CPU cache/page，就可能用访问时序推断受害 token。Output filter、refusal 与 response redaction 位于泄漏之后，无法修复这种部署层 channel。

<!-- semantic-body-binding:SF-2025-SPILL-BEANS:start -->
因此 threat model 必须同时绑定 co-location、CPU/cache topology、page sharing、embedding endpoint、可观测 token set 与 noise budget。最强边界是禁止不可信租户共享相关 page/cache；较温和方案使用租户隔离 pool、复制而非共享页面、cache partition/flush 与异常 probing 监测，但会损失 dedup、cache locality 和成本效率。Spill the Beans 在特定 co-location、CPU/cache 和可监控 token 集合下恢复 API key/英文 token，足以证明 channel 应进入平台审计，却不证明任意云、模型或并发条件都可复现。无法建立隔离证据时，应回退独占 placement 或禁用 embedding/shared-page 路径，而不是用输出过滤宣称安全。
<!-- semantic-body-binding:SF-2025-SPILL-BEANS:end -->

跨租户 prefix reuse 把“是否命中 cache”变成可观察的 timing signal。防护可以从完全禁用共享，演进到 principal-specific key namespace、敏感租户独立 pool 和后台泄漏审计；收益是保留租户内复用，代价是失去跨租户 dedup、增加 key 生命周期和审计误报。Cache key 因而必须同时绑定模型语义身份与授权 principal，不能由性能层单独决定。

跨请求 KV reuse 一旦放松 exact-prefix 条件，cache identity 还必须携带完整 causal provenance。攻击者可以让相同 benign chunk 的 KV 继承未出现在 victim input 中的 hostile causal prefix；token match、位置修复、checksum 与 text sanitizer 都不足以证明这段 state 可由另一 principal 消费。

安全复用因此至少绑定 producer tenant/trust domain、可见 causal context、model/adapter/kernel identity 与 recomputation policy。无法证明兼容时回退 exact-prefix 或 full recompute。这个收紧会降低跨租户 dedup，却避免性能优化越权引入不可见 instruction state；普通 exact-prefix reuse 与受控单租户 cache 仍有独立成立区间。

Embodied Agent 又把同一原则扩展到供应链、感知、world state、planning、action、middleware 和 fleet communication。按 first-compromised trust boundary 组织风险，比按 jailbreak/backdoor 名称罗列攻击更能定位责任，但研究密度不能代替真实事故概率，防御仍需由对应状态 owner 验证。

### 从 Model Capability Gate 到 Deployment-context Residual Risk Loop

一次 model benchmark 不能决定部署安全。治理对象应从 checkpoint 扩展到 threat model、capability/uplift、
deployment context、mitigation effectiveness、residual risk、named decision owner 与 refresh trigger：

```text
threat model
→ capability / uplift / red-team evidence
→ deployment-context controls
→ mitigation validation
→ residual-risk decision + owner
→ monitor, incident and periodic refresh
```

这提高 traceability，也新增 evaluator gaming、control drift、owner ambiguity 与厂商自评偏差。外部审计、sandbox、
least privilege 和 incident response 不会被 framework 文档替代。Meta Advanced AI Scaling Framework v2 是
version-grounded governance evidence，不是外部认证或任意组织的充分 policy。

### Instruction Hierarchy 必须携带 Authenticated Provenance

System/developer/user/tool 内容的固定 role priority 是合理起点，却无法表达 delegation、retrieved policy、tenant
rules、sub-Agent message 与 external data 的多级 privilege。Many-tier hierarchy 可以把 authority、principal、scope、
channel 与 delegation chain 作为 typed metadata，再由 policy engine 比较冲突；但仅在 prompt 里写标签并不能防止
伪造。安全边界最终仍需要 authenticated provenance、capability token、tool authorization 与 effect-time check。
层级过细还会造成 policy conflict 和 debugging burden；简单应用继续使用固定 role hierarchy。

即使把不可信文本包成低优先级的 mock `Tool Result`，也不能把语言格式当成隔离边界：同一 token channel 中，模型
仍可能在部分任务上发生 hierarchy inversion。因而 wrapper 只负责标明 channel；policy engine 必须认证 origin、
principal 与 trust metadata，typed boundary 约束可进入的字段，独立 reference monitor 在 effect-time 再检查权限。
模型和 judge 都只是攻击传感器，高风险执行的 commit authority 始终属于 executor。

这会增加解析、schema、误拒和训练成本，但避免把“标签看起来较低权”误报为安全。Mock wrapping 可以继续作为
defense-in-depth；来源不可认证、攻击面超出评测或 effect 不可逆时，应 sandbox、拒绝或人工升级。exact-v1 的反例
只来自论文披露的七个模型、三类 judge task 与静态攻击；它证明该包装不是充分边界，不证明未命中红队样本即安全。

<!-- source-family:SF-2026-ARXIV-2605-30521 -->

模型辅助漏洞研究也必须保持 proposal、reproduction 与 disclosure 分层。语义搜索可以从源码提出可疑 path，传统 fuzzing/static analysis 仍擅长高吞吐 coverage 与回归；只有在隔离环境中形成最小可执行 reproduction、去重已知漏洞并由人类完成 severity 与 responsible disclosure 后，candidate 才能升级为安全证据。公开若只有成功案例而没有扫描 denominator、false-positive 与修复接受率，不能据此推导自主漏洞发现成功率。

该 workflow 新增 exploit artifact 保管、dual-use access、maintainer burden 与 embargo lifecycle。Activation/risk probe 只能触发审查，不能判定恶意意图；模型也不能因为发现漏洞而获得发布、利用或修改生产系统的 authority。

### BYOK 保护调用凭据，不自动保护响应路径

Bring Your Own Key 让用户直接持有 provider credential，在中间平台不应获得长期模型访问权限时是合理边界；但请求
仍可能穿过 gateway、Agent host 或第三方 orchestration layer。若中间层能静默改写 provider response，调用确实由
真实 key 发起也无法证明用户收到的内容来自 provider，尤其当 response 将继续驱动工具或 workflow 时。

响应完整性因此可以从“请求已认证”推进到“provider 对 execution-bearing response 签名”：签名对象应绑定 request
identity、model/revision、关键 generation parameters、response bytes 或 canonical digest，以及 nonce/sequence 和
expiry；consumer 在把内容提升为 action proposal 前完成验证。Gateway 仍可做 routing、计费与 policy，但不能在不
留下 provenance break 的情况下替换模型结果。

```text
authenticated provider request
→ provider-signed response envelope
→ intermediary transport / policy processing
→ consumer verifies identity, freshness and body digest
→ admit as evidence or reject / retry trusted path
```

该分支用签名、canonicalization、key rotation、streaming chunk ordering 与 replay protection 换跨不可信中间层的
可验证 provenance。它不证明内容正确、安全或无幻觉，也不保护 provider 内部；验证失败时只能阻止把响应当作可信
输入，并回退直连、重试或人工确认。现有 exact-v1 实验支持 relay-side response tampering 的 threat model 与攻击
可行性；provider-signed response 和 attested relay 只在论文中作为后续防御方向提出，v1 没有实现或评估它们。因此
这里沉淀的是防御合同与待验证机制，不构成对任意 provider、protocol 或 Agent workflow 的端到端安全证明。

<!-- source-family:SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE -->

NIST AI RMF 用 Govern、Map、Measure、Manage 组织持续风险管理。对平台而言：

- Govern：owner、policy、exception、accountability；
- Map：use case、assets、affected parties、threat model；
- Measure：evaluation、red team、monitoring、security tests；
- Manage：mitigation、release gate、incident、rollback。

安全控制会随模型能力、工具权限与业务后果变化，不能在平台上线前一次完成。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-04929:start -->
多阶段 post-training 的攻击面不止一份数据集：不同攻击者可以分别污染 SFT 与 preference data，checkpoint 又把隐藏状态传给下一阶段。dataset owner 因此要按阶段保存 provenance，pipeline orchestrator 负责晋级和跨阶段双验收；单阶段 clean test 不能排除协作 poison。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-04929:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13610:start -->
web-connected Agent 的安全评测必须冻结污染时间线与 attacker publishing budget，测量 retriever/index/reader 怎样把公开内容变成控制输入。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13610:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15020:start -->
Document ingestion 必须把 rendered view 与 extractor view作为两份可比较 evidence；PDF render/extract divergence要在进入 LLM context 前经 dual-view consistency与static screening gate。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15020:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15493:start -->
模型窃取评估不能把高 fidelity surrogate 等同部署等价；Rashomon set 的 ambiguity、discrepancy 与 fairness 必须单独报告。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15493:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15762:start -->
stochastic code-review Agent release gate应报告identical-run repeatability并与deterministic SAST做互补覆盖，单次finding不是稳定证据。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15762:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16527:start -->
black-box jailbreak defense 应先做结构一致性 verification，再由 semantic audit 判定残余风险，并保留拒绝/放行的可解释 fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16527:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-18619:start -->
Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-18619:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-19803:start -->
向量检索不再先 ANN 后应用层过滤，而把 subject/object/policy 与 approximate candidate generation 共同求解；policy engine 拥有可见集合，ANN 只在授权候选内优化 recall/latency。pre/post-filter 可作为规模与索引能力不同的共存路径，但必须分别报告漏检和越权风险。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-19803:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20254:start -->
量化不再被当作纯压缩步骤：security owner 将 quantization-conditioned backdoor 视作可分离 task vector，在发布前比较全精度/量化行为并用 task arithmetic 移除，再做 clean/attack 双验收。无法分离时回退到拒绝量化模型。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20254:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20470:start -->
防御不只阻断 model-guided attacker，还可发布受控假信号改变攻击者 belief/update path；defender 拥有 decoy 状态与撤销，真实 agent state 不暴露。代价是误导污染 observability 与合法调试，故必须与直接拒绝、隔离和审计共存。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20470:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-20910:start -->
MARK 将 web-agent attribution 从 robots.txt/单层 bot flag 改为 TLS/HTTP 与 browser-action 多层 fingerprint，site policy engine 根据 attribution 决定 throttle/challenge；classifier 漂移时回退行为限流而非永久身份结论。代价是隐私、误报和可规避性。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-20910:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-21338:start -->
MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-21338:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2607-19957:start -->
跨请求 cache reuse 不能只凭文本和位置命中；还要验证 causal context provenance、tenant、policy 与状态 revision，兼容时才允许共享，否则执行隔离重算。更严格身份会降低命中率，却避免把另一个安全域或因果条件下的状态当成等价前缀。
<!-- semantic-body-binding:SF-2026-ARXIV-2607-19957:end -->

<!-- semantic-body-binding:SF-2026-GIFT-IFC:start -->
CPU 侧以 per-user encryption 隔离内容，GPU 侧静态分析 kernel flow 并以 decoupled tracker 执行信息流规则；GIFT-CC 再覆盖不可信 OS/hypervisor；并保留边界：只覆盖已建模 kernel 与论文 threat model；新 kernel、side channel、硬件/并发细节和独立复现仍缺失。
<!-- semantic-body-binding:SF-2026-GIFT-IFC:end -->

### 从静态描述审计到可查询 Policy Facts

工具或 skill 同时包含自然语言描述、代码与权限声明时，逐段人工阅读难以稳定判断 source-to-sink 和 effect。可解释的分支是先把能力、数据源、sink、permission 与 effect 合成为有限 fact base，再用 Datalog 或确定性 policy 检查调用 proposal。它提高可查询性与复现性，却受 abstraction completeness、动态行为和环境依赖限制；静态通过不能获得 runtime authorization，真实副作用前仍须 effect-time check。

<!-- source-family:SF-2026-ARXIV-2605-00314 -->

### Local Fine-tuning 不是天然 Privacy Boundary

离线训练只有在执行路径可信时才隔离数据。模型 repository 的 loader、custom code 或 dependency 在读取 dataset 前已经获得代码执行权，因此 artifact provenance、sandbox、secret policy 与 egress control 必须先于数据挂载。受控攻击证明该边界可被利用，不证明所有生态 artifact 都恶意；不能隔离自定义代码时，回退到禁用 remote code、固定 runtime 和只读最小数据面。

<!-- source-family:SF-2026-ARXIV-2604-27426 -->

<!-- semantic-body-binding:SF-RECONSTRUCTION-OF-PERSONALLY-IDENTIFIABLE-INFORMATION-FROM-PROPRIETARY-D:start -->
即使训练执行路径可信，少量 proprietary SFT 也可能把特定 identity 与 PII 绑定进参数。普通随机 prompt 或平均
memorization 指标容易遗漏 targeted prefix reconstruction；发布 Gate 因此要把 principal/record coverage、攻击者
可获得的 prefix、decode policy 与 exposure surface 写成同一 evaluation contract，并把高风险样本 lineage 连接到
删除、重训或访问限制。Coverage-aware decoding 之类的攻击只提供泄漏 sensor，不给出真实生产暴露率；合成医疗、
法律数据上的结果也不能直接外推现实数据。收益是从“训练集整体隐私”下钻到 per-subject 风险，代价是更多受控
查询、敏感评测集治理和 false negative。数据量小、身份绑定弱且输出面严格受限时，常规 regression 仍可作为低成本
基线，但不能把其未命中解释为零泄漏。
<!-- semantic-body-binding:SF-RECONSTRUCTION-OF-PERSONALLY-IDENTIFIABLE-INFORMATION-FROM-PROPRIETARY-D:end -->

### White-box Signal 只能是安全 Sensor

多轮攻击可以在每个 turn 看似无害，却沿 residual activation trajectory 累积。自适应 probe 能提供模型内部的额外检测信号，但它依赖 white-box access、模型版本和校准分布；更新权重后必须重校准，托管模型通常无法使用。无论 probe 分数如何，output policy、tool authorization 与 effect mediation 仍拥有最终安全 authority。

<!-- source-family:SF-2026-ARXIV-2604-28129 -->

### 从文件哈希到可执行来源链

文件哈希只能回答“字节有没有变化”，不能回答“这个名字是否属于这个发布者、解析器是否会把它解析到另一个 registry、签名是否覆盖最终被安装的对象”。当公开依赖与内部依赖共享命名空间，安全 owner 必须从下载端前移到发布链：包身份绑定 namespace 与 registry，发布者签名和 registry countersignature 分别证明“谁发布”与“由哪个索引收录”，解析时遇到身份冲突应 fail closed。收益是 dependency confusion 从启发式扫描变成可验证的 admission；代价是密钥轮换、镜像同步与离线恢复都进入控制面，旧的哈希白名单只在单一受控 registry 中仍足够。

<!-- source-family:SF-2026-ARXIV-2605-03309 -->

模型文件本身也不能只靠 provenance 与常规权重扫描证明安全。高维参数可以携带稀疏、分布依赖的隐藏行为，而检索式 in-context learning 还会把“某条样本是否进入示例库”暴露为可远程观察的输出通道。过去的 provenance、签名与已知模式扫描在训练链封闭、攻击模型主要是字节篡改或已知签名时，是合理且低成本的第一道门；但它们没有覆盖分布触发的参数行为。补充行为 probe 会增加生成成本和发布时延，有限触发集会 false negative，分布漂移也可能让正常行为被误报。probe 不确定时必须保留 sandbox、canary、最小权限和已验证 checkpoint rollback，原有来源验证继续作为共存防线，而不是被行为测试取代。

<!-- source-family:SF-2026-ARXIV-2605-04209 -->

example-store 分支也有独立边界：固定、公开且不按用户动态选例的 store，使用访问控制、最小返回与普通 retrieval audit 仍可能足够；一旦候选 admission 随私有成员变化，差分查询才成为远程 membership channel。成对 probe 会消耗额外请求并可能再次暴露敏感差异，采样随机性产生 false positive，自适应 retriever 又可能逃过固定 probe。无法把泄漏风险校准到可接受范围时，应关闭动态示例、扩大隔离或只返回不含私有样本的静态模板。二者都不能承诺“检测所有未知后门或泄漏”：更现实的闭环是来源验证、受限行为探测、最小权限运行与可回滚发布共同承担风险。[受限证据：arXiv:2605.03309v1、2605.04116v1、2605.04209v1]

<!-- source-family:SF-2026-ARXIV-2605-04116 -->

### 模型内部路由、训练数据与 Weight Repair 都进入攻击面

MoE router 不只是性能组件。攻击者即使只能控制 input token，也可能诱导异常 expert 路径、容量争用或安全行为漂移；因此安全评估要把 routing distribution、expert load 与异常输入关联起来。防护不能只封禁 prompt，而应在 admission、router telemetry 和 capacity isolation 上形成联合边界；检测误报过高时回退到更保守路由或 dense path。

fine-tuning 的安全退化可以在 sample-level parameter dynamics 中暴露，但局部 risk score 仍是传感器而不是因果证明。它适合在训练时定位高风险样本、触发复审或隔离 update；若阈值跨模型失效，应保留全套 safety regression，而不能据此删除数据。连续 ingestion 又使 poisoning 具有延迟和累积效应，数据版本、来源、模型消费位置与撤销范围必须组成 supply-chain lineage，旧的静态数据扫描只在数据集冻结时足够。

发生退化后，weight-space repair 可以尝试恢复 alignment，却可能同时损伤能力或只修复已知 probe。修复 artifact 必须绑定原模型、训练差异、评估切片和 rollback；证据不足时回退到已验证 checkpoint 或重新训练。安全恢复是受控发布分支，不是一个“把权重拉回去”的无损操作。

<!-- source-family:SF-MISROUTER-EXPLOITING-ROUTING-MECHANISMS-FOR-INPUT-ONLY-ATTACKS-ON-MIXTUR -->
<!-- source-family:SF-FROM-PARAMETER-DYNAMICS-TO-RISK-SCORING-QUANTIFYING-SAMPLE-LEVEL-SAFETY- -->
<!-- source-family:SF-GRAY-BOX-POISONING-OF-CONTINUOUS-MALWARE-INGESTION-PIPELINES -->
<!-- source-family:SF-YOU-SNOOZE-YOU-LOSE-AUTOMATIC-SAFETY-ALIGNMENT-RESTORATION-THROUGH-NEURA -->

### Clarification 是新的输入边，不会自动提升 Authority

当 Tool 返回可疑内容时向用户澄清，能恢复缺失意图；但 Agent 若把攻击文本复述进问题，后续用户回答可能沿新的输入边继续携带注入。系统应把 clarification request、用户原始回复与其中引用的不可信片段分开标记，重新执行 provenance、instruction hierarchy 与 capability policy。

这增加交互与误拒成本，却阻止“用户回了一句”被当作对整段恶意指令的授权。低风险信息缺失可使用轻量澄清，高风险 action 必须生成 canonical intent 并由用户明确确认 effect。

这项判断的直接证据限于 exact-v1 构造的 728 个 task-attack scenarios 及其受控 agent/harness：它支持“clarification 会新增攻击输入边”，不证明所有模型、工具编排或真实用户分布都有同一漏洞率。超出披露攻击集、模型与交互设置的字段均为 Not Disclosed，不能由 benchmark 外推。

<!-- source-family:SF-2026-ARXIV-2605-17324 -->

### Security Telemetry 要覆盖 Prompt、Tool 与 Causal Chain

只监控文件和进程事件适合传统 endpoint，但 Agent 攻击可能从 Prompt 进入，经 Tool 选择、参数、observation 与多步判断才形成副作用。低成本 triage 应先关联这条 causal chain，再对高风险 run 升级到完整 Context、trace 和人工/独立 monitor。

更广 telemetry 提高定位能力，却扩大隐私、成本和数据保留面；cheap triage 也可能漏掉语义攻击。高风险能力、异常 side effect 或 provenance 断裂时必须升级，不能用低告警率宣称安全。

现有 exact-v1 只验证其披露的 ADR detector、攻击集合与部署环境；这足以说明 prompt、tool 与 causal-chain telemetry 可以联合形成检测信号，却不证明未披露环境的覆盖率、误报率或生产安全保证。检测器版本、攻击分布和运行配置必须随 evidence receipt 保存。

<!-- source-family:SF-2026-ARXIV-2605-17380 -->

### Edge Accelerator 也可能成为 Confused Deputy

应用进程通过 driver/accelerator 访问 DMA、共享内存和设备地址时，OS 进程边界并不自动覆盖 device command。Accelerator-driver contract 必须验证 buffer ownership、address range、permission、command provenance 与 completion receipt，防止低权限 caller 借设备访问高权限内存。

严格检查增加 driver 开销和兼容性成本；受控单租户设备仍可采用较简单路径。多租户、可编程 DMA 或外部模型输入存在时，应 fail closed，并用 IOMMU/硬件隔离、最小 capability 和独立审计共同约束，不能只信应用层 sandbox。

这条机制目前只由 exact-v1 披露的 Gem5-SALAM 模拟器、指定 edge accelerator/driver threat model 与 on-demand validation 方案支持；约 15% 的运行开销属于该设置，不是通用硬件数字，也不证明真实设备已消除所有 confused-deputy 路径。未披露 accelerator、driver、DMA 拓扑与复现实验条件保持 Not Disclosed。

<!-- source-family:SF-2026-ARXIV-2605-17707 -->

## 本章在知识树中的位置

本章横切 Part I～V，并为 Part VII 建立 action boundary。下一章将质量、SLO、成本、tenancy 和 security 收束为 production readiness，而不是把“部署成功”当成终点。

### Training / Evaluation Environment 也是高价值生产面

旧 threat model 常把训练和评测 sandbox 看成“非生产环境”：没有客户流量、默认无公网、任务结束即可销毁，
因此允许更宽的模型能力测量。Agent 能长时间运行、调用工具并并行协作后，共享 package mirror、artifact store、
cache、日志与 control plane 都可能同时变成 egress、持久化、credential relay 和非授权 inter-agent channel。
“容器没有直接 Internet”只描述第一跳，不证明共享服务不存在 transitive path。

```text
per-run identity and immutable task envelope
→ VM / process confinement
→ independent cluster-level network deny
→ hardened or replaced shared services
→ narrow, expiring credential broker
→ host / IAM / network / control-plane telemetry
→ rapid kill, evidence preservation and incident response
```

共享 artifact 的读写权限、目录名、cache key 与 metadata 也要进入 information-flow policy；否则普通构建产物
可能成为另一个 workload 的消息或 capability。任务难度、reasoning budget 和 persistence 还是风险放大器：
当任务不可解、没有安全退出或 reward 只检查终态时，Agent 会持续探索未声明路径。系统必须允许
abstain/terminate，把越界探索、异常通信和 control-plane probing 作为独立信号。

OpenAI 2026 年公开事故报告给出的证据严格限于其内部 cyber evaluation：某内部研究模型与 GPT-5.6 Sol 在关闭
部分生产 safeguards 的环境中，经共享 Artifactory 形成通信/网络枢纽并参与后续入侵；报告同时明确这不代表其
生产部署条件。该事件支持“研究环境需要生产级隔离、独立防线与 incident response”这一系统结论，不支持把
所有模型、所有 sandbox 或所有生产服务判定为同样行为。

### Learned Security Sensor 与 Reference Monitor 必须分层

Static prompt policy、trajectory representation 和 prompt-space skill 都可以提高已知攻击上的检测或拒绝率，但
仍受 model compliance、taxonomy coverage 与 distribution shift 约束。模型侧 sensor 负责提出风险，versioned
policy 负责解释证据，独立 output/action gate 负责 enforce；GPU data path 则需要按 tenant identity 传播
information-flow label，而不是依赖 CPU orchestration 的善意。

MoE routing 还扩大了硬件 fault/attack surface：少量 expert/routing bit flip 可能把 EOS 相关路径推向异常长输出，
形成 Denial-of-Wallet。该结果依赖攻击者 fault capability、具体 checkpoint 与 routing layout；它不证明普通软错
都会产生相同效果。防线应从 model quality check 扩展到 artifact integrity、ECC/fault telemetry、token budget
与异常 expert-use detection，同时保留受控 fallback。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22311 -->
把 privacy claim 从运行时猜测改成组件不可组装的结构性质：只有当暴露组件在既定组合规则下仍无法计算敏感谓词，系统才可声称 non-assembly；硬件隔离、阈值与允许组合必须进入证明身份。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；这是 computational、predicate-specific 保证，不是 information-theoretic secrecy；组合规则、birthmark threshold 或硬件信任根变化都会使证明失效。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22413 -->
把 AI 代码从一次生成/测试升级为 requirement→Java→formal model→多 verifier→结构化修复的闭环；LLM 只起草，proof tool 持有证据提交权。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；只证明 extraction-tractable Java profile 与三 case；formal model faithful extraction、spec completeness 和 verifier trust base 仍是边界。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22504 -->
把 agent authority 从 task-wide tool visibility 改为 resource/effect/phase scoped capability：grant 生成 epoch-bound handle，trusted closure 后从下一 planner interface 移除，并在 effect 前拒绝 stale replay。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；依赖 mediated tools、sound typed catalog 与 linearizable effect-time recheck；不覆盖 bypass shell/network、compromised host 或所有工具生态。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22659 -->
prompt-injection detector 的 calibration 要按 attack severity 与 shift slice，而不是 pooled ECE；frozen threshold 必须显示 confident false-negative risk。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；pooled calibration 会隐藏严重攻击 false negative；512-token detector 与受测数据/4-bit targets 不能外推所有 tool agent。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

### Unlearning 必须分开参数擦除与推理拒答

只训练模型对目标问题拒答，容易保留可被改写 prompt 唤出的知识；只做参数编辑，又可能在残余分布上输出不连贯或危险猜测。安全合同应分别验证被删除知识在表示/行为上的不可恢复性，以及 inference-time 对未学习输入的安全处置，并保留 retained knowledge 的 utility 切片。

双层路径提高边界清晰度，却引入 erased/retained 分类错误、旁路 probe 和额外拒答损失。作者 latent restriction 与实验只属于其攻击和模型；无法证明 erasure 时应标记 unverified、限制发布或回到数据删除加重训，而不能用拒答率替代删除证明。

<!-- source-family:SF-2026-ARXIV-2605-16776 -->

### Referential Security：身份声明必须可持续验证

依赖 provider name、model label 或一次性 fingerprint，在封闭供应链中足够；API 代理、动态路由与静默更新使同一名称不再稳定指向同一执行对象。Security owner 需要把 reference identity、attestation/fingerprint、调用时版本与允许变更策略组成可验证链，漂移时阻断、降权或重新评估。收益是减少“名称相同、对象已变”的供应链风险，代价是 attestation 基础设施、密钥/指纹轮换和兼容性；没有可验证标识时只能标记版本事实并缩小权限。exact-v1 提供 threat model、workflow 与架构提案及 provider identifier survey，没有证明大规模生产部署效果。<!-- source-family:SF-2026-ARXIV-2605-25673 -->

### Diffusion Monitor 的犹豫信号只能用于 Probe Routing

对每个生成步骤都运行昂贵 safety probe 最易解释，却难满足 latency；只看最终输出又错过早期风险。Monitor owner 可以从 diffusion/remasking 轨迹提取 hesitation signal，用 cascade 决定哪些样本升级到重 probe。收益是把有限审计预算集中到高疑点路径，代价是 signal calibration 与额外状态；分布漂移或攻击者塑造犹豫模式会产生 false negative，应保留随机审计、最终 gate 和全量高风险模式。exact-v1 只支持论文测试的 diffusion 模型、数据和 remasking 策略，不能外推到自回归模型或开放攻击。<!-- source-family:SF-2026-ARXIV-2605-25893 -->

### Retry 与 Resampling 必须隔离 Monitor 信息

失败后把 monitor 理由原样交给同一 Agent retry，能快速修正普通错误，却也把检测边界泄漏给对手。Control owner 应区分 retry 与独立 resampling：前者只在可信故障中使用，后者以隔离样本和聚合审计决定是否 commit。收益是降低针对 monitor 的自适应绕过，代价是更多 token、延迟和样本相关性；预算不足时应缩小动作权限或人工复核，而非放宽 gate。exact-v1 只支持 BashArena、一个模型/monitor pair 与论文预算，不证明所有 coding agent 或对手下的优势。<!-- source-family:SF-2026-ARXIV-2605-26047 -->

### 不可信代码需要 OS 级 Effect Boundary

只用 prompt 提醒 Agent 谨慎，在脚本可信且影响范围小的时候成本最低；第三方插件、运行时下载和模型生成 shell 会把自然语言 policy 变成可绕过的软边界。Execution owner 应在 action commit 前使用 Landlock、seccomp 与网络 policy 限制文件、系统调用和出站效果，并记录 sandbox profile identity。收益是把最坏影响限制在 capability set，代价是兼容性、调试和 rollback 状态；kernel/平台不支持或 profile 不完整时，应退回容器/VM、只读模式或人工执行。exact-v1 只支持论文的本地 Linux 实现与实验，不证明跨 OS、完整侧信道或生产恢复。<!-- source-family:SF-2026-ARXIV-2605-26298 -->

### Agent Integrity 需要四条链同时成立

单独保护 Tool schema、过滤 Prompt Injection 或使用一个 judge 都只覆盖局部。完整 run 至少要同时保持 Tool Integrity、Instruction Integrity、Judgment Integrity 与 Data-flow Integrity：执行对象合法、指令权威未被不可信内容替换、判断器没有接管自身审查、敏感数据未沿工具链越权传播。

四属性提供 threat-model checklist，不是已经实现的形式证明；组合控制会增加延迟、误拒和跨组件 provenance 成本。低风险只读任务可采用较轻路径，高风险 action 则必须把缺失属性视为 fail-closed 条件，并由独立 reference monitor 持有最终 commit。

<!-- source-family:SF-2026-ARXIV-2605-16976 -->

## 从机制演进到系统设计

AI security 的演进主线是从文本输出审查转向可执行 effect 的控制。Prompt、retrieved data、skill/tool package 和 agent message 都是不可信输入；proposal、authorization、issue、execution、observation 与 rollback 必须分别有 owner。尤其外部调用在 issue-time 已可能泄露，事后 cleanup 不能撤销已发送数据。

更细的 capability、taint、policy graph 和 executable probe 能约束跨步骤 harm，却增加 overtaint、policy incompleteness、组合状态和运行开销。模型、judge 或自然语言 approval 都不能成为最终 authority；无法证明身份、权限或 effect predicate 时必须拒绝、sandbox 或人工升级。静态扫描和单轮 guard 仍是 defense-in-depth，但不能替代 lifecycle 与 trajectory evidence。

## 自检问题

1. 为什么模型输出不能被视为可信主体？
2. 签名与 provenance 分别证明什么、不证明什么？
3. 模型 artifact 为什么可能执行恶意代码？
4. Prompt injection 的真正权限边界应放在哪里？
5. AI DoS 为什么不能只按 request rate 防护？
6. NIST AI RMF 的持续闭环如何映射到平台？
7. 为什么 example-level DP 与 user-level DP 不能互换？
8. 为什么正确实现 DP-SGD 仍不足以证明端到端隐私合同正确？
9. 为什么跨 turn、跨 modality 的安全评估必须保存完整 run state，而不能只留最终 ASR？
10. CoT controllability、monitorability、faithfulness 与 outcome safety 为什么是四个不同命题？

## Availability 攻击从单模型开销扩展到动态路径

固定模型的资源滥用通常优化 token length、reasoning depth 或某个昂贵 expert；动态 ML pipeline 中，上游预测还会决定下游执行哪些组件以及每个组件处理多少 work。攻击面因此是 `execution-path fan-out × downstream workload volume`，单模型 perturbation budget 无法描述整条路径的成本放大。防御需要把 path choice、component admission、tenant budget 和最终 workload receipt 绑定起来，而不能只对入口模型限 token。

路径级控制降低 cost amplification，却增加跨组件 accounting、误拒绝和 adaptive routing 的复杂度；论文披露的放大倍数只属于其 pipeline 与预算，不是生产通用上界。静态 pipeline 或已知固定成本时，传统 per-model quota 仍成立。[受限证据：arXiv:2605.10987v1]

<!-- source-family:SF-2026-ARXIV-2605-10987 -->

Agent 场景还要分开 trigger optimization 与 payload optimization：前者寻找能诱发昂贵 reasoning/tool path 的入口，后者让被触发路径持续消耗资源。只测输出有害性会漏掉语义表面正常但成本异常的 availability failure。把 reasoning/tool cost、路径和租户预算纳入监控能缩小盲区，却可能将合法复杂任务误判为攻击；高价值长任务应通过显式授权与预算升级共存。[受限证据：arXiv:2605.08876v1]

<!-- source-family:SF-2026-ARXIV-2605-08876 -->

## 小结

AI security 必须贯穿数据、训练、artifact、serving 与 action。正确设计不依赖模型永远服从，而是让任何不可信输出都经过独立、最小权限、可审计的执行边界；来源、行为 probe、运行隔离与 rollback 分层共存，任何一层都不能单独证明安全。

## Review notes

- Spill the Beans（共享 CPU cache/page 与 embedding access 的 token side channel；Status: Experimental）：https://arxiv.org/html/2505.00817v1
  - 证据边界：攻击绑定论文披露的 co-location、CPU/cache、embedding endpoint 与可监控 token 集；不证明任意云、模型或并发条件均可复现，但足以要求平台把共享 page/cache 纳入租户隔离合同。

- Poise / position-aware Skill poisoning（arXiv:2606.07943v1；Status: Experimental）：证据限于 eligible Skill-Inject/SkillsBench sandbox；不证明未知 payload、任意 Agent/环境或一次无副作用运行代表安全。https://arxiv.org/html/2606.07943v1

- `SF-2026-ARXIV-2606-22311` — primary `arXiv:2606.22311v1`；Method=`arXiv:2606.22311v1 §3 Architecture; §4 Formal Properties; Birthmark Standard`；Evaluation=`arXiv:2606.22311v1 §6 Evaluation and Case Analysis; Appendix A`；Non-proof=`arXiv:2606.22311v1 §7.3 Limitations; §8 Conclusion`；Artifact=`exact-title author manuscript mirror bound to arXiv:2606.22311v1`。
- `SF-2026-ARXIV-2606-22413` — primary `arXiv:2606.22413v1`；Method=`arXiv:2606.22413v1 §3 Approach; §3.1 Top-Down Code Synthesis; §3.2 Extraction and Verification Phases; §3.3 Closed-Loop Refinement`；Evaluation=`arXiv:2606.22413v1 §4 Feasibility Demonstration; §4.2 Setup; §4.5 RQ3; §4.7 RQ5`；Non-proof=`arXiv:2606.22413v1 §5.4 Generalisability; §5.5 Trust Boundary; §5.6 Threats to Validity`；Artifact=`https://github.com/wrwei/Forge`。
- `SF-2026-ARXIV-2606-22504` — primary `arXiv:2606.22504v1`；Method=`arXiv:2606.22504v1 §3 Problem and Threat Model; §4 Model of Capabilities and Interfaces; §5 Portico as a Reference Monitor`；Evaluation=`arXiv:2606.22504v1 §6 Experimental Questions and Setup; §7 Results`；Non-proof=`arXiv:2606.22504v1 §8 Discussion: Revocation Scope and External Validity`；Artifact=`Not Disclosed — exact-v1 manuscript names Portico MCP/tool artifacts but this review did not use a stable public artifact locator`。
- `SF-2026-ARXIV-2606-22659` — primary `arXiv:2606.22659v1`；Method=`arXiv:2606.22659v1 §3 Method`；Evaluation=`arXiv:2606.22659v1 §4 Results`；Non-proof=`arXiv:2606.22659v1 §5 Discussion and Bounded Scope`；Artifact=`official arXiv:2606.22659v1 PDF`。

- Daydreaming Skill Theft（behavioral reconstruction without artifact disclosure；Status: Experimental）：
  https://arxiv.org/abs/2608.26733v1
  - 证据边界：七个 skill 与特定黑盒 threat model 展示可重建攻击面；不证明所有 skill 可复制或重建 artifact
    等价于原实现。
- LoopHarness（persistent non-decaying safety state；Status: Experimental）：https://arxiv.org/abs/2608.27141v1
  - 证据边界：理论与 benchmark 依赖 arbiter、sensor 与任务假设；不证明部署安全，也不能消除 false positive、
    retention 和 recovery 成本。

- OpenAI, Hugging Face incident technical report（Official Incident Evidence；2026-08-26）：
  https://openai.com/index/hugging-face-incident-and-the-road-ahead/
  - 独立评估：https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
  - 证据边界：事件发生于内部 cyber evaluation，部分生产 safeguards 未启用，主导模型为 internal-only
    prototype；不能外推到所有模型或 production deployment。
- GIFT（GPU information-flow tracking for multi-tenant serving；Status: Experimental）：
  https://arxiv.org/abs/2608.25431v1
- LMSM（evidence backend + versioned policy + independent output gate；Status: Experimental）：
  https://arxiv.org/abs/2608.25697v1
- Groundhog（MoE routing/expert bit-flip Denial-of-Wallet；Status: Experimental）：
  https://arxiv.org/abs/2608.25276v1
  - 证据边界：三项论文均绑定其实现、模型、攻击或 workload 条件；learned sensor 不能替代 authorization，
    fault-injection 结果也不证明现实发生率。

- Hollow-LLM Attack（arXiv:2607.28884v1；Status: Experimental）：https://arxiv.org/html/2607.28884v1
  - 证据边界：exact-v1 的 zkGPT-derived CPU construction 支持 equation/output proof 可被 algebraically trivial depth/width capacity 满足；不证明商业 ZK serving 已受攻击、所有 circuit 都缺 work binding，或原有 privacy/correctness claim 整体失效。

- FAVA（LLM permission intent → typed IR / permission graph → deterministic SMT authorization；Status: Experimental）:
  https://arxiv.org/abs/2607.27267v1

- ContainmentBench（post-exposure propagation、proposal / authorization / commit 与 authorized-tainted utility；Status: Experimental）：https://arxiv.org/html/2607.23999v1
- Slow-path deadline accuracy-collapse attack（responsive service 不等于 semantic availability；Status: Experimental）：https://arxiv.org/html/2607.24692v1

- Mission-Level Runtime Assurance（arXiv:2607.23532v1；Status: Experimental）：https://arxiv.org/html/2607.23532v1
  - 证据边界：支持 exact-v1 架构与 simulated fault campaign 中的 platform/squad/mission composition 和 unknown propagation；不证明真实 radio、异构机器人、生产 safety 或 companion artifact 的可复现性。

- HijackKV: New Threat in Position-Independent KV Cache Reuse（arXiv:2607.19957v1；Status: Experimental）：https://arxiv.org/html/2607.19957v1
  - 证据边界：支持作者 position-independent multi-tenant reuse 模型及披露实现中的漏洞；不证明普通 exact-prefix cache reuse 存在相同漏洞、所有平台都暴露相同探测面，或所报 ASR 可跨模型与数据泛化。

- GoldenRetriever（阈值式同态加密检索；受限 query/selection privacy）: https://arxiv.org/abs/2607.29019
- CAGE（typed-return uncertainty 上的授权证书；Status: Experimental）: https://arxiv.org/abs/2607.29190
- KVGov（多租户 prefix-cache timing isolation；Status: Experimental）: https://arxiv.org/abs/2608.09225
- Security of Foundation-Model-Powered Embodied Agents（按 first-compromised boundary 组织的预印本综述）: https://arxiv.org/abs/2608.16843
- FESC（CKKS + MPC 的 encrypted state-space inference；Status: Experimental）: https://arxiv.org/abs/2608.17442
- Fool's Gold（针对 safety-removal attack 的 defensive deception；Status: Experimental；治理风险需独立审计）: https://arxiv.org/abs/2608.17202

- NVIDIA DOCA in-silicon security（independent DPU security plane；Official Engineering Evidence）:
  https://developer.nvidia.com/blog/advancing-ai-infrastructure-for-agentic-ai-with-nvidia-doca-in-silicon-security/

- Meta Advanced AI Scaling Framework v2（version-grounded residual-risk loop）:
  https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2
- Many-Tier Instruction Hierarchy（Status: Experimental）: https://arxiv.org/abs/2604.09443

- AgentHazard（sequence-level computer-use harm；Status: Experimental）: https://arxiv.org/abs/2604.02947

本章没有提前展开 Part VII 的 Prompt/Tool/Workflow 机制，只冻结平台 security contract。OWASP 列表作为威胁入口，控制设计仍回到资产、主体、trust boundary 与生命周期。

Primary-source 与官方入口：

- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- OpenAI Privacy Filter model card:
  https://cdn.openai.com/pdf/c66281ed-b638-456a-8ce1-97e9f5264a90/OpenAI-Privacy-Filter-Model-Card.pdf
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- SLSA specification: https://slsa.dev/spec/v1.2/
- Kubernetes multi-tenancy/security: https://kubernetes.io/docs/concepts/security/
- Ethan Roland et al., "Modular Pretraining Enables Access Control", 2026（Status: Experimental）: https://alignment.anthropic.com/2026/modular-pretraining/
- Google Research, "Private prediction for large-scale synthetic text generation", 2025: https://arxiv.org/abs/2407.12108
- Google Research, "Fine-tuning LLMs with user-level differential privacy", 2025: https://research.google/blog/fine-tuning-llms-with-user-level-differential-privacy/
- JAX-Privacy 1.0: https://research.google/blog/differentially-private-machine-learning-at-scale-with-jax-privacy/
- Adaptive Text Anonymization（经验 attacker/utility Pareto；不提供 DP 保证；Status: Experimental）:
  https://arxiv.org/abs/2602.20743
- PromptGraph（关系感知的本地 sanitization 与 fail-closed restoration；Status: Experimental）：
  https://arxiv.org/abs/2607.10709v1
- IMMACULATE（probabilistic service-integrity audit；Status: Experimental）:
  https://arxiv.org/abs/2602.22700
- Integrity of peer-to-peer distributed LLM inference（exact v1；Status: Experimental）：https://arxiv.org/html/2607.19490v1
  - 证据边界：GPT-2/Pythia 小模型、408 个模拟配置、fp32 reference 对 fp16 live path 与 modeled Gaussian noise；低噪声 AUROC 不能外推 live heterogeneous pool 或 adaptive attacker。
- Agents of Chaos（cross-channel principal/policy/effect boundary；exploratory evidence）:
  https://arxiv.org/abs/2602.20021
- GateMem（multi-principal Memory utility/ACL/forgetting evaluation；Status: Experimental）:
  https://arxiv.org/abs/2606.18829
- Self-State Attacks on Self-Hosted AI Agents（self-state protection/recovery；Status: Experimental）:
  https://arxiv.org/abs/2607.17986
- Google Research, "Urania: Differentially Private Insights into AI Use", 2025: https://research.google/blog/a-differentially-private-framework-for-gaining-insights-into-ai-chatbot-use/
- OpenAI, "Research Preview of gpt-oss-safeguard", 2025:
  https://openai.com/index/introducing-gpt-oss-safeguard/
- MUSE（Status: Experimental；run-centric multimodal red-team）：
  https://arxiv.org/abs/2603.02482
- "Reasoning Models Struggle to Control their Chains of Thought"（Status: Experimental）：
  https://arxiv.org/abs/2603.05706
- CoT-Control official evaluation harness: https://github.com/YuehHanChen/CoTControl
- Faramesh（Status: Emerging；canonical action 与 effect-time authorization contract）:
  https://arxiv.org/abs/2601.17744
- Token-Level Capability Filtering（Status: Experimental；training-time loss/removal boundary）:
  https://arxiv.org/abs/2601.21571
- THINKSAFE（policy-generated safety data + independent guard；Status: Experimental）:
  https://arxiv.org/abs/2601.23143
- DeAction（off-task action detection and correction；Status: Experimental）:
  https://arxiv.org/abs/2602.08995
- SeerGuard（pre-execution semantic consequence sensor；Status: Experimental）:
  https://arxiv.org/abs/2607.15550
- BadWAM（imagination-preserving action attack；Status: Experimental）:
  https://arxiv.org/abs/2607.15207
- Anthropic, LLM-discovered 0-days（model-assisted discovery + executable reproduction + human disclosure；受限案例）:
  https://www.anthropic.com/research/zero-days
- OpenAI layered content provenance（C2PA + SynthID + public verifier；官方工程边界）:
  https://openai.com/index/advancing-content-provenance/

W32 primary-source cases：

- Formal Verification of Agentic Systems（Status: Experimental）: https://arxiv.org/abs/2608.03609
- SafeCommit（plausible-world action certification；Status: Experimental）: https://arxiv.org/abs/2608.04289
- Lights, Camera, Malfunction / ChromaGuard（robustness-versus-semantic-retention boundary；Status: Experimental）:
  https://arxiv.org/abs/2607.14698
- SafeFlow（跨委派 semantic provenance 与 irreversible-sink validation；Status: Experimental）:
  https://arxiv.org/abs/2607.25255v1

### Daily integration evidence trace

- `2026-05-02 / SF-ROUTEHIJACK-MOE-SAFETY-ROUTING` — exact-v1 `arXiv:2605.02946v1`；routing drift 只作为安全 sensor，输出 policy、authorization 与 safe commit 仍拥有最终权限。
- `2026-05-02 / SF-EMIA-RAG-CORPUS-MEMBERSHIP-INFERENCE` — exact-v1 `arXiv:2605.00955v1`；正文把 membership claim 绑定 retriever–generator 黑盒协议，不外推为任意 RAG 的泄漏率。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28649 — primary arXiv:2606.28649v1; exact-v1 URL=https://arxiv.org/html/2606.28649v1; Method=https://arxiv.org/html/2606.28649v1 — §II-C Security of ROS-Based Systems; III-A System Model; IV Methodology; Evaluation=https://arxiv.org/html/2606.28649v1 — §V Experimental Results; V-B Firewall Defense Evaluation; V-C Firewall Bypass Analysis; Non-proof=https://arxiv.org/html/2606.28649v1 — §III Threat Model; VI Discussion; VI-C The Sensory Vector as a Distinct Threat。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22827` — primary `arXiv:2606.22827v1`; Method=`arXiv:2606.22827v1 — §What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security; §2.3 Memory Analysis of Python; §5.3 Dependency Graph Construction`; Evaluation=`arXiv:2606.22827v1 — §2.3 Memory Analysis of Python; §5.3.1 Module Structure Analysis; §5.3.2 Bytecode Analysis`; non-proof=`arXiv:2606.22827v1 — §7 Limitations and Future Work; §8 Conclusion`; fallback=该 family 的 failure pressure 是：Modern software development relies heavily on third-party components from public repositories, expanding the software supply chain attack surface. 披露的 evaluation signal 是：In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22873` — primary `arXiv:2606.22873v1`; Method=`arXiv:2606.22873v1 — §2 Method; §2.3.3 Dynamic Rule Data Construction; §2.3.4 Chain-of-Thought Reasoning Data Construction`; Evaluation=`arXiv:2606.22873v1 — §3.2 Benchmark Composition and Statistics; §4.1 Evaluation Setup; §4.7 Dynamic Policy Evaluation`; non-proof=`arXiv:2606.22873v1 — §6 Conclusion; §C.4 Discussion`; fallback=该 family 的 failure pressure 是：This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. 披露的 evaluation signal 是：We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-22916` — primary `arXiv:2606.22916v1`; Method=`arXiv:2606.22916v1 — §I-A Relationship to OpenPort Protocol; §IV Threat Model; §IV-A System Boundary`; Evaluation=`arXiv:2606.22916v1 — §X Evaluation Design; §X-F Expected Analysis Without Fabricated Results; §X-I First-Batch External Benchmark Adaptation`; non-proof=`arXiv:2606.22916v1 — §IV-E Out of Scope; §XI Limitations and Threats to Validity; §XII-H Effect Estimation and Conservative Failure`; fallback=该 family 的 failure pressure 是：A trace-backed normalizer counterfactual removes this residual authority at substantial utility cost. 披露的 evaluation signal 是：We evaluate a reusable IGAC path over an OpenPort governance substrate using endpoint tests, 176 runtime-backed synthetic tasks, real-model classifier and planner pilots, 306 end-to-end model-task runtime trials, and a 36-trial benchmark-shaped external subset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23003` — primary `arXiv:2606.23003v1`; Method=`arXiv:2606.23003v1 — §VCT: A Verifiable Transcript System for LLM Conversations; §3.2 System State and Storage Model; §3.4 Threat Model and Security Goals`; Evaluation=`arXiv:2606.23003v1 — §4.4 Security Analysis; §5 Experimental Evaluation; §5.1 Prototype System and Evaluation Scope`; non-proof=`arXiv:2606.23003v1 — §5.1 Prototype System and Evaluation Scope; §5.8 Experimental Discussion; §6 Discussion and Future Work`; fallback=该 family 的 failure pressure 是：However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 披露的 evaluation signal 是：Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23277` — primary `arXiv:2606.23277v1`; Method=`arXiv:2606.23277v1 — §IV-B System Details; §V-B RQ2: How well does GIF detect policy violations with an LLM-as-a-declassifier design?`; Evaluation=`arXiv:2606.23277v1 — §III-C Operational Measurement of GIF; §V Evaluation; §V-C 2 Surrogate analysis models`; non-proof=`arXiv:2606.23277v1 — §VII Conclusion`; fallback=该 family 的 failure pressure 是：Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. 披露的 evaluation signal 是：Recent Information Flow Control (IFC)-based defenses show promise but lack a principled semantic foundation for reasoning about information flow through the model itself. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23416` — primary `arXiv:2606.23416v1`; Method=`arXiv:2606.23416v1 — §III Threat Model`; Evaluation=`arXiv:2606.23416v1 — §V-A 1 Locator evaluation`; non-proof=`arXiv:2606.23416v1 — §VI Discussion; §VII Conclusion`; fallback=该 family 的 failure pressure 是：A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. 披露的 evaluation signal 是：We release the resulting labeled dataset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-23969` — primary `arXiv:2606.23969v1`; Method=`arXiv:2606.23969v1 — §3 Platforms and Method; §4.1 Compute and GPU-Local Memory Are at Parity; §5.6 Runtime Design Rule`; Evaluation=`arXiv:2606.23969v1 — §3.3 Experiment Families; §5 Case Study: Policy Inversion in the Serving Runtime; §6 Case Study: Movement Engineering for Loading and KV State`; non-proof=`arXiv:2606.23969v1 — §3.4 Comparability and Claim Scope; §11 Conclusion`; fallback=该 family 的 failure pressure 是：We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 披露的 evaluation signal 是：We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24245: `arXiv:2606.24245v1`; exact-v1 URL=`https://arxiv.org/html/2606.24245v1`; Method=`https://arxiv.org/html/2606.24245v1 — §3 Overview; 4 Approach; ILP-Guided Predicate Learning`; Evaluation=`https://arxiv.org/html/2606.24245v1 — §5 Experimental Setup; 6 Evaluation`; Non-proof=`291 条 code/embodied trace 与 4–5 次迭代不证明稀疏、错误或对抗标注下收敛；发布前仍需 human approval、versioned rollback 与旧 expert rules 共存。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24322: `arXiv:2606.24322v1`; exact-v1 URL=`https://arxiv.org/html/2606.24322v1`; Method=`https://arxiv.org/html/2606.24322v1 — §II Threat Model; III TMA-NM; IV Formal Model`; Evaluation=`https://arxiv.org/html/2606.24322v1 — §V MEM-INV-Bench; VI Evaluation`; Non-proof=`保证依赖正确 origin labeling、独立 principal 与有限 TLA+ model；trusted tool compromise、隐式 value reconstruction、nested payload taint 和广泛真实任务仍未闭合。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24402: `arXiv:2606.24402v1`; exact-v1 URL=`https://arxiv.org/html/2606.24402v1`; Method=`https://arxiv.org/html/2606.24402v1 — §3 Problem Setting and Study Design; 5 Verification Boundary`; Evaluation=`https://arxiv.org/html/2606.24402v1 — §4 Poisoning Outcomes; 6 Generalization; 7 Mitigations`; Non-proof=`11 CTF、11 CVE、3 model family 下 prompt verification/multi-source retrieval 在 sparse-evidence 与 zero-day 会退化；不能把信息多数当独立真实性。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24408: `arXiv:2606.24408v1`; exact-v1 URL=`https://arxiv.org/html/2606.24408v1`; Method=`https://arxiv.org/html/2606.24408v1 — §3 Natural Identifiers; 4 DP Auditing; 5 Dataset Inference`; Evaluation=`https://arxiv.org/html/2606.24408v1 — §H DP-SGD Auditing; I/J/K Additional Evaluation`; Non-proof=`NID 可用性、独立性与 generator 正确性依赖数据域；黑盒可见性、重复 identifier、强 MIA 和 DP-SGD 配置变化会改变 sample complexity，不能当作逐样本法律证明。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24774: `arXiv:2606.24774v1`; exact-v1 URL=`https://arxiv.org/html/2606.24774v1`; Method=`https://arxiv.org/html/2606.24774v1 — §GradAudit gradient-slice and noise-masking methodology`; Evaluation=`https://arxiv.org/html/2606.24774v1 — §Seven pretraining/fine-tuning configurations; medical and general datasets`; Non-proof=`需要 white-box parameters 与 reference data；七个 VLM 配置、medical/general dataset 不证明黑盒 API、生成式泄漏或法律层面的逐样本归属。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-25189: `arXiv:2606.25189v1`; exact-v1 URL=`https://arxiv.org/html/2606.25189v1`; Method=`https://arxiv.org/html/2606.25189v1 — §3 Design; Policy DSL; Information-Flow Control`; Evaluation=`https://arxiv.org/html/2606.25189v1 — §5 Evaluation; Compliance; Macro/Micro Overhead`; Non-proof=`1.9%–8.4% overhead 与论文 policy/task 不证明所有 syscall、container/runtime 或 kernel version；DSL 生成错误时必须 fail closed、人工修订或回退传统 sandbox。`; Artifact=`https://github.com/eunomia-bpf/ActPlane`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25296**：Primary `arXiv:2606.25296v1`；Method `https://arxiv.org/html/2606.25296v1 — §SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation`；Evaluation `https://arxiv.org/html/2606.25296v1 — §Experimental Evaluation; Functional-Safety Case Studies`；未证明边界 `https://arxiv.org/html/2606.25296v1 — §Threats to Validity; Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25349**：Primary `arXiv:2606.25349v1`；Method `https://arxiv.org/html/2606.25349v1 — §IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation`；Evaluation `https://arxiv.org/html/2606.25349v1 — §VII Evaluation`；未证明边界 `https://arxiv.org/html/2606.25349v1 — §VIII Conclusion; exact-v1 analytical-evaluation-only note`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25366**：Primary `arXiv:2606.25366v1`；Method `https://arxiv.org/html/2606.25366v1 — §III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance`；Evaluation `https://arxiv.org/html/2606.25366v1 — §VIII Robustness; IX Integrated Evaluation`；未证明边界 `https://arxiv.org/html/2606.25366v1 — §XI-D Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25371**：Primary `arXiv:2606.25371v1`；Method `https://arxiv.org/html/2606.25371v1 — §III Problem Setup; IV Conformal Recovery-Deadline Certificate`；Evaluation `https://arxiv.org/html/2606.25371v1 — §V Experiments`；未证明边界 `https://arxiv.org/html/2606.25371v1 — §VI-D Limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25592**：Primary `arXiv:2606.25592v1`；Method `https://arxiv.org/html/2606.25592v1 — §2 Visual Prompt Attack and Defense; 2.2 VPA-Guard`；Evaluation `https://arxiv.org/html/2606.25592v1 — §3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments`；未证明边界 `https://arxiv.org/html/2606.25592v1 — §E.1 Limitations; E.4 Human-in-the-loop Discussion`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25721**：Primary `arXiv:2606.25721v1`；Method `https://arxiv.org/html/2606.25721v1 — §4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification`；Evaluation `https://arxiv.org/html/2606.25721v1 — §5 Evaluation; 5.1 Setup; 5.2 Results`；未证明边界 `https://arxiv.org/html/2606.25721v1 — §6 Discussion; baseline and hyperparameter sensitivity`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25863**：Primary `arXiv:2606.25863v1`；Method `https://arxiv.org/pdf/2606.25863v1 — §PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution`；Evaluation `https://arxiv.org/pdf/2606.25863v1 — §PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches`；未证明边界 `https://arxiv.org/pdf/2606.25863v1 — §PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26021**：Primary `arXiv:2606.26021v1`；Method `https://arxiv.org/html/2606.26021v1 — §V Attention-based MIA; VI Inference-Time Hardening Against MIAs`；Evaluation `https://arxiv.org/html/2606.26021v1 — §IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results`；未证明边界 `https://arxiv.org/html/2606.26021v1 — §VIII-C Limitations and opportunities; I Context size`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26028**：Primary `arXiv:2606.26028v1`；Method `https://arxiv.org/html/2606.26028v1 — §3 System Model: ERC-8004 Protocol; 7 Reputation Market Security`；Evaluation `https://arxiv.org/html/2606.26028v1 — §4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market`；未证明边界 `https://arxiv.org/html/2606.26028v1 — §9 Limitations and Future Work; C x402 attribution challenges`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26057**：Primary `arXiv:2606.26057v1`；Method `https://arxiv.org/html/2606.26057v1 — §2 Threat Model; 3 Requirements; 4 Design; 5 Implementation`；Evaluation `https://arxiv.org/html/2606.26057v1 — §6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment`；未证明边界 `https://arxiv.org/html/2606.26057v1 — §8.3 Limitations and Future Work; Artifact and Reproducibility`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26257**：Primary `arXiv:2606.26257v1`；Method `https://arxiv.org/html/2606.26257v1 — §Dataset Usage Inference formulation without shadow models or held-out data`；Evaluation `https://arxiv.org/html/2606.26257v1 — §Exact-v1 membership/dataset inference experiments and ablations`；未证明边界 `https://arxiv.org/html/2606.26257v1 — §Requires the paper's observable score/query regime; not per-record legal attribution`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26298**：Primary `arXiv:2606.26298v1`；Method `https://arxiv.org/html/2606.26298v1 — §Governing Actions, Not Agents; Institutional Attestation model`；Evaluation `https://arxiv.org/html/2606.26298v1 — §Action-level attestation scenarios and governance analysis`；未证明边界 `https://arxiv.org/html/2606.26298v1 — §Institutional model is a governance proposal, not a deployed enforcement benchmark`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26377**：Primary `arXiv:2606.26377v1`；Method `https://arxiv.org/html/2606.26377v1 — §Unified intent-and-harm verification defense`；Evaluation `https://arxiv.org/html/2606.26377v1 — §Threat-generation and defense evaluation`；未证明边界 `https://arxiv.org/html/2606.26377v1 — §Evaluated threat families and judges only; intent inference is not proof of harmless execution`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26479**：Primary `arXiv:2606.26479v1`；Method `https://arxiv.org/html/2606.26479v1 — §Out-of-band prompt-injection defenses organized as reference monitors and integrity policies`；Evaluation `https://arxiv.org/html/2606.26479v1 — §Adaptive evaluation methodology against policy-aware attackers`；未证明边界 `https://arxiv.org/html/2606.26479v1 — §Position/evaluation paper; static AgentDojo results do not establish adaptive robustness`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29581`；Method `https://arxiv.org/html/2606.29581v1 — §3 Methodology; quantization-temperature factorial design`；Evaluation `https://arxiv.org/html/2606.29581v1 — §3.1 Experimental Design; 4 Results`；未证明边界 `https://arxiv.org/html/2606.29581v1 — §5 Discussion`。

### Source-family integration record

<!-- daily-20260627:PLATFORM-SECURITY:start -->
### Owner-merged minimal durable delta

Robot middleware 会把 OCR、speech 与 range-derived state 序列化进高优先级 model context，因此 role label 不能建立信任。provenance 与 integrity check 必须沿 sensor data 经 middleware transformation 进入 prompt 的路径传播，并在 actuation 前保留 cross-modal consistency check 与 controller-side deny/hold path；未知或冲突的 sensory context 不得继承 system authority。

### Trade-off、failure、fallback 与 coexistence

证据只覆盖特定 ROS 2 transformation 与 attack，不覆盖所有 sensor/model；provenance 缺失或 modality 冲突时，在 action 前 fail closed。

<!-- daily-20260627:PLATFORM-SECURITY:end -->

<!-- recovered-daily-20260623:PLATFORM-SECURITY:start -->
### 2026-06-23 evidence integration — PLATFORM-SECURITY

相邻章 `books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22827**：What You See Is Not What You Execute: Memory-Based Runtime SBOM Generation for Supply Chain Security 的 exact-v1 机制为：In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 该 family 的 failure pressure 是：Modern software development relies heavily on third-party components from public repositories, expanding the software supply chain attack surface. 披露的 evaluation signal 是：In response to these growing risks, federal initiatives have advanced the Software Bill of Materials (SBOM) as a standardized mechanism for improving transparency by describing software components, dependencies, and their relationships. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-22873**：SingGuard: A Policy-Adaptive Multimodal LLM Guardrail with Dynamic Reasoning 的 exact-v1 机制为：We present \textbf{SingGuard}, a policy-adaptive multimodal guardrail model family for safety assessment in multimodal conversations. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 该 family 的 failure pressure 是：This broad deployment expands the safety surface: risks can arise from multimodal question answering, assistant responses, and cross-modal composition, while moderation policies may vary across products, regions, and deployment stages. 披露的 evaluation signal 是：We also introduce \textbf{SingGuard-Bench}, a multimodal guardrail benchmark with 56{,}340 examples spanning 80+ fine-grained risk types across multimodal QA, adversarial attack, and dynamic-rule evaluation settings, including cross-modal joint-risk cases where each modality is harmless in isolation but their composition implies unsafe intent. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-22916**：Intent-Governed Tool Authorization for AI Agents 的 exact-v1 机制为：We present Intent-Governed Access Control (IGAC), a server-side authorization layer that converts a trusted request into a short-lived intent certificate, narrows the statically authorized tool manifest, and checks proposed tool and payload effects before execution. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 该 family 的 failure pressure 是：A trace-backed normalizer counterfactual removes this residual authority at substantial utility cost. 披露的 evaluation signal 是：We evaluate a reusable IGAC path over an OpenPort governance substrate using endpoint tests, 176 runtime-backed synthetic tasks, real-model classifier and planner pilots, 306 end-to-end model-task runtime trials, and a 36-trial benchmark-shaped external subset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23003**：VCT: A Verifiable Transcript System for LLM Conversations 的 exact-v1 机制为：However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 该 family 的 failure pressure 是：However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. 披露的 evaluation signal 是：Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23277**：GIF: Locally Sound Geometric Information Flow Control for LLMs 的 exact-v1 机制为：We present Geometric Information Flow (GIF), a semantic framework for tracking information flow from input tokens to outputs. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 该 family 的 failure pressure 是：Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. 披露的 evaluation signal 是：Recent Information Flow Control (IFC)-based defenses show promise but lack a principled semantic foundation for reasoning about information flow through the model itself. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23416**：Detecting Malicious Agent Skills in the Wild using Attention 的 exact-v1 机制为：We present Locate-and-Judge, a two-stage detector designed for this regime. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 该 family 的 failure pressure 是：A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain foothold, which turns the skill marketplace into a new attack surface for agentic systems. 披露的 evaluation signal 是：We release the resulting labeled dataset. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-23969**：The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing 的 exact-v1 机制为：Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 该 family 的 failure pressure 是：We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 披露的 evaluation signal 是：We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:PLATFORM-SECURITY:end -->

<!-- recovered-daily-20260624:PLATFORM-SECURITY:start -->
### 2026-06-24 evidence integration — PLATFORM-SECURITY

相邻章 `books/part-06-ai-infrastructure/73-production-best-practice.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24245**：把静态 expert rule 的维护改为 annotation-driven CEGIS：trace evaluator 产出 FP/FN counterexample，ILP 选 discriminating predicate，candidate verifier 决定是否发布 rule revision。 291 条 code/embodied trace 与 4–5 次迭代不证明稀疏、错误或对抗标注下收敛；发布前仍需 human approval、versioned rollback 与旧 expert rules 共存。
- **SF-2026-ARXIV-2606-24322**：memory item 的行动权不再由可篡改 content/lineage 推断，而在 write 时绑定 origin authority；只有 k 个独立 trusted source 才 elevation，高风险 action 缺少 corroborator 时交给 one-time user confirmation。 保证依赖正确 origin labeling、独立 principal 与有限 TLA+ model；trusted tool compromise、隐式 value reconstruction、nested payload taint 和广泛真实任务仍未闭合。
- **SF-2026-ARXIV-2606-24402**：RAG 安全 gate 不再只问文档是否被检索，而按 local-artifact、model-knowledge、runtime-dependent 三层 verification boundary 决定 claim 能否进入行动；L3 需要动态探测或权威外部证据。 11 CTF、11 CVE、3 model family 下 prompt verification/multi-source retrieval 在 sparse-evidence 与 zero-day 会退化；不能把信息多数当独立真实性。
- **SF-2026-ARXIV-2606-24408**：利用训练数据自然出现且稀有的 identifier 作为 post-hoc audit unit，避免必须预埋 canary；auditor 分离 DP leakage 检查与 dataset inference，并记录 identifier cardinality/生成机制。 NID 可用性、独立性与 generator 正确性依赖数据域；黑盒可见性、重复 identifier、强 MIA 和 DP-SGD 配置变化会改变 sample complexity，不能当作逐样本法律证明。
- **SF-2026-ARXIV-2606-24774**：training-data audit 从 output entropy 转向 parameter-gradient signature；auditor 对跨模态 parameter slices 做稳定性/对齐特征，并用已知 train/non-train reference mask 掉不敏感维度。 需要 white-box parameters 与 reference data；七个 VLM 配置、medical/general dataset 不证明黑盒 API、生成式泄漏或法律层面的逐样本归属。
- **SF-2026-ARXIV-2606-25189**：policy context 留在 agent/harness，但 enforcement 下沉 OS kernel；IFC DSL 表达跨 event ordering/data-flow，eBPF 覆盖绕过 tool-call layer 的 system action，并返回 semantic denial。 1.9%–8.4% overhead 与论文 policy/task 不证明所有 syscall、container/runtime 或 kernel version；DSL 生成错误时必须 fail closed、人工修订或回退传统 sandbox。

<!-- recovered-daily-20260624:PLATFORM-SECURITY:end -->

<!-- recovered-daily-20260625:PLATFORM-SECURITY:start -->
### 2026-06-25 evidence integration — PLATFORM-SECURITY

- **SF-2026-ARXIV-2606-25296**：`SafeGen Methodology; Assertion Generation; Fault Criticality Evaluation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Threats to Validity; Limitations` 是 `SafeGen: LLM-Driven Assertion Generation and Fault Criticality Evaluation for Functional Safety` 的 source-specific 反例/局限边界；若运行条件离开 `Experimental Evaluation; Functional-Safety Case Studies` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25349**：`IV Two-Party Secure Inference Algorithm; V Storage-Communication Trade-off; VI Fused Relinearization and Rotation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `VIII Conclusion; exact-v1 analytical-evaluation-only note` 是 `General Techniques for Reducing Key-Switching Overhead in Privacy-Preserving Two-Party Transformer Inference` 的 source-specific 反例/局限边界；若运行条件离开 `VII Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25366**：`III System and Testbed; IV Verified Runtime Shield; VII Adaptation-Aware Runtime Assurance` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `XI-D Limitations` 是 `Reliability-Asymmetric Spacecraft Autonomy: Co-Designing a Capable Learned GNC Stack with a Verified, Adaptation-Aware Runtime Shield` 的 source-specific 反例/局限边界；若运行条件离开 `VIII Robustness; IX Integrated Evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25371**：`III Problem Setup; IV Conformal Recovery-Deadline Certificate` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `VI-D Limitations` 是 `Conformal Recovery-Deadline Certificates for Runtime Assurance of Adapting Controllers` 的 source-specific 反例/局限边界；若运行条件离开 `V Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25592**：`2 Visual Prompt Attack and Defense; 2.2 VPA-Guard` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `E.1 Limitations; E.4 Human-in-the-loop Discussion` 是 `VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks` 的 source-specific 反例/局限边界；若运行条件离开 `3 VVA-Bench; 3.2 Evaluation Protocol; 4 Main Experiments` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25721**：`4 Method; 4.1 Keyword Searching; 4.2 Secondary Verification` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `6 Discussion; baseline and hyperparameter sensitivity` 是 `Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution` 的 source-specific 反例/局限边界；若运行条件离开 `5 Evaluation; 5.1 Setup; 5.2 Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25863**：`PDF §3 Research Design; §3.3 PatchLens static analysis and build-system resolution` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `PDF threats to validity; compile-time C/C++ and project-specific build-resolver boundary` 是 `Automated Detection of Configuration-Specific Security Vulnerabilities via Patch Analysis` 的 source-specific 反例/局限边界；若运行条件离开 `PDF §4 Results; 1,192 Linux, 289 FFmpeg, 100 PHP patches` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26021**：`V Attention-based MIA; VI Inference-Time Hardening Against MIAs` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `VIII-C Limitations and opportunities; I Context size` 是 `Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries` 的 source-specific 反例/局限边界；若运行条件离开 `IV Tabular FMs Under Standard MIAs; V-B and VI-B Experimental Results` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26028**：`3 System Model: ERC-8004 Protocol; 7 Reputation Market Security` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `9 Limitations and Future Work; C x402 attribution challenges` 是 `Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem` 的 source-specific 反例/局限边界；若运行条件离开 `4 Dataset; 5 Agent Identity and Adoption; 6 Reputation Market` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26057**：`2 Threat Model; 3 Requirements; 4 Design; 5 Implementation` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `8.3 Limitations and Future Work; Artifact and Reproducibility` 是 `The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `6 Evaluation; 6.4 Machine-Checked Fail-Closed Invariant; 6.5 Live containment` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26257**：`Dataset Usage Inference formulation without shadow models or held-out data` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Requires the paper's observable score/query regime; not per-record legal attribution` 是 `Dataset Usage Inference without Shadow Models or Held-out Data` 的 source-specific 反例/局限边界；若运行条件离开 `Exact-v1 membership/dataset inference experiments and ablations` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26298**：`Governing Actions, Not Agents; Institutional Attestation model` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Institutional model is a governance proposal, not a deployed enforcement benchmark` 是 `Governing Actions, Not Agents: Institutional Attestation as a Governance Model for Autonomous AI Systems` 的 source-specific 反例/局限边界；若运行条件离开 `Action-level attestation scenarios and governance analysis` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26377**：`Unified intent-and-harm verification defense` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Evaluated threat families and judges only; intent inference is not proof of harmless execution` 是 `Verifying Intent and Harm: A Unified Defense Against LLM-Generated Threats` 的 source-specific 反例/局限边界；若运行条件离开 `Threat-generation and defense evaluation` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-26479**：`Out-of-band prompt-injection defenses organized as reference monitors and integrity policies` 所定义的源特定机制用于把威胁模型、策略判定、证明或 attestation 结果放在模型外控制平面并定义 fail-closed 边界；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `Position/evaluation paper; static AgentDojo results do not establish adaptive robustness` 是 `Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents` 的 source-specific 反例/局限边界；若运行条件离开 `Adaptive evaluation methodology against policy-aware attackers` 的验证域，`PLATFORM-SECURITY` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:PLATFORM-SECURITY:end -->

<!-- june29-owner:PLATFORM-SECURITY:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29581`）。** 现有 Security 正文有 threat matrix 与 fail-closed release，但未把 quantization precision、sampling temperature、multi-sample stability 与多 benchmark safety slice 联合成同一 release identity。 因此本次把这些增量合并到同一知识 owner：量化验收与 sampling temperature 不能分开：security release matrix 必须联合保存 model/quantization/sampler/multi-sample identity，并在多个 safety benchmark 上检查交互失稳。任一切片回归时回退已验收 precision/decoding 配置，而不是只恢复 greedy 单次测试。 共同代价与回退边界是：当前 official exact-v1 的 Abstract 与 §3 一致披露 9 models、161 configurations、AdvBench+XSTest 与约 322k responses；证据只覆盖以 Pile validation calibration 的 AWQ INT4/GPTQ INT8、2B–8B 模型与静态 AdvBench，未证明 NF4/GGUF/对抗式 calibration、>70B、adaptive jailbreak/prompt injection 或 judge 完美可靠。任一切片回归即恢复已验收 precision/sampler。

<!-- june29-owner:PLATFORM-SECURITY:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE:start -->
- `SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE` — Daily `2026-05-05`；primary `arXiv:2605.02187v1`；Books review `books-review:SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE`。

  **已吸收的语义增量：** BYOK 只认证调用资格，不能阻止 relay-side response tampering；provider-signed response envelope 是由该 threat model 推导出的待验证防御合同，论文 v1 未实现或评估该 defense，也不证明内容正确或安全。
<!-- daily-books-trace:SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE:end -->

<!-- daily-books-trace:SF-CONSENT-INTEGRITY:start -->
- `SF-CONSENT-INTEGRITY` — Daily `2026-06-02`；primary `arXiv:2606.02668v1`；Books review `books-review:SF-CONSENT-INTEGRITY`。

  **已吸收的语义增量：** 由 agent 自己撰写 approval summary 时，人批准的是可伪造 narration 而非真实 action。
<!-- daily-books-trace:SF-CONSENT-INTEGRITY:end -->

<!-- daily-books-trace:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:start -->
- `SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY` — Daily `2026-06-02`；primary `arXiv:2607.22569v1`；Books review `books-review:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY`。

  **已吸收的语义增量：** 把 filesystem/runtime side effect predicate 固化为 coding-agent release test，而非用 language refusal 代替。
<!-- daily-books-trace:SF-EXECUTION-GROUNDED-CODING-AGENT-SECURITY:end -->

<!-- daily-books-trace:SF-GHOST-TOOL-ISSUE-PRIVACY:start -->
- `SF-GHOST-TOOL-ISSUE-PRIVACY` — Daily `2026-06-02`；primary `arXiv:2606.02483v1`；Books review `books-review:SF-GHOST-TOOL-ISSUE-PRIVACY`。

  **已吸收的语义增量：** 增加 issue-time observation effect：外部调用发送即泄露，commit-time cleanup 不能撤回。
<!-- daily-books-trace:SF-GHOST-TOOL-ISSUE-PRIVACY:end -->

<!-- daily-books-trace:SF-SKILLHARM-LIFECYCLE:start -->
- `SF-SKILLHARM-LIFECYCLE` — Daily `2026-06-02`；primary `arXiv:2606.02540v1`；Books review `books-review:SF-SKILLHARM-LIFECYCLE`。

  **已吸收的语义增量：** 一次 session 的 poisoned skill 测试会漏掉 persistent package 被静默改写后在未来复用触发的 harm。
<!-- daily-books-trace:SF-SKILLHARM-LIFECYCLE:end -->

<!-- daily-books-trace:SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS:start -->
- `SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS` — Daily `2026-06-03`；primary `arXiv:2606.03381v1`；Books review `books-review:SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS`。

  **已吸收的语义增量：** §IV–V: distributed identities partition a global extraction query budget; the defense must correlate state above any one API key/IP, while the harness separates attack, defense and target-model components. Boundary: The experiment establishes failure of per-client state and fragility of naive global aggregation for this threat construction; it does not prove a production-ready identity-independent detector.
<!-- daily-books-trace:SF-AI-MODEL-EXTRACTION-ATTACKS-BYPASSING-SINGLE-CLIENT-ASSUMPTIONS:end -->

<!-- daily-books-trace:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:start -->
- `SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS` — Daily `2026-06-03`；primary `arXiv:2606.04071v1`；Books review `books-review:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS`。

  **已吸收的语义增量：** §3–4: a sender model can encode influence in apparently ordinary generated content consumed by a receiver, shifting provenance and trust ownership from human-visible text to the model-to-model channel. Boundary: The experiments demonstrate a model-to-model covert channel in tested settings; they do not establish prevalence in production or a complete detector.
<!-- daily-books-trace:SF-COVERT-INFLUENCE-BETWEEN-LANGUAGE-MODELS:end -->

<!-- daily-books-trace:SF-OVERLAYING-GOVERNANCE-COMPOSITIONAL-AUTHORIZATION-FRAMEWORK-DELEGATION-S:start -->
- `SF-OVERLAYING-GOVERNANCE-COMPOSITIONAL-AUTHORIZATION-FRAMEWORK-DELEGATION-S` — Daily `2026-06-03`；primary `arXiv:2606.03518v1`；Books review `books-review:SF-OVERLAYING-GOVERNANCE-COMPOSITIONAL-AUTHORIZATION-FRAMEWORK-DELEGATION-S`。

  **已吸收的语义增量：** Our model construction is guided by a single question: “Why is agent A A allowed to perform action X X on resource O O on behalf of user U U ?” To encode this reasoning, we introduce three families of relations: (i) delegation : who may act for whom; (ii) scope : under which contextual constraints a delegation is valid; and (iii) resource linkage : how human permissions lift to agents. We use OpenFGA syntax to present types and relations, focusing on the key relations for view / viewer ; additional permissions (e.g., editor ) follow analogously. We first model the principal entities: users and agents (agent’s syntax omitted for readability). Boundary: Agentic AI introduces a new operational model in which autonomous agents can act, reason, delegate, and collaborate with minimal human supervision. Such behavior challenges long-standing assumptions in IAM, where delegation is typically modeled as a static, token-mediated act. Modern agent ecosystems, however, require delegation and scoping to function as dynamic governance primitives that support continuous enforcement and auditability.
<!-- daily-books-trace:SF-OVERLAYING-GOVERNANCE-COMPOSITIONAL-AUTHORIZATION-FRAMEWORK-DELEGATION-S:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-04929:start -->
- `SF-2026-ARXIV-2606-04929` — Daily `2026-06-04`；primary `arXiv:2606.04929v1`；Books review `books-review:SF-2026-ARXIV-2606-04929`。

  **已吸收的语义增量：** 论文定义分别污染 SFT/preference datasets 的多攻击者 threat model，比较单阶段、分预算与协作 poison。dataset owners 持有阶段数据，checkpoint 传递隐藏状态，pipeline orchestrator 掌握阶段顺序和晋级。
<!-- daily-books-trace:SF-2026-ARXIV-2606-04929:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-05679:start -->
- `SF-2026-ARXIV-2606-05679` — Daily `2026-06-05`；primary `arXiv:2606.05679v1`；Books review `books-review:SF-2026-ARXIV-2606-05679`。

  **已吸收的语义增量：** Optimizer-invariant tuple-level provenance predicates move Agent data-release safety from prompts into the DBMS, giving the data plane enforcement ownership.
<!-- daily-books-trace:SF-2026-ARXIV-2606-05679:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-06697:start -->
- `SF-2026-ARXIV-2606-06697` — Daily `2026-06-05`；primary `arXiv:2606.06697v1`；Books review `books-review:SF-2026-ARXIV-2606-06697`。

  **已吸收的语义增量：** Virtualizing CUDA at a trusted worker and separating user from protected module/MMIO ranges moves context, handles and GPU-service state behind an OS-like protection boundary.
<!-- daily-books-trace:SF-2026-ARXIV-2606-06697:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07067:start -->
- `SF-2026-ARXIV-2606-07067` — Daily `2026-06-06`；primary `arXiv:2606.07067v1`；Books review `books-review:SF-2026-ARXIV-2606-07067`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07067:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07131:start -->
- `SF-2026-ARXIV-2606-07131` — Daily `2026-06-06`；primary `arXiv:2606.07131v1`；Books review `books-review:SF-2026-ARXIV-2606-07131`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07131:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07150:start -->
- `SF-2026-ARXIV-2606-07150` — Daily `2026-06-06`；primary `arXiv:2606.07150v1`；Books review `books-review:SF-2026-ARXIV-2606-07150`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07150:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07470:start -->
- `SF-2026-ARXIV-2606-07470` — Daily `2026-06-06`；primary `arXiv:2606.07470v1`；Books review `books-review:SF-2026-ARXIV-2606-07470`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07470:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07808:start -->
- `SF-2026-ARXIV-2606-07808` — Daily `2026-06-06`；primary `arXiv:2606.07808v1`；Books review `books-review:SF-2026-ARXIV-2606-07808`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07808:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07833:start -->
- `SF-2026-ARXIV-2606-07833` — Daily `2026-06-06`；primary `arXiv:2606.07833v1`；Books review `books-review:SF-2026-ARXIV-2606-07833`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07833:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07867:start -->
- `SF-2026-ARXIV-2606-07867` — Daily `2026-06-06`；primary `arXiv:2606.07867v1`；Books review `books-review:SF-2026-ARXIV-2606-07867`。

  **已吸收的语义增量：** Exact-v1 adds a source-specific mechanism and evaluation boundary not fully represented by the current owner proposition. The delta remains bounded by exact-v1 and does not transfer commit authority to an adjacent owner.
<!-- daily-books-trace:SF-2026-ARXIV-2606-07867:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08403:start -->
- `SF-2026-ARXIV-2606-08403` — Daily `2026-06-08`；primary `arXiv:2606.08403v1`；Books review `books-review:SF-2026-ARXIV-2606-08403`。

  **已吸收的语义增量：** 结构化浮点载体把恶意信号藏在原始文本视图之外，并在可信重建后才进入模型上下文，迫使安全 owner 同时校验 data layer 与 reconstruction layer。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08403:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-08539:start -->
- `SF-2026-ARXIV-2606-08539` — Daily `2026-06-08`；primary `arXiv:2606.08539v1`；Books review `books-review:SF-2026-ARXIV-2606-08539`。

  **已吸收的语义增量：** AgentTrust 按 lexical 与 semantic threat 分流 action decision，并让 allow/warn/block/escalate 的反馈进入可更新 judge，而不是扩张固定规则包。
<!-- daily-books-trace:SF-2026-ARXIV-2606-08539:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09935:start -->
- `SF-2026-ARXIV-2606-09935` — Daily `2026-06-08`；primary `arXiv:2606.09935v1`；Books review `books-review:SF-2026-ARXIV-2606-09935`。

  **已吸收的语义增量：** GitInject 把 issue、PR 与仓库文本中的 prompt injection 连到高权限 CI/CD agent，要求 untrusted content、repository permission 与 approval gate 分离。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09935:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09005:start -->
- `SF-2026-ARXIV-2606-09005` — Daily `2026-06-09`；primary `arXiv:2606.09005v1`；Books review `books-review:SF-2026-ARXIV-2606-09005`。

  **已吸收的语义增量：** RAG prompt assembly 必须把 document-authored metadata/provenance 视为 data 而非 policy，避免不可信文档在同一自然语言 channel 中冒充 control signal。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09005:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09084:start -->
- `SF-2026-ARXIV-2606-09084` — Daily `2026-06-09`；primary `arXiv:2606.09084v1`；Books review `books-review:SF-2026-ARXIV-2606-09084`。

  **已吸收的语义增量：** tool agent 的安全状态跨越多轮 artifact write/read；防御必须记录 artifact lineage 并在组合读取时执行 provenance-aware policy，不能只审核当前 turn。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09084:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-10724:start -->
- `SF-2026-ARXIV-2606-10724` — Daily `2026-06-10`；primary `arXiv:2606.10724v1`；Books review `books-review:SF-2026-ARXIV-2606-10724`。

  **已吸收的语义增量：** 在安全章节补一段 cluster ingress/egress 的独立证据面：passive taps 负责 commitment，secure gateway 负责 covert-channel sanitization；明确尚无部署验证。
<!-- daily-books-trace:SF-2026-ARXIV-2606-10724:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11632:start -->
- `SF-2026-ARXIV-2606-11632` — Daily `2026-06-11`；primary `arXiv:2606.11632v1`；Books review `books-review:SF-2026-ARXIV-2606-11632`。

  **已吸收的语义增量：** Agent proposal 必须编译为 typed contract，并绑定 evidence digest、policy/revocation epoch 与 scoped broker identity 后才可成为执行 authority。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11632:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11671:start -->
- `SF-2026-ARXIV-2606-11671` — Daily `2026-06-11`；primary `arXiv:2606.11671v1`；Books review `books-review:SF-2026-ARXIV-2606-11671`。

  **已吸收的语义增量：** Skill 安全不能只审静态文件；应按 capability profile 构造 targeted runtime context，在 sandbox 中执行并以 trace evidence 标注行为。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11671:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11871:start -->
- `SF-2026-ARXIV-2606-11871` — Daily `2026-06-11`；primary `arXiv:2606.11871v1`；Books review `books-review:SF-2026-ARXIV-2606-11871`。

  **已吸收的语义增量：** CUDA binary security 的 owner 是 executed SASS consumption site；protected-site CFI 必须恢复 site policy、验证 forward/backward transfer 并对 unsupported surface 显式出账。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11871:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11878:start -->
- `SF-2026-ARXIV-2606-11878` — Daily `2026-06-11`；primary `arXiv:2606.11878v1`；Books review `books-review:SF-2026-ARXIV-2606-11878`。

  **已吸收的语义增量：** GPU collective 的 mask、predicate、source lane、descriptor 与 epoch 是 authority-bearing non-control data；应在 collective 使用前绑定 membership/contribution/role/time。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11878:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11998:start -->
- `SF-2026-ARXIV-2606-11998` — Daily `2026-06-11`；primary `arXiv:2606.11998v1`；Books review `books-review:SF-2026-ARXIV-2606-11998`。

  **已吸收的语义增量：** trusted monitor 能力落后时，可用更强 untrusted monitor 评估 action，再让 weaker trusted model 监督其透明推理；control graph 要显式保存 collusion threat model。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11998:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12320:start -->
- `SF-2026-ARXIV-2606-12320` — Daily `2026-06-11`；primary `arXiv:2606.12320v1`；Books review `books-review:SF-2026-ARXIV-2606-12320`。

  **已吸收的语义增量：** 生产 Agent governance 应分 reasoning/network/identity/endpoint/data 五平面，并把 stop-anywhere mediation、capability attenuation、TTL 与 structured audit 组合为 cross-plane control。
<!-- daily-books-trace:SF-2026-ARXIV-2606-12320:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12703:start -->
- `SF-2026-ARXIV-2606-12703` — Daily `2026-06-11`；primary `arXiv:2606.12703v1`；Books review `books-review:SF-2026-ARXIV-2606-12703`。

  **已吸收的语义增量：** Persistent memory poisoning 的 certified boundary 必须在 write-time 做 cryptographic provenance，并在 query-time 对 authenticated adversary 做 randomized ablation 与 verdict aggregation。
<!-- daily-books-trace:SF-2026-ARXIV-2606-12703:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12737:start -->
- `SF-2026-ARXIV-2606-12737` — Daily `2026-06-11`；primary `arXiv:2606.12737v1`；Books review `books-review:SF-2026-ARXIV-2606-12737`。

  **已吸收的语义增量：** Prompt-injection red team 应从 attack-success search 扩为 source-aware test construction、feedback evolution、verification 与 localization，输出可修复 attack surface。
<!-- daily-books-trace:SF-2026-ARXIV-2606-12737:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14783:start -->
- `SF-2026-ARXIV-2606-14783` — Daily `2026-06-11`；primary `arXiv:2606.14783v1`；Books review `books-review:SF-2026-ARXIV-2606-14783`。

  **已吸收的语义增量：** Encoder-free VLM 的 visual tokens 与 layer-0 KV 可能成为 output filter 之前的可逆 privacy side channel；architecture 与 cache access 必须进入 threat model。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14783:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12797:start -->
- `SF-2026-ARXIV-2606-12797` — Daily `2026-06-12`；primary `arXiv:2606.12797v1`；Books review `books-review:SF-2026-ARXIV-2606-12797`。

  **已吸收的语义增量：** containment 必须在 perception/reasoning/execution/memory 边界分别绑定 validated write、policy gate 与 runtime monitor，而不能从 framework availability 推断 secure-by-default
<!-- daily-books-trace:SF-2026-ARXIV-2606-12797:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12918:start -->
- `SF-2026-ARXIV-2606-12918` — Daily `2026-06-12`；primary `arXiv:2606.12918v1`；Books review `books-review:SF-2026-ARXIV-2606-12918`。

  **已吸收的语义增量：** 多 Agent red-team 要把 agent marginal safety contribution、coalition selection 与 role-aware collusive perturbation纳入同一 closed loop
<!-- daily-books-trace:SF-2026-ARXIV-2606-12918:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13610:start -->
- `SF-2026-ARXIV-2606-13610` — Daily `2026-06-12`；primary `arXiv:2606.13610v1`；Books review `books-review:SF-2026-ARXIV-2606-13610`。

  **已吸收的语义增量：** web-connected Agent 的安全评测必须冻结污染时间线与 attacker publishing budget，测量 retriever/index/reader 怎样把公开内容变成控制输入
<!-- daily-books-trace:SF-2026-ARXIV-2606-13610:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13621:start -->
- `SF-2026-ARXIV-2606-13621` — Daily `2026-06-12`；primary `arXiv:2606.13621v1`；Books review `books-review:SF-2026-ARXIV-2606-13621`。

  **已吸收的语义增量：** design-time shield 合成只能在显式 state/action model 与安全性质下给 defensibility proof；部署时必须保留 model-bound identity 与 uncovered-state fallback
<!-- daily-books-trace:SF-2026-ARXIV-2606-13621:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13757:start -->
- `SF-2026-ARXIV-2606-13757` — Daily `2026-06-12`；primary `arXiv:2606.13757v1`；Books review `books-review:SF-2026-ARXIV-2606-13757`。

  **已吸收的语义增量：** code-review Agent 的 release gate必须把 vulnerability-introducing diff与persuasive PR narrative组合测试，且approval不能直接成为merge authority
<!-- daily-books-trace:SF-2026-ARXIV-2606-13757:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13949:start -->
- `SF-2026-ARXIV-2606-13949` — Daily `2026-06-12`；primary `arXiv:2606.13949v1`；Books review `books-review:SF-2026-ARXIV-2606-13949`。

  **已吸收的语义增量：** UI Agent 的 observation 在离开设备前应由trusted local broker按sensitivity与task necessity执行keep/abstract/remove三态最小披露
<!-- daily-books-trace:SF-2026-ARXIV-2606-13949:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13994:start -->
- `SF-2026-ARXIV-2606-13994` — Daily `2026-06-12`；primary `arXiv:2606.13994v1`；Books review `books-review:SF-2026-ARXIV-2606-13994`。

  **已吸收的语义增量：** Agent safety gate必须跨 benign-looking subtask保存cumulative intent/state，并测试decomposition graph最终是否完成有害目标
<!-- daily-books-trace:SF-2026-ARXIV-2606-13994:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14027:start -->
- `SF-2026-ARXIV-2606-14027` — Daily `2026-06-13`；primary `arXiv:2606.14027v1`；Books review `books-review:SF-2026-ARXIV-2606-14027`。

  **已吸收的语义增量：** Agentic browser 的 origin policy 必须追踪 agent 读入数据的 origin label，在跨 origin 写入前由浏览器侧 detector 与 user confirmation gate 授权；传统 script-only SOP 不覆盖 agent 自身形成的数据通道。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14027:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14154:start -->
- `SF-2026-ARXIV-2606-14154` — Daily `2026-06-13`；primary `arXiv:2606.14154v1`；Books review `books-review:SF-2026-ARXIV-2606-14154`。

  **已吸收的语义增量：** Skill supply-chain audit 必须联合读取自然语言 SKILL.md 与可执行 code，因为两种模态可以分别无害、组合后才形成 payload；admission 需覆盖 13 类 cross-modal mutation 与 runtime effect。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14154:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14517:start -->
- `SF-2026-ARXIV-2606-14517` — Daily `2026-06-13`；primary `arXiv:2606.14517v1`；Books review `books-review:SF-2026-ARXIV-2606-14517`。

  **已吸收的语义增量：** Reasoning guardrail 也必须有 token/time/concurrency budget 与 fail-closed/fail-open policy；否则攻击者可让安全模型陷入长推理并通过共享 guardrail queue 放大为租户级 DoS。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14517:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-14518:start -->
- `SF-2026-ARXIV-2606-14518` — Daily `2026-06-13`；primary `arXiv:2606.14518v1`；Books review `books-review:SF-2026-ARXIV-2606-14518`。

  **已吸收的语义增量：** Machine-unlearning audit 在互不信任 owner/auditor 下必须显式记录 audit leakage budget；只查询模型行为的通用 audit 对 convex models 无法同时识别 insufficient unlearning 且不泄露 retained-set membership。
<!-- daily-books-trace:SF-2026-ARXIV-2606-14518:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15020:start -->
- `SF-2026-ARXIV-2606-15020` — Daily `2026-06-13`；primary `arXiv:2606.15020v1`；Books review `books-review:SF-2026-ARXIV-2606-15020`。

  **已吸收的语义增量：** Document ingestion 必须把 rendered view 与 extractor view作为两份可比较 evidence；PDF render/extract divergence要在进入 LLM context 前经 dual-view consistency与static screening gate。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15020:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15057:start -->
- `SF-2026-ARXIV-2606-15057` — Daily `2026-06-14`；primary `arXiv:2606.15057v1`；Books review `books-review:SF-2026-ARXIV-2606-15057`。

  **已吸收的语义增量：** IPI 防御的 release contract 必须包含对已部署 defense 自适应优化的黑盒攻击，并把 action-open 用户欠规格单列为结构性风险层。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15057:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15242:start -->
- `SF-2026-ARXIV-2606-15242` — Daily `2026-06-14`；primary `arXiv:2606.15242v1`；Books review `books-review:SF-2026-ARXIV-2606-15242`。

  **已吸收的语义增量：** Skill 安全单位应从孤立 artifact 扩到 activated composition path，显式跟踪 capability flow、trust transfer 与 authorization confusion 的 state change。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15242:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15308:start -->
- `SF-2026-ARXIV-2606-15308` — Daily `2026-06-14`；primary `arXiv:2606.15308v1`；Books review `books-review:SF-2026-ARXIV-2606-15308`。

  **已吸收的语义增量：** confidence-based model cascade 是可攻击的资源控制面：输入可被优化为强制 deferral，使昂贵模型被持续调用。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15308:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15441:start -->
- `SF-2026-ARXIV-2606-15441` — Daily `2026-06-14`；primary `arXiv:2606.15441v1`；Books review `books-review:SF-2026-ARXIV-2606-15441`。

  **已吸收的语义增量：** IPI defense 应在每次 tool output 上做 task-alignment reasoning，并用自适应 red-team diversity reward 构造训练分布。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15441:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15493:start -->
- `SF-2026-ARXIV-2606-15493` — Daily `2026-06-14`；primary `arXiv:2606.15493v1`；Books review `books-review:SF-2026-ARXIV-2606-15493`。

  **已吸收的语义增量：** 模型窃取评估不能把高 fidelity surrogate 等同部署等价；Rashomon set 的 ambiguity、discrepancy 与 fairness 必须单独报告。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15493:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19380:start -->
- `SF-2026-ARXIV-2606-19380` — Daily `2026-06-14`；primary `arXiv:2606.19380v1`；Books review `books-review:SF-2026-ARXIV-2606-19380`。

  **已吸收的语义增量：** coding-agent safety failure 应拆成 underspecification、capability error 与 harness error，并分别用 policy、classifier/immutability 与 context/tool control修复。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19380:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15549:start -->
- `SF-2026-ARXIV-2606-15549` — Daily `2026-06-15`；primary `arXiv:2606.15549v1`；Books review `books-review:SF-2026-ARXIV-2606-15549`。

  **已吸收的语义增量：** terminal Agent command gate不能把开放命令空间压成load-bearing denylist；应以operation/effect为policy对象并用sandbox side-effect validator验证candidate bypass
<!-- daily-books-trace:SF-2026-ARXIV-2606-15549:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15609:start -->
- `SF-2026-ARXIV-2606-15609` — Daily `2026-06-15`；primary `arXiv:2606.15609v1`；Books review `books-review:SF-2026-ARXIV-2606-15609`。

  **已吸收的语义增量：** Agent access control必须跨turn组合memory fragments并在retrieval/fusion时重建cumulative intent，不能只检查最终query
<!-- daily-books-trace:SF-2026-ARXIV-2606-15609:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15762:start -->
- `SF-2026-ARXIV-2606-15762` — Daily `2026-06-15`；primary `arXiv:2606.15762v1`；Books review `books-review:SF-2026-ARXIV-2606-15762`。

  **已吸收的语义增量：** stochastic code-review Agent release gate应报告identical-run repeatability并与deterministic SAST做互补覆盖，单次finding不是稳定证据
<!-- daily-books-trace:SF-2026-ARXIV-2606-15762:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15899:start -->
- `SF-2026-ARXIV-2606-15899` — Daily `2026-06-15`；primary `arXiv:2606.15899v1`；Books review `books-review:SF-2026-ARXIV-2606-15899`。

  **已吸收的语义增量：** open-source Agent skill release需按capability、data flow、permission、dependency与behavioral evidence多维审计，LLM judge只提供risk proposal
<!-- daily-books-trace:SF-2026-ARXIV-2606-15899:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16100:start -->
- `SF-2026-ARXIV-2606-16100` — Daily `2026-06-16`；primary `arXiv:2606.16100v1`；Books review `books-review:SF-2026-ARXIV-2606-16100`。

  **已吸收的语义增量：** 黑盒 model fingerprint 在 provider 可自适应微调时不是身份凭证；gateway 必须把 attested model/version、计费证据与 challenge rotation 分开
<!-- daily-books-trace:SF-2026-ARXIV-2606-16100:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16242:start -->
- `SF-2026-ARXIV-2606-16242` — Daily `2026-06-16`；primary `arXiv:2606.16242v1`；Books review `books-review:SF-2026-ARXIV-2606-16242`。

  **已吸收的语义增量：** rapid-response 防御本身必须接受自适应 poisoning：攻击者可利用更新窗口改变 detector 的后续决策，而非只逃逸一次静态分类
<!-- daily-books-trace:SF-2026-ARXIV-2606-16242:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16287:start -->
- `SF-2026-ARXIV-2606-16287` — Daily `2026-06-16`；primary `arXiv:2606.16287v1`；Books review `books-review:SF-2026-ARXIV-2606-16287`。

  **已吸收的语义增量：** Agent skill 审计必须覆盖安装后动态行为、trigger 与跨 skill composition；静态 manifest/代码扫描不能代表 runtime authority
<!-- daily-books-trace:SF-2026-ARXIV-2606-16287:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16352:start -->
- `SF-2026-ARXIV-2606-16352` — Daily `2026-06-16`；primary `arXiv:2606.16352v1`；Books review `books-review:SF-2026-ARXIV-2606-16352`。

  **已吸收的语义增量：** remote LLM serving 的 attention integrity 可由 TEE 验证 GPU 计算，并对 prefill pipeline 与超显存 decode KV 分区分别设计通信路径
<!-- daily-books-trace:SF-2026-ARXIV-2606-16352:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16461:start -->
- `SF-2026-ARXIV-2606-16461` — Daily `2026-06-16`；primary `arXiv:2606.16461v1`；Books review `books-review:SF-2026-ARXIV-2606-16461`。

  **已吸收的语义增量：** privacy-preserving LLM inference 若依赖 orthogonal symmetry，必须把 transform key、equivariance 假设与不受保护的 metadata/side channel 分开声明
<!-- daily-books-trace:SF-2026-ARXIV-2606-16461:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16519:start -->
- `SF-2026-ARXIV-2606-16519` — Daily `2026-06-16`；primary `arXiv:2606.16519v1`；Books review `books-review:SF-2026-ARXIV-2606-16519`。

  **已吸收的语义增量：** world model 的安全 gate 需要对 observation/action perturbation 与 rollout compounding 做 adversarial contract，平均 prediction loss 不能替代 closed-loop robustness
<!-- daily-books-trace:SF-2026-ARXIV-2606-16519:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16527:start -->
- `SF-2026-ARXIV-2606-16527` — Daily `2026-06-16`；primary `arXiv:2606.16527v1`；Books review `books-review:SF-2026-ARXIV-2606-16527`。

  **已吸收的语义增量：** black-box jailbreak defense 应先做结构一致性 verification，再由 semantic audit 判定残余风险，并保留拒绝/放行的可解释 fallback
<!-- daily-books-trace:SF-2026-ARXIV-2606-16527:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16751:start -->
- `SF-2026-ARXIV-2606-16751` — Daily `2026-06-16`；primary `arXiv:2606.16751v1`；Books review `books-review:SF-2026-ARXIV-2606-16751`。

  **已吸收的语义增量：** jailbreak red-team 应针对多类防御做自适应策略搜索并保存 query budget；对单一 guard 的成功率不代表组合防线失效
<!-- daily-books-trace:SF-2026-ARXIV-2606-16751:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16821:start -->
- `SF-2026-ARXIV-2606-16821` — Daily `2026-06-16`；primary `arXiv:2606.16821v1`；Books review `books-review:SF-2026-ARXIV-2606-16821`。

  **已吸收的语义增量：** search Agent 的 source endorsement 可被网页 framing 操纵；评测应冻结操纵面并分离 retrieval exposure、citation 与最终 endorsement
<!-- daily-books-trace:SF-2026-ARXIV-2606-16821:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16914:start -->
- `SF-2026-ARXIV-2606-16914` — Daily `2026-06-16`；primary `arXiv:2606.16914v1`；Books review `books-review:SF-2026-ARXIV-2606-16914`。

  **已吸收的语义增量：** reward hacking 可由可见 incentive wording 触发；training/evaluation 必须把任务效用与可见奖励线索做 counterfactual 分离
<!-- daily-books-trace:SF-2026-ARXIV-2606-16914:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17110:start -->
- `SF-2026-ARXIV-2606-17110` — Daily `2026-06-16`；primary `arXiv:2606.17110v1`；Books review `books-review:SF-2026-ARXIV-2606-17110`。

  **已吸收的语义增量：** 攻击者可通过 loss-landscape poisoning 使后续 fine-tuning 提取未见训练数据；data provenance 与 update admission 必须联合审计
<!-- daily-books-trace:SF-2026-ARXIV-2606-17110:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17114:start -->
- `SF-2026-ARXIV-2606-17114` — Daily `2026-06-16`；primary `arXiv:2606.17114v1`；Books review `books-review:SF-2026-ARXIV-2606-17114`。

  **已吸收的语义增量：** tool-using Agent 的 leakage test 必须覆盖 realistic secret placement、multi-step tool chain 与 observable side effect，而非只测最终文本
<!-- daily-books-trace:SF-2026-ARXIV-2606-17114:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17229:start -->
- `SF-2026-ARXIV-2606-17229` — Daily `2026-06-16`；primary `arXiv:2606.17229v1`；Books review `books-review:SF-2026-ARXIV-2606-17229`。

  **已吸收的语义增量：** deception monitor 可利用 residual rank conflict signature，但 probe 的 label-free/cross-domain表现不能升级为 truth detector 或自动惩罚权
<!-- daily-books-trace:SF-2026-ARXIV-2606-17229:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17421:start -->
- `SF-2026-ARXIV-2606-17421` — Daily `2026-06-17`；primary `arXiv:2606.17421v1`；Books review `books-review:SF-2026-ARXIV-2606-17421`。

  **已吸收的语义增量：** 机密推理不能把 TEE 与 FHE 当互斥标签；应按算子泄漏面、密文代价与 PD 数据路径划分 trust boundary，并记录跨边界转换和 fallback。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17421:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17533:start -->
- `SF-2026-ARXIV-2606-17533` — Daily `2026-06-17`；primary `arXiv:2606.17533v1`；Books review `books-review:SF-2026-ARXIV-2606-17533`。

  **已吸收的语义增量：** Sandbox secure egress 必须把 workload-local eBPF filter、GENEVE overlay、独立 egress proxy、bandwidth/connection/port limits 与双层 policy integrity 串成数据面。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17533:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18198:start -->
- `SF-2026-ARXIV-2606-18198` — Daily `2026-06-17`；primary `arXiv:2606.18198v1`；Books review `books-review:SF-2026-ARXIV-2606-18198`。

  **已吸收的语义增量：** Skill scanner 必须把 docs/code/resources/visual layers 与 execution simulation联结，因视觉隐藏指令可绕过纯文本/静态扫描后影响运行行为。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18198:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18400:start -->
- `SF-2026-ARXIV-2606-18400` — Daily `2026-06-17`；primary `arXiv:2606.18400v1`；Books review `books-review:SF-2026-ARXIV-2606-18400`。

  **已吸收的语义增量：** 共享 GPU 上的模型权重保护可在 PCIe traffic、weight order 与 HBM physical page 三层破坏可重建 regularity，同时保留 authorized virtual layout；这是 cost-imposition 而非 secrecy proof。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18400:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18532:start -->
- `SF-2026-ARXIV-2606-18532` — Daily `2026-06-17`；primary `arXiv:2606.18532v1`；Books review `books-review:SF-2026-ARXIV-2606-18532`。

  **已吸收的语义增量：** AI sandbox 应以 threat model和 weakest-link evidence评估 fidelity、controllability、observability、containment、reproducibility与governance，不能把“进程在容器里”当成安全证明。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18532:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18550:start -->
- `SF-2026-ARXIV-2606-18550` — Daily `2026-06-17`；primary `arXiv:2606.18550v1`；Books review `books-review:SF-2026-ARXIV-2606-18550`。

  **已吸收的语义增量：** Tool safety gate依赖 contract integrity；应对 precondition/effect/risk/authorization字段做 signed provenance、typed attestation与runtime effect verification，且 effect字段比risk标签更load-bearing。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18550:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19390:start -->
- `SF-2026-ARXIV-2606-19390` — Daily `2026-06-17`；primary `arXiv:2606.19390v1`；Books review `books-review:SF-2026-ARXIV-2606-19390`。

  **已吸收的语义增量：** Agentic advisory automation需把 AIBOM/SBOM、runtime activation evidence、signed CSAF-VEX与replay bundle连成同一漏洞处置链，不能仅按静态依赖宣告 affected/not affected。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19390:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18619:start -->
- `SF-2026-ARXIV-2606-18619` — Daily `2026-06-18`；primary `arXiv:2606.18619v1`；Books review `books-review:SF-2026-ARXIV-2606-18619`。

  **已吸收的语义增量：** Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18619:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19535:start -->
- `SF-2026-ARXIV-2606-19535` — Daily `2026-06-18`；primary `arXiv:2606.19535v1`；Books review `books-review:SF-2026-ARXIV-2606-19535`。

  **已吸收的语义增量：** model artifact identity 必须绑定 serving platform/kernel；FloatDoor 通过两个 LoRA 放大 floating-point divergence 并把 platform signature 绑定恶意 task，暴露 audit/serve TOCTOU。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19535:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-19803:start -->
- `SF-2026-ARXIV-2606-19803` — Daily `2026-06-19`；primary `arXiv:2606.19803v1`；Books review `books-review:SF-2026-ARXIV-2606-19803`。

  **已吸收的语义增量：** `Policy-aware Vector Search: A Vision for Fine Grained Access Control in Vector Databases` 路由到 `PLATFORM-SECURITY`：向量检索不再先 ANN 后应用层过滤，而把 subject/object/policy 与 approximate candidate generation 共同求解；policy engine 拥有可见集合，ANN 只在授权候选内优化 recall/latency。pre/post-filter 可作为规模与索引能力不同的共存路径，但必须分别报告漏检和越权风险。
<!-- daily-books-trace:SF-2026-ARXIV-2606-19803:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20254:start -->
- `SF-2026-ARXIV-2606-20254` — Daily `2026-06-19`；primary `arXiv:2606.20254v1`；Books review `books-review:SF-2026-ARXIV-2606-20254`。

  **已吸收的语义增量：** `Quantization as a Malicious Task: Removing Quantization-Conditioned Backdoors via Task Arithmetic` 路由到 `PLATFORM-SECURITY`：量化不再被当作纯压缩步骤：security owner 将 quantization-conditioned backdoor 视作可分离 task vector，在发布前比较全精度/量化行为并用 task arithmetic 移除，再做 clean/attack 双验收。无法分离时回退到拒绝量化模型。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20254:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20470:start -->
- `SF-2026-ARXIV-2606-20470` — Daily `2026-06-19`；primary `arXiv:2606.20470v1`；Books review `books-review:SF-2026-ARXIV-2606-20470`。

  **已吸收的语义增量：** `Analyzing Defensive Misdirection Against Model-Guided Automated Attacks on Agentic AI Systems` 路由到 `PLATFORM-SECURITY`：防御不只阻断 model-guided attacker，还可发布受控假信号改变攻击者 belief/update path；defender 拥有 decoy 状态与撤销，真实 agent state 不暴露。代价是误导污染 observability 与合法调试，故必须与直接拒绝、隔离和审计共存。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20470:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20520:start -->
- `SF-2026-ARXIV-2606-20520` — Daily `2026-06-19`；primary `arXiv:2606.20520v1`；Books review `books-review:SF-2026-ARXIV-2606-20520`。

  **已吸收的语义增量：** `Sovereign Execution Broker: Enforcing Certificate-Bound Authority in Agentic Control Planes` 路由到 `PLATFORM-SECURITY`：Sovereign Execution Broker 将 prompt 声明的权限替换为 certificate-bound authority：principal 提交带 scope/expiry 的证书，broker 在工具执行前验证、记录并可 revoke；agent 不持有最终执行权。证书/身份漂移时 fail closed，并与人工 break-glass 共存。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20520:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20553:start -->
- `SF-2026-ARXIV-2606-20553` — Daily `2026-06-19`；primary `arXiv:2606.20553v1`；Books review `books-review:SF-2026-ARXIV-2606-20553`。

  **已吸收的语义增量：** `From Efficiency to Leakage -- Privacy Backdoor in Federated Language Model Fine-Tuning` 路由到 `PLATFORM-SECURITY`：联邦微调的效率路径被证明可承载 privacy backdoor；release contract 因此要在 client update 聚合前后检测泄漏触发与 utility，并由 server 持有 quarantine/rollback。安全聚合与效率优化需和隐私 red-team 共存。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20553:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20910:start -->
- `SF-2026-ARXIV-2606-20910` — Daily `2026-06-19`；primary `arXiv:2606.20910v1`；Books review `books-review:SF-2026-ARXIV-2606-20910`。

  **已吸收的语义增量：** `Whose Agent Are You? Multi-Layer Fingerprinting and Attribution of Autonomous Web Agents` 路由到 `PLATFORM-SECURITY`：MARK 将 web-agent attribution 从 robots.txt/单层 bot flag 改为 TLS/HTTP 与 browser-action 多层 fingerprint，site policy engine 根据 attribution 决定 throttle/challenge；classifier 漂移时回退行为限流而非永久身份结论。代价是隐私、误报和可规避性。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20910:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21037:start -->
- `SF-2026-ARXIV-2606-21037` — Daily `2026-06-20`；primary `arXiv:2606.21037v1`；Books review `books-review:SF-2026-ARXIV-2606-21037`。

  **已吸收的语义增量：** LLM attacker 与人类 attacker 的 deception response 不同，security evaluation 必须把 attacker class、trap recognition 与实际 exploit action 分开记录
<!-- daily-books-trace:SF-2026-ARXIV-2606-21037:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21045:start -->
- `SF-2026-ARXIV-2606-21045` — Daily `2026-06-20`；primary `arXiv:2606.21045v1`；Books review `books-review:SF-2026-ARXIV-2606-21045`。

  **已吸收的语义增量：** 训练完整性可以由连续 gradient-signal challenge 做 optimistic verification，但 verifier 必须拥有 challenge identity、容忍区间与失败升级路径
<!-- daily-books-trace:SF-2026-ARXIV-2606-21045:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21077:start -->
- `SF-2026-ARXIV-2606-21077` — Daily `2026-06-20`；primary `arXiv:2606.21077v1`；Books review `books-review:SF-2026-ARXIV-2606-21077`。

  **已吸收的语义增量：** 黑盒 Agent red-team 可用可迁移 observation/action perturbation 搜索 failure trajectory，但 attack generator 不能取得生产执行权
<!-- daily-books-trace:SF-2026-ARXIV-2606-21077:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21129:start -->
- `SF-2026-ARXIV-2606-21129` — Daily `2026-06-20`；primary `arXiv:2606.21129v1`；Books review `books-review:SF-2026-ARXIV-2606-21129`。

  **已吸收的语义增量：** Intent ABI 应把用户意图、capability grant 与 effect-time authorization 编译成可验证接口，而不是把自然语言意图直接当权限
<!-- daily-books-trace:SF-2026-ARXIV-2606-21129:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21172:start -->
- `SF-2026-ARXIV-2606-21172` — Daily `2026-06-20`；primary `arXiv:2606.21172v1`；Books review `books-review:SF-2026-ARXIV-2606-21172`。

  **已吸收的语义增量：** video/world-model poisoning 需要按 poison rate、trigger persistence 与 downstream action effect 验收，干净集精度不能覆盖后门风险
<!-- daily-books-trace:SF-2026-ARXIV-2606-21172:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21282:start -->
- `SF-2026-ARXIV-2606-21282` — Daily `2026-06-20`；primary `arXiv:2606.21282v1`；Books review `books-review:SF-2026-ARXIV-2606-21282`。

  **已吸收的语义增量：** DNN global robustness 是输入对的 2-safety property；differential halo zonotope 联合传播两条执行并界定 divergence，而非重复 local ball 检查
<!-- daily-books-trace:SF-2026-ARXIV-2606-21282:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21338:start -->
- `SF-2026-ARXIV-2606-21338` — Daily `2026-06-20`；primary `arXiv:2606.21338v1`；Books review `books-review:SF-2026-ARXIV-2606-21338`。

  **已吸收的语义增量：** MCP tool chain 的 privacy audit 需要跨参数、返回值与后续调用做 taint propagation，单调用 schema scan 会漏掉组合泄露
<!-- daily-books-trace:SF-2026-ARXIV-2606-21338:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21638:start -->
- `SF-2026-ARXIV-2606-21638` — Daily `2026-06-20`；primary `arXiv:2606.21638v1`；Books review `books-review:SF-2026-ARXIV-2606-21638`。

  **已吸收的语义增量：** tiered language-model service 应按 capability/risk 分离模型与权限；成本路由不能让弱安全模型获得强 effect authority
<!-- daily-books-trace:SF-2026-ARXIV-2606-21638:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21710:start -->
- `SF-2026-ARXIV-2606-21710` — Daily `2026-06-20`；primary `arXiv:2606.21710v1`；Books review `books-review:SF-2026-ARXIV-2606-21710`。

  **已吸收的语义增量：** 社会行为安全评估必须绑定场景、规范、judge 与 policy optimization，合成 reward 改善不证明真实人群规范覆盖
<!-- daily-books-trace:SF-2026-ARXIV-2606-21710:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21732:start -->
- `SF-2026-ARXIV-2606-21732` — Daily `2026-06-20`；primary `arXiv:2606.21732v1`；Books review `books-review:SF-2026-ARXIV-2606-21732`。

  **已吸收的语义增量：** 对 Agent/system 的组合攻击要显式建模 attacker capability、可见状态与 defense boundary；单点 sanitize 不等于 end-to-end containment
<!-- daily-books-trace:SF-2026-ARXIV-2606-21732:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-05029:start -->
- `SF-2026-ARXIV-2607-05029` — Daily `2026-07-07`；primary `arXiv:2607.05029v1`；Books review `books-review:SF-2026-ARXIV-2607-05029`。

  **已吸收的语义增量：** 新增证据边界：An attacker writes persistent memory entries that imitate a trusted reasoning trace and claim a safety check or prerequisite was already completed. Repetition creates correlated descendants, so majority/consensus logic may count one forged origin as apparently repeated support. SENTINEL layers lexical, provenance/taint, risk-pattern and reasoning checks, but its own ablation makes the Reasoning Guard load-bearing and the limitations show adaptive paraphrase can evade it. Project inference for the durable system contract: the memory store owns untrusted persisted claims and provenance; a security policy owns taint/risk routing; only the authoritative tool/environment/effect receipt can own whether an action actually completed. Read-time voting should collapse descendants sharing one provenance family before counting evidence. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L451`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-05029:end -->

<!-- daily-books-trace:SF-2026-ATTNLOCATE:start -->
- `SF-2026-ATTNLOCATE` — Daily `2026-08-26`；primary `arXiv:2608.24022v1`；Books review `books-review:SF-2026-ATTNLOCATE`。

  **已吸收的语义增量：** 新增 influence locator → authority registry → deterministic policy，明确 attention 不是因果或授权。
<!-- daily-books-trace:SF-2026-ATTNLOCATE:end -->

<!-- daily-books-trace:SF-2026-RAGSENTINEL:start -->
- `SF-2026-RAGSENTINEL` — Daily `2026-08-26`；primary `arXiv:2608.23965v1`；Books review `books-review:SF-2026-RAGSENTINEL`。

  **已吸收的语义增量：** 将 honest-majority retrieval sensor 放到 influence locator 与 authority adjudication 之前，并保留多数污染 failure mode。
<!-- daily-books-trace:SF-2026-RAGSENTINEL:end -->

<!-- daily-books-trace:SF-2026-STEPGUARD:start -->
- `SF-2026-STEPGUARD` — Daily `2026-08-26`；primary `arXiv:2608.24777v1`；Books review `books-review:SF-2026-STEPGUARD`。

  **已吸收的语义增量：** 将 learned safety/utility sensor 接入分层 authority chain，并保留 synthetic bias 和 false reject。
<!-- daily-books-trace:SF-2026-STEPGUARD:end -->

<!-- daily-books-trace:SF-2026-OPENAI-HF-INCIDENT:start -->
- `SF-2026-OPENAI-HF-INCIDENT` — Daily `2026-08-27`；primary `release:openai-hf-incident-2026-08-26`；Books review `books-review:SF-2026-OPENAI-HF-INCIDENT`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：把 environment containment、least privilege、secret boundary 和 independent monitoring 作为评测合同，而不是只约束 prompt；并保留边界：只能证明该次披露的链路与控制缺口；修复效果、其他模型与生产环境发生率未公开。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L47。前者拥有 tenant identity，后者拥有 release gate；二者均不拥有 evaluation sandbox 的 capability containment。
<!-- daily-books-trace:SF-2026-OPENAI-HF-INCIDENT:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-07943:start -->
- `SF-2026-ARXIV-2606-07943` — Daily `2026-06-07`；primary `arXiv:2606.07943v1`；Books review `books-review:SF-2026-ARXIV-2606-07943`。

  **已吸收的语义增量：** Postcondition-validated payload execution jointly with legitimate-task success changes skill-poisoning evidence from invocation to completed side effect, while position controls stealth and reliability. 只补这一条机制、non-proof 与旧路径共存边界。
<!-- daily-books-trace:SF-2026-ARXIV-2606-07943:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21877:start -->
- `SF-2026-ARXIV-2606-21877` — Daily `2026-06-21`；primary `arXiv:2606.21877v1`；Books review `books-review:SF-2026-ARXIV-2606-21877`。

  **已吸收的语义增量：** AgentRiskBOM 在 SBOM/AIBOM/MLBOM 之外声明 autonomy、tool permission、memory、credential scope、approval gate、audit signal、inter-agent channel 与 external action，并对 release mutation 做 diff。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21877:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22019:start -->
- `SF-2026-ARXIV-2606-22019` — Daily `2026-06-21`；primary `arXiv:2606.22019v1`；Books review `books-review:SF-2026-ARXIV-2606-22019`。

  **已吸收的语义增量：** subliminal-learning audit 不能只看 representation 是否线性可分；只有 signal 所在 channel 与审计 probe 的 initialization/alignment 匹配时，训练前 detector 才有权解释。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22019:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22263:start -->
- `SF-2026-ARXIV-2606-22263` — Daily `2026-06-21`；primary `arXiv:2606.22263v1`；Books review `books-review:SF-2026-ARXIV-2606-22263`。

  **已吸收的语义增量：** Revelio 让廉价 LLM/static analysis 只生成和排序 vulnerability hypothesis，最终必须提交 executable Proof-of-Vulnerability 并由 deterministic sanitizer 复现后才报告。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22263:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10709:start -->
- `SF-2026-ARXIV-2607-10709` — Daily `2026-07-13`；primary `arXiv:2607.10709v1`；Books review `books-review:SF-2026-ARXIV-2607-10709`。

  **已吸收的语义增量：** 新增证据边界：Move prompt privacy from independent PII-span masking to a client-owned graph that estimates contextual attribute leakage and pairwise utility dependencies, selects a privacy/utility cut, sends opaque placeholders, and restores only exact consistency-checked identifiers locally. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L83`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10709:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14698:start -->
- `SF-2026-ARXIV-2607-14698` — Daily `2026-07-17`；primary `arXiv:2607.14698v1`；Books review `books-review:SF-2026-ARXIV-2607-14698`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: broad color augmentation -> invariant-feature collapse diagnosis -> semantics-preserving perturbation training 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14698:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-19490:start -->
- `SF-2026-ARXIV-2607-19490` — Daily `2026-07-22`；primary `arXiv:2607.19490v1`；Books review `books-review:SF-2026-ARXIV-2607-19490`。

  **已吸收的语义增量：** 新增证据边界：The verifier interleaves indistinguishable known-answer canaries, stores clean fp32 intermediate activations, measures per-shard relative-L2 mismatch against live fp16 activations and ranks shards by per-canary AUROC rather than relying on one universal threshold. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-19490:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-19957:start -->
- `SF-2026-ARXIV-2607-19957` — Daily `2026-07-23`；primary `arXiv:2607.19957v1`；Books review `books-review:SF-2026-ARXIV-2607-19957`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: text/position cache hit -> causal-context provenance check -> tenant-scoped reuse or verified recomputation 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L732`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-19957:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-23532:start -->
- `SF-2026-ARXIV-2607-23532` — Daily `2026-07-27`；primary `arXiv:2607.23532v1`；Books review `books-review:SF-2026-ARXIV-2607-23532`。

  **已吸收的语义增量：** 新增证据边界：A three-tier L1/L2/L3 assurance fabric composes platform, squad and mission predicates over durable events; evidence gaps propagate as unknown instead of false all-clear. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L604`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-23532:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-23999:start -->
- `SF-2026-ARXIV-2607-23999` — Daily `2026-07-28`；primary `arXiv:2607.23999v1`；Books review `books-review:SF-2026-ARXIV-2607-23999`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: endpoint attack success -> run trace -> exposure/propagation/proposal/authorization/commit stages -> joint containment and authorized-utility evidence. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L261`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-23999:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24692:start -->
- `SF-2026-ARXIV-2607-24692` — Daily `2026-07-28`；primary `arXiv:2607.24692v1`；Books review `books-review:SF-2026-ARXIV-2607-24692`。

  **已吸收的语义增量：** 新增证据边界：Layering / Dependency: latency deadline as SLO -> deadline as merge/commit boundary -> shaped contention suppresses high-accuracy evidence -> availability protection must include semantic-quality residual risk. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L684`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24692:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25255:start -->
- `SF-2026-ARXIV-2607.25255` — Daily `2026-07-29`；primary `arXiv:2607.25255v1`；Books review `books-review:SF-2026-ARXIV-2607.25255`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: local prompt classification -> cross-agent semantic provenance -> sink-time workflow reconstruction -> deterministic pre-commit authorization. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25255:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.27267:start -->
- `SF-2026-ARXIV-2607.27267` — Daily `2026-07-30`；primary `arXiv:2607.27267v1`；Books review `books-review:SF-2026-ARXIV-2607.27267`。

  **已吸收的语义增量：** 新增证据边界：FAVA lowers LLM-derived permission intent into an intermediate representation, builds an evidence-backed permission graph and delegates decisions to a deterministic SMT authorizer at the gateway. This keeps the model as proposal owner, while policy completeness, evidence freshness and solver availability become explicit failure modes. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L566`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.27267:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28884:start -->
- `SF-2026-ARXIV-2607-28884` — Daily `2026-07-31`；primary `arXiv:2607.28884v1`；Books review `books-review:SF-2026-ARXIV-2607-28884`。

  **已吸收的语义增量：** 新增证据边界：Depth attack adds zero-work residual identities; width attack replicates coordinates with block-diagonal weights while preserving logits. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28884:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-29019:start -->
- `SF-2026-ARXIV-2607-29019` — Daily `2026-08-01`；primary `arXiv:2607.29019v1`；Books review `books-review:SF-2026-ARXIV-2607-29019`。

  **已吸收的语义增量：** GoldenRetriever 把加密检索从昂贵的 homomorphic top-k 排序改为 CKKS 上的阈值选择，并用七次 mask-polarization polynomial 把近似掩码收敛到可恢复离散 token 的精度。实验覆盖检索效果、延迟和规模变化，但 threat model 明确允许 retrieval server 持有明文 corpus，阈值还会改变返回集合大小；因此它证明的是该三方架构内的 query/selection privacy，不是端到端 RAG 保密。
<!-- daily-books-trace:SF-2026-ARXIV-2607-29019:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-29190:start -->
- `SF-2026-ARXIV-2607-29190` — Daily `2026-08-01`；primary `arXiv:2607.29190v1`；Books review `books-review:SF-2026-ARXIV-2607-29190`。

  **已吸收的语义增量：** CAGE 不再只对观测到的 typed tool return 做点式授权，而是枚举离散绑定邻域，并在每个分支上认证连续数值扰动；Exact、Lipschitz 与 randomized-smoothing 三层 backend 具有不同保证。实验覆盖 policy-as-code、监管和交易设置，但保证只针对一次 authorization decision，并依赖完整 mediation、正确 typed-return constructor、可枚举邻域与已校准预算；预算外逃逸不能被证书消除。
<!-- daily-books-trace:SF-2026-ARXIV-2607-29190:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-04289:start -->
- `SF-2026-ARXIV-2608-04289` — Daily `2026-08-05`；primary `arXiv:2608.04289v1`；Books review `books-review:SF-2026-ARXIV-2608-04289`。

  **已吸收的语义增量：** SafeCommit 在 reasoning 与有副作用执行之间维护 plausible latent-world set，只有当 conformal action certificate 对所有保留世界都判定安全时才 commit，否则选择低副作用 probe 或 fallback。受控 simulator 验证的是已校准 world coverage 下的边际风险界；固定动作集、确定性 probe、精确 safety map 与 exchangeability 都是强假设，错误 safety map 仍会认证危险动作，所以它不能替代授权、sandbox 与人工监督。
<!-- daily-books-trace:SF-2026-ARXIV-2608-04289:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-09225:start -->
- `SF-2026-ARXIV-2608-09225` — Daily `2026-08-11`；primary `arXiv:2608.09225v1`；Books review `books-review:SF-2026-ARXIV-2608-09225`。

  **已吸收的语义增量：** KVGov 把共享 prefix cache 的 timing signal 视为跨租户身份泄漏：以 principal-specific HMAC salt 分离 cache-key namespace，并用 background audit 观察 breach signal。作者在 vLLM/A100 与 llama.cpp/M4 两条不同栈上验证 channel 存在，但 boundary salting 的缓存收益来自外推，vLLM block-size 变化只关闭部分自由文本攻击；根隔离会牺牲跨租户共享，因此 namespace、principal identity 与 cache economics 必须共同设计。
<!-- daily-books-trace:SF-2026-ARXIV-2608-09225:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-16843:start -->
- `SF-2026-ARXIV-2608-16843` — Daily `2026-08-18`；primary `arXiv:2608.16843v1`；Books review `books-review:SF-2026-ARXIV-2608-16843`。

  **已吸收的语义增量：** 该综述按 first-compromised trust boundary，而不是按 jailbreak/backdoor 名称，对 embodied-agent 闭环中的供应链、输入、memory、感知、world state、planning、action、middleware 与 fleet communication 编码 attack/defense 记录。它提供的是研究密度与防御位置地图；多标签编码含判断，预印本状态会变化，论文数量不等于真实事故概率，因此不能据此给攻击风险排序。
<!-- daily-books-trace:SF-2026-ARXIV-2608-16843:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-17442:start -->
- `SF-2026-ARXIV-2608-17442` — Daily `2026-08-19`；primary `arXiv:2608.17442v1`；Books review `books-review:SF-2026-ARXIV-2608-17442`。

  **已吸收的语义增量：** FESC 把私有长上下文从 encrypted Transformer 的二次 attention 改造成 factorized encrypted scan-contract：线性计算留在 CKKS，SiLU/softplus/exp/RMSNorm 交给 MPC，compact transition 分块驻留并在 conversion 前 contraction。12 层 Mamba-base、三类长文分类和 A100 实测证明的是该 semi-honest 两方协议及近似训练下的可执行性；77.3 分钟并非交互服务级延迟，8192 token 还需要 secure carry refresh。
<!-- daily-books-trace:SF-2026-ARXIV-2608-17442:end -->

<!-- daily-books-trace:SF-2026-GIFT-IFC:start -->
- `SF-2026-GIFT-IFC` — Daily `2026-08-27`；primary `arXiv:2608.25431v1`；Books review `books-review:SF-2026-GIFT-IFC`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：CPU 侧以 per-user encryption 隔离内容，GPU 侧静态分析 kernel flow 并以 decoupled tracker 执行信息流规则；GIFT-CC 再覆盖不可信 OS/hypervisor；并保留边界：只覆盖已建模 kernel 与论文 threat model；新 kernel、side channel、硬件/并发细节和独立复现仍缺失。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L33;books/part-06-ai-infrastructure/73-production-best-practice.md#L47。Multi-tenant 只声明隔离平面，Production 只承接发布合同；kernel-level information-flow enforcement 属于 Security。
<!-- daily-books-trace:SF-2026-GIFT-IFC:end -->

<!-- daily-books-trace:SF-2026-GROUNDHOG-BITFLIP:start -->
- `SF-2026-GROUNDHOG-BITFLIP` — Daily `2026-08-27`；primary `arXiv:2608.25276v1`；Books review `books-review:SF-2026-GROUNDHOG-BITFLIP`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：定位与 EOS 等 token 强相关的 routing bits，破坏相关 expert 激活，使生成持续到 max-token 而尽量保持语义表面；并保留边界：是主动故障注入，不证明普通软错概率；硬件、精度、并发与线上检测 SLO 未完整披露。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L69;books/part-06-ai-infrastructure/73-production-best-practice.md#L91。前者只拥有 cache/serving 隔离，后者拥有容量与恢复；router 参数完整性与 fault-triggered output behavior 仍由 Security 拥有。
<!-- daily-books-trace:SF-2026-GROUNDHOG-BITFLIP:end -->

<!-- daily-books-trace:SF-2026-LMSM:start -->
- `SF-2026-LMSM` — Daily `2026-08-27`；primary `arXiv:2608.25697v1`；Books review `books-review:SF-2026-LMSM`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：把 calibrated evidence backend、versioned policy 和 independent buffered-output gate 分离，保持 request identity 穿过 continuous batching；并保留边界：learned backend 可能漂移且不能替代 reference monitor；结果只覆盖特定模型、规则和攻击集。 相邻章节对读：books/part-06-ai-infrastructure/71-multi-tenant.md#L90;books/part-06-ai-infrastructure/73-production-best-practice.md#L65。Tenant identity 和 readiness gate 只是输入合同；calibrated sensor 到 safe-commit enforcement 的控制权属于 Security。
<!-- daily-books-trace:SF-2026-LMSM:end -->

<!-- daily-books-trace:SF-2026-DAYDREAMING-SKILL-THEFT:start -->
- `SF-2026-DAYDREAMING-SKILL-THEFT` — Daily `2026-08-28`；primary `arXiv:2608.26733v1`；Books review `books-review:SF-2026-DAYDREAMING-SKILL-THEFT`。

  **已吸收的语义增量：** 补足不泄露文本也可行为重建的边界。
<!-- daily-books-trace:SF-2026-DAYDREAMING-SKILL-THEFT:end -->

<!-- daily-books-trace:SF-2026-LOOPHARNESS:start -->
- `SF-2026-LOOPHARNESS` — Daily `2026-08-28`；primary `arXiv:2608.27141v1`；Books review `books-review:SF-2026-LOOPHARNESS`。

  **已吸收的语义增量：** 补足跨 loop/session safety state 及显式 reset。
<!-- daily-books-trace:SF-2026-LOOPHARNESS:end -->
