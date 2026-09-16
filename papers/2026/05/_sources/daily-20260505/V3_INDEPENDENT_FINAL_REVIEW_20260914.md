# 2026-05-05 V3 fresh-context 独立终审（2026-09-14）

**复核者：** `fresh-context:may11_v3_author_as_may05_final_reviewer`

**角色隔离：** 未参与 2026-05-05 作者修复或 root Books 写回；本轮不重扫来源、不扩大日期，也不修改 Books 或代替作者修复。

**结论：** 未通过。Daily 保持 `进行中`。

## 已独立复算并通过的部分

- 分母守恒成立：`1058 raw = 138 retained + 920 pre-denominator closure`；1058 个 arXiv ID 与 Source Family ID 均唯一，138 个 retained 与 138 个 Evidence Review 身份集合一致。
- owner receipt 的原始路径可复算为 `754 official OAI direct + 304 revision recovery = 1058`。当前 V3 没有把普通 revision 当作当日新事件；日期结论以 initial registration、ID/version identity 与 2026 年 5 月 EDT 公告批次对应的北京时间 08:00 共同约束，不把作者提交时间或当前 OAI revision datestamp 单独当作 owner date。
- Evidence 数量成立：136 个可访问候选完成作者审阅，其中 67 个 deep、69 个 standard；2 个 exact-v1 blocked 与正面证据、评分结论和 Books 写回隔离。
- 三维评分可复算，所有 7～9 分候选均进入深入审阅；未发现用降分绕过深审的 retained 项。
- Books disposition 数量成立：30 个 `Integrate Applied`、106 个 proposition-level `No Change`、2 个 `Blocked / Unverified`。
- 30 个 Applied 的 source-family/semantic-body marker 均唯一且位于实际章节正文、`Review notes` 之前。逐项回读实际正文后，均能定位旧路径、约束变化、state/control 变化、trade-off/failure/fallback 与 evidence boundary；不是只有 trace 或“已吸收”标签。
- 对 6 个较易误收的 Applied 项（`2605.01032`、`2605.01790`、`2605.01837`、`2605.01928`、`2605.02083`、`2605.02106`）做反向挑战后，保留成立：它们分别以形式治理边界、层级生成、GPU 功率控制、不可微训练分支、artifact 级联一致性和显式记忆分层进入正文，且已明确理论/任务/规模边界。
- 106 个 No Change 均有存在的目标章节、可定位命题和逐命题比较；分层复核 `2605.00827`、`2605.01130`、`2605.01644`、`2605.02241`、`2605.02739` 等不同 owner/分数项后，未发现把新 owner 变化误写为 Existing Coverage。
- 前两轮作者修复恢复的项目以及第二轮 bounded audit 的 15 项均保留了唯一身份；其中 6 项新增 Books 写回与 9 项 No Change 的当前处置可回溯。
- 本地 exact-v1 缓存未检出 arXiv 官方 withdrawal notice；ledger 中的 withdrawal 文本是论文内容或审阅状态说明，不是撤稿标记。

## 未通过：高风险 closure 仍有明确 false negative

本轮先按机制风险分层，再在每层反查题名与完整摘要。低风险抽样中的通用任务、领域应用、position paper 和单一 benchmark closure 没有形成新的长期 owner；但训练状态、推理状态、生成范式、Embodied 控制与安全后训练层仍发现 7 个不能继续留在分母前的 family：

| arXiv v1 | 题摘已明确的设计变化 | 最小重开范围 |
| --- | --- | --- |
| `2605.01208v1` | 在稀疏 GUI reward 下，以 anchor 和 variance-adaptive tempering 防止 GRPO 低方差组的 advantage collapse，并把 abstention 纳入前置 SFT | `TRAIN-GRPO`；核验 GuAE、reward/rollout contract 与低方差反证 |
| `2605.01477v1` | 将 agentic goal-video imagination 与 action-space diffusion controller 分层，并给出跨 embodiment、sim-to-real 与真实 G1 的执行边界 | `MULTIMODAL-WORLD-MODELS` / `MULTIMODAL-EMBODIED-VLA`；核验 open-loop、安全与频率条件 |
| `2605.01766v1` | 用 Layer-wise Relevance Propagation 形成 inference-time objective，并直接更新 KV representation 以调整 modality contribution | `MULTIMODAL-REPRESENTATION` / `INFER-KV-CACHE`；核验更新范围、代价、回退与 hallucination evaluator |
| `2605.01913v1` | 下游 fine-tuning 会使 safety representation 几何漂移；方法约束 hidden-space update 以保留 refusal structure | `TRAIN-PRETRAINING` / `PLATFORM-SECURITY`；核验跨模型结果、utility trade-off 与 adaptive attack 边界 |
| `2605.01959v1` | LoRA rank 从静态参数变为按输入复杂度、且训练与推理一致的条件容量状态 | `TRAIN-LORA`；核验 rank controller、train/infer identity、额外路由成本与静态 LoRA fallback |
| `2605.02323v1` | 顺序 attention 增加 residual evidence state，显式记录哪些证据已经被解释；消融指出仅顺序化或正则化不能防 slot collapse | `MODEL-ATTENTION` / `MULTIMODAL-REPRESENTATION`；核验 additive-superposition 假设与跨任务边界 |
| `2605.02641v1` | 在统一 AR–Diffusion 架构中引入细粒度 DiT-MoE，并用 distillation + RL 将 30-step editing 压缩为 4-step | `MULTIMODAL-GENERATIVE-PARADIGMS` / `MODEL-MOE`；核验统一状态、routing、few-step 质量与 benchmark 条件 |

这 7 项的当前 closure 都以“局部方法/单域增量、不改变 owner”的通用结论结束，但其完整摘要已经给出具体 state、control 或 training/inference contract 变化。是否最终写 Books 尚未确定；它们必须先进入候选分母、取得 exact-v1、评分并完成 Evidence/Books Decision，不能在 Evidence Review 之前直接判 No Change。

## 边界 closure 的独立裁决

以下 5 项不要求进入候选分母，但作者必须把当前通用句替换成对应的具体关闭理由，避免以后同类项目再次误开：

- `2605.00915`：SSMProbe 改变的是冻结视觉表示的 probe/readout 顺序，不改变被测模型的训练、推理或 representation owner。
- `2605.01078`：SONAR 是 prompt sanitization 的一个 NLI-graph 实现；题摘没有证明该 heuristic 能替代 trust boundary、reference monitor 或 post-action validation。
- `2605.01462`：LocalAlign 是 near-target adversarial-example 的训练分支；它没有改变 trusted/untrusted data ownership 或生产 admission contract。
- `2605.01853`：StALT 是 hidden-state trajectory probe；题摘未建立 release-grade correctness calibration、可移植阈值或执行控制权。
- `2605.02421`：AOCI 是 code-repository 的特定索引协议与 benchmark；增量仍可由现有 context/RAG artifact identity 承载，不产生新的通用 owner。

## Source terminal 与 Blocked 隔离

- `SRC-OPENAI`、`SRC-GOOGLE-AI`、`SRC-QWEN`、`SRC-MOONSHOT`、`SRC-XIAOMI-MIMO` 缺目标日可复查的历史列表停止点；当前报告已明确禁止据此声明机构源零遗漏。只有取得目标窗口的官方归档/带日期列表时才重开对应来源，不重扫 arXiv。
- `2605.02206v1` 与 `2605.02375v1` 缺 exact-v1 正文，现有题摘不用于正面证据或 Books。exact-v1 PDF、作者存档全文或版本对应正式出版正文到达时，只重开各自 family。
- 这些 isolated terminal 不要求报告无限等待；但在材料到达前必须继续显示为 Coverage Limitation 或 `Blocked / Unverified`，不能计入 Evidence complete。

## 精确最小修复清单

1. 只重开上表 7 个 false-negative family，不扩大日期或重扫 1058 个 raw identity。
2. 对 7 项完成 exact-v1 withdrawal、Method、Evaluation、Limitations、三维评分和 owner 审阅；Books 仅在逐命题比较确认真实缺口时进入 root 串行写回。
3. 将 5 个边界项改成上节对应的 family-specific closure；不需要为它们下载全文或制造候选。
4. 从最终数组重新生成 retained/closure、Evidence 与 Books 汇总，并同步 Daily 正文；保持两个 blocked 和五个机构源 terminal 的隔离与精确重开条件。
5. 由另一名未参与修复/写回的 fresh-context reviewer 重新挑战新增候选、受影响 closure 和任何新增 Books 写回。

## Gate

- Coverage / Candidate Denominator：**未通过**；确认 7 个 false negative。
- Evidence：现有 136 个可访问候选结构通过；7 个新增候选尚未审阅，整体 **未通过**。
- Books：现有 30 个 Applied 与 106 个 No Change 通过本轮实际正文/逐命题复核；新增候选尚未完成 Books Decision，整体 **未通过**。
- Daily：**进行中**。

## 校验边界

- canonical ledger 与 Evidence JSON 均可解析；当前复算为 `1058 / 138 / 920` 与 `138 reviews / 67 deep / 69 standard / 2 blocked / 30 Applied / 106 No Change`。
- 30 个 Applied 的正文 marker 唯一且位于 `Review notes` 之前；106 个 No Change 的目标路径与 locator 可定位。
- 本终审没有修改 Books、没有重扫来源、没有扩大日期，也没有 stage、commit 或 push。
- 机器 validator 只能证明结构和可判定一致性，不能消除上述语义 false negative。
