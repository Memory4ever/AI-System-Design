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

上面的完整 softmax 是目标分布，不要求每种实现都先形成完整 logits。若为了减小词表头的读取量，先按簇抽取一个候选集合，再只对集合内 token 归一化，就必须区分“每个 token 都有机会入选”与“仍按原分布抽样”。令 `S` 为随机候选集合，最终边缘分布是 `q(t|h)=E_S[q(t|h,S)]`；全词表非零支持并不单独保证它等于 dense softmax。Greedy 检索遗漏最高分 token，或随机集合改变归一化分母，都会改变 next-token 的决策语义。<!-- source-family:SF-2026-ARXIV-2603-14591 -->

这是一条以离线簇索引、候选读取与近似误差换资源的分支，不是 top-k/top-p 的等价实现。[受限词表头实验](https://arxiv.org/html/2603.14591v1)只在已披露模型、batch1 RTX3500Ada 条件下显示任务均值与端到端延迟取舍；head 加速不能代替完整模型收益，概率任务的 Monte-Carlo 估计与零概率修补也不是精确 likelihood。需要原分布、严格复现、罕见 token 覆盖或大 batch 吞吐时，应保留 dense 路径，或另作分布误差与实际成本验收。

抽样结果若不是精确onehot，而是若干相邻坐标的混合，词表顺序也会进入下一步的语义载荷：可按embedding邻近性重新排坐标，再以低阶多项式压低残余混合，最后仍由对应embedding表消费。[受限近似采样分支](https://arxiv.org/html/2510.12343v1#S3)要求采样坐标、token ID映射与表行一起绑定，不能只改一个数组顺序。其实际实验为plaintext，不是密文执行、隐私部署或HE净速证明；honest-but-curious也不覆盖恶意参与方。邻近cosine不是所有语义的metric保证，未闭多项式/误差式不补完整recipe，额外LoRA改变分布亦须分账。全词表两两比较/重排、适配、后处理及加密执行的独立验证都计费；映射、质量或实际加密费用不合时保精确onehot/普通采样及可信映射，不由较低邻居误差批准原分布不变、内容保真或机密性。

<!-- source-family:SF-2025-ARXIV-2510-12343 -->

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

截断预算也可以约束候选重新归一后的随机性，而不只固定候选数或保留mass。一条[受限熵预算分支](https://arxiv.org/html/2509.02510v1)先声明当前分布p，再要求候选内条件分布q的熵不超过αH(p)，并尝试保留较大原概率质量；按概率降序加入token、下一项会超预算时停止，只是一种prefix贪心，不是任意子集的全局最优。对严格正概率的有序前缀，新增较小概率项会增加条件熵；mask、浮点零、空集或已确定分布需另定guard，不能直接继承严格增长或提前终止保证。词表支持、temperature、候选归一与实际sample顺序必须一起冻结，先限制top-N再算熵也不是原完整分布的同一量尺。熵只描述该模型的抽样随机性，不是事实confidence或文本连贯真值，部分任务和人评仍会退步；完整概率读取/排序、entropy计算、可能的host同步与参数搜索都付费。分布、质量或净时延不合格时，保留普通top-k/top-p、已验temperature或greedy并独立检查任务结果，不由更低熵批准正确、安全或免费生成。

<!-- source-family:SF-2025-ARXIV-2509-02510 -->

候选集合还可由离线参考token的统计来收窄，而不把高不确定性一律解释为应多探索：在固定模型、温度与logit处理下，按最大概率bin和rank统计teacher-forcing参考匹配率，再供动态rank上限或概率cutoff消费；低confidence处直接greedy是另一条不依赖该校准表的策略。[Correctness-first的受限对照](https://arxiv.org/html/2510.05987v1#S3)支持比较这些截断分支，却不让单一参考措辞的匹配率变成语义正确概率，gold-prefix统计也不自动迁移到自身错误prefix。Bin内均值乘积、稀疏零值与最大合格rank的处理须独立核对，不能由较好拟合宣布每个保留token安全；固定正斜率映射本质仍是概率阈值，不是在线语义verifier。闭答案多数票的收益与代码pass@k/创意质量不同，局部也有反退。参考/teacher制备、校准与阈值搜索、全vocab处理、全部样本/投票及独立答案核验均费；参考支持、温度或任务目标失配时，保原top-k/top-p、greedy或更宽独立候选，不由低confidence强制选择认证正确、安全和净降费。

<!-- source-family:SF-2025-ARXIV-2510-05987 -->

下一token也可由同一prefix下的多份条件logits合成，而不只过滤单一分布。例如给同一模型不同persona及neutral条件，按各路径confidence重权后再softmax；这增加的是条件前向，不等独立agent已有不同观察。尤其max-probability接近不代表token分布一致：两路径都以0.9押不同token，标量confidence仍相同；logit求和还改变有效temperature，权重可能为负时更不能叫凸共识。[CHOIR的有限对照](https://arxiv.org/html/2510.22475v1)支持局部多条件解码选择，未证互补知识或公平性根因。所有路径/KV、权重和采样顺序都计费，条件改变语义或质量/预算不合时保neutral单路径与已验采样，不让标量一致性认证答案正确。
<!-- source-family:SF-2025-ARXIV-2510-22475 -->

## Logit penalties 与约束的边界

Top-k 与 top-p 依据当前分数删减候选；如果任务还要求减少已出现内容的重复，或只允许合法格式，就需要把历史与任务约束也带入这一步。

Repetition、frequency、presence penalties 会根据已生成 tokens 修改 logits；grammar-constrained decoding 会屏蔽不符合语法的候选。

它们都发生在 token selection 层，却解决不同问题：penalty 是启发式偏好，grammar mask 是硬候选约束。它们可能改善格式或减少重复，也可能屏蔽正确 token。

候选删减也可能由学得的语言线索触发，而不来自确定grammar：冻结base，先用norm调整后的候选自蒸馏文字系统标签，再让hidden-state gate按当前分数与历史标签提议mask。[LCG的受限分支](https://arxiv.org/html/2510.17555v1)把软诊断接到硬支持集删除，因此gate错一次就可能让原本合法token不可达；script family不等语言，更不等当前语义应使用哪种语言。Symbols、低资源与低置信例外、合法code-switch及与top-k/top-p的处理顺序须明确，不能把norm当作全部混淆原因。Gate训练、逐token读取/候选处理及所有语言、代码和切换场景回归均计费，冻结base不保原输出law或任务分数；局部干预也确实会压低自然切换并损害代码成功。分类、支持或效用失配时，关闭gate、保更宽候选与原processor配置，不让较少语言混淆签发保义、全语言覆盖或安全解码。
<!-- source-family:SF-2025-ARXIV-2510-17555 -->

重复惩罚还须检查它能否跨过sampler的锁定门槛：声明的top-p规则在π>1/2且loop token概率q≥π时只留该token，后加temperature已不能打开出口；有界penalty只抬高这一门槛。DRY的breaker既截match又免罚自身，因而带短breaker-free片段的循环可让本应增长的惩罚封顶；[受限DRY-C分支](https://arxiv.org/html/2610.24715v1#S6)另按跨breaker recurrence计数，却仍被有限lookback封顶。未锁也不等预算内逃离，理论只解释verbatim loop已开始后的持续，不解释起因或near-loop。窗口/顺序、全采样与任务回归都收费，跨breaker惩罚也会伤合法复述、JSON或覆盖；需求允许重复或副作用不合时保较弱惩罚、显式长度预算与独立任务检查，不由少循环批准内容正确或无条件终止。
<!-- source-family:SF-2026-ARXIV-2610-24715 -->

循环也可先作内部诊断，而不直接修改 logits：将逐句 last-layer hidden 汇聚后交给线性 probe，再以正常样本校准的 CUSUM 阈值和 persistence 检查持续异常。反复的高 entropy reflection 可能早于可见文本重复，但 sensor 只提议风险；它不是 repetition penalty、已验缓解器或生产输出门禁，相关 hidden 特征也不证明真实吸引子因果。<!-- source-family:SF-2026-ARXIV-2601-05693 -->

[受限循环样本对照](https://arxiv.org/html/2601.05693v1)每模型使用平衡的至少50循环/50正常样本，不恢复自然 rare-loop 人口；EDR约.64–.76仍伴FPR约.24–.34，提前40–50句/约1500tokens不等于在线latency SLO。Probe训练、白盒读取、校准与误报复查付费；迁移失效或误报不合算时保留原采样、启发式penalty与可见重复检查，不让内部sensor自签停止或安全。

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

参数的顺序固定后，数值本身还可以由一个独立的学习控制器决定：先保持基座权重冻结，读取当前 prefix 的 hidden state、logits、长度和 entropy，再为下一步提议 temperature 与 top-p。小型 policy 在有界动作区间内调节采样分布，而不是生成新知识或取代原 grammar、停止与资源约束；基座没变也不意味着输出分布没变。训练这份 controller 可以使用完整回答的任务 reward，部署时则按不断变化的 prefix 执行已学策略；状态自适应不等于一条线上轨迹中持续更新参数。<!-- source-family:SF-2026-ARXIV-2603-18428 -->

[受限摘要任务对照](https://arxiv.org/html/2603.18428v1)只将这种接口与 greedy、单一固定温度比较，组合 reward 上涨不证明事实正确、更好的参数搜索已被排除或学习始终稳定。Hidden/logit 特征、逐 token controller、离线生成和 reference 评价均有成本；controller、特征编码、动作边界与 processor 次序也须同 decoding config 一起版本化。信号不可得、任务迁移失配或质量/完整成本无净收益时，关闭 controller、回固定 temperature/top-p 或 greedy，并用独立任务评价，而不让可回退的参数接口自签安全与零开销。

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

Token采样随机也不保证语义选项均匀：可先生成中间字符串，再以显式hash或sum-mod映射为离散选项，把语义分布接口从原token概率中分离。[SSoT的受限构造](https://arxiv.org/html/2510.21150v1#S3)需要条件字符概率界/实际随机选取的通用hash，或sum-mod所需的独立源与谱条件；任意LLM自选hash不能继承保证，T0字符串的压缩复杂度也不是真随机熵。有限选项与模型对照不授密码随机或普遍语义公平，额外字符串/推理tokens、映射及分布校准均付费。随机源、映射或目标分布不可靠时，保外部PRNG、受控sampler和固定选项接口，不由一个较均匀直方图批准跨任务的独立随机性。

<!-- source-family:SF-2025-ARXIV-2510-21150 -->

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

预算决策还可以放在长推理之前：先生成直接答案，再由评分器估计当前答案是否需要升级到CoT；这与在一条已开始的轨迹中提前停止不同。[Confidence-gated CoT的受限对照](https://arxiv.org/html/2510.21007v1#S3)把直接答、评分和升级后重答分成三个调用，阈值依验证人口与模型校准，不能把口述confidence当正确概率。局部质量/平均token取舍不保证尾延迟、最坏预算或换域后相同漏放率；不升级的错误也须单独计入。完整账包括首次直接生成、评分、被升级样本的完整推理及独立校准，而非只算最后留下的答案。分数、人口或预算失配时，保固定受控预算、可信verifier或明确拒答，不由较少CoT调用批准答案正确或省掉评分成本。

<!-- source-family:SF-2025-ARXIV-2510-21007 -->

### Test-time Budget 是 Runtime Policy，不是免费能力

Reasoning model 让停止条件进一步变成 compute policy：runtime 可以在达到上限时硬性停止生成，也可以注入结束标记，尝试把 thinking 通道切到 answer；后者不保证后续不再出现 reasoning-like 续写，阻止结束标记再次出现也不等于停止这种行为。反过来，模型过早结束时，可以抑制 delimiter、追加 continuation cue，再给它更多 token。
这类 budget forcing 证明“生成长度”可以成为可控变量，却不证明更多 token 必然提高质量，也不能仅凭文本 phase 标记推断不可直接观察的内部推理状态。[受限行为与干预证据](https://arxiv.org/html/2609.03633v1)

它把旧的自然 EOS 行为换成显式 sequential-compute budget：获得 capacity planning 与质量/成本
曲线的可控性，同时引入 forced continuation 的分布偏移、重复或错误推理、tail latency、KV
增长和被截断的 final answer。普通 EOS 在短任务、低延迟或模型已能可靠停止时仍更合理；并行
采样与 verifier 则用多条轨迹换取鲁棒性，和延长单条轨迹不是同一种 scaling。生产记录必须把
`reasoning budget + stopping policy + model/runtime version` 绑定到同一 evaluation subject。

名义上限相同，也不意味着模型实际使用了相同推理预算：同一道题加入无关长前缀、换成第二轮或嵌入子任务，可能改变模型自主结束thinking的行为。因此还应把context条件、turn位置、子题分摊规则与实际生成/验证行为写入评价身份，分别检查最终质量和完整Prefill/Decode费用。[受限context对照](https://arxiv.org/html/2604.01161v1)观察到verification文本与生成长度变化，同prefix末段重采样支持有限stop差额，却不证明质量变化全由少验证造成；个别模型/条件也生成更长，子题token除二不是同单题budget。无关前缀本身增加Prefill，较短trace不自动节省总成本，外层cap和deadline仍保留；条件变化或质量退步时应回到原单题/turn人口与独立答案验收，不把compaction或继续生成视为已经验证的修复。<!-- source-family:SF-2026-ARXIV-2604-01161 -->

长度控制还可以在多轮候选之间进行，而不直接干预正在生成的轨迹：在prompt中给出软步数上限，每轮采样后选一个答案，只对给出该答案的候选统计长度；将跨轮答案一致性与条件长度统计对约束的响应共同用作下一轮收紧或放松约束的proposal。[受限跨约束搜索](https://arxiv.org/html/2509.06174v1)用最短值、下四分位和中位数的组合及有限patience容忍偶然不一致，但它们描述的是被选答案人口，不认证答案真值或找到了最短正确链；稳定错误多数也能持续一致，软步数也不是外层硬token cap。约束变化未有单调正确性保证，原history、边界与跨轮置信保存未闭，不补成可执行最优二分配方。应绑定每轮prompt/约束、候选、答案规范化、样本分配和停止规则，另验最终质量；最终或正确人口的链长不等全部搜索费用，所有轮次的prefill、失败候选、串行等待、聚合与独立核验均计入，有限数学反退不由较短输出抹去。信号不稳、错误一致或全费不合算时，保留较松候选、固定self-consistency/BoN和独立verifier或Unknown，外层deadline仍约束整个搜索，不由patience耗尽自动批准正确提交。

<!-- source-family:SF-2025-ARXIV-2509-06174 -->

逐 token 的长度预测还可以采用与答案效用分开的监督目标。对固定生成 policy 采得的长度为 $L$ 的轨迹，在位置 $t$ 为每个非终止步赋负成本 $-(1-\gamma)$，可直接构造 $G_t=-(1-\gamma^{L-t})$，再用带标量 head 的预测器回归其条件均值。它无需额外人工长度标注，却仍要支付完整 rollout 与预测器训练；实现的 $G_t$ 越接近零，表示该样本剩余步数越少，不能把长度 value 解释为答案正确率或任务价值。折扣将不同长度压到有界区间，也会压缩长尾分辨率；未来结果相关的重加权还会改变所学条件目标。<!-- source-family:SF-2026-ARXIV-2604-27039 -->

这项预测也不是未经校准的容量承诺。对一个样本的 $G_t$ 取逆可恢复剩余长度，但对其条件均值取逆通常不等于剩余长度的条件期望，因而不能直接拿它替换调度器的平均长度预算；模型、生成 policy、终止与截断规则改变后，应重新验证预测误差。将候选下一状态送入预测器还增加 forward 成本，较短生成不自动意味着较低总时延。[固定policy监督与受限长度对照](https://arxiv.org/html/2604.27039v1#S3)只支持这一额外长度信号分支，不授已验证的RL优化或服务SLO；精确控制公式与收益归因尚有原文符号争议时，保留自然EOS、硬长度/deadline预算和独立答案验收。

文本信号还可以定义一种不同于答案正确率的停止风险：在完整、model-relative 的 wellposed 校准轨迹上，先固定 keyword lexicon、token bin 与统计函数，取每条轨迹所有 bin 的最大值，再用有限样本 order statistic 设阈值。测试轨迹任一 bin 严格越阈值才停止；在校准与测试完整轨迹可交换、统计函数固定的前提下，这把反复窥视的 ever-cross 事件一次纳入校准，而不是把每个局部检验的风险直接相加或当独立事件。它控制的是 wellposed 轨迹被误停的概率，不是提交答案错误率，也不保证识别所有坏推理。模型、lexicon、bin 或任务分布变化需重新核查；所测 OOD 的误停率仍有高于目标的反侧，缺少可区分文本信号时检测能力有限，粗 bin 会漏掉短轨迹，在线统计与离线完整生成也有成本。Renewal/Šidák 的近似分支不具有同一有限样本证书；普通 EOS 和硬 token/deadline 预算仍是无可靠信号时的回退。<!-- source-family:SF-2026-ARXIV-2602-13935 -->

另一种early-exit建议可以用完整轨迹构造离线监督，再让因果读出在当前prefix上预测是否已出现原轨迹的最终答案；它预测的是与原full-CoT答案的一致性，不是答案正确性，也不保证截断后一定生成同答。[TERMINATOR的受限证据](https://arxiv.org/html/2603.12529v1)把label生成与在线停止分开，但文字/Eq3标签方向及最早同答与语义首次到达的关系尚未明确，不能把其精确recipe或经验结果称为已证实最优。离线完整生成、标注/verifier、额外读出与阈值/窗口均付费，局部token或batch1延迟下降也不授fleet SLO；labeltarget、模型或任务失配时保留普通EOS、硬budget与独立答案verifier，不以“已到达原答”批准正确提交。<!-- source-family:SF-2026-ARXIV-2603-12529 -->

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

轨迹内控制还可以切换一份已训练adapter的强度，而不是只改停止条件或当前hidden：先学会较简短的回答模式，再由局部token entropy和双阈值提出详细模式，回滚到窗口起点重生成，随后切回简短模式。[这条受限分支](https://arxiv.org/html/2510.06052v1#S3)改变的是生成历史与参数路径，不把高熵当错误真值，也不保证窗口只覆盖必要推理。缓存必须随路径说明：保留旧模式prefix状态再补新span可以定义一种混合执行，但不等于用当前固定强度重算整条历史；仅让LoRA作用于MLP，也不能由K/V投影权重未变推出后层输入与KV不变，复用验收仍按[缓存身份合同](../part-05-inference-system/45-why-kv-cache-speeds-up.md)。局部数学对照仍有质量反退，较短最终trace不等总时延更低；adapter训练、entropy读取、废弃生成、重Prefill和阈值搜索均计费。信号失准、状态不兼容或独立质量/总费用不合格时，保留固定adapter/原模型、重算、普通EOS与外层硬预算，不由更少token批准无损推理或服务SLO。
<!-- source-family:SF-2025-ARXIV-2510-06052 -->

内部控制也可以在本次生成中临时求解，而不预训一份固定vector：以近期token entropy的相对尖峰提议干预，冻结主干和LM head，仅优化一份加到hidden的δ，用已生成历史token的teacher-forced CE约束偏移，同时降低当前输出entropy；随后只在当前finalhidden采样并丢弃δ。[受限self-reflective生成](https://arxiv.org/html/2510.02919v1)在这一步相当于给logits加Wδ，不是获得新观察或真实错误标签；历史自标可保住旧错，低熵自信错误也可能完全不触发。丢弃δ不撤回已生成token，新的prefix仍会改变后续分布；全局代理最优的条件结论不批准几步梯度已满足语义保持或正确trace不退。监测窗口、raw/tempered概率、历史hidden与detach、CE长度尺度、内循环步数和当前采样须共同绑定，未闭的温度/自适应权重规则不补成通用配方。全部head/历史状态制备驻留、entropy、内循环梯度、改后完整输出与独立质量回归均付费，局部额外时间不是长度无关上界；信号、代理或预算失配时，保留原解码、固定控制/外部verifier与硬预算，不由更确定或更像自身prefix批准答案正确。<!-- source-family:SF-2025-ARXIV-2510-02919 -->

隐藏状态的临时控制也可以追求一个目标值，而不只降低entropy或沿固定属性方向增强：先以外部reward训练value预测器，再在生成时用其梯度调整hidden，使预测接近请求的目标。[受限目标值控制分支](https://arxiv.org/html/2510.12121v1#S3)把reward定义、value近似和实际输出分开；TD读出不是目标事实，编辑后状态漂移也可能让原预测器失准，多属性各自可达更不保证联合目标可达。目标/容差、reward与value版本、层位、内循环预算及原decoder须共同保存，另验目标达到、语义/多样性和旧任务。只在base未达标样本上计算的成功率不能冒全请求控制率，SelfBLEU也不认证全部质量；Pareto候选仅支持给定采样人口。Value训练/外部reward、各步梯度、候选与独立输出回归全付费；预测、目标冲突或净质量失配时，保原解码、较保守目标/固定控制与外部结果检验，不由接近预测target批准真实属性、全局frontier和无损控制。

<!-- source-family:SF-2025-ARXIV-2510-12121 -->

### Semantic Steering 可以从单向 Vector 扩展为受限 Subspace

前面的轨迹控制既可调整是否继续探索，也可用外部reward的value近似追求给定目标；后一种已在改变行为，不再只控制时长。下面转向另一条语义控制分支：从activation估计固定方向或子空间，再校准注入位置与强度，而不要求每个目标都训练一份TD value并在生成中求解目标距离。两路都干预hidden，但控制参照、训练成本和失配方式不同；方向、预测值或更确定的输出均不能充当停止策略、实际属性或正确性的验证。

白盒steering的层位还决定它可能改动什么，而不只决定同一概念的强弱：末层残差注入紧邻最终归一化与读出，可能主要改变少数起始token的相对偏好；更早注入则还会经过后续attention、归一化和MLP。[受限RL向量诊断](https://arxiv.org/html/2509.06608v1)用显式起始prefix、跳过子模块与局部patching比较这些路径，局部正确率改善不自动表示新增了通用推理算法。若只对某head每个可见位置的Value加入同一常量、QK与归一化权重不变，行权重和为一会使其成为固定写入项；不能把这个条件等式外推到同时改QK、经过LayerNorm的完整残差干预。应绑定checkpoint/tokenizer、注入位置和向量、prefix、采样温度与核验人口，分别保留原模型同解码、简单prefix和完整steering对照；更低entropy或相似总体分数不识别唯一内部机制。独立训练的向量也可能互相干扰，双向量接近全层的局部例不保证跨模型可组合。向量训练、所有rollout/层位与组合搜索、额外前向及独立答案/旧能力回归全部计费，参数少不等完整训练或服务免费；层位、任务或预算失配时，保普通提示、原采样与已验checkpoint，降低或关闭注入，不让更偏好的起始词替答案正确性签字。
<!-- source-family:SF-2025-ARXIV-2509-06608 -->

单个 steering vector 适合近似一维、方向稳定的概念；当概念在 hidden state 中占据多个相关方向时，固定向量会漏掉模式，过强插值又可能破坏流畅性。Conceptor 一类分支用 contrastive activations 估计概念子空间，再通过 interpolation 或 replacement 控制投影强度；layer quota 只用于发现可能有效的 intervention point，不能作为 correctness 或安全真值。

子空间扩大 coverage，也会因 overlap、有限 pairs、layer drift 与 Boolean composition 产生非预期耦合，replacement 过强还可能生成退化输出。概念近似线性、简单向量已经稳定时保留旧方案；校准不足或外部行为 verifier 不通过时，应降低强度、关闭 steering 或回退提示/微调。exact-v1 只测试三种较小 instruction model、三个英文概念、单层 intervention 与自动 classifier，不证明生产行为正确或安全。

Steering还可在参考activation的统计区域内限制编辑，而不只沿方向无限移动：在PCA子空间拟合均值与协方差，用Mahalanobis椭球规定候选区域，再沿期望方向求与边界相容的步长。[IDS的受限构造](https://arxiv.org/html/2510.13285v1)把控制强度接到参考人口，却不使Gaussian近似或95%阈值成为真实语义流形/正确概率。直线无实交点时取最近点的fallback仍可能在椭球外，零方向、奇异协方差与坐标回投也需明确退路；不能据投影名称批准总是in-distribution。应共同保存拟合人口、PCA比例、协方差/阈值、方向与注入层，独立验约束实际满足、目标属性和原内容。F1或较低PPL并不认证事实/安全，拒答、负向属性与MMLU仍有取舍；拟合与选择若复用同人口也非独立泛化校准。全部activation采集、拟合/方向搜索、边界求解与新旧行为回归计费；域条件、真实约束或质量失配时，关闭/减小编辑、保原hidden或已验固定向量与外部核验，不由椭球内分数批准无损语义、任意属性可达和安全输出。

<!-- source-family:SF-2025-ARXIV-2510-13285 -->

另一条分支先用固定 SAE 把原 activation `h` 编码为 latent code，只在该坐标中施加偏好向量，再 decode，并把原重建残差 `h−Dec(Enc(h))` 加回。它把“修改哪些 latent 坐标”与“保留字典未重建部分”分开，但残差保留不认证原行为不变，ReLU 非负也不证明概念独立或真正稀疏；[受限偏好 steering 对照](https://arxiv.org/html/2601.08441v1)的语言/任务反侧要求另验 utility 与目标行为。SAE、layer、dictionary 和模型 revision 必须共同绑定，latent 维数还可能大于 dense hidden；reference-free 不免同 frozen 模型的 unsteered likelihood 比照。字典训练、activation patching、数据合成/judge、baseline forward 与 latent 优化都计完整成本，不能把少量向量参数当总费用；字典失配、过强干预或行为退步时，降低强度、关闭注入，保留 dense vector 或普通提示。<!-- source-family:SF-2026-ARXIV-2601-08441 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04980 -->

除了扩大单个概念的子空间，也可以保留有限 steering vector 库，让请求条件决定组合与强度。[一个受限 reasoning 分支](https://arxiv.org/html/2601.09269v1)先从正负回答的 contrastive activations 聚类建库，再由双头 controller 在 prefill 最后位置读取 hidden state，分别提议选哪些向量、各注入多少；得到的组合随后在整个 decode 中静态复用。这是每个 request 的条件化干预，不是逐 token 动态 routing，聚类也不能证明得到互相独立的认知能力。库、controller、checkpoint、layer 和强度范围应绑定同一 artifact，不能假定不同 hidden width 间可直接搬运向量。

条件化选择把固定向量的校准问题转为建库、候选组合搜索和 controller 训练问题，并未消除这些成本。离线回答生成、过滤、强度搜索、SFT/RL 与部署注入须分别计费；输出 token 变短不证明端到端延迟下降，局部任务还有简单 Top-1 优于组合的 slice。这里只采用 native 配置下的接口分工，不采用未说明跨宽度映射及口径不一致的 transfer 数字，也不把强度或组合当作正确性证据。版本漂移、任务失配或质量/成本未通过验收时，保留固定 vector baseline、降低强度或关闭注入，外部 verifier 与原 sampling budget 仍拥有最终约束。<!-- source-family:SF-2026-ARXIV-2601-09269 -->

语义控制也可以只作用于 logits，而不要求访问或修改 hidden state。普通 system prompt 在已能表达目标行为时最省计算；若需要连续调节其相对默认助手条件的强度，可以让同一 checkpoint 在同一 user message 和已生成 prefix 上，分别计算 custom 与 default system prompt 的 logits，再以 `softmax(z_custom + α(z_custom − z_default))` 选择下一个 token。`α=0` 回到 custom prompt 的普通解码，不是回到 default prompt；两条分支消费同一个已提交文本前缀，也不是各自生成两份答案后再选择。这里增加的是条件参照与强度旋钮，不能把 logit 差解释为已识别的独立能力或事实真值。<!-- source-family:SF-2026-ARXIV-2601-06403 -->

[受限 system-prompt 对照](https://arxiv.org/html/2601.06403v1#S3)需要两次条件前向，作者报告约两倍 FLOPs，KV sharing 仍是未来优化，不能由同一模型或同一文本 prefix 推出缓存可直接共享。强度加大也会损伤严格指令准确率和域内可答性；Qwen2.5-7B/14B 等有限任务反侧要求把 target/default prompt、模型、强度与评价人口一起校准，而不是采用通用安全默认值。额外算量不合预算、无法取得两份 logits 或行为回归时，保留普通提示、已验证的 vector 控制或关闭对比分支；外部 verifier、权限和停止预算仍独立约束最终输出。

条件对比的选集还可以随当前生成步骤变化，而不永久对比同一份system prompt：先把问题组织成带当前计划与推理的结构，再将原问题和当前plan对应的token作为本步anchor，比较原条件与遮住这些token的条件logits。[受限逐步锚定分支](https://arxiv.org/html/2510.03223v1)新增的是自动选集，借用的logit运算并不等于直接修改attention heads，也不证明模型已关注正确依据。Plan边界、选中span、共享prefix、遮挡方式与强度规则须绑定，计划和token概率都只是可错提案；打印状态式与强度映射不足时，不据其补成通用执行配方。结构生成、双条件前向和独立答案回归均付费，绝对tokens/s差小也可能是显著相对吞吐损失，不能由无训练或短篇演示签替代RL与服务SLO。选集错误、强度或净质量失配时，保留原prompt、固定条件对比或普通采样，外部verifier和停止预算不由anchor接管。<!-- source-family:SF-2025-ARXIV-2510-03223 -->

多个专家的分布也可以在解码时组合，而不先合并参数。以共同背景分布 `p_b` 为参照，在同一 prompt、词表和已提交 prefix 上计算 `p_b ∏ᵢ(p_i/p_b)` 再逐 token 归一；它表达各专家相对背景的乘积修正，不是 logits 平均或网络权重相加。一个[条件性组合结果](https://arxiv.org/html/2605.28304v1#S3)要求共同支持、预先固定且互不相交的 token-position masks、背景按这些 masks 分解，并且每个专家在自己 mask 外与背景相同。在这些强条件下，非活跃专家的 ratio 消去，各自指定部分的 marginal 才保持；不能从这个足够条件推出任意数学、代码或其他技能天然互不干扰，也不沿用未经核验的任意 feature 变换推广。

组合因而增加每 token 多个模型的前向、状态和归一成本，还要处理支持过小、条件交互与共同终止。受限 Gemma2-2B 数学/代码专家实验中，组合的数学表现低于数学专家，更多专家在 EOS 附近还可能失稳；这不是无损通用技能合并或强 weight-merging 对照胜出的证据。专家、背景、mask 或终止协议不满足条件，或多路成本不合算时，保留单一专家、普通条件提示与已校准的固定对比，不由分布乘积签发能力保留或答案正确性。<!-- source-family:SF-2026-ARXIV-2605-28304 -->

组合分布还须先声明“让成员受益”测的是什么，而不只选平均概率或相加logits。固定同一有限输出空间、严格正概率与当前前缀，若把成员的效用**定义**为其自身的 `log p_i`，则 `Δ_i=E_p[log p_i]−E_pi[log p_i]` 只衡量改用组合分布后的自评期望，不是对外界真值的proper-score改进。[一个受限理论结果](https://arxiv.org/html/2509.06701v1)表明，所有成员正权的线性混合不能让成员全部不损且至少一个严格改善；两个不同二元分布的正权log-pool也不能做到。另一方面，对n个成员、n+1个结果可构造严格全受益的log-pool，这只是存在性，不保证任意给定模型、权重或固定三结果空间都能获益。它把组合算子与效用定义分开，不把数学分解的witness当已识别的神经persona，更不推出提升一种行为必然增强相反行为或某种抑制策略安全。多分布前向、权重选择、归一、状态对齐与独立任务回归均有费；共同事件、效用或实测结果失配时，保留单一模型、原概率混合与独立verifier，不由log-welfare一致性批准答案正确或真实协作收益。
<!-- source-family:SF-2025-ARXIV-2509-06701 -->

条件参照还可随反馈轮次更新，而不始终对照一份固定 prompt：冻结模型，让 judge 的 critique 提出下一轮 context，再在同一已生成 prefix 上分别读取新 context 的概率 `P_new` 与上一轮 context 的 `P_old`。一条受限分支先取 `r=log(P_new/P_old)`，再用 softmax Jacobian 将它投影为 `delta(v)=P_new(v)[r(v)−E_P_new(r)]`，调节当前 logits；这不是普通的两份 logit 相减，正方向表示相对平均值更大的概率比，也不表示该 token 已正确。两条条件流仍有独立 KV；低置信支集的有限惩罚又改变实际 steering 方向。<!-- source-family:SF-2026-ARXIV-2610-22160 -->

[EMO 的有限推理对照](https://arxiv.org/html/2610.22160v1)支持将 context 改写与 decode 实现分开比较，但增量并非所有模型、任务都为正；候选覆盖高也可能被 judge 选错。其局部改善证明还要求 context 已改善目标 KL，且实际 masked 方向与目标对齐，只对足够小强度成立，不认证默认强度、截断采样或逐轮准确率单调上升。历史最高 judge 分只是选择依据，不是外部 verifier。双条件生成、judge、context 重写和全部候选长度均付费，按 generation equivalents 匹配不等同匹配 FLOPs 或延迟；方向、选择器或净预算不稳时，保留普通提示、context-only、固定对比或原候选采样，不让反馈循环自行授予正确性。

两份logits的参照也可以由同一模型内部mask形成：先用有reference的校准集逐head消融，按referenceNLL变化选择一组head，再在同一profile、query和已生成prefix下比较原模型与mask分支，用差分调节采样；另一分支可按离线profile簇选择head集合。这里测的是该reference与干预条件下的损失敏感性，不证明head专门或唯一存储用户偏好；所谓generic分支仍读取profile，不能当无profile因果对照。[DPS的受限个性化对照](https://arxiv.org/html/2604.22345v1)尚未给出共享prefill后mask分支KV语义的充分验收，不能由同prefix批准缓存通用共享或净费用接近一次前向。Reference选择、逐head校准、簇路由、双分支与完整任务回归均计费；标签、profile、head身份或质量失配时，保留普通profileprompt、固定条件对比或关闭干预，外部偏好/权限核验仍独立，不用NLL差签发用户意图真值。<!-- source-family:SF-2026-ARXIV-2604-22345 -->

两条件解码的参照还可由当前输出对输入的敏感度提出，而不预先选定一组head：白盒模型中，分别聚合当前token对视觉、提示与已生成文本的输入梯度，再以已提及noun所关联的位置形成局部视觉参照，比较完整视觉与受mask条件下的logits。[GACD的受限分支](https://arxiv.org/html/2509.03113v1)据此提出逐token控制强度，但梯度范数只是局部sensor，不是对象存在、真实分割或因果贡献；一般混合梯度的范数也不能当作各范数的线性组合，本次不照未闭合的影响对齐式作精确recipe。必须独立检查视觉支持、召回、输出长度与终止协议，不能以少幻觉均值掩盖遗漏；原有限对照仍有召回反退。白盒反传、两路前向/状态、noun检测、校准与全部行为回归均付费，不训练新模型也不等免费推理。sensor、mask或完整预算失配时，保留原视觉条件、固定对比/普通采样及独立核验，不由更高视觉影响分数批准输出正确或无风险。
<!-- source-family:SF-2025-ARXIV-2509-03113 -->

固定双分支的强度还可改成逐 token 学习，而不只在请求开始时选择一个常数。一条受限分支先用共享正确前缀下的正负步骤续写训练 reward LM，再冻结它与 base LM，让小 controller 读取当前两份 logits（或带 token 身份的 Top-k 特征），以 gold-token likelihood 和可选门控 entropy 学习每步的混合权重。这里学习的是解码选择，不是每个 token 的逻辑真值；迁移首先要求词表坐标、模型与已提交前缀身份能对齐，不能由同输出维度推任意模型通用。[TARo 的受限对照](https://arxiv.org/html/2603.18411v1)存在 logit 与 probability 插值口径差异，不能直接照为统一采样配方；部分非训练域任务弱于原 base，硬门控与更高数学分数也不保证全部能力保持。双模型前向、reward/controller 训练、词表特征与状态都付费，token 吞吐与请求吞吐须分账，不由少量 controller 参数或单次算量估计宣称免费推理。混合算子、身份、质量或预算无法验收时，保留固定强度、普通单模型采样与独立 verifier，而不让门控权重替答案签发正确性。<!-- source-family:SF-2026-ARXIV-2603-18411 -->

### Answer-first 与 Optional Justification

延长或压短推理仍默认先生成过程、后提交答案。如果任务只要求尽早拿到答案、解释可以稍后提供，那么还可以调整输出次序，而不把这项接口选择混同于增加搜索能力。

传统 reasoning decoding 把答案提交排在完整推理轨迹之后，这在 verifier、tool 或后续步骤必须消费过程时合理，却把 answer latency 与解释成本绑在一起。另一条条件分支是先生成并提交 final answer，再按需生成 answer-conditioned justification；训练时还可以 mask answer loss，只对 justification 提供监督。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06165 -->

后生成的解释不证明它忠实反映答案的因果过程，也可能把错误答案包装得更连贯。需要 faithful process、外部 verifier 消费 trace，或任务本身要求显式搜索时，仍应保留 pre-answer reasoning 或把搜索移入可审计的 workflow。该分支优化的是输出接口与延迟，不是凭空获得推理能力。

单条代码轨迹也可在已生成的code prefix中途切入thinking块，再返回代码，而不是只在代码之前完成全部说明。提交执行物时移除这些块并连接其余代码；phase标记定义续写/抽取接口，不是每token的真实不确定性sensor，删文字更不是安全隔离。[Think Anywhere的受限对照](https://arxiv.org/html/2603.29957v1)支持这种位置可选分支，但prompt-only/SFT及专门token切片仍有反退，padding也能改善部分结果，不能把位置或内容读成唯一收益因果。合成过滤保留了错误代码，格式合规不认证功能；特殊token还付embedding/LM-head适配费，合成、SFT/RL多rollout、抽取和test均计费，较少token不等完整延迟更低。Phase解析、拼接或功能回归失败时保留先推理后代码、原文本分隔与独立测试/执行权限，不由熵曲线或通过一组测试签发全能力与生产正确性。<!-- source-family:SF-2026-ARXIV-2603-29957 -->

在转向多条完整轨迹前，还可以让不同模型在一条共享文本前缀上提出局部续写。单模型逐 token 选择最省状态；当模型的 tokenizer 不同，直接对齐 vocabulary logits 不再有明确共同坐标，一个替代分支让各模型先完成到 word boundary，再对同一候选文本分别重新编码与评分。首 token 的 top-1/top-2 margin 只作为是否继续延长局部 span 的代理，低 margin 时在当前词结束后重评分，并以词数上限防止长时间失去交叉反馈。各模型按自己的 token 数归一化 NLL、再取均值，只形成跨模型排序的 heuristic，不使不同 tokenization 变成共同 posterior，也不证明高 margin 对应正确答案。[受限双模型对照](https://arxiv.org/html/2601.06022v1)中固定 pair 在部分数学任务弱于单模型，不能用 oracle 选择的最佳 pair 替换实际部署比较；双份模型状态、候选重编码与同步仍付费，word boundary 对新语言也需验收。延迟或质量收益不稳时，普通单模型采样、独立候选加 verifier 仍然合理。
<!-- source-family:SF-2026-ARXIV-2601-06022 -->

当目标本来就是多个模型在同一前缀上的非负归一概率混合，还可先按混合权重抽一个模型，再从它的条件分布抽token；全概率公式给出的next-token分布与先计算全部模型再平均相同。这里必须固定共同输出事件、词表映射、prefix和混合算子；它不保持argmax、logit平均或混合后任意Top-k变换的语义，更不意味着整条回答由同一个模型负责。<!-- source-family:SF-2026-ARXIV-2605-00419 -->

随机切换模型又引入状态成本：被选回的模型须先补算它未见的已提交prefix，维护各自KV，再产生下一个token；不同模型的cache不能直接互换。一次extend批处理缺失tokens可摊薄weight加载，却不消除历史token计算、多份权重/KV与词表转换费用。[受限采样与执行对照](https://arxiv.org/html/2605.00419v1)存在低于最好单模型的任务，最佳混合权重也经过搜索，不授免费增益或所有负载近单模型延迟。前缀差额大、状态预算不足、需要确定性决策或质量回归时，原单模型、全分布ensemble或独立候选加verifier仍合理。

### 多个 Token Draw 也可以只推进一个连续 State

共享文本前缀上的局部续写仍要提交离散 token；如果 runtime 能直接接收输入 embedding，另一条分支是在每步从同一 logits 分布独立抽取 K 个 token，将它们的 embedding 按均匀或模型概率权重聚合，再把这一个向量作为后续推理的输入。K=1 回到离散采样；K>1 改变单条轨迹的状态表示，并没有维护 K 条独立的历史、KV 和答案。[Multiplex Thinking exact-v1 §3](https://arxiv.org/html/2601.08808v1) 的训练对组成该向量的离散抽样动作计算 log probability；由于不同 token tuple 可以投影为同一 embedding，tuple 的概率或熵不能直接解释为连续 state 的密度或熵增保证。

这条路径把 token-wise 探索压入一个状态，却要求内部 embedding 输入接口、匹配的训练/推理路径，并承担投影的信息损失与分布偏移。更多抽样不等于更多 forward，也不等于已经证明墙钟成本不变；作者有限模型与数学任务中，增加宽度收益趋缓，聚合与训练对照也并非逐项占优。接口不可取得、任务质量或端到端成本不稳时，离散单轨迹继续合理；需要保持不同候选的独立可审计过程时，应采用下面的多轨迹采样，而不是把一个混合 state 当成 K 份可选择答案。
<!-- source-family:SF-2026-ARXIV-2601-08808 -->

单条autoregressive轨迹还可按位置选择离散token或soft embedding，而不固定每步都作同一种聚合：先对temperature-scaled分布、在Top-k/Top-p/Min-p过滤及重归一化之前计算最大概率，低于阈值时采离散token，高于阈值时把top-j候选组合成soft输入。它调节下一步的表示接口，不同时维护多条可选择历史；temperature、阈值、filter次序、j与EOS交接必须共同版本化，不能把过滤后抬高的概率误作原router条件。<!-- source-family:SF-2026-ARXIV-2602-11683 -->

最大概率仍是模型内confidence代理，错误答案也可能高置信；soft表示的接口、聚合与validation选点均付费，较短输出不自动证明完整服务更快或所有任务Pareto占优。[ThinkRouter exact-v1](https://arxiv.org/html/2602.11683v1)的受限对照里Random在一个coding设置更高，另一数学设置离散baseline更高，故要联验任务、真实decode成本与质量，而不按confidence授正确性。接口不可见、阈值漂移或质量回归时，保留离散单轨迹、固定soft分支及独立verifier/明确停止预算。<!-- source-family:SF-2026-ARXIV-2602-11683 -->

压缩连续状态还可改变“一步消费多少个相邻位置”，而不只把同一位置的多个候选混成一个向量：先将已选的两个相邻token embedding压成一份输入，由主干预测下一个奇数位，再用轻量MTP分支在该奇数位条件下预测偶数位，训练仍为两处离散token保留监督。若MTP信心不足，就拒绝该候选，下一轮只把已选奇数位送回主干重预测偶数位；这是需匹配蒸馏/联合训练的有损状态接口，不是保持原模型分布的speculative验收。[受限pair-state对照](https://arxiv.org/html/2606.13862v1#S3)中，强制每步压双token明显损伤数学精度，回退恢复部分质量但仍有任务反退，而且adaptive与非adaptive训练损失权重不同，不能把差异全归于线上阈值。平均正确轨迹的压缩步数、还原出的文字长度、全部请求计算和墙钟应分账；MTP、压缩、回退、数据制备及训练均付费，少forward不认证服务吞吐或SLO。监督、embedding接口、阈值校准或完整预算不合时，保留普通离散单轨迹与独立答案验收，不由高置信或两token一步批准无损推理。<!-- source-family:SF-2026-ARXIV-2606-13862 -->

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

缺少可投票的规范答案时，selector还可用候选长度作廉价代理，而不另训judge。[Shortest-answer selection的受限实验](https://arxiv.org/html/2510.21067v1#S3)在代码等任务比较先生成多答再取最短，支持长度与部分错误模式的局部关联，不证明短答更真或所有任务单调受益；代码仍须执行测试，长度也依tokenizer、格式和截断规则。全部候选已经生成，最终输出短不能抹去其余生成费；只有实际并发、生成速率与终止契约满足时，先完成即可停止其他分支的运行策略才可能减少等待，不能从离线最短选择自动继承。长度/质量关联消失、正确候选被截断或测试不充分时，保原selector、完整候选预算与独立任务verifier，不由低长度代替正确性判断。

<!-- source-family:SF-2025-ARXIV-2510-21067 -->

多条候选也不必等到完整生成后才比较，可以在每步共同管理仍存活的prefix：从这些prefix各扩展下一token，按累计序列概率排序，以相对当前留存扩展集的概率质量阈值决定保留多少条，再用硬cap约束宽度。[LTM的受限分支](https://arxiv.org/html/2509.07676v1)因此把固定beam宽度换成受质量阈值约束的中途支持选择，而不是单条prefix上的nucleus抽样；这里的“质量”是模型概率质量，不是答案质量，已剪去的正确路径也不能由后续选择补回。完成后按PPL选答仍须独立verifier，长度/EOS与概率来源不同不得直接混排，原下标/边界未闭时不补完整实现配方。外部负反馈可只触发按原问题重生，但gold触发与有误报/漏报的模型代理不是同一权限，不保证原正确答案均被保留或新答不会更差。全部proxy判断、prefix/KV驻留、扩展排序剪枝、重生与独立回归均计费，同输出token数不等同算力或净延迟，部分实测还慢于普通双轮。支持不足、概率接口不可得或预算/质量不合时，保留原答、普通nucleus/固定beam与独立验收，不由累计概率或低PPL批准事实正确、全树最优或停止搜索。
<!-- source-family:SF-2025-ARXIV-2509-07676 -->

外部评分若定义在完整对象而生成器逐token剪枝，还可以先把两个空间对齐，而不是等候选完成后再融合。对固定semantic-ID目录，先取判别模型Top-R cutoff以上的正margin，再把这些item的margin沿各自prefix–token边聚合；每次beam扩展在native累计log-score上加该边的有界强度修正，然后才保留global top-B。相同边可同时支持目录中多条后代路径，因此最终输出不必落在判别Top-R内，但未共享的后续边仍要由生成器完成。这是改变搜索路径分数，不是更新模型参数、重标定native token概率或认证对象真值；同一code路径、目录和判别score尺度必须共同绑定。

[受限生成式推荐对照](https://arxiv.org/html/2610.32098v1)以full-catalog softmax最大值作相对confidence gate，并非校准正确率；gate降低强度不等关闭干预，margin的加法平移不变也不使任意score缩放无影响。前缀存活条件要求目标已经在本轮frontier，且修正优势足以压过竞争者的native差额、每层都成立，不能当线上已知正确路径或全程保留证书。离线用gold移除target-path修正只说明已命中人口的依赖，失去Top-K hit多数未发生实际beam丢路径；原本存活的前缀也可被干预挤掉。同beam宽度仍多付判别全目录打分、Top-R/聚合和融合费用，较窄beam的局部质量—时延取舍不授通用加速或SLO。支持、校准或预算失配时，保留native beam、普通post-hoc融合与独立验收，不由共享前缀或有限存活定理批准正确交付。<!-- source-family:SF-2026-ARXIV-2610-32098 -->

多候选搜索还可改变“谁为每个prefix计算下一步”，而不减少beam或改目录。[Deco的受限SID分支](https://arxiv.org/html/2610.32980v2)先把每个历史item的多个code融合成一个输入，重backbone只读一次历史、输出固定数目的concept vectors；轻量causal decoder只读这份condition与已生成prefix，以自己的KV完成整棵受trie约束的AR beam，不再逐步调用或让重模型验收。相同SID、trie与因子分解不保原heavy概率或全局top-B，因此这是需联合训练/有限KD的替代分布，不是exact speculative decoding；沿gold prefix的teacher约束也不保证离轨prefix一致。Constant-size只指generator condition，不含beamcache、目录/trie或全部历史信息；重复消费需要另保history SID、权重和gate的O(T) copy支路，混合prefix概率在正mass时才可相除，不自行补零分母配方。有限比较须拆开fusion、decoder委派与KD：部分dataset仍低FlatGR，小backbone比decoder还轻时反而更慢，长历史prefill仍增长。单H100/bf16的50ms p95只约束已扫batch的GPU prefill加beam，排队、网络、数据加载、ID映射与编译预热未计，不授请求级服务SLO。全部SID构造/版本碰撞、teacher和student训练、concept刷新、trie/top-B/copy与端到端回归均付费；预计算condition还须绑定历史、producer及consumer版本，这是缓存资格要求而非原文已验的生命周期协议。目录、重复率、质量或预算不合时，保原full-backbone beam、明确历史与独立排名评价，不由更小condition、更多候选或局部吞吐批准无损压缩、事实检索正确和全负载净省。
<!-- source-family:SF-2026-ARXIV-2610-32980 -->

生成中选择也可以以固定上限的 token chunk 为单位：小模型提出若干续写，大模型只计算它们的条件 log-probability，再按大模型分数或两模型分差选一段继续；EOS 仍可提前结束，所以边界例外需保留。这与事后选整条链、按自然步骤评分及保持 target 分布的 speculative verification 都不同。[受限 chunk 对照](https://arxiv.org/html/2606.01682v1#S4)中，长度归一仍未消除自然步骤的长度偏好，较短固定 chunk 改变了干预时点，但 likelihood 不是逻辑正确性。相近干预次数不等相同打分算量或延迟，较短最终轨迹也未结清全部废弃候选和双模型驻留。生成、评分、缓存及每轮串行提交均计费；概率接口、质量或完整预算不合时，保留普通单路、整条候选加独立 verifier 或已验 PRM，不从无需新训练批准免费推理或原分布不变。<!-- source-family:SF-2026-ARXIV-2606-01682 -->

自然步骤的候选评分还可先扣掉“不见原问题时也容易生成”的部分，而不只比较某模型的绝对likelihood：在同一已提交步骤prefix上，分别计算评分器有、无原问题时对新步骤的logprob，累计其差，再用来保留有限搜索前沿。[这条受限问题条件分支](https://arxiv.org/html/2510.03632v1#S3)衡量的是该模型/模板下的相对依赖，不自动等于由共同joint分布积分得到的PMI，更不是逻辑正确或步骤的真实因果效用；照抄题目、很低的无题概率及生成器/评分器共错都可能抬高代理。步骤数归一不消除token长度和切步规则的影响，按下一token entropy经验分位分配扩展量也只提出预算，不识别错误概率。已剪正确prefix不能靠终局投票补回；分数若可为负，乘答案出现频率甚至会让更常见答案更负，不能把任何“加权共识”都当正确性保证。应共同绑定原题、两条件模板及独立KV、评分器、步骤/答案parser、分数符号/归一、全树与停止预算，另用可靠答案或执行verifier验收；全部候选/废弃前沿、双条件求值、entropy/排序、重试与选参都付费，相同最终链数不等同总节点或净墙钟。概率接口、任务相关性或净质量/预算不合时，保普通单路、固定预算CoT/SC与可信verifier，不由更高比值、更宽beam或少look-ahead批准原分布无损和最优推理。

<!-- source-family:SF-2025-ARXIV-2510-03632 -->

候选已经生成后，选择器还可分别读取整条链和链后答案，而不只按多数票或单个answer score排序。一条[受限组合评分](https://arxiv.org/html/2508.21787v1#S2)先累加生成链的token logprob，再在完整链后追加明确取答案的提示，对已抽取答案计算条件logprob，将两项相加；链项按长度归一则改变长短轨迹的选择压力。这是候选ranking heuristic，不是同一原始joint分布的直接MAP，更不使高likelihood认证每步推理或最终事实正确。Tokenizer、prompt/答案边界、概率来自raw还是过滤后分布、评分模型及长度规则须共同固定，不同evaluator的分数也不能自行共用概率尺度。更多采样或加入链分数仍可能退步，已知正确样本定义的回看“高峰”不能作为部署阈值；全候选生成、追加取答案、重评分/缓存与驻留费均计入，不从少几条候选批准净提速。接口不提供所需概率、目标域排序不稳或独立质量未过时，保留原候选、普通多数/已验selector与外部verifier或拒答，不让组合分数取得答案真值或提前停止权。
<!-- source-family:SF-2025-ARXIV-2508-21787 -->

连续形状输出需要先声明怎样算“同一候选”，再投多数票：把轨迹重采样为弧长点列，用允许的几何warp和配准距离聚类，再从最大簇选medoid；prototype与允许warp共同定义这个形状家族，不是prompt语义真值。若warp本身也从同批生成猜测，过窄会拆开正确样本，过宽会把错误形状并入共识。[受限trajectory self-consistency](https://arxiv.org/html/2603.29301v1)的多数/层级选择因此各需正确mode支持和好坏簇分离条件，不能由稳定多数认证运动意图或物理可行。有限模板/单prototype人口、ICP近似及阈值限制等价关系，scale变化也不保原距离误差；十九次生成与单次直接输出不是等预算。采样、配准、candidate warps和两两比较全部付费，mode或等价条件不可信时保留原候选、固定已知warp、单路/外部语义与几何检查，不从最大簇批准正确执行。<!-- source-family:SF-2026-ARXIV-2603-29301 -->

多路径预算不一定要每次从 prompt 重新支付完整生成。若已完成的轨迹中保存了若干高 token entropy 位置之前的 prefix，可以从这些位置重新抽取下一 token，再各自完成后缀；这里分配的是“在哪里重新分叉”的预算，而不是将高熵 token 判为错误或把后缀当独立解答。局部高熵与随机位置在同 generation budget 下的有限数学对照支持这一选择分支，但共享前缀也会保留相关错误，完成后的候选仍需要单独的答案检查。<!-- source-family:SF-2026-ARXIV-2604-00018 -->

entropy 只测当前模型分布，生成后较低的熵也不是正确性验收；没有可靠 verifier 时不能以“after-think confidence”自签停止。该路径仍支付首条轨迹、prefix/cache 保留、概率读取、重生成和候选检查，不同型号或 API 价格不能当同计算预算。受测两模型、两数学任务及训练集调参不授普遍接近满分，也未恢复有限 logprob API 与完整词表 entropy 的等价实现。信号不可得、分支强相关或检查费用不合算时，保留普通完整 self-consistency、随机分叉或单路加独立 verifier。<!-- source-family:SF-2026-ARXIV-2604-00018 -->

若截断采样经常重复相同轨迹，还可显式维护已探索的 token tree：从尚未展开的高概率 prefix 分支，再用 greedy continuation 完成新的 leaf，并复用共享 prefix 的 KV。这里主动改变的是候选枚举顺序；覆盖的质量是截断分布中的概率质量，不是正确答案、语义多样性或独立样本数量。完整遍历有限树才与原截断分布拥有相同 support，固定 leaf 预算下的 greedy suffix 也不保证找到概率最高的完整序列。

[有限 distinct-leaf 对照](https://arxiv.org/html/2604.20500v1)支持这条预算分支，但连续十个 token 与兄弟后缀相同就停止，是会误剪不同答案的近似 merge；较高 coverage 不能替代最终 verifier。树管理、保留 KV、候选完成与选择均计费，低 batch 的 prefix-cache 收益也不能直接搬到可并行生成的大 batch。截断支持不合适、分叉过多或语义误剪不可接受时，保留普通 self-consistency、较保守的分支枚举和独立答案核验。<!-- source-family:SF-2026-ARXIV-2604-20500 -->

预算策略本身还可先在固定的离线环境中搜索，而不为每个controller反复生成全部候选：预采并冻结branch与probe结果，让explorer根据已揭示状态和完整交互trace写出controller，再把冻结策略交给留出任务与真实运行验收。[受限replay搜索](https://arxiv.org/html/2605.08083v1)减少的是这份池内试验的重复generation，不把未揭示probe交给当前state，也不使池外新prompt、工具状态或分支成为已验证反事实。重复抽取同池不增加独立人口；搜索用AIME24不算held-out，更多token在部分配置仍降低质量，不能由单个trade-off宣称全Pareto。预采、模型、存储、搜索、全部在线probe/生成与验证均付费，离线零generation成本不继承到线上。Pool、任务或model失配时保留固定预算、普通self-consistency与独立verifier，外层deadline和服务SLO仍须实测，不让搜索得分批准真实提交。<!-- source-family:SF-2026-ARXIV-2605-08083 -->

当候选是可执行程序时，还可把一部分重新生成预算转移到模型之外：先生成一份程序，并保存指定单 token 数字或运算符在原 prefix 下的条件概率；再把这些位置编译成有限支持的随机变量，重采局部选择、执行程序并交给任务 verifier。它复用未被替换的文本，而不为每个变体重新调用完整 LM；同一原程序产生的多个变体共享固定部分，不能记作彼此独立的完整模型样本。<!-- source-family:SF-2026-ARXIV-2604-17290 -->

这种局部变体搜索改变了候选分布：前面 token 已替换而后缀没有重新条件化生成，原 LM 的完整程序分布一般不再保留；只留部分选项并重归一化、按执行条件过滤还会继续改变目标。[必要机制与反侧](https://arxiv.org/html/2604.17290v1)的精确性说明另需强后缀独立前提，不能借给一般代码。执行通过也只覆盖 verifier 真正检查的对象，训练或评测用已知答案选择不等于部署有该 oracle。概率存储、编译、CPU 重采、执行和检查均须计费，不能由没有额外 GPU forward 推出免费；局部支持不足、修改破坏程序或缺少可靠验收时，保留原完整生成、重新分叉后续写和外部 verifier。<!-- source-family:SF-2026-ARXIV-2604-17290 -->

讨论选择器是否“最优”之前，还要规定交付目标：最大化数值 reward 的期望，与提高相对参考回答的胜率，不是同一个优化问题。胜率只依赖成对排序，平局计半胜；对 reward 作保序变换可以保留排序，却改变数值期望。因而不能把某种期望 reward 下的次优性直接搬到胜率目标。对固定 prompt、独立采自同一参考 policy 的候选，可分别用参考分布上的成对排序误差衡量 selector，以及目标相对参考分布的 density-ratio 尾部衡量覆盖难度；前者小不等于数值 reward 已校准，后者大意味着目标偏爱的答案仍很难被采到。[受限理论分析](https://arxiv.org/html/2603.05739v1#S3)给出调好 N 的 BoN 在此 sample-and-evaluate 模型中的胜率 regret 界，并在非原子参考分布上给出匹配至对数因子的最坏情形下界；它不证明每个任务、任意自适应搜索或部署费用下 BoN 都最优。<!-- source-family:SF-2026-ARXIV-2603-05739 -->

这一目标变化仍没有消除过度选择：扩大 N 会同时改善覆盖、增加选中 reward 代理错误尾部的机会。一条受限替代分支用独立的正则参数 M 限制选择分布偏离参考的尾部，把采样规模与偏移强度分开；其胜率 regret 上界由覆盖尾部、M 倍成对误差和随 N 衰减的有限采样项组成。固定 M 时最后一项下降，不等于每个有限实例的实际胜率必然单调上升，也不是事实正确性或无 reward hacking 的生产保证。M 仍需校准，过于保守会放弃有价值的稀有答案，全部生成与评价也继续付费；无需这类保守控制、参考覆盖不足或误差条件不可信时，调好预算的普通 BoN、明确执行的 verifier 与拒答仍是合理分支。<!-- source-family:SF-2026-ARXIV-2603-05739 -->

固定偏移强度又留下一个问题：同一选择规则面对不同 prompt 时，代理 reward 的尾部形状可能不同，过度选择与过度保守的代价也不同。一条有限候选上的替代分支先将代理分数归一到 `[0,1]`，用高分候选距上界的 gap 估计右尾，再把尾部估计值 κ̂ 与校准尺度 κ₀ 映射为 `α = 1 + κ̂/(κ̂+κ₀)`；候选权重取 `[1+(α−1)r/λ]^(1/(α−1))` 后归一并随机选择，接近 α=1 时使用指数极限。这改变的是已经生成候选的 selection 分布，不是重新训练模型，也不是继续扩大 N。它尝试让每个 prompt 自己的代理分数形状调节偏移，却不能由“尾部较重”推断高分答案更真实；代理的形状与代理相对真值的误差仍是两个对象。<!-- source-family:SF-2026-ARXIV-2603-06797 -->

[受限尾部自适应实验](https://arxiv.org/html/2603.06797v1#S4)可以支持这种启发式选择分支，不能把所列权重自动称为原文正则目标的精确最优解：其目标、附录尺度与归一化推导存在冲突。有限候选下尾部估计会抖动，满分端点及过小候选集还需要显式数值保护；校准集、归一规则、κ₀、λ 和 reward model 都属于策略身份。复用同一候选池的 bootstrap 也不是独立生成实验，第二个 reward model 不等人类真值。全部候选生成、评分、排序与校准继续付费；未经独立校准、多峰误差明显或无法保护端点时，回退固定强度、普通 BoN 与独立 verifier，不宣称普遍免 reward hacking 或端到端提速。<!-- source-family:SF-2026-ARXIV-2603-06797 -->

候选数量固定时，仍可决定是否额外调用裁决器：每步先生成 N 个动作，按语义等价聚类得到投票分布，再用 entropy 或前两名 margin 提议是否再投入一次选择；不调用裁决器时保留多数票。这把生成预算与 selection 预算分开，但分歧只能描述本次采样和聚类，低熵也可能一致错，裁决器与生成器使用同一模型也不形成独立真值。[有限 Agent 动作对照](https://arxiv.org/html/2602.12276v1)支持这一条件分支，不支持冲突表格中的统一节省比例或全服务延迟保证。N 次生成、语义去重、阈值校准和裁决均计费，误合并动作或误覆盖共识还会损害结果；信号漂移、成本不合算时保留固定多数票与独立 verifier，实际动作仍接受原 tool/controller 验收。<!-- source-family:SF-2026-ARXIV-2602-12276 -->

若目标是已生成回答中最高的reward减去追加采样费，停止对象又不同于多数票是否稳定：在固定prompt、同一生成分布与相同单次成本下，可根据已见reward估计继续抽样的价值，最高reward达到fair-cap阈值才停。未知分布时，一条[受限自适应分支](https://arxiv.org/html/2510.01394v1#S4)先拟合exp(reward)的右尾，以该prompt的高分位benchmark把reward变成有界效用，再估计停止阈值；这让不同prompt的数值尺度不再直接共用一个绝对分数，但尾部分布族、最小样本、benchmark与成本比都成为策略身份。所谓acceptance rate仍是reward启发的proxy，不是实测用户接受或正确率；理论需要有效的anytime上界，不能从经验tail fit与不断重估benchmark直接继承任意分布保证。缓存回答重排中的较少调用也不证明在线时延或完整预算降低；预采、所有生成/RM评分、尾部估计与阈值求解均计费，回答长度变化还会破坏固定单次成本假设。tail失配、代理质量或净费用不合时，保留已验固定N、原选择器与独立verifier，不让停止阈值取得答案验收权。

<!-- source-family:SF-2025-ARXIV-2510-01394 -->

追加候选的停止建议也可以只读取已经得到的答案计数，而不训练内部状态分类器：先固定答案规范化和同一生成分布，用带未见类别质量的后验近似估计当前众数能否保持领先，再在证据阈值或外层预算处停止。[Best-of-infinity的受限分支](https://arxiv.org/html/2509.21091v1)把状态从一个票差扩成已见类别计数、未见支持先验及停止规则，但估稳分布众数不等找到真答案，近似Bayes factor阈值也不是未经校准的有限样本错误率。若每次先随机选择生成模型，混合权重、各模型采样/答案映射和驻留成本都属于同一策略；用带gold的离线回答池估概率、优化权重，不能冒充未知新题上无标签最优，重复池内抽样也不增加独立人口。应分开验众数恢复、独立答案正确性与全部费用，并保留不可解析/未见答案、tie、后验Monte Carlo误差和低票差未停的情况；删掉失败解析后更省样本不代表原请求收益。全部预采/标签、权重求解、多模型加载与切换、追加生成/后验计算和独立核验均计费；错误众数、接口或人口漂移、预算用尽时，保固定小N、可信verifier及Unknown，不由更强答案一致性批准事实或服务SLO。

<!-- source-family:SF-2025-ARXIV-2509-21091 -->

并行采样前还可从同一prompt的内部activation预测是否值得继续追加候选，而不先支付大量probe回答；这种classifier把困难度标签的生成与阈值校准移到离线。[ACT-SC的受限数学对照](https://arxiv.org/html/2602.09438v1)仍需新dataset的阈值和通过率标签，不是无校准停止保证；不同adaptive方法采用不同停止标准和采样预算，AIME等切片还能退步。须分别核最终选中正确率、调用数与误停，并计入白盒读取、标签采样、训练和迁移校准；局部秒数不授端到端SLO。内部接口不可得或错误停止成本过高时，保留固定SC预算、普通EOS与外部verifier。 <!-- source-family:SF-2026-ARXIV-2602-09438 -->

追加多少候选还可以等首条轨迹完成后再决定。先付一次完整 greedy 推理与答案，再从各句的选项条件概率、熵、变化量和词汇统计形成序列，由单独训练的判别器估计这条答案的可靠性；分数越过阈值时保留原答案，否则才追加多路径生成与聚合。[completed-trace 的受限机制](https://arxiv.org/html/2603.08999v1#S3)以每个基座模型自己的判别器支持这一分支。它改变的是后续采样预算，不缩短已经完成的首条轨迹，也不使概率趋势或文字风格成为正确性真值；全轨迹统计与非因果 attention 不能直接充当生成中的提前停止器。
<!-- source-family:SF-2026-ARXIV-2603-08999 -->

不重训判别器也不等于无需目标域校准：[有限迁移对照](https://arxiv.org/html/2603.08999v1#S5)仍用新数据集验证答案选择阈值，较少生成 token 与未显著的准确率差异不证明所有任务非劣或完整推理更快。首条 greedy、每句选项评分、特征抽取与判别、训练/标注/阈值搜索，以及被触发的全部候选和聚合都要计入预算。模型、选项形式、题型或概率接口改变后须重新验收；白盒信号不可得、校准不足或误接受代价过高时，保留原单路、固定 self-consistency 预算和独立 verifier，不由高 confidence 自签答案正确。
<!-- source-family:SF-2026-ARXIV-2603-08999 -->

候选已经生成之后，选择器也可利用中间层与最终层的不一致，只在高divergence候选上施加由token surprise构成的罚分，其他候选保留原评分。[CoCoA的受限门控](https://arxiv.org/html/2602.09486v1)改变的是selector，hidden-state一致不验证事实。alpha=0的候选搜索已经有收益，强罚分又会以更多拒答损失信息；总体与非拒答子集需要分账，不能用幸存者分数补回被拒内容。额外候选、隐状态读取、阈值搜索及judge都付费，未测服务协议不授free compute或SLO。门控漂移、拒答代价或质量回归时，保留原score、固定候选加独立verifier，不让内部agreement签发正确性。 <!-- source-family:SF-2026-ARXIV-2602-09486 -->

候选 selection 还可以明确选择后的分布，而不只报告较高 reward。对有限 response support 上独立采自同一 base 的 n 个候选，在每个 reward/λ 上加独立 exponential noise 后取最大，得到的是目标 reward-tilted 分布与残余分布的有限-n mixture；n 有限时不能直接叫精确 tilted sampling。若 noisy score 越过真实 reward 上界导出的阈值，则 hit 分支恰好具有 tilted law；按独立随机顺序扫描并取第一个 hit，可利用 exponential overshoot 的 memorylessness 提前结束评分，无 hit 时仍需完成候选评分与选择。

这些权限依赖有限 support、独立样本/噪声、真实 score 上界与固定评分规则，不是任意 judge threshold 的提前停止保证。加入截断的 draft–target likelihood ratio 会改变目标，更多候选只能缩小有限-n误差，不能消掉 clipping bias；另加 reward gate 或 base fallback 也不自动继承前面的 sampling law。候选若已全部预生成，提前退出省的是 target/reward 评分而非这些生成；受限实验的 token-compute估计与每步墙钟也有不同分母。support、上界或成本不可靠时保留完整候选评价、标准 BoN/target sampling，正确性仍由独立 verifier 验收，不用分布定理证明所有任务质量或免费提速。 [必要机制与反证](https://arxiv.org/html/2609.21899v1)。<!-- source-family:SF-2026-ARXIV-2609-21899 -->

逐 token 温度与完整 sequence 的 power 分布也不是同一个对象。将每个 prefix 的条件概率局部取幂并归一化，会引入随 prefix 变化的归一常数；它不能单独产生按完整路径概率取幂的目标。一个有限粒子分支仍以局部 powered proposal 生成 token，再用增量 importance weight 修正路径，按 ESS 触发祖先重采样。该 proposal 可消除当前 token 选择带来的增量权重方差，却不能消除不同 prefix 路径之间的退化。<!-- source-family:SF-2026-ARXIV-2602-10273 -->

重采样必须同时重排 prefix、KV、weight 与完成状态；EOS 吸收规则和最大长度截断也定义实际支持。[Power-SMC 的有限对照](https://arxiv.org/html/2602.10273v1)不授有限粒子为精确、独立的全目标样本，较高 batch 利用率也不是总 token-evaluations 减少。粒子复制、缓存驻留、ancestor identity 与评价都要计费；权重退化、资源不足或 support 不合适时，普通低温/Top-P、较小候选集合与外部 verifier 仍合理。

若多条reasoning trajectory可导向同一答案，目标还应明确是完整路径还是答案边缘分布。设m(a)=Σ_z p(z,a)，先求和再取m(a)^K，与Σ_z p(z,a)^K不相同：前者允许多个中等概率的路径共同支撑答案，后者分别强化每条路径。整数K可用独立latent traces扩张来表示这一目标，但这只是目标分布的恒等式，不使有限组轨迹或局部decoder自动成为精确采样器；这里的a也是规定的answer string，不是经oracle认证的全部语义等价答案。

[Marginal Sharpening的受限近似](https://arxiv.org/html/2605.28142v1#S3)保留各组的prefix weights，却在下一token的局部评分中把未来continuation normalizer当共同因子丢弃，因而不能把目标恒等与实际解码等同。多组trace的KV、每token多次forward、EOS与长度截断都付费；有限数学/代码对照中majority仍可更好，特定power baseline的超时差不授总成本普适优势。目标、支持或近似误差不合适时，保留原采样、固定预算的self-consistency与独立verifier，不用分布变尖替代任务正确性验收。<!-- source-family:SF-2026-ARXIV-2605-28142 -->

Sequence power 目标也可由有限步 MH 逼近；此时每次 accept/reject 确定下一状态，天然形成串行依赖。若后续 suffix proposal 所需 prefix 已经确定，可先批量生成若干未来决策分支，再沿原 MH 规则走实际路径；未满足 prefix 条件的请求延后，保留其随机输入而非重抽，未走到的分支只消耗资源。这种预取改变执行顺序，不改变每个已提交 transition 的 proposal 和 acceptance；预测可分配预取预算，却不能删除可能结果或替代精确接受规则。[PreSTO 的受限单 GPU/固定长度实验](https://arxiv.org/html/2610.13171v1)只测 model-call 时间，有限 MH 仍不等已经达到 power 目标；废分支、KV 和更大 batch 成本必须另计，收益不足时保留串行 MH 或普通采样。<!-- source-family:SF-2026-ARXIV-2610-13171 -->

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

候选频率也可先成为reward排序的支持门，而不直接决定多数答案：从同一生成分布取得候选，按已声明的答案身份计频，先丢掉经验频率过低者，再由RM选至多k个不同项组成提交集合。[受限筛后集合选择](https://arxiv.org/html/2510.03199v1)把support与偏好排序分开，不把高频当真值，也不等交付单一最佳答案；全空或不足k时须保明确的回退/拒答，而非补造固定集合。理论所需原分布RM误差、最优答案正支持与覆盖量不由这份样本自证，依赖未知最优频率的阈值和联合渐近结论也不批准有限N逐次不退。文本等价分组、同答案各轨迹的reward均值与固定答案评分是不同人口，应共同保存规范化、阈值、N/k、generator/RM和实际判分范围，独立验最终交付的正确性。全部候选生成、逐轨迹评分、聚组/去重、选参和后续消费均付费，不能由筛后项少宣称省去了已做判分；支持、RM或预算失配时，保原多数/已验selector、可信verifier或拒答，不以更大采样数和集合中最高代理分签发可靠答案。<!-- source-family:SF-2025-ARXIV-2510-03199 -->

候选若先产生视觉 cues、再消费 cues 推理，还可把两阶段的文本 uncertainty 分开：以各段高 entropy tokens 提议局部过滤，再按两段读数及其相对变化聚合答案，而不是用整条 trace 的单一 confidence 覆盖 producer 和 consumer。这里读取的是文字生成概率，不是视觉 grounding 真值；阶段边界、warmup population、阈值与停止规则都需绑定，删掉 cue 可能让后续答案看似更自信却失去依据。[受限两阶段 selector](https://arxiv.org/html/2602.12916v1)的比较还预生成完整 traces，保留 token 数下降不能直接等同实际少做了 producer 计算或改善 tail latency；在线节省必须连同 warmup、工具、已完成与已取消生成一起计账。信号失配、视觉证据冲突或预算不足时，保留完整候选、普通 voting 或外部 verifier，不让阶段 proxy 替代 acceptance。<!-- source-family:SF-2026-ARXIV-2602-12916 -->

候选聚合还可以产生新的 trace，而不只给已有答案投票或选出一条：先从各轨迹抽取 object keys，由独立视觉 detector 标注其对象支持，再将候选子集合送给 synthesis consumer，生成下一轮候选并重新核验。[受限多模态对照](https://arxiv.org/html/2601.08010v1)支持这条 object-sensor→subset synthesis→再核验的循环接口；detector 的对象存在判断不证明关系、每一步逻辑或总体 factuality，新 trace 也不能继承旧候选的验收。应保存原输入、候选/子集合、detector 版本与阈值、迭代轮次和新旧 trace identity；共享检测误差可能被多轮聚合强化。所有初始与迭代生成、detector forward、训练 teacher 和取消的候选均计费，增加人口或轮次有边际收益、退步与额外延迟，bootstrap 置信区间不替代全训练/生成重复。视觉支持冲突、合成后质量回归或剩余预算不足时，保留原候选、普通 voting/selector 与独立 acceptance verifier，不让聚合后的叙述一致性替代外部证据。<!-- source-family:SF-2026-ARXIV-2601-08010 -->

训练这种综合器时，还要按它实际消费的候选集合定义训练人口，而不能只给原问题贴一个固定难度标签。固定生成器、候选数量与采样规则后，同题不同集合的众数答案可能有不同正确性；一条[受限数学聚合分支](https://arxiv.org/html/2509.06870v1)用已知gold将“众数错”的集合保留，再混入一部分“众数对”的集合，以兼顾从少数正确线索恢复与较密的可验证reward。这个标签来自离线答案验证，不是线上票数或聚合器自己的confidence；生成器、集合和consumer改变后，原人口资格不能直接继承。只收hard与不滤easy在局部对照中都较弱，但各配比的曝光并未完全等预算，不能把某个比例或reward密度认作唯一原因。候选生成、过滤/答案验证、综合器训练、全部候选prefill与新增输出均付费；同题多组和多次输出不增加独立题目，较短单次聚合输出也不等完整流程更便宜。新的综合答案仍需独立验收；离线训练标签无法核验、集合迁移或质量/费用失配时，保留原候选、普通投票/已验selector与外部verifier，不让离线标签或稳定多数批准真值。

<!-- source-family:SF-2025-ARXIV-2509-06870 -->

聚合单位还可从整条候选缩小到对齐片段：先按word顺序寻找多份回答的公共anchor，在anchor间对局部替代表述作语义归组，以节点/边的出现频率保存一份partial-order图，再让解码器按阈值选片段、拼接并润色，或定位分歧后核查和重新生成。[这条受限共识图分支](https://arxiv.org/html/2510.03527v1#S3)改变的是候选到交付文本的中间表示，不是比较整条回答的pairwise图；频率只来自当前同模型样本池，不是独立证据或事实概率。把subset视为等价、以最长路径代表一组表述，可能把少数候选才有的事实带入共同段落；有序对齐也不认证指代和跨片段逻辑保持，局部核查更可能漏掉共同错。最终重新生成的答案须作为新产物验收，不能继承原候选的通过标签，也不再受“只从原候选挑一条”的pass上界约束。原候选、对齐/归组与代表规则、选择阈值、局部检查和新旧文本身份应共同保留；初始多样本、两两比较、构图、润色/重生成及独立事实与完整性核验都计费，少一部分判分token不等全链省费。归组、连贯或证据支持不可靠时，保留原回答、普通vote/selector与外部验证或拒答，不由更高局部共识批准真实知识覆盖和可靠解释。

<!-- source-family:SF-2025-ARXIV-2510-03527 -->

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

多候选也不一定需要逐条重做相同概率前向：对非自回归语音分支，可共享一次CTC逐frame概率，采样并collapse成候选，再经mask/CMLM修订与多轮采样，以候选互作pseudo-reference的平均负WER选expected utility最大者。[受限NAR-MBR对照](https://arxiv.org/html/2606.17537v1#S3)共享的是概率生产，不是候选修订、抽样/缓存或二次pair评分，pseudo-reference也不是真实转录。裁共同prefix/suffix可保edit distance，但WER仍用原reference长度，不能把裁短后的分母混入。更多轮或样本并非总改善选择，encoder与decoder架构差异也未被同参数量消除。全部编码、CMLM/样本状态、CPU效用与完整转录回归均付费，固定局部测时不授服务并发/SLO；噪声、候选支持或总预算失配时，保留greedy/单样本、较小固定池与可信参考核验，不由并行概率或更多自洽候选批准正确率与普遍加速。<!-- source-family:SF-2026-ARXIV-2606-17537 -->

决定把下一批候选给谁，还要把“总共可能获得多少收益”与“当前池再扩一次还能获得多少收益”拆开。固定生成器、selector和评价量尺，令Q(n)为大小n候选池下选出答案的平均评价质量，可用多次嵌套候选子集估计 `Q(n+b)−Q(n)`，而不是只按原问题的entropy分配；起始不确定性较高可能对应较大总潜力，却不告诉系统当前是否已接近这份有限池的饱和。候选已出现后，语义多样性或最优selector分数随扩池的变化，是另一组依赖当前集合的诊断输入，不与起始entropy互换。

[受限翻译搜索诊断](https://arxiv.org/html/2610.32679v1)中，这些信号随MBR、reranking及效用/评价模型组合改变：在同一COMET量尺上显得好，不保证换量尺仍相同；用多次嵌套重采样平均后得到的相关性，也不是单次在线池的校准精度。对有限预生成池定义的95%饱和不能当无限搜索上界，按预测排序给一部分请求扩池的对照也未证明在同总预算下优于统一分配。所有候选生成、MBR两两评分或reranker、信号计算、校准和最终核验均计费；信号/selector迁移或净预算无收益时，保留已验固定N、均匀分配与可信verifier，不把离线潜力诊断升级为最优停机、普遍省算或真实答案验收。<!-- source-family:SF-2026-ARXIV-2610-32679 -->

预算也可用于先选生成策略，而不只在一种策略内增加候选数：把多数票、不同打分的best-of-N与逐轮同步的beam及其参数列成有限菜单，用query特征和菜单项预测成功率，再减去token与执行时间的软惩罚选一项。[受限双成本分支](https://arxiv.org/html/2509.09864v1)的两项成本只是训练人口上每个策略的均值，并非当前请求的精确用量或延迟；同样的token量可有不同串行等待结构，而估计效用最大的菜单项也不是全局最优、硬deadline或部署SLO保证。成功率probe依赖离线gold重复采样与校准，不能取得答案真值、未知任务可靠性或在线准入权限；候选menu、生成器/打分器、输入支持、代价口径与偏好权重应共同保存。制备标签、所有候选与逐轮评分、query编码/probe、校准搜索、模型驻留及外层服务全部计费，warm组件均值不抹去冷启动、排队和尾部；oracle差距与部分低预算质量退步仍需独立回归。任务支持、费用预测或真实质量失配时，保留固定已验预算/单路、普通多数或可信verifier路径，不由软utility为自身签发正确性或时限承诺。
<!-- source-family:SF-2025-ARXIV-2509-09864 -->

候选来源也可以先在训练期分工，而不为每个新请求在线辨认难度：用固定基座的有限成功率为训练题分桶，让多份轻量prefix分别在偏向不同桶的混合人口上独立优化，部署再把采样calls均分给这些条件生成器。[受限形式证明对照](https://arxiv.org/html/2509.12603v1)还先以偏好训练选择直接证明或显式推理的倾向；模式选择与prefix多样性是两项制备，不是同一个在线router，也不因多head就成为MoE。分桶依赖原模型、采样和checker，词面覆盖不认证独立解法或更高成功率；最终checker只认证给定形式statement与环境，不能代签原问题翻译。分桶rollouts、偏好与各prefix训练、全部候选prefill/生成、驻留和检查均付费，少输出tokens不等更低总时延。条件支持、候选质量或净预算失配时，保留固定CoT/直接生成、原policy采样与独立checker，不从一次通过或平均token减少批准通用推理能力。

<!-- source-family:SF-2025-ARXIV-2509-12603 -->

候选池也不必先生成一批样例，再要求下一批避开它们：可以先让planner提出少量语义方向，把有限generation slots均分到各方向，各worker只读原任务与自己的方向，保持后续生成无peer样例依赖。[Anchorless Diversification的有限创意对照](https://arxiv.org/html/2605.30150v1#S3)支持这种分层分配分支，不是对原答案分布的无偏恢复；planner漏掉的方向、分层重叠及等额分配都会改变支持和频率。embedding距离、regionentropy与自动质量proxy不能替人类有用性或事实正确性，已生成池的rarefaction也不证明可在线自适应早停。必须把planning、seedpool、embedding/选anchor、再生成和最终selection全计，而不能只比较返回的第二池；token倍率只在同provider与口径内解释，不等美元或墙钟收益。任务、方向质量或净预算不合时，保独立采样/简单diverge指令与可靠selector，不由更分散的pool签发新能力或所有创意任务的最优方法。<!-- source-family:SF-2026-ARXIV-2605-30150 -->

另一条候选接口让模型在同一次调用中写出多个回答及其口述概率，再由外部规则均匀选择或按这些数值重新加权；[Verbalized Sampling的有限对照](https://arxiv.org/html/2510.01171v1#S4)支持比较这种提示与直接/列表提示，但没有证明口述数等于token logprob、正确率或基座分布。候选共享生成前缀，遗漏、重复与格式错误会改变最终law，低口述概率指令也不是token截尾。须分别绑定候选数、parser/去重与归一、均匀或加权消费者，并同时验覆盖、质量和安全；同返回N不等同tokens或时延，部分模型质量与拒答率仍退。候选/概率文本、CoT、多轮history和选择全计费；小模型、校准或预算不合时，保留普通独立采样、简单列表及可信selector，不把更分散的文本或与语料proxy更接近当成原分布恢复与安全证书。<!-- source-family:SF-2025-ARXIV-2510-01171 -->

## 约束输出：合法前缀、完整序列与内容正确

前面的 penalty 与 grammar mask 已足以定义单步选择，但更强的输出要求会暴露三个不同缺口：前缀是否合法、能否在预算内完成，以及完成后的内容是否正确。下面先处理可形式化的输出空间，再检查格式条件怎样改变内容，最后划清风险控制与接受证据的边界。这些条件分支不要求同时启用。

### 大型有限输出集合适合专用 Trie Automaton

当合法输出是一个很大的有限集合时，通用 grammar 每步解析会重复计算，而 trie 可以把共享前缀编成紧凑 automaton，只允许仍可到达某个合法叶子的 token。它以预处理时间和内存换取稳定 decode；集合频繁变化、语义约束开放或 tokenizer 不一致时，专用结构的维护成本会超过收益，应回退通用 constrained decoding 或后置验证。
<!-- source-family: arxiv:2608.12574v1; semantic-body-binding: finite-set-trie-decoding-path -->

对于不能预先枚举成有限集合的上下文无关输出，专门改写 parser 并不是唯一办法。另一分支先把原语法编成生成全部合法前缀的 prefix grammar：完整左侧片段保留原产生式，截断边界使用对应的前缀非终结符，再交给普通 parser。在权重满足相应可求和、交换半环条件且 parser 正确时，它保留前缀权重；对所有单 token 延伸求权重，若解析器支持 lattice、仅以半环运算求值且控制流不依赖这些形式变量，还可把末端扩展写成带形式变量的 lattice，经代数反向传播一次取得权重向量，避免逐候选重跑。这是语法权重，不是任意神经模型未来所有合法 suffix 的条件概率。<!-- source-family:SF-2026-ARXIV-2604-21191 -->

[必要定理与受限对照](https://arxiv.org/html/2604.21191v1)只把输入长度依赖交给原 parser；binarization、prefix transformation 与 parser 自己的预处理仍可扩大 grammar-structural factors。反向传播的常数界是算术操作数，不保证 wall-clock、内存或 LLM serving 吞吐；lattice 支持也须实际实现。编译、规则驻留和每步解析均计费，同一语法跨请求复用才可摊销；语法常变、预处理膨胀或预算不合算时，保留专用 prefix parser、有限集合 trie 或后置验证，另验输出预算与内容正确，不由高效解析批准完整任务。

### Prefix Feasibility 不等于能在 Token Budget 内完成

有限集合可以沿共享前缀定位合法叶子；对于带嵌套结构的输出，除了“不走入非法路径”，还需要知道剩余预算是否够走到接受状态。

一个前缀仍可扩展为合法输出，只说明没有进入死路；它可能距离 accepting state 太远，最终在 token budget 用尽时截断。带栈约束的解码可以同时维护 PDA reachability 与 distance-to-acceptance，在接近预算时优先选择可完成路径。这样提高结构完成的 soundness，却增加预处理、beam 状态与运行开销，也不能表达所有语义约束；自由文本仍需后置验证。
<!-- source-family: arxiv:2608.28229v1; semantic-body-binding: constrained-decoding-distance-to-acceptance -->

### Stateful Exact Conditioning 是有限状态约束的条件分支

保证最终合法，仍不意味着按照原模型在所有合法完整序列上的条件分布抽样。只有应用需要这个更强分布语义时，才值得承担全局条件化的状态与计算成本。

Rejection sampling 或生成后 repair 在约束稀疏、状态难形式化时最通用，却可能反复产生无效前缀。若约束能编译为冻结、可判定的有限状态 validator，且模型对 prefix 的依赖也能被足够小的状态精确汇总，可以把二者做 product construction，并在可计算未来接受概率质量的条件下精确条件化。合法性 soundness 与保持原模型在合法完整序列上的条件概率是不同保证；仅屏蔽当前非法 token，并不自动实现后者。多个约束会使 product state 乘法增长，模型状态自身也可能无法压缩到可处理规模；约束过大、动态或模型无法满足这些计算条件时，应回退 grammar mask、rejection 或生成后验证，不能把局部 validator 当作开放语义正确性证明。

<!-- source-family: arxiv:2608.08282v1; daily-trace: papers/2026/08/11/README.md; semantic-body-binding: finite-state-exact-conditioning-product-cost -->

约束语法简单，也不意味着全局条件概率容易计算。对一类描述长度有限、每步 next-token 概率可在多项式时间精确计算的自回归模型，即使约束只是“固定长度后以 eos 结束”，合法序列的总概率质量也可编码满足赋值计数，因而其精确计算是 #P-hard。困难在未来所有 suffix 的模型概率，而不只在 validator 有多少状态。有限状态 Markov 模型配合有限状态约束仍可用动态规划；一般 prefix-dependent 模型则需要另证模型状态汇总与 continuation mass 的可计算性。这个计数复杂性反例不证明每个具体模型都很难，也不证明任何可能的 exact sampler 都必须显式计算归一化常数；它限制的是通用、可高效的全局条件化保证。<!-- source-family:SF-2026-ARXIV-2604-07855 -->

全局未来质量难算时，还可另训较小的概率代理，而不声称已压缩原模型的全部prefix状态：从模型回答蒸馏HMM，将它与模板DFA做递推，估计候选token之后最终满足格式的概率，再把原next-token概率乘以这份估计的幂并重归一。[这一受限软条件分支](https://arxiv.org/html/2510.03595v1#S3)把解题主干、格式语言和未来合规估计器分开；只有估计恰为同一原模型、同一任务条件下的真实未来接受概率且幂为1，才对应原模型在合法完整串上的条件分布。只蒸馏continuation而不喂原instruction的HMM拟合的是任务回答混合分布，不是当前问题的完整条件；稀疏剪枝、额外调强和greedy选择还会继续改变law。有限模板/trie的可达与接受状态、输出长度及tokenization必须独立核验，软分数不能替任意schema的硬合法性，更不能批准抽取span、角色或答案正确；平均保留高概率质量也不保稀有合法分支的相对误差。须共同保存原任务/prefix、两模型与分词器、模板/终止、剪枝和幂参数，分别回归格式、内容与分布目标；全部教师采样、代理训练、状态表驻留、每token递推/重权和独立内容验证均付费，局部FLOPs不等完整解码净速。代理失配、内容退步或预算不合时，保原模型、已验grammar mask/普通拒绝采样和独立语义校验，不由样本格式全对批准精确原law或更可靠推理。

<!-- source-family:SF-2025-ARXIV-2510-03595 -->

无法求全体合法后缀的概率，也不必每次拒绝后忘掉已经证明无效的分支。若前缀检查器能可靠证明某个前缀没有任何合法延伸，可把这些前缀保存在排除树中，只计算这份已知无效集合的概率质量；下一次从原模型避开该集合后重新归一化的分布提议，再检验完整输出。设剩余质量为 `Z_W`、合法集合为 `L`，固定历史下提议有效串 `w` 的概率是 `P(w)/Z_W`，接受概率是 `P(L)/Z_W`，因此给定接受后的分布仍为 `P(w)/P(L)`。这不要求预先知道 `P(L)`，却要求它为正、模型几乎必终止、排除质量算准且不删任何有效串。

[自适应拒绝采样的有限分析](https://arxiv.org/html/2510.01902v1#S3)把提议效率与接受后的分布分开：新增有正质量的无效分支才能提高接受率，重复或零质量发现只持平，极稀少的合法输出仍可耗尽预算。原prompt、模型/tokenizer、温度与截断、约束和树必须共同绑定；经验失败、timeout或不可靠judge不能批准永久剪枝，误删合法分支便改变目标分布。前缀合法不保任务语义或完整计划成功，有限SQL对照也有超时。树/全词表检查、概率回传、状态内存及全部重试都付费，完整序列尝试数不是token前向数或净墙钟；检查器、数值或预算不可靠时，保留普通拒绝采样、已验grammar与后置核验，不由非减接受率批准通用高效或安全。

<!-- source-family:SF-2025-ARXIV-2510-01902 -->

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

- `SF-2025-ARXIV-2510-22475` - Daily2025-10-29补Oct28；[exact-v1](https://arxiv.org/html/2510.22475v1)，必要方法/支持/直接反侧见本日EVIDENCE或sole reader记录。新增同prefix条件logit聚合与标量confidence反例；不把persona当独立证据，也不照录其权重公式为概率混合。 未核实现或复现；PRE/真实SAVE/自读/actualPOST仅本日canonical后到记录，不由本注预签。

- `SF-2025-ARXIV-2510-13285` — Banach，Daily2025-10-17补Oct16；writer exact-v1 §3–5及Hegel R25必要复用，2+1+2=5，仅参考activation椭球/方向编辑与真实支持分责差额深入。保PCA40%/Mahalanobis95%、负判别式最近点仍可在外/a=0与奇异协方差未闭、SPI负向/MMLU拒答反退、同人口F1/PPL非事实及全费；不采always-ID/完整配方或实现复现，完整PRE/SAVE/自读/solePOST据canonical。

- `SF-2025-ARXIV-2510-12343` — Herschel，Daily2025-10-16补Oct15；消费Cicero R32 exact-v1 §1.2/2.1–2.2/3.1–3.3/4.1–4.4首次必要，2+2+2=6，仅近似onehot混合/坐标排序与embedding consumer差额。保plaintext非HE、诚实但好奇非恶意安全、TSP/PP式和cosmetric未闭、LoRA混杂及O(V²)/训练/加密全费，不授隐私部署或精确误差定理。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

- `SF-2026-ARXIV-2610-32980` — finish3，Daily2026-10-27补Oct26；N42采用exact-v2§3/4关键及C计时，R294 v1→v2受影响有限比较复用，首次拟2+2+2=6，不另增家族/不改旧日期。仅onebackbone concept/lightdecoder全ARbeam与generatorstate边界；保非exactheavy/非spec、goldprefixKD/τ1条件、copy O(T)/正mass、低Flat分项/小backbone反慢与全费。H10080GB/bf16/compile/CUDAgraph/beamshared，50ms是GPUbatch非requestSLO，未核代码/像素/服务复现/完整GPUh；不授全域排名、无损或净部署收益，PRE/SAVE/POST只后到。

- `SF-2026-ARXIV-2610-32098`，Daily2026-10-27；exact-v1 §3–4/A.1–A.2必要条件、§5.1/5.4–5.6/T1/3、B.2/C.1直接归因与成本首次必要，2+2+2=6，仅fullitem-score到prefixedge的pre-prune接口深入。保native概率未改/非真值、target已在frontier/每depth充分条件、gate未校准/score尺度、gold仅离线hit条件人口且多数hitloss非beam、原survivor displacement、同B更慢/低B fusion反侧和batch32warm测量边界。未核其余附录/图像素/代码或复现，不授通用推荐/LLM质量、训练seed等价或服务SLO；PRE/SAVE/完整自读/sole POST仅后到真实层。

- `SF-2026-ARXIV-2610-32679`，Daily2026-10-27；exact-v1 §3–5/F/G与资源披露首次必要复用，2+2+2=6，仅总潜力/剩余marginal与selector/量尺依赖的有限诊断深入。保1024有限池/20重采样平均非在线单池、Comet目标对齐、AppF跨量尺变化、选择扩池非同总预算uniform比较及无E2E时延/CI；不采最优controller/免费信号或人类质量保证。未核代码/推理复现；PRE、SAVE、自读与sole POST仅据后到真实记录，不由本注预签。

- `SF-2025-ARXIV-2510-05987` — Cicero，Daily2025-10-09补Oct08BJT；[Sample Smart exact-v1](https://arxiv.org/html/2510.05987v1)A178首次必要§2–5/Eq1–11/T1/3/§7/A1/2决定域/A5/6全T5/A9，2+2+2=6，仅参考匹配统计producer与候选截断consumer差额深入。保gold/rollout人口差、Eq6均值乘积与稀疏/非单调rank未闭、固定cutoff、代码/AIME反退与全费，不采语义oracle、epistemic唯一因果/全任务保证。未核T2/全部附表/图像素/代码或推理复现；PRE/SAVE/selfread/solePOST仅本日canonical，不以本注预签。

- `SF-2025-ARXIV-2510-03632` — Arendt，Daily2025-10-08补Oct07；原6，直接采用root R276唯一exact-v1 S3–4/T1–6/A/B/S6必要，不第二Methods。仅question-on/off步骤分数到搜索/终局consumer的差额；保BOS非真边际、step/token归一、entropy分位/tie与负分乘frequency、共prefix依赖、Qwen/StrategyQA反退及全部节点/双评分/KV费用。不采逻辑真值、完整动态recipe/最优time-accuracy或精确原law，未核全部case/像素/代码或复现；PRE/SAVE/fullselfread/solePOST仅本日canonical真实后到层，不以本注预签。

- `SF-2025-ARXIV-2510-03595` — Arendt，Daily2025-10-08补Oct07；原7，直接采用root R266唯一exact-v1 S2–5/A–E/H及F/G必要，不第二Methods。仅HMM未来合规proxy/模板资格/原law与内容消费者分责；保continuation-only/空初始prefix非this-query条件、gamma2/prune/greedy非exact、top200均值97.8%非稀有分支保证、T1/T2/T3反退及全部56GPUh教师采样/代理训练/DP驻留费。不采通用schema、语义真值/精确原模型条件采样或端到端近零开销，未核全图像素/全部prompt/代码或复现；PRE/SAVE/fullselfread/solePOST仅本日canonical真实后到层，不以本注预签。

- `SF-2025-ARXIV-2510-03527` — Arendt，Daily2025-10-08补Oct07；原6，直接采用root R251唯一exact-v1 S2–4/B/C真Alg1/E真Alg2–5/F/G/I必要，不第二Methods。仅word-anchor/局部语义partial-order图到选择、核查及重生成的消费者差额；保subset等价/最长代表加事实与非传递、频率非独立真值、GSV新生成非原候选Pass@m界、F25传记样本非全事实/支持覆盖、阈值/人口/小切片反退与全采样构图编辑费。不采开放truth/全部可靠拒答或全链82%净节省，未核全部表/像素/代码或复现；PRE/SAVE/fullselfread/solePOST仅本日canonical实际后到层，不以本注预签。

- `SF-2025-ARXIV-2510-06052` — Cicero，Daily2025-10-09补Oct08BJT；[MixReasoning exact-v1](https://arxiv.org/html/2510.06052v1)§3/4.1–4.4/T1、Fig3–5caption与A.1–2必要，2+2+2=6，具体adapter模式/windowrollback与cache路径差额深入。保fixed-alpha重算非混合状态、MLPonly不证KV不变、阈值文字方向冲突、localentropy非正确/因果、质量反退及全费，不采fullreuse/唯一MLP定位、固定长度或E2ESLO。未核图像素/代码/复现，PRE/SAVE/selfread/solePOST按本日canonical，不以本注预签。

- `SF-2025-ARXIV-2510-02919` — Meitner，Daily2025-10-07补Oct06；[SRGen exact-v1](https://arxiv.org/html/2510.02919v1)Boole R121唯一首次必要§2–6/B1–2/CAlg1/D/F–H必要，2+1+2=5，作者仅actualowner/当前hidden瞬态inner loop与self-prefix监督差额深入。保confidence错漏/旧错自标、global非fewstep、温度/λ建议未闭、表文/flip人口及prefix-head费用，不采语义无损/通用50%上界/净速；未核全像素/代码/复现。PRE/SAVE/POST仅本日canonical实际层。

- `SF-2025-ARXIV-2510-03199` — Meitner，Daily2025-10-07补Oct06；[BoM exact-v1](https://arxiv.org/html/2510.03199v1)Boole R94唯一首次必要§3–8/Alg1–3/式3.1–5.1/A/B1–4，2+1+2=5，作者仅actualowner/频率support与RM集合分责差额深入。保未知C*/空集合、联合渐近非逐N单调、阈值/union印式与gap可行域、轨迹评分/答案聚组人口及全费，不采全域minimax、正确性或省RM调用。未核曲线像素/代码/复现；PRE/SAVE/POST仅本日canonical实际层。

- `SF-2025-ARXIV-2510-03223` — Meitner，Daily2025-10-07补Oct06；[Self-Anchor exact-v1](https://arxiv.org/html/2510.03223v1)§2.1/3.1–2/3.4–8/T3–4及B/D/E必要，2+1+2=5，自动plan-selector与条件logit差额深入。R45必要实际独核复用；保Eq3/ω映射不足、概率非正确attention、位置/格式与成功链人口、约23%局部吞吐降幅及全部双forward/结构/验证费，不采head干预、通用RL替代或SLO。未核代码/图像素/复现；PRE/SAVE/POST按本日canonical实际状态。

- `SF-2025-ARXIV-2510-01171`：Daily2025-10-03补Oct02；[Verbalized Sampling exact-v1](https://arxiv.org/html/2510.01171v1#S4)，2+1+3=6/具体候选消费者gap深入。只联合候选+口述权重与外部uniform/weighted选择分责；保非logprob/校准/原law、E.4构造非学会/完整支持、RedPajama proxy、质量与Qwen/拒答反退、同N非全费。不采RLHF唯一因果/普遍多样性无损或安全，未核全部synthetic附件/像素/代码或复现。R21原分/日门复用；root R46必要/actualowner/整体PRE与本次窄授通过，已真实SAVE/fullselfread；root R49本项唯一实际POST通过，指定窄位释放。仅行政同步既成，不预DAY。

- `SF-2025-ARXIV-2510-01394` — Hilbert，Daily2025-10-04补Oct03；Optimal Stopping exact-v1 §2/3.1/4–6/Alg1必要，2+1+2=5，prompt-local reward-tail效用与追加回答停止差额深入。保iid/固定单次费、分布族/anytime上界、good-event理论与实用fit分责、LCB/UCB变体差别和960缓存/100回放全费；不授任意分布最优、用户真实acceptance、无reward hacking或生产SLO。未核Appendix全部证明/代码/图像素或复现；实际PRE/POST只按唯一reader已发生记录同步。

- `SF-2025-ARXIV-2509-21091` — Socrates，Daily2025-09-27补Sep26；[Best-of-infinity exact-v1](https://arxiv.org/html/2509.21091v1) S2–5/Alg1/E1–13/Theorem1/直接Lemmas、A2/A3/A6.4–5必要，2+1+2=5。作者77→Helmholtz R71一次必要实际采用；仅计数/未见类别后验停止与有标签离线混合权重分责，不授有限δ、mode正确/严格MILP tie等价或全预算最优。保DP/Dirichlet与prior近似、MC/不可解析删除/池内重复、跨年59未达与selector反退、截断judge/无E2E全费，不授实现复现/SLO。未核全部曲线/图像素/代码。本原三项已Helmholtz R79整体纯PRE通过，root本轮fresh明确独立新窄授；按原技术稿真实保存，writer已完整自读新增/完整两侧及本人注，Helmholtz R81唯一actualPOST通过，I15生效且指定正文/本人注窄位释放；本尾仅同步既成行政事实，不第三Source/PRE/POST或授DAY。

- `SF-2026-ARXIV-2606-01682` — Daily2026-06-03补Jun02；exact-v1 §3/Eq1–4、§4.1–4.8/Table1–5及Limitations，2+1+2=5；仅chunk内likelihood选择/长度偏好边界，不授true target-law、逻辑正确或免费/净速度，保EOS短段、matched interventions非matched FLOPs、同family/math/PRM与小greedy反侧及全费。必要Source/actual owner/精确PRE经独核R22–24，root已实际保存最小段，非writer jun03_next_reader已真实完整新增/直接两侧/本人注唯一actualPOST通过(R25)，生效释放；本句仅同步既成事实；未核代码/复现，不授完整DAY。

- `SF-2025-ARXIV-2509-12603` — Socrates，Daily2025-09-18补Sep17；[exact-v1](https://arxiv.org/html/2509.12603v1)§2–4/6、式1/表1–4及必要图注，2+2+2=6，reader65必要Source通过。仅原模型成功率桶→独立prefix训练→均分calls与模式偏好训练分责；保PDC非语义独立、Goedel/ProofNet反退、表2费用比例/IR口径冲突、checker形式身份与全制备/执行费用，不授全榜无损/总墙钟收益或新PPO算法。未核实现/复现；原三项按root独立fresh窄授真实保存并完整自读，Helmholtz88唯一actual完整新增/完整两侧及binding/本人注POST已通过，I16生效且指定位已释放；本尾仅同步既成行政事实，不第三正文/Source/PRE/POST或授DAY。

- SF-2025-ARXIV-2509-07676 — Darwin，Daily2025-09-11补Sep10；exact-v1 §2–5/式1–5/T1–2、Limitations及A2/A3/T3–6必要域，Bacon201首包→Darwin129一次缓存必要采用，正式2+1+2=5。只跨prefix累计概率质量与cap控制中途宽度；gold/proxy分责、剪枝支持/非truth、PPL/长度边界及完整费用/慢侧保留。不读图像素/代码或复现；唯一MODEL-SAMPLING Ch20窄gap，Bacon210纯PRE与root本次fresh窄授已过，Darwin按130原稿真实保存，Bacon215唯一actual完整POST已通过，本轮I8生效且窄位释放；仅同步既成状态，不预DAY。

- `SF-2026-ARXIV-2610-24715` — Daily2026-10-21/Oct20；C14必要exact-v1 Source/actual owner/完整PRE由reader R224具名通过，按root既授精确窄位保存核准单段/唯一marker，保受限理论/直接反侧和全部费用；未核实现/复现。作者完整新增/直接完整两侧/本人注自读后待唯一非writer actualPOST，不预生效/DAY。 截至本轮，唯一非writer R226 actualPOST已实际通过并生效；上述待POST只保历史过程，不再表示当前未完。仅行政同步，不第三核正文/Source。

- `SF-2026-ARXIV-2605-30150` — Daily2026-05-30补May29，2+1+3=6；exact-v1 §3–6/A必要域见A47/R84，仅无seed方向planning→有限slots分层candidatepool。保方向漏/重叠非原分布恢复、embedding/自动quality非人类有用、rarefaction非online早停与完整pipeline费用，不采跨provider美元/墙钟或AIfS展望。未核实现/复现。reader R84 Source/当前owner/原PRE通过，root授本单段+本人note，已真实保存，唯一reader R87实际完整新增/直接两侧/本人注POST通过并释放。

- `SF-2025-ARXIV-2509-06701` — Darwin继任Godel，Daily2025-09-10补Sep9；Bacon210/作者164最小P/day、Bacon214首理论稿/作者166一次非准备者必要采用，正式2+1+2=5，唯一Ch20小gap。实际必要域v1共同有限正概率空间/§2–3定义、C/D/E全部相关证明；仅采自定义log-welfare、正权linear与two-binary边界及n+1构造存在性。不授任意固定三结果/任意给定belief与weight、真值proper-score或神经persona/安全控制保证；partial1192451B中必要域均闭合，不冒整稿或缺尾I/J已读。多模型/权重/归一/状态与真实结果验收费保，未核实现/复现。Bacon216原三项/完整邻接PRE通过，root本次fresh精确授后已真实保存；仅待Bacon一次实际完整nonwriter POST，不预整合或DAY。

- `SF-2026-ARXIV-2605-08083` — Daily2026-05-12补May11；[exact-v1](https://arxiv.org/html/2605.08083v1)必要§2–5/T1–3/§7沿reader实际Source复用，2+2+2=6，为frozen replay搜索controller与真实运行分责差额深入。保有限128预采/64池复用、unrevealed probe隔离、AIME24选择非heldout、质量反退及全部预采/在线费用，不采AppD完整recipe、全Pareto或SLO，未核实现/复现。reader实际owner/逐字PRE通过，root已授指定一段/本人注，现已保存待非writer实际POST；不授DAY。 截至本轮后续有效结论：本项独立reader已实际完整新增/直接两侧/本人注非writer POST通过，root已接纳并释放指定窄位；此前“待”仅过程时态，本次纯行政同步、不重Source/正文、不预授DAY。

- `SF-2026-ARXIV-2610-22160` — Daily2026-10-17窗10-16；[EMO exact-v1](https://arxiv.org/html/2610.22160v1) §3–4/Alg1/必要B.3，2+1+2=5。只采相邻context同prefix双stream与Jacobian投影接口；保masked alignment条件、judge选择缺口、11/40相对context-only退步与judge/rewrite完整费用，不授单调accuracy或matched-compute。root已独核必要Source/最小PRE语义并授本两段及本注窄写；作者已保存并顺读；root已实际新两段、完整局部邻接及本人注非writer POST PASS，作者仅行政同步既成事实，不预签DAY。未核代码/复现。

- `SF-2026-ARXIV-2605-00419` — Daily2026-05-05补May04；[exact-v1](https://arxiv.org/html/2605.00419v1)必要§3/4/A.1–3，2+2+2=6。reader R15必要Source/date/具体owner通过，root C4 actual逐字PRE与完整邻接并授两段+本人注；只采probability-mixture随机选择等价与lazy prefix/KV分责，保λ搜索/局部反退及全部同步状态费用，不授argmax/logit/top-k任意等价或通用单模型延迟。作者已实际保存，root C5非writer实际正文/完整局部邻接及本人注POST通过，窄lease已释放，不预签DAY；未核artifact/复现。

- `SF-2026-ARXIV-2604-27039` — 原路由为Daily2026-05-02补May01（保留历史字段，非已核公开日）；reader R79/R80发现早提交至registered跨日且有限原始日组未恢复，实际May1归属未确认，隔离于本窗候选/覆盖/整合计数；技术审阅与有效正文保留，取得该ID官方首公告日或同日有效组合后仅恢复日期层；exact-v1 §3/4、必要E/F/G，2+1+2=5，因具体知识差额及控制符号冲突深入。只采用固定policy MC长度value/非线性inverse与extra-forward成本；Eq11/12解代数相符，但负beta偏更负value与shorter文字相反，精确tilting/相应性能因果保留争议，不默修或授RL已验。reader必要Source反核R3、actual owner/逐字PRE R8通过，root授指定两段及本人注窄lease；作者已保存并顺读完整邻接，非writer reader actual POST R10通过，root接纳并释放该窄lease；仅行政同步本注，不授DAY。未核实现/复现。

- `SF-2026-ARXIV-2604-22345` — Daily2026-04-28补Apr27；2+1+2=5，referenceNLL单headmask选择→原/masked双流profile条件采样，PCS非偏好专属/唯一storage、generic仍含profile、共享prefillKV/净费未证及反侧近文。reader必要Source/date/实际owner与修后逐字PRE通过，root授指定单段+本人注窄lease；作者已保存并顺读完整邻接，reader实际非writer正文/完整两侧/本人注POST已通过，root接纳释放指定窄lease；作者仅行政同步本注并实际读回。未核实现/复现，不授DAY。

- `SF-2026-ARXIV-2604-21191` — Daily2026-04-25补Apr24；[exact-v1](https://arxiv.org/html/2604.21191v1) §2–4/Fig1/AppB/Limitations，2+1+2=5。普通parser的prefix grammar与lattice/AD差额必要深入；保可求和半环、lattice支持/theta独立控制流、grammar预处理与算术ops非SLO条件，不授神经未来mass。非作者supp_apr25_review_fresh actual必要Source/date/owner/PRE修订通过，root逐字及插点授两段＋本注窄lease；作者已保存，非writer supp_apr25_review_fresh已实际顺读Ch20完整局部两侧及本人注并核限定diff，POST通过，root接纳释放本窄lease；作者仅行政同步并实际读回；未核代码/复现，不授DAY。

- `SF-2026-ARXIV-2604-01161` — Daily `2026-04-03`；[Reasoning Shift exact-v1](https://arxiv.org/html/2604.01161v1) §3–4/必要A/B。2+2+2=6，限定context-conditioned stop/effective-budget差额；same-prefix重采样非完整质量中介，subtask分摊非同budget，个别长生成与Prefill费用保留；work-in-progress，不授已开发mitigation、内部推理因果或生产保证。必要Source复用有效独核，准入本轮补核；root/reader实际PRE通过后窄写，reader实际正文/完整邻接/本人note nonwriter POST通过，未核代码/复现。

- `SF-2026-ARXIV-2610-13171` — [PreSTO exact-v1](https://arxiv.org/html/2610.13171v1) §3/Condition1/Alg1–2、Prop1 A1–A3、§5/D.2–3；Daily2026-10-13，2+1+2=5，具体MH执行缺口深入。prefix条件、defer保随机输入、原acceptance与有限K分开；single GH200/H100、固定1024无EOS/首20prompts、model-call速度、废分支和29/38局部统计非全分布证明保留。root必要Source/PRE通过，root实际非writer局部正文/邻接与本注POST通过；未核code或复现。

- `SF-2026-ARXIV-2603-14591` — Daily `2026-03-18` 补 `03-17` 自然日；[FlashHead exact-v1](https://arxiv.org/html/2603.14591v1) §3.1–3.3、§4.1–4.5/§5、Appendix C/D/D.1，2+1+2=5，具体采样语义差额定点深入。仅采用全 support 与 dense 目标分布分账、随机集合边缘化和资源/误差回退；不授精确 dense 采样、head 倍率即端到端、MC clip 即精确 likelihood、大 batch/生产 SLO 或实现复现。review_mar17_18 必要 Source、actual owner/Ch19–21 交接及逐字两段 PRE 通过，root 授两段与本注窄锁；作者写后完整局部邻接已顺读，review_mar17_18 非 writer 实际正文 31–82、完整局部邻接及本注 POST 通过，不授 DAY。

- `SF-2026-ARXIV-2603-06797` — Daily `2026-03-11` 补充；[exact-v1](https://arxiv.org/html/2603.06797v1) §3–4/Eq17–18/Alg1、必要 A.3 与 C.3。2+1+3=6，已确认 prompt-specific 尾部选择差额深入；只采 Hill→α→候选 power 权重的启发式及代价，不采 Eq11/A.32/闭式归一的最优性继承。原文尾端保护、独立校准人口与运行费用未披露，反侧近正文；review_20260311 必要 Source 独核通过，root 实际读取本章完整局部与前后章交接后窄写。supplement_20260311 非写入者实际顺读 324–377 完整局部与自身末注，回对 Alg1/Eq17–18/必要数学反侧，POST 通过。未核实现或复现，不授日级完成。

- `SF-2026-ARXIV-2601-06403` — Daily `2026-01-14` 增量；[exact-v1](https://arxiv.org/html/2601.06403v1) §3/Eq3–5、§4–5/Table1、Limitations。2+1+2=5，具体 same-prefix 双 system logits 与连续强度缺口深入；alpha0 为 custom，2×FLOPs、ID/严格准确反侧与原提示回退近文，不授默认权威/缓存共享已实证。peer必要原证/actual owner PRE通过、root授窄锁；作者实际正文与完整邻接顺读，root 非写者 actual POST 已通过（新正文、完整局部邻接与自身末注实际顺读）。未核 artifact/复现，不授整日完成。

- `SF-2026-ARXIV-2601-05693` — Daily `2026-01-13` 增量；[exact-v1](https://arxiv.org/html/2601.05693v1) §3.2–3.3/4；sentence-hidden→CUSUM/persistence；balanced人口/高FPR/非直接缓解近文；2+1+2=5，具体差额深入。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

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

- `SF-2026-ARXIV-2601-08010` — Daily `2026-01-15`；[exact-v1](https://arxiv.org/html/2601.08010v1) §4/Eq1–6、§6/Tables1–3、AppC/D1–4。2+1+2=5，object-sensor核候选→subset synthesis生成新trace→重核的具体gap深入；对象存在不授关系/逻辑/总体truth，DINO相关error与全部生成/检测/teacher费用近文。Table6同NKT有限增量与SFT反退、更多轮次边际/退收益保留，不采Eq13–14为标准ratio-GSPO配方。review_jan15_delta必要原证/actual owner PRE通过、root仅授本段＋自有末注窄锁；review_jan15_delta实际顺读Ch20正文366–409/394及本末注，actual POST通过，root窄锁释放，未运行实现/复现，非日级验收。

- `SF-2026-ARXIV-2601-08441` — Daily `2026-01-15` 增量；[exact-v1](https://arxiv.org/html/2601.08441v1)；2+1+2=5，review_jan15_delta必要原证/actual owner具体PRE通过，root授该处单段及自身末注窄锁；仅采用接口分工，局部反侧/完整费用与旧路径回退近文，不采不完整solver或普遍性能/安全保证。作者正文完整邻接已顺读，review_jan15_delta已实际独读新段/完整邻接及自身末注，actual POST通过，root窄锁释放。未运行实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-09438` — Daily `2026-02-12`补遗漏；[exact-v1](https://arxiv.org/html/2602.09438v1)。本日具名必要方法、关键评价与直接反侧由root独立Source限定通过，actual owner/局部邻接及逐字拟文PRE通过后授窄锁；作者已写最小差额，review_20260214非作者实际新正文、完整局部邻接及本人末注POST通过，窄锁释放，不授DAY。原件与配置/中心争议边界见本日同名前缀review笔记；未核artifact或复现。

- `SF-2026-ARXIV-2602-09486` — Daily `2026-02-12`补遗漏；[exact-v1](https://arxiv.org/html/2602.09486v1)。本日具名必要方法、关键评价与直接反侧由root独立Source限定通过，actual owner/局部邻接及逐字拟文PRE通过后授窄锁；作者已写最小差额，review_20260214非作者实际新正文、完整局部邻接及本人末注POST通过，窄锁释放，不授DAY。原件与配置/中心争议边界见本日同名前缀review笔记；未核artifact或复现。

- `SF-2026-ARXIV-2602-11683` — Daily `2026-02-14`补查；[ThinkRouter exact-v1](https://arxiv.org/html/2602.11683v1) §3–6，temperature-scaled pmax/filter前、discrete/soft位置路由；Random coding及离散数学局部更高，不授confidence真值/多世界/KV或全Pareto。2+2+2=6，实际owner差额受影响深入。root/reviewer必要Source及actual owner/完整邻接与逐字拟文PRE通过，root授两段+本末注窄锁；作者已写并顺读完整邻接，review_20260214已实际独核新正文、完整邻接及本末注，非作者actual POST通过，root释放窄锁，不授DAY。未核artifact/复现。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2602-12276` — Daily `2026-02-14`补查；[exact-v1](https://arxiv.org/html/2602.12276v1)，2+2+2=6。必要Source非作者限定通过，root actualowner提案与review_20260214非writer逐字PRE通过，root授本一段及本人末注窄锁；作者实际新正文/完整局部顺读，root非writer actualPOST通过、窄锁释放。费用、反侧、代理身份和旧路径回退近正文，不授全recipe、真实概率/安全/性能保证、实现复现或DAY。 本轮补查事件的首次公开日期未证，必要Source/PRE/实际POST研究仍有效，但不计本日已确认新增成果；归属只按[本日日报§5](../../papers/2026/02/14/README.md#5-缺口与下一步)的57日期请求定点重开，不撤正文或补造公开日。

- `SF-2026-ARXIV-2603-05739` — [2026-03-10补查](../../papers/2026/03/10/README.md)，[exact-v1](https://arxiv.org/html/2603.05739v1) §2.1–2.3/Thm3–5、§4、§5.1、§7；受限理论。正文区分expected reward与win-rate、pairwise误差与reference-tail coverage，并保留M校准/有限采样/独立样本条件；不授任意搜索最优、每实例单调、事实正确性或部署无reward hacking保证。必要原证与实际owner邻接已读；supplement_20260310非写入者实际正文/完整局部邻接及末注POST通过，日级补查验收以日报为准，未执行artifact或复现。

- `SF-2026-ARXIV-2603-08999` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.08999v1) §3–8/Eq1–6/Tables1–4，2+1+2=5；completed-trace采样门控差额深入。全greedy后非因果features只管追加预算，每LLM classifier/每targetval阈值、n.s.非等价、全部首轨迹/option评分/特征与判别成本近正文。不采在线earlyexit、无校准迁移、currentv4数字、未核曲线/全部附录、实现/复现或完整SLO。root独立必要§3/5/8及Tables1–4/日期/actual owner逐字PRE通过（不反称其全部§4/6设置）；作者按窄锁写两段与本注并顺读完整局部，非writer root实际顺读347–375完整邻接、新354/357与本注并回对必要原证，actualPOST通过，窄锁释放，不授DAY。

- `SF-2026-ARXIV-2603-12529` — Daily `2026-03-17`补03/16自然日；[exact-v1](https://arxiv.org/html/2603.12529v1)，2+2+2=6，必要核心/关键反侧及具体差额见本日SUP_STOP_CONTROL_PRE_20261011.md。supp_mar17必要Source、实际唯一owner/完整邻接与逐字PRE由review_mar17_18独立局部通过，root授本正文与本人注窄锁；作者按PRE实际写入，review_mar17_18非writer实际顺读246–293完整局部、新264与本人695注，回对已核必要Source/逐字PRE，局部POST通过；resume_review17_18最终末注定点回读局部通过，不授DAY。采用范围、费用、反侧及原路径回退近正文；未核artifact/复现。

- `SF-2026-ARXIV-2603-18428` — [exact-v1](https://arxiv.org/html/2603.18428v1) §3–5/Eqs1–2/Tables1–2；只采用冻结基座外的prefix-state→T/top-p控制接口。periodic离线controller更新≠线上逐轨迹学习；小模型摘要/单fixedT基线、reward代理、负early→late与ROUGE-only反侧及全部费用保留；不授通用稳定、事实正确、低风险或零开销，未核实现/复现。

- `SF-2026-ARXIV-2603-18411` — [TARo exact-v1](https://arxiv.org/html/2603.18411v1) §3–5/Tables1–6与必要A–E；只采用step偏好reward与gold-NLL逐token gate的训练/消费接口。logit/probability算子身份未统一、同词表迁移条件、OOD/粒度/entropy反退、TPS/QPS与估算成本、gold对但推导错误示例保留；不授无训练、任意跨模型迁移、全部能力保持或逻辑真值，未核代码/复现。

- `SF-2026-ARXIV-2604-00018` — Daily2026-04-03；[exact-v1](https://arxiv.org/html/2604.00018v1)§3/4.4–4.7，2+1+2=5，仅采用高entropy prefix分叉的同budget局部选择；保相关错误/原entropy接口资格/verification及全部费用，不授truth或通用可靠性，未核实现/复现。

- `SF-2026-ARXIV-2603-29957` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29957v1)S3–5必要，2+1+2=5，仅code-prefix中途thinking/strip后续代码消费接口。保5K合成/14K训练/8A10040G、格式过滤非正确、special70.0<text70.3、padding69.4→67.6及entropy选择混杂，Eq9不补完整数值recipe，全部制备/训练/rollout/test费；未核代码/复现。

- `SF-2026-ARXIV-2603-29301` — Daily2026-04-02补04-01；[exact-v1](https://arxiv.org/html/2603.29301v1)S3–6必要，2+1+2=5，仅prototype×warp/100arc-points/ICP/DBSCAN/medoid消费接口。保224templates/35shapes/2240 rejectionbalanced评价人口、known/inferred warp及too-restrictive95.6%/too-permissive80.6%边界、parabola shear混错/τ反退、19对1生成与67ms每pair累计费；不采严格距离不变/物理正确，未核代码/复现。

- `SF-2026-ARXIV-2604-17290` — Daily2026-04-22补Apr21；[exact-v1](https://arxiv.org/html/2604.17290v1)§2–3/Alg1–2/Eq1–4、§4.1–2、AppA/E/G。2+2+2=6，固定程序局部RV搜索的具体gap深入；有限支持/固定suffix不继承原LM law，同组变体非独立draw，GT verifier/Plot2Code textmatch与CPU全费边界近正文。root必要Source/逐字PRE与实际正文/完整局部邻接/本人注非作者POST通过，窄lease释放；本注仅同步已发生结果，不授实现/复现或DAY。

- `SF-2026-ARXIV-2604-20500` — Daily2026-04-24补Apr23自然日；[exact-v1](https://arxiv.org/html/2604.20500v1)§3–4/A/C.2/D.3必要层，2+2+2=6，prefix-mass枚举与truncated概率coverage差额深入。保fixed-k非全序列最优、十token merge非lossless、B1/2与大batch及tree/KV全费；未核代码/复现。必要Source与root实际owner/逐字PRE通过并授两段与本注窄lease，作者已写入并顺读完整邻接；root非writer实际正文/完整前后/本人注actualPOST通过，窄lease释放，本注仅行政同步，不授DAY。

- `SF-2025-ARXIV-2508-21787` — Godel，Daily2025-09-02补Sep01；[exact-v1](https://arxiv.org/html/2508.21787v1)必要§2–5/7/B及C有限层直接复用Newton51实际Source，2+1+2=5；本人实际owner对读/逐字稿，未冒重读全Source。仅chain+追加answer两评分consumer，保非jointMAP/正确性、长度与概率身份、pool上界疑点/反退及全费，不采用性能或完整recipe。未看全部附表/像素/核代码或复现；Newton53本逐字PRE通过，root已协调本指定一自然段/独立marker/本人注；已按稿实际保存，Newton58一次真实完整新增/完整直接两侧/本人注POST通过，本指定窄位生效释放；不预整日DAY。

- `SF-2025-ARXIV-2509-02510` — Noether，Daily2025-09-04补Sep3；[exact-v1](https://arxiv.org/html/2509.02510v1) §4–7/Alg1/Table1–3、A1/A3、C2/T5/C4/T9与E所印示例必要，2+1+2=5。仅conditional entropy预算/prefix截断接口，保严格正支持条件、greedy非全局最优、top100/实际温度/CPU同步不同实现角色、质量/人评反退与全费；不采NP-hard未审归约、准确runtime recipe或普遍SLO/真值，未核仓库/图像/复现。Ohm102实际必要Source/评分/具体gap/逐字PRE通过，root已协调本指定一自然段/独立marker/本人注；按原批准稿真实保存，Ohm105一次真实非writer完整新增/完整直接两侧/本人注POST通过，本指定窄位即时生效释放；不预整日DAY。

- `SF-2025-ARXIV-2509-03113` — Boyle，Daily2025-09-05补Sep4；root分担[exact-v1](https://arxiv.org/html/2509.03113v1)必要S3–S5/A/B/K–N/R/U与T1–5/14/18/19已实际非请求者核，2+1+2=5。只inputgradient sensor→noun条件mask→logit控制；保范数/链式项不闭、白盒权限、召回/终止人口及全费，不授精确对齐/无幻觉。未核其余附录全图/code/复现；root59实际消费81/82并通过本原逐字PRE和精确位，本一段/独立marker/本人注已真实保存并自读完整两侧，root62一次实际完整新增/完整两侧/本人注非writer POST通过，精确位即时生效释放；本注仅同步既成事实，不预DAY。

- `SF-2025-ARXIV-2509-06870` — Darwin继任Godel，Daily2025-09-10补Sep9；[AggLM exact-v1](https://arxiv.org/html/2509.06870v1) §3–7/Tables1–7必要域，2+2+2=6。仅generator候选集合的gold众数标签与consumer训练人口分责；保hard/easy曝光混杂、相对hard配比、16组/64组未配对/同题重复及候选prefill/训练/输出全费，不授gold线上可得、少数必胜或端到端节费。未核图像像素、代码/Math-Verify或复现；Bacon§10受限Source/正式评分/唯一Ch20窄gap、§12修窄逐字PRE已通过，root已新授本一段/独立marker/本人note窄位；已按原稿真实保存，Bacon§17一次真实非writer完整新增/完整两侧/本人注POST通过，本指定窄位即时生效释放；本注仅同步既成事实，不等root第三核，不预日级。

- `SF-2026-ARXIV-2605-28304` — Daily2026-05-29补May28自然日；精确v1必要方法、关键对照及直接限制见本日SUP_SOURCES A5。root已实际必要Source与具体owner比较通过并授本两段＋本人注窄位；作者实际保存，root已实际完整新增、完整直接两侧与本人注唯一非writer POST通过，窄位释放；不预DAY。仅采用正文限定命题，未核无关附件、实现或复现实验。
- `SF-2026-ARXIV-2605-28142` — Daily2026-05-29补May28；精确v1必要Source及实际owner差额见SUP_SOURCES A9，root已实际通过并授Power-SMC后/PreSTO前两段＋本人注。作者实际保存并顺读完整新增/直接两侧，root已实际完整新增/直接两侧/本人注唯一POST通过，窄位释放，不预DAY；只采marginal目标与local近似分账，未核无关附件、代码或复现。

- `SF-2025-ARXIV-2509-06174` — Darwin，Daily2025-09-10补Sep9；exact-v1 §3/Eq1–4/Alg1、§4/T2–4、Limitations/A1/T5必要域，2+1+2=5；Bacon266首必要/作者214一次采用。仅跨软长度prompt的答案一致与条件长度统计controller，保错误多数/非单调、伪码与统计人口未闭、T2/T4反侧和所有候选/串行/校准全费，不采最短正确/完整recipe/净效率，未核图像像素/代码或复现。

- `SF-2025-ARXIV-2509-06608` — Darwin，Daily2025-09-10补Sep9；exact-v1 §2–5、B–I全部必要文字/式及J两配对数值表，拟2+1+2=5。仅steering层位/起始token偏置、固定QK下Value常量写入与完整残差干预分责，保LN条件/前缀与decode对照、组合反退及全费，不授唯一推理算法/全域entropy因果/可组合或净效率；未核曲线像素、原训练实现/完整rollout或复现。

- `SF-2025-ARXIV-2509-09864` — Carson，Daily2025-09-16补Sep15BJT；Zeno229首必要exact-v1，126明确未读单让/本轮root接受后，root29一次不同角色必要采用通过，正式2+1+2=5/唯一Ch20；root实际正文/A1–5与四页PNG，Carson只151归并/当前owner拟稿、不第三Source。只有限策略菜单、成功率probe与每策略人口均值双成本软效用，保oracle/低预算反退、同步/全费和固定策略/可信验证退路；不采逐query精准成本、硬deadline/全局最优或普遍净省，未核实现/复现。152原三项与完整两侧经Zeno287纯PRE/root本轮fresh窄位通过；本人已按原稿真实保存，Zeno290唯一actual完整nonwriter POST通过，本日实际I35生效/窄位释放；仅同步既成事实，不第三Source/书段或授DAY。

- `SF-2026-ARXIV-2606-13862` — Daily2026-06-16补Jun15；[exact-v1](https://arxiv.org/html/2606.13862v1)§3–5/T1–2/A1–2必要，2+1+2=5，仅相邻pair状态/双离散监督/回退重预测分责。保lambda不同混杂、任务反退、正确人口steps非完整tokens及净成本、硬件/服务配置未披露；不采普遍speculation无效、scale因果或SLO。作者唯一首备，唯一reader§19必要/actualowner/逐字PRE通过并窄授，作者真实SAVE/完整两侧自读后，reader§20一次soleactualPOST已过、本指定窄位释放；此处仅行政同步既成状态，未核代码/复现，不预DAY。

- `SF-2025-ARXIV-2510-01902` — Hilbert，Daily2025-10-04补Oct03BJT；[CARS exact-v1](https://arxiv.org/html/2510.01902v1)§2–3/Alg1/Th1与proof、4.1/4.3/T2/B–D/E1–6/T3–7必要由Lagrange R297首次准备、作者一次另一角色采用，2+2+2=6。仅sound invalid-prefix排除质量/自适应proposal与接受后条件分布；保正支持/固定分布/准确质量、非减非严格提升、checker误删反侧、grammar非任务语义、SQL超时/局部反退、KL对象与完整序列/全费口径。不采通用高效、安全或代码精确实现，未核图像素/代码/复现；整体PRE/真实SAVE/selfread/唯一POST只据本日canonical实际层，不由本注预签。

- `SF-2025-ARXIV-2510-12121` — Herschel，Daily2025-10-16补Oct15；消费Cicero R19 exact-v1 §3.1–3.2/4.1–4.3/A首次必要，2+1+2=5，仅TD value/外部reward与test hidden目标距离控制差额深入。actual生成控制owner Ch20，不复写初始embedding；保目标冲突/编辑分布漂移、base未达标条件成功6.60–30.68%非全请求、SelfBLEU局限与全训练/梯度费，不授全局Pareto/通用精确控制。未第二Methods/代码/复现；PRE/SAVE/fullselfread/solePOST只本日canonical实际层。

- `SF-2026-ARXIV-2606-17537` — Daily06-18补Jun17，2+1+2=5，消费root§65首次必要§3–5/T1–2，仅CTC概率producer共享-v-CMLM/MBR效用consumer分责。保pseudo-reference非真值、原WER长度、迭代/样本反侧、architecture/loss不同及八Xeon核/RTX6000Ada局部测时排加载和未披precision/concurrency/SLO/全费。未核Rust实现或复现；sole整体PRE§75通过，作者已窄SAVE；实际POST待后到记录。

- SF-2025-ARXIV-2510-17555 — Socrates，Daily2025-10-22补Oct21；Tesla R17 exact-v1 3.2/3.3/4/5.1/5.2及5.3指定域必要与R49差额；script诊断→硬候选mask深入。保四family非语言真值、Symbols/LowRes例外、code-switch和Pass反退/全费，不采无损语言控制；未核实现/复现，整体PRE/真实SAVE/全自读/solePOST按同日实际层。

- `SF-2025-ARXIV-2510-21007`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R14受限Evidence通过。仅前置升级选择与轨迹内停止分责，保校准人口、漏放、三调用全费；未核实现/复现，PRE/SAVE/全自读/solePOST据本日实际层。

- `SF-2025-ARXIV-2510-21067`：Daily2025-10-28补Oct27；exact-v1必要层、2+1+2=5，R14通过。仅无规范投票答案时的长度代理与全部候选费用，非短即真或实测净延迟；未核实现/复现，完整PRE/SAVE/自读/solePOST按本日实际层。

- `SF-2025-ARXIV-2510-21150`：Daily2025-10-28补Oct27；R18必要/R25实际gap，2+1+2=5。仅字符串到语义选项的分布接口，保hash/独立性/T0条件和token全费；未核实现/复现，完整PRE/SAVE/自读/solePOST据本日实际层。
