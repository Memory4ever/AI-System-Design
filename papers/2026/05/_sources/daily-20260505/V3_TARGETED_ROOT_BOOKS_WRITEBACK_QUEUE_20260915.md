# 2026-05-05 V3 定点 Books root 写回队列

状态：作者侧 Proposed；只能由 root 按章节冲突顺序写入，写后必须经过新的非作者语义复核。

## `SF-2026-ARXIV-2605-00939` → `PLATFORM-EVALUATION-SYSTEM`

- 来源：https://arxiv.org/html/2605.00939v1
- 目标：`books/part-06-ai-infrastructure/66-evaluation-system.md`
- 现有覆盖：本章已有事实正确性、校准与证据门，但缺少把错误的局部可修正性作为独立诊断信号
- 所需增量：现有正文仍缺：以参数梯度敏感度近似局部曲率，区分可被小扰动修正的普通错误与对输入改写仍稳定的 stubborn hallucination。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 While EPGS provides a principled geometric signal for hallucination detection, several limitations exist. In this work, we address the critical challenge of Stubborn Hallucinations, where LLMs generate factually incorrect content with high confidence and stability. We propose Embedding-Perturbed Gradient Sensitivity (EPGS) , a geometric framework that distinguishes between generalized knowledge (residing in flat minima) and brittle memorization (residing in sharp minima) by probing the local cur
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01327` → `TRAIN-GRPO`

- 来源：https://arxiv.org/html/2605.01327v1
- 目标：`books/part-04-training-system/33-grpo.md`
- 现有覆盖：本章已有 group 与 token 级 credit assignment，但缺少由语义步骤持有 credit 与截断边界的中间粒度
- 所需增量：现有正文仍缺：把 token-level policy MDP 提升为推理 segment MDP，并按自适应分段计算 value、advantage 与 importance ratio。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 In this work, we analyzed the limitations of existing reinforcement learning approaches for reasoning in MLLMs and identified a fundamental mismatch between their optimization granularity and the step-wise structure of reasoning. To address this issue, we proposed Segment-Aligned Policy Optimization (SAPO), which aligns value estimation, advantage computation, and policy updates with reasoning steps under a step-wise MDP abstraction. By further introducing an entropy-based adaptive segmentation 
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01347` → `TRAIN-SFT`

- 来源：https://arxiv.org/html/2605.01347v1
- 目标：`books/part-04-training-system/29-sft.md`
- 现有覆盖：本章已有单教师 on-policy distillation 与 KL 方向选择，但没有教师集体形成 supervision state、confidence ownership 和 agent-step sampling 的分支
- 所需增量：现有正文仍缺：让多个教师在学生 on-policy state 上辩论形成 privileged distribution，并按任务选择 JSD 或 reverse-KL、按 agent step 稳定蒸馏。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 We presented MAD-OPD , a multi-teacher debate framework for on-policy distillation paired with OPAD for stable multi-step agentic training, and a task-adaptive divergence principle (JSD for agentic OPD, reverse KL for code). Across six teacher–student configurations and five benchmarks, MAD-OPD ranks first in every configuration; a 4B student trained under the 14B+8B teacher debate even exceeds its 14B teacher on LCB-v6 ( + 4.26 % +4.26\% pass@1, + 10.29 % +10.29\% BoN@16) at competitive token c
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01373` → `MULTIMODAL-GENERATIVE-PARADIGMS`

- 来源：https://arxiv.org/html/2605.01373v1
- 目标：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 现有覆盖：本章已有 selective refresh 与可变 commit，但未说明用跨步分布不稳定性决定哪些 token 重新开放
- 所需增量：现有正文仍缺：用相邻 denoising step 的 top-K 分布差识别高动态 token，并对其自对比重掩码，集中迭代修正预算。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 This work uncovers a critical yet long-overlooked property of DLMs: the heterogeneous information density distribution inherent in the generated context. Through systematic investigation of high-information-density (HD) tokens, we demonstrate their central role in both semantic guidance and decoding acceleration. Specifically, FoCore steers generation by exploiting HD tokens in a training-free, self-contrastive manner, while FoCore_A further leverages their convergence behavior to substantially 
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01429` → `TRAIN-LORA`

- 来源：https://arxiv.org/html/2605.01429v1
- 目标：`books/part-04-training-system/30-lora.md`
- 现有覆盖：本章已有 adapter merge 与冲突风险，但缺少 post-retrieval composition 的可靠性状态和 disagreement gate
- 所需增量：现有正文仍缺：在开放 LoRA 池检索后，以层级稀疏残差合并和多视图一致性审计决定组合、拒绝或回退。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 The primary causal comparison is tied to the matched FLAN-T5-Large, BBH, and 97-LoRA setting because that protocol fixes retrieval, support examples, decoding, and evaluation while changing the merge and reliability layers. The LLaMA, Qwen, and DeepSeek results provide protocol-distinct cross-backbone validation under the LoGo-style BBH-8 setting, but they use a different evaluation setup. We therefore distinguish protocol-matched causal evidence from protocol-distinct cross-backbone generalizat
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01642` → `TRAIN-RLHF`

- 来源：https://arxiv.org/html/2605.01642v1
- 目标：`books/part-04-training-system/31-rlhf.md`
- 现有覆盖：本章已有多目标 reward 与偏好聚合，但缺少 reward basis、jury membership 和时间变化权重的显式状态所有权
- 所需增量：现有正文仍缺：把人群偏好分解为低秩 reward basis，经民主过滤形成 jury，再随时间更新群体权重与策略。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 We presented Adaptive Pluralistic Alignment (APA), a modular pipeline for updating pluralistically aligned AI systems to track evolving societal values without repeating costly pretraining, fine-tuning, or large-scale reward modeling. APA achieves this by decoupling the expensive, one-time step of learning reward basis functions from the lightweight, recurring step of fitting new annotator weights and incorporating them into a democratic filtering procedure. The resulting system has several desi
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01710` → `PLATFORM-TRACE`

- 来源：https://arxiv.org/html/2605.01710v1
- 目标：`books/part-06-ai-infrastructure/69-trace.md`
- 现有覆盖：本章已有请求 trace，但缺少路由决策本身的候选集、策略版本和约束快照，模型名不能重建实际决策
- 所需增量：现有正文仍缺：为动态模型路由生成 route receipt，记录候选、策略版本、约束、选择结果与可披露 provenance。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 方法证据：exact-v1 §5、§6、§8 与 Appendix A 定义 per-answer route provenance、requested/effective route、fallback/tool/context/safety/redaction 字段及 v0.1 JSON Schema。
- 证据边界：position paper、schema proposal 与 documentation-based survey；§7 是 fictional case study，没有 alias drift、fallback frequency 或生产效果测量，不能推断 route receipt 会改善模型质量或独立满足合规。
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01733` → `MULTIMODAL-REPRESENTATION`

- 来源：https://arxiv.org/html/2605.01733v1
- 目标：`books/part-03-multimodal-world-models/23-multimodal-representation.md`
- 现有覆盖：本章已有多模态证据 provenance，但缺少 caption 作为不对称可疑证据的双路径 admission/拒绝控制
- 所需增量：现有正文仍缺：并行执行图像直答与 caption 辅助路径，以 confidence gate、information gain 和证据权重融合，限制错误 caption 锚定。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 We studied how captions influence VLM inference and identified two properties that govern the outcome: a deep anchoring effect, which extends a caption’s influence well past the final answer into the model’s reasoning trajectory, and an asymmetric error structure, in which omission outnumbers fabrication but each fabrication carries a much larger per-instance impact. Because both properties operate on the same caption, mitigating one without the other is not enough. Acting on this, we proposed G
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01749` → `PLATFORM-EVALUATION-SYSTEM`

- 来源：https://arxiv.org/html/2605.01749v1
- 目标：`books/part-06-ai-infrastructure/66-evaluation-system.md`
- 现有覆盖：本章已有 claim-level evidence gate，但缺少 exploration state 与 externally committed answer 的训练时分权
- 所需增量：现有正文仍缺：把长答案生成拆成 calibrated exploration 与 selective commitment，只将达到可靠性门槛的推理投影为最终 claim。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 In this paper, we propose an Exploration–Commitment Decoupling paradigm to improve long-form factuality by disentangling knowledge exploration from final answer commitment. We instantiate the paradigm with Calibration-Aware Generation (CAG) , a framework that integrates calibrated exploration and selective commitment, enabling models to perform end-to-end, calibration-aware generation by estimating step-level reliability and selectively incorporating trustworthy reasoning into final outputs. Exp
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01771` → `PLATFORM-EVALUATION-SYSTEM`

- 来源：https://arxiv.org/html/2605.01771v1
- 目标：`books/part-06-ai-infrastructure/66-evaluation-system.md`
- 现有覆盖：Ch66 已完整区分 outcome compliance 与 process compliance，并要求 textual agreement、typed action trace、environment affordance 与 effect receipt 分层；Ch69 只承载 trace 记录机制。
- 所需增量：无需新增正文；复用 Ch66 canonical evaluation block，拒绝在 Ch69 复制同一结论。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 Three limitations: (i) the 75-benchmark survey is bounded by 2022–2026 literature; emerging spec-evaluation efforts ( Ahmed et al., 2025 ; Zhang et al., 2025b ; Zhang et al., 2025a ) require tracking. (ii) R6 used ten non-expert raters (nine text-only); expert raters with tool-call training may achieve higher detection. (iii) Five task types do not exhaust all process instructions. Falsifiable claim: any RLHF-trained tool-using assistant evaluated only on text output, with delegation tools avail
- 状态：`applied_current_worktree_pending_independent_review`；existing canonical Ch66 body reused，duplicate Ch69 insertion rejected。

## `SF-2026-ARXIV-2605-01782` → `AGENT-RAG`

- 来源：https://arxiv.org/html/2605.01782v1
- 目标：`books/part-07-agent/76-rag.md`
- 现有覆盖：本章已有文档级 provenance 与 poisoning 防御，但缺少黑盒链路中从错误输出反查字符 span 的两阶段取证状态
- 所需增量：现有正文仍缺：先记录 misgeneration 与检索事件，再以 counterfactual deletion 回溯到字符级 poisoned span，并把 span provenance 返回修复环。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 The discussion below offers interpretations suggested by our empirical results. These should be read as evidence-consistent explanations rather than definitive causal claims. We presented RAGCharacter, a two-pass, event-conditioned forensic framework for character-level traceback in retrieval-augmented generation. In Pass-0, the system behaves as a standard RAG pipeline while logging prompt-anchored evidence and execution traces. In Pass-1, it re-enters a triggered trace and localizes the respon
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-01929` → `TRAIN-LORA`

- 来源：https://arxiv.org/html/2605.01929v1
- 目标：`books/part-04-training-system/30-lora.md`
- 现有覆盖：本章已有权重空间合并，但缺少跨 backbone/蒸馏变体迁移时的谱兼容性 gate 与无数据回退边界
- 所需增量：现有正文仍缺：在无目标数据时按谱刚性聚类 LoRA，并仲裁 video-diffusion 变体间的 routing interference。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 We studied why LoRAs trained on base video diffusion models often fail when reused on distilled variants. Through a weight-space analysis, we uncovered a pronounced spectral rigidity in VDMs and showed that both full fine-tuning and LoRA primarily introduce structured routing patterns at the cluster level, with incompatibility arising from conflicting routing interactions within spectrally functional subspaces. Motivated by these insights, we proposed Cluster-Aware Spectral Arbitration (CASA), a
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-02144` → `MODEL-SELF-ATTENTION`

- 来源：https://arxiv.org/html/2605.02144v1
- 目标：`books/part-02-model/14-self-attention.md`
- 现有覆盖：本章把 Q/K 视为可学习寻址坐标，但尚未呈现 projection-free kernel diffusion 作为不同归纳偏置的替代分支
- 所需增量：现有正文仍缺：用原始 hidden-state 间 Gaussian kernel 直接构造 row-stochastic attention，移除 Q/K 投影并以 bandwidth 控制局部性。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 These results highlight a gap between parametric efficiency and wall-clock efficiency: removing three projection GEMMs trades tensor-core-friendly matrix multiplications for bandwidth-dominated distance, exponentiation or normalization. A promising direction is fused Gaussian attention kernels (CUDA/Triton) that tile distance computation, exponentiation, masking, and normalization in a single IO-aware pass, analogous in spirit to FlashAttention [ 7 ] . This systems optimization is orthogonal to 
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-02152` → `MULTIMODAL-GENERATIVE-PARADIGMS`

- 来源：https://arxiv.org/html/2605.02152v1
- 目标：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 现有覆盖：本章已有 token commit/rollback，但缺少跨分辨率 draft、semantic lock 与 selective high-resolution compute 的组合
- 所需增量：现有正文仍缺：先低分辨率生成 draft，以语义验证锁定稳定区域，仅对未锁定区域恢复高分辨率并继续计算。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 We presented SpecEdit , a training-free dynamic-resolution framework tailored to diffusion-based image editing. SpecEdit follows a draft-and-verify paradigm: a low-resolution draft first approximates the semantic evolution of the edit, and token-level perceptual discrepancies are then used to identify tokens that warrant high-resolution Transformer computation, with a sparse uniform coverage set introduced to stabilize global structure. Across Qwen-Image-Edit and FLUX.1-Kontext-dev on GEdit-Benc
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-02269` → `PLATFORM-EVALUATION-SYSTEM`

- 来源：https://arxiv.org/html/2605.02269v1
- 目标：`books/part-06-ai-infrastructure/66-evaluation-system.md`
- 现有覆盖：本章已有 reward hacking 测试，但缺少把可利用机会、过程轨迹与表面成功分开的统一评价合同
- 所需增量：现有正文仍缺：用可观察环境中的隐藏 hacking opportunity 分离任务成功与 specification gaming，并测量 RL 后行为变化。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 While we aim for realism in our environments, motivated by recent concerns around evaluation-awareness ( Needham et al., 2025 ; Anthropic, 2025c ) , we also find value in environments that are less realistic but especially easy to run (e.g., the MC environments). We further find value in designing environments where executing the exploit does not require strong capabilities, meaning we can obtain signal on propensity rates across a broad range of model capabilities. However, we note this may com
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-02398` → `PLATFORM-EVALUATION-SYSTEM`

- 来源：https://arxiv.org/html/2605.02398v1
- 目标：`books/part-06-ai-infrastructure/66-evaluation-system.md`
- 现有覆盖：本章已有 prompt sensitivity，但缺少把 compliance scaffold 导致的自我评估退化单独隔离并复测
- 所需增量：现有正文仍缺：显示强制格式与合规措辞会在压力下压低模型元认知表达，要求把结构约束本身作为评测干预变量。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 We manually audited all 445 of DeepSeek V4 Pro’s Condition A failures as an illustrative archetype of the worst-case collapse. 100% were wrong answers; 0% were safety refusals (“I cannot comply”); 0% were empty responses. On EBD unanswerable tasks, 84.3% of responses provided an answer letter instead of correctly refusing. For this model, the threat does not trigger strategic deception—it triggers incompetence. A systematic failure taxonomy across all 8 collapsing models is left to future work. 
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-02469` → `TRAIN-GRPO`

- 来源：https://arxiv.org/html/2605.02469v1
- 目标：`books/part-04-training-system/33-grpo.md`
- 现有覆盖：本章已有 on-policy/offline 分界，但缺少何时 weighted SFT 能精确替代、何时因 support/ESS 产生不可约差距的判据
- 所需增量：现有正文仍缺：证明固定 reference 下 KL-regularized RLVR 可投影为 reference-sampled weighted SFT，并显式给出 support、ESS 与 one-shot gap。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 The projection result identifies when a fixed reference-rollout dataset can stand in for an online RLVR loop. The central condition is coverage. BOLT can precompute verifier scores and prompt-normalized density-ratio weights, but it cannot assign mass to completions that never appear under the reference policy. If correct or near-correct completions have probability p γ ​ ( x ) p_{\gamma}(x) close to zero under π ref \pi_{\text{ref}} , Proposition 23 requires Ω ⁡ ( 1 / p γ ) \Omega(1/p_{\gamma})
- 状态：`root_writeback_required_then_independent_review`。

## `SF-2026-ARXIV-2605-02765` → `AGENT-WORKFLOW`

- 来源：https://arxiv.org/html/2605.02765v1
- 目标：`books/part-07-agent/81-workflow.md`
- 现有覆盖：本章已有工作流 verifier，但缺少 hard/soft constraint 的不同所有权、冲突优先级与用户修订闭环
- 所需增量：现有正文仍缺：把用户约束分成 hard 与 soft：hard 交给形式 checker，soft 交给可校准 judge，并保留冲突解释与人工修改。应在保留旧方案适用条件的同时，补入状态/控制变化、证据边界、代价、失败模式与回退。
- 证据边界：只采用 exact-v1 所列方法、实验与限制段落支持的机制关系；未披露的硬件、并发、精度、长度或 SLO 不补齐，作者 benchmark 不外推。 Our findings from two user studies highlight the central challenge of combining reliability and flexibility in LLM-based planning. General users and domain experts alike recognized the value of balancing strict enforcement of critical rules with the adaptability needed to accommodate preferences and evolving contexts. Study 1 showed that explicitly distinguishing hard from soft constraints increased perceived performance, usefulness, and satisfaction, and crucially, this added value did not come
- 状态：`root_writeback_required_then_independent_review`。
