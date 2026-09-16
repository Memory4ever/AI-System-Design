# 2026-05-11 V3 fresh-context 非作者 post-write 终审

## 结论

**FAIL — Daily 必须保持 `Ongoing`。**

本轮未重放来源、扩展窗口或修改 Books，只复核当前 V3 denominator、Evidence Review、Books queue、最新作者返修与 root 写回记录，以及 20 个 `Integrate` 的当前 Books 主体。20 个既有写回本身通过语义复核；阻断项来自仍未冻结的 candidate denominator、ordinary-revision 负面断言的证据不足，以及结构化处置名与 Report 合同不一致。

## 审阅身份与范围

- 审阅者：`/root/may11_fresh_postwrite_final`；未参与本轮作者返修或 root Books 写回。
- 窗口：`2026-05-10T09:00:00+08:00` ～ `2026-05-11T09:00:00+08:00`，左闭右开。
- 输入：当前 `V3_SCREENING_LEDGER_20260914.json`、`V3_EVIDENCE_REVIEWS_20260914.json`、`V3_BOOKS_WRITEBACK_QUEUE_20260914.json`、`V3_BOUNDED_REPAIR_BOOKS_COMPARISON_20260915.json`、最新作者/root 记录、Daily 与 20 个 owner 正文。
- 禁止项：未重新枚举 arXiv，未读取窗外事件，未把 marker 或 validator 当作语义证明，未编辑 Books。
- Cross-model skipped：这是主任务委派的非交互式 fresh-context 审阅，不另行调用外部 CLI。

## 已通过的部分

### 当前结构化算术

- `826 = 635 official-announcement direct + 191 ordinary-revision recovery`。
- 当前文件内部 `635 = 60 retained + 575 pre-denominator closure`。
- `60 = 20 Integrate + 38 No Change + 2 report-only/context`；60 个 Source Family 与 arXiv identity 均唯一。
- 60 项三维分数均为 0–3，Total 等于三项之和；所有 Total ≥ 7 和所有 Integrate 均为 deep review。

这些等式只证明当前账本自洽；下面的 false negative 会改变真实 denominator，不能据此签署 Complete。

### exact-v1、日期与 Evidence locator

- 60 个 retained item 均绑定 `2605.xxxxxv1` 的 official exact-v1 HTML 或 PDF，`public_event` 均记录为 `2026-05-11T08:00:00+08:00 scheduled arXiv announcement`，完全落在本窗。
- 60 项均有 Method、Evaluation 与 Limitations/non-proof locator；前轮点名的 `2605.06733`、`2605.07568`、`2605.07881` 已按实际章节结构修正。
- 当前 V3 retained ledger 没有正向 withdrawal signal；本轮依任务边界没有重放 live source，因此这里只复核当前 exact-v1 记录的一致性，不把它扩大为新的实时状态证明。

### 20 个 Books 写回

- 20/20 owner/path 与 `ROADMAP.md` 一致，20 个 Source Family 的 marker 均只存在于唯一 owner 文件，并全部位于该文件 `## Review notes` 之前。新增五项使用成对 `start/end` range marker，其余使用单 marker；这只是定位形式，不计作两次知识写入。
- 前次独立复核已经通过且本轮未被返修改变的 15 项可以复用；本轮重新对读新增五项 `2605.06919`、`2605.07686`、`2605.07701`、`2605.07769`、`2605.07937` 的正文与相邻论证。
- 五项分别落在 RAG evidence authority、reasoning/output budget、diffusion guidance state、Agent no-op/partial-fix evaluation、clarification timing 的现有主线内；均写出旧方案成立条件、约束变化、state/control owner、trade-off、failure/fallback 与 exact-v1 证据边界，不是论文摘要堆叠。
- 因此当前 20 个 Books prose 不需要回滚；denominator 修复产生的新 Integrate 才需要进入新的 root queue。

### retained false-positive 挑战

对 20 个 Integrate 全量对读，并复用前轮对 12 个跨 owner/disposition retained family 的反向挑战；本轮未发现需要从 60 个 retained 中移除的明确 false positive。该结论不外推为对所有 575 个 closure 的正确性证明。

## 阻断 Complete 的问题

### P0：575 个 closure 中仍有 14 个明确 false negative

下列 family 的当前完整摘要已经直接给出可定位的机制、状态所有权变化或 evaluation contract；统一的“未找到长期增量”理由与摘要内容相矛盾。这里要求恢复为候选并审证，不预判最终必须 Integrate：

| arXiv | 摘要已明确给出的候选增量 |
| --- | --- |
| `2605.06672` | 长 CoT 累积 position bias，并用截断干预区分 direct-answer bias，直接改变 reasoning evaluation 的顺序鲁棒性与长度切片。 |
| `2605.06708` | 将 visual-text compression 的信息损失分解为 precision/coverage transport cost，并据此路由与 foveation，改变多模态压缩的 admission contract。 |
| `2605.06865` | 为 closed LLM 提供带统计检验的 dataset watermark，改变训练数据 provenance 与 benchmark contamination 的可验证边界。 |
| `2605.06892` | 按时空 token 动态分配 diffusion step，并显式处理 active/inactive token 的 KV 同步和 cached Euler state，改变生成 inference scheduling。 |
| `2605.07114` | 在固定 group advantage estimator 下按 posterior hit utility 重分配 RLVR rollout，改变训练采样预算的 owner 与饱和回退。 |
| `2605.07134` | 把 Web Agent observation 从 element 粒度改为持久 functional-region digest，改变 observation state 与 action space 的接口。 |
| `2605.07164` | 将经验从固定注入改为 runtime 可选择资源，并有 causal ablation，改变 Agent memory/experience 的读取控制。 |
| `2605.07182` | 一次 post-training 产生嵌套 reasoning submodels，并按 thinking/answer phase 动态选择计算，改变 elastic model identity 与 inference budget control。 |
| `2605.07234` | 将 KV eviction 从局部 attention-weight heuristic 改写为 output-aware、layer-wise、跨 head 可比的全局近似问题。 |
| `2605.07238` | LLM workflow scheduler 同时计入 model residency、parent-output locality、prefix reuse 与 future reachability，直接改变 DAG future-state owner。 |
| `2605.07242` | 对 derived Agent memory 定义 barrier-first cascade repair、withdraw-before-repair 与 predecessor-closed republish，改变删除/纠错传播合同。 |
| `2605.07260` | 以 equal-compute counterfactual routes 发现 fragile token 的 MoE misrouting，并用 router-only update 区分 route failure 与 expert capacity。 |
| `2605.07313` | 在固定证据、递增无关 session 下测 usable-scale boundary、tail call burden 与 budget-compliant reliability，改变 memory scalability claim。 |
| `2605.07414` | 证明 individually benign tool steps 可经 orchestration 组合成 harmful T2I output，新增 prompt-only 防线覆盖不到的 Agent attack surface。 |

这 14 项都来自现有 ledger，不需要扩窗、扩源或重扫 575 项。修复范围只包括它们及其因恢复而改变的计数、Evidence、Books comparison 与 Daily。

### P0b：191 个 ordinary-revision recovery 的负面断言不可由当前 V3 包独立复核

191 项全部只记录同一 `datacite_initial_created_owner_proxy` route、同一句“没有 important-revision signal”，以及 `none_in_owner_receipt; retained exact-v1 checked separately`。当前条目没有本次 revision event 的 version/date/comment 或 official version-history locator，且后一句对已排除项使用“retained exact-v1”本身不成立。因此当前材料只能支持“这些 recovery hit 不拥有本日首次公开”，不能支持 README 的“191 ordinary revisions 无 important-revision signal”全量断言。

有界修复可二选一：补入每项可复查的 official version/event/comment basis；或把 191 项明确降为不拥有窗口的 discovery noise，删除未经证明的 important-revision/withdrawal 全量断言。若其中确有落窗的重要修订，再只重开对应 family。

### P1：两项处置名仍使用非合同枚举

`2605.06755` 与 `2605.06997` 在 Evidence JSON 中写 `Weekly Only — Context`，README 又写“仅报告”。当前 Report 合同没有 `Weekly Only` Books disposition；应统一为合同内的“仅报告”，并说明为何不改变长期知识。这个字段问题不推翻两项现有证据，但必须随下一轮重算一起消除。

## 最小有界返修与再次验收

1. 只恢复上述 14 个 Source Family；逐项完成 exact-v1、公开事件与 withdrawal check、Score V2、相应深度 Evidence Review、Stable Node/相邻正文比较和最终 Books disposition。
2. 对 191 个 ordinary-revision recovery 按 P0b 补可复查依据或收窄断言；不要因此重跑 635 个 official direct family。
3. 将两项 `Weekly Only — Context` 统一为合同内“仅报告”，重算 ledger、evidence、queue 与 README 的 denominator/disposition/state。
4. 仅新产生的 Integrate 进入 root 串行 Books 写回；本轮已通过的 20 项保持不动，除非新证据直接推翻其 adopted claim。
5. 返修与必要写回后，由另一位未参与返修/写回的 reviewer 再做一次 fresh-context 终审；validator 与 marker 检查只作为辅助。

## 机器检查

- 当前报告 validator 通过。
- 当前 60 项分数、review depth、Evidence locator、identity 唯一性和内部算术检查通过。
- 20 个 Books owner/path、marker 位置与 scoped `git diff --check` 通过。
- 上述结果不补偿 denominator 与 revision-evidence 的语义失败。

## 文件影响

- 新增本终审记录并更新 Daily 的结论、arXiv coverage 缺口、下一步与复核结论。
- 未修改 Books，未 stage、commit 或 push。
