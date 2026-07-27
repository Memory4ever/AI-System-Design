# 2025 Weekly Research Index

> Coverage: 2025-W01～2025-W52
> Calendar Window: 2024-12-30～2025-12-28
> Backfilled: 2026-07-31
> Research Mode: Retrospective Backfill

## Archive Contract

- 使用 ISO week-year 和完整 Monday～Sunday。2025-W01 包含 2024-12-30～2025-01-05；
  2025-12-29～12-31 属于现有 2026-W01，不在本年度重复。
- 历史回填只生成 Weekly，不补造 Daily；事件日期、first-public date、来源和 evidence
  boundary 直接保留在对应周。
- 模型 release、paper v1、model card 与后续工程集成按不同证据角色记录；同一技术只形成一个
  Books source packet。
- Google Scholar、OpenAlex、DBLP 用于每日 discovery 和去重；Crossref 用于 Weekly
  metadata 交叉检查；机制结论回到 primary source。
- 2025 共 75 个评分条目，其中 32 个为 25～30 分、41 个为 20～24 分、2 个低于 20 分的
  Record Only 边界。新增的两项来自 Books 全文复核时纠正的 first-public 归属：Titans
  论文 v1 归入 W01，MIRAS 论文 v1 归入 W16；W49 只保留后续官方综合说明。

## Coverage Map

| Weeks | Calendar Window | Main Evidence Cluster |
| --- | --- | --- |
| W01～W05 | 2024-12-30～2025-02-02 | reasoning RL、hybrid/linear attention、test-time scaling、vLLM V1、research agents |
| W06～W13 | 2025-02-03～2025-03-30 | KV-constrained scheduling、native sparse attention、speculative decoding、Dynamo、interpretability/privacy |
| W14～W20 | 2025-03-31～2025-05-18 | multimodal/MoE model families、hybrid reasoning、compiler/runtime evolution、evaluator-driven agents、RAG sufficiency |
| W21～W26 | 2025-05-19～2025-06-29 | Kubernetes-native distributed inference、KServe/Gateway、user-level DP、long-reasoning co-design |
| W27～W33 | 2025-06-30～2025-08-17 | Kimi/GLM/Qwen agentic models、MTP/SpecForge、open-weight reasoning 与 safety |
| W34～W40 | 2025-08-18～2025-10-05 | hybrid model contracts、Kubernetes DRA、dual sparsity、NSA→DSA productization |
| W41～W46 | 2025-10-06～2025-11-16 | symmetric memory、policy-as-data safety、TPU backend portability、distributed DP runtime |
| W47～W52 | 2025-11-17～2025-12-28 | pipeline fusion、DeepSeek-V3.2、test-time memory、private telemetry、speculative artifact lifecycle |

## Cross-Week Evolution Routes

### Reasoning Training and Runtime Policy

```text
W04 DeepSeek-R1 / Kimi k1.5: outcome reward 与长 rollout
→ W05 s1: inference budget 也能成为能力杠杆
→ W09 Claude 3.7 / W18 Qwen3: thinking 与 non-thinking 合并为同一模型 contract
→ W16 o3/o4-mini: reasoning 中选择工具
→ W25 MiniMax-M1: attention architecture 与 RL rollout cost 联合设计
→ W34 DeepSeek-V3.1 / W49 V3.2: thinking state 进入 tool-use runtime
```

这条路线不是“RL 替代 SFT”。R1-Zero 暴露了纯 outcome optimization 的可读性边界，R1 的
cold start 与多阶段 pipeline 说明 SFT、筛选和偏好训练仍承担行为约束。后续 hybrid models
把训练收益转化为运行时 mode、reasoning budget、parser 与 capacity-planning 问题。

### Long Context and Memory

```text
W01 Titans: test-time neural memory
→ W03 MiniMax-01: hybrid linear/softmax attention
→ W07 Native Sparse Attention: trainable + hardware-aligned sparsity
→ W16 MIRAS: memory architecture / bias / retention / optimizer 设计空间
→ W25 MiniMax-M1: long context 与 long-reasoning RL co-design
→ W37 Qwen3-Next: hybrid attention + sparse MoE + MTP
→ W40 DeepSeek-V3.2-Exp: DSA 进入可服务模型
→ W49 DeepSeek-V3.2: sparse attention + tool reasoning
→ W49 Google Research synthesis: 对 W01/W16 的机构级解释与证据补强
```

这些分支解决不同问题：linear/recurrent state 控制随长度增长的成本，sparse attention 保留
选择性精确访问，test-time memory 允许在线更新参数化状态。它们分别引入压缩损失、稀疏
index/kernel 复杂度以及污染、遗忘、回滚和 session ownership。

### Speculative Decoding as an Artifact Lifecycle

```text
W10 EAGLE-3: draft architecture 与 training-time test
→ W29 SGLang MTP: draft/verify 进入 PD + EP runtime
→ W30 SpecForge: draft training 成为独立系统
→ W52 SpecBundle: target-specific draft weights 成为 versioned serving artifact
```

演进压力从“能否预测多个 token”转为 acceptance、verification cost、batch shape、训练数据、
target/draft compatibility、provenance 与持续重训。新工具链不改变 speculative decoding 在
高并发或低接受率场景可能失效的基本 trade-off。

### Distributed Inference Control Plane

```text
W05 vLLM V1: 单 engine 内统一 request/scheduler/execution state
→ W12 Dynamo: planner、router、KV transfer 与 telemetry
→ W21 llm-d: vLLM data plane + Kubernetes-native distributed stack
→ W22 KServe v0.15: multi-node/KV/autoscaling 进入声明式 API
→ W23 Gateway API Inference Extension: InferenceModel/Pool 与 endpoint selection
→ W35～W38 DRA: accelerator allocation、sharing 与 health 进入平台资源语义
```

单机 runtime、分布式 inference runtime、serving control plane、gateway 和 device scheduler
是分层依赖，不是互相替代。每上移一层都会获得更全局的决策信息，也会新增 freshness、
ownership、failure recovery、API lifecycle 与跨组件兼容性成本。

### Privacy from Algorithm to Operational Evidence

```text
W12 inference-time DP synthetic data
→ W21 user-level DP fine-tuning
→ W46 JAX-Privacy: clipping/noise/accounting/auditing 的 distributed runtime
→ W23 Urania paper / W50 Google Research follow-up: privacy-preserving usage telemetry
```

四个节点保护的 object 不同：query/record、user contribution、training pipeline、aggregate
usage insight。不能用“采用 DP”代替 privacy unit、threat model、epsilon/delta、accounting
和 utility boundary。

## Books Integration Gate

当前状态：`Books Integration Complete with 1 User-approved Unverified Exclusion`
（75/75 有 Source Review；74/75 full-primary-source verified；1/75 用户批准排除）。

此前结构检查只证明 52 个 ISO Weekly、75 个评分条目和 Markdown 归档完整，不能证明
原文阅读完成。75 个候选已完成历史建档和非模板化 Source Review；32 个高分、41 个中分与
2 个低分候选都已有逐项 evidence packet。Claude Opus 4.5 的官方 system-card PDF 虽可定位，
但当前来源通道因 11.5MB 文件体积限制无法阅读全文；用户于 2026-08-01 明确批准跳过，故它
保持 `User-approved exclusion / Unverified`，不计入全文核验数、不进入 Books，也不再阻塞其余
74 个候选。

已通过的归档检查：

- 52 个目录完整，ISO 周窗口连续覆盖 2024-12-30～2025-12-28；
- 75 个评分条目的分项和 Total 一致；
- 每周深入分析不超过 3 项，标题层级与代码围栏闭合；
- Sources 保留 URL、first-public date 与 accessed date；
- 性能/能力数字保持作者或厂商 evidence boundary，未脱离 workload contract 外推；
- Titans、MIRAS 与后发官方 Blog 的 first-public / follow-up 角色已纠正；
- 75/75 候选已有逐项 Source Review，74 项完成 full primary-source verification；
- 32/32 高分、40/41 中分与 2/2 低分候选完成核验；剩余 1 个中分候选按用户批准排除；
- 75/75 已获得最终 disposition：38 `Refine`、13 `No Change`、23 `Weekly Only`、1 `Excluded`；
- 目标及相邻章节已复核，所有 `Refine` 都有唯一主 owner 或明确 handoff。

Claude Opus 4.5 的全文缺口仍然存在，但已从年度 Gate 转为显式 exclusion。若未来重新纳入，
必须先阅读全文，再单独重开候选级 Books 判断；当前 Books 不包含该候选专属 claim。

## Candidate Disposition Ledger

此表列出全部 75 个评分候选的最终 disposition。`Complete` 表示 Source Review 与章节判断已完成，
不等于必须修改 Books；`Excluded / Unverified` 明确表示未完成全文核验且未进入 Books。

| Week | Candidate | Score | Source Review | Current Disposition |
| --- | --- | ---: | --- | --- |
| 2025-W01 | Titans: Learning to Memorize at Test Time | 27 | Complete | Refine — Existing Argument |
| 2025-W02 | vLLM 2024 Retrospective and 2025 Vision | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W03 | MiniMax-01 | 25 | Complete | Refine — Existing Argument |
| 2025-W03 | PRESERVE | 21 | Complete | Weekly Only — Experimental Hardware-specific Case |
| 2025-W04 | DeepSeek-R1 | 29 | Complete | Refine — Existing Argument |
| 2025-W04 | Kimi k1.5 | 27 | Complete | Refine — Existing Argument |
| 2025-W04 | Chain of Agents | 21 | Complete | No Change — Already Covered |
| 2025-W05 | vLLM V1 Alpha | 28 | Complete | Refine — Existing Argument |
| 2025-W05 | s1: Simple test-time scaling | 24 | Complete | Refine — Existing Argument |
| 2025-W05 | OpenAI deep research | 23 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W07 | Online Scheduling for LLM Inference with KV Cache Constraints | 24 | Complete | Refine — Existing Argument |
| 2025-W07 | Building AI for the pluralistic society | 20 | Complete | No Change — Already Covered |
| 2025-W07 | Native Sparse Attention | 27 | Complete | Refine — Existing Argument |
| 2025-W08 | AI co-scientist | 22 | Complete | No Change — Already Covered |
| 2025-W09 | Claude 3.7 Sonnet and Claude Code | 23 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W10 | EAGLE-3 | 26 | Complete | Refine — Existing Argument |
| 2025-W10 | Mistral OCR | 19 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W11 | Gemma 3 | 21 | Complete | No Change — Already Covered |
| 2025-W12 | Private prediction for large-scale synthetic text generation | 23 | Complete | Refine — Existing Argument |
| 2025-W12 | NVIDIA Dynamo | 27 | Complete | Refine — Existing Argument |
| 2025-W12 | SGLang joins PyTorch ecosystem | 20 | Complete | Weekly Only — Governance Fact |
| 2025-W13 | Gemini 2.5 Pro | 22 | Complete | Refine — Existing Argument |
| 2025-W13 | Tracing the thoughts of a large language model | 25 | Complete | Refine — Existing Argument |
| 2025-W14 | Llama 4 Scout and Maverick | 24 | Complete | No Change — Already Covered |
| 2025-W15 | Kimi-VL | 22 | Complete | Weekly Only — Experimental Model Case |
| 2025-W16 | OpenAI o3 and o4-mini | 24 | Complete | Weekly Only — Version/Product Fact |
| 2025-W16 | MIRAS — It’s All Connected | 26 | Complete | Refine — Existing Argument |
| 2025-W17 | PyTorch 2.7 | 23 | Complete | Weekly Only — Version/Product Fact |
| 2025-W17 | Kubernetes v1.33 | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W18 | Qwen3 | 26 | Complete | Refine — Existing Argument |
| 2025-W20 | AlphaEvolve | 25 | Complete | Refine — Existing Argument |
| 2025-W20 | Sufficient Context: A New Lens on RAG Systems | 25 | Complete | Refine — Existing Argument |
| 2025-W21 | llm-d community launch | 27 | Complete | No Change — Already Covered |
| 2025-W21 | Claude 4 | 22 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W21 | User-level differential privacy for LLM fine-tuning | 23 | Complete | Refine — Existing Argument |
| 2025-W22 | KServe v0.15 | 25 | Complete | No Change — Already Covered |
| 2025-W22 | DeepSeek-R1-0528 | 21 | Complete | Weekly Only — Version/Product Fact |
| 2025-W23 | Gateway API Inference Extension | 28 | Complete | No Change — Already Covered |
| 2025-W24 | Magistral | 21 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W25 | MiniMax-M1 | 26 | Complete | Refine — Existing Argument |
| 2025-W25 | Gemini 2.5 Pro/Flash GA | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W27 | GLM-4.1V-9B-Thinking | 21 | Complete | Weekly Only — Experimental Model Case |
| 2025-W28 | Kimi K2 release | 27 | Complete | Weekly Only — Version/Product Fact |
| 2025-W29 | SGLang Multiple Token Prediction integration | 25 | Complete | Refine — Existing Argument |
| 2025-W30 | Qwen3-Coder-480B-A35B-Instruct | 24 | Complete | Weekly Only — Version/Product Fact / Mechanism Partially Disclosed |
| 2025-W30 | SpecForge | 24 | Complete | Refine — Existing Argument |
| 2025-W31 | GLM-4.5 release | 25 | Complete | Weekly Only — Version/Product Fact |
| 2025-W31 | Kimi K2 technical report | 27 | Complete | No Change — Already Covered |
| 2025-W32 | gpt-oss-120b / gpt-oss-20b | 27 | Complete | Refine — Existing Argument |
| 2025-W32 | GPT-5 unified system | 24 | Complete | Refine — Existing Argument |
| 2025-W32 | GLM-4.5 technical report | 25 | Complete | No Change — Already Covered |
| 2025-W34 | DeepSeek-V3.1 | 25 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W35 | Kubernetes v1.34 DRA core GA | 26 | Complete | Refine — Existing Argument |
| 2025-W36 | Kubernetes DRA GA design details | 23 | Complete | Refine — Existing Argument |
| 2025-W37 | Qwen3-Next | 27 | Complete | Refine — Existing Argument |
| 2025-W38 | DRA resource health in Pod status | 22 | Complete | Refine — Existing Argument |
| 2025-W38 | DRA consumable capacity | 23 | Complete | Refine — Existing Argument |
| 2025-W39 | DeepSeek-V3.1-Terminus | 19 | Complete | Weekly Only — Version/Product Fact |
| 2025-W40 | DeepSeek-V3.2-Exp / DeepSeek Sparse Attention | 28 | Complete | Refine — Existing Argument |
| 2025-W42 | PyTorch 2.9 | 25 | Complete | Refine — Existing Argument |
| 2025-W44 | gpt-oss-safeguard | 24 | Complete | Refine — Existing Argument |
| 2025-W44 | SGLang-JAX | 25 | Complete | Refine — Existing Argument |
| 2025-W45 | Kimi K2 Thinking | 23 | Complete | No Change — Already Covered |
| 2025-W45 | SGLang Diffusion | 22 | Complete | No Change — Already Covered |
| 2025-W46 | JAX-Privacy 1.0 | 25 | Complete | Refine — Existing Argument |
| 2025-W47 | Gemini 3 | 22 | Complete | Weekly Only — Version/Product Fact |
| 2025-W47 | Real-time speech-to-speech translation | 23 | Complete | Refine — Existing Argument |
| 2025-W48 | Claude Opus 4.5 | 21 | Excluded / Unverified | User-approved exclusion / Unverified |
| 2025-W49 | DeepSeek-V3.2 | 29 | Complete | Refine — Existing Argument |
| 2025-W49 | Mistral 3 | 23 | Complete | Refine — Existing Argument |
| 2025-W49 | Google Research synthesis of Titans + MIRAS | 22 | Complete | No Change — Already Covered |
| 2025-W50 | Differentially private chatbot-use analytics | 25 | Complete | Refine — Existing Argument |
| 2025-W50 | GPT-5.2 | 22 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W51 | Gemini 3 Flash | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W52 | SpecBundle and SpecForge v0.2 | 24 | Complete | Refine — Existing Argument |

## Weekly Links

- [2025-W01](./2025-W01/README.md)
- [2025-W02](./2025-W02/README.md)
- [2025-W03](./2025-W03/README.md)
- [2025-W04](./2025-W04/README.md)
- [2025-W05](./2025-W05/README.md)
- [2025-W06](./2025-W06/README.md)
- [2025-W07](./2025-W07/README.md)
- [2025-W08](./2025-W08/README.md)
- [2025-W09](./2025-W09/README.md)
- [2025-W10](./2025-W10/README.md)
- [2025-W11](./2025-W11/README.md)
- [2025-W12](./2025-W12/README.md)
- [2025-W13](./2025-W13/README.md)
- [2025-W14](./2025-W14/README.md)
- [2025-W15](./2025-W15/README.md)
- [2025-W16](./2025-W16/README.md)
- [2025-W17](./2025-W17/README.md)
- [2025-W18](./2025-W18/README.md)
- [2025-W19](./2025-W19/README.md)
- [2025-W20](./2025-W20/README.md)
- [2025-W21](./2025-W21/README.md)
- [2025-W22](./2025-W22/README.md)
- [2025-W23](./2025-W23/README.md)
- [2025-W24](./2025-W24/README.md)
- [2025-W25](./2025-W25/README.md)
- [2025-W26](./2025-W26/README.md)
- [2025-W27](./2025-W27/README.md)
- [2025-W28](./2025-W28/README.md)
- [2025-W29](./2025-W29/README.md)
- [2025-W30](./2025-W30/README.md)
- [2025-W31](./2025-W31/README.md)
- [2025-W32](./2025-W32/README.md)
- [2025-W33](./2025-W33/README.md)
- [2025-W34](./2025-W34/README.md)
- [2025-W35](./2025-W35/README.md)
- [2025-W36](./2025-W36/README.md)
- [2025-W37](./2025-W37/README.md)
- [2025-W38](./2025-W38/README.md)
- [2025-W39](./2025-W39/README.md)
- [2025-W40](./2025-W40/README.md)
- [2025-W41](./2025-W41/README.md)
- [2025-W42](./2025-W42/README.md)
- [2025-W43](./2025-W43/README.md)
- [2025-W44](./2025-W44/README.md)
- [2025-W45](./2025-W45/README.md)
- [2025-W46](./2025-W46/README.md)
- [2025-W47](./2025-W47/README.md)
- [2025-W48](./2025-W48/README.md)
- [2025-W49](./2025-W49/README.md)
- [2025-W50](./2025-W50/README.md)
- [2025-W51](./2025-W51/README.md)
- [2025-W52](./2025-W52/README.md)

## Books Integration Summary

Status: Complete with 1 user-approved unverified exclusion（Claude Opus 4.5）。

本轮以 74 个已核验候选的 primary evidence 重新审查相邻章节；`Refine` 只表示候选补强或修正
了长期机制，不表示每个同族事件都重复生成一段正文。

| Evolution Route | Primary Weekly | Books Owner | Integrated Understanding |
| --- | --- | --- | --- |
| hybrid / sparse / test-time memory | W01、W03、W07、W16、W40、W49 | Ch22；Ch73 boundary | dense、linear/recurrent、hybrid、native sparse、DSA 与 neural memory 是不同约束下的分支；新增 selector、kernel、online state、隔离与恢复成本 |
| reasoning RL | W04 | Ch29 | pure RL 展示 emergence；cold start、筛选/SFT、第二阶段 RL 与 distillation 分别解决可读性、行为约束和部署成本，不互相覆盖 |
| speculative artifact lifecycle | W10、W29、W30、W52 | Ch44 | drafter 从独立小模型演进到 EAGLE-3、MTP、训练系统和 target-coupled bundle；收益受 acceptance、verification 与 workload 约束 |
| accelerator resource contract | W35、W36、W38 | Ch59 | DRA core GA、health alpha、consumable-capacity alpha 分层；driver、scheduler、admission 与 recovery 各有 owner |
| differential privacy stack | W12、W21、W46、W50 | Ch68 | privacy unit 从 record/query、user contribution 延伸到 distributed training runtime 与 production telemetry；DP 不是省略 threat model/accounting 的标签 |
| RAG control loop | W20 | Ch72 | relevance、context sufficiency、faithfulness 和 abstention 分开治理 |
| evaluator-driven search | W20 | Ch77 | evaluator、candidate lineage、evaluation cascade、diversity、held-out verification 与 human deployment authority 构成 Workflow，不等于模型自我改进 |
| interpretability evidence | W13 | Ch5 | probing→sparse replacement→attribution graph→原模型 intervention；更可读的图以 reconstruction、pruning 与 attention blind spot 为代价 |
| reasoning budget and rollout state | W04、W05、W18、W32 | Ch20、Ch29、Ch52 | stopping/effort、partial trajectory、route identity 与 serving capacity 是不同 owner 下的同一 compute contract |
| distributed runtime evolution | W05、W12、W42、W44 | Ch32、Ch45、Ch46、Ch48 | collective call、one-sided memory、backend portability、single-engine state 与 distributed paths 分层演进，不互相覆盖 |
| training resilience and distillation | W13、W49 | Ch24、Ch25 | elastic recovery 要保持 trajectory semantics；cascade distillation 用更多 lineage 换取更平滑的 teacher/student capacity gap |
| streaming pipeline fusion | W47 | Ch38 | cascade 的可替换/可诊断性与 end-to-end streaming 的 latency/voice continuity 共存；fusion 收紧 failure domain |

未写入的主要类别：

- Claude、Gemini、Gemma、Mistral、GPT、Qwen、Kimi、GLM 等产品/模型版本若没有公开的新机制，
  仅保留版本事实和 evidence boundary；
- llm-d、KServe 与 Gateway API 的长期分层原则已由 Ch48、Ch49、Ch58 覆盖；vLLM V1、Dynamo、
  PyTorch 2.9 与 SGLang-JAX 只把新的演进边界 refine 到 Ch46、Ch48、Ch32、Ch45；
- PRESERVE、Chain of Agents、AI co-scientist、Mistral OCR、pluralistic alignment 等候选仍受
  硬件、任务、评测或实现披露限制，保留为 Weekly evidence；
- 所有厂商 benchmark 与单篇论文实验均未升级为无条件生产结论。

Claude Opus 4.5 是唯一没有全文核验的候选，已按用户明确批准排除。除该 exclusion 外，
2025 的 74 个候选已完成 primary-source review、相邻章节复核和最终 disposition；没有把厂商
benchmark、后发报告或产品能力写成无条件事实。
