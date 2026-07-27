# 第29章 SFT

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-SFT`
**Legacy Chapter:** Ch25
**Status:** Draft

**Roadmap Intent:** 监督微调如何把通用模型对齐到指令、任务和业务风格。

## 本章要回答的问题

Pretraining 已经让模型能够续写文本，为什么它仍可能不遵循指令、模仿错误角色或输出不合适的格式？Supervised Fine-Tuning 怎样用 demonstrations 改变条件分布？为什么 SFT 仍然使用 cross-entropy，却能显著改变模型行为？

本章的核心判断是：**SFT 用高质量 `(instruction, response)` demonstrations 重新加权模型的条件生成行为，使“用户请求后应该怎样回答”成为训练分布中的高概率模式。**它主要教模型模仿目标行为，不等于证明回答正确，也不能表达所有相对偏好。

本章使用 `x` 表示 prompt/context，`y=(y_1,...,y_T)` 表示目标 response，`theta` 表示待更新参数，`m_t` 表示第 `t` 个位置是否参与 loss，`B` 表示 batch size，`V` 表示 vocabulary size。

## Pretraining 接口为什么不等于产品接口

预训练数据中可能同时出现：

- 问题与正确答案。
- 问题与错误答案。
- 多人争论、引用和角色切换。
- 网页导航、广告、代码、日志与模板。
- 对指令的描述，而不是对指令的执行。

模型学到的是这些文本条件关系。用户输入“请总结这段文档”时，pretrained model 可能继续讨论“总结”这个词，也可能模仿网页结构，而不是稳定输出目标摘要。

一种朴素解法是只靠 prompt engineering，把每个产品规则写进 system prompt。Prompt 可以选择和组合已有行为，却无法保证所有目标行为在模型分布中都足够高概率，也会占用 context、增加维护与注入风险。

SFT 通过参数更新，把目标交互模式直接放进模型行为分布。

## Demonstration 数据定义了什么

一条 instruction-tuning 样本通常包含：

```text
system policy
user instruction
optional context / tool result
assistant response
```

它不是普通问答表。数据同时定义：

- 角色和 turn 边界。
- 对指令的解释方式。
- 回答格式、长度与语气。
- 拒答、澄清和安全边界。
- 工具调用或结构化输出协议。

因此 SFT data schema 是模型接口的一部分。训练时的 chat template 与 Serving 时不同，即使可见文字近似，也可能形成 special-token、role id 或 whitespace 的 training-serving skew。

## SFT 的数学仍是条件最大似然

给定 prompt `x` 和 response `y`：

```text
p_theta(y | x)
= product_(t=1)^T p_theta(y_t | x, y_<t)
```

Response-only SFT loss 为：

```text
L_SFT(theta)
= - sum_(t=1)^T log p_theta(y_t | x, y_<t)
```

在 packed batch 中可写成 masked token loss：

```text
L_SFT
= - (1 / sum_(b,t) m_(b,t))
  * sum_(b,t) m_(b,t)
  * log p_theta(y_(b,t) | prefix_(b,t))
```

Logits 仍是 `[B,T,V]`，loss 并没有换成新的模型输出类型。变化来自训练分布、哪些 positions 被 mask，以及更新通常从 pretrained checkpoint 而不是随机参数开始。

## 一个 loss mask 小例子

假设 token sequence 是：

```text
[SYSTEM, policy, USER, 2+2?, ASSISTANT, 4, EOS]
```

若只训练 assistant response，labels 与 mask 可抽象为：

```text
labels = [policy, USER, 2+2?, ASSISTANT, 4, EOS]
mask   = [   0,    0,    0,         0, 1,   1]
```

System 和 user tokens 仍进入 context，决定 assistant tokens 的条件概率，但它们对应的 next-token positions 不贡献 loss。

若 mask 错位一格，模型可能被训练去预测角色边界而漏掉答案 token；若把 padding 也计入 loss，模型会学习无意义的 PAD 分布。SFT correctness 首先是 token-level alignment correctness。

## 是否应该对 Prompt 也计算 loss

对完整 conversation 所有有效 tokens 计算 loss，可以增加监督 token 数，并让模型学习 user/system 文本分布；response-only loss 则把容量更集中在目标输出行为。

两者没有脱离场景的绝对答案：

- Continued pretraining 或 domain adaptation 可能希望训练所有文本。
- Instruction following 通常更关心 assistant positions。
- 多轮对话可能只训练部分 assistant turns。
- Tool traces 可能需要分别 mask arguments、results 和自然语言。

必须记录 loss mask policy。只保存原始 JSON 而不保存模板和 masking code，无法复现实际训练 objective。

## 为什么少量高质量数据也可能有效

SFT 通常不是从零创造语言能力。Pretraining 已经形成大量表示与生成模式，SFT 的任务更像是选择、组合和稳定目标行为。

因此 demonstration 的边际价值可能高于随机网页 token。但“少量数据足够”不能泛化为固定数量定律：

- 新领域是否已在基座能力范围内。
- 输出协议有多复杂。
- 目标行为与基座分布偏离多远。
- 数据是否覆盖困难和失败案例。
- 模型规模与更新方式。

重复大量同质 examples 可能快速降低 training loss，却造成 style collapse、过度拒答或对 prompt phrasing 过拟合。

## SFT 数据质量比格式整齐更难

Tool-use SFT 还需要显式保存 decomposition 与 environment transition。把一条多步任务压成最终正确答案，会让模型学不到何时调用、如何消费 observation、哪些子任务可并行，以及 compose 失败怎样恢复。更完整的 demonstration contract 是：

```text
task and tool schema
→ dependency-aware subproblem plan
→ typed call / observation transitions
→ composition and final outcome
→ verifier evidence
```

分解可以降低复杂依赖的 lazy reasoning，却会在简单或强耦合任务上制造额外步骤、teacher leakage 与并行 side effect。SFT 负责模仿被验证的 decomposition；RL 的 entropy/process reward 只能作为补充，不能把多样性当 correctness。

高质量 demonstration 至少需要检查：

- Instruction 是否可解、信息是否充分。
- Response 是否正确，而不只是流畅。
- Style、verbosity 和格式是否与目标一致。
- Refusal 是否在正确边界触发。
- 多轮上下文与工具结果是否自洽。
- 不同 domains、语言与难度是否平衡。
- Synthetic data 是否经过 verifier 或抽样人工检查。

使用更强模型生成 synthetic demonstrations 可以扩大覆盖，却可能复制 teacher 的错误、偏好和措辞。过滤器与 judge model 也会引入自己的 selection bias。

### Distillation 不是“Teacher 越强越好”

#### Self-distillation 也可以改变 Target Distribution

Frozen model 以默认 sampling 生成自己的单一答案，再原样 SFT，容易只是复制当前 mode。对生成 logits 使用
non-unit temperature 与 truncation 后再采样，相当于先定义一个不同的 self-target distribution，随后把它通过
SFT 编译进参数；serving decode policy 仍是另一个独立选择：

```text
base checkpoint + prompt pool
→ target sampling policy (temperature / truncation)
→ generated demonstrations + filter
→ SFT parameter update
→ separately selected serving sampling policy
```

它省去强 teacher 或在线 verifier，却仍支付 generation、过滤和训练成本，并可能把错误代码、sampling artifact
与 benchmark-specific diversity 固化进权重。Plain on-policy self-training、external teacher 和 verified data 在
高风险或可获得可靠 verifier 时仍成立。Simple Self-Distillation 的作者实验只支持其五模型与 code benchmark
contract，不构成无监督“自我改进”的通用证明。

当 student 与 teacher 的容量、目标或输出风格差距过大时，直接模仿最强 teacher 可能产生不可学的
soft targets、过长 reasoning 或与 student inductive bias 不匹配的行为。一个可选演进是 cascade：
先从较近的 parent checkpoint prune 到目标 shape，完成 distillation 后再把 child 作为下一尺寸的
teacher，逐级缩小 capacity gap。

```text
large parent
→ prune to nearby shape
→ distill and validate
→ use validated child as next teacher
→ branch into instruct / reasoning post-training
```

它用更多 lineage、阶段和评估成本，换取更平滑的知识/行为转移；也会累积 teacher bias、pruning
误差和错误目标。独立从零训练在数据充分、需要不同 architecture 或不希望继承 teacher 偏差时仍然
成立。Mistral 的后续 Ministral 3 报告为这条机制提供了作者实验，其中“pretraining teacher 更强
未必更好、post-training teacher strength 又可能有益”只能视为其设置下的 sensitivity evidence，
不能升级为通用配方，也不能倒写成 2025 Mistral 3 release 已公开的完整训练机制。

### Context Distillation：把可逆 Prompt 行为迁移进权重

Prompt-only control 是最容易回滚的旧方案：在输入中加入“保持简洁”“展示步骤”或某种角色约束，
模型在运行时据此改变行为。它不需要修改 checkpoint，也便于按请求切换；代价是持续占用 context、
受 prompt injection/措辞敏感性影响，而且每次推理都要重新表达同一 policy。

若某种行为已稳定成为默认要求，可以让 teacher 与 student 读取不同 context，却在 **同一条 student
prefix** 上比较下一 token 分布：

```text
student samples y from original prompt x
-> for every student prefix y_<t:
   student logits = f_student(x, y_<t)
   teacher logits = f_teacher(x + privileged behavior context, y_<t)
-> minimize full-vocabulary distribution divergence
-> update student without privileged context
```

这与让 teacher 另写一条“更好的答案”再做 imitation 不同。Teacher 评价的是 student 实际访问到的
prefix，因此 supervision 仍覆盖 student 的 on-policy state distribution；full-vocabulary soft target 也保留
了单一 target token 丢失的相对概率信息。以 reverse KL 为例，它更偏向 teacher 的高概率 modes，但具体
KL 方向、token reduction 与 truncation 都会改变 objective，不能只用“distillation”一个名称代替训练合同。

当 teacher 只是 student 的周期性冻结快照时，系统还新增了持久状态：

```text
student checkpoint / optimizer state
+ teacher snapshot id
+ refresh interval and trigger
+ rollout policy version
+ privileged instruction version
+ synchronization / recovery point
```

Teacher 永久冻结，target 稳定但能力上限和 student distribution 逐渐错位；频繁刷新可缩小 distribution
gap，却可能形成即时正反馈，让 teacher 与 student 一起收缩到坏的短路行为。周期 refresh 是两者之间的
控制旋钮，不是普通超参数备注。恢复训练若只加载 student 而遗漏 teacher snapshot/cadence，也会静默改变
trajectory。

这种方法获得的是将行为写入参数、减少 runtime prompt 依赖，并不自动得到“更短且同样正确”。它仍会
强化错误 student prefix，继承 privileged instruction 的偏差，还需要额外 teacher forward、logit memory 与
同步。评估必须分开 correctness、format compliance、output length 和 task latency，避免把 scorer 只接受某
种答案格式造成的增益误判为 reasoning improvement。

On-policy distillation 还应把 **state coverage** 与 **token selection** 分开。先让 student 生成自己真实会访问的
prefix，再让 teacher 在同一 prefix 上给分布，可以减少纯 teacher trajectory 带来的 state mismatch；但如果
所有 token 都同权更新，容易把已一致的低价值位置与真正不确定、分歧大的决策混在一起。一个有界演进是：

```text
student-owned rollout and prefix
→ teacher distribution on the same prefix
→ entropy / teacher-student disagreement as diagnostic state
→ bounded token selection or weighting
→ outcome and regression evaluation
```

Entropy 表示 student 不确定，分歧表示 teacher 与 student 不同；二者都不是 correctness。TIP 的四象限选择和
Rethinking On-Policy Distillation 的作者实验只证明在其模型、数据和评测下某些 token allocation 更有效，不能
把高熵或高分歧直接当作因果 credit。固定全 token distillation 在算子成熟、差异较均匀或需要最简单 objective
时继续成立；选择性更新必须保存 threshold、teacher/student snapshots、mask 与被排除 token 的 regression 证据。

### Prefix Replay 同时承担复用与 Distribution-shift 债务

Fully online distillation 让 student 在自己访问到的 history 上得到 teacher conditional，能减少纯 teacher
demonstration 的 state mismatch，却必须反复执行 environment、tool 和 teacher；直接重放 teacher 的最终 action
最便宜，但 student 从自己的早期错误分叉后便失去覆盖。多轮环境中可以复用包含 observation 的 teacher prefix，
只让 student 在被监督 step 生成 action，再在同一 prefix 上查询 teacher distribution：

```text
versioned teacher trajectory and environment observations
→ sample a prefix / step under an explicit reliability schedule
→ student generates the current action only
→ teacher returns token conditionals on the same prefix
→ KL update without live environment execution
```

它降低在线 environment cost，却没有消灭 on-policy gap，而是把 gap 拆成两部分：replayed prefix 不是 student
occupancy；teacher 在较晚或异常 prefix 上也可能不可靠。按 step 衰减采样只是 reliability proxy，不是 correctness
证明。Prefix pool 因而必须绑定 teacher、environment、tool/schema、observation、student checkpoint、sampling
schedule 与 expiry；stale observation、support hole 和 mixed-version pool 都要能被审计。Online OPD 在环境便宜、
需要探索失败恢复时仍合理；普通 offline SFT 在没有 teacher logits 或只需行为复制时更简单。ReOPD 的作者实验
只支持其 math/search 合同中的成本与质量折中，不证明固定加速倍数或跨环境优势。

另一条 weak-to-strong 分支不模仿弱 teacher 的最终 policy，而在 strong student 自己的 prefix 上转移
`post-RL teacher / pre-RL reference` 的 token log-ratio。它试图转移的是“RL 改变了哪些相对偏好”，不是弱模型
的绝对能力上限；代价是双 checkpoint identity、top-k coverage、KL/length sensitivity 与额外 on-policy query。
只有 teacher shift 在 student states 上仍有意义时，这种 dense signal 才成立。它与 prefix replay 解决不同问题，
不能合并成一个默认 distillation recipe。

移动端或 GUI Agent 的 demonstration 还包含环境 intervention，而不只是文本答案。Synthetic trajectory 若
允许 generator 读取 privileged app state、全局地图或自动纠错器，训练 artifact 必须明确哪些 observation 在
部署时可见、哪些只用于生成/过滤：

```text
privileged environment trace
→ observable-state projection
→ action / recovery demonstration
→ executable replay and filter
→ SFT release artifact
```

OpenMobile 一类流水线支持用自动交互扩大轨迹覆盖，却把 app/version drift、reset、pHash/annotation error 与
global environment memory 写进数据合同；它不证明真实设备成功率可由 synthetic replay 外推。类似地，
Self-Distillation Zero 让后续尝试或 reviser 使用 privileged future evidence 时，teacher/reviser state 必须与
student deployment state 分离；future attempt 只可生成受验证 target，不能在评测时泄漏给 student。

因此技术演进不是单向替代：prompt-only control 适合可逆、按请求变化的 policy；filtered short-trace SFT
适合有可信 demonstrations 时直接监督目标轨迹；outcome RL 适合结果可验证且需要 exploration 的任务；
context distillation 则适合希望保留 student 自身 state coverage、又把稳定 prompt 行为迁入权重的场景。

部署经验还可以沿同一接口继续进入参数，但必须多一道 derived-state 边界。客户端先保存带环境 provenance
的成功/失败 trajectory，server 让当前 policy 将其压缩为可迁移策略；冻结 teacher 读取“策略 + student
prefix”，student 只读 prefix，并在 student 自己访问到的状态上完成 context distillation：

```text
raw deployment episode
→ provenance-preserving derived strategy
→ same-prefix on-policy distillation
→ versioned checkpoint
```

这不是把 Memory 简单“写进权重”。参数化降低以后每次调用的 Context 成本，却削弱按用户隔离、精确
删除和即时回滚，并新增 consent、poisoning、teacher staleness 与 forgetting。Raw episodic memory 在需要
纠错、审计和个性化时仍合理；高风险环境应先通过独立质量与隐私 Gate，再允许 derived strategy 进入训练。

### Demonstration Schedule 也是 Objective 的一部分

一次看到更多不同样本通常提高 coverage，但长 reasoning demonstration 中真正决定策略的稀有转折可能只出现
一次，容易被大量常规 token 稀释。重复同一 verified trajectory 能增加它在经验风险中的权重，却不会创造新证据：

```text
verified long trajectory
→ repeat or resample under an explicit schedule
→ change token-level gradient frequency
→ monitor exact-task gain, transfer and memorization
```

因此 repetition 是 sampling policy，不是“免费增加数据”。它可能强化关键长程结构，也可能记住答案、压低分布覆盖、
放大 demonstration error。旧的 broad-mixture SFT 在迁移和抗记忆优先时仍成立；只有在 trajectory 已独立验证、重复率
与总 token budget 一起报告，并用 held-out variants 区分结构学习与逐字记忆时，重复 schedule 才是可解释 actuator。

On-policy distillation 则处理另一种偏移：offline teacher traces 质量高，但 student 运行时会访问 teacher 从未写过的
prefix。让 student 先采样自己的 trajectory，再在这些 prefix 上读取 teacher/reference logits，可把监督移到当前
policy state distribution；reward extrapolation 或 KL constraint 只负责在 teacher 覆盖之外限制更新，不能证明这些
状态本身正确。系统必须绑定 rollout policy、teacher/reference snapshot、tokenizer、reward 和 refresh cadence。
Offline distillation 在 teacher 输出可预计算、成本和稳定性优先时仍更简单；on-policy 路线以额外 generation、teacher
forward、policy lag 和 self-reinforcing failure mode 换取更小的 state-distribution mismatch。

On-policy distillation 还可按 source rollout 的 advantage 选择 teacher anchor：高价值状态更靠近 teacher，
低价值或错误状态允许更强纠正。这比统一 KL 更贴近 deployment distribution，却把 reward/verifier calibration、
teacher revision 与 coefficient endpoint 写进 objective；公式与 prose 的端点若冲突，不能自行选择有利解释。
固定 offline KD 在成本、稳定性或 source probability 不可得时继续合理。RLAD 只提供受限实验，不证明
advantage-conditioned anchor 在所有 reasoning policy 上优于统一 teacher constraint。

### 一个 Mixture 不必共享同一个 Stopping Point

随机混合多个任务并使用统一 compute budget，能避免 sequential SFT 的次序遗忘，且 controller 简单；
但各任务收敛速度不同后，同一 checkpoint 可能同时让快任务过拟合、慢任务欠拟合。预先独立测量每个任务
的最佳 epoch 也不充分，因为移除一个任务会改变 aggregate gradient，剩余任务的 stopping point 会随之移动。

一种实验性控制回路是保存 active dataset set、per-task held-out metric、compute cursor 与 rollback
checkpoint：在当前 mixture 上推进一段，识别最早越过 peak 的任务，回退到它的 peak checkpoint，将其从
active set 移除，再在新的 gradient field 上重新估计其余 stopping point。它把 schedule 从一个标量升级为
可恢复的 SFT state machine，也付出多次 rollout、checkpoint footprint、评测泄漏与 hard exclusion 的代价。
任务动态相近、held-out oracle 不可靠或存储预算紧张时，统一 global budget 仍更稳健；软降权也可能比直接
删除更适合需要持续抑制 forgetting 的任务。

### Scaffold-bound specialization：环境协议也是监督分布

Coding Agent 的 demonstration 不只包含代码，还包含 repository layout、tool schema、termination rule、
error recovery 与 scaffold prompt。若只在一种 harness 上训练，模型可能学会协议捷径而非可迁移能力；同时混合
许多 scaffold 又会扩大格式冲突和 regression matrix。更可审计的演进是：

```text
general code/model checkpoint
→ executable repository tasks with scaffold identity
→ scaffold- or domain-specific SFT/RL experts
→ per-domain retention and cross-scaffold evaluation
→ distill into one deployment artifact, or keep experts separable
```

合并 artifact 减少在线 routing 与运维成本，却可能掩盖 negative transfer；保留专家便于独立 rollback，却增加 serving
状态和选择策略。无论哪条分支，teacher/expert checkpoint、task environment、tool template、reward/verifier 与
distillation dataset 都必须有 lineage。Qwen3-Coder-Next 报告为这条 staged specialization 提供了厂商实验，
但其模型规模、任务数量、context 长度和 benchmark 结果不是通用训练配方，完整训练实现也未公开。

当任务目标是产生可执行 artifact，而不是复述答案时，synthetic demonstration 还可从 answer-only 扩展为
environment-grounded interaction：先生成带 validator 的合成任务，让 teacher 在 sandbox 中完成、调试并留下
trajectory，再只把通过独立 outcome Gate 的轨迹交给 student。它能把 tool use、失败恢复和 artifact state
带入 SFT，却也可能让 task generator、teacher 与 validator 共享同一 blind spot。静态人工 demonstrations
在需求难形式化、artifact 有副作用或独立 verifier 不存在时仍更可信；合成任务规模不能替代 held-out transfer、
污染审计和 compute accounting。

### Distillation 的隐私边界：较少 Memorization 不等于隐私保证

Hard sequence distillation 在只有 black-box teacher output 时可行：teacher 先生成目标序列，student 再以
cross-entropy 拟合；soft logit distillation 则让 student 拟合 teacher 的完整概率分布。Soft targets 允许容量
较小的 student 在高不确定样本上保持更平坦的分布，而不是被 one-hot target 强迫高置信记忆，因此可能形成
regularization；但这种机制不会自动删除 teacher provenance，也不是 Differential Privacy。

设计与审计应分开记录：

```text
teacher checkpoint and training-data lineage
+ student initialization / capacity
+ soft or hard objective, KL direction and temperature
+ distillation dataset and teacher-output artifact
+ extraction definition, prefix/suffix length and decoding rule
+ utility, memorization and privacy-attack results
```

受控实验显示 soft/hard objectives 可以产生不同的 teacher-specific memorization inheritance，但结果绑定
模型家族、数据集、精确匹配式 extraction 与训练设置。不能据此宣称 KD 是隐私防护，也不能把较低可发现
memorization 等同于 membership、attribute 或其他攻击风险下降。若 privacy 是硬约束，仍需数据治理、
deduplication、access control、attack-specific evaluation，必要时使用带 accounting 的 DP；hard distillation
在 teacher logits 不可得时继续有工程价值，只是其输出数据也必须作为敏感衍生 artifact 管理。

## Full fine-tuning 与 parameter-efficient adaptation

Full SFT 更新全部参数：

```text
theta <- theta + Delta theta
```

它提供最大的更新自由度，也需要保存全部 gradients、optimizer states 和新模型权重。

第 30 章 LoRA 将更新限制为低秩 adapters：

```text
theta_base frozen
Delta theta represented by small trainable factors
```

两者可以使用相同 SFT data 与 token loss。LoRA 是参数化和训练状态选择，不是另一种 supervision objective。

## Catastrophic forgetting 与能力回退

若 SFT 数据分布很窄、learning rate 过大或训练过久，模型可能提高目标任务表现，却损伤通用能力。表现包括：

- 回答风格过度统一。
- 多语言或代码能力下降。
- 所有问题都触发相似模板。
- 事实知识被局部错误 demonstration 覆盖。
- 拒答边界过宽或过窄。

缓解方法可能包括混入部分 pretraining/domain data、降低 update magnitude、增加数据多样性、使用 adapters 或早停。但每种方法都重新定义训练分布，必须通过 multi-slice Evaluation 验证。

## SFT 能否注入知识

模型可能从 SFT examples 学到新事实或领域映射，但这不是可靠知识管理协议。少量参数更新可能：

- 只对相似 wording 有效。
- 与旧知识冲突。
- 造成无关行为变化。
- 难以追踪、更新或删除。

需要频繁更新、可引用或权限敏感的知识，通常还要考虑 Retrieval、tool 或外部 state。SFT 更稳定的角色是塑造行为和任务接口，而不是替代所有知识系统。

## SFT 不能表达“哪个回答更好”

Demonstration 只给出一个目标 response。它没有直接说明：

- 另一个回答差在哪里。
- 两个都可接受但哪个更好。
- Helpfulness 与 safety 冲突时怎样权衡。
- 输出偏离 reference 文本但仍正确时是否应奖励。

把唯一 reference 当作所有正确表达，会惩罚合理多样性。第 31 章从 preference pairs 和 reward modeling 开始处理相对判断；第 34 章 DPO 则直接用 chosen/rejected pairs 优化策略。

## 训练与 Serving 的接口一致性

上线前至少要核对：

- Tokenizer、special token ids 与 chat template。
- System/user/assistant role 顺序。
- BOS/EOS 的添加位置。
- Generation stop conditions。
- Tool schema 与 structured-output grammar。
- Adapter/base checkpoint 版本。

模型训练得到的是 token-level protocol。Serving 层若重新拼接字符串或重复添加 special tokens，会让模型面对训练中未见的 prefix。

## Evaluation 应分开能力与行为

SFT 后应同时比较：

- Instruction-following 与格式成功率。
- 任务正确率、事实性和代码执行结果。
- Safety、refusal precision/recall。
- 通用能力和多语言回归。
- 输出长度、verbosity 与 latency/cost。
- 对 prompt phrasing 和 system policy 的鲁棒性。

Training loss 只衡量对 demonstrations 的拟合。若 validation set 与训练模板高度相似，它也可能高估真实产品分布上的泛化。

## 本章在知识树中的位置

```text
pretrained checkpoint
+ instruction demonstrations
+ chat template / loss mask
-> SFT objective
-> instruction-following checkpoint
-> LoRA or full update
-> preference optimization
```

本章把第 28 章的通用 next-token learner 转成可交互模型。第 30 章改变更新的参数化成本，第 31～34 章加入相对偏好，Part VII 再把 prompt、tool 与 workflow 组织成运行时协议。

## 自检问题

1. Pretraining 能续写文本为什么不等于稳定遵循指令？
2. SFT 与 Pretraining 为什么可以使用同一种 cross-entropy？
3. Response-only loss 中 prompt tokens 发挥什么作用？
4. Loss mask 错位会产生什么训练错误？
5. Chat template 为什么属于 checkpoint 接口？
6. 少量 SFT 数据有效为什么不是固定规模定律？
7. Synthetic demonstrations 会引入哪些新偏差？
8. Full SFT 与 LoRA 的 objective 有什么关系？
9. 为什么 SFT 不是可靠的动态知识管理方案？
10. Demonstration 数据为什么不足以表达相对偏好？
11. Context distillation 与“让 teacher 生成一条新答案再做 SFT”有什么机制差别？
12. 为什么 teacher refresh cadence 属于可恢复训练状态，而不只是一个普通超参数？

## 小结

SFT 通过 demonstrations 和 loss mask，把 pretrained model 的开放续写分布收窄为目标交互行为。它仍然执行 token-level maximum likelihood，但数据 schema、角色协议与监督位置改变了模型被奖励的行为。

SFT 可以显著改善指令遵循、格式和风格，也可能导致过拟合、遗忘或错误行为固化。它需要和任务正确性、安全、通用能力回归以及 Serving protocol 一起评估。

## Review notes

- Simple Self-Distillation（sampling-shifted self-target；Status: Experimental）: https://arxiv.org/abs/2604.01193

本章将 SFT 定位为 demonstration imitation，明确 response-only masking、chat template、full/LoRA 参数化和 knowledge injection 边界。Preference ranking 与 reward optimization 留给第 31～34 章，Prompt 与 tool runtime 留给 Part VII。

2026-W10 的 CRISP/OPSDC 案例用于补全同-prefix context distillation、periodic teacher ownership 和
brevity/correctness/format 的评估解耦。其公开结果仍是单篇预印本的实验，且较早 revision 的部分准确率
差异受单路径答案格式 scorer 影响；正文不保留 benchmark 数字或固定 refresh recipe。

Primary-source 校验入口：

- Jason Wei et al., "Finetuned Language Models Are Zero-Shot Learners", 2021: https://arxiv.org/abs/2109.01652
- Victor Sanh et al., "Multitask Prompted Training Enables Zero-Shot Task Generalization", 2021: https://arxiv.org/abs/2110.08207
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Hyung Won Chung et al., "Scaling Instruction-Finetuned Language Models", 2022: https://arxiv.org/abs/2210.11416
- Mistral AI, "Ministral 3" technical report（Cascade Distillation case；2026 disclosure）:
  https://arxiv.org/abs/2601.08584
- Hyunjae Sang et al., "CRISP: On-Policy Self-Distillation for Reasoning Compression", 2026
  （Status: Experimental；历史事件为 v1 OPSDC，当前标题来自后续 revision）:
  https://arxiv.org/abs/2603.05433
- Memorization Dynamics in Knowledge Distillation（soft/hard KD 的受控 extraction evidence；不构成隐私保证）:
  https://arxiv.org/abs/2601.15394
- D-CORE（decomposition-aware tool-use SFT/RL；Status: Experimental）: https://arxiv.org/abs/2602.02160
- Data Repetition for Long-CoT SFT（Status: Experimental）: https://arxiv.org/abs/2602.11149
- Generalized On-Policy Distillation（Status: Experimental）: https://arxiv.org/abs/2602.12125
- ReOPD（multi-turn prefix replay；Status: Experimental）: https://arxiv.org/abs/2607.04763
- Weak-to-Strong Direct OPD（relative policy-shift transfer；Status: Experimental）:
  https://arxiv.org/abs/2607.05394
- Qwen3-Coder-Next Technical Report（scaffold-bound staged specialization 与 expert consolidation；
  Status: Experimental）: https://arxiv.org/abs/2603.00729
- Reinforcement-aware Knowledge Distillation（advantage-conditioned teacher anchor；Status: Experimental）:
  https://arxiv.org/abs/2602.22495
- AI Scientist via Synthetic Task Scaling（executable synthetic demonstrations；Status: Experimental）:
  https://arxiv.org/abs/2603.17216
- mSFT（Status: Experimental；heterogeneous task stopping 与 mixture-dependent rollback）:
  https://arxiv.org/abs/2603.21606
