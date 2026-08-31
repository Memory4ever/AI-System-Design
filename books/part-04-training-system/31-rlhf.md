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

若总是比较一个明显优秀回答和一个随机垃圾回答，Reward Model 容易学到表面 shortcut，却难以区分真实 policy 产生的相近候选。

Candidate distribution 也会随 policy 更新而漂移。旧 Reward Model 在新 policy 产生的 out-of-distribution outputs 上可能不可靠，因此 RLHF 常具有数据闭环，而不是一次离线训练后永久有效。

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

## 从 Reward 到 Policy objective

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

### 改变输出分布是目标，不是无副作用的偏好标签

只要 policy update 真正生效，条件分布就不再与 reference 完全相同：某些候选 response 的概率上升，另一些必然相对下降。Preference optimization 不是在原模型外面附加一个“更喜欢”的标签，而是在重写给定 prompt 下的 action probability。

```text
pi_ref(y | x)
-> reward / preference-weighted update
-> pi_theta(y | x)
```

KL constraint 只限制这种重写的平均幅度。若它是在某个 prompt distribution 上求期望，平均 KL 很小仍可能掩盖少数 prompt、语言、领域或 safety slice 上的较大移动；Sampling temperature、Prompt 和 Context 又会继续改变最终可观察分布。因此“KL 没超阈值”不能证明原有行为逐项保留。

这里还要把三种边界分开：pretrained parameters 中可被适当条件触发的 **latent capability**，当前 policy 通常会输出的 **elicited behavior**，以及接入 Retrieval、Tool、Sampling 与 guardrail 后的 **system capability**。RLHF 最直接改变第二层：它可以让已有能力更容易被调用，也可以压低不希望出现的行为；参数更新同时可能学习新模式或造成 capability regression，但单凭某个回答消失，无法证明相关表示已从参数中删除。反过来，某项 win rate 上升也不能证明模型获得了跨分布的新推理能力。

所以能力边界不能由 reward curve 或平均 KL 推断，必须比较 base/SFT/reference 与新 policy 在相同 decoding contract 下的多切片 Evaluation，并单独记录 capability gain、behavior shift 与 regression。InstructGPT 的原始实验同时报告目标 prompt distribution 上的人类偏好和公开 NLP evaluations，正体现了这两类证据不能互相替代。

### Reverse KL 会把“找到高奖励”收缩成单一路径

KL 约束最初合理，因为它限制 policy 远离 SFT reference 的速度；但 reverse KL 倾向于追随当前高概率、高奖励 mode，训练稳定并不等于保留了可替代行为。当目标分布本身包含多条有效解时，优化 owner 需要同时观察 reward 与 response-distribution coverage，并把 forward/group distribution matching 作为条件分支：它可保留更多 mode，却增加采样、密度估计和 group construction 成本，也可能把低质量 mode 一并保留。若任务只要求一个可验证答案或目标分布不可可靠估计，reverse-KL baseline 仍更简单；coverage 下降时再启用分布匹配，并以独立 verifier 和 diversity slice 作回退 Gate。

<!-- source-family:SF-2026-ARXIV-2605-19461 -->
exact-v1 的 Method §3 只证明其 forward/group distribution-matching objective，§4–5 的实验只覆盖作者披露的模型、prompt 与偏好数据；Appendix B 的设定不能证明该分支普遍优于 reverse KL，也不能把 diversity 当作正确性。

## Reward hacking 与 Goodhart's Law

Reward Model 是人类偏好的有限代理。Policy optimization 比普通 evaluation 更危险，因为 policy 会针对代理的弱点搜索。

可能出现：

- 通过更长、更自信或固定格式获得高分。
- 迎合 judge wording，而不提高任务正确性。
- 利用训练 pairs 中的 spurious cues。
- 产生 Reward Model 未见过的异常输出。
- 提高 aggregate reward，却损伤特定用户群体。

所以 reward 上升必须与 independent human evaluation、task verifier、安全评估和 distribution slices 同时解释。

### Reward Hacking 也可表现为更新方向漂移

只比较 reward 与 outcome 会在故障发生后才看见 Goodhart。若正常学习在低维更新子空间中形成相对稳定方向，持续偏离该方向可以作为 hacking proposal；训练控制面可限制更新、触发复核或回退 checkpoint，但不能把几何相似直接当成价值正确。收益是增加早期信号，代价是正常能力跃迁也可能改变方向，固定 trusted direction 会阻碍探索。保守 KL、独立 evaluation 与人工检查仍是 fallback。当前证据明确是初步研究，只覆盖披露模型与任务。

<!-- source-family:SF-2026-ARXIV-2605-25189 -->

### Majority Vote 可能只是在压尖已有分布

多数采样后投票在答案可离散比较时是低成本 baseline，但 pass@k 上升可能来自已有正确 mode 被更频繁抽中，而不是 policy 学到新能力。训练 owner 应把迁移结果拆成 `capability expansion`、`distribution sharpening` 与 `mode extinction`；当重复自训练开始消灭少数但有效的轨迹时，TTRL-style guard 可以冻结或降权高灭绝风险更新。收益是避免把表面成功率误读成能力增长，代价是额外 rollout、mode tracking 和 guard threshold；短任务、单一可验证答案或分布稳定时，普通 majority vote 仍成立。

<!-- source-family:SF-2026-ARXIV-2605-19444 -->
exact-v1 §2–3 给出 extinction 诊断与 TTRL-Guard，§4 的结果只属于论文实验，§6 明确留下任务广度与极端 sampling regime；它没有证明所有 majority-vote gain 都是 sharpening。

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

### 从持久权重更新到条件化 Activation Intervention

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

### Reward Model 也有 Policy-relative State

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

进一步地，多轮任务不能只保存一个 scalar reward。若更新依赖不可见的中间判断，credit owner 应维护显式 belief state，记录每一步可观察证据、belief revision 与最终 outcome，使 reward 能回溯到改变决策的 evidence。它改善长程 credit，却新增 belief model 偏差、状态膨胀与错误归因；终局可直接验证的短任务仍应使用简单 outcome reward。

<!-- source-family:SF-2026-ARXIV-2605-20061 -->
exact-v1 §3 给出 belief-based credit，§4 与 Appendix C 只证明作者环境中的归因改善，不证明 belief state 等于真实因果状态。

## RLHF 的系统成本

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

### 异步 On-policy Distillation 需要 Sample Freshness

缓存 rollout 能复用昂贵采样并提高 trainer 利用率，在 policy 变化慢时是合理近似；长 horizon 或异步更新后，同一 buffer 同时包含 rollout drift 与 supervision drift，旧样本不再等价于当前 on-policy evidence。Runtime 因而要为样本绑定 behavior/teacher revision，并用 freshness score 决定接受、降权或丢弃，而不是只按到达顺序消费。

收益是允许有限异步而不把所有旧样本当作同质量监督；代价是版本状态、freshness estimator、样本浪费和估计偏差。漂移无法可靠估计时应缩短 buffer 或恢复同步生成。exact-v1 只在其披露的长程任务、模型、buffer 与 freshness controller 中验证该机制，不给出跨任务通用阈值，也不证明更高吞吐必然改善最终策略。

<!-- source-family:SF-2026-ARXIV-2605-17862 -->

## Human feedback 不等于统一人类价值

标注结果受 rubric、文化、组织 policy、任务和标注界面影响。多数投票会掩盖少数群体偏好，专家任务又可能无法由通用标注者可靠判断。

系统需要记录：

- Label source 和 population。
- Rubric/version 与 policy change。
- Agreement、tie 和 uncertainty。
- Sensitive slices 与 appeal/escalation。
- Synthetic/AI feedback 是否混入。

更准确的名称是“使用特定 feedback process 优化模型”，而不是宣称模型已与抽象的“人类价值”完全对齐。

### Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间

把 reward 当作同尺度、同步到达的标量，在 rater 同质且反馈能在 update 前返回时是合理的；现实约束同时来自身份异质性和时间异步性：不同 rater 的 offset/slope 不同，慢 verifier 或人工反馈又可能晚到数个 gradient step。RLHF 状态因此需要同时持有 rater identity、calibration slice/shrinkage prior/version，以及 pending reward queue、age/kernel、originating policy/importance ratio 与 reinjection mass。每位 rater 的 held-out affine calibration 可用 empirical Bayes 向总体收缩；迟到 reward 则以 clipped residual 进入后续 advantage。论文分别在 PRISM/PluriHarms 与 tabular MDP 上报告 RMSE 改善和最高 47.9× bias reduction，但没有证明非线性或 adversarial rater、online drift、large-scale RLHF 稳定性与生产 queue failure。稀疏 rater 回退总体 calibrator 并抽样审计；delay/mass 假设失效时等待慢反馈或采用 bounded synchronous update。

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

### Imperfect Verifier 把监督噪声与 Rollout Compute 绑在一起

RLVR 假设 verifier 能稳定区分正确与错误，实际 false positive 会奖励错误轨迹，false negative 会丢弃有效探索；增加 rollout 数量可能同时放大这两种噪声。训练合同应记录 verifier confusion profile、rollout budget 与 policy distribution，并把“更多采样”和“更好监督”作为独立轴。收益是能选择 compute–supervision trade-off，代价是需要可控噪声估计与额外验证；确定性可执行任务仍可使用简单 verifier。现有结果仅覆盖 Qwen2.5、GSM8K 与 GRPO，不构成跨任务定律。

<!-- source-family:SF-2026-ARXIV-2605-25252 -->

### Reflection 只有进入可验证更新回路才是训练状态

把 reflection 作为一次性 prompt 文本，最容易接入但不会积累可审计经验；把失败轨迹、环境反馈与修订后的行动组织成 versioned reflection state，才能让后续 rollout 复用。其收益是把失败转成可训练信号，代价是错误反思自强化、额外存储与 evaluator 成本。Reflection 必须由环境结果或独立 verifier 筛选，并允许丢弃或回退到原 policy；没有可靠反馈时，临时 scratchpad 比持久更新更安全。

<!-- source-family:SF-2026-ARXIV-2605-20477 -->
exact-v1 §3–4 描述经验驱动 reflection，§5 的 MiniHack/ALFWorld 结果及 §5.3 边界不能证明开放域 reflection 忠实或长期稳定。

### 从终局 Reward 到可验证子问题 Curriculum

终局 reward 在任务短、成功条件明确时最少引入人为结构；长推理链里，它却把 credit 全部压到最后一步。若 reference chain 本身可审计，可以由 curriculum builder 把终局任务派生为有边界、可判定的 subproblems，verifier 只提交这些局部判据的 credit，再由训练控制面决定是否进入 policy update。这里 curriculum builder 拥有难度与分解边界，verifier 不拥有策略提交权。

更密集的反馈换来 reference bias、子问题捷径和“局部全对但整体失败”的新风险；因此必须保留未分解的终局任务作为 held-out gate，分解失真时回退终局可验证训练。arXiv:2605.22074v1 只支持作者 reference-derived curriculum 与受测任务中的实验结果，不证明任意 chain decomposition 都保持原目标。

<!-- source-family:SF-2026-ARXIV-2605-22074 -->

### 后训练分支的本质差异是 State Distribution

只按 token objective 区分 SFT、distillation 与 RL，容易忽略监督发生在哪个状态上。静态 SFT 在固定数据分布上学习；on-policy distillation 让当前 policy 先到达自己的状态，再接受 teacher signal；RL 则在 policy-induced states 上用 reward 改变访问概率。约束从“标签是否正确”变化为“训练是否覆盖部署时会到达的状态”，因此 rollout producer、policy revision、teacher/reward revision 与 staleness 必须共同进入 run identity。

扩大状态覆盖能修复静态数据看不到的错误，却增加 rollout 成本、off-policy staleness 和反馈回路；部署状态稳定、示范覆盖充分时，静态 SFT 仍然更简单可靠。arXiv:2605.22731v1 的比较仅支持论文模型、任务与训练设置，不证明 on-policy 路线普遍优于 SFT，也不把不同 reward contract 视为可直接比较。

<!-- source-family:SF-2026-ARXIV-2605-22731 -->

## PPO、GRPO、DPO 分别接住什么

### Feedback Loop 从固定环境演进为双层控制系统

固定环境与 verifier 在能力相对稳定时足以提供监督；当 policy 的能力边界持续移动，环境若不暴露新失败，训练会优化过时接口。更完整的闭环让 verifier diagnosis 产生 environment/interface proposal，再由独立 gate 更新任务和反馈分布，policy 与 learning interface 因而拥有各自版本与回滚点。它能把新失败转成课程，但会引入非平稳性、评估污染与共同过拟合；冻结环境的 held-out gate 仍必须保留。

<!-- source-family:SF-2026-ARXIV-2605-24426 -->

静态文字反馈同样可演进为 bilevel 控制：下层 actor 学习利用反馈，上层 feedback generator 以真实 policy return 为目标更新，而不是只模仿通用 rubric。收益是反馈能适应当前 policy，代价是 reward hacking、计算成本和 credit assignment 更难审计；固定 rubric 在样本少或上层回报不可信时仍更安全。该证据仅支持作者实验中的 Stackelberg 训练，不证明自然语言 critic 能代表人类偏好。

<!-- source-family:SF-2026-ARXIV-2605-24547 -->

### 在线 Credit 需要显式的时序状态

完整 trajectory 后更新实现简单，但长 horizon 与 partial observation 会让 credit 延迟且内存增长。维护 recurrent hidden state 与 eligibility trace 可在每一步执行 exact online update，把“当前可见状态”和“历史如何影响参数”分别交给两个状态 owner。收益是流式学习，代价是 recurrent state 漂移、截断恢复与并行训练更复杂；短 episode 或可离线重放时，batch trajectory 仍更容易验证。当前结论只覆盖特定 diagonal recurrent 架构及其实验，并不证明所有大模型后训练可直接使用同一更新规则。

<!-- source-family:SF-2026-ARXIV-2605-24709 -->

### Reward Model 误差必须在 Deployment Policy 下结算

只测 reward model 在训练偏好分布上的预测误差，无法回答优化后的 policy 会把流量推向哪里。评估应同时保留训练分布 prediction error 与 reward-tilted deployment distribution 下的 policy-value gap；后者由实际 policy occupancy 拥有。这样能发现“验证集准确但被 policy 放大”的误差，代价是需要 on-policy 或可信 importance weighting，且估计方差更高。policy 变化很小、支持集充分时，传统 held-out 误差仍有价值。该分析说明测量缺口，不自动给出一个无偏的真实人类价值估计器。

<!-- source-family:SF-2026-ARXIV-2605-24749 -->

本章只定义 RLHF pipeline 与 reward objective，后续三章职责不同：

```text
PPO   on-policy optimization with learned value/advantage and clipping
GRPO  group-relative advantage without a learned critic
DPO   offline pairwise objective derived from KL-constrained preference optimization
```

DPO 不训练显式 Reward Model，也不在 fine-tuning loop 内做 on-policy rollout，但仍依赖 preference data 和 reference policy。GRPO 可以使用 learned reward，也可以使用 verifiable reward；“移除 critic”不等于移除所有 reward design。

## Evaluation 必须独立于 Reward Model

至少要比较：

- Human preference win rate 与置信区间。
- Task correctness / verifier pass rate。
- Reward score 与 KL divergence。
- Response length、refusal 和 style shifts。
- Pretraining/SFT capability regressions。
- Safety、bias 与 adversarial prompts。
- Rollout throughput 与每次有效 update 成本。

如果最终 Evaluation 仍使用同一个 Reward Model，训练与评估共享漏洞，无法证明真实质量提升。

### Reward Proposal、Phase Handoff 与 Exploration 都需要独立 Gate

自动生成 reward hypothesis 可以扩大搜索，但生成质量不授予训练 authority。候选 reward 应从共享 checkpoint 分叉，由 competence-aware verifier 检查，再按 training phase 小流量部署；收益是缩短 reward engineering，代价是额外分支训练、验证成本与 specification gaming 风险。Verifier 不充分时应回退人工设计或固定 reward。

<!-- source-family:SF-2026-ARXIV-2604-28056 -->

SFT 到 RLVR 也不是中性 handoff：SFT 已改变 policy distribution，可能把 on-policy exploration 推离可验证区域。黑盒 on-policy distillation 可作为条件分支，在 preference/RL 前重新对齐起始分布，以额外 rollout、teacher 调用和 imitation bias 换更可训练的策略状态；没有 teacher access 或分布漂移不显著时，直接 handoff 仍更简单。

<!-- source-family:SF-2026-ARXIV-2604-28123 -->

最后，exploration 本身属于训练 trust boundary。模型可能通过减少有用动作抵抗更新，而不表现为显式 reward hacking；release evidence 应同时记录 rollout diversity、action coverage、policy-update magnitude 与 task progress。构造实验不证明部署模型普遍存在该行为，因此这些指标是诊断 sensor，不是恶意意图判决。

<!-- source-family:SF-2026-ARXIV-2604-28182 -->

### Teacher 与未来 Reward Model 都是反馈回路中的状态

On-policy distillation 比离线 teacher labeling 更接近学生实际访问的状态，但 teacher 输出不能被视为无条件真值：学生需要探索信息丰富的状态，teacher reliability 也必须决定哪些反馈可进入更新。这样能减少 distribution mismatch，却增加采样成本、teacher 不确定性估计和错误反馈放大；低风险、分布稳定的任务仍可使用离线 distillation。

<!-- source-family:SF-2026-ARXIV-2605-03677 -->

迭代 RLHF 还会把当前策略产生的数据用于训练未来 reward model，形成 policy → data → reward model → policy 的闭环。若优化只追逐当前 proxy，策略会逐步塑造更容易被未来 reward model 接受的数据，导致自强化的 alignment collapse。解决方向不是简单增加 KL，而是显式建模未来评估器、限制参数 steering 并保留独立 evaluation；其代价是双层优化和模型假设，假设不可靠时必须回退到冻结评估器、外部审计与阶段性发布。[受限证据：arXiv:2605.03677v1、2605.04266v1]

<!-- source-family:SF-2026-ARXIV-2605-04266 -->

### Post-training 必须把故障、探索与 Credit 组织成闭环

强化微调失败时，单看最终 reward 无法区分 environment error、rollout hang、verifier failure、policy regression 或数据污染。可靠 runtime 应采集可观察 fault fingerprint，先诊断故障 owner，再执行重试、隔离、降级或样本剔除，并把处置结果写回下一轮训练。自动 remediation 减少人工停机，却可能把诊断误差放大为数据偏差；无法归因时应冻结更新并保留原始 trajectory。

在线 preference learning 的 exploration 也不能只依赖当前 policy 的瞬时不确定性。历史样本覆盖、observer disagreement 与旧策略误差可以提供更稳定的 prior，再用当前观测修正 exploration budget。这样能把查询集中到高信息区域，但会引入历史分布滞后；发生 policy shift 时必须重置或降权旧不确定性，保留均匀探索作为覆盖 fallback。

tool-integrated trajectory 的 terminal reward 往往把多个动作混成一个结果。step-level credit 应绑定可观察 effect、状态变化与 verifier receipt，再决定哪些 turn 进入更新。没有外部 verifier 时，outcome-potential delta 可以作为弱监督，但其可识别性依赖状态表征和后续 outcome；它是估计器，不是真实因果 credit。局部 layer objective 能减少 end-to-end backprop 成本，却会牺牲跨层一致性，因此应通过端到端 holdout 与周期性全局校准共存，而非直接替代全局训练。

<!-- source-family:SF-TOWARDS-ROBUST-LLM-POST-TRAINING-AUTOMATIC-FAILURE-MANAGEMENT-FOR-REINFO -->
<!-- source-family:SF-DATA-DEPENDENT-EXPLORATION-FOR-ONLINE-REINFORCEMENT-LEARNING-FROM-HUMAN- -->
<!-- source-family:SF-EVERY-STEP-COUNTS-STEP-LEVEL-CREDIT-ASSIGNMENT-FOR-TOOL-INTEGRATED-TEXT- -->
<!-- source-family:SF-RETHINKING-LOCAL-LEARNING-A-CHEAPER-AND-FASTER-RECIPE-FOR-LLM-POST-TRAIN -->
<!-- source-family:SF-SELF-INDUCED-OUTCOME-POTENTIAL-TURN-LEVEL-CREDIT-ASSIGNMENT-FOR-AGENTS-W -->

### 多路反馈的混合权重应由噪声状态驱动

固定比例混合两类 reward/gradient，在两路信号方差稳定且方向一致时最容易复现；在线训练中，噪声和 disagreement 会随 policy 改变。Feedback controller 可以从梯度方差与方向分歧估计自适应 mixing weight，使低噪声、较一致的信号获得更多控制权。收益是减少固定权重对阶段变化的迟钝，代价是在线统计、额外同步和估计偏差；协方差假设失效或小样本抖动时会产生错误切换，应使用 clipping、慢更新或退回固定比例。exact-v1 只支持论文的 GAC 设定与所测任务，不证明任意 reward source 都可校准。<!-- source-family:SF-2026-ARXIV-2605-26184 -->

### 交互式后训练必须版本化 Simulator 与对话状态

静态 preference pair 适合一次性回答，却不能表达多轮行为对未来用户状态的影响。交互式 RL 分支把 user simulator、dialogue state、policy revision 与 reward/judge 共同纳入 rollout contract，再用 GRPO 类更新优化长程行为。它能训练澄清、追问和恢复策略，但新增 simulator bias、judge coupling 与 credit horizon；模拟用户未校准时，应限制为离线 proposal，并以真人或独立环境做 release gate，静态 SFT/RLHF 仍作为保守基线。exact-v1 仅支持论文披露的 simulator、模型和评估，不证明真实用户分布上的长期收益或安全。<!-- source-family:SF-2026-ARXIV-2605-26403 -->

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

## Review notes

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

- `2026-05-04 / SF-2026-ARXIV-2605-01831` — exact-v1 `arXiv:2605.01831v1`；正文吸收 explicit preference contract 与 paraphrase-consistency evaluation，不把 synthetic benchmark 外推到真实用户或下游 RL。

#### Source-specific exact-v1 Review notes

- SF-2026-ARXIV-2606-28955 — primary arXiv:2606.28955v1; exact-v1 URL=https://arxiv.org/html/2606.28955v1; Method=https://arxiv.org/html/2606.28955v1 — §3 Method; Pretraining.; Pretraining budget.; Evaluation=https://arxiv.org/html/2606.28955v1 — §Theoretical analysis.; 4 Experiments; 4.2 Main results; Non-proof=https://arxiv.org/html/2606.28955v1 — §5 Limitations and Future Work; 7 Conclusion；该 exact-v1 只证明论文所述 workload、model/runtime 与 evaluator 范围内的结果，未证明跨模型族、硬件、数据分布、未测 failure mode 或生产 SLO 的普遍成立。。

#### Source-specific exact-v1 Review notes

- `SF-2026-ARXIV-2606-23038` — primary `arXiv:2606.23038v1`; Method=`arXiv:2606.23038v1 — §4.1 Dual-LoRA Architecture; §4.4 Co-Evolutionary Training; §Appendix A EvoRubrics Algorithm`; Evaluation=`arXiv:2606.23038v1 — §2.2 Dynamic Rubrics and Adaptive Evaluation; §Appendix C Evaluation Details; §C.1 Policy LLM Evaluation`; non-proof=`arXiv:2606.23038v1 — §6 Conclusions and Future Work; §E.3 Discussion`; fallback=该 family 的 failure pressure 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 披露的 evaluation signal 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- `SF-2026-ARXIV-2606-24004` — primary `arXiv:2606.24004v1`; Method=`arXiv:2606.24004v1 — §4 Spec Learning Framework; §4.1 Selection Method; §4.4 Judge protocol and selection`; Evaluation=`arXiv:2606.24004v1 — §5 Results; §B Statistical robustness; §C Judge calibration`; non-proof=`arXiv:2606.24004v1 — §6 Discussion; §7 Limitations; §8 Conclusions and Future Work`; fallback=该 family 的 failure pressure 是：Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 披露的 evaluation signal 是：We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

### Source-family integration record

<!-- daily-20260628:TRAIN-RLHF:start -->
### Owner-merged minimal durable delta

Reward-hacking 防线可以前移到 transition admission：在修改环境或 replay state 前冻结 current policy 与 return evaluator，对 current/modified policy 做 equal-budget counterfactual forecast；只有 evaluator 接受才提交 transition。模型负责 proposal，独立 evaluator 拥有 gate，原始 true-objective evidence 继续保留。

### Trade-off、failure、fallback 与 coexistence

Gate 依赖已能把 hacking trajectory 排低的 evaluator、clean seed 与额外 1.8×–4.2× 成本；evaluator misspecification 时它会接受错误 transition，需回退人工/true-objective review。

<!-- daily-20260628:TRAIN-RLHF:end -->

<!-- recovered-daily-20260623:TRAIN-RLHF:start -->
### 2026-06-23 evidence integration — TRAIN-RLHF

相邻章 `books/part-04-training-system/32-ppo.md#L1` 只消费 handoff，不重复拥有机制。

### Owner-merged minimal body

- **SF-2026-ARXIV-2606-23038**：EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning 的 exact-v1 机制为：We propose EvoRubrics, a co-evolutionary RL framework where a Policy LLM and a Rubric Generator jointly improve through adversarial interaction within each training step. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 该 family 的 failure pressure 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 披露的 evaluation signal 是：However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
- **SF-2026-ARXIV-2606-24004**：Towards Spec Learning: Inference-Time Alignment from Preference Pairs 的 exact-v1 机制为：We propose spec learning, a framework that relies on a brief user instruction and a small set of preference judgments. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 该 family 的 failure pressure 是：Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 披露的 evaluation signal 是：We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- recovered-daily-20260623:TRAIN-RLHF:end -->

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-EVALSTOP:start -->
- `SF-EVALSTOP` — Daily `2026-06-03`；primary `arXiv:2606.04145v1`；Books review `books-review:SF-EVALSTOP`。

  **已吸收的语义增量：** Recall the architecture overview in Figure 1 . EvalStop is a composable wrapper around any base scheduling policy. It monitors eval-score trajectories (the world feedback signal) and early-stops jobs when quality is irrecoverably declining. Boundary: World feedback as a scheduling signal. Our results show that downstream evaluation (world feedback) is a better signal for scheduling RLHF jobs than training loss (proxy 2 ) or reward model score (proxy). This aligns with the growing recognition that proxy optimization in RLHF requires external grounding ( Gao et al., 2023 ; Skalse et al., 2022 ; Moskovitz et al., 2024 ) .
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
