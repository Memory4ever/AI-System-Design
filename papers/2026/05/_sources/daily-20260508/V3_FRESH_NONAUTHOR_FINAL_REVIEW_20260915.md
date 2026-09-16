# 2026-05-08 V3 fresh non-author 最终复核（2026-09-15）

## 角色与结论

- **Reviewer：** 未参与 2026-05-08 作者 Round 3 返修或 root Books 写回的新 reviewer。
- **复核范围：** 当前合同、canonical ledger、日报正文、Round 3 队列与 root 写回记录、4 个新增 Books 命题、2 个移动块、69 个 Applied owner/正文 locator、63 个 No Change 命题 locator、withdrawal/access/materials 以及 closure 的 fresh false-negative challenge。
- **结论：** **FAIL — 保持 `Ongoing`，`final_independent_signoff = false`。**

失败不来自账目、既有 Evidence 或 Books 写入缺陷，而来自 Candidate Denominator：对 487 个 closure 做独立分层反查时，官方 exact-v1 题摘已经足以确认至少 9 个 false negative。它们必须先重开并完成 Evidence、Score、owner 与 Books Decision；不能因为现有 Books 写回通过而提前关闭整日报。

## 机械账目与 Evidence

- canonical raw family：619；当前账本可复算为 `619 = 132 retained + 487 pre-denominator closure`。
- 132 个候选均有唯一 Source Family、exact-v1 URL、Score V2、Stable Node、Review Status 与 Books disposition。
- Score V2 算术成立：75 项为 7～9 分，57 项为 5～6 分；各分量均在 0～3，总分等于三项之和。
- Review 路由成立：92 项 `deep_complete`、40 项 `standard_complete`、0 项 pending。
- Books 分流成立：69 项 Applied、63 项 `No Change — Existing Coverage`，合计 132。

这些检查证明当前 retained 集合内部完整，但不能证明 487 个 closure 的语义分流完整。

## Books 变化范围复核

### Round 3 的 4 个新命题

| Source Family | Owner | 复核结论 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-05329` | `PLATFORM-EVALUATION-SYSTEM` | 正文位于 `Review notes` 前；先建立多数票的 policy ambiguity，再引入 annotator/policy identity，明确 APM 只是诊断工具并保留异质策略与 fallback，语义与 exact-v1 边界一致。 |
| `SF-2026-ARXIV-2605-05331` | `MULTIMODAL-REPRESENTATION` | 正文位于 fusion 与 `Review notes` 前；把 reconstruction、generator capacity 与 native-resolution artifact contract 分开，保留受限 Pareto 证据和旧表示方案的适用边界。 |
| `SF-2026-ARXIV-2605-06609` | `MODEL-TRANSFORMER-LAYER` | 正文位于章节结论与 `Review notes` 前；把“层可构造成归一化梯度步”限定为算法性解释，不外推成真实大模型隐藏状态的唯一机制。 |
| `SF-2026-ARXIV-2605-06660` | `TRAIN-DATA` | 正文位于去重链路与 `Review notes` 前；明确 setter、solver、verifier 的 artifact/authority 分工，保留 verifier 偏差、奖励投机和固定课程的 fallback。 |

4/4 的 owner、段落位置、演进关系、trade-off 与证据边界通过。

### Round 2 的 2 个移动块

- `SF-2026-ARXIV-2605-06216` 已移动到 `MODEL-EMBEDDING` 的“初始表示不等于上下文表示”基线之后，先解释 token identity 与 contextual state 的差别，再引入逐层 identity reinjection；顺序通过。
- `SF-2026-ARXIV-2605-06548` 已移动到 `MULTIMODAL-GENERATIVE-PARADIGMS` 的 diffusion 基本机制之后，先建立迭代修正，再讨论 continuous-latent/global-prior 分支；顺序通过。

### 69 Applied 与 63 No Change

- 69/69 Applied 均在声明的 Stable Node owner 中找到一个位于 `Review notes` 前的主正文 locator。早期 title-derived stable marker 通过兼容 alias 解析；review-note 中的证据索引重复不冒充第二个正文 owner。
- 63/63 No Change 的 Stable Node 均可由 ROADMAP 解析。此前已经独立通过且本轮 owner/disposition 未变化的 57 项保持有效；本轮新增 6 项逐项重新定位：`2605.05737` 对应 workflow 的 recovery/verification artifact，`2605.05777` 对应 calibration/risk–coverage/abstention，`2605.06219` 对应 per-verifier outcome 与 aggregation identity，`2605.06232` 对应 derived/contextual privacy，`2605.06320` 对应 authoritative coordination graph，`2605.06423` 对应 membership signal、sample identity、query budget 与低 FPR 边界。
- 本轮没有编辑 Books，也没有发现需要撤销现有 69 个 Applied 或 63 个 No Change 的确定性反例。
- README 候选表和 Evidence 小节中的部分 item-level suffix 仍保留“待非作者复核”这一写回时快照；本节与日报末尾的新 Gate 已记录真实终审结果。下轮同步新 denominator 时应一并清除这些过期 suffix，不能继续把它们当作当前状态。

## Withdrawal、Access 与 Materials

- 当前 132 个候选记录为 0 blocked、0 disputed、0 withdrawn、0 materials request；exact-v1 terminal 与日报 Evidence locator 均存在。
- 本轮重新打开的官方 arXiv exact-v1 页面未见 withdrawal banner。该判断只覆盖当前审阅时点，不对未来撤稿或 revision 作保证。
- Google Research、DeepSeek 与 MiMo 的日级历史目录限制已经在日报 Coverage Limitations 中显式隔离；它们不能支持“零遗漏”断言，但当前没有可唯一识别的材料请求。

## Candidate Denominator：fresh false-negative challenge

本轮不扩展来源、不重扫 619 identities。Reviewer 从 487 个 closure 中按 Model/MoE、Multimodal、World Model、Training/Agent、Inference 与 Security 分层抽取 26 项，直接比较 exact-v1 题摘与 family-specific closure reason。至少以下 9 项的原关闭理由被 primary evidence 反驳；表中结论只是“必须重开”，不预判最终一定写入 Books。

| Source Family | exact-v1 已证明的长期机制增量 | 原 closure 的错误 | 建议 owner / 最小复核 |
| --- | --- | --- | --- |
| [`SF-2026-ARXIV-2605-05278`](https://arxiv.org/abs/2605.05278) | 将 MoE gate 建模为同时控制计算、通信与准确率的 stochastic channel，并提出 routing information / accuracy-rate proxy。 | 以 finite-bank MNIST 证据较弱为由，把可迁移的 routing-control 问题整体关在分母外；弱外推应降低分数或形成 No Change，而不是抹掉候选身份。 | `MODEL-MOE`，对读 `INFER-SCHEDULING`；核验 toy setup、信息量估计与真实 distributed MoE 未证明项。 |
| [`SF-2026-ARXIV-2605-05485`](https://arxiv.org/abs/2605.05485) | 把 reasoning trace 编译为可复用 symbolic solver，使 test-time control 从逐请求 LLM search 转移到可验证 artifact，并形成一次构建、多次摊销的成本模型。 | 以 program synthesis 任务域为由忽略了 reasoning-to-artifact、authority transfer 与 amortization 的通用 Agent/Workflow 命题。 | `AGENT-WORKFLOW`，对读 Tool/Planning；核验 DSL 边界、solver verification、transfer 与失败回退。 |
| [`SF-2026-ARXIV-2605-05646`](https://arxiv.org/abs/2605.05646) | 将视觉 tokenizer 的 reconstruction–semantic conflict 归因于梯度/流形错配，并以 structure/value 的正交更新重新分配优化责任。 | 原 closure 只称“局部实现”，遗漏了表示 artifact 中 fidelity 与 abstraction 的长期冲突及 owner 分离。 | `MULTIMODAL-REPRESENTATION`；核验 gradient evidence、ablation、teacher/data 边界与服务条件。 |
| [`SF-2026-ARXIV-2605-05702`](https://arxiv.org/abs/2605.05702) | 同一 knowledge-graph construction path 同时拥有问题生成约束与 Solver 的 waypoint process reward，改变 synthetic task admission 和 credit assignment。 | 将其当成 QA 局部结果，忽略了 proposer/solver/reward artifact 的可迁移状态与控制分工。 | `TRAIN-DATA` / `TRAIN-GRPO`，对读 Agent search；核验 reward leakage、invalid-question filtering 与跨任务边界。 |
| [`SF-2026-ARXIV-2605-05709`](https://arxiv.org/abs/2605.05709) | 证明 MLLM 自身的 reconstruction capability 会成为 jailbreak attack surface；concealment 与 recoverability 构成跨模态 safety trade-off。 | 以攻击方法绑定模型/任务为由关闭，遗漏了 safety filter 与 victim reconstruction authority 分离的新 failure mode。 | `PLATFORM-SECURITY`，对读 Multimodal Representation；核验 threat model、模型覆盖与防御边界。 |
| [`SF-2026-ARXIV-2605-05892`](https://arxiv.org/abs/2605.05892) | 反证 fixed、single-step、position-invariant activation steering 假设，并用 concept-conditioned flow 改变 inference-time intervention 的状态轨迹。 | 将跨模型 held-out evaluation 与 intervention geometry 误写为局部方法，未进入 Model/Inference 的控制边界比较。 | `MODEL-TRANSFORMER-LAYER`，对读 Evaluation；核验 matched prompting baseline、token/layer ownership 与 OOD 泛化。 |
| [`SF-2026-ARXIV-2605-06124`](https://arxiv.org/abs/2605.06124) | 将 dual-pass CFG 改写为 initial-prior steering 的 single-pass 近似，直接改变生成推理的数据流、计算成本与 approximation boundary。 | 把明确的 execution-plan 分支关闭为局部生成结果。 | `MULTIMODAL-GENERATIVE-PARADIGMS`，对读 inference execution；核验一阶近似、matched latency/quality 与 workload 条件。 |
| [`SF-2026-ARXIV-2605-06192`](https://arxiv.org/abs/2605.06192) | 从抽象低维 action token 演进为 camera-space kinematic-to-visual action field，并以 bidirectional fusion 连接 action 与 visual transition。 | 以机器人 benchmark 域为由忽略了 action-conditioned world-state representation 的 owner 变化。 | `MULTIMODAL-WORLD-MODELS`，对读 Embodied VLA；核验 state/action identity、rollout fidelity 与 sim-to-real 未证明项。 |
| [`SF-2026-ARXIV-2605-06207`](https://arxiv.org/abs/2605.06207) | 给出 uniform visual codebook 的 information-theoretic entropy cliff，并用 position-varying capacity 建立 coarse-to-fine token hierarchy。 | 关闭理由称未改变 representation owner，但 exact-v1 正在改变 codebook capacity 的分配原则和 AR visual token contract。 | `MULTIMODAL-REPRESENTATION`，对读 Generative Paradigms；核验公式假设、dataset-size dependence、ablation 与语言类比边界。 |

上述 9 项均属于当前 619 raw set，日期 owner 不变，也不是要求把 487 项全部 retain。它们足以否定“Candidate Denominator 已冻结”的结论；修复者还需对同错误层做有界反查，防止只修列出的 title 而保留相同 generic closure。

## 最小返修范围

1. 只重开上述 9 个 Source Family，完成 exact-v1 Method、Evaluation、Limitations、withdrawal、Score V2、Stable Node 与 Books proposition compare；不机械全部 Integrate。
2. 有界反查与这 9 项共享的 closure 层：MoE routing/control、reasoning-to-executable artifact、visual tokenizer objective/capacity、synthetic task/reward ownership、multimodal reconstruction safety、activation intervention、single-pass generative inference、action-conditioned world state。不得扩展来源、日期或重新枚举 619。
3. 保留已通过的 132 Evidence、69 Applied、63 No Change、4 个新增 Books 命题与 2 个移动块；除非重开项目产生直接冲突，不得推倒这些已验收范围。
4. 若重开项目形成 Integrate，只生成精确 root queue；共享 Books 由唯一 owner 串行写入。
5. 同步 README 与 canonical ledger 的新 retained/closure、Evidence、Score 和 Books 分流，并清除 item-level 的过期“待非作者复核”suffix；再由未参与返修和写回的新 reviewer 对变化范围签署最终 Gate。

## Gate

- Coverage / identity：**Passed with declared source limitations**。
- Current ledger mechanics：**Passed for `619 = 132 + 487` snapshot**。
- Current 132 Evidence / Score / owner / disposition：**Passed**。
- Current 69 Applied / 63 No Change：**Passed**。
- Four Round 3 insertions / two flow moves：**Passed**。
- Withdrawal / access / materials：**Passed for current retained set**。
- Candidate Denominator：**FAIL — at least 9 additional false negatives**。
- Final completion：**Ongoing**。
- Final independent signoff：**false**。
