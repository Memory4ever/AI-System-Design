# Daily Research — 2026-09-17

**规范：** V3
**窗口：** 2026-09-16T09:00:00+08:00 ～ 2026-09-17T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-21T11:56:18+08:00

## 1. 结论

本窗完成 14 个 Daily 来源的定点检查。13 个机构源没有发现能够同时确认落窗、属于当前项目范围且提供长期机制增量的新材料；OpenAI 有两条仅标注 `2026-09-16` 的公告与窗口相交，但官方页没有提供可证明落在本窗内的时刻，其中经济研究又属于当前范围外，故均未冒充当窗候选。arXiv 当日列表跨 12 个目标分类去重后得到 514 个身份；完成标题范围判断后，对 116 个含义不明确或可能相关的家族阅读完整摘要。作者初筛保留的 42 项中，17 项已经由前一日报按 `2026-09-16T08:00:00+08:00` 的官方公告归属完成审阅，本日按跨日重复关闭、不重复评分；因此本窗候选分母冻结为 25 个材料家族（4.9%）。其余条目已经在[筛选记录](../_sources/daily-20260917/screening-ledger.md)按身份关闭，没有把“属于 AI”或“能映射章节”当作准入理由。

本窗最重要的变化集中在四条链路：第一，执行计划需要把真实生成轨迹、硬件语义和端到端验收连在一起，而不能从局部 synthesis 或单项 kernel 数字推出系统正确性；第二，状态优化必须保留语义身份与提交边界，涵盖长期 Agent memory、embedding 迁移、KV eviction 与 evidence materialization；第三，训练与 Agent workflow 要把 backward transport、temporal credit、interrupt/resume 和 effect provenance 放进各自的控制合同；第四，多模态 world model 的评价重点继续从视觉逼真度转向可控干预、action-conditioned transition 与真实闭环收益。

25 个本窗候选均已完成相应版本的证据审阅：22 个达到深入审阅，3 个按标准审阅。13 个长期语义增量已按唯一 owner 合并写入机制正文，另外 12 个由现有论点完整承载；写入依据见[精确 Books 队列](../_sources/daily-20260917/books-queue.md)。当前只待非作者执行 fresh-context 语义复核，复核通过后报告才能改为“完成”。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 检查 Research 索引与 2026-09-16 官方发布；最新 Research 索引项早于窗口。两条 9 月 16 日页面仅给日期，无法证明落在 09:00 后 | 已检查 | `model-misalignment-reporting-framework` 缺精确发布时间；隔离为日期保留项。经济研究已按范围关闭 |
| SRC-ANTHROPIC | 检查 Research 列表相邻日期；9 月 17 日 Science 条目没有可证明早于本窗终点的时刻，且属于暂缓的 AI for Science | 已检查 | 无 |
| SRC-GOOGLE-AI | 检查 DeepMind / Google Research 发布列表；相邻可见条目早于窗口 | 已检查 | 无 |
| SRC-META-AI | 检查 FAIR / AI Research 发布入口；未见可确认落窗的项目相关新材料 | 已检查 | 无 |
| SRC-QWEN | 检查官方 Blog 的相邻发布；未见可确认落窗的新研究事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 检查官网 Research / 官方仓库发布入口；未见可确认落窗的新研究事件 | 已检查 | 无 |
| SRC-MOONSHOT | 检查 Kimi Platform Blog 与官方仓库相邻发布；未见落窗事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | 检查 Research 页“全部”列表及官方仓库相邻事件；未见落窗事件 | 已检查 | 无 |
| SRC-ZAI | 检查官方 Research 目录、发布说明与仓库相邻事件；未见落窗事件 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | 检查 Research、Public Papers 与官方仓库相邻事件；未见落窗事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 检查 ERNIE 技术博客与官方仓库相邻事件；未见落窗事件 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 检查 MiMo 论文页与官方仓库相邻事件；未见落窗事件 | 已检查 | 无 |
| SRC-MINIMAX | 检查中英文 Blog、Agent Tech Blog 与官方仓库相邻事件；未见落窗事件 | 已检查 | 无 |
| SRC-ARXIV | 扫描 `cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA` 当日列表；跨分类去重后 514 个身份，116 个读完整摘要；42 个初筛保留项中 17 个由 09-16 日报拥有，跨日去重后本窗保留 25 个候选 | 已检查 | 一篇候选 HTML 不可用，已用同版本摘要与 PDF 定点恢复；无待执行缺口 |

## 3. 候选与判断

以下候选公开时间均为 `2026-09-17T08:00:00+08:00`；v1 的较早 submitted 字段只记录投稿，不改变首次公开归属。另有 17 个列表命中已由 09-16 日报按其官方首次公告归属闭合，不在下表重复评分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Latent Undertow](https://arxiv.org/abs/2609.15994v1) | 2026-09-17T08:00:00+08:00 | hidden-state probe 对普通拼写扰动并不稳健，且 KV suffix fork 可利用扰动衰减恢复检测；3+3+2=8 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Immutable Past](https://arxiv.org/abs/2609.16073v1) | 2026-09-17T08:00:00+08:00 | mutable RAG 的旧事实不是更多 top-k 可解决的问题，而需要 temporal dominance 与 contradiction GC；3+3+2=8 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Z-Loss Backward Geometry](https://arxiv.org/abs/2609.16179v1) | 2026-09-17T08:00:00+08:00 | 相同 forward penalty 可经 head/router、tied embedding、reduction 与 optimizer 传输成不同更新；3+2+2=7 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Anatomy of Associative Recall](https://arxiv.org/abs/2609.16183v1) | 2026-09-17T08:00:00+08:00 | matched-state 分解把 recurrence 类别差异收窄为 convolution、transition 与 curriculum/interference；3+2+3=8 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [The World Model Hardware Accelerator](https://arxiv.org/abs/2609.16244v1) | 2026-09-17T08:00:00+08:00 | diffusion 的静态 shape/step schedule 改变 accelerator 的控制流与语义验收契约；3+2+2=7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Early-Bird Decoding](https://arxiv.org/abs/2609.16450v1) | 2026-09-17T08:00:00+08:00 | dLLM 用 learnable variable block 与 position-aware parallel unmasking提前提交低熵簇；2+3+2=7 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [On the Importance of Gating](https://arxiv.org/abs/2609.16540v1) | 2026-09-17T08:00:00+08:00 | SSM 的短上下文 memorization 与长上下文 ICL 可分离，gating 决定是否走捷径；3+2+3=8 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Divergence Timing and Cumulative Disagreement under KV-Cache Eviction](https://arxiv.org/abs/2609.16617v1) | 2026-09-17T08:00:00+08:00 | KV eviction 的累计误差应从首次 divergence 分解，而非只看最终答案或局部 token；2+2+2=6 | 标准完成 | 已有覆盖：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [DeepShare](https://arxiv.org/abs/2609.16682v1) | 2026-09-17T08:00:00+08:00 | 多租户 GPU sharing 把 deficit、reclaimability、预测式抢占与 interference placement 置于同一 assurance contract；3+3+2=8 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER` [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [World Models for Embodied Intelligence](https://arxiv.org/abs/2609.16697v1) | 2026-09-17T08:00:00+08:00 | Plausible→Controllable→Actionable 把 world model 评价从视频逼真度推进到干预与行为收益；3+3+3=9 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [The Latent That Never Was](https://arxiv.org/abs/2609.16745v1) | 2026-09-17T08:00:00+08:00 | ACT 的 CVAE ablation 复跑没有支持原有 drop，暴露 latent 使用与训练预算混淆；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Embedding Backward Compatibility](https://arxiv.org/abs/2609.16875v1) | 2026-09-17T08:00:00+08:00 | 新 embedding 不能只追求新空间效果，还要显式保留旧库可比性与迁移 contract；3+3+2=8 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [OptiPrime](https://arxiv.org/abs/2609.16898v1) | 2026-09-17T08:00:00+08:00 | private inference 的 protocol choice、encoding、memory movement 与 accelerator 不能分层独立优化；3+3+2=8 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Reward-Compatible Temporal Credit](https://arxiv.org/abs/2609.16937v1) | 2026-09-17T08:00:00+08:00 | token-local on-policy distillation 与 sequence reward 的时间归因不一致，需要 reward-compatible temporal mixing；3+2+3=8 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [FlexEE](https://arxiv.org/abs/2609.17008v1) | 2026-09-17T08:00:00+08:00 | offloading 下 early exit 必须同时满足 KV compatibility 与 lossless verification 才能减少层执行和权重搬运；3+3+2=8 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [EviScope](https://arxiv.org/abs/2609.17081v1) | 2026-09-17T08:00:00+08:00 | paired counterfactual evidence 将正确答案拆成 support、conflict、abstention 与 source-use 行为；2+3+2=7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [After the Party](https://arxiv.org/abs/2609.17274v1) | 2026-09-17T08:00:00+08:00 | skill registry 的 privilege 证据普遍存在，且三个 scanner 在 61,990 项上的敏感度和判定严重分歧；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Mo' Models, Mo' Problems](https://arxiv.org/abs/2609.17306v1) | 2026-09-17T08:00:00+08:00 | 扩大异构模型池可能使 MAS 低于最强单模型，同族选择比盲目 diversity 更稳；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Where Should a Document Live](https://arxiv.org/abs/2609.17346v1) | 2026-09-17T08:00:00+08:00 | context、KV representation 与 parameter adaptation 形成准确率、压缩、检索和遗忘的条件分支，不存在单一赢家；3+3+2=8 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [XPACE](https://arxiv.org/abs/2609.17372v1) | 2026-09-17T08:00:00+08:00 | shared video backbone 联合 action prediction 与 simulation，并用自生成 recovery 轨迹反哺 policy；3+3+2=8 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Belief State Geometry In-Context](https://arxiv.org/abs/2609.17376v1) | 2026-09-17T08:00:00+08:00 | HMM 控制环境中的线性可解码与 steering 干预支持 ICL 近似 belief-state update，但外推受限；2+2+2=6 | 标准完成 | 已有覆盖：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [SlotDiT](https://arxiv.org/abs/2609.17414v1) | 2026-09-17T08:00:00+08:00 | object-centric slot 把 diffusion latent 从像素/VAE 压缩推进到显式实体状态并改善机器人任务完成率；3+2+2=7 | 深入完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Never Stop Thinking](https://arxiv.org/abs/2609.17416v1) | 2026-09-17T08:00:00+08:00 | continuous-time Agent 需要 interrupt/resume orchestration，且 judge reward 会反向伤害真实完成，verifiable shaped reward 才有效；3+3+3=9 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [World Model Science](https://arxiv.org/abs/2609.17419v1) | 2026-09-17T08:00:00+08:00 | 长时 Agent 需用 trajectory dynamics 诊断 local-valid/global-wrong、stress avalanche 与 metastable belief，而非只看 terminal reward；3+3+2=8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PhysStream](https://arxiv.org/abs/2609.17521v1) | 2026-09-17T08:00:00+08:00 | streaming video generation 用 online structured scene memory 与 velocity increment 实现 mid-generation physical control；3+2+2=7 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

逐项证据位置、机制、实验合同、未证明内容与 owner 比较见[证据笔记](../_sources/daily-20260917/evidence-notes.md)；Books 的串行写入顺序见[Books 队列](../_sources/daily-20260917/books-queue.md)。这里仅保留三条跨材料演进关系。

### [Latent Undertow](https://arxiv.org/abs/2609.15994v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：hidden-state probe 对普通拼写扰动并不稳健，且 KV suffix fork 可利用扰动衰减恢复检测。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [The Immutable Past](https://arxiv.org/abs/2609.16073v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：mutable RAG 的旧事实不是更多 top-k 可解决的问题，而需要 temporal dominance 与 contradiction GC。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Z-Loss Backward Geometry](https://arxiv.org/abs/2609.16179v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：相同 forward penalty 可经 head/router、tied embedding、reduction 与 optimizer 传输成不同更新。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Anatomy of Associative Recall](https://arxiv.org/abs/2609.16183v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：matched-state 分解把 recurrence 类别差异收窄为 convolution、transition 与 curriculum/interference。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [The World Model Hardware Accelerator](https://arxiv.org/abs/2609.16244v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：diffusion 的静态 shape/step schedule 改变 accelerator 的控制流与语义验收契约。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Early-Bird Decoding](https://arxiv.org/abs/2609.16450v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：dLLM 用 learnable variable block 与 position-aware parallel unmasking提前提交低熵簇。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [On the Importance of Gating](https://arxiv.org/abs/2609.16540v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：SSM 的短上下文 memorization 与长上下文 ICL 可分离，gating 决定是否走捷径。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Divergence Timing and Cumulative Disagreement under KV-Cache Eviction](https://arxiv.org/abs/2609.16617v1)

采用 arXiv v1 并按 `标准完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：KV eviction 的累计误差应从首次 divergence 分解，而非只看最终答案或局部 token。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [DeepShare](https://arxiv.org/abs/2609.16682v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：多租户 GPU sharing 把 deficit、reclaimability、预测式抢占与 interference placement 置于同一 assurance contract。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [World Models for Embodied Intelligence](https://arxiv.org/abs/2609.16697v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：Plausible→Controllable→Actionable 把 world model 评价从视频逼真度推进到干预与行为收益。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [The Latent That Never Was](https://arxiv.org/abs/2609.16745v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：ACT 的 CVAE ablation 复跑没有支持原有 drop，暴露 latent 使用与训练预算混淆。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Embedding Backward Compatibility](https://arxiv.org/abs/2609.16875v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：新 embedding 不能只追求新空间效果，还要显式保留旧库可比性与迁移 contract。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

Books owner 校正为 `AGENT-RAG`：具体落在 Ch76「Embedding Upgrade 是兼容性迁移，不只是新空间更准确」，与 freshness/index lifecycle 相接；Ch12 只保留 token/sentence embedding 边界和 handoff。

### [OptiPrime](https://arxiv.org/abs/2609.16898v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：private inference 的 protocol choice、encoding、memory movement 与 accelerator 不能分层独立优化。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Reward-Compatible Temporal Credit](https://arxiv.org/abs/2609.16937v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：token-local on-policy distillation 与 sequence reward 的时间归因不一致，需要 reward-compatible temporal mixing。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [FlexEE](https://arxiv.org/abs/2609.17008v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：offloading 下 early exit 必须同时满足 KV compatibility 与 lossless verification 才能减少层执行和权重搬运。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [EviScope](https://arxiv.org/abs/2609.17081v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：paired counterfactual evidence 将正确答案拆成 support、conflict、abstention 与 source-use 行为。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [After the Party](https://arxiv.org/abs/2609.17274v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：skill registry 的 privilege 证据普遍存在，且三个 scanner 在 61,990 项上的敏感度和判定严重分歧。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Mo' Models, Mo' Problems](https://arxiv.org/abs/2609.17306v1)

采用 arXiv v1 并按 `标准完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：扩大异构模型池可能使 MAS 低于最强单模型，同族选择比盲目 diversity 更稳。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Where Should a Document Live](https://arxiv.org/abs/2609.17346v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：context、KV representation 与 parameter adaptation 形成准确率、压缩、检索和遗忘的条件分支，不存在单一赢家。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [XPACE](https://arxiv.org/abs/2609.17372v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：shared video backbone 联合 action prediction 与 simulation，并用自生成 recovery 轨迹反哺 policy。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Belief State Geometry In-Context](https://arxiv.org/abs/2609.17376v1)

采用 arXiv v1 并按 `标准完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：HMM 控制环境中的线性可解码与 steering 干预支持 ICL 近似 belief-state update，但外推受限。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [SlotDiT](https://arxiv.org/abs/2609.17414v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：object-centric slot 把 diffusion latent 从像素/VAE 压缩推进到显式实体状态并改善机器人任务完成率。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [Never Stop Thinking](https://arxiv.org/abs/2609.17416v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：continuous-time Agent 需要 interrupt/resume orchestration，且 judge reward 会反向伤害真实完成，verifiable shaped reward 才有效。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [World Model Science](https://arxiv.org/abs/2609.17419v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：长时 Agent 需用 trajectory dynamics 诊断 local-valid/global-wrong、stress avalanche 与 metastable belief，而非只看 terminal reward。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### [PhysStream](https://arxiv.org/abs/2609.17521v1)

采用 arXiv v1 并按 `深入完成` 路径核对方法、评价与限制；作者阶段支持的最小结论是：streaming video generation 用 online structured scene memory 与 velocity increment 实现 mid-generation physical control。逐项证据位置见[证据笔记](../_sources/daily-20260917/evidence-notes.md)，最终 Books 处置按[队列](../_sources/daily-20260917/books-queue.md)串行完成。

### 静态执行计划 → 运行时资源合同 → 端到端验收

World Model accelerator 说明规则 shape/step schedule 可以换取专用执行效率，但 synthesis 与局部 P&R 不能证明真实 denoising trajectory 正确；DeepShare 又把共享 GPU 的 entitlement、可回收性、抢占风险和 interference 放进同一 assurance contract；OptiPrime 与 FlexEE 则分别显示 privacy protocol、memory movement、early exit 与 KV compatibility 不能由局部层独立决定。共同结论不是某个实现更快，而是 execution plan 必须绑定硬件/runtime identity、跨层状态约束和端到端验收；作者配置不能外推成普遍性能排序。

### “更多状态” → “有身份的状态” → “可提交、可回滚的状态”

mutable RAG、embedding migration、KV eviction、working-memory materialization 与 interruptible workflow 都在处理可变状态，但问题不只是容量。旧事实需要 supersession，embedding 升级需要旧索引兼容，KV 近似需要记录首次 divergence，按需 materialization 必须可回到原始 evidence，长时任务则要保存可恢复的 orchestration/effect state。因此优化对象应从“保存更多 token/cache”转成“维护带来源、版本、owner 和 commit 边界的可变状态”。作者实验仍局限于各自 workload，不能据此选择统一存储层或通用回收策略。

### 单体结果评价 → 系统轨迹评价 → 可恢复执行

EviScope 用成对反事实 evidence 区分 support、conflict、abstention 与 source-use；World Model Science 将 local-valid/global-wrong 等失败放回 trajectory；Never Stop Thinking 再把评价与 interrupt/resume、verifiable reward 和真实完成状态相连。技术演进不是“再加一个 benchmark”，而是把 evidence owner 从最终答案扩展为 trajectory、environment transition、tool effect 与 workflow commit。现有证据证明了若干测量缺口，但没有证明 learned judge、轨迹诊断或 orchestration harness 已形成通用可靠性保证。

## 5. 缺口与下一步

Books 核对与 13 项必要写入已经完成。独立终审核对了 514→25 的准入漏斗、17 个归属 09-16 的跨日重复、25 项 Evidence、13 个真实 Books 绑定、12 项 Existing Coverage 与 OpenAI 日期保留项；没有发现需要重开作者阶段或新增 Books 写入的问题。

本窗终态保留项（不用于正面证据、不进入 Books，也不支持无遗漏断言）：

- [Our framework for reporting model misalignment](https://openai.com/index/model-misalignment-reporting-framework/)：官方页只给 `2026-09-16`，日期与本窗相交但不完全落窗。缺少带时区发布时间；当前不作为候选、不评分。定点重开条件是取得官方页面 metadata、RSS 或存档中可核验的发布时间；届时只重开 2026-09-16/17 的归属判断。

窗外待办：无。

## 6. 复核

复核者：独立非作者终审（未参与本日报筛选、返修或 Books 写入）

结论：通过

终审确认：514 个 raw identity 中 116 个读取完整摘要，42 个初筛保留项里 17 个可逐项回溯到 09-16 Daily，本窗 25 个候选的评分与 Evidence 边界一致；13 个 `Integrate` 均在声明的唯一 owner 中存在且 source-family binding 各出现一次，12 个 `Existing Coverage` 可定位到现有具体论点。`2609.17416` 正确归属 `AGENT-WORKFLOW` Ch81。OpenAI misalignment 页面因只有 `2026-09-16` 日期而继续作为 Date Precision Gap 隔离，不评分、不写 Books；这不是材料审阅缺口。格式校验与 scoped diff-check 通过，但仅作为语义终审后的辅助检查。
