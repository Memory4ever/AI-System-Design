# AI Research Weekly — 2025-W14

> Coverage Window: 2025-03-31～2025-04-06
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：Llama 4 Scout and Maverick。记录聚焦约束、机制、证据边界与演进关系，不收集一般新闻。

## Coverage Window and Limitations

- 以官方发布日期、GitHub Release 或 arXiv v1 归档；搜索收录日与后续修订不替代 first-public date。
- Google Scholar、OpenAlex、DBLP 用于 discovery 与去重；论文机制回到正文。Crossref 仅做 Weekly metadata 交叉检查。
- 历史回填不补造 Daily；Accessed 统一为 2026-07-31。
- benchmark 缺少模型、硬件、长度、batch/concurrency、precision/quantization 与 SLO 时不做通用结论。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描 OpenAI、Anthropic、Apple、Google、Meta、Microsoft、NVIDIA、xAI、Amazon、Cohere、Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、Seed、ERNIE、Hunyuan、Huawei Noah、InternLM、StepFun、MiMo、InclusionAI 与 Hugging Face Blog。

- 保留：Llama 4 Scout and Maverick（2025-04-05）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 发现与去重，回到 v1 正文核验；Crossref 只做 metadata 交叉检查。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按固定工程顺序扫描 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、Dynamo、TensorRT-LLM、Ray、KServe、Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、ONNX Runtime 与 OpenXLA。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Llama 4 Scout and Maverick | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；与 MoE/Long Context/Serving 联合复核 |

### Deep Analysis 1 — Llama 4 Scout and Maverick

- First Public: 2025-04-05
- Status: Official open-weight release; vendor evaluation
- Primary Source: https://ai.meta.com/blog/llama-4-multimodal-intelligence/
- Evolution Relationship: Direct Evolution

#### Why

原生多模态、长上下文与 MoE 容量扩展同时争夺训练数据、激活计算、显存和 serving kernel 支持。

#### Principle and Mechanism

Meta 公开 Scout/Maverick 的 MoE 结构、训练与上下文目标；系统事实以模型卡和权重为准，能力比较仍属厂商评测。

#### Trade-off and Evidence Boundary

较低 activated parameters 可降低每 token 计算，却不消除总权重存储、expert routing、跨卡通信和长上下文 KV 成本。

#### Connection and Evolution

知识树位置：第 21、22、23、45、46 章。Must Read；与 MoE/Long Context/Serving 联合复核。后续若进入 Books，必须保留旧方案仍成立的条件，并把作者实验、官方版本事实和本项目推断分开。

## Full Source Review

### Llama 4 Scout and Maverick

- **Candidate / Week / Score:** Llama 4 Scout and Maverick / 2025-W14 / 24/30。
- **Source Family ID:** `meta-llama4-scout-maverick-2025`。
- **Source Type:** 官方 launch Blog、官方 model cards、weights/config/inference repository。
- **First-public Date / Revision History:** 2025-04-05 发布；官方 repository v0.2.0 同日发布。没有公开的完整独立 technical report；model card 和 repo是当前最直接机制/部署证据，后续页面更新不得无标记覆盖 launch facts。
- **Direct Primary Sources:** Meta AI launch Blog；Meta-authored Scout/Maverick model cards；meta-llama/llama-models release/repository。
- **Related Primary Sources:** iRoPE 所引用 NoPE/attention-temperature工作、Llama 3.x model cards，仅用于机制背景与演进。
- **Access and Verification Status:** Verified for published architecture/config/deployment claims；training recipe、router、vision pipeline 与完整 eval protocol仅部分披露，未公开部分标记 `Not Disclosed`。
- **Full-read Coverage:** launch architecture/training/post-training/safety、model card metadata/evaluation/intended use、repo precision/GPU requirements、license/use-policy 与 release docs。
- **Original Problem:** dense模型将总容量与每 token compute绑定；原生多模态、10M context与开放部署又同时增加视觉 token、KV、权重和kernel压力。
- **Why the Previous Design Was Reasonable:** dense Llama 3.x / 128K context简化路由与expert communication；separate/adapted vision tower降低多模态预训练复杂度；在短上下文和中等模型上更易复现部署。
- **Changed Constraint:** 希望在约 17B active parameters下提供 109B/400B total capacity，并把 Scout context从128K目标推到10M，同时统一text/image pretraining。
- **Mechanism:** Scout为17B active / 109B total / 16 experts，Maverick为17B active / 400B total / 128 experts；模型卡说明 autoregressive MoE + early fusion。Scout预训练和后训练到256K，却通过 iRoPE（RoPE layers与无位置编码 attention layers交错）及 inference-time attention temperature scaling外推到10M。Maverick使用Behemoth teacher codistillation，soft/hard targets动态加权。
- **State Ownership:** router/expert weights拥有条件计算；vision/text tokens在early-fusion decoder共同演化；runtime拥有total-weight placement、expert dispatch、KV cache与quantization。10M可接受输入不等于runtime保证可用KV容量或有效检索。
- **Control Flow / Data Flow:** text + up to disclosed image inputs → early-fusion token stream → interleaved RoPE/NoPE attention + MoE layers → logits；deployment需load全部expert weights、每token激活子集并保留context KV。
- **Implementation Details:** Scout/Maverick model cards披露约40T/22T training tokens、knowledge cutoff 2024-08、context 10M/1M；Scout full BF16至少4 GPUs，official repo称FP8需2×80GB、INT4需1×80GB。Launch称Scout单H100仅在Int4条件，不能省略量化。
- **Evaluation Setup:** Meta报告text、code、reasoning、multimodal、long-context、safety与bias suites；Scout 10M主要以needle retrieval与code cumulative NLL支撑。部分chat arena结果使用experimental chat model，不能等同released checkpoint。
- **Baselines / Ablations / Sensitivity:** launch材料给出Llama 3与同类模型比较、codistillation收益和若干post-training choices；缺少统一公开的MoE router、iRoPE layer ratio、10M多证据reasoning、quantization/SLO ablation。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** deployment条件如上；10M Scout、1M Maverick；online batch/concurrency、KV dtype、TTFT/TPOT/P99未披露。单GPU fit只说明特定weight quantization memory可容纳，不包含任意KV/workspace/concurrency。
- **What the Evidence Actually Proves:** released weights/config与官方材料证明两种MoE规模、early fusion、context/interface和受限hardware fit；厂商实验在其条件下支持length generalization与能力claims。
- **What It Does Not Prove:** 不证明10M上下文可在单H100满足production SLO，不证明needle/NLL等同多证据推理，不证明17B active带来dense 17B的memory/communication成本，也不证明experimental arena model等同released model。
- **Limitations / Threats to Validity:** 无完整technical report；vendor evaluation、未完整披露prompt/scaffold/serving contract；MoE router/parallel strategy不透明；10M训练长度与inference window不一致；license非OSI open source。
- **Trade-offs / New Failure Modes:** active compute与total capacity解耦换来expert weight placement、all-to-all与小batch效率；iRoPE extrapolation换来位置/attention sensitivity；10M context导致KV/TTFT/capacity爆炸；early fusion扩大data/contamination与modality balance问题。
- **Where the Previous Design Still Applies:** short-context、低延迟、有限GPU或runtime不支持Llama4 MoE/mixed attention时，dense/128K/separate vision adapter仍更简单可靠。
- **Evolution Relationship:** `Direct Evolution`：Llama 3.x dense/128K → Llama 4 MoE/early fusion/iRoPE；不是“10M替代RAG”或“MoE否定dense”。
- **ROADMAP Node:** 主 owner第21章；第22、23、45、46章为hand-off。
- **Target and Adjacent Chapters Read:** 已读第20章 Sampling、第21章 MoE、第22章 Long Context；核对第23、45、46章部署/数据边界。
- **Existing Coverage:** 第21章已完整覆盖total/active parameters、routing/all-to-all与“active不等于end-to-end cost”；第22章已覆盖窗口/有效利用/KV/SLO分离。因此候选主要提供受限案例，是否需要正文取决于全年MoE/long-context演进是否缺少mixed-position外推分支。
- **Integration Decision:** `No Change — Already Covered`；Ch21/22 已覆盖 active-vs-total cost 与 long-context contract。
- **Changed Files or Rejection Reason:** 不改 Books；公开报告只增加受限模型实例。
- **Open Questions:** iRoPE layer ratio和temperature calibration；10M下真实KV layout/quantization与P99；released checkpoint与experimental chat eval差异；multi-image数量和context竞争。

## Evidence Level

- 官方 Blog / Release 只证明公开事实；未公开实现保持未知。
- arXiv v1 默认 Status: Experimental；作者实验不等于独立复现。
- 跨来源连接是本项目推断，以 Evolution Relationship 标记。

## Cross-Week Deduplication

- 同一技术后续 revision 与工程集成回链首次公开周。
- 新版本不覆盖旧方案；年度索引记录 old constraint → new mechanism → new failure mode。

## Knowledge Tree Position

- Llama 4 Scout and Maverick → 第 21、22、23、45、46 章（Direct Evolution）

## Recommended Action

- Llama 4 Scout and Maverick：Must Read；与 MoE/Long Context/Serving 联合复核

## Event-Date Daily Decision

历史回填不创建 Daily；事件与证据边界直接保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略旧内容重发、二手转述、缺条件 benchmark 与纯可用性更新。
- discovery 排名和引用量不替代 novelty、reliability 或 longevity。

## Repository Changes

- 新增 papers/2025/weekly/2025-W14/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- Llama 4 的最终 disposition 等全年 MoE / Long Context sources 联合去重后决定。

## Sources

- Llama 4 Scout and Maverick — https://ai.meta.com/blog/llama-4-multimodal-intelligence/（First Public: 2025-04-05；Accessed: 2026-07-31）
- Llama 4 Scout model card — https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct（Release: 2025-04-05；Accessed: 2026-07-31）
- Llama models repository / Llama 4 inference requirements — https://github.com/meta-llama/llama-models（Accessed: 2026-07-31）
- Llama models v0.2.0 — https://github.com/meta-llama/llama-models/releases/tag/v0.2.0（Release: 2025-04-05；Accessed: 2026-07-31）
