# AI Research Weekly — 2025-W27

> Coverage Window: 2025-06-30～2025-07-06
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 1 项长期证据：GLM-4.1V-Thinking。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：GLM-4.1V-Thinking（2025-07-01）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 本组无达到保留门槛的候选。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| GLM-4.1V-Thinking | 4 | 3 | 3 | 4 | 4 | 3 | 21/30 | Worth Watching；等待与后续 GLM-4.5 形成稳定链 |

### Deep Analysis 1 — GLM-4.1V-Thinking

- First Public: 2025-07-01
- Status: Official open model / technical report
- Primary Source: https://github.com/zai-org/GLM-V
- Evolution Relationship: Layering / Dependency

#### Why

多模态 reasoning 的系统成本来自视觉编码、长上下文、RL rollout 和工具环境的共同作用。

#### Principle and Mechanism

项目公开模型、报告与 reasoning/tool-use 支持；benchmark 仍是作者评测。

#### Trade-off and Evidence Boundary

开放权重改善复现与部署，但视觉 token、KV state 和多轮环境会使 activated parameter 不能代表端到端成本。

#### Connection and Evolution

知识树位置：第 23～25、29、62、74 章。Worth Watching；等待与后续 GLM-4.5 形成稳定链。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### GLM-4.1V-9B-Thinking

- **Candidate / Week / Score:** GLM-4.1V-9B-Thinking / 2025-W27 / 21/30。
- **Source Family ID:** `GLM-V-2507.01006`。
- **Source Type:** arXiv technical report、official model repository/weights。
- **First-public Date / Revision History:** arXiv v1 于 2025-07-01 公开；当前 HTML 已由后续 revision 合并 GLM-4.5V/4.6V，故本周判断只使用 v1 与 4.1V 明确归属的材料，不把后续模型能力倒灌为 4.1V 事实。
- **Direct Primary Sources:** arXiv:2507.01006 v1/PDF/HTML；`zai-org/GLM-V` 中 GLM-4.1V-9B-Thinking 的 model card、config 与使用说明。
- **Related Primary Sources:** GLM-4-9B-0414 base model、AIMv2 vision encoder；后续 GLM-4.5V 仅用于标注 revision/evolution。
- **Access and Verification Status:** Verified for paper-described mechanism and released artifacts；完整训练数据、reward model、RL code、cluster topology 与 production runtime Not Disclosed。
- **Full-read Coverage:** 已阅读 metadata/revision boundary、Introduction、architecture、pre-training data/recipe、SFT data/recipe、RL data/reward/RLCS/infra、42 项 evaluation setting、cross-domain ablation、limitations/conclusion，以及与 GUI、grounding、coding protocol 相关 appendix。
- **Original Problem:** 多模态模型若只在短答案或单领域任务上训练，难以把视觉感知、长链推理、GUI action、grounding 与长文档理解放进同一反馈学习过程。
- **Why the Previous Design Was Reasonable:** 大规模 image-text pretraining 加 SFT 能稳定建立视觉语义对齐；固定数据分布、短 CoT 与单域 RL 在任务窄、reward 稳定时更易控制。
- **Changed Constraint:** 多领域样本难度与模型能力不同且随训练变化；固定混合比例会让已学会样本继续消耗 rollout，过难样本又缺少有效 reward signal。
- **Mechanism:** 4.1V 采用 AIMv2-Huge vision encoder、MLP projector 与 GLM-4-9B-0414 decoder；SFT 只保留 long-CoT thinking data。RLCS 以各 domain/sample 的近期 reward success 估计难度，动态扩展可学习样本，并将 rule-based 与 model-based reward 按领域组合。
- **State Ownership:** data pipeline 拥有 domain/sample metadata；rollout/evaluator 拥有 response 与 reward；curriculum controller 拥有难度统计和 sampling distribution；trainer 只消费选中样本与 advantage，不能由 model 自己宣称任务已掌握。
- **Control Flow / Data Flow:** image/video/document → visual tokenization/projector → long-CoT SFT → multi-domain rollout → domain-specific verification/reward → curriculum statistic update → next sampling distribution → policy update。
- **Implementation Details:** image-text corpus 超过 10B pairs，使用 heuristic/CLIP threshold 与 recaptioning；video temporal downsampling 使用 3D convolution；RL sequence/load 在 data-parallel ranks 间平衡，并把 samples packing 到 32K，作者报告 repacking 约减半 forward/backward time。
- **Evaluation Setup:** 42 个公开 benchmark；推理由 vLLM/SGLang 执行，最大输出 8,192 tokens；单图上限约 6,144 visual tokens，视频约 48,000；不同 benchmark 使用各自 prompt/parser，另有 domain-combination ablation。
- **Baselines / Ablations / Sensitivity:** 与同尺寸 open/closed VLM 比较；报告 pretrain→SFT→RL stage 增益及 single-domain/mixed-domain RL 对比。没有公开 reward-model calibration、curriculum 阈值全量 sensitivity、独立复现或相同 harness 下的所有闭源 baseline。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 9B decoder、32K packing、visual/output token limits 披露；训练 GPU 型号/数量、precision、global batch、online concurrency 与 serving SLO Not Disclosed。
- **What the Evidence Actually Proves:** 在作者 pipeline 与 42-benchmark harness 下，动态 curriculum 能在多个 domain 同时产生正向训练信号，且 RL 不只改善 final-answer STEM；它还展示多模态 RL 的 sampling controller 是系统组件，而非单一 loss 公式。
- **What It Does Not Prove:** 不证明 long CoT 总优于 short/no CoT，不证明 mixed-domain RL 对 grounding/GUI 都有效，也不证明榜单差异来自 RLCS 而非 data、base model、prompt 或 evaluator。
- **Limitations / Threats to Validity:** outcome reward 可能强化错误过程；model reward 可被 exploit；训练配置敏感；视觉 clutter、occlusion、复杂空间关系仍弱；混域实验未改善部分 grounding/GUI；当前 HTML 混入后续模型，必须维持版本隔离。
- **Trade-offs / New Failure Modes:** dynamic sampling 减少无效 rollout，却新增 curriculum state、跨 domain reward calibration、滞后统计与 feedback-loop bias；long CoT 增加 token cost、truncation 与 plausible-but-wrong reasoning。
- **Where the Previous Design Still Applies:** 感知任务简单、答案短、rule verifier 缺失或 reward 不可比较时，pretraining+SFT、固定采样或单域 RL 仍更可控；non-thinking mode 也仍适合 latency-sensitive workload。
- **Evolution Relationship:** `Direct Evolution`：multimodal pretraining/SFT → domain-specific reasoning RL → curriculum-controlled multi-domain RL；不是“RL 替代视觉 pretraining”。
- **ROADMAP Node:** Ch18、Ch23～25、Ch29、Ch62；Ch14 作为 attention/data-flow 前置。
- **Target and Adjacent Chapters Read:** 已阅读 ROADMAP 对 Ch14、Ch18、Ch23～25、Ch27～30、Ch62 的边界，并复核相邻 Model/Training/Evaluation 章节；当前没有独立 VLM 章节 owner。
- **Existing Coverage:** 现有训练章节已覆盖 verifiable reward、reward hacking 与 sampling bias，Evaluation 已要求 harness contract；缺口在 multimodal curriculum 如何拥有跨领域 sampling state。是否值得进入 Books 要等同族与后续多模态证据交叉后决定。
- **Integration Decision:** `Weekly Only — Experimental Model Case`。
- **Changed Files or Rejection Reason:** 不改 Books；单一 VLM report 未形成超出现有 multimodal/training/evaluation contract 的稳定机制。
- **Open Questions:** v1 与后续 revision 的精确差异、RL cluster/precision/global batch、reward calibration、dynamic sampling sensitivity 与独立复现。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- GLM-4.1V-Thinking → 第 23～25、29、62、74 章（Layering / Dependency）

## Recommended Action

- GLM-4.1V-Thinking：Worth Watching；等待与后续 GLM-4.5 形成稳定链

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W27/README.md。
- 新增候选级 Full Source Review 并更正 first-public date；本阶段未修改 Books。

## Open Questions

- GLM-V 当前 HTML 合并多次 revision；Books Gate 前仍需核对 v1 diff，并决定跨领域 curriculum state 是否已有足够第二来源。

## Sources

- GLM-4.1V-Thinking — https://arxiv.org/abs/2507.01006（First Public: 2025-07-01；Accessed: 2026-07-31）
- GLM-V repository — https://github.com/zai-org/GLM-V（Accessed: 2026-07-31）
