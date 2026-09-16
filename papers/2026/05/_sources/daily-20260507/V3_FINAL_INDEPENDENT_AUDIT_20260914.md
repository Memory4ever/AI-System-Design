# 2026-05-07 V3 非作者终审

## 判定

- Reviewer：`fresh-context:may07_final_reviewer:2026-09-14`
- 角色：未参与本日筛选、证据摘录、Books disposition 或 Books 正文写作的独立复核者。
- 结论：**未通过**。Daily 必须保持 `进行中`。
- Cross-model review：Skipped。本轮是已授权的独立智能体复核，没有额外外部模型调用授权。

机械校验通过不改变上述判定。阻塞原因不是普通材料暂时不可访问，而是当前仍有可执行的来源闭合、候选分母修复和活动记录同步工作。

## 复核范围

本轮重新读取当前合同、来源清单、统一 Prompt、ROADMAP、本日 README，以及 active screening ledger、active exact-v1 packet、机构窗口复查、作者整改、Books 重裁和 root 写回记录。没有相信作者或旧 reviewer 的完成声明。

实际检查包括：

- 548 个 arXiv identity 的唯一性、状态计数、撤回排除和日期路线；
- 137 个 retained 的 V3 三维评分算术、Evidence/Books 状态与审阅字段完整性；
- 410 个 closure 的标题全量可判定检查，并针对通用关闭理由、Evaluation、Attention/Inference、World Model 与 Agent 高风险层读取完整题摘；
- 50 个 `Integrate` 的 Books 实际命题绑定、marker/identity、owner 与正文位置；
- 67 个 `No Change`、16 个 `Daily Only`、4 个 `Disputed` 的最终理由与记录一致性；
- Ch14、Ch17、Ch66 的新增正文与相邻 handoff；
- Report validator、JSON 解析、候选表、链接、marker、Markdown 围栏和 scoped `git diff --check`。

## 已通过的部分

1. **时间与身份基线可复用。** 窗口正确为 `[2026-05-06T09:00:00+08:00, 2026-05-07T09:00:00+08:00)`。548 个 arXiv identity 唯一，状态计数为 `137 retained + 410 closure + 1 withdrawn`。`2605.04356` 只保留撤回身份、官方链接和排除理由，没有进入候选、评分或 Books。
2. **评分机械一致。** 137 个 retained 均存在三个 `0～3` 维度，Total 与三项和一致；报告候选表的评分算术也一致。该结果只证明评分字段可判定，不证明准入或分值语义正确。
3. **Evidence 记录可判定。** active packet 含 137 个唯一 identity，133 项记录 Method / Evaluation / Limitation，4 项 Disputed 都有精确重开条件；未发现把四项争议写入 Books 的情况。
4. **四项争议处理合格。** `2605.04069`、`2605.04243`、`2605.04295`、`2605.05029` 均明确了不采用的中心主张、当前证据冲突和具体重开条件。
5. **Ch14 新增命题本身成立于受限范围。** `2605.04061` 已真实写入 Ch14 主叙事，区分“线性可解码”与“必要/充分的因果控制”，并保留小模型、受控 ICL、样本量与 intervention OOD 风险。Ch14 将多层组合交给 Ch17、将 probe/干预/行为验证合同交给 Ch66，owner 与 handoff 没有越界。
6. **本地链接与格式。** README 的本地 Markdown 目标均存在；JSON 均可解析；代码围栏平衡；validator 和范围内 `git diff --check` 通过。

## 阻塞发现

### 1. 候选分母存在系统性 false negative

当前 closure 仍大量沿用“没有跨 workload ownership 变化”或“只是 benchmark / 局部方法”作为硬关闭门槛。这与研究合同要求的两条准入入口冲突：一篇材料只要提供可迁移的长期机制、评价合同、关键反例或会改变已有设计判断，就可以准入；它不必先改变跨 workload 的 state owner。

完整题摘已经足以确认下列八项不能维持当前 closure：

| arXiv | 当前误关原因 | 需要重开的具体贡献 |
| --- | --- | --- |
| `2605.04070` | 当作普通领域 benchmark | 人机互补实验直接反证 confidence routing 能识别 AI 错误的假设，改变 human-oversight routing 与 evaluation contract。 |
| `2605.04083` | 当作普通 semantic-eval benchmark | 把专家要求写成稳定 criteria/aggregation contract，并跨 model-only 与 agentic evaluation 复用审计 artifact；这是 Evaluation / post-training 的接口变化。 |
| `2605.04279` | 以“不改变跨 workload owner”关闭 | 多头 Attention 的 radial-shadow obstruction、单调性条件、近似正交鲁棒性和临界温度是模型机制边界，至少应进入标准 Source Review。 |
| `2605.04569` | 当作视频编辑局部性能结果 | context-token saliency、query sharpness/error 关系和 full/Taylor sparse 动态路由形成 Attention/执行的条件分支，不能只因 workload 是视频编辑而关闭。 |
| `2605.04637` | 当作 coding benchmark | 把 Agent 平台评价扩展到创建/修改、PM/Engineering/Ops、复杂度和 production readiness，并披露结构性失败模式；会改变 Agent Platform 的评价切片。 |
| `2605.04845` | 当作 repository-mining 局部任务 | 直接比较 agent 自主取 context 与预工程 context，暴露 context overflow 和 ground-truth ambiguity，改变 Agent Context/RAG 的评价边界。 |
| `2605.04894` | 当作 code-completion 领域结果 | 以 confidence + syntax validity 做逐请求 local/large-model routing，同时改变隐私、accelerator 使用和 correctness；是明确的 inference routing 机制。 |
| `2605.05187` | 当作 World Model benchmark | 把感知质量、物理真实性、条件一致性、时间一致性和异常时间定位拆成评价合同；直接补充 World Model / Evaluation 的 failure localization。 |

这不是“只补八篇”即可结束。作者应定点重开与上述错误共享理由的层级：

- `domain_dataset_or_benchmark_without_a_durable_evaluation_contract_delta` 的 10 项；
- `generic-cross-workload-gate` 的 87 项中与 Attention/Inference、Evaluation、World Model、Agent/Workflow 相关的题摘；
- `author-specific-boundary` 中使用相同跨 workload 硬门槛的相关记录。

不要求重读全部 410 项全文。先用完整题目和摘要重新判断贡献；只有准入项才按分数和触发条件进入相应 Source Review。修复前，137 不是有效冻结分母。

### 2. 来源覆盖尚未处理到安全终态

README 的来源表仍把 OpenAI、Google、Qwen、Moonshot、MiMo、arXiv 标为 `未完成`，把 Anthropic、Meta、Hunyuan、Z.ai、Seed 标为 `受阻`；`INSTITUTION_WINDOW_RECHECK.md` 也多处写明“未闭合”。与此同时 §5 又写 `0 access blocker`，并把剩余工作缩减为等待 reviewer，前后冲突。

外部材料不可得可以成为安全终态，但必须逐项说明：已穷尽的入口、不能支持什么断言、是否存在已知 positive identity、精确重开条件。当前至少两条 positive pending identity 仍需正式隔离或定点恢复：

- Anthropic `Natural Language Autoencoders`：日期跨 09:00 截点且正文读取受限；
- Seed / arXiv `2605.06548`：机构目录日期和 exact-v1 首次公开证据冲突。

作者须选择其一：继续定点恢复；或按 Report 合同把每项写成不会支撑候选、Books 或“无遗漏”断言的终态保留项。不能保留 `未完成/受阻`，同时声明只剩最终 reviewer。

### 3. active ledger 不是当前最终状态

README 声称 `screening-ledger-v3-author-repair.json` 是唯一 active ledger，但其当前字段仍是旧状态：

- 137 项 `review_status` 虽已更新为 133 complete / 4 disputed；
- `integration_disposition` 仍为 100 `暂缓`、24 `整合`、9 `已有覆盖`、4 `仅报告`；
- 与 active packet 的最终 Books disposition 有 **100 项不一致**；
- 多数新结果被写入名为 `integration_disposition_superseded` 的字段，语义方向相反，且仍不能覆盖全部当前结果。

必须把活动字段本身更新为当前最终 disposition，并把旧值放入明确的 history 字段或删除非必要投影。不能要求读者猜测 `superseded` 其实代表新值。

### 4. active evidence packet 与 README 不同步

- `2605.04061` 的 packet 仍写“待 root 写回”，但 Ch14 和 README 已写回完成。
- 九项 `No Change` 在 packet 中仍只有“无；作者侧证据与 Books 比较完成”，缺少合同要求的命题级覆盖：`2605.04808`、`2605.04897`、`2605.04920`、`2605.04972`、`2605.04995`、`2605.05003`、`2605.05058`、`2605.05185`、`2605.05191`。README 已存在较具体说明，应同步到 active packet。
- 四项 `Daily Only` 仍只有同一泛化句：`2605.05026`、`2605.05103`、`2605.05115`、`2605.05134`。README/实际题摘已经能说明为何其受限结果不能改变长期 owner，应同步具体边界。
- `2605.04711` 在 README/packet 声称正文 marker 为 `SF-2026-ARXIV-2605-04711`，实际 Ch28 使用 `SF-BUDGET-AWARE-AUTO-OPTIMIZER-CONFIGURATOR`。正文语义真实存在，但 identity 声明错误，必须统一为实际 canonical family 或增加无歧义 alias。

### 5. 50 项 Integrate 有真实正文；“15 项位于 Review notes 后”已撤销

本轮逐项以采用命题对读 owner 正文。当前 50 项都能找到实际机制段，不是只留下 marker；`2605.04711` 也是 marker 名称不一致而非正文缺失。Ch14/Ch17/Ch66 的新写回均保留了证据范围和相邻 owner 边界。

后续 root 用锚定标题 `^## Review notes` 与行号重新核查，发现本 reviewer 的原检查把机制正文中出现的普通字符串 `Review notes` 误当作标题。Ch33 的真实路径也应由 ROADMAP 解析为 `books/part-04-training-system/33-grpo.md`，不是猜测路径。Ch33、Ch66、Ch67、Ch72、Ch82 均只有一个真实章末标题；以下 15 项机制行全部位于该标题之前：

- `2605.04077`、`2605.04960`、`2605.05112` → Ch33；
- `2605.04116`、`2605.04209`、`2605.04446`、`2605.04572`、`2605.04901`、`2605.04992` → Ch72；
- `2605.04135`、`2605.04624`、`2605.04665`、`2605.05090` → Ch66；
- `2605.04213` → Ch67；
- `2605.05007` → Ch82。

因此该结构 blocker 是检查器 false positive，现明确撤销；不得据此移动、删除或重写 Books，也不生成无意义迁移队列。其余分母、来源和 disposition 问题不受这一纠正影响。

## 精确修复清单

### 作者 / Daily owner

1. 重开上述八项，并对共享错误关闭理由的相关层级执行题摘 false-negative 复查；更新分母、评分、Source Review 和 Books disposition。
2. 将所有到期来源处理到 `已检查` 或具精确重开条件的安全终态；把 NLA 与 `2605.06548` 作为唯一 family 定点恢复或隔离。
3. 使 active ledger 的当前字段与 README/active packet 一致；不要把新结果继续放进 `*_superseded`。
4. 同步 `2605.04061`、九项 No Change、四项 Daily Only 与 `2605.04711` canonical family identity。
5. 分母变化后重算 README 的候选、Evidence 与 Books 数量；不要沿用现在的 `137/133/50/67/16/4`。

### root / Books owner

6. 不处理已经撤销的 Review-notes 误报；只执行作者修复后真正产生的命题级 Books 写回队列。
7. 写回后重新核对 owner、相邻 handoff 与全部 `Integrate` 的实际语义绑定。

### 新的非作者 reviewer

8. 复核修后的 affected closure strata、最终 denominator、来源终态、active ledger/packet/README 一致性，以及改动后的 Books 结构与语义。当前 reviewer 不应自行作者化修复后再为自己签字。

## 校验结果

| 检查 | 结果 |
| --- | --- |
| `scripts/validate_research.py --report papers/2026/05/07/README.md` | Pass；仅格式/可判定一致性 |
| JSON 解析与 548 identity 唯一性 | Pass |
| 137 个 V3 评分范围与 Total | Pass |
| README 候选表、active packet identity | Pass，均为 137；其中 `2605.04530` 使用 PDF 链接 |
| 本地 Markdown 链接 | Pass |
| 50 Integrate 真实机制段 | 50/50 找到；15 项结构位置失败，1 项 canonical marker 不一致 |
| 67 No Change | README 有命题级说明；active packet 9 项不完整 |
| 16 Daily Only | 12 项理由明确；active packet 4 项不完整 |
| 4 Disputed | Pass，均有精确重开条件 |
| `git diff --check`（本日报、active source 与重点 Books 范围） | Pass |
| stage / commit / push | 未执行 |

## 最终结论

当前日报的 Evidence 摘录和 Books 语义写回有大量可复用成果，尤其 50 项 Integrate 不是空 marker；但候选分母仍漏掉至少八项明确符合贡献合同的材料，来源状态与“只剩复核”声明冲突，唯一 active ledger 又与最终处置相差 100 项。以上均是可执行工作，因此不能将本日报标为完成。
