# GradLoc 本窗官方材料

原始入口：https://hunyuan.tencent.com/research/100015 。2026-10-04实际只读POST api.hunyuan.tencent.com/api/blog/publicDetail，body {"id":100015}。本次默认en响应原字段：{"id":100015,"title":"Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping","lang":"en","publicAt":1770971763,"publishedAt":1770971763,"displayPublishTime":1770971763,"publishVersionId":"d67ds4c2c3m0lbl55ud0"}。en公开字段1770971763即2026-02-13T16:36:03+08:00；root定点zh原字段1770971794即16:36:34，均在本窗，语言版本差31秒，不虚合单精确秒。无新arxiv身份已匹配，按官方项目 family 单计。

**GradLoc Code Repository:** [Tencent-Hunyuan/GradLoc](https://github.com/Tencent-Hunyuan/GradLoc)

![intro.png](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026021315360057_f85ade3b58295f1a75f875eb438a10a8.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770968168;2086328168&q-key-time=1770968168;2086328168&q-header-list=&q-url-param-list=&q-signature=c7b5d1c3b8b2765e988c06f13f380029fc395820)
*!12 Figure 1: From black-box heuristics to white-box diagnostics for RLVR training collapse. !*

# Key Takeaways

<div style="background-color: #f0f7ff; border-left: 5px solid #2563eb; border-radius: 6px; padding: 20px 24px; margin: 20px 0 40px 0; clear: both; box-shadow: 0 2px 5px rgba(0,0,0,0.05); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;word-wrap: break-word; overflow-wrap: break-word; word-break: normal;">
  <div style="display: flex; align-items: center; margin-bottom: 12px;">
    <span style="font-size: 20px; margin-right: 8px;">🔥</span>
    <div style="margin: 0; color: #1e40af; font-size: 18px; font-weight: 700;">Key Takeaways</div>
  </div>
  <ul style="margin: 0; padding-left: 20px; color: #334155; line-height: 1.6;">
    <li style="margin-bottom: 12px;">
	<strong style="color: #1e3a8a;">RLVR Training Collapse with Gradient Spikes</strong>: The scalability of RLVR in large language models is hindered by frequent training collapse with gradient spikes. Prior mitigation methods are largely black-box and heuristic: they can alleviate training-inference mismatch, but often fail to deliver long-horizon stability because gradient spikes have multiple causes.
    </li>
    <li style="margin-bottom: 12px;">
      <strong style="color: #1e3a8a;">Localizing the Gradient Spike to a Single Culprit Token</strong>: Moving from black-box heuristics to white-box diagnosis, our distributed binary-search <strong>Gradient Anomaly Localizer (GradLoc)</strong> traces gradient spikes back to the <strong>exact culprit tokens</strong>. It achieves this with $O(\log N)$ complexity and high success rates. <span style="color: #2563eb; font-weight: 500;">(see §GradLoc)</span>
    </li>
    <li style="margin-bottom: 12px;">
      <strong style="color: #1e3a8a;">New Collapse Mode: Layerwise Gradient Heterogeneity</strong>: GradLoc reveals that anomalies stem from <strong>semantically coherent tokens</strong> with pathological <strong>numerical properties</strong> (e.g., extreme importance sampling (IS) ratios), rather than "dirty data". Beyond the known training-inference inconsistency, GradLoc identifies a new anomaly class: Tokens maintain safe IS ratios but exhibit severe <strong>layerwise gradient heterogeneity</strong>, where specific layers explode while others remain stable. <span style="color: #2563eb; font-weight: 500;">(see §Type B (New): Layerwise Gradient Heterogeneity)</span>
    </li>
    <li>
      <strong style="color: #1e3a8a;">Layerwise Gradient Clipping (LayerClip)</strong>: To address this heterogeneity, we propose LayerClip, which enforces constraints based on local layer statistics to avoid suppressing healthy layers in global gradient clipping. This approach significantly extends stable training. <span style="color: #2563eb; font-weight: 500;">(see §Addressing Type B: Layerwise Gradient Clipping)</span>
    </li>
  </ul>
</div>

# RLVR Training Collapse with Gradient Spikes
Scaling RLVR for large language models [^OpenAI o1][^DeepSeek-R1] is hindered by frequent training collapse. This instability is amplified by the infrastructure necessary for long Chain-of-Thought (CoT) rollouts. In advanced LLM training frameworks[^verl][^areal][^slime], acceleration techniques like KV-cache quantization[^KVQuant], custom kernel fusion[^vLLM], and asynchronous data generation[^Kimi k1.5] introduce approximation error, ranging from numerical precision loss to data staleness. Consequently, practical RLVR training evolves into an unstable, chaotic system that makes long-horizon training difficult in practice.

Fundamentally, training collapse stems from anomalous parameter updates driven by accumulated gradient anomalies. Under standard global monitoring, these anomalies appear as spikes in the global gradient norm (**gradient spikes**). Prior work typically attempts to eliminate these spikes via a black-box, "guess-and-check" loop: hypothesize a general cause (e.g., **Training-Inference Inconsistency**[^TIS]) and apply broad mitigations (such as system tweaks[^FP16][^LR_Scheduling] or IS-based constraints[^TIS][^IcePop][^SeqClipNoDetail][^SeqClip]). However, gradient spikes can arise from diverse failure modes, so broad mitigations are inherently fragile without fine-grained attribution. While such methods can temporarily postpone collapse, they fail to ensure long-term stability, suggesting that fragmented heuristics are insufficient to resolve the root causes of optimization failure.

To address training instability, we therefore shift to a **white-box, evidence-driven** workflow by establishing a systematic framework for anomaly attribution, analysis, and resolution. Specifically, we develop a **Gradient Anomaly Localizer (GradLoc)** to trace global spikes directly to the exact culprit tokens. This enables systematic classification of token-level gradient anomalies and targeted solutions (such as **Layerwise Gradient Clipping (LayerClip)**) based on granular evidence, yielding more reliable, monotonic performance improvements in algorithm development.

# GradLoc: Localizing the Gradient Spike to a Single Culprit Token
The prerequisite for resolving instability is granular observability. Standard monitoring tracks the global gradient norm, signaling *when* a collapse occurs but offering no insight into *where* it originates. Lacking token-level attribution, prior research has largely relied on black-box experimentation: postulating potential causes and validating heuristic mitigations empirically. Although techniques like IS clipping have shown success, many heuristic modifications fail to generalize, as identical global symptoms (gradient spikes) can arise from **distinct underlying failure modes**, resulting in a low success rate for algorithmic improvements.

To achieve precise attribution, we introduce **GradLoc**, an infrastructure tool designed to trace gradient spikes to specific culprit tokens. The main challenge for precise localization is computational: a naive linear traversal over global batches ($N \sim 10^7$) is prohibitive. GradLoc overcomes this via distributed binary search, reducing complexity to $O(\log N)$. In practice, it operates as an "always-on" monitor that remains dormant during stable training steps, activating only upon gradient spikes. While localization extends the spiked step time cost by $1\times$ to $3\times$, the amortized overhead is negligible: spikes are either rare anomalies in healthy training, or symptoms of irreversible collapse where training should be terminated regardless.

## Binary Search Localization with Threshold Shifting

![framework.png](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026021014064381_292614cc22b6644d9b103703c382334d.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770703606;2086063606&q-key-time=1770703606;2086063606&q-header-list=&q-url-param-list=&q-signature=75ad4d565710a81fca83486f4a96090a5ed956ed)
*!12 Figure 2: GradLoc localizes the global gradient spike to a single token via distributed binary search on FSDP. The search proceeds from global → micro-batch → rank → token in logarithmic time, while phase-specific thresholds adapt for different gradient aggregation scales.!*

**Anomaly Localization Framework**
GradLoc integrates a four-phase localization workflow into the FSDP backend. Technically, GradLoc leverages the FSDP forward-backward mechanism and loss masking to enable branch computation within the binary search. By adaptive thresholding, GradLoc prevents both missed anomalies and spurious detections. The specific localization logic for each phase is as follows:
*  **Phase 1: Global Trigger:** Check if the global norm $\|\mathbf{G}\|$ exceeds $\tau_{global}$.
*  **Phase 2: Micro-Batch Enumeration:** We iterate through cached micro-batches *before* any rank-level search[^FSDP_footnote]. 
*  **Phase 3: Rank Search:** Binary search over device ranks to pinpoint the specific GPU.
*  **Phase 4: Token Search:** Conduct a binary search within the target rank's micro-batch[^Phase4_footnote] to pinpoint the exact anomalous token and log the anomaly details.

As a diagnostic tool, GradLoc operates in a "read-only" mode triggered solely during steps when a gradient spike is detected, ensuring it neither interferes with the optimization objective nor affects parameter updates. Furthermore, we incorporate an **early stopping** mechanism across all phases: detection terminates immediately if the gradient norm of the current search branch falls below the threshold, minimizing localization overhead. During the binary search splits, GradLoc adopts a greedy strategy, prioritizing the traversal of the branch with the larger gradient norm.

**Adaptive Thresholds**
To minimize the impact on training efficiency, GradLoc must remain "silent" during stable RLVR training and trigger only precisely when gradient anomalies occur. The core challenge lies in the dynamic variation of gradient aggregation scales in distributed training: as the search scope narrows from the global batch to a single token, the number of contributing tokens ($n$) changes drastically, causing the statistical properties of the aggregated gradient to drift. Using a fixed threshold would inevitably lead to missed anomalies or spurious detections. Therefore, we derive adaptive thresholds based on the effective aggregation scale at each phase.

**Threshold Calculation per Phase**
Consider a gradient vector corresponding to a single token $\mathbf{g} \sim \mathcal{N}(0, s^2 I_D)$. For $n$ tokens in RLVR training, the expectation of the norm of the aggregated gradient vector $\bar{\mathbf{g}} = \frac{1}{n}\sum_{i=1}^n g_i$ is $\mathbb{E}[\|n\bar{\mathbf{g}}\|_2] = \sqrt{n} \cdot \mathbb{E}[\|\mathbf{g}\|_2]$. Consequently, the gradient anomaly threshold also scales by $\frac{\sqrt{n}}{n}$. Defining $\tau_{token}$ as the anomaly threshold for a single token's gradient norm, under token-mean loss aggregation, the new threshold is:
$$ 
\tau = \tau_{token} \cdot \sqrt{n} \cdot \frac{1}{n} 
$$

The adaptive thresholds for the four phases are derived as follows[^threshold_footnote] :

**Phase 1: Global Trigger**
The gradient calculation involves the full set of $N$ tokens, resulting in the strongest aggregation effect and the lowest threshold:
$$
\tau_{global} = \tau_{token} \cdot \sqrt{N}\cdot \frac{1}{N} = \tau_{token}\cdot \frac{1}{\sqrt{N}}
$$

**Phase 2: Micro-Batch Enumeration**
The search scope is reduced to a subset of size $N/M$, and the threshold is relaxed accordingly:
$$
\tau_{mb} = \tau_{token} \cdot \sqrt{N/M}\cdot \frac{M}{N} = \tau_{token} \cdot \frac{\sqrt{M}}{\sqrt{N}}
$$

**Phase 3: Rank Search**
When inspecting a rank subset of length $l$, the effective token count is approximately $N\cdot l/(M \cdot W)$. The threshold is adjusted to:
$$
\tau_{rank} = \tau_{token} \cdot \sqrt{\frac{N\cdot l}{M\cdot W}}\cdot \frac{M\cdot W}{N\cdot l} = \tau_{token} \cdot \frac{\sqrt{M} \cdot \sqrt{W}}{\sqrt{N}\cdot\sqrt{l}}
$$

**Phase 4: Token Search**
In this phase, the local average loss is recomputed for $L_{seg}$ tokens within the anomalous rank. The threshold is set as:
$$
\tau_{seg} = \tau_{token} \cdot \sqrt{L_{seg}} \cdot \frac{1}{L_{seg}} = \tau_{token} \cdot \frac{1}{\sqrt{L_{seg}}}
$$

## Computational Overhead
The total number of forward-backward steps required is $O(M + \log N)$.

The table below presents the empirical time cost of anomaly localization during spiked steps (max binary search depth = 60). While localization takes $1\times$ to $3\times$ the duration of a standard step, it is triggered **selectively** only when spikes occur. Consequently, the amortized overhead is negligible over a long training run.

| Exp ID | Step | Avg. Response Length | Step Time (s) | Localization Time (s) | Exp Cumulative Time (s) |
|:------:|:----:|:--------------------:|:-------------:|:------------------:|:-----------------------:|
|    1   |  68  |         7,682        |      513      |        1,408       |          38,485         |
|    2   |  78  |        15,769        |      1493     |        1,741       |          45,999         |
*!12 Table 1: Computational overhead of the GradLoc. !*

## Theoretical Analysis
We provide a theoretical analysis to address concerns that accumulated noise from large batches ($N$) might obscure a single anomaly. We demonstrate that the high dimensionality of LLM parameters ($D$) inherently stabilizes the binary search.

**Theorem 1** (See Appendix for the proof)
Let $\mathcal{G} = \{g_i\}_{i=1}^{N}$ be the set of per-token gradients where $g_i \in \mathbb{R}^D$. Assume $N-1$ tokens produce normal stochastic gradients $g \sim \mathcal{N}(0, s^2 I_D)$, and a unique token $k^*$ produces an anomalous pattern gradient $g_{k^*} \sim \mathcal{N}(0, \sigma^2 s^2 I_D)$ with $\sigma > 1$. The binary search algorithm localizes $k^*$ with probability at least $1 - \epsilon$, where $\epsilon$ can be chosen as any value satisfying $\epsilon \geq 2e^{-\frac{D}{144\log_2 N}}$, provided:

$$
\sigma^2 - 1 \geq 2.5 \cdot \frac{N}{\sqrt{D}} \cdot \sqrt{\log \left(1 + \frac{1}{\epsilon}\right)}
$$

This theorem guarantees localization with probability $1-\epsilon$ when the variance inflation $\sigma$ exceeds the noise ratio $\frac{N}{\sqrt{D}}$. This bound validates binary search as a statistically well-justified strategy for high-dimensional anomaly localization.

**Larger Model, Easier Localization**
The crucial insight from Theorem 1 is that the success probability hinges on the ratio $\frac{N}{\sqrt{D}}$. In modern LLM training, the model dimension $D$ (e.g., $10^{10}$) is significantly larger than the batch token count $N$ (e.g., $10^{7}$). This immense dimensionality effectively suppresses the noise term $\frac{N}{\sqrt{D}}$. For typical values ($D=10^{10}, N=10^{7}$), even a modest anomaly strength of $\sigma=25$ admits a success probability $> 99\%$.

# Analysis: Gradient Anomaly Taxonomy

With feasibility and distinguishability confirmed, we leverage GradLoc to identify the exact tokens responsible for triggering gradient spikes and driving the subsequent collapse.

**GradLoc Monitoring Target: From Global Norm to Token Gradients**
We begin with the standard RLVR objective (using GRPO[^GRPO] as a representative example):
$$ \mathcal{J}_{\text{GRPO}}(\boldsymbol{\theta}) = \mathbb{E}_{(q,a) \sim \mathcal{D}, \{o_i\}_{i=1}^G \sim \pi_{\beta}(\cdot|q)} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} J_{i,t}(\boldsymbol{\theta}) \right] $$ where $J_{i,t}(\boldsymbol{\theta}) = \min \left( r_{i,t} A_{i,t}, \text{clip}(r_{i,t}, 1-\epsilon, 1+\epsilon) A_{i,t} \right)$ represents the token-level contribution.

During training, we monitor the **global gradient norm** $\|\mathbf{G}\|_2$. Theoretically, this global vector is simply the aggregation of individual token gradients $\mathbf{g}_{i,t} = \nabla_{\boldsymbol{\theta}} J_{i,t}(\boldsymbol{\theta})$:
$$
\mathbf{G} = \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \mathbf{g}_{i,t}
$$
When a training collapse occurs (indicated by an extremely large $\|\mathbf{G}\|_2$), **GradLoc** allows us to decompose this global spike and pinpoint to a single token $o_{i,t}$ exhibiting a massive individual gradient norm $\|\mathbf{g}_{i,t}\|_2$.

**GradLoc Output: Token-level Evidence and Failure-mode Taxonomy**
By isolating these specific "culprit" tokens, we can analyze their properties directly. This localization provides an evidence-based, structured analysis of why existing methods fail, motivating a new algorithmic approach[^exp_setting_footnote]. Based on the exact tokens that triggered crashes, we classify failures into two distinct categories: **Type A** (Training-Inference Inconsistency) and **Type B** (Layerwise Gradient Heterogeneity).

![case-study.png#auto#500px#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026021120421436_30022cb7978d2f624ba3acc7a679a0cf.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770813737;2086173737&q-key-time=1770813737;2086173737&q-header-list=&q-url-param-list=&q-signature=5f395680e00c7efc66a01d6927e9fec70e926ea8)
*!12 Figure 3: GradLoc reveals that anomalies stem from semantically coherent tokens with pathological numerical properties (e.g., extreme IS ratios), rather than "dirty data". By constraining the token-level and sequence-level Importance Sampling (IS) ratios, Token-level IS Clipping (TIS) and Sequence-level Clipping (SeqClip) mitigate anomalous gradients from Type A.1 and A.2, respectively. However, gradient spikes persist frequently, caused by Type B tokens that exhibit layerwise gradient heterogeneity despite having safe IS ratios (almost 1.0), as detected by our tool. !*

## Type A: Training-Inference Inconsistency

This category encompasses samples where the token-level or sequence-level probability ratio between the training and inference policies deviates significantly from 1.

**A.1: Token-level Inconsistency**

**GradLoc's Discovery**
Deploying **GradLoc** reveals that gradient spikes under standard GRPO are frequently triggered by tokens exhibiting extreme **token-level Training-Inference Inconsistency**. These anomalies are characterized by a "True" Importance Sampling (IS) Ratio $\omega_{i,t}(\boldsymbol{\theta})$ that deviates wildly from unity, ranging from underflow levels ($<10^{-30}$) to massive explosions ($>10^5$):

$$ \omega_{i,t}(\boldsymbol{\theta}) = \frac{\pi_{\boldsymbol{\theta}}(o_{i,t} \mid q, o_{i,<t})}{\pi_{\beta}(o_{i,t} \mid q, o_{i,<t})} $$

Here, $\pi_{\boldsymbol{\theta}}$ is the policy computed by the training backend (e.g., FSDP in BF16) on current model parameters, while $\pi_{\beta}$ represents the behavior policy collected by the rollout engine (e.g., vLLM with parameter quantization).

**Analysis**
Intuitively, the standard clipping mechanism in GRPO/PPO should filter out tokens with extreme IS ratios. However, token-level evidence from GradLoc shows that these anomalous tokens actively participate in the objective function calculation. This occurs because standard GRPO clipping operates on the proxy ratio $r_{i,t}(\boldsymbol{\theta}) = \frac{\pi_{\boldsymbol{\theta}}(o_{i,t} \mid q, o_{i,<t})}{\pi_{\text{old}}(o_{i,t} \mid q, o_{i,<t})}$ rather than $ \omega_{i,t}(\boldsymbol{\theta}) = \frac{\pi_{\boldsymbol{\theta}}(o_{i,t} \mid q, o_{i,<t})}{\pi_{\beta}(o_{i,t} \mid q, o_{i,<t})} $:

$$
\mathcal{J}_{\text{GRPO}}(\boldsymbol{\theta}) = \mathbb{E}_{(q,a) \sim \mathcal{D}, \{o_i\}_{i=1}^G \sim \pi_{\beta}(\cdot|q)} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \min \left( r_{i,t} A_{i,t}, \text{clip}(r_{i,t}, 1-\epsilon, 1+\epsilon) A_{i,t} \right) \right]
$$
This allows tokens with anomalous $\omega$ values to escape the clipping. The discrepancy between $\omega$ and $r$ lies in the denominators $\pi_{\beta}$ and $\pi_{\text{old}}$. Theoretically, these should be identical. However, in modern training frameworks, significant deviations arise due to numerical precision differences (e.g., FP8 vs. BF16), non-deterministic forward computations, and other approximations.

For tokens where $\pi_{\beta}$ diverges significantly from $\pi_{\text{old}}$, the standard GRPO objective calculation becomes severely biased: the data is sampled from $\pi_{\beta}$, but the denominator of the IS ratio $r_{i,t}(\boldsymbol{\theta})$ uses $\pi_{\text{old}}$. Our experiments indicate that this biased objective function is a primary driver of training collapse and requires explicit rectification.

**Solution: TokenClip**
To resolve this, we can unify successful methods like TIS[^TIS] and ICEPOP[^IcePop] under a single generalized formulation that performs robust rectification $\Psi$:

$$
\mathcal{J}_{TokenClip}(\boldsymbol{\theta}) = \mathbb{E}_{\,(q,a)\sim \mathcal{D},\,\{o_i\}_{i=1}^G \sim \pi_{\beta}(\cdot \mid q)} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \Psi(r_{i,t}(\boldsymbol{\theta})) \cdot A_{i,t} \right]
$$

$$
\Psi(r_{i,t}) =
\begin{cases}
\min(\frac{\pi_{\text{old}}(o_{i,t})}{\pi_{\beta}(o_{i,t})}, C) \cdot \text{clip}(r_{i,t}, 1 - \epsilon, 1+\epsilon) & \text{(TIS: One-sided Shrinking)} \\
\omega_{i,t} \cdot \mathbb{I}(C_{low} \le \omega_{i,t} \le C_{high}) & \text{(ICEPOP: Double-sided Masking)}
\end{cases}
$$

Here, $C$ denotes the hyperparameter for clipping or masking thresholds. Since the IS ratio $r$ is effectively corrected to $\omega$, the original clipping logic based on $r$ is no longer applicable. Specifically, TIS applies an upper-bound shrinking to limit the impact of large ratios while retaining small ones, whereas ICEPOP employs a hard binary mask $\mathbb{I}(\cdot)$ to discard any token falling outside the trust region.

![performance_first3.png](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026020323200573_cb2ae9a782ecfaccf09da91aefa7f26a.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770132007;2085492007&q-key-time=1770132007;2085492007&q-header-list=&q-url-param-list=&q-signature=2d5b34593bab88bc6462bba2e406aaf3e3323145)
*!12 Figure 4: TokenClip (TIS, ICEPOP) postpones training collapse. !*

**Discussions on Asymmetric Clipping**
Our empirical observation highlights an asymmetry in risk. Tokens with huge $\omega_{i, t}$ are destructive and must be clipped or masked. Conversely, tokens with tiny $\omega_{i, t}$ ($< 10^{-30}$) are generally "safe" because the IS weight naturally suppresses the gradient update ($\|\omega_{i,t} \nabla \log \pi_{\boldsymbol{\theta}}\| \to 0$)[^omega_footnote]. This explains why both TIS (which shrinks them) and ICEPOP (which masks them) yield similar stability.

Crucially, lower-bound clamping remains a risk for collapse. These strategies enforce a minimum floor (e.g., $\max(\omega_{i,t}, 0.5)$) with preserved gradient. This is dangerous for tiny $\omega_{i,t}$ tokens: it artificially inflates a vanishing weight ($10^{-30} \to 0.5$) by orders of magnitude. This effectively multiplies a potentially noisy gradient term by a massive scalar, dominating the optimization.

**A.2 Sequence-level Inconsistency**

**GradLoc's Discovery**
Token-level constraints are necessary but insufficient. GradLoc revealed a second class of gradient anomalies: extremely large gradient norms arise from tokens whose token-level ratios are healthy ($\omega_{i,t} \approx 1$), yet their **sequence-level** divergence accumulates far from 1. We quantify this using the geometric mean of the sequence-level IS ratios:
$$
\rho_i(\boldsymbol{\theta}) = \left( \prod_{t=1}^{|o_i|} \frac{\pi_{\boldsymbol{\theta}}(o_{i,t} \mid q, o_{i,<t})}{\pi_{\beta}(o_{i,t} \mid q, o_{i,<t})} \right)^{\frac{1}{|o_i|}}
$$

**Analysis**
Ideally, $\rho_i(\boldsymbol{\theta})$ should remain close to 1. However, due to the multiplicative nature of joint probabilities, even minor token-level shifts can accumulate into massive sequence-level divergence. When $\rho_i(\boldsymbol{\theta})$ deviates significantly from 1, the RLVR objective function for sequence $i$ exhibits extreme bias[^1st_approx]. Consequently, the global objective function becomes dominated by these extremely biased components from sequence $i$, driving the RLVR training toward collapse.

**Solution: SeqClip**
A straightforward mitigation is to apply Sequence-level Clipping (SeqClip[^SeqClipNoDetail][^SeqClip]) to prune high-risk sequences from the training batch, excluding them from the objective function calculation. To systematically address A.1 and A.2, we propose a composite objective that unifies sequence-level masking ($M_i$) with token-level rectification ($\Psi$):

$$
\mathcal{J}_{\text{Composite}}(\boldsymbol{\theta}) = \mathbb{E}_{\substack{(q,a)\sim \mathcal{D} \\ \{o_i\}_{i=1}^G \sim \pi_{\beta}}} \left[ \frac{1}{G} \sum_{i=1}^G M_i(\rho_i(\boldsymbol{\theta})) \cdot \left( \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \Psi(r_{i,t}(\boldsymbol{\theta})) \cdot A_{i,t} \right) \right]
$$

Here, $M_i(\cdot)$ is the binary sequence mask defined as:

$$
M_i(\rho_i) = \mathbb{I}\left(C_{\text{low}}^{(s)} < \rho_i < C_{\text{high}}^{(s)} \right)
$$

where $C_{\text{low}}^{(s)}$ and $C_{\text{high}}^{(s)}$ are the sequence-level trust region bounds (e.g., $[0.995, 1.005]$).

However, while SeqClip improves stability by discarding sequences with accumulated drift, it significantly reduces sample efficiency and, crucially, fails to eliminate gradient spikes arising from *consistent* samples, which leads us to Category B.

![performance_first4.png](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026020323224636_4118d33f84c5a39b2edc5aea8a54d4f4.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770132167;2085492167&q-key-time=1770132167;2085492167&q-header-list=&q-url-param-list=&q-signature=b0b3f2ebb8ca8d8ad53e73ad185b253259969e99)
*!12 Figure 5: SeqClip postpones training collapse. !*

## Type B (New): Layerwise Gradient Heterogeneity

![Clipboard_Screenshot_1770097891.png#auto#500px#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026020313513540_50b7b578a470834b738ee5578e0a2b4d.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770097898;2085457898&q-key-time=1770097898;2085457898&q-header-list=&q-url-param-list=&q-signature=b472aa1cbf6a9e025955abccc0cfe545000d3100)
*!12 Figure 6: Layerwise Gradient Heterogeneity: Illustration of gradient norm dynamics across different layers of Qwen3-4B-Instruct. Shallower layers frequently exhibit gradient spikes, whereas deeper layers remain stable throughout the entire training process. !*

![Clipboard_Screenshot_1770174787.png#auto#350px#center](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026020411130940_6a8ce2a54933e50e69f4bac99eab3d1a.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770174790;2085534790&q-key-time=1770174790;2085534790&q-header-list=&q-url-param-list=&q-signature=ccf69b81ddfe6f65d5bb8a5f890635287fe03d25)
*!12 Figure 7: Intra-layer Gradient Homogeneity: Illustration of gradient norm dynamics across various sub-modules (Attn, MLP, Norms) within the first layer. In contrast to the disparity across layers, modules within the same layer exhibit highly synchronized spiking patterns. !*

**GradLoc's Discovery**
The most critical discovery from GradLoc is **Type B** anomalies. These are sequences that pass all standard safety checks (token IS $\omega_{i,t} \approx 1$, sequence IS $\rho_{i} \approx 1$), yet they drive the model into collapse.

Detailed inspection uncovers a critical structural dichotomy in these anomalies. First, we observe severe **Layerwise Gradient Heterogeneity**: the gradient explosion is not systemic but strictly localized: where specific layers (typically early in the network) explode with massive norms while subsequent layers remain stable. Conversely, at a finer granularity, we find **Intra-layer Gradient Homogeneity**: sub-modules within the same layer (Attention, MLP, Norms) exhibit highly synchronized spiking patterns. This implies that the instability is a phenomenon driven by collective layer dynamics rather than a single module failure.

**Analysis**
We hypothesize that this arises from a compounding effect: minor distribution shifts in early-layer activations (due to data staleness in asynchronous rollouts) could be amplified through the network, or certain attention heads may become transiently unstable on long, out-of-distribution sequences. 

Under layerwise heterogeneity, global gradient clipping becomes misaligned with the failure mode: it suppresses healthy layers to compensate for a few exploding ones. The standard clipping mechanism rescales all gradients uniformly using a single scalar coefficient $\nu$ based on the global gradient clipping threshold $\tau$ (e.g., commonly used $\tau=1$):

$$
\mathbf{G} \leftarrow \mathbf{G} \cdot \nu, \quad \text{where } \nu = \min\left(1, \frac{\tau}{\|\mathbf{G}\|_2}\right)
$$

When a Type B anomaly occurs:
1.  The global norm $\|\mathbf{G}\|_2$ is dominated by the few exploding layers.
2.  The scaling factor $\nu$ becomes infinitesimally small ($\nu \ll 1$) to compensate for the explosion.
3.  This tiny $\nu$ is broadcast to all layers. The gradients of well-behaved layers are aggressively suppressed to near zero.

Consequently, the majority of the model optimization momentum is effectively **frozen**, updates remain nearly unchanged in either direction or magnitude. Meanwhile, the optimization trajectory is disproportionately dictated by the erratic direction of the exploding layers. The model appears to be "stable" (the global norm is low), but it has ceased learning effectively and is being slowly steered into collapse by the outliers. This necessitates a move from global constraints to layerwise adaptive strategies.

## Addressing Type B: Layerwise Gradient Clipping

In this section, we aim to address the **Type B anomaly (Layerwise Gradient Heterogeneity)**, which persists even when training-inference consistency is enforced. Inspired by observed "layerwise gradient heterogeneity", we propose **layerwise gradient clipping (LayerClip)**. Instead of a fixed global threshold, we enforce a self-adaptive, layerwise constraint on the optimization trajectory of each layer (or FSDP handle).

For each layer $l$ at step $t$, we maintain a representative statistic $R_l^{(t)}$ of its gradient norm history. We employ an exponential moving average (EMA) or running average (CA) to track the layerwise expected scale[^LayerClip_footnote] :

$$
R_l^{(t)} =
\begin{cases}
\beta R_l^{(t-1)} + (1-\beta) \|\nabla_{\theta_l}^{(t)}\|_2, & \text{(EMA)} \\
(1 - \frac{1}{t}) R_l^{(t-1)} + \frac{1}{t} \|\nabla_{\theta_l}^{(t)}\|_2, & \text{(CA)}
\end{cases}
$$

Unlike global static clipping threshold in traditional gradient clipping, our clipping threshold is layerwise adaptive, for layer $l$ is defined dynamically as $\tau_l = \alpha \cdot R_l^{(t)}$, where $\alpha > 1$ is a hyperparameter. The gradient clipping rule becomes:

$$
\tilde{\nabla}_{\theta_l}^{(t)} = \nabla_{\theta_l}^{(t)} \cdot \min\left(1, \frac{\tau_l}{\|\nabla_{\theta_l}^{(t)}\|_2 + \epsilon}\right)
$$

Our approach combines two key advantages:

1. **Isolation:** An anomaly in Layer $l_A$ triggers clipping only for Layer $l_A$, allowing Layer $l_B$ to update normally. This prevents gradient anomaly layers from dominating the global gradient.
2. **Adaptivity:** It respects the numerical scale differences between layers, avoiding the bias introduced by a single global threshold.

Empirically, applying **LayerClip** on the Qwen3-4B-Instruct[^Qwen3] model eliminated the training instability caused by Type B anomalies. By effectively managing the gradient heterogeneity, we observed a more stable training compared to baselines.

![performance.png](https://hy-model-ap-prod-1258344703.cos.ap-guangzhou.myqcloud.com/llm-blog/default/abbac702/2026020317503771_a4cac944136234128037b420042512e2.png?q-sign-algorithm=sha1&q-ak=AKIDRl074nOsGdJ9zjMsCRWP3ShmgS3VtX4S&q-sign-time=1770112238;2085472238&q-key-time=1770112238;2085472238&q-header-list=&q-url-param-list=&q-signature=58edc938750dd57f76f5b804106e459c8dc77f03)
*!12 Figure 8: Training dynamics of different clipping methods. By sequentially addressing three classes of failure cases, TokenClip (TIS, ICEPOP), SeqClip, and LayerClip progressively stabilize training. As each method mitigates a specific anomaly type, training stability improves significantly, leading to consistent gains in performance. !*

# Conclusion

In this work, we tackle the persistent challenge of training instability in scaling RLVR by shifting the mitigation paradigm from heuristic data filtering to infrastructure-level diagnosis. Through a principled anomaly localization tool, **GradLoc**, we achieved precise localization of gradient spikes, thereby revealing a critical limitation in existing methods. We demonstrated that while IS constraints effectively address training-inference inconsistency, they fail to mitigate a newly identified class of "consistent" anomalies manifest as severe **Layerwise Gradient Heterogeneity**. To resolve this, we introduced Layerwise Gradient Clipping (**LayerClip**), which clips gradient based on local layer statistics rather than a global norm. Empirical validation confirms that effectively managing this heterogeneity significantly extends training stability. Our study establishes a systematic framework for understanding and analyzing RLVR training, and accelerates large-model training strategies in both academic and industrial scenarios.

# Future Work

RLVR faces a significant disconnect between engineering and theory. Due to the high complexity of engineering implementation, researchers often struggle to systematically observe training dynamics. Consequently, many promising theoretical explorations are hindered by cumbersome engineering debugging. This has historically shifted the community's focus on optimization theory and optimizer research heavily toward pre-training. To bridge this gap, we plan to open-source and iterate on **GradLoc**, transforming gradient anomaly localization into a routine diagnostic as accessible as monitoring loss curves. By lowering the barrier to fine-grained observation, we aim to empower the community to look inside the engineering "black box" and advance the theoretical foundations of RLVR optimization.

Furthermore, while **LayerClip** effectively mitigates instability by containing layerwise heterogeneity, it does not eliminate the root cause. This heterogeneity likely signals deeper, under-explored physical and statistical mechanisms in large model training. Moving forward, it is important to investigate these fundamental principles to transcend heuristic clipping and design optimization algorithms that are mathematically robust from first principles.

> **Contributors**: Guanhua Huang$^*$, Tingqiang Xu$^*$, Jinbo Wang$^*$, Guangming Sheng, Siheng Li, Evander Yang, Kejiao Li, Yunxiang Li, Zenan Xu, Qi Yi, Kyrierl Deng, Ziyuan Nan, Yuhao Jiang, Chenchen Zhang, Taiqiang Wu, Feiyuan Zhang, Junhao Wang, Bo Zhou$^{\dagger}$, Alex Chen$^{\dagger}$, Di Wang, Shunyu Yao.
>  ($*$: equal contribution; ${\dagger}$: corresponding author.)

# Citation
```
@misc{huang-xu-wang-2026-gradloc,
  title = {Stabilizing {RLVR} via Token-level Gradient Diagnosis and Layerwise Clipping},
  author = {Huang, Guanhua and Xu, Tingqiang and Wang, Jinbo and Sheng, Guangming and Li, Siheng and Yang, Evander and Li, Kejiao and Li, Yunxiang and Xu, Zenan and Yi, Qi and Deng, Kyrierl and Nan, Ziyuan and Jiang, Yuhao and Zhang, Chenchen and Wu, Taiqiang and Zhang, Feiyuan and Wang, Junhao and Zhou, Bo and Chen, Alex and Wang, Di and Yao, Shunyu},
  year = {2026},
  url = {https://hy.tencent.com/research/100015}
}
```


# Acknowledgments
We thank our Pre-train Team colleagues for their valuable discussions on gradient instability and for providing feedback on the deployment of GradLoc in pre-training scenarios. We also appreciate the fruitful discussions with our colleagues from the Post-train Team and thank the Infrastructure and Platform Teams for their technical support. Finally, we thank Weinan E, Zhouwang Yang, Lei Wu, and Mingze Wang for their in-depth exchanges regarding the optimization dynamics of Large Language Models.

# Appendix
## Proof for Theorem 1

**Proof.**  
The proof relies on the concentration properties of Chi-squared random variables and a union bound over the steps of the algorithm. Without loss of generality, one can set $s=1$.

**1. Preliminaries and Notation.**  
The algorithm proceeds in $L = \log_2 N$ steps. At step $j \in \{1, \dots, L\}$, let $\mathcal{S}_\text{anom}$ denote the subset containing the anomalous vector $g_{k^*}$, and $\mathcal{S}_\text{noise}$ denote the opposing subset containing only standard Gaussian noise vectors. Let $m_j = N / 2^j$ be the number of vectors in each subset at step $j$.

Define the sum vectors for the two subsets as:

$$
X = \sum_{v \in \mathcal{S}_\text{noise}} v, \quad Y = \sum_{v \in \mathcal{S}_\text{anom}} v.
$$

Based on the additivity of independent Gaussians, the distributions are:

$$
X \sim \mathcal{N}(0, m_j I_D), \quad Y \sim \mathcal{N}(0, (m_j - 1 + \sigma^2) I_D).
$$

Consequently, their squared norms scale with Chi-squared distributions:

$$
\|X\|^2 \sim m_j \chi^2_D, \quad \|Y\|^2 \sim (m_j + \Delta) \chi^2_D,
$$

where $\Delta = \sigma^2 - 1$ is the excess variance contribution from the anomaly.

**2. Concentration Bounds.**  
We utilize the Laurent-Massart bounds for a Chi-squared variable $Z \sim \chi^2_D$. For any $t > 0$:

$$
\begin{align*}
\mathbb{P}(Z - D \geq 2\sqrt{Dt} + 2t) \leq e^{-t}, \\
\mathbb{P}(Z - D \leq -2\sqrt{Dt}) \leq e^{-t}.
\end{align*}
$$

Let $\delta_j$ be the failure probability allowed at step $j$. We set $t = \log(1/\delta_j)$.

The algorithm makes an error at step $j$ if $\|X\|^2 \geq \|Y\|^2$. We seek to bound the probability of this event. Using the concentration inequalities, with probability at least $1 - 2\delta_j$, the norms are bounded by:

$$
\begin{align*}
\|X\|^2 \leq m_j (D + 2\sqrt{D t} + 2t) := B_{noise}^{upper}, \\
\|Y\|^2 \geq (m_j + \Delta) (D - 2\sqrt{D t}) := B_{anom}^{lower}.
\end{align*}
$$

A sufficient condition for success ($\|Y\| > \|X\|$) is $B_{anom}^{lower} > B_{noise}^{upper}$. Substituting the terms:

$$
(m_j + \Delta)(D - 2\sqrt{Dt}) > m_j (D + 2\sqrt{Dt} + 2t).
$$

Substituting $\Delta = \sigma^2 - 1$, a sufficient condition can be:

$$
\sigma^2 - 1 \geq 5 \frac{m_j}{\sqrt{D}} \sqrt{t} \text{ and } t \le \frac{D}{144}.
$$

**3. Union Bound.**  
The algorithm succeeds only if it makes the correct decision at all $L = \log_2 N$ steps. Let $E_j$ be the event of failure at step $j$. We assign an equal failure budget to each step, setting $\delta_j = (\frac{\epsilon}{1+\epsilon})^j := \mu(\epsilon)^j$.

By the union bound, the total probability of failure is:

$$
\mathbb{P}(\text{Failure}) \leq \sum_{j=1}^{L} \mathbb{P}(E_j) \leq \sum_{j=1}^{L} \mu(\epsilon)^j \leq \frac{\mu(\epsilon)}{1 - \mu(\epsilon)} = \epsilon.
$$

Substituting $t = \log(1/\mu(\epsilon)^j)$ into our condition derived in Step 2, we obtain the requirement:

$$
\begin{align*}
& t \le \frac{D}{144} \\
\Leftrightarrow
& -j\log \mu(\epsilon) \leq \frac{D}{144} \text{ for } 1 \leq j \leq \log_2 N \\
\Leftarrow
& -\log_2 N \log\frac{\epsilon}{2} \le \frac{D}{144} \text{ by } \frac{\epsilon}{1+\epsilon} \geq \frac{\epsilon}{2} \\
\Leftrightarrow
& \epsilon \geq 2e^{-\frac{D}{144\log_2 N}}.
\end{align*}
$$

and

$$
\begin{align*}
& \sigma^2 - 1 \geq 5 \frac{m_j}{\sqrt{D}} \sqrt{-j\log \frac{\epsilon}{1+\epsilon}} \text{ for } 1 \leq j \leq \log_2 N \\
\Leftrightarrow &
\sigma^2 - 1 \geq 5 \frac{N}{\sqrt{D}} \sqrt{\log (1 + \frac{1}{\epsilon})}\frac{\sqrt{j}}{2^j} \text{ for } 1 \leq j \leq \log_2 N\\
\Leftrightarrow &
\sigma^2 - 1 \geq 2.5 \frac{N}{\sqrt{D}} \sqrt{\log (1 + \frac{1}{\epsilon})}.
\end{align*}
$$

The second $\Leftrightarrow$ is by $\frac{\sqrt{j}}{2^j} \leq \frac{1}{2}$, it suffices to meet that requirement as stated in Theorem 1. Under this condition, the correct subset is selected at every step, leading to the unique anomaly $g_{k^*}$ with probability at least $1-\epsilon$.

[^OpenAI o1]: [OpenAI o1 System Card](https://arxiv.org/abs/2412.16720)

[^DeepSeek-R1]: [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://www.nature.com/articles/s41586-025-09422-z)

[^verl]:[HybridFlow: A Flexible and Efficient RLHF Framework](https://arxiv.org/abs/2409.19256)

[^areal]:[AReaL: A Large-Scale Asynchronous Reinforcement Learning System for Language Reasoning](https://arxiv.org/abs/2505.24298)

[^slime]:[slime: An LLM post-training framework for RL Scaling](https://github.com/THUDM/slime)

[^KVQuant]: [KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization](https://arxiv.org/abs/2401.18079)

[^vLLM]: [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://dl.acm.org/doi/10.1145/3600006.3613165)

[^Kimi k1.5]: [Kimi k1.5: Scaling Reinforcement Learning with LLMs](https://arxiv.org/abs/2501.12599)

[^LR_Scheduling]: [Beyond Precision: Why Training-Inference Mismatch is an Optimization Problem and How Simple LR Schedules Fix It](https://richardli.xyz/mismatch-lr-schedule)

[^TIS]: [Your Efficient RL Framework Secretly Brings You Off-Policy RL Training](https://fengyao.notion.site/off-policy-rl)

[^CISPO]: [MiniMax-M1: Scaling Test-Time Compute Efficiently with Lightning Attention](https://arxiv.org/abs/2506.13585)

[^GPPO]: [CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization in Reinforcement Learning](https://arxiv.org/abs/2509.20712)

[^IcePop]: [Small Leak Can Sink a Great Ship—Boost RL Training on MoE with IcePop!](https://ringtech.notion.site/icepop)

[^SeqClipNoDetail]: [When Speed Kills Stability: Demystifying RL Collapse from the Training-Inference Mismatch](https://yingru.notion.site/When-Speed-Kills-Stability-Demystifying-RL-Collapse-from-the-Training-Inference-Mismatch-271211a558b7808d8b12d403fd15edda)

[^SeqClip]: [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556)

[^FSDP]: [PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel](https://arxiv.org/abs/2304.11277)

[^GRPO]: [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)

[^Qwen3]: [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)

[^FP16]:[Defeating the Training-Inference Mismatch via FP16](https://arxiv.org/html/2510.26788v1)

[^1st_approx]: [Stabilizing Reinforcement Learning with LLMs: Formulation and Practices](https://arxiv.org/abs/2512.01374)

[^exp_setting_footnote]: Experiment Settings: Model: Qwen3-4B-Instruct; learning rate $\eta=2 \times 10^{-6}$; train prompt batch size = 128; rollout number = 8; maximum response length = 32,768; partial rollout chunk size = 4,096; TIS clipping range is [0, 5]; ICEPOP clipping range is [0.5, 5.0]; SeqClip clipping range is [0.995, 1.005].

[^FSDP_footnote]: In FSDP, gradients accumulate across micro-batches. If we performed rank search first, evaluating each rank subset would require re-accumulating gradients over all $M$ micro-batches ($M$ forward-backward passes). By isolating the target micro-batch first, the subsequent rank search only requires re-computation for a single micro-batch, reducing complexity from $O(M \cdot \log W)$ to $O(M + \log W)$.

[^Phase4_footnote]: In practice, this operates as a Depth-First Search (DFS) on a binary segmentation tree rather than a standard single-path search. Identifying the primary "culprit" is sufficient to deduce systemic issues without exhaustive enumeration. With a budget slightly above the theoretical lower bound ($\approx \log N$), GradLoc leverages DFS to backtrack and pinpoint co-occurring anomalous tokens with negligible cost, balancing detection speed with diagnostic completeness.

[^threshold_footnote]: For clarity, a simplified derivation is presented here; the actual FSDP implementation accounts for additional coefficients introduced by sharding strategies, as detailed in our code.

[^LayerClip_footnote]: Our key insight suggests other potential solutions. Specifically, the gradient of each layer can be explicitly regularized by coupling it to smoothed cross-layer statistics, such as CA or EMA, providing a possible alternative to address layerwise gradient heterogeneity.

[^omega_footnote]: Note that tokens with small $\omega_{i,t}(\theta)$ are safe only after the loss function is corrected to use $\omega_{i,t}(\theta)$. Before this correction (in standard GRPO), they are not safe because the coefficient of $\|\nabla \log \pi_{\boldsymbol{\theta}}\|$ is $r_{i,t}(\theta) \approx 1$ (since values deviating from 1 are clipped and do not participate in the loss), which fails to suppress the gradient norm.
