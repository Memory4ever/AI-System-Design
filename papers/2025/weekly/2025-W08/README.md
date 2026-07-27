# AI Research Weekly — 2025-W08

> Coverage Window: 2025-02-17～2025-02-23
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项与长期 AI System 认知相关的证据：AI co-scientist。重点不是记录发布热度，而是识别其改变了哪一项约束、机制与系统 trade-off。所有结论均按首次公开时间归档，性能或能力数字不脱离作者披露的模型、硬件、精度、输入输出、并发与 SLO 条件使用。

## Coverage Window and Limitations

- 使用官方发布日期、GitHub Release 时间或 arXiv v1 时间；不使用搜索收录日和后续修订日替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery、去重和引用链检查；论文机制回到 arXiv / 作者正文。
- Crossref 仅用于 Weekly metadata 交叉检验，不作为机制证据。
- 本周为历史回填，不补造 Daily；访问日期统一为 2026-07-31。
- 厂商 benchmark 和论文实验只代表其披露条件，缺少完整 workload contract 时不做跨系统性能结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：AI co-scientist（2025-02-19）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到论文 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| AI co-scientist | 4 | 4 | 3 | 4 | 4 | 3 | 22/30 | Worth Watching；不依据个案结果外推自治科研能力 |

### Deep Analysis 1 — AI co-scientist

- First Public: 2025-02-19
- Status: Google Research official prototype
- Primary Source: https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/
- Evolution Relationship: Layering / Dependency

#### Why

科学发现任务把 agent 的目标从生成答案扩展到提出、比较、演化和验证假设。

#### Principle and Mechanism

官方原型使用多 agent 角色和 tournament-style comparison 迭代研究提案，并有人类和实验反馈。

#### Trade-off and Evidence Boundary

更长 workflow 增加探索覆盖，但 evaluator bias、实验成本、领域安全与责任归属成为系统约束。

#### Connection and Evolution

知识树位置：第 62、74～78 章。Worth Watching；不依据个案结果外推自治科研能力。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### AI co-scientist

- **Candidate / Week / Score:** AI co-scientist / 2025-W08 / 22/30。
- **Source Family ID:** `google-ai-co-scientist-workflow`。
- **Source Type:** Google Research official Blog + arXiv/Nature author paper + extensive supplementary methods。
- **First-public Date / Revision History:** Blog 2025-02-19；paper v1 2025-02-26、v2 2026-06-29，后成为
  2026 Nature paper。W08 归档的是 Blog event；本轮按 v2 157-page author manuscript 核验，同时明确其中
  Gemini 2.5/3、GPT-5.4 等 2026 revision 内容不是 2025 已知事实。
- **Direct Primary Sources:** https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/；
  https://arxiv.org/abs/2502.18864；https://arxiv.org/pdf/2502.18864。
- **Related Primary Sources:** Gemini technical reports 定义 base-model capability；paper 所引 wet-lab protocols、
  databases 与 benchmark papers 定义验证环境，不公开 production deployment。
- **Access and Verification Status:** Verified；Blog、42-page main paper 与 115-page supplement 可访问。源码、
  scheduler implementation 与 production topology未公开，相关细节按 `Not Disclosed` 处理。
- **Full-read Coverage:** 已读 metadata/revisions、Abstract/Introduction/Related Work、architecture/Methods、六类
  agents、task queue/context memory、Elo tournament、human interaction、tools、203/15/11-goal evaluations、
  wet-lab studies、agent ablations、limitations/discussion、safety/red-team、pseudocode/prompts 与相关 supplement。
- **Original Problem:** scientific ideation 不只是一次 retrieval+answer，而是长期生成、查新、批判、比较、
  合并、实验设计与验证；单模型一次调用难维持 diverse hypotheses、全局 tournament state 与来源新颖性。
- **Why the Previous Design Was Reasonable:** 人类 scientist/peer review 对 novelty、feasibility 与实验风险有
  domain authority；单 agent/search pipeline 状态少、容易审计；brute-force parallel sampling 在有强 verifier
  的闭域任务可简单扩展。
- **Changed Constraint:** 希望用可扩展 test-time compute 探索开放 hypothesis space，并允许 expert 持续
  修改目标/约束；需要异步 workers、持久状态和评审反馈，而不是仅延长单条 CoT。
- **Mechanism:** Supervisor 解析 research goal/config，维护 asynchronous task queue并动态分配 Generation、
  Reflection、Ranking、Proximity、Evolution、Meta-review workers；pairwise debate 形成 Elo tournament；
  proximity graph 去重/聚类；Meta-review 的全局反馈追加到后续 prompts；persistent context memory 保存系统/
  agent state 与 summary statistics，支持长时运行和 restart。
- **State Ownership:** scientist 拥有 goal、constraints 与最终 selection；Supervisor 拥有 authoritative queue、
  allocation/terminal decision 与 progress statistics；specialized agents产生 hypotheses/reviews；tournament 拥有
  pairwise/Elo state；context memory持久化 agent/system state。paper 未披露 transaction、lease/idempotency schema。
- **Control Flow / Data Flow:** expert goal/documents→plan configuration→Supervisor enqueue→Generation/search→
  Reflection novelty/correctness review→Ranking debate/Elo→Proximity dedupe/cluster→Evolution refine/combine→
  Meta-review aggregate feedback→statistics/context checkpoint→再次 weighted scheduling→expert review→wet-lab。
- **Implementation Details:** Python 3.11.7；all agents 基于 Gemini 2.0 in original study；workers 通过 customized
  prompts/strategies 与 web/database/AlphaFold-like tools工作；Supervisor定期写 context memory并根据 queue/
  tournament stats调整 agent sampling。durable store、exact queue、retry与compute scheduler Not Disclosed。
- **Evaluation Setup:** 203 research goals 的 auto-Elo trajectory；15 expert-curated biomedical goals 与 frontier
  models/experts比较；11 goals blinded expert review；GPQA 用于 Elo concordance；三个 biomedical validations，
  包括从 2,300 approved drugs×34 cancers 搜索、expert筛选和 AML cell-line assays。
- **Baselines / Ablations / Sensitivity:** base LLMs/human best guesses；Generation strategies、Reflection with/
  without search、simple vs debate ranking、Evolution、Proximity、Meta-review ablations。search 将已发表 ideas 的
  auto-novelty score从 6.14 降至2.38；多数指标仍由 system/LLM auto-evaluation，不能视为外部 ground truth。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** base Gemini 2.0 variants；hardware、
  precision、worker concurrency、token/compute budget与tail SLO Not Disclosed。专家 setup <1h、final review约3h
  是三个案例的人工时间，不是端到端 system SLO。
- **What the Evidence Actually Proves:** author system展示了显式 role decomposition、async queue、persistent
  context 与 tournament feedback 的可运行组合；ablation 支持 external search 对 novelty grounding 和部分
  specialized agents 对作者指标有贡献；少量 expert-in-loop wet-lab提供“值得继续验证”的初步证据。
- **What It Does Not Prove:** 不证明系统自治完成科学发现、不证明 Elo 等于真实 hypothesis quality、不证明
  三个 biomedical cases 可跨领域外推，也不证明 multi-agent 本身优于等计算的强 single-agent baseline；
  in-vitro viability 不是 pre-clinical/clinical validation。
- **Limitations / Threats to Validity:** open-access literature遗漏付费 prior art 与 negative results；来源本身
  可错误/不可复现；模型 hallucination；Elo/self-judge circularity、small expert samples、revision混入更新模型；
  wet-lab 选择有人类筛选。paper明确验证仍 preliminary，可能 homogenize directions/加剧 reproducibility crisis。
- **Trade-offs / New Failure Modes:** 增加 exploration 与 restartability，却引入 queue starvation、duplicate
  work、stale tournament scores、Elo gaming/evaluator bias、context contamination、source poisoning、budget/
  stopping policy、artifact provenance、unsafe intermediate hypotheses 与责任边界；更多 agents 不等于独立证据。
- **Where the Previous Design Still Applies:** 单 agent+human review适合窄任务/低预算；确定性 pipeline适合
  regulated assays；人类 literature review/peer review 与 staged experiment仍是 epistemic gate，不可被 Elo 替代。
- **Evolution Relationship:** `Layering / Dependency`：long-running workflow 将 model/search/evaluator/memory/
  physical validation 组合；不是 frontier model capability 的单独升级，也不是 scientist replacement。
- **ROADMAP Node:** Ch77 主 owner；Ch73 memory、Ch74 tools、Ch75 planning、Ch76 multi-agent、Ch62 evaluation、
  Ch68 safety通过 handoff连接。
- **Target and Adjacent Chapters Read:** 已读 Ch62、Ch68、Ch71～80，并最终核对 Ch77 对
  scientific workflow、physical feedback、state/termination/evaluator risk 的描述。
- **Existing Coverage:** Ch77 已覆盖 durable workflow、human/physical gate 与 scientific-discovery案例；需在
  Evidence Gate 后检查是否准确区分 Supervisor authoritative state、Elo proxy 与实验 gate，删除任何“自治发现”
  或把 2026 revision 当 2025事实的表述。
- **Integration Decision:** `No Change — Already Covered`；Ch77 已有 evaluator-driven workflow、state lineage 与 human deployment authority。
  gate，不保留 vendor capability narrative。
- **Changed Files or Rejection Reason:** 不重复案例；保留在 Weekly 作为 scientific workflow 的受限 evidence。
- **Open Questions:** queue/lease/retry/idempotency contract、Elo calibration/independent verifier、claim-level
  provenance、safe intermediate-state policy、compute accounting、negative-result access与跨领域 replication。

## Evidence Level

- 官方 Blog / Release 只证明公开的产品、版本与项目事实；未公开实现标记为未知。
- arXiv v1 属于作者实验结论，默认 Status: Experimental，不等于独立复现或通用生产结论。
- 本周没有使用社区观点支撑机制结论；跨来源连接属于本项目推断，已通过 Evolution Relationship 标记。

## Cross-Week Deduplication

- 事件按 first-public date 归属本周；后续 revision、模型卡补充和工程集成回链本周，不重复创建新事件。
- 与前后周出现的同一技术只在年度索引建立演进关系，不把新版本写成对旧方案的静默替代。

## Knowledge Tree Position

- AI co-scientist → 第 62、74～78 章（Layering / Dependency）

## Recommended Action

- AI co-scientist：Worth Watching；不依据个案结果外推自治科研能力

## Event-Date Daily Decision

历史回填不创建 Daily。事件日期与 evidence boundary 直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 未保留旧内容重发、缺少 primary source 的转述、未绑定 workload contract 的 benchmark 宣传和纯产品可用性更新。
- discovery 数据库的相关性排序与引用量不作为 Technical Novelty 或 Source Reliability 的替代指标。

## Repository Changes

- 新增 papers/2025/weekly/2025-W08/README.md。
- 2025 Primary-Source Re-audit 进行中；本周尚未进入 Books Integration。

## Open Questions

- AI co-scientist 的持久状态、queue/retry、Elo calibration、provenance 与 safety contract 仍未完整公开。

## Sources

- AI co-scientist — https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/（First Public: 2025-02-19；Accessed: 2026-07-31）
- AI co-scientist paper — https://arxiv.org/abs/2502.18864（Paper v1: 2025-02-26；v2: 2026-06-29；Accessed: 2026-07-31）
