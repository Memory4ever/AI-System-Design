# 2026-05-08：九项返修后的 fresh non-author 最终复核

## 结论

**FAIL。** 当前日报继续保持 `Ongoing`，`final_independent_signoff = false`。

失败不是材料访问问题，也不是 6 个 root Books 新段本身的问题。当前快照的机械账、9 个 reopened family 的
exact-v1 Evidence、6 个新 Books 段均通过；但一个 `No Change — Existing Coverage` 没有真实正文承载，且对
478 个 closure 的有界高风险挑战又确认 10 个 contribution-gate false negative。因此不能签发 Complete。

## 已通过范围

### 账本与报告

- canonical ledger 为 `V3_RECERTIFICATION.json`，复算得到 `619 = 141 retained + 478 closure`。
- 141 项均具有 exact-v1 URL、public time、Score V2、Evidence record、Stable Node 与 Books disposition；三项分数
  均在 `0..3`，Total 均等于分项之和。
- 审阅深度为 `101 deep + 40 standard = 141`；Books 为 `75 Applied + 66 No Change = 141`。
- README 第 3 节恰好列出 141 个唯一 active candidate，与 canonical ledger 一一对应；评分和审阅深度账一致。
- 当前 retained 集合没有 blocked、disputed 或 withdrawn；Materials Request 为空。

### 九项限定返修

`2605.05278`、`2605.05485`、`2605.05646`、`2605.05702`、`2605.05709`、`2605.05892`、
`2605.06124`、`2605.06192`、`2605.06207` 的 exact-v1 HTML 均可访问，题名、Method、Evaluation 与
Limitations/non-proof 定位真实存在，页面未见 withdrawal 标记。9 项 Score、owner 与 Books disposition 和
`V3_BOUNDED_REPAIR_NINE_FALSE_NEGATIVES_20260915.md` 一致。

### 六个 root Books 新段

以下 marker 均唯一、owner 与 ROADMAP 一致，并位于对应章节真正的 `## Review notes` 之前：

| Source Family | Owner | 复核结果 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-05278` | `MODEL-MOE` | 通过；只把 routing information 写成 workload-specific proxy，保留 load/quality/capacity/communication fallback。 |
| `SF-2026-ARXIV-2605-05485` | `AGENT-WORKFLOW` | 通过；solver 只拥有候选求解权，workflow/effect/verifier authority 和开放任务 fallback 清楚。 |
| `SF-2026-ARXIV-2605-05646` | `MULTIMODAL-REPRESENTATION` | 通过；topology、semantic value 与 residual texture 的责任分解及跨域/decoder 代价边界完整。 |
| `SF-2026-ARXIV-2605-05702` | `TRAIN-DATA` | 通过；construction artifact、admission、bounded reward 与 terminal truth authority 分离。 |
| `SF-2026-ARXIV-2605-06124` | `MULTIMODAL-GENERATIVE-PARADIGMS` | 通过；dual-pass CFG 到 initial-prior steering 的条件分支、一阶近似、漂移风险和 fallback 完整。 |
| `SF-2026-ARXIV-2605-06207` | `MULTIMODAL-REPRESENTATION` | 通过；position-indexed capacity、entropy cliff、artifact identity 与 uniform-codebook fallback 完整。 |

这六项不需要返修 Books，也不能因为本轮整体 FAIL 被推倒重写。

## 有界失败 1：一个 No Change 没有正文承载

### `2605.05709` — Conceal, Reconstruct, Jailbreak

日报与返修记录声称 Ch72 已有“恶意信号藏在原始文本视图之外、可信重建后进入 Context，因此同时校验 data
layer 与 reconstruction layer”的长期命题。当前 Ch72 中这句话只出现在 `## Review notes` 后的历史归档说明，
不在机制正文；正文中 `Review notes` 之前的“重建”段落讨论图谱删除、skill reconstruction、memory backflow 等
不同问题，不能作为该攻击链的命题 locator。

因此 `No Change — Existing Coverage` 不成立。最小返修只能二选一：

1. 在 Ch72 `## Review notes` 前补入一个有界机制段，明确 raw-view concealment → trusted reconstruction →
   model context 的攻击路径、data/reconstruction 双层检查、作者 benchmark 边界与不能推出通用防御率；或
2. 找到当前主正文中真正等价的既有命题并给出精确 locator。当前复核未找到这样的命题。

修复后同步该 family 的 Books disposition/marker，再由新的非作者 reviewer 复核；本 reviewer 不编辑 Books。

`2605.05892` 的 nonlinear/local intervention 命题位于 Ch66 主正文且边界充分，`2605.06192` 的
“Action realization 与 environment response 应由不同 owner 承担”位于 Ch25 主正文；这两项 No Change 通过。

## 有界失败 2：closure 仍有高风险假阴性

本轮不重扫 478 项。只从标题明确触及当前主线的高风险 closure 中读取完整摘要，形成 12 项风险定向样本；这不是
总体误差率估计。`2605.05758`（生物医学 tool-calling 数据集）和 `2605.05914`（当前量子 adapter 单一 operating
point）仍可维持分母前关闭；以下 10 项的题名与完整摘要已经满足“潜在贡献明确、实验可信度待核”的候选准入条件，
不能继续以“局部方法/未改变 owner”的通用理由关闭：

| arXiv | 摘要已经给出的可核验增量 | 建议初始 owner |
| --- | --- | --- |
| `2605.05566` | GRPO all-fail group 的 zero-advantage 会浪费数据与 rollout budget；prompt-space perturbation 改变 hard-query exploration/resampling control。 | `TRAIN-GRPO` |
| `2605.05602` | 给出 attention coreset 的近最优空间上界与下界，直接约束 attention state 压缩是否可能；是否存在可执行构造须由 exact-v1 审阅判定，不能在贡献门前关闭。 | `MODEL-SELF-ATTENTION` / `MODEL-LONG-CONTEXT` |
| `2605.05676` | multi-task instruction tuning 的共享参数产生 gradient interference，并提出正交高奇异值 LoRA experts 改变能力/参数共享方式。 | `TRAIN-SFT` / `TRAIN-LORA` |
| `2605.05781` | understanding objective 直接监督 generative representation，改变统一多模态模型中理解与生成的 gradient/data ownership。 | `MULTIMODAL-REPRESENTATION` / `MULTIMODAL-GENERATIVE-PARADIGMS` |
| `2605.05826` | negative-dominant update 与 group positive advantage 试图避免 RLVR 缩窄 base-model exploration support，并报告 pass@k coverage 变化。 | `TRAIN-GRPO` |
| `2605.05893` | 用 internal activation、binary latent verifier 与三类 logical consistency constraint 构造无监督 verifier，改变 verifier label/constraint 来源。 | `PLATFORM-EVALUATION-SYSTEM` / `TRAIN-GRPO` |
| `2605.06460` | 在 late-interaction 的质量/索引成本与 single-vector 的 serving/storage 优势之间，以 internal-layer probing/fusion 改变 retrieval artifact。 | `AGENT-RAG` |
| `2605.06507` | 为多 reward diffusion RL 分离 advantage/gradient，再由 QP 合成 update direction，直接改变 multi-objective update control 与计算代价。 | `TRAIN-RLHF` / `MULTIMODAL-GENERATIVE-PARADIGMS` |
| `2605.06557` | 相同 return 可对应不同 redundant assignment、diversity 与 coordination efficiency，明确提出 process-level multi-agent evaluation contract。 | `PLATFORM-EVALUATION-SYSTEM` / `AGENT-MULTI-AGENT` |
| `2605.06643` | 受控统一协议显示多模态 domain-generalization 的近期增益可能来自不一致评价，并补入 corruption、missing modality 与 trustworthiness 条件。 | `PLATFORM-EVALUATION-SYSTEM` / `MULTIMODAL-REPRESENTATION` |

这些只是在 contribution gate 被重开，不代表论文结论已成立或必须进入 Books。最小返修是：只重开上述 10 项，读取
exact-v1 的必要 Method/Evaluation/Limitations，完成 Score、Evidence、唯一 owner 与 Books Decision；随后按这 10 项
暴露的共同错误理由，对同一高风险 closure 层做一次有界反查。不得重开已通过的 141 项或扩大来源/日期。

## Gate

- Mechanical ledger：PASS。
- 141 current Evidence/Score/owner/disposition：PASS（但 `2605.05709` 的 Books disposition 需要返修）。
- 6 个新 Books 段：PASS。
- 3 个 No Change：2 PASS / 1 FAIL。
- Bounded closure challenge：FAIL，确认 10 个 contribution-gate false negative。
- Withdrawal/access/materials：PASS。
- Final Independent Gate：**FAIL**。

本轮没有修改 Books，没有 stage、commit 或 push。跨模型第二意见未执行：这是非交互式、限定范围的独立终审，且
当前失败已有直接可复核的正文与题摘证据；后续新的非作者复核才是修复后的签署者。
