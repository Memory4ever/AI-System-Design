# Daily Research — 2026-08-07

**Coverage Window:** 2026-08-05 09:05 ～ 2026-08-07 09:05（Asia/Shanghai）
**Access Date:** 2026-08-07
**Archive Clock:** Friday；仅生成 Daily，不生成 provisional `2026-W32`
**Status:** Primary-source review complete；2 项 refine 现有章节，1 项完成章节级去重

## Executive Summary

过去 48 小时没有发现模型公司官方 Research 中同时满足 event date、公开机制与长期 AI System
增量的新发布。主要证据来自 2026-08-05 首次公开的 arXiv v1，以及 8 月 6 日的工程 Release：

1. **AFD-Ledger** 补上了 A/F disaggregation 从局部机制到真实部署决策之间缺失的 accounting
   layer。长期结论不是“异构 A/F 一定更快”，而是局部 acceleration 必须在相同 model、workload、
   SLO、预算、catalog 与 runtime contract 下，通过 best-vs-best 的完整 provisioning；FFN-only
   devices 还会带来 request-bearing-capacity tax。
2. **The Loss Does Not See the Basis, but Adam Does** 说明相同函数与 loss 不保证 optimizer
   trajectory 相同。对含 gauge symmetry 的 factored parameterization，coordinate-wise
   preconditioning 可能选择任意 basis；optimizer 因而是 parameterization contract 的一部分，
   不是可独立替换的标量旋钮。
3. **Argus** 为 fixed-weight、persistent agent runtime 提供了新的系统案例，但它的 durable state、
   bounded missions、review gate、rollback、event log 与 operator escalation 已被 Ch77 的 Workflow
   control-plane 框架覆盖。本轮采用 `No Change — Already Covered`，不复制架构角色或 benchmark。
4. **KServe v0.20.0** 与 **Dynamo v1.3.1** 作为工程版本事实保留。前者横跨 routing、KV tiering、
   traffic splitting、tracing 与 rollout；后者修复并保留了特定 GB200/SGLang/NIXL/EFA failure
   boundary。Release 不能代替各 PR、设计文档与代码路径，不直接写入 Books。

三篇论文均为单篇 v1 preprint，Evidence Level 为 `Experimental`。正文只吸收长期机制、适用条件
和反例边界，不吸收作者峰值 benchmark，也没有新增 Part、章节或 ROADMAP 节点。

## 1. 模型与研究机构

### Source Coverage

按 `CODEX_DAILY_RESEARCH_PROMPT.md` 的固定顺序检查：

- **OpenAI — No Material Update**
- **Anthropic — No Material Update**
- **Apple Machine Learning Research — No Material Update**
- **Google DeepMind — No Material Update**
- **Google Research — No Material Update**
- **Meta AI / FAIR — No Material Update**
- **Microsoft Research — No Material Update**
- **NVIDIA Research — No Material Update**
- **xAI News / Model Cards — No Material Update**
- **Amazon Science / AGI — No Material Update**
- **Cohere Labs — No Material Update**
- **Ai2 — No Material Update**
- **Mistral AI — No Material Update**
- **Alibaba Qwen — No Material Update**
- **DeepSeek — No Material Update**
- **Moonshot AI / Kimi — No Material Update**
- **Zhipu AI — No Material Update**
- **MiniMax — No Material Update**
- **ByteDance Seed / Research — No Material Update**
- **Baidu ERNIE — No Material Update**
- **Tencent Hunyuan — No Material Update**
- **Huawei Noah's Ark Lab / Pangu — No Material Update**
- **Shanghai AI Laboratory / InternLM — No Material Update**
- **StepFun — No Material Update**
- **Xiaomi MiMo — No Material Update**
- **InclusionAI / Ant Group — No Material Update**
- **Hugging Face Blog — No Material Update**

搜索结果中的旧文章重收录、模型榜单、partner marketing 与缺少 technical report、model card、
system card 或论文的功能 headline 均未进入候选。

### Candidate Scoring

本组无达到候选门槛的窗口内新事件。

## 2. arXiv / 学术来源

### Source Coverage

按 primary-source 顺序检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`stat.ML`，
并按关键词扩展到 `cs.PF`、`cs.CR`、`cs.MA`；同时检查 OpenReview/TMLR、Hugging Face Daily
Papers，并用 Google Scholar、Semantic Scholar、OpenAlex 与 DBLP 做 metadata、identifier、
作者和 first-public date 的 discovery / cross-check。后四者不替代论文正文或 arXiv revision
history。

三项 Deep Analysis 均读取 arXiv HTML 的 metadata、Introduction/Background、Method、公式与系统
结构、Implementation、Evaluation setup、baselines/ablation、limitations、Conclusion 及影响核心
结论的 appendix。无法披露的 workload 字段标为 `Not Disclosed`，不从实验结果反推生产 contract。

### Candidate Scoring

评分维度依次为 Technical Novelty（TN）、System Impact（SI）、Practical Value（PV）、Source
Reliability（SR）、Project Relevance（PR）、Longevity（L），每项 0～5。

| Candidate | TN | SI | PV | SR | PR | L | Total | Evidence / Action |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| AFD-Ledger: A/F deployment provisioning | 5 | 5 | 5 | 4 | 5 | 5 | 29 | Experimental；Refine Ch51 |
| Adam basis dependence | 5 | 5 | 4 | 4 | 5 | 5 | 28 | Experimental；Refine Ch24 |
| Argus agentic runtime | 4 | 5 | 4 | 4 | 5 | 4 | 26 | Experimental；No Change Ch77 |
| SafeCommit: memory-grounded action certification | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Must Read；Weekly source-family |
| CommBench: GPU communication code | 4 | 4 | 4 | 4 | 4 | 4 | 24 | Must Read；Weekly source-family |
| Architectural implications of Agentic workflows | 4 | 4 | 3 | 4 | 4 | 4 | 23 | Watch；未完成全文 Source Packet |
| Hierarchical Graph Memory | 4 | 4 | 3 | 4 | 4 | 4 | 23 | Watch；未完成全文 Source Packet |

`SR=4` 表示可以直接访问作者 preprint 与 metadata，但尚未 peer review；它不是对结论真实性或
production readiness 的满分背书。

### Deep Analysis 1 — AFD-Ledger

**Primary source:** arXiv:2608.04502v1，first public 2026-08-05。
**Evidence Level:** Experimental / analytical planner + three bounded physical validations。
**Knowledge Tree:** Ch51 PD/A/F disaggregation（owner）→ Ch52 scheduling → Ch59 placement。

#### Why

AFlex、HeteroPanacea 等工作可以展示 A/F pool 的局部 kernel、energy 或 simulator gain，却没有
自动回答部署问题：在相同模型、流量、TPOT SLO、总设备预算和可选 hardware catalog 下，独立
优化后的最佳 A/F plan 是否真的优于独立优化后的最佳 co-located plan。拿新架构对比一个固定而
较弱的 baseline，会把 provisioning quality 误写成 architecture advantage。

#### Principle

局部机制必须经过 full-budget accounting 才能转化为 deployment gain：

```text
best feasible disaggregated plan under contract Omega
vs.
best feasible co-located plan under the same contract Omega
```

`Omega` 至少包含 model、workload、input/output contract、TPOT SLO、budget、hardware catalog 与
runtime capability。A/F 分池还会产生 request-bearing-capacity tax：FFN-only device 不再保存
完整 request/KV state，移除 expert memory 或扩大 batch 的收益必须先偿还 resident request
capacity 的损失。

#### Mechanism

AFD-Ledger 使用 role-specific analytical estimator 生成 hardware pair 候选，通过反馈 refinement
减少需要完整求解的组合，再对候选执行 replica、parallelism、placement、queue 与 budget 的完整
provisioning。搜索与最终计划被分开：前者减少 evaluation cost，后者才判断 SLO-feasible decode
throughput。

论文分析 Qwen3-235B-A22B 与 DeepSeek-V3.2。披露的 workload table 包含 1K/4K input、多个
TPOT SLO 与 32/48/64 GPU budgets；作者还在三组 LongCat 2.0 physical deployments 上检查
architecture decision 和预测误差。作者报告的搜索减少比例、吞吐比与预测误差只属于这些
model、hardware catalog、budget 与 SLO 组合，未写入 Books 的通用结论。

#### Trade-off

- Replica、worker ratio 与 device count 是离散变量，会形成 threshold 与 near tie；局部 gain 不会
  平滑转化为部署 gain。
- Analytical planner 依赖 profile accuracy 与有限 catalog；物理验证误差不是跨环境置信区间。
- 论文只比较新建、saturated、steady-state decode service；installed-hardware reuse、elasticity、
  failure isolation、tail behavior 与 catalog drift 不在证明范围。
- 当方案差距小于模型误差时，应保留为 near tie，并由 replay、canary 与 telemetry 裁决。

#### Connection / Evolution

这是 Ch51 的 `Direct Refinement`：AFlex 提供有限平台实现，HeteroPanacea 提供更宽 architecture
space 的 simulation，AFD-Ledger 则补充 fair provisioning/accounting。三者不是单向替代：

```text
operator/pool local gain
→ conditional execution-graph factorization
→ same-contract best-vs-best provisioning
→ physical replay / canary / telemetry
```

Co-location、P/D 与 A/F/PDAF 仍分别在规模、interference、link、state ownership 和预算条件不同
时成立。

### Deep Analysis 2 — The Loss Does Not See the Basis, but Adam Does

**Primary source:** arXiv:2608.05136v1，first public 2026-08-05 17:56:26 UTC。
**Evidence Level:** Experimental / theorem + matrix-sensing experiments + bounded Transformer probes。
**Knowledge Tree:** Ch24 Pretraining（owner）→ Ch4 Learning → Ch26 LoRA/PEFT。

#### Why

训练文档常把 optimizer 写成 loss 之后可独立选择的更新器。但对 `W=UV^T`，任意正交矩阵 `Q`
都满足 `(UQ)(VQ)^T=UV^T`：两组参数表达相同函数和 loss。真正的问题是 optimizer 是否也把它们
视为同一个表示，还是因 coordinate system 不同而选择不同 interpolant。

#### Principle

只有对 gauge transformation 保持 equivariance 的 optimizer，才可能把 gradient flow 的某些
pathwise / implicit-bias 性质迁移到不同 basis；这是必要而非充分条件。Coordinate-wise second-
moment preconditioning 会在 basis rotation 后改变坐标统计，因此同一 `W` 和 loss 可以走出不同
的 function-space trajectory。

#### Mechanism

论文给出 first-step defect、equivariant update 的结构刻画与 transfer theorem，并比较九种更新
规则。作者把 Gradient Descent、momentum、shared-scalar Adam、Muon 与 Shampoo 归为满足相应
equivariance 的规则，把 Adam、RMSProp、Adafactor 等 coordinate-wise 方法归为破坏该对称性的
规则。实验使用 underdetermined matrix sensing、synthetic 与 hyperspectral data，另在 appendix
提供 H100 replication 与 character language-model / Transformer twin probes。

#### Trade-off

- 所有方法都可能达到很低 train loss，而 planted recovery 或 held-out error 不同；loss equality
  不是 trajectory equivalence。
- Equivariance 不是 generalization 或 low-rank recovery 的充分条件；任务需要更强 regularization
  或 per-coordinate adaptation 时，非 equivariant 方法仍可能更合适。
- 理论核心针对 factored matrix sensing；stochastic minibatch interaction 尚未被完整刻画。
- Transformer probes 不能证明 Adam 在一般 LLM Pretraining 中更差，也不能支持全局替换建议。

#### Connection / Evolution

Ch24 过去只说明 Adam state 与 schedule 会改变 trajectory。本次 refine 把 optimizer、
parameterization、initialization、data order 与 schedule 合并为训练身份，并增加 symmetry-twin
验证方法。它属于 `Principle Reuse`，不是把 matrix-sensing 结果外推到所有 Transformer。

### Deep Analysis 3 — Argus

**Primary source:** arXiv:2608.05144v1，first public 2026-08-05 17:58:58 UTC。
**Evidence Level:** Experimental / multi-arena technical report / evolving logging contract。
**Knowledge Tree:** Ch77 Workflow（owner candidate）→ Ch73 Memory → Ch62 Evaluation。

#### Why

Long-horizon Agent 不能依赖单次 context 完成工作，需要在多次 bounded missions 之间保留项目状态，
在证据支持时继续，在 verifier 或 hidden constraint 暴露失败时回退或换路。问题本质是运行时如何
拥有 accepted frontier，而不是如何延长一条 prompt。

#### Principle

Argus 把 model parameters `theta` 与 runtime state 分离。Manager 拥有 authority，Planner 生成有
依赖关系的 bounded tasks，Engineer 产生 artifact，Reviewer 决定 candidate state 是否进入
accepted frontier。Stage 只允许 hold、前进到相邻 stage 或 rollback；完整 event stream 与有界
working checkpoint 分离，进展也不要求每个 transition 单调。

#### Mechanism

Shared workspace 持久化 knowledge、artifacts、backlog、budget、daemon 与 memory。Execution 产生
candidate update，review gate 才 commit retained form。论文覆盖 software repair、GPU kernel、LM
training、training speed、research assistant 与 data synthesis 等七个 arenas，并保留各自 native
metric；它没有构造一个可以跨任务直接比较的统一 leaderboard。

#### Trade-off

- Reviewer 是 selective error-correction layer，不是 correctness oracle；false acceptance 会污染
  accepted state，false rejection 会阻断探索。
- 六个 paper projects 共用一个环境，campaign hours 存在重叠，review snapshots 由模型生成，
  logging contract 也在演进。
- 结果证明 bounded lifecycle、recovery 与 artifact production，不证明论文会被接受、产生科学
  novelty、优于人类，或达到未测量的 zero-touch autonomy。
- 成本比较缺少某些 baseline 的原始 per-wave traces，不能把 aggregate token ratio 泛化。

#### Connection / Evolution

Ch77 已经明确 Workflow 是 durable control plane，包含 authoritative event/state、deterministic
spine、agentic nodes、retry/replay、approval/authority、evaluator-driven search 与 rollback。Argus
提供了 `Explanatory Case`，但没有形成稳定机制缺口。因此 disposition 为 `No Change — Already
Covered`，以免按角色名重复书稿。

### Evidence Level

- **官方事实**：论文 title、authors、v1 time 与 revision history 来自 arXiv metadata；工程版本
  日期与 changed items 来自官方 GitHub Release。
- **论文实验结论**：mechanism、evaluation contract、limitations 与 benchmark 均按作者正文记录，
  只绑定披露条件。
- **自己的推断**：Ch24/Ch51 ownership、Argus 去重、evolution relationship 与 Books disposition
  是本仓库 integration judgment。
- **不得推断**：不能把 matrix-sensing 结论写成 Adam 的通用失败，不能把 planner prediction
  当 production guarantee，也不能从 Agent benchmark 反推内部模型能力或 deployment autonomy。

## 3. AI Infra 与工程项目

### Source Coverage

按固定顺序检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、
Ray、KServe、Kubeflow、Kubernetes、Hugging Face Transformers、Hugging Face Accelerate、
DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

| Candidate | TN | SI | PV | SR | PR | L | Total | Evidence / Action |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| KServe v0.20.0 | 3 | 4 | 5 | 5 | 5 | 3 | 25 | Version Fact；Weekly Source Family |
| Dynamo v1.3.1 | 2 | 4 | 4 | 5 | 5 | 3 | 23 | Version Fact；Record Only |
| DeepSpeed v0.19.4 | 2 | 3 | 4 | 5 | 4 | 2 | 20 | Version Fact；Record Only |
| Kubernetes v1.37.0-rc.0 | 2 | 3 | 3 | 5 | 3 | 2 | 18 | Pre-release；Ignored |

- **KServe v0.20.0** 的 Release 同时包含 model-based routing gates/status、KV cache CPU/secondary
  filesystem tiers、traffic splitting/group readiness、distributed tracing API、Managed DRA、
  canary rollout、llm-d/Gateway upgrades 与多项 correctness fixes。它证明版本表面与 integration
  direction，不证明这些能力已经形成一个统一、稳定、跨 runtime 的 serving contract。W32 将按
  source family 阅读相关 PR、API types、controller path、migration 与 E2E evidence 后再决定 Books。
- **Dynamo v1.3.1** 修复 GB200 上 SGLang disaggregated serving 通过 AWS EFA 时的 KV-transfer
  stall，并固定 NIXL 1.3.2、EFA Installer 1.49.0。Release 同时保留 intermittent silent stall 与
  GPU/EFA PCIe-topology mismatch 等 known issues，说明 data-path health 不能替代 request completion
  与 topology-aware allocation。该结论已被 Ch51 的 handoff correctness/failure boundary 覆盖，
  不追加版本事实。
- **DeepSpeed v0.19.4** 的 AutoTP/ZeRO-3 inference、scheduler validation 与 MoE 修复属于 patch
  facts，尚未形成新长期机制。
- 其余项目未发现窗口内改变 correctness、state ownership、failure semantics 或 SLO contract 的
  正式 Release/RFC。Nightly、rolling build、dependency bump 与未合并 PR 不进入 Books。

## Knowledge Tree Position

| Candidate | Primary Owner | Target and adjacent chapters read | Books decision |
| --- | --- | --- | --- |
| AFD-Ledger | Ch51 PD 分离 | Ch50～52；核对 Ch59 placement boundary | Refine — Existing Argument |
| Adam basis dependence | Ch24 Pretraining | Ch23～25；核对 Ch4/Ch26 boundary | Integrate — New Mechanism |
| Argus | Ch77 Workflow | Ch76～78；核对 Ch62/Ch73 boundary | No Change — Already Covered |
| KServe v0.20.0 | Ch58 KServe，待 W32 Source Packet | Ch52、Ch57～59 | Weekly Only — Version Fact |
| Dynamo v1.3.1 | Ch48 Dynamo / Ch51 handoff | Ch47～52 | No Change — Already Covered |

没有新增 ROADMAP node、Part 或章节。每项知识只有一个主 owner；Release 中跨多个 subsystem 的
能力不会被压缩成一个未经验证的通用设计结论。

## Recommended Action

- 已 refine Ch51：加入同 contract、best-vs-best 的 full provisioning、request-bearing-capacity tax、
  near-tie 与 physical validation boundary。
- 已 refine Ch24：加入 optimizer/parameterization symmetry contract、coordinate-wise basis
  dependence 与 symmetry-twin engineering check。
- Argus 作为 Ch77 的 chapter-level dedup evidence 保留，不复制 Manager/Planner/Engineer/Reviewer
  taxonomy 或作者 benchmark。
- KServe v0.20.0 已在 2026-08-13 完成 official release boundary review；多个 change families 只作为
  Version Fact，不推断默认行为或 production correctness。
- SafeCommit、CommBench 与 Hierarchical Graph Memory 已完成全文 Source Packet；分别为 Ch68 refine
  candidate、Ch62 No Change、Ch73 refine candidate，均未写 Books。

## Books Integration

### Absorbed

- `books/part-03-training-system/24-pretraining.md`：补充 optimizer 与 parameterization 联合决定
  trajectory、gauge equivariance、适用边界与 symmetry-twin 验证。
- `books/part-04-inference-system/51-pd-disaggregation.md`：补充局部 A/F gain 到完整 deployment
  provisioning 的 accounting layer、request-bearing-capacity tax 与 near-tie handling。
- `docs/LEARNING_STATE.md`：同步两项稳定认知与 Experimental evidence boundary。

### Not Absorbed

- **Argus**：Ch77 已有 durable state、bounded workflow、review gate、event log、retry/replay、
  authority 与 rollback；新增案例不足以改变设计结论。
- **KServe v0.20.0**：official signed release、tag commit 与 linked change list 已核验；一个 Release
  汇集多条独立机制，因此仍只记录 Version Fact，不把功能表变成统一架构结论。
- **Dynamo v1.3.1**：修复和 known issues 是重要版本/兼容性事实，但 Ch51 已覆盖 handoff completion、
  network topology 与 failure semantics，不把 version matrix 写入长期正文。
- **SafeCommit / CommBench / HiGram**：2026-08-13 已完成全文 Source Packet；作者 controlled simulator、
  benchmark hardware 与 memory benchmark 仍是受限证据，Historical Books Gate 关闭。

## Ignored Noise

- 模型榜单、community challenge、partner marketing 与缺少 primary technical evidence 的 headline。
- arXiv recent 中仅增加 benchmark、缺少机制或与 AI System Design 关联弱的条目。
- 缺少 model、hardware、precision、input/output、batch、concurrency 与 SLO contract 的性能宣传。
- GitHub nightly、dependency bump、rolling build、未合并 PR、未来 roadmap 与搜索引擎重收录。
- Kubernetes release candidate 与普通 patch 未被描述成稳定生产能力。

## Repository Changes

- 新增 `papers/2026/08/07/README.md`。
- Refine Ch24、Ch51，并同步 `docs/LEARNING_STATE.md`。
- 未修改 ROADMAP 或 `docs/DECISIONS.md`；未生成 provisional `2026-W32`。
- 运行前已有 Books、ADR、Learning State、interview 与 8 月 4～6 日 Daily 修改均保留；未执行
  stage、unstage、commit、push、reset、checkout 或 clean。

## Recovery Addendum — 2026-08-13

- SafeCommit：plausible-world conformal support、all-world safety certificate、probe/fallback 与 controlled
  benchmark 已核验；主 owner Ch68，Experimental。
- CommBench：100+ communication tasks、compile/correctness/performance harness 与 B300/GH200/MI325X
  contracts 已核验；Ch62 已覆盖，No Change。
- HiGram：hierarchical graph、path localization、coordinated rewrite、LoCoMo/MemConflict 与 provenance/
  concurrency 缺口已核验；主 owner Ch73，Experimental。
- KServe v0.20.0：release `1fb7810` 的版本边界已核验；Weekly Only。

## Open Questions

1. AFD-Ledger 的 planner 在 bursty arrivals、prefix cache、tail SLO、elastic scaling 与 failure
   recovery 下是否仍能保持 architecture decision stability？
2. Request-bearing-capacity tax 怎样与 installed-hardware reuse、mixed tenancy 和 power cap 一起计量？
3. Gauge equivariance 与 stochastic minibatch、distributed sharding、mixed precision 以及 real LLM
   factorized modules 的交互是什么？
4. Symmetry-twin divergence 应用 function distance、held-out quality 还是 optimizer-state distance 作为
   deployment-relevant signal？
5. Argus 的 Reviewer false-accept/false-reject operating point、state supersession 与 delete/rollback
   contract 如何独立评估？
6. KServe v0.20.0 的 routing gate、KV tiering、traffic split 与 readiness condition 在 rollback、
   migration 和 multi-controller failure 时分别由谁拥有？
7. Dynamo 的 silent EFA stall 如何在 HTTP success、zero-token completion 与 backend telemetry 之间
   建立端到端 completion invariant？

## Sources

访问日期均为 2026-08-07；论文日期为 arXiv first-public date，Release 日期为官方页面日期。

### Model and Institution Sources

- OpenAI Research: https://openai.com/research/
- Anthropic Research: https://www.anthropic.com/research
- Apple Machine Learning Research: https://machinelearning.apple.com/
- Google DeepMind: https://deepmind.google/blog/
- Google Research: https://research.google/blog/
- Meta AI: https://ai.meta.com/blog/
- Microsoft Research: https://www.microsoft.com/en-us/research/blog/
- NVIDIA Research: https://research.nvidia.com/
- xAI News: https://x.ai/news
- Amazon Science: https://www.amazon.science/
- Cohere Labs: https://cohere.com/research
- Ai2 Papers: https://allenai.org/papers
- Mistral AI Research: https://mistral.ai/research
- Alibaba Qwen: https://qwenlm.github.io/
- DeepSeek: https://api-docs.deepseek.com/news/
- Moonshot AI / Kimi: https://www.kimi.com/
- Zhipu AI: https://www.zhipuai.cn/
- MiniMax: https://www.minimaxi.com/news
- ByteDance Seed: https://seed.bytedance.com/
- Baidu ERNIE: https://ernie.baidu.com/blog/zh/publication/
- Tencent Hunyuan: https://github.com/Tencent-Hunyuan
- Huawei Noah's Ark Lab: https://noahlab.com.hk/
- Shanghai AI Laboratory: https://www.shlab.org.cn/
- StepFun Research: https://www.stepfun.com/research
- Xiaomi MiMo: https://mimo.xiaomi.com/
- InclusionAI: https://www.inclusion-ai.org/publication/
- Hugging Face Blog: https://huggingface.co/blog

### Academic Sources

- AFD-Ledger metadata（2026-08-05）: https://arxiv.org/abs/2608.04502
- AFD-Ledger full HTML: https://arxiv.org/html/2608.04502
- Adam basis dependence metadata（2026-08-05）: https://arxiv.org/abs/2608.05136
- Adam basis dependence full HTML: https://arxiv.org/html/2608.05136
- Argus metadata（2026-08-05）: https://arxiv.org/abs/2608.05144
- Argus full HTML: https://arxiv.org/html/2608.05144
- SafeCommit metadata: https://arxiv.org/abs/2608.04289
- CommBench metadata: https://arxiv.org/abs/2608.04450
- Architectural Implications of Agentic AI Workflows metadata: https://arxiv.org/abs/2608.04458
- Hierarchical Graph Memory metadata: https://arxiv.org/abs/2608.05095
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent: https://arxiv.org/list/cs.DC/recent
- arXiv cs.IR recent: https://arxiv.org/list/cs.IR/recent
- arXiv stat.ML recent: https://arxiv.org/list/stat.ML/recent
- OpenReview: https://openreview.net/
- TMLR submissions: https://openreview.net/submissions?venue=TMLR
- Hugging Face Daily Papers: https://huggingface.co/papers
- Google Scholar: https://scholar.google.com/
- Semantic Scholar: https://www.semanticscholar.org/
- OpenAlex: https://openalex.org/
- DBLP: https://dblp.org/

### Engineering Sources

- PyTorch Releases: https://github.com/pytorch/pytorch/releases
- JAX Releases: https://github.com/jax-ml/jax/releases
- CUDA Toolkit Release Notes: https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html
- Triton Releases: https://github.com/triton-lang/triton/releases
- vLLM Releases: https://github.com/vllm-project/vllm/releases
- SGLang Releases: https://github.com/sgl-project/sglang/releases
- Dynamo v1.3.1（2026-08-06）: https://github.com/ai-dynamo/dynamo/releases/tag/v1.3.1
- TensorRT-LLM Releases: https://github.com/NVIDIA/TensorRT-LLM/releases
- Ray Releases: https://github.com/ray-project/ray/releases
- KServe v0.20.0（2026-08-06）: https://github.com/kserve/kserve/releases/tag/v0.20.0
- Kubeflow Releases: https://github.com/kubeflow/community-distribution/releases
- Kubernetes Releases: https://github.com/kubernetes/kubernetes/releases
- Hugging Face Transformers Releases: https://github.com/huggingface/transformers/releases
- Hugging Face Accelerate Releases: https://github.com/huggingface/accelerate/releases
- DeepSpeed Releases: https://github.com/deepspeedai/DeepSpeed/releases
- Megatron-LM Releases: https://github.com/NVIDIA/Megatron-LM/releases
- Unsloth Releases: https://github.com/unslothai/unsloth/releases
- MLX Releases: https://github.com/ml-explore/mlx/releases
- llama.cpp Releases: https://github.com/ggml-org/llama.cpp/releases
- ONNX Runtime Releases: https://github.com/microsoft/onnxruntime/releases
- OpenXLA Releases: https://github.com/openxla/xla/releases
