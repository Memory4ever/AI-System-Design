# 第十一批已发现的具体贡献题摘

只本日已有相关题摘；不把宽库存变全文队列。六项题摘显露具体选择条件，准入尚待独立校准。

## 2602.15539v1 — Dynamic Training-Free Fusion of Subject and Style LoRAs

[精确v1](https://arxiv.org/html/2602.15539v1)

Recent studies have explored the combination of multiple LoRAs to simultaneously generate user-specified subjects and styles. However, most existing approaches fuse LoRA weights using static statistical heuristics that deviate from LoRA’s original purpose of learning adaptive feature adjustments and ignore the randomness of sampled inputs. To address this, we propose a dynamic training-free fusion framework that operates throughout the generation process. During the forward pass, at each LoRA-applied layer, we dynamically compute the KL divergence between the base model’s original features and those produced by subject and style LoRAs, respectively, and adaptively select the most appropriate weights for fusion. In the reverse denoising stage, we further refine the generation trajectory by dynamically applying gradient-based corrections derived from objective metrics such as CLIP and DINO scores, providing continuous semantic and stylistic guidance. By integrating these two complementary mechanisms—feature-level selection and metric-guided latent adjustment—across the entire diffusion timeline, our method dynamically achieves coherent subject-style synthesis without any retraining. Extensive experiments across diverse subject–style combinations demonstrate that our approach consistently outperforms state-of-the-art LoRA fusion methods both qualitatively and quantitatively.

贡献判断：固定LoRA fusion忽略每layer/输入差异→base-vs-subject/style特征KL动态权重加生成轨迹metric修正→重新考虑固定融合与采样时额外优化的成本/质量条件，拟5；不是新名字准入。

## 2602.15543v1 — Selective Perception for Robot: Task-Aware Attention in Multimodal VLA

[精确v1](https://arxiv.org/html/2602.15543v1)

In robotics, Vision-Language-Action (VLA) models that integrate diverse multimodal signals from multi-view inputs have emerged as an effective approach. However, most prior work adopts static fusion that processes all visual inputs uniformly, which incurs unnecessary computational overhead and allows task-irrelevant background information to act as noise. Inspired by the principles of human active perception, we propose a dynamic information fusion framework designed to maximize the efficiency and robustness of VLA models. Our approach introduces a lightweight adaptive routing architecture that analyzes the current text prompt and observations from a wrist-mounted camera in real-time to predict the task-relevance of multiple camera views. By conditionally attenuating computations for views with low informational utility and selectively providing only essential visual features to the policy network, Our framework achieves computation efficiency proportional to task relevance. Furthermore, to efficiently secure large-scale annotation data for router training, we established an automated labeling pipeline utilizing Vision-Language Models (VLMs) to minimize data collection and annotation costs. Experimental results in real-world robotic manipulation scenarios demonstrate that the proposed approach achieves significant improvements in both inference efficiency and control performance compared to existing VLA models, validating the effectiveness and practicality of dynamic information fusion in resource-constrained, real-time robot control environments.

贡献判断：uniform多camera fusion使无关视觉占预算→用prompt+wrist观测预测view任务相关并有条件跳过计算、VLM自动标注router→重新考虑何种视角可省和teacher标签误差，拟5；只task-aware runtime条件。

## 2602.15556v1 — Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs

[精确v1](https://arxiv.org/html/2602.15556v1)

LVLMs have achieved strong multimodal reasoning capabilities but remain prone to hallucinations, producing outputs inconsistent with visual inputs or user instructions. Existing training-free methods, including contrastive decoding and auxiliary expert models, which incur several times more computational overhead and may introduce potential interference, as well as static internal signal enhancement, are often vulnerable to the attention sink phenomenon. We find that internal Positive Attention Dynamics (PAD) in LVLMs naturally reveal semantically core visual regions under the distortions of attention sinks. Based on this, we propose Positive Attention Dynamics Enhancement (PADE), a training-free attention intervention that constructs a PAD map to identify semantically core visual regions, applies per-head Median Absolute Deviation Scaling to adaptively control the intervention strength, and leverages System-Token Compensation to maintain attention to complex user instructions and support long-term output consistency. Experiments on multiple LVLMs and benchmarks show that PADE improves visual grounding and reduces hallucinations, validating the effectiveness of leveraging internal attention dynamics for reliable multimodal reasoning.

贡献判断：静态视觉attention增强受sink失效→跨内部positive attention dynamics定位+perhead MAD强度/systemtoken补偿→重新考虑视觉增强与指令保留的竞争条件，拟5；不凭幻觉数字或术语保留。

## 2602.15563v1 — 1-Bit Wonder: Improving QAT Performance in the Low-Bit Regime through K-Means Quantization

[精确v1](https://arxiv.org/html/2602.15563v1)

Quantization-aware training (QAT) is an effective method to drastically reduce the memory footprint of LLMs while keeping performance degradation at an acceptable level. However, the optimal choice of quantization format and bit-width presents a challenge in practice. The full design space of quantization is not fully explored in the context of QAT, and the precise trade-off between quantization and downstream performance is poorly understood, as comparisons often rely solely on perplexity-based evaluations. In this work, we address these shortcomings with an empirical study of QAT in the low-bit regime. We show that k-means based weight quantization outperforms integer formats and can be implemented efficiently on standard hardware. Furthermore, we find that, under a fixed inference memory budget, the best performance on generative downstream tasks is achieved with 1-bit quantized weights.

贡献判断：低bit格式通常只PPL比较→kmeans QAT与integer在固定memory下generative task取舍→重新考虑bitwidth×模型容量与真正任务质量，拟5；必要核同预算/formatkernel。

## 2602.15564v1 — Beyond Static Pipelines: Learning Dynamic Workflows for Text-to-SQL

[精确v1](https://arxiv.org/html/2602.15564v1)

Text-to-SQL has recently achieved impressive progress, yet remains difficult to apply effectively in real-world scenarios. This gap stems from the reliance on single static workflows, fundamentally limiting scalability to out-of-distribution and long-tail scenarios. Instead of requiring users to select suitable methods through extensive experimentation, we attempt to enable systems to adaptively construct workflows at inference time. Through theoretical and empirical analysis, we demonstrate that optimal dynamic policies consistently outperform the best static workflow, with performance gains fundamentally driven by heterogeneity across candidate workflows. Motivated by this, we propose SquRL, a reinforcement learning framework that enhances LLMs’ reasoning capability in adaptive workflow construction. We design a rule-based reward function and introduce two effective training mechanisms: dynamic actor masking to encourage broader exploration, and pseudo rewards to improve training efficiency. Experiments on widely-used Text-to-SQL benchmarks demonstrate that dynamic workflow construction consistently outperforms the best static workflow methods, with especially pronounced gains on complex and out-of-distribution queries. The codes are available at https://github.com/Satissss/SquRL .

贡献判断：静态SQL工作流不同query有异质收益→workflow policy训练中dynamic actormask/pseudoreward→重新考虑heterogeneity条件下可学路由与训练探索，而非泛agent组合，拟5；理论optimal上界与实际训练分开。

## 2602.15567v1 — Constraining Streaming Flow Models for Adapting Learned Robot Trajectory Distributions

[精确v1](https://arxiv.org/html/2602.15567v1)

Robot motion distributions often exhibit multi-modality and require flexible generative models for accurate representation. Streaming Flow Policies (SFPs) have recently emerged as a powerful paradigm for generating robot trajectories by integrating learned velocity fields directly in action space, enabling smooth and reactive control. However, existing formulations lack mechanisms for adapting trajectories post-training to enforce safety and task-specific constraints. We propose Constraint-Aware Streaming Flow (CASF), a framework that augments streaming flow policies with constraint-dependent metrics that reshape the learned velocity field during execution. CASF models each constraint, defined in either the robot’s workspace or configuration space, as a differentiable distance function that is converted into a local metric and pulled back into the robot’s control space. Far from restricted regions, the resulting metric reduces to the identity; near constraint boundaries, it smoothly attenuates or redirects motion, effectively deforming the underlying flow to maintain safety. This allows trajectories to be adapted in real time, ensuring that robot actions respect joint limits, avoid collisions, and remain within feasible workspaces, while preserving the multi-modal and reactive properties of streaming flow policies. We demonstrate CASF in simulated and real-world manipulation tasks, showing that it produces constraint-satisfying trajectories that remain smooth, feasible, and dynamically consistent, outperforming standard post-hoc projection baselines.

贡献判断：learned streamingflow posttrain不能适应环境约束→workspace/joint distance→localmetric pullback变形velocity→重新考虑持续流与posthoc projection的可行性/多峰取舍，拟6；理论安全条件必要核，不因机器人应用自动保留。

