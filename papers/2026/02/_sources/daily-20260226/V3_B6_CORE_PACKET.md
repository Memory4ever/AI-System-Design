## 2602.20555v1

原文精确HTML：https://arxiv.org/html/2602.20555v1；下方为该精确原源实际paragraph机械抽取，非作者摘要。

Here  f_{0}(\boldsymbol{x})=\mathbb{E}[Y|\boldsymbol{X}=\boldsymbol{x}]:[0,1]^{d\times n}\to\mathbb{R}  is the unknown target function,  \{(\boldsymbol{X}_{i},Y_{i})\}_{i=1}^{m}\subset[0,1]^{d\times n}\times\mathbb{R}  are observation pairs,  \{\xi\}_{i=1}^{m}  are i.i.d. Gaussian noises with  \mathbb{E}\xi_{i}=0,\mathrm{Var}(\xi_{i})=\sigma^{2} . Let  \mu  be the marginal distribution of  \boldsymbol{X} . We assume that  |Y|\leq B_{Y}  with some constant  B_{Y}>0 . Our goal is to estimate  f_{0}  based on the given observation pairs  \{(\boldsymbol{X}_{i},Y_{i})\}_{i=1}^{m} . Specifically, we consider the following least square problem over a function class  \mathcal{F} :

Then with probability at least  1-2\exp\left(-m^{dn/(2\gamma+dn)}\right) , there holds

There are several promising directions for future research. For example, it is crucial to establish a theoretical foundation for Transformers in broader applications, such as pre-training in large language models (LLMs) and vision Transformers (ViT) in computer vision tasks. Recent theoretical studies have investigated the approximation and generalization errors of Transformers in the setting of in-context learning (ICL) [26, 41, 5]. Their findings indicate that in ICL, only when both the number of tokens and the number of pre-training sequences are sufficiently large can the final error be made sufficiently small. However, these results often rely on architectural simplifications: [26, 5] utilize linear attention instead of softmax attention, while [41] employs softmax only in the final layer of the network. Deriving the convergence rates of a standard Transformer in ICL settings remains an open problem. Furthermore, while the present work focuses on the approximation error and generalization error of Transformers, the optimization error incurred during the training process, specifically the convergence rates of Transformers under various optimization algorithms, also warrants further investigation.

## 2602.20566v1

原文精确HTML：https://arxiv.org/html/2602.20566v1；下方为该精确原源实际paragraph机械抽取，非作者摘要。

Local Pruning: We use the intra-view importance scores to perform local pruning within each view. At this stage, we rank tokens within each view by their intra-view importance scores and remove a fixed proportion of the least important tokens. However, to ensure that our score map is spatially coherent and avoid abrupt changes in importance values, we apply spatial adaptive weighting (Eq. 3) to refine the raw importance scores before pruning. Specifically, each token’s final importance score is refined by incorporating information from spatially neighboring tokens, where closer tokens have a stronger influence on the final score:

We evaluate our algorithm in both RoboTwin and real-world environments. During comparison, all baseline methods and our approach are trained on the same dataset for the same number of steps. We use the officially released codes of  \pi_{0}  [9] and RDT-1B [14].
For  \pi_{0}  [9] and algorithms built on  \pi_{0}  [9], we perform full-parameter fine-tuning for 5000 steps with a global batch size of 256 for each task. For RDT [14] and algorithms built on RDT, we fine-tune for 1200 steps with a global batch size of 128. The loss hyperparameters  \lambda_{1}  and  \lambda_{2}  are both set to 0.1, the prune ratio  [\alpha_{1},\alpha_{2},\alpha_{3},\beta]  set to be  0.3,0.2,0.2,0.5  and the weighting parameter  \epsilon  is set to 0.01.
Since dropping tokens within the LLM backbone in  \pi_{0}  [9] would break the KV cache which will slow the speed, we perform token pruning before tokens enter the LLM backbone. For RDT [14], following DART [20], we perform token pruning at the second layer of the DiT block. Other methods maintain complete consistency with their original papers.
We collected 50 episodes for the ’Bottle Pick’ task and 100 episodes for the seven other simulator tasks. For the four out-of-domain (OOD) task in RoboTwin2 [32], we collect 50 episodes each. Additionally, we designed 5 real-world experiments, each with 200 episodes, encompassing single-arm and dual-arm tasks as shown in Figure 6, with several tasks featuring extensive distractions that distinguish them from simulator environments. For evaluation, we test each simulator task 100 times and each real-world task 20 times. All training was conducted on eight NVIDIA A100 GPUs, and inference was performed on a single NVIDIA RTX 3090 GPU.

In Table IV, “w/o Hierarchical” means we obtain the final token scores by directly multiplying inter-view importance with intra-view importance, and conduct pruning accordingly. Without hierarchical token pruning, our success rate drops significantly. This is because direct end-to-end ranking tends to select the main view while discarding wrist camera information, similar to using only the main view.
“w/o Adaptive Weight” refers to distance weighting not being used. The results show that using distance weighting, which prevents pruning the tokens between objects and grippers, improves our method’s performance in all four tasks.
Therefore, our hierarchical token pruning and adaptive weight are both effective.

Then we conduct experiments without the inter-view importance predictor (Inter-IP) and intra-view importance predictor (Intra-IP), shown as “w/o Inter-IP” and “w/o Intra-IP” in Table IV, using only hierarchical pruning without cross-view importance and only using the inter-view importance score to prune. As shown in Table IV, both components enable our model to more accurately identify which tokens to prune.
To further validate our method, we compare BFA++ with adaptive pooling [35], random token pruning, and online pooling, which computes intra-view and inter-view importance scores via online annotation. For fair comparison, all methods are applied during both post-training and inference. Our method significantly outperforms all baselines. We observe that online pruning shows notably lower speed and success rate than the baseline, because online annotation is excessively time-consuming during inference and substantially increases post-training time due to repeated annotations. In contrast, our method effectively backpropagates gradients from both inter-view and intra-view perspectives. Finally, we ablate the fixed prune ratio by comparing with adaptive token prune ratios.
During two-step pruning, it prunes the number of tokens with scores below 0.5 multiplied by 0.8, which is the best parameter we found through exploration, with other settings identical to BFA++. This approach shows inconsistent speed due to variable prune ratio, making it unsuitable for VLA tasks, and achieves lower success rates than BFA++.

## 2602.20574v1

原文精确HTML：https://arxiv.org/html/2602.20574v1；下方为该精确原源实际paragraph机械抽取，非作者摘要。

We use Qwen3-4B-Base as the underlying model for all experiments.
We construct a fixed-challenger dataset by prompting Qwen2.5-32B-Instruct to generate questions from documents in the Nemotron-CC-Math corpus (Mahabadi et al., 2025), following a procedure similar to SPICE (Liu et al., 2025).
For each candidate question, we generate  k{=}8  tutor rollouts with document context and require at least  5/8  tutor answers to agree; questions that fail this strict consensus filter are dropped.
Validity additionally requires producing a parsable final answer (the last \boxed{...} expression) and satisfying document-leakage guardrails (Appendix A.4).
The resulting dataset contains 551 training questions and 50 held-out evaluation questions (Table 1).
All experiments use this fixed challenger; adaptive curricula are discussed in §5.

GATES relies on agreement among multiple tutor rollouts as a proxy for correctness.
If the tutor is insufficiently capable, biased, or produces low-diversity reasoning traces, consensus may reflect shared errors rather than reliable supervision.
Relatedly, to avoid reinforcing incorrect supervision, we discard all questions without sufficient tutor agreement, which improves reliability but reduces the effective number of training updates and may limit sample efficiency.

A natural extension of GATES is to generate questions on the fly using an adaptive challenger, potentially improving coverage and curriculum quality.
Unlike the fixed challenger, which uses Qwen2.5-32B-Instruct to pre-generate questions offline, adaptive training generates questions from the model itself, making it a strictly harder setting with no external question source.
Preliminary experiments (Figure 6) suggest that adaptive training can improve out-of-distribution benchmark performance, with the best adaptive variant reaching 38.3% average accuracy compared to 35.4% under the fixed challenger.
Notably, the configuration that performs best under adaptive training differs from the canonical GATES setup: adding the oracle loss ( \mathcal{L}_{\text{cons}} ) appears to help when questions are generated adaptively, possibly because harder or less familiar questions increase the prevalence of confident but incorrect tutor agreement (the primary failure mode of consensus gating), and the oracle loss provides a direct corrective signal for exactly these cases.
Without this grounding, the adaptive GATES configuration reaches 29.8% (below the fixed challenger (35.4%) but still well above the pretrained baseline (20.2%)), suggesting that the optimal loss composition may depend on the properties of the data generation process.
All adaptive variants outperform the SPICE baseline (21.6%) under a matched update budget, indicating that consensus-gated distillation remains effective even under non-stationary training distributions.
We view adaptive challenger optimization as a promising direction for fully self-contained self-distillation, though further work is needed to develop evaluation protocols and reliability mechanisms suited to non-stationary settings.

Figure 9 reports accuracy under greedy decoding.
Under this single-sample metric, GATES and Tutor-Trajectory SFT achieve near-identical average accuracy (40.0% vs. 40.3%), with Tutor-Trajectory SFT slightly ahead on AMC and Minerva.
The gap between these methods is substantially larger under maj@8 decoding (Figure 4a), suggesting that consensus gating improves the consistency of correct answers across samples rather than peak single-sample performance.

## 2602.20577v1

原文精确HTML：https://arxiv.org/html/2602.20577v1；下方为该精确原源实际paragraph机械抽取，非作者摘要。

This discretization transforms the trajectory generation problem into a sequence of  N -way classification problems, constraining the output space to physically feasible spatial primitives.

Instead, we enforce a modality-constrained unmasking policy that prioritizes the resolution of the trajectory.
Let  \mathbf{x}_{t}  denote the sequence at diffusion step  t , containing both action-token positions and reasoning-token positions. In each iteration, the transformer predictor outputs the probability distribution  p_{\theta}(\mathbf{x}_{0}\mid\mathbf{x}_{t})  for all masked tokens.
Although the model predicts the entire sequence simultaneously, we restrict the unmasking candidate set exclusively to the action indices until planning is fully determined.
Specifically, we compute the confidence score  u_{j}=\max_{k}p_{\theta}(x_{j}=k\mid\mathbf{x}_{t})  for all masked action-token positions  j . We then select the subset of action tokens with the highest confidence scores to demask, i.e., replace  [\texttt{M}]  with the predicted token ID, while keeping all reasoning tokens in the masked state.

We investigate this trade-off by training MVLAD-AD with vocabulary sizes  N\in\{128,256,384\} , as reported in Table IV. We observe that  N=256  strikes the optimal balance, achieving the lowest planning error of  1.28\text{\ }\mathrm{m} . Crucially, increasing  N  to 384 leads to a performance degradation to  2.76\text{\ }\mathrm{m}  with an obvious increase in final training loss from 0.36 to 0.53. This indicates that despite higher theoretical precision, the model struggles to converge due to the optimization difficulty in distinguishing between dense action tokens. Conversely, reducing  N  to 128 yields the lowest training loss of 0.32, suggesting an easier classification task, but the planning error rises to  1.73\text{\ }\mathrm{m} . This confirms that further reducing the codebook size creates a quantization bottleneck that limits physical precision, regardless of stable training convergence.

Effectiveness of Geometry-Aware Embedding Learning.
We investigate the impact of geometry-aware embedding learning on the planning metrics of the model.
As a comparison, we remove this module and train the model with random embeddings. This causes a substantial performance degradation, increasing the average L2 error from  1.28\text{\ }\mathrm{m}  to  2.39\text{\ }\mathrm{m} .
This comparison confirms that treating action tokens as independent categorical indices discards useful metric information, making it difficult for the model to learn effective planning.
By enforcing geometric consistency, our method ensures that the distance between tokens in the latent space correlates with their physical displacement, enabling the model to generate accurate trajectories.
