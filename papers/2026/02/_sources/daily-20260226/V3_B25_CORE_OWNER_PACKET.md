# B25 — 五项必要原证 / actual owner；本次独立复核已落实

2026-10-06 feb26_close_oct06 非原packet作者从各raw重新定位全部pID，20670原3.2 gate与forcedprefix/credit、20680原CORE710–820 Table1及§4metric直接读，未借吞<的PARA假冲突。actualCh80同源feedback/stopbudget、Ch24真实history→generatedhistory及current97–99codec/anchor费用、Ch26proposal/controller权限独立核。20670/20672受限RM/格式控制仅报告；20685/20687具体已有覆盖；20680真实bit/payload/ECC中心混淆隔离恢复保证，保reported有限威胁signal，不自补null/random指标/50%baseline、不泛否水印。原人口/费用/反侧/ND保留，未新写Books或运行artifact/复现，非日级验收。

## 2602.20670v1
https://arxiv.org/html/2602.20670v1

S3.SS3.p3.1 | Crucially, we apply the RL credit only to the generation of the final verdict v_{1} and any intermediate reflection J , while treating the initial verdict v_{0} as part of the context that is not directly optimized. This design allows the model to learn whether to confirm or revise its initial judgment through reflection. If the initial verdict is likely correct, the optimal strategy is to repeat it as the final verdict; if incorrect, the model can improve its reward by changing the final verdict after reflection. Through training, this reflective behavior emerges naturally from the reward structure rather than being hard-coded.

S3.SS3.p4.1 | Counterfactual Prefix Augmentation. To strengthen the model’s ability to revise incorrect initial judgments, we augment the training data with counterfactual initial verdicts. For each instance (x,z)\in\mathcal{D} , we construct two training examples with the same input x but different forced initial verdicts: one with v_{0}=\texttt{A} and one with v_{0}=\texttt{B} . The reward is computed only from the final verdict via Equation 8. This augmentation exposes the model to diverse starting points and prevents the reflective stage from degenerating into simply echoing the initial verdict, improving the robustness of self-correction.

S4.SS2.SSS0.Px1.p1.1 | CAMEL consistently achieves state-of-the-art results across all three benchmarks, outperforming strong baselines including much larger models such as LLaMA-3.1-Nemotron-70B and INF-ORM-LLaMA3.1-70B. Notably, CAMEL attains an average accuracy of 82.9%, surpassing the second-best baseline by 3.2%, despite using only 14B parameters. In particular, CAMEL-Fast, which bypasses the reflection stage, achieves 90.5% on RewardBench, 74.8% on RM-Bench, and 65.2% on JudgeBench. CAMEL-Reflection, which always invokes reflection, achieves higher scores of 92.8%, 84.2%, and 71.6% on the respective benchmarks. The full CAMEL model—equipped with confidence-gated reflection—achieves 92.4%, 81.9%, and 69.1%, respectively, striking a favorable trade-off between performance and generation cost.

## 2602.20672v1
https://arxiv.org/html/2602.20672v1

S3.SS1.p1.1 | In BBQ, we extend the common practice of synthetic captioning for text-to-image training. Starting from long structured captions [1], we augment each caption with numeric bounding boxes and RGB colors. Although extracting such parameters is well studied in vision and graphics, we find that general-purpose LLM/VLM systems (e.g., Gemini 2.5 [49]) are not sufficiently reliable for high-precision outputs. Therefore, for each image we first generate a FIBO-style structured caption, following [1]. For every object mentioned in the caption, we extract its bounding box from grounded SAM2 [50], estimate relative depth using Depth Anything V2 [51], and obtain dominant object colors using Pylette [52]. We replace semantic location and qualitative color terms with explicit bounding box coordinates and RGB triplets. Finally, a global RGB palette from Pylette is added to capture the overall color scheme. This automated extraction provides the precise parametric grounding required to align numeric tokens with visual synthesis.

S3.SS3.p1.1 | The trained model enables new forms of user interaction, including object dragging, resizing, and recoloring. However, building a complete end-to-end system introduces two key challenges. First, when a user edits a bounding box, the system must preserve global coherence and avoid breaking the composition. For example, if two people are hugging and the user separates their boxes, the underlying action must necessarily change. Second, for generation from scratch, a short natural-language prompt must be expanded into a full structured caption with a plausible composition, now including explicit bounding boxes and colors. While BBQ provides unprecedented precision through its parametric schema, manually authoring JSON prompts with exact RGB triplets and normalized bounding box coordinates is impractical for human users.

S4.SS1.SSS0.Px3.p1.1 | To evaluating color fidelity we wish to isolate the specific object and remove noise from other parts of the image. Therefore, we generated 200 images depicting single objects on white background, where each object was assigned a specific target RGB color in the prompt. For evaluation, we extract object pixels by masking out the white background using foreground segmentation, and then apply K-means clustering (with K=5 and K=8 ) in CIELab color space on the extracted object pixels to identify the dominant color palette. Clusters representing less than 5% of object pixels are filtered out. Among the remaining clusters, we select the one with the minimum distance to the target color. We report two distance metrics: \Delta E_{00} (CIEDE2000), which measures perceptual color difference, and Euclidean distance in the a-b chromaticity plane, which isolates hue and saturation differences independently of light. For both metrics, we report mean, median, and 90th percentile (p90) statistics, where p90 captures tail behavior and robustness to difficult cases that may not be reflected by central tendency alone. Like in TaBR, BBQ and FIBO utilize their native structured schemas for compatibility, where for FIBO we ask the VLM to choose the name of the color that best describes the RGB. For Flux.2 Pro we follow the prompting guide [61] and for Nano Banana Pro we’ve found that the best results are achieved with the same prompts as Flux.

S4.SS3.SSS0.Px2.p1.1 | Table 2 evaluates spatial grounding under box-conditioned prompts on COCO and LVIS. Across both datasets, BBQ consistently outperforms strong text-to-image baselines such as Nano Banana Pro and Flux.2 Pro, as well as the dedicated grounding model GLIGEN, while trailing the current state-of-the-art InstanceDiffusion. These results position BBQ as a strong non-specialized alternative for box-conditioned generation. Unlike InstanceDiffusion and GLIGEN, which rely on grounding-specific architectural modifications or inference-time alignment mechanisms, BBQ is trained at a substantially larger scale for general high-fidelity image synthesis, achieving strong bounding-box alignment without sacrificing expressiveness, inference time or requiring specialized components. Furthermore, unlike InstanceDiffusion, BBQ exhibits native disentanglement that enables intuitive parametric refinement, as illustrated in Fig. 7 and Fig. 3

## 2602.20680v1
https://arxiv.org/html/2602.20680v1

S3.I1.i2.p1.1 | Guided Diffusion Watermark Removal: In this mode, the attacker is aware of the presence of a watermark and possibly knows the decoding algorithm g_{\text{dec}} (though not necessarily the secret key or exact parameters if any). The attacker then incorporates g_{\text{dec}} ’s feedback into the diffusion process to specifically disrupt m . We implement this by augmenting the diffusion model’s loss with a term that penalizes the presence of the watermark. Concretely, assume the diffusion model generates images via iterative denoising x_{T}\rightarrow\dots\rightarrow x_{0} , where x_{0} is the output image I^{\prime} . We introduce an additional loss \mathcal{L}_{wm} applied at the final step on x_{0} : \mathcal{L}_{wm}=\|g_{\text{dec}}(x_{0})-\tilde{m}\|^{2} , where \tilde{m} is a target “null” message (e.g., a vector of 0s or any innocuous bit pattern). This encourages the output image to decode to \tilde{m} instead of the original m . We integrate this with the diffusion model’s usual reconstruction or guidance loss via a weight \lambda . During generation, we compute x_{0} at each iteration (after a full denoising) and backpropagate \nabla_{x_{0}}\mathcal{L}_{wm} through the denoising process (similar in spirit to diffusion adversarial dreaming or iterative prompt refinement). Algorithm 1 provides pseudocode for this procedure.

S4.SS0.SSS0.Px4.p1.1 | We evaluate (i) Watermark Decoding Accuracy: For StegaStamp, this is the bit accuracy out of 56 bits (we report average percent of bits correct per image). For TrustMark and VINE, which output a message vector that goes through error-correction, we report the success rate of decoding the correct payload (in %). Additionally, we report Bit Error Rate (BER) where applicable. (ii) Image Quality: To verify that diffusion-edited images remain high quality (and essentially the “same” to a human), we use PSNR and SSIM between I_{\text{wm}} and I^{\prime} (after aligning for any shift). We also use LPIPS (learned perceptual distance) which correlates with human perceptual difference. Lower LPIPS and high SSIM indicate the content is preserved. For text-guided edits, we also ensure the generated image correctly reflects the prompt (though our prompts are just descriptive of the original, so this is trivial). (iii) Detection of Watermark Presence: Some watermark schemes allow a separate detection (e.g., a detector that says “watermark present or not”). If such is available (TrustMark has a trained decoder which can output random bits for no watermark, but no separate flag), we measure whether the attacked images are falsely identified as unwatermarked.

决定性Table1与原metric文字，直接CORE；不使用吞掉未转义<的PARA结果：
Table 1:
Watermark decoding accuracy (higher is better) for different watermarking methods under various attacks. The diffusion-based attacks (regeneration and guided removal) cause a dramatic drop in decoding accuracy, compared to conventional distortions.
Watermark Method
No Attack
JPEG-50
Crop
Noise
Regeneration
Guided Removal
(Baseline)
(Quality 50)
(10% removed)
(
σ
=
10
\sigma=10
)
(Diffusion)
(Diffusion+Guide)
StegaStamp
(
Tancik et al., 2020
)
99.8%
92.5%
88.1%
90.3%
7.4%
0.0%
TrustMark
(
Bui et al., 2023
)
99.9%
94.7%
91.2%
95.5%
12.8%
0.0%
VINE
(
Lu et al., 2024b
)
(VINE-R)
100.0%
96.4%
93.0%
97.8%
24.5%
1.6%
As expected, without any attack, all methods decode perfectly or near-perfectly (
≈
100
%
\approx 100\%
). Under moderate JPEG compression (quality=50) or addition of noise, decoding drops somewhat (e.g., StegaStamp to 92.5%), but remains high, confirming the claimed robustness of these schemes. Cropping 10% off the image edges is more challenging, since part of the watermark signal is lost; still, decoding accuracies around 88–93% are observed, which is remarkable (these methods likely use redundancy across the image). In stark contrast, the
diffusion regeneration attack
reduces the decoding accuracy to
<
25
%
<25\%
in all cases. StegaStamp and TrustMark are almost completely broken (only 7.4% and 12.8% on average of the payload bits are correct, essentially at chance-level for 56-bit payloads). VINE appears slightly more robust with 24.5% accuracy, but this is still extremely low, corresponding to decoding error rates of
>
75
%
>75\%
. We note that VINE’s training included exposure to generative distortions (via surrogate blur attacks)
(
Lu et al., 2024b
)
, which might explain why it retains a small fraction of the watermark under unguided diffusion; however, the majority of the payload is lost. Finally, the
guided removal attack
drives decoding accuracy effectively to
0
%
0\%
for StegaStamp and TrustMark (no image had any correct payload bit after error correction in our tests), and to
1.6
%
1.6\%
for VINE (in a few cases VINE’s error correction still latched onto a couple bits). These results clearly illustrate that diffusion-based editing can neutralize robust watermarks far beyond traditional distortions. Even the best-performing scheme (VINE) fails to retain meaningful information when facing a diffusion model intentionally or unintentionally “washing out” the embedded signal.
Visual Quality and Fidelity.
Crucially, the diffusion-attacked images remain nearly indistinguishable from the originals to humans. For the regeneration attack, the average PSNR between
I

## 2602.20685v1
https://arxiv.org/html/2602.20685v1

S3.SS5.p2.1 | To bridge this gap, we propose a novel training paradigm to align the training and inference distributions (Alg. 1). It recurrently conducts forward and backward propagation frame by frame, and the gradients are accumulated until the end of each long sequence for model optimization. Obviously, the later frames are conditioned on the earlier frames. We cache the latent features in the global self-attention module since it is the only module operating across frames (Sec. 3.4). While previous works often cache the keys and values separately [11, 51] during inference, we directly store the latent features before KV projection layer instead. In this case, we can 1) save half of the GPU memory and 2) ensure the KV projection layer in the computational graph, which is critical for temporal information extraction.

S4.SS2.p3.1 | Motion Cues in Synthetic Videos. In addition to visual quality and condition fidelity, we further evaluate whether our synthetic videos support plausible driving decisions by applying an end-to-end planner (VAD [24]) pretrained on real scenes to our generated videos. Tab. 4 shows that the pretrained planner derives actions from synthetic videos consistent with real scenes. This reflects not only visual realism but also physical and motion plausibility in our generated videos.

S4.SS4.p1.1 | Scale Causality. RayNova is built up on scale and time dual-causality. The temporal causality is inevitable if we would like to extend to long video autoregression. For scale causality (Eq. 4), different from low-scale condition in previous frames, we consider two alternatives conditions: 1) all scales or 2) same scale features in previous frames. Results are shown in Tab. 7 and Fig. 4. Higher scales features of previous time steps cause future frames simply copying the details without simulating the dynamics, and same scale condition is far from enough for stable spatio-temporal modeling.

## 2602.20687v1
https://arxiv.org/html/2602.20687v1

S3.SS3.p3.1 | Spatial Alignment. Similar to the search task, the agent must align the center of its view with the specified object. However, to decouple from other foundational skills such as planning and navigation, we initialize the agent close to the target so the object is already within its egocentric view. We also remove all movement actions from the action space, leaving only view-adjustment actions. As a result, the agent need not devise a search strategy or physically approach the target; it merely adjusts its gaze, enabling a focused evaluation of the model’s fine-grained spatial alignment capability.

S3.SS3.p5.1 | Planning. The goal of this task is to evaluate an agent’s task-planning ability. In essence, this ability corresponds to the brain’s cognitive reasoning functions rather than the cerebellum’s motor-control functions. To effectively decouple motor control from planning, we abstract the four basic motion primitives into directly callable navigation interfaces. We adopt an interactive-task framework because the explicit, multi-stage nature of its execution process is especially well-suited for fine-grained evaluation of planning capability.

S3.SS4.p3.1 | To further enhance sample quality, we implemented a human-machine collaborative approach. We deployed an advanced MLLM to conduct 5 rounds of rollout evaluations on the samples, tracking the success rate for each sample. We then identified samples that either achieved complete success or complete failure across all rounds. Human experts subsequently intervened to assess the task feasibility of all-fail samples and the difficulty level of all-pass samples. We filtered out infeasible erroneous samples from the all-fail samples and excluded samples with insufficient difficulty from the all-pass samples, ultimately obtaining all samples for NativeEmbodied. More details of the data collection pipeline are provided in Appendix.

S4.SS4.p1.2 | We selected Claude-3.5-Sonnet as our experimental subject, as this model demonstrates moderate performance in benchmark tests, offering good representativeness that facilitates more generalizable conclusions. As shown in Figure 3, the experimental results reveal three important insights:

S4.SS5.p3.1 | Thinking may interfere with basic action execution. After engaging in thinking mode, success rates for tasks that require precise action actually decreased significantly, such as alignment and navigation. This decline might be attributed to excessive reasoning processes, which can introduce unnecessary complexity and interfere with the intuitive execution of basic actions.

## actual owner — books/part-07-agent/80-reflection.md

L45–56:
## Feedback 来源决定价值

Feedback 可以来自：

| 来源 | 示例 | 独立性 |
| --- | --- | --- |
| Deterministic verifier | compiler、tests、schema、constraint solver | 高 |
| Environment | API result、game state、user correction | 中高 |
| Separate evaluator | judge model、specialized classifier | 取决于模型/数据 |
| Same model self-critique | “检查自己的答案” | 低 |

同一模型可能在 generation 与 critique 中重复同一盲点。External tests 和 environment outcomes 通常比自由文本“再想想”更可操作。

L199–214:
## Stopping Policy

无限循环会消耗 token、tool calls 和 wall time，并可能来回振荡。停止条件可包含：

```text
verifier passes
max_iterations
no material delta
same failure repeats
budget/deadline reached
risk threshold exceeded
human decision required
```

Runtime 必须持久化 attempt、feedback 和 decision。只把全部历史重新塞入 Context 会越来越长，还可能强化错误。


## actual owner — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

L48–58:
第 23 章给出了表示的重构和语义契约，本章还必须问一个不同的问题：**这种表示是否容易被当前生成路径逐步预测？**
视觉 encoder 的高维连续 latent 即使能重构图像，单个 latent token 的分布仍可能比低维 VAE latent 难建模。
在 teacher forcing 下，AR 看到真实历史；生成时却要以自己的连续预测作下一步条件，高维误差会随步骤进入后续条件。
因此，重构分数不能替代生成质量、误差滚动或推理成本的验收。

一种受限分支先校准 token 分布，再在训练时扰动真实历史，让预测器练习接住偏离数据流形的前缀；它以更复杂的
表示归一化和训练噪声换生成容错，却不能靠更低训练损失证明最终图像更好。若扰动不匹配真实 rollout、
生成质量仍落后或稳定性优先，沿用重构导向 VAE 仍是合理选择。[RAE-AR 的图像实验](https://arxiv.org/html/2604.01545v1)
只支持所测 encoder、AR 架构、训练设置与指标下的这条表示—生成张力；其消融中归一化单独使用并非总有益，
结果也不证明高维语义 latent 已普遍追平 VAE。<!-- source-family:SF-2026-ARXIV-2604-01545 -->


L97–99:
历史压缩还有一条不同于 recurrent state 的视频分支：保留固定长度的当前 noisy window，把历史 clean frames 按远、中、近期采用不同的时间与空间 patch 粒度，再用首帧 anchor 约束外观。它让近期细节与远期轮廓承担不同责任，而不是把所有历史保成同精度 token；局部位置重索引限制了接口长度，却不恢复已经压缩掉的旧细节。

推理继续消费自己生成的历史，因此训练可对历史逐帧加入扰动，模拟累积误差而非只见干净 teacher-forcing 条件。该分支支付额外训练、历史压缩与 anchor 依赖，并与 coarse-to-fine 采样、少步蒸馏分别验收；降低 motion 可能改善某些 smoothness/aesthetic 指标，不等于所有质量都更好。[Helios v1 §3.1–3.3、§5.1–5.4](https://arxiv.org/html/2603.04379v1) 的去 anchor、去 frame-aware corruption 消融支持受测长视频中的局部收益，不证明任意长度稳定或通用实时吞吐。精细历史、运动或身份一致性退化时，保留更短生成段、更大历史窗口或既有 dense 路径。<!-- source-family:SF-2026-ARXIV-2603-04379 -->

## actual owner — books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md

L14–27:
本章的核心判断是：**Embodied AI 把生成结果变成具有 deadline、坐标系、控制权和不可逆副作用的 action。VLA 只有放在 perception → proposal → controller → environment → observation 的闭环中才有系统意义。**模型可以提出 trajectory 或 action chunk，low-level controller 与 safety envelope 必须独立决定如何、何时以及是否执行。

## 约束为何从 VLM 到 VLA 发生变化

VLM 的错误通常是一段错误描述；VLA 的错误会改变环境。于是输出 contract 从语义正确扩展为：

- action schema 与单位正确；
- reference frame 与 embodiment 匹配；
- 在 deadline 前产生；
- 与最新 observation 对齐；
- 满足动力学、碰撞和权限约束；
- 可中止、接管、降级或补偿。

同样的模型准确率在不同环境可能对应完全不同风险。控制系统关心的不只是平均 task success，还包括最大偏差、near miss、intervention、recovery 和 unsafe action rejection。
