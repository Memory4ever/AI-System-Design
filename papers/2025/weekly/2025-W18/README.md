# AI Research Weekly — 2025-W18

> Coverage Window: 2025-04-28～2025-05-04
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Qwen3。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Qwen3（2025-04-29）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Qwen3 | 4 | 4 | 4 | 5 | 5 | 4 | 26/30 | Must Read；与 Claude 3.7、DeepSeek V3.1 形成 hybrid reasoning 演进链 |

### Deep Analysis 1 — Qwen3

- First Public: 2025-04-29
- Status: Official open-weight release
- Primary Source: https://qwenlm.github.io/blog/qwen3/
- Evolution Relationship: Direct Evolution

#### Why

用户既需要低延迟即时回答，也需要高预算 reasoning；如果为两种行为维护独立模型，会增加训练、部署与路由成本。

#### Principle and Mechanism

Qwen3 在同一模型中提供 thinking/non-thinking modes，并组合 dense/MoE 尺寸、长上下文与 reasoning post-training。

#### Trade-off and Evidence Boundary

统一模型减少 model fleet 分裂，却把 mode control、prompt format、budget accounting 和 capacity planning 变成 runtime contract；厂商 benchmark 不能证明所有 workload 的 Pareto 优势。

#### Connection and Evolution

知识树位置：第 20～24、29、45、46 章。Must Read；与 Claude 3.7、DeepSeek V3.1 形成 hybrid reasoning 演进链。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Qwen3

- **Candidate / Week / Score:** Qwen3 / 2025-W18 / 26/30。
- **Source Family ID:** `qwen3-2025-base-hybrid-reasoning`。
- **Source Type:** 官方 release blog、open-weight model cards/repository，以及后续 arXiv technical report。
- **First-public Date / Revision History:** Qwen3 weights/blog 2025-04-29；Technical Report arXiv v1 2025-05-14（属于 W20 的后续 evidence，但与 release 联读）；截至访问日 report 只有 v1。7 月 2507 variants 不反投影到本候选。
- **Direct Primary Sources:** Qwen3 release blog、QwenLM/Qwen3 repository、Qwen/Qwen3-235B-A22B model card。
- **Related Primary Sources:** Qwen3 Technical Report arXiv:2505.09388（35 页）；QwQ-32B和 Qwen2.5作为训练/架构前序。
- **Access and Verification Status:** Verified；release/model card 与 report 的 architecture、pretraining、全部 base/post-training evaluation、four-stage post-training及 references 已读。训练代码、RL stack与完整 artifact未公开。
- **Full-read Coverage:** metadata；architecture tables；data construction与三阶段 pretraining；15个 base benchmarks；long-CoT cold start、reasoning RL、thinking-mode fusion、thinking budget；model cards/chat templates；限制与未披露项。
- **Original Problem:** 独立 chat model 与 reasoning model 形成两个 weight fleet，带来训练、部署、路由、cache和版本治理成本；固定 reasoning depth又无法按任务复杂度控制 latency/cost。
- **Why the Previous Design Was Reasonable:** 独立模型避免 thinking/non-thinking behavior相互干扰，能为各自目标单独调优、容量规划和回归测试；简单请求无需承担长 CoT。
- **Changed Constraint:** 同一产品需要在即时响应与高 test-time compute之间动态切换，同时用 open-weight family覆盖从 0.6B dense 到 235B MoE 的部署规模。
- **Mechanism:** 先做 long-CoT cold start，再以3,995个 query-verifier pairs和 GRPO reasoning RL训练 thinking policy；随后用 thinking data（Stage 2 model rejection sampling）与 curated non-thinking data持续 SFT，通过 `/think`、`/no_think`和空 thinking block统一格式，最后做 general-domain RL。Thinking budget通过 early termination控制最大 reasoning tokens。
- **State Ownership:** model weights承载两种行为；chat template/host选择mode与budget；serving runtime拥有token budget、KV、admission和SLO。模型不拥有业务级budget policy。
- **Control Flow / Data Flow:** request + mode flag/budget → 同一 policy生成 hidden/visible thinking block → 达到终止条件或budget → final answer；训练链为 base → cold-start SFT → verifier reward rollouts/GRPO → mode-fusion SFT → general RL。
- **Implementation Details:** dense采用GQA、SwiGLU、RoPE、pre-RMSNorm，移除QKV bias并加入QK-Norm；MoE为128 experts、每token激活8个、无shared expert，并使用global-batch load-balancing loss。模型context table为32K或128K；release blog早期pretraining叙述32K extension与最终 model card需按具体checkpoint解释。
- **Evaluation Setup:** base model用15个general/reasoning/math/code/multilingual benchmarks，同一 pipeline与few-shot/CoT设置比较Qwen2.5、DeepSeek-V3、Gemma3、Llama3/4等；post-training含AIME、LiveCodeBench、CodeForces、BFCL等作者评测。Report未提供生产latency/cost测量。
- **Baselines / Ablations / Sensitivity:** report比较不同规模和dense/MoE baseline，并给thinking budget随token增加的趋势；没有完整mode-fusion ablation、budget-to-latency曲线、router/load-balance sensitivity或独立复现。AIME单次RL run从70.1到85.1只证明该recipe实例。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model sizes、experts、active params、context与pretraining tokens（约36T）披露；硬件、训练precision、global batch、rollout batch/并发、serving quantization、TTFT/TPOT和SLO为 `Not Disclosed`。作者只说large batch/high rollouts有利。
- **What the Evidence Actually Proves:** 一个open-weight policy可通过显式数据与template把thinking/non-thinking behaviors合并，并暴露推理budget control；在作者benchmark中不同budget表现有系统差异。
- **What It Does Not Prove:** 不证明单模型在所有 workload 都比双模型fleet便宜/更稳、thinking trace忠实、budget与质量单调于所有任务、MoE active params直接等于真实成本，或厂商benchmark可跨scaffold比较。
- **Limitations / Threats to Validity:** vendor-authored evaluation；训练hardware/precision/系统成本缺失；无mode interference与forgetting ablation；benchmark contamination和grader差异；report晚于release两周；后续2507改变checkpoint语义。
- **Trade-offs / New Failure Modes:** 合并fleet减少weight duplication与外部router，却新增mode adherence、prompt/template identity、budget enforcement、thinking token容量、错误早停、mode contamination和同endpoint latency bimodality；MoE另有expert routing/communication与hotspot。
- **Where the Previous Design Still Applies:** 强隔离SLO、独立安全策略、不同hardware/quantization、简单请求占绝大多数或需要可预测latency时，独立chat/reasoning models或host router仍合理。
- **Evolution Relationship:** 对QwQ/独立reasoning model为 `Direct Evolution`；对serving scheduler是 `Layering / Dependency`。它与Claude3.7/后续DeepSeek hybrid reasoning形成同一设计分支，不表示后者覆盖前者。
- **ROADMAP Node:** Ch20、Ch21、Ch23–25、Ch29、Ch45–46；长期主 owner 为Ch29（multi-stage reasoning training），mode/budget runtime只在Ch20/52做handoff。
- **Target and Adjacent Chapters Read:** Ch20–25、Ch28–30、Ch44–46已读。
- **Existing Coverage:** Ch29已写R1式pure RL→cold start→reasoning RL→general能力恢复，但尚需Books Gate判断Qwen3的“mode fusion + budget contract”是否构成不同机制；Ch20已覆盖sampling/stop不等同能力，Ch21已覆盖MoE成本边界。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch52，单 policy 双 mode 进入 route/effort/evaluation identity。
- **Changed Files or Rejection Reason:** 已更新 `books/part-04-inference-system/52-inference-scheduling.md`；不记录型号 benchmark。
- **Open Questions:** mode-fusion data比例与干扰、thinking budget训练目标、不同budget下calibration与SLO、MoE expert placement、rollout系统和general RL细节均未公开。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- Qwen3 → 第 20～24、29、45、46 章（Direct Evolution）

## Recommended Action

- Qwen3：Must Read；与 Claude 3.7、DeepSeek V3.1 形成 hybrid reasoning 演进链

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W18/README.md。
- 本周候选已完成 Source Review；Books Integration 仍受年度 Evidence Gate 约束。

## Open Questions

- 已完成 Qwen3 的 Books disposition；未来只在出现新机制、纠错证据或新的演进关系时重新开启审计。

## Sources

- Qwen3 — https://qwenlm.github.io/blog/qwen3/（First Public: 2025-04-29；Accessed: 2026-07-31）
- Qwen3 Technical Report — https://arxiv.org/abs/2505.09388（First Public: 2025-05-14；v1；Accessed: 2026-07-31）
- Qwen3 repository — https://github.com/QwenLM/Qwen3（Release family opened: 2025-04-29；Accessed: 2026-07-31）
- Qwen3-235B-A22B model card — https://huggingface.co/Qwen/Qwen3-235B-A22B（Accessed: 2026-07-31）
