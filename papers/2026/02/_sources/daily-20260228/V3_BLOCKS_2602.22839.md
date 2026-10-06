[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: DeepPresenter : Environment-Grounded Reflection for Agentic Presentation Generation

[3] h6: Abstract

[4] p: Presentation generation requires deep content research, coherent visual design, and iterative refinement based on observation. However, existing presentation agents often rely on predefined workflows and fixed templates. To address this, we present DeepPresenter , an agentic framework that adapts to diverse user intents, enables effective feedback-driven refinement, and generalizes beyond a scripted pipeline. Specifically, DeepPresenter autonomously plans, renders, and revises intermediate slide artifacts to support long-horizon refinement with environmental observations. Furthermore, rather than relying on self-reflection over internal signals (e.g., reasoning traces), our environment-grounded reflection conditions the generation process on perceptual artifact states (e.g., rendered slides), enabling the system to identify and correct presentation-specific issues during execution. Results on the evaluation set covering diverse presentation-generation scenarios show that DeepPresenter achieves state-of-the-art performance, and the fine-tuned DeepPresenter-9B remains highly competitive at substantially lower cost. Our project is available at: https://github.com/icip-cas/PPTAgent

[5] figure: Figure 1: Illustration of DeepPresenter . Given a user instruction, the Researcher gathers information and compiles a structured manuscript, while the Presenter transforms it into visual slides. Both agents interact and collaborate with a shared environment, leveraging grounded observations for reflective refinement.

[6] h2: 1 Introduction

[7] p: Presentations are a primary medium for information delivery across education, business, and research. A high-quality presentation combines well-researched content with coherent visual design, enabling audiences to grasp complex ideas efficiently. However, creating such presentations remains time-consuming and skill-demanding, motivating recent work that leverages Multimodal Large Language Models (MLLMs) to automate this task ( Liang et al., 2025 ; Zheng et al., 2025 ; Yang et al., 2025b ) .

[8] p: However, existing presentation agents ( Sefid et al., 2021 ; Xu et al., 2025 ; Yang et al., 2025b ) fall short of meeting these demands. First, they rely on predefined workflows ( Zheng et al., 2025 ) and content-agnostic templates ( Cachola et al., 2024 ) , limiting adaptability to varying user intents. This yields text-heavy slides with insufficient research depth and visual designs that fail to resonate with the narrative. Second, introspective reflection over internal signals (e.g., code or reasoning traces) cannot detect post-render defects ( Tang et al., 2025 ; Kim et al., 2025 ) , resulting in overlapping elements, truncated text, and broken layouts.

[9] p: To address these limitations, we propose DeepPresenter , an agentic framework for presentation generation (Figure 1 ). Unlike prior methods that decouple content and design via rigid templates, DeepPresenter coordinates two specialized agents through a shared observation space. The Researcher autonomously explores and compiles a structured manuscript aligned with the user intent, while the Presenter converts it into visually coherent slides via content-driven design rather than template filling. Crucially, instead of introspective self-reflection over internal signals, DeepPresenter grounds reflection in perceptual artifact states obtained from environmental observation (Figure 2 ): agents use inspect to view rendered manuscripts and slides, and think to plan targeted revisions to correct post-render defects.

[10] p: While our framework achieves strong performance with proprietary models, their high cost motivates a more efficient alternative. We therefore develop DeepPresenter-9B via supervised fine-tuning on curated trajectories (Figure 3 ). We first construct diverse presentation tasks from PersonaHub ( Ge et al., 2024 ) , arXiv, and FinePDFs ( Kydlíček et al., 2025 ) , augmented with verifiable constraints. During trajectory synthesis, we mitigate self-verification bias ( Stechly et al., 2024 ) with extrinsic verification: an independent critic evaluates artifacts in isolation and provides reasoning traces that steer targeted refinements, improving the quality of synthesized trajectories.

[11] p: We evaluate our method on a held-out set of 128 diverse presentation tasks across three dimensions: constraint satisfaction, content quality, and visual style. With proprietary backbones, DeepPresenter achieves an average score of 4.44, surpassing open-source baselines and the commercial system Gamma (4.36). Our specialized agentic design yields richer content and coherent design, while environment-grounded reflection reduces post-render defects by revising against observed perceptual artifact states. DeepPresenter-9B scores 4.19, outperforming all open-source baselines and approaching GPT-5 (4.22) at lower cost.

[12] p: In summary, our contributions are threefold:

[13] p: We propose DeepPresenter , an agentic presentation framework that coordinates Researcher and Presenter agents via a shared observation space, enabling autonomous information research and topic-aware design.

[14] p: We introduce environment-grounded reflection that grounds self-correction in perceptual artifact states obtained from post-render observations, reducing defects that are not detectable from internal signals alone.

[15] p: Results on the evaluation set covering diverse presentation-generation scenarios show that DeepPresenter achieves state-of-the-art performance, and the distilled DeepPresenter-9B remains highly competitive at substantially lower cost.

[16] h2: 2 DeepPresenter

[17] p: In this section, we present DeepPresenter , a dual-agent framework for presentation generation. We first formulate the task as an interactive agentic process, then describe the Researcher-Presenter collaboration and the environment-grounded reflection mechanism, as illustrated in Figure 2 .

[18] h3: 2.1 Task Formulation

[19] p: We formulate presentation generation as an interactive agentic task. Given an instruction ℐ \mathcal{I} and an agent environment ℰ \mathcal{E} equipped with a tool library 𝒯 \mathcal{T} and a file system ℱ \mathcal{F} , the system aims to generate a high-quality presentation 𝒫 \mathcal{P} . The generation process can be modeled as a multi-step trajectory τ = { ( r 1 , a 1 , o 1 ) , … , ( r T , a T , o T ) } \tau=\{(r_{1},a_{1},o_{1}),\dots,(r_{T},a_{T},o_{T})\} , where at each step t t , the agent generates a reasoning trace r t r_{t} , selects an action a t ∈ 𝒯 a_{t}\in\mathcal{T} , and receives observation o t o_{t} from ℰ \mathcal{E} . We decompose the trajectory into two sequential phases: τ = τ R ∘ τ P \tau=\tau^{R}\circ\tau^{P} , where τ R \tau^{R} and τ P \tau^{P} denote the Researcher and Presenter trajectories, respectively. The two agents communicate through ℱ \mathcal{F} , where the Researcher persists a structured manuscript ℳ \mathcal{M} and associated assets for the Presenter to consume. Appendix C lists the tools.

[20] h3: 2.2 Dual-Agent Collaboration

[21] p: Presentation generation requires both information research and visual design, which demand different planning and tool use. We split these roles between two specialized agents while sharing the same backbone model.

[22] figure: Figure 2: Comparison between self-reflection and environment-grounded reflection. Self-reflection relies on uncertain triggers and inputs without external signals. DeepPresenter grounds reflection in environmental observations through the inspect tool.

[23] h4: Researcher Agent

[24] p: Given ℐ \mathcal{I} , the Researcher autonomously plans its exploration instead of following a predefined workflow. It executes multiple steps during τ R \tau^{R} , invoking tools from 𝒯 \mathcal{T} to retrieve and synthesize supporting materials and to create auxiliary assets as needed. The exploration depth and strategy adapt to user intent: a technical presentation may require surveying related work, while a general-audience talk may prioritize accessible examples and vivid illustrations. Finally, the Researcher compiles slide text and associated assets into a structured markdown manuscript ℳ \mathcal{M} organized by narrative flow, and persists it to ℱ \mathcal{F} .

[25] figure: Dimension Category Count Ratio (%) Language English 603 52.34 Chinese 549 47.66 Source PersonaHub 586 50.87 FinePDFs 362 31.42 arXiv 204 17.71 Aspect Ratio 16:9 Widescreen 327 28.39 4:3 Standard 304 26.39 A1 Poster 30 2.60 Free 491 42.62 Slide Count 11-20 249 21.61 1-10 320 27.78 Free 583 50.61 Total 1,152 100.00 Table 1: Statistics of the constructed presentation tasks by language, source, aspect ratio, and slide count. “Free” indicates no constraint is specified.

[26] h4: Presenter Agent

[27] p: Rather than populating predefined templates, the Presenter generates slides from scratch during τ P \tau^{P} . Given ℳ \mathcal{M} from ℱ \mathcal{F} , the agent first develops a global design plan, establishing color themes and typography that resonate with the topic. It then generates each slide as a standalone HTML file, translating manuscript content into visual elements following the design plan. This content-driven approach enables stylistic choices aligned with the presentation topic, such as earthy palettes for sustainability or minimalist layouts for academic tutorials.

[28] h3: 2.3 Environment-Grounded Reflection

[29] p: We ground agent reflection in environmental observations rather than introspective reasoning over internal signals ( He et al., 2025 ) . The key issue with self-reflection is state mismatch: agents operate on intermediate representations (e.g., HTML or markdown), while users perceive only rendered artifacts. As a result, many defects manifest only in perceptual states (e.g., broken images, overflow, or low contrast), leaving introspective reflection operating in a mismatched observation space.

[30] p: To make perceptual artifact states observable to the agent, we introduce the inspect tool as an explicit observation interface. For the Presenter, inspect renders an HTML file into image pixels, exposing post-render defects such as overflow, overlap, and low contrast; for the Researcher, inspect returns structured diagnostics of the manuscript and file state, including slide count, asset availability, and detected language. Agents then use think to reflect on observed defects and plan targeted edits. This forms an observe–reflect–revise loop where agent observations align with user perception.

[31] figure: Figure 3: Our data synthesis pipeline. The process ensures high-quality trajectories for supervised fine-tuning through three integrated mechanisms: (1) Query Construction augments tasks with verifiable constraints; (2) Extrinsic Verification injects reasoning traces when defects are identified to guide agent self-correction during sampling; and (3) Trajectory Filtering validates constraint compliance and assesses consistency and output quality.

[32] h2: 3 Frontier Presentation Agent Model

[33] p: This section presents our training pipeline as shown in Figure 3 : task dataset construction, trajectory synthesis with extrinsic verification to elicit high-quality reflective behaviors, and multi-stage filtering for quality.

[34] h3: 3.1 Query Construction

[35] p: We construct a task collection for training our compact model and evaluating our framework. To cover diverse presentation scenarios in both intent-driven and document-conditioned settings, we draw task seeds from PersonaHub ( Ge et al., 2024 ) , arXiv, and FinePDFs-Edu ( Kydlíček et al., 2025 ) . Each task is augmented with verifiable constraints (e.g., slide count, language, aspect ratio) to capture fine-grained user-specified requirements. For PersonaHub, we prompt GLM-4.6 to synthesize presentation tasks conditioned on persona descriptions; for arXiv and FinePDFs-Edu, we construct tasks that require generating presentations based on provided documents. Each task is further augmented with verifiable constraints, including slide count, language, and aspect ratio. In total, this task collection contains 1,152 tasks, with 1,024 for trajectory sampling and 128 held out for evaluation. Detailed statistics are shown in Table 1 .

[36] h3: 3.2 Verification-Guided Trajectory Synthesis

[37] p: When sampling agentic trajectories, self-reflection is susceptible to self-verification bias ( Jiang et al., 2025 ) : the agent judges its own intermediate outputs from within the same trajectory state that produced them. This coupling entangles verification with self-justification, resulting in flawed outputs being accepted. To break this coupling, we introduce extrinsic verification, where verification signals are produced in an isolated context.

[38] p: As illustrated in Figure 3 , after the agent invokes inspect and obtains an observation o t o_{t} , an independent critic performs verification conditioned on o t o_{t} and the corresponding intermediate artifacts. The critic outputs a reasoning trace that identifies defects (e.g., low contrast) and specifies actionable adjustments (e.g., adjust text color). We append this trace to the agent context as a think call, guiding targeted revisions before continuing the rollout.

[39] figure: Framework Model Constraint Content Style Avg. Diversity Close-sourced Baseline Gamma – 4.93 4.08 4.08 4.36 0.52 Open-sourced Baseline PPTAgent GPT-5 3.96 3.00 4.07 3.68 0.35 Gemini-3-Pro 4.22 3.09 4.30 3.87 0.19 Claude-Sonnet-4.5 3.72 2.93 4.15 3.60 0.17 GLM-4.6 4.02 3.17 4.24 3.81 0.30 KCTV GPT-5 4.95 2.84 3.63 3.81 0.21 Gemini-3-Pro 4.58 3.01 3.90 3.83 0.27 Claude-Sonnet-4.5 4.88 2.90 3.99 3.92 0.20 GLM-4.6 4.66 2.83 3.94 3.81 0.25 Ours DeepPresenter GPT-5 4.80 3.79 4.07 4.22 0.56 Gemini-3-Pro 4.70 4.25 4.37 4.44 0.79 Claude-Sonnet-4.5 4.90 4.05 4.27 4.41 0.49 GLM-4.6V 4.69 3.25 3.75 3.90 0.58 GLM-4.6V-Flash 4.67 3.11 3.69 3.82 0.47 DeepPresenter-9B 4.77 3.52 4.29 4.19 0.53 Table 2: Performance comparison of different frameworks and models. The best/second-best scores are bolded / underlined . Quality metrics (Constraint, Content, Style, Avg.) are scaled to 0–5, while Diversity is scaled to 0–1.

[40] h3: 3.3 Trajectory Filtering

[41] p: We adopt a three-stage filtering pipeline to ensure trajectory quality. First, we verify constraint compliance through a rule-based system. Second, we evaluate consistency using GLM-4.6, removing trajectories that fail to follow the extrinsic-verification trace with aligned revisions (i.e., reflection–action inconsistency). Third, we assess output quality using GLM-4.6V, filtering out trajectories with critical defects such as element overlap or broken images.

[42] h2: 4 Experiment

[43] p: In this section, we evaluate our method on presentation generation and analyze our key components.

[44] h3: 4.1 Setup

[45] h4: Implementation Details

[46] p: We sample trajectories by running DeepPresenter with Gemini-3-Pro as the backbone and critic model on 1,024 training tasks, with a maximum context window of 50K tokens. 802 trajectories pass our filtering pipeline and are used for supervised fine-tuning. We fine-tune GLM-4.6V-Flash on these trajectories using MS-SWIFT ( Zhao et al., 2024 ) , with a batch size of 32 and learning rate of 1e-5 for 5 epochs. Training takes approximately 80 GPU hours on 8 A800 GPUs.

[47] h4: Models and Baselines

[48] p: We compare against one commercial system, Gamma 1 1 1 https://gamma.app/ , and two academic frameworks: PPTAgent ( Zheng et al., 2025 ) and KCTV ( Cachola et al., 2024 ) . For backbone models, we evaluate with proprietary GPT-5 ( OpenAI, 2025 ) , Gemini-3-Pro ( Comanici et al., 2025 ) , and Claude-Sonnet-4.5 ( Anthropic, 2025 ) , as well as open-source GLM-4.6 ( Zeng et al., 2025a ) . For DeepPresenter , we additionally evaluate with GLM-4.6V and GLM-4.6V-Flash ( Team et al., 2025 ) , as our framework leverages visual feedback through the inspect tool.

[49] h4: Evaluation Protocol

[50] p: We hold out 128 tasks from the constructed task collection and evaluate generated presentations using the following metrics:

[51] p: ∙ \bullet Constraint scores each presentation by the fraction of user-specified constraints it satisfies, covering slide count, language, and aspect ratio, verified through rule-based checking.

[52] p: ∙ \bullet Content & Style evaluate the quality of slide content and visual design. We adopt the MLLM-based evaluation framework from Zheng et al. (2025) with GPT-5 as the judge, which has been validated to correlate well with human judgments.

[53] p: ∙ \bullet Diversity quantifies visual style variance across generated presentations using the Vendi Score ( Friedman and Dieng, 2022 ) , which computes diversity based on the eigenvalue entropy of feature similarity matrices extracted by DINOv2 ( Oquab et al., 2023 ) .

[54] p: We report Avg. as the mean of Constraint, Content, and Style (scaled 0–5), while Diversity (scaled 0–1) measures cross-presentation variation.

[55] h3: 4.2 Main Results

[56] p: Table 2 presents the main experimental results.

[57] h4: DeepPresenter achieves state-of-the-art performance

[58] p: Across all backbone models, DeepPresenter consistently outperforms open-source baselines. With Gemini-3-Pro as the backbone, DeepPresenter attains an average score of 4.44, surpassing the best open-source baseline (KCTV + Claude-Sonnet-4.5, 3.92) by 13.3% and the commercial product Gamma (4.36). The improvements stem from two aspects: (1) Content quality improves most because Researcher performs intent-adaptive information seeking and synthesis, rather than relying on fixed workflows or user-provided inputs. Baseline frameworks depend on user-provided materials and lack deep retrieval capability, while our agent searches, retrieves, and synthesizes information from diverse sources. (2) Style scores improve through content-aware design and environment-grounded reflection. Our framework enables Presenter to align design decisions with the narrative, while environment-grounded reflection mitigates free-form generation failures by revising against post-render defects.

[59] h4: Free-form generation enables greater visual diversity, with DeepPresenter achieving a diversity score of 0.79.

[60] p: Under our diversity metric, DeepPresenter more than doubles template-based baselines by generating slides in a free-form manner. Baseline frameworks achieve diversity scores of only 0.17 to 0.35, as fixed templates constrain visual variation. PPTAgent, in particular, shows lower constraint scores because its style decisions are predetermined by the workflow, limiting task-specific adaptation. Even Gamma, despite its commercial polish, achieves only 0.52. In contrast, our framework maintains high constraint compliance while enabling greater visual diversity (0.79).

[61] h4: DeepPresenter-9B surpasses all open-source baselines with high efficiency.

[62] p: With only 802 trajectories, our compact model achieves an average score of 4.19, outperforming open-source baselines and matching GPT-5 (4.22) at substantially lower cost. These results support the effectiveness of our verification-guided trajectory synthesis and suggest that compact models can acquire agentic behaviors from limited but high-quality samples.

[63] figure: Configuration Cons. Content Style Avg. Gemini-3-Pro DeepPresenter 4.70 4.25 4.37 4.44 w/o Grounded Reflection 4.52 4.15 4.31 4.32 w/o Dual-Agent 3.94 3.96 4.22 4.04 DeepPresenter-9B DeepPresenter-9B 4.77 3.52 4.29 4.19 w/o Grounded Reflection 4.21 3.23 4.01 3.82 w/o Dual-Agent 3.65 2.93 3.11 3.23 w/o Trajectory Filtering 4.67 3.30 4.12 4.03 Table 3: Ablation study on framework components and training strategy. Cons. denotes constraint satisfaction.

[64] figure: Configuration Cons. Content Style Avg. Δ \Delta GLM-4.6V-Flash 4.67 3.11 3.69 3.82 – + Fine-tuning 4.71 3.19 3.92 3.94 +0.12 + Extrinsic Verification 4.74 3.28 4.03 4.02 +0.20 Table 4: Effect of extrinsic verification on model performance. Both fine-tuned variants use 300 trajectories. Δ \Delta denotes improvement over the base model.

[65] h3: 4.3 Ablation Study

[66] p: We ablate key components of DeepPresenter on Gemini-3-Pro and DeepPresenter-9B, as shown in Table 3 . (1) Environment-grounded reflection is critical because it extends observation space to post-render perceptual artifact states. Disabling inspect confines reflection to pre-render artifacts and degrades performance from 4.44 to 4.32 on Gemini-3-Pro and from 4.19 to 3.82 on DeepPresenter-9B. (2) Dual-agent collaboration contributes significantly by decomposing long-horizon execution into specialized sub-tasks. Without it, performance drops substantially on both backbones. (3) Trajectory filtering effectively prevents biased and low-quality patterns from being distilled during fine-tuning. Removing it drops DeepPresenter-9B from 4.19 to 4.03.

[67] h2: 5 Analysis

[68] p: We analyze the effectiveness of the extrinsic evaluation, examine failure modes in trajectory synthesis, and present efficiency comparisons alongside qualitative case studies.

[69] figure: Figure 4: Distribution of defects identified by self-verification and extrinsic verification for manuscripts (left) and slides (right), respectively.

[70] h3: 5.1 Effect of Extrinsic Verification

[71] h4: Extrinsic verification improves trajectory synthesis by mitigating self-verification bias.

[72] p: To quantify its impact, we train two variants on 300 trajectories sampled from the same set of tasks, with and without extrinsic verification during trajectory synthesis. As shown in Table 4 , adding extrinsic verification yields a 67% larger gain in Avg. (0.20 vs. 0.12) than fine-tuning alone. This indicates that, even with environment-grounded observations, revision signals produced solely within the agent’s own trajectory state can be biased, leading to suboptimal refinements being distilled during learning.

[73] h4: Extrinsic verification mitigates self-verification bias by strengthening defect-triggered revision signals.

[74] p: We categorize reflection-triggered defects into three manuscript types: integrity (e.g., missing asset references), constraint (e.g., mismatched slide count), and format (e.g., invalid markup); and three slide types: layout (e.g., overlap), render (e.g., blank slides), and style (e.g., low contrast). Figure 4 compares defects identified on the same 300 trajectories under self-verification versus extrinsic verification. Extrinsic verification consistently yields more defect detections across categories, with the largest gaps on slides (e.g., 308 vs. 212 for layout and 101 vs. 43 for render ). This pattern indicates a systematic failure in self-verification: when verification is conducted within the generating trajectory state, the agent tends to rationalize defects, producing biased judgment ( Jiang et al., 2025 ; Stechly et al., 2024 ) . By decoupling verification from the agent’s own trajectory state, extrinsic verification mitigates this bias and provides stronger signals to trigger corrective revisions during synthesis.

[75] figure: Figure 5: Failure distribution in synthesized trajectories before filtering

[76] figure: Figure 6: Performance vs. Price scatter plot with Pareto frontier representation. Different colors represent different frameworks

[77] h3: 5.2 Trajectory Failure Analysis

[78] p: Following the categories in Section 3.3 , we analyze failures in synthesized trajectories before filtering (Figure 5 ). Quality errors are most prevalent (43.0%), underscoring the difficulty of sustaining high standards under free-form generation. Environment failures are also common (32.3%), reflecting long-horizon fragility from context overflow and infrastructure disruptions. The remaining cases include Constraint violations (13.5%) and Consistency errors (11.2%), which are less frequent but still non-negligible.

[79] figure: Figure 7: Qualitative comparison of presentations generated by different methods. DeepPresenter under Gemini-3-Pro and DeepPresenter-9B produce high-quality slides with styles that resonate with the topic. Baselines rely on document-embedded or AI-generated images with template-based generation, producing text-heavy outputs and misaligned visual themes.

[80] h3: 5.3 Efficiency Analysis

[81] p: Figure 6 presents the cost-performance trade-off across frameworks and models. (1) DeepPresenter-9B advances the Pareto frontier, significantly outperforming the prior frontier point at comparable cost. Compared to KCTV + Gemini-3-Pro (3.83), DeepPresenter-9B achieves 4.19 at a similar price, a significant improvement in cost-quality trade-off. (2) DeepPresenter establishes a new upper bound for presentation generation, surpassing the previous best system Gamma. With an average score of 4.44 versus Gamma’s 4.36, DeepPresenter delivers the strongest result in our evaluation.

[82] p: Notably, baseline frameworks exhibit flat performance across backbone models, whereas DeepPresenter demonstrates substantial variation (3.82 to 4.44). This pattern is consistent with baselines being limited by their fixed pipelines, while DeepPresenter can better leverage stronger model capacity.

[83] h3: 5.4 Case Study

[84] p: We present qualitative examples in Figure 7 . (1) DeepPresenter produces visually rich slides through diverse asset sources, while baselines tend to yield text-heavy outputs. Gamma includes more imagery than academic baselines. However, it relies heavily on AI-generated images and often mishandles figures embedded in source documents (e.g., inappropriate scaling of architectural diagrams). Open-source baselines rarely retrieve or create supporting visuals, resulting in predominantly textual content. (2) DeepPresenter generates visual themes that resonate with content, whereas baselines rely on fixed templates. For example, DeepPresenter employs green tones for environmental topics and minimalist layouts for academic presentations, while baseline methods exhibit limited topical alignment due to template-driven generation.

[85] h2: 6 Related Work

[86] p: Presentation generation has attracted increasing attention due to its practical value for information delivery. Before the emergence of large language models, presentation generation was primarily formulated as a document summarization task. These approaches employed extractive summarization to select salient sentences using neural networks ( Hu and Wan, 2014 ; Fu et al., 2022 ; Sun et al., 2021 ) or phrase-based methods ( Wang et al., 2017 ) . However, the limited reasoning capabilities of pre-LLM models constrained their ability to handle diverse user intents and produce visually engaging outputs.

[87] p: The emergence of LLMs has shifted the paradigm toward agent-based approaches that leverage stronger reasoning and generalization capabilities. Recent work explores multi-agent collaboration for content extraction and layout planning ( Liang et al., 2025 ; Yang et al., 2025b ; Xu et al., 2025 ; Ge et al., 2025 ; Cachola et al., 2024 ) , aesthetic-aware generation ( Liu et al., 2025 ) , as well as slide understanding and editing ( Jung et al., 2025 ; Huang et al., 2025 ; Zheng et al., 2025 ; Zeng et al., 2025b ) . However, these approaches often focus on predefined workflows and fixed templates, limiting adaptation to user intent and iterative refinement with environmental feedback.

[88] p: Compared with previous methods, DeepPresenter formulates presentation generation as an autonomous exploration and collaboration process between two specialized agents. The Researcher-Presenter decomposition enables adaptive planning based on task complexity, while environment-grounded reflection allows agents to verify and refine artifacts through rendered slides and file system states ( Tang et al., 2025 ; Jiang et al., 2025 ; Stechly et al., 2024 ) .

[89] h2: 7 Conclusion

[90] p: In this work, we propose DeepPresenter , an agentic framework for presentation generation in which agents plan autonomously and adapt to diverse user intents. Our framework grounds self-reflection in perceptual artifact states from environmental observations, enabling agents to iteratively identify and fix post-render defects. We further train DeepPresenter-9B on trajectories synthesized with extrinsic verification, which mitigates self-verification bias and strengthens reflective behaviors. Results show that DeepPresenter achieves state-of-the-art performance, while DeepPresenter-9B remains competitive at substantially lower cost.

[91] h2: Limitations

[92] p: While DeepPresenter demonstrates strong performance, several limitations remain. First, DeepPresenter relies on multi-step, tool-using rollouts, which increase inference cost and are sensitive to environment instability (e.g., context overflow and infrastructure failures) observed in our trajectory analysis. Second, extrinsic verification is only used during trajectory synthesis. We do not employ an external critic at inference time, as critic-provided reflection signals can introduce reflection–action inconsistency and additional overhead. Future work can explore mitigating self-verification bias at inference time.

[93] h2: References

[94] h2: Appendix A Detailed Analysis

[95] h3: A.1 Human Evaluation

[96] p: To address concerns about potential circularity introduced by LLM-as-judge evaluation, we conduct a small-scale human study to corroborate the automatic assessments. We recruited two graduate students majoring in computer science to evaluate 32 randomly sampled presentations from the test set. Following the evaluation dimensions in Section 4 , annotators rate Content and Style on a 1–5 Likert scale using the scoring criteria of Zheng et al. (2025) , while Constraint satisfaction is verified via rule-based checks consistent with our evaluation protocol. Evaluators were provided with rendered slide images and scored them independently. Table 5 reports the resulting ratings. Importantly, the relative ranking and overall trends under human judgment align with our automatic evaluation, suggesting that the observed improvements are not an artifact of relying solely on GPT-5 as the judge.

[97] h3: A.2 Performance by Domain

[98] p: We analyze DeepPresenter with Gemini-3-Pro across domains. PersonaHub shows the strongest content (4.49) and style (4.49) scores, but relatively lower constraint satisfaction (4.38). This is likely because PersonaHub queries are synthesized by an LLM based on persona descriptions, resulting in more diverse and complex constraint specifications that are harder to follow. arXiv achieves near-perfect constraint satisfaction (4.91) but the lowest content (3.84) and style (4.13) scores. The formal nature of academic presentations restricts visual diversity, and accurately conveying technical content requires deeper domain understanding.

[99] h3: A.3 Tool Usage Analysis

[100] p: We analyze tool invocation patterns across agents and domains, as shown in Figure 8 . For agent roles (Figure 8 a), Researcher and Presenter exhibit distinct tool preferences aligned with their responsibilities. Researcher relies heavily on Retrieve tools for information gathering, while Presenter focuses on File operations and Reason tools for iterative slide editing and reflection. This specialization validates our dual-agent design, where each agent develops tool usage patterns tailored to its role.

[101] p: Across domains (Figure 8 b), Researcher shows adaptable usage patterns reflecting task characteristics. PersonaHub tasks exhibit significantly higher Retrieve usage, as persona-driven queries do not provide reference documents, requiring agents to actively search for relevant materials. In contrast, arXiv and FinePDF tasks involve provided source documents, leading to higher File usage for document processing and lower reliance on retrieval. Tool categories are detailed in Table 8 .

[102] h2: Appendix B Dataset

[103] h3: B.1 Data Sources

[104] p: We collect presentation tasks from three sources to ensure diverse scenario coverage. For academic presentations, we pair arXiv papers with requests that specify target audiences (beginners, intermediate learners, domain experts, or peer researchers) and corresponding scenarios (lectures, seminars, defenses, or conference talks). For general educational topics, we sample English and Chinese PDF documents from FinePDFs-Edu ( Kydlíček et al., 2025 ) , each accompanied by instructions to create a presentation based on the attachment.

[105] figure: Method Cons. Content Style Avg. Gamma 4.84 3.52 3.90 4.09 PPTAgent 3.72 3.07 3.60 3.46 KCTV 4.41 2.84 3.19 3.48 DeepPresenter 4.56 3.86 4.25 4.22 Table 5: Human evaluation results on 32 randomly sampled presentations.

[106] figure: Domain Cons. Content Style Avg. PersonaHub 4.38 4.49 4.49 4.45 arXiv 4.91 3.84 4.13 4.29 FinePDF 4.94 4.21 4.38 4.51 Table 6: Domain performance breakdown. Cons. denotes constraint satisfaction.

[107] figure: Figure 8: Tool usage analysis. (a) Distribution of tool invocations by agent role. (b) Tool usage patterns of Researcher across different domains.

[108] p: For personalized scenarios, we leverage PersonaHub ( Ge et al., 2024 ) and prompt Qwen3-235B-A22B ( Yang et al., 2025a ) to generate realistic presentation requests grounded in user personas. We adopt two generation strategies: knowledge-grounded generation, which incorporates both persona descriptions and synthesized domain knowledge, and open-ended generation, which relies solely on persona characteristics. The model is instructed to adopt the persona’s perspective and select the appropriate language based on cultural background. Generated queries undergo language filtering, semantic deduplication, and LLM-based quality control to remove low-quality or inappropriate samples.

[109] h3: B.2 Constraint Augmentation

[110] p: To assess instruction-following capabilities, each task is augmented with verifiable constraints, including slide count, aspect ratio (widescreen 16:9, standard 4:3, or poster), and language. These constraints are randomly assigned per task. For automated verification, we parse generated PDFs and validate them against specified constraints using a rule-based system. The constraint satisfaction score is computed as the proportion of constraints successfully met.

[111] h3: B.3 Evaluation Set

[112] p: To facilitate replication, we disclose the composition of our 128-task evaluation split and statistics in Table 7 .

[113] figure: Dimension Category Count Ratio (%) Language English 74 57.81 Chinese 54 42.19 Source PersonaHub 57 44.53 FinePDFs 38 29.69 arXiv 33 25.78 Aspect Ratio 16:9 Widescreen 42 32.81 4:3 Standard 34 26.56 A1 Poster 4 3.12 Free 48 37.50 Slide Count 11-20 26 20.31 1-10 36 28.12 Free 66 51.56 Total 128 100.00 Table 7: Evaluation set statistics across language, source, aspect ratio, and slide-count constraints. “Free” indicates no constraint is specified.

[114] figure: Category Action Retrieve search_web, search_images, search_papers, fetch_url, get_paper_authors, get_scholar_details , document_analyze, image_caption File convert_to_markdown, read_file, write_file, move_file, edit_file, download_file, execute_command, create_directory, list_directory Reason thinking, inspect_slide, inspect_manuscript Control todo_create, todo_update, todo_list, finalize Create image_generation Table 8: Action Categories

[115] h2: Appendix C Agent Framework

[116] p: Presentation creation requires interacting with heterogeneous resources beyond static web text, including search results, images, papers, and local files, as well as inspecting intermediate artifacts such as manuscripts and rendered slides. To support this, we organize our toolset into five categories (Table 8 ): Retrieve for information gathering, File for document manipulation, Reason for inspection and reflection, Control for task management, and Synthesis for code execution and asset generation.

[117] h4: Inspection Tools.

[118] p: The Reason category includes two inspection tools that enable environment-grounded reflection:

[119] p: inspect_manuscript : Parses the markdown manuscript and returns structured diagnostics, including the total slide count, detected content language, and validation results for referenced image assets. The tool checks whether each image path exists, flags external URLs that should be downloaded locally, identifies missing alt text, and warns about duplicate image usage.

[120] p: inspect_slide : Renders an HTML slide into a pixel image using a headless browser and returns the image to the agent’s visual context. The tool supports multiple aspect ratios (16:9 widescreen, 4:3 standard, A1 poster) and enables agents to perceive visual defects such as contrast issues and element overflow that are invisible at the code level.

[121] p: Each task is executed as a sequence of reasoning-action-observation steps within a maximum context window of 50K tokens. To prevent context overflow, our system sends warning messages when the accumulated window length reaches 50% and 80% of the maximum capacity, allowing the agent to adjust its strategy accordingly.

[122] h2: Appendix D Prompts

[123] h3: D.1 Data Synthesis Prompts

[124] h3: D.2 Extrinsic Verification Prompts

[125] h3: D.3 Agent System Prompts

[126] h2: Instructions for reporting errors

[127] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[128] p: Tip: You can select the relevant text first, to include it in your report.

[129] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[130] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
