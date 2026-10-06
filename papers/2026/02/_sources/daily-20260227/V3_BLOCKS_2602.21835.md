[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: UniVBench : Towards Unified Evaluation for Video Foundation Models

[3] h6: Abstract

[4] p: Video foundation models aim to integrate video understanding, generation, editing, and instruction following within a single framework, making them a central direction for next-generation multimodal systems. However, existing evaluation benchmarks remain fragmented and limited in scope, as they each target a single task, rely on task-specific metrics, and typically use short or simple video clips. As a result, they do not capture the unified capabilities that these models are designed to deliver. To address this gap, we introduce UniVBench, a benchmark purpose-built for evaluating video foundation models across four core abilities: video understanding, video generation, video editing, and a newly proposed task, video reconstruction, which assesses how faithfully a model can reproduce video content it has encountered. Our benchmark substantially expands the complexity of evaluation by incorporating 200 high-quality, diverse and multi-shot videos, each paired with detailed captions, multi-format editing instructions, and reference images. All videos are human-created and carefully validated, offering richer cinematic information than prior benchmarks. In addition, we develop a unified agentic evaluation system (UniV-Eval) that standardizes prompting, instruction parsing, and scoring across all tasks, enabling fair, scalable, and reproducible comparisons of unified video models. By grounding evaluation in instruction-based multi-shot video tasks, UniVBench provides the first framework for measuring the integrated capabilities that video foundation models aim to achieve. Extensive human annotations ensure our evaluation aligns with human judgment, enabling rigorous assessment and accelerating progress toward robust video intelligence. Code and datasets are available at https://github.com/JianhuiWei7/UniVBench

[5] figure: Figure 1 : Overview of the UniVBench evaluation setting across 8 Dimensions, 21 Sub-Dimensions, and 6 Tasks. Given a source video, T2V synthesizes a video using its ground-truth caption, while V2V reconstructs the video based solely on the model’s self-generated understanding text, enabling a direct diagnosis of perception–generation coupling. UniVBench supports six unified tasks—video captioning ( V2T ), text-to-video generation ( T2V ), reference-image video generation ( R2V ), text-instruction video editing ( TV2V ), reference-image video editing ( RV2V ), and video reconstruction ( V2V ).

[6] h2: 1 Introduction

[7] p: Video foundation models have recently emerged as a promising direction for next-generation multimodal systems. These models aim to integrate understanding and generation within a single architecture. However, current approaches remain fundamentally separated. Generation-focused systems [ 3 , 35 , 32 , 50 , 14 , 69 , 57 ] excel at synthesis but cannot reason about video content, while understanding models [ 68 , 25 , 12 , 76 , 2 , 16 , 1 , 19 , 20 ] achieve strong perception but cannot generate videos. Emerging unified architectures [ 45 , 74 , 62 , 55 , 66 , 61 , 5 , 9 , 28 , 44 , 43 , 56 ] attempt to bridge this divide by integrating LLMs with visual tokenizers and video decoders, enabling both video understanding and generation in response to instructions.

[8] p: Despite these architectural advances, a critical question remains: does unification actually improve performance across the full spectrum of video tasks? Current benchmarks cannot answer this due to two fundamental limitations. First, existing datasets are task-specific and cannot support unified evaluation. As shown in Table 1 , most video understanding benchmarks [ 75 , 54 , 4 , 29 ] use copyrighted web videos that may contaminate evaluation data and lack the instructions needed for generation and editing tasks. Video generation benchmarks [ 7 , 18 , 24 , 71 , 22 , 73 , 72 , 51 ] focus on text-to-video synthesis without supporting understanding or editing evaluation. Video editing benchmarks [ 59 , 13 , 39 , 67 , 21 , 27 ] remain limited to single-shot scenarios, lacking the multi-shot content. Beyond task coverage, existing benchmarks also exhibit fragmented evaluation of cinematic qualities. As shown in Table 2 , understanding benchmarks like AuroraCap [ 4 ] emphasize subject detection and camera motion but ignore style and spatial relationships; generation benchmarks like VBench [ 18 ] evaluate subjects and actions but lack systematic lighting and color assessment; editing benchmarks like TGVE [ 59 ] focus on subject preservation but omit background and spatial coherence. No existing benchmark systematically evaluates cinematic dimensions across all video tasks.

[9] p: Second, evaluation metrics are fundamentally fragmented. As shown in Table 3 , understanding uses reference-based measures, generation uses distributional metrics that often disagree, and editing requires ad hoc metric combinations [ 58 , 70 , 11 ] . This fragmentation limits cross-task comparison. Moreover, a single scalar score severely limits interpretability, obscuring nuanced trade-offs between a model’s strengths and weaknesses, and consequently failing to provide actionable feedback to the training phase. High-quality evaluation is inherently complex, multifaceted, and dynamic. Fixed evaluation criteria may not generalize across diverse video properties: some videos emphasize faithful reconstruction of visual entities, while others prioritize narrative coherence over instance-level fidelity.

[10] p: We introduce UniVBench, the first unified benchmark designed to evaluate video foundation models across their full capability spectrum. The benchmark comprises 200 high-quality, multi-shot videos, each with rich annotations including detailed captions, multi-format editing instructions, and reference images. Crucially, all content is human-created and copyright-free, enabling fair evaluation of editing, reconstruction, and instruction-following without legal or data contamination concerns. We pair the benchmark with a unified agentic evaluation system (UniV-Eval) that standardizes prompting, instruction parsing, and multi-dimensional scoring across all tasks. This provides consistent, interpretable metrics that enable direct cross-model and cross-task comparison, while supporting fine-grained attribution of errors to perception versus generation components.

[11] p: Our work makes three key contributions: (1) The first multi-shot video dataset specifically designed for unified evaluation, free of copyright and contamination issues; (2) a unified agentic evaluation system that enables measurement across understanding, generation, editing, and reconstruction; and (3) a principled framework for attributing model capabilities and failures across the perception-generation spectrum. By aligning evaluation with the goals of unified video modeling, our benchmark establishes a foundation for measuring progress toward general-purpose, instruction-following video intelligence.

[12] figure: Tasks : ①: V2T ②: T2V ③: R2V ④: TV2V ⑤: RV2V ⑥: V2V Benchmark Multi-task Multi-shot Copyright Issue Benchmarks for Video Understanding M-VAD [ 46 ] ① ✗ Yes MPII-MD [ 49 ] ① ✗ Yes MSR-VTT [ 63 ] ① ✓ Potential Charades [ 38 ] ① ✗ Yes ActivityNet [ 23 ] ① ✓ Yes Youcook2 [ 75 ] ① ✗ Yes VATEX [ 54 ] ① ✗ Yes AuroraCap [ 4 ] ① ✗ Potential ShotBench [ 29 ] ① ✗ Yes Benchmarks for Video Generation EvalCrafter [ 30 ] ② ✗ NA FETV [ 31 ] ② ✗ NA MQT [ 7 ] ② ✗ NA VBench [ 18 ] ② ✗ NA GenAIBench [ 24 ] ② ✗ NA LGVQ [ 71 ] ② ✗ NA T2VQA-DB [ 22 ] ② ✗ NA AIGVQA-DB [ 52 ] ② ✗ NA VBench2.0 [ 73 ] ② ✗ NA Q-Eval [ 72 ] ② ✗ NA AIGVE-60K [ 51 ] ② ✗ NA Benchmarks for Video Editing CCEdit [ 13 ] ④ ✗ No TGVE [ 59 ] ④ ✗ No TGVE+ [ 39 ] ④ ✗ No VE-Bench [ 42 ] ④ ✗ No UNIC [ 67 ] ⑤ ✗ Potential VACE-Bench [ 21 ] ③ ④ ⑤ ✗ Potential FIVE [ 27 ] ④ ✗ Potential UniVBench ① ∼ \sim ⑥ ✓ No Table 1: Comparison of benchmarks for video understanding, generation and editing. Multi-task shows the applicable tasks of the benchmark. Multi-shot indicates that whether the video source and text annotations have multi-shot content. Copyright Issue indicates whether the video sources in the dataset are editable without copyright issue.

[13] h2: 2 Related Work

[14] h3: 2.1 Video Foundation Models

[15] p: Early progress in video foundation models emerged from text-to-video generation, where diffusion-based frameworks such as ModelScopeT2V [ 53 ] , LAMP [ 60 ] , CogVideoX [ 65 ] , Vidu [ 3 ] and Wan [ 50 ] achieved high-fidelity video synthesis, while autoregressive models like Show-1 [ 69 ] and Emu2 [ 41 ] introduced unified visual tokens for more controllable generation. However, these approaches are inherently one-directional, focusing on synthesis without true multimodal reasoning. In parallel, video-to-text understanding models including VideoLLaMA3 [ 68 ] , LLaVA-OneVision [ 25 ] , and VILA 2 [ 12 ] extended large multimodal encoders to interpret temporal content and perform grounded question answering. Despite strong perception ability, these encoder-based methods remain limited to understanding and cannot generate or reconstruct visual dynamics, leaving a clear separation between perception- and generation-oriented paradigms. To close this divide, unified video foundation models have recently emerged, seeking to integrate understanding, generation, and editing within a single architecture. Representative works such as Chameleon [ 45 ] , Transfusion [ 74 ] , Show-o [ 62 ] , Emu3 [ 55 ] , and UNIC [ 66 ] jointly train autoregressive and diffusion objectives to unify decoding across text and visual tokens. Further developments like NExT-GPT [ 61 ] , Janus-Pro [ 5 ] , BAGEL [ 9 ] , Mogao [ 28 ] , CoDi-2 [ 44 ] , Omni-Video [ 43 ] and UniVideo [ 56 ] incorporate large language models with 3D visual tokenizers and causal VAEs to achieve bidirectional reasoning over text, image, and video modalities.

[16] figure: Benchmarks Style Subject Action Backg. Lighting Color Spatial Relationship Camera AuroraCap ✗ ✓ ✗ ✓ ✗ ✗ ✗ ✓ VGenEval ✓ ✓ ✓ ✓ ✓ ✗ ✓ ✓ ShotBench ✗ ✗ ✗ ✗ ✓ ✗ ✗ ✓ FETV ✗ ✓ ✓ ✓ ✓ ✗ ✗ ✗ VBench ✗ ✓ ✓ ✓ ✗ ✓ ✓ ✗ VBench2.0 ✗ ✓ ✓ ✓ ✗ ✗ ✓ ✓ Charades ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✗ YouCook ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ MPII-MD ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✗ EvalCrafter ✓ ✓ ✗ ✓ ✗ ✗ ✗ ✓ TGVE ✓ ✓ ✗ ✓ ✗ ✗ ✗ ✗ TGVE ✓ ✓ ✗ ✓ ✗ ✗ ✗ ✗ UNIC ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✓ FiVE ✗ ✓ ✓ ✗ ✗ ✓ ✗ ✓ VE-Bench ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✗ CC-Edit ✗ ✓ ✓ ✓ ✗ ✗ ✗ ✓ UniVBench ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ Table 2 : Comparison of cinematic dimensions across different video evaluation benchmarks.

[17] h3: 2.2 Video Benchmark

[18] p: Early video understanding benchmarks like M-VAD [ 46 ] and MPII-MD [ 49 ] focused on single-shot video captioning with limited scale. Larger benchmarks such as MSR-VTT [ 63 ] and ActivityNet [ 23 ] expanded dataset size and introduced multi-shot content, enabling evaluation of temporal reasoning and long-form video understanding. More recent efforts like AuroraCap [ 4 ] and ShotBench [ 29 ] have improved annotation quality and introduced shot-level analysis. However, these benchmarks primarily use web-scraped videos, raising potential copyright and data contamination concerns when evaluating models trained on large-scale internet data.

[19] p: With the emergence of text-to-video models, specialized generation benchmarks have been developed. Early works like FETV [ 31 ] and MQT [ 7 ] introduced basic quality metrics, while VBench [ 18 ] established a comprehensive evaluation framework with 16 dimensions covering quality, semantics, and temporal consistency. Subsequent benchmarks like GenAIBench [ 24 ] , LGVQ [ 71 ] , T2VQA-DB [ 22 ] expanded evaluation to include subjective quality assessment and diverse generation scenarios. Recent efforts like VBench2.0 [ 73 ] , Q-Eval [ 72 ] , and AIGVE-60K [ 51 ] have scaled up evaluation with larger test sets and more refined metrics. However, all existing generation benchmarks focus exclusively on text-to-video synthesis, lacking support for reference-guided generation or editing.

[20] p: Video editing benchmarks has primarily focused on instruction-following capabilities. CCEdit [ 13 ] and TGVE [ 59 ] pioneered text-guided editing assessment, measuring both editing accuracy and video quality preservation. TGVE+ [ 39 ] and VE-Bench [ 42 ] extended evaluation to more complex editing scenarios with fine-grained metrics. Recent works like UNIC [ 67 ] introduced reference image-based editing, while VACE-Bench [ 21 ] attempted to unify multiple editing modalities. FIVE [ 27 ] provided adversarial test cases for robust editing evaluation. Despite these advances, existing editing benchmarks are limited to single-shot videos and do not support multi-shot content, which is essential for evaluating real-world video editing capabilities.

[21] p: Overall, current benchmarks suffer from three critical limitations: they are task-specific, restricted to single-shot scenarios, and understanding benchmarks often use copyrighted content that may contaminate evaluation. Our UniVBench addresses all these limitations by providing the first multi-task, multi-shot benchmark with copyright-free content, enabling comprehensive evaluation across the full spectrum of video tasks.

[22] figure: Tasks : ①: V2T ②: T2V ③: R2V ④: TV2V ⑤: RV2V ⑥: V2V Evaluation Method Fine-grained Multi-shot Multi-dimension Task BLEU [ 34 ] ✗ ✓ ✗ ① CLIPScore [ 17 ] ✗ ✗ ✓ ② CIDEr [ 48 ] ✗ ✓ ✗ ① FVD [ 47 ] ✗ ✗ ✓ ② CLIPSIM [ 22 ] ✗ ✗ ✓ ② LPIPS [ 70 ] ✗ ✗ ✗ ② LLM-as-a-Judge [ 26 ] ✓ ✓ ✗ ① ∼ \sim ⑥ UniV-Eval ✓ ✓ ✓ ① ∼ \sim ⑥ Table 3 : Comparison of core capabilities across existing evaluation metrics and our proposed agent-based evaluation system. “-” indicates the metric is not applicable to this dimension.

[23] h3: 2.3 Video Evaluation Methods

[24] p: Video evaluation has traditionally relied on task-specific metrics that lack the flexibility required for unified assessment. For video understanding, BLEU [ 34 ] and CIDEr [ 48 ] measure n-gram overlap between generated and reference captions, providing coarse-grained quality scores but failing to capture semantic nuances or fine-grained errors. For video generation, metrics like FVD [ 47 ] assess distributional similarity between generated and real videos, while CLIPScore [ 17 ] and CLIPSIM [ 22 ] measure semantic alignment between videos and text prompts. LPIPS [ 70 ] evaluates perceptual similarity for frame-level reconstruction. For video editing, evaluation typically combines multiple metrics, using LPIPS [ 70 ] for background preservation, CLIPScore [ 17 ] for instruction alignment, and frame-by-frame comparisons for temporal consistency. However, these metrics are fundamentally limited: they operate at the video or dataset level without fine-grained error attribution, most cannot handle multi-shot videos, and each is designed for a specific task, limiting cross-task comparison.

[25] p: Recent work [ 18 , 73 , 51 , 26 ] has explored LLM-as-a-Judge approaches that use vision-language models to provide qualitative assessments across multiple tasks. While these methods offer flexibility and can handle diverse inputs including editing scenarios, they typically produce single overall scores without multi-dimensional analysis, limiting their diagnostic value for model development. Overall, no existing evaluation method simultaneously provides fine-grained analysis, multi-shot support, multi-dimensional scoring, and cross-task applicability. Our agentic evaluation system addresses these limitations by decomposing evaluation into interpretable dimensions, providing shot-level attribution, and maintaining consistent criteria across all video tasks.

[26] h2: 3 UniVBench

[27] h3: 3.1 Dataset Construction

[28] h4: Video Synthesis.

[29] p: To ensure comprehensive cinematic coverage, we adopt eight fundamental dimensions from prior works [ 64 , 24 , 14 , 18 ] and extend them with 21 fine-grained sub-dimensions (Figure 1 ): style, subject (category, quality, appearance), action, background, camera (focus, shot size, motion, perspective, angle, height, techniques), lighting (direction, brightness, effect), color (hue, contrast, saturation), and spatial relationships(iter-frame/subject layout, camera-subject position). We pre-classify categories for each sub-dimension (e.g., styles: realistic, animation, 2D; camera movements: static, zoom, pan, tracking; lighting: daylight, golden hour, studio).

[30] p: We recruit 15 professional experts with video production backgrounds who receive detailed training on our dimension taxonomy and annotation guidelines. For script writing, annotators sample random category combinations and compose detailed narratives specifying all dimension attributes shot-by-shot. Each multi-shot script must maintain narrative coherence across shots while covering diverse dimension values. Scripts undergo peer review where a second annotator verifies dimension coverage and coherence before generation.

[31] p: We generate videos using top commercial APIs (Hailuo, Kling, Veo3) and apply three-stage human-in-the-loop filtering: (1) automated pre-filtering removes watermarks and IP content via vision-language models, (2) three trained reviewers independently verify each video’s adherence to script specifications across all eight dimensions, accepting only videos with unanimous agreement, (3) quality specialists inspect for artifacts, unnatural motion, and temporal inconsistencies. Videos failing any stage are regenerated or discarded. On average, each video undergoes 2.3 generation attempts before approval. This rigorous process yields 100 single-shot and 100 multi-shot videos (avg. 3.72 shots).

[32] figure: Figure 2 : Workflow of UniV-Eval. The system accepts arbitrary inputs within a task setting and performs dynamic evaluation after planning and decomposition. The final results are delivered as a fine-grained checklist, providing traceable feedback for training optimization.

[33] h4: Detailed Captioning.

[34] p: We generate dimension-complete ground-truth captions using Gemini 2.5 Pro through: (1) dimension-wise extraction for all eight dimensions and sub-dimensions, (2) synthesis into coherent, shot-level descriptions. Three annotators then independently verify each caption against the source video, checking dimension completeness and temporal accuracy. GPT-4o provides additional automated verification by cross-checking factual claims. Captions with any disagreement undergo collaborative review where annotators discuss discrepancies and produce corrected versions. Each caption is revised an average of 1.8 times before finalization.

[35] p: Reference Images. To construct a diverse reference image sets for R2V, RV2V tasks, we generate high-fideility reference images using Gemini 2.5 Flash Image (Nano Banana) and Seedream4.0 [ 37 ] . We firstly define three type of reference images: subject, style, and scene. For subject, we also define human subjects, animals, non-living objects(clothes, paper, etc.,). For style, it mainly covers 6 major styles: animation(2D, 3D), real(cinematic style, ), arts(Japanese ukiyoe style), sci-fi(cyberpunk style, wasteland style), dressing (rococo, lolita), and materials(clay animation style, building block style). For background, it is divied into natural (with different seasons, weather and time), human crafted (street, buildings), and vritual (magic library) scenes. The generated images are also carefully picked to ensure quality and prevent any infringement. Finally, 864 unique and diverse images are created for reference image related tasks.

[36] p: Video2Video Reconstruction. We innovatively propose a new task, Video2Video reconstruction, to evaluate the performance of unified models in both understanding and generation tasks. Specifically, this task first requires the model to understand a video and generate corresponding detailed captions, then reconstruct the video based on the generated text. By directly comparing the reconstructed video with the original one, we can assess the unified model’s capabilities in understanding and generation. A high-quality unified model should first generate excellent captions through understanding, and second produce high-quality videos based on text. Failure in either task will result in a significant discrepancy between the reconstructed video and the origin.

[37] h3: 3.2 UniV-Eval

[38] p: We first introduce the evaluation tasks and corresponding evaluation strategies encompassed by our proposed unified evaluation system. Existing evaluation approaches typically assess the performance of video understanding and generation models on isolated tasks, in a decoupled manner, lacking a unified and integrated evaluation framework. Meanwhile, these methods often oversimplify the evaluation process, which leads to several potential risks: First, producing a single scalar score can severely limit interpretability, failing to reveal fine-grained distinctions between the model’s strengths and weaknesses. As a result, evaluations based solely on aggregate metrics make it challenging to provide actionable feedback for refinement during training. Second, assessing high-quality generation inherently involves complex, multifaceted, and dynamic dimensions. Fixed evaluation criteria may fail to accommodate diverse video attributes. For instance, some test cases emphasize the faithful reconstruction of visual instances, while others prioritize narrative coherence over instance-level fidelity.

[39] p: Therefore, in contrast to performing single-valued and fixed-dimension evaluations of video generation quality, we propose a dynamically adaptive, fine-grained agentic system UniV-Eval that decomposes overall “generation performance” into a set of interpretable, multidimensional checklists. This design enables a more comprehensive and diagnostic assessment of model capability beyond conventional single-score evaluations. Specifically, as a complementary component to UniVBench, our evaluation system centers on the user instruction and standardizes the prompting and instruction parsing procedures across tasks. Given any input (source video, reference image, and reference text), the system enables the evaluation of any output (including both video and text) in a unified and consistent manner.

[40] h4: Decomposing and Planning.

[41] p: Due to the current limitation on model generation length, a long video 𝒱 \mathcal{V} is mechanically segmented into multiple clips 𝒱 = { 𝒄 i } i = 1 C \mathcal{V}=\{\bm{c}_{i}\}_{i=1}^{C} for both generation and evaluation. As illustrated in Figure B6 (a), the proposed agent system UniV-Eval first decomposes each clip-level input into shot-level units for evaluation. Specifically, the multi-shots video is segmented as V = { v 1 , v 2 , … , v n } V=\{v_{1},v_{2},...,v_{n}\} using PySceneDetect 1 1 1 A tool designed to extract the minimal sub-shots from multi-shot videos. , thereby determines the number n n of shot-level units in a single clip.

[42] p: Meanwhile, the shot_classification agent aligns the reference images I I and initial user instruction T T with their corresponding shots: I = { i 1 , i 2 , … , i n } I=\{i_{1},i_{2},...,i_{n}\} and T = { t 1 , t 2 , … , t n } T=\{t_{1},t_{2},...,t_{n}\} , resulting in a set of shot-level inputs ( v , i , t ) (v,i,t) that serve as the foundation for subsequent evaluation. Notably, in the proposed system, all input modalities are optional, allowing flexible combinations of inputs depending on the evaluation scenario.

[43] h4: Shot-level Fine-grained Evaluation.

[44] p: Let the output of the tested model as o_1, combining with the input tuple ( v , i , t ) (v,i,t) , we invoke the shot_evaluation agent to perform assessment. To ensure fine-grained scene and visual understanding at the shot level, we design nine major category groups: subject, relative_position, actions, background&scene, color_info, lighting_info, video_style, atmosphere and camera_info [ 6 , 40 , 15 , 36 , 10 ] , as shown in the checklist of Figure B6 (b). Each major category is further decomposed into specific, interpretable subcategories (21 in total) that the shot_evaluation agent scores and reports, enabling diagnostic, fine-grained feedback at the shot level.

[45] p: The shot_evaluation agent performs per-category comparisons between the model output o_1 and the input tuple ( v , i , t ) (v,i,t) , producing a structured weakness checklist that highlights fine-grained deficiencies useful for targeted training optimization. This checklist is then forwarded to an evaluation_score agent , which aggregates the diagnostic signals and issues final scores along six evaluation dimensions for quantitative performance comparison.

[46] h2: 4 Experiments

[47] figure: Task Models Subject Background Action Camera Color Lighting Video Style Relative Position Average Understanding (V2T) Gemini 2.5 Pro ‡ 54.4% 57.8% 27.0% 54.1% 65.8% 63.8% 65.4% 44.4% 54.1% Seed 1.6 ‡ 46.3% 46.9% 22.3% 42.8% 54.6% 49.7% 45.9% 33.8% 42.8% Qwen3-VL-30B § 15.8% 14.6% 6.4% 17.6% 25.3% 27.1% 24.1% 9.8% 17.6% AuroraCap § 16.7% 14.4% 6.9% 17.8% 23.9% 26.4% 25.2% 10.8% 17.8% Tarsier2 § 34.3% 25.0% 32.7% 20.9% 7.7% 4.4% 20.1% 21.9% 21.9% Showo-2 § 25.9% 22.2% 10.6% 16.3% 13.7% 11.3% 18.3% 12.3% 16.3% Generation (T2V) Seedance-1.0-Pro ‡ 68.8% 65.2% 74.3% 76.5% 84.8% 83.4% 76.8% 91.6% 77.9% Wan2.2-14B § 70.0% 79.7% 62.1% 72.2% 81.6% 69.2% 79.9% 90.0% 74.9% CoDi-2 § 6.1% 15.6% 25.0% 44.7% 54.6% 55.7% 37.1% 83.4% 40.1% Omni-Video § 45.0% 52.6% 41.2% 49.6% 67.6% 66.2% 60.6% 66.5% 56.2% CogVideoX § 42.6% 62.9% 33.9% 61.7% 82.0% 83.2% 77.8% 81.3% 65.7% Generation (R2V) Seedance-1.0-Lite ‡ 64.7% 68.2% 39.8% 63.1% 75.4% 74.2% 73.8% 74.4% 66.7% Editing (TV2V) Wan2.1-VACE-14B § 66.3% 51.2% 45.3% 62.5% 75.3% 68.9% 72.5% 78.4% 65.1% Editing (RV2V) Wan2.1-VACE-14B § 53.1% 57.3% 71.1% 70.5% 70.1% 74.1% 64.0% 71.2% 66.4% Reconstruction (V2V) Omni-Video § 20.7% 29.1% 19.8% 71.5% 59.8% 63.3% 37.3% 81.6% 47.9% Wan2.1-VACE-1.5B § 7.1% 6.9% 29.0% 69.2% 32.7% 37.0% 17.6% 79.5% 34.9% Wan2.1-VACE-14B § 56.4% 60.4% 68.2% 77.5% 40.9% 66.7% 51.3% 79.9% 62.7% CogVideoX-1.5-5B § 4.6% 6.1% 12.7% 47.2% 15.4% 34.8% 6.7% 37.8% 20.7% Note: Model types are separated into: ‡ Commercial Models, § Open-Source Models. Table 4 : Performance comparison of different baselines on UniVBench, summarizing results over six tasks, across eight dimensions.

[48] figure: Figure 3 : Case Study Analysis of UniVBench in T2V and Reconstruction Task. T2V generation uses the ground truth text of the video, while V2V reconstruction relies on model’s understanidng text. The generated videos are selected from OmniVideo

[49] h3: 4.1 Implementation Details

[50] p: For a fair and reproducible comparison, we evaluate all baselines under a unified experimental protocol. For commercial large multimodal models such as GPT-5, Gemini 2.5 Pro [ 8 ] , Seed 1.6 [ 16 ] , and Seedance-1.0-Lite [ 14 ] , we directly access their official inference APIs released in late 2025. For open-source baselines, including CogVideoX [ 65 ] , CoDi-2 [ 44 ] , Omni-Video [ 43 ] , Wan2.1-VACE [ 50 ] , and other video generation or editing models, we use their official codebases and pre-trained checkpoints. All models use consistent inference settings: 50 DDIM sampling steps, classifier-free guidance scale of 7.5, and native resolution (typically 720×480 for 16:9 videos). All models are executed under consistent settings, including fixed sampling steps, classifier-free guidance scales, and resolution configurations aligned with their default or recommended parameters. When models lack native support for certain tasks, we implement minimal adaptations: for TV2V editing, we concatenate instruction text with source video embeddings; for RV2V editing, we inject reference image features into the diffusion process at intermediate layers. We use Seed-1.6 [ 16 ] as the evaluation LLM.

[51] p: All models receive identical inputs per task: ground-truth captions for T2V generation, source videos and editing instructions for TV2V, reference images and prompts for R2V. For V2V reconstruction, we first generate captions using each model’s understanding component (or GPT-4o for generation-only models), then reconstruct using those captions. Video inputs are center-cropped and resized to each model’s expected resolution while maintaining aspect ratio. All outputs undergo evaluation by our agentic system using identical prompts, rubrics, and dimension weightings, ensuring differences in scores reflect model capabilities rather than evaluation variance. All experiments are conducted on 8 NVIDIA H100 GPUs 80GB.

[52] h3: 4.2 Main Results

[53] p: Our comprehensive evaluation on UniVBench, summarized in Table 4 , reveals a distinct specialization among current video models, highlighting the performance gap between systems designed for single task versus those for unified tasks. More experiments are provided in the supplementary materials.

[54] h4: Task-Specific Leaders.

[55] p: In the video understanding (V2T) task, Gemini 2.5 Pro demonstrates superior performance with an average score of 54.1%, significantly outpacing other models. Conversely, unified video models like Showo-2 score (16.3%) in this domain, showcasing their lack of perceptual reasoning. For text-to-video (T2V) generation, Seedance-1.0-Pro achieves the top score of 77.9%. For reconstruction (V2V), Wan2.1-VACE-14B delivers the strongest performance, with scores of 62.7%.

[56] h4: Cross-Dimensional Insights.

[57] p: A key observation across all tasks is the difficulty models have with the ‘Action’ dimension, which frequently receives the lowest scores, particularly in video understanding. This suggests that accurately interpreting and synthesizing complex temporal dynamics remains a major challenge. In contrast, generative models exhibit greater control over stylistic attributes like ‘Color’, ‘Lighting’, and ‘Video Style’, where they often achieve their highest scores.

[58] h4: The Unification Gap.

[59] p: Overall, the results quantitatively indicates that no single model currently excels across the full spectrum of understanding, generation, and editing. The benchmark effectively maps the strengths and weaknesses of existing architectures, providing a clear and necessary baseline to guide future efforts in developing truly unified video foundation models.

[60] h3: 4.3 Analysis

[61] h4: Reconstruction Case Study.

[62] p: We present qualitative results in Figure 3 , where T2V generation leverages the video’s ground truth text and reconstruction relies on the model’s self-derived understanding text. A comparison of these three sets of videos reveals varying degrees of inconsistency. Notably, the V2V task exhibits more pronounced inconsistencies than its T2V counterpart, indicating information transmission loss during the V2T → T2V pipeline. Collectively, these findings clearly highlight the inherent weaknesses of current unified video models.

[63] figure: Figure 4 : An example of evaluation using different metrics, where the blue-highlighted part shows that UniV-Eval provides more detailed, traceable validation and assessment.

[64] h4: Metrics Case Study.

[65] p: To qualitatively demonstrate the superiority of the proposed UniV-Eval over previous metrics, we present a case study in Figure 4 . BLEU Score measures the lexical overlap between candidate and reference texts, yet in V2T tasks, the varying effective caption lengths across models can substantially distort BLEU scores. Meanwhile, conventional LLM-as-a-Judge approaches offer fine-grained feedback, but typically consider limited evaluation dimensions and still lack interpretability. In contrast, as shown in Table 3 , UniV-Eval implements a fine-grained dynamically adaptive evaluation strategy.

[66] figure: Figure 5 : Human expert annotations used to validate the reliability of UniV-Eval.

[67] h4: Human Study.

[68] p: To assess the reliability of UniV-Eval, we randomly sampled 10% of the data and conducted a three-fold cross-validation study. Human experts reviewed each sample with reference annotations and provided the corresponding labels. As shown in Figure 5 , UniV-Eval achieves a high alignment with human judgments, with an average agreement of nearly 85%, demonstrating that the proposed metric faithfully reflects human annotations.

[69] h2: 5 Conclusion

[70] p: UniVBench addresses a critical gap in video foundation model evaluation by providing the first unified framework to comprehensively assess understanding, generation, editing, and reconstruction capabilities. Our benchmark comprises 200 high-quality, multi-shot videos with comprehensive annotations including detailed captions, multi-format editing instructions, and reference images. We establish systematic evaluation across eight fundamental cinematic dimensions decomposed into 21 fine-grained sub-dimensions, providing complete coverage where existing benchmarks exhibit fragmented evaluation of subsets.

[71] p: Our unified agentic evaluation system standardizes assessment across all six tasks with multi-dimensional, shot-level scoring that enables interpretable analysis, direct cross-task comparison, and precise attribution of failures to perception versus generation components—capabilities absent in existing metrics relying on single scalar scores. Through this comprehensive framework spanning professional-grade cinematic evaluation, multi-shot temporal assessment, and unified cross-task metrics, UniVBench establishes a principled foundation for measuring progress toward general-purpose, instruction-following video intelligence.

[72] h2: 6 Limitation and Future Works

[73] p: This work focuses on establishing a unified benchmark for evaluation and does not introduce a new model architecture. A primary limitation is the current scale of our dataset; while the 200 richly annotated videos are sufficient for comprehensive evaluation, they are not enough to train a large-scale unified video model from the ground up. Therefore, a crucial direction for future work is to significantly expand the UniVBench dataset in volume. Looking ahead, our goal is to leverage this expanded benchmark to train and validate novel Unified Video Models, using the insights gained from our evaluation framework to drive the development of more integrated and capable systems.

[74] h2: 7 Acknowledgement

[75] p: This work is supported by the National Key R&D Program of China (Grant No. 2024YFC3308304), the ”Pioneer” and ”Leading Goose” R&D Program of Zhejiang (Grant no. 2025C01128), and the ZJU-Angelalign R&D Center for Intelligence Healthcare.

[76] h2: References

[77] p: Supplementary Material

[78] h2: Appendix A Evaluation Cases

[79] p: In this section, we presents the evaluation resulst in different tasks. In Figure A1 and A2 , we present the source video and the reference captions we provided, along with generated video from CogVideoX, OmniVideo and Wan2.2-15B. In Figure A3 , we present the results of reference images to video generation by Seedance-Lite.

[80] p: From the rows of images, we can see that current video generation models still struggle to meet the text requirements. In Figure A1 , the two animals enter the frame and walk to the front of the camera and wave hands are not captured by CogVideoX and OmniVideo. In Figure A2 , the dinosaur-shaped pet bed opens when the cat enters. CogVideoX and OmniVideo’s results didn’t conform to it. In Figure A3 , the referenced subject has serious identity shift when cut to the next shot. These qualitative results show that current video generation models still have large room for improvements.

[81] figure: Figure A1 : Examples of T2V generation results across different baselines

[82] figure: Figure A2 : Examples of T2V generation results across different baselines

[83] figure: Figure A3 : Examples of R2V generation results of Seedance-Lite

[84] h2: Appendix B More Details of UniVBench

[85] h3: B.1 Captioning Meta Data Distribution

[86] p: In Figure B4 , we provided the video content distribution across each sub-dimensions. This indicates that our dataset is semantically rich and diverse.

[87] figure: Figure B4 : The meta-data distribution of video content.

[88] h3: B.2 Captioning Prompt

[89] p: In this subsection, we release our system prompts to generate dense video captions for our benchmark construction. They are shown in Figure B7 to B13 . The prompts are divided into two steps: First, the model is tasked to extract the necessary content attributes from the video. This can include: subjects, actions, background, camera information, color, lighting, video style, etc., Then, the model merges them together to generate a coherent and structured video script, the format is shown in Figure B5 . The essence of a video script format is: first describes the fixed, unchanging content, including the overall style and atmosphere of the video. Then, specify the information of the video’s first frame, such as the subjects appearing in the first frame, their positions, and initial states. Subsequently, output subject actions, camera movements, and any changing information in chronological order—including adjustments to the relative positions of subjects and camera parameters. If the video is multi-shot, appending the keyword: Shot cut, and repeate the first frame description, subject actions, camera movements in chronological order.

[90] figure: Figure B5 : The script format used to generate the coherent video captions. Red font indicates the content model needs to fill in. Green font indicates the explanation of each field.

[91] figure: Figure B6 : Evaluation case of LLM as judge and human

[92] figure: Figure B7 : Captioning prompts used to generate detailed video captions.

[93] figure: Figure B8 : Captioning prompts used to generate detailed video captions.

[94] figure: Figure B9 : Captioning prompts used to generate detailed video captions.

[95] figure: Figure B10 : Captioning prompts used to generate detailed video captions.

[96] figure: Figure B11 : Captioning prompts used to generate detailed video captions.

[97] figure: Figure B12 : Captioning prompts used to generate detailed video captions.

[98] figure: Figure B13 : Captioning prompts used to generate detailed video captions.

[99] h2: Appendix C Evaluation System Prompt

[100] p: In this section, we provide a detailed description of the system prompts used in UniV-Eval, organized by task categories. Specifically, we present the system prompts corresponding to the six major tasks: V2T (Figure F14 ), T2V (Figure F15 ), R2V (Figure F16 ), TV2V (Figure F17 ), RV2V (Figure F18 ), and V2V (Figure F19 ).

[101] p: It is important to note that, for the V2T task, the evaluation prompt must be used together with a predefined template (Figure F20 ), since the final comparison is conducted between the ground-truth caption and the baseline caption. For the other tasks, the comparison rules for generic objects are illustrated in Figure F21 . In practice, these components should be combined to form the complete system prompt used for evaluation.

[102] h2: Appendix D Evaluation Cost

[103] p: Average cost of running one case is provided in Table D1 . The cost of evaluating one task is less than 10 US dollars.

[104] figure: V2V TV2V R2V RV2V T2V V2T I/O total tokens 25104 25898 16743 27534 19567 1413 Times (s) 45 62 44 55 49 27 Table D1: The cost of evaluation

[105] h2: Appendix E Potential LLM-as-Judge Bias

[106] p: Self-preference bias exists when the same LLMs act as both evaluatee and evaluator, they can recognize their own outputs and give higher scores, which is well-discussed in existing work [ 33 ] . In our settings, evaluatee and evaluators are different. The evaluatee models are video generation models, while the evaluator models are vision-language models. These two models differ significantly in both their architectural designs and training data.

[107] h2: Appendix F Evaluation cases

[108] p: Here we provide a evaluation case in Figure B6 between human and LLM-as-Judge. While the judge model conducts meticulous, all-dimensional evaluations, it overlooks critical issues. Human evaluators, by contrast, focus on salient errors and ignore subtle details. Below is a case analysis. The model evaluates that: the cucumbers in the video have a smooth surface, without the wrinkled texture and white dots in the reference image [ orange region]; While human evaluates that the the cucumber is cut sideways [ red region], which conflicts with the slices on the cutting board.

[109] figure: Figure F14 : Captioning prompts used to generate detailed video captions.

[110] figure: Figure F15 : Evaluation prompts used for V2T task.

[111] figure: Figure F16 : Evaluation prompts used for R2V task.

[112] figure: Figure F17 : Evaluation prompts used for TV2V task.

[113] figure: Figure F18 : Evaluation prompts used for RV2V task.

[114] figure: Figure F19 : Evaluation prompts used for V2V task.

[115] figure: Figure F20 : Evaluation Json template used for V2T task.

[116] figure: Figure F21 : Evaluation Json template used for V2T task.

[117] h2: Instructions for reporting errors

[118] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[119] p: Tip: You can select the relevant text first, to include it in your report.

[120] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[121] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
