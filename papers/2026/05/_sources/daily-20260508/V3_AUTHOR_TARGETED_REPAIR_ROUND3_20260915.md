# 2026-05-08 V3 作者定点返修 Round 3

## 范围与状态

本轮只处理 `V3_FRESH_FINAL_REVIEW_ROUND2_20260915.md` 的失败项，不扩大来源或 raw identity。作者不能自签最终 Gate；完成后仍为 `Ongoing`。

机械状态更新为：`619 = 132 retained + 487 pre-denominator closure`；132/132 Evidence complete，92 deep + 40 standard。Books 为 49 项既有 Applied、16 项已写回待终审、4 项新增 root 写回、63 项 No Change。

## 四项重开 Evidence Review

### 2605.05329 — Understanding Annotator Safety Policy with Interpretability

- **Score V3：** 3 + 2 + 3 = 8；Deep。
- **Owner：** `PLATFORM-EVALUATION-SYSTEM`，向 `TRAIN-DATA` 与 `PLATFORM-SECURITY` handoff。
- **Method：** exact-v1 §3 从既有 binary safety labels 构建共享 concept space，并为每个 annotator 拟合 non-negative logistic regression 或 DNF policy model。概念提取器与 policy model 分权，后者只近似 annotator 的实际标注行为。
- **Evaluation：** BeaverTails、WildGuardMix、五个 LLM annotator 与 DICES human annotations；报告 held-out predictive accuracy、controlled policy recovery 和 counterfactual faithfulness。`>80%` 只属于论文所列 LLM annotation 设置。
- **Limitations / non-proof：** concept space 依赖 LLM 生成与 embedding labeling；模型能显示“谁在什么概念上不同”，不能解释价值差异的真实原因；尚未证明 APM 驱动的 policy update 会改善下游模型或部署安全。
- **长期增量：** majority vote 不能抹平 operational failure、policy ambiguity 与 value pluralism。Evaluation 必须保存 annotator/policy identity，并按 disagreement type 选择返工、澄清或治理分支。
- **Disposition：** `Integrate — Root writeback required`。

### 2605.05331 — ViTok-v2

- **Score V3：** 3 + 2 + 3 = 8；Deep。
- **Owner：** `MULTIMODAL-REPRESENTATION`，向 `MULTIMODAL-GENERATIVE-PARADIGMS` handoff。
- **Method：** NaFlex variable-resolution training、2D RoPE、浅 encoder / 大 decoder、Charbonnier + SSIM + DINOv3 perceptual loss；避免 adversarial objective，并在 inference 使用 sliding-window attention。
- **Evaluation：** 约 2B images；88M～4.5B decoder、多个 compression ratio、450M/1.2B flow model；ImageNet reconstruction 与 generation protocol 明确区分 rFID/gFID。作者披露 128 H200、BF16/FP8 GEMM、batch 8192；这些条件不能外推成通用效率结论。
- **Limitations / non-proof：** 主要覆盖图像 autoencoder 与所列数据/模型；native-resolution reconstruction 不证明任意视觉分布、视频或 production decoder latency；Pareto ranking 会随 generator capacity 和 metric 改变。
- **长期增量：** representation artifact 必须绑定 resolution/aspect-ratio policy、compression ratio、latent channels、decoder capacity 与 loss identity；“更好 reconstruction”不能脱离 downstream generator capacity 声明更优 tokenization。
- **Disposition：** `Integrate — Root writeback required`。

### 2605.06609 — Transformers Efficiently Perform In-Context Logistic Regression via Normalized Gradient Descent

- **Score V3：** 3 + 2 + 3 = 8；Deep。
- **Owner：** `MODEL-TRANSFORMER-LAYER`，向 `WORLDVIEW-LLM-INTELLIGENCE` handoff。
- **Method：** 构造 softmax-attention Transformer，使每层精确执行一次 in-context logistic loss 的 normalized-gradient step；再用 one-step GD teacher 监督单层并循环应用形成 looped model。
- **Evaluation / proof contract：** 论文给出训练 loss landscape、局部极小值、线性收敛及特定线性分类分布下的 OOD guarantee；系数比对应 effective learning rate。
- **Limitations / non-proof：** 这是受限构造与理论分布，不证明真实大模型的任意 ICL 都执行梯度下降，也不证明 hidden state 与可观察 optimizer state 等价；teacher algorithm 与 learned algorithm 也不能由行为拟合唯一识别。
- **长期增量：** Layer 可以被理解为对 context-carried state 的迭代更新器，但“像优化”必须绑定函数类、数据分布、循环共享参数和定理条件。
- **Disposition：** `Integrate — Root writeback required`。

### 2605.06660 — Verifier-Backed Hard Problem Generation for Mathematical Reasoning

- **Score V3：** 3 + 3 + 3 = 9；Deep。
- **Owner：** `TRAIN-DATA`，向 `TRAIN-GRPO` 与 `PLATFORM-EVALUATION-SYSTEM` handoff。
- **Method：** setter–solver–verifier 三方 self-play；setter reward 同时受 verifier 的 validity 与 solver 的 difficulty 约束。Hard symbolic verifier 与 Soft LLM verifier 的 authority 和保证范围分开。
- **Evaluation：** indefinite integration 与 general math；披露 generation/filter funnels、solver/judge acceptance、held-out split、ablation 和 subgroup results。general-math Soft verifier 的结果是 pipeline evidence，不是数学正确性保证。
- **Limitations / non-proof：** hard guarantee 只适用于可符号验证的窄域；soft judge 仍会接受细微错误、欠规格问题或 reward-hacking artifact；不同 baseline 的 budget、mixture、selection 和 schedule 不完全匹配，主要覆盖一个 model family。
- **长期增量：** synthetic curriculum 必须把 problem generator、solver snapshot、verifier type/version、filter funnel 和 reward policy 绑定为同一 data lineage；难度不能由 setter 自证，soft verifier 失败时回退 deterministic checker、人工 gold 或 abstention。
- **Disposition：** `Integrate — Root writeback required`。

## 同错误层有界反查

在四类错误模式中复核 12 个最易误判的 closure；没有扩展 raw set。以下项目保持分母前关闭，是因为 current Books 已承载其长期命题或证据仍是 workload-local，并非仅靠题名拒绝：

| Family | 复核结论 |
| --- | --- |
| `2605.05662` XL-SafetyBench | country-grounded benchmark 是受限数据资产；Ch66 已要求 distribution、slice、policy 与 evaluator identity，未新增可迁移 mechanism。 |
| `2605.05668` LVLM attention | RID/MixIG 与 noise replacement 是诊断证据；Ch14 已拥有 attention weight 非解释、intervention 与 dense fallback，论文未建立可部署架构替换。 |
| `2605.05742` Weak-to-Strong linear theory | 线性 logistic setting 的 theorem 不改变本日已保留的 `2605.05710` pretraining/W2S owner 或系统合同。 |
| `2605.05781` UNO | frozen understanding expert 向 generator 传 gradient 的受限 post-training 实现；Ch24 已承载 shared understanding/generation state、gradient authority 与专用模型 fallback。 |
| `2605.05893` LoVer | white-box hidden-state verifier 与逻辑一致性 objective 是 learned sensor；Ch66 已明确 verifier 不拥有 truth、需独立 oracle 与 abstention。 |
| `2605.06070` ArenaPO | offline Arena reward 的 diffusion preference tuning 是局部 algorithm branch，未改变现有 reward provenance、judge drift 与 DPO/PPO fallback。 |
| `2605.06170` DynT2I-Eval | dynamic prompt、pairwise evaluation 与 online ranking 已由 Ch66 的 adaptive evaluation、sample identity、evaluator revision 和 human fallback 覆盖。 |
| `2605.06201` VL-LCM | annotation-free logical consistency 只能作 sensor；论文也承认 consistency 不保证 correctness，Ch66 已明确同源一致性不能支持 truth acceptance。 |
| `2605.06318` annotation variation | 作为 `2605.05329` 的经验旁证，不单独改变 owner；interaction finding 不能替代 policy model、workflow 或 deployment validation。 |
| `2605.06509` FreeSpec | SVD global/local reconstruction 是两个 base video models 上的 training-free feature modulation；Ch24 已承载 latent-history、spectral/selection failure 与 base-model fallback，不能外推 scene planning。 |
| `2605.06643` MMDG-Bench | 7402 networks/95 tasks 说明 matched contract 与 missing-modality slice 的必要性；Ch66 已拥有 distribution/slice/corruption identity，benchmark 本身不新增控制机制。 |
| `2605.06667` ActCam | camera/pose control 是生成模型受限实现；Ch24/26 已拥有 action/camera condition 与 validator/physical-evidence 边界。 |

## 作者 Gate

- 四项 exact-v1 可访问、未见 withdrawn banner，无 blocked/disputed。
- 四项已完成 score、Method、evaluation、limitations、owner 与 disposition。
- Books 尚未写回；两项已有正文只生成重排指令。
- 状态保持 `Ongoing`，等待 root 写回/重排和新的非作者终审。

