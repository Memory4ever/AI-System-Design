# 2026-05-13 V3 Round 4 独立终审

**Review Provenance ID:** `daily-20260513-v3-round4-fresh-nonauthor-final-20260915`

**结论：FAIL；Daily 继续保持 `Ongoing`。**

本次由未参与 Round 4 作者返修和 Books 写回的 reviewer 在 fresh context 下执行终审。审查范围在本文件形成时冻结，不再扩大为全日重扫。格式与机械账目通过不能替代语义 Gate：有界假阴性挑战仍发现 20 个明确漏收，另有 6 个边界项需要保留具体重开条件；已写入 Books 的 30 个新段落中有 6 个缺少足以支撑长期正文的 exact-v1 证据边界；62 个 `No Change` 的锚点虽然机械存在，但有 3 个已确认不能语义承载对应增量。

## 1. 已通过的范围

- 账目闭合：`838 = (128 retained + 519 pre-denominator closure + 0 withdrawn) + 191 route isolation`。
- 128 个 retained family 均有唯一 Evidence Review、V3 score、Stable Node owner 与 Books disposition；V3 review depth 和分数档位机械一致。
- Books disposition 账目为 `15 Already Present + 51 current-worktree Applied + 62 No Change = 128`。
- Round 4 新写入的 30 个 `source-family` marker 均唯一、位于正确 owner 文件、位于唯一 `## Review notes` 之前；既往 21 个 `semantic-body-binding` 仍存在且未重复返工。
- 62 个 `No Change` locator 均能机械定位到 Review notes 前的正文；这只证明锚点存在，不证明命题等价。
- `scripts/validate_research.py --report papers/2026/05/13/README.md` 与 `git diff --check` 通过。

以上通过项在返修时不得被解释为整日 Gate 已通过，也不要求重新完成已经通过的 128 项全文审阅。

## 2. 有界 closure challenge

### 2.1 冻结方法

519 个 closure 中，337 个已有 Round 3 的独立 `closure_reconfirmed`，182 个尚无同等级的独立复核。本轮只在后者中冻结 26 个高风险 family，覆盖 Training、Inference、Multimodal、Agent、Evaluation 与模型机制；逐项依据标题和完整摘要判断是否改变长期机制、state/data/control ownership、evaluation contract 或 Books 既有命题。没有扩为 519 项全量重扫。

### 2.2 明确 false negatives：20 项必须重开

下列 family 不能继续作为 `Rejected — Below Candidate Denominator`。返修条件统一为：进入 Candidate Denominator；核验 exact-v1 正文、withdrawal 与版本身份；完成相应深度的 Evidence Review、V3 score、Stable Node owner、Books comparison 和独立复核。Books 是否修改仍由完成证据审阅后的 comparison 决定，不能从本表直接推导为 `Integrate`。

| arXiv ID | 为什么当前 closure 不成立 |
| --- | --- |
| `2605.11387` | RL fine-tuning 的 mode collapse 与行为多样性保持改变多模态生成 policy 的后训练约束，不只是特定机器人任务结果。 |
| `2605.11494` | 单步 diffusion 失去迭代随机性的约束及 feature-geometry perturbation 改变 inference-time diversity/fidelity 控制分支。 |
| `2605.11570` | activation observable 被用于识别训练 regime、weight decay 与 learning-rate 状态，直接影响训练可观测性和控制。 |
| `2605.11666` | skill × complexity 的任务发现、组合和 ZPD 过滤构成训练数据/curriculum controller，而非普通 reasoning benchmark。 |
| `2605.11706` | tool dependency graph、graph token 与 on-policy distillation 改变 Agent tool planning 的状态表达和控制流。 |
| `2605.11722` | 固定 visual program、predicate verification 与 edit/resample routing 改变生成过程的验证和 commit 控制。 |
| `2605.11872` | 将 PEFT 的 support selection 与 orthogonal transformation 分离，改变 adaptation subspace 的所有权和遗忘权衡。 |
| `2605.12039` | typed directed skill graph 及 merge/split/remove lifecycle 改变 Agent skill/memory 的持久状态管理。 |
| `2605.12056` | correspondence-preserving audiovisual chunking 与 cooperative token compression 改变多模态表示和推理数据流。 |
| `2605.12120` | 用户、机构与专业规范冲突下的 principal hierarchy 与 omission failure 直接改变 alignment/evaluation release contract。 |
| `2605.12122` | shared-feature collateral damage 与 concept-separated sparse representation 改变 diffusion unlearning 的状态隔离边界。 |
| `2605.12171` | 一层 Transformer 计算 parity 的 head × postprocess degree 下界属于架构表达能力边界，不是局部任务改进。 |
| `2605.12294` | 可执行知识图将 GUI planning 从重复自由生成迁移为 retrieval/execution 和 value-guided graph search。 |
| `2605.12327` | 多 FP4 grid、group-size 边界及 PTQ/pretraining 差异改变量化格式与精度配置判断。 |
| `2605.12380` | policy-ratio ESS 把 trust region 与 off-policy reliability 绑定到 batch 自适应目标，直接改变 RL post-training 控制。 |
| `2605.12426` | relational superposition、relation-conditioned MLP selection 及 capacity-depth trade-off 提供模型事实召回机制证据。 |
| `2605.12466` | fixed-point latent refinement、implicit differentiation 与 adaptive iteration 改变有效深度和训练内存契约。 |
| `2605.12480` | modality-wise reward routing、gradient surgery 与 region-wise credit 改变音视频 diffusion RL 的 credit ownership。 |
| `2605.12481` | GUI 与 tool 两类 action path 的选择、分阶段 SFT/RL 和效率 reward 改变 Agent action/workflow controller。 |
| `2605.12492` | 通过左右正交变换保持 spectrum 的 optimizer 是直接的 LLM training update 机制，不应在 denominator 前闭合。 |

### 2.3 Borderline closure：6 项保持 closure，但必须保存重开条件

这些项目本轮不进入 Candidate Denominator；它们不是“无关”，而是当前公开证据尚未越过长期系统命题门槛。未来只在满足表中条件时重开，不因同主题新论文或标题相似自动重开。

| arXiv ID | 当前处置 | 精确重开条件 |
| --- | --- | --- |
| `2605.11672` | 保持 closure | 出现形式化证明或跨设置实证，能够改变具体 correctness、bias、utility 的评估或 refusal contract。 |
| `2605.11905` | 保持 closure | 有跨 workload 对照能把一般 supervision granularity 原理与 theorem-proving 特定 recipe 分离。 |
| `2605.11931` | 保持 closure | 受控证据证明 vision-grounded self-improvement 的一般适用边界，而非只改善选定多模态 benchmark。 |
| `2605.12201` | 保持 closure | 不确定性方法改变通用 calibration/release contract，并证明可从 code-generation 特定 metric 外推。 |
| `2605.12422` | 保持 closure | 跨领域证据表明 disagreement prediction 是可复用的人类分歧传感器，而非教育难度判断的局部方法。 |
| `2605.12255` | 保持 closure | 形式化或实证结果真正改变可执行 world-state/model design；哲学或推断类比本身不构成 World Model 机制证据。 |

本轮真实结果是 **20 reopen + 6 borderline closure**。不得为了匹配先前口述计数而改写为 21+4。

## 3. Books 写回的证据边界缺口：6 项

30 个新 marker 的位置和 owner 均机械通过，但下列正文块没有完整兑现“旧约束 → 新机制 → 状态/控制权 → 代价/failure/fallback → exact-v1 证明与未证明”的长期正文合同。返修只能补强相应 marker 前的 canonical body，不得把 Review notes 或论文摘要复制进正文；补强后必须由未参与写入者重新逐项验收。

| arXiv ID | Owner | 已确认缺口 | 精确返修条件 |
| --- | --- | --- | --- |
| `2605.11195` | `PLATFORM-EVALUATION-SYSTEM` | 已说明 DP social bias 在行为层级间不同，但 trade-off、failure/fallback 与 exact-v1 受测模型/指标边界不足。 | 绑定 exact-v1 的模型、DP setting、行为层级与 metrics；补充什么条件下仍沿用独立 privacy/fairness gate，以及该证据不支持的因果和跨模型结论。 |
| `2605.11202` | `PLATFORM-EVALUATION-SYSTEM` | timed multi-request trace、replay 与 log-prob oracle 已写入，但缺少 exact-v1 engine/workload 范围和引入灰盒 fuzz 的成本/失败边界。 | 写清受测 engine、trace/oracle 能证明什么、不能证明什么；补充 nondeterminism、oracle drift 或 replay cost 下的 trade-off 与 fallback。 |
| `2605.11209` | `PLATFORM-EVALUATION-SYSTEM` | CEM 的 evidence-allocation 权与 failure-rate authority 已区分，但 exact-v1 task/model/sampling 范围及未证明项不完整。 | 绑定受测任务、模型与估计过程；明确 rare-event proposal 的证明边界、importance-accounting 失败条件及 uniform/stratified fallback。 |
| `2605.11376` | `AGENT-MULTI-AGENT` | population-scale negotiation 的 authority、代价与 fallback 已有，但缺少 exact-v1 evaluation/limitations 边界。 | 补充受测 population、protocol、agent/model 和 evaluator 范围；明确不能外推为真实社会协商或生产规模收益。 |
| `2605.12087` | `AGENT-PLATFORM` | typed/versioned/addressable/dependency-aware artifact 已写入，但 exact-v1 scope、tested boundary 与可执行 fallback 不足。 | 区分论文提出的数据模型与已验证 artifact；写清存储/一致性/迁移成本、authority 冲突 failure，以及何时回退轻量 event/log state。 |
| `2605.12131` | `PLATFORM-EVALUATION-SYSTEM` | rollout-card publication bundle、privacy/volume 代价与非证明项已有，但 exact-v1 evaluation/limitations 范围不充分。 | 绑定作者实际 bundle/rollout/reporting scope；明确 reproducibility evidence 不等于结果正确或可迁移，并给出隐私、体量或缺失 rollout 时的降级方案。 |

## 4. `No Change` 语义错配：3 项

62 个锚点全部可定位，但以下三项已确认“存在的标题”不等于“已有相同命题”。它们必须重开目标章节与相邻章节对读，重新选择真实 owner，并在 `No Change — Existing Coverage` 与 `Integrate` 之间重新判断；不能只更换一个更相似的标题。

| arXiv ID | 当前错误映射 | 为什么需要重开 |
| --- | --- | --- |
| `2605.11537` | 动态 expert replication/prefetch → `INFER-TENSORRT-LLM` 的“量化为什么不自动带来加速” | 量化命题不承载 future-token expert overload prediction、replica lifecycle、placement 和通信/内存 trade-off。 |
| `2605.11581` | adaptive MegaKernel DAG search → 同一量化锚点 | portability–efficiency、静态/动态 DAG schedule 与 branch penalty 不是量化是否加速的同一命题。 |
| `2605.12265` | cross-domain LLM monitor training → `PLATFORM-MONITORING` 的“Monitoring 也会改变系统” | 多任务 prompt fine-tuning 的跨域泛化证据不由通用 observability observer-effect 命题承载。 |

## 5. 有限返修清单与 Gate

本轮冻结后的返修范围只有四组：

1. 重开第 2.2 节 20 个 false negative，并完成 Candidate → Evidence → Score → Owner → Books Decision → 独立复核；
2. 保留第 2.3 节 6 个 closure 及其精确重开条件，不继续扩样；
3. 修复第 3 节 6 个 Books body 的 evidence boundary，再执行 fresh non-author post-write review；
4. 重做第 4 节 3 个 `No Change` comparison，不机械复用现有锚点。

在上述项目闭合前：

- `papers/2026/05/13/README.md` 必须保持 `Ongoing`；
- 51 个 current-worktree write 不能整体宣称最终 `Applied`；
- 不得将 validator、JSON 算术、marker 唯一性或本审计文件本身解释为 Daily Complete；
- 已通过的 128 项证据记录和其余 24 个新 Books marker 不要求重复返工，除非返修产生直接命题冲突。

本 reviewer 未修改任何 Books 文件，未 stage、commit 或 push。
