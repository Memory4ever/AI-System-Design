# Daily Research — 2026-09-14

**规范：** V3
**窗口：** 2026-09-13T09:00:00+08:00 ～ 2026-09-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-14T23:30:00+08:00

## 1. 结论

本窗处理了十四个每日来源：十二个完成窗口检查，Meta 与 MiMo 两个来源因缺少稳定的日级完整枚举而受阻，并已隔离为不支持候选、Books 或“当窗绝对零事件”断言的终态保留项。arXiv 在北京时间 09-14 约 08:00 公布 Monday new-submission batch；十二个目标分类合并后得到 375 个唯一 identity，375/375 均完成 title + abstract 语义筛选。官方 `cs.LG/new` 将 `2609.11956` 列为本次 Monday new submission，因此 375 个当窗 identity 最终冻结为 109 个候选与 266 个候选前关闭。29.1% 的保留率只是审计结果，不是反向控制候选数量的配额。

109/109 个当窗候选均已完成与 V3 分数和 Books Gate 相称的 exact-v1 原始证据审阅：83 项深入完成、24 项标准完成、2 项证据后关闭；105 项使用 arXiv HTML，4 项在 HTML 不可用时使用 PDF。未发现撤回、争议或候选级访问阻塞。最终处置为 74 项整合、24 项已有覆盖、8 项仅报告、2 项证据审阅后拒绝、1 项结构候选；74 项长期语义增量已经由对应 Stable Knowledge Node 的正文吸收，未用论文名列表代替机制写入。

上一轮独立语义复核因发现四类系统性漏收而判定失败；本轮重开共享错误理由族后恢复遗漏候选，并由非作者再次执行写后复核。复核同时纠正了 `2609.11956` 的事件归属：arXiv submission history 不是公开时间，官方 Monday new-submission list 才是本窗归属证据。最终 `375 in-window → 109 candidates + 266 closures` 的准入口径、109 项证据边界与评分、Books 决定以及 74 项真实正文落点均已通过检查，Daily Gate 闭合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/RSS；窗口内 09-14 08:00 客户案例已读并因未披露可复核的新系统机制在候选前关闭 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 列表按窗口检查；最新相关条目早于起点 | 已检查 | 无当窗事件 |
| SRC-GOOGLE-AI | DeepMind Research 与 Google Research publication 入口按窗口检查 | 已检查 | 无当窗事件 |
| SRC-META-AI | FAIR/Research 公开入口与可见条目按窗口检查 | 受阻 | 目录缺稳定的日级完整枚举；不能据此证明当窗绝对零事件，取得带发布时间的完整列表后定点重开 |
| SRC-QWEN | Qwen Blog/Research 目录按窗口检查 | 已检查 | 无当窗事件 |
| SRC-DEEPSEEK | 官方 Research/发布入口按窗口检查 | 已检查 | 无当窗事件 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 公开仓库发布事件按窗口检查 | 已检查 | 无改变机制或接口的当窗事件 |
| SRC-TENCENT-HUNYUAN | 官方 Research“全部”列表及公开仓库按窗口检查 | 已检查 | 最新可见研究早于本窗 |
| SRC-ZAI | 智谱 Research 列表、发布说明与公开仓库按窗口检查 | 已检查 | 无当窗事件 |
| SRC-BYTEDANCE-SEED | Seed Research、论文目录与公开仓库按窗口检查 | 已检查 | 无当窗事件 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客与公开仓库按窗口检查 | 已检查 | 无当窗事件 |
| SRC-XIAOMI-MIMO | MiMo 论文卡片与公开仓库按窗口检查 | 受阻 | 公开卡片缺稳定日级发布时间；获得日级列表或唯一新材料身份后定点重开 |
| SRC-MINIMAX | 中英文 Blog、Research 与公开仓库按窗口检查；页面 `dateModified` 未当作材料事件 | 已检查 | 实际内容日期早于本窗 |
| SRC-ARXIV | Monday new list；`cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA`，跨分类去重 375 项；375/375 题摘语义筛选，冻结为 109 候选、266 候选前关闭 | 已检查 | 无 |

Meta 与 MiMo 的目录限制只限制“当窗绝对零事件”的断言，不构成任何候选的 Blocked 状态，也不支持从不可见内容推断机制或写回 Books。

## 3. 候选与判断

评分顺序为 Design Delta / System Reach / Durability。所有 arXiv 事件均以 Monday new list 首次公开为准；论文名称后的版本为本次实际采用的 exact v1。`Primary` 表示直接审阅原论文，不表示作者 benchmark 可脱离其模型、硬件、精度、长度、并发或 SLO 条件外推。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Fixed State, Long Reach（arXiv:2609.11998）](https://arxiv.org/html/2609.11998v1) | 2026-09-14T08:00:00+08:00 | Block diffusion 原先随长度增长的状态代价被精确 block-causal 常数缓存改写，需要核验生成并行与 cache/commit 边界；3 + 3 + 3 = 9。 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Beyond Argmax（arXiv:2609.12099）](https://arxiv.org/html/2609.12099v1) | 2026-09-14T08:00:00+08:00 | 冻结多模态模型组合若过早做 argmax 会丢掉可传递语义，完整分布融合可能改变表示接口；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [The Cost of Compression（arXiv:2609.12111）](https://arxiv.org/html/2609.12111v1) | 2026-09-14T08:00:00+08:00 | 事实幻觉不能只归因于模型能力，rate-distortion 给出了压缩误差与事实覆盖失败的可区分边界；2 + 1 + 3 = 6（由 7 下调，标准审阅足够）。 | 深入完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Chopthin-Consensus Power Sampling（arXiv:2609.12243）](https://arxiv.org/html/2609.12243v1) | 2026-09-14T08:00:00+08:00 | SMC 的等权重重采样会过早杀死可能正确的轨迹，非等权多样性保持改变 test-time reasoning search；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：Weekly-only — `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [The Rank the Task Demands（arXiv:2609.12259）](https://arxiv.org/html/2609.12259v1) | 2026-09-14T08:00:00+08:00 | 在硬单状态瓶颈下，任务代数要求的最小忠实表示维度决定被训练出的 state rank，补充 recurrent memory 容量边界；2 + 1 + 2 = 5（由 6 下调）。 | 标准完成 | 仅报告：Weekly-only — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Breaking the Token Ceiling（arXiv:2609.12303）](https://arxiv.org/html/2609.12303v1) | 2026-09-14T08:00:00+08:00 | matched scaling 比较给出 byte 与 token 模型在数据、性能和 logit 存储上的真实 crossover，而非只比较 tokenizer 偏好；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [OneLA（arXiv:2609.12399）](https://arxiv.org/html/2609.12399v1) | 2026-09-14T08:00:00+08:00 | beam search 不必复制每条 beam 的完整 recurrent state，共享 prompt state 与 append-only transition 改变线性注意力 decode 数据流；3 + 2 + 2 = 7（Durability 由 3 下调）。 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Temporal Recurrence Favors Fewer Layers（arXiv:2609.12531）](https://arxiv.org/html/2609.12531v1) | 2026-09-14T08:00:00+08:00 | temporal recurrence 提供跨步计算后，固定 compute 下的最优分配从层深转向时间状态，改变深度/状态预算判断；2 + 1 + 2 = 5（System Reach 由 2 下调）。 | 标准完成 | 仅报告：Weekly-only — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [TokenMapper（arXiv:2609.12563）](https://arxiv.org/html/2609.12563v1) | 2026-09-14T08:00:00+08:00 | 异构 speech-token space 之间可直接翻译而无需 waveform round-trip，明确暴露 codebook/rate/direction 的互操作约束；2 + 2 + 2 = 6。 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Residual Vector-based Reconstruction（arXiv:2609.12686）](https://arxiv.org/html/2609.12686v1) | 2026-09-14T08:00:00+08:00 | 声称借 FFN activation residual 以近常数显存重建两百万 token 中的事实，若成立会改变长上下文存储设计；主张很强，须重点验证；3 + 2 + 2 = 7（Durability 由 3 下调）。 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [RunningTensor（arXiv:2609.12814）](https://arxiv.org/html/2609.12814v1) | 2026-09-14T08:00:00+08:00 | 将矩阵 recurrent state 推广为高阶 tensor，并保留 recurrent/parallel 线性时间形式，直接改变线性注意力的状态容量设计；3 + 2 + 2 = 7（Durability 由 3 下调）。 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Fewer Words, Not Fewer Tokens（arXiv:2609.12960）](https://arxiv.org/html/2609.12960v1) | 2026-09-14T08:00:00+08:00 | tokenizer 成本应按 proposition 并使用 matched tokenizer 对照，而非按词或单一部署 tokenizer 下结论；2 + 1 + 1 = 4（由 5 下调）。 | 已关闭 | 仅报告：Rejected — `MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [SAS（arXiv:2609.13141）](https://arxiv.org/html/2609.13141v1) | 2026-09-14T08:00:00+08:00 | 稀疏 attention selector 若只蒸馏 dense attention 排名会与固定预算下的 LM 目标错位，端到端 gate 改变训练目标；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Pelican-Sim 1.0（arXiv:2609.12036）](https://arxiv.org/html/2609.12036v1) | 2026-09-14T08:00:00+08:00 | 跨 embodiment 的统一 action 表示、action-to-visual 注入、稀疏容量与少步 rollout 共同定义 world-model simulator 接口；3 + 2 + 2 = 7（Design Delta 由 2 上调，Durability 不上调）。 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Efficient VLA Management and Serving（arXiv:2609.12075）](https://arxiv.org/html/2609.12075v1) | 2026-09-14T08:00:00+08:00 | 机器人工厂中的 VLA pipeline 需要 intra-GPU stage disaggregation、SM 限制与 SLO 调度，改变实时闭环 serving；3 + 3 + 2 = 8。 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Does Video Memory Use What It Retrieves?（arXiv:2609.12090）](https://arxiv.org/html/2609.12090v1) | 2026-09-14T08:00:00+08:00 | read-time substitution 直接区分“有 memory 更好”与“使用了检索内容”，改变视频 memory 的因果评价合同；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [CLAW: Amortized Low-Rank Adaptation for Model-Based RL（arXiv:2609.12278）](https://arxiv.org/html/2609.12278v1) | 2026-09-14T08:00:00+08:00 | world model 的 test-time adaptation 在 ICL 的低成本与 gradient update 的表达力间存在缺口，hypernetwork 生成 LoRA 是可核验分支；2 + 1 + 2 = 5（System Reach 由 2 下调）。 | 标准完成 | 仅报告：Weekly-only — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [AnchorVLN（arXiv:2609.12285）](https://arxiv.org/html/2609.12285v1) | 2026-09-14T08:00:00+08:00 | 将 VLM 限于语义提议、把 metric geometry 交给工具 schema，可避免模型直接编造距离和角度，明确状态/控制边界；2 + 2 + 2 = 6。 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [DATAFARM（arXiv:2609.12316）](https://arxiv.org/html/2609.12316v1) | 2026-09-14T08:00:00+08:00 | 成功的 TAMP demo 若 joint/style/timing 分布与 VLA 预训练不匹配仍可能无效，改变合成数据的可用性判断；3 + 2 + 3 = 8。 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [IMPLY（arXiv:2609.12441）](https://arxiv.org/html/2609.12441v1) | 2026-09-14T08:00:00+08:00 | world-model rollout 的自洽可以稳定地错；由已观察 calibration push 锚定的物理一致性才支持评价；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Agent as Policy（arXiv:2609.12541）](https://arxiv.org/html/2609.12541v1) | 2026-09-14T08:00:00+08:00 | 通用 agent 直接拥有 perception、program、motion command 与 physical-feedback revision，需核验 high-level reasoning 接管控制的适用边界；2 + 1 + 2 = 5（System Reach 由 2 下调）。 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [STAR（arXiv:2609.12549）](https://arxiv.org/html/2609.12549v1) | 2026-09-14T08:00:00+08:00 | tactile 的空间、时间和信息稀疏要求独立 token/预测目标，而非把触觉当普通 dense modality；2 + 2 + 2 = 6。 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Online Material Estimation for Conditioned Diffusion Policy（arXiv:2609.12634）](https://arxiv.org/html/2609.12634v1) | 2026-09-14T08:00:00+08:00 | action policy 在同一目标下仍需在线估计 material state；错误状态估计会成为明确的闭环失效点；2 + 1 + 1 = 4（由 5 下调）。 | 已关闭 | 仅报告：Rejected — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [VideoTok4D（arXiv:2609.12874）](https://arxiv.org/html/2609.12874v1) | 2026-09-14T08:00:00+08:00 | static/dynamic 分解与 track-aligned token 将视频从 image sequence 表示推进到 compact 4D world representation；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Dynin-Robotics（arXiv:2609.13053）](https://arxiv.org/html/2609.13053v1) | 2026-09-14T08:00:00+08:00 | 统一离散 trajectory token 可在一个 masked-diffusion 模型中拥有 action、next observation、goal 与 inverse instruction 多种条件接口；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Rank-Efficient LoRA / Iso-LoRA（arXiv:2609.12123）](https://arxiv.org/html/2609.12123v1) | 2026-09-14T08:00:00+08:00 | nominal rank 不等于 optimizer 实际使用的 effective rank，optimizer 与 adapter capacity 的耦合改变 LoRA 预算解释；3 + 2 + 2 = 7（Design Delta 由 2 上调、Durability 由 3 下调）。 | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [MInTRL（arXiv:2609.12419）](https://arxiv.org/html/2609.12419v1) | 2026-09-14T08:00:00+08:00 | sparse teacher intervention 可以扩展 on-policy 探索而不永久接管 policy，形成 intervention/off-policy contamination 的具体分支；3 + 2 + 2 = 7（Design Delta 由 2 上调）。 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Granularity-Adaptive Credit Assignment（arXiv:2609.12424）](https://arxiv.org/html/2609.12424v1) | 2026-09-14T08:00:00+08:00 | long-horizon agent RL 的 credit granularity 应随 state criticality 变化，而不是给每步广播同一 trajectory scalar；3 + 2 + 2 = 7（Design Delta 由 2 上调）。 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [EvoRS（arXiv:2609.12459）](https://arxiv.org/html/2609.12459v1) | 2026-09-14T08:00:00+08:00 | policy 优化会使固定 reward rubric/DAG 失效，reward system 本身应被视为需要版本与审计的训练状态；3 + 2 + 3 = 8。 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [AMDKernelVault（arXiv:2609.12471）](https://arxiv.org/html/2609.12471v1) | 2026-09-14T08:00:00+08:00 | execution-verified HIP/Triton corpus 与 ROCm 验证扩展 kernel-agent 训练来源，且公开了 correctness/speed 不一致的边界；2 + 1 + 2 = 5（System Reach 由 2 下调）。 | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [CluSTER（arXiv:2609.12584）](https://arxiv.org/html/2609.12584v1) | 2026-09-14T08:00:00+08:00 | 数据约简在 data parallel 下还要同时保证 cluster 与 worker 覆盖，weighted update 承担原分布语义；2 + 2 + 2 = 6。 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Subliminal Learning Reproduction（arXiv:2609.12586）](https://arxiv.org/html/2609.12586v1) | 2026-09-14T08:00:00+08:00 | 语义无关蒸馏可传递行为 trait 但并非普遍发生，受控复现收窄训练数据污染/对齐风险；3 + 2 + 2 = 7（Durability 由 3 下调）。 | 深入完成 | 已有覆盖：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Distortion of AI Alignment Revisited（arXiv:2609.12651）](https://arxiv.org/html/2609.12651v1) | 2026-09-14T08:00:00+08:00 | RLHF 的 distortion 可能主要来自 preference-data 与 KL reference 的分布错配，而非算法必然指数退化；3 + 1 + 3 = 7（System Reach 由 2 下调）。 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Expert-Space Exploration in MoE RL（arXiv:2609.13058）](https://arxiv.org/html/2609.13058v1) | 2026-09-14T08:00:00+08:00 | MoE routing 是额外 rollout exploration state；若 rollout/optimization 不 replay 同一路由会引入 policy mismatch；3 + 2 + 3 = 8。 | 深入完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [CanvasAnneal（arXiv:2609.13060）](https://arxiv.org/html/2609.13060v1) | 2026-09-14T08:00:00+08:00 | teacher-filled diffusion canvas 逐步退火为独立生成，为 diffusion-LM RL 的探索瓶颈提供 curriculum 分支且收益受任务约束；3 + 2 + 2 = 7（Durability 由 3 下调）。 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Hardware-Attributed Operator Profiling（arXiv:2609.11938）](https://arxiv.org/html/2609.11938v1) | 2026-09-14T08:00:00+08:00 | profiler 的 operator identity 需要跨软件层与硬件层保持，且未归因区间必须显式化，才能支持性能判断；2 + 2 + 2 = 6。 | 深入完成 | 整合：`PLATFORM-TRACE` [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [The Battery Price of Edge AI（arXiv:2609.11940）](https://arxiv.org/html/2609.11940v1) | 2026-09-14T08:00:00+08:00 | on-device LLM 的能耗/精度 Pareto 与 quantization 非单调性，加上 embodied carbon，改变“local-first 更绿色”的部署假设；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Vortex（arXiv:2609.12208）](https://arxiv.org/html/2609.12208v1) | 2026-09-14T08:00:00+08:00 | 极端压缩只有被 execution architecture 真正实现才有系统收益，需要核验 VQ/sparsity 与 kernel/runtime 的共同边界；3 + 2 + 2 = 7（从建议 8 下调：系统收益依赖专用架构模型，尚非生产 silicon）。 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [AKTS（arXiv:2609.12276）](https://arxiv.org/html/2609.12276v1) | 2026-09-14T08:00:00+08:00 | 预验证 policy library 把 agent 的 runtime kernel-control 动作缩成安全整数索引，使 verifier failure 离开热路径；3 + 3 + 3 = 9。 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER` [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [Argus（arXiv:2609.12299）](https://arxiv.org/pdf/2609.12299v1) | 2026-09-14T08:00:00+08:00 | semantic region identity 可把 compiler、kernel 与硬件计数联结起来，同时必须暴露跨层 attribution ambiguity；3 + 2 + 3 = 8（从建议 6 上调：stable region identity 与 interference-aware measurement planner 是可跨工具复用的设计增量）。 | 深入完成 | 整合：`PLATFORM-TRACE` [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Equality Saturation for Tensor Programs（EquiForge）（arXiv:2609.12330）](https://arxiv.org/html/2609.12330v1) | 2026-09-14T08:00:00+08:00 | equality-saturation IR 同时表达 algebraic rewrite 与 tiled execution search，改变 tensor compiler 搜索空间组织；2 + 2 + 3 = 7。 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [ForgeMegakernel（arXiv:2609.12379）](https://arxiv.org/html/2609.12379v1) | 2026-09-14T08:00:00+08:00 | decode megakernel 的 agentic synthesis 若配合中间状态 oracle，可把 correctness gate 纳入生成/调优闭环；3 + 2 + 3 = 8。 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Quality-Constrained Quantized MoE Routing（arXiv:2609.12550）](https://arxiv.org/html/2609.12550v1) | 2026-09-14T08:00:00+08:00 | 固定 resident pool 中的 quantized MoE 实例对不同请求有不同质量风险，routing 要同时拥有质量与资源约束；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Dissecting GPU Utilization（arXiv:2609.12923）](https://arxiv.org/html/2609.12923v1) | 2026-09-14T08:00:00+08:00 | 单一 SM utilization 掩盖 fragment fill、occupancy、stall、wave 与 kernel choice，改变 decode 瓶颈的诊断合同；3 + 2 + 2 = 7。 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [SeqMoE（arXiv:2609.12978）](https://arxiv.org/html/2609.12978v1) | 2026-09-14T08:00:00+08:00 | predictive prefetch/cache 与 graph-compatible offload 共同改变 MoE expert state 的驻留和搬运控制；3 + 3 + 3 = 9。 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Pixel Decodability Is Not a Compression Signal（arXiv:2609.13012）](https://arxiv.org/html/2609.13012v1) | 2026-09-14T08:00:00+08:00 | causal intervention 表明可解码像素信息不等于任务使用信息，否定以 pixel reconstructability 作为视觉 KV eviction 信号；3 + 2 + 3 = 8。 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Subquadratic Disaggregation（arXiv:2609.13134）](https://arxiv.org/html/2609.13134v1) | 2026-09-14T08:00:00+08:00 | subquadratic attention 改变 arithmetic intensity 和 state shape，因此 decode disaggregation 边界不应继续沿用 dense-attention 假设；3 + 3 + 2 = 8。 | 深入完成 | 整合：`INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [R2VC（arXiv:2609.11955）](https://arxiv.org/html/2609.11955v1) | 2026-09-14T08:00:00+08:00 | 将 retrieval、verification 与 calibration 分开后可定位错误来源，并给出置信度/abstention 的可检查接口；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Harness or Model?（arXiv:2609.11987）](https://arxiv.org/html/2609.11987v1) | 2026-09-14T08:00:00+08:00 | 同模型配对实验把 agent harness 效应从模型能力中分离，并暴露 task-stratum、成本与污染混杂；3 + 2 + 3 = 8。 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Can We Trust LLM Judges（arXiv:2609.12002）](https://arxiv.org/html/2609.12002v1) | 2026-09-14T08:00:00+08:00 | judge 的 capability-dependent leniency 在 accuracy 控制后仍存在，label-free disagreement calibration 改变 judge gate；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Competence-Gated Pooling（arXiv:2609.12101）](https://arxiv.org/html/2609.12101v1) | 2026-09-14T08:00:00+08:00 | verbal confidence 不能识别模型相对外部先验的边际价值，基于已决 outcome 的 competence gate 才支持 defer；3 + 1 + 3 = 7（从建议 8 下调：直接证据只有 forecasting pooling）。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Certifying Concept Unlearning（arXiv:2609.12163）](https://arxiv.org/html/2609.12163v1) | 2026-09-14T08:00:00+08:00 | 有限 adversarial prompts 的 attack success 会低估全 prompt-space 泄漏，统计 certification 改变 unlearning audit 合同；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [GAUGE（arXiv:2609.12191）](https://arxiv.org/html/2609.12191v1) | 2026-09-14T08:00:00+08:00 | LLM judge 的排序一致不等于 construct validity，agent 用户模拟需要单独判断何时不可信；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ParaRecover（arXiv:2609.12345）](https://arxiv.org/html/2609.12345v1) | 2026-09-14T08:00:00+08:00 | 只看 agent 最终成功率无法定位并行 tool-use 的错误传播，process-level benchmark 补充 localization/recovery 合同；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SynthSentry（arXiv:2609.12353）](https://arxiv.org/pdf/2609.12353v1) | 2026-09-14T08:00:00+08:00 | 在训练前检测 synthetic contamination 是新的 data gate，但小规模结果尚未证明下游损害或 pruning 收益；2 + 1 + 1 = 4（从建议 6 下调）。 | 标准完成 | 仅报告：Weekly-only — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [VRL-Bench（arXiv:2609.12404）](https://arxiv.org/html/2609.12404v1) | 2026-09-14T08:00:00+08:00 | 有限 trial budget 下 reflection 可能降低成功率，评价必须区分经验利用与继续探索；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [SoK: Rethinking Jailbreaking in the Era of Agentic AI（arXiv:2609.12413）](https://arxiv.org/pdf/2609.12413v1) | 2026-09-14T08:00:00+08:00 | 最终回答安全可能掩盖 planning、memory、tool state 已被攻陷，agent security 需要跨层 observer；3 + 3 + 3 = 9。 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Beyond the Query / Do Retrieval Signals Improve Routing?（arXiv:2609.12437）](https://arxiv.org/html/2609.12437v1) | 2026-09-14T08:00:00+08:00 | retrieval feature 只有优于 matched query-only control 才能被归因于 routing value，提供受控负面证据；3 + 1 + 3 = 7。 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [GraphProfiler（arXiv:2609.12448）](https://arxiv.org/html/2609.12448v1) | 2026-09-14T08:00:00+08:00 | source-linked personal KG 将隐私属性推断回溯到具体 post/edge，使泄漏归因与定点缓解可审计；2 + 2 + 2 = 6。 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ZipBench（arXiv:2609.12475）](https://arxiv.org/html/2609.12475v1) | 2026-09-14T08:00:00+08:00 | compact benchmark 若能给出 rank/error guarantee，可在不先拥有大规模 score matrix 时降低评价成本；2 + 2 + 2 = 6。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ProactiveBench（arXiv:2609.12658）](https://arxiv.org/html/2609.12658v1) | 2026-09-14T08:00:00+08:00 | streaming model 不只要答对，还要在 standing request 下决定何时回答与保持沉默，改变时序评价合同；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Historical Corpus Is Not a Historical System（arXiv:2609.12766）](https://arxiv.org/html/2609.12766v1) | 2026-09-14T08:00:00+08:00 | historical replay 只冻结 corpus 仍会被 future interaction memory 泄漏，必须一起版本化 state；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [K-Bench（arXiv:2609.12808）](https://arxiv.org/html/2609.12808v1) | 2026-09-14T08:00:00+08:00 | unlearning 需要检查 weights、prompt、retrieval 与全部 agent channel，而不能以 final refusal 代替知识移除；3 + 3 + 3 = 9。 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MedSNIP（arXiv:2609.12884）](https://arxiv.org/html/2609.12884v1) | 2026-09-14T08:00:00+08:00 | atomic claim 分解可能破坏 causal/conditional 依赖；verification unit 的粒度直接影响正确性与调用成本；2 + 2 + 2 = 6。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Judging by the Cover / Audit-Prune（arXiv:2609.13003）](https://arxiv.org/html/2609.13003v1) | 2026-09-14T08:00:00+08:00 | benchmark 表面线索可让模型在不掌握事实时得分，受控 counterfactual 支持 audit-and-prune release gate；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Tasks over Application Manuals (TAM)（arXiv:2609.13005）](https://arxiv.org/html/2609.13005v1) | 2026-09-14T08:00:00+08:00 | 长手册的多步规则执行显示短链 benchmark 会高估能力，且可比较 RAG/ReAct/harness 的失效边界；2 + 2 + 2 = 6。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MemRetriever（arXiv:2609.11951）](https://arxiv.org/html/2609.11951v1) | 2026-09-14T08:00:00+08:00 | memory access 从固定 top-k 变成可终止的 plan/search/filter 控制环，改变 retrieval state 与停止条件；3 + 2 + 3 = 8。 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Look Before You Leap（arXiv:2609.11957）](https://arxiv.org/html/2609.11957v1) | 2026-09-14T08:00:00+08:00 | deterministic pre-action verification 将 shell/edit 的 silent failure 转化为可检查 abstention，改变 tool commit gate；3 + 2 + 3 = 8。 | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Local Edits, Global Ripples / RIPPLE（arXiv:2609.12127）](https://arxiv.org/html/2609.12127v1) | 2026-09-14T08:00:00+08:00 | prompt-policy 的局部编辑会产生全局和组合效应，持久化前必须以同一基线 replay 并检查交互；3 + 2 + 3 = 8。 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [GuardrailLoop（arXiv:2609.12216）](https://arxiv.org/html/2609.12216v1) | 2026-09-14T08:00:00+08:00 | hash-pinned policy、prefix compute accounting 与 crash recovery 共同定义 durable loop；恢复成功不等于 exactly-once trace；3 + 3 + 3 = 9。 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Sampling via Decision-Flow（arXiv:2609.12317）](https://arxiv.org/html/2609.12317v1) | 2026-09-14T08:00:00+08:00 | 将 terminal utility 沿 reasoning tree 回传给 latent path，为 token-local sampling 提供不同的 test-time control 分支；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：Weekly-only — `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [AIM / Agentic Interoperable Memory（arXiv:2609.12320）](https://arxiv.org/html/2609.12320v1) | 2026-09-14T08:00:00+08:00 | multi-agent/multi-user memory 需要 public/private state、索引级 access control 与 create/update/delete 生命周期；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [CueMem（arXiv:2609.12354）](https://arxiv.org/html/2609.12354v1) | 2026-09-14T08:00:00+08:00 | memory record 应作为指向 source turn 的 cue，而非自包含事实；查询时再重建可追溯 evidence context；3 + 2 + 3 = 8。 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Robust Personalized Alignment / CORE（arXiv:2609.12373）](https://arxiv.org/html/2609.12373v1) | 2026-09-14T08:00:00+08:00 | 将 turn-local observation 与 persistent persona revision 分离，并以不确定性控制 commit，明确 derived memory 的更新权；3 + 2 + 3 = 8。 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [LifeMem（arXiv:2609.12655）](https://arxiv.org/html/2609.12655v1) | 2026-09-14T08:00:00+08:00 | 将 trajectory 聚类为可复用 workflow skill，为跨环境 transfer 与 catastrophic forgetting 提供 memory consolidation 分支；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Skill Issue（arXiv:2609.12742）](https://arxiv.org/html/2609.12742v1) | 2026-09-14T08:00:00+08:00 | repository skill 优化的增益可能落在 agent run-to-run variance 内，说明文档优化必须配 paired baseline 与足够任务数；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [What Drives Recovery in Agentic Text-to-Cypher? / LAST-CQ（arXiv:2609.12746）](https://arxiv.org/html/2609.12746v1) | 2026-09-14T08:00:00+08:00 | counterfactual 显示 recovery 的主要增益来自 failure detection + retry routing，而非复杂 feedback 或并行 sampling；3 + 2 + 3 = 8。 | 深入完成 | 整合：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [The Mechanics of a Swarm（arXiv:2609.12748）](https://arxiv.org/html/2609.12748v1) | 2026-09-14T08:00:00+08:00 | third-party side effects、异步 timing 与缺失 read/outcome logs 使群体 agent 事件无法可靠重建，暴露环境评价合同；3 + 3 + 3 = 9。 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Online Video Agent Harness / VideoXAgent（arXiv:2609.12818）](https://arxiv.org/html/2609.12818v1) | 2026-09-14T08:00:00+08:00 | 对长视频按问题在线寻证并按预算调用工具，可替代 dense context packing，且需处理观察冲突和 non-termination；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |

| [MoPA: Coordinated Mobile Manipulation via Subsystem-Specific Perception Alignment（arXiv:2609.12081）](https://arxiv.org/html/2609.12081v1) | 2026-09-14T08:00:00+08:00 | 用 Mobile Query 与 Manipulation Query 分别读取共享 VLM token，query bank 之间互相 mask，避免在感知阶段提前混合；§III-D 只允许对应 action branch 读取匹配 query，同时在每层 action decoder 中交换…；3 + 2 + 2 = 7。 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [DIA: Denoising Intermediate Advantage for Diffusion Policy Optimization（arXiv:2609.12245）](https://arxiv.org/html/2609.12245v1) | 2026-09-14T08:00:00+08:00 | 把 denoising chain 展平为 primary MDP；§IV-B 推导该 flattened MDP 上的 exact policy gradient；§IV-C 指出同一最终 return 下，部分去噪 action 的条件分布不同，因此 intermediate value 随…；3 + 2 + 2 = 7。 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [DWMP: Leveraging Dual World Models for Humanoid Obstacle Traversal（arXiv:2609.12347）](https://arxiv.org/html/2609.12347v1) | 2026-09-14T08:00:00+08:00 | 的 Auto-Koopman 将低维但非线性的 proprioception 提升到近似线性演化 latent；§III-C 的 RSSM Depth Dreamer 用 deterministic recurrent state + stochastic state 压缩高维、噪声深度观测，训…；3 + 2 + 2 = 7。 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents（arXiv:2609.12394）](https://arxiv.org/html/2609.12394v1) | 2026-09-14T08:00:00+08:00 | 在真实、已登录、联网移动设备上采集完整 trajectory；§2.4 用 heterogeneous triple-system consensus 做轨迹判定与路由；§2.5 先定位失败层级，再做 step correction、保留有效 prefix 的 query adjustment …；3 + 3 + 2 = 8。 | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [UFO: Chain-of-Evaluation for Omni-Condition Alignment in Multi-Modal Image Generation（arXiv:2609.12397）](https://arxiv.org/html/2609.12397v1) | 2026-09-14T08:00:00+08:00 | 把 prompt/参考条件拆为 AEUs；§3.2.2 为每个 AEU 判定 image-only、text-only 或 joint；§3.2.3 按类型调用 VQA 或专用函数（如 identity）；§3.2.4 由 VLM 给出 1–5 relevance weight 后汇总；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [HoliBench: A Cross-Platform Benchmarking and Deployment Toolkit for Foundation Models in CPS-IoT Applications（arXiv:2609.12412）](https://arxiv.org/html/2609.12412v1) | 2026-09-14T08:00:00+08:00 | PAL 统一不同设备 telemetry 的语义单位；§3.2 用同步 bracket 区分 load/prefill/decode 或 vision/decode，并报告 gross 与 idle-subtracted net energy、host/device memory；§3.4 先按…；3 + 3 + 3 = 9。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory（arXiv:2609.12436）](https://arxiv.org/html/2609.12436v1) | 2026-09-14T08:00:00+08:00 | 用 learned orthogonal basis 把 rank-8 memory 分为 stable/plastic 各四行；§4.3 router 由 lifecycle metadata 监督，permanent write 同时更新两类子空间，temporary write 抑制 st…；3 + 2 + 3 = 8。 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Not All Speech Is Intent: Adaptive Self-Correcting Inference Layer for Post-ASR False Wake-Up（arXiv:2609.12469）](https://arxiv.org/html/2609.12469v1) | 2026-09-14T08:00:00+08:00 | base classifier 与 NLU 并行运行；§3.3 ASCIL 从上一轮 repetition、cancellation、silence 等行为信号提炼 FP/FN pattern，记录 noise、word count、energy、rate 及类别/转写一致性，下一轮用于修正 i…；3 + 2 + 2 = 7。 | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [ChitraMiti: Benchmarking Visual Grounding and Modality Reliance in Bengali Geometric Reasoning（arXiv:2609.12509）](https://arxiv.org/pdf/2609.12509v1) | 2026-09-14T08:00:00+08:00 | ChitraMiti-12.8k 是 12,874 个 synthetic Bengali geometry problems，NCTB-500 是 500 个课本图；共享 15-attribute description schema；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [One Skill Does Not Fit All（arXiv:2609.12517）](https://arxiv.org/html/2609.12517v1) | 2026-09-14T08:00:00+08:00 | 论文把长视频 QA 的 frame selection 定义为固定预算下的 evidence acquisition；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [From Collaboration to Capability: RIVET（arXiv:2609.12578）](https://arxiv.org/html/2609.12578v1) | 2026-09-14T08:00:00+08:00 | RIVET 明确分成两个状态阶段；3 + 2 + 3 = 8。 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [SCOPE-OPSD（arXiv:2609.12579）](https://arxiv.org/html/2609.12579v1) | 2026-09-14T08:00:00+08:00 | 方法在 OPSD 上增加 final-layer hidden auxiliary；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：Weekly-only — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Beyond Generation and Accuracy: GeoVAD / GeoWeave（arXiv:2609.12606）](https://arxiv.org/html/2609.12606v1) | 2026-09-14T08:00:00+08:00 | GeoVAD-Bench 的核心不是再加一个最终准确率，而是把视觉几何推理拆成原始感知、辅助图质量、辅助图是否被消费、推理过程与最终答案五个维度；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SteerDuplex（arXiv:2609.12623）](https://arxiv.org/html/2609.12623v1) | 2026-09-14T08:00:00+08:00 | 以 Moshi-based 7B 为底座，先 SFT，再做两阶段 GDPO：每个 reward channel 独立组内归一化，Stage I 用 continuity 项阻止靠短答骗取 timing reward，Stage II 增加 noise/backchannel continuati…；3 + 2 + 3 = 8。 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Breaking the Vision–Action Shortcut: LIT（arXiv:2609.12641）](https://arxiv.org/html/2609.12641v1) | 2026-09-14T08:00:00+08:00 | Latent Interface Training 先做 image-free、spatial-goal-conditioned action pretraining，形成 action prior；再用 pose supervision 训练 action expert 唯一的 latent …；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [IABEdit（arXiv:2609.12691）](https://arxiv.org/html/2609.12691v1) | 2026-09-14T08:00:00+08:00 | 方法把 instruction embedding、source-image embedding 与 source spatial latent 分开；冻结 VLM 在 ground-truth edited image 上生成 Descriptive Anchor，trainable Inst…；2 + 1 + 2 = 5。 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [GRACE（arXiv:2609.12731）](https://arxiv.org/html/2609.12731v1) | 2026-09-14T08:00:00+08:00 | GRACE 用 semantic-weighted PCA 定位 diffusion UNet feature 中的 concept-sensitive low-rank subspace，只训练 adapter；safe anchor 从 text embedding 中去除目标方向，CLIP…；2 + 2 + 2 = 6。 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Balancing Emotional Alignment and Semantic Consistency（arXiv:2609.12830）](https://arxiv.org/html/2609.12830v1) | 2026-09-14T08:00:00+08:00 | 论文把 flow/diffusion sampler 改写为带 tractable transition density 的 stochastic SDE，以 GRPO 优化冻结 valence-arousal regressor 的 terminal reward；另用 neutral zer…；2 + 1 + 2 = 5。 | 标准完成 | 仅报告：Weekly-only — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [TAC-Merge（arXiv:2609.12897）](https://arxiv.org/html/2609.12897v1) | 2026-09-14T08:00:00+08:00 | Multimodal Influence Mapping 同时观察 image/instruction 改变引起的 representation/readout response，并以 Ricci-curvature-style signal 追踪 expert update 的跨层传播；Cou…；2 + 1 + 2 = 5。 | 标准完成 | 结构候选：model capability merging（当前无稳定 owner） |
| [Physics-Aware Video Generation via Agentic Planning and Graph-Guided Optimization（arXiv:2609.13006）](https://arxiv.org/html/2609.13006v1) | 2026-09-14T08:00:00+08:00 | 将一次 video diffusion 拆成两阶段；2 + 2 + 2 = 6。 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Kraken: LLM-based Speech-to-Speech Translation via Low-bitrate VQ and Dual-path Source Conditioning（arXiv:2609.13045）](https://arxiv.org/html/2609.13045v1) | 2026-09-14T08:00:00+08:00 | 将 S2ST 的语义传输和声学保真分责；3 + 2 + 3 = 8。 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Continue, Adapt, or Yield: In-Turn Adaptation to Overlapping Speech in Full-Duplex Agents（arXiv:2609.13117）](https://arxiv.org/html/2609.13117v1) | 2026-09-14T08:00:00+08:00 | 将 listener cue intent（backchannel / collaboration / interruption）与 speaker observed response（continue / adapt / yield）分开；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [InitGen: Candidate Generation for Interaction Initiation in Intelligent Assistants（arXiv:2609.11953）](https://arxiv.org/html/2609.11953v1) | 2026-09-14T08:00:00+08:00 | 系统在用户尚未明确提问前一次生成一组 initiation candidates，之后由既有 filter/ranker 只曝光其中子集；3 + 2 + 2 = 7。 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [HeatCache: Thermal-aware Energy-efficient LLM Inference Scheduling（arXiv:2609.12449）](https://arxiv.org/html/2609.12449v1) | 2026-09-14T08:00:00+08:00 | 把 chassis-level AIO liquid loop 的短时热惯性建模为可消费的 heat budget，而不是只把温度当作事后告警；3 + 3 + 2 = 8。 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [RoofLang: Enabling AI-Driven Architecting of LLM Inference Systems（arXiv:2609.12551）](https://arxiv.org/html/2609.12551v1) | 2026-09-14T08:00:00+08:00 | 定义 typed DSL，将 compute graph、hardware graph、placement、semantics-preserving transformations 和 discrete-event simulation 放进同一 architecture artifact；3 + 3 + 2 = 8。 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Where Decoder Cosine Similarity Fails for SAE Feature Flow Discovery（arXiv:2609.12591）](https://arxiv.org/html/2609.12591v1) | 2026-09-14T08:00:00+08:00 | 同时训练 state SAE 与 MLP-update SAE，以候选 state/update feature 对预测下一 residual target feature；仅用 decoder cosine 排序后，再通过 decoded-update ablation 测 target fe…；2 + 1 + 2 = 5。 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Can LLMs in Draft-Verify-Revise Pipelines Resolve Deictic Ambiguity?（arXiv:2609.12162）](https://arxiv.org/html/2609.12162v1) | 2026-09-14T08:00:00+08:00 | 论文用 controlled minimal pairs 检查 draft→verify→revise context cascade 中同一词 `previous` 的 referent：它可能表示操作时点前的值，也可能被模型错误绑定到名为 Previous 的字段；3 + 2 + 2 = 7。 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents（arXiv:2609.12896）](https://arxiv.org/html/2609.12896v1) | 2026-09-14T08:00:00+08:00 | 在固定 rank 的单一 agent LoRA 中处理 heterogeneous trajectories；3 + 2 + 2 = 7。 | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction（arXiv:2609.13082）](https://arxiv.org/html/2609.13082v1) | 2026-09-14T08:00:00+08:00 | 把 benchmark construction 表成 typed artifact dependency graph，而不是一次性 prompt chain；3 + 2 + 3 = 8。 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

| [Performance, Efficiency and Collapse — Advantages and Challenges in Offline Post-training of Code LLMs（arXiv:2609.11956）](https://arxiv.org/html/2609.11956v1) | 2026-09-14T08:00:00+08:00 | 固定离线偏好对上的 repeated policy-gradient update 会令 policy 离开数据支持域，并出现 ratio、log-prob variance 与正负 likelihood drift 失控；3 + 2 + 3 = 8。 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |

## 4. 证据与知识整合

以下 109 项均直接引用 exact-v1 原始论文。每项把作者材料所支持的机制、不能外推的边界、最终 Books 处置和真实 owner 放在一起；`整合` 表示本轮正文已经落实，`已有覆盖` 表示相同长期命题已经存在，`仅报告`、`拒绝` 与 `结构候选` 均不写入 Books。

### [Fixed State, Long Reach（arXiv:2609.11998）](https://arxiv.org/html/2609.11998v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)

论文在相同 single-frontier block-causal objective 下比较 attention、Mamba 与 hybrid 3B 模型；递归状态不是部署时追加的近似淘汰，而是与训练计算一致的 exact state transition。作者在单张 H100 80GB、bf16、指定 block/step 设置下报告到 256K 的 cache、step latency 与吞吐对照，并观察到训练长度之外的受限外推。

**证据边界：** 常数 footprint 不等于无损记忆；质量、吞吐和外推结论只属于 3B、300B-token recipe、作者 block 设置、H100/bf16 与所测任务，不能外推生产并发或替代逐 token KV。

**Books 对读：** 现有正文已承载相同长期命题。`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：第24章「Cache、rollback 与 exactness」→「Block Cache 可以从历史条目演进为固定大小的递归状态」。现有正文已包含 exact-v1 source-family、旧 KV 路径、训练一致性、有限状态损失和 fallback，无需重复加入。

### [Beyond Argmax（arXiv:2609.12099）](https://arxiv.org/html/2609.12099v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)

在冻结 RegionPLC、SAM3、mask、几何、词表、场景与 fusion 的受控组合中，只改变保留的语义 alternatives；top-1 到 top-2 贡献最大，保留有限 posterior support 或完整分布在两个 3D segmentation 数据集上优于硬 argmax。校准修复没有消除“延迟离散化”的优势，多种替代 fusion operator 也保留方向一致性。

**证据边界：** 只证明该冻结 3D segmentation composition 中，过早 argmax 会丢失可用语义；不证明所有多模态系统都应传递完整分布，也不证明长尾类别可信。小规模 GroundingDINO 诊断不是总体 benchmark。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：第23章「Fusion：在哪里让模态相遇」之后、「对齐不是把向量拉近这么简单」之前。加入“上游 posterior 是下游可消费状态，argmax 是不可逆 commit；只有在 latency/带宽或校准不可靠时才提前离散化”的条件分支。

### [The Cost of Compression（arXiv:2609.12111）](https://arxiv.org/html/2609.12111v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)

随机事实源上的下界把错误拆为“已观察事实的 rate-distortion”与“未观察事实的 coverage”，并在 free-addressing 渐近条件下给出紧性；合成 fact injection 与 LoRA rank 实验只作为容量代理。它明确区分闭卷参数压缩失败与来源未覆盖。

**证据边界：** 均匀、无结构、合成事实与抽象 bit budget 不能变成现实 LLM 幻觉率公式，也不覆盖冲突知识、时效、decoding、calibration 或 instruction pressure。

**Books 对读：** 现有正文已承载相同长期命题。`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)：第5章「记忆与泛化不是简单对立」。现有正文已写入该 exact-v1 的 rate-distortion/coverage 边界，以及 retrieval、verification、abstention 的外部证据路径。

### [Chopthin-Consensus Power Sampling（arXiv:2609.12243）](https://arxiv.org/html/2609.12243v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 仅报告 — `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md)

Chopthin resampling 允许不等权 particles 并维持 ESS 下界，再由 semantic-majority selector 提交答案；3 个开放模型、5 个 benchmark、固定 N=32 的实验显示 oracle coverage 多数提高，但最终准确率取决于 selector，且至少有设置基线最终准确率更高。

**证据边界：** 提高 candidate coverage 不等于提高 accepted answer；结果受 N、温度、模型、benchmark 与 selector 约束，exact power sampling 仍不可行。

**Books 对读：** 作为受限背景证据保留在日报，不扩写正文。`MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md)：第20章「Parallel Sampling：先分开 Coverage 与 Selection」已完整承载 coverage/selection 分权和 correlated-error 边界；Chopthin 是一种受限实现案例，不足以扩充主干。

### [The Rank the Task Demands（arXiv:2609.12259）](https://arxiv.org/html/2609.12259v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 仅报告 — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)

在固定 decoder、单一硬状态矩阵与合成有限群组合任务中，训练得到的有效 rank 与最小忠实实表示维度高度相关；强制 rank 低于阈值产生任务 ceiling，达到阈值后恢复。

**证据边界：** 结论属于高度受控的群任务和硬单状态 bottleneck；它不证明真实 LLM、自然语言长上下文或任意 recurrent architecture 的容量都由同一 representation rank 决定。

**Books 对读：** 仅报告。`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) 只给出一般的有限状态碰撞与容量边界，没有承载该论文在受控群任务中观察到的具体 rank-law；而这一结果的任务与 bottleneck 假设又不足以升级为通用长上下文设计结论，因此保留为 Weekly-only 受限证据，不以主题相近冒充已有覆盖。

### [Breaking the Token Ceiling（arXiv:2609.12303）](https://arxiv.org/html/2609.12303v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)

作者把 token-teacher logits 映射到 byte space，比较近似 marginalization 与 exact end-of-token 两类 distillation interface；在约 1B、layer-matched、最高 1T bytes 的训练与 8 个 benchmark 中，token 模型低 compute 占优但较早平台，byte 模型显示更高拟合上限。真正的新信息是跨表示蒸馏需要定义 teacher probability 如何归属 byte boundary，并同时计算 logit storage/teacher cost。

**证据边界：** “更高上限”和数据倍数主要来自 scaling 外推与固定规模 recipe；不能推出 byte 模型普遍优于 token 模型，也未消除输出合法性、较长序列与大词表 head 的系统成本。

**Books 落点：** 已按审阅锚点落实到正文。`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)：第11章「当 token 进入 Scaling Contract，比较单位必须回到信息量」之后、「Tokenizer 与 checkpoint 是联合行为接口」之前。补入“跨 tokenizer 蒸馏必须定义概率质量的边界映射，byte 作为稳定 denominator 不代表 teacher logits 可直接复用”。

### [OneLA（arXiv:2609.12399）](https://arxiv.org/html/2609.12399v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)

大 beam、短输出的生成式推荐中，所有 beam 共享 post-prefill prompt state，只为各分支保存 append-only transition 与 ancestry index，按需 replay 所需 state；Qwen3.5 0.8B 的 6 attention + 18 GDN 设置给出 operator sweep 和端到端 decode 增益。

**证据边界：** 数据流优化依赖线性 attention/GDN、beam=256 一类大宽度、短输出推荐 workload；不等于普通采样、长生成或任意 recurrent state 都能零成本共享。headline speedup 绑定作者实现和硬件。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)：第54章「混合序列模型需要 Typed Memory Pages」之后。加入“beam state 可拆为共享 immutable root、分支 transition log 与可重建 materialized state；memory owner 保存 ancestry/版本，executor 才按需 replay”的受限分支，并 handoff 第49章 execution plan。

### [Temporal Recurrence Favors Fewer Layers（arXiv:2609.12531）](https://arxiv.org/html/2609.12531v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 仅报告 — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)

Parallel Experts testbed 在近似 matched per-step compute 下改变 step 内 depth、expert 数、width 和是否 recurrent；Sokoban 与小型 FineWeb 结果都提示 temporal recurrence 出现后，较少层可在若干预算点接近更深非递归模型。

**证据边界：** 这是受控小架构/任务上的 compute-allocation 观察，配置按训练回报选优且 compute matching 近似；不能形成“递归模型应更浅”的通则。

**Books 对读：** 作为受限背景证据保留在日报，不扩写正文。`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)：第22章固定状态与 temporal recurrence 主线已说明跨步状态和层内计算是不同预算轴；现有证据不足以改变架构结论。

### [TokenMapper（arXiv:2609.12563）](https://arxiv.org/html/2609.12563v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)

论文在 GLM-4-Voice 单 codebook 与 MiMi/DualCodec 八 codebook 之间直接翻译离散 speech tokens，用 direction/codebook/position embeddings 表达接口身份，避免 waveform decode/re-encode；LibriSpeech/VCTK 的 WER、MOS 与 latency 显示部分方向可行。

**证据边界：** 只覆盖三个 codec、相近 effective token rate、有限英语语音；部分方向 MOS 较低，不能宣称任意声学 token space 可无损互换。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：第23章「连续表示、离散表示与混合表示」中的离散/分层残差表示之后。补入“跨 codec translation 是显式版本化 bridge；codebook、rate、position 与 direction 均属于接口身份，waveform round-trip 仍是兼容 fallback”。

### [Residual Vector-based Reconstruction（arXiv:2609.12686）](https://arxiv.org/html/2609.12686v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)

在冻结 Phi-3.5-mini、Qwen3-4B 与 Llama3.1-8B 上，系统从文本抽取事实，把 FFN activation-derived residual vector 写入分层外部 store，并在查询时重建选中事实；作者在 2M-token 合成/受控单事实检索中仍能回答一部分问题，并把故障拆为 extraction、routing/anchor 和 answer composition。

**证据边界：** “不受上下文窗口限制”必须收窄为“外部选择性单事实重建”；并非模型把两百万 token 保存进常数内部状态。多事实隐含关系、广泛综合、原文引用与 routing failure 明显较弱；memory、latency 与结果绑定作者 pipeline。

**Books 落点：** 已按审阅锚点落实到正文。`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)：第22章「路线五：不把所有信息放进窗口」之后。明确区分 raw-context archive、fact extraction、layer-specific residual store 与 query-time reconstruction；外部 store 拥有事实/版本，activation vector 只是派生索引，失败时回退普通 RAG/原文证据。

### [RunningTensor（arXiv:2609.12814）](https://arxiv.org/html/2609.12814v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)

把 order-2 matrix recurrent state 扩展为 order-o tensor，以 rank-1 outer-product update 和 contraction read 保持 recurrent/parallel 两种线性时间形式；对 order-3 给出性质证明，并在多查询 associative recall、预训练和有限语言/检索任务验证容量方向。

**证据边界：** 理论容量随 `W^o` 增长也意味着内存和算力迅速增长；形式证明主要到 order-3，训练规模和任务尚不足以证明高阶状态是长上下文通用替代。

**Books 落点：** 已按审阅锚点落实到正文。`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)：第22章「从线性混合到原生稀疏」固定矩阵 fast-weight state 之后。作为 `vector summary → matrix association → higher-order interaction state` 的条件演进，保留维度爆炸、优化稳定性和 attention/RAG 共存边界。

### [Fewer Words, Not Fewer Tokens（arXiv:2609.12960）](https://arxiv.org/html/2609.12960v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 已关闭 · **Access：** HTML · **Books：** 仅报告（证据后改判排除） — `MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)

matched BPE 对照把 Sanskrit/English 的 proposition-level token ratio 分解为字符长度与 tokens/character，说明按“词更少”推断 token 成本不成立；不同词表和 domain 的方向并不一致。

**证据边界：** 语言、翻译长度、诗体/散文和 corpus domain 的强限制使它不能支撑通用 tokenizer 设计更新；没有给出新的模型或系统机制。

**Books 对读：** 证据审阅后不满足长期正文门槛，不写入 Books。`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)：第11章「多语言中的隐藏不公平」已经要求按语言切片测 token fertility；无需加入单语言案例。

### [SAS（arXiv:2609.13141）](https://arxiv.org/html/2609.13141v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)

冻结 Qwen3 4B/8B/14B 主体，只训练 sparse-attention selector；相对以 dense-attention ranking 为教师的 selector，SAS 把连续 gate 注入 attention logits，使 selector 直接从 LM loss 获得任务梯度，并用 fused Triton 路径执行。reasoning、LongBench、BFCL 的 tight-budget 对照支持“attention similarity 与有限预算下的 task utility 不同”。

**证据边界：** 128K 仍与 full attention 有明显差距，pooled block summary 会丢失细粒度局部信息；结果绑定 Qwen3、作者预算、selector 结构与 benchmark，不能宣称端到端 gate 普遍胜过蒸馏 selector。

**Books 落点：** 已按审阅锚点落实到正文。`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)：第22章「Selector 可以进入 Forward，但必须显式承担语义责任」。补入 `attention-score imitation → task-loss-trained differentiable gate` 的演进，同时保留 full-attention fallback、tight-budget operating point 与 pooled-summary failure。

### [Pelican-Sim 1.0（arXiv:2609.12036）](https://arxiv.org/html/2609.12036v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)

以 28D 统一 robot action value 加 URDF/camera 渲染的 action video，把跨 embodiment action 注入视频 world model；通过 sparse MoE 容纳 real/sim heterogeneity，并将 35-step teacher 蒸馏为 4-step causal rollout。约百万 real/sim trajectories 支持 policy learning、rollout evaluation、action selection 和 OOD test 的受限链路。

**证据边界：** mixed-domain ablation 同时改变语料规模与多样性，不能唯一归因 domain mixing；action schema、camera/URDF、模型与评测均绑定作者系统，生成视频仍不等于物理真值或可安全执行 transition。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：第25章「Action-conditioned transition」之后、「Latent dynamics」之前。写入“跨 embodiment action 必须经版本化 schema/geometry 映射进入 transition；action video 是 conditioning protocol，不是 control authority”，并 handoff 第26章真实 controller。

### [Efficient VLA Management and Serving（arXiv:2609.12075）](https://arxiv.org/html/2609.12075v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

对四类 VLA pipeline，将 VLM 与 action-diffusion stage 在同 GPU 内分 stream 管理，用 SM restriction 约束长 stage 干扰，再由 SLO-aware scheduler 协调模型和请求；作者在 4×RTX 6000 Pro、LIBERO request replay 上报告 98% SLO attainment operating point。

**证据边界：** 结论属于 local edge server、指定模型、负载、action frequency 与 SLO；“可服务机器人数量”不能外推网络延迟、真实 factory safety 或其他 GPU。跨 GPU disaggregation 在模型放不下/阶段更长时仍合理。

**Books 对读：** 现有正文已承载相同长期命题。`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：第26章「Streaming VLA 必须版本化 Observation、Buffer 与 Control Deadline」后续段落。现有正文已包含 exact-v1、同卡 stage/SM partition、admission、fallback 与实验边界。

### [Does Video Memory Use What It Retrieves?（arXiv:2609.12090）](https://arxiv.org/html/2609.12090v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)

在 read time 替换 retrieved memory、保持其余 pipeline 不变，对 DINO-WM、WorldMem、SAM2 做因果审计：部分 world-model 增益主要来自 representation repair，即使换成不匹配内容仍可改善；WorldMem 有分级依赖，而 SAM2 更依赖精确空间内容。该实验把“系统有 memory”与“输出使用了其内容”分开。

**证据边界：** 三个系统的 task、memory representation 与 readout 不同，不能形成统一 memory 排名；替换实验只定位依赖性，不证明被读取内容真实、充分或对最终决策安全。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：第25章「Memory 架构为何从静态 cache 演进」之后、「Evaluation：从画面质量到干预结果」之前。加入 matched/mismatched/identity-free substitution 作为 content-specificity gate，并区分 representation repair 与 factual/spatial recall。

### [CLAW: Amortized Low-Rank Adaptation for Model-Based RL（arXiv:2609.12278）](https://arxiv.org/html/2609.12278v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 仅报告 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)

hypernetwork 从少量 test transitions 生成 world-model LoRA，在训练时与 base world model 联合学习；测试时无需 gradient loop，形成 ICL 与 gradient adaptation 之间的 amortized branch。受控 locomotion/manipulation families 和 5 seeds 支持较短 adaptation time。

**证据边界：** 已知环境族、较小 MBRL、少量 episode context；代码仅声明随最终版本提供。未证明开放 world model、跨 embodiment 或长时部署漂移能由生成 LoRA 可靠吸收。

**Books 对读：** 作为受限背景证据保留在日报，不扩写正文。`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：第25章「World Model 与 Agent Memory 的边界」与第30章「从学习适配器到生成适配器」已提供足够 owner 和 operating-regime 边界；本论文不足以改变主干。

### [AnchorVLN（arXiv:2609.12285）](https://arxiv.org/html/2609.12285v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

VLM 只提出语言语义与对象 handle，10 个 MCP tools 接受 phrase/handle 并由 geometry service 计算 metric distance/angle/pose；接口明确禁止模型直接输出 metric numbers。CMU challenge dev 的有限导航任务说明这种 authority split 可执行。

**证据边界：** 约 30 个 instruction questions、15 scenes、单一 Claude model、2Hz 且单步约 30 秒，不足以证明低延迟控制或跨模拟器泛化；MCP 只是接口载体，不是几何真实性来源。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：第26章「Grounded language 是可消费观测，不必成为控制关键路径的生成物」。补入 `semantic proposal → typed object handle → deterministic metric tool → controller commit`，保留显式 geometry fallback 和低层 authority。

### [DATAFARM（arXiv:2609.12316）](https://arxiv.org/html/2609.12316v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)

从 DROID reference 分别拟合 joint configuration density 与 trajectory latent density，把 TAMP 成功轨迹在配置、motion style 和 execution timing 上对齐后再训练 VLA。三个 tabletop tasks 与 cloth retention 中，raw task-valid TAMP demonstrations 明显弱于 aligned data；移除 timing alignment 的消融尤其暴露 deployment dynamics mismatch。

**证据边界：** 一个 VLA/platform、有限任务与目标域；成功率变化不能拆成每个对齐组件的普遍因果份额，也不证明所有 synthetic data 都应模仿人类风格。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)：第27章「从 Trajectory Count 到 Primitive × Transition Coverage」之后。增加“任务成功只是 validity gate；joint/state density、trajectory style 与 timing 必须对齐目标 policy/embodiment”的 behavior-distribution contract，并 handoff 第26章 control frequency。

### [IMPLY（arXiv:2609.12441）](https://arxiv.org/html/2609.12441v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)

inverse simulator 从多条 rollout 推断 mass/friction 等潜变量，再用两次真实 calibration push 锚定；受控实验显示“典型物体”predictor 可以内部完全自洽却物理错误，而 anchor-based detector 明显提高错误识别。对 V-JEPA2-AC 的自有/错配 calibration 对照进一步支持 anchor identity 必须匹配对象。

**证据边界：** 已知 simulator、单类 contact、少量 calibration pushes，且继承 simulator error；pixel-only 路径未得到同等验证。高 AUROC/相关性只属于作者设置，不能转化为普遍 safety guarantee。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：第25章「Imagined Rollout 只有经过校准，才能进入控制」。补入“self-consistency 只能验证内部闭合；物理参数 verdict 需要 observation-backed calibration anchor，并绑定 object/environment revision”。

### [Agent as Policy（arXiv:2609.12541）](https://arxiv.org/html/2609.12541v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

通用 agent 生成程序、发出运动命令并依据物理反馈修订；单一真实机器人设置中，多数配置达到较高小样本成功率，说明 high-level program synthesis 可以进入控制 proposal loop。

**证据边界：** 单一 hardware/interface、每配置试验数少、执行时间和成本高；未证明通用 agent 应拥有低层 commit、安全 envelope 或实时 control authority。

**Books 对读：** 现有正文已承载相同长期命题。`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：第26章「从语言推理到 One-step Meta-action」「Learned Controller 必须位于可验证的 Runtime Assurance 之内」。现有正文已规定模型/Agent 只拥有 proposal，controller/safety monitor 拥有动作提交；论文不改变该结论。

### [STAR（arXiv:2609.12549）](https://arxiv.org/html/2609.12549v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)

200h、10,576 trajectories、65 tasks 的 vision–tactile pretraining 使用 sparse-global tactile tokens 与 sparse future tactile prediction，使高频但多数时刻信息稀疏的触觉不必复制成 dense visual stream；有限真实任务 post-training 提供受限可行证据。

**证据边界：** 单一 dexterous hand/sensor stack、任务和数据规模有限；tactile 在部分任务无益，未验证 sensor drift/noise、语言对齐或跨 embodiment 迁移。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：canonical owner 调整为 `MULTIMODAL-REPRESENTATION` → 第23章「Token Hierarchy 可以承载不同时间尺度」之后；写入“event-sparse tactile stream 需要独立 rate/timestamp/calibration identity 与 sparse prediction target”。第25/26章只短 handoff 到 contact belief 与 action commit。

### [Online Material Estimation for Conditioned Diffusion Policy（arXiv:2609.12634）](https://arxiv.org/html/2609.12634v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 已关闭 · **Access：** HTML · **Books：** 仅报告（证据后改判排除） — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

在线 recurrent material classifier 每步读取 multi-view images/joint state，再条件化 diffusion action sequence；480 demos、4 materials、3 groove tasks 表明 material state 对该 manipulation pipeline 有用。

**证据边界：** 狭窄任务、材料集合和单一 policy；estimated labels 经常不准确但策略仍成功，说明机制解释并不唯一。没有形成可迁移的大模型/VLA 架构或平台 contract。

**Books 对读：** 证据审阅后不满足长期正文门槛，不写入 Books。`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：第25章已将摩擦/接触列为不可观测 belief state，第26章已有 sensor/action freshness；无需加入单领域案例。

### [VideoTok4D（arXiv:2609.12874）](https://arxiv.org/html/2609.12874v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)

通过 static/dynamic token disentanglement、track-aware attention 与 4D diffusion prior，把多视角视频从 frame sequence 压成可追踪的动态对象/静态背景表示；MultiCamVideo 13,600 scenes、10 cameras、400 asset-disjoint test 与 capacity-matched ablation 支持 representation/storage 方向。

**证据边界：** 主要在单一合成/构建数据集、估计 tracks 与 camera geometry 上评估；“四个数量级存储”依赖比较表示和 operating point，不证明物理动力学、真实控制或任意视频域。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：第23章「Native 3D Token 把几何从 Sidecar 变成可修订状态」之后。补入 `frame tokens → track-aligned static/dynamic identity → compact 4D generative state`，并把 transition truth 交回第25章。

### [Dynin-Robotics（arXiv:2609.13053）](https://arxiv.org/html/2609.13053v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

用同一 masked-diffusion trajectory sequence 表示 language、visual states、goals 与 actions，通过 condition/target spans 训练 action prediction、next observation、terminal goal 和 inverse instruction；1.33M trajectories/48 OXE datasets 及 simulated/real robot evaluations 支持统一 conditional interface。

**证据边界：** action discretization、辅助损失权重和 benchmark 饱和会影响结果；29.2× 是作者实现的生成速度，不是生产 VLA SLO，也不证明单一模型应取代模块化 controller。

**Books 落点：** 已按审阅锚点落实到正文。`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：第26章「Action representation」之后。加入“统一 trajectory token 只统一 condition/target protocol，不统一 state truth 或 action authority”；第24章只 handoff masked-diffusion 的可变位置/commit 语义。

### [Rank-Efficient LoRA / Iso-LoRA（arXiv:2609.12123）](https://arxiv.org/html/2609.12123v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)

从 weight-space tangent spectral descent 推导耦合的 LoRA A/B update，使低秩因子更新更接近目标权重更新；0.1B–7B 模型、独立超参搜索和约 2000 H100-hours 的实验支持“nominal rank 不等于 optimizer 实际使用的 effective rank”。

**证据边界：** 一阶理论省略 damping、momentum、weight decay 等现实项；结论不能变成固定 rank recipe，且大规模结果仍受模型、数据和训练预算约束。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)：第30章「Rank 与 target modules 决定更新空间」。在“rank 不是任务本质维度”之后加入 `nominal factor rank → optimizer-induced effective rank`，要求 rank、初始化、optimizer transform 与实际谱共同成为 adapter capacity evidence。

### [MInTRL（arXiv:2609.12419）](https://arxiv.org/html/2609.12419v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

judge 在 rollout 过程中只于错误 suffix 注入简短 correction，随后把生成权交回 learner；sequence-level advantage regression 避开逐 token importance sampling。Qwen3 1.7B/4B 的数学/代码实验及 intervention-rate 对照显示中等干预比完全接管或零干预更稳健。

**证据边界：** teacher/judge 质量与成本是核心依赖；被纠正轨迹已不再是纯 learner on-policy data，`semi-on-policy` 不能省略 contamination/staleness 身份。结果仅覆盖作者模型、任务和 500-step 设置。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)：第33章「Scaffold 可以退火，但不能假装从未存在」与「Teacher Signal 要跟随 Learner 的当前 Rollout Distribution」之间。增加“局部 suffix correction 形成带干预 provenance 的 trajectory；teacher 只拥有纠错 proposal，learner 恢复控制，更新必须识别 intervention span”。

### [Granularity-Adaptive Credit Assignment（arXiv:2609.12424）](https://arxiv.org/html/2609.12424v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

用 token NLL-derived state criticality 在 step-level 与 episode-level advantage 之间调节 credit granularity；ALFWorld/WebShop、1.5B/7B 的 matched mean-weight 对照支持“所有步骤广播同一 scalar”与“全程细粒度 credit”之间存在条件分支。

**证据边界：** NLL 只是 state criticality proxy，不是因果贡献；两个 agent benchmark 和有限模型不足以提供通用阈值，理论条件也不证明真实长程环境满足假设。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)：第33章「多步 Credit 要先分配给 Action，再分配给 Token」。补入“credit granularity 由可观测 criticality proposal 调节，但终局 verifier 保留 authority；proxy 失配时回退 episode/step fixed branch”。

### [EvoRS（arXiv:2609.12459）](https://arxiv.org/html/2609.12459v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)

将 reward criteria 组织成可变 Reward-DAG；on-policy responses 与 node-level reward traces 反馈给 agentic designer，后者更新节点/边而非只调整一个 scalar。开放写作/角色扮演任务同时追踪 reliability、coverage 与 informativeness，显示 fixed rubric 会随 policy 分布移动而失效。

**证据边界：** 评价仍高度依赖模型 judge，开放任务没有独立真值；reward designer 可能过拟合、引入新的 reward hacking 或审计攻击面。不能宣称自演化 reward 自动变得更客观。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)：第31章「Reward Model 也有 Policy-relative State」之后。增加 `fixed scalar/rubric → versioned reward graph → policy-relative mutation proposal → held-out/human gate`，明确 designer 不拥有 truth 或 release authority。

### [AMDKernelVault（arXiv:2609.12471）](https://arxiv.org/html/2609.12471v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)

数据集含 62,153 HIP kernels、39,893 Triton kernels 与 2,377 ROCm QA；generation/evaluate/reflect 流程以编译、correctness 和 speed feedback 验证训练样本，Qwen3-8B SFT+RL 展示 corpus utility，同时暴露“正确率最高不一定 compilation/speed 最优”。

**证据边界：** AMD/ROCm、MI355X、固定 iteration budget 与指定 kernel/task；数据集规模和作者 benchmark 不构成新的通用训练机制，也不证明生成 kernel 可直接发布。

**Books 对读：** 现有正文已承载相同长期命题。`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：`INFER-EXECUTION` → 第49章「Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission」「Kernel Agent 应生成 Typed Schedule」。现有主干已完整规定 generator/compiler/correctness/profiler 分权；本项只作为受限 corpus/artifact 事实留在报告。

### [CluSTER（arXiv:2609.12584）](https://arxiv.org/html/2609.12584v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)

以 final hidden state/token probability 构造 gradient proxy，先做 cluster-aware data reduction，再做 DP-aware balanced allocation；weighted updates 试图保留原数据分布。4→8 GPUs、7B/13B 和多 instruction datasets 的结果显示 data reduction 与 worker assignment 必须联合考虑。

**证据边界：** gradient proxy、cluster、保留率和收益都绑定作者数据/模型/超参；加权只近似原分布，不证明相同梯度或泛化。极端稀有/安全样本可能在聚类约简中丢失。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)：第27章「Streaming 与随机性」中 worker 重复/遗漏段落之前。加入 `semantic/gradient clustering → coverage-preserving selection → DP worker allocation → weighted update`，要求 cluster coverage 与 worker exposure 分别验收。

### [Subliminal Learning Reproduction（arXiv:2609.12586）](https://arxiv.org/html/2609.12586v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)

在 Qwen2.5、Gemma3、Ministral 等开放权重模型与新增 traits/tasks 上复现“语义无关训练输出传递行为 trait”的一部分现象，同时观察并非所有模型都出现、较小 answer space 往往更强，从而收窄而非无限扩大原主张。

**证据边界：** 原始 GPT-4 fine-tuning 不可复现，模型 family 和训练接口不同；trait/task/answer-space 有限，不能推导通用隐藏信道或所有蒸馏数据都有相同风险。

**Books 对读：** 现有正文已承载相同长期命题。`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)：第27章「Synthetic data：从先生成再打分到 Specification Compilation」已规定语义表面无害不等于行为中性及 behavioral canary；第72章已有 subliminal-learning 的 channel-specific audit。新论文加强 replication boundary，但不改变现有长期命题。

### [Distortion of AI Alignment Revisited（arXiv:2609.12651）](https://arxiv.org/html/2609.12651v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)

理论上下界指出 RLHF distortion 的关键量是 preference-data distribution `mu` 与 KL reference `pi_ref` 的 log density-ratio bound，而不只是 Bradley–Terry specification；当二者一致时给出较温和的 beta scaling。小型 reward model 与三选项合成实验只作方向验证。

**证据边界：** utilitarian average、BT、clipping、KL regime 等假设很强，实证规模小；不能把定理直接变成生产 distortion 估算，也不证明 distribution matching 足以解决 reward hacking。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)：第31章「改变输出分布是目标，不是无副作用的偏好标签」之后。补入“KL reference 只定义更新坐标；若 preference sampling distribution 与 reference coverage 不同，平均 KL 无法控制未覆盖区域的 distortion”。

### [Expert-Space Exploration in MoE RL（arXiv:2609.13058）](https://arxiv.org/html/2609.13058v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

对 MoE router logits 加扰动，保留高置信 anchor experts、从 plausible pool 采样其余 experts，并按 entropy 调节噪声；关键系统语义是 rollout 时记录 expert path，优化时 replay 相同路由，避免 behavior/output 相同表面下的条件计算路径 mismatch。

**证据边界：** 结果属于 Qwen3 30B-A3B、Sigma、Moonlight 和作者 math/science/code benchmark；推理时关闭扰动，额外 route metadata、负载/placement 和 replay 可用性仍有成本。“无额外 compute”不能外推 runtime/communication overhead。

**Books 对读：** 现有正文已承载相同长期命题。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)：第33章「MoE Route Replay 也属于 Behavior-policy Identity」。现有正文已覆盖 route metadata、expert availability、staleness、current-policy fallback 与实验边界；无需再写同义段落。

### [CanvasAnneal（arXiv:2609.13060）](https://arxiv.org/html/2609.13060v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

在 diffusion LM RL 训练中把 teacher reasoning tokens 注入可编辑 canvas，随训练退火 masking ratio，同时保留一部分 pure-noise inputs；teacher 在 inference 完全移除。LLaDA7B-A1B 的数学/Tau2 结果和 ablation 显示 pure-noise fraction 是避免 learner 只依赖 teacher state 的关键，但并非所有 benchmark 都优于 diffu-GRPO。

**证据边界：** 单一 backbone、任务依赖、teacher 生成成本与训练依赖明显；GSM8K 等反例禁止写成普遍升级路线。teacher-filled canvas 是 curriculum state，不是独立真值或永久 inference context。

**Books 落点：** 已按审阅锚点落实到正文。`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)：第33章「Scaffold 可以退火，但不能假装从未存在」。增加 diffusion 分支：`teacher-filled mutable canvas → mask annealing + pure-noise floor → teacher-free rollout`，并 handoff 第24章 editable-token/commit semantics。

### [Hardware-Attributed Operator Profiling（arXiv:2609.11938）](https://arxiv.org/html/2609.11938v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-TRACE` [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)

作者把 PyTorch operator、编译器 fusion map 与 GPU 硬件计数连接成同一归因链。实现使用 CUPTI correlation、逐 stream 的 NVTX interval tree，并按 invocation order 而不是跨时钟 timestamp 对齐 NCU/NSYS；无法归因的 cuDNN 区间被显式保留，而不是分摊掉。RTX PRO 6000 Blackwell 上，编译 workload 的归因覆盖为 95–100%，但 cuDNN workload 可有超过 85% 未归因；两个编译案例报告 1.76–2.24 倍 profiled-kernel-time 改进。

**证据边界：** 只有单一 GPU 架构、GPT-2/SDPA/LSTM 小组工作负载与两次测量点；没有端到端 wall-clock 证明，cuDNN 归因仍弱。论文证明“语义归因和 ambiguity 必须共同输出”，不证明该工具能覆盖所有 runtime。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-TRACE` [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)：在 `### 跨节点时间戳不是天然的因果顺序` 之后、`## Metrics、Logs 与 Traces 的互补` 之前加入“跨 profiler 的 invocation/region identity 优先于 timestamp；未归因区间是一等证据”的短节，并与后文 `### Failure Attribution 必须从阶段定位升级到可证伪的因果候选` handoff。

### [The Battery Price of Edge AI（arXiv:2609.11940）](https://arxiv.org/html/2609.11940v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)

论文比较三个模型家族、18 个模型/量化配置，在 Pixel 8、iPhone 14 与 A100（含/不含 batching）上同时测量 energy/token、TTFT/ITL、accuracy 与电池循环寿命。测试中本地推理平均比 batched server 低约 3 倍能效，量化收益非单调，Q4 是这组设备上的 Pareto sweet spot；其生命周期模型中 embodied carbon 占主导，因此“local-first 天然更绿色”并不成立。

**证据边界：** 设备仅两款手机和一个服务器；本地与服务器能耗测量方法异构，energy/token 不含 prefill；5–7 倍与 88–90% 等数字依赖电池、使用率和生命周期假设，不能作为通用常数。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)：在 `### Generation Energy 不是 Token 数的线性函数` 后增加“on-device 的分母必须同时结算 prefill、batch 利用率、电池循环与 embodied cost”，并回链 `### Utilization 应由实际负载推出，而不是由计算器假定`。

### [Vortex（arXiv:2609.12208）](https://arxiv.org/html/2609.12208v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)

Vortex 将 vector-quantized weights、运行时 KV 量化、vector/codebook 粒度的 contextual sparsity 与 prefill/decode 两条执行流共同设计。Llama2-7B/13B、Mistral-7B 与 2-bit AQLM 工作负载中，作者报告相对所选 accelerator baseline 的 8.03–23.7 倍加速和 5.68–12.5 倍能效，并在两款 Llama 上以 30%/25% 稀疏度维持至少 95% 的相对 AQLM accuracy。

**证据边界：** 结果来自架构/模拟评估与特定任务、压缩方案和硬件假设，不是生产加速卡实测；相对 accuracy 也不是完整质量/SLO 合同。可沉淀的是 compression artifact 与 execution plan 必须共同设计，而非这些倍率。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：在 `## 从计算图开始` 的 operator fusion/scheduling 之后、`### 从逐 Kernel Launch 到 Persistent Executor` 之前增加“压缩只有进入 load/decode 数据流才形成系统收益”，并在 `## 量化为什么不自动带来加速` 回链其 coexistence boundary。

### [AKTS（arXiv:2609.12276）](https://arxiv.org/html/2609.12276v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-GPU-SCHEDULER` [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)

AKTS 把 reasoning plane 与 kernel execution plane 分离：策略库预先编译并通过 verifier，运行时 Agent 只能写入一个整数 selector，由内核 tail call 选择既有策略。因此模型没有生成任意 kernel 行为的权限。Linux 6.14 `sched_ext` 原型报告约 920 ns p50 切换开销；60,217 次非法索引调用保持 inert；vLLM oracle 切换覆盖 97% batch work，并对 latency burst 作出响应。

**证据边界：** 真正验证的是“预验证策略库 + 有界 selector”的控制结构与 oracle switching，不是 learned agent policy 的安全性或收益；实现绑定 Linux `sched_ext`，也没有证明跨内核/跨集群适用。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-GPU-SCHEDULER` [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)：在 `## 与推理 Scheduler 的边界` 后加入“语义策略只能产生 policy ID，kernel hot path 只执行已验证动作”的 bounded-control 分支；强调 policy generation 不拥有 execution authority。

### [Argus（arXiv:2609.12299）](https://arxiv.org/pdf/2609.12299v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** PDF · **Books：** 整合 — `PLATFORM-TRACE` [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)

Argus 以稳定 region ID 贯穿编译、lowering、执行与 variant，并用 `observe(region, signals, scope)` 声明观测。measurement planner 把 reference tracing、forced-wait probe、CUPTI/NVBit/Nsight 采集拆成互不干扰的多轮 DAG，再以 region/dynamic context 合并，输出 provenance 与 ambiguity。Hopper 案例包括 AlphaEvolve 的 44 个 kernel、TinyLlama decode megakernel 与 2/4 GPU PGO。

**证据边界：** 不同工具轮次不是同一次执行，forced-wait 与 instrumentation 仍会扰动 workload；tiny kernel 的 reference tracing 开销可到 10.5–13%。案例改进不能外推，核心证据只支持“region identity + measurement-plan provenance”。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-TRACE` [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)：与 2609.11938 共用一个 owner，在 `## 从 Linear Trace 到 Root-cause Graph` 前补“稳定 semantic region 是跨编译/硬件 join key；互相干扰的 sensor 必须分轮运行并保存 provenance”。

### [Equality Saturation for Tensor Programs（EquiForge）（arXiv:2609.12330）](https://arxiv.org/html/2609.12330v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)

EquiForge 用一个 typed IR 同时表示高层 tensor algebra 与 tiled parallel implementation，让 equality saturation 组合 algebraic rewrite、early compaction 与 subgraph composition，而不是先固定图再局部 autotune。系统能推导 fused online-attention/FlashAttention-like 形式；作者在所选 workload 上报告相对每配置最快 baseline 的 1.32 倍几何平均、最高 2.74 倍，以及若干 QK/MLA/mHC 个案收益。

**证据边界：** 收益绑定测试算子、形状与 baseline；论文没有建立搜索/编译开销和生产 workload 的通用上界。长期结论是“代数等价与 tile/schedule 搜索需要共享 typed state”，不是某个速度数字。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：在 `## 从计算图开始` 内，把现有 graph rewrite 推进为“typed equality space → implementation schedule → cost selection”的演进链；与 `### Generated Kernel 必须先进入 Typed Schedule IR` 互相引用而不重复。

### [ForgeMegakernel（arXiv:2609.12379）](https://arxiv.org/html/2609.12379v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)

系统按十个递进 milestone 让 coding agent 生成每模型 decode megakernel，并用独立的 mid-state oracle 检查中间状态，而非只看最终 token。运行时采用每 SM instruction stream、dependency counter 与 shared-memory buffer pool。单张 H100 80GB、bf16 weights/KV、14 个算子和八个模型家族上，报告 50.5–85.9% MBU，相对 SGLang 0.5.18 几何平均 1.21 倍，嵌入 SGLang 后为 1.11 倍且保持可比 accuracy。

**证据边界：** 只有 H100 单架构；agent 生成流程、milestone portability、shared-memory pressure 和更广模型正确性未被证明。mid-state oracle 是 correctness gate，不等于形式验证。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：在 `### 从逐 Kernel Launch 到 Persistent Executor` 后加入“生成 megakernel 必须以 typed schedule 和 mid-state oracle 收窄搜索”，与 Ch49 现有 `### Generated Kernel 必须先进入 Typed Schedule IR` 合并重排。

### [Quality-Constrained Quantized MoE Routing（arXiv:2609.12550）](https://arxiv.org/html/2609.12550v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)

工作负载在固定、已物化的 quantized MoE resident pool 中选实例，并用 prefill 预测请求级质量退化；两专家 affinity/fragility 分解、跨层修正与 LP/KKT price 将质量预算和资源预算合并。88 条扩展 Qwen prompts、W2/W3/W4 组合中，离线模型报告 1.284 倍 multiplier，相比 request-agnostic 1.253 倍与 W4 基线 1.0。

**证据边界：** 这是小样本、离线、model-based routing；不包含真实拓扑、实例 provisioning/reconfiguration、在线 drift 或 tail SLO。不能把 1.284 倍视为部署收益。

**Books 对读：** 现有正文已承载相同长期命题。`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)：现有 `### MoE Decode：从 Queue Length 到 Expert Working Set`、`### Expert weights 与 KV 的联合 working set`、`### Calibration 是在线 Routing State` 已承载“质量与驻留/预算联合 routing”；本论文只作为受限证据，不新增机制正文。

### [Dissecting GPU Utilization（arXiv:2609.12923）](https://arxiv.org/html/2609.12923v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)

论文把单一 SM utilization 拆成 fragment fill、occupancy、stall、wave 与 kernel choice 等八个 counter-pinned view，并区分 cold/warm、prefill/decode 与 layer role。vLLM + FA3 + cuBLASLt、H100 NVL、四个生产模型的实验显示，Hopper BF16 GMMA 的 64-row fragment floor 可让小 batch decode 同时呈现高 busy 和低 useful fill；FA3 decode 的 stall 又是另一类瓶颈。

**证据边界：** 只覆盖 Hopper/H100、选定 kernel 和 NCU 计数口径；不能据此给出跨架构阈值，也未直接证明任何调度策略的端到端收益。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)：在章节开头的 memory hierarchy 引入之后、`## 显存里到底有什么` 之前增加“utilization 必须分解为有效 fragment、驻留、stall、wave 与 kernel choice；高 busy 不能推出显存或算力被有效使用”，并 handoff Ch69 的证据归因。

### [SeqMoE（arXiv:2609.12978）](https://arxiv.org/html/2609.12978v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)

SeqMoE 将 expert activation prediction 写成跨 token/层的 sequence model，用 job-sequencing deadline 调度 prefetch、以 probabilistic Belady 管理 cache，并通过 compute-transparent placement 与无同步 orchestration 保持 graph compatibility。作者在 RTX4090/5090/PRO6000、四款 MoE 与 50K 长度 0.1–10K 的 trace 中报告：45% residency 达到 96.97% hit rate 与全加载性能的 80.22%。

**证据边界：** 证据绑定 host-offload、PCIe 代际、所选模型和 trace；论文未证明 predictor drift、miss burst、不同 expert topology 与真实多租户下仍成立。数值不可外推，机制增量是“prediction、deadline、cache replacement 与 graph capture 必须共享 expert-state contract”。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)：重写 `### MoE Expert Staging 可以消费时序与跨层激活相关性` 的后半段，形成“静态 offload → 单步预取 → 序列预测 + deadline → graph-compatible placement”的演进，并把 routing ownership handoff 到 Ch56。

### [Pixel Decodability Is Not a Compression Signal（arXiv:2609.13012）](https://arxiv.org/html/2609.13012v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)

预注册实验在 Gemma-4-12B（encoder-free）与 InternVL3.5-8B（encoder-based）上，把“像素是否可从 KV 解码”与“该 KV 是否被任务因果使用”分开。作者训练 pixel inversion decoder，再用 single-superpatch causal KV ablation 测 teacher-forced gold-answer log-prob drop；48 个 calibration、72 个 heldout 样本上，decodable retention 与 causal utilization 没有正相关，attention 仅有约 0.11–0.12 的弱相关。

**证据边界：** 只有两模型、小图、teacher-forcing 和单单元消融；冗余表示可能掩盖因果用途，也没有构建端到端 eviction system。论文否定“可解码性可直接充当 eviction authority”，不证明任何替代指标最优。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：在 `### Eviction 不能只看 Attention Mass` 与 `### KV Eviction 应显式承认自己是有偏估计` 之间补“representation decodability 也只是 sensor；只有任务干预证据才接近 causal utility，且仍不能单独拥有 eviction authority”。

### [Subquadratic Disaggregation（arXiv:2609.13134）](https://arxiv.org/html/2609.13134v1)

**主题组：** Inference、Execution 与 Observability · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)

SQD 不再按传统 operator 名称或固定 P/D 阶段切分，而按 arithmetic intensity 与 footprint：quadratic attention 留在带 HBM 的 GPU，subquadratic attention 与 FFN 移向 SRAM-rich ASIC；当多数层为 subquadratic 时，跨设备边界也随模型结构变化。作者用修改版 SGLang、8×B200 proxy、32K/256K/1M 三种 workload 和三款 LLM 做 graph-captured 测量，再用 Rubin/LPX analytical model 投影 throughput。

**证据边界：** LPX 不是实机部署；性能使用 dummy weights，top-k locality 来自真实 trace；one-sided 通信与 64.6–130.7 μs 结果绑定 proxy 拓扑，功耗模型还排除了 HBM。支持的是“attention complexity 改变 disaggregation boundary”，不是投影吞吐的生产保证。

**Books 落点：** 已按审阅锚点落实到正文。`INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)：在 `## 从 P/D 到 P/D/A/F：分离是条件化切分，不是单向演进` 中加入“算子复杂度改变 arithmetic intensity/state footprint 后，A/F 边界也必须重新计算”，并保留 co-location 作为小规模/低跨域成本条件下的旧方案。

### [R2VC（arXiv:2609.11955）](https://arxiv.org/html/2609.11955v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)

R2VC 把 sparse+dense retrieval、SFT+DPO candidate generation、外部 NLI cross-encoder selection、sequence calibration 与 abstention 分成可观测阶段。FEVER、8B 配置报告 13.74% accuracy 增量；去掉 selection 后 accuracy 为 76.24%，去掉 calibration 后 Brier 几乎翻倍到 0.161；250 个错误的人工分析把 retrieval/wrong entity 定位为主因。

**证据边界：** 单一 FEVER/Wikipedia/8B workload，无法证明开放网页、高风险事实或多跳任务上同样成立；NLI 选择器和 calibrator 仍会继承分布偏差。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)：`## Relevance 不等于 Sufficient Context`、`### Evidence Access Right、Cost 与 Sufficiency 是联合检索状态`、`### Escalation 与 Abstention Threshold 必须联合校准` 已完整承载 retrieval/verification/calibration/abstention 分权，不新增正文。

### [Harness or Model?（arXiv:2609.11987）](https://arxiv.org/html/2609.11987v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

256 个任务（179 private repo、77 post-cutoff contest），每模型/每 harness 配对 80 个相同任务，计划 800 次、792 次成功评分。Opus 4.8 与 GPT-5.5 的 native-vs-neutral 平均优势均未被置信区间分辨；Opus 的 repo/contest 交互虽显著，但属于 post-hoc。另有 22/81 个 ceiling-cancelled run 在终止前已经通过，说明 correctness 与 completion 不能合并。

**证据边界：** 任务池私有且有限，white-box coupling label 未保存；task-stratum 结论 post-hoc，账单价格排序仍不确定。论文证明 harness identity 是 evaluation identity 的一部分，不证明某种 harness 普遍更好。

**Books 对读：** 现有正文已承载相同长期命题。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：`### Evaluation Identity 必须包含 Harness 与 Environment`、`#### Prefill 是 Harness 输入，不是模型自然历史` 与 `## Harness Optimization 的 Test Boundary 必须对优化器不可见` 已直接覆盖；只需 Weekly 保存此受限实证。

### [Can We Trust LLM Judges（arXiv:2609.12002）](https://arxiv.org/html/2609.12002v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

在 QuALITY、GSM8K、MBPP、AIME，六模型、36 个 judge–examinee pair 上，任务能力与 judging accuracy 高相关（r≥0.90），与方向性偏差负相关（r≤−0.83）；但对更强 examinee 又出现 leniency（r≥0.83）。作者用 judge disagreement 的 label-free weighted majority voting 估计 FPR/FNR，模拟 distribution shift 中与 oracle 的差异低于 0.5pp。

**证据边界：** 高相关不等于跨任务因果；label-free calibration 的有效性主要来自模拟，依赖 judge error 条件独立/可识别与 shift 假设。客观短任务不能代表开放式或安全判决。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：在 `#### Judge Ranking 要同时校准局部比较与全局区间` 后补“judge 的 capability 与 directional/leniency bias 必须分开”；在 `### Judge Agreement 不是单一数字` 中加入“无标签 disagreement 只能生成待验证 calibration state，不能替代锚点集”。

### [Competence-Gated Pooling（arXiv:2609.12101）](https://arxiv.org/html/2609.12101v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

论文把 competence 定义为模型相对市场/crowd/statistical prior 的边际价值，而不是自述 confidence；用 Brier-based domain weights、global shrinkage 与 recalibration 决定 pooling/defer。2,357 个已决 ForecastBench 二元问题上，Brier 从 0.0771 改善到 0.0732，verbal confidence 的 risk-coverage AUC 为 0.054，而 competence gate 为 0.019；官方 market subset 没有收益。

**证据边界：** 需要已决 outcome 才能学习 gate；未测 latency、token/provider cost，也未证明能迁移到新 domain、非 forecasting 任务或非平稳先验。可沉淀的是“confidence 不等于相对外部基线的边际价值”。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：在 calibration/risk-coverage 主线（`### 不确定性必须绑定覆盖假设` 与 `### Atomic Claim 置信度怎样合成整体结论` 之间）加入“defer gate 必须比较模型与外部 prior 的 incremental Brier，而非读取 verbal confidence”。

### [Certifying Concept Unlearning（arXiv:2609.12163）](https://arxiv.org/html/2609.12163v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)

方法沿 concept-relevant embedding direction 做 worst-case analysis，并以统计上界表达 residual leakage，而不是把有限 adversarial prompt 的未命中当作删除证明。在 SD-Turbo/SDXL-Turbo、NSFW/style/celebrity、六种 unlearning 方法、攻击预算 10²/10³/10⁴ 与五 seeds 下，certified bound 平均高于观察 ASR 16.2%，表明有限攻击会系统性低估残余风险。

**证据边界：** 证书只对指定模型、prompt distribution、embedding direction、concept classifier 与攻击预算成立；它不证明 parameter erasure、完整语义删除或整个 prompt universe 安全。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)：在 `### Unlearning 必须分开参数擦除与推理拒答` 后加入“observed ASR → attack-budget-aware statistical upper bound → parameter/artifact evidence”的验收层级，并与 `### Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family` 形成边界。

### [GAUGE（arXiv:2609.12191）](https://arxiv.org/html/2609.12191v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

GAUGE 把 user-simulated task-agent evaluation 拆成 ranking validity 与 construct validity。25 agents、6 providers、tau2-bench 与 SimulatorArena 上，150 条 transcript 由三位 blind human 标注，alpha=0.79，human ceiling rho=0.85；LLM judge 与满意度相关 rho=0.846/0.827，但 satisfaction 与 task success 相关为 −0.147，57.5% 的“满意”会话实际失败。close pair 的决策 disagreement 达 31%，wide-reward pair 低于 1%。

**证据边界：** 数字绑定两套 simulator benchmark、所选 judge/agents 与 close-pair sample；不能外推“满意度无用”。它证明 construct 与 ranking 必须分别验证，completion bit 只能是 tripwire。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：在 `### Judge 先证明看见了目标变化，再谈总体准确率` 后加入“rank fidelity 与 construct fidelity 是两条 gate”；在 `### Trajectory Judge 必须区分叙述、动作与完成证据` 中纳入 satisfied-but-failed 的受限案例。

### [ParaRecover（arXiv:2609.12345）](https://arxiv.org/html/2609.12345v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

ParaRecover 提供 10,626 个并行多轮 tool-use instance、14 类 error taxonomy，并以 structural/diagnostic/evolution rubric 评估十余模型如何定位错误、重规划与恢复，显示早期错误会跨并行支路传播，最终成功率无法解释 recovery quality。

**证据边界：** benchmark 与 rubric 均为合成环境；未覆盖真实副作用、不可逆工具、真实权限和生产恢复成本，也不能从相关表现推出 recovery 策略的因果最优性。

**Books 对读：** 现有正文已承载相同长期命题。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：Ch66 已在 process evaluation 主线中区分 isolated/cumulative error、first causal error、recovery 与 final success，尤其 `### 从 Final Answer 到 Artifact、Process 与 Environment Evolution`；不新增正文。

### [SynthSentry（arXiv:2609.12353）](https://arxiv.org/pdf/2609.12353v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** PDF · **Books：** 仅报告 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)

方法以 lexical diversity collapse、n-gram tail truncation 与 cross-model perplexity variance 三类特征，经 whitening、distributional divergence 与 bootstrap threshold 检测 synthetic corpus；包含 leave-one-generator-out 与跨 domain 检查。

**证据边界：** 样本极小（36 corpus instances；部分设置每类 12 文档、每 domain 30 文档、37 shards），无 confidence interval、未做 panel ablation、只覆盖英语模板 domain、无 adversarial/recursive generation，并要求 pre-generative reference corpus。下游 pruning 没有发现 contamination 导致的 accuracy 缺口，只暴露 over-pruning 风险。因此不能建立“部署该 detector 可改善训练质量”的长期结论。

**Books 对读：** 作为受限背景证据保留在日报，不扩写正文。`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)：若未来更强证据出现，应落在 `### Synthetic data：从“先生成再打分”到 Specification Compilation` 与 `## 数据质量不能只看 validation loss` 之间；本次没有足够证据修改正文。

### [VRL-Bench（arXiv:2609.12404）](https://arxiv.org/html/2609.12404v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)

VRL-Bench 把 verbal reinforcement learning 放进有限 trial budget，覆盖 MiniWoB/WebShop、三模型、六设置。多种 verbal memory update 在不同设置中可能提高也可能降低成功率，直接 replay 也会退化；VEX2 联合选择 policy 与剩余预算，是六设置中唯一全部正向的方法。

**证据边界：** 只有两类 harness、三模型与受限 budget；无法证明 VEX2 是一般最优 controller，也未覆盖生产工具副作用、长期 memory drift 或成本模型。可靠结论是 reflection/replay 不是单调收益，必须拥有 stopping/budget state。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)：`## Feedback 来源决定价值`、`## Stopping Policy`、`## Evaluation` 已承载“有限预算下 reflection 的 intervention value 与停止条件”；不新增正文。

### [SoK: Rethinking Jailbreaking in the Era of Agentic AI（arXiv:2609.12413）](https://arxiv.org/pdf/2609.12413v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** PDF · **Books：** 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)

SoK 把攻击入口、目标组件、持久性、交互结构与 trust boundary 分开，并明确区分 native harmful-prompt safety、adversarial jailbreak robustness 与 agent-level security。受控实验固定 LangGraph Agent，使用 Qwen3.5-4B 作为 router/tool model，Qwen3.5-4B 与 Llama-3.1-8B-Instruct 为最终模型；比较 Vanilla + 16 defenses，XSTest 250 benign/200 harmful、AdvBench 前 50 harmful × 9 attacks，以及 AgentHarm 的 TRACE/MINJA/AgenticRed。它同时测 ASR/DSR、over-refusal、utility、latency/token 与 planning/memory/tool intermediate compromise。关键结果不是某个最优防御，而是 final-response ASR 会掩盖内部状态失陷：例如 Self-Eval 在三种 Agent 攻击下 final ASR 为 0%，但 MINJA unsafe memory 仍达 95.65%，TRACE unsafe planning 为 93.62%；而某些 0% ASR 防御通过拒绝全部 benign prompt 获得，utility 为 0。

**证据边界：** taxonomy 覆盖跨层攻击，但 empirical depth 只比较代表性模型层 inference-time defense；两种最终模型、固定 Agent architecture、公开 benchmark 与模拟/隔离 tool effect 不能证明端到端生产安全，也不能把 defense ranking 跨模型外推。LLM judge、min–max normalization 和模型内 ranking 还限制了绝对比较。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)：在 `### Containment 不能只看最终是否发生攻击` 后，把安全 outcome 明确拆成“native refusal / adversarial robustness / intermediate state integrity / external effect”，并要求 security–utility–efficiency 联合结算；与 `### Security Agent 的评估必须绑定 Tool Trace 与 Deterministic Predicate`、`### Agent Integrity 需要四条链同时成立` 衔接，避免重复列攻击名。

### [Beyond the Query / Do Retrieval Signals Improve Routing?（arXiv:2609.12437）](https://arxiv.org/html/2609.12437v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)

论文在同一 optional action、router family、训练和评测协议下，对照 query-only 与 query+retrieval-state router。文档、音频和视频任务共形成 3,574 queries / 10,722 states，最终 held-out 为 720 queries；retrieval feature 在开发集上的小幅收益没有在 held-out 上形成可靠增量。它还区分“能预测后续 step 是否有益”与“能改善最终 RUN/SKIP 决策”，并报告 whole-page 修复、DOC_CLIP 使用率和额外延迟等诊断。

**证据边界：** 单一 Qwen2.5-Omni-7B generator、有限 router/action 和三类数据不证明 retrieval state 普遍无用；held-out 区间包含零，Audio/Video 的真实 warm-serving 增量时间没有有效记录，source-level split 隔离也未完全证明，预期 positive control 未完成。

**Books 落点：** 已按审阅锚点落实到正文。`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)：第76章「Retrieval Router 选择的是检索系统，而不只是文档」。在现有 query-only router 论证后加入 attribution gate：retrieval-state signal 只有在 matched query-only control 上产生增量，才能被归因于 routing value；相关性或 future-step predictability 不能替代最终 action 改善。

### [GraphProfiler（arXiv:2609.12448）](https://arxiv.org/html/2609.12448v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)

作者把用户 post history 建为 source-linked personal KG，使实体、关系、预测和引用都能回到具体 post；在 SynthPAI 八属性与 PANDORA 上报告 86.7% / 84.6% attack success，超过 98% 的预测带引用。删除 cited posts 比删除等量随机 posts 更显著降低 attack success，支持“被引用来源确实参与推断”的有限归因。

**证据边界：** 这是隐私攻击审计而非完整缓解；冗余 cue 使定点删除不保证消除泄漏，local graph search 不穷举全部证据，graph extraction faithfulness 未大规模人工标注，也缺 matched chunk-RAG control。SynthPAI 是合成历史，PANDORA label 是 proxy，流水线主要依赖 GPT-4o；高预测覆盖不等于高泄漏召回。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)：第72章「Privacy Boundary 必须覆盖全部 Observable Channels」之前。补入 source-linked inference audit：attribute verdict 必须能回到 post/edge/source identity，定点删除后需重建索引并重测；citation 只是 selected support，不是 exhaustive leakage proof。

### [ZipBench（arXiv:2609.12475）](https://arxiv.org/html/2609.12475v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

ZipBench 用六个真实 anchor LLM 的完整结果生成 pseudo evaluation logs、学习 item fingerprint 并选 compact subset；作者为压缩误差和 rank consistency 给出理论条件，并在 100+ text/multimodal/agent benchmark proxy 上报告 MAE 0.002–0.02、平均 Spearman 0.98。机制意义在于：压缩 benchmark 也应发布 score fidelity 与 ranking fidelity，而不是只声明节省样本。

**证据边界：** compact subset 必然丢失 full benchmark signal；理论保证依赖 anchor 与合成日志假设，仍需六个 anchor 跑完整 benchmark，agent benchmark 的 residual cost 仍高。作者结果不证明未来模型族、极端 slice 或新能力保持同样误差，也不允许 pseudo logs 替代真实 held-out 验证。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：第66章 benchmark artifact / adaptive evaluation 主线。在 benchmark 作为版本化 reference artifact 后加入“压缩是带误差预算的 proxy release”：冻结 anchor、subset builder、score/rank guarantee、held-out model fidelity 与失效条件；无法给出 fidelity 时回退完整 benchmark。

### [ProactiveBench（arXiv:2609.12658）](https://arxiv.org/html/2609.12658v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

benchmark 以 standing request 驱动每秒 streaming evaluation，不提供显式回答 cue；六个子任务同时测 response、silence、early/in-window/missed 与重复计数。六个系统中有四个 premature response 多于 missed response，说明只测“最终答对”会漏掉时序行动边界。

**证据边界：** 结论只属于给定录制数据、六套系统、最多 30 秒上下文和各自 silence interface；几何聚合会改变排名，部分子任务不共享完全相同 recording，不能推断生产连续视频或真实用户容忍窗口。

**Books 对读：** 现有正文已承载相同长期命题。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：第66章「Proactive Agent 必须同时测 Act、Silent 与 Stop」。现有正文已区分正确行动、正确沉默、拒绝后的停止、deterministic effect check 与 soft preference judge，并保留 simulator/profile/history identity 与 synthetic-persona 边界。

### [A Historical Corpus Is Not a Historical System（arXiv:2609.12766）](https://arxiv.org/html/2609.12766v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

Point-in-Time Discovery 把 anchor、corpus、retriever、budget 固定，只改变 memory-time eligibility；系统状态同时包含 corpus、model/derived state 和 request-time memory，并以 event、observation、materialization 三类时钟检查可用性。三个 DPDisc domain 的 Future memory 使 Asset Recall@100 全部提高 2.62–5.24 points，FreshStack 方向一致；实验还显示 hindsight 可掩盖 harmful trace memory，并夸大 positive-feedback memory。

**证据边界：** 只测三类 table-text discovery、两种 retriever、两类透明 memory 与五个 FreshStack topic；Asset Recall 不是 answer quality、用户成功或生产收益。固定日志排除了 branch-dependent feedback，black-box state 没有 timestamp/dependency lineage 时只能部分审计。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：第66章「Longitudinal State：事实必须先于对话，读写路径必须分开审计」。在 canonical fact ledger 后补充：historical corpus 只是系统状态的一部分；derived state 必须继承最晚 ancestor event time，PIT/Future branches 要冻结 retriever、budget 与 anchor，并将 model/index/profile/request memory 的 lineage 一并纳入历史有效性。

### [K-Bench（arXiv:2609.12808）](https://arxiv.org/html/2609.12808v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)

K-Bench 把同一 synthetic PII 单独注入 parameter、retrieval、prompt/context 等 substrate，并让 observer 检查 deployed agent 的六类 observable channel；collapse-aware score 同时看泄漏和 agent utility。13-method panel 与 20-method leaderboard 显示，单看 final answer 或 parametric channel 会高估 unlearning，泄漏可迁移到未监控 channel；某些 weight recipe 的“遗忘”实为 ReAct policy collapse。

**证据边界：** 主要语料是 Faker synthetic PII，real-format validation 只覆盖 date-of-birth；parametric injection 主要经 LoRA，不代表 pretraining memorization。实验以 pure single-substrate cell 做归因，不覆盖跨 substrate 组合泄漏；observer 是 binary channel detector，无法拼接多 channel partial fragments，模型轴也不是完整 factorial grid。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)：第72章「Privacy Boundary 必须覆盖全部 Observable Channels」。把现有 channel inventory 扩展为 unlearning contract：明确 secret substrate、六类观测面、组合 attacker、agent-collapse guard 与 retain utility；final refusal 或单 channel clear 只能形成 suppression/局部编辑 verdict，不能形成 deletion verdict。

### [MedSNIP（arXiv:2609.12884）](https://arxiv.org/html/2609.12884v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

MedSNIP-Bench 将 276 个医疗回答标为 2,524 个 snippets，并同时保留 in-general / in-patient-context label 与六类结构 pattern；pipeline 按 enumeration、causal/conditional chain、premise–conclusion 等依赖合并 atoms。实验和 rewrite ablation 表明，过度原子化会切断局部前提，snippet 收益不能完全由措辞更清晰解释。

**证据边界：** 只覆盖英语医疗 fact-checking；decomposition 主要用 GPT-5.4，绝对结果依赖 verifier、aggregation、retrieval 和 prompt。弱 verifier 的 full-context 设置可缩小甚至反转 snippet 优势；当 claims 本来独立时，atom 仍可能是更好的单位。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：第66章「Atomic Claim 置信度怎样合成整体结论」之前。补入 verification-unit gate：atomization 必须保留 causal、conditional、enumeration 和 premise–conclusion edge；验证单位由依赖结构决定，不能为了可计数而切断判定所需 context。

### [Judging by the Cover / Audit-Prune（arXiv:2609.13003）](https://arxiv.org/html/2609.13003v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

作者用只读 answer string 的六个 surface features（negation、hedging、length 等）审计 TruthfulQA binary pairs，并扩展到另外 13 个 benchmark。Audit-Prune 迭代删除最强化 leakage 的 pair，再 add-back，在预声明 residual-leakage threshold 下发布 TruthfulQA-476；同时检查 14 个 open-weight models 上的 ranking fidelity，并用 surface-inversion adversarial set 证明原 benchmark 的 shortcut 可被利用。

**证据边界：** Surface6 只覆盖已知、可解释的局部 shortcut，不证明剩余 subset 无其他 lexical/semantic leakage；pruning 会改变 task distribution，模型 ranking 保持也不是 construct validity。单一 TruthfulQA 清洗结果不能成为通用阈值，classifier family、pairing、CV 与 add-back procedure 都应进入 artifact identity。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：第66章 benchmark contamination / clean-twin 与 release artifact 论证附近。加入 question-blind/partial-input surface probe、label inversion counterfactual、预声明 leakage threshold、prune/add-back lineage 和 held-out ranking/semantic fidelity；清洗通过只关闭所测 shortcut。

### [Tasks over Application Manuals (TAM)（arXiv:2609.13005）](https://arxiv.org/html/2609.13005v1)

**主题组：** Evaluation、Evidence 与 Security · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

TAM 将 ICD-10-CM coding（1,000 cases / 2,555 codes）和美国联邦量刑（200 human-verified cases）表成跨数百页、数万规则与交叉引用的 exact procedural task，并比较 single-pass RAG、agentic RAG、ReAct manual tools 和 staged harness。GPT-5 系统的最佳 exact match 仍约为 ICD 1%、sentencing 15.5%；50 条已保存的非 exact ReAct trajectory 中，最早可见偏差主要是 global inconsistency，其次为 incomplete/missing-required-state。

**证据边界：** 两个 rule-heavy domain 不代表所有长期推理；baseline 是通用 prompt/harness，而非 exhaustive specialized system。35/200 legal harness runs 因 provider filtering 提前终止；retrieval、judge 和 exact-match 约定会影响结果，医疗/法律结论不应外推为实务正确性。

**Books 落点：** 已按审阅锚点落实到正文。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：第66章从 component score 进入 long-horizon artifact / deterministic verifier 的主线。补入 procedure-complete contract：冻结 manual revision、required-state inventory、跨节 dependency、intermediate decision trace 与 exact terminal outcome；partial credit 不能掩盖单个前置规则错误，短链 benchmark 不能外推完整 procedure reliability。

### [MemRetriever（arXiv:2609.11951）](https://arxiv.org/html/2609.11951v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)

MemRetriever 将 memory read 从一次 top-k 改成多步 policy：state 包含问题、evidence pool 与 search history，action 为 parallel search、serial search、reflection/denoise 和 stop；Qwen3-4B-thinking 经 SFT + GRPO 学习，stage reward 分别覆盖 gold evidence 增量、query cost、去噪保留和 downstream answer sufficiency。实验覆盖 LoCoMo、LongMemEval 与三项 multi-hop QA。

**证据边界：** 训练 reward 使用 gold evidence 与特定 downstream reader，不能证明 online retrieval utility 的因果归因；“storage agnostic”没有在生产异构 store、权限、多租户和 latency SLO 下验证。论文缺少独立的完整 limitations 讨论，模型、检索 pipeline 与 judge 相关性必须保留。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)：第77章「从一次 Top-k 检索到有预算的关联回忆」与「Fact State 与 Retrieval-policy State 必须分离」。现有正文已包含 anchor recall、bounded expansion、stop controller、provenance/ACL、candidate ceiling、selector drift 和 flat/full-context fallback。

### [Look Before You Leap（arXiv:2609.11957）](https://arxiv.org/html/2609.11957v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)

论文用 construction-defined ground truth 测 shell command 与 code edit 的 pre-action verifier，并将 outcome 分为 success、clean failure、silent failure 与 abstention operating point。9,930 commands / 482 tools 的 static verifier 在 10% false-positive operating point 捕获 95.8% invalid commands；640 edits 中 one-line shift 使 line anchors 99.1% corruption，而 content anchors 倾向 clean fail；Robust-Apply 在 8,320 perturbations 中仅 1 次 silent misapply。

**证据边界：** 只覆盖所选 shell help、tool family、语言、编辑形式和 synthetic perturbation；不证明 semantic correctness、authorization 或并发文件 side effect。v1 仅承诺后续发布 code/data，本次没有 immutable artifact verification。

**Books 落点：** 已按审阅锚点落实到正文。`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)：第78章「安全执行需要 Preventive Gate 与 Evidential Gate」，其中已存在 `SF-2026-ARXIV-2609-11957`：effect 前重新匹配唯一 content anchor、检查 expected old content，并在零/多匹配或 revision 变化时拒绝，把 silent corruption 转成可恢复失败。

### [Local Edits, Global Ripples / RIPPLE（arXiv:2609.12127）](https://arxiv.org/html/2609.12127v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)

RIPPLE 将 persistent prompt-policy edit 拆成 what failed、where to edit、whether to persist；确定性 failure taxonomy 将轨迹定位到七个 prompt segments，candidate 先全部相对同一 iteration-start policy 比较 isolated gain，再按顺序叠加已接纳 edits 做 replay gate。Flow-HO 的 39 个 held-out modification tasks、三种 frozen backbone 和 interaction case 显示 local edit 会改变下游 tool/resource/validation，孤立有益 patch 在组合后可转为有害。

**证据边界：** 任务是合成 closed-schema JSON workflow，patch 来自预定义 library，主要 Haiku 结果只证明 service-validation gain，workflow correctness 增量未解决；greedy sequential promotion 不是全局最优，允许的小 regression 还可能累积。不能外推开放 prompt rewriting 或线上自动发布。

**Books 落点：** 已按审阅锚点落实到正文。`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)：第81章 harness / artifact sequential refinement 与 held-out admission 段落。加入 composition-aware promotion：所有 patch 先用共同 baseline 估 isolated effect，再按真实持久化顺序重放交互；locality 只约束 edit locus，不证明 downstream effect local，任一组合回归触发 reject/rollback。

### [GuardrailLoop（arXiv:2609.12216）](https://arxiv.org/html/2609.12216v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)

测试台以 hash-pinned policy 固定 goal、scope、evaluation、budget 和 release，机器只能从 code-owned catalog 选择 bounded knobs；event log 是 source of truth，并在每个 execution prefix 计 simulated compute。50-seed utility ablation 中 round growth 达标 50/50、no-growth 0/50；240 个 crash cells 的 scientific projection 全部恢复，但 normalized trace 仅 210/240，一组 pre-commit planner call 被重复，直接反驳“结果恢复即 exactly-once”。

**证据边界：** 一个 shirt-folding simulator、一个 simulated VLA、offline deterministic planner 与 simulated GPU-hours 不能证明真实效用、安全或成本。无 sealed holdout，hash chain 未签名、approval 未认证、protected-key list 重复；selected crash sites 不覆盖网络、kernel、并发和远端不可逆 effect。

**Books 落点：** 已按审阅锚点落实到正文。`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)：第84章「长任务恢复依赖 Event Log，而不是 Transcript」。补入双观察量：恢复后的 authoritative scientific state 与 normalized execution trace 必须分别验收；prefix budget、policy hash 和 effect receipt 同属 run contract，local atomic commit 不等于外部 exactly-once。

### [Sampling via Decision-Flow（arXiv:2609.12317）](https://arxiv.org/html/2609.12317v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 仅报告 — `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md)

DF-Sample 构造 hierarchical reasoning tree，以 terminal-node energy 作为 trajectory proxy，再将 utility 向中间 branch 回传，与 generation prior 组合后选择路径；在三类模型和 MATH500、HumanEval、GPQA-Diamond、AlpacaEval 2.0 上优于作者对照。它说明 token-local probability 与完整 trajectory utility 可能不同。

**证据边界：** terminal node 是完整 reasoning quality 的 proxy，不是独立 truth verifier；作者 comparison 受 tree/block size、energy model、benchmark、模型和 test-time compute 约束，且 limitations 仅讨论未来 distillation，没有充分量化搜索成本、judge dependence 或 contamination。单篇结果不能证明 RL 只是在重分配既有路径，也不能证明该 tree policy 优于所有 verifier/search。

**Books 对读：** 作为受限背景证据保留在日报，不扩写正文。`MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md)：第20章「Parallel Sampling：先分开 Coverage 与 Selection」及“多数票选择稳定盆地，不是真值”。现有正文已要求区分 trajectory probability、path coverage、selector 与外部 verifier；DF-Sample 是受限的 global-trajectory selector 实例，不足以增加长期主干。

### [AIM / Agentic Interoperable Memory（arXiv:2609.12320）](https://arxiv.org/html/2609.12320v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)

AIM 为 multi-user/multi-agent memory 定义 create/read/update/delete/no-op、多标签 intent、private/public visibility 与 index-level filter，并用 MUMBench 评估 evolving state 下的 operation 和 visibility。三次运行中 visibility classification 为 96.0%，strict/state-aware operation 为 58.8%/70.5%，表明权限分类好并不等于 lifecycle operation 已可靠。

**证据边界：** retrieval relevance 最高 45.0%、tag overlap 35.5%；LOCOMO 只跑一次且不能测试 multi-user privacy。任意用户仍可写错 public memory，conflict resolution 和 user audit 是未来工作；分类器、索引过滤和 synthetic benchmark 不证明并发安全或端到端无泄漏。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)：第77章「Shared Memory 必须选择性写入」「Recall 与 Commitment 必须分开授权」以及章节小结。现有正文已将 RBAC/ABAC、tenant isolation、competing claims、CRUD/supersession、before-image、conflict visibility 与可恢复 transaction 作为 memory owner contract。

### [CueMem（arXiv:2609.12354）](https://arxiv.org/html/2609.12354v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)

CueMem 将 extracted triple 作为带 source-turn pointer 的 retrieval cue，而不是 self-contained evidence；query 时由 cue 找 anchor，再沿 temporal/semantic turn graph 做 one-hop context reconstruction。LoCoMo / LongMemEval-S 同用 Llama-3.3-70B、MiniLM embedding 与 LLM judge；graph-removal ablation 在 LoCoMo 将 81.1% 降至 71.4%，并报告约 2K context 相对 full history 的 token/latency结果。

**证据边界：** 只测两项 text conversational QA，source turns、graph edges 和 update precedence 都由特定 extractor/prompt 决定；answer generator 与 judge 同源，full-history latency 未绑定生产并发。UPDATE 仅靠“优先较新证据”prompt，不提供冲突 transaction 或并发 write guarantee。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)：第77章「从一次 Top-k 检索到有预算的关联回忆」。现有正文已写 `anchor recall → bounded expansion → evidence assembly`，明确 memory unit 绑定 source episode、valid time、supersession，edge 不是事实 owner，并保留 flat top-k/full-context fallback。

### [Robust Personalized Alignment / CORE（arXiv:2609.12373）](https://arxiv.org/html/2609.12373v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)

CORE 将 turn-local evidence distribution 与 persistent slot belief 分离，以 relevance、ambiguity、conflict 和 prior confidence 路由 `Commit / Defer / Ignore`，只有 Commit 才做 gated belief revision；SFT 后再用 PPO 优化 state/action/response/clarification。ALOE、PersonaChat 与 PERSIST stress test 分开测 response、closed-slot state 与 update action，结果支持 access to memory 不等于正确 revision control。

**证据边界：** benchmark-instantiated slots 与 structured supervision 不覆盖 open-ended/cross-slot preference；closed-slot normalization 只代表可规范化子集。PERSIST 主要是 post-anchor stress，不测真实用户何时改变长期偏好，且未覆盖 retrieval corruption、third-party update 与 external-tool memory failure；保守 route 也可能延迟真实更新。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)：第77章「Recall 与 Commitment 必须分开授权」、`persist / current-session only / reverify / clarify` commit state，以及 preference scope / correction 路线。现有正文已要求局部 observation 先作为 evidence，policy owner 再提交持久 state；冲突或不确定默认不升级。

### [LifeMem（arXiv:2609.12655）](https://arxiv.org/html/2609.12655v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)

LifeMem 从 cross-environment trajectories 初始化、聚类和演进经验 memory，再在 database、web search、data analysis 与 browser 环境中检索 reusable workflow skill；实验包含 seen/OOD、backward-transfer 与 component ablation，强调经验 consolidation 而非无限追加 raw trace。

**证据边界：** benchmark environment 与人工/模型生成轨迹不代表生产工具、副作用和权限；百万级 experience 的检索、并发、删除、污染与端到端 SLO 未测试，论文 limitations 主要把它们留给未来工程优化。跨环境分数不能证明抽出的 skill 是因果必要步骤或不会携带 shortcut。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)：第77章「从原始轨迹到派生策略：Memory 的演进不是无限追加」与「Hierarchical Skill 不是固定 Taxonomy，而是 Retrieval Plan」。正文已保留 raw trajectory、success/failure、distilled procedural lesson、re-evaluation/consolidation、provenance、applicability 和 workflow 重新 admission。

### [Skill Issue（arXiv:2609.12742）](https://arxiv.org/html/2609.12742v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)

作者从 Kotlin repositories 的 merged PR mining、reverse application 与 hidden FAIL_TO_PASS validation 建 task pool，再以相同 model/tools/container 将 candidate SKILL 与 empty-seed run 配对；GEPA/SkillOpt 只改变 `SKILL.md`。mining 需至少 100 graded tasks 才能分三 split，但 test split 仍只有 20–26 tasks；所测几百分点 gain 落在 frozen agent 自身 run-to-run variance 内，maintainer qualitative reading 与 pass-rate attribution 被明确分开。

**证据边界：** 三个 Kotlin/JVM repository、Sonnet 4.6、有限 held-out tasks 和单 maintainer 不能证明 skill optimizer 通用有效；LLM revert 会制造 validation 看不见的 defect，task synthesis 可能泄漏 solution。一次 stored seed 与少量 attempts 不能形成稳定部署概率，成本结论也绑定作者 run。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)：第84章「从 Trajectory 到 Skill 是一次受治理的 Compilation」与 fresh-executor 段落。现有正文已明确 held-out selection 会过拟合有限任务、fresh execution 是 stochastic sample、task bootstrap 不含 run-to-run search variance，并要求增加重复 trials 或拒绝 promotion。

### [What Drives Recovery in Agentic Text-to-Cypher? / LAST-CQ（arXiv:2609.12746）](https://arxiv.org/html/2609.12746v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)

LAST-CQ 把 Text-to-Cypher refinement instrument 为 detection、correction、schema grounding、retry/sampling 等可替换环节，并以 no-refinement counterfactual、naive retry 和 paired subset 分解 recovery。结果支持主要收益来自识别失败并获得另一次有效尝试，而不是丰富 feedback 本身；schema grounding 在 214-query paired subset 上只建立有限 equivalence，best-of-3 还混合了 temperature 与 first-non-empty selection。

**证据边界：** 只覆盖一个 Neo4j benchmark、16 domains 与一个 engine；1,917-query comparison 条件于 LAST-CQ 自己选择修复的失败，不能作为 end-to-end 优势。部分模型被替换，no-refinement 是重打分 counterfactual，human calibration 单 annotator，judge 只看 LAST-CQ+DB，empty-reference convention 还可能奖励错误非空结果。

**Books 落点：** 已按审阅锚点落实到正文。`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)：第80章「Reflection 与 Retry 的区别」及「Critic Accuracy 不等于 Intervention Value」。补入机制分解：检测到失败、路由 retry、提供 feedback、重 grounding 与 candidate selection 是不同 treatment；只有 paired ablation 能把 recovery 归因于 reflection，简单 retry 已解释的增益不得记给 rich critique。

### [The Mechanics of a Swarm（arXiv:2609.12748）](https://arxiv.org/html/2609.12748v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)

论文从第三方 wiki archive 重建约 900 agent episodes，区分 wiki name、episode、thread/container proxy、page revision、arrival/activity clock 与可见 shared-board exposure；它能证明大量外部写入和 rendezvous substrate，却没有 read log、termination、harness feedback 或真实 task correctness。作者撤销早期过强因果解释：共享词汇和时间聚集既可能来自 wiki 传播，也可能来自共同 scaffold/启动 wave；documented progress 与 board exposure 没有 robust positive association。

**证据边界：** 无 successful read event，因而 exposure 不等于 consumption；自由复用的 names 不能还原 container identity，510/907 episodes 才有被删失的 ordinal outcome。classifier 由两模型标注、单作者 adjudication，部分 recall 很低；clock 样本小，基础设施负载未测，删除页面和未归档 write 使全部 count 都是下界。

**Books 落点：** 已按审阅锚点落实到正文。`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)：第84章「长任务恢复依赖 Event Log，而不是 Transcript」与 run identity 主线。加入 multi-agent external-effect event schema：principal/run/thread/episode/action/third-party revision、read exposure、write receipt、termination、feedback 与 outcome 必须分字段和时钟；共享 substrate 上出现协调模式不是 utility 或因果传播证据。

### [Online Video Agent Harness / VideoXAgent（arXiv:2609.12818）](https://arxiv.org/html/2609.12818v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)

VideoXAgent 不预建 query-agnostic video index，而是先从 expert reasoning trace 提炼 22 类 atomic capabilities，再映射到 40 个 tools / 12 backend families；ReAct orchestrator 根据 query、modality 和 media scope 在线 coarse-to-fine 取证，保留 observation/tool/timestamp/region 关系。VLM tools 返回 visual evidence、answer、uncertainty，冲突触发定点复查；硬 step limit、progressive warnings 与 forced answer 约束 non-termination。五项 long-video benchmark 和 ablation 支持该受限 harness 分支。

**证据边界：** 这是静态长视频理解而非真实环境 action；tool taxonomy、Claude Opus 4.6 orchestrator、Gemini/Qwen VLM backends、外部 OCR/ASR/detector 与 benchmark sampling 共同决定结果。input-context 数字不是统一硬件/SLO 下的端到端成本，forced answer 只保证终止、不保证证据充分；能力挖掘和工具映射也可能遗漏长尾能力。

**Books 对读：** 现有正文已承载相同长期命题。`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)：第84章 Harness Controller、observation interface、tool routing/budget/credit 主线；同时由第76章 Evidence Graph 承接 evidence identity。现有正文已要求 model intent、tool payload、environment result、observation locator、budget、verification 和 outcome receipt 绑定同一 run identity，并保留静态 workflow/fixed retrieval fallback。

### [MoPA: Coordinated Mobile Manipulation via Subsystem-Specific Perception Alignment（arXiv:2609.12081）](https://arxiv.org/html/2609.12081v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

§III-C 用 Mobile Query 与 Manipulation Query 分别读取共享 VLM token，query bank 之间互相 mask，避免在感知阶段提前混合；§III-D 只允许对应 action branch 读取匹配 query，同时在每层 action decoder 中交换动作状态；§III-E 用共享 flow time 的 coupled conditional flow matching 联合生成 base/manipulation action chunks。它把“分开看”与“联合行动”置于不同阶段，而不是把两个子系统完全独立训练。

**关键验证：** ManiSkill-HAB 三组任务与四个真实任务；真实任务每项 200 demonstrations、20 trials，统一训练/比较 DP、AC-DiT、pi0.5。论文报告四任务平均 full-task success 76.3%，比最佳基线高 12.5 个百分点；Shared Query、移除 joint attention、移除 corresponding-query access 都下降。该消融支持“读取边界 + 动作耦合”共同有用，但不能完全分离 backbone、数据与训练预算的所有影响；部分任务与强基线持平，收益不是普遍常数。

**证据边界：** 证明在披露的移动操作任务中，感知分流、对应读取和动作层耦合比共享 query 或弱耦合更有效；不证明 query bank 学到了物理可解释的 subsystem state，不证明跨 embodiment、控制频率或安全关键任务仍成立。

**Trade-off / failure：** 分流降低感知干扰，却增加 query/branch 参数、配对 schema 与训练耦合；错误 subsystem assignment 会把必要信息屏蔽，过强动作耦合又可能重新引入干扰。任务只需单一执行器或共享视觉足够时，统一 policy 更简单。

**Books 落点：** **Integrate** 到 `MULTIMODAL-EMBODIED-VLA`，锚点为 `26-multimodal-embodied-vla.md` 的 learned action-query mediator（约 110–113 行）之后、Online RL action interface 之前。正文应写成“感知状态可按执行子系统隔离读取，动作层再按同步约束耦合；perception isolation 不等于 control independence”，并保留错配与额外接口成本。

### [DIA: Denoising Intermediate Advantage for Diffusion Policy Optimization（arXiv:2609.12245）](https://arxiv.org/html/2609.12245v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

§IV-A 把 denoising chain 展平为 primary MDP；§IV-B 推导该 flattened MDP 上的 exact policy gradient；§IV-C 指出同一最终 return 下，部分去噪 action 的条件分布不同，因此 intermediate value 随 step 变化；§IV-D 用 ensemble Q 估计 environment action value，训练 inner value；§IV-E 在 scale matching 后混合 inner advantage 与 outer GAE。价值不是给每个去噪 step 复制同一个 terminal advantage，而是估计“当前 partial action 对最终可执行 action 的边际贡献”。

**关键验证：** Robomimic、FurnitureBench、Franka Kitchen 与 D3IL；短任务收益较小，长 horizon 更明显。论文报告 Transport return 提升约 23% 但 success 接近，One-Leg return / success 约 +12% / +3%，Lamp-Med 约 +20% / +12%，并报告完成时间下降；Appendix B 对 flattened GAE、Q target 与 scale matching 做设计消融，Appendix D 单列 wall-clock overhead。结果支持长链 credit 的局部价值，但 return 与 success 不总同步。

**证据边界：** 证明 intermediate advantage 在受测 diffusion-control 任务中比只看环境边界的 credit 更有信息，并通过设计消融排除若干简单替代；不证明 inner critic 无偏、不证明真实机器人或任意 denoising scheduler 获益，也不证明 return 增益自动等于安全或 task success。

**Trade-off / failure：** 更细 credit 换来额外 Q ensemble、inner value、advantage scale matching 与训练墙钟；Q bias、尺度错配或 denoising Markov 假设偏差会沿多个内部 step 放大。短 horizon 或 outcome signal 足够密时，环境步 credit 仍更稳、更便宜。

**Books 落点：** **Integrate** 到 `TRAIN-GRPO`，锚点为 `33-grpo.md` 的“Sequence Reward 怎样作用到 Tokens”（约 167–181 行）之后。应新增“生成器内部状态也可能是 typed credit boundary”，明确 denoising-step credit 是 diffusion policy 分支，不把它写成 token GRPO 的通用替代。

### [DWMP: Leveraging Dual World Models for Humanoid Obstacle Traversal（arXiv:2609.12347）](https://arxiv.org/html/2609.12347v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)

§III-B 的 Auto-Koopman 将低维但非线性的 proprioception 提升到近似线性演化 latent；§III-C 的 RSSM Depth Dreamer 用 deterministic recurrent state + stochastic state 压缩高维、噪声深度观测，训练包含 reconstruction、reward prediction 与 KL；§III-D 将两者 latent 融合给 actor。训练先由 privileged teacher 收集数据并预训练表示，再在非 privileged student policy 中联合适配。

**关键验证：** 论文分别检查两阶段训练、视觉表征、障碍穿越、模型 inference/reconstruction，以及 Unitree G1 真实障碍布局。RSSM 类视觉 world model 相对纯 VAE 更强，dual representation 相对 direct teacher-student baseline 在复杂地形与真实 pass rate 更好。组件比较支持“异质模态应按预测结构分治”，但整体 actor、teacher data 与 jointly trainable encoders 仍耦合，不能把全部终局收益归因给某一个 world model。

**证据边界：** 证明在该 humanoid traversal 合同中，近似线性 proprioceptive dynamics 与 stochastic visual dynamics 的组合具有可行性；不证明 Koopman latent 真正全局线性、不证明 RSSM state 是因果或 control-sufficient、不证明真实部署安全与跨 terrain 泛化。

**Trade-off / failure：** 状态分治降低单一 encoder 的冲突，却增加双模型训练、融合校准和 teacher/student gap；任一 latent stale、融合尺度错配或 privileged-data 偏差都可能让 actor 形成错误 belief。模态弱耦合或数据不足时，共享 encoder / observation-only policy 仍合理。

**Books 落点：** **Integrate** 到 `MULTIMODAL-WORLD-MODELS`。锚点为 `25-multimodal-world-models.md` 的“Multimodal latent dynamics”中 operator-structured / stochastic latent 分支（当前约 204–230 行）之后，并与“World Model 也可以只在训练期承担表示约束”（约 663–669 行）互相 handoff。正文只沉淀“按模态动力学特性分配 state model，并在 fusion 前保留各自 uncertainty/identity”，真实 pass rate 作为受限证据。

### [BlueLM-GUI Technical Report: A Real-Device-Centric Flywheel for Self-Improving Mobile GUI Agents（arXiv:2609.12394）](https://arxiv.org/html/2609.12394v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)

§2.3 在真实、已登录、联网移动设备上采集完整 trajectory；§2.4 用 heterogeneous triple-system consensus 做轨迹判定与路由；§2.5 先定位失败层级，再做 step correction、保留有效 prefix 的 query adjustment 与 counterfactual derivation，生命周期逐步淘汰已掌握任务；§3.3 的真实设备环境实现 reset/step/close，GRPO 结合 trajectory 与 step reward，并把所有结果回流数据池。Safety audit 拦截隐私、资金和禁用任务。

**关键验证：** CPT/SFT、trajectory-heavy 数据、judge 设计和 online/offline RL 均有消融；从同一 SFT 起点，固定离线轨迹 RL 未带来增益，而真实设备在线环境提高到论文报告的 82.0；atomic judge 与重复评估也提升结果稳定性。MobileGUI-VBench 用任务、复杂度、交互/风险等配额约束 query 分布。该结果把 policy-induced state coverage 与固定离线 replay 区分开，但 benchmark、judge 与设备集由作者控制。

**证据边界：** 证明完整 real-device transition、失败驱动数据再生与在线 rollout 在该移动 GUI 栈中共同可行，并给出“offline replay 不足”的受控迹象；不证明每个组件的独立因果贡献、不证明商业设备集外泛化、不证明其 LLM judges 或安全筛查达到生产保证。

**Trade-off / failure：** 真实环境提高 state coverage，却带来设备集群、账户状态、网络漂移、重放困难、隐私/副作用与 judge 成本；失败驱动 curriculum 会追逐诊断器 blind spot。静态、可重放、低副作用任务仍适合离线数据。

**Books 落点：** **Integrate** 到 `TRAIN-DATA`，锚点为 `27-data.md` 的 executable trajectory / failure-driven curriculum（约 405–424 行）之后、GUI 跨步状态对象（约 426 行）之前。已有原则不应重复；新增的是“真实设备 transition 是训练数据的一部分，offline/online 对照可检验固定轨迹是否覆盖当前 policy 状态分布”。

### [UFO: Chain-of-Evaluation for Omni-Condition Alignment in Multi-Modal Image Generation（arXiv:2609.12397）](https://arxiv.org/html/2609.12397v1)

**主题组：** Platform、Evidence 与 Governance · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

§3.2.1 把 prompt/参考条件拆为 AEUs；§3.2.2 为每个 AEU 判定 image-only、text-only 或 joint；§3.2.3 按类型调用 VQA 或专用函数（如 identity）；§3.2.4 由 VLM 给出 1–5 relevance weight 后汇总。这不是让一个 judge 直接给全局分，而是先决定“谁能证明哪条条件”。

**关键验证：** 660 个 case、四类 personalization/editing paradigm、三档难度，比较六个系统；人工评估抽 100 cases / 600 images 做 1–6 排名。论文报告 UFO 与人评 Spearman 0.6889，高于 CLIP-I/CLIP-T/DINO 与其他 MLLM metrics；去掉 AEU decomposition 或 adaptive weight 均下降。相关性和消融支持分解/路由价值，但人评样本有限，且 decomposition、weight 与部分 scoring 均依赖模型判断。

**证据边界：** 证明在该个性化图像生成集合中，typed atom + modality-specific verifier + explicit aggregation 比单指标更贴近人评；不证明 atom 完备、权重可跨 domain 校准、不证明同一/相关 VLM judge 没有共享偏差，也不证明图像设置可直接外推文本或视频。

**Trade-off / failure：** 可诊断性换来 atomization error、judge correlation、权重漂移和更高调用成本；漏拆联合约束或把 joint 条件错路由为 text-only 会产生虚高分。约束少且可确定性验证时，简单 scorer 更透明。

**Books 落点：** **Integrate** 到 `PLATFORM-EVALUATION-SYSTEM`，锚点为 `66-evaluation-system.md` 的“Per-verifier Outcome 与 Aggregation Rule 都属于 Evaluation Identity”（约 360–364 行）之后。新增内容应强调 modality/claim type 决定 verifier authority，并补充 shared-judge correlated error；不保留模型排行榜。

### [HoliBench: A Cross-Platform Benchmarking and Deployment Toolkit for Foundation Models in CPS-IoT Applications（arXiv:2609.12412）](https://arxiv.org/html/2609.12412v1)

**主题组：** Platform、Evidence 与 Governance · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

§3.1 PAL 统一不同设备 telemetry 的语义单位；§3.2 用同步 bracket 区分 load/prefill/decode 或 vision/decode，并报告 gross 与 idle-subtracted net energy、host/device memory；§3.4 先按 memory/modality 等硬约束剪枝，再让可插拔 solver 选 profile；profile key 包含 model、quantization、backend、device。§7 只在阶段顺序执行假设下组合单模型 profile，而不是宣称任意并发可加。

**关键验证：** 20 个模型、7 类设备、3 档量化、8 个 backend、30+ tasks。论文显示量化并非单调加速：RTX 3070 上 4B 可提速而 sub-1B 反而更慢，A5000 上若干配置更慢，Jetson 小模型甚至显著退化；vLLM 跨设备/尺寸也出现相反效果。顺序共驻 Jetson case 中，solver 预测 latency/power 与实测接近，88.8% cycle 满足 1.6s deadline，而 accuracy-greedy 因 VLM 输出长度导致全部 miss。数字只属于披露配置。

**证据边界：** 证明 device/backend/quantization interaction 足以改变部署排序，并展示统一 phase/energy contract 与 hard-feasibility-first 选择的可行性；不证明 profile 能在线性组合到并发与 dynamic batching，不证明 LLM judge 已校准，不证明 telemetry scope 跨所有平台完全等价。

**Trade-off / failure：** 跨平台可比性换来 PAL 适配、同步测量和 profile matrix 成本；idle subtraction、设备传感器采样率、输出长度和 backend kernel 都可能造成错归因。未 profile 的配置、并发干扰或 runtime revision 漂移会让 solver 选择失效。

**Books 落点：** **Integrate** 到 `PLATFORM-EVALUATION-SYSTEM`，锚点以“从模型名评分到 Versioned Evaluation Object”（约 2339–2345 行）为主，并与 edge real-device contract（约 2864 行）连接。应补入“deployment profile 必须以 device × backend × precision/quantization × phase identity 版本化；顺序 profile 不可未经验证组合为并发预测”。

### [LifeFuse-Mem: Lifecycle-Aware State Fusion Against Temporary Overwriting for Long-Term Memory（arXiv:2609.12436）](https://arxiv.org/html/2609.12436v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)

§4.2 用 learned orthogonal basis 把 rank-8 memory 分为 stable/plastic 各四行；§4.3 router 由 lifecycle metadata 监督，permanent write 同时更新两类子空间，temporary write 抑制 stable-row erase/write；§4.5 的 protected readout 在受控协议中保存 Phase-A stable state，并按 permanent/temporary query 选择融合。这里的保护依赖训练标签和阶段协议，不是模型自行发现生命周期。

**关键验证：** Hard Attribution Anti-Overwrite 显式控制 acquisition、retention 与 overwrite；并在 LoCoMo、MemoryAgentBench 上补测。Qwen3-4B 与 SmolLM3-3B 的 ablation 中，移除 route supervision 明显降低 retention/overwrite 指标，stable rows 与 retention loss 也有贡献但幅度和方向不完全一致。该证据支持 routing 是核心组件，却不证明统一分区适合任意 memory workload。

**证据边界：** 证明已知 lifecycle 标签下，stable/plastic 子空间和受控 readout 可减少临时覆盖；不证明系统能从自然对话可靠推断 `persist`，也不证明受保护的 checkpoint/readout 可直接在开放生产会话使用。

**Trade-off / failure：** 隔离永久状态换来固定容量分配、router 标注、正交约束和读出协议；错误 permanent label 会让污染进入 stable rows，错误 temporary label 会阻止必要持久化。生命周期不确定时仍应保留原始 evidence 并请求澄清，而不是依靠 learned route 自动提交。

**Books 落点：** **Integrate** 到 `AGENT-MEMORY`，精确锚点为 `77-memory.md` 约 1269 行的 `persist / current-session only / reverify / clarify` commit 状态之后。正文应把该论文作为受限 implementation branch：分类器只拥有 route proposal，policy owner 才拥有生命周期 commit；route supervision 不是自主意图识别。

### [Not All Speech Is Intent: Adaptive Self-Correcting Inference Layer for Post-ASR False Wake-Up（arXiv:2609.12469）](https://arxiv.org/html/2609.12469v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)

§3.2 base classifier 与 NLU 并行运行；§3.3 ASCIL 从上一轮 repetition、cancellation、silence 等行为信号提炼 FP/FN pattern，记录 noise、word count、energy、rate 及类别/转写一致性，下一轮用于修正 intent 判定；§3.4 在设备端运行，只 suppress response，不把该层提升为用户意图真值或副作用执行者，也不保存原始音频/转写。

**关键验证：** 3,667 次 proprietary interactions（2,358 intentional、1,309 unintentional），session-disjoint、14 类重叠条件。完全由 baseline failures 构成的 held-out subset 上，54.27% 是条件恢复率，不能解读为总体 error reduction；issue-tagged slice 在 threshold 0.90 下报告 error -24.39%、CAR 89.15→93.49、UICR 25.44→40.72；clean/no-issue set 在较低 threshold 0.85 反而恶化 26.25%。这直接暴露阈值和 slice 依赖。

**证据边界：** 证明基于行为反馈的结构化纠错在作者数据上能修复一部分 post-ASR false activation，且错误操作点随阈值变化；不证明反馈 heuristic 的 precision/recall、本地硬件普适时延、跨用户/语言/设备/风格泛化或生产长期稳定性。

**Trade-off / failure：** 自适应减少重复误触发，却引入 cold start、含糊反馈归因、历史模式 stale、threshold drift 和 silent false rejection。明确 utterance 或高风险动作仍需完整意图/授权检查，不能让 suppression confidence 替代 authority。

**Books 落点：** **Integrate** 到 `AGENT-TOOL-CALLING`，锚点为 `78-tool-calling.md` 的 streaming intent admission（约 414–421 行）之后。应补一条“执行后用户行为只能形成下一次 intent-gate 的更新 proposal；必须分 slice 校准且不能追溯改变已发生 effect”，与实时 intent stability 形成前后闭环。

### [ChitraMiti: Benchmarking Visual Grounding and Modality Reliance in Bengali Geometric Reasoning（arXiv:2609.12509）](https://arxiv.org/pdf/2609.12509v1)

**主题组：** Platform、Evidence 与 Governance · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** PDF · **Books：** 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

ChitraMiti-12.8k 是 12,874 个 synthetic Bengali geometry problems，NCTB-500 是 500 个课本图；共享 15-attribute description schema。§4.1 三阶段分别输入 diagram-only、diagram+description、description-only；§5 用 ±5% margin、alpha=0.05 的 TOST 检查后两者等价；§6 再用关系/数值 ablation 和 swapped spatial relation 测模型是否真正用图像反驳文本。

**关键验证：** 五个 VLM、temperature 0、统一 64-token limit；B/C 在预设 margin 内等价。移除 relational information 的影响大于只移除数值；交换一条空间关系使原本答对样本的准确率下降 2.2–12.0%，表明 aligned-input 得分不能证明 visual verification。只对 Qwen3.5-4B 做 SFT，ChitraMiti-1k 12.7→34.2、NCTB-500 9.6→23.6。

**证据边界：** 证明在 Bengali planar geometry 与该 schema 下，模型可依赖文本代理而不检查图像，paired contradiction 是必要诊断；不证明 description 与 diagram 信息严格等价、不排除 NCTB pretraining exposure；synthetic 描述由 Gemini 生成且仅 200 条经三位双语 annotator 抽查，非符号答案又依赖 LLM judge。小 NCTB 样本使区间更宽，SFT 只覆盖一个 open model。

**Trade-off / failure：** 结构化文本代理便于受控反事实，却可能把图像结构预先解析给模型；swap 也可能产生不自然或含糊样本。它适合 diagnosis，不应成为通用 multimodal capability 排名。

**Books 对读：** **No Change — Existing Coverage**，owner 为 `PLATFORM-EVALUATION-SYSTEM`。`66-evaluation-system.md` 约 2533–2537 行已经明确：hallucination/grounding 分数改善前须排除 decoding/output-distribution 替代解释，并用反事实视觉干预或 paired grounding test 检查证据依赖。该论文提供一个低资源几何实例，但没有改变这条长期合同；无需重复写入 Books，可在 Daily 保留为受限验证案例。

### [One Skill Does Not Fit All（arXiv:2609.12517）](https://arxiv.org/html/2609.12517v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)

论文把长视频 QA 的 frame selection 定义为固定预算下的 evidence acquisition。作者先在 3,000 条有标签 source pool 中选 300 条中等难度样本，让 LLM agent 生成可执行 frame-selection skill，经真实执行反馈保留五个 skill；再只使用 1,500 条无标签 target query/options 诱导 19 类 taxonomy，并用 source-grounded rewrite 估计 category-to-skill utility。推理时冻结 Qwen2.5-VL-7B 或 Qwen3.5-4B，只改变 128-frame budget 的分配；skill 执行失败回退 uniform，回归 skill 不准入。

**关键验证：** 五个 long-video split 上，Qwen2.5-VL 平均从 56.4 提升到 58.8，Qwen3.5 从 59.2 到 60.4；单 skill 的改善小于路由组合。搜索在第六轮附近饱和，继续增加 discovery cycle 没有稳定收益。这组结果支持“skill utility 是 task-slice-dependent derived state”，而不是证明某个 frame selector 普遍最佳。

**证据边界：** target adaptation 能看到目标域 query/options，因此属于 transductive routing；它仍依赖 source labels、LLM 生成 taxonomy/rewrite 和有限模型/视频 benchmark。“Training-free”只表示不更新主 MLLM 参数，不表示 discovery、辅助模型与路由校准没有成本。未证明开放视频、动态 taxonomy、生产延迟或安全关键 evidence selection 下仍成立。

**Trade-off / failure：** taxonomy routing 用额外发现和校准成本换取有限 frame budget 的任务适配；错误分类、taxonomy drift、source-to-target mismatch 或 skill runtime failure 会把 evidence budget 分给错误策略。固定 uniform 或人工规则在任务稳定、样本少、审计要求高时仍更容易复算。

**Books 对读：** `AGENT-PLATFORM` → 第84章「从 Skill Catalog 到 Competence-aware Orchestration」已经把 skill artifact 与按 task slice 漂移的 empirical competence 分开，并要求 authorization/tool hard mask、cost/latency evidence、verify/retry/escalate；紧随其后的 paired marginal-utility Gate 也覆盖 no-skill/skill 对照与负迁移。本文的 frame-selection taxonomy 是该机制的领域实例，不足以新增主干。

### [From Collaboration to Capability: RIVET（arXiv:2609.12578）](https://arxiv.org/html/2609.12578v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)

RIVET 明确分成两个状态阶段。Stage I 让 compact controller 用 expert-augmented GRPO 学习何时调用多个冻结异构 LLM expert/tool；Stage II 只把 verifier 通过的成功协作轨迹转换为 SFT 数据，并移除外部 LLM experts（保留本地 Python）。因此 runtime collaboration、trajectory admission 与 parameter internalization 拥有不同 revision 和 commit boundary。

**关键验证：** learned routing 的 internalized controller 达 44.16，优于单 Qwen3.5-9B 42.08 与 random routing 39.03。普通 trajectory SFT 从 37.67 提至 40.90；对 expert span 的 format weighting 为 0.5 时到 44.16，而 1.0 反降到 42.64，说明提升依赖接口/轨迹转换设计。作者还报告保留 74.68%–84.55% 原有独立成功样本，并内化 46.43%–55.56% 的 expert-rescued cases。

**证据边界：** 结果限两个 controller scale、三个冻结 expert 与数学/GPQA 设置；没有给出长期 token-cost、在线 expert 成本与训练摊销的 break-even。expert-span entropy 只是一项不完整诊断，不能唯一证明知识迁移；format weighting 的敏感性也无法排除学到调用格式而非能力机制。未证明移除 scaffold 后可跨领域保持能力，或 runtime collaboration 总应演进为参数内化。

**Trade-off / failure：** 外部 expert 提高可达轨迹覆盖并保留易回滚的能力边界，代价是在线成本、路由错误和 vendor/tool 依赖；内化降低在线依赖，却引入成功轨迹选择偏差、错误格式蒸馏、能力遗忘与重新训练成本。expert revision、router、verifier 和 conversion policy 任一变化，都应生成新 training identity。

**Books 落点：** 第31章「后训练分支的本质差异是 State Distribution」之后，加入 `external expert routing → verified trajectory admission → parameter internalization → scaffold-removal regression` 的两阶段分支；与第84章外部 skill/平台路由形成 handoff，但训练样本身份、蒸馏与 checkpoint 回归由 Ch31 拥有。

### [SCOPE-OPSD（arXiv:2609.12579）](https://arxiv.org/html/2609.12579v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 仅报告 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

方法在 OPSD 上增加 final-layer hidden auxiliary。privileged teacher state 冻结，低秩 factor 由 privileged residual covariance 与 output-head Fisher pullback 离线构造；Fisher spectral weighting 同时抑制 output-invisible 与已经高敏感方向。rank=64、128 prompts 校准后全程冻结，不增加 rollout、reward 或 inference-time state。matched-random control 保持 rank、spectrum、trace，并在初始化匹配 gradient RMS，因而比普通随机 low-rank 对照更能隔离 orientation 效果。

**关键验证：** Qwen3 1.7B/4B/8B 在共同 step 75，Pure OPSD 为 41.48/62.13/64.45，structured 为 43.33/63.80/65.28；对 matched random 的增量分别为 1.39/0.37/0.93。1.7B 上 Random < GapOnly < Structured，FullHidden 低于 Structured；完整轨迹中 structured 在 12 个 scale-checkpoint pair 全部不低于 pure，并在 10/12 高于 random。离线 factor 捕获 privileged-gap score 为 random 的 4.40 倍。

**证据边界：** 三个 scale 同属一个 model family，任务限 competition math，固定 Avg@12；组件机制对照主要集中在 1.7B。结果不证明 Fisher 条件化唯一导致最终提升、不证明 rank 64 可迁移，也不说明复杂任务和其他 output head 下的计算/稳定性。它是局部几何 regularizer，不是新的 GRPO lifecycle。

**Trade-off / failure：** 低秩 frozen factor 几乎不增加在线状态，但增加离线校准、teacher-state provenance、Fisher 估计和 rank 选择；校准样本偏差、输出头变化或 subspace collapse 会把 privileged error 注入错误方向。普通 OPSD、token supervision 或全 hidden loss 在信号充分、结构校准不可靠时仍合理。

**Books 对读：** `TRAIN-GRPO` → 第33章「Adapter 约束会让 Token Credit 退化为少数 Residual Direction」已承载低秩 update space、hidden residual diagnostic 与错误 redistribution 的边界；privileged teacher 的 sign/authority 也已在前文定义。本文提供更强 matched-orientation case，但不足以扩展长期主干。

### [Beyond Generation and Accuracy: GeoVAD / GeoWeave（arXiv:2609.12606）](https://arxiv.org/html/2609.12606v1)

**主题组：** Platform、Evidence 与 Governance · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

GeoVAD-Bench 的核心不是再加一个最终准确率，而是把视觉几何推理拆成原始感知、辅助图质量、辅助图是否被消费、推理过程与最终答案五个维度。`No-Aux / Auto-Aux / GT-Aux` 三臂干预保持题目与主模型不变，分别测“辅助证据是否有用”和“模型能否自主生成可用证据”。GeoWeave 的 multi-stage SFT + interleaved RL 是配套优化案例，不拥有 benchmark 结论。

**关键验证：** GPT-5.4 + GPT-image2 的 No/Auto/GT 为 69.8/71.6/73.1，说明自主生成接近但仍未达到 reference auxiliary；Qwen3-VL-8B + Qwen-image-edit 为 43.0/36.0/46.0，SenseNova-U1-8B 为 43.8/37.3/50.8，显示“GT 辅助有价值”可以与“自主生成辅助反而伤害结果”同时成立。对两个开源视觉推理系统，stage error 占归因错误的 93.1%/89.7%，最终答对也可能保留错误过程。

**证据边界：** 600 道几何题、特定图形生成器、judge rubric 和模型组合不能代表通用 visual CoT；GT-Aux 是人工/reference 上界，不等于部署可得证据。过程 judge 与最终答案可能共同偏误；配套训练改善不证明五维诊断能自动给出正确修复，也不证明生成图像就是忠实推理。

**Trade-off / failure：** 介入式多维评测能分离 perception、generation 与 uptake，却增加 reference auxiliary、干预生成、judge 和人工裁决成本；Auto-Aux 还引入自生成错误被后续 reasoning 接纳的 correlated failure。低风险任务可保留 final accuracy，只有辅助状态会影响决策时才需要完整干预矩阵。

**Books 落点：** 第66章「从 Final Answer 到 Artifact、Process 与 Environment Evolution」中加入 `No auxiliary / generated auxiliary / validated auxiliary` 的三臂合同，并在「Judge 先证明看见了目标变化」处回链：evaluation owner 分别拥有 auxiliary quality、evidence uptake 与 final outcome，生成模型不能用最终答对自证中间证据有效。

### [SteerDuplex（arXiv:2609.12623）](https://arxiv.org/html/2609.12623v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

以 Moshi-based 7B 为底座，先 SFT，再做两阶段 GDPO：每个 reward channel 独立组内归一化，Stage I 用 continuity 项阻止靠短答骗取 timing reward，Stage II 增加 noise/backchannel continuation bonus。policy loss 施加在 text stream（含 padding/timing token），audio codebook action 不直接承受 policy loss；reward 组合 turn timing、continuity、transcript judge 与 waveform-integrity gate。

**关键验证：** source-clean FDB-v1.5 中 interruption 后正确响应从 72.5% 到 82.5%，backchannel 后 continuation 从 71.4% 到 80.6%；synthetic pause barge-in 从 26.5% 降至 9%，但 takeover latency 增约 40 ms，semantic score 3.94 降至 3.88。只优化 promptness 虽得到 0.670 reward，却让 shared duplex diagnostic 为 0，96 项中 25 项空输出；继续优化又把 interruption reward 从 0.450 提至 0.793，同时 continuation 从 3.20 秒降到 2.00 秒、noise reward 从 1.961 降到 0.770，直接展示 channel interference。

**证据边界：** 英语、固定 reference clips、作者 judge 与 top-checkpoint 选择限制外推；不同系统的 top-3 selection 不完全等价。没有生产 latency distribution、speaker/domain breadth 或 deployment safety。judge 与自动 timing metric 也可能冲突，不能把 composite reward 当作真实 conversational utility。

**Trade-off / failure：** 多通道归一化避免尺度直接吞噬，却不能防止优化一条行为时侵蚀另一条；continuity 可修复短答 hacking，却可能鼓励冗长或延迟让权。必须保存 per-channel reward、空输出、turn/overlap、semantic task 与 latency，而不是只看总 reward。文本 reward 还可能无法正确给 audio action 分配 credit。

**Books 落点：** 在「多 Reward 聚合不能掩盖 Channel Collapse」后补入“per-channel group normalization 仍需 guardrail/retention matrix，constant-in-group channel 不产生梯度”；在「Audio-native Trajectory 还包含 Observation Error」处加入 text/audio action space 与 timing token 的 credit boundary。合并成一条 speech-control 分支，不建立论文式附录。

### [Breaking the Vision–Action Shortcut: LIT（arXiv:2609.12641）](https://arxiv.org/html/2609.12641v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)

Latent Interface Training 先做 image-free、spatial-goal-conditioned action pretraining，形成 action prior；再用 pose supervision 训练 action expert 唯一的 latent visual interface。它不是简单多一层 projector，而是阻断 action head 直接消费容易形成 shortcut 的原始视觉路径，把通用视觉 backbone、action-facing state 与 controller 的责任分开。

**关键验证：** 在 pi0.5、MolmoAct2、FAST-WAM、ImageWAM 四种架构上保持相同预训练 backbone/随机 action expert 和总训练 steps。LIBERO-Plus OOD overall 分别从 68.97→79.67、63.62→71.92、51.44→60.63、83.02→86.89，28 个 perturbation pair 中改善 26 个，最大退化 2.11。真实机器人三任务、300 demos 的 aggregate ID 从 74.7→88，lighting/camera/distractor 分别从 53.3→70、30→46.7、50→63.3。MolmoAct2 消融中 full 71.92，高于 no Stage1、no pose、direct visual access 及单独 staged/pose 路径。

**证据边界：** 实机范围只有三任务，demo、robot、camera 与 controller 受限；LIBERO perturbation 不是开放世界。attention/representation 分析支持 shortcut 假设但不是内部因果完备证明。未证明所有 VLA 都需要 pose bottleneck，或 image-free prior 能覆盖 contact-rich、语言歧义与新 embodiment。

**Trade-off / failure：** latent interface 用额外阶段、pose labels 和信息瓶颈换 OOD 稳定；若 pose 不足以表达任务语义，接口会丢失纹理、对象状态或接触信息。direct fusion 在 viewpoint 稳定、数据充分和低延迟时仍合理；接口失配应回退更广感知、显式几何或保守 controller，而不是让 latent policy 自证安全。

**Books 落点：** 第26章「Action-facing Representation 也是 Gradient Authority Boundary」现有 learned action-query 分支之后，加入 `direct visual path → image-free action prior → pose-supervised latent interface` 的条件演进；同时在「World-action model」前明确该 interface 只产生 action-relevant state，真实 controller/environment 仍拥有动作提交与 transition truth。

### [IABEdit（arXiv:2609.12691）](https://arxiv.org/html/2609.12691v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)

方法把 instruction embedding、source-image embedding 与 source spatial latent 分开；冻结 VLM 在 ground-truth edited image 上生成 Descriptive Anchor，trainable Instruction Aligner 读取生成图像，二者 token-logit KL 的梯度经单步低噪声估计回到 generator。VLM 只在训练期存在，标准 diffusion/flow inference 不新增 verifier；人脸编辑另用可选 ArcFace identity loss。

**关键验证：** RealEdit/MagicBrush 的 CLIP-T、CLIP-I、DINO 与 L1 结果支持 instruction alignment 与 context preservation 可以同时改善；denoise+distill 相对 denoise-only 的 human metric 增 2.47，LoRA 增 4.42，context condition 增 1.81。但 GPT-4o 评测中并非所有 perceptual quality 都领先，说明语义/保存与画质仍是多目标权衡。

**证据边界：** 论文“训练 FLOPs 增加 9.03%”同时列出约 6624 与 733 GFLOPs，数量关系明显不一致，因此成本数字不得进入长期结论。VLM anchor 可能继承描述遗漏、token bias 和训练同源偏差；单步近似不证明完整 denoising 轨迹按同一语义对齐。失败例包括 devoid/off/less 等关系词，不能外推复杂组合编辑或通用视觉 groundedness。

**Trade-off / failure：** 训练时额外 VLM/gradient path 换取 instruction 与 source context 的显式分权，但增加参数、显存、alignment drift 与 anchor bias；更强 identity loss 也可能阻碍目标编辑。pixel/perceptual loss 在局部几何任务中仍更直接，外部 VLM 不应成为图像真实性 authority。

**Books 落点：** 第24章「Distributional Distance 可以成为受限训练目标」之后，补入 image editing 的 `instruction target / preserved source context / spatial latent` 三状态分解，并说明 frozen anchor 只提供训练 signal、generator 保留生成权、独立 evaluator 才判断编辑成功；不写入有冲突的 FLOPs 数字。

### [GRACE（arXiv:2609.12731）](https://arxiv.org/html/2609.12731v1)

**主题组：** Platform、Evidence 与 Governance · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)

GRACE 用 semantic-weighted PCA 定位 diffusion UNet feature 中的 concept-sensitive low-rank subspace，只训练 adapter；safe anchor 从 text embedding 中去除目标方向，CLIP loss 保留 residual semantics，off-subspace regularizer 限制旁路改变。推理时以 normalized projection energy 经 sigmoid threshold 动态开启 adapter，并按 denoising timestep 缩放。

**关键验证：** SD1.5 主实验覆盖 nudity、style、IP、identity 和 COCO preservation，并补 SD2.1/SDXL/FLUX 的泛化展示。Ring-A-Bell 设置中报告受测 nudity/identity attack 为 0%/2%；扩展到 10/20/50 celebrity 时，目标 erasure 与 general preservation 随规模变差。消融显示标准 PCA、去掉 subspace loss 或 energy gate 都降低保留性能；介入太早损害邻近/一般概念，太晚又不足以擦除。

**证据边界：** classifier/CLIP/FID 和有限 attacks 只能给已见行为证据，不是 parameter erasure 或未知 prompt universe 的删除证明；跨模型结果部分是 qualitative。concept-specific threshold、regularizer 与时间 schedule 缺少统一校准，且没有独立 deployment safety 或泄漏证书。

**Trade-off / failure：** 动态 gate 用条件干预减少 collateral damage，但增加 energy calibration、threshold drift 和 concept-specific state；低秩 subspace 选错会漏删或误伤邻近概念。更保守的重训、数据删除、固定 adapter 或拒绝发布在证据不足时仍成立。

**Books 对读：** `PLATFORM-SECURITY` → 第72章「Unlearning 必须分开参数擦除与推理拒答」已明确行为抑制、表示/参数擦除与 retained utility 需分开，并要求有限 attack 不得升级为删除证明；「Diffusion Monitor 的犹豫信号只能用于 Probe Routing」也已规定 diffusion-derived gate 只是 sensor。GRACE 是条件 adapter 的实现实例，没有改变现有 security contract。

### [Balancing Emotional Alignment and Semantic Consistency（arXiv:2609.12830）](https://arxiv.org/html/2609.12830v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 仅报告 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

论文把 flow/diffusion sampler 改写为带 tractable transition density 的 stochastic SDE，以 GRPO 优化冻结 valence-arousal regressor 的 terminal reward；另用 neutral zero-VA generation 作为 semantic anchor，以 CLIP drift penalty 限制模型只追逐情绪分数。它本质上是一个“目标 reward + 保留 anchor”的多目标生成后训练实例。

**关键验证：** 3,300 samples、SD3.5M/SDXL 条件下，完整方法的 V-Err/A-Err 为 1.132/1.492、CLIP 30.179、IQA 0.861；GRPO-only 情绪误差更低（1.097/1.375）但 CLIP 降到 28.648，直接表明 anchor 用部分 reward 换语义保持。30 人、每人 50 张的 user study 支持受测偏好，但规模和抽样不足以形成通用质量结论。

**证据边界：** 各 baseline 接口与 backbone 不同，不能把差异全部归因 GRPO；冻结情绪 regressor 可能把文化/语言/面部表达偏差写进 reward。CLIP anchor 只降低平均语义漂移，不证明细节、构图或身份保持，也没有生产 safety、跨文化或长 prompt 证据。

**Trade-off / failure：** anchor constraint 降低 reward hacking，却会限制真实需要改变语义内容的情绪编辑；权重错误会在 alignment 与 consistency 间形成不可见 Pareto 偏置。人工 rubric、单 reward 或 SFT 在目标简单、reward 不可信时仍更可控。

**Books 对读：** `TRAIN-GRPO` → 第33章「多 Reward 聚合不能掩盖 Channel Collapse」和 policy-update anchor 分支已经覆盖多目标 guardrail、per-channel collapse 与 anchor compatibility。情绪图像生成属于单领域实例，不足以新增长期机制正文。

### [TAC-Merge（arXiv:2609.12897）](https://arxiv.org/html/2609.12897v1)

**主题组：** 跨章结构候选 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** Structural Candidate — model capability merging

Multimodal Influence Mapping 同时观察 image/instruction 改变引起的 representation/readout response，并以 Ricci-curvature-style signal 追踪 expert update 的跨层传播；Coupled Merge Control 再拟合 compact quadratic response surface，联合选择 layer-region coefficient，proposal check 失败则回退 uniform merge。新意在于把多模态 merge 从独立 layer coefficient 调参改为跨层、跨模态耦合选择。

**关键验证：** Qwen3.5-4B 与 Qwen3-VL-8B 上，每个八个 seen task 训练一个 LoRA expert，并测四个 unseen task。4B 的 seen/unseen 为 78.50/68.10，8B 为 77.50/66.50，均高于所列最强 baseline；去掉 MIM、modality contrasts、CMC 或 direction coupling 均退化。large-radius calibration proposal 会伤害 unseen，暴露 response-surface calibration 的迁移边界。

**证据边界：** 只有两个 backbone、LoRA expert、八 seen/四 unseen task 与作者 merge suite；Ricci curvature 是用于路由/拟合的诊断，不是能力传播的完整因果证明。compact quadratic surface 在更远 coefficient、更多 expert 或不同 tokenizer/representation 下可能失真；没有说明 merge 构建成本、训练替代成本和长期 regression。

**Trade-off / failure：** 联合控制减少独立层贪心带来的 interference，却增加 calibration set、response-surface misspecification、coefficient search 与解释成本；unseen degradation 说明 proposal check 不能由 seen score 替代。简单 average/linear merge 在 expert 相近、风险低或校准稀缺时仍合理，冲突高时应回退单模型、adapter routing 或重新训练。

**结构判断：** 当前 `PLATFORM-SECURITY` 第72章「Model Merge Input 是对权重的 Supply-chain Write Access」只拥有来源、隔离、攻击与 release gate，不应承载 capability composition/merge optimization。ROADMAP 目前没有稳定的“model merging as capability composition” owner；建议进入季度结构复核，候选位置为 Part IV checkpoint/artifact 之后、部署 artifact 之前。未形成独立知识链前保留 Weekly，不强塞 Security 或 GRPO。

### [Physics-Aware Video Generation via Agentic Planning and Graph-Guided Optimization（arXiv:2609.13006）](https://arxiv.org/html/2609.13006v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)

§3 将一次 video diffusion 拆成两阶段。VLM 先把动作、对象和环境关系转为可检查的 kinematic/depth conditions；推理期优化再用 object-centric gradient routing 只更新移动对象的相关 latent 区域、尽量保持 passive environment，并根据 kinetic-intensity profile 调整优化密度与学习率。这里新增的不是“再写一段 prompt”，而是让 physical plan 成为指导局部 latent revision 的控制状态。

**关键验证：** §4 的 PhysGenBench 报告 overall 0.59，对照 CogVideoX-I2V 0.52、Frame Guidance 0.51；Physics-IQ 为 28.1，对照 26.5。消融中删除 kinetic profile 或 object routing 后分别降至 26.7、26.9。60 人 2AFC user study 中，作者报告 physical plausibility、frame quality、temporal smoothness 的偏好率分别为 72%、60%、73%。这些均是作者任务、基座、指标和实现条件下的结果。

**证据边界：** FVD 500.2/495.6 与 Physics-IQ 只构成所披露 benchmark 证据；不能证明系统学得一般物理定律，也不能把 object mask 描述成对背景的绝对锁定。§5 明确指出 autoregressive keyframe planning 会累积误差，VLM/API 与 token 成本随 keyframe 数增长；训练外 backprop 还增加推理 latency 和 memory。3–5 个 keyframe、给定基座与 evaluator 不能外推到长视频、复杂接触或实时生产。

**Trade-off / failure：** 稀疏约束保留 base prior，却可能约束不足；过强或错位 mask 会僵化运动、误保留应变化区域。更密优化可提高局部一致性，但增加延迟、显存和对 planner/VLM 共因错误的暴露。直接生成在低约束、低延迟场景仍是合理基线。

**Books 落点：** `MULTIMODAL-GENERATIVE-PARADIGMS` → 第24章「从一次生成到 Plan → Generate → Validate → Retry」之后。补入受限分支：plan 不只供最终 validator 使用，也可形成 object/kinematic-scoped revision state；gradient router 只拥有候选局部更新，base trajectory 与最终 validator 仍拥有 commit。不要吸收 headline 分数为跨模型常数。

### [Kraken: LLM-based Speech-to-Speech Translation via Low-bitrate VQ and Dual-path Source Conditioning（arXiv:2609.13045）](https://arxiv.org/html/2609.13045v1)

**主题组：** 多模态、World Model 与 Embodied · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)

§3 将 S2ST 的语义传输和声学保真分责。冻结 W2v-BERT2 encoder 的连续特征以 12.5 Hz 输入 LLM；输出端使用 25 Hz、8192-code、325 bps 的单层 VQ，目标是重构 SSL feature 而非 waveform。Autowave-X decoder 同时读取低码率目标 VQ 与源语音较低层 SSL feature，前者提供翻译内容，后者补 speaker/prosody；可选 iterative refiner 再修正生成。低码率 token 因而不再独自承担全部语义和声学信息。

**关键验证：** §4 在 Qwen3-8B backbone、约 150k 小时训练数据上评测。FLEURS 十种 X→En 语言中，Kraken 的平均 ASR-BLEU 超过 Seamless 和 Qwen2.5-Omni，但总体略低于 Qwen3-Omni；作者还报告 UTMOS 3.13、speaker similarity 0.75、emotion 0.77、AutoPCP 2.48，并用 source-conditioning ablation 支持双路径责任划分。CVSS 八语平均 ASR-BLEU 为 43.5。人工评测为 25 个 clips、3 名专业双语标注者，Krippendorff α 为 0.772–0.878。

**证据边界：** 结果只覆盖 X→En、十种语言与离线任务；论文不支持 streaming readiness、通用 speech codec 优越性或对所有音色/情绪的保真。作者说明 speech fine-tuning 会损失一般 instruction-following，且因 deepfake 风险未开放模型与代码，第三方可复现性受限。人工评测规模很小，Qwen3-Omni 在部分剩余指标更强。

**Trade-off / failure：** 低码率降低 LLM 序列负担，却把声学细节责任转给 source-conditioned decoder，并新增 source/target 时间对齐、说话人泄漏、decoder artifact identity 与安全滥用风险。源音频不可用、目标说话人应匿名化或需要在线低延迟时，独立 codec/文本中间层仍可能更合适。

**Books 落点：** `MULTIMODAL-REPRESENTATION` → 第23章「Rate、distortion 与下游容量必须联合选择」之后，并与「Token Hierarchy 可以承载不同时间尺度」衔接。新增不对称责任链：低 rate semantic token 服务 LLM，source-conditioned waveform decoder 保留 speaker/prosody；把 privacy、streaming、alignment 和 decoder capacity 写成代价，而不是将 325 bps 写成普遍最优点。

### [Continue, Adapt, or Yield: In-Turn Adaptation to Overlapping Speech in Full-Duplex Agents（arXiv:2609.13117）](https://arxiv.org/html/2609.13117v1)

**主题组：** Platform、Evidence 与 Governance · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

§3 将 listener cue intent（backchannel / collaboration / interruption）与 speaker observed response（continue / adapt / yield）分开。二元 stop/continue 会把“接纳对方信息但不交出话轮”的 adapt 隐去；full-duplex evaluation 因而必须同时判断 cue intent、内容 uptake 和 floor transfer，而不是只测是否停说。

**关键验证：** 语料为 80 段双通道英语对话、20.32 小时、39 名参与者；作者先取得 2,591 个 cue inventory，再从 300 个 human-confirmed cues 构造 paired case，最终 208 个 active/scorable pairs。真人在 collaboration cues 上 adapt 68.2%，PersonaPlex 为 34.8%；真人面对 interruption 也只在 39.3% cases yield，45.9% 是 adapt。response scorer 与人工在 142 个可比样本上 agreement 108/142（76.1%），Cohen’s κ=0.641。

**证据边界：** 一个 PersonaPlex checkpoint、单次 generation、英语语料、recorded partner、有限 history 和十秒窗口不能代表开放式实时对话。cue intent review 会看到 A 的后续响应，collaboration 定义又部分依赖 uptake，存在标注耦合；46 个 unusable model responses 与 86 个 cue-onset inactive cases 缩小了有效分母。voice conversion、网络、并发和真实设备延迟也不在结论内。

**Trade-off / failure：** 三态 contract 改善 failure attribution，却增加 cue labeling、时钟同步、重叠区间和 scorer calibration 成本。`adapt` 识别错误会把无关继续误当作协作；始终 yield 则会把正常协作 cue 当成抢占。简单 turn-taking 在单向、半双工或不允许重叠的产品中仍合理。

**Books 落点：** `PLATFORM-EVALUATION-SYSTEM` → 第66章「Duplex Agent Evaluation 要联合测 Timing 与 Content」。将 response state 从 stop/continue 扩展为 continue/adapt/yield，并分别保存 cue intent、uptake evidence、floor transfer 与 latency window；Ch23 只承接 audio representation handoff，不拥有 evaluation contract。

### [InitGen: Candidate Generation for Interaction Initiation in Intelligent Assistants（arXiv:2609.11953）](https://arxiv.org/html/2609.11953v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)

系统在用户尚未明确提问前一次生成一组 initiation candidates，之后由既有 filter/ranker 只曝光其中子集。未曝光 candidate 没有可观察 outcome，逐 candidate 打标签会制造伪监督；作者因此将被序列化的 query set 作为 KTO alignment 单元，仅在至少一项曝光时按 set-level click outcome 更新，并用 user-activity 与 ranking-score weights 调节反馈可信度，训练数据采用 rolling window 周期更新。

**关键验证：** 论文报告在 OPPO Xiaobu Assistant 的生产 A/B 中保持相同流量与下游 pipeline；CTR 从 0.95% 到 1.61%（相对 +69.1%），exposure +17.9%，total clicks +99.5%。服务侧使用 vLLM、20 张 A100 80GB，超过 12K query-set QPM，约 150 ms latency，低于披露的 180 ms 约束。上述数字只属于作者产品、流量、候选生成和 ranker contract。

**证据边界：** click 是 engagement proxy，不等于回答质量、长期满意、安全或 causal usefulness；未曝光 candidates 仍是盲区，ranking score 加权可能放大现有 ranker 偏差。私有生产数据限制复现，报告没有证明 rolling window 消除了 drift/feedback loop，也不能把相对 CTR 增益外推到其他 assistant。

**Trade-off / failure：** set-level label 避免虚构 item-level preference，却牺牲候选内 attribution；频繁更新更贴近近期交互，也增加 policy–ranker co-adaptation、版本漂移和 selection bias。若每个 item 都有独立 outcome，item-level preference 仍提供更精确 credit。

**Books 落点：** `TRAIN-RLHF` → 第31章「反馈预算必须绑定样本粒度与可观测不确定性」之后。补入原则：optimization unit 必须匹配 outcome 的可观测粒度；未曝光 item 不得被反推 label，set serializer、exposure/ranker version、weight policy 与 rolling-window revision 都进入 preference artifact identity。第84章只承接上线与反馈回路。

### [HeatCache: Thermal-aware Energy-efficient LLM Inference Scheduling（arXiv:2609.12449）](https://arxiv.org/html/2609.12449v1)

**主题组：** Inference Runtime · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)

§3 把 chassis-level AIO liquid loop 的短时热惯性建模为可消费的 heat budget，而不是只把温度当作事后告警。lumped RC model 推进 coolant/thermal state，HeatiTS 用 job history 和 electrical regularization 预测 job-level power、heat 与 duration；online controller 先做快速 budget check，再用 RC model 精确验证，联合选择 micro-batch、DVFS 和 GPU placement，受 TTFT/TPOT 与 thermal threshold 约束。

**关键验证：** §4 的原型为 4×RTX 4090 24GB、i9-13900K、机箱级水冷，覆盖量化 Llama3.1、Qwen2.5-Coder、DeepSeek-R1 和 LMSYS/CodeAlpaca/QReCC。作者报告最高 18% compute-energy reduction、最高 82.5% SLO-violation reduction、0.8–2.8% throttle exposure；消融支持 RC model、HeatiTS 及 batch+DVFS 联合控制，但 precise verification 增加约 7% scheduling latency。

**证据边界：** 单机、单 chassis AIO 不证明 direct-to-chip/CDU/immersion、rack-scale 或 multi-tenant 行为；ambient setpoint 固定，未联合 HVAC 优化。预测器需要 hardware/site calibration，RC reduced-order model 会受流量、冷却液和老化漂移影响。厂商/作者数字不能转写为通用能耗或 SLO 收益。

**Trade-off / failure：** 利用 thermal inertia 可在安全窗口内提高有效容量，却引入 sensor freshness、模型校准、控制延迟和 runaway/oscillation risk；过保守会浪费 headroom，过乐观会 throttle 或违约。硬温度/安全上限必须由独立 fail-safe 拥有，controller 只能提出 operating point。散热余量充足或遥测不可信时，固定 power cap 与保守 admission 仍更可审计。

**Books 落点：** `INFER-SCHEDULING` → 第56章「SLO-aware Admission」之后、进入长期 reservation 前。把 thermal state 定义为带时间常数的 versioned resource：sensor/RC predictor 提供 heat-budget estimate，scheduler 联合 admission/batch/DVFS/placement，runtime 与硬件保护拥有实际温度和 emergency action。第70章只承接 energy accounting，不重复控制机制。

### [RoofLang: Enabling AI-Driven Architecting of LLM Inference Systems（arXiv:2609.12551）](https://arxiv.org/html/2609.12551v1)

**主题组：** Inference Runtime · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)

§2 定义 typed DSL，将 compute graph、hardware graph、placement、semantics-preserving transformations 和 discrete-event simulation 放进同一 architecture artifact。transformation 不是任意文本编辑，而是更新 graph 与 analytical attributes 的受约束操作；agent 只提出 system architecture candidates，simulator/语义约束负责可行性与性能反馈。

**关键验证：** §3 在代表性现有/未来 LLM 与硬件上构造 throughput/interactivity Pareto simulation，并给出三项 agent-found designs：PP cost/head-aware partition +20.3%、DP–CP expert splitting +6.23%、node-local expert replication +50.1%。这些均是 simulator 下的候选 architecture results，不是实际生产系统测量。

**证据边界：** §5 明确指出结果依赖初始 compute/hardware graph 正确；模拟简化包括理想 MoE load balance，并遗漏 KV append、speculative structure 和 Kimi multimodal 等路径。大型 Kimi K3 / 128-GPU simulation 可耗费数小时和数百 GB。论文没有证明 agent-found plan 在真实 runtime、故障、动态负载或编译器 lowering 后保留同等收益。

**Trade-off / failure：** typed IR 扩大可审计搜索空间，却把 correctness 责任转移到 transformation semantics、cost model 与 simulator calibration；模型遗漏会产生“合法但物理错误”的 Pareto frontier。手工 plan 和真实 hardware replay 在稳定部署或模型不可信时仍是必要 fallback。

**Books 落点：** `INFER-TENSORRT-LLM` → 第49章「Execution Plan 先拥有 State，再选择 Kernel」之后，并在「Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission」之前建立 architecture-search 上层：typed compute/hardware/placement graph → semantics-preserving transform → simulation/correctness gate → measured replay → commit。不要把模拟百分比写成 runtime speedup。

### [Where Decoder Cosine Similarity Fails for SAE Feature Flow Discovery（arXiv:2609.12591）](https://arxiv.org/html/2609.12591v1)

**主题组：** 模型、表示与生成机制 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 标准完成 · **Access：** HTML · **Books：** 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)

§2 同时训练 state SAE 与 MLP-update SAE，以候选 state/update feature 对预测下一 residual target feature；仅用 decoder cosine 排序后，再通过 decoded-update ablation 测 target feature 的归一化变化。它把“向量方向相似”与“该 update 是否实际改变目标 feature”分成不同证据层。

**关键验证：** 在 Pythia-160M、L7→L8、20M tokens 的 atlas 中，作者找到 38,125 个强 ablation-effect transitions，其中 88.0% 的 state-target 与 update-target cosine 都低于 0.7；Gemma-3-4B 的 preliminary top-30k candidates 中相同比例为 53.6%。这支持高 cosine threshold 会漏掉一部分受控干预可见的局部 transition。

**证据边界：** §4 明确限定为一个 Pythia layer pair/full atlas，以及一个 Gemma layer pair/top-ranked subset；目前只研究 MLP update。结论依赖 SAE dictionary、reconstruction、TopK 和 pruning，decoded-feature ablation 仍是局部 replacement intervention，不证明 feature label 唯一、整网行为语义或可安全编辑模型。Gemma 跨模型比例也明显较弱。

**Trade-off / failure：** causal ablation 比 cosine 更接近机制证据，却扩大组合搜索与 intervention 成本，并可能受 SAE reconstruction error 和 off-manifold replacement 干扰。cosine 仍适合作为便宜的 discovery heuristic，只是不能拥有最终 causal verdict。

**Books 对读：** `WORLDVIEW-REPRESENTATION` → 第5章「从可读出到机制：证据应逐级变强」。现有正文已明确 `correlation → decodability → localized intervention → downstream behavioral change → cross-context / cross-model replication`，也保留 replacement-model error、局部近似和跨模型复现边界；本论文是该命题的受限案例，不应为保存论文名称重复正文。

### [Can LLMs in Draft-Verify-Revise Pipelines Resolve Deictic Ambiguity?（arXiv:2609.12162）](https://arxiv.org/html/2609.12162v1)

**主题组：** Agent information、action 与 workflow state · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)

论文用 controlled minimal pairs 检查 draft→verify→revise context cascade 中同一词 `previous` 的 referent：它可能表示操作时点前的值，也可能被模型错误绑定到名为 Previous 的字段。primary/ablation experiments 改变 grader feedback 的 error-classification labels，并用 rationale probe 区分是否表述了 operational interpretation、是否真正让该解释控制 verdict。核心机制不是模型榜单，而是自然语言相对指代在 stage handoff 中没有稳定 identity。

**关键验证：** 10 个 base examples×3 conditions，六个模型、21 种 reasoning configurations；每次实验为 12,600 trials。balanced accuracy 从 0.156 到接近 1；例如 GPT-5.2 none 为 0.156、max 为 0.942。Gemini 3 Pro 各 effort level 均超过 0.94，作者报告 low effort 在该测试上以约 5% per-trial cost 超过 GPT-5.2 xhigh。e-value procedures 控制多重比较，且 reasoning effort 的改善并非单调。

**证据边界：** §4.5 指出所有 10 个例子的正确 target 都恰好位于 `Current` 字段；只做 field matching 也可得 1.0，因此高分不证明 operational reasoning。刺激只有一个词、合成场景和重复变体；rationale classifier 对正确 verdict 的生成机制不可见，后验 audit 也不是完全独立，模型大小/成本比较受 provider 配置约束。论文没有实际测 revision artifact 的最终正确性。

**Trade-off / failure：** 把 referent 编译成 typed field/version 可减少歧义，却增加 schema、normalization 和 migration 成本；字段名本身若错误或 context version 过期，结构化表示仍会稳健地产生错结论。简单短流程且唯一上下文时自然语言 handoff 仍足够。

**Books 落点：** `AGENT-WORKFLOW` → 第81章「Task State Alignment 是每次 Dispatch 的前置条件」。补入 deictic normalization gate：dispatch 前把 `previous/current/latest/that result` 解析为 `(artifact_id, field, revision, temporal standpoint)`；无法唯一绑定时重新询问或 defer，不能把字段 label 当成 referent 真值。第66章可引用 minimal-pair evaluation 方法，但 canonical owner 是 workflow state。

### [Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents（arXiv:2609.12896）](https://arxiv.org/html/2609.12896v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)

§4 在固定 rank 的单一 agent LoRA 中处理 heterogeneous trajectories。Behavior Quotient Balancing 用 reference histories 上的 decision distributions 定义局部 behavior geometry，将产生近似决策变化的轨迹更新视为冗余并降权；Decision Preserving Compression 再把 balanced update 投影到可实现的 fixed-rank tangent space，以 effective-weight error 与 decision distortion 的联合目标重新分解 LoRA factors。这里的 equivalence 由行为作用定义，而非只看参数距离。

**关键验证：** Qwen3.5-4B/9B 上覆盖 AppWorld 与 BrowseComp-Plus。论文报告相对最强 MoRAgent baseline 在八个任务指标平均提高约 2.14/2.12 points，并减少 interaction count。去掉 BQB 后 4B/9B 的 AppWorld Test-C 分别下降 3.57/3.83 points；去掉 DPC 的平均下降约 3.64/3.57 points。完整方法在 8 个设置中领先 7 个，γ 消融显示 weight approximation 与 decision preservation 存在 operating-point trade-off。

**证据边界：** 仅两个 backbone size、两个 agent benchmark，不证明开放工具、真实生产或所有 LoRA task。behavior quotient 是围绕选定 reference histories 的局部几何；history coverage、linear/tangent approximation 和 evaluator 都会决定何为“等价”。没有单独的 safety、catastrophic forgetting 或广泛原能力回归；个别设置中 BQB removal 甚至略升，不能宣称每个任务都受益。

**Trade-off / failure：** decision-aware compression 更贴近 agent action，却增加 reference-history selection、Jacobian/geometry 计算、压缩校准和 distribution-shift 风险。错误的 reference set 会把长尾但关键行为当作冗余。标准 LoRA/weight-error projection 在任务同质、行为样本不足或需要简单可复现时仍合理。

**Books 落点：** `TRAIN-LORA` → 第30章「Rank 与 target modules 决定更新空间」之后。补入固定 rank 下的第二层问题：名义低秩空间确定后，trajectory redundancy 应由 induced decision change 判断，压缩 gate 同时约束 weight approximation 与 decision distortion；reference histories、behavior metric 和 projection revision 必须成为 adapter artifact identity。

### [Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction（arXiv:2609.13082）](https://arxiv.org/html/2609.13082v1)

**主题组：** Platform、Evidence 与 Governance · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)

§3 把 benchmark construction 表成 typed artifact dependency graph，而不是一次性 prompt chain。typed skills 声明 I/O、precondition 和 backend；forward path 从 intent、data、evidence/state 生成 benchmark/report，requirement contracts 和 offline/interactive track gates 验证中间 artifact。失败时 provenance 决定 local repair、rebind、resynthesize、reexecute 或 upstream rollback，只重建受影响 downstream closure。

**关键验证：** 构造套件覆盖六类 embodied settings；interactive evaluation 含 220 个 executable tasks。质量评测使用 4 个 LLM/VLM judges 和 10 名人类标注者。作者报告 10k-item offline build 为 38–160 分钟、平均 86 分钟、11.45M tokens；消融中移除 requirement contracts 使 quality 降 10.47 points、valid rate 降 31.5 pp，移除 provenance-guided repair 使 token cost 从 2.62M 上升至 3.93M。不同组件移除后 judge-human agreement 也从约 0.87 降至约 0.78。

**证据边界：** 论文没有独立 limitations 章节。LLM-as-judge、较小 human sample、生成/资源/模拟器域和 generator–verifier 共因偏差都限制结论；embodied simulator 的有效性不等于真实物理安全或 sim-to-real validity。model ranking 只说明所构造 suite 在当前模型间形成差异，不证明 ground truth、无泄漏或完整能力覆盖。

**Trade-off / failure：** dependency/provenance graph 降低全量重建，却增加 schema、edge correctness、cache invalidation 和 repair policy；漏掉依赖边会让 stale artifact 被错误复用，过度传播又退化为全量重建。依赖不清、judge 不可信或高风险真实环境中，应回退 full rebuild、人工检查或真实 execution gate。

**Books 落点：** `PLATFORM-EVALUATION-SYSTEM` → 第66章 verifier-first benchmark synthesis 段（以 `typed inspection endpoint + executable checker` 开头）之后。将单 task/checker artifact 扩展为 typed multi-artifact dependency graph，并明确 failure diagnosis 只允许重开有 provenance 支持的 downstream closure；offline 与 interactive track 保留各自 validity gate。第81章只承接可恢复 workflow 的通用状态机。

### [Performance, Efficiency and Collapse — Advantages and Challenges in Offline Post-training of Code LLMs（arXiv:2609.11956）](https://arxiv.org/html/2609.11956v1)

**主题组：** Training 与数据 · **状态：** active · **Evidence Level：** Primary / exact-v1 · **Review：** 深入完成 · **Access：** HTML · **Books：** 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)

官方 `cs.LG/new` 将该论文列为 2026-09-14 Monday new-submission 第 5 项，因此本日报按公开列表事件归属；Submission history 中更早的 submitted time 不覆盖该列表归属。论文在固定 CodeNet 正负提交对上执行多 epoch、RLOO-like offline policy update：正负样本都远离初始策略，但负样本 token logit gap 增长更快；collapse run 的 sequence log-prob variance 爆炸，而由固定组构造的 advantage variance 仍保持稳定。这将问题定位为固定 support 被重复消费后产生的 importance-ratio 与 policy-distribution 失控，而不是笼统的 reward 下降。

**关键验证：** 8,321 个 Python submissions、609 个题目，覆盖 Qwen、DeepSeek 与 CodeLlama 多个尺寸，并在 MBPP、APPS 上分别报告 pass@1 与 pass@k。不同模型对同一 recipe 的响应明显不同：部分小模型在较高学习率下先升后跌至 pass@1 为零，而 CodeLlama 基本不获益。跨模型复现支持 failure signal 的存在，但没有隔离预训练或后训练数据差异是否构成模型家族差异的因果来源。

**证据边界：** 证据证明固定离线代码对上的 repeated offline policy update 存在可复现、模型相关的崩塌，并给出 log-prob variance 与正负 logit-gap imbalance 作为诊断；不证明这些指标是充分的提前预警器，也不证明更换 negative sampling、clipping 或在线数据即可修复，更不能直接外推到自然语言、工具轨迹或其他 reward contract。

**Trade-off / failure：** 离线数据便宜、可重放且不依赖在线环境，但重复消费会把 policy 推离数据支持域；更保守的 epoch、learning rate 与 ratio gate 会牺牲样本复用和短期收益，在线补样本又增加执行成本与环境非平稳。主要 failure 包括负样本 likelihood 被过度压低、ratio 方差爆炸、能力 collapse，以及跨模型 recipe 不可移植；稳定 distillation 与在线 rollout 应作为条件分支。

**Books 落点：** `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 offline distillation 与 outcome-routed update 之间。长期命题是：固定离线 support 的 policy-gradient 重复更新必须同时 gate epoch、learning rate、ratio/log-prob variance 与正负 likelihood drift，不能把数据可重放误写为可无限安全优化。

## 5. 缺口与下一步

Meta 和 MiMo 的目录限制是本窗终态保留项，不支持正面证据、Books 写回或无遗漏断言。定点重开条件是取得带日级时间的完整官方列表或唯一新材料身份；届时只重开相应来源与本窗归属，不扩扫无关历史。109 项当窗候选中没有 Blocked、Withdrawn 或 Disputed，普通证据、Books 写回和独立复核待办均为零。

### 候选前关闭（266 项）

下列是排除理由族的代表样本，不是只审了这些样本。266 项均已完成 title + abstract 语义筛选；只有标题已明确落在暂停或范围外领域时才不继续展开摘要。

| 排除理由族 | 代表身份 | 关闭依据 |
| --- | --- | --- |
| AI for Science 当前暂停 | `2609.12107`, `2609.12223`, `2609.12260` | 强制位移抽取、分子碰撞截面、生物医学假设发现属于下一阶段领域研究，不能通过 Data/Evaluation/Agent 绕回。 |
| 单领域应用或数据集替换 | `2609.11997`, `2609.12122`, `2609.12793`, `2609.12827` | EEG、语音学、金融预测、医学成像中复用已知模型并提升任务指标，没有给出可迁移的模型/系统机制。 |
| 通用优化/控制理论，未落到大模型主线 | `2609.12014`, `2609.12119`, `2609.12785`, `2609.13040` | 数学上可能新颖，但未改变当前大模型训练、推理或平台设计判断。 |
| 普通机器人/轨迹规划，缺少 FM/VLA/world-model 增量 | `2609.12248`, `2609.12502`, `2609.12795`, `2609.12927` | robotics contribution 不自动成为 AI-System-Design 候选；需要可迁移的 foundation-model、state 或 control 增量。 |
| 只新增任务覆盖的 benchmark/dataset | `2609.12151`, `2609.12366`, `2609.12653`, `2609.12872` | 没有暴露既有评价协议测不到的系统能力、混杂因素或 failure boundary。 |
| 局部模块重组或单 operating point | `2609.12382`, `2609.12915` | 新模块、损失或 adapter 在局部任务更好，但摘要未显示新的长期机制解释或适用边界。 |
| 立场、综述或“agentic”包装不足以准入 | `2609.11942`, `2609.11945`, `2609.12105`, `2609.12932` | 提出方向、分类或系统术语，没有可定位的新机制、可检查反证或真实行为变化。 |
| 通用 edge/HPC/system 但无 LLM 可迁移合同 | `2609.11944`, `2609.11946`, `2609.12091` | 资源或性能问题存在，但没有建立对大模型 workload、state 或 SLO 的新判断。 |

### Repository Changes

- `MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)：吸收 1 项经限定的长期语义增量（`2609.12303`），并保持旧方案、条件、代价与 fallback 的衔接。
- `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)：吸收 3 项经限定的长期语义增量（`2609.12686`, `2609.12814`, `2609.13141`），并保持旧方案、条件、代价与 fallback 的衔接。
- `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)：吸收 5 项经限定的长期语义增量（`2609.12099`, `2609.12563`, `2609.12549`, `2609.12874`, `2609.13045`），并保持旧方案、条件、代价与 fallback 的衔接。
- `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)：吸收 2 项经限定的长期语义增量（`2609.12691`, `2609.13006`），并保持旧方案、条件、代价与 fallback 的衔接。
- `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)：吸收 4 项经限定的长期语义增量（`2609.12036`, `2609.12090`, `2609.12441`, `2609.12347`），并保持旧方案、条件、代价与 fallback 的衔接。
- `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)：吸收 4 项经限定的长期语义增量（`2609.12285`, `2609.13053`, `2609.12081`, `2609.12641`），并保持旧方案、条件、代价与 fallback 的衔接。
- `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md)：吸收 3 项经限定的长期语义增量（`2609.12316`, `2609.12584`, `2609.12394`），并保持旧方案、条件、代价与 fallback 的衔接。
- `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)：吸收 2 项经限定的长期语义增量（`2609.12123`, `2609.12896`），并保持旧方案、条件、代价与 fallback 的衔接。
- `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)：吸收 4 项经限定的长期语义增量（`2609.12459`, `2609.12651`, `2609.12578`, `2609.11953`），并保持旧方案、条件、代价与 fallback 的衔接。
- `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)：吸收 6 项经限定的长期语义增量（`2609.12419`, `2609.12424`, `2609.13060`, `2609.12245`, `2609.12623`, `2609.11956`），并保持旧方案、条件、代价与 fallback 的衔接。
- `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：吸收 1 项经限定的长期语义增量（`2609.13012`），并保持旧方案、条件、代价与 fallback 的衔接。
- `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)：吸收 4 项经限定的长期语义增量（`2609.12208`, `2609.12330`, `2609.12379`, `2609.12551`），并保持旧方案、条件、代价与 fallback 的衔接。
- `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)：吸收 3 项经限定的长期语义增量（`2609.12399`, `2609.12923`, `2609.12978`），并保持旧方案、条件、代价与 fallback 的衔接。
- `INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)：吸收 1 项经限定的长期语义增量（`2609.13134`），并保持旧方案、条件、代价与 fallback 的衔接。
- `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)：吸收 1 项经限定的长期语义增量（`2609.12449`），并保持旧方案、条件、代价与 fallback 的衔接。
- `PLATFORM-GPU-SCHEDULER` [Ch63](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)：吸收 1 项经限定的长期语义增量（`2609.12276`），并保持旧方案、条件、代价与 fallback 的衔接。
- `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)：吸收 13 项经限定的长期语义增量（`2609.12002`, `2609.12101`, `2609.12191`, `2609.12475`, `2609.12766`, `2609.12884`, `2609.13003`, `2609.13005`, `2609.12397`, `2609.12412`, `2609.12606`, `2609.13117`, `2609.13082`），并保持旧方案、条件、代价与 fallback 的衔接。
- `PLATFORM-TRACE` [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)：吸收 2 项经限定的长期语义增量（`2609.11938`, `2609.12299`），并保持旧方案、条件、代价与 fallback 的衔接。
- `PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)：吸收 1 项经限定的长期语义增量（`2609.11940`），并保持旧方案、条件、代价与 fallback 的衔接。
- `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)：吸收 4 项经限定的长期语义增量（`2609.12163`, `2609.12413`, `2609.12448`, `2609.12808`），并保持旧方案、条件、代价与 fallback 的衔接。
- `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)：吸收 1 项经限定的长期语义增量（`2609.12437`），并保持旧方案、条件、代价与 fallback 的衔接。
- `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)：吸收 1 项经限定的长期语义增量（`2609.12436`），并保持旧方案、条件、代价与 fallback 的衔接。
- `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)：吸收 2 项经限定的长期语义增量（`2609.11957`, `2609.12469`），并保持旧方案、条件、代价与 fallback 的衔接。
- `AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md)：吸收 1 项经限定的长期语义增量（`2609.12746`），并保持旧方案、条件、代价与 fallback 的衔接。
- `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)：吸收 2 项经限定的长期语义增量（`2609.12127`, `2609.12162`），并保持旧方案、条件、代价与 fallback 的衔接。
- `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)：吸收 2 项经限定的长期语义增量（`2609.12216`, `2609.12748`），并保持旧方案、条件、代价与 fallback 的衔接。

以上共 74 项；其余 24 项由现有正文覆盖，8 项只保留日报上下文，2 项在证据审阅后拒绝，1 项进入季度结构复核，没有为了制造 diff 重复写入。

### Open Questions

- fixed recurrent state 在需要逐事实可寻址回忆时，怎样暴露可验证的 information-loss budget 与 dense fallback 条件？
- 多模态与 VLA 的 mutable state、观测时钟和 action commit 在跨设备 serving 中应如何形成统一 identity？
- pre-action verifier 的 false-positive budget 应怎样随 effect reversibility、延迟与用户确认成本变化？
- 训练中的 teacher intervention、reward graph 与 expert-path replay 如何携带足够 provenance，而不把 off-policy contamination 隐藏在“半 on-policy”标签中？
- benchmark、judge、retrieval 与 longitudinal memory 的版本怎样共同进入 release gate，避免单一最终分数掩盖 harness、surface leakage 或 future-state contamination？
- compiler/kernel 与 GPU profiler 的局部收益怎样在真实 concurrency、precision、shape 和 SLO 下转化为可归因的端到端 goodput？

### Sources

- [arXiv Monday new submissions](https://arxiv.org/list/cs.AI/new?skip=0&show=2000)，以及第2节列出的十二个目标分类列表；公开事件 2026-09-14T08:00:00+08:00，访问日期 2026-09-14。
- 第3、4节链接的 109 份当窗 exact-v1 原始论文：105 份 HTML、4 份 PDF；访问日期 2026-09-14。
- [OpenAI Research](https://openai.com/research/)、[Anthropic Research](https://www.anthropic.com/research)、[Google DeepMind Research](https://deepmind.google/research/) 及第2节列出的其余官方每日入口；访问日期 2026-09-14。

## 6. 复核

复核者：非作者独立语义复核（Codex / `semantic_review_sep_w37`）

结论：通过

独立复核覆盖来源与窗口归属、候选准入、评分与审阅深度、109 项 Evidence、Books 决定、74 项正文写入、证据边界、链接与 Markdown。`375 = 109 + 266`、`83 + 24 + 2 = 109`、`74 + 24 + 8 + 2 + 1 = 109` 均自洽；候选表与 Evidence 逐项对应。复核纠正了 `2609.11956` 的公开列表归属并确认其 Ch33 唯一正文绑定，清除了 Ch54 中 `2609.12923` 的重复绑定，确认其余 Integrate 项均有真实、唯一、owner 一致的正文落点。Meta 与 MiMo 的来源限制已隔离，`2609.12897` 保持 Structural Candidate，不把无法验证的目录内容或结构候选强行写入 Books。

**机器校验：** 通过（`scripts/validate_research.py --report`、`git diff --check` 与未跟踪日报的 `git diff --no-index --check` 均无错误）；机器结果不替代独立语义复核。
