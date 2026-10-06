# Nov07 窄主题完整题摘初筛

只记录最初实际选取并读完整题摘的25项，不是全部分类/月表队列，不是冻结候选数。原始query/start/max/total在Atom中；published是提交字段，不是公开证明。当前版题摘只作发现，非v1已定点恢复并保留原件，未来内容不回填。以下“普通下一步”保留初筛过程；最新逐项裁决、日期隔离与必要反侧以[TAIL作者有限收束](TAIL_NECESSARY_NOTES.md)为准，不再把已隔离项作全实验普通队列，不授完整Evidence/Books完成。

## 2511.02919 Cache Mechanism for Agent RAG Systems

原始身份：[http://arxiv.org/abs/2511.02919v1](https://arxiv.org/abs/2511.02919v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-04T19:02:29Z`；updated `2025-11-04T19:02:29Z`。

完整原摘要：

> Recent advances in Large Language Model (LLM)-based agents have been propelled by Retrieval-Augmented Generation (RAG), which grants the models access to vast external knowledge bases. Despite RAG's success in improving agent performance, agent-level cache management, particularly constructing, maintaining, and updating a compact, relevant corpus dynamically tailored to each agent's need, remains underexplored. Therefore, we introduce ARC (Agent RAG Cache Mechanism), a novel, annotation-free caching framework that dynamically manages small, high-value corpora for each agent. By synthesizing historical query distribution patterns with the intrinsic geometry of cached items in the embedding space, ARC automatically maintains a high-relevance cache. With comprehensive experiments on three retrieval datasets, our experimental results demonstrate that ARC reduces storage requirements to 0.015% of the original corpus while offering up to 79.8% has-answer rate and reducing average retrieval latency by 80%. Our results demonstrate that ARC can drastically enhance efficiency and effectiveness in RAG-powered LLM agents.

筛选理由与普通下一步：保留潜在准入：历史 query 分布与 embedding geometry 联合管理每 Agent 小语料，可能改变固定 corpus/cache retention 选择；不是以缓存这个成熟概念关闭。尚需核选择/更新规则与容量、has-answer、延迟的可比条件。

## 2511.02997 Evaluating Control Protocols for Untrusted AI Agents

原始身份：[http://arxiv.org/abs/2511.02997v1](https://arxiv.org/abs/2511.02997v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-04T21:04:49Z`；updated `2025-11-04T21:04:49Z`。

完整原摘要：

> As AI systems become more capable and widely deployed as agents, ensuring their safe operation becomes critical. AI control offers one approach to mitigating the risk from untrusted AI agents by monitoring their actions and intervening or auditing when necessary. Evaluating the safety of these protocols requires understanding both their effectiveness against current attacks and their robustness to adaptive adversaries. In this work, we systematically evaluate a range of control protocols in SHADE-Arena, a dataset of diverse agentic environments. First, we evaluate blue team protocols, including deferral to trusted models, resampling, and deferring on critical actions, against a default attack policy. We find that resampling for incrimination and deferring on critical actions perform best, increasing safety from 50% to 96%. We then iterate on red team strategies against these protocols and find that attack policies with additional affordances, such as knowledge of when resampling occurs or the ability to simulate monitors, can substantially improve attack success rates against our resampling strategy, decreasing safety to 17%. However, deferring on critical actions is highly robust to even our strongest red team strategies, demonstrating the importance of denying attack policies access to protocol internals.

筛选理由与普通下一步：拟准入，待独立校准：给 adaptive attacker resampling/monitor 内部 affordance 后安全评价显著反转；新增局部反证可改变 protocol information boundary。v1 完整题摘另核，无须要求摘要披露所有攻击预算才保留。

## 2511.03019 SLIP: Structural-aware Language-Image Pretraining for Vision-Language Alignment

原始身份：[http://arxiv.org/abs/2511.03019v1](https://arxiv.org/abs/2511.03019v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-04T21:33:57Z`；updated `2025-11-04T21:33:57Z`。

完整原摘要：

> Vision-Language Pretraining (VLP) has achieved remarkable success across various downstream tasks, but such gains are largely driven by scaling up on training data. Yet, literature methods treat image-text pairs as isolated training examples; this neglects the rich relational structure naturally present in many domains, such as e-commerce product co-purchase graphs and social recommendation networks. Inspired by neuroscientific evidence that human encodes knowledge as relationship cognitive maps, we introduce Structure-aware Language-Image Pretraining (SLIP). SLIP integrates a structural contrastive loss to align modalities while also modeling relationships between neighboring entities in a structured graph. To support this paradigm, we construct a large-scale Amazon Product Co-purchase Multimodal Graph Dataset, enabling structured cross-modality supervision at scale. Experiment results show that SLIP consistently outperforms CLIP on cross-modal retrieval and classification tasks in both zero-shot and few-shot settings, showing the value of relational supervision for cross-modal alignment.

筛选理由与普通下一步：保留潜在准入：图邻接关系的 structural contrastive loss 改变跨模态监督，而非只换电商应用数据。需核实际损失与 matched CLIP 控制，不外推所有关系图。

## 2511.03051 No-Human in the Loop: Agentic Evaluation at Scale for Recommendation

原始身份：[http://arxiv.org/abs/2511.03051v1](https://arxiv.org/abs/2511.03051v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-04T22:49:39Z`；updated `2025-11-04T22:49:39Z`。

完整原摘要：

> Evaluating large language models (LLMs) as judges is increasingly critical for building scalable and trustworthy evaluation pipelines. We present ScalingEval, a large-scale benchmarking study that systematically compares 36 LLMs, including GPT, Gemini, Claude, and Llama, across multiple product categories using a consensus-driven evaluation protocol. Our multi-agent framework aggregates pattern audits and issue codes into ground-truth labels via scalable majority voting, enabling reproducible comparison of LLM evaluators without human annotation. Applied to large-scale complementary-item recommendation, the benchmark reports four key findings: (i) Anthropic Claude 3.5 Sonnet achieves the highest decision confidence; (ii) Gemini 1.5 Pro offers the best overall performance across categories; (iii) GPT-4o provides the most favorable latency-accuracy-cost tradeoff; and (iv) GPT-OSS 20B leads among open-source models. Category-level analysis shows strong consensus in structured domains (Electronics, Sports) but persistent disagreement in lifestyle categories (Clothing, Food). These results establish ScalingEval as a reproducible benchmark and evaluation protocol for LLMs as judges, with actionable guidance on scaling, reliability, and model family tradeoffs.

筛选理由与普通下一步：准入事实含糊，定点补读：多数 LLM 投票被称 ground truth，可能只有 evaluator 排名，也可能暴露类别依赖评价盲区；需要判断是否有独立 anchor/可改变评价选择的证据。不能因 benchmark 直接关闭。

## 2511.03060 The Curved Spacetime of Transformer Architectures

原始身份：[http://arxiv.org/abs/2511.03060v1](https://arxiv.org/abs/2511.03060v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-04T22:58:40Z`；updated `2025-11-04T22:58:40Z`。

完整原摘要：

> We present a geometric framework for understanding Transformer-based language models, drawing an explicit analogy to General Relativity. Queries and keys induce an effective metric on representation space, and attention acts as a discrete connection that implements parallel transport of value vectors across tokens. Stacked layers provide discrete time-slices through which token representations evolve on this curved manifold, while backpropagation plays the role of a least-action principle that shapes loss-minimizing trajectories in parameter space. If this analogy is correct, token embeddings should not traverse straight paths in feature space; instead, their layer-wise steps should bend and reorient as interactions mediated by embedding space curvature. To test this prediction, we design experiments that expose both the presence and the consequences of curvature: (i) we visualize a curvature landscape for a full paragraph, revealing how local turning angles vary across tokens and layers; (ii) we show through simulations that excess counts of sharp/flat angles and longer length-to-chord ratios are not explainable by dimensionality or chance; and (iii) inspired by Einstein's eclipse experiment, we probe deflection under controlled context edits, demonstrating measurable, meaning-consistent bends in embedding trajectories that confirm attention-induced curvature.

筛选理由与普通下一步：准入事实含糊，定点补读：几何类比本身不足；受控 context edit 与 chance/dimension 对照可能是表示演化的局部新证据。只核这部分是否可验证，不新建 spacetime owner。

## 2511.03106 Large language models require a new form of oversight: capability-based monitoring

原始身份：[http://arxiv.org/abs/2511.03106v1](https://arxiv.org/abs/2511.03106v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T01:20:28Z`；updated `2025-11-05T01:20:28Z`。

完整原摘要：

> The rapid adoption of large language models (LLMs) in healthcare has been accompanied by scrutiny of their oversight. Existing monitoring approaches, inherited from traditional machine learning (ML), are task-based and founded on assumed performance degradation arising from dataset drift. In contrast, with LLMs, inevitable model degradation due to changes in populations compared to the training dataset cannot be assumed, because LLMs were not trained for any specific task in any given population. We therefore propose a new organizing principle guiding generalist LLM monitoring that is scalable and grounded in how these models are developed and used in practice: capability-based monitoring. Capability-based monitoring is motivated by the fact that LLMs are generalist systems whose overlapping internal capabilities are reused across numerous downstream tasks. Instead of evaluating each downstream task independently, this approach organizes monitoring around shared model capabilities, such as summarization, reasoning, translation, or safety guardrails, in order to enable cross-task detection of systemic weaknesses, long-tail errors, and emergent behaviors that task-based monitoring may miss. We describe considerations for developers, organizational leaders, and professional societies for implementing a capability-based monitoring approach. Ultimately, capability-based monitoring will provide a scalable foundation for safe, adaptive, and collaborative monitoring of LLMs and future generalist artificial intelligence models in healthcare.

筛选理由与普通下一步：按完整题摘关闭贡献：提议 capability-based monitoring 的组织原则与实施考虑，未呈现独立新增检测机制或验证其跨任务能力的证据。不是因 healthcare 单词排除，也不采用其医学安全判断；日期不追查。

## 2511.03121 Control Barrier Function for Aligning Large Language Models

原始身份：[http://arxiv.org/abs/2511.03121v2](https://arxiv.org/abs/2511.03121v2)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T02:12:59Z`；updated `2025-11-06T03:06:07Z`。

完整原摘要：

> This paper proposes a control-based framework for aligning large language models (LLMs) by leveraging a control barrier function (CBF) to ensure user-desirable text generation. The presented framework applies the CBF safety filter to the predicted token generated from the baseline LLM, to intervene in the generated text. The safety filter includes two significant advantages: this safety filter is an add-on type, allowing it to be used for alignment purposes without fine-tuning the baseline LLM, and if there is an evaluation model regarding the desired alignment, it can be directly applied to the filter design. The overall text-generation system is implemented with open-source language models, aiming to generate positive text.

筛选理由与普通下一步：保留潜在准入：token-level CBF add-on 可能改变训练外约束路径。[exact-v1完整题摘已恢复](nov07-version-recovery-selected.txt)，摘要相同；v2提交字段为11/06 03:06:07Z，不证明本窗已公开，也没有取得实质修订说明。普通下一步只核v1评价模型/可行性条件，不从CBF名称推出安全保证。

## 2511.03190 Efficient Linear Attention for Multivariate Time Series Modeling via Entropy Equality

原始身份：[http://arxiv.org/abs/2511.03190v1](https://arxiv.org/abs/2511.03190v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T05:07:55Z`；updated `2025-11-05T05:07:55Z`。

完整原摘要：

> Attention mechanisms have been extensively employed in various applications, including time series modeling, owing to their capacity to capture intricate dependencies; however, their utility is often constrained by quadratic computational complexity, which impedes scalability for long sequences. In this work, we propose a novel linear attention mechanism designed to overcome these limitations. Our approach is grounded in a theoretical demonstration that entropy, as a strictly concave function on the probability simplex, implies that distributions with aligned probability rankings and similar entropy values exhibit structural resemblance. Building on this insight, we develop an efficient approximation algorithm that computes the entropy of dot-product-derived distributions with only linear complexity, enabling the implementation of a linear attention mechanism based on entropy equality. Through rigorous analysis, we reveal that the effectiveness of attention in spatio-temporal time series modeling may not primarily stem from the non-linearity of softmax but rather from the attainment of a moderate and well-balanced weight distribution. Extensive experiments on four spatio-temporal datasets validate our method, demonstrating competitive or superior forecasting performance while achieving substantial reductions in both memory usage and computational time.

筛选理由与普通下一步：保留潜在准入：entropy/ranking 条件下构造 linear attention 是模型基本机制，不按 time-series 应用标题自动排除。只核逼近条件与反例，不把预测指标外推 LLM。

## 2511.03214 LGM: Enhancing Large Language Models with Conceptual Meta-Relations and Iterative Retrieval

原始身份：[http://arxiv.org/abs/2511.03214v1](https://arxiv.org/abs/2511.03214v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T06:04:38Z`；updated `2025-11-05T06:04:38Z`。

完整原摘要：

> Large language models (LLMs) exhibit strong semantic understanding, yet struggle when user instructions involve ambiguous or conceptually misaligned terms. We propose the Language Graph Model (LGM) to enhance conceptual clarity by extracting meta-relations-inheritance, alias, and composition-from natural language. The model further employs a reflection mechanism to validate these meta-relations. Leveraging a Concept Iterative Retrieval Algorithm, these relations and related descriptions are dynamically supplied to the LLM, improving its ability to interpret concepts and generate accurate responses. Unlike conventional Retrieval-Augmented Generation (RAG) approaches that rely on extended context windows, our method enables large language models to process texts of any length without the need for truncation. Experiments on standard benchmarks demonstrate that the LGM consistently outperforms existing RAG baselines.

筛选理由与普通下一步：准入事实含糊，定点补读：concept meta-relation/reflection/iterative retrieval 可能只是组合，须核区别于既有 graph RAG 的实际机制或失效修正；any-length 不能从检索接口直接成立。

## 2511.03270 SCALE: Upscaled Continual Learning of Large Language Models

原始身份：[http://arxiv.org/abs/2511.03270v2](https://arxiv.org/abs/2511.03270v2)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T08:05:50Z`；updated `2025-12-11T12:41:40Z`。

完整原摘要：

> We revisit continual pre-training for large language models and argue that progress now depends more on scaling the right structure than on scaling parameters alone. We introduce SCALE, a width upscaling architecture that inserts lightweight expansion into linear modules while freezing all pre-trained parameters. This preserves the residual and attention topologies and increases capacity without perturbing the base model's original functionality. SCALE is guided by two principles: Persistent Preservation, which maintains the base model's behavior via preservation-oriented initialization and freezing of the pre-trained weights, and Collaborative Adaptation, which selectively trains a subset of expansion components to acquire new knowledge with minimal interference. We instantiate these ideas as SCALE-Preserve (preservation-first), SCALE-Adapt (adaptation-first), and SCALE-Route, an optional routing extension that performs token-level routing between preservation and adaptation heads. On a controlled synthetic biography benchmark, SCALE mitigates the severe forgetting observed with depth expansion while still acquiring new knowledge. In continual pre-training on a Korean corpus, SCALE variants achieve less forgetting on English evaluations and competitive gains on Korean benchmarks, with these variants offering the best overall stability-plasticity trade-off. Accompanying analysis clarifies when preservation provably holds and why the interplay between preservation and adaptation stabilizes optimization compared to standard continual learning setups.

筛选理由与普通下一步：保留潜在准入：冻结base、width expansion的preservation/adaptation改变continual-learning干扰边界。[exact-v1完整题摘已恢复](nov07-version-recovery-selected.txt)，其中已含SCALE-Route；纠正此前把Route称作未来扩展的表述。v2为12/11，未采用其新增内容；普通下一步核v1 preservation的精确初始化/冻结条件与matched budget。

## 2511.03276 Diffusion Language Models are Super Data Learners

原始身份：[http://arxiv.org/abs/2511.03276v1](https://arxiv.org/abs/2511.03276v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T08:17:42Z`；updated `2025-11-05T08:17:42Z`。

完整原摘要：

> Under strictly controlled pre-training settings, we observe a Crossover: when unique data is limited, diffusion language models (DLMs) consistently surpass autoregressive (AR) models by training for more epochs. The crossover shifts later with more or higher-quality data, earlier with larger models, and persists across dense and sparse architectures. We attribute the gains to three compounding factors: (1) any-order modeling, (2) super-dense compute from iterative bidirectional denoising, and (3) built-in Monte Carlo augmentation; input or parameter noise improves AR under data constraint but cannot close the gap. At scale, a 1.7B DLM trained with a ~1.5T-token compute budget on 10B unique Python tokens overtakes an AR coder trained with strictly matched settings. In addition, a 1B-parameter DLM achieves > 56% accuracy on HellaSwag and > 33% on MMLU using only 1B tokens, without any special tricks, just by repeating standard pre-training data. We also show that rising validation cross-entropy does not imply degraded downstream performance in this regime.

筛选理由与普通下一步：原贡献方向保留，事件重开：matched unique data/compute 下的 DLM/AR crossover 与 validation CE/downstream 解耦有准入价值。已另核 v1；作者仓库/原 Notion 显示更早发布线索，先核本窗是否有实质新事件，不因 arXiv 新 ID 重复收录。

## 2511.03367 Decoupling Augmentation Bias in Prompt Learning for Vision-Language Models

原始身份：[http://arxiv.org/abs/2511.03367v1](https://arxiv.org/abs/2511.03367v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T11:15:16Z`；updated `2025-11-05T11:15:16Z`。

完整原摘要：

> Recent advances in large-scale vision and language models have led to significant progress in zero-shot learning tasks. Methods such as CoOp and CoCoOp have shown that replacing handcrafted prompts with learnable vectors, known as prompt learning, can result in improved performance. However, these models often struggle to generalize to entirely unseen categories. While traditional zero-shot learning techniques benefit from various data augmentation strategies, prompt learning has primarily focused on text-based modifications, leaving the potential of image-based augmentation largely unexplored. In this work, we explore how image-level augmentations, particularly those that introduce attribute-specific variations, can support and enhance prompt learning. Our analysis examines the interaction between these augmentations and soft prompt frameworks, revealing their potential to improve generalization. We also identify a limitation in existing methods, such as CoCoOp, which do not provide explicit guidance for learning prompts that focus on semantically meaningful visual features. To address this, we propose Adding Attributes to Prompt Learning, AAPL, a novel method that introduces adversarial token embeddings to decouple superficial visual variations introduced by augmentation from class-relevant semantic representations. This decoupling enables the learned prompts to concentrate on visually discriminative features that align with the target categories. We conduct comprehensive experiments on eleven benchmark datasets, and AAPL consistently outperforms existing methods across few-shot, zero-shot, cross-dataset, and domain generalization settings. Our source code is publicly available at: https://github.com/Gahyeonkim09/AAPL

筛选理由与普通下一步：保留潜在准入：adversarial token embeddings 解耦 augmentation bias 与 class semantics 是具体适配机制；需必要目标/控制，不仅依赖 11 个数据集排名。

## 2511.03506 HaluMem: Evaluating Hallucinations in Memory Systems of Agents

原始身份：[http://arxiv.org/abs/2511.03506v3](https://arxiv.org/abs/2511.03506v3)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T14:37:34Z`；updated `2026-01-05T03:29:33Z`。

完整原摘要：

> Memory systems are key components that enable AI systems such as LLMs and AI agents to achieve long-term learning and sustained interaction. However, during memory storage and retrieval, these systems frequently exhibit memory hallucinations, including fabrication, errors, conflicts, and omissions. Existing evaluations of memory hallucinations are primarily end-to-end question answering, which makes it difficult to localize the operational stage within the memory system where hallucinations arise. To address this, we introduce the Hallucination in Memory Benchmark (HaluMem), the first operation level hallucination evaluation benchmark tailored to memory systems. HaluMem defines three evaluation tasks (memory extraction, memory updating, and memory question answering) to comprehensively reveal hallucination behaviors across different operational stages of interaction. To support evaluation, we construct user-centric, multi-turn human-AI interaction datasets, HaluMem-Medium and HaluMem-Long. Both include about 15k memory points and 3.5k multi-type questions. The average dialogue length per user reaches 1.5k and 2.6k turns, with context lengths exceeding 1M tokens, enabling evaluation of hallucinations across different context scales and task complexities. Empirical studies based on HaluMem show that existing memory systems tend to generate and accumulate hallucinations during the extraction and updating stages, which subsequently propagate errors to the question answering stage. Future research should focus on developing interpretable and constrained memory operation mechanisms that systematically suppress hallucinations and improve memory reliability.

筛选理由与普通下一步：保留潜在准入：将memory hallucination从端到端QA拆成extract/update/QA操作级，可改变错误定位与累积评价。[exact-v1完整题摘已恢复](nov07-version-recovery-selected.txt)，操作级三任务和错误累积方向确在v1；v2为11/09、v3为2026/01/05，均不回填。普通下一步核真值生成与stage attribution，不因只是benchmark关闭。

## 2511.03531 Efficient Neural Networks with Discrete Cosine Transform Activations

原始身份：[http://arxiv.org/abs/2511.03531v1](https://arxiv.org/abs/2511.03531v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T15:02:58Z`；updated `2025-11-05T15:02:58Z`。

完整原摘要：

> In this paper, we extend our previous work on the Expressive Neural Network (ENN), a multilayer perceptron with adaptive activation functions parametrized using the Discrete Cosine Transform (DCT). Building upon previous work that demonstrated the strong expressiveness of ENNs with compact architectures, we now emphasize their efficiency, interpretability and pruning capabilities. The DCT-based parameterization provides a structured and decorrelated representation that reveals the functional role of each neuron and allows direct identification of redundant components. Leveraging this property, we propose an efficient pruning strategy that removes unnecessary DCT coefficients with negligible or no loss in performance. Experimental results across classification and implicit neural representation tasks confirm that ENNs achieve state-of-the-art accuracy while maintaining a low number of parameters. Furthermore, up to 40% of the activation coefficients can be safely pruned, thanks to the orthogonality and bounded nature of the DCT basis. Overall, these findings demonstrate that the ENN framework offers a principled integration of signal processing concepts into neural network design, achieving a balanced trade-off between expressiveness, compactness, and interpretability.

筛选理由与普通下一步：保留潜在准入：DCT basis/activation 与 coefficient pruning 涉及基础表示和结构紧凑性，不能只因不是大 LLM 关闭；需核独立机制和任务控制。

## 2511.03559 AILA--First Experiments with Localist Language Models

原始身份：[http://arxiv.org/abs/2511.03559v1](https://arxiv.org/abs/2511.03559v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T15:43:54Z`；updated `2025-11-05T15:43:54Z`。

完整原摘要：

> This paper presents the first empirical demonstration of controllable locality in transformer language models, a novel architectural framework that enables continuous control over the degree of representation localization through a tunable locality dial parameter. Unlike traditional language models that rely exclusively on distributed representations, our approach allows dynamic interpolation between highly interpretable localist encodings and efficient distributed representations without requiring model retraining. We conducted experiments on the WikiText corpus using a two-layer transformer architecture, systematically varying the locality parameter λ across the full spectrum from 1.0 (fully localist) to 0.0 (fully distributed). Our results demonstrate that localist configurations achieve dramatically lower attention entropy, with λ = 1.0 yielding 5.36 bits compared to 7.18 bits at λ = 0.0, while maintaining substantially higher pointer fidelity scores reflecting stronger alignment with rule-specified targets. Prediction experiments reveal that intermediate locality values optimize the tradeoff between interpretability and performance, with λ = 0.6 achieving test perplexity of 4.65 and accuracy of 84.7%. These findings establish that localist language models provide a practical framework for applications in regulated domains requiring both transparency and capability, offering precise mathematical control over the interpretability-performance spectrum through explicit penalty thresholds and information-theoretic design principles.

筛选理由与普通下一步：保留潜在准入：两层模型 locality dial 的 pointer fidelity/预测取舍可作为受限表示证据；小规模不自动排除。需核训练、目标指针真值及无 retraining 声称。

## 2511.03570 TabGemma: Text-Based Tabular ICL via LLM using Continued Pretraining and Retrieval

原始身份：[http://arxiv.org/abs/2511.03570v1](https://arxiv.org/abs/2511.03570v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T15:51:03Z`；updated `2025-11-05T15:51:03Z`。

完整原摘要：

> We study LLMs for tabular prediction with mixed text, numeric, and categorical fields. We introduce TabGemma, a schema-agnostic in-context learner that treats rows as sequences and tackles two practical hurdles when adapting pretrained LLMs for tabular predictions: unstable numeric tokenization and limited context size. We propose to canonicalize numbers via signed scientific notation and continue pretraining of a 12B Gemma 3 model with a target imputation objective using a large-scale real world dataset. For inference, we use a compact n-gram-based retrieval to select informative exemplars that fit within a 128k-token window. On semantically rich benchmarks, TabGemma establishes a new state of the art on classification across low- and high-data regimes and improves monotonically with more context rows. For regression, it is competitive at small sample sizes but trails conventional approaches as data grows. Our results show that LLMs can be effective tabular in-context learners on highly semantic tasks when paired with dedicated numeric handling and context retrieval, while motivating further advances in numeric modeling and long-context scaling.

筛选理由与普通下一步：保留潜在准入：signed scientific notation 与 target-imputation 继续预训练可影响数值 tokenization/ICL；regression 随样本数落后亦有局部边界。仅应用排名不是拟采用命题，需匹配控制。

## 2511.03675 Whisper Leak: a side-channel attack on Large Language Models

原始身份：[http://arxiv.org/abs/2511.03675v1](https://arxiv.org/abs/2511.03675v1)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T17:47:46Z`；updated `2025-11-05T17:47:46Z`。

完整原摘要：

> Large Language Models (LLMs) are increasingly deployed in sensitive domains including healthcare, legal services, and confidential communications, where privacy is paramount. This paper introduces Whisper Leak, a side-channel attack that infers user prompt topics from encrypted LLM traffic by analyzing packet size and timing patterns in streaming responses. Despite TLS encryption protecting content, these metadata patterns leak sufficient information to enable topic classification. We demonstrate the attack across 28 popular LLMs from major providers, achieving near-perfect classification (often >98% AUPRC) and high precision even at extreme class imbalance (10,000:1 noise-to-target ratio). For many models, we achieve 100% precision in identifying sensitive topics like "money laundering" while recovering 5-20% of target conversations. This industry-wide vulnerability poses significant risks for users under network surveillance by ISPs, governments, or local adversaries. We evaluate three mitigation strategies - random padding, token batching, and packet injection - finding that while each reduces attack effectiveness, none provides complete protection. Through responsible disclosure, we have collaborated with providers to implement initial countermeasures. Our findings underscore the need for LLM providers to address metadata leakage as AI systems handle increasingly sensitive information.

筛选理由与普通下一步：拟准入安全反证，待精确身份/独立校准：TLS 内容保密不覆盖 streaming packet metadata，具体攻击与不完全 mitigation 改变 privacy boundary。不得遗漏安全披露；原 Microsoft blog 为 11/07 日期线索，不据此认定本窗公开。

## 2511.03690 The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents

原始身份：[http://arxiv.org/abs/2511.03690v2](https://arxiv.org/abs/2511.03690v2)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T18:16:44Z`；updated `2026-04-22T13:47:42Z`。

完整原摘要：

> Agents are now used widely in the process of software development, but building production-ready software engineering agents is a complex task. Deploying software agents effectively requires flexibility in implementation and experimentation, reliable and secure execution, and interfaces for users to interact with agents. In this paper, we present the OpenHands Software Agent SDK, a toolkit for implementing software development agents that satisfy these desiderata. This toolkit is a complete architectural redesign of the agent components of the popular OpenHands framework for software development agents. To achieve flexibility, we design a simple interface for implementing agents that requires only a few lines of code in the default case, but is easily extensible to more complex full-featured agents with features such as custom tools, memory management, and more. For security and reliability, it delivers seamless local-to-remote execution portability, integrated REST/WebSocket services. For interaction with human users, it can connect directly to a variety of interfaces, such as visual workspaces (VSCode, VNC, browser), command-line interfaces, and APIs. Compared with existing SDKs from OpenAI, Claude and Google, OpenHands uniquely integrates native sandboxed execution, lifecycle control, model-agnostic multi-LLM routing, and built-in security analysis. We validate the architecture empirically: production deployment data shows that V1 substantially reduces system-attributable failures over V0 with negligible event-sourcing overhead, and evaluations across multiple models and benchmarks demonstrate strong agent performance. Put together, these elements allow the OpenHands Software Agent SDK to provide a practical foundation for prototyping, unlocking new classes of custom applications, and reliably deploying agents at scale.

筛选理由与普通下一步：保留潜在准入，但纠正潜在证据：[exact-v1完整题摘已恢复](nov07-version-recovery-selected.txt)，v1只有SDK重新设计、sandbox/lifecycle/multi-LLM routing/security analysis与SWE-Bench Verified/GAIA评价，没有system-attributable failures下降或event-sourcing overhead实测。上方v2摘要仅保留原发现记录，后两项不得支撑本日准入/Books。普通下一步只核v1实际状态/执行契约是否超出模块组合；不是因为没有production数据自动排除。

## 2511.03773 Scaling Agent Learning via Experience Synthesis

原始身份：[http://arxiv.org/abs/2511.03773v2](https://arxiv.org/abs/2511.03773v2)；raw [arxiv-topic2.xml](arxiv-topic2.xml)；published(submission) `2025-11-05T18:58:48Z`；updated `2025-11-10T05:02:36Z`。

完整原摘要：

> While reinforcement learning (RL) can empower autonomous agents by enabling self-improvement through interaction, its practical adoption remains challenging due to costly rollouts, limited task diversity, unreliable reward signals, and infrastructure complexity, all of which obstruct the collection of scalable experience data. To address these challenges, we introduce DreamGym, the first unified framework designed to synthesize diverse experiences with scalability in mind to enable effective online RL training for autonomous agents. Rather than relying on expensive real-environment rollouts, DreamGym distills environment dynamics into a reasoning-based experience model that derives consistent state transitions and feedback signals through step-by-step reasoning, enabling scalable agent rollout collection for RL. To improve the stability and quality of transitions, DreamGym leverages an experience replay buffer initialized with offline real-world data and continuously enriched with fresh interactions to actively support agent training. To improve knowledge acquisition, DreamGym adaptively generates new tasks that challenge the current agent policy, enabling more effective online curriculum learning. Experiments across diverse environments and agent backbones demonstrate that DreamGym substantially improves RL training, both in fully synthetic settings and in sim-to-real transfer scenarios. On non-RL-ready tasks like WebArena, DreamGym outperforms all baselines by over 30%. And in RL-ready but costly settings, it matches GRPO and PPO performance using only synthetic interactions. When transferring a policy trained purely on synthetic experiences to real-environment RL, DreamGym yields significant additional performance gains while requiring far fewer real-world interactions, providing a scalable warm-start strategy for general-purpose RL.

筛选理由与普通下一步：保留潜在准入：reasoning-based transition/reward synthesis、real replay与adaptive curriculum改变真实rollout成本/反馈可信性取舍。[exact-v1完整题摘已恢复](nov07-version-and-native-recovery.txt)，该方向与sim-to-real warm-start已在v1；不回填11/10 v2。普通下一步核transition/reward校验及真实环境transfer控制，摘要缺实验设置不是关闭理由。

## 2511.02996 SCALE-VLP: Soft-Weighted Contrastive Volumetric Vision-Language Pre-training with Spatial-Knowledge Semantics

原始身份：[http://arxiv.org/abs/2511.02996v1](https://arxiv.org/abs/2511.02996v1)；raw [arxiv-topic3.xml](arxiv-topic3.xml)；published(submission) `2025-11-04T21:03:17Z`；updated `2025-11-04T21:03:17Z`。

完整原摘要：

> Vision-language models (VLMs) have demonstrated strong cross-modal capabilities, yet most work remains limited to 2D data and assumes binary supervision (i.e., positive vs. negative pairs), overlooking the continuous and structured dependencies present in volumetric data such as CT. Existing approaches often treat volumetric scans as independent 2D slices, compromising spatial coherence and underutilizing rich clinical semantics. We propose SCALE-VLP, a soft-weighted contrastive vision-language pre-training framework that integrates (i) volumetric spatial semantics to preserve anatomical structure and (ii) domain-aware, knowledge-infused semantics (e.g., radiological ontologies) to guide alignment. This yields structurally consistent and semantically grounded representations under limited supervision, demonstrating strong cross-task transferability (retrieval, report generation, and classification), and cross-domain generalizability with consistent gains without further fine-tuning. In particular, compared to the previous state of the art, SCALE-VLP achieves up to 4.3x higher top-1 CT-report retrieval, improves abnormality classification by 10 points, and reaches ROUGE-L 0.44 and BERT-F1 0.89 for report generation. Further, in zero-shot evaluation on an out-of-domain external dataset, we observe consistent gains, indicating the cross-task and cross-domain generalization ability of SCALE-VLP.

筛选理由与普通下一步：准入事实含糊，定点补读：volumetric spatial semantics 与 medical ontology 为领域监督，若只提升医学 retrieval/report/classification 则暂缓范围；但 soft-weighted contrastive objective 是否独立改变基础学习机制需核最小方法，不能仅医学标题自动关闭。

## 2511.03077 WorldPlanner: Monte Carlo Tree Search and MPC with Action-Conditioned Visual World Models

原始身份：[http://arxiv.org/abs/2511.03077v1](https://arxiv.org/abs/2511.03077v1)；raw [arxiv-topic3.xml](arxiv-topic3.xml)；published(submission) `2025-11-04T23:52:07Z`；updated `2025-11-04T23:52:07Z`。

完整原摘要：

> Robots must understand their environment from raw sensory inputs and reason about the consequences of their actions in it to solve complex tasks. Behavior Cloning (BC) leverages task-specific human demonstrations to learn this knowledge as end-to-end policies. However, these policies are difficult to transfer to new tasks, and generating training data is challenging because it requires careful demonstrations and frequent environment resets. In contrast to such policy-based view, in this paper we take a model-based approach where we collect a few hours of unstructured easy-to-collect play data to learn an action-conditioned visual world model, a diffusion-based action sampler, and optionally a reward model. The world model -- in combination with the action sampler and a reward model -- is then used to optimize long sequences of actions with a Monte Carlo Tree Search (MCTS) planner. The resulting plans are executed on the robot via a zeroth-order Model Predictive Controller (MPC). We show that the action sampler mitigates hallucinations of the world model during planning and validate our approach on 3 real-world robotic tasks with varying levels of planning and modeling complexity. Our experiments support the hypothesis that planning leads to a significant improvement over BC baselines on a standard manipulation test environment.

筛选理由与普通下一步：保留潜在准入：visual world model 的 action sampler 缓和规划 hallucination，MCTS/MPC 有具体闭环机制；属于 World Model/VLA 主线，不把三任务局部结果外推普适机器人。

## 2511.03163 Subsampled Randomized Fourier GaLore for Adapting Foundation Models in Depth-Driven Liver Landmark Segmentation

原始身份：[http://arxiv.org/abs/2511.03163v1](https://arxiv.org/abs/2511.03163v1)；raw [arxiv-topic3.xml](arxiv-topic3.xml)；published(submission) `2025-11-05T04:16:49Z`；updated `2025-11-05T04:16:49Z`。

完整原摘要：

> Accurate detection and delineation of anatomical structures in medical imaging are critical for computer-assisted interventions, particularly in laparoscopic liver surgery where 2D video streams limit depth perception and complicate landmark localization. While recent works have leveraged monocular depth cues for enhanced landmark detection, challenges remain in fusing RGB and depth features and in efficiently adapting large-scale vision models to surgical domains. We propose a depth-guided liver landmark segmentation framework integrating semantic and geometric cues via vision foundation encoders. We employ Segment Anything Model V2 (SAM2) encoder to extract RGB features and Depth Anything V2 (DA2) encoder to extract depth-aware features. To efficiently adapt SAM2, we introduce SRFT-GaLore, a novel low-rank gradient projection method that replaces the computationally expensive SVD with a Subsampled Randomized Fourier Transform (SRFT). This enables efficient fine-tuning of high-dimensional attention layers without sacrificing representational power. A cross-attention fusion module further integrates RGB and depth cues. To assess cross-dataset generalization, we also construct a new Laparoscopic Liver Surgical Dataset (LLSD) as an external validation benchmark. On the public L3D dataset, our method achieves a 4.85% improvement in Dice Similarity Coefficient and a 11.78-point reduction in Average Symmetric Surface Distance compared to the D2GPLand. To further assess generalization capability, we evaluate our model on LLSD dataset. Our model maintains competitive performance and significantly outperforms SAM-based baselines, demonstrating strong cross-dataset robustness and adaptability to unseen surgical environments. These results demonstrate that our SRFT-GaLore-enhanced dual-encoder framework enables scalable and precise segmentation under real-time, depth-constrained surgical settings.

筛选理由与普通下一步：拟定点准入校准：医学分割应用指标不纳入，但 SRFT 替代 SVD 的 gradient projection 是独立基础优化候选，不可一并范围排除。v1 已另核；只补读 optimizer 规则及实际成本/可比消融，不扩读医学队列。

## 2511.03165 SENT Map -- Semantically Enhanced Topological Maps with Foundation Models

原始身份：[http://arxiv.org/abs/2511.03165v1](https://arxiv.org/abs/2511.03165v1)；raw [arxiv-topic3.xml](arxiv-topic3.xml)；published(submission) `2025-11-05T04:22:04Z`；updated `2025-11-05T04:22:04Z`。

完整原摘要：

> We introduce SENT-Map, a semantically enhanced topological map for representing indoor environments, designed to support autonomous navigation and manipulation by leveraging advancements in foundational models (FMs). Through representing the environment in a JSON text format, we enable semantic information to be added and edited in a format that both humans and FMs understand, while grounding the robot to existing nodes during planning to avoid infeasible states during deployment. Our proposed framework employs a two stage approach, first mapping the environment alongside an operator with a Vision-FM, then using the SENT-Map representation alongside a natural-language query within an FM for planning. Our experimental results show that semantic-enhancement enables even small locally-deployable FMs to successfully plan over indoor environments.

筛选理由与普通下一步：准入事实含糊，定点补读：JSON representation 本身不是新机制；existing-node grounding 是否真实拒绝 infeasible states、并有受控对照是决定事实，只核这一点。

## 2511.03206 QG-CoC: Question-Guided Chain-of-Captions for Large Multimodal Models

原始身份：[http://arxiv.org/abs/2511.03206v1](https://arxiv.org/abs/2511.03206v1)；raw [arxiv-topic3.xml](arxiv-topic3.xml)；published(submission) `2025-11-05T05:49:48Z`；updated `2025-11-05T05:49:48Z`。

完整原摘要：

> Recently, Multimodal Large Language Models (MLLMs) encounter two key issues in multi-image contexts: (1) a lack of fine-grained perception across disparate images, and (2) a diminished capability to effectively reason over and synthesize information from multiple visual inputs. However, while various prompting methods aim to describe visual content, many existing studies focus primarily on single-image settings or specific, constrained scenarios. This leaves a critical gap in understanding and addressing how MLLMs tackle more general and complex multi-image reasoning tasks. Thus, we first extensively investigate how current prompting methods perceive fine-grained visual details and process visual information when dealing with multiple images. Our findings reveal that existing prompting methods fall short in attending to needed clues and seamlessly integrating perception and reasoning. Inspired by the findings, we propose a new zero-shot prompting method, Question-Guided Chain-of-Captions (QG-CoC), a generalized prompting approach that effectively handles problems with an arbitrary number of images. We evaluate our method on various open-source and closed-source MLLMs for multi-image and single-image benchmarks. Experimental results indicate that QG-CoC demonstrates competitive performance across tasks and exhibits robust improvements in the challenging scenarios where existing prompting methods fail.

筛选理由与普通下一步：保留潜在准入：multi-image clue failure 与 question-guided captioning 的收益边界可能修正 perception/reasoning 接口。不因 prompt 方法名称关闭，也不从 arbitrary image count 得出无上限保证。

## 2511.03768 What's in Common? Multimodal Models Hallucinate When Reasoning Across Scenes

原始身份：[http://arxiv.org/abs/2511.03768v1](https://arxiv.org/abs/2511.03768v1)；raw [arxiv-topic3.xml](arxiv-topic3.xml)；published(submission) `2025-11-05T15:37:50Z`；updated `2025-11-05T15:37:50Z`。

完整原摘要：

> Multimodal language models possess a remarkable ability to handle an open-vocabulary's worth of objects. Yet the best models still suffer from hallucinations when reasoning about scenes in the real world, revealing a gap between their seemingly strong performance on existing perception benchmarks that are saturating and their reasoning in the real world. To address this gap, we build a novel benchmark of in-the-wild scenes that we call Common-O. With more than 10.5k examples using exclusively new images not found in web training data to avoid contamination, Common-O goes beyond just perception, inspired by cognitive tests for humans, to probe reasoning across scenes by asking "what's in common?". We evaluate leading multimodal language models, including models specifically trained to perform chain-of-thought reasoning. We find that perceiving objects in single images is tractable for most models, yet reasoning across scenes is very challenging even for the best models, including reasoning models. Despite saturating many leaderboards focusing on perception, the best performing model only achieves 35% on Common-O -- and on Common-O Complex, consisting of more complex scenes, the best model achieves only 1%. Curiously, we find models are more prone to hallucinate when similar objects are present in the scene, suggesting models may be relying on object co-occurrence seen during training. Among the models we evaluated, we found scale can provide modest improvements while models explicitly trained with multi-image inputs show bigger improvements, suggesting scaled multi-image training may offer promise. We make our benchmark publicly available to spur research into the challenge of hallucination when reasoning across scenes.

筛选理由与普通下一步：拟准入局部评价反证，事件重开：single-image perception 饱和不覆盖跨 scene common-object reasoning，fresh-image 对照可能暴露评价盲区。v1 已另核，NeurIPS D&B 接收触发 OpenReview 更早公开定点核查；不以 35%/1% 榜单本身准入。

## 当前停止边界

原25项及其他窄查询已发现含糊相关项已有限收束，最新见[TAIL](TAIL_NECESSARY_NOTES.md)与[CURRENT_STOP](CURRENT_STOP.md)。Common-O/UserAlign OpenReview公开身份仍受阻；DLM本窗无已识别实质增量由root裁决不作为新事件，ScalingEval关闭。首批与SECOND未变校准复用。原生宽月表不转全类题摘/全文队列；没有日期证明者保留潜在方向/最小重开，不称已完成贡献Evidence，也不称零命中。新增关闭及必要安全反侧仍待非作者局部校准。
