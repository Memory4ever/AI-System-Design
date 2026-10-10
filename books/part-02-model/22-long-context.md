# 第22章 Long Context

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-LONG-CONTEXT`
**Legacy Chapter:** Ch22
**Status:** Draft

**Roadmap Intent:** 长上下文为什么困难，位置编码、显存、注意力复杂度和检索增强如何互相影响。

## 本章要回答的问题

为什么把 context window 从 8K 扩到 128K 或更长，不只是修改一个长度参数？模型能够接收长输入、能够在远处保持位置关系、能够找到相关信息，以及系统能够承载它们，为什么是四个不同问题？

本章的核心判断是：**Long Context 是位置有效性、Attention 计算、KV Cache 容量、信息利用与系统 SLO 的联合能力。**任何只移动一个瓶颈的方案，都不能自动得到可用的长上下文系统。

第 21 章通过条件计算扩展参数容量，本章处理另一条正交轴：同一个模型怎样承载更长的输入与状态。它不是 MoE 的下一层，而是回到第 13、14、15、19 章，把此前分散出现的 `T` 重新放进一个联合约束模型。

第19章已经定义 KV 的逻辑对象与复用条件；本章进一步决定哪些历史必须继续可寻址、哪些可以压入状态。物理驻留、分页和失败恢复仍交给 Part V，不把状态表示变化误写成 runtime 的免费优化。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`H` 表示 Query head 数，`H_kv` 表示 Key/Value head 数，`d_h` 表示单个 head dimension，`L` 表示 layer 数，`b` 表示每个 cache 元素的 bytes。

## 先拆开四种能力

讨论“支持长上下文”时，至少要区分：

1. **Accepted length**：接口、模型配置和 kernel 能否接收 `T` 个 token。
2. **Positional generalization**：位置机制是否在更远位置保持稳定关系。
3. **Effective utilization**：相关信息进入窗口后，模型能否检索、组合并抵抗干扰。
4. **System capacity**：能否在可接受 TTFT、TPOT、吞吐、显存与成本下承载。

一个系统可以接受 128K tokens，却在远距离依赖上明显退化；也可以离线答对长文档，却因单请求 cache 太大而无法在线并发。最大长度只是上限声明，不是质量或容量证明。

## Position Encoding 的外推边界

第13章说明位置机制如何让 Attention 看到顺序。将 `T` 扩大时，第一个问题是新 positions 是否位于训练分布内。

Learned absolute table 可能根本没有对应 rows；sinusoidal 与 RoPE 可以计算更远位置，却不保证模型在训练中学会使用这些频率区间。RoPE scaling、插值或长序列继续训练，会改变位置分布与频率映射。

因此：

```text
position function is defined at T
!= model behavior is reliable at T
```

长度扩展必须通过 distance slices、不同位置放置和组合任务评估，而不只验证 forward 不报错。

## Prefill 的 Attention 成对成本

长度为 `T` 的 dense Self Attention，每个 Query 与 `T` 个 Keys 建立关系。每层 score/aggregation 核心计算近似为：

```text
O(B * H * T^2 * d_h)
```

逻辑 score shape：

```text
[B,H,T,T]
```

FlashAttention 通过 IO-aware tiling 避免在 HBM 中完整物化全部中间 scores，并降低 memory traffic；它仍计算 exact dense pair interactions，不能消除 `T^2` FLOPs。

长 prompt 因而放大 Prefill compute、workspace、排队和 TTFT，并可能干扰同 GPU 上正在 Decode 的短请求。

## Decode 的 KV Cache 线性增长

第19章得到：

```text
KV bytes = 2 * L * B * T * H_kv * d_h * b
```

它对 `T` 线性增长，却乘上 layers、KV heads、head dimension、dtype 和并发。这里沿用等长 batch 抽象；变长请求应使用第 19 章的 `sum T_r`。单请求长上下文会占据更多 cache，直接降低可同时服务的请求数。

Decode 每步还要读取更长历史 K/V。即使容量足够，memory bandwidth 与 TPOT 也可能随上下文增长而恶化。

所以 Long Context 同时影响：

```text
Prefill: pairwise compute and TTFT
Decode : KV capacity, bandwidth and concurrency
```

## 一个长度翻倍小例子

忽略其他维度，将 `T` 从 8K 翻倍到 16K：

```text
Dense Attention pairs:
(16K)^2 / (8K)^2 = 4x

KV Cache elements:
16K / 8K = 2x
```

位置外推质量则没有固定倍数，必须实测。这个例子说明，同一次长度翻倍会对不同层产生不同增长规律。

## Effective utilization 为什么不能由长度推出

模型可能在短距离 retrieval 上表现良好，却忽略窗口中部、被无关上下文干扰，或无法组合分散证据。原因可能来自训练长度分布、Attention pattern、position mechanism、任务难度和 evaluation prompt。

“Needle in a haystack”可以测试精确检索，却不能完整代表跨段推理、代码依赖、时间顺序或多文档冲突。反过来，平均 QA 分数也可能掩盖特定位置退化。

### 长上下文容量必须同时声明计算、状态与读取合同

Attention 保存完整历史并随长度增加计算，固定递归或压缩状态用有限容量换长度无关的单步更新，外部检索则把历史放到可查询存储。三者不是一场只有一个赢家的架构比赛：在有限精度下，系统无法同时获得与历史长度无关的计算、固定大小状态，以及随事实数量增长的 worst-case exact recall。设计必须至少放松一项——允许 compute 或 state 随长度增长，或把 correctness 改为近似、分布化和可拒绝的 retrieval contract。<!-- source-family:SF-2026-ARXIV-2605-05066 -->

即使参数量相同，“可存多少”也不能脱离“怎样读出”。Top-1 winner-take-all 必须让正确项压过所有干扰项，极值竞争会带来随候选数增长的额外压力；listwise 或 Tail-Average Margin 只要求正确项进入可交给 reranker/verifier 的候选集合，因此可以获得不同容量阈值。后者降低门槛，是因为 correctness 定义改变了，不是免费得到更多精确记忆。现有理论只覆盖 linear memory、isotropic Gaussian associations 与其准则，TAM 的部分渐近结论还依赖假设；小 tail 退回 top-1 的行为仍未完全解决。<!-- source-family:SF-2026-ARXIV-2605-05189 -->

softmax 读取还存在另一种受限极值压力，不能与线性记忆的容量定理混为一谈。设只有一个 decisive evidence，其 logit 上界为 γ，N 个干扰 logit 独立同分布为零均值 Gaussian、方差 σ²，温度 τ 固定；再假定正确证据的 attention mass 低于 ρ 时，decoder 正确率至多 a₀。此时 accuracy 至多为 `a₀+(1−a₀)Φ((γ+τ log((1−ρ)/ρ))/σ)^N`，其中 Φ 是标准正态累积分布函数。在这些前提内，为容许固定的高 accuracy，证据 margin 必须随有效干扰数承担约 `σ√(2 log N)` 的增长压力。N 指能竞争 softmax 尾部的干扰项，不等于窗口 token 数；真实 logit 的相关性、非 Gaussian 分布、多条互补证据或其他读出路径，都可能越出该抽象，不能据此断言长窗口必然失败。

把候选压到 K 项可以减少竞争，却同时产生漏掉必要证据的 recall penalty；只在 retrieval-hit 子集改善，不代表总体答案更好。相应 gate 命题仍是条件上界，不是改善的下界保证。[受限验证](https://arxiv.org/html/2609.22101v1)在固定 100 QA 的 GPT-4.1 配对实验中，512K 固定 K=16 的总体增益区间跨零；扩大 K 以恢复 support recall 后，增益区间下界仍为零、McNemar p≈0.09。另有有限 filler 测试未观察到退化，也不满足该定理的分布假设。因此这条分支要求同时验收有效竞争、gate recall 和无条件 outcome，并支付检索、预算选择与证据检查成本；证据互补、检索漏失或假设不成立时，完整上下文与既有 verifier 继续合理，不能单向缩 K。<!-- source-family:SF-2026-ARXIV-2609-22101 -->

因此容量测试必须绑定读取规则、候选集大小、后续 verifier、数据结构和失败代价。结构化数据、近似召回或允许外部存储时，固定状态仍可能是好方案；需要最坏情况精确回读时，完整历史或可验证检索仍不可替代。模型层只定义可表示和可读取的状态，Part V 再承担 Prefill、Decode 与 KV 的实际成本。

直接 lookup 的记忆残差可以成为明确的读取 reference，而不必无条件混合所有生成表示。一个条件分支分别从检索 cue 和关闭记忆的 backbone 额外前向生成 latent 候选：先训练记忆及读取接口，再冻结这些路径，以训练时 future-token likelihood 相对 reference 的增量监督 router。推理只用当前状态预测增量与 confidence，超过门槛才以有界插值修正直接残差；未通过则在该注入位置精确返回 reference。这样把候选生成、路由监督与实际采用分开，但全路径端点标签不能因果分摊到某层，likelihood 增量也不是真值或正确性概率。

生成路径增加 reader/generator 参数、额外前向和阈值校准成本，局部 reference fallback 更不等于整个模型安全。[受限 MemoryAthena 实验](https://arxiv.org/html/2609.25853v1)中各生成路径并非一致优于直接读取，普通 soft fusion 有退步，个别任务须调整阈值；独立 GPT-2 microbenchmark 仍以直接路径更快、更省驻留内存，不能与 Mistral 的下游任务质量拼成同一系统收益。门槛漂移、训练监督不适配或额外成本过高时，保留直接 lookup/既有表示路径；需要事实验证时仍交给独立证据机制，而非扩大模型内 router 的权限。<!-- source-family:SF-2026-ARXIV-2609-25853 -->

保留完整历史还没有回答一个更小的问题：正确 token 明明可访问，当前 answer state 是否能从竞争内容中选择并读出它？专门训练的浅层 Transformer 可以学会精确相对位置读取，预训练 chat 模型却未必沿同一路径计算。在受限 N-back 回读实验中，近期非目标项、重复字母和序列转移统计会改变表现；跨层表示测量支持一种解释——部分内容在共享表示中竞争，中层先降低它们的重叠，晚层才把目标对齐输出读头。这里的瓶颈是学到的选择与读出，不等于 KV 丢失，也不能由模型拥有更长窗口直接解决。

这种解释可以用定点干预检验，但不能直接变成部署配方：在首层的答案位置，把字母身份方向上的变化移向其平均投影，可以在部分模型与负载上改善回读；这只支持该方向对所测任务的局部干扰，既不是删除所有 token identity，也不证明其他信息应一并压制。方向和强度搜索增加校准成本，选择每个模型/负载上的最大收益还会高估固定策略的迁移性；自然语言、thinking、外部记忆或不同 chat 格式下需要重新验证。任务明确且专训的位置读取已可靠时，直接索引式路径仍是合理基线；共享表示的抑制过强反而可能损害内容使用。<!-- source-family:SF-2026-ARXIV-2604-09670 -->

读取失败还应把位置效应与背景竞争拆开：固定证据位置和内容，只改变近端无关背景的数量或 logit，就可能改变归一化后的证据质量。在 M 个同分背景的简化模型中，证据权重为 `1 / (1 + M exp(s_background - s_evidence))`；距离没有改变，数量与 score gap 仍能共同稀释读取。RoPE 旋转保持范数，并不保证任意内容对都随距离单调衰减。因此位置扩展解决可访问范围时仍合理，但不能单独修复已经可访问、却被竞争内容淹没的证据。

一条条件分支对旋转后的 Q/K 归一化，再以 t-distributed 映射整形相似度；这保留位置变换与 mask，却改变原 dot-product 对范数的依赖。相对同温 cosine 基线，收益还要求证据/背景的相似度差与映射压缩程度满足相应条件，不能由排序不变推出归一化证据概率必然增加。[Sirens/LYRA 的受限对照](https://arxiv.org/html/2609.26718v1)微调整个末 block，其他方法未全部使用匹配训练，部分任务及较大整形参数会退步，不把收益唯一归因于 QK 变换。它也没有减少 dense Attention 的复杂度或 KV 容量，额外 FLOPs 分析不是实机延迟。校准或任务质量不通过时，保留原 QK、位置扩展与显式检索；诊断继续分别改变位置、背景数量和内容，而不是把所有失败统称距离不足。<!-- source-family:SF-2026-ARXIV-2609-26718 -->

评估至少应切分：

- 信息所在绝对位置与相对距离。
- 单点 retrieval 与多证据 composition。
- 干扰信息数量与冲突。
- 输入长度、输出长度和任务类型。
- 正确率、拒答、引用与延迟成本。

比较容量曲线时，还应分开“相对自身最佳表现还能保留多少”和“是否达到同一任务要求”。设负载K、干扰D下回读率为p_D(K)，单绑定ceiling为C_D，chance为b，且C_D>b；自身归一化r_D=(p_D−b)/(C_D−b)适合比较退化形状，却会把ceiling损失移出曲线。绝对要求π>b对应r_D≥(π−b)/(C_D−b)，不同模型或干扰条件的相对门槛因此不同。在回读率不增的前提下，ceiling已低于π便没有合格负载；等于π仍可能在首点或plateau合格，高于π也不能把域外交叉当实测容量。

[受限binding测量](https://arxiv.org/html/2609.30634v1)中，自身midpoint几乎不变仍可伴随固定reference明显下降；专训与预训练size-law外推的差距也不是直接测得的可释放容量。报告应保留(K,D)实测可行集合、absolute requirement、chance/ceiling和两处不确定性，拟合外推与censor另列。更细的长度、位置、干扰及模型校准增加测量费用；单query回读不认证全部属性联合正确、动态更新或action遵守。绝对要求不满足时，完整历史、显式重申或外部可验证索引仍是合理选择，不能靠归一化、窗口规格或一次probe为运行负载签发能力保证。<!-- source-family:SF-2026-ARXIV-2609-30634 -->

### 信息仍在 Residual 中，不等于当前路径还能使用它

多轮交互中“丢失系统目标”不能只用窗口截断解释。受限层级测量显示，指向 goal tokens 的 attention accessibility 会随轮次下降，即使与目标相关的信息仍可从 residual representation 解码；这把状态分成“信息是否存在”和“当前生成路径是否能读取并使用”两层。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12922 -->

Probe 可解码不证明信息拥有因果控制，滑动窗口和特定模型结果也不能代表所有架构。系统应同时监测目标 token 可达性、行为遵循和干预效果；诊断不能复现时，回退显式重申、context compaction 或外部 workflow state，而不是只增大窗口。

### Token 数不等于 Effective Context

标称窗口以 token 计数，但同一源序列经 fragmentation 或不同 tokenizer 后，每个 token 覆盖的源信息跨度不同。即使编码无损，更细碎的表示也会让固定 token window 看到更短的原始依赖，因此 long-context identity 必须包含 tokenizer revision、fragment boundary 与 source-span distribution。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13485 -->

理论构造说明 achievable loss 会受有效源跨度影响，却没有证明具体 Transformer 一定实现该 predictor 或训练能找到它；tokenizer 还要平衡 vocabulary、输出层成本和长尾 token。无法证明新 tokenizer 改善真实 source-span coverage 时，应保留原 tokenizer，并按源文档跨度而非 token 数比较能力。

## 决策地图：先判断要移动哪个瓶颈

| 方案 | 主要改变对象 | 没有自动解决 |
| --- | --- | --- |
| RoPE scaling / long training | 位置与训练分布 | Attention/KV 成本 |
| FlashAttention | Dense Attention IO | `T^2` pair FLOPs |
| Sparse/local Attention | 连接数量 | 全局信息质量 |
| Hybrid linear/softmax | 长历史状态 + 周期性精确寻址 | 双重状态与执行复杂度 |
| Native learned sparsity | 训练时连接与实际 KV traffic | selector 错误与专用 kernel |
| Ring Attention | 设备容量与分布执行 | 总资源与通信 |
| GQA/MQA/quantization | KV elements/bytes | 位置外推与信息利用 |
| Offload/ShadowKV | Memory hierarchy | 传输延迟与选择误差 |
| RAG/compression | 进入窗口的信息量 | Retrieval/压缩损失 |
| Test-time neural memory | 在线压缩、写入与遗忘 | 精确回读、污染与状态治理 |
| Context-turnover recurrent state | Working context 之外的计算连续性 | 精确归档、无界位置与跨会话治理 |

这张表是 Long Context 的工程决策核心：先识别当前约束，再选择直接作用于该约束的设计。

从 dense softmax 的完整历史出发，状态预算与读取成本会推动不同分支，而不是形成一条必然替代的时间线：

- 线性 Attention / 递归状态压缩历史，降低随长度增长的状态成本，但限制未来查询可恢复的细节。
- Hybrid 将固定状态与显式 Attention 组合，保留两种访问方式，也同时承担它们的执行与管理成本。
- Query-aware sparse Attention 继续保留可寻址历史，只选择部分位置参与当前计算；索引器可以原生训练，也可通过 continued training 迁入既有模型。这是另一条设计分支，不是从固定状态演化出的必经后继。

下面先处理位置与训练这一共同前提，再沿历史保存方式分开讨论：保留可寻址历史时，问题是怎样少读、由谁选择；将历史压成状态时，问题转为容量、写入与遗忘；需要两者时，再决定 hybrid 分工和 checkpoint 迁移。外部工作集改变模型看到什么，分布执行与 KV 分层则负责把选定语义落实到资源上。它们可以组合，不构成必然替代的阶段。

## 共同前提：先验证目标距离上的位置有效性

位置插值、RoPE scaling、relative bias 或长序列 continued training，主要解决模型是否能在新距离上形成有效位置关系。

它们不自动降低 Attention FLOPs，也不减少 KV Cache。继续训练还需要长样本、更多 activation memory 和分布设计。

因此这条路线的主要输出是模型有效性，不是系统容量。

### 位置索引一致性需要保持内容与可见性不变

延长位置范围之外，还可在相同token内容和causal mask上，只让suffix的RoPE index出现跳跃；用标准位置view的stop-gradient分布作teacher，对扰动view做suffix reverse-KL，并保留CLM。这把“可见材料没有变”与“位置坐标改变后模型是否稳定”分开，不是真实文档重排，也不取消语义顺序或任务对位置的依赖。Teacher只提出一致性目标，不因stop-gradient就获得事实真值或零成本身份。

额外teacher forward和一致性约束换位置稳健性，也可能固化teacher错误、压制有效的位置敏感行为。`arXiv:2604.14339v1` 受测Llama8B64K/16A100、Qwen4B256K/32A100中，额外forward约增加到1.6× step时间；CLM多1.6×steps是wall-clock对照，不是同训练token。NoPE 29.5、chunk permutation 46.2均低于baseline47.9，不支持任意扰动都有效。长短context切片或teacher一致性回归失败时，应回退普通CLM与已验证scaling；这一训练分支不是直接降低runtime Attention/KV成本或扩大可用容量的保证。

<!-- source-family:SF-2026-ARXIV-2604-14339 -->

### Multimodal Long Context 需要联合迁移数据与位置策略

把文本长上下文配方直接搬到 VLM，会混淆视觉 token 密度、文档布局和长度外推。更完整的 continued-pretraining 合同要共同版本化 document pool、视觉页面编码、长文问答与转录任务比例、位置策略，以及短上下文到超训练窗口的分层评价；否则“支持 128K”无法说明模型实际使用了哪些模态证据。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13831 -->

受限实验把一个 7B 模型从 32K 扩到 128K，并报告更长窗口表现，但不能证明任意 VLM、数据域或 256K/512K 生产质量。若长文训练损害短上下文、OCR 或跨页检索，应回退较短窗口、分段检索或分层摘要，而不是用标称长度覆盖行为退化。

跨页任务还需要把页面 identity 当成训练和推理共同使用的接口，而不是测试时临时加一个标号。Page index 可以让问答引用具体页面，但模型只有在训练中见过同样的标识与文档编码，才可能可靠地消费它；仅在评价时添加 index 的反侧说明，更多 metadata 不必然更有帮助。训练窗口、实际页数、视觉分辨率与输入长度分布应分别记录，344K 的位置窗口不是336页，也不说明每篇都达到最大长度。<!-- source-family:SF-2026-ARXIV-2602-15257 -->

[Long-context visual documents v1](https://arxiv.org/html/2602.15257v1)的 page-index train+eval 对照支持这一受限接口条件，但同时变化的动态分辨率、CPT/SFT/LongPO预算和 merged-weight artifact 不能归为单独长度效应。递归 teacher 数据在一项视觉平均分改善却使修正版 MMLongBenchDoc 54.5 低于普通57.0；LongPO增加计算也不是各任务均胜。评价纠错更换了问题/答案并移除无法作答条目，须固定其版本后比较，不能合并旧分数。页编码、训练接口或短任务回归失败时，保留较短窗口、分段检索与分层摘要；本条件不授文档事实正确性或生产吞吐。

## 保留可寻址历史：从访问图约束到稀疏选择

位置关系可用以后，下一问是每个 Query 是否必须读取全部历史。这里先保留历史的显式身份，只改变可见范围与选择规则；如果连历史本身都无法承担，再转向下一节的固定状态。

先区分两种改变：稀疏 Attention 保留可寻址历史而减少读取边，固定状态模型则把历史写入受限状态，不再逐项保存。前者主要改变访问图，后者同时改变记忆容量与更新规则；两者可以组合，但不能共用“少算一些 Attention”的解释。

Sliding-window、local、block-sparse 或 global/local hybrid Attention 减少每个 Query 直接连接的 Keys 数量，使算法不再执行全部 `T*T` pairs。

代价是信息图发生变化。远距离 token 可能需要多层传播，或必须通过少数 global tokens。计算下降不保证任务质量不变。

“长上下文任务”还必须按**语料关系的需求**分层，而不能只按 token 长度或单事实检索得分分层。找一条事实通常可逐文档检查；找出所有互相矛盾的声明、跨两组材料配对或动态发现稀有类别，则可能需要随文档数增长的多文档关系比较。此时独立处理各文档、只让少数 query token 作全局读取的 block-sparse 路径，省掉的恰可能是任务所需的交叉关系；较短语料上的“近似无损”不能替更复杂关系的长语料签字。

因此比较 dense、sparse 和 recurrent/hybrid 时，应在相同语料构造和评价预算下分别测单事实检索、跨文档配对/矛盾、聚合与长度外推，并把训练所见长度、mask/状态路径和所省计算一起记录。[受控语料复杂度研究](https://arxiv.org/html/2609.29245v1)在其 2K～32K、22 项任务和有限模型上观察到：低关系复杂度任务中 block-sparse 与 full attention 接近，高复杂度任务的差距随长度增长；短上下文训练向 64K/128K 外推亦显示条件差异。这是**评测任务与访问图匹配**的证据，不是任意任务都需要全连接，也不是对百万 token 规模的证明。对稀疏路径必要的跨文档边无法稳定定位、或高复杂度质量门禁失败时，应增加全局交互、分阶段显式配对/检索，或在可负担范围内回退 dense；以局部证据查找为主、语料关系稀疏且延迟敏感时，原有稀疏/递归分支仍成立。论文用候选 oracle 算法给任务分级，并未证明每类任务的严格复杂度下界；其部分合成任务和不同模型训练预算也限制了普遍化。
<!-- source-family:SF-2026-ARXIV-2609-29245 -->

FlashAttention 与 sparse Attention 必须区分：

```text
FlashAttention  same dense semantics, better IO execution
Sparse Attention fewer pair connections, changed model semantics
```

<!-- semantic-body-binding:SF-2026-ARXIV-2605-00768:start -->
### Local 与 Global Attention 是互补算子，不只是精度—成本折中

把 global attention 截成局部窗口首先是计算优化，但它也改变了单层可表达的时间关系：global operator 可直接读取任意历史位置，local operator 则天然保留相邻顺序和有限邻域组合。因而 local 不是 global 的纯低成本近似；在固定精度、固定深度和受限位置谓词下，local-only 与 global-only 可识别不同的 temporal relation，组合两者才覆盖更丰富的函数类别。

系统设计因此不能只比较 FLOPs。window、global token 与 hybrid layer placement 同时决定信息传播路径；扩大深度可以让很小的 local window 逐层传播远距信息，却增加 latency、训练难度和中间状态，增强位置编码也可能缩小理论差异。长距离精确 retrieval 或浅层直接依赖仍适合 global/dense 分支，强局部结构、规则 kernel 与成本敏感 workload 才更适合 local；hybrid 获得表达互补性，同时付出不规则执行和路由校准成本。

exact-v1 的结论建立在 fixed-precision、fixed-depth formal-language recognizer 和有限 positional predicates 上，并以所选自然语言实验作一致性证据；它不证明任意 LLM、任意深度或生产 workload 的质量排序。该理论只解释为何 global/local hybrid 可能改变函数类别，具体窗口和 kernel 仍需由训练分布、硬件与 SLO 验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-00768:end -->

### Immutable Task Prefix 与 Recent Reasoning State 可以分治

Sliding window 丢弃最旧 token，在局部依赖主导时简单有效；Agent reasoning 却常同时依赖开头的 system/task
contract 与最新工作状态。一个更有条件的分支固定保留不可变 task prefix，只让中间推理历史滑出，并保持
RoPE position 与 KV identity 连续：

```text
immutable task / system prefix
+ recent reasoning window
→ bounded attention state
→ continued absolute positions
→ next reasoning step
```

训练也必须模拟同一可见性：长序列只对末端窗口计算 loss，并让 prefix 与 recent window 共同提供条件。它用
bounded KV 和 tile skipping 换取中间证据丢失、tool output 淹没窗口与更复杂 kernel/mask；短生成、需要精确
回看完整轨迹或 task prefix 会变化时，完整 Context 或 retrieval/compression 仍更合理。Prefix Sliding 的结果
绑定 Qwen3 1.7B/7B、单 H100 与特定 window，不能外推任意模型或生产 serving。

### Context Anchor 从 Passive Sink 演进为独立状态轨道

BOS/attention sink 可自然聚合全局信息，却不保证它保存的是当前 query 所需 evidence。硬替换 BOS 会破坏原
计算，静态融合又固定强度；另一分支保留 causal self-attention，同时在少数层用 cross-attention 更新独立
anchor state。它新增 source/context identity、anchor freshness、injection-layer contract、malicious-context
amplification 与 KV/cache compatibility。短 Context、原生 long-context training 或 RAG 已能提供精确证据时，
不需要额外 anchor。SinkTrack 仅提供 Experimental evidence，不证明 dual-track anchor 普遍优于原生 Attention。

attention sink 还可能不是某个特殊 token 的语义需求，而是多层算子共同制造的结构性不平衡：value aggregation 的方差差异、FFN 中少数 super-neuron 与维度尺度分化，会让部分位置成为低成本的剩余注意力落点。受控干预能制造或移动 sink，head-wise RMS normalization 也能削弱作者设置中的现象，但这仍是条件性机制假说，不是“所有 sink 都由同一原因产生”的证明。把它当作诊断，可要求同时观察 head/position 方差、异常维度与长程任务质量；把 normalization 当作 actuator，则要重新验收训练稳定性、KV 兼容和真实 retrieval。证据不匹配或收益不覆盖结构变化时，保留 BOS/anchor、训练分布调整与普通 attention baseline。

<!-- source-family:SF-2026-ARXIV-2605-06611 -->

### Conditional Attention 的路由粒度必须匹配执行粒度

固定 full/local/sparse layer 配置可预测、易编译，也让所有请求共享同一 KV contract；它的边界是不同 prompt
需要的远程依赖并不相同。Prompt-conditioned router 可以在 Prefill 读取边界表示，为每层选择 Full 或 Sparse
Attention，并让 Decode 固定复用该 route：

```text
prompt + model revision
→ layer-route vector
→ KV retention / sparse-kernel plan
→ Decode reuses immutable route
```

Head-level route 更细，却容易造成同一 kernel 内不规则 memory access；layer-level route 损失表达粒度，但更容易
整体跳过远端 KV traffic。Route vector 必须进入 prefix/KV/cache identity；tool result 追加或 Context mutation 后
要定义延续、重算或 fallback。固定配置在 batch 规整、graph capture、cache sharing 或 calibration 不可靠时仍然
合理。Flux Attention 的作者结果只覆盖特定模型、A800、batch 1、BF16 和 sparse kernel，不是 production goodput。

#### Sparse Attention 的 Block Size 也是 Per-head 路由状态

固定 block size 让 layout、kernel 和 KV contract 可提前编译，在 head 行为近似时效率稳定；不同 head 的远程依赖与局部密度不同时，同一粒度会让部分 head 过算、部分 head 丢失上下文。adaptive branch 为每个 head 选择 block size，并让 route、mask、kernel/layout 与 KV retention 共同进入 execution identity，而不是把算法稀疏率与可实现速度分开报告。

细粒度选择减少无效 attention，却增加 route metadata、kernel fragmentation、负载不均和编译缓存；错误路由还会造成不可恢复的信息遗漏。上下文短、head 差异小或硬件只优化固定 tile 时，统一 block 仍更合适。`arXiv:2605.12110v1` 的 §2–§4 与结论只支持作者模型、kernel 与硬件，不能把 headline 稀疏率直接外推为端到端 serving 加速。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12110 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20813:start -->
固定 selector 可以省去在线路由开销，却会在上下文结构变化后持续使用过期列。周期刷新 column-sparse
Attention 的 selector state，是在静态稀疏与逐 token 重路由之间增加 cadence：刷新间隔较长时摊薄选择成本，
较短时更快跟随依赖漂移。代价是 selector revision、刷新 kernel、编译 layout 与 KV retention 必须共同版本化，
刷新瞬间还会造成负载波动。作者模型与 kernel 的结果不证明通用长上下文收益；selector 不稳定、刷新成本过高
或质量 Gate 失败时，应回退固定 sparse pattern 或 full attention。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20813:end -->

### 从固定访问图到可训练选择器：同时约束语义与硬件

另一种压缩路径把 chunk 内的直接 token 访问与跨 chunk 的 summary handoff 分开：处理当前 chunk 时保留细粒度原文，完成后通过 summary 接续后文；cache 显式维护各自的三个状态段，summary 只能读取其所属 chunk，不能偷看后续文本。Chunk 边界必须完成 direct→summary 的交接，不能让 partial chunk 既退出直接窗口、又尚未进入完整 summary，形成两端都不可见的盲区。训练、attention mask 与 cache identity 必须一致，不能用一次 prompt 摘要替代完整 handoff 协议。<!-- source-family:SF-2026-ARXIV-2604-24432 -->

它用受限跨 chunk 信息通道换长上下文预算，同时增加 summary 训练、三段 cache 生命周期和边界更新成本；压缩会丢失尚未知道未来 query 是否需要的证据，不保证摘要语义无损。精确引用、细粒度远程依赖或 chunk 分布迁移时，应保留原文检索/回读或更大 direct window，并分别检查吞吐与任务质量。

固定 mask 与 prompt-conditioned routing 决定读取范围；若希望选择器随模型一同学习，就还要约束训练和访存。Native Sparse Attention（NSA）给出这一分支的具体机制。它不是在已训练 dense model 上临时剪掉
KV，而是在训练中并行学习三条路径：压缩 block 提供 coarse global summary，query-aware
selection 保留细粒度远程信息，sliding window 负责局部模式；选择粒度又刻意对齐连续
memory block、GQA/MQA 的 KV sharing 和 Tensor Core 执行。它解决了两类旧边界：post-hoc
sparsity 可能偏离训练分布，随机 token 选择即使减少 FLOPs 也可能因不连续访存没有实际
加速。新增成本则是 selector/gate 的训练、专用 backward/kernel、稀疏模式校准，以及选错
远程 block 时不可恢复的信息损失。

DeepSeek Sparse Attention（DSA）展示另一种迁移起点：在已有 MLA 模型上
先以 dense Attention distribution warm up 一个轻量 indexer，再进入 sparse continued
training，让每个 query 只读取 top-k latent KV entries。它说明“原生稀疏”不只可以从头
预训练，也可以通过受控迁移进入既有 checkpoint；但迁移依赖 teacher distribution、长序列
continued-training 数据和专用 kernel，不能从单一作者模型外推成所有 dense model 都可低成本
转换。

稀疏选择器本身还需要明确 gradient ownership。若 auxiliary objective 能反向修改作为 teacher 的
主干分布，模型可能通过移动目标而不是提高 selection recall 来降低 loss。一条更可审计的分支让
dense/Main Branch 拥有语义分布，让 Index Branch 只接收 stop-gradient teacher signal；先以 full
Attention warm up selector，再让它接管主数据流。到执行层，GQA-group shared、block-level selection
用较粗粒度换连续访存，KV-outer loop 则反向收集选择同一 KV block 的 queries，并对热门 block 做
CTA 拆分与 two-phase softmax combine。于是完整契约是：

```text
teacher distribution ownership
→ selector warm-up and migration boundary
→ GQA-group / block selection granularity
→ KV-outer reuse and hot-block load balancing
→ end-to-end Prefill / Decode evidence
```

这条路线降低 selector 与 gather 的不规则性，却新增 block 内无关 token、不同 query-head 需求被合并、
selector miss 静默传播、workspace 与专用 kernel portability。MiniMax Sparse Attention 的作者实验只在
其 109B/6B-active、matched-token training 与所披露 H800 microbenchmark contract 下支持这种联合设计；
当前 artifact 的 SM100 contract 不能倒写成历史实验条件。短 Context、严格 exactness、无法 continued
training 或缺少匹配 kernel 时，Dense FlashAttention 仍是合理分支。

无法继续训练模型时，还可只更换 query-aware selector，而不假装它学会了 dense teacher。一条 post-hoc hash 分支把 key 在每张表硬分配到一个 bucket，query 则经连续投影对多个 bucket 给出 soft probability；对每个历史 key，聚合其 buckets 的 query probability 并乘 value norm，再以 graded score 选 Top-K。它用软 query 消除单个 hard-hash 边界的一部分不连续性，让相邻 bucket 也能参与排序；但 value norm 加权与有限 hash tables 只是候选读取规则，不是原 QK softmax mass，也不证明任意 trained KV 上 soft selector 更好。

这个接口仍为全部 $N$ 个 keys 计算聚合分数，省下的是后续读取而非免除历史扫描，hash metadata、建表、prefill 与 gather 也要计费。其角核理论使用随机采样聚合及分布假设，不等于实际 deterministic Top-K；原文最终 attention 权重的伪码与文字不一致，因此这里只采用 selector 接口，不补造最终 weighting 或授 dense exactness。作者 A100/H200 上单层 batch-1 decode 测量不证明 LLM 端到端加速。选择质量或总成本不合格时，保留原 selector 或 dense；若需要降低扫描本身，再考虑下面的层次索引，而非把 hash 排序称为 sublinear retrieval。<!-- source-family:SF-2026-ARXIV-2602-06283 -->

选择器本身的扫描仍随历史增长时，可将 pooled keys 建成由粗到细的 pyramid，每层只展开上一层保留的 bounded Top-K 候选，再在 leaf 对原始 keys 计算 LSE 并读取所选 KV。固定预算、branching、block size 与模型维度时，训练／Prefill 对全部 N 个 queries 的 routing 成本为 O(N log N)，单步 Decode 的缓存更新和 routing 则按 O(log N) 摊销结算。首块、前块和当前块的强制保留及祖先路径要独立处理 causal eligibility，不能让包含未来 keys 的 summary 参与 ranking；最终 attention 仍执行自己的 causal mask。

Leaf 分数精确不修复 ancestor pooling 漏选，所选原 KV 上的精确 attention 也不等于 dense；离散候选的梯度保持固定，不应称直接训练选择决策。层次 metadata 与不同 query 的 tile 复用增加成本，作者短 context 的单层 BSA 反而更快，长 context selection 计时排除了所选 attention 且硬件未披露；forced-block overlap、Top-K reference mass 与真实任务质量又是不同分母。质量或成本失配时，增加预算、退回单层 selector 或 dense；不能由条件复杂度和 selector 倍率推生产 SLO。[PISA §3–4／Appendix B–D](https://arxiv.org/pdf/2609.31093v1) <!-- source-family:SF-2026-ARXIV-2609-31093 -->

Pool 的漏选还可能来自位置编码而不只是摘要容量：block 内内容近稳定时，RoPE 的相位旋转使跨 token 均值按频率衰减，局部位置信号与较慢变化的内容分量不能默认保有相同比例。[一条无需重训的选择分支](https://arxiv.org/html/2602.08426v1#S3)分别对高、低频 band 的 pooled Query/Key 评分，用各 band 相对全向量的 RMS 比例调整温度，再取两张 Top-P mask 的并集；band 可以重叠，温度也只是选择校准，不恢复已经消失的信息或证明 dense 等价。只放大近零高频还会放大噪声，因此 block size、频段、阈值、真实 density 与任务质量要共同验收。有限 long-context 对照仍有检索质量退步，attention prefill 的加速不包含完整 serving；额外评分、mask union、tile overfetch 与校准漂移均付费。内容不满足近稳定条件、关键证据漏选或净延迟不合算时，保留更细粒度、原 selector 或 dense 回退。<!-- source-family:SF-2026-ARXIV-2602-08426 -->

层次 key 索引不是减少全历史评分的唯一方式。若 hybrid 模型已维护顺序递归状态，可以让它的累计表示提供 span-search key：query 先只评分固定 stride anchors，再对选中的连续 span 读取原 KV，最后用 selected-span search scores 的 softmax 合并输出。在 stride 间距与 span extents 满足覆盖条件、候选 span 家族共同覆盖全部 eligible keys 时，没有 token 被固定 pattern 永久排除；top-k 实际读取仍可能漏掉证据。令 \(T\) 为序列长度，两级方案若每 query 的 search 为 \(O(T^p)\)、span 读取为 \(O(T^{1-p})\)，总成本为 \(\max\{O(T^{1+p}),O(T^{2-p})\}\)，理论平衡 \(p=1/2\) 得到 \(O(T^{3/2})\)，不是免费 dense 等价，也不是任意层数搜索都已实现。<!-- source-family:SF-2026-ARXIV-2601-18401 -->

这种分支减少评分与读取计算，却不删除完整 KV；离散 top-k 不求导，只有本轮选中的 span 经过 soft gate 获得梯度，未选证据可能长期缺乏 credit。Routing 冗余和长度课程增加预算、减轻失败但不消除。[受限 feasibility 实验](https://arxiv.org/html/2601.18401v1)在 Nemotron-30B-A3B、单 B200、batch 1、32K chunk 下展示 10M 执行可行，质量只用训练 4K–64K 后的 NIAH 至 256K 检查，仍有失败，不能把最大运行长度当 effective context。短 Context 不偿 kernel 开销、router 漏检或无法再训练时，保留 dense、更宽 selector 或明确原文回读；效率与质量各自验收，不用结构可达签发正确率。20 步 Decode 吞吐与未披露精度也不能认证生产 SLO。

### Selector 可以进入 Forward，但必须显式承担语义责任

Teacher-distilled index branch 把 dense Attention 留作语义 owner，便于校准和迁移；另一条并存分支让
selector 直接进入 Attention forward。对每个远程 chunk，不再只用 mean/max pooled key 给出一个被 hard
top-k 丢弃的分数，而是学习近似 chunk LogSumExp mass 的 summary，并先在 chunks 间分配 mass、再在 chunk
内对 tokens 归一化。由于 chunk score 参与最终 attention output，next-token LM loss 可以直接训练 selector。

这不会把近似 selector 变成 exact full attention。Landmark/query calibration、HoPE/position rule、chunk
size、top-k、local window 与 sparse kernel 必须随 checkpoint 版本化；漏选 chunk 仍是不可恢复的信息损失。
将相邻 queries 的候选 chunks 合并加载可以提高 Tensor Core 利用率，却会引入 union overfetch。短 Context、
严格回读、无法 continued training 或缺少匹配 kernel 时，dense attention 或 teacher-owned selector 仍更合理。
这条分支当前只在作者披露的 345M、1.4B、OLMo3-7B、指定训练 recipe 与单 H800 batch-1 inference contract
下得到验证，不构成通用长度或性能保证。

Selector 的监督还会决定它究竟模仿“Attention 看过哪里”，还是学习“有限预算下什么对任务有用”。用 dense-attention ranking 作 teacher 容易迁移且便于校准；把连续 gate 注入 attention logits，则可让最终 LM loss 直接训练选择器，避免相似度与 task utility 错位。后者获得端到端 credit，却把 selector miss 直接带入模型语义，并新增 pooled summary、稀疏 kernel 和 continued-training 依赖。预算宽松或 exactness 优先时，teacher-owned selector 与 dense fallback 仍应保留。

<!-- source-family:SF-2026-ARXIV-2609-13141 -->

可训练选择器还可以先学习连接的距离几何，而不是先得到每对完整相似度。分别让位置编码后的 query 与 key 选择局部、中程或全局 regime，再用双方分布组合出 pair-dependent decay，作为 attention 的额外 bias；只有双方都选 global 的连接保持不衰减，单侧 global 并不自动否决局部选择。这样可在计算 dot product 前提出访问候选，但soft训练仍需全pairs，有限decay floor也只是衰减而非删除。

将分布投成 top1、将有限tail硬截断、再让kernel只执行选中tile，是三次不同的变化。作者top1质量对照仍使用dense计算及非零floor，不能证明硬稀疏输出或速度；小nominal reach也不直接认证discarded attention mass。双路由、metadata、tile overfetch与kernel成本要另计，有限LM对照保留top1退步及更强cost压力反退。无法维持任务质量、分布漂移或缺匹配kernel时，保留soft/dense或更宽访问图，不从learned geometry推Serving加速。[方法与条件反例](https://arxiv.org/html/2609.31261v1) <!-- source-family:SF-2026-ARXIV-2609-31261 -->

### 无法重训 Target 时，Draft 只能提供稀疏候选

直接由 target model 计算 dense attention 最容易保持原模型语义；当长上下文 pair compute 成为主瓶颈，可以复用较便宜 draft model 的 attention 作为 target 稀疏 admission mask，再只计算被选中的 target attention。这里 draft 只拥有候选连接，target projection、target KV 与最终输出仍是 authoritative state：

```text
draft attention pattern
→ bounded sparse candidate mask
→ target Q/K/V computation on admitted pairs
→ target-owned output
```

这种路径避免重新训练 target，却引入 selector false negative、draft/target 分布漂移和稀疏 kernel 成本。mask 未覆盖关键 token、draft revision 不匹配或稀疏度不足以摊销控制开销时，应扩大候选集或回退 dense attention；作者速度与精度结果只属于其披露模型、长度、稀疏度和 evaluator，不能外推为通用长上下文收益。

<!-- source-family:SF-2026-ARXIV-2605-15508 -->

检索信号也可以只改变dense attention相对权重，而不删除历史。一个受限分支先以少数中层heads的partial forward估计token relevance，再用EMA平滑、累计质量和容量上限选集合；完整forward对被选token的所有heads logits加log β，等于把未归一权重乘β，而非把logits整体乘β。[必要机制与同模型反侧](https://arxiv.org/html/2602.22175v1)只支持这种软提升，全部历史KV和dense矩阵仍保留；query/head profile不是真实检索证书，额外partial forward增加decode计算，长prefill稀释的FLOP估计不是延迟/SLO。随机head已有部分收益、非CoT任务也退步；校准漂移、费用或质量不合算时回退原dense或显式retrieval，不能借用稀疏kernel的省内存结论。<!-- source-family:SF-2026-ARXIV-2602-22175 -->

### 选择器的成本如何摊薄：刷新、复用与地址状态

Sparse Attention 还包含两个独立 ownership 轴。第一，谁周期性读取 full history 并刷新 selector；第二，哪些层或 heads 复用该 selector 与 KV。让少数 full layers 同时产出 block scores 与 global KV，再由后续 sparse layers 复用，可以摊薄全局检索；保留 layer-local sliding-window KV 则维持局部 representation。另一分支只让少数 retrieval heads 刷新 token indices，其余 heads 继承选择集合。

冻结权重中的 `W_K^T W_Q` 几何还可作为不读取运行时 attention score 的候选 admission signal，用于提出哪些 head 更可能承担 retrieval、哪些更适合 streaming。它减少校准 prompt 和在线 profiling 成本，却不把 head role 变成输入无关真值；最终 sparse selection 仍需长上下文任务、输入分布与 dense fallback 验收，multimodal 或 cross-attention 也不能直接继承该分类。

<!-- source-family: arxiv:2608.06849v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: frozen-qk-geometry-as-sparse-head-admission-signal -->

```text
global refresh owner: layer interval / retrieval heads
local state owner: current layer or head
reuse scope: block, head group, adjacent layers
invalidation: model/profile/context revision
```

更粗的复用减少 selector 与 memory traffic，却会放大 stale selection、head imbalance 和 index error；更细粒度选择质量更灵活，却增加 irregular gather、专用 kernel 与 metadata。Dense/full+window 在短上下文、实现成熟度或低迁移风险优先时继续成立。

跨阶段共享还要区分“投影源相同”和“KV 数值相同”。一种训练结构让 self-decoder 的 full-attention 层输出成为后续 cross-attention 的投影源：每个 cross-full 层仍用自己的参数重新生成 K/V，Q 来自当前层；再在第二个域中让 sparse 层复用这些 full 层的 KV 与选择结果。这样 prefill 可以在 self-decoder 末退出，后续消费已形成的源表示，而不是为普通 checkpoint 任意删除后层。强制把最近 token 纳入候选，又可用同一选择集合承担局部覆盖，不必另维护 sliding-window 分支。

这用训练时的源/消费结构与 recent-budget 耦合换取更少重复状态，源表示错误也会传播到多个读取层。[HySparse2 的必要方法与对照](https://arxiv.org/html/2609.26368v1)支持这个受限分支，但 GQA/MQA 和 head 维度也有变化，不能把所有质量或容量收益只归因于桥接；部分任务的 forced-window 与 sparse 选择各有退步，FLOPs/KV 计算也不是部署延迟。没有相应训练结构、迁移风险过高或关键 token 未被选中时，应扩大选择、保留独立窗口或回退 full/dense 路径，不能把早退出当作所有模型无损的推理开关。
<!-- source-family:SF-2026-ARXIV-2609-26368 -->

复用还可以跨相邻 Decode 时间步，而不只跨层或 head。先按当前 query 选 blocks、再在其中选 tokens 的同步流程，选择结果更新及时，却可能把 CPU→GPU KV 传输留在关键路径。一条受限替代路线让当前步的粗选集合为下一步预取，当前步细选则读取上一轮粗选集合：`M_t = BlockSelect(q_t)`，`S_t = TokenSelect(q_t, M_{t-1})`。GPU resident cache 只补入 `M_t` 中尚未驻留的 blocks；细选可用校准后的低维、量化 key index，最终 attention 仍读取被选 tokens 的完整 KV。[AsyncTLS](https://arxiv.org/pdf/2604.07815v1)用这种时间错位重叠选择、传输与计算，改变的是候选状态的生成和消费时点，不是把 full history 永久删除。

收益依赖相邻 query 的 block locality；旧候选漏掉当前需求时，细选无法从未进入候选的 blocks 恢复它，因此这不是 dense attention 的精确等价。校准集、索引量化、block/token 预算与驻留集合都成为兼容状态；我们的实现取舍还应包括分布变化检测以及同步重选或 dense fallback，不能把它们冒充论文已经验证的控制器。作者的 Qwen3/GLM、RULER/LongBench 和特定稀疏预算支持有限质量对照，不支持任意输入无损；offloading 的吞吐还同时受 batch 容量变化影响，不能仅归因于流水化。短 Context、弱 locality 或精确回读优先时，同步选择和 dense 路径仍成立，具体 copy/compute overlap 由运行时兑现。

<!-- source-family:SF-2026-ARXIV-2604-07815 -->

上述路线通常把 token indices 当作由当前 query 或周期性 full layer 重新生成的选择结果。另一条并存分支把
**地址本身**提升为跨层状态：每个 token 除 hidden features 外，还携带稀疏 edge indices 与可微 weights；referral
把两跳候选路径组合后 coalesce，并以 hard top-s 保持固定访问预算，sparse attention 再把 `log(edge weight)` 与
query-key score 一起归一化。这样后续层既传递内容，也能继续演化“下一层应到哪里读取”的地址；它改变的是
Attention 的连接状态，不是替换 MLP。

这种分支用可在 `O(n)` 历史中动态变化的常数级访问，换来 hard selection 后只有保留权重接收梯度、duplicate
coalescing、irregular gather、额外参数和专用 kernel。Dense refresh 或周期性 dense layer 仍要承担全局纠偏与
fallback；短文档、成熟 dense kernel 或必须精确回读时，现有 dense/full+window 方案更可靠。现有
[稀疏 edge referral 与 attention](https://arxiv.org/html/2609.02881v1)只证明 596M 规模、单 seed、15.7B-token
预训练中的可训练性；其文档平均长度远小于 4,096，generic PyTorch 原型反而慢数倍，因此不能据此声称已获得
长上下文能力或端到端加速。

Block selector 还必须尊重 position encoding。对 RoPE 后的 K 在 block 内直接求均值，可能让不同频率分量
发生相消；因此“pool 后再打分”并非与位置表示正交的通用近似。一条受限分支是把低频与高频子空间分开：
低频承担较平滑的 block-level semantic estimate，高频补充局部位置变化，再合并两个候选 mask。它能降低
token-level selection tax，却增加 frequency split、energy calibration、union density 与 RoPE variant 的
兼容状态。固定 block/window 在 position rule 稳定、selection overhead 不值得支付时仍更简单；作者单卡
Prefill 结果不能外推到 Decode、其他 RoPE scaling 或任意 GPU。

### Attention Coreset 给出容量下界，不直接给出 KV 淘汰算法

完整 KV 保留逐 token 寻址，在稀有事实回读、provenance 和误差不可接受时最稳妥；它的代价是容量随序列增长。
若 key/value 具有 unit norm、query norm 有显式上界，并且应用允许 additive approximation error，理论上可以只保留
与序列长度无关的 attention subset，近似原 softmax attention。这个分支说明“所有历史 token 永久驻留”并非每个
受限 workload 的必要条件，但 matching lower bound 也说明 query radius 增大或误差容忍收紧时，所需容量压力无法
被算法技巧消除。

这里改变的是可证明的表示容量边界，不是 runtime 已获得一个 production-ready eviction controller。存在性构造没有
定义 causal stream 中何时选入或淘汰 token，也没有覆盖逐 token provenance、真实 kernel、并发、迁移和延迟 SLO。
因此假设可验证且允许近似时，coreset 可作为后续 selector 的理论目标；需要精确回读、假设失效或尚无可执行构造时，
完整 KV、外部 RAG 与 recurrent/compressed state 仍分别承担精确证据、可治理历史和连续计算状态。

<!-- source-family:SF-2026-ARXIV-2605-05602 -->

## 将历史压入状态：先定义读写，再讨论容量

完整 Attention 把各位置的 K/V 保留下来，当前 query 再决定读取哪些历史；这让精确回读合理，却让状态随长度增长。另一种选择是在 token 到达时就合并信息。固定维状态省去逐条历史，代价是未来 query 只能消费已压缩的结果，不能要求恢复任意被覆盖的细节。

压缩时已经知道什么，比最终任务名称更重要。若完整源状态 x 已可见、未来任务来自已知有限线性算子族 T_u，只在形成保留状态前收到至多 K 种 advice，具体任务 u 要稍后才揭示，那么每条 advice 必须保留其任务集合的共同充分状态。将该集合的算子堆叠为 T_C，连续编码与连续解码、单位球上的最坏情形精确恢复所需最小坐标数是 p*(K)=min_{至多 K 个任务分组} max_C rank(T_C)。决定容量的是同组任务的联合行空间，而非单个任务的秩或任务数量；只有共享核心外的私有子空间互为直和且等维时，才有对应的简洁闭式容量界。它明确展示“先得到有限任务线索”与“压完后面对任意未知 query”是不同约束，不能把前者的低维结论移给后者。

这里计算的是连续实坐标，不是有限精度 bit、learnability 或实际 KV 占用。一般近似恢复只得到以堆叠算子的截断奇异值及任务组大小限定的上下界，最优 advice 分组本身又是强 NP-hard；论文的 attention 例子固定 keys 和有限未来 query/block 家族，未证明真实语言模型的自由 continuation 可按同样比例压缩。构造分组、估计任务算子、维护 advice 身份和重新验收都增加成本；线索不可靠、未来任务越界或要求 provenance/任意精确回读时，完整 KV 或外部可治理历史仍合理。工程实现应另核精度误差、查询覆盖与更新成本，不把该理论存在性当成在线淘汰算法。 [必要机制与反证](https://arxiv.org/html/2609.21523v1)。<!-- source-family:SF-2026-ARXIV-2609-21523 -->

可见状态有限，还没有说明训练时需要保留多深的依赖图。一个有损分支先在句内做 causal Attention，再从句末读出一个向量，后续句通过 cross-attention 读取滚动保留的若干句向量。这样把过去 token 的可寻址历史换成语义摘要，推理时可见窗口可以固定；但若 memory write 不 detach，后续 loss 会沿读取、写入及先前表示的祖先继续反传。窗口里只剩有限个向量，并不意味着这些向量背后的训练 graph 也有限，或任意旧事实仍能精确回读。

因此 visible memory window、training stream/reset boundary 与 gradient credit horizon 要分别选择。Detach 可切断祖先、减少反传工作，却使后续任务无法再训练产生早期摘要的路径；按 stream reset 或逐步增加训练流长则控制另一种信用分配边界，不是免费删除 activation。[Thought Gestalt 的必要机制与消融](https://arxiv.org/html/2512.25026v1)只在 WikiText-103、至多50M训练tokens及约85M非embedding参数的受限模型上支持这种质量—训练成本取舍，句边界、packing及其余设计仍参与结果。它不证明工业规模推理更快、无限记忆或解决反向关系推理。需要逐token provenance、任意精确回读或信用跨度难以验收时，完整KV、显式历史或detach/reset较短的训练路径仍合理；运行状态与训练图须各自测量。<!-- source-family:SF-2026-ARXIV-2512-25026 -->

先看最简单的可核对桥梁。令 q、k、v 为列向量，选择有限维非负特征映射 phi，使相似度采用 `phi(q)^T phi(k)`，则因果线性 Attention 可写为：

```text
S_0 = 0, z_0 = 0
S_t = S_(t-1) + v_t phi(k_t)^T       S_t: [d_v, r]
z_t = z_(t-1) + phi(k_t)              z_t: [r]
o_t = S_t phi(q_t) / (z_t^T phi(q_t))
```

展开 S、z 后，仍是对过去 value 的归一化加权和，但无需逐项重读 K/V。分母须非零，数值实现还要处理小分母；有限维特征核一般不是 softmax 指数核的精确替身。固定 r、d_v 时单步状态与更新成本不随历史长度增长，长序列的总计算和训练 activation 却没有消失。这里的线性指长度复杂度；投影、归一化和整层网络并不因此都成为线性函数。

有限状态也可先定义一组可学习 prototype 通道，让每个到达 token 对通道产生归一化写入权重，再由各通道累积过去 value 及相应 mass、用不同衰减尺度维护因果 EMA；当前 token 先读取截至上一位置的通道摘要，再将自身写入供后续读取，而非逐项历史 KV。这里 prototype 提供固定数量的读写坐标，不等于发现了独立人类概念；past-only 边界、衰减、mass normalization 和 reset 须作为同一状态接口，不能用未来 token 更新当前读取。它是重新选择历史 factorization 的模型分支，不是原 softmax 的精确缓存压缩。<!-- source-family:SF-2026-ARXIV-2602-11852 -->

通道数固定可使历史状态不随长度增长，却把细节、写入冲突和长程召回转为容量问题，训练 graph 与投影/归一化工作也未消失。[ProtoT 的受限小模型对照](https://arxiv.org/html/2602.11852v1)中，更长 context 的 perplexity 可反退，短 context 训练吞吐亦低于 Transformer；单 H100 长 context 推理的局部交叉点不能代替全训练或服务 SLO，可命名 prototype 更不认证内部推理 faithfulness。EMA 尺度、低 mass 或任务回归时，完整 KV、有限 kernel summary 与已有 SSM/hybrid 继续共存，应联验任务质量、真实状态费用和端到端执行，而非因长度复杂度或解释性标签默认替换。<!-- source-family:SF-2026-ARXIV-2602-11852 -->

固定状态也可以只接管远历史，而不是替换全部精细访问。视频的 chunk 内及相邻边界对运动连续性敏感，一条受限混合分支在局部和重叠区域保留 softmax，在更早历史用可学习 kernel summary，并对两部分共同归一化；重叠 token 必须从远历史集合排除，不能计算两次。因果边界按 chunk 而非每个空间 token 定义，所以 chunk 内双向访问不等于读取未来 chunk。这里购买的是不同距离的表示精度分配，不是原 softmax 的精确压缩。

已有双向 teacher 也不能直接换上因果 summary 就保持行为。可先固定原 block，只学习 query/key feature map 去匹配 teacher activation，再以全模型目标修复局部适配留下的跨 chunk 偏差；后一步增加训练费用，并让这条路径区别于单纯 runtime cache 优化。ReHyAt 的视频受限对照支持这一适配分支，但递归公式把全部远历史重复加入累计状态，字面上不足以证明与并行形式等价；也仍保留部分 full-attention block，不能据局部状态定长宣布全模型无限时长定内存。物理控制与人偏好并非全面改善，mobile block 时间也不等端到端生成 SLO。精确回读、适配质量或递归一致性不满足时，原 full attention、局部窗口及直接训练的 recurrent 路径继续共存。<!-- source-family:SF-2026-ARXIV-2601-04342 -->

### SSM：把累加器推广为有动态的状态

纯累加不区分新旧信息。结构化 State Space Model 为旧状态增加演化规则；以一个输入通道 u_t、N 维状态 h_t、零初态说明：

```text
h_t = A_bar h_(t-1) + B_bar u_t
y_t = C h_t
y_t = sum_(i=1..t) C A_bar^(t-i) B_bar u_i
```

当 A_bar、B_bar、C 跨位置不变时，展开式是只依赖距离的卷积：训练可并行计算整段，逐 token Decode 可用递推。这两种执行方式承载同一算子；实际模型通常约束 A 的结构，避免每步密集 N×N 状态转移。连续时间参数的离散化是构造 A_bar、B_bar 的一种方式，不是所有递推都必须采用的定义。

固定 dynamics 还把“状态能否稳定运行”与“这些 dynamics 能否高效学出”分开。在线数据和更新预算很少时，预设 recurrent basis、只拟合 readout 是合理分支；开放学习 pole 则增加 BPTT、识别和曲率压力。[受限线性分析](https://arxiv.org/html/2602.21454v1)中，两非重合实 pole 即使都远离 unit circle，其无限 impulse-response 平方误差的最优 Hessian 也可在 pole 相近时变得任意病态；forward 稳定不保证 pole-learning 好优化。互异非零 pole/gain、零初态、无噪声及已知可逆输入下的有限识别条件，不能迁成 noisy 神经网络的样本/收敛保证；无线实验的 recurrent-matrix condition number 也不是 loss Hessian。固定 basis 用较简单更新换取表达限制，basis 与任务失配或数据充足时仍应比较 learned transition、输入相关 gate 与显式 Attention，而不是因局部曲率反例宣布所有 pole 都不该学习。<!-- source-family:SF-2026-ARXIV-2602-21454 -->

固定卷积核擅长稳定的距离规律，却难以让某次写入随内容决定“记住还是忽略”。Selective SSM 让步长 Delta、写入 B 和读出 C 依赖当前输入，离散后的转移便随 token 改变；不必把基础 A 也改成逐 token 预测。固定卷积不再适用，但在本层输入已知时，仿射状态更新可组合成 parallel scan，Decode 仍逐步递推。并行 scan、融合与反向重算解决执行问题，不证明模型能保留无限关联。

输入相关Delta规定了可调接口，却没有规定该调哪一层、哪项activation。一个[局部SSM诊断分支](https://arxiv.org/html/2602.22719v1)先以token-weighted activation的entropy/敏感性定位，再用逐项消融筛Delta-sensitive分量，最后在固定调整人口上搜索scalar gain；几何指标只提假设，不能替代消融，也不把未给完整basis的“subspace”直接实现成投影。有限Mamba-130M/Pile调整中，所选层在一项IFEval对照只维持baseline，随机或high-variance选择反退，其他增益不授所有steering都有效。训练另一种多timescale/gate/sparse-attention架构是不同bundle，不能借它给局部gain归因；其约2.8倍per-token/1.5倍净计算与每层参数成本也不支持“256参数即可忽略”的统一口径。诊断、消融和gain搜索均付费，完整hardware/dtype/SLO未披露；目标人口变化或质量下降时关闭额外gain，保留原selective recurrence或显式Attention，不以entropy降低认证无限记忆。<!-- source-family:SF-2026-ARXIV-2602-22719 -->

固定状态的容量还取决于内部耦合，而不只是维度大小。对角转移便于 scan，却限制状态间混合；一种替代分支让每个通道的多阶历史组成 companion state，再在小块内使用稠密 channel mixing。前者增加时间阶数，后者增加通道耦合，两者不能混称为更大的同一种记忆。[结构化递推的受限证据](https://arxiv.org/html/2602.12021v1)还把稳定控制落实到联合的输入与状态权重：将一行全部 recurrent 系数和 input gate 的绝对值和限制在 1 以内，零初态且输入有界时，状态的无穷范数不超过输入的 supremum；非零初态则取初始状态范数与输入 supremum 的最大值。仅检查每个时刻转移矩阵的特征值，不能替代时变乘积的这个条件；该前向有界性也不证明梯度不消失或渐近收敛。

更强的状态耦合会改变执行合同：块大小为 m 的稠密 transition 在 scan 合并时引入 m³ 级矩阵运算，扩大多阶 state 也增加 hidden/state 预算。作者的较大 block 存在质量反退，训练 kernel 的收益还依赖形状与硬件调优；不能由 parallel scan 可用推出任意块大小都更快、更准确。需要更强混合但可承担状态和 scan 成本时才考虑这个分支；质量、预算或执行收益不足时，保留对角/更小块递推或显式 Attention，而不是只按状态维数宣称长程容量。<!-- source-family:SF-2026-ARXIV-2602-12021 -->

历史压缩与关联访问也可以保存为两个不同状态：temporal SSM总结近期输入，再由它提出write/query address、value与gate；另一个polynomial-basis bank表示地址上的函数，按当前预测残差沿该地址的basis向量更新，读取则计算query的basis内积。这样相近地址的干扰由显式reproducing kernel描述，而不是假设有限state记录完整token archive。[受限关联记忆实验](https://arxiv.org/html/2602.21340v1)只展示小规模recall与地址图；write gate和epsilon令更新不必严格插值成功，basis截断、碰撞、额外bank与求值/训练都有成本。需要精确访问或容量失配时，保留显式Attention/KV，不由可解释地址图推导foundation-LM吞吐或无限记忆。<!-- source-family:SF-2026-ARXIV-2602-21340 -->

### 从累加到定向编辑：写入、擦除与训练并行

状态递推确定以后，还需要决定每次写入怎样处理旧关联。普通 linear attention 可以把历史压缩进固定大小的矩阵状态 `S_t`，却会让不同 key-value association 在有限维度中碰撞；统一 decay 能快速遗忘，但会同时衰减所有记忆；纯 delta rule 可以沿当前 key 定向改写旧 association，却不擅长在 context switch 时整体清空无关状态。Gated DeltaNet 将两种控制组合为：

```text
S_t = S_(t-1) [ alpha_t (I - beta_t k_t k_t^T) ]
      + beta_t v_t k_t^T
o_t = S_t q_t
```

`alpha_t` 控制全局 state decay，`beta_t` 与 delta term 控制当前 key 方向的定向替换。它把显式的 `T` 个历史 KV 压缩为 recurrent state，并通过 chunkwise parallel form 让训练仍可使用大块矩阵计算；交换条件是 state capacity、association collision、顺序依赖和专用 kernel。论文自身仍把 Gated DeltaNet 与 sliding-window attention 组成 hybrid，说明 fixed-state recall 与显式局部 token access 是互补关系，而不是线性状态已经无条件替代 softmax Attention。

旧状态与新写入的比例也可以由归一化质量决定，而不只由自由预测的 gate 决定。以 chunk 为单位，对每个 key feature channel 沿时间维累加 `exp(K)` 得到当前质量 `w_s`，再维护 `z_s=z_(s−1)+w_s`；旧矩阵状态乘逐 channel 的 `z_(s−1)/z_s`，当前 prediction-error 写入乘 `w_s/z_s`。这里 key 的局部特征以 `w_s` 归一，query 则沿 feature 维作 softmax，两者不能交换为同一种逐 token 归一化。这给 delta update 增加了历史质量的相对权重，但没有新增可独立寻址的无限槽位。与两个相邻 chunk 的显式 softmax K/V 共存时，先从该近窗之前的远状态读取，再把即将离开近窗的 chunk 写入 memory，使近窗与远 state 不把相同历史重复计入；这是读写与可见性合同，不是保留全部历史的无损证明。<!-- source-family:SF-2026-ARXIV-2601-06463 -->

质量比仍会稀释旧关联，压缩矩阵仍有碰撞；额外 `z`、query/key 特征、memory 更新和两个 chunk 的 K/V 都需计费。[Gecko 的受限方法与评价](https://arxiv.org/html/2601.06463v1#S3)以 7B、2T tokens、32K 训练与两 chunk 近窗支持这条分工，却同时改变多个组件，不能从 bundle 收益推每个 update 的唯一因果或同总算力。4M-token books 的 PPL 下降不等于 4M 精确检索，passkey 与 essay retrieval 只测试更短的受限范围；短任务 MMLU/ARC-e 对 Megalodon 也有退步。未披露完整端到端 precision、并发与 SLO 时，连续 chunk 或通信重叠不能认证 Serving 加速。质量稀释、数值或任务支持不足时，原受测 GDN/gated update、显式历史与外部 retrieval 继续成立；这里不补用原文有歧义的 EMA bias-correction 式来保证状态或能力稳定。<!-- source-family:SF-2026-ARXIV-2601-06463 -->

若再把定向更新的 `beta_t` 从标量改为逐通道向量，问题不只是让每个维度拥有不同强度，还要让训练侧保住原来的 chunk 并行代数。天真地只在左侧乘 `Diag(beta_t)`，外积仍是 rank-one，却不再是原先两侧同向的对称 `uu^T` 更新，不能直接继承该 generalized-Householder/WY lowering。一个受限折中是以 `sqrt(beta_t)` 同时缩放 key 与写入 value：用对称的 key 外积保留原 transition 的可并行结构，再让 key/value 的独立缩放分别承担擦除与写入控制。这与后文 GDN-2 的 erase/write 分权是相邻设计选择，不表示两者有必然继承关系，也不等于在模型训练中实际运行了 Adam 式二阶优化。<!-- source-family:SF-2026-ARXIV-2604-19021 -->

这种代数兼容性是以更新形状受约束、额外投影/gate 与 kernel 实现成本换来的，不会把有损矩阵状态变成精确 KV。作者的 340M/1.3B、有限训练与长文任务可以检验这个操作点，却不是所有指标胜出：1.3B 的单独向量 `beta` 在 LongBench 为 16.0，低于 KDA 的 16.4；另一变体的语言建模均值也有退步。H800/BF16 上的固定长度与 batch prefill 对照不能推出任意部署的吞吐或尾延迟。旧标量 gate、已有 KDA kernel，以及需要逐字回读的 Attention 因而继续按成本和任务共存。

Gated DeltaNet-2 继续细分这个 update contract：channel-wise decay 负责背景遗忘，erase gate `b_t` 决定沿当前 key 清除哪些旧内容，write gate `w_t` 决定提交哪些新 value channels。原 Gated DeltaNet 用同一个标量 update gate 耦合定向擦除与写入，因而“需要纠正旧关联但只少量写入”和“保留旧关联但大量写入”不能独立表达。解耦获得更细的 memory editing，自身代价是更多 gate state、反向与 kernel 复杂度；作者的 1.3B/100B-token 实验只能作为该 recipe 的受限证据，不能证明它普遍优于 softmax 或其他 recurrent architectures。

但把 erase 与 write 分开仍不保证所有已读信息都可编辑。若 fast-weight update 只能沿当前 key 的方向修改状态，未来 query 仍可能从与该 key 正交的子空间读到旧干扰；写入规则的方向因此也定义了“可纠正子空间”。一种受限扩展是从 query 派生额外 erase direction，再与原有 key-directed delta 共同更新。它增加了可编辑性，却同时增加 gate、方向估计与训练稳定性成本；短上下文、干扰很弱或附加方向收益不足时，原有 key-gated update 更简单。`arXiv:2608.13668v1` 只在 340M 模型、15B training tokens 和作者的合成 retrieval/语言任务上支持该机制，部分消融并不显著，不能把约两倍 usable context 外推为通用结论。

<!-- source-family:SF-2026-ARXIV-2608-13668 -->

这种思想与 LSTM 共享“有限状态需要学习保留和遗忘”的祖先，但 state contract 不同。LSTM 主要维护向量 cell state，并用 input/forget/output gates 做逐维递归更新；DeltaNet 一类机制维护矩阵 fast-weight state，用 Query 读取、用 key-value association 与 prediction error 定向改写。前者更像更新当前序列摘要，后者显式暴露内容寻址的关联结构。两者都把历史压进固定状态，都会碰撞、覆盖和遗忘；Gated DeltaNet 的 chunkwise parallel algorithm 改善的是训练执行路径，不会把有损状态变成完整 token archive。

仿射 scan 的并行条件还允许另一种写入折中。若非线性更新必须读取尚未算出的 `S_(t-1)k_t`，每个 transition 便依赖中间 state；可先用仅依赖已知 input 的短卷积生成 local proxy，再在该 proxy 上迭代形成非线性 residual 分量，将多个 outer products 注入写入项 B，同时保持 A/B 不消费中间 recurrent state。这里 state-independent 是训练侧可预先构造 transition 的接口条件，不是无 input 条件或没有历史；多分量注入的 rank 至多为 L，只有独立方向才达到上界，residual subtraction 也不自动是正交化。<!-- source-family:SF-2026-ARXIV-2602-10796 -->

这种分支用局部表示与更多 projection/refinement 换写入表达力，却让 local proxy 的偏差成为新压力。只有真实 dynamics 符合所声明 fading memory、proxy 捕获近窗贡献且尾项有界时，截窗误差界才成立；forget operator 非扩张且某些特征值等于1，并不能单独推出严格衰减或普遍对数累积误差。[受限机制实验](https://arxiv.org/html/2602.10796v1)的 toy/recommendation 与单卡小模型 kernel 结果不认证基础LLM质量、端到端训练加速或生产SLO。长距必要信息无法由 proxy 保存、额外写入成本不划算或质量退化时，保留原 delta/GDN 的有损矩阵状态，或增加显式局部 Attention、检索与完整 KV 路径，而不是把多分量写入当作无限精确记忆。

#### 非扩张的状态转移也可以包含旋转

编辑方向之外，transition还能表达怎样的跨步运动？正的channel-wise decay便于遗忘，但即使它与delta update不交换、乘积不对称，也不自动产生复特征值。以列状态写 `H_t=A_t H_(t-1)+B_t`，令 `A_t=(I−β_t k_t k_t^T)Diag(α_t)`；单位key、`β_t∈[0,2]`和各`α_t∈[-1,1]`使齐次转移的算子范数不超过1。允许不同channel取相反符号，再与`β=2`的Householder反射组合，可在实数状态中实现二维旋转，而非只改变整体衰减或符号。这给固定矩阵状态增加周期与非交换组合的表示分支，不需要把每个元素换成复数，也不等同新增momentum state。<!-- source-family:SF-2026-ARXIV-2609-24797 -->

非扩张只约束`A_t`传播已有状态的方式，不能在持续forcing `B_t`下直接保证总状态有界，更不能由“存在正确参数”推导训练一定找到它。CKDA的[§3–6/Theorem3–5](https://arxiv.org/html/2609.24797v1)分别给出有限群的构造能力，以及在non-expansive、每head有限可达状态等前提下单层不能tracking `S5`的边界；`A5`构造不等于随机初始化就能学会。通用weighted-automata扩展还需要`β>2`和精确代数/相应精度条件，已经离开上述非扩张范围，不能拿来为BF16无限长度正确性背书。

signed gate也增加符号前缀状态与kernel接口成本；实际实现用累计sign变换把读取与状态还原接回原chunk路径，必须验证scan、最终state和梯度的一致性。作者1.3B/100B-token语言建模结果与bounded KDA接近，周期任务仍有GRU更强的反例，hybrid Attention配方又改变了读取能力，不能把其收益全归因于旋转。需要明确遗忘、已有kernel更成熟或旋转分支未学稳时，正gate与标量delta继续成立；需要精确历史回读时仍保留Attention/外部检索。

还可以把几何约束放到状态本身，而不只限制转移矩阵。给定酉群的闭 Lie 子群 G、初始 `H_0∈G` 与切空间更新 `U_t∈Lie(G)`，精确 `H_(t+1)=H_t Exp(U_t)` 保持状态在 G 中；用群内 prototype 与 `Re tr(H* P_v)` 读出，是另一种表示/预测合同。[受限群状态分支](https://arxiv.org/html/2602.18417v1#S4)的 Attention 先聚合矩阵，再把相对更新投影到切空间并经 Exp 返回，不能说加权平均本身仍在群中，也不能把这与向量状态上的非扩张线性转移混为一谈。闭包不证明完整梯度、目标优化或任务质量稳定，有限精度与近似 Exp 的闭包偏差仍需检查；矩阵状态、指数映射、prototype 读出和切空间混合都增加成本。现有实验仅 O(d) 的小型字符 LM、单 seed 和参数近匹配，不验证全部子群、等计算预算或基础 LLM。表示限制过强、数值漂移或执行成本不合适时，保留普通向量/矩阵 recurrence、已验收的正交转移及显式历史，不从群内有界状态批准无界精确记忆。<!-- source-family:SF-2026-ARXIV-2602-18417 -->

#### 写入几何与时间惯性是不同的扩展方向

固定矩阵状态的写入还可区分“当前预测误差多大”和“这个 key 在历史中与哪些方向高度相关”。在线 ridge 分支维护 key Gram 矩阵及其逆；在声明的初始化与可逆条件下，读取侧的预条件可等价搬到 key 的写入侧，并用递推更新保留相同状态关系。它不恢复被压掉的全部历史，而是让重复或相关 key 的几何影响下一次定向写入。<!-- source-family:SF-2026-ARXIV-2604-21100 -->

精确 inverse 带来顺序依赖、额外统计和数值成本；若以对角二阶矩及前缀统计换取 chunk 执行，就不能再声称精确两端等价。decay、gain 与 log-centering 等训练配方也不是全局稳定性定理。340M/1B 受限实验有额外预条件成本及若干任务退步，NIAH 改善不能脱离 recipe 宣称普适长文收益。统计代价不合算时仍保留普通 delta/gated update，需要逐字追溯时回到显式 Attention 或检索。后面讨论的更高阶状态解决的是表示多元关系的容量问题，并不自动消除这条写入几何的执行成本。

一阶 delta update 只利用当前写入误差，控制简单且便于 recurrent decode；当连续更新具有可利用的方向惯性时，二阶
momentum state 可以保留前一步更新趋势，并通过 correction term 减少局部振荡。这个分支的关键不是多加一个公式，而是
训练与推理必须拥有同一 recurrence：训练侧的 chunk-parallel 重排、反向重建与 decode 侧的逐 token state transition
必须代数一致，momentum state、correction value 和稳定性条件也都进入 checkpoint identity。

二阶状态以额外 state、activation、反向计算和专用 kernel 换取更长的可用依赖；错误 momentum 会累积过期方向，且公开
证据尚未覆盖 7B 以上模型或 tensor-parallel runtime。普通 delta/gated recurrence 在短上下文、状态预算紧或 kernel 成熟度
优先时仍更合适；需要精确回读时仍应保留局部 softmax 或外部 retrieval。现有 400M/1.3B 实验只支持所测语言建模、
retrieval 与 needle workload，不能把吞吐或质量收益外推到大模型生产 Serving。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05838 -->

### Context switch 与重复表述暴露固定状态的真实边界

同一序列从问题 A 切到无关问题 B 时，recurrent state 不会自动变成两个隔离 namespace。理想情况是边界 token 触发 decay/erase，新 Query 不命中旧 association，新写入逐步接管状态；但这些都是训练得到的软行为，不保证彻底清空或未来可恢复。安全隔离必须由 runtime 在独立请求、用户和 session 之间分配或 reset state，不能依赖模型 gate 猜测边界。

相同语义的不同表述也可能生成不同 keys，造成重复写入与 state churn。Delta rule 在当前 state 已能沿该 key 预测目标 value 时只写 prediction error，可以减小重复更新；它却不保证 paraphrases 落到同一 key，也不能避免相近 associations 在固定矩阵中干扰。Gated DeltaNet-2 的独立 erase/write gates 增加编辑自由度，但 gate 仍需计算，也不是语义去重器或 hard skip scheduler。

因此它把 full Attention“保存并反复读取显式历史”的代价，转换为“持续维护有损摘要”的代价。局部 softmax Attention、recurrent state 与外部 retrieval 分别保留精确近邻、压缩工作记忆和可恢复证据；是否组成 hybrid，应由目标任务的 context switch、精确回看、延迟和 state capacity 一起决定。

“可以遗忘什么”也不能只由 state rank 或重构误差回答。若两个内部状态对声明的所有未来测试给出相同条件预测，它们才在这些测试下属于同一 predictive fiber；纠错器可压缩同一 fiber 内的冗余方向，却不能精确抹掉区分未来的方向。这为 recurrent state 的数值稳定与语义保持划出不同责任：表示 owner 可提议收缩，独立的 future-probe audit 决定哪些差异在指定测试/区域内确实可忽略。有限 probe 只给受限语义保证；连续可区分状态也不能承诺在有限维空间对任意正半径扰动都精确恢复。测试覆盖不足、环境转移变化或需要逐字追溯时，应保留显式历史或外部检索，而非把低维状态称为“无损记忆”。<!-- semantic-body-binding:SF-2026-ARXIV-2609-23366 -->

### Fixed-state Recall 要分解 Transition、Convolution 与 Interference

观察到模型使用 memory gate，也不等于它已学会远程检索。一种 segment memory 在写入当前段之前先读取旧状态，再以 head-wise `α` 混合压缩检索与局部 Attention；可检查 `α`、层间分布和输出是否变化，却不能仅凭 gate 非零把收益归因于可用的远期证据。训练的 padded sequence 长度同样不是有效依赖支持：如果真实文档大多较短，模型可能反复更新状态，却很少遇到必须从旧段精确取回信息的监督。

先读后写还需要说明数值稳定操作属于哪一个时间点。若 memory 是在线学习的非线性 fast weights，刚写入便把权重范数拉回初始尺度，可能在下一次读取之前改变新学到的映射。一条[受限实现分支](https://arxiv.org/html/2602.13680v1)把顺序改为：当前 chunk 先从旧的、尚未再归一化的 fast weights 读取，再沿输入维度按初始权重范数归一化 memory 权重，随后用当前 chunk 更新。归一化的对象是 memory network 的权重，不是 readout；它也不同于 Q/K 的 RMSNorm 或输出 gate。这样将“让刚写入的状态先被读取一次”和“为下一次写入控制尺度”分开，但不证明状态更新无损，也不能把非线性 memory 的读写直接搬成普通 affine scan。<!-- source-family:SF-2026-ARXIV-2602-13680 -->

这条时序分支与局部 SWA 共存，原 SWA 和 channel mixer 冻结，只训练新增 memory 的 meta-parameters；迁移收益仍依赖 distillation 数据和训练预算，不是给任意模型免费追加长期记忆。Qwen3 0.6B/1.7B 的有限长文评价存在部分召回退步，固定状态的 FLOPs/cache 分析也不是实测 request SLO。原文 momentum 式的左右同下标尚不足以核实实际递推实现，因此这里只采用正文与 Fig.2 对应的读、权重归一化、写入顺序，不补造梯度 clipping 的执行次序。质量或稳定性未通过时，继续保留显式历史、受测 SWA 窗口和外部检索，而非由一次读取或 gate 使用认证远期证据可用。<!-- source-family:SF-2026-ARXIV-2602-13680 -->

[Infini-Attention 的小规模预训练反证](https://arxiv.org/html/2512.23862v1)中，300M 模型的 FineWeb 文档中位长度为418，baseline 与 memory 分支还使用不同学习率，因此一般任务或 gate 统计不能独立证明压缩记忆的因果收益。needle 微调可以改善部分位置，但超过训练支持的长度和许多插入深度仍失败；一个位置的提升不能变成全位置召回保证。应分别验收真实依赖距离、重复压缩、插入位置及训练配方，而不把固定 state 或 padded length 当作能力。如果任务要求精确回读或长距支持不足，保留显式历史、受测窗口与外部检索；任务定向微调也要单独计预算，不能称为结构本身免费的无限上下文。<!-- source-family:SF-2026-ARXIV-2512-23862 -->

不同 recurrent/SSM 架构在 associative recall 上的差异，不能只归因“状态容量”。Matched-state 评价应分开 convolution/readout、state transition、写入干扰和 curriculum；只有这样才能判断瓶颈来自无法寻址、旧信息覆盖还是训练没有迫使模型使用 recurrence。<!-- source-family:SF-2026-ARXIV-2609-16183 -->

Gating 可以抑制短上下文 memorization shortcut，迫使模型学习跨距 retrieval，却只是受控任务中的必要条件候选，不是所有 SSM 泛化的充分保证。真实语言 workload 或长距干扰不匹配时，仍需显式 Attention/RAG 或更大状态。<!-- source-family:SF-2026-ARXIV-2609-16540 -->

### 固定矩阵状态的 Rank 是可寻址关联容量

recurrent matrix memory 用固定大小状态压缩历史，避免 KV 随序列增长；但能同时保存和独立读出的关联受更新矩阵的有效 rank 约束。训练可能逐步招募新的 rank direction，并通过表示几何复用它们，而不是为每条记忆分配独立槽位。于是“state 大小不变”不代表可存关系无限，rank、读写冲突和组合结构才是容量诊断。

提高 rank 会增加状态计算、数值漂移和干扰；受控关联任务中的必要性与干预结果也不能直接给出自然语言记忆容量。rank 饱和、读取冲突或长期质量退化时，应扩大 state、分层/稀疏保存 item，或回退显式 KV/retrieval。<!-- source-family:SF-2026-ARXIV-2609-17594 -->

#### 扩大特征阶数会把长度成本转成维度成本

固定状态的容量也不是只有“向量或矩阵”两个选项。更高阶 tensor state 能保存多元 interaction，并继续用 rank-one update 与 contraction read 维持随序列长度线性推进；它解决的是矩阵 fast-weight 难以区分更复杂组合关系的问题。代价则从序列长度转移到状态阶数：宽度为 `W` 时，朴素状态规模随 `W^o` 增长，训练稳定性、kernel 和 checkpoint 都更难。因而它是 `vector summary → matrix association → higher-order interaction` 的条件分支，不是无限上下文；短序列、精确回读或内存受限时，局部 Attention、普通矩阵状态和外部检索仍更合理。

<!-- source-family:SF-2026-ARXIV-2609-12814 -->

固定状态还可以增加 recurrent feature order 提高表达容量，但这会把随序列长度增长的 KV 成本换成随 head
dimension 快速增长的 state、kernel 与数值成本。二阶 feature 的 state 对 sequence length 可保持固定，却可能近似
随 `d_h³` 增长；若恢复 exponential/softmax-like content addressing，又可能重新引入随长度增长的 KV。

因此演进不是 `softmax → linear → higher-order` 的单向替代，而是三角取舍：精确 token addressing、对长度固定的
state、以及对 feature dimension 可承受的计算/容量。First-order recurrent state 在常数小且压缩可接受时成立；
higher-order state 只在真实 kernel、并发和 checkpoint/migration contract 证明 crossover 后成立；exact Attention 在
provenance、稀有 token retrieval 或成熟 runtime 更重要时继续合理。

除了提高每份矩阵的特征阶数，还可以保留多份局部摘要，再决定怎样组合它们。单个全局累加器最节省状态，却把所有历史压到同一份关联矩阵；一个双向或视觉分块分支把序列分成 M 块，各自保存 key–value summary 和归一化量，再用 learned M×M 系数矩阵为每个 query-block 混合这些摘要，块内仍由 query 与 key 的特征内积区分 token。这里增加的是 block-address 的混合自由度，不是输入每次重新产生系数的动态 content router；普通线性 Attention 本来就有 query 内容依赖，也不能把增加 rank 的条件构造写成恢复所有 softmax 函数。

这种容量分支把单摘要的状态成本换成 O(Md²) 的摘要银行与 O(M²d²) 的跨块混合，另有 O(Nd²) 的局部计算。只有布局使 M 固定或 M² 不超过相应长度预算时，才能沿用随 N 线性的说法；固定小块长、让 M 随 N 增长不是同一成本合同。分块布局、系数与表示训练需要共同校准，增加块数也不保证质量或吞吐单调改善。[MHLA 的受限机制与对照](https://arxiv.org/html/2601.07832v1)支持这一结构选择，不支持这里直接采用其未完整说明的自回归 prefix/mask 与缓存复杂度；NLP 训练人口冲突也不用于质量背书。需要精确逐 token 回读、布局迁移后质量不稳或混合成本抵消收益时，单累加器、局部/完整 Attention 仍各有合理边界。<!-- source-family:SF-2026-ARXIV-2601-07832 -->

### 不只增大静态 State：容量可以随序列渐进解锁

增大 rank 或 feature order 都是在改变可用状态的结构；若压力主要随序列推进才出现，还可以改写容量何时可用，而不要求每一步支付相同预算。

固定 recurrent capacity 在短序列和实现简单性优先时可预测，却迫使模型从第一步就支付完整状态，或在长序列过早饱和。渐进解锁分支让可写 memory capacity 随序列阶段增长，以早期 bottleneck 换后期 retention；controller 必须声明何时扩容、旧状态如何迁移以及不同长度下的训练覆盖。它降低早期成本，却可能损伤早期细节、制造阶段不连续和专用 kernel 需求；短上下文或要求全程无损 recall 时静态容量仍更合理。`arXiv:2608.16844v1` 的 Proteus 结果只覆盖作者模型、长度和任务，不证明任意长上下文都应动态扩容。

<!-- source-family:SF-2026-ARXIV-2608-16844 -->

### 固定维 Register 是增长历史之外的受限状态分支

前面的扩容仍在权衡保留多少历史；另一些生成路径则明确放弃已完成 chunk 的离散历史，只让紧凑连续状态跨边界传递。

显式 token history 最易追溯，却随上下文增长；recurrent/compact state 可以把过去压入固定维向量。对 chunked diffusion generation，一个更严格的版本让离散 chunk 在完成后被清空，只由连续 register 跨 chunk 传递，因此 register update、chunk boundary、auxiliary supervision 与 reset rule 必须共同版本化。<!-- source-family:SF-2026-ARXIV-2609-16372 -->

固定 memory 换来 bounded state，也引入 drift、不可解释和训练监督成本；作者 scratch task 中 full context 在 1024 setting 仍更强。任务需要逐项引用、register 未校准或分布漂移时，应回退显式 history、RAG 或更大可审计窗口。

### 以稀疏 Item 保留例外，并验证状态是否仍可使用

固定 register 接受整段历史只能间接影响未来。如果少量稀有实体不能承受这种压缩，另一种容量分配方式是为它们保留可寻址例外，而不是把整个历史都恢复为逐 token KV。

纯 recurrent state 把历史压成固定向量，容量稳定却难以保留稀有实体；完整 Attention 保留每个 token，检索精细却让计算和 KV 随长度增长。中间分支不按 token 等距保存，而由模型识别 distinct item，仅为少量 item 分配可寻址 cache，并让 recurrent state 承担其余背景。它获得了稀疏召回能力，也引入 item identity 漂移、写入冲突和 cache miss；当历史短或所有 token 都可能关键时，完整 Attention 仍更可靠。

#### 容量诊断不能由结构或静态权重直接推出

保留 item、扩大 rank 或改变 state 形状，描述的仍是可用资源；是否真正保存并读出了信息，还要观察状态在具体输入下的行为。

Selective SSM 的 state 诊断也不能只看训练后静态权重。输入相关 gate 会让同一 mode 在不同样本间迁移重要性；精确的 per-mode output decomposition 可以测量“本次输入实际用了哪些 state”，但它只是 instrumentation，不自动给出安全 pruning 决策。要删除 mode 仍需在目标分布上验证输出、任务质量和 failure slices。

从 depth dynamics 看，selective state update 还可能让不同 token 表示向同一 consensus equilibrium 收敛；这不是“固定状态必然遗忘”的同义改写，而是一个带条件的稳定性问题。受控连续时间分析只在 persistency-of-excitation 等假设下证明局部指数稳定，并在更强正定条件下给出吸引域；输入相关权重改变 principal direction 时，收敛可能被打断。更关键的是 output gate 会衰减这种共识在最终输出中的可见程度，因此 state transition 的收敛范围与输出读取的可观测范围必须分开测量。它提示长上下文评价要同时检查跨层 representation collapse 和输出可区分性，却不证明实际离散 Mamba-2、任意训练分布或任务质量必然发生共识；gate、权重或输入条件不满足时，原有 state-capacity 与任务级 evaluation 仍是主判断。

<!-- source-family:SF-2026-ARXIV-2609-17997 -->

无论保留哪些 mode 或 item，新的 state algebra 只有映射到可实现 scan/kernel 才成为系统机制。phase-controlled delta update 可以改善表示，但 chunk-WY 等 lowering 才决定并行度、数值误差和真实内存流量；kernel benchmark 不证明端到端 LLM 优势。Full Attention、recurrent-only 与 sparse item cache 因而是按 workload 共存的分支。

<!-- source-family:SF-2026-ARXIV-2607-09889 -->
<!-- source-family:SF-2026-ARXIV-2607-11796 -->
<!-- source-family:SF-2026-ARXIV-2607-11897 -->

## 将写入变成学习过程：Test-time Memory 的目标与生命周期

Attention 保存可直接寻址的 token history，线性 RNN/SSM 把历史压入固定大小状态。Test-time
neural memory 提出另一条分支：把 memory 本身做成可在线更新的参数化模块，用当前输入产生
的 prediction error 或 gradient 作为“surprise”信号，再通过 momentum 与 forgetting/
regularization 决定写入和保留。

Titans 是这一分支的具体架构案例；MIRAS 则把 sequence model 拆成四个选择：memory
architecture、attentional bias、retention gate 与 memory learning algorithm。这个抽象的长期
价值在于，它把“长上下文”从选择哪些历史 token 扩展为“谁拥有历史状态、用什么目标写入、
怎样遗忘、怎样更新”。

多份内部 bank 的读取还可以受较慢的 context state 调节：对近期已检索的 proposal context 作有界 EMA，将其汇聚并投影成 bank query 的加性 bias，而不把这个缓冲当作新的事实记录或参数优化器。Context persistence、bank addressing 与 write-back 分属不同接口；对写入证据再作 EMA 也不是累积训练 loss 的梯度。[Miniature Brain 的小型符号实验](https://arxiv.org/html/2603.07217v1)展示受监督的 bank routing 可以明显分化，关联 recall 却仍约5%，因此路由分离必须与实际读出成功分别验收；逐项叠加消融不证明任意组合的必要协同，entropy/检索范数 gate 也不自动拥有 confidence 或 novelty 的真值。额外 bank、context/momentum buffer、监督标签、训练与读取都计费，状态更新次序和 reset 必须另行绑定；context 漂移、覆盖不足或任务回归时，保留简单单 bank、原 Attention/可回放历史与外部检索，不由内部热图宣布记忆能力提升。<!-- source-family:SF-2026-ARXIV-2603-07217 -->

### 先定义写入目标：重建关联还是保留后续行为

先看把写入目标显式化的 test-time training with KV binding：若每步用历史 key/value 定义在线回归
目标并更新 fast weights，在特定假设下其读写可重写为 history-dependent linear Attention。这个等价性解释了
为何它能携带连续计算状态，却不赋予逐事实回读、provenance 或删除语义；当 optimizer、nonlinearity、更新步数
或 binding 假设改变，等价关系也可能失效。普通 KV 在精确 token addressing 时仍合理，外部 Agent Memory 仍由
第77章治理。

写入目标也可以来自已经执行的历史读取，而非直接重建每一对 key/value。一个受限分支保留有界 episodic buffer 处理例外，以连续状态承载背景，再把反复检索得到的输出作为停止梯度的 teacher，训练低秩 semantic adapter 近似这些读取；router 选择何时仍调用 episodic 路径。这样，“是否少检索”与“被省去的读取能否由参数近似”成为两个必须联合验收的问题。[CRAM 的必要方法与反侧](https://arxiv.org/html/2602.12204v1)中用于衡量近似质量的 q 本身仍依赖真实 retrieval output，不能据此宣称部署 gate 无需读取便能免费获知误差。检索次数减少也不保证整体状态可用：局部 dynamics 和 activity 任务发生质量退步，attention reduction 并非端到端时延。buffer/连续状态驻留、teacher 检索、adapter 更新、评分与路由均计费；重复模式不足、分布变化或误差不可校准时，保留真实 episodic 读取、固定路由和原 Attention，而不是把 learned 近似当事实证据。<!-- source-family:SF-2026-ARXIV-2602-12204 -->

历史重建之外，还有以**后续行为**定义压缩目标的分支：保留完整历史 `XY` 的冻结 teacher 先产生后续片段 `Y` 的 hidden-state 目标，移除 `X` 的学生只读 `Y`，通过 LoRA 更新去匹配这些目标，再滚动吸收下一段历史。这与用历史 KV 做在线回归不同：前者训练的是有限后续片段上的行为近似，后者定义的是状态读写关系。[受限实验](https://arxiv.org/html/2604.20915v1)支持这一目标分支，但有限 `Y` 上对齐不证明任意未来的因果效应保持，也不恢复逐 token 证据。<!-- source-family:SF-2026-ARXIV-2604-20915 -->

这种方法以 teacher 前向、学生反传、adapter 更新和状态生命周期换取更短的显式历史。更新后的权重、吸收边界、训练片段与 reset/checkpoint 规则必须一起管理；这是系统的状态隔离要求，不是论文已验证的多租户机制。Llama2-7B/RTX4080SUPER 的作者时延扣除了 Prefill，短上下文反而较慢，同步窗口也非越大越好，因此不能宣称全成本常数或无限容量。需要准确引用、删除审计、域外稳定性，或在线更新成本不划算时，显式 KV、可回放历史与外部检索仍是合理回退。

逐出的 KV 还可以通过已训练的 forward 接口写成动态权重，而不在每个 context 上反传优化：用一组 global query 读取被逐出的 key/value，将所得压缩量加入请求内状态 `S_e` 并归一化，再以 `A S_e B` 产生低秩增量供后续 token 使用。这里训练得到的 query、A/B 与 base checkpoint 是模型资产，沿历史滚动变化的 `S_e` 才是 request state；它不是普通可永久 merge 的固定 LoRA，也不是逐 token 可精确回读的 KV。[原始机制](https://arxiv.org/html/2602.16839v1)的 Qwen 配置描述与官方 config 冲突，本处只采用接口，不采用其精确模型性能或 attention-only 成本为全流程常数。压缩、动态 matmul、状态驻留与训练均有费用；eviction/order、状态版本、request reset 与可回放历史应由 runtime 绑定，这是工程防污染边界，不是作者已验证的租户隔离。压缩失真、身份不明或质量回归时，保留原 KV/full或sliding attention、显式优化及外部检索分支，不把内部动态状态提升成持久事实或授权证据。<!-- source-family:SF-2026-ARXIV-2602-16839 -->

写入控制还可以来自自然语言指令，而不是固定 surprise 或把整份文档一律吸收。先将 document 与“只学习哪些事实、格式或拒答行为”的 instruction 共同编码，把 hidden-state embeddings 写入内部 bank，再由未来 query 读取；训练时同时用当前与旧步骤的正向/排除 probes 约束 write 和 read，测试时仅更新 bank 而不更新 base parameters。这是模型内的可学习读写接口，不是 Ch77 的外部检索索引，也不是每份文档另跑 SGD。[Generalized Neural Memory 的受限实验](https://arxiv.org/html/2602.23201v1)中只训练 reader 的消融丢失 selectivity/format，支持让写入参与目标的选择；但 synthetic CounterFACT 的已知假事实与随机指令只检验行为控制，refusal 或 unchanged probe 不证明隐私删除，整层互换也不识别独立的 instruction 因果变量。<!-- source-family:SF-2026-ARXIV-2602-23201 -->

这种分支支付 probe 训练、每层 bank 驻留与额外读取费用，并需绑定写入边界、覆盖和 reset；bank 的随机 overwrite 与约20步后的 retention 退化不允许无限记忆承诺。RAG/ICL 基线 prompt 在 test-ood 上择优，不能当作完全未触碰的测试集比较；精度、硬件、端到端 SLO 未在必要材料披露。冲突文档或保留目标失效时，应回到显式历史、外部检索或独立可核的写入策略，不把内部 learned state 当事实或授权证据。

### 把可写容量扩展为稀疏 Slots

Test-time memory 也可以沿容量结构继续分叉。Dense fast-weight matrix 容量固定且每次更新触达较大状态；
Product Key Memory 先用两组子 key 的 Cartesian composition 建立大量 slots，再只读取少量 top-k entries，
但传统 PKM 在 inference 时冻结，只保存训练期形成的 slow-weight knowledge。将 key/value slots 在 forward
中按 chunk-local objective 更新，便得到一种 sparse fast-weight memory：

```text
hidden states
→ sparse product-key addressing
→ local write objective updates selected key/value slots
→ gate memory output into token path
→ carry updated fast weights across later chunks
```

这条路线用稀疏访问换取更大可写容量，却新增 slot collapse、竞争写入、顺序依赖、遗忘与实现效率问题。
边际 slot-usage regularization、对同一 slot 的写入聚合和 lookahead target 可以改善作者设置中的寻址与写入，
但不是通用 memory protocol。FwPKM 的长流实验主要支持“反复读取可逐步积累信息”，并不证明一次读取、
开放域事实、并发 session 或真实 Agent personalization 已经成立；其实现吞吐也受未优化 kernel 限制。

这里还要区分两份形状相同但生命周期不同的状态：训练得到的 `M_0` 是 checkpoint 的 parametric initialization，
进入一次 sequence/request 后演化的 `M_t` 才是 runtime mutable state。扩大 slot 数量可以在作者 iso-FLOP 设置中
增加 addressable capacity，却同步增加 HBM footprint；它不意味着每 token compute、memory traffic 或服务容量都
保持不变。Checkpoint restore 只能恢复 `M_0`，session resume 则必须绑定并恢复正确的 `M_t`。

因此 runtime 必须把 fast weights 当作 request/session-owned mutable model state：identity 至少包含 model
revision、initial state、chunk/order、update rule、precision 与 reset/checkpoint boundary。Batch 中无意共享会
造成跨租户污染，失败重试若从错误状态继续也会改变输出。Attention 在短上下文和精确 token provenance 上
仍更可靠，外部 RAG/Agent Memory 在 ACL、delete 与引用要求下仍更可控；sparse fast weights 只补充模型内部
低 FLOPs 持续写入这一分支。

### 写入目标的有效期必须覆盖状态的使用期

Fast-state architecture 还必须与训练 objective 的 credit horizon 对齐。若 state 会跨多个 chunks 被读取，却只用
当前 token 或当前 chunk 的 loss 决定写入，optimizer 会偏好立即有用但长期污染的更新。一个更长 horizon 的分支是：

```text
state before chunk k
→ propose fast-weight update from chunk k
→ consume updated state on later chunks
→ score the next-sequence usage window
→ assign credit to the state transition, then commit or reset
```

这会让训练目标更贴近 state lifetime，却增加 delayed credit、跨 chunk replay、reset boundary 和 online update cost。
同一 sequence 不同 prefix 的 relative reward 也不等于原始 same-prompt GRPO；normalization population、state version
与使用窗口必须写入 objective identity。短状态或写入作用可立即验证时，local loss 仍是更稳定的旧方案。

### 多次读取能否摊薄显式优化的写入成本

另一条分支不是让固定 update rule 直接提交一次写入，而是在每个 context 上显式优化一份临时 memory state：

```text
context evidence + initialized memory state
-> inner-loop write objective
-> several bounded gradient updates
-> frozen optimized state serves one or more reads
-> reset, retain under a lease, or discard
```

这把 write 从普通 forward 的副作用提升为可观测的优化过程。它可能在同一 context 被多次读取时摊薄写入成本，
却新增 inner-step budget、初始状态、optimizer/precision、early stop、tenant isolation 和 retry semantics；第一次读取
的端到端延迟也可能更差。GradMem 的实验性结果只说明这种 WRITE/READ 分离在作者模型与任务中可行，不证明
每个 request 都值得在线训练，也不支持把临时参数直接升级成跨用户长期知识。一次读取、严格 TTFT 或状态难以
隔离时，单次 forward memory、Attention 或外部 RAG 仍更合理；只有预计重复读取、收益可测且 reset/rollback
明确时，显式优化的 context state 才可能跨过 break-even。

这并不是免费的无限上下文。在线参数更新增加 write compute、数值稳定性、污染与 session
reset 问题；压缩后的 memory 也不能提供 Attention 那样逐 token 的精确 provenance。作者在
特定规模和 benchmark 上的结果只证明该设计值得继续研究，不能证明它已经替代 Transformer
或外部 RAG。

### Offline Consolidation 把 Wake-time 与 Sleep-time 分开

<!-- semantic-body-binding:SF-2026-ARXIV-2605-26099:start -->
在线 fast-weight update 适合每个 chunk 都能立即验证的写入，却把额外计算放在请求关键路径上。论文验证的受限机制是在
KV eviction boundary 前，对当前 context 执行多轮 recurrent passes 来更新 SSM fast weights，随后清空 KV，并把额外计算
留在 consolidation phase。把这条机制落到可恢复 runtime 时，还需要进一步冻结 recent context 与当前 fast-state version，
再由质量与一致性 Gate 决定是否原子提交新 fast state；只有提交成功后才能清空对应 KV。后半段是系统设计推论，而不是
论文已经验证的实现：sleep trigger、pass budget、state version、clear/commit 和恢复点必须共同构成 context lifecycle。

这条分支用离线计算换取稳定的 wake-time latency，却新增暂停协调、重复提交、状态分叉和不可恢复丢失风险。受限证据只覆盖作者的 hybrid attention/SSM、合成与数学任务及披露的 sleep schedule，不证明任意上下文都可无损写入 fast weights，也没有验证多租户隔离、迁移或生产 tail SLO。sleep 超时、质量回归或恢复验证失败时，运行时必须保留旧 fast state 与 KV，不提交新状态，并回退 full/sliding attention、普通 recurrent update 或外部检索。<!-- semantic-body-binding:SF-2026-ARXIV-2605-26099:end -->

还必须与第 77 章的 Agent Memory 划清边界：这里的 owner 是模型 forward 过程中的内部自适应
state，通常没有用户授权、来源追踪、跨会话持久化和删除语义；Agent Memory 则是平台管理的
外部 durable state。二者只有 `Principle Reuse`，不能因为都叫 memory 就共享同一治理结论。

### 写入 Admission 与停止读取不能共用一个判断

Recurrent/compressed state 还需要把“是否写入”与“是否停止读取”拆成两个 gate。Unconditional update
能保证每个 chunk 都被消费，却会把无关信息和噪声不断写入；update gate 可以控制 admission，但不能说明
当前 evidence 已经充分。Exit gate 依据任务状态停止扫描，节约后续计算，却会在 exhaustive、多答案或未知
证据位置任务上产生不可恢复的 premature stop。因此 runtime contract 应包含：

```text
chunk identity
→ write / skip decision
→ memory-state version
→ continue / exit decision
→ exhaustive-task bypass or fallback
```

### Recurrent State 的控制信号不能取得 Truth Authority

内部低维 state 可以提出 evidence activation、继续迭代或停止的控制信号，却不能证明当前答案正确或证据已经充分。state detector、更新规则、stop threshold 与模型版本必须共同校准；误判会造成漏读、过早停止或无效循环。<!-- source-family:SF-2026-ARXIV-2609-16055 -->

即使更新方向的局部导数为正，有限 recurrent step 仍可能因 curvature 或 overshoot 变得有害，因此还要把方向与 step magnitude 分开验收。校准域外应回退固定保守步长、显式 history/完整上下文或减少循环，而不是让内部 state 自签完成。<!-- source-family:SF-2026-ARXIV-2609-16665 -->

现有证据限少量 text/VLM 与 looped-transformer family，不证明普通 decoder 或开放域 free-running 的通用停止策略。

下一阶段压力不是继续宣称更长窗口，而是定义写入、遗忘、
reset、checkpoint、migration、isolation 与 provenance 之间可验证的组合关系。

## Hybrid 与迁移：明确两类状态怎样共同承担历史

线性 Attention、SSM 与前面的 delta-rule memory 都把增长历史换成受限状态，但它们的写入、遗忘与读出规则不同，不能仅凭“recurrent”合并成同一种模型。压缩状态负责背景积累，少量完整或局部 Attention 层负责显式读取，便形成 hybrid 的基本分工；完整层保留多远、局部窗口多大，仍决定哪些历史可以直接访问。

这也保留了旧方案的成立条件：逐字引用、稀有关联和未知未来查询依赖完整历史时，显式 Attention 或检索仍合理；稳定流式处理、可压缩背景与长历史预算受限时，固定状态更有吸引力。Hybrid 同时支付状态更新和 KV 管理成本，需在目标长度、干扰和检索任务上验收，不从渐近复杂度直接推断吞吐或质量胜出。

混合也可以发生在同一层的历史表示内部：先以全长 K/V recurrence 将远期信息写入逐位置状态，再只读取稀疏间隔的状态。它缩短的是 Attention 的直接访问集合，不是 recurrence 已经不消费被跳位置；只有先前状态能保留必要信息时，稀疏读才有意义。[RAT+ 的受限分支](https://arxiv.org/html/2602.18196v1#S4)在训练 batch 中同时暴露 dense 与较大 dilation 的读取模式，以免模型在 dense 访问下学会绕过 recurrence；这与按层交错两个算子、或 runtime 直接将 dense checkpoint 稀疏化不同。输出分布变化、recurrence 的初始化/学习及模式训练需共同验收，不能由 recurrence 存在推出所有 dilation 都无损。更稀疏访问有质量退步，sink tokens 也改变可见接口，pattern adaptation 与预训练预算须分开计账；GH200 算子对照或未训练质量的较大模型吞吐不签发服务 SLO。直接历史依赖、训练模式失配或稀疏质量失败时，保留 dense 读取、更小 dilation 与原有显式/递归 hybrid，而不是继续放大跳读间隔。<!-- source-family:SF-2026-ARXIV-2602-18196 -->

MiniMax-01 展示了固定状态与显式寻址的这一折中。Lightning Attention 通过调整乘法顺序和分块执行维护递归
`K^T V` 状态，计算可随序列长度近似线性增长；但论文实验发现 pure linear attention 的
retrieval 较弱，于是每七层 linear block 后保留一层 softmax Attention。这里旧方案仍然
合理：linear path 负责便宜地传播长历史，softmax path 周期性提供内容寻址能力。代价是
两类 layer、两种状态和并行实现同时存在，模型不再拥有单一 Attention contract。

这条混合路线也可以从**训练预算**而非仅从推理 KV 出发。显式 Attention 擅长按内容回读，递归状态擅长顺序累积；“先更新状态，再根据该状态选择历史”需要两种能力组合，而不是简单把更多层换成较便宜算子。在限定深度、精度与复杂度假设下的形式任务及合成 state-based recall 中，混合可表达单一路线难以完成的组合；这不证明自然语言里的每项收益都由该表达性差异造成。

因此架构验收应同时比较固定训练预算的质量与达到同一目标所需的 token/计算，再分解 recurrent 比例、放置、gate 和数值状态。受限 Olmo Hybrid 实验把大部分 sliding-window 层改为 GDN、保留周期性全局 Attention，在约 7B/6T-token 路线上取得数据效率证据，却调整了形状/recipe，部分代码、QA 与 held-out 指标仍退步；合成任务的负特征值收益也不能解释所有语言建模 scaling 差异。较少 token 不直接等于更短 wall-clock：新增状态、反向和 kernel 成本仍须测量。检索精度或已有执行栈更重要时，原 Attention 主线仍成立；只有质量—训练成本—服务状态三者共同受益，才值得替换。[混合架构、受控比较与消融边界](https://arxiv.org/html/2604.03444v1#S5.SS1)

与前面稀疏选择器部分的 NSA、DSA 对照，这三条路线解决的问题并不相同：hybrid linear/softmax 保留两种记忆偏好，NSA 联合设计训练
稀疏与硬件访问，DSA 强调既有模型的 staged migration。最终应比较的是 effective utilization、
Prefill/Decode 两阶段收益、KV traffic 与迁移成本，而不是只比较渐进复杂度。

### Hybrid Attention 还需要按层分配精确访问预算

把 Full Attention 与线性、局部或递归层交错，最初通常被理解为“以少量精确层补回近似层损失的召回能力”。但训练诊断进一步暴露了两种不同职责：高效层不只节省计算，也会改变表示形成与优化路径；真正需要跨越长距离、精确回取历史内容的工作，仍可能主要落在少数 Full Attention 层。于是层比例不能只按 FLOPs 均匀切分，而应同时测量各层对优化稳定性、长程 retrieval 与运行时状态的贡献：

```text
hybrid layer layout
→ representation / optimization path
→ long-range retrieval responsibility
→ per-layer exact-access budget
```

增加 Full Attention 比例能提高精确访问容量，却会恢复成对计算和 KV 流量；一味扩大高效层窗口也可能让这些层重复承担自己并不擅长的 retrieval。作者在若干 hybrid backbones 上的 scaling 与 probing 只支持这种职责分化在其训练合同内出现，不给出跨架构通用比例。短上下文、硬件无法高效执行异构层或任务要求任意位置精确回看时，纯 Full Attention 仍是更清楚的基线。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15378 -->

把所有层统一替换成 recurrent 或 linear state，执行规则最整齐，却隐含“各层对精确 token 访问同样不敏感”的
假设。逐层替换实验可以先测量该假设：若早层在移除 softmax 后质量下降更大、深层更能容忍压缩状态，则运行时
可以让早层保留更大的显式窗口，深层更多使用 recurrent aggregation：

```text
checkpoint + target workload
→ layerwise replacement sensitivity
→ per-layer softmax-window / recurrent-state budget
→ hybrid KV layout and kernel plan
```

这不是“深层一定不需要 Attention”的结构定律，而是一次与 checkpoint、任务、长度和实现绑定的校准结果。
它以更少的 KV 读取换取异构 layer plan、更多 cache identity、校准漂移和 fallback 复杂度；换模型、换 workload
或质量 slice 越界时应重新测量，并回退到更大的 softmax window 或 dense Attention。规则化执行、短 Context、
共享 cache 或校准样本不足时，统一 layer contract 仍更可靠。

<!-- source-family:SF-2026-ARXIV-2607-24788; daily-trace:papers/2026/07/29/README.md -->

层敏感性校准还可以用于选择随后重新训练的布局，而不是直接认证当前权重的转换结果。一个分支先冻结 midtraining 结束时的模型，只学习各层 full/sparse 混合系数，按系数选择稀疏层，再回到 midtraining 开始时的 checkpoint 重新训练所选布局。因此必须分别保存 selection checkpoint、训练起点、placement 与后续训练身份：旧权重即时替换的退步和重训后的结果不是同一个实验，也不能把结束时的层排序当作早期权重已经具备的能力。稀疏层的 sink/local window 不等于其余 full-Attention 层也只有固定窗口；校准与再次训练预算、异构 KV 和 kernel 成本仍要共同承担。任务或长度切片退步时，可扩大精确访问预算或回到已验收的 dense/fixed-hybrid 布局；重训路径与直接部署校准并存，不构成免费转换或普遍无损保证。<!-- source-family:SF-2026-ARXIV-2512-23966 -->

固定 hybrid 布局把校准结果写进单一 checkpoint，便于编译、缓存共享与容量规划；当工作负载在长程精确检索与低成本延续之间变化时，另一条分支是在训练时让**同一模型资产**覆盖多个已指定的 layer mixer 布局，并分别验收它们。这样选择的不再只是部署参数，而是某个已训练、已验证的 placement：共享参数可以复用，各布局的 Attention KV、局部窗口与递归状态却不能混作同一份历史。模型 revision、placement、状态形状、训练覆盖和质量切片必须共同定义可发布的工作点；第49章只接收相应的执行计划，不替模型层证明某布局可靠。<!-- source-family:SF-2026-ARXIV-2604-19877 -->

多布局训练节省为每个工作点重新训练完整模型的代价，却扩大训练搜索、权重驻留、图捕获和验收矩阵。它不意味着请求可以无成本地逐条换布局：已公开实现按单个 preset 服务，切换需要迁移 mixer 权重并重捕执行图；同实例逐请求路由仍是未完成的方向，异构请求还会破坏同布局 batching。质量退步、长距回取失败或运行时容量不足时，应退回已验收的固定 hybrid/full-Attention 布局。作者的质量测试与吞吐测试使用不同执行模式，不能拼成同一生产 SLO 的 Pareto 保证。

### Cross-layer Routing 必须先对齐 Receiver 的表示基底

决定哪些层保留精确访问之后，还可以调整层与层之间怎样交换状态。这是与层比例并存的连接选择，不意味着采用 hybrid 就必须跨层共享；首先要满足的是接收方的表示约定。

跨层复用 recurrent state 能缩短信息路径，但“发送方的 update signal”不一定是“接收方可消费的 state”。尤其
delta/write-error 绑定当前层的 key、value 与 residual basis，直接传给另一层会把不同坐标系误当成同一语义。
更稳妥的分支只路由已经对齐的 value/hidden stream，或先经过初始近似恒等、可逐步学习的 projection：

```text
source-layer state / value stream
→ explicit basis-alignment projection
→ gated cross-layer route
→ receiver-owned recurrent update
```

Projection、route topology 与 gate 都进入 checkpoint identity；额外路径可能放大梯度、形成层间 shortcut 或破坏
kernel 规整性。实验比较还必须固定 optimizer、learning rate、训练 token 与 pure/hybrid stack，不能把训练 recipe
差异归因于 routing。表示基底天然共享或额外路径收益不足时，逐层独立 state 仍是更简单的基线。

[第19章的 depth-wise KV sharing](./19-kv-cache.md#depth-wise-kv-sharing-是-model-contract不是-runtime-eviction)已定义共享映射属于模型合同；这里进一步检查接收层能否消费该表示。同样的约束延伸到跨层 KV mixing：被复用的 K/V 不是“同一 token 的通用缓存”，而是由 source layer、projection、position、precision 与 receiver contract 共同定义的派生状态。若 runtime 只按 token prefix 命中，可能把旧 mixing topology 下的 cache 交给新模型路径。cache key 应绑定跨层连接与投影 revision；配置变化时失效重算。复用能缩短状态路径，却用更复杂的身份、训练耦合和失效规则换取收益。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18486 -->

#### Output gate 不等于跨时间的 Memory gate

跨层 routing 与前面的 memory transition 都可能用 gate 控制信息流，但不能因此与 gated softmax attention 混为同一机制。后者仍先计算标准 SDPA，再用当前 query 产生的 head-specific sigmoid gate 调节该 head output，可抽象为：

```text
h_i = sigmoid(x_i W_g) elementwise SDPA(Q_i, K_<=i, V_<=i)
```

这个 gate 决定“当前 query 要把多少 attention result 写回 residual stream”，并在作者实验中表现出 input-dependent sparsity、较少 attention sink 与更稳定的训练；它没有把历史改写成固定大小 state，也没有取消 dense SDPA 的 pair computation 或 KV Cache。两者的共同点是用输入相关乘法门控制信息流；区别是 Gated DeltaNet 的 gate 属于跨时间 memory transition，gated attention 的 gate 属于当前 token 的 softmax-attention output。前者适合把 sequence-length state 成本压到固定边界并接受 recall trade-off，后者适合保留 exact softmax access、用额外参数与非线性调节输出；需要两类记忆偏好时可以组成 hybrid，而不应仅凭名字互换。

### 共享全局历史与增加计算深度可以分别设计

Local/Global 分工还能改变**加深网络时要保存多少历史**。把整个 full-attention block 循环多次可重用参数，却让每轮都重新付出全局读取与逐层 KV；只缩小窗口又可能失去长程访问。一个条件化架构先让 local-window 或其他高效算子的 Self-Decoder 循环细化表示，再只生成一次全局 KV，由后续 Cross-Decoder 各层共同读取。增加循环次数主要扩大 local compute 与窗口状态，而不使全局 KV 按循环次数再复制；这把“更多计算深度”与“更多完整历史副本”部分解耦。

它不是免费的深度：local state、循环 FLOPs、训练稳定性和一次性全局 KV 的表示瓶颈仍要计入，Cross-Decoder 共享同一历史也限制逐层重写 KV 的自由。短 Context、无需额外循环、或各层确实需要不同全局表示时，普通 Transformer、固定 YOCO 或不循环的 hybrid 仍合理。[受限 YOCO-U 实验](https://arxiv.org/html/2604.01220v1)只支持作者架构、模型与披露的训练/服务配置，不能把较低 KV 直接外推为生产吞吐或 SLO 胜出。模型层在此决定状态形状；第 45 章再管理其物理驻留和身份。<!-- source-family:SF-2026-ARXIV-2604-01220 -->

另一种递归不重复执行整段网络，而发生在同一层的时间轴：过去位置的持久 KV 由该层输出派生；当前位置先以层输入形成临时 KV，计算完输出后才提交未来可读的持久 KV，避免当前 token 在同一步读取自己的循环结果。这给同层历史增加了有效计算路径，却仍为每个历史 token 保存状态，不能当作固定容量的 recurrent summary；训练时同层位置间的依赖和服务时的逐 token 提交也必须按同一状态契约验收。<!-- source-family:SF-2026-ARXIV-2604-21215 -->

这一路线用时间依赖、临时与持久两种 KV 的身份和额外计算换表示能力，和 YOCO-U 的跨层共享并不互相替代。公开受限实验不能证明通用质量或推理 SLO 胜出；顺序依赖与全长 KV 不划算时，普通 Attention、跨层共享或前面的固定状态/稀疏分支仍更合理。模型层定义何时写入、写的是什么，第45章再负责物理驻留与失败恢复。

### 从 Dense Checkpoint 迁移到 Hybrid State Model

从头训练 hybrid attention/RNN 最容易保持架构一致性，却放弃已有 dense checkpoint 的能力资产。受控迁移
可以逐层测量 hidden-state reconstruction error，先替换最可转换的层、保留少量 attention，再通过
distillation 与 long-context continued training 修复：

```text
dense attention checkpoint
→ layer-wise conversion probe
→ retain hard-to-replace attention layers
→ distill converted recurrent layers
→ long-context calibration
```

这条路线获得更小的长期 state，却新增 layer-selection、teacher distribution、GQA/MHA layout、gate、
position rule 和 kernel identity；单层 MSE 也不保证端到端行为保持。原生 dense attention 在精确回读、
迁移数据不足或 runtime kernel 不成熟时继续成立。单 GPU NIAH/吞吐结果只能支持作者转换 recipe，不能证明
任意 Transformer 都可低成本变成 hybrid model。

### 可映射的中间算子可以成为完整替换的迁移桥

若目标是完全替换attention，而不是保留难转层，可以先拟合normalized linear feature算子，再把phi(K)/phi(Q)、V、恒等初始状态转移和normalization state映射到SSM，最后受控解锁conv/gate等动力学并以真实token CE适配。函数匹配发生在中间linear operator上，不是原softmax的精确等价，也不是仍保留原attention block的hybrid。迁移artifact需分开算子匹配、初始化和后续学习；input/output embeddings保持冻结，不应把其余模型finetune写成“所有参数解锁”。

这个桥增加中间拟合、扩展state、kernel适配和能力回归成本，少distillation tokens不证明更低wall-clock。`arXiv:2604.14191v1` 的Attention to Mamba受测Pythia1B/10B OWT tokens、8A100/BF16中，state扩到2048造成scan serialization，作者约12d9h、训练时间大于8×；Lambada32.31低于42.07、BoolQ55.20低于60.82，不能保证全面保留能力或部署长检索质量。函数/能力/执行成本任一验收失败时，原dense checkpoint、保留attention的hybrid与更多迁移数据仍是合理共存路径；替换架构并不替代独立任务评价。

<!-- source-family:SF-2026-ARXIV-2604-14191 -->

### State continuity：历史可访问与计算连续性不是同一问题

RAG、摘要和外部 memory 让已经离开 working context 的历史仍可被重新访问。这条路线合理，
因为原始文档可以保留 provenance、权限与删除语义，系统也能按当前问题选择证据；但每次检索
都要重新判断“过去的什么与现在有关”，无法天然携带模型在连续交互中逐步形成的内部计算
状态。递归模型的固定状态恰好反过来：它可以低成本地延续计算，却是有损压缩，通常不能逐
token 精确回读。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09867:start -->
不断追加显式 token history 最透明，也最容易回放；当在线适应使历史无界增长并重复重算时，可以把一部分跨 step 的算法状态压入 continuous latent context。理论构造表明，Transformer 在受控条件下可以用这种紧凑状态实现 multiplicative-weights 或 tabular Q-learning 式更新；这说明 latent state 能承担计算连续性，不等于模型会自然学到该算法，更不等于它拥有事实真值。内部 state 只拥有计算 proposal，外部 evidence 仍拥有 provenance、权限和可删除的事实 authority。

紧凑状态用固定计算边界换来 state drift、不可解释性和恢复困难；训练分布改变时，旧状态还可能把错误持续带入后续步骤。现有证据限构造性理论与小规模实验，不证明 frontier model、长时间在线学习或生产 SLO 下的稳定收益。需要逐项追溯、强审计或状态校准不足时，应回退显式 history、RAG 或平台管理的可审计 Memory。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09867:end -->

LiveMem 是这一边界的实验性案例。它在 bounded full-Attention KV window 之外增加固定大小的
recurrent state，并在训练和推理中主动执行 context turnover：一旦旧 KV 被释放，后续预测仍
必须依赖持续更新的 side state。这里真正新增的抽象不是“无限保存历史”，而是让两种状态拥有
不同生命周期：active KV 服务当前精确寻址，latent state 在 working context 淘汰后继续承载
有损的历史影响。训练也必须真实移除旧证据，否则模型可以绕过 memory path，离线存在的状态
并不等于它成为 load-bearing state。

这会把模型机制直接带入 Serving contract。Runtime 除了管理 sink 与 active KV pages，还要为
每条 stream 分配、更新、隔离和释放 recurrent state；Prefill chunk 边界、失败重试、迁移、
model revision 与 session reset 都必须与该状态一致。若请求结束后没有释放或跨租户错误复用，
它不只是 cache miss，而会成为状态泄漏或语义污染。固定容量也没有消除 position horizon，
作者在单一模型族和受限 benchmark 上的结果不能证明 arbitrary-token recall 或真正无界推理。

还存在不淘汰历史的派生状态分支：让轻量 consolidator 直接读取 backbone 已有的完整 KV，生成少量 latent embeddings，再经 backbone 把它们转换为追加的 KV，供后续生成读取。它避免为历史另建一套完整 encoder cache，但原历史仍在，追加状态也占用位置、容量与执行预算；因此不能把“复用已有 cache”解释成固定内存或压缩后释放历史。该派生状态应绑定源 KV、模型与 consolidator 版本及触发规则，不能跨会话随意复用。冻结 backbone 参数也不意味着训练时无需经过其计算图：若梯度要穿过 backbone 更新 consolidator，前向与反向执行成本仍存在。

这条分支依赖模型学会使用追加表示，而不只是保存了一个 tensor。用 attention entropy 触发整理时，sink masking、归一化与阈值都需校准；熵下降不是事实正确或“知道自己不知道”的证明。新增 latent 可能放大错误历史，整理过频又会抵消收益，必须同时检查任务质量、原历史与追加状态的总预算。短生成、精确引用、触发不稳或收益无法覆盖执行成本时，继续使用普通 KV 与外部可追溯证据；真正需要淘汰旧历史时，则仍须采用并验证前述有实际 context turnover 的路线。
<!-- source-family:SF-2026-ARXIV-2601-05505 -->

因此长期设计更接近分层而不是替代：

```text
bounded KV                     : 当前窗口内的精确 token addressing
external retrieval / archive   : 可追踪、可删除的历史证据
latent recurrent state         : 有损但持续的计算状态
```

短会话、精确引用或强审计任务仍应优先使用 KV 与外部证据；长期交互且历史影响难以预先检索时，
latent continuity 才可能补足缺口。

### 在固定状态与完整历史之间选择保存粒度

固定 recurrent state 与完整增长 KV 之间还存在可增长的 compressed checkpoint 分支：模型每隔若干步把历史
压成一个 memory slot，保留少量 slots 供后续 recurrent update 读取。更细 checkpoint 提高局部恢复能力，却让
memory size、lookup 和 write cost 随历史增长；更粗 checkpoint 接近固定状态，成本低但信息损失更集中。
这不是“既常数内存又精确回读”，而是把容量旋钮从 token 粒度移动到 checkpoint 粒度。Memory Caching 的实验
支持该中间分支，但没有 production kernel、迁移、租户隔离和端到端 SLO 证据。

另一条分支把远期 KV 压缩为 memory bank，只让近期 working KV 保持高分辨率。它延长可访问 horizon，
却丢失逐 token provenance，并新增 compressed-state schema、gate、refresh 与 model/session identity。外部
RAG 仍适合需要 ACL、删除和精确引用的 evidence；full scan/full KV 在错误代价高、证据必须完备时继续成立。

## 外部工作集：先选择材料，再决定怎样与 Context 交互

内部状态的每种压缩都要承担未来查询可能需要已丢细节的风险。若原始材料可以留在模型之外，就可以把问题改写为“这一次应取回什么”；这不会取消检索错误，只是让历史保存与模型计算不再共享同一容量边界。

RAG、检索、摘要和 memory compression 先选择或压缩信息，再把较小 working set 放入 context。

它们减少模型内部 `T`，却引入另一组失败模式：

- Retrieval recall 不足。
- Chunk 切分破坏语义。
- Ranking 选择错误证据。
- 摘要丢失细节。
- Index freshness 与权限不一致。

Long Context 回答“窗口内能处理多少”，Retrieval 回答“有限窗口该放什么”。二者可以互补，不能简单写成高配版与低配版。

外部状态也不必只保存原文 chunk。另一条受限分支先抽取事实，再把与特定层和模型版本绑定的 residual vector 存入外部库，查询时只重建命中的表示。它把 raw-context archive 压成可选择的派生状态，可能越过单次上下文窗口，却新增 extraction、routing、anchor、模型兼容和组合推理失败；activation vector 不是事实 owner，更不能替代原文证据。需要精确引用、多事实关系或跨模型迁移时，应回退普通 RAG 与可追溯原文。

<!-- source-family:SF-2026-ARXIV-2609-12686 -->

Soft Context Compression 还需要把“压多少”与“怎样解码”分开。固定 ratio 最易实现、batch shape 稳定，
适合信息密度相近的输入；但稠密公式、稀疏日志和自然语言冗余度不同，同一 ratio 会让一部分样本浪费
budget、另一部分丢失关键状态。一种实验性分支先用 density predictor 提议离散 compression level，再由
compressor 生成少量 latent tokens，并绑定能消费这些 tokens 的 decoder/model revision：

```text
raw context + segment boundaries
→ density / budget proposal
→ discrete compression ratio
→ versioned latent working set
→ compatible decoder under a task EvalSpec
```

Density score 是 budget proposal，不是 evidence importance 的 ground truth。Summary-length proxy、短输入训练、
substring scorer 或相关性 ablation 都可能把“容易压缩”与“对任务不重要”混淆；latent tokens 还削弱逐字段
provenance、跨模型可移植性和精确删除。固定 ratio、typed retrieval 或 raw Context 在可审计性、未知 query、
decoder compatibility 与小 workload 中继续成立。Compression artifact 至少绑定 source digest、segment policy、
predictor/compressor/decoder revision、ratio、task slice 与回退入口。

### 从访问 Context 到搜索 Context-interaction Program

当原始 Context 可以保存在外部变量、REPL 或 sandbox 中时，模型不必把全部内容一次塞进窗口，而可以生成程序去 search、slice、aggregate，并在必要时调用子模型。它把“窗口容量”推进为“如何与 Context 交互”的 policy：结构化检索和可分解计算可能受益，但一次错误 query、过早停止或污染的中间状态也会让整条程序失败。

进一步并行生成多条 interaction programs 会提高 coverage，却把瓶颈移到 trajectory selection：

```text
external context + interaction environment
-> K candidate programs and mutable execution states
-> normalized answers / candidate groups
-> trajectory selector
-> accepted answer or abstention
```

Plurality、self-reported confidence、trace length 或其他同源 proxy 可以帮助排序，但不能成为 correctness proof。多数候选可能相关地犯同一个错误，短轨迹可能只是过早停止，自信也可能未校准。系统必须记录 candidate set、program/environment revision、execution state、selection rule、budget 与最终 acceptance evidence；并行 wall-clock 接近单轨迹也不等于总 calls、tokens 或 FLOPs 相同。

因此长期演进是 `capacity -> access/traversal policy -> candidate coverage -> selection -> acceptance`，而不是“递归比长窗口新”或“自反选择淘汰递归”。Direct prompting 在短任务和严格 SLO 下仍成立；typed retrieval 更便宜可审计；summary 适合容忍有损压缩的语义任务；recursive traversal 适合结构化 search/computation；存在确定规则时，独立 executable verifier 仍比同源 uncertainty proxy 更强。

### Mergeable Aggregation State 是 Token History 的有损替代

有些长历史任务并不需要以后逐字回读，而只要求持续维护集合、计数、分组或其他可组合统计。把每个中间值都重新
序列化进 prompt 最容易复用通用模型，却让 context 随历史增长，并把本可并行合并的操作退化成串行 token
处理。另一条路线让模型输出带显式 algebra 的 compact state，再由确定性执行层合并：

```text
history shard → model-derived aggregation state
multiple states → deterministic merge operator
merged state → query-specific finalization
```

这不是无损压缩。它用较小、可合并的状态换掉逐 token provenance 和任意回读能力；正确性还依赖 state schema、
merge 的结合律/交换律、数值范围和模型是否把输入正确映射到该 algebra。集合式 workload、分片并行且允许任务专用
operator 时，它可以位于完整 context 与外部数据库查询之间；需要原文引用、任意 lookup、删除或 ACL 时，保留 raw
history 与外部 authoritative store 仍然合理。模型只负责提出 aggregation state，执行器拥有 merge commit，评估则
必须同时检查局部 state、跨分片 merge 和最终答案，不能只看最终文本碰巧正确。

## 把模型状态交给执行层：长度收益仍须支付资源成本

前面的选择已经确定哪些历史可见、哪些信息被压缩、怎样写入和读取。执行层只能兑现这些语义，不能用分页、迁移或更多设备补回模型从未保留的信息；反过来，较少状态也不能替代通信、kernel 与并发验证。这里沿用[第19章的模型状态接口](./19-kv-cache.md#从模型状态到-runtime-对象)，只说明资源压力如何转移。

### 把序列计算分布到多设备

Ring Attention 将长序列 blocks 分布到多个 devices。每个 device 持有局部 Query block，K/V blocks 沿环传递，在 blockwise attention 中逐步完成全局交互，并尝试让通信与计算重叠。

它扩展单设备可承载长度，但没有让全局 Attention 免费：

- 需要更多设备。
- 引入跨设备 bandwidth 与 latency。
- 需要 block schedule、load balance 与容错。
- 训练与推理的适用方式可能不同。

它把单卡 memory 问题转化为分布式执行问题。

### 减少或分层管理 KV Cache

模型架构可通过 GQA/MQA 减少 `H_kv`，KV quantization 减少 `b`，sliding window 限制保留长度。Runtime 还可以 offload 到 CPU memory 或其他层级。

Offload 用更大容量换取数据传输。若 cache 不能在使用前到达 GPU，Decode 会等待。

ShadowKV 是更具体的研究方案：利用 key cache 的低秩结构、value offload 与稀疏选择，按需重建/检索部分 KV pairs。它依赖模型、选择策略和硬件通路，不能泛化为所有 KV 分层方法的同义词。

#### 压缩表示必须与实际 Decode 路径兼容

缩小 KV 也可能依赖模型参数化本身，而不是把相同张量放到另一层存储。这里沿用[第15章的 head sharing 与 latent 表示](./15-multi-head-attention.md)，只检查它在长上下文下能否保持预期执行路径。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-16310:start -->
MLA 的 post-projection QK RMSNorm 可拆为可吸收到权重的静态部分与逐 token/group 动态标量，从而保留 latent-KV decode path。该变换减少额外状态，却要求数值等价、RoPE 与量化路径共同验证；不满足时继续显式执行 normalization。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-16310:end -->

## 生产评估不能只看最大长度

容量规划应使用真实 prompt/output 分布，并至少测量：

- `TTFT` 随 prompt length 的曲线。
- `TPOT` 随 active context 的曲线。
- 单请求 KV bytes 与可承载并发。
- Prefix reuse、offload 或分布式 Attention 的命中/通信。
- 不同位置和任务切片的 effective utilization。
- 超长请求对短请求 tail latency 的干扰。
- 每个成功任务的 token、GPU 与成本。

厂商或模型卡声明的最大长度只能作为兼容入口，不能代替这些证据。

### 相同 Token Length 仍可能承载不同 Information Load

只按 token 数量、关键信息位置与任务类型切片，在文本的信息密度近似时是合理的：序列越长，模型需要跨越的距离通常越大，Attention、KV 与端到端延迟也随之增长。但固定长度并没有固定推理难度。同样数量的 token 可以只是冗余叙述，也可以同时包含更多实体、关系与相互竞争的事实；后一种输入即使没有扩大窗口，也会让可可靠利用的 effective context 缩小。因此，`max context length` 不是单独的模型能力，`prompt length` 也不是足够的 workload identity。

生产评估需要把 lexical density 或可复现的内容结构作为 EvalSpec 的一个条件，与 token length、关键信息位置、任务、模型版本和解码策略一起冻结：先在长度与位置相同的样本上改变信息密度，再观察检索、组合推理和干扰错误如何变化。这样得到的是 density-conditioned quality/utilization curve，而不是一个脱离输入结构的“可用上下文长度”。调度器仍可用 token 数估算显存和计算，但发布判断不能把资源容量等同于认知利用率。

这条分层会增加数据构造、切片数量和统计成本，而且 lexical density 本身依赖 tokenizer、语言与度量方法；若密度变化同时改变了语义难度，相关性也不能被解释为单一因果。此时应回退到人工定义的任务/内容结构分层，并保留原有长度—位置切片作为共同基线。现有论文证据只说明其披露模型与 benchmark 中“同长度、不同密度”会改变有效上下文，不证明所有模型、语言、硬件、并发或生产 SLO 都遵循同一数值关系。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-06203 -->

### 长上下文能力是联合架构属性

短序列上的训练损失不能单独证明模型已经具备长上下文能力。归一化、位置规则、GQA/MQA 的共享方式、预训练实际见过的长度以及部署窗口共同决定长序列中的数值稳定性和检索路径。早期架构筛选可以用短序列指标缩小范围，但进入长上下文发布前仍需在目标长度、任务与 KV 配置上回归；失败时应保留较短窗口或更稠密注意力作为共存路径。
<!-- source-family: arxiv:2608.10296v1; semantic-body-binding: long-context-readiness-as-joint-architecture-property -->

## 从机制演进到系统设计

从扩大可见窗口出发，位置外推、Prefill 二次复杂度、KV 容量和信息利用率会成为相互制约的压力；具体先触及哪一项，取决于模型、任务与执行资源。因而后续方案不是同一条速度排行榜，而是多条条件分支：稀疏 selector 减少读取，sliding/prefix policy 保留不同类型的历史，recurrent 或 parametric state 把跨段信息迁出显式 token window。

这些机制共同要求 context state 带有位置、可见性、预算、更新规则和 fallback identity。更小的状态换来更低 memory/compute，却会引入 selector drift、中间证据丢失、写入污染和训练—推理可见性不一致。需要完整回看、selector 未校准或状态语义变化时，应回退 dense context、检索或更大 KV；位置扩展本身不能证明模型真正利用了远距离证据。

## 本章在知识树中的位置

```text
Position Encoding
+ Self Attention [B,H,T,T]
+ KV Cache [L,B,H_kv,T,d_h]
-> Long Context constraints
-> model effectiveness + runtime capacity
-> Inference System / RAG / platform policy
```

本章是 Part II 的收束节点。它把第 13、14、15、19 章的机制放进同一个约束问题。第 27、28 章决定模型实际见过的长度和内容分布，第 36、40 章用 Context Parallel 扩展长序列训练；第 43、45、54～56 章再处理在线 Prefill、KV capacity、memory hierarchy 与 SLO。Part VII 的 RAG/Memory 则改变有效 working set，而不是自动扩大模型能力。

沿 Memory 横线，本章首先暴露 sequence length 对 activation 与 KV capacity 的联合压力；第 35、39 章分别处理训练状态的持久化与分片，第 45、47、52、54、55 章则处理在线 KV 的生命周期、placement、tiering、总预算与跨池移动。这是一组 memory-category 分支，不是一条状态格式的继承链。

至此 Part II 已回答“一个文本 token 如何变成答案”。进入训练之前，还需处理一个不能被文本主线顺带解决的边界：图像、视频、音频、environment state 与 action 如何获得带 time、modality 和 provenance 的 representation contract；不同生成范式又怎样定义 mutable state 与 commit。Part III 因而先从第23章进入多模态表示，再沿生成、World Model 到具身行动。Part IV 从第27章“数据”开始，回答这些能力怎样由数据和优化产生。

## 自检问题

1. Accepted length、positional generalization、effective utilization、system capacity 有何区别？
2. Position function 可计算更远位置为什么不等于行为可靠？
3. `T` 翻倍时 dense Attention pairs 与 KV elements 分别增长多少？
4. FlashAttention 为什么没有消除 `T^2` pair FLOPs？
5. Sparse Attention 用什么代价减少连接？
6. Ring Attention 把单设备限制转化成什么问题？
7. GQA/MQA 与 offload 分别改变 KV 公式中的什么？
8. ShadowKV 为什么不能代表所有 cache 分层？
9. RAG 与 Long Context 为什么是互补而非简单替代？
10. 生产容量为什么不能只依据最大 context window？
11. Hybrid linear/softmax、native sparse 与 test-time memory 分别改变了哪一种状态？
12. Gated DeltaNet 的 memory-transition gate 与 gated softmax attention 的 output gate 分别控制什么？
13. Gated DeltaNet-2 为什么要把 erase 与 write 解耦，它没有解决什么？
14. 为什么同一序列的 context switch 不能等同于 runtime 的请求隔离？
15. 固定状态的线性 Attention 为什么既不等于有限维 exact softmax，也不意味着训练内存为常数？
16. LTI SSM 为什么可写成卷积，而输入相关的 selective update 需要不同执行路径？

## 小结

Long Context 不是一个模型参数，而是一组联合约束。位置机制决定远距离关系能否表达，Attention 决定 Prefill 成对计算，KV Cache 决定 Decode 状态容量与带宽，训练与 Evaluation 决定模型能否真正利用信息。

不同方案只移动特定瓶颈：位置扩展、IO 优化、稀疏连接、分布执行、cache 压缩与检索各有不同失败模式。正确决策必须同时看质量、延迟、并发和成本。

## Review notes

- `SF-2026-ARXIV-2603-07217` — Daily `2026-03-11` 补遗漏；[Miniature Brain exact-v1](https://arxiv.org/html/2603.07217v1) §4–11/必要Table1–5、§12–13。2+1+2=5，较慢context read-bias与bank addressing/write-back分责gap深入；EMA检索证据非optimizer gradient，route≠recall、叠加消融非普遍协同，novelty/confidence gate真值不授；buffer/reset次序/监督与额外费用、单bank/原Attention回退近文。review_mar11_continue actual necessary Source、Ch22逐字PRE和root窄锁通过；supplement_20260311 窄写一段，review_mar11_continue 非写入者实际新674段、665–701完整邻接/1176–1187自身注回对必要v1，POST通过，不授DAY；未核artifact或复现。

- `SF-2026-ARXIV-2601-18401` — Daily `2026-01-28` 增量；[Superlinear attention exact-v1](https://arxiv.org/html/2601.18401v1) §2.1–2.4/3.1–3.4/4.1–4.2/4.4–4.5/5。2+2+2=6，具体 long-context routing gap 深入，采用累计 key→covering candidate span family→selected soft gate、N=2 成本平衡/全 KV 与失败；structural non-exclusion 不等于每 query 读全历史，10M 效率不授质量。N>2/log 为 future，§4.5 factor 描述内部不一致故不采精确调参数字。jan28_review 实际必要原源/owner/PRE及完整局部正文/邻接/自身末注POST通过，覆盖条件窄措辞已按其复核修正，不授日级完成；未核 artifact 或复现实验。

- `SF-2026-ARXIV-2601-06463` — Daily `2026-01-14` 增量；[Gecko exact-v1](https://arxiv.org/html/2601.06463v1) §3.3/Eq17–27、S1/Table1与§4，2+1+2=5，chunk质量比与两近chunk/远state不重复的具体差额深入。时间key/feature-query归一、read-before-write、state dilution/碰撞和额外状态成本近文；不授no-forgetting/任意长度准确，4MPPL与更短retrieval分开、MMLU/ARC-e反侧保留。§3.1 Eq12以mu非m作mean bias correction与叙述不一致，未采用或自修完整执行式。7B/2T/32K/256H100有限bundle，完整precision/Serving协议未披露，未核artifact/复现。root必要原证/actual完整局部邻接PRE通过；作者新正文/完整邻接与本注写后顺读，root非写者实际507–549完整邻接、新段及本注POST通过，窄锁释放，非DAY。

- `SF-2026-ARXIV-2601-04342`（Experimental，递归等价强主张未采用）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04342v1) §3.2–3.4/Eq5–19、§4及§5。只采用chunk-local softmax/远历史kernel共同归一化及teacher到causal混合的两阶段适配；Eq13与17/18全远历史重复累加保留，不静默修公式。Wan1.3B的15/20/25 of30转换、81×480×832及低分辨率消融、500paired/50prompt、160H100h适配预算与physics/control、人偏好反侧限定；Snapdragon8Gen4 block并非端到端，precision/concurrency/SLO未披露，不采用通用性能数字。root窄写；jan10_books_audit实际必要源、正文/完整局部邻接与末注独立POST通过，未复现。

- `SF-2026-ARXIV-2602-21340`：exact-v1显式OP关联bank与Appendix C；保gate/epsilon非严格插值、碰撞和额外state，只小规模recall，未复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。
- `SF-2026-ARXIV-2602-22175`：exact-v1 relevance/EMA与log-beta intervention、同模型head反侧及预算；dense历史仍读，不授稀疏成本/SLO，未复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。

- `SF-2026-ARXIV-2602-18417` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18417v1) §3–5的群state/tangent/Exp/trace-readout与§6–7的O(d)限定实验。2+1+2=5，约束状态本体而非transition的具体差额深入；精确闭包前提/近似数值验收、weighted aggregate不在群、Exp/state/readout成本及单seed小charLM近文，不授普遍梯度或质量稳定。root必要源/actualowner PRE通过并授窄锁；作者实际正文/完整邻接及自身末注顺读、限定diff-check通过，root非作者实际正文/完整邻接及自身末注POST通过，锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18196` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18196v1) §4、§5及Table7的稀疏/ARL消融。2+1+2=5，同层全长K/V recurrence→稀疏直接读取与joint dense/dilated训练差额深入；lazy recurrence、sinks/训练预算混杂、稀疏反退及GH200operator≠生产SLO近正文。root必要源/actualowner PRE通过并授窄锁；作者实际正文/完整邻接及自身末注顺读、限定diff-check通过，root非作者实际正文/完整邻接及自身末注POST通过，锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-10796` — Daily `2026-02-13`；[PRISM exact-v1](https://arxiv.org/html/2602.10796v1) §4、D/E/F必要假设与Table3反侧。2+1+2=5，local input proxy→非线性多分量B且transition不依赖中间state的具体差额深入；rank≤L、fading条件与成本/完整KV共存近正文，不搬谱logT普适保证、174倍或推荐质量到LLM。root必要原源与current owner/邻接PRE通过授窄锁；root已实际顺读正文、前后邻接与末注，非作者POST通过，窄锁释放，日级未授。未核代码或复现。

- `SF-2026-ARXIV-2601-05505`：[FlashMem exact-v1](https://arxiv.org/html/2601.05505v1)，Daily 2026-01-13；原2+2+2=6，具体完整KV→派生latent→追加KV共存分支缺口深入。必要§3.1–3.4、§4.3/4.4及A.1–A.3/Algorithm1；不采用 injective hidden state→充分统计量、entropy→真值或无界固定成本。运行计时限单A100、固定8轮32text+8latent的受控任务，吞吐分母不含latent，64k仍慢于vanilla；不外推生产SLO。冻结参数不免除反向执行，未复现；jan01_v3实际必要原源→owner非作者核通过，正文写后待独立验收。

- **基础机制桥核验：** 线性 Attention 采用 [ICML 2020 会议版 §3.2–3.4、Eq.(5)、(9)–(12)、(16)–(20)](https://proceedings.mlr.press/v119/katharopoulos20a/katharopoulos20a.pdf)，正文为列向量约定，将原文状态矩阵转置；没有沿用其性能数字。SSM 的递推/卷积对应、输入相关 Delta/B/C 与 scan 执行依据 [Mamba v2 §2、§3.1–3.3](https://arxiv.org/html/2312.00752v2)，仅核这些定义和边界，不将特定架构结果推广为所有 recurrent 模型。本次补桥与段落归位不是对本章既有全部来源的重新事实验收。

- `SF-2026-ARXIV-2604-19877`（Experimental）：[exact-v1](https://arxiv.org/html/2604.19877v1) §2–3、§5–8、Appendix E/H；Daily 2026-04-23 日期归属仍待官方批次独立确认。仅采用共享 checkpoint 中多个训练过的 mixer placement 与运行时状态/执行计划分权。§6 当前单 preset，切换需权重迁移与 graph recapture；per-request routing 为 under development。§8 质量用 eager、吞吐用 CUDA graph，长距检索有回退，0.5B 消融不可外推 15B，作者加速数字不作通用 SLO。apr20_resume 已完成有限非作者 source→owner 核及实际正文、相邻衔接的写后复核；未复现实验，不代表日级验收。

- `SF-2026-ARXIV-2604-19021`（Experimental）：[exact-v1](https://arxiv.org/html/2604.19021v1) §2.2–3.5/Eqs8–14、§4/Tables1–4，Daily `2026-04-22`。仅采用逐通道更新强度与原对称 WY/chunk 降低形式之间的代数兼容桥；左乘外积仍为 rank-one，但不保原对称形式。双边缩放、key/value 分责与 GDN-2 只是相邻分支，不声称全胜或普遍服务收益；340M/1.3B、8K训练、H800 BF16 固定配置及 Table4 反向保留。root 已完成必要来源→当前 owner 写前复核；实际正文与相邻衔接经 root 非作者写后复核通过，见 papers/2026/04/_sources/daily-20260422/V3_ROOT_19021_WRITE_AFTER.md，未复现实验。

- `SF-2026-ARXIV-2604-21100`（Experimental）：[exact-v1](https://arxiv.org/html/2604.21100v1) §2.3/3.1–3.5/4.1/4.3/E.3，Daily 2026-04-24。采用在线 ridge Gram inverse→有条件两端预条件等价→对角近似改变执行与结论的分支；340M/1B任务退步和额外统计成本保留，不推广为通用稳定或服务收益。root 必要 source→现有 owner 采用核、实际正文及相邻衔接写后非作者复核均通过；未复现实验。
- `SF-2026-ARXIV-2604-21215`（Experimental）：[exact-v1](https://arxiv.org/html/2604.21215v1) §2.1–2.3/4–7/E.4，Daily 2026-04-24。同层 output-derived persistent KV 与当前 input temporary KV 分权，仍逐 token 增长且有时间依赖；不当作固定容量 state 或通用推理加速。root 必要 source→现有 owner 采用核、实际正文及相邻衔接写后非作者复核均通过；未复现实验。

- `SF-2026-ARXIV-2604-14339`（Experimental）：[exact-v1](https://arxiv.org/html/2604.14339v1)，Daily `2026-04-17`。采用§2.2–2.4/§3.1/3.6–3.7/Table10的同内容/mask、suffix index扰动与standard stop-gradient teacher一致性；非内容重排/teacher必真、额外forward/wall-clock非token匹配及NoPE/permutation退步保留。复用 `V3_ORDINARY_TEN_THREE_INDEPENDENT_AUDIT.md` §7及root当前必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-14191`（Experimental）：[Attention to Mamba v1](https://arxiv.org/html/2604.14191v1)，Daily `2026-04-17`。采用§3.1–3.2/§4/Table1–2/Implementation的normalized-linear中间算子→SSM初始化→受控解锁，input/output embeddings冻结；非softmax精确等价/保留attention、state/serialization成本与能力退步保留。复用 `V3_ORDINARY_TEN_THREE_INDEPENDENT_AUDIT.md` §4及root当前必要采用PASS；本次root顺读真实完整正文及相邻交接写后PASS（14591歧义修后再次读句通过），未复现实验，不预支日级Gate。

- `SF-2026-ARXIV-2604-09670`，Experimental：[exact-v1](https://arxiv.org/html/2604.09670v1) §2.1–2.3、§4.1–4.3、Discussion、A.3/A.5.12。采用访问、竞争表示和读出分离的受限解释；10模型non-thinking、字母N-back、多轮chat，五模型answer-position SVD方向干预，逐model/负载取best sweep是乐观存在性证据，不证明固定线上controller或自然语言通用收益。跨模型下游相关不作因果。apr02必要源/实际owner对照及实际两段写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-07815`（Status: Experimental）：[官方 PDF v1](https://arxiv.org/pdf/2604.07815v1) §4.1–4.2 支持当前 coarse/上一轮候选内 fine selection、增量 KV 预取与量化索引。§5 的 block size=64、128 blocks，fine budget=512/1024/2048；Qwen3-8B/14B、GLM-4.7-Flash 的质量结果不能替代 exactness。GLM RULER 有四任务因 harness 异常未测；offloading 对照包含 batch 6 对 full-attention batch 1，不作为纯流水化因果增益或生产 SLO 证据。本文的失效检测/fallback 是系统设计建议，不是作者已验证机制。

- The Attention Within（Status: Experimental）：[arXiv:2609.17997v1](https://arxiv.org/html/2609.17997v1) 的 §II–V 在 continuous-time Mamba-2 depth dynamics 与 PoE/positive-definiteness 假设下分析 consensus equilibrium，§VI 检查 fixed/time-varying weights 和 output gate；不证明实际离散网络、训练过程、所有输入或任务质量必然收敛，output gate 只支持可观测范围与 state convergence 分离。

- [Momentum DeltaNet](https://arxiv.org/html/2605.05838v1)（Status: Experimental）：400M/1.3B 结果支持二阶 recurrent update 与 chunk-parallel formulation；未验证 7B+、TP 或生产 Serving。

- Prefix Sliding（task prefix + recent reasoning window；Status: Experimental）：
  https://arxiv.org/abs/2608.26070v1

- Flux Attention（prompt-conditioned layer routing；Status: Experimental）: https://arxiv.org/abs/2604.07394
- SinkTrack（adaptive dual-track context anchor；Status: Experimental）: https://arxiv.org/abs/2604.10027

本轮联章 Review 明确了 MoE 的参数容量轴与 Long Context 的序列容量轴，并补齐 Part II → Part III → Part IV 的过渡。既有 FlashAttention、Ring Attention、ShadowKV 与 RAG 内容保持不变。后续新增任何长上下文方法，都应先标注它改变位置、pair compute、KV bytes、memory hierarchy 还是 working set。

SRLM 的实验性结果用于补足 programmatic Context interaction、candidate-program state 与 selection/acceptance 分层；正文不保留作者模型排名、相对增益或把 verbalized confidence 解释成 calibrated uncertainty。

Primary-source 校验入口：

- Tri Dao et al., "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", 2022: https://arxiv.org/abs/2205.14135
- Ofir Press, Noah Smith, Mike Lewis, "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation", 2021: https://arxiv.org/abs/2108.12409
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245
- Hao Liu et al., "Ring Attention with Blockwise Transformers for Near-Infinite Context", 2023: https://arxiv.org/abs/2310.01889
- Nelson F. Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", 2023: https://arxiv.org/abs/2307.03172
- Hanshi Sun et al., "ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference", 2024: https://arxiv.org/abs/2410.21465
- MiniMax et al., "MiniMax-01: Scaling Foundation Models with Lightning Attention", 2025: https://arxiv.org/abs/2501.08313
- Songlin Yang et al., "Gated Delta Networks: Improving Mamba2 with Delta Rule", 2025: https://arxiv.org/abs/2412.06464
- Ali Hatamizadeh et al., "Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention", 2026（Status: Experimental）: https://arxiv.org/abs/2605.22791
- Klaus Greff et al., "LSTM: A Search Space Odyssey", 2015: https://arxiv.org/abs/1503.04069
- Zihan Qiu et al., "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free", 2025（Status: Experimental）: https://arxiv.org/abs/2505.06708
- Jingyang Yuan et al., "Native Sparse Attention", 2025: https://arxiv.org/abs/2502.11089
- DeepSeek-AI, "DeepSeek-V3.2", 2025: https://arxiv.org/abs/2512.02556
- Ali Behrouz et al., "Titans: Learning to Memorize at Test Time", 2025: https://arxiv.org/abs/2501.00663
- Ali Behrouz et al., "It's All Connected / MIRAS", 2025: https://arxiv.org/abs/2504.13173
- Fast-weight Product Key Memory（Status: Experimental；sparse inference-time mutable state）:
  https://arxiv.org/abs/2601.00671
- Sparse Delta Memory（parametric `M_0` / request-owned `M_t` 与 iso-FLOP capacity；Status: Experimental）:
  https://arxiv.org/abs/2607.07386v1
- Linear Attention Architectures（cross-layer routing basis alignment；Status: Experimental）:
  https://arxiv.org/abs/2607.07953v1
- Zhichen Liu et al., "LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference", arXiv v1, 2026（Status: Experimental）: https://arxiv.org/abs/2608.02515
- HALO / HypeNet（dense checkpoint 到 hybrid recurrent-attention state 的受限迁移案例；Status: Experimental）: https://arxiv.org/abs/2601.22156
- Mergeable Aggregation State（模型生成可合并代数状态，替代把全部中间历史重新放回 prompt；Status: Experimental）:
  https://arxiv.org/abs/2607.26448v1
- Recursive Language Models Meet Uncertainty（Status: Experimental）: https://arxiv.org/abs/2603.15653
- Density-aware Soft Context Compression（Status: Experimental；density proposal 与 decoder contract）:
  https://arxiv.org/abs/2603.25926
- HySparse（full-layer-owned global selector/KV + layer-local SWA；Status: Experimental）: https://arxiv.org/abs/2602.03560
- LycheeDecode（retrieval-head refresh 与 sparse-head index reuse；Status: Experimental）: https://arxiv.org/abs/2602.04541
- Prism（RoPE-aware spectral block selection；Status: Experimental）: https://arxiv.org/abs/2602.08426
- Gated Recurrent Memory（write admission 与 exit gate；Status: Experimental）: https://arxiv.org/abs/2602.10560
- LycheeMemory（compressed KV memory bank；Status: Experimental）: https://arxiv.org/abs/2602.08382
- MiniCPM-SALA（sparse/linear hybrid 与 staged conversion；Status: Experimental）: https://arxiv.org/abs/2602.11761
- HiLS-Attention（forward-coupled hierarchical sparse selector；Status: Experimental；不证明字面意义的无限上下文）: https://arxiv.org/abs/2607.02980v1
- MiniMax Sparse Attention（selector gradient ownership 与 KV-outer block execution；Status: Experimental）:
  https://arxiv.org/abs/2606.13392
- REFINE（fast-state objective horizon；Status: Experimental）: https://arxiv.org/abs/2602.16704
- 2Mamba2Furious（higher-order recurrent state；Status: Experimental）: https://arxiv.org/abs/2602.17363
- Memory Caching（growing compressed checkpoints；Status: Experimental）:
  https://arxiv.org/abs/2602.24281
- TTT with KV Binding（test-time update as conditional linear-attention state；Status: Experimental）:
  https://arxiv.org/abs/2602.21204
- `SF-2026-ARXIV-2604-20915` — [Absorber LLM v1](https://arxiv.org/html/2604.20915v1)，§3.1–3.3/Eq2–6/Alg1–2、§4.1–4.2、§4.6.2–4.6.3；有限后续 hidden-state 对齐，冻结 teacher/更新学生依 Alg1 区分，不沿 §3.2 符号不一致。source→owner 非作者 apr02 通过；实际正文写后待 root 核验；未复现实验，precision/并发/SLO 未披露。

### Daily integration evidence trace

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-22874` — primary `arXiv:2606.22874v1`; Method=`arXiv:2606.22874v1 — §SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers; §Method; §2.1 Selector architecture`; Evaluation=`arXiv:2606.22874v1 — §Evaluation.; §Analysis and ablations; §Empirical shape gap.`; non-proof=`arXiv:2606.22874v1 — §Conclusion`; fallback=该 family 的 failure pressure 是：Sparse attention cuts these costs by attending only to a relevant subset of past tokens, but selecting that subset is itself expensive. 披露的 evaluation signal 是：Quantizing the selector's K-cache to INT4 or FP4 microscale shrinks it 3.5x at no accuracy cost. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

#### Source-specific Review notes

- SF-2026-ARXIV-2606-25156: `arXiv:2606.25156v1`; exact-v1 URL=`https://arxiv.org/html/2606.25156v1`; Method=`https://arxiv.org/html/2606.25156v1 — §3 Methodology; Polar Attention; Gated-Delta Memory`; Evaluation=`https://arxiv.org/html/2606.25156v1 — §4 Experimental Setup; 5 Results; C Complete Sweep`; Non-proof=`378M、2K train、256K eval 中 FinePDFs exact retrieval 为 0%，hardware transition audit 非随机；不能宣称普遍外推，Raven/softmax/更短 context 仍是共存点。`; Artifact=`https://github.com/kreasof-ai/atma`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-25342**：Primary `arXiv:2606.25342v1`；Method `https://arxiv.org/html/2606.25342v1 — §Parametric Attention and Lifelong In-Context Learning formulation`；Evaluation `https://arxiv.org/html/2606.25342v1 — §Experiments; Lifelong sequence results`；未证明边界 `https://arxiv.org/html/2606.25342v1 — §Discussion; finite-memory and task-family limitations`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-2026-ARXIV-2606-15378:start -->
- `SF-2026-ARXIV-2606-15378` — Daily `2026-06-14`；primary `arXiv:2606.15378v1`；Books review `books-review:SF-2026-ARXIV-2606-15378`。

  **已吸收的语义增量：** hybrid architecture 中 efficient attention 主要塑造 optimization，而长程 retrieval 仍主要由 full-attention layers 承担；ratio 与 positional treatment 应按该分工设计。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15378:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16310:start -->
- `SF-2026-ARXIV-2606-16310` — Daily `2026-06-16`；primary `arXiv:2606.16310v1`；Books review `books-review:SF-2026-ARXIV-2606-16310`。

  **已吸收的语义增量：** MLA 的 post-projection QK RMSNorm 可拆成可吸收的静态权重与每 token/group 动态标量，从而保留 latent KV decode path
<!-- daily-books-trace:SF-2026-ARXIV-2606-16310:end -->


<!-- daily-books-trace:SF-2026-ARXIV-2606-21803:start -->
- `SF-2026-ARXIV-2606-21803` — Daily `2026-06-20`；primary `arXiv:2606.21803v1`；Books review `books-review:SF-2026-ARXIV-2606-21803`。

  **已吸收的语义增量：** TTT-NTP 在推理时用 next-token prediction 写入 fast weights；write scope、chunk boundary 与 reset policy 必须成为 context state
<!-- daily-books-trace:SF-2026-ARXIV-2606-21803:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-02980:start -->
- `SF-2026-ARXIV-2607-02980` — Daily `2026-07-07`；primary `arXiv:2607.02980v1`；Books review `books-review:SF-2026-ARXIV-2607-02980`。

  **已吸收的语义增量：** 新增证据边界：Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 该 delta 已进入 `books/part-02-model/22-long-context.md#L247`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-02980:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07386:start -->
- `SF-2026-ARXIV-2607-07386` — Daily `2026-07-09`；primary `arXiv:2607.07386v1`；Books review `books-review:SF-2026-ARXIV-2607-07386`。

  **已吸收的语义增量：** 新增证据边界：Sparse Delta Memory replaces a fixed dense recurrent matrix with an explicit N-by-d memory table. Product keys choose a small write set and read set, and a gated delta rule changes only selected slots. Increasing N expands addressable state without increasing per-token arithmetic proportionally, but the physical table grows and leaves fast on-chip memory. 该 delta 已进入 `books/part-02-model/22-long-context.md#L374`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07386:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07953:start -->
- `SF-2026-ARXIV-2607-07953` — Daily `2026-07-10`；primary `arXiv:2607.07953v1`；Books review `books-review:SF-2026-ARXIV-2607-07953`。

  **已吸收的语义增量：** 新增证据边界：A common recurrent form exposes where DeltaNet/GDN/Kimi-like architectures differ in decay, update and gating rather than treating names as incomparable systems. Cross-layer error routing fails when a write residual is injected into a basis that does not share its representation; CLVR first projects the write value into an aligned hidden stream, making the added route semantically compatible. 该 delta 已进入 `books/part-02-model/22-long-context.md#L180`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07953:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.26448:start -->
- `SF-2026-ARXIV-2607.26448` — Daily `2026-07-30`；primary `arXiv:2607.26448v1`；Books review `books-review:SF-2026-ARXIV-2607.26448`。

  **已吸收的语义增量：** 新增证据边界：The model emits compact mergeable aggregation state so set-like queries can be combined without serializing every intermediate value back through the prompt. This trades exact raw-history access for algebraic state semantics, merge correctness and task-specific operator support; it fills a gap between token context and externally executable aggregation. 该 delta 已进入 `books/part-02-model/22-long-context.md#L529`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.26448:end -->

<!-- daily-books-trace:SF-2026-PREFIX-SLIDING:start -->
- `SF-2026-PREFIX-SLIDING` — Daily `2026-08-27`；primary `arXiv:2608.26070v1`；Books review `books-review:SF-2026-PREFIX-SLIDING`。

  **已吸收的语义增量：** 当前书稿 diff 已把以下长期机制写入该 owner：永久保留 system/task prefix 与最近 reasoning window，丢弃中间 token；继续 RoPE position 复用 KV，RL 侧用约4×window context、末端 loss mask；并保留边界：LiveCodeBench 旧代码依赖受损；短生成收益小、tool output 可淹没 window；v1 时 repo 只有 README/License，无实现代码。 相邻章节对读：books/part-02-model/21-moe.md#L317;books/part-03-multimodal-world-models/23-multimodal-representation.md#L215。MoE 拥有 conditional compute，Multimodal Representation 拥有 modality identity；token-retention policy 与 context-loss boundary 属于 Long Context。
<!-- daily-books-trace:SF-2026-PREFIX-SLIDING:end -->

- `SF-2026-ARXIV-2512-25026`：[exact v1](https://arxiv.org/html/2512.25026v1) §3.1–3.3句表示/rolling memory/不detach及训练stream curriculum，§4.1–4.4和Table1，Appendix B/C.1及§5限制。采用visible window与递归training graph/credit horizon分账，不采用规模拟合、通用速度或reversal-curse已解决的宣称。必要原源、限定命题及实际正文/邻接已由root非作者复核通过；未运行代码或复现实验。

- `SF-2026-ARXIV-2512-23862` — Daily `2026-01-02`；[Probing the Limits of Compressive Memory exact-v1](https://arxiv.org/html/2512.23862v1) §3.1–3.5、§4–5/Table1及§6–9限制。7分只采用retrieve-before-update/gate使用与有效远程retrieval分界、真实训练支持与padded length、LR对照不一及FT depth失败；不由0.4%>8192倒推全部≤1024，不采单depth提升为全位置或硬件保证。必要精度BF16/needle累积FP32，硬件/总成本未披露、未复现；必要原源、具体owner及实际正文/邻接写后已由root非作者复核通过。

- `SF-2026-ARXIV-2512-23966` — Daily `2026-01-02`；[LoZA exact-v1](https://arxiv.org/html/2512.23966v1) §1 Calibration/Training、§2–3及Table1。6分具体gap深入，采用end-of-midtraining校准选布局再rewind/retrain的身份分账；50% MLA替SSA、1sink+7×128只限稀疏层，540B token/后训练及LongEval退步保留，不授整网固定成本、免费转换或无损。未复现实验；root必要原源与具体owner写前通过，root实际正文800、780–811邻接及1257末注非作者写后复核通过，日级Gate待验。

- `SF-2026-ARXIV-2601-07832` — Daily `2026-01-14`；[MHLA exact-v1](https://arxiv.org/html/2601.07832v1) §4.1–4.3 Eq3–5、Table1及必要视觉/视频、块数对照，AppC仅定位隔离边界。原6分具体缺口深入，只采用block-summary bank与learned blockmix、O(Nd²+M²d²)/O(Md²)成本条件，不授动态router、普遍满rank/线性、AR causal/cache精确性或冲突NLP人口的质量结论。未核实现或复现实验；root必要原源和实际owner写前通过，jan01_v3实际顺读545–583正文/邻接及1263源注，非作者写后通过；不等日级Gate。

- `SF-2026-ARXIV-2602-06283` — Daily `2026-02-10`；[SOCKET exact-v1](https://arxiv.org/html/2602.06283v1) §4/Algo1–3、§5关键假设/Lemma5–6、§6及AppD。2+2+2=6，具体selector gap与理论实践冲突深入；只采用hard-key/soft-query graded rank与全部N扫描成本，不采用冲突最终weight配方、angular-kernel theory对practicalTopK softmax exactness或单层速度对E2E保证。有限质量反侧/AVG分母、模型口径与metadata成本保留；未核实现/复现。root必要源/owner写前通过并授窄锁，实际两段+末注已写，root 已实际顺读两段正文、前后交接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-12021` — Daily `2026-02-14`；[exact-v1](https://arxiv.org/html/2602.12021v1) §2–3/Prop1、§6–7、AppE。只采用时间 companion/块内 mixing 与输入+状态联合 row-L1 的有界前向条件，保留非零初态、m³ scan、状态预算及质量反退；不授梯度或收敛保证。 root 必要源/具体 owner PRE 通过并授单文件两段窄锁；实际两段正文、前后邻接与本末注经 root 非作者 POST 通过，窄锁释放；已落实。未运行代码或复现实验，非日级 Gate。

- `SF-2026-ARXIV-2602-15257` — Daily `2026-02-19`；[Long-context visual documents exact-v1](https://arxiv.org/html/2602.15257v1) §3–5/Table1–7/AppendixA.1。2+2+2=6，page-identity train/infer一致性差额深入，344K窗口与336页分清；merged artifact、resolution/budget混杂、recursive54.5vs57.0反侧及评价版本改变保留。Ch66评价owner不重复推导；root必要源/owner PRE通过，root已实际核正文/完整邻接及末注，非作者POST通过，窄锁释放，未核代码或复现。

- `SF-2026-ARXIV-2602-13680` — Daily `2026-02-18`；[AllMem exact-v1](https://arxiv.org/html/2602.13680v1) §3.2/Fig.2、§3.3、§4–5。2+2+2=6，具体 norm 对象/时序差额深入；采用先读旧 unnormalized fast weights、再 memory weight normalization、最后 chunk update，不是 readout norm 或已核 clipping 实现。冻结迁移范围、局部精度反侧、momentum 下标争议及 FLOPs/cache 非 SLO 边界保留；未核代码或复现。root必要源/owner PRE通过并授Ch22窄锁，实际两段、完整邻接与末注非作者POST通过，锁释放；日级未验收。

- `SF-2026-ARXIV-2602-16839` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16839v1) §3/Eq2–4与§4必要反侧。2+2+2=6，forward stream-state具体差额深入；Qwen3B/7B配置冲突性能隔离，不授全pipeline常数/无限容量；reset/provenance为明确工程边界。root必要原源/actual owner PRE通过并授窄锁，作者实际正文/完整邻接/末注已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-21454` — Daily `2026-02-27`；[When Learning Hurts exact-v1](https://arxiv.org/html/2602.21454v1)。2+1+3=6，pole collision的Hessian病态与forward稳定分开；有限无噪识别/固定basis表达代价与learned回退近文，不将κ(Wrec)作loss曲率或宣全RNN不可学。root必要源/actual owner PRE通过并授单段窄锁；作者实际正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放，未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-22719` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22719v1) 必要blocks23–55/57–61/71–101/263–276/300–311；2+1+3=6，entropy/消融/gain选择分责与独立bundle费用差额深入。fresh非原prepared作者必要原证/actual owner PRE完成，身份/精确v1/命题未变结果复用；获Ch22窄锁，人口、成本口径反侧及原递推回退近正文，作者已实际顺读正文/完整邻接/自身末注，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放；未核实现/复现，非日级。

- `SF-2026-ARXIV-2602-23201` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23201v1) 必要blocks20–43/44–74/86–103；2+1+2=5，instruction-conditioned write/read及排除probe差额深入，synthetic/retention/test-ood择优反侧与费用近文。root窄准入通过，fresh非原packet作者必要原证/actual owner PRE完成并获Ch22锁；作者实际正文/完整邻接/自身末注已顺读，root非写入者实际独读正文/完整邻接/自身末注POST通过，窄锁释放；未核实现/复现，非日级。

- `SF-2026-ARXIV-2602-08426` — Daily `2026-02-11`补查；[Prism exact-v1](https://arxiv.org/html/2602.08426v1) §3/4/8/9；2+1+2=5，RoPE下pooling的频率衰减与重叠band/RMS校准具体差额深入。近稳定内容条件、dead-zone噪声、Top-P union与真实density近正文；不授互斥频带、信息复原或dense exact。RULER128K Llama72.75<77.77、Qwen72.65<75.09，5.1×仅H100 attention prefill、20%仅selector workspace；B64 selector约22ms>B128约9ms。root实际必要Source与owner完整邻接/PRE通过并授本一段及自身末注窄锁；作者实际正文与完整局部顺读，root非作者实际343–365完整邻接、新352及1355自身末注POST通过，窄锁释放。未核实现或复现，不授DAY。

- `SF-2026-ARXIV-2602-11852` — Daily `2026-02-14`补查；[ProtoT exact-v1](https://arxiv.org/html/2602.11852v1) §3/4/5/6，2+2+2=6，固定 prototype EMA/mass 读写差额定点深入。只采 past-only read-before-write 与容量分责，不授可命名概念即 faithful reasoning、PMR 全局稳定、无限召回或端到端加速；234.9M/L12/h512 质量、ctx1024→2048 PPL80.5→81.9、BF16短ctx训练反退与单H100/b1长ctx交叉点限定。root/reviewer必要Source及actual owner/邻接PRE通过，root授两段+本人末注窄锁；作者已写并顺读完整邻接，review_20260214已实际独核新正文、完整邻接与本末注，非作者actual POST通过，root释放窄锁，不授DAY。未核artifact/复现。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2602-12204` — Daily `2026-02-14`补查；[CRAM exact-v1](https://arxiv.org/html/2602.12204v1) §2/4/6–9，2+2+2=6，真实读取输出→semantic近似与episodic例外接口差额深入。q依当前retrieval、免费无读取gate未成立，DynMSE/Activity反退、probe非causal/attention非总费限定近正文；root actualowner拟文经review_20260214非作者逐字PRE通过，root授一段及本人note窄锁；作者新段/完整邻接/本人note已顺读，非writer实际正文、完整局部邻接及本人末注actualPOST通过，root释放窄锁。不授完整循环router执行recipe、生物因果、实现/复现或DAY。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。
