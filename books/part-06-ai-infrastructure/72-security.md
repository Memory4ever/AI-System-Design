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

## Availability 与 Abuse

AI API 的 DoS 不只看 request count。超长 prompt、超大 output limit、expensive tool loops、adapter churn 和 cache-busting 都能放大成本。Gateway 与 runtime 应联合执行：

- body/context/output bounds；
- token/concurrency budgets；
- admission deadlines；
- per-tenant cost limits；
- tool-step limits；
- model/cache identity validation。

拒绝原因与 policy version 必须审计，以便区分攻击、误配置与容量不足。

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

## Review notes

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
- IMMACULATE（probabilistic service-integrity audit；Status: Experimental）:
  https://arxiv.org/abs/2602.22700
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
