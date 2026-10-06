# B14 — 六项最小必要原证与actual owner（六项已有覆盖安全终态）

2026-10-06 feb26_close_oct06非原packet作者独立定点核：20903 §3.2/4.2/AppG、20904原PDF文本§3.1–3.2/4.2/6（220–241/413–425/810–833/880–906）、20911§3/4.4、20913§3/6/AppA2/C、20924§4/7/9、20926§3/4.4必要原段与当前actual Ch31异质reward、Ch5 replacement faithfulness、Ch30谱兼容/组合重验、Ch75 map/source authority、Ch66执行/方法/结论分责、Ch76 graphtext/provenance与querysubgraph段逐项对应。六项具体已有覆盖通过；不复制glyph/驾驶/网络领域recipe，不采用lowentropy最优path、全部trace忠实、所有OCR假象、或指数邻接费用免除。原反侧/ND/分母全部保留，无新Books。旧行号随并行写入可能移动，按具体正文身份定位而非旧marker。仅本批通过，非日级验收。

## 2602.20903v1
https://arxiv.org/html/2602.20903v1；paragraph身份保留：

S3.SS2.SSS1.p1.1 | To address the structural blindness and overconfident scoring of prior OCR-based methods, our reward formulation is built upon a structure-aware assessment module. As illustrated in Fig. 2, this module identifies fine-grained structural anomalies in the generated text (e.g., missing or spurious strokes) and flags them with special markers. The detailed construction of this module is presented in Sec. 3.2.2. Assuming we have such a module, we formulate our composite reward as follows.

S3.SS2.SSS1.Px2.p1.2 | Here, \mathcal{T} and \mathcal{P} are the sets of words in the target and generated text, respectively. \mathcal{M} represents the optimal word pairing between \mathcal{T} and \mathcal{P} , found via the Hungarian algorithm to achieve the minimum alignment cost based on Normalized Edit Distance (NED). The \text{Penalty}(\cdot) term is the count of any unmatched words. This ensures that both superfluous generated words and missing target words contribute to the overall error. The final score \mathcal{S}_{E} is also clipped to the range of [0,1] , where a higher value indicates better semantic alignment.

S4.SS2.SSS1.p4.1 | RL for VTR. Tab. 3 quantifies the effectiveness of our RL-based optimization across diverse scenarios. Overall, integrating TextPecker’s structure-aware reward yields consistent improvements across four benchmarks, three base models, and both English and Chinese rendering tasks. For Flux.1[dev] [28] on English, gains are pronounced: +38.3% Sem. and +31.6% Qua. over the base model, and +11.7% Sem. over the OCR-reward baseline on GenTextEval. While gains are consistent overall, we also observe a few seemingly contradictory results when evaluated by different metrics. For example, SD3.5-M [16] on CVTG-2K reports +8.3% average word accuracy across five regions, yet -7.8% Sem. compared to the OCR-reward baseline. This divergence indicates that structure-unaware, OCR-based metrics can overestimate performance on structurally flawed text, underscoring the necessity of a structure-aware assessor for faithful evaluation—despite these localized divergences, the overall benchmark averages still show marked improvement. Notably, even for the well-optimized Qwen-Image [55], TextPecker-based RL delivers significant improvements, especially on Chinese rendering: +14.3% on OneIG, +7.4% on LongText, and +8.7% on GenTextEval over prior SOTA; compared to the OCR-reward baseline, Qua. increases by +2.0% and Sem. by +2.3%. Taken together, these results establish TextPecker as a generalizable, plug-and-play reward that advances structurally faithful and accurate text rendering.

A7.SS1.p1.1 | The evaluator is used only during RL training and run as a separate asynchronous service, hence it adds negligible overhead and does not affect inference latency; on SD3.5-M[16], 100 RL steps take 5.52 h (TextPecker) vs. 5.40 h (PPOCRv5[15]).

## 2602.20911v1
https://arxiv.org/html/2602.20911v1；paragraph身份保留：

S3.SS2.SSS0.Px2.p2.1 | For each cluster G_{k} , we start with a set of leaf experts, where each expert corresponds to a single task t\in G_{k} and holds its adapter parameters \theta_{t}\in\mathbb{R}^{D} and visual prototype \mathbf{p}_{t}^{\text{f}} . The tree is built using a bottom-up, iterative process. At each step, we find the two most similar experts in the current set by computing the cosine similarity between their visual prototypes:

S3.SS2.SSS0.Px3.p3.1 | The inference process begins with a parallel search, performed independently for each of the K trees. Starting from each tree’s root, the search path follows the child expert that shows lower predictive entropy for the given input. This recursive selection defines an optimal inference path \mathcal{P}_{k} from root to leaf for each tree. Further details on this entropy-guided selection process are provided in Appendix A.2.

S4.SS4.SSS0.Px3.p1.1 | A key advantage of SAEF’s hierarchical structure is the ability to control the trade-off between computational cost and predictive accuracy during inference. This is achieved via an entropy threshold, \tau_{e} , which enables an early-exit mechanism: the search down a path terminates if the current node’s predictive entropy falls below \tau_{e} . A higher threshold encourages more frequent early exits, thereby reducing the average search depth and accelerating inference. As shown in Table 3, this mechanism allows for significant efficiency gains. Compared to the ’Flat Structure’ baseline, which must query all N task adapters, SAEF offers a flexible spectrum of operating points. Setting \tau_{e}=1.0 strikes an excellent balance: it reduces the average search depth to just 1.19 and achieves a nearly 6 \times theoretical speedup, while incurring only a negligible 0.29% drop in accuracy. Notably, the measured inference time reduction closely aligns with our theoretical speedup calculations (see Appendix C), confirming the practical benefits of our method. This demonstrates that for many samples, high-level, generalized experts in the upper tiers of the forest are sufficient for confident prediction, making SAEF not only effective but also highly practical for real-world deployment.

## 2602.20913v1
https://arxiv.org/html/2602.20913v1；paragraph身份保留：

S3.SS2.p2.1 | To support exploring video clips of different lengths, we organize the video into a multi-level tree structure. The root node of the tree is the entire video, i.e., \mathbb{V}\equiv\mathbb{V}[0,T] . The tree has D levels (the root is the 0 -th level and the leaf node is the D -th level); each non-leaf node has K children, corresponding to its video clip partitioned into K equal-length, non-overlapping sub-clips. We denote a d -th-level clip as \mathbb{V}_{k_{1},\ldots,k_{d}} , where k_{d^{\prime}}\in\{0,\ldots,K-1\} indicates the child index at the d^{\prime} -th level. Unless otherwise specified, we assume that D=3 and K=\mathrm{round}(\sqrt[D]{T/16\mathrm{s}}) so that the video clip at the leaf level is approximately 16 -second long. This hierarchical structure allows the agent to check long video clips first and, when necessary, ‘zoom in’ to find an answer in finer-scale visual content. While the uniform partition is easy to implement, we understand that it is not the optimal choice, e.g., it would cause semantically similar content to fall into neighboring sub-clips, increasing the ambiguity of localization.

S3.SS2.p3.2 | There is a major difference between these two tools: \mathtt{video\_cap}() aims to offer generic video descriptions that assist the subsequent steps for key content localization, while \mathtt{video\_qa}() , often called at the last step, focuses on answering the specific question. For simplicity, we assume that both tools sample frames time-uniformly from video data, and vanilla visual encoding (i.e., no compression) is performed on the frames.

S6.SS2.p2.1 | Results on MLVU and Video-MME. The comparisons are shown in Tables 3 and 3, respectively. While LongVideo-R1 also performs well, it does not excel among the open-sourced MLLMs. The reason lies in the property of the benches: MLVU contains many short videos, and Video-MME contains many global questions like ‘What is the main idea of the video?’, which is beneficial for the uniform or adaptive (e.g., [42]) frame sampling methods. LongVideo-R1’s advantage also reflects in inference time. We compare LongVideo-R1 with Ego-R1 [45], which reports a similar accuracy on Video-MME. Differently, Ego-R1 requires video captioning every 30 seconds, resulting in an average of 86 caption segments on VideoMME, while LongVideo-R1 only undergoes an average of 10.5 rounds, claiming a much lower computational cost. The model’s performance on MLVU and Video-MME also benefits from improved multimodal tools, e.g., Qwen3-VL-32B-Instruct for video captioning.

A2.SS3.SSS0.Px2.p1.1 | During RL, we pre-extract all hierarchical captions to accelerate training, while the video_qa tool is invoked in real time. Qwen-2.5-VL-32B is deployed on two GPUs to serve as the video_qa module, while the remaining six GPUs are dedicated to RL training.

A4.p1.1 | Although LongVideo-R1 performs well across various long-video benchmarks, failure cases still occur (Figure 8, Figure 9). When a visually similar but irrelevant object appears in the video, the model sometimes commits to the wrong branch and fails to return to the correct segment.

## 2602.20924v1
https://arxiv.org/html/2602.20924v1；paragraph身份保留：

S4.SS2.p2.1 | The Verification Engine addresses these challenges with a three-stage pipeline. The Evaluator performs a systematic assessment of the workflow using the Knowledge Graph. The Selector determines the optimal verification strategy based on the Evaluator’s scores, selecting whether a given workflow merits direct use, requires enhancement, or benefits from combining with complementary workflows. Finally, the Synthesizer generates refined workflows: either by improving individual workflows in enhancement mode or by combining multiple workflows in hybrid mode. Note that the verification here assesses methodological alignment with prior work rather than guaranteeing the correctness of conclusions.

S7.SS1.p2.1 | Experimental Setup: We generate workflows using four models (Claude Sonnet 4.5, Claude Opus 4.5, Gemini-3-Pro, Gemini-3-Flash), at three temperatures (0.0, 0.5, 1.0), producing 12 configurations. Each configuration is run once, yielding a total of 12 generated workflows.

S7.SS1.p5.1 | Results: Workflows improved from 0% accuracy to operational correctness with one targeted fix guided by automated detection. Synthesizer correctly fixed the 0.0.0.0/0 bug for BGP prefixes, but issued a warning for the same issue for WHOIS records. The synthesized workflow also automatically implemented bogon prefix filtering and invalid AS record elimination, with additional warnings flagging suspicious patterns (e.g., large numbers of ASNs assigned to the U.S. DoD). Due to a warning for WHOIS, unlike an updated workflow in the case of BGP, LLM-guided manual correction of the WHOIS 0.0.0.0/0 record was required. Note that this correction is also fully automated without manual intervention when the query has better clarity (§ 7.3).

S9.p4.1 | Limitations. Despite demonstrated capabilities, Airavat exhibits fundamental limitations. While it can be fully automated for well-known problems, it can only serve as a co-pilot for never-seen-before problems. The Registry requires manual curation; while the RegistryCurator Agent identifies reusable patterns, all additions require expert validation to maintain quality standards. While the knowledge graph captures a broad slice of measurement literature, it may miss informal best practices. The verification engine can only detect methodological flaws documented in existing literature. The system cannot generate validation strategies for workflows requiring long-term longitudinal studies, large-scale infrastructure deployment, or proprietary datasets unavailable in public repositories. Finally, query precision can dramatically impact accuracy, as demonstrated in § 7.3, requiring both experts and non-experts to be precise in their interactions.

## 2602.20926v1
https://arxiv.org/html/2602.20926v1；paragraph身份保留：

S3.SS2.SSS2.p3.1 | Iterative Expansion. At each step i (where 2\leq i\leq N , and N denotes the number of expansion hops), the model extends reasoning paths to incorporate broader context. Specifically, in the i -th expansion round, we process each HyperNode H\in H_{i-1} individually. We identify a set of adjacent triplets \mathcal{T}_{adj} from the Knowledge Graph \mathcal{G} that are directly connected to the entities contained within the current H . For each adjacent triplet \tau_{next}\in\mathcal{T}_{adj} , we instantiate a new expanded HyperNode H^{\prime}=H\cup\{\tau_{next}\} . The global candidate set \mathcal{C}_{cand} is then formed by accumulating all such generated H^{\prime} instances derived from each preceding HyperNode in H_{i-1} . This incremental growth allows each HyperNode to transition from a single fact to a complex path structure representing a multi-hop chain of evidence.

S3.SS3.p2.1 | To bridge the semantic gap between the retrieved structural knowledge and the original source corpus, we leverage the Triple-to-Passage Index \Phi . This specialized inverted index, as constructed in Sec. 3.1, establishes a one-to-many mapping between each unique triplet \tau and the set of source passages from which it was extracted. By recognizing that a single factual claim can be instantiated across multiple disparate passages, this index ensures comprehensive evidence coverage. Such a mechanism enables robust provenance tracking, allowing the model to backtrack from a specific hop in the reasoning path to all supporting textual fragments that validate the underlying logic.

S4.SS4.p1.1 | 1) Hybrid Retrieval Strategy. Table 2 underscores the synergy between structural precision and semantic coverage within our Hybrid Retrieval Strategy. To provide a multi-dimensional assessment, we report both Exact Match (EM), which measures the percentage of predicted answers that exactly match the ground truth, and Recall@5, which indicates whether at least one of the top-5 retrieved passages contains the gold evidence required to answer the query. The evaluation shows that performance peaks at M=4 , a 20%+ improvement over pure dense retrieval ( M=0 ), proving that logical paths effectively resolve multi-hop dependencies. However, when semantic backfill is constrained ( M=5 ), performance slightly declines. This non-monotonic trend suggests that a purely logical path-guided approach is vulnerable to graph incompleteness and structural noise; thus, maintaining a dense retrieval component is essential as a robust fallback to ensure comprehensive evidentiary support.

S4.SS4.p3.1 | On one hand, the retrieval time exhibits an exponential growth pattern. While the latency remains manageable at N=1 and N=2 , it surges dramatically to 577.2 s at N=3 and becomes prohibitive at N=4 . On the other hand, the F1 score follows a non-monotonic trajectory, yet remarkably remains above 74.5\% across all values of N , demonstrating HELP’s robustness and strong performance. Specifically, performance peaks at 76.18\% when N=3 , as deeper exploration retrieves more relevant context. However, increasing N to 4 leads to a performance degradation. This decline suggests that excessive expansion introduces significant noise and irrelevant information, which outweighs the benefits of broader context coverage. Given that the F1 score remains competitive even at lower hops, N=2 offers a compelling balance, achieving high accuracy with only a fraction of the computational overhead required for N=3 .

## 2602.20904v1
HTML为空转换壳，精确PDF https://arxiv.org/pdf/2602.20904v1 定点机械摘录。

### PDF extraction L220–241
base(x) +T ℓ(x)≈MLP ℓ
target(x). More precisely, we
build areplacement modelby replacing each MLP in the
target model with a base MLP and transcoder adapter. At
each layer, the replacement model forward pass computes:
ˆh′
ℓ = ˆhℓ−1 +Attn ℓ
target(ˆhℓ−1)
ˆhℓ = ˆh′
ℓ +MLP ℓ
base(ˆh′
ℓ) +T ℓ(ˆh′
ℓ)
where ˆh0 is the embedded input and hℓ and ˆhℓ denote hid-
den states at layer ℓ for the target and replacement models.
Finally, we let ytarget and ˆydenote the output distributions
of the target and replacement models respectively. Only
transcoder parameters are updated during training.
3.2. Training Objective
We train transcoder adapters to faithfully reconstruct the
target model’s outputs and hidden states. In addition to
faithful reconstruction, adapter features must be sparsely

### PDF extraction L413–425
NMSE captures raw reconstruction error, it is hard to inter-
pret in a vacuum. To contextualize this, we perform partial
replacements—substituting the first k, final k, or a single
layer k with adapter layers—and measure output KL di-
vergence. Notably, KL divergence when replacing subsets
of layers is always less than KL divergence when using
adapters to approximate all layers, indicating that internal
errors do not accumulate beyond what is reflected in the
final output. Results for L0 1.4 adapter are shown in Fig-
ure 3. Appendix C shows these metrics for our full suite of
adapters and for an adapter trained without the bridging loss.
When ablating the bridging loss, NMSE remains low but KL
divergence under partial replacement increases substantially.

### PDF extraction L810–833
6.1. Features Necessary and Sufficient for Hesitation
As a proxy for hesitation, we measurewaittoken frequency
per 1,000 response tokens. Removing hesitation output fea-
tures reduceswaitfrequency by 70% (from 5.5 to 1.5); addi-
tionally removing template features reduces it further to 0.5.
As the model generates fewer hesitation tokens, response
length drops from 7.8k to 3.5k tokens when removing both
feature groups (Figure 9, left). Given that hesitation output
features were selected precisely for promoting hesitation
words, it is perhaps unsurprising that they are necessary for
the model to saywait. We next test whether these features
are sufficient by adding them to the hybrid model, which
has a near-zero rate of hesitation tokens and short responses
( 1.2k tokens). Adding just template features or just hesita-
tion output features produces slight increases (0.2 and 1.5,
respectively), but adding both produces a much larger effect
(8.2), supporting our observation that these feature classes
interact (Figure 9, right).7 When adding or ablating random
features as a control, modifying even 50,000 random fea-
tures produces smaller effects than our 5,623 hand-selected
features.
7In fact, rate ofwaitexceeds the full adapter’s rate of 5.5.
We find that adding an additional 5k features that activate before
hesitation tokens returns the rate to full adapter levels without

### PDF extraction L880–906
is unchanged on MATH500, AMC23, and GPQA Diamond.
On AIME25, accuracy decreases from 26% to 20%. This is
consistent with prior work showing it is possible to reduce
reasoning-model verbosity, via additional training (Liu et al.,
2025a) or inference-time interventions (Wang et al., 2025;
Huang et al., 2025). Though less performant, our interven-
tion emerges naturally from decomposing the fine-tuning
difference, suggesting that a partial separation between ver-
bosity and accuracy arises naturally from reasoning training.
We next test whether this intervention transfers to the target
model. In the adapter setting, we ablate features by zeroing
their encoder and decoder parameters. We observe that ab-
lating transcoder adapter features is equivalent to adding a
new feature with the same encoder and a negated decoder.
We thus intervene on the target model by first construct-
ing an adapter where each feature we wish to suppress is
negated8, then evaluating the target model with this negated
8Scaling by −1 led to incoherent outputs; we use −0.5. We
hypothesize this is because of distribution shift in encoder inputs.
8
=== PAGE 9 ===
Transcoder Adapters for Reasoning-Model Diffing
adapter added. Figure 10 (red) shows that suppressing these
adapter features in the target reasoning model also reduces
response length, with only a slight decrease in accuracy.
We expect some decrease in performance given this cruder
intervention. However, accuracy remains high enough to

### PDF extraction L1258–1266
A. Training Details
Optimization.We train transcoder adapters using the Adam optimizer with default hyperparameters, a learning rate of
8×10 −4, and a batch size of 1. Although we use a batch size of 1, OpenThoughts3 samples average approximately 7,500
tokens, so each gradient step computes losses over all token positions in the sample. We apply a linear learning rate warmup
for the first 5% of training followed by cosine decay. Training is conducted in bfloat16 precision.
Loss computation.Computing the bridging loss at every layer is expensive, as it requires forward passes through the
remaining layers of both models. To reduce this cost, we estimate the bridging losses at each step by uniformly sampling a
single cutoff layer k∼Uniform{1, . . . , L} and computing the forward and backward bridging losses at layer k only. We
weight all four reconstruction losses (output KL, forward and backward bridging KL, and NMSE) equally with coefficient 1.

## Actual owner books/part-04-training-system/31-rlhf.md

### 原文件L255–257
同质文本输出可以共用 string matching；回答同时包含正文、公式与表格后，先要分清每路 reward 在比较什么，再讨论如何聚合。一个 format-decoupled 分支分别比较 text edit similarity、公式的 LaTeX token overlap 与表格结构，再只对 ground truth 中非空的类型取平均。此时 type membership 决定了每个样本的分母；缺少某种类型不等于该项通过，也不能把没有参考对象的分项默认为满分。Reward owner 应版本化类型划分、匹配对象、eligible population 及 regex/parse 失败口径，聚合器消费这些定义，不能通过改变分母静默改写目标。

分工能减少一种 string metric 对异质对象的误判，却不提供全格式正确性保证：公式 BLEU 不等于数学或表达式语义正确，table TEDS 不等于全部格式有效，平均分也不证明每路都满足。作者在同一 Qwen3-VL-4B 文档解析设置中的分项消融支持局部 reward 分工，text 指标并非随整体分数单调改善；难度过滤的不同样本比例也不是等预算比较。格式拆分增加 parser、参考对象维护与分项校准成本；输出同质、类型抽取不稳或语义要求未被代理指标覆盖时，应回退已校准的单项匹配、分项报告与独立 semantic/validity gate，不能让聚合 reward 替代验收。<!-- source-family:SF-2026-ARXIV-2601-08834 -->

## Actual owner books/part-01-worldview/05-what-neural-networks-learn.md

### 原文件L304–311

当研究者用 sparse features、transcoder 或 attribution graph 替代原模型的一部分计算时，
得到的是一个 **解释用 replacement model**，不是原模型本身。它至少引入四类差距：feature
dictionary 无法重构的 error nodes、未被替换的 attention/QK path、为可读性做的 graph pruning，
以及人类对 features 和 supernodes 的命名。图更小、更可读，通常意味着保留的计算更不完整。

因此 circuit evidence 应同时报告：replacement reconstruction error、pruning threshold 与 graph
completeness、在原模型上的 intervention，以及 prompt/model selection 范围。若干选定案例能被

## Actual owner books/part-04-training-system/30-lora.md

### 原文件L595–597
权重增量在同一 backbone 和坐标系中才有直接相加的语义；跨蒸馏版本或 video-diffusion 变体时，低秩方向可能代表不同功能。无目标数据的受限分支可以用更新的谱结构与刚性度聚类，先判断哪些 LoRA 可能共享子空间，再限制 routing 或 merge 范围。谱 gate 只拥有兼容性筛选权，不拥有下游质量证明。

它避免盲目合并，却可能把功能相近但谱不同的 adapter 拒绝，也无法观察真实数据上的交互。若有代表性目标数据，应优先做组合后评测；若坐标身份不明，回退独立加载。现有 exact-v1 仅覆盖作者的模型变体，不能给出通用兼容阈值。<!-- semantic-body-binding:SF-2026-ARXIV-2605-01929 -->

### 原文件L603–607
```text
W = W_0 + lambda_1 Delta W_1 + lambda_2 Delta W_2
```

不同 adapters 可能修改同一表示方向，组合后分布也可能超出各自训练范围。Adapter composition、merge 和 routing 都需要重新 Evaluation，不能把独立任务得分当作组合行为证明。

## Actual owner books/part-07-agent/75-context.md

### 原文件L391–397
### Context Map 是轻量导航状态，不是事实副本

把全部历史塞回 prompt 在短会话中最忠实；长任务中可维护一个小型 orientation map，只保存主题、位置、freshness 与 provenance pointer，再按需读取原文。它降低 assembly cost，却新增 map 漂移、错误指针和遗漏风险，因此 map 不能拥有事实 authority，命中后仍须回源；任务短或证据不可寻址时，直接 context 仍合理。<!-- source-family:SF-2026-ARXIV-2605-19932 --> exact-v1 §3–4 支持其 orientation cache，§5 不证明该摘要在开放长期任务中无损。

当 tool result 可按 path/hash 重新寻址时，完整保留所有消息并不是唯一的 correctness baseline。一个受限分支是在透明 Messages-API proxy 中先驱逐或压缩匿名、短寿命的输出，把完整 conversation 留在 client backing store，并在可寻址内容的位置插入 retrieval handle；后续重复读取触发 fault，再按 path/hash 取回并 pin 住该内容。Context manager 因而拥有 visible message working set、handle 与 pin state，backing store 仍拥有原始事实；这不是把 KV tensor 从 HBM page 到 host/storage。它以 fault tail、错误驱逐和 hash/path 失效风险换取 token 空间，短会话、高风险审计或工具输出不可稳定寻址时仍应完整携带。`arXiv:2603.09023v1` 的 §3 支持该 L1/L2 机制，§5 只评测 message eviction 与 fault-driven pinning；L3 只完成实现而未做规模评测，L4 仅是接口，因此不能把分层设计外推为已验证的通用 Context storage。<!-- source-family:SF-2026-ARXIV-2603-09023 -->

Context 参与模型行为身份。至少需要记录：

## Actual owner books/part-06-ai-infrastructure/66-evaluation-system.md

### 原文件L47–49
问题不在于分数无用，而在于**任何分数都是在某个对象、分布、环境和测量方法下产生的条件性证据**。丢掉条件，只留下数值，评估就会退化为不可解释的排行榜。

## HTTP 成功只是质量判断的第一道门

### 原文件L108–110
分析型 Agent 还要把待估量与分析规范分开：同一 dataset、hypothesis 和 estimand，只固定了“要估什么”，没有固定缺失值处理、异常点、协变量、函数形式、权重或 standard error 的选择。代码实际执行且 auditor 判合规后，多条看似合理的 pipeline 仍可能给出不同区间和结论；只挑一个支持预期的结果，会把规范搜索隐藏成同一个任务的稳定答案。EvalSpec 因而应保存这些选择、persona/model/sampling identity 和可比较的 pipeline 分布，而不是仅由一份可运行代码认证结论唯一。<!-- source-family:SF-2026-ARXIV-2602-18710 -->

[固定 estimand 的有限分析审计](https://arxiv.org/html/2602.18710v1)将 4,946 次运行过滤为 3,303 次合规分析，排除率还随模型与 confirmation-seeking persona 改变；合规后的支持率不能替代所有请求的成功率，或成为原假设真值。完整 tool transcript 比只读最终报告更能核实执行，却不使 LLM auditor 自动独立、无误或消除所有规范争议；旧结果污染、未量化的人审抽样与事后方向纠正均限制外推。Ensemble、工具执行、审计和选择规则都付费；规范自由度或审计资格未校准时，应预先限制关键选择、同时披露 survivor 分母与失败人口，保留独立复算/人工核验，而不是由大量合规结果自行签发确定结论。

## Actual owner books/part-07-agent/76-rag.md

### 原文件L281–283
混合 text/graph RAG 不应只拼接两路结果。Graph-to-text 通道可用已访问节点为文本证据投票降噪；text-to-graph 通道则把 search history 中被 beam pruning 的 orphan nodes 保存为带 provenance 的 deferred search state，并在文本线索支持时重开。该机制用历史状态与双向校验换 recall/precision，代价是 stale graph、错误 resurrection 与额外融合控制；identity/provenance 不完整时回退独立 text/graph 检索与显式 rerank。

作者仅报告多个 multi-hop benchmark 的相对结果，摘要未披露完整模型、硬件、并发或生产 freshness 条件；不证明通用最优融合。 PLATFORM-SECURITY 只接收 poisoning/authorization handoff；RAG 章节拥有检索状态与证据 admission。

### 原文件L805–810
在线 graph traversal 也不只等于“向量检索后扩邻居”。多 anchor 从不同 entity/frontier 出发，在交汇处
形成 query-specific evidence subgraph，可以捕捉分散关系；代价是 graph construction/provenance、anchor
calibration、动态更新/删除、授权过滤与 tail latency。Source graph 稳定且关系是主要信号时值得使用；
关系弱、索引频繁变化或授权过滤会破坏连通性时，chunk retrieval 与原文 dereference 更简单。

Graph 的来源审计还不能只验证最终引用句子。若 ingestion 允许把 corpus 中同类型实体互换，局部文本仍可能流畅，构成的边和多跳桥接却已指向错误主体；后续 traversal 即使忠实于图，也会把错误拓扑当作证据。因而 graph owner 应把实体身份、类型、边的原文 span 与构图 revision 一起纳入 admission，并在图上复核关键路径能否回指原始关系；静态文本过滤和 citation 格式正确都不足以证明拓扑未被污染。这增加图更新与核对成本；无法可靠维护 provenance 时，应回退到原文检索和逐跳验证。受控 GraphRAG 攻击只证明所测 corpus、构图器和多跳问答的这一失效路径，不给开放部署的统一攻击率。<!-- source-family:SF-2026-ARXIV-2604-02954 -->
