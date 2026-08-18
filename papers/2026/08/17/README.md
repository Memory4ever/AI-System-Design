# Daily Research — 2026-08-17

**Date:** 2026-08-17  
**Timezone:** Asia/Shanghai  
**Research Window:** 2026-08-15 00:00～2026-08-17 23:59  
**Access Date:** 2026-08-17  
**Status:** Daily Complete；W33 Discovery/Evidence Gate Reopened；4 Full Source Reviews Complete；32 Discovery Review Pending；Books Gate Closed

## Executive Summary

今天最重要的发现不是单篇论文，而是研究流程本身出现了可验证的 recall failure：8 月 16 日 Daily 与最初生成的
W33 Weekly 没有取回 arXiv `recent` 页面中 8 月 14 日展示的批次。重新读取 `cs.AI → cs.CL → cs.LG → cs.DC`
后，确认其中存在多项 first-public date 属于 W33 的 AI System 候选。因此保留原 21 项 Full Source Review，撤回
“W33 发现已闭合”的结论，并把 W33 重新打开。

本轮先完成四篇高相关论文的正文级审计：QuoteBench 把 tool-use evaluation 从最终脚本扩展到
`generation contract × execution transport`；OmniScientist 把多模态科学工作流拆成 proposal、deterministic
transition、execution record 与 claim gate；Beyond Final Scores 用 trajectory evidence 分解长程 Agent 的过程质量；
AlayaWorld 展示 World Model memory 从静态图像/深度 warp 向 motion-aware latent 与 streaming point cache 的受限
演进。后三项的长期机制已由现有章节覆盖；QuoteBench 可能补足 Ch66，但必须等本次 W33 correction batch 完成
去重、相邻章节复核与 Books Gate 后再写入。

本日不生成 W34 Weekly，也不修改 Books。另有 32 个 source family 进入 Discovery Review queue；“被发现”不等于
“已评分”或“已全文审计”。

## 1. 模型与研究机构

### Source Coverage

按固定顺序复查 OpenAI、Anthropic、Apple ML Research、Google DeepMind、Google Research、Meta AI / FAIR、
Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、Ai2、Mistral、Qwen、DeepSeek、Kimi、
Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、Shanghai AI Lab、StepFun、Xiaomi MiMo、
InclusionAI 与 Hugging Face Blog 的官方 Research / News / model-card surface。

没有确认到 first-public date 位于 8 月 15～17 日、同时公开长期机制的新模型或机构事件。搜索结果中的旧发布、
后续转载与无 technical report 的产品能力不进入候选表。

### Candidate Scoring

本组没有 retained candidate。

## 2. arXiv / 学术来源

### Source Coverage

重新读取 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC` recent 全量页面，并用 Google Scholar、OpenAlex、DBLP、
Semantic Scholar 与 Hugging Face 作为发现、身份和重复关系的辅助入口。Crossref 只承担 Weekly metadata
交叉检验，不承担机制结论。回放确认 8 月 16 日扫描遗漏了 8 月 14 日展示批次；候选归属仍按 arXiv v1
first-public date，而不是展示日或本日发现日。

### Candidate Scoring

| Candidate | Event Date | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Evidence / Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| QuoteBench | 2026-08-13 | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | E2；Books Pending，owner Ch66，handoff Ch80 |
| Beyond Final Scores | 2026-08-13 | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | E2；No Change Ch66/Ch81 |
| OmniScientist | 2026-08-13 | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | E2；No Change Ch23/Ch66/Ch81 |
| AlayaWorld | 2026-08-13 | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | E2；No Change Ch25；Experimental source-family update |

### Discovery Review Queue

下列 32 项只完成 candidate identity 发现，尚未完成统一的 first-public/revision、跨分类去重、六维评分和全文审计；
它们不计入 W33 retained-row 总数，也不进入 Books：

| arXiv ID | Candidate | Likely Owner | Status |
| --- | --- | --- | --- |
| 2608.13517 | DFM Mimir v1 | `MODEL-*` / `TRAIN-*` | Discovery Review Pending |
| 2608.13515 | Measuring Task-Agnostic Training Data Influence | `TRAIN-DATA` | Discovery Review Pending |
| 2608.13520 | Data Geometry of Masking Diffusion | `MULTIMODAL-GENERATIVE-PARADIGMS` | Discovery Review Pending |
| 2608.13545 | LittleLearner | `TRAIN-*` | Discovery Review Pending |
| 2608.13538 | SAEVerbalizer | `MODEL-*` / `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.12888 | When Your Agent Opens the Chat App | `AGENT-TOOLS` / `PLATFORM-SECURITY` | Discovery Review Pending |
| 2608.12851 | Practice Makes Unsafe | `PLATFORM-SECURITY` / `AGENT-PLATFORM` | Discovery Review Pending |
| 2608.12847 | Query-Conditioned Reuse of Long-Horizon Agent Trajectories | `AGENT-MEMORY` | Discovery Review Pending |
| 2608.12932 | FlashDrive | `MULTIMODAL-EMBODIED-VLA` / `INFER-*` | Discovery Review Pending |
| 2608.12788 | ARAC | `PLATFORM-EVALUATION-SYSTEM` / `AGENT-WORKFLOW` | Discovery Review Pending |
| 2608.12585 | Reasoning Jury | `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.12720 | ERSkill | `AGENT-PROMPT` / `AGENT-PLATFORM` | Discovery Review Pending |
| 2608.12627 | EgoCITE | `MULTIMODAL-REPRESENTATION` / `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.12915 | InFactPlanner | `AGENT-PLANNING` | Discovery Review Pending |
| 2608.13076 | SPADE | `INFER-SPECULATIVE-DECODING` / `INFER-DISTRIBUTED` | Discovery Review Pending |
| 2608.13179 | Verifier-Bounded Credit Assignment | `TRAIN-RLHF` / `TRAIN-GRPO` | Discovery Review Pending |
| 2608.13173 | SkillShapley | `AGENT-PLATFORM` / `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.13120 | SkillEvo | `AGENT-PROMPT` / `AGENT-WORKFLOW` | Discovery Review Pending |
| 2608.13060 | VALG | `AGENT-WORKFLOW` / `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.13046 | BoardroomAI | `AGENT-MULTI-AGENT` | Discovery Review Pending |
| 2608.13043 | Local Mismatch to Global Impact | `MULTIMODAL-GENERATIVE-PARADIGMS` / `INFER-*` | Discovery Review Pending |
| 2608.12895 | Agent Behavioral Contracts II | `AGENT-WORKFLOW` / `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.12892 | Predictive Memory Localization | `AGENT-MEMORY` | Discovery Review Pending |
| 2608.13456 | Causal World Models survey | `MULTIMODAL-WORLD-MODELS` | Discovery Review Pending |
| 2608.13267 | Scientific-Figure Behavioral Evaluation | `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.13160 | TRAPSBench | `PLATFORM-EVALUATION-SYSTEM` / `PLATFORM-SECURITY` | Discovery Review Pending |
| 2608.12440 | Specification-First Convergence | `AGENT-WORKFLOW` | Discovery Review Pending |
| 2608.13410 | Who Speaks Matters | `AGENT-RAG` | Discovery Review Pending |
| 2608.13389 | TopoIntent | `AGENT-MULTI-AGENT` / `AGENT-PLANNING` | Discovery Review Pending |
| 2608.13459 | CAPRI | `AGENT-WORKFLOW` / `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |
| 2608.12322 | What Drives LLM Self-Reflection | `AGENT-REFLECTION` | Discovery Review Pending |
| 2608.12321 | LLMs Know the Constraint But Do Not Use It | `AGENT-PLANNING` / `PLATFORM-EVALUATION-SYSTEM` | Discovery Review Pending |

## Deep Analysis 1 — QuoteBench：Tool Evaluation 必须跨过 Execution Boundary

### Why → Principle

只检查模型生成的 Bash 是否“看起来正确”在单一 shell 中曾经合理；Agent runtime 增加 JSON、SSH、parser、
serializer 与 wrapper 后，同一字符串会经历多次解释。失败可能来自模型，也可能来自 transport 对 quoting、escaping
或 token boundary 的重写。最终 pass rate 无法告诉系统应修模型、prompt、parser 还是 interface。

### Mechanism

QuoteBench 用 56 个 one-shot Bash tasks 和 14 类 incident-derived operations，交叉 generation contract 与
execution transport；fixed-output replay 固定模型输出，只改变 parser/serializer/SSH path，从而隔离 post-generation
damage。比较 raw transport、额外 unescaped parser、真实 SSH 与 JSON serializer，并把 temporary script、typed
operation 作为替代边界。

### Trade-off / Evidence Boundary / Evolution

Typed tool 可以删除一层 shell quoting，却新增 payload/schema/version errors；contract-aware model 也可能通过补偿
掩盖不安全 transport，所以“分数相同”不等于“边界正确”。论文只覆盖构造的一次性 Bash 任务，不证明生产事故
发生率。长期路线是：final-output evaluation → layer-isolated replay → typed execution contract → end-to-end evidence。
Ch66 已有 EvalSpec 与 evidence chain，但是否缺少 `generation × transport` 的显式二维合同，待 correction batch 闭合后
联读 Ch65～66 与 Ch80 决定。

## Deep Analysis 2 — OmniScientist：科学 Agent 的 Authority 来自执行记录，不来自叙事

### Why → Principle

多模态科研工作流若让同一模型同时拥有观察、假设、实验、统计与成文 authority，会把 perception error、analysis
choice 与 post-hoc narrative 混成一个不可审计结论。旧的一次性 notebook 在短问题中合理；长程探索需要把 proposal
与 evidence ownership 拆开。

### Mechanism

系统将 raw evidence 分成 perceptual、symbolic、quantitative/statistical、procedural families，由 ideation、experiment、
writeup Agents 提案，deterministic pipeline 拥有 transition/backtracking。execution record 是数值 authority；idea、
rigour、claim checks 由代码约束；unsupported analyses 留在 trace，不升为 headline；multiple comparisons 统计所有尝试。

### Trade-off / Evidence Boundary / Evolution

固定 gate 降低 HARKing，却引入 schema coverage、judge bias、tool failure 与 pipeline rigidity。36 个案例、五类学科、
四类 evidence family 和 model-judge 实验只证明受限 workflow 可行性，不证明自主科学有效性。Ch23 的 representation
identity、Ch66 的 claim/evidence provenance 与 Ch81 的 deterministic commit gate 已覆盖这条机制，故目前 No Change。

## Deep Analysis 3 — Beyond Final Scores：过程指标是诊断证据，不是能力真值

### Why → Principle

长程 R&D task 的最终成功会压扁大量中间状态：同样失败可能源于错误 framing、执行不稳或 feedback control 无法
修正；同样成功也可能依赖高成本穷举。仅比较 outcome 不能指导 runtime、harness 或 training 改进。

### Mechanism

作者在 36 个长程任务、七个 frontier models 上，把轨迹拆成 Solution Framing、Execution、Feedback Control，并从
verifier outcome 与 recorded signals 计算 rule-based metrics；另做经验复用与 harness controlled comparison。

### Trade-off / Evidence Boundary / Evolution

过程指标改善 diagnosability，却可能把可记录行为误当 latent reasoning；harness 在该实验中主要改变 reliability，不能
外推为模型 ceiling。Ch66 已有 outcome + trajectory evidence 与 process decomposition，Ch81 已有 harness/runtime state，
因此本项为 No Change，不重复写入正文。

## AlayaWorld Source Review

AlayaWorld 保持 backbone、chunk-wise autoregressive scheme 与 training data 不变，只重构 conditioning/memory：
static-frame conditioning → motion-aware latent conditioning；depth-warp memory → streaming 3D point-cache renderer；
再以 causal encoding、pixel-aligned temporal window、hard memory dropout 与统一 VAE protocol约束 train/rollout/eval
identity。WBench 的 158 个 navigation cases 支持受限 consistency 改善，但其 temporal dynamics 并非全面领先。
Ch25 已有 action-conditioned transition、persistent/revisable world state、view-indexed memory 与 representation-contract
边界，故为 `No Change — Experimental Source-family Update`。

## 3. AI Infra 与工程项目

### Source Coverage

检查 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、
Transformers、Accelerate、DeepSpeed、Megatron-LM、MLX、llama.cpp、ONNX Runtime 与 OpenXLA 的 official
release / RFC / PR surface。未确认 8 月 15～17 日 first-public 且达到长期机制门槛的新工程事件。

### Candidate Scoring

本组没有 retained candidate。

## Evidence Level and Claim Boundary

- **E2 / Primary paper:** 四篇已审计论文覆盖 metadata/revision、Introduction/Related Work、Method、Implementation、
  Evaluation、ablation/sensitivity、limitations 与相关 Appendix/artifact；结论只在公开 workload contract 内成立。
- **E1 / Discovery identity:** 32 项 queue 只有 title/arXiv identity 与初步 owner，尚未形成机制结论。
- **Official fact:** 模型/工程页面仅用于确认是否存在 in-window release；没有公告反推内部机制。
- **Project inference:** owner 和演进关系来自论文与知识树联合判断，不是作者共同声明。
- 所有 benchmark 未披露的 hardware、model、precision、length、batch、concurrency、SLO 或 evaluator 字段均为
  `Not Disclosed`，不补猜、不跨论文拼接 headline。

## Knowledge Tree Position

| Candidate | Stable Owner | Current / Legacy | Adjacent Chapters Read | Decision |
| --- | --- | --- | --- | --- |
| QuoteBench | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Ch65、Ch66、Ch80 | Books Pending — correction Gate open |
| Beyond Final Scores | `PLATFORM-EVALUATION-SYSTEM` / `AGENT-WORKFLOW` | Ch66 / Ch81 | Ch66、Ch81 | No Change — Already Covered |
| OmniScientist | `MULTIMODAL-REPRESENTATION` / `PLATFORM-EVALUATION-SYSTEM` / `AGENT-WORKFLOW` | Ch23 / Ch66 / Ch81 | Ch23、Ch66、Ch81 | No Change — Already Covered |
| AlayaWorld | `MULTIMODAL-WORLD-MODELS` | Ch25 / Ch25 | Ch24、Ch25、Ch26 | No Change — Already Covered |

## Recommended Action

- 重开 W33 Discovery/Evidence Gate；保留原 21 项审计与 Books 修改，不把遗漏批次静默合并进“已完成”。
- 先对 32 项 queue 完成 identity/date/revision、跨分类/跨周去重与评分；所有 `20+` 项再完成 Full Source Review。
- correction evidence 全部闭合后，才对 QuoteBench 做 Ch66/Ch80 最终 Books Integration 判断。
- Monday 不生成 W34 provisional Weekly；今天不修改 Books、ROADMAP 或 DECISIONS。

## Ignored Noise

- recent-page 展示日不等于 event date；revision、cross-list 与同一 source family 不重复计分。
- 搜索摘要、Scholar/HF 热度、旧 release、营销 benchmark 与缺少 workload contract 的数字。
- 32 项 Discovery queue 的初步 owner 不是最终 disposition。

## Repository Changes

- 新增 `papers/2026/08/17/README.md`。
- 校正 8 月 16 日 Daily 的 discovery boundary，并重开 W33 Weekly gate。
- 更新 W33 Weekly 与年度索引的状态、发现队列、来源和未决问题。
- 更新 `docs/LEARNING_STATE.md`；Books、ROADMAP、DECISIONS 保持不变。
- 未 stage、commit、push、reset、checkout 或 clean。

## Open Questions

1. 32 项 queue 中哪些 first-public date 实际早于 W33，哪些是 cross-list/revision 或同一 source family？
2. QuoteBench 的 `generation contract × transport` 是否补足 Ch66 的长期机制缺口，还是只需增强现有 EvalSpec？
3. arXiv recent batch 的 Sunday scan 为什么未召回；自动化是否需要保存分类页 count 与 last-seen identifier？
4. OmniScientist 的 deterministic gates 在 schema 外实验、failed tool 与 human override 下如何保持 trace completeness？
5. World Model 的 geometric cache 怎样跨 camera calibration drift、dynamic objects 与 long-horizon compaction 验证？

## Sources

- arXiv cs.AI recent（访问 2026-08-17）: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent（访问 2026-08-17）: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent（访问 2026-08-17）: https://arxiv.org/list/cs.LG/recent
- arXiv cs.DC recent（访问 2026-08-17）: https://arxiv.org/list/cs.DC/recent
- QuoteBench, arXiv:2608.13547v1（2026-08-13；访问 2026-08-17）:
  https://arxiv.org/html/2608.13547
- OmniScientist, arXiv:2608.13558v1（2026-08-13；访问 2026-08-17）:
  https://arxiv.org/html/2608.13558
- AlayaWorld, arXiv:2608.13492v1（2026-08-13；访问 2026-08-17）:
  https://arxiv.org/html/2608.13492
- Beyond Final Scores, arXiv:2608.13417v1（2026-08-13；访问 2026-08-17）:
  https://arxiv.org/html/2608.13417
- OpenAI Research（访问 2026-08-17）: https://openai.com/research/
- Anthropic Research（访问 2026-08-17）: https://www.anthropic.com/research
- Google DeepMind publications（访问 2026-08-17）: https://deepmind.google/research/publications/
- Hugging Face Papers（访问 2026-08-17）: https://huggingface.co/papers
- vLLM releases（访问 2026-08-17）: https://github.com/vllm-project/vllm/releases
- SGLang releases（访问 2026-08-17）: https://github.com/sgl-project/sglang/releases
- KServe releases（访问 2026-08-17）: https://github.com/kserve/kserve/releases
