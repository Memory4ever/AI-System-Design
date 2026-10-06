# B12 — 六项最小必要原证与actual owner（本批安全终态）

2026-10-06 feb26_close_oct06（非原packet作者）定点复核：20751原§2.2/2.3/3.1–3.2、20791§III–V、20794§3.2/4.2/4.4及Table7、20796§III–V必要原HTML paragraph与实际Ch31 538–550、Ch28 1478–1490、Ch23 105–107、Ch29 854–858逐项对应。确认20751/20794/20796具体已有覆盖，20791仅报告；不授未经核验的完整理论证明、cosine最优selector或部署安全/性能保证。新复核未运行代码/实验，未新增Books。20759新发现阈值相似关系不自动传递，却被§4.3称为equivalence classes；保持原证，暂不以仅报告标签绕过此身份问题，待定点查实现/定义及root裁决。20770此前root复核保持有效。

20759当前中心D已独立原证/有限实现定点核并经root裁决隔离，原阈值/partition冲突和必要官方重开材料在README；上段“待定点/root裁决”是发现时点，不再是普通待办。20770保root已核终态。

## 2602.20751v1
https://arxiv.org/html/2602.20751v1；原HTML paragraph身份保留：

S2.SS2.SSS2.p1.2 | The first term is an empirical estimate of the verification gap in Eq. (3), favoring items that separate the reference answer from the current candidates; the second term is a verifiability regularizer that favors items yielding more stable judgments under \pi_{v} . If \pi_{v} produces scalar scores, \sigma(q_{t},r_{t}^{k}) can be the standard deviation of repeated evaluations of \pi_{v}(q_{t},o_{t},r_{t}^{k}) . If \pi_{v} produces binary judgments (e.g., 1 for satisfied and 0 for unsatisfied), this term can be omitted.

S2.SS2.SSS3.p2.1 | Each stored item keeps: (i) the criterion itself, (ii) an aggregated reward, and (iii) aggregated context and supporting evidence (e.g., queries, and optionally ground truth or feedback from the verifier). In our current implementation, the evidence is instantiated using queries only.

S2.SS3.p1.1 | The reward \alpha_{t}^{k} in Eq. (12) is defined relative to the candidate set used during memory tuning. If this set is weak or lacks diversity, tuning may overfit to separating o^{\star} from a narrow set of failure modes.

S3.SS1.p4.1 | Metrics. We report two metrics. (1) Preference accuracy. For each query q , we compare the verifier scores of the expert reference answer o^{\star} and a candidate answer o under each rubric item r . For item r , we assign a pairwise outcome of 1 if \pi_{v}(q,o^{\star},r)>\pi_{v}(q,o,r) , 0.5 if they are equal, and 0 otherwise. Preference accuracy is the weighted average of these pairwise outcomes over rubric items, using the rubric-item weights. (2) Pairwise win rate (vs. base). We sample answers from the GRPO-trained policy and the base model, and report the fraction of wins for the RL policy under an external judge that uses the reference answer as the gold standard. We use OpenAI o4-mini as the judge model; prompts are provided in Appendix A.

S3.SS2.p6.1 | Adversarial candidate refresh further improves performance over non-adversarial memory tuning (Table 1), supporting the hypothesis that refreshing the candidate pool helps expose rubric-specific blind spots that are not covered by the initial samples. This effect is especially pronounced on RaR-Medicine, while on GovReport the gain is smaller but still positive, suggesting diminishing returns when candidate diversity is already high or the quality dimensions are more diffuse.

## 2602.20759v1
2026-10-06 定点补核：§4.2–4.3的sim≥τ关系不自动传递，却直接取equivalence classes计唯一奖励；AppC pairwise去重未补运行时闭包/聚类定义。仅查当前官方仓库main 4ea283a19444059e7b5363cb64614bd281e43eef：op_reward_batch.py为格式/精确重复惩罚，reward_manager/batch.py消费外部uniq_rewards；未找到足以解除该中心身份冲突的定义，未宣称全仓复现或current main=exact-v1。root同意中心争议Disputed安全隔离，保作者有限多样性经验，不称整篇无效；重开须作者明确具有传递闭包的聚类/实现定义并绑定该实验版本，随后重核唯一奖励及消融。
https://arxiv.org/html/2602.20759v1；原HTML paragraph身份保留：

S4.SS2.p3.1 | To resolve the issue of many-to-one matching, we adopt Mutual-Best Greedy Matching (MBGM) that enforces strict one-to-one alignment. The algorithm introduces three key improvements: (1) Keyword masking: high-frequency tokens from the prompt are replaced with placeholders, reducing their influence on similarity scores and allowing the model to focus on more informative differences. (2) Mutual best matching: a pair (c_{i},r_{j}) is valid only if c_{i} is the top match for r_{j} and vice versa, i.e., s(c_{i},r_{j})=\max_{j}s(c_{i},r_{j}) and s(c_{i},r_{j})=\max_{i}s(c_{i},r_{j}) . (3) Thresholding and greedy removal: pairs are accepted only if s(c_{i},r_{j})\geq\tau . Once a valid pair is selected, both the candidate c_{i} and the reference r_{j} are removed from further consideration. This prevents re-use of references, guarantees one-to-one alignment, and repeats until no valid pair remains.

S4.SS3.p5.1 | Reward 2: Group Perspective Uniqueness. To encourage diversity within each OP window, we penalize redundancy among candidates. Let s_{kk^{\prime}}=\mathrm{sim}(c^{(k)},c^{(k^{\prime})}) and define k\underset{{\tau_{\mathrm{dup}}}}{\sim}k^{\prime} if s_{kk^{\prime}}\geq\tau_{\mathrm{dup}} . We use u(a) to denote the number of distinct clusters after partitioning C(a) into equivalence classes under \underset{{\tau_{\mathrm{dup}}}}{\sim} . The uniqueness ratio is computed as r_{\mathrm{uniq}}(a)=\tfrac{u(a)}{K(a)} . Thus higher values of R_{\mathrm{uniq}} indicate greater distinctness between the perspectives in an response a .

S5.SS2.SSS0.Px5.p3.1 | Ablation study on the uniqueness reward. Evaluating whether LLM responses exhibit strong OP performance requires considering two key criteria: (i) achieving high coverage with respect to the true human reference perspectives, and (ii) maintaining sufficient perspective diversity so that each generated viewpoint remains distinct, thereby broadening the overall perspective spectrum. In this study, we test the removal and modification of the uniqueness reward component and fine-tune Qwen2.5-3B-Instruct under this modified setup. As shown in Table 4, the results reveal a clear and stable trade-off between coverage and uniqueness: removing uniqueness entirely (1:0) largely preserves coverage but causes a substantial drop in uniqueness, while our chosen ratio (5:1) offers the best balance, maintaining high coverage and restoring strong uniqueness. Increasing the uniqueness weight (e.g., 3:1 or 1:1) yields only marginal uniqueness gains (about +1–2%) but leads to substantial coverage degradation, suggesting that overly strong uniqueness pressure pulls the model away from true human perspectives. This confirms that coverage should remain the dominant term, since Overton Pluralism centers on aligning with real human viewpoints, while uniqueness plays a secondary but necessary role in preventing redundancy. This clearly demonstrates the contribution of the uniqueness reward, showing that it effectively improves perspective diversity and underscores the necessity of explicitly encouraging uniqueness in reward design.

## 2602.20770v1
https://arxiv.org/html/2602.20770v1；原HTML paragraph身份保留：

2026-10-06 root非原作者定点复核：精确v1 §3.3/4.1–4.3/5.1–5.2及原paragraph记录实际核验；公开范围沿用同身份官方公开批次下界与登记上界，Submitted不是首次公开。2+1+2=5，标准审阅完成，Books已有覆盖。Ch66“Binary Verdict通过不等于语义忠实”及紧邻形式证明段实际区分execution verdict、原题语义、axiom与correspondence审计、人工规格/abstain；Ch65资源控制与Ch67观测的交接无owner冲突，不新增正文。

需要收窄的原主张：easy theorem可绕开原推理结构，未观察到困难题误报不证明零误报；interactive §3.3允许`sorry`，编译成功不能直接认证完整证明。§4.2的similar为150题、排除难形式化人口；§5.1 answer-only comparator与原proof验证端点不同，不能当同合同优胜。类型/库覆盖、lemma上下文、人工干预与脚本维护均有费用或误拒。只接受这些边界，不采用普遍precision/语义忠实保证，未运行artifact。此决定只关闭20770，不授B12其余五项或本日终态。

S3.SS3.p1.1 | The algorithm for both automatic and interactive modes consists of 6 steps: getting a specifically structured solution, analyzing its structure with the script, formalizing all "facts" and checking their evidence, formalizing all lemmas and checking the quality of the translation with the script, proving all lemmas and linking the whole proof. Figure 1 displays the scheme of the algorithm.

S4.SS1.p4.1 | At this point of development, we consider the solution to be well-explained iff each lemma is able to be proven with earlier context in automatic mode (or however the user decides in the interactive mode) and all the lemmas are able to be linked together either without any assistance or with the use of several scripts (for example, if the last lemma concludes not with the expected theorem statement, but the statement follows from that conclusion, we can implement the last lemma and check using Prover LLM whether that is true and finish the proof automatically. Thus, this solution is considered well-explained).

S4.SS1.p5.1 | It has been experimentally proven to be highly unlikely to encounter a False Positive in both modes, excluding the following scenario: sometimes the problem is too easy (for example, ’find the GCD of 3 numbers’), the Solver LLM becomes confused and is unable to provide the adequate structure for the solution, however, the theorem in Lean4 may be able to be proven even without the structure due to the optimization of the proof assistant. In other cases, either the solve_by_elim tactic will not work or the translated lemma will not be able to be proven. Cases where the wrong solution for a hard enough problem was able to be translated into a correct proof have not been noticed experimentally, not to mention that the translation is checked with the script in order to catch possible inaccuracies or hallucinations. To further minimize the probability of False Positives appearing, one can provide the correct formalization of the main theorem instead of the Translator LLM.

S5.SS1.p4.1 | After but still in the early stages in development, this pipeline was compared with the pipeline consisting of only Kimina-Autoformalizer + Prover with the latter having a natural language solution as a hint in the prompt (formalizing the problem statement using Kimina-Autoformalizer and giving the whole statement to Kimina-Prover rather than lemmas in our original pipeline). The goal of this pipeline was to check not solutions but answers. On easy, the results were relatively the same (at least 9 out of 10 problems were able to be solved each time), but on similar, the other pipeline was able to check on average 7 more answers. This does not diminish our results, as the goals of the pipelines are different and the amount of true negatives is not the same, although this does show that the structures developed in relation to Neural Theorem Proving are suited better for the purposes of that area.

## 2602.20791v1
https://arxiv.org/html/2602.20791v1；原HTML paragraph身份保留：

S3.Thmtheorem1.p1.1 | For t\in T , element of \boldsymbol{X}_{t} follows i.i.d standard Gaussian. The noise \boldsymbol{\epsilon}_{t} is independently drawn from N(0,\sigma_{t}^{2}I_{n_{t}}) , where \sigma_{t}\geq 0 denotes noise level.

S4.p3.1 | Increasing the rehearsal size enhances the model’s adaptability under underparameterization, whereas it can be detrimental under overparameterization. Specifically, when n+s>p+1 in Equation (6), \mathbb{E}[\mathcal{A}(\widehat{\boldsymbol{w}}_{T})] decreases as s increases, indicating that more playback contributes to better adaptation. When slightly overparameterized in Equation (5), we have p\approx n+s and thus \lambda\approx 0 . At this point, Term A1 and the denominator in Term a_{noise} approach zero when tasks are similar, and thus a_{noise} dominates and causes \mathbb{E}[\mathcal{A}(\widehat{\boldsymbol{w}}_{T})] to be increasing w.r.t. s . When heavily overparameterized in Equation (5), Term A1 is close to zero, and thus \mathbb{E}[\mathcal{A}(\widehat{\boldsymbol{w}}_{T})] decreases as s increases when \sigma is low. Intuitively, when tasks are similar, the model can leverage rehearsal more effectively, leading to improvements in performance on current task.

S5.p3.1 | The impact of rehearsal size on memory errors is illustrated in Figures 6(e)–(f) and Figure 7. Specifically, we split the MNIST and CIFAR-10 into 2 tasks, each comprising 5 classes. The partitioning schemes for CIFAR-100 and Tiny-ImageNet follows the previous settings. In the figures, the memory errors first decrease and then increase as the rehearsal size grows, with this effect being more pronounced when sharing category is two. These observations suggest that larger rehearsal do not necessarily lead to better memorability, and that further gains become marginal once rehearsal reaches a certain level.

## 2602.20794v1
https://arxiv.org/html/2602.20794v1；原HTML paragraph身份保留：

S3.SS2.p1.1 | To fully harness the cross-view geometric modeling capability of VGGT and effectively empower the VLM to meet the stringent accuracy and robustness demands of complex autonomous driving scenarios, we design a Hierarchical Adaptive Injection Mechanism. Specifically, this mechanism employs the frozen VGGT model to perform cross-view 3D geometric modeling on an input set of N surround-view images I=\{{I_{c}}\}_{c=1}^{C} , from which the visual features extracted before the DPT module [39] are utilized as the 3D features. Notably, we retain the original camera and registration embeddings within the 3D features V^{3d}\in{\mathbb{R}^{B\times C\times{N_{1}}\times{D_{1}}}} , as these embeddings also encode critical multi-view information that is indispensable for accurate scene geometry representation. Furthermore, our CVGE allows the 2D visual embeddings V_{0}^{2d} to query the 3D representations V^{3d} , thereby capturing the necessary cross-view geometric information.

S3.SS2.p2.3 | where M_{id}^{img}\in{\{0,1\}^{B\times(C\cdot{N_{2}}+N_{s}+N_{t})}} denotes the image ID mask, with values set to 1 for image token N_{2} positions and 0 otherwise (i.e., special tokens N_{s} and text tokens N_{t} ). Next, V_{i}^{2d} and V^{3d} are fed into the proposed CVGE to obtain geometry-enhanced 3D visual embeddings \{{V_{i}^{3d}\in{\mathbb{R}^{B\times C\cdot{N_{2}}\times{D_{2}}}}}\}_{i=1}^{n} . Considering the differences in embedding representations and their sensitivity to 3D information across network layers, the CVGE adopts a modular design with consistent structure but independent parameters across layers, enabling the 2D visual features at each layer to adaptively learn and extract the geometric information most relevant to that layer.

S4.SS4.p3.1 | Effectiveness of Key Components. Tab. 7 presents the ablation analysis of the key components in VGGDrive. Under the integration scheme and adaptive injection mechanism of VGGDrive, ID-2 refers to the ablation of MHCA, where addition is used as a replacement for MHCA; ID-3 refers to the scenario where the multi-layer CVGE shares its structure and parameters. ID-4 corresponds to removing the residual setting during LLM injection (i.e., Eq. 6: \{{x_{i}=X_{i}^{{}^{\prime}}}\}_{i=1}^{n} ), and ID-5 corresponds to using only single-stage full fine-tuning of all model parameters.

## 2602.20796v1
https://arxiv.org/html/2602.20796v1；原HTML paragraph身份保留：

S3.p2.1 | To achieve the above objectives, the parameter space is split into shared and task-specific parts, with task-specific parts quantified to minimize catastrophic forgetting. The optimized model is denoted as y_{(k)}=X_{(k)}^{\top}u_{(k)}+Z_{(k)}^{\top}q_{(k)}+\varepsilon_{(k)} , where X_{(k)}\in\mathbb{R}^{p\times n_{(k)}} represents the features associated with the shared parameters u_{(k)}\in\mathbb{R}^{p} , and Z_{(k)}\in\mathbb{R}^{p_{(k)}\times n_{(k)}} denotes features associated with the task-specific parameters q_{(k)}\in\mathbb{R}^{p_{(k)}} . Performance on task k is measured by squared loss, following the metric from [66, 62, 22].

S4.p8.4 | The complete version are provided in Appendix A.3. Theorem IV.4 shows that the average forgetting with respect to the trainable parameter p_{(2)} reaches an extremum when \xi>\eta>0 , beyond which further increases in p_{(2)} yield diminishing returns. In particular, a plateau occurs when \|q_{(2)}-q_{(1)}\| is small. The following lemma describes average forgetting under initialized training.

S5.SS1.p2.1 | In Algorithm 1, when task is introduced, the relationship between the current task and previous tasks is first quantified by examining the consistency of gradient directions with respect to prior tasks. Specifically, the metric s_{t} is computed, where g_{t} denotes the parameter gradient under the training loss, and MetricFunction(g_{t},\;g_{t-1}) represents the metric function, which defaults to cosine similarity. Tasks with scores below threshold are considered unrelated and are assigned more modules to enhance task-specific learning.

S5.SS3.p3.1 | As shown in the second row of Table I, Frozen Training demonstrates a stronger ability to resist forgetting than Initialized Training on Correlated Split CIFAR-100. On Corrupted Split CUB-200, however, the advantage of Frozen Training gradually diminishes as task dissimilarity increases. Adaptive Training more effectively integrates the strengths of both approaches, achieving a 6.43% and 4.09% improvement in average accuracy, along with a 2.42% and 0.45% reduction in forgetting rate on Correlated Split CIFAR-100 and Corrupted Split CUB-200, respectively. In summary, these results highlight the substantial potential of Adaptive Training for enhancing performance in continual learning.

### 原txt 20751 L1488–1520
Rubric source
RaR-Medicine
GovReport
Original Rubrics
49.6
—
Few-shot Rubrics
51.2
48.9
𝐒𝐢𝐛𝐲𝐥𝐒𝐞𝐧𝐬𝐞
\bf{SibylSense}
-Base
56.0
52.6
𝐒𝐢𝐛𝐲𝐥𝐒𝐞𝐧𝐬𝐞
\bf{SibylSense}
-Adv
60.6
52.9
Table 1:
Pairwise win rate (%, higher is better) of the GRPO-trained policy against the base model under an external judge. Rewards derived from
𝐒𝐢𝐛𝐲𝐥𝐒𝐞𝐧𝐬𝐞
\bf{SibylSense}
-generated rubrics improve downstream policy learning over static rubric baselines, and adversarial candidate refresh (
𝐒𝐢𝐛𝐲𝐥𝐒𝐞𝐧𝐬𝐞
\bf{SibylSense}
-Adv) provides an additional gain over non-adversarial memory tuning (
𝐒𝐢𝐛𝐲𝐥𝐒𝐞𝐧𝐬𝐞
\bf{SibylSense}
-Base).
Better rubrics translate to better downstream RL, and adversarial candidate refresh provides additional gains.
The downstream win-rate results in Table
1

### 原txt 20794 L2284–2345
Table 7
:
Ablation Study of the Main Components of VGGDrive.
ID
Methods
NAVSIM
NuInstruct
EP↑
PDMS↑
MAP↑
BLEU↑
Avg↑
Time (s)↓
1
Baseline
81.00
86.04
6.15
75.75
31.32
0.81
2
w/o MHCA
82.05
87.79
27.43
77.89
39.29
1.00
3
Share CVGE
82.48
88.05
30.85
79.55
40.95
0.96
4
w/o Residual
82.32
87.86
27.98
78.31
40.02
1.03
5
One-stage SFT
82.83
88.62
36.19
80.75
42.05
1.04
6
OURS
82.92
88.76
37.49
81.13
42.98
1.04
Effectiveness of Key Components.

## Actual owner books/part-04-training-system/31-rlhf.md

### 原文件L540–545
这种分账增加 on-policy 采样、likelihood 和独立 outcome 成本；它不是鼓励故意错奖的配方。[原始研究](https://arxiv.org/pdf/2604.25872v1)的停滞定理依赖线性 softmax、正交特征与 exact-gradient flow，正内积特征还可改变结论方向；四个小 policy 上 HAcc 与后训收益的相关仍弱、部分为负，主实验所谓真值又是另一 RM 的代理而非人类效用。无法取得独立 outcome 或分布不稳定时，pairwise ranking 仍是廉价筛选，只能报告该偏好集上的拟合，不能取得安全或真实效用 authority。<!-- source-family:SF-2026-ARXIV-2604-25872 -->

固定 scalar 或 rubric 还会在 policy 分布改变后失效。把 criteria 表为版本化 Reward DAG，允许设计器依据 on-policy response 与 node-level trace 提出节点/边更新，可以定位 coverage 与 reliability 的变化；但设计器不是 truth owner，自演化也会制造新的 reward hacking。任何 graph mutation 都必须经过 held-out、人类或确定性 verifier 的 promotion gate，并保留旧 rubric 作为可回滚基线。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08703:start -->
开放式任务还可能要求 reward contract 随失败证据演进。冻结 Reward Model 在目标稳定时最易校准；当视觉编辑等任务不断暴露新的判据和工具缺口时，orchestrator 可以依据失败轨迹提出 skill/tool library 与验证 rubric 的版本变更，但 subagent 只执行冻结版本，独立 validation Gate 才拥有提交权。这样把“自我改进”拆成 proposal、execution 和 promotion 三种责任，避免同一个模型既生成规则又宣布自己通过。

### 原文件L214–218
#### Reward Basis、Jury 与时间权重是三种不同状态

直接为每个人群训练独立 reward model，能保留差异却难以扩展；把所有偏好平均又会抹掉少数群体。一个中间分支先学习低秩 reward basis，再由显式规则筛选 jury membership，并随时间更新各群体权重与策略。Basis owner 只表示可复用偏好方向，governance owner 决定谁进入 jury，deployment policy 持有当前权重；三者不能由同一聚合器静默改写。

这种分解提高可追踪性，却引入 basis 误设、代表性偏差、时间漂移与治理成本。群体少且目标稳定时，独立模型或固定多目标 reward 仍可用；无法证明代表性时，应报告分组结果并保留人工决策。现有 exact-v1 只支持作者的偏好数据与民主过滤设定，不建立普遍社会合法性。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01642 -->

## Actual owner books/part-06-ai-infrastructure/66-evaluation-system.md

### 原文件L3557–3557
安全评估同样不能只靠固定采样。search-based route 可以冻结 deployment config，在 likelihood budget 内复用 prefix cache、做 chunked search，并报告找到的 failure mass 与尚未覆盖的 residual mass。它擅长发现低概率但结构化的失败，代价是搜索策略本身会改变被观察分布；因此必须与随机 sampling 并列，不能把“没有搜到”解释为“没有风险”。

### 原文件L1791–1795

<!-- semantic-body-binding:SF-2026-ARXIV-2609-11085:start -->
编译、solver 或单元测试给出的 binary verdict 是必要 execution gate，但任何只看 verdict 的 evaluator，都无法区分与参考实现语义等价的答案和“恰好保持同一通过/失败结果”的不忠实答案。需要在离线评估中构造 same-verdict matched pairs：正例满足参考语义，负例由双向 executable check 或反例搜索确认 verdict 相同但语义不等价。reference、solver、约束编码与判定预算属于 privileged evaluation state，不应在部署时泄露给被评系统。

可由这些配对数据训练一个部署时不读取 reference 的 generative verifier，但它只是一枚 learned sensor：负责 gate、候选选择或 trace 采样 proposal，不获得 semantic authority。训练标识重叠、solver 只能覆盖形式化子集、参考约束不完备或不可满足时的 vacuous equivalence，都会让高准确率失去含义；`Best-of-N` 的采样收益也必须与 verifier gate、selection 和 feedback 的增量分开报告。

## Actual owner books/part-04-training-system/28-pretraining.md

### 原文件L1478–1489
### Continual Pretraining 可以减少 Replay，但不能宣称消除遗忘

replay buffer 通过重看旧样本维持能力，直观且可验收，却增加数据存储、权限和重复计算。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-15053:start -->
TFGN 提供的是无 replay、无 task ID/phase boundary 的 internal overlay：forward read 保持 dense，task-driven update signal
被结构性地导向不同 trainable subspaces。它试图在网络内部减少新任务更新对旧能力的干扰，但 overlay 只拥有 update
proposal；最终 checkpoint 仍需分别验收 acquisition、retention 与 transfer。代价是额外 capacity/compute、内部状态身份
和无法独立检查的实现边界，论文还明确说明关键 lever/specification 受 NDA 限制，因此不能把它改写成已公开的“新旧任务
梯度分量分解器”。旧数据可合法保存、内部机制不可审计或 retention 回归时，replay、regularization 与独立 adapter 仍是
更稳妥的 fallback。现有证据只覆盖作者任务与实验设置。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-15053:end -->

## Actual owner books/part-03-multimodal-world-models/23-multimodal-representation.md

### 原文件L105–107
如果 consumer 不是一个分类 readout，而是语言 decoder 的多个层，访问哪层视觉表示还须与“在哪个语言层、更新哪些 token 位置”共同定义。一个可比较的分支保留原 projector，为不同视觉 producer 层配置低秩适配，再在指定 decoder 层由视觉特征与当前 hidden state 的摘要生成门控权重；按该接口的约定，残差更新发生在 visual-token positions，不把任意文本位置改成直接视觉 cross-attention。它将 producer 层选择与 consumer 层/位置耦合，而不是仅把多层 summary 融合后送给唯一分类头；门控权重也不证明浅层必负责纹理、深层必负责推理。<!-- source-family:SF-2026-ARXIV-2601-10710 -->

这条分支增加中间特征驻留、逐层适配、门控计算与监督训练成本，不能从少量新增参数推导端到端 SLO。[受限跨层注入对照](https://arxiv.org/html/2601.10710v1)的 0.5B、半量指令数据消融中，仅增加多层投影收益很小，结合门控的局部结果更好；完整 projector 调优却以更大参数容量获得更高分，不能把全部差异归因接口。注入密度也不单调：中等密度可弱于稀疏配置。于是要同时版本化 producer 层、projector、consumer 层、位置 mask 和训练预算，并分别验收任务质量与执行成本；任务只需末层语义、训练或驻留预算不足时，保留原末层 projector，分类任务也仍可采用前述多层 summary readout。

## Actual owner books/part-04-training-system/29-sft.md

### 原文件L854–858
把 fine-tuning regime 固定后比较 continual-learning 方法，在参数预算、更新深度和任务顺序稳定时最容易复算；但 full fine-tuning、只更新上层、adapter 或其他 PEFT 并不是同一优化问题。它们把梯度投影到不同 trainable subspace，因而同时改变新任务拟合、旧能力保持和可恢复的 update state。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-21927:start -->
所以 continual SFT 的 EvalSpec 必须把 trainable parameter set、更新深度、optimizer state 与 task order 写进 adaptation identity；方法排名若只在一个 regime 下成立，不能外推成算法本身的稳定优劣。更小的 subspace 可降低状态与遗忘面，却可能缺少目标任务所需自由度；更大的 subspace 提高可塑性，也扩大回退和旧能力损伤风险。论文只在其 task-incremental 模型与 benchmark 中展示 regime-dependent 结果，不能证明某种深度普遍最优。目标变化需要广泛表征重写时 full tuning 仍合理，数据窄、回滚与多租户 adapter 更重要时 PEFT 仍合理。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-21927:end -->
