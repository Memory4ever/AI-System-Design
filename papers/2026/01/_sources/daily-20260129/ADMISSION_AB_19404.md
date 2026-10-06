# 独立准入校准：2601.19404v1

原完整题摘记录：AB3.md。仅用于定点准入，不代表日期或必要证据审阅完成。

[2601.19404v1] RPO:Reinforcement Fine-Tuning with Partial Reasoning Optimization
 Abstract: Within the domain of large language models, reinforcement fine-tuning algorithms necessitate the generation of a complete reasoning trajectory beginning from the input query, which incurs significant computational overhead during the rollout phase of training. To address this issue, we analyze the impact of different segments of the reasoning path on the correctness of the final result and, based on these insights, propose Reinforcement Fine-Tuning with Partial Reasoning Optimization (RPO), a plug-and-play reinforcement fine-tuning algorithm. Unlike traditional reinforcement fine-tuning algorithms that generate full reasoning paths, RPO trains the model by generating suffixes of the reasoning path using experience cache. During the rollout phase of training, RPO reduces token generation in this phase by approximately 95%, greatly lowering the theoretical time overhead. Compared with full-path reinforcement fine-tuning algorithms, RPO reduces the training time of the 1.5B model by 90% and the 7B model by 72%. At the same time, it can be integrated with typical algorithms such as GRPO and DAPO, enabling them to achieve training acceleration while maintaining performance comparable to the original algorithms. Our code is open-sourced at this https URL . 
 Submission history From: Zhenyu Guan [ view email ] [v1] Tue, 27 Jan 2026 09:38:32 UTC (2,226 KB) [v2] Fri, 30 Jan 2026 08:18:54 UTC (2,226 KB) 


