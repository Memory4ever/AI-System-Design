# AI Research Weekly — 2025-W41

> Coverage Window: 2025-10-06～2025-10-12
> Research Mode: Retrospective Backfill / Full Historical Discovery Replay
> Accessed and Re-audited: 2026-08-24
> Archive Status: W41 Evidence Gate Passed; Historical Books Gate Closed

## Executive Summary

W41 不是 No Material Update。按机构、逐日 arXiv/学术索引及 AI Infra 官方源重放后，共闭合 55 个唯一 Source Family：27 个高分候选、11 个中分候选和 17 个低分候选。38 个 `20+` 候选均完成独立 Full Source Review，17 个低分候选均完成 identity、v1 日期、评分与拒绝理由核验；`Review Pending = 0`，`Unverified / Blocked = 0`。

本周的长期主线不是单一模型发布，而是三条相互连接的系统演进：

```text
静态 prompt / monolithic rewrite
→ 可寻址、增量更新的 context state
→ 从 execution trace 中反思与修订

expert demonstration
→ agent 自己产生的 early experience
→ future state supervision / implicit world model
→ 后续 reward-driven learning

单一 modality 或单一生成目标
→ shared / continuous representation
→ understanding、generation 与 action 的联合训练
→ 状态 identity、控制频率和安全边界成为系统契约
```

官方事件中，Codex GA 只证明产品与接口可用性；Google 的 AI security strategy 和 OpenAI 的 political-bias evaluation 提供的是 threat-model / evaluator contract，均不能反推未公开的模型或 runtime 内部机制。AI Infra 固定项目扫描未发现归属本周、且能形成独立长期机制结论的 release/RFC/PR。

## Coverage Window and Limitations

- ISO 周窗口为 Monday 2025-10-06 00:00:00 至 Sunday 2025-10-12 23:59:59；论文按 arXiv v1 UTC 时间归档，官方事件按公开发布日期归档。
- 当前 arXiv HTML 可能是后续 revision。每项 review 都回看 abstract 页 submission history；后续 revision 只用于理解机制与局限，不作为新的 W41 事件。
- Google Scholar、OpenAlex、DBLP、Semantic Scholar、Hugging Face Daily Papers 和 Crossref 只承担 discovery、identity 与去重；机制结论回到 arXiv HTML/PDF、官方 report、官方 repo 或官方公告。
- 历史回填不补造 Daily。W42 feed/history 中 first-public 属 W41 的 21 个 family 已回拨；其 revision 不在 W42 重复计分。
- 作者 benchmark 只在论文披露的模型、数据、evaluator 与实验配置内成立。硬件、precision、length、batch、concurrency 或 SLO 未披露时统一记录 `Not Disclosed`，不外推为生产结论。
- 本轮未使用 Scholar/OpenAlex 导出证明召回绝对完备；Gate 证明固定源、相邻周与已知 spillback 已闭合，而不是证明互联网不存在其他论文。

## 1. 模型与研究机构

### Source Coverage

按 OpenAI → Anthropic → Google/DeepMind → Meta → Microsoft → NVIDIA → Amazon → Apple → Alibaba/Qwen → Baidu → Tencent → ByteDance → Mistral → Cohere → xAI → Hugging Face 顺序扫描官方 Blog、report、system/model card 与 release。

- OpenAI：保留 Codex GA 的版本事实与 political-bias evaluation 的 evaluator contract。
- Google：保留 AI security frontier strategy / SAIF 2.0 的分层防御框架；CodeMender 只作为公开工程能力事实，不推断内部 agent 实现。
- Anthropic CTO 任命、Google September roundup 等不改变 AI System 机制 contract，归入 Ignored Noise。
- 其余机构本窗口未发现同时满足事件日期、primary-source 和项目相关性门槛的新机制证据。

## 2. 论文与学术来源

### Source Coverage

逐日重放 2025-10-06～10-10 的 arXiv / Hugging Face discovery 页，并向前检查 10-13/10-14 feed 以恢复延迟入榜但 v1 属 W41 的项目；再以 OpenAlex、DBLP、Crossref 与作者项目页交叉 identity。共形成 52 个论文 Source Family：35 个进入 Full Source Review，17 个在 Low-Score Closure 闭合。

重点覆盖：context adaptation、agent learning/tool use、安全与 executable evaluation、RL data/objective、hybrid sequence architecture、multimodal representation/generation、VLA/world model、long-context state 与 benchmark temporal validity。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch、JAX/TensorFlow、CUDA/Triton、vLLM、SGLang、TensorRT-LLM、Dynamo、DeepSpeed、Megatron-Core、Ray、Kubernetes/KServe/Kubeflow、Volcano/KAI Scheduler 的 release、RFC、PR 与 design document 顺序扫描。

- 未发现 first-public 属 W41、且达到 `20/30` 的独立工程 release/RFC/PR。
- vLLM v0.11.0 属 W40；PyTorch 2.9 及后续工程事件属 W42，不回拨。
- 论文中的 artifact 只用于核验对应 paper family，不另建一条工程候选。

## Candidate Scoring

| Candidate / Source Family | First-public | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Final Weekly Disposition |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| OpenAI Codex GA / `official:openai:codex-ga-2025-10-06` | 10-06 | 3 | 4 | 4 | 5 | 3 | 3 | 22 | Weekly Only — Version Fact / Mechanism Not Disclosed |
| Google AI security frontier strategy / `official:google:saif2-2025-10-06` | 10-06 | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Books Pending — source family gate passed |
| OpenAI political-bias evaluation / `official:openai:political-bias-eval-2025-10-09` | 10-09 | 4 | 4 | 4 | 5 | 4 | 4 | 25 | Books Pending — source family gate passed |
| Agentic Context Engineering / `arxiv:2510.04618` | 10-06 | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Books Pending — source family gate passed |
| Hybrid Architectures for Language Models / `arxiv:2510.04800` | 10-06 | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Books Pending — source family gate passed |
| Reinforce-Ada / `arxiv:2510.04996` | 10-06 | 5 | 5 | 4 | 5 | 4 | 3 | 26 | Books Pending — source family gate passed |
| Watch and Learn / `arxiv:2510.04673` | 10-06 | 4 | 5 | 4 | 5 | 4 | 4 | 26 | Books Pending — source family gate passed |
| Multi-Agent Tool-Integrated Policy Optimization / `arxiv:2510.04678` | 10-06 | 5 | 5 | 4 | 5 | 4 | 3 | 26 | Books Pending — source family gate passed |
| BIRD-INTERACT / `arxiv:2510.05318` | 10-06 | 4 | 5 | 5 | 5 | 4 | 3 | 26 | Books Pending — source family gate passed |
| Context Denoising Training / `arxiv:2510.05862` | 10-07 | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Books Pending — source family gate passed |
| In-the-Flow Agentic System Optimization / `arxiv:2510.05592` | 10-07 | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Books Pending — source family gate passed |
| D2E / `arxiv:2510.05684` | 10-07 | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Books Pending — source family gate passed |
| TaTToo / `arxiv:2510.06217` | 10-07 | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Books Pending — source family gate passed |
| Asymmetric Ratios for Outcome-Supervised RL / `arxiv:2510.06062` | 10-07 | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Books Pending — source family gate passed |
| Lumina-DiMOO / `arxiv:2510.06308` | 10-07 | 4 | 5 | 4 | 5 | 4 | 4 | 26 | Books Pending — source family gate passed |
| Webscale-RL / `arxiv:2510.06499` | 10-07 | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Books Pending — source family gate passed |
| Ming-UniVision / `arxiv:2510.06590` | 10-08 | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Books Pending — source family gate passed |
| RLinf-VLA / `arxiv:2510.06710` | 10-08 | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Books Pending — source family gate passed |
| SWE-IF / `arxiv:2510.07315` | 10-08 | 4 | 4 | 5 | 5 | 4 | 3 | 25 | Books Pending — source family gate passed |
| Artificial Hippocampus Networks / `arxiv:2510.07318` | 10-08 | 4 | 5 | 4 | 5 | 4 | 4 | 26 | Books Pending — source family gate passed |
| Native Hybrid Attention / `arxiv:2510.07019` | 10-08 | 4 | 4 | 4 | 5 | 4 | 4 | 25 | Books Pending — source family gate passed |
| When Benchmarks Age / `arxiv:2510.07238` | 10-08 | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Books Pending — source family gate passed |
| TTRV / `arxiv:2510.06783` | 10-08 | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Books Pending — source family gate passed |
| WristWorld / `arxiv:2510.07313` | 10-08 | 4 | 4 | 3 | 5 | 4 | 3 | 23 | Books Pending — source family gate passed |
| Your Harness is Not Secure / `arxiv:2510.06607` | 10-08 | 4 | 5 | 4 | 5 | 4 | 4 | 26 | Books Pending — source family gate passed |
| When Thoughts Meet Facts / `arxiv:2510.07499` | 10-08 | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Books Pending — source family gate passed |
| Hybrid Reinforcement / `arxiv:2510.07242` | 10-08 | 4 | 5 | 4 | 5 | 4 | 4 | 26 | Books Pending — source family gate passed |
| Learning to Route LLMs from Bandit Feedback / `arxiv:2510.07429` | 10-08 | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Books Pending — source family gate passed |
| Agent Learning via Early Experience / `arxiv:2510.08558` | 10-09 | 5 | 5 | 5 | 5 | 5 | 4 | 29 | Books Pending — source family gate passed |
| MM-HELIX / `arxiv:2510.08540` | 10-09 | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Books Pending — source family gate passed |
| UniVideo / `arxiv:2510.08377` | 10-09 | 4 | 5 | 4 | 5 | 4 | 4 | 26 | Books Pending — source family gate passed |
| DeepPrune / `arxiv:2510.08483` | 10-09 | 4 | 4 | 3 | 5 | 4 | 3 | 23 | Books Pending — source family gate passed |
| First Try Matters / `arxiv:2510.08308` | 10-09 | 4 | 4 | 3 | 5 | 3 | 3 | 22 | Books Pending — source family gate passed |
| Learning on the Job / `arxiv:2510.08002` | 10-09 | 5 | 5 | 4 | 5 | 5 | 4 | 28 | Books Pending — source family gate passed |
| Memory Retrieval and Consolidation in LLMs through Function Tokens / `arxiv:2510.08203` | 10-09 | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Books Pending — source family gate passed |
| Thinking with Camera / `arxiv:2510.08673` | 10-09 | 5 | 5 | 4 | 5 | 4 | 4 | 27 | Books Pending — source family gate passed |
| BigCodeArena / `arxiv:2510.08697` | 10-09 | 4 | 5 | 5 | 5 | 4 | 3 | 26 | Books Pending — source family gate passed |
| OpenRubrics / `arxiv:2510.07743` | 10-09 | 4 | 4 | 4 | 5 | 4 | 3 | 24 | Books Pending — source family gate passed |
| LightCache / `arxiv:2510.05367` | 10-06 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — narrow evidence |
| StaMo / `arxiv:2510.05057` | 10-06 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — narrow evidence |
| OBS-Diff / `arxiv:2510.06751` | 10-08 | 3 | 3 | 3 | 4 | 3 | 2 | 18 | Weekly Only — narrow pruning evidence |
| ARMOR / `arxiv:2510.05528` | 10-07 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — insufficient system delta |
| Global Planner Training / `arxiv:2510.05608` | 10-07 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — narrow task evidence |
| LongRM / `arxiv:2510.06915` | 10-08 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — benchmark-bound reward model |
| Training-Free GRPO / `arxiv:2510.08191` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — naming exceeds evidence |
| Alignment Waltz / `arxiv:2510.08240` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — preliminary alignment study |
| NaViL / `arxiv:2510.08565` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — narrow multimodal variant |
| CoMAS / `arxiv:2510.08529` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — system delta not isolated |
| Beyond Turn Limits / `arxiv:2510.08276` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — benchmark-specific |
| A2Search / `arxiv:2510.07958` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — search variant |
| BEAR / `arxiv:2510.08759` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — benchmark family only |
| Which Heads Matter for KV Compression / `arxiv:2510.08525` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — sensitivity result |
| Don't Waste Mistakes / `arxiv:2510.08696` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — training recipe evidence |
| ARES / `arxiv:2510.08457` | 10-09 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — limited generality |
| Speculative Jacobi-Denoising / `arxiv:2510.08994` | 10-10 | 3 | 3 | 3 | 4 | 3 | 3 | 19 | Weekly Only — no independent production evidence |

Scoring review: every row total was recomputed from six dimensions. Thresholds are `25～30 = High`、`20～24 = Medium`、`<20 = Low`；没有用分数替代 evidence boundary。

## Deep Analysis

### 1. Agentic Context Engineering：把 context 从文本变成可演进状态

**Why.** 静态 prompt 易失去新经验；每轮整体重写虽能吸收反馈，却会产生 brevity bias 与 context collapse。旧方案在短任务和小 context 下合理，但当 agent 要跨 episode 保存策略、错误与工具约束时，整段文本不再是安全的更新单元。

**Principle and Mechanism.** ACE 将 context 表示为带 identifier 与 helpful/harmful counters 的 itemized entries。Generator 产生轨迹，Reflector 从成功与失败中抽取局部 delta，Curator 再以确定性 merge、dedup 与 pruning 更新 playbook。状态所有权由“每次让 LLM 重写全部 prompt”转成“结构化 context store 拥有 entry identity；LLM 只提议 delta”。

**Evidence and Boundary.** 论文覆盖 AppWorld、finance、medical、text-to-SQL，比较 ICL、MIPROv2、GEPA、Dynamic Cheatsheet，并提供 ablation、sensitivity、cost/latency 与不同 backbone 检查。收益仍是作者实验；LLM-as-a-judge 的 BIRD-SQL、不同 provider 的价格和 KV reuse 假设不能外推为通用 serving 结论。

**Trade-off and Evolution.** 局部更新降低 destructive rewrite 风险，却新增 entry provenance、conflict、supersession、poisoning、retention 与 delete/rollback 问题。它是 `static context → adaptive context → governed derived memory` 的直接演进，owner 为 `AGENT-MEMORY`。

### 2. D2E：从 desktop observation 扩展到 embodied action 的 schema bridge

**Why.** 机器人 trajectory 稀缺，而 desktop video 丰富；直接把 GUI 像素与 robot action 混合又会遇到 observation/action schema 不一致。旧的单域 imitation 在固定 embodiment 上合理，却难利用跨平台行为数据。

**Principle and Mechanism.** D2E 以统一 Open World Agent 格式压缩并标准化 observation/action event，Generalist-IDM 从 video 反推动作与时间戳，再用 Visual Action Pre-Training 将 desktop 行为表征迁移到 embodied policy。关键状态不是“视频 token 越多越好”，而是 observation identity、event timestamp、action proposal 与 embodiment-specific controller 的边界。

**Evidence and Boundary.** 论文披露约 1.3K 小时 desktop 数据、多个 embodied benchmark 与 transfer ablation；报告的 LIBERO/CANVAS 成绩只在作者数据、模型、protocol 内有效。camera calibration、real-time control frequency、hardware latency、安全 envelope 和真实部署 SLO 未形成通用证据。

**Trade-off and Evolution.** 桥接 schema 扩大可用行为数据，但 inverse dynamics 伪标签会把不可观测动作和时序误差传播到策略；domain shift 仍需 embodiment adapter 与 closed-loop correction。owner 为 `MULTIMODAL-EMBODIED-VLA`。

### 3. Agent Learning via Early Experience：在 imitation 与 RL 之间增加 future-state supervision

**Why.** expert SFT 只覆盖专家访问过的窄状态；online RL 又需要可靠 reward 和昂贵长 horizon rollout。二者之间缺少一种能让 agent 接触自身分布、但不依赖最终 reward 的学习信号。

**Principle and Mechanism.** agent 执行动作后得到的 future state 本身成为 supervision：implicit world modeling 学习 action-conditioned transition，self-reflection 从 suboptimal action 与后继状态生成修正。数据流由 `expert trajectory → policy` 扩展为 `policy action → environment state → transition/reflection target → updated policy`。

**Evidence and Boundary.** 论文在八类环境与多个模型 family 上评估 effectiveness 和 OOD generalization，并在有 reward 的环境观察 early experience 对后续 RL 的帮助。它没有证明无 reward 的 future state 等价于 task success，也没有消除 environment coverage、simulator bias、unsafe exploration 或 credit assignment。

**Trade-off and Evolution.** 该路线降低对专家 demonstration 和 final reward 的依赖，却新增环境状态版本、trajectory provenance、action consequence 对齐与错误 reflection 的治理成本。owner 为 `AGENT-REFLECTION`。

## Full Source Review

### A. 模型与机构及 10-06～10-07 Source Families

#### OpenAI Codex GA — 22/30

- **Identity / coverage:** 官方公告 2025-10-06；全文可读，无独立 technical report/system card。Source Family `official:openai:codex-ga-2025-10-06`。
- **Mechanism / state / control:** 只证明 CLI、IDE、cloud 与 SDK/Slack integration 的产品可用性；模型、训练数据、runtime、state ownership 与调度均未公开，固定为 `Version Fact / Mechanism Not Disclosed`。
- **Evidence / limits / owner:** 客户陈述不是可复现实验；hardware、model、precision、length、concurrency、SLO 均 `Not Disclosed`。owner `AGENT-PLATFORM`，`Weekly Only`。

#### Google AI security frontier strategy / SAIF 2.0 — 24/30

- **Identity / coverage:** Google 官方 2025-10-06 strategy/tooling 公告与 SAIF 2.0 材料可读；CodeMender 只作同 family 工程能力事实。
- **Mechanism / state / control:** 旧 perimeter control 无法覆盖 model theft、prompt injection、tool misuse 与 autonomous remediation；框架把 threat modeling、system control、monitoring 与 incident response 分层，artifact、identity、permission、telemetry 和 release gate 各有 owner。
- **Evidence / limits / owner:** 材料不证明 CodeMender 内部 agent architecture 或生产效果；新增误报、policy drift、权限升级与自动修复 rollback 风险。owner `PLATFORM-SECURITY`，Books Pending。

#### OpenAI political-bias evaluation — 25/30

- **Identity / coverage:** 官方 evaluation methodology 2025-10-09 可读；它是 evaluator/report family，不是模型发布。
- **Mechanism / state / control:** 单一 aggregate score 会混合 prompt distribution、issue mix、refusal 与 asymmetry；方法拆分 behavior taxonomy、prompt set、grader 与 aggregation，使 claim 绑定 sampling 与 rubric version。
- **Evidence / limits / owner:** 只对所列模型、prompt、grader 与 operating point 成立，不证明“无偏见”，也不能从平均值推断每个 atomic claim。owner `PLATFORM-EVALUATION-SYSTEM`，Books Pending。

#### Agentic Context Engineering — 29/30

- **Identity / coverage:** `2510.04618` v1 2025-10-06，当前 v3 2026-03-29；全文覆盖 method、delta、grow-and-refine、AppWorld/domain evaluation、ablation、sensitivity、cost 与 limitations，作者 repo 可访问。
- **Mechanism / state / control:** Generator、Reflector、Curator 分权；itemized entry 持有 ID 与 feedback counters，delta 由非 LLM merge 写入，替代 monolithic rewrite。旧静态 prompt 在短任务仍更简单。
- **Evidence / limits / owner:** 作者结果支持局部更新降低 context collapse 与适配成本，不证明跨 provider 普适；新增 provenance、conflict、poisoning、pruning 与 rollback。owner `AGENT-MEMORY`，handoff `AGENT-CONTEXT`、`AGENT-REFLECTION`、`AGENT-WORKFLOW`，Books Pending。

#### Hybrid Architectures for Language Models — 27/30

- **Identity / coverage:** `2510.04800` v1 2025-10-06；全文覆盖 attention/SSM background、inter/intra-layer taxonomy、scaling、long-context experiments、ablation 与 limitations。
- **Mechanism / state / control:** attention 提供内容寻址，state-space recurrence 提供线性序列状态；hybrid 将全局 retrieval capacity 与低成本 state update 组合，state owner 分为 attention KV 与 recurrent state。
- **Evidence / limits / owner:** 结果只覆盖所测模型规模、training tokens、length 与 kernels，不能宣布 hybrid 普遍优于 dense attention；新增两类 state、kernel fragmentation、placement 与 checkpoint compatibility。owner `MODEL-TRANSFORMER-LAYER`，Books Pending。

#### Reinforce-Ada — 26/30

- **Identity / coverage:** `2510.04996` v1 2025-10-06；全文覆盖 nonlinear objective、adaptive sampling estimator、baseline、ablation 与 sensitivity。
- **Mechanism / state / control:** 固定 sampling 在非线性 RL objective 下会浪费 rollout；方法按估计样本贡献分配预算。sampler 拥有 proposal distribution，trainer 拥有 policy update 与 importance correction。
- **Evidence / limits / owner:** 作者 reasoning task 支持 sample efficiency，不证明所有 reward/off-policy regime 稳定；新增 estimator bias、feedback loop 与 rare-mode starvation。owner `TRAIN-GRPO`，Books Pending。

#### Watch and Learn — 26/30

- **Identity / coverage:** `2510.04673` v1 2025-10-06；全文覆盖视频数据构建、action inference、agent training、computer-use evaluation 与 limitations。
- **Mechanism / state / control:** 从在线视频恢复 observation/action pairs，将 passive video 变成 demonstrations；data pipeline 拥有 timestamp/alignment，policy 消费规范化 trajectory。
- **Evidence / limits / owner:** 结果支持作者视频域与 benchmark 的迁移，不证明隐藏操作、身份或权限可正确恢复；伪动作标签与 UI/version drift 是 failure mode。owner `TRAIN-DATA`，handoff `AGENT-TOOL-CALLING`、`PLATFORM-SECURITY`，Books Pending。

#### Multi-Agent Tool-Integrated Policy Optimization — 26/30

- **Identity / coverage:** `2510.04678` v1 2025-10-06；全文覆盖 multi-agent formulation、tool-integrated rollout、credit assignment、实验与 limitations。
- **Mechanism / state / control:** 多 agent 协作轨迹与 tool result 一起进入 policy optimization；trajectory store 持有 participant/tool provenance，learner 做 role-conditioned credit。
- **Evidence / limits / owner:** 不证明增加 agent 数量单调获益，也未消除 communication tax、shared-state race 与 tool nondeterminism。owner `AGENT-MULTI-AGENT`，handoff `TRAIN-GRPO`、`AGENT-WORKFLOW`，Books Pending。

#### BIRD-INTERACT — 26/30

- **Identity / coverage:** `2510.05318` v1 2025-10-06；全文覆盖 dynamic interaction benchmark、environment、protocol、metrics、baseline 与 failure analysis。
- **Mechanism / state / control:** Text-to-SQL 从单次 string match 变为 agent 与 database 多轮交互；environment 拥有 schema/data，harness 记录 query、tool error、repair 与 final artifact。
- **Evidence / limits / owner:** 测到的是 model+harness+database opportunity，不是纯模型能力；database version、turn budget、permission 会改变结果。owner `PLATFORM-EVALUATION-SYSTEM`，Books Pending。

#### Context Denoising Training — 24/30

- **Identity / coverage:** `2510.05862` v1 2025-10-07、v2 2025-11-04；全文覆盖 Integrated Gradient noise analysis、Context Denoising Training、四类任务、context-window scaling、ablation 与 limitations。
- **Mechanism / state / control:** 先用 attribution signal 识别对预测有干扰的 contextual noise，再以训练目标强化 critical-token influence；dataset/trainer 持有 noise label 与 attribution version，inference 仍消费完整或受控过滤后的 context。
- **Evidence / limits / owner:** 8B 作者模型与所测任务支持 noise-aware training，不证明 IG score 是普适因果解释，也不能把与 GPT-4o 的单点分数比较外推；误删弱相关事实与 attribution cost 是代价。owner `MODEL-LONG-CONTEXT`，handoff `TRAIN-PRETRAINING`，Books Pending。

#### In-the-Flow Agentic System Optimization — 29/30

- **Identity / coverage:** `2510.05592` v1 2025-10-07；全文覆盖 planning/tool-use co-optimization、online trajectory、training/evaluation、ablation 与 error analysis。
- **Mechanism / state / control:** 沿真实 execution flow 收集 state-action-feedback，联合修订 planner/tool policy；workflow runtime 拥有 environment state，optimizer 消费带 provenance 的 trace。
- **Evidence / limits / owner:** 作者 benchmark 不能把收益归因于单一 model weight；tool availability、timeout、retry 与 evaluator 都是系统变量。owner `AGENT-WORKFLOW`，Books Pending。

#### D2E — 28/30

- **Identity / coverage:** `2510.05684` v1 2025-10-07；全文覆盖 OWA format、Generalist-IDM、VAPT、约 1.3K 小时 desktop corpus、transfer、ablation 与 limitations。
- **Mechanism / state / control:** 统一 observation/action/timestamp schema，将 desktop video 转为 trajectory，再迁移到 embodied controller；data pipeline、policy 与 low-level controller 状态分离。
- **Evidence / limits / owner:** LIBERO/CANVAS 等结果不证明 real-world robot 普适；inverse-dynamics label、calibration、control frequency、latency 与 safety envelope 仍是边界。owner `MULTIMODAL-EMBODIED-VLA`，Books Pending。

#### TaTToo — 27/30

- **Identity / coverage:** `2510.06217` v1 2025-10-07；全文覆盖 tool-grounded PRM、test-time search、tabular benchmarks、ablation 与 cost。
- **Mechanism / state / control:** PRM 绑定 tool execution result 与 table state，对候选步骤评分；search controller 拥有 branch/rollback，tool runtime 拥有事实状态。
- **Evidence / limits / owner:** 表格证据不能外推到开放式工具；tool error、PRM miscalibration 与 search cost 会放大。owner `AGENT-PLANNING`，handoff `PLATFORM-EVALUATION-SYSTEM`，Books Pending。

#### Asymmetric Ratios for Outcome-Supervised RL — 24/30

- **Identity / coverage:** `2510.06062` v1 2025-10-07；全文覆盖 importance-ratio credit pathology、asymmetric correction、theory、experiments、ablation 与 limitations。
- **Mechanism / state / control:** sequence-level outcome reward 下，对好/坏 token 对称 clipping 会误分配 credit；非对称 ratio 调整 positive/negative update 的控制范围。
- **Evidence / limits / owner:** 支持特定 objective 与 policy-lag 下的稳定性，不证明替代 dense process reward；新增 hyperparameter、bias 与 reward-noise sensitivity。owner `TRAIN-PPO`，Books Pending。

#### Lumina-DiMOO — 26/30

- **Identity / coverage:** `2510.06308` v1 2025-10-07；全文覆盖 discrete diffusion architecture、understanding/generation training、benchmark、ablation 与 limitations。
- **Mechanism / state / control:** 统一 discrete diffusion objective 处理 text/image understanding 与 generation，以 iterative denoising 取代纯 causal factorization；sampler 拥有 mask/refinement state。
- **Evidence / limits / owner:** 8B 作者模型不能证明 diffusion 取代 AR；GPT-4.1 judge、sampling steps、resolution 与 hardware 绑定结果。owner `MULTIMODAL-GENERATIVE-PARADIGMS`，Books Pending。

#### Webscale-RL — 27/30

- **Identity / coverage:** `2510.06499` v1 2025-10-07、v2 2026-04-10；全文覆盖 filtering、domain/persona、verifiable QA、quality/leakage checks、Qwen2.5-3B GRPO 与 reproducibility appendix。
- **Mechanism / state / control:** pretraining document 变成 self-contained query+short verifiable answer，source document 与 verifier 定义 reward；pipeline 拥有 provenance/decontamination，trainer 消费闭合 QA。
- **Evidence / limits / owner:** 1.2M/9+ domains 与 token efficiency 是作者配置；verifier bias、contamination、binary-reward shortcut 与 revision drift 限制外推。owner `TRAIN-DATA`，handoff `TRAIN-GRPO`、`PLATFORM-EVALUATION-SYSTEM`，Books Pending。

### B. 10-08～10-10 Source Families

#### Ming-UniVision — 28/30

- **Identity / revision / coverage:** `2510.06590` v1 2025-10-08；全文覆盖 MingTok continuous tokenizer、semantic expansion、unified AR training、understanding/generation evaluation、ablation 与 artifact。
- **Mechanism / state / control:** low-level encoder 保留重建信息，semantic expansion 增加语言对齐，在 shared continuous token space 自回归；token identity 绑定 modality、position 与 codec version。
- **Evidence / limits / owner:** 只支持作者模型内联合训练，不证明 continuous token 普遍优于 discrete codec；resolution、token rate、decoder cost影响结论。owner `MULTIMODAL-REPRESENTATION`，Books Pending。

#### RLinf-VLA — 28/30

- **Identity / revision / coverage:** `2510.06710` v1 2025-10-08；全文覆盖 VLA RL dataflow、rollout/training framework、distributed implementation、robot tasks、ablation 与 limitations。
- **Mechanism / state / control:** environment rollout、reward、advantage、policy update 与 VLA observation/action batching统一；simulator/env state、trajectory buffer 与 learner weights分离。
- **Evidence / limits / owner:** 吞吐与成功率绑定具体 simulator、model、GPU 与 task，不能外推真实机器人；sim-to-real、unsafe exploration 与 sensor latency未解决。owner `MULTIMODAL-EMBODIED-VLA`，Books Pending。

#### SWE-IF — 25/30

- **Identity / revision / coverage:** `2510.07315` v1 2025-10-08；primary title 是 **SWE-IF: Aligning Code Evaluation with Human Preference**，不是 discovery metadata 中误配的 “Vibe Checker”；全文覆盖 benchmark、human preference、baseline 与 agreement。
- **Mechanism / state / control:** code agent evaluation 从 test-pass 单一信号扩展为 executable correctness 与 human preference 分离量度；artifact、test、rubric 与 rater judgement 各有 identity。
- **Evidence / limits / owner:** preference 不等价 correctness，rater disagreement 与 task sampling影响结论；不把 aggregate score 外推为 deployment autonomy。owner `PLATFORM-EVALUATION-SYSTEM`，Books Pending。

#### Artificial Hippocampus Networks — 26/30

- **Identity / revision / coverage:** `2510.07318` v1 2025-10-08；全文覆盖 memory module、long-context training/evaluation、baseline、ablation、complexity 与 limitations。
- **Mechanism / state / control:** 专门 memory state 压缩并选择历史，不让全部 token 保持完整 attention；memory writer/reader 与 base model KV 身份分离。
- **Evidence / limits / owner:** 作者任务不证明任意事实可无损压缩；write error、stale memory、capacity saturation 与 retrieval miss 是新 failure mode。owner `MODEL-LONG-CONTEXT`，handoff `INFER-KV-CACHE`、`INFER-GPU-MEMORY`，Books Pending。

#### Native Hybrid Attention — 25/30

- **Identity / revision / coverage:** `2510.07019` v1 2025-10-08；全文覆盖 hybrid attention operator、训练/推理复杂度、baseline、ablation 与 sensitivity。
- **Mechanism / state / control:** 单一可训练 operator 内组合局部/全局或稀疏/密集路径；routing/mask 决定 token-pair 的计算所有权。
- **Evidence / limits / owner:** kernel、length、model scale 与 training budget决定收益；新增 routing overhead、负载不均和后端支持要求。owner `MODEL-SELF-ATTENTION`，handoff `INFER-TENSORRT-LLM`，Books Pending。

#### When Benchmarks Age — 24/30

- **Identity / revision / coverage:** `2510.07238` v1 2025-10-08；全文覆盖 temporal misalignment setup、factuality datasets、model comparison、statistics 与 limitations。
- **Mechanism / state / control:** benchmark item 绑定 knowledge cutoff、fact-valid interval 与 evaluation time，否则 score 混合 model capability、training recency 与 answer freshness。
- **Evidence / limits / owner:** 只证明所测 factuality set 有时间漂移，不证明所有 benchmark 同速老化；web revision 与 contamination仍难分离。owner `PLATFORM-EVALUATION-SYSTEM`，handoff `TRAIN-DATA`，Books Pending。

#### TTRV — 24/30

- **Identity / revision / coverage:** `2510.06783` v1 2025-10-08；全文覆盖 VLM test-time RL、pseudo reward/augmentation、benchmarks、ablation 与 compute overhead。
- **Mechanism / state / control:** 在测试分布用自生成视图/反馈更新 policy，而非静态 inference；adapter/checkpoint 与 request-specific state必须隔离。
- **Evidence / limits / owner:** 不证明在线 weight update适合 multi-tenant serving；污染、catastrophic drift、latency 与 rollback成本显著。owner `TRAIN-LORA`，handoff `PLATFORM-MULTI-TENANT`、`PLATFORM-PRODUCTION`，Books Pending。

#### WristWorld — 23/30

- **Identity / revision / coverage:** `2510.07313` v1 2025-10-08；全文覆盖 wrist-view 4D world model、generation pipeline、robot manipulation evaluation 与 limitations。
- **Mechanism / state / control:** 从外部 observation 预测 action-relevant wrist view，给 controller 增加局部几何状态；world-model proposal 与真实 sensor observation区分版本与置信度。
- **Evidence / limits / owner:** simulation/task 结果不等同真实闭环安全；occlusion、calibration、hallucinated geometry 与 rollout error仍在。owner `MULTIMODAL-WORLD-MODELS`，Books Pending。

#### Your Harness is Not Secure — 26/30

- **Identity / revision / coverage:** `2510.06607` v1 2025-10-08；current title 为 *Your Harness is Not Secure: Benchmarking Real-world Threat of Command Line Interface Agent*，早期 discovery title 作为同 family alias；全文覆盖 threat scenarios、CLI harness、attack chain、metrics 与 disclosure boundary。
- **Mechanism / state / control:** executable evaluation拆开模型输出、tool permission、environment opportunity 与 artifact impact；harness拥有permission/target state，verifier检查side effect。
- **Evidence / limits / owner:** 结果衡量 model+harness+environment，不等于裸模型能力或真实攻击率；turn budget、network、credentials 与 sandbox决定机会。owner `PLATFORM-SECURITY`，Books Pending。

#### When Thoughts Meet Facts — 27/30

- **Identity / revision / coverage:** `2510.07499` v1 2025-10-08；全文覆盖 reusable reasoning units、long-context retrieval/assembly、training/evaluation、ablation 与 limitations。
- **Mechanism / state / control:** 把可复用 reasoning 与事实 context 分离：事实按 query检索，strategy 按 provenance/适用条件复用，避免整条旧 trajectory被当成真理复制。
- **Evidence / limits / owner:** 作者任务不证明 extracted strategy跨域正确；错误策略会重复放大，需要 supersession与review。owner `AGENT-MEMORY`，handoff `AGENT-RAG`、`AGENT-REFLECTION`，Books Pending。

#### Hybrid Reinforcement — 26/30

- **Identity / revision / coverage:** `2510.07242` v1 2025-10-08；全文覆盖 sparse outcome+dense feedback组合、objective、reasoning experiments、ablation 与 sensitivity。
- **Mechanism / state / control:** sparse reward定义最终可验证目标，dense signal改善中间 credit；reward mixer拥有信号权重，optimizer保留来源与尺度。
- **Evidence / limits / owner:** dense feedback也会引入 reward-model bias与shortcut；作者任务不能证明通用最优配比。owner `TRAIN-RLHF`，handoff `TRAIN-PPO`、`TRAIN-GRPO`，Books Pending。

#### Learning to Route LLMs from Bandit Feedback — 27/30

- **Identity / revision / coverage:** `2510.07429` v1 2025-10-08；全文覆盖 contextual bandit routing、partial-feedback estimator、baseline、regret/empirical evaluation 与 limitations。
- **Mechanism / state / control:** router无需每个request运行所有模型取全标签，而从被选模型的cost/quality feedback在线更新；router持有decision trace与policy version。
- **Evidence / limits / owner:** partial feedback带 exploration risk、delayed reward 与 non-stationary drift；离线benchmark不证明生产SLO安全。owner `INFER-SCHEDULING`，handoff `PLATFORM-COST`、`PLATFORM-EVALUATION-SYSTEM`，Books Pending。

#### Agent Learning via Early Experience — 29/30

- **Identity / revision / coverage:** `2510.08558` v1 2025-10-09，v2 2025-10-13，当前 v3 2026-05-24；全文覆盖 implicit world modeling、自反思、八类环境、跨模型评估、ablation 与 limitations。
- **Mechanism / state / control:** agent action后的 future state成为无需final reward的supervision，桥接 expert SFT 与 online RL；environment state、trajectory provenance 与 checkpoint分离。
- **Evidence / limits / owner:** 支持作者环境中的 effectiveness/OOD improvement，不证明 future state代表task success；unsafe exploration、simulator bias、long-horizon credit仍在。owner `AGENT-REFLECTION`，Books Pending。

#### MM-HELIX — 27/30

- **Identity / revision / coverage:** `2510.08540` v1 2025-10-09、v2 2025-10-11；全文覆盖 42-task platform、trace data、Adaptive Hybrid Policy Optimization、evaluation 与 ablation。
- **Mechanism / state / control:** offline trace learning提供起点，online policy optimization适应自身分布；platform绑定task、trace、reward/evaluator 与 policy version。
- **Evidence / limits / owner:** 1260 benchmark与约100K traces是作者配置；Qwen2.5-VL-7B结果不能外推所有MLLM，judge、task mix与reward design影响结论。owner `TRAIN-RLHF`，Books Pending。

#### UniVideo — 26/30

- **Identity / revision / coverage:** `2510.08377` v1 2025-10-09；全文覆盖 unified video understanding/generation representation、training stages、benchmarks、ablation 与 limitations。
- **Mechanism / state / control:** 共享时空 token/latent backbone，同时保留理解 head 与生成 decoder 的不同 commit语义；frame timestamp与clip identity成为数据契约。
- **Evidence / limits / owner:** 作者视频benchmark不证明单一objective消除理解/生成冲突；resolution、frame rate、compression与sampling steps限制比较。owner `MULTIMODAL-REPRESENTATION`，Books Pending。

#### DeepPrune — 23/30

- **Identity / revision / coverage:** `2510.08483` v1 2025-10-09；全文覆盖 pruning criterion、layer/token behavior、model experiments、ablation 与 limitations。
- **Mechanism / state / control:** judge 从 partial reasoning trace 预测 final-answer equivalence，online greedy clustering 合并等价路径并尽早停止冗余 rollout；scheduler 拥有 trace cluster/stop decision，base model 生成状态不变。
- **Evidence / limits / owner:** 作者报告 65.73%～88.50% token reduction 且精度变化受限，只在所测 judge、reasoning model 与 benchmark 成立；错误聚类会删除少数正确分支，judge 本身也增加成本。owner `INFER-SCHEDULING`，Books Pending。

#### First Try Matters — 22/30

- **Identity / revision / coverage:** `2510.08308` v1 2025-10-09；全文覆盖 first-attempt signal、training recipe、reasoning benchmark、ablation 与 analysis。
- **Mechanism / state / control:** 将首个sample与后续resampling分开，避免pass@k掩盖首答policy质量；evaluator持有attempt index与sampling seed。
- **Evidence / limits / owner:** 诊断不证明首答永远比best-of-N更重要；temperature、budget与grader改变结论。owner `PLATFORM-EVALUATION-SYSTEM`，Books Pending。

#### Learning on the Job — 28/30

- **Identity / revision / coverage:** `2510.08002` v1 2025-10-09；全文覆盖 deployment-time experience collection、adaptation mechanism、agent tasks、baseline、ablation 与 limitations。
- **Mechanism / state / control:** 真实workflow execution outcome转成可审计experience，经selection/reflection更新context或policy；线上serving state与训练candidate state隔离。
- **Evidence / limits / owner:** 作者任务支持continual adaptation，但不证明未审查线上轨迹可直接训练；privacy、poisoning、non-stationarity与rollback是核心成本。owner `AGENT-WORKFLOW`，Books Pending。

#### Memory Retrieval and Consolidation in LLMs through Function Tokens — 24/30

- **Identity / revision / coverage:** `2510.08203` v1 2025-10-09；全文覆盖 function-token hypothesis、feature-token bipartite graph、activation case studies、pretraining loss analysis 与局限；这里的 function token 指 punctuation/articles/prepositions 等语言 token，不是外部 memory API。
- **Mechanism / state / control:** 论文观察少量 function tokens 会激活大量 context-predictive features，并提出 pretraining 时预测其后的 content token 促进 feature consolidation；这是内部表示/训练动力学假说，没有 external store、read/write command 或 runtime commit。
- **Evidence / limits / owner:** graph correlation与case study支持解释假说，但不足以证明单一token对“记忆”有完整因果所有权；不同模型、tokenizer、层与干预实验仍待验证。owner `WORLDVIEW-REPRESENTATION`，handoff `MODEL-TRANSFORMER-LAYER`、`TRAIN-PRETRAINING`，Books Pending。

#### Thinking with Camera — 27/30

- **Identity / revision / coverage:** `2510.08673` v1 2025-10-09；全文覆盖camera parameter/map表示、约4M triplets、regression+diffusion、evaluation 与 limitations。
- **Mechanism / state / control:** camera从隐含metadata变成显式 control variable；连续参数由regression读取/预测，visual generation由diffusion commit，共享scene representation。
- **Evidence / limits / owner:** 不证明几何因果或真实robot calibration；synthetic bias、coordinate convention与extrapolation是边界。owner `MULTIMODAL-REPRESENTATION`，Books Pending。

#### BigCodeArena — 26/30

- **Identity / revision / coverage:** `2510.08697` v1 2025-10-09、v2 2025-12-18；全文覆盖 BigCodeArena platform、on-the-fly execution environment、14K+ sessions、10 models、10 languages、8 execution environments、preference analysis 与 limitations。
- **Mechanism / state / control:** 人类不再只阅读静态代码，而可运行候选、观察 execution outcome 后再做 pairwise preference；platform 持有 code/environment/session identity，rater 拥有 preference，执行结果提供 grounded evidence。
- **Evidence / limits / owner:** 互动执行提高 preference 的信息量，但 human vote仍不是 hidden-test correctness；participant mix、language/environment分布与self-selection限制排名外推。owner `PLATFORM-EVALUATION-SYSTEM`，Books Pending。

#### OpenRubrics — 24/30

- **Identity / revision / coverage:** `2510.07743` v1 2025-10-09；全文覆盖开放rubric构建、grader协议、agreement、task evaluation、artifact 与 limitations。
- **Mechanism / state / control:** rubric由隐含grader prompt变成versioned evaluation artifact；task item、criterion、grader output与aggregation可分别审计。
- **Evidence / limits / owner:** 开放artifact改善复查性但不消除rater/model judge偏差；rubric drift与criterion相关性会让aggregate失真。owner `PLATFORM-EVALUATION-SYSTEM`，Books Pending。

## Low-Score Closure

以下 17 个 family 的正文/abstract、identity、v1 日期和评分已核验；它们不是 Review Pending，也没有被静默遗漏。

| Source Family | Verified date | Total | Rejection reason |
| --- | --- | ---: | --- |
| `arxiv:2510.05367` LightCache | 10-06 | 19 | 特定 video workload/cache policy 的局部收益，未改变 cache identity、invalidation 与 rollback 结论。 |
| `arxiv:2510.05057` StaMo | 10-06 | 19 | 时空建模变体，缺少足以形成独立系统演进链的 state/serving contract。 |
| `arxiv:2510.06751` OBS-Diff | 10-08 | 18 | Timestep-aware one-shot diffusion pruning 是机制受限的作者证据；尚未建立 production kernel、hardware portability 与端到端 SLO。 |
| `arxiv:2510.05528` ARMOR | 10-07 | 19 | 任务范围与实现证据窄，未隔离相对既有 robustness/evaluation owner 的机制增量。 |
| `arxiv:2510.05608` Global Planner Training | 10-07 | 19 | 特定规划任务结果，缺跨环境 state/action contract 与系统级 failure recovery。 |
| `arxiv:2510.06915` LongRM | 10-08 | 19 | 长链 reward-model 证据受 benchmark 与 judge 约束，未形成新的通用 credit/evaluation contract。 |
| `arxiv:2510.08191` Training-Free GRPO | 10-09 | 19 | 名称暗示替代 training，但证据更接近 inference-time selection/estimation，边界不足。 |
| `arxiv:2510.08240` Alignment Waltz | 10-09 | 19 | alignment 观察依赖特定 judge/task mix，未形成稳定 control contract。 |
| `arxiv:2510.08565` NaViL | 10-09 | 19 | 多模态结构变体，缺独立 representation identity 或数据流改变。 |
| `arxiv:2510.08529` CoMAS | 10-09 | 19 | multi-agent 收益未隔离 single-agent headroom、communication tax 与 shared-state 影响。 |
| `arxiv:2510.08276` Beyond Turn Limits | 10-09 | 19 | 主要扩展指定 benchmark 的 turn budget，未证明可迁移 workflow mechanism。 |
| `arxiv:2510.07958` A2Search | 10-09 | 19 | search 策略变体，收益未与额外 rollout/tool budget 充分解耦。 |
| `arxiv:2510.08759` BEAR | 10-09 | 19 | benchmark 贡献为主，尚无新的 evaluator/executable artifact contract。 |
| `arxiv:2510.08525` Which Heads Matter for KV Compression | 10-09 | 19 | sensitivity 结果模型/层/长度依赖强，不能升级为通用 KV policy。 |
| `arxiv:2510.08696` Don't Waste Mistakes | 10-09 | 19 | 错误轨迹复用是 training recipe，尚未形成可治理的 provenance/credit mechanism。 |
| `arxiv:2510.08457` ARES | 10-09 | 19 | 所测设置有限，无法隔离相对既有 reasoning/evaluation 路线的长期增量。 |
| `arxiv:2510.08994` Speculative Jacobi-Denoising | 10-10 | 19 | 作者实验显示候选执行路径，但缺 production kernel、rollback 与 SLO 证据。 |

## Evidence Level

- **Level A — Primary mechanism evidence:** 35 篇论文均打开 arXiv primary HTML/PDF family，覆盖 method、implementation/evaluation、ablation/sensitivity 或 limitations；后续 revision 与 v1 事件日期分离。
- **Level B — Official system/evaluator contract:** Google security strategy、OpenAI bias evaluation 支持公开 taxonomy、workflow 与 evaluation contract。
- **Level C — Version fact:** Codex GA 只支持公开产品/接口事实，机制未披露。
- **Discovery-only:** Hugging Face Daily、Scholar、OpenAlex、DBLP、Semantic Scholar、Crossref 只用于召回/metadata，不承担机制结论。
- **Inference:** `context state → experience state → governed update` 是本项目综合推断，不是任何单篇论文直接证明。

## Cross-Week Deduplication and Spillback

### W42 feed/history 回拨到 W41（21 families）

以下项目在后续 feed 才集中出现，但 arXiv v1 为 10-09/10-10，owner 是 W41：Agent Learning via Early Experience、MM-HELIX、UniVideo、DeepPrune、First Try Matters、Learning on the Job、Memory Function Tokens、Thinking with Camera、BigCodeArena、OpenRubrics，以及 Low-Score Closure 中的 Training-Free GRPO、Alignment Waltz、NaViL、CoMAS、Beyond Turn Limits、A2Search、BEAR、Which Heads Matter、Don't Waste Mistakes、ARES、Speculative Jacobi-Denoising。其 revision 不得在 W42 重复计分。

### 排除到 W40 或更早

first-public 早于 10-06，未计入本周：Optimal Scaling Needs Optimal Norm (`2510.03871`)、Front-Loading Reasoning (`2510.03264`)、RxT (`2510.03561`)、MOSS-Speech (`2510.00499`)、Prosperity before Collapse (`2510.01161`)、Judging with Confidence (`2510.00263`)、CWM (`2510.02387`)、Fathom (`2509.24107`)、Fast-dLLM v2 (`2509.26328`)、CoDA (`2510.03270`)、Scaling Code CoT (`2510.04081`)、OneFlow (`2510.03506`)、Cache-to-Cache (`2510.03215`)、Low-Precision Flash Attention (`2510.04212`)、Patch-as-Decodable Token (`2510.01954`)、Reinforcement Mid-Training (`2509.24375`)、G2RPO (`2510.01982`)、DeepTravel (`2509.21842`)、MEMTRACK (`2510.01353`)、Single Character Eval Sensitivity (`2510.05152`, v1 10-02) 与 VeriGuard (`2510.05156`, v1 10-03)。

### 排除到 W42

KORMo (`2510.09426`)、StreamingVLM (`2510.09608`)、Multimodal Prompt Optimization (`2510.09201`)、PhysToolBench (`2510.09507`)、Dyna-Mind (`2510.09577`)、Adaptive Attacks (`2510.09462`)、Mind-Paced (`2510.09592`) 与 Mitigating Overthinking (`2510.09535`) 的 v1 属 W42；没有提前归档。

## Knowledge Tree Position

| Evolution route | Canonical owner | Adjacent handoff |
| --- | --- | --- |
| structured context、derived memory、reflection | `AGENT-MEMORY` (Ch77) | `AGENT-CONTEXT`、`AGENT-REFLECTION`、`AGENT-WORKFLOW` |
| early experience、workflow adaptation | `AGENT-REFLECTION` / `AGENT-WORKFLOW` | `TRAIN-RLHF`、`MULTIMODAL-WORLD-MODELS` |
| tool/evaluable agent behavior | `PLATFORM-EVALUATION-SYSTEM` (Ch66) | `AGENT-TOOL-CALLING`、`PLATFORM-SECURITY` |
| security verifier / permission boundary | `PLATFORM-SECURITY` (Ch72) | `AGENT-WORKFLOW`、`PLATFORM-PRODUCTION` |
| multimodal representation/generation | `MULTIMODAL-REPRESENTATION` / `MULTIMODAL-GENERATIVE-PARADIGMS` | `MULTIMODAL-WORLD-MODELS` |
| world state、VLA、physical feedback | `MULTIMODAL-WORLD-MODELS` / `MULTIMODAL-EMBODIED-VLA` | `TRAIN-DATA` |
| RL data、objective 与 credit | `TRAIN-DATA` / `TRAIN-RLHF` / `TRAIN-PPO` / `TRAIN-GRPO` | `PLATFORM-EVALUATION-SYSTEM` |
| long-context/hybrid execution state | `MODEL-LONG-CONTEXT` / `MODEL-SELF-ATTENTION` | `INFER-KV-CACHE`、`INFER-TENSORRT-LLM` |
| online model routing | `INFER-SCHEDULING` | `PLATFORM-COST`、`PLATFORM-EVALUATION-SYSTEM` |

## Recommended Action

- W41 archive evidence 已闭合；保留 38 个 `20+` candidate 作为后续年度 Books 审计输入。
- Historical Books Gate 继续关闭：本周没有修改 Books，也不把 Weekly summary 直接沉淀为长期机制。
- 后续优先按 `AGENT-MEMORY` → `AGENT-REFLECTION` / `AGENT-WORKFLOW` → `PLATFORM-EVALUATION-SYSTEM` / `PLATFORM-SECURITY` 与 `MULTIMODAL-REPRESENTATION` → `MULTIMODAL-WORLD-MODELS` → `MULTIMODAL-EMBODIED-VLA` 两条路线整合，避免论文列表式追加。

## Event-Date Daily Decision

历史回填不创建 Daily。所有真实事件日期、revision和Books候选状态直接保留在本 Weekly；W42 feed的延迟发现不改变owner week。

## Books Integration Decision

**Historical Books Gate Closed.** 本周 `20+` candidates均为 `Books Pending` 或 `Weekly Only`；Source Family review完成不等于已进入Books。等2025全年Historical Evidence Gate通过后，再读取owner与相邻章节、逐项决定 `Integrate / Refine / No Change / Weekly Only`。

## Ignored Noise

- Anthropic管理层任命、机构活动、融资、营销榜单与Google September roundup：没有新机制或证据contract。
- 缺workload条件的“领先”“SOTA”与单一author benchmark：不作为通用事实。
- 只有后续revision日期、无W41 v1/official event的项目：不冒充本周事件。
- 论文名相近或discovery metadata错配：以arXiv identity为准；`2510.07315`已纠正为SWE-IF。

## Repository Changes

- 重建 `papers/2025/weekly/2025-W41/README.md`：从错误的零候选周恢复为55个评分family、38个Full Source Review、17个Low-Score Closure和跨周spillback账本。
- 未修改Books、年度索引、Learning State、W40/W42或其他Weekly；未stage、unstage、commit或push。

## Open Questions

- ACE / derived memory在adversarial feedback下，entry-level provenance、supersession、delete与rollback应采用什么统一contract？
- early experience的future state如何区分“环境变化”与“任务进展”，避免无reward supervision学习到可预测但无用的transition？
- multimodal unified token在训练和serving中如何绑定codec version、timestamp、modality与cache identity，才能安全复用state？
- executable agent evaluation如何报告model、harness、tool permission与environment opportunity各自贡献，而不是压成单分？

## Sources

### Official primary sources

- OpenAI, “Codex is now generally available,” 2025-10-06: https://openai.com/index/codex-now-generally-available/
- Google, “Our AI security frontier strategy and tools,” 2025-10-06: https://blog.google/innovation-and-ai/technology/safety-security/ai-security-frontier-strategy-tools/
- OpenAI, “Defining and evaluating political bias in LLMs,” 2025-10-09: https://openai.com/index/defining-and-evaluating-political-bias-in-llms/

### arXiv primary sources — Full Source Review

- https://arxiv.org/abs/2510.04618
- https://arxiv.org/abs/2510.04800
- https://arxiv.org/abs/2510.04996
- https://arxiv.org/abs/2510.04673
- https://arxiv.org/abs/2510.04678
- https://arxiv.org/abs/2510.05318
- https://arxiv.org/abs/2510.05862
- https://arxiv.org/abs/2510.05592
- https://arxiv.org/abs/2510.05684
- https://arxiv.org/abs/2510.06217
- https://arxiv.org/abs/2510.06062
- https://arxiv.org/abs/2510.06308
- https://arxiv.org/abs/2510.06499
- https://arxiv.org/abs/2510.06590
- https://arxiv.org/abs/2510.06710
- https://arxiv.org/abs/2510.07315
- https://arxiv.org/abs/2510.07318
- https://arxiv.org/abs/2510.07019
- https://arxiv.org/abs/2510.07238
- https://arxiv.org/abs/2510.06783
- https://arxiv.org/abs/2510.07313
- https://arxiv.org/abs/2510.06607
- https://arxiv.org/abs/2510.07499
- https://arxiv.org/abs/2510.07242
- https://arxiv.org/abs/2510.07429
- https://arxiv.org/abs/2510.08558
- https://arxiv.org/abs/2510.08540
- https://arxiv.org/abs/2510.08377
- https://arxiv.org/abs/2510.08483
- https://arxiv.org/abs/2510.08308
- https://arxiv.org/abs/2510.08002
- https://arxiv.org/abs/2510.08203
- https://arxiv.org/abs/2510.08673
- https://arxiv.org/abs/2510.08697
- https://arxiv.org/abs/2510.07743

### arXiv primary sources — Low-Score Closure

- https://arxiv.org/abs/2510.05367
- https://arxiv.org/abs/2510.05057
- https://arxiv.org/abs/2510.06751
- https://arxiv.org/abs/2510.05528
- https://arxiv.org/abs/2510.05608
- https://arxiv.org/abs/2510.06915
- https://arxiv.org/abs/2510.08191
- https://arxiv.org/abs/2510.08240
- https://arxiv.org/abs/2510.08565
- https://arxiv.org/abs/2510.08529
- https://arxiv.org/abs/2510.08276
- https://arxiv.org/abs/2510.07958
- https://arxiv.org/abs/2510.08759
- https://arxiv.org/abs/2510.08525
- https://arxiv.org/abs/2510.08696
- https://arxiv.org/abs/2510.08457
- https://arxiv.org/abs/2510.08994

## Independent Review and Gate

### Account Reconciliation

- Unique scored Source Families: **55**.
- High (`25～30`): **27**.
- Medium (`20～24`): **11**.
- Low (`<20`): **17**.
- `20+` Full Source Reviews: **38/38**（3 official + 35 papers）。
- Low-Score Closures: **17/17**.
- W42 feed/history spillback owners restored to W41: **21**.
- Ordinary `Review Pending`: **0**.
- `Unverified / Blocked`: **0**；无须用户补交材料。
- Duplicate scored family inside W41: **0**.

### Independent Evidence Review

- **Identity:** arXiv ID 与标题逐项复核；纠正 `2510.07315` metadata 错配。
- **Date/revision:** v1 决定 owner week；ACE、Webscale-RL、Agent Early Experience 等 revision 没有重复计分。
- **Fact boundary:** 官方公告、作者实验、discovery metadata 与项目推断已分层；没有从产品行为反推隐藏机制。
- **Evaluation:** 数字只在作者披露的 model/data/evaluator 内保留；未披露 hardware、precision、length、batch、concurrency、SLO 不补写。
- **Dedup:** W40 earlier owner、W42 later owner 与 W42-feed/W41-owner 均在 ledger 闭合。
- **Knowledge tree:** 每个 `20+` family 有 canonical Stable Node 与相邻 handoff；没有因目录外问题搁置。
- **Books safety:** Historical Books Gate 明确关闭，W41 没有修改 Books。

### W41 Gate

**PASS — Weekly Evidence Closed.** 固定源重放、55 行评分、38 个 Full Source Review、17 个低分 closure、spillback、日期/revision、Stable Node 与 disposition 均已闭合；`Review Pending = 0` 且无 blocker。该结论只代表 W41 Weekly Evidence Gate，不代表 2025 全年 Archive Gate 或 Historical Books Gate 完成。
