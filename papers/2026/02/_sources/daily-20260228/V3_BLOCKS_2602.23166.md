[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: AgentVista : Evaluating Multimodal Agents in Ultra-Challenging Realistic Visual Scenarios

[3] h6: Abstract

[4] p: Real-world multimodal agents solve multi-step workflows grounded in visual evidence. For example, an agent can troubleshoot a device by linking a wiring photo to a schematic and validating the fix with online documentation, or plan a trip by interpreting a transit map and checking schedules under routing constraints. However, existing multimodal benchmarks mainly evaluate single-turn visual reasoning or specific tool skills, and they do not fully capture the realism, visual subtlety, and long-horizon tool use that practical agents require. We introduce AgentVista , a benchmark for generalist multimodal agents that spans 25 sub-domains across 7 categories, pairing realistic and detail-rich visual scenarios with natural hybrid tool use. Tasks require long-horizon tool interactions across modalities, including web search, image search, page navigation, and code-based operations for both image processing and general programming. Comprehensive evaluation of state-of-the-art models exposes significant gaps in their ability to carry out long-horizon multimodal tool use. Even the best model in our evaluation, Gemini-3-Pro with tools, achieves only 27.3% overall accuracy, and hard instances can require more than 25 tool-calling turns. We expect AgentVista to accelerate the development of more capable and reliable multimodal agents for realistic and ultra-challenging problem solving.

[5] h6: Keywords:

[6] p: Website: agentvista-bench.github.io github.com/hkust-nlp/AgentVista

[7] h2: 1 Introduction

[8] p: Humans seamlessly integrate multi-sensory information to tackle complex real-world problems ( Stein, 2012 ) . With the rapid evolution of AI agents ( Wang et al., 2024a ; Comanici et al., 2025 ; OpenAI, 2025f ; Team et al., 2026 ) , developing visual agentic intelligence becomes essential. For instance, an agent is expected to assist in shopping by scanning shelf products and retrieving nutritional information to satisfy user health constraints, or support troubleshooting by linking malfunction photos with schematic diagrams to diagnose specific faults. However, a major challenge in developing such multimodal agents is the absence of a benchmark based on realistic scenarios that covers the diversity and complexity of long-horizon tool interactions across different modalities, which limits reliable evaluation of agent capabilities in open domains ( Xie et al., 2024 ; Li et al., 2025a ) .

[9] figure: Figure 1 : A representative AgentVista task grounded in a real home-renovation scenario. The agent needs to match flooring styles across images, verify the target room, retrieve product specifications, and compute final cost via interleaved tool use.

[10] figure: Figure 2 : Sampled AgentVista examples from each domain. Each query is grounded in complex, real-world visual scenes and is designed to elicit agentic tool use with multi-step reasoning toward a unique, verifiable answer.

[11] p: Traditional multimodal benchmarks ( Antol et al., 2015 ; Hudson and Manning, 2019 ; Yue et al., 2024b ; Wang et al., 2024b ; Scale AI, 2025 ) focus on assessing visual perception and complex reasoning capabilities. Recently, a growing number of benchmarks have emerged to evaluate multimodal agentic behaviors ( Ma et al., 2024 ; Li et al., 2025b ; Ashraf et al., 2025 ; Guo et al., 2025 ; Tao et al., 2025 ; Geng et al., 2025 ) . However, these evaluations typically present two main gaps: ❶ Capability-Specific Evaluation : They typically emphasize particular capabilities, focusing on skills such as visual manipulation ( Wang et al., 2025 ; Lai et al., 2025 ) , web browsing ( Li et al., 2025c ; Tao et al., 2025 ) , or code generation ( Yang et al., 2024 ) . This narrow focus makes it difficult to evaluate generalist agents that must combine multiple skills and remain reliable in long-horizon workflows. ❷ Trade-off between Realism and Difficulty : Practical agent tasks are difficult because they combine cluttered visual evidence with long-horizon tool use under constraints. Yet many benchmarks increase difficulty by simplifying the visual state or by relying on tool patterns that deviate from everyday workflows, which can shift the bottleneck away from realistic grounding and interaction. For example, VisualToolBench pre-processes the input images to facilitate specific visual operations ( Guo et al., 2025 ) . While this design is effective for evaluating visual manipulation, it also shifts the problem from reasoning over natural visual states to operating on curated inputs.

[12] figure: Table 1: Comparison with representative multimodal agent benchmarks. Operation abbreviations: VO. (Visual Operations), VS. (Visual Search), TS. (Text Search), and CE. (Code Execution). Tool categories are based on the tools and signals used in these benchmarks. “# Turns” reports the average number of tool-calling turns by GPT-5 , used as a proxy for task complexity. Benchmark VO. VS. TS. CE. Multi Image # Turns TIR-Bench ✓ ✗ ✗ ✓ ✓ 2.92 Agent-X ✓ ✗ ✓ ✓ ✓ 3.4 MMSearch-Plus ✗ ✓ ✓ ✗ ✓ 4.6 BrowseComp-VL ✗ ✓ ✓ ✓ ✗ 4.3 VisualToolBench ✓ ✗ ✓ ✓ ✗ 4.46 AgentVista (Ours) ✓ ✓ ✓ ✓ ✓ 12.67

[13] p: To address these gaps, we introduce AgentVista , a benchmark designed to evaluate generalist multimodal agents on diverse, realistic, and challenging tasks. AgentVista contains 209 tasks spanning 25 sub-domains across 7 categories, including commerce, geography, society, technology, entertainment, culture, and academics, and grounds each query in detail-rich visual states such as daily photos, screenshots, and technical diagrams, with both single-image and multi-image inputs. Each query is manually authored to reflect authentic user intent and is subjected to strict quality control, where every instance is carefully reviewed to ensure mandatory visual dependence and a unique, verifiable answer. Every task requires long-horizon interaction with interleaved tools, where the agent repeatedly grounds visual cues, retrieves external information, and verifies intermediate decisions. Table 1 summarizes the key differences between AgentVista and representative agentic multimodal benchmarks. Figure 1 shows a representative example from AgentVista motivated by a real home renovation need: the agent need to match flooring styles across scenes, verify the target room with image-based checks, retrieve product specifications online, and compute a deterministic final cost from the room size and packaging information.

[14] p: AgentVista is evaluated in a controlled yet practical setting, we adopt four widely used tools that cover the core interaction patterns of real-world multimodal agents, including web search, image search, page navigation, and code-based operations for both image processing and general programming. Our experiments on representative open-source and commercial MLLMs show that AgentVista remains far from being solved, leaving substantial room for improvement. Even the best performance in our evaluation, Gemini-3-Pro , achieves only 27.3% overall accuracy. Further error analysis shows that many failures start with visual misidentification and then lead to wrong retrieval and unreliable tool use over many steps. To facilitate future research, we will release both the AgentVista benchmark and a lightweight yet general agent framework to facilitate reproducible evaluation and accelerate progress on long-horizon multimodal tool use.

[15] h2: 2 The AgentVista

[16] figure: Figure 3 : Overview of the AgentVista dataset construction pipeline, consisting of agent-centric filtering, expert finalization, execution filtering, and two-round verification to produce realistic and ultra-challenging multimodal agent tasks.

[17] figure: Figure 4 : The categorization of AgentVista . The benchmark spans 7 major categories and 25 sub-domains, covering a broad range of realistic and challenging multimodal agent scenarios. Category abbreviations: Comm. (Commerce), Geog. (Geography), Ent. (Entertainment), Tech. (Technology), Soc. (Society), Acad. (Academics), and Cult. (Culture).

[18] h3: 2.1 Overview of AgentVista

[19] p: We introduce AgentVista , a benchmark for evaluating generalist multimodal agents on realistic and ultra-challenging tasks. AgentVista focuses on realistic user requests that are still hard in practice and require long-horizon tool use grounded in visual evidence. AgentVista contains 209 tasks spanning 25 sub-domains across 7 categories: Technology, Commerce, Geography, Entertainment, Society, Academics, and Culture. The domain distribution and dataset composition are summarized in Table 2 and Figure 4 . As shown in Figure 2 , tasks are built from authentic user needs and require multi-step reasoning with tool use. For example, an agent may need to read key constraints from a photo or screenshot, retrieve missing details from external resources, and then combine multiple pieces of evidence to produce the final answer. This includes diagnosing a hardware issue by matching visible components to technical documentation, selecting a product that satisfies allergy and nutrition constraints by comparing labels with online specifications, and planning a route under time and transit limits by reading schedules from images and verifying them with web search. To enable robust and scalable evaluation, each instance is paired with a clear and deterministic ground truth answer, typically a short phrase or a numeric value.

[20] figure: Table 2 : Summary statistics of the AgentVista benchmark. Statistic Number Total queries 209 Total images 308 Primary categories 7 Secondary categories 25 Average query length 401.4 Average answer length 40.8 Image distribution - Single-image queries 151 (72.2%) - Multi-image queries 58 (27.8%)

[21] h3: 2.2 Data Construction

[22] h4: 2.2.1 Core Design Principles

[23] p: We design AgentVista based on three principles:

[24] p: Vision-centric tasks with realistic images. Each task requires obtaining the key evidence from the visual input. The images are real and contain visual details to support visual understanding, such as small but important cues, multiple related objects, or subtle differences across views. The query avoids stating the key information in text and avoids questions that can be answered by a keyword search. These constraints ensure that solving the task relies on understanding and comparison of visual details, rather than on textual shortcuts.

[25] p: Natural interleaved hybrid tool use. Each task requires using different tool types together, and the interaction must include interleaved tool calls across at least two tool categories. The intended solution should mix visual tools and text-based tools, such as using image search or image processing to gather visual evidence, then using web search or page navigation to retrieve needed facts, and finally combining the evidence to reach the answer. Tool use must follow natural and real-world workflows. Each tool call should be necessary for solving the task, rather than added only to make the interaction longer. To keep tasks realistic and challenging, we favor instances that require grounding tool outputs in the visual input under explicit constraints.

[26] p: Easy to verify and stable over time. Following recent evaluation protocols ( Li et al., 2025c ; Wei et al., 2025 ) , each task has a concise target answer in a fixed format, such as a number, an entity name, or a short description. This design makes the evaluation process simple and accurate, similar to math tasks. Additionally, we address the issue of information changing over time. Annotators verify facts against reliable sources. When necessary, we include specific time constraints in the question to ensure the ground truth remains valid.

[27] h4: 2.2.2 Dataset Creation Pipeline

[28] p: We build AgentVista from 300k+ real images and real user needs collected from public model arenas, annotator-captured daily scenarios, and private community forums, with details in Appendix A.2 . The dataset construction pipeline is shown in Figure 3 .

[29] h5: Stage 1: Agent-centric filtering.

[30] p: We start with model-assisted mining and filtering to identify candidate initial states that reflect realistic daily workflows. We first use Claude-Opus-4 to filter the raw image pool by removing cases with limited visual information or weak agentic potential, such as pure OCR screenshots, single-object landmark photos, and images that can be solved without meaningful visual reasoning. We provide Claude-Opus-4 with our tool schema and ask it to propose an initial task query that is compatible with the available tools and has a verifiable answer format. The proposed query serves as a candidate starting point for downstream curation. We then apply human screening to retain only images with sufficiently rich visual evidence and queries that support a natural task formulation with hybrid tool use. To avoid simple cases, we prioritize candidates with non-trivial constraints and keep only those that naturally require multi-step reasoning rather than a single direct lookup.

[31] h5: Stage 2: Expert finalization.

[32] p: We recruit and train expert annotators on the project scope, taxonomy, and quality requirements, and ask them to finalize each candidate produced in Stage 1. Starting from the image and the initial query, annotators rewrite the query into a realistic user request while keeping it self-contained and vision-centric. Realism is enforced by preserving the original visual state and intent, and by expressing constraints in the way users typically specify them, such as time, budget, compatibility, and safety requirements. To make tasks ultra-challenging in a natural way, annotators select cases where the answer depends on fine-grained visual cues and cannot be obtained by a single direct lookup. They ensure that solving the task requires combining visual evidence with information gathered from tools, and that the process includes necessary interleaving across tool types. Annotators then produce a deterministic target answer and record the key evidence and tool steps used to obtain it, which enables later checking.

[33] h5: Stage 3: Execution filtering.

[34] p: We validate each instance by executing the candidate task in our tool environment and checking that the annotated answer is supported by reproducible tool outputs. During this process, we run Gemini-3-Flash in the same tool environment to screen for tool-use diversity, and we retain only tasks that require interleaved calls across at least two categories. Furthermore, we run Gemini-2.5-Pro with tool access disabled and remove samples that can be solved from the prompt alone.

[35] h5: Stage 4: Two-round verification.

[36] p: Finally, we conduct two rounds of verification. The first round removes instances with insufficient visual evidence, weak visual dependency, or questionable answer validity. In the second round, a separate group re-checks each instance by following the evidence and tool steps recorded by annotators, and confirms that the final answer is supported by the visual cues and the tool outputs. Instances with unclear evidence, unstable answers, or unrealistic workflows are removed. The remaining instances form the final AgentVista benchmark.

[37] figure: Table 3 : Main results on our proposed AgentVista . Domain abbreviations: Comm. (Commerce), Geog. (Geography), Ent. (Entertainment), Tech. (Technology), Soc. (Society), Acad. (Academics), and Cult. (Culture). Input mode abbreviations: Single. (Single-image input) and Multi. (Multi-image input). The best-performing model in each category is in-bold , and the second best is underlined . Overall, Gemini-3-Pro achieves the highest accuracy among all evaluated models. All values are accuracies in %. Model By Category By Input Mode Summary Comm. Geog. Ent. Tech. Soc. Acad. Cult. Single. Multi. Overall # Turns Qwen3-VL-235B 7.14 7.69 7.69 26.47 16.00 20.00 13.33 11.84 15.79 12.92 2.34 GPT-4.1 16.67 15.38 10.26 29.41 20.00 20.00 13.33 15.13 24.56 17.70 1.74 o3 21.43 15.38 7.69 23.53 40.00 26.67 13.33 17.76 26.32 20.10 13.18 o4-mini 2.38 10.26 2.56 8.82 8.00 13.33 0.00 6.58 5.26 6.22 1.89 GPT-5 23.81 23.08 12.82 35.29 28.00 26.67 26.67 24.34 24.56 24.40 12.67 GPT-5.1 23.81 12.82 15.38 26.47 24.00 40.00 40.00 19.74 31.58 22.97 17.14 GPT-5.2 21.43 17.95 20.51 38.24 24.00 33.33 20.00 23.03 28.07 24.40 13.85 Grok-4 11.90 23.08 7.69 20.59 28.00 0.00 0.00 13.82 17.54 14.83 16.44 Claude-Sonnet-4 9.52 15.38 2.56 29.41 16.00 20.00 6.67 11.18 21.05 13.88 5.37 Claude-Opus-4 19.05 12.82 5.13 26.47 20.00 20.00 6.67 11.84 26.32 15.79 6.89 Claude-Opus-4.1 11.90 23.08 10.26 29.41 16.00 26.67 13.33 16.45 22.81 18.18 7.28 Claude-Sonnet-4.5 11.90 23.08 7.69 26.47 24.00 20.00 13.33 17.11 19.30 17.70 9.99 Gemini-3-Flash 16.67 17.95 10.26 29.41 28.00 40.00 20.00 18.42 28.07 21.05 7.78 Gemini-3-Pro 16.67 28.21 20.51 32.35 32.00 40.00 40.00 23.68 36.84 27.27 6.67

[38] h5: Filtering statistics.

[39] p: We begin with 300k+ candidate images. Stage 1 uses model-assisted filtering and human screening to select 568 potential initial states, 0.19% of the raw pool. Stage 2 expert finalization yields 315 tasks after rewriting the initial queries into realistic user requests and adding deterministic target answers. Stage 3 execution filtering retains 241 tasks by validating reproducible tool outputs, enforcing interleaved calls across at least two tool categories, and removing tasks solvable when tool access is disabled. Stage 4 two-round verification selects the final 209 tasks by re-checking visual evidence, recorded tool steps, and answer validity. On average, constructing a single instance takes about 4 hours, and expert annotators take about 30 minutes to solve an instance.

[40] h4: 2.2.3 Tool environment

[41] p: AgentVista supports a compact set of tools that cover common multimodal agent workflows. Models can call web_search to retrieve web pages, visit to open and navigate a page, and image_search to locate images when a query requires external visual references. We also provide code_interpreter , which supports both programming and image processing. It enables arithmetic and parsing, structured extraction, and operations such as cropping, resizing, measuring, and comparing visual regions when needed. All tools are exposed with detailed descriptions and structured inputs and outputs, so the model can decide when to call a tool and how to use the returned results. Detailed tool definitions are provided in Appendix B.1 .

[42] h2: 3 Experiments

[43] h3: 3.1 Experimental Setup

[44] h5: Models.

[45] p: We evaluate a broad set of frontier multimodal models that are commonly used as generalist agents. Specifically, we test GPT-4.1 ( OpenAI, 2025a ) , o3 , o4-mini ( OpenAI, 2025e ) , GPT-5 ( OpenAI, 2025d ) , GPT-5.1 ( OpenAI, 2025b ) , GPT-5.2 ( OpenAI, 2025c ) , Gemini-3-Flash ( Google DeepMind, 2025b ) , Gemini-3-Pro ( Google DeepMind, 2025a ) , Grok-4 ( xAI, 2025 ) , Claude-Sonnet-4 ( Anthropic, 2025a ) , Claude-Opus-4.1 ( Anthropic, 2025b ) , Claude-Sonnet-4.5 ( Anthropic, 2025c ) , and Qwen3-VL-235B-A22B ( Bai et al., 2025 ) .

[46] h5: Evaluation Setup.

[47] p: For all experiments, we use a temperature of 0.6 and cap the tool interaction budget at 30 turns for every model. Since AgentVista provides concise target answers in deterministic formats, evaluation reduces to verifying the final answer. We use GPT-4.1 as a fixed judge model to assess whether a model’s final response matches the annotated ground truth under the required format. We report accuracy as the evaluation metric.

[48] h3: 3.2 Main Results

[49] p: We report the overall performance in Table 3 . We make the below three observations.

[50] h5: AgentVista is ultra-challenging.

[51] p: The results show that AgentVista remains difficult for current multimodal agents. Even the best-performing model, Gemini-3-Pro , achieves 27.27% overall accuracy, indicating substantial headroom. Performance is also low for a large portion of models: 4 out of 14 models score below 15% overall accuracy. These results suggest that agents still have significant room for improvement in complex long-horizon settings that require multi-step tool use grounded in real visual evidence. The average number of turns further reflects this difficulty. For example, GPT-5.2 uses 13.85 turns on average, and 5 out of 14 models exceed 10 turns on average, indicating that many tasks require extended multi-step interactions rather than a short tool sequence. We also observe a sizable gap between the open-source model Qwen3-VL-235B and the closed-source models, suggesting substantial room for open-source multimodal agents. We report additional open-source baselines in Appendix B.2 . We further analyze common failure patterns in Section 4.3 .

[52] h5: Domain strengths differ across model families.

[53] p: Performance varies noticeably across categories, revealing complementary strengths among model series. The GPT-5 family shows strong coverage on practical categories, with GPT-5.2 performing best on Technology and tying for the best score on Entertainment , while GPT-5 and GPT-5.1 lead Commerce . The Gemini series is strongest overall: Gemini-3-Pro achieves the highest overall accuracy, leads Geography , and performs competitively on Society and Culture . Claude models are comparatively stronger on categories that emphasize careful reading and constraint following, with their best results appearing in Technology and Geography . Overall, these results suggest that current agents do not yet provide uniform competence across domains, and improving broad, consistent performance across realistic long-horizon tasks remains an open challenge.

[54] h5: Multi-image inputs are not uniformly harder than single image inputs.

[55] p: For nearly all evaluated models, accuracy with multi-image inputs is higher than with single-image inputs. The gain is especially large for Gemini-3-Pro , which improves from 23.68% under single-image input to 36.84% under multi-image input. This pattern matches how our multi-image instances are constructed. Additional views often provide complementary evidence, reduce ambiguity, and reveal details that are missing in a single shot, which can make grounding and downstream retrieval more reliable. While multi-image inputs still require cross-image alignment, the results suggest that the main bottleneck remains long-horizon tool use and constraint tracking, rather than the presence of multiple images itself.

[56] h2: 4 Further Analysis

[57] figure: Figure 5 : Tool-use distribution across models. GPT models rely more on the code interpreter, while Gemini and Claude models use web search most frequently.

[58] h3: 4.1 Tool Distribution Analysis

[59] p: In this section, we analyze the distribution of tool calls across models. As shown in Figure 5 , the GPT-5 series relies most heavily on the code interpreter. We further break down code interpreter calls by operation type in Figure 6 . The results suggest that these models more often perform image-centric operations during problem solving, such as zooming in, cropping, resizing, measuring regions, and carrying out structured extraction or calculations. Across the inspected models, crop is the most frequent operation, indicating that many trajectories depend on localized visual grounding before proceeding to retrieval or computation. Second, the Gemini and Claude series call web search most often, indicating a stronger preference for retrieval-driven workflows. Across all models, image search is used less frequently than the other tools. In the next tool ablation study, we quantify how each tool contributes to performance and how accuracy changes when a tool is removed.

[60] figure: Figure 6 : Image manipulation operation distribution of code interpreter calls across four multimodal models. Tool usages are automatically categorized into image-editing and analysis-related types. Across models, crop is the most frequent operation, suggesting that many interactions rely on localized visual grounding before further reasoning.

[61] h3: 4.2 Tool Ablation Study

[62] p: In this section, we ablate tool access to quantify how each tool modality contributes to performance.

[63] h5: Experimental setup.

[64] p: We evaluate three settings with prompts lightly adapted to reflect the available capabilities, while keeping the evaluation protocol and inference hyperparameters fixed. ❶ Vision only : the agent has access only to a visual manipulation environment, enabling image processing operations for inspection and transformation, but no external retrieval. ❷ Search only : the agent can retrieve external evidence through both image-based and text-based search, and can read retrieved webpages, but cannot perform tool-based visual manipulation or programmatic verification. ❸ No tool : the agent relies purely on direct generation without any tool assistance.

[65] figure: Figure 7 : Tool ablation on Gemini-3-Pro and Claude-Sonnet-4.5 . Both models perform best with the full tool suite, highlighting the importance of combining visual manipulation and retrieval.

[66] h5: Key findings.

[67] p: Figure 7 shows that using the full tool suite yields the best performance for both models, confirming that AgentVista rewards hybrid workflows that combine visual manipulation and retrieval. For Gemini-3-Pro , the full tool setting reaches 27.27% accuracy, higher than the vision-only setting at 20.10% and the no-tool setting at 18.18%. For Claude-Sonnet-4.5 , the full tool setting achieves 17.70%, slightly above the vision-only setting at 17.22%, while the search-only and no-tool settings both drop to 13.40%. We also find that the role of retrieval differs across models. For Gemini-3-Pro , the search-only setting reaches 26.32%, close to the full tool setting. This suggests that its strong visual perception enables it to extract reliable cues from images and benefit primarily from retrieval and page navigation, while visual manipulation mainly supports inspection and verification. In contrast, Claude-Sonnet-4.5 relies more on visual manipulation than retrieval, since the vision-only setting remains close to the full tool setting, whereas the search-only setting degrades substantially.

[68] figure: Figure 8 : Error category distribution on AgentVista across four multimodal models. Error types are automatically labeled by Gemini-3-Flash based on model trajectories. Across all models, visual misidentification is the dominant failure mode, indicating that many errors originate from incorrect grounding on fine-grained visual evidence.

[69] h3: 4.3 Error Analysis

[70] p: To understand the main bottlenecks on AgentVista , we analyze failures from four representative models. For each incorrect case, we assign an error label, including tool execution failure, visual misidentification, knowledge hallucination, calculation error, instruction misinterpretation, and others. The labels are generated by Gemini-3-Flash based on the model trajectories, and the distributions are shown in Figure 8 . Detailed definitions for each error type are provided in Appendix C . Figure 8 shows a clear trend that visual misidentification is the main failure mode across all models. This aligns with the design of AgentVista , where tasks are grounded in realistic and cluttered visual states and often depend on small but critical details. From bad cases, we find that frontier agents can often zoom in to the relevant region, but they still fail when the image is blurry or the key cue is visually subtle. Knowledge hallucination is the second most common error type, which also matches our benchmark design. Many tasks require applying diverse world knowledge to long-horizon tool interactions, and current models still struggle to resolve long-tail facts reliably even with web search. We include representative good and bad cases with detailed explanations in Appendix D . Overall, these results suggest that AgentVista can expose practical weaknesses in both fine-grained visual understanding and knowledge-grounded reasoning under realistic tool use.

[71] h3: 4.4 Test Time Scaling

[72] figure: Table 4: Test-time scaling results under different sampling budgets K K on Gemini-3-Flash . We report Random1@ K K as a lower bound, Best-of- K K (BoN@ K K ) selected by a reward model, and Pass@ K K as an upper bound. All values are accuracies in %. Setting K = 1 K{=}1 K = 2 K{=}2 K = 4 K{=}4 K = 8 K{=}8 K = 16 K{=}16 Random1@ K K 21.05 19.11 18.23 17.09 18.05 BoN@ K K 21.05 24.88 26.32 28.23 30.62 Pass@ K K 21.05 26.07 34.22 42.59 51.67

[73] p: To study whether additional sampling at test time can improve performance on AgentVista , we evaluate test-time scaling on Gemini-3-Flash . We generate K K independent solutions per instance and use Gemini-3-Flash as the reward model to select a final answer when selection is required. We follow the same evaluation protocol as in prior experiments. Table 4 reports three settings: Random1@ K K , which randomly selects one of the K K samples as a lower bound, Best-of- K K ( BoN@ K K ), which selects the highest-scoring sample under the reward model, and Pass@ K K , which measures whether at least one of the K K samples is correct as an upper bound.

[74] h5: Key findings.

[75] p: Table 4 shows that test-time scaling consistently improves performance. Under BoN , accuracy increases from 21.05% at K = 1 K{=}1 to 30.62% at K = 16 K{=}16 . The upper bound rises even more, with Pass@ K K increasing from 21.05% at K = 1 K{=}1 to 51.67% at K = 16 K{=}16 . In contrast, Random1@ K K remains low and does not improve with larger K K , indicating that gains mainly come from better selection rather than sampling alone. Despite these improvements, scaling alone is not sufficient to solve AgentVista . Even at K = 16 K{=}16 , BoN reaches only 30.62%, while Pass@ 16 16 is 51.67%. This gap indicates substantial room for reinforcement learning or other optimization methods that can better close the gap between selection and the achievable upper bound, and more broadly highlights the need for stronger long-horizon tool use and more reliable visual grounding.

[76] h2: 5 Related Work

[77] h3: 5.1 Multimodal Agents and Tool Use

[78] p: Recent years have witnessed rapid progress in large multimodal models that combine visual perception with language-based reasoning ( Peng et al., 2023 ; Liu et al., 2023 ; Zhu et al., 2023 ; Li et al., 2023 ) . A key step toward practical multimodal agents is to couple these models with tools so they can inspect visual evidence, verify intermediate hypotheses, and refine solutions over multiple steps. OpenAI o3 and o4-mini follow this direction by manipulating user-provided images during reasoning through operations such as cropping, zooming, and rotation, and coordinating these visual operations with other tools when needed ( OpenAI, 2025f ) . This paradigm has inspired open systems that study tool-driven multimodal reasoning and long-horizon interaction ( Su et al., 2025a ; Su et al., 2025b ) . Recent work also explores stronger training signals for repeated grounding, such as reinforcement learning for interleaved perception and reasoning ( Zheng et al., 2025 ) , and extends multimodal agents with web and code tools for mixed tool use in realistic settings ( Hong et al., 2025 ; Geng et al., 2025 ) . Despite this progress, there is still no benchmark that evaluates generalist multimodal agents on realistic, ultra-challenging tasks. AgentVista fills this gap by focusing on long-horizon, interleaved tool use grounded in real visual inputs.

[79] h3: 5.2 Multimodal Agent Benchmarks

[80] p: Early multimodal benchmarks mainly evaluate perception and visual reasoning in static question answering, where models respond from a fixed image and text context without interaction ( Antol et al., 2015 ; Hudson and Manning, 2019 ; Lu et al., 2023 ; Yue et al., 2024a ; Wang et al., 2024b ) . While useful, they do not test whether an agent can choose actions, call tools, and verify intermediate results. Recent agent benchmarks add tool use, including multi-step planning ( Ma et al., 2024 ) , web browsing and search ( Li et al., 2025c ; Tao et al., 2025 ) , and tool-assisted visual reasoning and active perception ( Wu and Xie, 2024 ; Lai et al., 2025 ; Li et al., 2025b ; Ashraf et al., 2025 ) . More recent works further move toward interleaved tool settings, but the visual evidence is often relatively clean or lightweight, which makes perception less demanding, and the resulting tool trajectories tend to be shorter and less diverse ( Guo et al., 2025 ; Hong et al., 2025 ; Chen et al., 2026 ) . AgentVista addresses this gap by emphasizing realistic visual inputs and long-horizon workflows that require repeated visual checking and interleaved use of multiple tool types.

[81] h2: 6 Conclusion

[82] p: We introduce AgentVista , a benchmark for evaluating generalist multimodal agents on realistic, ultra-challenging tasks that require long-horizon, interleaved tool use grounded in visual evidence. AgentVista contains 209 tasks spanning 25 sub-domains across 7 categories, with strict quality control to ensure vision-centric queries and unique, verifiable answers. Experiments across frontier models show that AgentVista is far from solved: even the best-performing model, Gemini-3-Pro , reaches only 27.3% overall accuracy. The benchmark also elicits long interaction trajectories, with models such as GPT-5.2 averaging 13.85 tool turns per task, indicating substantial complexity beyond short tool chains. Further analysis highlights visual grounding and long-horizon tool use as key bottlenecks for current multimodal agents. We hope AgentVista provides a practical benchmark for tracking progress and motivates the development of multimodal agents that can solve complex, multi-step real-world tasks more reliably.

[83] h2: Impact Statement

[84] p: This work introduces AgentVista , a benchmark for evaluating generalist multimodal agents on realistic, ultra-challenging tasks that require long-horizon tool use grounded in real visual inputs. By using concise, verifiable answers and a controlled tool environment, AgentVista enables reproducible comparisons and helps identify key bottlenecks in visual grounding, constraint tracking, and tool reliability. Improved multimodal agents could benefit practical applications such as shopping assistance, travel planning, and troubleshooting from user photos, where agents must combine visual evidence with online information and computation. At the same time, stronger agents may increase risks of privacy leakage from user-provided images and overconfident but incorrect outputs in real deployments. We mitigate these concerns by filtering and rewriting tasks to avoid personal identifiers when applicable, and by emphasizing short answers that encourage checkable evaluation rather than persuasive free-form text.

[85] p: Benchmark construction can also reflect biases from source data and annotator decisions, which may affect coverage across domains and scenarios. We hope AgentVista supports future work on more robust and responsible multimodal agents by providing a shared evaluation target for realistic, long-horizon tool use.

[86] h2: References

[87] h2: Appendix A AgentVista Details

[88] h3: A.1 Dataset Taxonomy of AgentVista

[89] p: AgentVista covers seven major categories: (1) Technology , which includes hardware troubleshooting, engineering analysis, and system configuration grounded in real photos, screenshots, and diagrams; (2) Commerce , which includes product selection, pricing and budget calculation, and finance-related reasoning under practical constraints; (3) Geography , which includes route planning, map interpretation, location identification, and spatial calculations; (4) Entertainment , which includes sports analytics, media and hobby curation, and game-related reasoning; (5) Society , which includes everyday tasks such as health and culinary decisions, home maintenance, manual assembly troubleshooting, and plant care; (6) Academics , which includes mathematical computation, scientific identification, and data analysis; and (7) Culture , which includes cultural knowledge, history-related understanding, and artifact appraisal grounded in visual evidence.

[90] h3: A.2 Data Sources

[91] p: All AgentVista instances are grounded in real images and real user needs. Across all sources, we apply a unified set of criteria. We retain only images with sufficient visual detail to support non-trivial reasoning, and we exclude cases where the solution can be obtained by directly searching the query text or by retrieving the same image and question from the public web. We curate candidates from three channels.

[92] h5: Public user-submitted arenas.

[93] p: We collect image-based user submissions from public vision-language model arenas, including VisionArena and WildVision ( Chou et al., 2025 ; Lu et al., 2024 ) . This source provides 284.4K images with diverse real-world scenes. We first apply an automated filter using Claude-Opus-4.1 to remove images with limited visual information and cases that do not fit agentic problem settings. The filter also proposes a candidate task query that reflects the plausible action space. The prompt is shown in Appendix B.3.1 . Human annotators then select high-quality candidates for downstream curation.

[94] h5: Annotator-captured real-life scenarios.

[95] p: We also include tasks collected by annotators from real daily situations, together with the original photos or screenshots that motivated the request. This channel naturally captures practical constraints, such as cluttered scenes, partial evidence, and ambiguous context, which are common in real deployments. We treat these instances as first-party user needs and keep their intent while ensuring the final task remains self-contained.

[96] h5: Private community forums.

[97] p: We also curate candidates from community help-seeking forums. We collect posts that include visually informative images and reflect realistic user goals. Since these posts often contain lengthy discussions and personal details, we rewrite each case into a standalone task while preserving the original intent and removing identifying information. We apply stricter screening to ensure clarity and consistency with our benchmark standards.

[98] h2: Appendix B Experimental Details

[99] h3: B.1 Tool Definition

[100] p: AgentVista is evaluated in a controlled tool environment with a compact set of commonly used tools for multimodal agent workflows. Models can invoke these tools appropriately within the <tool_call>...</tool_call> block during interaction. In detail, our tools are defined as follows.

[101] h3: B.2 Analysis of open-source model results.

[102] figure: Table 5 : Results of representative open-source models on AgentVista by category. Domain abbreviations: Comm. (Commerce), Geog. (Geography), Ent. (Entertainment), Tech. (Technology), Soc. (Society), Acad. (Academics), and Cult. (Culture). The best-performing model in each category is in-bold , and the second best is underlined . All values are accuracies in %. Model Comm. Geog. Ent. Tech. Soc. Acad. Cult. Overall Qwen3-VL-235B 7.14 7.69 7.69 26.47 16.00 20.00 13.33 12.92 DeepEyes-v2-7B 9.52 10.26 2.56 14.71 24.00 6.67 20.00 11.48 WebWatcher-32B 0.00 10.26 0.00 23.53 24.00 20.00 0.00 10.05

[103] p: Table 5 reports results for three representative open-source multimodal models. In particular, DeepEyes-v2-7B ( Hong et al., 2025 ) and WebWatcher-32B ( Geng et al., 2025 ) are tool-using open-source agents that can interact with external tools to support multi-step problem solving, while Qwen3-VL-235B serves as a strong open-source multimodal backbone. Overall, these open-source baselines remain far from solving AgentVista , i.e., their overall accuracy ranges from 10.05% to 12.92%, substantially lower than the best-performing model Gemini-3-Pro at 27.3%. This gap further reflects the ultra-challenging nature of AgentVista and highlights the large room for improving open-source multimodal agents.

[104] h3: B.3 Prompts

[105] h4: B.3.1 Prompts for Data Construction

[106] h4: B.3.2 The Prompt for Evaluation

[107] h2: Appendix C Error type definitions.

[108] p: In Section 4.3 , we report the error distributions of representative models on AgentVista . Here we define the error types used in our taxonomy.

[109] h5: Tool execution failure.

[110] p: This category captures cases where the agent follows a plan, but fails due to issues in tool interaction. Typical examples include empty tool outputs, invalid requests, and failures to open or parse retrieved content. These errors suggest that robust tool use and self-checking are important for completing long-horizon workflows.

[111] h5: Visual misidentification.

[112] p: This category includes errors caused by incorrect visual understanding, such as reading the wrong text on a label, confusing similar components, missing a small indicator, or miscounting objects. Because visual evidence often determines what to search for and how to apply constraints, a single perception mistake can cause later steps to follow an incorrect direction.

[113] h5: Knowledge hallucination.

[114] p: This category refers to cases where the agent outputs facts that are not supported by the provided images or retrieved sources. Common patterns include inventing details that look plausible, relying on generic rules of thumb, or asserting standards that do not match the evidence in the current instance. These failures indicate insufficient grounding in the multimodal context.

[115] h5: Calculation error.

[116] p: This category covers mistakes in arithmetic or multi-step aggregation, such as wrong unit conversions, incorrect date computations, or errors when combining multiple retrieved values. These cases often arise after several steps, when the agent must keep intermediate numbers consistent while continuing to use tools.

[117] h5: Instruction misinterpretation.

[118] p: This category includes failures to follow the user request or constraints, such as ignoring a time window, missing a required format, applying the wrong condition, or answering a related but different question. Even when perception and retrieval are correct, misunderstanding the intent can still lead to an incorrect final answer.

[119] h5: Others.

[120] p: This category groups remaining failures that do not fit the above types or that involve multiple types without a clear primary cause. Examples include incomplete final answers, premature termination, inconsistent outputs across steps, or cases where the model produces an answer that cannot be checked against the required format. We use this bucket to keep the taxonomy simple while still accounting for long-tail error patterns.

[121] h2: Appendix D Case Study

[122] p: In this section, we present representative trajectories to illustrate both successful and failed behaviors on AgentVista . We first show a good-case example that demonstrates effective long-horizon, interleaved tool use. We then provide one bad-case example for each error type, highlighting how different failure modes arise and how they derail the overall workflow.

[123] h3: D.1 Good Case Examples

[124] h5: Traj #1: Sneaker Authentication.

[125] p: This task involved verifying the authenticity of luxury sneakers based on visual evidence. Through a sequence of seven tool invocations, the model conducted a systematic examination of specific features. It utilized Image Search to contrast tongue and size tags with authentic references, identifying an anomalous ”A8513” sticker. Subsequent validation via Web Search confirmed this as a counterfeit indicator, leading to the correct classification.

[126] h5: Traj #2: Strongest German Beer Analysis.

[127] p: Identifying the strongest beer required distinguishing specific brands within a cluttered image. The model synergized the Code Interpreter for visual refinement with Web Search for factual retrieval. This approach enabled the precise filtering of lower-alcohol options, resulting in the accurate identification of a tie between Steam Brew German Red and Perlenbacher Strong.

[128] h3: D.2 Bad Case Examples

[129] h5: Traj #3: Karst Jigsaw Puzzle. Tool execution failure .

[130] p: Task. Reconstruct a 6 × 6 6{\times}6 jigsaw puzzle from an input image and locate the missing piece position. Failure. The model attempted to segment puzzle pieces with code-based image processing, but the segmentation failed and extracted only 24 segments instead of the expected 35. Without a complete set of pieces, the model could not form a valid grid and the reconstruction became infeasible. Classification Rationale. The core issue is a breakdown in tool-based image processing, which blocks the workflow even though the high-level plan is reasonable.

[131] p: -5pt

[132] h5: Traj #4: Authors United Window Display. Visual misidentification .

[133] p: Task. Identify the author shown in a window display from the provided image. Failure. The visible author is Donna Tartt, but the model failed to identify her. Although it performed cropping, it still did not extract the correct visual cue and produced an incorrect identification. Classification Rationale. The decisive evidence is in the image, and the failure comes from incorrect visual recognition rather than retrieval or reasoning.

[134] p: -5pt

[135] h5: Traj #5: Target Arena Identification. Visual misidentification .

[136] p: Task. Identify the correct university basketball facility shown in the image. Failure. The model misread an unclear floor logo and anchored on the wrong university, then reinforced the mistake using generic features such as roof trusses. It concluded the venue was St. Thomas AARC, while the correct answer is UNC. Classification Rationale. The initial mistake is a wrong visual anchor, and later steps follow that incorrect anchor.

[137] p: -5pt

[138] h5: Traj #6: Pilea Root Diagnosis. Knowledge hallucination .

[139] p: Task. Diagnose the hard mass on Pilea roots from the image. Failure. The correct interpretation is calloused residue from root rot, but the model claimed it was a “nursery plug” or fungal material and described visual properties that are not supported by the image. The final diagnosis followed a made-up interpretation aligned with retrieval results rather than the provided evidence. Classification Rationale. The model introduces unsupported facts and forces the image to fit a preconceived explanation.

[140] p: -10pt

[141] h5: Traj #7: Studio Swing Prop Design. Instruction misinterpretation .

[142] p: Task. Design a stationary photo prop that visually looks like a suspended swing. Failure. The model proposed a design where the seat is visibly supported by a horizontal bar, which removes the hanging illusion and violates the core constraint of the request. Classification Rationale. The model fails to follow the key constraint and answers a different problem than the one asked.

[143] p: langley00

[144] h2: Instructions for reporting errors

[145] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[146] p: Tip: You can select the relevant text first, to include it in your report.

[147] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[148] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
