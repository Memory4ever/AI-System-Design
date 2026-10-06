# B10 — 必要原证＋actual owner（3项，非整日验收）

## 2602.20720v1
https://arxiv.org/html/2602.20720v1；原HTML paragraph机械摘段：

As illustrated in Table 2, existing benchmarks (Debenedetti et al., 2024; Zhan et al., 2024) exhibit limited tool diversity and narrow test coverage. To better simulate realistic and generalizable agent scenarios, we introduce IPI-3K, a comprehensive dataset specifically designed to evaluate adaptive IPI attacks within the diverse tool ecosystems prevalent in modern systems. Specifically, IPI-3K comprises 3,691 benign agent trajectories, derived through the consolidation and reorganization of established benchmarks (Zhang et al., 2025a), covering multi-step processes that necessitate external data retrieval. Furthermore, IPI-3K includes 277 attack tools identified as possessing high-authority permissions to access sensitive user information.

Strategy Distillation.
This module aims to enhance the generalization and transferability of strategy libraries. Inspired by Inductive Logic Programming (ILP) (Cropper and Dumančić, 2022), we first abstract discrete strategies into higher-level representations. Furthermore, drawing on the pruning principle from decision tree algorithms, we employ an ASR-based metric to consolidate the extensive strategy library  \mathcal{S}  into a compact, transferable repository. This process preserves essential decision patterns while discarding redundant or over-specialized rules. Specifically, as illustrated in Fig. 4, we convert discrete textual strategies into latent semantic embeddings using a text-embedding model (Zhang et al., 2025b; Wang et al., 2024). We then apply clustering techniques (e.g., K-means (Ahmed et al., 2020)) to group semantically similar strategies. This abstraction filters out idiosyncratic, sample-specific details and induces generalized strategy descriptions capable of bypassing an agent’s security guardrails. For the consolidation phase, we utilize ASR as the primary utility metric. A subset of strategies is merged into a generalized form only if the resulting ASR degradation does not exceed a predefined threshold  \delta . Through this iterative pruning, we construct an optimized strategy library that maintains comparable ASR to the original fine-grained set while significantly reducing redundancy and enhancing cross-task utility.

Markovian Transition Modeling
We model tool-use sequences as sequential dependencies where the latent user intent is encoded within the historical trajectory  \tau_{t} . Drawing inspiration from sequential recommendation systems (Barkan and Koenigstein, 2016), we employ a first-order Markov Chain to capture the temporal patterns of tool execution. Assuming a grey-box adversary (e.g., a malicious MCP controller) can observe the most recent tool invocation  f_{t} , we define a transition probability matrix  M\in\mathbb{R}^{|\mathcal{F}|\times|\mathcal{F}|} . Each entry  M_{ij}  represents the likelihood of transitioning from tool  f_{i}  to  f_{j} , learned from all benign trajectories:

Effectiveness of Attack Enhancement (Grey-box Attack). To improve the stealthiness of IPI attacks, we design a tool selection mechanism for grey-box attackers. Due to the high costs of API calling, we employ one commercial LLM and one open source LLM to illustrate. As shown in Table 4, we report the ASR and UA with and without this mechanism.
The attack enhancement increases the ASR by 4.7% and 7.9% on GPT-4.1 and Qwen3-8B, respectively. This improvement arises because our method bypasses unrelated failure cases of LLMs by selecting the most task-relevant attack tools. This experiment demonstrates the effectiveness of our tool selection mechanism.

Strategy Analysis.
As described in Section 3, we adopt a multi-iteration attack process to optimize strategies and improve the ASR of IPI attacks.
We set the default number of iterations  k_{a}  to 5.
To validate this choice, we conduct a comparison across seven iteration settings.
As shown in Figure 8, the ASR reaches about 35% with a single iteration, and increases to over 80% as the number of iterations grows, eventually converging.
Although using 6 or 7 iterations can yield slightly higher ASR, the improvement is marginal, while the corresponding API cost grows.
Hence, we choose 5 iterations as a trade-off between attack performance and computational cost.

## 2602.20722v1
https://arxiv.org/html/2602.20722v1；原HTML paragraph机械摘段：

where  u_{i}  is the unique identifier of each prompt,  \{x_{i,j}\} ,  \{y_{i,j}\} ,  \{r_{i,j}\}  represent the set of prompts, generated responses, and corresponding rewards, respectively.  \{\alpha_{\mathcal{B}}(y_{i,j}|x_{i})\}_{j=1}^{G}  is the rollout policy’s probability, which is stored for calculating  \rho_{\alpha_{\mathcal{B}}}(\theta)  when reusing, and  |\mathcal{B}|  is the buffer size.

Let  \mathcal{B}_{\text{bad}}\subseteq\mathcal{B}  denote the buffer for difficult samples. To manage the computational overhead associated with the re-evaluation process, we limit the buffer capacity  |\mathcal{B}_{\text{bad}}|  to be equal to the training batch size. A First-In-First-Out (FIFO) mechanism is employed to automatically discard outdated samples when the buffer reaches capacity.  \mathcal{X}_{2}  is formulated as:

(3) Reused Historical High-quality Samples ( \mathcal{X}_{3} ).
To prevent underfilled batches caused by the scarcity of  \mathcal{X}_{1}  and  \mathcal{X}_{2} , we maintain a FIFO auxiliary buffer  \mathcal{B}_{\text{high}}\subseteq\mathcal{B} . To mitigate training instability from stale data,  \mathcal{B}_{\text{high}}  is restricted to high-quality trajectories from the three most recent steps. The subset  \mathcal{X}_{3}  is randomly sampled to fill the remaining capacity:

Implementation Details. All comparative experiments were run on 8 A100 GPUs with 80GB memory based on the Verl framework (Sheng et al., 2025). Identical parameters were used to ensure fair comparison, with specific details in Appendix A.7.

Tracking Difficult Samples. We visualize the training dynamics in Figure 7. BAPO exhibits a superior capability to ”unlock” difficult problems: after 3 epochs, BAPO successfully improves 31% of the samples that were initially unsolvable ( 0/8  accuracy), compared to only 19% for GRPO.

As observed in Figure 8, the assembled training batch size frequently fluctuates below the maximum configured capacity. This reduction in backward propagation load effectively offsets the computational overhead caused by off-policy re-evaluation and log-probability re-computation. Consequently, as detailed in Table. 2, BAPO maintains a training speed comparable to GRPO while requiring significantly fewer rollouts than DAPO, achieving a superior trade-off between convergence performance and computational cost.

## 2602.20727v1
https://arxiv.org/html/2602.20727v1；原HTML paragraph机械摘段：

Given a parameter matrix  W\in\mathbb{R}^{d\times d} , the rows of  W  are treated as individual elements within a collection. These row vectors are partitioned into  k  distinct clusters using the K-Means constrained with minimum cluster size (Levy-Kramer, 2018) algorithm with the Euclidean distance metric. Within each cluster  C_{i}(i=1,2,...,k) , we select the  r  row vectors exhibiting the smallest Euclidean distance to the cluster centroid  \mu_{i} . The selected rows from each cluster  C_{i}  are then aggregated to form a low-rank matrix  A_{i}\in\mathbb{R}^{r\times d} .
This process yields a set of  k  structured low-rank matrices  {A_{i},A_{2},\ldots,A_{k}}  that collectively capture the dominant row-space patterns of the original matrix  W , prioritizing proximity to cluster centers.
In our experiments,  k  is equal to  4 , and  r  is set according to the specific experimental requirements.

where  B\in\mathbb{R}^{\frac{d}{2}\times\frac{r}{2}} ,  A_{i}\in\mathbb{R}^{r\times d} , and  f_{c}  is the concate operator.  x_{i}^{1}  and  x_{i}^{2}  are equal divisions from vector  x_{i} .
 \alpha_{i}  is the output of router, i.e.,  \alpha_{i}=T\odot x_{i} , where  \odot  is the inner product.

Figure 3 shows the time and extra memory overhead during inference of different methods in multi-task experiments. During inference, since the adapters introduced by LoRA and DoRA can be merged with the original parameters, the model structure remains unchanged, avoiding additional memory overhead and time latency.
In contrast, the adapters introduced by MoELoRA and HydraLoRA can not be merged, resulting in extra memory usage and inference latency. The time consumption increased by 61.6% and 36.5% compared to LoRA.
In our method, we only need to retain the clustering location information and the matrix  B . ID-LoRA achieves a 45% reduction in extra memory usage relative to both MoELoRA and HydraLoRA, while incurring a minimal time overhead of only 0.5% compared to LoRA.

Table 3 presents a controlled ablation on the LLaMA-3.2-3B multi-task benchmark to isolate the contribution of RB (PMRC+RB vs w/o RB). To ensure parity, we configure ID-LoRA with rank  r=128  closely matching the parameter budget of the variant that omits RB. Across four multi-task evaluation benchmarks, the RB-enhanced variant delivers consistent gains, except on MATH. MATH tasks necessitate precise and accurate directional updates to the weight matrix; simply increasing the rank through the RB algorithm alone is insufficient to enhance performance. These results validate the intrinsic effectiveness of the RB algorithm in multi-task scenarios.

### 20720 原正文txt L1556–1603
Qwen-3-8B
maintains higher benign utility and demonstrates stronger resistance in utility preservation, though its ASR still climbs to 44.5%, reflecting the inherent difficulty of defending high-capacity, tool-using models against sophisticated IPI attacks.
In general, commercial LLMs are equipped with effective mechanisms to resist adversarial attacks compared with open source LLMs.
Figure 7
:
The transferability of our method in InjectAgent Dataset.
Foundation Model
Configuration
ASR
(%
↑
\uparrow
)
UA
(%
↓
\downarrow
)
GPT-4.1
w/o selection
21.4
43.8
w/ selection
26.1
44.8
Improvement
(
Δ
\Delta
)
+4.7
+1.0
Qwen3-8B
w/o selection
52.7
36.4
w/ selection
60.6
32.6
Improvement
(
Δ
\Delta
)
+7.9
-3.8
Note:
Δ

### 20722 原正文txt L2320–2407
𝒳
1
\mathcal{X}_{1}
:
We apply strictly standard zero-advantage filtering, removing only the prompts where all
G
G
responses are entirely correct or entirely wrong.
𝒳
2
\mathcal{X}_{2}
:
We replay historical
all-wrong
samples (
μ
α
,
r
​
(
x
)
=
0
\mu_{\alpha,r}(x)=0
). These correspond exactly to the difficult cases discarded by
𝒳
1
\mathcal{X}_{1}
, creating a closed-loop system that recovers waste data without requiring a difficulty threshold
c
1
c_{1}
.
𝒳
3
\mathcal{X}_{3}
:
Instead of a dynamic accuracy range, we reuse historical samples with exactly
50% accuracy
. As formally proven in Proposition
A.3
, samples with accuracy
μ
α
,
r
​
(
x
)
=
1
2
\mu_{\alpha,r}(x)=\frac{1}{2}
maximize the reward variance, thereby providing the theoretical maximum potential for single-step policy improvement
J
⁡
(
π
θ
)
−
J
⁡
(
π
θ
t
)
J(\pi_{\theta})-J(\pi_{\theta_{t}})
.
The results in Figure
5
demonstrate that even in the hyperparameter-free “Mini-test”, BAPO maintains a clear advantage over GRPO. This confirms that the structural introduction of
𝒳
2
\mathcal{X}_{2}
and
𝒳
3
\mathcal{X}_{3}
drives the performance, not the specific tuning of
c
c
values.
Component Efficacy.

### 20727 原正文txt L561–716
4.1
Parameter Matrix Row Clustering
Given a parameter matrix
W
∈
ℝ
d
×
d
W\in\mathbb{R}^{d\times d}
, the rows of
W
W
are treated as individual elements within a collection. These row vectors are partitioned into
k
k
distinct clusters using the K-Means constrained with minimum cluster size
(
Levy-Kramer, 2018
)
algorithm with the Euclidean distance metric. Within each cluster
C
i
​
(
i
=
1
,
2
,
…
,
k
)
C_{i}(i=1,2,...,k)
, we select the
r
r
row vectors exhibiting the smallest Euclidean distance to the cluster centroid
μ
i
\mu_{i}
. The selected rows from each cluster
C
i
C_{i}
are then aggregated to form a low-rank matrix
A
i
∈
ℝ
r
×
d
A_{i}\in\mathbb{R}^{r\times d}
.
This process yields a set of
k
k
structured low-rank matrices
A
i
,
A
2
,
…
,
A
k
{A_{i},A_{2},\ldots,A_{k}}
that collectively capture the dominant row-space patterns of the original matrix
W
W
, prioritizing proximity to cluster centers.
In our experiments,
k
k
is equal to
4
4
, and
r
r
is set according to the specific experimental requirements.
To refine the approximation, we introduce an initialized trainable shared matrix
B
∈
ℝ
d
×
r
B\in\mathbb{R}^{d\times r}
that reconstructs the updated parameter matrix
Δ
​
W
\Delta{W}
jointly with each cluster-specific matrix
A
i
A_{i}
.
Δ
​
W
=
∑
i
=
1
k
α
i
​
(
B
​
A
i
)
\Delta{W}=\sum_{i=1}^{k}\alpha_{i}(BA_{i})
(3)
where
α
i
\alpha_{i}
is a scalar. As shown in Figure
2
,
α
i
\alpha_{i}
=
T
⊙
A
i
​
h
t
T\odot A_{i}h_{t}
, where
⊙
\odot
is the inner product.
This blend retains key row patterns and efficiently tracks small updates to
Δ
​
W
\Delta W
.
Figure 2:
A diagram of the ID-LoRA architecture.
4.2

### 20727 原正文txt L718–824
Relying on a single shared weight matrix
B
B
significantly complicates achieving balanced and harmonious interactions among expert modules.
To address this issue, we first partition the activation vector
x
∈
ℝ
r
x\in\mathbb{R}^{r}
through matrix multiplication with
A
i
A_{i}
, then integrate these partitioned activation vectors via this unified shared low-rank matrix
B
B
, as shown in Figure
2
. The formula is as follows:
x
i
=
A
i
​
h
t
,
u
t
=
W
​
h
t
+
∑
i
=
1
k
α
i
​
f
c
​
(
[
B
​
x
i
1
,
B
​
x
i
2
]
)
x_{i}=A_{i}h_{t},~u_{t}=Wh_{t}+\sum_{i=1}^{k}\alpha_{i}f_{c}([Bx_{i}^{1},Bx_{i}^{2}])
(4)
where
B
∈
ℝ
d
2
×
r
2
B\in\mathbb{R}^{\frac{d}{2}\times\frac{r}{2}}
,
A
i
∈
ℝ
r
×
d
A_{i}\in\mathbb{R}^{r\times d}
, and
f
c
f_{c}
is the concate operator.
x
i
1
x_{i}^{1}
and
x
i
2
x_{i}^{2}
are equal divisions from vector
x
i
x_{i}
.
α
i
\alpha_{i}
is the output of router, i.e.,

### 20727 原正文txt L1714–1764
(b)
Extra GPU Memory
Figure 3:
The inference time and extra memory overhead of different adaptation methods under the same hyperparameter settings as the multi-task experiments on LLaMA-3-8B, tested on an A800 GPU.
Method
# Params (%)
MATH
MMLU
CQA
CODE
Pass@1
Pass@5
Pass@10
LoRA
1.49%
38.6
43.8
58.2
28.8
34.7
37.1
ID-LoRA (PMRC+RB)
0.77%
38.1
48.5
65.6
29.4
35.9
38.2
ID-LoRA (w/o RB)
0.83%
38.8
45.2
64.4
28.7
35.3
38.6
ID-LoRA (SS+RB)
0.77%
35.1
48.2
65.3
29.3
35.3
37.6
ID-LoRA (RS+RB)
0.77%
36.6
48.5
65.1
28.9

## Actual owner books/part-06-ai-infrastructure/72-security.md

### 原文件L684–695
### Goal Alignment 不等于组合后的授权

保持用户意图还需要区分外部文本中的有用信息与企图重定向任务的指令，而不是将所有外部 instruction 一概删除。一条训练分支给 teacher 显示注入位置与目标答案，生成保持用户任务的分析、推理和最终答案；再用 aligned/hijacked 轨迹对训练偏好 judge，让每步多个候选先经 judge 选择，才进入后续 proposal。[ReasAlign 的局部机制](https://arxiv.org/html/2601.10173v1)改变的是监督构造与路径选择，不是给 reasoning trace 授权：teacher 可见高亮及目标并非线上可用条件，偏好 judge 也不是逻辑真值或模型内部 reasoning 因果的证明。外部信息可以成为任务证据，却不能升级为 trusted user authority。<!-- source-family:SF-2026-ARXIV-2601-10173 -->

这增加合成数据、teacher、judge 和多候选搜索成本。所测文本注入下较低 ASR 与良性 SEP utility 从 98.9 到 98.0 的反退并存；默认每步三个候选不能用只统计成功任务、单候选的 token 成本认证端到端预算，失败路径、硬件、精度与总训练成本仍未披露。推理监督与答案监督还同时改变输出长度和训练目标，不能把收益唯一归因于内部推理。缺少可信意图、可靠 judge 或足够预算时，保留 canonicalized context、原单候选流程与独立 effect gate；即使路径一直贴合用户目标，下面的跨步权限关系仍须单独核验。

对每次 tool proposal 检查是否推进用户目标，适合目标已经授权、操作相互独立的短流程；编排器把一句请求自动拆成多步后，局部目标一致却可能把不应合并的权限拼在一起。例如先取某个范围的数据、再作格式转换、最后发往另一个目的地，各步表面上都服务同一目标，但真正需要批准的是 **数据范围 × 变换后的敏感性 × 最终目的地** 的关系，而不是三次孤立的文本分类。编排器只提出 plan，安全 owner 应在 dispatch 前核这条关系，并在真实 effect 提交时再次核验实际对象、目的地与授权是否仍一致；计划级 sensor 不能替执行器授予权限。

这增加计划视图、数据流关联、误拒绝与检查延迟，也会遇到动态计划和实际执行偏离；静态 allowlist、单步语义检查和最小权限在短且低风险的流程中仍有价值。[受限组合攻击实验](https://arxiv.org/html/2604.08608v1)只显示旧 LlamaGuard-7b/Koala 栈漏掉了作者构造的请求与子任务，而不证明任何单步守卫必然失效：原文的单步 LLM 分析仍能看见部分危险路由，较新的 LlamaGuard-3 也标出了部分子任务。其 14 个生成请求、8 个成功生成计划的 benign controls 与 prompted pipeline，不是对真实框架的完整集成验收；CIV 同时参与成功定义和防线评分，不能把在这组已定义成功案例上的全检出当作独立的通用安全保证。无法取得完整计划或准确关联数据来源时，应收窄 scope、隔离执行或转人工，而不是凭局部“与目标一致”直接放行。

<!-- source-family:SF-2026-ARXIV-2604-08608 -->


### 原文件L2855–2862
### Control Evaluation 要测试 Attacker 如何选择攻击时机

随机注入攻击可以估计 monitor 在给定分布上的识别能力，却会高估有耐心的 attacker 面前的安全性。对手会先为候选攻击估计被发现风险，再根据质量与审计预算决定是否提交；低频、高选择性攻击会让安全对 monitor false-positive rate 比平均 true-positive rate 更敏感。因此 red-team contract 必须同时冻结 attack generator、quality estimator、submission policy、attempt opportunity 和 audit budget，不能只报一个 monitor accuracy。

这种评测更接近自适应对手，但受 red-team 能力、攻击候选集和窄审计预算强烈影响，不是真实攻击概率上界。选择器未被充分激发时，应将结论降为已见攻击下界，并保留独立审计、最小权限和 safe-commit gate。<!-- source-family:SF-2026-ARXIV-2602-04930 -->

不可信writer与monitor即使没有共享显式secret，也可能通过同模型的代码风格与语义结构识别彼此输出，形成绕过外部honeypot的协同条件。Control evaluation因而要分别激发passive self-recognition、显式/隐式signal及组合策略，并让红队针对实际minify或summary协议再训练；“prompt时没识别到”和“去掉变量名”都不能自动上界该能力。Writer/monitor/jammer身份、训练人口、反馈可见性与审计机会集应作为同一个control artifact保存。<!-- source-family:SF-2026-ARXIV-2602-20628 -->


## Actual owner books/part-04-training-system/31-rlhf.md

### 原文件L680–688
### 异步 On-policy Distillation 需要 Sample Freshness

缓存 rollout 能复用昂贵采样并提高 trainer 利用率，在 policy 变化慢时是合理近似；长 horizon 或异步更新后，同一 buffer 同时包含 rollout drift 与 supervision drift，旧样本不再等价于当前 on-policy evidence。Runtime 因而要为样本绑定 behavior/teacher revision，并用 freshness score 决定接受、降权或丢弃，而不是只按到达顺序消费。

收益是允许有限异步而不把所有旧样本当作同质量监督；代价是版本状态、freshness estimator、样本浪费和估计偏差。漂移无法可靠估计时应缩短 buffer 或恢复同步生成。exact-v1 只在其披露的长程任务、模型、buffer 与 freshness controller 中验证该机制，不给出跨任务通用阈值，也不证明更高吞吐必然改善最终策略。

<!-- source-family:SF-2026-ARXIV-2605-17862 -->

## Human feedback 不等于统一人类价值

## Actual owner books/part-04-training-system/30-lora.md

### 原文件L191–195
但 nominal rank 只是参数化上限，optimizer 如何同时更新两个低秩因子会决定实际可用的 effective rank。若 A/B 的几何与初始化让更新方向长期退化，提高 rank 也不一定扩大有效子空间；反过来，耦合的谱更新可更接近目标 weight-space direction，却增加优化器假设、阻尼和稳定性成本。Adapter capacity 因而应同时记录 rank、初始化、optimizer transform 与实际更新谱，而不是只用 `r` 解释结果。

<!-- source-family:SF-2026-ARXIV-2609-12123 -->

更接近 weight-space direction 还可以改变梯度接口，而不先生成完整更新矩阵。对同一 linear batch，缓存输入 X 与输出梯度 S 后，完整梯度可按 SᵀX 的乘积接口求值；把当前低秩增量的完整一步近似投影回 rank-r 时，warm-start 的 proximal alternating update 可在变化后的因子上重新计算所需乘积，避免物化 dense G 和每步全矩阵 SVD。它不同于普通 autograd 只给旧因子的梯度，因而需要保存 X/S 并执行内循环；结构化对角预条件还只是完整 curvature 的近似。[必要机制与反侧](https://arxiv.org/html/2602.16456v1)的投影收敛定理只针对无 proximal 项、初子空间非零重叠及谱间隙条件，不认证实际阻尼或 stochastic 更新；更多内迭代也可能更差，额外缓存与乘积不能按参数量宣称免费。内存、噪声或任务收益不合算时，普通因子优化、原有受控谱更新和离线 rank 压缩继续成立，不把局部近似升级成全部 LoRA 训练的稳定性或速度保证。<!-- source-family:SF-2026-ARXIV-2602-16456 -->

### 原文件L203–207
多个 target modules 的容量还可以分成“共享更新方向”和“模块自己的组合系数”。普通 LoRA 为每个投影学习独立的左右因子，模块数增加时 trainable state 近似随模块数线性增长；若这些投影确实需要部分共同方向，一个替代分支让 m 个同形模块共享 p 对 d×r、r×d 的基，模块 j 只学习各自 r×r 的系数 Q_h^j，更新为 ΔW_j=Σ_h D_h Q_h^j U_h。忽略共同的其他参数，独立因子约需 2drm 个参数，共享分支约需 p(2dr+mr²)；只有 r 相对 d 足够小、共享基数量受控时才有节省，表达 rank 上界也受 pr 约束，不能把共享解释为免费保留所有独立模块容量。

这一选择仍改变 parameterization，而不改变 objective 或引入按输入选择专家的 router；训练完成后的固定线性增量可以 merge。共享全部因子与保留模块系数是不同约束，前者过强时会损害适配；用权重的 Frobenius 项代理不同基输出的 decorrelation，也不等于在真实输入分布上已正交，且正则计算有额外成本。受限 ViT/VTAB 对照支持这种共享与容量的取舍，但部分 baseline 来自不同配置或原报告，正则项计算下降不等端到端加速。模块需求异质、基共享不稳或原独立 LoRA 已满足发布预算时，保留独立因子与逐任务回归，不从较少 trainable parameters 推出统一质量或训练速度保证。<!-- source-family:SF-2026-ARXIV-2512-24603 -->

共享也可沿被选中的 FFN 行组织，而不为整个投影学习自由的两组低秩因子：冻结基座，用 harmful/benign activation 的线性 probe 提出 gate/up 的候选行，将其分组，再让同组行共享一个可训练线性增量；训练后把增量加回这些行，推理不再保留额外 adapter 分支。这改变的是更新支集与 tied parameterization，probe 权重只给关联性 proposal，不认证因果“安全神经元”。[受限安全适配对照](https://arxiv.org/html/2602.16835v1)对 activation 归一化及聚类上限的描述有冲突，因此不把其写成确定 recipe；对照数据/训练预算亦非全部匹配，部分通用能力退步，未测 white-box 攻击。行选择、分组、校准与训练成本仍须计入，固定增量可 fold 不意味着总训练免费或所有攻击被阻止；选定行遗漏、分组不稳或安全/效用回归时，保留普通 LoRA、全量适配与独立行为验收，而非凭小参数量发布安全保证。<!-- source-family:SF-2026-ARXIV-2602-16835 -->

### 原文件L213–231
- 其他模型特有 linear layers。

只适配 Q/V 与覆盖全部 Attention/MLP 会得到不同容量和 artifact shape。最优 rank 与位置依赖任务、数据、基座和预算，不能从 LoRA 名称推出。

Rank 也不等于任务“本质维度”的直接测量。训练成功只说明该配置足以形成某个有用 update，不证明所有任务更新都严格低秩。

当 supervision 本身存在分歧时，rank 验收还要区分“能否拟合一个多数标签”与“怎样对待一个有多种合理判断的样本”。保留每个 item 的标注分布、歧义切片与训练 loss 轨迹，才能观察更新容量是否选择性地降低明确样本的 loss，却提高争议样本对既定标签的 loss。这里 annotation entropy 是外部诊断，rank 是参数化配置，逐样本 loss 是对当前 objective 的测量：三者不能合并成“高 entropy 就是错误数据”或“提高 rank 必然恢复不确定性”。在四个 encoder、两个 decoder 和 NLI 的受限证据中，争议样本确有这种轨迹，但 FullFT 对照只覆盖 encoder；最多 100 个标注者给出的分布也不是所有部署任务的真值。

因此，增大 rank、改用 soft labels 或换 PEFT 只能成为待验的 proposal，不能由该相关性直接升级为修复。原实验中 soft-label 条件仍可出现 loss 上升，跨数据集关系变弱，noise injection 也未给出 rank 唯一因果。验收应同时保留逐 item 的目标、歧义与 held-out 行为；多数标签 loss 上升不单独证明模型功能退化。标签清楚、固定 shape 或现有行为已达标时，静态 rank 与原 SFT objective 仍然合理，监督分布的解释责任继续交给第 29 章与 Evaluation，而不是让 adapter 替标注者决定真值。

<!-- source-family:SF-2026-ARXIV-2604-16332 -->

静态 rank 在任务同质、kernel 依赖固定 shape 时最容易复现；输入难度差异很大时，它要么为简单样本持续支付最大容量，要么让复杂样本受限。条件容量分支可以让 router 从版本化 input feature 提出允许 rank，并在所有目标层一致截取 adapter 的前 `r` 个方向；但训练和推理必须复用同一 router、difficulty-label rule、rank set、alpha 与 target modules，不能训练时动态、部署时再凭经验固定。

rank policy 因而成为 adapter artifact identity 的一部分，也新增 router 误判、标签循环、dynamic-shape batching 碎片和更大发布矩阵。任务分布漂移、router 不稳定、延迟收益未证或静态 kernel 更重要时，固定 rank 仍是首选回退。`arXiv:2605.01959v1` 只在作者 Llama 3.2/Whisper 与 QA、数学、语音任务中验证质量和参数量；它没有披露生产 batch、硬件、端到端 latency 或 SLO，trainable parameters 减少不等于 serving cost 已下降。

<!-- source-family:SF-2026-ARXIV-2605-01959 -->

条件适配还可以改变权重本身，而不只截取固定 adapter 的 rank。静态 adapter 便于 merge、缓存和固定 shape 执行；若不同输入需要不同模型与不同增量，一个分支先由 router 选择基座，再用共享该 router 特征的 hypernetwork，按同一输入生成所选基座的 LoRA 权重。此时输入相同的 routing prompt 同时决定 architecture 和参数 proposal，不能把它解释为只选 rank 的容量策略；router、基座、hypernetwork 和生成 adapter 应共同定义执行身份，这是由接口推得的验收要求。按基座分 bucket 后的批量矩阵乘可以组织这些不同增量，却仍支付路由、权重生成、packing 和 batch 碎片成本。[受限两组件实验](https://arxiv.org/html/2601.05903v1)支持这种联合选择，但价格模型是模拟而非生产账单，也不证明全局最优；新输入、生成权重或成本回归未通过时，保留固定 adapter、已有模型路由或静态 rank。
