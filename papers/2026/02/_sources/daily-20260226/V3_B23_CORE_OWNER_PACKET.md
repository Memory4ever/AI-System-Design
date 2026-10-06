# B23 — 六项必要原证 / actual owner；本次独立复核已落实

2026-10-06 feb26_close_oct06 非原packet作者实际从各raw定位全部所引pID，无缺失；20652原§3.3 theorem交集/valid split、20758原§3.1–3.2 finite链/adversarial目标、21160原二阶机制及high-order反側另读。actualCh66 calibration/bias、Ch27任务效用与Ch23 codec/训练分布、Ch24已移161–163 posterior/MC/solver分别核。20294/20652/20758具体已有覆盖，20650/21160有限压色/近似读出仅报告；不授人格truth/校准复用theorem/exactposterior/medical结论。20731真实差额已写并root actualPOST，本批不重新排写；旧PRE仅保历史提案，当前终态以README与自身末注POST为准。原费用/ND/人口/反侧保留，未运行artifact/复现，非日级验收。

## 2602.20294v1
https://arxiv.org/html/2602.20294v1

S3.SS1.p3.1 | These results reveal a clear trade-off: memory-based retrieval excels at capturing communication style and personality traits, while chronological-based methods better preserve factual consistency and knowledge retention. Memory-based retrieval with 100 semantically selected examples outperforms chronological-based with 1,000 sequential examples on content similarity and personality similarity, but achieves a higher contradiction ratio of 6.27% compared to 5.72%. Note that MCQ evaluation is not applicable for memory-based methods because retrieved examples change dynamically per test question, making the fixed-context MCQ format incompatible.

S3.SS2.p2.1 | Content similarity improves monotonically with retrieval size, from 3.46 to 3.52, and personality similarity peaks at 78.4% with 100 examples. Contradiction ratios remain stable across relevance-based variants at 6.23% to 6.47%, indicating that increasing retrieval volume does not degrade factual consistency. The random selection baseline provides critical validation: selecting 100 examples without regard to semantic similarity yields substantially lower content similarity of 3.38 and personality similarity of 76.0% compared to relevance-based retrieval, with a higher contradiction ratio of 6.90%. This confirms that embedding-based retrieval is essential to the method’s effectiveness, as simply providing more context without relevance-based selection yields limited benefit.

S7.SS0.SSS0.Px2.p1.1 | All evaluation metrics rely on LLM judges, which may exhibit systematic biases. Personality similarity is assessed through Big Five traits, a well-established but reductive model that may miss important individual characteristics. The held-out test set is drawn from the same time period as training data, so we cannot assess how methods handle personality evolution over time. Moreover, personalities are often asked similar questions across different interviews, which may introduce topical overlap between training examples and test questions. This overlap could inflate performance for methods that include training examples in context, though it affects all interview-grounded methods equally. Human evaluation, while infeasible at our scale, would complement these automated metrics.

## 2602.20650v1
https://arxiv.org/html/2602.20650v1

S3.SS2.p1.1 | The pipeline of the Dataset Color Quantization (DCQ) framework is shown in Figure 3. DCQ first groups images with chromatically similar distributions into clusters and constructs a shared cluster-level palette. Next, within each cluster, we perform K-means on the color palettes of individual images to generate a shared color palette for all images in the same cluster. The generated palettes and their corresponding indices are stored for later use. During training, we retrieve the stored indices and palettes to reconstruct quantized images, which are then used to train a neural network. In the following, we will give a detailed introduction of the proposed method.

S3.SS2.SSS2.p2.1 | To identify high-impact palettes, we employ Grad-CAM++ (Chattopadhay et al., 2018) to obtain an attention map generated from task-specific pre-trained models. The Grad-CAM++ heatmap reveals discriminative regions that contribute to the network’s classification decision. The higher attention values indicate greater relevance to the network’s prediction. For each image, we retain the top k_{Gra}\% of pixels with the highest attention values, ensuring that only the most relevant regions are preserved, while all remaining pixels are set to zero. The value of k_{Gra}\% was determined through ablation studies in Appendix 12.

S4.SS2.p1.1 | How Many Clusters? Table 2(b) presents the impact of varying the number of clusters in the initial K-Means clustering step. Using the least number of clusters, which is 1 cluster, extracts all color palettes to get a shared quantized color palette for every image in the dataset. On the other hand, the most number of clusters (i.e., 50,000 clusters for CIFAR-10) means that we assign each image a unique quantized color palette, which can be seen as Image-Property-based CQ. The best performance is achieved with 20 clusters.

## 2602.20652v1
https://arxiv.org/html/2602.20652v1

S3.SS3.p3.1 | The combination is motivated by the complementary geometric properties of the two scores. Intuitively, by intersecting the irregular, discrete boundaries of the k -NN rank score with the smoother, continuous boundaries of the CLR density score, DANCE retains the semantic groupings captured by the latter while applying the former as a cardinality constraint to prune extraneous classes. Thus, controlling q_{knn} is critical as it explicitly caps the maximum size of the DANCE prediction set. Assume the total error rate is set as \alpha=\alpha_{knn}+\alpha_{clr} . We introduce hyperparameter \lambda to control the division such that \alpha_{clr}=\lambda\cdot\alpha and \alpha_{knn}=(1-\lambda)\cdot\alpha . This leads to the following proposition for coverage guarantee.

S4.SS1.SSS1.p3.1 | Our methodology coverage guarantees apply to fully disjoint reference/calibration splits. However, to improve data efficiency in finite-sample experiments, we also evaluate a calibration-reuse setting where \mathcal{D}_{\text{cal}} is reused as reference set \mathcal{D}_{\text{ref}} . Specifically, when computing calibration nonconformity scores, for each Z_{i}\in\mathcal{D}_{\rm cal} , neighbors are found based via a leave-one-out search where \mathcal{D}_{\text{ref}}=\mathcal{D}_{\text{cal}}\backslash\{Z_{i}\} to avoid self-matching. Similar reuse strategies have previously been used in neighbor-based methods (Papernot and McDaniel, 2018; Ghosh et al., 2023). Thus, we report empirical results under this reuse setting. Additionally, we empirically corroborate this choice against a theoretically-valid disjoint split in Appendix D, demonstrating closely matching coverage and UQ performance. For fairness, all local CP methods compared reuse the \mathcal{D}_{\text{cal}} as \mathcal{D}_{\text{ref}} .

S4.SS2.p1.1 | Table 1 shows results using embeddings from the CLIP ViT-B/16 backbone. At the relaxed error rate of \alpha=0.1 , RFM Adapter (RAPS) achieves the lowest average set size (2.21), with the APS variant following closely (2.23). CLR Set shows its robustness properties, with the lowest CCV (8.128), albeit with high set size (5.82), predicting over twice as many classes on average compared to more efficient baselines. DANCE achieves third best CCV (8.442), with comparable set size efficiency (2.49) to the top competitors.

## 2602.20731v1
https://arxiv.org/html/2602.20731v1

S3.SS1.p1.1 | As noted in the introduction, as the amount of information embedded in the latent message increases (in our case, the number of crops), it is natural to expect the model to discard irrelevant secondary details and retain only the most essential features for reconstruction. This process would naturally induce a hierarchical structure in the feature space. However, if during training the number of crops the model aggregates were fixed, the network would instead learn to pre-allocate parts of the latent message for future crops. This would effectively enforce a fixed capacity per crop, with each information chunk occupying a predetermined location in the message. To avoid this behavior, we randomize the number of crops the model processes during training. As a result, the model never knows whether additional crops will follow the current one and is therefore encouraged to use the available tokens greedily. This corresponds to the setting with fixed capacity and varying amount of information, which is precisely the regime we were aiming for.

S3.SS1.p2.1 | In addition, backpropagating gradients through the entire sequence of message updates would be computationally expensive and memory-intensive. To address this, we apply a stop-gradient operation to all updates except the final one. Combined with the randomized number of crop aggregations, this further promotes greedy token usage while enabling efficient training. In preliminary small-scale experiments, we found that restricting gradient backpropagation in this way has only a moderate impact on performance.

S4.SS1.p5.1 | Cropping policy. Table 3 compares different cropping policies. A single global crop yields competitive average performance across tasks while incurring the lowest test-time cost (the number of crops). Based on this observation, we adopt global-only cropping as the default for the remainder of our probing experiments unless stated otherwise. Importantly, COMiT also naturally supports test-time scaling: adding local crops provides modest gains on compositional generalization and inter-object relations, suggesting that local processing can benefit certain benchmarks. Notably, all differences across cropping policies arise purely at test-time, without retraining the model.

S4.SS2.p2.1 | Similarly to prior work (Bachmann et al., 2025), we observe that scaling the model from B to L improves both reconstruction and representation, and further scaling the model from L to XL allocates the additional capacity to aid reconstruction, while diminishing the semantics.

## 2602.20758v1
https://arxiv.org/html/2602.20758v1

S3.SS2.p3.6 | which promotes D_{\phi} to be 1-Lipschitz on the space of feasible image pairs. In practice, both \mathcal{L}_{\text{adv}} and \mathcal{L}_{\text{disc}} are approximated using minibatches of data, with randomly sampled layers \ell\sim{\mathbf{l}} among which we choose to discriminate samples. The weights \theta are then learned using stochastic optimisation techniques. In [57], it was shown that joint optimization of the objectives \mathcal{L}_{\text{adv}} and \mathcal{L}_{\text{disc}} using mini-batching leads to a heavily biased approximation of the Wasserstein distance. A Lipschitz-continuous discriminator was shown empirically to create an accurate solution landscape for the min-max game (19).

S4.SS1.SSS1.p1.1 | We consider a linear inverse problem of the form (2), with Ax=k*x representing convolution with a motion-blur kernel k . As remarked above, unfolded MCMC architectures are able to naturally embed model parameters. This allows the training of deep unfolded generative networks robust to small perturbations in the observation model, represented in this instance through the kernel k . To demonstrate this, for each observation y we sample the kernel k randomly as a realisation of {\mathbf{k}}\sim\mathcal{GP}(11,\lambda_{\text{Matern}}=0.3,\sigma_{\text{Matern}}=0.25) , representing a random 2-dimensional trajectory embedded on a grid size 11\times 11 , simulated independently from x and y as a 2-dimensional trajectory from a Gaussian process with a Matérn covariance function with length scale 0.3 and standard deviation 0.25 . This procedure for sampling {\mathbf{k}} is described in [50]. We assume that the realisation of {\mathbf{k}} is known at inference time. Therefore, for each tuple (x,y,k) , the posterior (3) becomes \pi_{\theta}(x|y,{\mathbf{k}}=k)\propto p(y|x,{\mathbf{k}}=k)p_{\theta}(x) .

S4.SS1.SSS5.p2.1 | The above experiment shows unfolding an MCMC architecture effectively encodes A into the trained network which is beneficial when working with a range of similar forward operators. To highlight this property further, Section B.1 shows numerical results when comparing each of the above models on out-of-training-distribution operators A .

## 2602.21160v1
https://arxiv.org/html/2602.21160v1

S2.SS5.p2.1 | We use the third-order term as a diagnostic rather than a correction. Including it yields C_{k}^{(3)}=\tfrac{1}{2}\mathrm{Var}[p_{k}]/\mu_{k}-\tfrac{1}{6}\,m_{3,k}/\mu_{k}^{2} , but the 1/\mu_{k}^{2} singularity can drive this quantity negative for right-skewed distributions near the simplex boundary, violating non-negativity (A0). More fundamentally, adding Taylor terms improves accuracy only when posterior samples are tightly concentrated around the mean, which is precisely not the high-uncertainty regime where the metric matters most. The skewness ratio \rho_{k} (Section 2.5) instead flags when the second-order approximation is unreliable, without compromising the guarantees of C_{k} .

S5.SS2.SSS0.Px2.p1.1 | On CIFAR-100, the 1/\mu_{k} normalisation amplifies contributions from low-probability classes, inflating \sum_{k}C_{k} relative to MI by 1.17\times for the low-rank model and 1.89\times for MC dropout. The \mathcal{O}(K^{2}) scaling analysis and mitigation strategies are detailed in Appendix F.3.

S6.p3.1 | A finding we did not anticipate is that the posterior approximation shaped metric behaviour at least as strongly as the metric itself. Switching from variational inference to MC dropout reversed the ranking of our deferral policies, because dropout inflated skewness precisely for the rare classes where the Taylor expansion is most sensitive. The disentanglement experiments sharpened this further: freezing a pretrained backbone and attaching a Bayesian head degraded AU/EU separation by over an order of magnitude compared to end-to-end training, even when the Bayesian component was identical. This raises a question for the growing literature on post-hoc Bayesian methods: if features are learned without any posterior objective, the resulting variance structure may not support meaningful epistemic attribution regardless of the last-layer treatment. We do not suggest post-hoc methods lack practical value, but the quality of their uncertainty outputs deserves scrutiny commensurate with the attention given to their scalability.

原 TeX仅二阶近似，不作为exact MI：
C_{k}(x)=\tfrac{1}{2}\,\mathrm{Var}[p_{k}](x)\,/\,\mu_{k}(x)

## actual owner — books/part-06-ai-infrastructure/66-evaluation-system.md

L140–156:
### Continual Update 需要同步推进 Calibration State

只在模型 accuracy 明显下降后重新评估，在更新稀少、分布稳定时成本最低；continual fine-tuning 会持续改变 score distribution，使旧 threshold 或 conformal set 的 coverage 在 accuracy 尚未报警时已经失效。更完整的 release identity 因而同时版本化 model artifact 与 task-specific calibration artifact，并在每次更新后执行小规模 calibration replay：

```text
model update
-> task-specific calibration replay
-> coverage / calibration evidence
-> accuracy gate AND coverage gate
-> promote model + calibration artifact
   or freeze and rollback together
```

这把 uncertainty 从一次性 benchmark 变成 release state，却依赖 calibration sample 与部署分布的 exchangeability。现有结果覆盖三类 model family、八个以 classification/MCQ 为主的任务序列；`m=200`、低于 1% replay 的结论不能外推到开放式 generation，后者在论文中仍属探索。Exchangeability 或 coverage Gate 失败时应冻结 promotion，回退上一组 model/calibration artifacts；accuracy 与 coverage 两条 Gate 必须并存，不能相互抵消。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-23987:start -->
模型更新与 calibration 更新属于同一个 release transaction，但 accuracy evidence 与 coverage evidence 保持独立。

L309–314:
Judge 自身的 task competence、directional bias 与对更强 examinee 的 leniency 也必须拆开测。能力较强可能提高 judging accuracy，却不会消除系统性宽松或偏向；无标签 disagreement 只能生成待校准状态，不能替代人工 anchor。Route/defer 更不能读取 verbal confidence 直接决策，而应比较模型相对外部 prior 的边际 proper-score 收益；先验更强或 domain 漂移时，保留 crowd、market、rule 或人工分支。

<!-- source-family:SF-2026-ARXIV-2609-12002 -->
<!-- source-family:SF-2026-ARXIV-2609-12101 -->

这套校准降低硬判决噪声，却依赖 exchangeability、model pool 与 prompt 分布稳定；marginal coverage 也不是每个模型都覆盖。Judge、候选池或 rubric 漂移时必须重新校准，无法满足前提时回退人工标注或报告无序区间。现有证据不支持把低成本 judge 结果当作人类真值。

## actual owner — books/part-03-multimodal-world-models/23-multimodal-representation.md

L137–149:
### 阶段三：共享 token space

系统开始把图像、视频或音频压缩为离散 codes，与文本 ID 一起交给共享 autoregressive backbone。它的吸引力是统一 objective 与生成接口：所有 modality 都可以表示成“预测下一个 ID”。

但离散化不会免费发生。codebook size、层数和 stride 决定序列长度与 fidelity；quantization error 会进入训练分布；codec 与 backbone 版本不一致时，同一 ID 可能不再代表同一信号。统一协议减少模型接口数量，却增加 codebook governance。

共享 codes 还要决定保留的是像素重构还是理解语义。若每次生成视觉中间状态都先渲染成图，再交给视觉 encoder 读取，接口直观且方便人工检查，却把渲染误差和重复编码带入推理。一条条件分支以已有理解模型的行为为约束训练语义 quantizer，由生成分支预测这些 codes，再由理解分支重新处理并写入自己的 KV；像素 decoder 独立训练，只在需要可视化或像素评价时调用。省去像素往返不等于省去重新计算，也不能把生成分支的 KV 直接冒充理解状态。

这种选择用低层细节和 decoder 独立性的代价换取语义中间状态复用，还可能继承原理解模型的盲点。[LatentUM 的受限案例](https://arxiv.org/html/2604.02097v1#S3)支持 InternVL3.5-4B 路线中的表示消融、图像生成与视觉规划；它的 action-conditioned recurrent rollout 仍先渲染、再编码下一帧，不能称为已经实现全 latent World Model。细节保真优先、需要独立感知验证或闭环接口仍依赖像素时，保留独立 encoder/decoder 更合适。

<!-- source-family:SF-2026-ARXIV-2604-02097 -->

### 阶段四：native multimodal representation

## actual owner — books/part-04-training-system/27-data.md

L353–355:
生成器的大小也不能脱离生成要求单独选择。固定来源与目标训练预算时，简单改写可能在较小生成器上已经足够，复杂的 Guided Rewrite 则可能需要更强生成器才能保持有用结构；输出严格符合格式，也不等于目标模型从中学到更多。数据选择因此要联合记录 prompt 要求、generator identity、source partition 与原始/合成 mixture，并分开验收格式执行率、语义保真和固定训练 recipe 下的任务效用。提高生成器规模、增加模板或把合成量填满预算，分别改变生成成本、分布和重复次数，不能把它们合成一个“数据质量”数字。<!-- source-family:SF-2026-ARXIV-2604-13977 -->

有限的合成预训练对照支持这条条件分支，而非通用的小生成器优先规则：多数受测格式中扩大生成器没有稳定收益，但复杂改写存在较大生成器占优的反例；混入原始文本又能缓解纯合成数据在部分 NLU 任务上的退步。模板多样性与收益的跨家族相关没有隔离模板本身的因果作用，同 token 预算也不等于相同 unique-data 或生成总成本。采用时应保留任务切片、回归检查及真实数据回退；生成要求简单、原始语料可靠或预算不足以做联合选择时，较小生成器和固定 mixture 仍是合理旧路径，而不是把作者某一配置的最优规模移植到所有任务。

## actual owner — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

L157–159:
Gaussian 噪声下，posterior mean 足以把平均残差换成 marginal score，这解释了平方去噪回归为何是合理接口；改变噪声分布后，这份充分性不自动保留。对可归一化、具有相应可微与可积条件的 elliptical noise，一条替代分支从 posterior 平均 noise log-gradient 求 score。若噪声由形状参数 β 与尺度矩阵 Σ 定义，求值残差的 energy 必须与它们匹配；β=2 的 Gaussian 情形退化为 mean residual，非 Gaussian 情形通常需要整个 posterior 的加权残差期望，而不是把原 MSE mean 直接代入。所谓 path derivative 在这里固定 posterior measure，只对残差函数的求值位置求导，不能连同生成 posterior 的路径一起微分。<!-- source-family:SF-2026-ARXIV-2512-23818 -->

这个接口让 noise law、posterior learner 和 score 求值分别接受核验，没有消除学习或采样成本。训练必须覆盖部署所用的噪声参数族；有限 posterior samples 引入 Monte Carlo 误差与额外调用，求解器仍有积分误差，零残差处不光滑的 energy 还需检查定义和可积条件。受限二维分布实验及其近似参考不证明任意模型质量更好，也不把非 Gaussian 更新升级为通用 reverse SDE。posterior 失配、样本预算不足或净收益未验收时，保留 Gaussian mean/MSE 接口与原有 sampler，而不由一个能量公式批准任意临时换噪声。

## 20731 PRE — 在Ch23当前141后/143前两段；没有写入或lease

固定长度的离散 message 也可在多次观察中更新，而不是每个新 crop 都增加一段 tokens：同一表示模型消费旧 message、当前局部 crop 与相对位移，再将新 message 量化并送回下一轮；最后才以这份状态条件生成整图。训练随机化 crop 数，避免预先给未来观察保留固定槽位，并只对最后一次更新回传梯度。这把预算从“每帧生成多少 codes”转成“有限状态怎样重新分配已观察信息”，不意味着被覆盖的细节仍可恢复，后续 token 也不是独立的对象真值。

语义对齐与重构需分别验收：[COMiT的受限对照](https://arxiv.org/html/2602.20731v1)用DINOv2语义对齐、flow reconstruction及local-crop训练形成可读结构；更大模型可继续改善重构却降低语义probe，单global crop已成本最低，增加local crop只有部分任务的有限增益。最佳IoU token由gold mask离线选择，不能当在线实体定位或内部因果；32 GH200/200epoch训练、循环编码及adaptive policy的额外decode都计费。存储/encoder/decoder与probe identity应一起版本化；语义退步、细节丢失或循环费用不合算时，保留一次性codec、更长message或独立encoder/decoder，不从重构保真批准生成状态的事实用途。
