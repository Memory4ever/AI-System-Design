# 第27章 数据

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-DATA`
**Legacy Chapter:** Ch23
**Status:** Draft

**Roadmap Intent:** 数据质量、分布、清洗、去重、配比决定模型上限。

## 本章要回答的问题

Part II 已经解释通用模型怎样把 token 变成答案，Part III 又定义了跨模态 representation、生成、环境状态与 action contract；但参数最初并不知道语言、图像、物理或世界知识。什么数据应该进入训练？为什么“更多 token”不等于“更多有效能力”？清洗、去重、配比、污染控制与 provenance 怎样共同决定模型最终优化的是哪个分布？

本章的核心判断是：**训练数据不是等待模型消费的原料，而是对模型行为分布的可执行 specification。**收集、过滤、去重、配比和采样共同定义经验风险中的样本权重；数据 pipeline 的任何偏差，都会通过梯度进入 checkpoint。

本章使用 `x` 表示一个训练样本或 token sequence，`q(x)` 表示训练数据分布，`q_k(x)` 表示第 `k` 个数据域的分布，`alpha_k` 表示该域的采样权重，`T` 表示 sequence length，`N` 表示训练 token 数。

## Part IV 的能力生产链

Part IV 不按工具目录组织，而按能力与训练状态怎样演化组织：

```text
Data
-> Pretraining
-> SFT / LoRA
-> Preference data and reward
-> PPO / GRPO / DPO
-> Checkpoint
-> Distributed Training
-> TP / PP / ZeRO
-> Megatron / DeepSpeed runtime
```

多模态 raw sample、codec token、frame/second 和 action trajectory 不能用一个未经定义的“token 数”混合计量。第23～26章拥有表示与行动语义；本章拥有这些样本怎样被选择、版本化、配比与送入优化。这个边界使 representation 研究不会寄居于 Data，也使 Data 不退化成文件清单。

第 27～34 章主要回答“优化什么行为”，第 35～41 章主要回答“怎样可靠保存并扩展这段优化过程”。后半段不能反过来证明前半段的数据和目标正确；更高 GPU utilization 只意味着更快执行既定训练 specification。

## 先从“把互联网都抓下来”开始

最朴素的数据方案是收集尽可能多的网页、书籍、代码和对话，然后直接进行 next-token training。它看似最大化覆盖，实际会同时引入：

- 重复页面、镜像站点和模板文本。
- 垃圾内容、SEO 文本、乱码和机器生成污染。
- PII、版权、许可和删除请求风险。
- 语言、领域与时间分布失衡。
- Evaluation benchmark 或答案泄漏。
- 极端长短样本和不可控 token efficiency。

模型不会自动知道哪些内容是“高质量事实”，哪些只是高频重复。若某段文本出现一千次，它在经验风险中获得的权重就可能接近一千个独立样本，即使重复并没有增加新信息。

所以数据工程的目标不是让磁盘尽可能满，而是构造一个有来源、可解释、可复现、与能力目标匹配的训练分布。

## Collection protocol 为什么先于 Filtering 定义数据

“先收集、再清洗”容易让人误以为 raw data 是自然存在的客观样本。对语音、图像、交互轨迹、
专家示范和安全数据，样本往往由采集系统主动产生：向谁提问、展示什么刺激、允许多长回答、
在什么环境记录、由谁标注，都会决定哪些行为有机会进入 dataset。

```text
capability / deployment target
-> target population and task
-> collection or elicitation protocol
-> annotation and quality-control policy
-> governed data partitions
-> train / validation / test split
-> model outcome
```

因此 collection protocol 不是 filtering 之前的中性搬运步骤，而是 `q(x)` 的上游生成机制。
例如，scripted read speech 可以控制音素覆盖、说话人和声学质量，适合语音合成；自然环境中的
image-prompted description 更容易产生 spontaneous speech、停顿和 code-switching，适合另一类语音识别
分布，却增加转写、内容审核和复现成本。后者没有让前者过时；两种 acquisition path 服务不同的
task contract，混在一个“speech hours”数字里反而会丢失最重要的语义。

主动采集还要求把 ownership 与 policy 下沉到 partition，而不是只给顶层 dataset 一个名称：

```text
partition identity
+ source / collecting organization
+ population, task and recording environment
+ speaker or subject identity policy
+ consent scope and withdrawal path
+ license and derivative obligations
+ schema and annotation version
+ split rule and group-disjoint key
+ manifest digest and supersession history
```

同一 dataset 中不同 provider、语言或模态可能拥有不同 license、consent scope 和可删除性。顶层页面写着
“open”或“permissive”不能替代 partition-level authorization；论文、发布页和 dataset card 对规模或许可
不一致时，也不能挑选最大的数字继续训练。Consumer 应锁定实际读取的 immutable manifest、schema、
policy 与 digest，并把 correction、withdrawal 和 supersession 传播到 derivatives 与 checkpoint lineage。

Train/eval split 同样属于采集合同。随机按 rows 切分可能让同一 speaker、用户、文档或 session 同时进入
train 与 test，从而把 identity overlap 当成泛化。系统应先声明 deployment 中需要泛化到什么单位，再选择
speaker-disjoint、user-disjoint、source-disjoint、time-based 或其他 group split。未公开 split algorithm 时，
`80/10/10` 只说明比例，不能证明 leakage 已被控制。

删除 transcript 中的直接 PII 也不等于匿名化完成。Voice、face、writing style 或行为轨迹本身可能携带
可推断身份和敏感属性。更可靠的设计要同时保存 collection purpose、risk review、access/retention policy、
withdrawal semantics 与 downstream-use boundary，而不是把伦理问题压缩成一个 `pii_removed=true` 字段。

## 数据分布就是优化权重

Pretraining 最小化训练分布上的期望 loss：

```text
R(theta) = E_(x ~ q)[L(theta; x)]
```

实际只能使用有限数据集：

```text
R_hat(theta) = (1 / n) * sum_(i=1)^n L(theta; x_i)
```

如果数据来自 `K` 个 domains，可以把采样分布写成：

```text
q(x) = sum_(k=1)^K alpha_k * q_k(x)

alpha_k >= 0
sum_k alpha_k = 1
```

`alpha_k` 不是中性的 loader 参数。它决定每个 domain 产生梯度的频率。代码占比增加，可能提升代码能力，也可能压缩自然语言、特定语言或长尾知识的有效训练预算。

数据配比因而是一种多目标优化：不同 domain 的 loss、能力收益、重复率、质量和合规成本并不相同。不存在脱离模型规模、token budget 与 Evaluation 的通用最优比例。

### Data Reuse 改变的是 Layer-wise Growth，不只是 Epoch 计数

在数据充足、样本近似独立时，扩大 unique corpus 是最直接的能力来源；数据稀缺后重复采样可以让优化器继续沿已有方向下降，却也可能把少数模式放大。更细的解释应把 reuse schedule、sampling bias 与 layer-wise relative norm 一起记录：data loader 拥有样本出现频率，training telemetry 观测各层增长，controller 才能判断重复是在加速尚未学完的结构，还是只强化已占优模式。

重复可能提高有限数据的 compute 利用率，也增加 overfitting、层间失衡和分布偏置；小数据上的速度收益不能自动变成更多 unique data 下的结论。数据充分或 reuse signal 与 held-out capability 冲突时，应回退更低重复率和静态 mixture。`arXiv:2605.20314v1` 的 §2–§5 只支持其 sampling-bias、relative-norm mechanism 与 interventions，§6 明确 repetition 何时不成立；它不证明重复数据普遍优于新增数据。

<!-- source-family:SF-2026-ARXIV-2605-20314 -->

### 静态 Mixture 到版本化 Data Control Plane

固定 `alpha_k` 最容易复现，也能在各 domain 收敛速度相近时避免 controller 噪声；但真实训练中，选择、
混合与加权可能需要读取不同信号，并以不同 cadence 变化。更清楚的系统分解是：

```text
immutable source rows and provenance
→ versioned data operators: select / transform / mix / weight
→ observation signals: embedding / loss / gradient / validation
→ bounded mixture proposal
→ checkpointed active set, weights and cursor
→ independent held-out evaluation
```

这里 data operator 只提出训练分布，training controller 拥有 active set、采样权重、cache 与更新时机，
Evaluation 仍决定变化是否可接受。动态策略能把不同阶段的 data need 写进控制面，却新增 feedback delay、
validation leakage、oscillation、distributed-state access 和恢复问题。来自 Web Agent 的 trajectory 还必须保存
teacher 与 student 的 observation modality、action abstraction、browser/environment revision、verifier 和
side-effect policy；否则 privileged structural teacher 编译出的 screenshot-only 行为会失去关键 lineage。

这不是静态清洗和配比的淘汰。信号噪声大、训练短、审计复现优先或 controller 成本高时，冻结 manifest 与
mixture 仍更可靠。阶段化 data pipeline 与动态 control 的论文只证明各自 workload 中的可行机制，不提供可
跨模型照搬的比例、stage 或演化律。

## 一个三域配比小例子

假设训练每 1000 个 sequences 期望采样：

```text
Web   alpha_web  = 0.60 -> 600 sequences
Code  alpha_code = 0.25 -> 250 sequences
Math  alpha_math = 0.15 -> 150 sequences
```

若原始数据库存量为：

```text
Web  = 90%
Code = 8%
Math = 2%
```

那么训练分布已经对 Code 和 Math 做了上采样。若 token budget 固定为 `N`，增加 `alpha_math` 不会凭空增加预算，而是在重新分配其他 domains 的训练机会。

这个例子也说明“数据占比”必须注明单位。按 documents、characters、bytes 或 tokens 统计，会得到不同结果；训练计算最直接对应的是实际进入 loss 的有效 tokens。

### Data tags 也可能训练一条隐式控制策略

Data mixture 不只决定模型“学什么内容”。当样本带有 task、mode、tool 或 budget tag 时，模型还会学习
“在什么输入下选择哪种行为”。例如，同一 checkpoint 的一部分 demonstrations 以 direct-answer marker
开始，另一部分以 reasoning marker 开始，SFT 实际同时训练了内容分布和一个隐式 mode policy：

```text
task features + data mixture + mode tag
-> learned mode probability
-> output length / tool path / sequential compute
```

这比始终使用长 reasoning 节省平均 token，也比维护两个独立模型减少 artifact 与 capacity 分叉；代价是
mode boundary 来自训练分布中的 correlation，未必对应真实 uncertainty、evidence sufficiency、latency SLO 或
cost。显式 tag 还可能成为 prompt injection 或错误 override 的控制面。Separate models、外部 router 和固定
single mode 在严格隔离、可预测 SLO 或控制策略尚未校准时仍然合理。

多模态数据会让同一问题进一步前移。Image processor 选择 resolution、crop 和 visual-token budget，决定
Transformer 最多能看到哪些证据；提高 token budget 可能改善细粒度 grounding，也会增加 context、Attention、
TTFT 与 KV 成本。数据系统因此应把 `source image -> transformation -> visual tokens -> task/mode label` 保存为
同一 lineage，而不能只保存原图 URL 和最终文本。模型后续的 reasoning 无法恢复 featurization 已经丢弃的证据。

这里的长期结论不是某个 reasoning/direct 配比或 visual-token 上限，而是：**当数据字段会改变控制流或计算量，
它就属于可执行 training policy，必须与 serving policy 和 evaluation workload 一起版本化。**

## Quality filtering 在过滤什么

质量不是单一分数。数据 pipeline 可能组合：

- 规则过滤：语言、长度、字符分布、重复符号、HTML 结构。
- 内容分类器：教育价值、可读性、主题、安全或垃圾概率。
- Source-level policy：来源许可、可信度、时间与地域。
- Model-based filtering：使用模型对文本质量或目标相关性评分。

过滤器会降低明显噪声，也会带来选择偏差。规则可能误伤代码、公式、方言或低资源语言；模型过滤器会继承评分模型的偏好；过度追求“教科书风格”可能减少真实世界多样性。

因此过滤策略需要同时报告 retention rate 和分布变化，而不能只报告“删除了多少低质量数据”。删除前后各语言、领域、长度和来源发生了什么，才决定模型看见了什么。

### Filter Threshold 必须绑定 Compute-to-Unique-Data Regime

在 compute 少、原始数据多时，高阈值过滤可以减少明显低质 token；当 compute 已能多次覆盖稀缺 corpus 时，继续追求更纯的小集合会同时提高重复率并丢失长尾。Filter owner 因而要把 retained unique tokens、expected passes、model/compute scale 与 domain coverage 绑定到同一 manifest，再用 held-out capability 验证，而不是复用固定 quality score。

扩大 retained set 保留多样性，却带回噪声、许可与训练成本；收紧 threshold 提高平均质量，却可能在 high-compute/data-scarce regime 过早耗尽新信息。数据充足、预算低或风险语料明确时，传统高阈值过滤仍合理。`arXiv:2605.19407v1` 的 §3–§7 只支持其 compute/data/filter scaling studies，§8 不证明某一 filter 或 threshold 跨模型、token budget 与领域保持最优。

<!-- source-family:SF-2026-ARXIV-2605-19407 -->

### 内容无害不等于更新无害：过滤器还要预测 Training Effect

按主题、安全分类或表面质量过滤 benign SFT data，在样本风险与参数更新方向高度相关时便宜而合理；但微调会改变
模型内部的 compliance boundary，一条内容本身无害的样本仍可能沿着与拒答能力相关的表示方向推动参数。约束从
“这条文本说了什么”变成“这条文本在当前 checkpoint、训练 recipe 下会造成什么更新”后，filter artifact 需要同时
记录内容判定与有限的 training-effect evidence：用于抽取 compliance direction 的 checkpoint、被选中的
safety-critical layers、projection score、threshold 以及最终 admission decision。数据 pipeline 拥有这份证据与
decision lineage；trainer 只能消费已版本化的过滤结果，不能把训练后才出现的 safety regression 追溯成一个无身份的
“数据质量问题”。

这种机制用额外 forward/probe 成本、checkpoint coupling 和误拒绝 benign diversity，换取在训练前发现一类表面过滤器
看不到的 safety-degrading samples。Compliance direction 可能随模型、adapter、数据顺序和 safety policy 漂移，layer
selection 也可能把 correlation 误写成因果；因此它不能取代内容过滤、训练后 safety regression 或 held-out red-team。
Probe 未校准、目标 checkpoint 不同或误拒绝成本过高时，保留传统过滤并在小规模 canary 上验证更新仍是更稳健的旧路径。
`arXiv:2606.00160v1` 的 §IV 与 §V 只支持作者披露模型和任务中的 compliance-vector extraction、layer selection 与
过滤实验；§VI 不证明相同方向、阈值或层集合能跨模型族、训练配置和生产安全边界复用。

<!-- source-family:SF-2026-ARXIV-2606-00160 -->

### Synthetic data：从“先生成再打分”到 Specification Compilation

最直接的 synthetic-data pipeline 是让模型生成任务、回答或 Agent trajectory，再由另一个 model judge
过滤。它便宜、覆盖开放语义，在 verifier 难以形式化的任务中仍然合理；但 generator 和 judge 可能共享
事实错误、风格偏好与同源 blind spot，语言上自洽不等于环境中可执行。

当 task schema、sandbox state 和 tool effects 可形式化时，可以使用更强的编译式路线：

```text
versioned executable state
-> sample satisfiable constraints
-> fuzzify into natural or ambiguous request
-> generate interaction trajectory
-> verify final state against original constraints
-> retain as SFT data or map verdict to RL reward
```

它把 ground truth 放在语言生成之前：task 与 verifier 从同一 executable specification 派生，因而能降低
不可解任务和 judge ambiguity。Verifier 应检查 outcome，而不是强制唯一 action sequence，否则合法替代路径会
被误判。Constraint identity、fuzzifier、simulator/disclosure policy、environment revision、trajectory 与 verifier
version 都要进入 row lineage；只保留最终对话会丢失样本为什么“正确”的证据。

这条路线也产生新的上限：generator 和 verifier 共享同一 ontology，可能同时漏掉 safety、privacy、未编码的
用户意图或不可逆副作用。`deterministic` 只表示相对于已编码 constraints 可重复，不表示 specification 完备或
现实世界绝对正确。高风险和开放语义任务仍需 independent oracle、human audit、held-out verifier 与真实用户分布
校准；同一 verifier 若同时筛选 SFT data、提供 RL reward 和评估模型，尤其需要防止 measurement channel 被优化。

当工具本身是事实来源时，Specification Compilation 还可以反转常见的 query-first 顺序。先写问题再尝试验证，在工具少、
API 稳定且有人工清洗时很直接；tool pool 扩大到跨 domain、stateful protocol 后，它会生成大量当前环境根本无法回答的任务。
Evidence-first 路线先执行真实工具形成可追溯 evidence set，再反推只由该 trace 支持的 query 与 answer：

```text
versioned toolset and environment
-> bounded real execution trace
-> evidence set with provenance
-> entailed task / answer synthesis
-> independent validity and coverage checks
```

它提高 solvability，却把任务支持域限制在当前工具能返回的内容，并继承 provider coverage bias、结果 freshness、outage 与 policy
变化。`task + toolset + evidence + verifier` 必须是同一版本化 family，不能只保存语言 row。DIVE 的作者实验支持该顺序在其
工具环境中减少不可解样本并增加结构多样性，不证明 `diversity > quantity` 是跨模型、跨 API 的通用定律。Query-first 在需要
反事实、极端边界或尚无真实 evidence 的能力规划中仍有价值；更稳健的组合是 evidence-first 保证 grounding，再由独立 spec、
adversarial generator 与人工审计补 coverage。

搜索与多模态任务进一步要求 evidence 不是一段无来源文本，而是可重放的结构。可先从 seed source 构建
带 provenance 的 entity/document graph，筛掉 closed-book 已可回答的问题，再让 teacher 在受控摘要与
原始 observation 之间生成 tool trajectory；student 训练时只能读取部署态可见的 observation。这样能把
难度、可回答性和来源绑定起来，却也引入 oracle-subgraph leakage、网页漂移、teacher privileged-state
泄漏与 search backend 偏差。

视觉多跳数据同理：从带 object evidence 的图像出发，构造 dependency-constrained questions，并要求
每一 hop 的 grounding 都可验证，比只保存 image-answer pair 更能暴露视觉证据链。但 segmentation、
annotation 与 verifier 共享错误时，“可验证”仍只相对于该 pipeline 成立。结构简单、人工 gold evidence
充足的领域继续适合 curated QA；graph-grounded synthesis 是补充 coverage 的分支，不是替代人工数据。

#### 没有真实后端时，Synthetic API State 只能是派生训练状态

当 API specification 存在而 executable backend 尚未部署时，可以让 teacher 提议调用、由 history-conditioned simulator 生成 response，再用 schema/argument checks、语义一致性 judge 与 trajectory vote 筛选 SFT trace。这比 single-call 合成更能覆盖 stateful transition，却不能把 simulator response 升格为环境事实。

Lineage 必须保存 specification revision、task proposal、simulator identity、每次 synthetic transition、过滤 verdict 与最终 real-environment evaluation；还要报告 API × transition coverage、长响应 failure、judge disagreement 与 rejected trace。真实 backend 仍是 effect authority。这条分支用覆盖与成本换取 simulator/judge bias，适合训练 proposal，不适合证明真实 side effect；有可执行环境时，evidence-first 或 specification compilation 仍更强。

### Failure-driven Curriculum：难例必须来自可重放失败，而不是模型自信

随机合成 tool trajectories 覆盖面广，但常把概率质量花在短、浅、同质调用上。若已有可执行 tool environment，
可以先运行多个 baseline，找出重复失败的 tools、parameter constraints 与 dependency paths，再从这些失败区域
生成更难 query、tool variant 或多步 trace：

```text
versioned tool environment
→ baseline execution and failure attribution
→ failure-prone dependency subgraph
→ hard query / tool evolution proposal
→ executable reasoner-verifier loop
→ retain only outcome-valid trajectories
```

这里 failure signal 是 curriculum proposal，不是 ground truth。它会偏向当前 baseline 的 blind spots，也可能
把 harness bug、tool overlap 或 judge bias放大成训练分布。Hard tool 的新增 schema 与 behavior 必须进入 environment
version；trajectory 只有在完整多步 outcome、参数与 side effect 都可验证时才进入 SFT/RL data。失败来自不可调用的
proprietary API、外部世界不可逆动作或缺少 oracle 时，随机/人工数据仍可能比伪造 executable correctness 更诚实。

HardGen 在作者构造的 2,095-tool environment 和 BFCL evaluation 上为这条路线提供了受限案例；其 generator、
judge、verifier 与 benchmark 仍可能共同贡献结果，也没有证明超出该工具分布的通用 Agent 能力。正文因此吸收
“failure attribution → curriculum → executable verification”的 lineage，不保留模型排名、数据量或 headline gain。

Terminal 与 repository 任务进一步说明，训练 row 的最小单位不能只是 instruction/response。可执行能力来自
task intent、初始 filesystem/container state、tool protocol、trajectory 与 verifier 的联合分布；缺少任一项，
“成功样本”都可能只是 harness artifact。数据控制面应保存：

```text
repository / container / dependency snapshot
+ task and hidden verifier identity
+ scaffold / tool schema / policy checkpoint
+ complete success or failure trajectory
+ final artifact and executable outcome
```

失败轨迹可以暴露 recovery signal，却不能因“更难”就天然优于成功轨迹：environment build failure、test
incompleteness 和 agent bug 会混入同一 failure label。诊断结果可以驱动下一轮 source/task/environment quota，
但 diagnostic model 与当前 policy 的 blind spot 也会使 curriculum 追逐噪声。因此闭环应是
`failure attribution → bounded mixture proposal → regenerated executable rows → independent validation`，并保留
固定人工/历史数据作为分布锚。Terminal-capability data engineering、SWE-rebench V2 与 DPE 分别为数据对象、
environment diagnostics 和 diagnostic-driven mixture 提供了实验性证据；它们没有证明某个数据量或失败比例是通用配方。

Repository 与 GUI 任务还要求 specification 保留跨步 state。只把单个函数、截图或最终 patch 当作样本，会丢掉依赖图、工具返回值、文件版本和 action side effect。更完整的数据对象应是：

```text
initial executable state + dependency graph
→ instruction / issue intent
→ stateful tool trajectory
→ intermediate observations and failures
→ final artifact + outcome verifier
```

当规模扩到真实 pull requests，environment 本身需要像 dataset row 一样构建和验收。单一“tests pass”容易接受
原本就通过、与 issue 无关或 hard-code oracle 的样本；更强的最小合法性合同是同一 immutable image 上执行：

```text
repository base + dependency image + issue intent
-> apply test-only patch: expected fail
-> apply complete fix: expected pass
-> inspect shortcut / unrelated regression
-> retain image, scripts, logs and verdict as one source family
```

Builder 可以将 Dockerfile、evaluator 与 task diagnosis 分成可重试阶段，并用 loose data parallelism 扩大吞吐；
但 image cache invalidation、shared queue/filesystem、zombie cleanup 和 dependency/network drift 都成为数据控制面。
daVinci-Env / OpenSWE 的受限系统证据支持 fail-before/pass-after 比单一终局 exit code 更能筛掉无效环境，不证明
synthesized tests 等同真实 requirement，也不能把大规模构建数字外推为通用成本。人工维护的小型 canonical
environment 在高风险与长期回归中仍更可信；自动构建只有在 base commit、image、test/fix patch、script、log
和 validator revision 可联合重放时才形成训练数据，而不是下载缓存。

真实 PR/commit 历史保留了开发者意图与自然 failure distribution，合成 emulator 则能控制覆盖、故障注入和可重放性。前者可能带 contamination、许可和未显式记录的环境依赖；后者可能共享不完整 ontology。两者应互相校验，而不是把“可执行合成”或“真实历史”当成单一真值来源。

### 可验证数据也要保持 Policy-relative Sweet Spot

静态 verifier 解决“答案能否判定”，不保证样本对当前 policy 仍有训练信号。题目过易时同组 reward 全相同，
过难时也没有正样本；让 generator 只追求更难，会越过 learnability boundary。更稳健的数据控制回路是：

```text
source / executable specification
→ synthesize candidate task
→ sample current-policy rollouts
→ estimate correctness and group reward variance
→ retain, revise or retire by target difficulty zone
→ version task with generator / verifier / policy identity
```

开放文本还可以被重构为局部可验证的 reconstruction/discrimination task，但它验证的是“恢复来源片段或选项”，
不是原开放问题的现实正确性。这个分支扩大可验证数据供应，却新增 synthesizer bias、shortcut、许可、
decontamination 和 policy drift。固定人工题库在长期可比性优先时仍合理，procedural environment 在真实语义可
执行时更强；policy-relative filtering 只是在两者之上维护有效学习区间，不是无限制造可靠 ground truth。

### 从样本数量到 Coverage Contract：Curriculum 必须同时管理内容、能力与环境

只按文本相似度追求 diversity，会漏掉“表述不同但都只训练同一种能力”；只按当前 policy 的正确率调难度，
又可能反复采样同一类 feature。更完整的数据控制面至少区分三种 coverage：

```text
source / semantic coverage
+ representation or feature-space coverage
+ executable dependency / environment coverage
→ current-policy difficulty and failure attribution
→ task synthesis or composition
→ independent verifier / rubric execution
→ accepted training row with complete lineage
```

Feature-space coverage 可以寻找已有数据尚未激活的表示方向，dependency graph 可以定位多步工具链中反复失败的
节点，composed prompts 可以把多个可验证约束组合成更难任务。它们解决的是不同缺口，不能压成一个“多样性分数”。
尤其是 generator、rubric creator、verifier 与 evaluator 若共享同一模型或 ontology，会把共同 blind spot 同时写进
数据与 reward。Rubric formation、criterion execution 和 final-answer correctness 应保留独立身份；feature extractor、
policy checkpoint、environment、tool schema、composition recipe 与 verifier version 也必须进入 lineage。

这条路线把静态 dataset 推进为可反馈的 curriculum，却新增 distribution chasing、proxy coverage、任务不可满足、
reward leakage 与环境模拟偏差。固定人工数据在需要长期可比、语义开放或现实副作用不可重放时仍是合理基线；闭环
合成只在 coverage signal 可解释、task 可执行、verifier 相对独立且 held-out distribution 未被同一控制器消费时成立。

### 从 Trajectory Count 到 Primitive × Transition Coverage

机器人数据若只按 trajectory 数量计费，会把大量重复直线段和少量关键接触转移视为等价。更有诊断力的预算单位
是可复用 primitive 的组合以及 primitive 之间的 transition interface：先估计结构桶的覆盖和边际收益，再从每个桶
选择稳定代表，而不是让高频轨迹自然占满预算。

```text
trajectory stream
→ primitive and transition discovery
→ coverage bucket + diminishing-return estimate
→ representative / medoid selection
→ policy training and closed-loop tail audit
```

这会新增 encoder、clustering 与版本 identity；medoid 偏好中心样本，可能把罕见但安全关键的 failure tail 当成
outlier 删除。发现的 cluster 也不等于真实 Skill。结构估计不稳定、接触尾部重要或数据量仍可承受时，保留全量
数据仍优于激进子采样。

### 从 Physical Teleoperation 到带 Provenance 的 Digital Teleoperation Data

真实 teleoperation 提供最直接的 robot-action evidence，却被操作员时间、硬件占用和 embodiment 绑定限制。一个扩展
分支是用 human hand pose 驱动 action-conditioned video world model，再把 pose stream retarget 到目标 robot schema，
把生成的 egocentric sequence 与 action label 作为派生轨迹：

```text
human hand pose + scene observation
→ action-conditioned generated video
→ pose/depth reconstruction and retargeting
→ derived robot trajectory with provenance
→ mixed-data training
→ real closed-loop admission
```

它没有消除 sim-to-real，而是把 gap 移到生成 fidelity、pose/depth reconstruction、retargeting 与 per-embodiment
adaptation。派生 row 必须绑定生成模型、revision、输入来源、robot schema 与 verifier；现实接触、calibration 和
安全尾部仍需真实 teleoperation。作者设置中的 policy gain 或 synthetic-only feasibility 不能证明生成视频是物理真值。

## 去重为什么改变梯度而不只是节省磁盘

Exact dedup 可以删除完全相同的 documents；near dedup 则要识别局部修改、模板替换或大段重叠。粒度可以是 document、paragraph、sequence 或 substring。

去重带来三类作用：

1. 减少重复样本对梯度的过度权重。
2. 在固定 token budget 下释放位置给更多独立内容。
3. 降低模型逐字记忆与 benchmark overlap 风险。

但去重不是“越强越好”。法律条文、代码模板、引用和常用表达天然重复；激进去重可能删除有效频率信号，或对短文本产生过高误判。

还必须明确去重集合：只在单个 shard 内去重，会漏掉跨 shard 重复；只在训练集内部去重，也不能发现训练与 Evaluation 之间的 contamination。

## Contamination 为什么破坏评估因果

若 benchmark 问题、答案或高度相似变体出现在训练数据中，模型得分无法清楚区分泛化与记忆。污染检查至少要区分：

```text
exact match
substring / n-gram overlap
near duplicate
semantic or transformed overlap
```

匹配越宽，召回越高，误报也越多。没有单一 detector 能证明数据绝对无污染。

更稳健的系统做法是：

- 在训练前冻结 Evaluation 集和 contamination policy。
- 保存匹配算法、阈值与删除记录。
- 对 benchmark 发布时间与数据抓取时间做 provenance 检查。
- 对高风险评估同时报告 contaminated/clean slices。
- 不把一次扫描结果写成永久“无污染”证明。

污染治理属于 Evaluation correctness，而不只是数据清洁度。

## Tokenizer、切分与 Packing 的边界

第 11 章已经解释 Tokenizer 的模型接口。本章关心的是固定 tokenizer 下，数据怎样形成训练 sequences：

```text
documents
-> tokenize
-> token stream
-> truncate / split / pack
-> input_ids [B,T]
-> labels [B,T]
```

将多个短 documents pack 到同一长度 `T`，可以减少 padding 并提高有效 token ratio。但系统必须明确 document boundary、EOS、position ids、Attention mask 和 loss mask。错误 packing 可能让本不相关文档互相读取，或让 label 跨边界预测。

截断也不是无害操作。总在文档尾部截断，会系统性减少结论、答案或长程结构；只保留短样本则会让模型缺少长上下文训练分布。

## Data lineage 是训练可复现性的前提

### 元数据生成也必须是可治理的数据变换

人工维护 schema、统计特征和语义标签在小型、稳定数据集上清晰可靠；数据源和版本增多后，手工登记容易落后于真实 artifact。可以把 schema inference、profiling、semantic annotation 和 Croissant/JSON-LD 等标准化描述组织为一条可重放 pipeline，但它的输出仍是派生 metadata，不是来源事实本身：

```text
source snapshot + parser revision
→ schema inference and profiling
→ semantic annotation
→ typed metadata artifact
→ validation and manual override
```

自动化减少登记成本并改善跨工具发现，却会放大推断错误、敏感字段暴露和模型版本漂移。每次产物应绑定 source snapshot、工具与规则版本、置信边界及人工修订历史；高风险 license、PII 与 label 语义仍需独立检查。数据规模小或 schema 变化极少时，受控 manifest 仍是更简单的基线。

<!-- source-family:SF-2026-ARXIV-2605-15079 -->

### Data Attribution 本身也需要对抗性 Provenance Contract

把 attribution value 当作参与者贡献的被动统计，在参与方诚实且训练集中式时便于定价与审计；分布式学习允许参与者改变本地更新，使全局 utility 几乎不变却抬高自身 credit。因而 attribution pipeline 要记录本地数据/更新身份、计算方法和最终 utility，并以 adversarial audit 检查“credit 增长是否对应可复现贡献”：

```text
participant data and update lineage
→ attribution computation
→ claimed contribution
→ matched global-utility and attack audit
→ accept | quarantine | recompute
```

更强审计增加重算、隐私暴露和机制博弈成本，也无法从相关 attribution 单独证明因果贡献。参与方可信、规模小或 attribution 不触发支付/治理时，简单统计仍可使用；一旦 credit 会改变资源或权益，原始 lineage 与独立 utility evidence 必须保留，不能让参与者同时拥有更新和最终归因权。

<!-- source-family:SF-2026-ARXIV-2605-15520 -->

<!-- daily-20260621:train-data:start -->
### 从 sample provenance 到训练生命周期 lineage

RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。

**Trade-off、failure、共存与回退。** robot workflow 与作者工具不能证明跨 embodiment/stack 互操作；lineage 完整不保证 reviewer 判断或 deployment recommendation 正确。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-22142` — primary `arXiv:2606.22142v1`；exact-v1 URL=`https://arxiv.org/html/2606.22142v1`；Method=`https://arxiv.org/html/2606.22142v1 — §3 Method; §3.2 Agent-Native Governance Over Lifecycle Artifacts; §3.5 Data Health, Training Integration, and Version Governance`；Evaluation=`https://arxiv.org/html/2606.22142v1 — §4 Experiments; §4.1 Experimental Setup`；Non-proof=`https://arxiv.org/html/2606.22142v1 — §5 Limitations and Discussion`。
<!-- daily-20260621:train-data:end -->

### 从 Sample Dedup 到 Typed Lineage Graph

样本级 hash 只能回答“这段内容是否重复”，无法回答一个 evaluation item 是否由训练文档、合成 prompt、
teacher output、过滤器或后续 mixture 间接派生。更完整的 lineage graph 把 dataset artifact、sample、source、
transformation、generator/judge、split 与 release 表达为 typed nodes/edges：

```text
source artifact
→ extraction / transform / synthesis
→ sample identity
→ split / mixture / checkpoint consumption
→ evaluation overlap or deletion impact
```

它让 contamination、license、deletion 和 reproducibility 可以沿 dependency 传播，也新增 graph completeness、
edge authenticity、storage/cardinality 与敏感 source disclosure 问题。小型人工数据或单阶段 pipeline 仍可用
manifest + content hash；typed graph 只在跨版本、多 derivation 和治理查询中值得。Tracing the Roots 的作者方法
提供 Experimental lineage evidence，不证明自动抽取的所有边都真实完整。

一个 dataset version 不能只由 bucket path 表示。至少需要记录：

- Source snapshot、抓取时间、许可与 provenance。
- 解析、normalization、过滤和去重代码版本。
- Tokenizer 与 vocabulary version。
- Domain mixture、sampling weights 和 random seed。
- Shard manifest、样本/token count 与 checksums。
- Evaluation exclusion 和 contamination policy。
- 删除、纠错与合规变更历史。

训练读取的应是不可变 manifest，而不是会被原地覆盖的目录。否则同一个 experiment config 在不同日期可能读到不同数据，却仍产生相同的“dataset name”。

Lineage 还连接到 checkpoint：只有知道某个 checkpoint 看过哪些 data versions、到哪个 data cursor，才能解释能力变化、恢复训练或执行删除影响分析。

### 从 Shard 可见到 Batch 原子发布

不可变 manifest 解决了“训练读的是哪一版数据”，却不自动解决对象存储中 producer 与 consumer 并发时的
可见性边界。最简单的旧路径是让 worker 各自写 shard，trainer 看到对象就读取；在单 producer、写入完成后再
启动训练时，这种方式足够直接。在线预处理、跨 worker packing 与持续训练并存后，单个对象存在不再意味着一个
global batch 已完整、顺序一致且可以安全回收。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09994:start -->
更严格的数据平面把 global batch 作为原子 commit unit：producer 先写带 checksum、sample range 与 batch epoch
的对象，再发布 batch manifest；consumer 只推进到已提交 manifest，并以独立 consumption cursor 确认使用完成；
GC 只有在 producer publication 与全部必要 consumer acknowledgment 都满足后才能删除。状态所有权由此分成
`object bytes → producer`、`batch visibility → manifest owner`、`consumption progress → trainer`、`reclamation → GC policy`。

这条路径避免 partial batch、重复消费和过早回收，却引入 manifest 协调、元数据读放大、迟到 worker 与 orphan
object 清理。对象存储的一致性语义、batch size、worker 数或 recovery policy 改变后必须重新验证；离线静态
dataset、单 consumer 或可以整体重跑的小任务仍可使用 shard manifest + checkpoint cursor。现有实验只支持其
公开的对象存储与 64-GPU workload，不证明任意数据湖、训练框架或生产 tail 下都有相同收益。
[受限证据：arXiv:2605.09994v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09994:end -->

### AI for Science：实验记录不是普通文档语料

科学数据除了来源和许可，还需要 protocol、instrument、unit、calibration、sample/batch、环境条件、negative result 与人工修订。论文正文中的结论、补充材料中的测量、实验室原始读数和模型生成的 hypothesis 不是同一 Evidence Level；若在解析时压成无类型文本，模型会把推测、观察与结论混为同一 truth source。

```text
physical sample / simulation state
-> instrument and protocol revision
-> raw measurement
-> calibrated / derived artifact
-> human interpretation or model-generated hypothesis
-> training example and loss-bearing region
```

`TRAIN-DATA` 只拥有 acquisition、schema、provenance 与 mixture；第66章判断 derived artifact 能支持什么 claim，第81章组织实验/仿真 Workflow，第72章限制危险材料、隐私数据和现实执行权限。AI for Science 因而是跨 owner 的领域组合，不需要独立 Part。

### Unlearning 要对齐 Counterfactual Optimizer State

删除数据后只修正当前参数，适合无状态或近似一阶更新；带 momentum、Adam moments 或 L-BFGS memory 的 optimizer 还保存“如果从未看过该数据，本应不存在”的历史方向。完整删除合同应比较 counterfactual parameter、optimizer memory 与下一步 update，而不是只测当前输出忘记率。

重建这些状态可能接近重训成本，近似修正又会留下残余。高影响删除应保留训练 lineage、optimizer revision 和 matched retrain audit；无法证明等价时标记近似 unlearning，不把一次行为测试升级为完全擦除。

<!-- source-family:SF-2026-ARXIV-2605-17590 -->

### Reasoning-trace Bypass 先排除 Parser 与 Prefill 差异

同一被删除知识在普通问答拒绝、加入 reasoning trace 后又出现，不必然说明 weights 保留了知识；format/parser、system prefix、prefill 长度、seed 与 decoding 也可能改变 elicitation。Unlearning evaluation 必须冻结这些身份，并用 matched intervention 逐项隔离。

该协议提高因果解释，却增加实验矩阵与重复运行。若只观察单一 prompt gap，应报告 bypass evidence 而非 weight-level memory；只有在输入路径对齐后仍稳定恢复，才支持更强残留结论。

<!-- source-family:SF-2026-ARXIV-2605-18891 -->

## Streaming 与随机性

大规模数据常无法先完全 shuffle 到单机文件。系统会在 shards、workers 和局部 buffer 上执行多级随机化。

这里要区分：

```text
statistical shuffle quality
deterministic replay
distributed worker partition
```

Shuffle buffer 太小可能产生 source clustering；不同 worker 重复读取会改变样本权重；故障恢复若只恢复 optimizer step 而不恢复 data cursor，可能重复或跳过数据。

所以 data loader 不是训练外围组件。它参与定义实际 `q(x)`，并与第 35 章 Checkpoint 的可恢复状态直接相连。

### 时间顺序也是 Data / Objective Identity

随机 shuffle 在样本近似平稳、目标不依赖事件顺序时能改善优化混合；事实随时间演化时，它会把旧状态和新状态当作可交换证据。Temporal corpus 应保存 snapshot time、ordering policy、dedup revision 与重复率，并明确训练是在学习“某时点事实”还是“变化规律”。Data pipeline 拥有顺序与版本，trainer 不能在 run 内静默重排后仍复用同一数据身份。

按时间组织能改善事实绑定和时序评估，却削弱 i.i.d. 假设、降低混合随机性并可能放大短期偏差；非时间任务或数据稀疏时，shuffle 仍是更稳健的基线。arXiv:2605.22769v1 的实验只支持其 corpus、ordering 与评估协议，不证明所有预训练任务都应采用时间顺序。

<!-- source-family:SF-2026-ARXIV-2605-22769 -->

## 数据质量不能只看 validation loss

### Synthetic Trajectory Weight 可以由真实任务外层目标拥有

先生成再由外部 judge 二值过滤实现简单，却把 judge 偏差直接写进数据。bilevel 选择让下层模型在加权 synthetic multi-turn trajectories 上训练，上层 reweighting head 依据 held-out real trajectories 的损失连续调整每条权重。收益是数据选择与真实目标对齐，代价是双层优化昂贵、held-out 集可能被反复适配，且权重难解释；可靠 judge 或低数据量时，离散过滤仍更稳健。该证据只表明特定任务上的连续重加权有效，不证明它消除了 synthetic bias。

<!-- source-family:SF-2026-ARXIV-2605-24743 -->

Validation loss 能回答 held-out distribution 上的平均预测质量，却可能掩盖：

- 某些语言或领域退化。
- Memorization、PII 与版权风险。
- Benchmark contamination。
- Toxicity、安全与偏见。
- 长上下文、代码执行或事实时效性问题。

数据实验应把 model outcome 与 pipeline changes 连接起来。至少同时记录 token-level loss、能力切片、memorization/privacy tests、数据覆盖和训练效率。

DataComp-LM 一类 controlled data benchmark 的价值也在这里：保持模型与计算预算相对可比，才能把质量差异更可信地归因到数据策略，而不是隐藏在规模变化中。

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-FOLD-ONLINE-DEDUP:start -->
在线去重从反复扫描 LSH bucket 演进为持续维护的 HNSW：数据面把文档映射为适配 Jaccard 的 bitmap signature，索引 owner 负责增量插入与候选搜索，SIMD 和 cached popcount 只优化执行。它用额外索引状态换在线吞吐；证据只覆盖给定语料、signature 和 reference-label 设置，不能证明跨语言、任意相似度或最终训练质量。
<!-- semantic-body-binding:SF-FOLD-ONLINE-DEDUP:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-13873:start -->
source-level unlearning若是硬需求，应在训练时把shared backbone与source-addressable sparse sinks分离，并把disable-sink作为部署revoke动作。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-13873:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16110:start -->
machine-unlearning 验收需要无需 scratch retrain/shadow fleet 的 proof-of-ignorance audit，并显式保存攻击面与误判边界。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16110:end -->

### Post-training Data Selection 是当前 Policy 的在线控制环

静态 difficulty sampling 在 policy 固定时可重放且易审计；RL 过程中模型能力移动后，长期保留已学会或完全不可学的样本会浪费 rollout。在线 selector 可以依据当前 policy 的 reward/gradient frontier 估计 active learning zone，再决定采样、降权或延后。

Selector 只拥有数据 admission，不拥有 objective；它用更高数据效率换 policy-dependent feedback、分布收缩和额外观测成本。frontier 估计不稳或需要严格复现实验时，回退冻结 mixture，并保留所有采样概率与 policy revision。

<!-- source-family:SF-2026-ARXIV-2605-17003 -->

### pass@1 提升可能掩盖 Solution Coverage 收缩

只优化最可能成功路径会提高 pass@1，却可能把 base model 的多个有效 reasoning forks 压缩成单一路线，使 pass@k 或分布外恢复能力下降。数据构建应显式保存 decision points 与替代分支，训练和评估同时报告单次成功与多样覆盖：

```text
problem + verified solution forks
→ decision-point-aware synthesis
→ training mixture
→ pass@1 + pass@k + diversity/validity slices
```

鼓励多样性会增加生成、验证和训练成本，也可能保留低质量噪声；不存在多解需求或部署只允许确定输出时，聚焦最优路径仍合理。作者观察只属于其 reasoning task 与 decoding，不证明所有 post-training 都会收缩覆盖。

<!-- source-family:SF-2026-ARXIV-2605-17026 -->

### 数据阶段切换也会改变最优 Batch 控制

沿用稳定训练阶段的大 batch 穿过 quality transition，在分布平稳时可以维持吞吐；新数据阶段刚切换时，梯度信号与噪声结构同时改变，固定 batch 会稀释短暂但有用的方向。Data/optimizer control owner 可以在切换点先降 batch、低位积累信号，再逐步 ramp up 抑制噪声。收益是把 phase transition 变成显式控制状态，代价是吞吐波动和额外调参；切换检测错误、数据异质性或 ramp 过快都会放大不稳定。没有可信 transition signal 时，固定 batch 或保守 warmup 仍更合适。exact-v1 只支持论文的理论结构与所测 midtraining 配置，不证明该 schedule 对所有模型规模与集群都优。<!-- source-family:SF-2026-ARXIV-2605-25698 -->

## 本章在知识树中的位置

```text
Raw sources
-> provenance / policy
-> parsing / filtering / dedup / decontamination
-> domain mixture q(x)
-> tokenize / pack / shard / sample
-> Pretraining loss
-> Checkpoint capability
-> Evaluation and feedback
```

本章定义能力生产链的输入分布。第 28 章解释 next-token objective 怎样消费这些 tokens；第 35 章负责保存 data cursor 与 dataset identity；第 66 章再把 evaluation dataset、contamination evidence、slice 与 deployment population 组织成评估契约。

## 从机制演进到系统设计

训练数据从静态语料集合演进成有版本的生产系统：采集和过滤决定候选分布，去重与 repeat policy 决定 compute 是否反复消费同一信号，mixture/controller 决定不同 domain 在训练阶段获得多少预算，synthetic-data pipeline 则把 generator、validator 与 lineage 引入数据面。

新的控制能力改善覆盖和成本，却会引入 controller reward 偏差、合成错误放大、semantic near-duplicate 漏检和 provenance 断裂。数据 owner 因而必须保存 source、transform、sample、split、mixture、checkpoint consumption 与删除证据；行为或 feature attribution只能提供复核线索，不能替代删除/重训对照。固定 mixture、人工抽样和保留原样本仍是 drift 或归因不可靠时的 fallback。

## 自检问题

1. 为什么训练数据应被视为行为 specification，而不是被动原料？
2. Domain mixture 中 `alpha_k` 怎样影响梯度频率？
3. Documents 占比与 tokens 占比为什么可能不同？
4. Quality filter 为什么会产生新的选择偏差？
5. 为什么 collection protocol 本身也是训练分布 specification？
6. 为什么顶层 dataset license 不能替代 partition-level policy？
7. `80/10/10` 为什么不能单独证明 evaluation split 无泄漏？
8. Data tag 为什么可能同时训练一条 compute 或 mode policy？
9. 为什么 constraint-derived verifier 仍可能与 generator 共享 blind spot？
10. 去重为什么会改变经验风险，而不只是节省存储？
11. Training dedup 与 benchmark decontamination 有什么不同？
12. Packing 需要同时维护哪些边界和 masks？
13. 为什么 dataset name 不足以支持可复现训练？
14. Data cursor 为什么属于 checkpoint 状态？
15. Validation loss 为什么不能单独证明数据更好？
16. Failure-driven synthetic curriculum 为什么必须区分 baseline blind spot、harness failure 与真实任务难度？

## 小结

数据 pipeline 通过过滤、去重、配比和采样构造训练分布 `q(x)`。模型优化的不是抽象的“互联网知识”，而是这条 pipeline 实际提供、按特定频率出现的 token sequences。

更可靠的数据系统必须同时管理采集协议、质量、覆盖、partition ownership、许可与 consent、重复、污染、
provenance、合规和可复现性。数据决定能力生产的上游边界，也决定后续任何 loss 下降究竟代表什么。

## Review notes

- SIEVE（primitive × transition coverage 与代表性子集；Status: Experimental）:
  https://arxiv.org/abs/2607.06442v1
- RynnWorld-Teleop（digital teleoperation derived data；Status: Experimental）:
  https://arxiv.org/abs/2607.06558v1

- Tracing the Roots（typed training-data lineage；Status: Experimental）: https://arxiv.org/abs/2604.10480

本章将数据定位为经验风险的分布 specification，并建立 Data、Tokenizer、Pretraining、Checkpoint 与 Evaluation 的接口。WAXAL 的多方语音数据 release 作为受限案例补足了 acquisition protocol、partition-level policy 与 split identity：其论文、发布页和 dataset card 的规模与许可口径并不完全一致，支持“consumer 必须锁定实际 artifact contract”，不支持任何模型性能结论。CoVe 作为实验性案例补足 constraint-derived synthetic data 与 verifier lineage；其确定性只对已编码 ontology 成立。Phi-4-reasoning-vision-15B 的技术报告则支持 data tag、visual-token transformation 与 learned compute policy 的连接，但不支持把作者配比或 benchmark 写成通用配方。具体 next-token loss 留给第 28 章；SFT demonstration 与 preference data 分别留给第 29、31 章；AI for Science 的数据入口由本章交给第66章 Evidence、第81章 Workflow 与第72章 Security；平台级数据权限和治理留给 Part VI。

Primary-source 校验入口：

- Colin Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", 2019: https://arxiv.org/abs/1910.10683
- Katherine Lee et al., "Deduplicating Training Data Makes Language Models Better", 2021: https://arxiv.org/abs/2107.06499
- Jeffrey Li et al., "DataComp-LM: In Search of the Next Generation of Training Sets for Language Models", 2024: https://arxiv.org/abs/2406.11794
- Luca Soldaini et al., "Dolma: an Open Corpus of Three Trillion Tokens for Language Model Pretraining Research", 2024: https://arxiv.org/abs/2402.00159
- Zekun Deng et al., "Investigating Data Contamination for Pre-training Language Models", 2024: https://arxiv.org/abs/2401.06059
- Abdoulaye Diack et al., "WAXAL: A Large-Scale Multilingual African Language Speech Corpus", arXiv v3, 2026: https://arxiv.org/abs/2602.02734
- Google Research WAXAL dataset card v2.0.0（artifact/schema/split/license contract）: https://huggingface.co/datasets/google/WaxalNLP
- Jinpeng Chen et al., "CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification"（Status: Experimental）, 2026: https://arxiv.org/abs/2603.01940
- Jyoti Aneja et al., "Phi-4-reasoning-vision-15B Technical Report"（Status: Experimental）, 2026: https://arxiv.org/abs/2603.03975
- HardGen（Status: Experimental；failure-driven tool-use curriculum 与 executable verification）:
  https://arxiv.org/abs/2601.01498
- Golden Goose（开放文本到局部可验证任务；作者实验边界）: https://arxiv.org/abs/2601.22975
- Sweet Spot Learning（policy-relative difficulty zone；Status: Experimental）:
  https://arxiv.org/abs/2601.22491
- daVinci-Dev（repository-native development trajectories；Status: Experimental）: https://arxiv.org/abs/2601.18418
- ASTRA（stateful tool dependency graph 与 executable emulator；Status: Experimental）: https://arxiv.org/abs/2601.21558
- SERA（soft verification 不能替代 semantic correctness；Status: Experimental）: https://arxiv.org/abs/2601.20789
- Dr. SCI（data difficulty、rubric 与 current-policy feedback；Status: Experimental）: https://arxiv.org/abs/2602.08321
- DataChef（可执行 data recipe 与 reward；Status: Experimental）: https://arxiv.org/abs/2602.11089
- Composition-RL（verifiable constraint composition；Status: Experimental）: https://arxiv.org/abs/2602.12036
- Dreaming in Code（executable curriculum loop；Status: Experimental）: https://arxiv.org/abs/2602.08194
- DataFlex（Status: Experimental；Select/Mix/Weight data control plane）: https://arxiv.org/abs/2603.26164
- daVinci-LLM（Status: Experimental；stage-aware data operators 与 trajectory identity）:
  https://arxiv.org/abs/2603.27164
- MolmoWeb（Status: Experimental；privileged-teacher 到 visual-policy 的 trajectory lineage）:
  https://arxiv.org/abs/2604.08516
- REDSearcher（search task、environment 与 trajectory curriculum；Status: Experimental）: https://arxiv.org/abs/2602.14234
- Less is Enough / FAC Synthesis（feature-space coverage；Status: Experimental）: https://arxiv.org/abs/2602.10388
- Data Engineering for Scaling LLM Terminal Capabilities（task/environment/verifier row contract；
  Status: Experimental）: https://arxiv.org/abs/2602.21193
- SWE-rebench V2（executable-environment diagnostics；Status: Experimental）:
  https://arxiv.org/abs/2602.23866
- DPE（diagnostic-driven data-mixture feedback；Status: Experimental）:
  https://arxiv.org/abs/2602.22859
- OpenResearcher（evidence-grounded deep-research trajectory；Status: Experimental）:
  https://arxiv.org/abs/2603.20278
- HopChain（dependency-constrained visual evidence chain；Status: Experimental）:
  https://arxiv.org/abs/2603.17024
- Environment-free Synthetic Data Generation for API-Calling Agents（synthetic API transition lineage；Status: Experimental；simulator response 不是环境事实）:
  https://arxiv.org/abs/2607.16900v1

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28772 — primary arXiv:2606.28772v1; exact-v1 URL=https://arxiv.org/html/2606.28772v1; Method=https://arxiv.org/html/2606.28772v1 — §3 Methods; Evaluation=https://arxiv.org/html/2606.28772v1 — §3.3 Statistical Analysis; 4 Results; Non-proof=https://arxiv.org/html/2606.28772v1 — §Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain; 4.1 Disagreement Concentrates at the Value Boundary; 4.5 Boundary Disagreement Is Not Driven by Annotation Error；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22883` — primary `arXiv:2606.22883v1`; Method=`arXiv:2606.22883v1 — §3 Method; §3.2 Task Blueprint Construction; §3.4 Test Construction and Executable Filtering`; Evaluation=`arXiv:2606.22883v1 — §4.3 Scaling Analysis; §4.4.1 Cross-benchmark transfer; §4.5 Error Study`; non-proof=`arXiv:2606.22883v1 — §5 Conclusion; §Appendix C Failure Mode Examples`; fallback=该 family 的 failure pressure 是：While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck. 披露的 evaluation signal 是：Remarkably, fine-tuning Qwen3-32B on CLI-Universe-6K achieves 33.4% on Terminal-Bench 2.0. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-28386` — primary `arXiv:2606.28386v1`; Method=`arXiv:2606.28386v1 — §3 Method; §3.3 A Framework for Data Provenance in IARs; §3.3.1 QuantLoss`; Evaluation=`arXiv:2606.28386v1 — §4 Empirical Evaluation; §4.1 Experimental Setup; §4.2–§4.4 Results and Ablations`; non-proof=`arXiv:2606.28386v1 — §R Adaptive Attack; §W Comparison with Membership Inference Baselines; §5 Conclusions`; fallback=该 family 的 failure pressure 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 披露的 evaluation signal 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-24133: `arXiv:2606.24133v1`; exact-v1 URL=`https://arxiv.org/html/2606.24133v1`; Method=`https://arxiv.org/html/2606.24133v1 — §2 Methodology: The Holistic Data Scheduler; 2.2 Online Data Mixing`; Evaluation=`https://arxiv.org/html/2606.24133v1 — §3 Experiments and Analysis; 3.1 Experimental Setup`; Non-proof=`The Pile、给定 16-layer/2048-dim recipe 与 reward sensitivity 不证明跨 tokenizer、optimizer、数据污染或超大规模 pretraining 仍有相同收益。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`
- SF-2026-ARXIV-2606-24998: `arXiv:2606.24998v1`; exact-v1 URL=`https://arxiv.org/html/2606.24998v1`; Method=`https://arxiv.org/html/2606.24998v1 — §3 Methods; Repeated-pool construction`; Evaluation=`https://arxiv.org/html/2606.24998v1 — §4 Results; F Training and Evaluation Details`; Non-proof=`结论绑定 synthetic repeated pools、模型尺度与 loss-floor fit；自然语料的语义近重复、curriculum 与 downstream contamination 未证明，不能由单一 repeat threshold 自动删除。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25388**：Primary `arXiv:2606.25388v1`；Method `https://arxiv.org/html/2606.25388v1 — §III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control`；Evaluation `https://arxiv.org/html/2606.25388v1 — §V Experimental Evaluation; V-A Experimental Setup`；未证明边界 `https://arxiv.org/html/2606.25388v1 — §VII Discussion and Future Work`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25871**：Primary `arXiv:2606.25871v1`；Method `https://arxiv.org/html/2606.25871v1 — §3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic`；Evaluation `https://arxiv.org/html/2606.25871v1 — §4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance`；未证明边界 `https://arxiv.org/html/2606.25871v1 — §5 Production Deployment and Discussion; sponsored-search relevance boundary`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-25996**：Primary `arXiv:2606.25996v1`；Method `https://arxiv.org/html/2606.25996v1 — §2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist`；Evaluation `https://arxiv.org/html/2606.25996v1 — §3 Experiments; CS, legal, and scientific reasoning tasks`；未证明边界 `https://arxiv.org/html/2606.25996v1 — §6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

#### 2026-06-29 source-specific Review notes

Review note：`SF-2026-ARXIV-2606-29171`；Method `https://arxiv.org/html/2606.29171v1 — §3 Symbolic Mechanistic Data Attribution Framework; 3.2 Symbolic Policy Model; 3.3 Influence Computation`；Evaluation `https://arxiv.org/html/2606.29171v1 — §4 Experimental Setup; 5 Results`；未证明边界 `https://arxiv.org/html/2606.29171v1 — §6 Discussion; Symbolic model fidelity and scope; First-order approximation`。

### Source-family integration record

<!-- daily-20260628:TRAIN-DATA:start -->
### Owner-merged minimal durable delta

标注聚合不能静默删除价值分歧。Data owner 应保存 per-annotator label、annotator/threshold identity、disagreement 与 aggregation revision；majority 或 soft label 只是可重建的 materialized view。训练可消费聚合结果，但 evaluation 与 policy review 必须能恢复 contested boundary。

### Trade-off、failure、fallback 与 coexistence

三位 annotator 和单一 HateXplain/BERT slice 不能区分稳定价值阈值与标注噪声；高分歧时保留多视图或转人工，不把 minority label 自动升级为真值。

<!-- daily-20260628:TRAIN-DATA:end -->

<!-- recovered-daily-20260623:TRAIN-DATA:start -->
### 2026-06-23 evidence integration — TRAIN-DATA

相邻章 `books/part-04-training-system/28-pretraining.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-22883**：CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents 的 exact-v1 机制为：To overcome this, we introduce CLI-Universe, a principled synthesis engine that constructs terminal-agent tasks. 因此 把任务/样本生成、可执行验证、过滤与训练 lineage 绑定。 该 family 的 failure pressure 是：While recent LLM-based terminal agents have demonstrated promising capabilities, the scarcity of high-quality, executable training data remains a critical bottleneck. 披露的 evaluation signal 是：Remarkably, fine-tuning Qwen3-32B on CLI-Universe-6K achieves 33.4% on Terminal-Bench 2.0. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-28386**：Data Provenance for Image Auto-Regressive Generation 的 exact-v1 机制为：Leveraging this, we present a post-hoc framework that enables the robust detection of such patterns for provenance tracing. 因此 把任务/样本生成、可执行验证、过滤与训练 lineage 绑定。 该 family 的 failure pressure 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 披露的 evaluation signal 是：Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:TRAIN-DATA:end -->

<!-- recovered-daily-20260624:TRAIN-DATA:start -->
### 2026-06-24 evidence integration — TRAIN-DATA

相邻章 `books/part-04-training-system/28-pretraining.md` 只接收 handoff，不重复拥有机制。

### Owner-merged minimal text

- **SF-2026-ARXIV-2606-24133**：把固定或单目标 data mixture 改为 SAC controller：state 汇聚 domain loss/lexical diversity/weight-norm，action 写回下一训练阶段的 domain weights，多目标 reward 决定调度。 The Pile、给定 16-layer/2048-dim recipe 与 reward sensitivity 不证明跨 tokenizer、optimizer、数据污染或超大规模 pretraining 仍有相同收益。
- **SF-2026-ARXIV-2606-24998**：数据去重从 hygiene 建议升级为 compute allocation contract：相同样本的 internal repetition 先改善后破坏 eval loss，data owner 应记录 repeat count、unique pool 与 model-size-dependent peak。 结论绑定 synthetic repeated pools、模型尺度与 loss-floor fit；自然语料的语义近重复、curriculum 与 downstream contamination 未证明，不能由单一 repeat threshold 自动删除。

<!-- recovered-daily-20260624:TRAIN-DATA:end -->

<!-- recovered-daily-20260625:TRAIN-DATA:start -->
### 2026-06-25 evidence integration — TRAIN-DATA

- **SF-2026-ARXIV-2606-25388**：`III System Overview; IV Methodology; IV-F Execution-Guided Validation and Control` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `VII Discussion and Future Work` 是 `TabClean: Reusable LLM-Synthesized Programs for Tabular Data Cleaning` 的 source-specific 反例/局限边界；若运行条件离开 `V Experimental Evaluation; V-A Experimental Setup` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25871**：`3 Our Approach; 3.1 System Architecture; 3.3 Per-Class Isotonic Calibration; 3.4 Cascade Decision Logic` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `5 Production Deployment and Discussion; sponsored-search relevance boundary` 是 `AutoRelAnnotator: Calibrated Model Cascades for Cost-Efficient Relevance Evaluation in Sponsored Search` 的 source-specific 反例/局限边界；若运行条件离开 `4 Experiments and Evaluation; 4.2 Dataset and Setup; 4.5 Cascade Performance` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。
- **SF-2026-ARXIV-2606-25996**：`2 Autodata; 2.1 Agentic Self-Instruct; 4 Meta Optimization of the Data Scientist` 所定义的源特定机制用于把数据选择、校准或验证结果变成训练前可审计的数据控制状态；旧路径仍作为未满足前置条件或质量退化时的 coexistence/fallback。 `6 Conclusion and Discussion; Hacking & limitations; A Token Efficiency and Truncation` 是 `Autodata: An agentic data scientist to create high quality synthetic data` 的 source-specific 反例/局限边界；若运行条件离开 `3 Experiments; CS, legal, and scientific reasoning tasks` 的验证域，`TRAIN-DATA` 必须保留旧路径并阻止该结果取得生产 commit，而不能把论文内结果外推为跨设置保证。

<!-- recovered-daily-20260625:TRAIN-DATA:end -->

<!-- june29-owner:TRAIN-DATA:start -->
### 2026-06-29 约束变化与机制增量

**Owner-merged 正文（覆盖 `SF-2026-ARXIV-2606-29171`）。** 现有 Data 正文拥有 lineage、dedup、contamination 与删除证据，却缺少从训练 pair 经 SAE feature 归因到 learned behavioral policy 的中间可审计层。 因此本次把这些增量合并到同一知识 owner：普通 sample lineage 只能回答数据来自哪里；symbolic mechanistic attribution 进一步把样本影响连接到可解释 behavioral policy，使数据 owner 能把选择、删除或复核请求落到行为证据链。归因仍是模型化证据，符号解释不稳定时保留原数据并回退重训/对照实验。 共同代价与回退边界是：只在 Llama-3.2-3B-Instruct refusal proxy、特定 SAE 与 200 个 SFT pair 上验证一阶符号归因；feature label、Ridge fidelity 与 first-order approximation 不等于真实删除/重训因果。保留原样本与重训对照。

<!-- june29-owner:TRAIN-DATA:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-FOLD-ONLINE-DEDUP:start -->
- `SF-FOLD-ONLINE-DEDUP` — Daily `2026-06-03`；primary `arXiv:2606.03001v1`；Books review `books-review:SF-FOLD-ONLINE-DEDUP`。

  **已吸收的语义增量：** FOLD replaces repeatedly rescanned LSH buckets with an incrementally maintained HNSW index over bitmap signatures aligned to Jaccard similarity, then implements the search path in a multithreaded FAISS C++/Python system with SIMD and cached-popcount optimizations. Boundary: The exact-v1 demonstrates an online deduplication design under the selected Jaccard-signature and HNSW assumptions; it does not establish recall or cost for arbitrary languages, similarity functions, distribution drift or a complete training-quality outcome.
<!-- daily-books-trace:SF-FOLD-ONLINE-DEDUP:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-11127:start -->
- `SF-2026-ARXIV-2606-11127` — Daily `2026-06-10`；primary `arXiv:2606.11127v1`；Books review `books-review:SF-2026-ARXIV-2606-11127`。

  **已吸收的语义增量：** 在训练数据章节补一段 provenance-preserving synthetic curation：faithfulness/reward 双 gate 与 diagnosed repair；不得把阈值或 judge 规模写成通用 release SLO。
<!-- daily-books-trace:SF-2026-ARXIV-2606-11127:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12385:start -->
- `SF-2026-ARXIV-2606-12385` — Daily `2026-06-11`；primary `arXiv:2606.12385v1`；Books review `books-review:SF-2026-ARXIV-2606-12385`。

  **已吸收的语义增量：** 模型卡不足以表达递归 training dependencies；provenance 应以 artifact identity 和 operation-centered edges 递归解析生成、过滤、judge 与 selection 关系。
<!-- daily-books-trace:SF-2026-ARXIV-2606-12385:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-12764:start -->
- `SF-2026-ARXIV-2606-12764` — Daily `2026-06-11`；primary `arXiv:2606.12764v1`；Books review `books-review:SF-2026-ARXIV-2606-12764`。

  **已吸收的语义增量：** Code training-data audit 必须检测 functional equivalence，而不能只依赖文本 overlap；应以 exposed target 对未 exposed reference 做 counterfactual execution comparison。
<!-- daily-books-trace:SF-2026-ARXIV-2606-12764:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18284:start -->
- `SF-2026-ARXIV-2606-18284` — Daily `2026-06-11`；primary `arXiv:2606.18284v1`；Books review `books-review:SF-2026-ARXIV-2606-18284`。

  **已吸收的语义增量：** 训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18284:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13629:start -->
- `SF-2026-ARXIV-2606-13629` — Daily `2026-06-12`；primary `arXiv:2606.13629v1`；Books review `books-review:SF-2026-ARXIV-2606-13629`。

  **已吸收的语义增量：** synthetic-data inference 必须把 generator、selection/filter与downstream sample视为同一随机过程，并检验 task-level exchangeability 后才报告置信区间
<!-- daily-books-trace:SF-2026-ARXIV-2606-13629:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13873:start -->
- `SF-2026-ARXIV-2606-13873` — Daily `2026-06-12`；primary `arXiv:2606.13873v1`；Books review `books-review:SF-2026-ARXIV-2606-13873`。

  **已吸收的语义增量：** source-level unlearning若是硬需求，应在训练时把shared backbone与source-addressable sparse sinks分离，并把disable-sink作为部署revoke动作
<!-- daily-books-trace:SF-2026-ARXIV-2606-13873:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15216:start -->
- `SF-2026-ARXIV-2606-15216` — Daily `2026-06-14`；primary `arXiv:2606.15216v1`；Books review `books-review:SF-2026-ARXIV-2606-15216`。

  **已吸收的语义增量：** pretraining subset selection 应在 gradient space 以 set-level diversity 与 quality 联合优化，而不是逐样本 top-score。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15216:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15367:start -->
- `SF-2026-ARXIV-2606-15367` — Daily `2026-06-14`；primary `arXiv:2606.15367v1`；Books review `books-review:SF-2026-ARXIV-2606-15367`。

  **已吸收的语义增量：** deep-research 训练数据应从 graph-grounded task 生成，经真实 AgentLoop rollout，再用多维 trajectory verifier 决定收录。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15367:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16110:start -->
- `SF-2026-ARXIV-2606-16110` — Daily `2026-06-16`；primary `arXiv:2606.16110v1`；Books review `books-review:SF-2026-ARXIV-2606-16110`。

  **已吸收的语义增量：** machine-unlearning 验收需要无需 scratch retrain/shadow fleet 的 proof-of-ignorance audit，并显式保存攻击面与误判边界
<!-- daily-books-trace:SF-2026-ARXIV-2606-16110:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17122:start -->
- `SF-2026-ARXIV-2606-17122` — Daily `2026-06-16`；primary `arXiv:2606.17122v1`；Books review `books-review:SF-2026-ARXIV-2606-17122`。

  **已吸收的语义增量：** instant unlearning 可把 passport 嵌入 LoRA 表示并以 authority-mediated verification 验证配置，但 deactivate credential 不自动证明所有信息删除
<!-- daily-books-trace:SF-2026-ARXIV-2606-17122:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21337:start -->
- `SF-2026-ARXIV-2606-21337` — Daily `2026-06-20`；primary `arXiv:2606.21337v1`；Books review `books-review:SF-2026-ARXIV-2606-21337`。

  **已吸收的语义增量：** 训练数据 pipeline 应将任务生成、过滤、difficulty routing 与训练后 validation 绑定同一 lineage，synthetic volume 不是质量证明
<!-- daily-books-trace:SF-2026-ARXIV-2606-21337:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22142:start -->
- `SF-2026-ARXIV-2606-22142` — Daily `2026-06-21`；primary `arXiv:2606.22142v1`；Books review `books-review:SF-2026-ARXIV-2606-22142`。

  **已吸收的语义增量：** RoboLineage 把 rollout、review、dataset decision、training run、policy metadata、evaluation、deployment recommendation 与 next-collection plan 变成 typed lineage artifacts，agent 只能在 artifact boundary 内推进。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22142:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06442:start -->
- `SF-2026-ARXIV-2607-06442` — Daily `2026-07-08`；primary `arXiv:2607.06442v1`；Books review `books-review:SF-2026-ARXIV-2607-06442`。

  **已吸收的语义增量：** 新增证据边界：Replace trajectory-count coverage with reusable-structure coverage: allocate budget over primitive compositions and transition interfaces under diminishing returns, then choose stable representatives within each structural bucket. 该 delta 已进入 `books/part-04-training-system/27-data.md#L393`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06442:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06558:start -->
- `SF-2026-ARXIV-2607-06558` — Daily `2026-07-08`；primary `arXiv:2607.06558v1`；Books review `books-review:SF-2026-ARXIV-2607-06558`。

  **已吸收的语义增量：** 新增证据边界：Decouple operator time from physical robot recording by driving an action-conditioned video world model with human hand poses, retargeting the pose stream to a robot schema and treating the generated egocentric sequence plus action label as a derived training trajectory. 该 delta 已进入 `books/part-04-training-system/27-data.md#L411`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06558:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16900:start -->
- `SF-2026-ARXIV-2607-16900` — Daily `2026-07-19`；primary `arXiv:2607.16900v1`；Books review `books-review:SF-2026-ARXIV-2607-16900`。

  **已吸收的语义增量：** 新增证据边界：API specifications seed solvable tasks; a teacher proposes calls, a history-conditioned simulator produces derived responses, schema and semantic checks filter transitions, and a trajectory judge admits SFT traces before real-environment evaluation. 该 delta 已进入 `books/part-04-training-system/27-data.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16900:end -->
