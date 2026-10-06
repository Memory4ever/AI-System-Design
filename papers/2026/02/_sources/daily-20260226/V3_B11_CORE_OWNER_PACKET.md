# B11 — 必要原证与 actual owner（3项，未授终态）

## 2602.20732v1
https://arxiv.org/html/2602.20732v1；原HTML paragraph机械摘段：

Relying solely on partial context selection involves inherent risks, as retrieving incorrect or irrelevant context can significantly degrade generation performance.
To mitigate this, CHESS incorporates a Quality-Aware Backtracking mechanism that initiates context reconstruction strictly when generation quality deteriorates.
Specifically, CHESS monitors real-time generation dynamics via two complementary uncertainty metrics: average Entropy ( \bar{H}_{p} ), which serves as a proxy for the model’s lack of confidence, and Varentropy ( \operatorname{Var}(H)_{p} ), which captures the temporal instability often characteristic of hallucination loops (Kuhn et al., 2023).

Our system manages the KV cache at the granularity of a page, serving as the atomic unit for memory allocation.
Chunks and Grids are logical views as they restructure access patterns without physically duplicating the underlying tensor data.
This design maintains three distinct structural perspectives (Grid, Chunk, Page) over the same memory footprint, achieving a zero-copy implementation that incurs negligible memory overhead.

To maximize GPU utilization and minimize kernel launch overhead, we vectorize the similarity computation across all hierarchy levels (Algorithm 1).
Instead of sequentially iterating through Grids, Chunks, and Pages, we coalesce their semantic vectors into a unified tensor  \mathbf{V}_{all}\in\mathbb{R}^{N_{total}\times D}  (Line 2), where  N_{total}  sums the counts of all hierarchy nodes and  D  denotes the feature dimension.
Utilization of the single query anchor  \mathbf{v}_{anchor}  enables us to compute similarity scores for the entire hierarchy via a single GEMM operation:  \mathbf{S}_{all}=\mathbf{v}_{anchor}\cdot\mathbf{V}_{all}^{\top}  (Line 3).
The subsequent filtering logic is implemented as a vectorized dependency check.
Specifically, a Chunk is selected only if its similarity score satisfies the threshold and its parent Grid is active, a condition enforced via hierarchical boolean masking (Lines 10 – 13).
This design effectively replaces expensive control-flow divergence with efficient tensor operations.

Our system configuration relies on several key hyperparameters governing memory structure and sparsity levels.
We standardize the Page size to 32 across all experiments.
To control retention rates, we evaluate multiple configurations for Grid, Chunk, and Page ratios.
Regarding uncertainty metrics, we perform offline calibration using the LongBenchV2 dataset (Bai et al., 2025).
Specifically, we calculate the empirical distribution of entropy and varentropy, adopting the 99th percentile values as the cutoff thresholds to prune high-uncertainty outliers.
Figure 4 illustrates the distribution and threshold.

We evaluate the efficiency of our dynamic mechanism by comparing it against a static triggering configuration.
To ensure a rigorous evaluation, we configured the baseline to reconstruct the context every 6 pages—a frequency significantly higher than our dynamic approach (averaging  \sim 10 pages).
Despite the baseline benefiting from more frequent updates, the results in Figure 9 demonstrate that our dynamic construction consistently yields superior performance across various budget ratios.

## 2602.20739v1
https://arxiv.org/html/2602.20739v1；原HTML paragraph机械摘段：

Concretely, each rollout is evaluated using a combination of answer accuracy and tool usage. After a rollout is completed, we verify the correctness of the final answer, yielding an accuracy reward  R_{\text{acc}}\in\{0,1\} . In addition, we compute an accumulative tool reward proportional to the number of tool calls, given by  0.1\cdot n_{\text{tc}} , where  n_{\text{tc}}  denotes the total number of tool calls during the rollout. This accumulative tool reward is added to the final reward only when the answer is correct, ensuring that tool usage is encouraged without rewarding unproductive or incorrect tool calls.

Finally, even among valid and correct rollouts, reward shaping can introduce subtle optimization issues. In particular, when multiple correct trajectories exist within a group but differ in tool-call counts, group-level normalization may assign negative advantages to correct but more concise solutions, suppressing useful behaviors during training.

To address these challenges, we adopt an oversampling, filtering, and ranking framework for rollout generation. Specifically, we first oversample rollouts, then apply online filtering to remove groups with zero reward variance and rollouts with broken agent–environment interaction. Among the remaining candidates, we rank rollout groups by group-level reward standard deviation, which serves as a proxy for sample difficulty (Jiang et al., 2024; Zhu et al., 2025), and retain the top-ranked groups for training. This strategy prioritizes moderately difficult rollouts that provide informative learning signals, while also substantially reducing the prevalence of correct samples with negative advantages, resulting in more stable and efficient agentic RL (Sec. 4.3). We refer to this strategy as Standard Deviation Sorting.

Both PyVision -Image and PyVision -Video are trained for 700 RL steps using the same hyperparameters: oversampling batch size 32, training batch size 16, group size 8, and learning rate  1\times 10^{-6}  on 8 H100 GPUs.

Quantitatively, Fig. 4 compares the average of visual tokens consumed per sample on VSI-Bench across PyVision -Video, Qwen2.5-VL-7B, Video-R1 (Feng et al., 2025), and SpaceR (Ouyang et al., 2025). PyVision -Video uses approximately 5K visual tokens per sample on average, achieving a performance of 44.0%. In contrast, Qwen2.5-VL-7B attains its best performance (38.0%) when sampling at 1.0 FPS, at the cost of approximately 45K visual tokens per sample. Video-R1 and SpaceR reduce token usage to around 25K per sample, with SpaceR achieving comparable performance (45.6%) to PyVision -Video. Overall, PyVision -Video achieves the most favorable trade-off between visual token efficiency and reasoning performance on VSI-Bench, demonstrating that agentic, on-demand frame selection can substantially reduce context length without sacrificing accuracy.
Overall, PyVision -Video achieves the most favorable trade-off between visual token efficiency and reasoning performance, demonstrating that agentic, on-demand frame selection can substantially reduce context length without sacrificing accuracy.

Next, we study the effect of the accumulative tool reward. In the baseline, we apply an accumulative tool reward with a coefficient of 0.1 during RL training ( Eq. 1). To ablate its effect, we rerun training with the coefficient set to 0. Removing the accumulative tool reward leads to a noticeable reduction in tool usage during training, as illustrated in Fig. 7. In Fig. 5, the model without the accumulative tool reward achieves slightly better performance in the early stage of RL training. However, as training continues to beyond 500 steps, its performance falls behind the baseline. This indicates that while the accumulative tool reward may slow early optimization, it plays a crucial role in enabling stronger long-horizon reasoning and improved final performance.

Finally, we analyze standard deviation sorting and normalization. Removing standard deviation sorting during RL training degrades performance in the early stages, as shown in Fig. 5, indicating its importance for stabilizing optimization when rewards are noisy. Meanwhile, retaining the common standard deviation normalization in the advantage computation leads to persistent performance fluctuations as training progresses, suggesting that it introduces excessive variance into the learning dynamics and hampers convergence.

## 2602.20743v1
https://arxiv.org/html/2602.20743v1；原HTML paragraph机械摘段：

If computational budget remains, the algorithm transitions to a refinement phase that aims to escape local optima and achieving finer-grained control over the privacy–utility trade-off. This phase extends standard GEPA with two novel mechanisms.

A rich feedback function  \mu_{\text{rich}}  is derived from the task-specific metric definitions by decomposing the aggregate score  \mu . In addition to scalar values,  \mu_{\text{rich}}  may include natural-language explanations or evaluator reasoning traces that provide interpretable, structured feedback to the proposer agent. This feedback function is generated once per task by a separate LLM (referred to as the rich feedback agent in Figure 1), ensuring consistency and avoiding manual, subjective feedback design11
                1
                
                
                
              In practice, we assign the rich feedback agent a code-generation task using the implementation of  \mu  in order to obtain the corresponding implementation of  \mu_{rich} . More information in Appendix D..

To improve exploration under the remaining budget, we evaluate candidate prompts over sampled validation subsets  D^{\prime}_{\text{valid}}\subset D_{\text{valid}} . Sampling follows a round-robin strategy prioritizing under-evaluated examples, balancing computational efficiency with coverage diversity. This reduces the budget consumption during evaluation while mitigating overfitting. Final model selection is performed using the full validation set to ensure fair comparison.

Third, although a key contribution of our framework is enabling anonymization with locally deployable open-source models, the evaluation pipeline still relies on closed-source LLMs for certain privacy and utility metrics. This reliance is partially mitigated by the small number of annotated examples required during optimization, which limits the amount of sensitive data that must leave the local boundary. However, determining which anonymized text is itself safe to share with external evaluators remains and is not fully resolved in this work.

Figure 4 ablates the main components of our GEPA-based optimizer by comparing: (i) our full two-stage GEPA pipeline (warm-start + refinement), (ii) a warm-start-only variant using simple scalar feedback (GEPA Simple Feedback), (iii) a refinement-only variant driven by rich structured feedback (GEPA Rich Feedback), and (iv) the state-of-the-art prompt optimizer MIPROv2 Opsahl-Ong et al. (2024). All methods are run under the same rollout budget and evaluated using the same task score as in the main paper. We report learning curves on two representative tasks/backbones: SynthPAI with Gemma-3-27B-it (top) and TAB with Mistral-Small-3.2-24B (bottom).

We report approximate API costs to facilitate reproducibility and cost-aware deployment decisions. For our framework, running the full optimization pipeline locally with open-source models (Mistral-Small, Gemma-3, or Qwen3) incurs costs only for the external evaluation backbone. Using Gemini-2.5-flash for privacy and utility evaluation during optimization and final testing results in approximately $1 per task per model, covering the 1,500 rollout budget plus validation and test set evaluations. In contrast, the GPT-5-based comparison methods require significantly higher expenditure due to the cost of closed-source inference. Running a single GPT-5-based agent across all test examples costs approximately $8 per task. These estimates highlight a practical advantage of our approach by shifting the computational burden to locally deployed open-source models and using affordable API-based evaluation only for metric computation. Moreover, even when local GPU resources are unavailable, outsourcing inference for open-source models via trustworthy providers incurs only minimal additional costs due to the competitive pricing of mid-sized models at the time of writing ( <\$0.10  per task).

### 20732 原txt L1226–1254
𝐒
a
​
l
​
l
=
𝐯
a
​
n
​
c
​
h
​
o
​
r
⋅
𝐕
a
​
l
​
l
⊤
\mathbf{S}_{all}=\mathbf{v}_{anchor}\cdot\mathbf{V}_{all}^{\top}
(Line 3).

### 20732 原txt L1327–1394
100%
30.2
33.9
28.0
38.3
24.2
28.7
H2O (Best)
20%
34.0
40.1
30.2
41.7
28.8
31.5
KeyDiff (Best)
8192 toks
29.2
33.3
26.7
30.6
26.5
32.4
SnapKV (Best)
4096 toks
30.2
34.9
27.3
34.4
24.2
35.2
Quest (Best)
2048 toks
32.0
34.9
30.2
40.0
25.6
31.5
CHESS (Conservative)
73%
30.4
34.9
27.7
36.1
26.0
29.6
CHESS (Moderate)
40%
32.2
35.4
30.2
41.7
24.7
31.5
CHESS (Aggressive)
1%
33.2
38.0
30.2
40.0
27.4
33.3
Hardware and software environment.
All experiments were conducted on a single node with four H20 GPUs, using Python 3.12.3, PyTorch 2.5.1, and CUDA 12.4.
Baselines.
We compare our method against
Full-KV

### 20739 原txt L774–812
,
t
=
R
⁡
(
x
,
y
i
)
−
mean
⁡
(
{
R
⁡
(
x
,
y
i
)
}
i
=
1
G
)
.
\widehat{A}_{i,t}=R(x,y_{i})-\mathrm{mean}\left(\{R(x,y_{i})\}_{i=1}^{G}\right).
(2)
where
R
⁡
(
x
,

### 20743 原txt L739–765
|
D
train
|
=
|
D
valid
|
=
111
|D_{\text{train}}|=|D_{\text{valid}}|=111
), reserving all remaining examples exclusively for testing. We configure the evolutionary optimization with a maximum rollout budget of
B
=
1500
B=1500
LLM forward passes, an early-stop patience of
n
=
5
n=5
iterations and set the adaptive validation sampling ratio to
α
=
0.3
\alpha=0.3

### 20743 原txt L1562–1593
MedQA
Qwen3-30B-A3B
Seed Prompt
64.0/100
12.6/92.4
36.2/54.0
82.3/72.1
3.52/58.6
Optimized Prompt
65.5/100
22.5/94.4
92.3/56.2
98.0/79.3
24.6/45.9
Qwen-2.5-7b
Seed Prompt
41.2/97.3
5.88/91.5
34.3/55.3
79.7/87.3
5.18/47.1
Optimized Prompt
47.1/98.0
17.6/86.0
90.6/53.2
88.4/79.2
7.29/41.2
Table 4:
Performance of Qwen-2.5-7b compared to Qwen3-30B-A3B and their seed prompt version (encoded as
privacy/utility
).
Task

## Actual owner books/part-05-inference-system/45-why-kv-cache-speeds-up.md

### 原文件L188–198
把 ranked evidence 全部序列化进 prompt、随后 dense 读取完整 KV，保留了最简单的逻辑语义。若 retrieval 或 graph prior 已经足够稳定，可以把它编译成 versioned access-plan IR：逻辑 prompt 仍保持不变，executor 只在 proposal path gather 计划区域，verification 或不确定时回退 full context。这样获得的不是“相关 token 天然正确”，而是受约束的 physical-read optimization。

Access plan 必须绑定 model、prompt / tokenization、KV layout、knowledge revision 与 compiler version。收益来自减少 HBM traffic，代价是 plan staleness、irregular gather、漏掉因果依赖和 fallback 成本；短 Context、访问稠密或 gather kernel 不成熟时，dense FullKV 仍更合理。第 76 章拥有 relevance 与 provenance，本章拥有 plan 到 physical KV read 的执行接口，第 49 章拥有 kernel realization。

当选择器自身扫描完整 head 的成本已经很高，可在校准集上衡量 RoPE 耦合维度对与完整 query–key 排名的一致性，保留低维频率子空间先提出 token 索引，再 gather 选中 row，以完整维度计算最终 attention。子空间分数只拥有 ranking proposal，不能替代 attention weights，也不能拆散 RoPE 维度对；跨层/head 可共用索引字典，但不意味着各项使用相同索引。纯计算变体仍驻留完整 KV，分层内存变体则在 GPU 保留 dominant Key 部分、在 CPU 保存其余 Key 与 Value，选择后才补给所需 row，两者不可用同一容量口径比较。Cache manager 还须验证 row/head、pair、校准配置与布局身份；校准、selector、gather/传输和误选都会付费。[受限频率选择对照](https://arxiv.org/html/2602.03152v1)不证明 exact attention 或完整质量等价，短序列、相关性漂移、误选或搬运成本过高时，应回退 dense FullKV。<!-- source-family:SF-2026-ARXIV-2602-03152 -->

选择还可以跨层分工，而不是每个 head 都重扫完整序列。一条条件分支让部分 head 做 dense attention，用其 attention map 选出 token 索引并交给下一层同一 head index；稀疏 head 只读取继承集合，继续向后传递而不刷新，首层则全部 dense 以初始化集合。这里减少的是完整 KV 中的读取与计算，不是删除未选 KV 的容量；继承索引也不证明下一层 query 仍有同样相关性。训练用 HardKuma 随机变量混合 dense/sparse 两张 map 并蒸馏 teacher logits，部署再按期望阈值固定角色，期望 L0 约束不等于每次精确满足 head 预算。Head/layer、索引 revision、预算与 KV row 身份须一起校验；dense selector、离线角色训练、gather 与误选均付费。[受限长上下文对照](https://arxiv.org/html/2602.04541v1)中更稀疏仍可能损害质量，部分 head 配置未快于 dense kernel；不能从单段 decode 推 TTFT 或生产 SLO。跨层相关性不足、继承集合陈旧或收益不可摊销时，应增加刷新或回退 dense FullKV。<!-- source-family:SF-2026-ARXIV-2602-04541 -->

一种更具体的实现把语义选择编译成 `Grid → Chunk → Page` 的层级访问计划：较粗表示先缩小候选区域，较细选择再落到与 physical KV page 对齐的索引，executor 直接 gather 已驻留 page，而不是重新拼接一份逻辑 Context。这样减少的是 selection metadata、重复搬运与 attention read，不是原始事实本身；selector 只拥有 page proposal，cache manager 仍验证 page generation、offset、residency 和 fallback。层级池化或 coarse miss 会永久跳过细粒度证据，page 对齐也可能保留无关 token；短 Context、选择稠密或 zero-copy path 不可用时，dense read 仍是正确基线。

<!-- SF-2026-ARXIV-2602-20732 -->

## Actual owner books/part-04-training-system/31-rlhf.md

### 原文件L949–955
### Post-training 必须把故障、探索与 Credit 组织成闭环

强化微调失败时，单看最终 reward 无法区分 environment error、rollout hang、verifier failure、policy regression 或数据污染。可靠 runtime 应采集可观察 fault fingerprint，先诊断故障 owner，再执行重试、隔离、降级或样本剔除，并把处置结果写回下一轮训练。自动 remediation 减少人工停机，却可能把诊断误差放大为数据偏差；无法归因时应冻结更新并保留原始 trajectory。

在线 preference learning 的 exploration 也不能只依赖当前 policy 的瞬时不确定性。历史样本覆盖、observer disagreement 与旧策略误差可以提供更稳定的 prior，再用当前观测修正 exploration budget。这样能把查询集中到高信息区域，但会引入历史分布滞后；发生 policy shift 时必须重置或降权旧不确定性，保留均匀探索作为覆盖 fallback。

tool-integrated trajectory 的 terminal reward 往往把多个动作混成一个结果。step-level credit 应绑定可观察 effect、状态变化与 verifier receipt，再决定哪些 turn 进入更新。没有外部 verifier 时，一条弱监督分支从某个 turn state 采样多条 future answers，按语义答案聚类，再把各 cluster 的 probability mass 与可靠性估计组成 outcome-potential distribution；相邻 turn 的 potential delta 只表示“后续答案分布是否向更可靠的 cluster 移动”，不是该动作的真实因果 credit。Cluster 边界、future-sampling budget 和 reliability estimator 都会改变信号，开放答案或同义归并不稳时，应回退 terminal outcome 或可执行 subgoal verifier。

## Actual owner books/part-04-training-system/33-grpo.md

### 原文件L104–132

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

### 原文件L2172–2178
重复执行多轮工具环境十分昂贵时，缓存成功轨迹或工具结果可以作为训练期的受限 experience service；但 cache hit 不是一次真实 environment transition。精确命中、模糊命中和缺失命中应成为不同 observation tier，缓存生成版本与当前 policy 必须进入 trajectory identity，来自缓存的 tool-return tokens 也必须从 policy-action mask 中排除。否则训练会把旧环境反馈、检索近似或缓存文本误当成当前策略产生的动作。

缓存能降低 rollout 成本，却会改变 policy 所见的环境分布，并引入 staleness、模糊匹配误归因和 reward scale 漂移。训练应分别报告各 cache tier 的命中率、真实性能与无缓存回放结果；高风险、有副作用或强时效工具仍应 live execute。单一小模型、特定工具任务上的作者结果只说明这种分层缓存 recipe 可行，不证明缓存轨迹可替代真实交互或保持严格 on-policy。

随机工具返回还有比陈旧更隐蔽的边界：一次返回在同组多个 rollout 中共享，即使每条轨迹的条件 reward 分布正确，也改变了组内 reward 的**联合分布**。Group-normalized advantage 会再用这一组样本估计均值与尺度；因此缓存可能改变更新方向，而不只是增大方差。训练期复用须把独立随机源数量、cache sharing scope 和 group membership 一起记录，并与独立执行对照；可用仅中心化的 estimator 作受限控制，但它也不自动恢复完整 GRPO 的 clipping、KL 和 optimizer 语义。这个反例来自两动作、一步 on-policy 的精确有限求和及脚本化缓存审计，不是完整大模型训练测量，也不否定确定性工具结果的正确复用。<!-- source-family:SF-2026-ARXIV-2609-26866 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-14179 -->

### 原文件L2314–2316

### Tool-use RL 的训练对象包含环境编排


## Actual owner books/part-06-ai-infrastructure/72-security.md

### 原文件L253–260
Learned anonymization policy 进一步把 detector、rewrite 与 utility 放进一个经验优化回路：给定某类 attacker、
downstream task 和文本分布，选择删改哪些 span 以形成 privacy/utility Pareto。它可以比固定 redact rule 更适应
上下文，却不能提供 Differential Privacy 的跨攻击者数学保证。其 identity 至少包含 attacker model、utility
metric、task/data distribution、rewrite policy、threshold 和 human escalation。Attacker、语言或用途变化后，
旧 operating point 可能失效；生成式 rewrite 还可能改变事实或制造新敏感线索。确定性规则在强格式、法规字段
或低延迟路径中继续成立。Adaptive Text Anonymization 的实验只支持其所测 contract，不应被写成 DP 或
compliance guarantee。

