# 第55章 Model Registry

**Knowledge Tree:** Part V AI Infrastructure：从工具到平台
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

第 31 章已经把 checkpoint 定义为可恢复、可转换的训练资产。进入平台后，还需要一个 deployment artifact contract，把 source checkpoint、转换过程和 runtime artifact 区分开。

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

## Evidence 而不是“分阶段按钮”

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

## 本章在知识树中的位置

```text
Chapter 31 checkpoint
→ conversion / packaging
→ Model Registry identity and evidence
→ Chapter 57 KServe desired deployment
→ runtime load and logits regression
```

本章管理“部署什么”的可信身份。下一章回到“如何运行生产任务”，讨论 Training Operator 怎样把分布式训练意图转为可恢复的 Kubernetes workload。

## 自检问题

1. 为什么 object storage 路径不能作为模型身份？
2. Immutable version 与 mutable alias 应怎样配合？
3. LLM 的行为身份为什么超出 weights？
4. Registry 与 artifact store 的责任边界是什么？
5. 为什么 stage 字段本身不是 promotion evidence？
6. Registry 为什么不应主动创建 serving workload？

## 小结

Model Registry 让模型从一组文件变成有身份、有来源、有证据、可发布和可回滚的资产。它连接 Part III 的 checkpoint 与 Part IV 的 runtime artifact，但保持 metadata control plane 的被动边界。

## Review notes

本章承接第 31、45、50、52 章的 artifact contract，明确训练 checkpoint、deployment artifact 与 service revision 不能混为一谈。第 62 章再把 MLflow 映射到 tracking/registry 实现，不在此处依赖某个产品的数据模型。

Primary-source 与官方入口：

- ML Metadata paper: https://arxiv.org/abs/2010.03067
- Kubeflow Hub Model Registry architecture: https://www.kubeflow.org/docs/components/hub/reference/architecture/
- MLflow Model Registry workflow: https://mlflow.org/docs/latest/ml/model-registry/workflow
