# 2026-05-08 V3 fresh-context 最终独立复核（2026-09-14）

## 结论

- **角色：** 未参与 05-08 作者修复、两轮 false-negative repair 或 root Books 写回的 fresh-context reviewer。
- **终审结果：** **未通过**。日报保持 `进行中`，不得登记 `Complete`，`final_independent_signoff` 保持 `false`。
- **已通过范围：** 当前账本机械守恒、日期与 Source Family 唯一性、Score V2 算术和深度路由、49 项 Applied 的 Books 正文存在性、57 项 No Change 的 owner/既有命题定位、cross-day owner 以及当前候选的 withdrawal/source terminal。
- **阻断范围：** 513 个 closure 的高风险语义反查发现 17 个由官方 exact-v1 题摘即可反驳现有关闭理由的明确 false negative；另有 `2605.05219` 的 retained Evidence record 内部冲突。现有 `619 = 106 + 513` 因而只能视为修复前账本，不能视为冻结终态。

本轮没有扩展来源、日期或 raw identity，也没有修改 Books。反例全部来自当前 619 个 canonical identity。

## 机械账本与当前候选检查

- 619 个 `arxiv_id` 与 619 个 Source Family ID 均唯一；当前文件可复算为 `619 = 106 retained + 513 closure`。
- 106 个候选均有 Evidence 终态：66 个 `deep_complete`、40 个 `standard_complete`、0 个 pending。
- Score V2 为 53 个 `7..9` 与 53 个 `5..6`；三个分量都在 `0..3`，总分复算无误，所有 `7..9` 均为深入审阅。
- Books 分流为 `49 Integrate — Applied + 57 No Change — Existing Coverage`；README 候选表、106 个 Evidence 小节与 JSON 的 106 个 ID 集合一致。
- primary terminal 为 105 个官方 exact-v1 HTML 与 1 个官方 exact-v1 PDF。当前 106 个候选及本轮 17 个反例的 arXiv 页面均未见 withdrawal banner；这里只确认审阅时的 exact-v1 状态，不对未来 revision 作保证。

上述检查只能证明当前文件内部一致，不能证明 closure 语义正确。

## Books 复核

### 49 项 Applied

- 43 项可由 canonical Source Family marker 或 exact arXiv identity 直接定位到声明 owner 的机制正文。
- 其余 6 项使用早期冻结的 title-derived stable marker，而不是当前 canonical ID；兼容映射分别为：`2605.05262`（InfoTree）、`2605.05274`（Sealing the Audit-Runtime Gap）、`2605.05379`（Partial Evidence Bench）、`2605.05413`（From History to State）、`2605.05467`（Nitsum）与 `2605.05628`（in-switch TP）。六段正文均位于各章 `Review notes` 之前，并真实承载预算选择、artifact identity、受限证据、workflow state、动态 TP 或 in-switch execution 的长期命题。
- 对 root 最近写入的 5 项重新阅读正文与相邻段落：`2605.05715`、`2605.05750`、`2605.06036`、`2605.06078`、`2605.06200` 均把机制、authority、证据边界、trade-off 与 fallback 写入唯一 owner，没有把作者 benchmark 外推为通用结论。

因此当前 49 项 Applied 的“正文真实存在”与“长期命题已落盘”通过；本轮 closure 新增候选的 Books Decision 尚未发生，不在这 49 项中。

### 57 项 No Change

- 57 个声明 owner 均能在 ROADMAP 解析，README 均给出待比较命题而非“章节已满”或低分关闭。
- 对本轮变化的 `2605.05250`、`2605.05501`、`2605.05678`、`2605.06308` 逐项检查具体正文：Ch66 已承载 simulator behavioral realism/decision fidelity、异质 confidence sensor 与 risk–coverage/abstention；Ch72 已承载 proposal-only、独立 policy/authorization gate 以及 trace/output/action/outcome authority 分离。
- 对未变化 53 项按 Agent、Training、Inference、Model/Multimodal、Evaluation 与 Security owner 重新分层核对，并复用此前独立审阅中未变化的 primary evidence；未发现把主题相似冒充具体既有覆盖的新增反例。

因此当前 57 项 No Change 通过；它们不是本轮 Gate 失败来源。

## Retained Evidence 的一个精确缺陷

`SF-2026-ARXIV-2605-05219` 的 Evidence 小节不能按当前文本通过：

1. `Evaluation contract` 是残缺句段（以 “asking different questions ...” 开始），没有自包含地说明 workload、对照与结果边界；
2. 同一小节写 `Disposition: Integrate`，却又说“current Books proposition already owns ... so no duplicate paragraph was added”；JSON 与紧随其后的 Books 结论则是 `Integrate — Applied`，Ch45 也确有该 family 正文。

最小修复是只重写该小节的 evaluation contract 与 disposition 说明，使其忠实描述 exact-v1 实验，并与实际 Applied 状态一致；无需删除或重写 Ch45 已存在的机制正文。

## Closure Gate：17 个明确 false negative

以下项目均已由官方 arXiv exact-v1 题名、完整摘要与 v1 日期确认。表中结论只是“必须重开候选审阅”，不预判最终一定 Integrate。

| Source Family | 当前关闭理由为何被原文反驳 | 建议 owner / 最小后续 |
| --- | --- | --- |
| [`SF-2026-ARXIV-2605-05561`](https://arxiv.org/html/2605.05561v1) | 4-bit quantization 会扭曲 test-time compute controller 的 uncertainty/stability 信号并导致 premature halt；这是 precision 与 runtime control 的明确耦合，尽管证据只有很小的 GSM8K shards。 | `INFER-SCHEDULING`，对读量化 execution owner；深入审阅统计功效与 controller 边界。 |
| [`SF-2026-ARXIV-2605-05632`](https://arxiv.org/html/2605.05632v1) | 在四类 RAG 架构上分离 retrieval 与 content-reasoning poisoning，并显示架构选择改变攻击成功率与 non-answer failure；直接改变 RAG security/evaluation contract。 | `PLATFORM-SECURITY`，对读 `AGENT-RAG`；深入审阅实现差异、judge precision 与 artifact。 |
| [`SF-2026-ARXIV-2605-05737`](https://arxiv.org/html/2605.05737v1) | deterministic harness 将错误检测与恢复从模型自省中分离，并给出跨模型、跨任务的长程 failure/recovery 证据；不是普通 Agent 应用。 | `AGENT-WORKFLOW` 或 `AGENT-PLATFORM`；深入审阅 state/operator 与失败回退。 |
| [`SF-2026-ARXIV-2605-05777`](https://arxiv.org/html/2605.05777v1) | 以轻量 proxy 对黑盒 LLM 的输出分布做 adversarial distillation，试图用单次推理替代多采样 uncertainty；会改变 confidence sensor 的成本与校准边界。 | `PLATFORM-EVALUATION-SYSTEM`；审阅 calibration、distribution shift 与 proxy fidelity。 |
| [`SF-2026-ARXIV-2605-05846`](https://arxiv.org/html/2605.05846v1) | 把 Agent termination judgment 明确为可被 context poisoning 控制的攻击面，并量化 step amplification；这是 workflow termination authority 的新 failure mode。 | `PLATFORM-SECURITY`，对读 `AGENT-WORKFLOW`；深入审阅 threat model、termination owner 与防御边界。 |
| [`SF-2026-ARXIV-2605-05953`](https://arxiv.org/html/2605.05953v1) | 用 residual-stream density estimator 作逐 token dynamic gate，只在异常时触发 contrastive decoding；这是 detection sensor 与 intervention control 的新分工。 | `PLATFORM-EVALUATION-SYSTEM`，对读 inference decoding；深入审阅 factual-manifold 假设、校准与 corruption rate。 |
| [`SF-2026-ARXIV-2605-05965`](https://arxiv.org/html/2605.05965v1) | selective eligibility trace 用低熵 token mask 替代 RLVR 的均匀 trajectory credit，直接改变 credit assignment owner 与稀疏 reward 传播。 | `TRAIN-GRPO`；深入审阅 mask 依据、baseline、公平预算与规模边界。 |
| [`SF-2026-ARXIV-2605-06166`](https://arxiv.org/html/2605.06166v1) | 从同一个 gradient interaction matrix 联合导出 parameter mask 与 data subset，改变受限微调中两类 selector 的耦合与成本。 | `TRAIN-SFT`，对读 `TRAIN-DATA`；标准/深入审阅 bilevel 近似和 matched budget。 |
| [`SF-2026-ARXIV-2605-06188`](https://arxiv.org/html/2605.06188v1) | 反证 OPSD 在 thinking-enabled reasoning 中能普遍“纠错”，并把它重新定位为 SFT→RLVR 后的 compression stage；直接改变 post-training pipeline 的适用边界。 | `TRAIN-GRPO`，对读 `TRAIN-SFT`；深入审阅 correct/incorrect rollout split 与任务范围。 |
| [`SF-2026-ARXIV-2605-06216`](https://arxiv.org/html/2605.06216v1) | 重新注入 token identity 的 EmbeddingMemory 直接挑战“一次 embedding、随后丢弃 token index”的 Transformer 结构假设，并给出 rare-token/contextual-collapse 机制。 | `MODEL-EMBEDDING`，对读 Transformer/Long Context；深入审阅结构、参数成本与因果证据。 |
| [`SF-2026-ARXIV-2605-06232`](https://arxiv.org/html/2605.06232v1) | 将 Agent privacy 从训练数据记忆扩展到搜索、上下文推断和聚合 profiling，并给出低成本现实攻击链；改变 data-access 与 derived-profile 风险边界。 | `PLATFORM-SECURITY`，对读 `AGENT-MEMORY`；深入审阅攻击能力、合法数据边界与测量方法。 |
| [`SF-2026-ARXIV-2605-06285`](https://arxiv.org/html/2605.06285v1) | 将 Agentic RAG 的自然语言 reasoning/subquery 改为单次 forward 的 latent token 与 latent retrieval，改变检索数据流、可观察性与 latency trade-off。 | `AGENT-RAG`，对读 inference execution；深入审阅可比延迟、joint training 与透明性。 |
| [`SF-2026-ARXIV-2605-06320`](https://arxiv.org/html/2605.06320v1) | 多 Agent 共同维护可演进 coordination graph，显式拥有依赖、assignment 与 progress state，并在 partial observability/communication constraints 下动态协调。 | `AGENT-MULTI-AGENT`；深入审阅一致性协议、冲突处理、wall-clock/token/file-operation 口径。 |
| [`SF-2026-ARXIV-2605-06423`](https://arxiv.org/html/2605.06423v1) | quiz-style black-box membership inference 在无内部访问下测试训练样本记忆，并比较多类防御；这是训练数据隐私的具体攻击/evaluation contract。 | `PLATFORM-SECURITY`，对读 `TRAIN-DATA`；深入审阅数据生成、query budget、FPR 与防御边界。 |
| [`SF-2026-ARXIV-2605-06548`](https://arxiv.org/pdf/2605.06548v1) | hierarchical continuous latent diffusion 将 global semantic prior transport 与 local text realization 分离，明确提出非 AR 的语言生成 factorization 与跨模态路线。 | `MULTIMODAL-GENERATIVE-PARADIGMS`；深入审阅 VAE/DiT/decoder 分工、matched baselines 与 scaling claim。 |
| [`SF-2026-ARXIV-2605-06596`](https://arxiv.org/html/2605.06596v1) | paired secure-aggregation queries 与跨轮统计把 client attribution 加入 federated LLM fine-tuning，同时引入可量化 privacy leakage/overhead。 | `PLATFORM-SECURITY`，对读 Training data provenance；深入审阅 SA 威胁模型、mutual-information bound 与 attribution measurement。 |
| [`SF-2026-ARXIV-2605-06632`](https://arxiv.org/html/2605.06632v1) | 通过显式 utility budget 联合优化 routing mask 与权重，把 SFT behavior 压进可因果干预的 sparse carrier，并在 inference 用 soft prompt 反转；改变 SFT behavior locality 与控制边界。 | `TRAIN-SFT`，对读 Model representation/Security；深入审阅 causal necessity、utility retention 与 trigger failure。 |

这 17 项均在 2026-05-08 的 official public batch 内，未发现 cross-day owner 冲突，也未见 withdrawal banner。修复后 retained 至少为 123、closure 至多为 496；最终数字仍须在相同高风险 closure strata 的最小同层反查完成后冻结。

## 最小修复范围

1. 只重开上述 17 个 family，完成 exact-v1 Evidence Review、Score V2、Stable Node、相邻章节对读与 Books Decision；不要机械全部 Integrate。
2. 对与反例共享错误模式的高风险 closure 做有界同层反查，范围限于：quantization×runtime controller、RAG/Agent security 与 termination、uncertainty/intervention、RLVR/post-training credit、Transformer identity injection、latent generation/RAG、multi-Agent coordination、LLM privacy/attribution。不得扩展新来源或其他日期。
3. 修复 `2605.05219` 的 Evidence record 文本冲突；Ch45 正文不需重写。
4. 同步 JSON 与 README 的真实 retained/closure、review depth、score 与 Books 分流；若新增 Integrate，再交 root 串行写 Books。
5. 由未参与这些修复与 Books 写回的 reviewer 对变化范围及同层 closure 再做 independent Gate。此前 49 Applied 与 57 No Change 的通过范围可复用，除非 owner 正文被修改。

## Gate

- **Coverage：** `Closed with declared source limitations`。
- **Current ledger mechanics：** `Passed`。
- **Current 49 Applied / 57 No Change：** `Passed`。
- **Candidate Denominator / Closure：** `Failed — at least 17 false negatives`。
- **Evidence：** `Failed — denominator incomplete; 2605.05219 record inconsistent`。
- **Books：** `Passed for current 49 Applied; pending decisions for reopened families`。
- **Completion：** `Ongoing`。
