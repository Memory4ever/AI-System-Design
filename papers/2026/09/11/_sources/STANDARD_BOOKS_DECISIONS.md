# 2026-09-11 Standard Review Books Decisions

**范围：** arXiv:2609.10657、2609.10658、2609.10723、2609.10863、2609.10976、2609.10993、2609.11127  
**判断基础：** exact-v1 审阅完成后，对照 `ROADMAP.md` 的 canonical owner、目标章节正文及相邻交接内容。评分只决定最低审阅深度，不自动触发 Books Integration；`2609.10863` 因进入 Books 触发深入审阅，独立补充见 `FLOW_DUALITY_DEEP_SUPPLEMENT.md`。

## 决策摘要

| Source Family | Disposition | Canonical owner / 精确正文锚点 |
| --- | --- | --- |
| `SF-2026-ARXIV-2609-10657` | `No Change — Existing Coverage` | `WORLDVIEW-REPRESENTATION` / Ch5：`## 记忆与泛化不是简单对立`；`## 工程上怎样验证模型学到了什么` |
| `SF-2026-ARXIV-2609-10658` | `No Change — Existing Coverage` | `TRAIN-RLHF`：`### 从持久权重更新到条件化 Activation Intervention`；`PLATFORM-EVALUATION-SYSTEM`：`### 表征审计必须先消除模板混淆，再谈因果` |
| `SF-2026-ARXIV-2609-10723` | `No Change — Existing Coverage` | `MULTIMODAL-REPRESENTATION`：`### 统一架构不等于双向可用的统一语义空间`；`MULTIMODAL-GENERATIVE-PARADIGMS`：`### Conditional Guidance 把 Diffusion 并行策略变成逐 Step 状态` |
| `SF-2026-ARXIV-2609-10863` | `Integrate` | `MULTIMODAL-GENERATIVE-PARADIGMS`：`### Continuous 与 Discrete Flow 的等价是有条件的`；marker `source-family:SF-2026-ARXIV-2609-10863` |
| `SF-2026-ARXIV-2609-10976` | `仅报告 — Explanatory Analogy` | `MODEL-SELF-ATTENTION`：`## 固定信息流为什么不够`、`## 从匹配分数到读取权重` |
| `SF-2026-ARXIV-2609-10993` | `No Change — Existing Coverage` | `WORLDVIEW-REPRESENTATION` / Ch5：`## 分布式表示与 Superposition`、`### 从可读出到机制：证据应逐级变强`；`PLATFORM-EVALUATION-SYSTEM` / Ch66：`### 表征审计必须先消除模板混淆，再谈因果` |
| `SF-2026-ARXIV-2609-11127` | `No Change — Existing Coverage` | `TRAIN-RLHF`：`### 后训练分支的本质差异是 State Distribution`、`### Teacher 与未来 Reward Model 都是反馈回路中的状态`；`TRAIN-PRETRAINING`：`### Distillation 要分开 Prefix Provenance 与 KL Direction` |

## 逐项判断

### arXiv:2609.10657v1 — Grokking Scaling

**Disposition：** `No Change — Existing Coverage`。

Ch5 的 `## 记忆与泛化不是简单对立` 已明确说明模型可以同时拟合局部样本与压缩共享结构，并要求用未见数据、时间切分和分布外评估判断泛化；`## 工程上怎样验证模型学到了什么` 又把切片、扰动、跨分布、内部分析和线上闭环组织成证据阶梯。论文在两个 modular-arithmetic task、小型 MLP 与单 seed/config 上观察到的幂律、phase transition 和 norm threshold，没有改变这项长期判断，也不足以形成 LLM 训练或部署的新 contract。

论文的 scaling exponent 与临界点保留在 Daily 作为受限实验事实。它未证明不同架构、优化器、自然语言任务或大模型规模遵循同一规律，因此不把经验拟合写成 Books 的通用演进结论。

### arXiv:2609.10658v1 — GeoSteer

**Disposition：** `No Change — Existing Coverage`。

Ch31 的 `### 从持久权重更新到条件化 Activation Intervention` 已拥有 runtime activation steering 的 canonical mechanism：离线建立条件映射，在线以 prompt gate 与 token-active state 做有界干预，并列明 feature-basis/version coupling、off-manifold 污染、开销和回退权重更新。Ch66 的 `### 表征审计必须先消除模板混淆，再谈因果` 也已区分 probe 的可分性与 intervention 的因果证据。GeoSteer 的 hyperspherical/geodesic PCS 是这个分支的具体控制算法，不改变 state/control ownership。

其受测模型、任务与 steering strength 下的结果不能证明持久 alignment，也不能替代 safety gate；算法细节与 benchmark 保留在 Daily，不重复进入正文。

### arXiv:2609.10723v1 — AcFlow

**Disposition：** `No Change — Existing Coverage`。

Ch23 的 `### 统一架构不等于双向可用的统一语义空间` 已要求跨分支 steering 使用 matched intervention、random/unrelated controls，并把 off-manifold steering 与 evaluator bias 列为边界；Ch24 的 `### Conditional Guidance 把 Diffusion 并行策略变成逐 Step 状态` 已将 conditional branch、step、latent revision、合成与 commit 的 owner 分开。AcFlow 的 shared activation-conditioned control field 是该设计空间内的局部算法实例，不形成新的长期 owner。

论文未证明概念被因果删除、非目标语义保持或相同资源下优于所有 per-concept/parameter adaptation；硬件与生产 SLO 也未披露。因此只在 Daily 保存机制和 evidence boundary。

### arXiv:2609.10863v1 — Flow Duality and Source Geometry

**Disposition：** `Integrate`。

已在 Ch24 `### Continuous 与 Discrete Flow 的等价是有条件的` 中补入：严格假设下 continuous convex interpolant 经 argmax 诱导 categorical conditional path；source pairwise-gap geometry 改变有效 transition timing；source、coupling、schedule、learned field 与 runtime commit 的 owner 必须分离。正文同时保留 Gaussian/既有 schedule 的共存条件，以及假设失效、source 更换和 coefficient 饱和时的 failure/fallback。

正文明确限制证据：理论只覆盖条件路径；10K-step OpenWebText single run 与 toy trajectory 不证明生成质量排序、训练稳定性或 serving 收益。非作者深入审阅已确认该窄化正文与 exact-v1 的定理、证明、实验和 artifact 边界一致。

### arXiv:2609.10976v1 — Associative Memories via Hidden Neurons

**Disposition：** `仅报告 — Explanatory Analogy`。

Ch14 的 `## 固定信息流为什么不够` 与 `## 从匹配分数到读取权重` 已把 Self Attention 的长期机制定义为 content-dependent routing：Q/K 决定匹配，V 承载被聚合内容。论文的 hidden-neuron associative-memory model 可以解释高阶 interaction 怎样改变理论 load 与 retrieval phase，但它没有证明生产 Transformer 的 learned attention 服从同一 equilibrium、Gaussian-pattern、replica-symmetric 或温度假设。

这项结果目前属于 explanatory analogy，而不是 Attention 的 direct evolution、可部署容量公式或新的 runtime contract。将其写进正文会把 statistical-mechanics 特例误升格为实际模型机制，因此只保留报告证据。

### arXiv:2609.10993v1 — Distribution-aware Language Neurons

**Disposition：** `No Change — Existing Coverage`。

Ch5 的 `## 分布式表示与 Superposition` 已说明单 neuron 可能 polysemantic、概念也可能分布在多个方向，并明确区分 correlation、prediction 与 causation；`### 从可读出到机制：证据应逐级变强` 要求从 decodability 继续走到 intervention、downstream behavior 和跨 context/model replication。Ch66 的表征审计锚点进一步要求先控制 prompt/template 混淆。论文提出的多语言分布感知 neuron identification 与 intervention，正处于这条既有证据阶梯中。

其七种语言与指定 SiLU-GLU 模型上的结果支持 functional sensitivity，不证明神经元是稳定、单义的知识 owner，也不改变现有 evaluation contract，故不重复写入 Books。

### arXiv:2609.11127v1 — KuaiRP

**Disposition：** `No Change — Existing Coverage`。

Ch31 的 `### 后训练分支的本质差异是 State Distribution` 已把静态 SFT、on-policy distillation 与 RL 的差异定位到训练所覆盖的 policy-induced states，并要求 rollout producer、policy/teacher/reward revision 与 staleness 进入 run identity；`### Teacher 与未来 Reward Model 都是反馈回路中的状态` 明确 teacher 不是无条件真值。Ch28 的 `### Distillation 要分开 Prefix Provenance 与 KL Direction` 已承载 teacher-forced、student-prefix、forward/reverse KL、sampling 与 curriculum 的组合边界。

KuaiRP 的 role-playing pipeline 与 context-dependent distillation weighting 是这条既有路线的特定实现。自建/专有评测、一个失败的 Qwen3.5 scaling attempt，以及未披露的完整成本条件不足以支持新的通用后训练结论；因此保留 Daily 案例，不新增正文。

## 一致性结论

- 本批仅 `SF-2026-ARXIV-2609-10863` 改变长期知识正文；其 marker 位于 Ch24 首个 `## Review notes` 之前。
- 其余六项均获得精确 owner 与 disposition；`No Change` 表示正文已经覆盖机制合同，`仅报告` 表示证据仍不足以成为实际模型机制。
- 本轮没有依据论文名称、评分或局部 benchmark 强行制造 Books diff，也没有把受限实验外推为通用质量、性能或部署结论。
