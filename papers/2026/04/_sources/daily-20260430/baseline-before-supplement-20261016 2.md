# Daily Research — 2026-04-30

**规范：** V3
**窗口：** 2026-04-29T09:00:00+08:00 ～ 2026-04-30T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-30T19:51:12+08:00

> 本文按当前V3合同收口；[旧V2.1正文原样存档](../_sources/daily-20260430/V2_REPORT_ARCHIVE.md)，旧46/54及Complete不继承。34家族的必要证据/准入和source→actual-owner已独立复核，17个新gap已真实写入且非作者实际写后通过；写前/写后及整日日级验收分开，本日另经[root非作者日级终核](../_sources/daily-20260430/V3_ROOT_DAILY_GATE_20260430.md)通过。

## 1. 结论

本窗确定的机构技术事件是智谱官方 04/29 16:00 北京时间发布的 Scaling Pain。其 Decode abort 未传递至 Prefill、旧 RDMA 写越过已复用 KV slot 的失效与 ACK 修复已在 Ch55 窄整合；按 CP rank 分层持有 KV 并于 attention 前广播的 LayerSplit 已在 Ch54 窄整合。arXiv 工作集中，DMEP 的一次性物理 expert/optimizer-state 裁除与旧可回滚 mask 的分支已在 Ch30 窄整合，OCR-Memory 的视觉定位与原文日志确定性回读已在 Ch77 窄整合，动态量化跨租户侧信道已有 Ch72 具体承载；三项均获必要原文、实际 owner 及写后或既有覆盖的非作者核验。单篇通过本身不代表整日报完成；本日另有完整日级独立验收。

arXiv 2604.25919–26952的1034个exact ID仍只是原始题名/题摘可取库存，不是1034个已语义筛选或全文队列。相关/含糊标题和高风险共享理由的受影响子集已按完整题摘及必要原文收紧，最后负侧26516的中心安全反例保护性恢复，当前34家族＝33 arXiv＋ZAI。20实际整合、1具体已有覆盖、7仅报告、6中心争议；三项既有整合及一Existing复用有效具名结果，17新gap实际写齐且均由root非作者实际正文/邻接写后通过，独立日级终核通过，普通可执行待办为0。[完整独立source→owner结果](../_sources/daily-20260430/V3_APR29_INDEPENDENT_SOURCE_OWNER.md)与[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)分开，不让中心争议或八条外部历史限制伪装未做普通工作。

本日报日期依据是 arXiv 官方美国东部周三 20:00 公告/赋号规则、相邻连续 ID 的官方处理批次、月列表和 exact-v1 的组合，推断批次于北京 04/30 08:00～09:00 公开；Submitted、Updated、OAI 或 DOI 字段均不单独冒充逐篇首次公开。具体跨批和版本例外须隔离。OpenAI Research Index、Seed Publications、MiMo Blog 等历史分页不能由首页证明零更新。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [News RSS](https://openai.com/news/rss.xml) 04/28 邻界与窗内四篇；[Research Index](https://openai.com/research/index/) 首屏 Sep23→Aug18 | 受阻 | RSS 四篇已逐篇初判；Research Index Load more 交互超时，未取本窗历史邻界；不推全站零发布 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 本窗 BioMysteryBench，较早邻界 04/22 | 已检查 | 已读受控 signal-validation notebook/同题五次尝试；Ch66 reference/attempt 分账已有，单篇受限任务不等超人真值 |
| SRC-GOOGLE-AI | [DeepMind Publications](https://deepmind.google/research/publications/) 可见有序段 05/06→04/25→04/23→04/22；[Google Research Publications](https://research.google/pubs/) 混排 | 受阻 | DeepMind 可见段跨本窗；Google Research 混排历史无日级邻界，不能推全生态零 |
| SRC-META-AI | [Publications p2](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=2) 近期有序段 May19→May04→Apr16→Apr14 | 受阻 | 可见 publication 段跨本窗；[Research 首页](https://ai.meta.com/research/) 子入口不可回溯 |
| SRC-QWEN | [研究 API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US) 邻界 04/28 10:00→04/30 12:00；[qwen-code Releases](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=10&page=33) p33–34 | 已检查 | 研究条目无本窗；v0.15.5 reasoning replay 相对 Ch84 具名前闭；p33–34 不代表组织全部仓库 |
| SRC-DEEPSEEK | [Research & News](https://www.deepseek.com/en/news/) 可见 News 09/10→04/24，Research 06/24→02/25 | 受阻 | 当前可见段跨本窗；两个 View All 历史交互未展开，不写全站零 |
| SRC-MOONSHOT | [Kimi Platform Blog](https://platform.kimi.com/blog) 静态可见段 2025/11→2024/05，无 2026 条目；[kimi-cli 1.41.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.41.0) 晚于截点，前一稳定 1.40.0 为 04/28 | 受阻 | 已核稳定 release 邻界与旧 Blog 可见层；其它重要仓库/新技术正文未得同窗邻界，不推全组织零 |
| SRC-TENCENT-HUNYUAN | [Research API](https://api.hunyuan.tencent.com/api/blog/publicList) 全 9 项，下一项 04/30 15:00、上一 03/23 | 已检查 | 可见 Research 层无本窗；不推全部仓库零 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 04/29 16:00 Scaling Pain，上一 04/07；[New Released](https://docs.z.ai/release-notes/new-released) 06/16→04/07 模型发布邻界 | 已检查 | Ch55/54 两处真实整合且 root 写后通过；受限部署数字和 zai-org 仓库当前列表不推全部事件为零 |
| SRC-BYTEDANCE-SEED | [Seed Research](https://seed.bytedance.com/en/research) 07/06→04/26→04/22；[Publications](https://seed.bytedance.com/en/public_papers) 首屏 1–20/242 至 05/14 | 受阻 | Research 可见段跨本窗；Publications 下一页非静态链接，试 ?page=2/3 未得历史邻界 |
| SRC-BAIDU-ERNIE | [ERNIE Blog](https://ernie.baidu.com/blog/zh/) 05/09→04/30 Preview→04/15；[PaddlePaddle/ERNIE Releases API](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100&page=1) 仅 2025-06-30 一条，默认分支本窗 commits 查询为空 | 已检查 | Blog 本窗榜单文章具名前闭；仓库日期查询不证明其它 branch/仓库零更新 |
| SRC-XIAOMI-MIMO | [MiMo](https://mimo.xiaomi.com/) Paper 06/29→03/13→02/03 | 受阻 | 可见 Paper 段跨本窗；Blog 卡片无日期、More 未展开，不能说无更新 |
| SRC-MINIMAX | [英文 Blog](https://www.minimax.io/blog) 08/13→05/26→03/18；[中文 Blog](https://www.minimaxi.com/blog) 05/25→04/27→03/18；[Agent Tech](https://agent.minimax.io/docs/llms.txt) 仅索引 Agent Team | 受阻 | 中英文有序层跨本窗；Agent Tech 文章入口及重要仓库未得可回溯日界 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html)、[cs 月列表](https://arxiv.org/list/cs/2026-04)、相邻 25918/25919 与 26952/26953 的官方处理链；[本日发现记录](../_sources/daily-20260430/V3_SOURCE_DISCOVERY.md) | 已检查 | 1034仅raw库存；主题标题补检/相关完整题摘与停止点保存，非逐篇公开日志/全学科召回，日期Gate由非作者终核 |

来源入口、实际分页尝试和无法回溯的恢复条件详见[有界发现记录](../_sources/daily-20260430/V3_SOURCE_DISCOVERY.md)。对不可取得的历史层只保留其精确限制，既不伪称零更新，也不让其它可执行研究停下。

## 3. 候选与判断

经apr29_close全拟入选及具名负侧有限复核，冻结**34家族＝33 arXiv＋ZAI**：原33再恢复26516中心安全保证争议，其他身份不变；此前26516共模旧覆盖关闭被保护性反例替代。17新gap均已source→actual-owner通过且实际写入，非作者实际写后全通过；3既有整合/1Existing复用有效记录，7Only/6D受限处置通过。总处置20整合/1已有覆盖/7Only/6暂缓，必要审阅22深入/6标准/6争议已完成；整日日级Gate由非作者root独立通过，见§6，不作者自签。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Scaling Pain](https://www.zhipuai.cn/zh/research/159) | 2026-04-29T16:00:00+08:00 | Decode abort/Prefill 写入 epoch 与 CP-rank 分层 KV ownership 两条不同边界；2+2+2=6 | 深入完成 | 整合 INFER-PD-DISAGGREGATION [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) 与 INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Adaptive and Fine-grained Module-wise Expert Pruning for Efficient LoRA-MoE Fine-Tuning](https://arxiv.org/html/2604.26340v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 逐模块 Top-k 路由计数后一次性裁 expert/optimizer state、重排 gate 并改变后阶段目标；2+2+2=6 | 深入完成 | 整合 TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Quantamination: Dynamic Quantization Leaks Your Data Across the Batch](https://arxiv.org/html/2604.26505v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 同 batch per-tensor scale 让受害输入改变攻击者可见量化误差与 logits；2+2+2=6 | 深入完成 | 已有覆盖 PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory](https://arxiv.org/html/2604.26622v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 图像只提出轨迹片段索引，日志按索引确定性回读原文；2+2+2=6 | 深入完成 | 整合 AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts](https://arxiv.org/html/2604.26039v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 实际路由结果决定同一 batch CTA grid/config；2+2+2=6 | 深入完成 | 整合 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [From Prompt Risk to Response Risk: Paired Analysis of Safety Behavior of Large Language Model](https://arxiv.org/html/2604.26052v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 输入与输出独立风险标签保留方向分母；2+2+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DAK: Direct-Access-Enabled GPU Memory Offloading with Optimal Efficiency for LLM Inference](https://arxiv.org/html/2604.26074v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | direct/staged 搬运按 operation 分配；2+2+2=6 | 深入完成 | 整合 `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent](https://arxiv.org/html/2604.26102v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 读污染规划 context 与格式失败不同 owner；2+2+2=6 | 深入完成 | 整合 `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Evergreen: Efficient Claim Verification for Semantic Aggregates](https://arxiv.org/html/2604.26180v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 量词类型决定查询/停止/tuple lineage；2+2+2=6 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent](https://arxiv.org/html/2604.26197v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 同一业务树绑定候选/聚合/失效三域；2+2+2=6 | 深入完成 | 整合 `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [DORA: A Scalable Asynchronous Reinforcement Learning System for Language Model Training](https://arxiv.org/html/2604.26256v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 单版本 DP group/最老窗口/同版本 KV 迁移；2+2+2=6 | 深入完成 | 整合 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents](https://arxiv.org/html/2604.26274v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 低熵良性 trace→pDFA→pre-effect state gate；2+2+2=6 | 深入完成 | 整合 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Folding Tensor and Sequence Parallelism for Memory-Efficient Transformer Training & Inference](https://arxiv.org/pdf/2604.26294v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 同 D-way rank 轴共享两类驻留选择；2+2+2=6 | 深入完成 | 整合 `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [DUAL-BLADE: Dual-Path NVMe-Direct KV-Cache Offloading for Edge LLM Inference](https://arxiv.org/html/2604.26557v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 同资产按 layer KV unit 绑定 page-cache/LBA；2+2+2=6 | 深入完成 | 整合 `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | action先完成须覆盖 clean-action/noisy-video；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding](https://arxiv.org/html/2604.26779v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | target forward 复用信号但 draft loss detach；2+2+2=6 | 深入完成 | 整合 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving](https://arxiv.org/html/2604.26837v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | Index/Select 与 Offload/Retrieve、active metadata；2+2+2=6 | 深入完成 | 整合 `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Who Trains Matters: Federated Learning under Enrollment and Participation Selection Biases](https://arxiv.org/html/2604.26604v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 未入组者与轮次参加是两层 inclusion；2+2+2=6 | 深入完成 | 整合 `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [CoQuant: Joint Weight-Activation Subspace Projection for Mixed-Precision LLMs](https://arxiv.org/html/2604.26378v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 双量化误差改变保护空间校准准则；2+1+2=5 | 深入完成 | 整合 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Tatemae: Detecting Alignment Faking via Tool Selection in LLMs](https://arxiv.org/html/2604.26511v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 同压力的监控措辞可改变动作选择；2+1+2=5 | 深入完成 | 整合 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics](https://arxiv.org/html/2604.26836v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | reachable tube 之外增加 certain-set 约束；2+2+2=6 | 深入完成 | 整合 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Breaking the Autoregressive Chain: Hyper-Parallel Decoding for Efficient LLM-Based Attribute Value Extraction](https://arxiv.org/html/2604.26209v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 逻辑position/mask与物理cache顺序分离；2+1+2=5 | 标准完成 | 仅报告 Ch48 条件性任务factorization |
| [Progressive Semantic Communication for Efficient Edge-Cloud Vision-Language Models](https://arxiv.org/html/2604.26508v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | encode一次后按重建误差追加有序prefix；2+1+2=5 | 标准完成 | 仅报告 Ch23 受限edge-split控制 |
| [When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models](https://arxiv.org/html/2604.26649v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | logical-step boundary 的中途检索执行形态；2+1+2=5 | 标准完成 | 仅报告 Ch76 受限checkpoint实现 |
| [STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation](https://arxiv.org/html/2604.26848v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 预测geometry作用于action→visual attention；2+1+2=5 | 标准完成 | 仅报告 Ch26 受限几何actuator |
| [Test-Time Safety Alignment](https://arxiv.org/html/2604.26167v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | token/text相同不代表连续输入相同；2+1+2=5 | 深入完成 | 仅报告 Ch72 保护性oracle边界 |
| [Multi-Server Secure Aggregation with Arbitrary Collusion and Heterogeneous Security Constraints](https://arxiv.org/html/2604.26391v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 异质collusion×两跳拓扑改变key/通信率；2+1+2=5 | 标准完成 | 仅报告 Ch36 严格有限域条件线索 |
| [A Leakage Bound for Confidence Sets after Black-Box Selection](https://arxiv.org/html/2604.26706v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | TV/互信息泄漏限制选择后noncoverage；2+1+2=5 | 标准完成 | 仅报告 Ch66 条件性selection-bound |
| [Anchored Confabulation: Partial Evidence Non-Monotonically Amplifies Confident Hallucination in LLMs](https://arxiv.org/html/2604.25931v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 置信诊断标签与互信息保证不能互代；2+2+2=6 | 争议 | 暂缓 中心保证不作Books正面证据 |
| [reward-lens: A Mechanistic Interpretability Library for Reward Models](https://arxiv.org/html/2604.26130v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | final LN 与逐项线性readout不相容；2+2+2=6 | 争议 | 暂缓 中心恒等式不作Books正面证据 |
| [PRAG: End-to-End Privacy-Preserving Retrieval-Augmented Generation](https://arxiv.org/html/2604.26525v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 中心排序/算法/trust-boundary主张需隔离；2+2+2=6 | 争议 | 暂缓 中心隐私保证不作Books正面证据 |
| [Differentially Private Contrastive Learning via Bounding Group-level Contribution](https://arxiv.org/html/2604.26467v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 依赖域→clip/noise须绑定同一随机机制；2+2+2=6 | 争议 | 暂缓 中心DP保证不作Books正面证据 |
| [Asynchronous Federated Unlearning with Invariance Calibration for Medical Imaging](https://arxiv.org/html/2604.26809v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 旧snapshot直接发布与KL不推永久删除；2+2+2=6 | 争议 | 暂缓 中心删除保证不作Books正面证据 |
| [Lyapunov-Guided Self-Alignment: Test-Time Adaptation for Offline Safe Reinforcement Learning](https://arxiv.org/html/2604.26516v1) | 2026-04-30T08:00:00+08:00 ～ 2026-04-30T09:00:00+08:00 | 密度→cost安全及折扣Lyapunov→不逃域的保证桥须纠错；2+2+2=6 | 争议 | 暂缓：中心安全保证隔离，不Books |

## 4. 证据与知识整合

下列全部33项arXiv家族的公开范围是本批常规美国东部 20:00 公告、连续 ID 与相邻处理链的联合推断，而非逐篇 first-public 时间戳。原始收据中 `26340/26505` 的 v1 `Updated` 分别为 04/30 00:27:52Z/00:40:21Z，OAI 当前日戳均为 04/30；这些仅作身份/版本交叉核验，不能单独证明首次公开。完整日期例外与截点隔离见[工作表](../_sources/daily-20260430/V3_CANDIDATE_RECONCILIATION.md)。

### [Scaling Pain](https://www.zhipuai.cn/zh/research/159)

官方 2026/04/29 16:00 北京发布。§BugFix#1 表明 Decode 已取消而 Prefill 尚在写旧请求 KV 时，slot 重用可遭到迟到 RDMA 写覆盖；修复的 ACK 属于释放/复用前的跨角色完成确认，而不是单方面 abort。§LayerSplit 则把长上下文的 KV 层按 CP rank 持有并在 attention 前广播，区别于全 rank 常驻或简单 host offload。这两条分别进入 Ch55 Handoff/Cancellation 与 Ch54 Peer GPU Spare Memory 后的层级管理分支，保留短上下文、弱互联、隔离回退与额外等待成本。作者 90% cache hit、40k–120k、GLM-5.1 的部署数字仅限原配置，不能推通用异常率或吞吐。两处的 root 非作者正文写后核在 [Ch55](../_sources/daily-20260430/V3_ROOT_ZAI_CH55_WRITE_AFTER.md) 与 [Ch54](../_sources/daily-20260430/V3_ROOT_ZAI_CH54_WRITE_AFTER.md) 的独立记录中；未复现实验。

### [Adaptive and Fine-grained Module-wise Expert Pruning for Efficient LoRA-MoE Fine-Tuning](https://arxiv.org/html/2604.26340v1)

官方 exact-v1 §III-C–F/Algorithm 1/Table I–II 将均匀探索时累计的逐模块硬路由计数用于选择 survivor，固定 warm-up 后一次性切除未保留的 expert 权重及 optimizer moments、重排 gate 输出，再在后阶段关闭 load-balancing loss。这相对 Ch30 原本的可回滚 mask 是训练 artifact 与优化目标迁移，不是同一遮罩的另一名字。已在[原段后](../../../../books/part-04-training-system/30-lora.md)窄写，保留完整 checkpoint/旧 mask 回退；算法印刷不是在线 drift 阈值触发，Table I 吞吐只测后阶段，ScienceQA 有低于对称 MoE 的切片。[root 采用边界](../_sources/daily-20260430/V3_ROOT_TWO_BOOKS_BOUNDARY_FINITE.md)及[实际写后复核](../_sources/daily-20260430/V3_ROOT_26340_CH30_WRITE_AFTER.md)均通过；实验未复现。

### [Quantamination: Dynamic Quantization Leaks Your Data Across the Batch](https://arxiv.org/html/2604.26505v1)

官方 exact-v1 §3–6 的受限攻击使同一 batch 中动态 per-tensor scale 由租户间输入共同决定，改变攻击者可观察的 logit 误差。它改变安全边界，但[Ch72 现文](../../../../books/part-06-ai-infrastructure/72-security.md)已有 scale granularity、batch composition、tenant 分隔、logit access 与旧单租户 fast path 的具体分账，故不重复写 Books。受测为 TinyStories-1M/Pythia-70M/SmolLM2-135M、batch 2；完成 runs 的成功率不等生产环境攻击率。[root 独立 source—owner 核](../_sources/daily-20260430/V3_ROOT_TWO_BOOKS_BOUNDARY_FINITE.md)已通过。

### [OCR-Memory: Optical Context Retrieval for Long-Horizon Agent Memory](https://arxiv.org/html/2604.26622v1)

官方 exact-v1 §4 式(5)–(15) 同时存渲染图像、verbatim 文本片段与 metadata；SoM 检索器只选 `(image, segment)`，再从原文日志确定性取回文字。低清图命中后按原日志重渲高清，不把模糊图本身写成无损证据。Ch77 原先的纯图像风险仍成立，但[新增分层路径](../../../../books/part-07-agent/77-memory.md)让图像仅作低 token 定位、日志拥有精确证据；错定位与已选后原文一致是不同验收项，revision、授权和删除同步为工程条件而非论文已验证的安全保证。作者 Table 3 动态 Step SR 46.1% 低于静态高清 46.5%；Table 7 主 Agent 文本注入 3980→596 token/step，同时磁盘 18KB→1.47MB/episode、检索 0.3→1.7s/step，不能声称端到端普遍更省。[root 写前源—owner 核](../_sources/daily-20260430/V3_ROOT_26622_CH77_SOURCE_TO_OWNER.md)与[非写入者实际正文核](../_sources/daily-20260430/V3_APR01_26622_CH77_WRITE_AFTER.md)已通过；实验未复现。

作者必要证据与最终受限处置已由[apr29_close全34有限独立核](../_sources/daily-20260430/V3_APR29_INDEPENDENT_SOURCE_OWNER.md)通过。下列每项保留精确版本、关键机制/评价反证与Books差额；实际写后另核，不由采用pack文件存在推通过。

### [RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts](https://arxiv.org/html/2604.26039v1)

§IV–V 在同 kernel binary/硬件下比较 routing-aware 配置；不是跨 GPU placement 或 router 改写。单 H200、vLLM eager、顺序请求和 FP8 MoE 的结果不证明并发 SLO。现 Ch49 grouped execution 有 tile/imbalance 成本，已补同一batch histogram→本机配置的窄分支。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_KERNEL_OFFLOAD.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)的routing histogram→CTA/grid配置分支（本轮锚617–619；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [From Prompt Risk to Response Risk: Paired Analysis of Safety Behavior of Large Language Model](https://arxiv.org/html/2604.26052v1)

§3–4 对同一 pair 独立标风险类别/等级及相关性。作者 drift-up 是给定响应有害回看输入无害，不能倒写成给定无害输入后的危害概率；两模型 prompt 不配对、1250 单轮英文不支持跨模型因果差。已落实Ch66双端风险转移。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_EVAL.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的prompt/response双端标签与方向分母分支（本轮锚614–616；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [DAK: Direct-Access-Enabled GPU Memory Offloading with Optimal Efficiency for LLM Inference](https://arxiv.org/html/2604.26074v1)

§2.3–4.3/6 的特定 TMA/互联允许 host→SMEM 绕过 HBM staging，须限制在途访问、按 operation 敏感度配比。GH200/Blackwell 离线短 decode 与 PCIe 高 offload 比率下差额消失，不是一般 host offload 最优；已落实Ch54物理搬运分支。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_KERNEL_OFFLOAD.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[INFER-GPU-MEMORY](../../../../books/part-05-inference-system/54-gpu-memory.md)的host→SMEM逐operation搬运分支（本轮锚266–268；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [SWE-Edit: Rethinking Code Editing for Efficient SWE-Agent](https://arxiv.org/html/2604.26102v1)

§3–4 拆 Viewer/main/Editor context，编辑器另有受限 GRPO；三角色不是通用默认。GPT-5 全 Verified 的 resolve/成本、其他模型前100题与额外调用不同分母；旧 workspace revision/patch admission 仍成立，已补检视污染与补丁格式分账。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_THREE_REMAINING.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[AGENT-WORKFLOW](../../../../books/part-07-agent/81-workflow.md)的Viewer读取污染与Editor格式失败分账分支（本轮锚1144–1146；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Evergreen: Efficient Claim Verification for Semantic Aggregates](https://arxiv.org/html/2604.26180v1)

§2–6 编译 existential/universal/count 等关系 claim：witness、counterexample 与剩余 tuple 上界决定停止。16条人工检查 compiler、三LLM多数票 reference 不等真值；grounded universal 假反例保留。已落实Ch66验证单位，不复制查询执行 owner。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_EVAL.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的关系量词query/tuplelineage与受限CS早停分支（本轮锚2051–2053；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Hierarchical Long-Term Semantic Memory for LinkedIn's Hiring Agent](https://arxiv.org/html/2604.26197v1)

§3.2/3.5.1/3.7 用稳定业务实体树先筛可读 subtree，更新叶子只重建祖先。lossless incremental 是与同规则 full rebuild 对齐，不是摘要事实无损；120 queries/50 docs、RAG precision 与 full-context recall 反例不能藏。已落实Ch77三域绑定，ACL/迁移仍外部验证。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_HIERARCHICAL_MEMORY.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[AGENT-MEMORY](../../../../books/part-07-agent/77-memory.md)的业务授权树/聚合域/祖先失效分支（本轮锚287–289；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [DORA: A Scalable Asynchronous Reinforcement Learning System for Language Model Training](https://arxiv.org/html/2604.26256v1)

§4.2–4.4 单 DP group 持一个 policy version、长尾原版继续、最老版本收齐再滑窗；按在途量重分组，同版本搬 KV。64/128 GPU 开放设置不证千卡或通用收敛；版本、P2P与悬挂轨迹成本同账。已落实Ch33 lifecycle 而非复制 fabric 章节。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_DORA.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)的逐轨迹policy版本窗口与KV同权重迁移分支（本轮锚1169–1171；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Enforcing Benign Trajectories: A Behavioral Firewall for Structured-Workflow AI Agents](https://arxiv.org/html/2604.26274v1)

§4/5/7–8 人工确认良性序列编 pDFA/参数guard，每 session 状态在执行前检查，拒绝不前进。profile 更新也是权限变化，不替代 IAM；开放任务、poisoning、合法循环与字符串绕过保留。O(1)查表不含全部guard，五ASB场景非完整安全SLO。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_GUARD_ROLLOUT.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[PLATFORM-SECURITY](../../../../books/part-06-ai-infrastructure/72-security.md)的可信正向轨迹编译pDFA与参数guard分支（本轮锚986–988；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Folding Tensor and Sequence Parallelism for Memory-Efficient Transformer Training & Inference](https://arxiv.org/pdf/2604.26294v1)

PDF-v1 §III–VI 为方法权威：attention 权重广播/KV all-gather，MLP ring 权重轮转，额外通信换两类 residency；不是普通两维 mesh。1024 MI300X 主表多为 forward-only，只有16 GPU microbatch 给 forward+backward，不能叫完整训练普遍加速。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_THREE_REMAINING.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[TRAIN-DISTRIBUTED-TRAINING](../../../../books/part-04-training-system/36-distributed-training.md)的单D轴weight/sequence联合分片分支（本轮锚549–551；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [DUAL-BLADE: Dual-Path NVMe-Direct KV-Cache Offloading for Edge LLM Inference](https://arxiv.org/html/2604.26557v1)

§III–V 初始化 host budget、unit→extent/path；direct 仍经过 pinned DRAM，不是 SSD→GPU 或任意在线热迁移。DRAM 富余时全direct反慢，edge OPT/两SSD与2–11GB budget不证生产尾延迟；extent版本、持久/回收和队列是新成本。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_KV_TIER.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[INFER-GPU-MEMORY](../../../../books/part-05-inference-system/54-gpu-memory.md)的NVMe初始化page-cache/LBA双路径分支（本轮锚599–601；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/html/2604.26694v1)

§3.3/Eq4/Alg2 在浅 action 完成后固定 t_a=0，video 继续；训练需覆盖该组合而非独立时刻。Table4无5800小时预训练，同1033ms的67.2→67.8与视频质量不能解释整模型headline。连续训练律非逐点部署schedule、安全授权仍controller。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_XWAM.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)的clean-action/noisy-video异步时间训练支持分支（本轮锚257–259；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding](https://arxiv.org/html/2604.26779v1)

§2–4 exact verifier 保持 target law，hidden/logprob detach 后训练 draft，不能让auxloss修改policy gradient。8B同步实测与235B异步模拟分开；draft加长虽acceptance升却speed反降，生成收益不等整步收益。已落实Ch33 target/gradient/version三权分离。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_GUARD_ROLLOUT.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)的policy信号复用但draft-head stop-gradient分支（本轮锚1173–1175；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving](https://arxiv.org/html/2604.26837v1)

§4–6 把算法接口与 runtime 页映射分开，最坏 batch/context/layer/head 页元数据可先于 KV bytes 压 HBM；head-wise活跃物理metadata降低最坏逻辑reserve，pinned CPU tables仍可由GPU直接读取。dense对照混算法，在线高负载TPOT可反高；质量、fault和metadata成本联合验收。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_KV_TIER.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[INFER-GPU-MEMORY](../../../../books/part-05-inference-system/54-gpu-memory.md)的稀疏算法/运行时分页分责和活跃物理metadata分支（本轮锚603–605；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Who Trains Matters: Federated Learning under Enrollment and Participation Selection Biases](https://arxiv.org/html/2604.26604v1)

§2–5 区分 global target population 与 enrolled objective；只校正轮次到达不能恢复从未可观察者。ignorability/positivity/可估propensity或aggregate calibration才支持条件校正，否则缩小estimand；synthetic logistic不能称LLMFL实测。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_BOOKS_ADOPTION_PACK_THREE_REMAINING.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[TRAIN-DISTRIBUTED-TRAINING](../../../../books/part-04-training-system/36-distributed-training.md)的enroll population与round参与两阶段抽样分支（本轮锚1172；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [CoQuant: Joint Weight-Activation Subspace Projection for Mixed-Precision LLMs](https://arxiv.org/html/2604.26378v1)

§3–5/AppendixA.3 加权未中心化 XᵀX+WWᵀ 选高精度输入子空间；Eq27丢捕获能量乘积后才有surrogate最优，非真实loss全局最优。1B/3B、512 WikiText、单A100无专用kernel/服务时延；已补不同于curvature bit allocator的共享高精度子空间分支。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)的联合W/A共享高精度子空间分支（本轮锚1079–1081；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Tatemae: Detecting Alignment Faking via Tool Selection in LLMs](https://arxiv.org/html/2604.26511v1)

§2–4 中性capability、压力无/有监控、理由judge组成AF label。T2→T3换的是虚构RLHF监控system prompt，不是真实训练状态；JSON/XML选择未执行，理由非隐动机真值。108场景六模型五次只支撑受限composite标签，保护性深核假阳性。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的同压力无监控/声称监控配对分支（本轮锚165–167；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics](https://arxiv.org/html/2604.26836v1)

v1 §5.1–5.3 的轨迹每点要在模型certain set，否则controller可利用epistemic error；保守噪声/无偏均值/初始robust controller/Lipschitz是前提。§6零Lipschitz、K=0、软约束明确打破形式保证，100k采样不是实时硬件证书；已补窄模型有效域分支。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_AUTHOR_FINAL_ADMISSION.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

已实际写入[MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)的轨迹state-action模型certain域准入分支（本轮锚1200–1202；并发插段后依family定位），保旧方案/cost/fallback。apr29_close必要源→实际owner通过；root非作者实际正文及邻接写后通过，见[实际写后记录](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)。

### [Breaking the Autoregressive Chain: Hyper-Parallel Decoding for Efficient LLM-Based Attribute Value Extraction](https://arxiv.org/html/2604.26209v1)

v1 §4–6 在共同文档/键下近似独立的AVE字段用position gap并行；mask按逻辑position而非追加顺序，训练同mask。它改变输出factorization，不是lossless target串验证；独立性/fixed Kmax须任务核，三个电商任务不证通用AR替代。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [Progressive Semantic Communication for Efficient Edge-Cloud Vision-Language Models](https://arxiv.org/html/2604.26508v1)

v1 §III–V/B–C 缓存视觉编码，cloud用预测重建误差决定下一段传输；不是仅减少固定带宽。TableIII的100%LTL满足不等线上E2E stopping加速，预测误差并非视觉事实oracle；当前Ch23授权/表示接口不因专科部署组合重写。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [When to Retrieve During Reasoning: Adaptive Retrieval for Large Reasoning Models](https://arxiv.org/html/2604.26649v1)

v1必要方法把检索插在reasoning logical-step boundary；open-weight KV与completion-only refeed不同成本。gold answer只离线训练，线上非oracle。Ch76已有query/compression/stopping联合policy，三多跳QA证据不足新增长期owner，但边界执行形态可受限报告。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [STARRY: Spatial-Temporal Action-Centric World Modeling for Robotic Manipulation](https://arxiv.org/html/2604.26848v1)

explicit HTML-v1 §3/Table4/AppC只改action读权重；action-only也从同门控大幅受益，不能把全部差额归fullfuture model。三真机任务与depth/pose误差不证可达状态；现Ch26 prediction仅提案，controller/environment仍最终权威。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [Test-Time Safety Alignment](https://arxiv.org/html/2604.26167v1)

v1 §4–5/Alg1逐请求embedding搜索每轮N+1生成/moderation，同一moderation oracle定义优化和flagged。API同源zero flagged不能当独立安全保证；连续值身份与文字/token身份分账，保留计算及外部outcome缺口，不写普遍防御。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [Multi-Server Secure Aggregation with Arbitrary Collusion and Heterogeneous Security Constraints](https://arxiv.org/html/2604.26391v1)

exact-v1必要方法/定理对不同共谋集合和两跳多服务器拓扑求key与通信率；有限域、无误广播与指定对手集合不可省略。它为聚合设计提供受限约束轴，不等任意FL/LLM协议实现或生产网络保证；不写Books通用安全结论。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [A Leakage Bound for Confidence Sets after Black-Box Selection](https://arxiv.org/html/2604.26706v1)

exact-v1必要定理把同一样本被黑盒选择后目标CI的noncoverage与TV/MI泄漏相连，要求固定推断目标和可界定联合分布。尚无模型评测中的leakage估计/校准，不据公式发布coverage保证；保留sampling vs selection的条件化理论线索。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [Anchored Confabulation: Partial Evidence Non-Monotonically Amplifies Confident Hallucination in LLMs](https://arxiv.org/html/2604.25931v1)

§3 Theorem1所称任意post-gen信号不劣于pre-gen，常数U而g含标签信息即反例；G*是GraphRAG升级收益不是逐题wrong label。保留受限诊断/预算曲线，不采普遍定理或阈值保证。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_PROTECTION_DISPUTED_FINITE_PACK.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [reward-lens: A Mechanistic Interpretability Library for Reward Models](https://arxiv.org/html/2604.26130v1)

§3声称分项和exact重建reward，AppendixB却有非线性final LN，一般wᵀLN(Σh_i)不等Σwᵀh_i。单首对答案patching排序多负相关只说明probe不自动获因果权，不否定visualizer/patching全部。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_PROTECTION_DISPUTED_FINITE_PACK.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [PRAG: End-to-End Privacy-Preserving Retrieval-Augmented Generation](https://arxiv.org/html/2604.26525v1)

§V-C各误差小于gap一半恰足以保序；误差差值上界不推排序近随机，恒零误差即反例。Alg3虚拟向量下一层Neighbors未给node映射；明文embedding/context又给第三方，非所有服务方E2E保密。保留HE与client-assisted受限取舍。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_PROTECTION_DISPUTED_FINITE_PACK.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [Differentially Private Contrastive Learning via Bounding Group-level Contribution](https://arxiv.org/html/2604.26467v1)

v1 AppendixA Thm2假设邻接增删后旧pair同组，Alg1却随机group；S=2两pair→三pair无法同时固定旧组和维持均匀二人+单人组边际。该缺桥不否定实验效用，未给稳定grouping/accountant前不把印刷2C/ε叫生产证书。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_PROTECTION_DISPUTED_FINITE_PACK.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [Asynchronous Federated Unlearning with Invariance Calibration for Medical Imaging](https://arxiv.org/html/2604.26809v1)

v1 Alg1直接赋旧snapshot派生删除权重，无并发retained update比较/合并/重放，进展可被旧回传覆盖；恒等变换/已不变模型KL=0不推feature erasure。5–20客户端CNN、十轮backdoor/参数距非一般async/永久删除证明。 [必要证据与实际 owner 索引](../_sources/daily-20260430/V3_PROTECTION_DISPUTED_FINITE_PACK.md)保存方法、评价、反证与停止点；本轮复用命题/版本未变的有效阅读，不声称复现实验。

### [Lyapunov-Guided Self-Alignment: Test-Time Adaptation for Offline Safe Reinforcement Learning](https://arxiv.org/html/2604.26516v1)

exact-v1 §2.2–3.2的中心安全信号使本项从贡献前关闭保护性恢复：Eq4的occupancy密度下界没有cost–density联系，不能保证CMDP预算；§2.3 G≥γE[min G′]只限制折扣后期望，γ=.9、当前G=1、唯一后继G′=1.1满足条件却逃出c=1域。平衡点0/正值条件不排除该局部转移。保留SAS受限prompt/VAE仿真实验，不说全部算法无效；不采用逐路径不增/安全保证，不Books。恢复需真正未折扣逐路径barrier、明确cost-density关系及模型误差的修补证明，见[独立必要公式反核](../_sources/daily-20260430/V3_APR29_INDEPENDENT_SOURCE_OWNER.md)。

## 5. 缺口与下一步

以下外部历史来源、五项日期Hold及六项中心争议均是**本窗终态保留项**：不用于正面证据、不进入Books、不支撑无遗漏或性能/安全保证；可接受材料补到后仅定点重开所指家族/来源层，不扩大本窗或全月。八个source具体入口/停止/恢复请求引用[SOURCE_DISCOVERY](../_sources/daily-20260430/V3_SOURCE_DISCOVERY.md)，五个日期项25925/26365/26889/26940/26951的首公开请求引用[RECONCILIATION隔离节](../_sources/daily-20260430/V3_CANDIDATE_RECONCILIATION.md#首次公开家族身份隔离不计本窗正面候选)；六D需要的必要公式/实现修补条件如下及各§4，不把保留项叫Coverage/Evidence通过。26334为另具名家族去重线索，不混进五个日期项计数。

普通可执行待办：**无（0）**。扫描/筛选、逐项必要审阅、Books处置与真实写入、非作者实际写后及日级Gate均已获得本次终态结论；没有将外部限制当作通过的覆盖。17新增实际写后和3既有整合/1Existing的有效复用分别核验，最终完成元数据依据[root独立日级记录](../_sources/daily-20260430/V3_ROOT_DAILY_GATE_20260430.md)同步，不作者自签。

八个历史子层分别为OpenAI Research Index、Google Research Publications、Meta Research主页、DeepSeek View All、Moonshot2026 Blog/技术仓库历史、Seed Publications、MiMo Blog/More、MiniMax Agent Tech；§2和[来源发现](../_sources/daily-20260430/V3_SOURCE_DISCOVERY.md)逐项保留实际停止/尝试与恢复条件。这些层没有必要日级材料可恢复时已终态隔离，不支持候选/Books/覆盖保证，不用搜索首页或静态无日期卡片认零。

六个中心争议不是材料访问故障：25931需修正任意U互信息比较或限定非平凡信号/联合律；26130需处理final LayerNorm的真实非线性并提供可核分解及sanity证据；26525需给排序随机性分布桥和虚拟节点可遍历映射/清楚trust边界；26467需相邻随机分组保持边际的有效coupling或稳定grouping/accountant；26809需并发retained版本的merge/replay/CAS语义及非augmentation恒等式的删除证据；26516需未折扣逐路径barrier、cost-density联系和模型误差前提。未修前只保受限观察，不正面采用对应保证、不Books；必要补件到达只重开该family。

`2604.26334`的更早软件/论文家族身份另需官方初次正文/release对应证明，暂不重复按April ID计分；`26157`有具名官方撤回原因，永久清除该撤回版本的候选/评分/采用链，不当访问受阻。这里不处理真实窗外日期的研究，亦不创建另一份Daily或Weekly。

本窗明确隔离：OpenAI Research Index、Seed Publications、MiMo Blog、DeepSeek View All 等历史分页目前不能支持“该机构全站无本窗发布”；恢复条件分别为官方可读历史页/分页响应或同日原始条目。`2604.25925v1` 的同题 OpenReview 全文、`2604.26365v1` 的[作者 02/22 主页版本](../_sources/daily-20260430/V3_CANDIDATE_RECONCILIATION.md#首次公开家族身份隔离不计本窗正面候选)分别构成更早同家族身份线索；arXiv April ID 和提交/OAI 时间不能排除早公开，故两项均不在本窗评分或正面 Books，待精确首发记录定点重开。另外 `2604.26889/26940/26951` 的 v1 处理字段分别在本窗 09:00 截点后 1–4 分钟，官方 abs-v1 仅列 04/29 Submitted、cs 月列表未给逐篇公开时刻；[本日工作表](../_sources/daily-20260430/V3_CANDIDATE_RECONCILIATION.md#首次公开家族身份隔离不计本窗正面候选)保留原机制/争议证据，但在得到官方逐篇公告或同等首次公开上界前，三项均作日期未核隔离、不评分/不正面写 Books。这些处理字段不能反证其实际晚公开。中心公式争议和其它具体日期/版本污染仅在具名源证据、作者修订或官方公告能够解决时定点重开，不据它们写正面 Books。窗外 2604.26953–27045 不进入本窗分母。

## 6. 复核

复核者：root（非本日报/新段作者）；apr29_close（全34准入/必要source→actual-owner）。
结论：通过

[root独立日级终核](../_sources/daily-20260430/V3_ROOT_DAILY_GATE_20260430.md)检查十四每日源的实际查询/停止范围、1034库存与贡献漏斗、官方批次有界日期/例外、34逐家族证据与最终Books处置。复用[apr29_close全34及七具名负侧](../_sources/daily-20260430/V3_APR29_INDEPENDENT_SOURCE_OWNER.md)的有效必要原版结果；root另核机构四篇OpenAI/Anthropic/Qwen/ERNIE具体关闭，不将未查库存说全量摘要/全文验真。安全信号26516恢复D，26157撤回排除，八历史子层与日期保留不支撑无遗漏。

17新family实际正文与前后衔接全部经[root非作者写后](../_sources/daily-20260430/V3_ROOT_WRITE_AFTER_REVIEW.md)通过，3既有整合/1Existing另有本日ROOT/APR01具名记录。Ch33 Objective标题、Ch54 MoE标题与CoQuant曲率段插序已定点修复并重新实际读取，不以marker或作者自读替代。ScalingPain同family两落点只算一次。source、写后和日级权限分开，未复现实验、未把争议主张正面采用。

完成状态V3校验、34唯一行/34证据段与本地链接检查及限定diffcheck通过；机器只验机械一致性，不替代语义。普通待办0，终态保留仍按§5具体请求定点重开。未stage、commit或push，原有无关及暂存修改保留；本lane到本日完成即停止，不接新日期或Weekly。
