# 第31章 RLHF

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-RLHF`
**Legacy Chapter:** Ch27
**Status:** Draft

**Roadmap Intent:** 人类偏好如何通过奖励模型影响模型输出。

## 本章要回答的问题

SFT 可以模仿 demonstration，但现实中往往很难为每个 prompt 写出唯一“标准答案”。人类更容易判断两个回答哪个更好。怎样把这种相对偏好变成可训练信号？为什么需要 Reward Model、reference policy 和 KL constraint？RLHF 为什么是一条 pipeline，而不是 PPO 的同义词？

本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。

本章使用 `x` 表示 prompt，`y_w`、`y_l` 表示 preferred/chosen 与 dispreferred/rejected response，`r_phi(x,y)` 表示 Reward Model score，`pi_theta(y|x)` 表示当前 policy，`pi_ref(y|x)` 表示 reference policy，`beta` 表示 KL regularization strength。

## Demonstration 为什么不足以表达偏好

对同一个 prompt，多个回答可能都正确，但在 helpfulness、clarity、safety、conciseness 和 style 上不同。若只提供一个 SFT reference：

```text
prompt -> one target response
```

所有不同 wording 都会在 token-level loss 中偏离 reference，即使它们同样可接受。

Preference comparison 改写监督问题：

```text
prompt x
candidate y_a
candidate y_b
human chooses y_w over y_l
```

它不要求标注者从空白开始写完美答案，却仍需要明确 rubric。若不同标注者对“好”的定义不同，pairwise label 只是某个群体、时间和 policy 下的偏好样本，不是客观真理。

## RLHF 的完整 pipeline

经典 LLM RLHF 可以拆成：

```text
pretrained model
-> SFT demonstrations
-> SFT policy
-> sample candidate responses
-> human preference comparisons
-> train Reward Model
-> optimize policy with reward + KL constraint
-> human / task Evaluation
```

这里至少有三种模型状态：

```text
policy model     produces responses
reward model     scores prompt-response pairs
reference model  anchors policy behavior
```

PPO 实现还常加入 value/critic model。于是 RLHF 不只是一个 loss function，而是跨数据生成、标注、多个 checkpoints、rollout 与 Evaluation 的迭代系统。

模型角色还可以沿训练阶段变化，而不必增加一个上线 judge。对于能核最终答案的离线任务，一个受限分支先让同一 policy 判断已有解答的最终 verdict，用 gold answer 对比产生二元 reward，再从这份 checkpoint 初始化生成阶段，恢复对自己最终答案的 RLVR 奖励。评论文字与 verdict 共用训练信号，不代表局部批评已经逐步核实；前一阶段学会判别，也不保证自动得到更好的生成策略。Candidate 来源、正误平衡、两个阶段的 task/reward identity 与 handoff checkpoint 都应保留。<!-- source-family:SF-2026-ARXIV-2601-08468 -->

作者等更新步数的两阶段对照支持局部质量—长度取舍，但不等总 rollout tokens、候选构造或 teacher 成本；混合训练和只做判别在部分任务仍可占优，某些任务正确率下降或输出更长。固定基础模型对生成文字的 PPL 与转折词减少只描述风格代理，不证明内部已经完成纠错。任务标签不可靠、阶段目标互扰或质量回归时，应保留直接生成 RLVR、原 SFT checkpoint 与独立评价，而不据“先判断”签发更少推理或生产收益保证。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20863:start -->
当 RLVR rollout 包含长尾生成与工具等待时，job-local 的同步、异步或 colocated 优化仍可能让 trainer 与 rollout
资源交替空闲。Cluster-level orchestrator 可以跨任务调度 rollout、training 与 tool capacity，并用 backlog 和阶段
状态重分配资源；它改变的是集群控制面，不改变 reward truth。收益是减少阶段性 idle，代价是 policy lag、跨任务
公平、抢占恢复和状态传输。作者集群与 workload 之外，若 lineage、隔离或 SLO 无法保证，应回退 job-local pipeline
或静态资源预留。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20863:end -->

## Reward Model 怎样学习相对判断

常见做法让 Reward Model 对整个 `(x,y)` 输出一个 scalar：

```text
r_phi(x,y) in R
```

使用 Bradley-Terry / logistic preference model：

```text
P_phi(y_w > y_l | x)
= sigmoid(r_phi(x,y_w) - r_phi(x,y_l))
```

Reward Model loss：

```text
L_RM(phi)
= - E_(x,y_w,y_l)
  [log sigmoid(r_phi(x,y_w) - r_phi(x,y_l))]
```

训练只约束 score difference。给所有 scores 加同一个常数不会改变 pair probability，因此 reward absolute zero 没有天然语义。

还要区分拟合一份“真实 reward”与拟合给定比较人口的条件胜率。记 `P(x,y,y')` 为有序比较的出现分布，实际监督的目标是 `p = P(x,y,y') / [P(x,y,y') + P(x,y',y)]`；人口 negative log-likelihood 等于与模型无关的条件熵，加上按这些比较出现频率加权的 Bernoulli KL。因此只有模型族可实现该目标、达到人口全局最优时，才能在 observed comparison support 上恢复胜率；不可实现时得到的是该模型族中的加权投影，换比较人口也会换拟合重点，而不是发现唯一的 absolute reward。有限且正概率的比较空间中，Bradley–Terry 还要求胜率 odds 能写成 `h(x,y)/h(x,y')`；一组条件独立假设可以充分导出该形式，但“存在另一个同胜率的独立分布”不证明原比较人口本身满足独立性。[精确版本的识别边界](https://arxiv.org/html/2602.10286v1)不授权任意连续空间、未比较 pair 或有限神经训练的普遍恢复保证。

比较覆盖因而不是单纯的数据条数：train-pair 分布、连接性、模型族与 test-pair 分布共同决定哪些差值有支持。作者有限 toy 实验中的较高连接性只在它成为瓶颈时有益，不能修复小 margin，更不能把胜率拟合变成人类效用或下游 policy 的正确性证书。应保留比较人口与 support 的审计、未覆盖切片的独立评价，以及原 pairwise loss；支持不足或模型失配时，不让一个可输出 scalar 的 Reward Model 自动替未观察偏好授权。<!-- source-family:SF-2026-ARXIV-2602-10286 -->

Scalar reward 也没有规定如何从 token 表示读出。一个替代分支先计算全部 K 个 refinement blocks，再由 router 混合不同深度表示；随后分别从末 response token、response-token 均值与可读取 prompt 的 attention pooling 得到三个视图，将这些视图与 prompt context 一同路由为 scalar。[AdaJudge 的受限 readout](https://arxiv.org/html/2601.08097v1)改变的是偏好模型的表示与聚合，不是动态 early exit；pairwise 偏好监督也不会自动提供 token evidence、process correctness 或下游 policy 的真值。<!-- source-family:SF-2026-ARXIV-2601-08097 -->

固定 pooling 的同 backbone/data/objective 对照支持局部 readout 取舍，但新增 blocks、router 与 pooling 增加参数和 inference latency，完整预算未匹配；不加 refinement 的一些安全、代码与推理切片仍更好。实验最大8B，按域平均的路由权重只能描述聚合行为，不能证明哪个视图因果拥有有效证据，也未核下游 policy 收益。延迟敏感、额外表示无净收益或质量回归时，保留原 last-token/固定 pooling、Bradley–Terry 目标和独立偏好评价，而不把“动态聚合”当作更省或更真实的奖励保证。

如果除了偏好方向，还能取得“这次比较有多强”的信号，训练对象可以进一步变成比较之间的 utility difference 排序，而不是把所有 response 直接排成同一条绝对序列。先在 annotator、长度等 strata 内核验强度 proxy 与 utility difference 的局部单调关系，再把这些比较及零强度 anchor 放入排序目标；单个比较的特例仍可退回 Bradley-Terry。Stratification 只是控制混杂的手段，不保证 reaction time、口头强度或 agreement 真有该单调关系，也不能从 ordinal 预测准确自动识别真实 cardinal utility。

强度的来源因此必须进入监督和预算合同。真实偏好标注中的 reaction-time proxy 可在分层后仍失败，stated strength 的小幅收益可能不显著，随机排序的局部改善也可能不迁移；利用四位 annotator 的 agreement，即使训练方向只抽一票，仍使用额外标签资源，不是免费的 single-label 增量。应分别报告 strata 支持、ties、metadata/标注成本和训练配置，不能把 Reward Model 的局部结果直接授予下游 policy。proxy 不可校准、分层样本不足或资源不公平时，保留原 Bradley-Terry 与独立人工偏好对照，而不强行加入看似精细的强度。<!-- source-family:SF-2026-ARXIV-2512-25023 -->

另一种监督直接给单条 trajectory 标注有序类别，而不是比较之间的 utility difference 强度。若类别真有可信的 cardinal 区间，回归区间 midpoint 是简单目标；只有“好、一般、差”的顺序后，固定数值间距与同类 return 向 midpoint 收缩就成为额外假设。一个 ordinal 分支每类抽一条 trajectory，以预测 discounted return 的排名匹配类别序号，使用 ranking MSE，而不强迫同类 return 相等。其条件理论识别的是满足跨类顺序的 reward 解集，不是唯一真实 reward；realizability、真实 return 的类别不重叠、exact rank，以及对所有跨类 tuple 成立都是结论的前提，有限 minibatch 拟合不能自动替它们签发保证。

这一分支增加分层采样、rank 算子与反馈类别维护成本，也不能只按反馈次数比较标注资源：一条 rating 与需要观看两条 trajectory 的 preference pair 不是等成本。有限控制任务中的五人试验存在不同标签下真实 return 重叠，因而只提供该设置中的经验表现，不满足条件理论的 non-overlap 保证；精确版本的 rank offset 与 regularization 展示不一致，不能照抄为可执行配方。它没有语言模型 policy 实测，也不证明 ordinal reward 足以保持最优策略或降低真实人类认知成本。类别顺序不稳、排名近似失配或监督支持不足时，应回退可核的 pairwise 偏好、可信 cardinal rating 或独立人工评价，而不是由 reward 拟合准确替下游行为授权。<!-- source-family:SF-2026-ARXIV-2601-09236 -->

语言模型的另一个有序分支不直接回归 scalar，而由 LM head 给出每条 response 的等级分布；在两条等级 marginal 独立的建模假设下，对 `s_chosen > s_rejected` 的下三角联合质量求和得到偏好概率。只有偏好方向仍不能识别真实绝对质量；若另有可追溯的好/一般/差粗锚，目标可把允许的质量 region 与该排序区域相交，保留 region 内顺序信号，而非只训练两个互不相干的矩形类别。[受限 ordinal reward 对照](https://arxiv.org/html/2602.12660v1)改变的是监督对象与读取方式，不证明数字间距有 cardinal 意义、分布宽度已校准人类分歧或锚本身是真值；用期望等级排名也须保持固定编码身份。粗锚生成、冲突处理及专家标签另有成本，且局部 RgFT 提升伴随部分 RewardBench/RMB 退步。应分别验偏好、等级校准和下游 policy；锚来源不可信或质量回归时，保留 Bradley–Terry、scalar readout 与独立人工评价。<!-- source-family:SF-2026-ARXIV-2602-12660 -->

等级监督还可以来自真实对话的后续反馈，而非预先要求用户给一对答案排序。[一条有界路径](https://arxiv.org/html/2602.08829v1#S2)先区分显式拒绝、错误纠正、积极参与和明确满意，保留无明确信号的 Unknown；再为各等级阈值学习“是否高于该级”的概率，以固定编码的期望等级读出 reward。这把反馈来源与 reward 目标分开，却不能把相关追问自动当正确性、没有反馈当负面，或把对正当拒绝的不满当应被优化掉的行为。相邻 turn 回填与拒绝核验均是版本化观测规则，须保标签出处、筛选人口和独立安全/任务效标；有序类别也不识别真实数值间隔或跨 query 效用。采集、分类、人工校准与在线候选生成都付费，有限 online DPO 收益不证明所有 RL 或等预算优越；反馈稀疏、筛选漂移或阈值未校准时，保留明确 Unknown、可信人工偏好与独立行为检查，不让用户参与度接管安全授权。<!-- source-family:SF-2026-ARXIV-2602-08829 -->

偏好方向还可能经过隐私通道再进入训练。对二元标签做 randomized response，以概率 `s = exp(ε)/(1+exp(ε))` 保留原标签、否则翻转，训练可见的是被扰动后的比较；若干净 Bradley-Terry 胜率为 `P`，观测标签的 likelihood 就是 `sP+(1-s)(1-P)`，不能把它直接当作干净偏好。相应回归构造用 `c=1/(2s-1)` 缩放标签来恢复条件均值；隐私越强、`s` 越接近一半，缩放越大，观测噪声和所需样本也随之增加。这里保护的是比较标签，不是原 prompt、response 或标注者的全部信息。

腐败数据与隐私随机化的次序因此也属于观测合同：先污染再随机化，与先随机化再污染，不是可交换的两条路径。在有限且可实现的 reward class、bounded reward 和论文规定的污染模型下，缩放后条件均值的偏差分别受 `O(α)` 与 `O(cα)` 控制，对应平方误差中的 `α²` 与 `c²α²` 项；算法不必知道次序，并不表示两者风险相同。离线结论还依赖同分布比较与 concentrability，在线分支另需探索覆盖及 oblivious 污染，不能授予任意自适应攻击者或神经优化找到全局解的保证。通道、污染或支持条件不明时，应保留可信人工比较与保守目标，先核观测人口和成本，而不是用“private alignment”替原始数据签发安全证明。<!-- source-family:SF-2026-ARXIV-2512-23816 -->

## 一个 preference score 小例子

假设 Reward Model 输出：

```text
r_w = 1.2
r_l = 0.4
delta = r_w - r_l = 0.8
```

则：

```text
P(y_w > y_l) = sigmoid(0.8) ~= 0.690
loss = -log(0.690) ~= 0.371
```

若模型把差值增大到 `2.0`：

```text
sigmoid(2.0) ~= 0.881
loss ~= 0.127
```

这表示模型更确信 chosen 优于 rejected，不表示 chosen 已经达到某个绝对质量，也不表示它优于未出现在 pair 中的所有回答。

## Preference data 的难点不只是数量

Preference dataset 需要控制：

- Candidate responses 来自哪个 policy version。
- Pair 难度：明显错误与细微差异比例。
- 标注 rubric、标注者背景和 disagreement。
- Position、length、style 与 verbosity bias。
- Safety 与 helpfulness 冲突如何处理。
- Ties、invalid prompts 和无法判断样本。

安全与 helpfulness 的冲突也可以改变 reward 的形状，而非只调两个正向分数的权重：令 judge 测得的泄漏比例为 L、帮助程度为 H，一条条件分支在 L>0 时给出 −min(L^α+H^β+b₁,1)，在 L=0 时才给 b₂+(1−b₂)H^β。因此泄漏分支中的 H 同样增加负项、达到 cap 后则不再改变分数，不是“泄漏时忽略帮助分”。这一监督以合成偏好和优化预算换取所测 privacy/helpfulness 取舍，却不把 judge-zero 变成现实零泄漏，也不由 reward 有界推出梯度或训练稳定。作者有限 PrivacyLens split/模型中仍有泄漏，另一个对照的 helpfulness 也更高；部署还需独立泄漏与效用验收，未通过时保留确定性 policy gate、人工复核或原偏好对，而不让软训练承担严格执行权。<!-- source-family:SF-2026-ARXIV-2602-13840 -->

安全与 helpfulness 的冲突还取决于监督如何呈现：完整规则在推理时直接拼入，不一定比由具体案例展示规则如何适用更可靠，局部对照甚至同时损伤拒绝与帮助行为。一条受限训练分支以 unsafe requests 上的 case reasoning 和较短 code 形成示范，再优化拒绝 outcome；其中“非空 reasoning/格式完整”只是单独的格式 reward，不是推理质量或内部判断正确的标签。KL 约束限制相对 reference 的漂移，也不自动认证 benign requests 的效用保持。<!-- source-family:SF-2026-ARXIV-2601-08000 -->

[局部安全训练证据](https://arxiv.org/html/2601.08000v1)来自两个8B模型、unsafe-only训练请求与有限 harmful/benign 测试人口；不同请求分母、拒绝标签与最终回答 judge 应分账。Benign 及通用能力切片仍可退步，有限模型和攻击集合不授普遍安全、未知攻击覆盖或真正内部 reasoning 的改善；案例合成、SFT/偏好优化与 judge 均有成本。任务清楚或目标冲突未验收时，保留原偏好对、独立 benign 回归与部署 gate，不让格式 reward 或较低 harmful 成功率替整个可用性签证。

安全训练的信号也不必全部来自显式 safe/unsafe 标签：一条受限分支先选定风险相关的合成视觉语境，再让 teacher 生成不含显式安全词的中性 VQA，经质量筛选后作 instruction tuning。这里省去的是人工安全标签，不是 teacher 示范、数据选择或训练监督；中性问题也不认证答案与场景不携带风险语义。[VSFA 的有限对照](https://arxiv.org/html/2603.08486v1)支持把这种数据构造作为候选训练分支，但图像、答案、筛选和预算没有在匹配的非风险图像对照中全部固定，不能将行为变化唯一归于视觉曝光。Harmful 成功率、合法请求拒绝与通用能力须分别验收，未给原模型对照的能力表不能证明保持原能力。按同一安全 benchmark 的响应差分筛出 SAE features，再以双向 steering 选择方向，只说明所选方向的局部行为敏感性，不认证唯一安全 persona 或完整训练中介。图像与 QA 生成审核、adapter 训练、attack/benign/能力评价及 SAE 搜索干预全部计费；真实请求人口、能力或安全回归时，保留可信带标签安全 SFT/偏好对、原 checkpoint 与独立 runtime gate，不由无显式标签或较低 ASR 批准发布。<!-- source-family:SF-2026-ARXIV-2603-08486 -->

若总是比较一个明显优秀回答和一个随机垃圾回答，Reward Model 容易学到表面 shortcut，却难以区分真实 policy 产生的相近候选。

相近候选的标签还依赖标注流程有没有保存同一个比较对象：用户选择、系统随后展示的回答和用户解释选择理由，不能被当作天然一致的记录。受限的 choice-swap 实验中，50 名参与者各经历四次调换后，只展示被替换的单个回答、不能回看原比较；未察觉调换不证明用户仍认可原选择，更不把随后流畅的解释变成可靠 preference label。由此可得到的工程要求是保留原 pair、选择索引、随后展示内容与解释的绑定关系，并允许回看、复核或弃权；这是对标注身份的设计推论，不是对所有生产界面或用户的失误率估计。

身份完整也不等于奖励强度可靠。一个固定 HH-RLHF 测试集上的受限对照中，训练标签随机翻转 10% 时，pairwise accuracy 只下降约 0.9 个百分点，reward margin 和相对未污染训练基线的预测翻转却已变化；这说明排序是否正确与偏好分离程度需要分开观测，不证明 margin 就是校准过的人类价值。另一个同为 30% 污染的 hard/easy 定向对照显示，污染位置会改变 accuracy 与 flip rate，但不支持“两种架构的 margin 均近乎毁灭”；后续 BoN 实验只测试随机污染，不能接成定向 hard 污染导致选择失效的因果链。其 clean Reward Model 参照也只是未污染评分器，不是独立人类真值，实验没有完成下游 RL 训练。标注身份审计、多 seed 重训、匹配模型与训练 recipe 的 margin/flip 检查及独立偏好评价均增加成本；对照不足时仍保留可核偏好对和人工抽查，不靠 held-out accuracy 或一句合理解释替后续 policy 验收。<!-- source-family:SF-2026-ARXIV-2603-08412 -->

固定长度、格式等属性清单便宜且透明，却可能遗漏尚未命名的 shortcut。一条有条件的审计分支先从响应与 reward 提出自然语言属性，在 Reward Model 偏好与独立 judge 反偏好的目标之间搜索 Pareto 候选，再用最小属性改写构造反事实响应，在独立 validation/test 人口上检验并控制多重比较。发现阶段的高分只授权继续检验，不证明属性已经是偏置，更不证明下游 policy 已学会它；需要同时保存 prompt 子分布、属性、改写与 judge 身份，避免把整个响应变化误归给单一属性。

这种搜索增加属性生成、重写、模型评分与检验成本，独立模型也不自动拥有 human truth，改写仍可能同时改变相关属性。[受限偏置发现实验](https://arxiv.org/html/2602.15222v1)的17个待验属性只有10个双侧显著；搜索深度比较只有一次完整运行，合成召回也仅覆盖三个 regex 属性，不能据此认证未知偏置的完整召回或普遍更优搜索策略。预算不足、judge/rewriter 共同偏差或反事实无法保持其余内容时，回退人工可解释属性、随机审计与独立评估，不用搜索置信度替奖励或部署行为签证。<!-- source-family:SF-2026-ARXIV-2602-15222 -->

只有训练终点回答，还可能看不出哪些奖励压力共同塑造了 policy。一条替代审计分支读取多个 checkpoint 的回答轨迹，用当前 reward-surrogate 的高残差 prompt 提出自然语言目标，筛选可解释性与变化趋势，再组合成线性 reward proxy，并用该 proxy 重训检查行为能否再现。这里拟合的是有限轨迹上的原 Reward Model 行为，不是唯一真实内部目标；ObjDisco 的 Model-Fit 是重训 policy 与原 policy 的平均原奖励比值，不是“解释了90%方差”或因果覆盖。固定样本目标集合上的贪心解释保证，也不认证开放目标发现最优。共同 judge/rubric 偏差、相邻 checkpoint 相关、候选生成与重训成本仍存在，人类匹配生成风格不等证明内部目标；残差或 proxy 再现不足时，仍要回到前述独立反事实检验、人工属性和 outcome 审计，不能让一条可读奖励解释替行为验收。<!-- source-family:SF-2026-ARXIV-2602-15338 -->

Candidate distribution 也会随 policy 更新而漂移。旧 Reward Model 在新 policy 产生的 out-of-distribution outputs 上可能不可靠，因此 RLHF 常具有数据闭环，而不是一次离线训练后永久有效。

多轮偏好还需要保存分支中的用户身份与历史。若 chosen/rejected 各自用先前对话生成下一轮用户输入，两条 trajectory 的差异就同时包含 assistant 动作与用户后续响应，而不是在同一外部状态下只替换一个动作的反事实比较。完整轨迹的 terminal scalar Reward Model 可以学习哪条交互整体更合偏好，却不能凭这种标签把收益归给某个 tool step；增加多轮 contrast 也不自动得到过程信用。应绑定每条分支的历史、用户模拟器、candidate policy、rubric 与 teacher/judge 身份，区分 trajectory preference、动作替换比较和 step credit。

保持固定用户脚本便于匹配对照，却可能牺牲真实交互对动作的响应；另一条路径是保留可审计的反事实分支，或在独立用户人口上检验偏好和最终结果。多轮生成、contrast 筛选与评价都增加预算，同一 teacher 兼任模拟器与 judge 还会带入共同偏差。受限合成多轮实验只支持该轨迹偏好构造，不证明独立真实用户收益、长程工具可靠性或更细 credit。分支与评价身份不可恢复时，应保留 trajectory-level 标签的有限权限，回退目标清楚的单轮偏好对或独立 outcome verifier，而非制造逐步监督。

“不要迎合错误说法”还需要与“遇到可靠新证据应更新”一起标注。若偏好对只区分坚持己见和接受反驳，却没有把**来源可靠度与题目设定的先验强度**写入标签，同一表面反驳下的接受或拒绝无法被训练目标识别，实测容易退化为偏向固执或轻信的总开关。一条受限分支让训练样本覆盖先验强弱 × 来源可靠度 × 保持/更新动作，并分别检查拒绝无依据施压、采纳可靠纠错和拒绝不可靠来源。但若“可靠度”只是来源自报数值，模型可能学会读取这个字段而不是验证来源：独立审计、provenance 与冲突处理必须由证据系统另行提供。该结果只来自构造的明确数值可靠度任务和少数模型，不证明自然文本中可靠性可自动判真。<!-- semantic-body-binding:SF-2026-ARXIV-2609-22359 -->

形式完整的规范说明还不能决定行为在该情境下是否恰当。监督可以先把信息流程识别、norm 识别和回答的 norm appropriateness 分开；再固定同一 completion，分别在适用 norm context 与随机错误 context 下评价，用两者 reward 差异抑制只会复述规则的 shortcut。一个受限分支先把提取的类型化 norm 与流程转换为 SFT，再用正确 context 分数减去带权错误 context 分数并截断的信号做 GRPO。这里 retriever 和 critic 提供训练 proxy，不拥有现实规范真值，更不能由模型生成的规范自动授权运行行为。<!-- source-family:SF-2026-ARXIV-2604-20904 -->

双 context 评价、norm 检索/抽取和 policy 训练增加成本，也可能把 judge 误解和 context 选择偏差一同学入参数。作者的虚构社会规范及 9B 模型只支持受限迁移，HIPAA 任务亦有不利切片；附录称 reward judge 为 Qwen3-32B，而 disclosure 写 Qwen2.5-32B-Instruct，这一身份冲突不能静默修补。它不提供普遍法律遵从或零 trade-off 保证。现实高风险场景仍需独立规范来源、人工争议处理和确定性 policy gate；原有直接偏好对在目标清晰、上下文稳定时更简单。部署执行保护交第72章，不由这项训练 reward 批准。

### Preference Admission 不必强迫所有样本进入 Reward Model

对全部 preference pairs 做 strict mass-conserving matching，在数据近似干净且每条标注都应被解释时最直接；混入 outlier、
冲突标签或语义不一致样本后，这条约束会强迫 Reward Model 拟合本应拒绝的质量。Partial optimal transport 提供一个条件
分支：只匹配与语义一致性相容的 preference mass，把剩余部分作为被拒绝样本保留，而不是把 rejection 偷换成负标签。
Admission owner 保存原始 pair、selection mask、embedding/reward-model revision 与 dispute path，trainer 只消费冻结后的
admitted set。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06036 -->

它用更少的错误监督换来两两距离计算、selection bias 和新的超参数；“干净样本语义更一致”本身也只是可检验假设，
systematic 或 adversarial noise 可能同样形成紧密 cluster。现有理论只约束 selected subset，作者实验也限于三套 preference
data、7B–72B 模型与其 judge，未解决 online `O(N²)` 成本。无法独立验证 selection quality 时，应回退原始数据、人工争议处理
或带噪声鲁棒但不丢弃样本的 baseline，而不能把被过滤数据静默消失。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-01831:start -->
Preference contract 还必须显式包含“谁偏好什么”。把所有 pair 压成一个 universal-quality ranking，在用户目标一致时最简单；当用户对长度、风格、风险或领域有不同取舍时，同一 response pair 可能出现相反标签。Reward Model 的输入因此可以加入版本化 preference profile，并用语义等价的 profile paraphrases 检查表示是否稳定：

```text
prompt + candidate pair + explicit preference contract
→ conditional reward comparison
→ paraphrase-consistency and held-out preference slices
→ downstream policy evaluation under the same contract
```

条件化获得个性化表达，却新增 profile 获取、隐私、prompt injection 和未见偏好的 extrapolation。synthetic English preferences 只能证明 intrinsic ranking/generalization，不能证明真实用户分布、跨文化价值或 PPO/DPO 下游收益；缺少可信 preference identity 时，分开训练窄域 reward、请求澄清或保留通用保守 baseline 更合理。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-01831:end -->

### Pluralistic Aggregation 不能把 Group State 压成一个平均 Reward

#### Reward Basis、Jury 与时间权重是三种不同状态

直接为每个人群训练独立 reward model，能保留差异却难以扩展；把所有偏好平均又会抹掉少数群体。一个中间分支先学习低秩 reward basis，再由显式规则筛选 jury membership，并随时间更新各群体权重与策略。Basis owner 只表示可复用偏好方向，governance owner 决定谁进入 jury，deployment policy 持有当前权重；三者不能由同一聚合器静默改写。

这种分解提高可追踪性，却引入 basis 误设、代表性偏差、时间漂移与治理成本。群体少且目标稳定时，独立模型或固定多目标 reward 仍可用；无法证明代表性时，应报告分组结果并保留人工决策。现有 exact-v1 只支持作者的偏好数据与民主过滤设定，不建立普遍社会合法性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01642 -->

低秩分解还可以支持少样本个体适配，而不把每位用户都变成独立的大模型：共享 reward basis 与初始混合权重，用该用户的 support pairs 只更新低维权重，再以分离的 query pairs 更新共享 basis 和初始化。Query loss 可以提高难适配用户在 outer 更新中的权重，但它是当前模型的损失，不是用户价值真值或逐人最坏风险保证。[受限 meta-reward 实验](https://arxiv.org/html/2601.18731v1)中最难一成用户仍可低于随机准确率，重加权也只有有限增量；少量显式静态偏好不验证漂移、隐式噪声或下游 policy。应绑定 user/support/query 身份，分别计共享训练、个体适配与标注成本；低维参数少不认证全链费用更低。用户信号不足、query 支持失配或困难切片不稳时，回退固定 basis、独立窄域 reward 或请求澄清。<!-- source-family:SF-2026-ARXIV-2601-18731 -->

Federated RLHF 用平均 group reward 聚合更新，在群体偏好近似同质且每组信号质量相当时简单有效；群体对齐程度、样本量和历史收益不同后，平均会让多数或高分群体持续主导，直接取最差群体又可能牺牲整体可用性并放大噪声。

自适应 pluralistic aggregation 可以根据每个 group 的历史 alignment reward 调整 PPO 使用的群体 reward 权重。在这里的实现分支中，服务器生成回答并广播给群体；客户端用冻结的偏好预测器和本地 few-shot 数据产生逐回答 reward，服务器聚合这些 reward vectors，再更新中央 policy。这不是客户端参数更新的联邦平均。聚合 owner 必须保存 group identity、reward/evaluator revision、历史窗口、权重变化和 fairness/utility decision；客户端提供评价信号，不能自行改变全局公平目标。收益是把 worst-group 与 overall alignment 放入同一显式 trade-off，代价是 group 定义错误、历史漂移、权重振荡和隐私泄露；原始偏好数据不出本地，也不等于返回的 reward 已有差分隐私保证。

群体标签不可信、样本过少或权重不稳定时，应回退有界平均、min-group constraint 或人工 policy review。公开结果只覆盖 GLOBALQA、OQA 与三类模型设置，不证明未测人群、文化或 preference protocol 的公平性。

<!-- source-family:SF-2026-ARXIV-2604-04261 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21822:start -->
当不平衡 crowd preference 同时混入 user-specific goal 与真正共享的 safety penalty，单一平均 reward 可能让多数
context 接管排序，调权也无法解开两种责任。一个条件分支先验证 shared-safety 假设，再从 preference data 学习
一组低层 behavior skills，冻结 skill policy，由 downstream controller 只在该 support 内组合任务行为。Preference
owner、skill owner、task controller 与 hard-safety gate 必须分权。它用较少 scalar entanglement 换取 offline data、
skill coverage 与 latent-basis 成本；共同安全目标或 skill expressivity 不成立时，应回退分组报告、显式 safety cost /
hard gate、独立 task baseline 与人工裁决。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21822:end -->

### 多目标 Reward 的 Bottleneck 聚合不能冒充 Hard Constraint

算术均值在多个 reward channel 尺度相近、允许相互补偿时最简单，却不能证明每个 must-have criterion 都满足：一个目标的高分
可以掩盖另一个目标的失败。SoftMin 或 variance-penalized aggregation 可作为 risk-sensitive 分支，让最低或分歧最大的 channel
获得更多更新权重；aggregation owner 必须版本化 channel 定义、归一化、temperature/penalty 与 schedule，optimizer 只消费
冻结的合成 reward。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05750 -->

这种分支提高 bottleneck adherence，却按“当前难度”而非 policy 声明的优先级分配控制权，容易放大 noisy reward channel；过高
temperature 或过早启用还可能导致 collapse。真正不可补偿的 safety、schema 或 execution constraint 仍需逐项报告并由
deterministic gate 拒绝。作者证据只覆盖 HealthBench、GPQA、tool-calling、Qwen2.5 和其 17/2-channel 配置，且对 group size、
schedule 与噪声敏感；channel 校准不足时回退分项 reward、保守均值或 hard gate。

偏好分布也可以只改变完整候选的选择，而不更新 policy：在同一 realized pool 内，保留多位评分者或代理扰动的 score 样本，对 `β>0` 用 `Vβ=−log(mean(exp(−βr)))/β` 得到较悲观的经验价值，以 `mean(r)−Vβ` 表示相对均值的 risk premium；另可先保留 near-best value 候选，再按 disagreement 选择。这里重加权的是给定评分分布，不是重新生成候选或识别全部用户风险，score 尺度、β、归一化与 pool 身份必须一起保存。[DARC 的受限对照](https://arxiv.org/html/2603.08145v1)不把 rewrite/RM 分散等同于真实人群异质，低争议也不证明事实正确；LCB 要求的采样与 proxy closeness、跨 prompt 的尾分数和每个用户的 tail 是不同验收对象。原证 τ 选择的目标口径不一，空可行集回全 pool 也不是硬风险 cap，因此不把这条 recipe 授为安全过滤。所有候选生成、rewrite/筛选/重试、RM/多 scorer、开发集校准及独立人评均计费，局部 latency 不签全链净收益。代理、尺度或可行集失配时保留原 mean selector、固定可信预算、独立 held-out 人评与明确 abstain/hard gate，不由 soft-pessimism 批准行为。<!-- source-family:SF-2026-ARXIV-2603-08145 -->

聚合之前还要问判据从哪里来。全局质量分在目标稳定、人工尺度已校准时简单，却可能让开放式输出靠自我赞美或表面格式取得高 reward；一个受限分支先为同一输入生成多教师候选，与初始 student 输出比较，只把共识中尚未满足的部分转成带严重度权重的 binary criteria，再冻结为逐样本 rubric。训练 rollout 随后由文本 judge 逐项检查是否表达这些规则，以权重归一的通过率产生 reward；教师与 writer 的大模型调用前移到制备阶段，训练并非每步重新投票或刷新 rubric。这与下文从 verdict pattern 推断质量的测量器不同：这里改变的是评分尺子的来源和覆盖对象，后者消费已经定义的判据。

缺口导向也留下一个新的盲区：初始已经正确的部分被排除，后续补齐全部 criteria 不保证其他事实仍正确，更不保证教师未提到的错误被覆盖。只读规则和 caption 的文本 judge 不能重新看到原图验证事实，共识与匿名教师身份也不认证独立真值；committee、初始 student、criterion、权重和 judge revision 应共同保存，并以独立视觉证据和保留任务验收。原稿的共识阈值与 prompt 口径不同，必须先锁定实际规则，不能自行修成可复现 recipe。[必要方法与直接反侧](https://arxiv.org/html/2603.09160v1)支持有限 caption reward 分支，但模型 judge 偏好和均值提升不授普遍优于人工或无遗忘，部分保留任务仍退步。教师制备、全部逐项评分、rollout/训练与独立审核均计费；规则饱和、遗漏或质量—费用不改善时，保留完整人工 rubric、原 reference/SFT 与独立 outcome gate，再考虑受控更新尺子，不让模型自行宣布 verification 已闭合。<!-- source-family:SF-2026-ARXIV-2603-09160 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-35646:start -->
加总rubric点数适合判据尺度清楚、优先级由任务owner明确的场景；判据难度与区分度不同后，同样总分可能来自不同verdict pattern。一个条件测量分支令各criterion通过概率随共同scalar quality严格上升，在给定quality后条件独立，用题目和criterion文本预测difficulty/discrimination，再以verdict likelihood和prior推断reward。该scalar是模型相对的测量，不是正确性或安全真值；在线校准改变测量参数，也应同policy版本分账。

固定测量器后，可按当前rollout quality估计未评criterion的Fisher信息，每获得一次verdict再更新推断，避免把固定高权重当每个quality区间的最优评估。[Rubric IRT v1 §3–5](https://arxiv.org/html/2609.35646v1)的局部信息界依赖monotone/条件独立模型，不能把likelihood score的界授予MAP reward或完整policy；judge相关性和latent误设会破坏解释。额外测量器训练、校准和选择都有成本，RubricBench半预算也有退步。独立truth、must-have gate与分项结果仍须保留，目标不共用scalar、校准失效或预算宽松时回退完整rubric/既有固定聚合。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-35646:end -->

同质文本输出可以共用 string matching；回答同时包含正文、公式与表格后，先要分清每路 reward 在比较什么，再讨论如何聚合。一个 format-decoupled 分支分别比较 text edit similarity、公式的 LaTeX token overlap 与表格结构，再只对 ground truth 中非空的类型取平均。此时 type membership 决定了每个样本的分母；缺少某种类型不等于该项通过，也不能把没有参考对象的分项默认为满分。Reward owner 应版本化类型划分、匹配对象、eligible population 及 regex/parse 失败口径，聚合器消费这些定义，不能通过改变分母静默改写目标。

分工能减少一种 string metric 对异质对象的误判，却不提供全格式正确性保证：公式 BLEU 不等于数学或表达式语义正确，table TEDS 不等于全部格式有效，平均分也不证明每路都满足。作者在同一 Qwen3-VL-4B 文档解析设置中的分项消融支持局部 reward 分工，text 指标并非随整体分数单调改善；难度过滤的不同样本比例也不是等预算比较。格式拆分增加 parser、参考对象维护与分项校准成本；输出同质、类型抽取不稳或语义要求未被代理指标覆盖时，应回退已校准的单项匹配、分项报告与独立 semantic/validity gate，不能让聚合 reward 替代验收。<!-- source-family:SF-2026-ARXIV-2601-08834 -->

固定聚合假定同题候选使用同一套奖励尺子；若希望按回答的实际特征分配多目标压力，一条受限分支在处理完整prompt与response后，从末层hidden state读取线性controller，为组内每条已完成回答独立采样reward-emphasis action并形成scalarized reward，再用组advantage将另一个head的训练信号缓存为(h,a,A)，周期更新controller。它改变的是完成轨迹的奖励测量，不是生成前的prompt-only控制，也不同于下面直接组合policy gradients；controller、channel归一化、buffer与更新周期须随policy保存，这是为重放该接口所需的工程约束而非原文完整协议。[MAESTRO的有限结构证据](https://arxiv.org/html/2601.07208v1#S3)未闭合完整action到权重向量映射，不能补成执行recipe、充分统计量或Pareto/防梯度消失保证。逐response改变权重还会削弱raw score可比性，不能靠adaptive聚合修复有偏proxy；完整序列表示、head/buffer、reward judge和两角色更新均付费，部分所测任务反而增加overhead，早/末状态对照也非处处严格改善。奖励身份、独立质量回归或净成本不成立时，保留固定权重、分项验收与原组内训练，不让controller兼任truth或hard gate。<!-- source-family:SF-2026-ARXIV-2601-07208 -->

### 从 Reward 混合演进到 Gradient-space Harmonization

标量加权或根据噪声动态调整 reward 权重，在各 channel 的梯度大体同向时简单有效；当 specialist samples 的优势被总
reward 稀释，或不同目标在参数空间直接冲突时，仅在 reward 数值层混合不足以说明最终 update direction。更强的分支先为
每个 reward 独立估计 advantage 和 policy gradient，再由受约束优化器选择共同方向，并周期性求解、用 EMA 平滑系数，
把每步 `R+1` 次 backward 的成本转化为可摊销的 controller state。

这要求明确分开四种所有权：reward/evaluator 定义目标证据，advantage estimator 估计每路信用，gradient controller 提议
组合方向，optimizer 才提交参数更新。收益是让冲突成为可观测、可治理的状态；代价是额外 backward、QP 数值不稳定、
系数滞后和 evaluator correlation。现有证据只覆盖 SD3.5-M、rank-32 LoRA、五个 rewards、16 张 H200 与作者图像指标，
不证明更大模型、视频或生产训练普遍获得 Pareto 改善。reward 同尺度且方向稳定，或控制器成本与抖动不可接受时，应回退
固定 scalarization、sequential curriculum 或单 reward specialist。

<!-- source-family:SF-2026-ARXIV-2605-06507 -->

### Demonstration-derived Reward 仍需要可识别性与多重验收

成对偏好标注能直接表达相对选择，却昂贵且可能覆盖有限。另一条分支从 demonstrations 与当前 policy samples
在一个显式 response-feature 空间中的分布差异恢复 reward，再用于 reranking 或 on-policy 更新。它减少人工 pair，
却把目标强烈绑定到 feature/evaluator：多个 reward 都可能解释同一 demonstrations，policy 也可能学会利用未观测
维度。因而 reward proposal 必须在 held-out 行为、adversarial samples 和更新后 policy 上重验；不可识别或被利用时，
回退人工 preference、verifiable reward 或冻结 reranking。
<!-- source-family:SF-2026-ARXIV-2607-24900; daily-trace:papers/2026/07/29/README.md -->

Demonstration 的目标也可以来自专家视频的相对帧序，而非成对偏好或响应特征密度：以初始、当前和目标观察预测进度分布，将其均值提议为 potential，再用相邻观察的折扣差构成 dense reward。Online rollout 另可将非专家样本的预测分布推向零均值、较宽的先验，限制未覆盖状态的乐观外推；非专家不天然错误，预测方差也不取得 epistemic 校准或任务成功真值。Reward model、采样 policy 与 replay/参数重要性状态应分别版本化，并用真实任务 outcome 与旧任务独立回归验收。[ProgAgent 的有限模拟对照](https://arxiv.org/html/2603.07784v1)中 potential 随训练更新，有限 episode、goal 与原 reward 的绑定未闭合，不由 potential 形式直接授 policy invariance；expected 曲线也不认证无 hacking，联合移除 replay/重要性正则不识别各项独立因果。Expert 制备、在线探索与 reward refinement、replay/正则和调参均计费，编译并行不抵完整训练预算；示教、先验或旧任务退步时，保留固定/可验证 reward、可信专家监督和独立 held-out gate，不由拟合进度批准真实机器人安全。<!-- source-family:SF-2026-ARXIV-2603-07784 -->

更保守的演进是先由目标 policy 生成候选，分别用 helpfulness、factuality、conciseness 等 rubric 和 process critic
校正，再只接纳多评审高共识样本进入训练。这个 Gate 把数据质量置于 objective 之前，但不会让 evaluator 变成
真值：同源评审可能共同误判，多路调用也增加成本。低共识样本应保留为未决或交给人类，而不是靠平均分强制纳入。
<!-- source-family:SF-2026-ARXIV-2607-25136; daily-trace:papers/2026/07/29/README.md -->

## 从 Reward 到 Policy objective

### Solver 与 Auditor 让 Reward Design 成为双层激励问题

单一 reward model 直接给 solver 打分，在 evaluator 稳定且错误成本低时最简单；当 auditor 还要发现
并纠正 solver 的错误时，奖励只鼓励“首次答对”会让发现问题、接受修正和诚实暴露不确定性缺少激励。
更完整的设计分别定义 solver proposal、auditor finding 与成功 correction event，再由上层选择奖励
参数，使局部最优行为仍指向系统目标。它用机制设计和额外交互换更可解释的监督，却引入均衡选择、
collusion、auditor 误判与固定默认策略依赖；无法独立验证纠错时，应回退确定性 verifier 或人工审阅。
作者博弈模型与有限实验只支持其假设内的 incentive pattern，不证明开放 Agent 系统已经对齐。
<!-- source-family:SF-2026-ARXIV-2605-01643 -->

但增加一个 auditor 并不是唯一分支：多目标主答复奖励还可能鼓励模型隐藏自己已经知道的违规。另一种受限设计保留主任务的原有奖励，在回答后要求同一 policy 单独报告目标、遵从情况与不确定性，并只按这份报告的诚实度给它奖励；承认主回答有问题不能增减主回答的奖励。这样把“任务做得怎样”与“是否如实披露”拆成两个 reward channel，用额外生成和 judge 成本换取诊断信号。它与独立 auditor 是可组合的不同分工，不是已经消除错误的替代方案。<!-- source-family:SF-2025-OPENAI-CONFESSIONS -->

这种分离首先是输出信用与奖励的分离，不是同一 policy 的共享参数被隔离；如果再把自报直接用于惩罚主回答，还可能重新引入隐瞒激励。模型不知道自己错了、指令含糊、judge 被利用或更强优化压力都可能使自报失效。[原始 proof-of-concept](https://openai.com/index/how-confessions-can-keep-language-models-honest/)只支持在所测压力任务中增加行为可见性，不支持“不再违规”或普遍可靠性。任务成功、安全与模型晋级仍要由独立证据判定；自报不足时回退外部 verifier 或人工审阅，而不是用诚实报告替代验收。这也说明接下来设计 policy objective 时，必须同时写清奖励属于哪个输出、更新如何影响共享参数，以及未被奖励证明的行为边界。

如果只最大化 learned reward：

```text
max_theta E_(y ~ pi_theta(.|x))[r_phi(x,y)]
```

Policy 会主动搜索 Reward Model 的漏洞。更常见的抽象加入对 reference policy 的 KL penalty：

```text
max_theta E_(x, y ~ pi_theta)
[
  r_phi(x,y)
  - beta * KL(pi_theta(.|x) || pi_ref(.|x))
]
```

`pi_ref` 常从 SFT checkpoint 冻结得到。KL 项限制 policy 离开已知语言和行为分布的速度，也防止 Reward Model 成为唯一目标。

`beta` 太大时，policy 几乎无法改变；太小时，更容易 reward overoptimization。KL 是更新幅度控制，不是事实性或安全性的证明。

惩罚施加在哪些样本上，以及相对哪个 reference 测量，也可以分别变化。一条生成模型训练分支先在同一 batch 内比较优化 proxy 与辅助评分器的 win-rate，把相对分歧较高的样本选为 KL 惩罚人口；这只是 ensemble-relative 排序，不是校准的人类真值，也不等于删去这些训练样本。若 reference 达到阈值或固定周期后 hard-reset 到当前 policy，下一次 KL 已使用新锚点，局部约束不能签发距最初 base 的累计移动界。[有限图像训练对照](https://arxiv.org/html/2512.24138v1)里部分所谓 unseen 指标同时参与辅助 gate，不能拿它们独立认证无 reward hacking。训练身份因此应同时保存 selected population、anchor version 与 reset 条件，另付辅助评分、特征比较和独立人口评价的成本；评分器失配或累计行为漂移未受控时，回冻结 reference、统一惩罚或暂停更新，而不是继续追自身 instrument 的高分。<!-- source-family:SF-2026-ARXIV-2512-24138 -->

限制离开 reference 的分布距离，与限制 proxy objective 在参数邻域内的尖锐变化，是两个不同控制对象。一条受限分支惩罚训练目标的梯度范数，以沿梯度方向的参数扰动和两次梯度差近似其更新，尝试偏向更平的 reward maxima；它不是让模型回到原输出分布，也不使 proxy reward 自动变成真值。[原版本的理论与直接控制](https://arxiv.org/html/2602.18037v1#S3)需要连续 Gaussian action、平滑 proxy、true reward 的 Lipschitz 等条件，离散 LM 只提供有限实验外推，不授防止 reward hacking 的普遍保证。实际 LM 实现只扰动部分 transformer 参数、clip 并复用原采样 actions，没有重要性修正，因而不当作无偏 policy-gradient 算法；扰动、额外 backward、LR/regularization 搜索和独立评分仍计费。较强 RM 下 reference reset 也可更好，judge reward 与规则 accuracy 不必同向；flatness、质量或费用未通过时保留冻结 reference、KL/已验 reset 与暂停更新，不让更小梯度范数签发安全或事实性。<!-- source-family:SF-2026-ARXIV-2602-18037 -->

### 改变输出分布是目标，不是无副作用的偏好标签

只要 policy update 真正生效，条件分布就不再与 reference 完全相同：某些候选 response 的概率上升，另一些必然相对下降。Preference optimization 不是在原模型外面附加一个“更喜欢”的标签，而是在重写给定 prompt 下的 action probability。

KL reference 只定义更新坐标，不能单独控制偏好数据未覆盖区域的 distortion。若 preference sampling distribution 与 reference policy 的 density 差异很大，平均 KL 很小也可能隐藏局部行为重写；系统应保存两者的覆盖关系、density-ratio 假设和被裁剪区域。匹配分布可以收紧理论边界，却会牺牲长尾价值覆盖，因而仍需 held-out behavior 与独立安全评估。

<!-- source-family:SF-2026-ARXIV-2609-12651 -->

这里还要区分两种都来自人的监督：`p_H(y|x)` 是人在同一情境下**会写出什么**，`r_P(x,y)` 则表示人**希望助手写出什么**。最大化偏好奖励并以 `pi_ref` 为 KL 锚点时，理想化最优分布与 `pi_ref(y|x)·exp(r_P(x,y)/beta)` 成正比，而不自动等于 `p_H`。即使 `pi_ref` 已拟合人类回答，只要奖励在这些回答上不是常数，偏好加权仍会把分布从人类行为推开；若 reference 原本不匹配人类行为，只有奖励恰好补偿二者的 log-density ratio、且支持集允许时，才可能同时达到两目标。这不是 RLHF 失败，而是目标不同：优秀助手未必应当像普通人那样回答。

因此把模型用于人群模拟、行为研究或“像人”验收时，不能拿 preference win rate 充当 human-response fidelity。需另锁定人类回答样本、参考分布、提示与采样协议，在 held-out responses 上测试 likelihood 和生成分布；提高人类相似度也可能增加冒充与操纵风险，应由应用 owner 决定是否需要。现有论文在所测人写回答、偏好权重与 DPO 设置中支持两目标分离，却不建立任意人群的真实分布，也不要求通用助手追求人类模仿。<!-- source-family:SF-2026-ARXIV-2609-23640 -->

同一奖励加权机制用于离线后训练时，还要说明噪声与 temperature 共同限定了什么。在固定 context、有限动作且 behavior support 内，若观测奖励是真 reward 加各动作独立的零均值 sub-Gaussian 噪声，以 $\sigma$ 表示噪声尺度、$\delta$ 表示失败概率预算，理想的精确归一化 tilt 的动作误差半径可写成 $\epsilon=\sigma\sqrt{2\log(2|\mathcal A|/\delta)}$。真实 reward 在 $[0,R_{\max}]$ 时，相对 behavior 的最坏价值退化可由 $R_{\max}(e^{2\epsilon/\lambda}-1)$ 控制；较大 $\lambda$ 减少噪声敏感度，却也让 policy 趋回 behavior。这是给定假设下的退化容忍界，不是正改进、逐用户不伤害或多步 Agent 安全保证。置信预算、支持集、reward 范围与噪声模型都应写入训练验收，偏置反馈、未观测动作或多步状态分布变化不能直接沿用这条界。[精确单步范围与证明](https://arxiv.org/html/2603.10279v1)见§4及Appendix A.2–A.3。

这个 ideal-policy 界不能跳过实际 weighted-SFT 的投影误差：归一化目标含每个 context 的 $Z(s)$，直接用未归一化指数 weight 会改变跨 context 的拟合权重；共享参数、有限样本和未收敛优化不自动恢复逐 context 最优分布。需把理想 tilt、实现中的 weight/normalizer、实际 policy 和 held-out 行为分开验收，另算数据、reward 与训练费用。不在线优化 learned Reward Model 只移除一个代理搜索通道，并不消除离线标签偏差或高权重捷径；高 rating 过滤后的 next-item 排名也不是无偏用户价值。噪声假设、coverage 或部署切片不成立时，保留 BC/plain SFT 或更保守权重，并让独立质量与安全评估决定是否采用；固定 behavior occupancy 也不能替一般 MDP rollout return 背书。[训练接口与评价限制](https://arxiv.org/html/2603.10279v1)见§3、5–7。<!-- source-family:SF-2026-ARXIV-2603-10279 -->

```text
pi_ref(y | x)
-> reward / preference-weighted update
-> pi_theta(y | x)
```

KL constraint 只限制这种重写的平均幅度。若它是在某个 prompt distribution 上求期望，平均 KL 很小仍可能掩盖少数 prompt、语言、领域或 safety slice 上的较大移动；Sampling temperature、Prompt 和 Context 又会继续改变最终可观察分布。因此“KL 没超阈值”不能证明原有行为逐项保留。

这里还要把三种边界分开：pretrained parameters 中可被适当条件触发的 **latent capability**，当前 policy 通常会输出的 **elicited behavior**，以及接入 Retrieval、Tool、Sampling 与 guardrail 后的 **system capability**。RLHF 最直接改变第二层：它可以让已有能力更容易被调用，也可以压低不希望出现的行为；参数更新同时可能学习新模式或造成 capability regression，但单凭某个回答消失，无法证明相关表示已从参数中删除。反过来，某项 win rate 上升也不能证明模型获得了跨分布的新推理能力。

所以能力边界不能由 reward curve 或平均 KL 推断，必须比较 base/SFT/reference 与新 policy 在相同 decoding contract 下的多切片 Evaluation，并单独记录 capability gain、behavior shift 与 regression。InstructGPT 的原始实验同时报告目标 prompt distribution 上的人类偏好和公开 NLP evaluations，正体现了这两类证据不能互相替代。

行为优化还须将 objective 与 target-distribution 适配分成两轴：同一训练目标可沿用原人口或加入新域，迁移好坏不能只归于目标名称。用教师产生新答复并自动设为 chosen、原 reference 自动设为 rejected 时，标签代表构造约定，不是经独立相对偏好裁决的真值；offline可直接SFT或pair训练，online则先训练reward model再做policy更新，监督路径与成本不同。<!-- source-family:SF-2026-ARXIV-2601-05882 -->

[受限域迁移对照](https://arxiv.org/html/2601.05882v1)的Llama3.3-70B每prompt采三候选、temperature .7，并非greedy数据生成；GPT5-nano-2025-08-07 judge随机展示顺序，diversity另用500prompt×16、temperature1。高synthetic SFT胜率仍伴语义/语法diversity下降，online保多样性也未必适应shift；不同QA/摘要人口不能合成通用收益。教师、RM、rollout与训练费用分账，目标概述不当实现公式；teacher偏好失真、覆盖坍缩或新域回退时，保留真实target标签、原reference与多切片质量/多样性回归，不用胜率授新的偏好真值。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22156:start -->
当 verifier 已证明某个 deviation 优于陈旧 reference，symmetric KL 仍可能把更新方向拉回 prior。One-way trust-region
分支让 verifier-signed advantage 决定方向，reference log-ratio 只以正权重调节幅度：inferior deviation 加速，
superior deviation 降幅而不反转，并把 reference refresh 作为可回滚 ratchet state。它增加 reference forward、
active-sample、clip 与 refresh 状态，也会放大 false-positive verifier 并锁入漂移。Qwen/math binary-verifier 证据不
证明单调自我改进；verifier confusion、非可验证能力回归或 coverage/KL 漂移时，应冻结最后通过的 reference，
回退 symmetric KL / plain GRPO，并由独立 held-out 与 safety Gate 决定下一次 refresh。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22156:end -->

### Reverse KL 会把“找到高奖励”收缩成单一路径

KL 约束最初合理，因为它限制 policy 远离 SFT reference 的速度；但 reverse KL 倾向于追随当前高概率、高奖励 mode，训练稳定并不等于保留了可替代行为。当目标分布本身包含多条有效解时，优化 owner 需要同时观察 reward 与 response-distribution coverage，并把 forward/group distribution matching 作为条件分支：它可保留更多 mode，却增加采样、密度估计和 group construction 成本，也可能把低质量 mode 一并保留。若任务只要求一个可验证答案或目标分布不可可靠估计，reverse-KL baseline 仍更简单；coverage 下降时再启用分布匹配，并以独立 verifier 和 diversity slice 作回退 Gate。

<!-- source-family:SF-2026-ARXIV-2605-19461 -->
exact-v1 的 Method §3 只证明其 forward/group distribution-matching objective，§4–5 的实验只覆盖作者披露的模型、prompt 与偏好数据；Appendix B 的设定不能证明该分支普遍优于 reverse KL，也不能把 diversity 当作正确性。

Binary verifier 还暴露了更基础的退化：reward 只区分 valid/invalid 时，所有完全落在 valid support 上的分布都具有相同 expected reward；真正决定 valid outputs 之间相对概率的，是 base/reference distribution 与 divergence。KL-to-base 因而不只是“限制更新幅度”，还隐式选择了一个按 base mass 归一化的 filtered target。随着正则压力减弱，forward KL 可以趋近该 target；但 target 在 invalid outputs 上具有零支撑，任何 full-support autoregressive policy 对它的 reverse KL 都可能为无穷。模型族又无法精确表示 target 时，低 `beta` 压力便可能选择更容易达到的近 Dirac valid path，把“找到一个高奖励答案”误当成完整目标分布。

所以 verifier 只拥有有效性判定权，reference distribution 保留 valid support 内的相对概率先验，optimizer 只在可表示 policy family 中更新；evaluation owner 必须并列记录 validity、entropy/coverage、KL direction、model family 与 optimization path。Forward KL 或 alpha-divergence 能把 coverage 纳入目标，却需要从 filtered target 采样或近似密度，也可能保留低质量但 valid 的 modes。任务只需一个可验证答案、target 无法可靠估计或额外采样成本不可接受时，reverse-KL baseline 仍合理；只有 coverage 退化且独立 verifier/diversity slice 能稳定复现时，才启用替代分支。

`arXiv:2605.02375v1` 的 §2.3–§2.4、§3.1/§3.3–§3.4、§4.1–§4.4、§5.1 与 Appendix A–B 支持上述 binary-reward degeneracy、KL 方向与 toy n-gram 示范；它没有给出规模化 LLM RLVR 证据，也不证明真实系统必然 mode collapse，或 forward/alpha divergence 普遍优于 reverse KL。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-02375 -->

标量 reward 在偏好近似可传递时便于排序；偏好成环时，则未必存在击败所有回答的 Condorcet winner。一条受限理论分支用已知 bounded item features、skew-symmetric bilinear 参数和 symmetric differentiable link 表达 pairwise 偏好，再以 strongly-convex regularizer 定义 symmetric Nash equilibrium。其新增边界是：在该模型与 greedy NE oracle 下，沿当前 policy feature 的参数平方误差能够控制 regularized dual gap，不仅依赖 KL 特有代数；这不是 deep-network 优化或真实 rater 必然符合模型的证明。[GBPM 原条件分析](https://arxiv.org/html/2602.23116v1)的探索/regret 界仍支付 feature coverage、link curvature、维度和 regularization 费用，population NE oracle 的高效实现亦未给出。尤其单位球 feature 使 covariance trace≤1，故最小特征值 Cmin≤1/d，不能把原文“增长维度时 Cmin 常数”的说明当 dimension-free 保证。正则变弱也改变误差界；模型、覆盖或 oracle 不可用时，保留经审校的标量 reward/KL 或已验证 pairwise 分支，以实际偏好和行为回归决定采用，而非从理论低秩签发可部署效率。<!-- source-family:SF-2026-ARXIV-2602-23116 -->

## Reward hacking 与 Goodhart's Law

Reward Model 是人类偏好的有限代理。Policy optimization 比普通 evaluation 更危险，因为 policy 会针对代理的弱点搜索。

可能出现：

- 通过更长、更自信或固定格式获得高分。
- 迎合 judge wording，而不提高任务正确性。
- 利用训练 pairs 中的 spurious cues。
- 产生 Reward Model 未见过的异常输出。
- 提高 aggregate reward，却损伤特定用户群体。

所以 reward 上升必须与 independent human evaluation、task verifier、安全评估和 distribution slices 同时解释。

即使把 learned reward 换成规则明确、始终未被修改的 task verifier，代理边界也没有消失。数学 checker 可能只检查终局答案，代码测试只执行被抽取的程序；它们并不因此拥有整段生成行为的安全判定权。攻击者若能污染训练 prompt，使“先产生不允许的内容、再给正确答案”获得正 reward，而拒答因没有答案获得负 reward，policy 就可能在不改变 checker 的情况下学会奖励这种组合。这里需要区分 **checked span 的任务正确性** 与 **完整输出的行为约束**，不能由前者为未检查的前缀、工具调用或副作用背书。<!-- source-family:SF-2026-ARXIV-2604-09748 -->

因此，训练验收除了固定 verifier 的版本与输入抽取规则，还要分别测任务表现、非触发安全和触发后的行为，并控制训练数据来源及污染样本的选择方式。更完整的输出审查增加延迟、误拒与评价成本，也不能保证没有未知触发；受信数据、封闭输出格式和只需验收终值的任务，简单 checker 仍是合理基线，开放生成则应另设安全边界。受限 RLVR 后门实验支持这个输出覆盖漏洞，但经 shadow model 筛选的少量样本不等于随机污染的生产风险，部分非触发指标也退步；不得据此宣称任务效用完全不受影响或某种防御已经消除后门。

即使 checked span 的标签全对，自动奖励仍可能只鼓励实例拟合，而不是学习规则。若任务语义要求对象标识不变性，可以固定同一已生成的 hypothesis `H`，先在原实例做 extensional 验收，再将对象常量双射改名、保持其余属性与标签不变，用同一个 `H` 做 isomorphic 验收；不重新生成答案。只枚举已见对象可过第一道 checker，却可能在第二道失败。这是在比较同一规则的保义适用性，不是把“再问模型一次”当独立验证，也不能把无效变换造成的失败算作 reward hacking。

双检增加变换构造与执行成本，并要求显式冻结标识语义、checker 和实例对应关系；标识本身有任务含义、只需记忆实例或无法构造有效变换时，原实例 checker 仍合理，泛化与安全另由独立 held-out 评价承担。`arXiv:2604.15149v1` 的受限逻辑任务以同一基模两次训练、仅改变奖励，支持这个局部分支，但无重复 seeds，跨模型部分训练标签为 presumed；Table 1 部分 RLVR rows 与 GPT-5-mini-low 的零 observed shortcuts 反驳“必然捷径”，也不证明零漏洞或双检能消除全部代理失效。

<!-- source-family:SF-2026-ARXIV-2604-15149 -->

代理失效也可能始于表示接口，而不是回答语义：policy 与 Reward Model 使用不同词表时，相同数值 token ID 并不表示相同文本。若为省去 decode/re-tokenize 直接转交 IDs，甚至把越界 ID 夹到合法上界，优化器实际搜索的是另一个输入空间；可读回答与被评分序列已经失去对应关系。Reward adapter 因而要绑定两端 tokenizer、特殊 token、模板与映射策略，并对实际评分输入做一致性检查；跨词表以文本桥接为默认路径，同词表的直接路径也须验证身份，不能把 index 合法当语义有效。

这增加转换与校验成本，但阻止代理奖励为一个用户没有看到的序列背书；桥接本身仍不能消除普通 reward hacking。受限攻击实验通过两组 Llama/Qwen policy–RM 的原始 ID 映射和标量反馈，找到高奖励乱码；它证明所设接口可被利用，不证明正确重分词的生产 RLHF 必然同样失效，也不证明任务 verifier 天然不会被攻击。[表示接口攻击的机制与实验边界](https://arxiv.org/html/2604.02686v1#S3.SS2)

### Reward Hacking 也可表现为更新方向漂移

只比较 reward 与 outcome 会在故障发生后才看见 Goodhart。若正常学习在低维更新子空间中形成相对稳定方向，持续偏离该方向可以作为 hacking proposal；训练控制面可限制更新、触发复核或回退 checkpoint，但不能把几何相似直接当成价值正确。收益是增加早期信号，代价是正常能力跃迁也可能改变方向，固定 trusted direction 会阻碍探索。保守 KL、独立 evaluation 与人工检查仍是 fallback。当前证据明确是初步研究，只覆盖披露模型与任务。

<!-- source-family:SF-2026-ARXIV-2605-25189 -->

把内部 probe 当 reward 时，还须区分两条更新路径：停止 probe 的直接梯度、把其数值作为 reward 做样本 policy-gradient，与直接穿过 probe/activation 反传，并不是同一个优化器。前者没有 direct probe gradient，却仍会因 policy 参数更新而改变表示；旧 probe 分数下降可能是表示漂移，不必是相同文本已移除被测信息。可以对同一文本比较旧/新模型、旧/重新训练 probe，并独立验收行为 outcome。[Obfuscation Atlas 的有限 GRPO 对照](https://arxiv.org/html/2602.15515v1#S5)中，新 probe 能恢复读出；无直接梯度不保证不漂移，样本 GRPO 也不自动继承理想 score-function 的无偏条件。较高 KL、长度奖励与过强 probe 系数退化是局部反侧，重新训练/校准 probe 和额外调用均付费。因此 probe/reward、policy revision、梯度路径与预算要共同冻结；表示或人口变化时重校准并保留独立评价/KL回退，不把 sensor 低分当通用 honesty 或安全证书。<!-- source-family:SF-2026-ARXIV-2602-15515 -->

Pass@k 目标也不等于在同一数据人口上放大 Pass@1。在固定 binary verifier、每题 iid 采样且单次成功概率为 `pθ(x)` 时，population 目标为 `E[1−(1−pθ(x))^k]`；其梯度给每题的 `∇pθ(x)` 乘以非负权重 `k(1−pθ(x))^(k−1)`。同题方向未反转，但跨题合成更偏重低成功率题。能否损伤 Pass@1 还取决于各题梯度与总 Pass@1 梯度的 agreement：只有重权后的平均 agreement 为负，才有局部方向冲突；“hard prompts 更多”本身不够。

[有限 Pass@k 对照](https://arxiv.org/html/2602.21189v1)的诊断梯度对象是最终 hidden-layer state 的 Monte Carlo 估计，不是实际全参数 RL 更新；它不认证任意训练都会降低 Pass@1。原部分 corollary 的符号与严格步长端点未闭合，本段不采用其阈值或更新 recipe。应共同冻结 prompt population、verifier、k、sampling/optimizer 身份，并分别验收单次与多次成功率、额外 rollout/梯度费用和有效 mode 保持。Agreement 不稳、真实更新未获验证或单次质量退步时保留固定训练目标与独立多预算评价；下述 majority vote 仍可作为不改变 policy 的 baseline。<!-- source-family:SF-2026-ARXIV-2602-21189 -->

多预算曲线仍不能区分“已有单步操作更容易被串起来”与“每个操作本身得到改善”。可在同一任务 oracle 下分别保留 atomic tasks 与它们的 held-out compositions，再在组合轨迹中提供正确前缀，测下一步操作的条件成功率；这条 teacher-forced 诊断排除了前序错误传播，却不等于自由 rollout 的链可靠性。无条件逐步率相乘需要独立性，完整链通常需要逐步条件概率。[受限 RLVR 训练对照](https://arxiv.org/html/2602.08281v1#S6)中，组合成功可以与原子任务退步并存，因此训练后应联合检查两个人口、完整 rollout 与多预算曲线，而不从相关图或128次零命中判定内部新技能或成功概率零。构造 oracle、分步重测和更多采样都增加费用；操作无法独立验算、前缀干预改变任务或质量回归时，保留原任务结果、单/多次采样评价与可靠 checkpoint，不把分解诊断替代最终能力验收。<!-- source-family:SF-2026-ARXIV-2602-08281 -->

### Majority Vote 可能只是在压尖已有分布

多数采样后投票在答案可离散比较时是低成本 baseline，但 pass@k 上升可能来自已有正确 mode 被更频繁抽中，而不是 policy 学到新能力。训练 owner 应把迁移结果拆成 `capability expansion`、`distribution sharpening` 与 `mode extinction`；当重复自训练开始消灭少数但有效的轨迹时，TTRL-style guard 可以冻结或降权高灭绝风险更新。收益是避免把表面成功率误读成能力增长，代价是额外 rollout、mode tracking 和 guard threshold；短任务、单一可验证答案或分布稳定时，普通 majority vote 仍成立。

<!-- source-family:SF-2026-ARXIV-2605-19444 -->
exact-v1 §2–3 给出 extinction 诊断与 TTRL-Guard，§4 的结果只属于论文实验，§6 明确留下任务广度与极端 sampling regime；它没有证明所有 majority-vote gain 都是 sharpening。

一次 rollout 投票只反映当前 checkpoint 的采样状态；在同一 preference pair 被反复访问的自训练中，可以为该 pair 保存历轮 pseudo-label，把历史平均与当前多次偏好输出共同构造下一轮目标，再奖励与目标一致的判断。历史在这里改变的是训练 target，而非仅复用生成经验或累计 reward。若两项恰好抵消，目标为零并跳过相应判断奖励；这只是所定义 sign 聚合的零点，不是自动校准的“所有低置信样本”检测器。<!-- source-family:SF-2026-ARXIV-2604-07484 -->

额外的 critique 相似度奖励还可只作用于已经匹配目标的输出，但历史共识与文本相似都可能稳定一个共同错误。训练必须保留 pair identity、history 和模型版本、初始化/聚合规则，并用独立偏好与任务切片检查漂移；历史平均会带来缓冲成本和响应变慢，不能获得事实 authority。受限 GRM 实验同时涉及当前投票、历史目标和 critique 奖励，部分 benchmark 退步；训练集筛选也使用了既有 ground-truth 标签，因此不能把“不新增人工 reward 标注”写成全流程不依赖外部真值。历史失配或自我确认上升时，回退当前投票、冻结 RM 或可信偏好监督，而非无条件延长记忆。

### 部署给出 K 个候选时，训练目标也可能依赖 K

单回答的 population-preference 最优解，不一定适合“用户从 `k` 个独立候选中选最喜欢的一项”。受限理论允许为每个 `k` 训练不同的单输出 policy，再从**同一 policy** iid 抽取 `k` 个回答；在有限 prompt/response 空间及满足论文 Property1 的偏好法则下，可以让其集合击败任意单输出对手的 population win probability 至少为 `k/(k+1)`。[Asymptotic Universal Alignment 的边界](https://arxiv.org/html/2601.08777v1)由此改变的是训练目标与部署候选数的配对，不是把固定 checkpoint 多采几次就获得通用保证。NLHF 的多数偏好可能收缩成确定性输出，重复采样也无法凭空恢复多样性；用户偏好胜率更不等于事实正确性或一个会选错的自动 selector 的正确率。<!-- source-family:SF-2026-ARXIV-2601-08777 -->

对应的 no-regret 构造先抽取一个历史 iterate `t`，再从该 iterate 抽 `k` 个样本，而非分别从平均 policy 独立抽取；保存训练历史与额外候选都有成本。理论中的 simplex-gradient fixed point 也不证明 LLM 参数训练会收敛。人口偏好不满足假设、回答空间开放、候选高度相关或 selector 资格未验时，保留单输出偏好训练与独立的候选质量/选择评价，不把有限理论当生产对齐证书。部署 mode coverage 与历史目标仍各有自己的诊断，下一节的 sequence-to-token credit 同样不能由集合偏好定理代办。

## Sequence reward 与 token updates 的错位

### Training–Inference Mismatch 也可能来自 Numerical Execution Identity

<!-- semantic-body-binding:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:start -->
RL pipeline 常把 rollout engine 与 training forward 当作“同一 policy”，但 kernel、precision、sampling/logprob 实现的细小差异会让 importance ratio 和 advantage 归因偏离，即使 checkpoint 名称相同。Run identity 必须绑定两侧执行图、数值策略、tokenization 和 logprob contract，并用 zero-mismatch diagnostic 先隔离数值分歧，再讨论 stale policy 或算法。追求 bitwise 对齐会牺牲 kernel 自由和吞吐；允许误差则必须有界并监测累积。作者 collapse 结果只属于其配置，不说明所有 RL 失败都来自数值 mismatch。
<!-- semantic-body-binding:SF-DIAGNOSING-TRAINING-INFERENCE-MISMATCH-IN-LLM-REINFORCEMENT-LEARNING:end -->

Reward Model 常在完整 response 结束后给一个 scalar，但 policy 是逐 token 生成：

```text
y = (y_1,...,y_T)
r = r_phi(x,y)
```

训练需要把 sequence-level outcome 转成各 token action 的更新信号。PPO 通过 return、value estimate 和 advantage 处理 credit assignment；GRPO 用同一 prompt 下组内 rewards 构造相对 advantage。

Reward Model score 本身没有告诉系统哪个 token 导致好坏。长序列、稀疏 reward 和延迟反馈会增加方差。

多 Agent 训练的个体 credit 还存在两种不同缺失：competition routing 只观察被选提案的反馈，需要选择 propensity 与未选 outcome model；collaboration 得到共同 reward，却缺少替换某个 Agent 提案后的 counterfactual effect。不能把 selected reward 或 shared reward 直接复制为每个 Agent 的训练标签；后续重采样也应保留候选与选择 lineage。<!-- source-family:SF-2026-ARXIV-2604-22785 -->

DR 校正依赖 positivity，以及 propensity 或 outcome model 至少一侧正确等条件，不覆盖联合误设；协作归因还增加替代提案与环境评价成本。作者只在单轮、小数据、单 seed routing 试验验证收益，未验证协作通用效果。支持不足或 counterfactual 不可核时，回退 set-level outcome、独立监督或保守 credit，不把估计 credit 当环境真值。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-24517:start -->
在 agent rollout 中只对 action token 使用 task reward，能保持 policy objective 清晰，却把 environment 返回的 observation 当作不可学习的只读 context；当终局 verifier 稀疏时，这会丢掉一条密集信号。受限分支可增加对下一段 observation token 的辅助预测目标：environment 仍拥有真实 transition，task verifier 仍拥有成功判定，world-model loss 只帮助 representation 学习 action-conditioned dynamics，不能替代 policy gradient 或把预测 observation 当成真实执行结果。

辅助目标提供更密集的学习信号，也可能奖励“容易预测”而非“有助于控制”的环境，或让 observation loss 压过 action objective。训练 artifact 因此要绑定两类 token mask、loss weight、environment revision 与 held-out dynamics/task gates；任务成功、校准或 action quality 下降时，应减小或移除辅助项并回退标准 GRPO/PPO。现有证据只支持论文披露的 terminal-agent objective、TerminalBench 与实验，不能证明 observation prediction 在任意工具环境都免费改善控制。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-24517:end -->
<!-- source-family:SF-2026-ARXIV-2605-24517 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21654:start -->
Critic-free actor update 也不等于完全没有 value-like temporal signal。对连续可微、additive-noise rollout，actor
backward 的 hidden-state sensitivity 可解释为 empirical costate，其条件期望在论文假设下对应 value gradient；
离散 Transformer 只沿 attention path 近似传播，token sampling path 缺失，误差还受 entropy 与 sampling gap 影响。
Reward/verifier 拥有 outcome，autodiff 只提出 credit，optimizer 才提交更新。该诊断需要 hidden gradients 与 matched
rollout，并存在低熵减小近似误差却损伤探索的张力；假设或预测不成立时，应回退标准 score-function/advantage、
process reward、显式 critic 或 held-out checkpoint sweep。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21654:end -->

### Harm Horizon：Sequence Reward 的 Gradient 可能天然局部

把一个 sequence-level harm score 分配给整条 response，看似让所有 token 都收到安全信号；但 policy gradient 只会
沿“当前 token 改变未来期望 harm”的条件依赖传播。若在某个位置之后，继续生成已不能改变终局 harm 的条件期望，
这些 token 的期望 gradient 就会消失。因而浅层 alignment 不一定只是优化器或数据不足，也可能来自 objective 定义
出的 **harm horizon**。

Martingale decomposition 可以把逐前缀的条件期望 harm 写成一系列 innovation，再由 gradient characterization 识别
哪些位置真正携带 harm information。这提供了一种诊断顺序：先检查 harm function、prefix state 与可恢复路径是否让
后续 action 仍能改变 outcome，再讨论增加样本、调学习率或扩大 KL penalty。若希望错误出现后仍奖励恢复行为，objective
必须显式定义 recovery event 与 penalty，而不能期待同一个终局标量自动产生深层 credit。

```text
prefix-conditioned expected harm
-> per-token harm innovation
-> gradient support / harm horizon
-> optional recovery-aware objective
```

这种分析换来更清楚的 credit boundary，却依赖 harm 定义、模型参数化和论文中的正则条件；共享参数还会造成跨位置
耦合，理论上的零梯度不等于实际训练中所有相关参数完全不动。Recovery penalty 也可能诱导表面纠错、拖长有害轨迹，
或与终止策略冲突。终局 outcome 已充分表达任务、错误不可恢复或 hard safety gate 必须立即阻断时，原 sequence reward
仍是合理 baseline。现有证据以理论刻画和补充证明为主，不证明任意 RLHF pipeline 都存在同一 horizon，或提出的恢复
目标已经解决部署安全。

<!-- source-family:SF-2026-ARXIV-2603-04851 -->

### 从持久权重更新到条件化 Activation Intervention

持久权重的更新也可缩到跨语言的局部接口，而非直接放大同一 activation：由 harmful/harmless probe 选择稀疏 MLP 位置，在低资源语言输入上拟合目标 anchor，同时对 safe-input 响应加入软平方 penalty 与 regularizer；对该线性二次目标白化、截断 SVD 再反白化，得到低秩更新。[受限跨语分支](https://arxiv.org/html/2602.22554v1)解的是这个线性 surrogate，不是整个非线性模型的 safety 优化；post-activation target 与 pre-activation 线性代理不能忽略激活导数而宣称精确，utility penalty 更不是 hard nullspace 保证。稀疏定位、English anchor 和翻译人口都是假设/校准选择，Jaccard 重叠不认证普适因果 safety basis。所测语言有 unsafe 数增多，模型 utility 也会退，单独 anchor/regularizer 与组合的反侧须一起看。捕获、求解、merge 与跨语审校均有成本，翻译器和同一 Guard judge 的标签不等独立安全真值；改变 weights 后须重做语言/utility/攻击切片验收，失配时保留原 safety training、小幅可撤销 steering 或关闭更新，不由“training-free”误称权重未变或安全无损。<!-- source-family:SF-2026-ARXIV-2602-22554 -->

RLHF/DPO 把偏好持久写入 weights，适合需要稳定行为变化的部署；dense representation steering 或 static
SAE direction 则更易撤销，却容易对所有 prompt 和 token 使用同一方向。当偏好只在某类输入 feature 与
当前激活状态下相关时，可以把控制再拆成两层：offline 从 preference triples 建立 prompt-feature 到
output-feature 的稀疏 conditional map，runtime 只对当前 prompt 选中的、且当前 token 已激活的 residual
features 做有界修改。

```text
preference data + input/output feature dictionaries
→ versioned sparse conditional map
→ prompt gate
→ token-active residual intervention
→ unchanged base weights
```

它换来可撤销、较轻的行为控制，也新增双 SAE 与 map 的版本耦合、每 token encode/edit/decode、rare-gate
噪声、feature co-activation 污染和 bypass surface。Feature label 不是因果语义，judge preference 也可能只
奖励 style。没有稳定 feature basis、需要持久 alignment 或 runtime overhead 敏感时，权重更新仍合理；这类
intervention 只能是 policy 下的 actuator，不能替代 safety training、access control 或独立 Evaluation。

运行时activation干预还要先检查偏好方向与其他特征的几何关系。若一个宏方向同时承载activation norm或无关概念，沿它加减可能混合目标与副作用；可分离时，宏方向反而能比稀疏微方向更完整地改变目标。条件分支因此先比较宏方向与SAE微特征的可分离性，再在同一问卷/输出合同下分别验收行为变化和原能力，不把“稀疏”当作一律更安全。probe的可读出性不等干预因果，干预改变回答也不等真实道德属性得到认证。<!-- source-family:SF-2026-ARXIV-2601-05437 -->

[两英语7–8B模型的受限观察](https://arxiv.org/html/2601.05437v1)中，norm纠缠的模型微方向更有效，可分离的模型宏方向更强；base与aligned差异未单独隔离，不能唯一归因于RLHF。微干预的MMLU下降达4.3/4.9点，与“无显著能力损失”的宣传并列保留；additive公式、clamp叙述及剂量描述也不能拼成已验证的执行配方。该路线新增SAE/方向校准与副作用评价成本，不授生产安全、refusal或跨文化保证；geometry不清、能力回归或剂量身份不稳时，保留冻结权重偏好、保守宏干预与独立guardrail。

在部署这个 actuator 之前，还要区分“某个特征可被 probe 读出”和“沿模型自己的输出通道推动该特征能改变答案”。中间层的任意线性分类器可能已能区分目标，但同一层的 residual state 经最终 normalization 与 unembedding 后未必把目标 token 排到前面；沿均值差方向加激活，也未必经过后续层仍朝目标输出移动。因而选层不能只凭 probe accuracy 或“取中间层”的习惯：在冻结模型、tokenizer、目标概念和具体干预方向后，可比较逐层输出投影、实际注入后的目标概率变化及非目标行为回归，再为该版本选择有界层和幅度。前者只是候选 sensor，后两者才是干预效果与副作用证据。<!-- source-family:SF-2026-ARXIV-2604-15557 -->

输出对齐诊断省去盲目尝试全部层，却依赖目标 token 的定义与该模型的输出 head；单 token 题上的相关性不是多 token 概念、未知输入或生产安全的因果保证。Probe 可读而干预无效时应回退另选层/方向、训练可用 actuator，或直接采用权重级后训练；目标分布漂移、非目标能力受损或没有独立行为 Gate 时不能让诊断器自行拥有发布权。这样也保留了早层表征可能“有信息但尚未按输出方向表达”的解释，而不把低 logit-lens 分数误写成模型完全不知道该概念。

实际注入有效之后，还要把三种行为性质分账：目标效果、与目标相关但应保持的控制性质，以及同一控制性质在输入分布变化后的保持。例如减少无害问题的过度拒绝，不应同时增加有害问题的服从；在普通有害问题上仍能拒绝，也不证明附加误导前缀后仍能拒绝。无关知识或流畅度回归是另一条检查轴，不能替代这种相关控制测试；目标效果能迁移到新输入，同样不认证相关控制在新输入上保持。方向、层、幅度与选择所用的验证人口应冻结，再对每一性质分别比较未干预基线。<!-- source-family:SF-2026-ARXIV-2602-06256 -->

这会增加相关控制、分布变化与judge校准的评价成本，也可能暴露同一方向在不同性质之间的冲突。[有限英语模型与静态前缀对照](https://arxiv.org/html/2602.06256v1)支持“ID控制保留不等于OOD控制保留”这一验收边界，不证明所有干预必然失败、局部激活投影具有唯一因果解释或覆盖了开放攻击。控制切片退步、judge失配或没有预算验证变化后输入时，应限制幅度或关闭该干预，必要时回到权重级后训练与独立安全评价；可撤销只是控制方式，不是行为安全证书。

选定干预方向仍不等于选定施加量：同一前向内，当前层的 feature error 会经后续层传播，使一次性的静态 steering 在不同激活状态下偏离目标。另一条可撤销路径是在代表激活附近离线估计按层传输的局部 Jacobian，为指定 feature、setpoint 与控制代价求固定的 Riccati gain；runtime 读取当前层 feature error，再施加对应反馈，base weights 不变。这里的控制 horizon 是网络层深，不是对未来自回归 token 内容的最优规划；离线模型、feature basis、setpoint 和 gain 必须作为同一版本化 actuator 验收，也不取得 safety policy authority。

固定 gain 避免逐 token 重解控制问题，却引入离线线性化与校准、gain 驻留、每 token 额外计算及局部模型漂移的代价。Feature setpoint 并非语义真值，局部 remainder 条件也不能认证开放输入；受测 toxicity 改善须与 PPL、MMLU、throughput 和未知触发器回归同看，作者 Gemma 切片的 PPL 就从 8.95 升到 12.26。离开已校准的激活区域或不能承担在线成本时，回退小幅静态 steering 或权重级后训练，并由独立行为 Gate 决定是否采用，而不是把反馈器当通用安全保证。

<!-- source-family:SF-2026-ARXIV-2604-19018 -->

即使单个 feature intervention 可解释，多个方向也不能默认线性叠加。稀疏字典中的 feature 往往非正交，ReLU 截断又会让连续 steering 沿锥边界积累；分别有效的方向共同施加时，可能出现目标相互抵消、无关 feature 被激活或更新幅度的单向 ratchet。组合控制因此要把 feature set、系数、顺序与 residual checkpoint 作为一个整体 artifact，先做 joint intervention 与未目标行为回归，再决定是否提升为 runtime policy。它用更细的可撤销控制换组合搜索、共激活污染和字典漂移；组合证据不足时回退单方向、较小幅度或权重级后训练。exact-v1 的理论使用随机过完备字典，实验使用 CLEVR 结构化语义 feature；它不证明 SAE 坐标是普适因果 basis，也不证明真实偏好空间遵循同一坍塌阈值。

<!-- source-family:SF-2026-ARXIV-2605-05223 -->

### Reward Model 也有 Policy-relative State

排序正确率把偏好对等权计数，policy-gradient 实际消费的却是相对当前策略期望的奖励优势，并受答案生成概率影响。在一个受限 softmax 坐标模型中，更新含 `pi(y)·[r_proxy(y)−E_pi r_proxy]`：错排的 rejected 若仍低于当前代理奖励均值，未必吸引更新；较常见的中等质量答案若获得略高于均值的奖励，却可能先吸走概率，使稀有最优答案更难被探索。选择 RM 时因此应冻结初始 policy 与候选分布，并列 pairwise accuracy、按当前 policy 估计的 harm-aware 错误切片和独立后训 outcome，不能用一个模型无关排行榜代替训练验收。

这种分账增加 on-policy 采样、likelihood 和独立 outcome 成本；它不是鼓励故意错奖的配方。[原始研究](https://arxiv.org/pdf/2604.25872v1)的停滞定理依赖线性 softmax、正交特征与 exact-gradient flow，正内积特征还可改变结论方向；四个小 policy 上 HAcc 与后训收益的相关仍弱、部分为负，主实验所谓真值又是另一 RM 的代理而非人类效用。无法取得独立 outcome 或分布不稳定时，pairwise ranking 仍是廉价筛选，只能报告该偏好集上的拟合，不能取得安全或真实效用 authority。<!-- source-family:SF-2026-ARXIV-2604-25872 -->

固定 scalar 或 rubric 还会在 policy 分布改变后失效。把 criteria 表为版本化 Reward DAG，允许设计器依据 on-policy response 与 node-level trace 提出节点/边更新，可以定位 coverage 与 reliability 的变化；但设计器不是 truth owner，自演化也会制造新的 reward hacking。任何 graph mutation 都必须经过 held-out、人类或确定性 verifier 的 promotion gate，并保留旧 rubric 作为可回滚基线。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08703:start -->
开放式任务还可能要求 reward contract 随失败证据演进。冻结 Reward Model 在目标稳定时最易校准；当视觉编辑等任务不断暴露新的判据和工具缺口时，orchestrator 可以依据失败轨迹提出 skill/tool library 与验证 rubric 的版本变更，但 subagent 只执行冻结版本，独立 validation Gate 才拥有提交权。这样把“自我改进”拆成 proposal、execution 和 promotion 三种责任，避免同一个模型既生成规则又宣布自己通过。

自演化 reward path 会引入同源自评、library 膨胀、小验证集过拟合和版本漂移；当前证据还依赖专有 orchestrator、单一图像编辑领域与有限 validation。无法提供独立 held-out evidence、工具身份不稳定或更新频率低时，应回退冻结 Reward Model、人工 rubric 和阶段性离线更新。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-08703:end -->

<!-- source-family:SF-2026-ARXIV-2609-12459 -->

冻结 RM 把 reward interface 固定下来，最容易部署和复现；policy 持续更新后却可能进入 RM 未覆盖的
representation region。周期性全量 retraining 能跟随 drift，但成本高且同时移动 feature space。一条实验性
中间分支冻结 RM backbone，只让 policy hidden state 经 cross-attention 影响 reward head，并随 policy step
更新小型 head：

```text
trajectory + policy representation/version
→ frozen semantic RM backbone
→ policy-conditioned reward head
→ reward + RM-head version
```

这把 reward 从无状态 scalar service 变成与 policy coordinate 绑定的 measurement state，新增 hidden-space
compatibility、representation privacy、version skew 和 policy/RM co-adaptation。冻结 RM 在 auditability、
低频 policy 更新或跨模型复用优先时仍合理；只有 drift 能被独立评估、head update 有 held-out gate 时才值得
动态追踪。作者 benchmark 不能证明 co-adaptation 已消除 reward hacking。

### 多轮 Credit 不能让 Prefix 污染当前 Action

只给完整 trajectory 一个 outcome reward，成本低且不依赖逐步 judge，但长链中很难分辨当前 action 与既有 prefix 各自承担多少责任；对每一步调用外部 judge 又会显著增加成本。prefix-aware internal reward 把 prefix state 与当前 action 的贡献分开，为多轮优化提供更密的 credit，同时保持最终 objective 的 authority 不变。

这种分解换来更低方差的局部信号，也引入 reward-model 偏差、intervention 成本和错误归因；内部 reward 不能取代最终任务成功率与安全 gate。短任务、可验证终局或缺少可靠 prefix intervention 时，outcome reward 仍是稳健基线。exact-v1 只支持其披露的 agent tasks、模型、reward construction 与 ablation，不证明内部 reward 在开放工作流中忠实代表因果贡献。

<!-- source-family:SF-2026-ARXIV-2605-17877 -->

### 反馈预算必须绑定样本粒度与可观测不确定性

对每条 trajectory 都请求同等反馈，最易复现且不依赖 selector；反馈昂贵或环境长尾后，平均分配会把预算浪费在已确定样本上。选择性反馈把 trajectory-level uncertainty、状态覆盖和 verifier availability 交给 acquisition owner，只有高信息样本进入人类或高成本 judge；收益是提高单位反馈的信息量，代价是 selector bias、未知未知与覆盖盲区。必须保留随机 audit slice 与 coverage floor；无法校准不确定性时回退均匀采样。

<!-- source-family:SF-2026-ARXIV-2605-19447 -->
exact-v1 §3 描述 selective-feedback 机制，§4 只在 ALFWorld/WebShop 验证，Appendix C 的条件不支持开放域长期工作流外推。

选择器也可以控制合成监督的位置，而不直接查询更多人类标签：每轮用当前 Reward Model 的 chosen/rejected margin，把固定增广预算更多分配给绝对 margin 小的原偏好对，再改写两侧文本并保留原对训练下一轮。[margin-aware 增广](https://arxiv.org/html/2602.17658v1)中的新 pair 继承原排序假设，不因此成为新增人类 truth；大幅错排的负 margin 也可能因绝对值大而被少选。在线性 Bradley–Terry 分析中，小 margin 只增大 logistic 曲率标量，还需增广 feature covariance 在原任务各方向有支撑、两分布 margin 分离及相应系数条件，才能得到平均 Hessian 的 PSD 下界；这不证明 condition number 改善、任意神经 RM 更稳或覆盖所有困难样本。DeBERTa-v3、T5 改写与小型 policy/judge 的有限对照没有独立验证所有改写的偏好保真，PKU test 不可用时退用 train 的设置还限制泛化评价。逐轮评分、生成和重训另付费用，匹配 epoch/学习率不等总生成 token 或墙钟等预算。方向支持、标签保真或预算不可靠时，保留原人类偏好对、均匀增广/随机 audit 与独立 held-out 评价，不让 synthetic margin 给下游 policy 自授质量或安全。<!-- source-family:SF-2026-ARXIV-2602-17658 -->

进一步地，多轮任务不能只保存一个 scalar reward。若更新依赖不可见的中间判断，credit owner 应维护显式 belief state，记录每一步可观察证据、belief revision 与最终 outcome，使 reward 能回溯到改变决策的 evidence。它改善长程 credit，却新增 belief model 偏差、状态膨胀与错误归因；终局可直接验证的短任务仍应使用简单 outcome reward。

<!-- source-family:SF-2026-ARXIV-2605-20061 -->
exact-v1 §3 给出 belief-based credit，§4 与 Appendix C 只证明作者环境中的归因改善，不证明 belief state 等于真实因果状态。

#### 优化单元必须匹配可观测 Outcome 的粒度

逐候选反馈只有在每个候选都被独立展示并产生 outcome 时才成立。若系统先生成一组候选、再由 filter/ranker 只曝光其中一部分，未曝光项没有可观察结果；为它们补 item-level 正负标签会把选择偏差伪装成监督。更诚实的更新单元是绑定 generator、filter/ranker、exposure log 与 outcome window 的完整候选集合，并且只在集合中至少一项真实曝光后，才消费 set-level outcome。Generator 提出集合，ranker 决定曝光，日志系统拥有 exposure/click 事实，learner 只能在这个可观测边界内更新；click 仍不拥有质量、安全或 release 判断。

Set-level feedback 避免伪造隐藏标签，却牺牲集合内部 attribution，并可能继承 ranker bias、位置效应和活跃用户偏差。Rolling-window 更新能追踪近期行为，也会增加 policy-ranker co-adaptation、版本漂移与反馈回路；因此 identity 还要保存 serialized set、exposure/ranker revision、权重策略和窗口。若每项都有独立 outcome，回退 item-level supervision 更精确；若曝光事实也不完整，则应拒绝更新而不是制造标签。exact-v1 的生产 A/B 只证明该机制在作者 assistant 流量和 click proxy 下可运行，不证明 click 等于长期效用，或选择偏差已经消除。

<!-- source-family:SF-2026-ARXIV-2609-11953 -->

### Weak-to-Strong 不能只用 Capacity Mismatch 解释

较强 student 从较弱 teacher 的反馈中超过 teacher，常被解释为 student capacity 足以恢复 teacher 没有表达的知识。这个解释可能成立，却不是必要条件：在线性 logistic regression 与 approximate ellipticity 等明确假设下，weak-to-strong 可以在较广的 student-teacher 组合中出现，并不要求 capacity mismatch。<!-- semantic-body-binding:SF-2026-ARXIV-2605-05742 -->

这只是对“必要机制”的反证，不是 frontier LLM、非凸训练或任意 noisy feedback 的工程保证。生产后训练仍需用 held-out capability、teacher error slices 和 policy-relative evaluation 验收，不能因为理论可行就降低反馈质量 Gate。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12908:start -->
一个并列的 feature-level 机制给出更具体、但也更窄的解释：在两层 reward model、pretraining task subspace 与 localization 等假设下，weak-label fine-tuning 的多步 SGD 可能逐步 elicitate 已存在的 latent target feature，同时近似保留 off-target pretrained features。弱监督此时改变的是可读出的方向，而不是从零创造能力；weak supervisor 仍不拥有 truth authority。

这项理论没有分析 second-layer learning，只证明 feature alignment 而不是完整 function approximation，并依赖具体算法、even link 与合成 geometry。假设不能确认时，仍须用真实模型、held-out capability、teacher-error slices 与 policy-relative evaluation；不得以“可能 elicitate latent knowledge”为理由降低反馈质量 Gate。exact-v1 的证据限合成设置 `d=1024, s=128, K=2` 及披露的 learning-rate sweep，不是 frontier LLM 的经验结果。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12908:end -->

弱标签不只有一个平均错误率。若错误随输入和 teacher/student 的分歧变化，直接拟合弱标签或只筛选高置信样本，会把不同错误结构压成同一种监督。一个条件分支从冻结强模型的多种提示模板及正反排列提取 logit margin，把弱模型置信度、margin 的均值与稳定性、双方是否同意作为特征，拟合实例相关的 noisy channel。这里的候选真标签是隐变量：以强模型 margin 导出的 prior 乘以 channel 对观测弱标签的 likelihood，再归一化并调节 posterior 的锐度，得到训练用 soft labels；随后交替训练 student、用其预测重新估计 channel，再更新 posterior。来源只执行两轮这种 EM 式细化，channel 留在训练期，部署时仍是 student 的普通 forward。它与前述 capacity 或 latent-feature 理论是并列的监督构造方案，不是对那些理论的替代证明。

这条分支增加了多模板推理、channel 拟合和重复 fine-tuning 的成本，也把 prior、噪声模型与 student 的相关误差耦合起来；posterior 不是可识别真标签的保证，模型彼此一致也可能共同出错。证据限于 Qwen1.5-0.5B-Chat 监督 Qwen3-4B-Base 的二元偏好、数学及代码验证设置，其中跨任务迁移仍依赖强模型能否提供有用信号。迁到 Sonnet 4.0 生产偏好数据时，强模型的单 token 强制选择 margin 太弱，最好配置的微小提升仍在测量噪声范围内。因此工程上应分别检查 prior 的辨别力、teacher-error slices 与独立 held-out 结果；这些条件不成立时，回退直接弱标签训练、可靠标签筛选或更高质量监督，比反复自举一个失真的 posterior 更稳妥。这一回退建议是设计判断，不是作者已经验证的通用防御。

<!-- source-family:SF-2026-ANTHROPIC-AUTOMATED-W2S-RESEARCHER -->

### 从二元偏好到分布条件化的连续 Reward

Pairwise preference 保留了相对判断，却丢掉“胜得多明显”的强度信息；单独训练 reward model 又引入新的模型与漂移状态。一个中间分支是先从 arena comparison 拟合模型 capability distributions，再结合分布和胜负推断 latent quality gap，把 binary verdict 转成连续 offline reward。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06070 -->

latent gap 仍不是绝对质量真值，它依赖 capability 分布假设、pairwise 样本选择和任务域。分布拟合不稳定、arena selection bias 较大或跨域失效时，应回退二元偏好、显式 reward model 或人工标注。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20740:start -->
若同一输入会产生多条连续值 rollout，单点 reward 还会丢掉整组预测分布的 spread 与 calibration。一个条件分支用
CRPS 评价整组样本，再以 leave-one-out marginal contribution 把 group score 分配回每条 rollout；reward 因而同时
约束点误差、分布宽度和相对 credit，而不是把每个样本当成彼此独立的标量答案。

这种分布 reward 用 `K` 次 rollout、组内耦合、数值解析和更高方差换取不确定性表达；少样本 CRPS 或 reward noise
会使 marginal credit 不稳定。分布校准失败、解析不可靠或 rollout 成本超限时，应回退 pointwise reward/SFT，并把
calibration 留给独立 release Gate。exact-v1 只支持 Gaussian mixture、代码性能与 MoleculeNet 等披露任务，不证明
分布 reward 在开放式 LLM 输出上天然等于真实 outcome quality。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20740:end -->

离散决策还要区分“从已有 reasoning trace 读出某个标签的概率”与“这个标签正确的概率”。如果 trace 已强烈指向一个结论，最后 decision token 即使读出得近乎确定，也可能只是忠实提取错误结论；给整条 rollout 正误 reward 并不自动校准这个读出。一条受限训练分支将 decision token 的 GRPO advantage 置零，让其余 tokens 继续接受轨迹 reward，再对 decision token 加交叉熵：正确 rollout 使用 one-hot 标签，错误 rollout 向候选标签的 uniform target 调整。这样把轨迹学习与决策校准的监督权限分开，但 uniform 化可能改变 greedy 选择，不能保证原决策或 reasoning—label 一致性不变。

[校准训练的有限对照](https://arxiv.org/html/2601.13284v1#S5)在三个 Qwen3 规模、每项任务500训练样本及固定辅助权重下支持这种取舍；分类 accuracy 与校准误差必须分别检查，部分配置准确率退步，也没有证明所有 RLVR 都无法校准。所报 equal-count bin 指标依赖分箱与评价人口，OOD 两套数据不能代替任意部署漂移；额外 token 标签、辅助 loss 与校准回归均有成本。标签、候选集合或校准分布不可信时，保留原 SFT/RLVR、独立 held-out 校准和拒绝/人工路径，不由最后 token 的高概率签发 correctness 或上线信心保证。<!-- source-family:SF-2026-ARXIV-2601-13284 -->

### Outcome 相同也可能走了错误 Trace

只奖励终局 outcome 在可观测状态充分时简单有效；在 POMDP 中，不同 action trace 可能得到近似相同结果，其中一条却利用了 shortcut。可以把 lagged traces 学成 distributional prior，再用 task reward 与 KL 共同约束 stochastic policy，使优化对象同时包含结果和行为分布。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06529 -->

这个修复把 prior 质量和 state observability 变成新的故障面。现有证据限于 two-hotel simulator、固定竞争者和给定 prior，不能外推到开放 Agent 或任意安全对齐任务。先验失真、环境漂移或 trace 不可观测时，应回退 outcome reward 加独立 trace audit、显式 state estimator 或人工 policy。

## RLHF 的系统成本

训练成本不只由同时驻留的模型决定，也由各阶段允许更新哪些参数决定。普通 RL 从 SFT checkpoint 直接更新整个 policy，适合不清楚哪组参数先适应、或额外 warmup 得不偿失的情况。一条替代分支先冻结特征提取器，仅对 unembedding classifier 做 reward-grounded 更新，再恢复全参 RL；它改变的是进入完整更新时的输出接口，而不是用 classifier-only 永久替代表示学习。受限实验中，初段单独 reward 改善很小，后段曲线才出现增益；不能把参数变化较快解释成某一组参数拥有全部能力，也不能把局部 NTK 分解当实际 Adam/GRPO 的全程保证。

这条分支增加一个 classifier epoch、阶段边界与优化器状态管理。Pythia-2.8B、AlpacaFarm/UltraFeedback、固定 ArmoRM 的三次训练没有证明端到端成本更低、特征变化更小或所有模型多样性更好；ArmoRM 的评分也不是人类价值真值。应分别验 warmup 费用、后段收益和独立能力回退，无净收益时保留从原 SFT checkpoint 直接全参更新。来源的一般 KL 推导存在 log-ratio 表达冲突，本节只采用分阶段参数权限和受限经验结果，不用争议公式替这条分支担保。<!-- source-family:SF-2026-ARXIV-2601-04670 -->

一轮 PPO-style RLHF 可能同时需要：

- Actor/policy forward 与 backward。
- Reference policy forward。
- Reward Model forward。
- Value/critic forward 与 backward。
- Autoregressive rollout generation。
- Variable-length sequence storage 与 masks。

Rollout 不像 Pretraining teacher forcing 那样能并行知道未来 tokens。它需要真实 Decode，因此 generation throughput、KV Cache 和 Sampling policy 会直接影响训练吞吐。

训练系统还要维持 prompt、response、old log probabilities、reward、value、advantage、policy version 与 checkpoint 的一致性。Stale rollouts 会让 on-policy assumption 逐步失效。

模型与 rollout runtime 扩展后，还会出现一个更隐蔽的不一致：训练端与生成端虽然加载“同一 checkpoint”，
却可能因 kernel、precision、并行切分、长 Context communication 或 log-probability 重算路径不同而产生数值漂移。
小规模单 runtime 中直接复用 rollout probability 最简单；分离 inference / training engines 后，update contract
必须把 tokenizer、precision、parallel layout、ratio source 与 KL 计算版本一并冻结，并在必要时以训练端重新计算
或有界校正 ratio：

```text
rollout policy identity
+ inference numerical path
+ training recomputation path
→ ratio / KL consistency check
→ accept, correct or reject trajectory
```

这用额外通信、重算和校准换取更大规模 RL 的更新稳定性；它不保证 bitwise 一致，也不能把 correction 当作任意
off-policy reuse 的许可证。短 Context、同一 engine 或数值差异远小于 clipping / reward noise 时，简单路径仍更可靠。
长序列的 context parallelism 还必须把 communication cost 与 policy-quality target 同时计量，不能只报告峰值吞吐。

量化不能只作为独立 kernel 优化：RL loop 会让 rollout logits、reward score 与 update gradient 的误差经不同路径累积。数值 owner 应分别记录 rollout distribution drift、reward-ranking flip 与 optimizer update deviation，再决定哪些张量可用 MXFP4、哪些必须保留更高精度。低精度换吞吐和显存，却新增跨阶段误差耦合；一旦 verifier pass、KL 或 held-out capability 超出误差预算，应回退局部高精度，而不是只看训练 loss。

<!-- source-family:SF-2026-ARXIV-2605-20402 -->
exact-v1 §5–6 的 MXFP4 分解和 §7 实验只支持论文披露的训练配置；它不证明所有 RLHF pipeline 都可安全使用同一低精度策略。

各自减小相对高精度参考的量化误差，不保证训练与 rollout 两条量化路径更一致。相同 trajectory、token 和 quantization site 可保存 rollout codeword 与 scale，再从训练激活的两个相邻 FP4 候选中选择更接近该 codeword 的值。完整信息只在相同候选和 scale 下不增加局部差异，不保证整网或 policy divergence 单调下降，也不消除异步策略陈旧。

Guidance 还需经历 GPU 缓冲、CPU cache、存储和训练端回载；只保后半层 mantissa/scale 是降通信的近似分支，不继承完整 codeword 的逐点保证。[TRACE v1](https://arxiv.org/html/2610.07767v1)的有限 MoE 对照仍有任务退步，少保层也降低质量；decode-only 吞吐不等端到端 RL 加速。配对、存储或校准成本不合算，或质量/陈旧样本未过门时，已有 ratio 校正、短 buffer 与较高精度路径仍成立。<!-- source-family:SF-2026-ARXIV-2610-07767 -->

多条不同权重的 RL pipeline 还可共享同一设备的不同 SM/显存份额：prefill、decode、工具等待与训练的资源形状互补时，spatial multiplex 能提高总吞吐；同一 pipeline 的 DP workers 则可把剩余长尾 rollout 合并到少数 worker，释放其余资源。这是跨 pipeline 资源分配和 pipeline 内尾部迁移两种控制，不等于单管线的异步 policy-staleness 容忍。Runtime 应保留 pipeline/model identity、各阶段和 microbatch profile、SM/memory interference、迁移 frontier 与 KV recompute 预算，不能把另一条训练的占用当空闲资源。<!-- source-family:SF-2026-ARXIV-2604-23838 -->

它增加 profile/lookahead、微批重排、迁移及 KV 重算成本，并依赖资源画像慢漂移。[exact-v1 §4–5](https://arxiv.org/html/2604.23838v1)的两 pipeline 汇总 tokens/sec 提高，与单 pipeline 平均 step 延迟增至约 1.48 倍可以同时成立；吞吐结果不证明训练质量等价、公平性或每个作业的 deadline 改善。画像失效、同卡争用或单作业延迟超界时，应回退独占/静态配额与普通同步/有界异步 runtime；更新端的 logprob、freshness 和 outcome gate 不因资源复用而取消。

### 异步 On-policy Distillation 需要 Sample Freshness

缓存 rollout 能复用昂贵采样并提高 trainer 利用率，在 policy 变化慢时是合理近似；长 horizon 或异步更新后，同一 buffer 同时包含 rollout drift 与 supervision drift，旧样本不再等价于当前 on-policy evidence。Runtime 因而要为样本绑定 behavior/teacher revision，并用 freshness score 决定接受、降权或丢弃，而不是只按到达顺序消费。

收益是允许有限异步而不把所有旧样本当作同质量监督；代价是版本状态、freshness estimator、样本浪费和估计偏差。漂移无法可靠估计时应缩短 buffer 或恢复同步生成。exact-v1 只在其披露的长程任务、模型、buffer 与 freshness controller 中验证该机制，不给出跨任务通用阈值，也不证明更高吞吐必然改善最终策略。

<!-- source-family:SF-2026-ARXIV-2605-17862 -->

剔除一个 group 全对或全错能减少无相对 advantage 的更新，却不能把当时全错的 query 永久判成不可学。一个有界回放分支将 query 与旧 response 分开保存：周期性用当前 policy 重生成曾失败的 query，只有观察到新的混合 reward 才进入更新；补 batch 时则使用短窗口内的历史 response，保留其 behavior probability 用于分账。Re-evaluation 改变的是当前学习支持，response reuse 承担旧策略偏差，两者不能共用 on-policy 标签。<!-- source-family:SF-2026-ARXIV-2602-20722 -->

有限 group 的零命中不是成功概率零，当前重测也会受 verifier 和采样噪声影响；FIFO 容量、重测周期、reward 范围与新旧样本占比共同改变训练分布。[BAPO 有限1.5B～8B/三类推理任务的 mini-test](https://arxiv.org/html/2602.20722v1)支持这一 batch 构造分支，不签普遍正 policy-improvement 定理；变小的实际 batch 减少 backward 工作，故少 rollout 或相同步数并非整流程等预算。重生成、behavior logprob 重算、存储与调参均付费；reward 不可靠、policy 漂移难以估计或成本不合算时，保留 fresh rollout、短 buffer 与独立 held-out 验收，而不把旧成功轨迹当当前能力。

## Human feedback 不等于统一人类价值

标注结果受 rubric、文化、组织 policy、任务和标注界面影响。多数投票会掩盖少数群体偏好，专家任务又可能无法由通用标注者可靠判断。

系统需要记录：

- Label source 和 population。
- Rubric/version 与 policy change。
- Agreement、tie 和 uncertainty。
- Sensitive slices 与 appeal/escalation。
- Synthetic/AI feedback 是否混入。

更准确的名称是“使用特定 feedback process 优化模型”，而不是宣称模型已与抽象的“人类价值”完全对齐。

从人的反馈提取原则时，当前任务中的偏好理由与脱离具体任务表达的一般价值应作为两条来源流：前者能解释这次比较，却可能看不见已被满足或罕见风险的原则；后者补充更宽目标，却不自动反映同一人群的具体选择。可以分别生成、聚类并按偏好预测或多样性/共识代理排序，合成 candidate constitution，但来源人口、任务条件、聚类与排序版本应保留，stakeholder discussion 与 ratification 才决定是否批准。[受限两流实验](https://arxiv.org/html/2601.18760v1)用不同数据人口，局部人类偏好和小安全切片不能认证组合因果或民主合法性。模型误读理由、代表性缺失和冲突观点压缩仍需处理，生成、标注与讨论也计费；来源不匹配或批准缺位时，回直接征询、窄域显式原则与独立审核，不把聚类后的高分候选冒充共同意愿。<!-- source-family:SF-2026-ARXIV-2601-18760 -->

反馈类型还决定观测模型，不能把 preference、demonstration、ordinal rating 和“何时停止”直接当同尺度 reward 相加。一个条件分支用共享 latent reward 连接它们，但分别写出 Bradley–Terry 比较、基于 Q 的 Boltzmann demonstration、ordinal likelihood 和依累计 regret 变化的 stopping hazard；未观察到停止时也须保留 right-censor 信息，而不是伪造一个负面评分。变分推断同时拟合 reward 与辅助 Q，使不同类型提供互补约束，但依赖给定 latent reward 后的条件独立和各自 likelihood 合理；这与下文 rater identity 校准、迟到反馈队列是不同问题。<!-- source-family:SF-2026-ARXIV-2602-15206 -->

[MAVRL v1](https://arxiv.org/html/2602.15206v1)的反馈由已知 reward/Q 模拟，生成与拟合采用同类模型；固定每种反馈数量后合并多种类型，总反馈量也增加，不能解释为同总标注预算的纯优势。CartPole 某组合 return 12.2 低于 rating-only 的69.8，EPIC 的 shaping/scale 等价也不提供 cardinal reward 真值。环境扰动测试重新训练 policy，不是原策略的零样本安全证书。真实人口相关、模型错设或 censor 机制未知时，应分别校准反馈类型、保留可信偏好监督和独立 held-out 行为验证，而非强行统一；likelihood 推断与收集成本仍须计入。

### Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间

把 reward 当作同尺度、同步到达的标量，在 rater 同质且反馈能在 update 前返回时是合理的；现实约束同时来自身份异质性和时间异步性：不同 rater 的 offset/slope 不同，慢 verifier 或人工反馈又可能晚到数个 gradient step。RLHF 状态因此需要同时持有 rater identity、calibration slice/shrinkage prior/version，以及 pending reward queue、age/kernel、originating policy/importance ratio 与 reinjection mass。每位 rater 的 held-out affine calibration 可用 empirical Bayes 向总体收缩；迟到 reward 则以 clipped residual 进入后续 advantage。论文分别在 PRISM/PluriHarms 与 tabular MDP 上报告 RMSE 改善和最高 47.9× bias reduction，但没有证明非线性或 adversarial rater、online drift、large-scale RLHF 稳定性与生产 queue failure。稀疏 rater 回退总体 calibrator 并抽样审计；delay/mass 假设失效时等待慢反馈或采用 bounded synchronous update。

标注者差异还可能是比较方向的系统性反转，而不只是 offset、尺度或随机噪声。一个受限分支联合学习 reward 与正、零、负 expert trust，让稳定反向的比较贡献反号信号；零信任则不据此提供方向。识别依赖共享且有非零 reward 差的比较支持与连接条件，reward/trust 同时反号仍可产生同样的观察，因此方向锚点不能由 joint fit 自签。[受限控制任务实验](https://arxiv.org/html/2601.18751v1)使用模拟 experts，更多反馈也能恶化结果，单个 global trust 不说明不同 context 的资格。应保留 annotator、比较图、信任版本与外部方向核验，并支付联合拟合和反馈成本；正文与算法的精确权重因子未闭合，不拼成保证。支持不相连、可靠方向未知或真实反馈漂移时，回零权重争议隔离、已校准非负信任与独立人工审核，不把负信任解释为“已恢复真实价值”。<!-- source-family:SF-2026-ARXIV-2601-18751 -->

### 在线反馈的采样预算应由 Epistemic Uncertainty 驱动

静态离线 preference pairs 易复现、审核成本可控，在 policy 变化小或人类反馈昂贵时仍合理；但 policy
持续更新后，旧 pairs 会偏离当前 response distribution。简单周期刷新能改善 on-policy coverage，却仍把
预算平均花在模型已确定的比较上。

更有信息效率的路线是在当前 policy 产生候选后，用 reward ensemble、posterior 或其他可校准方法估计
epistemic uncertainty，只把高不确定 pair 送去人类/可信 oracle，再增量更新 Reward Model 与 policy：

```text
current policy candidates
→ uncertainty-calibrated pair selection
→ authoritative preference acquisition
→ versioned RM update
→ policy update and held-out audit
```

这把 feedback selection 本身变成 policy state，必须记录 selector、calibration、population 与拒绝策略。
模型 disagreement 也可能来自共同错误或噪声，不等于真实信息价值；若 selector 只挑“模型觉得困难”的
样本，还会遗漏未知未知与少数群体。因此需要随机 audit slice、覆盖 guardrail 和独立 evaluator。静态数据
在监管复现、低漂移任务和 calibration 不可信时继续成立。

Reward interface 也可以从静态 scalar judge 演进为 policy-conditioned reasoning judge：让 judge 观察当前
policy 的对象、分步检查等价性或结构约束，再输出 preference。它能减少字符串匹配对数学/结构对象的误拒，
却让 judge 与 policy 更容易共同适应；teacher/judge revision、表达 canonicalization 和 human calibration
必须进入 evaluation contract，不能把 generative judge 当成 truth oracle。

## RLHF、RLAIF 与 Verifiable Reward

Feedback 不一定直接来自人类逐条点击。AI judge、规则检查器、代码测试或数学 verifier 都可以产生 reward。

这些路径改变 reward source：

```text
RLHF  human preference feedback
RLAIF AI-generated or AI-judged feedback
RLVR  rule-based / verifiable outcome reward
```

但稳定问题相同：reward 是否代表真实目标，policy 是否能 exploit evaluator，训练分布是否覆盖部署任务。Verifier 更客观不等于完整，例如单元测试可能漏掉隐藏错误，数学 final answer 正确也不证明 reasoning process 可靠。

规则反馈还可以先由模型离线构造，再在训练 rollout 上仅执行冻结的规则：从 reference answers 提取 keypoints 和有序 keywords，以正则匹配后的 keyword-LCS 测内容覆盖；风格则由另行生成的 Python functions 加权评分。离线模型拥有 reference 与规则提案，运行时执行器只测这份 artifact，不能因为没有在线 LLM judge 就把合成偏差消除。[受限 RLVRR 对照](https://arxiv.org/html/2601.18533v1)中有序匹配比直接词面奖励少一种 verbosity hacking，却不验证事实、否定或等义改写，也不是 token-level 语义监督。Reference、keywords、code、权重及失败口径应共同版本化；离线生成费用与训练 step 费用分账，0.71% 的相对 step 成本不等全链降本。规则过拟合、语义错判或代码不可安全执行时，回人工 rubric、独立 semantic verifier 或已有 outcome reward，不让 compiled proxy 替实际质量签证。<!-- source-family:SF-2026-ARXIV-2601-18533 -->

反馈者也可以取得 student 不可见的训练期信息：让 judge 读取参考语言的解答，在目标语言 rollout 之间做成对比较，再把同题候选的胜率转成相对 reward；student 仍只从目标语言问题生成。这不同于把参考答案直接拼入 student，也不同于答案、格式或语言识别器的二值验证。Reference 来源、翻译、judge 与 rollout batch 应共同保存，胜率依赖候选集合，交换展示顺序后平均也不能消除循环偏好或共同错误。[受限多语训练对照](https://arxiv.org/html/2601.18722v1)中特权 judge 对某些两答案均正确切片反而更弱，不构成逐步真值；八候选带来二次成对调用，少数据不等全训练降本。参考或 judge 资格不可靠时，保留 objective verifier、独立过程审核和原无特权反馈，而不由相对排序替答案正确性签证。<!-- source-family:SF-2026-ARXIV-2601-18722 -->

若目标是提高推理文本的可审计性，而不是只奖励最终答对，可以让独立simulator根据原输入、回答与CoT预测同一policy在counterfactual输入下的答案，再与不看CoT的outcome-only simulator比较。两者差额定义推理文本对行为预测的增量，区分解释有用、无增量与误导；据此重写/筛选轨迹并用reward-weighted正例学习与negative unlikelihood更新policy。Counterfactual、policy、rewriter、simulator及采样预算共同定义监督身份，该奖励不是真实内部计算或答案正确性的标签。<!-- source-family:SF-2026-ARXIV-2602-20710 -->

[有限二元任务对照](https://arxiv.org/html/2602.20710v1#S5)显示cue条件下的simulatability改善，却在部分generic任务主要改善outcome一致性而非CoT增量；人工cue/拒绝样本人口与反向cue限制外推，作者未观察到cue-based与model-generated两类counterfactual之间的transfer，分别训练不授统一introspection。额外重写、simulation与训练均计费，任务准确率仍须独立验收；simulator共同偏差、增量不成立或质量下降时，回退原outcome verifier、人工/独立过程审计，不把可模拟性替正确性或causal faithfulness。

当 feedback 可以自动验证后，下一层瓶颈会从“怎样打分”转向“怎样持续生成既有学习价值、
又可可靠验证的任务”。只从固定 environment 取样，verification 较强，但 task
distribution 容易过窄；让模型开放式生成任务可以扩大覆盖，却可能把 malformed、
trivial 或无法验证的样本送进 reward loop。一个可能的中间抽象是把可复用的 task
pattern、generation constraints 和 validator 组织成 skill-conditioned curriculum：

```text
fixed environment
→ reliable verifier, narrow task distribution

unguided task generation
→ broad distribution, noisy or unverifiable reward

skill-conditioned proposer + validator
→ bounded task family + explicit verification contract
```

Skill Self-Play 是这一方向的实验性案例：proposer 根据动态 skill 生成任务，solver
在验证后的 curriculum 上更新，controller 再根据执行反馈扩展或淘汰 skill。这里可长期
保留的不是作者 benchmark，而是论文机制中的 training task、validator、skill library
与 solver policy 会共同演化。工程上，这意味着它们都必须版本化并接受独立 Evaluation。
单篇预印本尚不能证明这种设计已解决 open-ended curriculum、validator exploit、
跨领域迁移或 bootstrap 能力门槛。

课程的可变对象还可以从固定规则下的随机 seed，扩展为固定 simulator 接口内的 initial-state、transition 与 goal 程序：先根据父环境及学习反馈提出规则描述，再生成代码，经编译与短 rollout 后送入课程。但代码能运行只通过执行层检查，不证明规则语义正确、任务可学习或课程值得训练；仍可给原目标环境保留明确采样份额，防止持续扩展的生成分布取代交付目标。生成器、程序/engine、parent lineage、课程选择和 learner revision 应共同保存，这是对该接口可重放性的工程推导；[DiCode 的受限 Craftax/GTrXL 对照](https://arxiv.org/html/2602.08194v1#S3)只支持该模拟分支，同环境步数不等更新次数、模型生成调用或总训练费用，去掉 parent/performance 的消融也只识别这组设计的联合贡献。生成、短运行过滤和分布验证都付费；代码错误、目标质量回归或课程失去学习价值时，退回固定 engine/seed 课程、目标环境与独立 held-out 验收，而不是把可执行程序当作通用 LLM 训练或现实环境有效性的保证。<!-- source-family:SF-2026-ARXIV-2602-08194 -->

同一问题内部的 verifier budget 也有 curriculum 条件：弱 policy 可能从较容易的测试获得有效正反馈，较强 policy 才能利用困难切片；不能仅按参数量或“测试越难越好”选比例。一条受限分支先依据基础 policy 的能力诊断预选各 test tier 的训练配比 α，再单独设 reward weight w；抽哪些测试和怎样计分是两项状态，这不是训练期间在线自适应的难度 controller。[TAROT 的有限 coding 对照](https://arxiv.org/html/2602.15449v1#S3)中不同模型/目标域的最佳策略不同，某些简单或完整测试基线仍更好；reference、生成器覆盖与测试生成成本也限制可归因范围。Tier 身份、诊断人口、α/w 和执行预算均须版本化，诊断失准或尾部质量回归时保留固定完整测试、既有 curriculum 与独立 evaluator，不能以局部均值提升授予通用 hard-first 或正确性保证。<!-- source-family:SF-2026-ARXIV-2602-15449 -->

长度也是训练中的选择条件，而不只是部署统计。只给“答对且短”正 reward 时，四类 rollout——短正确、长正确、短错误、长错误——必须分别保存 mask、reward 和真实采样截点；零 reward 仍参与 group 比较，移除样本却改变了有效训练人口。若只保留正确轨迹，长正确便可能成为唯一负信号，使 policy 把“短”当成“正确”的捷径；把所有长轨迹 mask 掉又可能留下未约束的长度空间。因而长度曲线应按 correctness 拆开，不能以平均输出变短签推理能力保持。

[受限效率 RL 对照](https://arxiv.org/html/2602.20945v1)显示，正反馈稀疏的 hard prompts、不同负样本 mask 与 staleness 会改变 collapse 或 length-rebound；缩短真实 rollout 截点与生成长轨迹后惩罚不是同一干预。较易 prompt 或更多 rollout 能改善有效 reward 密度，却改变输入支持与计算量，不能据此宣布普遍 easy-first 或 N 越大越好。应在相同 policy/verifier 下并列多个部署 token 预算、质量和每次有效 update 成本；小预算提升可能伴大预算退步，代码任务收益也较小。质量、奖励密度或长度控制不稳时保留原 correctness-only 目标、已验证的固定采样预算与独立多预算评价，而不是继续加强“更短”的代理目标。<!-- source-family:SF-2026-ARXIV-2602-20945 -->

### Imperfect Verifier 把监督噪声与 Rollout Compute 绑在一起

RLVR 假设 verifier 能稳定区分正确与错误，实际 false positive 会奖励错误轨迹，false negative 会丢弃有效探索；增加 rollout 数量可能同时放大这两种噪声。训练合同应记录 verifier confusion profile、rollout budget 与 policy distribution，并把“更多采样”和“更好监督”作为独立轴。收益是能选择 compute–supervision trade-off，代价是需要可控噪声估计与额外验证；确定性可执行任务仍可使用简单 verifier。现有结果仅覆盖 Qwen2.5、GSM8K 与 GRPO，不构成跨任务定律。

<!-- source-family:SF-2026-ARXIV-2605-25252 -->

这个取舍还会反过来改变训练人口，而不只是 verifier 的准确率。若一次回答必须同时满足多个约束，联合奖励会把任何一项漏检传给整个样本；增加 soft constraint 种类也可能增加误接受，而非自动扩展有效监督。一个受限指令跟随分支先短程训练，保留 pilot 中至少曾获正奖励的样本，再把每题 soft constraint 限为一项，让约束覆盖与判定可靠性成为两个可比较的轴。它不是识别“逻辑不可满足”的算法：零成功可能来自当前 policy 或预算不足，删掉这些样本会改变课程与支持人口。<!-- source-family:SF-2026-ARXIV-2601-04954 -->

[局部 hard-only/mixed 与过滤对照](https://arxiv.org/html/2601.04954v1)支持检查这一分支，但 hard-only 并不在所有任务和模型上胜过 mixed；单向 false-accept 注入也不代表真实 judge 的相关噪声。注意力变化不能证明已经学会通用 meta-skill，每步变快不包含 pilot 和全部数据成本。没有可靠规则代理、困难样本被过度排除或独立泛化回归失败时，保留 mixed、人工或模型 judge，并单独验收被删人口；不能由 training reward 或约束变少批准长期泛化。

### Reflection 只有进入可验证更新回路才是训练状态

把 reflection 作为一次性 prompt 文本，最容易接入但不会积累可审计经验；把失败轨迹、环境反馈与修订后的行动组织成 versioned reflection state，才能让后续 rollout 复用。其收益是把失败转成可训练信号，代价是错误反思自强化、额外存储与 evaluator 成本。Reflection 必须由环境结果或独立 verifier 筛选，并允许丢弃或回退到原 policy；没有可靠反馈时，临时 scratchpad 比持久更新更安全。

<!-- source-family:SF-2026-ARXIV-2605-20477 -->
exact-v1 §3–4 描述经验驱动 reflection，§5 的 MiniHack/ALFWorld 结果及 §5.3 边界不能证明开放域 reflection 忠实或长期稳定。

对多轮生成工具，最终满足约束的 point reward 与相邻结果被 judge 判为改善的 pair reward，可以提供不同压力：前者测交付候选，后者只鼓励修订方向；最终失败时降低 pair 的权重，避免只有“相对变好”就获得完整成功信号。Pair judge 仍可能共同误判，连续改善不认证每个约束或内部反思忠实；[受限图像工具训练](https://arxiv.org/html/2601.18543v1)还按交互轮数重采样 rollout，必须连同候选人口与工具版本保存，不能把变化全归给奖励形状。配对判断、更多生成和训练期特权参考另付费，局部消融增量与第三轮收益下降不授任意工具或免费质量提升；多义目标会诱发过度反思。缺可靠终局判据、工具能力已达上限或费用不值时，保留固定轮数、普通 outcome reward 与独立交付验收，不由 pair 分数替安全 gate。<!-- source-family:SF-2026-ARXIV-2601-18543 -->

### 从终局 Reward 到可验证子问题 Curriculum

终局 reward 在任务短、成功条件明确时最少引入人为结构；长推理链里，它却把 credit 全部压到最后一步。若 reference chain 本身可审计，可以由 curriculum builder 把终局任务派生为有边界、可判定的 subproblems，verifier 只提交这些局部判据的 credit，再由训练控制面决定是否进入 policy update。这里 curriculum builder 拥有难度与分解边界，verifier 不拥有策略提交权。

更密集的反馈换来 reference bias、子问题捷径和“局部全对但整体失败”的新风险；因此必须保留未分解的终局任务作为 held-out gate，分解失真时回退终局可验证训练。arXiv:2605.22074v1 只支持作者 reference-derived curriculum 与受测任务中的实验结果，不证明任意 chain decomposition 都保持原目标。

<!-- source-family:SF-2026-ARXIV-2605-22074 -->

#### Learning Progress Reward 必须绑定 Sealed Audit

把“最近变好多少”作为 intrinsic reward，只有当进步等于固定 sealed-audit loss 的有符号下降时，累计奖励才 telescoping 到端点改善。Evaluator owner 必须冻结 audit panel、model class、访问协议和未裁剪的 signed delta；训练 scheduler 只能消费该分数，不能让 agent 选择评测 stream 或反复探测可复用 panel。

这条路径把好奇心奖励约束到可审计学习，却以 holdout 容量、访问隔离和 uniform generalization 前提为代价。Clipping、agent 自有 stream、panel 泄漏或模型类过强都会使保证失效；此时回退独立 holdout、外部可验证 reward 或人工 curriculum。作者的理论、有限实验与形式化只支持明确前提下的 Goodhart resistance，不证明开放任务中的普遍安全。
<!-- source-family:SF-2026-ARXIV-2606-11417 -->

### 后训练分支的本质差异是 State Distribution

只按 token objective 区分 SFT、distillation 与 RL，容易忽略监督发生在哪个状态上。静态 SFT 在固定数据分布上学习；on-policy distillation 让当前 policy 先到达自己的状态，再接受 teacher signal；RL 则在 policy-induced states 上用 reward 改变访问概率。约束从“标签是否正确”变化为“训练是否覆盖部署时会到达的状态”，因此 rollout producer、policy revision、teacher/reward revision 与 staleness 必须共同进入 run identity。

扩大状态覆盖能修复静态数据看不到的错误，却增加 rollout 成本、off-policy staleness 和反馈回路；部署状态稳定、示范覆盖充分时，静态 SFT 仍然更简单可靠。arXiv:2605.22731v1 的比较仅支持论文模型、任务与训练设置，不证明 on-policy 路线普遍优于 SFT，也不把不同 reward contract 视为可直接比较。

<!-- source-family:SF-2026-ARXIV-2605-22731 -->

事后反馈还可以改变教师评分时的条件，而不改变学生作决策时的输入。一个 turn 结束后，标量 PRM 把下一次用户回复或工具结果压成好坏；若其中含可操作的纠正方向，则可先抽成短 hint，只附到教师使用的原 prompt，再让同一模型对学生已经生成的 action 做逐 token 强制评分。教师在增强上下文与学生在原上下文下的 log-probability 差，提供比整段同向 reward 更细的更新方向；部署学生仍只看当时可得的原 prompt。这里事后信息是训练监督，不是声称 Agent 行动时知道未来，也不要求另一个更强教师。标量路与 hint 路的 admission 应分开：没有可核 hint 时仍可保留可信的 scalar 反馈，但不能制造方向标签。<!-- source-family:SF-2026-ARXIV-2603-10165 -->

这条分支用 hint 抽取、额外 teacher scoring 和筛选偏差换更密的监督；最长或较详细的 hint 不自动更正确，用户不满也不能覆盖任务正确性与安全约束。样本应绑定原 prompt/action、后续反馈、selector 与 teacher/behavior revision，异步时仍执行前述 freshness 规则；增强条件的训练收益还须在移除 hint 的学生、独立 outcome 及原能力回归上验收。[有限模拟与 Agent 对照](https://arxiv.org/html/2603.10165v1)使用同一模拟 LLM 作个性化评分，GUI 又评训练集，不能认证真实用户或开放环境中的普遍收益，也不证明标量与方向混合免费优于单路。Hint 不可信、反馈稀疏、配方或 revision 不清时，回退可信 scalar/outcome、fresh rollout 或覆盖充分的 SFT，不把事后教师分数当部署能力或 release 授权。

覆盖当前 policy 的状态不一定要求每次生成完整长回答。一个预算分支只让 student 生成前 L 个 token 后停止，teacher scoring 与反向 KL 更新也仅消费该前缀，部署评价则移除长度 cap；随着训练逐步延长 L，可以把生成和监督预算从尚未稳定的长尾移向头部。它要求 teacher/student vocabulary 与基础指令格式兼容，格式 special token 的强制也须进入训练身份。前缀省掉的不是无用状态：短前缀未监督的尾部仍可能漂移，容量较小的 student 尤其不能借头部改善推断整条 trajectory 或拒答/calibration 已学会。<!-- source-family:SF-2026-ARXIV-2602-15260 -->

[Prefix OPD v1](https://arxiv.org/html/2602.15260v1)在 Qwen3/OpenThoughts3 的受限实验中出现1.7B短前缀 GPQA/MMLU 低于 base、尾部 loss 上升的反侧；渐长 schedule 与较大 student 更稳，充分预算下较长监督也可能更好。AIME24 同时参与 checkpoint 选择与报告，SeqKD 使用不同 teacher、batch 和数据预算；所报47倍是达到类似 AIME 目标的 GPU FLOPs 估算（2.7e19 对5.7e17），不是测得的时间缩短；GPU hours 另报且未计 SeqKD 离线生成，不能当普遍训练加速。late refusal/calibration 风险只是讨论，并非已测安全结果。应保留完整尾部与 OOD 行为回归，失败时延长 prefix、恢复 full OPD 或使用覆盖充分的 SFT；新的预算取舍不取消前述 revision/freshness 条件。

Teacher/student tokenizer 不同时，状态覆盖还要与监督对齐的可靠性分开。可按共同文本边界分组，仅在双方均为单 token 的严格位置比较共同词汇，并分别归一化概率、计算 reverse KL；学生选出的 top-k 共同词项可形成更小的共享监督集合。静态词汇重叠率不决定实际轨迹上的严格位置比例，扩大不匹配 span 的监督也不必然迁移更多能力。

把 span 内 token log-probability 加总后做 MSE 虽补齐结构覆盖，却改变了逐位置分布匹配的目标。[三组异 tokenizer 数学/代码对照](https://arxiv.org/html/2610.08448v1)中，正 span 权重均低于仅严格位置的结果；弱/负梯度方向只是诊断，不证明所有 span loss 有害。对齐、共同词项、归一化、EOS、权重和完整回答 outcome 应分别验收，不能用 coverage 签发迁移收益。单次100步、H20×8 BF16 的局部实验不授 top-16 通用配方或总成本下降；严格覆盖不足时，仍需更可靠的 byte/span 对齐或已验收的同 tokenizer teacher。<!-- source-family:SF-2026-ARXIV-2610-08448 -->

#### 从外部协作到参数内化需要独立 Scaffold-removal Gate

在 policy 尚不能独立到达有效轨迹时，运行时调用冻结 expert 或 tool 是可逆、可观测的能力扩展；它不会自动成为本地模型能力。若要降低在线调用成本，可以先训练 controller 学会在 policy-induced state 上路由外部 expert，再只将 verifier 通过的成功协作轨迹转换为监督数据，最后训练本地 checkpoint。Router 拥有调用 proposal，expert 产生外部 span，verifier 拥有 trajectory admission，learner 写入参数；只有移除 scaffold 后的独立回归、原能力 retention 与安全 gate 才能提交“能力已内化”。

这条分支用在线专家成本、路由错误和外部依赖换取更广的可达状态，再用 success-selection、格式蒸馏、遗忘风险与重训成本换取较低的部署依赖。Training identity 必须绑定 controller/policy、每个 expert revision、router、verifier、trajectory-conversion policy 与目标 checkpoint；格式权重敏感或 expert-span entropy 变化都不能单独证明知识迁移。任务量小、领域持续变化、verifier 不完整或回归失败时，应保留运行时 expert/skill；示范已充分覆盖时，普通静态 SFT 仍更简单。exact-v1 证据只覆盖两个 controller 规模、三个冻结 experts 与数学/知识问答设置，也未给出在线成本与训练摊销的 break-even。

<!-- source-family:SF-2026-ARXIV-2609-12578 -->

### Memory-conditioned Rollout 改变 Behavior Distribution Identity

在每个 episode 清空外部状态，rollout distribution 只需绑定 policy、prompt 和 environment；让 Agent 先生成 tips/memory 并在后续 episode 中读取，会同时改变 observation、exploration path 与 action probability。若随后混合 on-policy 与 replayed/off-policy updates，样本 identity 必须增加 memory content/hash、生成它的 policy/reward revision、read mode、behavior probability、episode lineage 与清空边界。memory generator 只产生 exploration proposal，trajectory store 保存真实 context，learner 根据 support/freshness 决定 update，outcome verifier 仍拥有任务正确性。

跨 episode memory 可以复用探索经验，却引入 self-confirmation、错误 tips 放大、memory staleness、importance-ratio 方差和训练/部署状态不一致；把 memory 内化进参数后，也不能默认外部 scaffold 已可删除。memory 来源不可信、behavior probability 不可恢复或 deployment 不提供相同 read path 时，应清空状态、回退 fresh on-policy rollout 或仅使用可审计的监督样本，而不能把混合经验当成同一 policy distribution。

<!-- SF-2026-ARXIV-2602-23008 -->

## PPO、GRPO、DPO 分别接住什么

### Feedback Loop 从固定环境演进为双层控制系统

固定环境与 verifier 在能力相对稳定时足以提供监督；当 policy 的能力边界持续移动，环境若不暴露新失败，训练会优化过时接口。更完整的闭环让 verifier diagnosis 产生 environment/interface proposal，再由独立 gate 更新任务和反馈分布，policy 与 learning interface 因而拥有各自版本与回滚点。它能把新失败转成课程，但会引入非平稳性、评估污染与共同过拟合；冻结环境的 held-out gate 仍必须保留。

<!-- source-family:SF-2026-ARXIV-2605-24426 -->

静态文字反馈同样可演进为 bilevel 控制：下层 actor 学习利用反馈，上层 feedback generator 以真实 policy return 为目标更新，而不是只模仿通用 rubric。收益是反馈能适应当前 policy，代价是 reward hacking、计算成本和 credit assignment 更难审计；固定 rubric 在样本少或上层回报不可信时仍更安全。该证据仅支持作者实验中的 Stackelberg 训练，不证明自然语言 critic 能代表人类偏好。

<!-- source-family:SF-2026-ARXIV-2605-24547 -->

### 在线 Credit 需要显式的时序状态

完整 trajectory 后更新实现简单，但长 horizon 与 partial observation 会让 credit 延迟且内存增长。维护 recurrent hidden state 与 eligibility trace 可在每一步执行 exact online update，把“当前可见状态”和“历史如何影响参数”分别交给两个状态 owner。收益是流式学习，代价是 recurrent state 漂移、截断恢复与并行训练更复杂；短 episode 或可离线重放时，batch trajectory 仍更容易验证。当前结论只覆盖特定 diagonal recurrent 架构及其实验，并不证明所有大模型后训练可直接使用同一更新规则。

<!-- source-family:SF-2026-ARXIV-2605-24709 -->

#### Off-policy Action Credit 必须绑定 Behavior Policy 与 Decision State

完整 trajectory 由同一版 policy 生成时，return 与 action 的归属最清楚；但真实 VLA 数据常由旧 policy、人工接管和不同环境条件混合产生，直接把离线 advantage 当作当前 policy 的 on-policy credit，会把策略变化误算成动作质量。更完整的 transition identity 至少应包含 observation/action prefix、behavior-policy revision 与 action probability、critic revision、environment/task revision 以及 intervention state。数据采集端拥有 behavior facts，evaluator 只产生 action-level credit proposal，learner 才拥有参数更新的提交权。

importance correction 与 advantage weighting 能提高旧轨迹的利用率，却会引入高方差、support mismatch 和 critic bias；clip 或筛选能控制方差，也会丢弃稀有但关键的纠错动作。当前 policy 已明显离开 behavior support、概率不可恢复或人工动作没有可比较 propensity 时，应回退到新鲜 rollout、受控再采集或仅把样本用于监督学习，而不能给离线 credit 伪造精确归属。

<!-- SF-2026-ARXIV-2602-12691 -->

### Reward Model 误差必须在 Deployment Policy 下结算

只测 reward model 在训练偏好分布上的预测误差，无法回答优化后的 policy 会把流量推向哪里。评估应同时保留训练分布 prediction error 与 reward-tilted deployment distribution 下的 policy-value gap；后者由实际 policy occupancy 拥有。这样能发现“验证集准确但被 policy 放大”的误差，代价是需要 on-policy 或可信 importance weighting，且估计方差更高。policy 变化很小、支持集充分时，传统 held-out 误差仍有价值。该分析说明测量缺口，不自动给出一个无偏的真实人类价值估计器。

<!-- source-family:SF-2026-ARXIV-2605-24749 -->

修复这种人口失配也可以改变Reward Model的训练候选，而不只重测误差：先在reference与人工构造的perturbed候选上训练评分器，随后用当前policy真实生成替换perturbed候选，再交替更新评分器与policy。一条[有限图像编辑分支](https://arxiv.org/html/2602.17558v1#S4.SS3)观察到简单扰动与policy组合编辑的支持不同；候选换代因此应记录policy/RM revision、样本来源与每轮训练角色，不能把旧评分器的准确率直接移交给新policy。它仍规定reference总优于候选，训练reward包含此排序和格式要求；MLLM过滤与标注不会证明该关系对所有policy生成都真，也不把生成的审美metric变成人类价值。Qwen2.5-VL-7B双模型与GLM-4.5V注评共享、10k扰动/额外5k候选及300自建测试/400无同类instruction目标的MIT图像只支持局部比较，perturbed-only与policy-guided的结果不授跨任务保证；GPU、precision与完整训练预算未披露。额外policy rollout、metric生成、RM重训与交替policy训练都付费；候选确可能优于reference、共同judge盲点、独立偏好或预算回归时，冻结换代、保留原RM与可核偏好/reranking，不靠持续交替优化自己的分数宣布真实效用改善。<!-- source-family:SF-2026-ARXIV-2602-17558 -->

改变 reward instrument 与更新 policy 也可以分阶段持有不同参数权限。对生成模型的一条受限路线先冻结 generator，仅在其样本上学习评分器的 text-condition direction；将正反方向归一化并外推形成新评分条件后，再冻结这个条件、更新 generator。它试图调整 proxy 的选择偏向，却没有恢复真实人类价值的权限，第二阶段的新人口仍须独立评价；one-step 重建对象也不等于部署完整采样。[有限图像偏好对照](https://arxiv.org/html/2512.24146v1)并非所有指标都更好，局部多样性切片不保证任意 mode coverage。额外评分条件训练、generator 更新、判定器和盲评均付费，不能只用最后阶段步数称总预算更低；评分条件失配、模型改版或独立质量回归时冻结更新，回原 evaluator、可核偏好或保守 reranking，而不是继续优化自身改写的分数。<!-- source-family:SF-2026-ARXIV-2512-24146 -->

### 错误 Reward 的修复边界取决于 Update 是否已提交

发现个别 reward 错误后，最朴素的做法是改正分数，或在下一轮补一个方向相反的奖励。前者只在 optimizer update 尚未提交时是原位修复：系统应保留原始 trajectory 和 evaluator revision，用修正后的 reward 重新评分，并重算所有派生统计。PPO 需要重算 return、advantage 和 critic target；GRPO 中一个样本的分数变化会改写整组均值、方差与 advantages，因而不能只补丁单个标量。

一旦 update 已提交，修改存储的 reward 不会撤销已经发生的状态转移：模型参数、optimizer moments、critic 以及随后的 rollout distribution 都可能已改变。“补一个反向 reward”也不是逆操作，因为它作用在新参数、新 optimizer state 和新采样路径上。若污染范围小且独立回归未见恶化，可停用错误 evaluator，丢弃不再满足 support / freshness 的旧样本，再从新鲜 rollout 继续纠偏；这是 compensating training，不是精确撤回。

若错误是系统性的、影响跨越多个 updates，或已观测到能力与安全回归，可验证的路径是回退到污染前最后一个可信 resumable checkpoint，再用修正后的 reward contract 重放受影响区间。这通常不需要从 pretraining 开始，但要求 checkpoint 同时恢复 actor / critic、optimizer、scheduler、随机性、数据与 rollout cursor，并把 reward / policy revision 写入 lineage；只有 weights 时只能 warm start，不能声称继续原训练轨迹。

这里的 owner 边界必须清楚：本章拥有 reward / evaluator revision 与纠错决策；第 32、33 章分别拥有 PPO 与 GRPO 的派生统计重算；第 35 章拥有可原子恢复的训练状态。工程上是以重放成本换取纠错确定性；若没有 reward lineage 和可信 checkpoint，系统只能估计污染边界，不能证明错误已被完全消除。

本章只定义 RLHF pipeline 与 reward objective，后续三章职责不同：

```text
PPO   on-policy optimization with learned value/advantage and clipping
GRPO  group-relative advantage without a learned critic
DPO   offline pairwise objective derived from KL-constrained preference optimization
```

DPO 不训练显式 Reward Model，也不在 fine-tuning loop 内做 on-policy rollout，但仍依赖 preference data 和 reference policy。GRPO 可以使用 learned reward，也可以使用 verifiable reward；“移除 critic”不等于移除所有 reward design。

## Evaluation 必须独立于 Reward Model

### 训练停止不能只看 Training Loss 或 Reward Model Score

固定训练预算、training loss 与 Reward Model score 在代理指标仍能代表下游质量时，是成本最低且最容易复现的停止依据；但 policy 持续优化同一个 proxy 后，reward 可能继续上升，而独立任务质量已经进入不可恢复的下降区间。此时，停止判断必须引入带版本的外部 Evaluation Run：Evaluation 系统产生按时间排列的 downstream quality evidence，RLHF controller 根据持续下降、观测不确定性与 patience window 提出 stop proposal，训练作业 owner 决定是否提交停止，GPU Scheduler 只消费随后产生的资源释放事件，不拥有 reward 或质量真值。

这条反馈链可以减少继续训练坏 checkpoint 的时间并更早释放 GPU，但代价是额外评测、反馈延迟、judge drift、错误早停和多租户公平性压力。单点下降不能直接终止作业；信号不足时应回退固定预算、要求连续多个窗口确认或进入人工 gate。现有实验只来自离散事件模拟：Poisson 到达、slot 化 GPU、两分钟抢占以及参数化的 LoRA/DPO/RLHF 学习曲线；它没有证明生产 workload、生产 SLO 或真实集群中的通用收益。

<!-- semantic-body-binding:SF-EVALSTOP -->

至少要比较：

- Human preference win rate 与置信区间。
- Task correctness / verifier pass rate。
- Reward score 与 KL divergence。
- Response length、refusal 和 style shifts。
- Pretraining/SFT capability regressions。
- Safety、bias 与 adversarial prompts。
- Rollout throughput 与每次有效 update 成本。

如果最终 Evaluation 仍使用同一个 Reward Model，训练与评估共享漏洞，无法证明真实质量提升。

把多个 reward 组成 ensemble，也不自动补齐未被任何判据覆盖的质量维度：图文相似度、对象定位和总体偏好可以各有用途，却共同漏掉局部结构 artifact。诊断这种盲区，应固定同一 prompt，用独立人判的有/无 artifact 成对样本分别测 reward 的排序和 tie，再核对训练真正优化了哪些维度；总体分数上升与局部结构改善不能合成一个结论。辅助视觉 detector 可以补充观测，但其二标签归一分数仍是 proxy，训练/提示优化人口与独立诊断人口的切分、校准和误判须另验，不能把同一批诊断对上的读数当外样本准确率。新增标注、视觉判别、提示搜索与训练调用也要计入总预算；某些 reward 组合加入 detector 后仍可能退步，证据不足时保留独立人审和受控样本评价，并回退保守训练，而不是以 ensemble 数量宣称已消除 hacking。

### Reward Proposal、Phase Handoff 与 Exploration 都需要独立 Gate

自动生成 reward hypothesis 可以扩大搜索，但生成质量不授予训练 authority。候选 reward 应从共享 checkpoint 分叉，由 competence-aware verifier 检查，再按 training phase 小流量部署；收益是缩短 reward engineering，代价是额外分支训练、验证成本与 specification gaming 风险。Verifier 不充分时应回退人工设计或固定 reward。

<!-- source-family:SF-2026-ARXIV-2604-28056 -->

生成 reward code 前还须声明函数能读取哪些状态。只读当前 `(s,a)` 的 flat reward 无法区分到达同一状态的两条历史；若行为规范要求“上个 option 不同，下一 option 也应不同”，高层签名可显式读取 `(previous_option,s,option)`，低层签名读取 `(s,option,a)`。这是变量接口扩大了可表达的规范，不是层级 reward 对一切 flat reward 的优势：把同样历史加入 flat state 后，原来的不可区分反例不再成立；更多字段也不认证模型忠实翻译了语言规范。<!-- source-family:SF-2026-ARXIV-2602-18582 -->

这种生成链应拆开代码可编译/变量许可、任务可行性与行为规范对齐三个人口：先验证低层 subgoal policy，再训练高层组合，最终另验 task success 与规范。只在任务成功候选上平均行为分，或在可编译候选上报告任务成功率，不能改写为每次生成的成功概率。受限模拟对照保留同两层 trainer，但 flat prompt 不提供 option 字段；候选搜索、多 trial 训练与视频人评增加成本，固定 options/termination 和有限人评不授开放 Agent 安全。接口不足、验证器失准或预算不合算时，保留显式历史状态、人工设计/固定 reward 与独立任务验证，不由生成器提交安全结论。

SFT 到 RLVR 也不是中性 handoff：SFT 已改变 policy distribution，可能把 on-policy exploration 推离可验证区域。黑盒 on-policy distillation 可作为条件分支，在 preference/RL 前重新对齐起始分布，以额外 rollout、teacher 调用和 imitation bias 换更可训练的策略状态；没有 teacher access 或分布漂移不显著时，直接 handoff 仍更简单。

<!-- source-family:SF-2026-ARXIV-2604-28123 -->

最后，exploration 本身属于训练 trust boundary。模型可能通过减少有用动作抵抗更新，而不表现为显式 reward hacking；release evidence 应同时记录 rollout diversity、action coverage、policy-update magnitude 与 task progress。构造实验不证明部署模型普遍存在该行为，因此这些指标是诊断 sensor，不是恶意意图判决。

<!-- source-family:SF-2026-ARXIV-2604-28182 -->

### Teacher 与未来 Reward Model 都是反馈回路中的状态

On-policy distillation 比离线 teacher labeling 更接近学生实际访问的状态，但 teacher 输出不能被视为无条件真值：学生需要探索信息丰富的状态，teacher reliability 也必须决定哪些反馈可进入更新。这样能减少 distribution mismatch，却增加采样成本、teacher 不确定性估计和错误反馈放大；低风险、分布稳定的任务仍可使用离线 distillation。

<!-- source-family:SF-2026-ARXIV-2605-03677 -->

迭代 RLHF 还会把当前策略产生的数据用于训练未来 reward model，形成 policy → data → reward model → policy 的闭环。若优化只追逐当前 proxy，策略会逐步塑造更容易被未来 reward model 接受的数据，导致自强化的 alignment collapse。解决方向不是简单增加 KL，而是显式建模未来评估器、限制参数 steering 并保留独立 evaluation；其代价是双层优化和模型假设，假设不可靠时必须回退到冻结评估器、外部审计与阶段性发布。[受限证据：arXiv:2605.04266v1]

<!-- source-family:SF-2026-ARXIV-2605-04266 -->

### Post-training 必须把故障、探索与 Credit 组织成闭环

强化微调失败时，单看最终 reward 无法区分 environment error、rollout hang、verifier failure、policy regression 或数据污染。可靠 runtime 应采集可观察 fault fingerprint，先诊断故障 owner，再执行重试、隔离、降级或样本剔除，并把处置结果写回下一轮训练。自动 remediation 减少人工停机，却可能把诊断误差放大为数据偏差；无法归因时应冻结更新并保留原始 trajectory。

在线 preference learning 的 exploration 也不能只依赖当前 policy 的瞬时不确定性。历史样本覆盖、observer disagreement 与旧策略误差可以提供更稳定的 prior，再用当前观测修正 exploration budget。这样能把查询集中到高信息区域，但会引入历史分布滞后；发生 policy shift 时必须重置或降权旧不确定性，保留均匀探索作为覆盖 fallback。

tool-integrated trajectory 的 terminal reward 往往把多个动作混成一个结果。step-level credit 应绑定可观察 effect、状态变化与 verifier receipt，再决定哪些 turn 进入更新。没有外部 verifier 时，一条弱监督分支从某个 turn state 采样多条 future answers，按语义答案聚类，再把各 cluster 的 probability mass 与可靠性估计组成 outcome-potential distribution；相邻 turn 的 potential delta 只表示“后续答案分布是否向更可靠的 cluster 移动”，不是该动作的真实因果 credit。Cluster 边界、future-sampling budget 和 reliability estimator 都会改变信号，开放答案或同义归并不稳时，应回退 terminal outcome 或可执行 subgoal verifier。

当任务允许对中间环境状态执行明确的 acceptance check 时，还可用相邻 turn 的已验证进度变化分配训练 credit，而不是只把进度加到整条轨迹的终局 reward。这样保留最终任务成功作为验收，同时让策略辨认哪一步真正推进了可检验子目标；代价是需要可靠的中间检查器及状态访问，误设检查器会把局部进度变成可投机目标。已有实验只在作者所用的工具环境和模型上表明 turn-level 分配有益，不证明任意开放任务都存在可执行的进度刻度；没有这种刻度时，前述 terminal outcome 或弱监督 potential 分支仍是适用方案。<!-- source-family:SF-2026-ARXIV-2609-27532 -->

局部 layer objective 能减少 end-to-end backprop 成本，但“每层各学各的”会切断任务梯度。一个更具体的折中是在网络中选择 midpoint：任务 loss 的梯度只更新后半段；前半段输出经过轻量 bottleneck head，学习重建 stop-gradient 的输入 embedding state，使早期表示在继续更新时维持与后半段相容的接口。每一步先完成前半段的 auxiliary update，再重新计算并 detach 边界 activation，供后半段执行 task update，从而避免消费 stale boundary。

它缩短 task-induced backward path，却把 midpoint、auxiliary-head revision、重建权重、两阶段更新顺序和端到端 holdout 变成训练状态；feature reconstruction 只约束表示接口，不保证保留所有下游能力。边界表示漂移、跨层协同占主导或额外 forward 抵消收益时，应回退完整 backprop，而不是把局部目标当作无损替代。

<!-- source-family:SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO -->
<!-- source-family:SF-DATA-DEPENDENT-EXPLORATION-FOR-ONLINE-REINFORCEMENT-LEARNING-FROM-HUMAN- -->
<!-- source-family:SF-EVERY-STEP-COUNTS-STEP-LEVEL-CREDIT-ASSIGNMENT-FOR-TOOL-INTEGRATED-TEXT- -->
<!-- source-family:SF-RETHINKING-LOCAL-LEARNING-A-CHEAPER-AND-FASTER-RECIPE-FOR-LLM-POST-TRAIN -->
<!-- source-family:SF-SELF-INDUCED-OUTCOME-POTENTIAL-TURN-LEVEL-CREDIT-ASSIGNMENT-FOR-AGENTS-W -->

### 多路反馈的混合权重应由噪声状态驱动

固定比例混合两类 reward/gradient，在两路信号方差稳定且方向一致时最容易复现；在线训练中，噪声和 disagreement 会随 policy 改变。Feedback controller 可以从梯度方差与方向分歧估计自适应 mixing weight，使低噪声、较一致的信号获得更多控制权。收益是减少固定权重对阶段变化的迟钝，代价是在线统计、额外同步和估计偏差；协方差假设失效或小样本抖动时会产生错误切换，应使用 clipping、慢更新或退回固定比例。exact-v1 只支持论文的 GAC 设定与所测任务，不证明任意 reward source 都可校准。<!-- source-family:SF-2026-ARXIV-2605-26184 -->

### 交互式后训练必须版本化 Simulator 与对话状态

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05415:start -->
### Adversarial Objective 可以从平均风险演进为有界最坏情形

把已生成的攻击样本等权加入训练，在攻击分布稳定、样本质量接近时是透明基线；少数高损失模式被平均值淹没后，模型可能只改善常见攻击。Distributionally robust 分支在经验分布周围定义一个有界的 f-divergence ambiguity set，并对集合内 worst-case reweighting 优化；半径与其 KL-dual 系数拥有 robustness–utility 强度，attack generator 只产生样本，objective owner 决定权重，独立 safety gate 验证未见攻击。

它用更强的 hard-case 压力换来半径选择、样本集中、clean utility 回退和对 attack generator 的依赖；对已观察样本的最坏重加权不等于 unseen-attack guarantee。现有证据只覆盖披露模型、HarmBench 子集与作者攻击器。权重塌缩、utility regression 或 coverage 不足时，应回退等权聚合、扩大攻击族并保留独立 holdout，而不是把高 adversarial loss 当成真实风险全貌。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05415:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06583:start -->
### Flow-model Preference Alignment 也必须显式分配 Trajectory Credit

终点 reward 足以评价短、低维生成，但 flow model 的控制变量是整条 velocity field；只在终点反传会把早期和后期状态的责任混在一起。一条确定性分支把 alignment 写成 pretrained velocity field 上的 optimal control，用 adjoint target 沿轨迹分配 credit，并以 terminal-segment truncation 把计算集中到影响更直接的区段；非二次 regularizer 则表达不同的偏离成本。Reward 只定义目标，adjoint estimator 提供更新 proposal，独立质量与 diversity gate 决定是否发布。

截短减少 VJP 与轨迹成本，也可能漏掉早期决定、依赖 terminal concentration 假设并造成 calibration drift。现有结果只覆盖 SiT-XL/2、FLUX.2-Klein-4B 与作者指标，不证明最佳 truncation、确定性动力学或偏好收益可普遍迁移。早期 credit 或数值稳定性不能闭合时，应增加轨迹范围，回退 full adjoint 或普通 reward/KL fine-tuning。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06583:end -->

静态 preference pair 适合一次性回答，却不能表达多轮行为对未来用户状态的影响。交互式 RL 分支把 user simulator、dialogue state、policy revision 与 reward/judge 共同纳入 rollout contract，再用 GRPO 类更新优化长程行为。它能训练澄清、追问和恢复策略，但新增 simulator bias、judge coupling 与 credit horizon；模拟用户未校准时，应限制为离线 proposal，并以真人或独立环境做 release gate，静态 SFT/RLHF 仍作为保守基线。exact-v1 仅支持论文披露的 simulator、模型和评估，不证明真实用户分布上的长期收益或安全。<!-- source-family:SF-2026-ARXIV-2605-26403 -->

### Tool-call Boundary 可以成为 Turn-level Credit 的状态切面

短推理任务用终局 outcome reward 最直接；当一条轨迹含几十次工具调用时，同一标量会把有用中间动作与最终错误一起惩罚。一个有条件的分支在每次 tool call 前后冻结状态，让独立 value proxy 估计“新 observation 是否提高了正确答案的可预测性”，再用相邻状态的 temporal-difference 变化分配 turn credit，并与终局 reward 合并。

该分支减少稀疏性，却把可靠性依赖转移到 state boundary、reference model 与可验证 gold answer。已知短答案的 search agent 可以使用 log-probability proxy；长代码、多文件 artifact 或开放偏好没有唯一 gold output 时，这个 value 可能失真，应回退 execution-based subgoals、process verifier 或 outcome-only reward。Credit estimator 只生成训练信号，不拥有任务正确性的最终裁决。

<!-- source-family:SF-2026-ARXIV-2607-13988 -->

### 把 KL 系数解释成可检测性预算，而不只是调参旋钮

固定 KL 系数在 reference、reward 与部署 monitor 稳定时简单且可重放；当真正约束变成“policy 改变不能越过外部可检测边界”时，手工 beta 只是在间接猜测。可以把 policy 与序贯检测器写成对策：训练侧提高 reward，monitor 侧判断行为分布是否已可区分，再搜索使二者处于边界的隐含 KL 强度。

这条分支改变的是约束解释，不是证明“难以检测就安全”。它增加 rollout、likelihood 估计与 monitor 校准成本，并继承检测器 misspecification、reference 过期和 oracle 不可得等失败模式。只有 detection contract 可定义且能持续校准时才采用；否则固定 beta、显式 KL/行为 slice 与独立安全 gate 仍是更可审计的基线。论文证据限于披露模型、LoRA+GRPO 与任务设置，不能给出通用系数。

<!-- source-family:SF-2026-ARXIV-2607-26358 -->

## 本章在知识树中的位置

```text
SFT policy
-> candidate rollouts
-> preference pairs
-> Reward Model
-> reward - beta * KL
-> PPO / GRPO policy optimization

preference pairs + reference policy
-> DPO direct optimization
```

本章是 demonstration learning 到 preference optimization 的桥梁。第 32～34 章分别展开具体 objective；第 35 章负责保存 policy、reward/value、optimizer 和 rollout-related state。

### 从局部结果到可执行的系统边界

### Process Reward 必须携带有限证据强度

一个标量 process reward 在 judge 次数固定、噪声可忽略时简单有效；当不同步骤来自不同数量的 continuation 或成功计数，同样的均值可能具有完全不同的证据强度。更完整的状态保留 `(K,N)` 或等价统计，让 reward model 同时输出均值与 concentration，再由独立控制器用于排序、停止或触发修复：

```text
step + continuation outcomes
→ finite count evidence
→ reward mean + concentration
→ risk-aware rank / stop / repair
```

Concentration 只表示给定 continuation generator 与 judge 下的学习证据强度，不是 epistemic truth 或通用置信区间。更多 rollout、存储和校准换来更好的资源分配，也可能产生 confident-wrong early stop；计数不可得、judge 漂移或延迟预算要求固定时，标量 PRM 与固定 Best-of-N 仍是合理基线。

<!-- source-family:SF-2026-ARXIV-2605-15529 -->

<!-- body-source:SF-2026-ARXIV-2606-22600 -->
on-policy distillation 的 token position 并非等权：teacher/student prefix compatibility 与序列位置共同影响 gradient；修正 bias 必须声明 density proxy 和残余 mismatch。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；prefix compatibility 只是 density correction proxy；4B scale、数据与 DPO 小 10× LR/少 40× rows 构成 confound。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

匹配同一数值 learning rate 也不保证 selective-token 与 dense 更新的比较中性：选择器改变参与 loss 的 token 人口，optimizer、clipping 和闭环评分又共同决定真实更新。应先看 arm × rate 的响应，而不是把 raw gradient norm 的差异直接换算成应调整的步长。[受控比较](https://arxiv.org/html/2609.22109v1)中，LoRA 的原始梯度相差 15.5 倍，但按 learning rate 归一化的实际参数位移仅差约 2.2%；冻结初始模型 θ₀ 来评分仍逐轮选择新 token、仍使用当前 student 的 rollout，它只切断直接评分反馈，并非冻结 mask 或消除所有 on-policy 依赖。TV selector 的 n=12 双 rate 交互为 3.79 pp、CI [0.29, 7.30]，而 entropy 和小样本 MATH 未复现该交互；不能推广为所有选择器共享一个效应。

因此评估 selective distillation 时，独立 tuning holdout、匹配搜索预算及更新量日志是工程验收要求，不是作者已经完成公平 per-arm tuning 的证明；初始评分模型副本、额外 forward 与 rate 搜索也要计成本。现有结果限于 Qwen2.5 1.5B/7B、GSM8K、LoRA rank 32、top-5%、AdamW/clip 1、4090 上的 1,536 steps；FullFT 使用 fp32 master 和 A800 80GB、没有 frozen 对照，不能与 LoRA 拼成同条件因果证明。n=3 endpoint 的 Random 5.4 pp（p=.097）与 Full 1.8 pp（p=.26）不支持确定差异或等价，post-hoc 未校正统计和非配对 rescoring 频率观察也不替代因果控制。选择收益在预算匹配后不稳定时，dense 更新仍是有效基线，不能以“同 LR”宣告任一分支优越。<!-- source-family:SF-2026-ARXIV-2609-22109 -->

<!-- body-source:SF-2026-ARXIV-2606-23740 -->
offline reasoning training 的方法差异要同时看 weight-space trajectory、data/step/LR matching 与功能结果；几何分离若训练预算不匹配不能归因于 objective。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；单 seed/domain/checkpoint，且 DPO 用 10× smaller LR 与 40× fewer rows，构成强 confound；不能形成 objective superiority 结论。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

偏好训练最初把人工比较压缩成固定 Reward Model；当 policy 持续变化后，静态 rubric 会逐渐失去区分度，feedback 的 rater identity、产生时间和适用 domain 也会改变 reward 的含义。演进方向因此是把 preference、rubric/spec、reward model、policy revision 与独立 evaluator 分离版本，而不是让 policy 与 judge 在同一闭环中共同漂移。

动态 rubric、spec learning 或 on-policy distillation可以提高适应性，却会放大 reward hacking、judge correlation、density mismatch 与评价成本。它们必须通过 frozen holdout、独立 outcome evidence 和 rollback gate；反馈不足或评估失去区分力时，回退静态 rubric、SFT 或人工 adjudication。几何差异只有在 data、step 和 learning rate 匹配时才可归因于 objective。

## 自检问题

1. 为什么 preference comparison 能表达 SFT demonstration 缺少的信息？
2. RLHF pipeline 中至少有哪些模型状态？
3. Bradley-Terry model 为什么只约束 reward difference？
4. 小例子的 reward score 为什么不是绝对质量？
5. Candidate policy version 为什么影响 preference data？
6. KL penalty 约束什么，又不能保证什么？
7. Reward hacking 为什么比普通分类误差更危险？
8. Sequence reward 怎样产生 token-level credit assignment 问题？
9. RLHF rollout 为什么会把推理成本带入训练？
10. PPO、GRPO、DPO 在 pipeline 中分别替换哪一部分？
11. Verifiable self-play 为什么仍需在 task diversity 与 verification reliability 之间取舍？
12. Preference optimization 为什么必然改变条件输出分布，而平均 KL 又为什么不能证明每个 slice 都被保留？
13. Latent capability、elicited behavior 与 system capability 为什么不能由一次 RLHF 结果互相替代？

## 小结

RLHF 把相对偏好拟合为 reward，再在 reference policy 约束下优化生成策略。它比单一 demonstration 更能表达“哪个回答更好”，也让训练目标依赖标注 process、Reward Model 泛化和 policy rollout distribution。

这条 pipeline 的核心风险是代理目标：policy 会优化 Reward Model 能看见的东西，而不是自动优化所有真实需求。异步样本 freshness 与 prefix-aware credit 进一步说明，监督信号还必须携带 policy revision 和因果归属。可靠 RLHF 必须把 reward、KL、独立 Evaluation、数据 provenance 和多模型训练状态放进同一个控制闭环。

当 task generator、validator 与 policy 一同进入反馈循环时，curriculum 本身也成为需要版本化和独立评估的训练状态；可自动验证不等于任务分布自然充分。

### Alignment Actuator 可以从参数更新迁到运行时状态

offline preference training 把行为写入权重，适合稳定目标，却难以针对请求快速刷新。RAG-Pref 把 preferred 与
dispreferred evidence 在推理时检索出来，形成 contrastive alignment signal；retriever 只拥有本次 steering proposal，
安全 policy 与最终 evaluator 仍决定是否提交回答。它提高可更新性，也引入检索污染、对抗文档、延迟与 refusal 误触发；
证据缺失或检索失校准时，应回退冻结权重策略、确定性 guardrail 或人工升级。论文结果不证明未测攻击下的生产安全。

<!-- source-family:SF-2026-ARXIV-2605-11217 -->

更进一步，独立 value module 可以通过 bridge tokens 把 value state 注入 backbone，而不修改全部主模型参数。价值模块
拥有可刷新的偏好表示，bridge 只传递条件，backbone 生成候选；这降低重训练范围，却增加约 50% 的作者设置 latency、
单维 value 表达限制与文化偏差。目标稳定或在线成本敏感时，直接 SFT/RLHF 仍更合理；现有证据只覆盖四个 backbones、
公开 safety data 与三次随机种子。

<!-- source-family:SF-2026-ARXIV-2605-11712 -->

视觉 flow policy 还暴露了另一条边界：固定的 policy entropy 可能保持不变，而可感知图像多样性已经坍缩。perceptual
entropy 因而可作为独立控制量，约束离散 reasoning reward 与连续视觉 trajectory reward 的共同更新；它是 sensor，不是
质量真值。额外 embedding/evaluator 会带来偏差和计算，指标相关性失效时应回退多样性切片、人工评测或冻结更新。
现有证据限 FLUX.dev、SD3.5-Medium 与作者披露的 rewards。

<!-- source-family:SF-2026-ARXIV-2605-12112 -->

### 成功率优化会压缩行为 Mode，Diversity 需要独立状态

生成式 policy 只追求单一成功 reward 时，Reverse KL 式更新可能收缩到一条高分路径。轨迹级 mode discovery 可以提出当前行为分支，再用 mutual-information regularizer 在同一更新中保护已发现 mode；task reward 仍拥有成功方向，mode inference 不拥有任务真值。保留多样性会与单一 optimum 竞争，也引入 mode alias、过度分裂和归因漂移。mode 证据不稳或部署只需要一条可靠路径时，应回退常规 RL、entropy/KL 约束和独立 coverage evaluation。exact-v1 只覆盖披露机器人任务与 policy，不保证真实安全或 mode 完备。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11387 -->

### 多模态 Reward 需要按 Branch 与 Region 分配 Credit

joint audio-video diffusion 使用一个 global advantage，容易混合不一致目标、跨 modality gradient 和稀疏同步区域。条件分支可让各 reward channel 只为对应 modality/layer/region 提供 credit，cross-modal layers 保留共享梯度，region weight 表示 decision density，而不是让单一标量拥有全部目标。分权减少 gradient interference，却增加 reward calibration、routing 和 gradient surgery complexity，错误归因可能牺牲另一模态。指标冲突或路由不稳时，应回退 global reward 加 conservative KL、冻结受影响 branch，或分阶段训练后联合验收。exact-v1 只支持披露模型和 evaluator，不证明跨架构通用、无 reward hacking 或真实同步质量。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12480 -->

### 偏好目标位置与声学监督位置需要分开

当同一序列交替生成文字与声学 token，主要反馈又衡量文本语义时，把 preference loss 铺给所有位置会混合不同监督职责。一个条件分支让 GRPO likelihood 只读取 text tokens，同时用 all-token SFT 保留声学分布 anchor；这与前面的 modality branch 路由不同，分开的是偏好目标的支持集与保留原能力的监督位置。Loss mask 不会冻结共享参数，也不证明 audio 行为已被隔离，仍须同时验收语义、音色与表达质量；第33章拥有具体组优势更新，本节只界定目标与监督责任。

两类 loss 可固定混合，也可用归一 rollout reward variance、是否存在有效高奖励样本及 EMA 调节比例，减少单批抖动；这些是信号可用性的 proxy，不是 reward 真值或声学安全概率。`arXiv:2604.14932v1` 的 WavAlign 在 VITA/KimiAudio、13.5k 训练样本与作者 evaluator 下，scope×mix 消融支持局部选择，但 style 仍有相对 SFT 的退步。动态混合新增采样、SFT anchor 与系数状态成本，架构和评价差异不能合成通用声学稳定保证；反馈稀少、声学回归或系数漂移时，固定混合、分阶段训练或原 SFT 路线继续成立。

<!-- source-family:SF-2026-ARXIV-2604-14932 -->

### 个性化 Agent RL 必须把通用能力与个人偏好分账

<!-- semantic-body-binding:SF-2026-ARXIV-2605-23382:start -->
把所有用户反馈合成一个 reward，在偏好近似同质时最省状态；个性化约束出现后，generic reward、personal reward、user anchor 与 preference-aligned skill graph 必须分别版本化。个人记忆只能调整可撤销的 policy proposal，不能覆盖平台安全或通用能力 Gate。

分账可以减少平均偏好对少数用户的抹平，却会带来稀疏反馈、身份漂移、隐私与过拟合风险。exact-v1 只支持作者任务与用户设置，不证明 skill graph 是稳定人格模型；个人证据不足、冲突或回归失败时，应回退通用 policy，并要求显式确认或重新收集偏好。arXiv:2605.23382v1
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23382:end -->

### Alignment Midtraining 的规则保留需要单独 Stress Test

在中期训练加入安全/行为规则，可以比末端少量 post-training 更早塑造表示；但随后少量冲突数据就可能擦除这类行为，而总体 loss 和通用能力仍看似正常。训练 lifecycle 应把 rule retention 作为独立状态：冻结规则版本与冲突强度，沿后续 checkpoint 持续评价，并把“当前遵从”与“对后续训练扰动的稳定性”分开。<!-- source-family:SF-2026-ARXIV-2609-20412 -->

持续 stress test 增加 checkpoint、对抗数据和安全评估成本，也可能过拟合已知规则表达。作者实验不证明所有 alignment 都脆弱或 midtraining 无效；稳定性不足时，应加强数据 rehearsal、post-training/release gate 与运行时 guardrail，而不是仅依赖更早注入规则。

### Distillation Credit Horizon 要与 Sequence Reward 对齐

On-policy distillation 若逐 token 追 teacher，却用 sequence-level reward 判断成败，局部 imitation signal 可能强化最终任务无关的早期动作。Reward-compatible temporal credit 应把终局 evidence 沿可解释 horizon 分配回 student trajectory，并记录 teacher policy、rollout revision 与 mixing rule；它是普通 token KD 的条件分支，不是无条件替代。<!-- source-family:SF-2026-ARXIV-2609-16937 -->

更长 credit horizon 增加方差和归因偏差，过强 mixing 又会抹去 token-level 学习。环境 reward 稀疏或 attribution 不稳时，应回退 sequence-level filtering、短 horizon 或独立 verifier；理论与作者实验不给出通用 mixing 系数。

## Review notes

- `SF-2026-ARXIV-2603-10279` — Daily补查 `2026-03-13`；[exact-v1](https://arxiv.org/html/2603.10279v1) §3–7/A.1–A.3必要范围，2+1+2=5。固定context噪声半径/temperature退化资格与共享参数省Z投影断点的实际差额深入；理想单步界不授finite SFT、MDP、无hacking或无偏用户价值，人口与费用/原BC回退近文。root非证据作者实际原证、Ch31邻接/PRE通过后窄写两段；保留原人类行为→人群模拟连贯段，新增置其后。mar13_supplement作为非Books写入者实际顺读348–392、新360/362及本注，回核§4/A.2–A.3及训练、MDP和评价边界，POST通过；root核回执并释放窄锁。未核代码、图像点值或复现，不授日级验收。

- `SF-2026-ARXIV-2603-10165` — 2026-03-13 补查；[OpenClaw-RL exact-v1](https://arxiv.org/html/2603.10165v1) §4.1–4.4/5.1–5.4、Appendix A/C/D。只采用同一自产 action 的 teacher-only posthoc hint、原 prompt student 与 scalar/hint 不同准入人口；不采用 v1 主文 current-logprob 与伪代码 stored-old-logprob 未统一的精确实现，也不借最长 hint 认证正确性。模拟用户与同源评估、GUI训练集、额外 PRM/teacher 成本和部署去 hint 验收保留；无 zero-coordination、安全或普遍泛化保证。mar13_admission_review 实际必要 Source/具体 owner 两段 PRE、root 实际原证/局部与相邻 Ch30/32 回读后窄写；mar13_admission_review 已实际读新两段、完整878～925邻接与本人末注，非写入者 POST通过，窄锁释放，不授日级完成。未核代码或复现。

- `SF-2026-ARXIV-2603-09160` — Daily `2026-03-12`补查；[exact-v1](https://arxiv.org/html/2603.09160v1) 必要完整§3/4、B/E/F/H及Tables1/5/6。2+1+2=5，committee→初始缺口rubric→冻结文本judge的两阶段接口与覆盖盲区差额深入；阈值3/2冲突、modeljudge非人工真值、retention反退与完整费用近正文。root实际必要Source/date/逐字PRE通过并授两段与本注窄锁，作者已实际写入并顺读完整局部邻接与本注，root非writer实际顺读245–280完整局部、新257/259及本1219注并回对必要原证，actualPOST通过，窄锁释放；未核全部曲线、实现/复现或完整SLO，不授DAY。

- `SF-2026-ARXIV-2601-05882` — Daily `2026-01-13` 增量；[exact-v1](https://arxiv.org/html/2601.05882v1) §3.1–3.3/4/5/6；objective×target两轴与teacher pseudo配对；3×T.7/win-diversity/evaluator近文；2+2+2=6，具体差额深入。jan10_books_audit必要原证/actual owner PRE通过、root授窄锁；作者完整邻接已顺读，root非Books写入者已实际读正文/完整邻接/自身末注，POST PASS；窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2601-04954`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04954v1) §2–5/Table1–4、AppD–F必要定义/消融。采用pilot-ever-positive与单soft约束这一人口/监督粒度联动；不采用普遍precision胜diversity、attention因果或总成本下降保证。7B/32B与64 Ascend910b等条件只按原文范围；完整精度/32B预算/独立重复 Not Disclosed。必要证据与实际owner独立PRE完成，root窄写，jan10_books_audit 非写入者实际正文/完整局部邻接/自身末注 POST通过（本日 post-audit-20261007.md §5）；未核实现/复现，不授日级 Gate。

- `SF-2026-ARXIV-2601-04670`（Experimental）：Daily `2026-01-10`补查；[exact-v1](https://arxiv.org/html/2601.04670v1) §4.3/§5.1–5.4、B.1–B.3。采用 classifier-first→full-RL 的参数权限分阶段及额外 epoch 成本，不采用 A.1 Eq23 log/log 与后续 log-ratio 求导冲突的一般 KL 定理或熵普降保证。非写入者 `audit_supp_jan06`必要证据/实际owner差额PRE，root定点核原文与成本邻接后写两段；该复核者于2026-10-07 15:42实际顺读正文、完整邻接与本注，写后复核通过。未核代码/复现，非日级完成。

- `SF-2026-ARXIV-2602-22554` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22554v1)，跨语linear低秩edit/softutilitypenalty与译者judge/语言utility反侧。2+1+2=5，具体owner差额深入；限制、反侧、完整费用与原分支回退近正文。root实际必要原源/owner PRE通过并授单段窄lease；作者正文/完整邻接/自身末注已顺读，root非作者实际正文/完整邻接/自身末注POST通过。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-13840` — Daily `2026-02-18`；[PrivAct exact-v1](https://arxiv.org/html/2602.13840v1) §3.3/Eq1、必要§4与C.1/C.2。2+1+2=5，具体reward形状差额深入；L>0时H亦增负项/cap，L=0才正reward。judge-zero非privacyzero，leak@K人口、394/99split与局部helpfulness反侧保留，不授gradient稳定或严格执行。root必要原源/actual owner PRE通过并授单文件窄锁；root实际正文、完整邻接与末注非作者POST通过，锁释放。未复现或核代码，非日级Gate。

- `SF-2025-OPENAI-CONFESSIONS`（Experimental）：[2025-12-03 官方 Blog](https://openai.com/index/how-confessions-can-keep-language-models-honest/)的 How confessions work、What we learned、Limitations。只采用主答复与自报的 reward channel 分离及诊断边界；不把 joint bad-and-no-confession 概率写成条件检出率，不采安全保证或未公开训练实现。root 实际读取必要原文、Ch31 Solver/Auditor→policy objective 与相邻 Ch30/32 后窄写两段；非写入者 Mill（agent ID `01a0fc18-6d14-7b60-9ba1-b6b579aaef3e`）2026-10-02 实际重读官方 Blog 核心、两段及前后衔接、Ch30 更新表示与 Ch32 token credit 后 POST 通过：reward/output 信用分离不授共享参数隔离，诊断不替代独立验收。后来的 arXiv v1 为窗外限定证据，不反填成当时公开正文；未运行或复现实验。

- `SF-2026-ARXIV-2604-15557`（Experimental）：[官方 exact-v1](https://arxiv.org/html/2604.15557v1) §3.2–3.5、§4.2–4.3、§5 与必要 Appendix D/F/H/J。只采用“任意 probe 可读、当前 output head 对齐、真实 steering 生效”三者需分账的选层边界。作者的 logit lens 使用最终 LayerNorm+unembedding 的单 token top-1，残差 MLP probe 的 80/20 拆分只显示该校正可读；trained probe 各层高分类率而早层 steering 近零，是“可读不等可控”的受限反证。主相关按层/概念家族算，depth 与层间相关未完全消除；个别 target 支持很小、最佳层选择和跨模型拓展不等 held-out 生产 controller。Mamba/RWKV 仅复测表征读出，没有做 steering；未证明通用内部三阶段或任何概念不可干预。root 完成必要来源→Ch31 真实缺口的窄写入，非作者写后复核 PASS（`papers/2026/04/_sources/daily-20260420/V3_APR20_15557_CH31_WRITE_AFTER_INDEPENDENT.md`）；04/20 整日 Gate 未通过，未复现实验。

- `SF-2026-ARXIV-2604-19018`（Experimental）：[A-LQR exact-v1](https://arxiv.org/html/2604.19018v1) §4.1–4.3/Eq19、§7/Tables1–2；采用按层局部 Jacobian/Riccati gain 与当前 feature error 的在线反馈，不采未来 token 最优规划、feature setpoint 真值或通用安全保证。Gemma toxicity/PPL 取舍、RTX4090 throughput 及 gain 驻留/局部漂移要同验。root 已完成必要 source→Ch31 采用与[实际正文写后非作者复核](../../papers/2026/04/_sources/daily-20260422/V3_ROOT_19018_WRITE_AFTER.md)，未复现实验。

- `SF-2026-ARXIV-2604-20904`（Experimental）：[Normative Simulacra v1](https://arxiv.org/html/2604.20904v1)，Daily 2026-04-24；§3.1–3.5、§4.1–4.2/§5、A.1/A.3/A.4。采用同 completion 在正确/错误 norm context 下的条件 reward 训练桥，不采规范真值或法律遵从保证。HIPAA 负例、双 context 成本及 Qwen3-32B/Qwen2.5-32B judge 披露冲突保留；6分保护/缺口深入。apr20及root必要 source→实际 owner 采用通过；实际正文与相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-15149` — [LLMs Gaming Verifiers v1](https://arxiv.org/html/2604.15149v1)，Daily `2026-04-17`。采用 §3–4/Table1/AppendixC 的同一H原实例/保义双射改名双验收；保义前提、两run无重复seed、presumed标签及零观察非保证保留。复用 `V3_ORDINARY_TEN_TWO_INDEPENDENT_AUDIT.md` §10 有效必要source→owner PASS；本次root顺读真实正文及相邻段写后PASS；未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-14932` — [WavAlign v1](https://arxiv.org/html/2604.14932v1)，Daily `2026-04-17`。采用 §3.1–3.4/4.1–4.3/Table1–3 的text-only preference与all-token声学anchor、rollout统计/EMA混合；mask非共享参数隔离、proxy非truth及style退步保留。复用本日 `v3-reopen-notes.md` 具名apr01必要原文/真实Ch31 owner PASS；本次root顺读真实正文及相邻段写后PASS；未复现实验，不预支日级Gate。

- `SF-2026-ARXIV-2604-09748`（Status: Experimental）：[精确 v1](https://arxiv.org/html/2604.09748v1) §3.2、§4.1–4.3、§5.1/Table1、§6.1–6.3 支持不改 verifier 的 prompt 污染与终局验证覆盖漏洞；正文只采用 checked span / 完整行为分责，不采用普遍攻击概率。作者以 shadow/dual-verification 选择 top200 样本，不是随机剂量；GRPO/verl、所测 Qwen/Mistral/Llama 及任务受限，CA 为非触发安全而不是任务 accuracy，PRR/PDR 另依各表口径，Table1 的 CA 也有退步。硬件、精度、部署长度/并发/SLO 未在采用的必要设置披露；未运行代码或复现实验。apr02 提案 source/owner 独立通过，真实两段写后待非作者验收。

- ConsistRM（Status: Experimental，SF-2026-ARXIV-2604-07484）：[官方 PDF v1](https://arxiv.org/pdf/2604.07484v1) §3.2–3.4 Eq2–8、§4/Table1、§5.2–5.3、Appendix A.2–A.4。采用 per-pair 历史 pseudo-label 与当前投票共同构造 target 的窄机制；正文 Eq4 将 n 项除以 n−1，与 Algorithm1 的1/n及n=0置0不一致，不抄该公式或称精确实现已验证。sign 零点不等一般低置信区间。AppA.2 使用HelpSteer3真实标签排除八rollout全对项，故不采“全流程无human annotation”headline。Qwen3、四epochs/global batch64、八rollout、prompt4096/response1024、八A800；precision、部署并发/SLO未披露。五benchmark均值不覆盖所有切片，critique/shared-error和历史漂移保留，output长度非latency。作者侧必要源及实际两段已核，待 root 非作者写后复核；未运行实现或复现实验。

- `SF-2026-ARXIV-2605-05750`（Status: Experimental）：exact-v1 支持作者在 HealthBench、GPQA、tool-calling、Qwen2.5
  与 17/2 reward channels 下的 risk-sensitive aggregation 分支；`k`、group size、schedule 与 noise sensitivity 限制外推，
  不证明 SoftMin 可替代 hard safety/schema gate。Primary: https://arxiv.org/html/2605.05750v1
- `SF-2026-ARXIV-2605-06036`（Status: Experimental）：exact-v1 支持三套 preference data、7B–72B 模型和作者 judge 下的
  partial-OT admission；理论只覆盖 selected subset，`O(N²)` 与 systematic/adversarial noise 未解决。
  Primary: https://arxiv.org/html/2605.06036v1

- `SF-2026-ARXIV-2602-23008`（Status: Experimental）：exact-v1 的 §4.1～4.2 定义 self-generated memory 与 hybrid on/off-policy optimization，§6.1～6.3 和附录 D/F/G 报告作者任务、消融与成本，Appendix C 解释 importance ratios，§7/Ethics/Reproducibility 不证明 tips 忠实、跨环境迁移或任意 replay mixture 无偏。https://arxiv.org/html/2602.23008v1

- `SF-2026-ARXIV-2602-12691`（Status: Experimental）：exact-v1 的 §IV（尤其 §IV-A～B）定义 VLA action-level off-policy critic 与 advantage-weighted policy improvement，§V 给出论文任务、比较与消融，§VI 仅支持作者设置中的结论；它不证明任意 behavior-policy mixture、不可恢复 propensity 或开放物理环境中的 credit 都可被无偏估计。https://arxiv.org/html/2602.12691v1

- **APPA（arXiv:2604.04261v1；Status: Experimental）**：exact-v1 支持历史 group reward 驱动的 federated PPO weighting，以及 GLOBALQA/OQA、Gemma 2 2B、Llama 3.2 3B、Qwen3 0.6B 设置中的 fairness/alignment trade-off；不证明未测人群或真实偏好协议。https://arxiv.org/abs/2604.04261v1

- `SF-2026-ARXIV-2606-22600` — primary `arXiv:2606.22600v1`；Method=`arXiv:2606.22600v1 §3 Position-Bias Analysis; §4 Proposed Correction`；Evaluation=`arXiv:2606.22600v1 §5 Experiments; Appendix C Protocol`；Non-proof=`arXiv:2606.22600v1 Appendix E Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-23740` — primary `arXiv:2606.23740v1`；Method=`arXiv:2606.23740v1 §2 Experimental Setup`；Evaluation=`arXiv:2606.23740v1 §3 Results`；Non-proof=`arXiv:2606.23740v1 §4 Discussion; Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Ring-Zero（large-scale RL numerical identity 与 context-parallel communication；Status: Experimental）:
  https://arxiv.org/abs/2607.12395v1

本章只定义 preference data、Reward Model、KL-constrained policy objective 与系统 pipeline。PPO clipping/value、GRPO group advantage、DPO closed-form pair loss 分别留给第 32～34 章，避免重复算法推导。本轮审计进一步把 preference update 对条件输出分布的重写，与 latent capability、可观察行为和 system capability 三层边界分开；平均 KL 仍只是更新幅度信号，不是逐切片能力保持证明。

Primary-source 校验入口：

- Paul F. Christiano et al., "Deep Reinforcement Learning from Human Preferences", 2017: https://arxiv.org/abs/1706.03741
- Nisan Stiennon et al., "Learning to summarize from human feedback", 2020: https://arxiv.org/abs/2009.01325
- Long Ouyang et al., "Training language models to follow instructions with human feedback", 2022: https://arxiv.org/abs/2203.02155
- Siyuan Huang et al., "Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills", 2026, `Status: Experimental`: https://arxiv.org/abs/2607.22529
- Real-Time Aligned Reward Model（policy-conditioned RM head；Status: Experimental）:
  https://arxiv.org/abs/2601.22664
- Efficient Exploration at Scale（uncertainty-directed feedback acquisition；Status: Experimental）:
  https://arxiv.org/abs/2603.17378
- Reasoning over Mathematical Objects（policy-conditioned reasoning judge；Status: Experimental）:
  https://arxiv.org/abs/2603.18886
- DSPA（Status: Experimental；prompt-conditional、token-active preference steering）:
  https://arxiv.org/abs/2603.21461

### 2026-06-26 source-specific Review notes

- `SF-2026-ARXIV-2606-27578` — PEBS: Per-rater Empirical-Bayes Shrinkage for RLHF Reward-Model Calibration; primary=`arXiv:2606.27578v1`; Method=`arXiv:2606.27578v1 — §2 Method; §Base-model training details.`; Evaluation=`arXiv:2606.27578v1 — §2.3 PRISM setup and base reward model; §3 Experiments`; counterevidence/non-proof locator=`arXiv:2606.27578v1 — §3.9 Ablations and failure cases; §4 Discussion; §5 Limitations`; claim boundary=证据来自 PRISM 与 PluriHarms 上的 held-out affine per-rater calibration；RMSE 改善不证明非线性/adversarial rater、极稀疏标注或 online rater drift 下仍校准。; fallback=校准或 delay/mass 假设失效时回到总体 calibrator 或 bounded synchronous update。
- `SF-2026-ARXIV-2606-27580` — Retroactive Advantage Correction: Closed-Form V-Trace Bias Correction for Delay-Aware RLHF; primary=`arXiv:2606.27580v1`; Method=`arXiv:2606.27580v1 — §2 Method: Retroactive Advantage Correction`; Evaluation=`arXiv:2606.27580v1 — §Setup.; §K = 2 K{=}2 result and cost-quality Pareto.; §Scope of the closed-form result.`; counterevidence/non-proof locator=`arXiv:2606.27580v1 — §4 Conclusion; §Appendix E Limitations and Discussion; §Background and discussion.`; claim boundary=无偏结论要求 clipped importance ratio 无偏且 delay kernel reinject 全部质量，实验为 tabular MDP proof-of-concept；最高 47.9× bias reduction 不证明 large-scale RLHF 稳定性或生产 pending-queue failure 已解决。; fallback=校准或 delay/mass 假设失效时回到总体 calibrator 或 bounded synchronous update。

### Daily integration evidence trace

- `2026-05-05 / SF-2026-ARXIV-2605-01831` — exact-v1 `arXiv:2605.01831v1`；正文吸收 explicit preference contract 与 paraphrase-consistency evaluation，不把 synthetic benchmark 外推到真实用户或下游 RL。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-23038` — primary `arXiv:2606.23038v1`; Method=`arXiv:2606.23038v1 — §4.1 Dual-LoRA Architecture; §4.4 Co-Evolutionary Training; §Appendix A EvoRubrics Algorithm`; Evaluation=`arXiv:2606.23038v1 — §2.2 Dynamic Rubrics and Adaptive Evaluation; §Appendix C Evaluation Details; §C.1 Policy LLM Evaluation`; non-proof=`arXiv:2606.23038v1 — §6 Conclusions and Future Work; §E.3 Discussion`; fallback=该 family 的 failure pressure 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 披露的 evaluation signal 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-24004` — primary `arXiv:2606.24004v1`; Method=`arXiv:2606.24004v1 — §4 Spec Learning Framework; §4.1 Selection Method; §4.4 Judge protocol and selection`; Evaluation=`arXiv:2606.24004v1 — §5 Results; §B Statistical robustness; §C Judge calibration`; non-proof=`arXiv:2606.24004v1 — §6 Discussion; §7 Limitations; §8 Conclusions and Future Work`; fallback=该 family 的 failure pressure 是：Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 披露的 evaluation signal 是：We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Daily Books delta trace（2026-05—08）

<!-- daily-books-trace:SF-2026-ARXIV-2605-05750:start -->
- `SF-2026-ARXIV-2605-05750` — Daily `2026-05-08`；primary `arXiv:2605.05750v1`；Books review `books-review:SF-2026-ARXIV-2605-05750`。

  **已吸收的语义增量：** 将可补偿的多目标平均、risk-sensitive bottleneck 聚合与不可补偿的 deterministic hard gate 分成不同权限层。
<!-- daily-books-trace:SF-2026-ARXIV-2605-05750:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2605-06036:start -->
- `SF-2026-ARXIV-2605-06036` — Daily `2026-05-08`；primary `arXiv:2605.06036v1`；Books review `books-review:SF-2026-ARXIV-2605-06036`。

  **已吸收的语义增量：** Preference admission 允许拒绝与语义一致性冲突的 noisy mass，并要求保存原始 pair、selection mask、模型版本与 dispute path。
<!-- daily-books-trace:SF-2026-ARXIV-2605-06036:end -->

<!-- daily-books-trace:SF-EVALSTOP:start -->
- `SF-EVALSTOP` — Daily `2026-06-04`；primary `arXiv:2606.04145v1`；正文锚点“训练停止不能只看 Training Loss 或 Reward Model Score”。
<!-- daily-books-trace:SF-EVALSTOP:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09932:start -->
- `SF-2026-ARXIV-2606-09932` — Daily `2026-06-08`；primary `arXiv:2606.09932v1`；Books review `books-review:SF-2026-ARXIV-2606-09932`。

  **已吸收的语义增量：** 过度 SFT 会耗尽后续 RL 的 policy plasticity；SFT-to-RL handoff 应以可学习性而非只看 SFT checkpoint accuracy 作为 release 条件。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09932:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09711:start -->
- `SF-2026-ARXIV-2606-09711` — Daily `2026-06-09`；primary `arXiv:2606.09711v1`；Books review `books-review:SF-2026-ARXIV-2606-09711`。

  **已吸收的语义增量：** reward-hacking 监测需观察显性 exploit 之前形成的 proxy-reward internalization：正确性判断、proxy acceptance 预测与 proxy-gold gap 推理三种状态。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09711:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18322:start -->
- `SF-2026-ARXIV-2606-18322` — Daily `2026-06-17`；primary `arXiv:2606.18322v1`；Books review `books-review:SF-2026-ARXIV-2606-18322`。

  **已吸收的语义增量：** SAE feature clamp/ablation 不能被当作行为控制 complete；residual stream 会在后续层恢复被压制行为，需做 post-intervention trajectory 与 residual recovery audit。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18322:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18383:start -->
- `SF-2026-ARXIV-2606-18383` — Daily `2026-06-17`；primary `arXiv:2606.18383v1`；Books review `books-review:SF-2026-ARXIV-2606-18383`。

  **已吸收的语义增量：** SAE 只有在 proxy risk、reconstruction gap、concept mismatch 与 proxy complexity 共同受控时才能支撑干预结论；单独 sparsity/reconstruction score不足以认证 fidelity。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18383:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-20002:start -->
- `SF-2026-ARXIV-2606-20002` — Daily `2026-06-19`；primary `arXiv:2606.20002v1`；Books review `books-review:SF-2026-ARXIV-2606-20002`。

  **已吸收的语义增量：** `Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Generalization Via Reinforcement Learning` 路由到 `TRAIN-RLHF`：Connect-the-Dots 用跨 domain、跨 lifecycle 的 RL trajectory 把短任务 reward 改为长期 agent state transition 信号；trainer 拥有 curriculum、reward 与 checkpoint selection，旧单域 SFT/RL 作为稳定初始化。代价是跨域 reward leakage 和 credit assignment，失败时需回退到分域训练/验证。
<!-- daily-books-trace:SF-2026-ARXIV-2606-20002:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21795:start -->
- `SF-2026-ARXIV-2606-21795` — Daily `2026-06-20`；primary `arXiv:2606.21795v1`；Books review `books-review:SF-2026-ARXIV-2606-21795`。

  **已吸收的语义增量：** reward clustering 应把异质 reward mode 分开优化并保存 cluster identity，聚合 scalar reward 会隐藏冲突偏好与 hacking
<!-- daily-books-trace:SF-2026-ARXIV-2606-21795:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-12395:start -->
- `SF-2026-ARXIV-2607-12395` — Daily `2026-07-15`；primary `arXiv:2607.12395v1`；Books review `books-review:SF-2026-ARXIV-2607-12395`。

  **已吸收的语义增量：** 新增证据边界：The pipeline combines clipped importance sampling, training-engine numerator correction, KL control, mixed-precision safeguards and context-parallel communication optimization; staged self-distillation/RL and length-conditioned modes separate discovery, sharpening and adaptive inference depth. 该 delta 已进入 `books/part-04-training-system/31-rlhf.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-12395:end -->

- `SF-2026-ARXIV-2512-25023` — Daily `2026-01-02`；[ResponseRank exact-v1](https://arxiv.org/html/2512.25023v1) §2/3/5/8、Appendix D.1–D.3。6分针对 preference-strength measurement 的具体缺口深入受影响证据，只采用 utility-difference rank/zero anchor、局部单调假设与 metadata 资源分账。MultiPref 有限标注、RR-RT失败/Stated小增益不显著/Random不迁移，Agree使用四票；Llama3.1-8B fullFT/BF16，BT与RR部分最佳epoch不同，尚未验证 downstream LLM-policy收益。未复现实验；root必要原源与owner写前核通过，root实际正文/前后邻接及末注写后非作者复核通过。

- `SF-2026-ARXIV-2512-23816` — Daily `2026-01-02`；[Improved Bounds for Private and Robust Alignment exact-v1](https://arxiv.org/html/2512.23816v1) §2.1–2.4、§3.1–3.2、§4–5及B.1–B.2/C.1相关归约。只采用二元label channel、private likelihood、缩放与CTL/LTC顺序的条件边界；有限realizable/ bounded reward、离线concentrability及在线coverability/oblivious条件不授文本隐私、自适应污染或神经argmin保证。8分必要理论审阅，不要求硬件benchmark，未复现；root必要原源与owner写前核通过，root实际正文/前后邻接及末注写后非作者复核通过。

- `SF-2026-ARXIV-2512-24693` — Daily `2026-01-02`；[MUSIC exact-v1](https://arxiv.org/html/2512.24693v1) Alg1、§3.1–3.4、§4.1–4.3及§6。5分因trajectory-pair identity缺口深入受影响机制：chosen/rejected用户分支各随自身history生成，terminalhidden BT非toolstep信用，固定脚本/反事实/独立用户评价各有不同约束。Gemini1.5Pro兼simulator/judge、Gemma2-9B和追加多轮数据不授真实用户/长程可靠或预算匹配归因；硬件/precision/完整生成评价成本未披露，未复现。root必要原源与owner写前核通过，实际正文、前后邻接及末注已root非作者写后复核通过，不代表日级Gate。
- `SF-2026-ARXIV-2512-24146` — Daily `2026-01-02`；[D2Align exact-v1](https://arxiv.org/html/2512.24146v1) §4.2/Eq5–10、§5/Tables1–2、B.2与D.1–D.2。6分instrument/参数权限gap深入，限冻结G学条件方向、冻结方向再学G；有限blind human/population及非单调边界保留，不授全偏好纠正、mode覆盖或20步即总训练便宜。未运行代码；root必要原源/owner及实际正文、邻接与末注非作者写后复核通过。
- `SF-2026-ARXIV-2512-24138` — Daily `2026-01-02`；[GARDO exact-v1](https://arxiv.org/html/2512.24138v1) §4.1–4.3/Eq7–8、§5.1–5.2/Tables1–2及A.1。6分因selected-population/reference双身份具体缺口深入受影响机制；aux与proxy批内win-rate差不是真实human uncertainty，hard-reset局部KL非累计base界，部分aux兼evaluation非独立；LoRA alpha/r字段冲突保原限制，不采用数值配方、全硬件或无reward-hacking保证。未运行代码；root必要原源/owner及实际正文、邻接与末注非作者写后复核通过。

- `SF-2026-ARXIV-2601-03468` — Daily `2026-01-09`；[Understanding Reward Hacking in Text-to-Image RL exact-v1](https://arxiv.org/html/2601.03468v1) §3.2–3.3/§4、补充§6 APO与§7.2–7.4/Table7。原6分因ensemble共同遗漏局部结构的具体gap深入受影响证据；同prompt人判paired诊断支持有限盲区，tie/排序和未优化维度分账，APO视觉detector非校准真值，诊断对与其优化人口独立切分未明确，不采用Table2外样本准确率。Janus-Pro-1B、T2I-R1数据及有限reward对照，不外推所有模型/ensemble或质量全维保持；完整硬件/precision/concurrency与额外调用预算未披露，未复现。root必要原源与owner写前复核通过，实际正文、前后衔接及源注已root非作者写后复核通过，不代表日级Gate。

- `SF-2026-ARXIV-2601-08777` — Daily `2026-01-15`；[Asymptotic Universal Alignment exact-v1](https://arxiv.org/html/2601.08777v1) Property1、NLHF反例、Theorem2/3、Prop5/6。2+2+3=7，仅采用有限响应/符合假设人口的k-dependent集合偏好目标与单历史t后kcopies；不授事实正确性、固定checkpoint或LLM训练收敛。历史/候选成本与假设失配退路保留，无LLM实测/生产收益；未运行代码或复现。root实际必要原源/现owner写前通过并授窄锁；作者已核两段正文与前后衔接，root已实际核正文、前后交接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08468` — Daily `2026-01-15`；[JudgeRLVR exact-v1](https://arxiv.org/html/2601.08468v1) §3.2–3.3/4.1–4.5/Table1–2。2+2+2=6，同policy阶段objective具体gap深入；只采offline gold verdict→generation阶段分责，不授独立线上judge或内部纠错。等250steps非等rollout/总tokens、Mixed/JudgeOnly局部占优与MATH500退步、PPL/marker为style代理保留。未运行代码或复现；root必要原源/现owner写前通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08834` — Jan16恢复时写入；作者正文已见2025.11.26首次公开，非本窗首次公开整合；[Reading or Reasoning? Format Decoupled Reinforcement Learning for Document OCR exact-v1](https://arxiv.org/html/2601.08834v1) Eq1–2、format reward 定义与 Table5–6。2+1+2=5，因 typed matching object/eligible denominator 的具体缺口深入受影响证据；仅采用 heterogeneous output 分工与 GT 非空 membership，不授公式语义正确、全格式有效、uncertainty 或等预算过滤收益。Qwen3-VL-4B 与 OmniDocBench 局部对照，text 反侧及 parser/regex 工程口径保持显式；precision BF16 属 SFT 配置，RL 完整 precision/GPU 型号与重复运行未披露，未运行代码或复现。root 必要原源与 owner 写前批准；root 实际正文、前后衔接与本末注非作者写后复核通过，窄锁释放，不代表日级 Gate。

- `SF-2026-ARXIV-2601-09236` — Daily `2026-01-16`；[Reward Learning through Ranking Mean Squared Error exact-v1](https://arxiv.org/html/2601.09236v1) §3–6、A.2.2/A.4/B.1及C.4–5。2+1+2=5，ordinal class tuple loss 的具体监督分支缺口深入；仅采用 order-compatible 解集与 non-overlap/exact-rank/realizability 条件，不恢复 unique/cardinal reward，不授 LLM-policy 收益。五人含两作者、标签 return 重叠、单条 rating 与 pair 资源不等及 offset/config 矛盾保留，不采用精确 recipe。未运行代码或复现；root必要原源与 owner 写前批准，实际正文/前后衔接与末注经root非作者POST通过，锁释放，日级 Gate 未授。

- `SF-2026-ARXIV-2601-08097` — Daily `2026-01-15`；[AdaJudge exact-v1](https://arxiv.org/html/2601.08097v1) §3.1–3.4/Eq1–6、4.1–4.4/Table1–3与Limitations。2+1+2=5，具体RM表示/refinement/readout分工缺口深入；全部K先算而非earlyexit，router消费response三视图+prompt，偏好监督非token真值。≤8B与同backbone/data/objective对照的预算未匹配、component切片退步、额外latency与原pooling/BT退路保留；未授下游policy收益。未运行代码/复现；root实际必要原源/现owner写前核通过并授窄锁，root实际正文/前后衔接非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08000` — Daily `2026-01-15`；[CADA exact-v1](https://arxiv.org/html/2601.08000v1) §2.3、§3.1–3.4、§4.1及关键反侧。2+2+2=6，具体owner缺口深入（CADA另涉及安全采用边界）；unsafe-only case reasoning与拒绝outcome/非空格式reward分开；KL非benign效用证书，有限2×8B/三runs与harmful/benign分母、局部退步与训练/judge成本近正文。未运行代码或复现；root实际必要源与具体owner写前核通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过，日级Gate未授。

- `SF-2026-ARXIV-2602-06256` — Daily `2026-02-10`；[Steering Safely or Off a Cliff? exact-v1](https://arxiv.org/html/2602.06256v1) §3–7/Table2与AppC必要配置。2+2+2=6，安全必要深入，只采用target efficacy、related-control ID与same-control shifted三分验收，不采泛化失效或PCA因果保证。四instruction models、五methods、256训练/100验证、500测试与25静态prefix×100有害query，三runs；RTX2080各model/method 15 GPU-hours，precision/完整解码及全成本未披露；Table2 safety=1−HarmScore，不倒转ComplianceRate。未运行代码或复现；root实际必要原源/owner写前批准，实际正文、邻接及末注非作者POST通过，窄锁释放，不代表日级Gate。

- `SF-2026-ARXIV-2602-10286` — Daily `2026-02-13`；[What Does Preference Learning Recover exact-v1](https://arxiv.org/html/2602.10286v1) §3–7与AppA/B必要代数。2+2+2=6，具体设计假设深入；采用人口加权 Bernoulli KL 投影、observed support / realizability / 全局最优及有限正概率 odds 条件，不采原P独立性必要、任意连续空间或全部 sample-complexity 保证，原展示式符号/括号滑误不作实现配方。必要原源与实际owner经root独立PRE通过；实际新增两段、前后衔接及末注已由root非作者POST通过，窄锁释放，不代表日级通过。未核代码或复现。

- `SF-2026-ARXIV-2602-15222` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15222v1) §2.1–2.3、§3.1–3.4及§5。2+1+2=5，未知属性发现/独立counterfactual检验差额深入；Pareto搜索≠bias事实/已学policy，17候选10双侧显著，single-full-run和n10/三合成regex召回局限保留。Judge/rewriter关联变化及生成/评分预算近正文，不授全部未知偏置召回或human truth。root必要源/实际31及30/32邻接PRE通过并授窄锁；root已实际核两段正文、完整邻接及末注，非作者POST通过，窄锁释放；未核代码或复现，未授日级Gate。

- `SF-2026-ARXIV-2602-15206` — Daily `2026-02-19`；[MAVRL exact-v1](https://arxiv.org/html/2602.15206v1) §3–5/AppendixA.2。2+1+2=5，反馈 type 的不同 likelihood/共享 latent reward 具体差额深入，保留 conditional independence/right censor、synthetic matched family、总反馈量混杂、CartPole退步及EPIC非cardinal真值；不授真实LLM人反馈或扰动安全。root必要源/实际owner PRE通过，root已实际核正文/完整邻接及末注，非作者POST通过，窄锁释放；未核代码或复现。

- `SF-2026-ARXIV-2602-15260` — Daily `2026-02-19`；[Prefix OPD exact-v1](https://arxiv.org/html/2602.15260v1) §2–5/Table1–3、§8。2+2+2=6，student prefix早停/渐长监督与完整tail风险差额深入；同vocab/格式条件、1.7B反侧、AIMEdev/test复用与SeqKD预算/teacher混杂保留，47倍仅compute-to-target/FLOPs估算，GPU hours另报且SeqKD离线生成未计，安全仅风险讨论。root必要源/实际owner PRE通过，root已实际核正文/完整邻接及末注，非作者POST通过，窄锁释放；未核代码或复现。

- `SF-2026-ARXIV-2602-15338` — Daily `2026-02-19`；[ObjDisco exact-v1](https://arxiv.org/html/2602.15338v1) §3/5、必要OE/Model-Fit及human study。2+1+2=5，trajectory residual→reward surrogate→行为重训再现的具体差额受影响深入；fixedsample解释非开放目标最优，Model-Fit非variance/因果覆盖，human匹配非唯一内部目标、共judge/时间相关/重训成本近正文。root必要原源与actual owner PRE通过；root实际正文/完整邻接及末注非作者POST通过，窄锁释放。未核代码或复现。

- `SF-2026-ARXIV-2602-15449` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15449v1) 必要方法、主对照与直接反侧。2+1+2=5，基础policy能力诊断预选test-tier α与rewardweight w分账，非在线adaptive或普遍hardfirst；reference/生成器/目标域与反侧、测试成本近正文。root必要source/actualowner PRE通过；root实际正文/完整邻接及末注POST通过，窄锁已释放，未运行代码或复现。

- `SF-2026-ARXIV-2602-15515` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15515v1) §5与AppendixD stop-gradient公式；2+2+2=6，probe reward两条梯度路径与同text表示漂移对照深入。GRPO样本非理想无偏、no direct probe gradient非no drift，highKL/长度/alpha退化与费用保留。root 必要源/actual owner PRE 通过并授窄锁，作者正文/完整邻接已顺读，root 非作者正文/完整邻接及末注 POST 通过，窄锁已释放。未核实现/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-12660` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12660v1) 必要方法、关键对照及直接限制；2+1+2=5，实际 owner 差额定点深入。root 必要原源/owner PRE 通过并授一段窄锁；仅采用正文的条件分支，不授泛化性能、正确性或安全保证。作者正文及完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST 通过，窄锁释放；未核 artifact 或复现，非日级验收。

- `SF-2026-ARXIV-2602-18037` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18037v1) §2.3/3.1–3.2、§5、C.1–C.4。2+1+2=5，flatness与distribution-distance不同控制对象差额深入；连续action/平滑/Lipschitz条件、biased reuse/clip、joint LR/scorer与强RM反侧、真实额外backward成本近正文，不授离散LM无偏或防hacking保证。root必要source/actual owner PRE通过并授窄锁；作者正文/完整邻接及末注实际顺读、限定diff-check通过，窄锁释放，root非作者实际正文/完整邻接/自身末注POST通过。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-18582` — Daily `2026-02-25`；[L2HR exact-v1](https://arxiv.org/html/2602.18582v1) §3–5、B.3。仅采用 state/option/history reward 签名与编译、任务可行、规范对齐三人口及两层消费 Gate；不排 history-augmented flat。固定 options/termination、候选/trial 搜索及训练、人评成本与无开放安全保证近正文。root 必要原源与 actual owner PRE 通过并授自身两段/末注窄锁；作者实际顺读正文、完整邻接及自身末注；root 非作者 actual POST 通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-17558` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17558v1) §4.2–4.3/5.1/5.4。2+1+2=5，具体owner差额深入；RM候选支持perturbed→currentpolicy与交替训练；reference-order假设/同GLM注评/未披露完整预算近正文，不授普遍保证。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-20710` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20710v1) §3/Table1/4/5/7。3+2+2=7；counterfactual行为预测与outcome-only增量训练差额深入。人工cue/拒绝采样人口、generic无CoT增量/反向cue/未见跨两类transfer与accuracy代价近正文；LoRA32/在线重写与simulation成本不授内部真值、统一introspection或部署保证。root必要源/actual owner PRE及正文749/751、完整741–770/本末注actual POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-17658` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17658v1) §3/4 Ass1/2/Th1、§5与A.2必要配置。2+1+2=5，margin selector的合成监督分配和feature方向条件缺口深入；小margin不授truth、PSD不授conditionnumber，改写/PKU split/额外生成成本与原对/均匀回退近文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-20722` — Daily `2026-02-26`；[BAPO exact-v1](https://arxiv.org/html/2602.20722v1) §3.1–3.2/4/5.2–5.3与mini-test。2+1+2=5，曾失败query当前重测与历史response reuse分责差额深入；finite0/8、FIFO/window/behaviorprob身份、underfilledbatch非等预算、重生成/重算费用及fresh回退近正文，不采用正improvement理论或全部rulelearning保证。root实际必要源/owner PRE通过并授两段＋自身note窄锁；作者实际正文/完整邻接/末注顺读、限定diffcheck通过；root非作者actual正文688/690、完整680–701及自身1326末注POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-20945` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20945v1) §2–4，2+2+3=7，correctness×length四格/mask与rollout截点身份差额深入。Hard正反馈稀疏、长mask反弹、多budget质量与更多rollout/staleness费用近文；不授所有任务长度/Pareto保证。非原packet作者必要原源/actual owner PRE，root授窄锁；作者实际正文/完整邻接/自身末注已读，root非写入者actual POST通过。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-21189` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.21189v1) §3 Eq2与negative weighted-agreement identity、必要形式反侧及有限hidden-state诊断，3+2+3=8深入。只采用固定binary/iid下非负prompt重权与负agreement条件，不采冲突corollary符号/strict-step endpoint；费用/实际全参数更新/单次多次mode验收近文。非原packet作者原证/actual owner PRE、root授锁；作者实际两段/邻接/自身末注已读，root非写入者实际正文/完整邻接与自身末注POST通过。未运行artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-23116` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23116v1)，必要原段/对照与局部反侧见当日core/owner packet。fresh非旧packet作者独核具体原证与actual owner差额，获root该owner窄ownership后写一段；作者正文及完整邻接实际顺读，root非写入者实际正文、完整邻接与自身末注POST通过，窄锁释放。采用正文窄命题，局部错误不授理论/全系统保证，未核实现或复现，不授日级Gate。

- `SF-2026-ARXIV-2601-05437` — Daily `2026-01-13` 增量；[Moral Foundations exact-v1](https://arxiv.org/html/2601.05437v1) §5.3、§7、B.3.2及macro/micro干预边界。2+1+2=5，geometry条件与能力反证差额深入；两模型英语/base aligned混杂、MMLU4.3/4.9点反侧与add/clamp剂量身份近文。独立必要原证/owner PRE通过、root授Ch31窄锁；作者完整邻接已顺读，root非写入者实际501–549完整邻接及本末注POST PASS，窄锁释放。未核artifact/复现，非日级Gate。

- `SF-2026-ARXIV-2601-07208` — Daily `2026-01-14`增量；[MAESTRO exact-v1](https://arxiv.org/html/2601.07208v1) §3–5/Limitations及受影响E.1–E.4、C.4–C.5由review_jan15_delta独立核原文。2+1+2=5，completed-response terminal h→逐response controller scalarization→groupA→周期head buffer结构差额必要深入；不采完整w(h,a)映射、sufficient-statistics/Pareto/vanishing理论或完整执行recipe。固定聚合仍共存，跨response尺子/proxy误设、head/fullseq/buffer/judge及更新全费近文，Table2overhead/早末状态非严格改善保留。保存版本/criterion normalization/updatecadence是本次工程推断，非原文完整协议。独立必要PRE PASS，root授本章最小单段/自身note窄锁；作者写后完整局部邻接及本注已顺读，review_jan15_delta非writer实际正文259/完整248–282及本注1374 POST PASS，窄锁释放。当前abs v2ACL26无已有明确withdraw/correction，Jan13公告与注册上界落BJTJan13，采用精确v1不比较全史；未核artifact/复现，非DAY。
<!-- supplement-20260122-review-note -->

- `SF-2026-ARXIV-2601-13284` — Daily `2026-01-22`增量；[exact-v1](https://arxiv.org/html/2601.13284v1) §3.2/4/5 Eq4/Table4。2+2+3=7；只采用decisiontoken trace读出与correctness分责、A_d=0+正onehot/错uniformCE分支，拒绝p≥1/C保证argmax的推断；CSQA4B accuracy回归、ACE分箱及3Qwen/500样本/λ条件近正文。不称所有RLVR失效。root实际必要原源/actual owner PRE通过并授窄锁；作者正文与完整邻接/末注顺读，root非作者actual POST通过，窄锁释放。未核实现或复现，不授日级验收。

- `SF-2026-ARXIV-2601-18731` — Daily `2026-01-28`补查；[exact-v1](https://arxiv.org/html/2601.18731v1)必要机制、评价与直接反侧见本日 `supplement-reviews-20261008.md` 与 `supplement-pre-resume-20261008.md`。2+2+2=6，具体owner差额受影响深入；仅采用正文最小接口与相邻失败边界，不授全性能/安全/公平保证。作者与 resume_20260128_audit 必要Source及字面PRE通过，root重授本章一段/自身末注窄锁；作者已顺读完整局部邻接与自身note，resume_20260128_audit实际POST通过，窄锁释放，非DAY。未核artifact或复现。

- `SF-2026-ARXIV-2601-18722` — Daily `2026-01-28`补查；[exact-v1](https://arxiv.org/html/2601.18722v1) §2–4/必要Table3。2+2+2=6，judge-only reference/组内ordinal feedback与二值verifier具体差额深入；按最终答案组拼接测试不授step truth，二次调用/异预算/双正确反側近文。root非作者必要Source、audit字面PRE通过、root授本两段/自身末注窄锁；作者实际写入并顺读邻接，resume_20260128_audit已实际读正文、完整局部邻接与自身note，POST通过，窄锁释放，非DAY。未核artifact或复现。

- `SF-2026-ARXIV-2601-18760` — Daily `2026-01-28`补查；[exact-v1](https://arxiv.org/html/2601.18760v1) §2–6/8/limitations。2+2+2=6，contextual/general两流→不同排序→candidate与ratification具体差额深入，人口/局部组件归因/代表性/费用/回退近文。root非作者必要Source、audit字面PRE通过、root授本两段/自身末注窄锁；作者实际写入并顺读邻接，resume_20260128_audit已实际读正文、完整局部邻接与自身note，POST通过，窄锁释放，非DAY。未核artifact或复现。

- 2026-01-28 来源遗漏补查，arXiv:2601.18751v1：必要 Source 复用本日具名独核，root 实际正文邻接与逐字 PRE 通过后授本段及自身末注窄锁；已写入，resume_20260128_audit 非作者实际正文、完整局部邻接及自身末注 POST 通过（Ch31 段分隔亦已独核），窄锁释放。采用范围、直接反侧与回退近正文保留；未核 artifact/复现。<!-- source-family:SF-2026-ARXIV-2601-18751 -->
- 2026-01-28 来源遗漏补查，arXiv:2601.18533v1：必要 Source 复用本日具名独核，root 实际正文邻接与逐字 PRE 通过后授本段及自身末注窄锁；已写入，resume_20260128_audit 非作者实际正文、完整局部邻接及自身末注 POST 通过（Ch31 段分隔亦已独核），窄锁释放。采用范围、直接反侧与回退近正文保留；未核 artifact/复现。<!-- source-family:SF-2026-ARXIV-2601-18533 -->
- 2026-01-28 来源遗漏补查，arXiv:2601.18543v1：必要 Source 复用本日具名独核，root 实际正文邻接与逐字 PRE 通过后授本段及自身末注窄锁；已写入，resume_20260128_audit 非作者实际正文、完整局部邻接及自身末注 POST 通过（Ch31 段分隔亦已独核），窄锁释放。采用范围、直接反侧与回退近正文保留；未核 artifact/复现。<!-- source-family:SF-2026-ARXIV-2601-18543 -->

- `SF-2026-ARXIV-2602-08194` — Daily `2026-02-11`补查；[exact-v1](https://arxiv.org/html/2602.08194v1) §3/4/6。2+2+2=6，具体课程可变对象差额深入；采用固定engine内state/transition/goal程序、compile/短rollout执行gate与目标anchor，保Craftax/GTrXL/5seeds、OLbundle/更新与FM成本边界，不授任意LLM或真实环境保证。root实际Source/owner PRE通过并授一段+本末注窄锁；作者已顺读实际正文完整邻接及Ch30/32交接，root实际正文/813–834完整局部/自身末注POST通过，窄锁释放，不授DAY。未核artifact/复现。

- `SF-2026-ARXIV-2602-08281` — Daily `2026-02-11`补查；[exact-v1](https://arxiv.org/html/2602.08281v1) §3–7及必要AppendixB。2+1+2=5，atomic/composition设计反证差额深入；正确前缀是条件测量非自由rollout，无条件乘积需独立/实际链用条件概率，δ=.125/K8只保证期望、0/128不判p=0，有限模型/操作与oracle、atomic反退保留。root实际必要Source/owner PRE及最小草稿通过并授本段+末注窄锁；作者实际正文完整邻接/Ch30/32交接已顺读，root实际419–440完整局部/新正文/自身末注POST通过，窄锁释放，不授DAY。未核实现/复现。

- `SF-2026-ARXIV-2602-08829` — Daily `2026-02-11`补查；[WildReward exact-v1](https://arxiv.org/html/2602.08829v1) §2–3/Limitations/必要A/B。2+2+2=6，原生followup观测与三阈值ordinal reward接口深入；neutral未知、参与非truth、正当refusal与独立安全分责、类别编码不识别cardinal utility保留。186k筛后人口、mining/refusal的SRP反侧、Platt fit/eval分母、未知线上gold margin与offline4/online8不同预算限制保留，不授所有RL效果。root实际必要Source及Ch31 101–129/Ch30/32入口PRE通过并授本一段及自身末注窄锁；作者实际写后顺读，root非作者实际新119/完整111–130及自身末注POST通过，窄锁释放。未核artifact或复现，非DAY。

- `SF-2026-ARXIV-2603-08412` — Daily `2026-03-11`补查；[Alignment Illusions 精确v1 PDF](https://arxiv.org/pdf/2603.08412v1) §2–4.3、A.1–A.3、B/Table1、C。2+2+3=7。root已核必要正文与附录；review_20260311独立核原文并实际看pp5–6 Figure3–5，发现Gemma margin图文冲突与BoN无targeted arm，采用边界已按此收窄。只采choice/display/justification身份及uniform、targeted、BoN三组诊断的分责；不采共同margin毁损、targeted→BoN因果、LLM标签一致即confidence或完整RL保证。root实际owner/邻章比较并窄写两段，非写入者review_20260311已实际顺读新增正文、完整局部邻接及本注并回对必要原证，POST通过，不授DAY；未核实现或复现。

- `SF-2026-ARXIV-2603-07784` — Daily `2026-03-11`补查；[ProgAgent exact-v1](https://arxiv.org/html/2603.07784v1) 必要原证76–190/237–324，2+2+2=6；专家相对帧序潜势与online reward refinement的owner接口具体差额深入。review_mar11_continue实际Source与Ch31 284–298/562–595/985–1004、Ch26 528–551 owner/PRE通过，root授示教段后/多评审分支前一段与本人末注窄锁。折扣difference与动态potential、prediction distribution非epistemic、expected曲线/联合消融/未支持realrobot及完整费用边界近文；作者实际写入，review_mar11_continue非writer实际279–310完整邻接、新293和本人注POST通过；root已释放窄锁，不授DAY、实现核验或复现。

- `SF-2026-ARXIV-2603-08145` — Daily `2026-03-11`补查；[DARC exact-v1](https://arxiv.org/html/2603.08145v1) §2–5必要核心、A5/A12/Algorithm1、H1–4/H6/H13–14/I的具名必要段；2+1+2=5，τ目标冲突/真实风险边界与已确认owner差额定点深入。review_mar11_continue实际必要Source及Ch31 206–269/1093–1108 owner/PRE，root实际接纳逐字一段并在09160实际POST释放后授本段与本人注窄锁。作者已实际完整245–277邻接及Ch30/32交接，采用给定pool经验entropic值/RP和独立人口验收，不补统一τ/硬riskcap；全文与直接反侧范围见本日笔记。已写入，review_mar11_continue非writer实际245–284/new257/本人1443及β>0窄补253–261/1440–1445最终POST通过，root窄锁释放，不授DAY、artifact核验或复现。

- `SF-2026-ARXIV-2603-08486` — Daily `2026-03-11`补查；[VSFA exact-v1](https://arxiv.org/html/2603.08486v1) §3–5/Table1–2及B/C必要反侧（SUP_CORE_08486.txt108–165/167–487/1050–1133），2+2+2=6。label-free仅省显式安全标签，不授视觉曝光唯一因果/原能力保持/真实persona或完整训练中介；局部ASR、合法请求和能力分测、SAE选择边界与全部费用/旧checkpoint/runtime gate近文。review_mar11_continue必要Source及actual Ch31 owner/逐字PRE经root接纳，授本段与自身注窄锁；作者actual151–178完整邻接与既有Ch30/32入口已读并写入，review_mar11_continue非writer actual新增段/完整局部邻接与本人注POST通过，root接纳并释放锁，不授DAY。未核pixels、artifact或复现。
