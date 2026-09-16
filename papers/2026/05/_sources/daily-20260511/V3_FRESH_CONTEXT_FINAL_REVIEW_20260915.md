# 2026-05-11 V3 Fresh-context 终审

**复核者：** `/root/may11_fresh_final_review`（未参与作者筛选与 Books 写回）  
**复核时间：** 2026-09-15（Asia/Shanghai）  
**结论：** 未通过；`2026-05-11` 必须保持 `进行中`

## 1. 复核范围

本次不接受 README 中的完成度陈述作为证据，独立检查了：

- 当前 `RESEARCH_CONTRACT.md` 与 `REPORT_CONTRACTS.md`；
- Daily README、V3 screening ledger、Evidence reviews、Books writeback queue 与 root 写回记录；
- 计数、日期、三维评分、Evidence / Books disposition；
- 10 个 Books 写回的实际正文、上下文位置与唯一 source-family marker；
- retained 与 closure 的 false-positive / false-negative 抽样；
- withdrawn / blocked 隔离；
- validator 与 scoped `git diff --check`。

## 2. 已通过且应保留的部分

### 2.1 账目与评分算术

- `826 = 635 official direct + 191 ordinary revision recovery`；
- `635 = 29 retained + 606 pre-denominator closure`；
- `29 = 28 accessible + 1 blocked`；
- 当前 disposition 为 `10 Integrate + 16 No Change + 2 Weekly Only + 1 Temporarily Blocked`；
- 29 项现有评分的三个分项均在 `0–3`，Total 加总正确；
- 窗口、时区与 arXiv official announcement owner 口径一致。

`2605.06675` 只由 ordinary-revision recovery 命中，当前没有 important-revision signal；它不是本窗 candidate false negative，继续排除是正确的。

### 2.2 已落实的 10 个 Books 写回

以下 marker 在 Books 中各出现且仅出现一次：

| Source Family | Owner | 正文检查 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-06733` | `TRAIN-LORA` | 通过 |
| `SF-2026-ARXIV-2605-06788` | `PLATFORM-EVALUATION-SYSTEM` | 通过 |
| `SF-2026-ARXIV-2605-06885` | `MULTIMODAL-GENERATIVE-PARADIGMS` | 通过 |
| `SF-2026-ARXIV-2605-06914` | `INFER-SCHEDULING` | 通过 |
| `SF-2026-ARXIV-2605-07063` | `TRAIN-DATA` | 通过；但来源链接须按 3.3 修复 |
| `SF-2026-ARXIV-2605-07546` | `WORLDVIEW-SCALING-LAW` | 通过 |
| `SF-2026-ARXIV-2605-07568` | `MULTIMODAL-REPRESENTATION` | 通过 |
| `SF-2026-ARXIV-2605-07698` | `INFER-SPECULATIVE-DECODING` | 通过 |
| `SF-2026-ARXIV-2605-07881` | `INFER-TENSORRT-LLM` | 通过 |
| `SF-2026-ARXIV-2605-08012` | `PLATFORM-EVALUATION-SYSTEM` | 通过 |

这些正文均位于唯一的 `## Review notes` 之前，并且实际写出了旧约束、状态或控制权变化、机制、trade-off、failure / fallback 与证据边界；没有发现论文清单式追加或重复 marker。后续修复不应回滚或重写这 10 处已通过正文，除非新证据直接推翻其采用命题。

### 2.3 机器检查与隔离

- `python3 scripts/validate_research.py --report papers/2026/05/11/README.md` 通过；
- 本日报、V3 evidence/ledger/queue 与 10 个 Books owner 文件的 scoped `git diff --check` 通过；
- 当前 V3 正向链中未发现 withdrawn family；
- OpenAI、Google AI、Meta、Qwen、Moonshot、MiMo Blog 的历史目录限制均有隔离范围和定点重开条件，没有被用作候选、Books 或“全站无遗漏”证据。

以上机器检查只证明格式和可判定一致性，不改变下面的语义失败结论。

## 3. 阻止 Complete 的问题

### 3.1 P0：Candidate Denominator 存在跨主题系统性 false negative

False-positive 抽样覆盖全部 10 个 Integrate，以及按处置分层抽取的 `2605.06755`、`2605.06841`、`2605.06997`、`2605.07002`、`2605.07209`、`2605.07719`、`2605.07935`；这些 family 均具有明确的 AI System 机制或 evaluation contribution，没有发现应退回分母前的明显 false positive。该结果只支持抽样项，不外推为 29 项全量无误。

对 direct closure 做确定性间隔抽样和面向边界主题的定向抽样后，至少发现下列 14 个 official-direct family 的题名与完整摘要已经明确触发候选准入条件，却被统一模板理由关闭。这里的结论是“必须进入 candidate 并进一步评分/审证”，不是预判它们必须写入 Books。

| arXiv | 为什么必须重开候选准入 |
| --- | --- |
| `2605.06676` LKV | 直接改变 KV eviction 的 head budget 与 token selection owner，由 heuristic allocation 变为端到端学习。 |
| `2605.06702` CASCADE | 直接讨论部署期无权重更新的 episodic memory / contextual-bandit adaptation，改变 learning state 所在位置。 |
| `2605.06905` Conservative Flows | 提出从 data-support 初始化并保持数据分布不变的替代生成动态，属于生成范式分支。 |
| `2605.06946` Adaptive Memory Decay | 为 log-linear attention 引入 input-dependent、多层级记忆衰减，改变 fixed-state 的遗忘控制。 |
| `2605.07046` IRT Evaluation | 用 stochastic response 与 item heterogeneity 替代平均 accuracy，直接改变 evaluation contract。 |
| `2605.07247` EnvSimBench | 暴露 LLM 环境模拟在 state change 下的能力断崖，并构造 constraint-driven environment，直接影响 Agent 训练与评测。 |
| `2605.07278` RC-aux | 区分 predictive latent 与 plannable latent，并用多时间尺度 / reachability supervision 修正目标错配。 |
| `2605.07363` MISA | 直接针对 DSA indexer 成本，以 mixture-of-indexer routing 改变长上下文稀疏注意力的选择路径。 |
| `2605.07490` Cross-Modal Backdoors | 将多模态 connector 明确为可跨模态迁移的 supply-chain attack surface，改变安全边界。 |
| `2605.08013` CLI Agent | selective observation 与 structured turn/action credit assignment 直接改变 Agent 训练的观测和 credit owner。 |
| `2605.08029` STARFlow2 | 以 causal mask / KV cache 连接 autoregressive LM 与 normalizing flow，属于统一多模态生成机制。 |
| `2605.08037` GraphDPO | 将 pairwise preference 扩展为含传递性与等价类的 preference graph，改变 post-training objective。 |
| `2605.08044` Fast Byte Latent Transformer | 以 block diffusion、自推测与验证解决 byte-level 自回归吞吐，直接涉及模型与推理机制。 |
| `2605.08060` Memory Curse | 通过 content-vs-length 隔离说明更多可见历史可能降低多 Agent cooperation，改变 memory/evaluation 边界。 |

此外，`2605.06673`、`2605.06696`、`2605.06723` 所在的 metacognition、multi-agent monitoring 与 pre-verbalization state strata 也应重新语义筛选；本次抽样不足以替它们预先做最终 admission。

这些漏选横跨 KV、长上下文、生成、World Model、Agent、评测、训练与安全，不能解释为单个关键词或单一 owner 的局部遗漏。606 个 closure 使用同一泛化结尾，未形成可复核的 family-specific comparison。作者应只重开受影响的 in-scope strata，保留显然 out-of-scope 的关闭项；不要求把 606 项全部变为候选。

### 3.2 P0：29 项 Evidence Review 缺少实际证据位置

`V3_EVIDENCE_REVIEWS_20260914.json` 的每项只记录 claim、机制概述、non-proof、owner 与 disposition，没有 Method / evaluation / limitations / appendix 等实际证据位置，也没有在 claim 依赖 artifact 时记录 artifact 状态。README 也只给出总结性段落。

这不满足当前合同的“记录实际证据位置与解释”以及报告合同的“写清采用的精确版本、关键证据位置、机制与边界”。因此 28 项 `accessible_exact_v1` 目前不能整体视为 Evidence Gate 已通过；不能以“长证据字段”替代可定位证据。

### 3.3 P0：blocked family 已恢复，终态隔离失效

2026-09-15 实测官方 `https://arxiv.org/html/2605.07250v1` 返回 `200`，全文、Limitations 与附录均可读。现有 `blocked_exact_v1`、README 中“HTML/PDF/TeX 均未恢复”以及终态外部保留项已经失效。

作者需定点阅读 exact-v1 的 threat model、visual degradation 设置、模型与 evaluator、机制/缓解 ablation、limitations，并重新完成评分边界、Evidence 与 Books Decision。无需重扫其他来源。

### 3.4 P1：两项 `accessible_exact_v1` 指向失效的 HTML

2026-09-15 实测以下 README / evidence primary URL 返回 `404`：

- `https://arxiv.org/html/2605.06760v1`
- `https://arxiv.org/html/2605.07063v1`

这不自动推翻现有 claim 或已通过的 Books prose，但作者必须把 evidence primary 改为实际可访问的 official exact-v1 PDF / TeX / 其他原始版本，并补充对应证据位置；不能让 `accessible_exact_v1` 只由失效链接支撑。

### 3.5 P1：低于 7 分的 Deep Review 缺少 override 理由

`2605.06733`、`2605.06788`、`2605.07063`、`2605.07881` 的 Total 为 5 或 6，却标记为 Deep Review。因它们被判定为 Books 增量，强制 deep 可以符合合同，但当前 evidence / README 没有明确记录 override 原因。修复时应把“与 Books 当前命题比较后确认存在长期缺口”写成 review-depth override，避免读者误以为评分阈值失效。

## 4. 精确修复边界

1. 保留现有 10 个 Books 写回及其唯一 marker；不要因为本次终审失败而回滚合格正文。
2. 重新语义筛选 3.1 所列 family 与同类受影响 strata，给出 family-specific admission / closure 理由；至少将表内 14 项恢复为候选。
3. 对恢复候选补齐三维评分、Evidence Review、Owner、Books 比较与最终 disposition；若产生新 Integrate，再由 root 按日期顺序串行写 Books。
4. 为 29 个现有 retained family 补齐 exact-v1 的关键证据位置；证据依赖 artifact 时记录 artifact 状态。定点完成 `2605.07250` 的全文审阅。
5. 修正 `2605.06760`、`2605.07063` 的 exact-v1 primary 路径。
6. 为四个低分 Deep Review 补写强制深审的具体原因。
7. 重算 README、ledger、evidence、queue 与 checkpoint 的计数和状态，重新运行 validator、Markdown / marker / score / diff 检查。
8. 作者修复完成后交给另一名未参与修复的 reviewer 做新的 fresh-context 终审；本 reviewer 不能自审自己的修复。

在上述可执行工作完成前，`2026-05-11` 不得标记 V3 Complete。
