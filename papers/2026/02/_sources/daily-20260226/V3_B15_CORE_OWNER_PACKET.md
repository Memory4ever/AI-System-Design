# B15 — 八项最小必要原证与actual owner（安全终态，旧PRE保历史）

2026-10-06 feb26_close_oct06非原packet作者定点核：20937原§4/AppB与actual Ch28 656–658、20943§3.2/4.2/4.4与Ch25 1001–1009、20972§2–4/AppD与Ch27过滤/重训/派生metadata、20973§4/5.1/5.4与Ch66难度切片/3671–3673通过具体已有覆盖；20951§4/5/AppH及20976§3–7/限制按本包窄贡献仅报告。20945原§2–4/实际Ch31与20980原§3.3–3.4/4.3/实际Ch23两段真实差额已root授锁后窄写，actual正文/完整邻接/自身末注root非写入者POST通过，整合安全终态已同步；以下旧PRE保历史，不是等锁/待写队列。20980注意力loss实际为Frobenius MSE，摘要中“attention KL”不采用。未运行artifact/复现，原ND/对照分母与关键反侧保留。

## 2602.20937v1
https://arxiv.org/html/2602.20937v1；paragraph身份保留：

Thmassumption3.p1.1 | The batch size, B , is fixed and independent of the width, that is, B=\Theta(1) . If i denotes the index of a training sample in the batch then,

S4.SS1.p2.1 | The scaling factors for the model weights and their initial variance, that is, akin to parameters \{a_{l},b_{l}\}_{l=1}^{L} in the abc -parameterization, can be computed by satisfying the condition on ||\mathbf{W}_{l}||_{*} in (C.2.). More rigorously, let us define the model weights as \mathbf{W}_{l}=\sigma_{l}\tilde{\mathbf{W}_{l}}\in\real^{n_{l}\times n_{l-1}} where the elements of \tilde{\mathbf{W}_{l}} are sampled from some initial distribution with scaled variance, n^{-2b_{l}}\sigma^{2} . For ease of theoretical analysis, we fix b_{l}=0 for all layers. Then, ||\mathbf{W}_{l}||_{*}=\sigma_{l}||\tilde{\mathbf{W}_{l}}||_{*} . Since ||\tilde{\mathbf{W}_{l}}||_{*} is a random matrix with unit variance, existing results in random matrix theory can be leveraged to deduce the scaling of the spectral norm in terms of matrix dimensions (Rudelson and Vershynin, 2010) Vershynin (2018). Then, \sigma_{l} can be computed by equating \sigma_{l}||\tilde{\mathbf{W}_{l}}||_{*}=\Theta\left(\sqrt{n_{l}/n_{l-1}}\right) .

A2.SS1.p2.1 | It is interesting to note that since the theoretical underpinnings for \mu P hold in infinite width (Yang and Hu (2020)), the model width has to be “large enough” for the coordinate check plots to stabilize. This is especially observed in the coordinate check plots for LAMB (Fig. 9 and Fig. 16) where the mean values of the feature vectors initially increase, but gradually stabilize with increasing model width. This phenomenon is also observed in Fig. 2 which demonstrate the zero-shot learning rate transfer across model width on the NanoGPT model. In the minimum validation loss tables for ADOPT (Table 7) and LAMB (Table 11) the optimal value of the learning rate gradually stabilizes after a width of 256, whereas for AdamW (Table 5) and Sophia (Table 9) the optimal learning rate stabilizes after a width of 128. These inconsistencies across optimizers also suggest that introducing a “base model width” for \mu P scalings will introduce another HP. Therefore, we fix the value of the base model width to 1 in our implementation. In comparison to NanoGPT, the width scaling plots (Fig. 3) for Llama2 show that the model is “large enough” for the optimal learning rate to stabilize from the smallest model width of 128 . This is perhaps because for width of 128 , the total number of parameters in Llama2 is significantly higher than the total number of parameters in NanoGPT.

A2.SS1.p3.1 | The second set of simulations empirically evaluate the performance of the depth-scaling parameterization in existing works (Yang et al. (2023b); Dey et al. (2025)). The coordinate check plots (bottom row) for depth-scaling demonstrate that the feature vectors are stable with increasing model depth. In the coordinate check plots for ADOPT and LAMB (Figs. 7 and 9) the feature vectors stabilize after a depth of 16, while for AdamW, Sophia and Shampoo (Figs. 6, 8 and 10) the feature vectors are stable for shallow depths too. This phenomenon is similar to our observations for \mu P, because the depth-scaling parameterization is also derived for an infinite depth limit (Yang et al. (2023b)). Therefore, to prevent tuning an additional “base model depth” HP, we fix its value to 1 in our simulation setup. However, the loss plots in Figs. 11, 12 and 13 do not consistently demonstrate zero-shot learning rate transfer across increasing model depths. While the validation loss tables for AdamW (Table 6) and Sophia (Table 10) demonstrate that the optimal value of the learning rate stabilizes for deep models, the same is not observed for ADOPT (Table 8), LAMB (Table 12) and Shampoo (Table 14), where the value of the optimal learning rate oscillates as the depth is increased. These results suggest that deriving depth-scaling parameterization for different optimizers needs a more thorough theoretical analysis. Additionally, performing simulations on a finer grid of learning rates can also give further insights into the depth-scaling behavior.

## 2602.20943v1
https://arxiv.org/html/2602.20943v1；paragraph身份保留：

S3.SS2.SSS0.Px2.p2.1 | Specifically, for each incoming frame I_{t} with pose P_{t} , we first identify all scene tokens that lie within the camera frustum. Among these candidates, we select the closest K tokens based on their distance to the camera center, forming a visible set:

S3.SS2.SSS0.Px2.p2.3 | The updated scene representation is constructed by replacing the visible tokens with their refined versions, appending the newly created tokens, and keeping all other tokens unchanged:

S4.SS2.p2.1 | Our method exhibits nearly linear time complexity in the input sequence length n , while the baseline (STORM) displays quadratic growth. Although both methods show roughly linear memory growth, our method scales more slowly and uses approximately 25% less memory for 16s sequences. All measurements exclude the Gaussian rendering stage to focus on the behavior of the reconstruction networks.

S4.SS4.p3.1 | Interestingly, even without scene tokens in variant (2), the model still benefits noticeably from iterative training across temporal chunks. Empirically, we find that the model learns a prior over the correlation between opacity and time: earlier timesteps tend to produce short-range Gaussians, while later timesteps produce long-range Gaussians. This learned temporal prior helps allocate Gaussians more effectively across the sequence and contributes to overall performance gains, even in the absence of explicit scene-token memory.

## 2602.20945v1
https://arxiv.org/html/2602.20945v1；paragraph身份保留：

S3.SS1.SSS0.Px1.p2.1 | As illustrated in Figure 3, the training dynamics exhibit stark differences. Training exclusively on hard prompts results in catastrophic failure. The policy entropy spikes drastically, and the rollout length collapses prematurely. Consequently, downstream performance metrics (e.g., Mean@8 on AMC and Olympiad Bench) degrade significantly. This suggests that when the model struggles to generate correct answers, the RL signal becomes dominated by the length penalty on incorrect rollouts, leading to reasoning collapse. We attribute such an issue to the sparsity of positive samples, which leads to the overfitting on short output length. Conversely, training on the easier counterpart yields the most stable trajectory. The policy entropy remains low and stable, indicating consistent positive reinforcement. The rollout length adapts smoothly to the target budget. Crucially, despite training on easy prompts, the performance on relatively tough tasks (e.g., AIME’25) is comparable to (or even slightly exceeding) training on the full dataset.

S3.SS2.SSS0.Px1.p2.1 | For masking all incorrect rollouts (-I), we only penalize overlong and correct rollouts. The training signal only contains a) short and correct rollouts with positive reward and b) overlong and correct rollouts with negative reward. In this way, the model would hack this bias to generate short output. As shown by the orange line, the policy entropy explodes after 400 steps and rollout length collapses precipitously. The model abandons reasoning entirely to satisfy the length constraint. Meanwhile, when masking overlong correct and short incorrect rollouts (-L&C-S&I), the dynamics are similar. The training signal only contains a) short and correct rollouts with positive reward and b) overlong and incorrect rollouts with negative reward.

S3.SS2.SSS0.Px4.p1.1 | Additionally, we compare these complex shaping strategies against a simple baseline sampling at target length (i.e., L_{R}=L_{T}=4k , brown line). Compared to Vanilla ( L_{R}=16k,L_{T}=4k ), the positive samples are roughly the same (correct rollouts that are less than 4k ) while the negative samples are much shorter (4k vs. 6k). We can observe that it achieves the optimal Pareto frontier. We attribute such success to avoiding the harmful explicit length bias trap that short is correct. Typically, the positive rollouts are shorter than negative ones, which implictly encourges the model to be short yet accurate.

Sx1.SS0.SSS0.Px3.p1.1 | In this paper, we conduct extensive experiments (about 0.2 million GPU hours) in a unified protocol on the DeepSeek-R1-Distill-Qwen-1.5B. Moreover, we extend our evaluation to the Qwen3 family, such as Qwen3-30B-A3B-Instruct-2507. However, due to the limited GPUs, we do not evaluate on extremely large LLMs such as Qwen3-235B-A22B-Instruct-2507. We leave it for future work.

## 2602.20951v1
https://arxiv.org/html/2602.20951v1；paragraph身份保留：

S4.I2.i1.p1.1 | Target Region. For p_{t}\in\mathcal{P}_{T} mapped to p_{r} , we replace the positional embedding (PE) and the value embedding of p_{t} with those of p_{r} : \tilde{Q}^{(\ell)}_{p_{t}}=\text{RoPE}(Q^{(\ell)}_{p_{t}},p_{r}) , \tilde{K}^{(\ell)}_{p_{t}}=\text{RoPE}(K^{(\ell)}_{p_{t}},p_{r}) , and V^{(\ell)}_{p_{t}}\leftarrow V^{(\ell)}_{p_{r},\text{inv}} .

S4.I2.i2.p1.1 | Background Region. For a non-target patch p_{b}\in\mathcal{P}_{B} , we keep their original positional information and reuse the V^{(\ell)}_{\text{inv}} values to maintain the context of the original image: \tilde{Q}^{(\ell)}_{p_{b}}=\text{RoPE}(Q^{(\ell)}_{p_{b}},p_{b}) , \tilde{K}^{(\ell)}_{p_{b}}=\text{RoPE}(K^{(\ell)}_{p_{b}},p_{b}) , and V^{(\ell)}_{p_{b}}\leftarrow V^{(\ell)}_{p_{b},\text{inv}} .

S5.p3.1 | We construct ArtiBench with 1K images generated by five state-of-the-art diffusion models, Stable Diffusion3.5 [11], FLUX-schnell/dev [5], Qwen-Image [49], and Nano-Banana [13], with the prompts sampled from three datasets, MS-COCO [7], PartiPrompts [52], and FuseCap [44]. For annotation, we involve 12 human annotators and label each image with: 1) a binary indicator denoting the presence or absence of artifacts, 2) bounding boxes for all artifact regions, and 3) concise descriptions of the observed abnormalities. The dataset is balanced with an equal ratio of artifact-free and artifact-containing samples. Further details on the construction and annotation pipeline are provided in Appendix E.

A8.p2.1 | Test-Time Scaling. At inference time, we use the verifier as a reward model in a compute-scaled best-of- N sampling procedure [28]. For each prompt, round r samples 2^{r} independent latent noises, generates all corresponding images, and evaluates them with the verifier. The highest-scoring image is retained, and the search space doubles in the next round. This random-search strategy expands the candidate pool exponentially, enabling the diffusion model to reliably discover images with fewer artifacts without modifying the weights of the model.

## 2602.20972v1
https://arxiv.org/html/2602.20972v1；paragraph身份保留：

S2.SS3.p3.1 | On the other hand, human-provided annotations are not always better than MLLM-generated ones. For certain categories, models trained on MLLM-annotated data surprisingly outperform those trained on human-annotated data. Figure 3(b) illustrates the top-10 categories on O365, ranked by the performance difference between models trained on MLLM-annotated data and those trained on human-annotated data. We observe that for many categories, models trained on MLLM-annotated data significantly outperform those trained on human-annotated data. This is primarily because the annotation task in O365 is substantially more challenging than in COCO 2014, as it includes many hard-to-recognize categories, leading to much more manual annotation error compared to COCO 2014. These results suggest that using MLLMs to replace human annotators not only reduces the cost of manual annotation significantly, but also offers certain advantages in annotation quality compared to human annotations. Unlike human annotators, whose performance may suffer from inattention or fatigue, MLLMs provide consistent annotations free from such human-induced variability. This further highlights the potential of MLLMs as a scalable and reliable alternative to human annotators.

S4.SS1.SSS0.Px1.p1.1 | To evaluate the performance of the proposed method, we perform experiments on three benchmark datasets, including MS-COCO 2014 (COCO 2014), MS-COCO 2017 (COCO 2017), and Objects365 (O365). We perform several pre-processing steps on all datasets; detailed dataset descriptions and pre-processing protocols are provided in Appendix D. For COCO 2017 in particular, we use the unlabeled split as a practical application scenario for our method, which contains approximately 123 k images without manual annotations. Since ground-truth labels are unavailable, we cannot directly score annotation quality. Instead, we train models on the annotations produced by each method and assess annotation quality via their performance on the COCO 2014 validation set.

A4.SS0.SSS0.Px4.p1.1 | The human annotations referred to in this paper are the original annotations provided in the respective datasets. Below, we briefly introduce the workflows and methodologies related to image category annotation in each dataset.

## 2602.20973v1
https://arxiv.org/html/2602.20973v1；paragraph身份保留：

S5.SS1.p2.1 | Metrics To evaluate the performance of the LLMs, we use Accuracy as the metric to evaluate the generated truth values. Also, following the P-FOLIO (Han et al., 2024b) paper, we try two metrics to evaluate the generated proofs: ROUGE (Lin, 2004) and pass @ k (Chen et al., 2021). The Accuracy metric reports the percentage of correct truth value (True/False/Unknown) generated by the tested LLMs. The ROUGE metrics including ROUGE-1, ROUGE-2, and ROUGE-L (Lin, 2004), are used to compare the model-generated proofs with human-written proofs. The pass @ k metric is defined as the same in P-FOLIO (Han et al., 2024b): After sampling k proofs from the tested LLM, the pass @ k represents the percentage of instances in which at least one generated proof follows the same reasoning process as the annotated proof. The verification process is automatically checked by GPT-4o, and the prompt templates are provided in Appendix D.

S5.SS4.p1.1 | In Section 5.2, we observe that LLMs exhibit low accuracy when solving proof-by-cases type FOL problems. Consequently, employing another LLM to evaluate the correctness of the answers (e.g., the Pass@k metric in Section 5.3), would likely introduce significant errors. To mitigate this issue, we further conduct a manual experiment to evaluate the answers generated by the GPT-4o model. Specifically, in this experiment, we utilize GPT-4o (web interactive version) to generate a proof with a corresponding label for each problem in our PC-FOL dataset. These proofs are then examined by a professional mathematician, who categorized each instance into one of three categories: Wrong Label with Wrong Proof, Correct Label with Wrong Proof, and Correct Label with Correct Proof. The distribution of results across these categories is reported in Table 8.

S5.SS4.p2.1 | We can now answer the research question “(2): Are the proofs generated by LLMs correct?” based on the results in Table 8, which indicates that for linear-reasoning problems, when the model assigns a correct label, the corresponding proof is also likely to be correct. However, for proof-by-cases problems, not only is the label accuracy only 54.21 \% , but fewer than half of these samples with the correct label actually get a correct proof. Through our manual checking of the proofs, we identify four main reasons for the proof errors: misapplication of premises, misinterpretation of disjunctive statements, mistakes in inductive and deductive reasoning, and semantic misunderstandings. In particular, for proof-by-cases problems, the predominant cause of incorrect proof is the misapplication of disjunctive statements, where the tested LLM often misunderstands exclusive disjunctions, or fails to provide proofs that address separate scenarios.

## 2602.20976v1
https://arxiv.org/html/2602.20976v1；paragraph身份保留：

S4.SS1.SSS0.Px2.p1.1 | A model produces a response r_{i}=M(q_{i}) . The response set of a model is \mathcal{R}=\{r_{1},r_{2},\dots,r_{N}\} . We define four response subsets of \mathcal{R} , 1) Harmful Behavior \mathcal{H}=\{r_{i}\in\mathcal{R}\mid r_{i}\text{ adopts or is similar to }h_{i}\} , 2) Safe Alternative \mathcal{S}=\{r_{i}\in\mathcal{R}\mid r_{i}\text{ provides an environmentally safe alternative}\} , 3) Warnings \mathcal{W}=\{r_{i}\in\mathcal{R}\mid r_{i}\text{ contains environmental or legal warnings}\} , and 4) Aligned Impact \mathcal{A}=\{r_{i}\in\mathcal{R}\mid r_{i}\text{ explicitly aligns with }e_{i}\} .77 7 We employ GPT-5 to annotate each model response by assigning it to the corresponding subsets and extracting supporting evidence sentences. Human verification on 200 randomly sampled instances shows a 94% human-GPT agreement rate.

S6.SS0.SSS0.Px2.p1.1 | Response length is the dominant factor affecting proactive awareness. All models exhibit a substantial drop in Proactive Rate while Blind Spot Rate increases and Harmful Adoption Rate substantially increase when constrained to short answers across both languages, indicating that proactive environmental reasoning is highly verbosity-dependent.

S7.SS0.SSS0.Px2.p2.1 | 1) Compared with vanilla short responses, the system prompt yields a consistent and substantial increase in ProR across all evaluated models, with absolute gains ranging from 0.15 to 0.40. Both WarnIntel and SafeAlt rise markedly, with particularly large improvements observed for Qwen. On the other hand, such instruction may also drive generic disclaimers as GR increases (except GPT).

Sx1.p2.1 | Second, our definition of proactive ecological intelligence focuses on a specific set of environmentally and legally grounded safety behaviors (e.g., SafeAlt, WarnIntel, GR, and Blind). However, model responses may contain other forms of potentially relevant or even beneficial warnings that fall outside our taxonomy, such as reminders about personal safety, social responsibility, or unrelated legal risks. These behaviors are not counted as proactive ecological reactions in our framework, which may lead to an underestimation of the full spectrum of safety-oriented reasoning exhibited by some models.

## 2602.20980v1
https://arxiv.org/html/2602.20980v1；paragraph身份保留：

S3.SS3.SSS0.Px2.p1.1 | This path operates on the perturbed image I_{cor}=\mathcal{C}(I) . The corresponding input sequence S_{cor}=\{I_{cor},Q,CoT,Ans\} . We enforce a latent-level dependency by replacing the latent representations at each decoder layers in the corrupted path with corresponding latents in \mathbf{T}_{lat} derived from the intact path. The model then generates the logits \mathbf{P}_{cor} for the perturbed sequence.

S3.SS4.SSS0.Px1.p2.1 | Specifically, the objective is to conduct a logit-level loss between \mathbf{P}_{int} and \mathbf{P}_{cor} , targeting at the tokens corresponding to the ground-truth Ans . This targeted alignment compels the latent reasoning states to “crystallize” into targeted visual representations that are functionally indispensable for the final generative process.

S4.SS3.p3.1 | Furthermore, we investigate how the specific formulation of alignment affects model performance. While adopting a standard MSE-based alignment provides marginal gains, it lacks the flexibility to capture complex cross-modal dependencies. Notably, we found that applying KL-type alignment to the entire attention map (from answer to both image and latent tokens) actually degrades performance. The model achieves its best performance only when the alignment is restricted to the attention from answer tokens (as queries) to latent tokens (as keys).

S4.SS3.p4.1 | Abalation on corruption strategy. We evaluate different corruption strategies \mathcal{C} in the proposed SIC module, including Gaussian blur, random masking, colour distortion, jigsaw shuffling, additive Gaussian noise. As shown in Table 5, Gaussian blur consistently achieves the best performance across all benchmarks, while other corruption types lead to inferior results.

### 20937 C.2 原display formula TeX（L1295–1320内机械筛出）
||\mathbf{W}_{l}||_{*}=\Theta\left(\sqrt{\frac{n_{l}}{n_{l-1}}}\right)\quad\text{ and }\quad||\Delta\mathbf{W}_{l}||_{*}=\Theta\left(\sqrt{\frac{n_{l}}{n_{l-1}}}\right),\quad\text{ for }\quad l=1,2,\ldots,L.

### 20945 原Eq2 TeX（原txt L337）
R_{T}(x,y_{i})=\mathbb{I}(y_{i}\text{ is correct})\cdot\mathbb{I}(L(y_{i})\leq L_{T}),

## Actual owner books/part-04-training-system/28-pretraining.md

### 原文件L656–658
把 MHA 改成 GQA 后继续沿用满秩矩阵假设与旧学习率，最容易维持工程连续性，却可能把 head repetition、非满秩投影和深度变化产生的尺度偏移误判为架构收益。一个更严格的参数化先用适配非满秩权重的 modified spectral norm 描述有效 operator scale，再据此导出 GQA repetition、depth 与 weight-decay 的 maximal-update scaling。参数化 owner 只给出可迁移的初始化/学习率 proposal，真实训练曲线仍拥有验收权。

这提高小规模到目标规模 transfer 的可解释性，却依赖模型形状、coordinate checks 与推导假设；公式错误会表现为 activation/update scale 漂移，而不是立即报错。exact-v1 只支持 §3 推导、§4 与 Appendix B 的所测形状，且 Appendix B.2 已给出某类 coordinate check 的失败边界。架构超出校准域、rank 假设不成立或训练信号冲突时，应回退邻近规模 sweep，而不是把 μP 公式当作免调参保证。<!-- source-family:SF-2026-ARXIV-2605-15290 -->

## Actual owner books/part-03-multimodal-world-models/25-multimodal-world-models.md

### 原文件L1001–1003
## Persistent World State 需要流式更新与观测校正

逐帧重新编码会重复计算并积累几何漂移。流式 point cache 可以保存可更新空间状态，让新 observation 只修正受影响区域；表示与生成器使用同一 latent domain，还可减少反复域转换。cache owner 必须定义写入、淘汰、冲突和 observation correction，生成结果不能覆盖真实观测 authority。

### 原文件L1009–1009
持久状态提高长序列一致性，也会累积错误和占用内存；scene change、定位失败或 cache confidence 越界时，应重建或回退短窗口。作者场景中的生成指标不证明它已学习真实因果动力学。

## Actual owner books/part-04-training-system/31-rlhf.md

### 原文件L785–790
同一问题内部的 verifier budget 也有 curriculum 条件：弱 policy 可能从较容易的测试获得有效正反馈，较强 policy 才能利用困难切片；不能仅按参数量或“测试越难越好”选比例。一条受限分支先依据基础 policy 的能力诊断预选各 test tier 的训练配比 α，再单独设 reward weight w；抽哪些测试和怎样计分是两项状态，这不是训练期间在线自适应的难度 controller。[TAROT 的有限 coding 对照](https://arxiv.org/html/2602.15449v1#S3)中不同模型/目标域的最佳策略不同，某些简单或完整测试基线仍更好；reference、生成器覆盖与测试生成成本也限制可归因范围。Tier 身份、诊断人口、α/w 和执行预算均须版本化，诊断失准或尾部质量回归时保留固定完整测试、既有 curriculum 与独立 evaluator，不能以局部均值提升授予通用 hard-first 或正确性保证。<!-- source-family:SF-2026-ARXIV-2602-15449 -->

### Imperfect Verifier 把监督噪声与 Rollout Compute 绑在一起

RLVR 假设 verifier 能稳定区分正确与错误，实际 false positive 会奖励错误轨迹，false negative 会丢弃有效探索；增加 rollout 数量可能同时放大这两种噪声。训练合同应记录 verifier confusion profile、rollout budget 与 policy distribution，并把“更多采样”和“更好监督”作为独立轴。收益是能选择 compute–supervision trade-off，代价是需要可控噪声估计与额外验证；确定性可执行任务仍可使用简单 verifier。现有结果仅覆盖 Qwen2.5、GSM8K 与 GRPO，不构成跨任务定律。


## Actual owner books/part-04-training-system/27-data.md

### 原文件L329–332
最直接的 synthetic-data pipeline 是让模型生成任务、回答或 Agent trajectory，再由另一个 model judge
过滤。它便宜、覆盖开放语义，在 verifier 难以形式化的任务中仍然合理；但 generator 和 judge 可能共享
事实错误、风格偏好与同源 blind spot，语言上自洽不等于环境中可执行。


### 原文件L240–248

- 规则过滤：语言、长度、字符分布、重复符号、HTML 结构。
- 内容分类器：教育价值、可读性、主题、安全或垃圾概率。
- Source-level policy：来源许可、可信度、时间与地域。
- Model-based filtering：使用模型对文本质量或目标相关性评分。

过滤器会降低明显噪声，也会带来选择偏差。规则可能误伤代码、公式、方言或低资源语言；模型过滤器会继承评分模型的偏好；过度追求“教科书风格”可能减少真实世界多样性。

因此过滤策略需要同时报告 retention rate 和分布变化，而不能只报告“删除了多少低质量数据”。删除前后各语言、领域、长度和来源发生了什么，才决定模型看见了什么。

### 原文件L308–310
当不良行为是在一次 preference training 后才发现，事后数据诊断还需要共同的表示坐标。可以把同一 prompt 的训练前、训练后 response 都 teacher-force 到同一个 initial checkpoint，取 response-token 的 activation 均值差作为行为方向；训练 pair 的 chosen/rejected 也在这个 checkpoint 上取差，再按两种差的 cosine 提出数据 ranking。这样比较的是 response 在共同模型中的表示，而不是直接相减两套 checkpoint 的 hidden state；prompt/pair、层选择、initial checkpoint 与 scorer 必须一同绑定。ranking 只提出值得干预的数据集合，不证明每个样本造成了该行为。<!-- source-family:SF-2026-ARXIV-2602-11079 -->

验证责任随后从 probe 转回训练：从相同起点，以相同干预数量比较过滤、交换 chosen/rejected、随机及其他 selector 的重训结果，再检查行为与 utility。[有限 OLMo2 对照](https://arxiv.org/html/2602.11079v1)中，小规模过滤并非最优，较大交换虽减少目标行为却有任务质量与拒答反侧；人工选出的行为/layer、judge 与 prompt bootstrap 也不能变成跨训练 seed 的因果保证。checkpoint 抽取、ranking、重训和审计都需成本，不能把 ranking 的估算省时当作全 pipeline 加速。诊断漂移、干预损害 utility 或无法同预算验证时，保留内容过滤、原 preference data 与小规模 canary，不把相似方向当作已经修复安全的证书。

### 原文件L800–810
人工维护 schema、统计特征和语义标签在小型、稳定数据集上清晰可靠；数据源和版本增多后，手工登记容易落后于真实 artifact。可以把 schema inference、profiling、semantic annotation 和 Croissant/JSON-LD 等标准化描述组织为一条可重放 pipeline，但它的输出仍是派生 metadata，不是来源事实本身：

```text
source snapshot + parser revision
→ schema inference and profiling
→ semantic annotation
→ typed metadata artifact
→ validation and manual override
```

自动化减少登记成本并改善跨工具发现，却会放大推断错误、敏感字段暴露和模型版本漂移。每次产物应绑定 source snapshot、工具与规则版本、置信边界及人工修订历史；高风险 license、PII 与 label 语义仍需独立检查。数据规模小或 schema 变化极少时，受控 manifest 仍是更简单的基线。

## Actual owner books/part-06-ai-infrastructure/66-evaluation-system.md

### 原文件L132–134
任务难度切片也不能只按输入长度或实体数划分。关系推理可以分别改变输入规模、任务生成器规定的 binding arity，以及识别或比较单个 operand 的难度；它们是三个不同轴。同一 arity 下更多输入可能提供额外线索，而非必然更难；实体少却需要同时满足更多关系，也可能比长输入更困难。EvalSpec 应保存生成规则和 oracle，在输出格式、scorer、推理预算可比的切片中交叉改变这些轴，不把换任务后不同的 accuracy、substructure 或 recall 拼成同一条下降曲线。<!-- source-family:SF-2026-ARXIV-2604-12176 -->

这种控制比单一长度排行榜增加生成、oracle 与样本预算，也仍只能约束已测混杂。生成器定义的 relational complexity 是任务属性标签，不是模型内部容量的计算下界；合成、多选与有限 token 预算下的失败，更不证明增加任意计算都无效。简单任务、长度已主导成本时仍可保留原长度切片，复杂关系任务再补上述交叉维度。受限关系评估支持将这些难度来源分账，而不支持通用 arity 阈值或唯一失败因果。

### 原文件L94–104
`intended use` 决定什么错误重要。例如代码补全、医疗问答和广告生成都可以计算文本相似度，但相同指标不代表相同风险。评估 specification 至少应声明：

```text
EvalSpec =
  target behavior
  + eligible population
  + failure taxonomy
  + metrics and scorers
  + slice definitions
  + thresholds / comparison rules
  + uncertainty requirement

### 原文件L3671–3673
长上下文回答可能最终正确，却引用了无关或错误 evidence path；也可能轨迹合理但终局合成失败。评测应分别保存 claim、自然 evidence trail、检索/工具事件与最终 verdict，让 scorer 只拥有对应层的判断权。这样提高诊断性，却增加标注和 trace 成本；低风险短答案仍可用 final-only baseline，关键结论则不能从答案正确反推证据链正确。

开放文本轨迹还可以先把公开参考 rationale 拆成 atomic units，再比较候选理由覆盖了哪些参考单元；但这先定义了一份新的测量人口，而不是发现模型内部真正使用的推理。拆分规则、人工筛选、参考集合、匹配器及其 reuse/阈值约束、输出与理由预算都应进入 scorer identity，不能让更长的理由或同一候选片段反复匹配制造无条件 coverage。[必要方法与反侧](https://arxiv.org/html/2602.04649v1)支持这一参考对齐分支；公开文本的一致性、与另一个 judge 的相关性不等人类事实真值或内部 faithfulness，匹配公式与提示实现尚未一致的子命题也不能用来认证奖励机制。工程上应定点人工核对拆分与匹配、同时保留 final verdict 和不匹配样本，这是测量验收推导而非作者已实现完整 guard。标注、匹配调用及更长 trace 均有成本；参考不可信、划分或匹配不稳定时，回退 final-only、可执行 oracle 或人工 evidence 审计，不让参考覆盖率替过程正确性自证。<!-- source-family:SF-2026-ARXIV-2602-04649 -->

## Actual owner books/part-03-multimodal-world-models/23-multimodal-representation.md

### 原文件L1046–1054
当文字 CoT 难以表达空间中间态时，还可以把文字与辅助图像写入统一 canvas，再压缩为连续 latent reasoning state。
这让布局、OCR 与视觉草图参与后续推理，却牺牲部分可检查性，并把 canvas codec、压缩器和 token budget 变成新的状态
身份；OCR/layout 失败会污染整条链。高风险任务仍应保留可读 trace、外部工具和最终证据验收，不能把 latent state
当作可解释证明。现有证据只覆盖作者的 VLM reasoning benchmarks。

<!-- source-family:SF-2026-ARXIV-2605-11856 -->

### Object Hallucination 需要分开视觉写入与语言读取
