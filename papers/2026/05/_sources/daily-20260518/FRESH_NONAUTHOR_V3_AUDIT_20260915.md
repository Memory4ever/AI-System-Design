# 2026-05-18 V3 fresh-context 非作者终审

- 复核角色：fresh-context non-author；未参与 V3 筛选、Evidence Review 或 Books 写回。
- 目标窗口：`[2026-05-17T09:00:00+08:00, 2026-05-18T09:00:00+08:00)`。
- 复核结论：**未通过，日报保持 Ongoing**。
- Cross-model：本轮是父任务委派的独立非作者复核；未再发起额外跨模型复核。

## 已核对且守恒的部分

1. Daily 来源清单是当前合同定义的 14 项，V3 覆盖表为 14/14。
2. `screening-ledger-v3.json` 的结构化算术成立：537 identities = 48 retained + 489 pre-denominator closures，withdrawn=0。
3. `evidence-review-v3.json` 有 48 条记录，其中 10 条标记为 current exact-v1 review，38 条标记为 identity/version/adopted-claim unchanged reuse；三维评分 Total 算术正确。
4. `books-comparison-v3.json` 有 48 条决定：19 Integrate、29 No Change；`root-books-writeback-queue-v3.json` 的 19 项与 Integrate 集合一致，19 个 source-family binding 在对应 Books 正文中可定位且位于 `## Review notes` 之前。
5. 旧 submission-window 52 项与 current 48 项的集合不相交，V3 没有重复计分；旧集合已记录回拨去向。

以上只能证明结构一致，不能证明日期、候选准入、证据复用或 Books 语义 Gate 已通过。

## 阻断问题

### 1. 09:00 截点没有被可复核证据闭合

V3 将 537 项绑定到“official arXiv 2026-05-18 announcement/listing batch”，但当前 receipt 主要使用 OAI 日级 datestamp，并以 DataCite initial-created timestamp 作交叉证据。日级 datestamp 不能证明公开发生在 09:00 前；DataCite 样本时间反而晚于截点，例如 `2605.15220` 为 `2026-05-18T01:44:18Z`（北京时间 09:44:18）。arXiv abs 页中的 v1 submission time 又是投稿来源时间，而不是本次 listing 的公开时刻。

因此现有 artifact 不能在不作推断的情况下证明这 537 项全部属于目标半开区间。需要补充能够锚定 announcement batch 在 09:00 前公开的 authoritative evidence；若只能证明日期而不能证明时刻，应隔离为 owner-time uncertain，不能签 Complete。

### 2. denominator 关闭理由引入了合同外的“跨 workload”门槛，造成系统性 false negative

489 项的大量关闭理由要求候选改变“跨 workload 的 state/data/control ownership”，但当前合同允许单一 workload 的机制证据进入候选，只要它会改变一个具体 AI System 设计选择。bounded challenge 已确认以下至少 7 项不能在 denominator 前关闭，必须重开并完成 exact-v1 Evidence Review 与 Books Decision：

- `2605.15220` OP-Mix：把 data mixing 从分阶段静态选择改为贯穿 pretraining、continual midtraining 与 instruction tuning 的在线决策，直接涉及 `TRAIN-DATA` / `TRAIN-PRETRAINING`。
- `2605.15250` GQLA：同一权重暴露 MQA-absorb 与 GQA 两条等价执行路径，运行时按硬件选择，直接改变 KV、TP 与 execution-plan 边界。
- `2605.15290` GQA-μP：给出 GQA 的参数化与 learning-rate/weight-decay transfer 边界，直接影响训练超参数迁移。
- `2605.15484` sparse vision MoE：给出 compute leverage、top-k 与 batch-axis dispatch 的符号反转/失败边界，改变 MoE 适用条件。
- `2605.15492` FLASH：以连续多项式 action trajectory 和 single-step flow 改变 VLA action representation、控制频率与推理延迟的权衡。
- `2605.16165` ML-FOP-SOAP：针对跨模态梯度异质性改变 optimizer state 与大 batch scaling 设计边界。
- `2605.16241` VLA-AD：把语义 teacher 限定在离线训练侧、让轻量 student 独立闭环运行，改变训练/部署 state ownership 与控制频率。

进一步抽样中，`2605.15239`、`2605.15224`、`2605.15300`、`2605.15491`、`2605.16233`、`2605.16143`、`2605.15309`、`2605.15458`、`2605.15217`、`2605.15248`、`2605.15298` 也具有重开信号。修复不能只定点增加上述 7 项；应先删除合同外的 cross-workload 关闭前提，再对受该模板影响的 closure cohort 做一次 bounded false-negative replay，并逐项保留具体关闭理由。

### 3. retained 集合存在明确 false positive / 评分膨胀

- `2605.15638` ITHICA 是通用 CPU silent-data-corruption 检测机制，当前材料没有证明其改变 AI model/training/inference/platform 的专属机制；把它以 9 分 Integrate 到 `PLATFORM-MONITORING` 主要是解释类比，不满足项目贡献门槛。应移出候选，回滚/移除仅由该 family 导致的 Books 增量，或补出它与 AI workload 的直接设计改变证据。
- `2605.15734` 的单领域 user-state psychometric study 与 `2605.16194` 的论文 JSON 协调约定均被评为 8 分。二者可以作为受限案例，但现有记录没有证明其 System Reach 与 Design Delta 达到该分值；需重新评分并决定 pre-denominator closure、Weekly Only 或保留。

### 4. 38 项 Evidence reuse 只有布尔声明，尚不足以独立证明复用 Gate

V3 为 38 项写了 `identity_unchanged=true`、`exact_version_unchanged=true`、`adopted_claim_unchanged=true`，但当前 artifact 没有逐项给出“原 evidence locator/hash → 当前 exact-v1 locator/hash → 采用命题”的可重放比较。布尔值不能替代复核证据。至少需要：

1. 指向原已完成 Source Review 的精确 artifact/claim locator；
2. 证明复用的是同一 exact version，而不是后来 revision 或不同 owner-day 的正文；
3. 证明采用命题和 evaluation boundary 未变化；
4. 重新检查 withdrawn/correction signal。

若无法逐项证明，必须按 current exact-v1 重开；不能以“曾读过”签署 48/48。

### 5. Books 集合在 denominator 修复前不能终验

当前 19 个 binding 的存在性和 placement 已通过结构检查，但候选集合已被证明存在漏选和误选，所以 19 Integrate / 29 No Change 不是稳定终态。先完成候选修复，再对新增/移除 family 做命题级 owner/adjacent comparison；已经存在且语义正确的正文禁止重复追加。尤其 `2605.15638` 的 Books 段落需随准入结论一并重审。

## 精确返修顺序

1. 补齐或隔离 537 项的 09:00 owner-time evidence；未闭合前不得宣称本日 owner denominator 已冻结。
2. 删除 screening reason 中合同外的 cross-workload 必要条件，重开上述 7 项，并对受同一模板影响的 closure cohort 做 bounded replay。
3. 重审 ITHICA、user-state psychometrics 与 `paper.json` 三个 false-positive/评分样本；同步修正 denominator、Evidence、Books decision 与正文。
4. 为 38 个 reuse family 建立可重放的原审阅 locator/version/claim 对照；否则改为 current exact-v1 review。
5. 重新冻结候选后，重算 48/489、Evidence、Integrate/No Change 和 owner reconciliation；不得机械维持旧数字。
6. 由另一位未参与返修的人再次做 false-positive/false-negative challenge 和 post-write semantic audit。只有日期、准入、Evidence、Books 四个 Gate 同时通过，README 才能改为 Complete。

