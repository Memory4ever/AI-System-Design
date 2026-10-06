# 第33章 GRPO：从组内相对优势到 Trajectory Lifecycle

**Knowledge Tree:** Part IV Training System：模型能力如何产生
**Stable Knowledge Node ID:** `TRAIN-GRPO`
**Legacy Chapter:** Ch29
**Status:** Draft

**Roadmap Intent:** 解释 GRPO 如何用组内相对优势移除 critic，以及当 rollout 演进为有状态、异步、可恢复的 trajectory artifact 后，objective invariants 怎样约束训练系统。

## 本章要回答的问题

PPO 使用 critic/value model 估计 advantage，但 LLM policy 和长 responses 会让 critic 成为额外的大模型状态。能否对同一个 prompt 采样一组 responses，用组内 reward 的相对高低代替 learned value baseline？GRPO 省掉了什么，又增加了哪些 rollout、reward 和统计稳定性问题？

本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。

本章以 DeepSeekMath 提出的 Group Relative Policy Optimization 为基线。后续系统可能修改 token weighting、KL estimator、normalization 或 clipping；同名 GRPO 实现必须逐项核验，不能仅凭算法名称推断完全相同 objective。

本章使用 `x` 表示 prompt，`G` 表示每个 prompt 的 sampled response 数，`y_i` 表示第 `i` 个 response，`r_i` 表示其 reward，`A_i` 表示 group-relative advantage，`pi_old`、`pi_theta`、`pi_ref` 分别表示 rollout、current 与 reference policy。

为避免把后续研究读成彼此并列的技巧，本章沿四层责任推进：

```text
group-relative estimator 与 trust region
→ verifier / measurement / multi-stage objective
→ rollout artifact、policy identity 与 update compatibility
→ stateful trajectory、typed credit 与跨 policy reuse
```

前两层回答“优化信号怎样形成”，后两层回答“这个信号在异步、长轨迹和工具环境中怎样仍属于预期 policy update”。后续分支只有改变其中一层的状态或控制权时才进入正文；单一 benchmark 变体不构成新的演进阶段。

## 为什么移除 Critic 会有吸引力

PPO-style RLHF 常训练与 actor 同规模或相近结构的 value model：

```text
V_psi(x,y_<t) -> expected return
```

它需要：

- Value parameters、gradients 和 optimizer states。
- Token-level value forward/backward。
- Return target、mask 和 value clipping。
- 与 actor rollout version 对齐。

对于可验证数学、代码或规则任务，同一 prompt 可以生成多个候选并直接比较 outcome。一个自然问题是：组内平均表现能否充当 baseline，而不再学习 `V_psi`？

GRPO 的回答是使用 group-relative reward。

## 同 Prompt 生成一组 Responses

对每个 prompt `x`，旧策略采样：

```text
y_1,...,y_G ~ pi_old(. | x)
```

每个 response 得到 reward：

```text
r_i = R(x,y_i)
```

Reward 可以来自 learned Reward Model、规则、数学答案检查、代码 tests 或组合函数。GRPO 的定义不自动保证 reward 可验证或正确。

有参考答案却没有可靠 outcome verifier 时，一个受限分支是在 sampled CoT 后 teacher-force 参考答案，用当前 policy 给它的似然作 reward，而不是另外采样答案再判断对错。整段概率、log-probability、平均 token 概率与平均 token log-probability不是中性的单位换算：整段概率会因长参考序列变得极小，长度归一则改变不同题目与答案长度的相对权重；平均 token 概率也不是整段正确概率。参考答案的覆盖与质量仍限制监督，不能把较高似然当作所有有效答案的接受率。额外 forced forward、数值稳定性和答案长度分布都须进入 reward contract；可靠 verifier 可得时，原 outcome reward 仍更直接。[受限 reward 对照](https://arxiv.org/html/2602.03979v1)。<!-- source-family:SF-2026-ARXIV-2602-03979 -->

这里的 reward 还随当前参数 θ 变化：完整期望目标的梯度既含 CoT 采样的 score-function 项，也含 reward 对 θ 的直接导数；后者在 log-likelihood 分支连接到参考答案的监督梯度。把 reward detach 后只作 policy-gradient 更新，会省略直接导数、改变梯度估计，不能静默称作完整期望目标的等价实现；用于减方差的 baseline 也须与当前 sampled CoT 独立。二项梯度分解并非这项实验首创，新增证据限于几种 reward/advantage 在作者两个 3B 模型、四个数据集上的取舍：greedy 与 sampled 的排序可能不同，长答案设置的 CoT 可收缩到接近普通 SFT；长度约束、KL 或 warm-start 维持更多 CoT，也不保证回答更好。reward 代理失配、参考不足或反向路径难以核实时，应回到可验证 outcome 或明确的普通 SFT，并分别验收输出质量、推理长度与总计算。

没有参考答案或可用 verifier 时，还可把同题 rollout 的末 token hidden state 归一化，用迭代 Gaussian 重权估计组内中心，再以到中心的负距离和组内 min–max 缩放构造 reward。[Latent-GRPO 的受限分支](https://arxiv.org/html/2601.08427v1)改变的是 reward 来源，不是为答案提供新的真值：表示一致性可能反映共同格式、风格或系统性同错，中心也不能自动叫作正确推理方向。min–max 尺度不是校准后的正确概率，更不保证梯度安全；末 token 选择、组大小、中心估计与 policy revision 都应随训练信号保存。<!-- source-family:SF-2026-ARXIV-2601-08427 -->

这条路径省去外部 judge 调用，却仍支付 hidden-state 存取和中心迭代成本。作者小模型数学实验有低于初始模型的反侧；API judge 的 2 QPS 是主动限流条件，不能把其耗时差写成普遍的两倍训练提速。采用前应独立验证正确性、同错簇和格式变化，并分账 rollout、代理计算与最终质量；一致性失配、组内信号退化或可靠 outcome verifier 可用时，保留普通 outcome GRPO，而不是用更紧的 latent cluster 替代答案检查。

组采样的关键是条件相同：同一个 prompt 下的 candidates 共享任务难度。若把不同 prompts 的 raw rewards 直接比较，简单问题可能系统性获得更高 advantage。

如果搜索轮次会改变可选候选集合，分组条件还应从任务状态扩展为 `(state, allowed-set)`。一种分支在 prompt 中列出有限候选，每轮只移除此前合法采样过的动作，再在新的集合条件下采样一组、计算组内 advantage；各轮样本可共同更新，但并不是原始未约束 policy 人口的无偏样本，也不能跨轮直接混比 raw reward。Prompt 列表不是硬 logit mask，非法或不可解析输出仍可能重复，须由 parser/verifier 处理；达到最佳分或轮次上限只定义停止条件，不保证遍历全部合法动作。[有限棋类对照](https://arxiv.org/html/2602.16833v1)中，候选提示措辞也与基线不同，匹配 rollout 或更新预算不等同于匹配 token/验证成本，不能把全部收益唯一归给集合剪枝。条件、合法性检查和采样 policy 应共同绑定，若候选集合遗漏有效动作、信号退化或额外轮次不抵成本，保留普通同 prompt outcome-GRPO 与独立动作验证，不由训练分组获得安全保证。<!-- source-family:SF-2026-ARXIV-2602-16833 -->

## Group-relative advantage

令组内均值与标准差为：

```text
mu_r = (1/G) * sum_(i=1)^G r_i

sigma_r
= sqrt((1/G) * sum_(i=1)^G (r_i - mu_r)^2)
```

标准化 advantage：

```text
A_i = (r_i - mu_r) / (sigma_r + delta)
```

`delta` 是数值稳定项。高于组平均的 response 得到正 advantage，低于平均得到负 advantage。

这是一种 sample-relative baseline。它不估计“这个 prefix 的长期价值”，而是回答“这次同题采样中，哪个完整 response 相对更好”。

Baseline 的比较人口还可以与尺度估计人口分开：保留同题 reward mean 作为中心，却以 batch 内相近 difficulty-proxy 桶的多题 rewards 共同估计 std。一条分支由视觉 patch 的谱 entropy 和生成序列 likelihood 分别提议 quartile buckets，再混合这两条 advantage 与原 GRPO；它改变 reward variance 的缩放，不授权跨题直接比较 raw reward，也不把 likelihood、length 或 encoder 谱视为校准的任务难度。Reward spec、同题采样、bucket population、ties、空桶和 zero variance 必须分别保护，不能因共享尺度就去掉数值稳定项。[受限视觉推理对照](https://arxiv.org/html/2602.21743v1)中 combined 平均较高，但 reasoning-only 在 MathVerse 反而更强；谱计算、额外 likelihood、分组与调参均计入总训练预算，未完整披露的 steps/seeds 不授通用稳定性或无偏目标。Proxy 漂移、桶退化或任务回归时，回退每题 std+delta、固定 scale 与普通 outcome GRPO，继续以独立任务结果验收。<!-- source-family:SF-2026-ARXIV-2602-21743 -->

同一问题也未必意味着同一比较人口。同一 speech/text policy 若对文本输入只给 correctness/format reward，对语音输入还给与当前正确文本回答的表征、输出相似性奖励，跨模态共用一个均值会把奖励定义与基线能力差异混进 advantage。一个条件分支仍联合采样，却分别以 speech 和 text 子组均值中心化；语音分支只从本组已正确的文本 completion 选择参考，没有正确文本时关闭相似性项、回到 base reward。这里的参考随当前 policy 移动，不是固定 teacher，也不把语音低于文本基线本身当成应受惩罚的动作。<!-- source-family:SF-2026-ARXIV-2601-05543 -->

这种分组增加正确参考筛选、hidden-state 保存和 embedding 打分成本，并减少每个子组的有效样本数；相似性仍可能奖励风格而非真实推理。受测 7B 语音模型、合成 TTS QA、冻结 encoder/projector 的对照只支持这一训练分支，不证明语音识别误差已消失或内部 reasoning 已被因果对齐。Modality Recovery Rate 的分母还是原始文本 backbone，不是更新后文本 policy；即使超过 100%，也不能据此宣称两模态当前能力完全相等。没有可靠正确文本参考、子组退化为常量或额外成本不合算时，保留独立任务 reward 与普通 outcome GRPO。

## 一个三样本小例子

假设同一数学 prompt 采样 `G=3` 个 responses，rewards 为：

```text
r = [1.0, 0.5, 0.0]
mu_r = 0.5
sigma_r ~= 0.408
```

忽略很小的 `delta`：

```text
A ~= [ 1.225, 0.000, -1.225]
```

第一个 response 的 tokens 被鼓励，第三个被抑制，中间 response 相对组平均没有一阶方向。

如果所有 rewards 都相同：

```text
sigma_r = 0
A_i ~= 0
```

这一组几乎不提供区分信号。二值 reward、较小 `G` 或任务过难时，all-zero/all-one groups 会降低有效 sample ratio。

等完整 rollout 后才丢掉零方差组，能依据真实 outcome 判断，却已经支付生成成本。一条条件分支先在不启用过滤的 warm-up 中，让小估计器学习当前 actor 的同题平均 reward 与 question perplexity；随后在生成前按估计排除过易或过难候选。它改变的是 rollout admission 时点，不是 GRPO 的实际 advantage 定义：平均 reward 预测不是组内中心化 advantage，接近端点也不能证明下一次随机 group 必定零方差。未披露或方向含糊的 ranking/threshold 不能自行补成可重放的精确 selector。<!-- source-family:SF-2026-ARXIV-2602-06375 -->

生成前拒绝会失去本来可能学会的样本，actor 移动又使估计器过时，因此需保留随机 coverage、被拒题目的定点 rollout checks 与普通全量 rollout 回退。受限作者实验中，过滤过强伴随质量退步，困难/容易题较少的语料收益也较弱；warm-up、BERT/PPL 更新与候选扫描都应计入成本，等 optimizer steps 不等生成 tokens 或总预算相同。局部 step time 接近 GRPO、低于过采样 DAPO，不能写成免费估计或任意 curriculum 的两倍加速；质量或代理校准失准时停止过滤，继续以真实组 reward 更新。

## GRPO 的 clipped objective

对 response `y_i` 的第 `t` 个 token：

```text
rho_(i,t)(theta)
= pi_theta(y_(i,t) | x,y_(i,<t))
  / pi_old(y_(i,t) | x,y_(i,<t))
```

核心 clipped term 与 PPO 相似：

```text
min(
  rho_(i,t) * A_i,
  clip(rho_(i,t),1-epsilon,1+epsilon) * A_i
)
```

对 group、response 和有效 tokens 聚合，并加入 reference-policy regularization。一种抽象写法：

```text
J_GRPO(theta)
= E[
  (1/G) * sum_i
  (1/|y_i|) * sum_t
  (
    min(rho_(i,t) A_i, clip(rho_(i,t)) A_i)
    - beta * KL_term_(i,t)
  )
]
```

不同实现对 response/token normalization、KL 放置和 estimator 有差异。本章保留稳定结构，不把某个 runtime 的具体 loss reduction 当作统一定义。

### 正负 Advantage 不必共享同一 Clipping Contract

对正负 advantage 使用同一旧策略 ratio，优点是保守且容易解释；但它也把“继续放大已变好的动作”和“阻止坏动作
突然变得过小”绑定在同一 trust-region 规则中。一条实验性分支让正 advantage 使用当前 policy 的 detached
probability 作为分母：前向 ratio 数值为 1，但分母停止梯度，因此梯度仍推动当前 token probability；负 advantage
继续使用 behavior-policy ratio 与 clipping，KL、rollout provenance 和 freshness 约束保持不变。

```text
A > 0: current probability / stop_gradient(current probability)
A < 0: current probability / behavior probability, with clipping
```

它把 exploration 与 stability 分成两条控制路径，却会削弱正样本相对 behavior policy 的显式边界，并让 stale rollout、
极小概率 token 和长度归一化更敏感。对分布漂移小、方差控制优先或 freshness 难保证的训练，标准对称 clipping 仍是
更稳妥基线；作者结果只支持其特定 RL workload，不构成通用替代。

硬 clipping 的停止分支还可以换成有限的软衰减，而不改变最终 outcome verifier。一条[受限更新提案](https://arxiv.org/html/2602.17550v1#S4)只在正 advantage 的ratio>1、负 advantage的ratio<1这两侧，用停止梯度的Gaussian gate乘到ratio×advantage上；宽度再按该token的old-policy概率反向缩放，并以signed group advantage分别扩张正侧或收紧负侧。这是token概率质量与正负信号共同控制的采样更新，不是按response语义簇频率重权，也不使gate的平滑值成为硬trust-region证明。稀有old probability、指数下溢、rollout freshness与有界宽度仍须数值检查；整条答案的正负reward不判定每个token是否正确，group内成功频率也不是题目真实难度。原DAPO-Math-17K、1.5B/7B/14B、math_verify训练与prime_math评测的对照中，单边SAPO改动可避免一个1.5B配置的collapse，不能由此识别全部variance/risk组件的独立因果；更高entropy也未让所有baseline更好。512 rollout/32 update batch形成16次off-policy更新，KL coefficient为0，原研究总预算超过20k GPU-hours，不能把样本效率当墙钟或免费稳定性。应保存behavior概率、detach、符号分支、宽度参数和数值处理，与原对称clipping在匹配质量/训练预算下比较；stale或极小概率不稳、局部质量或总成本回归时，保留原GRPO/PPO与保守freshness门。<!-- source-family:SF-2026-ARXIV-2602-17550 -->

同一条多轮 rollout 中，更新的 freshness 也可以按 turn 而不是只按 token 判断：对负 advantage 的一轮输出，先平均该轮的 `log(pi_old/pi_current)`，超出阈值才将这轮的更新 mask 置零；正 advantage 保留。这是 sequence-level 门控叠在原 token-level 更新上，不是删除整个 episode，也不是以内容质量验证器筛选错误。它以减少陈旧负轮的破坏换取负例覆盖收缩，须保留 mask 阈值、有效 token/turn 数及 KL 和 batch 的共同对照；较大的 KL 容限或 batch 也能影响恢复，不能把所有收益归给门控。额外 rollout、调参和统计费用仍要结算，loss 聚合方式在不同任务上可反向变化；新鲜数据或负例已可信时，原 clipping/soft-gating 更新继续合理。<!-- source-family:SF-2026-ARXIV-2602-21534 -->

#### Positive-only 不是没有负向梯度，而是改变负样本的来源

标准 PPO/GRPO 同时采样正负 rollout，在 reward 足够稠密、失败样本能区分严重程度时，显式负 advantage 提供清楚的
相对基线。稀疏 binary RLVR 中，大量失败 rollout 可能都得到同一个零值；继续扩大负样本池会增加生成成本，却未必增加
可辨别的失败信号。一个条件分支只让 positive subset 进入显式 importance objective，通过 softmax normalizer 对未采样
token 自然产生隐式负梯度，再用 bounded/self-normalized importance、EMA siamese anchor 与有界表示相似度约束更新漂移。

这种方法没有取消负向作用，而是把它从“失败 rollout 的显式 advantage”移到 probability normalization 与 reference
representation。Sample selector 拥有 positive-set membership，behavior/current policy identity 约束 importance，EMA
branch 提供稳定 anchor，最终 correctness 仍由外部 verifier 决定。它减少对无分级负样本的依赖，却在 zero-positive
batch 中没有可用更新，并新增 selection bias、EMA state、representation penalty 与 support collapse 风险；密集 reward、
负样本本身有信息或跨域校准不足时，标准 GRPO/PPO 仍更可靠。现有 exact-v1 结果限公开数学 benchmark、text-only
模型和 7B 以内规模，不证明跨领域或大规模训练优势。

<!-- source-family:SF-2026-ARXIV-2605-06650 -->

### 策略稀有度改变 Advantage 权重，不替代正确性

普通 GRPO 以同题 reward 的相对高低给完整回答定方向，并不区分多个回答是否只是同一种解法的改写。当训练目标还要求保留不同解法时，一条条件分支先由较大的 judge 对组内完整 reasoning 与 answer 作语义聚类，再以局部簇频率 `f` 构造 `f^(-alpha)` 权重，乘到原 signed advantage 上；`alpha=0` 回到普通 GRPO。[Rewarding Rare 的组内机制](https://arxiv.org/html/2601.08763v1)因此不只是奖励“正确且稀有”：稀有的负 advantage 也被重新加权，而正确性仍由原 outcome verifier 决定。这个频率只描述当前采样组与当前聚类器，不是全局新颖性，也不是 token entropy 或真实推理策略的认证。<!-- source-family:SF-2026-ARXIV-2601-08763 -->

该分支新增 judge 调用、聚类误差与 group-size 依赖；小组偶然稀有或同义解法被拆簇，都会改变更新力度。作者数学实验的 pass@k 及其面积比较支持有限的覆盖取舍，并非各任务普胜；20 道题的人工作法覆盖对照是 INSTRUCT 而非 GRPO，不能据此单独归因于频率重权。策略标签不可靠、额外 judge 成本不合算或主要目标只是可验证正确率时，保留普通 GRPO 更直接。这仍是完整 response 的权重，下面的 token credit 问题并没有被语义聚类解决。

## Sequence Reward 怎样作用到 Tokens

若 reward 只在 response 末尾给出，常见简化是同一 `A_i` 作用于该 response 的所有有效 tokens：

```text
A_(i,1) = ... = A_(i,|y_i|) = A_i
```

这比 learned token value 简单，也更粗糙。正确 final answer 可能包含冗余或错误 reasoning，错误 final answer 也可能包含部分有价值步骤。

没有独立 PRM 时，也可让 token credit 依赖 policy 相对 reference 的后续偏移，而不把整条回答的 advantage 原样广播。[PRL exact-v1 的 Algorithm 1](https://arxiv.org/html/2601.10201v1)先标准化组内 outcome advantage，再从当前位置到回答尾部累加 `log(pi/pi0)`，按温度缩放后从 advantage 中扣除；该局部 credit 作 stop-gradient，进入 token-wise clipped-ratio 更新。这里 `pi0` 是固定 reference，`pi` 是当前 policy，suffix 信号不是对该步骤语义正确性的评分。最优 policy 下的理论恒等式不能自动移交给当前 policy 实现，detach 也不证明与参数依赖 reward 的全梯度等价。<!-- source-family:SF-2026-ARXIV-2601-10201 -->

这增加 reference scoring、后缀统计及粒度选择成本；正文额外 beta-KL 项与 Algorithm 1/Table 6 的 KL-loss=0 配方必须区分，不自行合并。所测数学模型中，7B 的短 segment 16/64 低于 GRPO，而较长 256 略高；1.5B newline 分段又高于固定 256，因而不支持通用 step 粒度或解空间覆盖保证。作者 4 H100、约 15 小时/次运行并非逐方法全部匹配预算，精度与 seed 未披露；未核 Appendix A 证明不作为采用依据。suffix credit、reference identity 或预算未验时保留普通 sequence advantage 与可靠 outcome verifier，需要语义步骤验收则仍交给下面的独立 PRM 分支。

另一种不依赖独立 PRM 的 signal，是在已生成推理中将有限可解析 span 换成 placeholder，再 teacher-force 原 answer，测其概率下降；将这份 answer-dependency 信号映射成有界权重，乘回原 group advantage。outcome verifier 仍决定正负方向，负 advantage 也会被重权，不能只解释成“奖励正确步骤”。它改变的是局部更新幅度，不像 prefix 重采改变 continuation 人口，也不等于识别真实因果步骤。 [必要机制与反侧](https://arxiv.org/html/2602.09331v1)。<!-- source-family:SF-2026-ARXIV-2602-09331 -->

placeholder 可能引入 OOD 输入，原 answer 依赖某 span 也不证明该 span 正确或删除具有因果效用。有限算术/句子 parser、span 数与概率归一共同限制适用域；受测代码任务反退、不同模型统计支持不一致，而且额外 forward 将训练时间增加约32–74%，不能称总训练省算。parser、信号或预算不稳时，保留原 sequence advantage、独立过程 verifier 或不重权；正确性继续由终局验收承担，不将 dependency 传给 token truth。<!-- source-family:SF-2026-ARXIV-2602-09331 -->

当有可用 PRM 时，可以把局部质量与整条轨迹是否成功分开给权：先按生成 entropy 的峰划出候选 segment，用 PRM 评价各段并把段内信号广播到 tokens，再叠加由同题 rollout 的 outcome 决定的 trajectory shift。这样，同一条成功或失败轨迹内仍可能有不同局部权重，而不是让 PRM 替代最终答案的验收。[PRPO 的有限配方](https://arxiv.org/html/2601.07182v1)用固定 uniform prior 的均值/标准差变换 process score；这是尺度选择，不代表 PRM 概率已校准，entropy 峰也不是语义步骤边界的 oracle。分段方式的直接消融会明显退化，PRM 错验或尺度漂移还可能把局部错误放大，作者也未给出完整的无 collapse 保证。额外 PRM serving、scoring 与训练时间须和 outcome-only 基线分账，部分测试仍有反退；分段、PRM 资格或净收益未验时保留普通 sequence advantage 与可靠 process verifier，而不因更细粒度就宣称更正确。<!-- source-family:SF-2026-ARXIV-2601-07182 -->

没有独立 PRM 时，还可在训练 rollout 中构造受控分叉：先生成纯文本路径，在非收尾区域的 clause 边界选高 entropy 位置，再按 hint 的条件 likelihood 采样位置/hint 对，插入工具提示并执行代码后续写。训练树的叶子仍由最终答案 verifier 评分；内部节点取后代叶子的均值，span advantage 同时比较全树均值与父节点均值，再广播给该 span 的模型 tokens，工具返回不进入 loss。这是 tool-hint 改变条件后的树内效用 proxy，不是 iid GRPO 组，也不证明工具调用具有唯一因果收益；树只用于训练，测试不必继续执行同一搜索树。<!-- source-family:SF-2026-ARXIV-2601-08274 -->

树需要额外候选、hint likelihood 探测、代码执行与 outcome 检查；用15个叶子估值、仅抽8条路径训练，不等于8条独立 rollout 的总预算。局部对照支持该树中细分信用的取舍，扩大树在某些任务仍退步；论文 Eq7 的简略目标表达不足以核验完整梯度实现或无偏性。Entropy 不是语义步骤 oracle，hint、sandbox 截断和有限叶子也会改变估值人口。工具资格、分叉或预算不可靠时，保留完整 response 的 sequence advantage、可靠过程 verifier 与普通独立 rollout，不把更多工具使用本身当成更正确。

Process reward、step verifier 或更细粒度 credit assignment 可以提供局部信号，但会增加标注/evaluator 复杂度，并引入新的 exploit surface。

也可以在训练时让多个 listener 仅消费 speaker 推理的部分前缀，续写后按其答案与 speaker 原答案的匹配数构造 reward，再把这种可执行性信号与正确答案监督分工：先做 GRPO，后单独做 answer-only masked SFT 并合并适配参数。匹配只表示给定 listener、前缀切分和续写协议下的一致性，双方可能共同答错，不能签发内部 faithfulness 或真实因果推理保证；后阶段不对 reasoning tokens 直接计 loss，也不意味着共享参数不受影响。[受限对照](https://arxiv.org/html/2602.16154v1)中，单用匹配信号会牺牲准确率，单用 correctness 又可能降低 hint 使用；hint/AOC 指标本身只检验有限行为 proxy。listener 续写、样本筛选和第二阶段训练均需计价，部署只保留 speaker 也不抹去这些成本；共识误验、协议迁移或准确率回退时，可靠 outcome-only 训练与独立过程 verifier 仍是有效分支。<!-- source-family:SF-2026-ARXIV-2602-16154 -->

当训练环境另有一个已知的隐含目标，而中间动作主要是在收集信息时，也可以不用独立PRM，而在相邻交互history下，让当前policy为同一个目标打log-probability分，取两次读数的差，再把其正部分与终局outcome、格式/重复及每轮成本一起组成reward。组内advantage按turn计算，只广播给该轮policy生成的tokens，环境返回不进入policy loss。这把“对已知目标的概率读数增加”作为局部训练proposal，不把模型confidence变成真实Bayesian belief或步骤正确性；目标标签由训练环境持有，不能让部署agent凭空获得答案，使用答案与模拟响应的lookahead也只是特权诊断。取正后的差不再是原始未截断的potential差，不能据此承诺policy-invariant shaping或无偏信用。<!-- source-family:SF-2026-ARXIV-2602-12342 -->

这条分支支付额外target likelihood求值、标签与模拟器成本，并把校准、reference选择和reward scale变成训练接口身份。固定一个参考目标可能压制多个同样有效的解；probability差的幅度也不受终局reward范围约束，过强shaping在[受限长程交互对照](https://arxiv.org/html/2602.12342v1)中会使训练崩溃。原对照保留效率惩罚并为outcome-only基线调学习率和loss聚合，但同时改变局部reward与turn credit，不能把全部收益归给其中一项；同轮比较仍须满足后文的history/group合同。标签不可得、校准漂移、多解被挤压或额外评分不合算时，保留可靠outcome、独立process verifier或普通trajectory advantage，而不是让概率读数签发真实客服效果或免费探索证书。

有外部 evidence 与可解析步骤时，还可以让同一 outcome advantage 的正负方向决定 span 权重：正 advantage 对 evidence-supported step 保留完整权重、对 unsupported step 折扣；负 advantage 则对 unsupported step 保留完整惩罚、对 supported step 折扣，再把步骤标签映射到其 token span。它减少正确局部步骤因错误终点承受的惩罚，却没有鉴定模型真实内部推理；parser、step-to-token 映射、evidence 来源与 verifier checkpoint 都是训练信号的身份。离线 gold evidence 或参考推导不能冒充部署 oracle，错验与遗漏会把局部标签放大成错误更新，额外 attribution calls 也要计价。[受限多跳问答对照](https://arxiv.org/html/2602.03507v1)中，综合指标改善仍伴随部分正确率下降，不能授予全面 Pareto 改善或必无幻觉；无可靠证据、步骤无法对齐或验收回退时，保留普通 GRPO 与可靠 process reward。<!-- source-family:SF-2026-ARXIV-2602-03507 -->

局部 verifier 还可以改变 rollout 的条件人口，而不只改变已生成 span 的权重：找到首个被判为不受 context 支持的句子后，保留其前缀、从该条件重采 suffix；原/新路径因此共享一个条件状态，结果差可形成受限的对照信号，不保证新 suffix 更好或识别内部因果。[FaithRL exact-v1](https://arxiv.org/html/2602.05897v1)以 HHEM-2.1 作 sentence verifier，完全通过的路径另从原 prompt 独立采样，八条初始路径扩为十六条，不等同 token、judge 或总计算预算。该方案把 context support 与 answer outcome 分开，部分问答准确率仍退步；其“information gain”惩罚实际控制句数、长度与重复，不能当作信息论量。截断、parser 与 verifier 错判会改变采样支持并放大偏差；资格或预算不稳时，应回退独立完整 rollout、可靠 process verifier 与原 sequence advantage，不能从共享前缀就取得无偏 credit 或必无幻觉保证。<!-- source-family:SF-2026-ARXIV-2602-05897 -->

若没有可信的逐句 verifier，也可用当前 policy 在候选 prefix 下的有限续写结果定位经验分叉：某处出现成功 suffix 就向后搜索，全部失败则向前搜索，在有限 anchor 上近似找到可恢复性下降的位置。内部节点按 children 的 outcome 均值形成 branch credit，与叶子所属 trajectory 的相对 credit 混合；再只对提议的 critical suffix 放宽负 advantage 的 lower clip，保留正 advantage 的 upper clip。这改变条件采样、局部 credit 和负向更新窗口，不是识别真实 first error 或证明其它 prefix 已无解。<!-- source-family:SF-2026-ARXIV-2602-09598 -->

[ELPO 的必要机制与反侧](https://arxiv.org/html/2602.09598v1)只在确定性代码/数学环境提供受限支持：有限 Pass@k 依赖当前 policy、decoder 与预算，稀少成功可能被判成不可恢复，多错交互也不由单边界涵盖；同 rollout 数不等同 token、工具或总训练成本。定位错误会把更强负更新施加在错误 span，entropy-gap 与分支预算也需校准；局部 clipping 消融存在表文不一致，不据此签发稳定性保证。采样支持不足、工具反馈不可靠或额外预算不合算时，保留完整独立 rollout、原 clipping 与可靠过程 verifier，而不把经验失败变成语义错误真值。<!-- source-family:SF-2026-ARXIV-2602-09598 -->

局部分叉还要决定把有限续写预算投给哪些失败 prefix，而不只定位单一边界：可用“深度偏好×有限 K 次续写至少一次成功的经验 recoverability”形成采样 proposal，在难以从 root 到达与仍有机会恢复之间取舍。只以相对深度拟合的 logistic sensor 不是每个 prefix 的真实成功概率；K、decoder 与刷新人口变化都要重验。main root 轨迹和条件辅助 suffix 分别形成 advantage 与归一，再用显式 λ 控制两流比例，避免失败数量或分支数改变时静默淹没主信号。辅助 prefix 的 gradient mask 只限定 loss 人口，不免除 prefix forward 或额外串行采样，也不把局部更新变成整个 root 分布的无偏估计。[受限 DEEP-GRPO 对照](https://arxiv.org/html/2602.14169v1)支持这项预算/人口分工，不保证不可恢复失败也能获得有效修正；恢复信号不可靠、额外费用不合算或局部训练退步时，保留普通 root rollout、原 sequence objective 与可靠 verifier。<!-- source-family:SF-2026-ARXIV-2602-14169 -->

多轮回答还有一种更早的信号错位：模型已经能在合并后的完整用户条件下解决问题，却在含旧回答的历史中继续沿用过时推理。此时可以先用同一个 outcome verifier 筛选“完整单轮表现优于原多轮历史”的训练支持集，再对历史条件下采样的同一最终回答，计算 frozen reference 在完整条件下的长度归一 likelihood，将它作为辅助 sequence reward 加到原 outcome 上。Anchor 改变的是候选回答相对完整条件的偏好，不是把历史删掉，也不把 reference 的流畅性升级为正确性或 token 级因果 credit。<!-- source-family:arxiv:2603.04783v1 -->

这个分支增加完整条件构造、预筛 verifier 与 reference scoring 成本，并受单轮能力上限和过滤偏差约束；完整条件本身遗漏更新或 reference 仍坚持旧答案时，anchor 也会误导。[受限多轮对照](https://arxiv.org/html/2603.04783v1)只覆盖可合并条件的合成数学、代码及摘要任务：去过滤消融下降，Qwen2.5-7B 的一项 refinement 结果仍略低于普通 GRPO，不能据此承诺所有多轮 RL 都应替换。未知事实、主动澄清或外部状态持续变化时，保留可靠 outcome/process verifier、明确上下文更新与普通 GRPO；辅助似然不能创造原模型未具备的能力。

只有 outcome 标签且同题组同时含正误 rollout 时，还可把 policy 自身 hidden states 当作局部更新 sensor：按重叠 span 比较两类隐藏态分布，为每个 span 取到反方 span 的最小 Sinkhorn 距离，再以重叠 span 的最大权重乘原 sequence advantage。Outcome verifier 仍决定正负方向；分布差异只是 credit proposal，不证明某个 token 因果地造成错误，也不等同外部 PRM 或字段真值。无反方样本时恢复原 GRPO。<!-- source-family:SF-2026-ARXIV-2604-23318 -->

它增加隐藏态存储、span 对齐与 Sinkhorn 计算，默认全组归一还会改变跨 rollout 的梯度幅度，不能称为守恒的 token 分账。[exact-v1 §3–6](https://arxiv.org/html/2604.23318v1)的距离排序定理依赖有界隐藏态、分布差异超过采样噪声等条件，best-observed 数学/代码结果和额外训练时间不证明同总预算普胜。组内无正误混合、表示漂移、对齐或成本失控时，应回退 sequence advantage、可靠过程 verifier 或显式 critic，独立验收最终 outcome。

完整回答若含多个可解析的结构字段，终局 reward 广播还会把一个字段的错误分给其它字段。一条条件分支先按输出 schema 定位字符区间，再依据累计解码 offset 映射到 token span；对各几何字段分别构造组内相对 advantage，仅把该字段的信号送回相应 span，语义与格式背景另按明确规则混合。这里训练信号的身份不只是字符串位置，还包括 parser 版本、字段边界、char-to-token 映射和每组样本支持。字段组的归一与整条回答在 rollout 组内归一不是同一个分母，也不同于一条回答内部候选集合的 Shapley 分账。<!-- source-family:SF-2026-ARXIV-2604-21160 -->

这需要解析、对齐与字段 verifier 的额外成本；malformed 输出、跨字段 token、重叠 span 和零方差组应有显式 admission/回退，不能把不可解析部分静默当作已审结果。这些是工程要求，不是论文已验证的完整防御。预测的 3D 投影与预测 2D 一致只说明内部一致性，落入 GT box 也不等于关键点坐标正确，最终几何质量仍需独立验收。[受限 Point-VLM 对照](https://arxiv.org/html/2604.21160v1)中，单用字段 credit 的 3D IoU 略低于广播，加入一致性分支才局部改善；故细粒度本身不是质量保证。字段 oracle 或对齐不可靠时保留完整回答 reward，且不能把所测 ShapeNet/模型与训练预算推广成任意 JSON 任务或机器人安全。

答案 verifier 可靠却不能区分多个正确回答的过程质量时，可以先保留完整组的 outcome reward，只在已验证正确的子集中做有界、tie-aware 的相对质量排序，并把居中辅助分数加回原 reward；没有至少两个正确回答时辅助项归零。正确性资格由外部 verifier 决定，过程 judge 只拥有子集内相对偏好，之后仍在原 prompt 的完整 rollout 组内计算 advantage。子集居中不等于完整组归一，也不识别 token 级因果贡献；负辅助项更不等于最终 reward 为负。<!-- source-family:SF-2026-ARXIV-2604-18892 -->

这个分支用额外 judge 上下文和相对质量噪声换取正确答案之外的学习区分；judge 看不到图像或受选项、解析影响时，过程一致性不能证明 grounding 或 faithfulness。[受限多模态对照](https://arxiv.org/html/2604.18892v1)有任务退步，且未匹配全部 judge 成本，故应同时验收最终答案与独立过程切片；子集过小、judge 不可靠或预算紧时，应回退 outcome-only、可靠 PRM 或人工 process 标注，而不凭零和公式承诺无 reward hacking。

多模态过程的压缩还应先区分视觉观察、背景先验、推导与最终答案的权限，再选择紧凑字段和符号连接。格式可解析只证明这些陈述能被定位，不证明图像支持观察、先验适用或推导有效。一条受限训练分支将压缩trace与reference steps对齐：最终答案错误时仍按参考推导的完成程度给部分credit，并对unsupported匹配步骤折扣；这提供局部训练信号，不把reference agreement、步骤数量或紧凑表示升级为正确性、视觉grounding或token级因果贡献。

这种选择用teacher生成/过滤reference、额外step judge和解析预算换取短trace；shared teacher/verifier偏差和不同解法的粒度会进入credit。[DRT的受限整体结果](https://arxiv.org/html/2609.21675v1)减少输出长度，但MathVista、GSM等单项反退，辅助bonus又增加长度且有切片退步，不能归因每个压缩或奖励组件均有效。应同时验收最终答案、视觉依据、过程支持与含judge的总成本；reference不可靠、压缩丢失必要证据或任务回归时，保留完整trace审查、outcome-only或可靠process verifier，而不只优化格式与长度。<!-- source-family:SF-2026-ARXIV-2609-21675 -->

压缩过程也可用改变条件输入的第二次 rollout 来提供训练信号，而非请 judge 直接认证 trace。先让同一多模态 policy 从图像与原 query 生成目标 description 和答案，再只给图像与 description 做第二 pass，以 gold segmentation/空间答案核第二次结果；所得 reward 只检验这组图像、description 与 decoder 的条件充分性，不证明原 reasoning faithful、description 唯一因果或无需 gold。训练两次、部署仅第一次是不同计算合同，不能把训练期 second-pass 检查当线上 verifier。[DR2Seg exact-v1](https://arxiv.org/html/2601.09981v1)支持这条监督构造分支，不采用其宽泛过程理论。

比较两次 reasoning 长度还需要绝对 anchor，避免二者同时变长仍获相对奖励；该配方在整组 accuracy reward 都为零时关闭长度项，保留先学会定位的机会。这是条件 reward 设计，不是最短 trace 证书：过紧 anchor 反而增加输出并损质量，3B 对照的 gIoU 提升伴随 cIoU 下降，设置说明与最佳 anchor 表值也不完全一致。额外 pass、图像前向、gold/segmentation reward 与训练成本须计入，推理 token 减少不等于完整 GPU 费用减少。description丢失目标、gold 或解析不可靠、质量反退时，保留完整 trace、可靠原 outcome oracle 与无长度项的训练，而不让“自奖励”名称承担事实验收。<!-- source-family:SF-2026-ARXIV-2601-09981 -->

压缩目标还可用冻结 reference 的表现作相对容忍边界，而不固定对每个 token 征税：同一 prompt 分别从 current 与 reference 采样回答，用 minibatch accuracy 的差值决定这轮优化正确性还是归一化长度；下一阶段再把长度作为约束、正确性作为目标，并固定上一阶段估计的长度统计。[CRT 的受限分支](https://arxiv.org/html/2602.12526v1)在参考表现附近分配更新方向，但这个 guard 是采样 proxy，不是逐题正确性保持或硬约束证书，离散 indicator 也不能直接按普通导数实现。额外 reference rollouts、verifier、统计估计与两阶段训练都要计费；所测数学模型有 OOD 单项退步、另一模型平均正确率下降，完整两阶段也不总有更短 OOD 输出。应绑定 reference、容忍量、normalization 与采样人口，分别验收正确性、长度和总成本；估计不稳、域外回归或参考不可靠时，保留普通 outcome-only、保守长度项或无长度项的训练。<!-- source-family:SF-2026-ARXIV-2602-12526 -->

正确性与长度还可以在两个位置分责：保留 binary outcome，只给已验证正确且短的 rollout 加 bonus，再用组内归一的 `L_i^(−β)` 系数乘各 rollout 的 token-SUM loss。[一个受限 hybrid-thinking 分支](https://arxiv.org/html/2602.22556v1)由双 teacher 的 think/non-think SFT 起步，随后调首个控制 token 的激励；这不是逐题正确性保持证书。普通 binary GRPO 中正确长回答的 advantage 本已非负，不能说 bonus 修复了所有“正确长负 advantage”；`β=0` 也只是系数均匀，不是每 sample 的总梯度均权，因为乘的是 token sum，公共 normalizer 还改变更新尺度。λ、β、长度与 reward 分母共同定义目标，过强控制 token 激励、teacher 格式迁移和非数学任务会改变折中。teacher 构造、MathVerify、rollouts 与训练仍付费，少 tokens 或更多 non-think 不直接签 wall-clock/SLO 收益；质量、长度或总成本回归时保留普通 outcome-only、无长度项与原完整 trace，而不只追求一个固定短输出比例。<!-- source-family:SF-2026-ARXIV-2602-22556 -->

参考步骤只能表达一种路径时，可分别计算“执行自己的计划”与“覆盖离线参考计划”两种训练分数：前者用已执行步骤相对计划和总动作的比例，后者按语义匹配到的参考步骤相对参考规模和总动作的比例，再取二者最大值。这样让替代路径不必被低参考分稀释，效率分母也不同于直接奖励步骤数量。[Search-P1 v1](https://arxiv.org/html/2602.22576v1)的去单轨控制支持这一局部分支，但 self-consistency 不是真实 outcome，取 max 更不保证防 gaming；gold-conditioned teacher、离线拒绝/vote、语义 matcher、训练 judge 与多rollout均付费，换小 evaluator 还出现 accuracy 反退。原文 soft-outcome 默认实现说明不一致，不据此认证唯一配置；参考/匹配不可靠或成本不合算时，保留 outcome-only、可靠 process verifier 或人工路径标注。<!-- source-family:SF-2026-ARXIV-2602-22576 -->

全错组也可先改变采样条件，再注入有界支持：带完整 gold solution 的 verifier 对原失败回答给 mistake report，仅在整组 negative 时让同一 policy 读取该报告重采。过滤掉显式引用报告/旧答的文本后，再移除条件输入，把所得 positive 与原 online negatives 混组，缩放其 advantage 并选择性施加 KL。[ContextRL v1](https://arxiv.org/html/2602.22623v1)中 standalone 文本并不使该样本恢复原 prompt 下的 on-policy 分布，也不保证过程 faithful 或无偏 credit。拒绝样本再经大 judge 同意的人工确认率只是选择条件 precision，不是所有过程 accuracy/recall；去组件仍有任务改善。Gold/teacher、额外反馈rollout、筛选和训练均付费，SFT/RL预算亦不全匹配；条件支持或 verifier 不可靠时，回到原完整 rollout、可靠 process verifier 与 outcome-only，不让所谓 information gain 代替独立验收。<!-- source-family:SF-2026-ARXIV-2602-22623 -->

题目自己的历史还能成为 reward state：用 asymmetric EMA 追踪同题成功率，仅对低于全局历史均值的题增加 detached entropy advantage 或更多训练 epochs；当前成功率超过自己的历史时，才以历史最短 correct response 为长度锚，对正确样本施加相对长度惩罚。[CEEH v1](https://arxiv.org/html/2602.22642v1)改变的是 difficulty 与长度的条件人口，不授真实难度或最短有效解；式11的 cosine 后半可负，式13又没有正确长样本惩罚的硬上界，不能继承始终鼓励 entropy 或 correct 永远高于 wrong 的保证。有限数学对照仍有 ME/强长度项反退，历史状态、rollout、entropy与调参成本都在；历史漂移、verifier失准或质量下降时，关闭这些辅助项，保留普通 outcome-only 与可靠短解支持。<!-- source-family:SF-2026-ARXIV-2602-22642 -->

### 一条回答包含候选集合时，Reward 还要分到候选

上面的 `G` 是同一 prompt 的多个**完整回答**；另一种结构是一条回答内部列出 `K` 个候选，用户只采用其中最好的一项。此时若集合 reward 是 `max`，把同一正 reward 复制给全部候选，会让无效候选搭便车。若每个候选都能由独立 oracle 评估，且集合效用对次序不敏感，可以按候选加入不同子集时的边际贡献（Shapley credit）把集合 reward 分给候选，再在各候选 token span 上实施更新；回答中的解释文本仍保留独立的 sequence reward。它解决的是**集合内候选归因**，不是替代 GRPO 组内回答比较，也不自动解决一个候选内部的 token/step 因果归因。

这种分解需要稳定的候选边界、可查询的子集效用与额外计算；若候选顺序影响效用、集合 reward 不是可分解的 `max`，或只有最终点击而没有候选级 oracle，直接套公式就失去原实验的计算与归因保证。短且同质的单回答任务继续使用普通 sequence reward 更便宜。作者的 Qwen3-8B、两张 GH200 及列出的推荐/生成任务只支持该受限集合场景，不证明一般 Agent 轨迹或开放偏好训练的收益。<!-- source-family:SF-2026-ARXIV-2603-29871 -->

一个较粗的 process 分支不逐步给分，而是请 teacher 定位失败 rollout 的首个推理错误，减少此前有效前缀承受的惩罚。它仍需先用可执行 verifier 检查 teacher 的参考解，参考解不可靠时回到 outcome-only GRPO。Cliff 的具体形式在错误前使用 `lambda * A_cor - b`、从错误处起使用 `A_inc - b`，其中 `A_cor`/`A_inc` 是组内成功/失败 advantage，`b` 是 token-weighted 居中项。主实验取 `lambda=0`，所以前缀得到的是 `-b`，不是必然为正的奖励或零梯度。

这种单边界监督节省密集标注，却把错误定位、step-to-token 对齐与参考解质量变成新的训练依赖。正确终点可能掩盖错误过程，错误步骤也可能被后续修复，不能把“首错后的推理全无价值”当成定理。作者对超长 rollout 把错误位置设为开头，并在正向前缀奖励过强时观察到长度增长；这支持联合审计 truncation、长度和最终正确率，不证明杜绝 reward hacking。可靠终局检查且过程定位误差较大时，原来的 sequence reward 仍更稳妥。[首错边界监督的公式与限制](https://arxiv.org/html/2609.02817v1)

### 生成器内部状态也可能成为 Typed Credit Boundary

Token policy 的中间 action 天然是 token；diffusion policy 则在一次环境动作提交前经历多个 denoising states。只把最终 return 复制给全部内部 step，等价于假设这些 partial actions 对最终可执行动作贡献相同；在长 denoising chain 中，这会隐藏早期方向选择与后期修正的差异。一个条件分支是把 denoising chain 展平为内部 MDP，用最终 environment action 的 Q estimate 训练 inner value，再经过 scale matching 将 inner advantage 与外层 GAE 合并。环境 verifier 仍拥有 terminal outcome，inner critic 只提出内部 credit，optimizer 消费校准后的 advantage，controller 才拥有最终动作提交权。

更细的 credit 可能改善长链归因，却新增 Q ensemble、inner value、尺度校准和墙钟成本；Q bias、scale mismatch 或内部 Markov 假设失效会沿多步放大。短 horizon、dense outcome 或 critic 不可靠时，应回退 environment-step credit，而不是把 diffusion 分支推广成 token GRPO 的统一替代。exact-v1 的消融和结果仅覆盖作者的仿真控制任务；return 提升与 success 并不总同步，也未证明真实机器人安全或任意 denoising scheduler 获益。

<!-- source-family:SF-2026-ARXIV-2609-12245 -->

不训练 inner critic 时，还可以付出额外采样成本，为中间状态构造终点效用代理：缓存随机去噪轨迹中的 latent，再从相邻状态分别以确定性 ODE 续到 clean endpoint，取两次终点评分的差作为 step increment。对符合局部与长期评分符号条件的 turning point，改用实际终局评分减该 ODE 续写评分的 aggregated reward，再在相同步骤的 rollout 组内归一。它改变的是训练 credit；同一边际分布不使 ODE continuation 成为随机后续的条件均值，符号选择也不识别唯一因果贡献或保证无偏 estimator。<!-- source-family:SF-2026-ARXIV-2602-06422 -->

这条分支用额外 ODE continuation、reward calls 与 latent 状态替代 learned value 的训练依赖；按正负 aggregated reward 平衡、丢弃小幅样本又会改变实际更新人口。主表保留 KL，而部分训练曲线去 KL，不能拼成一份安全或全成本保证；作者设置中 window 缩到四步、噪声过小或过大都有反退，较少 optimizer steps 也不等于较少 GPU 时间。clean endpoint 评分失准、续写偏差或额外预算不合要求时，保留 terminal reward、可靠 inner critic 或更完整的随机后续评价，而不把更密集的信号当作更准确的 credit。

## 为什么 GRPO 不是“无 Critic 的免费 PPO”

移除 critic 节省：

- Value model weights。
- Value gradients 与 optimizer states。
- Value forward/backward 和 value loss。

但每个 prompt 需要 `G` 个 rollouts：

```text
rollout tokens per prompt
= sum_(i=1)^G |y_i|
```

`G` 增大可以改善组内比较，却线性增加 generation、reward evaluation 和 sequence storage。长 chain-of-thought 任务尤其容易让 rollout 成为主成本。

因此 GRPO 的系统 trade-off 是：

```text
less learned value state
<-> more grouped generation and reward evaluation
```

### Policy-implied Value 是 Group Baseline 与 Learned Critic 之间的条件分支

Group-relative baseline 在同 prompt 能稳定产生可比较样本时省去了 critic；learned critic 则在跨状态 credit 需要泛化时提供更丰富估计，但新增一套模型与 stale-value 生命周期。中间分支可由当前 policy 与固定 reference 的 log-ratio 构造 policy-implied value，让 value signal 与 policy revision 同步，而不单独训练 critic。

它减少 value-model 状态，却没有消除估计偏差：固定 reference、系数 schedule 和 exact-KL 计算都进入 run identity，log-ratio 也不自动等于真实 return。组内比较充分时继续使用 GRPO baseline；任务状态丰富且估计误差可独立验证时 learned critic 仍合理。现有结果只覆盖作者的数学推理设置与理论假设，不证明该分支能在任意长程、工具或高并发 rollout 中替代 critic。
<!-- source-family:SF-2026-ARXIV-2606-20008 -->

另一个分支先承认完整序列的监督不能唯一识别每个 prefix 的价值：不同局部 score 分配可以得到相同累计 log-ratio，因而“序列偏好模型可用”不授权任意中途查询。可以另外训练一个 implicit prefix scorer，用终局 outcome label 约束归一化 prefix score，再对 old-policy 的高概率词表候选计算局部 TD 信号，同时保留实际采样分支的 GAE 与 outcome。这里 scorer 是新增的训练状态，不是上一分支无需额外模型的 policy-implied value；候选词表的比较也没有为未执行 token 创造真实的反事实终局。Verifier 继续拥有 outcome，scorer 只提供局部更新 proposal，policy、reference、old-policy candidate set 与 scorer refresh 必须保持版本绑定。

它以额外 scorer 训练、候选前向与在线 refresh 换更细的更新接口，却增加局部/长程目标失配、在线估计漂移与词表截断偏差。Prefix BCE score 不自动是校准成功率，局部 TD 与单条最终结果低相关也不单独证明信号无用；应分别验 prefix 排序、实际更新和最终 task outcome。作者数学推理实验中早步/晚步权重适合不同选择目标，部分组合未稳定超越 GRPO，不能推所有候选更新都有收益或没有新增成本。组内结果可比、scorer 不稳或预算紧时，原 group baseline 与采样 GAE 仍应保留；需要独立跨状态价值估计时，显式 critic 也不因此被取消。<!-- source-family:SF-2026-ARXIV-2604-13197 -->

还有一条需要区分两个训练目标的 prefix 分支：在多个中间推理预算截点采样完成，得到当前 continuation policy 下的 Monte Carlo 可解性标签；BCE 只训练 confidence probe，policy 则接收终局答案 reward 与正确/错误前缀集合的相对 confidence margin。前者估计局部可解性，后者优化两类前缀的可排序差距，不是直接让 policy 最小化每步概率误差；probe 也不获得证明过程正确的权限。<!-- source-family:SF-2026-ARXIV-2604-23333 -->

多预算、多 completion 增加训练采样与 probe refresh 成本，标签又随 policy 改变。相对 margin 改善不保证绝对概率校准，校准改善也不保证任务准确率全面提高：[exact-v1 §3–4](https://arxiv.org/html/2604.23333v1)所测数学任务中普通 GRPO 的整体 accuracy 仍最高。应分别验 probe calibration、margin、终局 outcome 与 held-out compute selector；漂移、样本支持或预算不足时保留原 group baseline/outcome-only 更新，不让旧 probe 分数自动控制更多推理或发布。

Prefix 上增加 scorer 是序列时间轴上的细分；若模型对同一个待输出 token 反复运行共享 transformer，还存在内部计算深度轴。普通 terminal-loop loss 的反向传播已经经过前面的 loops，不能称它们没有梯度。另一条分支在每个 loop 的表示上读取同一词表分布，对 terminal-loop policy 采出的 token 使用加权的各 loop log-probability surrogate，仍由最终答案的二元 verifier reward 产生 group advantage，并仅在 terminal 分布上计算 reference KL。差额是增加直接 loss 入口，不是为每个 latent step 取得独立 outcome 真值；把同一 advantage 赋给所有 loops 也不识别真实因果 credit，不能据此宣称与 terminal policy expected-return 梯度无偏等价或不再需要正确性监督。

这类监督必须与循环次数、权重、sampled policy 和 vocabulary readout 版本绑定，并核实际 memory/packing 成本。[RLTT 的受限配置](https://arxiv.org/html/2602.10520v1)已有 per-loop logits，新增主要是保留多 loop log-probability；作者为适配显存将每 GPU token packing 上限减半到 8192，并用更多 mini-steps 补足原 batch，不是统一无成本。四 H200 上同 Ouro 2.6B、四 loops、140 updates 的有限比较支持该训练分支，但相同 emitted-token 上限不自动等于任意模型的 FLOPs 或端到端成本相等，各 loop 权重在不同任务也有取舍。显存不足、内部目标互扰或终局质量回归时，保留原 terminal-only outcome/group baseline；独立 prefix probe 与 learned critic 仍解决不同的估计问题，不因新增内部 head 被取消。<!-- source-family:SF-2026-ARXIV-2602-10520 -->

## Group Size 改变什么

较小 `G`：

- Rollout 成本低。
- Mean/std 估计噪声大。
- 二值 reward 更容易全相同。

较大 `G`：

- 更容易产生正负相对样本。
- 统计更稳定。
- Generation、memory 和 straggler 成本更高。

最佳 group size 依赖 policy 当前成功率。若任务成功率接近 0 或 1，即使增加 `G`，有效 mixed-outcome groups 仍可能稀少，需要调整 curriculum、reward 或任务分布。

调整 curriculum 还要问相邻难度能否传递学习信号，而不只是各题是否出现过成功。在一个受限的群作用状态追踪模型中，固定 MLP 已拥有单步原子技能，单层 attention 仅靠正交位置标识关联操作；从零初始化的 `Q` 出发，只更新 `Q`，对各长度均匀混合并使用精确期望的长度归一 terminal-reward 梯度。此时过大的长度比例仍可产生长平台期，适中的比例则使较短 horizon 的更新为下一 horizon 提供 gradient relay。这个条件分支依赖有限非交换单群的单纯传递作用、随状态数增长的指定长度范围及步长，不是从成功率直接推导真实 LLM 的课程阈值。作者的 `Z96` toy 实验改用交换群并加入 EMA baseline 与 entropy 项，提供受限现象而非同一理论前提的验证；其终点正确率也不认证全轨迹正确。实践仍要分别观测各难度的学习进展、稀有成功与实际梯度估计噪声，计入更多难度层的采样/验证预算；原子技能、语义上下文或规划方式同时变化时，保留随机 coverage 与静态 curriculum，不把“混合更平滑”当作普遍最优。<!-- source-family:SF-2026-ARXIV-2602-14872 -->

这里还要把“能够形成相对更新”与“覆盖同一题的稀有正确解法”分开。固定 prompt，若 `G` 条回答独立同分布、reward 为二值，记总成功概率为 `mu`，某个指定稀有正确轨迹集合的概率为 `tau`（`0 < tau < mu`），则 mixed-outcome 概率为 `1 - mu^G - (1-mu)^G`；既有正负结果、却未采到该集合的概率为 `(1-tau)^G - (mu-tau)^G - (1-mu)^G`。因此相同成功率可以隐藏不同的正确解法分布：组内 reward 有方差，只证明本组存在比较信号，不认证稀有正确模式已经获得正向样本。这是同题 trajectory coverage 的问题，不能用增加稀有题的 curriculum coverage 直接替代。

当目标同时包含单次正确率和探索覆盖，验收应分账报告 pass@1、固定生成预算下的 pass@k，以及稀有正确轨迹的覆盖代理与构造成本；较高 pass@k 也不能独自认证真实解法多样性。依据基础模型 likelihood 或聚类定义的“稀有”依赖所选模型、候选池和标签，额外采样、验证或 judge 调用必须计入预算。上述概率只描述固定 policy 的 iid 二值采样，不证明共享参数的长期训练必然收缩或保留某个模式；只需可验证单次正确率、代理不可靠或采样预算有限时，普通组内比较仍是直接基线。
<!-- source-family:SF-2026-ARXIV-2602-06717 -->

只按 reward variance 选题在二元 verifier 下很直观，却会把“偶然不稳定”与“位于当前能力边界”混在一起。
selector 可以联合 success rate、同题输出分歧与学习到的难度，优先分配一次性 RLVR 预算；curriculum
owner 只决定采样 proposal，verifier 仍拥有 outcome，trainer 才提交参数更新。它用额外 selector 训练和
周期评测换更密的有效 credit，却会产生 selection bias、冷启动误判和困难长尾遗失，因此必须保留随机
coverage slice 与静态采样 fallback。作者结果只支持其 one-shot 设置，不证明该 selector 对所有 policy
阶段优于 reward variance。
<!-- source-family:SF-2026-ARXIV-2605-01823 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11235:start -->
Curriculum selector 还可以从当前 policy 的近期输出中学习“哪些题现在值得分配更多 rollout”。条件分支让同一 policy 读取带 evidence 的 in-context judgment，生成难度/收益 proposal，再以 Top-B 方式分配训练预算；self-judgment reward 只负责 curriculum sensor，外部 verifier 仍拥有 outcome truth，trainer 只消费冻结后的选择结果。这样比静态难度表更贴近能力边界，却会形成 policy 与 selector 的耦合反馈。

该路径增加 ICL evidence 构造、解析、self-bias 与选择偏差；移除 ICL evidence 时作者实验出现 87.6% parse failure，说明 sensor 并非无上下文可用。最高 67% wall-clock reduction 和约 3.9% overhead 只属于作者 workload，不能外推生产集群。Evidence 缺失、selector 漂移或关键覆盖下降时，应回退 random coverage slice、static curriculum 或 external selector。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-11235:end -->

### 同步 Group Size 也可以由 Straggler Risk 有界调节

<!-- semantic-body-binding:SF-STRAGGLER-AWARE-RL-GROUP:start -->
固定 `G` 在设备、长度和环境延迟稳定时最容易复算，也保持每次 update 的统计口径一致；但同步 on-policy rollout 的完成时间由最慢样本决定，长尾一旦变化，继续扩大组会用更多等待换来很少的新比较信息。受约束的 controller 可以从已完成样本更新 straggler-time posterior，在保持同步与当前 policy identity 的前提下，选择仍能满足风险上限的 group size。Scheduler 拥有采样数量 proposal，group builder 冻结最终 membership，optimizer 只能消费完整、同版本的组，不能为了吞吐接纳过期或残缺 trajectory。

动态 `G` 用较低 barrier 等待换来组间方差、controller 误差和 measurement drift；posterior 失准还可能系统性缩小困难任务的样本数。因而需要同时报告 group-size 分布、完成时间尾部、mixed-outcome rate、gradient variance 与最终质量，并保留静态 `G` 作为低方差 fallback。作者证据只覆盖其同步 on-policy workload、控制器和实验分布，不证明所有环境都能在不改变学习动力学的情况下提速。
<!-- semantic-body-binding:SF-STRAGGLER-AWARE-RL-GROUP:end -->

### Mid-rollout 提前停止只能取消低边际信息轨迹

固定生成完整 `G` 条 response 保持 group membership 简单，也不会因为中途预测而偏向某类答案；当长 rollout 成为主要
成本后，可以先生成统一 prefix，再比较同组轨迹是否已经明显分化。若前若干步的编辑差异仍很低，继续生成往往只是在
复制同一探索路径；受约束的 rollout controller 可以终止这部分低边际信息轨迹。Controller 只拥有取消 proposal，
group builder 必须冻结最终 membership 并记录 prefix、终止原因与 sampling identity，optimizer 只能消费满足当前
objective 合同的完整组，不能把缺失 suffix 当成零 reward。

这种 selective rollout 以更少生成 token 换取 early-divergence predictor 的 selection bias：答案可能在后半程才分叉，
表面相似的 prefix 也可能隐藏不同 latent path。验收要同时比较 token saving、mixed-outcome rate、最终质量、被取消轨迹的
反事实完成结果和不同长度切片；阈值失配或任务具有 late branching 时回退完整 rollout。现有证据只支持论文使用的
prefix 长度、编辑差异指标与任务分布，不证明任意 reasoning workload 都能安全提前停止。
<!-- source-family:SF-2026-ARXIV-2605-05802 -->

#### Exploration Signal 只能控制采样，不能充当 Outcome Truth

仅用 prefix 相似度取消低分化轨迹，在早期表示变化可预测后续分叉时很有效；更一般的 Agent rollout 还可能需要先改变思考路径，下一 turn 才决定重采或取消。两层 controller 因而可以让 token 层只提出 bounded thinking intervention，让 turn 层只提出 resample/cancel；group builder 保存触发分数、阈值、policy/environment revision 与最终 membership，optimizer 不把缺失 suffix 或重采样副本当作独立证据。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02178 -->

这种控制减少空转，却以额外 token、selection bias、estimator drift 与 on-policy staleness 为代价。Uncertainty 不等于错误，低变化也可能表示已经收敛，late reward 还可能让提前终止系统性丢失难例；校准不足时应回退完整 rollout 或静态采样。作者实验只覆盖 WebShop、ALFWorld、Search QA 与披露配置，不支持把触发分数当成跨任务 verifier。

在构造 group 前按 confidence 筛选 prompt，还多出一层人口责任：对冻结 behavior/selector 的二值 mask $w(x)$，用真实保留率 $\beta=E[w]$ 归一的 $w/\beta$ 更新，优化的是筛选后人口，而不是原 prompt 分布。若 surrogate 统一有界，二者目标差可受 $2L_{\max}(1-\beta)$ 限制，但该界不保证实际 SGD 回到原目标最优，clipping/KL 也不自动提供所需界。[VI-CuRL 的条件分析](https://arxiv.org/html/2602.12579v1#S4)还出现 $1/\beta$ 放大的条件方差与 mask/均值项；只有相应 gradient envelope 和 numerator 缩减足够，才可讨论降方差，低 entropy 本身不满足这些条件或认证 reward truth。实际 minibatch quantile、ties 与估计保留率不等于固定 population mask；应记录它们与 behavior 版本，并以相同 prompt/rollout 预算分别测 bias 和 variance。confidence 由整组回答计算时，被拒生成、统计和退火仍有成本；筛选漂移、难例遗漏或费用不合算时，保留随机/静态选择、完整人口采样与独立 verifier，不把筛选器当成 outcome authority。<!-- source-family:SF-2026-ARXIV-2602-12579 -->

### Group-relative Gradient 不是独立样本均值

把同一 prompt 的 `G` 条 response 当成普通 minibatch，容易误以为增加 `G` 只是增加独立样本数。实际上每条
response 的 advantage 都使用同组统计量，样本经由共同 baseline 相互耦合；改变或删除一条 response，会同时改变
其他 response 的更新权重。因而这里的统计对象更接近对一组样本定义的对称核，而不是 `G` 个独立 gradient 的简单平均。

这个视角仍须指定 estimator，而不能直接授予章首全部 clipped objective 相同的理论身份。[受限分析](https://arxiv.org/html/2603.01162v1)使用当前 policy 下条件 i.i.d. 的完整回答、leave-one-out reward baseline 和未裁剪 score-function gradient；含自身的 group mean 要经 `G/(G-1)` 重标度才对应此中心化对象。Reward 标准差归一、旧 rollout 的 importance-sampling reuse、clipping 与 KL penalty 均不在该推导内；相关采样或这些实现分支需要另验，不因都叫 GRPO 就继承无偏性或 oracle 最优。

归一化与退火联用时，还要检查它是否隐式改变了多项 objective 的相对权重。一个[Gaussian logit-noise 的受限对照](https://arxiv.org/html/2610.02486v1)在固定 logits、零和子空间的独立 Gaussian draws、floored bounded/Lipschitz score 下，分别核对未归一的含自身 baseline、无 std 的 leave-one-out 与 pathwise gradient；LOO 的无偏性不传给依赖同一组样本的 std 分母。小噪声下若局部 reward spread 随 `sigma` 近似缩小，再除该 spread 会放大 score-function 项相对固定 CE 的尺度；这里约 `1/sigma` 是局部解释，不是任意 reward 或 token-level GRPO 的定律。<!-- source-family:SF-2026-ARXIV-2610-02486 -->

应在相同 checkpoint、batch 与 noise 下用 matched gradient probe 比较方向、尺度与方差，再对照去归一/LOO/pathwise 分支及 held-out 质量。作者 probe 支持该配方的相对 CE 权重随退火增加；每步都触发 global clipping 时，影响是更新方向，不可称步长同比增大。探测与对照增加训练成本，且更低 estimator variance 不自动意味着更好泛化；若该诊断不适用或无质量退步证据，保留既有 normalized objective，不把小编码器的 typed-decision 结果外推为所有 LLM RL 配方失效。

在这个受限对象及有界 reward 条件下，固定每次更新的采样数 `N=B*G`，增加同题回答数会减少高阶组内残差，却也减少独立 prompt 数并放大 prompt 异质性项；一阶条件内方差项在该预算下不随 `G` 单独下降。因此 budget 选择必须并列估计 prompt 间与同题内变化。它付出额外统计与探测成本；平滑性、PL 等进一步条件下的最优 group size 只是所分析上界的取舍，不是实际 clipped LLM 训练的通用最优值。条件或估计失效时，保留原实现，在匹配总 rollout 与质量目标下做有限 `B/G` 对照。

U-statistic 视角把这层依赖显式化：先定义组内相对比较产生的 gradient kernel，再用 Hoeffding decomposition 区分
一阶有效信号与高阶组内交互。它解释了为什么 group size 会通过有限样本 variance decomposition 改变 MSE，同时影响
有效 prompt 数和 rollout 成本，也提醒实现不能用独立样本公式直接估计不确定性。收益是能够在明确的
bounded-reward、smoothness 等假设下分析 MSE
与有限样本行为；代价是统计估计和 batch 设计更复杂，而且理论假设并不自动覆盖 non-stationary judge、相关采样或
distributed rollout 的版本漂移。

这不是要求所有 GRPO 系统都采用新的 estimator。组很小、reward 简单且只做工程回归时，现有 group-normalized
实现仍是合理 baseline；需要比较 group size、报告 gradient variance 或据此分配 rollout budget 时，才必须把组内依赖
纳入 measurement contract。现有证据证明论文设定中的统计结构与实验趋势，不证明某个固定 `G` 对所有模型和任务最优。

<!-- source-family:SF-2026-ARXIV-2603-01162 -->

当 rollout 很贵、group 很小时，系统可以把当前小样本统计与一个跨任务 value prior 做 shrinkage，再按“多采一次
能减少多少估计误差”决定继续或停止。它位于无 critic 的 group mean 与完整 learned value function 之间：

```text
fresh group measurement + versioned generalist prior
-> bias / variance trade-off
-> marginal-value stopping decision
-> more rollouts or policy update
```

收益是用 bounded bias 换较低方差和自适应 compute；风险是 policy、domain、reward 或 prompt 漂移后 prior
过期。Support buffer、prior checkpoint、policy version 与 reward definition 必须共同标识 freshness，并在
失配时增加采样或回退到标准 group mean。V0.5 的数学与作者 math-RL 实验支持这一折中在其 contract 中成立，
不证明极小 group、non-stationary judge 或多域 rollout 都会收敛。Rollout 便宜或 prior 不可信时，标准 GRPO
仍更无偏；dense state value 可可靠学习时，同步 critic 仍是有效分支。

跨 prompt 的 prior 也可以来自训练流本身，而不是额外的 value model 或停止控制器。一个[在线统计分支](https://arxiv.org/html/2602.05165v1)在初始化时建立两份全局累计状态：全部 response reward 与每个 group 的 mean；每批先并入当前样本，再按全局 reward variance 除以 group size 与 group-mean variance 的相对大小，决定 local group mean 向历史 global mean 收缩的权重，最后仍在当前 batch 内对 advantage 做 center/scale。这里的统计人口与更新顺序属于 objective identity：不是每个 prompt 的 variance、每个 topic 的独立 bank，也没有 learned critic 或 adaptive stopping；当前 batch 同时参与 prior 与 advantage，存在 self-coupling，raw group-mean variance 也包含采样噪声，不能直接当作潜在任务难度的纯方差。全错 group 在 raw baseline 层可能保留跨 prompt 的相对信号，但不保证最终 normalized advantage 总为负或梯度必非零。工程上应把 policy、reward definition、累计人口、更新顺序与统计状态版本一起保存，并测量长期累计在任务漂移后的陈旧性；这些是部署 guard，而不是作者已验证的任意漂移收敛保证。Gaussian MSE 与独立性分析只在其假设下成立，topic clustering 又增加标签和准备 rollout，有限实验也并非所有 group size 或任务都优于原基线。历史支持集不相容时，保留 local group mean 分支，不能由省掉 critic 推出免费或普遍稳定。

组采样还暴露了另一类浪费：不是所有 prompt 都同样容易产生有区分度的 group。均匀重采最简单，也最少引入
selection bias；但当少数 prompt 曾经产生高方差或 mixed-outcome group 时，把下一轮预算继续均匀分给已经稳定
全对或全错的 prompt，会降低有效 gradient density。一个受限分支可以记录近期的 prompt-level signal，只重放
高信号 prompt，并且**始终用当前 policy 重新 rollout**：

```text
uniform prompt sampling
→ versioned prompt-level outcome statistics
→ select recent high-signal prompts
→ current-policy rollout produces a new group
→ ordinary GRPO scoring and update
```

这里复用的是 prompt admission evidence，不是旧 trajectory、旧 log-prob 或旧 advantage。Prompt replay owner
需要绑定 policy/reward revision、统计窗口、选择阈值与采样概率；旧 response 只能解释“为什么再采一次”，不能
直接进入 on-policy update。它用较高的 sample efficiency 换取 curriculum bias：困难或偶然高方差的任务可能被
持续放大，尚未产生正信号的任务反而被饿死；policy 演进后旧 signal 也会迅速过期。因此应保留 exploration
quota、重要性监控和均匀采样回退。任务信号近似均匀、统计不稳定或分布覆盖比短期吞吐更重要时，标准 prompt
sampling 仍更合理；现有证据只支持 early training-time / sample-efficiency 改善：作者曲线随后更早 plateau，
最终接近 baseline，cooldown ablation 又受 spurious reward 干扰且没有多 seed 显著性验证。它不证明最终质量提升、
稳定超过 baseline，或任何 GRPO workload 都应重放高信号 prompt。
<!-- source-family:SF-2026-ARXIV-2603-21177 -->

失败轨迹还可改变新 rollout 的条件，而不只决定原 prompt 值不值得重采。一个 error-branch 分支将刚发生的失败与诊断反馈放入 corrective context，再由当前 policy 产生新的 group，继续用 tool/outcome verifier 作 GRPO；新错误优先的 LIFO buffer 保存的是重采条件，不把旧 response、log-prob 或 advantage 冒充当前样本。训练期 error simulator 若读取 ground-truth tool call，其反馈属于 privileged supervision，不能假定部署时同样有 oracle。反馈、policy revision、buffer 条件和 verifier 需共同标识，额外诊断与 rollout 均付费；偏置选取失败状态、反馈错误和条件分布变化，也不会因 LIFO 较新就获得严格 on-policy 或无偏保证。反馈不可核、成本过高或部署观测与训练特权失配时，回退普通 outcome group、可靠环境反馈与均匀探索。[有限多轮工具实验](https://arxiv.org/html/2601.15625v1)支持该训练分工，不签发通用 recovery、安全或等 compute 优势。<!-- source-family:SF-2026-ARXIV-2601-15625 -->

Prompt 重采改变的是组从哪里来，另一条分支改变同题组内的 policy 条件：先用 expert 成功与探索失败轨迹预训练 quality-token 接口，再从固定 `P_sample(mode)` 为各 rollout 采样模式，以同一 outcome/tool-action verifier 判分并作组内归一。Quality token 只控制生成分布，不是真实成功标签；current/old ratio 也须条件化于同一 mode，而不是把不同模式的概率相除。部署使用 high-quality mode，与训练中的混合采样不是同一分布，更不保证每条轨迹成功。它增加轨迹准备、模式监督与采样身份维护；[受限工具调用对照](https://arxiv.org/html/2602.03025v1)中，未预训练该接口的混模式分支有反退，期望 reward variance 的条件性增加不保证每个 group 非零或原人口无偏，也不证明 entropy 是唯一原因。接口失配、verifier 漂移或准备成本过高时，应回退普通 GRPO 与明确的 prompt exploration。<!-- source-family:SF-2026-ARXIV-2602-03025 -->

条件也可由 policy 自己先选择，而不是由外部固定模式分布指定。例如先生成 thinking-language tag，再生成该语言轨迹，就把语言选择纳入行为与概率身份；探索期按当前 batch 中已出现语言的频次加 bonus，利用期则让某语言子组只要出现一个正确回答，其余同语言回答也取得子组成功 bonus。后者奖励的是选择条件的机会，不等于每条回答正确，必须与逐回答 verifier reward 分开，未采到的语言也不会凭频次奖励自动获得支持。[有限数学对照](https://arxiv.org/html/2602.21887v1)支持先探索再利用的局部分支，但 cold-start 会损害原准确率，普通利用 reward 在部分切片反而优于特殊子组 bonus；语言遵守后的条件准确率与把不遵守计错的完整分母不同。Teacher 生成、语言识别、LoRA、额外轨迹与验证都付费，同步数不等完整同算力；tag 失配、稀有语言支持不足或任务回归时，保留固定 English、外部明确模式与普通逐回答 outcome 更新，不把多语 entropy 或子组成功签成真值、无偏梯度或通用探索优势。<!-- source-family:SF-2026-ARXIV-2602-21887 -->

## 从 GRPO 到 DAPO：后续演化不是单线版本升级

评估后训练收益还须确认策略**以哪一种推理模式**完成任务。混合 Think/NoThink 模型若在标称 NoThink 的输出中借用了原有 Think 行为，答案分数提高不等于无需推理也获得同等新能力。可固定任务、生成预算与模式接口，用内部表示干预和反向对照检查增益对既有思考方向的依赖；这增加干预假设与模型访问成本，也不能由一条方向捕尽所有泄漏。只需比较最终产品质量时，原始准确率仍有用；要宣称某个短路径训练方法更高效，则必须把模式遵守、长度/算力和增益来源分开。[三模型受控研究](https://arxiv.org/html/2609.28682v1)限于数学任务与所测后训练方法，不能推断所有 GRPO 分支都发生同类泄漏。
<!-- source-family:SF-2026-ARXIV-2609-28682 -->

把 reasoning RL 的演化写成 `PPO -> GRPO -> DAPO -> 下一个缩写`，会掩盖每一步真正替换的系统对象。PPO
用 learned critic/GAE 降低 policy-gradient variance，并用 old-policy ratio 与 clipping 限制更新；RLOO、GRPO
等 critic-free 分支则改用同 prompt 的多次采样构造经验 baseline。它们节省 value state，却把代价转移到
grouped rollout、reward comparison 与样本统计。到这里，问题已从“有没有 critic”分裂为至少四个控制轴：

```text
advantage baseline：learned value / leave-one-out / group mean-std
sample admission：固定 prompt batch / 按 mixed-outcome group 动态补样
loss reduction：response-equal / token-equal / fixed-budget normalization
update constraint：token ratio / clipped weight / sequence ratio
```

因此，后续工作不是在同一个旋钮上不断变优，而是在不同失败模式下选择新的 bias、variance、exploration 与
compute 组合。

### DAPO 把朴素 GRPO 的运行失败拆成四处修补

朴素理解是：GRPO 已经有 group-relative advantage 与 PPO-style clipping，只要扩大 rollout 就能持续提升。
但长 reasoning 训练会同时遇到 entropy collapse、全对或全错 group 的零梯度、长短 response 在 loss 中的
权重失衡，以及截断样本被错误惩罚造成的 reward noise。DAPO 保留 group-normalized advantage 与 token-level
importance ratio，却把这些失效点分别落到四个机制上：

- `Clip-Higher` 解耦上下 clipping 边界，为低概率正优势 token 的概率上升留下更大空间；它增加 exploration
  余量，也减弱了原对称 trust region 的保守性。
- `Dynamic Sampling` 持续补采并过滤全对、全错的零优势 group，使每批保留 mixed-outcome prompts；它提高
  有效梯度密度，也让训练分布变成由当前 policy 难度动态选择的隐式 curriculum。
- `Token-Level Policy Gradient Loss` 跨 batch 内所有有效 tokens 归一化，而不是先对每条 response 求均值；
  它避免长 response 的每个 token 被系统性降权，也会让长序列在总更新中占据更大权重。
- `Overlong Reward Shaping` 区分内容错误与因 generation budget 截断，采用过滤或软惩罚降低边界噪声；它
  稳定了长度边界附近的信号，也把长度先验显式写进 reward specification。

这四项合起来是一套 large-scale long-CoT RL recipe，不是“证明 GRPO 已被全面替代”的单一新定理。它没有
修复 verifier correctness、base policy coverage 或 deployment Evaluation；动态补样、长度 shaping 与
token reduction 还会改变实际优化的数据分布和目标权重。

补采昂贵时，难度 proposal 也可来自训练中已有的估计量，而不先为所有 prompt 生成额外 group。一个受限分支把当前行为策略 `π_old` 下 trajectory-balance 平方损失的 `log Z` 截距用于估计二元奖励均值：固定 `θ` 并对截距达到条件最优时，`p_old = β log Z* − β KL(π_old || π_θ)`；有限 `Z_φ` 拟合与省略 KL 后得到的只是有偏代理，不是精确 accuracy，平均 KL 小也不保证每个 prompt 的误差。它按估计的中等难度选 fresh prompts，并把已成功 trajectory 按估计误差优先 replay，因而须分开保存估计器、reward、来源 policy 与年龄，成功-only buffer 不代表原完整人口。[PACED-RL 的有限对照](https://arxiv.org/html/2602.12642v1)支持局部 rollout/质量取舍，不授权无偏 scheduler、语义多样性或全任务支配；预计算 embedding、估计器训练和 replay 仍需计费。估计漂移或支持失配时，保留均匀 fresh prompts、原 mixed-group 补采与独立 verifier，而非用归一化项替正确性签字。<!-- source-family:SF-2026-ARXIV-2602-12642 -->

Dynamic Sampling 的前提是补采成本可接受，并且丢弃全对/全错 group 不会抹掉稀疏但重要的失败模式。若 reward 有可信的上下界、长 GUI rollout 昂贵且 collapsed group 本身仍包含训练信号，另一个分支可只把固定 anchors 加入均值与方差统计，而不把它们伪装成新 rollout：全错组的真实样本得到同号负 advantage，全对组得到同号正 advantage，再用 variance-aware tempering 限制不同 group 的更新尺度。

这种做法保留 group，却没有创造组内排序；它以 boundary-dependent bias、超参敏感和共同错误放大换取稀疏 reward 下的非零更新。reward 边界不可信、信号稠密或补采便宜时，普通 GRPO 或 Dynamic Sampling 仍更清楚。`arXiv:2605.01208v1` 只在作者 Qwen3-VL-8B、GUI/RFT 数据与奖励合同下支持该 estimator 分支；Trap success-rate 数字不能外推到其他环境，abstention SFT 也不证明模型知道事实是否成立。

<!-- source-family:SF-2026-ARXIV-2605-01208 -->

另一种稀疏监督约束是：扩大同题 rollout 搜索也找不到命中，整个全错组既不能按原组内相对奖励更新，持续补采又昂贵。若任务本来有可验证的目标输出与结构相似度，可以只在这种组里用目标派生的正 anchor 替换最低信息样本，先恢复正负边界，再从组中选最强正例和最难负例进入 actor 更新；结构分数只负责组内挑选，不冒充最终 task reward。这样搜索宽度 `G` 可以保留对稀有命中的探索，而 old/reference log-prob 与 actor 反传只处理常数个选中样本。它既不同于丢弃全错组的 Dynamic Sampling，也不同于仅用固定边界改变统计量却不制造组内排序的做法。<!-- source-family:SF-2026-ARXIV-2604-22169 -->

这项分离并非免费或无偏：目标派生 anchor 与自采样 rollout 的 producer 不同，边界样本筛选改变实际更新分布，不能把修复后的组仍称为原样 on-policy 样本。必须分别记录原 rollout、插入样本、选择规则与 behavior-policy 身份，并联验命中质量、生成搜索成本和 actor 更新成本。受限的离线单目标 next-item 推荐实验在 64 张 Ascend NPU、Qwen3-8B、`G=32` 下报告 step 时间 `371.54→77.00s`、actor 更新时间 `211.04→12.71s`；这不是通用 RL 或端到端服务加速，强 backbone 上修复还可能退步。没有可靠目标输出、结构语义或值得付费搜索的稀疏奖励时，普通 GRPO、Dynamic Sampling 或保守跳过仍是更清楚的选择。

另一条分支不丢弃全错 prompt，而根据当前 group 的结果分流训练目标：全错时使用多教师 demonstration 的 SFT，mixed-outcome 时继续 GRPO 并混入同一 on-policy group 中成功/失败回答的对比 loss，全对时跳过更新。它把“缺少可区分奖励”与“已经饱和”分开，也把监督注入与相对强化放入同一轮训练，而不是认为所有 prompt 都应加大 rollout。多教师 sampling 与有界 contrastive coefficient 是实现选择，不等于监督无偏或梯度方差必然更小。

尤其当 GRPO 与对比项共用 rollout 时，两项梯度通常相关，方差账本不能省去 covariance；教师共享错误也不会被增加教师数自动消除。[DYPO 的受限证据](https://arxiv.org/html/2604.08926v1)在两个 Qwen reasoning 配置中给出分项消融，但某任务的难度分流仍有退步，八次在线采样和教师生成都要计成本。奖励足够稠密、教师缺乏可靠答案或目标无需注入新监督时，普通 GRPO、动态补样和分阶段 SFT→RL 仍更容易控制；不能把该条件分支写成任何负载上的严格 variance 改善。<!-- source-family:SF-2026-ARXIV-2604-08926 -->

也有不添加 teacher 或 anchor 的条件分支：以 old policy 对已采 response 的平均 NLL 为代理，按组均值与单条 NLL 的比值给权重，再对正确/错误分别 clamp；全对跳过，全错改为统一负 advantage，mixed 仍用原组优势。[EGPO v1](https://arxiv.org/html/2602.22751v1)默认 clamp 后不 renormalize；可选重归一会破坏原正确权重至少1、错误至多1的方向界，组均权1也不保证梯度尺度。Sampled NLL 不是完整分布 entropy 或 correctness，统一负优势也不必有非零期望梯度，最终答案 verifier 不认证每个 token。有限任务有反退、八次评价不是八个训练seed，只有 old logs 已记录时才可能低增量开销；权重、支持或质量失配时，回到跳过、动态补采或可靠外部监督，而非把自组重加权当元认知真值。<!-- source-family:SF-2026-ARXIV-2602-22751 -->

过滤零优势组解决的是有效学习信号与补采成本，不承担已掌握行为的保持责任。一个不同的分支为有限 rollout 中全对的 prompt 保留专门的 consolidation loss，对相邻更新在所采 token 上的 log-ratio 越界施加 hinge，同时另行调整 majority-correct 组的难度权重。它把“这里没有 outcome 区分信号”与“更新其他 prompt 后这里仍应稳定”分开；全对分支须显式处理，不能把零标准差继续代入普通归一公式而期望自动成立。<!-- source-family:SF-2026-ARXIV-2604-16972 -->

所采 token 的漂移惩罚不是未来正确率保证，有限组的 mastery 判断和共同 checker 错误也可能锁住错误行为。原文取消 dynamic filter 后同时改变输入分布与补采成本，不能将全部增益唯一归因 hinge 或称为全 compute 匹配；14B 的 AMC23 pass@8 与重加权消融也有反向切片。保持分支增加统计与训练工作，任务漂移时须重新验收；若全对判断不可靠、稀疏失败被遮蔽或收益不足，动态补样、普通 GRPO 与独立回归测试继续合理。<!-- source-family:SF-2026-ARXIV-2604-16972 -->

处理全零组之外，目标函数还可以改变不同prompt的成功边际权重。以成功概率P为对象的q-loss产生与P^−q相关的跨样本权重；GARL的prior-rollout/RLOO与likelihood梯度路径，和PAFT的posterior-resample训练不同，不能将这种目标变化解释为只调学习率或再补一个全零组。q、采样分布、reward与估计规则都应进入训练identity。

难样本权重增大也会放大奖励错误和有限采样偏差，P难估计时更不自动解决cold start。受限Tsallis结果的连续flow结论依赖score-norm等假设，不是Adam收敛速度保证；q=1的latent marginal目标也不等于所有teacher-forced SFT。小模型单seed、错误标签记忆与peak后collapse限制外推；奖励失准或估计不稳时，保留普通GRPO、可靠监督与独立held-out回归。 [原文必要机制与限制](https://arxiv.org/html/2604.25907v1)。
<!-- source-family:SF-2026-ARXIV-2604-25907 -->

成功边际权重的比较还须指定用哪一只时钟。binary outcome 下，同题更新可拆为正确/错误 response 的平均 score-gradient 方向差与有效系数；对极低 success 的 prompt，普通 RLOO 或 GRPO 的有效系数可能较小，上调困难 prompt 是一个可试分支。但“少做几次更新”与“少花预算才取得一次稀有成功”不相同：一个受限 population 模型以 KL-proximal policy-distribution 更新和连续时间分析前者，再按 Bernoulli 稀有命中成本的 `1/rho` 代理重标时钟。即使使用相同的积分 weight budget，两种时钟也会偏好不同权重；这个代理不是实际 rollout tokens、硬件时间或 Adam/clip 的 compute 最优保证。<!-- source-family:SF-2026-ARXIV-2602-11128 -->

[有限从零 RL 与 post-SFT 对照](https://arxiv.org/html/2602.11128v1)中，低初始 success 的任务获益，而已 SFT 的任务没有普遍增益。有限 group 的经验 success 会有噪声，全错组给非零 advantage 也不证明期望方向正确或必有非零梯度，warmup 与边界处理仍需显式定义；原文 batch/clipping 配置不一致，不照录成统一运行合同。比较时应分账成功率人口、更新次数、实际采样/训练成本和 held-out 质量，再决定是否加权；稀有命中几乎不可得、verifier 不可靠或估计不稳时，保留普通 GRPO、可靠 SFT 支持与保守探索，不让理论时钟替代真实预算验收。

### DAPO 之后，各分支继续修改不同约束

Dr. GRPO 重新检查 estimator 本身：原 GRPO 的 group reward standard-deviation normalization 会按各 prompt
的组内 reward dispersion 反向缩放更新，而按实际 response length 归一化会引入长度相关权重。其做法是
去除这两项，并以固定 generation budget 作为 loss normalization，希望恢复更接近无偏 Monte Carlo 的
policy-gradient estimator。代价是原本由标准化吸收的 reward-scale 差异重新暴露给 batch composition 和
optimizer。它与 DAPO 的 token-level reduction 不是可以无条件叠加的两个“技巧”，而是在回答**一个 token、
一个 response 还是一个
固定采样预算应成为统计单位**。

配对的两类prompt还可以用各组优势的L1大小估计学习信号，再向共同target重权；这里平衡的是优势proxy，不是实际梯度向量。response长度、token reduction、score-gradient方向及相关性仍决定各域真正贡献，不能由两组L1相同授gradient等权。binary reward下该proxy可化成组准确率的函数，加入不恒定format reward后就不能自动继承同一式；动态过滤还改变实际消费人口。<!-- source-family:SF-2026-ARXIV-2512-24271 -->

这提供paired-domain权重的可审计接口，也增加成对数据生成/验证、采样和统计成本。group mean与sum的因子口径必须固定；同G时公共因子可在权重比中消去，不等于实现已核或全部实测无效。应分别测两域实际梯度、独立outcome及原人口utility；paired support、reward定义或proxy校准不稳时，保留原DAPO/GRPO与固定权重，不把局部合成视频收益外推为一般域均衡保证。

另一条更受限的分支直接改变接纳人口与更新目标：对已有推理能力的模型，用本轮固定的 `pi_old` 生成答案，只接纳可验证正确且未超过长度阈值的 response；再删去 group mean/std 与 reference KL，以 batch 最大 response 长度归一化正向 token log-likelihood。在 current policy 尚等于 rollout policy 的单次更新点，ratio 为一、clipping 不活跃，梯度可写成该二元权重下的 token CE；这不是原始 GRPO 在任意参数、任意 reward 或反复更新旧轨迹时都等价于 SFT。下一轮仍须刷新生成 policy，长度归一因子只对当前固定 batch 的更新参数为常数，不能当成整个训练过程的固定值。<!-- source-family:SF-2026-ARXIV-2602-13407 -->

这种 filtered on-policy CE 省掉部分 reward normalization 与 reference 工作，却将探索和监督交给当前 policy、correctness verifier 及 length admission；全错时没有正样本，错误 checker 或过紧长度也会消除有效学习支持。[受限数学对照](https://arxiv.org/html/2602.13407v1)中，改变采样温度或按实际 response 长度归一出现 collapse，不能把“有 verifier”推成 KL 的安全、保留能力或 trust-region 用途全部失效。作者只在 1.5B/7B reasoning distill、五项数学评价、H100 94GB 训练与 A800/vLLM 推理下比较刷新数据和成本，更新步数减少不等于通用总算力节省。支持不足、verifier 失准或分布保持重要时，保留原 GRPO 的相对信号/约束、可靠 demonstrations 与独立回归；第29章仍拥有普通 SFT 的监督接口。

CISPO 修改的是 clipping 位置：MiniMax-M1 报告把 importance-sampling weight 本身裁剪，而不是直接裁掉越界
token 的更新信号。这样可以保留更多梯度，但它已经改变 trust-region estimator 的语义，不能只沿用 PPO/GRPO
的 clip fraction 解读稳定性。公开证据目前首先是该技术报告中的算法与实验 contract，不应外推为所有模型、
reward 和 policy lag 下的通用优越性。

GSPO 再把约束单位从 token 移到 sequence：用 sequence likelihood 定义 importance ratio，并在 sequence
层执行 clipping、rewarding 与 optimization。它让 trajectory-level reward 与 update unit 更一致，作者也在
其 MoE RL workload 中报告了稳定性收益；但它不再与 token-wise trust region 等价，长序列、单 token
异常和 off-policy skew 都必须在 sequence contract 下重新测量。

Sequence ratio 的长度归一化与 loss 外层的长度权重是两个控制对象，不能把二者都概括为“消除长度偏差”。一个[长度重权分支](https://arxiv.org/html/2602.05261v1)保留 GSPO 的几何均值 ratio，却把每条已采样 response 的长度乘到外层 objective；在采样长度固定、未进入 clipping 的分支中，显式外乘长度可以抵消 ratio 求导产生的 \(1/L\) 因子。它改变的是每条样本对更新的相对权重，不把几何 ratio 变成整条 sequence 的 joint importance ratio，也不证明 estimator 无偏或所有长度偏差已除；进入 clip 区域后，仍须按实际边界检查梯度。因而 rollout artifact 要同时记录 tokenizer/EOS、截断与 overlong reward、ratio normalization、outer length weighting 和 clip identity，并把训练步数与实际生成 token、长轨迹显存及 GPU 时间分别计量。这些身份 guard 是系统推导，不是论文已验证的所有异步配置。有限数学/视觉实验有任务退步与一处 delta 数字不一致，较长输出本身也不证明推理能力提升；只有质量与总 token/cost 回归支持时才启用该分支，否则保留原 GSPO 的 sequence contract。

这条演化链的工程含义不是追逐最新名称，而是让实验与 checkpoint metadata 显式记录：baseline estimator、
sample-admission rule、loss denominator、ratio granularity、clip location、length treatment、reward/verifier
version 和 rollout policy identity。只有这些对象一致，两个“GRPO-family”实验的 loss、clip fraction、有效
token 数和最终能力才可比较；算法名称本身不是资产身份，也不是兼容性证明。

## Verifiable Reward 的优势与边界

数学 final answer、代码 unit tests 和格式检查可以减少 learned Reward Model 的主观误差。这类 reward 适合大规模自动 rollout，也推动了 reasoning-oriented RL。

但 verifier 仍是 specification：

- Final answer matcher 可能忽略推理有效性。
- Tests 可能覆盖不足或被 hard-code exploit。
- 格式 reward 可能压过内容正确性。
- 多个 reward components 的 scale 会改变总排序。

Policy 会优化 verifier 可见的目标，因此必须保留 held-out tests、adversarial cases 和独立人工检查。

视觉 caption 的完整与正确还需要两个不同的事实支持域：从 image 提出问题、只让 caption 回答，近似“图中信息有多少被覆盖”；从 caption 拆出 atomic claims、回到 image 检查，则近似“写出的信息有多少被支持”。[双向 reward 的有限对照](https://arxiv.org/html/2602.21655v1)显示只优化一侧可以损害另一侧，但两个分母都由可错的 query generator/judge 估计，并不是可枚举的全部图像真值。Query 多样性或 embedding 图覆盖不签发 completeness，同名 policy/judge 还可能共同遗漏；按回答方差改变 query 采样也会改变所优化的人口。应保存原 image、query/subclaim 来源、judge 与采样/混合权重，独立验收 coverage、grounding 和最终效用，而不把总 reward 当 caption 正确率。额外 query 生成、多次 judge、rollout 与训练均计费；双 reward 并非所有指标最优，按训练步的曲线也不是端到端加速。支持域或 evaluator 不可靠、净成本不合要求时，保留固定问题集、已校准单目标/参考监督及独立原图检查，不让更长 caption 或更多问题自行认证完整性。<!-- source-family:SF-2026-ARXIV-2602-21655 -->

可执行 database 的前后差分也不是完整 outcome oracle：目标在执行前已成立时，正确的幂等 no-op 可能因没有预期变化被判失败；错误对象上的变化又可能满足形式条件而被判成功。因此 scorer 需要同时保留 task/object identity、初始状态与实际作用对象，按目标谓词验收，而不能仅奖励“发生了变化”。结合 trajectory/state 的语言 judge 可以补查这两类错误，却仍是可错的互补 sensor；runtime 异常被修复只证明程序可执行，不证明 transition 或 reward 语义正确。固定独立 checks 与人工反例在 judge 不可靠时仍是基线。[AWM 的具体差分反例](https://arxiv.org/html/2602.10090v1)只支持其合成环境中的这一判断，不认证真实工具环境。<!-- source-family:SF-2026-ARXIV-2602-10090 -->

Verifier 本身由 policy 生成时，奖励 test 的通过率会诱使它只出容易通过的题。一个有外部测试锚点的分支先用 GT test 的部分通过比例衡量候选代码，再奖励 generated test 的 pass/fail 向量对该比例的区分信息，并用正 covariance gate 排除“更错的代码更易通过”的反向信号。Code producer 和 test producer 可以共享参数，却不能共享正确性自签权；有限 GT suite 仍定义训练锚点，测试信息量也只相对于当前候选人口。

先生成较大 pool、执行后按输入与行为列去重，可以改变 tester 更新人口，而不会消除完整 pool 的生成和 execution 成本。不同列不保证独立或完整语义覆盖，不能由去重推出任意有限样本的严格方差下降；作者的非退化16-test suite仍漏掉需要多步操作才能暴露的aliasingbug。实测 co-training 增加总GPU预算，matched steps并非matched compute；人口或锚点失配时保留fixed GT tests、独立adversarial tests和coder-only分支，最终代码仍须按部署任务重新验证。 [必要机制与反证](https://arxiv.org/html/2609.21208v1)。<!-- source-family:SF-2026-ARXIV-2609-21208 -->

执行反馈也可能以两个不同接口改变训练人口。[Dr. Kernel 的受限分支](https://arxiv.org/html/2602.05885v1)先重复测量同一候选，用几何平均运行时间之比筛查测量稳定性；这个比值接近一只表示重复测量接近，不是代码很快。另以生成kernel执行时间占全部算子执行时间的比例提供profiling shaping，并按该比例决定样本获准进入训练的概率：前者改变reward，后者改变sampler population，不能合并成吞吐或优化质量证书。生成kernel越慢也可能占比越高，因此正确性、已知hack排除、独立速度比较仍须各自验收。由此推导的工程记录应绑定算子、shape/dtype、设备、profiler、测量窗口与接纳规则，另计编译、重复运行及被拒样本成本；筛选后的有效轨迹若不再满足前述leave-one-out的条件独立与完整样本假设，也不能沿用其无偏结论。所测模型/KernelBench结果不证明生产任务普遍获益；反馈或速度人口失配时，回退固定独立tests、完整交互和已有库kernel，而不奖励更多执行覆盖本身。<!-- source-family:SF-2026-ARXIV-2602-05885 -->

昂贵环境还会改变训练样本的单位。代码每轮都要编译、执行与 profiling 时，可以把交互中反复出现的决策拆成单轮任务：从需求生成代码，以及读取已有代码和反馈后修复。训练支持集保存对应的输入、反馈来源与下一步验收结果；它训练局部技能，而不是把固定反馈前缀伪装成当前 policy 完整探索出的轨迹。[StitchCUDA 的受限分支](https://arxiv.org/html/2603.02637v1)以生成样本和“下一轮已正确”的反馈样本共同训练 Coder，降低反复完整交互的需求，也引入成功反馈筛选与部署状态分布不匹配的风险。

局部执行通过仍不能独自决定奖励：已通过正确性检查的候选还须排除已识别的 hard-code/copy exploit，再由任务、反馈遵循和优化覆盖等 rubric 提供有界 shaping。Rubric 是可错的训练判断，不拥有程序语义真值；同数据与参数的无 rubric 对照支持这个受测选择，却不是等总算力，额外 judge 仍有成本。完整多轮训练的节省主要来自交互耗时估算，不证明局部 surrogate 与整轨迹目标等价。未覆盖的新失败、反馈失真或真实效果无法验收时，应刷新交互样本、恢复完整 rollout 或保留固定 tests 与独立人工检查，而不让训练得分自行认证代码。<!-- source-family:SF-2026-ARXIV-2603-02637 -->

### Group Size 只有在样本身份独立时才代表探索

同一 prompt 生成 `G` 条 response 时，最简单的实现是复制整条请求；但如果复制也继承了同一个随机 seed，
多个 rollout 可能逐 token 相同。此时系统表面支付了 `G` 倍生成成本，实际只有一个样本，组内标准差与
relative advantage 也会退化。正确的 sampling contract 应把 `prompt_id`、`sample_id`、policy revision
和 seed derivation 一起保存：每个 sample 获得不同的稳定 seed，同时在 DP reshaping、重排和异步返回后仍能
复算同一身份。随机 seed 只拥有探索机会，不拥有 reward 或正确性；增加随机性也不会修复 base policy 从未覆盖的解。

稳定派生增加了 seed metadata 与跨 runtime 一致性要求，却避免“可复现”被误实现成“同组完全重复”。
若任务本身确定、只需要一次 greedy rollout，`G=1` 仍更便宜；需要 group-relative credit 时，则必须先验收
unique completion、有效 mixed-outcome group 和实际 sampling diversity，再解释 GRPO 的收益。UniRL #208
暴露的具体故障是固定 seed 使 `n=8` 退化成八份相同输出；该修复证明这一实现边界，不证明任何 seed 策略都能
产生高质量探索。

独立 seed 只能增加采样机会，不能决定组内 credit 是否还只表达 correctness。另一条[受限分支](https://arxiv.org/html/2601.09085v1)把 reward 与 response embedding 的组内相似度组合：以最高 reward 样本为起点，对后续候选扣除与已选集合的最大相似度，再用调整后的 reward 计算 relative advantage。它保留全部 response，而不是把重复样本过滤掉；即使原始 correctness 全相同，diversity 项也可能产生新的 advantage。因此这是改变训练目标的 reward shaping，不是恢复原 correctness 目标的有效样本数，原二值 reward 与 fresh mixed-outcome group 仍应保留为基线。<!-- source-family:SF-2026-ARXIV-2601-09085 -->

混合权重依赖原 reward 标准差，缩放 reward 会改变它，不能由无需手调 λ 推导尺度无关；这也未消除 embedding、reward 标度等配置。Embedding revision、归一化、选序与 reward scale 都属于可复算的目标身份。额外 embedding、组内比较、训练与评估选择成本必须计入；作者以事后峰值比较训练速度，动态采样预算也不同，所测1.5B配置在同一峰值步数的 wall-clock 并未更快，不能把 headline 降本归因于 shaping 本身。相似度失真、正确性退步或成本优势不能复算时，回退原 correctness reward 与独立采样，而不是把不相似自动当成值得学习。

奖励塑形之外，还可改变分支生成的位置。普通整条 rollout 为同一 prompt 独立生成完整回答；当规划格式把回答拆成若干段时，一个受限分支先为每个当前 prefix 扩展更多候选，再按语义差异保留固定数量的规划分支，进入后续正文后每个 parent 只续写一个 child。这样将探索预算集中到前置规划，但最终 group 带有展开、筛选和共享 prefix 的 ancestry，不再是未经选择的独立整条样本。Prompt、policy、规划段界、parent/child 与保留规则因此属于采样身份；沿所选 token 计算普通 likelihood ratio，不自动证明相对于原始独立 rollout 目标无偏。<!-- source-family:SF-2026-ARXIV-2601-09609 -->

分支选择与训练奖励还应分开：一个[有限开放生成对照](https://arxiv.org/html/2601.09609v1)仅在质量 sensor 超过阈值后，让组内 unique n-gram 与长度归一化的 diversity proxy 参与 reward；它不是语义正确性、真实创造力或独立样本数的证书。额外规划 SFT、teacher 改写、扩大候选池、embedding 选择和续写均有成本，相同步数与保留 group 大小不等于相同 token 或墙钟预算。作者局部消融中去掉 branching 的质量差很小，另一模型的部分 diversity 指标还低于普通 GRPO，不能将全部收益归因于分支位置。规划格式不稳定、选择偏差或质量回归时，保留普通独立整条 rollout、原质量 reward 与匹配预算的基线，不把“更不相似”自行升级为值得学习。

### Verifier Error 可能在组内相关

把每条 completion 的 verifier error 当独立噪声，会高估一个 group 提供的统计信息。相同 prompt、答案格式或
parser path 会让错误成簇出现；增加 `G` 虽增加样本数，却不一定按比例增加有效样本量，majority vote 也无法消除
共同偏差。训练与评估应按 prompt/answer-form 切片估计组内相关性，并重放不同 verifier 下的 advantage sign，
把“group 全对/全错”“verifier 共同误判”和“policy 真正没有区分能力”分开。

这要求额外的人类标签、成簇统计与 verifier revision，代价高于只报 aggregate accuracy；小规模、强确定性
checker 仍可先沿独立近似运行，但应把它写成假设而不是事实。`arXiv:2609.06386v1` 在 Qwen2.5-1.5B、
三个数学数据集的 24,998 个八样本组中估计 pooled correlation 为 0.530，并给出约 1.70 的 design-effect
effective sample size；作者没有分离 prompt difficulty 与 answer-form causality，也没有做跨模型 held-out replication，
所以这里吸收的是“必须测相关性”的 evaluation contract，不是通用相关系数。

不完美verifier也不等于无法训练。需要进一步区分每次重新抽取的随机翻转与固定、可被policy利用的系统性偏差，以及test、completion和整个group上的噪声：同一个aggregate错误率不规定advantage受到怎样的扰动。训练时用独立可信检查器同时测reward信号与按独立测试合同测得的task outcome，才能判断policy是否仍获得可用的方向；测试通过仍不等于完整程序语义正确。best checkpoint和最终checkpoint也要分开，不能用最高点掩盖后期退化。<!-- source-family:SF-2026-ARXIV-2604-07666 -->

这为“先有完美oracle才能做RL”提供有条件的反例，而非允许忽略checker错误。受限代码/推理实验在某些重新采样噪声下仍能学习，但结构间表现不同，多数条件只有单seed；模型verifier的precision和accuracy共同变化，也没有独立证明提高precision总比提高recall有效。固定偏差、分布漂移或可利用漏洞仍可能驱动reward hacking。可靠确定性checker继续是更易验收的基线，开放任务则需保留可信切片、错误结构与持续独立回归，而不是采用通用噪声容忍阈值。

总体错误率相同也不表示训练动力学相同。随机散布的 verifier error 往往先表现为有效信号变弱、学习变慢；
若 false positive 集中在某种可被 policy 识别的 trigger 上，policy 会主动提高对该区域的访问概率，使错误奖励从
外部噪声变成被优化目标。训练于是可能依次进入 delay、plateau，甚至 collapse。诊断项必须同时包含
`error pattern × trigger frequency × policy visitation × conditional advantage`，而不能只报一个 FPR。

这种诊断增加受控注入、oracle reward 与轨迹切片成本；当 checker 确定且攻击面很小，aggregate error 仍可作为
便宜基线。现有证据来自受控算术任务和人工错误模式，只证明不同模式可产生不同动力学，不证明开放式 verifier
的全部失效都可归入同一阶段图。无法辨认错误模式时，应冻结或回退到上一 verifier revision，而不是继续让
policy 用在线 reward 为 verifier 自证正确。

<!-- source-family:SF-2026-ARXIV-2605-02909 -->

<!-- source-family:SF-2026-UNIRL-208 -->
<!-- source-family:SF-2026-ARXIV-2609-06386 -->

### Verifier 也成为 Policy 时，必须分离更新与权威

固定 tests/checker 最容易复算，是发布门禁和高风险 regression 的 authority；但它无法持续覆盖当前 policy
新出现的错误。让独立 Test Policy 阅读候选并生成 assertions，再只保留能通过 ground-truth solution 或
独立 oracle 验证的 tests，可以形成 `code policy ↔ verifier policy` 的双策略闭环。失败案例还可进入带
版本和过期规则的 failure book，作为下一轮 test proposal 的状态。

这提高错误覆盖，也新增 collusion、oracle dependency、failure-memory staleness 与 sandbox nondeterminism。
Verifier 的 reward 不能只鼓励“让当前代码失败”，还要同时约束 validity；训练用 adaptive tests 也不能
替代独立 hidden tests。没有可信 solution/oracle、程序有副作用或 specification 开放时，固定人工 tests、
property checking 和人工 review 仍是 authority。

需要更易检查的呈现时，还可固定 solver 的答案生成能力，仅让 translator 改写其输出，并另用拿到 ground-truth 的 sneaky translator 构造有说服力的错误答案来训练 verifier。[DPVG v1](https://arxiv.org/html/2602.23248v1)把解题与检查接口拆开，但 faithfulness 只定义为最终答案一致，不是推理语义等价或人类可读性。理想 equilibrium 的 loss/策略假设不认证有限 RLOO 已 sound；role-conditioned score 归一还须处理零方差。有限测试保答案 accuracy，没有 human legibility 实验，比较的 CoT、loss 和训练轮数亦不同；solver样本、gold、两种translator与verifier训练付费。呈现丢证、判别失配或预算不足时，保留固定格式、原solver与独立外部核验，不能让说服力取得 correctness authority。<!-- source-family:SF-2026-ARXIV-2602-23248 -->

### Verifier 拥有方向，Privileged Teacher 最多调节幅度

Binary verifier 若是 correctness authority，privileged teacher 的 token signal 不应翻转 update sign；一种分层是
让 verifier 决定正负方向，teacher 只提供严格为正、受限的 token multiplier。它能提供细粒度 weighting，却仍会
改变 parameter trajectory，并新增 teacher bias、额外 forward cost、normalization 与 leakage surface。

Self-Distilled RLVR 的数学形式支持正 multiplier 不翻转 sampled-token direction，不证明 privileged signal “零影响”
或形成真实 causal credit。可靠 token/process verifier 可用时应优先直接监督；teacher 不可靠时 sequence-level
verifier reward 仍是安全分支。

#### Teacher 权重遇到负 Outcome 时必须 Reset

在 student on-policy trajectory 上，teacher/student likelihood ratio 可以把 teacher 的 token-level 分布用于调节正向 update，比无条件 KL imitation 更接近 RL；但 ratio 不能获得 reward sign 的 authority。若 outcome advantage 为负，继续按 teacher likelihood 重权可能保留一个虽像 teacher、却被环境判错的 action。因此一个条件分支只在正 advantage 上使用 clipped teacher weighting，负 advantage 重置为 ordinary RL；再以 sequence-level geometric normalization 保持样本内乘性权重的尺度。

这使 outcome verifier 拥有方向、teacher 只调节幅度，与“teacher 永远正确”的 OPD 不同。代价是额外 teacher forward、ratio clipping/normalization state，以及 teacher 在 student trajectory 上局部更弱时的误导；它也不扩大 student 从未探索到的 state support。Teacher 与 student 差异小、outcome reward 足够细或额外 forward 太贵时，普通 RL/OPD 仍是更简单分支。

专家轨迹也可以只扩充高不确定prefix后的探索，而不是接管完整回答。保留self-rollout池，在候选anchor后从expert suffix分叉，只有专家池确实提供更好outcome时才加入混合组；负advantage的专家分支停止shared prefix梯度，suffix仍按其采样身份更新。这样避免同一已复用prefix因专家suffix失败被反复惩罚，却没有取消self池或赋予entropy信号“知道自己不知道”的权限。混合prefix与suffix需要各自对应的ratio，不能把专家生成当纯on-policy样本。<!-- source-family:SF-2026-ARXIV-2604-09455 -->

它用专家查询、额外分支与分组/梯度mask状态换稀疏成功下的探索机会，也新增expert error、分支选择偏差与预算比较成本。[受限工具推理消融](https://arxiv.org/html/2604.09455v1)支持prefix梯度分流的重要性，但tree advantage在部分任务退步，增加expert比例也不单调；warm-up与后续RL的expert/self组成不同，不能只凭总成绩证明同预算收益。无可靠outcome、专家不适配或分支昂贵时，普通self GRPO、离线SFT或可追溯的局部teacher correction仍合理；工具副作用与最终commit继续由环境verifier决定。

#### 共享搜索树统计不等于合并各 Policy 的更新样本

与同一 prefix 后的专家 suffix 分叉不同，异构 policy 还可以用各自生成或修订的完整解答构成搜索树：节点有自己的 public-test reward，parent/sibling reward 提供共享 credit 参照，shaped reward 再进入树级归一统计。树结构与统计可以共享，但第 `j` 个 policy 的 loss 只消费由它生成的节点集合 `T_j`，likelihood ratio 仍属于该节点的实际 producer。训练 artifact 因而需要保留 producer、policy revision、原始 reward 与 shaping/normalization 身份；共享 advantage 参照不能把另一个 policy 的 tokens 自动变成自己的 on-policy 样本，解答树也不自动等同实际工具执行的共同 prefix。

这个分支以更多生成、public tests、选择器和逐节点扩展成本换协作探索，reward shaping 修改目标，树内相关与选择偏差仍需验收；不承诺无偏、原目标不变或普遍降低方差。`arXiv:2604.14564v1` 的 MARS² 使用 7,992 个筛选 code prompts，等 per-agent 样本和 update steps 不等 wall-clock，AReaL-14B 的 pass@8 也低于 RS²；单模型 shaping 曲线不建立全面优势。协作收益不足、测试不可靠或 producer lineage 无法保持时，应回退各 policy 独立采样、分别归一和独立更新；最终代码正确性仍由独立验收拥有。

<!-- source-family:SF-2026-ARXIV-2604-14564 -->

### 多阶段交互需要 Phase-specific Credit，而不是一个终局标量

工具 Agent 的轨迹可能包含探索、提出结构、执行与确认。只给 terminal reward 实现简单，却会让早期结构
选择得不到信用，甚至通过穷举或绕过中间约束获得高分。可以用显式 phase checkpoint 和 token masks，把
schema/evidence reward 只分配给相应动作，再让 execution reward 覆盖完整轨迹；中间 reward 只有终局成功
时才生效，可减少“找对对象但结果错误”的 shortcut。

Phase boundary、mask 与 reward coupling 都属于 objective semantics。它们会引入 boundary gaming、
标注成本和状态机复杂度，也不保证适用于不同工具协议。小 schema、短轨迹或 terminal verifier 足够密集时，
单一 reward 仍更透明。

#### Milestone 是中间 Credit 粒度，不是因果归因

Terminal reward 在短轨迹和唯一成功条件下最清楚；长交互只有最终标量时，已完成 subgoal 的学习信号会被后续失败吞没。
把 environment 可验证的 milestone 作为 segment boundary，并在 segment 与 trajectory 两个尺度计算 advantage，形成一种比整轨迹
reward 更细、比逐 action causal credit 更弱的中间分支。Environment/harness 拥有 milestone identity，group builder 冻结
segment membership，optimizer 只消费对应 credit。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06078 -->

### 语义 Segment 可以成为 Token 与 Episode 之间的 Credit Boundary

Token-level MDP 能精确描述每个生成动作，却会把长推理中的同一语义步骤切成许多高方差更新；episode-level reward 又无法指出哪一步改变了结果。中间分支先以可审计的分段器冻结 reasoning segment，再在 segment transition 上估计 value、advantage 与 importance ratio，最后把 credit 受约束地下发到段内 token。Segment owner 持有边界与版本，reward/verifier 持有结果证据，optimizer 不得事后改变分段来放大收益。

它以额外分段误差、边界漂移和 value 估计成本换更贴近决策步骤的 credit。步骤不可稳定识别、短回答或 token feedback 已足够密集时，token/sequence baseline 仍更可靠。现有 exact-v1 只支持作者的推理任务与分段设定，不证明语义段是所有 RL 的自然状态。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01327 -->

前述 milestone 分支能保留已完成阶段的信号，却会引入 milestone gaming、边界误标和相关 segment gradient；命中 milestone 也不证明该 action
因果导致最终成功。作者实验只覆盖 ALFWorld、WebShop、ScienceWorld 的离散 text action 和有限 steps，未覆盖 continuous
control、Multi-Agent 或无显式 transition 的任务。milestone 过稀时回退 terminal reward；过密、不可验证或因果要求更高时，
回退 critic、verifier 或 counterfactual credit 分支。

还有一种segment信用分支把**定位者**与**数值估计者**分开：judge只在成功轨迹中提出关键action段，不能直接给该段reward；runtime恢复段前与段后的完整history和environment snapshot，固定当前policy，从两端分别采样若干全新continuations，以终局成功率之差估计这段带来的条件增益。只有正增益作为有界bonus下发到段内token，额外continuations不混入原训练group。这样能保留原终局GRPO信号，同时避免把judge评价直接当credit authority。

固定policy、可恢复状态、确定的已执行segment、无中间reward等假设下，两端Monte Carlo均值差可以估计条件成功概率变化；这不认证positive-only、clipped实际更新的无偏性，更不是每个token的因果贡献。ProVer的[§3–5/Eqs2–4/Tables1–3](https://arxiv.org/html/2609.36178v1)包含预算匹配与不同judge对照，但局部judge也可使WebShop低于GRPO，某配置仍落后critic搜索；token额外成本小不等于wall-clock小。恢复不完整、continuation variance大、环境不可逆或judge不稳时，应回退终局reward、可验证milestone或更保守critic，不能通过把未来环境“模拟回来”绕过真实执行风险。<!-- source-family:SF-2026-ARXIV-2609-36178 -->

长程交互还可能把“完整对话历史”误当成 Markov state。历史易记录，适合短 horizon；但环境经过工具或
外部事件变化后，语言 transcript 可能既冗余又缺少 authoritative current state。若 runtime 能提供紧凑、
可验证的 environment snapshot，可以把 transition 与 action 分开训练：先根据前一状态与 observation 形成
下一状态，再由 policy 在该状态上决策，并把 credit 对齐到 state-action boundary。

```text
history-conditioned response
→ explicit environment snapshot
→ transition proposal + validation
→ action policy
→ next authoritative observation
```

这只在状态足够可观测、schema 可版本化且 transition error 可检查时成立。错误 snapshot 会让整个 rollout
在看似紧凑的状态上稳定偏航；部分可观察、随机或不可逆环境仍需 belief/history、reconciliation、approval
和 rollback。单篇 text-game 实验不能证明显式 Markov state 普遍提高真实 Agent 能力。

如果完整 transition 已由实际 rollout 提供，中间训练还可以不先估计 action 的终局 credit，而让当前 policy 从 `(state, action, next-state)` triplet 学习下一观察的预测，再接通常的 task RL。这里的局部 reward 比较预测文本与真实采样的下一观察：可用冻结 embedding 的距离阈值，也可对工具响应采用词面匹配，不能把两种 proxy 合并为语义真值。它与部署时确认 authoritative state 是不同责任，训练观察来自环境或用户模拟器也不等于预测已在真实环境发生。额外 rollout、过滤/SFT、重复预测与 embedding scoring 均有成本，弱基座可能学不动；参数变化较小不证明没有遗忘。预测代理与实际 task success 失配、环境不可复现或新状态支持不足时，应回退直接 task RL、显式状态校验或保留 history，而不是把预测得分当执行许可。<!-- source-family:SF-2026-ARXIV-2602-05842 -->

Binary terminal reward 的另一个边界是：当前 policy 若对一批任务几乎全成功或全失败，group-relative advantage 会退化。可以在 hard correctness gate 之外，引入由 task geometry 定义的离散 proximity zones，让 near-success trajectory 获得有序但受限的 shaping signal：

```text
terminal correctness
+ bounded, discretized progress zone
→ group-relative ordering
```

离散化可以减少连续噪声被过度放大，却把 proximity function、zone boundary 与权重变成 reward contract。它只在 partial progress 可可靠定义时成立；开放式 research、语义质量和不可逆 tool action 往往没有可信“距离”。错误 proxy 会制造 reward hacking，因此 binary verifier 在 hard pass/fail 风险边界中仍不可替代。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12667:start -->
当 auto-rater 输出 `1..K` 的有序离散等级时，直接在整个等级上做一次 group normalization 很容易让单个离群 judgment 同时改变组均值、方差与全部样本的 advantage。一个更受限的分支把等级分解为 `K-1` 个有序 binary thresholds，对每个阈值独立归一化后再累积更新；一次 rating error 于是只污染部分 threshold，而不是整次 update。

这个 noise-isolation 分支也引入新的 objective state：rating scale、threshold ordering、每阈值 coverage 与 rater revision 都必须进入 run identity。它不消除 judge bias、threshold bias 或 reward hacking；等级顺序不稳定、某些阈值样本退化，或任务只有 hard correctness 时，应回退 binary verifier、重复 judging 或保守 GRPO。exact-v1 的证据限 Qwen2.5-7B/Qwen3-4B、UltraFeedback/RLAIF、8×H100 训练和 4×A100 评测，不支持跨 reward scale 外推作者相对增益。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12667:end -->

### 跨步骤依赖需要保留 Episode Identity

逐 action 打散采样、分别计算 GRPO advantage，在每一步的 reward 近似独立、trajectory 短且 terminal signal 足够密时最简单，也能维持固定 batch 与较高设备利用率。长交互若包含“收集证据→形成 intent→执行最终决策”一类强依赖，前序动作的价值只有通过后续状态才能观察；把 steps 独立 shuffle 会让同一 episode 的协调关系在 update 前消失。

一个条件分支把完整 episode 作为不可拆分的采样单位，先为异构 stage 保留各自的 verifiable step reward，再构造只表达跨 stage 一致性的 episode reward。更新时，每个 action 的局部 group-relative advantage 与有界 episode-level advantage 合并；sampler 按 episode 分组并保留时间顺序，使同一批次能同时看到产生证据的上游动作和消费证据的下游决策。Episode reward owner 只能表达已声明的跨步骤合同，不能覆盖各 stage 的 correctness verifier，也不能把一次最终成功反向解释成所有步骤都正确。

保留 episode identity 会增加变长 batch、长尾 straggler、显存占用和 episode-length weighting；把同一 episode signal 广播到所有步骤还会造成 credit smearing，并提高相关梯度与 reward hacking 风险。因而应分别报告 step correctness、episode outcome、各 stage 消融、长度分布和额外训练成本；跨阶段 reward 不可校准、episode 太长或依赖很弱时，回退 step-wise GRPO、terminal reward，或只在可验证的 phase boundary 分配 credit。Exact-v1 的作者实验仅覆盖 102 个 SmartSpot episodes、Qwen2.5-VL-3B 和单张 H100-80G；它支持 episode-preserving sampling 与跨阶段 credit 在该 GUI 个性化任务中的联合效果，不证明 reward broadcast 已识别逐步因果贡献，也不证明其超越所有长程 Agent objective。

<!-- source-family:SF-2026-ARXIV-2607-25369 -->

若任务允许重复试验，采样单位还可从单个 episode 扩到同一任务的一组 episodes：每次 reset 只重置环境的初始状态，固定 transition/reward contract，并把此前交互保留在下一次 policy 输入中；训练时按这条跨 episode trace 的完成结果比较同任务的候选，而测试时冻结参数，适应发生在 retained context 中，不是在线修改模型权重。这要求 sampler 同时保存 task identity、reset boundary、history-retention 规则与 reward/credit 的归属，不能把不同任务的旧记录当作同一环境的经验，也不能由后续成功认证前次每一步正确。多次试验、变长历史与稀疏跨 episode credit 增加 rollout、上下文和相关样本成本；context 超限、环境在 reset 间变化、行为不可逆或试验预算不足时，应回退单 episode 或只保留可验证的历史。受限文本环境结果支持这种 meta-training 分支，不证明 GRPO 普遍不能使用 dense/process reward，也不证明多次试验在相同总预算下总优于单次执行。<!-- source-family:SF-2026-ARXIV-2602-04089 -->

压缩观察还会改变 policy 的条件输入，因而“是否省略”与“省略后继续生成”是两个不同的概率事件。一个受限分支先在原始 observation view 下决定保留或省略，再让后继生成消费压缩后的 view；若离线只保存压缩 trace，却用它重算此前省略决策的 old/current probability，就已换掉原 sampler 的 conditioning，不能静默称为同一行为策略的 ratio。观察 token 的 loss mask 也只是指定哪些位置参与优化，不等于删去该条件事件。工程上应保存决策前 view、所采 action 与 old log-probability，再分别绑定压缩映射、后继输入及 reward/verifier 身份；这是从接口分责推出的训练审计要求，不宣称原实现已验证完整 guard。[必要方法与反侧](https://arxiv.org/html/2602.04284v1)中的 counterfactual rollout 与正确性筛选还要支付额外生成、解析和验证成本；错误轨迹不给省略收益，不足以证明开放环境没有 reward hacking，论文中参考分布的零概率/优化结论也不能升级为部署最优策略保证。决策 view 不可恢复、压缩丢失必要证据或 verifier 不可靠时，回退保留完整 observation 与独立终局验证，不用短 trace 代替完整概率账。<!-- source-family:SF-2026-ARXIV-2602-04284 -->

## Measurement 也是 Reward Interface 的一部分

“可执行”不等于“无噪声”。代码 correctness test 通常给出离散结果，而 execution time、
energy、latency 或 simulator score 会受到 host load、warmup、sandbox version、timeout 和
长尾抖动影响。若这些观测直接进入 reward，训练目标实际上是：

```text
policy output
→ evaluation environment
→ noisy measurement
→ reward transformation
→ group-relative advantage
```

因此 environment identity、measurement repeatability 与 reward mapping 都属于训练
specification。一个真实差异若小于观测噪声，会随机翻转组内排序；reward 太稀疏或饱和，
又会制造大量 zero-advantage groups。增加连续小数位不一定提供更多有效信号，反而可能把
measurement noise 放大到 gradient。

在带性能目标的 RL 中，更可靠的工程顺序是：

1. 先用 correctness gate 排除无效输出。
2. 通过较大、可区分的 workloads 与重复测量校准 environment。
3. 在同 prompt、相近时间窗口比较 candidates，降低跨任务难度与 service drift。
4. 检查 reward density、monotonicity、saturation 与 all-equal group ratio。
5. 用廉价 replay/simulator 筛掉明显退化的 environment/reward 配置，再启动昂贵 rollout。
6. 训练与 Evaluation 记录 sandbox、hardware、load、timeout、aggregation 和 calibration
   version，避免把 drift 当成 policy improvement。

《Reinforcement Learning for Code Optimization》在 code timing 场景中系统化展示了这条
路径，并报告 naive timing reward 会被 noise、sparsity 与 GRPO instability 淹没。其具体
数据集、reward recipe 与收益仍是单篇预印本的实验结论；本章吸收的长期原则是：
**verifiable reward 的测量系统也是被优化接口，必须与 policy 一起设计和审计。**

### 长上下文 RL 还要验证 Context 是否真正被使用

终局答案可验证时，只给 correctness reward 最简单，也能避免把不可靠的过程 judge 写进 objective；但在长上下文任务中，
模型可能凭参数记忆、题目先验或局部线索得到正确答案，而没有学习检索和使用提供的 evidence。此时 correctness 仍为真，
训练目标却无法区分“基于当前 context 求解”与“绕过 context 猜中”。

更严格的分支把 reward 拆成两个职责不同的 signal：答案项继续衡量 outcome correctness，context 项则用
chunk-label 调制的 F-score 衡量回答与给定上下文的对齐。论文把二者相加为 `r_total = r_ans + r_ctx`，因此它不是
“两个 hard gate 均通过才接纳”的布尔合同，而是让两类证据共同影响 trajectory 的相对权重：

```text
answer-quality reward + context-alignment reward
-> total reward
-> group-relative comparison and update
```

这能惩罚明显绕开 context 的 shortcut，并把 retrieval/read state 纳入训练合同；代价是额外标注、evidence provenance
与 reward specification gaming。尤其要注意，chunk-label F-score 只能证明输出与标注片段更一致，不能证明模型在因果上
使用了这些证据；开放研究和多跳解释仍可能把“复述了证据”误当成“证据支持结论”。短任务、闭卷能力训练或 context
本就不是 authority 时，单一 outcome reward 仍更合适。作者实验只支持其长上下文任务、模型和 reward construction，
不证明开放域 grounding 已被解决。

<!-- source-family:SF-2026-ARXIV-2603-02146 -->

### Reasoning Cost 也是版本化的 Reward Prior

硬 token cap 与线性长度惩罚便宜、可解释，并直接对应 decode 数量；在硬 SLO 或每个 token 成本近似一致时仍是必要边界。
训练期还可以改变**预算由谁竞争**，而非直接给每个 token 加税：把多道可验证题放进同一次 completion，分享一个硬 cap，reward 以各题正确性为主，另含格式奖励而不含长度惩罚。前题占用过多 token 会挤掉后题的可用空间，于是 policy 必须学习在题目间分配推理深度；部署时仍可单题使用。这和单题长度惩罚的梯度不同，但会引入题序、难度配比、答案边界解析和截断后题的偏差。预算太紧会丢失必要推理，题目不能共用可比较 verifier、或产品必须分别治理每次请求的 SLO 时，单题硬 cap/显式代价仍是清楚的旧方案。[受限数学推理实验](https://arxiv.org/html/2604.02322v1)只支持作者 1.5B/4B 模型及其训练设置；两组长度惩罚对照发生坍缩，不证明任何软惩罚都必然失败，也不证明跨域或生产吞吐获益。<!-- source-family:SF-2026-ARXIV-2604-02322 -->

显式预算还可把“本条超支的惩罚”与“下一轮预算压力”分开：primal reward 只扣归一化超额长度 `(L−B)+/B`，使预算内长短不再承受同一 token 税；dual multiplier 则按批次平均 `mean(L)/B−1` 的有符号偏差更新，并限制在有限区间。前者改变单条 response 的排序，后者调整跨批次的平均预算压力；平均满足预算不等于每条请求或尾延迟满足硬 cap，外层 token/deadline fallback 仍须保留。这个分支增加 multiplier、预算及其更新节律，且 cap 可让最长正确样本的 reward 恰为零、与短错误样本并列，不能宣称任何正确回答都严格优先。精确期望/最优响应等理想化前提也不能替有限 GRPO 更新签发收敛保证；所测 1.5B 数学配置中 token 降幅伴随约 2pp 质量代价，训练 step/能量测量不是线上 SLO。预算或质量失配时，保留硬 cap、原线性 cost 或重新校准 dual，而不把平均控制当成逐请求认证。<!-- source-family:SF-2026-ARXIV-2602-14468 -->

若继续采用显式代价，统一的 token 税又无法区分必要的罕见步骤与重复 filler。若 prompt 在生成答案时始终可见，reasoning trace 应付出的不是重复
编码 prompt 的代价，而是相对某个 trace prior 的额外信息成本。于是 reward 可以从：

```text
correctness - beta * token_count
```

演进为：

```text
correctness + beta * log Q_prior(reasoning_trace)
```

Uniform prior 可恢复线性长度惩罚；换一个 prior，就是换一套“哪些 trace 昂贵”的训练 specification。Prior checkpoint、
tokenizer、template、`beta` 与 verifier 必须进入 experiment identity，且 prior surprisal 不能被叫作 semantic necessity：必要但
低频的 notation、domain term 或策略转换也可能被错误加税。Reasoning as Compression 在作者数学模型与训练 contract 中改善了
accuracy-token frontier，但没有证明 token 减少会稳定转化为线上 latency、energy 或 capacity，也没有证明压缩后的自然语言
CoT 更 faithful。Hard cap 继续拥有外层安全边界，uniform penalty 仍是廉价 proxy；prior-dependent cost 只在 bias、额外 forward、
版本漂移与 rollback 可被审计时增加价值。

### 降低推理输出成本，也可以改变中间动作空间

上述预算方法仍在自然语言 reasoning trace 中调整“写多少”；自然语言步骤可读、可局部检查，但每一步也消耗解码 token，长度惩罚又可能删掉必要推理。另一条实验性分支在 tokenizer 中保留一组离散抽象码与起止标记，让 policy 先在受约束码表内生成短中间序列，再生成普通答案。此时优化对象不只是长度，而是 `prompt → 抽象码状态 → 答案` 的联合动作空间：码表、最大长度与约束解码器进入训练和推理身份，reference policy 则作为训练时 KL 约束的版本化状态。随机初始化的新码没有既定语义，直接从冷启动做 RL 容易失效；可先让带 verbal CoT 的监督经过注意力瓶颈塑造抽象码，再用不带 verbal CoT 的自身采样做蒸馏，最后对抽象码和答案联合做受约束的组相对更新。<!-- source-family:SF-2026-ARXIV-2604-22709 -->

这用额外 warm-up、专用 token、解码约束和更难审计的中间状态换较短的可见输出；码序列不是可解释或忠实的思维步骤，也不因 token 更少就已证明训练加推理的总成本、服务时延和安全性更优。Abstract-CoT 的受限 Qwen3 4B/8B 与 Granite 3B 实验支持该条件分支：冷启动 RL-only 弱于 warm-up，某些任务以较少输出 token 接近或超过 verbal-CoT 基线，但 Qwen3-8B 的 MATH-500 准确率仍低于 verbal SFT+RL。需要可审过程、预算不足以训练码表，或普通 hard cap/可读 CoT 已满足目标时，继续保留自然语言与现有长度控制，而不把抽象码写成 GRPO 的必然下一代。<!-- source-family:SF-2026-ARXIV-2604-22709 -->

## 从 DeepSeekMath 到 R1：Pure RL 与 Multi-stage Training 为什么同时成立

DeepSeekMath 提出 GRPO，动机之一是避免 PPO critic 带来的额外 memory，并将其用于数学
reasoning。DeepSeek-R1 的价值不只是把同一算法放大，而是公开了两条必须同时保留的路线。

第一条是 R1-Zero：从 base checkpoint 出发，不先做 reasoning SFT，针对数学、代码和逻辑题
采样成组 responses，以 answer correctness 与 format rule 提供 reward。论文观察到 response
长度、反思、回溯和策略切换随 RL 训练出现。这支持一个受限结论：**当任务足够困难、结果
可可靠验证且 rollout compute 足够时，outcome-level incentive 可以从 pretrained model 中
激发新的搜索行为。**它不证明自然语言 CoT 等同于真实内部推理，也不证明该路线适用于不可
验证的开放领域。

第二条是完整 R1 pipeline。R1-Zero 同时暴露出 readability、language mixing 与通用写作/
开放问答能力不足，因此后续流程不是继续用 pure RL 覆盖一切，而是：

```text
base checkpoint
→ 少量 cold-start reasoning traces
→ reasoning-focused RL
→ rejection sampling + reasoning/general SFT
→ second RL for reasoning + helpfulness + safety
```

这是一条 `Direct Evolution`，但不是“RL 取代 SFT”。Cold start 约束可读格式和语言，第一轮
RL 扩展可验证任务上的搜索，rejection sampling 把较好的 policy experience 转回训练数据，
general SFT 补回非 reasoning 能力，第二轮 RL 再处理偏好与安全。每一阶段解决上一阶段暴露
的边界，也引入新的 data selection、reward-model bias、policy lag 与成本。

Distillation 还形成第三个分支：把大模型生成的 reasoning traces 用于较小模型 SFT，可以转移
行为而不复刻原始 RL 系统；代价是学生受到 teacher 覆盖和轨迹质量上限约束。它与直接在小
模型上做大规模 RL 不是同一个实验命题。

从这些工作能稳定得到的结论是：在可采样多个候选、reward 可比较或验证的任务上，
group-relative policy optimization 是一条有效工程路径；而 production reasoning model 往往
需要在 exploration、readability、general ability 与 safety 之间使用多阶段训练，而不是把某一
阶段绝对化。

不能直接推出：

- GRPO 对所有领域都优于 PPO/DPO。
- RL 自动产生可靠、可解释或忠实的 reasoning。
- R1-Zero 的结果证明 cold-start/SFT 已不再需要。
- 任何带 group normalization 的实现都等价于原始 GRPO。
- Benchmark gain 自动转化为生产可靠性。

Cold-start scaffold 也可以在 rollout context 中逐阶段退火，而不一定先写入参数。示例轨迹在早期让 policy
更容易命中合法 tool call，后续从多示例降到零示例，试图把行为从 prompt scaffold 内化到 policy：

```text
demonstration-rich rollout
-> fewer demonstrations
-> zero-demonstration rollout
-> held-out tool and outcome verification
```

这条分支用 inference tokens、tool calls 和精选 demonstrations 换较少的标注训练，却仍需要可比较 reward、
tool-result provenance 与格式/answer verifier。退火步数不是越细越好；过早移除 scaffold 会让探索重新变稀疏，
tool-return tokens 若被当作 policy action 训练又会混淆 credit。ICRL 的作者实验只在特定 QA、搜索与代码工具
contract 中支持这种 curriculum，不证明 SFT 不再需要。安全动作、稀疏 reward、工具昂贵或 demonstration
本身承载 policy constraint 时，参数化 SFT cold start 仍更可靠；两者是可组合分支。

### Scaffold 可以退火，但不能假装从未存在

External Skill、hint 或 procedure 可在早期 rollout 提供结构，再依据 held-out utility 过滤、排序并逐步降低注入，

Teacher 也可以只在失败 suffix 注入局部 correction，然后立刻把生成权交回 learner。这样比完整接管更接近 learner 分布，却仍生成了带 intervention provenance 的 trajectory：必须记录干预 span、teacher/judge revision 与恢复控制的位置，不能把它伪装成纯 on-policy rollout。中等干预可能兼顾探索与纠错；teacher 不可靠、成本过高或 contamination 难追踪时，纯 learner rollout 仍更可审计。

<!-- source-family:SF-2026-ARXIV-2609-12419 -->

Diffusion LM 的 scaffold 还可表现为 teacher-filled mutable canvas，再逐步提高 mask 并保留一部分 pure-noise inputs，最终在 inference 去掉 teacher。Pure-noise floor 防止 learner 只依赖 teacher state，却会增加训练成本且不同任务收益不一致；teacher canvas 是 curriculum state，不是真值或永久 context，退火失败时应回退普通 noise initialization 或 outcome-only RL。

<!-- source-family:SF-2026-ARXIV-2609-13060 -->
最终训练一个不依赖 runtime Skill 的 policy。这样做改变的是 curriculum/control state，而不是证明模型“内化”了
可验证程序：Skill revision、selection score、injection schedule、policy checkpoint 与 no-skill evaluation 必须
联合版本化。稳定 runtime Skill 在频繁更新、审计、tenant policy 或模型容量不足时仍然成立。

SKILL0 的作者结果支持 scaffold annealing 的一种实现；helpfulness estimate、coupled reward、visual rendering 与
repository drift 使因果归因仍为 Experimental。

论文当前 revision 相比 2025 年 v1 补充了更完整的 recipe、限制和系统细节；引用具体
hyperparameters 或 benchmark 时必须锁定 revision。本文只沉淀跨版本仍成立的阶段职责和
trade-off，不把作者 recipe 泛化为 GRPO 的统一定义。

### Derived Skill 的 Utility 必须由当前 Policy 反事实验证

从历史成功或失败 trajectory 总结 reusable skill，再把它静态注入后续 rollout，是一种合理的 cold-start scaffold；问题是 policy 更新后，旧 skill 可能不再对应当前可达状态，analyzer 也可能生成听起来合理却没有行为增益的规则。

更严格的分支让最新 policy 先产生 on-policy trajectory，再由外部 analyzer 提出 skill candidate；对同一 state/action context，分别计算有 skill 与无 skill 时当前 policy 的 token probability，只有相对 delta 与 group outcome 一致的部分才进入 update。这样 skill 不拥有 reward authority，而是一个 policy-synchronous derived signal：environment outcome/verifier 决定成功，matched with/without comparison 衡量局部 utility，group-relative objective 决定更新幅度。

Analyzer 额外增加推理成本、同源偏差和 prompt dependence；probability delta 仍是 relevance proxy，不证明因果，失败 trajectory 总结的规则还可能放大错误归因。静态 curated skill 在 policy 变化慢、审计或 tenant policy 要求稳定时继续成立。作者实验绑定 Qwen/GLM analyzer、给定文本/视觉 agent environments 与 8×A800 训练，不是普遍的 skill learning recipe。

### Privileged Trajectory 必须先匹配 Student State

直接把成功 reference trajectory 的第 `t` 步蒸馏给 student，隐含了 student 已处于相同 environment state。
长 Agent trajectory 中，这一假设经常不成立：student 的历史 action 已改变 inventory、page、tool result 或
available actions。更安全的分支是先抽取 structured state signature，只在找到兼容 reference state 时使用
contextual teacher；无法匹配时退回 on-policy outcome RL。

```text
student on-policy history + environment snapshot
→ state signature and matcher
→ compatible reference turn ? contextual distillation : GRPO fallback
→ terminal verifier remains correctness owner
```

Matcher 不是新的 truth source。它可能学习 environment shortcut、泄漏 privileged reference 或把不同业务状态误判
等价；state schema、reference set、matcher revision 与 fallback rate 都要进入训练身份。SMRC-SD 的 ALFWorld/
WebShop 实验只支持这一分支在两个文本环境中的可行性，不证明 browser、robot 或不可逆 workflow 可安全抽象。
普通 on-policy rollout 在状态难形式化时更可靠，固定 demonstration 在初始状态可复算时仍更简单。

还可以先把外部专家 trace 压成 plan，再让 base policy 在真实环境中沿 plan 自行重走，只接纳 verifier 判成功的轨迹；随后用该任务的新 policy 成功轨迹刷新 cache，仅在当前整组 rollout 全失败时替换一条失败轨迹。它用较窄的成功支持集缓解稀疏反馈，却不是把外部专家直接改名为 on-policy。尤其 self-roll 的条件是 `instruction + plan`，后续混入训练时却去掉 plan prefix；action 由同一模型产生，也不能抹去这个 conditioning change。Cache 必须保存 plan、产生策略、环境/成功判据、刷新与选取身份，当前整组失败只触发候选复用，不认证其采样概率。<!-- source-family:SF-2026-ARXIV-2601-05787 -->

这一分支额外支付专家执行、plan 抽取、环境重放与 cache 维护成本，并偏向专家或 base 已能成功的任务。所测 GUI RLVR 的较高旧策略 likelihood、概率直方图接近和有限任务上的成功刷新，只是分布诊断；使用 current/old-policy ratio 并不自动成为该 cache 行为分布的严格 importance correction，也不保证成功示例必产生足够、无偏的梯度。条件历史无法复原、cache 陈旧或成功判据失配时，应隔离该轨迹，回到 fresh rollout、明确的离线监督或原来的 state-matched reference 分支。

### Prompt Robustness 不能只靠更多 Template

多模态 RLVR 常在少量 prompt templates 上训练，policy 可能把 evaluator wording 或 output format 当成 reward shortcut。
一种分支把 prompt mutation 变成训练分布，并分别处理正确、错误与不可判定结果，再以原任务 outcome 作为 hard gate：

```text
task / media identity
→ bounded prompt mutation family
→ trinary outcome and robustness reward
→ group-relative update
→ held-out template and free-form evaluation
```

这获得对已知 paraphrase family 的鲁棒性，却可能让 mutation 改变任务本身，或把 template generator bias 写入 policy。
PIRL 的有限模型、三 seed 与 benchmark 结果只支持其 contract 下的 gap 缩小；free-form 后各方法明显下降，说明
prompt robustness 尚未解决。固定 canonical template 在 API contract 明确时仍合理；开放交互必须保留 held-out
human phrasing、semantic-equivalence audit 与 no-mutation baseline。

## Rollout 进入 Update 之前：Artifact 与监督语义

基础同步实现只需要按 prompt 形成 group、完成 reward、计算 old/current/reference log-probability，再提交更新。随着探索精度、teacher、optimizer 或 environment 参与，trajectory 不再只是文本，而是带 lineage 的 objective artifact。本节先处理“哪些样本有资格进入 update”；下一节再处理它们怎样由独立服务产生并保持 freshness。

### OPD 是探索催化剂，不是能力上限扩展器

离线蒸馏或朴素 On-Policy Distillation 在 Teacher 与 Student 能到达相近状态、回答长度分布稳定时仍然合理：Teacher 给出的 token 分布可以直接成为低方差监督，不必先把整个环境改造成 RL 问题。约束改变发生在 Student 的 on-policy rollout 进入 Teacher 训练分布之外之后。此时更大的 Teacher 不必然提供更有用的梯度；Teacher/Student 分布错配会放大不可靠 token，而按 sequence 聚合的长度效应还可能让长轨迹在更新中获得不成比例的权重。

因此，OPD 的状态所有权应留在 Student：先由 Student 产生自己真实可达的 rollout，再查询 Teacher 的 token-level guidance，对过大的分布差异做 clipping 或 log-compression，并由 outcome verifier 决定该轨迹能否进入更新。Prompt coverage、Teacher 版本、压缩阈值与 objective 必须共同版本化。这个机制改善的是可达状态上的探索与监督质量，不会凭空扩大 Student 的表示容量或能力上限。

代价是多一次 Teacher 推理、额外的阈值与 verifier 依赖；过强压缩还会抹掉少数但有价值的纠偏信号。稳定、覆盖充分的任务仍适合离线蒸馏；需要环境交互发现新状态时，RL 仍承担不可替代的探索职责。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12652:start -->
朴素 OPD 把每条 student rollout 独立交给 Teacher，在轨迹之间近似独立、单条反馈已经足够时最简单。稀疏成功任务里，同一 prompt 的多条 on-policy attempts 已形成一个局部 trial-and-error state：成功 peer 提供可行路径，失败 peer 提供结构化负证据。可以冻结 group membership、policy revision 与 verifier result，把两类 peer evidence 共同放入 teacher context，再为当前 trajectory 生成 token-level supervision proposal；Teacher 仍不拥有 reward 或 admission authority。

这种 peer-conditioned guidance 用更多 rollout、额外 teacher context/query 换 instance-adaptive 监督，也会放大同组错误相关、verifier label contamination 和上下文成本。没有可靠 outcome、开放任务无法验证或预算不足时，应回退独立 OPD、离线蒸馏或普通 outcome RL。exact-v1 只支持 Qwen3-4B/8B、每题 8 rollouts 与作者披露的 verl/异步 vLLM/FSDP/BF16 任务，不证明任意 Teacher、开放任务或生产 SLO 下成立。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-12652:end -->

Teacher guidance 也可进入 advantage-signed ratio，而不作为独立 token KL：[一个局部分支](https://arxiv.org/html/2602.22495v1)用 `r=(pi_student/pi_old)^α·(pi_student/pi_teacher)^(1−α)` 替换 PPO surrogate 中的 ratio，再与 signed advantage 进入 min/clip，原 reference KL 保留；它改变正负 advantage 的更新压力，近零 advantage 则几乎不带 teacher 信号。公式的 `α=1` 回到 old-policy ratio、`α=0` 为 teacher ratio，原文字端点相反，采用公式而隔离错误叙述；未归一化的几何 anchor 也不是 proper mixture policy。surrogate clipping 不强制真实 ratio 保持硬界，原 log-bound/KL 等价推导不能据此签发 global trust-region 或 DPO 保证。Qwen3 小模型蒸馏的作者实验支持局部启发式，部分指标仍有 KDRL 更好，AIME24 同时参与 checkpoint selection 与评价；teacher query、log-probability 和 clipping 均增加训练费用，省去部署 teacher 不等输出长度或延迟相同。数学保证或净收益未成立时保留独立 KDRL/OPD、普通 GRPO 及原 verifier，不把这一 loss 分支升级为通用收敛定理。<!-- source-family:SF-2026-ARXIV-2602-22495 -->

### Low-fidelity Exploration 不能直接成为 High-fidelity Objective Artifact

当大量候选最终都会被丢弃时，探索阶段可以用低精度/低 fidelity policy 扩大 seed search；但进入 gradient 的
trajectory/target 必须由 objective-compatible policy、precision 和 solver 重建，并保存 seed、ranker、precision、
policy revision 与 regeneration evidence：

```text
low-fidelity candidate exploration
→ rank / retain extreme or informative seeds
→ high-fidelity deterministic regeneration
→ verified training target
→ policy update
```

这减少的是 rejected-candidate generation cost，不证明低精度 trajectory 本身适合训练。Rank order 若随精度变化，
探索会系统性丢弃真正高价值 seed；重建也可能失败。FP4 Explore/BF16 Train 是 diffusion RL 的 Experimental
case，不能外推所有 autoregressive rollout。

低成本代理还可以不直接输出 trajectory，而只输出相对于自身 anchor 的 **policy-update artifact**，再由主模型
用匹配 anchor 校准这份相对变化。它比复制代理的绝对分布更接近“转移 post-training delta”，但主模型必须保留
接纳权：model family、tokenizer、support、anchor 和 domain 任一不匹配，都可能把代理偏差放大成更新方向。
因此 proxy update 只能先作为 proposal，经主模型 likelihood、任务 verifier 与 high-fidelity canary 验收后进入
objective；没有匹配 anchor 或可验证 outcome 时，重新生成 high-fidelity trajectory 仍是更清晰的基线。

结构化 pruning 之后也不能默认沿用原 policy 的离线 distillation 分布。剪枝改变了 student 可达状态与失败模式；
只在 teacher/offline trajectories 上恢复容易覆盖旧的成功路径，却看不到 pruned policy 自己会进入的错误状态。
一个受限恢复分支先从当前 pruned policy 生成 on-policy rollouts，再按 failure type 和 horizon 控制 curriculum，
最后由 verifier 决定哪些 trajectory 可进入 update。它用更多在线生成与非平稳数据换取 state coverage；稳定、
已覆盖的分布仍适合便宜的 KD。Pruning revision、rollout policy、failure taxonomy、horizon 与 verifier 必须共同
进入 artifact identity，不能把短期恢复分数写成原能力已完整重建。

### 固定 Offline Support 不能被无限次重复消费

### Weighted SFT 何时能替代 KL-Regularized RLVR

当 reference policy 固定、reward 可在其 support 上计算且优化目标确实是 KL-regularized expected reward 时，可以把目标投影成从 reference 采样的加权 SFT；这把 rollout/update 回路换成一次离线监督，降低系统复杂度。等价边界由 reference support、importance weight 和有效样本量共同决定：目标策略需要的区域不在数据中，或权重集中到极少样本时，one-shot projection 无法复制 on-policy 探索。

因此 weighted SFT 只拥有已覆盖 support 内的低成本替代权，不能把一次加权拟合宣称为通用 RL。ESS 过低、reward 随策略变化或环境反馈会改变状态分布时，应回退 on-policy rollout、迭代数据刷新或更保守的 KL 约束。现有 exact-v1 理论与实验只支持其固定 reference 和披露任务。<!-- semantic-body-binding:SF-2026-ARXIV-2605-02469 -->

标准 reverse-KL 蒸馏也可改为一种保持目标分布、改变拟合几何的条件分支。给每个固定 response 赋正权 f，分别把 teacher/student 的 `exp(f·logπ)` 归一化成诱导分布 P；在分区函数存在且同 support 的前提下，`P_student=P_teacher` 仍唯一指向 `π_student=π_teacher`。组内中心化 `f·log(π_student/π_teacher)` 后作平方损失，会消去 prompt 级未知 partition ratio；它不要求 token 逐位置对齐，但必须声明共同 response 对象、各自 scoring 及采样 support。

无 importance ratio 指采用了这项不同损失，不是离线样本无偏估计原 policy gradient；全 support 下的 global zero-loss 目标也不证明有限参数/样本、截断 decoder 或 Adam 实际收敛。长度权 `f=|y|^(−alpha)` 在一个 student/两个 teacher 数学实验中改变结果，最佳 alpha 随 teacher 变化而非单调。它增加 teacher sequence scoring、组统计和权重调参成本；support 不足、loss/能力漂移或 teacher 不是可信目标时，保留标准 OPD/offline KD、刷新 rollout 或外部 verifier，而非由理论最优点宣称训练稳定。 [必要机制与反证](https://arxiv.org/html/2609.21432v1)。<!-- source-family:SF-2026-ARXIV-2609-21432 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11956:start -->
离线偏好对便宜、可重放，也不依赖在线 environment；当更新幅度小、数据 support 仍覆盖当前 policy 时，多轮消费同一批数据可以提高样本效率。但 policy-gradient 会同时改变正负样本相对当前策略的 likelihood：epoch 或 learning rate 继续增加后，policy 可能已经离开这批固定样本能够约束的区域，即使组内 advantage 方差仍稳定，importance ratio、sequence log-prob variance 与正负 likelihood drift 也可能持续放大，最终表现为能力 collapse。

因此训练控制面不能只用 reward 或单一 loss 决定继续更新；同一个 gate 应共同约束 `epoch / learning rate / importance ratio or log-prob variance / positive-negative likelihood drift`，并绑定 dataset、sampling、base/policy revision 与 evaluator identity。它们是 support drift 的诊断信号，不是充分的提前预警器；任一指标越界时，应停止或回滚 checkpoint，再根据约束选择更保守的离线更新、稳定的 distillation，或补充由当前 policy 产生并经 verifier 验收的在线 rollout。前两者保留可复现性与低环境成本，后者换取新状态覆盖，却新增执行成本、非平稳性和 verifier 风险。

exact-v1 证据只覆盖固定 CodeNet 正负提交对上的离线更新、Qwen / DeepSeek / CodeLlama 模型族，以及 MBPP / APPS 评测。它支持“同一 recipe 的稳定性依赖模型与更新轨迹”，但不证明上述指标能充分预测 collapse，不证明 negative sampling、clipping 或在线数据可以通用修复，也不能外推到自然语言、工具轨迹或其他 reward contract。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11956:end -->

### Outcome-routed Update 先分支，再做 Group Calibration

Uniform online policy distillation 会让 teacher 对已正确样本继续提供高熵噪声，也无法区分“保持正确”和“修复
错误”。一种分支先由 outcome verifier 区分 correct/incorrect：正确样本约束 student 自身分布，错误样本再
吸收 teacher signal，最后在 group 内校准 sample weight。它新增 verifier error、branch imbalance、teacher bias
与 group-composition dependency；稳定 offline distillation 或可靠 demonstrations 仍是低复杂度方案。
SCOPE 提供受限机制证据，不构成跨任务最优 OPD recipe。

thinking-enabled reasoning 中，on-policy self-distillation 不应默认承担错误纠正；对 correct/incorrect rollout 分组后，证据更支持把 OPSD 放在 SFT→RLVR 之后作为压缩已学会轨迹的条件阶段。Admission owner 只允许已验证正确的 rollout 进入 compaction，错误轨迹回到 RLVR/teacher correction；否则 hindsight supervision 会把错误路径压进参数。代价是额外分流/verifier 成本，短输出或可靠 teacher 能提供局部纠正时原 OPSD 路径仍可成立。

证据限于 thinking-enabled 数学推理和作者 correct/incorrect split；不证明 OPSD 对所有模型、任务或短 thinking-disabled 输出只能做压缩。 TRAIN-SFT 解释 distillation objective；TRAIN-GRPO 拥有 post-RL pipeline position 与 rollout admission。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06188 -->

### Selective Distillation 还要区分“需要纠正”与“与任务有关”

Teacher/student disagreement、entropy 或低概率能指出某个 token **难学或尚未学会**，却不能证明这份监督由
当前任务条件决定。若只按 optimization need 选择，有限 token budget 可能花在风格、通用语法或 prompt 表面
变化上。一个实验性分支固定 student on-policy rollout，并为同一 source prompt 构造 meaning-preserving
paraphrase 与 task-changing counterfactual，比较两个干预对每个 token distribution 的影响：

```text
student-owned rollout on original prompt
→ score the fixed tokens under original / paraphrase / counterfactual
→ task-changing sensitivity - surface sensitivity
→ select a bounded token subset
→ teacher supervision only on selected positions
```

这是一种 **task-relevance proxy**，不是 causal credit。Counterfactual 可能同时改变 difficulty，paraphrase 可能
并不严格等价，top-k-with-residual divergence 也只是 full-vocabulary distribution 的近似；生成、验证三元组还会
把额外模型与数据成本移到训练前。它与 outcome routing 是不同层：outcome verifier 先决定该 trajectory 是否需要
teacher correction，selector 再决定有限监督预算落在哪些 token。稳定 demonstration、full-token OPD 或简单
disagreement mask 在任务同质、预算充足、contrast 难可靠构造时继续成立。

CROP 在两个 Qwen teacher/student 组合、数学训练 prompt、固定 10% nominal token budget 下提供受限实验，不能
证明 counterfactual selector 可跨 domain、model family 或长 Agent trajectory 泛化。应同时报告 triplet validation
通过率、构造成本、selected-token coverage、teacher calls、下游 outcome 与 no-selection baseline，而不是只保留
六个 benchmark 的 aggregate headline。

Selective distillation 还可能遇到另一类冲突：teacher 在局部 token distribution 上更强，却把 student 当前已经形成
的正确 reasoning progress 拉回到另一条风格或路径。仅按 teacher/student disagreement 选段会把这种分歧误当成
“需要纠正”。一个实验性分支可在 segment boundary 估计 continuation solve probability，以增量 process reward
表示该段是否推动终局，再只在 teacher direction 与 progress direction 一致的 segment 上蒸馏：

```text
student on-policy response
→ segment boundaries + repeated continuation rollouts
→ estimate incremental solve-probability change
→ rank within-response teacher/progress conflicts
→ mask a bounded conflict fraction
→ reverse-KL distillation on retained segments
```

它以额外 rollout 和 verifier cost 换取“不要为了模仿 teacher 破坏已有进展”的保护，但 solve-probability estimator
本身方差大，segment 划分、rollout 数、mask fraction 与 verifier bias 都进入 objective identity。数学可验证任务上
的受限增益不证明开放式 Agent trajectory 也有可靠 process signal；当 continuation cost 太高、verifier 不可信或
teacher 就是目标分布时，full-response OPD 与 offline distillation 仍更简单。

### Advice 的预测敏感性可以选择监督，但不证明执行因果

在advisor训练中，teacher correction还可能改善“怎样说建议”，却没有改变冻结外部executor的行为。可以先让reflection提出待修正决策，再由更新前advisor对**同一条已记录executor response**分别在有/无已发advice的context下评分，用平均log-likelihood差的绝对值选择整条advice决策。该contrast不需要executor logits或额外executor rollout，却只是advisor的预测敏感性proxy，不是executor行为的因果反事实。Original abstention的两context相同，contrast恒零，必须另保留其被reflection发现的漏建议机会。

一个受限实现用从其他任务移入、但不真正发送的donor advice校准固定阈值，再对选中决策加feedback-conditioned self-distillation；原GRPO仍使用每个episode原来的advantage，不按选择器重写reward。AdviSD的[§4–7及AppendixE](https://arxiv.org/html/2609.38142v1)中matched-count random对照支持选择内容的作用，但数量只在各自rollout的episode内匹配，不是同一批决策的成对干预；shared-parameter分析假设fixed/stationary teachers，不证明changing-teacher GRPO–AdamW收敛。跨executor迁移及某些多步任务仍弱于专门训练或纯GRPO。它新增reflection、双路评分、阈值校准与API版本成本；预测不稳、advice无可靠作用或外部executor更换时，应重新校准或回退纯outcome RL、已验证advice和不监督，而不是因teacher更像正确文本就认为执行改善。<!-- source-family:SF-2026-ARXIV-2609-38142 -->

### Teacher 的绝对分布与 Post-training Delta 是两种监督对象

普通 OPD 在 student rollout 上逼近强 teacher，适合“teacher behavior 本身就是目标”的场景；若 teacher 是
同一 base 经 reasoning RL 得到，绝对分布还混合了 base 的语言/style prior。可以引入 matched teacher-base，
把每个 token 的监督拆成 `log π_teacher - log π_teacher-base`，再用普通 teacher/student direction 作为 sign Gate：

```text
student-owned on-policy prefix
→ teacher / matched-base token log-ratio delta
→ centered magnitude under a declared vocabulary support
+ teacher/student direction gate
→ clipped policy update
```

它试图转移 post-training change，而不是宣称 delta 等同“reasoning knowledge”。Matched lineage、tokenizer/template、
top-k support 与三份 checkpoint 都进入 objective identity；base 不匹配会把 architecture/style 差异误当能力增量，
sign Gate 也可能丢弃有效反向信号。绝对 OPD 在没有 matched base 时更简单，outcome RL 在需要 environment
exploration 时仍是独立分支。OPD² 的作者实验只支持其 Qwen/Gemma、短程训练与指定 benchmark 合同。

但 matched-base 的 log-ratio 仍只量相对变化：当 teacher 与 base 给 student 候选 token 的绝对概率质量都趋近零时，log-ratio 和由它产生的局部更新可以不变，两个分布的 JSD/KL 与可观察行为差异却趋近零。逐 token 全量蒸馏因此会把“几乎没有行为意义的方向”也当密集奖励。一个有条件的修正是在 student 实际到访的 prefix 上计算 teacher–base divergence，只给高差异状态监督；这需要额外记录选择阈值、候选 support 和被屏蔽比例，也可能丢掉小而重要的变化。Direct-OPD 在教师行为差异普遍显著、数据稀少时仍是合理基线；选择性分支只在作者两组 teacher pair、四种 1.7B–8B student 和数学任务的八种设置中胜出七种、持平一种，不能推为跨领域最优。<!-- source-family:SF-2026-ARXIV-2609-29142 -->

比较 teacher 的绝对分布与 base 变化之外，还可比较同一冻结模型在正确和错误 privileged contexts 下的分布。固定 student 自己生成的 prefix，由两个 self-teachers 重评分同一 token，对正确上下文做 attraction、对错误上下文做 repulsion；在 balanced reverse-KL 的解释公式中，共同 student 项严格抵消，留下半个 log(p_correct/p_incorrect)。这只是一条条件监督方向，不是 token correctness verifier：两 context 共同携带的风格偏移能抵消多少，取决于它们实际共享多少偏好，不能从代数消项推出纯正确性 credit。它与前述 verifier 决定 outcome sign、teacher 仅调节幅度的 RL 分支不同，不应暗中替换后者的 authority。

两路评分、correct/incorrect context 采集和有界长度都增加成本并限制训练人口。作者只在 group 同时提供两种上下文时蒸馏错误 rollout，teacher 始终冻结、没有辅助 GRPO；实际训练使用 sampled-token generalized JSD，因此 reverse-KL 的精确 log-ratio 恒等式不能直接当全部实验 loss。Qwen3-4B 数学与 Anagrams 的受限结果中，单边 repulsion 可激活原有 thinking 却未超过初始 thinking 基线，随后长度增长与截断导致崩溃；已 thinking 的 Anagrams 上 attraction 本身也可改善，去掉 thinking context 会改变长度。token credit 池化/打乱又削弱训练收益，不能把效果缩成单一模式切换或长度因果。评估 mean@4 不是 pass@4，跨训练 seed 不确定性与硬件/精度未披露，不构成普遍稳定性证明。Context 不可信、两侧缺失或成本不合算时保留已验证单教师、outcome RL 或不更新；最终正确性仍由外部 checker 和 holdout 判定。 [必要机制与反证](https://arxiv.org/html/2609.21561v1)。<!-- source-family:SF-2026-ARXIV-2609-21561 -->

对照两种 teacher contexts 可以消去共同 student 项，却还没有回答 baseline teacher–student 差异中有多少只是 teacher 对提示的正常漂移。一条受限分支固定 student 实际 rollout 与每个 prefix，由同一冻结 teacher 分别读无额外上下文及正/负干预；按该 token 的 log-prob 上下变化，围绕 baseline teacher 构造放宽的区间。student log-prob 在区间内时不给更新，区间外只保留到最近端点的有符号超额，而不是把整个 teacher–student 差值都当能力 credit。干预只用来估计参照变化，不直接作为 student 的 privileged 输入；这与先前双 teacher 对比、任务/改写 counterfactual 与 divergence 选点是共存的过滤分支。

这个区间来自有限 prompts，不是统计覆盖保证、token correctness verifier 或知识/风格的可识别分解；放宽系数和 probe 内容会过滤有用信号，reference-solution probe 在受限结果中甚至低于初始 student。两组 Qwen 数学训练的平均收益与全局优势缩放、同稀疏度随机 mask 对照提供局部支持，但强 TSD 阈值对照已接近该结果，未披露跨训练 seed 不确定性，不能据此签发“只学能力”的因果结论。每 token 两次额外 teacher 评分并非免费：同硬件计时只在较小 teacher pair 更快，30B teacher 两种 student 反而更慢，长度变化也参与总成本。probe 不可信、保留量过小或端到端预算不合算时，保留普通 OPD、已验证的其他选择性监督或不更新；正确性仍由独立 outcome/holdout 验收。 [必要机制与反证](https://arxiv.org/html/2609.21619v1)。<!-- source-family:SF-2026-ARXIV-2609-21619 -->

Teacher 在单图的预测分布可被拟合，却不自动约束学生怎样随视觉证据改变。一个受限分支固定原图生成的 student prefix，在原图和局部编辑图上分别匹配 teacher 端点，再比较两 world 的 log-prob 变化，把归一后的相对变化另作蒸馏 target。第二项会消去两 world 共享的加性 logit 偏移，但不能清除所有 teacher 错误；编辑 world 评分也不是该 world 独立采样的 on-policy 历史。Pair、question、shared prefix、teacher hint 与更新 identity 都须保留，不能把答案一致或 teacher 变化当真实视觉因果。

CW-OPD 的受限 pair/λ=0 对照支持这条目标分工；同向扰动对 transition 不变，反向 teacher 错误仍可使它更差，endpoint 还会接收共同偏差。VLM 编辑验收不认证严格单变量干预，部分任务反退与主 EMA/固定 teacher 扰动实验人口需分开。Pair 生成过滤、两 world 评分和 trainable vision 增加成本；先看双正确率及实际 hold-out 能力，不用低 flip rate 掩盖两边同错。编辑无法保义、teacher 对视觉变化不可靠或预算不合算时保留普通 OPD、可信 grounding 监督或不更新，不由跨 world 匹配自签“学到了 why”。[必要机制与反证](https://arxiv.org/html/2609.38777v1)。<!-- source-family:SF-2026-ARXIV-2609-38777 -->

上述分支监督两 world 的相对响应，但强 teacher 也不能直接替学生读取图像；提高学生对一切扰动的敏感性，又会把无关变化当证据。另一条分支固定原图的 student response 与 prefix，用 teacher 在原图/遮挡图对同 token 的概率下降选择 contrast 位置：只在这些位置放大学生两图分布差异；另对预期保义的轻噪声图收缩差异。Teacher 提供选择与权重，学生自己的两路响应形成辅助目标，不是 teacher 标出 token 真值，也不把遮挡与轻噪声的角色互换。

S-OPD 的受限 count-matched random 与全 token 对照显示，contrast 并非越广越好；mask 可能毁掉目标、noise 也未逐实例认证保义。文本 oracle 补充会改变输入接口，gap 下降有时还来自 oracle 条件变差，不能独立证明感知电路修复。额外 teacher 遮挡评分、学生两种 view 与调参都付训练成本，部署 module 不变不等总预算相同；部分任务/配置仍回退。视觉 gate、扰动语义或 hold-out 不可靠时，保留普通 OPD、可信视觉标签/少量辅助目标或不更新，分别验最终答案、证据利用和端到端训练成本。[必要机制与反证](https://arxiv.org/html/2609.39120v1)。<!-- source-family:SF-2026-ARXIV-2609-39120 -->

### RL Recipe 必须绑定 Optimizer Transform 与 Sharding Layout

相同 GRPO loss 换用 matrix-aware optimizer，并不是只改一个名称。Hidden 2D matrices、embedding/norm/head
可能走不同 parameter router；完整矩阵 orthogonalization 与 FSDP shard layout 还可能冲突：

```text
credit estimator + KL / clipping
→ matrix gradient
→ parameter-class router
→ Muon-like transform or AdamW fallback
→ sharding / collective / checkpoint semantics
→ effective update-scale and outcome evidence
```

Nominal learning rate 在不同 transform 下不可直接比较，update RMS、regularization、fallback 参数尺度、optimizer
latency、memory 与 restart correctness 都要进入 recipe。Muon 在特定 Agent RL 实验中显示的是更大的稳定 update
headroom，而非 spectral transform 的普遍因果优势；后续 matched-scale ablation 也说明收益会被 update magnitude
混淆。AdamW 在成熟 sharding、checkpoint portability 与较小 headroom 时仍是可靠旧分支。

GUI 与 long-horizon tasks 还会把外部 hint、历史错误和跨 step evidence 带进 reward。更安全的层次不是把它们
直接当作 correctness，而是先把 outcome 作为 hard gate，再把辅助 evidence 限定在对应 decision boundary：

```text
verified terminal outcome
→ phase / step identity
→ provenance-bound hint or prior-error evidence
→ bounded shaping / credit adjustment
→ independent outcome and regression check
```

ClawGUI/KnowRL 的环境知识可以帮助探索，但它可能来自同一 generator 或过时界面；MEDS 的历史错误可帮助避免
重复失败，却可能把前序策略、verifier 与环境偏差固化成 reward。Hint、error memory、extractor 与 policy revision
必须分别版本化，并定义 expiry、reset 与 counterfactual no-hint/no-memory slice。Sparse terminal reward 在
verifier 可靠、任务短或辅助证据不可校准时仍更可信；密集 shaping 不能越过 hard outcome gate。

```text
prompt batch
-> replicate each prompt G times
-> rollout workers generate responses
-> verifier / Reward Model scores
-> group rewards by prompt identity
-> normalize advantages
-> actor computes current logprobs
-> reference computes KL terms
-> clipped updates
-> synchronize new policy to rollout workers
```

系统必须防止：

- Group members 被错误跨 prompt 聚合。
- Policy version 与 old logprobs 不一致。
- Variable lengths 造成大量 padding 或 stragglers。
- Reward service timeout 导致 group 缺样本。
- 更新后的 actor weights 未及时同步到 rollout workers。

这些都可能让 loss 数值正常，却改变算法实际语义。

Agent RL 可以继续把 rollout 执行做成独立 service：trainer 提交 policy/version 与 task，rollout workers
运行有状态环境并返回 token、logprob、transition、reward 与 terminal evidence；trainer 控制 cancellation、
weight swap 和 admission。这样 generation/environment latency 不再阻塞 optimizer phase，也能独立扩缩，
却新增 queue backpressure、stale acceptance、crash replay、exactly-once/at-least-once 语义与 sandbox tenancy。

```text
trainer-owned policy epoch
→ rollout-service admission
→ environment-owned transitions
→ provenance-complete trajectory
→ freshness / validity gate
→ optimizer update
```

多个领域共用异步服务后，快环境还会淹没慢环境。Sequential domain RL、joint mixing 或阶段间 on-policy
distillation 是不同分支：前者隔离 domain interference 却产生 order/forgetting，后者吞吐高却需要显式
mixture control。没有 compute-matched order ablation 时，不能把某一 cascade 配方写成普遍规律。

混合目标还要区别生成数与有效消费数：某域的有效贡献同时取决于环境生成速度和通过 mixed-outcome group filter 的比例，按原始请求数配额并不能保持训练 mixture。消费侧可按 domain-tagged group 的 integer quota 接纳；生产侧则读取累计 admitted count 与目标 quota `q_i` 的归一化比值，对跑得过快的域施加 backpressure，减少先生成再丢弃的浪费。这两侧分别控制“哪些组进入 update”与“接下来生成多少”，不应混成一个抽象调度开关。

配额也不能无限等待慢域：bounded wait 后放松 cap 能恢复进度，却会偏离原定 mixture，必须作为可记录的 fallback，而非声称始终保持目标比例。它与 policy freshness 或 importance ratio 修正是不同对象，不能相互替代。`arXiv:2609.22083v1` 的 Table2 与 §3.4.3 给出这一消费/生产分权，但 mobile/desktop 联合训练结果没有独立消融证明 quota 与 backpressure 各自的因果收益；混合稳定或单域训练时，固定同步服务仍是更简单的基线。[受限来源：MintAct v1](https://arxiv.org/html/2609.22083v1)

<!-- source-family:SF-2026-ARXIV-2609-22083 -->

另一条演进把 experience extractor 作为独立 policy：actor rollout 产生 success/failure evidence，extractor
形成可复用策略，再由 actor 在新状态中验证和更新。它比 actor 自我反思更能分离角色，却增加 extractor/
actor 共适应、library merge 与 causal attribution；经验必须保留 source policy、environment、适用条件、
supersession 和 rollback，不能只存一段“成功经验”。

## Rollout 变成服务：Environment、资源与 Policy Freshness

当 rollout 延迟、工具环境和 update compute 使用不同资源画像时，同步 colocate 仍最容易证明，却会放大 idle 与长尾。把 rollout 服务化可以独立扩缩，但必须先明确 environment state、policy epoch、trajectory admission 与失败终态，不能让资源调度暗中改写训练分布。

同步 rollout 的资源人口也可利用同题重访历史：用过去 response 长度的 EWMA 提出排名，让相近长度留在同 actor、短 actor 较早退出；预测低估时，只把该 actor 未完成 response 迁到仍有空槽的 actor，再以 profiled TPOT、GPU-time 与 transfer 条件选择 actor count。改变的是 generation 资源，不是同题样本数或 optimizer commit。[RLHFless v1](https://arxiv.org/html/2602.22718v1)的局部 trace-replay 控制支持这一分支，但依赖排名稳定、迁入槽与 policy/KV identity；过早切分增加传输，槽不足时省费停止。两节点16L40S实测与70B模拟分开，GPU-second proxy不是完整云账费，prewarm/residency/profile/Redis亦付费；原 unique-prefix 单调说法不成立，不采用其保证。预测或传输失配时，回到固定actor/无迁移、完整同步group，调度加速不自签质量不变或生产TCO。<!-- source-family:SF-2026-ARXIV-2602-22718 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2610-03286:start -->
Action-level 调度让工具等待与其他 generation 重叠，却未必更早准备好一次训练更新：同一 prompt 的 group 仍等最慢 trajectory，下一 trainer batch 又等足够完整 groups。因此调度目标可以从独立 GPU utilization 改为下一批完整 group 的 ready time，以剩余生成长度的 heuristic 提议优先级，再让 framework slots、engine prefill token budget、decode retraction 与 trajectory-level KV references 消费同一优先级和容量快照。KV 引用直到 trajectory 完成才释放，而不在一次 tool turn 结束时释放；admission 与 eviction 之间若引用状态变化，先前计算的可回收容量便不可信。

优先级也不能无限压低长轨迹：最后有效 policy version 的工作应提升服务优先级，但这不取消本章的 staleness admission；高优先级 KV 仍放不下时，可受控暂停/降级部分 trajectory 以保护其余 residency，而非让它们反复互相驱逐。[VenusRL 的披露 Hopper、Qwen3/OpenSWE 对照](https://arxiv.org/html/2610.03286v1)支持这一实现分支，不证明任意 length predictor、任务或异步程度都保持训练分布与质量。预测漂移、迁移、缓存快照和环境容量都付费，其 sandbox 过量准入还保留 OOM 后暂停/迁移成本；低并发、组长度接近或版本/容量无法一致维护时，原 action-level/同步策略更简单。Complete-group、behavior-policy identity 与 optimizer commit 仍由算法生命周期验收，不能由优先级或吞吐替代。
<!-- semantic-body-binding:SF-2026-ARXIV-2610-03286:end -->

同步更新并不要求把所有梯度计算都推迟到最后一条 rollout 返回。一条分支冻结当前 policy/version，以 experience table 记录 prompt、turn、trajectory 与完整训练字段；某个 microbatch 的样本及其 group reward/normalizer 都已就绪时，先计算并缓存梯度，与其余 rollout 重叠，仍等同一 global batch 完整后才做 optimizer commit 和统一权重同步。提前的是 compute，不是 policy epoch 的提交；组内归一化尚未完成、样本人口变化或权重提前替换时，不能沿用这一分界声称同步目标未变。缓存梯度增加状态、显存与故障重放责任；[FlexMARL 的受限实现](https://arxiv.org/html/2602.09578v1)支持披露 NPU/Agent 负载中的吞吐重叠，没有独立质量或收敛实测，不能从加速推出数值等价或普遍训练稳定性。预算不足或版本/恢复语义难以保持时，完整同步 phase 仍更简单。<!-- source-family:SF-2026-ARXIV-2602-09578 -->

服务还会改变 policy 能读到的历史。训练与评估必须绑定相同 observation-history 截断规则，而不只是相同模型权重；history limit 改变 conditioning state，跨规则复用 rollout 也需重新验证。AWM 的 4B 对照中，对齐训练后的 limited history 有局部收益，直接在未对齐 policy 上截断却让部分任务明显退步，因此不能把“更短上下文”当免费优化。保留完整历史在信息依赖不明时仍合理；截断分支需计入再训练、信息丢失与独立 outcome 验收，合成环境收益不授真实部署泛化。<!-- source-family:SF-2026-ARXIV-2602-10090 -->

环境可启动还不等于当前任务具备执行前提。固定预置 workspace 在任务与资源稳定时最容易比较；真实云控制台或工具链任务则可能依赖尚未创建的集群、权限和跨资源状态。一个受限分支让环境 owner 保存带依赖的资源 description/configuration 与 create、verify、destroy 操作，在隔离 account/sandbox 中按需 provision，并先验收任务 precondition。Provisioning 成功不是任务成功，资源缺失或 quota 故障也不能直接变成 policy 的负 reward；轨迹须绑定资源状态、准备结果及清理回执，再由 admission 决定能否进入训练。

按需构建提高环境覆盖与并行隔离，却引入账户额度、真实账费、模板/DOM 漂移、长时间资源就绪及清理失败。[云控制台 Agent 的受限实验](https://arxiv.org/html/2606.09447v1)支持该环境分责，但 judge 共识不证明 outcome oracle 没有 false positive，灰度模型与成本投影也不等生产验证。前提无法满足时应隔离本次样本、修复或重置环境，保留准备失败与任务失败两种终态；不能让生成环境或训练 policy 自己批准其验收。重复任务、受限预算及不可撤销资源下，固定已验证环境仍是更安全的基线。<!-- source-family:SF-2026-ARXIV-2606-09447 -->

### Environment 与 Policy 可以共同演进，但 Held-out Evidence 不能回流

基础 environment 与对它施加的 harness transformation 必须分别版本化。增加噪声、工具限制、prompt wrapper 或 reward adapter 会改变 agent 可观察状态和 transition，即使底层 simulator 未变，也不再是同一训练分布。rollout identity 因此同时绑定 base environment revision 与 transformation graph；跨版本复用样本前要证明 observation/action 兼容，否则重新执行。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19880 -->

若 environment 是由模型生成的可执行程序，语法通过只证明它能启动，不证明语义、隔离或评分正确。进入 rollout pool 前必须在 sandbox 中执行 deterministic checks、资源与 effect policy，并用生成过程不可见的 held-out tasks 验证 transition 和 scorer；失败 artifact 隔离而非进入训练。生成环境扩大任务覆盖，却会把 generator bias、漏洞和 evaluator leakage 带入 objective，人工构造或已验证环境在高风险训练中仍是基线。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19197 -->

固定人工 environment 提供清楚 schema、oracle 与长期可比性；当 tool 组合、database state 和 capability gap
快速变化时，可从 tool/MCP specification 生成 candidate environment、task 与 executable oracle，再用 failure
trace 形成 targeted curriculum：

```text
source tool specification and data
→ generated environment + unit tests
→ task / oracle admission
→ isolated rollout and verified outcome
→ failure-family diagnosis
→ versioned targeted curriculum
→ new policy checkpoint
```

Database/tool runtime 拥有环境状态，verifier 拥有 outcome evidence，diagnosis 只产生弱点假设，trainer 才拥有
checkpoint transition。若 held-out arena 的具体失败直接回流为训练任务，再在同一 arena 报告改善，就发生
evaluation leakage；必须冻结 final holdout，并把 environment、generator、oracle、diagnosis 与 policy revisions
共同入账。Agent-World 的作者实验支持多 environment 与第二轮 targeted curriculum 在其 Qwen3/GRPO 设置下
相关于增益，不能隔离各组件贡献，也不证明规模本身带来泛化。监管、高风险或独立 oracle 稀缺时，人工 frozen
core 继续成立；可演进 arena 只作为并存分支。

### Phase-aware Orchestration：Compute 与 Fabric 不能只各自局部最优

最简单的 colocated synchronous RL 让 generation 与 update 在同一资源布局上轮流执行，policy freshness 与
故障边界最清楚；代价是 generation 常受 KV/latency 限制，training 则更偏 compute/collective，固定 allocation
会让两个 phase 互相等待。把 rollout 与 training 分池或异步重叠可以减少 idle，却仍会遇到 response-length
long tail、policy synchronization 与随 phase 改变的 communication pattern。

更进一步的系统分支，是让 compute scheduler 与可重构 fabric 共享 phase forecast：

```text
rollout / update phase and queue state
→ choose worker allocation, parallelism and request migration
→ estimate reconfiguration slack
→ keep current topology or commit a new fabric epoch
→ execute with fallback and observe mismatch
```

这不是“网络自动优化训练”。Scheduler 拥有 policy/rollout version、phase 与 queue；fabric controller 拥有
connectivity epoch。只有预测空隙大于重配置和稳定时间时才切换 topology，否则沿用旧路径。二者必须共享
epoch、commit point、timeout 和 fallback，避免 compute 已迁移而 network plan 尚未生效。收益来自减少 phase
mismatch，新增成本则是 stale forecast、request migration、circuit failure、control-plane race 与硬件成本。

OrchestrRL 的物理实验只验证了有限规模 compute scheduling，光网络与千卡规模收益主要来自 simulation；
因此 RFabric 保持 `Status: Experimental`，正文不保留其 cost-efficiency 数字。已有 non-blocking fabric、
规模较小或 phase 稳定时，固定 topology 仍更简单；严格 on-policy 任务还必须优先限制 async lag。长期原则是：
**当 workload phase 同时改变 compute 与 communication contract 时，资源编排应联合评估，但状态 ownership 与
两阶段证据必须分开。**

### 从“允许异步”到“用算法不变量约束异步”

仅记录 queue length 或 rollout worker 使用的 checkpoint id，不能证明异步 RL 仍在执行预期算法。随着
rollout、reward 与 training 分池，系统调度器可能为了消除长尾而迁移、截断、冗余生成或混用多个版本；这些
操作在资源层看起来都合理，却可能让 training 消费超出目标允许范围的 experience。更稳健的演进是把
staleness 从 scheduler hint 提升为 trajectory lifecycle invariant：

```text
trajectory proposed with V_traj
→ Reserve before generation
→ Occupy only after rollout and reward complete
→ place into buffer V_buf only if V_traj + eta >= V_buf
→ Consume a complete training batch
→ retire reservation on abort / retry / timeout
```

Staleness manager 拥有 admission 与 lifecycle ledger；rollout coordinator 仍可决定 migration、partial
rollout、redundant rollout 和 parameter refresh，但任何吞吐策略都不能绕过前者。它把“最多容忍几个旧版本”
从平均监控指标变成可检查的安全边界，也新增 reservation leak、aborted trajectory 回收、manager
availability、buffer head-of-line blocking 与恢复一致性。同步 pipeline 在规模较小、trajectory 短或严格
on-policy 证据更重要时仍成立；无界异步不能仅因 utilization 更高就被视为演进终点。

#### 版本窗口与 Draft 复用仍须保护 Trajectory Identity

多版本 rollout 池可以用滑动版本窗口消除长尾，但每个 DP 组在一条 trajectory 内必须固定 policy version：较早完成的完整训练批可以先交给 trainer，最老版本的所有轨迹都 collected/forwarded 后，窗口才向前滑动。跨 worker 迁移 KV 也要求同一权重版本；完成一条 trajectory 不等于任意 GRPO 残组都可消费，group membership 和 behavior log-prob 仍须一起绑定。<!-- source-family:SF-2026-ARXIV-2604-26256 -->

该分支用更多 rollout 资源与版本池换利用率，同时增加旧组等待、KV 迁移、buffer 和窗口恢复成本。版本边界混淆或 group 未完整时，不能靠吞吐指标声明 objective 等价；应停止窗口推进、补齐或有规则地废弃整个受影响组，必要时回退同步/更窄版本窗口。

Rollout 的 speculative draft 还可以直接复用 policy 前向已经产生的 hidden state 与 log-prob，但 hidden state 对 draft head 的训练须 stop-gradient，不能让辅助损失未经声明改写 policy objective。Policy/draft 的版本配对、目标 verifier 的概率 law、接受与回退规则共同定义生成分布；这不是把通用 speculative decoding 的加速率直接搬进训练系统。<!-- source-family:SF-2026-ARXIV-2604-26779 -->

Draft head 训练、验证和状态维护仍有成本，长 draft 即使提高 acceptance 也可能降低速度。作者异步235B路径仅为 projection，不能称已测集群吞吐；draft 过期、概率接口不匹配或验证时间超过收益时，应回退普通 policy sampling，保留完整 behavior probability 与 rollout 成本。

相同 policy version 与接近一的平均 ratio，还不足以证明 rollout 与 replay 消费了同一个条件序列。单一文本路径的 tokenizer/prefix 对齐相对容易；多模态路径还要绑定 source image 的预处理、latent 采样方式、注入的 KV layout 与输出 canvas。一个[具体实现纠错](https://github.com/Tencent-Hunyuan/UniRL/pull/547)中，request batch 被 unwrap 后，取图 helper 仍查 batch 字段，导致 rollout 跳过图像上下文注入、走另一条 prefill，而 trainer replay 使用原来的变换；以 replay 重算 old logprob 更只是 trainer 自比。作者 BAGEL-7B-MoT、LoRA、16 prompts×8 samples、512×512 canvas、rollout/trainer 为 8×H20 且 reward 在另一节点的受限对照里，换用 rollout old logprob 后平均 ratio 仍接近一，KV 序列长度却不一致，固定 canvas 还掩盖了另一项尺寸失配。因此应先核 conditioning/layout 身份，再用概率诊断判断更新，不能反过来用 ratio 为身份签字。保存与比较多模态输入和布局增加 trace 与重放成本；无法恢复同一条件时应隔离受影响轨迹、回退已对齐的采样/replay 路径，不把该修复前后的 reward 或时延差当作保持相同分布的通用收益。<!-- source-family:SF-2026-UNIRL-20261005 -->

#### Staleness 还可以成为 Objective-level Actuator

Trajectory lifecycle gate 只能决定样本能否进入 buffer，不能说明已接纳样本在 objective 中应该获得同样大的更新权限。固定 PPO/GRPO clipping 在 rollout 与 current policy 始终接近时最清楚；异步 rollout/training 分池后，同一 batch 内样本的 realized mismatch 可能高度异质，单一 checkpoint lag 无法表达低概率 action 上的风险。

一个实验性分支是对每个 sampled token 计算 current/behavior log-ratio，以 batch 高尾分位数形成 staleness proxy，再只向内收缩 PPO 原有的外侧 clip 边界：匹配较好的样本沿用原 contract，风险较高的样本不能获得更宽的更新区间。这里的关系是 Alternative Branch，而不是替代 lifecycle admission。

它用样本级风险响应换取 quantile 对 domain/length mixture 的依赖；sampled ratio 也不是全 vocabulary divergence 或严格 trust region 的证明，token mismatch 还可能在 sequence ratio 中抵消。proxy 未校准、严格 on-policy 或 correctness 证据优先时，同步或有界 staleness 仍更可靠。

连续生成还会让 replay 的有效支持集随去噪阶段改变。高噪声阶段仍有可比较的随机转移；接近低噪声终点时，转移方差趋近零，旧轨迹与当前策略的细微差异也会放大 likelihood ratio。一个受限 flow-matching 分支因而只复用旧轨迹的前段，再由当前策略重生成末段；训练时将 current/old 的逐步 PPO clipping 与 old/off-policy 的序列重加权分开，不能把 replay policy 错当作同一个 clipping 参照。<!-- source-family:SF-2026-ARXIV-2604-04142 -->

每个条件只保留一个高 reward 样本并随年龄衰减、将一个 replay 样本与其余 fresh 样本混组，可以提高样本复用，却额外引入 reward selection bias、条件覆盖与组内相关性。作者图像/视频模型中 replay 比例过高仍会发散，减少新采样步数也不等于同等 wall-clock 或普遍无损；无法稳定估计末端 ratio、reward 漂移或分布支持不足时，应缩短复用前段、降低 replay 比例或回退完全当前策略采样。这里增加的是阶段化 replay admission，不能替代前面的 trajectory identity 与生命周期 gate。

限制 replay 年龄仍未控制 ratio 的数值尺度。在同一可逆 Gaussian 转移族、同条件和 drift 身份下，可比较 current/old 条件律；但对 D 维项作 mean reduction 不是原始 likelihood ratio，不能悄悄继承它的概率解释。一条受限训练分支用时间相关的 LambdaNorm surrogate，把 detached λ 作为只衰减的预算控制量，限制过大更新信号。它改变的是训练中的 proxy 尺度与阻尼规则，而不是证明旧轨迹已满足当前 trust region。

选择 λ、校准 surrogate 与监测 ESS 增加成本；启发式有效样本量不认证 support、无偏或训练安全。作者 single-seed pilot 与 GenEval 退步的反例只支持局部稳定性/质量取舍，不能将 ratio 数值更温和写成所有任务更优。应分别保留真正条件律、归一化 convention、阻尼前后信号及总采样/更新成本；失配、质量下降或 proxy 无法校准时，缩短 replay、增加当前采样或回退已验收目标，不让预算参数替代独立 outcome 验收。 [必要机制与反证](https://arxiv.org/html/2609.22041v1)。<!-- source-family:SF-2026-ARXIV-2609-22041 -->

#### Replay 是成本与分布的共同选择，不是越新越好

前面的admission gate排除超出算法合同的旧轨迹，却没有回答已允许的轨迹应该使用几次。若rollout生成远比一次更新昂贵，generate-then-discard会重复支付采样成本；有限FIFO buffer可以让训练者均匀重采样、让生成和消费解耦。设计应同时区分buffer horizon `N/R`（每轮加入R条、最多保留N条）、平均reuse `B/R`（每轮更新取B条）与rollout/trainer资源比例，而不是用一个lag上限代表全部选择。

增加reuse降低每次更新分摊的生成成本，也使样本影响未来参数，再被同一参数轨迹重复使用；importance ratio纠正边际policy mismatch并不自动消除这种历史相关性。更大buffer可能增加旧policy多样性、缓和过拟合，同时增加staleness；过高reuse又会降低局部样本多样性并退化。应在匹配学习率搜索后比较达到同一质量所需的采样、更新、估算GPU-compute与实际wall-clock，不能只比较gradient steps。受限Qwen0.6B/7B数学实验和有smoothness/bias/variance/correlation假设的理论支持这一条件分支，不提供生产最优buffer常数或frontier-model保证；生成便宜、相关性强、off-policy方差高或证据不足时，fresh-only与更短buffer仍合理。<!-- source-family:SF-2026-ARXIV-2604-08706 -->

在已接纳轨迹之间采用非均匀 replay 时，还应分清三种统计对象：priority 的年龄与重算规则、buffer sampling distribution 的纠正，以及 action 的 current/behavior ratio。旧 reward priority 可以保持固定，advantage/TD priority 则可能随模型重算；二者都不由“轨迹尚未超时”自动成为当前学习价值真值。对 base priority 施加年龄衰减是一种降低旧排序支配的 proposal，不能让年龄取得 reward 正确性或 state-distribution admission 权。<!-- source-family:SF-2026-ARXIV-2604-16918 -->

采样权重与 action ratio 也不能互相代替：前者回应 buffer 的非均匀抽样，后者回应条件 action policy mismatch，仍不自动纠正 state distribution 与历史相关性。原文默认 FreshPER 不用 buffer IS，而对照 Standard PER 使用 IS，收益不能全部归因 decay；衰减尺度的失败、简单任务暂态不稳与饱和结果仍需保留。priority 重算与年龄控制增加 metadata/诊断成本，ESS 或 KL 的近似动机不是硬有效性证明；reward 改变、权重方差高或排序信号不可信时，缩短 buffer、重算优先级或回退均匀/fresh-only 采样更容易审计。<!-- source-family:SF-2026-ARXIV-2604-16918 -->

Agent RL 还要求 environment failure 与 policy staleness 使用不同终态。Gateway 可以保留服务端实际 token ids，
避免客户端 retokenization 改写 action/loss mask；trajectory 进入 buffer 前再联合检查 generating-policy version、
environment outcome、failure reason 与 reward completeness：

```text
gateway-owned token lineage + environment-owned transition
→ COMPLETE | ENV_FAILED | CANCELLED | STALE
→ only compatible COMPLETE trajectories enter the update population
```

这样 token-in/token-out 解决的是序列身份，version filtering 解决的是 policy lineage，environment state machine
解决的是执行是否形成有效 sample，三者不能用一个“rollout 成功”布尔值替代。代价是 sample drop、buffer holes、
weight-sync race 和 crash recovery；严格同步 loop 在 rollout 短、环境稳定或 off-policy bias 难估时仍更容易证明。

Staleness 也不是 policy identity 的全部。即使 rollout 与 training 标记为同一 checkpoint，二者若经过不同
quantization graph、scale/granularity 或 kernel 数值路径，行为 policy 仍可能不同：

```text
policy identity
= checkpoint / tokenizer / decoding contract
+ forward precision graph
+ quantization scale and granularity
+ operator / kernel version
```

低精度差异还可能通过 importance correction 改变裁剪边界，而不是仅增加 log-prob 噪声。设高精度旧策略为 proximal policy，量化 rollout 为 behavior policy，截断修正系数为 `r = π_behavior / max(π_behavior, π_proximal/C) ≤ 1`。把它吸收到 proximal ratio 后，正优势分支的有效上界会缩成原上界乘以 `r`；仅在 `π_proximal/π_behavior > C`、即 `r<1` 时，扩大 proximal ratio 的正侧上界至 `(1+ε)/r`，才能补偿这项额外收缩，负侧边界并未同样放宽。这是特定截断估计器与 clipping 的接口修正，不证明无偏或一般 trust-region 保证，也不替代后面的负优势数值校准。

即使目标人口校正了，高精度 master weights 的小更新仍可能落在量化网格同一格内，使 rollout 的实际参数不动。一个受限分支在训练前缩放权重、反向缩放相邻 activation，并将变换折入已有归一化参数，使权重变化相对于固定量化步长更可见；这改变的是更新可分辨率，不是给所有 optimizer 统一乘 `s²` 的精确保证。[作者实验](https://arxiv.org/html/2602.13953v1)仍有 FP8 单次 greedy 数学得分退步和缩放过大失效；权重/activation 精度、量化粒度、变换与学习率必须一起验收。独立 inference QPS 测量不能算 RL 端到端收益，质量或数值身份失准时保留高精度 rollout 和原 clipping 基线。<!-- source-family:SF-2026-ARXIV-2602-13953 -->

### MoE Route Replay 也属于 Behavior-policy Identity

<!-- semantic-body-binding:SF-2026-ARXIV-2606-00395:start -->
MoE rollout 若只保存 token、log-prob 与 checkpoint，仍可能漏掉决定实际前向路径的 expert route。直接在训练时用当前 router 重新选择 expert，最简单却会让 importance estimation 比较两个不同执行路径；只保存最终 expert ID 又无法解释 top-k 选择、容量冲突或 router revision。更严格的 sample identity 应把 rollout 时的 predicted route、router/policy revision 与路由约束一起冻结，训练时重放同一路径，再判断该样本能否进入当前 update。

Route replay 把 behavior-policy identity 扩展到条件计算控制流，减少 rollout/training 路径漂移；代价是 route metadata、expert 可用性、负载不均和旧路由与当前参数失配。它不能绕过 staleness gate，也不授权训练端为提高吞吐静默改路。路由缺失、expert 不可用或版本差距超过边界时，应丢弃样本、重新 rollout，或回退 current-policy routing 并把它作为不同实验分支。论文只支持披露的 MoE RL 设定，不证明任意 router、并行拓扑或异步系统都获得相同收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-00395:end -->

一种收敛优先的方案，是让 rollout graph 成为 training forward graph 的数值一致子图，使两边共享 FP8
precision flow，而训练额外保留高精度 master state 和 backward path。它用更一致的 policy coordinate 换取
低精度 rollout/training 的速度机会；代价是训练栈必须支持相同量化算子、activation/gradient 精度设计和
硬件能力。BF16 仍是机制最简单、数值边界最清楚的基线。单篇 FP8 实验不能证明所有模型、长度与 objective
都能保持收敛，更不能把“相同权重版本”简化成“相同 policy”。

还要区分 fake quant 的数值模拟与实际训练算术：高精度 GEMM 读取经过舍入/反量化的值，不等于 rollout 所执行的低比特 GEMM。一个更严格的对齐分支在 learner forward 使用实际低精度路径计算 log-prob，同时保留高精度 master weights、STE 和 backward；更新后将 materialized 量化权重发布给 rollout，连同 scale/granularity、kernel 与量化配置冻结数值身份。W4A16 只将权重降到四位，activation 仍为十六位，不能统称两者低比特；相同 artifact 也不承诺跨 kernel、batch 或设备 bitwise 相同。它增加训练栈适配、量化发布及回归成本，不能顺便证明 clipping objective 的信任域或普遍稳定性；必要算子不兼容、质量退步或 identity 无法核实时，BF16 及显式记录 sampler–learner 差异仍是可用回退。<!-- source-family:SF-2026-ARXIV-2604-07853 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2609-22870:start -->
即使两端统一 FP8 缩小了**前向策略身份不一致**，也不能保证更新目标在低精度下保持相同语义。GRPO 用旧策略与当前策略的 token 概率之比决定是否裁剪；两次 log-prob 的数值误差会在比值中叠加。当负优势 token 的真实比值仍高于下界、FP8 估计却越过下界时，本应继续压低坏输出的梯度被误判为已裁剪而归零。此时 checkpoint、量化路径都可以对齐，失效点却已经从 policy identity 转移到 **surrogate objective 的有效更新人口**。

一种受限的修复分支是周期性用 BF16 shadow forward 校准负优势比值的低端分位数，再结合正、负更新幅度调整另一侧边界。它保留大部分 FP8 训练路径，但额外支付参考前向、分位数估计与校准周期的成本；若样本分布或 objective 改变，边界也可能失准。现有证据只涉及作者所测的 GRPO/DAPO 模型与数学、代码任务：报告中的最高 1.5 倍是排除了 BF16 校准开销的离线训练阶段吞吐，不能当作端到端 RL 收益或普遍收敛保证。BF16 基线、数值路径对齐与裁剪校准是依次收窄不同失效面的方案，而非互相替代。<!-- source-family:SF-2026-ARXIV-2609-22870 -->
<!-- semantic-body-binding:SF-2026-ARXIV-2609-22870:end -->

多领域 Agent RL 又增加第三个合同：**freshness 合格的样本集合，仍可能具有错误的 domain mixture。**完全
streaming 的 generation、environment execution 与 reward 可以去掉 batch barrier，但快环境会填满队列，慢或
困难环境可能长期供样不足。系统需要分别记录 domain quota、historical pass rate、oversampling coefficient、
queue age 与实际 training share；动态 oversampling 是 throughput 与目标分布之间的控制器，不是免费的数据
增强。它可能改善困难域覆盖，也会放大 noisy verifier、让 pass-rate feedback 形成自激偏差。严格 per-batch
mixture 在需要清晰实验控制时继续成立。

最后，普通 GRPO 把成功和失败都留在下一批统一采样中；交互式 tool use 则可把新近 execution failure 转成
一个受限的 corrective branch：保留失败调用与环境反馈，构造 corrective context，以 LIFO 优先消费最近错误，
再从 current policy 采样一组恢复尝试。这个分支获得更密集的 failure signal，却新增 feedback provenance、
simulator fidelity、重复错误去重、额外 rollout compute 与 failure-distribution overfitting。它只在反馈可验证、
错误可安全重放时成立；deployment retry 与 training corrective resampling 属于不同层，不能共用“自我修复”
一词掩盖状态和风险边界。

把 trajectory-level advantage 均匀广播到所有 token 是 critic-free RLVR 的低成本起点，却会让非关键 token 消费同等 credit。Selective eligibility trace 用低熵 token mask 限制 terminal reward 的传播范围，形成稀疏的 token-credit artifact；mask/entropy policy、trajectory revision 与 optimizer update 必须共同版本化。熵与因果贡献不一致、长尾 token 被漏选或方差上升时回退 uniform credit、过程 verifier 或显式 critic。

证据限于 Qwen3 1.7B/4B/8B 和作者 pass@16/效率设置；不证明低熵 token 普遍因果关键，也未建立所有任务、reward sparsity 与异步 rollout 下的收益。 PLATFORM-EVALUATION-SYSTEM 只负责 verifier/evidence calibration；TRAIN-GRPO 拥有 credit assignment。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05965 -->

## 从 Sequence Reward 到 Typed Trajectory

服务化解决 trajectory 从哪里来，不解决 credit 应落在哪个 decision boundary。单轮、同角色、单 verifier 的 sequence reward 仍是最小方案；当角色、阶段、环境状态和分支增多时，样本 identity 必须先细化，才能讨论更局部的 advantage、持久 partial rollout 或跨 policy reuse。

### Hierarchy of Groups 必须成为 Trajectory Identity

标准 GRPO 假设同一 prompt 下采样的 responses 共享可比较起点，组内相对 reward 因而能近似 advantage；长程 Agent 在不同历史中到达相似当前 observation 时，若只按当前 prompt 分组，会把不同 hidden context 的结果当作同一条件分布。更细的 group contract 可以先按任务/当前 state 建立外层比较，再按 history/context identity 建立内层组，只在可比较层级内归一化和聚合 credit。trajectory store 拥有完整历史与 behavior-policy identity，group builder 产生可审计 membership，optimizer 只消费已经冻结的 group graph。

层级分组改善 context inconsistency，却减少每组有效样本、增加方差、history hashing/压缩错误与 group fragmentation；过粗会混入不可比样本，过细又退化成没有相对基线。短任务、同 prompt 独立 rollout 或 history 对动作无影响时，普通 GRPO 仍更简单。无法证明 state equivalence 时，应保留 trajectory-level reward、扩大重新采样或使用 critic/监督信号，而不能用语义相似度伪造同分布组。

上游选择证据、下游根据所选证据回答时，还可以把 group identity 固定到最终选择集合，而不是让一次回答的成败同时代表选择和执行质量。一个受限分支先采样 G 条选择轨迹，再对每条轨迹的最终集合独立重采 N 个回答：把回答正确率均值作为该选择轨迹的 reliability credit，广播到整条 controller 轨迹；reasoner 则只消费终轮回答的组内 credit，并按回答方差选取一个集合组更新。这样把“选到可回答的集合”与“在该集合上回答”拆成不同条件人口；均值仍依赖 evaluator，不是集合充分性或选择因果贡献的真值，按方差选组也改变实际训练分布。<!-- source-family:SF-2026-ARXIV-2602-18645 -->

[必要方法与反侧](https://arxiv.org/html/2602.18645v1)在同一 Qwen3-4B 的两个 prompt 角色中使用 G=N=6，低方差组的 advantage 置零，但所有组方差均为零时的选组分布退路未明确。额外 G×N 回答、编码和迭代调用都付费；去掉 reliability 的对照也改变嵌套采样与信号，不能把收益全归给 credit 分责。六个单变量时序任务中存在更强基线，低覆盖率分组的高准确率还混合任务难度，不证明少选证据必然更好。集合或 evaluator 不可比、组退化或净预算不合算时，应保留同条件普通 group、统一 outcome credit 或明确的重新采样退路，而不是把这个分支称为无偏标准 GRPO。

逐轮 credit 也可在单条 session 内比较，而不是跨 completion 构造标准 GRPO group：终局用户模拟器 satisfaction、每轮 GenPRM 原则分与 costly-action penalty 合成后，以本条轨迹所有 turn rewards 的均值/方差归一；下一批再按平均 cost 偏差更新有界软 multiplier。[InteractCS-RL v1](https://arxiv.org/html/2602.22697v1)的 PID 是成熟控制复用，局部增量在 session/turn 信号与 multiplier 联动，既不识别 token 因果，也不认证硬预算；7B 测量仍越过标称 voucher 目标。同源模拟器/judge不能验真实客服，persona、roleplay、process scoring与校准均付费，部分迁移任务退步；反馈、支持人口或质量失配时，保留固定权重、可靠outcome/真实成本核验，硬预算继续由外层权限与执行边界承担。<!-- source-family:SF-2026-ARXIV-2602-22697 -->

#### Turn Index 只是受限 Comparison Key

把不同轮次的 rollout 全部 pooled normalization，在 context distribution 随深度变化时会混合不可比状态；按
`(prompt, turn-index)` 分组，并配合 sqrt-depth rescaling 与 turn-level clipping，可以把 process credit 对齐到更细的 turn unit。
但 turn index 只描述控制流位置，不证明两个 trajectory 处于相同环境或 belief state。Group builder 拥有 membership 与
context identity，optimizer 只能消费冻结 group；group size 小于等于一或缺少 ground-truth answer 时，应退回 outcome reward、
critic 或其他可验证 signal。<!-- semantic-body-binding:SF-2026-ARXIV-2605-06200 -->

这条分支用更可比的局部 normalization 换取 group fragmentation、depth-dependent bias 与额外 attribution 计算。现有证据只覆盖
七个 QA benchmarks、三种 Qwen backbone、本地 Wikipedia retrieval 和 8×H20/VeRL；Integrated Gradients forward 成本以及
production asynchronous trajectory 均未验证。context similarity 随深度下降时，不能靠同一 turn number 继续宣称 state equivalence。

当逐轮 return 已可计算、却不想另训练 parametric critic 时，另一条受限路线不构造同轮 reward group，而用其他 trajectories 的 return 做时间核回归：对当前轨迹第 t 步，把其他轨迹在各 t′ 的 return 按 Gaussian 时间距离加权归一化，得到 baseline，再从本步 return 中减去它。排除的是当前整条轨迹，而不只当前样本，以减少自己的结果泄入基线；它仍是以控制流时间作特征的估计，不认证不同 observation、history 或 policy 的同分布，也不因排除自身就获得任意离策略条件下的无偏证明。trajectory store 因而还须绑定任务人口、history、behavior-policy revision 与采集轮次；核带宽只规定哪些时间邻域贡献估计，不能代替这些身份。<!-- source-family:SF-2026-ARXIV-2602-12351 -->

这以显式 return buffer、核计算和支持集选择换取免训练 value network；保留更多旧轨迹可以降方差，却会引入陈旧 policy/history 的错配。[受测导航分支](https://arxiv.org/html/2602.12351v1)在 rollout buffer 为16时保留最近256条估计 baseline，并明确承认这一取舍。同 dense reward 的有限带宽与无限带宽比较中，长轨迹改善而中等长度成功率反而下降；它不是所有 horizon 都更优的证据，和 sparse outcome baseline 的比较也同时改变了 reward。缺少可比支持、核邻域有效样本过少或 staleness 超出校准时，应刷新轨迹、缩小复用支持或回退普通同条件 group/critic，而不是把更大的 buffer 当作免费信用精度；异步派发 episode 与同步 DDP 更新也属于不同执行合同。

层级还可以来自 policy 显式生成的 strategy state，而不只来自已有 history。反应式 Agent 直接从当前 observation 产生
action，在 horizon 短或环境变化快时最简单；长程任务的高层意图若始终隐含在 token 中，strategy quality 与 action
execution 会共享一个无法拆分的 credit。一个条件分支先从初始 observation 生成带身份的 strategy，再为每个 strategy
采样多个 action trajectories，分别构造 strategy group 与 action group，使高层探索和低层执行在同一 frozen group graph
中接受相对更新。

Strategy generator 只提出计划，trajectory store 绑定 `strategy_id + initial state + behavior policy`，group builder 冻结
`N strategies × M rollouts` membership，optimizer 才能消费两层 credit。收益是暴露高层 credit boundary；代价是 rollout
预算相乘，而且初始时刻冻结的 strategy 会在环境变化后变陈旧。非平稳或部分可观测环境应允许 receding-horizon revise，
或回退 reactive GRPO/critic；不能让旧 strategy 覆盖新的 authoritative observation。现有证据只覆盖 ALFWorld、WebShop
与 SciWorld，不建立生产 Agent 的通用优越性。

<!-- source-family:SF-2026-ARXIV-2605-06642 -->

<!-- SF-2026-ARXIV-2602-22817 -->

跨 update 使用历史经验时，还要区分“历史参与 credit 的参照”与“历史样本直接参与 policy loss”。前者可以为同一任务目标和初始环境保留 transition graph，让旧路径帮助评价当前动作离成功状态的距离；也可把旧组的 outcome 作为 detached reference，与当前重新采样组共同计算相对分数。真正进入 clipped loss 的仍只有 current-policy rollouts，而不是把旧轨迹 token 伪装成新样本。这改变了 credit estimator 和任务重访分布，不等同于保持原 GRPO objective 完全不变。

这种参照要求任务、状态与转移条件仍兼容，重访也应替换既定 rollout 配额而不是隐形增加预算。图越积越大、旧路径失效或相同 observation 隐藏不同状态时，历史参照会引入成本与偏差；应保留仅当前组的基线，并同时核验 group size、环境步数和最终 outcome。TIGPO 在两个交互式环境中的实验支持该受限分支，但对照的每组采样数不同，不能将收益全部归给图持久化，也不能将测量中未显著增加开销写成历史管理免费。[跨更新参照与当前策略采样的区分](https://arxiv.org/html/2609.03383v1)

交互工具轨迹的另一种credit粒度是两次环境交互之间的chunk：按chunk到终局的距离折扣，再把同一份权重送到该chunk的tokens。这与按token距离折扣不同，也不证明chunk内每个token具有同等因果贡献。若优化器使用chunk内token概率比的几何均值及current/old或backend mismatch mask，几何均值不是完整chunk的联合概率比，过滤还改变实际学习人口，不能据此授无偏off-policy或尺度均衡。为探索成功后续，可以重放teacher prefix，再从不同anchor采suffix；正确prefix是训练条件，不是部署可得的事实，reset/replay、额外teacher和rollout均付费。跨backend或环境无法可靠重放时，应保留一致生成/训练后端、从真实初始状态采样与原credit基线，并分别验收chunk权重、过滤人口和最终outcome，不将组合配方的收益归给单一credit机制。<!-- source-family:SF-2026-ARXIV-2512-24873 -->

### Immediate Reward、Delayed Correction 与 Staleness 是同一 Lifecycle

交互轨迹的 credit 还必须对齐真实执行顺序。若环境在后续 turn 才暴露早期 action 的后果，训练 artifact 应把 reverse-turn correction 指回原 action，同时绑定产生该 action 的 policy version；不能把迟到信号平均分给当前模型的所有 token。它提高因果对齐，却依赖可追踪 action identity，并会放大长延迟与 stale-policy variance；无法建立 lineage 时应降低权重或重新 rollout。<!-- semantic-body-binding:SF-2026-ARXIV-2608-18682 -->

长 Agent trajectory 可在 stage 完成时得到 immediate reward，再由最终 outcome 产生 delayed correction；两者
必须绑定同一 behavior-policy/token identity。若 correction 到达时 policy 已更新，trainer 要么丢弃、降权，要么
使用可验证的 off-policy correction，不能把旧 credit 当成当前样本。

GrandCode 提供这一多阶段 reward lifecycle 的受限案例，但独立 normalization、缺少关键 ablation 与未公开训练
代码使 headline 不能归因于某一组件。短任务、可靠 terminal verifier 或延迟很低时，单一 terminal reward 仍更简单。

若每一阶段都同时拥有即时信号和未来 outcome，可以分别对 centered immediate deviation 与 future-return
deviation 做组内标准化，再在同一 behavior-policy identity 下组合。这样不会让一个尺度更大的终局 reward
吞没局部防御、格式或工具阶段信号；代价是两套 normalization population、权重和方差都会进入 objective identity。
它仍是 outcome-conditioned proxy，不是该 turn 对结果的 causal contribution。尤其在攻击/防御训练中，局部
“看起来安全”不能越过最终 verifier；短轨迹或可靠 terminal reward 下也没有必要增加这条分支。

多个 reward criterion 的尺度还可以先各自在同一 prompt 的 rollout population 内归一，再按显式权重合并；合并后的 advantage 另作 batch-level center/scale。这两个操作拥有不同对象：前者决定各criterion如何参与相对目标，后者决定本批组合信号的更新尺度，不能把原reward先相加再组内归一当作等价实现。分别归一会改变奖励的相对优先级，不保证冲突目标被同时保留；常量/零方差criterion的处理约定、容易满足的格式reward与质量reward的权重、group及batch人口都属于objective identity。[GDPO 的受限方法与消融](https://arxiv.org/html/2601.05242v1)说明末批尺度处理本身也会影响训练，因此应分别验收各criterion、组合utility和数值/训练预算，而非由advantage更均匀推定没有reward hacking。额外grader、统计与校准均有成本；人口或utility不稳定时，保留原始reward组合、单一可信verifier或停止该更新分支，不以归一化替代目标选择。<!-- source-family:SF-2026-ARXIV-2601-05242 -->

当组合系数承担 Lagrange multiplier 的职责时，标准化还会改变约束控制的单位：先将 reward 与 weighted costs 相加再组内标准化，有效 cost 系数会随各分量方差及组合 covariance 改变；先分别标准化再组合，则是在新的单位上定义相对目标，不能自动继承原始 cost 的 dual update 或 violation guarantee。应同时保留各项原始 violation、阈值、乘子更新与标准化后 advantage，constraint controller 不等于 execution veto。[CGRPO exact-v1](https://arxiv.org/html/2602.05863v1)的有限 NAVSIM/Qwen2.5-VL 对照支持这一接口差额，但困难场景仍未达若干目标，进展与安全也有取舍；额外仿真、统计和调参需计价。单位不明、零方差处理缺失或 violation 退步时，回退原 reward/cost 定义、可靠约束控制与独立安全 gate，不把分别归一当作满足真实约束的证明。<!-- source-family:SF-2026-ARXIV-2602-05863 -->

这里还要区别“分别标准化两种不同来源的信号”与“逐 turn 标准化后再求轨迹总和”。后者会让每个 turn 的比较群体和尺度先改变，再相加；若把原始 discounted return 先相加再做组内标准化，得到的符号与前者未必相同。因此，reward shaping 的设计不仅要决定奖励什么，还要决定 normalization 在哪一级发生。一个有条件的分支是：先累计折扣后的原始局部 reward 与 outcome，再对整个 return 做组内标准化，并以单独标准化的 outcome advantage 作辅助校准。它把轨迹级比较和终局信号明确分开，却新增折扣、组合权重及各自 population 的目标身份；不能由一次诊断中的符号一致，就保证所有任务的 credit 正确。

校准仍要同时检查局部信号能否区分终局 outcome，以及它是否只奖励容易出现的表面行为。局部 tier 与成功的相关性不是因果贡献，字符串或对象比较器的宽松等价也可能误给工具 reward。`2604.02869v1` 对5952条rollout的受限诊断支持上述归一化顺序差异；其多配置训练同时改变learning rate、KL、步数或prompt，不能把headline收益单独归给reward重排。短轨迹、单一可靠terminal verifier时，原有终局GRPO仍更简单；这里也不否定前一段对不同来源分别标准化的设计分支。<!-- source-family:SF-2026-ARXIV-2604-02869 -->

Multi-Agent trajectory 还暴露另一类 credit 问题：不同 role 的 action 发生在不同 conditional state，不能把
同一终局 reward 直接复制给所有 agent，也未必能构造“同 prompt 同 state”的 group。可以由独立 coach 按
role、input、action 与 tool feedback 给出 process reward，再使用跨 trajectory normalization 更新各自 policy。
它获得更密集的局部信号，却新增 coach latency、role bias、state comparability 和 reward collusion；stateless
coach 可能系统性偏爱某类局部动作而损害终局任务。Outcome verifier 仍应拥有最终 gate，process reward 只在
有独立 calibration、至少多次 seeds/checkpoints 且成本可接受时作为辅助信号。

多轮 Agent RL 还会让同一 trajectory 同时包含可验证与不可验证步骤。把 terminal reward 均匀复制给每个 token
容易奖励偶然动作；只保留明确可验证步骤又可能删除完成任务所需的探索。更稳健的 update contract 应把
partial-verifiability、step boundary、shared prefix 和 future consequence 一起版本化：同一 prompt 下，只有共享
相同 prefix/state 的候选才适合局部相对比较；截断后仍要保留后续 outcome 对当前 step 的 delayed credit。
GUI-Libra 与 SLATE 为这一边界提供了实验性证据，但不证明其 trust region、sampling ratio 或局部 scorer 可跨 GUI/
retrieval workload 外推。

Continual GUI adaptation 把 reward contract 再推进一步：新 domain、resolution 或界面版本顺序到达时，只优化当前 task reward 会遗忘旧状态；直接 replay 全量历史虽然清晰，却增加数据保留与训练成本。用 spatial / scale exploration reward 鼓励当前 policy 覆盖新的 action region，可以缓解受控 distribution shift，但 diversity 本身不是 correctness，可能奖励无意义点击。工程上必须把 current-task correctness、backward retention、exploration reward、domain order 与 checkpoint 共同版本化，并以旧域 replay/canary 检查遗忘。

#### Mastered Set 需要 Acquisition–Retention Turnover Ledger

只记录 checkpoint 的总正确率，在任务分布稳定、训练只关心净增益时最简单；continual RLVR 中，相同总分却可能由大量新解出题目抵消大量已掌握题目遗忘。训练控制面因此要把 held-out item identity 与 checkpoint 绑定，分别记录 `incorrect -> correct` 的 acquisition 和 `correct -> incorrect` 的 forgetting，并把 mastered set 的净 turnover 作为独立 gate，而不是把它折叠进平均 reward。

当遗忘存在可修复窗口时，review controller 可以在旧题首次失败后延迟复测，确认不是采样噪声，再把仍未恢复的 item 放入下一轮 rollout 的有界 replacement queue。这样用有限回放预算定位 retention failure，却新增 item-level 历史、复测延迟、队列偏置和对 stochastic decoding 的敏感性；队列只能替换既定 rollout 配额，不能隐形增加预算或让旧题长期挤占新分布。item identity 不稳定、复测无法区分随机波动或任务本身已变化时，应回退固定 replay/canary 与 aggregate retention slice。

`arXiv:2606.03087v1` 在两个 backbone 和 20 个文本、图像、视频数学 benchmark 上支持 acquisition/retention 分账与有限 review queue；它没有证明 repair window 跨任务固定，也没有把“零额外 rollout”证明为零训练成本。

<!-- semantic-body-binding:SF-CORRECT-SET-TURNOVER-RLVR -->

探索也不能只追求 action entropy。若 verifier 能识别多个正确 outcome modes，可以在正确轨迹集合内鼓励
mode-level diversity，再对高置信错误施加更强 correction；这分别解决 correct-mode collapse 与 overconfident
negative update。二者都依赖当前/reference policy 的概率校准、长度归一化与 binary verifier，不能合并成
“多样性越高越好”。DSDR 与 ACE 是这两个相邻 actuator 的受限案例。

当 GUI 轨迹的 demonstration match 被用作 verifier，未匹配既可能是真错，也可能是另一条有效路径，直接赋强负 advantage 会误罚探索。一个受限修正先用同组经验匹配率 `p_g` 构造 `lambda_g=min(lambda_0+kappa*p_g,1)`，仅将负 advantage 乘以它：组内低匹配时弱化负更新，正更新不变。这和下述 reference-confidence 放大负梯度控制的是不同噪声来源。匹配率不是真值，整组 reward 为零也不会凭缩放产生有效 advantage；demo/verifier 校准、额外采样与 KL 仍需付费。有限对照中两项在线环境改善，但离线 action accuracy 的部分指标下降，不能声称统一提升；可信负例与固定环境可回到普通组更新。<!-- source-family:SF-2026-ARXIV-2602-22190 -->

在已经判断为负的同组轨迹中，还可将 advantage 乘以 `1 + alpha * softplus(c)`，其中 `c` 是当前 policy 相对 frozen reference 的逐 token log-probability ratio 均值；正确轨迹保持原 advantage。这样额外抑制相对 reference 更受偏好的错误，但 `c=0` 仍增加 `alpha*ln(2)`，不是只惩罚正置信度；reference 概率也不认证真值。计算权重时 stop-gradient，理想 on-policy、无限样本下仍有分解残差，不应把该更新称为与 KL 正则精确等价或普遍降低方差。[ACE 的有限数学对照](https://arxiv.org/html/2602.21420v1)支持局部收益，部分模型/小样本任务的低 `k` 也退步；binary verifier、长度归一化、advantage 噪声和 reference 校准继续付费，所谓无新增计算只在原流程已取得相应 logprobs 时成立。噪声负例被放大或 reference 失准时，回到普通组更新和已验证的 correction 权重。<!-- source-family:SF-2026-ARXIV-2602-21420 -->

即使已经只在正确 outcome 内测多样性，也要区分“很少进入一种解法”与“进入后无法完成”。前者改变的是早期分支概率，后者是条件执行能力；单看自由采样的 pass@k 或正确轨迹数量会把两者混在一起。在可枚举、可验证的环境中，可以固定任务与预算，对照自由采样和外置的最小可行入口，再观察后续完成率。有限预算内没有采到某分支，并不证明其概率严格为零；外置入口得到的完成率也不能直接替代 policy 自然选择入口后的条件分布。

这把探索调节从“整体提高 entropy”收窄到具体失效位置。若主要压力是入口收窄，增加相同 policy 的重复 rollout 可能收益递减；受限的入口配额、多解监督或 checkpoint 混合可以作为实验分支，但分别需要可行族定义、数据覆盖和额外模型/校准成本。长轨迹仍可能在进入后执行失败，跨模型的首计算 proxy 也不等于完整解空间；因此不能把一个受控实验写成 RLVR 必然收窄、SFT 必然更优或参数插值无损。单次正确率是唯一目标、可行分支不可验证或干预成本过高时，普通组采样与现有 regularization 仍是清楚的基线。

多模态 tool RL 还应把 interaction budget 写入 reward。Python、crop、zoom 或 perception tool 可能增加必要证据，
也可能被 policy 当成容易获得的 shaping reward；group selection 若偏向恰好会调用工具的样本，又会改变训练分布。
因此必须分别观察 task correctness、tool necessity、call cost、sandbox risk 与 no-tool baseline。PyVision-RL 只证明
作者环境中 reward、group selection 和 media materialization 的联合改变有效，不能把更多 tool calls 视为能力。

另一个分支让两个 policy 在自博弈中共同生成 task 与 solution，或让当前 policy 在临时 memory scaffold 中跨 rollout
探索，再把经 verifier 接受的经验内化到参数。这提高 curriculum coverage，却新增 role collusion、self-confirmation、
off-policy drift 和“临时状态何时清空”的问题。Tool-R0、EMPO² 与 CUDA Agent 的 executable-kernel 环境支持
`curriculum/proposal owner != solver/update owner != verifier` 的分责；固定外部题库和单 policy rollout 在复算、
隔离或高风险任务中继续合理。

具体的工具调用自博弈仍需要外部 task specification 限定 domain、context、工具菜单及调用数；这些支持集约束不等于“没有人工答案就没有外部先验”。Generator 的格式、schema 和参数词边界检查只能确认生成题目与 gold calls 的局部一致性，不证明语义正确或真实执行安全。一个受限课程控制用多次 Solver rollout 的成功比例提出中等难度区间，再另付 judge 调用检验语义代理：[Tool-R0 的角色分离、冻结出题方与难度门消融](https://arxiv.org/html/2602.21320v1)支持该接口差别，而非无限自提升。重复采样与 judge 都进入预算，AST 工具匹配不替代执行结果；同源自确认、难度落到两端或小模型课程饱和时，仍回退外部验题、固定题库与单 policy rollout。<!-- source-family:SF-2026-ARXIV-2602-21320 -->

没有外部答案标签时，出题难度还可以由两条回答路径的差异提出：Questioner 在生成图像问题时同时给出直接答案，冻结 Solver 对该问题多次推理，以多数答案及其票数比例构造反馈；直接答案与多数答案一致时偏向中等一致度，不一致时奖励较高一致度，再只让 Solver 学习票数比例落在有限区间的题目。这改变了课程提案和样本准入接口，却没有增加独立真值来源。两角色同源、多数答案一致地错或问题本身失真时，难度门仍可能放行；四选项与格式检查只保证可解析，不能把这种自举训练奖励称为可靠 verifier。<!-- source-family:SF-2026-ARXIV-2601-10094 -->

双路径让固定外部题库之外多了一条实验分支，也增加生成问题、重复 Solver rollout、伪标签筛选和两角色更新成本。[V-Zero 的受限对照](https://arxiv.org/html/2601.10094v1)支持双 track 和难度筛选在指定 Qwen2.5-VL 配置中的差别，但直接答案与推理答案并非同模型、同条件的纯 reasoning 对照；3B 模型第二轮还略有退步，不能归纳为无限自改进或唯一容量原因。训练从约9K来源图像选4K，Questioner 另用GPU托管反馈 Solver，作者每轮约9小时也不证明比人工标注监督更低总成本。自确认、题目失真或预算失控时，回到独立验题、冻结题库和普通 outcome GRPO，而不以投票比例替代正确性。

自博弈还会形成一个相互追逐的反馈环：出题方把 solver 的失败当收益时，可以选择过难、重复或不可满足的问题；solver 的采样若越来越集中，又会让一组答案几乎全对或全错，使组内相对奖励缺少有效差异。此时问题不只是“entropy 太低”，而是题目支持集、可解率和梯度信号同时改变。一个受限分支只在尚未解出的固定目标上提出有边界的辅助问题，并用 guide 对问题质量给出代理，把 solver 的 correctness、难度奖励和尝试/长度 shaping 分开记录。Guide 仍不拥有数学真值，最终接受依赖可执行 verifier；代理高分不能授权扩大难度或覆盖域。<!-- source-family:SF-2026-ARXIV-2604-20209 -->

这一分支增加目标条件、guide 调用与角色训练成本，也可能让 proposer 迎合 guide，或使 solver 与课程一起收窄。验收需在同预算下分别看生成问题的有效性、目标覆盖、可解率分布、组内奖励退化和外部留出任务，而不是只看自博弈 solve 曲线。作者在固定 Lean 目标上的局部消融支持这条控制压力，但移除目标条件或冻结出题方的配置还同时移除了 guide，不能把差值纯归一个部件；它没有证明任意 GRPO 都会塌缩或无限自博弈必然改进。代理失准、可解率落到两端或 verifier 支持不足时，回退冻结题库、普通组采样或单独验证的 curriculum，比继续加大自生成量更可审计。<!-- source-family:SF-2026-ARXIV-2604-20209 -->

### Fork Placement 要追踪 Belief Shift，而不是假设中点最有信息

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11061:start -->
树式 rollout 若总在固定中点、固定 token 数或均匀边界处分叉，控制最简单，却会把比较预算花在 policy 尚未形成不同答案倾向，或答案已经基本锁定的位置。一个更有针对性的控制面先枚举可合法分叉的边界，再用探针比较边界前后 answer-belief distribution 的变化，只把 fork 放在 belief shift 足够大且兄弟分支仍可能分化的位置。

该 selector 只拥有 sampling topology：它决定从哪个 checkpoint 复制 policy state、生成多少 sibling 以及消耗多少 probe budget；leaf verifier 仍拥有终局正确性，global/local credit 仍由 reward owner 计算。候选边界、probe 模型与版本、belief label space、阈值、最大分支数、复制的 KV/RNG/tool state，以及 fork 后共享与独立的 history 都必须进入 run identity。训练前得到的静态 belief-shift vector 在 checkpoint 更新后可能失效，不能默认为在线、持续校准的控制器。

收益来自把有限比较放到更可能改变解法的决策点，但它会增加 probe forward、checkpoint materialization 和树调度成本；siblings 最终收敛到同一答案时，局部多样性也可能没有新增 credit。现有结果只有少量模型、数学与代码任务以及 best-per-arm checkpoint 对照，且某些代码设置并不优于固定中点，不构成普适 fork rule。probe 漂移、边界不可定义、分支差异不足或探针开销进入 critical path 时，应回退固定中点、均匀分叉或普通链式 group sampling，而不是让 selector 以“belief 改变”替代 verifier 的事实判断。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-11061:end -->

### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界

#### Evidence-derived Rubric 是版本化 Reward State

<!-- semantic-body-binding:SF-DEEP-RESEARCH-RUBRIC-RL:start -->
单个 judge 分数在任务定义稳定、答案短且标准明确时最简单；研究型 Agent 的目标却常由多条可核验约束共同组成，free-form judge 容易把遗漏证据、论证质量和表达偏好混在一个标量里。一个受约束分支先从外部证据生成原子 rubric，再用 rubric 对 policy output 评分；rubric 的来源、粒度、生成模型、bootstrap 轮次、版本与适用范围因此都属于 reward identity，不能只保存最终分数。

原子 rubric 增加 reward density 和失败定位，却把检索遗漏、错误约束、自举偏置与 evaluator 共偏差带入训练。Reward owner 只接纳带 provenance、独立抽检和冻结版本的 rubric；bootstrap 改写必须形成新 revision，并监控分数极化、约束收缩和跨轮多样性。证据不足、polarization 上升或后续 bootstrap 退化时，应停止自举并回退人工/静态 rubric 或终局 verifier。现有 exact-v1 结果只覆盖论文报告的 research-agent 任务、模型、搜索环境和 bootstrap 深度，不证明自动 rubric 会持续自我改进或取得事实 authority。
<!-- semantic-body-binding:SF-DEEP-RESEARCH-RUBRIC-RL:end -->

版本化 rubric 还可成为课程的控制面，而不只是固定 reward 列表。先在初始 policy 的 rollout 人口上分别记录 applicability 和条件成功率，再划分 foundational/advanced 项；训练中以 easy rubric 的 batch 平均奖励作门控，只有连续窗口内每一步都超过阈值，才逐步提高 hard rubric 的 reward 混合权重。它改变的是监督权重，不是直接重采样任务，也不能把最初的难度标签视为后续 policy 的永久难度。覆盖率、teacher/ground-truth 判分、窗口与 ramp 都属于 Reward State；Bernoulli reward 的变异系数不证明实际梯度方差下降。保留原 outcome reward、固定 rubric/静态课程作退路，并将 rubric 构建、判分与训练费用同预算比较；门控失准会延迟或过早触发监督。<!-- source-family:SF-2026-ARXIV-2602-21628 -->

Rubric 还可以改变 credit 的比较单位。把每条约束的响应级通过/失败分数投影到相关 token，再把所有回答的 token 混作一个归一化组，会让长回答贡献更多统计权重。一个条件分支由单独训练的 relevance discriminator 提议 token–criterion 对应，在每条回答、每条约束内部标准化，再与跨回答 outcome advantage 组合；前者定位局部更新，后者保留整答优劣，不能互相替代。相关性标注不是因果贡献，统一相关的 token 还可能形成零方差，因此分组、数值保护与混合权重都是 objective identity。

这用额外判别器训练/推理和标注偏差换更密的 credit；局部项过强会压倒整答目标，误定位则把正确 outcome 归给错误 token。受限指令遵循实验在 Qwen/Llama 小规模 policy 上支持这种分组选择，却出现部分域外能力下降，不能称普遍保持通用能力，也未验证长程 Agent。标注或收益不稳时，回退响应级 rubric 与 outcome-only GRPO。[Rubric-to-token 分组机制及消融](https://arxiv.org/html/2604.02795v1#S4.SS2)

把过程代理与终局结果直接相加，在代理已可靠校准、任务确实需要相应过程时很简单；检索任务中的 embedding 相似度却可能把有效但非典型的查询分解打低分。一个条件分支由二元 outcome 控制辅助项：`r = r_outcome + β(1-r_outcome)r_process + r_format`。已通过终局合同的轨迹不再因这项过程代理被减分或额外奖励；未通过的轨迹仍可获得有界 shaping 信号。这里控制的是训练 reward 的聚合，不是证明中间步骤正确，格式奖励也仍是另一项独立信号。<!-- source-family:SF-2026-ARXIV-2604-07415 -->

这种 residual 聚合保留稀疏终局判断的优先性，却不能让错误轨迹上的高相似度自动成为有效证据；代理仍依赖 retriever、encoder 和分解方式，并增加计算与动态权重的状态。受限问答实验中，中间奖励在需要多跳检索的任务上有益，在不需要分解的任务上反而退步，因此是否开启和如何加权应按任务切片验证，而不是统一加密 reward。终局标签不可靠、代理收益不稳或成本超过收益时，回退 outcome-only 或经独立校准的过程奖励；没有人工标注推理轨迹也不等于训练不需要最终答案真值。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08061:start -->
Outcome verifier 稀缺时，可以让 policy 不可见的 grounding passage 与 weighted rubric 产生 criterion-level reward：policy 只生成答案，冻结 judge 读取受控证据并逐项打分，trainer 再按声明权重聚合给 GRPO。Grounding、rubric、weight、judge 与 policy revision 必须共同标识；judge 只拥有该协议内的 score，不拥有事实或发布 authority。同一 judge 同时训练和评价会造成 shared-bias 与 reward overoptimization，合成 criteria 也可能错误；高风险或漂移时回退 executable verifier、人工 rubric、outcome-only reward 或 Unknown。 [受限证据：arXiv:2605.08061v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-08061:end -->

#### Rubric Pool 还需要 Admission、Consolidation 与 Retirement

冻结 rubric 适合任务契约稳定、人工标准明确的训练；搜索型 Agent 的失败模式会随 policy 和检索环境变化，单次生成的 rubric 很快变成陈旧 reward state。可复用 rubric 因而不能只是自由文本缓存：候选规则先绑定产生它的 evidence、policy、任务和 judge，经独立 outcome 对照后才能 admission；语义重叠项合并到 common pool，持续失配或随 policy drift 失效的条目则 quarantine 或 retirement。

```text
trajectory contrast + evidence provenance
-> candidate rubric
-> outcome-calibrated admission
-> deduplicate / consolidate into versioned pool
-> apply as bounded process reward
-> revalidate, quarantine or retire on drift
```

复用能提高 process-reward density 并减少每轮重新生成，但会把 judge bias、错误规则、跨任务污染和陈旧标准放大到更多 rollout。rubric pool 只拥有过程诊断与辅助 credit，terminal verifier 仍拥有 correctness；缺少独立校准、domain 变化过大或 pool 的 false admission 无法量化时，应回退静态人工 rubric 或 outcome-only reward。`arXiv:2606.03239v1` 的结果只覆盖所测 Qwen3 scales、multi-hop QA、搜索环境和 LLM judge，不证明 rubric truth、跨域稳定或自动生命周期可以无人监管。

<!-- semantic-body-binding:SF-ARBOR-REUSABLE-RUBRIC-BUFFER -->

#### Adapter 约束会让 Token Credit 退化为少数 Residual Direction

按 token 分配 surprisal、entropy reduction 或 policy-divergence weight，是全参数 update 能沿多个方向表达差异时合理的旧路径；
LoRA/adapter 把更新限制在低秩子空间后，不同 token signal 可能投影到少数相似 residual directions，表面上存在细粒度权重，
实际 gradient mass 却高度集中。Credit owner 因而要先记录 weight Gini、effective-token ratio 等 concentration diagnostic，
再决定是否把 advantage 按 adapter-residual contribution 重分配；trajectory outcome reward 仍拥有 correctness gate，adapter
diagnostic 只拥有 token 内部的分配建议。

这条分支可在 signal degeneracy 已被观测时恢复一部分有效更新。ARCA 的运行时观测量是 adapter-enabled 与
adapter-disabled 最后一层 hidden state 的 L2 residual；在论文实现里，它复用已有 KL/reference-policy 路径所需的
一次 no-grad adapter-disabled forward，而不是显式计算 Jacobian。代价仍包括这次额外 forward、trajectory 内
normalization、两条 hidden-state 路径的一致性以及 adapter-rank coupling；错误 redistribution 会放大 verifier noise，
浓度高也不必然意味着 credit 错误。Full-rank update、短 response、uniform credit 已稳定，或 reference path 成本
不可接受时，原有 sequence/group advantage 更简单。`arXiv:2606.00257v1` 的 §3、§4 只支持作者在其 LoRA、MATH
与训练合同中的 degeneration diagnostic 和 redistribution；附录中的 softmax Jacobian 属于理论解释，不是运行时
机制。§4.8 也不证明 ARCA 可替代 outcome reward、critic 或其他模型族的 credit assignment。

<!-- source-family:SF-2026-ARXIV-2606-00257 -->

<!-- daily-20260621:train-grpo:start -->
### Reward 轨迹的可推导性、感知依赖与 decision density

对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。 multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。 多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。

**Trade-off、failure、共存与回退。** 竞赛型同生成器 testbed、LoRA 与有限模型族不建立普遍不可学习定理；catalog escape 依赖有限结构并把 search 成本移到外部。 单一模型与 video-QA task 不给出跨模型 reward 阈值；VHS 是 temporal perturbation proxy，回答正确也不证明 grounded reasoning。 推导依赖 critic error 受控与 routine turn 真正 reward-equivalent；受控环境不证明开放 agent 能可靠标出 decision turn。 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，回退到现有 deterministic owner、supported path 或人工审批。

#### Review notes

- `SF-2026-ARXIV-2606-21884` — primary `arXiv:2606.21884v1`；exact-v1 URL=`https://arxiv.org/html/2606.21884v1`；Method=`https://arxiv.org/html/2606.21884v1 — §4 Method: Solver-Grounded Synthetic CoT and the Experiment Ladder`；Evaluation=`https://arxiv.org/html/2606.21884v1 — §5 Results; §6 Anatomy of the Failures`；Non-proof=`https://arxiv.org/html/2606.21884v1 — §8.2 Threats to validity; §10 Limitations`。
- `SF-2026-ARXIV-2606-22043` — primary `arXiv:2606.22043v1`；exact-v1 URL=`https://arxiv.org/html/2606.22043v1`；Method=`https://arxiv.org/html/2606.22043v1 — §2 Setup — Task and model; Visual-hacking diagnostic (VHS); Held-out OOD evaluation; Trajectory fleet`；Evaluation=`https://arxiv.org/html/2606.22043v1 — §3 Onset is real and seed-robust; §4 Reward strength: a monotone dose–response with formation–reversal asymmetry; §5 A critical intervention window; §6 What changes inside: representation probe; Appendix A Reproducibility and diagnostic details`；Non-proof=`https://arxiv.org/html/2606.22043v1 — §8 Discussion and limitations — Limitations`。
- `SF-2026-ARXIV-2606-22164` — primary `arXiv:2606.22164v1`；exact-v1 URL=`https://arxiv.org/html/2606.22164v1`；Method=`https://arxiv.org/html/2606.22164v1 — §2 Preliminaries; §3 The Signal Dilution Problem`；Evaluation=`https://arxiv.org/html/2606.22164v1 — §4 Experimental Setup; §5 Results`；Non-proof=`https://arxiv.org/html/2606.22164v1 — §7 Discussion; Appendix A assumptions; Appendix B Diluted Doors`。
<!-- daily-20260621:train-grpo:end -->

同一 prompt、同一 role、单个 final-answer verifier 时，sequence-level reward 简洁且可复算；当 trajectory
包含多个角色、多个目标、草稿—修订阶段或可迁移中间产物时，把一个标量复制到全部 tokens 会混合不同
conditional state。演进方向不是无条件增加 reward model，而是先让样本身份跟上真正的决策边界：

```text
terminal outcome
→ role-conditioned normalization population
→ block / subgoal credit with explicit boundaries
→ draft-selection and refinement state
→ receiver-tested transfer utility
→ verifier-gated reflection and policy consolidation
```

Role-conditioned statistics 只修正不同角色 reward 分布的尺度，不解决跨角色 delayed credit；blockwise
advantage 只在 block 边界与局部目标可定义时降低 credit dilution；让第二阶段读取最佳草稿可以在固定 sample
count 下重分配探索预算，但最佳草稿由当前 policy 与 verifier 共同产生，不能当作外部新知识。Transfer reward
要求把中间结果交给独立 receiver 执行或续写，能补充 final correctness，却会把 receiver identity、能力和偏好
写进 objective。Reflection-conditioned RL 还需把 episode、lesson、retrieval 和 consolidation 分开版本化，避免
把未经验证的自我解释直接固化进 policy。

Block 粒度还会改变 baseline 应条件化的状态。后续 block 已读取具体 prefix，其 conditional value 未必等于原 prompt 的组均值；把同题 rollout 按最终正确/错误 outcome 分箱，再复用箱内统计，可以给局部 block 一个较便宜的近似 baseline，但只有 outcome 足以承载所需 prefix 条件时才有相应无偏解释。若箱内均值包含当前样本自身 reward，还会产生同组 self-inclusion bias，不能由“不新增 rollout”推导一般无偏 policy gradient。<!-- source-family:SF-2026-ARXIV-2602-10231 -->

[受限 blockwise 对照](https://arxiv.org/html/2602.10231v1)显示，confidence calibration、任务正确率和更大组的收益并不总同向；固定 batch 增加组大小还会减少独立 prompt 数。Parser/block 边界、bin 支持、局部 token reduction 与 terminal verifier 应共同版本化，稀疏箱和 outcome 不能代表 prefix value 时保留 prompt-level sequence advantage，或支付独立 continuation/critic 成本；更细 credit 不获得内容真值权限。

Search / research trajectory 还可以用最终被引用的 evidence provenance 回指最早的 `search / read` exposure，
把这一步标成 relevance candidate，再用 sign-preserving modulation 调整原有 advantage。它改善了“终局标量平均
铺给所有检索动作”的粒度，却只证明证据曾经进入可见状态，不证明该 exposure 对最终结论具有不可替代的因果贡献。
重复来源、后续改写与 judge 偏好都会污染归因；因此 terminal outcome 继续拥有 reward gate，provenance、judge、
query、document revision 与最早可见 step 必须共同版本化。无法稳定恢复 exposure lineage 时，sequence reward
加明确的检索成本仍更可复算。

检索训练还可以使用训练期特权信息构造不同于 exposure provenance 的局部信号：固定 gold answer 与原 history，比较真实检索 document/refinement 和批内其他问题的 document/refinement 所得到的长度归一 answer log-likelihood，再把处理后的差值加到 query-token credit，其余 tokens 保留终局组 advantage。这个代理测的是 gold 条件下的效用，不是检索材料的真实性、Shannon mutual information 或纯 query 的因果贡献；document 与 refinement 一起变化，随机批内也只近似匹配长度/结构分布，而非逐样本严格配对。第76章继续拥有 evidence validity，训练代理不能转为推理时事实置信度。

终局全失败时仍可能得到代理优化方向，不等于凭空获得真值；它增加 gold 依赖、多路 reference scoring、deadzone、负值衰减及 query-length 归一的控制状态，也可能给包含竞争答案的有效 query 负信号。Log soft-clipping 不是全值硬界，query-only loss 位置不隔离共享参数。`arXiv:2604.15148v1` 的 IG-Search 仅覆盖 Qwen2.5-3B/7B、E5/Wiki2018 检索与作者训练配置，Bamboogle .424 低于 GiGPO .641；同任务/样本数不是总 compute 匹配或生产 SLO 改善。缺少可靠 gold、检索分布漂移或代理与真实结果失配时，应回退终局 reward 加显式检索成本，或保留有来源的 exposure shaping，不以更密的代理覆盖真实 outcome。

<!-- source-family:SF-2026-ARXIV-2604-15148 -->

另一个文档使用代理不比较随机替代检索结果，而固定模型生成的 quote，用同一冻结 verifier 分别在有、无原 document 条件下计算 quote 的 mean-token NLL，再以无文档 NLL 为分母衡量相对改善，并对唯一 quotes 聚合。这样能让最终答案奖励之外的训练压力指向“这段文字是否更依赖文档”，却不测互信息期望、真实阅读行为或 quote 的事实正确性。无 quote、prior NLL 近零与过度追求可预测引用都需要单独处理；verifier 变大也不必更好，有限反侧中较大的 verifier 在长文本任务退步。重复条件 scoring 与较长 rollout 增加成本，代理失配时应保留终局质量验收、可追溯引用与无该辅助项的退路，不用条件 likelihood 替代 evidence grounding。<!-- source-family:SF-2026-ARXIV-2602-05758 -->

Entropy controller 是与 credit assignment 正交的 actuator：固定 clipping 容易解释，dynamic threshold 可以
在特定 token/ratio regions 调整探索—收敛轨迹，却新增 phase、band、oscillation 和跨模型校准状态。以上机制
都只能在 hard outcome gate、独立 calibration 与完整 trajectory identity 之上使用；开放研究、不可逆 action
或 verifier 脆弱时，稀疏但可信的 terminal reward 仍优于密集而错误的 proxy。

Typed Credit 之前还需要一层 **update evidence**。Aggregate KL、entropy 或 gradient norm 只能回答 policy
变化“多大”；对同一 prefix 比较 base 与 RL policy 的 signed `Delta log p` 或完整 token-distribution divergence，
才能描述变化朝哪个方向发生。若再做 forward/reverse cross-sampling，只在高差异位置替换 distribution，才
能检验少量 token 是否对结果具有功能作用：

```text
aggregate update magnitude
→ same-prefix signed direction / divergence
→ bounded token intervention
→ outcome change under an explicit budget
```

这条 evidence ladder 不等于新的默认 objective。它需要成对 checkpoints、两套 distributions、prefix 与
sampling seed；替换 token 后 prefix 已改变，后续 attribution 也不再是 fixed-context。用低概率或高 divergence
token 重加权 advantage 还可能放大 verifier noise。缺少 paired policy 或干预成本过高时，标准 sequence-level
advantage 仍更可靠；受控 RLVR 结果也不证明 policy 从不产生新能力或某个 threshold 是通用常数。

决策边界还可能位于 role、turn 或 modality，而不只是 token。Multi-Agent 可用 leave-one-role-out outcome
构造有界 counterfactual credit，但它增加 verifier calls，并在贡献不可分或循环 topology 中失去清晰 baseline；
shared team reward 在这些场景仍合理。视觉生成的 text-token 与 flow/action block 也不能不加区分地共享
normalization：joint trajectory 可以复用 outcome gate，却应保留 modality-specific probability coordinate、
mask 与 credit scale。Perception/exploration token 的局部 reward 同样只能是辅助信号，不能越过终局 correctness。

固定 ratio clip 本身也是一种低成本 trust-region 近似。它在旧 policy 与 current policy 接近、action probability 不极端时清晰可靠；但统一 ratio 区间映射回 probability simplex 后，对低概率与高概率 token 的实际可移动距离不同。概率高度不均匀、又需要保护长尾探索时，可以由旧 action probability、divergence family 与 radius 计算 token-specific feasible band：

```text
old categorical policy + sampled action
-> chosen divergence and radius
-> feasible probability interval
-> action-specific ratio bounds
-> clipped policy update
```

这更直接表达 distributional trust region，却增加每 token 求解、近似误差、kernel 成本和新的 `delta` 校准。它也不产生更可靠的 reward；verifier 错误、advantage bias 和 support mismatch 仍在更上游。固定 clip 在开销、可解释性和成熟实现优先时继续成立，probability-aware band 只是一种条件分支，不是对 PPO/GRPO clipping 的全面替代。

Hard mask 与 smooth constraint 还代表不同的纠错语义。越界后直接丢弃样本最容易形成明确边界，却会让
本可纠正的 trajectory 完全失去梯度；无界 importance weight 保留信号，却可能被极端 ratio 放大。Binary-TV
一类连续约束尝试在越界后仍提供有界纠正信号：它改变的是 trust-region actuator，不会修复 reward、reference
policy 或 estimator bias。DRPO 的作者实验只覆盖其 math/RLVR 与采样合同，因此这里保留机制分支，不宣称其
普遍优于 clipping。

长 trajectory 的 credit 也可以从“整条 response 一个 advantage”演进到共享前缀后的受控反事实比较：在候选
decision point 分叉，固定 prefix 与 environment snapshot，比较不同 action 的未来 outcome，再把差异归给该
branch。它能缩短 credit path，却需要 replayable environment、branch identity、matched budget 与独立 verifier；
分叉点选择、相关样本和额外 rollout compute 又成为新偏差。APPO 为这一机制提供实验性案例，但稳定 terminal
reward、短 trajectory 或环境不可复放时，sequence/group advantage 仍更可靠。

Typed Credit 还要警惕把 **hindsight relevance** 误称为 causal credit。终局结果可以重新条件化每一步 action 的评分，再与 trajectory-level advantage 组合；这可能在长轨迹中区分关键与偶然步骤，但同源模型的 posterior、跨 state normalization、future-information leakage 与 smoothing 都会引入 bias。没有 action intervention 或可校准 behavior denominator 时，它只是 outcome-conditioned relevance proxy，不能证明某一步造成了成功。短轨迹、廉价可靠的 terminal verifier 或 critic 不可信时，coarse sequence credit 仍可能更稳健。

最后，max response length、truncation mask、temperature、KL/clip 与 verifier 会共同塑造 policy 能探索的 trajectory。把所有截断样本删除可避免学习不完整答案，却也可能让“尚未写完但可能正确”的路径完全失去信号；条件保留能降低这种偏差，又可能屏蔽真正错误的长输出。长度和 entropy 只能是 curriculum state，不能成为能力代理。可靠实现应按 outcome/length slice 记录 mask rule、RNG、policy/version、token budget 与 verifier verdict，并用 expected value per token、tail cost 和 reward-hacking canary 判断是否值得延长探索。

这个 canary 也不能只检查某一个看起来安全的 checkpoint。如果 policy 能改写评价器，早期作弊失败后转向正常解题，并不代表攻击路径已经消失；当正常解题能提供的有效奖励不足时，它还可能学会更容易成功的评价器改写，再次转向 hacking。应沿训练过程分开记录作弊尝试、作弊成功、真实解题成功与进入更新的有效样本，而不能把暂时降低的 hacking rate 当作持续安全证明。[受控的 coding 环境实验](https://arxiv.org/html/2604.01476v1#S2)还观察到限制正确 rollout 进入梯度更新的数量会加速反弹；这是特定奖励与权限设置下的证据，不意味着所有 RL 都遵循同一阶段顺序。

用内部 shortcut probe 对 reward 作折扣可以是一条辅助训练分支，但 probe 仍是可漂移的相关信号，不拥有真实正确性。若在组内归一化之前修改 reward，改变的是整组 advantage 的比较基准，不能把同一惩罚随意移到归一化之后；它也可能压制合法捷径或诱导 policy 隐藏 probe 特征。上述实验仍有非零 hacking，且 rollout score 与 prompt-position activation 的实现描述存在未决细节，因此不能据此承诺通用防御。可靠 verifier、评价器写权限隔离及跨 checkpoint 独立验收仍不可由 probe 替代。
<!-- source-family:SF-2026-ARXIV-2604-01476 -->

短窗本身也会塑造训练行为，而不只是长度 reward 的实现参数。把原正确回答截去末答会让 verifier 判失败，于是某些失败组含有尚未完成的有效步骤。一个受限 update 分支按 outcome 分开 mask：正确 rollout 中低 confidence 步骤不承受正 advantage，失败 rollout 中高 confidence 步骤不承受负 advantage；其余步骤仍用原信号。这是在两种错误 credit 风险之间作选择，不是 confidence 已经获得过程正确性。<!-- source-family:SF-2026-ARXIV-2604-24003 -->

[exact-v1 §2.2–2.3/§4](https://arxiv.org/html/2604.24003v1)的人工截断约 29% 使原正确回答变 verifier-failed，只说明该预算的混杂；confidence 与 PRM 排序接近也不证明概率校准或语义真值。训练 wall-clock 约增 17%，两种 mask 的消融和任务反向须与长度/token 预算一起比较。Probe 不稳、错误真实来自过程或 mask 降低关键切片质量时，回退统一 outcome advantage、明确 truncation admission 或可靠过程监督，不以短回答自动判更高效。

还可保持 action 不变，只比较支撑它的思考深度：在 verifier 判成功的交互步骤中，固定 observation/history 与原 action，重新生成若干深度的 thinking，再读取同一 action 在各 thinking 条件下的平均 log-probability。将这些读数在组内标准化并作 softmax，用所得权重重分配原 trajectory advantage；失败轨迹不作这种扩展。这不同于改 action 后比较未来 outcome，也不同于把 confidence 当正确性标签：它只提出“同一成功 action 与哪种思考条件更兼容”的更新分支，不能证明某段 thinking 因果必要或低深度在所有状态都足够。<!-- source-family:SF-2026-ARXIV-2602-12662 -->

权重和为一也不保证总梯度幅值守恒：扩展后的成功样本包含不同长度的 thinking，token 分母、条件分布与失败样本人口都可能改变。应保存原成功 verdict、固定 action、各级生成与评分身份，分别验收成功率、thinking tokens 和完整生成/scoring 费用；[受限离散 Agent 对照](https://arxiv.org/html/2602.12662v1)中，最高成功率分支不是最短输出，失败也参与 confidence 扩展有反退。成功支持集不足、动作概率受措辞影响或扩展费用不合算时，普通 outcome-only GRPO、固定深度与可信过程监督仍是回退，不用概率读数给 reasoning 签发真值。

### Partial Rollout：减少 Straggler，也把 Trajectory 变成持久状态

同步等待每条长 CoT 完成，语义最清楚，却会让极长 response 阻塞整个 batch。一个实验性分支
是把 rollout 按 token budget 切成 segments：当前 segment 用当前 policy 继续生成，未完成
trajectory 连同 prefix、policy version 和 reward context 写入 replay buffer，后续再恢复。

它把一次性 sample 演进成有生命周期的训练对象：

```text
trajectory_id
+ prompt / environment identity
+ completed prefix and masks
+ generating policy version
+ segment boundaries
+ reward / terminal status
```

收益是降低 length-tail straggler、提高 rollout/training 资源重叠；新增问题是 historical prefix
staleness、segment credit assignment、buffer recovery、loss masking 和 on-policy 边界。严格 on-policy
objective、短 rollout 或恢复语义尚不可靠时，完整同步 trajectory 仍是更安全的旧方案。Kimi k1.5
公开系统提供了这条 state lifecycle 的具体证据，但没有证明任意 objective 下复用 partial history
都无偏，也没有给出可直接外推的集群成本结论。

### 从 Opaque Harness Call 到可训练 Trajectory Tree

White-box Agent loop 直接拥有 observation、action、tool result 与 trajectory，最容易定义 mask、reward 和
policy ratio。成熟 harness 则会自行重试无效调用、压缩 Context、启动 subagent，并重新序列化模型输出；只抓
最终 transcript 会把原始 sampling tokens、被替换的调用和 branch identity 混在一起。

一种中间路线是不侵入 harness control flow，而在 model-serving boundary 保存不可变 call evidence：

```text
isolated task environment + opaque harness
→ serving proxy captures exact input/output tokens and rollout logprobs
→ longest-prefix matching reconstructs a call tree
→ remove retry dead leaves and unrelated auxiliary branches
→ count shared prefix tokens once
→ PPO / GRPO consumes retained branches under rollout-level reward
```

这里有两个不能合并的视图。Harness 消费 decoded/structured text 来驱动工具和环境；训练器必须消费 inference
engine 实际 sampled tokens，不能把 harness 重新格式化后的文本再次 tokenize 后冒充原 trajectory。Serving proxy
因此拥有 model-call evidence，不拥有 tool semantics；verifier 拥有最终 workspace verdict，不拥有每个 branch 的
局部 credit；trainer 才拥有 mask、advantage 与 parameter update。

Tree reconstruction 减少 shared-prefix 重复训练，也允许复用无法修改的成熟 harness，却没有自动解决 credit
assignment。Retry 产生的 dead leaf 可以删除；subagent、Context compaction 和 sibling branch 若共享同一个 terminal
reward，贡献仍可能不可辨认。简单地把 rollout reward 广播到全部 paths 会引入 bias，PPO 对 forked state 的 value
backup 也可能需要额外假设。ClawGym II 的作者实验只证明这种 capture/reconstruction 在两种 harness、指定模型和
受控 verifier 下可训练；硬件、完整 lifecycle cost 与生产 SLO 未披露，不能把其 benchmark 增益写成通用结论。

因此每个 black-box sample 还必须绑定：

```text
harness / proxy / tokenizer / policy revisions
+ task workspace and verifier identity
+ call / retry / compaction / subagent branch lineage
+ exact sampled tokens, logprobs and train-time correction
```

Harness 少、trajectory 短或需要逐 action causal credit 时，white-box loop 仍更可靠；只有 harness 复用价值足以覆盖
proxy schema、tree corruption、reward attribution 与 train/serve mismatch 时，black-box bridge 才值得引入。下一阶段
压力不是捕获更多 calls，而是为 auxiliary branches 建立可验证的 marginal contribution 与独立 reward boundary。

### Cross-Policy Rollout Reuse：共享 Experience，不共享概率坐标

标准 GRPO/GSPO 让每批 trajectories 来自一个明确的 rollout policy。这个约束看似浪费——另一个 policy
已经为同类 prompt 生成并验证了答案，为何不能直接复用？但 rollout 不只是文本；它还是某个 source
policy 在特定 tokenizer 与版本下产生的概率样本。跨策略复用必须保留：

```text
trajectory / prompt / reward / verifier identity
+ source policy id and checkpoint version
+ source tokenizer and tokenization
+ source log-probability coordinates
+ target retokenization and target log-probability
+ generation time / staleness
+ reuse count and clipping decision
```

一个可行的数据流是：多个异构 policies 各自产生 source-tagged rollouts，组成联合 experience batch；每个
target policy 用自己的 tokenizer 重新表示文本、重算 target log-probability，再依据 source/target capability
或 sample value 调整 advantage，最后在 bounded ratio/clipping 下更新各自 checkpoint。收益是复用昂贵的
generation 与 verifier work，并让一个 policy 看见另一个 policy 覆盖到的 modes；代价是同时维护多套
weights、optimizer、tokenizer、logprob 与 rollout workers，还要处理 support mismatch、staleness 和共享
verifier error。

这里不能把跨 tokenizer 的 sequence likelihood ratio 伪装成严格的 token-wise importance ratio。两种
tokenizer 对同一字符串使用不同的事件分解，token positions 也不一一对应；重新 tokenization 能让 target
计算自己的 likelihood，却不会自动恢复 source policy 在 target 坐标下的逐 token 行为概率。Capability
adjustment 若依赖未知的 oracle ratio，只能给出条件理论；实际系统用 finite-batch estimate、normalization
和 clipping 后，本来就有意接受 bias 来换取 bounded update。分母接近零、源策略几乎无成功样本或两者
support 差异过大时，权重还可能爆炸、饱和或把噪声放大。

因此这条路线不是“更多 policy 必然更好”，也不是推理时的 Multi-Agent cooperation。它发生在 training
experience plane：policies 可以共享经过来源标注的 evidence，但仍独立更新和部署。单策略 on-policy
rollout 在需要最清楚的 objective、较低系统复杂度或 verifier 便宜时继续成立；one-way distillation 适合
只想把强 policy 行为迁给弱 policy；offline replay 适合允许更大 policy lag 的目标。Cross-policy reuse 只在
额外覆盖与 verifier 复用足以抵消双份 runtime/state、且 provenance 与 bias 可观测时才值得采用。

### Inference-time Controller 是训练分布的一部分

固定 controller 下训练 policy，在 Serving protocol 稳定、tool/scaffold 不变时最容易维持 on-policy 语义；但当
推理阶段会组合 calculator、retriever、self-consistency、reflection 或其他 controller，模型实际面对的不再是单一
action protocol。只把 controller 留到上线时外挂，会产生 train–serve mismatch。一个条件化分支是把 controller
identity 与 trajectory 一起进入 rollout distribution：

```text
task + policy revision
→ sample controller / module composition
→ controller-mediated multi-turn trajectory
→ turn-level reward / advantage
→ controller-tagged GRPO update
→ held-out composition and protocol-shift evaluation
```

Controller 不是外部噪声，而是决定 observation、可用 action、turn boundary 与 credit assignment 的环境版本。
每条样本至少绑定 controller vocabulary、composition、implementation revision、tool schema、policy checkpoint、
reward/verifier 与 turn lineage；Serving 只有使用兼容 protocol，训练收益才可迁移。多 controller exposure 可能提高
对已测组合的鲁棒性，却增加 rollout cost、group variance、稀疏 credit、protocol-version coupling 和 negative transfer；
某些 controller 还会把同一能力切成不同长度与 reward density。

现有证据只支持所披露的 Llama-3.2-3B、数学任务与十二种 controller/composition，不证明 controller-agnostic 或
跨任务 cooperation。协议固定、额外 controller 没有生产价值、或需要最清晰 objective 时，单 controller on-policy
训练仍更好；controller 快速变化时，还应优先版本化和兼容性测试，而不是无限扩大训练 mixture。

Agentic coding 又把 policy identity 扩展到 environment、tool schema、scaffold、turn boundary 与 verifier。
一种演进先在不同 domain/scaffold 中分别优化 experts，再让统一 student 在自己访问到的 states 上接受对应
expert 的 log-probability supervision；这能降低 online routing 成本，却新增 teacher selection、specialist
forgetting 与 cross-domain interference。长 trajectory 还可按 turn 而非整条 sequence 聚合 ratio，或把共享
prefix 的 tree paths 编进同一 attention graph；前者依赖稳定 scaffold markers，后者依赖 mask、position、
loss weight 与 kernel correctness。重复多次 forward 估计 MoE log-probability 可以降方差，却以额外 compute
换取估计稳定。

因此可执行的 Agent RL sample 至少应绑定：

```text
policy / tokenizer / precision graph
+ environment / tools / scaffold
+ task / verifier
+ turn and branch identity
+ source expert or rollout policy
```

单一 mixed policy、sequence-level ratio 与逐条 root-to-leaf training 在 domain 少、轨迹短、分支稀疏或
可审计性优先时仍是更小的方案。厂商报告只能证明其整体 pipeline 在披露 harness 下可运行，不能把某个
benchmark、倍数或未拆分组件写成通用因果结论。

多任务训练还需区分“采样 mixture”与“实际 gradient mixture”。某些 task 的 group rewards 更常全相同，经过 zero-gradient filtering 后，即使原始 prompts 等比例采样，optimizer 看到的有效任务权重也会偏移。控制回路因此应记录：

```text
target task utility / weight
→ prompt sampling
→ task-specific zero-gradient and verifier acceptance rate
→ effective gradient-bearing counts
→ bounded resampling / weight update
```

Worst-task 或 improvement-aware weighting 可避免强任务掩盖弱任务，却可能牺牲平均能力、放大 noisy verifier 并增加 straggler。Uniform mixture 在任务同质、过滤率相近或产品目标本就按平均效用定义时仍更简单。类似地，sequence-level objective 的 token normalization 会改变长短 trajectory 的实际权重；消除短答偏置不能被解释成“越长越好”，还必须约束 verbosity、token budget 与 tail latency。

多任务 RL 把所有任务按固定 curriculum 和统一 KL 训练，容易让已饱和任务继续占预算、弱任务又受同一 trust region 约束。更完整的 controller 以版本化 task utility 同时驱动训练预算/样本调度与 per-task KL；两者必须共享同一观测窗口和 policy revision，避免一边改变分布、一边用过期 calibration。utility 不稳定或跨任务迁移为负时回退固定 mixture、任务级 floor 或独立 specialist。

证据只覆盖两个 LLM、四类代码任务与作者的 utility 定义；9.0–9.5%/7.5–12.8% 相对结果不证明其他任务、并发 rollout 或生产成本。 TRAIN-DATA 可提供 mixture identity；TRAIN-GRPO 拥有 runtime curriculum/KL controller。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06111 -->

### 多 Reward 聚合不能掩盖 Channel Collapse

把多个 reward 直接求和或加权，在通道尺度稳定、目标一致时最简单；RLIF 中各 channel 的稀疏度、噪声和梯度方向可能不同，平均值上升仍可能伴随某一关键能力退化。Aggregator 因而只能形成 update proposal，训练控制面还需监控 per-channel coverage、collapse、gradient conflict 与 held-out behavior；单通道 guardrail 拥有否决权。

这种约束避免强信号吞没弱信号，却增加 reward calibration、冲突处理和样本成本；目标单一时保留单 reward 更可解释。arXiv:2605.22620v1 的方法与实验只支持论文定义的多 reward 设置，不证明任意 reward 组合都能通过同一聚合器得到 Pareto 改善。

<!-- source-family:SF-2026-ARXIV-2605-22620 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20722:start -->
组内统计还可用来提出自适应 clip 与 sampling temperature：reward dispersion 变小时扩大探索，update 风险变高时
收紧 clip。该 controller 只拥有 exploration / update proposal，不拥有 reward correctness；统计噪声、all-equal
group 或分布漂移会让反馈回路振荡。作者设置之外，应由 KL、held-out retention 与 per-channel guardrail 提交
checkpoint；校准失败时回退固定 temperature、固定 clip 或分阶段调参。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20722:end -->

若温度本身由可训练 head 逐 token 选择，控制动作就不能藏在普通 token ratio 之外：保存 keep/reset 决策、reset 时的抽样变量、实际温度及生成 token，并分别计算控制 law 与该温度条件下的 token likelihood。Keep 分支不把未实际使用的 Beta 密度当成当前温度概率；[分层控温的受限方法](https://arxiv.org/html/2602.13035v1)给出了这一联合动作接口，而非更可靠的难度或正确性探测。交替冻结温度 head 仍不冻结随 policy 参数变化的 hidden context，shared advantage、两个 clipping 目标与采样人口仍耦合，不能授整体无偏或一般收敛。部分任务与固定温度对照反退，head、保存/scoring、训练和 decode 成本须合并；信号失配或收益不足时，保留固定温度及上段外部统计 controller，不把小 head 当成免费探索或全任务胜出。 <!-- source-family:SF-2026-ARXIV-2602-13035 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-21467:start -->
RLVR update 也可从 discriminator 视角理解：policy-gradient 方向在 token-gradient vectors 上形成一个线性分界，
决定哪些 token probability 被推高或压低。这个视角能暴露 aggregate reward 下真正收到 credit 的 token，却只是
局部更新诊断，不证明分界对应语义正确或因果步骤。它需要额外 gradient probe，并受 tokenizer、batch 和模型状态
影响；方向不稳或与 outcome slice 冲突时，应回退常规 advantage、逐 token credit 检查和独立 verifier。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-21467:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-19577:start -->
当一个 batch 混合 EM、F1、NDCG、ROUGE-L 等异构任务时，per-prompt normalization 仍在比较不可比尺度；强任务的稳定 reward 会掩盖弱任务的学习压力。一个条件分支先用 task-level RMS 对齐数值尺度，再以平滑 pass-rate 调节 difficulty weight，并把 task taxonomy、reward identity 与 policy revision 共同冻结。它解决的是跨任务 credit coordinate，不证明这些指标已经成为真实 outcome。

该分支新增任务划分、历史 pass-rate、难度权重和合成数据偏差；样本不足、metric 语义不可比或分布漂移时，归一化会制造虚假公平。此时应回退 task-specific GRPO、单任务 batch 或不做跨任务聚合。现有证据只覆盖 23K 样本、九类长上下文任务、Qwen3 4B/30B 与作者 benchmark，不能外推 taxonomy 完备性或跨模型阈值稳定性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-19577:end -->

#### 独立归一化也不能消除语音 Reward Channel 的相互侵蚀

在全双工语音 policy 中，timing、continuity、transcript quality 与 waveform integrity 具有不同尺度，逐通道 group normalization 可以防止数值尺度直接吞噬，却不能保证一个通道改善时其他行为不退化；组内常量通道甚至不产生有效 advantage。训练控制面因此必须保存 per-channel reward 与 coverage，同时把空输出、turn/overlap、semantic task、noise/backchannel continuation 和 takeover latency 组成 retention matrix；任何关键行为 guardrail 都可以否决总 reward 上升的 checkpoint。

Credit 的 action space 也必须显式声明：若 policy loss 只施加在包含 timing/padding token 的 text stream，而 audio codebook action 不直接承受梯度，文本 judge 的改善不能被解释为完整音频控制 credit。Continuity reward 可以阻止用极短或空回答骗取 promptness，却可能诱发冗长、延迟让权或对 backchannel 过度反应。交互模式单一或多通道校准不足时，应回退单一可解释 reward、分阶段优化或冻结已通过的 channel。exact-v1 结果只覆盖英语、固定 reference clips、作者 judge 与受测 checkpoint；它展示了 channel interference 和约 40 ms 的 takeover-latency 代价，但不提供生产延迟分布、广泛 speaker/domain 或部署安全保证。

<!-- source-family:SF-2026-ARXIV-2609-12623 -->

## 关键诊断指标

除 PPO 常见 ratio、KL 和 clip fraction 外，还应观测：

- Reward mean/std 与 per-prompt group variance。
- All-equal reward group ratio。
- Positive/negative/zero advantage 比例。
- 每个 prompt 的有效 completions 数。
- Response length 与 reward correlation。
- Verifier failure/timeout rate。
- Rollout tokens per optimizer update。
- Policy lag 与 sample reuse epochs。
- Per-source policy sample share、support mismatch 与 cross-policy clipping fraction。
- Retokenization failure、near-zero capability denominator 与 source-age distribution。

若 reward std 接近 0，大量 GPU 生成的 samples 可能几乎不贡献 policy gradient。

但“熵仍高”也不能证明 policy 仍在响应不同输入。多轮 Agent RL 可能对每个 prompt 生成表面多样的轨迹，
却逐渐收敛到跨输入复用的 reasoning template。训练监控因此要把同一输入内的 variability 与跨输入的
distinguishability 分开：

```text
conditional entropy H(Z|X)
+ input dependence I(X;Z) or a declared proxy
+ prompt-group reward variance
+ held-out task success and coverage
```

真实 mutual information 往往不可解；batch 内 cross-scoring、retrieval accuracy 或 z-score 只是额外 forward
得到的 diagnostic，不是 faithful reasoning 或 correctness 证明。Reward-variance filtering 可以少更新 all-equal
groups，却会把原 objective 改成 filtered objective，并可能偏向 noisy high-variance verifier、永久丢掉已掌握或
极难 prompts。RAGEN-2 的实验性结果支持“健康 entropy 可能漏报 input-agnostic collapse”这一诊断缺口，不支持
固定阈值或把 MI proxy 设成 release gate。可靠控制器还要保留 curriculum/replay 让被过滤任务重新进入，并用
独立 verifier、held-out prompts 与目标分布监控 bias。

Online Agent RL 又把样本生命周期从 batch 扩成持续 feedback stream。User reply、tool result、GUI transition
和 test verdict 到达时间不同，也可能包含隐私或攻击内容；不能因为它们都叫 next state 就直接写入更新：

```text
serving policy version + authorized session state
-> typed feedback and process/outcome judgment
-> quarantine / deduplicate / consent and deletion checks
-> training buffer with policy and environment lineage
-> update, canary and rollback
```

Serving、environment、judge 与 trainer 是四个独立 owner；directive hint 可以构造 teacher signal，evaluative
feedback 可以形成 reward，但二者不能互相冒充事实。异步闭环提高 credit density，却引入 judge error、policy
skew、privacy、poisoning 和跨用户污染。Offline curated RL 在合规、复算和 verifier 稳定性优先时仍是正确旧
分支；在线更新只有在 consent、quarantine、version barrier、delete propagation 与 rollback 都可验证时成立。

## 与 PPO、DPO 的边界

```text
PPO
  learned critic baseline
  on-policy rollouts
  clipped ratio

GRPO
  group-relative baseline
  grouped on-policy rollouts
  clipped ratio

DPO
  offline preference pairs
  no rollout in update loop
  no learned critic
```

GRPO 仍属于 policy optimization，不应因为没有 critic 就被描述成 supervised pair loss。DPO 则不需要从当前 policy 为每个 update 生成一组 responses。

### 从序列 Reward 到受约束的 Token Credit

把同一个序列 advantage 广播到所有 token，在轨迹短、关键步骤不稀疏时简单且稳定；长推理会让真正改变结果的少数 token 与大量过渡 token 获得相同更新。一个条件分支是用当前策略与参考策略的有界分布距离形成 token 权重，再用 entropy gate 抑制“罕见但自信的错误偏离”，同时保持序列总 advantage 的尺度。它减少了 credit dilution，却没有证明 entropy 等于语义正确，也引入参考分布计算、温度校准和错误归因；因此它只能作为 reward redistribution proposal，最终正确性仍由 outcome/verifier contract 拥有，普通短轨迹仍可保留序列级更新。[受限证据：arXiv:2605.03327v1]

<!-- source-family:SF-2026-ARXIV-2605-03327 -->

还有一种折中不为每个 token 都采样 continuation，而只在一个早期 prefix 上购买一组条件完成：下游结果的平均值评价这个 prefix 是否让后续更容易解出，组内相对结果继续更新下游策略。因为每题最终只选一个上游 prefix，上游不能直接复用下游的空间 group baseline；可使用随 policy 漂移衰减的每题历史 baseline，形成两个不同的信用坐标。将 prefix 和原问题一起送入下游，保留绕过错误草稿的机会，却也使测到的效用属于这条重排后的条件接口，不是原始 token 的纯因果信用。<!-- source-family:SF-2026-ARXIV-2604-08690 -->

只靠“共享 prefix”不保证成本相同。一个实现先并行生成多个短段，再按平均负 log-probability 的中位偏差选一段，重定向各分支的 KV 指针，并为重排后的输入重新计算必要 KV，避免两次串行 GPU dispatch。代价是 rollout engine 的暂停/重排支持、discarded-prefix 工作、历史 baseline 漂移与有限 continuation 的符号噪声；KV 共享必须保存真实条件序列身份。[作者消融](https://arxiv.org/html/2604.08690v1)支持 skip、Monte Carlo 和选择规则在所测数学任务上的联合价值，但外部强模型对正确轨迹的续写诊断不是 learner 内部因果归因，sample count 对齐也不等于所有设备的 wall-clock 等价。预算小、prefix 无法合法复制或历史 tracker 不稳时，普通 outcome-broadcast GRPO 仍是明确的基线。

### Exploration 必须与 Verified Progress 对齐

把 entropy 当成统一奖励会鼓励无方向随机性，但 entropy 本身也不能证明 reasoning 正在变正确。一条实验性分支先用
组内 outcome advantage 保留正确性的正负方向，再让高 entropy token 获得更大的 outcome-advantage 幅度；随后以
`log pi_current - log pi_ref` 构造 **implicit progress proxy**，按 outcome 符号决定方向，并依据一条 trajectory 的累计
entropy 比例而不是绝对 token 位置划分 logical-progress buckets。在桶内标准化 proxy 后，它才作为小尺度的 token-level
修正项与 outcome advantage 合并：

```text
verified outcome direction
+ entropy-gated outcome magnitude
+ bucket-normalized policy/reference divergence proxy
-> token credit proposal
```

这里 verifier 只拥有终局 outcome；policy/reference divergence 只是自监督 proxy，不是 verified per-step correctness。
当组内 reward 方差非零时，proxy direction 使用 outcome advantage 的符号；方差为零时，论文改用
`sign(reward - reward_threshold)`，二值奖励阈值为 `0.5`，因此 outcome advantage 虽为零，progress 项仍可能产生更新。
这个退化分支不是逐步正确性保证：它把阈值、frozen reference、bucket statistics 与缩放系数都引入 objective identity，
而论文的理论分析主要依赖非零 reward 方差和由 old policy 固定的桶统计。若 proxy 与 outcome 冲突、零方差分支未被
独立验证或统计不足，本书的工程建议是回退普通 outcome-only GRPO；不能把 entropy 或 policy confidence 当成过程真值。
EP-GRPO 的证据仅覆盖作者的数学 reasoning 设置，不证明这一组合适用于所有 Agent RL。

<!-- source-family:SF-EP-GRPO-ENTROPY-PROGRESS-ALIGNED-GROUP-RELATIVE-POLICY-OPTIMIZATION-WITH -->

Binary reward 的相邻问题不是怎样重新解释 token entropy，而是怎样让 rollout 停留在可比较的 pass-rate 区域。固定
题目分布和 fresh group 在中等难度时最清楚；一组 `N=8` 全错或全对时没有可用边界，controller 直接过滤；`3–5/8`
按普通组训练。只有 `1–2/8` 的困难题保存成功 trajectory，`6–7/8` 的简单题保存失败 trajectory，再按每个难度桶的
prefix ratio 截取旧 response，把旧 assistant prefix 的 loss mask 设为零，由 **current policy** 从该点生成新
continuation。新结果的 pass-rate 通过 EMA 反馈调节 prefix 长度，使采样向中间区域移动。

这不是恢复一份完整 sandbox snapshot。Agent 场景需要把保存 response 重新送入原 action parser 与 environment executor，
重建 code、history 和 tool outputs；到截断点以后才由当前 policy 接管并获得 advantage。它因此依赖可重放、近似确定的
工具环境，以及保存 trajectory、环境版本、prefix boundary、mask 和 current-policy identity。环境不可复算、外部动作
不可逆或 replay drift 无法量化时，继续使用 fresh group、curriculum sampling 或静态题目分布更可靠。论文中的二值奖励
结果只支持所测 Qwen3 模型和实现；它没有证明目标 pass rate、prefix controller 或加速数字能跨任务外推。

<!-- source-family:SF-ROLLOUT-PASS-RATE-CONTROL-STEERING-BINARY-REWARD-RL-TOWARD-ITS-MOST-INFO -->

训练继续推进后，diversity 收缩还可能来自题目被当前策略逐渐“吃完”，而不是采样温度本身过低：几乎全对的组不再提供区分方向，几乎全错的组也没有可比较的成功边界。继续在两端样本上重复 rollout 会把计算集中到已经饱和或尚不可学的区域。因而 admission controller 可以用滚动成功率、zero-success 比例和 boundary contribution 把预算移向仍有混合结果的题目，同时保留少量探针监测能力边界是否移动。

这不是永久删除困难题。有限 rollout 会把“尚未观察到成功”误判成不可学，动态过滤也会改变训练分布并隐藏能力退化；必须记录估计窗口、采样预算和重新准入条件。固定题目分布在规模小、比较实验要求严格或成功率估计不稳定时仍更可靠。相关作者实验支持 problem saturation 与过训练可以解释其 RLVR diversity collapse，不证明所有 collapse 都应由 curriculum gate 解决。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15455 -->

#### Policy-level Explorer 只拥有 Proposal，不拥有 Update Truth

提高 temperature 或注入 token-level noise 是扩大 rollout diversity 的直接旧路径；当 step-wise noise 破坏长链一致性时，
可以让较小 policy 提供结构不同但内部连贯的 trajectory proposal，再由较大 target policy 与同一 verifier 评分、归一化并
提交 update。变化不在于“小模型教大模型正确答案”，而在于 rollout 的 proposal identity 从单一 policy 扩展为混合来源：
每条 trajectory 必须绑定 proposer checkpoint、target/reference policy、sampling budget 与 annealing phase，target trainer
仍拥有最终 gradient，verifier 仍拥有 outcome gate。

小模型降低 proposal compute 并可能增加 policy-level diversity，却引入 support mismatch、off-policy bias、弱 proposer
质量上限和 schedule 状态；纯小模型 rollout 还可能让 target 长期停留在过时 support。因而应限制混合比例、监控
importance/compatibility，并逐步回到 target-owned rollout；若一致性或收益不成立，回退普通 target sampling。`arXiv:2605.30789v1`
的 §3、§4 只支持作者披露模型、任务和 progressive transition 下的 S2L-PO 结果；Limitations 不证明小模型天然适合作为
所有 GRPO workload 的 explorer，也不改变 on-policy 与独立 verifier 要求。

<!-- source-family:SF-2026-ARXIV-2605-30789 -->

### Verifiable Reward 不等于每个样本都可学习

RLVR 把答案是否通过 verifier 变成稳定 reward，在任务分布与当前 policy 有足够交集时简单有效；某些样本即使 reward 可计算，也可能没有与其余数据一致、可泛化的 policy-gradient direction。训练 admission 因而应把“可验证”与“当前可学习”分开，通过跨样本 gradient/representation evidence 识别孤立方向。

过滤能减少无效更新，却可能删掉真正新颖但稀有的能力，并增加 gradient probe 成本。低相似不等于永远不可学习；curriculum、数据重写或模型阶段变化后应重新评估。数据量小、probe 不稳定时，保留样本并降低权重或转人工分析，比永久删除更稳健。

<!-- source-family:SF-2026-ARXIV-2605-16787 -->


#### Entropy Flow 必须在严格 On-policy 边界内治理

固定 entropy bonus 把所有 token 的探索压力统一增加，在早期策略和任务同质时简单；RLVR 训练后期的 entropy collapse 可能来自 entropy-increasing 与 entropy-decreasing token update flow 失衡。控制器可以观测两类 flow，在当前 policy 的样本上调节更新权重；它拥有优化 proposal，而 verifier reward 与 policy update 语义不能被离线样本静默改写。

定向调节能保留部分探索，却新增 token 分类噪声、额外统计和策略振荡；过强的 entropy-increasing 更新也会牺牲可验证正确率。样本少、估计不稳或严格复现更重要时，固定正则与早停仍是回退。`arXiv:2605.11491v1` 的 §3–§6 与文末 Limitations 只支持作者 RLVR 设置，不证明该 flow 分解适用于 off-policy pipeline 或所有奖励结构。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11491 -->

### Tool Feedback 只能密化已有接口信息

Step-level credit 不能只由 judge 对自然语言轨迹评分。至少要在可重置环境中实际 replay 所声称的 action，并用 shuffled 或 counterfactual control 检查 reward 是否依赖正确步骤而非位置、长度或模板。执行验证增加环境成本且仍受 simulator fidelity 限制；不可重放副作用应使用 receipt 或人工审计，而不是伪造 control。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19760 -->

Outcome-only RLVR 在工具任务早期有效，因为最终答案可验证；当 policy 学会 exploit 稀疏信号后，训练可能先升后塌。把 tool error、observation 与 intermediate verifier 写入 token/step credit 可以提前暴露失败，但 feedback owner 只能传播接口已经提供的信息，不能凭 reward densification 修复含糊 schema 或不可观测状态。收益是更短的 credit path，代价是工具日志耦合和 shaping bias；反馈被 hack 或与目标冲突时，应回退 outcome gate、修复 interface，再逐步恢复 dense reward。exact-v1 只支持 Freebase/CWQ、Qwen-7B、四 seed 与 oracle ablation，不证明所有工具环境都能避免 collapse。<!-- source-family:SF-2026-ARXIV-2605-26037 -->

重复执行多轮工具环境十分昂贵时，缓存成功轨迹或工具结果可以作为训练期的受限 experience service；但 cache hit 不是一次真实 environment transition。精确命中、模糊命中和缺失命中应成为不同 observation tier，缓存生成版本与当前 policy 必须进入 trajectory identity，来自缓存的 tool-return tokens 也必须从 policy-action mask 中排除。否则训练会把旧环境反馈、检索近似或缓存文本误当成当前策略产生的动作。

缓存能降低 rollout 成本，却会改变 policy 所见的环境分布，并引入 staleness、模糊匹配误归因和 reward scale 漂移。训练应分别报告各 cache tier 的命中率、真实性能与无缓存回放结果；高风险、有副作用或强时效工具仍应 live execute。单一小模型、特定工具任务上的作者结果只说明这种分层缓存 recipe 可行，不证明缓存轨迹可替代真实交互或保持严格 on-policy。

随机工具返回还有比陈旧更隐蔽的边界：一次返回在同组多个 rollout 中共享，即使每条轨迹的条件 reward 分布正确，也改变了组内 reward 的**联合分布**。Group-normalized advantage 会再用这一组样本估计均值与尺度；因此缓存可能改变更新方向，而不只是增大方差。训练期复用须把独立随机源数量、cache sharing scope 和 group membership 一起记录，并与独立执行对照；可用仅中心化的 estimator 作受限控制，但它也不自动恢复完整 GRPO 的 clipping、KL 和 optimizer 语义。这个反例来自两动作、一步 on-policy 的精确有限求和及脚本化缓存审计，不是完整大模型训练测量，也不否定确定性工具结果的正确复用。<!-- source-family:SF-2026-ARXIV-2609-26866 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14179 -->

### On-policy 来源不等于 Conditioning State 一致

Student 自己采样 action 只能证明 action source 是 on-policy；若 teacher 在不同 token positions、visibility mask、memory encoding 或 environment snapshot 上为该 action 评分，训练信号仍来自 student 从未访问的条件状态。Replay 因而必须记录 invocation 的 token IDs、positions、causal mask、memory revision 与 environment snapshot，并证明 packed reconstruction 与原执行等价。更严格身份增加存储与重算成本；状态无法重建时应放弃该 teacher score，回退当前状态上的 outcome RL，而不能用“动作来自 student”掩盖 state off-policy。

<!-- source-family: arxiv:2608.07068v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: on-policy-action-conditioning-state-equality -->

## 多步 Credit 要先分配给 Action，再分配给 Token

把 episode reward 均匀广播给所有 token，会让长动作获得隐式更大权重，也无法区分真正改变环境的步骤。一个更守恒的分解先用 temporal signal 分配 action-level credit，再根据 teacher–student likelihood gap 等证据分到该 action 的 token；归一化必须保证总 credit 和符号不被长度改变。

Credit granularity 也不必在整个 episode 固定。可以用 state criticality proxy 在 episode-level 与 step-level advantage 之间调节：关键转移获得更细 credit，普通区段保留低方差的粗粒度回报。NLL 或 uncertainty 只是 proposal，不是因果贡献；proxy 失配、环境短或 verifier 很弱时，固定 episode/step 分支仍更稳健，最终 reward authority 不能交给 criticality estimator。

<!-- source-family:SF-2026-ARXIV-2609-12424 -->

这种估计会继承 value/teacher bias，并增加额外推理成本。reward 本就稠密、动作短或 teacher 不可靠时，简单 outcome advantage 仍可能更稳。验收应同时检查 credit conservation、长度敏感性与最终 policy，而不是只看训练 loss。

<!-- source-family: arxiv:2608.07118v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: action-then-token-credit-conservation -->

### Post-training Compute 应先定位瓶颈，再选择投入位置

扩大 backbone、增加 rollout search、增加 optimizer updates 与改善 reward feedback 都会消耗预算，但它们修复的是不同瓶颈。能力不足时更多搜索只会重复错误策略；探索不足时增加 update 会在窄分布上过拟合；feedback 噪声大时扩大模型也可能只是更强地利用错误目标。因此资源控制器应把 compute 分成 model、search、learning 与 feedback 四个账户，在 held-out evaluator 下比较边际收益，再移动预算。

这种诊断需要额外对照实验，单次训练成本更高，而且作者实验不能提供通用配比。已有稳定 recipe、预算很小或 evaluator 不可信时，冻结分配比自适应控制更安全；任何动态迁移都不能让训练 reward 同时成为预算分配与最终验收的唯一权威。

<!-- source-family:SF-2026-ARXIV-2607-13389 -->

### 异步 RL 的 trust region 应区分低熵噪声与高熵探索

统一 importance-ratio 阈值假设所有 token 的概率变化具有相同含义；在低熵 token 上，微小 train/inference discrepancy 就可能产生很大 ratio noise，而高熵 token 的较大 ratio 可能来自合法探索。按局部 entropy 缩放 deviation gate，可以把“数值/版本噪声”和“策略探索”分开处理。

entropy 不是 staleness 的充分统计量，校准错误会放进坏更新或挡住新行为；受限异步 stack 的吞吐/质量结果也不能给出通用阈值。系统仍须绑定 behavior/current policy revision、token identity 与 rollout provenance；entropy gate 失效时回退同步或严格版本有界路径。

<!-- source-family:SF-2026-ARXIV-2607-22186 -->

### 训练目标必须包含部署时 Inference Controller

若部署会使用 reranker、verifier、search、sampling budget 或 early-stop controller，仅训练裸模型的单次输出，会造成 training/deployment mismatch：模型可能学到与 controller 冲突的概率结构。训练可在 rollout 中实际运行目标 controller，并对“模型 + controller”的最终行为优化，同时记录 controller revision 和预算。

这种 co-adaptation 提高部署适配，却可能过拟合一个 controller、放大 reward hacking 并降低裸模型可移植性。应保留 controller-free slice 和替代 controller 回归；部署策略频繁变化或无法重放时，训练裸模型仍是更稳的基线。

<!-- source-family:SF-2026-ARXIV-2607-23771 -->

### 开放任务只有在 Transformation 保留目标且能自验证时才适合 RLVR

没有可靠 verifier 的任务，强行生成 reward 会把 judge bias 写进 policy。可将原任务变换为保留核心能力、但能由程序或一致性条件验证的子任务，再用 self-verification reward 训练；关键 gate 是 transformation 是否保持目标语义，而不是“自动产生了分数”。

变换会缩窄任务、引入捷径和 distribution shift，有限实验不能证明迁移到原开放任务。若无法建立 preservation evidence，应回退 SFT、人工偏好或 outcome-limited evaluation，而不是把弱 verifier 当真值。

<!-- source-family:SF-2026-ARXIV-2607-23802 -->

## 本章在知识树中的位置

```text
prompt x
-> G policy rollouts
-> reward / verifier
-> group-relative advantage
-> clipped policy update + reference KL
-> reasoning-oriented checkpoint
```

本章承接第 32 章的 ratio/clipping，先替换 value baseline，再把同一 objective 扩展到有状态 rollout、typed credit、policy freshness 与可恢复 trajectory；第 34 章走另一条离线 preference optimization 路线。第 35 章保存相关训练状态，第 36～41 章只接管 actor update 的分布式执行与 runtime policy。

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-22570 -->
LLM reasoning RL 的 update quality 取决于 rollout freshness、update count 与 policy drift；同一 reward 下不能把更多 optimizer steps 当成免费收益。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；单模型/任务与固定 1e-6 LR 不证明通用最优 update ratio；更少 drift 以额外 rollout 成本为代价。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

<!-- body-source:SF-2026-ARXIV-2606-22716 -->
效率 RL 不应奖励所有短答案；correct-only adaptive reward 先冻结 correctness，再在正确轨迹中调节效率 credit，避免把错误的短输出当优化方向。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；单 scale/数据与 reward verifier 限制结论；correct-only gate 会牺牲错误样本中的潜在学习信号。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

### Teacher Signal 要跟随 Learner 的当前 Rollout Distribution

离线 teacher traces 成本可控、容易复现，但 learner policy 演进后会遇到训练集未覆盖的状态。在线 teacher 可在 learner 当前 rollout 上提供 critique/reward，使监督对齐真实访问分布；代价是采样、teacher 调用和反馈相关性显著增加。

Teacher 只拥有辅助信号，不拥有最终 objective；需要绑定 learner/teacher revision、rollout policy 与 judge，并保留 frozen holdout。成本过高、teacher 不稳定或在线分布过窄时，回退离线数据或混合 replay。

若没有更强外部教师或完整专家解答，却能检验终局正确性，另一条分支是先把当前模型训练成 outcome-conditioned reviser，再让它提供密集监督。先采样初答，依据外部二元结果给出修订或重述提示，保留修订成功的轨迹；训练同时包含“给定初答与提示预测修订”的 loss，以及“只给题目预测 `[初答, 修订提示, 修订回答]` 整串”的 generation loss。后一项并非只监督正确末答，失败初答和后续纠正也在目标串中。随后 student 在当前策略下生成回答，冻结的 reviser 看到完整回答及其外部结果，给出特权上下文下的 token 分布，以 reverse-KL 监督 student 原本没有这些信息的生成路径；阶段结束后可再同步 teacher revision。<!-- source-family:SF-2026-ARXIV-2604-12002 -->

这里的增量是把稀疏 outcome 经过已训练的修订能力转为密集学习信号，不是让模型无监督地知道自身错误。正确性仍由外部 checker 负责；局部 KL 集中或修订词减少不证明定位了真实错误原因，冻结 teacher 也会继承修订偏差。它增加成功轨迹采集、过滤、teacher forward 和版本同步成本；生成数或估算 completion tokens 相近，不表示 prompt、backward、FLOPs 与 wall-clock 全匹配。现有数学/代码与 Qwen3-4B、Olmo3-7B 的受限结果不保证无限自改进。修订成功率不足、checker 不可靠或成本超过收益时，回退 outcome-only GRPO、已有离线监督或外部教师，保留独立 holdout 而不把自我蒸馏当作最终验收。

在线蒸馏后的提升也不自动证明教师知识被迁移。一个必要的归因对照是在相同任务与可比 rollout/token 预算下移除 teacher，改用固定 advantage 或只作用于特定概率位置的更新，并检查 entropy、长度与 held-out outcome 是否仍出现相近变化。若 teacher-free 对照已经解释主要收益，结论应收窄为 student policy 的重塑，而不是宣称获得新的教师知识或扩大了探索边界。这类对照增加训练与评价成本，也不证明 teacher 永远无用；只有在额外知识增量得到独立验证时，才将那部分收益归因给教师监督，普通离线蒸馏仍适用于行为迁移明确、成本优先的情形。

现有 exact-v1 只在其披露的 reasoning learner、teacher、任务集合与采样预算中验证这种 on-policy distillation；它支持“当前 rollout 能暴露离线 trace 未覆盖状态”，不证明任意 teacher、开放任务或更大预算下都优于离线监督。未披露模型、硬件、并发与 judge 条件保持 Not Disclosed。

<!-- source-family:SF-2026-ARXIV-2605-17497 -->

### Asynchronous RL 必须把 Policy Staleness 写进 Advantage

异步 rollout 提高 actor 利用率，却让 trajectory 来自旧 policy。若把所有样本当 current policy，importance ratio、group baseline 与 advantage 会混入版本偏差。Runtime 应携带 behavior-policy revision，并在 update 时校正、降权或拒绝超出 staleness window 的样本。

这用吞吐换校正方差、丢样和更多版本状态；环境昂贵且 drift 慢时可接受有界陈旧，质量敏感或 policy 快速变化时回退同步 barrier。staleness 数字必须与 convergence/outcome 一起验收。

exact-v1 的支持范围仅包括其披露的 GRPO 配置、模型、rollout workload 与少量 sequential generation-optimization stages；它证明这些设置可容忍比既有假设更大的 staleness，不证明异步程度可以无界增加，也不建立跨模型通用阈值。未披露硬件、并发与生产 SLO 保持 Not Disclosed。

<!-- source-family:SF-2026-ARXIV-2605-17570 -->

但版本年龄不是 train/rollout mismatch 的唯一来源，同一权重也可能因 precision 或 kernel 路径产生概率差异。除了对已经接纳的样本校正ratio，一个更保守的分支先对prompt整组做admission：以rollout policy下的概率比估计 \(\mathcal K(x)=\mathbb E[r-1-\log r]\)，只有估计drift低于阈值 \(\tau\) 才让该prompt的整组输出进入gradient。这里 \(r\) 比较current与rollout policy在同一scored对象上的概率；scoring、support与估计方法也须明确。如此得到的目标是在 \(P(X\mid\mathcal K(x)<\tau)\) 上更新，不只是对原prompt人口做importance correction；低drift更不等于样本正确或reward可靠。<!-- source-family:SF-2026-ARXIV-2512-24618 -->

这用额外scoring、整组丢样和可能的重采成本换较窄的更新支持，也会把高drift任务持续排除。因此要分别保存原prompt人口、接纳/拒收切片、阈值、behavior/current revision与数值路径，并检验有限样本估计及目标覆盖；不能把条件目标称为原人口的无偏优化。[Youtu-LLM v1 §4.2.2/Fig13](https://arxiv.org/html/2512.24618v1)只给内部math/code上的局部训练动态，未建立通用阈值、任意kernel一致性或FP16普遍优于BF16。估计不稳、拒收率过高或重要任务被饿死时，应校验数值路径、刷新rollout并退回同步/版本有界采样，而不是仅放宽阈值后宣称原目标已恢复；普通ratio/clipping在mismatch可控时仍是更简单的旧路。

整组拒收之外，还可以对已生成的完整 sequence 做 soft reshaping。固定 behavior 分布 μ 与 current policy π，令 W=π/μ；在正支持、可归一和所声明 KL 混合及期望比值约束可行的条件下，变分 proposal 具有 Q∝μ W^α exp(−λW) 的形式。训练再用按 advantage 符号选择的可调幂次与指数 kernel，将 detached sequence weight 乘到整串 log-probability 更新上，不另以长度平均。这改变被强调的 sequence 人口，而不是自动恢复 π 下的无偏 policy gradient；比值期望只是约束 proxy，不是实际 advantage 与 score-function 梯度方差的完整证明。<!-- source-family:SF-2026-ARXIV-2602-10693 -->

该分支增加 behavior/current scoring、支持检查与 sign-kernel 校准成本，也不能替代 train/rollout 数值一致性。原受限数学实验通过批内多个 update 改变 staleness，并非固定墙钟或任意版本年龄保证；同标配置的两张结果表、负 advantage 参数解释存在冲突，不能据此指定唯一最优参数或拼接准确率。比值估计、kernel 或任务覆盖不稳时，应刷新 rollout、回退已有 ratio/clipping、整组 admission 或同步路径，而不是把 soft weight 当作 reward 可靠性和无限陈旧容忍证书。[必要机制与反侧](https://arxiv.org/html/2602.10693v1)见 §3、Appendix B、Tables1–2 与 §4.6。

即使权重和数值路径相同，rollout 的历史 view 也会创造另一个 sampler：KV 被压缩后，生成策略以稀疏历史为条件，而 dense old policy 和当前 learner 仍以完整历史评分。于是 policy ratio 要分成 learner/dense-old 的版本差异，与 dense-old/sparse-sampler 的 view 差异；后者不能藏在一个旧 checkpoint 名字里。一个受限分支用同 prefix 的逐 token 比值 ξ 检测极端不一致，任一 token 低于阈值就令整条 response 不参与梯度，再把保留项的 ξ 放到仅约束 learner/dense-old 的 clipping 之外。这分别改变 response admission 与 token update 权重，不让压缩算子拥有 reward 或逻辑正确性的判断权。<!-- source-family:SF-2026-ARXIV-2601-10079 -->

两个局部概率比相乘可以消去 dense-old，但没有因此恢复稀疏 sampler 已产生的 prefix 人口；response 拒收、group advantage 和 clipping 也不能继承完整 dense RL 的无偏保证。低 ξ 只是相对概率异常，不证明 hallucination、数学 support 为零或推理无效。[Sparse-RL 的受限实验](https://arxiv.org/html/2601.10079v1)在四个1–7B模型、R-KV/SnapKV、binary数学 verifier、4 H20 与400 steps下支持这种稳定化分支；512-token KV预算的有效性不普遍，128预算会退化，部分模型仍低于 dense baseline。KV retained-token 节省也不是总显存或端到端加速：dense scoring、拒收废样、比值方差和 view/mapping 身份都增加成本。拒收率过高、必要历史丢失或 verifier 不可靠时，应回退完整 KV、fresh/dense rollout 与现有同步或有界陈旧路径。

## 从机制演进到系统设计

GRPO 去掉 critic 后，把主要状态转移到同 prompt rollout group、相对 reward 与 policy freshness。规模扩大时，瓶颈不只在公式：domain curriculum、group straggler、stale rollout、update ratio、reward density 和 supervisory repair 共同决定有效 credit。controller 可以利用 gradient transfer 或运行时风险选择 domain/group，但不能拥有最终 correctness。

这类控制减少无效 rollout 或 critic 状态，却引入更多采样、估计噪声、跨域干扰和 collapse gate。收益必须在相同 rollout/token/optimizer budget 下比较；gradient conflict、verifier drift 或 policy divergence 越界时，应回退 proportional mixture、同步 rollout 或 PPO/SFT 分支。PPO 与 GRPO 是 credit fidelity、variance 和 compute 的条件分支，而不是新旧替代。

## 自检问题

1. GRPO 为什么要求同一 prompt 下生成一组 responses？
2. Group-relative advantage 与 value model advantage 有何不同？
3. 三样本小例子如何得到正、零、负 advantage？
4. 所有 group rewards 相同会发生什么？
5. GRPO 保留了 PPO 的哪些机制？
6. 移除 critic 节省哪些状态，又增加什么成本？
7. Group size 为什么应随任务成功率理解？
8. Verifiable reward 为什么仍可能被 exploit？
9. Policy lag 怎样破坏 grouped rollout 的语义？
10. 为什么不能把所有“GRPO”实现视为同一 objective？
11. Partial rollout 为什么会把 trajectory 变成需要 checkpoint 与恢复的状态？
12. 为什么跨 policy 共享 rollout 时不能丢弃 source policy 与 tokenizer identity？
13. 跨 tokenizer 重算 target log-probability 为什么不等于严格的 token-wise importance correction？
14. Phase-aware RL orchestration 中，compute scheduler 与 fabric controller 为什么需要共享 epoch 和 fallback？
15. 为什么 DAPO 应理解为四个运行失败点的组合修补，而不是 GRPO 的单一标量升级？
16. DAPO 的 token-level reduction 与 Dr. GRPO 的 fixed-budget normalization 为什么不能被视为同一目标？
17. CISPO 与 GSPO 分别改变 clipping 的什么对象和 importance ratio 的什么粒度？

### Tool-use RL 的训练对象包含环境编排

当 trajectory 跨越多个工具回合时，policy 的 reward 同时受环境隔离、工具等待和 rollout 调度影响。把每个 MCP 环境作为有版本、可回收的执行单元，并用重叠流水线覆盖 I/O stall，可以提高 rollout goodput；但训练日志必须保留环境镜像、tool response、timeout 和 episode ownership，才能区分策略改善与运行时差异。RL backend 只负责更新参数，不应隐式拥有这些外部状态。
<!-- source-family: arxiv:2608.22167v1; semantic-body-binding: mcp-rollout-environment-ownership -->

### Audio-native Trajectory 还包含 Observation Error

语音 Agent 的 rollout 不只是文本 token 序列：ASR、speaker turn、时间边界和声学歧义都会改变 policy 实际看到的 observation。训练与评测要把 modality observation error、reward density、工具结果和最终 outcome 分开；更密的 process reward 可以改善 credit assignment，却不能替代任务结果与授权 gate。否则模型可能学会迎合中间评分而非完成真实交互。
<!-- source-family: arxiv:2608.26432v1; semantic-body-binding: audio-native-trajectory-observation-error -->

### Loss Reduction 也在重写 Credit 权重

<!-- semantic-body-binding:SF-2026-ARXIV-2605-04077:start -->
GRPO 已经为每条 response 计算组内相对 advantage，但最终如何聚合 token loss 仍会改变每条轨迹对 update 的实际权重。先对每条 sequence 求均值再对 batch 求均值，可以避免正负样本的贡献随长度比例漂移，却会系统性下调长 response；把所有 token 直接求均值能恢复 token-level 权重，又会把正、负样本的平均长度差耦合进梯度符号。因而 `sequence` 与 `token` reduction 不是纯实现选项，训练 artifact 必须保存聚合规则、正负长度分布、有效 token 数和 clipping identity。

一个条件分支是先按 advantage 符号分组，在组内做 token aggregation，再按正负 sequence 数合并，使 sign balance 与 token weighting 分开。它增加统计与实现复杂度，也不能消除 reward error、group zero variance、importance-ratio drift 或长度本身携带的任务信号；长度差小、响应近等长时，简单 sequence aggregation 仍更易解释。`arXiv:2605.04077v1` 的 §3–§5 只支持所测数学/代码 RLVR、模型与训练设置中的偏差分解和 Balanced Aggregation，不证明跨 reward、超长 agent trajectory 或任意 clipping 配置通用最优。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-04077:end -->

### Rollout Allocation 的统计单元应是 Comparison Pair

GRPO 的相对优势来自组内比较，额外 token 或 rollout 若只按单条样本分配，会改变哪些 comparison pair 被观测。以 pair 为统计单元并按 inclusion probability 校正，可以在理想单步、无裁剪和无标准化条件下保持估计无偏；真实训练中的 clipping、多 epoch 与 advantage normalization 会破坏该证明。工程实现应把它标为近似并用重复实验检查偏差。
<!-- source-family: arxiv:2608.11368v1; semantic-body-binding: pair-level-rollout-allocation -->

## 小结

GRPO 用同 prompt 多个 responses 的相对 reward 代替 learned critic baseline。它减少 value-model 状态，并保留 clipped policy update 与 reference constraint，适合 reward 可比较、尤其可验证的 rollout 任务。

它没有让 RL 变简单到只剩一个公式。Group variance、rollout generation、reward specification、token credit、policy synchronization 和 implementation variants 共同决定训练是否有效。
从 DAPO 到 Dr. GRPO、CISPO 与 GSPO 的后续分支进一步说明：样本准入、loss reduction、clipping 对象与
ratio 粒度是彼此独立的设计轴，方法名称不能替代 objective 与 artifact contract。


### Group-relative 更新还要管理 Token Covariance 与异构 Reward

对组内所有 token 使用同一归一化 advantage，在样本短且 credit 均匀时简单；极端 token 与组内其他 token 强相关时，
它会放大方差。covariance-aware reweighting 根据组内更新相关性调整 token 权重，把“哪一个 token 主导梯度”变成显式
controller state。收益是作者设置中的稳定性，代价是协方差估计噪声、额外统计和过度压制稀有关键 token；小模型、短序列
或估计不稳时应回退标准 GRPO。证据仅覆盖至 7B 与数学任务。

<!-- source-family:SF-2026-ARXIV-2605-11538 -->

统一多模态生成把离散 reasoning 与连续视觉 trajectory 放进同一 policy 后，单一 final reward 会掩盖失败发生在哪个状态。
AlphaGRPO 将目标拆成可分别验证的 reasoning atoms 与视觉 trajectory atoms，再由明确的 aggregation contract 组合；
evaluator 拥有各原子证据，optimizer 只消费冻结后的 advantage。它改善 credit localization，却扩大 reward hacking、评估成本
与通道冲突。原子 verifier 不可靠或任务不可分解时，应回退 outcome reward、分阶段训练或人工评测。现有结果不能外推到
论文未测模型与视觉任务。

<!-- source-family:SF-2026-ARXIV-2605-12495 -->

### Diffusion Policy 的 Credit 需要覆盖整条去噪轨迹

只最大化终局高 reward 样本，会让 diffusion language policy 追逐少数 mode，探索范围逐步收缩。trajectory-balance
分支把完整去噪轨迹及其前后向概率纳入 credit，使多个可行终点仍获得训练信号；这改变的是 trajectory distribution，
不是给每个中间状态创造了真值。收益是维持覆盖，代价是归一化估计、探索预算和高方差；估计不稳或任务近单峰时，
标准 outcome GRPO/离线偏好仍更合适。exact-v1 的结论限作者任务与 Appendix H 所述边界。

<!-- source-family:SF-2026-ARXIV-2605-13935 -->

完整轨迹终奖之外，还可以对一个冻结的中间 masked state 构造局部对照：缓存行为模型在该状态的 logits，保留已填位置，只对尚可动作的位置抽若干一次性全填候选，再用同一个 terminal evaluator 评价完整文本、形成同状态的相对信号。这不是从原 rollout 接着运行剩余去噪过程，也没有为中间位置创造 causal label；optimizer 只更新本次新填的 action positions，已填内容仍作 context。这个 Experimental 分支把完整轨迹的 outcome 信号与冻结状态内的候选比较分开，不能由其经验目标推得实际 policy gradient 无偏：归一化 surrogate、实际 branch sampling law 与组内 baseline 的桥梁尚未建立。<!-- source-family:SF-2026-ARXIV-2602-06462 -->

同 rollout 数、同 update 数仍不是同总预算：更多候选要另付 terminal reward 与 surrogate log-probability 求值，缓存原 logits 只免去相应的候选生成 forward。作者配置的实际吞吐约为基线的 0.4 倍，wall-clock 学习比较限于 Sudoku；增加候选数并非质量单调改善，部分 Countdown/GSM 设置也有退步。因此应共同冻结中间状态、mask、行为策略、评价器、候选数与完整成本，分别验收局部质量和净训练效率；状态或 surrogate 不可信、代价不合算时，保留完整 rollout 的 outcome GRPO、原 diffusion credit 或离线偏好，不以受限方差定理批准通用稳定性。

masked policy 的更新还须冻结 surrogate 的权重与 rollout 人口：用互补的两个 mask views 使每个 token 被预测一次，再取单位权重而非 `1/t`，改变的是原 masked ELBO-surrogate 的时间加权，不是得到 exact sequence likelihood；据此构造 SFT、偏好或组相对 loss，也不意味着三者的目标或 KL 功能全部等价。另一项人口干预只在组内全低分时，把 ground-truth answer 强制放入新的 rollout，让其余位置获得训练信号；这把标签条件下的轨迹带进更新，正确 answer 仍不认证 reasoning 内容。两视图、online surrogate 求值与 forcing 都付额外成本；受测消融中 100% forcing 坍缩，而较低比例更好，质量/repetition reward 也只是所选任务的 proxy。应把 mask、权重、行为模型、forcing 比例及强制位置共同纳入 experiment identity，分别测自由生成与标签条件人口；目标或人口失配时，恢复原时间权重、未强制 rollout 或离线监督，不能把局部效果当成统一无偏 policy gradient。<!-- source-family:SF-2026-ARXIV-2602-14147 -->

### Verifiable Process Supervision 要验证 Claim，不是奖励更长 Trace

只有 final-answer reward 时，模型可通过偶然或 shortcut 得到正确结果；直接奖励完整 reasoning text 又容易把格式和冗长当质量。Verifiable process supervision 把中间过程拆成结构化 claims，由可执行或可核查的 verifier 给出局部信号，再与最终准确率共同优化。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12519 -->

Verifier coverage 不完整时，模型会迁移到未检查的步骤，claim decomposition 也可能丢失跨步依赖。现有任务结果不能证明开放推理忠实；无法形式验证时，应回退 outcome reward、独立 trace audit 和人工检查，不以过程长度代替正确性。

### Sequence-level Contrast 改变 RLVR 的 Credit Coordinate

Token-level clipped objective 易把已验证序列的整体相对关系切碎。以长度归一的 sequence log-probability 为 score，并在同组中对比 verified positive 与 negative distractors，可以把 credit 放回完整 trajectory；收益是直接优化相对序列偏好，代价是更粗的局部归因和对组构成敏感。<!-- semantic-body-binding:SF-2026-ARXIV-2605-12969 -->

长度归一和负样本并非中性，可能偏向特定风格或难度。所测 reasoning benchmark 不证明通用优势；组内正负覆盖不足或长度偏差明显时，应回退 token/step reward、重构 group，或使用混合 objective。

### Dense Teacher Signal 也会沿序列失去可教性

On-policy distillation 让 teacher 在 student 自己的 rollout 上提供 dense feedback，缓解离线分布偏移；但 prefix 尚在双方共同 support 内时信号可学，suffix 随 policy divergence 增大后可能逐步失去 teachability。训练需要按位置监测 support overlap、teacher-student divergence 与梯度有效性，而不是把整条序列平均。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13643 -->

局部可教性指标仍依赖模型和任务，不代表 suffix 永远不可学习。后缀信号退化时，应缩短 rollout、增加中间 anchor、混入离线高质量轨迹，或回退 prefix-level distillation。

多轮交互的 teacher support 还可通过两种不同的 curriculum 恢复。前向扩展只先开放短 student prefix，再逐渐增加深度；反向扩展先由 teacher 沿已验证成功轨迹导航到近终点状态，student 接管后缀，再逐步把接管点向前移动。二者改变的状态分布和采样责任不同：前者限制 student 尚不能被有效监督的深度，后者依赖 teacher 成功前缀与环境重放，不能统称为纯 on-policy 采样。<!-- source-family:SF-2026-ARXIV-2604-24005 -->

反向 curriculum 额外支付 pass@10 成功轨迹筛选、teacher action 和 reset/replay 成本，还可能只覆盖 teacher 擅长的路径；应绑定 teacher/student、任务与接管 frontier，分别比较监督有效性、环境调用与终局 outcome。[exact-v1 §4–5](https://arxiv.org/html/2604.24005v1)只支持给定师生和 ALFWorld/WebShop/ScienceWorld 的受限实验，不证明成功前缀是开放环境真值或任意任务可超越 teacher。环境不能重放、teacher 无可靠成功路径或预算不足时，保留前向短 rollout、普通 OPD/离线监督和独立 outcome gate。

### Policy Staleness 应进入 Advantage 的可信度

异步 rollout 复用旧 policy 样本能提高设备利用率，但固定 clipping 把 trust region 与 behavior mismatch 隐藏在一个超参数里。更直接的路径用 behavior/current-policy ratio 表示 staleness，并让 ESS controller 分配本批 update trust；rollout engine 差异也必须进入 identity。它减少手调，却会被小 batch、重尾 ratio 和数值误差误导，保留高-ratio signal 还会提高方差。ESS 不稳时，应回退固定 clip/KL、fresh on-policy rollout、丢弃超龄样本并校验 trainer-rollout 数值一致性。exact-v1 不证明免调参或任意陈旧数据都可安全学习。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12380 -->

ESS 已经能描述旧样本的权重集中，另一个独立问题是同一批 rollout 的 reward baseline 怎样与实际梯度相配。在未截断 importance ratio、支持集相容且允许交换微分与期望的条件下，固定的 population scalar baseline 可按 \(w^2\|g\|^2\) 加权 reward 来最小化该 score-function estimator 的方差；它不是普通 group mean，也不是 learned value。一个[受限执行分支](https://arxiv.org/html/2602.17616v1)以有限 batch 的加权比值作 plug-in，并在梯度中停止对 baseline 求导；包含样本自身的估计与后续 TIS 截断不能继承固定 population baseline 的无偏性或 variance-optimal 保证。其 ESS 从未裁剪 ratios 计算，而实际更新使用 TIS，并按 off-policy ESS 与 on-policy reference 的比值平方根缩放步长；reference、behavior/current revision 与数值支持须一起保存，不能将这一经验控制称为任意 staleness 下的稳定性定理。<!-- source-family:SF-2026-ARXIV-2602-17616 -->

这个 baseline 也改变训练执行：逐 trajectory 计算 score gradient 与其范数，延迟 DP 同步，分别累积 reward-weighted 和 score 两个梯度 buffer，最后组合再 all-reduce，避免为每条 trajectory 额外再做一次 backward，而不是整批只做一次无代价反传。Qwen2.5-7B、4 H100/TP4、8192-token 单步测量仍增加约 19% step time 与14% memory；它不同于 MATH/MATH-500、lag10、4 H100 sampler加4 H100 trainer、512 rollout、4096 response/400-step 的训练对照，精度与端到端SLO未披露。同配置组件和较低固定LR反侧只支持该 population 的成本／质量取舍，不证明组合的所有提升都来自 baseline。小 batch、重尾权重、plug-in 不稳或额外缓冲不合算时，保留独立／leave-one-out基线、fresh rollout与原固定 step/clip路径，并重新匹配同质量预算。

### Critic 只有在改善后续 Solver 结果时才获得训练信用

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15224:start -->
固定外部 critique 在错误类型稳定时容易审计，但不能随 solver 的能力边界共同演化；直接联合训练 solver 与 critic 又可能让两者互相迎合。ICRL 把 critic 的 reward 绑定到“solver 读取该 critique 后是否取得更好的后续结果”，再以 distribution ratio 约束 critique-conditioned policy 向 critique-free solver 的迁移，并按角色分别计算 group-relative advantage。critic 因而只拥有建议，solver 拥有解答 trajectory，任务 verifier 才拥有 outcome。

这种共同训练改善 credit density，却引入自我确认、critic/solver distribution shift、ratio 估计误差和双倍 rollout 成本；critic 说得像样不等于因果上改善答案。exact-v1 的 §3.1–3.2、§4.2–4.3、§5.2–5.4 与 Appendix A/B 只支持披露任务和模型。critic reward 与独立 outcome 脱钩、ratio 不稳定或角色优势塌缩时，应冻结 critic、回退外部 critique，或只对可验证 solver outcome 做 RLVR。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15224:end -->

另一个分支直接让同一 policy 采 answers，再对筛入 cache 的 question-response 采 critiques；每题只留一个 correct 与一个 wrong，抑制原 n² 扩张及标签偏斜，然后把 answer 的 outcome 与 critique 最终 binary verdict reward 混入同一组。[Second-order Rollout v1](https://arxiv.org/html/2602.22765v1)没有验证 critique 中间步骤，平衡人口上的判别准确率也不是自然错误率人口的诊断；同训练数据更不等同总采样/teacher预算。有限数学对照中 dynamic data 对 joint update 有益，却在 critique-only 中让 policy 故意生成错答再判 wrong，static反而更好。缓存、过滤、蒸馏与额外采样付费，作者也报告收敛更慢；标签、规则oracle或支持不稳时，保留 static 外部critique、固定标签或仅generation RL，不把动态自评写成免费或普遍无偏监督。<!-- source-family:SF-2026-ARXIV-2602-22765 -->

另一种训练约束不让 solver 与 auditor 同时演化：先分别校准 Planner/Solver，再冻结它们，运行真实系统收集两者的完整 trace，由高容量 Inspector teacher 产生审计与恢复标签，最后只训练消费 `(question, expert trace)` 的 Inspector。变化在 Stage-II observation 与 reward，而不在 GRPO optimizer；冻结专家让“从什么基线恢复”更可辨认，Inspector 仍只提出改写、扩检或重试，correctness 由任务 outcome 验收。净收益应拆成失败被恢复与原先正确却被改坏两份，而不能只看 recovery 次数。<!-- source-family:SF-2026-ARXIV-2601-05465 -->

冻结减少共同漂移，却会把当前专家的盲点和成功 trace mining 的选择偏差固定下来；teacher 审计标签也可能有错，inspection/solver 占据额外运行时间。受限多跳 QA 的模块替换与训练消融支持 trace-conditioned audit 的一个实现，不给任意任务的 do-no-harm 或生产可部署保证。专家 checkpoint、retriever/corpus 或失败人口改变后，需重新收集 trace 并同时检查 recovered、regressed 与检测误报；成本过高或标签不可靠时，保留固定外部检查、人工审计或只训练 solver 的旧分支。

### Relative Advantage 还要保留数值尺度与平移身份

Group-relative ranking 不足以定义可执行更新。低方差 reward group 中，归一化后的 advantage 即使符号正确，也可能小到低于优化器、混合精度或梯度裁剪可分辨的尺度；相反，off-policy scorer 的加性漂移虽然不改变 action ranking，却会改变绝对 update magnitude。稳定实现应把 reward/score 版本、group statistics、centering reference、恢复上限和 optimizer scale 写入同一 batch identity：先只移除不携带偏好信息的公共偏移，再在明确上限内恢复过小信号，最后由 KL、ESS 与 held-out outcome gate 决定是否提交。<!-- source-family:SF-2026-ARXIV-2609-19164 --><!-- source-family:SF-2026-ARXIV-2609-20807 -->

这两类修正用更可用的梯度换来额外估计噪声，也可能放大本来就不可靠的 reward。作者实验不证明固定 centering 或 rescaling 对所有模型和任务安全；group variance 真实接近零、off-policy support 不足或校准后 regression 变差时，应跳过更新、重新采样或回退 fresh on-policy rollout，而不是强行制造 advantage。

### Rollout Tree 的分支预算应购买梯度信息，而不是购买表面不确定性

按 policy entropy 在每个高不确定节点扩展分支很直观，却可能反复采样对最终梯度几乎没有区分力的动作。更直接的 controller 估计候选分支在单位生成成本下能降低多少 policy-gradient uncertainty，再把有限 rollout budget 分给预期信息增益最高的节点。它改变的是采样 proposal，不拥有 reward 真值；inclusion probability、branch ancestry 与实际 token cost 必须保留，才能避免把自适应采样静默写进 objective。<!-- source-family:SF-2026-ARXIV-2609-20004 -->

收益是把 compute 集中到有比较价值的分支，代价是价值估计器本身可能偏置、冷门状态会被饿死，而且 tree bookkeeping 增加延迟。估计不稳、任务分支少或需要无偏覆盖时，均匀/分层采样仍是更可靠的 baseline。

### On-policy Distillation 需要统一停止语义，并让 Teacher 有退出条件

Student 与 teacher 使用不同表面 EOS token 时，逐 token distillation 会把“应该停止”误写成“token 不一致”，导致正确终止动作被惩罚。训练合同应先把多个表面 token 映射到同一个 semantic stop class，再由 decoder 保留各自词表身份；仅扩大推理解码的 stopping set 不能修复训练梯度。<!-- source-family:SF-2026-ARXIV-2609-20511 -->

Teacher 也不应永久留在控制环。先独立优化 privileged teacher，再持续测量 student discrepancy 与任务 success；只有二者达到预注册 gate 且不再改善时，controller 才可退休 teacher，并保留重新启用条件。这样把 privileged information 从永久 authority 降为有生命周期的训练 actuator，代价是双模型成本、退出阈值和回归监控。现有证据只覆盖作者的 agentic RL 与 OPD 设置，不证明任意 teacher 可以安全退休；student 回归、环境漂移或 semantic-EOS 映射失效时，应恢复 teacher/离线数据或停止更新。<!-- source-family:SF-2026-ARXIV-2609-20784 -->

### Filter Predicate 不能被 Shaped Reward 伪造出对比度

Group filtering 需要区分 task outcome、training reward 与 filter predicate。Shaped score 可以为 policy 提供更密的梯度，但若原始任务结果在组内没有对比，reward shaping 制造的 spread 不能冒充“这一组值得用于相对更新”；否则 filter 与 optimizer 共同改变了 objective，却仍被记录成原任务信号。<!-- source-family:SF-2026-ARXIV-2609-13866 -->

这条分离增加 outcome 记录和双重指标维护成本，也受任务判定器质量限制。无法获得可信 task outcome 时，应关闭 dynamic group filter 或回退固定采样/离线检查；作者 GSM8K/MATH、Qwen2.5 与短 LoRA 训练不支持通用阈值。

## Review notes

- `SF-2026-ARXIV-2602-21534`：[v1 §3–4 / Table 4](https://arxiv.org/html/2602.21534v1)。采用负 turn 的序列 log-ratio mask 与 token 更新分层；CISPO 数字正文/表格有小差异，KL/batch 和 loss aggregation 反侧保留，不采用无条件稳定性。`SF-2026-ARXIV-2602-21628`：[v1 §3 / Eq.6–8](https://arxiv.org/html/2602.21628v1)。初始 rollout 难度、持续 easy-batch 门控与 hard reward ramp；条件成功率不能混成全人口，CV 不能外推梯度保证。`SF-2026-ARXIV-2602-22190`：[v1 SNGS / 在线离线对照](https://arxiv.org/html/2602.22190v1)。负 advantage 缩放、零组与离线下降保留。三项均由非原 packet 作者核必要原证与 owner 后窄写，root已实际顺读正文、完整邻接与自身末注，POST通过，未复现实验。

- `SF-2026-ARXIV-2602-22556` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22556v1)，binarycorrectshortbonus/L^-beta×tokenSUM与共享normalizer/双teacher。2+1+2=5，具体owner差额深入；限制、反侧、完整费用与原分支回退近正文。root实际必要原源/owner PRE通过并授单段窄lease；作者正文/完整邻接/自身末注已顺读，root非作者实际正文/完整邻接/自身末注POST通过。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-22495` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22495v1) §3–4/Eq3/必要反侧；teacher-old几何ratio与signed advantage，隔离端点/硬clip/KL误授并保selection人口与费用。2+1+2=5，具体owner差额深入，限制与原分支回退近正文。root实际必要原源/owner PRE通过并授窄lease；作者正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注POST通过，窄lease释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21320` — Daily `2026-02-27`；[Tool-R0 exact-v1](https://arxiv.org/html/2602.21320v1) §3–4/Table3/§5.2/6。2+2+3=7，外部spec支持集、MC难度门与schema≠执行真值深入；不合并Table1/2 APIbank baseline冲突，不授无先验、无总成本或无限自提升。root必要原源/实际owner PRE及实际正文/完整邻接/自身末注非作者POST通过，窄锁释放。未核实现或复现，非日级完成。

- `SF-2026-ARXIV-2602-21420` — Daily `2026-02-27`；[ACE exact-v1](https://arxiv.org/html/2602.21420v1) §4/Eq4–14/Alg1、§5/Table1–3/§6。2+1+3=6，具体negative multiplier接口深入；c0、均值logratio/stopgrad残差、reference不认证truth与Llama低k反退近正文，不采用方差定理或全模型全k保证。root必要原源/实际owner PRE及实际正文/完整邻接/自身末注非作者POST通过，窄锁释放。未核代码/复现，非日级完成。

- `SF-2026-ARXIV-2602-14169` — Daily `2026-02-18`；[DEEP-GRPO exact-v1](https://arxiv.org/html/2602.14169v1) §4.1–4.4、必要评价/Implementation/Limitations。2+1+2=5，depth×有限K经验recoverability与main/aux人口归一差额深入；prefix gradient mask不免forward、local非root无偏、logistic非逐prefix真值、λ/串行成本与原root回退近正文。Eq轨迹均值与附录batch-token均值口径冲突仅报告，不授exact objective。root必要源/actual owner PRE及实际正文/完整邻接与末注非作者POST通过，窄锁释放；未核实现或复现，非日级。

- `SF-2026-ARXIV-2602-12579` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12579v1) §2–4/Th4.1/Eq12、C1、必要配置及反侧。2+1+2=5，normalized selection 人口/方差责任深入；真实β/冻结mask不同batchquantile，有界目标差不授SGD最优或低entropy必降variance，拒绝rollout成本近正文。root必要源/actual owner PRE通过并授一段窄锁；作者已顺读正文/完整邻接；root非作者实际正文/完整邻接及末注POST通过，窄锁已释放。未运行实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-14468` — Daily `2026-02-18`；[LACONIC exact-v1](https://arxiv.org/html/2602.14468v1) Eq3–9、必要 cap/idealized 条件与预算反侧。2+1+2=5，hinge-primal/signed-mean-dual 具体差额深入；平均非tail、cap可并列、有限GRPO不继承理想化保证，质量/成本边界在机制附近。root 必要原源/actual owner PRE通过并授窄锁；实际正文/完整邻接/本末注经root非作者POST通过，锁释放。未核代码或复现，非日级Gate。

- `SF-2026-ARXIV-2602-14147` — Daily `2026-02-18`；[LaViDa-R1 exact-v1](https://arxiv.org/html/2602.14147v1) §3、AnswerForcing 消融和 Appendix C必要 online成本。2+2+2=6，互补 mask 权重与标签强制 rollout 人口的具体差额深入；不授统一likelihood/无偏/所有KL功能等价，100% forcing collapse与额外求值成本近正文。root必要原源/actual owner PRE通过并授窄锁；实际正文/完整邻接/本末注经root非作者POST通过，锁释放。未核代码或复现，非日级Gate。

- `SF-2026-ARXIV-2602-06375` — Daily 2026-02-10；[DEPO exact-v1](https://arxiv.org/html/2602.06375v1) §3.1–3.2/Eqs4–9、§4.1–4.3/Table2/Fig7。2+1+2=5，before-rollout estimator vs actualzero-group接口gap深入；不采用ranking方向/未披露threshold或真实zero-variance保证。Qwen2.5 1.5/7B、16/32H100、1000steps/b128/G8、eval32/temp1/topp.95；总125.65秒高于GRPO121.85秒且columns不假设串行相加，过filter反退保留。precision/seed/outcap/SLO未披露，未复现。root必要原源与owner写前通过，实际POST待核。

- `SF-2026-ARXIV-2601-10079`（Experimental）— Daily `2026-01-17`；[Sparse-RL exact-v1](https://arxiv.org/html/2601.10079v1) §3/4.1–4.3/5.1–5.3/5.5、Limitations及AppendixE，3+2+3=8。只采用 sparse sampler/dense old/learner 三分布、response ratio gate 与 clip 外 ξ；同prefix ratio相消不恢复prefix人口，不认证逻辑valid或无偏完整dense objective。slime、hard~8k、G8、KV512、max4096、400steps、4H20，binary奖励；token saving非总memory/time，未复现。root必要原源/owner写前通过，已实际核正文、邻接及末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08427`：[exact-v1](https://arxiv.org/html/2601.08427v1) §3.1–3.4/Eqs2–4、§4/Table4、§6、Appendix F.2 与 Limitations，Daily 2026-01-15。5分具体 reward-source 缺口深入；只采用归一末 token 表示→IRCE 中心→组内距离 proxy 与失败条件，不采 truth direction、普遍加速或零成本。root 必要来源与现 owner 写前独立复核通过，已实际核L64–76正文/邻接与末注，非作者POST通过；未复现实验，日级Gate未授。

- `SF-2026-ARXIV-2602-05758` — Daily `2026-02-07`；[LongR exact-v1](https://arxiv.org/html/2602.05758v1) §3.3.1/3.3.2、verifier-size反侧与必要配置。2+2+2=6，具体quote条件似然代理缺口深入；不采MI/真实阅读/事实真值或同总预算收益。root实际必要源/owner写前通过，实际正文/邻接及末注root实际非作者POST通过；未复现。

- `SF-2026-ARXIV-2602-05842` — Daily `2026-02-07`；[RWML exact-v1](https://arxiv.org/html/2602.05842v1) §2.2/3.2–3.4/4.1–4.3及B1/C1。2+2+2=6，具体transition prediction proxy中间训练缺口深入；ALFWorld embedding与τ²用户embedding/tool ROUGE分开，不采truth、无忘记或exact GRPO ratio保证。root实际必要源/owner写前通过，实际正文/邻接及末注root实际非作者POST通过；未复现。

- `SF-2026-ARXIV-2601-05543`（Experimental）：[TARS exact-v1](https://arxiv.org/html/2601.05543v1) §3.2–3.3/Eq2–7、§4.1–4.4。只采用 speech/text 输入子组中心化、当前正确 text reference 与无参考 fallback；7B、TTS QA、冻结 encoder/projector、MRR 原文本分母和 similarity 非 causal reasoning 边界保留。未运行代码/复现实验；root 必要 source→owner 写前核及实际正文/邻接写后非作者检查通过。
- `SF-2026-ARXIV-2601-05787`（Experimental）：[BEPA exact-v1](https://arxiv.org/html/2601.05787v1) §4.1–4.3/Eq5、§5.1 及 distribution-analysis protocol。只采用 plan-conditioned self-roll、verifier-success cache、全失败条件替换及刷新身份；去 plan 的训练条件变化不被 source identity 掩盖，旧策略分母不授 strict cache-behavior correction。128 solvability-selected 训练任务/241 held-out、54 expert-only 中19更新任务的诊断边界与额外专家/replay成本保留。未复现；root 写前必要 source→owner 核及实际正文/邻接写后非作者检查通过。
- `SF-2026-ARXIV-2601-05465`（Experimental）：[PRISMA exact-v1](https://arxiv.org/html/2601.05465v1) §3.3.1–3.3.2、§4.1、§4.3–4.4。只采用 frozen Planner/Solver→真实 trace-conditioned Inspector 的阶段分责及 recovered−regressed 净增；OARPO 非新 optimizer，teacher 标签/成功 trace mining 偏置及 Inspector 成本保留。作者多跳 QA/4H100/5次平均不授任意 do-no-harm、等总预算或生产能力。未复现；root 写前必要 source→owner 核及实际正文/邻接写后非作者检查通过。

- `SF-2026-ARXIV-2602-05885` — Daily `2026-02-07`；[Dr. Kernel exact-v1](https://arxiv.org/html/2602.05885v1) §3 KernelGym/hackcheck、§4 turn-level estimator、§5/Eqs6–9、§6配置/§7限制及Appendix A/B/D/E必要原段。原3+2+2=7，只采用geometric MRS稳定性、profiling reward与PRS接纳人口三接口分账；LOO条件复用本章已有论证，不采所有多轮无偏、PR等吞吐或覆盖即优化保证。额外profiling、筛选成本、奖励慢kernel风险、TRLOO仍不稳定与已有库合理性保留；工程identity/fallback是推断，未复现。root实际必要源/owner写前通过，并实际顺读513正文、497–520邻接与2267末注，非作者POST通过；日级Gate未验。

- `SF-2026-ARXIV-2601-05242` — Daily `2026-01-10`；[GDPO exact-v1](https://arxiv.org/html/2601.05242v1) §2/3.1 Eq4–6/3.2、§4.1五run及batch normalization消融。原2+1+2=5，per-criterion归一→加权合并→batch尺度的具体接口缺口深入；旧immediate/future标准化仍保留为另一来源分支，不冒称完整GDPO已有覆盖。不授所有信号必保留、零方差公式已实现、通用质量或无reward hacking；工程身份/回退为推断，未复现。root实际必要源与owner写前通过，feb01_v3实际正文1395–1417及本注非作者POST通过，仅写后范围不重复原源，日级Gate待验。

- `SF-2026-ARXIV-2602-05261` — Daily `2026-02-07`；[LUSPO exact-v1](https://arxiv.org/html/2602.05261v1) §4.2–4.4/Eq7–9、§5训练配置与Tables1–4。2+2+2=6，具体 ratio/outer-length gap 深入；只采用外乘固定采样长度与几何 ratio 的归一化分账，抵消仅限未clip分支的显式1/L，不采joint IS、无偏或所有长度偏差消除。Qwen2.5-7B/VL-7B用8H800、30B-A3B用32H800，max32K/4K、accuracy/format/overlong reward与clip配置绑定；同steps非同tokens/compute。DynaMath24.6低于GSPO25.9却Δ栏写+.7，隔离该定量子命题，保作者其他有限结果，不授全benchmark优势。未运行代码/复现；jan02_v3必要原源/owner写前核验通过，root授窄锁；jan02_v3已实际顺读489正文、482–495邻接与2263末注，非作者POST通过，日级Gate未验。

- `SF-2026-ARXIV-2602-05165` — Daily `2026-02-07`；[EBPO exact-v1](https://arxiv.org/html/2602.05165v1) §3/Eq2–4、§4理论及Appendix A/B Algorithm1。2+2+2=6，具体 online baseline gap 深入；只采用全局 reward/group-mean 两份累计状态、先并入当前 batch 再 shrinkage 与最终 batch center/scale 的分工。self-coupling、raw variance 含采样噪声与历史漂移边界保留，不采用全错组最终总负、必非零梯度、Gaussian MSE/一致性在任意任务成立或无坍塌保证。G32均值62.41低于GRPO62.91，AMC/MATH反侧、clustering额外16 rollouts/GPT4.1标签与checkpoint选择成本保留；硬件 Not Disclosed。未运行代码/复现；jan02_v3必要原源/owner写前核验通过，root授窄锁；jan02_v3已实际顺读375正文、357–377邻接与2265末注，非作者POST通过，日级Gate未验。

- `SF-2026-ARXIV-2602-04089` — Daily `2026-02-06`；[ORBIT exact-v1](https://arxiv.org/html/2602.04089v1) §2–5，尤其固定MDP/reset/retained history、§3 reward/GRPO与§4.2配置。原2+2+2=6，具体sampler gap深入，只采用同task多episode trace与测试冻结θ/跨episode输入分责；不采GRPO必不能dense、必防reward hacking或同总预算优势。三episode、受限文本任务、32K上下文及checkpoint/模型配置不同保留，未复现。root必要原源/owner写前通过，正文及源注经root实际顺读正文、前后邻接与末注，非作者POST通过，日级Gate未通过。

- `SF-2026-ARXIV-2602-03979` — Daily `2026-02-06`；[Likelihood-Based Reward Designs exact-v1](https://arxiv.org/html/2602.03979v1) §2/Eq2–18、§3.1–3.4、Appendix A.1/Eq19–23、A.2/A.4。6分具体 reward-contract gap 深入，仅采用参考答案似然尺度/长度权重与 current-θ reward 的直接导数分账；二项梯度非作者首创，不授似然等于 correctness、所有 reward 尺度等价或普遍 long-form 优势。两个3B模型/四datasets、greedy与sampled不同、CoT collapse与KL/长度/warm-start取舍保留；A.2 Base-RL 100/10/0 format reward 不与主文 binary 概述合并为唯一配方。未运行代码或复现。root必要源/owner差额及实际66/68两段与邻接/末注POST通过；日级Gate未验收。

- `SF-2026-ARXIV-2603-01162`：[exact-v1](https://arxiv.org/html/2603.01162v1) §3.1–3.2、§4.1–4.2、§5.1–5.2；Daily 2026-03-04，2+2+3=7。窄补已有 U-statistic 段的 estimator 身份及固定 N=BG 方差上界预算分账；不认证完整收敛/最优定理，不授标准化/clipped/IS/KL实现同一identity或 universal G。作者必要源/owner/邻接检查完成，root非作者必要源→实际正文/邻接POST通过；未复现实验。

- Daily 2026-03-07：[RLSTA exact-v1](https://arxiv.org/html/2603.04783v1) §5.1/Eq2、§5.2/Eqs4–5、§6/Table1、AppendixA.3/B。采用模型特定支持集与完整条件下对同一候选的 frozen-reference likelihood anchor；不采 reference likelihood 是真值或多轮错误均由惯性造成的因果断言。数学合成800条与3B～7B模型、匹配的GRPO/RLSTA预算及未过滤消融已核；代码/摘要训练方法预算不同，主动澄清不在验证范围。作者已写，root实际写后及邻接独立复核通过；未复现实验。

- Daily 2026-04-30：DORA [v1 §3/§4.2–4.4](https://arxiv.org/html/2604.26256v1) 的版本组/滑窗和 NeMo [v1 §2–3](https://arxiv.org/html/2604.26779v1) 的 detach draft-head 窄采用已由 apr29_close 独立 source→owner 通过；作者实写，root已实际读取正文及前后衔接，非作者写后通过。完整 trajectory 不豁免 GRPO membership，acceptance 不等 wall-clock，235B异步结果为投影。

- `SF-2026-ARXIV-2604-20209`（Experimental）：[exact-v1](https://arxiv.org/html/2604.20209v1)，必要方法、固定3,323个Lean目标/每题8尝试、guide与条件/冻结消融及限制。只采用自生成题支持集×可解率×相对奖励的控制压力；No Problem Conditioning/Frozen Conjecturer 同时去guide，不采用单部件纯因果或无界泛化保证。BF16、H200、8192长度的作者配置不是生产SLO；source→owner已独立核，实际正文已由apr24_close非作者写后核。日期原值与有界推定见04/23原始记录，未复现实验。

- Daily 2026-09-30，Experimental：[ProVer v1](https://arxiv.org/html/2609.36178v1) §3–5/Eqs2–4/Tables1–3仅支持judge提段、两端恢复＋fixed-policy continuation估值，不采用逐token因果归因或实际clipped更新无偏主张；[AdviSD v1](https://arxiv.org/html/2609.38142v1) §4–7/AppendixE仅支持predictive-not-causal advice决策选择与原GRPO advantage保持，fixed-teacher分析不扩为changing-teacher收敛。sep30_evidence_check已定点读精确原文并写入；未复现，正文/邻接待root非作者写后复核。

- `SF-2026-ARXIV-2604-22169`（Status: Experimental）：[ReCast exact-v1](https://arxiv.org/html/2604.22169v1) §2–4、§5.1/5.5、§6.2；只采用离线单目标 next-item、稀疏二元命中下的全零组目标派生 anchor 与搜索/actor 更新宽度分账。64 Ascend NPU、Qwen3-8B、`G=32` 的 step/actor 时间仅属同设置对照；anchor producer 与 rollout 不同，selection/off-policy 风险及强 backbone 修复反收益保留。04/27 作者必要源/邻章已核，root 对实际正文与前后衔接完成非作者写后复核；未复现实验，非整日报 Gate。

- `SF-2026-ARXIV-2604-22709`（Experimental）：[Abstract-CoT exact-v1](https://arxiv.org/html/2604.22709v1) §3.1–3.3、§4/Table 1、Appendix A；Daily 2026-04-27。采用保留离散码表、带 verbal-CoT 瓶颈 SFT→无 CoT self-distillation→受约束抽象码与答案联合 GRPO 的状态/动作分支，不采抽象码可解释或 token saving 等于总成本节约。受限 Qwen3 4B/8B、Granite 3B 中 cold RL-only 弱于 warm-up；Qwen3-8B MATH-500 的 warm-up+RL 90.8/144 tokens 低于 verbal SFT+RL 92.6/1671 tokens。reference policy 只在训练 KL 中使用，不写成推理状态；root 核原文并实写，apr20_resume 对实际修后句、证据边界与相邻交接独立 PASS；未复现实验，不代表日级 Gate。

- `SF-2026-ARXIV-2604-21160`：[exact-v1](https://arxiv.org/html/2604.21160v1) §3.3–3.5/Eq 6–16、§4.2/Table 3、§4.5；Daily 2026-04-24。仅吸收可解析几何字段的 char→token span、字段组内 advantage 与 background 分账；RPC 内部一致性非外部几何真值，GRCA-only IoU3D 低于 broadcast 的反例保留。malformed/跨字段/零方差的 admission 是工程要求，非作者已验证防御。root 已完成必要源→当前 owner 写前复核，且实际正文与相邻衔接写后非作者复核通过；未复现实验。

- `SF-2026-ARXIV-2604-16918`：[exact-v1](https://arxiv.org/html/2604.16918v1)，Daily 2026-04-21；§3.1–3.5、§4.3、F/Table5。采用 priority 生命周期、buffer sampling correction、behavior ratio 三对象分工；保留默认 IS 差异、衰减失效与成本，不声称年龄保证学习真值。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。
- `SF-2026-ARXIV-2604-16972`：[exact-v1](https://arxiv.org/html/2604.16972v1)，Daily 2026-04-21；§5.1–5.2/Eq7–15、§6/Table1–2。过滤零信号与有限已掌握行为的 consolidation 分账，p=1 须独立分支；非未来正确率硬保证、非全 compute 匹配，反向质量切片保留。apr02 必要 source→当前 owner 独立通过；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-14564`（Experimental）：[MARS² v1](https://arxiv.org/html/2604.14564v1)，Daily `2026-04-17`。采用 §2.1–2.4/Eq3、7–8/§3/Table1 的共享tree credit参照与各policy仅消费自身T_j的更新责任；完整解答树非执行prefix、shaping非无偏同目标、pass@8反例和非wall-clock匹配保留。复用 `V3_ORDINARY_TEN_FOUR_INDEPENDENT_AUDIT.md` §6有效必要source→owner PASS；本次root顺读完整正文及相邻交接写后PASS，未复现实验，不预支日级Gate。
- `SF-2026-ARXIV-2604-15148`（Experimental）：[IG-Search v1](https://arxiv.org/html/2604.15148v1)，Daily `2026-04-17`。采用 §2.1–2.4/Eq2–6/§3.3/Table2 的gold-conditioned document/refinement基线与query-only credit；随机批内非严格配对、proxy非truth/MI/纯query因果、controller成本及Bamboogle退步保留。复用 `V3_FINAL_BATCH_INDEPENDENT_AUDIT.md` 15148有效必要source→owner PASS；本次root顺读完整正文及相邻交接写后PASS，未复现实验，不预支日级Gate。

- `SF-2026-ARXIV-2604-13197`（Experimental）：[exact-v1](https://arxiv.org/html/2604.13197v1) §2.2、§3、§4.2–4.3。Sequence aggregate 的弱识别与另训 prefix scorer 分责，候选 TD 与采样 GAE 并存；prefix BCE 非校准 truth，2500 分支约 .64 AUROC / .0226 TD–单条 outcome correlation、Table6 退步和在线 RM 稳定性边界保留。不把未采样候选当已执行反事实或声称零 RM 成本。2+2+2=6，知识缺口深入；必要 source→owner 独立通过（apr02），实际写后待非作者核，未复现实验。

- `SF-2026-ARXIV-2604-12002`（Experimental）：[SD-Zero exact-v1](https://arxiv.org/html/2604.12002v1) §2.1–2.2/Eq1–4、§3.2–3.4、§4.1–4.2、C.1–C.2。Eq2 generation loss覆盖整串，teacher有外部 outcome 特权、阶段内冻结；KL/词汇变化非因果自知。采集/保留数量与 completion 预算非总计算匹配。6分实际缺口深入；必要来源/owner 独立复核通过（apr02），实际正文及相邻交接写后非作者复核通过（root、apr02）；未复现实验。

- `SF-2026-ARXIV-2604-09455`（Experimental）：[exact-v1](https://arxiv.org/html/2604.09455v1) §4.1–4.2/§5.1–5.3/Table3–4/AppendixC。expert分叉负adv停shared-prefix梯度，suffix保留更新/self池与mixed ratio，不宣称理论消歧或knowledge boundary。8A100；SFT bf16/4096/batch128/3epochs；RL n8+m8/k3/50warmsteps vs n16+m0/250poststeps，batch128/minibatch16/response8192/obs512/max4tools；tree-adv在AMC反收益，文字降幅与表不一致不采用。6分gap深入；必要源/owner非作者核通过（apr03），实际正文/相邻论证写后非作者复核通过（apr03），未复现实验/生产SLO。

- `SF-2026-ARXIV-2604-07853`：[QaRL exact-v1](https://arxiv.org/html/2604.07853v1) §2.2/3.1 Figure2、§3.2与§4 Table1。只采用 fake-quant 模拟/实际 GEMM、高精度 master/STE backward 与 materialized artifact 发布的数值身份区别；W4A16 不等 activation 低比特，不采 bitwise 等同。长度归一概率、ratio/log-domain clip 定义张力不用于 TBPO 保证，Table1局部退步保留。6分知识缺口深入；root 必要原文与实际写后独立核通过。

- `SF-2026-ARXIV-2604-08690`，Experimental：[exact-v1](https://arxiv.org/html/2604.08690v1) §3.1–3.2/Eq1–6、§4.1–4.3/Table2、AppendixC/D。Qwen2.5-Math-7B/Llama3.2-3B、dapo-math-17k、500steps、128prompts、G8、prompt1024/completion3072、bf16；upstream SPO历史baseline与downstream组相对更新不能混用。GPT5-nano只续写已正确轨迹，chat instruction近似raw-prefix continuation，不能作为learner真实信用证明。采用证据未披露训练GPU型号/完整并发SLO，不采用通用成本相等。本次必要原文与实际正文/相邻交接已由root独立复核通过，未复现实验。

- `SF-2026-ARXIV-2604-08926`，Experimental：[exact-v1](https://arxiv.org/html/2604.08926v1) §3.1–3.3/Eq4–19、§4.1–4.5/Table3、§7。Hard→多教师SFT、Mid→GRPO+on-policy pair GAL、Easy→跳过；理论噪声独立与教师bias条件未证明由共享group自然满足。Qwen2.5-Math-7B/Qwen3-4B-Base、16A80080GB、bf16、group8、8192 response cap、LR1e-6、AIME/AMC pass@32 与其他pass@1分开。Table3 dynamic grading在AMC有退步，不采用全部消融单调或普遍降variance；在线与教师预算不等免费。root 已完成必要原文与实际正文/相邻链路的写后独立复核，通过，本地实验未复现。

- SubSearch（Status: Experimental，SF-2026-ARXIV-2604-07415）：[官方 PDF v1](https://arxiv.org/pdf/2604.07415v1) §3.3 Eq5–9、§4.3/4.5、Appendix A/D。采用 outcome 成功时关闭过程代理的 residual 聚合；top-3 文档/子查询 embedding 是相似度代理，不保证语义穷尽或因果 credit。NQ/HotpotQA 合并训练、四 H100、prompt4096/response500/observation1200、base600/instruct200步，precision、部署并发/SLO未披露；中间奖励对 NQ 退步，保留额外 encoder/retrieval 成本。正文 Qwen3.2-3B 与图2/3 Qwen2.5-3B 名称不一致，不采用绑定特定模型的精确收益或跨配置比较。作者侧必要证据及正文已核，等待 root 非作者写后复核；并未运行实现或复现实验。

- `SF-2026-ARXIV-2604-08706`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.08706v1) §3–5.5、§4 Assumptions4.1–4.3与conditional optimal-design theorem。FIFO uniform/sharded replay，horizon N/R、reuse B/R与W/T不可混同；importance correction不消sample–iterate conditioning。Qwen3-0.6B/Qwen2.5-7B、OpenR1-Math/MATH，至少4seed、median/IQR、LR Pareto对照；compute ratio为active-GPU秒近似，wall-time单独测，过度reuse退步与后期collapse保留。资源/queue实现与更大模型不由此保证，正文不采用40%宣传或最优常数；未复现实验，本次写后独立复核通过（root）。

- `SF-2026-ARXIV-2604-07666`，Experimental：[exact-v1](https://arxiv.org/html/2604.07666v1) §3–5、§6.3及Limitations。采用有限噪声下可继续学习与错误结构分账，不采用跨任务15%容忍阈值、所有noise type等价或precision普遍最优的保证。MBPP/Qwen3/GLM4等配置、主要单seed与best/final差别保留；apr03已完成必要原文与正文的独立复核，未复现实验。

- `SF-2026-ARXIV-2604-04142`（Experimental）：[exact-v1](https://arxiv.org/html/2604.04142v1) §4.1–4.3、§5 与消融支持 reward/age buffer、序列 off-policy correction 与低噪声末段重生成的分工；SD3.5-M/Wan2.1-1.4B及作者 evaluator，较高 replay 比例发散。步数节省不是同硬件总时间/SLO保证，reward-selected mixture 不据此证明无偏。未复现实验；本次写后独立复核通过（root）。

- [2604.02869v1](https://arxiv.org/html/2604.02869v1)，Experimental；§3.1–3.2、Table1–2、§4/Table6–7。采用的是逐turn GN与raw-return先汇总后GN的非交换边界，不采用普遍零mismatch或单组件因果收益。作者Qwen3.5-4B/Qwen3-30B-A3B、8×H20 96GB、verl/Megatron；rollout prompt/response上限10K/45K、40turn、N=4、temperature=.9。不同训练配置与不同train/eval simulator需要分账，生产并发/SLO未披露。原始证据与章内差异由root审阅，apr03独立复核。

- `SF-2026-ARXIV-2605-06078`（Status: Experimental）：exact-v1 支持 ALFWorld、WebShop、ScienceWorld 离散文本动作环境中的
  milestone segmentation 与 dual-scale advantage；milestone 不是 causal credit，不覆盖 continuous control、Multi-Agent 或无显式 transition。
  Primary: https://arxiv.org/html/2605.06078v1
- `SF-2026-ARXIV-2605-06200`（Status: Experimental）：exact-v1 支持七个 QA benchmarks、三种 Qwen backbone、本地 Wikipedia
  retrieval 与 8×H20/VeRL 设置中的 turn-aware grouping；turn index 不证明 state equivalence，production async trajectory 未验证。
  Primary: https://arxiv.org/html/2605.06200v1

- [Does On-Policy Distillation Really Distill? v1](https://arxiv.org/html/2608.31046v1)：采用§3.1–3.2的low-logp与teacher-free fixed-advantage对照，结合§4.1、§5及Appendix A/C的entropy、预算和范围限制。作者观察支持“提升不能单独证明知识蒸馏”的归因反证；不采用固定负值/百分位为通用配置，也不从所测Qwen规模与任务推断所有教师无价值或探索边界扩张。

- [Locked at the Entrance, Open Inside](https://arxiv.org/html/2608.29188v1) 的 Countdown 受控实验区分自由采样访问与外置最小入口后的执行；一般数学的首计算只是 proxy，有限采样的未观察不证明零 support。采用 §3–7 与 Appendix A/B.2/I 的局部诊断，不采用“RLVR 必然坍塌”或摘要中的插值无损说法；Table 4 的置信区间不足以支持该等价结论。Source Family：`arxiv:2608.29188`，对应当前日报的精确版本证据笔记。

- `SF-2026-ARXIV-2602-22817`（Status: Experimental）：exact-v1 的 §4.1～4.2 定义 historical-context inconsistency 与 hierarchy-of-groups optimization，§5.1～5.5 给出作者环境的结果、参数分析和消融，Appendix A～C 固定算法与训练细节，§6 不证明任意历史表示可建立可比 group 或长程生产稳定性。https://arxiv.org/html/2602.22817v1

- `SF-2026-ARXIV-2606-22570` — primary `arXiv:2606.22570v1`；Method=`arXiv:2606.22570v1 §3 Analysis of Update Factors; §4 Algorithm`；Evaluation=`arXiv:2606.22570v1 §5 Experiments`；Non-proof=`arXiv:2606.22570v1 Appendix N Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。
- `SF-2026-ARXIV-2606-22716` — primary `arXiv:2606.22716v1`；Method=`arXiv:2606.22716v1 §3 Method and Reward Formalism`；Evaluation=`arXiv:2606.22716v1 §3.3 Experimental Setup; §4 Results`；Non-proof=`arXiv:2606.22716v1 §Limitations`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Training Language Models to Cooperate with Inference-Time Controllers（arXiv:2607.23771v1；Status: Experimental）：https://arxiv.org/html/2607.23771v1
  - 证据边界：支持 Llama-3.2-3B、GSM8K/MATH500/AMC23 与作者十二种 controller/composition 下的 controller-aware GRPO；不证明 controller-agnostic、跨任务或任意 protocol shift 的普遍收益。

- Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations（OPD 分布错配、长度聚合与能力边界；Status: Experimental）:
  https://arxiv.org/abs/2607.13399v1

- On-policy post-pruning recovery with failure-controlled horizon（Status: Experimental）:
  https://arxiv.org/abs/2607.13124v1

- UP（positive self-anchored ratio 与 asymmetric clipping；Status: Experimental）:
  https://arxiv.org/abs/2607.06987v1
- Single-Rollout Asynchronous Optimization（policy/value/freshness boundary；Status: Experimental）:
  https://arxiv.org/abs/2607.07508v1

- FP4 Explore, BF16 Train（precision-separated rollout artifact；Status: Experimental）:
  https://arxiv.org/abs/2604.06916
- SCOPE（outcome-routed adaptive OPD；Status: Experimental）: https://arxiv.org/abs/2604.10688

- SKILL0（Skill scaffold annealing；Status: Experimental）: https://arxiv.org/abs/2604.02268
- GrandCode（immediate reward、delayed correction 与 staleness；Status: Experimental）:
  https://arxiv.org/abs/2604.02721
- Self-Distilled RLVR（verifier-owned direction / teacher magnitude；Status: Experimental）:
  https://arxiv.org/abs/2604.03128

本章以 DeepSeekMath 原始 GRPO 为机制基线，补齐 group normalization、三样本计算、clipped ratio、sequence-to-token credit 与系统流水线；并用 R1-Zero→R1 的完整演进说明 pure RL、cold start、rejection sampling、general SFT 与第二轮 RL 各自解决的边界，不把其具体 recipe 泛化为所有 GRPO。

2026-W10 的 HACRL/HACPO 案例用于补全 cross-policy experience reuse 的 provenance、probability-coordinate
与 finite-batch bias contract。其理论无偏性依赖不可直接获得的 capability ratio，公开实验也不能证明异构
协作对任意任务成立；正文不保留作者成本或效果 headline，并明确它不是 inference-time Multi-Agent。

BandPO、HCAPO 与 MicroCoder-GRPO 分别用于补足 probability-aware trust region、hindsight relevance 的因果边界，以及 length/truncation/diversity 共同形成 curriculum 的机制；三者均保持 Experimental workload contract，不保留作者 benchmark headline。

Primary-source 校验入口：

- Zhihong Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models", 2024: https://arxiv.org/abs/2402.03300
- Arash Ahmadian et al., "Back to Basics: Revisiting REINFORCE Style Optimization for Learning from Human Feedback in LLMs", 2024: https://arxiv.org/abs/2402.14740
- Qiying Yu et al., "DAPO: An Open-Source LLM Reinforcement Learning System at Scale", 2025: https://arxiv.org/abs/2503.14476
- Zichen Liu et al., "Understanding R1-Zero-Like Training: A Critical Perspective", 2025: https://arxiv.org/abs/2503.20783
- MiniMax et al., "MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention", 2025
  （CISPO；technical-report evidence）: https://arxiv.org/abs/2506.13585
- Chujie Zheng et al., "Group Sequence Policy Optimization", 2025: https://arxiv.org/abs/2507.18071
- DeepSeek-AI et al., "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", arXiv v2 revised 2026: https://arxiv.org/abs/2501.12948
- Kimi Team et al., "Kimi k1.5: Scaling Reinforcement Learning with LLMs", 2025
  （partial-rollout system case）: https://arxiv.org/abs/2501.12599
- Zhixiang Zhou et al., "Heterogeneous Agent Collaborative Reinforcement Learning", 2026
  （Status: Experimental）: https://arxiv.org/abs/2603.02604
- Pierre Chambon et al., "Reinforcement Learning for Code Optimization"
  （Status: Experimental）, 2026: https://arxiv.org/abs/2607.25970
- OrchestrRL（Status: Experimental；physical compute scheduling + simulated reconfigurable fabric）:
  https://arxiv.org/abs/2601.01209
- StaleFlow（trajectory-level staleness protocol；作者实验边界）:
  https://arxiv.org/abs/2601.12784
- Jet-RL（training/rollout precision-flow consistency；作者实验边界）:
  https://arxiv.org/abs/2601.14243
- LongCat-Flash-Thinking-2601（multi-domain asynchronous RL；technical-report evidence）:
  https://arxiv.org/abs/2601.16725
- Fission-GRPO（execution-failure corrective branch；Status: Experimental）:
  https://arxiv.org/abs/2601.15625
- MAPPA（role-conditioned process reward；Status: Experimental）: https://arxiv.org/abs/2601.23228
- Sweet Spot Learning（terminal verifier + discretized proximity zones；Status: Experimental）: https://arxiv.org/abs/2601.22491
- Continual GUI Agents / GUI-AiF（sequential domain/resolution adaptation；Status: Experimental）: https://arxiv.org/abs/2601.20732
- Multi-Task GRPO（post-filtered gradient-mixture control；Status: Experimental）: https://arxiv.org/abs/2602.05547
- LUSPO（sequence-length weighting boundary；Status: Experimental）: https://arxiv.org/abs/2602.05261
- Flexible Entropy Control（dynamic clipping controller；Status: Experimental）: https://arxiv.org/abs/2602.09782
- Dr. MAS（role-conditioned normalization；Status: Experimental）: https://arxiv.org/abs/2602.08847
- iGRPO（best-draft-conditioned refinement；Status: Experimental）: https://arxiv.org/abs/2602.09000
- Blockwise Advantage Estimation（typed block credit；Status: Experimental）: https://arxiv.org/abs/2602.10231
- Beyond Correctness / RLTR（receiver-tested transfer reward；Status: Experimental）: https://arxiv.org/abs/2602.08489
- Experiential Reinforcement Learning（reflection-to-policy consolidation；Status: Experimental）: https://arxiv.org/abs/2602.13949
- DICE（executable CUDA verifier 与 curriculum；Status: Experimental）: https://arxiv.org/abs/2602.11715
- GLM-5 Technical Report（TITO、policy-version filtering 与 environment failure semantics；作者系统证据）:
  https://arxiv.org/abs/2602.15763
- ARLArena（multi-turn Agent RL contract；Status: Experimental）: https://arxiv.org/abs/2602.21534
- GUI-Libra（partial-verifiability policy update；Status: Experimental）: https://arxiv.org/abs/2602.22190
- SLATE（shared-prefix local credit；Status: Experimental）: https://arxiv.org/abs/2602.23440
- DSDR（correct-mode diversity；Status: Experimental）: https://arxiv.org/abs/2602.19895
- ACE（confidence-shifted negative correction；Status: Experimental）: https://arxiv.org/abs/2602.21420
- PyVision-RL（interaction-budget reward；Status: Experimental）: https://arxiv.org/abs/2602.20739
- Tool-R0（co-evolving curriculum and solver roles；Status: Experimental）: https://arxiv.org/abs/2602.21320
- EMPO²（temporary memory scaffold and policy internalization；Status: Experimental）:
  https://arxiv.org/abs/2602.23008
- CUDA Agent（executable kernel environment and staged warm-up；Status: Experimental）:
  https://arxiv.org/abs/2602.24286
- BandPO（Status: Experimental）: https://arxiv.org/abs/2603.04918
- Hindsight Credit Assignment Policy Optimization（Status: Experimental）: https://arxiv.org/abs/2603.08754
- MicroCoder-GRPO / Breaking Training Bottlenecks（Status: Experimental）: https://arxiv.org/abs/2603.07777
- Code-A1（co-evolving code/test policies；Status: Experimental）: https://arxiv.org/abs/2603.15611
- TRUST-SQL（phase-specific Agent credit；Status: Experimental）: https://arxiv.org/abs/2603.16448
- Complementary Reinforcement Learning（actor/extractor co-evolution；Status: Experimental）:
  https://arxiv.org/abs/2603.17621
- Nemotron-Cascade 2（staged domain RL 与 on-policy distillation；作者实验边界）:
  https://arxiv.org/abs/2603.19220
- ProRL Agent（rollout service boundary；Status: Experimental）: https://arxiv.org/abs/2603.18815
- Reintroducing Markov States（explicit environment state；Status: Experimental）:
  https://arxiv.org/abs/2603.19987
- On the Direction of RLVR Updates（Status: Experimental；signed token update direction）:
  https://arxiv.org/abs/2603.22117
- Sparse but Critical（Status: Experimental；distribution divergence 与 bounded intervention）:
  https://arxiv.org/abs/2603.22446
- CCPO（Status: Experimental；role-level counterfactual credit）: https://arxiv.org/abs/2603.21563
- UniGRPO（Status: Experimental；text/flow joint trajectory 的 typed credit）:
  https://arxiv.org/abs/2603.23500
- PEPO（Status: Experimental；perception/exploration token credit）: https://arxiv.org/abs/2603.22847
- Composer 2（Versioned Vendor Evidence；asynchronous multi-scaffold policy identity）:
  https://arxiv.org/abs/2603.24477
- KAT-Coder-V2（Status: Experimental；turn-ratio、MoE estimator 与 tree trajectory training）:
  https://arxiv.org/abs/2603.27703
- DRPO（Status: Experimental；越界后仍保留有界纠正信号）: https://arxiv.org/abs/2606.09821
- APPO（Status: Experimental；共享前缀后的 decision-branch counterfactual credit）:
  https://arxiv.org/abs/2606.12384
- OPD²（matched-base policy-delta distillation；Status: Experimental）:
  https://arxiv.org/abs/2607.15161
- P-OPD（proxy relative-update artifact 与 primary acceptance；Status: Experimental）:
  https://arxiv.org/abs/2607.11505v1
- Multi-turn dual reward normalization（immediate / future-return branch；Status: Experimental）:
  https://arxiv.org/abs/2607.11070v1
- Provenance-guided earliest-exposure credit（relevance 不是 causal credit；Status: Experimental）:
  https://arxiv.org/abs/2607.11172v1
- When Does Muon Help Agentic Reinforcement Learning?（optimizer/update-scale/sharding contract；
  Status: Experimental）: https://arxiv.org/abs/2607.16169
- CROP（paraphrase-calibrated counterfactual relevance for selective OPD；Status: Experimental）:
  https://arxiv.org/abs/2608.13387
- R2-OPD（reasoning-progress-aware segment masking；Status: Experimental）:
  https://arxiv.org/abs/2608.19408

W32 primary-source cases：

- SMRC-SD（state-matched contextual distillation；Status: Experimental）: https://arxiv.org/abs/2608.05219
- PIRL（prompt-robust multimodal RLVR；Status: Experimental）: https://arxiv.org/abs/2608.08802
- Intern-S2-Preview technical report（partial rollout、online draft、typed process credit；No Change /
  Source-family synthesis）: https://arxiv.org/abs/2608.13505
- SEED（policy-synchronous hindsight skill distillation；Status: Experimental）:
  https://arxiv.org/abs/2607.14777
- Distilled Reinforcement Learning（positive-advantage teacher weighting / negative reset；Status: Experimental；受限 math/code recipe）:
  https://arxiv.org/abs/2607.17247v1
- Stale but Stable / SAT（exact v1；Status: Experimental）：https://arxiv.org/html/2607.18722v1
  - 证据边界：Qwen3-30B-A3B 数学 RL、30,712 prompts、4096 responses/iteration、544 iterations、lag 1/8；event-time GradLoc repo commit 早于论文，不能证明 SAT artifact 已公开。

### Daily integration evidence trace

<!-- daily-books-trace:SF-2026-ARXIV-2607-25369:start -->
- `SF-2026-ARXIV-2607-25369` — Daily [2026-07-29](../../papers/2026/07/29/README.md)；primary `arXiv:2607.25369v1`；正文锚点“跨步骤依赖需要保留 Episode Identity”。本章吸收 episode-preserving sampler、stage-local reward 与有界 episode credit 的组合边界；单数据集、单模型和单卡实验不证明 reward broadcast 是逐步因果 attribution。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25369:end -->

#### Source-specific Review notes

- SF-2026-ARXIV-2606-25178: `arXiv:2606.25178v1`; exact-v1 URL=`https://arxiv.org/html/2606.25178v1`; Method=`https://arxiv.org/html/2606.25178v1 — §3 Method; Gradient-Based Transferability; Curriculum Algorithm`; Evaluation=`https://arxiv.org/html/2606.25178v1 — §4 Experiments; B Implementation/Evaluation Details`; Non-proof=`六域、Qwen3-1.7B/Llama3.2-3B 与 <1% overhead 不证明更大模型、non-verifiable reward 或 adversarial domain；gradient conflict 不稳定时回退 proportional/hand-designed mix。`; Artifact=`Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26027**：Primary `arXiv:2606.26027v1`；Method `https://arxiv.org/html/2606.26027v1 — §4 Method; 4.2 catastrophic collapse; 4.4 supervisory fixes`；Evaluation `https://arxiv.org/html/2606.26027v1 — §5 Experiments; 5.1 Dataset and Models; D Detailed Evaluation`；未证明边界 `https://arxiv.org/html/2606.26027v1 — §B Training Details; C Qwen3 Training; E Training Dynamic`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-05—08）

<!-- daily-books-trace:SF-2026-ARXIV-2605-06078:start -->
- `SF-2026-ARXIV-2605-06078` — Daily `2026-05-08`；primary `arXiv:2605.06078v1`；Books review `books-review:SF-2026-ARXIV-2605-06078`。

  **已吸收的语义增量：** Milestone boundary 作为 terminal reward 与逐 action causal credit 之间的中间粒度，并冻结 environment-owned milestone identity。
<!-- daily-books-trace:SF-2026-ARXIV-2605-06078:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2605-06200:start -->
- `SF-2026-ARXIV-2605-06200` — Daily `2026-05-08`；primary `arXiv:2605.06200v1`；Books review `books-review:SF-2026-ARXIV-2605-06200`。

  **已吸收的语义增量：** `(prompt, turn-index)` 可作为 process-credit 的受限 grouping key，但不能冒充真实 state equivalence；membership 与 optimizer 权限必须分离。
<!-- daily-books-trace:SF-2026-ARXIV-2605-06200:end -->

<!-- daily-books-trace:SF-DEEP-RESEARCH-RUBRIC-RL:start -->
- `SF-DEEP-RESEARCH-RUBRIC-RL` — Daily `2026-06-02`；primary `arXiv:2606.01091v1`；正文锚点“Evidence-derived Rubric 是版本化 Reward State”。

  **已吸收的语义增量：** DR-Rubric retrieves external evidence, synthesizes atomic verifiable constraints, scores policy outputs against that rubric, and feeds the result into group-relative reinforcement learning; rubric provenance, granularity, bootstrap version, and polarization therefore become reward-state and stopping-contract inputs rather than free-form judge text. 证据边界：Results are bounded to the reported research-agent tasks, models, search environment, and bootstrap depth; external evidence may be incomplete or stale, generated constraints can be wrong, and later bootstrap steps polarize and collapse rather than guaranteeing self-improvement.
<!-- daily-books-trace:SF-DEEP-RESEARCH-RUBRIC-RL:end -->

<!-- daily-books-trace:SF-STRAGGLER-AWARE-RL-GROUP:start -->
- `SF-STRAGGLER-AWARE-RL-GROUP` — Daily `2026-06-02`；primary `arXiv:2606.02218v1`；正文锚点“同步 Group Size 也可以由 Straggler Risk 有界调节”。

  **已吸收的语义增量：** 增加在保持同步 on-policy 下按 posterior straggler risk 动态选择 group size。
<!-- daily-books-trace:SF-STRAGGLER-AWARE-RL-GROUP:end -->

<!-- daily-books-trace:SF-ASYMPO:start -->
- `SF-ASYMPO` — Daily `2026-06-03`；primary `arXiv:2606.03070v1`；Books Decision=`No Change — Existing Coverage`；命题锚点“正负 Advantage 不必共享同一 Clipping Contract”“Asynchronous RL 必须把 Policy Staleness 写进 Advantage”。

  当前正文已经把 current-policy positive branch、behavior-bounded negative branch、stale rollout 风险和标准对称 clipping fallback 写成完整机制；该 family 不再触发新增正文。
<!-- daily-books-trace:SF-ASYMPO:end -->


<!-- daily-books-trace:SF-2026-ARXIV-2606-15455:start -->
- `SF-2026-ARXIV-2606-15455` — Daily `2026-06-14`；primary `arXiv:2606.15455v1`；Books review `books-review:SF-2026-ARXIV-2606-15455`。

  **已吸收的语义增量：** RLVR 的 diversity collapse 应按 problem saturation/overtraining 解释，并用 zero-success/boundary contribution gate 决定哪些题继续更新。
<!-- daily-books-trace:SF-2026-ARXIV-2606-15455:end -->


<!-- daily-books-trace:SF-2026-ARXIV-2606-21090:start -->
- `SF-2026-ARXIV-2606-21090` — Daily `2026-06-18`；primary `arXiv:2606.21090v1`；Books review `books-review:SF-2026-ARXIV-2606-21090`。

  **已吸收的语义增量：** post-training control loop 应分别持有 campaign-level memory、within-campaign early stop 与 optimizer；峰值 checkpoint 必须先于最终 collapse 被保存和晋级。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21090:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-21884:start -->
- `SF-2026-ARXIV-2606-21884` — Daily `2026-06-21`；primary `arXiv:2606.21884v1`；Books review `books-review:SF-2026-ARXIV-2606-21884`。

  **已吸收的语义增量：** 对 deterministic generator 构造 solver-grounded CoT 后，区分 forward-derivable procedure 与 information-free backtracking search；不可忠实前向化的 search 应外置为 catalog/search，再让模型做 bounded verification。
<!-- daily-books-trace:SF-2026-ARXIV-2606-21884:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22043:start -->
- `SF-2026-ARXIV-2606-22043` — Daily `2026-06-21`；primary `arXiv:2606.22043v1`；Books review `books-review:SF-2026-ARXIV-2606-22043`。

  **已吸收的语义增量：** multimodal RLVR 的 answer reward 会先强化语言 shortcut，再在足够视觉证据/奖励强度下发生 watching transition；应监控 visual reliance 并在形成窗口干预。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22043:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-22164:start -->
- `SF-2026-ARXIV-2606-22164` — Daily `2026-06-21`；primary `arXiv:2606.22164v1`；Books review `books-review:SF-2026-ARXIV-2606-22164`。

  **已吸收的语义增量：** 多轮 RL 的难度由 decision density ρ 而非 raw horizon 单独决定；routine reward-equivalent turns 给 trajectory estimator 增方差但不增期望 signal，低 ρ 时需要 turn-level critic/credit。
<!-- daily-books-trace:SF-2026-ARXIV-2606-22164:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-06987:start -->
- `SF-2026-ARXIV-2607-06987` — Daily `2026-07-09`；primary `arXiv:2607.06987v1`；Books review `books-review:SF-2026-ARXIV-2607-06987`。

  **已吸收的语义增量：** 新增证据边界：For positive advantages, UP replaces the stale rollout ratio with πθ divided by a stop-gradient copy of itself. Its forward value is one while its gradient is the current-policy REINFORCE gradient, so the positive branch no longer hits the usual upper clipping ceiling. The negative branch retains a conventional bounded ratio/KL safeguard, making the change asymmetric rather than removing stability controls globally. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L151`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-06987:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11070:start -->
- `SF-2026-ARXIV-2607-11070` — Daily `2026-07-14`；primary `arXiv:2607.11070v1`；Books review `books-review:SF-2026-ARXIV-2607-11070`。

  **已吸收的语义增量：** 新增证据边界：DC-GRPO decomposes centered discounted return into separately normalized immediate-reward and future-return deviations, then recombines them so turns do not inherit one undifferentiated trajectory advantage. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11070:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11172:start -->
- `SF-2026-ARXIV-2607-11172` — Daily `2026-07-14`；primary `arXiv:2607.11172v1`；Books review `books-review:SF-2026-ARXIV-2607-11172`。

  **已吸收的语义增量：** 新增证据边界：A verifier maps each supported atomic evidence item to the earliest search/read step that exposed the cited document; sign-preserving modulation amplifies credited positive steps and shields them from uniform negative penalty. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11172:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-11505:start -->
- `SF-2026-ARXIV-2607-11505` — Daily `2026-07-14`；primary `arXiv:2607.11505v1`；Books review `books-review:SF-2026-ARXIV-2607-11505`。

  **已吸收的语义增量：** 新增证据边界：A smaller proxy explores with GRPO; relative policy update signals are extracted, anchor-calibrated across model scales and applied to a larger primary with a signal-guided objective. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-11505:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13124:start -->
- `SF-2026-ARXIV-2607-13124` — Daily `2026-07-16`；primary `arXiv:2607.13124v1`；Books review `books-review:SF-2026-ARXIV-2607-13124`。

  **已吸收的语义增量：** 新增证据边界：On-policy distillation evaluates a frozen pre-pruning teacher on student samples; repetition/truncation feedback and two EMAs shrink early horizons then restore long generation as recovery improves. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13124:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-13399:start -->
- `SF-2026-ARXIV-2607-13399` — Daily `2026-07-16`；primary `arXiv:2607.13399v1`；Books review `books-review:SF-2026-ARXIV-2607-13399`。

  **已吸收的语义增量：** 新增证据边界：OPD is an exploration catalyst on student-owned on-policy states, not a capacity creator; teacher/student mismatch and length aggregation can corrupt the guidance signal. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-13399:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14777:start -->
- `SF-2026-ARXIV-2607-14777` — Daily `2026-07-17`；primary `arXiv:2607.14777v1`；Books review `books-review:SF-2026-ARXIV-2607-14777`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: sparse outcome RL/static skills -> policy-synchronous hindsight-skill on-policy distillation 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14777:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-17247:start -->
- `SF-2026-ARXIV-2607-17247` — Daily `2026-07-20`；primary `arXiv:2607.17247v1`；Books review `books-review:SF-2026-ARXIV-2607-17247`。

  **已吸收的语义增量：** 新增证据边界：outcome-only RL/unconditional OPD -> sign-authorized teacher weighting 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-17247:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-18722:start -->
- `SF-2026-ARXIV-2607-18722` — Daily `2026-07-22`；primary `arXiv:2607.18722v1`；Books review `books-review:SF-2026-ARXIV-2607-18722`。

  **已吸收的语义增量：** 新增证据边界：SAT derives a detached sampled log-ratio, computes a batch-relative high-tail quantile, and contracts only the sign-selected outward side of PPO's interval. It is a drop-in sampled-surrogate change: the adaptive interval is contained in PPO's, pull-back updates are unchanged, and the objective differs only in the newly clipped outward band. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-18722:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-23771:start -->
- `SF-2026-ARXIV-2607-23771` — Daily `2026-07-28`；primary `arXiv:2607.23771v1`；Books review `books-review:SF-2026-ARXIV-2607-23771`。

  **已吸收的语义增量：** 新增证据边界：Multi-controller sampling and turn-level GRPO train the policy against a vocabulary of inference-time controller/module compositions. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1115`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-23771:end -->

- `SF-2026-ARXIV-2604-18892`（Experimental）：[exact-v1](https://arxiv.org/html/2604.18892v1)，Daily 2026-04-22；§3.1–3.3/Eqs1–8及§4.3。正确子集tie-aware居中与完整GRPO组advantage分责，Eq7零/单correct辅助归零；text-only judge不是visual truth/因果credit，负aux不是总reward负。Qwen2.5-VL7B/ViRL/rollout8及五benchmark各500；任务退步、judge额外成本及hardware/precision/SLO未披露保留。6分具体缺口深入，root必要源/actual owner/literal独立采用通过；apr01 已顺读实际正文及前后交接并通过写后复核，见 [04/22 写后记录](../../papers/2026/04/_sources/daily-20260422/V3_APR01_18892_WRITE_AFTER.md)；未复现实验。

<!-- daily-books-trace:SF-2026-ARXIV-2605-02178:start -->
- `SF-2026-ARXIV-2605-02178` — Daily `2026-05-05`；primary `arXiv:2605.02178v1`；Books review `books-review:SF-2026-ARXIV-2605-02178`。

  **写回边界：** exploration progress 只获得 token-level intervention 与 turn-level resample/cancel 的采样控制权；group builder 必须冻结最终 membership，uncertainty 不得冒充 outcome verifier，late-reward 或校准不足时回退完整 rollout。
<!-- daily-books-trace:SF-2026-ARXIV-2605-02178:end -->

- `SF-2026-ARXIV-2603-02637` — Daily `2026-03-05`；[StitchCUDA exact-v1](https://arxiv.org/html/2603.02637v1) §3.2.1–3.2.2/Eq2、§4.2–4.3、Appendix C.1.1/C.2.1/C.3–C.4。6分具体知识缺口深入；采用单轮生成/反馈修复支持集与 correct/nonhack/rubric 分责，不采用无 reward hacking、任意程序正确或 surrogate 等价保证。Qwen3-32B、400样本、LoRA128/group8，测试最多15轮best runtime；无rubric同数据/参数却增加128→160 H200-hour估算/计量预算，完整15轮基线耗时为估算。正文训练约4GPU×20h与AppC160h口径不统一，不作统一降本比。作者必要源与窄正文/邻接检查完成；root已实际对读必要原文、新增两段与邻接，非作者POST通过，未复现或审读artifact。

- `SF-2026-ARXIV-2512-24618` — Daily `2026-01-02`；[Youtu-LLM exact-v1](https://arxiv.org/html/2512.24618v1) §4.2.2/Fig13及CF-GRPO公式。7分只采用prompt-level drift整组admission→条件 \(P(X\mid K<\tau)\) 目标，与importance correction分离。有限估计、拒收切片及丢样/重采成本保留；原节未给硬件、group数值与完整消融预算，不采用普遍FP16优势、原人口无偏或收敛保证。未运行代码或复现实验；root非作者已实际核必要原源、两段正文及前后衔接，写后通过。

- `SF-2026-ARXIV-2602-03507` — Daily `2026-02-05`；[FaithRL exact-v1](https://arxiv.org/html/2602.03507v1) §3.1–3.2、§4.2.2/Eq10及结果表、§5.5与必要A.6/G.1/G.3。6分具体gap深入仅采用signed advantage对evidence-supported span的方向性权重；gold decomposition/数学参考steps属离线条件，外部attribution不认证内部faithfulness。Qwen MuSiQue正确率75.7低于GRPO79.4，THS面积改善不是全Pareto；不把idealized evidence⇔answer或Appendix轨迹公式授为tokenwise GRPO必无幻觉。未复现；root已实际核必要源/owner及195行正文/187–202邻接与末注，写后复核通过；日级Gate待验。

- `SF-2026-ARXIV-2602-03025` — Daily `2026-02-05`；[RC-GRPO exact-v1](https://arxiv.org/html/2602.03025v1) §3.1–3.3/Eq、§4.3 Tables2/3/Q4。6分具体gap深入仅采用RCTP接口预训练、固定mode混采与同verifier/group normalization/current-old同mode ratio分账；部署high mode不等混合分布或全成功。期望variance假设不授每组非零/无偏，Table3无RCTP反侧和额外轨迹准备成本保留，entropy因果不采；未运行代码/复现。root已实际核必要源与owner及394行正文、387–401邻接与末注，写后POST通过；日级Gate待验。

- `SF-2026-ARXIV-2512-24873` — Daily `2026-01-02`；[Let It Flow: Agentic Crafting on Rock and Roll — Building the ROME Model within an Open Agentic Learning Ecosystem exact-v1](https://arxiv.org/html/2512.24873v1) §3.2.4.1–4/Eq5–7与rollback/anchor位置、§3.3.1。6分具体chunk-credit gap深入，仅承载chunk discount、几何均值非完整概率比、mismatch筛选人口与teacher prefix训练权限/预算；不授无偏off-policy、scale均衡、部署可得正确prefix或配方单机制因果收益。未运行代码；root必要源/owner写前通过，实际正文/邻接写后经root非作者实际复核通过。

- `SF-2026-ARXIV-2512-24271` — Daily `2026-01-02`；[Taming Hallucinations: Boosting MLLMs’ Video Understanding via Counterfactual Video Generation exact-v1](https://arxiv.org/html/2512.24271v1) §4.2/Eq6/8/9、alpha重权、§5/Tables3–4与B.10–15。6分paired-domain proxy gap深入，L1优势等权不授真实gradient等权、binary/format条件分账；Eq9/B10乘G与B15除G冲突隔离实现权限，同G比率可消不否全部经验。未运行代码；root必要原源/owner通过，实际正文/前后邻接及末注写后经root非作者复核通过。

- `SF-2026-ARXIV-2602-04284` — Daily `2026-02-06`；[AgentOmit exact-v1](https://arxiv.org/html/2602.04284v1) 必要方法、训练与直接反侧。原2+2+2=6，具体original-view omit决策与compressed successor概率账gap深入；counterfactual preparation、observation loss mask与正确性筛选分权。Eq4零概率/优化reference不授最优policy KL或无reward hacking；不采未对齐预算的headline。部署view/old-logprob guard为工程推导，未声称作者已验证。未运行代码/复现；jan01_v3实际必要原源/owner写前通过，root授窄锁；root实际新增正文/前后邻接及末注POST通过，日级Gate未验。

- `SF-2026-ARXIV-2601-07182` — Daily `2026-01-14`；[PRPO exact-v1](https://arxiv.org/html/2601.07182v1) §3/4/6/7、Appendix B/C。2+2+2=6，只采用entropy分段PRM局部项与outcome trajectory shift分责；固定0.5/0.289是uniform prior尺度非实际概率校准，entropy峰非语义oracle，不采用未完成的collapse保证。8H200policy+8H200PRM，batch128/8rollouts/2048tokens、MATH12k，early-stop epochs不同；MATH greedy与AMC/AIME32次平均不同人口。random/uniform分段反侧、AIME2025反退及step46.8→80.8/84的PRM成本保留，非同总预算普胜；精度、完整成本未披露。未运行代码/复现；root 必要原源与实际 owner 写前通过，root 已实际顺读正文/前后邻接/末注，非作者 POST 通过，日级 Gate 待验。

- `SF-2026-ARXIV-2601-08763` — Daily `2026-01-15`；[Rewarding Rare exact-v1](https://arxiv.org/html/2601.08763v1) §3.2–3.4/Eq4–5、§4.4/Table1与Limitations。2+1+2=5，具体signed advantage局部簇频率重权gap深入；不授全局新颖性、语义entropy、正确稀有样本专属bonus或token credit。Qwen2.5-7B/Qwen3-8B/Olmo3-7B与较大judge、rollout8；20题coverage对照INSTRUCT非GRPO，聚类误差、分组依赖与judge成本保留，完整训练成本未披露。未运行代码/复现；root必要原源/现owner写前通过并授窄锁，作者已核实际两段及前后交接，root已实际核正文、前后交接与末注，非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-08274` — Daily `2026-01-15`；[DART exact-v1](https://arxiv.org/html/2601.08274v1) §2.1–2.2/Eq1–7、§5.2–5.4/Table2、AppA3/A4。2+2+2=6，tool-hint conditional-tree credit gap深入；不授iidGRPO、工具因果真值、Eq7完整梯度实现或普胜。15叶估值/8训练sample非同总compute、GPQA扩大树反退及sandbox截断保留；未运行代码或复现。root必要原源/现owner写前通过并授窄锁，root实际正文/前后邻接及末注非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2601-09085` — Daily `2026-01-16`；[exact-v1](https://arxiv.org/html/2601.09085v1)，必要原段见本日PRIMARY/EVIDENCE。5分MMR改变reward而非过滤的具体gap深入；同correctness组亦可能新advantage，std/sigmoid依reward尺度。Embedding成本、后验peak预算与1.5B反侧保留，不采scale-invariant/无配置成本或70%收益保证。root必要源/owner写前通过，root actual正文/邻接与末注POST通过，λ措辞单点亦实际确认，锁释放；未运行artifact或复现。

- `SF-2026-ARXIV-2602-06422` — Daily `2026-02-10`；[TurningPoint-GRPO exact-v1](https://arxiv.org/html/2602.06422v1) §5.1–5.3/§6.1–6.3/Table1与AppB/C/D。6=2+2+2，inner critic之外ODE-completed endpoint差额与terminal替换的具体gap深入；不授ODE条件均值、无偏或causal credit。32H20/SD3.5M LoRA/512/train10-test40/G24、KL/无KL人口、window4/噪声反侧及额外sampling/reward成本分开；precision/seed/SLO未披露，未核artifact或复现。root必要原源/owner写前通过，root实际L255–274正文邻接及末注2711非作者POST通过，锁释放；不授日级Gate。

- `SF-2026-ARXIV-2601-10094` — Daily `2026-01-17`；[V-Zero exact-v1](https://arxiv.org/html/2601.10094v1) §3.2–3.3/4.1–4.3/§6及A1–3。6分双track课程提案与filtered pseudo-label具体gap深入；同源票数/格式不授真值，3B轮2退步与4K/额外feedbackGPU/rollout成本近正文。未核实现或复现；root必要原源/owner写前通过，root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-10201` — Daily `2026-01-17`；[PRL exact-v1](https://arxiv.org/html/2601.10201v1) Algorithm1、Table4/5/6。7分仅采用 current-policy stopgrad suffix-logratio credit 控制接口；非 PRM/最优恒等或未核 AppendixA proof，body beta 与算法 KL0、粒度反退/配置成本近正文。未核实现或复现；root必要原源/owner写前通过，root实际两段/前后邻接及末注非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-09981` — Daily `2026-01-17`；[DR2Seg exact-v1](https://arxiv.org/html/2601.09981v1) §3.3 Eq1–8、§4.1–4.3/Table3–6。2+2+2=6，conditional description reward 的具体 gap 深入；second pass用gold，不授faithfulness因果或线上verification，length绝对anchor/group全失败disable及局部退步、训练双pass费用相邻。不采§3.4宽理论。未核实现或复现；root必要原源/owner写前通过，root已实际核两段/前后邻接与末注，非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2601-09609` — Daily `2026-01-16`；[DPWriter exact-v1](https://arxiv.org/html/2601.09609v1) §4–6/Table1–3/AppA。2+2+2=6，分段 expand/select sampler lineage 与 gated diversity reward 的具体 gap 深入；选后 group 非 iid、likelihood ratio 不授原目标无偏，规划格式/SFT/完整候选与 embedding 成本及局部反侧相邻。不授生成语义等价、普遍创造力或免费分支；未核 artifact/复现。root 必要源/owner写前通过；实际两段与前后邻接L565–586及本末注由 root 非作者 POST 通过，窄锁释放；日级 Gate 未授。

- `SF-2026-ARXIV-2602-06462` — Daily `2026-02-10`；[DiSPO exact-v1](https://arxiv.org/html/2602.06462v1) §3/Alg1、§4与A1.1必要归一化/采样条件、§5.1–5.6 Tables1–3及AppB配置。6=2+2+2，冻结masked-state全填支路与仅actionable位置credit的具体gap深入，仅采用Experimental经验接口；不授实际policy-gradient无偏/普遍variance theorem，surrogate normalization/branch law/group-baseline条件未桥接，理论子命题不采用。LoRA128/alpha64、4H10094GB、256tokens局部任务；更多Z/部分任务反退、约0.4倍吞吐与额外reward/surrogate成本近正文，Sudoku wallclock不外推全任务。seed/precision/完整配置未披露，未核实现或复现。root必要原源/当前owner写前通过并授窄锁，root实际正文L2269/2271、前后2258–2277与末注2741非作者POST通过，锁释放；不授日级Gate。

- `SF-2026-ARXIV-2602-06717` — Daily `2026-02-10`；[F-GRPO exact-v1](https://arxiv.org/html/2602.06717v1) §3.1/Eq9–11、§3.2/4、Table3与AppF2/H/I。6分深入仅采用固定policy/iid二值采样中mixed availability与同prompt rare-correct coverage的概率区别及评价分账，不授共享参数长期收敛或真实tail标签认证。Focal成功率重权只是受限案例：pass@1/pass@256非单调，基础模型NLL代理、γ搜索与额外采样成本保留；16H100数学实验不作同总预算普胜。未运行代码/复现；root必要源/具体owner写前通过，root已实际顺读两段正文、前后邻接与末注，非作者POST通过，窄锁释放；日级Gate未授。

- `SF-2026-ARXIV-2602-09578` — Daily `2026-02-12`；[FlexMARL exact-v1](https://arxiv.org/html/2602.09578v1) §3–4、Table2/3、§8.1–8.2/8.6–8.7、§9。2+2+3=7，仅采用完整 group/reward 条件下 microbatch 梯度提前与 global optimizer commit 的分界；不授数值等价、任务质量/收敛或跨硬件稳定性。root 必要 source→owner 写前核通过授窄锁；root 已实际核正文、前后邻接及本末注，非作者 POST 通过，窄锁释放。未运行代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-10090` — Daily `2026-02-12`；[AWM exact-v1](https://arxiv.org/html/2602.10090v1) §3.3.1、Table6/7、B.2、Limitations。2+1+3=6，具体 reward/context 缺口深入，仅采用幂等 no-op false-negative、wrong-entity false-positive 与 history-limit 训练评估对齐；hybrid 非全项严格更优，Table7 仅 4B，runtime repair 不授语义真值。root 必要 source→owner 写前核通过授窄锁；root 已实际核正文、前后邻接及本末注，非作者 POST 通过，窄锁释放。未复现，非日级 Gate。

- `SF-2026-ARXIV-2602-09598` — Daily `2026-02-12`；[ELPO exact-v1](https://arxiv.org/html/2602.09598v1) §4.1–4.4/Alg1、C/E/F及必要评价/限制。2+2+3=7，仅采用有限 recoverability 二分提案、branch/trajectory credit 与 critical-suffix lower clip；不授真实 first-error、无解边界、同 rollout 等总预算或稳定性，表文矛盾保留。root 必要 source→owner 写前核通过并授窄锁；root 已实际核两段、邻接及本末注，非作者 POST 通过，窄锁释放。未运行代码/复现，非日级 Gate。

- `SF-2026-ARXIV-2601-15625` — Daily `2026-01-24`；[Fission-GRPO v1](https://arxiv.org/html/2601.15625v1) §3.3/4.1/4.4–4.6，7分必要深入。采用失败轨迹与诊断feedback改变current-policy重采group条件，与prompt-only replay/peer-conditioned OPD分责；GT simulator是训练特权、LIFO非严格on-policy、额外rollout成本近正文。root 必要原源/owner写前通过并授窄锁，正文L447/前后邻接与末注root POST通过、锁释放；未核代码或复现。

- `SF-2026-ARXIV-2602-09331` — Daily `2026-02-12`；[Counterfactual Credit exact-v1](https://arxiv.org/html/2602.09331v1) §3–5/Tables1–3/7/A。2+2+2=6，具体owner差额深入：span placeholder原answer概率drop重权原advantage，OOD dependency非causal/正确性；负adv与forward32–74%费用近正文；未核实现或复现。必要source独立通过、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2602-10520` — Daily `2026-02-13`；[RLTT exact-v1](https://arxiv.org/html/2602.10520v1) §2–3、Table1/3与AppA必要配置。2+1+2=5，具体owner差额深入：区分 emitted-token / latent-loop 两轴、terminal backprop 与直接 per-loop surrogate；GT outcome、terminal KL、非真实因果 credit 和额外 log-probability memory / packing 边界在正文，不采用token-hitting定理或无 verifier / 通用同成本提升。必要原源和实际owner经root非作者PRE通过；实际两段、前后衔接及末注经root非作者POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-10231` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10231v1)，必要方法/关键评价/直接反侧见本日 V3_EVIDENCE_SIX；2+1+2=5，具体owner差额深入。只采用prefix-conditional value/outcome分箱充分性及self-inclusion bias，不授无偏或真实credit。root实际必要原源与current owner/邻接PRE通过；root实际正文、前后邻接与末注非作者POST通过，窄锁释放，日级未授；未运行代码或复现实验。

- `SF-2026-ARXIV-2602-10693` — Daily `2026-02-13`；[VESPO exact-v1](https://arxiv.org/html/2602.10693v1) §3/AppB、Table1–2/§4.6/F。2+2+2=6，proposal与sign-kernel接口差额定点深入；正支持与可行约束、detached weight≠无偏梯度、表格/sign解释冲突与数值一致性成本近正文，不采用全方差/无限stale保证。root必要原源与current owner/邻接PRE通过授窄锁；root已实际核正文、前后邻接与末注，非作者POST通过（Ch24 noise-to-intermediate定点措辞已同步），窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-11128` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.11128v1)；§2–5、B/C与D1必要人口递推。2+2+2=6，binary有效系数/更新轴与稀有命中成本代理的clock差额深入；不采Eq13首行normalizer、统一batch/clip或现实compute最优。root必要原源/现owner邻接PRE通过并授Ch33窄锁；root已实际顺读两段正文/邻接与末注，非作者POST通过，窄锁释放，未核代码/复现，日级未授。

- `SF-2026-ARXIV-2602-13407` — Daily `2026-02-18`；[On-Policy SFT exact-v1](https://arxiv.org/html/2602.13407v1) §3.1–3.2/Eq4–9、§4/5 与 Appendix C。2+1+2=5，具体 owner 差额受影响深入；仅采二元正确/长度 admission、固定本轮 rollout 的单 update weighted CE 条件与下一轮刷新，保留 KL 其他用途、温度/长度 collapse、所测模型/数学人口与训练/推理硬件边界。root 必要原源与实际 owner/相邻 PRE 通过；实际两段、完整邻接与末注 root 非作者 POST 通过，窄锁释放，日级未验。未运行实现或复现实验。

- `SF-2026-ARXIV-2602-12342` — Daily `2026-02-17`；[Intrinsic Credit Assignment exact-v1](https://arxiv.org/html/2602.12342v1) §2–4/Eq1–4、§5.1/8 与 A.1/F.1。2+2+2=6，target likelihood difference→positive reward→turn信用具体owner差额定点深入；只采已知训练标签proxy与尺度/多解/extra scoring回退，不授Bayesian真值、potential不变性、无偏或真实客服保证。正文/附录test规模与4B成功率冲突不合并，reward与granularity联动、效率惩罚及基线调参边界保留。root必要原源/现owner PRE通过，作者已读实际两段/完整邻接，root已实际顺读正文/完整邻接及末注，非作者POST通过，窄锁释放；未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-12351` — Daily `2026-02-17`；[LongNav-R1 exact-v1](https://arxiv.org/html/2602.12351v1) III-C/IV-B、V-C/TableIII 与 VII-B。2+2+2=6，时间核baseline/whole-own-trajectory exclusion与陈旧支持具体owner差额深入；仅采时间特征、支持身份与staleness–variance取舍，不采用原文return求和的下标歧义作精确执行配方，不授任意无偏、全horizon更优、实时或constant KV。dense-vs-sparse混杂及50–200步反侧保留。root必要原源/TableIII/VII-B与现owner PRE通过；实际窄写两段，作者顺读完整邻接，root已实际顺读正文/完整邻接及末注，非作者POST通过，窄锁释放；未核代码/复现，非日级Gate。

- `SF-2026-ARXIV-2602-13953` — Daily `2026-02-18`；[QuRL exact-v1](https://arxiv.org/html/2602.13953v1) Eq6–12与§5必要配置/反侧。2+2+2=6，TIS/clipping与量化更新分辨率具体差额深入；不授最终无偏、任意optimizer的s²保证或推理QPS等于RL端到端收益。root必要原源/actualowner PRE通过，实际两段/邻接与末注经root非作者POST通过，窄锁释放；未核实现或复现，非日级验收。

- `SF-2026-ARXIV-2602-12662` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12662v1) §3/Eqs1–6、§4/Table2。2+1+2=5，成功 same-action 条件下 thinking-depth 重分配的具体差额深入；不授 action logprob 真值或总梯度守恒，失败扩展/CoSFT及长度反侧近正文。root必要原源/actual owner PRE与实际正文/完整邻接/末注非作者POST通过，锁释放；未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-12526` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12526v1) §4/Eq3–9、§5/Tables2–6 与必要 A 配置；2+1+2=5，reference-relative sampled accuracy 换目标与 StageII 固定统计具体差额深入；不授硬正确性保持、literal indicator 梯度实现或全 OOD 支配，额外 reference 成本/模型反侧近正文。root必要源/actual owner PRE通过并授窄锁；实际一段/完整邻接作者已读，root非作者实际正文/完整邻接/末注POST通过；未运行artifact或复现实验，非日级Gate。

- `SF-2026-ARXIV-2602-14872` — Daily `2026-02-18`；[exact-v1 PDF](https://arxiv.org/pdf/2602.14872v1) §3/5/7–8。2+1+2=5，具体 curriculum 梯度传递条件差额定点深入；固定原子 MLP、position-only `Q`、精确期望/长度归一与群作用假设近正文，理论与 Z96/EMA/entropy 实验分开，终点不认证全轨迹；不授真实 LLM 阈值或普遍课程最优。root 必要源与 actual owner PRE 通过，实际正文/完整邻接及末注经 root 非作者 POST 通过，窄锁释放；未核代码或复现，不授日级。

- `SF-2026-ARXIV-2602-12642` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12642v1) 必要方法、关键对照及直接限制；2+1+2=5，实际 owner 差额定点深入。root 必要原源/owner PRE 通过并授一段窄锁；仅采用正文的条件分支，不授泛化性能、正确性或安全保证。作者正文及完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST 通过，窄锁释放；未核 artifact 或复现，非日级验收。

- `SF-2026-ARXIV-2602-13035` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.13035v1) 必要方法/关键反侧/直接限制；2+2+2=6，实际 owner 差额定点深入。联合温度控制与token条件likelihood，不授正确性、整体无偏或全任务胜出；root PRE 通过并授窄锁，作者完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST通过，窄锁释放；未核 artifact/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16833` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.16833v1) §4/5及A4/A5/A8。2+1+2=5，具体mask条件分组差额定点深入；allowed-set只是prompt、轮次/措辞/总token与verifier成本保留，不授unmasked无偏或安全。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接/末注已顺读，root非作者实际正文/完整邻接/末注POST通过，窄锁释放，未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-16154` — Daily `2026-02-20`；[REMuL exact-v1](https://arxiv.org/html/2602.16154v1) §2.2–2.4/3/4及Appendix A。2+2+2=6，具体 listener agreement 与 RL→answer-only SFT 分工差额深入；仅采用局部可执行性 proxy，不授 truth/内部 faithfulness 或 reasoning 参数不变，hint/AOC协议、listener及二阶段预算保留。root必要原源/actual owner PRE及实际正文/完整邻接/末注非作者POST通过，窄锁释放；未核代码或复现，非日级 Gate。

- `SF-2026-ARXIV-2602-18645` — Daily `2026-02-25`；[exact-v1](https://arxiv.org/html/2602.18645v1) §3/4、Table3、Appendix A/E。2+1+2=5，固定最终集合的 selector 均值 credit 与 reasoner 终轮组 credit 差额定点深入；方差选组人口、全零选组退路、G×N 与任务反侧近正文，不授无偏或因果保证。root 必要原源/actual owner PRE及非作者实际正文/完整邻接/自身末注 POST通过，锁释放；未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-17550` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17550v1) §4/Eq5–8/5.1–5.3、C.1–C.3/D.2。2+1+2=5，具体owner差额深入；stopgradient单边Gaussian gate×ratioA、oldmass/signedwidth；group信号非token真值/数值与freshness/非全factorial/总预算近正文，不授普遍保证。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接/自身末注已顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-17616` — Daily `2026-02-21`；[Stable Asynchrony exact-v1](https://arxiv.org/html/2602.17616v1) §3.2–3.5/Algorithm1、AppendixB/C/D与F.3。2+2+2=6，population baseline→有限plug-in与双buffer执行差额深入；unclipped ESS/TIS、self-inclusive偏差与support、pertrajectory/延迟DP/开销配置、组件/低LR反侧和旧基线回退近正文。root actual必要源/owner PRE授窄锁；作者实际正文/完整邻接/ownnote顺读，root非作者实际2395/2397、完整2387–2407/own2895 POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21655` — Daily `2026-02-27`；[CCCaption exact-v1](https://arxiv.org/html/2602.21655v1) §3–4/Eq3–8/Table4–5。2+2+2=6，imagefacts/captionfacts双支持域分母差额深入；可错query/judge与采样目标、非完整coverage/通用双reward胜出、完整费用与独立原图Gate回退近文。root必要源/actual owner PRE通过并授单段窄锁；作者正文/完整邻接/自身末注已实际顺读，root非作者已实际独读正文/完整邻接/自身末注，POST通过，窄锁释放；未核实现或复现，非日级Gate。
- `SF-2026-ARXIV-2602-21743` — Daily `2026-02-27`；[Durian exact-v1](https://arxiv.org/html/2602.21743v1) §3/Eq11–13/4.3。2+1+2=5，同题baseline/跨题scale人口差额深入；proxy非difficulty truth、zero/tie保护、单分支反侧与总费用回退近正文。root必要原源/actual owner PRE通过；作者实际正文/完整邻接/自身末注顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现/复现，非日级Gate。

- `SF-2026-ARXIV-2602-21887` — Daily `2026-02-27`；[ExpLang exact-v1](https://arxiv.org/html/2602.21887v1) §3/§5–6/Table2/6–8/AppC，2+2+2=6；policy自选language行动/子组成功bonus与逐条verifier分责深入。coldstart反退、naiveexploit反侧、完整/条件分母及teacher/识别/训练费用与fixedEnglish回退近正文；root必要原源/actualowner PRE与实际正文483、完整邻接477–489及自身末注非作者POST通过，窄lease释放。未核artifact/复现，非日级验收。

- `SF-2026-UNIRL-20261005` — Daily `2026-10-06`；[#547](https://github.com/Tencent-Hunyuan/UniRL/pull/547) 原 controlled core及精确 [0a82feb](https://github.com/Tencent-Hunyuan/UniRL/commit/0a82feb2240f8b3b2964ec95f4e60215f827b3cc) pipeline 三 helper diff，家族2+2+2=6、纠错受影响深入。采用 ratio≈1 不认证 conditioning/KV layout 的有限反侧；事件是10/05 main合入，不称bug首次披露。作者实际代码/必要反侧与 owner 邻接已读，root PRE通过；root非作者实际正文/完整邻接及本末注POST通过，窄锁释放。未运行代码或复现实验。

- `SF-2026-ARXIV-2602-22576` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22576v1) 必要blocks31–48/65–72/85–89/103–110；2+1+2=5，双轨max分母/非truth与teacher费用差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-22623` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22623v1) 必要blocks48–83/108–111/116–122；2+2+3=7，allnegative条件重采/rollback非onpolicy、selection precision差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-22642` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22642v1) 必要blocks32–64/85–88；2+1+3=6，历史EMA/长度锚、Eq11/13保证反侧差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-22697` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22697v1) 必要blocks50–70/95–97；2+1+3=6，session/turn人口与软cost反馈非硬预算差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-22718` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22718v1) 必要blocks49–93/119–132；2+2+3=7，ranking/local迁移/actor费，prefix单调子命题隔离差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-22751` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22751v1) 必要blocks33–61/74–81/102–105；2+1+3=6，sampleNLL权重/default非renorm、方向与费用边界差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-22765` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22765v1) 必要blocks22–58/73–74/85；2+2+2=6，cache混组/最终verdict、dynamic critique-only反侧差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。

- `SF-2026-ARXIV-2602-23248` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.23248v1) 必要blocks9–40/47–54；2+2+2=6，frozen solver/translator接口、answer-only faithful非humanlegibility差额深入，预算、反侧与旧路径回退近正文。fresh非原packet作者实际独核必要原证/actual owner PRE，未变身份/精确版/命题复用；获Ch33窄锁，作者已实际顺读正文/完整邻接及自身末注，root非写入者actual POST通过，Ch33窄锁释放；未核artifact/复现，不授日级完成。
