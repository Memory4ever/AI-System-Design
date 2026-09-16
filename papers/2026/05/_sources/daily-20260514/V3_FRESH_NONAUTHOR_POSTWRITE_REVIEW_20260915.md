# 2026-05-14 V3 Fresh Non-author Post-write Review

**复核时间：** 2026-09-15T15:42:27+08:00

**复核者：** fresh non-author context `/root/may14_fresh_postwrite`

**结论：** `FAIL — Ongoing`

## 复核边界

本次只审阅 2026-05-14 已有 V3 artifacts、Daily 正文和 78 项 root Books 写回，不扩展日报窗口，不重跑来源，不修改 Books。

## 已通过的检查

- Candidate artifacts 当前记账为 `714 = 118 retained + 596 pre-denominator closure + 0 withdrawn`；2 个官方 Source Family 另计后 denominator=120。
- `exact-v1-source-reviews-bounded.json` 含 118 项：114 个 deep、4 个 standard；118/118 `accessible`，0 withdrawn，0 non-accessible。
- 78 项 root queue 的 Stable Node ID 与 owner path 均能在 `ROADMAP.md` 解析；Source Family 无重复。
- 78/78 Books marker 在唯一 owner 中各出现一次，且都位于该章最终 `## Review notes` 之前。
- 逐项审阅 78 个写回块后，未发现只追加论文名或 marker 而没有正文语义的条目。写回内容均能定位旧路径、约束变化、机制或状态责任、收益与代价、失败/回退及 exact-v1 evidence boundary；7 组共享段落中的两个 Source Family 也分别承担可辨识的证据作用。
- 40 个 `No Change — Existing Coverage` 均有 owner；对其中使用章级入口标题的高风险项回到 Books 正文对读，未发现必须仅因标题泛化而改判的条目。

## 未通过：Candidate Denominator 仍有 False Negative

对 596 个 closure 做了两层有界复核：固定种子的 30 项抽样，以及 4 项接近 Books 边界的定向挑战。以下 6 个 Source Family 的完整摘要已经明确改变长期机制、状态或控制责任，却仍被标记为 `pre_denominator_closure`；它们至少应进入 Candidate Denominator，再按 Score、Evidence Review 和 Books Decision 处理：

1. `SF-2026-ARXIV-2605-12863` — **Language-Based Agent Control**  
   摘要提出面向 Agent 应用的 programming model：让 Agent 生成带类型程序，由 type checker 在 effect 前拒绝不安全程序，并让 access control、information flow、provenance 统一覆盖 Agent 与 scaffolding。当前关闭理由称其“未改变平台信任边界、授权 owner”，与摘要披露的静态检查和 runtime enforcement 边界直接冲突。

2. `SF-2026-ARXIV-2605-12879` — **ASAP: Amortized Doubly-Stochastic Attention via Sliced Dual Projection**  
   摘要明确给出 train-then-compile 路径：训练时保留 Sinkhorn，推理时替换为固定 sliced-dual operator。它改变 Attention 的 training/inference contract 与在线迭代状态，不应以“只新增 task/evaluator/benchmark contract”关闭。

3. `SF-2026-ARXIV-2605-12913` — **Revisiting DAgger in the Era of LLM-Agents**  
   摘要把长程 Agent 的 covariate shift 定义为 student rollout 改变后续 state distribution，并以 teacher/student turn-level interpolation 收集 on-policy-like states、再用 teacher label 训练。它改变 trajectory acquisition 与监督 ownership，不能以“只新增 benchmark contract”关闭。

4. `SF-2026-ARXIV-2605-13228` — **ReTool-Video: Recursive Tool-Using Video Agents with Meta-Augmented Tool Grounding**  
   摘要区分 high-level intent 与 primitive tool call，引入 resolver 承担 parameter repair、tool substitution 与 decomposition，并在 runtime 递归落地 tool chain。它明确改变 Agent action representation、resolver authority 与失败恢复路径，不是单纯领域 benchmark。

5. `SF-2026-ARXIV-2605-13316` — **Test-time Sparsity for Extreme Fast Action Diffusion**  
   摘要披露跨 current forward、previous denoising timestep 与 earlier rollout iteration 的 cache reuse，以及 encoder/pruner 与 decoder 的异步重叠。当前关闭理由称其“未改变 cache ownership、调度或 SLO contract”，与摘要内容直接矛盾。

6. `SF-2026-ARXIV-2605-13821` — **Harnessing Agentic Evolution**  
   摘要把累计 candidate、feedback、trace 与 failure 组成 process-level state，并让 meta-agent 编辑控制后续演化的 procedure/context，而不是直接生成下一个 candidate。它改变 workflow state 与 meta-edit authority，不能以“只新增 benchmark contract”关闭。

## 一致性问题

Daily 的结论和复核段使用 `118/596`，但来源覆盖表中的 `SRC-ARXIV` 行仍写 `77 retained + 637 closure`。后者是修复前 checkpoint，出现在当前报告的有效覆盖结论中会造成分母冲突。`screening-ledger-final.json` 也仍保留部分已恢复项目的旧 closure 状态；若作为历史 checkpoint 保留，必须明确其非当前状态，不能与 `screening-outcomes-v3.json` 并列充当 final ledger。

## Gate Decision

78 项 Books 写回本身通过本轮 post-write review；本次失败来自 Candidate Denominator 的未闭合，而不是要求返工这些 Books。重新裁决上述 6 项、同步唯一 final screening ledger、修正 Daily 覆盖数字，并完成新增候选所需 Evidence/Books Decision 后，必须再由 fresh non-author context 复核，才能把日报改为 `Complete`。
