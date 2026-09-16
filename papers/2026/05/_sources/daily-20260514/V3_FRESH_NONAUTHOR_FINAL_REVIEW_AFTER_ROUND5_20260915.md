# 2026-05-14 V3 Fresh Non-author Final Review after Round5

**复核者：** `/root/may14_round5_fresh_final`  
**身份：** fresh non-author；未参与 Round5 作者返修与 root Books 写回  
**结论：** **未通过；Daily 保持 Ongoing**  
**边界：** 不扩窗口、不重做全量研究、不编辑 Books。Cross-model skipped: non-interactive subagent context.

## 1. 已通过的部分

- 时间窗保持 `[2026-05-13T09:00:00+08:00, 2026-05-14T09:00:00+08:00)`；13 个非 arXiv Daily source 与 `SRC-ARXIV` 共 14 个来源均有终态记录，非 arXiv unresolved=0。
- active owner inventory 与当前筛选集合逐 ID 相等且均为 714 个唯一 identity；当前算术为 `714 = 124 retained + 590 pre-denominator closure + 0 withdrawn`，另有 2 个官方候选，因此报告所写 Candidate Denominator=126 在算术上成立。
- Round5 六项 `2605.12863 / 12879 / 12913 / 13228 / 13316 / 13821` 都有 exact-v1 fetch 状态、非 withdrawal 结论、三维评分、非模板化 Method/Evaluation/limitation 边界与 Stable Node owner。五项 Integrate 的评分分别为 9/8/9/7/8；`2605.13821` 为 9 分 concrete No Change。
- 本轮五个 Books binding 在各自 owner 中恰好出现一次，均位于首个 canonical `Review notes` 之前。正文真实承载 baseline、changed constraint、mechanism/state/control、trade-off/failure、fallback 与 evaluation boundary，而不是只有 source marker。
- `2605.13821` 的 No Change 有具体命题依据：Ch84 已明确承载 model/harness 配对 artifact、外部 controller、evaluator/holdout 隔离、budget、success-preserving intervention、release owner、rollback 与 static-workflow fallback。
- 旧 78 项 root writeback queue 仍为 78 个唯一 Source Family；78/78 均能在声明的 owner 中唯一定位，且位于 Review notes 前。Round5 五项写回没有破坏旧队列、owner 或正文位置。
- Report validator 与本轮 scoped `git diff --check` 通过。工具结果只证明格式，不替代以下语义反证。

## 2. 未通过：Candidate Denominator 仍未冻结

对 590 个关闭项执行了一个不扩窗的有界 challenge：抽取 10 个 training / representation / agent / evaluation 高风险近边界项与 11 个明显低风险对照项，并对 4 个 standard candidate 与一组现有 deep candidate 做 false-positive 对照。低风险领域应用样本可以继续关闭，但高风险样本暴露出两类可复现问题。

第一，`screening-outcomes-v3.json` 的多条关闭理由被机械截断为 240 个字符，只留下标题和摘要中的“具体机制”，没有写出为什么该机制不改变本项目的长期 owner、state/data/control ownership、evaluation contract 或现有结论。例如 `2605.12652`、`2605.12667`、`2605.12714`、`2605.12718`、`2605.12729`、`2605.12741` 的 reason 都在机制描述中途截断。即使其中某项最终仍应关闭，这种记录也不满足 family-specific pre-denominator closure。

第二，以下题名与完整摘要已经给出不能继续直接关闭的具体贡献信号：

| arXiv | 需要重开的原因 | 最低后续动作 |
| --- | --- | --- |
| `2605.12652` | peer-conditioned multi-rollout OPD 同时使用成功/失败 rollout 改写 teacher signal，明确涉及 rollout-group state、teacher supervision 与 verifier feedback 的责任边界 | exact-v1 标准/深入审阅，重新判断 `TRAIN-SFT` 或 `TRAIN-GRPO` |
| `2605.12667` | 将有噪多级 auto-rater reward 分解为 ordinal binary thresholds，直接改变 GRPO/MaxRL advantage estimator 的噪声传播 contract | exact-v1 深入审阅，重新判断 `TRAIN-GRPO` / `TRAIN-RLHF` |
| `2605.12741` | rare-success on-policy distillation 把失败 trace 变为局部 reflection 与持久 playbook，再生成 token-level supervision，改变 feedback→training-data 控制流 | exact-v1 深入审阅，重新判断 `TRAIN-SFT`、`TRAIN-GRPO` 与 `AGENT-MEMORY` 的 canonical owner |
| `2605.12714` | layer-wise measurement 同时被用于 label-free model selection 与 inference-time layer pruning；当前截断理由没有说明为何它只是局部指标而非 evaluation/execution contract 增量 | 重读完整摘要并给出可审计准入结论；若保留则 exact-v1 审阅 |
| `2605.12718` | graph-structured belief state、可配置 adjudication policy 与可审计 belief artifact 可能改变 multi-agent state/evaluation contract；当前理由没有完成排除 | 重读完整摘要并给出可审计准入结论；若保留则 exact-v1 审阅 |
| `2605.12908` | weak-to-strong generalization 的 feature-elicitation 机制可能修正 Books 对 latent knowledge / reward-model learning 的既有解释；现有理由只写“特定模型/数据/目标”而未比较具体命题 | 重读完整摘要并对读 `WORLDVIEW-REPRESENTATION` / post-training owner 后裁决 |

这六项不是预先判定必须进入 Books，但在完成上述裁决前，`590 closure` 与 `124 retained` 不能作为最终冻结分母。发现这些问题后本轮按 bounded stop condition 停止，没有继续滚动抽样或扩成第六次全量重审。

## 3. 未通过：一个 false-positive 与最终状态不一致

- `2605.13695` 当前作为 6 分 standard candidate 保留，但证据只支持单一 judge、单一 prompt recipe、单一 350-item benchmark，且成本约为 vanilla judge 的 47 倍，关键增益组件没有分离。它更像受限 prompting result，而非新的长期 evaluation contract。作者应重新执行贡献准入：若不能提出超出现有 self-consistency / critique / LLM-as-judge 边界的具体 delta，则降为 pre-denominator closure，不继续用 `No Change` 掩盖 admission false positive。
- Round5 五项已经实际写入 Books，但终审开始时，Daily 候选表、`exact-v1-source-reviews-bounded.json` 与 `books-comparison-bounded.json` 仍写 `Root Writeback Pending`。本复核已把这五处客观状态同步为 Applied；`books-comparison-bounded.json` 当前汇总为 83 Applied + 0 Pending + 41 No Change。
- `v3-author-recert.json`（79 candidate）与 `v3-bounded-semantic-repair.json`（120 candidate）是早期 checkpoint，不是当前 126 denominator。最终返修应在一个当前 reconciliation artifact 中明确标记二者 superseded，避免未来校验把旧数字当成并行总账。

## 4. 精确 Repair List

1. 只重开 `2605.12652 / 12667 / 12741 / 12714 / 12718 / 12908` 六项；先完成完整题摘准入，前三项至少进入 exact-v1 Evidence Review，后三项依准入结果决定，不扩展到其他日期或全站重扫。
2. 重新裁决 `2605.13695` 的 candidate admission；没有可定位的长期 design/evaluation delta 就降级，并同步分母、评分和报告正文。
3. 对上述改判更新 `screening-outcomes-v3.json`、exact-v1 evidence、Books comparison、README 候选表与守恒式；所有 closure 必须给出完整、非截断、family-specific 理由。
4. 新增或更新唯一的当前 reconciliation artifact，登记最终 raw/retained/closure/withdrawn、官方候选、Evidence、Applied/No Change，并显式把 79 与 120 两个旧 checkpoint 标成 superseded。
5. 如产生新的 Integrate，仍由 root 顺序写 Books；然后交给另一 fresh non-author reviewer 做一次针对这 7 项与总账的有界终审。不要再次重扫 714 项。

## 5. Gate

| Gate | 结论 | 说明 |
| --- | --- | --- |
| Source / Window | Pass | 14/14 到期 Daily sources 有记录，窗口未扩张 |
| Inventory identity | Pass | owner receipt 与 screening outcome 为同一 714-ID 集合 |
| Candidate Denominator | **Fail** | 有界抽查发现 6 个关闭项需重开，且关闭理由存在 240-char 截断 |
| Evidence | Partial | Round5 六项通过；新重开项尚未完成 |
| Books | Partial | 既有 78 + Round5 5 项实际写回通过；新重开项尚无最终 Books Decision |
| Independent Review | **Fail** | 本轮发现可执行的实质问题，不能签署 Complete |

**Final Status：Ongoing — Round5 evidence and five Books writebacks pass, but denominator repair for six closures plus one retained false-positive challenge remains.**
