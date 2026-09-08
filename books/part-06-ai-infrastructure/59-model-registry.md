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

### Source-family integration record

<!-- recovered-daily-20260623:PLATFORM-MODEL-REGISTRY:start -->
### 2026-06-23 evidence integration — PLATFORM-MODEL-REGISTRY

相邻章 `books/part-06-ai-infrastructure/60-training-operator.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22875**：FedOT: Ownership Verification and Leakage Tracing via Watermarks for Federated LDMs 的 exact-v1 机制为：In this paper, we propose FedOT, the first framework for ownership verification and leakage tracing in federated LDMs. 因此 把 ownership/provenance 证据与 artifact hash、client identity 和泄露追踪绑定。 该 family 的 failure pressure 是：However, FL requires sharing the global model with multiple participants, which risks unauthorized model distribution or resale by malicious clients. 披露的 evaluation signal 是：Extensive experiments demonstrate that FedOT achieves superior performance in both ownership verification and traceability. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:PLATFORM-MODEL-REGISTRY:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-21787:start -->
- `SF-2026-ARXIV-2606-21787` — Daily `2026-06-20`；primary `arXiv:2606.21787v1`；Books review `books-review:SF-2026-ARXIV-2606-21787`。

  **已吸收的语义增量：** 模型 artifact 的 semantic fingerprint 应与文件 hash、版本和部署证据并存，用于识别行为差异而非替代 lineage
<!-- daily-books-trace:SF-2026-ARXIV-2606-21787:end -->
