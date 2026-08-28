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

## Supply-chain Integrity

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

### 局部合理动作会累积成有害轨迹

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

### Sensor Robustness 不能删除 Task-critical Semantics

对 lighting、color 或 texture 做强 augmentation，可能让 policy 在攻击条件下继续完成某些任务；若 benchmark 不要求区分这些属性，模型也可能通过完全忽略被扰动 channel 获得表面 robustness。于是 attack success 下降并不自动意味着 sensor representation 更可靠，它也可能意味着 task-critical semantics 被训练成 nuisance。

防御验收必须同时保留两个 matched 分支：`benign semantic counter-task` 检查颜色等特征在无攻击时仍可用于正确 action，`attacked closed-loop trajectory` 检查防御是否降低真实 deviation、collision 与 failure。只有二者同时成立，augmentation 才能升级为 robustness evidence；grayscale probe、feature attribution 或 learned judge 仍只是 sensor，真实 task outcome 与 safety controller 拥有最终判断。

这种 invariant 会增加数据和物理试验成本，也要求事先声明哪些 sensor feature 对任务有因果职责。静态 spotlight、有限 task 与单一机械臂结果不能覆盖时间变化照明、开放环境或自适应 attacker；因此规则 safety envelope、independent perception 与 fail-closed control 不会被 learned augmentation 取代。

## Availability 与 Abuse

AI API 的 DoS 不只看 request count。超长 prompt、超大 output limit、expensive tool loops、adapter churn 和 cache-busting 都能放大成本。Gateway 与 runtime 应联合执行：

- body/context/output bounds；
- token/concurrency budgets；
- admission deadlines；
- per-tenant cost limits；
- tool-step limits；
- model/cache identity validation。

拒绝原因与 policy version 必须审计，以便区分攻击、误配置与容量不足。

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

### 共享状态的性能身份同时也是安全身份

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

模型辅助漏洞研究也必须保持 proposal、reproduction 与 disclosure 分层。语义搜索可以从源码提出可疑 path，传统 fuzzing/static analysis 仍擅长高吞吐 coverage 与回归；只有在隔离环境中形成最小可执行 reproduction、去重已知漏洞并由人类完成 severity 与 responsible disclosure 后，candidate 才能升级为安全证据。公开若只有成功案例而没有扫描 denominator、false-positive 与修复接受率，不能据此推导自主漏洞发现成功率。

该 workflow 新增 exploit artifact 保管、dual-use access、maintainer burden 与 embargo lifecycle。Activation/risk probe 只能触发审查，不能判定恶意意图；模型也不能因为发现漏洞而获得发布、利用或修改生产系统的 authority。

NIST AI RMF 用 Govern、Map、Measure、Manage 组织持续风险管理。对平台而言：

- Govern：owner、policy、exception、accountability；
- Map：use case、assets、affected parties、threat model；
- Measure：evaluation、red team、monitoring、security tests；
- Manage：mitigation、release gate、incident、rollback。

安全控制会随模型能力、工具权限与业务后果变化，不能在平台上线前一次完成。

## 本章在知识树中的位置

本章横切 Part I～V，并为 Part VII 建立 action boundary。下一章将质量、SLO、成本、tenancy 和 security 收束为 production readiness，而不是把“部署成功”当成终点。

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

## 小结

AI security 必须贯穿数据、训练、artifact、serving 与 action。正确设计不依赖模型永远服从，而是让任何不可信输出都经过独立、最小权限、可审计的执行边界。

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

## Review notes

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
