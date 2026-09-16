# 2026-05-13 V3 Round 7 fresh non-author 写后复核

- 复核角色：fresh-context non-author；未参与 Round 7 作者返修或 root Books 写入。
- 复核范围：Round 7 六项正文写回、当前 838 identity 守恒与整日冻结状态。
- 结论：**六项写回通过；整日报告未通过，保持 Ongoing。**
- Cross-model：本轮是父任务委派的独立非作者复核；未再发起额外跨模型复核。

## Round 7 六项写回验收

以下六项均满足：唯一 canonical Books 文件、start/end binding 各一个、正文位于锚定 `## Review notes` 之前、机制 owner 与 ROADMAP 一致、正文同时保留旧基线、变化约束、状态/控制责任、exact-v1 证明与未证明、trade-off/failure 和 fallback/coexistence。

| arXiv | Owner | 写后判断 |
| --- | --- | --- |
| `2605.11136` | `AGENT-MULTI-AGENT` | 通过；individual/team/population 三层状态与 population controller 的 commit responsibility 清楚，3.6× 推理成本和开放 population 未证明边界保留。 |
| `2605.11167` | `AGENT-MULTI-AGENT` | 通过；latent lockstep channel、两模型生成状态和 tool effect commit 分离，文本 handoff/异步/单模型 fallback 保留。 |
| `2605.11169` | `AGENT-TOOL-CALLING` | 通过；online bandit 只更新下一次 selector，未越过 permission/effect gate；unsafe exploration、poisoning 与 non-stationarity 边界完整。 |
| `2605.11225` | `AGENT-PLANNING` | 通过；versioned incumbent、suffix replacement 与 verifier commit 形成完整 replan 演进链，token proxy 与 HITL/autonomous 边界没有外推。 |
| `2605.11996` | `PLATFORM-SECURITY` | 通过；KG→encoder/projector→soft prompt 被纳入供应链 identity，semantic anchor 仍只是 sensor，禁用旁路和 signed snapshot fallback 明确。 |
| `2605.12477` | `PLATFORM-EVALUATION-SYSTEM` | 通过；Deletion/Cascade/Absence 与 retriever/updater/answerer 分层验收可定位，合成 KG、英语、小规模 episode 边界保留。 |

六段与相邻章节衔接自然，没有重复追加或将 source marker 当作语义正文。Round 7 root queue 的 6/6 可从 `pending_fresh_review` 更新为 `Applied / post-write passed`。

注意：`v3-active-evidence.json` 顶层仍保留“6 round7 root writes pending”的旧摘要，六个 item 的 Books pending 标签也尚未同步；本审计已完成写后复核，但这些结构化字段必须在下一轮定点返修时同步，不能用旧 pending 文本否定或替代本次实际审阅。

## 整日冻结未通过：bounded false-negative challenge

当前 838 = 157 retained + 490 closure + 191 isolation 的算术成立，157 个 retained 也都有 Evidence/owner/Books 状态；但算术守恒不等于候选准入正确。对 closure 做独立主题分层抽样后，确认以下项目使用了过窄的“局部 optimizer/model/benchmark 不改变长期 owner”模板，不能在 Candidate Denominator 前关闭：

1. `2605.10981` ξ-DPO：把 SimPO 的 β/γ 作用拆成 sample filtering 与 dataset reward-gap dependence，并用 ratio reward margin 重写 preference objective。它至少可能改变 `TRAIN-DPO` 的 objective/hyperparameter contract，需 exact-v1 review 后才能决定 No Change 或 Integrate。
2. `2605.11059` Uniform Scaling Limits in AdamW-Trained Transformers：给出 depth/head scaling 下 forward/backward dynamics 的统一极限与 token/embedding-dimension independence 条件，可能修正 `TRAIN-PRETRAINING` / Transformer scaling 的现有结论；仅以“局部优化增量”关闭不足。
3. `2605.11181` Muon is Not That Special：该论文直接挑战 Muon 的几何/LMO 解释，并把收益归因到 alignment、descent potential 与 step-size optimality。它属于“可能修正 Books 既有机制解释”的强制重开项。
4. `2605.11235` METIS：把 curriculum judgment 从手工规则/辅助模型迁入 policy 内部，并以 within-prompt reward variance 驱动 training allocation。它改变 curriculum sensor、allocation controller 与 optimization loop 的责任边界。
5. `2605.11290` ReAD：以 uncertainty-aware contextual bandit 分配 capability-distillation token budget，并显式处理 cross-capability spillover，改变 distillation budget 的控制状态与 failure boundary。
6. `2605.11311` Couple to Control：把独立 Gaussian seed 从默认不变量改为保持边缘分布不变的 joint noise coupling，改变多样性/一致性的生成控制接口，应在 `MULTIMODAL-GENERATIVE-PARADIGMS` 下完成证据判断。

这些项目“需要重开”并不等于一定写入 Books；它只说明 title+abstract 已达到可能改变具体 AI System 设计选择或既有机制解释的候选门槛，必须完成 exact-v1 Evidence Review、V3 score 与命题级 Books comparison 后才能关闭。

## 精确下一步

1. 保留已通过的 Round 7 六项 Books 正文，不重复写入。
2. 只重开上述 6 个 Source Family；不扩日期、不扩来源、不重新枚举 838 identity，也不触碰 191 isolation。
3. 对 6 项执行 withdrawn 检查、exact-v1 Method/Evaluation/limitations/artifact review、三维评分和 owner/adjacent Books comparison。
4. 若判定 Integrate，由 root 按 owner 串行写回；若 No Change，必须引用现有具体命题；若不足则用 family-specific closure 终结。
5. 更新 157/490、Evidence、Books 和 queue 数量后，再由未参与返修的人做最终 bounded false-positive/false-negative challenge。此前不得把 05-13 标为 Complete。
