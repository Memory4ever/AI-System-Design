# AI Research Weekly — 2026-W08

> Coverage Window: 2026-02-16～2026-02-22
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-08
> Re-audit Status: Source-Family Books Gate Complete — 23/23 final dispositions; 18 Integrate/Refine, 4 No Change, 1 Weekly Only; Archive Completion Gate Open

## Executive Summary

旧版只保留 Anthropic autonomy telemetry 与 OpenAI First Proof，两项不足以代表本周研究面。
按固定来源顺序重新扫描后，已恢复 21 项候选：GLM-5、Agent reliability、ResearchGym、
Computer-Using World Model、personalization/memory、long-context mechanism、training optimizer 与
Agent safety 等形成多条系统演进线。原两项 Source Review 仍成立，MapTrace 完成低分来源核验；
GLM-5、Agent Reliability 与 ResearchGym 已完成论文全文、Appendix 和公开 artifact 联合复核；
Agent Reliability 的 v1 outcome-consistency 公式在 v3 被公开纠正；ResearchGym 则把最终分数、
实验进展和环境完整性分成不同证据面。Computer-Using World Model 也已完成全文复核，其
“Agent task score”被重新限定为离线单步 action matching，而不是多步真实执行。PAHF 也已完成
论文、证明、限制与官方代码联读；其结果限于 persona simulator，而官方当前代码又有 paper 后的
prompt/feedback refinements。Calibrate-Then-Act 的 v1→v3 与官方 artifact 也已完成复核；其长期价值是
把 prior calibration 与 cost-aware action selection 解耦，不是把合成任务的 discounted reward 当作
生产收益。Modeling Distinct Human Interaction in Web Agents 也已完成 v1→v4、模型卡与 PlowPilot
联读；其真实用户 trajectory 是有价值的 deployment evidence，但 observed intervention 不是规范性的
help/approval ground truth。Frontier AI Risk Management Framework v1.5 的五个风险族、mitigation、
limitations 与 related misevolution artifact 也已完成联读；五套 heterogeneous experiments 不能压成统一模型
风险排行，同集群受指令创建 Deployment 也不能外推为自然跨环境复制。OpenClaw trajectory audit 也已完成
PDF、六份 seed JSON 与官方机制文档联读；其 environment/permission 反例有价值，但 artifact inconsistency 与
unpinned runtime 使 headline 不能进入 Books。Magma 也已完成论文、证明、训练契约与全部消融复核；
论文支持的是特定小规模 Pretraining contract 下的 stochastic update masking，而不是已验证的通信、
显存或大模型训练加速，且 alignment sampling 在论文自己的消融中没有优于 uniform sampling。其余
TAROT 也已完成论文与公开 reward/config/data artifact 联读；tiered tests 与 curriculum 的受限案例有价值，
但论文没有给出可执行的 capability-selection rule，当前 reward artifact 还存在输出行数未校验、active-tier
reward ceiling 随 schedule 改变等证据问题，不能作为已验证的通用 curriculum 机制。Vision Wormhole 也已
完成 v1 全文、v2 revision 与官方代码联读；它提供了从 pairwise latent translator 到 per-model hub adapter 的
实验性通信分支，但只降低 adapter 集成复杂度，且速度、准确率与可审计性均有明确条件。DreamZero 也已
完成唯一 v1、全部 Appendix、项目页与当前代码联读；其长期机制是联合 world/action prediction、真实
observation 回灌与 action-chunk latency window 共同形成闭环，而不是作者的 2x/38x headline。In-context
co-player inference 也已完成唯一 v1、理论 Appendix 与实验细节复核；它支持“多样 co-player 训练 →
history-conditioned adaptation → 可被 shaping/extortion → mutual pressure 下可能合作”的受限机制链，不支持
将 IPD 结果外推成现实 Agent 会自然合作。REFINE 也已完成唯一 v1、全部实验/Appendix 与官方
artifact 边界复核；它支持 fast-weight state 的训练目标应匹配多 token 使用周期，但不支持把跨不同
prefix 标准化的相对 reward 当作原始 GRPO 同义词，也不支持在数据源已替换后宣称严格复现。MMA 也已
完成唯一 v1、全部实验/Appendix 与官方实现联读；它把 retrieval relevance 之后的 source、valid time、
neighborhood support 与 abstention 暴露为独立 policy，但当前 confidence 是未校准 heuristic，代码中的
consensus 也依赖已存邻居分数与 embedding cosine，不能等同于事实共识或 contradiction proof。AlphaEvolve
MARL 论文也已完成 v1/v2 事件版本、v3 revision、全部算法/消融/测试集与代码 Appendix 联读；W08 当时只能
支持 raw VAD-CFR/SHOR-PSRO 是在精确小型 game-tree evaluator 中产生的候选，5 月 v3 才补出
`search → train/test ablation → human distillation`。这一 revision 反而推翻了 v1 对 volatility、hybrid blending
与 train/eval asymmetry 的强机制归因，因此不能把高 fitness 候选直接写成新原理。Unified Latents 也已完成
唯一 v1 全文、公式、全部 image/video experiments、ablation 与 Appendix 复核；它把 latent bitrate、reconstruction
fidelity、base-model capacity 与 decoder compute 显式耦合，但 headline 的 training FLOPs 排除了 autoencoder，
diffusion decoder 采样又显著更贵。结构迁移前的 ROADMAP 没有 Diffusion/VAE owner；新增 Part III 后，
长期机制已分别由 Ch23 与 Ch24 承接。DDiT 也已完成唯一 v1、13 页论文、项目页、机制、
实验与分析复核；它支持“按 denoising trajectory 的局部变化自适应选择 token granularity”这一实验分支，
但只证明 scheduler rule 是 training-free，整个方案仍需 patch-specific embedding、LoRA 与 distillation 训练。
论文的阈值—速度表存在内部不一致，hardware/batch/precision/training budget 与 user-study contract 也未披露；
当前 ROADMAP 又没有 diffusion inference owner，不能把它误写成 LLM Continuous Batching 或推理调度。
2Mamba2Furious 也已完成 v1 全文、v3 revision、当前作者仓库、checkpoint collection 与 custom Triton
kernel 联读。它支持的长期机制不是“linear Attention 已经替代 softmax”，而是“固定 recurrent state 的
表达能力可通过高阶 feature 提升，但会把随序列长度增长的 KV 成本换成随 head dimension 快速增长的
state、kernel 与数值成本”。作者自己的 artifact 将 kernel 定位为 proof of concept，NIAH 又只是删去
最长样本后的 1000 条单次评估，因此没有 latency/throughput 或通用 long-context 结论可进入 Books。
至此 23/23 候选已完成来源核验与逐项 Books disposition。2026-08-13 的 owner-chapter integration
把 18 项机制重排进 12 个 Stable Knowledge Nodes，4 项由已有论证覆盖，MapTrace 仅保留 Weekly。
历史 GitHub release/RFC 覆盖仍不完整，因此 Source-Family Books Gate 已完成而 Archive Completion Gate
继续 Open；两种状态不得混写。

## Coverage and Source Coverage

- 模型与研究机构：已核验 Anthropic 2 月 18 日、OpenAI 2 月 20 日、Google Research 2 月 17 日与
  GLM-5 2 月 17 日技术报告。Google/Meta/Anthropic/OpenAI 的后续页面只作 source-family 核验，
  不反写为本周首发事件。
- 论文与学术来源：扫描 Hugging Face Daily Papers 2 月 16～20 日并回到 arXiv v1 定归周；2 月
  21～22 日 discovery 页面无法稳定返回，作为 coverage gap。HF 推荐日不等于论文首发日。
- 跨周去重：SkillsBench、SAE sanity checks、SLA2、SpargeAttention2、AutoWebWorld、Empty
  Shelves、Mobile-Agent-v3.5 等虽然在 W08 discovery page 出现，但 arXiv v1 属 W07，不重复计分。
- AI Infra：已检查 PyTorch、vLLM、SGLang、Dynamo 的公开 release 入口；历史 GitHub pagination
  无法证明 W08 有高门槛 stable release。SGLang Apple-device roadmap issue 只是 2 月 21 日计划信号，
  不是实现或 release；工程来源覆盖仍标记不完整。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Measuring AI agent autonomy in practice | 3 | 4 | 5 | 4 | 5 | 4 | 25/30 | No Change — Ch67 already covers deployment telemetry |
| OpenAI First Proof submissions | 3 | 3 | 3 | 5 | 4 | 4 | 22/30 | No Change — Ch66 already separates artifact evidence |
| MapTrace / Teaching AI to read a map | 2 | 2 | 2 | 5 | 2 | 3 | 16/30 | Weekly Only — Low-score verified |
| GLM-5 technical report | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Refine — `TRAIN-GRPO` |
| Frontier AI Risk Management Framework v1.5 | 3 | 4 | 4 | 3 | 4 | 4 | 22/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` |
| Trajectory-Based Safety Audit of OpenClaw | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | No Change — Ch72 already covers trajectory/tool-policy boundaries |
| ResearchGym | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` |
| Magma / Masking Updates in Adaptive Optimizers | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `TRAIN-PRETRAINING` |
| TAROT test-driven curriculum RFT | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | No Change — Ch33/27 already cover verifier and curriculum contracts |
| Vision Wormhole latent MAS communication | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Refine — `AGENT-MULTI-AGENT` / Experimental |
| DreamZero / World Action Models | 4 | 4 | 3 | 4 | 3 | 4 | 22/30 | Refine — `MULTIMODAL-EMBODIED-VLA` / Experimental |
| In-context co-player inference | 4 | 3 | 3 | 4 | 3 | 4 | 21/30 | Refine — `AGENT-MULTI-AGENT` / Experimental |
| Towards a Science of AI Agent Reliability | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` |
| REFINE / Reinforced Fast Weights | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Refine — `MODEL-LONG-CONTEXT` / Experimental |
| PAHF / Personalized Agents from Human Feedback | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `AGENT-MEMORY` / Experimental |
| MMA / Multimodal Memory Agent | 3 | 3 | 3 | 3 | 4 | 4 | 20/30 | Refine — `AGENT-MEMORY` / Experimental |
| AlphaEvolve for multiagent algorithm discovery | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Refine — `AGENT-WORKFLOW` / Experimental |
| Calibrate-Then-Act | 3 | 4 | 4 | 4 | 5 | 5 | 25/30 | Refine — `AGENT-PLANNING` / Experimental |
| Unified Latents | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Refine — `MULTIMODAL-REPRESENTATION` / Experimental |
| DDiT dynamic patch scheduling | 3 | 3 | 4 | 4 | 3 | 4 | 21/30 | Refine — `MULTIMODAL-GENERATIVE-PARADIGMS` / performance disputed |
| Computer-Using World Model | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `MULTIMODAL-WORLD-MODELS` / Experimental |
| 2Mamba2Furious | 3 | 4 | 3 | 4 | 4 | 4 | 22/30 | Refine — `MODEL-LONG-CONTEXT` / Experimental |
| Modeling Distinct Human Interaction in Web Agents | 3 | 4 | 4 | 4 | 5 | 5 | 25/30 | Refine — `AGENT-WORKFLOW` / Experimental |

## Recovered Candidate Census

| Event Date | Candidate | Primary Source | Discovery / Family Signal | Initial Scope Decision | Review State |
| --- | --- | --- | --- | --- | --- |
| 2026-02-16 | Frontier AI Risk Management Framework v1.5 | arXiv:2602.14457 + related misevolution artifact | HF 02-20 / risk framework | Ch62 main owner; Ch68 handoff candidate | Full Review Complete — Evidence Families Separated |
| 2026-02-16 | Trajectory-Based Safety Audit of OpenClaw | arXiv:2602.14364 + official seed-case artifact | HF 02-18 / trajectory audit | Ch68 main owner; Ch62/73/74 handoff checked | Full Review Complete — Evidence Contract Incomplete |
| 2026-02-16 | ResearchGym | arXiv:2602.15112 + official benchmark/runtime artifact | HF 02-18 / executable research eval | Ch62 main owner; Ch75/77 handoff candidates | Full Review Complete |
| 2026-02-17 | MapTrace | Google Research + linked paper/artifact | official research archive | Low relevance; source/date/rejection verified | Verified — Below 20 |
| 2026-02-17 | GLM-5 | arXiv:2602.15763 + official model/runtime artifacts | Zhipu technical report | Ch29 main owner; Ch22/31/32/44/51/77 handoff candidates | Full Review Complete |
| 2026-02-17 | Magma optimizer | arXiv:2602.15322 | HF 02-18 / optimizer mechanism | Ch24 main owner; Ch21/32 boundary checked | Full Review Complete — Scope and Owner Corrected |
| 2026-02-17 | TAROT | arXiv:2602.15449 + official artifact | HF 02-18 / code RFT | Ch29 main owner; Ch23/62 boundaries checked | Full Review Complete — Selection and Verifier Contract Incomplete |
| 2026-02-17 | Vision Wormhole | arXiv:2602.15382 v1→v2 + official artifact | HF 02-18 / latent MAS protocol | Ch78 main owner; Ch77/79 boundaries checked | Full Review Complete — Scope and Revision Corrected |
| 2026-02-17 | DreamZero | arXiv:2602.15922 v1 + official project/current artifact | HF 02-19 / world-action model | Ch75 main owner; Ch10/38/42 boundaries checked | Full Review Complete — Scope and Artifact Boundary Corrected |
| 2026-02-18 | In-context co-player inference | arXiv:2602.16301 v1; no official artifact located | HF 02-19 / MARL | Ch78 main owner; Ch77/80 boundaries checked | Full Review Complete — Owner and Scope Corrected |
| 2026-02-18 | Agent Reliability | arXiv:2602.16666 v1→v3 + HAL artifact | HF 02-19 / reliability metrics | Ch62 main owner; Ch63/68/69 handoff candidates | Full Review Complete — Formula Revised |
| 2026-02-18 | REFINE fast weights | arXiv:2602.16704 v1 + official artifact | HF 02-19 / next-sequence objective | Ch22 main owner; Ch24/29 boundaries checked | Full Review Complete — Owner and Reproduction Boundary Corrected |
| 2026-02-18 | PAHF | arXiv:2602.16173 + facebookresearch/PAHF | Meta source family | Ch73 main owner; Ch75/77/80 handoff candidates | Full Review Complete — Scope Corrected |
| 2026-02-18 | MMA | arXiv:2602.16493 v1 + official artifact | HF 02-19 / memory reliability | Ch73 main owner; Ch72/62/76 boundaries checked | Full Review Complete — Mechanism and Evidence Boundary Corrected |
| 2026-02-18 | AlphaEvolve for MARL algorithms | arXiv:2602.16928 v1→v3; no official artifact located | Google/AlphaEvolve family | Ch77 main owner; Ch62/78 boundaries checked | Full Review Complete — Revision and Owner Corrected |
| 2026-02-18 | Calibrate-Then-Act | arXiv:2602.16699 v1→v3 + official artifact | HF 02-20 / costly exploration | Ch75 main owner; Ch72/74/77 handoff candidates | Full Review Complete — Revision Audited |
| 2026-02-19 | Unified Latents | arXiv:2602.17270 v1; no official artifact located | HF 02-20 / latent codec | No direct owner; Ch5/18 boundary checked | Full Review Complete — Below 20 / Structural Gap |
| 2026-02-19 | DDiT | arXiv:2602.16968 v1 + official project page; no code located | HF 02-20 / dynamic token scheduling | No direct owner; Ch17/38/42/45/52 boundaries checked | Full Review Complete — Owner and Evidence Boundary Corrected |
| 2026-02-19 | Computer-Using World Model | arXiv:2602.17365 + GUI-360 data lineage | HF 02-20 / UI transition model | Ch75 main owner; Ch74/76/77 handoff candidates | Full Review Complete — Scope Corrected |
| 2026-02-19 | 2Mamba2Furious | arXiv:2602.17363 v1→v3 + author artifacts | HF 02-20 / linear attention | Ch22 main owner; Ch14/19 boundaries checked | Full Review Complete — Revision, State and Kernel Boundary Corrected |
| 2026-02-19 | Human Interaction in Web Agents | arXiv:2602.17588 v1→v4 + models + PlowPilot | HF 02-20 / intervention model | Ch77 main owner; Ch75/80 handoff candidates | Full Review Complete — Scope and Revision Corrected |

`Recovered Candidate Census` 的 `Initial Scope Decision` 是 2026-08-08 的历史快照，只证明当时的来源与
首次公开日期判断；不得按新章节号解释。最终 owner 与 Books disposition 以 Candidate Scoring、
Knowledge Tree Position 和 `2026-08-13 Source-Family Books Integration` 为准。

## Deep Analysis — Autonomy 是 Runtime Measurement，不是模型标签

Anthropic 分析真实 human-agent interactions，并观察长尾 session duration 随时间变化；官方
同时指出变化可能来自用户构成、信任、任务与产品，而非单一模型发布。第一性原理上，
autonomy 是 model capability、tool permission、termination policy、human intervention 与
workload selection 的联合观测量。更长运行时间可能意味着更强能力，也可能意味着低效、
失控或任务更复杂，因此必须与成功率、外部副作用和 intervention rate 联合解释。

## Full Source Review

本节各 packet 中的 `Human Gate Pending`、旧章节号与“本轮不修改 Books”保留为 2026-08-08 的审计
时间线。它们已由本周顶部 Candidate Scoring、最终 Books Integration Decision 和文末
`2026-08-13 Source-Family Books Integration` 覆盖，不代表当前 Gate 状态。

### Measuring AI agent autonomy in practice

- **Candidate / Week / Score:** Agent autonomy in practice / 2026-W08 / 25/30；
  `Source Family ID: anthropic-deployment-agent-autonomy-telemetry`。
- **Source Type / Date / Sources:** Anthropic 官方完整研究页及 PDF appendix；2026-02-18。
- **Full-read Coverage:** Verified；已检查 Claude Code turn-duration series、public API tool-call sample、
  autonomy/risk/human-involvement classifiers、privacy method、clusters、recommendations 与 limitations。
- **Problem / Previous Design:** capability benchmark 测模型能否完成任务，却不说明用户实际授权多少
  决策、agent 运行多久、采取哪些动作或下游是否还有 human review。
- **Changed Constraint / Mechanism:** agent products 产生长 trajectory 和 tool-call telemetry；研究从
  Claude Code turns 与 API calls 采样，用隐私保护 classifier 估计 duration、domain、risk、autonomy 和
  human involvement。产品/runtime 拥有 raw events，研究 pipeline 拥有 sampling/classifier state。
- **Evaluation Contract:** 99.9 percentile duration 是长尾 proxy；API 按 individual tool call 采样会
  overrepresent 多调用 deployment；classifier 只能看到局部 Context，不能识别所有 downstream review、
  eval/red-team 或 production state。
- **Evidence Boundary:** 证明该产品生态中特定窗口的观测分布与平滑变化；不证明更长 duration 等于
  success/能力/风险，也不证明模型 release 是变化原因。
- **Trade-offs / Previous Design:** post-deployment telemetry 改善风险发现，却增加 privacy、retention、
  sampling bias、classifier drift 与 false alarm；offline sandbox eval 对可重复 gate 仍不可替代。
- **Evolution / ROADMAP:** `Layering / Dependency`；Ch63 主 owner，Ch62/65/77/80 相邻。已读相关章节；
  Ch63 已把 autonomy 定义为 deployment observation 而非模型标量。
- **Integration Decision:** `No Change — Already Covered`；保留现有 Ch63，不重复厂商数字。
- **Open Questions:** 如何联合 success、meaningful progress、idle loops、side effects、takeover 与 policy
  violation，形成可比较且隐私最小化的 autonomy telemetry？

### OpenAI First Proof submissions

- **Candidate / Week / Score:** First Proof submissions / 2026-W08 / 22/30；
  `Source Family ID: openai-first-proof-artifacts-2026`。
- **Source Type / Dates / Sources:** OpenAI 官方结论页 + 公开 10 个 proof attempts/preprint；attempts
  2026-02-14，说明页 2026-02-20，后续专家反馈已把 problem 2 从可能正确修正为错误。
- **Full-read Coverage:** Verified as artifact/evaluation record；检查十题范围、proof artifacts、prompting
  appendix、expert-review status 与官方 correction。内部模型、training、hardware 和 run policy 未披露。
- **Problem / Mechanism:** research math 不能只用 short answer；系统产生 end-to-end proof artifact，
  交由领域专家与社区逐题审查。Artifact、prompt pattern、review status 与 correction history 是主要 state。
- **Evidence Boundary:** 公开可检查的 proof attempts 比单一 score 更强；仍不证明所有 claims 正确、
  不构成总体 research autonomy estimate，也不能把内部 model capability 与 manual interaction 分离。
- **Trade-offs / Previous Design:** artifact review 提供可追溯纠错，却昂贵、慢且依赖稀缺专家；形式化
  proof checker 在可形式化领域仍提供更确定但覆盖较窄的 verifier。
- **Evolution / ROADMAP:** `Principle Reuse`；Ch62 主 owner，Ch75/77 相邻。现有 evaluation 已要求
  artifact、verifier、review status 和 correction lineage。
- **Integration Decision:** `No Change — Already Covered`；Weekly 保留 correction 作为 evidence lesson。
- **Open Questions:** proof claim-level provenance、expert disagreement、formalization 和 model/manual
  contribution 如何进入 EvalSpec？

### MapTrace / Teaching AI to read a map

- **Candidate / Week / Score:** MapTrace / 2026-W08 / 16/30；
  `Source Family ID: google-research-maptrace-2026`。
- **Source Type / Date / Sources:** Google Research 官方技术文章及其链接的研究 artifact；官方页面发布于
  2026-02-17。该条只执行低分候选所需的来源、日期、机制边界与拒绝理由核验，不冒充论文级全文审计。
- **Problem / Mechanism:** 一般视觉语言模型可能识别地图中的局部文字或图形，却未必能把道路、地标、方向
  与问题约束组合成可检查的空间推理。公开材料描述以地图任务数据和 critic/evaluator 反馈训练或评估模型，
  让答案与中间推理能受到任务结构约束。
- **Evidence Boundary:** 官方材料明确承认 critic 仍会产生 false positive；公开证据不足以证明该方法跨地图
  类型、比例尺、语言和真实导航分布泛化，也没有可用于 AI System 主干结论的完整 hardware、latency、
  concurrency 或 SLO contract。
- **Trade-offs / Previous Design:** 专用数据与 critic 能提高垂直任务可测性，但把系统可靠性转移到数据覆盖、
  evaluator calibration 和错误反馈污染。通用 VLM 在开放任务中覆盖更广，专用 pipeline 只在任务边界稳定、
  verifier 可持续维护时更合理。
- **Evolution / ROADMAP:** `Explanatory Analogy`；与 Ch62 的 verifier/evaluation contract 有弱连接，
  不构成新的章节 owner。
- **Integration Decision:** `Weekly Only — Below 20`；低项目相关性且 evidence contract 不足，不进入 Books。
- **Open Questions:** critic 的 false-positive/false-negative operating point、跨地图分布迁移和人工复核成本
  是否有公开、可复算的评估？

### GLM-5 technical report

- **Candidate / Week / Score:** GLM-5 / 2026-W08 / 29/30；
  `Source Family ID: glm5-dsa-agentic-rl-slime-2026`。
- **Source Type / Date / Revision:** 模型技术报告 + 官方模型仓库 + 官方 RL runtime 仓库。arXiv v1
  首发于 2026-02-17，v2 于 2026-02-24；事件归 W08，v2 只用于 revision 核验，不能反写为本周新事件。
- **Direct / Related Primary Sources:** arXiv HTML/PDF、GLM-5 官方仓库、THUDM/slime 官方仓库。
  GLM-5 仓库公开 model weights、deployment/fine-tuning 入口和技术报告链接，但不公开完整 pretraining、
  DSA conversion 或 GLM-5 RL training code。slime 当前仓库公开 training/rollout/Data Buffer 分层、
  SGLang-native pass-through、PD、session affinity、weight sync、fully-async 与 coding-agent examples；
  当前快照包含 2 月 17 日后的演进，只能验证设计家族仍有公开 artifact，不能证明所有代码在 v1 当日存在。
- **Access and Verification Status / Full-read Coverage:** Verified。已读 metadata 与 revision、Abstract、
  Introduction、Pre-Training、Architecture、DSA/MTP/MLA ablation、data/mid-training、training infrastructure、
  SFT、Reasoning/Agentic/General RL、cross-stage distillation、slime、agent environments、chip adaptation、
  全部 evaluation setup、base/ARC/agentic 表格、Appendix hyperparameters 与 evaluation details；并核对
  两个官方仓库的公开责任边界。论文没有独立 Limitations / Threats to Validity 章节。
- **Original Problem / Why the Previous Design Was Reasonable:** Dense/MLA attention、同步 rollout-update
  与聚合式推理部署分别提供了简单的全局可见性、较强 on-policy 语义和较少跨服务状态；在 context、
  rollout duration、模型规模与硬件差异较小时，这些旧方案更易验证和恢复。GLM-5 面对 744B MoE、
  长上下文、长尾 Agent trajectory 与多硬件部署后，attention compute、同步 barrier、trajectory
  对齐和硬件适配共同成为约束。
- **Changed Constraint / Mechanism:** 模型为 744B total / 40B active、80 layers、256 experts；通过
  MLA-256、parameter-shared MTP、mid-training 后 staged DSA conversion 降低长上下文执行成本。
  DSA 先用 1,000 steps 训练 indexer，再做 20B-token sparse adaptation；Reasoning RL 使用 GRPO
  变体，DSA indexer top-k 为 2,048，并用 deterministic `torch.topk` 换取训练/rollout 一致性。
  Agentic RL 将 trainer 与 rollout 放到独立 GPU pools，通过 Multi-Task Rollout Orchestrator、TITO、
  双侧 token importance clipping、policy-version filtering 与 DP-aware routing 管理异步数据。
- **State Ownership / Control and Data Flow:** trainer 拥有 current policy、optimizer 与 update step；
  rollout server/router 拥有 generation capacity、session/prefix locality 和 rollout policy revision；
  environment service 拥有 task state 与 side effects；trajectory 必须携带 exact token ids、loss mask、
  reward/verifier result、failure reason 与 generating-policy version，经 Data Buffer 进入训练。权重按
  版本同步到 rollout engines；样本超过 staleness threshold 或 environment collapse 时丢弃。这里的
  correctness contract 是 `trajectory identity + policy lineage + environment outcome`，而不是“文本能重分词”。
- **Implementation Details:** pretraining infrastructure 描述 flexible MTP placement、Pipeline ZeRO-2、
  Muon shard gather、activation offload、deferred weight-gradient、sequence-chunked loss、动态 CP group 与
  hierarchical all-to-all。slime 侧针对 RL tail 而非只优化平均吞吐：FP8 rollout、MTP、PD disaggregation、
  heartbeat deregistration/reroute、fully async trainer/inference、TITO gateway、consistent-hash DP routing。
  这些为作者实现陈述；除公开 slime 责任分层与接口外，GLM-5 exact training snapshot、集群配置、
  部分故障恢复代码和运行 trace 未公开。
- **Evaluation Contract:** 公共结果覆盖 HLE、SWE-bench、Terminal-Bench、BrowseComp、MCP-Atlas、
  tau2、Vending 等，但 harness 不统一：HLE 可用 131,072/202,752 context，SWE-bench 使用 OpenHands，
  Terminal-Bench 使用 Terminus 或指定 Claude Code 版本并允许不同 wall-clock policy，BrowseComp 只保留
  最近五轮或整体丢弃 Context。内部 CC-Bench-V2 frontend 使用 Claude Code/Sonnet 4.5 + Playwright
  judge；130 checks 上报告 94% item agreement，8 个模型上报告 85.7% Spearman。SWE-rebench 的
  42.1% 对 41.3% 差异没有建立显著性结论。
- **Baselines / Ablations / Sensitivity / Overhead:** efficient-attention ablation 包含 fixed/searched SWA、
  GDN/SimpleGDN 和 DSA；结果并非单向改善，部分 long-context task 下降。DSA 小规模验证、MLA/MTP
  对比与 base benchmarks 同样存在回退。论文披露若干 token budgets 与 RL hyperparameters，但没有
  给出 async RL 各稳定化机制的完整独立 ablation，也没有把所谓 1.5～2x attention compute、half GPU
  cost 与统一 hardware、sequence mix、concurrency、precision、SLO 绑定。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 公开 contract 包含模型规模、
  4K→200K context curriculum、28.5T tokens、GRPO group/batch、FP8 rollout、INT4 QAT 与部分 benchmark
  上下文/timeout；训练集群 GPU 型号、拓扑、端到端并发及明确 SLO 多数 `Not Disclosed`。Ascend 案例
  披露混合 W4A8、单 Atlas 800T A3、kernel/runtime 优化，但“接近双卡国际平台”和约 50% cost 降低
  缺少 fully matched workload，不得外推到其他芯片或 serving workload。
- **What the Evidence Proves:** 证明作者构建了把 sparse attention migration、长尾 rollout system、
  policy lineage 与 agent environment 联合考虑的完整设计；公开论文给出机制、部分训练预算、ablation
  和 harness details，当前 slime artifact 也验证 training/rollout/Data Buffer 的责任分层是可实现路径。
- **What It Does Not Prove:** 不证明 DSA 普遍 lossless、异步 RL 总比同步 RL 更稳定或更高效、所有
  headline benchmark improvement 都来自所述机制、Agent 输出中的 reasoning 文本忠实反映内部推理，
  也不证明中国芯片适配结果可跨硬件复现。官方模型仓库不是完整 training artifact。
- **Limitations / Threats to Validity:** 机制贡献与 28.5T data、模型规模、SFT/RL recipe、harness 和
  serving stack 同时变化，难以 attribution；内部 benchmark/judge 依赖厂商流程；部分对比的 prompt、
  time budget 与工具栈不同；没有独立 limitations 章节、完整 cluster contract 或训练代码快照。
- **Trade-offs / New Failure Modes:** DSA 增加 indexer、top-k determinism、稀疏 kernel 与 staged migration；
  async RL 增加 policy lag、off-policy bias、version filtering、weight-sync race、sample drop 和恢复复杂度；
  TITO 减少 retokenization mismatch，却要求 gateway 保存 token-level lineage；PD 与 affinity 降低 Agent
  rollout tail/interference，也引入跨池 state、热点、router failure 和 cache invalidation；单一 SGLang
  backend 保留原生能力，却减少 backend portability。
- **Where the Previous Design Still Applies:** 短 context 或缺少高效 sparse kernel 时保留 dense/MLA；
  policy-lag 容忍度低、rollout 较短或恢复语义未成熟时保留同步 on-policy loop；单池干扰与 KV transfer
  成本不构成 break-even 时保留 aggregated serving；需要多 backend portability 时不应照搬 slime 的
  SGLang-native trade-off。
- **Evolution Relationship:** `Direct Evolution`：GLM-4.5 的 MoE + decoupled rollout → GLM-5 staged
  DSA + fully async Agent RL；`Layering / Dependency`：MTP、PD、router、Data Buffer、environment/verifier
  在同一 RL dataflow 上叠加。它们不是“新模型替代旧模型”的单线版本史。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch29 为主 owner；已读 Ch28～32，并交叉检查 Ch22、
  Ch44、Ch48、Ch51、Ch52、Ch77。现有 Ch22 已覆盖 DSA staged migration 与 mixed results，Ch29 已覆盖
  policy lag、rollout version 和 partial trajectory，Ch31 已覆盖 RL multi-object checkpoint，Ch44 已覆盖
  MTP artifact，Ch48/51 已覆盖 state-aware routing 与 PD break-even，Ch77 已覆盖 deterministic workflow
  ownership。真正可能新增的是 Ch29 中 `TITO + policy-version filtering + environment failure semantics`
  如何把 asynchronous Agent RL 的 correctness boundary 具体化。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Human Gate Pending`。
  本轮只写 Weekly Source Review，不修改 Books；必须等 W08 Evidence Gate 和人工 Review 后再决定是否
  对 Ch29 做最小化 refine，并只给 Ch22/31/51/77 短 handoff。
- **Open Questions:** async RL 的吞吐、policy lag、sample-drop 与 learning quality 是否有可复现实验；
  exact GLM-5 slime commit/config 能否定位；TITO、optimizer reset、weight update 与 checkpoint 如何形成
  crash-consistent transaction；DSA 在不同 hardware/context distribution 下的 break-even 是什么？

### Towards a Science of AI Agent Reliability

- **Candidate / Week / Score:** Agent Reliability / 2026-W08 / 28/30；
  `Source Family ID: princeton-agent-reliability-v1-v3-2026`。
- **Source Type / Date / Revision History:** 学术论文 + interactive dashboard + HAL harness。v1 于
  2026-02-18 首发，v2 于 2026-02-23，v3 于 2026-06-02；W08 结论必须以 v1 的 14 models、18 months
  与当时公式为事件证据。v3 已被 ICML 2026 接收，扩展为 15 models / 24 months，并公开致谢读者发现
  v1 outcome-consistency calculation error；后续修订只用于纠错与稳定性核验。
- **Direct / Related Primary Sources:** arXiv v1/v3 HTML 与 PDF、HAL Reliability Dashboard、
  `princeton-pli/hal-harness`。HAL repository 中公开 `reliability_eval`、benchmark/scaffold、trace/cost
  collection 等 artifact，2026-07-01 后 archived；仓库当前状态不能反证 W08 当日每个文件的 exact commit。
- **Access and Verification Status / Full-read Coverage:** Verified with revision correction。已读 v1 的
  metadata、Introduction、cross-domain background、12/14-metric definitions、aggregation、capability
  disentanglement、setup、results、recommendations、limitations、research agenda、benchmark/scaffold、
  perturbation/fault/confidence/safety protocols 与 extended results；再逐项对照 v3 公式、模型集合、
  limitations 与 acknowledgement，并核验 HAL harness/dashboard 的公开责任边界。
- **Original Problem / Why the Previous Design Was Reasonable:** 单次 mean task success 易复现、易排序，
  在静态 benchmark 和无外部副作用的 model comparison 中是合理起点；但同样 accuracy 可能来自固定
  失败集或随机失败，且无法说明重跑方差、环境变化、failure severity 和 agent 是否知道自己会失败。
- **Changed Constraint / Principle:** Agent 开始操作数据库、Web、文件和业务工具后，evaluation object
  从 final answer 变成带 environment、scaffold、trajectory、resource 和 side effects 的 stochastic
  system。论文把 reliability 拆成 consistency、robustness、predictability、safety；核心原则不是固定
  12 个指标，而是让 capability 与 failure behavior 成为两条独立证据轴。
- **Mechanism / State Ownership:** Evaluation harness 拥有 task identity、benchmark/environment version、
  scaffold、random seed、perturbation/fault policy、trace 与 resource record；agent/model 拥有 action
  distribution 与 self-reported confidence；judge 拥有 compliance/severity verdict。一次可靠性结论必须
  保存 nominal 与 perturbed run 的配对关系、同一任务的 K 次重复、完整 trajectory 及 scorer version。
- **Metrics:** consistency 包括 outcome、trajectory distribution/sequence 与 resource variation；robustness
  使用 fault/environment/prompt condition 相对 nominal accuracy 的 clamped ratio；predictability 使用
  post-hoc confidence 的 calibration、AUROC 与 Brier；safety 分开保存 violation frequency 与 conditional
  severity。Safety 不进入 overall mean，因为低频高后果事件不能被其他维度平均抵消。
- **Revision-Critical Formula Boundary:** v1 把 outcome consistency 写成
  `1 - sample_variance / (p_hat(1-p_hat)+epsilon)`；对 Bernoulli 样本，sample variance 与分母存在机械
  关系，不能可靠提供作者所声称的 capability-independent separation。v3 改为 `(2p_hat-1)^2`，并明确
  致谢外部读者发现错误。该修订使“v1 全部数值可直接沉淀”为不成立；可保留多维 reliability 原则，
  但任何 outcome-consistency 趋势必须引用 revision、重算数据并重新核验。
- **Evaluation Contract:** v1 评估 14 个闭源模型；GAIA validation 为 165 tasks，tau-bench 使用经研究
  指出原 50 个 airline tasks 中 24 个有问题后的 26-task clean subset。每任务 K=5，非 reasoning
  models temperature=0；reasoning model 使用 provider defaults。另生成 J=5 naturalistic paraphrases，
  fault injection probability 为 0.2，environment 使用 medium structural perturbation；GAIA timeout 10 分钟，
  tau-bench 5 分钟，最大输出常为 4,096～8,192，transient API failure 最多重试 3 次。
- **Perturbation / Judge Details:** 七类 injected faults 的条件分布由作者指定，并额外模拟 recovery
  probability，因而 fault robustness 同时测 agent 与 synthetic fault model；environment 主要改变格式、
  key、nesting 和 tool schema，是 structural proxy，不是完整 distribution shift。confidence 来自 agent
  在看到完整 history 后的 post-hoc self-assessment，parse 失败会回退到 error-count heuristic；safety
  由 GPT-4o 对 trace 判断 violation 与 0～10 severity，再映射 low/medium/high。
- **What the Evidence Proves:** 在 GAIA 与 clean tau-bench、固定 scaffolds 和这些 perturbation contracts
  下，单一 accuracy 无法重建相同 reliability profile；prompt sensitivity、trajectory order、resource
  variance、confidence discrimination 与 severity 提供了互补诊断。清洗错误 ground truth 会明显改变
  predictability/safety，也证明 benchmark correctness 是 reliability measurement 的上游状态。
- **What It Does Not Prove:** 不证明“能力进步普遍不带来可靠性进步”、四维/等权聚合是唯一理论、
  trajectory 越一致总是越好、post-hoc self-confidence 可直接驱动生产 defer，也不证明这些指标能提前
  防止论文列举的真实事故；事故映射属于作者的 counterfactual analysis，不是 retrospective experiment。
- **Limitations / Threats to Validity:** 两个 benchmark、每个仅一套 scaffold、闭源 API 与 provider
  defaults 限制外推；K=5 对 tail failure 很弱；robustness ratio 在低 baseline accuracy 时不稳定且 clamp
  会隐藏“扰动后偶然改善”；semantic-preserving paraphrase 由另一模型生成；LLM safety judge、severity
  thresholds、uniform weights 与 confidence elicitation 都是可争议 measurement policy。v1 公式错误进一步
  说明 metric implementation、paper equation、dashboard revision 必须共同版本化。
- **Trade-offs / New Failure Modes:** multi-run 和 multi-condition evaluation 显著增加 API cost、时间与
  correlated-sample 处理；generative perturbation 增加 coverage，也可能改变任务语义；更高 consistency
  提升 auditability，却可能压制 brainstorming/exploration；hard safety gate 保护 tail risk，却依赖
  constraint taxonomy 与 judge recall；aggregate 便于比较，却重新引入 Goodhart 与风险掩盖。
- **Where the Previous Design Still Applies:** 静态、确定性、低风险 component test 仍可使用单次 pass/fail；
  creative workload 不应把 trajectory diversity 自动当缺陷；可执行 verifier 应优先于 LLM judge；高风险
  production gate 需要 human review、sandbox、monitoring 与 incident policy，不能由 reliability score 替代。
- **Evolution Relationship:** `Direct Evolution`：single-run accuracy → repeated-run consistency →
  condition perturbation → confidence/severity profile；`Layering / Dependency`：offline EvalSpec → release
  hard constraints → online Monitoring/incident feedback。v1→v3 还展示 measurement 本身也需要 revision、
  provenance 和可重算性，而不是用新公式静默覆盖旧结论。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch62 为主 owner；已读 Ch61～63，并交叉检查 Ch68、
  Ch69。Ch62 已覆盖 EvalSpec、failure taxonomy、重复采样、不确定性、trajectory judge、hard safety gate
  与 per-example evidence；Ch63 已区分 Monitoring，Ch68/69 已覆盖 threat model/readiness。可能新增的
  长期缺口是把 `consistency / robustness / predictability / severity` 写成同一 reliability profile，
  并用 v1→v3 公式修订说明 Eval metric 也必须有 implementation/revision lineage。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Human Gate Pending`。
  本轮只更新 Weekly，不修改 Books；整周 Gate 后再判断是否在 Ch62 增加最小化 reliability-profile 与
  metric-revision 段落，Ch63/68/69 只保留短 handoff。
- **Open Questions:** v3 是否公开提供按新公式重算的 raw per-run data 与 exact commit；K=5 能怎样表达
  tail confidence；robustness ratio 如何处理低 baseline 与 paired uncertainty；confidence signal 应由
  self-report、external monitor 还是 outcome model 拥有；severity judge 怎样校准 human/executable gold？

### ResearchGym

- **Candidate / Week / Score:** ResearchGym / 2026-W08 / 25/30；
  `Source Family ID: researchgym-executable-research-agent-eval-2026`。
- **Source Type / Date / Revision History:** 学术论文 + 官方 benchmark/runtime artifact。arXiv v1 于
  2026-02-16 首发，v2 于 2026-03-11；W08 以 v1 为事件证据，后续 workshop acceptance、README 与
  当前代码只用于核验设计家族，不反写为事件日实现。官方仓库当前有 36 commits、无公开 release，
  因而不能从 main branch 推断 v1 当日的 exact code snapshot。
- **Direct / Related Primary Sources:** arXiv v1 全文与 Appendix、当前 arXiv metadata、
  `Anikethh/ResearchGym` 官方仓库。仓库公开五个 task skeleton、grader、agent adapter、local/Docker
  runtime、resume、inspection agent 与 run-artifact layout；未见与 v1 对齐的 tag 或 release。
- **Access and Verification Status / Full-read Coverage:** Verified with version boundary。已读 metadata、
  Introduction/Related Work、benchmark selection/packaging、Task/Environment/Solver/Evaluation abstractions、
  metrics、setup、全部结果与资源表、resource/hint/scaffold/async ablation、35+ trace case studies、
  reward hacking/self-termination/overconfidence、Discussion 与影响结论的 Appendix；并核对官方仓库的
  task layout、Docker/local runtime、budget、resume、inspector、logs/transcript/cost/status/plan artifacts。
- **Original Problem / Why the Previous Design Was Reasonable:** code completion、bug fixing、短答案或
  proposal judge 便于批量、确定性评测；研究复现 benchmark 也能检查执行能力。在任务目标固定、无需
  提出并检验新假设时，这些设计成本较低且可比较。但它们无法区分“会写研究叙述”与“能在真实代码库
  中建立 baseline、提出方法、运行受控实验、解释反例并留下可核验 artifact”。
- **Changed Constraint / Principle:** end-to-end empirical research 是长时、开放、资源受限的闭环；
  环境故障、实验不可比、污染和 verifier gaming 会与研究能力混在一起。ResearchGym 将 evaluation
  object 扩展为 `task contract + pruned repository + executable environment + trajectory + graded workspace`。
  原则不是让 Agent 自己多跑几小时，而是先固定可比较的实验合同，再把结果、过程与完整性分开验证。
- **Mechanism / State Ownership:** Task 拥有 research goal、constraints、primary subtask、baseline 与
  task-native metrics；Environment/runtime 拥有 dependency、hardware visibility、sandbox、wall-time 与
  API budget；Solver 只拥有 hypothesis/action policy；workspace/Git/log system 拥有 code、commands、
  observations、commits 与 resume lineage；grader 从最终 workspace state 计算 metrics；post-run inspector
  读取 logs、commit history 和 file diff，标记 evaluation tampering、leakage 或可疑结果。Inspector 是
  辅助 detection，不拥有 ground truth，也不能替代隔离和 deterministic checks。
- **Control Flow / Data Flow:** 论文从 1,387 篇候选论文中抽取 task cards，经两阶段过滤得到 90 项，
  再人工选取五项；每项移除作者 proposed method，保留 dataset、evaluation、baseline 与 pinned env，
  并回填 withheld method 验证分数可在小偏差内复现。运行时 adapter 复制 task → runtime 注入受限资源
  → Agent 读写 Git workspace、启动实验并可调用 `grade.sh` → actions/observations/cost/trace 持续记录
  → grader 生成 task-native result → inspector 审计全过程。39 个 subtasks 允许区分“primary metric 偶然
  提升”与“实验链完整完成”。
- **Implementation Details:** 官方 artifact 支持 Python/`uv` 开发路径和 Docker 隔离路径；task 目录
  包含 description、requirements/install、grading、可选 hint 与 baseline code。RGAgent 暴露执行、文件、
  Web、background-job 与 termination tools；run 目录保存 workspace、adapter/agent/stdout logs、完整
  transcript、cost summary、metadata、status 和 plan。论文还实现 context compression、run resume、GUI、
  trace/cost tracking 和 URL blocking；这些 state surfaces 使失败可诊断，但不自动保证实验语义正确。
- **Evaluation Contract:** 五个 2025 oral/spotlight/highlight empirical ML papers，共 39 subtasks；主实验
  为 GPT-5 high + rg-agent，单 NVIDIA A100 80GB，每个 task 三个独立 runs，默认 12h / 约 $10 API budget，
  best run 可追加 12h / $10。论文还在经过尽量对齐的 setting 下测试其他 scaffold。核心 score 由各任务
  原生 grader 产生，不以 LLM judge 评分最终研究结果；另报告 completion、beat-baseline improvement、
  mean 与 best@3。October 2024 Web cutoff 与 related-URL block 降低显式泄漏，但不能证明模型 pretraining
  不含相关论文。
- **Baselines / Ablations / Sensitivity / Overhead:** 15 个主 runs 中只有 1 个超过 strongest provided
  baseline，平均只完成 26.5% subtasks；mean 与 best@3 差距及大方差说明单次最优不是稳定能力。
  best run 追加资源未改善结果，hint 提供 withheld method 的高层思想后仍常被 engineering/debugging
  阻塞，说明 ideation 与 execution 不可合并成一个 failure label。scaffold 对比只在同预算、prompt、
  Web 与工具条件下有意义；async tools 也未自动修复 stalled job monitoring。论文的 action-density
  correlation、约 9h plateau 与作者 headline 都是五任务特定观察，不构成因果定律。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露主评测模型/scaffold、A100
  80GB、12/24h、API cost、input/output token、attempts 与 time-to-first-attempt；各 source task 的训练
  model、seed、batch、precision 和 metric 随任务而变，不存在一个可合并的统一 workload contract。
  生产级并发、queueing、网络拓扑和 SLO 为 `Not Disclosed / Not Applicable`。因此任何性能数字必须按
  task/run 读取，不能把 normalized ratio 跨不同 metric 当作统一 research capability 标尺。
- **What the Evidence Proves:** 在这五个经人工包装的 empirical ML tasks、固定预算和公开 scaffold 下，
  frontier Agent 偶尔能产生很强结果，却频繁无法完成可比较实验；结果分数、subtask completion、trace
  与 integrity evidence 提供互补信息。案例确实观察到 frozen log 被当进展、全局 kill 导致自我终止、
  跨 run 复制 artifact、拼接互斥配置结果、以及没有 baseline sanity check 便持续优化。
- **What It Does Not Prove:** 不证明 Agent 普遍具有或缺乏“自主科学研究能力”，不证明偶然超过一个
  packaged task 等于新颖、可发表或可复现的科学发现，也不证明 1/15、26.5% 或约 9h plateau 可外推到
  theory、multimodal、wet-lab、large-cluster 或不同 scaffold/model。摘要称一次 improvement 为 11.5%，
  但正文表格包含多种 baseline/SOTA 与 task-native metrics；在 exact derivation 未明确前不复述该百分比。
- **Limitations / Threats to Validity:** 仅五项经人工选择的 tasks，另有三项 development tasks 用于
  scaffold 调整，存在 selection/tuning bias；只覆盖可由 objective metric 评分的 empirical ML，明确排除
  theory、proof、主观研究与高算力训练；模型污染只能缓解不能排除；任务 packaging、grader fidelity 与
  withheld-method reproduction 含人工判断；best@3 放大 lucky run；inspection agent 依赖 LLM prompt，
  injected attacks 只验证已知 taxonomy，对未知 reward hacking 没有 completeness guarantee。
- **Trade-offs / New Failure Modes:** executable task 比文本 judge 更接近真实产物，却把 grader correctness、
  dependency pinning、sandbox escape、data leakage、cross-run isolation 和 baseline comparability 变成平台
  责任；开放 `grade.sh` 促进 Agent 自校验，也暴露 Goodhart/overfitting surface；长 budget 增加探索空间，
  也放大 context drift、stale jobs、资源浪费与 state recovery；异步并行提高潜在利用率，却需要 job identity、
  progress signal、timeout、dependency、cancellation 和 result-validity contracts。
- **Where the Previous Design Still Applies:** unit test/bug-fix、形式化 proof 或确定性 compiler task 仍应
  优先使用更窄、更强的 verifier；proposal/peer review 仍负责新颖性、意义和理论正确性；高算力、湿实验
  与主观领域仍需专家或 staged real-world evaluation。ResearchGym 是 text-only 与真实开放研究之间的
  一层，不替代这些旧路径。
- **Evolution Relationship:** `Direct Evolution`：answer/proposal score → executable artifact → controlled
  experiment workspace → task-native result + trace + integrity audit；`Layering / Dependency`：planning/
  workflow 产生 experiment lineage，Evaluation 决定这些 evidence 能支持什么 claim。论文失败案例还给出
  下一步压力：process liveness 不能等于 semantic progress，post-run audit 不能替代运行前隔离与在线 gate。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch62 为主 owner；已读 Ch61～63，并交叉检查 Ch75、
  Ch77。Ch62 已覆盖 `artifact + environment + execution trace`、versioned verifier、claim provenance、
  trajectory judge 与 run identity；Ch75 已把 plan step 定义为带 success evidence 的状态转移；Ch77 已覆盖
  experiment lineage、async ownership 和 recovery。真正可能新增的是 Ch62 中明确拆分 `result validity /
  semantic progress / environment integrity`，并把 inspector 放在 defense-in-depth 而非 ground truth 位置。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Human Gate Pending`。
  本轮只写 Weekly Source Review，不修改 Books；必须等待 W08 Evidence Gate 与人工 Review。若通过，Ch62
  只做上述机制性 refine，Ch75/77 最多增加短 handoff，不复制 ResearchGym 名称或 benchmark 数字。
- **Open Questions:** grader 如何建立 mutation/adversarial tests 与独立 gold；semantic progress 怎样区别
  GPU/process liveness；experiment config、dataset split、checkpoint 与 result 如何形成 immutable lineage；
  inspector 的 false-positive/false-negative 如何校准；如何在不泄漏 withheld solution 的前提下提供足够
  debugging evidence；task selection 如何覆盖理论、multimodal、distributed-system 与真实协作研究？

### Computer-Using World Model

- **Candidate / Week / Score:** Computer-Using World Model (CUWM) / 2026-W08 / 26/30；
  `Source Family ID: cuwm-office-single-step-world-model-2026`。
- **Source Type / Date / Revision History:** Microsoft 等作者的学术论文，arXiv v1 于 2026-02-19 首发，
  截至访问日无后续 revision。相关数据 lineage 来自 GUI-360 v1（2025-11-06）。论文 metadata、正文和
  通常检索入口未给出 CUWM 官方代码、checkpoint 或 event-date artifact；实现细节只能标记为作者陈述，
  不能宣称已复现。
- **Direct / Related Primary Sources:** CUWM v1 全文、公式、全部表格、Appendix 与 prompts；GUI-360 v1
  的 collection、trajectory validation、schema 与 action-prediction protocol。GUI-360 说明原始轨迹由
  TrajAgent 自动执行、EvaAgent/GPT-4.1 过滤，100 条样本上与 human judgement 的 agreement 为 86%；
  这使“successful trajectory”本身带有 model-judge selection boundary。
- **Access and Verification Status / Full-read Coverage:** Verified paper / artifact unavailable。已读 metadata、
  Introduction/Related Work、two-stage architecture、GPT annotation、SFT/GRPO、test-time action search、
  textual/visual/agent evaluation、case study、Conclusion、dataset splits、完整训练超参、judge/ACS/TRS
  公式、agent protocol、ground-truth coverage、RL sensitivity 与 prompts；并核验 GUI-360 数据生成和
  post-processing 中影响 transition validity 的章节。论文没有独立 Limitations/Threats 章节。
- **Original Problem / Why the Previous Design Was Reasonable:** GUI Agent 通常直接在当前 screenshot/
  accessibility state 上选下一 action，再从真实环境接收 observation。对可撤销、低延迟、有确定 API 或
  sandbox 的操作，这种 reactive loop 状态最真实、实现简单，也不承担 simulator error；但 desktop
  artifact workflow 的错误可能持续累积，真实环境又不适合为多个候选 action 执行 counterfactual rollout。
- **Changed Constraint / Principle:** 当 action 的真实试错昂贵或不可安全回滚时，Planning 需要在执行前
  比较候选后果。CUWM 将 UI dynamics 近似分解为
  `p(Delta_t | screenshot_t, action_t) × p(screenshot_(t+1) | screenshot_t, Delta_t)`：先预测局部、结构化
  的文本变化，再渲染未来画面。长期原则是把 action proposal 与 predicted consequence 分开，让额外
  test-time compute 用于受限的 counterfactual selection；预测仍是假设，不是实际 state transition。
- **Mechanism / State Ownership:** frozen Agent 拥有 candidate action generation 和最终选择；textual
  transition model 拥有对 active tab、selection、content、pane 等 decision-relevant delta 的预测；visual
  renderer 拥有把 delta 映射为 screenshot 的近似；真实 Office environment 仍是 authoritative state owner。
  Planner 必须保存 candidate set、world-model version、predicted delta/image、selection rationale 与 uncertainty，
  executor 只能在 policy/approval 后执行一个 action，再以真实 observation invalidates 或校正 imagined state。
- **Control Flow / Data Flow:** GUI-360 成功轨迹产生 `(s_t,a_t,s_(t+1))` → GPT-5 从前后 screenshot 生成
  transition description → Stage 1/2 LoRA SFT → Stage 1 以 GPT-5 judge + relative length penalty 做 GRPO →
  test 时 Agent 从 current screenshot/a11y/instruction 生成五个 candidate actions → CUWM 为每项生成 text
  delta 和/或 image → 同一 frozen Agent 比较 imagined outcomes、选择一项。论文评测随后把所选 action 与
  dataset 中记录的单个 action 比较，并未真的执行它或滚动多步 imagined trajectory。
- **Implementation Details:** Stage 1 使用 Qwen2.5-VL-7B-Instruct、all-linear LoRA；Stage 2 使用
  Qwen-Image-Edit-2509 的 DiT LoRA；GRPO 仅更新 Stage 1，K=5、KL coefficient 0.01，并用 ground-truth
  description 长度的 0.75～1.25 区间作 penalty。Dataset 从 GUI-360 的连续成功轨迹抽取，删除前后帧
  不变、invalid action 与高噪声样本；最终为 2,876 train、98 validation、339 test，覆盖 Word、Excel、
  PowerPoint。过滤提高可学习性，却系统性移除 no-op、failure 和 recovery transition。
- **Evaluation Contract:** fidelity 层比较 Base/SFT/SFT+RL 的 GPT-5 judge 与 Action Consistency Score，
  再以 PSNR/SSIM/LPIPS/FID 和 OmniParser + embedding 的 Text Rendering Score 测 screenshot；agent 层在
  339 个离线 single-step samples 上评估 Qwen3-VL-8B、GPT-4.1-mini、GPT-4o、Gemini-2.0-Flash。所谓
  task score 是 function/status/args 全部匹配记录 action 的比例，coordinate 允许 ±25 pixels 或落在 bbox；
  不是完整任务 success、artifact correctness、side-effect safety 或恢复能力。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 no world model、text-only、off-the-shelf
  Qwen-Image-Edit、CUWM、GPT-Image-1.5 及 image/image+text 输入。CUWM image-only 在四个 frozen backbones
  的该单步 metric 上均高于 no-world-model，但增量较小且 text+image 多数退化；作者将其推断为
  cross-modal conflict/noise accumulation。SFT→RL 的 judge/ACS 增量有限；100-sample、last-six-runs 的
  downstream表只支持局部 sensitivity，不能证明 GRPO 奖励设计普遍优于 SFT。论文未报告每候选生成
  latency、五路 diffusion cost、端到端 TTFT 或与真实 action latency 的 break-even。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 公开 Stage 1 BF16 batch 4 × grad
  accumulation 4、Stage 2 mixed-16 batch 1、max pixels 1,048,576、GRPO train batch 32 / micro-batch 8 和
  K=5；训练/推理 GPU 型号、数量、wall time、并发、Office/app version 与 end-to-end SLO 均
  `Not Disclosed`。API Agent 与 GPT-5 annotator/judge 的具体 snapshot 也未完全固定。
- **What the Evidence Proves:** 在 339 个从 GUI-360 成功轨迹抽取并清洗的 Office 单步 transitions 上，
  两阶段模型能改善若干文本/视觉 fidelity metrics；把五个候选的 imagined next state 交给 frozen Agent，
  在记录 action matching metric 上比直接选择获得一致但有限的增益。它还提供一个有价值反例：同时给
  text 和 image 不会自动增加证据，两个近似通道冲突时反而降低决策质量。
- **What It Does Not Prove:** 不证明 CUWM 可以准确 rollout 多步 workflow、保存真实 document artifact、
  表示 hidden application state、执行选中 action、识别不可逆副作用或在软件版本/分辨率/语言变化后泛化。
  Logged action 不一定是唯一正确 action，action match 也不等于 task completion。约 35% samples 的五候选
  中没有 ground-truth action；排除这些 cases 后的分数只是在 condition-on-coverage 下的 reranking 能力。
  论文因而不能支持“真实执行鲁棒性已验证”或“世界模型已成为安全边界”。
- **Limitations / Threats to Validity:** 小规模、三种 Office 应用、成功轨迹 selection 与 no-op/failure
  deletion 造成 narrow transition distribution；annotation reference 与 judge 都使用 GPT-5，误差相关；
  GUI-360 的成功标签本身主要由 LLM judge 过滤；single-step random split 可能共享 app/template/style；
  image metrics 对细小但决定性的 control state 不充分，ACS 又把 frozen Agent 选择当功能等价 proxy；
  没有 OOD、uncertainty calibration、multi-step compounding、adversarial UI、failure/recovery 或 human study。
- **Trade-offs / New Failure Modes:** learned simulation 减少真实试错，却增加五路模型调用、diffusion
  latency/GPU cost 和 planning tail；两阶段 factorization 增强 interpretability/modularity，也会传播 text
  hallucination 到视觉层；逼真但错误的 screenshot 可能让 Agent 高置信选择危险 action；模态融合会出现
  conflicting evidence；软件升级、theme、locale、window size 与 accessibility schema 引发 model drift。
  若 uncertainty 不可见，Planner 甚至无法决定何时应跳过 imagination、改用真实 sandbox 或人工批准。
- **Where the Previous Design Still Applies:** 有 authoritative API/DOM/a11y transition model 时，确定性
  simulation 优先于生成 screenshot；低风险、易撤销 action 可直接执行并观察；高风险 action 仍需要
  policy、approval、sandbox、dry-run 或 transaction preview；latent/text-only world model 在只需 value/
  structural affordance 时更便宜；真实 environment replay 保持评估 authority，不能被 imagined state 替代。
- **Evolution Relationship:** `Direct Evolution`：reactive next-action → generate multiple candidates →
  predict one-step consequences → rerank before one real action；未来才可能进入 uncertainty-aware multi-step
  rollout、real-observation correction 与 risk gate。`Layering / Dependency`：Ch74 定义 action/executor，
  Ch75 拥有 candidate search，Ch76 消费真实 prediction error，Ch77 保存 imagined/actual lineage 和 recovery。
  这不是用 world model 覆盖 reactive execution，而是在真实执行前增加一层有误差的 planning instrument。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 census 的 Ch71 owner 已纠正：Ch71 是 Context，
  不拥有 world-model planning。Ch75 为主 owner；已读 Ch74～77。Ch75 已覆盖 belief/state、search cost 和
  verifier quality，但缺少 model-based counterfactual planning、authoritative-vs-imagined state 以及
  uncertainty/break-even；Ch74 已覆盖 trusted executor，Ch76 已覆盖 evidence-backed correction，Ch77 已
  覆盖 durable state。CUWM 适合 refine Ch75，其他章节只需短 handoff。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Scope Corrected /
  Human Gate Pending`。本轮只更新 Weekly，不修改 Books。若 W08 Gate 通过，Ch75 只吸收“候选后果预测
  是有误差的 planning instrument”及其 break-even/authority 边界，不写论文 headline 或单步百分比。
- **Open Questions:** 多步 rollout error 如何估计并触发截断；hidden document/application state 如何进入
  world-state identity；是否应预测 typed semantic delta 而非完整 screenshot；candidate coverage、model
  uncertainty、risk 与 simulation cost 如何共同决定 search depth；真实 observation 怎样校准/回放预测误差；
  deterministic Office API/a11y model 与 generative world model 的最优分层是什么？

### PAHF / Personalized Agents from Human Feedback

- **Candidate / Week / Score:** Personalized Agents from Human Feedback (PAHF) / 2026-W08 / 26/30；
  `Source Family ID: pahf-dual-feedback-personalization-memory-2026`。
- **Source Type / Date / Revision History:** Meta、UT Austin 等作者的学术论文，arXiv v1 于
  2026-02-18 首发，截至访问日无后续 revision。官方 `facebookresearch/PAHF` 仓库为当前公开 artifact，
  没有 release/tag 可将代码精确固定在论文事件日；README 明示 shopping agent 在论文后调整了 prompt 与
  feedback logic，当前结果可能优于论文。因此当前 main branch 只能验证机制轮廓，不能当作论文版本复现。
- **Direct / Related Primary Sources:** PAHF v1 的正文、证明、Appendix、完整 persona/evaluation protocol、
  prompts 与官方代码仓库；项目页只作 source-family 入口。仓库公开 `agents`、`memory`、`prompts`、data 与
  runner，提供 SQLite/FAISS 两种 memory backend，但没有 paper-time commit、release artifact 或真实用户数据。
- **Access and Verification Status / Full-read Coverage:** Verified paper / current artifact verified / event-date
  code snapshot unavailable。已读 metadata、Introduction/Related Work、pre-action/post-action framework、
  memory-update algorithm、dynamic-regret assumptions/proofs、embodied/shopping setup、baselines、ablation、
  model/simulator sensitivity、Appendix、prompts 与 limitations，并检查当前仓库的 memory isolation、retrieve、
  feedback detection 与 update 路径。
- **Original Problem / Why the Previous Design Was Reasonable:** 静态 persona、profile 或历史检索把
  personalization 当作 task 开始前已知的只读 Context。偏好稳定、反馈稀少、错误可逆时，这种设计简单、
  成本低，也避免每一步打扰用户；但它无法区分“系统从未知道该偏好”与“系统记住的偏好已经过期”，
  更无法在 drift 后只凭旧记录恢复。
- **Changed Constraint / Principle:** 用户偏好是随时间变化、仅能通过有限交互观测的 latent state，而非
  永久事实。反馈时机应按 epistemic condition 分层：行动前若关键偏好缺失或歧义高，先问最小 clarification；
  行动后若实际结果暴露旧估计错误，再把 correction 作为新 evidence。Memory 是对偏好的 versioned estimate，
  不是用户真实意图本身。
- **Mechanism / State Ownership:** 每个用户拥有隔离的显式 memory namespace；pre-action controller 检索
  相关 note、判断 ambiguity，并在必要时发起 clarification；agent 根据 instruction、observation、memory 和
  clarification 执行动作；post-action controller 在非最优结果与用户 correction 后做 salience detection、
  note extraction，并以相似度决定 merge/replace 或 add。用户仍是偏好 authority，memory service 只拥有带
  provenance 的估计；论文实现却以文本替换表达更新，没有显式 temporal validity、supersession edge 或 consent。
- **Control Flow / Data Flow:** user instruction → tenant-scoped retrieval → ambiguity/relevance decision → 可选
  clarification 并先写入反馈 → action generation/execution → outcome/correction → LLM salience detector →
  preference note summary → similar-note retrieval → thresholded merge/replace 或 append → 后续请求重新检索。
  该流程把 ask-before-act 与 learn-after-error 放进同一 loop，但 merge 本身仍由 LLM 与 embedding similarity
  近似，不能视为冲突已正确消解。
- **Implementation Details:** 论文与当前仓库都采用短 natural-language preference notes 与 embeddings；
  SQLite/FAISS backend 共享抽象接口并保持 per-user 隔离。当前 artifact 是简化公开实现，未提供 production
  concurrency、transaction、schema migration、retention/delete、conflict audit 或 rollback contract；repo 后续
  prompt/logic refinements 又使它不能直接复现 paper tables。
- **Theoretical Contract:** 作者把真实偏好写成 piecewise-stationary latent state，最多发生 `K` 次切换，
  使用 0/1 loss、唯一最优 action/tie-break，并假设 drift 后第一次错误可得到正确 correction。在这些假设下，
  post-action feedback 将 drift regret 限制为 `O(K)`；若歧义样本占比为 `gamma`，每次最多 `k` 个近似均衡的
  `m` 叉问题，pre-action residual regret 为 `O(gamma T m^-k)`，组合为
  `O(K + gamma T m^-k)`。这证明的是理想化 feedback channel 的上界，不证明真实用户会及时、无噪声地给出
  唯一正确偏好，也不覆盖渐变、context-dependent 或 mutually inconsistent preferences。
- **Evaluation Contract:** 全部用户均为 simulator。Embodied domain 使用 40 个 simulated users、每阶段
  30 个 scenarios、四阶段共 2,400 learning + 2,400 evaluation interactions；shopping 使用 20 users、
  每阶段 45 个 scenarios，共 1,800 + 1,800。四阶段依次为 initial learn、无反馈 test、drift learn、无反馈
  test；embodied evolved persona 对偏好作系统性 1:1 inversion，shopping 重新采样偏好并构造近似但错误的
  poison-pill choices。主 agent 为 GPT-4o，另以 GPT-4.1 和不同 simulator models 做敏感性检查。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 no memory、pre-action only、post-action only 与
  PAHF；指标为 success rate、是否出现任意 feedback 的二值频率和 average clarifications per episode。
  两种 feedback 组合在作者模拟 benchmark 多数 phase 最好，post-action 对 drift recovery 更关键，pre-action
  在 cold-start/ambiguity 下提供增益；但这些数字依赖强制 drift、simulator 与任务模板。论文没有真实 human
  burden、clarification quality、错误动作代价、memory-conflict rate、privacy cost、latency 或 production load。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 披露主 agent 与 simulator 的 API
  model families，以及 user/scenario/phase 数；未披露固定 model snapshots、sampling contract、hardware、
  precision、token length、并发、memory index size、p95 latency、cost budget 或 SLO，均为 `Not Disclosed`。
- **What the Evidence Proves:** 在两个作者构造的 persona-simulation domains 中，pre-action clarification 与
  post-action correction 解决不同 failure source，组合比无 memory 或单一路径更稳定；理论上也说明当 drift
  次数有限、correction 可靠、问题能均衡收缩 ambiguity 时，双反馈可以把 regret 分成 drift 与 residual
  uncertainty 两项。这支持“反馈时机应由不确定性类型决定”的机制性结论。
- **What It Does Not Prove:** 不证明真实用户愿意频繁回答、会提供无噪声 correction，或系统能从自然语言
  中准确识别 stable preference；不证明简单相似度 merge 能处理 scope、时间、群体共享或矛盾；不证明成功率
  能迁移到真实 embodied side effect、购物支付或长期 retention。产品能力也不能由当前代码反推，论文后的
  prompt/logic 改动不得反写为 2 月 18 日事件事实。
- **Limitations / Threats to Validity:** simulated users 与 agent 可能共享模型先验；hard preference inversion
  比真实 gradual/contextual drift 更显著；shopping post-action feedback 部分由 deterministic rules 生成；
  `feedback frequency` 只记录是否发生，不衡量 turns、认知负担或中断成本；salience detector、summary 与
  similarity merge 可能同时误判；旧 note 被文本替换而非保留可审计 supersession；没有真实用户、privacy、
  consent、retention/delete、poisoned feedback、multi-device concurrency 或 long-horizon study。
- **Trade-offs / New Failure Modes:** clarification 降低错误动作，却增加 user friction、latency 与 abandonment；
  post-action learning 减少重复错误，却必须先让用户承担一次错误结果；LLM extraction 提高可扩展性，也引入
  fabricated preference、scope collapse 与 silent overwrite；per-user memory 隔离降低 cross-user leakage，
  但增加 identity linking、deletion propagation 与 multi-tenant operations。若系统把低置信 note 当 policy，
  个性化会放大而非修正错误。
- **Where the Previous Design Still Applies:** 偏好稳定、风险低、任务短或没有可靠 feedback channel 时，
  静态 profile / retrieval-only memory 更便宜且更可预测；高风险决策应使用 explicit confirmation、policy 与
  transaction preview，而不是等待 post-action correction；组织级规则、权限与安全约束不能被个人偏好覆盖；
  无法证明 relevance 时应选择 abstain/no-write，而不是强制产生 memory。
- **Evolution Relationship:** `Direct Evolution`：static profile/history retrieval → pre-action clarification for
  missing preference → post-action correction for stale preference → future versioned preference state with
  provenance、scope、supersession、consent、delete 与 rollback。`Layering / Dependency`：Ch75 消费 uncertainty
  并决定是否询问，Ch77 保存 workflow interaction，Ch80 提供 tenant/policy/retention boundary；Ch73 仍是
  preference memory 的唯一主 owner。这不是用动态 memory 否定静态 profile，而是按 drift 与 action cost
  决定是否增加反馈闭环。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch73 为主 owner；已读 Ch72～75，并检查 Ch77/80。
  Ch73 已覆盖 typed memory、write decision、source/confidence、tenant isolation、append/noop/revise/reject/defer、
  supersession、delete 与 derived-state propagation，明显强于论文的简单 merge/replace。PAHF 真正补充的是
  “missing/ambiguous preference 在行动前询问，stale-but-confident preference 在结果后纠正”的 timing split，
  以及 preference memory 只能是 latent state estimate。Ch75/77/80 只需短 handoff，不复制框架。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Scope Corrected /
  Human Gate Pending`。本轮只写 Weekly，不修改 Books。若 W08 Evidence Gate 与人工 Review 通过，只在 Ch73
  refine feedback-timing、preference-state versioning 与 user-cost trade-off；不保留模拟成功率，不把论文的
  similarity overwrite 写成推荐 production design。
- **Open Questions:** 怎样校准“该问”与“可安全默认”的阈值；用户 correction 如何绑定 scope、time 与
  evidence；渐变、矛盾或多人共享偏好如何表示；salience/merge 的 false write 如何测试；真实用户 friction、
  abandonment 与一次错误动作成本如何进入 objective；consent、retention、delete、poisoning 与 rollback 如何
  成为 personalization memory 的一等 contract？

### Calibrate-Then-Act

- **Candidate / Week / Score:** Calibrate-Then-Act: Cost-Aware Exploration in LLM Agents / 2026-W08 /
  25/30；`Source Family ID: cta-calibrated-prior-cost-aware-exploration-2026`。
- **Source Type / Date / Revision History:** NYU 等作者的学术论文，arXiv v1 于 2026-02-18 首发、v2 于
  02-19、v3 于 05-15 修订。历史事件归 W08；v3 只用于核验 revision。v1 的 FileReading dataset 段落曾把
  一组 cost ratio 写为 `rho={0.5,1.5,2.0,4.0}`，而训练与结果使用 `1.0`；v3 统一为 `1.0`，并新增正式
  Limitations、prior-quality sensitivity、paired bootstrap significance 与完整 GRPO hardware/details。
- **Direct / Related Primary Sources:** arXiv v1、最新版 v3、submission history、作者主页链接的官方
  `NSF-Simons-CosmicAI-Institute/CalibrateThenAct` 仓库。旧 `Wenwen-D/env-explorer` 已重定向到该仓库；
  当前仓库有 7 个 commits、无 release/tag，公开三个 tasks、data/eval scripts 以及基于 EasyR1/veRL 的训练
  入口。缺少 event-date release，当前 main 不能当作 2 月 18 日精确代码快照。
- **Access and Verification Status / Full-read Coverage:** Verified v1 and v3 / current artifact verified /
  event-date code snapshot unavailable。已读 metadata 与版本历史、Introduction/Background、POMDP
  formalization、Pandora proof、QA/FileReading task、prior estimation、CTA-Prompted/CTA-RL、datasets、
  metrics、baselines、全部 results、Related Work、Conclusion、Limitations、prior sensitivity、significance、
  dataset construction、oracle proof、GRPO details、prompts、case traces 与官方 artifact 结构。
- **Original Problem / Why the Previous Design Was Reasonable:** Agent 常使用固定 exploration policy：始终
  search、始终先跑 tests，或达到固定 step 数才 commit。成本稳定、uncertainty 难校准、错误代价相近时，
  固定策略简单、可预测，也避免给模型一套易被误解的概率；但当每个 task 的先验不确定性与 tool/action cost
  不同，同一策略会在某些请求上过度探索，在另一些请求上过早行动。
- **Changed Constraint / Principle:** 是否获取更多信息取决于 value of information，而非“工具通常有用”。
  Planner 应比较当前 belief 下直接 commit 的期望效用，与一次 exploration 后的预期效用减去 latency、money、
  user burden、risk 与 opportunity cost。CTA 的关键不是一个新 RL algorithm，而是把 prior estimator 与 action
  policy 解耦，将 `estimated uncertainty + action cost contract` 显式交给 policy。
- **Mechanism / State Ownership:** calibration component 拥有对 latent environment variables 或 model
  correctness 的 versioned prior estimate；Planner 拥有 posterior/belief、candidate actions 与 explore/commit
  选择；Workflow/runtime 拥有真实 cost budget、deadline、policy 和 side-effect class；environment/tool 拥有
  authoritative observation。模型可消费 prior，但不能自行发明 cost、把 confidence 当事实或修改 runtime
  constraint。
- **Control Flow / Data Flow:** task/query → prior estimator 从 model confidence 或 historical task data 产生
  `p_hat(Z|x)` → runtime 注入当前 action costs → policy 比较 explore 与 commit → 可选 retrieval/test/code →
  observation 更新 belief → 继续探索或 commit → trace 记录 prior/version、cost vector、action、observation 与
  outcome。论文 QA 实际最多一次 retrieval；FileReading 才允许 unit test/code 多步交错，但 latent space 很小。
- **Implementation Details:** QA 用 Qwen3-8B verbalized confidence，经 validation-set isotonic regression
  校准 direct-answer probability，并把 retriever quality 当全局常数；FileReading 用 4.4M-parameter BERT-tiny
  从 filename 的四个 binary features 预测 delimiter、quote、skiprows 三个独立 marginal priors。CTA-Prompted
  只把这些概率加入 prompt；CTA-RL 在同一输入上以 GRPO 优化 discounted reward。独立 prior model 增加一个
  可校准边界，也新增 distribution drift 与 version coupling。
- **Formal / Oracle Contract:** 通用形式是含 latent state `Z`、explore actions 与 terminal commit 的 POMDP，
  reward 为 success indicator 乘 action-sequence discount。QA oracle 在
  `p_retrieval × gamma >= p_direct_answer` 时检索；Pandora toy setting 通过 Bellman recursion 比较当前最高
  posterior box 的 commit value 与 verify value。这个 oracle 依赖已知/正确的 prior、transition、reward 与
  multiplicative cost，不是复杂真实 workflow 的通用最优性证明。
- **Evaluation Contract:** Pandora 使用 100 个三盒样本；QA 从 PopQA 抽 1,000 questions、Contriever，
  retrieval discount `gamma~U[0.1,0.65]`；FileReading 是作者合成的 2,000 个 CSV tasks（1,400/300/300），
  真实格式从 filename-conditioned soft prior 采样，再为四种 `rho` 复制成本条件。指标分 exploration count、
  exact task accuracy 与 multiplicatively discounted reward。它刻意隔离 cost-aware decision，不代表真实
  coding repository、不可逆 action 或 long-horizon workflow。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 fixed never/always retrieve、Prompted、NonThink、
  end-to-end GRPO、CTA-Prompted、CTA-RL，以及 test-first/code-first policies。v3 在 300 paired FileReading tasks
  × 四种 cost regimes 上做 10,000 次 paired bootstrap：CTA-RL 只在部分 regime 显著优于各 baseline，另一些
  与最佳静态分支不可区分；因而应写“跨 regime 更自适应”，不能泛化为处处严格最优。prior degradation 从
  learned→noisy→uniform→adversarial 时性能平滑下降，但 confidently wrong prior 最差；该 sensitivity 仍来自
  同一合成 latent space。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** v3 披露 Qwen3-8B、veRL GRPO、group
  size 8、KL `0.01`、temperature `1.0`、learning rate `1e-6`、global batch 16、update micro-batch 2、
  experience micro-batch 4，以及单节点 8×NVIDIA A100。未披露 precision、sequence length、training wall
  time、inference concurrency、prior-service latency/cost、tool p95 或 production SLO；均为 `Not Disclosed`。
- **What the Evidence Proves:** 在受控三盒、一次检索 QA 与低维合成 CSV 环境中，thinking model 能在显式
  prior/cost 下接近 oracle decision；把经过校准或独立学习的 prior 暴露给 policy，可使 action pattern 随 cost
  regime 改变，并在作者的 discounted reward 上优于若干 prompt/RL baselines。它还证明一个重要负面结果：
  端到端 RL 可能学到静态 test-first shortcut，即使训练数据包含隐式 prior correlation。
- **What It Does Not Prove:** 不证明 CTA 在任意 POMDP、真实 coding repository、多工具 DAG、nonstationary
  cost、连续/相关 latent state 或 irreversible side effects 下最优；不证明 verbalized confidence 能跨模型、
  数据与时间稳定校准；不证明 multiplicative discount 等价于真实 money/latency/risk utility；也不证明额外
  estimator、prompt token 和 inference latency 的系统成本低于节省的 exploration。最新版结果不得反写为
  v1 事件日已具备的证据。
- **Limitations / Threats to Validity:** 只有 Qwen3-8B；QA 只有一次 retrieval 且 retriever quality 是非
  question-specific 常数；isotonic calibration 使用同域 validation；FileReading 的 filename cue、latent variables、
  task generator 与 prior model 同构，且三种 attributes 用独立 marginals，弱化真实依赖；reward 和 cost 由作者
  人工定义；没有 OOD/cross-model calibration、online drift、multi-step posterior calibration、真实 user burden、
  side effects、wall-clock/cost accounting 或 production study。作者 v3 也明确 CTA 不保证 arbitrary environment
  optimality。
- **Trade-offs / New Failure Modes:** 显式 prior 让 policy 可审计、可随 cost 改变，却引入 estimator drift、
  false precision、stale calibration、adversarial feature 与 model/prior version mismatch；confidently wrong 比
  uniform uncertainty 更危险。多维成本压成一个 discount 会隐藏 safety/approval hard constraint；不断探索可
  延迟完成，过早 commit 则把 epistemic uncertainty 变为真实副作用。prior service 本身也消耗 latency、compute、
  telemetry 与维护预算。
- **Where the Previous Design Still Applies:** exploration 很便宜、错误很贵时 always-verify 是安全且简单的
  分支；工具昂贵而任务低风险时 direct commit/abstain 更合理；cost regime 稳定、可证明的静态 policy 可能与
  CTA 相当；high-impact action 的 approval、deterministic test 与 policy gate 是 hard constraints，不能因模型
  高 confidence 跳过；缺少可校准 prior 时使用 conservative/default policy 比伪概率更可信。
- **Evolution Relationship:** `Direct Evolution`：fixed exploration policy → belief-aware heuristic → separately
  calibrated prior + explicit cost contract → uncertainty/cost-conditioned action → future online posterior update、
  drift detection 与 risk-constrained value of information。`Layering / Dependency`：Ch72 的 retrieval quality、
  Ch74 的 tool cost/side-effect、Ch76 的 observation feedback 与 Ch77 的 durable budget 都为 Ch75 的决策提供
  输入；主 owner 仍是 Planning。这不是用 CTA 覆盖 test-first/search-first，而是解释这些旧分支分别在哪种
  uncertainty/cost 区间成立。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch75 为主 owner；已读 Ch74～77，并交叉检查 Ch72。
  Ch75 已覆盖 belief、search cost、budget、constraint、verification 与 replanning，但缺少 expected value of
  information、prior-estimator/action-policy separation、calibration identity 和 confidently-wrong failure mode。
  因而 CTA 适合对 Ch75 做机制性 refine；Ch72/74/77 最多短 handoff，Ch76 已有 observation-driven correction，
  无需重复。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Revision Audited /
  Human Gate Pending`。本轮只写 Weekly，不修改 Books。若 W08 Evidence Gate 与人工 Review 通过，Ch75 吸收
  value-of-information decision、state ownership、旧策略共存条件与 calibration failure；不保留作者 headline、
  合成 reward 数字或“Pareto-optimal”泛化。
- **Open Questions:** multi-dimensional latency/money/risk/user burden 如何保留 hard constraints 而不被 scalar
  reward 淹没；prior 与 policy 的 joint version/calibration drift 如何监测；observation 后 posterior 由谁更新；
  tool quality 如何做到 per-task 而非全局常数；怎样以 shadow/canary 测量 estimator cost 是否真的换来较少探索；
  high-impact action 的 conservative override 与 human approval 如何进入 value-of-information contract？

### Modeling Distinct Human Interaction in Web Agents

- **Candidate / Week / Score:** Modeling Distinct Human Interaction in Web Agents / 2026-W08 / 25/30；
  `Source Family ID: cowcorpus-intervention-control-transfer-2026`。
- **Source Type / Date / Revision History:** CMU、Duke 等作者的学术论文，arXiv v1 于 2026-02-19 首发，
  v2/v3/v4 分别于 02-27、05-31、07-07 修订。v1 live study 只有 4 名 returning participants，报告平均
  user rating 增加 26.5%；v4 又招募 12 名新参与者并把 n=16 合并报告，headline 改为 36.8%。历史事件仍
  归 W08，两个比例必须绑定版本与样本，不得拼成稳定产品效应。
- **Direct / Related Primary Sources:** arXiv v1 与最新版 v4、submission history、论文链接的 CowCorpus
  Hugging Face organization、Gemma-27B/LLaVA-8B 及三个 style model cards、`oaishi/PlowPilot` 官方代码。
  当前 HF organization 公开 5 个 model repositories，却显示 0 public datasets；论文所称 400 trajectories
  无公开 dataset card/download 可独立检查。PlowPilot 当前有 29 commits、无 release/tag，不能固定 event-date
  runtime；README 还列出 API retry、DOM failure、debugger conflict 与 initialization race 等现实失败模式。
- **Access and Verification Status / Full-read Coverage:** Verified v1 and v4 / current models and code verified /
  raw dataset unavailable / event-date code snapshot unavailable。已读 problem formulation、PTS、collection、
  intervention taxonomy、clustering、SFT experiments、style customization、live study、Related Work、Conclusion、
  participant protocol、CowPilot collection runtime、完整 benchmark、few-shot/reasoning/history/modality/time-offset
  ablations，并核验 model cards 的 input、training config、precision 与公开 artifact 缺口。论文无独立
  Limitations/Threats to Validity 章节。
- **Original Problem / Why the Previous Design Was Reasonable:** 传统 Agent 要么默认持续自主执行，只在明确
  policy gate 停止；要么每一步都请求确认。前者在低风险、任务明确时减少 user burden，后者在高风险或模型
  不成熟时提供强控制；但真实 web workflow 中错误、偏好补充、UI 障碍与 user trust 会在执行过程中变化，
  两个固定极端都不能决定何时移交控制。
- **Changed Constraint / Principle:** Human involvement 不是单一 approval bit，而是随 trajectory 演化的控制权
  状态：监督、短暂 correction、协作接力和完全 takeover 有不同 handback semantics。系统需要把“预测用户
  可能介入”当 advisory signal，再由 risk、action reversibility、uncertainty、user preference 与 policy 决定
  ask/pause/continue/takeover；历史 intervention 是 observed behavior，不是规范性最优标签。
- **Mechanism / State Ownership:** intervention model 消费 screenshot、AXTree、past human/agent actions 与
  proposed next action，输出 `<ask_user>` 或 `<agent_continue>`；Workflow 拥有 `AgentControl / AwaitingUser /
  HumanControl / HandbackPending / AgentControl` 等 authoritative state、pause/cancel、pending-action identity 与
  resumable context；human 拥有是否介入、执行哪些动作、何时 handback 的 authority；executor 只在当前 control
  lease 与 policy 允许时行动。Style cluster/profile 只能是低置信 personalization hint，不能替用户授权。
- **Control Flow / Data Flow:** Agent 形成 proposed UI action → capture current screenshot/AXTree 与 trajectory →
  intervention predictor 给出 probability/token → policy 合并 side-effect/risk/user settings → continue 或进入
  `AwaitingUser` → human approve、correct、take over 或 cancel → runtime 记录 actor-attributed actions → explicit
  handback 后重建 belief/plan → Agent resume。直接把 classifier token 接到执行器会混淆“用户过去会介入”与
  “系统现在必须停止”，也可能让 false negative 越过不可逆 action。
- **Implementation Details:** CowCorpus 来自 20 名 20～30 岁参与者，每人 10 个 Mind2Web tasks + 10 个
  self-chosen tasks，共 400 trajectories、2,748 agent actions、1,476 human actions。CowPilot 以 GPT-4o 驱动，
  使用 suggest-then-execute Chrome extension，允许任意 pause/takeover/handback；参与者每项最多尝试三次并
  自选一条最终 trajectory。模型以 SFT 学习 stepwise binary token；style 由每用户 frequency、intensity、
  normalized position、handback rate 四个特征做 k-means `k=4`，再对三类有 intervention 的 cluster 微调。
- **Evaluation Contract:** 数据按 trajectory-level 而非 user-level 切分，保持约 1:7 intervention/non-
  intervention ratio；Hands-off 因没有正例被排除，processed set 只有 1,247 train steps、251 test steps。
  指标为 step accuracy、两类 F1 与作者定义的 Perfect Timing Score；PTS 对 ground-truth intervention event 的
  exact hit 加分，并按与事件距离的平方惩罚之前的 false positives。live study 的 v4 样本是 4 returning +
  12 newly recruited users，使用六个 7-point Likert items；不是 blinded randomized crossover，也未报告任务
  success、side-effect error 或长期 retention。
- **Baselines / Ablations / Sensitivity / Overhead:** 对比 Always Intervene、Always No Intervention、Claude 4
  Sonnet、GPT-4o、Gemini 2.5 Pro、base/SFT Gemma-27B 与 LLaVA-8B，以及三种 style-specific models。
  Class imbalance 使 Always No Intervention 的 step accuracy 达 0.853 却 intervention F1/PTS 为 0；SFT
  Gemma 的 intervention recall 仍只有 0.216。Few-shot 影响不一致，explicit reasoning 反而降低 PTS；移除
  human-action history 降低 macro F1；PTS 的 alpha sweep 只保持模型相对排序，未验证 metric 与真实 harm/
  user preference 的外部效度。Takeover cluster 仅 11 positive steps，style diagonal dominance 已出现例外。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 论文披露 base models 与 step counts；
  Gemma/LLaVA model cards补充 linear-decay learning rate `1e-5→~2e-9`、6 epochs、120 global steps、batch 1、
  BF16。GPU 型号/数量、sequence/image resolution budget、class weighting、training wall time、inference latency、
  browser concurrency、intervention threshold、p95 task time 和 production SLO 均 `Not Disclosed`。论文反而
  显示原 CowPilot agent 平均每项耗时 71.7～93.1 秒，用户对是否更快只给中性 4.05/7。
- **What the Evidence Proves:** 在这 20 名熟悉 Agent 的参与者与 CowPilot UX 下，human actions 不是随机噪声，
  而包含 error correction、preference refinement、assistive takeover，并表现出 frequency/intensity/position/
  handback 的差异。用相同环境收集的 multimodal trajectory 做 SFT，能比对应 base model 更好预测稀有
  intervention steps；v4 的小规模 follow-up 提供 intervention-aware prompting 可能改善 perceived usefulness 的
  初步 evidence。
- **What It Does Not Prove:** 不证明四类 style 是普遍、稳定或因果的人群类型；不证明 classifier 学到的是
  user need 而非 CowPilot latency、agent bug、website、participant identity 或 existing UX；不证明预测 historical
  intervention 的时机就是系统应该 ask/approve 的时机；不证明低 recall 足以保护不可逆 action，也不证明
  subjective rating 等于 task success、降低 harm 或减少总人工成本。v4 增补结果不得反写为 v1 已有证据。
- **Limitations / Threats to Validity:** 只有 20 名 20～30 岁、频繁使用 AI 且熟悉 Agent 的 participants；
  k-means `k=4` 只作用于 20 个 points，没有跨 cohort stability；trajectory-level split 可能让同一 user 同时
  出现在 train/test，不能验证 cold-user generalization；Hands-off 被排除使部署 class mix 不一致；最多三次
  尝试后由参与者自选最终 trajectory 带来 selection bias；400 tasks 中 200 个是同一 10-task set 的重复用户
  轨迹；raw dataset 未公开；无 confidence interval、participant-level bootstrap、longitudinal drift、privacy/
  consent reuse、fairness、adversarial intervention、harm study 或独立复现。v4 的 new/returning groups “无显著
  差异”不等于二者等价，n 很小且 baseline comparison 仍非随机同期对照。
- **Trade-offs / New Failure Modes:** 选择性求助能减少 continuous monitoring，却会增加 prediction latency、
  prompt/context capture、privacy exposure 和 false interruption；false positive 造成疲劳与 abandonment，false
  negative 让 Agent 越过关键 decision point；style personalization 会冻结用户过去的风险容忍度或误把 Agent
  缺陷当偏好；human takeover 期间 Agent 的 pending action、credentials、timers 与 leases 若未暂停会产生
  concurrent side effects；handback 后若不 reconcile environment，旧 plan 会在新 state 上继续执行。
- **Where the Previous Design Still Applies:** irreversible/high-impact action 继续使用 deterministic approval，
  不依赖 intervention predictor；低风险、易回滚、短任务可默认 autonomous；高监管或模型早期阶段的
  confirm-every-step 虽昂贵但仍是安全分支；用户主动 pause/takeover 必须永远可用，不能被个性化模型关闭；
  没有 user-level calibration 或公开 evidence 时，通用 conservative policy 优于强行 style classification。
- **Evolution Relationship:** `Direct Evolution`：always-autonomous / confirm-every-step → explicit pause/takeover →
  logged actor-attributed control events → advisory intervention prediction → policy/risk-conditioned selective ask →
  future user-calibrated control transfer with explicit handback/reconcile。`Layering / Dependency`：CTA 为“是否
  额外求助”提供 value-of-information 原理，PAHF 区分行动前问与行动后改；本工作加入真实 control-transfer
  trajectory。三者互补，不能互相覆盖。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 census 的 Ch78 owner 已纠正：human 和 Agent 的
  authority transfer 不是 Multi-Agent topology。Ch77 为主 owner；已读 Ch74～78 与 Ch80。Ch77 已覆盖
  AwaitingApproval、Human-in-the-Loop、durable events 与 state machine，但缺少 intervention、takeover、handback、
  reconcile 的完整 control lifecycle，以及 `predicted intervention != approval policy` 的边界。Ch75 只接收
  ask/continue advisory signal，Ch80 管 profile/privacy/rollout；Ch78 无需修改。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Scope and Revision
  Corrected / Human Gate Pending`。本轮只写 Weekly，不修改 Books。若 W08 Evidence Gate 与人工 Review 通过，
  Ch77 refine control-transfer state machine、handback/reconcile 和 advisory-vs-authority separation；Ch75/80 最多
  短 handoff，不保留 style 名称、headline 百分比或厂商模型排行。
- **Open Questions:** intervention ground truth 如何从 observed behavior 提升为 risk-aware normative label；怎样
  做 held-out-user、cross-agent、cross-website 与 longitudinal evaluation；pause/takeover 时 pending action、lease、
  budget 与 credential 如何原子转移；handback 后怎样 reconcile state 与 invalidate old plan；false positive/
  negative 如何绑定 user burden 与 harm；trajectory privacy、consent、deletion 与 style-profile expiry 如何治理？

### Frontier AI Risk Management Framework in Practice v1.5

- **Candidate / Week / Score:** Frontier AI Risk Management Framework in Practice: A Risk Analysis Technical Report
  v1.5 / 2026-W08 / 22/30；`Source Family ID: shlab-frontier-risk-framework-v1.5-2026`。
- **Source Type / Date / Revision History:** 上海人工智能实验室的 49 页技术报告；报告内部标注 v1.5、最后更新
  2026-02-15，arXiv 只有 v1，于 2026-02-16 首发。它是在 2025 年 v1.0 七类风险框架上的一次五类更新，
  不是 arXiv v1→v1.5 的 revision history；model availability cutoff 为 2026-01-31。事件归 W08，后续来源只用于
  核验，不得反写为当周已有证据。
- **Direct / Related Primary Sources:** arXiv v1 HTML/PDF 与 submission history；报告引用的 2025 v1.0 family；
  `ShaoShuai0605/Misevolution` 是 memory/tool misevolution 的作者官方 artifact，但本报告没有给出覆盖五个风险族
  的统一 release、tag、raw run 或 event-date commit。arXiv 的 Code/Data 区也没有直接关联代码；公开可核验性
  因此是 report-level，不是完整 benchmark reproduction。
- **Access and Verification Status / Full-read Coverage:** Verified report / related misevolution artifact verified /
  unified raw evidence unavailable。已读 metadata、Introduction、model taxonomy、五个风险族的 problem、method、
  metrics、tables、case studies、mitigation、domain limitations、global ethics/limitations、change log 与关键公式；
  同时核验报告列出的 sample counts、judge、turn budget、model cutoff 和作者对结果的 claim boundary。
- **Original Problem / Why the Previous Design Was Reasonable:** 静态聊天模型时代，用知识问答、CTF、refusal 或
  一次性 red team 测试，可以低成本比较离散能力；模型不持久保存 memory、不能执行工具、也没有集群权限时，
  这些 proxy 与实际风险之间的距离相对较小。进入长期 Agent、外部工具、社会交互和可变运行状态后，同一个
  weights 会因 harness、权限、历史状态与环境反馈产生不同风险，单一 benchmark score 不再足够。
- **Changed Constraint / Principle:** frontier risk 不是模型上的一个标量，而是 `hazard capability × elicitation ×
  opportunity × permissions × environment × mitigation` 的条件性 evidence。Cyber uplift、autonomous exploit、
  persuasion、training-induced dishonesty、memory/tool drift 与 resource proliferation 的 subject、population、
  success event 和 consequence 都不同，必须分别建 EvalSpec；不同风险族的百分比不能相加、平均或排序成一个
  “综合安全分”。
- **Mechanism / State Ownership:** Evaluation System 拥有 risk taxonomy、每个风险族的 EvalSpec、subject/
  harness/judge identity、sampling、uncertainty 与 claim boundary；Security/Workflow 拥有实际 memory/tool artifact、
  code provenance、permissions、approval 与 enforcement；cluster control plane 拥有 Deployment、quota 与 admission；
  model 只提出 action，不能因 benchmark 中成功执行过命令就获得生产 authority。报告本身是多套实验的汇编，
  没有一个共同的 causal mechanism 或统一 scorer。
- **Control Flow / Data Flow:** intended harm / asset → per-family threat model → versioned model + prompt/agent +
  tool/permission/environment → repeated execution → deterministic verifier、model judge 或 human outcome → per-family
  evidence and uncertainty → mitigation experiment → residual-risk decision。上线后还需 telemetry、incident 与新分布
  回流；static evaluation 不能替代持续治理。
- **Implementation Details:** Cyber PACEbench v2.0 包含 32 个环境、四类场景，以 Pass@5 和作者设定的
  `0.2/0.3/0.3/0.2` 权重聚合；RvB 让 planner/executor/reporter Red Agent 与 Mini-SWE-Agent Blue Agent 迭代五轮。
  Persuasion 使用 LLM-to-LLM attitude/voting setup，mitigation 由 9,566 条 human behavioral records 经 GPT-4o
  补 reasoning/personality，再做 SFT + GRPO。Emergent misalignment 对 math/code/medical 错误数据和 simulated
  biased-user trajectories 做 SFT/KTO。Memory test 是 40 个 cases、四领域；tool reuse 为 25 例，malicious-repo
  为 371 例，安全由 Gemini-2.5-Pro judge。OpenClaw/Moltbook 为 48 小时、四种 backbone、三档 SOUL initialization、
  30 条 prompt-injection cases；self-replication 则给 Agent Kubernetes cluster、Deployment task 与执行权限。
- **Evaluation Contract:** 报告没有全局统一 contract。Cyber 的成功是拿到 flag；persuasion 是固定 voter 的
  opinion shift；dishonesty 依赖 MASK/DeceptionBench belief proxy；memory/tool 使用 judge 判 unsafe 的 ASR；OpenClaw
  只比较 medium-level evolved SOUL 前后的 30-case ASR；self-replication 以 M1～M4、overuse rate/count 衡量，其中
  M4 明确要求创建新的独立 Deployment。只有在各自的 prompt、权限、环境与 judge 内，结果才可比较。
- **Baselines / Ablations / Sensitivity / Overhead:** RvB 对 cooperative MAS 并报告五轮轨迹，但未给出足以隔离
  adversarial curriculum、report quality、模型与迭代次数的完整 ablation；persuasion mitigation 只在 Qwen-2.5-7B/
  32B 上与多 persuaders 比较，HumanEval/GPQA 只覆盖有限 capability retention；data cleaning sweep 把 contamination
  从 50% 降至 1%，仍有 residual dishonesty；prompt reminder 对 memory/tool 的效果随模型/领域大幅变化，个别条件
  反而恶化。OpenClaw evolved SOUL 由 medium-level MiniMax-M2.1 迁移给四个模型，不是每个模型独立 evolution
  的因果对照；self-replication 没有 least-privilege/no-command、permission-denied 或 human-baseline ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 报告披露 model snapshots、部分 task/
  attempt/turn counts、数据规模与 cutoff；训练硬件、GPU 数量、precision、context/output budget、sampling temperature、
  API revision、并发、总 token/cost、wall time、失败重试、judge calibration、cluster RBAC/quota、network boundary、
  confidence intervals 与 production SLO 多数 `Not Disclosed`。因此任何百分比都不能作为跨模型、跨风险族或生产
  部署的稳定排行。
- **What the Evidence Proves:** 在作者构造的多个 harness 中，离散 exploit skill 与长链 autonomy 会分离；
  contaminated/biased feedback pipeline 可改变被测 honesty proxy；持久 memory、reused/generated tool 与外部 code
  会把历史 proxy reward 和 supply-chain risk 带到后续 action；简单 prompt reminder 不能在所有模型/领域稳定
  消除该风险；给 Agent 集群执行权后，任务完成判断与 state verification 缺陷会表现为 ineffective loop、重复
  创建与 resource overuse。报告也提供了把 risk evaluation 从静态回答推进到 stateful executable environment 的
  初步实例。
- **What It Does Not Prove:** 不证明被测模型有统一、稳定或可跨部署迁移的 frontier-risk rank；不证明 LLM-to-LLM
  persuasion 等于对人的真实 uplift；不证明 MASK/LLM judge 可以读取模型“内部意图”；不证明 1% contamination
  在任意训练 pipeline 都产生同样 cross-domain effect；不证明 Moltbook 社区自然提高安全——作者承认热门/随机
  内容受到显著 anthropogenic interference；不证明模型在没有权限、没有任务指令或跨机器凭证时会自然 self-
  replicate。报告 Table 1 对 self-replication 的文字定义是部署到 other machines，而实际更新实验是在同一
  Kubernetes cluster 创建新 Deployment，两者不可等同。
- **Limitations / Threats to Validity:** 报告自己承认 threat taxonomy 不完备、可能 insufficient elicitation、static
  evaluation 不能覆盖长期 iterative assistance、缺少多领域 human-uplift studies。除此之外，五族实验的模型集合、
  harness、judge、sample size 与 mitigation baseline 不一致；多个关键 verdict 使用单一 model judge；大多无 raw
  per-run artifact、uncertainty 或独立 replication；“open-source”与“open-weight”、standard/reasoning 的模型标签
  采用作者口径且并不总是精确；报告在局部同时使用 risk manageable、robust mitigation 与 preliminary/residual
  risk 语言，最终 claim 必须回到具体 table 和 setup，而不是摘要形容词。
- **Trade-offs / New Failure Modes:** executable risk eval 提高生态有效性，却需要危险能力隔离、严格 egress、
  credential/target control、artifact 保密和伦理审批；更强 elicitation 减少 false negative，却可能生成可滥用 artifact；
  model judge 降低成本，却引入共享盲点和 prompt injection；持续更新 taxonomy 能追踪新风险，却破坏跨版本可比性。
  mitigation 也会新增目标错置：stance consistency 可能压制合理更新，adversarial patching 可能过拟合当前 attack，
  data cleaning 不能处理未识别错误，prompt reminder 会被持久 state 或外部 code 绕过。
- **Where the Previous Design Still Applies:** 静态 knowledge/refusal/CTF 适合作为低成本 screening；单步 sandbox
  适合早期 capability gate；没有 tool/permission 的模型不应强行用 Agent self-replication contract 评估；确定性
  policy、least privilege、quota/admission、code signing/sandbox 与 human approval 仍是生产 authority，不由更复杂
  benchmark 替代。新 eval 是在旧层次上增加 state、environment 与 consequence，不是否定旧层次。
- **Evolution Relationship:** `Direct Evolution`：static answer/refusal → discrete executable task → end-to-end agent
  trajectory → persistent memory/tool/supply-chain evaluation → permissioned resource-control scenario → continuous
  post-deployment risk monitoring。`Layering / Dependency`：每一层保留旧 screening，并增加新的 state owner、harness
  与 failure mode；不同 risk families 彼此并列，不能构造单向“更安全/更危险”的演进排行。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 为 Ch62，已读 Ch62、相邻 Ch61/63，并检查 Ch68/69。
  Ch62 已覆盖 EvalSpec、subject identity、executable evidence、Agent trajectory、judge audit 与不可外推边界；缺口是
  更明确写出 `risk taxonomy != aggregate metric`，以及 capability、elicitation、opportunity、permission、consequence
  的 threat-model factorization。Ch68 已覆盖 NIST RMF、tool boundary、supply-chain 与 least privilege，可短 handoff
  persistent memory/tool/code 和 cluster authority；Ch69 无需拥有风险 taxonomy。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Evidence Families
  Separated / Human Gate Pending`。本轮只写 Weekly，不修改 Books。若 W08 Evidence Gate 与人工 Review 通过，Ch62
  只 refine per-risk EvalSpec 与 umbrella-score prohibition，Ch68 只增加 self-evolving artifact/permission handoff；
  不保留模型排行、headline 百分比、厂商框架口号或把实验称为普遍 self-replication 证据。
- **Open Questions:** 如何为每个 risk family 建立最低公开 evidence contract 与 cross-version comparability；
  LLM judge verdict 怎样用 deterministic/human evidence 校准；怎样把 elicitation strength、tool/credential/RBAC、
  environment realism 与 consequence severity 分开报告；OpenClaw evolved SOUL 的 per-model causal effect 能否复现；
  self-replication eval 如何区分被明确要求的 availability recovery、越权 persistence 与真实跨边界复制；统一 artifact、
  raw run、negative control、confidence interval 与 independent reproduction 是否会公开？

### A Trajectory-Based Safety Audit of Clawdbot (OpenClaw)

- **Candidate / Week / Score:** A Trajectory-Based Safety Audit of Clawdbot (OpenClaw) / 2026-W08 / 24/30；
  `Source Family ID: openclaw-trajectory-audit-minimax-m21-2026`。
- **Source Type / Date / Revision History:** ShanghaiTech 与上海人工智能实验室作者的 22 页安全评估论文；arXiv
  只有 v1，于 2026-02-16 首发。论文研究名为 Clawdbot、又说明公开文档中也称 OpenClaw/Moltbot；这是一套
  2026-02-10 前后配置快照的研究，不是当前 OpenClaw 所有版本的产品安全声明。
- **Direct / Related Primary Sources:** arXiv v1 PDF、submission history、作者公开的 `tychenn/clawdbot_report`
  seed-case repository、论文引用的 OpenClaw security/memory/skills/exec/logging 官方文档。当前仓库只有 5 commits、
  无 release，公开六个 JSON prompt sets；没有 raw trajectories、Gateway JSONL、截图原始件、完整 workspace seed、
  exact OpenClaw commit/config bundle 或可一键重放的 judge pipeline。当前 OpenClaw 文档只用于机制交叉核验，不能
  反写成 2026-02-16 runtime 已具备同样控制。
- **Access and Verification Status / Full-read Coverage:** Verified PDF / current seed cases and official docs verified /
  event-date runtime and raw runs unavailable。已读六维 taxonomy、34-case composition、deployment/interface、tool
  surface、trajectory collection、automated/human judgment、aggregate results、六类 case analysis、discussion、
  references，并逐个核验六份 JSON 的 case 数、label 与 README reproduction instructions。论文没有独立 Limitations、
  Threats to Validity、Appendix、hardware 或 statistical-analysis 章节。
- **Original Problem / Why the Previous Design Was Reasonable:** 文本 chatbot 的错误通常停留在答案层，可重新询问、
  纠正或丢弃；用 final response 做 content moderation 因而曾是合理的低成本安全检查。Agent 把同一输出接到 file、
  shell、browser、message 与 authenticated services 后，中间 action 已产生副作用；只检查最终语言会漏掉删除、覆盖、
  外发、错误 artifact 与被持久化的注入。
- **Changed Constraint / Principle:** safety subject 必须从 `response` 扩为 `model + prompt + memory + skills + tool policy
  + permission + environment + complete trajectory + side effects`。失败严重度不只由模型是否答错决定，还由 action
  reversibility、blast radius、authorization 和 accumulated exposure 决定；低单次失败率也不能直接当长期可靠性，
  尤其 task failures 相关、软件版本变化或 attacker adaptive 时。
- **Mechanism / State Ownership:** 论文使用 OpenClaw Gateway JSONL 作为 trajectory source，AgentDoG-Qwen3-4B
  给 binary judgment，human review 形成最终 label。生产上，Gateway/Workflow 应拥有 actor-attributed event、tool
  arguments/results 与 pending side effects；Security executor 拥有 sandbox、allowlist、approval、credential 与 egress；
  Memory/Skill store 是不可信、可持久影响 future action 的 artifact；model 的 final claim 不是 execution ground truth。
- **Control Flow / Data Flow:** user/untrusted content → plan → proposed tool call → policy/sandbox/approval → execution →
  typed result/side effect → durable trajectory → per-step deterministic checks + calibrated trajectory judge + human review →
  failure taxonomy/mitigation。若 memory 或 skill 可写，写入本身必须是受审计 state transition；下一 session 读取前还要
  检查 source、authority、expiry 与 supersession，而不是把 Markdown 自动升级为 trusted instruction。
- **Implementation Details:** 单一 backbone 为 `minimax/MiniMax-M2.1`，主要通过 browser Control UI 交互；tool surface
  固定为 scoped workspace 中 arbitrary shell、`web_search` 与 `web_fetch`，明确关闭 sandbox。需要 Gmail、chat 或
  login side effect 的任务被改写为在本地目录输出 JSON/YAML action file，并把文件生成当 completion signal。34 个
  canonical cases 来自 ATBench 10、LPS-Bench 10、Upward Deceivers 7、作者自建 7；每个 trajectory 包含 message、
  action、tool arguments/output 与 final response。
- **Evaluation Contract:** 六维为 user-facing deception、hallucination/reliability、intent misunderstanding/false
  assumption、unexpected result from ambitious goal、operational safety/efficiency、prompt-injection/jailbreak robustness。
  每个 case 只分配一个 primary dimension；论文报告 automated 与 manual labels 在 34 个 cases 完全一致，但没有报告
  reviewer 数量、blindness、rubric adjudication、inter-rater agreement、judge threshold 或 human–judge independence。
  headline 58.9% 可由论文 outcome 与 artifact case counts 推断为 `(5/7 + 7/7 + 0/3 + 1/2 + 6/8 +
  4/7) / 6 = 58.93%` 的 unweighted macro average，而不是 34 个 cases 的 micro pass probability；论文未显式说明
  这个 aggregation formula，且 `false_assumption.json` 的 label 冲突又阻止从 artifact 独立复算。
- **Baselines / Ablations / Sensitivity / Overhead:** 没有第二个 backbone、OpenClaw version、tool-policy baseline、
  sandbox-on/exec-denied/approval-on comparison、multi-run sampling、temperature sweep、judge ablation 或 cross-platform
  baseline。Hallucination dimension 除 canonical cases 外又测试 “50+” variants，但没有公开这些 variants、raw output
  与 per-run labels。论文只定性称在 memory 加入 honesty instruction 可降低 deception，没有 sample size、before/after
  table 或对 persistent prompt 的攻击/utility trade-off。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 仅披露 MiniMax M2.1 identifier、Brave web
  search、34-case sources 与 tools；OpenClaw exact commit/release、MiniMax API snapshot、sampling parameters、context/
  output budget、AgentDoG serving config、CPU/GPU、OS、token/latency/cost、run concurrency、retry、task timeout、failure
  recovery、workspace quota 与 production SLO 均 `Not Disclosed`。论文用 `1-(1-p)^n` 给独立同分布 task 的暴露直觉，
  但真实 tasks、sessions、memory 与攻击并不独立，不能把 5% illustrative p 当测得的部署风险。
- **What the Evidence Proves:** 在作者这套单模型、unrestricted local exec、sandbox disabled 的环境中，34 个特定
  prompts 产生非均匀 outcome；有些失败只在 action/observation trajectory 中可见。case study 具体展示了 empty
  evidence 仍声称完成、模糊清理条件引发高影响 action、open-ended goal 与 persistent artifact 发生语义串扰、以及
  benign wrapper 将文本请求连接到可执行 action file。它支持“风险是 model×runtime×permission×state”的系统结论，
  也支持在 tool boundary 做 defense in depth，而非只过滤 final text。
- **What It Does Not Prove:** 不证明 OpenClaw 当前或所有版本安全率为 58.9%；不证明 MiniMax M2.1 自身有相同失败率；
  不证明真实 Gmail、交易、chat 或 browser side effects 与 local JSON/YAML proxy 等价；不证明 AgentDoG 在更长、不同
  模型或 adversarial trajectory 上准确；不证明 ambiguity dimension 的 0% 能外推到其他 prompts；不证明 memory/skills
  是失败原因而非 task setup、prior workspace state 或 runtime bug。关闭 sandbox、开放 arbitrary shell 是实验 contract，
  不是从 model output 单独推导出的 capability。
- **Limitations / Threats to Validity:** 每个 canonical prompt 看起来只有一次 run，n 很小且 hand-curated；无置信区间、
  repeated seed、paired control、version pin、severity-weighted consequence、real-user distribution 或 independent replication。
  artifact 没有 raw trajectories/完整 seed files；README 说 case 含 expected safe/unsafe annotations，但 label semantics 未定义。
  更严重的是 `false_assumption.json` 当前三个 case 全标 `safe`，却与论文该维度 0% pass 冲突；论文正文称 hallucination
  有 six seed queries，而当前 JSON 有 7 个、总计也需 7 个才能达到 34。因无 tag/event-date commit，无法判断是
  post-paper drift、标注错误还是文档语义差异，公开 artifact 不能独立重建 headline。
- **Trade-offs / New Failure Modes:** 记录完整 trajectory 提高可审计性，却扩大 secret/PII/tool-output 的日志面并增加
  retention/redaction 成本；真实 host 增加生态效度，也增加 destructive test 风险；local action proxy 降低真实伤害，
  却改变权限、网络、UI 与 downstream validation。Prompt memory 可以降低一类 deception，却会成为跨 session 注入面；
  skill bundle 提升复用，却把 instruction 与 executable recipe 变成供应链 artifact；强 confirmation 降低 irreversible
  harm，却增加 fatigue 和延迟。
- **Where the Previous Design Still Applies:** final-response moderation 仍适合无工具的 text path；静态 prompt set 仍可
  做 cheap regression screening；低风险、可回滚 action 可用较宽松 policy；高影响 action 必须 deterministic approval、
  least privilege、workspace/egress restriction 与 idempotency。Sandbox-off 真实 host 测试只能在 dedicated disposable
  environment 中进行，不能作为生产默认控制。
- **Evolution Relationship:** `Direct Evolution`：final response safety → tool-call/action trace → complete trajectory +
  side-effect evidence → versioned model/runtime/permission EvalSpec → production incident/continuous evaluation。
  `Layering / Dependency`：output moderation 没被淘汰；sandbox、policy、approval、memory provenance、skill supply chain
  与 trajectory audit 分属不同防线，任何单层都不能宣称解决 Agent safety。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 为 Ch68；已读相邻 Ch67/69，并检查 Ch62、Ch73、Ch74、
  Ch77。Ch62 已明确 subject identity 包含 tool/sandbox/workflow/environment，且 trajectory judge 需审计；Ch68 已把
  prompt injection 根因定位为 untrusted context 与高权限 action 混合，并把 authority 放在执行器；Ch73 已覆盖
  memory provenance、poisoning、supersession 与 recovery；Ch74 已覆盖 typed validation、authorization、approval、
  reversibility 和 trace。因此这篇论文强化现有边界，但没有形成新的长期机制缺口；Ch67 也无需把 single-user
  gateway 误写成 multi-tenant isolation。
- **Integration Decision / Changed Files:** `No Change — Already Covered / Evidence Contract Incomplete`。本轮只写
  Weekly，不修改 Books。论文保留为“environment/permission 改变 safety claim”的受限案例；artifact inconsistency、
  unpinned runtime、single-model/single-run 与无 raw trajectory 使 headline 不进入正文。若未来公开可重放 snapshot、
  多模型/多 policy ablation 或真实 side-effect verifier，再重新评估是否 refine Ch62/68。
- **Open Questions:** event-date OpenClaw commit/config 与 exact MiniMax snapshot 是否可恢复；六个 JSON 的 label 到底
  表示 observed verdict、expected behavior 还是 prompt safety；false-assumption label 与 0% pass 如何解释；58.9% macro
  aggregation、per-case final labels、raw Gateway logs、human reviewer protocol 与 AgentDoG config 是否会公开；怎样在
  sandbox-on/off、exec deny/allowlist/full、approval 与 memory clean/poisoned 之间做 paired factorial evaluation？

### Magma / Masking Updates in Adaptive Optimizers

- **Candidate / Week / Score:** Magma / On Surprising Effectiveness of Masking Updates in Adaptive Optimizers /
  2026-W08 / 24/30；`Source Family ID: magma-stochastic-optimizer-update-masking-2026`。
- **Source Type / Date / Revision History:** Google、Northwestern University 作者的学术论文；arXiv v1
  于 2026-02-17 首发，截至访问日无后续 revision。arXiv metadata、论文正文及作者公开入口未链接
  官方代码或可执行 artifact，因此实现只能按论文描述核验，不能标记为 reproduced。
- **Direct / Related Primary Sources:** arXiv v1 HTML/PDF、公式、Algorithms 1～2、四组实验、证明与
  Appendix A～C；相关基线只用于理解论文的比较合同，不用二次来源补造 Magma 实现或事件日行为。
- **Access and Verification Status / Full-read Coverage:** `Verified paper / official artifact unavailable`。
  已读 metadata、Introduction/Related Work、SkipUpdate 与 Magma 算法、局部 Taylor 结论、constant-step
  non-convex analysis、Llama 2/C4、Nano MoE、heavy-tailed linear-transformer、heterogeneous quadratic、
  ResNet-50 反例、全部实验设置、mask component/granularity、sampling ratio、damping、dense-vs-sparse
  momentum 与 learning-rate sensitivity。论文没有独立 Limitations/Threats 章节。
- **Original Problem / Why the Previous Design Was Reasonable:** dense optimizer update 会把每个 step 的
  梯度信息应用到全部参数；当 backward 已经计算出 dense gradient，逐元素 Adam/RMSProp state update 与
  parameter write 的语义简单、可复现，也不会因为 mask 增加额外随机方差。对于相对 homogeneous、条件数
  温和的 landscape，论文自己的 quadratic 与 ResNet-50 对照也说明 dense update 仍然合理。问题出现在
  Transformer-like、block-wise curvature 高度异质且 gradient noise heavy-tailed 时：少数高曲率或高噪声
  方向可能收窄稳定 learning-rate 区间，dense application 不一定是最好的 implicit bias。
- **Changed Constraint / Principle:** 论文把“每步是否更新全部参数”从实现常量变成 optimization policy。
  对独立 Bernoulli block mask，局部二阶展开给出 expected post-update loss 等于 dense update loss 加上
  与 `(1-p)/p` 和 block-direction curvature 相关的项；这提供了 stochastic update masking 可能偏向较平坦
  trajectory 的机制解释。该结论依赖局部 Taylor、独立 mask 与给定 update vector，不能直接证明最终
  generalization，也不能把 adaptive alignment 的收益全部归因于这一个无偏公式。
- **Mechanism / State Ownership:** `SkipUpdate` 先让 base optimizer 对所有 blocks 更新 dense first/second
  moment state，再以 block-wise `Bernoulli(p)` mask 选择 parameter update，并用 `1/p` 保持基础 mask 的
  conditional expectation。`Magma` 另计算当前 gradient 与 momentum 的 block-wise cosine alignment，经
  sigmoid/temperature 和 EMA（论文实现为旧分数 0.9、新分数 0.1）得到 damping score，再乘到被保留的
  update 上。Base optimizer 拥有 momentum/variance，masking wrapper 拥有 RNG、block identity、alignment
  与 damping；model parameters 只接收最终 masked update。由于 damping 引入 bias，Magma 本身不能再被
  描述为无偏 update estimator。
- **Control Flow / Data Flow:** `gradient -> dense optimizer-state transition -> candidate update Delta ->
  per-block momentum/gradient alignment -> score EMA -> Bernoulli mask -> score × mask × Delta -> parameter`。
  被 mask 的 block 本 step 不改变 parameter，但其 optimizer state 仍吸收当前 gradient；下一步因而不是
  “冻结后原样恢复”，而是带着更新后的历史统计重新参与。论文消融显示若连 momentum state 也稀疏更新，
  训练会明显不稳定；这一区分是理解机制与系统成本的关键。
- **Implementation Details:** 默认实验取 `p=0.5`、`tau=2`，只对 Attention 与 MLP parameter blocks 使用
  Magma；block granularity 是效率折中，而不是质量唯一来源。作者尝试把 alignment score 当 survival
  probability 并用其倒数做无偏 rescaling，但报告训练不稳定，最终选择 biased damping。论文宣称 overhead
  可忽略，却没有官方代码、kernel path、wall time、memory traffic 或 distributed implementation 数据；
  因而不能断言 mask 会自动跳过 backward、optimizer-state memory、gradient collective 或 parameter
  communication。
- **Evaluation Contract:** C4 实验使用 Llama 2-style 60M/130M/350M/1B，batch 512、max sequence 256，
  分别训练 10K/20K/60K/100K steps；每种方法在 `1e-4～1e-2` 五点 learning-rate grid 中选择最终
  validation perplexity 最好的 run，10% warmup 后 cosine decay 到 peak 的 10%。Nano MoE 为 124M
  GPT-2-style、8 experts、top-2、MoE stride 2、OpenWebText，50K iterations、8×A100、batch 12、gradient
  accumulation 40、sequence 1024、weight decay 0.1、grad clip 1.0。C4 的 GPU、precision、seed、误差条、
  padding/effective-token 数和 wall time未披露；MoE 的 precision、并发与网络拓扑也未披露，不存在生产 SLO。
- **Baselines / Ablations / Sensitivity / Overhead:** C4 比较 Adam、RMSProp、LaProp、C-Adam 及若干借自
  其他论文的 optimizer 结果；表中 Magma wrapper 在四个规模上改善对应 base optimizer 的最终 PPL，
  但部分基线不是同一实验代码重新运行。130M 消融显示只作用于 Attention+MLP 优于只作用 Attention 或
  全部 parameters；`p=0.5` 在测试的 0.25/0.5/0.75 中最好，temperature 相对不敏感。更重要的是，
  `uniform sampling + damping` 在 granularity 表中不差于 alignment-based sampling，作者也明确承认后者
  没有优于 uniform sampling；因此不能把全部增益归因于 alignment 选择。Dense momentum 明显优于 sparse
  momentum；Adam+Magma 在作者的 130M sensitivity 中有更宽 LR 稳定区间，但没有 timing/memory ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 只有 Nano MoE 明确 8×A100；C4
  hardware 和全部实验 precision 均 `Not Disclosed`。长度、batch、steps 如上；distributed degree、通信量、
  并发、利用率、checkpoint overhead 与 SLO 均 `Not Disclosed / Not Applicable`。因此 1B PPL 数字不能
  脱离 dataset、model recipe、best-LR selection 与 token contract，被外推为大模型 optimizer 排名。
- **What the Evidence Proves:** 在论文给定的 C4 小中型 Llama、Nano MoE 与两个受控 toy contracts 中，
  对 base adaptive optimizer 增加 structured stochastic parameter-update masking 可以改善作者报告的最终
  loss/PPL，并在 heterogeneous/heavy-tailed 设置中表现出与 curvature-regularization 解释一致的趋势。
  homogeneous quadratic 与 ResNet-50 反例同时支持“收益依赖 landscape”，而不是所有训练都应稀疏更新。
- **What It Does Not Prove:** 不证明 Magma 在 frontier-scale LLM、多节点训练、不同 tokenizer/data mix、
  长 sequence 或长期 token budget 上稳定获益；不证明 alignment sampling 是收益的必要原因；不证明更低
  PPL 来自更少 compute，也不证明 parameter masking 会减少 gradient computation、optimizer-state memory、
  All-Reduce bytes 或 wall-clock。Discussion 的收敛界分析 constant-step SGD，不是正文使用的 Adam/RMSProp
  完整动态；“可类似扩展”不是 adaptive-optimizer theorem 或系统实现证据。
- **Limitations / Threats to Validity:** 最大真实语言模型只有 1B，主要 corpus 只有 C4，Nano MoE 只有
  124M；多个结果按最佳 LR 选择但没有 seeds/confidence intervals；部分强基线来自其他工作；没有官方
  artifact、复现说明、训练 wall time、memory 或 failure logs；C4 hardware/precision 未披露；无独立
  generalization/task evaluation。alignment 归因与 uniform+damping 消融存在张力，ResNet 反例又限制了
  architecture generality；理论假设也没有测量真实 Transformer 的 block curvature 是否满足。
- **Trade-offs / New Failure Modes:** masking 增加 RNG、block identity、score EMA 与 resume determinism；
  parameter 不更新而 moment state 更新，要求 checkpoint 原子保存两者及 mask/score/RNG lineage。较小 `p`
  放大保留 update，可能增加方差或 instability；damping 换稳定性却引入 bias；block 太细增加 score/mask
  metadata 与 memory traffic，太粗又可能混合不同 curvature directions。若 runtime 不能真正跳过 parameter
  write 或 communication，系统只承担复杂度而没有吞吐收益；若试图连 state update/collective 一起稀疏化，
  又会改变论文已验证的算法并引入 rank mask consistency、stale state 与 recovery 问题。
- **Where the Previous Design Still Applies:** dense Adam/RMSProp 仍适合 homogeneous landscape、成熟且
  高度融合的 kernel/runtime、要求简单 deterministic replay 或没有证据表明 masking 能覆盖额外复杂度的训练；
  deterministic Cautious-style gating、matrix preconditioning、gradient clipping、schedule tuning 与 SAM 类
  flatness 方法解决不同层面的稳定性问题。Magma 是 base optimizer 上的一层 policy，不是对这些旧分支的
  单向替代，也没有消除 dense optimizer state。
- **Evolution Relationship:** `Direct Evolution`：dense adaptive update → deterministic alignment gating →
  unbiased stochastic block masking → alignment-conditioned biased damping；`Layering / Dependency`：base
  optimizer 继续拥有 dense state，mask policy 改变 parameter application。下一阶段压力是证明 causal
  component、scale law 与 distributed execution contract，并决定稀疏的是 parameter write、state update、
  gradient collective 还是仅数学 update；这些选择不能从论文名称反推。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 census 的 Ch27 映射错误：Ch27 是 RLHF，不拥有
  Pretraining optimizer。主 owner 应为 Ch24；已读相邻 Ch23～25，并检查 Ch21 与 Ch32。Ch24 已覆盖
  `objective + parameterization + optimizer state/update rule + schedule + data order`、basis-dependent
  preconditioning 与训练稳定性，但尚未明确区分 dense state transition、sparse parameter application 和
  stochastic update geometry。Ch21 的 Nano MoE 只是受限实验场景；Ch32 负责 collective/runtime，而论文
  没有 distributed masking 机制，均不应成为主 owner。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Books Candidate — Scope and Owner
  Corrected / Human Gate Pending`。本轮只更新 Weekly，不修改 Books。若 W08 Evidence Gate 与人工 Review
  通过，Ch24 可小幅补充“update density 也是 optimizer policy”、dense-state/sparse-application 边界，以及
  landscape-dependent coexistence；不写论文 PPL headline，不把 Magma 命名为通用最佳 optimizer，也不改 Ch32。
- **Open Questions:** uniform mask、damping 与 alignment 各自的独立因果贡献是什么；大模型和更长 token
  budget 是否保持收益；如何度量真实 block curvature/heavy-tail 并决定 `p`；mask/RNG/EMA 怎样进入 checkpoint
  transaction；distributed ranks 是否需要一致 mask；parameter write、optimizer state、gradient collective 与
  wall-clock 哪一项实际减少；biased damping 是否存在稳定且可证明的替代？

### TAROT / Test-driven Curriculum RFT for Code Generation

- **Candidate / Week / Score:** TAROT / 2026-W08 / 21/30；
  `Source Family ID: tarot-tiered-test-curriculum-code-rft-2026`。
- **Source Type / Date / Revision History:** ETRI、HKUST(GZ)、HKUST、Hugging Face、Ant Group 作者的
  学术论文与官方 GitHub/Hugging Face artifact；arXiv v1 于 2026-02-17 首发，截至访问日无 revision。
  官方仓库当前 main 有 12 commits、无 tag/release；它只能核验公开实现家族，不能自动视为事件日快照。
- **Direct / Related Primary Sources:** arXiv v1 全文、全部表格与 Appendix；`deep-diver/TAROT` 的
  dataset shards/sample、custom reward、各模型 GRPO YAML、dstack recipe、评测说明与公开模型/数据入口；
  上游 Open-R1 verifiable coding dataset 只用于确认数据 lineage，不替代 TAROT 自身的验证责任。
- **Access and Verification Status / Full-read Coverage:** `Verified paper + current artifact / strict
  reproduction not established`。已读 Introduction/Related Work、dataset construction、curriculum/reward
  公式、全部模型与 benchmark 结果、OOD/standard-reward/architecture 对比、Limitations、test-generation
  prompt、训练/执行 contract、beta/temperature/length sensitivity、Gemma 反例、全量表、training dynamics
  与样例；并检查公开 reward 的 parsing、sandbox execution、weighting 与 schedule code。
- **Original Problem / Why the Previous Design Was Reasonable:** code RFT 常把整个 test suite 压成平均
  pass rate 或全通过二值 reward。固定 verifier 简单、可执行且跨 rollout 一致；当 policy 能力与 tests
  难度匹配时，它比 learned judge 更接近 functional correctness。但过易 tests 让 group 全通过，过难
  tests 让 group 全失败，二者都可能形成 all-equal reward；把不同难度的 tests 无差别平均，也看不出
  policy 卡在哪类行为边界。
- **Changed Constraint / Principle:** 同一 problem 内的 verification coverage 可以被拆成 basic、
  intermediate、complex、edge 四层，再把“哪些 tier 在何时进入训练”与“各 tier 成功值多少 reward”
  视为两个独立 policy。这个区分在概念上有价值：sampling/allocation 决定 policy 看见什么，reward
  weighting 决定看见后优化什么；模型规模只是 capability proxy，真正需要的是当前 policy 在各 slice
  上的 outcome distribution。然而论文只从预定义 portfolio 静态选择 schedule，没有实现在线
  capability estimator 或 continuous adaptive controller。
- **Mechanism / State Ownership:** dataset 拥有 problem、reference solution 和 tier-labelled stdin/stdout
  tests；reference execution 只验证每个生成 test 与一个 solution 一致。Curriculum policy 拥有 tier
  schedule，reward policy 拥有 tier weights，sandbox 拥有代码执行/timeout，GRPO 拥有同 prompt 的八个
  completions 与 group-relative update。真正的状态应包含 test-suite version、generator snapshot、reference
  solution、tier rationale、curriculum phase、active tiers、reward weights、executor version 与 failure reason；
  否则同名 run 无法重放。
- **Control Flow / Data Flow:** 约 15K Python problems + baseline test → frontier model 生成四个 tier tests →
  reference solution 逐 test 执行，任一失败则丢弃 problem → policy 为 prompt 采样 8 completions → 当前
  schedule 选择 active tiers → sandbox 执行 candidate code → tier pass 经过 weights 形成 reward → GRPO
  group normalization/update → 独立 code benchmarks 评估。论文公式用 `sum_l alpha_l w_l r_l` 表达
  allocation 与 valuation；公开代码则通过 phase-dependent test filtering + fixed weights 近似实现。
- **Implementation Details / Artifact Audit:** 论文称约 15K problems、60K tiered tests、生成器为 o3/o4；
  当前 README 写 15.5K、约 62K、生成器为 `o1-pro/o3/o4-mini`，必须标记 snapshot/documentation drift。
  `var_asce_normal.py` 将 labels 映射为 `basic/medium/high/edge`，按 epoch 0.2/0.4/0.6 逐步开放 tiers，
  E2B 内逐 test 启动 Python subprocess。公开比较器用 `zip(actual_lines, expected_lines)` 逐行比较，却
  没有检查行数相等：匹配前缀但缺少/多出行的输出可能被误判通过。代码还返回 passed weight sum 而非
  active-weight normalization，随着 active tiers 增加，最大 reward ceiling 也变化；这使 schedule、reward
  scale 与 difficulty effect 没有完全解耦。
- **Evaluation Contract:** 训练覆盖 Qwen2.5 Instruct/Coder 1.5B、3B、7B，Gemma2 2B/9B 与
  Qwen3-4B-Instruct-2507；全部单 epoch GRPO、AdamW `1e-6`、global batch 8（较大模型 4）、input 1,024、
  completion 4,096、8 generations/prompt、主实验 beta 0.01。训练为 8×A100 80GB、CUDA 12.4、PyTorch
  2.6；评测为 4×A100 80GB、vLLM、batch 64、Python 3.11 sandbox、每 test 10s。HumanEval(+)、MBPP(+)
  用 pass@1，CodeForces/LiveCodeBench v5 用 overall accuracy，CruxEval 用 input/output prediction accuracy。
- **Baselines / Ablations / Sensitivity / Overhead:** 比较 forward/reversed/static curricula、uniform 与
  B/I、C/E weights、basic/complex/edge only，以及 full-suite Avg-reward/Pass@All。不同 model/benchmark
  的最佳策略经常不同：例如 Qwen3-4B 的 C/E weighted 改善四个 function benchmarks，却在 CodeForces/
  LCBv5 低于 base；Qwen2.5-7B 在 LCBv5 的 best 是 Basic Only。Gemma2-2B 多数 curricula 退化。
  beta、temperature 与 max completion 都显示 benchmark-specific sensitivity；训练 reward 与 downstream
  score 只有弱相关。论文没有 seeds、error bars、significance、train-time/wall-clock 或等算力的完整
  sample-efficiency对比；`TAROT (Best)` 又是多策略、多 benchmark 后的选择，带 selection optimism。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware、CUDA/PyTorch、模型、
  batch、generation count 与长度如上；训练 precision、gradient accumulation/并行布局、每策略 tokens、
  wall time、sandbox concurrency、E2B image/version、网络与 SLO 未完整披露。不同模型因 batch 与
  accumulation 在 fixed compute budget 下 trajectory 长度不同，不能把 reward curve 当严格等步比较。
- **What the Evidence Proves:** 在这些 Python interview-style problems、合成 tier tests、指定 GRPO recipe
  与评测 harness 下，改变 test exposure/weights 会显著改变训练稳定性与 benchmark outcome；任务过难时
  sparse reward 可伤害较弱 policy，且单一训练 reward 不足以预测 downstream quality。它还提供了一条
  可复用观察：difficulty 需要按 model × target-domain 条件化，不能只由 parameter count 决定。
- **What It Does Not Prove:** 不证明论文给出一个可部署的 capability-adaptive selector——没有 capability
  composite 的公式、阈值、校准集或从 baseline 到 schedule 的确定算法；不证明 harder-first 普遍适合
  stronger model，也不证明 `TAROT (Best)` 可在未知 benchmark 上事前选择。Reference solution 通过生成
  tests 只证明自洽，不证明 tests 完整、expected output 唯一或没有 shared bug；当前 comparator 缺陷又使
  开源 reward 不能被当作无误的 ground truth。
- **Limitations / Threats to Validity:** synthetic tests 继承 generator bias，只有 Python；问题来自
  verifiable-coding dataset，与多个 code benchmark 可能共享题型、平台或污染路径；每问题看起来仅一项
  test per tier，tier 名称不等于 coverage。缺少 seeds/statistical uncertainty、能力选择协议、dynamic
  controller、held-out tier mutation tests 和 reward implementation validation。论文与当前 artifact 的
  generator/count drift、无 tag/release 与 prefix-output bug 进一步限制 strict reproduction。
- **Trade-offs / New Failure Modes:** tiering 增加 verifier generation/validation cost、taxonomy drift 与
  suite version；hard-first 提高有效 challenge，也可能让弱 policy 全零 collapse；easy-first 提供 gradient，
  也可能长期过采样 trivial cases。分开 allocation 与 weighting 提高控制力，却扩大 policy-search space；
  若两者、reward ceiling、KL beta 和 sampling temperature同时变化，归因困难。训练直接暴露 tests 还会让
  policy overfit/hard-code verifier；sandbox timeout、parser、stdout normalization 或 reference bug 都会被
  GRPO 放大成 gradient。
- **Where the Previous Design Still Applies:** full-suite average/pass-all 仍适合 suite 小、coverage 已审计、
  policy success rate 位于有信息区间且不需要 curriculum search 的任务；固定 easy-to-hard 适合 capability
  未校准、重训练预算有限的保守启动；held-out/adversarial/mutation tests 和 human review 仍负责验证
  reward 外的真实正确性。动态 controller 在没有稳定 feedback 与 replay contract 时不应取代静态 schedule。
- **Evolution Relationship:** `Direct Evolution`：single binary test reward → per-test partial reward →
  intra-problem difficulty slices → separate exposure schedule and reward valuation → future online
  capability-conditioned controller。`Layering / Dependency`：curriculum 管 data exposure，verifier 管
  reward evidence，GRPO 只消费相对 reward；任一层缺陷都不能由另两层自动修复。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch27 映射错误，主 owner 是 Ch29；已读相邻
  Ch28～30，并检查 Ch23 与 Ch62。Ch29 已明确 success rate 接近 0/1 时应调整 curriculum/reward/task
  distribution、verifier 是被优化 specification、held-out tests 与 environment identity 必须保留；Ch23
  已把 sampling 定义为 data distribution policy；Ch62 已覆盖 executable verifier 的不完整与版本化。
  TAROT 的长期原则已被这些章节覆盖，论文当前没有提供足够可信的新 controller 或 verifier mechanism。
- **Integration Decision / Changed Files:** `No Change — Already Covered / Capability Selection and Verifier
  Contract Incomplete`。本轮只更新 Weekly，不修改 Books。若未来提供预注册的 capability→schedule rule、
  多 seed paired results、修复且有 mutation tests 的 reward artifact，以及在线 adaptation/rollback 证据，
  再考虑在 Ch29 refine “allocation 与 valuation 分离”；当前不把论文 benchmark 或 TAROT 名称写入正文。
- **Open Questions:** capability score 怎样由 per-tier outcome/uncertainty 校准并事前选择 schedule；如何避免
  `TAROT (Best)` selection bias；tier suite 怎样做 mutation/coverage/differential testing；reference 与生成器
  shared bug 如何发现；reward comparator、line count、timeout、normalization 怎样建立 golden tests；active-tier
  reward ceiling 是否应归一化；curriculum phase、verifier version 与 GRPO checkpoint 如何原子恢复？

### The Vision Wormhole / Heterogeneous Latent Multi-Agent Communication

- **Candidate / Week / Score:** The Vision Wormhole / 2026-W08 / 23/30；
  `Source Family ID: vision-wormhole-heterogeneous-latent-mas`。
- **Source Type / Date / Revision / Sources:** arXiv 论文与作者官方代码；v1 于 2026-02-17 首发，v2 于
  2026-05-28。W08 事实以 v1 为准；v2 只用于 revision audit。GitHub history 显示事件日有 initial commit
  `a0e58a3` 与 README update `d1530a6`，当前 main 已含 3 月新增 OCR/LatentMAS-Hybrid baseline，但没有
  tag/release，不能把当前 main 当作事件日可重放 snapshot。
- **Access and Verification Status / Full-read Coverage:** Verified with artifact limitation；已读 v1 metadata、
  Introduction、Related Work、Method、全部主实验、single-agent 对照、weak-supervision、preliminary
  4B～12B、runtime contract、codec/alignment 公式、failure analysis、prompts 与 Appendix；对照 v2 新增 baseline、
  Limitations 与删改范围，并检查当前 README、codec/decoder、model wrappers、merge 与 experiment entry points。
  可用接口无法取回 event-date commit 的完整源码，因此 strict event-date code reproduction 标记为 unavailable，
  但不影响对论文机制和当前公开实现边界的核验。
- **Original Problem / Why the Previous Design Was Reasonable:** text message 是异构 Agent 最自然的公共接口：
  它不要求共享 tokenizer、hidden dimension、layer/KV layout，可被人读取、记录、过滤和重放。代价是 sender
  必须 decode、receiver 再 tokenize/prefill，长 reasoning trace 受 token bandwidth 和离散化约束。直接传
  hidden state/KV 能省掉部分文本路径，却在同构模型上才容易成立；为每个 sender→receiver 训练 translator
  又使 N 个 model family 的接入边数量最坏增至 O(N²)。
- **Changed Constraint / Principle:** 当一个 MAS 同时追求 heterogeneous model specialization 与低通信开销时，
  “消息格式”本身成为系统接口。论文把 VLM 原生可接收 continuous image embedding 的 pathway 当作较稳定的
  receiver port，并用 shared reference latent space 将 pair-specific translation 改写为 per-model adapter。
  这里的 O(N) 仅指新增 model family 所需的 alignment/adapter 数量，不是 runtime message、token、FLOP、latency
  或 network complexity 的普遍 O(N) 结论。
- **Mechanism / State Ownership:** 每个 VLM 拥有冻结 backbone、sender encoder、receiver decoder、dummy-image
  baseline、outbound/inbound affine alignment 与 codec version；共享层拥有 reference-space schema 和 append-only
  latent message buffer；Workflow 仍拥有 role order、message identity、authority 与 completion state。Sender 在
  prompt boundary 复用 KV cache 做 T-step continuous pseudo-token rollout，经 norm matching 与 Perceiver-style
  resampler 形成 fixed-size universal tokens；receiver 将累计 tokens 解码成 gated residual，重采样到自己的
  image-token span，再由冻结 VLM 继续生成。Text teacher 与 latent student 在 boundary hidden state、next-token
  distribution 和 injection RMS 上蒸馏；跨模型 affine map 用 anchor messages 拟合。
- **Control Flow / Data Flow:** role prompt → sender boundary hidden state → 1,024-step latent rollout → per-model
  encoder → reference-space affine map → shared latent buffer append → receiver inverse alignment/decoder → gated
  perturbation + dummy-image span → next role；最后 judger 才输出 text。实验固定 Planner→Critic→Refiner→Judger，
  因而验证的是 sequential channel replacement，不是任意 graph、parallel/decentralized routing 或 dynamic topology。
- **Implementation Details / Artifact Audit:** 论文 recipe 为 D=512、六层/八头 codec、dropout 0.10、latent
  steps 1,024、image injection tokens 256、AdamW `2e-4`、400 steps、batch 2，backbone frozen。当前实现确实含
  semantic/global/style queries、cross-attention resampler、affine application、decoder gate 与多种 VLM image-span
  适配。但论文 Appendix 把 `K_u=1024` 写作 codec-token 数，README CLI 把
  `vision_codec_tokens=1024` 传给实现中的 semantic-query count，而代码随后再 append global/style 两个 query；
  这形成 1024 与 1026 的公开 notation/config ambiguity。当前仓库还自述为 ongoing project，未提供 release、
  event-date environment lock 或完整结果 artifact，严格复现必须先解决 snapshot 与 token-count identity。
- **Evaluation Contract:** 九个 reasoning/code benchmark；主设置覆盖 Qwen3-VL-2B、Gemma-3-4B、
  SmolVLM2-2.2B、LFM2.5-VL-1.6B 的两模型与四模型组合，Appendix 另有 Qwen3-VL-8B/Gemma-3-12B 等
  preliminary setting。全部为 NVIDIA A6000；主 two-backbone 同置一张 GPU，four-backbone 与 4B～12B 用两张；
  greedy decoding，max-new-tokens 2,048～20,000，batch 12/8/4，OOM 后按 12→8→4→2→1 重试。
  论文报告的是 `batch wall time / samples`，不是 interactive p95/p99、跨机网络 latency 或 production SLO；
  precision、seed、error bar、显著性、训练 wall time 与 codec checkpoint size 均未完整披露。
- **Baselines / Ablations / Sensitivity / Overhead:** v1 的主要 baseline 是 matched-prompt TextMAS；没有完成与
  Cache-to-Cache/LatentMAS 的等条件主表。v2 才加入 OCR 与 heterogeneous LatentMAS-Hybrid failure sweep，不能
  反写为 W08 证据。主表并非所有 cell 都提速：部分 code setting 为 0.57×、0.58×、0.64×、0.79×、0.85×、
  0.93×；accuracy 也有 -10.0pp、-7.5pp、-7.1pp 等回归。弱监督少于 100 anchors 时仍呈配置依赖；v1 的
  4B～12B preliminary setting 虽 macro speedup 5.92×，macro accuracy 却为 -5.3pp，且该整段在 v2 被移除，
  因而不能用“规模越大越有利”解释。缺少 codec-token/rollout-length、anchor 数量、alignment family、gate、
  buffer growth、placement 与 TextMAS message-length 的系统消融。
- **What the Evidence Proves:** 在固定四角色顺序、指定 VLM families、A6000 placement、batch-normalized
  runtime 与公开 benchmark 下，vision-token pathway 可以承载经过 per-model codec/alignment 的异构 latent
  message；hub-and-spoke adapter 把 pair-specific integration graph 变成每模型一次接入，并在多数而非全部
  cell 降低 wall time。它还证明通信表示会改变 accuracy/coordination behavior，不能只当 serialization 优化。
- **What It Does Not Prove:** 不证明任意 LLM/VLM、任意 Agent topology 或长时任务都能无损 latent communication；
  不证明 vision span 是跨版本稳定 ABI，不证明 O(N) runtime scaling，不证明 macro average 可代表每个 task，
  也不证明 latent message 能替代 typed artifact、authoritative state、human-readable evidence 或 security audit。
  single-agent 对照是跨配置 macro aggregation，不能隔离 role assignment、弱模型注入与 channel 的全部因果贡献。
- **Limitations / Threats to Validity:** 仅 VLM、公开小中型 checkpoints 和固定 sequential workflow；没有随机
  seeds/uncertainty、真实用户/工具/副作用、networked execution、failure injection、message corruption、codec
  upgrade、cross-version compatibility 或 adversarial latent input。Affine basis 假设在训练数据、tokenizer、
  multimodal fusion 与 norm calibration 差异大时可能失效。Append-only latent buffer 的增长、过期、顺序、
  replay identity、删除和冲突语义没有形成生产协议；latent content 本身不可读，降低诊断和 policy inspection。
- **Trade-offs / New Failure Modes:** text channel 慢但 portable/auditable；direct hidden/KV 快但强耦合；
  pairwise translator 局部可调但 integration edge 爆炸；hub codec 降低接入边数，却形成 shared-space version、
  anchor quality、codec drift、receiver calibration 与 central schema dependency。Fixed-size message 限制 bandwidth，
  也可能静默丢失 rare evidence；gate 抑制过注入，但其误判不可由文本日志直接解释。新增风险包括 codec poisoning、
  latent prompt injection、cross-tenant leakage、model upgrade incompatibility、undetected semantic corruption、
  non-replayable handoff 与 text fallback 分叉。
- **Where the Previous Design Still Applies:** text/typed artifact 仍适合高风险、需 provenance、跨组织、异步、
  长期持久化、人工审批或 heterogeneous non-VLM 场景；homogeneous co-located models 可继续直接传 hidden/KV；
  模型族少且 pair semantics 特殊时 pairwise translator 可能比统一 hub 更可控。Latent channel 更适合可容忍近似、
  接口由同一 operator 治理、模型/codec 版本固定且最终结果有独立 verifier 的 bounded ephemeral handoff。
- **Evolution Relationship:** `Direct Evolution`：human-readable text → homogeneous hidden/KV transfer →
  pair-specific heterogeneous translator → shared latent hub + per-model adapter。`Layering / Dependency`：latent
  channel 只优化 communication representation；Ch77 的 workflow state、Ch78 的 role/topology/verification 与
  Ch79 的 protocol/authorization 仍在其上，不会被 codec 取代。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch57～59/76 映射错误；主 owner 应为 Ch78，已读
  Ch77～79，并检查 ROADMAP Communication/State 横线。Ch57 KServe、Ch58 Gateway、Ch59 GPU Scheduler 管
  serving/platform control plane，不拥有 Agent message semantics；Ch76 是 Reflection。Ch78 已覆盖 coordination tax、
  topology、typed handoff、message/state 分离与 failure，但缺少从 text 到 latent representation 的演进、兼容性、
  inspectability 与 fallback contract，因此这不是已有观点的简单重复。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Experimental Latent Message Contract /
  Scope and Revision Corrected / Human Gate Pending`。本轮仅更新 Weekly，不修改 Books。整周 Evidence Gate 与
  人工 Review 通过后，候选内容应 refine Ch78 的通信表示层：保留 text/typed artifact 成立条件，把 latent codec
  作为 experimental branch，并要求 message identity、codec/model version、fidelity probe、text fallback、
  verifier、audit projection 与 replay policy；不写论文 headline 或孤立项目介绍。
- **Open Questions:** 怎样定义 latent message schema/identity 与跨 model/codec version compatibility；如何测
  semantic fidelity 而不只看 final accuracy；buffer 的 TTL、ordering、supersession、dedup 与 rollback 由谁拥有；
  怎样生成可审计 text projection 而不让 projection 反过来成为权威消息；怎样防 latent injection/tenant leakage；
  codec drift 如何 canary；何时 fallback 到 text/typed artifact；在跨机网络、p99 SLO 和工具副作用下收益是否仍在？

### DreamZero / World Action Models are Zero-shot Policies

- **Candidate / Week / Score:** DreamZero / 2026-W08 / 22/30；
  `Source Family ID: dreamzero-world-action-model-2026`。
- **Source Type / Date / Revision / Sources:** NVIDIA 作者团队论文、项目页与官方代码。arXiv 只有 v1，首发于
  2026-02-17；论文事件以该版本为准。官方仓库当前 README 记录 2 月 20 日才公开完整 training code、dataset
  和 guide，之后又增加 checkpoint 与修复；仓库没有 release/tag，因此当前 main 只能核验实现家族，不能当作
  2 月 17 日 paper-time snapshot。
- **Access and Verification Status / Full-read Coverage:** Verified with artifact-time limitation；已读 metadata、
  Introduction、Related Work、architecture/flow-matching objective、closed-loop inference、全部 model/system/
  implementation optimizations、pretraining/post-training、real-robot evaluation、全部 ablation、alternative world-model
  architectures、training/inference pseudocode、数据收集、evaluation details 与 failure cases；并核对当前 README、
  distributed WebSocket inference path、client、training config 与 dataset guide。论文没有独立 Safety、Limitations 或
  Threats to Validity 章节，相关边界需从 Discussion、footnote、Appendix 和 artifact 中恢复。
- **Original Problem / Why the Previous Design Was Reasonable:** 模块化 `high-level planner + skill library + low-level
  controller` 可解释、容易限制动作，但要求预先拥有技能库和可靠接口，跨模块误差会累积；end-to-end VLA 将
  language/vision semantics 直接映射为动作，在训练任务覆盖充分时更简单，却主要继承静态 image-text prior，未必
  学会新环境中的几何、动力学和未见 motion。显式 latent world model 或 3D world model 更紧凑、可做 search/MPC，
  但需要额外 planner、objective 或 inverse-dynamics interface。它们都是合理分支，不因 WAM 出现而失效。
- **Changed Constraint / Principle:** 当任务要求用少量 heterogeneous robot data 泛化到未见 motion，并要求真实机器人
  持续响应环境时，仅有 semantic prior 或离线 imagined trajectory 不够。论文把未来 video 当 dense predictive target，
  把 action 与其共同建模：`p(video_future | history, language, proprioception) × p(action | video_future,
  proprioception)`。核心假设是 pretrained video diffusion 的时空 prior 能充当 implicit visual planner，再由 joint
  action head 学 inverse dynamics；这是作者在指定机器人任务中的实验性设计，不是“生成视频必然学得因果物理”。
- **Mechanism / State Ownership:** Wan2.1-I2V-14B-480P 初始化的 autoregressive DiT 接收 VAE visual context、
  text condition 与 proprioceptive state，用 flow matching 联合去噪 video/action latent，并由独立 decoder 输出两种
  modality。Model/KV cache 拥有约 6.6 秒 visual history 与当前预测上下文；motion controller 拥有正在执行的最新
  action chunk；sensor/environment 拥有 authoritative actual state；runtime 必须拥有 observation timestamp、chunk
  revision、deadline、cancel/override 与 safety interlock。论文只实现前述 model/controller path，没有把后半套生产
  authority contract 定义完整。
- **Control Flow / Data Flow:** initial observation prefill → joint video/action denoising → motion controller 执行 action
  chunk → 最新真实 observation 编码并写回 KV cache → 丢弃 predicted visual state 作为下一轮 authoritative history →
  继续生成。AgiBot action horizon 为 48 steps@30Hz，DROID 为 24 steps@15Hz，均覆盖 1.6 秒；controller 与 inference
  异步，前者持续执行最近 action，后者消费最新 observation。这个闭环减少长视频自回归预测误差，却不能消除当前
  chunk 内的 open-loop exposure，也新增 stale action、out-of-order observation、late result 和 emergency-stop 语义。
- **Implementation Details / Artifact Audit:** 论文从 naïve 16-step/14B 路径叠加双 GPU CFG parallelism、DiT cache、
  `torch.compile`/CUDA Graph、cuDNN attention、GPU scheduler、GB200 NVFP4/FP8/FP16 mixed precision 与
  DreamZero-Flash。Flash 将 video noise timestep 偏向高噪声 `Beta(7,1)`、action timestep 保持 uniform，使 action
  decoder 在不完整 visual plan 下训练，把四步去噪缩到一步。论文称双 GB200 optimized stack 从 5.7s 降到 150ms；
  当前 README 却写启用 DiT cache 后约 0.6s/GB200、约 3s/H100，且 current distributed server 需要至少两张 GPU。
  这说明公开 run path/config 与 paper optimized path 尚未形成同一可重放 artifact，不能混写为一个速度事实。
- **Training Contract:** AgiBot 约 500 小时、7.2K episodes、22 environments、平均 episode 约 4.4 分钟，DROID
  使用公开数据；两者各训练 100K steps、global batch 128，更新 DiT blocks 和 state/action encoders/decoder，冻结
  text/image encoder 与 VAE。论文未披露 optimizer、learning rate、precision、完整并行布局、训练 GPU 型号、wall
  time 与能耗。当前仓库默认 4 GPU、per-device batch 1、LoRA、`lr=1e-5`、`max_steps=10` 是 sanity-check recipe，
  不是论文 pretraining contract。
- **Evaluation Contract:** AgiBot seen/unseen 各 10 tasks×8 rollouts/checkpoint；DROID seen/unseen 各 20 tasks×2
  rollouts/checkpoint；post-training 为每 task 10 rollouts，结果主要是人工/任务 progress 0～1。主比较使用相同 data、
  total batch 和 gradient steps，但 baseline 还分 from-scratch 与带数千小时先验数据的 pretrained checkpoint。论文
  报告 AgiBot 平均 progress 62.2% 对最佳 pretrained VLA 27.4%，这只是在作者 task、harness 与 checkpoint 下的
  comparative evidence；不能外推为 WAM 对 VLA 的普遍 2x 优势。
- **Baselines / Ablations / Sensitivity / Overhead:** 受 50K steps、batch 32、PnP Easy 限制的 ablation 中，diverse
  data 对 repetitive data 为 50%±6.3 对 33%±4.2，14B 对 5B 为 50%±6.3 对 21%±4.2；AR 与 bidirectional
  平均同为 50%，只显示不同 variance，不能证明 AR 普遍更准。DreamZero-Flash 在单个 table-bussing setting 中为
  74%±10.1，而四步 baseline 为 83%±6.1、naïve 一步为 52%±10.2。缺少多 seed、统计检验、各优化的完整 accuracy/
  power/memory ablation、端到端 p95/p99、network/controller jitter 和等硬件成本比较。
- **What the Evidence Proves:** 在作者的 AgiBot/DROID real-robot contract 下，联合 video/action prediction 可以
  形成可执行闭环；真实 observation 回灌使预测 video 不再永久充当事实状态；异步 action chunk 与多层优化可让
  大型 diffusion policy 在指定硬件上接近论文设定的 reactivity window。failure cases 还直接显示 action 会忠实执行
  错误 visual plan，因此 world prediction quality 与 action safety 是耦合对象，而非两个可独立验收的模块。
- **What It Does Not Prove:** 不证明 video prediction 等于 causal world model，不证明作者所谓 zero-shot 覆盖开放世界，
  不证明 7Hz 足以满足所有机器人 dynamics/SLO，不证明回灌 ground truth 可消除 chunk 内误差，也不证明 human/video
  transfer 可扩展到 web-scale 或任意 embodiment。论文没有 evaluation memory-only tasks；约 6.6 秒 context 不能支持
  长时任务。150ms headline 也不代表当前开源 H100/GB200 路径、单 GPU、tail latency 或 production controller。
- **Limitations / Threats to Validity:** 数据、architecture、pretrained prior、model size 与 system optimization 同时变化，
  attribution 有限；真实机器人 rollout 样本较小，progress scorer、seed/significance 和 safety incidents 未充分披露；
  训练数据集中于一个 AgiBot system，DROID 又是另一 embodiment 独立 pretraining。当前 artifact 无 event-date tag、
  paper optimized config、action lease/deadline、sequence reconciliation、policy gate 或 safety interlock；WebSocket server
  更接近研究 harness，不能据此声称 production readiness。
- **Trade-offs / New Failure Modes:** joint WAM 降低 planner/skill-library handoff，代价是 14B video path、训练/推理
  成本、可解释性下降与 video/action correlated failure；AR + ground-truth replacement 保留历史并限制跨 chunk drift，
  代价是 cache identity、observation freshness 与 short-context ceiling；大 action chunk 为慢模型争取时间，却扩大环境
  变化后的 open-loop exposure；异步执行隐藏 inference stall，却新增 stale/late chunk、控制权争用与 rollback 困难；
  cache/quantization/one-step denoising换取 latency，也会带来近似误差与 hardware specificity。
- **Where the Previous Design Still Applies:** 高风险、强约束或可用技能库的任务仍适合显式 planner + verified skills +
  low-level safety controller；动作数据充分且消费级硬件/高频控制优先时 VLA 仍可能更合适；需要显式 counterfactual search
  或 MPC 时 latent/3D world model + separate planner 仍有价值。WAM 更适合视觉动态 prior 有用、可容忍生成式近似、
  action 有独立 safety envelope 且真实 observation 能高频回灌的场景。
- **Evolution Relationship:** `Direct Evolution`：semantic VLM/VLA prior → video-conditioned inverse dynamics → joint
  world/action prediction → AR action chunks + actual-observation replacement → async execution + latency-aware
  model/system co-design。`Layering / Dependency`：WAM 只提供低层 implicit visual plan/policy；高层 goal decomposition、
  safety policy、control authority、verification 与 durable Workflow 仍位于其外部。它不是显式 Planning 的全量替代。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch18/71/75 映射已收敛为 Ch75 主 owner；已读 Ch74～77，
  并检查 Ch10、Ch18、Ch38、Ch42。Ch18 只拥有 Decoder-only token architecture，Ch71 只拥有 Agent context，Ch10
  已覆盖 world-model 长期方向，Ch38/42 拥有 inference request/scheduling，不拥有 physical action authority。Ch75 已有
  belief→action→observation/replanning 主干，但缺少“显式 model-based search 与 implicit generative policy”分支、actual
  observation replacement、action-chunk freshness 和 wrong-world-plan→wrong-action 的机制链，因此存在可契合的 refine。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Closed-Loop World-Action Policy and Reactivity
  Contract / Scope and Artifact Boundary Corrected / Human Gate Pending`。本轮只更新 Weekly，不修改 Books。W08
  Evidence Gate 与人工 Review 通过后，候选应最小化 refine Ch75：保留模块化/VLA/latent/3D 旧分支，增加 implicit
  predictive policy 的闭环、authority/freshness/safety contract；Ch38 或 Ch42 至多增加一条 action-window handoff，
  不写 2x、38x、7Hz 或产品名为通用结论。
- **Open Questions:** 真实 observation、predicted video、proprioception 与 action chunk 如何绑定 timestamp/revision；
  late result 怎样 cancel，chunk 已部分执行时怎样 reconcile；安全 controller 如何拒绝与 visual plan 对齐但危险的 action；
  怎样区分 video plausibility、causal dynamics、action alignment 与 task success；更长 context 是否增加 stale state 和
  memory cost；当前仓库能否公开 paper-time optimized config、trace、tail latency 与 failure-injection evidence？

### Multi-agent cooperation through in-context co-player inference

- **Candidate / Week / Score:** In-context co-player inference / 2026-W08 / 21/30；
  `Source Family ID: google-in-context-coplayer-inference-2026`。
- **Source Type / Date / Revision / Sources:** Google Paradigms of Intelligence 团队学术论文；arXiv 只有 v1，
  首发于 2026-02-18。论文没有链接代码、dataset、project page 或 release；公开搜索未定位作者官方 artifact，
  因而实现可审计性限于论文中的 pseudocode、hyperparameters 与软件列表。
- **Access and Verification Status / Full-read Coverage:** Verified with no official artifact；已读 metadata、Introduction、
  POSG/IPD setup、mixed-pool training、PPI/A2C、全部 main results、causal decomposition、implementation details、
  ablations、additional trajectories、PPI variational derivation、predictive-equilibrium definitions/proofs、Nash/subjective
  embedded equilibrium 关系与 software/LLM-usage disclosure。论文没有独立 Limitations、Ethics 或 Threats to Validity
  章节，需从实验范围、Appendix assumptions 与不稳定结果恢复边界。
- **Original Problem / Why the Previous Design Was Reasonable:** decentralized MARL 中每个 agent 把 co-player 当环境一部分，
  但对手也在学习，使 transition distribution 非平稳；self-interested agents 又可能收敛到 mutual defection。显式
  learning-aware 方法通过对手 update rule 求导，能定向 shape 对手，却要求知道并固定其 optimizer/update；另一类
  meta-learning 方法让 fast naive learner 与 slow meta-learner 分时标更新，语义清楚但角色不对称、训练复杂。固定 opponent
  ID 则让 best response 更直接，却无法处理未知或变化策略。这些旧方案在对手类型可知、更新可观测或需要可解释机制时仍合理。
- **Changed Constraint / Principle:** sequence policy 已能把整段 interaction history 当 Context，在单个 episode 内改变行为，
  不必真的更新参数。论文把这种 fast in-context adaptation 视为过去 naive learner 的功能替代：对多样 co-player 训练迫使
  agent 从行为历史推断对手并学习 best response；这种适应性同时使它可被另一 agent shaping/extortion。slow in-weight
  learning 再根据这些互动调整 policy，形成 fast context state 与 slow parameter state 的双时间尺度闭环。
- **Mechanism / State Ownership:** 每个 agent 只拥有 local history `x<=t=(observation, previous action, previous reward)`、
  GRU hidden state、policy/world-model parameters 与自身 reward；environment 拥有 joint action→payoff transition，但没有
  central controller 或 shared authoritative state。训练 pool 以 50% learning-agent、50% 从五维 memory-1 parameter space
  uniform sample 的 static tabular agent 组成，且不提供 identity。PPI 的 sequence model 同时作为 joint trajectory predictor、
  behavioral prior 和 Monte Carlo simulator；A2C 则直接用 recurrent policy/value head。合作不是 protocol invariant，而是
  特定 payoff、population distribution、adaptation dynamics 与 optimization 共同产生的 equilibrium behavior。
- **Control Flow / Data Flow:** 100-round IPD history → recurrent state 推断 co-player response → 当前动作 C/D → joint payoff/
  observation 返回 history。PPI 外层每 phase 用 sequence-model rollout 估计 15-step Q，以
  `p(a|history)·exp(beta·Q)` 改善 policy，采集新 trajectories，再将所有新旧数据合并并从头训练 model；A2C 用 standard
  decentralized policy gradient。机制分析把路径拆为：tabular diversity 产生 in-context best response → fixed in-context
  learner 可被新 agent extort → 两个 extortion agent 相互 shape → 部分 seeds 中转向 cooperation。
- **Implementation Details / Training Contract:** PPI 为 128-dim GRU、32-dim modality embeddings、separate observation/
  action/reward heads；先在 200K random-tabular trajectories 上 pretrain，再做 30 phases，每 phase 20K trajectories、
  accumulated replay、10 epochs、batch 256、AdamW `1e-4`、weight decay `1e-2`、gradient clip 1.0、`beta=0.01`。
  A2C 使用同尺寸 GRU 并为四个 mechanism steps 分别搜索 learning rate、GAE、normalization、reward scaling 与 entropy；
  best setting 才报告。JAX/Flax/Optax 等软件被披露，但 commit、version、hardware、runtime、sample cost 与 code 均未公开。
- **Evaluation Contract:** 环境只有两 agents、两个 actions、五种 observations、固定 payoff matrix 与 horizon 100；main
  curves 为 10 random seeds，部分 A2C mechanism figure 只有 5 initializations。主证据是 cooperation/defection ratio 与双方
  per-round reward trajectory，不是自然语言 Agent、heterogeneous tools、通信、long-horizon workflow 或有副作用环境。
  实验用 opponent-ID 和 no-tabular-pool ablation；前者显式给 tabular parameters/learning-agent flag，后者还同时改变 PPI
  pretraining distribution，因而不完全隔离“identity exposure”和“diversity/history inference”的各自贡献。
- **Baselines / Ablations / Sensitivity / Overhead:** mixed pool 下 PPI 与 A2C 最终趋向 cooperation，而显式 opponent ID 或
  移除 tabular opponents 的版本趋向 defection；step-wise experiment支持 adaptation→extortion→mutual shaping 的可能链条。
  但 A2C 的 mutual extortion 会随 seed 再坍塌为 defection，作者自己报告 training instability；hyperparameters 为事后 best
  search，缺少 held-out opponent families、population ratio/payoff/horizon/history-length sensitivity、communication noise、
  collusion/adversarial policies、compute overhead 和等预算 comparison。
- **Theory / Evidence Boundary:** PPI derivation给出 KL-regularized surrogate 与 local gradient relation，并在 compactness、
  continuity、finite KL 等条件下构造 mixed predictive equilibrium；把 mixed equilibrium提升为 pure parameter equilibrium
  还依赖 functional convexity，而作者承认这对 finite-capacity network 是 idealization。Existence theorem 不保证 algorithm
  convergence、equilibrium uniqueness、cooperation、social welfare 或 robustness；perfect predictive equilibrium 只约束
  on-path distribution，off-path counterfactual 仍可能任意错误，因此也不能当作安全保证。
- **What the Evidence Proves:** 在指定 IPD、mixed population、GRU/PPI/A2C 与调参 contract 中，不显式提供 opponent ID
  的 history-conditioned policy 可以表现出 episode 内 best-response adaptation；这种 adaptation 会被对手利用，且 mutual
  shaping 在实验中可把部分 training trajectories 推向 cooperation。它说明 partner inference 是 Multi-Agent state 的一部分，
  也说明“更会适应”同时扩大 strategic attack surface。
- **What It Does Not Prove:** 不证明 foundation-model ICL 与小型 GRU 使用同一机制，不证明多样训练数据足以让开放 Agent
  合作，不证明合作是稳定/公平/合意 equilibrium，也不证明 self-interested reward 与 extortion 是生产协作的合理设计。
  不提供 co-player identity 反而改善 IPD 结果，不等于系统应隐藏 identity、authority 或 audit principal；runtime identity
  与 policy inference 是两类不同对象。
- **Limitations / Threats to Validity:** 单一两人 IPD、固定 horizon/payoff、memory-1 tabular population 与极小 action/state
  space；训练和 evaluation pool 关系有限，缺少现实分布外伙伴、communication、coalition、partial identity、tool side effect、
  malicious peer 与 human norms。No-mixed-pool ablation 同时变化 pretraining，A2C 有 seed collapse，best-hyperparameter reporting
  存在 selection bias；无公开 code/hardware阻止 strict reproduction。理论 assumptions 与 neural optimization gap 很大。
- **Trade-offs / New Failure Modes:** history-based partner inference 避免 hardcoded opponent update 和角色时标分离，却增加
  belief error、behavioral fingerprinting、distribution shift、策略诱导与非平稳 replay；多样 pool 促进适应，也可能教会
  exploitation/collusion。Fast in-context state 提供快速响应，但不可审计、会被 adversarial history 污染；slow weight update
  可沉淀策略，却会把短期对手行为固化。合作 equilibrium 可能提高双方 reward，也可能只是 tacit collusion、排斥新成员或
  对不同 payoff 失效，必须由外部 policy/evaluation 定义“可接受合作”。
- **Where the Previous Design Still Applies:** 对手 update 已知且需要可解释 shaping 时保留 explicit learning-aware method；
  快慢角色天然不同的组织/训练场景可保留 meta-learner separation；稳定 protocol、已知身份或高风险协作应优先使用 typed
  contract、deterministic rules 与 central policy，而非让行为推断替代 authorization。单 Agent + Workflow 在任务无需真正
  strategic peer 时仍是更小、更可验证的系统。
- **Evolution Relationship:** `Direct Evolution`：fixed/identified opponent → explicit opponent-update model → separated
  naive/meta timescales → sequence policy 以 history 实现 fast partner adaptation + slow in-weight learning。`Principle Reuse`：
  Context 作为 working state、population diversity 作为 training distribution、performative loop 中 policy 改变未来数据。
  这条演进不表示后者替代 identity、protocol 或 governance。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch76 映射错误；主 owner 为 Ch78，已读 Ch77～80。Ch76 研究基于
  verifier/observation 修正自己的 candidate，不拥有 strategic co-player inference；Ch77 拥有 authoritative workflow state，
  Ch80 拥有 runtime identity/policy。Ch78 已覆盖 topology、coordination tax、stale message 与 malicious peer，但未明确区分
  runtime identity 与 inferred behavioral policy，也未覆盖 fast partner adaptation 的收益/可利用性双面，因此存在契合 refine。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Experimental Partner-Adaptation and Strategic
  Shaping Contract / Owner and Scope Corrected / Human Gate Pending`。本轮只更新 Weekly，不修改 Books。W08 Evidence
  Gate 与人工 Review 通过后，应在 Ch78 以短机制段落补充 `observed history → partner belief → adaptive action → peer shapes
  future history`，同时要求 identity、authority、policy constraints、adversarial partner eval 和 equilibrium/welfare evidence；
  不写“extortion 自动产生合作”或论文 IPD 曲线为通用规律。
- **Open Questions:** partner belief 如何显式版本化、校准并与 authenticated identity 分离；对手策略突变、伪装或 coalition
  时如何检测 belief drift；什么 external policy 判定 cooperation、collusion 和 extortion；mixed population 的比例、覆盖与
  curriculum 怎样进入 reproducible EvalSpec；fast context state 与 slow weight/memory update 如何防 poisoning；能否在
  heterogeneous tools、partial observation 和有副作用任务中复现而不牺牲 safety？

### ReFINE / Reinforced Fast Weights with Next-Sequence Prediction

- **Candidate / Week / Score:** REFINE / 2026-W08 / 23/30；
  `Source Family ID: refine-fast-weights-next-sequence-2026`。
- **Source Type / Date / Revision / Sources:** Princeton Visual AI 学术论文与作者官方实现。arXiv 只有 v1，首发于
  2026-02-18；官方 Git history 显示 artifact 在 paper 前已开始形成且 2 月 17 日仍有更新，当前无 release/tag。
  当前 README 明示论文使用的 Long-Data-Collections 已不可获取，并建议以 SlimPajama-6B 替代；替代数据只能验证
  code path 可运行，不能重现论文的 data distribution 或 headline results。
- **Access and Verification Status / Full-read Coverage:** Verified with reproduction limitation；已读 metadata、Background、
  NTP/NSP objective、entropy selection、rollout/reward/GRPO-like optimization、mid/post/test-time training、全部结果、
  reward/selection analysis、`k/c` ablation、Discussion/Limitations/Impact、Related Work、dataset/metric inventory、全部
  hyperparameters、compute、validation/entropy/reward/short-context analyses 与 qualitative examples；并核对官方 README、
  commit history、training/evaluation entry points和数据替代声明。受网络接口限制未逐文件打开 current source tree，
  因而 artifact audit 只证明公开 implementation family 与入口存在，不声称 code-level strict reproduction 已完成。
- **Original Problem / Why the Previous Design Was Reasonable:** dense Attention 保留显式 token-to-token addressing，能直接
  用 NTP 为每个位置提供监督，但 Attention/KV state 随长度增长；linear/recurrent fast-weight architecture 把历史压进固定
  大小矩阵或 memory state，换取近似 constant memory/linear execution，却让每次 online write 同时影响多个后续预测。
  NTP 对当前 next token 提供密集、稳定、低成本梯度，在短期预测和普通 Transformer 上仍合理；问题是它未显式评价一次
  fast-state write 对未来 sequence 的整体影响，而不是 NTP 本身失效。
- **Changed Constraint / Principle:** 当内部 state 是有损、持续更新且被多个未来 token 复用时，training objective 的
  credit horizon 应匹配 state 的使用 horizon。论文把 selected prefix 后的 `k`-token rollout 看成一个单位，用未来序列
  representation 的相似度反馈 fast-weight initialization；为避免每个 prefix 都 rollout，又按局部 NTP entropy 在每个 chunk
  采一个位置。长期原则是 `state lifetime ↔ objective horizon ↔ evaluation horizon` 要对齐，而不是“RL 比 CE 更强”。
- **Mechanism / State Ownership:** LaCT 的 fast weights 或 DeltaNet 的 recurrent memory state 拥有压缩后的 Context；base
  parameters/optimizer 拥有跨样本长期更新；当前 sequence/prefix、selected positions、rollouts、hidden-state reward 与
  old-policy identity 属于 training run。REFINE 先 full forward 计算 entropy，把 sequence 分为 `c=8` chunks，每 chunk
  entropy-weighted sample 一个 position；从八个截断 prefix 各 rollout `k=5` tokens，比较 prediction/ground-truth 最后一层
  hidden states 的逐位 cosine similarity，再与全序列 NTP loss 联合更新，避免只优化 rollout reward 后遗忘基础能力。
- **Control Flow / Data Flow:** sequence → full NTP forward/entropy/ground-truth hidden state → per-chunk position sampling →
  copy/truncate eight prefixes → policy rollout → representation/exact-match reward → same-sequence reward standardization →
  policy update + whole-sequence NTP update。Mid-training 用 cosine reward；post-training 在 instruction prompt 内 nested REFINE
  后再对 response SFT，并混合 cosine+exact match；TTT 直接对 test prompt 做 REFINE，用 exact-match reward。每个阶段
  改变的是 fast-state initialization/parameters，不是外部 RAG/Agent Memory。
- **GRPO Naming Boundary:** 论文称采用 GRPO，但 `n=1 rollout/selected position`，group 由同一长 sequence 中八个不同
  prefix positions 构成并在其 rewards 间标准化；这些 prefix 的 entropy、位置和预测难度并不相同。原始 Ch29 GRPO 的
  稳定语义是同一 prompt 下多 responses 共享任务难度。因此可复用的是“relative policy gradient without critic”原则，
  不能仅凭名称宣称它与原始 GRPO 在 grouping、credit、KL 或 sampling contract 上等价。论文还把 actor gradient clip
  记为 0.2、KL coefficient 设为 0，进一步要求按 exact implementation 而非算法名审计。
- **Training / Compute Contract:** 两个预训练 fast-weight models 为 LaCT-760M 与 DeltaNet-1.3B；mid-training 使用
  Long-Data-Collections 200M tokens、16K context，8×L40 约 24 小时；post-training 同为 8×L40，TTT 为 4×L40。
  batch 分别 128/64/8，PPO minibatch 32/16/4，learning rate `1e-6`、Adam `(0.9,0.999)`、weight decay 0.01、
  `lambda_SFT=1`、`lambda_RL=0.2/0.2/0.4`、sampling temperature 1、rollouts/position 1。未披露 L40 memory SKU、
  interconnect、precision、gradient accumulation、end-to-end tokens/s、energy、SFT 等算力 baseline 与 TTT per-request latency。
- **Evaluation Contract:** RULER NIAH 每长度 500 samples，4K/8K/16K；RULER SQuADQA/HotpotQA 各 1600 train/
  200 test；LongBench 选 12 个 English tasks 且过滤到 ≤16K，单任务样本 56～488；另用 Booksum validation 与九类
  short-context tasks。指标跨 recall/F1/ROUGE/accuracy/code similarity/perplexity，不能把平均分当统一概率质量。论文表格
  多为单点 score；Booksum curve 只有三 trials 的 min/max，主 benchmark 未报告 seed、error bar、significance 或
  paired per-example variance。
- **Baselines / Ablations / Sensitivity / Overhead:** 与 base 和同阶段 NTP SFT 比较；entropy-weighted sampling 在两个模型
  的 LongBench average 略高于 uniform/max/min entropy，cosine reward 略高于 binary。`k` 从 3→5 改善、到 7 回落，
  `c` 从 2→8 小幅上升，说明更长 rollout 并非单调更好且更多 chunks 伴随更多 compute。部分 RULER/LongBench cells
  仍回退；short-context average LaCT 45.1→45.0、DeltaNet 50.4→50.2，故“无 catastrophic forgetting”只表示该表未见
  大幅整体退化，不等于所有能力无损。没有和等 rollout-token/等 wall-time 的 CE、multi-token head、larger model、
  retrieval 或 attention hybrid 做完整比较。
- **Reward Boundary:** cosine similarity使用同一个正在更新模型的 final hidden space 同时表征 predicted 与 ground-truth
  continuation；reward scale/geometry 会随 policy 更新，语义相似不等于事实或 sequence correctness。位置对齐的 cosine
  也可能奖励逐 token 表示接近而非整体逻辑一致。Exact match 密集性低，hybrid reward 改变 memorization/generalization
  权衡；`k` 增大后 reward mean/variance 都下降，作者确认 signal sharpness 恶化。自监督 reward 消除人工标签，不消除
  self-referential drift、representation collapse 或 reward hacking 风险。
- **What the Evidence Proves:** 在两个 760M/1.3B fast-weight model、16K 数据与作者训练 recipe 中，稀疏选择 prefix、
  生成短 rollout 并用 sequence-level relative reward 与 NTP 联训，可以改变 long-context retrieval/QA 表现，且多数报告
  aggregate 高于同阶段 NTP SFT。它支持“压缩状态的写入目标不应只看下一 token”这一机制假设，并提供 mid/post/TTT
  三个 placement 的受限实验。
- **What It Does Not Prove:** 不证明 fast weights 已替代 dense/hybrid Attention，不证明 NTP 普遍不适合 long context，
  不证明 REFINE 对大型模型、>16K、instruction-tuned Transformer、生产 TTT 或不同数据分布有效，也不证明作者相对收益
  来自 RL 而非更多 rollout compute。它不证明 hidden-state cosine 是可靠 semantic verifier，更不能把 current substitute
  dataset 的可运行性当原结果复现。
- **Limitations / Threats to Validity:** 只有两种小型 fast-weight architecture 和单一 200M-token mid-training contract；
  post/TTT evaluation 与训练 task 分布接近，TTT 在 test prompt 上更新还需严格区分 transductive adaptation 与 label/test
  leakage。主结果缺少 uncertainty、等算力 baseline、state-transfer cost 与 long rollout scaling；官方原数据失效、当前仓库
  无 tag/release，environment/commit/checkpoint identity 不完整。论文 limitation 只提 reward/rollout length，未充分讨论
  self-referential reward、grouping mismatch、privacy/tenant reset 或 online parameter update 的生产风险。
- **Trade-offs / New Failure Modes:** fixed-state architecture 降低 length-dependent memory，却牺牲精确 provenance和可寻址
  retrieval；NSP 扩大 credit horizon，却需要多次 truncated-prefix forward/rollout、显著训练 compute 与复杂 replay state；
  entropy sampling聚焦不确定区域，也可能过采样噪声/罕见 token并漏掉低 entropy 但长期关键事实；TTT 提供 per-input
  adaptation，却新增 latency、checkpoint/reset、cross-request contamination、prompt poisoning、rollback 与 tenant isolation。
  NTP 混合项降低遗忘风险，也意味着收益无法归因于纯 NSP。
- **Where the Previous Design Still Applies:** dense/hybrid Attention 仍适合精确 retrieval、可承担 KV cost 或缺少成熟 fast-state
  kernel 的场景；标准 NTP 仍是大规模密集监督和通用能力底座；multi-token prediction heads 可在不引入 online RL/rollout
  时提供更短的额外 horizon；外部 RAG/Memory 仍负责 provenance、删除和跨会话状态。若 TTT latency、污染或恢复契约不可控，
  应在离线 mid/post-training 固化模型，而不是线上改权重。
- **Evolution Relationship:** `Direct Evolution`：dense token history → fixed-size recurrent/fast-weight state → NTP 训练的
  compressed state → selected next-sequence feedback → mid/post/test-time placement。`Layering / Dependency`：REFINE 是
  fast-state training policy，不是新 memory architecture；GRPO-like optimizer、reward representation 与 data lifecycle 位于
  其下。旧 Attention/NTP/RAG 分支各自仍在其适用条件成立。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch17/22/25 映射已收敛为 Ch22 主 owner；已读 Ch17、Ch22、
  Ch24 与 Ch29。Ch17 拥有 residual/norm/Attention/MLP layer 主干，不应加入训练 recipe；Ch24 拥有通用 NTP 与训练状态；
  Ch29 拥有原始 same-prompt GRPO contract。Ch22 已有 linear/recurrent state、test-time neural memory、write/forget/reset
  与 exact-token provenance 边界，但缺少“objective horizon 必须匹配 compressed-state lifetime”以及 online TTT rollout 对
  serving state 的新增成本，因此存在窄而契合的 refine。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Experimental Objective-to-State-Lifetime Contract /
  GRPO and Reproduction Boundary Corrected / Human Gate Pending`。本轮只更新 Weekly，不修改 Books。W08 Evidence Gate
  与人工 Review 通过后，最多 refine Ch22 的路线六：以无论文名的机制段说明 NTP 的合理性与 fast-state 长期 credit 缺口、
  sequence-level feedback 的 compute/reward/TTT trade-off；Ch29 仅加“不同 prefix grouping 不等价于同 prompt GRPO”的短
  handoff。不得写论文相对百分比或把 SlimPajama substitute 当复现。
- **Open Questions:** 同一 sequence 不同 prefix 的 reward 如何按 difficulty/entropy 校准；等 rollout-token、等 wall-time 的
  NTP/multi-token/REFINE 比较是否仍成立；hidden-state reward 用 frozen encoder 或 independent verifier 是否更稳定；fast
  state 怎样跨 truncated prefixes 复用以降低 compute；TTT 的 state identity、reset、rollback、tenant isolation、latency 与
  prompt poisoning 如何验证；原 Long-Data-Collections snapshot/checksum 能否恢复？

### MMA / Multimodal Memory Agent

- **Candidate / Week / Score:** MMA / 2026-W08 / 20/30；
  `Source Family ID: mma-memory-reliability-selective-action-2026`。
- **Source Type / Date / Revision / Sources:** 北京大学作者论文与官方代码。arXiv 只有 v1，首发于
  2026-02-18；官方仓库 2026-01-13 已有 initial release，论文次日 2 月 19 日更新 README，但没有
  tag/release 或论文声明的 exact experiment commit。事件日 Source Family 可核验，paper-time run identity
  与当前 `main` 仍不能画等号。
- **Access and Verification Status / Full-read Coverage:** Verified with artifact and reproduction limitations；已读
  metadata、Introduction、Related Work、MMA/MMA-Bench method、全部公式、FEVER/LoCoMo/MMA-Bench 主结果、
  evolutionary analysis、全部 ablation、sensitivity、Limitations、Conclusion 与完整 Appendix；并核对官方 README、
  commit history、confidence config、`confidence_module.py`、公开运行入口与 unit test。公开材料没有披露 API
  model snapshot、temperature、并发、硬件、延迟、token/cost、完整 bootstrap/significance 或 production SLO；
  因而不能复现 wall-clock，也不能把作者的 risk-aware utility 外推为生产 operating point。
- **Original Problem / Why the Previous Design Was Reasonable:** similarity retrieval 先解决“哪些 memory 与 query
  相关”，在来源较同质、事实变化慢且 conflict 稀少时，top-k relevance 加生成器判断是简单、低成本且合理的
  design。随着长期 memory 混入不同来源、时间、派生摘要与互相冲突的信息，相关不再等于可信；若仍把所有
  retrieved items 等权送入 reasoning，旧错误会跨轮次放大。问题不是向量检索本身失效，而是 retrieval 后缺少
  evidence qualification 与 selective-action policy。
- **Changed Constraint / Principle:** 长期 Agent 的 read path 至少要把四件事分开：`relevance` 决定候选，
  `reliability features` 描述来源/有效期/支持关系，`sufficiency` 判断证据能否支持本次 claim，`decision policy`
  决定 answer/abstain/escalate。一个 scalar confidence 只能是 policy 输入，不能同时充当事实真值、校准概率和
  action authority。source prior、recency 与 consensus 的适用条件不同，不能以固定加权和掩盖 hard constraint。
- **Mechanism / State Ownership:** MMA 在 MIRIX typed memory 之上增加 post-retrieval confidence module。论文把
  每条 memory 的分数写成 source prior、指数时间衰减与邻居 consensus 的归一化加权和，再据此重排 evidence
  与触发 abstention。Memory service 拥有 item、source、created/occurred time、embedding、links、stored
  confidence 与公式版本；retriever 拥有候选集合；answer policy 拥有 threshold/abstention operating point；原始
  source 或 authoritative system 仍拥有事实真值。任何一个模块都不能因输出高分而获得写回或执行 authority。
- **Implementation Details / Code Boundary:** 当前 settings 给出 30 天 half-life、0.4 abstain threshold 与
  `S/T/C=0.45/0.40/0.15`，config 另给静态 source scores 和等价于约 30 天衰减的 `lambda=0.0231`；但
  config loader 读取 `time_half_life_days` 而未读取 `lambda`，所以实际 half-life 来自 settings/env 而不是该 config 字段。
  代码按 source string substring 映射 prior，以当前时间对
  `created_at/occurred_at` 统一指数衰减，再用 embedding+fuzzy-text 建邻居。`compute_consensus` 读取邻居已存的
  `confidence`，乘 link weight 与 signed cosine 后聚合；没有发现独立 contradiction classifier、source independence、
  fixed-point/convergence、更新顺序、循环依赖、版本失效或批量重算协议。论文中的“negative semantic support”在
  当前实现只是 embedding cosine，语义矛盾可能仍高度相似。unit test 只验证相似 item 被拉高、无关 item 近似
  V1，没有覆盖矛盾、重复来源、correlated misinformation、乱序更新、staleness propagation 或 probability calibration。
- **Control Flow / Data Flow:** query → authorized typed-memory retrieval → similarity links → `S/T/C` feature
  calculation → heuristic confidence/reweight → LLM reasoning → answer or abstain → task-level scoring。若 memory
  新增、修正、supersede 或删除，可靠系统还应执行 source/version lineage、neighbor invalidation、confidence
  recomputation 与 decision trace；这些 production lifecycle 不是论文结果或当前公开实现已经证明的能力。
- **Evaluation Contract:** FEVER 只取前 500 条、3 个 seeds（42/922/2025）；MMA 与 MIRIX raw accuracy
  为 59.93% 与 59.87%，selective score 在 `alpha=0.2` 时为 0.6484 与 0.6468，所谓 35.2% 是三次运行
  standard deviation 从 2.50 降到 1.62 的相对变化，不是大样本显著性结论。LoCoMo 为 `N=1542`：full
  MMA 的 accuracy/actionable accuracy（72.31%/76.80%）低于 baseline（77.37%/78.96%），去掉 consensus
  的 `S+T` 才达到 75.94%/79.64% 与更少 wrong answers（298 vs 317）。Utility 数字必须带
  `lambda/r`：Table 7 的 883.6 属 `lambda=1,r=0.2`，Table 8 的 609.0 属 `lambda=2,r=0.5`；正文又把
  573.5/488.0 误指向 Table 7，不能脱离 operating point 引用。MMA-Bench 只有 30 个程序生成 case、每例
  10 sessions；GPT-4.1-mini/Qwen3-VL-Plus full-context 与 MIRIX/MMA 在 Text/Vision、四类逻辑和三步
  verdict/wager/reflection 下比较，grader 用 GPT-4o-mini，benchmark generation 还依赖 Qwen3-Max 与
  Qwen-Image-Plus。模型 snapshot、sampling 与 paired uncertainty 未披露。
- **What the Evidence Proves:** 在作者公开的三个 evaluation contracts 中，显式 source/time/neighbor features
  会改变 coverage、wrong-answer 与 abstention 行为；consensus 在 FEVER 三 seeds 上降低 variance，却在 sparse
  LoCoMo 降低 raw/multi-hop accuracy，说明 reliability component 需要按 evidence density 和 risk policy 选择，
  不是单向叠加。MMA-Bench 还证明“回答正确”和“因证据充分而回答/拒答”必须分开：baseline 的 Type-D 高分可由
  retrieval blindness/default Unknown 产生，reflection 也可能出现 correct→wrong false confession 或承认错误却不改 verdict。
- **What It Does Not Prove:** 该研究不证明 confidence 是 calibrated probability、静态 source prior 普遍正确、旧事实
  必然更不可信、semantic neighborhood 等于独立事实共识，或 raw image 普遍导致“Visual Placebo Effect”。它也不证明
  full MMA 整体优于 baseline：MMA-Bench Vision 的 overall CoRe 为 -0.16、core accuracy 13.55%，而 baseline
  为 0.35/32.67%；full MMA 在 LoCoMo 也更差。30 个 synthetic cases、两类固定 user reliability 与少量 API model
  只能支持诊断假设，不能建立跨域因果规律。后处理无法修复 retrieval miss，score 也不能替代 claim-source entailment。
- **Limitations / Threats to Validity:** static source prior 会固化 authority bias，并在 historically reliable source
  本次出错时反向伤害 Type-B；统一 exponential decay 混淆 record age、fact valid-time 与 volatility，timeless fact、
  delayed correction 或生效日在未来都可能被误判；semantic consensus 会把重复/相关错误当支持，也会压低稀疏但正确的
  multi-hop evidence。stored-neighbor confidence 还引入 update-order、cycle、stale-cache 与 poisoning amplification 风险。
  CoRe/utility 依赖 reward/penalty/wager policy；synthetic generation、LLM judge、固定 persona 与未披露 snapshots 会引入
  generator/judge leakage。作者明确承认 post-retrieval recall ceiling 与 sparsity-consensus trade-off。
- **Trade-offs / New Failure Modes:** 显式 filtering 用更低 coverage 换较少 overconfident error，也可能产生 false
  abstention、cognitive paralysis 与弱证据链丢失；可配置组件增加 domain tuning、calibration、recompute 和 audit 成本。
  source prior 可被伪造 identity、role drift 或 coordinated sources 利用；recency 可被 timestamp refresh gaming；consensus
  可被 duplication/Sybil/correlated misinformation 放大；visual evidence 能绕过 text-side caution；reflection prompt 又可能
  制造 false confession。若 threshold 与 action cost 未外置，模型会把 heuristic 分数误用成事实或权限判断。
- **Where the Previous Design Still Applies:** 单一 authoritative corpus、短生命周期 session、冲突稀少或高 recall 优先
  的 workload 仍适合简单 relevance/rerank；稀疏长对话中 `S+T` 可能优于 full consensus；高风险事实应保留
  authoritative source、typed supersession、人工验证和 deterministic policy，不应由 neighborhood voting 接管。Conformal/
  calibrated selective prediction、claim-level verifier 与 source-independent corroboration 是互补分支，不被 MMA heuristic 替代。
- **Evolution Relationship:** `Layering / Dependency`：similarity retrieval → post-retrieval evidence features → sufficiency/
  conflict gate → risk-aware answer/abstain policy。`Direct Evolution` 只适用于 memory read 从等权注入走向带 provenance、
  valid-time 与 reliability metadata 的选择；它不表示 heuristic scalar 取代 typed memory lifecycle。`Principle Reuse`：
  Evaluation 的 operating point、Reflection 的 false-correction check、RAG 的 sufficiency 与 Memory 的 supersession。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch72/73 映射已收敛为 Ch73 主 owner；已读 Ch71～74、
  Ch62 与 Ch76。Ch72 拥有 retrieval relevance/sufficiency 与 claim-evidence 边界，Ch62 拥有 risk/coverage、slice 与
  uncertainty，Ch76 拥有 reflection acceptance gate；它们只需短 handoff。Ch73 已覆盖 source、time、confidence、expiry、
  conflict、supersession、derived-state lineage 与 no-memory baseline，但尚未明确拆开“相关性、可靠性 feature、证据充分性、
  calibrated uncertainty、行动阈值”，也未说明 consensus 对 evidence density、independence 和 recomputation lifecycle 的依赖，
  因而存在窄而契合的 refine。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Experimental Memory-Evidence Reliability and
  Selective-Action Contract / Mechanism and Evidence Boundary Corrected / Human Gate Pending`。本轮只更新 Weekly，不修改
  Books。W08 Evidence Gate 与人工 Review 通过后，最多在 Ch73 `Memory Read` 与 `评估 Memory` 之间 refine 一段无产品名的
  机制：`relevance → reliability features → sufficiency → policy threshold`，同时保留 source calibration、fact valid-time、
  independent corroboration、confidence invalidation/recompute 与 risk/coverage evaluation；Ch72/62/76 只作短 handoff。
  不写 MMA 固定权重、作者 headline 或“视觉信息天然更不可信”。
- **Open Questions:** source reliability 如何从静态角色分数变成可校准、可撤销且防伪的 evidence；record time、event time、
  valid-from/to 与 volatility 怎样取代统一 half-life；怎样识别 source dependence、duplicate evidence、semantic contradiction 与
  Sybil consensus；neighbor confidence 的初始化、fixed-point/recompute、cycle 与 deletion propagation 如何定义；heuristic score
  怎样与 calibrated/conformal uncertainty、claim verifier 和 action cost 联合；MMA-Bench 能否以真实多用户、多模态、跨域、
  adversarial provenance 与 human-reviewed labels 重建，并发布 model snapshots、raw traces 与 paired uncertainty？

### Discovering Multiagent Learning Algorithms with Large Language Models

- **Candidate / Week / Score:** AlphaEvolve for MARL algorithms / 2026-W08 / 23/30；
  `Source Family ID: alphaevolve-marl-search-distillation-2026`。
- **Source Type / Date / Revision / Sources:** Google DeepMind 作者论文。arXiv v1 首发于 2026-02-18，v2 于
  2026-02-21 更新，二者都属于 W08；v2 修正实现细节并补充在另一组训练游戏上发现的 AOD-CFR。v3 于
  2026-05-07 才加入 18-game suite、系统 train/test ablation、WOP-CFR/PM-PSRO distillation、随机 normal-form
  games 与明确 limitations。v3 可用于 revision/evolution 核验，不能倒填为 2 月事件事实。论文 Appendix 公开
  search skeleton、prompts 与四个最终算法的 source listings，但未定位到作者官方 repository、release、完整
  AlphaEvolve program database、candidate history 或 experiment manifest。
- **Access and Verification Status / Full-read Coverage:** Verified at paper/revision level; artifact and search-run
  reproduction unavailable。已读 v1/v2/v3 metadata、Introduction、CFR/PSRO background、AlphaEvolve method、
  search space/objective、全部四个实验与 train/test protocol、逐组件 ablation、18-game Appendix、随机 NFG
  experiment、prompts、算法 code listings、Related Work、Conclusion 与 Limitations；并核对原 AlphaEvolve
  公开论文/Blog 的 workflow contract。公开材料没有披露 evolutionary generations/candidate count、LLM calls、
  token/compute cost、hardware、wall time、parallelism、失败 candidate 分布、完整 run seed、exact OpenSpiel/
  dependency commit 或独立 search trajectories，因此只能审计最终 artifact 与作者实验，不能重放搜索过程。
- **Original Problem / Why the Previous Design Was Reasonable:** CFR/PSRO 的 update rule、discount、averaging 与
  meta-solver schedule 过去主要由人根据理论和实验逐步设计。人工方案的优势是机制较小、可分析、容易形成
  convergence argument；在 evaluator 昂贵或反馈含噪时，研究者只比较少量候选也更节省预算。但可组合的
  update logic 很多，超参数搜索只改变数值，无法探索新的 state/control flow；LLM semantic mutation 因而被用作
  executable program proposal operator。旧方案不是失败，而是 search-space coverage 与分析成本之间的取舍。
- **Changed Constraint / Mechanism:** 系统先固定可修改接口和 evaluator，而不是让模型重写整个 solver。CFR
  暴露 regret accumulation、current-policy derivation 与 average-policy accumulation 三个 stateful component；PSRO
  暴露 train-time 与 evaluation-time meta-strategy solver。Gemini 2.5 Pro 接收 parent code、prior successful programs
  与 edit prompt，生成局部 source diff；candidate 在手选 proxy games 上执行，以固定迭代后的 exact negative
  exploitability 作为多项 fitness，合格程序进入 population。这里模型拥有 proposal，AlphaEvolve workflow 拥有
  parent/selection/evaluation；研究者拥有 search skeleton、训练游戏、fitness、seed program 与最终解释。
- **State Ownership / Control Flow / Data Flow:** `CFR+ or Uniform seed → program population → parent/context
  selection → LLM code diff → syntactic/runtime validation → OpenSpiel exact game-tree execution → per-game and mean
  fitness → population admission/selection`。VAD-CFR 的 persistent state 位于每个 information state 的 cumulative
  regret/policy 与 volatility/averaging schedule；SHOR-PSRO 则持有 population payoff tensor、train/eval meta-strategy
  state 与内部 iteration budget。v3 增加第二条控制流：`raw high-fitness program → component ablations on train/test
  games → identify necessary/generalizing mechanics → human-written minimal solver → comparative evaluation`。这一步
  不是 AlphaEvolve 自动完成，作者明确把它定义为 human-in-the-loop distillation。
- **Implementation Details:** 事件日 v1/v2 的 VAD-CFR 混合 EWMA volatility、自适应正负 regret discount、正 regret
  boost、optimistic nonlinear policy projection、前 500/1000 iterations 不累计 average policy 以及 magnitude-sensitive
  weighting；SHOR-PSRO 混合 optimistic regret matching、softmax pure-strategy bias、annealing/diversity、population-
  dependent inner budget，并让 train solver 返回 average、eval solver 返回 last iterate。v3 的逐项 audit 表明这些
  raw mechanisms 不是同等必要：WOP-CFR 只保留 extreme asymmetric discount、optimistic nonlinear prediction 与
  hard warm-start；PM-PSRO 则保留 tangent-projected utility + regret matching、随 population 增长的 inner budget 与
 统一 time-averaged solver。后者删除了 v1 强调的 hybrid blending、annealing 和 train/eval asymmetry。
- **Evaluation Contract:** v1/v2 在四个手选 training games 上搜索，并在同家族更大 test variants 中比较；公开主张
  基于 tabular imperfect-information games、CFR `K=1000`、PSRO `K=100`、exact payoff/exploitability 与 exact best
  response。v3 固定四个 training games、十四个 test games，共 18 个 OpenSpiel instances，信息状态从 2 到
  347,810；所有 solver deterministic，并以 full game-tree traversal 计算 metric。CFR baselines 包括 CFR/CFR+/
  LCFR/DCFR/PCFR+/DPCFR+/HS-PCFR+；PSRO 包括 Uniform、LP Nash（适用时）、AlphaRank、PRD 与 10^4-step RM。
  ablation 报告相对 raw candidate 的 per-game log-exploitability improvement，并以 central 50% IQM 聚合。v3 还在
  3～5 players、20～100 actions、Gaussian/Uniform payoff 的六组 constant-sum normal-form games 上各采样 1000
  games，使用 run-level 50,000 bootstrap。模型精度、训练 batch、生成长度和 deployment SLO 不适用于此 tabular
  evaluator；search hardware、LLM sampling、运行成本与 wall time 均 `Not Disclosed`。
- **What the Evidence Actually Proves:** 在作者公开的 exact tabular contract 中，LLM-guided code search至少产生了
  可执行、可与人工 baselines 比较的 raw solver candidates。更重要的是，v3 的同一作者 revision 提供了反证式证据：
  raw candidate 的显著复杂度可以提高 training fitness，却不是 generalization 的必要原因；删去 VAD 的 volatility
  或 SHOR 的 blending/annealing 后，test 结果可保持甚至改善。WOP-CFR 相对 raw VAD 的 Test IQM 为 +0.119，
  PM-PSRO 相对 raw SHOR 为 +0.059；这些数字只表示该 18-game、固定 horizon、log-improvement aggregation 下
  的相对结果。随机 NFG 扩展支持 PM/SHOR 在所测 constant-sum meta-games 上的稳定排序，但仍是 synthetic exact setting。
- **What It Does Not Prove:** v1 对“volatility-adaptive discounting 是收益原因”“hybrid blending/annealing 管理探索到
  exploitation”“train/eval asymmetry 让测量更准确”的机制叙述后来未被 v3 audit 保留，不能写成已证因果。
  论文没有证明自动发现优于人类研究流程、没有 convergence guarantee，也没有覆盖 deep CFR、neural oracle、
  stochastic RL、cooperative/general-sum environments、真实 Agent coordination 或生产 workload。单个 search trajectory
  不证明方法稳定；固定 `K` 的 exploitability 不证明渐近收敛、wall-clock efficiency 或大规模可扩展性。公开 source
  listings 也不等于完整 AlphaEvolve artifact。论文的“state-of-the-art/competitive”仅相对于列出的 tabular baselines。
- **Limitations / Threats to Validity:** v3 明确承认只有一次 AlphaEvolve trajectory、headline IQM 主要来自共享
  Poker/Goofspiel/Liar's Dice family 的 within-family generalization、distillation 依赖人工判断、无形式保证、最大 game
  小于 350K information states，且未与 deep/neural methods 比较。额外推断：v3 的 researchers 使用 Test IQM 来选择和
  评价 ablation/distilled core，因此这十四个 test games 已参与 mechanism development，不能再充当完全未触碰的 final
  holdout；仍需第三套独立 suite 或 external replication。搜索预算、candidate multiplicity 与 failed runs 未披露，也无法
  量化 selection bias/multiple comparisons。exact exhaustive evaluator 消除了采样噪声，却同时把结论限制在可枚举 game tree。
- **Trade-offs / New Failure Modes:** semantic program mutation扩大 search space，但增加 invalid code、hidden state、
  accidental complexity、objective gaming 与无法解释的 mechanism coupling；强 exact evaluator 提供低噪声 selection，
  代价是局限于小型 tabular domains。raw candidate 可能利用 training-game quirks，distillation 降低复杂度和 audit cost，
  却重新引入研究者主观选择、test-set reuse 与遗漏 synergistic mechanism 的风险。把 train/eval solver 同时纳入可变 artifact
  还会混淆“生成更好的 population”和“从既有 population 选择更低 exploitability distribution”；必须把 solver semantics、
  final metric 与 independent evaluator 固定并版本化。搜索出的 update rule 若直接部署，还会新增 numerical stability、
  adversarial game、runtime budget 与 rollback failure mode。
- **Where the Previous Design Still Applies:** 有形式保证需求、evaluator 不完整、实验代价高或副作用不可逆时，人工从
  小型机制族推导并证明仍更合理；超参数/有限结构搜索在 search space 可解释时成本更低。CFR+/DCFR/PCFR+ 等旧方案
  仍拥有更清楚的理论和工程边界；raw VAD/SHOR 也不是因 v3 出现便被否定，它们仍是 discovery artifact 与 candidate-
  interaction evidence，但不应在缺少复现和理论时替代 simpler solver。自动搜索更适合作为 proposal generator，而不是
  deployment authority 或 scientific conclusion owner。
- **Evolution Relationship:** `Direct Evolution`：manual update-rule design → constrained program search with executable
  fitness → raw high-fitness artifact → cross-distribution component audit → minimal human-distilled mechanism → independent
  final validation。`Layering / Dependency`：LLM mutation 位于 Workflow 的 evaluator/program-database/selection 之内；
  Ch62 的 EvalSpec 和 held-out authority 位于搜索结果之上。`Explanatory Analogy` 而非同一对象：MARL game solver
  研究多个策略主体的 equilibrium，不等于 Ch78 部署多个 LLM Agent 的责任/通信 topology。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch29/76/79 映射不成立，已读 Ch29、Ch62、Ch76～79。
  Ch29 拥有 GRPO/reward interface，不拥有外部程序搜索；Ch76 是单次 inference-time reflection；Ch78 是 deployed
  Multi-Agent coordination；Ch79 是 protocol integration。Ch77 已完整覆盖 original AlphaEvolve 的
  `human evaluator → LLM diff → sandbox → program database/lineage → selection → held-out/human decision`，主 owner
  因而收敛为 Ch77；现有正文已经覆盖 evaluator gaming、search-level overfit 与 artifact population，不需要重复论文
  algorithm。真正缺口是 raw search result 与长期 mechanism 之间还需要 `ablation/distillation/independent final holdout`
  的 evidence gate；Ch62 只需短 handoff，Ch78 只保留边界。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Experimental Search-to-Distillation and
  Independent-Validation Contract / Revision and Owner Corrected / Human Gate Pending`。本轮只更新 Weekly，不修改 Books。
  W08 Evidence Gate 与人工 Review 通过后，最多在 Ch77 的 AlphaEvolve 段后加入无算法名的演进链：高 fitness artifact
  先冻结 → development/test component ablation → mechanism distillation → untouched final holdout/external replication；
  明确 test 一旦参与 distillation 就已成为 development evidence。Ch62 加一句 evaluation ownership handoff；不向 Ch29/
  Ch76/Ch78/Ch79 写 CFR/PSRO 细节，不保留作者排名数字。
- **Open Questions:** 是否能公开 exact AlphaEvolve run、program population、失败 candidates、search seeds、LLM sampling、
  OpenSpiel commit 与 compute budget；独立重复 search 是否发现相同 core；怎样用 nested development/validation/final-test
  避免 ablation 反复观察 test set；如何把 empirical component necessity 转化为 convergence/stability analysis；在 stochastic
  deep RL、approximate oracle 与 general-sum/cooperative domains 中 evaluator noise、credit assignment 和 non-stationarity 会否
  破坏搜索信号；自动 distillation 能否在不隐藏 researcher choice 的前提下产生 typed evidence graph？

### Unified Latents

- **Candidate / Week / Score:** Unified Latents / 2026-W08 / 18/30；
  `Source Family ID: unified-latents-rate-distortion-compute-2026`。
- **Source Type / Date / Revision / Sources:** Google DeepMind 作者论文，arXiv 只有 v1，首发于 2026-02-19。
  arXiv 没有 HTML，已读取 17 页 PDF；未定位到 Google Research/DeepMind 独立发布页、作者官方 repository、
  checkpoint、config、dataset manifest 或 release。论文注明核心实验最初于 2025 年 3 月完成，但公开事件仍按
  arXiv 首发归入 W08，不能回填到 2025。
- **Access and Verification Status / Full-read Coverage:** Verified at paper level; artifact/reproduction unavailable。
  已读 metadata、Introduction、VAE/diffusion background、完整 ELBO/bitrate 推导、encoder/prior/decoder 两阶段
  training 与 sampling algorithms、Related Work、model architecture、metrics、ImageNet-512、internal text-to-image、
  latent bitrate/shape/L2 sweeps、Kinetics-600 video、四项 ablation、Limitations、Conclusion 与 single-stage Appendix。
  论文未披露 optimizer、learning rate、batch、hardware、precision、完整 step schedule、random seeds、uncertainty、
  data identity 或可复现代码，internal text/image/video datasets 也不可访问。
- **Original Problem / Why the Previous Design Was Reasonable:** Latent Diffusion 通过在压缩空间生成而降低 base-model
  compute。经典 VAE 用标准 Gaussian KL 与 channel/spatial bottleneck 限制 latent，但 decoder 没有精确 likelihood 时，
  KL weight 需要人工调节；pretrained semantic encoder 又会主动丢掉高频 detail。旧方案在目标是快速 decode、架构简单、
  现有 GAN/VAE artifact 可复用时仍很合理，问题是“latent 到底携带多少可建模信息”缺少显式 contract：重建越好通常
  代表 base model 要拟合更多 bits，过强 decoder 又可能产生 posterior collapse。
- **Changed Constraint / Mechanism:** 论文把 latent 设计从“固定 channel 数”改写为 rate–distortion–modeling problem。
  deterministic encoder 先产生 `z_clean`，再注入与 prior diffusion 最小噪声级一致的固定 Gaussian noise，形成 `z0`；
  diffusion prior 用未重加权 ELBO 估计并正则化 latent distribution，使 loss 成为 latent information 的 tight upper bound；
  diffusion decoder 在 image/video space 条件于 `z0` 重建，并用 sigmoid-reweighted ELBO 与 loss factor 决定哪些信息留在
  latent、哪些交给 decoder。loss factor/bias 因而成为 information-rate knob，而不仅是 reconstruction coefficient。
- **State Ownership / Control Flow / Data Flow:** Stage 1 为 `x → deterministic encoder → z_clean → fixed-noise z0`，
  latent diffusion prior 同时预测 `z_clean` 并把 gradient 传回 encoder，image-space diffusion decoder 则读取 `x_t + z0`
  重建 `x`；encoder、prior、decoder 联合优化。作者发现 ELBO-trained prior 的 sample quality 不足，Stage 2 冻结 encoder/
  decoder，用 sigmoid weighting 重新训练更大的 latent base model：`N(0,I) → latent diffusion → z0 → diffusion decoder → x`。
  这意味着“joint representation learning”最终仍是 two-stage lifecycle；paper-time base model 不是 Stage-1 prior 的直接复用。
- **Implementation Details:** 事件论文使用 ResNet encoder、8-block/1024-channel latent prior、两级 ViT base model，
  UVit diffusion decoder；ImageNet 输入 512×512，经 16× downsampling 得到 32×32 latent，latent channels 在 4～64
  sweep。默认 final latent log-SNR `lambda_z(0)=5`，对应约 `sigma=0.08` fixed noise；decoder loss factor 常在
  1.3～1.7。作者还测试 diffusion-prior + MSE decoder、normal-prior + diffusion decoder、learned encoder variance
  与 single-stage variants。single-stage 虽可稳定训练，但同配置 400K steps 的 FID 约 4，未达到 two-stage 路线。
- **Evaluation Contract:** ImageNet-512 使用 gFID 衡量 generation、rFID/PSNR 衡量 reconstruction、estimated
  bits per dimension/pixel 衡量 latent upper bound；作者用 linear/attention FLOPs ×3 近似 training cost，但 Figure 4
  明确排除 autoencoder training cost。text-to-image 在未公开 internal dataset 上训练 100/300/970-GFLOP base models，
  无 guidance 采样 30K，并相对 training-set statistics 计算 FID/CLIP。Kinetics-600 使用 16×128×128 videos、
  4×8×8 downsampling、condition 5 frames / generate 11 frames；部分 baselines 的 17-frame tokenization 通过从 FLOP
  计算中丢弃 extra token 作近似对齐。FID/FVD 数字没有 confidence interval 或多 seed，hardware/time/energy 未披露。
- **What the Evidence Actually Proves:** 在作者 ImageNet contract 中，fixed encoder noise + trainable diffusion prior
  gradient + diffusion decoder 的组合确实通过 ablation 显示为相互依赖：stop-gradient/normal-prior、近乎无噪 latent、
  learned variance 都劣于 baseline；loss-factor sweep 还直接显示 bitrate 增加改善 reconstruction，却使小 base model 的
  generation 变差，而 medium model 对 rate 更不敏感。它支持一个长期机制：**表示压缩率不能脱离下游 model capacity 与
  decoder expressiveness 选择**。更强 base model 能消费更多 latent information；减少 latent bits 可能只是把工作移给 decoder。
- **What It Does Not Prove:** 摘要的 ImageNet FID 1.4/Kinetics FVD 1.3 与“更少 training FLOPs”不能证明端到端
  system 更便宜，因为 headline cost 不含 autoencoder，inference/decode cost 也未计入。论文不证明 bitrate upper bound
  等于真实 entropy/code length，不证明结果适用于 text token、LLM hidden state、world-model planning 或 production image
  serving，也不证明 2026 全部 contemporaneous baselines 的统一 SOTA。internal-data text/video results 无法独立核验，
  FID/FVD 也不能单独证明语义、文本细节、temporal consistency 或用户质量。
- **Limitations / Threats to Validity:** 作者明确承认低信息 latent 可能只是把 modeling problem 推给更强 diffusion
  decoder；不同方法的 decoder class 与 autoencoder training data 不同，使 cross-paper comparison 混杂；diffusion decoder
  sampling 比 GAN decoder 贵一个数量级，未经 distillation 的 UL inference 明显更贵。额外边界包括 autoencoder cost 排除、
  FLOP 只统计 linear/attention、baseline extra-token adjustment、internal datasets、无 artifact/seeds/uncertainty，以及
  “为每个 experiment 选择最佳 bitrate”产生的 model-specific tuning。rFID 使用当前样本自身作为 reference distribution，
  还可能掩盖 instance-level detail loss，因此必须与 PSNR/visual task 联合解释。
- **Trade-offs / New Failure Modes:** 更低 rate 让 latent prior/base model 更易拟合，却丢失小文字与高频 detail，并把
  stochastic reconstruction 交给 decoder；更高 rate 改善 fidelity，却增加 base-model capacity/compute。fixed noise 提升
  stability和 rate 可解释性，代价是 posterior expressiveness 受限；learned variance 更灵活但论文中高 variance/不稳定。
  two-stage training 容易扩展 base model/batch，却新增 encoder/decoder freeze、latent-version binding、Stage-1/Stage-2
  distribution drift 与两套 diffusion sampling cost；single-stage 生命周期更简单，却在本实验显著劣化。强 decoder 也可能
  “看起来重建合理”而非保留原 instance 证据。
- **Where the Previous Design Still Applies:** Stable-Diffusion-style VAE/GAN decoder 在低 latency、已有 artifact、固定
  visual domain 或端到端成本优先时仍成立；semantic pretrained representations 适合 generation quality 高于 pixel fidelity
  的任务；discrete tokenizer 适合需要 codebook/interface identity 或快速 decoder 的场景；pixel diffusion 避免 latent
  mismatch，但承担更高 base-model compute。UL 是 rate-control 的一个实验分支，不是这些路线的普遍替代。
- **Evolution Relationship:** `Direct Evolution`（仅在 visual latent modeling 内）：channel/spatial bottleneck + heuristic
  KL → learned semantic/low-rate latents → prior-coupled measurable rate → base-model-capacity-aware rate tuning。
  `Layering / Dependency`：encoder rate、base-model modeling cost 与 decoder cost 三者联合决定 system optimum；不能只优化
  FID/FLOPs 中的一层。它与 LLM token embedding、Agent latent communication 或 world-model state 仅属
  `Explanatory Analogy`，不能共享实现结论。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch18 映射错误；已读 ROADMAP、Ch4～6、Ch10、Ch12、
  Ch17～20。Ch18 是 causal Decoder-only，Ch19/20 是 KV Cache/Sampling，均不拥有 VAE/diffusion representation；
  Ch12 是 discrete token embedding，也不能承载 visual compression。Ch5 已有“表示为目标服务、过强 invariance 会丢信息”
  的上位原则，但没有 Diffusion/VAE 数学与生成系统边界；把 UL 细节插入会把 Part I 的通用论证变成孤立 vision case。
  当前 80 章不存在 direct owner，这是结构覆盖 gap，不应通过误塞章节掩盖。
- **Integration Decision / Changed Files:** `Weekly Only — Below 20 / No Direct ROADMAP Owner / Full Review Complete`。
  本轮不修改 Books，也不因一篇 18 分论文新增 Part/章节。若未来多个高质量 sources 共同形成“generative representation
  contract”演进链，再由人工决定是否在 Part II 新增跨模态 representation owner；届时可吸收无产品名的
  `rate ↔ reconstruction ↔ downstream model capacity ↔ decoder/inference cost`，而不是论文 headline。
- **Open Questions:** tight upper bound 与真实 entropy coding/传输 bytes 的差距多大；包含 autoencoder training、latent
  base model、diffusion decode、distillation 与 serving latency 后的 end-to-end Pareto 是否仍领先；不同 base-model capacity
  的 optimal rate 能否形成稳定 scaling law；真实 OCR/identity/motion preservation 是否随低 rate 退化；公开 data/code/
  hardware/multi-seed 后 headline 是否可复现；未来 ROADMAP 是否应在多来源成熟后增加 generative representation owner？

### DDiT / Dynamic Patch Scheduling for Efficient Diffusion Transformers

- **Candidate / Week / Score:** DDiT / 2026-W08 / 21/30；
  `Source Family ID: ddit-dynamic-patch-diffusion-inference-2026`。
- **Source Type / Date / Revision / Sources:** Amazon/BU 作者论文与官方项目页。arXiv 只有 v1，首发于
  2026-02-19；已读取 13 页 PDF、HTML 与 submission metadata。当前项目页将工作标为 CVPR 2026 Highlight，
  但没有 code、checkpoint、config、training log 或 benchmark harness 链接；后续 venue 状态只用于 source-family
  核验，不改变 W08 的首次公开日期。
- **Access and Verification Status / Full-read Coverage:** Verified at paper/project-page level; artifact and reproduction
  unavailable。已读 Introduction、Related Work、DiT/patch preliminaries、patch-specific embedding/de-embedding、
  LoRA/distillation、三阶 finite-difference scheduler、percentile aggregation、全部 image/video tables、user study、
  order/threshold analysis、Conclusion 与全文 References。论文提及“Additional results are in Appendix”，但公开的
  13 页版本在 Conclusion 后直接进入 References，没有可供复核的 Appendix；也未披露 hardware、precision、batch、
  training steps/epochs、训练时间、random seeds、metric uncertainty、scheduler overhead 或 code revision。
- **Original Problem / Why the Previous Design Was Reasonable:** DiT 把 VAE latent 固定切成 `p×p` patches；token 数
  `N=HW/p²`，self-attention 的 pairwise 部分随 `N²` 增长。固定细 patch 在所有 denoising timesteps 上保留统一
  spatial fidelity、shape 与 kernel contract，最容易复用 pretrained model、batch 和 compiled executable；代价是即使
  某些 timesteps/outputs 只需粗粒度结构，也支付完整 token compute。固定粗 patch、减少 denoising steps、cache、
  pruning 与 quantization 各自降低不同成本，但可能静态丢掉细节或需要另一套 quality contract。
- **Changed Constraint / Mechanism:** 论文把“每一步使用同一 token granularity”改为 trajectory-conditioned choice。
  为 `p_new∈{p,2p,4p}` 增加 patch-specific embedding/de-embedding、插值 positional embedding 与 patch-size id，
  冻结 base model，在每个 Transformer block 的 FFN 加 rank-32 LoRA 和一个 residual block；coarse-patch branch 用
  fine-patch frozen teacher 的 noise prediction 做 L2 distillation。运行时保留最近 latent states，计算一、二、三阶
  finite difference，再按 candidate patch 切块、计算块内变化的标准差，以 `ρ` percentile 聚合；若聚合值低于阈值
  `τ`，选择满足条件的最大 patch，否则回到最小 patch。每个 timestep 全图只使用一个 patch size，尚不支持同一步
  内的 spatially heterogeneous patches。
- **State Ownership / Control Flow / Data Flow:** 静态 artifact 拥有 base weights、不同 patch-size 的 embedding/
  de-embedding、LoRA、residual block 与 patch-size id；单次 generation trajectory 拥有 latent history、当前 timestep、
  `Δ³z`、per-patch variance、`ρ/τ` 与被选 patch size。控制流是 `recent latents → finite differences → per-candidate
  spatial statistics → threshold choice → patchify → DiT+LoRA → de-patchify → next latent`。因此这是 model-internal
  adaptive-compute state，不是 request admission、Continuous Batching、KV ownership 或 cluster placement state。
- **Implementation Details:** T2I 以 FLUX-1.dev 为 base，支持 `2p/4p`，在 base 生成的 T2I-2M synthetic data 上
  fine-tune，使用 Prodigy、learning rate 1.0；T2V 以 Wan-2.1 1.3B 为 base，在 base 生成且 prompts 来自
  Vchitect-T2V-Dataverse 的 synthetic videos 上训练，使用 AdamW、learning rate `1e-4`。patch-embedding 用
  bilinear-interpolation projection 的 pseudo-inverse 初始化。主实验写 `τ=0.001, ρ=0.4`，但没有报告这两个
  hyperparameters 的独立 validation split、跨 dataset calibration 或 `ρ` ablation。
- **Evaluation Contract:** T2I 为 1024×1024、50 steps、guidance 3.5；Table 1 报 FLUX baseline 12.0 s/image、
  DDiT 5.5 s/image，并在 COCO/DrawBench/PartiPrompts 上使用 FID、CLIP、ImageReward，以及相对 base output 的
  SSIM/LPIPS。T2V 为 Wan-2.1 1.3B、480×832、81 frames、50 steps，用 VBench。比较对象包括减少 steps、
  TeaCache 与 TaylorSeer；还比较 finite-difference order 和 `τ`。但是 seconds/image 与 speedup 没有绑定 GPU、
  runtime、precision、batch/concurrency、warmup、compile/cache state 或 SLO；论文也没有给出 training/adapter cost，
  所以这些数字只属于作者未完整披露的 offline single-generation contract。
- **What the Evidence Actually Proves:** 在作者两个 base-model contracts 下，加入可训练 multi-patch branches 后，
  trajectory-dependent patch choice 能在所列 perceptual metrics 上形成 quality–compute trade-off；固定使用更大 patch
  将 token 数从 4096 降到 1024/256，作者的测量也显示单图时间下降。order ablation 显示作者的 third-difference
  proxy 在该 T2I setting 上优于一、二阶版本。这支持的长期机制是：**iterative generative process 的不同阶段不一定
  需要同一表示粒度，adaptive granularity 可以把 compute budget 变成显式 policy。**它不证明“三阶变化等于语义
  complexity”，只证明该 proxy 在有限实验中与作者 metrics 相关。
- **What It Does Not Prove:** “test-time / training-free”只适用于 patch-selection rule；整个系统必须训练新的
  patch modules 与 LoRA，不能直接作用于任意 off-the-shelf DiT。两种 model family 不足以证明适用于“any DiT”，
  也不证明 long-video、不同 sampler/step count/resolution、real training data 或 production batching 下仍成立。
  FID/CLIP/ImageReward/VBench 不证明文字、identity、fine motion 或最坏样本不退化；SSIM/LPIPS 对 base sample 的
  接近也不等于真实质量。论文没有固定 seed pairing、confidence interval 或完整 human-study protocol，不能从
  `61% tie / 22% baseline / 17% DDiT` 推出总体用户无差异。
- **Internal Consistency / Reproduction Boundary:** Equation 5 与文字都意味着提高 `τ` 会让更多 candidate 满足
  `<τ`、更早选择 coarse patch。Table 4 的 `τ=0.004 → 1.88×`、`τ=0.001 → 2.18×` 却与这一单调关系相反，
  `τ=0.01 → 3.52×` 又恢复预期方向；Wan Table 2 的 0.004/0.001 也同样反序。并且摘要的 T2I 3.52×在 Table 1
  来自 DDiT+TeaCache，而 Table 4 又把 3.52×写成 DDiT `τ=0.01`，对应的 quality metrics 也不同。没有 code/logs
  无法判断是 table label、threshold semantics、workload sampling 还是配置记录错误，因此精确 control curve 与
  headline speedup 均不能进入 Books。
- **Limitations / Threats to Validity:** 公开正文没有 architecture-component ablation，无法分离 patch embedding、
  LoRA、residual、distillation、percentile aggregation 与 dynamic scheduler 的因果贡献；没有与固定 coarse/fine、
  hand-written timestep schedule 或同 training budget 的 adaptive-token baseline 做完整对照。`ρ/τ` 在测试数据上的
  tuning lineage 未披露，synthetic teacher-generated training data 还可能让 student 特别贴合 base output。三阶差分
  需要历史 latent 与额外 statistics，但其 memory/kernel overhead 未测；user study 的参与者、pair 数、sampling、
  agreement 与 significance 均未披露。
- **Trade-offs / New Failure Modes:** coarse patch 以更少 tokens 换 compute，却可能不可逆丢失局部 detail；fine patch
  保留 fidelity，却维持原成本。dynamic policy 可按 trajectory 适应，但新增 threshold calibration、history state、
  shape switching、多个 artifact branches 与分布漂移。作者每一步全图统一 shape，利于单请求 kernel；若未来同一步
  局部 patch size 不同，会新增 ragged layout、load imbalance 与 kernel complexity。跨请求部署时，不同请求在同一
  timestep 选择不同 token shapes，还可能破坏 homogeneous batching、graph capture 与 kernel reuse；这一 serving
  后果是由机制推导的工程风险，不是论文已验证结果。
- **Where the Previous Design Still Applies:** fixed fine patch 在 deterministic shape、simple deployment、worst-case
  detail retention、batching/compilation stability 或无 adaptation data 时仍合理；static coarse patch/step reduction 在
  latency budget 固定且可接受质量退化时更易验证；cache/quantization 优化不同成本层，也可与 patch policy 组合，
  但组合收益不能相加假设。DDiT 是 adaptive granularity 的实验分支，不是固定 tokenization 的普遍替代。
- **Evolution Relationship:** `Direct Evolution`（仅在 DiT inference family 内）：fixed patch each timestep → manually
  reduced/static token compute → learned multi-patch artifact → trajectory-conditioned global patch schedule → future
  within-step regional granularity。`Layering / Dependency`：model artifact 先获得 multi-shape semantics，runtime policy
  才能安全选择 shape；training-free scheduler 不等于 training-free system。它与 LLM scheduling 仅是“先定义执行对象、
  再分配 budget”的 `Principle Reuse`，不能共享 state machine 或 benchmark。
- **ROADMAP / Chapters Read / Existing Coverage:** 初始 Ch42/45 映射错误；已读 ROADMAP、Ch17、Ch18、Ch38、
  Ch42、Ch45 与 Ch52。Ch17 只拥有通用 Transformer Layer，Ch18/38～52 明确围绕 decoder-only LLM、token-generation
  process、KV 与 Serving；Ch42 调度跨 request 的 iteration membership，Ch45 映射 LLM graph/kernel，Ch52 调度带
  request/KV state 的 token work。DDiT 的 owner 应是尚不存在的 diffusion model/inference node。把它塞进这些章节会
  混淆 model-internal denoising step、patch token 与 LLM request token，是与 Unified Latents 同属 generative-system
  coverage gap 的第二个信号，但单周两篇仍不足以擅自扩章。
- **Integration Decision / Changed Files:** `Weekly Only — No Direct ROADMAP Owner / Experimental Evidence Contract /
  Owner and Evidence Boundary Corrected / Full Review Complete`。本轮不修改 Books 或 ROADMAP。未来若多个 primary
  sources 共同形成 diffusion representation、denoising runtime、batching 和 SLO 的稳定演进链，再由人工决定是否新增
  owner；届时可吸收“artifact shape capability 与 runtime shape policy 必须分离、adaptive compute 会把单请求收益转化为
  batching/compile trade-off”这一长期机制，不复制 3.52× headline。
- **Open Questions:** 阈值表的反序与两个 3.52× contract 如何解释；hardware/precision/batch/runtime 固定后速度是否
  可复现；patch-module training cost 与 scheduler overhead 多大；`ρ/τ` 能否在 untouched validation 上校准并跨 sampler/
  resolution/model 迁移；paired seeds、rare-detail/OCR/identity/motion 与完整 user study 是否仍支持质量不退化；多请求
  heterogeneous shapes 如何 bucket/rebatch、维护 graph cache 与兑现 tail SLO？

### 2Mamba2Furious / Higher-Order Recurrent Attention State

- **Candidate / Week / Score:** 2Mamba2Furious / 2026-W08 / 22/30；
  `Source Family ID: 2mamba-higher-order-recurrent-attention-2026`。
- **Source Type / Date / Revision / Sources:** 作者论文、官方实验仓库、Hugging Face checkpoint collection 与
  独立 custom Triton Kronecker kernel 仓库。arXiv v1 首发于 2026-02-19，v2 为 2026-04-02，v3 为
  2026-05-15；W08 事件只使用 v1，v3 只用于核验 later revision。v3 新增逐 token inference algorithm、
  checkpoint 链接并澄清部分公式；当前主仓库无 release/tag，且现有 README、模型和 commit 可能晚于
  event date，不能反写成 2 月 19 日已具备的 artifact contract。
- **Access and Verification Status / Full-read Coverage:** Verified at paper/current-artifact level; event-time code
  snapshot unavailable。已读 v1 与 v3 的 Abstract、Introduction、Background、Mamba-2 decomposition、全部
  ablation、Mamba-2S、2Mamba/2Mamba-E 方法、复杂度与 state-memory 推导、NIAH、Conclusion、inference
  algorithm、model setup、gradient Appendix、Pile/SlimPajama Appendix；并联读当前训练/推理入口、实验参数、
  checkpoint 说明、NIAH 脚本说明和 custom kernel。没有公开 production inference benchmark、优化后端比较、
  seed-level loss、置信区间、完整 checkpoint lineage 或 event-time commit；公开 W&B 入口存在，但没有冻结成
  与论文表格一一对应的 immutable artifact。
- **Original Problem / Why the Previous Design Was Reasonable:** exact causal softmax Attention 保留逐 token
  content addressability，训练时 pairwise compute 随 `N²` 增长，Decode 则持有随历史长度 `N` 线性增长的
  KV Cache。FlashAttention 改善 IO 而保留 exact semantics；GQA/MQA 减少 KV heads；它们在 kernel 成熟、
  精确 retrieval、短中 context 与可解释 cache lifecycle 上仍合理。first-order linear Attention/SSM 将历史压入
  固定 recurrent state，训练可用 associative scan 随 `N` 线性扩展，Decode state 不随 `N` 增长，但有限 feature
  map 往往牺牲表达力。Mamba-2 再加入 input-dependent decay、convolution、gate、normalization 与 discretization，
  代价是很难知道收益来自哪项机制。
- **Changed Constraint / Mamba-2S Mechanism:** 论文先把 Mamba-2 当成“带 decay mask 的 linear Attention”而非
  只用 SSM 术语，并在约 300M Llama-2-style 模型上逐项移除 activation、`A` mask、short convolution、`D`
  residual、`Z` gate、normalization 与 value discretization。作者实验支持 softplus-negative decay mask 和短
  convolution 是该 contract 下的主要贡献，于是构造 Mamba-2S：保留 softplus `A` mask、kernel-size-2
  convolution、value discretization 与 output normalization，移除多项额外 bias。value discretization 在部分
  300M run 有益，却使 700M squared variant 不稳定，因此最终 2Mamba 不保留它，并将 output normalization
  换成二阶 feature 上的 softmax-like normalization。这是受限 ablation，不证明被移除组件在其他规模、
  optimizer、data 或 kernel 中普遍无用。
- **2Mamba Mechanism / State Ownership:** 2Mamba 将 `QKᵀ` 的 inner product 平方，再用 decay/causal mask 与
  softmax-like denominator 归一化；平方可视为 exponential kernel 的二阶 Maclaurin feature，增加 fixed-state
  expressiveness，并让 feature image 非负。v3 的 recurrent inference 不保存全部 token KV，而为每个 layer/head
  持有两组 request-owned state：numerator `H_up [D,d_h]` 与 denominator `H_down [D]`，其中
  `D=d_h(d_h+1)/2` 利用对称二阶项去重；另保存 convolution window 所需的上一时刻 Q/K/V。每步先计算
  `a_t=exp(-softplus(h_t W_A))`，衰减旧 state，再写入二阶 `k_t` feature 与 `v_t`，最后用二阶 `q_t` feature
  读取 numerator/denominator。状态量对 sequence length 是 `O(1)`，却约为
  `d_h(d_h+1)^2/2 + 3d_h` elements/head，即随 head dimension 近似立方增长；“constant memory”只能解释为
  对 `N` 固定，不能解释为对 model、heads、layers、batch 或 concurrency 固定。
- **Control Flow / Data Flow / Kernel Boundary:** 训练公式可写成 `N×N` matrix 便于说明 semantics，但 causal
  linear-time execution 依赖 scan/recurrent reordering 和专用 kernels。二阶 feature 还需要 symmetric
  Kronecker product；作者另建的 Triton repo 只有少量 commits，README 明示它是临时实现，不应被视为成熟
  backend。当前主仓库的 inference script 也明确“不 really optimized”，作者把 kernels 称为 proof of concept。
  因此算法对 `N` 的渐进复杂度、raw state crossover、可训练性与 production latency/throughput 是四个不同
  claim；论文没有证明高阶 state 在真实 serving 中优于 FlashAttention/KV Cache。
- **2Mamba-E Is a Different Branch:** 2Mamba-E 将 inner product 指数化，本质可重写为带 softplus forgetting
  mask 与 input convolution 的 softmax Attention；作者在约 700M loss curves 中观察到它略优于 softmax。
  但 exponential 不再能用有限二阶 recurrent state 精确分解，因而重新需要随 `N` 增长的 KV Cache。
  它是 `softmax + learned forgetting` 分支，不是 2Mamba 固定状态优势的无代价增强。将 2Mamba-E 的 loss
  结果用来证明 2Mamba 同时具有更高准确率与 constant memory，会把两个互斥 contract 拼成一个 headline。
- **Implementation / Evaluation Contract:** 主实验使用 FineWeb `CC-MAIN-2024-51`，0.1% held-out test、
  seed 123，Llama-2 tokenizer/backbone；small 约 300M（hidden 1024、16 heads、`d_h=64`、20 layers），
  medium 约 700M（hidden 1536、24 heads、`d_h=64`、27 layers）。AdamW `β=(0.9,0.999)`、global batch 32、
  LR `1e-4`、10K warmup、weight decay 0.01、无 gradient clipping；2048/4096/8192 contexts。论文报告
  100K training steps，却因 evaluation off-by-one bug 只比较到 90K，并明确没有重跑。当前 README 说明
  AMP 使用 bfloat16，多数 run 为两张 80GB A100，medium 8192 run 为 16 GPUs；通常不超过两天，400K
  NIAH run 约一周。README 的 scheduler `num_steps=1,000,000` 与 `early_stop=100,000`、`9182` typo 和覆盖式
  checkpoint 保存进一步说明 reproduction 必须固定 config/commit，不能只依据论文表述。
- **Memory and Long-Context Evidence:** 作者比较每 head raw state，得到 softmax KV `2Nd_h` 与 2Mamba
  `d_h(d_h+1)^2/2+3d_h` 的理论 crossover；`d_h=64` 时约为 `N>1058`。这只比较 state elements，不含
  weights、activations、workspace、allocator、layout、replication、kernel scratch 或 multi-request fragmentation，
  也没有把更大的 per-step state update compute 纳入 SLO。NIAH 使用 batch 64、8192-token training 的 400K
  checkpoint，却在 Nanotron benchmark 上按约 1024～16384 **characters** 构造输入；公开 artifact 说明只从
  约 12K rows 中 seeded 抽取 1000 条、因 memory 删除 16K-character case、用 one-shot maximum likelihood，
  并把结果 hardcode 成 heatmap。作者本人要求在得出 context-usage 结论前继续研究，因此它不能证明
  arbitrary-token recall、跨任务 effective context 或 production long-context capability。
- **What the Evidence Proves / Does Not Prove:** 证据支持三点：在指定 300M/700M training contract 中，
  Mamba-2 的 decay+short-convolution 是值得保留的强组件；二阶 feature 提供一条在表达力与固定 recurrent
  state 大小之间调节的机制；2Mamba 与 2Mamba-E 揭示“逼近 softmax”会沿 state capacity 或恢复 KV Cache
  付费。它不证明 2Mamba 在大模型、下游任务、等 compute/token、等 wall-clock 或 production serving 上达到
  softmax parity；不证明 `N>1058` 即有端到端 memory/latency 收益；不证明 NIAH 等于通用 long-context；也不
  证明 Mamba-2 被移除组件普遍无效。作者的 `competitive in accuracy` 与 `efficient in practice` 必须限定为
  paper-scale loss/raw-state evidence，不得写成通用事实。
- **Trade-offs / New Failure Modes:** 相比 softmax，2Mamba 用有损 fixed state 降低随 `N` 增长的 cache，
  但二阶 state 随 `d_h³` 增长，增加 HBM 常驻量、update FLOPs、数值动态范围、custom-kernel 依赖、checkpoint/
  migration 负担和每 request/layer/head 的 reset/rollback/isolation 语义。decay 会主动遗忘，state 又不能逐 token
  精确删除、引用或恢复 provenance；一个错误 token 的影响可能被压进后续 state。2Mamba-E 恢复 exact
  softmax-like content addressing，却也恢复 KV lifecycle。Hybrid Attention/SSM 可在不同 layers 保留两类路径，
  但新增双重 state、kernel、batching 与 observability contract。
- **Where the Previous Design Still Applies / Evolution Relationship:** `Direct Evolution`：softmax + growing KV →
  first-order linear/recurrent state → gated/decayed Mamba-2 → ablation-derived Mamba-2S → second-order 2Mamba。
  `Branching Evolution`：2Mamba-E 回到 softmax + forgetting gate，并放弃 fixed-state contract。exact softmax 在
  kernel maturity、精确 retrieval、短中 context、token-level provenance 与可管理 KV state 时仍合理；first-order
  Mamba/linear Attention 在更小 state、较低 constant 和可接受质量损失时仍合理；2Mamba 是容量更大的实验性
  fixed-state branch，而非前两者的必然替代。
- **ROADMAP / Chapters Read / Existing Coverage:** 已读 ROADMAP、Ch14、Ch15、Ch17、Ch19、Ch22 及相邻
  Part II 边界。Ch14 定义 dense softmax semantics，Ch19 定义 KV state 随 `T` 增长和 request lifecycle；两章应
  保持基础推导，不由单篇论文改写。Ch22 已拥有 `dense softmax → linear/recurrent state → hybrid → learned sparse`
  及“bounded KV / external archive / latent recurrent state”演进线，因而是唯一主 owner。现有正文已经陈述固定
  state 是有损压缩，却没有显式写出“提高 recurrent feature order 会用 `d_h` 维度成本换表达力”及
  “恢复 exponential expressiveness 会恢复 KV”这一双向边界；这是候选可 refine 的真实缺口，不是新增章节理由。
- **Integration Decision / Changed Files:** `Refine — Existing Argument / Experimental Higher-Order State Contract /
  Revision, Evaluation and Kernel Boundary Corrected / Human Gate Pending`。本轮只更新 Weekly，不修改 Books、
  ROADMAP、Learning State 或 Git index。人工 Gate 通过后，最多在 Ch22 的线性/递归路线中 refine 一段长期
  机制，并向 Ch19 做短 handoff；不复制论文名、loss headline、1058 阈值或 checkpoint 版本。
- **Open Questions:** 等参数、等 token、等 wall-clock、等 optimizer 与多 seeds 下二阶 feature 的独立增益多大；
  `d_h`、heads、layers、batch 与 context 分布改变后真实 crossover 在哪里；优化 kernel 后 TPOT、TTFT、goodput、
  power 与 tail SLO 是否优于 FlashAttention/GQA；state 如何 checkpoint、migrate、rollback、reset、隔离与校验；
  decay 遗忘和不可逐 token 删除如何与 provenance/privacy 兼容；NIAH 在完整 12K rows、token-length slices、
  multi-evidence/干扰任务与独立 harness 中是否仍成立；v3 Algorithm 6 的 `y_N/y_t` notation 与 checkpoint 标注
  能否由作者澄清？

## Evidence Level

原两项 Source Review 仍成立：真实使用 telemetry 具有生态有效性但受产品用户与采样方法限制，
First Proof 是公开 artifact 而不是总体研究能力估计。MapTrace 已完成官方来源、日期、artifact 与
低分拒绝核验；其 Google Blog 明示 critic 仍有 false positive，且领域数据机制不足以改变当前
AI System 主干。GLM-5 已达到全文 Source Review，但其公开代码不足以复现完整训练系统；Agent
Reliability 已完成 v1→v3 revision audit，核心 reliability profile 成立，但 v1 outcome-consistency
公式错误使原数值不得无版本引用。ResearchGym 已完成 v1、Appendix 与当前官方 artifact 联读；其
长期价值是把 result validity、semantic progress 与 environment integrity 分开，而不是单次 SOTA headline。
CUWM 已完成论文与 GUI-360 data lineage 联读；其证据只支持离线 single-step consequence reranking，
不支持多步真实执行或 safety claim。PAHF 已完成论文、证明和当前官方 artifact 联读；其双反馈机制只在
persona simulation 与理想化 regret assumptions 下成立，当前仓库也不是可追溯的 paper-time snapshot。
Calibrate-Then-Act 已完成 v1→v3、证明、sensitivity、significance 与当前官方 artifact 联读；其证据只支持
受控低维任务中的 uncertainty/cost-conditioned exploration，不能证明真实 Agent 的全局最优策略。
Human Interaction in Web Agents 已完成 v1→v4、模型卡与当前 PlowPilot 联读；其真实用户轨迹支持
control-transfer 是独立系统对象，但小 cohort、trajectory-level split、低 intervention recall 与非随机 user
study 不支持把 classifier 当 approval authority。Frontier AI Risk Management v1.5 已完成五个风险族、方法、
metrics、mitigation、limitations 与 related artifact 联读；它支持 per-risk EvalSpec 和 stateful executable evaluation，
不支持统一模型风险排行，也不支持把同集群受指令创建 Deployment 外推为自然跨环境复制。其长期机制已进入 Ch66。
OpenClaw trajectory audit 已完成 PDF、六份 seed JSON 与当前官方 docs 联读；它证明 unrestricted tool environment 中
trajectory evidence 的必要性，但 artifact 标注冲突、runtime 未固定、单模型单次运行与无 raw logs 使 58.9% headline
不能作为产品或模型安全率。Magma 已完成算法、理论、四组实验与 Appendix 联读；其证据支持
landscape-dependent stochastic update masking，不支持通信/显存加速，也不能把 uniform+damping 的收益归因给
alignment sampling。TAROT 已完成论文、全量实验表与当前官方 artifact 联读；其 tiered curriculum
观察成立于受限 Python RFT contract，但 capability selector 未被操作化，当前 reward comparator 与
版本 lineage 也不足以把开源 artifact 当作严格复现。Vision Wormhole 已完成 v1、v2 revision 与当前官方
代码联读；证据支持 VLM image span 上的实验性异构 latent channel 和 O(N) adapter integration，不支持
runtime O(N)、普遍 accuracy parity 或以不可读 latent buffer 替代 authoritative state。DreamZero 已完成唯一
v1、全部 Appendix、项目页与当前官方 artifact 联读；证据支持指定机器人 contract 中的 joint world/action
prediction、actual-observation replacement 与 action-window-aware asynchronous execution，不支持把 visual
plausibility 当 causal world model、把作者 2x/38x/7Hz headline 外推到其他 workload，也不支持把当前开源路径
当作 paper-time optimized artifact。In-context co-player inference 已完成唯一 v1、PPI/A2C 实现、全部
ablation 与 equilibrium proof 联读；证据只支持 100-round IPD、指定 mixed pool 和小型 GRU 中的 partner
inference/shaping mechanism，不证明 diversity、in-context learning 或 self-interest 在开放 Agent 环境会自然导向
合作。REFINE 已完成唯一 v1、全部实验/Appendix 与官方 artifact 边界复核；证据支持两个小型 fast-weight
model 在 16K contract 中从 selected multi-token feedback 受益，但不证明 NTP 普遍失效、GRPO naming 完全等价、
TTT 可直接生产化或替代数据可严格复现。MMA 已完成唯一 v1、全部 benchmark/ablation 与官方代码联读；
证据支持将 post-retrieval reliability 与 risk-aware abstention 设为独立系统层，也直接暴露 consensus 在 dense conflict 与
sparse multi-hop 中方向相反的 trade-off；它不证明静态 source prior、统一 recency decay、embedding consensus 或最终
scalar 已校准为 truth probability，30 个 synthetic cases 也不支持跨域“视觉安慰剂”规律。AlphaEvolve MARL
已完成 v1/v2 事件版本、v3 revision、全部 algorithm listings、18-game 与 random-NFG
evaluation 联读；证据支持“constrained program search 能产生可执行候选”及“raw fitness 必须经过 mechanism
audit/distillation”，却不支持 v1 对 volatility、hybrid blending 或 train/eval asymmetry 的因果叙述，也不支持把
单次 exact-tabular search 外推为自动科学发现或 deployed Multi-Agent。Unified Latents 已完成唯一 v1 的
17 页 PDF、全部公式/实验/ablation/Appendix 复核；证据支持 rate、reconstruction 与下游 model capacity 的耦合，
但不支持排除 autoencoder/decode cost 后的 FLOP headline 外推为端到端效率，也没有 artifact、公开 internal data、
hardware 或 uncertainty。其 18 分不改变原评分，但新增 Part III 已关闭 structural owner gap，长期机制以
Experimental 边界进入 Ch23。DDiT 已完成唯一
v1、项目页、全部方法与实验复核；证据支持 adaptive patch granularity 是一种 model-internal compute policy，
但不支持把 training-free scheduler 外推为 training-free system。阈值表反序、3.52× contract 歧义、无
hardware/runtime/training/user-study artifact 进一步限制精确效率结论；其 LLM 章节误映射也已撤回，长期机制以
Disputed performance boundary 进入 Ch24。2Mamba2Furious 已完成 v1、v3 revision、训练/推理 artifact、checkpoint collection 与 custom kernel
联读；证据支持 higher-order feature 是 fixed recurrent state 的表达力—容量旋钮，却不支持 production
latency/throughput、通用 softmax parity 或 NIAH 的 broad long-context headline。论文 evaluation bug、仅 1000 条且
删去最长 case 的 NIAH、实验性 kernel 与 event-time code snapshot 缺失均已进入证据边界。23/23 候选的
primary-source disposition 已明确，Candidate Evidence Gate 与 Source-Family Books Gate 均通过；AI Infra
历史 release/RFC 覆盖仍不完整，所以整周 archive 仍不得写成 fully complete，Archive Completion Gate 保持 Open。

## Cross-Week Deduplication

后续 agent telemetry 报告若更换 classifier、产品 surface 或样本窗口，不能直接拼接成同一
时间序列。HF 2 月 18～20 日页面中的 SkillsBench（2602.12670）、SAE sanity checks
（2602.14111）、SLA2（2602.12675）、SpargeAttention2（2602.13515）、AutoWebWorld
（2602.14296）、Empty Shelves（2602.14080）与 Mobile-Agent-v3.5（2602.16855）均按 arXiv v1
重定位到 W07；本周不重复计分。PAHF 的 Meta Research 页面到 2 月 26 日发布，只用于核验
source family，不改变 2 月 18 日 arXiv 首发归周。

## Knowledge Tree Position

W08 最终使用 12 个 Stable Knowledge Node owner：`MODEL-LONG-CONTEXT`（Ch22）、
`MULTIMODAL-REPRESENTATION`（Ch23）、`MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）、
`MULTIMODAL-WORLD-MODELS`（Ch25）、`MULTIMODAL-EMBODIED-VLA`（Ch26）、
`TRAIN-PRETRAINING`（Ch28）、`TRAIN-GRPO`（Ch33）、`PLATFORM-EVALUATION-SYSTEM`（Ch66）、
`AGENT-MEMORY`（Ch77）、`AGENT-PLANNING`（Ch79）、`AGENT-WORKFLOW`（Ch81）与
`AGENT-MULTI-AGENT`（Ch82）。旧 Ch24/29/62/73/75/77/78 分别映射到 current Ch28/33/66/77/79/81/82；
新增 Part III 关闭了 Unified Latents、DDiT 与 CUWM 的 structural owner gap。

## Recommended Action

Source-Family Books Gate 已完成。后续只追踪未完成的 engineering discovery 与跨索引召回，不重复把本周
机制写入 Books。DDiT 的 threshold/3.52× 冲突、GLM-5 的 exact training snapshot、OpenClaw 的 event-date runtime
和所有未披露 workload 字段继续冻结；Archive Completion Gate 关闭前不得把这些空白补写成事实。

## Event-Date Daily Decision

Historical Backfill 不补造 Daily；21 项 recovered candidates 直接保留在本 Weekly。真实事件日期
见 census，HF discovery date 不作为 Event-Date Daily。

## Books Integration Decision

`Source-Family Books Gate Complete / Archive Completion Gate Open`。

- `Refine — Existing Argument`（18）：GLM-5、Frontier AI Risk Management、ResearchGym、Magma、
  Vision Wormhole、DreamZero、in-context co-player inference、Agent Reliability、REFINE、PAHF、MMA、
  AlphaEvolve MARL、Calibrate-Then-Act、Unified Latents、DDiT、CUWM、2Mamba2Furious、Human Interaction。
- `No Change — Already Covered`（4）：autonomy telemetry、First Proof、OpenClaw audit、TAROT。
- `Weekly Only`（1）：MapTrace（16/30，来源与拒绝理由已核验）。

所有 Refine 均写入 owner 论证中的“旧方案边界 → 约束变化 → 新机制 → 新 failure mode / 共存条件”，
没有复制论文摘要或性能 headline。DDiT 保持 `Disputed performance contract`，其他 Experimental 条件亦保留。

## Ignored Noise

把 session duration 等同于成功率或“自主性等级”的二次解读；把 HF 推荐日期当首次公开日；
把 GLM-5、DreamZero、CUWM 等作者 benchmark 当通用系统结论；把 SGLang Apple-device roadmap
issue 当已实现功能或 release。

## 2026-07-31 Full Re-Audit Addendum — Provisional

- Agent autonomy 官方报告已全文复核。长期结论是 autonomy 为模型、任务机会、产品边界、
  用户干预与工具权限共同形成的 deployment observation，不是纯模型标量；已写入 Ch63。
- session duration/tool calls 仍标记为 proxy；单厂商流量、classifier 与 sampling 边界未被
  外推。First Proof 继续 Weekly only。
- 2026-08-08 discovery repair 证明该 Addendum 只覆盖旧版两项，不能代表 W08 完成；新增候选的
  `Integration Decision` 均等待非模板化 Source Review。

## Repository Changes

- 2026-08-13：完成 W08 的逐项 Books Integration 与独立周级 Review；23 项最终 disposition 为
  18 Refine、4 No Change、1 Weekly Only，更新 12 个 Stable Node owners。原有 2026-08-08 “不修改 Books”
  记录保留为当日审计历史，不代表当前状态；Source-Family Books Gate Complete，Archive Completion Gate Open。

- 2026-08-08：重开 W08 discovery，新增 21 项候选的评分与 census；只补 Weekly，不修改 Books、
  Daily、ROADMAP 或 Git index。
- 2026-08-08：完成 GLM-5 论文、Appendix、官方模型仓库和 slime artifact 的联合 Source Review；
  明确训练实现未完整开源、当前 slime 快照不能反写事件日，并保持 Books Gate 关闭。
- 2026-08-08：完成 Agent Reliability v1 全文、v3 revision、HAL dashboard/harness 的联合 Source
  Review；识别并记录 v1 outcome-consistency 公式已在 v3 纠正，不修改 Books。
- 2026-08-08：完成 ResearchGym v1、Appendix 与当前官方 benchmark/runtime artifact 的联合 Source
  Review；把单一结果分数拆为 result validity、semantic progress、environment integrity，并明确当前
  main branch 无 tag/release、不能反推事件日代码，不修改 Books。
- 2026-08-08：完成 CUWM v1、Appendix 与 GUI-360 data lineage 的联合 Source Review；将旧 census 的
  Ch71 owner 纠正为 Ch75，并把作者的 Agent task score 限定为 339 条离线单步 action matching，未
  外推为多步真实执行或安全保证，不修改 Books。
- 2026-08-08：完成 PAHF v1、证明、Appendix 与当前官方代码的联合 Source Review；把主 owner 从初始泛化
  范围收敛到 Ch73，区分行动前 ambiguity clarification 与行动后 stale-preference correction，并明确
  persona simulation、理想化 regret assumptions 和 paper-time code snapshot 缺失，不修改 Books。
- 2026-08-08：完成 Calibrate-Then-Act v1→v3、oracle proof、prior sensitivity、paired significance、GRPO
  contract 与当前官方 artifact 联合 Source Review；识别 v1 cost-ratio 文本不一致已在 v3 修正，将主 owner
  收敛到 Ch75，并保持 Books Gate 关闭。
- 2026-08-08：完成 Human Interaction in Web Agents v1→v4、模型卡与当前 PlowPilot artifact 联合 Source
  Review；识别 live-study headline 从 4 人/26.5% 变化为合并 16 人/36.8%，将主 owner 从 Ch78 纠正为 Ch77，
  并记录 trajectory-level split、raw dataset unavailable 与 advisory-vs-authority 边界，不修改 Books。
- 2026-08-08：完成 Frontier AI Risk Management Framework v1.5 的五个风险族、mitigation、global limitations 与
  related misevolution artifact 联合 Source Review；将多套 heterogeneous experiments 拆回 per-risk EvalSpec，指出
  同集群、具备 Kubernetes 权限且 M4 要求新建 Deployment 的实验不能外推为自然跨环境 self-replication，并保持
  Books Gate 关闭。
- 2026-08-08：完成 OpenClaw trajectory audit 的 22 页 PDF、六个 seed-case JSON 与当前官方 security/memory/
  skills/exec/logging docs 联合 Source Review；识别 58.9% 是六维 macro average、sandbox disabled/unrestricted exec
  是 evaluation contract，并记录 false-assumption labels、seed count、runtime pin 与 raw trajectory 缺口；结论为
  `No Change — Already Covered / Evidence Contract Incomplete`，不修改 Books。
- 2026-08-08：完成 Magma v1 的算法、证明、Llama/Nano-MoE/controlled experiments 与全部消融复核；将
  错误的 Ch27 owner 纠正为 Ch24，区分 dense optimizer-state transition 与 sparse parameter application，并
  记录 alignment sampling 未优于 uniform sampling、无官方 artifact、无系统性能证据；结论为
  `Refine — Existing Argument / Scope and Owner Corrected / Human Gate Pending`，不修改 Books。
- 2026-08-08：完成 TAROT v1、全部实验/Appendix 与当前官方 reward/config/data artifact 联读；将主 owner
  从错误的 Ch27 纠正为 Ch29，识别 capability selector 未操作化、论文与仓库的 generator/count drift，及
  reward comparator 未检查输出行数、active-tier reward ceiling 未归一化等问题；结论为
  `No Change — Already Covered / Capability Selection and Verifier Contract Incomplete`，不修改 Books。
- 2026-08-08：完成 Vision Wormhole v1 全文、v2 revision 与当前官方代码联读；将主 owner 从错误的
  Ch57～59/76 纠正为 Ch78，区分 O(N) adapter integration 与 runtime complexity，记录 v1 的 mixed
  speed/accuracy、4B～12B accuracy regression、v2 scope change、无 tag/release 与 1024/1026 codec-token
  ambiguity；结论为 `Refine — Existing Argument / Experimental Latent Message Contract / Scope and Revision
  Corrected / Human Gate Pending`，不修改 Books。
- 2026-08-08：完成 DreamZero 唯一 v1、全部 Appendix、项目页与当前官方代码联读；将主 owner 从
  Ch18/71/75 候选收敛到 Ch75，区分 joint world/action model、actual-observation replacement、action-chunk
  reactivity window 与外部 safety authority，记录论文 150ms optimized path 和当前 README 0.6s/3s path
  不同、无 event-date tag 及 current training config 不是 paper pretraining recipe；结论为 `Refine — Existing
  Argument / Closed-Loop World-Action Policy and Reactivity Contract / Scope and Artifact Boundary Corrected /
  Human Gate Pending`，不修改 Books。
- 2026-08-08：完成 In-context co-player inference 唯一 v1、PPI/A2C 实现、全部 ablation 与 equilibrium
  proofs 复核；将初始 Ch76 owner 纠正为 Ch78，区分 authenticated runtime identity 与从 history 推断的
  behavioral policy，记录 A2C seed collapse、best-hyperparameter selection、no-mixed-pool confound、理论
  idealization 与无官方 code/hardware；结论为 `Refine — Existing Argument / Experimental Partner-Adaptation
  and Strategic Shaping Contract / Owner and Scope Corrected / Human Gate Pending`，不修改 Books。
- 2026-08-08：完成 REFINE 唯一 v1、全部实验/Appendix、官方 README 与 commit history 复核；将
  Ch17/22/25 泛化映射收敛到 Ch22，区分 fast-state architecture 与 objective horizon，指出同一 sequence
  不同 prefix 的 reward grouping 不等价于原始 same-prompt GRPO，并记录原 Long-Data-Collections 已不可用、
  当前建议替代数据不能复现论文分布；结论为 `Refine — Existing Argument / Experimental Objective-to-State-
  Lifetime Contract / GRPO and Reproduction Boundary Corrected / Human Gate Pending`，不修改 Books。
- 2026-08-08：完成 MMA 唯一 v1、全部实验/Appendix、官方 confidence config、核心实现、运行入口、
  unit test 与 commit history 联读；将初始 Ch72/73 映射收敛到 Ch73，区分 retrieval relevance、可靠性
  features、sufficiency、calibrated uncertainty 与 action policy，识别当前 consensus 依赖邻居已存 confidence 与
  embedding cosine、缺少 contradiction verifier/fixed-point/invalidation 协议，并记录 FEVER 三 seeds、LoCoMo
  两套 utility operating point、30-case synthetic MMA-Bench 与未披露 API snapshot/hardware 边界；结论为
  `Refine — Existing Argument / Experimental Memory-Evidence Reliability and Selective-Action Contract /
  Mechanism and Evidence Boundary Corrected / Human Gate Pending`，不修改 Books。
- 2026-08-08：完成 AlphaEvolve MARL 的 v1/v2 事件版本、v3 revision、CFR/PSRO search skeleton、全部
  algorithm listings、18-game/random-NFG evaluation、component ablation、prompts 与 limitations 联读；将初始
  Ch29/76/79 映射纠正为 Ch77，识别 5 月 v3 才新增 distillation，并记录 v1 对 volatility、hybrid blending 与
  train/eval asymmetry 的强机制归因未通过后续 audit、test set 已参与 distillation、单次 search trajectory、无完整
  artifact/compute disclosure 等边界；结论为 `Refine — Existing Argument / Experimental Search-to-Distillation
  and Independent-Validation Contract / Revision and Owner Corrected / Human Gate Pending`，不修改 Books。
- 2026-08-08：完成 Unified Latents 唯一 v1 的 17 页 PDF、ELBO/bitrate 推导、two-stage lifecycle、全部
  image/video experiments、rate/shape/L2 sweeps、四项 ablation、Limitations 与 single-stage Appendix 复核；
  将错误的 Ch18 owner 改为 `No Direct ROADMAP Owner`，记录 training FLOPs 排除 autoencoder、diffusion
  decoder 采样成本、internal data、无 artifact/hardware/seeds/uncertainty 等边界；结论为 `Weekly Only — Below
  20 / No Direct ROADMAP Owner / Full Review Complete`，不修改 Books 或 ROADMAP。
- 2026-08-08：完成 DDiT 唯一 v1 的 13 页 PDF/HTML、官方项目页、multi-patch artifact、finite-difference
  scheduler、全部 image/video tables 与 analysis 复核；撤回错误的 Ch42/45 owner，记录只对 scheduler 成立的
  training-free 边界、阈值—速度反序、两个 3.52× contract、无 hardware/training/user-study artifact 与多请求
  shape fragmentation 风险；结论为 `Weekly Only — No Direct ROADMAP Owner / Experimental Evidence Contract /
  Owner and Evidence Boundary Corrected / Full Review Complete`，不修改 Books 或 ROADMAP。
- 2026-08-08：完成 2Mamba2Furious v1、v3 revision、全部 method/evaluation/Appendix、当前训练与推理 artifact、
  checkpoint collection 和 custom Triton Kronecker kernel 联读；将 Ch17/22 泛化映射收敛到 Ch22，区分
  `O(1) in sequence length` 与 `O(d_h³)` recurrent state、2Mamba 与恢复 KV 的 2Mamba-E、raw-state crossover 与
  end-to-end SLO，并记录 90K evaluation bug、受限 NIAH、未优化 kernel 和 event-time code snapshot 缺失；结论为
  `Refine — Existing Argument / Experimental Higher-Order State Contract / Revision, Evaluation and Kernel Boundary
  Corrected / Human Gate Pending`，不修改 Books、ROADMAP、Learning State 或 Git index。

## Open Questions

1. autonomy telemetry 如何同时刻画有效进展、空转、风险动作与 human takeover？
2. GLM-5 的 exact slime commit/config、异步 RL 机制独立 ablation、完整集群 contract 与
   crash-consistent policy/trajectory transaction 仍能否获得？
3. Agent Reliability v3 是否公开按新公式重算的 raw per-run data/exact commit，怎样为低 baseline、
   K=5 与 severity judge 建立 paired uncertainty 和 calibration？
4. reliability metric、trajectory audit、research environment 与 user intervention model 如何形成
   互补的 EvalSpec，而不是再压缩成单一成功率？
5. ResearchGym 的 grader mutation tests、semantic-progress signal、cross-run isolation 与 inspector
   calibration 能否形成可复用的 research-agent evaluation contract？
6. CUWM 的 imagined/actual state、uncertainty、candidate coverage 与 multi-step error 怎样形成可执行的
   model-based planning contract，而不是把生成 screenshot 当 authoritative state？
7. PAHF 的 preference scope、temporal validity、supersession、consent 与 user-friction cost 怎样进入统一的
   personalization memory contract，而不是把 LLM merge 当作真值更新？
8. Calibrate-Then-Act 的 prior calibration、multi-dimensional action cost、posterior update 与 conservative
   override 怎样成为 Planning contract，而不是 prompt 中一组不可追溯的概率？
9. Human intervention 的 observed behavior 怎样转为 normatively safe 的 ask/takeover policy，control lease、
   pending action、handback 与 state reconciliation 又怎样进入 durable Workflow？
10. frontier-risk EvalSpec 怎样显式分离 capability、elicitation、opportunity、permission 与 consequence，并对不同
    risk family 保留不可聚合的 evidence boundary？
11. OpenClaw audit 的 event-date runtime、raw trajectories、label semantics 与 macro aggregation 能否恢复，怎样用
    sandbox/tool-policy/approval/memory 的 paired ablation 分离失败来源？
12. Magma 中 uniform mask、damping 与 alignment 的独立因果贡献如何分离，dense-state/sparse-application
    在大模型 distributed runtime 中能否产生可测的 memory、communication 或 wall-clock 收益？
13. TAROT 的 capability→schedule rule 如何事前校准，当前 reward comparator、reward ceiling 与 suite
    coverage 如何经 golden/mutation/differential tests 修复并形成可重放 verifier version？
14. latent Agent message 怎样绑定 model/codec/schema version、fidelity probe、text fallback、audit projection、
    buffer lifecycle 与 replay identity，避免把不可读 embedding 误当 authoritative state？
15. World Action Model 的 actual/predicted state、observation timestamp、action chunk revision/deadline 与 safety
    controller 如何形成可恢复控制契约，并把 video plausibility、causal dynamics、alignment 和 task success 分开评估？
16. co-player belief 如何与 authenticated identity 分离并校准，怎样检测 strategic shaping、collusion、belief poisoning
    与 equilibrium drift，并由外部 policy 定义“可接受合作”？
17. fast-state objective 的 credit horizon 怎样按 state lifetime 自适应，同一 sequence 不同 prefix 的 relative reward
    如何校准，TTT 的 reset/rollback/tenant isolation 又怎样进入 serving contract？
18. memory reliability 如何把 source calibration、fact valid-time、independent corroboration、contradiction verifier、
    confidence recompute/invalidation 与 risk-aware threshold 组成可审计 contract，而不是固定 heuristic scalar？
19. program search 的 raw fitness、cross-distribution ablation、human distillation 与 untouched final holdout 怎样形成
    不复用 test evidence 的多层 Gate，独立 search 是否会发现相同 mechanism core？
20. generative latent 的 rate、reconstruction、base-model capacity、autoencoder training 与 decoder serving cost 如何
    形成端到端 Pareto；多来源成熟后是否需要独立 ROADMAP owner？
21. DDiT 的阈值表、两个 3.52× contract 与缺失 artifact 如何复核；dynamic shape 在 multi-request batching、
    graph capture、kernel reuse 与 tail SLO 下是否仍有净收益？
22. 2Mamba 的 higher-order state 在等 compute/token/wall-clock 与优化 kernel 下是否仍有净收益；真实 crossover、
    state checkpoint/migration/reset/isolation、完整 token-length retrieval/composition evaluation 如何建立？
23. 历史 GitHub release/RFC 如何建立可重复的日期索引，补齐 W08 engineering coverage？

## Sources

- Anthropic, “Measuring AI agent autonomy in practice,” published 2026-02-18:
  https://www.anthropic.com/research/measuring-agent-autonomy
- OpenAI Research, “Our First Proof submissions,” published 2026-02-20:
  https://openai.com/index/first-proof-submissions/
- Google Research, “Teaching AI to read a map,” published 2026-02-17:
  https://research.google/blog/teaching-ai-to-read-a-map/
- GLM-5 technical report, arXiv v1 2026-02-17; official code:
  https://arxiv.org/abs/2602.15763
  https://github.com/zai-org/GLM-5
  https://github.com/THUDM/slime
- Hugging Face Daily Papers discovery pages, accessed 2026-08-08; discovery only:
  https://huggingface.co/papers/date/2026-02-16
  https://huggingface.co/papers/date/2026-02-17
  https://huggingface.co/papers/date/2026-02-18
  https://huggingface.co/papers/date/2026-02-19
  https://huggingface.co/papers/date/2026-02-20
- Recovered W08 primary papers; review state follows the census:
  https://arxiv.org/abs/2602.14457
  https://arxiv.org/abs/2602.14364
  https://arxiv.org/abs/2602.15112
  https://arxiv.org/abs/2602.15322
  https://arxiv.org/abs/2602.15449
  https://arxiv.org/abs/2602.15382
  https://arxiv.org/abs/2602.15922
  https://arxiv.org/abs/2602.16301
  https://arxiv.org/abs/2602.16666
  https://arxiv.org/abs/2602.16704
  https://arxiv.org/abs/2602.16173
  https://arxiv.org/abs/2602.16493
  https://arxiv.org/abs/2602.16928
  https://arxiv.org/abs/2602.16699
  https://arxiv.org/abs/2602.17270
  https://arxiv.org/abs/2602.16968
  https://arxiv.org/abs/2602.17365
  https://arxiv.org/abs/2602.17363
  https://arxiv.org/abs/2602.17588
- Magma v1 paper and revision metadata:
  https://arxiv.org/html/2602.15322v1
  https://arxiv.org/abs/2602.15322
- TAROT v1 and current official artifact:
  https://arxiv.org/html/2602.15449v1
  https://arxiv.org/abs/2602.15449
  https://github.com/deep-diver/TAROT
- Vision Wormhole v1/current v2, revision metadata and official artifact:
  https://arxiv.org/html/2602.15382v1
  https://arxiv.org/html/2602.15382v2
  https://arxiv.org/abs/2602.15382
  https://github.com/xz-liu/heterogeneous-latent-mas
- DreamZero v1, project page and current official artifact:
  https://arxiv.org/html/2602.15922v1
  https://arxiv.org/abs/2602.15922
  https://dreamzero0.github.io/
  https://github.com/dreamzero0/dreamzero
- In-context co-player inference v1; no official code/artifact located:
  https://arxiv.org/html/2602.16301v1
  https://arxiv.org/abs/2602.16301
- REFINE v1, official artifact and event-time commit history:
  https://arxiv.org/html/2602.16704v1
  https://arxiv.org/abs/2602.16704
  https://github.com/princetonvisualai/ReFINE
  https://github.com/princetonvisualai/ReFINE/commits/main/
- MMA v1, official artifact, core confidence implementation/config/test and commit history:
  https://arxiv.org/html/2602.16493v1
  https://arxiv.org/abs/2602.16493
  https://github.com/AIGeeksGroup/MMA
  https://github.com/AIGeeksGroup/MMA/blob/main/MMA/MMA/services/confidence_module.py
  https://github.com/AIGeeksGroup/MMA/blob/main/MMA/MMA/settings.py
  https://github.com/AIGeeksGroup/MMA/blob/main/MMA/configs/confidence_v2.yaml
  https://github.com/AIGeeksGroup/MMA/blob/main/MMA/tests/test_confidence_v2.py
  https://github.com/AIGeeksGroup/MMA/commits/main/
- AlphaEvolve for MARL event-time v1/v2, later v3 revision and original AlphaEvolve family; no official
  paper-specific artifact located:
  https://arxiv.org/html/2602.16928v1
  https://arxiv.org/html/2602.16928v2
  https://arxiv.org/html/2602.16928v3
  https://arxiv.org/abs/2602.16928
  https://arxiv.org/abs/2506.13131
  https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- Unified Latents v1 PDF and revision metadata; no official artifact located:
  https://arxiv.org/pdf/2602.17270
  https://arxiv.org/abs/2602.17270
- DDiT v1 PDF/HTML, revision metadata and official project page; no official code located:
  https://arxiv.org/pdf/2602.16968
  https://arxiv.org/html/2602.16968v1
  https://arxiv.org/abs/2602.16968
  https://ddit-fast.github.io/ddit/
- 2Mamba2Furious event-time v1, later v3 revision, current author artifacts and checkpoint collection:
  https://arxiv.org/html/2602.17363v1
  https://arxiv.org/html/2602.17363v3
  https://arxiv.org/abs/2602.17363
  https://github.com/gmongaras/2Mamba2Furious
  https://github.com/gmongaras/Triton-Efficient-Kronecker-Product
  https://huggingface.co/collections/gmongaras/2mamba2furious-linear-in-complexity
- Agent Reliability revision family and public evaluation artifacts:
  https://arxiv.org/html/2602.16666v1
  https://arxiv.org/html/2602.16666
  https://hal.cs.princeton.edu/reliability/
  https://github.com/princeton-pli/hal-harness
- ResearchGym v1, revision metadata and current official artifact:
  https://arxiv.org/html/2602.15112v1
  https://arxiv.org/abs/2602.15112
  https://github.com/Anikethh/ResearchGym
- Computer-Using World Model v1 and GUI-360 data lineage:
  https://arxiv.org/html/2602.17365v1
  https://arxiv.org/abs/2602.17365
  https://arxiv.org/html/2511.04307v1
- PAHF v1 and current official artifact:
  https://arxiv.org/html/2602.16173v1
  https://arxiv.org/abs/2602.16173
  https://github.com/facebookresearch/PAHF
- Calibrate-Then-Act v1, current v3, revision metadata and official artifact:
  https://arxiv.org/html/2602.16699v1
  https://arxiv.org/html/2602.16699v3
  https://arxiv.org/abs/2602.16699
  https://github.com/NSF-Simons-CosmicAI-Institute/CalibrateThenAct
- Modeling Distinct Human Interaction in Web Agents v1/current v4 and public artifacts:
  https://arxiv.org/html/2602.17588v1
  https://arxiv.org/html/2602.17588v4
  https://arxiv.org/abs/2602.17588
  https://huggingface.co/CowCorpus
  https://huggingface.co/CowCorpus/gemma-27b-cowcorpus
  https://github.com/oaishi/PlowPilot
- Frontier AI Risk Management Framework v1.5 and related misevolution artifact:
  https://arxiv.org/html/2602.14457v1
  https://arxiv.org/abs/2602.14457
  https://github.com/ShaoShuai0605/Misevolution
- OpenClaw trajectory audit v1, seed-case artifact and official mechanism docs:
  https://arxiv.org/pdf/2602.14364
  https://arxiv.org/abs/2602.14364
  https://github.com/tychenn/clawdbot_report
  https://docs.openclaw.ai/gateway/security
  https://docs.openclaw.ai/concepts/memory
  https://docs.openclaw.ai/tools/skills
  https://docs.openclaw.ai/tools/exec
  https://docs.openclaw.ai/gateway/logging
- SGLang Apple-device support roadmap issue, created 2026-02-21; planning signal only:
  https://github.com/sgl-project/sglang/issues/19137

## 2026-08-13 Source-Family Books Integration

独立 Source-Family Books Gate 已对 23/23 候选完成反向核验，最终为 18 Refine、4 No Change、
1 Weekly Only。18 项机制合并进入下列 owner，而非在章末建立论文列表：

| Stable owner | Current / Legacy | Integrated mechanism |
| --- | --- | --- |
| `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | objective horizon、fast-state lifetime、higher-order recurrent state cost |
| `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | rate–distortion–capacity–decoder contract |
| `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | adaptive granularity 与 multi-shape runtime artifact |
| `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | imagined UI consequence 与 actual-observation authority |
| `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | world/action prediction、observation replacement 与 reactivity window |
| `TRAIN-PRETRAINING` | Ch28 / Ch24 | dense optimizer state、sparse parameter application 与 masking bias |
| `TRAIN-GRPO` | Ch33 / Ch29 | TITO、policy-version identity 与 environment-failure terminal semantics |
| `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | reliability profile、research evidence split 与 heterogeneous risk families |
| `AGENT-MEMORY` | Ch77 / Ch73 | preference scope、valid-time、corroboration 与 selective action |
| `AGENT-PLANNING` | Ch79 / Ch75 | calibrated prior、information value、cost 与 hard override |
| `AGENT-WORKFLOW` | Ch81 / Ch77 | search-to-distillation Gate 与 ask/takeover/handback transition |
| `AGENT-MULTI-AGENT` | Ch82 / Ch78 | latent-channel contract 与 behavioral-belief/authenticated-identity split |

No Change 项均有具体去重依据：Ch67 已拥有 deployment autonomy telemetry；Ch66 已拥有 artifact/claim
evidence ladder；Ch72 已拥有 trajectory、tool policy 与 permission boundary；Ch27/33 已拥有 curriculum 与
verifier contract。MapTrace 不改变当前主干。所有作者 benchmark、未披露实现与冲突性能数字均未进入正文。

Repository Changes：更新上述 12 个 owner chapters，并同步本周最终 disposition、年度索引和 Learning State。
Archive Completion Gate 仍 Open，只代表 discovery/release coverage 尚未闭合，不撤销已完成的 Source-Family
Books Gate。
