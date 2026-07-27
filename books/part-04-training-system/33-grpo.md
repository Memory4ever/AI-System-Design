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

组采样的关键是条件相同：同一个 prompt 下的 candidates 共享任务难度。若把不同 prompts 的 raw rewards 直接比较，简单问题可能系统性获得更高 advantage。

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

## Sequence Reward 怎样作用到 Tokens

若 reward 只在 response 末尾给出，常见简化是同一 `A_i` 作用于该 response 的所有有效 tokens：

```text
A_(i,1) = ... = A_(i,|y_i|) = A_i
```

这比 learned token value 简单，也更粗糙。正确 final answer 可能包含冗余或错误 reasoning，错误 final answer 也可能包含部分有价值步骤。

Process reward、step verifier 或更细粒度 credit assignment 可以提供局部信号，但会增加标注/evaluator 复杂度，并引入新的 exploit surface。

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

## Verifiable Reward 的优势与边界

数学 final answer、代码 unit tests 和格式检查可以减少 learned Reward Model 的主观误差。这类 reward 适合大规模自动 rollout，也推动了 reasoning-oriented RL。

但 verifier 仍是 specification：

- Final answer matcher 可能忽略推理有效性。
- Tests 可能覆盖不足或被 hard-code exploit。
- 格式 reward 可能压过内容正确性。
- 多个 reward components 的 scale 会改变总排序。

Policy 会优化 verifier 可见的目标，因此必须保留 held-out tests、adversarial cases 和独立人工检查。

### Verifier 也成为 Policy 时，必须分离更新与权威

固定 tests/checker 最容易复算，是发布门禁和高风险 regression 的 authority；但它无法持续覆盖当前 policy
新出现的错误。让独立 Test Policy 阅读候选并生成 assertions，再只保留能通过 ground-truth solution 或
独立 oracle 验证的 tests，可以形成 `code policy ↔ verifier policy` 的双策略闭环。失败案例还可进入带
版本和过期规则的 failure book，作为下一轮 test proposal 的状态。

这提高错误覆盖，也新增 collusion、oracle dependency、failure-memory staleness 与 sandbox nondeterminism。
Verifier 的 reward 不能只鼓励“让当前代码失败”，还要同时约束 validity；训练用 adaptive tests 也不能
替代独立 hidden tests。没有可信 solution/oracle、程序有副作用或 specification 开放时，固定人工 tests、
property checking 和人工 review 仍是 authority。

### Verifier 拥有方向，Privileged Teacher 最多调节幅度

Binary verifier 若是 correctness authority，privileged teacher 的 token signal 不应翻转 update sign；一种分层是
让 verifier 决定正负方向，teacher 只提供严格为正、受限的 token multiplier。它能提供细粒度 weighting，却仍会
改变 parameter trajectory，并新增 teacher bias、额外 forward cost、normalization 与 leakage surface。

Self-Distilled RLVR 的数学形式支持正 multiplier 不翻转 sampled-token direction，不证明 privileged signal “零影响”
或形成真实 causal credit。可靠 token/process verifier 可用时应优先直接监督；teacher 不可靠时 sequence-level
verifier reward 仍是安全分支。

### 多阶段交互需要 Phase-specific Credit，而不是一个终局标量

工具 Agent 的轨迹可能包含探索、提出结构、执行与确认。只给 terminal reward 实现简单，却会让早期结构
选择得不到信用，甚至通过穷举或绕过中间约束获得高分。可以用显式 phase checkpoint 和 token masks，把
schema/evidence reward 只分配给相应动作，再让 execution reward 覆盖完整轨迹；中间 reward 只有终局成功
时才生效，可减少“找对对象但结果错误”的 shortcut。

Phase boundary、mask 与 reward coupling 都属于 objective semantics。它们会引入 boundary gaming、
标注成本和状态机复杂度，也不保证适用于不同工具协议。小 schema、短轨迹或 terminal verifier 足够密集时，
单一 reward 仍更透明。

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

Binary terminal reward 的另一个边界是：当前 policy 若对一批任务几乎全成功或全失败，group-relative advantage 会退化。可以在 hard correctness gate 之外，引入由 task geometry 定义的离散 proximity zones，让 near-success trajectory 获得有序但受限的 shaping signal：

```text
terminal correctness
+ bounded, discretized progress zone
→ group-relative ordering
```

离散化可以减少连续噪声被过度放大，却把 proximity function、zone boundary 与权重变成 reward contract。它只在 partial progress 可可靠定义时成立；开放式 research、语义质量和不可逆 tool action 往往没有可信“距离”。错误 proxy 会制造 reward hacking，因此 binary verifier 在 hard pass/fail 风险边界中仍不可替代。

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

### Reasoning Cost 也是版本化的 Reward Prior

硬 token cap 与线性长度惩罚便宜、可解释，并直接对应 decode 数量；在硬 SLO 或每个 token 成本近似一致时仍是必要边界。
但统一的 token 税无法区分必要的罕见步骤与重复 filler。若 prompt 在生成答案时始终可见，reasoning trace 应付出的不是重复
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
最终训练一个不依赖 runtime Skill 的 policy。这样做改变的是 curriculum/control state，而不是证明模型“内化”了
可验证程序：Skill revision、selection score、injection schedule、policy checkpoint 与 no-skill evaluation 必须
联合版本化。稳定 runtime Skill 在频繁更新、审计、tenant policy 或模型容量不足时仍然成立。

SKILL0 的作者结果支持 scaffold annealing 的一种实现；helpfulness estimate、coupled reward、visual rendering 与
repository drift 使因果归因仍为 Experimental。

论文当前 revision 相比 2025 年 v1 补充了更完整的 recipe、限制和系统细节；引用具体
hyperparameters 或 benchmark 时必须锁定 revision。本文只沉淀跨版本仍成立的阶段职责和
trade-off，不把作者 recipe 泛化为 GRPO 的统一定义。

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

### Outcome-routed Update 先分支，再做 Group Calibration

Uniform online policy distillation 会让 teacher 对已正确样本继续提供高熵噪声，也无法区分“保持正确”和“修复
错误”。一种分支先由 outcome verifier 区分 correct/incorrect：正确样本约束 student 自身分布，错误样本再
吸收 teacher signal，最后在 group 内校准 sample weight。它新增 verifier error、branch imbalance、teacher bias
与 group-composition dependency；稳定 offline distillation 或可靠 demonstrations 仍是低复杂度方案。
SCOPE 提供受限机制证据，不构成跨任务最优 OPD recipe。

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

另一条演进把 experience extractor 作为独立 policy：actor rollout 产生 success/failure evidence，extractor
形成可复用策略，再由 actor 在新状态中验证和更新。它比 actor 自我反思更能分离角色，却增加 extractor/
actor 共适应、library merge 与 causal attribution；经验必须保留 source policy、environment、适用条件、
supersession 和 rollback，不能只存一段“成功经验”。

## Rollout 变成服务：Environment、资源与 Policy Freshness

当 rollout 延迟、工具环境和 update compute 使用不同资源画像时，同步 colocate 仍最容易证明，却会放大 idle 与长尾。把 rollout 服务化可以独立扩缩，但必须先明确 environment state、policy epoch、trajectory admission 与失败终态，不能让资源调度暗中改写训练分布。

### Environment 与 Policy 可以共同演进，但 Held-out Evidence 不能回流

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

一种收敛优先的方案，是让 rollout graph 成为 training forward graph 的数值一致子图，使两边共享 FP8
precision flow，而训练额外保留高精度 master state 和 backward path。它用更一致的 policy coordinate 换取
低精度 rollout/training 的速度机会；代价是训练栈必须支持相同量化算子、activation/gradient 精度设计和
硬件能力。BF16 仍是机制最简单、数值边界最清楚的基线。单篇 FP8 实验不能证明所有模型、长度与 objective
都能保持收敛，更不能把“相同权重版本”简化成“相同 policy”。

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

## 从 Sequence Reward 到 Typed Trajectory

服务化解决 trajectory 从哪里来，不解决 credit 应落在哪个 decision boundary。单轮、同角色、单 verifier 的 sequence reward 仍是最小方案；当角色、阶段、环境状态和分支增多时，样本 identity 必须先细化，才能讨论更局部的 advantage、持久 partial rollout 或跨 policy reuse。

### Immediate Reward、Delayed Correction 与 Staleness 是同一 Lifecycle

长 Agent trajectory 可在 stage 完成时得到 immediate reward，再由最终 outcome 产生 delayed correction；两者
必须绑定同一 behavior-policy/token identity。若 correction 到达时 policy 已更新，trainer 要么丢弃、降权，要么
使用可验证的 off-policy correction，不能把旧 credit 当成当前样本。

GrandCode 提供这一多阶段 reward lifecycle 的受限案例，但独立 normalization、缺少关键 ablation 与未公开训练
代码使 headline 不能归因于某一组件。短任务、可靠 terminal verifier 或延迟很低时，单一 terminal reward 仍更简单。

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

探索也不能只追求 action entropy。若 verifier 能识别多个正确 outcome modes，可以在正确轨迹集合内鼓励
mode-level diversity，再对高置信错误施加更强 correction；这分别解决 correct-mode collapse 与 overconfident
negative update。二者都依赖当前/reference policy 的概率校准、长度归一化与 binary verifier，不能合并成
“多样性越高越好”。DSDR 与 ACE 是这两个相邻 actuator 的受限案例。

多模态 tool RL 还应把 interaction budget 写入 reward。Python、crop、zoom 或 perception tool 可能增加必要证据，
也可能被 policy 当成容易获得的 shaping reward；group selection 若偏向恰好会调用工具的样本，又会改变训练分布。
因此必须分别观察 task correctness、tool necessity、call cost、sandbox risk 与 no-tool baseline。PyVision-RL 只证明
作者环境中 reward、group selection 和 media materialization 的联合改变有效，不能把更多 tool calls 视为能力。

另一个分支让两个 policy 在自博弈中共同生成 task 与 solution，或让当前 policy 在临时 memory scaffold 中跨 rollout
探索，再把经 verifier 接受的经验内化到参数。这提高 curriculum coverage，却新增 role collusion、self-confirmation、
off-policy drift 和“临时状态何时清空”的问题。Tool-R0、EMPO² 与 CUDA Agent 的 executable-kernel 环境支持
`curriculum/proposal owner != solver/update owner != verifier` 的分责；固定外部题库和单 policy rollout 在复算、
隔离或高风险任务中继续合理。

### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界

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

## 小结

GRPO 用同 prompt 多个 responses 的相对 reward 代替 learned critic baseline。它减少 value-model 状态，并保留 clipped policy update 与 reference constraint，适合 reward 可比较、尤其可验证的 rollout 任务。

它没有让 RL 变简单到只剩一个公式。Group variance、rollout generation、reward specification、token credit、policy synchronization 和 implementation variants 共同决定训练是否有效。

## Review notes

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
- When Does Muon Help Agentic Reinforcement Learning?（optimizer/update-scale/sharding contract；
  Status: Experimental）: https://arxiv.org/abs/2607.16169

W32 primary-source cases：

- SMRC-SD（state-matched contextual distillation；Status: Experimental）: https://arxiv.org/abs/2608.05219
- PIRL（prompt-robust multimodal RLVR；Status: Experimental）: https://arxiv.org/abs/2608.08802
