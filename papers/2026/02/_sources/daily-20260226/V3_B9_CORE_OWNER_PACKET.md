# B9 — 必要原证＋实际owner（3项，非整日验收）

## 2602.20696v1
https://arxiv.org/html/2602.20696v1；精确HTML原paragraph机械摘段：

Just as LLMs conditioned on positive ( P ) and negative ( N ) prompts yield distinct probability distributions  \mathbb{P}^{(P)}  and  \mathbb{P}^{(N)} , VLMs conditioned on these prompts exhibit distinct visual attention patterns.
We define  A_{l}^{(P)}(\mathcal{I})  as the attention distribution at layer  l  under the positive prompt, which captures behavior-specific positive signals (e.g., semantic relevance to the question).
Conversely, we define  A_{l}^{(N)}(\mathcal{I})  as the attention under the negative prompt, which primarily reflects generic negative patterns (e.g., visual saliency or noise) shared across contexts.
PromptCD leverages this analogy by contrasting these attention maps— A_{l}^{(P)}(\mathcal{I})  versus  A_{l}^{(N)}(\mathcal{I}) —to isolate and amplify the task-relevant visual grounding signals, similar to how it contrasts token probabilities in LLMs.

While contrastive scoring effectively highlights discriminative features, it introduces a risk of the “amateur correction” pathology.
Specifically, a token that is extremely unlikely under the negative prompt (very large negative  \log\mathbb{P}^{(N)} ) might receive an artificially inflated score after subtraction, even if it is nonsensical in the positive context.
To mitigate this and ensure the semantic fluency of the generated text, we adopt the Adaptive Plausibility Constraint (APC) [36].
This constraint imposes a dynamic validity mask, restricting the candidate pool  \mathcal{V}_{\text{head}}  to only those tokens that are already plausible under the positive prompt:

A distinct structural feature of PromptCD, which differentiates it from standard re-ranking or layer-contrastive methods [17], is the simultaneous maintenance of two synchronized generation trajectories.
Although the generation is guided by the contrastive distribution, the resulting token must maintain coherence in both prompt contexts to allow for iterative contrast.
Let  x^{*}_{t}  be the token sampled from the adjusted distribution  \hat{\mathbb{P}}(x_{t})  (Eq. 6).
Crucially, this single selected token is appended to both the positive and negative context buffers before proceeding to step  t+1 :

where  \otimes  denotes the Hadamard product.
Under the negative prompt, which provides only generic cues (e.g., ”Write a general description of the image”), the behavior-specific signal becomes approximately uniform, causing attention to primarily reflect the generic pattern:  A_{l}^{(N)}(\mathcal{I})\approx\mathcal{F}^{(-)}(\mathcal{I}) .

We investigate the sensitivity of PromptCD to the adjustment coefficient  \gamma , which governs the magnitude of the penalty applied to the negative logits (i.e., the strength of suppression).
For all reported experiments on text-only LLMs, we uniformly set  \gamma  to 0.5.
The detailed ablation results are presented in Table V.
We observe that performance follows an inverted U-shape trend: an excessively small  \gamma  fails to sufficiently amplify the contrast between positive and negative contexts, while an overly large  \gamma  may disrupt the model’s linguistic coherence.
The results empirically confirm that a moderate  \gamma  yields the optimal balance, effectively steering the behavior without degrading generation quality.

Since PromptCD necessitates dual forward passes at each decoding step, it inevitably incurs computational overhead.
Table VII reports the inference latency comparison evaluated on the NQ dataset, indicating that our method results in a  1.6\times – 1.8\times  overhead in latency and throughput compared to standard decoding.
While this cost is non-negligible, we argue that it is a justifiable trade-off for safety-critical and high-stakes applications—such as those in medical, financial, or legal domains.
In these scenarios, factual errors, unmanaged knowledge conflicts, or safety violations can have severe consequences.
Therefore, the marginal increase in computational cost is outweighed by the substantial gains in reliability, trustworthiness, and the capability for precise, human-in-the-loop behavioral governance.

## 2602.20708v1
https://arxiv.org/html/2602.20708v1；精确HTML原paragraph机械摘段：

We first compute the generation-normalized token entropy for each query  i  to align the focus intensity with the generation scale:

Feature Fusion and Prober Architecture. To construct a comprehensive representation, we select a subset of  K  attack sensitive layers  \mathcal{L}^{*}\subseteq\{1,\dots,L\} , based on FIS of each layer. The global feature vector  \mathbf{z}  is formed by concatenating head-wise features across all selected layers:

In this formulation,  \gamma<1  functions as an intensive suppression coefficient. This mechanism is conducted before multi-head attention softmax mechanism that exploits the Softmax redistribution effect: by diminishing anomalous attention peaks, the subsequent normalization naturally reallocates focus toward the benign task context (where  M_{l,h}=0 ). This selective re-weighting effectively performs latent-level signal-to-noise enhancement, restoring the agent’s functionality without damaging the global semantic structure.

Datasets. We utilize two widely used datasets, InjectAgent (Zhan et al., 2024) and AgentDojo (Debenedetti et al., 2024) to evaluate the effectiveness of ICON. For training, we adopt TrojanTools (Anonymous, 2025), which provides diverse tool selections in order to demonstrate the out-of-distribution capability of our ICON. For visual tasks, we utilize Visual Prompt Injection Benchmarks (Wan et al., 2024) provided by Meta.

Notes: ADR = Attack Detection Rate. URR = Utility Recover Rate.
Values are reported with standard deviations computed over 5 cross validation.

## 2602.20715v1
https://arxiv.org/html/2602.20715v1；精确HTML原paragraph机械摘段：

This formulation adaptively modulates exploration: high variance during non-interaction phases encourages diverse trajectory exploration, while low variance during interaction phases enforces precise, stable execution—seamlessly bridging the discrete visual-derived interaction signal  I_{t}  with continuous policy uncertainty modulation.

where  \beta  is the temperature hyperparameter for AWR, and  \hat{a}_{\tau}  denotes the flow trajectory at time  \tau . This objective upweights data with higher estimated advantages while preserving the flow ODE structure for stable policy refinement.

For each task, we collect 60 expert demonstrations via teleoperation to form the initial dataset  \mathcal{D}_{\text{demo}} . During the Human-in-the-Loop stage, we perform 10 rollouts per training update and add them to  \mathcal{D}_{\text{real}}  for IG-AWR updates, iterating 4 times (totaling 40 rollouts). For fair comparison, baseline methods without Human-in-the-Loop utilize 100 expert demonstrations. The metric is Success Rate (SR), defined as the ratio of successful trials to the total number of attempts.

Beyond final performance, we further investigate the impact of IG on data efficiency in Figure 5. IG-RFT is represented by the red curve, while the baseline AWR w/ dense reward is represented by the blue curve and AWR w/o dense reward by the gray curve. Our method exhibits a significantly steeper learning trajectory. IG-RFT achieves an average success rate of 77.5% with only 40 human interventions, and ultimately converges to an 82.5% success rate. The AWR w/ dense reward method learns more slowly, reaching only 62.5% under the same 40 human interventions. This demonstrates that our method achieves superior performance with significantly lower human cost. Even when the data scale is extended to 70 episodes, the baseline without IG fails to match the peak performance of IG-RFT. This confirms that modulating exploration based on visual interaction signals not only improves policy performance but also drastically reduces the human effort required for fine-tuning. The other baseline, AWR w/o dense reward, further validates this conclusion and highlights that our dense reward is equally significant for policy improvement in Human-in-the-Loop learning.

As a powerful and effective policy improvement technique, RL possesses the potential to enable SFT models to break through the upper limit of their representation capability. However, existing research, including this work, tends to utilize RL as a fine-tuning method to bridge the domain gap and improve task success rates, rather than applying RL to large-scale training as seen in Large Language Models (LLMs) [62, 63]. We attribute this to two main reasons: 1) Sampling and exploration using policy gradient-based online RL (like GRPO, PPO) [64, 65] in the high-dimensional action space of the real world are expensive, while simulation faces a significant sim-to-real gap, and Human-in-the-Loop guidance relies heavily on manual labor, making it difficult to scale up. 2) A general Reward Model that can be directly applied to fully on-policy, online, and new real-world domains does not yet exist; the lack of real-time feedback from such a model poses significant challenges for real-robot on-policy learning.

### 20696 原正文txt L1193–1283
)
)
,
\hat{\mathbb{P}}(x_{t})=\mathrm{softmax}\left(\mathcal{F}\left(\mathbb{P}^{(P)}(x_{t}),\mathbb{P}^{(N)}(x_{t})\right)\right),
(6)
where the operator
ℱ
⁡
(
⋅
,
⋅
)
\mathcal{F}(\cdot,\cdot)
computes the token-level logits modification.
Drawing inspiration from Contrastive Decoding
[
36
]
, we formulate this operator as a weighted subtraction in the log-probability space.
This operation is mathematically equivalent to maximizing the mutual information between the token and the positive control signal, while minimizing the influence of the negative prior:
ℱ
⁡
(
⋅
)
=
{
log
⁡
ℙ
(
P
)
​
(
x
t
)
−
γ
⋅
log
⁡
ℙ
(
N
)
​
(
x
t
)
,
if
​
x
t
∈
𝒱
head
,
−
∞
,
otherwise
,
\mathcal{F}(\cdot)=\begin{cases}\log\mathbb{P}^{(P)}(x_{t})-\gamma\cdot\log\mathbb{P}^{(N)}(x_{t}),&\text{if }x_{t}\in\mathcal{V}_{\text{head}},\\
-\infty,&\text{otherwise},\end{cases}
(7)
where
γ
≥
0
\gamma\geq 0
is a critical hyperparameter serving as the
contrastive coefficient
.
This coefficient controls the strength of the penalty applied to the negative distribution.
Intuitively, for high-frequency stop words or generic tokens where
ℙ
(
P
)
≈
ℙ
(
N
)
\mathbb{P}^{(P)}\approx\mathbb{P}^{(N)}
, the subtraction significantly dampens their scores.

### 20708 原正文txt L1310–1450
k
k
ratio
τ
\tau
. Specifically,
θ
l
,
h
\theta_{l,h}
is determined as the
(
1
−
τ
)
(1-\tau)
-th percentile of the attention weights in head
h
h
, defining the
saliency budget
for intervention. The steering mask
M
l
,
h
M_{l,h}
is formally defined as:
M
l
,
h
​
(
i
,
j
)
=
𝕀
⁡
(
a
l
,
h
​
(
i
,
j
)
≥
θ
l
,
h
)
,
M_{l,h}(i,j)=\mathbb{I}\big(a_{l,h}(i,j)\geq\theta_{l,h}\big),
(11)
where
a
l
,
h
​
(
i
,
j
)
a_{l,h}(i,j)
is the raw attention weight and
𝕀
⁡
(
⋅
)
\mathbb{I}(\cdot)
denotes the indicator function.
•
Steering Intensity (
γ
\gamma
):
We apply a
Contrastive Steering Operation
to the attention matrix using the coefficient
γ
\gamma
:
A
~
l
,
h
=
A
l
,
h
⊙
[
1
+
M
l
,
h
⋅
(
γ
−
1
)
]
.
\tilde{A}_{l,h}=A_{l,h}\odot[1+M_{l,h}\cdot(\gamma-1)].
(12)
In this formulation,
γ
<
1
\gamma<1
functions as an intensive suppression coefficient. This mechanism is conducted before multi-head attention softmax mechanism that exploits the Softmax redistribution effect: by diminishing anomalous attention peaks, the subsequent normalization naturally reallocates focus toward the benign task context (where
M
l
,
h
=
0
M_{l,h}=0
). This selective re-weighting effectively performs latent-level signal-to-noise enhancement, restoring the agent’s functionality without damaging the global semantic structure.
Table 2:
Evaluation of
ICON
against IPI attacks on various agentic LLMs.
FMs

### 20708 原正文txt L1765–1818
Table 3:
OOD Performance of
ICON
trained on TrojanTools.
Model
Metric
InjectAgent
AgentDojo
No Def.
ICON (Ours)
No Def.
ICON (Ours)
Qwen-3-8B
ADR
0%
80.1%
±
\pm
1.9
0%
98.0%
±
\pm
1.2
URR
0%
62.3%
±
\pm
2.3
0%
69.6%
±
\pm
2.7
LLaMA-3.1-8B
ADR
0%
85.4%
±
\pm
1.3
0%
97.3%
±
\pm
1.8
URR
0%
47.6%
±
\pm
3.1
0%

### 20715 原正文txt L555–590
Methodology
IV-A
Interaction-guided AWR for Flow Matching
In complex long-horizon robotic manipulation tasks, achieving an optimal balance between exploration and exploitation remains a critical yet unresolved challenge. Conventional RL methods often suffer from detrimental exploration during delicate operations. To address this, we decompose episodes into non-interactive phases (e.g., approach, retraction), where we encourage exploration for trajectory diversity, and contact-rich interaction phases (e.g., handover, grasping), where we prioritize precision and stability. Specifically, we first introduce the extraction of interaction signals, followed by their application to the RL fine-tuning of flow-based VLA models.
Fig. 2:
Illustration of Dynamic Uncertainty Modulation in IG-AWR.
This mechanism modulates the initial sampling noise
ϵ
\epsilon
of the flow ODE based on the extracted interaction signal
I
t
I_{t}
. During non-interaction phases (top), a higher variance
σ
high
\sigma_{\text{high}}
is applied to encourage diverse trajectory exploration. Conversely, during interaction phases (bottom), the variance is reduced to
σ
low
\sigma_{\text{low}}
to ensure precision and stability for contact-rich manipulation.
IV-A
1
Interaction Signal Extraction
Efficient and autonomous interaction labeling is crucial for processing VLA demonstrations. Leveraging global visual observations, at each time step
t
t
, we first employ the robot segmentation model, RoboEngine
[
55
]
, to generate a binary robot mask
M
t
M_{t}

### 20715 原正文txt L676–762
excludes robot pixels to focus on environmental motion. We count the pixels where the squared flow magnitude
‖
F
t
(
u
,
v
)
‖
2
||F_{t}^{(u,v)}||^{2}
exceeds the threshold
δ
flow
\delta_{\text{flow}}
. If this count exceeds
Θ
pixel
\Theta_{\text{pixel}}
, the time step is labeled as an interaction phase (
I
t
=
1
I_{t}=1
).
IV-A
2
Dynamic Uncertainty Modulation
During the rollout phase, as illustrated in Figure
2
, we dynamically regulate the variance of the initial sampling noise conditioned on the predicted interaction signal probability. Building directly on the binary interaction labels derived from visual observations (Section
IV-A1
), the critic network predicts
p
int
​
(
s
)
∈
[
0
,
1
]
p_{\text{int}}(s)\in[0,1]
—a soft estimate of interaction likelihood for the state, trained to approximate the ground truth. We define the effective sampling temperature
𝒯
⁡
(
s
)
\mathcal{T}(s)
as:
𝒯
⁡
(
s
)
=
σ
base
⋅
(
1
−
α
⋅
p
int
​
(
s
)
)
+
σ
min
\mathcal{T}(s)=\sigma_{\text{base}}\cdot(1-\alpha\cdot p_{\text{int}}(s))+\sigma_{\text{min}}
(2)
The policy generates actions by solving the flow ODE starting from a scaled noise distribution. Specifically, the initial state
a
^
0
\hat{a}_{0}

### 20715 原正文txt L1612–1684
Ablation Studies
To validate our design choices, we conduct ablation studies on the
Parcel Packing
and
Drink Shelving
tasks, which demand the most complex manipulation capabilities. This section answers
Q2
.
V-C
1
Effect of Interaction-Guided AWR
We compare our IG-AWR with a standard AWR implementation that also follows the three-stage training recipe but uses uniform exploration noise. As illustrated in Table
II
, removing the interaction-guided dynamic uncertainty modulation results in a performance drop of approximately 15%. Qualitative analysis reveals that without interaction guidance, the robot tends to jitter during the delicate ”flap folding and box closing” phase. Furthermore, we observe that without interaction guidance, the agent lacks sufficient exploration during non-interactive phases, leading to poor generalization regarding object positions. It often drifts towards the object locations seen in the pre-collected data, consequently causing task failure when facing out-of-distribution (OOD) cases during testing.
Beyond final performance, we further investigate the impact of IG on data efficiency in Figure
5
. IG-RFT is represented by the red curve, while the baseline AWR w/ dense reward is represented by the blue curve and AWR w/o dense reward by the gray curve. Our method exhibits a significantly steeper learning trajectory. IG-RFT achieves an average success rate of 77.5% with only 40 human interventions, and ultimately converges to an 82.5% success rate. The AWR w/ dense reward method learns more slowly, reaching only 62.5% under the same 40 human interventions. This demonstrates that our method achieves superior performance with significantly lower human cost. Even when the data scale is extended to 70 episodes, the baseline without IG fails to match the peak performance of IG-RFT. This confirms that modulating exploration based on visual interaction signals not only improves policy performance but also drastically reduces the human effort required for fine-tuning. The other baseline, AWR w/o dense reward, further validates this conclusion and highlights that our dense reward is equally significant for policy improvement in Human-in-the-Loop learning.
TABLE II:
Ablation Study Results.
We evaluate the contribution of Interaction Guidance (IG) and Reward Function on the two most challenging tasks.
Configuration
Parcel
Packing
Drink
Shelving
Avg. Drop
Ours (Full System)
85.0
70.0
-
w/o Interaction Guidance
70.0
55.0
↓
\downarrow
15.0
w/o Trajectory-level Reward
75.0
60.0
↓
\downarrow
10.0
w/o Subtask-level Reward
55.0
45.0
↓
\downarrow
27.5
TABLE III:
Subtask Completion Progress.
Instead of binary success rates, we report the normalized progress score (0.0-1.0), representing the average proportion of subtasks completed per episode. This metric reveals when the policy fails.
Reward Configuration
Parcel
Packing
Drink
Shelving
Avg. Progress
Ours (Hybrid)
0.96
0.88
0.92
w/o Trajectory Reward
0.84
0.78
0.81
w/o Subtask Reward
0.68
0.54
0.61
Fig. 5:
Data Efficiency Analysis in Human-in-the-Loop Fine-tuning.
We report the mean success rates averaged over the Parcel Packing and Drink Shelving tasks. The curves show that IG-RFT (Ours) achieves superior sample efficiency, converging to 77.5% success with only 40 interventions, significantly outperforming baselines. Shaded regions indicate the min-max range across tasks.
V-C

## Actual owner books/part-02-model/20-sampling.md

### 原文件L145–168
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

## Actual owner books/part-06-ai-infrastructure/72-security.md

### 原文件L2257–2270

<!-- semantic-body-binding:SF-2026-ARXIV-2605-00236:start -->
#### Component Ablation 不是 Routing Robustness

定位少数与拒答强相关的 attention heads，并用 ablation 检查其必要性，是合理的静态诊断：它能告诉安全团队应把 sensor 放在哪里。但 residual compensation 使“删除一个组件”与“让组件继续存在却把 attention 分配到错误位置”成为两种不同干预。攻击者若能在不改变表面语义的 token 上重定向 routing，下游残差流仍可能收到被稀释或错配的 safety signal；因此 head 的存在、幅度或单次 ablation 都不能独自承担 release evidence。

更完整的 defense evaluation 要把模型、tokenizer、alignment revision、被测 heads、输入预算和 white-box 能力写入 threat identity，同时比较 component removal、attention redistribution 与 held-out prompts。安全头只拥有观测信号，policy gateway 仍拥有拒绝或放行权；routing 指标漂移、模型不可见或攻击优化超出校准域时，应回退到输出策略、工具授权、隔离执行和人工升级，而不是由内部 attribution 自证安全。

这条路径用逐模型校准、额外白盒计算和更高误报风险换取对“组件仍在但控制流已被改写”的可见性。exact-v1 证据只覆盖 LLaMA-3-8B、Mistral-7B、Gemma-2-9B 与 200 条 HarmBench prompts，且同一批样本参与 head calibration 和评估、拒答由关键词 classifier 判定；它不证明闭源 API、更大模型或未见攻击具有相同成功率，也不把 attention 相关性升级为普适因果机制。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-00236:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-18619:start -->
Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-18619:end -->

## Actual owner books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

### 原文件L657–678
策略池固定且工作条件稳定时，为一次任务选择全局最优 expert 是可解释且低成本的。策略池持续增长后，选择问题分裂为两个控制动作：为新条件 commissioning 现有 expert，以及判断新 candidate 是否补足 incumbent 的真实 failure gap。VLA owner 因此要持有 condition split、outcome-disjoint probe、candidate version、probe budget 与 onboarding decision，只在新策略覆盖现有池无法处理的失败区间时提交上线。论文在 cost-matched probe budget 和五个 expert 上报告 held-out 60.53%、相对基线提升 1.64 个百分点；这不证明更大策略池、分布漂移或物理安全约束下仍成立。probe 泄漏、样本不足和错误 onboarding 会污染路由；置信度或 coverage 不足时保留 incumbent/default controller，并让人工或保守策略接管。

### Fleet 学习必须把部署、干预与再部署组成版本循环

离线 imitation 或一次性 RL 在环境稳定、人工演示足够时最容易复算；真实 fleet 上的新 failure 却只会在部署后暴露。若只把人工接管片段丢回通用 replay buffer，系统会失去当时的 policy、embodiment、observation frontier 和 intervention reason，无法判断新策略究竟修复了什么。持续学习因此应保存一条版本化循环：

```text
deployed policy revision + embodiment/environment identity
→ intervention and outcome receipt
→ offline value/policy update on frozen evidence
→ bounded online correction under a safety envelope
→ canary redeployment or rollback
```

deployment owner 持有生效 revision，teleoperation/intervention service 持有接管事实，training run 只产生 candidate policy，controller 与 safety monitor 仍拥有动作提交和 veto。该循环获得更贴近失败前沿的数据，却引入 on-policy exploration risk、选择偏差、版本碎片和旧能力退化；干预稀疏、奖励不可信或物理 blast radius 无法隔离时，应停在离线更新、simulation/shadow evaluation 和人工审批，不把“来自真实 fleet”误写成安全证明。

<!-- source-family:SF-LWD-FLEET-OFFLINE-ONLINE-ROBOT-RL -->

<!-- semantic-body-binding:SF-2026-ARXIV-2604-13645:start -->
多来源对齐也不能以抹去所有 domain 信息为目标：同类观测在模拟与真实系统中可能对应不同动作分布，完全域不变会把动作所需的区别一起丢掉。一条条件分支显式保留 domain condition，同时对齐其余表示；混合比例因而不只是样本条数的重加权，还会改变表示与条件行为。它与前述 action schema 对齐不同，解决的是哪些域差异应保留，而不是把模拟观测认证为真实事实。

域标签、对齐训练和真实校准带来额外成本，标签错误或对齐失败也会放大负迁移。Sim-and-Real Co-Training exact-v1 只在有限三任务、balanced regime 下做真机验证；普通 ADDA/OT 的平均结果还低于直接混训，组合结果不证明域条件对所有 VLA 必需。域差异小、标签不可靠或证据不足时，real-only、普通 mixture 和保守真实微调继续成立，latent 对齐不能替代下游物理验收。
