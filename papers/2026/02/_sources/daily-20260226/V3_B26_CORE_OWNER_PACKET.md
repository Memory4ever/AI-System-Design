# B26 — 最后五项必要原证 / actual owner；非原作者已定点独核

2026-10-06 feb26_close_oct06 实际从各 exact-v1 raw 重定位以下 pID，读足采用命题与反证，并顺读 actual Ch4/5/23/29/66/82 必要相邻段。20804 E、20921/20967 Only、20971/21020 D，已同步本日 README；没有新 Books 写入或运行 artifact/复现。20921只识别有界 fixed-T/τL 与截断非负条件，不采用全 proof；20971另核§1–3/8，output-range缺项由f≡100反例明确。21020另核§3 value/occupancy与C.1 p3必要split，max差的反例与官方修正重开材料在Report；不自修、不以state-only有限观察改Only绕过中心rate争议。以下旧作者提案仍保留，当前终态以前述及Report为准。

## 2602.20804v1
https://arxiv.org/html/2602.20804v1

S4.SS1.p4.1 | This definition requires that memory is both beneficial (producing higher returns) and active (influencing decisions). We quantify this with a performance diagnostic, and with two complementary information-theoretic probes.

Thmdiagnosticbold1.p1.2 | We test \mathbf{H_{0}}:\ \mathrm{median}(\Delta_{\mathrm{Mem}})\leq 0 vs. \mathbf{H_{1}}:\ \mathrm{median}(\Delta_{\mathrm{Mem}})>0 using a one-sided Wilcoxon signed-rank test (Wilcoxon, 1945) over the paired differences. A significant result ( p<0.05 ) indicates a reliable performance advantage from memory under matched training.

S6.p3.1 | Evaluation Protocol. We train with 10 seeds, matching original training budgets, and evaluate every 5% of training (mean evaluation return over 32 episodes) (Gorsane et al., 2022). For aggregate comparisons, we report min–max normalised interquartile mean (IQM) with 95% stratified bootstrap CIs (Agarwal et al., 2021). Hyperparameters are tuned per scenario, full details in App. A.1.

S6.p4.1 | Algorithms. We use Independent PPO (De Witt et al., 2020, IPPO,) and Multi-Agent PPO (Yu et al., 2022, MAPPO,) as they are widely used MARL baselines. We treat them as two training paradigms: IPPO uses independent critics, whereas MAPPO uses a centralised critic. Additionally, we compare feed-forward (FF) and recurrent (RNN) policies to study the role of memory and temporal information flow in these settings. Finally, to avoid confounders from optimisation and representation choices associated with shared weights in heterogeneous tasks (Christianos et al., 2021; Tessera et al., 2025), we do not use parameter sharing in any baseline.

S7.p6.1 | A key take-away is that information-theoretic diagnostics can provide structured signals about how policies utilise observations and interact with other agents under the training distribution. When interpreted jointly, they can indicate whether behaviour appears observation-driven or convention-driven. However, these metrics quantify statistical dependence rather than causal relationships. As a result, high mutual information does not guarantee sensitivity to noise, and low values do not necessarily imply the absence of structured coordination. Careful behavioural evaluation alongside the use of diagnostics can however provide indications of robustness and generalisation of learned policies.

S8.p1.1 | Policy-dependent probes. All diagnostics are expectations under the converged joint policy p^{\boldsymbol{\pi}} and therefore characterise learned behaviour under IPPO/MAPPO with FF/RNN architectures, not worst-case or best-case properties of the environment. This is deliberate, as we probe behaviours induced by widely used algorithms; however, stronger or weaker algorithms may yield different diagnostic profiles for the same scenario.

S8.p2.1 | Estimation noise. Our MI/CMI/DI estimators (kNN and KSG (Kraskov et al., 2004)) are biased in finite samples, especially with long histories or large action spaces. We mitigate this via permutation null baselines that account for estimator-specific bias, and report bootstrap confidence intervals throughout. Nonetheless, these probes are diagnostic tools, not hard pass/fail filters, and borderline cases should be interpreted with caution.

## 2602.20921v1
https://arxiv.org/html/2602.20921v1

S3.I1.ix1.p1.1 | (Bounded data distribution) The data distribution \mathfrak{D} is supported in a bounded set, i.e., for all (\mathrm{d},\mathrm{g})\sim\mathfrak{D},\ \|\mathrm{d}\|_{2}+\|\mathrm{g}\|_{2}\leq B_{\rm in} for some B_{\rm in}>0 .

Thmtheorem5.p1.1 | (Generalization error for discrete-time ResNets) Assume assumptions ( {A}_{1} )-( {A}_{4} ) hold. Let the activation function \psi\in\mathscr{A}(\mathbb{R}) with \phi_{1},\phi_{2}\in\Gamma(\mathbb{R}) and \alpha,\beta>0 . Then there are constants {C}_{\mathcal{S}}^{l} dependent on data \mathcal{S} , 0\leq{C}_{\mathcal{S}}^{l}\leq\min\{\sqrt{S}\frac{1+2\mathrm{Lip}_{\psi}B_{\boldsymbol{\Theta}}}{2(\mathrm{Lip}_{\phi_{1}}\alpha+\mathrm{Lip}_{\phi_{2}}\beta)},S\} (l=1,\ldots,L) such that for any \delta\in(0,1) , with probability at least 1-\delta , every \mathrm{x}^{L}(\cdot;{\Theta}^{\rm total}_{L})\in{\mathcal{F}}^{L} satisfies

Thmtheorem7.p1.1 | The non-positive structural term in the generalization bound reflects a structural effect induced by the activation function. This term depends on several activation-related constants, including \mathrm{Lip}_{\phi_{1}} , \mathrm{Lip}_{\phi_{2}} , \alpha , and \beta . Note that the associated data-dependent quantities C_{\mathcal{S}}^{l} are introduced in an existential manner. Therefore, it is difficult to characterize explicitly for realistic network architectures and data distributions. Even for simplified settings, their precise values can be nontrivial to compute (see Example 3.1). As a result, it is generally difficult to quantitatively compare the tightness of different generalization bounds for the same model, or to derive explicit design rules for activation parameters. Nevertheless, this negative structural term theoretically reveals the potential role of activation function structure in improving generalization. From a practical perspective, this suggests that learning activation parameters (such as \alpha and \beta ) may enable the network to discover activation configurations that yield improved generalization performance. We will further explore this phenomenon empirically in the experimental section.

S4.SS2.p14.2 | Let {C}_{\mathcal{S}}^{l+1}=\min\{\sqrt{S}\frac{1+2\mathrm{Lip}_{\psi}B_{\boldsymbol{\Theta}}}{2(\mathrm{Lip}_{\phi_{1}}\alpha+\mathrm{Lip}_{\phi_{2}}\beta)},\bar{C}_{\mathcal{S}}^{l+1}\} , 0\leq l\leq L-1 . This truncation is introduced to ensure that the coefficients in the recursive inequality remain nonnegative, which is required for the application of the discrete Grönwall inequality. Then we get

S4.SS2.p14.3 | where 0\leq l\leq L-1 and 0\leq{C}_{\mathcal{S}}^{l+1}\leq\min\{\sqrt{S}\frac{1+2\mathrm{Lip}_{\psi}B_{\boldsymbol{\Theta}}}{2(\mathrm{Lip}_{\phi_{1}}\alpha+\mathrm{Lip}_{\phi_{2}}\beta)},S\} . By applying Grönwall’s inequality [13] to the inequality above together with \tau_{L}\cdot L=T , we get

CORE L3695–3695 原式/原段（不是修补）：
\displaystyle=\{{\Theta}^{\rm total}_{L}:{\Theta}^{\rm total}_{L}\in\mathcal{E}^{\rm pre}\times\mathcal{E}^{L},\|{\Theta}^{\rm total}_{L}\|_{\infty}\leq B_{\boldsymbol{\Theta}}\},

CORE L3743–3743 原式/原段（不是修补）：
\displaystyle=\{\boldsymbol{\Theta}^{\rm total}:\boldsymbol{\Theta}^{\rm total}\in\mathcal{E}^{\rm pre}\times(\mathcal{C}([0,T];\mathcal{E})\cap\mathcal{H}^{1}(0,T;\mathcal{E})),\|\boldsymbol{\Theta}^{\rm total}\|\!\leq\!B_{\boldsymbol{\Theta}}\}.

CORE L4143–4260 原式/原段（不是修补）：
\displaystyle 2\sqrt{2}nB_{\kappa}B_{\boldsymbol{\Theta}}\frac{M(T,\!\mathrm{Lip}_{\psi},\!n_{\mathrm{d}},\!B_{\rm in},\!B_{\boldsymbol{\Theta}})}{\sqrt{S}}\!+\!4B_{\ell}\sqrt{\frac{2\!\log(4/\delta)}{S}}
\displaystyle+(-2\sqrt{2})nB_{\kappa}B_{\boldsymbol{\Theta}}\frac{(\mathrm{Lip}_{\phi_{1}}\alpha\!+\!\mathrm{Lip}_{\phi_{2}}\beta)\exp(T\mathrm{Lip}_{\psi}B_{\boldsymbol{\Theta}}^{2})}{S}\!\tau_{L}\!\sum_{l=1}^{L}{C}^{l}_{\mathcal{S}},

## 2602.20967v1
https://arxiv.org/html/2602.20967v1

S2.SS1.p3.2 | Likewise, \epsilon is added to prevent zero division. The final output is obtained via Eq. (1) and decoded by the backend ASR.

S3.SS2.SSS2.p1.1 | We evaluate the proposed OA method using three ASR systems with diverse architectures and robustness levels. Whisper-large [25] and Parakeet [26, 27] are employed as strong, noise-robust ASR models, representing large-scale sequence-to-sequence and TDT-based transducer frameworks, respectively. For Whisper, we use the Whisper-large model, while for Parakeet we adopt the parakeet-tdt-0.6b-v2 model11 1 https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2. In addition, we include a wav2vec2-large ASR model [28] fine-tuned on the full LibriSpeech [32] labeled dataset22 2 https://huggingface.co/facebook/wav2vec2-large-960h, which serves as a comparatively weaker and more noise-sensitive CTC-based baseline. This setup allows us to evaluate OA under contrasting conditions where either noisy or enhanced speech may be preferred.

S4.SS1.p1.1 | Tables 3 and 3 compare various OA methods. WER-OA (Eq. 2) consistently achieves the lowest WER in all test cases, supporting the design of intelligibility-guided OA in Section 2.1. The proposed Conf-OA (Eq. 3) achieves the best overall practical performance, confirming ASR confidence as a reliable alternative in the OA task. We note three cases in Table 3 (CHiME-4 Simu+Whisper, CHiME-4 Simu+Parakeet, and CHiME-4 Real+Whisper) where Conf-OA slightly exceeds the WER of the noisy speech. This occurs when the relative performance gap between noisy and enhanced speech is large, making the weaker signal insufficient to improve the stronger one. Nevertheless, Conf-OA still outperforms other baselines, demonstrating greater robustness. We also observe that our 3-class classifier variant ( \text{Classifier-OA}_{3class} ) generally outperforms the original 2-class classifier ( \text{Classifier-OA}_{2class} ). However, it still requires training an explicit model, unlike the proposed training-free Conf-OA approach, which is much simpler by design and yield more robust performance.

S4.SS3.p1.1 | Table 4 compares utterance-level (Section 2.1) and frame-level (Section 2.3) using Conf-OA (Eq. 3). We observe performance degradation with frame-level OA. This is likely because frame-level fusion introduces inconsistent weighting across adjacent frames, disrupting the temporal continuity expected by the ASR. In contrast, utterance-level OA preserves global consistency, resulting in more stable recognition performance.

CORE L195–201 原式/原段（不是修补）：
′
)
×
x
^
\bar{x}=S^{\prime}\times y+(1-S^{\prime})\times\hat{x}
(1)

CORE L396–400 原式/原段（不是修补）：
^
)
,
S^{\prime}=\frac{\mathrm{conf}(y)}{\mathrm{conf}(y)+\mathrm{conf}(\hat{x})},
(3)

## 2602.20971v1
https://arxiv.org/html/2602.20971v1

S3.p3.1 | Throughout this subsection, assume Y\in[-1,1] almost surely and that f is L -Lipschitz. Define the robust squared loss

S9.SS4.SSS1.p2.1 | This quantity constitutes a lower bound on the global Lipschitz constant because it is restricted to observed sample directions rather than worst-case adversarial directions.

S9.SS5.p3.1 | In particular, for these low-capacity models, the network outputs (logits) appear to be predominantly negative across certain subsets of the data. After applying the transformation \tilde{f}(x)=\tanh(f(x)) , this leads to outputs saturating near -1 . As a result, differences of the form |\tilde{f}(x_{i})-\tilde{f}(x_{j})| collapse to zero for many pairs of inputs, yielding an empirical Lipschitz estimate of zero. We drop these values to ensure consistency in evaluation.

S10.p1.1 | This is the first approach towards unifying notions of robustness, i.e., worst-case robustness and robust generalization eror as pointed out by (Bubeck and Sellke, 2021). We also want to generalize our approach to Bregman Divergence losses. As seen in the experiments, there is a clear discrepancy: we perform classification with cross-entropy loss, while our theoretical results are derived for square losses. We also aim to improve the bounding of loss using local Lipschitz notions, thereby strengthening our bounds. In future versions, we also intend to use local Lipschitz constants for the radius of the cover itself. Additionally, we believe that Distributional Robustness can be linked with robust generalization, thus unifying different notions of robustness. On the empirical side, we also plan to run experiments on datasets beyond MNIST, namely CIFAR and ImageNet, thereby broadening the scope of the paper.

CORE L861–985 原式/原段（不是修补）：
Throughout this subsection, assume
Y
∈
[
−
1
,
1
]
Y\in[-1,1]
almost surely and that
f
f
is
L
L
-Lipschitz. Define the robust squared loss
ℓ
ρ
​
(
f
,
(
x
,
y
)
)
≔
sup
‖
δ
‖
≤
ρ
(
f
⁡
(
x
+
δ
)
−
y
)
2
.
\ell_{\rho}(f;(x,y))\coloneqq\sup_{\left\lVert\delta\right\rVert\leq\rho}\bigl(f(x+\delta)-y\bigr)^{2}.
Since
f
f
is
L
L
-Lipschitz, for any
‖
δ
‖
≤
ρ
\left\lVert\delta\right\rVert\leq\rho
we have
|
f
⁡
(
x
+
δ
)
−
y
|
≤
|
f
⁡
(
x
)
−
y
|
+
|
f
⁡
(
x
+
δ
)
−
f
⁡
(
x
)
|
≤
2
+
L
​
ρ
,
|f(x+\delta)-y|\leq|f(x)-y|+|f(x+\delta)-f(x)|\leq 2+L\rho,
and hence the robust loss is uniformly bounded by
0
≤
ℓ
ρ
​
(
f
,
(
X
,
Y
)
)
≤

CORE L3444–3444 原式/原段（不是修补）：
\mathcal{B}_{L}\coloneqq\{f:\mathcal{X}\to[-1,1]:f\ \text{is $L$-Lipschitz}\}.

CORE L3617–3617 原式/原段（不是修补）：
\mathfrak{R}(\ell_{\rho}\circ\mathcal{B}_{L}\circ S)\leq 2\,\mathfrak{R}(\ell\circ\mathcal{B}_{L}\circ S).

## 2602.21020v1
https://arxiv.org/html/2602.21020v1

S4.SS2.p4.1 | Let the learned policy be the constant \pi((a_{1},a_{2})|s)=1 such that \mu_{\pi}=\mu_{\pi^{E}} and V_{2}^{\pi}(\nu_{U})=-\frac{1}{1-\gamma} . Noting that V_{2}^{\pi^{E}}(\nu_{U})=\frac{2/3}{1-\gamma} , this concludes the proof as:

S4.SS3.p1.1 | Assuming again state-action matching, we show that full-state support is essential for learning a Nash equilibrium in general games. We draw on the example given by Tang et al. (2024, Figure 2) to point out issues from a non-visited region \mathcal{S}^{-}_{\pi^{E}}\neq\emptyset and derive the following theorem.

S6.SS1.p7.1 | A Nash equilibrium of this game is the constant policy \pi^{E}((a^{r}_{1},a^{c}_{2})|s)=1 for all s\in\mathcal{S} . The expert is such that \mu_{\pi^{E}}(s_{\text{exp}})\leq\epsilon/2 . Therefore, the policy \pi((a_{1},a_{2})|s)=\pi^{E}((a_{1},a_{2})|s) if s\neq s_{\text{exp}} and \pi((a^{r}_{1},a^{c}_{1})|s_{\text{exp}})=1 , has BC error at most \epsilon .

S6.SS1.p8.1 | A best-response to \pi_{2} is the constant policy \pi^{*}_{1}(a^{r}_{2}|s)=1 for all s\in\mathcal{S} which incurs \mathbb{E}_{s\sim\mu_{\pi^{E}}}\left[\left\lVert\pi^{*}_{1}(\cdot|s)-\pi^{E}_{1}(\cdot|s)\right\rVert_{1}\right]=2 . Note that G has a consistent bound for any error assumption ( \epsilon_{\text{BC}}=0\Leftrightarrow\epsilon_{\mu}=0\Leftrightarrow\epsilon_{\rho}=0 for G , and \mathcal{S}^{+}_{\pi^{E}}=\mathcal{S} ). ∎

Thmlemma3.p1.1 | Suppose \pi^{E} is a (weak) Dominant Strategy Equilibrium. Then, any learned policy \pi with BC error \epsilon_{\text{BC}} satisfies \operatorname{NashGap}(\pi)\leq 2n\epsilon_{\text{BC}}/(1-\gamma)^{2} .

Thmlemma4.p1.1 | Suppose the equilibrium expert is \pi^{E} and the game is \delta -continuous at \pi^{E} . Then, \operatorname{NashGap}(\pi)\leq\frac{2n\epsilon_{\text{BC}}+\delta(\epsilon_{\text{BC}})}{(1-\gamma)^{2}} .

S6.SS3.SSS0.Px1.p1.1 | Consistence and tractability properties of the bound are directly related to the properties of the \delta function: the bound is consistent if \delta(0)=0 and it is tractable if \delta itself is tractable. Lemma 4 then provides the key insight that deriving exploitability upper bounds reduces to characterizing \delta for the considered game.

## actual owner — books/part-01-worldview/04-why-models-learn.md

L41–55:
神经网络“能够学习”至少包含三个不同命题。

第一是 **representation capacity**：模型函数族里是否存在一个足够好的函数。Universal Approximation 一类结果讨论的是特定条件下的表示能力。它说明某些网络可以逼近一类函数，但不告诉我们需要多少参数、多少数据，也不保证训练算法能找到那组参数。

第二是 **optimization**：从当前参数出发，算法能否在可接受时间和资源内找到低训练损失区域。一个好解存在，不代表梯度下降一定到达；loss surface、初始化、数值精度、batch 噪声和学习率都会影响路径。

第三是 **generalization**：训练集上的低误差能否延续到未见样本。即使模型把训练集完全记住，经验风险也可以很低，但真实业务分布上的风险仍可能很高。

可以把三者写成三个不同问题：

```text
Can the function family express a useful solution?
Can optimization find a useful solution?
Will the solution work beyond the training samples?
```

## actual owner — books/part-01-worldview/05-what-neural-networks-learn.md

L242–267:

```text
correlation: an activation co-occurs with a concept
prediction: an activation can predict a concept label
causation: changing the activation changes model behavior as claimed
```

线性 probe 能从表示中读出信息，不一定证明模型在原任务中使用了该信息；干预某个方向导致输出变化，也需要排除连带影响。可解释性不是给每个参数命名，而是建立可复现、可反驳的内部机制证据。

### 从可读出到机制：证据应逐级变强

内部分析至少要区分一条证据阶梯：

```text
behavioral correlation
→ decodability
→ localized intervention
→ downstream behavioral change
→ cross-context / cross-model replication
```

前两层可以发现“某种信息存在于 activation 中”，却没有证明原始 forward path 依赖它。
更强的主张需要在控制混杂因素的前提下修改候选表示，并观察预期的 downstream computation
或行为是否随之改变；即使如此，单个 prompt、单个模型家族或局部线性近似上的效果仍不是
完整机制。


## actual owner — books/part-06-ai-infrastructure/66-evaluation-system.md

L36–47:

- 测试集是否进入过训练数据？
- 三分提升是否来自某个高频 slice，还是所有关键场景都改善？
- prompt、tokenizer、retriever、runtime 和 sampling 是否与生产一致？
- scorer 测量的是格式、事实、任务成功，还是用户偏好？
- 结果方差有多大，重复运行是否稳定？
- 延迟、成本、安全和少数高风险失败是否恶化？
- benchmark 分布是否仍代表当前生产请求？

再把用户点赞作为标准，也会遇到新问题：愿意反馈的用户不是随机样本；推荐和路由策略改变了谁会看到结果；短期满意不代表事实正确；高风险失败可能数量少，却不能被平均值抵消。

问题不在于分数无用，而在于**任何分数都是在某个对象、分布、环境和测量方法下产生的条件性证据**。丢掉条件，只留下数值，评估就会退化为不可解释的排行榜。

## actual owner — books/part-03-multimodal-world-models/23-multimodal-representation.md

L37–47:
## 一个思想实验：同样是 256 个 token

假设系统收到三段长度都为 256 的 token：一段文本、一张图像和一秒音频。对 Transformer 来说，它们都可以成为 `[256, d]`；对系统设计来说，它们完全不同。

- 文本 token 可能覆盖 150～250 个词，并保持严格顺序。
- 图像 token 可能来自 `16 × 16` patch grid，邻接关系是二维的。
- 音频 token 可能覆盖固定时间窗，边界取决于采样率和 codec stride。

把 shape 统一，只解决了“可以送进同一算子”；没有回答空间位置、时间同步、信息损失、重建能力或跨模态指代。**Tensor compatibility 不是 semantic compatibility。**

由同一个输入派生另一种模态，还要分开“表示更容易被读取”和“取得了新环境信息”：把文本送入 TTS，再由 speech encoder 提供辅助表示，会引入生成模型的 prior、声学形式与计算，但没有重新观察原说话者或现场。[受限翻译对照](https://arxiv.org/html/2602.21646v1)中，text+synthetic speech 与 text+authentic speech 的两个平均指标相近且都高于 text-only，支持该模型的表示替代，不证明所有语音信息都仅来自文本或合成 prosody 等于原声。应保存原 text、TTS/encoder与配对身份，分别评价任务收益、声学信息损失与真实新增 observation；派生模态不能作为独立事实源。TTS、speech encoding、额外 token/训练和自筛选费用仍需结算，部分语言也有指标反退；text 已足够、现场声学不可丢或表示回归时，保留 text-only、原始语音及专用声学接口，而不以多一个模态名称认证独立证据。<!-- source-family:SF-2026-ARXIV-2602-21646 -->

## actual owner — books/part-04-training-system/29-sft.md

L214–221:
- 多轮上下文与工具结果是否自洽。
- 不同 domains、语言与难度是否平衡。
- Synthetic data 是否经过 verifier 或抽样人工检查。

使用更强模型生成 synthetic demonstrations 可以扩大覆盖，却可能复制 teacher 的错误、偏好和措辞。过滤器与 judge model 也会引入自己的 selection bias。

### 离线 Feedback 可以先编译成显式 Goal Conditioning


## actual owner — books/part-07-agent/82-multi-agent.md

L62–74:

```text
single reasoning locus
→ independent parallel exploration
→ centralized verification
→ decentralized communication
→ task-dependent hybrid topology
```

每一步解决不同边界。Independent 让可分解搜索并行，却缺少跨结果纠错；centralized
verification 截断部分错误传播，但形成 bottleneck；peer communication 提供更多局部信息，
也会分裂全局 Context 并拉长 critical path。旧方案没有被后者否定：顺序约束强、工具密集或
单 Agent baseline 已较高时，统一 Context 往往比协调更重要。
