# AI Research Weekly — 2025-W09

> Coverage Window: 2025-02-24～2025-03-02
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项与长期 AI System 认知相关的证据：Claude 3.7 Sonnet and Claude Code。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Claude 3.7 Sonnet and Claude Code（2025-02-24）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Claude 3.7 Sonnet and Claude Code | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching；作为 hybrid reasoning 产品信号 |

### Deep Analysis 1 — Claude 3.7 Sonnet and Claude Code

- First Public: 2025-02-24
- Status: Official release; vendor evaluation
- Primary Source: https://www.anthropic.com/news/claude-3-7-sonnet
- Evolution Relationship: Direct Evolution

#### Why

同一模型需要在即时响应与长思考之间选择不同 inference budget；coding agent 还需要把 reasoning 接到可执行工具闭环。

#### Principle and Mechanism

官方发布引入 hybrid reasoning 与可控 thinking budget，并以 Claude Code research preview 展示终端 agent。

#### Trade-off and Evidence Boundary

统一模型简化产品路由，却把预算控制、可见 CoT、成本与 latency 交给运行时；厂商 benchmark 无法分离 model 与 harness 贡献。

#### Connection and Evolution

知识树位置：第 20、52、74～77 章。Worth Watching；作为 hybrid reasoning 产品信号。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Claude 3.7 Sonnet and Claude Code

- **Candidate / Week / Score:** Claude 3.7 Sonnet and Claude Code / 2025-W09 / 23/30。
- **Source Family ID:** `claude-3-7-hybrid-reasoning-and-code-agent`。
- **Source Type:** Anthropic official release + 43-page system card + extended-thinking disclosure；Claude Code
  当时为 product research preview，无公开 runtime design paper。
- **First-public Date / Revision History:** 2025-02-24；system card 与 release同日。后续 Claude Code/product
  changes 不反写为 3.7 release facts。
- **Direct Primary Sources:** https://www.anthropic.com/news/claude-3-7-sonnet；
  https://www.anthropic.com/news/visible-extended-thinking；
  https://www.anthropic.com/system-cards；官方 Claude 3.7 Sonnet System Card PDF。
- **Related Primary Sources:** linked SWE-bench/TAU-bench definitions与 scaffold disclosures；Claude Code current
  docs只证明后续状态，不证明 2025 preview architecture。
- **Access and Verification Status:** Verified for public model/product behavior and system-card evaluations；model
  architecture、training recipe、Claude Code planner/state/recovery 为 `Mechanism Not Disclosed`。
- **Full-read Coverage:** 已读 announcement/appendix/scaffolding、extended-thinking rationale、system card training/
  release process、thinking mode、computer-use/prompt-injection、CoT faithfulness、autonomy/cyber/CBRN evaluations、
  thresholds与third-party assessment；核对 Claude Code preview公开 tool surface。
- **Original Problem:** users需要按 task difficulty在低延迟回答与更多 inference compute之间选择；coding
  还需让模型读取/修改 repository并运行命令/测试，不能只生成 isolated snippet。
- **Why the Previous Design Was Reasonable:** separate fast/reasoning models可独立优化成本与质量，standard
  response减少 latency和 token暴露；人工 coding workflow把 shell/git/test权限留在人类，failure radius较小。
- **Changed Constraint:** 同一产品希望连续调节 reasoning tokens并减少 model routing discontinuity；terminal
  agent需要把 reasoning接到高权限工具，同时面临 prompt injection、partial success和long-horizon stopping。
- **Mechanism:** system card只公开同一 model由 RL训练生成 extended-thinking tokens，API通过 system prompt给
  maximum thinking tokens；standard/extended mode由用户选择。Claude Code preview公开可搜索/读取/编辑文件、
  运行 tests/CLI、commit/push，并要求 user in loop；内部 planner、sandbox、state machine Not Disclosed。
- **State Ownership:** model/runtime拥有当前 thinking-token budget与completion；Claude Code可观察地持有 session/
  tool transcript，但 authoritative file/git state仍在用户环境。权限、checkpoint、retry与approval owner在
  2025来源中 Not Disclosed，不能从后续产品推断。
- **Control Flow / Data Flow:** prompt+mode/budget→single model standard或extended completion→可见 thinking+
  final answer；coding preview是 user task→model选择 bash/file-edit actions→environment结果回流→iterate→
  human oversight。具体 orchestration/rollback未知。
- **Implementation Details:** extended mode maximum tokens由system prompt指定；training仅披露 proprietary data mix、
  filtering、RL/Constitutional AI概况。Claude Code release列出 bash+string-replacement editor等 minimal scaffold；
  high-compute SWE-bench另有parallel attempts、visible-test filtering与scoring model，不能和vanilla pass@1混用。
- **Evaluation Setup:** release含 SWE-bench Verified、TAU-bench等vendor evaluations；TAU-bench max steps从30增至
  100并加planning tool；SWE-bench high-compute使用parallel sampling/filter/ranker。system card另做176-task prompt-
  injection eval、autonomy rule-out suite与CoT faithfulness tests。
- **Baselines / Ablations / Sensitivity:** standard vs extended mode、3.5 predecessor、不同 thinking lengths与
  mitigations；prompt-injection 74%→88% prevention同时0.5% false positive属于176-task adversarial set；system
  card显示 thinking length只在部分 domain提升，CoT常未显式提关键 clues。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** hardware、parameter、precision、serving
  batch/concurrency Not Disclosed；thinking budget为token cap但具体 benchmark各自配置不同；不构成通用 latency/
  cost/SLO curve。
- **What the Evidence Actually Proves:** 官方提供同一model的可控 extended-token interface及一个terminal coding
  preview；system card证明tool-using risk需要model training+runtime classifier等分层 mitigation，且明确可见
  CoT不保证faithful。benchmark结果高度依赖 scaffold/steps/compute。
- **What It Does Not Prove:** 不公开 hybrid model内部architecture，不证明thinking tokens忠实或单调提升质量，
  不证明Claude Code使用某种durable workflow，也不证明厂商 SWE-bench score可分离model与harness贡献。
- **Limitations / Threats to Validity:** proprietary model与vendor eval；benchmark scaffold/infra exclusions改变
  comparability；thinking可泄露或帮助jailbreak，streaming classifier可false-positive；prompt injection仍有未阻止
  cases；autonomy suite是rule-out而非通过即证明真实R&D acceleration。
- **Trade-offs / New Failure Modes:** unified model减少routing complexity，却把budget/latency/cost与thinking exposure
  交给runtime；terminal tools增加环境注入、credential/data exfiltration、partial edits、premature completion与
  rollback责任；CoT monitoring若不faithful会产生虚假安全感。
- **Where the Previous Design Still Applies:** latency-critical/简单请求使用standard mode；separate specialized
  models在成本隔离/独立升级时仍合理；高风险代码/运维应保持human approval、least privilege与deterministic CI。
- **Evolution Relationship:** `Direct Evolution`（product interface）：fixed response mode→same-model controllable
  compute；`Layering / Dependency`（coding）：model→tool harness→environment/approval，而非model自治的同义词。
- **ROADMAP Node:** Ch52主 owner（inference budget/SLO）；Ch20 reasoning/sampling handoff；Ch74～77负责tool/
  workflow；Ch68负责prompt-injection/security。
- **Target and Adjacent Chapters Read:** 已读 Ch19～21、Ch50～52、Ch68、Ch73～78；核对 budget control、
  model-vs-harness evaluation与untrusted tool environment。
- **Existing Coverage:** Books已有 adaptive inference budget、tool permission与workflow state原则；来源主要是
  version/product fact和system-card case，未披露可新增的model/runtime mechanism。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
  Disclosed`；若写入只可能作为Ch52/68受限案例，不形成新设计结论。
- **Changed Files or Rejection Reason:** 不改 Books；thinking budget、tool permission 和 workflow state 已由 Ch20/52/74～77 的通用 contract 覆盖。
- **Open Questions:** quality-per-token calibration、budget owner、encrypted/hidden thinking audit、Claude Code
  2025 preview的sandbox/approval/recovery contract与model/harness contribution separation。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- Claude 3.7 Sonnet and Claude Code → 第 20、52、74～77 章（Direct Evolution）

## Recommended Action

- Claude 3.7 Sonnet and Claude Code：Worth Watching；作为 hybrid reasoning 产品信号

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W09/README.md。
- 2025 Primary-Source Re-audit 进行中；本周尚未进入 Books Integration。

## Open Questions

- hybrid reasoning的内部机制、quality-per-token calibration以及Claude Code preview的state/sandbox/recovery
  contract仍未公开。

## Sources

- Claude 3.7 Sonnet and Claude Code — https://www.anthropic.com/news/claude-3-7-sonnet（First Public: 2025-02-24；Accessed: 2026-07-31）
- Claude 3.7 Sonnet System Card — https://www.anthropic.com/system-cards（First Public: 2025-02-24；Accessed: 2026-07-31）
