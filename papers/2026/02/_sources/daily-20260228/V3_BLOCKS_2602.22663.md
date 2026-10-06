[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline

[3] h6: Abstract

[4] p: Vision-Language-Action (VLA) models have emerged as a generalist robotic agent. However, existing VLAs are hindered by excessive parameter scales, prohibitive pre-training requirements, and limited applicability to diverse embodiments. To improve the practicality of VLAs, we propose a comprehensive benchmark and an improved baseline. First, we propose CEBench, a new benchmark spanning diverse embodiments in both simulation and the real world with consideration of domain randomization. We collect 14.4k simulated trajectories and 1.6k real-world expert-curated trajectories to support training on CEBench. Second, using CEBench as our testbed, we study three critical aspects of VLAs’ practicality and offer several key findings. Informed by these findings, we introduce LLaVA-VLA, a lightweight yet powerful VLA designed for practical deployment on consumer-grade GPUs. Architecturally, it integrates a compact VLM backbone with multi-view perception, proprioceptive tokenization, and action chunking. To eliminate reliance on costly pre-training, LLaVA-VLA adopts a two-stage training paradigm including post-training and fine-tuning. Furthermore, LLaVA-VLA extends the action space to unify navigation and manipulation. Experiments across embodiments demonstrate the capabilities of generalization and versatility of LLaVA-VLA , while real-world mobile manipulation experiments establish it as the first end-to-end VLA model for mobile manipulation. We will open-source all datasets, codes, and checkpoints upon acceptance to foster reproducibility and future research.

[5] figure: Fig. 1: Overview of this work. We conduct a comprehensive study on the practicality of vision-language-action models. We first construct a cross-embodiment benchmark, CEBench, across simulation and the real world, and offer diverse evaluation settings. Then we explore three critical aspects (Q1-Q3) and offer several key findings. Based on the above findings, we introduce our LLaVA-VLA, a lightweight yet effective baseline capable of mobile manipulation.

[6] h2: I INTRODUCTION

[7] p: The emergence of Vision-Language-Action (VLA) [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 ] models has revolutionized the field of robotics, offering powerful capabilities in visuomotor control and the comprehension of complex instructions through end-to-end learning processes. These models have demonstrated their potential in various robotic tasks, enabling systems to interpret multimodal sensory data and execute actions based on language instructions. However, despite their success, current VLAs face significant hurdles that impede their widespread deployment and practical use in real-world scenarios: 1) Billions of parameters make them difficult to deploy in resource-constrained environments, such as mobile platforms and consumer-grade devices. 2) Extensive pre-training using large-scale robotic datasets leads to prohibitive training costs and the need for vast computational resources. 3) Fixed-base manipulation limits their applicability to cross-embodiment deployment, i.e. , mobile manipulation tasks.

[8] p: Existing work has partly investigated some of the aforementioned issues. TinyVLA [ 12 ] introduced a 1B-level model trained from scratch. It employs Low-Rank Adaption [ 13 ] and diffusion head for efficient training and inference. MiniVLA [ 14 ] is a variant of OpenVLA [ 15 ] with a smaller backbone and uses a VQ-VAE tokenizer to quantize actions, achieving fast and precise inference. NORA [ 16 ] utilizes FAST [ 17 ] to quantize action tokens and diffusion expert. SmolVLA [ 18 ] realizes efficient training through skipping layers, pruning visual tokens, and initializing a small VLM backbone. Despite these advances, these approaches have not systematically examined the practicality of their lightweight and pretraining-free designs, and they remain incapable of performing mobile manipulation tasks.

[9] p: To improve the practicality of VLAs, we propose a comprehensive benchmark and an improved baseline. First, we introduce CEBench, a practical robotic benchmark suite that spans diverse embodiments (single arm [ 19 ] , bimanual [ 20 ] , and mobile bimanual) in both simulation and the real world, with explicit consideration of domain randomization. In CEBench, we collect 14.4k simulated demonstrations across 36 tasks and 1.6k high-quality real-world demonstrations across 8 tasks.

[10] p: Second, using CEBench as our testboard, we study three critical aspects for VLAs: the lightweight designs, the training curriculum, and the unified action space, and empirically offer several valuable findings and insights into their choices. Informed by these findings, we propose LLaVA-VLA, a lightweight VLA with strong performance, which is capable of mobile manipulation . Figure 1 shows that LLaVA-VLA does not need pre-training and can be trained and deployed on consumer-grade GPUs. LLaVA-VLA initializes a compact VLM and integrates multi-view input, proprioception tokenization, and action chunking to balance efficiency and performance while maintaining minimalist model design. To eliminate the reliance on pre-training, we further adopt a two-stage training paradigm, combining post-training on multi-task data with fine-tuning on task-specific data. Finally, we design a unified action space including a specific action space for navigation and a manipulation action space combined through several special tokens.

[11] p: Extensive evaluation of our LLaVA-VLA on CEBench shows that it matches or surpasses models over 10× larger, especially under domain-randomized settings, which demonstrates its strong visual generalization capabilities. LLaVA-VLA successfully manages tasks like move to the operation table from outside and place the bottle , which indicates that LLaVA-VLA is the first end-to-end VLA model capable of handling mobile manipulation tasks. Cross-embodiment experiments demonstrate the versatility of our model and the effectiveness of the proposed hybrid action space design. This work represents a promising step toward democratizing VLAs by making them lightweight, generalized, and practical for deployment in mobile embodied systems.

[12] p: To summarize, our key contributions are:

[13] p: We construct a benchmark to evaluate the practicality of VLAs, which spins diverse embodiments in both simulation and the real world, and considers domain randomization.

[14] p: We conduct a comprehensive study on the practicality of VLAs and offer several insightful findings.

[15] p: We propose an improved baseline, LLaVA-VLA, which is lightweight, pretraining-free, and capable of mobile manipulation.

[16] p: We will release all datasets, codes, and checkpoints upon acceptance to provide a reference for future research in open-source VLAs.

[17] h2: II RELATED WORKS

[18] h3: II-A Vision-Language Models

[19] p: Vision-Language Models (VLMs) [ 21 , 22 , 23 ] have rapidly advanced and extended the success of Large Language Models (LLMs) [ 24 , 25 ] into multimodal domains. By incorporating visual modalities, these models achieve impressive performance on tasks requiring visual reasoning and understanding. At the embedding level, a representative line of work leverages vision encoders such as CLIP [ 26 ] or SigLIP [ 27 ] to embed visual information into the language space. Through large-scale multistage alignment training [ 28 , 29 ] , these models significantly enhance cross-modal alignment and exhibit strong visual reasoning abilities. These developments in language and vision further inspire extensions to other modalities, including action, touch, and sound.

[20] h3: II-B VLA Models

[21] p: Early works such as [ 1 , 2 , 3 ] trained transformers from scratch on web-scale vision-language data and large-scale robot trajectories to improve performance and generalization. RoboFlamingo [ 30 ] adapted pre-trained VLMs to manipulation via lightweight imitation learning. OpenVLA [ 15 ] released the first open-source 7B VLA trained on public data. OpenHelix [ 31 ] proposed a dual-system dual-system architecture. More recently, GR00T N1 [ 32 ] advances general-purpose humanoid control with a diffusion-based action generator in a dual-system architecture. PD-VLA [ 4 ] and CEED-VLA [ 5 ] explored the acceleration of inference. ReconVLA [ 8 ] and FlowVLA [ 33 ] leveraged extra low-level visual perception. VLA-Adapter [ 34 ] proposes a lightweight, parameter-efficient bridge from pre-trained VLMs to action prediction. VLM4VLA [ 35 ] benchmarks how VLM choice affects VLA performance with minimal adaptation. However, these models remain computationally demanding and pose challenges for deployment in resource-constrained settings and mobile manipulation tasks.

[22] h2: III CEBench

[23] p: Prior benchmarks exhibit a significant gap in practical deployment, lacking comprehensive and unbiased evaluation across embodiments, potential domain randomization, and mobile manipulation needs. To bridge this gap, we propose Cross-Embodiment Benchmark ( CEBench ), a reliable benchmarking suite designed for systematic evaluation of practicality in VLAs. Notably, we treat CALVIN [ 19 ] as a subset of our dataset and mainly introduce our dataset in RoboTwin [ 20 ] and the real world.

[24] h3: III-A System Setup

[25] p: We evaluate our LLaVA-VLA in both simulated and real-world environments to comprehensively assess task performance and generalization.

[26] p: Single-arm manipulation. The CALVIN benchmark [ 19 ] includes a Franka Panda single robotic arm and a table environment to study long-horizon language-conditioned manipulation and visual generalization.

[27] p: Bimanual manipulation. The RoboTwin benchmark [ 20 ] , built on the Sapien [ 36 ] simulator, designed to evaluate positional generalization and visual robustness. It fosters an expert data synthesis pipeline that leverages VLMs and simulation-in-the-loop refinement to automatically generate task-level execution code.

[28] p: Bimanual mobile manipulation. Figure 2 shows the real-world experimental setup using the Cobot-Magic dual-arm mobile robot, equipped with four Piper robotic arms (two master arms and two puppet arms), which capture RGB images at a resolution of 480 × 640 and 30 Hz.

[29] figure: Fig. 2: Real-world setup of the Cobot-Magic system for mobile bimanual manipulation (top view).

[30] h3: III-B Datasets

[31] p: For CALVIN, we use the official datasets. On the RoboTwin platform [ 20 ] , we constructed a large-scale simulation dataset containing 14.4k trajectories and 36 tasks (400 trajectories per task) in an automatic manner. All trajectories were collected under a simplified scenario with a clutter-free tabletop and stable background and lighting. In the real world, we designed 8 tasks and collected 200 trajectories per task. The tasks include:

[32] p: Stack bowls : Pick the bowl and put it on the other.

[33] p: Restore bottle : Return a toppled bottle to its upright position.

[34] p: Click bell : Trigger a desk bell by pressing its small button.

[35] p: Place vegetable : Grasp a vegetable and correctly place it into the target container.

[36] p: Pack bottles : Insert two bottles neatly into a designated box.

[37] p: Lift pot : Grasp a pot with two arms and lift it off the table surface.

[38] p: These tasks cover different difficulties, from basic pick-and-place operations to more complex bimanual interactions. We also collect 2 mobile manipulation tasks:

[39] p: Move and fetch bottles : move to the table and fetch the bottle on it.

[40] p: Move and open the drawer : move to the drawer and open it.

[41] p: These data provide a solid foundation for systematic training and evaluation.

[42] h3: III-C Evaluation and Metrics

[43] p: For CALVIN, we follow the official evaluation setting and report the success rates of each sub-task as well as the average success length across 5 tasks. For RoboTwin, we select 8 representative tasks to ensure fair and efficient comparison: click bell , click alarmclock , lift pot , move can pot , open laptop , pick dual bottles , place dual shoes , rotate qrcode . The evaluation on RoboTwin is conducted on seen settings as well as unseen settings with domain randomization ( DR ), which includes clutter, random lighting, diverse textures, and variable table heights. For real-world experiments, we evaluate on all tasks in the datasets. To simulate the DR setting in reality, we vary the color and texture of the tabletop and randomly place distractor objects (e.g., blocks, pens ) in the workspace, creating visual and layout variations that were unseen in training.

[44] h3: III-D Baselines

[45] p: To comprehensively evaluate the performance of policies and VLAs with fewer than 1B parameters, we conduct comparisons with the following baselines in RoboTwin and the real world in Section V .

[46] p: ACT [ 37 ] : A CVAE-based imitation learning approach is proposed, which leverages action chunking to forecast sequences of upcoming actions and incorporates temporal ensembling to achieve smooth execution.

[47] p: Difussion policy [ 38 ] : A visuomotor policy learning framework that models action prediction through a conditional denoising diffusion process.

[48] p: TinyVLA [ 12 ] : A compact VLA model that leverages a lightweight multimodal backbone to efficiently generate robot actions from vision-language inputs, enabling fast inference and strong generalization across diverse tasks.

[49] p: RDT [ 39 ] : A Transformer model incorporating diffusion is proposed for bimanual robotic manipulation, which employs a unified action space and multimodal inputs to enable efficient few-shot learning across various tasks.

[50] p: For the CALVIN benchmark, we compare with representative methods on the official leaderboard.

[51] h2: IV LLaVA-VLA and Its Associated Findings

[52] p: To build a lightweight, pretraining-free, and cross-embodiment VLA for practical use, we systematically explore design choices of VLAs. Specifically, we formulate three research questions to guide our explorations:

[53] p: Q1: To what extent does model performance depend on parameter scale, and which techniques enable small models to achieve comparable performance to their larger counterparts?

[54] p: Q2: Is pre-training necessary for small models to accomplish tasks in specific scenarios?

[55] p: Q3: How to define a unified action space for cross-embodiment manipulation, including fixed-base and mobile ones?

[56] figure: Fig. 3: Model architecture of our LLaVA-VLA.

[57] h3: IV-A LLaVA-VLA

[58] p: We conduct our study in a top-down manner. We first present our Light weight VLA (LLaVA-VLA). As shown in Figure 3 , LLaVA-VLA is built upon a pre-trained LLaVA-OneVision-0.5B [ 40 ] backbone, taking concatenated multi-view images as input, augmented with proprioceptive signals, and producing action chunks through an action tokenizer. To enable mobile manipulation, we construct a hybrid action space consisting of direction tokens and their corresponding value tokens, which allows the model to seamlessly switch between navigation and manipulation. In the following part, we discuss the design choices made during its development step by step to provide the key findings (F1-F8).

[59] h3: IV-B Study on Lightweight Designs (Q1)

[60] p: Toward lightweight VLAs, we first investigate whether compact models can rival large-scale counterparts (F1), then identify the key design choices that make such performance attainable (F2-4).

[61] p: Key Findings 1: Model performance is not strictly proportional to parameter scale. Small VLAs can achieve performance comparable to their large-scale counterparts. Table I , LLaVA-VLA-0.5B achieves performance on par with 7B models despite less than 10% parameters. On the first sub-task, it reaches a success rate of 96.2%, comparable to 97.4% of its 7B counterpart. On the last task, it achieves 50.6%, significantly outperforming 23.5% of the 3B RoboFlamingo and 43.5% of the 7B OpenVLA. With an average action length of 3.65, it fully surpasses these larger models. These results suggest that performance gains are not solely determined by scale. With the proposed techniques, small VLAs can match or surpass larger models.

[62] figure: TABLE I: Comparison among different versions of LLaVA-VLA in terms of success rates and average length on RoboTwin. Here, B denotes billions. Model Param. Success Rate (%) Avg. Len. 1/5 2/5 3/5 4/5 5/5 ABC → \rightarrow D LLaVA-VLA (ours) 0.5B 96.2 84.8 72.6 60.8 50.6 3.65 LLaVA-VLA (ours) 7B 97.4 86.2 73.4 64.6 53.4 3.75 RoboFlamingo [ 30 ] 3B 82.4 61.9 46.6 33.1 23.5 2.47 OpenVLA [ 15 ] 7B 91.3 77.8 62.0 52.1 43.5 3.27

[63] p: Key Findings 2: Multi-view images are critical as they enable stereoscopic perception of 3D space, and containing multi-view information in 1 image is an effective way. In manipulation tasks, third-person view images provide global contextual information, while first-person view images offer precise object-to-gripper positional cues, which are crucial for achieving precise manipulation. While inheriting the above information, multi-view images capture disparity information, which is essential for constructing a three-dimensional understanding of the scene. Therefore, incorporating both perspectives is essential.

[64] p: Several strategies exist for handling multi-view inputs [ 41 , 42 ] . Encoding each image separately and then concatenating its image tokens typically leads to an excessive number of image tokens and introduces considerable redundancy, resulting in suboptimal performance. One potential remedy is to apply token compression methods to reduce visual token count. However, this approach may incur information loss, which may result in slight performance degradation. Consequently, we adopt a simpler yet effective strategy: vertically concatenating the first- and third-person view images into a single composite image. This approach not only reduces the number of tokens while preserving complete multi-view visual information, but also aligns with the training paradigm of our VLM backbone, thereby avoiding potential performance degradation.

[65] figure: TABLE II: Comparison of different methods for integrating multi-view images on CALVIN. Method Success Rate (%) Avg. Len. 1/5 2/5 3/5 4/5 5/5 ABC → \rightarrow D Concate Image Tokens 65.3 37.1 23.5 14.7 9.2 1.50 Merged Image 94.8 84.5 71.3 62.5 53.8 3.68

[66] p: Key Findings 3: Proprioception is critical as it improves understanding of physical states, and tokenizing proprioception works better than encoding them by linear layers. Proprioceptive information is critical for enabling robots to infer their current state and maintain action continuity. A common approach is to encode this information using an MLP. In our design, we translate proprioception values into a sequence of proprioception tokens via a proprioception tokenizer, which can be regarded as an inverse form of the action de-tokenizer. As shown in Table IV , this integration facilitates better exploitation of the VLM’s language modeling capabilities for understanding and generating coherent actions.

[67] figure: TABLE III: Comparison of different methods for integrating proprioceptive information on CALVIN. Method Success Rate (%) Avg. Len. 1/5 2/5 3/5 4/5 5/5 ABC → \rightarrow D MLP Projector 90.4 76.0 58.0 48.0 37.2 3.09 Prop. Tokenizer 94.8 84.5 71.3 62.5 53.8 3.68

[68] p: Key Findings 4: Action chunking is critical as it strengthens the model’s planning capability and action stability. Action chunking plays a pivotal role in manipulation tasks [ 37 ] . Training VLAs to predict action chunks implicitly endows them with planning capabilities and improves the temporal coherence of the generated actions. We employ this design and set the action chunking size to 5.

[69] figure: TABLE IV: Comparison of different chunk sizes in terms of average length on CALVIN. Chunk Size 1 5 12 20 Avg. Len. 2.25 3.68 3.35 0.70

[70] h3: IV-C Study on Training Curriculum (Q2)

[71] p: Key Findings 5: Cross-embodiment large-scale pre-training is not essential. Post-training on in-domain multi-task data is sufficient to establish the mapping from vision and language to action. Large-scale cross-embodiment pre-training often suffers from low-quality samples and discrepancies in action spaces, which limit its effectiveness. In contrast, domain-specific datasets are typically composed of high-quality demonstrations collected either in simulation or from human experts in real-world settings. Consequently, conducting post-training across multiple tasks within downstream datasets, followed by fine-tuning on a single task, emerges as a promising approach. In both real-world and simulated experiments with dual-arm configurations, we conduct the two-stage training paradigm, including post-training and fine-tuning, and make LLaVA-VLA achieves the best overall performance. This suggests that the vision-to-action mapping can be effectively learned from domain-specific data when training tasks provide sufficient diversity in goals and scenes.

[72] figure: TABLE V: Comparison of different training curricula on the seen tasks on RoboTwin. Training Curriculum Open Laptop Lift Pot Pre-training 20.0% 18.0% Post-training 38.0% 39.0%

[73] figure: TABLE VI: Comparison with various manipulation baselines on CALVIN. Category Method Params w/o Success Rate (%) Avg. Len. Pre-training 1/5 2/5 3/5 4/5 5/5 ABC → \rightarrow D Generative Methods 3D-VLA [ 43 ] ( ICML’24 ) 1B × \times 44.7 16.3 8.1 1.6 0 0.70 GR-1 [ 2 ] ( ICLR’24 ) 195M × \times 85.4 71.2 59.6 49.7 40.1 3.06 Vidman [ 44 ] ( NIPS’24 ) 1B × \times 91.5 76.4 68.2 59.2 46.7 3.42 Diffusion Policy 3D Diffuser Actor [ 45 ] ( CoRL’24 ) 70M ✓ 93.8 80.3 66.2 53.3 41.2 3.35 Large VLA Models RoboFlamingo [ 30 ] ( ICLR’24 ) 3B ✓ 82.4 61.9 46.6 33.1 23.5 2.47 OpenVLA [ 15 ] ( CoRL’24 ) 7B × \times 91.3 77.8 62.0 52.1 43.5 3.27 LLaVA-VLA (Ours) 500M ✓ 94.8 84.5 71.3 62.5 53.8 3.68

[74] figure: TABLE VII: Evaluation on RoboTwin benchmark. Success rates for 8 tasks on the Seen and DR settings. Best result in each row highlighted in Bold . Small Model w/o Pre-training Large Model Simulation Task ACT DP LLaVA-VLA (Ours) RDT Seen DR Seen DR Seen DR Seen DR Click Bell 4.0% 2.0% 54.0% 0.0% 81.0% 72.0% 80.0% 9.0% Click Alarmclock 11.0% 0.0% 61.0% 5.0% 73.0% 65.0% 61.0% 12.0% Lift Pot 7.0% 2.0% 31.0% 0.0% 39.0% 21.0% 72.0% 9.0% Move Can Pot 0.0% 0.0% 39.0% 0.0% 28.0% 16.0% 25.0% 12.0% Open Laptop 31.0% 0.0% 49.0% 0.0% 38.0% 31.0% 59.0% 31.0% Pick Dual Bottles 4.0% 0.0% 22.0% 0.0% 26.0% 7.0% 41.0% 10.0% Place Dual Shoes 0.0% 0.0% 7.0% 0.0% 8.0% 5.0% 4.0% 3.0% Rotate Qrcode 0.0% 0.0% 13.0% 0.0% 29.0% 12.0% 49.0% 5.0% Average success 7.1% 0.5% 34.5% 0.6% 40.3% 28.6% 48.9% 11.4%

[75] h3: IV-D Study on Action Space (Q3)

[76] p: To design a unified action space, we first investigate whether it should be discrete or continuous (F6-7), and then explore how navigation and manipulation can be integrated within the same framework (F8).

[77] p: Key Findings 6: Continuous action space in the diffusion head is not indispensable. With action chunking, discrete actions can achieve comparable performance. While many VLAs adopt a diffusion head to generate precise continuous actions, this design compromises the autoregressive nature of the model, thereby limiting its scalability when integrated with advanced techniques on VLMs and LLMs. In contrast, our approach combines action tokenization with action chunking, achieving competitive performance while preserving the autoregressive property.

[78] figure: TABLE VIII: Comparison among different action spaces of LLaVA-VLA on CALVIN. Decoder Success Rate (%) Avg. Len. Type 1/5 2/5 3/5 4/5 5/5 ABC → \rightarrow D Discrete 94.8 84.5 71.3 62.5 53.8 3.68 Continuous 93.5 84.4 73.5 63.3 54.3 3.70

[79] p: Key Findings 7: Fine-grained action tokenization does not lead to high performance. While a finer granularity in action representation might intuitively seem to improve the model’s ability to capture subtle differences, it introduces more training complexity to fit a larger action space. As shown in Table IX , using a larger number of action bins leads to lower success rates compared with coarser discretization, indicating that overly fine-grained action tokenization results in a loss of efficiency and generalization.

[80] figure: TABLE IX: Comparison of different numbers of bins on CALVIN. Bin Success Rate (%) Avg. Len. Numbers 1/5 2/5 3/5 4/5 5/5 ABC → \rightarrow D 256 94.8 84.5 71.3 62.5 53.8 3.68 1024 96.4 86.5 72.1 60.2 48.6 3.65

[81] p: Key Findings 8: The unified action space can be realized through a combination of direction token and value token. For mobile manipulation tasks, we aim for the VLA to simultaneously output both navigation data and manipulation data. An intuitive approach is to tokenize the navigation data in the same manner as the manipulation data. However, experiments revealed that this method is unstable and often causes the robot to abruptly resume movement during the manipulation phase after coming to a stop. We designed the navigation output as a direction token ( forward, turn left, turn right, stop ) followed by a value token representing the distance to advance or the angle to rotate. Specifically, to ensure stability during manipulation, when the direction token is stop , we append the value tokens for manipulation after it. This design allows the model to flexibly switch between navigation and manipulation. Furthermore, we introduce a special <Navigation> token following task instructions to prompt the model to perform mobile manipulation tasks.

[82] figure: TABLE X: Comparison of unified action space on the mobile manipulation tasks in the real world. Unified Move and Move and Action Space fetch bottles open the drawer Action Value Token 2/10 1/10 Direction + Vaule Token 4/10 4/10

[83] h2: V Evaluation of LLaVA-VLA

[84] p: We comprehensively evaluate our final architecture on CEBench to evaluate its manipulation performance, capabilities of visual generalization, cross-embodiment versatility, and abilities of mobile manipulation.

[85] h3: V-A Training Setup

[86] p: All post-training is conducted on 8 NVIDIA H100 GPUs unless otherwise noted, and fine-tuning is conducted on 1 NVIDIA 4090 GPU. For the CALVIN ABC → \rightarrow D task split, we post-train on multiple tasks for a single epoch without fine-tuning, which costs approximately six hours. For bimanual manipulation on RoboTwin and in the real world, we perform 2 epochs of post-training followed by 8 epochs of fine-tuning.

[87] figure: TABLE XI: Comparison of success rates on real-world bimanual tasks. Embodiments Basic Single-arm Tasks Dexterous Bimanual Tasks Task Stack Bowls Restore Bottle Click Bell Place Vagetable Pack Bottles Lift Pot Avg. Success Settings Seen DR Seen DR Seen DR Seen DR Seen DR Seen DR Seen DR ACT [ 37 ] 30% 10% 15% 0% 30% 10% 20% 0% 10% 0% 7% 0% 18.6% 3.0% TinyVLA [ 12 ] 25% 10% 10% 0% 25% 5% 15% 0% 20% 5% 10% 5% 17.5% 4.2% LLaVA-VLA (Ours) 58% 40% 38% 27% 66% 54% 50% 32% 28% 16% 25% 15% 44.2% 30.7%

[88] figure: Fig. 4: Visualization of real-world tasks. The top two rows illustrate the seen tasks, while the bottom two rows correspond to settings with domain randomization. Out of the eight real-world tasks, we select two representative examples of single-arm manipulation (left) as well as two examples of bimanual collaboration (right).

[89] h3: V-B Single-arm Manipulation on CALVIN

[90] p: Evaluation detail. We report the average completed trajectory length (Avg. Len.) across all five subtasks as well as success rates on each subtask. Following the official ABC → \rightarrow D settings [ 19 ] , the evaluation is conducted in an unseen scene. To ensure reliable evaluation, we test each method 1000 times.

[91] p: Evaluation results. Table VI shows that our LLaVA-VLA, with a lightweight 0.5B LLM and no large robot-dataset pre-training, tops all sub-tasks in success rate and attains the best average completed length of 3.68 against other Large VLA Models [ 15 , 30 ] . Compared with 3D-aware baselines [ 45 ] , our LLaVA-VLA outperforms them with a 0.33 increase in the average length of the completed trajectory, demonstrating its strong spatial reasoning ability. Despite no pre-training, our model outperforms methods [ 44 , 2 , 43 ] that rely on large-scale video pre-training and future image prediction. These results show that combining our techniques enables a light model to outperform architecturally complex, large-parameter, and training-expensive models.

[92] h3: V-C Bimanual Manipulation on RoboTwin

[93] p: Evaluation details. We evaluate our LLaVA-VLA 100 times in both the seen and DR settings and report success rates per task. For additional details, please refer to official settings [ 20 ] .

[94] p: Evaluation results. Table VII shows that as a small model without pre-training, our LLaVA-VLA achieves a success rate of 40.3% on seen tasks and 28.6% on domain-randomization tasks, outperforming diffusion-based [ 38 ] and VAE-based [ 37 ] baselines. Compared to larger VLAs that require extensive pretraining, our LLaVA-VLA achieves higher success rates in the DR environment, which indicates that our LLaVA-VLA owns visual generalization as well as spatial comprehension capabilities.

[95] h3: V-D Bimanual Manipulation in the Real World

[96] p: Evaluation details. For fixed-base bimanual manipulation, each method is evaluated over 100 episodes per task under both easy and hard settings, and for mobile manipulation, we report results over 10 episodes per task.

[97] p: Evaluation results on fixed-base tasks. Table XI shows that our LLaVA-VLA consistently outperforms the ACT [ 37 ] and TinyVLA [ 12 ] across 6 tasks, demonstrating its effectiveness in real-world experiments. Notably, when evaluated in unseen scenarios with background variations and distractor objects, both ACT and TinyVLA experience a dramatic drop in success rate, approaching zero. In contrast, Figure 4 shows that our LLaVA-VLA is much less affected, demonstrating strong robustness and visual generalization capabilities.

[98] p: Evaluation results on mobile manipulation tasks. Since existing VLA models lack mobile manipulation capabilities, we adopt the implementation of ACT in the mobile ALOHA [ 46 ] setting as the baseline. However, Figure 5 shows that ACT suffers from low navigation accuracy, which prevents it from reliably executing manipulation tasks, resulting in only a 10% success rate. Moreover, ACT is not equipped with multi-task learning capabilities. In contrast, our approach leverages the strengths of small VLMs to learn from diverse multi-task trajectories, thereby enabling effective instruction following and precise mobile manipulation.

[99] figure: Fig. 5: Evaluation in real-world mobile manipulation tasks.

[100] h2: VI Conclusion

[101] p: In this work, we introduced CEBench, a practical benchmark that spans diverse embodiments across both simulation and the real world and explicitly considers potential domain randomization. By conducting extensive experiments on CEBench, we systematically investigated the design space of lightweight VLAs and distilled several key insights into their architecture, training, and action representation. Building upon these insights, we developed LLaVA-VLA, a lightweight yet powerful VLA architecture that eliminates the need for costly pre-training while maintaining strong performance. The experimental results demonstrate its cross-embodiment versatility and visual generalization. Meanwhile, the real-world evaluations establish LLaVA-VLA as the first end-to-end VLA model capable of mobile manipulation. Our study builds a road map by providing valuable insights toward making VLA research more practical and accessible for embodied robotic systems.

[102] h2: References

[103] h2: Instructions for reporting errors

[104] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[105] p: Tip: You can select the relevant text first, to include it in your report.

[106] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[107] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
