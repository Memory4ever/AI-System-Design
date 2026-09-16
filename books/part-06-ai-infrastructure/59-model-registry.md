# 第59章 Model Registry

**Knowledge Tree:** Part VI AI Infrastructure：从工具到平台
**Stable Knowledge Node ID:** `PLATFORM-MODEL-REGISTRY`
**Legacy Chapter:** Ch55
**Status:** Draft

**Roadmap Intent:** 模型资产、版本、元数据和血缘管理。

## 本章要回答的问题

为什么把 checkpoint 放进 object storage 还不够？Model Registry 管理的是二进制文件、模型名字，还是一个可验证的部署承诺？

本章的核心判断是：**Registry 是模型身份与证据的索引。它把不可变 artifact、训练 lineage、评估结果、批准状态和部署引用绑定起来，但不替代 artifact store，也不主动编排 workload。**

## 文件路径不能承担模型身份

朴素方案常用：

```text
s3://models/team-a/llm/latest/
```

这里至少有四个不确定性：

- `latest` 是否发生过覆盖？
- 目录中是否同时包含 tokenizer、config、adapter 和 quantization metadata？
- 该产物来自哪次训练与哪份数据？
- 当前线上服务加载的是目录的哪个时间点？

第 35 章已经把 checkpoint 定义为可恢复、可转换的训练资产。进入平台后，还需要一个 deployment artifact contract，把 source checkpoint、转换过程和 runtime artifact 区分开。

## Registry 的逻辑模型

可以用以下关系理解：

```text
RegisteredModel
  └─ ModelVersion (immutable identity)
       ├─ artifact references + digests
       ├─ tokenizer / config / adapter identity
       ├─ source run and dataset lineage
       ├─ evaluation evidence
       ├─ compatibility metadata
       └─ deployment status / references

Alias or Channel (mutable pointer)
  └─ points to one ModelVersion
```

`ModelVersion` 应不可变；`candidate`、`champion`、`production` 等 alias 可以移动。若部署只记录 alias 而不解析并固化实际 version/digest，事后就无法重建行为。

## Identity 必须覆盖模型行为

对 LLM，单纯 weight digest 不够。可部署身份通常至少包含：

```text
model_identity =
  weights
  + architecture config
  + tokenizer and special tokens
  + chat template
  + adapters and merge order
  + quantization scheme and calibration
  + runtime compatibility contract
```

同一 checkpoint 配不同 tokenizer 或 chat template，logits 与行为会变化；同一 LoRA adapter 应用到错误 base model，shape 可能可加载但语义错误。Registry 必须能够表达这些组合关系。

文件身份无法解释的 drift，可以用版本化的行为指纹补充观测。例如在固定 structured-action / tool schema 下，
重复采样模型的类别策略，并用预先校准的统计检验与可信 reference 比较；这比自由文本相似度更少受措辞变化影响。
但 receipt 必须同时绑定 template 与 schema revision、hidden prompt、sampling configuration、query budget、reference
population、显著性阈值和测试实现。少任一项，都无法区分 model drift、wrapper change 与测量条件变化。

行为指纹是 revalidation trigger，不是权重、provider 或所有权证书。同一权重经过 wrapper 或低比特量化后可能被拒，
不同实现也可能在有限 probes 上碰巧通过；知道完整 probe 的服务方还可能重放目标分布。因此 Registry 应把指纹结果与
digest、lineage、部署 receipt 和独立 evaluation 并列保存：变化时阻断 promotion 或启动重评，不能仅凭接受或拒绝
裁定模型是否被替换。

### Byte integrity 与 Behavior integrity 必须联合验收

签名和 content digest 可以证明拿到的 bytes 是否等于已批准 artifact，因而是存储、传输和部署前验证的第一道门；但它们不能说明一次微小、未经授权的权重变化会影响哪类决策。反过来，有限行为 canary 能发现指定语义面的漂移，却无法穷举模型行为，也不能证明未命中的 bytes 没有变化。模型完整性因此需要两类 owner 并列：artifact pipeline 验证签名、hash 和 provenance，evaluation owner 对高风险决策面执行版本化 canary；任何一侧不一致都把 artifact 留在 quarantine，而不是继续 promotion。

部署后少量 bit changes 的受限攻击实验表明，在保持一般输出近似正常时，定向立场仍可能持续偏移。这证明“通用 sanity check 通过”不能替代权重完整性与定向回归，但不证明任意硬件、模型或 bit budget 都存在相同攻击面，也不能估计真实供应链发生率。更强 gate 会增加 canary 维护、误报和发布延迟；若 artifact bytes 可端到端信任且模型只用于低风险离线实验，digest-only 仍可作为较低成本基线。

<!-- source-family:SF-2026-ARXIV-2607-25227 -->

### Adapter 从文件变成 Policy Revision

少量 adapter 时，把 LoRA 文件挂到 base model 上已经足够；当训练持续产生大量 policy variants，文件身份却
不能回答“哪次 rollout 产生了它、何时可服务、哪些 working sets 已激活”。更完整的 managed unit 应拆开：

```text
mutable training adapter + optimizer / rollout state
→ immutable exported adapter revision
→ policy record + rollout / evaluation lineage
→ catalog-visible but not necessarily resident
→ CPU cache → GPU batch → readiness
→ serving exposure, retirement or rollback
```

Catalog addressability、CPU/GPU residency 与 request readiness 是三种状态；“能命名百万 revisions”不等于单机
同时加载百万 adapters。Export 还必须绑定 base、rank、target modules、layout/conversion 与 runtime compatibility，
并在 files 和 metadata 原子可见后才允许 exposure。预热可以降低 cold activation，却会挤压 warm tenants；packed
layout 减少 object fanout，却可能形成 runtime lock-in。因而 Registry 拥有 immutable policy identity 与 lineage，
runtime 拥有 cache/activation，scheduler 拥有 admission，training worker 仍拥有未提交的可变状态。MinT 的
作者系统为这条分层提供了实现证据，但不证明 catalog population 等于并发 residency，也不提供跨 runtime
format portability 的通用保证。

### Adapter 准入可以在生成之前增加 Weight-only Sensor

对来源未知的 LoRA，最直接的内容检查是加载并生成样本；它能够观察实际行为，却可能先产生不应被生成的内容，而且成本随 adapter 数量增长。一个前置分支对 LoRA weight update 做奇异值分解，以主导 left-singular direction 构造内容 fingerprint，在加载到 serving runtime 之前给出风险信号。Registry 必须把 sensor 结果绑定到 base model、adapter digest、特征提取版本、threshold 和 abstention 状态；命中只触发 quarantine 与后续政策处置，不能把统计分类结果写成“该 adapter 必然生成某类内容”。

受限实验以人类年龄 proxy 观察到信号在部分 base models、噪声和精度变化下仍存在，但 proxy 不等于真实违法内容，也没有覆盖主动规避攻击。Weight-only scan 的收益是减少高风险 artifact 首次执行，代价是阈值漂移、跨 base 失配、误杀与未知概念盲区；sensor 无法校准或 abstain 时，应保持隔离并交给独立人工与政策流程，而不是自动放行或自动定罪。对可信 lineage、低风险内部 adapter，现有 digest、compatibility 与行为 evaluation 仍是可接受基线。

<!-- source-family:SF-2026-ARXIV-2607-25750 -->

## Evidence 而不是“分阶段按钮”

模型升级不能只做 `old → new` 二选一。每个能力与接口应分别决定 retain、port、refresh 或 retrain：权重兼容说明 artifact 能加载，行为兼容说明关键契约未破坏，evaluation compatibility 说明分数仍可比较，三者不可互相替代。Registry 保存 upgrade plan、迁移证据和 rollback target；全面重训在差异过大或 lineage 不可信时仍是清晰基线。<!-- semantic-body-binding:SF-2026-ARXIV-2608-20918 -->

传统 registry 常提供 stage 字段。真正的 production promotion 应由 evidence 支撑：

- offline quality/evaluation suite；
- safety 与 policy checks；
- artifact conversion 的 logits regression；
- target hardware/runtime compatibility；
- owner、approval 与风险例外；
- canary/shadow 的线上证据。

Stage 只是状态；状态转换的输入、执行者和时间才构成可审计决策。

## Registry 与 Artifact Store 的边界

Artifact store 保存大对象，Registry 保存 metadata 与引用：

| 系统 | 优化目标 |
| --- | --- |
| Object store | durable bytes、throughput、retention |
| Registry | identity、query、lineage、policy、status |

把大权重存进 Registry database 会使 metadata control plane 被数据传输拖垮；只存 URI 而没有 digest，又无法验证内容未被替换。合理设计是 URI + content digest + provenance + access policy。

### 物理共享不能合并逻辑模型身份

少量、彼此独立的 checkpoint 直接保存完整副本，恢复路径最短，也最容易验证。一个 base model 派生出大量
同源 fine-tuning checkpoint 后，完整复制会把重复 tensor 同时放大为容量、传输和缓存压力。Artifact Store
可以在 bytes 层引入 family clustering、tensor/chunk-level dedup 与 lossless delta compression，但这不改变
Registry 的逻辑对象：

```text
logical model revision
→ base / delta lineage
→ content digest and authorization
→ physical chunks shared by the artifact store
→ independent materialization and hash verification
→ deployment reference / rollback target
```

<!-- semantic-body-binding:SF-2025-ZIPLLM-STORAGE:start -->
物理 dedup owner 只能决定 bytes 怎样共享；Registry 仍保存每个逻辑模型的 identity、base/delta lineage、
完整性 hash、访问策略和可独立 materialize 的恢复路径。删除 base 或共享 chunk 前必须证明所有引用均可恢复，
否则一次存储优化会同时破坏多个 deployment revision。
<!-- semantic-body-binding:SF-2025-ZIPLLM-STORAGE:end -->

收益是减少容量和传输，代价是 clustering 误判、base deletion、恢复放大、加密/量化不兼容和跨租户侧信道。
family 相似性不稳定、license/tenant boundary 不允许共享，或独立恢复比容量更重要时，完整 checkpoint 仍是正确
分支。公开实验只覆盖作者披露的 Hugging Face model families 与编码组合，不能外推到任意 encrypted、quantized
或受不同授权约束的 artifact。

Kubeflow 官方当前也明确 Model Registry/Hub 是 passive metadata repository，不是主动 control plane。部署 controller 可以读取 Registry 决策，但 Registry 不应自行创建 GPU workloads。

## 一次 Promotion 的状态转换

```text
registered
→ validated
→ approved
→ deployed-canary
→ serving
→ deprecated
```

转换应采用 compare-and-set 或明确 version precondition，防止两个审批或发布流程覆盖彼此。Mutable alias 需要审计日志和 rollback target。

删除也不是简单删文件：必须先检查 deployment references、retention/legal hold、下游 derived artifacts 和 reproducibility requirement。

## Trade-off

强制所有 metadata 完整后才能注册，可提高治理质量，却会阻碍探索阶段；允许任意 tags 灵活，但会产生不可查询的 metadata 方言。

一个实用策略是分层 schema：

- 核心字段强约束：identity、owner、digest、source、format；
- lifecycle 字段按阶段逐步必填；
- domain-specific metadata 允许扩展，但需 namespace 与版本；
- promotion gate 比 initial registration 更严格。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-22875:start -->
联邦生成模型的 ownership 证据不能只保存最终 watermark 命中；Registry 应把 watermark revision、artifact hash、client identity、训练/聚合 lineage 与泄露追踪结果绑定。它提高归责能力，却不自动证明法律所有权，也不能让watermark 检测覆盖未观测的模型变换。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-22875:end -->

### Distributed Model Merge 需要把 Replication 与 Merge Strategy 分层

权重平均、task arithmetic 等 merge strategy 通常不满足交换、结合与幂等，直接把它们当 CRDT operation 会让消息顺序改变最终 checkpoint。更稳健的两层结构让外层 CRDT 只复制有唯一身份的贡献集合，所有 replica 再以同一排序、strategy revision 和参数执行 deterministic merge：

```text
immutable contribution IDs
→ conflict-free replicated contribution set
→ deterministic ordered merge strategy
→ merged artifact + lineage
```

外层可保证相同贡献集合最终收敛，却不能证明 merge 后模型质量，也不能让非确定 kernel 自动可复现。它增加 metadata、重复计算和 contribution retention；单写者 registry 或集中式 merge 仍更简单。Promotion 必须继续由独立 evaluation 决定，而不是由 replica convergence 授权。

<!-- source-family:SF-2026-ARXIV-2605-19373 -->

### MoE Merge 的发布身份还要包含 Router Calibration

把两个 dense checkpoint 合并后，registry 至少可以用贡献集合、merge strategy 与结果 digest 标识新 artifact；MoE
还多了一层非线性 routing state。即使 expert weights 的合并可复算，合并后的 router 也可能不再把 token 分配到原本承担
相应能力的 experts。因而 promotion identity 应进一步绑定 `merged weights + router calibration data/revision +
expert-assignment regression + load-balance evidence + source-model fallback`。Merge job 只产生候选权重和 calibration proposal，
registry 保存 lineage，Evaluation gate 才能决定该组合是否可发布。

额外校准能修复一部分 routing drift，却会增加数据选择、router overfit、能力迁移和线上负载偏移；恢复 source routing
也不证明它是合并后唯一正确的目标。校准集不能代表目标 workload、assignment regression 与任务质量冲突，或生产流量出现
新热点时，应阻止 promotion，回退 source models、重新训练 router，或保留未合并部署。exact-v1 的 OLMoE math/code merge
只支持所测 merge algorithms、calibration data 与 expert assignment，不证明跨 MoE 架构或生产负载普适。

<!-- semantic-body-binding:SF-MODEL-MERGE-ROUTER-CALIBRATION -->

### 模型 artifact 的身份必须覆盖可执行架构，而不只覆盖权重

只扫描 weights、训练数据和 clean utility，会漏掉藏在 architecture definition、remote code、custom operator、text encoder/config 或 exported graph 中的 dormant behavior。模型 registry 因而应把这些可执行组成一起纳入 artifact manifest、content hash、provenance 与隔离构建，并在允许 remote code 前检查实际计算图和 trigger-sensitive behavior。

受控 VLM backdoor 证明这种攻击面存在，却没有提供“扫描通过即安全”的完备 detector。更强 artifact trust 会增加构建隔离、签名、行为 probe 与兼容成本；无法验证自定义逻辑时，应禁用 remote code、转换到受支持 graph 或拒绝发布，而不是让权重 digest 替代执行身份。

<!-- source-family:SF-2026-ARXIV-2607-25479 -->

### Multimodal Connector 也必须进入 Promotion Identity

把 multimodal connector 当成可以随 backbone 任意替换的小附件，在 connector 只做无状态格式转换、来源可信且 clean utility 足够时很方便；但 learned connector 本身也可能保存跨模态触发状态。共享 latent space 甚至会让一种模态植入的 activation 被另一种模态触发，因此只验证 backbone weights 与 clean task accuracy，会遗漏真正改变系统行为的 artifact。

Registry 应把 connector weights、训练 provenance、activation modality、cross-modal trigger slices、backbone/codec revision 一起纳入组合身份；artifact pipeline 提交这组不可变 manifest，独立 security/evaluation gate 对 clean 与 attack slices 分别验收，只有两侧都通过才允许 promotion。这样把触发面从“模型内部未知行为”变成可追踪的发布条件，却增加跨模态 red-team 成本，也无法证明未覆盖 trigger 不存在。connector 来源不可信、模态覆盖不足或结果冲突时，应冻结或拒绝该 connector，回退已验收组合或专用模态路径，而不能让 clean utility 取得安全裁决权。

[受限证据](https://arxiv.org/html/2605.07490v1)来自受控 poisoning、指定 connector/target 与 exact/relaxed ASR；它证明跨模态持久触发是可实现攻击面，不证明现实 prevalence、未知 trigger 可被完备检测或扫描通过即安全。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-07490 -->

### Producer provenance 与 consumer compatibility evidence 不能由一张 Model Card 混代

模型生产者关心训练 lineage、许可和发布声明，复用者还需要目标 runtime、量化、输入 schema、可靠性与治理证据；双方即使引用同一 artifact，也可能对记录深度、位置和用途有不同要求。Registry schema 应显式保存 claim owner、intended consumer、required evidence 与 missing status，而不是假设发布者提供的 metadata 自动满足部署判断。

调查型人因证据不能证明某一 schema 会因果提高可靠性，但足以说明缺失状态必须是一等信息。更丰富 contract 增加维护和迁移成本；低风险内部复用可采用较小 profile，高风险跨组织发布则应 fail closed 或要求 consumer-side validation。

<!-- source-family:SF-2026-ARXIV-2607-21738 -->

### 派生链水印是 Provenance Sensor，不是所有权裁决

训练、微调和 merge 形成多级模型派生链后，仅记录最终 artifact 的发布者会丢失中间贡献。可检测的 multi-user watermark 可以把 carrier、插入顺序、检测阈值与 parent lineage 绑定到每个模型版本，为“某段贡献是否仍可检出”提供独立信号。Registry 应把该信号保存为带方法版本和误检边界的 provenance evidence，而不是把检测结果直接写成所有权事实。

水印会受到剪枝、量化、adapter merge、共谋与未知变换影响，阈值选择也会产生误检；它因此不能替代签名、训练输入记录和完整派生 manifest。高风险发布仍需多种证据交叉确认，无法稳定检测时回退显式 lineage 与受控构建流程。

<!-- semantic-body-binding:SF-2026-ARXIV-2606.17123 -->

### 黑盒服务的 Provenance 只能形成统计证据，不能替代 Artifact Lineage

文件 digest、签名和构建记录适合可取得 artifact 的部署；第三方黑盒 API 无法直接提供同等证明。此时可以用
一组经过稳定性、鲁棒性和区分度筛选的 probes，估计服务输出是否仍落在某个候选模型的决策区域，并把结果作为
behavior-sensitive provenance evidence：

```text
declared service revision
→ versioned probe set and evaluator
→ response distribution / decision-region evidence
→ statistical match with uncertainty
→ promotion or escalation decision
```

这个分支补足的是“无法读取权重时怎样发现身份漂移”，不是证明模型所有权或字节等价。蒸馏、代理转发、probe
泄露、采样设置和 API 后处理都可能产生误判；Registry 必须保存 probe version、调用配置、置信区间与复验条件，
并与供应商声明、attestation 和运行审计并列。可访问 artifact 时，签名/hash 仍是更直接的 baseline；黑盒匹配
不足或结果冲突时应停止自动 promotion，转人工或要求更强 provenance。

<!-- source-family:SF-2026-ARXIV-2607-25880; daily-trace:papers/2026/07/29/README.md -->

### 从固定 Challenge 到 Query-varying 流量：黑盒身份只能逐步累积证据

预先设计的一组 probes 适合周期性验收已知服务，却会改变输入分布，也可能被服务识别并针对性适配。真实流量中的 query
不断变化时，Registry 需要另一条被动证据链：由冻结的 proxy model 读取黑盒响应，把 token hidden states 做时间聚合，再用带
正则的多类线性 probe 产生单次 posterior；跨独立 query 的 evidence accumulation 才逐步提高区分度。Registry 保存的不是
“模型已被证明是谁”，而是 `candidate set + proxy/probe revision + query distribution + evidence epoch + query budget +
calibration + confidence/abstention`。

这种方法把一次响应的弱统计信号变成可审计的累计身份 sensor，但它没有获得 artifact authority。closed-set 分类会把未知模型
硬塞进已知候选，蒸馏、路由、temperature、wrapper 和多个 provider 混合也会改变表示；同一 query stream 的相关性还会让朴素
Bayesian 累积过度自信。因此低置信或分布漂移时必须输出 Unknown，并回退 provider attestation、签名 artifact、固定 challenge
probe 或人工复验。Trace 章节负责保存调用证据，Security 章节决定异常后的权限处置；两者都不重定义模型身份。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-10794 -->

## 本章在知识树中的位置

```text
Chapter 35 checkpoint
→ conversion / packaging
→ Model Registry identity and evidence
→ Chapter 61 KServe desired deployment
→ runtime load and logits regression
```

本章管理“部署什么”的可信身份。下一章回到“如何运行生产任务”，讨论 Training Operator 怎样把分布式训练意图转为可恢复的 Kubernetes workload。

沿 State 横线，第 55 章管理单个在线请求的 KV ownership 与 handoff，本章切换到跨运行长期存在的 artifact identity、revision 和 promotion state；第 75 章再把被授权的 artifact、evidence 与当前任务输入组装为一次调用的 working state。三者分别位于 request、asset 与 invocation 边界。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22593 -->
registry 的 release authority 不是 package presence；必须测量谁能发布、撤回、覆盖 metadata，以及 registry mediator 是否保留身份和审计链。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；公开 registry metadata 只能观察可见 authority，不证明离线凭据、组织流程或未披露 compromise。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Registry 从保存权重文件演进为模型交付身份图：base、adapter、tokenizer、data/objective、checkpoint、quantization、runtime compatibility、evaluation evidence 和 deployment decision 必须可追溯。规模化 PEFT 进一步说明，一个 base 可以对应大量租户 adapter，版本和访问边界不能只靠文件名表达。

更完整的 lineage 支持复现、promotion 和 rollback，却增加元数据一致性与存储治理成本。缺少兼容性或 evidence 的 artifact 只能处于 candidate 状态，不能被 registry 的“已注册”误解为“可生产发布”；简单目录仍可用于本地实验，但不承担跨团队 release authority。

## 自检问题

1. 为什么 object storage 路径不能作为模型身份？
2. Immutable version 与 mutable alias 应怎样配合？
3. LLM 的行为身份为什么超出 weights？
4. Registry 与 artifact store 的责任边界是什么？
5. 为什么 stage 字段本身不是 promotion evidence？
6. Registry 为什么不应主动创建 serving workload？

### 私有权重 Artifact 可以增加 Behavior-sensitive Proof

digest 能确认公开字节完全一致，却无法让不暴露权重的服务证明自己运行了预期模型。对行为敏感的 adversarial probes 配合隐私保护证明，可以补充 registry 的远程身份验证；它只能证明被探测行为与承诺模型一致，不能证明完整权重等价，也可能受蒸馏、转发和 probe 泄露影响。因此行为证明应与 artifact digest、attestation 和运行证据并列，而不是替代它们。
<!-- source-family: arxiv:2608.27954v1; semantic-body-binding: private-model-behavior-sensitive-proof -->

## 小结

Model Registry 让模型从一组文件变成有身份、有来源、有证据、可发布和可回滚的资产。它连接 Part IV 的 checkpoint 与 Part V 的 runtime artifact，但保持 metadata control plane 的被动边界。

## Review notes

- `SF-2026-ARXIV-2606-10794`（Status: Experimental）：官方 exact-v1 的 frozen proxy、token-state temporal mean、L2
  multinomial probe 与 Bayesian evidence accumulation 支持“query-varying 黑盒流量可形成累计身份 sensor”。Agent500 为
  50 个目标模型、每个 500 prompts、共 25,000 trajectories；单响应 top-1 为 31.0–42.4%，50 响应累积为
  70.0–84.0%，并测试 9 个 proxy readers。closed-set、single-source、无 closed API、换 label 需重训及未覆盖
  adaptive/mixed provider 限制其结论；统计 sensor 不等于模型所有权、字节身份或 attestation。

- `SF-2026-ARXIV-2606-22593` — primary `arXiv:2606.22593v1`；Method=`arXiv:2606.22593v1 §3 Authority Model and Measurement; §3.4 Evaluation`；Evaluation=`arXiv:2606.22593v1 §4 Results`；Non-proof=`arXiv:2606.22593v1 §5 Limitations and Discussion`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

本章承接第 35、49、54、56 章的 artifact contract，明确训练 checkpoint、deployment artifact 与 service revision 不能混为一谈。第 66 章定义 Evaluation Run 怎样把 subject、dataset/environment、scorer 与结果绑定，并把 MLflow 作为一种 evidence implementation；本章只索引 evidence 和 promotion state，不定义质量语义。

Primary-source 与官方入口：

- ML Metadata paper: https://arxiv.org/abs/2010.03067
- Kubeflow Hub Model Registry architecture: https://www.kubeflow.org/docs/components/hub/reference/architecture/
- MLflow Model Registry workflow: https://mlflow.org/docs/latest/ml/model-registry/workflow
- MinT（managed adapter/policy revision lifecycle；作者系统边界）:
  https://arxiv.org/abs/2605.13779
- AgentProv（Status: Experimental；structured tool-policy fingerprint、permutation-calibrated MMD 与 prompt/
  quantization/wrapper controls；结果只触发 deployment revalidation，不证明 provider identity 或 model ownership）:
  https://arxiv.org/html/2609.00052v1

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22875` — primary `arXiv:2606.22875v1`; Method=`arXiv:2606.22875v1 — §3.1 FedOT Framework; §3.2 Watermark Design and Training; §0.A.1 Federated LDMs and Threat Model`; Evaluation=`arXiv:2606.22875v1 — §0.C.2 Analysis of LVT`; non-proof=`arXiv:2606.22875v1 — §5 Conclusion`; fallback=该 family 的 failure pressure 是：However, FL requires sharing the global model with multiple participants, which risks unauthorized model distribution or resale by malicious clients. 披露的 evaluation signal 是：Extensive experiments demonstrate that FedOT achieves superior performance in both ownership verification and traceability. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-21787:start -->
- `SF-2026-ARXIV-2606-21787` — Daily `2026-06-20`；primary `arXiv:2606.21787v1`；Books review `books-review:SF-2026-ARXIV-2606-21787`。

  **已吸收的语义增量：** 模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage
<!-- daily-books-trace:SF-2026-ARXIV-2606-21787:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25227:start -->
- `SF-2026-ARXIV-2607-25227` — Daily `2026-07-29`；primary `arXiv:2607.25227v1`；正文锚点“Byte integrity 与 Behavior integrity 必须联合验收”。
  证据限三个开放模型与两类定向场景，不证明普遍可攻击性或真实供应链发生率。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25227:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-25750:start -->
- `SF-2026-ARXIV-2607-25750` — Daily `2026-07-29`；primary `arXiv:2607.25750v1`；正文锚点“Adapter 准入可以在生成之前增加 Weight-only Sensor”。
  证据只支持人类年龄 proxy 与部分 base/noise/precision 条件下的前置风险信号，不等价真实 CSAM、内容必然生成或规避鲁棒性。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25750:end -->
