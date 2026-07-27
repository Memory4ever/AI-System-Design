# AI Research Weekly — 2025-W31

> Coverage Window: 2025-07-28～2025-08-03
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：GLM-4.5、Kimi K2 technical report。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：GLM-4.5（2025-07-28 (release); 2025-08-08 (paper v1)）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 保留：Kimi K2 technical report（2025-07-28）。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GLM-4.5 | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Must Read；与 Qwen3/DeepSeek V3.1 比较 hybrid contract |
| Kimi K2 technical report | 5 | 4 | 4 | 5 | 5 | 4 | 27/30 | Must Read；Books 只形成一个 K2 source packet |

### Deep Analysis 1 — GLM-4.5

- First Public: 2025-07-28 (release); 2025-08-08 (paper v1)
- Status: Official open-weight release; report published later
- Primary Source: https://github.com/zai-org/GLM-4.5
- Evolution Relationship: Direct Evolution

#### Why

面向 agent 的模型开始把 reasoning、coding、tool use 与 non-thinking latency 放到同一 base model contract。

#### Principle and Mechanism

官方仓库披露 hybrid reasoning、MoE 尺寸、deployment paths 与 tool/reasoning parsers；论文 v1 在 W32，需分开记录。

#### Trade-off and Evidence Boundary

统一模型减少 fleet 分裂，却增加 parser compatibility、mode state、reasoning token 与引擎 feature matrix。作者排名不写成通用结论。

#### Connection and Evolution

知识树位置：第 20、21、29、45、46、74 章。Must Read；与 Qwen3/DeepSeek V3.1 比较 hybrid contract。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

### Deep Analysis 2 — Kimi K2 technical report

- First Public: 2025-07-28
- Status: arXiv v1; official technical report
- Primary Source: https://arxiv.org/abs/2507.20534
- Evolution Relationship: Layering / Dependency

#### Why

W28 的产品/权重事实需要报告补足 optimizer stability、训练数据、post-training 和 infrastructure boundary。

#### Principle and Mechanism

报告详细描述 MuonClip、MoE training、agentic data 与评测；这是对 W28 release 的证据补全，不是第二个独立模型事件。

#### Trade-off and Evidence Boundary

作者披露提升可审计性，但训练稳定性和 benchmark 仍需按实现、数据与硬件限定。

#### Connection and Evolution

知识树位置：第 21、24、29、32、45、74 章。Must Read；Books 只形成一个 K2 source packet。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### GLM-4.5 release

- **Candidate / Week / Score:** GLM-4.5 release / 2025-W31 / 25/30。
- **Source Family ID:** `GLM-4.5-2508.06471`（与 W32 technical report 联读）。
- **Source Type:** official repository/open weights/model cards/deployment documentation；technical report后发。
- **First-public Date / Revision History:** release 2025-07-28；technical report arXiv v1 2025-08-08。release事件只保留当时 artifact/interface事实，报告机制在 W32归档。
- **Direct Primary Sources:** `zai-org/GLM-4.5` release-time README、model cards/config/weights；official inference examples。
- **Related Primary Sources:** arXiv:2508.06471；Transformers/vLLM/SGLang model/reasoning/tool parser support用于compatibility核验。
- **Access and Verification Status:** Verified for released model sizes, modes, weights/license and documented deployment；training/post-training mechanism由W32 report补证，production SLA/failure data Not Disclosed。
- **Full-read Coverage:** 已阅读release/model cards的355B-A32B与106B-A12B variants、thinking/non-thinking contract、BF16/FP8 artifacts、parser/runtime matrix与GPU memory examples；对照后发报告标记release未公开机制。
- **Original Problem:** agent workload既需要复杂reasoning/tool use，也需要低latency direct response；若拆成多个独立model fleets，会增加routing、evaluation与version governance。
- **Why the Previous Design Was Reasonable:** 专用reasoning model与chat model各自优化清晰，mode不混淆；外部workflow可显式选model并控制cost。
- **Changed Constraint:** 同一产品希望共享base capability、tool protocol与deployment stack，同时按请求切换thinking budget；open weights还必须交付parser和runtime compatibility。
- **Mechanism:** release可确认hybrid reasoning的thinking/direct response两种公开模式、355B/32B-active与Air 106B/12B-active、base/hybrid/FP8 artifacts；23T training、loss-free balancing与RL流程只由W32 report证明。
- **State Ownership:** artifact registry拥有model/config/tokenizer；request policy拥有mode选择；runtime parser拥有reasoning/tool channel解释；workflow拥有tool authority。model文本不能自行改变mode或权限事实。
- **Control Flow / Data Flow:** request+mode policy → chat template/parser config → MoE serving → reasoning/direct response或tool proposal → workflow验证；release文档没有公开provider内部router。
- **Implementation Details:** official repo列出Transformers/vLLM/SGLang parser路径与最低GPU组合（如BF16 16×H100、FP8 8×H100的示例）；它们是deployment guidance，不是吞吐/SLO保证。
- **Evaluation Setup:** release汇总12项benchmark并形成overall score；model/precision/harness/scaffold异构，且无统一hardware、concurrency、length与latency contract。
- **Baselines / Ablations / Sensitivity:** release无controlled architecture/training ablation；两种mode也没有production routing误差或cost-quality curve。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model size、BF16/FP8 artifact和最低H100配置示例可核；batch/concurrency、input/output、TTFT/TPOT、network与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 证明同一open-weight family对外暴露mode contract并要求runtime/parser配套，形成“model artifact不是单一weights文件”的系统事实。
- **What It Does Not Prove:** 不证明统一hybrid model总优于双模型fleet，不证明FP8与BF16质量等价，不证明综合排名或GPU数量代表production efficiency。
- **Limitations / Threats to Validity:** repository当前包含后续GLM-4.6/4.7信息，必须版本隔离；release benchmark为作者评测；tool/reasoning parser兼容和外部runtime版本可能漂移。
- **Trade-offs / New Failure Modes:** 共享family减少fleet分裂，却新增mode/parser state、reasoning token成本、backend feature matrix、quantization parity与rolling upgrade coupling。
- **Where the Previous Design Still Applies:** SLO与行为隔离严格、traffic可预测或runtime不支持hybrid parser时，专用fast/reasoning model fleets仍更清晰。
- **Evolution Relationship:** `Direct Evolution`：separate chat/reasoning serving → one family with explicit mode contract；这不是内部统一router已公开的证据。
- **ROADMAP Node:** Ch20～21、Ch31、Ch45～48、Ch52、Ch74。
- **Target and Adjacent Chapters Read:** 已阅读 Ch19～22、Ch30～32、Ch44～48、Ch51～52、Ch73～75；主 owner 倾向model/runtime interface，待W32 mechanism packet后决定。
- **Existing Coverage:** Ch46～48已覆盖model config/parser/runtime contract，Ch52覆盖routing/cost；release主要补充Version/Product Fact，单独不足以修改核心设计结论。
- **Integration Decision:** `Weekly Only — Version/Product Fact`；与 W32 report 合并去重。
- **Changed Files or Rejection Reason:** 不改 Books；release 不独立驱动机制结论。
- **Open Questions:** release-time commit/model-card snapshot、mode contamination、FP8 parity、parser compatibility tests与production routing/SLO。

### Kimi K2 technical report

- **Candidate / Week / Score:** Kimi K2 technical report / 2025-W31 / 27/30。
- **Source Family ID:** `KIMI-K2-2507.20534`（与 W28 release同族）。
- **Source Type:** official arXiv technical report v1、v2 minor revision、weights/repository/artifacts。
- **First-public Date / Revision History:** arXiv v1 2025-07-28；v2 2026-02-03标为minor updates。历史结论以v1为准，v2只用于发现修订，不改变first-public。
- **Direct Primary Sources:** arXiv:2507.20534 v1 PDF/HTML与v2 revision；Kimi K2 base/instruct artifacts/repository。
- **Related Primary Sources:** Muon/Moonlight lineage、DeepSeek-V3 MLA/MoE/MTP lineage、公开agent benchmark harness。
- **Access and Verification Status:** Verified for full report and released artifacts；complete pretraining data、MuonClip/training code、RL environment implementation、kernel patches与independent reproduction unavailable。
- **Full-read Coverage:** 已阅读metadata/v1-v2 history、Introduction/architecture、MuonClip formula/ablation、pretraining data/recipe、distributed training/activation management、long-context extension、SFT/agentic data/RL、evaluation protocols与appendix、safety/known weaknesses/conclusion；并检查artifact config。
- **Original Problem:** 超大稀疏MoE在长训练中既要获得Muon的sample efficiency，又要避免attention logits爆炸；同时agent post-training需要可扩展environment和训练/rollout引擎切换。
- **Why the Previous Design Was Reasonable:** AdamW易理解且成熟；标准Muon改善矩阵参数更新；dense/GQA架构和独立训练/推理集群在较小scale下简化一致性与调度。
- **Changed Constraint:** 1T total参数、15.5T tokens、长context与MLA/MoE让optimizer数值稳定、activation memory、expert communication和rollout utilization共同成为约束。
- **Mechanism:** K2为1T/32B-active ultra-sparse MoE+MLA；MuonClip在Muon/weight decay/consistent RMS scaling之上监测attention logits并对Q/K updates做clip（threshold 100）；agentic post-training合成tool specs/agents/tasks/trajectories并在real/synthetic environments做joint RL。
- **State Ownership:** trainer拥有weights/optimizer与QK-clip statistic；data pipeline拥有15.5T corpus与agent specs；environment/verifier拥有outcome/reward；colocated runtime在training/rollout切换时必须维护权重版本与precision一致性。
- **Control Flow / Data Flow:** pretrain 4K context → MuonClip stability control → long-context stages（4K/32K并用YaRN到128K）→ SFT/agent data synthesis → environment rollout/self-critique rubric → group-relative RL + PTX regularization → checkpoint/artifact。
- **Implementation Details:** mid-scale 53B/9B-active ablation；H800 nodes每节点8 GPUs/NVLink/NVSwitch、inter-node 8×400Gbps RoCE；16PP×16EP+ZeRO-1，6TB parameter/gradient buffers跨256 GPUs；selective recompute、FP8-E4M3仅存activation并配FP32 scales、CPU offload、interleaved 1F1B overlap。训练用BF16参数/FP32 gradient accumulation。
- **Evaluation Setup:** non-thinking setting，通常最大output 8,192，SWE-bench 16,384；long-context测到128K；部分任务多次sampling或best-of-N内部verifier；agent benchmarks使用各自scaffold/environment，因此不能按单一harness横比。
- **Baselines / Ablations / Sensitivity:** 对MuonClip组件和attention-head选择做mid-scale study；64 heads相对更多heads权衡loss与128K inference FLOPs。未公开1T full-run optimizer对照、完整data ablation、RL environment/scaffold sensitivity或独立复现。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** pretraining topology/网络/precision/15.5T与global batch 67M tokens披露；serving hardware、batch/concurrency、TTFT/TPOT与SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者mid-scale实验中QK-Clip能抑制attention-logit增长；在K2 full run中作者报告零loss spike，并公开足够系统细节说明optimizer、parallelism、activation和context recipe协同，而非单一算法魔法。
- **What It Does Not Prove:** 不证明MuonClip普遍优于AdamW/其他stable optimizer，不证明零spike由它单独造成；agent benchmark不证明可靠自主性；vendor training efficiency不能外推到不同topology/kernel。
- **Limitations / Threats to Validity:** optimizer full-scale缺controlled baseline；data/RL代码不开放；activation FP8 storage与engine switching的一致性/容错边界未完整披露；agent模型会过度调用tool、产生未完成tool call，one-shot project可能弱于专用agent scaffold；safety judge具主观性。
- **Trade-offs / New Failure Modes:** ultra-sparse MoE降低active FLOPs却放大expert network与weight storage；MuonClip增加QK monitoring/control；activation压缩/offload节省HBM却引入precision与host bandwidth风险；colocation提高utilization却增加mode switch和版本一致性故障。
- **Where the Previous Design Still Applies:** 规模较小、network弱、稳定优先时dense/较小MoE+AdamW更简单；固定chat任务无需复杂agent environment；分离train/rollout clusters在故障隔离更重要时仍合理。
- **Evolution Relationship:** `Direct Evolution`：Muon → consistent scaling → QK-Clip；dense/less-sparse scaling → ultra-sparse MoE+MLA；SFT tool use → environment-grounded agent RL。三条链是layering，不是单一替代。
- **ROADMAP Node:** Ch21、Ch24、Ch29、Ch31～34、Ch45、Ch74～77。
- **Target and Adjacent Chapters Read:** 已阅读 Ch20～24、Ch28～35、Ch44～46、Ch73～77；需要在 Books Gate检查Ch21/32能否吸收“optimizer-control与topology协同”而不把K2写成产品案例堆叠。
- **Existing Coverage:** Ch21已有MoE routing/All-to-All；Ch32～34已有communication/PP；Ch29已有group-relative RL；长期新增点可能是optimizer数值control、activation storage precision与并行拓扑的共同稳定contract。
- **Integration Decision:** `No Change — Already Covered`；MoE、Muon、agentic post-training 与 serving contract 已在 Ch21/24/29/52/77 分层覆盖。
- **Changed Files or Rejection Reason:** 不改 Books；报告提供同族 evidence，但未改变这些章节的设计结论。
- **Open Questions:** v1-v2 exact diff、1T controlled optimizer baseline、checkpoint/recovery语义、engine switching protocol、agent data provenance与independent reproduction。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- GLM-4.5 → 第 20、21、29、45、46、74 章（Direct Evolution）
- Kimi K2 technical report → 第 21、24、29、32、45、74 章（Layering / Dependency）

## Recommended Action

- GLM-4.5：Must Read；与 Qwen3/DeepSeek V3.1 比较 hybrid contract
- Kimi K2 technical report：Must Read；Books 只形成一个 K2 source packet

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W31/README.md。
- 新增 2 个候选级 Full Source Review；本阶段未修改 Books。

## Open Questions

- GLM-4.5 release 与 W32 report 的最终主 owner 仍待 Books Gate。
- Kimi K2 的 optimizer、activation precision 与 topology 是一个联合稳定性 contract，需在 Ch21/32/34 之间选择唯一主 owner。

## Sources

- GLM-4.5 — https://github.com/zai-org/GLM-4.5（First Public: 2025-07-28 (release); 2025-08-08 (paper v1)；Accessed: 2026-07-31）
- Kimi K2 technical report — https://arxiv.org/abs/2507.20534（First Public: 2025-07-28；Accessed: 2026-07-31）
