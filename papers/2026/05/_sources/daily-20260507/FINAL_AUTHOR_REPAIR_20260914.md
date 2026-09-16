# 2026-05-07 最终作者修复交接

**角色：** 作者修复，不是 final reviewer  
**状态：** 作者侧完成；Daily 继续保持 Ongoing  
**后续 Gate：** 新的非作者语义复核（root Books 写回已完成）

## 1. 分母与状态守恒

- 原始身份：548。
- 当前分母：148 retained + 399 pre-denominator closure + 1 withdrawn = 548。
- Evidence：144 source review complete + 4 disputed + 0 pending = 148。
- Books disposition：53 Integrate + 75 No Change + 16 Daily Only + 4 Disputed = 148。
- retained-candidate 访问阻塞：0；机构来源仍有明确 coverage limitation，但不会被写成全站无遗漏。NLA 与
  2605.06548 不属于 05-07 候选，已用明确重开条件隔离，而非作为模糊 pending。

唯一 active ledger 为 `screening-ledger-v3-author-repair.json`，唯一 active packet 为
`exact-v1-review-packet-v3-author-repair.json`。旧 `*_superseded` 当前字段已提升为正式字段，避免同一候选同时出现
“暂缓”和最终处置。

## 2. 明确漏项恢复

终审指出的 8 项全部恢复为候选并完成 exact-v1 Source Review：

| family | Score V2 | Owner | Books Decision |
| --- | --- | --- | --- |
| 2605.04070 | 3+2+3=8 | `PLATFORM-EVALUATION-SYSTEM` | No Change；Ch66 已要求 confidence 只作 sensor，并以 complementarity、外部证据和 human adjudication 决定 routing |
| 2605.04083 | 3+2+3=8 | `PLATFORM-EVALUATION-SYSTEM` | No Change；Ch66 已冻结 criterion outcomes、judge/rater identity、aggregation 与 disagreement |
| 2605.04279 | 3+1+3=7 | `MODEL-MULTI-HEAD-ATTENTION` | Integrate；补 head 正交不消除 shared-token/radial-shadow 动力学耦合 |
| 2605.04569 | 3+2+2=7 | `INFER-TENSORRT-LLM` | Integrate；补 query-risk 驱动 full/Taylor sparse execution 分支与 exact fallback |
| 2605.04637 | 3+2+2=7 | `PLATFORM-EVALUATION-SYSTEM` | No Change；Ch66 已覆盖 create/modify、requirements、artifact、runtime、Ops/Security 的分阶段 evidence |
| 2605.04845 | 2+2+2=6 | `AGENT-CONTEXT` | No Change；Ch75 已保留小仓库静态 context 与大仓库动态探索的条件分支 |
| 2605.04894 | 3+2+2=7 | `INFER-SCHEDULING` | No Change；Ch56 已要求 confidence 联合可验证 observation，再由 risk/SLO controller 决定 accept/escalate |
| 2605.05187 | 2+1+2=5 | `MULTIMODAL-WORLD-MODELS` | No Change；Ch25 已拆 perceptual/temporal/physical/action-conditioned/outcome，并要求局部 failure localization |

## 3. 有界同层反查

反查只覆盖与上述误判共享高风险理由的 36 个题摘，不扩展为全库重扫：evaluation/benchmark 被一概当作领域结果、
Attention/生成机制被一概当作局部模型改进、Agent/代码系统被一概当作应用案例、routing/serving 被一概按
workload 排除。完整 ID 集已写入 active ledger 的 `final_author_repair.bounded_stratum_ids`。

反查恢复 3 项：

- 2605.04165 FlowEval：完成 exact-v1；No Change，Ch66 已拥有 reference/executable/human 三类 evidence 的责任边界。
- 2605.04291 Glauber text diffusion：完成 exact-v1；Integrate，Ch24 尚缺预训练 LM 作为能量/条件分布来定义局部
  transition 的分支。
- 2605.04677 CodeEvolve：完成 exact-v1；No Change，Ch81/Ch49 已拥有 proposal、profile evidence、typed checks、
  artifact commit 与 fallback。

其余 33 项保持关闭。关闭不是“论文没有价值”，而是题摘未给出会改变本项目长期机制/owner/contract/Books 反例的
证据。例如 JoyAI-Image 是模型发布与训练 recipe，RecGPT-Mobile 是具体移动推荐落地，CAST 是受限 VLM steering
方法，RACER 是生成式推荐的 EMB/KV workload；它们不能只因能映射 ROADMAP 就自动进入候选。

## 4. 其他修复

- 2605.04061：packet 已从“待 root 写回”同步为“root 已落实，待新 reviewer 复核”。
- 2605.04711：canonical family 改为 Books 实际 marker
  `SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR`；`SF-2026-ARXIV-2605-04711` 与
  `arxiv:2605.04711v1` 只作 aliases。
- 九项 No Change 与四项 Daily Only：active packet 的 `books_comparison` / `review_gap` 均为具体命题级理由，不再使用
  “作者侧比较完成”作为唯一说明。
- Review notes：用 `^## Review notes` 和 ROADMAP 真路径复核后，原“15 项位于首个 Review notes 后”是字符串
  误匹配；该 blocker 已在原终审记录中撤销，没有修改 Books。
- NLA / 2605.06548：见 `institution-pending-identities.json`，二者均为 05-07 安全隔离终态；只有获得不可变日期或
  exact-version material 才重开。

## 5. 仍需新 reviewer 完成

root 已处理 `FINAL_ROOT_BOOKS_QUEUE_20260914.md` 的 3 项写回，没有把本轮 No Change 项强行写入 Books。新的非作者
reviewer 仍须重新核对：548 身份守恒、11 个恢复项、36 项反查、144/4 Evidence、53/75/16/4 Books、三项新增正文
真实绑定及 NLA/2605.06548 的隔离边界。作者没有自签最终 Gate。
