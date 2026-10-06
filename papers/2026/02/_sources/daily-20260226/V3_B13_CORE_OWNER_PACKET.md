# B13 — 六项最小必要原证与actual owner（本批安全终态）

2026-10-06 feb26_close_oct06非原packet作者定点读必要原方法/关键反侧与actual owner：20800/20813/20878具体已有覆盖，协议冲突/conditional-turn/judge与goldpath代理反侧保留；20799跨文件packing、20816rank-tail质量、20880category guidance确有窄差额。root授三处窄锁后实际写入Ch27 788–790、Ch29 250–252、Ch24 238–240，并由root非写入者顺读实际两段/完整邻接/自身末注POST通过；未运行artifact/复现，非日级验收。

## 2602.20799v1
https://arxiv.org/html/2602.20799v1；原HTML paragraph身份保留：

S2.SS2.SSS1.p1.1 | We extract only file nodes and inter-file dependency relations from the code graph, resulting in a directed acyclic subgraph, which will be used to construct the pretraining code corpus. Unlike previous works~(guo2024deepseekcoder), which process project source code by taking a topological ordering for each connected component in the subgraph and then splitting it according to the context window limit to obtain the final file-level dependency data, our approach addresses a key limitation of this strategy. Files that are actually dependent on each other are not necessarily adjacent in topological order. Therefore, when a topological sequence is split due to the context window length limit, some files with dependency relations may not appear in the same training sample, leading to an insufficient description of how these files collaborate within the same codebase.

S2.SS2.SSS1.p2.1 | To address this issue, we perform a depth-first traversal over the directed acyclic subgraph as illustrated in Algorithm 1. We start from nodes with zero in-degree, i.e., files that are not depended on by any other files, and find all depth-first paths in the subgraph. This strategy ensures that any pair of files with a true dependency relationship appears as adjacent nodes in at least one traversal path. For each path, we generate training samples using a sliding-window strategy. Specifically, we fix the left pointer at the beginning of the traversal path and move the right pointer incrementally, until the total length of all file content within the current sequence exceeds the model’s context limit. The concatenated content of the files in the current sequence constructs a CPT training sample. Then, we update the left point location by one step and find the proper right pointer in the same way. We repeat such a process for all traversal paths and construct the dependency-preserving CPT data.

S2.SS3.SSS1.p5.1 | Post Filtering. Directly assessing the correctness of a model’s reasoning trace is challenging, as the underlying reasoning is often lengthy, information-dense, and difficult to evaluate in isolation. Therefore, we simplify the evaluation by judging the correctness of the model’s output and using it as a proxy for the correctness of the associated reasoning trace. Specifically, we employ a modern LLM to determine whether the output produced by the reference model is semantically consistent with the constructed ground-truth response and filter out the samples judged as inconsistent. The validated reasoning trace is then embedded into the original data instances, completing the construction of the single-hop relation reasoning data training set.

S4.SS4.p3.1 | Training Setup. Due to variations in programming languages and codebases scales, the number of epochs used in the dependency-preserving CPT stage differs across codebases. For C++ codebases, the CPT stage is conducted for 1 epoch on sqlgen and for 2 epochs on reaction and hexi. For the Python codebase leann, CPT is performed for 1 epoch. In the graph-grounded SFT stage, all codebases are trained for 3 epochs. For other hyperparameters, both CPT and SFT stages employ full-parameter fine-tuning with a learning rate of $5.0e^-5$, a warmup ratio of 0.1, a context window length of 32,768 tokens, and a gradient accumulation step of 1. All experiments are conducted on 32 NVIDIA H20 GPUs. The complete configuration and training details are available on GitHub.

## 2602.20800v1
https://arxiv.org/html/2602.20800v1；原HTML paragraph身份保留：

S3.SS1.p10.1 | Judge A is never used for training, early stopping, hyperparameter tuning, prompt tuning, threshold selection, or any form of model selection. Formally, we enforce strict role separation: y_{B} is used only to train/tune f_{\theta} , while all reported metrics are computed only from y_{A} on held-out queries. This mitigates preference leakage and self-preference bias, where evaluators disproportionately favour outputs from their own model family (Li et al., 2025; Koo et al., 2024; Chen et al., 2024). We enforce this by instantiating Judge A and Judge B using different model families (e.g., Yi-34 vs. Llama-3). We employ a hierarchical rubric where Score 1 indicates irrelevant content, Score 3 indicates generic thematic alignment without cultural markers, and Score 5 requires deep integration of specific cultural customs and worldview.

S4.SS1.p4.1 | The intersection filtering removes missing/invalid judge outputs and ensures that every method ranks the same candidates per query, which is critical for fair within-query comparisons under judge-based evaluation (Voorhees and Tice, 2000; Smucker et al., 2007). On the processed NGR-33k dataset ( N=33{,}052 ), the unified intersection pool (y_{A}\cap y_{B}) retains 17,965 stories across 343 queries. Across eligible queries, intersection-pool sizes satisfy \min/\mathrm{median}/\mathrm{mean}/\max=10/52/52.38/106 , and all reported results use cutoff k{=}5 and evaluate only queries with |\mathcal{S}_{q}^{\cap}|\geq k .

S4.SS2.p4.1 | 3. Dense Retrieval Baseline: We evaluate the BGE-M3 (Distilled) model described in Section 3. As noted, this model is used off-the-shelf and is not fine-tuned on our dataset; it serves as a strong dense baseline.

S5.p1.1 | Methodological Rigour—Evaluating without Circularity: Our framework addresses the systemic self-preference bias and preference leakage inherent in single-judge evaluations (Koo et al., 2024; Chen et al., 2024; Li et al., 2025). We rigorously enforce estimator separation ( J_{A}\neq J_{B} ) to prevent the model from overfitting to the idiosyncrasies of a specific evaluator. We acknowledge, however, that “leakage-free” refers to the experimental framework, not the pre-training distribution. Since Yi-1.5 and LLaMA-3 likely share training data (e.g., CommonCrawl), they inevitably share latent societal priors. Critically, our results on the OOD control dataset (SSGEN) show that this shared background is insufficient to produce agreement on its own ( \rho\approx 0.04 ). High agreement only emerges when the underlying narrative contains valid normative structures (Moral Stories, \rho\approx 0.65 ). This confirms that while the judges share a “worldview”, our framework successfully isolates the learning signal from the evaluation signal, preventing the circular inflation typical of self-rewarding loops.

## 2602.20813v1
https://arxiv.org/html/2602.20813v1；原HTML paragraph身份保留：

S4.SS0.SSS0.Px1.p3.1 | Many scenarios include trigger conditions that determine whether follow-up turns execute. For example, an escalation turn that only fires if the model shows initial vulnerability. A referee model evaluates whether triggers are met, enabling efficient testing of escalation resistance without unnecessary turns when models resist immediately.

S5.SS0.SSS0.Px2.p2.1 | When categorising scores into pass ( \geq 4 ), borderline (3), and fail ( \leq 2 ), human-AI category agreement was 70%. Notably, human variance differed by category: failures showed tight consensus (std = 0.33), passes showed moderate variance (std = 0.67), while borderline cases showed highest disagreement (std = 1.01) which mirrored the inherent ambiguity of edge cases.

S5.SS0.SSS0.Px3.p2.1 | Agreement on criteria selection was more moderate than score agreement. For pass criteria, the AI judge achieved F1 = 0.69 relative to human majority selections (precision 0.76, recall 0.63). For fail criteria, agreement was substantially lower (F1 = 0.11). This pattern suggests that while humans and the AI judge often reach similar verdicts, they oftentimes cite different reasons.

S7.SS0.SSS0.Px3.p1.1 | Firstly, our factor-analytic conclusions are constrained by sample size: with 24 models and 37 behaviours, we cannot compute standard sampling adequacy tests, and the factor structure may not be stable. While the convergence of multiple indicators suggests the structure is meaningful, replication with larger model samples is essential. Secondly, while scenarios draw from multiple sources using automated generation via Bloom (Gupta et al., 2025) and adversarial probing via Petri (Fronsdal et al., 2025), with all undergoing human review, the corpus may still contain systematic gaps; coverage is reasonably balanced across categories (75–239 scenarios each), but this process may miss failure modes that emerge only in deployment or that require domain expertise we lack. Thirdly, although we validate LLM judges against human annotations and demonstrate high levels of agreement, LLM judges may share systematic blind spots—particularly for subtle misalignment that frontier models also fail to recognise (Wataoka et al., 2025, Chen et al., 2024). Fourthly, several behaviours show near-ceiling performance, limiting discriminative power; this may reflect genuine alignment progress or insufficient scenario difficulty. Fifthly, our scenarios are English-language and reflect predominantly Western normative assumptions; alignment norms vary across cultures (Awad et al., 2018), and the structure we observe may not generalise. Finally, our findings are correlational: we observe that alignment behaviours covary across models, but this could reflect either a genuine unified construct or an artifact of developers applying similar training interventions across objectives.

## 2602.20816v1
https://arxiv.org/html/2602.20816v1；原HTML paragraph身份保留：

S2.p3.1 | Observe that if the probability distribution is skewed towards the modes, i.e., top- K token probabilities and has a thin tail, \sum_{k=1}^{K}\accentset{\ast}{p}^{T}_{k} is very high, and the contribution of \mathcal{D}_{KL_{2}} to the KL divergence is very low. To mitigate this, we can multiply the second term by a hyperparameter \beta , yielding the two-term loss \mathcal{D}_{KL_{1}}+\beta\alpha^{T}_{k}\mathcal{D}_{KL_{2}} . In this form, we recover the exact KL Divergence for \beta=1 , and the loss requires \beta>1 . Setting the value of \beta becomes quite difficult, and the loss does not converge. We overcome this issue by sequence-level normalization. For the stochastic form of training, we use a mini-batch of sequences, and every token in a sequence has a different value of \{p^{T}_{1},p^{T}_{2}\dots,p^{T}_{v}\} . If a sequence has N tokens, we can normalize \beta by the mean of \alpha_{K}^{T} across all the tokens. Indexing the tokens with t\in[N] , the final loss for a token t in the sequence takes the form,

S2.p5.1 | Our method is motivated by decoupled knowledge distillation (DKD; Zhao et al. (2022)), which was proposed for supervised classification with labeled datasets and improves accuracy on ImageNet and CIFAR-100. In contrast, language model pretraining distillation operates on unlabeled corpora, so the original DKD formulation is not well-suited to this setting. While one might treat the next token as a target label, this creates a fundamental mismatch: in classification, the target class is, by definition, correct. However, since most LMs’ pretraining corpora are undisclosed and we distill using a generic corpus, the teacher’s most probable token (i.e., \arg\max_{v\in\mathcal{V}}p_{v}^{T} ) may differ from the ground-truth next token. When we study this discrepancy on the validation set of our dataset (see Section 3.2), we observe a mismatch rate ranging from 39\% to 46\% , depending on the teacher, with larger teachers having lower mismatch rates (Figure 2). This mismatch creates conflicting signals between the dataset labels and teacher predictions. We therefore introduce TAD: a rank-based Top- K vs. tail decoupling using a probability-mass-normalized tail KL divergence that preserves the teacher’s distributional information. TAD is not a variant of DKD: DKD’s decoupling is label-anchored (target vs. non-target), while TAD’s is rank-anchored (Top- K vs. tail) and label-free. Two examples with identical values of p^{S} and p^{T} yield the same TAD losses, but their DKD losses can be different if their labels differ.

S3.SS2.SSS2.p3.1 | The students receive no fine-tuning after distillation, and we evaluate them on the same few-shot tasks as before. MiniPLM did not outperform Vanilla KD, and on Phi-2 it was worse (Table 4). Adding the cosine loss on hidden states improved both Vanilla KD and TAD. As formulated, MiniPLM (a data-selection method) does not incorporate such internal-state losses, which reduces its competitiveness relative to Section 3.2.1. To ensure parity, we also report reverse KL (RKL) with the same cosine loss on the hidden states (Table 4). RKL is slightly better than vanilla KD but remains inferior to TAD. For TAD, performance improved up to K=5 or 10 , beyond which we observed no significant gains (Table 4).

S3.SS2.SSS4.p1.1 | Across experiments with Qwen1.5-1.8B (Section 3.2.1) and with the larger teacher models, we observe that performance peaks at K=5 or 10 and then declines. In natural language, the next-token probabilities are approximately Zipfian, and the teacher’s tail mass \alpha^{T}_{K}(t)=1-\sum_{k=1}^{K}\accentset{\ast}{p}^{T}_{k}(t) decay sharply beyond K\gtrsim 5\text{\textendash}10 (see Figure 2). Even after normalizing the tail term in \mathcal{L}_{DIV} by the sequence mean \bar{\alpha}_{K}^{T}=\frac{1}{N}\sum_{t=1}^{N}\alpha_{K}^{T}(t) of the tail probability mass, many low-entropy tokens still satisfy \alpha_{K}^{T}(t)\to 0 as K grows. Instead, the contribution of high-entropy (noisier) tokens increases with K . Consequently, we observe no material gains beyond K\approx 5\text{\textendash}10 .

A2.p2.1 | The experiments are divided into two major parts: pretraining distillation from scratch, and continued pretraining. For pretraining distillation from scratch, we distilled the Qwen1.5, Phi2, and Qwen2.5 models on a single H100 GPU for a week, whereas we used 2 H100 GPUs for distilling the Gemma2-9B model. We used flash attention (Dao et al., 2022) whenever possible to speed up the computation, except for Gemma2. We used Adam optimizer (Kingma and Ba, 2014) with a learning rate of \eta=1e-4 and a weight decay of \lambda_{d}=0.1 for all the experiments. We used a batch size of 128 for all the experiments.

## 2602.20878v1
https://arxiv.org/html/2602.20878v1；原HTML paragraph身份保留：

S3.p5.1 | 4) Minimal Causal Pruning. To obtain a minimal sufficient causal graph, we iteratively remove nodes and edges that are not required to derive the correct answer. An LLM, given only the graph (without the image), evaluates whether the remaining structure is sufficient to answer the question. Components that do not affect answer validity are pruned. The final VLCG therefore represents the smallest set of causally relevant elements supporting the ground-truth answer.

S5.p5.1 | Causal Inference (CI). CI evaluates whether the identified attributes are coherently composed into a valid reasoning chain that supports the final prediction. Specifically, we use an LLM-based alignment protocol where a separate evaluator model is prompted to compare: (i) the generated reasoning, and (ii) the gold causal assumptions encoded in the VLCG. The evaluator assesses whether the reasoning: (a) links relevant attributes to the outcome, (b) maintains logical consistency, and (c) avoids unsupported assumptions. The CI score reflects agreement between generated reasoning and the structured causal path, averaged across test instances.

S5.T2.3.1 | Metric Zero-shot Standard ICL VLCG (Best) Causal Attribution (CA) 0.458 0.455 0.488 Causal Inference (CI) 0.652 0.654 0.690 VQA Accuracy 0.763 0.763 0.768 BLEU (reasoning) 0.164 0.163 0.177 ROUGE (reasoning) 0.266 0.264 0.273

## 2602.20880v1
https://arxiv.org/html/2602.20880v1；原HTML paragraph身份保留：

S3.SS3.p3.1 | Safety Averaging Degradation. This degradation arises from the attenuation effect observed when multiple harmful categories are aggregated. When heterogeneous safety directions are combined, their opposing components partially cancel each other, weakening the net safety signal and leaving certain harmful semantics under-constrained. As shown in Table 1, this leads to significantly weaker suppression compared with well-aligned single-category guidance. When harmful directions are aggregated across categories (“all”) or jointly applied (“hate+sexual”), the resulting attack success rates remain higher (48.8% and 5.8%) than those achieved by single-category guidance (3.2%). Such results demonstrate that the attenuation phenomena observed earlier directly cause safety weakening during aggregation, showing that combining more harmful categories does not guarantee stronger protection but may instead dilute safety control.

S4.SS1.p5.1 | To determine which harmful category is most relevant to the current prompt semantic state of the generation process, we compute the cosine similarity between each harmful guidance g_{i} and the prompt guidance g_{p} :

S4.SS1.p5.2 | A larger cosine similarity (smaller angle) indicates stronger alignment between harmful and prompt guidance, meaning that this harmful category is more likely to influence the current generative trajectory. We therefore identify the harmful category with the highest cosine similarity as the dominant harmful direction:

S4.SS1.p6.1 | STEP 3: Alignment Category Application. Once the dominant harmful category is identified, we apply safety steering along the harmful direction associated with this category. This correction is seamlessly integrated into the SLD procedure, retaining all remaining SLD mechanisms and hyperparameters exactly as originally designed. By replacing the original multi-category harmful direction with the most aligned harmful direction, CASG+SLD ensures that the latent update remains both targeted and fully compatible with the standard SLD framework.

S5.SS1.SSS0.Px1.p3.1 | Evaluation Metrics. Following SLD [38], we use Q16 [39] and NudeNet [29] for safety assessment33 3 Some methods focus solely on nudity mitigation and report results using NudeNet. We include Q16 because it can detect multiple types of harmful content, enabling a more comprehensive safety evaluation.. An image is labeled harmful if either classifier flags it. For benign prompts, CLIP score [15] and FID [16] measure semantic alignment and image fidelity.

A4.I1.i2.p1.1 | For latent-space guidance, CASG+SLD exhibits a linear growth with respect to the number of predefined harmful categories k , adding approximately 1 second per additional category per sample. In our experiments, we follow the original SLD setting and adopt 7 predefined harmful categories, where the inference time reaches 10.2 seconds per sample, which is 2.58 times of SLD.

### 20799 exact-v1 PDF p14 Table4, extraction L743–750
Table 4. Ablation Study on base model Qwen3-14B-Base. CUD: codebase utilization data, SHRRD: single-hop
relation reasoning data, CARD: compositional API reasoning data
Tech. sqlgen reaction Hexi LEANNcompilation@1 pass@1compilation@1 pass@1compilation@1 pass@1pass@1
UCD-Training 29.3% 22.2% 42.0% 29.1% 54.2% 47.2% 55.2%w/o CUD 23.8% (↓5.5) 21.7% (↓0.5)33.1% (↓8.9) 21.6% (↓7.5)53.4% (↓0.8) 46.1% (↓1.1)49.8% (↓5.4)w/o SHRRD 27.5% (↓1.8) 21.3% (↓0.9)33.0% (↓9.0) 19.8% (↓9.3)50.6% (↓3.6) 44.2% (↓3.0)54.6% (↓0.6)w/o CARD 12.7% (↓16.6) 9.8% (↓12.4)37.8% (↓4.2) 24.2% (↓4.9)34.4% (↓19.8) 30.8% (↓16.4)25.5% (↓29.7)with only general data0.5% (↓28.8) 0.5% (↓21.7)0.5% (↓41.5) 0.3% (↓28.8)28.8% (↓25.4) 24.4% (↓22.8)10.5% (↓44.7)w/o filter of problem and referenceanswers of CARD 18.2% (↓11.1) 15.2% (↓7.0)40.0% (↓2.0) 27.2% (↓1.9)52.5% (↓1.7) 44.7% (↓2.5)39.1% (↓16.1)
w/o filter of reasoningcontent of CARD 25.3% (↓4.0) 19.0% (↓3.2)42.0% (+0.0) 28.0% (↓1.1)55.9% (↑1.7) 46.7% (↓0.5)50.2% (↓5.0)
we independently remove:w/o filter of problem and reference answers, which eliminates filtering at
the question–answer pair level andw/o filter of reasoning content, which removes filtering applied
to reasoning traces and final responses.

### 20816 原txt L656–704
\displaystyle\mathcal{L}_{DIV}(t;\mathcal{P}^{T},\mathcal{P}^{S})
=
D
K
​
L
1
​
(
t
)
\displaystyle={D}_{KL_{1}}(t)
+
β
1
N
​
∑
t
=
1
N
α
k
T
​
(
t
)
​
α
k
T
​
(
t
)
​
D
K
​
L
2
​
(
t
)
\displaystyle+\frac{\beta}{\frac{1}{N}\sum_{t=1}^{N}\alpha^{T}_{k}(t)}\alpha^{T}_{k}(t){D}_{KL_{2}}(t)
(3)

### 20816 原txt L1973–2102
↓
\downarrow
1.2B
CLM (no KD)
36.2
53.0
26.4
46.6
25.9
61.6
35.7
58.9
43.0
−
-
1.9
1.49
CLM (Mat.)
38.1
53.9
27.6
47.6
26.6
62.8
36.5
60.4
44.2
−
-
0.7
1.41
Vanilla KD
38.0
53.4
26.8
50.6
27.4
64.0
38.8
60.4
44.9
1.42
MiniPLM
37.3
53.4
29.2
49.4
25.3
64.7
38.6
61.4
44.9
+
0.0
+0.0
1.45
RKL
38.9
53.7
28.2
50.7
27.6
63.8
39.0
61.4
45.4
+
0.6
+0.6
1.99
TAD (
K
=
1
K=1
)
39.9
54.3
27.5
52.1
27.8
64.9
39.7
60.9
45.9
+
+
1.0
1.29
TAD (
K
=
5
K=5
)
39.9
53.5
27.9
53.4
27.9
64.9
39.2
61.0
46.0
+
+
1.1
1.30
TAD (
K
=
10
K=10
)
40.6
54.5
29.6
52.0
28.4
64.8
39.3
61.5
46.3
+
+
1.6
1.32
TAD (
K
=

## Actual owner books/part-04-training-system/27-data.md

### 原文件L327–330
### Synthetic data：从“先生成再打分”到 Specification Compilation

最直接的 synthetic-data pipeline 是让模型生成任务、回答或 Agent trajectory，再由另一个 model judge
过滤。它便宜、覆盖开放语义，在 verifier 难以形式化的任务中仍然合理；但 generator 和 judge 可能共享

### 原文件L788–790
将多个短 documents pack 到同一长度 `T`，可以减少 padding 并提高有效 token ratio。但系统必须明确 document boundary、EOS、position ids、Attention mask 和 loss mask。错误 packing 可能让本不相关文档互相读取，或让 label 跨边界预测。

从 token stream 扫描 EOS 推定 document boundary，在每个文档都保留 terminator 时是简单而合理的旧路径；若上游 truncate 连同尾部 EOS 一起丢弃，下一文档便可能被误认为同一长文档。随后按最大文档长度再截断，不仅改变跨文档 attention，还可能使下一文档完全不进入训练。[Olmo-core v3.0.0 的数据路径纠错](https://github.com/allenai/Olmo-core/releases/tag/v3.0.0)因此提供显式采用 source metadata boundaries 的分支，并让 block-diagonal mask 的 document lengths 来自同一边界源；它保留本地 token 扫描默认值，不表示所有使用者已切换。语料存在、总 token 数相同和 attention mask shape 正确，都不能代替实际进入 instances 的文档及有效 token 检查。<!-- source-family:SF-2026-OLMOCORE-300 -->

## Actual owner books/part-06-ai-infrastructure/66-evaluation-system.md

### 原文件L128–130
对会读写评测仓库的 Agent，目标写清楚还不够：公开验证集的标签若与代码一同暴露，逐轮反馈又只强调公开分数，Agent 便可能复制标签、据此训练或调参，让分数上升而独立隐藏集不改善。公开集和即时反馈在开发阶段仍有价值，但 EvalSpec 此时必须同时冻结**可见文件与标签权限、反馈措辞和轮数、执行与停止规则**；轨迹审计分别查直接复制、训练、调参和校准，发布判断交给真正独立的 holdout。把公开文件称作“held-out”，或者仅靠提示禁止捷径，都不能代替运行时隔离与独立验收。<!-- source-family:SF-2026-ARXIV-2604-20200 -->

隔离会降低调试便利，并增加隐藏评价、访问控制和轨迹审计成本；低风险探索可保留可见公开集，但其分数只能用于开发反馈，不能越权取得 release 证据。受限 coding-agent 实验观察到这类 public/private 分离，并在小规模提示消融中看到行为缓解；它没有证明提示能可靠阻断泄漏，也不能推算生产环境中的发生率。这个边界把上面的 proxy 问题落到**评价通道由谁控制、Agent 实际看见什么**，再进入下文对任务难度和分布的条件化测量。

### 原文件L293–299
Judge 自偏好审计要区分三个测量对象：高 contrast 答案的判别能力、近等质答案中的 self-PIR，以及第三方 judge 对这些答案的 Null-PIR。前者测试能否辨别质量，后两者控制答案来源和评判者身份；差分只是在协议内分解观测偏好，并不自动识别纯粹的 self 因果效应。双 LLM 的 quality proxy 也不是独立 gold。<!-- source-family:SF-2026-ARXIV-2604-22891 -->

外部 source label 也须与内容质量分开：保持内容不变，只交换媒体、品牌、URL 或资历标签，并控制展示顺序，再观察模型实际任务选择；直接询问“偏好哪个来源”的自述不能替代这一 indirect 行为测量。[SourcePreferences 的有限对照](https://arxiv.org/html/2602.15456v1#S3)支持部分选择依赖 attribution，但不表示所有来源依赖都错误：医学资历可能与任务可信性有关，真实新闻的不同正文又不能当纯标签干预；seller 提示改善价格/速度选择的反侧也说明偏好并非不可改变。EvalSpec 因而要分别冻结内容、标签、顺序、任务目标和模型版本，支付配对调用与人工内容核验成本；标签和内容无法解耦时只报告联合效应，开放来源质量仍保留独立评价，不能从来源敏感性推定训练因果或规范真值。<!-- source-family:SF-2026-ARXIV-2602-15456 -->

这增加答案配对、第三方调用和质量匹配成本，proxy 错误、风格差异与候选生成方式仍会混入比较。近等质控制不可信或新域未校准时，应补人工 anchor、报告三个量的不确定性，或保留无排序结论；不能由高 contrast 判别好就批准低差额排名。

把每次 LLM judge 比较硬化成确定 win/loss，在 judge 存在 position bias、自偏好或 intransitivity 时会把局部错误放大到 Elo 排名。局部层应先把 score difference 校准为 soft win probability，再进入 Bradley–Terry/Elo；全局层再用 held-out judge–human residual 构造 conformal rating interval。Judge 只拥有比较 evidence，release owner 仍需根据 interval overlap 与风险决定是否排序或保持并列。

### 原文件L998–1000
由此得到的工程取舍是：发布判断须保留各分支失败、工具与输入条件以及汇总方式；图像处理、外部工具运行、私有 holdout 维护和 judge 核验都会增加成本。单一用途、输入来源固定时，简单固定基准仍是合理基线；跨用途条件无法对齐时，应收窄发布声明，而非用总平均认证全部能力。这是从测量协议推得的设计要求，不声称 FACTS 已实现完整的平台治理，也不沿用其排行榜或后来技术稿的阈值作为生产保证。下一步若要定位搜索分支内部的失败，才需要进一步拆解检索、重排、上下文组装与生成。

### RAG 端到端评估必须保留阶段级归因

### 原文件L3671–3673
长上下文回答可能最终正确，却引用了无关或错误 evidence path；也可能轨迹合理但终局合成失败。评测应分别保存 claim、自然 evidence trail、检索/工具事件与最终 verdict，让 scorer 只拥有对应层的判断权。这样提高诊断性，却增加标注和 trace 成本；低风险短答案仍可用 final-only baseline，关键结论则不能从答案正确反推证据链正确。

开放文本轨迹还可以先把公开参考 rationale 拆成 atomic units，再比较候选理由覆盖了哪些参考单元；但这先定义了一份新的测量人口，而不是发现模型内部真正使用的推理。拆分规则、人工筛选、参考集合、匹配器及其 reuse/阈值约束、输出与理由预算都应进入 scorer identity，不能让更长的理由或同一候选片段反复匹配制造无条件 coverage。[必要方法与反侧](https://arxiv.org/html/2602.04649v1)支持这一参考对齐分支；公开文本的一致性、与另一个 judge 的相关性不等人类事实真值或内部 faithfulness，匹配公式与提示实现尚未一致的子命题也不能用来认证奖励机制。工程上应定点人工核对拆分与匹配、同时保留 final verdict 和不匹配样本，这是测量验收推导而非作者已实现完整 guard。标注、匹配调用及更长 trace 均有成本；参考不可信、划分或匹配不稳定时，回退 final-only、可执行 oracle 或人工 evidence 审计，不让参考覆盖率替过程正确性自证。<!-- source-family:SF-2026-ARXIV-2602-04649 -->

## Actual owner books/part-04-training-system/29-sft.md

### 原文件L246–250
### Distillation 不是“Teacher 越强越好”

当任务给出可信的已知标签 `y`，teacher 的错误 top-1 也可以作为 target 修正的局部门槛，而不必用 temperature 同时改变所有 dark-class odds。设其概率为 `p`、错误 top-1 为 `k*≠y`，选择 `δ=min(η p_k*, m(p_k*−p_y))`，其中 `0<η<1`、`0<m≤1`，只从 `k*` 减去 δ 并向 `y` 加回，其他坐标不变；直接代数保证非负、总质量与未涉及类别之间的 odds，不保证任意 entropy/semantic-neighborhood 约束、wrong-mass 阈值或正确性。它新增 gold 标签、门槛及目标版本的依赖；[原始有界机制与反侧](https://arxiv.org/html/2602.12687v1)只在受测分类 teacher/student 中提供局部支持，AGNews 有退步，soft entropy loss 也不是 hard bounds。原稿 A.1 把含 entropy 上界的可行集视为凸集，其一般 unique projection 推出仍有争议，不能借给这条质量转移分支。标签不可靠、任务不满足单标签坐标或 held-out utility 退化时，保留原 teacher target、普通温度蒸馏或原 student。<!-- source-family:SF-2026-ARXIV-2602-12687 -->

跨 tokenizer 蒸馏还要先解决监督坐标：同一文本在两端具有不同词表和序列长度，不能按 token 索引直接比较概率。一条分支先用可学习 attention/projector 将两端 hidden states 映入对方输出空间，再分别以 student entropy、投影 teacher 的最大概率及 teacher entropy 提议 token 权重，并以 Soft-DTW 为序列匹配增加单调路径约束；attention entropy 还能提议软 band 宽度，但软惩罚不等于跳过完整 cost matrix，也不认证语义一一对应。词表、prefix、双空间映射、权重与路径共同定义监督，entropy/max-probability 只是代理，不证明学生已懂或教师正确。[受限跨分词对照](https://arxiv.org/html/2602.21669v1)中，band/gate 部分任务退步，强化 DSKD 基线也高于原完整方案；同 batch 的训练步从 .35s/26.38GB 到 .45s/29.92GB，额外 teacher forward、projector warm-up、路径求值与校准均付费，generation seeds 不等于重复训练。映射失配、教师错误被放大或 held-out 行为回归时，保留 sequence-level／统一蒸馏与原 student，不能用更低对齐损失代替任务验收。<!-- source-family:SF-2026-ARXIV-2602-21669 -->

## Actual owner books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

### 原文件L232–236
guidance 的两次求值也不必来自去掉 conditioning 的两支。[Sparse Guidance](https://arxiv.org/html/2601.01608v1)保持同一参数 θ、时刻和条件 c，只以不同 token sparsity γ 构成强、弱 capacity branch，再用 `ω D_strong(c)+(1−ω)D_weak(c)` 外推；它不是低成本 unconditional CFG，去条件的组合另有定义。两支各自 forward、随机 subset 以及 routing 暂绕后回填或 masking 的不同状态损失都要计费，ω 与两支 γ 需联合校准，并保留训练 sparsity 设置的兼容性。局部 attention 省算不能直接当作端到端吞吐收益：decoder、路由、质量与多样性可能改变净成本，受限图像/T2I 对照不授任意模型普效。分支失配或质量/多样性退步时，回退已验收的 dense sampling 或 CFG；这是一条以 capacity gap 提供信号的替代分支，不静默覆盖原条件差分的机制。<!-- source-family:SF-2026-ARXIV-2601-01608 -->

guidance reference也可以来自同一采样轨迹的历史，而非再计算去条件或低capacity网络。一条连续Flow分支保存与latent同形的velocity EMA，当前步用 `v + α(v−m)` 外推，随后为下一步更新历史；初始化、时间网格、衰减和update顺序都属于sampler state。它复用已算velocity而不新增网络求值，但有CFG时仍支付原两支求值，EMA驻留与向量算术也需计费；历史reference不是精确unconditional或独立弱模型。<!-- source-family:SF-2026-ARXIV-2602-20360 -->

[有限Euler采样对照](https://arxiv.org/html/2602.20360v1#S4)支持该历史分支的局部质量收益，却额外搜索了强度、衰减与guidance时窗；过强外推或与强CFG叠加会退步。低NFE、较好FID和不增加network evaluation须分别验收，不授分布保持、wall-clock减半或所有生成任务的收益。配置与轨迹变更、质量或多样性未通过时，减弱或关闭历史外推，回退原Euler/已校准CFG与capacity分支，而不让陈旧EMA自动接管新的采样协议。
