# 有限剩余贡献线索：11份已存Atom完整题摘

仅03-14/Mar13自然日。2026-10-10实际从原四主题/两title补检缓存按精确ID读取完整title/summary；没有新query，不全149/41逐项AB，不授日期/Source/评分。当前Atom可能latest v2/v3：首公开事件需必要exact-v1，具体纠错只核受影响当前版本，不能把新版本摘要倒灌早版。最新root逐ID实际回官方Atom完整题名/摘要/版本校准通过7窄P、3决定core、11687具体EX，主独核末节已记；当前仍不授日期、Evidence或评分。

## http://arxiv.org/abs/2603.11211v3

原件：SUP_TOPIC_MULTIMODAL.raw

标题：A Simple Efficiency Incremental Learning Framework via Vision-Language Model with Nonlinear Multi-Adapters

完整摘要：Incremental Learning (IL) aims to learn new tasks while preserving previously acquired knowledge. Integrating the zero-shot learning capabilities of pre-trained vision-language models into IL methods has marked a significant advancement. However, these methods face three primary challenges: (1) the need for improved training efficiency; (2) reliance on a memory bank to store previous data; and (3) the necessity of a strong backbone to augment the model's capabilities. In this paper, we propose SimE, a Simple and Efficient framework that employs a vision-language model with adapters designed specifically for the IL task. We report a remarkable phenomenon: there is a nonlinear correlation between the number of adaptive adapter connections and the model's IL capabilities. While increasing adapter connections between transformer blocks improves model performance, adding more adaptive connections within transformer blocks during smaller incremental steps does not enhance, and may even degrade the model's IL ability. Extensive experimental results show that SimE surpasses traditional methods by 9.6% on TinyImageNet and outperforms other CLIP-based methods by 5.3% on CIFAR-100. Furthermore, we conduct a systematic study to enhance the utilization of the zero-shot capabilities of CLIP. We suggest replacing SimE's encoder with a CLIP model trained on larger datasets (e.g., LAION2B) and stronger architectures (e.g., ViT-L/14).

作者初判：窄P：更多adapter连接未必改善、block内/跨block不同干扰的负侧可能修正配置解释；不借CLIP规模/9.6数字加分。

## http://arxiv.org/abs/2603.12055v3

原件：SUP_TOPIC_MULTIMODAL.raw

标题：Continual Learning with Vision-Language Models via Semantic-Geometry Preservation

完整摘要：Continual learning of pretrained vision-language models (VLMs) is prone to catastrophic forgetting, yet current approaches adapt to new tasks without explicitly preserving the cross-modal semantic geometry inherited from pretraining and previous stages, allowing new-task supervision to induce geometric distortion. We observe that the most pronounced drift tends to concentrate in vulnerable neighborhoods near the old-new semantic interface, where shared visual patterns are easily re-explained by new textual semantics. To address this under an exemplar-free constraint, we propose Semantic Geometry Preservation for Continual Learning (SeGP-CL). SeGP-CL first probes the drift-prone region by constructing a compact set of adversarial anchors with dual-targeted projected gradient descent (DPGD), which drives selected new-task seeds toward old-class semantics while remaining faithful in raw visual space. During training, we preserve cross-modal structure by anchor-guided cross-modal geometry distillation (ACGD), and stabilize the textual reference frame across tasks via a lightweight text semantic-geometry regularization (TSGR). After training, we estimate anchor-induced raw-space drift to transfer old visual prototypes and perform dual-path inference by fusing cross-modal and visual cues. Extensive experiments on five continual learning benchmarks demonstrate that SeGP-CL consistently improves stability and forward transfer, achieving state-of-the-art performance while better preserving semantic geometry of VLMs. Code is available at: https://github.com/chiyuan-IVIPLab/SeGP-CL.

作者初判：窄P：无exemplar约束下old-new邻域漂移、adversarial anchors→几何distill→prototype转移的实际条件可能改变保持接口；不把模块数或SOTA即贡献。

## http://arxiv.org/abs/2603.11510v1

原件：SUP_TITLES_CL_RETRY.raw

标题：Tiny Aya: Bridging Scale and Multilingual Depth

完整摘要：Tiny Aya redefines what a small multilingual language model can achieve. Trained on 70 languages and refined through region-aware posttraining, it delivers state-of-the-art in translation quality, strong multilingual understanding, and high-quality target-language generation, all with just 3.35B parameters. The release includes a pretrained foundation model, a globally balanced instruction-tuned variant, and three region-specialized models targeting languages from Africa, South Asia, Europe, Asia-Pacific, and West Asia. This report details the training strategy, data composition, and comprehensive evaluation framework behind Tiny Aya, and presents an alternative scaling path for multilingual AI: one centered on efficiency, balanced performance across languages, and practical deployment.

作者初判：只决定core：小模型多语种/region-aware posttraining目前未给新增原理；仅核训练/数据/区域共享取舍有无新可支持界限，不能因modelreport默认深审或因小而排除。

## http://arxiv.org/abs/2603.11687v2

原件：SUP_TITLES_CL_RETRY.raw

标题：SemBench: A Universal Semantic Framework for LLM Evaluation

完整摘要：Recent progress in Natural Language Processing (NLP) has been driven by the emergence of Large Language Models (LLMs), which exhibit remarkable generative and reasoning capabilities. However, despite their success, evaluating the true semantic understanding of these models remains a persistent challenge. Traditional benchmarks such as Word-in-Context (WiC) effectively probe this capability, but their creation is resource-intensive and often limited to high-resource languages. In this paper, we introduce SemBench, a framework for automatically generating synthetic benchmarks that assess the semantic competence of LLMs using only dictionary sense definitions and a sentence encoder. This approach eliminates the need for curated example sentences, making it both scalable and language-independent. We evaluate SemBench in three languages (English, Spanish, and Basque) spanning different levels of linguistic resources, and across a wide range of LLMs. Our results show that rankings derived from SemBench strongly correlate with those obtained from standard WiC datasets. Furthermore, our analysis demonstrates that only a small number of examples is required to achieve stable and meaningful rankings. Overall, SemBench provides a lightweight, adaptable, and data-efficient framework for cross-lingual evaluation of semantic understanding in LLMs.

作者初判：拟具体EX：dictionary+sentenceencoder合成WiC替代人口、rank相关与少样本稳定是benchmark制备局部；摘要未发现新的语义评价盲区/原评估失效界，language-independent口号不认证任何语言。不是因Basque/语言学标签。

## http://arxiv.org/abs/2603.11698v2

原件：SUP_TITLES_CL_RETRY.raw

标题：OSCBench: Benchmarking Object State Change in Text-to-Video Generation

完整摘要：Text-to-video (T2V) generation models have made rapid progress in producing visually high-quality and temporally coherent videos. However, existing benchmarks primarily focus on perceptual quality, text-video alignment, or physical plausibility, leaving a critical aspect of action understanding largely unexplored: object state change (OSC) explicitly specified in the text prompt. OSC refers to the transformation of an object's state induced by an action, such as peeling a potato or slicing a lemon. In this paper, we introduce OSCBench, a benchmark specifically designed to assess OSC performance in T2V models. OSCBench is constructed from instructional cooking data and systematically organizes action-object interactions into regular, novel, and compositional scenarios to probe both in-distribution performance and generalization. We evaluate six representative open-source and proprietary T2V models using both human user study and multimodal large language model (MLLM)-based automatic evaluation. Our results show that, despite strong performance on semantic and scene alignment, current T2V models consistently struggle with accurate and temporally consistent object state changes, especially in novel and compositional settings. These findings position OSC as a key bottleneck in text-to-video generation and establish OSCBench as a diagnostic benchmark for advancing state-aware video generation models.

作者初判：窄P：video scene/text一致不等物体动作后状态改变，regular/novel/composition按OSC拆分可修正生成评价；cooking只是刺激来源，不能采Science场景分数或人类真值普遍保证。

## http://arxiv.org/abs/2603.11781v1

原件：SUP_TITLES_CL_RETRY.raw

标题：From Debate to Deliberation: Structured Collective Reasoning with Typed Epistemic Acts

完整摘要：Multi-agent LLM systems increasingly tackle complex reasoning, yet their interaction patterns remain limited to voting, unstructured debate, or pipeline orchestration. None model deliberation: a phased process where differentiated participants exchange typed reasoning moves, preserve disagreements, and converge on accountable outcomes. We introduce Deliberative Collective Intelligence (DCI), specifying four reasoning archetypes, 14 typed epistemic acts, a shared workspace, and DCI-CF, a convergent flow algorithm that guarantees termination with a structured decision packet containing the selected option, residual objections, minority report, and reopen conditions. We evaluate on 45 tasks across seven domains using Gemini 2.5 Flash. On non-routine tasks (n=40), DCI significantly improves over unstructured debate (+0.95, 95% CI [+0.41, +1.54]). DCI excels on hidden-profile tasks requiring perspective integration (9.56, highest of any system on any domain) while failing on routine decisions (5.39), confirming task-dependence. DCI produces 100% structured decision packets and 98% minority reports, artifacts absent from all baselines. However, DCI consumes ~62x single-agent tokens, and single-agent generation outperforms DCI on overall quality. DCI's contribution is not that more agents are better, but that consequential decisions benefit from deliberative structure when process accountability justifies the cost.

作者初判：只决定core：typed acts/workspace/decisionpacket与guaranteedtermination要核是否原文新增条件/flow invariant，不能仅把四role/14acts和62x成本当机制贡献。

## http://arxiv.org/abs/2603.11863v2

原件：SUP_TITLES_CL_RETRY.raw

标题：CreativeBench: Benchmarking and Enhancing Machine Creativity via Self-Evolving Challenges

完整摘要：The saturation of high-quality pre-training data has shifted research focus toward evolutionary systems capable of continuously generating novel artifacts, leading to the success of AlphaEvolve. However, the progress of such systems is hindered by the lack of rigorous, quantitative evaluation. To tackle this challenge, we introduce CreativeBench, a benchmark for evaluating machine creativity in code generation, grounded in a classical cognitive framework. Comprising two subsets -- CreativeBench-Combo and CreativeBench-Explore -- the benchmark targets combinatorial and exploratory creativity through an automated pipeline utilizing reverse engineering and self-play. By leveraging executable code, CreativeBench objectively distinguishes creativity from hallucination via a unified metric defined as the product of quality and novelty. Our analysis of state-of-the-art models reveals distinct behaviors: (1) scaling significantly improves combinatorial creativity but yields diminishing returns for exploration; (2) larger models exhibit ``convergence-by-scaling,'' becoming more correct but less divergent; and (3) reasoning capabilities primarily benefit constrained exploration rather than combination. Finally, we propose EvoRePE, a plug-and-play inference-time steering strategy that internalizes evolutionary search patterns to consistently enhance machine creativity.

作者初判：窄P：可执行code的质量×novelty与reverse/self-play人口、探索/组合分离/scale收敛反侧可修正评价；objectively distinguishes不自动truth，EvoRePE策略另核实际delta。

## http://arxiv.org/abs/2603.12123v2

原件：SUP_TITLES_CL_RETRY.raw

标题：Cross-Context Review: Improving LLM Output Quality by Separating Production and Review Sessions

完整摘要：Large language models struggle to catch errors in their own outputs when the review happens in the same session that produced them. This paper introduces Cross-Context Review (CCR), a straightforward method where the review is conducted in a fresh session with no access to the production conversation history. We ran a controlled experiment: 30 artifacts (code, technical documents, presentation scripts) with 150 injected errors, tested under four review conditions -- same-session Self-Review (SR), repeated Self-Review (SR2), context-aware Subagent Review (SA), and Cross-Context Review (CCR). The central result is that a second review helps only when it happens in a fresh session: CCR (F1 28.6%) outperforms a second review in the same session (SR2, 21.7%) robustly, both in the first run (paired t, p<0.001) and in the three-run average (Holm-adjusted p=0.004). This version updates the broader comparisons. Averaged across runs, and excluding one SR run whose records could not be verified, CCR is not significantly ahead of context-aware subagent review (SA, 23.8%; p=0.057) or of a single same-session review (SR, 27.1%; p=0.26); the first version's advantages over these two baselines came from run 1. CCR needs no infrastructure and costs one extra session.

作者初判：窄P且具名纠错：当前v2明确三run更正/一个SR记录不可核，CCR对SA/SR不再显著只对SR2保持。需定点当前说明/早版主张身份，不全revisiondiff，不由摘要自动新事件或重复评分。

## http://arxiv.org/abs/2603.12165v3

原件：SUP_TITLES_CL_RETRY.raw

标题：QAQ: Bidirectional Semantic Coherence for Selecting High-Quality Synthetic Code Instructions

完整摘要：Synthetic data has become essential for training code generation models, yet it introduces significant noise and hallucinations that are difficult to detect with current metrics. Existing data selection methods like Instruction-Following Difficulty (IFD) typically assess how hard a model generates an answer given a query ($A|Q$). However, this metric is ambiguous on noisy synthetic data, where low probability can distinguish between intrinsic task complexity and model-generated hallucinations. Here, we propose QAQ, a novel data selection framework that evaluates data quality from the reverse direction: how well can the answer predict the query ($Q|A$)? We define Reverse Mutual Information (RMI) to quantify the information gain about the query conditioned on the answer. Our analyses reveal that both extremes of RMI signal quality issues: low RMI indicates semantic misalignment, while excessively high RMI may contain defect patterns that LLMs easily recognize. Furthermore, we introduce a selection strategy based on the disagreement between strong and weak models to identify samples that are valid yet challenging. Experiments across three datasets spanning code generation (WarriorCoder, Magpie-Qwen2.5-Coder-Pro-300K) and math reasoning (OpenR1-Math-220k) demonstrate that selecting just 25\% of data using stratified RMI matches full-data performance while being consistently competitive with or better than existing data selection methods. Our approach highlights the importance of bidirectional semantic coherence in synthetic data curation, offering a scalable pathway to reduce computational costs without sacrificing model capability. Code is available at https://github.com/XXSg559/QAQ.

作者初判：窄P：A|Q高难度与噪声不可辨→Q|A reverse信息增益及strong/weak分歧采样→可能改变合成instruction选择条件，极值不能自动签quality。

## http://arxiv.org/abs/2603.11287v2

原件：SUP_TITLES_SYSTEM_RETRY.raw

标题：Synthesis-in-the-Loop Evaluation of LLMs for RTL Generation: Quality, Reliability, and Failure Modes

完整摘要：RTL generation is more than code synthesis. Designs must be syntactically valid, synthesizable, correct, hardware-efficient. SOTA evaluations stop at functional correctness and do not measure synthesis and implementation quality. This paper evaluates 32 language models on 202 Verilog tasks from VerilogEval and RTLLM using the Hardware Quality Index (HQI) that combines post-synthesis area, delay, and warnings related to expert references in a Nangate45 45\,nm flow. Three performance regimes emerge: 14 frontier models achieve HQI $>$ 66, led by Gemini-3-Pro at 87.5\% coverage and 85.1 HQI; 15 models cluster 43--66 HQI; 3 are below 43. Gap between best-of-five capability and single-attempt quality spans 3.7--22.1 HQI points, limiting integration into agentic pipelines. A taxonomy of 195 synthesis failures reveals systematic divergence: proprietary models fail late through elaboration errors and synthesis timeout; open models fail early often due to missing module wrappers and non-synthesizable constructs, a pattern consistent with training corpora skewed toward simulation over synthesis-grade RTL.

作者初判：窄P：功能正确不等可综合/实现面积延时/警告，bestof5→single gap与failurestage有具体评价接口；不是32模型排行即准入或通用硬件benchmark。

## http://arxiv.org/abs/2603.11489v1

原件：SUP_TITLES_SYSTEM_RETRY.raw

标题：AutoVeriFix+: High-Correctness RTL Generation via Trace-Aware Causal Fix and Semantic Redundancy Pruning

完整摘要：Large language models (LLMs) have demonstrated impressive capabilities in generating software code for high-level programming languages such as Python and C++. However, their application to hardware description languages, such as Verilog, is challenging due to the scarcity of high-quality training data. Current approaches to Verilog code generation using LLMs often focus on syntactic correctness, resulting in code with functional errors. To address these challenges, we propose AutoVeriFix+, a novel three-stage framework that integrates high-level semantic reasoning with state-space exploration to enhance functional correctness and design efficiency. In the first stage, an LLM is employed to generate high-level Python reference models that define the intended circuit behavior. In the second stage, another LLM generates initial Verilog RTL candidates and iteratively fixes syntactic errors. In the third stage, we introduce a Concolic testing engine to exercise deep sequential logic and identify corner-case vulnerabilities. With cycle-accurate execution traces and internal register snapshots, AutoVeriFix+ provides the LLM with the causal context necessary to resolve complex state-transition errors. Furthermore, it will generate a coverage report to identify functionally redundant branches, enabling the LLM to perform semantic pruning for area optimization. Experimental results demonstrate that AutoVeriFix+ achieves over 80% functional correctness on rigorous benchmarks, reaching a pass@10 score of 90.2% on the VerilogEval-machine dataset. In addition, it eliminates an average of 25% redundant logic across benchmarks through trace-aware optimization.

作者初判：只决定core：referencePython→RTLfix→concolic traces/coverage pruning是否新验证反馈约束，需核causal是否只是轨迹提示、reference谁签真值，不能模块组合自动贡献。
