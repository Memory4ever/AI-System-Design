# 第34章 DPO

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-DPO`
**Legacy Chapter:** Ch30
**Status:** Draft

**Roadmap Intent:** 直接偏好优化如何绕过显式奖励模型。

## 本章要回答的问题

RLHF 已经收集 chosen/rejected pairs，为什么一定要先训练 Reward Model，再通过 PPO/GRPO rollout 优化 policy？能否从 KL-constrained reward optimization 推导一个直接作用于 preference pairs 的分类 loss？DPO 移除了哪些系统状态，又保留了哪些假设？

本章的核心判断是：**DPO 将 KL-constrained RLHF 的最优策略与 Bradley-Terry preference model 结合，把 reward difference 改写为 policy 相对 reference policy 的 log-probability difference，从而直接用离线 preference pairs 更新模型。**它移除显式 Reward Model 和 on-policy rollout loop，但没有移除 preference data、reference constraint、distribution shift 或 objective bias。

本章使用 `x` 表示 prompt，`y_w`、`y_l` 表示 chosen 与 rejected response，`pi_theta` 表示待训练 policy，`pi_ref` 表示 frozen reference policy，`beta` 表示 DPO preference-logit scaling / KL trade-off 参数。

## 从 RLHF 的两阶段复杂度开始

经典 pipeline：

```text
preference pairs
-> train Reward Model
-> current policy rollouts
-> score rollouts
-> PPO/GRPO policy updates
```

它允许 policy 探索新 outputs，也需要多个模型、generation、reward evaluation 和版本同步。

若已有高质量离线 pairs，一个朴素替代是对 chosen 做 SFT：

```text
maximize log pi_theta(y_w | x)
```

但这丢弃了 rejected response 提供的信息。模型不知道 chosen 相对 rejected 好在哪里，也没有直接约束二者之间的 margin。

DPO 的目标是同时使用 pair 两侧，又避免显式训练 reward 和在线 RL loop。

## KL-constrained 最优策略

第 31 章的抽象目标：

```text
max_pi E_(y ~ pi(.|x))[r(x,y)]
       - beta * KL(pi(.|x) || pi_ref(.|x))
```

对固定 prompt `x`，该目标的最优 policy 具有形式：

```text
pi_star(y|x)
= (1 / Z(x))
  * pi_ref(y|x)
  * exp(r(x,y) / beta)
```

其中 `Z(x)` 是对所有 responses 归一化的 partition function。反解 reward：

```text
r(x,y)
= beta * log(pi_star(y|x) / pi_ref(y|x))
  + beta * log Z(x)
```

对同一 prompt 比较两个 responses 时，`log Z(x)` 会相消。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20834:start -->
上述闭式关系依赖 preference model、reference policy 与 support 条件。条件被破坏时，DPO 可能存在满足 pairwise
loss 却偏离原 KL-constrained RLHF 目标的解空间；两者不能再被称为同一 objective 的不同实现。系统因此要把
pair construction、reference、policy support 与 beta 共同冻结，并用 online/held-out outcome 检查等价前提。
作者理论和实验不证明所有数据都会失配；条件成立且离线可审计时 DPO 仍更简单，失配明显时应回退显式 reward、
在线 RL 或重新构造 preference data。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20834:end -->

## 从 Reward Difference 到 Policy Difference

Bradley-Terry preference probability：

```text
P(y_w > y_l | x)
= sigmoid(r(x,y_w) - r(x,y_l))
```

代入上面的 reward parameterization，得到 preference logit：

```text
u_theta
= beta * [
    log pi_theta(y_w|x) - log pi_ref(y_w|x)
    - log pi_theta(y_l|x) + log pi_ref(y_l|x)
  ]
```

DPO loss：

```text
L_DPO(theta)
= - E_(x,y_w,y_l)[log sigmoid(u_theta)]
```

模型被训练去提高 chosen 相对 reference 的 log-ratio，并降低 rejected 相对 reference 的 log-ratio。

## 一个 pair loss 小例子

假设 `beta=1`，sequence log-ratios 为：

```text
chosen:
log pi_theta(y_w|x) - log pi_ref(y_w|x) = -0.2

rejected:
log pi_theta(y_l|x) - log pi_ref(y_l|x) = -0.8
```

则：

```text
u = (-0.2) - (-0.8) = 0.6
sigmoid(u) ~= 0.646
loss ~= -log(0.646) ~= 0.437
```

若 chosen/rejected relative log-ratio 顺序反过来，`u<0`，loss 增大。DPO 优化的是相对 margin，不要求 chosen 的绝对 log probability 在每一步都上升。

## Sequence Log Probability 怎样得到

对 response `y=(y_1,...,y_T)`：

```text
log pi_theta(y|x)
= sum_(t=1)^T
  log pi_theta(y_t | x,y_<t)
```

实现需要：

```text
chosen_input  -> token logprobs -> masked sum
rejected_input-> token logprobs -> masked sum
reference     -> same two sequence logprobs
```

Prompt、padding 和跨样本 tokens 不应进入 response logprob。Chosen/rejected 必须使用同一 tokenizer、chat template 和 prompt prefix，否则 pair comparison 不再对应同一 `x`。

Pair 的任务身份也必须相同：让模型解题，与给定一道题及候选答案后判断它对不对，不是同一个条件任务。前者可构造 `(x, correct solution, incorrect solution)`，后者则是 `(x + candidate answer, correct verdict trace, incorrect verdict trace)`；chosen/rejected 的质量标签分别来自答案正确性与 verdict 是否符合该候选的正确性。改用 backward pairs 因而改变监督目标与 prefix，不是普通 solution pairs 的另一种命名。答案生成 accuracy、对错误候选输出 FAIL 的识别率、对正确候选误判 FAIL 的率应分别验收，不能由一种 pair 的 loss 或分数改善签发另一能力。<!-- source-family:SF-2026-ARXIV-2601-07199 -->

[Forward/Backward DPO 的必要原证](https://arxiv.org/html/2601.07199v1)只支持这个任务与标签分账，不证明生成和验证是正交技能或普遍互不迁移。受限数学对照中，评测模型使用的样本数不同，错误识别还条件于各自生成的错误答案，不能把它当同一固定错误池上的因果比较；CalibF1 的正类定义与表中数字不一致，不能由读者改正后当作已验证校准。采样正确/错误轨迹、构造候选、检查 verdict、训练及两个任务的回归都需计费，模型自评不是真值。普通解题 pairs 在只需生成能力、标签可靠时仍合理；验证标签或保留能力不过关时，应回退可靠 pairs、外部验证与原 checkpoint，不能靠更强自我确认取得答案发布权。<!-- source-family:SF-2026-ARXIV-2601-07199 -->

轨迹终局失败时，逐动作构造 pair 还需要明确反事实分工：PRM 只定位候选 failure state，在同一历史替换一个 expert action，再让当前 policy 执行后缀，以 outcome evaluator 验证是否翻转结果，最后冻结相同 prefix 下的原动作/替代动作作为 step-level preference。终局收益因此提供这次 intervention 的资格，不是让 PRM、expert 或一个成功后缀直接证明动作普遍因果必要。它支付分支执行、后缀方差、网络/工具与 evaluator 成本；gold-based judge 也会误判，[受限 Agent 对照](https://arxiv.org/html/2602.03412v1)的 PRM 定位或验证反侧与不同 pair 数量不能授予 noise-free 标签或匹配总预算因果保证。状态不可重放、验证不可靠或后缀收益不稳定时，保留可靠的普通 preference pairs，而不把整条成功轨迹静默拆成全部正确动作。<!-- source-family:SF-2026-ARXIV-2602-03412 -->

Vanilla DPO 使用 sequence log-probability sum。较长 response 包含更多 token terms，因此 length distribution 会影响 log-ratio。Length normalization 或其他 variant 会改变 objective，不能悄悄加入后仍称为原始公式。

同样地，把 response-level margin 重新分配到不同 tokens，也已经改变了 reward attribution 与局部 KL geometry，而不是实现细节。若 preference 的关键差异确实集中在少数 span，token weighting 可能比等权求和更有效；但权重 policy 必须是可版本化 artifact，并与原始 pair、reference checkpoint 和 reduction 方式一同保存。一种受限方案让冻结 reference 以 chosen/rejected 交换顺序执行两次 pairwise-judge prompt，从 verdict token 的 attention 中提取、归一化权重，并显式处理 attention sink。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21883:start -->
Pair label owner 仍决定相对偏好，weight extractor 只提出 token credit，objective owner 冻结 reduction，optimizer 才提交更新。Attention 不是因果解释，也不是 preference truth；这种启发式还增加两次 forward、layer/head 选择、顺序敏感性、sink correction 与 judge bias。若 swap invariance、weight stability、chosen/rejected likelihood、KL 或 held-out behavior 回归失败，应回退 vanilla sequence-sum DPO，或只使用经过验证的 token/process labels。现有证据限于作者的 instruction-following 数据和较小模型，不证明 attention 权重可跨模型迁移或更高 judge score 等同更安全的行为。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21883:end -->

另一种目标变化不调整 token 权重，而调整偏好反馈经过非线性函数的单位。令每段的 reference-relative log-ratio margin 为 `u_s`，普通 sequence DPO 先聚合为 `-log sigmoid(sum_s u_s)`；分段反馈则使用 `sum_s -log sigmoid(u_s)`，两者不等价。[一个受限分支](https://arxiv.org/html/2602.09533v1)区分 token 长度与 feedback segment 长度，通过 EOS padding 的固定段长或固定段数等分，把 prefix-wise Bradley–Terry 假设落实为局部目标；只有单段时才回到原 sequence loss。Pair、分段规则、padding 与 reference identity 因而都属于 objective artifact，而不只是 batch 实现。<!-- source-family:SF-2026-ARXIV-2602-09533 -->

分段增加反馈频率，却没有增加真实过程标签：把一对完整回答的偏好继承给各前缀，不证明每一步正确，异长度回答中序号相同的段也未必语义对齐。不同前缀上的 reward shift 不自动抵消，全序列 energy 的全局 Boltzmann 归一也不自动等于逐条件归一的乘积，因此不能由此保证原 reward 或原 KL 最优解不变。作者受测细度有反退，更细不是普遍更好；生成长度也可能大幅增加，粒度搜索、训练和输出成本需另计。缺乏可靠 prefix 偏好或无法承受这些代价时，保留普通 sequence pairs，或采用真正经过验证的过程标签，不把该局部目标当作免费 step credit。

等长切段之外，语义边界也能定义局部反馈单位：reasoning trace 与 final response 可能一段拒绝而另一段泄露，整条偏好会掩盖这种异向失败。一条受限分支用显式结束标记分开两段，分别取得 harmfulness proxy，再为两段独立的 DPO loss 分配权重；这既不同于全序列一个 sigmoid，也没有取得真实逐步骤信用。[必要接口与有限同数据对照](https://arxiv.org/html/2602.21346v1)支持这种分责，但原文的 binary mask/连续权重命名和 pair threshold 说明不一致，段间 score 差异还可能异号或分母为零，不能直接当作已完备、非负加权的实现契约。三类 judge、额外采样与训练均有成本，proxy 可误签安全且调参会退步；权重人口、数值 guard 或独立行为未验收时，保留普通 sequence DPO 或经验证的过程标签，而不从局部 attack-rate 下降推出普遍安全。<!-- source-family:SF-2026-ARXIV-2602-21346 -->

## Reference Policy 仍然存在

DPO 常让 `pi_ref` 是 SFT policy 的 frozen copy。它提供两个作用：

- 定义 policy 改变的相对坐标。
- 对应原 KL-constrained RLHF 中的 anchor。

训练时不一定需要把 reference model 永久作为独立在线服务，但需要获得 reference logprobs。可以预计算到 dataset，或训练时 forward；两者在存储、灵活性和一致性上不同。

若预计算 reference logprobs，任何 tokenizer、template 或 reference checkpoint 变化都会使缓存失效。Reference-free variants 属于不同假设，不是 vanilla DPO 的默认语义。

相对坐标也会留下一个容易被总 loss 掩盖的盲区。令 `Delta_theta = log pi_theta(y_chosen|x) - log pi_theta(y_rejected|x)`，`Delta_ref` 为同一对回答的 reference margin；普通 DPO 的 sigmoid 输入是 `beta * (Delta_theta - Delta_ref)`。当 `Delta_ref < Delta_theta < 0` 时，policy 比 reference 更偏向 chosen，相对 margin 已为正，sigmoid 的更新权重可能逐渐衰减，但 policy 自身仍给 rejected 更高的 sequence likelihood。因而 loss 下降不自动意味着 raw preference margin 已翻正。[一个受限分支](https://arxiv.org/html/2602.11902v1)把所有负的 `Delta_ref` 截为零，让 reference 不再以更负的起点提前满足该对目标；这是 objective 的改变，不是原 KL-constrained 最优解或生成正确性保持不变的证明。<!-- source-family:SF-2026-ARXIV-2602-11902 -->

这个修正仍信任 pair label：如果 reference 正确反对一个误标的 chosen，截断反而可能把 policy 更强地推向错误回答。验收要同时记录 raw chosen/rejected margin、各自 likelihood、相对 reference 的 KL 和 held-out behavior，而不能只看 relative loss 或 judge 总分；还要计入获取 reference logprobs 的必要 forward、缓存一致性及训练/搜索成本。作者同 SFT、同参数设置的有限对照支持这一失败条件值得单独检查，但主结果还混入 reference 与 margin 设置变化，不授通用胜出或全 pipeline 免费。标签质量、held-out 行为或 KL 回归失败时，保留原 DPO 与原 reference anchor，而不是把截断当作正确性门。

## Beta 怎样影响更新

`beta` 缩放 chosen/rejected relative log-ratio 进入 sigmoid 的幅度，并对应推导中的 KL trade-off。它会影响：

- 达到相同 preference confidence 所需的 policy/reference margin。
- Gradient scale 与 saturation。
- Policy 偏离 reference 的倾向。

不同代码库可能对 `beta`、temperature 或 loss sign 使用不同 convention。不能只比较配置数字，必须先对齐公式。

这里的 `beta` 与第 31、32 章 KL-constrained objective 中的 `beta` 来自同一
理想化推导：都描述 reward 改善与偏离 reference 之间的 trade-off。但工程中
不能把两者的配置值直接互换。PPO-style RLHF 可能使用按 rollout 统计自适应的
KL coefficient 和特定 KL estimator；vanilla DPO 则把 `beta` 作为离线 pair
logit 的固定缩放。Estimator、token/sequence reduction 和实现 convention
不同，相同数值不代表相同的实际 KL 或 policy displacement。

`beta` 也不是安全旋钮。更接近 reference 不等于更符合产品目标，偏离更多也不等于更强。

### Preference Scale 与 Optimization Scale 不应共用一个旋钮

Vanilla DPO 把 `beta` 同时放进 preference logit 和 loss gradient。这样做在目标固定、只需要一套简单 recipe 时很合理，
但它把两个本应分别回答的问题耦合起来：一是 preference pair 被假设有多大噪声，二是 optimizer 每一步应走多远。
因此在固定 learning rate 下，改变 `beta` 不只是改变 reference trade-off，也会改变 gradient magnitude 与 saturation；
两个 run 即使 loss curve 相近，也可能得到不同的 policy displacement。

一种实验性分支是先对 softplus preference loss 做中心化与尺度归一化，使 preference-noise scale 仍由 `beta`
表达，而 optimizer learning rate 独立拥有 update scale。该变换可以保持有限 `beta > 0` 下的最优解集合，
并让 `beta -> 0` 连续趋向线性 preference-margin objective；它解决的是参数语义与调参可解释性，不是 preference
data、reference identity 或 distribution shift。工程验收仍要分别记录 raw margin、gradient/update norm、实际 KL、
chosen/rejected likelihood 与独立行为评估，不能因为目标函数在数学上 argmin-equivalent 就假设有限步训练轨迹相同。

旧的单一 `beta` 在固定数据、固定 optimizer 且已有充分 sweep 的场景仍更简单；只有跨 scale 迁移、自动调度或需要解释
policy displacement 时，分离两种 scale 才值得增加新的配置与校准状态。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10981:start -->
即使 preference scale 与 update scale 已分开，SimPO 的 `beta` 仍会通过 sigmoid saturation 隐式过滤样本，而 `gamma` 的有效含义又随数据集 reward-gap 分布变化；因此二者的联合 sweep 很难跨数据复用。一个有界 ratio-margin 分支先把目标从“持续扩大 gap”改写为“接近最优 margin”，再以 chosen/rejected reward ratio 消去 `beta` 对 margin 定义的影响，并用单一、有界的 `xi` 表达期望相对分离。`xi` 可以由训练前 gap 分布的 quantile 提议，但这只是可审计的初始化状态，不是数据无关常数。

这条分支不是给 `beta`、`gamma` 之外再增加第三个旋钮，而是以 `xi` 取代二者对目标 margin 的耦合调节。它减少重复联合试参，却新增 ratio normalization、初始分布估计与可能的 `xi` schedule；分布漂移、后期 target likelihood collapse 或归一化不稳时，仍应回退经过验证的 DPO/SimPO，并同时观察 raw gap、chosen/rejected likelihood、KL 与行为结果。exact-v1 只支持作者四个数据集以及 Mistral-7B-Instruct、Llama3-8B-Instruct、Gemma2-9B-Instruct，不证明免调参或跨数据集普适。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10981:end -->

### 从对称 Pair Gradient 到 Probability-geometry Gate

Vanilla DPO 假设每个 retained pair 都应推动 chosen/rejected margin。数据经过充分审校、pair preference 与 reference
policy 的局部改进方向一致时，这一旧方案简单且可复现；但 pair 只表达相对偏好，并不保证它对当前 policy 的 chosen
与 rejected 概率同时产生期望方向。直接累积所有梯度，可能主要压低 rejected，甚至让 chosen likelihood 一起下降。

因此可以把 rejected response 的 probability geometry 作为 **update sensor**：当负梯度继续作用于已经处在极低概率
区域的 response、容易放大 valley collapse 时，显式 gate 衰减 rejected-gradient magnitude；其他区域仍保留标准
preference update。最后仍由 optimizer 在同一 checkpoint、batch 和 learning-rate contract 内提交更新。Gate 调制的
是 rejected 方向的梯度流，不拥有“偏好是否真实”的判决权，也不是对整条 pair 做 gradient-conflict admission。

```text
preference pair + reference identity
→ rejected-response probability geometry
→ gated rejected-gradient magnitude
→ bounded optimizer update
→ chosen likelihood, margin, KL and task evaluation
```

它用额外梯度统计、阈值校准与潜在 selection bias 换稳定性；错误 gate 可能丢掉困难但有效的 preference，batch-level
统计也可能掩盖 subgroup conflict。高质量、同分布数据或 gate 不能可靠校准时，原始 DPO 加独立 likelihood/KL 监控
仍是更清楚的基线。现有 exact-v1 实验支持若干架构与 preference datasets 上的条件现象，不证明对任意 optimizer、
数据噪声或长期行为都更优。

<!-- source-family:SF-GRADIENT-GATED-DPO -->

同一 batch 中的负 margin，也可以分别驱动两种保守提案：第一项在 warm-up 后，按交换 chosen/rejected 能降低的当前 loss 分配稀疏、总量受限的软标签混合；第二项只对混合损失的高分位尾部提出软 cap。前者改变监督方向，后者限制当前损失尾部，两套预算不能互相代替，难 pair 或负 margin 也不能被直接认证为错误标签。[wDPO 的受限方案](https://arxiv.org/html/2603.07211v1)明确停止 label weight 与 batch cap budget 的梯度，却未明确 quantile threshold 和逐样本 cap weight 的完整梯度路径，因此这里只采用分责接口，不抄成已证明的纯梯度缩放或参数梯度硬界。稀疏分配、quantile、warm-up/预算校准与独立安全/能力回归仍计费；受测 judge 的改善既不普遍，也不授发布安全。批次构成、标签方向或训练回归不可信时，保留审校后的 vanilla DPO、独立 likelihood/KL 与行为评价，不让优化中的自信代替偏好真值。<!-- source-family:SF-2026-ARXIV-2603-07211 -->

前述 rejected-response probability gate 调节已有偏好对的更新幅度，不改变标签；扩散生成中若同一对图像在不同偏好维度上冲突，还可选择另一条受限监督分支：保留经明确 proxy 共识筛出的 clean anchors，将其余 pair 视作未标注，再按去噪时间段用当前 DPO margin 符号提议局部标签、以分时阈值控制准入。这里增加的是标签的时间身份与自举过程，不是用梯度大小重新证明人类偏好；原 pair、proxy 版本、checkpoint、时间段与阈值都要进入训练 lineage，clean anchor 不能被伪标签静默替代。

margin 只是模型自身 confidence proxy，晚段信号可能更弱；用于阈值调整的 clean 样本不能同时冒充独立最终校准集。多维共识也可能抹掉真实偏好分歧，组间 variance 分解不证明训练必然收敛到次优或自举必然修复。[该分支](https://arxiv.org/html/2604.24952v1)需独立行为评价，并把 proxy 调用、筛选覆盖损失及迭代训练成本与对应质量分账；标注或阈值失准时，回退经审校的 vanilla DPO 或可信分时/process labels，不把有限视觉模型结果写成通用偏好恢复保证。
<!-- source-family:SF-2026-ARXIV-2604-24952 -->

如果目标是修正 synthetic preference 对同一目标人口的系统偏差，而不是按时间段重新提议标签，还可保留另一条统计分支：先计算全池的 pseudo-label loss，再在代表性的人工标注子集上计算 `true-label loss − pseudo-label loss` 的残差均值，并把它加回全池 criterion。对固定 policy 参数、同目标人口和代表性抽样，这个期望身份能抵消 pseudo criterion 的平均偏差；它不是说有限训练得到的 policy 无偏，更不是每个样本的伪标签已变正确。只挑容易审校、偏好鲜明或高置信样本的人为筛选，不自动满足同人口条件，需有可信采样/权重依据才可采用。

标注稀少会放大残差噪声，pseudo annotator 的独立性也要单独检查：独立 nuisance 数据或有相应假设的 cross-fitting 才能支撑所需统计条件，当前 policy 在同标注数据上自训练可能把 correction 拟合成零。[受限原始证据](https://arxiv.org/html/2602.06195v1)的 diffusion 实验并非处处胜出，原损失式与导数还有符号不一致，因而这里只保留估计器接口，不采用其具体 BCE 写法、收敛 rate 或网络权重距离保证。标注、synthetic 调用、残差和额外 forward 都需计入成本，发布仍靠独立行为评价；人口失配、方差过大或独立性无法核实时，回退代表性真实标签上的 DPO，或先保持既有 clean-anchor 分支，不用“debiased”名称签发质量/安全承诺。<!-- source-family:SF-2026-ARXIV-2602-06195 -->

前面的 DPO 推导依赖 policy/reference 的 log-probability ratio；若生成器是 consistency model，另一条分支用 PF-ODE 轨迹上相邻两点的一致性 residual 构造偏好 margin：冻结 diffusion model 推进到较早时间点，以固定 consistency reference 的较早端输出为 target，比较 trainable 与 reference 在较晚端各自到该 target 的距离，再对 chosen/rejected 两个 reference-centered residual 作 sigmoid loss。它拥有的是一个可训练 surrogate，不是已经证明等于 endpoint density ratio；fixed reference 也不是随更新的 EMA。[精确目标及受限反侧](https://arxiv.org/html/2602.13055v1)只支持该替代接口，不能继承普通 DPO 的精确概率/KL 保证，或把同时变化的 curricula、rank、分辨率和 sampler 收益都归于 residual。两点构造、solver/reference identity、额外前向、训练成本和独立质量回归都要验收；proxy 失准或 reference 不再适配时，回退经审校 pairs 的普通 Diffusion-DPO 或可信生成目标，不把一致性误差当人类偏好真值。<!-- source-family:SF-2026-ARXIV-2602-13055 -->

相对 margin 还可叠加 noise-output anchor：对 diffusion 的 chosen/rejected noisy samples，分别惩罚 trainable prediction 偏离固定 reference prediction，而不是直接拟合实际注入的 noise target。前者限制相对训练如何移动两侧输出，后者则是不同的 SFT 监督；都不是硬 KL 或全函数保持。纯 DPO 可通过同时恶化 winner/loser 的拟合而改善相对 margin，因此 anchor 身份与 noise/time、reference forward 需共同冻结。[SpatialAlign v1 §3–4](https://arxiv.org/html/2602.22745v1)用可检出实体的几何 proxy 筛 pair，有限实验同时出现 proxy 正确提升和 identity/视觉质量反退，SFT-anchor 也并非所有指标更差。该 proxy 所写归一化不确保总分≤1，不能作概率或物理真值；detector 漏检、valid 过滤人口损失、生成/追踪和双侧 reference 成本都要计入。Proxy/anchor 失配或质量回归时，回退可信 noise target、原 reference 与重新审校的 pairs，不把 anchor 的有限收益解释成避免所有 reward hacking。<!-- source-family:SF-2026-ARXIV-2602-22745 -->

## DPO 移除了什么系统复杂度

Fine-tuning loop 不再需要：

- 显式 Reward Model training/serving。
- Actor rollout generation。
- Critic/value model。
- Advantage/return estimation。
- On-policy old-logprob lifecycle。

训练更接近 supervised pairwise fine-tuning：读取固定 `(x,y_w,y_l)`，计算 policy/reference logprobs，反向更新 policy。

但计算通常仍比单条 SFT 更重，因为每个 pair 至少包含 chosen 与 rejected 两条 response，reference logprobs 也要计算或读取。

## DPO 保留了什么难题

第一，preference data quality。错误、表面化或单一人群偏好会直接进入 objective。

开放式任务没有可靠规则 verifier 时，pair judge 可以先读取一份独立参考答案，再比较当前 policy 的多个候选；这份 **reference answer** 提供内容与指令遵循的锚，工程上不应把它直接误用为逐字或风格复制的要求，也不是 DPO 的 **reference policy**。后者仍是冻结 SFT policy，负责定义 likelihood ratio 与 KL 坐标；更新候选来源、改变判分依据和移动 policy anchor 是三个不同选择。参考答案应绑定 teacher、生成协议与审校身份，因为 teacher 错误和风格偏好仍会进入 pairs；换用弱 reference 后收益缩小，参考锚的收益也随任务类型与模型后训练程度变化，有限分类实验中 creative 上的收益对 Qwen 较弱而对 Llama 仍明显。受限的 [RefEval 实验](https://arxiv.org/html/2602.16802v1)先用强 teacher 的60K答案做 SFT，再为每题生成5个当前-policy候选并比较10对，不是免费自改善；参考生成、judge调用、SFT/DPO及参数选择都要计费，最终 judge win rate 也不认证事实或安全。reference 不可靠、域外校准失败或总预算不合算时，保留独立审校的普通 pairs、人工/可执行 verifier，而不是让同一答案锚独占训练标签与发布真值。<!-- source-family:SF-2026-ARXIV-2602-16802 -->

这里的数据质量还包括 chosen 与 rejected 的相对来源分布：即使逐条回答表面中性，由不同 teacher 系统性生成的两侧仍可能携带隐性行为差异，成为对比训练的信号。因此清洗显式迎合措辞不能替代 teacher/pair provenance 与独立行为验收；交换来源或修复 pair 后也要复测基础能力和格式，不能假定去偏没有代价。

偏差校正还须区分“同一 pair 的标签有偏”与“标注两类 labels 的候选来自不同生成分布”。如果少量样本同时具有 AI 与可信目标 label，可以先在大量 AI labels 上计算 loss，再用这些同 pair 的 loss 差作残差校正；当两类样本的 response generator 不同，还须以 generator density ratio 校正人口错位。这条条件分支不只是过滤坏 pairs，也不把 DPO reference policy 当成样本生成器：前者定义 policy/reference 的优化坐标，后者决定校正权重。只有目标人口得到覆盖、ratio 与偏差估计可用时，paired residual 才有预期解释；缺失支持不能靠少量校准标签补出。<!-- source-family:SF-2026-ARXIV-2602-08259 -->

校准 label 的身份决定究竟向谁纠偏。人工标签与强模型代理不是同一目标，当前 policy 在线采样的对称残差分支，也不是直接复用上述离线目标；两者都新增配对标注、generator likelihood/ratio 估计与训练成本。[有限纠偏对照](https://arxiv.org/html/2602.08259v1#S5)包含模拟翻转与模型代理 label，部分 summary/dialog 条件仍不及未校正对照，online 与 offline 预算也不一致，因此不授普遍人类真值、发布安全或总训练降本。覆盖不足、权重不稳或校准者与独立评价共同偏差时，应回退审校后的普通 DPO pairs、可信人工/可执行 verifier 与独立行为回归；自动 label 较便宜的旧路径在偏差可接受、目标人口稳定时仍有价值。

第二，offline distribution。Dataset candidates 由旧 policy 产生，当前 policy 训练后可能进入 pairs 未覆盖的区域。

重新用当前 policy 生成 pairs，是刷新这个分布的一条分支，但不自动改善目标 coverage。[条件理论](https://arxiv.org/html/2601.08421v1)把每轮偏好优化的误差缩小建立在有限问题空间、可辨认的有界线性特征、精确 Bradley–Terry 偏好 oracle、可实现性、目标协方差非退化与局部 coverage 增长等假设上，并要求 batch 足以压低统计误差；有限样本仍留下误差 floor。同一语境中的 reference 保持固定，不能把“更新生成 policy”与“更新正则化 reference”混为一事，也不能由条件上界推出任意 LLM 的 on-policy 更新会增加覆盖。<!-- source-family:SF-2026-ARXIV-2601-08421 -->

一种混合采样设计把当前 policy 的联合 prompt–response 分布与 G-optimal 联合设计分布配对使用；后者不是任意旧 replay，求它还需要可用特征与候选空间，设计计算本身有成本。刷新样本又增加生成和标注预算，等 optimizer steps 不等于等总 tokens 或 oracle 调用；局部聊天实验也不在每个指标上单调改善。因此应分别验收覆盖、任务质量与 acquisition 成本。离线 pairs 覆盖充分、fresh 预算不足或设计假设无法验证时，保留固定 reference 的廉价离线训练，并用独立切片定位真正需要补采的区域。

第三，相对而非绝对质量。Chosen 只表示比 rejected 好，可能两者都差。

相对质量也不能把多个目标压成同一个胜负标签：按 helpfulness 排出的 chosen，可能反而不如 rejected 安全。一条受限分支重新收集当前模型暴露的攻击与 responses，按帮助性组成 pairs，同时独立保存两侧 safety score 的有符号差，在 policy/reference 的 preference margin 中加入额外目标项。这里，pair 的排序依据、辅助目标的方向与权重、训练 judge 和独立评价者各有自己的身份；“chosen”不能自动解释为各维度都更好，训练 judge 的高分也不是发布安全性。<!-- source-family:SF-2026-ARXIV-2603-07017 -->

[小模型的多目标对照](https://arxiv.org/html/2603.07017v1#S4)只支持这一条件接口，不支持免费自对齐或普遍安全恢复。原文 unsafe 阈值方向在正文与附录不一致，应先消歧，不能直接抄入筛选器；去掉目标中的权重分母又改变 sigmoid 的有效尺度，需与前面的 preference/optimization scale 分责一起检验，而不是当作保持原目标的稳定化。实验先用有害 QA 弱化拒答，不证明安全先验全部消失，部分正常问题帮助性和人工安全评估仍有反退；减少 preference 条数也没有计尽 reset、攻击生成、judge 与训练成本。目标冲突、score 漂移或回归失败时，保留独立审校的普通 pairs、明确安全约束与固定 reference，不让同一闭环同时定义标签和最终真值。<!-- source-family:SF-2026-ARXIV-2603-07017 -->

这种相对质量还要拆成**生成器能力差**与**同一 pair 内的质量差**。用更强模型生成 chosen、更弱模型生成 rejected，可以扩大两侧差距，却同时改变来源、风格和推理分布；仅凭最终答案对错也不能描述 pair 的全部信号。一条受限的数据选择分支先冻结 generator identity、共同 prompts 和 verifier，再用独立 judge 比较 factuality、step coherence 等维度，选择差距明确的 pairs，同时保留正确/错误方向、随机同预算子集和域外 outcome 对照。

这增加了 judge 调用和选择偏差，也可能把 judge 偏好的连贯风格误当成有效推理。[受控 reasoning 实验](https://arxiv.org/html/2604.08723v1)在同一组 3,500 prompts 上发现，四种正确/错误配对方向都能带来小幅数学收益，但正确对错误仍最好；不能据此取消正确性标注。较大 generator gap 与域外收益、step-coherence top-k 与数据效率的关系只在该 Nemotron-8B recipe 中成立，未证明单一维度的因果贡献或任何任务都优于随机样本。预算不足、judge 失配或迁移退步时，保留经 verifier 检查的 pair 与分层随机采样，而不是把“大差距”写成通用质量保证。<!-- source-family:SF-2026-ARXIV-2604-08723 -->

视觉生成中的 pair 质量还可以控制非目标差异，而不只是拉大总体好坏差距。一条受限分支把正确与损坏的目标文字放进同一次左右拼接生成，借共同背景、共享生成噪声与边缘条件约束两侧，再切开并用视觉语言模型过滤。这样提出的是“尽量保持周边一致、只比较目标文字”的近似局部配对；它与交换 teacher 来源或只按 judge 差距筛选不同，但同一次生成和像素层面的共同项不证明共享 U-Net、Attention 中的网络梯度精确相消。<!-- source-family:SF-2026-ARXIV-2602-06355 -->

控制条件也会改变训练人口：teacher 生成、文字损坏规则、边缘控制与 VLM 过滤共同决定留下哪些 pairs，并增加生成和审校成本。受限 OCR 对照支持在所测文字生成设置中继续比较这种 pair 与背景变化 pair、DPO 和 chosen-only SFT，不支持任意视觉偏好或精确梯度局部化；四次生成和 bootstrap 也不是四次独立训练。背景控制或负例失配时，应保留普通经审校 pairs，并独立检查目标文字与非目标画面是否一起退步。

第四，pair coverage。Single-turn preference 不自动覆盖多轮、tool use 或长期 task success。

第五，overoptimization。模型可能学会 length、style 或格式 shortcut，提高 pairwise likelihood 而不提高真实任务结果。

还可以不立即补采，而在离线偏好内部增加保守聚合。二元 Bradley–Terry 胜负概率的两个方向之和固定为一，若想同时下估两侧效用，仅调整普通二元估计器会碰到这一约束；一条分支引入 tie-event mass，在互不重叠的 pairs 子集上训练不同 adapters，再以完整 response 在各 policy 中的最小概率作保守聚合。其单一 comparator 保证依赖有限 prompt/action support、有界 reward 与 log-ratio、Bradley–Terry 人口、足够 ensemble 大小及有效 tie upper bound，不证明任意未知生成分布都免于 overoptimization。实际使用固定 penalty，也不能当作已经满足这些定理条件。<!-- source-family:SF-2026-ARXIV-2602-06239 -->

聚合粒度会改变交付分布：完整 sequence 的最小概率和逐 token 取最小后重新归一化，不是同一个目标；后者的局部 token 规则不继承上述 response-level 理论。[受限实验](https://arxiv.org/html/2602.06239v1)中，完整 response rejection 曾因 policies 分歧出现零接受，截断重试又改变可获得输出的条件；mean/std 变体也改变目标，不能称为 exact 替代。共享 base weights 只节省重复权重存储，不省掉全部 adapter 前向或 ensemble GPU-hours。因而保守程度、独立 holdout 质量、接受率与完整计算预算必须一起比较，自家 judge 的有限 win rate 不作通用质量保证；覆盖充分或聚合退步时保留普通 DPO，缺口明确且预算允许时再用 fresh coverage 分支。

DPO 更简单，不意味着不需要独立 Evaluation 或迭代数据闭环。

### Preference Pair 选择是实验设计，不只是数据量选择

随机收集 chosen/rejected pairs 在候选来源近似同分布、标注成本充足时容易复现；当生成预算与标注预算都受限时，增加 pair 数并不保证增加有效信息。数据 owner 需要同时决定生成哪些 responses、比较哪些 pairs，以及哪些比较能覆盖当前 policy 与目标行为之间的缺口；训练器只消费已经冻结并带 provenance 的 pairs，不能用 loss 反向改写采样事实。

多模态 pair 还要声明交换的是输出还是条件。固定视频与问题、比较两个答案，仍属于同一输入下的 response preference；固定问题和答案、比较两个视频，则是在不同输入条件下比较各自 policy/reference 的 log-likelihood ratio。后者直接训练条件敏感性，却不能沿用“同一 prompt 的两个答案”解释：原视频对、生成器/编辑版本、目标语义与 reference identity 必须共同冻结，并独立检查编辑是否真的改变目标动作或顺序、而保持其他任务条件。两项 loss 的系数同为 1 也不保证梯度幅度平衡。

这条分支增加反事实生成与有效性审计成本；同一 anchor frame 只是 scene 保持的构造目标，不是纯因果干预证书。[受限 CounterVid 对照](https://arxiv.org/html/2601.04778v1)中，244 个 held-out 人审样本只有约68%同时满足标签与画质要求，且部分外部指标不及 text-only preference；冻结 vision encoder 的训练结果不能证明内部已学到唯一视觉因果。应分别验收 answer discrimination、input sensitivity 和普通视频理解，把生成预算、过滤损失及双条件前向计入代价；编辑/标签失准时丢弃受影响 pairs，保留经审校的固定输入 DPO、真实原样本和独立 grounding 测试。<!-- source-family:SF-2026-ARXIV-2601-04778 -->

更有信息量的 pair acquisition 可以减少冗余标注，却会引入 selection bias、设计分布与部署分布错位，以及对离线估计假设的依赖。覆盖不足或设计假设无法验证时，应回到随机或分层抽样并扩大独立评测，而不是把理论效率当作质量保证。现有证据来自理论与离线 randomized-design 条件，只支持把 pair acquisition 纳入实验合同，不证明某一选择策略在真实标注流程中普遍最优。
<!-- source-family:SF-2026-ARXIV-2606-19607 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22211:start -->
只用 length reward 或硬 token budget 约束最终长度，会把必要推理和冗余内容一同压缩。一个条件分支先由当前 policy 产生 rollout，只保留被 verifier 判为正确的样本，再局部删除重复、无关、不可读或答案后的探索内容，以 augmented-original pair 的辅助 reference-free DPO 学习内容级差异。正确性 gate、删除规则、policy revision 与 pair distance 必须共同冻结；augmentation 只拥有编辑 proposal，训练数据 owner 才能接受 pair。

该路线需要额外 augmentation model、正确性验证和删除审计；过度编辑会移除必要推理，reference-free objective 也可能学习 style shortcut。exact-v1 只支持作者任务、模型和设置，不证明离线编辑在远离当前 policy 后仍有效。编辑后答案或过程验证失败、pair distance 过大或 held-out accuracy 下降时，应丢弃 pair，回退原 rollout、保守 length control 或只训练经程序/人工验证的局部编辑。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22211:end -->

### 从独立 Pair 到 Preference DAG：只在全局顺序可信时升级

独立 chosen/rejected pairs 在偏好关系局部、每条标签都能单独解释时仍是最清楚的训练事实；但同一 prompt 若存在多个等价答案和可传递的质量层级，重复 pair loss 会惩罚等价样本，也无法保存全局顺序。此时可以先按冻结的 preference signal 聚合 equivalence classes，再以 DAG 保存严格 dominance，只在跨类边上计算 local Plackett-Luce/DPO-style loss。Data owner 负责 graph construction 与 provenance，objective owner 只消费冻结图；graph revision 必须和 dataset、reference policy 一起进入 run identity。

图结构减少重复和相互矛盾的局部比较，却会增加 graph inference、anchor bias，并可能把一次错误的传递性判断系统性放大。偏好非传递、不同主体发生冲突或图证据不足时，应保留未排序集合，回退经过审校的 pairwise DPO，而不是让算法补造不存在的全序。

[受限证据](https://arxiv.org/html/2605.08037v1)来自作者构造的 preference graph、三个 benchmark 与三个 seed；它支持这条条件分支，不证明开放偏好天然满足 DAG，也不把 reward/preference signal 升级为事实真值。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08037 -->

## Chosen Probability 也可能下降

DPO 只要求 chosen 相对 rejected 的 policy/reference margin 增大。某些更新可能主要通过大幅降低 rejected probability 实现，chosen absolute likelihood 也可能下降。

因此监控应同时包含：

- Chosen/rejected policy logprob。
- Chosen/rejected reference logprob。
- Preference margin 与 accuracy。
- Response length 和 format。
- Independent task/human Evaluation。

只看 DPO loss 会掩盖模型通过哪一侧改变 margin。

## 与 SFT、PPO、GRPO 的统一比较

| 方法 | 训练数据 | 显式 Reward Model | 在线 Rollout | Learned Critic | 核心信号 |
| --- | --- | --- | --- | --- | --- |
| SFT | `(x,y)` demonstration | 否 | 否 | 否 | Target token likelihood |
| PPO-RLHF | Prompts + reward | 常见 | 是 | 是 | Value-based advantage |
| GRPO | Prompts + group rewards | 可选 | 是 | 否 | Group-relative advantage |
| DPO | `(x,y_w,y_l)` pairs | 否 | 否 | 否 | Relative policy/reference margin |

这张表描述训练 loop，不代表方法质量排序。选择取决于能否可靠生成 reward、是否需要在线探索、可用 preference data 和系统预算。

## 工程数据流

一组response共同进入preference objective时，直接保留整个group的前向图最清楚，却会同时驻留多条长序列activation；把所有正负pair展开再逐pair反传虽省驻留图，又会重复计算同一response。对只通过每条response的score `u_i(θ)` 耦合的可微group loss，可以先在同一参数点无梯度计算全部scores，得到 `c_i=∂L_group/∂u_i`，再固定系数，以 `Σ_i c_i u_i(θ)` 逐sample累积梯度。chain rule使其在该参数点保持一阶梯度，不保持原loss值或Hessian；response、reference、token reduction与参数点必须一致，全部梯度累积完才提交更新。forward随机性或score版本不同也会破坏这份等价，这是将公式落实成执行协议的额外条件，不是论文已验证所有runtime的保证。

[受限GroupDPO实现](https://arxiv.org/html/2604.15602v1)用额外no-grad pass和小系数状态换较低activation驻留，group-level pair interactions仍可为二次规模，并非总计算与group大小无关。其单H10080GB、gradient-checkpointing测量的memory overhead排除了初始化后的参数/optimizer base及optimizer.step临时峰值，不能写成GPU总峰值恒定；step latency反而包含optimizer，额外pass也不能省略。取样/偏好truth仍由数据owner负责，正例NLL是另一项objective选择；系数陈旧、数值不一致、二阶optimizer或额外前向成本不合适时，保留直接group graph、较小group或匹配的pair基线，并共同验收chosen likelihood、KL和任务slices。<!-- source-family:SF-2026-ARXIV-2604-15602 -->

### DPO 的分布式身份不止是梯度归约

单机集中式 pair dataset 下，把 DPO 看成普通 mini-batch 优化是合理的；进入 federated/decentralized topology 后，client preference distribution、reference/policy revision、local drift、communication round 与 graph connectivity 会共同决定 objective/run identity。协议 owner 必须保存这些状态，并约束何时聚合、何时拒绝 stale update；通信层不能把它们压成无来源的平均梯度。

去中心化减少集中数据搬运，却引入 non-IID 偏好、拓扑断连、版本漂移与更难复算的 campaign。连接或版本契约失效时，应暂停聚合并回退到可追溯的集中式 pair snapshot。`arXiv:2605.20696v1` 的 §3 与 §7、Appendix E/F 只支持其图拓扑和实验设置；§8 不证明任意 federated DPO 都能获得集中式质量或隐私保证。

<!-- source-family:SF-2026-ARXIV-2605-20696 -->

### Online Discovery 与 Offline Preference Update 可以分权

纯 online GRPO 让 rollout 与 update 紧耦合，在奖励稀疏、探索昂贵时成本很高；纯 offline DPO 成本稳定，却只能消费已有覆盖。一条条件分支让 online 阶段只发现 informative state/rollout，并冻结 provenance-complete preference dataset，再由 offline DPO 拥有后续 update。Handoff 必须绑定生成 policy、reward/evaluator、采样条件、pair 构造与冻结时间。

它以较少在线更新换取 selection bias、dataset staleness 与二阶段 objective mismatch；覆盖退化时应恢复在线采样或人工数据修复，不能继续消费陈旧 pairs。`arXiv:2605.21266v1` 的 iterative/hybrid Method 与 §4 实验只支持作者流程；§6、Appendix B 不证明该拆分普遍优于端到端 online RL。

<!-- source-family:SF-2026-ARXIV-2605-21266 -->

### Sequential DPO 必须保留目标关系与训练顺序

连续对多个 preference setting 做 DPO 时，只报告一个 aggregate forgetting 数字会把不同机制混在一起：后续目标可能与前一目标一致、正交或冲突，训练顺序和信号强度也会改变哪些 pairs 受益、哪些受损。Campaign identity 因此必须保存 objective relation、stage order、每阶段 reference revision 与 pair provenance；评测则使用固定 reference slice，分别报告 helped/harmed redistribution，而不是让后一次 evaluator 静默改写前一次结论。

这种分账能解释遗忘来自目标冲突还是顺序效应，却增加评测矩阵和长期 campaign state。目标相近、一次性训练或预算不足时，合并数据后做单阶段 DPO 仍更简单；但只要宣称 continual preference improvement，就不能省略顺序与固定参照。现有证据限一个 8B LoRA 模型和四类 preference regime，不构成普遍遗忘定律。
<!-- source-family:SF-2026-ARXIV-2606-19744 -->

在逐 stage reference 上，还可给每个 pair 的 `−log p` 乘 focal 因子 `(1−p)^γ`，再与当前任务 CE 合成目标：容易 pair 降权、难 pair 相对保留，但 pair confidence 不拥有真实群体比例，合成 hallucination 的 rejected 也不是实测遗忘人口。[φ-DPO v1 Eq14/17 与有限对照](https://arxiv.org/html/2602.22601v1)支持这一可定义的目标分支，不支持自动公平或全部旧知识保留。原 Eq15 的导数符号以及组内期望因子化不能直接继承，γ 趋无穷令更新消失也不是有用的均衡学习；有限 γ 过大确有反退。Gold/负例生成、人工审校和训练均有费用，β 的稳定性改善也可伴随目标质量降低。难度与群体失配、更新过弱或旧任务回归时，保留 vanilla DPO、reference replay 或显式代表性组采样，不让 focal 名称代替人口与行为验收。<!-- source-family:SF-2026-ARXIV-2602-22601 -->

```text
pair dataset
-> tokenize shared prompt + chosen/rejected
-> policy forward for both responses
-> reference logprobs (online or cached)
-> masked sequence log-ratios
-> DPO pair loss
-> policy backward/update
-> pair metrics + independent Evaluation
```

Packing pair data 时必须保留 pair identity。若 chosen 与 rejected 被不同 shuffle、截断或模板处理，loss 仍可能是有限数值，却已不再训练目标 pair。

## 本章在知识树中的位置

```text
SFT reference policy
+ offline preference pairs
-> policy/reference sequence log-ratios
-> DPO loss
-> preference-tuned checkpoint
```

本章收束第 31～34 章：RLHF 定义 preference pipeline，PPO/GRPO 是在线 policy optimization，DPO 是离线 pairwise 路线。下一章转向所有训练阶段共同依赖的 Checkpoint 状态。

## 从机制演进到系统设计

DPO 把 online rollout 与 critic 移出主路径后，训练状态集中到 preference pair、reference policy、beta 与 campaign history。重复 campaign 说明“保留旧能力”与“积累下一轮如何训练的知识”不是一件事，strategy/evaluator memory 需要独立版本；preference noise 与 update scale 也必须拆开诊断。

更薄的运行时换来对数据覆盖、reference identity 和 beta 的更高敏感度。chosen probability 下降、噪声主导或 campaign 间目标冲突时，应回到 SFT、人工数据修复或 online PPO/GRPO；DPO 是偏好优化的条件分支，不是 RLHF 的无条件替代。

## 自检问题

1. 对 chosen 做 SFT 为什么会丢失 rejected 信息？
2. KL-constrained optimal policy 怎样连接 reward 与 reference policy？
3. `Z(x)` 为什么在同 prompt 的 reward difference 中相消？
4. DPO loss 中四个 log-probability terms 分别是什么？
5. 小例子的 preference probability 怎样得到？
6. Sequence logprob 为什么必须正确 mask prompt 和 padding？
7. `pi_ref` 在 DPO 中扮演什么角色？
8. DPO 移除了 PPO pipeline 的哪些状态？
9. Chosen absolute likelihood 为什么仍可能下降？
10. DPO 更简单为什么不代表 preference correctness 已解决？

## 小结

DPO 把 reward difference 参数化为 policy 相对 reference 的 sequence log-ratio difference，从而直接在离线 chosen/rejected pairs 上训练。它保留相对偏好的信息，同时删除显式 Reward Model、critic 和 on-policy rollout loop。

简化的代价是更依赖固定 pair distribution。Preference coverage、reference identity、sequence masking、length effect 和独立 Evaluation 仍决定最终行为是否真正改善。

### Preference Negative 可以在线生成，但必须保留时间扰动身份

固定人工 preference pairs 易复现，却难覆盖视频—音频不同步的连续错误。SyncDPO 用规则化时间扰动为当前正样本生成
负例，并用 curriculum 逐步增加错位难度；扰动器拥有 negative proposal，独立同步指标与人工/感知 evaluator 才拥有
偏好判断。它降低标注成本，却可能让模型只识别规则伪影，且时间 metric 与主观质量并不等价。扰动分布偏离部署错误或
evaluator 不稳定时，应回退真实错位数据、固定 DPO 或分任务训练。现有证据受规则负例、数据、模型和时序指标限制。

<!-- source-family:SF-2026-ARXIV-2605-12179 -->

### Reference-free Convex 分支以表达能力换取优化保证

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23244:start -->
标准 reference-based DPO 用固定 reference 约束 policy drift，适合需要保持原模型行为的场景；reference-free convex 分支通过重写 policy class 获得更清晰的优化结构。凸性只属于重写后的表示和假设，不能反推原始深网 objective 已变成全局可解。

更强优化保证降低搜索不确定性，却可能限制策略表达能力或改变与基础模型的兼容边界。exact-v1 只支持作者公式、模型与实验；质量、容量或安全回归时，应回退标准 reference-based DPO、SFT 或更受控的 online 路线。arXiv:2605.23244v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23244:end -->

### 多轮 DPO 的 Reference 需要保留 Policy Lineage

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23398:start -->
每轮只使用一个固定 reference，在单次 campaign 中最容易解释；重复 campaign 后，历史 policy 可能分别保留不同能力，trajectory-aware 分支可以保存 lineage 并学习融合权重。融合器只提出 reference candidate，held-out preference 与通用能力回归才决定是否提交。

保留轨迹减少遗忘，却增加 checkpoint 存储、权重不稳定和 preference noise 累积。作者实验不证明迭代次数越多越好；融合权重坍缩、目标冲突或 held-out 回归时，应回退固定 reference、停止 campaign 或重新修复偏好数据。arXiv:2605.23398v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23398:end -->

reference lineage 与历史 response lineage 也不是同一个对象。一个 self-play 分支保留初始 policy 生成的 proto responses，并在每轮同时训练“gold response 胜过当前 response”与“当前 response 胜过初始 proto response”两项偏好。[T-SPIN 的 triplet 分支](https://arxiv.org/html/2601.08198v1)以 policy log-probability 构造这两个 signed gaps，不在 reward 中计算在线 reference ratio；仍须保留 proto 数据及其 source checkpoint。后一项会对当前 response 给出不同于前一项的梯度方向，二者由系数共同决定；它不是融合历史 reference，也不证明梯度永不消失。解析 opponent 解只属于指定函数类与优化条件，不授实际 LLM 的全局收敛。<!-- source-family:SF-2026-ARXIV-2601-08198 -->

reference-free objective 免去 reward 中的反复 reference forward，缓存初始 proto 则为历史比较增加存储；每轮仍要生成当前 negatives，整条 acquisition 成本没有消失。固定 gold 分布又可能与新任务漂移错位；作者五轮、50k标注的配方与200k SFT不是总生成/训练 tokens匹配，局部任务也存在退步。因此应独立检查当前质量、历史比较标签、proto版本与完整预算；偏好关系失真、漂移或更新无净收益时，停止 self-play 并补新标注，保留固定-reference DPO 或 SFT，而不是仅靠历史第二项维持迭代。

### Preference Pair 需要先验证事实关系

若 rejected response 在事实层面正确、只因风格被偏好系统压低，DPO 会把错误信号写进 policy。训练前应验证 pair 的 factual relation，并在证据支持时反转、降权或丢弃；格式、长度与内容偏好必须分账。<!-- source-family:SF-2026-ARXIV-2609-16532 -->

pair validation 增加 judge 和标注成本，judge noise 也可能制造新偏差。两个 benchmark、8B 以内模型与 LLM judge 不证明普遍收益；证据不闭合时回退 verified preference pairs、CPT/SFT 或保留不更新。

## Review notes

- `SF-2026-ARXIV-2603-07211` — Daily `2026-03-11` 补遗漏；[wDPO exact-v1](https://arxiv.org/html/2603.07211v1) §3.2–3.4、§4、Alg1/B及必要反侧。2+1+2=5，label mixture/loss-tail cap 分责具体gap深入；难pair≠错label、τ/λ完整梯度路径未明、训练budget非matched与安全回归/vanilla回退近文，不授硬梯度或真实偏好保证。review_mar11_continue actual necessary Source、Ch34逐字PRE和root窄锁通过；supplement_20260311 窄写一段，review_mar11_continue 非写入者实际新253段、225–261完整邻接/自身491注回对必要v1，并定点复核 rejected-response probability gate 的邻接回指修复，POST通过，不授DAY；未核artifact或复现。

- `SF-2026-ARXIV-2603-07017` — Daily `2026-03-11`补查；[exact-v1](https://arxiv.org/html/2603.07017v1) §4.1–4.5/Alg2、§5–6/8与必要A.3–A.5/A.8。2+2+2=6，安全目标方向和多目标pair接口定点深入；helpfulness排序与signed safety margin分责，不采§4.3/A.4相反阈值方向或删除w0后仍保持原目标的保证。Safety-reset不是移除全部先验；英文1–2B/有限人口、正常任务与人工评价反侧、6–11倍偏好条数非总费用均近文。review_mar11_continue必要原证独核通过，root已实际必要方法/目标/反侧、具体owner与Ch33/35交接PRE后窄写；非写入者 supplement_20260311 已实际回对必要原证并顺读新正文、完整局部邻接及自身末注，POST通过，不授日级完成，未核artifact或复现。

- `SF-2026-ARXIV-2602-08259` — Daily `2026-02-11`增量；[exact-v1](https://arxiv.org/html/2602.08259v1) §3–5。2+2+2=6，same-pair residual 与 generator density ratio 的纠偏目标差额深入；只采用覆盖/可用估计下的条件分支，DDPO离线与DIPO在线分开，reference≠generator，不授普遍human truth或效率。BT/realizability/overlap/nuisance条件、40%翻转/20%恢复、proxy human与judge共用、summary/dialog局部负反侧及总费用未披露近正文。root 实读必要Source及 actual Ch34/Ch33/35 PRE通过并授两段/自身末注窄锁；作者实际正文/完整邻接顺读，root 非作者实际新正文/完整局部邻接及自身末注 POST 通过，窄锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2601-07199` — Daily `2026-01-14` 增量；[Forward versus Backward exact-v1](https://arxiv.org/html/2601.07199v1) §3–7，2+1+2=5，solution/verdict pair条件任务及accuracy/error-identification/false-rejection三轴差额深入。Eq5/Table1 CalibF1冲突、评测350/250人口不同及各自错误池隔离，不采用普遍过度自信、严格nontransfer或技能正交；rejection sampling/候选标注/训练与双任务评价费用近文。Llama3.1-8B-Instruct、r16 attention LoRA/BF16、2000训练题，hardware未披露；未核artifact/复现。peer必要原证/actual owner完整邻接PRE通过，root授窄锁；作者实际正文/完整局部邻接及本注已顺读，root非写者已实际顺读正文、完整局部邻接及本注，actual POST通过，窄锁释放，不授DAY。

- `SF-2026-ARXIV-2602-21346`：exact-v1 §3、Table12及数据说明；只采用语义两段独立loss/proxy分责。保mask/weight、筛pair说明及未给guard冲突、调参/攻击退步；未核代码或复现，不授安全保证。 非原 packet 作者必要原证/actual owner PRE 与窄写完成；root 已实际顺读正文、完整邻接与自身末注，POST 通过。

- `SF-2026-ARXIV-2602-06355` — Daily 2026-02-10；[Di3PO exact-v1](https://arxiv.org/html/2602.06355v1) §3.1–3.2/Eqs4–5、§4、§5.1–5.2/Table2。2+1+2=5，pair nuisance-control 差额定点深入；不采用 Eq4 符号歧义下的精确梯度取消。300受控pairs、SDXL/SD3文字OCR、8TPUv4/900steps、2000held-out/4生成/1000bootstrap，只支持局部作者结果；precision/resolution/SLO未披露，无实验复现。root必要源与owner写前通过，root非作者实际正文/邻接与末注POST通过。

- `SF-2026-ARXIV-2602-06195` — Daily `2026-02-10`；[exact-v1](https://arxiv.org/html/2602.06195v1) §4/Prop1–2/独立nuisance条件、§5.1、§6及supp必要假设/反侧。5=2+1+2，具体 owner gap 定点深入；root 必要原源/owner 写前通过。只采用 fixed-policy/same-population/representative sampling 的 true-minus-pseudo loss correction 接口，不授训练policy无偏；Eq5/18 BCE符号与Eq21导数不一致，不静默修式，不采用收敛rate/网络权重距离子命题。SD1.5/XL局部退步和额外调用/残差成本保留，15 test runs不称15训练seeds；未核代码/复现，root 已实际顺读 L241/243 正文、clean-anchor 至系统边界邻接与本末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08198` — Daily 2026-01-15；[T-SPIN exact-v1](https://arxiv.org/html/2601.08198v1) §3/Eqs4–8/Prop1、§4/Table1–2、Conclusion/Limitations与B.1。2+2+2=6，current/historical response两项与online-reference区分gap深入；不授永不vanish或实际LLM全局解。proto cache lineage、fresh生成/固定gold drift、部分退步与不等token预算保留；8H10080GB/global64/max2048，precision Not Disclosed；未复现。root必要源/owner写前通过，root已实际核正文、前后交接及末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08421` — Daily 2026-01-15；[exact-v1](https://arxiv.org/html/2601.08421v1) Assumptions 2–4/Proposition3.1/Theorem3.2/Algorithm2与§6/Table1。2+2+3=7，条件 coverage 上界与联合设计采样差额深入；不采用印刷/定义有争议的 lower-bound 命题，不授任意 neural policy 收敛或无条件 coverage 增长。oracle/feature/realizability/batch、误差floor、fresh预算与非单调反侧保留；未复现。root必要源与owner写前通过，已实际核L254–279正文/邻接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-04778` — Daily `2026-01-10`；[CounterVid exact-v1](https://arxiv.org/html/2601.04778v1) §3.2–3.4 Eq3–8、§4.1–4.3/Tables1–4、Limitations/Ethics。原2+1+2=5，具体input-vs-output pair接口缺口深入；只采用fixed-input output preference与fixed-answer input preference的不同合同，不授sameanchor纯因果或λ1梯度平衡。244人审/68%good、Qwen2.5-VL3B/7B及冻结visionencoder、短动作/生成3000GPUh与外部反侧保留；未复现，root必要源→owner写前通过，root实际正文/邻接与末注POST通过。

- `SF-2026-ARXIV-2604-08723`，Experimental：[exact-v1](https://arxiv.org/html/2604.08723v1) §2–5、Appendix D。Nemotron-8B，OpenR1 数学 pairs；generator experiment 固定 s1-3B rejected，correctness experiment 同 3,500 prompts，16.5k 全集与 top-k 样本数不同。GPT-OSS-120B medium reasoning/temperature0.6/五次评分，DPO LR5e-8/beta0.2；AMC/AIME avg@16 与其余 pass@1 分开。generator 与 judge 信号相关不排除全部来源/风格混杂，未采用普遍 data-efficiency 或 training-speed 保证；hardware/precision/deployment SLO 未在采用证据披露。root 已独立核必要原文与实际正文，采用通过；本地实验未复现。

- 2026-09-01 偏好来源的隐性信号：<https://arxiv.org/html/2608.31079v1> §3.2–3.4/5.1–5.3、Discussion 与评测附录。所测 teacher 反转、chosen-only SFT 和多 objective 支持受限行为迁移；behavior-rate log-ratio 是经验关系，不是由 DPO 公式推出的普遍因果定理。评测以全答对题目交集上的压力 prompt 为条件，不代表总体事实能力；反转也可能损害能力/格式。

本章从 KL-constrained optimal policy 推导 DPO objective，补齐 sequence logprob、数值 pair、beta/reference 与 chosen-likelihood 边界。DPO variants 不在 Draft 阶段展开为目录；任何改变 normalization、reference 或 preference model 的方法都应单独标注假设。

Primary-source 校验入口：

- Rafael Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model", 2023: https://arxiv.org/abs/2305.18290
- Disentangling Optimization Scale from Preference Scale in DPO（centered-softplus reformulation；Status: Experimental）:
  https://arxiv.org/abs/2608.27032v1
  - 证据边界：论文支持有限 `beta > 0` 下的 argmin equivalence、`beta -> 0` 连续端点及作者模型/数据上的
    optimization/KL 现象；不证明有限步 trajectory、所有 optimizer 或所有 preference distribution 下都更优。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-GRADIENT-GATED-DPO:start -->
- `SF-GRADIENT-GATED-DPO` — Daily `2026-05-05`；primary `arXiv:2605.02626v1`；Books review `books-review:SF-GRADIENT-GATED-DPO`。

  **已吸收的语义增量：** DPO 对 chosen/rejected 使用对称 sequence-level coefficient，但极低概率 rejected region 可能发生 destructive squeezing；probability-geometry gate 只调制 rejected-gradient magnitude，preference truth 与最终 optimizer commit 仍由独立数据和训练合同拥有。
<!-- daily-books-trace:SF-GRADIENT-GATED-DPO:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21089:start -->
- `SF-2026-ARXIV-2606-21089` — Daily `2026-06-18`；primary `arXiv:2606.21089v1`；Books review `books-review:SF-2026-ARXIV-2606-21089`。

  **已吸收的语义增量：** 重复 DPO campaign 的 checkpoint 链需要另存 strategy/evaluator memory；保留旧能力不等于积累了如何训练下一 campaign 的科学知识。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21089:end -->

<!-- daily-books-trace:SF-2026-DPO-SCALE-SEPARATION:start -->
- `SF-2026-DPO-SCALE-SEPARATION` — Daily `2026-08-28`；primary `arXiv:2608.27032v1`；Books review `books-review:SF-2026-DPO-SCALE-SEPARATION`。

  **已吸收的语义增量：** 拆开 preference-noise 与 update scale。
<!-- daily-books-trace:SF-2026-DPO-SCALE-SEPARATION:end -->

- `SF-2026-ARXIV-2604-15602` — Daily `2026-04-20`；primary [GroupDPO v1](https://arxiv.org/html/2604.15602v1)；7分必要深入。新增coupled-score系数计算与逐sample backward分离，同参数点/stopgradient保一阶不保loss值/Hessian；随机性一致是工程推断非复现。H10080GB/checkpoint测overhead排参数optimizer base与optimizer.step临时峰、latency含optimizer，group pair仍可二次；任务质量不全胜pair。root source→actualowner采用及真实正文/相邻写后通过。采用依据 `papers/2026/04/_sources/daily-20260420/V3_DELEGATE_GROUPDPO_OWNER_PROPOSALS.md`。

- `SF-2026-ARXIV-2602-03412` — Daily `2026-02-05`；[CSO exact-v1](https://arxiv.org/html/2602.03412v1) §3.2.2–4/§3.3与§5.1 k/skip-PRM反侧。6分具体gap深入仅采用PRM定位→same-state one-action expert替换→CURRENT policy后缀→outcome验证→same-prefix step pair；不采noise-free、因果识别或equal-budget保证。Frozen pair、gold-based LLM judge与分支/后缀成本及普通pair回退保留；未运行代码/复现。root已实际核必要源与owner及148行正文、143–153邻接与末注，写后POST通过；日级Gate待验。

- `SF-2026-ARXIV-2602-06239` — Daily `2026-02-10`；[PEPO exact-v1](https://arxiv.org/html/2602.06239v1) §3/Alg1–2、§4.1条件、§5 Tables1–2与A1.4–5反侧。2+2+2=6，binary下估约束→tie mass/disjoint adapters→response-min的具体gap定点深入；有限support/log-ratio/BT/足够ensemble和tieupperbound条件保留，constant penalty及token-min不继承理论。接受率零/16cap、目标变体和全部前向/GPU-hours成本近正文；未运行代码/复现。root必要原源/owner写前通过并授窄锁，实际正文/邻接與末注經root非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-09533` — Daily `2026-02-12`；[ADPO exact-v1](https://arxiv.org/html/2602.09533v1) §4/Eq10/14、§5 Tables2–3、A canonical reward、B global partition、C prefix shift及E配置。2+1+3=6，具体分段非线性反馈差额深入，仅采用局部目标；sequence BT标签不授真实step credit，canonical shift与条件归一不授原reward/KL最优不变，细度反退与输出/搜索成本近正文。未核实现或复现；root必要原源/owner写前通过，实际正文/邻接与末注经root实际非作者POST通过、窄锁释放，不授日级Gate。

- `SF-2026-ARXIV-2602-11902` — Daily `2026-02-14`；[HyPO exact-v1](https://arxiv.org/html/2602.11902v1) §3 Eq7–13、§4/4.1、A5 同 SFT/同参数 h0 对照、§6 标签噪声与 A2–3 配置。采用负 reference margin 使 relative objective 过早满足而 raw policy margin 仍负的具体差额；不照录 Eq5/6 的 beta convention 冲突，不签 clipping 保持原 KL 最优、全局收敛或正确性，Table1 的 better-reference/h10 增益不单归因截断。未运行代码/复现；root 必要原源与 owner PRE、实际正文173/175与邻接165–187及末注519的非作者 POST 通过，窄锁释放，不授日级完成。

- `SF-2026-ARXIV-2602-13055` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.13055v1) §III-B Eqs6–7、§IV/关键反侧。2+1+2=5，固定 reference 的 consistency residual 替代接口差额深入；PF-ODE 相邻两点身份保留，surrogate 不借 DPO logratio/KL 保证，curricula/rank/sampler 混杂和 admin overlap lineage 保留，旧 curriculum 不重复计分。root 必要原源/actual owner PRE 与实际正文/完整邻接/末注非作者 POST 通过，锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-16802` — Daily `2026-02-21`；[RefEval exact-v1](https://arxiv.org/html/2602.16802v1) §3.2–4.3/Tables1–4与6。2+2+2=6，reference answer与frozen reference policy的具体差额定点深入；teacher偏差/风格、5候选10pairs、60K强teacher SFT与全部判分/训练成本近正文，不授免费self-improvement、规则verifier或judge真值。root必要原源/actual owner PRE、实际正文与完整邻接的非作者POST通过；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-22745` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22745v1)，必要原段/对照与局部反侧见当日core/owner packet。fresh非旧packet作者独核具体原证与actual owner差额，获root该owner窄ownership后写一段；作者正文及完整邻接实际顺读，root非写入者实际正文、完整邻接与自身末注POST通过，窄锁释放。采用正文窄命题，局部错误不授理论/全系统保证，未核实现或复现，不授日级Gate。
- `SF-2026-ARXIV-2602-22601` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22601v1)，必要原段/对照与局部反侧见当日core/owner packet。fresh非旧packet作者独核具体原证与actual owner差额，获root该owner窄ownership后写一段；作者正文及完整邻接实际顺读，root非写入者实际正文、完整邻接与自身末注POST通过，窄锁释放。采用正文窄命题，局部错误不授理论/全系统保证，未核实现或复现，不授日级Gate。
