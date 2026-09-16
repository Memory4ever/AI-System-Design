# 2026-05-05 V3 独立最终复核

**复核者：** `fresh-context:may05_independent_gate`

**复核时间：** 2026-09-14T20:51:13+08:00

**结论：** 未通过；Daily 保持进行中。

本记录只裁决 2026-05-05，不把作者侧 `Complete`、旧审计标签或机器校验当作完成证据。

## 已通过的部分

- 时间窗口为 2026-05-04 09:00～2026-05-05 09:00（Asia/Shanghai）。arXiv owner receipt 有 1058 个唯一身份，ID 范围为 `2605.00826～2605.02892`，与 canonical ledger 的 1058 行守恒；旧审计中 `.030xx/.052xx/.066xx` 等条目不属于本日 owner batch。
- 13 个机构来源均有本次终态：Anthropic、Meta、DeepSeek、Hunyuan、ZAI、ByteDance Seed、Baidu、MiniMax 共 8 个有可复查历史边界；OpenAI、Google AI、Qwen、Moonshot、Xiaomi MiMo 共 5 个被隔离为历史目录缺口。后 5 项不支持零遗漏断言，但按合同不要求日报永久等待外部快照。
- 当前 101 个候选的三维分数算术全部正确：`5=68`、`6=13`、`7=7`、`8=13`；没有 9 分。高分项没有发现仅因标题相关或映射章节而抬分的共同模式。
- 99 个可访问候选的 method、evaluation、limitations 与 claim-boundary 内容均非复制模板；`2605.02206`、`2605.02375` 两项正文缺失已被隔离，不用于正面证据或 Books。
- 当前 18 个 `Integrate Applied` 的 source-family marker 都只出现一次；逐项回读显示正文写入了机制、适用边界与代价，而不是只有 trace 或“已吸收”标签。
- 对 exact-v1 HTML 与当前标题做了身份复核，并在本次 owned 文件中修正 7 个实质标题漂移：`2605.01298`、`2605.01342`、`2605.01790`、`2605.02028`、`2605.02124`、`2605.02187`、`2605.02395`。纯标点、空格或副标题差异没有制造新 family。

## 阻断完成的发现

### 1. 候选分母发生已证实的回退

当前 canonical ledger 把以下 4 个本日 family 关闭在分母外，但仓库已有 exact-v1 深审、Books writeback 和通过的 post-write semantic audit；对应 Books 正文 marker 仍存在：

| arXiv v1 | 当前错误状态 | 已有长期增量 | Books marker |
| --- | --- | --- | --- |
| `2605.02125v1` | `pre_denominator_closure_reviewed` | 跨 facility 训练把 batch scheduler admission delay、staleness cutoff 与 aggregation 放入同一控制状态 | `SF-FEDQUEUE-CROSS-FACILITY-QUEUE-AWARE-TRAINING` / `TRAIN-DISTRIBUTED-TRAINING` |
| `2605.02179v1` | `pre_denominator_closure_reviewed` | 连续推理把 deadline-violation risk 与 burst history 提升为跨时间调度状态 | `SF-EDGE-CONTINUOUS-INFERENCE-RISK-BUDGET` / `INFER-SCHEDULING` |
| `2605.02391v1` | `pre_denominator_closure_reviewed` | temporal dependency、noise placement 与 privacy composition 共同限定流式监控发布 | `SF-DP-RUNTIME-MONITORING` / `PLATFORM-MONITORING` |
| `2605.02626v1` | `pre_denominator_closure_reviewed` | DPO 的低概率 rejected-gradient squeezing 与 probability-geometry gate 改变稳定训练边界 | `SF-GRADIENT-GATED-DPO` / `TRAIN-DPO` |

这不是抽样猜测，而是同一仓库中“已深审并写入”与“未入候选”同时成立的直接矛盾。四项必须恢复为候选并使用既有 exact-v1 证据重新校准分数；不能通过删除旧证据或 Books marker 消解矛盾。

`2605.02187v1` 当前被保留但判为 `No Change`，而 Books 中已有同一 primary 的 `SF-RESPONSE-PATH-TAMPERING-PROVIDER-SIGNATURE` 正文 marker。它需要登记为同一 family 的 alias，并将处置改成“已整合/既有正文复用”，不能把 `SF-2026-ARXIV-2605-02187` 当作另一个 family。

### 2. 一个旧 Books trace 的日期 owner 错误

`2605.03190v1` 不在本日 1058 个身份中。官方 owner receipt 将它归到 2026-05-06，initial registration 为 `2026-05-06T01:48:31Z`；但 `SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING` 的 Books trace 写成 Daily `2026-05-05`。保留正文机制，root 应把 provenance trace 和 owner report 迁到 2026-05-06，不能把它塞回 05-05 分母。

### 3. 81 个 `No Change` 尚无完整的具体覆盖证明

81 项中只有 5 项在 `V3_EVIDENCE_REVIEWS.json` 留下可定位的 existing-coverage marker：`2605.00842`、`2605.01708`、`2605.01989`、`2605.02038`、`2605.02087`。其余 76 项只有 owner 与章节路径，没有指出章节中实际承载命题的段落或具体既有论点。

章节名相似不能证明 `No Change — Existing Coverage`。应逐项补充“当前章节的具体论点 → 本文新增证据为何没有改变它”的短比较；若比较后存在新的长期增量，转为 root Books queue。这个缺口不能用 marker 数量、标题匹配或 validator 替代。

### 4. 分层 closure 抽检命中真实 false negative

对 957 个 closure 按 local-method、domain/application、benchmark/evaluation、other-specific 四类及 ID 等距样本复核时，上述 4 个已写 Books 的 family 构成确定 false negative。因此关闭理由共享的受影响簇尚不能通过。只需扩查以下语义簇，不要求重扫全部来源或追求全站零遗漏：

- training/runtime co-design：提前退出与 distillation 冲突、跨 facility admission、DPO gradient gating；
- time-coupled serving/monitoring：risk budget、temporal privacy composition；
- evaluation identity：编译/运行环境导致假失败、structured-output contract；
- Agent state/control：planner/actor/memory 计算所有权与 closed-loop data/workflow。

优先复核的具体条目为 `2605.01058`、`2605.02168`、`2605.02179`、`2605.02195`、`2605.02363`、`2605.02391`、`2605.02626`。它们不是自动准入清单；每项仍需按题摘中的实际设计变化作恢复或具体关闭。

## Root 串行修复队列

1. 将 `2605.02125`、`2605.02179`、`2605.02391`、`2605.02626` 恢复到本日候选；复用 `exact-v1-review-packet.json` 的既有审阅，按当前 V3 三维定义重新评分，并同步 Daily/canonical/evidence 计数。
2. 为 4 个恢复项及 `2605.02187` 建立 generic arXiv family 与现有 semantic family marker 的明确 alias；不得重复计数。
3. 将 `2605.03190` 的 Books provenance owner 改为 2026-05-06，并由 05-06 报告承接；正文不删除。
4. 对剩余 76 个 `No Change` 增补具体章节论点比较；只把比较失败的 family 加入共享 Books 写回队列。
5. 扩查上节列出的四个受影响 closure 语义簇。全部改判有明确理由、必要 Books 写回完成并做写后复核后，再重新执行一次非作者最终复核。

## Gate

- Coverage：安全终态；5 个机构历史目录缺口保持隔离。
- Evidence：99 项通过作者证据完整性检查，2 项终态受阻；候选恢复簇仍需重开。
- Books：未通过；存在候选/Books 状态矛盾和 76 项未证实的 `No Change`。
- Daily：未完成。

