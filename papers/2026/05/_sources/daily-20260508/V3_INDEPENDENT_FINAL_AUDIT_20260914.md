# 2026-05-08 V3 独立终审（2026-09-14）

## 结论

- **角色：** 未参与 05-08 作者审阅、challenge 修复或共享 Books 写回的 fresh-context reviewer。
- **终审结果：** **未通过**。日报必须保持 `进行中`，不能登记 `Complete`。
- **通过部分：** 当前账本集合、88 项候选证据记录、14 个 Daily 来源的已声明边界、37 项 Books 写回存在性，以及 challenge 新增四段 Books 正文均已通过本轮复核。
- **阻断部分：** 对 531 个 closure 的独立反例抽检再次发现可执行的 false negative。作者 challenge 已经把 6/6 高风险样本从 closure 恢复为候选；本轮使用不同样本仍发现 9 个明确需要重开的 family，因此 closure Gate 不能接受。

这不是要求无界扩张或证明全站绝对零遗漏。反例均来自已经冻结的 619 个 raw identity，且题名与完整摘要已经足以反驳当前“没有长期 AI System 增量”的关闭理由。

## 已独立通过的检查

### 账本、日期与唯一性

- `ARXIV_OWNER_RECONCILIATION_V3.md` 中本批次 ID 为 619 个且全部唯一，与 `V3_RECERTIFICATION.json.items` 集合完全相同。
- `619 = 88 retained + 531 pre-denominator closure`；不存在重复 arXiv ID、重复 Source Family ID、无终态项目或分数算术错误。
- 88 个候选都具有 exact-v1 URL、`public-batch-derived` 时间、Stable Node、三维分数、审阅深度和 Books disposition；README 的 88 个候选表行、88 个证据小节与 current ledger 集合一致。
- 公开批次 `2026-05-08T08:00:00+08:00` 落在日报窗口内。195 个缺少同批次 OAI confirmation 的 DataCite proxy 没有混入 current 619 ledger。
- current ledger、README 与本轮本地证据没有 withdrawn 标记。该结论只覆盖当前已审阅身份与记录，不把“未见标记”扩写成对所有未来 revision 的保证。

### 候选评分与证据深度

- 88 个候选的 Score V2 均满足三个维度各自为 `0..3`、总分复算正确且不低于准入线；分布为 38 个 `7..9` 与 50 个 `5..6`。
- 审阅深度为 49 个 deep、39 个 standard；38 个高分项全部 deep，另外 11 个较低分项因 Books override 或结论风险进入 deep，没有用总分替代审阅深度判断。
- 88 个证据小节均有独立正文，不是仅有链接或标题；每项都记录机制、评价或可验证条件、non-proof/适用边界与 Books 判断。未发现 `Review Pending` 或材料受阻被伪装成完成。
- 三维分数并非简单复制：当前候选存在 11 种 `(Design Delta, System Reach, Durability)` 组合。部分 `2+2+2` 项仍较集中，但本轮没有找到会改变其 disposition 的单项抬分反证。

### Daily 来源

- README 明确列出 13 个机构源与 arXiv，共 14 个 Daily 来源；没有混入 Weekly-only 来源。
- Google AI、DeepSeek、MiMo 三项只被记录为不可用于候选或零遗漏断言的隔离限制；OpenAI、Anthropic、Qwen 的日期粒度不足项也没有被强行归入窗口或用于 Books。
- 因此来源表本身没有把 access gap 伪装成“检查到零命中”。这些限制仍需保留，但不是本轮 closure Gate 失败的原因。

### Books：37 Applied 与 51 No Change

- current ledger 已同步为 `37 Integrate — Applied + 51 No Change — Existing Coverage`，不再把已经落盘的四项写成 `Queued`。
- 37 个 Applied family 均能在其声明 owner 章节找到唯一 source-family marker 或等价的 stable body marker；没有 marker 指向错误章节。
- 51 个 No Change 在 README 的证据小节中均给出具体 owner 与已有命题，不是以“章节已满”或分数不足关闭。抽查覆盖 Agent、Evaluation、Security、Training、Inference、World Model 各 owner，未发现显著 owner 冲突。

#### challenge 新增四段逐段结论

1. `2605.05365 / INFER-SCHEDULING / Ch56`：**通过**。正文把 bounded active context 与 bounded total work 分开，明确 round boundary、batch membership、carried tail、状态版本、tail sufficiency 与 full-history fallback；证据边界限于 8B、DP+CP 和披露的 Markovian RSA。
2. `2605.06615 / TRAIN-PRETRAINING / Ch28`：**通过**。正文没有把 SignSGD 写成通用排名，而是绑定 `ell_1` stationarity、`ell_infinity` smoothness、separable sparse noise；同时保留 magnitude-aware optimizer 的适用条件和小模型证据边界。
3. `2605.06642 / TRAIN-GRPO / Ch33`：**通过**。正文区分 strategy state 与 action trace 的两级 group owner，记录 `N×M` rollout 成本、strategy staleness、receding-horizon 修订及 reactive fallback；与相邻 token/trajectory credit 主线衔接正常。
4. `2605.06650 / TRAIN-GRPO / Ch33`：**通过**。正文明确 positive-only 仍通过 softmax normalization 产生负向作用，分离 positive-set、policy identity、EMA anchor 与外部 verifier owner，并保留 zero-positive、selection bias 和标准 PPO/GRPO fallback。

## Closure Gate 反例

本轮先按 `systems/runtime`、`agent/RAG/security`、`training/optimization`、`evaluation`、`multimodal/embodied`、`domain/local method` 六层做确定性分层抽查，再对摘要中显式出现 state/control ownership、execution contract、release/evaluation contract 或跨层 trade-off 的 family 做高风险反查。以下 9 项不能维持当前 closure：

| Source Family | 摘要已显示的长期增量 | 建议 owner | 终审要求 |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-05594` | oracle context 反而破坏正确多模态预测，并把 recorruption 定位到视觉注意力抑制与位置偏置；这是 multimodal RAG 的跨模态状态/证据融合 failure contract | `AGENT-RAG`，并与 `MULTIMODAL-REPRESENTATION` 对读 | 重开、exact-v1 审阅、评分与 Books Decision |
| `SF-2026-ARXIV-2605-05657` | 由代码结构复杂度选择多 Agent 拓扑，并以 resource algebra 保证动态图预算守恒；直接改变 topology selector 与 budget owner | `AGENT-MULTI-AGENT` | 重开、验证 theorem/实验边界并决定是否仅 No Change |
| `SF-2026-ARXIV-2605-05700` | 真实 IDE trace 与 LLM 模拟 trace 在多样性、时序和探索行为上显著不同，直接反驳仅以模拟 interaction 作为 Agent evaluation/training evidence 的做法 | `PLATFORM-EVALUATION-SYSTEM` | 重开、审阅数据与 simulation-to-reality contract |
| `SF-2026-ARXIV-2605-05818` | RAG leakage 被拆为 query generation 与 adversarial instruction 的独立因素，并暴露 faithfulness 提升与 leakage 的冲突；这是明确的 Security/Evaluation contract | `PLATFORM-SECURITY` | 重开、exact-v1 与 artifact 审阅、Books 对读 |
| `SF-2026-ARXIV-2605-05838` | stepwise momentum 的 linear-attention recurrence、严格因果 chunkwise parallel training 与 recurrent decode consistency 形成新的 state/update/execution contract | `MODEL-LONG-CONTEXT` | 重开、核对公式、Triton 实现、throughput 与 train/decode handoff |
| `SF-2026-ARXIV-2605-06014` | 两/三次 randomized Hadamard transform 分别满足标量量化与 block VQ 所需的不同分布条件，并提出 runtime 自适应次数检查；改变 quantization preconditioner 的正确性边界 | `INFER-TENSORRT-LLM` | 重开、审阅证明适用条件与 runtime 成本，不得把渐近界外推成通用加速 |
| `SF-2026-ARXIV-2605-06311` | 以 lighting/material realism 校准 simulation 对真实机器人策略排序的可信度，并报告 sim-to-real correlation；这是 Embodied evaluation 的环境真实性 contract | `MULTIMODAL-EMBODIED-VLA` | 重开、核对 real-world 配对、policy 数量与相关性边界 |
| `SF-2026-ARXIV-2605-06326` | tool-enabled evaluation 即使几乎不调用工具也可能损伤 reasoning，并把 teacher learnability、tool-trajectory ratio、SFT/RLVR handoff 与 mode-collapse safeguard 放入一条训练链 | `TRAIN-SFT`，相邻对读 `TRAIN-GRPO` 与 `AGENT-TOOL-CALLING` | 重开、exact-v1 与配方可归因性审阅；可能为 No Change，但不能在分母前关闭 |
| `SF-2026-ARXIV-2605-06631` | 将音频压缩验收从 aggregate accuracy 改为 worst-family excess answer error，并以统计置信度签发 compression budget；这是明确的部署 release/evaluation contract | `PLATFORM-EVALUATION-SYSTEM` | 重开、核对统计假设、family partition 与模型/任务边界 |

反查中的 `2605.05561`、`2605.05702`、`2605.06342`、`2605.06460`、`2605.06529`、`2605.06557`、`2605.06576` 等仍可维持 closure：它们分别受极小 partial shard、局部 reward/steering/retrieval 方法、领域模拟或非本项目对象限制，摘要尚不足以证明新的通用 owner 或 release contract。

## Root 修复队列与 Gate

1. 由作者/repair lane 对上述 9 个 family 做 exact-v1 Evidence Review、独立三维评分、Stable Node 与 Books Decision；不要机械全部 Integrate。
2. 若结论为 `No Change`，必须指向 owner 章节的具体既有命题；若为 `Integrate`，交 root 串行写共享 Books 后再做 post-write semantic audit。
3. 将真实修复结果同步到 `V3_RECERTIFICATION.json` 与 README，重新计算 retained/closure、分数分层、审阅深度及 Books 分流。
4. 由另一个未参与这 9 项修复的 reviewer 对修复项和其余 closure 再做一次有界独立抽查。新的抽查若不再出现 false negative，才可关闭 05-08。

**当前 Gate：** Coverage `Closed with declared source limitations`；Evidence `Failed — closure false negatives remain`；Books `Passed for current 37 Applied, pending decisions for reopened families`；Completion `Ongoing`。

## 后续修复 handoff（不改写本次独立结论）

修复作者随后已对上述 9 个 family 完成 exact-v1 Evidence Review、Score V2、Stable Node 与 Books Decision，并将它们从 closure 恢复为候选；结果见 `V3_FALSE_NEGATIVE_REPAIR_20260914.md`。其中 7 项进入 `BOOKS_WRITEBACK_QUEUE_FALSE_NEGATIVES.md`，2 项为具体 owner 下的 `No Change — Existing Coverage`。

本说明只登记后续状态，不把作者修复冒充本 reviewer 的再次验收。root 写回 7 项共享 Books 后，仍需一个未参与本次修复与写回的 reviewer 执行新的独立 Gate。
