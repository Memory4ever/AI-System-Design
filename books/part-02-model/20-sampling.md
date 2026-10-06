# 第20章 Sampling

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-SAMPLING`
**Legacy Chapter:** Ch20
**Status:** Draft

**Roadmap Intent:** 温度、top-k、top-p、贪心解码如何影响输出风格和稳定性。

## 本章要回答的问题

Decoder-only 模型每步输出 `V` 个 logits，为什么不能说“模型已经给出了答案”？Greedy、temperature、top-k 和 top-p 怎样把概率分布变成一个 token，又分别牺牲什么？

本章的核心判断是：**Sampling 是把模型条件分布转换为单条实际生成轨迹的决策过程。**它可以改变随机性、重复、尾部风险和输出多样性，不能增加 checkpoint 中不存在的知识，也不能把低概率正确答案稳定变成高概率答案。

[上一章](./19-kv-cache.md)保存了逐层 K/V，使下一步能够复用历史计算；但 cache 不决定输出哪个 token。本章先完成 logits、候选处理、选择与停止的最小闭环，再讨论何时值得延长一条轨迹、生成多条轨迹，或增加更强的约束与验证。这些是受任务和预算约束的分支，不是每次生成都必须经过的阶段。

本章使用 `B` 表示 batch size，`T` 表示 sequence length，`V` 表示 vocabulary size。

## Logits 还不是概率

[第18章](./18-decoder-only.md)得到：

```text
logits shape = [B,T,V]
```

生成下一 token 时，取每个 sequence 最后一个有效 position：

```text
z shape = [B,V]
```

`z_i` 是 token `i` 的未归一化分数。Softmax 将它转换为概率：

```text
p_i = exp(z_i) / sum_j exp(z_j)
```

数值实现通常先减最大 logit：

```text
p_i = exp(z_i-z_max) / sum_j exp(z_j-z_max)
```

减去同一常数不会改变概率，却能减少 overflow。

有了归一化后的分布，下一步仍不是唯一的：它可以支持确定选择，也可以支持随机抽样。先固定同一组 logits，才能看清各策略究竟改了什么。

### 一个固定 logits 例子

假设 vocabulary 只有三个候选，logits 为：

```text
z = [2,1,0]
```

Softmax 近似得到：

```text
p = [0.665,0.245,0.090]
```

模型认为 token 0 最可能，但 token 1 和 token 2 仍有非零概率。Decoder 必须选择：总取最大值，还是按某个变换后的分布随机抽样。

## Greedy decoding：每步取最大值

Greedy 选择：

```text
token = argmax_i z_i
```

在例子中总选择 token 0。它简单、单步确定、无需随机数，但只保证当前一步概率最大，不保证整段序列联合概率最高，也不保证最终任务质量最好。

语言生成中，局部最可能路径可能进入重复、模板化或过于保守的区域。另一方面，结构化抽取、分类式输出或严格复现任务可能更需要低随机性。

## Temperature 改变分布锐度

Greedy 在需要低随机性时足够直接；当同一个前缀允许多个合理续写时，先保留随机抽样，再控制分布的尖锐程度，比只取最大值更灵活。

Temperature `tau > 0` 作用于 logits：

```text
p_i(tau) = softmax(z_i / tau)
```

- `tau < 1`：分布更尖锐，高 logit 更占优势。
- `tau = 1`：保持原 softmax。
- `tau > 1`：分布更平坦，低概率 token 更容易被选中。

对 `z=[2,1,0]`：

```text
tau=0.5 -> softmax([4,2,0])   ~= [0.867,0.117,0.016]
tau=1.0 -> softmax([2,1,0])   ~= [0.665,0.245,0.090]
tau=2.0 -> softmax([1,.5,0])  ~= [0.506,0.307,0.186]
```

Temperature 不改变 logits 排名，只改变相对概率。`tau -> 0` 的极限接近 greedy，但实现通常不会真的除以 0，而是使用专门 greedy path。

## Top-k：固定保留 k 个候选

温度会重新分配概率，却不会单独移除尾部候选。如果问题是少量极低概率 token 会把续写带偏，就需要限制允许抽样的集合。

Top-k 只保留概率或 logits 最高的 `k` 个 token，其余设为 0，再重新归一化。

例子中 `k=2`：

```text
before = [0.665,0.245,0.090]
keep   = [0.665,0.245,0.000]
renorm = [0.731,0.269,0.000]
```

它直接移除长尾候选，降低抽到极低概率 token 的风险。但固定 `k` 不感知分布形状：模型非常确定时仍保留 `k` 个，模型非常不确定时又可能只保留过少候选。

## Top-p：按累计概率动态截断

固定候选数适合可接受集合大小相对稳定的情形；当不同前缀的分布锐度差异很大时，约束保留的概率质量更能随模型状态变化。

Nucleus sampling 先按概率降序排列，选择累计概率达到阈值 `p` 的最小 token 集合，再归一化抽样。

对同一例子，`top_p=0.8`：

```text
token 0 cumulative = 0.665 < 0.8
token 1 cumulative = 0.910 >= 0.8
```

因此保留 token 0 和 1，结果同上：

```text
[0.731,0.269,0.000]
```

若 `top_p=0.6`，第一个 token 已超过阈值，候选集可能只剩 token 0。具体实现通常保证至少保留一个 token。

Top-p 的候选数会随分布变化：模型确定时集合小，不确定时集合大。这是它相对固定 top-k 的主要适应性。

## Logit penalties 与约束的边界

Top-k 与 top-p 依据当前分数删减候选；如果任务还要求减少已出现内容的重复，或只允许合法格式，就需要把历史与任务约束也带入这一步。

Repetition、frequency、presence penalties 会根据已生成 tokens 修改 logits；grammar-constrained decoding 会屏蔽不符合语法的候选。

它们都发生在 token selection 层，却解决不同问题：penalty 是启发式偏好，grammar mask 是硬候选约束。它们可能改善格式或减少重复，也可能屏蔽正确 token。

本章不展开具体 API，因为参数定义和顺序依赖实现。稳定原则是：任何 logits 变换都应进入 Evaluation 和可复现配置。

## 参数组合的顺序很重要

现在已有改变分数、删减候选与调整锐度的不同操作。它们要共同作用于一次选择，因此必须先确定操作顺序，再讨论实际抽到了什么。

常见逻辑是：

```text
raw logits
-> penalties / constraints
-> temperature
-> top-k / top-p filtering
-> renormalize
-> random sample
```

但不同框架可能采用不同 processor 顺序，top-k 与 top-p 也可能同时启用并取交集。由于这些变换通常不可交换，相同参数名不保证跨 runtime 产生完全相同分布。

因此生产系统要版本化完整 decoding config，而不是只记录 temperature。

## Random seed 与确定性边界

固定处理顺序只固定了目标分布；随机样本能否复现，还取决于执行时如何消费随机数。

随机抽样需要伪随机数。固定 seed、相同 logits、相同候选处理和相同随机数消费顺序时，通常可以复现 token 选择。

但端到端确定性还可能受以下因素影响：

- Batch 中请求进入和退出改变 RNG consumption。
- 并行执行与 kernel 可能包含非确定性。
- 不同 precision 使接近阈值的 logits 排名变化。
- Runtime 版本改变 logits processor 顺序。
- 模型、tokenizer、prompt 或 adapter 不同。

所以 `seed` 是生成配置的一部分，不是跨系统字节级复现保证。

## EOS、停止条件和最大长度

选中 token 后还不能无条件进入下一轮：输出可能已经完成，也可能需要由系统预算强制终止。停止规则因此与候选选择一起定义生成行为。

EOS 是 vocabulary 中的特殊 token。若被选中，generation 可以结束。系统还可能使用：

- Maximum generated tokens。
- Stop token ids 或 stop strings。
- Grammar/schema constraints。
- 超时与任务预算。

Stop string 可能跨 token 边界，需要 detokenization 或增量匹配；EOS 则直接在 token 层终止。二者不能混为一谈。

若模型长期不给 EOS，max tokens 是系统安全边界。若 EOS 被错误 suppress，输出和 KV Cache 会持续增长。

### 把单步选择接回自回归循环

```text
Decoder hidden state
-> logits [B,V]
-> temperature / filtering / constraints
-> token id [B]
-> append token id to sequence
-> next Decode step computes and appends its K/V
-> repeat until stop
```

这里有一个容易混淆的时序：采样先把 token id 追加到序列，下一次 Decode 才计算这个 token 的 K/V；若已经满足停止条件，就无需为了继续生成而再执行一步。至此，普通单轨迹生成已经完整，后面的控制与搜索只在这条基础路径触及约束时启用。

## Sampling 为什么会影响长程行为

每步选择的 token 会进入下一步 prefix：

```text
x_(t+1) ~ p(. | x_<=t)
```

一次低概率选择会改变之后全部 logits。Sampling 因此不只是最终输出层的小装饰，而是在自回归闭环中持续改变状态轨迹。

过于 greedy 可能形成重复或单调模式；过高 temperature 或过宽 tail 可能让早期错误把序列带离高质量区域。Top-k/top-p 试图截断不可靠 tail，同时保留一定多样性。

不存在全任务通用的最佳参数。代码生成、创意写作、事实问答、结构化 JSON 和 Agent tool arguments 对随机性的容忍不同。

### 局部校准误差会复合成序列级多样性坍缩

top-k、top-p 或 temperature 假设 token 概率的相对顺序和形状足以支持逐步选择；在短输出和低歧义任务中这是合理近似。长序列会把 order miscalibration 与 shape miscalibration 持续写回 prefix：前者让候选排序错误，后者让概率质量过尖或过平，局部误差最终表现为 sequence-level diversity collapse。评测因此要同时保存 token-level calibration slice 与整段输出的覆盖、多样性和正确性，不能只调一个解码超参数。

联合校准增加 reference distribution、采样次数和 evaluator 成本，也可能把任务本身的单峰答案误判为坍缩。确定性任务或严格可复现接口仍可使用 greedy/低温策略；缺少可靠 target distribution 时应报告未判定而非声称已校准。`arXiv:2605.11128v1` 的 §4–§5、相关附录实验及 Appendix J 只证明作者模型与任务上的两类误差，不给出跨 workload 的通用采样配方。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11128 -->

多次抽样时，局部选择目标还可显式包含“一个有价值 token 至少被抽到一次”。给定 K 次独立抽取与非负价值 proxy `w_v`，命中效用为 `U_K(q)=Σ_v w_v[1−(1−q_v)^K]`；K>1 时边际收益递减，继续提高已有高概率 token 的收益会变小。把这个效用与模型 score、相对原分布的 KL 代价合并，再从原分布开始以 mirror ascent 迭代求每步 q，是不同于固定 temperature 或截尾的局部采样分支。[BoK 的必要目标与对照](https://arxiv.org/html/2602.18292v1#S4.SS3)不把 token 命中变成完整正确解答覆盖：后续 prefix 依赖、价值 proxy 与 selector 仍决定整条轨迹结果，未披露的实际 K/weight 配方也不能由 baseline 的 top-k=50 补齐。逐 token 迭代需付计算，受测五步与更多步的质量并不单调，低温 GPQA/HumanEval 有反侧，未绑定硬件与服务协议的局部秒数不认证 SLO。单样本、近确定任务或 proxy/成本失配时，保留 greedy、普通 temperature/top-p 与独立候选加 verifier，不由“防坍缩”目标自签可靠性。<!-- source-family:SF-2026-ARXIV-2602-18292 -->

## 单轨迹控制：何时多算、何时提交

逐步选择会改变后续前缀，因此长度不只是输出统计，也是一项可控制的计算预算。先从不修改模型的停止策略开始，再区分对轨迹内部状态的干预和对答案提交顺序的调整；它们优化的对象并不相同。

### Test-time Budget 是 Runtime Policy，不是免费能力

Reasoning model 让停止条件进一步变成 compute policy：runtime 可以在达到上限时硬性停止生成，也可以注入结束标记，尝试把 thinking 通道切到 answer；后者不保证后续不再出现 reasoning-like 续写，阻止结束标记再次出现也不等于停止这种行为。反过来，模型过早结束时，可以抑制 delimiter、追加 continuation cue，再给它更多 token。
这类 budget forcing 证明“生成长度”可以成为可控变量，却不证明更多 token 必然提高质量，也不能仅凭文本 phase 标记推断不可直接观察的内部推理状态。[受限行为与干预证据](https://arxiv.org/html/2609.03633v1)

它把旧的自然 EOS 行为换成显式 sequential-compute budget：获得 capacity planning 与质量/成本
曲线的可控性，同时引入 forced continuation 的分布偏移、重复或错误推理、tail latency、KV
增长和被截断的 final answer。普通 EOS 在短任务、低延迟或模型已能可靠停止时仍更合理；并行
采样与 verifier 则用多条轨迹换取鲁棒性，和延长单条轨迹不是同一种 scaling。生产记录必须把
`reasoning budget + stopping policy + model/runtime version` 绑定到同一 evaluation subject。

文本信号还可以定义一种不同于答案正确率的停止风险：在完整、model-relative 的 wellposed 校准轨迹上，先固定 keyword lexicon、token bin 与统计函数，取每条轨迹所有 bin 的最大值，再用有限样本 order statistic 设阈值。测试轨迹任一 bin 严格越阈值才停止；在校准与测试完整轨迹可交换、统计函数固定的前提下，这把反复窥视的 ever-cross 事件一次纳入校准，而不是把每个局部检验的风险直接相加或当独立事件。它控制的是 wellposed 轨迹被误停的概率，不是提交答案错误率，也不保证识别所有坏推理。模型、lexicon、bin 或任务分布变化需重新核查；所测 OOD 的误停率仍有高于目标的反侧，缺少可区分文本信号时检测能力有限，粗 bin 会漏掉短轨迹，在线统计与离线完整生成也有成本。Renewal/Šidák 的近似分支不具有同一有限样本证书；普通 EOS 和硬 token/deadline 预算仍是无可靠信号时的回退。<!-- source-family:SF-2026-ARXIV-2602-13935 -->

### 从请求级 Budget 到轨迹内 Feedback Control

请求开始时一次性选择 `max_tokens`、effort tier 或停止策略，状态少、容易做 admission 和成本上界；当任务难度较窄、
模型不能暴露内部状态或 deadline 是硬约束时，它仍是最稳健的设计。困难来自同一 checkpoint 面对难度差异很大的
请求：统一压短会伤害必要探索，统一放长又会把冗余推理转化为 tail latency 与 KV 占用。

一种更细的分支是在生成过程中读取 model-relative signal，例如近期 token confidence 与局部波动，再双向调节继续探索
或尽快 commit：

```text
fixed request budget
-> difficulty-aware external stop
-> trajectory-state feedback
-> bidirectional internal control under a hard outer budget
```

这里的 confidence 不是 correctness，也不是校准后的不确定性。若控制依赖 hidden-state direction，系统还必须把 checkpoint、
tokenizer、注入 layer、control vector、window、阈值和 prompt/adapter revision 绑定成同一 artifact；版本漂移或 proxy 误判会
抑制必要 self-correction，也可能放大错误自信。外层 scheduler 仍拥有 deadline、fairness 与资源上限，模型侧 controller 只在
该 envelope 内调节轨迹。ReBalance 的实验说明这类双向控制在若干 reasoning workload 上可以改变 accuracy-length frontier，
不证明它能普遍提升线上 capacity。无法取得 hidden/logprob、高风险任务需要可解释 verifier，或控制 artifact 尚未校准时，
固定 budget、普通 EOS 和外部 early exit 继续成立。

### Semantic Steering 可以从单向 Vector 扩展为受限 Subspace

前一分支围绕是否继续探索调节轨迹；若目标变成引导特定语义行为，控制对象就从时长转向 hidden-state 方向。两者都干预生成过程，但语义 steering 不能充当停止策略或正确性验证。

单个 steering vector 适合近似一维、方向稳定的概念；当概念在 hidden state 中占据多个相关方向时，固定向量会漏掉模式，过强插值又可能破坏流畅性。Conceptor 一类分支用 contrastive activations 估计概念子空间，再通过 interpolation 或 replacement 控制投影强度；layer quota 只用于发现可能有效的 intervention point，不能作为 correctness 或安全真值。

子空间扩大 coverage，也会因 overlap、有限 pairs、layer drift 与 Boolean composition 产生非预期耦合，replacement 过强还可能生成退化输出。概念近似线性、简单向量已经稳定时保留旧方案；校准不足或外部行为 verifier 不通过时，应降低强度、关闭 steering 或回退提示/微调。exact-v1 只测试三种较小 instruction model、三个英文概念、单层 intervention 与自动 classifier，不证明生产行为正确或安全。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04980 -->

除了扩大单个概念的子空间，也可以保留有限 steering vector 库，让请求条件决定组合与强度。[一个受限 reasoning 分支](https://arxiv.org/html/2601.09269v1)先从正负回答的 contrastive activations 聚类建库，再由双头 controller 在 prefill 最后位置读取 hidden state，分别提议选哪些向量、各注入多少；得到的组合随后在整个 decode 中静态复用。这是每个 request 的条件化干预，不是逐 token 动态 routing，聚类也不能证明得到互相独立的认知能力。库、controller、checkpoint、layer 和强度范围应绑定同一 artifact，不能假定不同 hidden width 间可直接搬运向量。

条件化选择把固定向量的校准问题转为建库、候选组合搜索和 controller 训练问题，并未消除这些成本。离线回答生成、过滤、强度搜索、SFT/RL 与部署注入须分别计费；输出 token 变短不证明端到端延迟下降，局部任务还有简单 Top-1 优于组合的 slice。这里只采用 native 配置下的接口分工，不采用未说明跨宽度映射及口径不一致的 transfer 数字，也不把强度或组合当作正确性证据。版本漂移、任务失配或质量/成本未通过验收时，保留固定 vector baseline、降低强度或关闭注入，外部 verifier 与原 sampling budget 仍拥有最终约束。<!-- source-family:SF-2026-ARXIV-2601-09269 -->

### Answer-first 与 Optional Justification

延长或压短推理仍默认先生成过程、后提交答案。如果任务只要求尽早拿到答案、解释可以稍后提供，那么还可以调整输出次序，而不把这项接口选择混同于增加搜索能力。

传统 reasoning decoding 把答案提交排在完整推理轨迹之后，这在 verifier、tool 或后续步骤必须消费过程时合理，却把 answer latency 与解释成本绑在一起。另一条条件分支是先生成并提交 final answer，再按需生成 answer-conditioned justification；训练时还可以 mask answer loss，只对 justification 提供监督。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06165 -->

后生成的解释不证明它忠实反映答案的因果过程，也可能把错误答案包装得更连贯。需要 faithful process、外部 verifier 消费 trace，或任务本身要求显式搜索时，仍应保留 pre-answer reasoning 或把搜索移入可审计的 workflow。该分支优化的是输出接口与延迟，不是凭空获得推理能力。

在转向多条完整轨迹前，还可以让不同模型在一条共享文本前缀上提出局部续写。单模型逐 token 选择最省状态；当模型的 tokenizer 不同，直接对齐 vocabulary logits 不再有明确共同坐标，一个替代分支让各模型先完成到 word boundary，再对同一候选文本分别重新编码与评分。首 token 的 top-1/top-2 margin 只作为是否继续延长局部 span 的代理，低 margin 时在当前词结束后重评分，并以词数上限防止长时间失去交叉反馈。各模型按自己的 token 数归一化 NLL、再取均值，只形成跨模型排序的 heuristic，不使不同 tokenization 变成共同 posterior，也不证明高 margin 对应正确答案。[受限双模型对照](https://arxiv.org/html/2601.06022v1)中固定 pair 在部分数学任务弱于单模型，不能用 oracle 选择的最佳 pair 替换实际部署比较；双份模型状态、候选重编码与同步仍付费，word boundary 对新语言也需验收。延迟或质量收益不稳时，普通单模型采样、独立候选加 verifier 仍然合理。
<!-- source-family:SF-2026-ARXIV-2601-06022 -->

### 多个 Token Draw 也可以只推进一个连续 State

共享文本前缀上的局部续写仍要提交离散 token；如果 runtime 能直接接收输入 embedding，另一条分支是在每步从同一 logits 分布独立抽取 K 个 token，将它们的 embedding 按均匀或模型概率权重聚合，再把这一个向量作为后续推理的输入。K=1 回到离散采样；K>1 改变单条轨迹的状态表示，并没有维护 K 条独立的历史、KV 和答案。[Multiplex Thinking exact-v1 §3](https://arxiv.org/html/2601.08808v1) 的训练对组成该向量的离散抽样动作计算 log probability；由于不同 token tuple 可以投影为同一 embedding，tuple 的概率或熵不能直接解释为连续 state 的密度或熵增保证。

这条路径把 token-wise 探索压入一个状态，却要求内部 embedding 输入接口、匹配的训练/推理路径，并承担投影的信息损失与分布偏移。更多抽样不等于更多 forward，也不等于已经证明墙钟成本不变；作者有限模型与数学任务中，增加宽度收益趋缓，聚合与训练对照也并非逐项占优。接口不可取得、任务质量或端到端成本不稳时，离散单轨迹继续合理；需要保持不同候选的独立可审计过程时，应采用下面的多轨迹采样，而不是把一个混合 state 当成 K 份可选择答案。
<!-- source-family:SF-2026-ARXIV-2601-08808 -->

## Parallel Sampling：先分开 Coverage 与 Selection

延长一条轨迹是在纵向增加 sequential compute；并行采样则在横向生成多条候选，再决定接受哪一条：

```text
prompt + decoding policy
-> N candidate trajectories
-> candidate coverage
-> selector / verifier
-> accepted answer or abstention
```

这条路径至少有两个不同的成功概率。`Coverage` 问正确候选是否出现在集合中；`Selection`
问系统能否从已有候选中识别它。`pass@N` 只能给出前者的上界，不能证明 self-verifier 能达到这个
上界。扩大 `N` 可能提高覆盖率，也会带来更多近似答案、相关错误和选择成本；若 selector 的辨别力
没有同步提高，更多样本甚至可能让最终选择更不稳定。

候选 selection 还可以明确选择后的分布，而不只报告较高 reward。对有限 response support 上独立采自同一 base 的 n 个候选，在每个 reward/λ 上加独立 exponential noise 后取最大，得到的是目标 reward-tilted 分布与残余分布的有限-n mixture；n 有限时不能直接叫精确 tilted sampling。若 noisy score 越过真实 reward 上界导出的阈值，则 hit 分支恰好具有 tilted law；按独立随机顺序扫描并取第一个 hit，可利用 exponential overshoot 的 memorylessness 提前结束评分，无 hit 时仍需完成候选评分与选择。

这些权限依赖有限 support、独立样本/噪声、真实 score 上界与固定评分规则，不是任意 judge threshold 的提前停止保证。加入截断的 draft–target likelihood ratio 会改变目标，更多候选只能缩小有限-n误差，不能消掉 clipping bias；另加 reward gate 或 base fallback 也不自动继承前面的 sampling law。候选若已全部预生成，提前退出省的是 target/reward 评分而非这些生成；受限实验的 token-compute估计与每步墙钟也有不同分母。support、上界或成本不可靠时保留完整候选评价、标准 BoN/target sampling，正确性仍由独立 verifier 验收，不用分布定理证明所有任务质量或免费提速。 [必要机制与反证](https://arxiv.org/html/2609.21899v1)。<!-- source-family:SF-2026-ARXIV-2609-21899 -->

逐 token 温度与完整 sequence 的 power 分布也不是同一个对象。将每个 prefix 的条件概率局部取幂并归一化，会引入随 prefix 变化的归一常数；它不能单独产生按完整路径概率取幂的目标。一个有限粒子分支仍以局部 powered proposal 生成 token，再用增量 importance weight 修正路径，按 ESS 触发祖先重采样。该 proposal 可消除当前 token 选择带来的增量权重方差，却不能消除不同 prefix 路径之间的退化。<!-- source-family:SF-2026-ARXIV-2602-10273 -->

重采样必须同时重排 prefix、KV、weight 与完成状态；EOS 吸收规则和最大长度截断也定义实际支持。[Power-SMC 的有限对照](https://arxiv.org/html/2602.10273v1)不授有限粒子为精确、独立的全目标样本，较高 batch 利用率也不是总 token-evaluations 减少。粒子复制、缓存驻留、ancestor identity 与评价都要计费；权重退化、资源不足或 support 不合适时，普通低温/Top-P、较小候选集合与外部 verifier 仍合理。

这里还要区分三种对象：单条 trajectory 的概率、归一化 answer 的总概率质量，以及有限样本真正覆盖到多少种可用 reasoning path。对 token 分布做全局 power sharpening，可能提高正确答案的理论总质量，却同时压低若干中等概率但互补的正确路径；当最终答案依赖 self-consistency 聚合时，有限样本反而更容易集中到相关错误 mode。因而分布变尖不是单调的质量开关，deformation 参数应按任务与 selection rule 校准，并同时观察 answer accuracy 与 path support。

这条分支以更复杂的 query-local 校准换取更好的 coverage/selection 配合；单样本、分布近单峰或没有轨迹聚合时，低温或普通 Top-P 仍更简单。`arXiv:2608.14420v1` 在作者受测模型与 reasoning benchmarks 上给出固定 exponent 的反例，最高下降 18.5 个百分点，但不证明所有 verifier、search pipeline 或 workload 都有相同失效。

<!-- source-family:SF-2026-ARXIV-2608-14420 -->

多个已训练forward policy也不能每步固定权重平均后，就声称终止对象服从同权重reward mixture。在共享DAG、非负reward和准确component分布/partition下，一条分支按state reaching mass，以v_i u_i(s)/Σ_j v_j u_j(s)混合forward transition；它将局部选择权重与终止目标接起来。[必要线性组成条件](https://arxiv.org/html/2602.21565v1)只在β=1且flows/partition正确时支持精确目标；各component partition估计误差会改变相对权重，不能仅称全局rescale，nonlinear distortion也不保证全support为常数。Training-free只指新composition，base bank训练、每步多模型求值和reaching-state估计仍计费；toy控制不能升为生产SLO。估计失准或费用不合算时保留单policy、直接终止对象mixture或重新训练，正确性仍由独立verifier负责。<!-- source-family:SF-2026-ARXIV-2602-21565 -->

### 提前评价前缀，决定哪些路径值得完成

单条轨迹的 feedback controller 调节继续探索或尽快提交；预算分给多条轨迹后，还需要决定哪些前缀值得支付剩余生成成本。外部 verifier 可以读取文本，接口清晰且不要求修改生成模型，但会重新编码前缀并增加独立模型成本。能读取内部状态时，一个替代分支先由冻结的 generator 生成多条前缀并保留其 KV，再在每个前缀的临时评分分支中追加专用 query token，只在这一步启用评价 adapter 与分类头。评分结束即丢弃临时分支，保留下来的轨迹从原来的前缀状态恢复生成；评价 token 和 adapter 派生状态不成为 base continuation 的已提交前缀。这里的分数估计“给定当前模型、前缀和采样规则后完成正确的概率”，可以用多次 continuation 的成功率训练，却不是证明轨迹逻辑有效的 verifier。

这种状态隔离用新增评分参数、Monte Carlo 监督构造与一次局部 forward，换取少完成一些低价值路径；它没有使评分和训练免费。固定前缀长度会在识别错误的可靠性与已经支付的生成成本之间取舍，错误剪枝还可能删掉后续能自行修正的路径。验收应分别记录初始路径数、保留数、前缀长度、selected-path 平均正确率与最终 query-level success，并把 check、临时 cache、恢复与吞吐影响计入总预算；分数较好、评分时延较低不等于端到端成本一定更低。现有证据支持若干数学、逻辑和受限工具任务的单阶段过滤，不证明经验保留率拟合跨任务普适、attention 图揭示必要推理机制或生产 tail SLO。无法访问内部状态、评价 adapter 漂移或剩余预算不足时，随机保留、固定宽度完成与独立文本 verifier 仍是共存路径。[受限状态隔离与评价证据](https://arxiv.org/html/2604.16029v1)

### 从候选集合到选择状态

前缀剪枝决定是否继续支付生成成本；候选完成后，仍需要决定哪个答案值得交付。两者可以复用评分信号，但不能把“值得继续”直接当成“已经正确”。

旧的聚合方法各自对应不同假设：majority vote 假设正确轨迹形成最大等价类；pointwise scoring
假设每条候选可被独立校准；pairwise comparison 只要求局部判断两个候选的相对优劣。Pairwise
方案并没有消除状态，而是把状态改写为 comparison graph：

```text
candidate id / text / generation config
+ compared edges and judge outputs
+ per-candidate score / degree
+ comparison budget and stopping rule
```

先覆盖低 degree 节点、再比较当前近分候选，是在固定预算内平衡 exploration 与 refinement 的一种
策略；全量 tournament、Swiss-style sparse graph、独立 pointwise score 或 executable verifier 仍是有效
分支。图上分数差只是当前 judge 与拓扑下的排序证据，不是天然校准的置信度。同一模型同时生成和
判分还会产生 correlated error：它可能一致偏爱相同措辞、推理风格或错误假设。因此 self-verification
适合作为 selection signal，不应被写成 acceptance proof；高风险任务仍需要独立 oracle、工具执行、规则
检查或人工升级，所有候选都未达阈值时还应允许 abstain。

Selection 还可以从单条分数推进到 **query-local distribution state**。当同一问题已经产生许多候选时，系统可在该候选集合内拟合置信度分布、识别经验簇，再过滤或聚合；这比固定全局阈值多利用了一层相对结构，却没有创造外部真值。它的状态至少包括：

```text
candidate set and normalized answers
+ confidence extraction rule
+ local distribution model and parameters
+ component identity / fallback policy
+ filtering, voting and abstention decision
```

若分布单峰、样本太少、component 交换，或 temperature、模型和任务发生变化，局部 mixture 会退化；同一个模型产生轨迹又报告 confidence 时，两者还共享校准盲点。因此 majority vote 在答案可规范化且错误较分散时仍然有效，pointwise/pairwise selector 在绝对簇结构不稳定时仍合理，独立 executable verifier 才能把 selection evidence 提升为 acceptance evidence。

候选若先产生视觉 cues、再消费 cues 推理，还可把两阶段的文本 uncertainty 分开：以各段高 entropy tokens 提议局部过滤，再按两段读数及其相对变化聚合答案，而不是用整条 trace 的单一 confidence 覆盖 producer 和 consumer。这里读取的是文字生成概率，不是视觉 grounding 真值；阶段边界、warmup population、阈值与停止规则都需绑定，删掉 cue 可能让后续答案看似更自信却失去依据。[受限两阶段 selector](https://arxiv.org/html/2602.12916v1)的比较还预生成完整 traces，保留 token 数下降不能直接等同实际少做了 producer 计算或改善 tail latency；在线节省必须连同 warmup、工具、已完成与已取消生成一起计账。信号失配、视觉证据冲突或预算不足时，保留完整候选、普通 voting 或外部 verifier，不让阶段 proxy 替代 acceptance。<!-- source-family:SF-2026-ARXIV-2602-12916 -->

### Selector 也要先证明“正确性信号可读”

Majority vote 不只是一个便宜 baseline，它隐含“正确答案比任一错误答案更常出现”。困难问题可能进入相反的
modal-wrong regime：samples 的错误高度相关，增加 `N` 只会让错误 mode 的票数更稳定。Hidden-state selector
提供另一条分支——不根据答案出现次数，而从候选的内部表示读取一个 correctness ranking signal。

但 probe accuracy 很容易被 question identity 泄漏。若同一 question 的多个 candidates 被随机拆到 train/test，
selector 可以学会“这是一道总体很难/很容易的题”，却仍无法在该题内部区分对错。真正与 selection decision 对齐的
measurement 应是：

```text
group split by question
→ rank correct candidates above incorrect candidates within each question
→ compute leakage-free decodability on held-out questions
→ compare expected selector gain against voting / verifier cost
```

只有当这条 within-question signal 在目标 model、layer、task、sampling policy 和 difficulty slice 上稳定可读，才启用
hidden-state selection；否则保留 majority、output-space score、独立 verifier 或 abstain。这个 gate 测的是 selector
competence，不是候选本身的 truth probability，也不能授予最终 acceptance authority。

CASE 的作者实验为这条机制提供了受限证据：answer-token hidden state 的线性 readout 在部分 model/task 上可预测
selection 相对 voting 的收益，而在 signal 近 chance 的设置中不应启用；普通 random split 会显著高估 probe。论文
主要覆盖 multiple-choice、最终 answer token 与可取得 hidden state 的模型，阈值又依赖 difficulty distribution，
因此正文不保留固定 AUC、任务增益或“更大模型必然更可解码”的结论。

这形成一条条件演进，而不是单向替代：

```text
majority under diverse errors
→ semantic / output-space grouping
→ hidden-state selector when correctness is decodable
→ external verifier when acceptance requires truth evidence
```

更多 candidates 只有在 coverage 增长且 selector 可靠时才增加系统正确率；在 modal-wrong 且无可读 correctness signal
时，采样和投票都不能制造新知识。

### 多数票选择的是稳定盆地，不是真值

内部表示无法稳定区分对错时，继续堆采样和投票不会解决证据缺失；另一条选择分支是引入与当前票数不同的外部信号，同时限制它可以改变排序的幅度。

当多条采样轨迹的错误近似独立时，多数票是便宜的 selector；一旦同一模型反复落入稳定但错误的 reasoning basin，票数只测到自洽密度。此时 selection owner 可以在多数证据上叠加一个有界外部证据修正：只有可审计信号足够强才改变排序，信号弱时保留原决定或交给 verifier。收益是避免微弱、噪声证据任意翻转结果；代价是额外 evidence acquisition 与校准，失败模式则是 evidence source 同样相关或被污染。低风险、错误近似独立的任务仍可使用多数票。exact-v1 只在论文测试的数学任务、三个模型族与证据构造中支持这条分支，不证明它是开放域 truth oracle。<!-- source-family:SF-2026-ARXIV-2605-26172 -->

### 统一核算生成、筛选与选择的预算

Parallel sampling 的预算也不能只写“调用次数”。完整 contract 至少包括各候选的 prompt/prefill
复用、生成 tokens、KV 占用、judge 输入输出 tokens、并行度、端到端 latency、成本与停止规则。
一次长 pairwise judge 与一次短 candidate generation 不是等价工作量。Greedy 或单样本在低延迟、低
风险和 selector 不可靠时仍更合理；majority 在可规范化且错误相对独立时仍很有效；pairwise graph 是
当绝对评分困难、又无法承受全量两两比较时出现的中间设计，而不是它们的单向替代。

## 约束输出：合法前缀、完整序列与内容正确

前面的 penalty 与 grammar mask 已足以定义单步选择，但更强的输出要求会暴露三个不同缺口：前缀是否合法、能否在预算内完成，以及完成后的内容是否正确。下面先处理可形式化的输出空间，再检查格式条件怎样改变内容，最后划清风险控制与接受证据的边界。这些条件分支不要求同时启用。

### 大型有限输出集合适合专用 Trie Automaton

当合法输出是一个很大的有限集合时，通用 grammar 每步解析会重复计算，而 trie 可以把共享前缀编成紧凑 automaton，只允许仍可到达某个合法叶子的 token。它以预处理时间和内存换取稳定 decode；集合频繁变化、语义约束开放或 tokenizer 不一致时，专用结构的维护成本会超过收益，应回退通用 constrained decoding 或后置验证。
<!-- source-family: arxiv:2608.12574v1; semantic-body-binding: finite-set-trie-decoding-path -->

### Prefix Feasibility 不等于能在 Token Budget 内完成

有限集合可以沿共享前缀定位合法叶子；对于带嵌套结构的输出，除了“不走入非法路径”，还需要知道剩余预算是否够走到接受状态。

一个前缀仍可扩展为合法输出，只说明没有进入死路；它可能距离 accepting state 太远，最终在 token budget 用尽时截断。带栈约束的解码可以同时维护 PDA reachability 与 distance-to-acceptance，在接近预算时优先选择可完成路径。这样提高结构完成的 soundness，却增加预处理、beam 状态与运行开销，也不能表达所有语义约束；自由文本仍需后置验证。
<!-- source-family: arxiv:2608.28229v1; semantic-body-binding: constrained-decoding-distance-to-acceptance -->

### Stateful Exact Conditioning 是有限状态约束的条件分支

保证最终合法，仍不意味着按照原模型在所有合法完整序列上的条件分布抽样。只有应用需要这个更强分布语义时，才值得承担全局条件化的状态与计算成本。

Rejection sampling 或生成后 repair 在约束稀疏、状态难形式化时最通用，却可能反复产生无效前缀。若约束能编译为冻结、可判定的有限状态 validator，且模型对 prefix 的依赖也能被足够小的状态精确汇总，可以把二者做 product construction，并在可计算未来接受概率质量的条件下精确条件化。合法性 soundness 与保持原模型在合法完整序列上的条件概率是不同保证；仅屏蔽当前非法 token，并不自动实现后者。多个约束会使 product state 乘法增长，模型状态自身也可能无法压缩到可处理规模；约束过大、动态或模型无法满足这些计算条件时，应回退 grammar mask、rejection 或生成后验证，不能把局部 validator 当作开放语义正确性证明。

<!-- source-family: arxiv:2608.08282v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: finite-state-exact-conditioning-product-cost -->

约束语法简单，也不意味着全局条件概率容易计算。对一类描述长度有限、每步 next-token 概率可在多项式时间精确计算的自回归模型，即使约束只是“固定长度后以 eos 结束”，合法序列的总概率质量也可编码满足赋值计数，因而其精确计算是 #P-hard。困难在未来所有 suffix 的模型概率，而不只在 validator 有多少状态。有限状态 Markov 模型配合有限状态约束仍可用动态规划；一般 prefix-dependent 模型则需要另证模型状态汇总与 continuation mass 的可计算性。这个计数复杂性反例不证明每个具体模型都很难，也不证明任何可能的 exact sampler 都必须显式计算归一化常数；它限制的是通用、可高效的全局条件化保证。<!-- source-family:SF-2026-ARXIV-2604-07855 -->

### 格式损失要先定位在 Prompt，还是 Decoder

即使结构约束的计算已经正确，内容质量也可能变化。此时先区分模型收到的条件与 decoder 执行的屏蔽，才能判断该改 prompt、生成流程还是 sampler。

Grammar mask 只约束候选是否合法；要求模型同时解题并输出特定格式，也会在屏蔽 token 之前改变条件分布。因此不能把结构化输出的质量下降全部归因于 decoder。最低比较应固定任务和模型，分开自由输出、仅在 prompt 请求格式、相同 prompt 再启用 mask 三条路径，并分别测格式合规与内容正确。解析更成功，不等于推理更准确。

若格式只是答案的呈现方式，可尝试先自由生成答案，再用第二次调用重格式化；这与单次生成内先 thinking 后输出是不同分支。分离可能恢复内容质量，却增加调用、tokens、延迟和重格式化改错的风险，仍须核验答案是否保留。格式本身编码正确性时——如代码、测试或 tool arguments——不能照搬这项呈现格式实验来放宽约束；第 78 章继续拥有参数语义和执行授权。低延迟、简单抽取或已能稳定兼顾格式的模型，单次生成与 grammar mask 仍成立。

上述[受限证据](https://arxiv.org/html/2604.03616v1)并未证明格式请求必然有害、thinking 必然补偿损失，或某种闭源训练机制造成鲁棒性；它新增的是先分清损失发生位置，再选择干预层的评价分支。<!-- source-family:SF-2026-ARXIV-2604-03616 -->

### Grammar 放行的 Schema Key 仍是语义条件

区分 prompt 与 decoder mask 还不够：合法 schema 中的字段名会进入自回归输出的 prefix，影响后续内容分布，不只是 parser 的占位符。因此即使字段数、顺序和 grammar 不变，rename 也不是内容语义不变操作。可以分别比较语义提示只在 prompt、只在 key、两处都有或都没有的四配置，并将 prompt wording、schema wording、grammar/tokenizer 与 parser/字段映射共同冻结，分别验格式和内容；这不是等 token 长度或任意字符串语义等价的证明。

命名提供低成本的 instruction channel，却引入模型依赖、重复提示竞争及接口版本/下游映射成本。`arXiv:2604.14862v1` 在七个 Qwen/Llama 变体、GSM8K/Math500 与固定 XGrammar 下观察到 key-only 退步、两处并用也非普遍加成；不能推出通用最佳命名、恶意注入防御或未披露的硬件/并发 SLO。接口兼容优先或效果不稳定时，标准稳定 key、prompt-only 说明和独立内容验证仍成立；tool arguments 的实体/字段语义与执行权限继续由第78章拥有，parse 通过不批准动作。

<!-- source-family:SF-2026-ARXIV-2604-14862 -->

### 从固定 Logit 变换到 Sensor-gated Safety Decoding

格式与字段名能够约束或引导输出，却不能表达所有行为风险。若风险只在生成途中显现，可以考虑随轨迹变化的干预强度；其信号仍须与安全保证分开。

<!-- semantic-body-binding:SF-2026-ARXIV-2602-02027:start -->
固定 safety mask 或 request-level guidance strength 在风险边界稳定时最简单，但它无法适应风险在生成轨迹中途才出现的情况。一条实验性分支同时保留 base 与 safety-expert 分布，以二者逐 token 的差异作为 risk sensor，经 temporal accumulator 判断风险是否持续，再只在触发时对 union Top-k candidates 做分布插值后提交 token。prompt-level self-reflection 决定一次请求的 intervention strength，token-level disagreement 决定当前 step 是否介入；两者是不同状态，不能合并成一个“模型知道自己危险”的置信度。

这仍只是 sensor-driven logits policy，不是事实或安全 authority。专家差异可能来自无害的能力偏差，累积阈值可能漏掉单步危险 token，gate 漂移又会造成过度拒答或漏防；safety expert 还带来额外计算。`base/safety checkpoint / risk dimensions / accumulator / threshold / candidate-set rule / judge version` 必须共同版本化并在 false refusal、未见攻击与 utility 上校准。公开实验使用特定模型、安全/效用 benchmark 和 GPT-4-Turbo judge，只能证明该条件化分支在这些设定中的行为，不构成生产安全保证。弱 alignment、分布外攻击或 gate 失配时，grammar constraint、tool authorization、外部 policy 与 release gate 仍必须保留。
<!-- semantic-body-binding:SF-2026-ARXIV-2602-02027:end -->

### Anchored Decoding 把版权风险编译为序列信息预算

逐步干预还可以由显式序列预算驱动，而不只由风险传感器触发。下面的预算约束针对可测的逐字复现风险，不能与前面的计算 token budget 或通用安全判定互换。

仅在输出后查找相同片段，无法阻止高风险 LM 在生成过程中已经进入逐字复现路径。Anchored Decoding 保留原模型的 proposal，同时引入只用宽松许可数据训练的 reference distribution，把用户选择的 sequence-level information budget 分配到每个 token step，只提交满足局部距离约束的候选。跨 tokenizer 组合时，byte-level fusion 也必须成为 sampler identity 的一部分。

这条路径降低可测的 verbatim-copying 风险，代价是双模型执行、词表对齐、utility 损失与 reference model 本身的数据边界。它不是法律合规证书，也不覆盖意译、情节或外部检索泄漏；当 reference 不可信、budget 无法校准或 exact sampling 是必要语义时，回退固定 decoding、输出检查与人工版权复核。<!-- source-family:SF-2026-ARXIV-2602-07120 -->

### Accepted-generation Risk 需要 Chance Constraint，不是 Confidence Threshold

上述约束改变允许生成什么，却没有自动规定何时有足够证据接受结果。若目标是控制已接受输出的失败风险，必须另行定义随机约束、证据累积方式与拒绝路径。

当同一接口被反复调用时，降低平均幻觉率不等于控制“已接受生成中的失败频率”。一条更强的提交路径把每次生成视为随机约束试验，以 sequential，anytime-valid 证据逐步判定当前输入是否达到了预设的 chance constraint，然后再 accept、defer 或宣告不可行。这与按 confidence 排序不同：后者可以提升选择后质量，却不自动给出概率风险边界。

该分支以多次采样成本、constraint scorer 误差和独立/相关性假设换取可组合的风险控制；输入分布、scorer 或采样假设偏移时，证书不得继续流用。低风险且延迟敏感的请求仍可使用固定 decoding 或普通 selective prediction；公开证据只支持作者的 QA、多跳任务与披露采样协议，不证明生产幻觉率上界。<!-- source-family:SF-2026-ARXIV-2602-01637 -->

## Sampling 不能修复模型能力

降低 temperature 可以让高概率行为更稳定，但若正确答案本来概率很低，它不会创造知识。提高 temperature 可能偶尔采到正确答案，也会增加错误候选。

同样，top-p 只重分配已有分布，不判断事实正确性。Sampling 调整的是 capability 的表达与轨迹，不替代数据、训练、retrieval、tool 或 verifier。

## 工程与评估含义

这些分支最终都要回到同一评估对象：模型与完整生成策略的组合。先核算质量、风险和成本，再区分改变分布的策略优化与保持分布的执行优化。

生成配置应与模型版本一起评估：

- 单次成功率与 pass@k 回答不同问题。
- 平均质量会掩盖 seed 与长尾波动。
- 输出长度影响 latency、KV Cache 和成本。
- 结构化任务要测解析成功与语义正确。
- Agent 任务要测错误 action，而不只最终文本。

Sampling kernel 可以在 GPU 或 CPU 执行，是否成为瓶颈取决于 vocabulary、batch、约束复杂度和数据传输。本章不进入 scheduler 层。

### 保持分布不变，也可以改变 Logits 的物化边界

经典路径先写出完整 `[B,V]` logits，再执行 temperature、mask、normalization 与 sampling。它最容易
组合任意 logits processor、返回完整 logprobs 并进行调试；在大 batch 的 compute-bound GEMM 中也可能
最有效。小 batch、large vocabulary 的 decode 则可能受 logits 写回 HBM、再次读取和多次 kernel launch
限制。

对 categorical sampling，Gumbel-Max 允许逐 tile 计算 `logit + noise`，只保留局部最大值并最终归并，
从而把 LM head 与 sampler 融合而不物化完整 logits。Tensor Parallel 下还可先在 shard 内归约，再按
group probability mass 做层次采样。只要 mask、temperature、RNG 与归并保持同一数学分布，这改变的是
执行计划而不是模型 sampling policy。

代价是 processor order、RNG determinism、shard identity 与 kernel layout 被更紧地耦合；需要完整
logprobs、复杂 grammar、不可融合 processor、跨重试可复现或高 batch GEMM 占优时，物化 logits 仍更
简单。某一 revision 的 kernel speedup 不能外推到不同 vocabulary、batch、hardware 或 processor chain。

## 本章在知识树中的位置

本章闭合一个 token 的生成循环。[第 31 章](../part-04-training-system/31-rlhf.md)及其后的算法章节会说明 rollout sampling 怎样
进入 preference optimization，[第 44 章](../part-05-inference-system/44-decode.md)说明在线 Decode 怎样执行 token 决策，
[第 48 章](../part-05-inference-system/48-speculative-decoding.md)则要求 exact speculative decoding 保持同一 target sampling 分布。

[第24章](../part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)拥有另一条分支：当生成状态允许 masked refinement 或 retroactive editing 时，sampler 不只选择“下一个 token”，还要选择哪些 provisional positions 可修改、何时 commit。该分支可能改变输出分布；只有带正确 acceptance rule 的 speculative verification 才能声称保持 target distribution。

到这里，第 11～20 章的顺序主干已经闭合：文本变成 token ids，ids 变成带位置的 hidden states，Transformer 产生 logits 与 KV state，Sampling 选择 token 并把它追加回前缀。接下来的[第 21 章](./21-moe.md)和[第 22 章](./22-long-context.md)不是 Sampling 之后的新步骤，而是回到这条主干内部，分别讨论参数容量和序列容量怎样扩展。

## 自检问题

1. Logits 与 probabilities 有什么区别？
2. 为什么 softmax 可以先减去最大 logit？
3. Greedy 为什么不保证整段序列最优？
4. Temperature 是否改变 token 排名？
5. `z=[2,1,0]` 时，较低 temperature 如何改变概率？
6. Top-k 与 top-p 的候选集规则有何区别？
7. 为什么 logits processor 顺序会影响结果？
8. 固定 seed 为什么仍不保证跨 runtime 完全复现？
9. EOS 与 stop string 分别在哪一层工作？
10. 为什么 Sampling 不能替代模型能力提升？
11. 为什么 `pass@N` 不能直接代表系统最终答对的概率？
12. Pairwise selector 需要持久化哪些 graph state，为什么 score difference 不等于置信度？
13. 为什么 selector 的 calibration 必须按 question 分组并测量 within-question ranking？
14. 合法前缀、预算内完成、保持条件分布与内容正确分别需要什么保证？
15. 前缀剪枝的临时评价状态为什么不能直接进入保留路径的 base continuation？

## 小结

Sampling 将模型给出的条件分布变成一条实际 token 轨迹。Greedy 选择局部最大值，temperature 改变分布锐度，top-k 固定候选数量，top-p 根据累计质量动态截断。

这些选择会在自回归循环中持续改变后续状态，因此必须与模型、prompt、seed、停止条件和 Evaluation 一起版本化。Sampling 控制能力如何表达，不创造模型没有的能力。

## Review notes

- `SF-2026-ARXIV-2602-21565`：exact-v1 §4与线性证明，shared DAG/nonnegative/true reaching mass和partition条件；隔离estimated Zi全局rescale说法，不采用科学应用或生产保证；未复现。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。

- `SF-2026-ARXIV-2602-18292` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18292v1) §4.3/Eq14–23、§4.4/Table1–3。2+1+2=5，K-draw局部tokenhit效用与迭代q求解差额深入；proxy/未披露K与weight、token≠完整解答coverage、低温反侧及steps/time非SLO近正文。root必要源/actualowner PRE通过并授窄锁；作者实际正文/完整邻接及自身末注顺读、限定diff-check通过，root非作者实际正文/完整邻接及自身末注POST通过，锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2604-16029` — [Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning v1](https://arxiv.org/html/2604.16029v1)，Daily `2026-04-20`。采用 §3.2/F.2 的冻结前缀、临时 STOP/LoRA 评分分支丢弃后恢复 base continuation；MC32 标签是模型/解码条件成功估计，非逻辑 verifier。F.2 单 H100/7B/batch16/prefix2048 总时长34.33s大于33.20s、吞吐−2.71%及监督构造成本保留，不采零开销/普适保留率或 tail SLO。apr02 已实际必要源→当前 owner/literal 独立通过（`V3_APR02_LATEST_FIVE_16022_16044_INDEPENDENT.md`）；作者在 root 窄锁内落实两段，root实际顺读真实正文与相邻写后PASS（`V3_STOP_OWNER_PROPOSAL.md`末），真实整合；非整个日Gate。

- `SF-2026-ARXIV-2604-14862` — [Schema Key Wording v1](https://arxiv.org/html/2604.14862v1)，Daily `2026-04-17`。采用 §3.1–3.4/4.1/Table1/3 的 key-prefix 语义通道及None/Key/Prompt/Both四配置；不声称等token长度、普遍最佳key或projection定理。复用 apr01 必要原文/当前owner PASS（daily-20260417/v3-reopen-notes.md「新收到三项非作者source→owner」）；root已实际顺读正文与两侧/复用有效必要证据后写后独立PASS；真实整合，本批章锁释放。

- `SF-2026-ARXIV-2604-07855`（Status: Theoretical）：[exact-v1](https://arxiv.org/html/2604.07855v1) §2 的 succinct rational next-token 模型、§5 Theorem2 的 `Z=#SAT/2^m` 构造、§8 有界模型状态与 validator product。正文补齐有限 validator 并非充分计算条件，不采用 Corollary2 对任意 exact sampler 的更强推断；无硬件/吞吐/SLO实验，不伪造性能收益。6分因修正既有条件缺口深入，root 已独立核必要原文与实际正文，通过。

- Light Alignment / neuron-gated safety decoding（Status: Experimental）:
  https://arxiv.org/abs/2602.02027

本轮联章 Review 明确本章是 token 生成主干的闭环点，第 21～22 章属于回看主干的容量扩展。正文仍以固定 logits 完成 temperature、top-k、top-p 的数值比较，并明确 processor 顺序和 seed 的实现边界。RLHF/SFT 属于 Part IV，batch scheduling 属于 Part V，不在本章展开。

2026-W10 的 V1 案例用于补全 parallel coverage 与 selection 的分层、comparison-graph state 和
self-verifier 的相关错误边界。正文只保留这种长期 contract；作者任务分数、固定候选数和“线性 calls”
不作为跨 workload 性能结论。

DistriVoting 用于补足 query-local mixture state、component-identification failure 与“内部 confidence 只能支持 selection”的边界；其两分量假设、128-sample 预算和数学题结果不作为通用配置。

Primary-source 校验入口：

- Angela Fan, Mike Lewis, Yann Dauphin, "Hierarchical Neural Story Generation", 2018: https://arxiv.org/abs/1805.04833
- Ari Holtzman et al., "The Curious Case of Neural Text Degeneration", 2019: https://arxiv.org/abs/1904.09751
- Niklas Muennighoff et al., "s1: Simple test-time scaling", 2025（Status: Experimental）:
  https://arxiv.org/abs/2501.19393
- Zihan Wang et al., "V1: Parallel Generation and Pairwise Self-Verification", 2026（Status: Experimental）:
  https://arxiv.org/abs/2603.04304
- Believe Your Model / DistriVoting（Status: Experimental）: https://arxiv.org/abs/2603.03872
- CASE / Decodability（Status: Experimental；hidden-state selection admission gate）:
  https://arxiv.org/abs/2608.17124
- FlashSampling（Status: Experimental；exact fused sampling 与 TP hierarchical reduction）:
  https://arxiv.org/abs/2603.15854
- The Format Tax（Status: Experimental；`arXiv:2604.03616v1`）：
https://arxiv.org/html/2604.03616v1 — §3–7、Table 5、Appendix G/I。六个 3B–32B 开源模型、四个 API 模型，数学/选择题/写作及四种呈现格式；同 prompt 的 GCD 对照支持分离上游条件与 token mask，不支持内部因果机制或工具参数/代码正确性外推。数学/写作采用 LLM judge，thinking 有退步例，两调用增加成本；生产 hardware/precision/concurrency/SLO=`Not Disclosed`。本文未复现作者代码；根任务已独立重开 exact-v1 并对读相邻正文，完成本项采用与写后复核，不代表整日报 Gate 通过。

- `SF-2026-ARXIV-2601-06022` — Daily `2026-01-13`；[AdaFuse exact-v1](https://arxiv.org/html/2601.06022v1) §3–4。原评分保持，具体owner差额深入；仅采用word boundary、first-token margin与跨tokenizer meanNLL heuristic；固定pair反侧及双模型成本，不授通用性能/安全保证。未运行代码或复现实验；root实际必要原源/现owner写前核通过并授窄锁；root实际正文/前后邻接及末注非作者POST通过。

- `SF-2026-ARXIV-2601-08808` — Daily `2026-01-15`；[Multiplex Thinking exact-v1](https://arxiv.org/html/2601.08808v1) §3、§4、§5/Tables2–4。2+2+2=6，连续状态 owner 缺口深入；采用 token tuple→单 embedding/state 与投影概率边界，不采用投影熵增、普遍质量或零端到端成本保证。未核代码或复现；root 必要原源/owner 写前核通过，root 实际正文/前后衔接及末注非作者 POST 通过，日级 Gate 未授。

- `SF-2026-ARXIV-2601-09269` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09269v1) §3–5/Algorithm1、Appendix C/D/E。6分 prefill-once selection/strength 双头与静态 decode 组合具体差额深入；不授逐步路由、独立认知能力或未明异宽 transfer，Top-1 反侧、离线库/search/RL 成本与无注入/vector baseline 相邻。root 必要原源/owner 写前通过，root 非作者实际正文/邻接与末注 POST 通过，窄锁释放；未运行代码或复现。

- `SF-2026-ARXIV-2602-10273` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10273v1)，必要方法/关键评价/直接反侧见本日 V3_EVIDENCE_SIX；2+1+2=5，具体owner差额深入。只采用token温度与sequence power目标/增量weight/ESS祖先KV身份，有限粒子不授精确全目标/少compute。root实际必要原源与current owner/邻接PRE通过；root实际正文、前后邻接与末注非作者POST通过，窄锁释放，日级未授；未运行代码或复现实验。

- `SF-2026-ARXIV-2602-13935` — Daily `2026-02-18`；[exact-v1](https://arxiv.org/html/2602.13935v1) §2–3/Algorithm1/Proposition2.1、Table3、Appendix C。2+1+2=5，具体停止风险owner差额深入；只采用完整trace最大值校准的交换性/fixed-statistic边界，wellposed误停不等答案correctness风险，OOD/无signal/bin成本与EOS/硬预算回退相邻，renewal/Šidák仅近似。root必要原源与实际owner/邻章PRE、实际正文/完整邻接和末注非作者POST通过，锁释放；未复现代码或实验，不代表日级验收。

- `SF-2026-ARXIV-2602-12916` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12916v1) §3、Table4/关键配置。2+1+2=5，cue producer/reasoning consumer 的分段 uncertainty proxy 差额深入；不授视觉 truth，pre-generation 保留总费用，不把 retained tokens 等同实际计算或 tail latency。root 必要原源/actual owner PRE 与实际正文/完整邻接/末注非作者 POST 通过，锁释放；未核代码或复现，非日级验收。
