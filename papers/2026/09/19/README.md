# Daily Research — 2026-09-19

**规范：** V3
**窗口：** 2026-09-18T09:00:00+08:00 ～ 2026-09-19T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-21T13:12:00+08:00

## 1. 结论

本窗的来源扫描已经完成，候选准入在三轮有限返修后重新冻结：arXiv 十二个目标分类共有 633 个当窗 new/cross 唯一 identity；前两轮各恢复 29 项，fresh false-negative audit 又定点重开 15 项且全部恢复。对同一 generic-close 理由簇追加 12 项分层摘要抽检后没有发现新的漏收，最终冻结 142 个 arXiv Source Family。机构来源另保留 3 个官方工程 Source Family；replacement list 中的 AIREP v2 与 CatchBench v4 是两个不重复计分的重要修订事件。因此，本日报需要处置 145 个新 Source Family 与 2 个修订事件。完整身份闭包见 [denominator closure](../_sources/daily-20260919/denominator-closure.md)，有限返修范围、逐项裁决、撤回/纠错和官方 commit 见 [screening ledger](../_sources/daily-20260919/screening-ledger.md)。

本日最重要的长期增量集中在五条链路：训练信号的数值身份（GRPO advantage scale、on-policy distillation 的 semantic EOS、off-policy score centering）；运行时状态的明确所有权（KV fabric、block-parallel diffusion training、prefix reuse、weight-sync transaction）；Agent 执行的并发与证据边界（destructive preemption、verification-status laundering、cognitive serializability、cut-point replay）；评估传感器不能冒充真值（probe 可读性、CoT entropy、verbal confidence、overclaiming）；以及 AR、masked diffusion、video-native recurrent/attention 混合路线的不同并行与状态契约。

139 个 arXiv 家族已读取 exact-v1 HTML 的方法、评价和相关限制；`2609.19866v1`、`2609.20497v1` 与 `2609.20543v1` 使用 exact-v1 PDF 完成同等深度审阅。3 个工程事件读取了官方 commit 与变更范围；全部 147 个事件的 Method / Evaluation / Limitations 定位见 [evidence locators](../_sources/daily-20260919/evidence-locators.md)。作者侧已完成评分、证据边界和 Books 比较：24 个新 Source Family 均已写入对应 Stable Knowledge Node，前两轮恢复的 58 项和本轮 13 项由现有正文具体论点覆盖。当前账目为 `24 Integrate + 120 Existing Coverage + 1 Weekly Only = 145`。AIREP v2 与 CatchBench v4 的修订增量也已分别进入 `PLATFORM-SECURITY` 与 `PLATFORM-EVALUATION-SYSTEM`。fresh non-author reviewer 已在限定范围内复核第三轮 15 项恢复、12 项关闭样本、账目与两项新增 Books 绑定，未发现需要继续执行的工作，本报告完成。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/News 官方列表按窗口检查；可见 GPT-Live API 发布为 09-10，Privacy Filter 页面中的 09-18 只是示例文本，无当窗候选 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 列表与 09-18 可见官方内容；企业安全 webinar 是部署说明，不是新增研究机制，无当窗候选 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind/Google Research 列表；09-18 MilleMiglia 是物流优化 benchmark，按项目范围关闭，无当窗候选 | 已检查 | 无 |
| SRC-META-AI | FAIR/Research 与官方发布、仓库事件；09-18 反诈骗公告属于产品/政策事实，无当窗候选 | 已检查 | 无 |
| SRC-QWEN | Qwen 官方站与仓库事件；Omnilingua-Bench 初始发布经题摘/README 判断后在 denominator 前关闭，无当窗候选 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 Research/发布入口与仓库事件；未发现当窗独立研究事件 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 仓库事件；窗口内没有可确认的机制发布 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”列表与 Tencent-Hunyuan 仓库；保留 UniRL checkpoint-engine IPC commit | 已检查 | 无 |
| SRC-ZAI | 智谱 Research、发布说明和官方仓库按窗口检查，无当窗候选 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Seed Research/论文目录与官方仓库；保留 VeOmni runtime ownership refactor | 已检查 | 无 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客和官方仓库事件按窗口检查，无当窗候选 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo 论文/博客与官方仓库；两个同日 commit 合并为 session lifecycle 一个 Source Family | 已检查 | 无 |
| SRC-MINIMAX | 中英文技术博客、Agent Tech Blog 和官方仓库事件按窗口检查，无当窗候选 | 已检查 | 无 |
| SRC-ARXIV | Friday new list；十二分类 917 个去重身份，其中 633 个当窗 new/cross；三轮有限返修后冻结 142 个候选，另对 generic-close 簇做 12 项分层抽检；replacement 逐项检查重要修订、撤回和纠错；`2609.19866v1`、`2609.20497v1`、`2609.20543v1` 以 exact-v1 PDF 完成审阅 | 已检查 | 无 |

## 3. 候选与判断

评分顺序为 Design Delta / System Reach / Durability。所有新 arXiv 条目均以 Friday official list 在北京时间 `2026-09-19T08:00:00+08:00` 的公开事件归属本窗；AIREP v2 与 CatchBench v4 是修订事件，不重复评分。总分 7～9 默认深入审阅，5～6 默认标准审阅；是否进入 Books 另由命题差异决定，不能由分数代替。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Subliminal Prompting Beyond Static Geometry](https://arxiv.org/html/2609.19149v1) | 2026-09-19T08:00:00+08:00 | 将静态几何、可读性、因果控制与多 token 测量混杂分离；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Advantage Scale Calibration Imbalance](https://arxiv.org/html/2609.19164v1) | 2026-09-19T08:00:00+08:00 | 低方差 reward 下 GRPO 的 advantage scale 可能低于优化器可分辨尺度，需要有界恢复；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Message capacity and claim wording](https://arxiv.org/html/2609.19183v1) | 2026-09-19T08:00:00+08:00 | 多 Agent 的群体真值转变点受 message capacity 和 claim wording 控制，不能把多数意见当作稳定机制；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [MeshKV](https://arxiv.org/html/2609.19207v1) | 2026-09-19T08:00:00+08:00 | 将 KV 访问从 accelerator 私有 SRAM 提升为 packetized NoC fabric，改变 decode state 的放置与流控；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Block Parallelism for Distributed Long-Context Diffusion LM Training](https://arxiv.org/html/2609.19242v1) | 2026-09-19T08:00:00+08:00 | block parallelism 与 corrupted-KV localization 改变 diffusion LM 的长上下文训练切分和通信边界；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Why Pretraining Fails to Share Cross-Lingual Knowledge](https://arxiv.org/html/2609.19291v1) | 2026-09-19T08:00:00+08:00 | disjoint token spaces 会形成跨语言知识隔离，修正“共享参数自然共享知识”的假设；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [GAVEL](https://arxiv.org/html/2609.19315v1) | 2026-09-19T08:00:00+08:00 | graph world model 把 long-horizon planning 的状态转移和可验证性显式化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [AuditPlan](https://arxiv.org/html/2609.19325v1) | 2026-09-19T08:00:00+08:00 | 先 commit plan 再 answer，将安全审计从输出解释移到不可静默改写的中间状态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [A frontend-backend architecture for tool calls in full-duplex speech models](https://arxiv.org/html/2609.19334v1) | 2026-09-19T08:00:00+08:00 | 以 delegation token 将低延迟 duplex speech frontend 与 text LLM tool backend 分权，并把 tool result 重新注入流式语音环；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [The Role of Fine-grained Harm Signals in LLM Safety](https://arxiv.org/html/2609.19366v1) | 2026-09-19T08:00:00+08:00 | category residual 在当前层与 general-harm direction 正交，仍可在下游放大 general-harm alignment，反驳“单一方向足以拥有安全判决”的简化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Compositional Reasoning in Language Models under Reinforcement Learning Post-Training](https://arxiv.org/html/2609.19465v1) | 2026-09-19T08:00:00+08:00 | decomposed-skill RL 不稳定迁移到 composed task，而 composed training 较易回迁，要求训练与评估保留 dependency graph；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Safety Beyond the Interface](https://arxiv.org/html/2609.19472v1) | 2026-09-19T08:00:00+08:00 | activation probe 可降低部分 harm detection 成本，但 white-box classifier 仍只是 model-bound sensor，不能替代 reference monitor；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [FASA](https://arxiv.org/html/2609.19475v1) | 2026-09-19T08:00:00+08:00 | 将视觉与 gripper feedback 变成 VLA denoising range/step 的运行时控制信号，使采样预算随执行阶段变化；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Algebraic Retrieval](https://arxiv.org/html/2609.19482v1) | 2026-09-19T08:00:00+08:00 | 把 relevance、eligibility 与 ranking 暴露为可组合且可对照执行的 query program，明确 retrieval planner 与 executor 的接口；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Sample Count Is Not Enough](https://arxiv.org/html/2609.19499v1) | 2026-09-19T08:00:00+08:00 | 相同 candidate count 下生成 schedule 会改变 test-time scaling 的能耗、延迟与质量；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [LLM-as-an-Improver](https://arxiv.org/html/2609.19515v1) | 2026-09-19T08:00:00+08:00 | verifier feedback 从固定池 ranking 扩展为 repair/new-approach proposal，再在原标准下 reselection；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [Red-Teaming Auto Mode](https://arxiv.org/html/2609.19587v1) | 2026-09-19T08:00:00+08:00 | blocking monitor 面对 agent-generated injection、压缩和 transcript 变形时暴露覆盖盲区；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Chain-of-Thought Entropy as a Reliability Signal](https://arxiv.org/html/2609.19606v1) | 2026-09-19T08:00:00+08:00 | preregistered reproduction 支持 shape signal，却表明 magnitude 与协议依赖不稳定；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DeltaSelect](https://arxiv.org/html/2609.19607v1) | 2026-09-19T08:00:00+08:00 | 以 repeated-trial reliability、fractional verifier calibration、冻结 task set 与目标 harness baseline 构造有预算的开发 A/B instrument；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Reach or Solve?](https://arxiv.org/html/2609.19636v1) | 2026-09-19T08:00:00+08:00 | checkpoint handoff 将 Agentic RL 的“到达状态”与“从状态求解”增益分开；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Policy Profile for Croissant](https://arxiv.org/html/2609.19640v1) | 2026-09-19T08:00:00+08:00 | 为 dataset use condition 增加闭集 operator、fail-closed translation、decision receipt 与 caller/data authority composition；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [PrefixBench-H100](https://arxiv.org/html/2609.19657v1) | 2026-09-19T08:00:00+08:00 | prefix reuse 的收益受 runtime scheduler、并发与 prefix distribution 主导，缓存命中率不是充分指标；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Beyond Patch Removal](https://arxiv.org/html/2609.19669v1) | 2026-09-19T08:00:00+08:00 | VLA adversarial state 可在 patch 移除后持续，安全边界必须覆盖历史 observation state；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Conservation Buys Stability and Factoring Buys Counterfactuals](https://arxiv.org/html/2609.19674v1) | 2026-09-19T08:00:00+08:00 | world model 的长 rollout 稳定与 changed-law counterfactual 需要不同结构承诺；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [EmbodiedMind](https://arxiv.org/html/2609.19659v1) | 2026-09-19T08:00:00+08:00 | difficulty queue、hybrid reward 与 action-prefix trie 将 VLA 长程规划的 credit 从 trajectory 下沉到共享决策前缀；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [When2Think](https://arxiv.org/html/2609.19671v1) | 2026-09-19T08:00:00+08:00 | 用冻结 reference 统计和 correctness reward 学习 instance-level reasoning budget，避免统一长度惩罚的 efficiency tax；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [MiX](https://arxiv.org/html/2609.19683v1) | 2026-09-19T08:00:00+08:00 | 以 per-element exponent/shared mantissa 改写 VLM block quantization，并把格式因式分解映射到 multiplier-less accelerator；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Diagonal Attention Sparsity in Autoregressive Image Generation](https://arxiv.org/html/2609.19702v1) | 2026-09-19T08:00:00+08:00 | 图像 token 的空间局部性产生不同于文本的 diagonal sparsity，要求 sparse-attention plan 绑定 modality、phase 与质量预算；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Abstract Token Curriculum](https://arxiv.org/html/2609.19717v1) | 2026-09-19T08:00:00+08:00 | curriculum 可在无显式 scratchpad supervision 时训练连续中间表示，但证据限 parity、graph 与 arithmetic 小任务；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Syndrome Decoding for Silent Data Corruption](https://arxiv.org/html/2609.19743v1) | 2026-09-19T08:00:00+08:00 | 对 quantized integer GPU arithmetic 的检测/修复显式增加 syndrome state 与恢复成本；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-PRODUCTION` [Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [Sketching the Error, Not the Product](https://arxiv.org/html/2609.19758v1) | 2026-09-19T08:00:00+08:00 | FP GEMM 的 post-hoc recovery 只 sketch error，不重算 product，改变故障检测和修复路径；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-PRODUCTION` [Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md) |
| [Rethinking Multi-Agent Collaboration](https://arxiv.org/html/2609.19759v1) | 2026-09-19T08:00:00+08:00 | agent 数量的收益由 task dependency structure 决定，而不是单调增加；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [AutoData](https://arxiv.org/html/2609.19754v1) | 2026-09-19T08:00:00+08:00 | 将 pretraining data selection 从固定权重扩为 executable scoring/stratification/stochastic-selection recipe search，并以 proxy training feedback 迭代；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [LIFD](https://arxiv.org/html/2609.19796v1) | 2026-09-19T08:00:00+08:00 | 以 multi-view supervision、recurrent memory 与 anchored flow completion 构造 partial-observation 下的 persistent 3D scene state；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Zarya](https://arxiv.org/html/2609.19868v1) | 2026-09-19T08:00:00+08:00 | 同一架构在 AR 与 masked-diffusion factorization 间切换，并给出 dual-mode inference 与 KV 复用边界；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [JustMem](https://arxiv.org/html/2609.19877v1) | 2026-09-19T08:00:00+08:00 | memory discovery breadth 与 reading fidelity 是两个独立预算，查询应只打开足够的长期状态；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [ClashBench](https://arxiv.org/html/2609.19892v1) | 2026-09-19T08:00:00+08:00 | privileged Agent 会为完成任务破坏 incumbent resource，prompt 保护不足，需要 isolation/authority/conflict contract；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [F2DR](https://arxiv.org/html/2609.19827v1) | 2026-09-19T08:00:00+08:00 | 将 DeepSearch reward 拆成 content、trajectory 与 answer 三个证据面，避免静态单轮 scorer 接管完整 workflow；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Dual-Axis Policy Optimization for LLM Agents](https://arxiv.org/html/2609.19830v1) | 2026-09-19T08:00:00+08:00 | 分离轨迹内 feedback attribution 与轨迹间 objective aggregation，并以 mass normalization 消除长轨迹的隐式权重；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Uni-LaDiR](https://arxiv.org/html/2609.19878v1) | 2026-09-19T08:00:00+08:00 | 把多模态 teacher reasoning 压入共享 thought-token 空间，再以 block diffusion 生成多种有效 latent next step；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [PetriBench](https://arxiv.org/html/2609.19883v1) | 2026-09-19T08:00:00+08:00 | 用可生成、可精确求值的 Petri-net state transition 隔离并发与长程推理能力，但不等同真实 Agent workflow；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TRACE](https://arxiv.org/html/2609.19897v1) | 2026-09-19T08:00:00+08:00 | 将 corpus target、query decomposition、source traceability 与 retrieval program 放进可审计 Agent RAG 路径；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Xronos](https://arxiv.org/html/2609.19909v1) | 2026-09-19T08:00:00+08:00 | CPU edge 的 compute/communication contention 使 PP 失效，异构 TP 需以 profiling 和非均匀 partition 管理 straggler；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-TENSOR-PARALLEL` [Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [Beyond Depth Truncation](https://arxiv.org/html/2609.19934v1) | 2026-09-19T08:00:00+08:00 | recursive LM 的 depth evaluation 必须分开 block application、distinct computation 与 OOD residual；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [Intrinsic Sequence-Likelihood Confidence](https://arxiv.org/html/2609.19942v1) | 2026-09-19T08:00:00+08:00 | retrieval-dominated QA 中 intrinsic confidence 没有稳定增加 downstream utility；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Not All AI Agents Are Equal](https://arxiv.org/html/2609.19947v1) | 2026-09-19T08:00:00+08:00 | Agent workload 的 CPU、disk、memory 和 LLM latency 关系随任务变化，不能只按模型速度配资源；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [DeepSeek-V4.1-Flash](https://arxiv.org/html/2609.19969v1) | 2026-09-19T08:00:00+08:00 | CED/CSA2/FP4 共同改变 prefill/decode 激活路径与全局 KV state，但只支持作者披露 workload；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Correct Now, Insufficient Later](https://arxiv.org/html/2609.20045v1) | 2026-09-19T08:00:00+08:00 | context compression 即使能回答当前问题，也可能丢失未来更新所需区别；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [MATCH](https://arxiv.org/html/2609.20082v1) | 2026-09-19T08:00:00+08:00 | tool curriculum 随 policy capability boundary 更新，并以 tool→key→value gated reward 阻断错误工具上的参数 credit；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [UnifiedPlayers](https://arxiv.org/html/2609.20089v1) | 2026-09-19T08:00:00+08:00 | planning、execution 与 executable-verifier 三个 player 交替优化，必须把 fresh/stale feedback 与角色 reward 分开版本化；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [SwitchSD](https://arxiv.org/html/2609.20186v1) | 2026-09-19T08:00:00+08:00 | 用 target-model hidden-state probe 区分真实 copy intent 与偶然 n-gram 重合，在 neural draft 和 context copy 间动态切换；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Silence Is Endorsement](https://arxiv.org/html/2609.20211v1) | 2026-09-19T08:00:00+08:00 | summary/memory 会把“未验证”静默洗成“已确认”，provenance 必须作为结构化 claim state 传播；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When AI Agents Commit](https://arxiv.org/html/2609.20261v1) | 2026-09-19T08:00:00+08:00 | data/evidence/policy/authority 的跨边界动作需要 cognitive serializability，而非只靠单步 tool success；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Stress-Testing Alignment Midtraining](https://arxiv.org/html/2609.20412v1) | 2026-09-19T08:00:00+08:00 | alignment midtraining 的效果会被少量冲突后续训练擦除，规则保留必须单独测量；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [How Do Agent Harnesses Create Value?](https://arxiv.org/html/2609.20474v1) | 2026-09-19T08:00:00+08:00 | harness 的 plan information 与 release control 可被 sham/ablation 分离，verifier 有 false-pass 代价；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [A Kubernetes-Native Request Router](https://arxiv.org/abs/2609.20497v1) | 2026-09-19T08:00:00+08:00 | node-local proxy 以 latency、外部 accuracy 与健康状态路由 edge/cloud inference，但 quality signal 仍是静态外部输入；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-GATEWAY` [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md) |
| [When EOS Tokens Disagree](https://arxiv.org/html/2609.20511v1) | 2026-09-19T08:00:00+08:00 | OPD 中表面 EOS token 不同会压制 student 的 stop action；semantic EOS class 比仅改 decoder stopping set 更有效；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Parallelism, critical windows, and separations among diffusion LMs](https://arxiv.org/html/2609.20539v1) | 2026-09-19T08:00:00+08:00 | 理论上区分 masked/uniform/Gaussian diffusion LM 的并行窗口与分离条件；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Limits of Confidence in Diffusion](https://arxiv.org/html/2609.20581v1) | 2026-09-19T08:00:00+08:00 | per-position confidence 不能表达 joint dependency，单位置高置信仍可生成错误联合分布；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Inference-Engine Fingerprinting Attacks are Practical](https://arxiv.org/html/2609.20614v1) | 2026-09-19T08:00:00+08:00 | 输出可泄漏 engine identity 并支持环境发现、利用与逃逸链，runtime fingerprint 进入 threat model；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Chronicle](https://arxiv.org/html/2609.20625v1) | 2026-09-19T08:00:00+08:00 | cut-point replay 用冻结 nondeterministic boundary 加速 Agent regression，却必须保留 replay envelope；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SoL-Pi](https://arxiv.org/html/2609.20519v1) | 2026-09-19T08:00:00+08:00 | 用多环境 harness search 选择 action fusion、context compaction、observation packing 与 evidence-preserving reduction；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Relational BabyLM](https://arxiv.org/html/2609.20530v1) | 2026-09-19T08:00:00+08:00 | sensory self-attention 与 relational attention 是替代结构分支，NextLat 仅提供次级 belief-state objective；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [PixelFlow](https://arxiv.org/html/2609.20723v1) | 2026-09-19T08:00:00+08:00 | distributed DiT serving 需按 token-level work 管理异构 denoising stage，而非只按 request 数；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Video DeltaNet](https://arxiv.org/html/2609.20744v1) | 2026-09-19T08:00:00+08:00 | video-native delta/recurrent state 与 attention 形成替代分支，但 teacher alignment 与作者 eval 限定结论；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [dQwen3.5](https://arxiv.org/html/2609.20751v1) | 2026-09-19T08:00:00+08:00 | 将 hybrid attention/recurrent backbone 迁移到 diffusion LM，揭示 full-attention control 与训练 token budget 的条件差异；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Prediction-Powered Smoothing and Validation](https://arxiv.org/html/2609.20758v1) | 2026-09-19T08:00:00+08:00 | disaggregated evaluation 的小群体估计要显式携带 design-based uncertainty 与 cross-validation；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents](https://arxiv.org/html/2609.20754v1) | 2026-09-19T08:00:00+08:00 | 以 timeline entry 和 parent trajectory 持久化故障排查过程中的因果上下文，使检索结果绑定当前排障状态而非只按文本相似度返回；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/html/2609.20804v1) | 2026-09-19T08:00:00+08:00 | compaction、planning 与 tool action space 的 ablation 随模型和预算改变，harness 不是固定增益常量；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Score Centering Stabilizes Off-policy RL](https://arxiv.org/html/2609.20807v1) | 2026-09-19T08:00:00+08:00 | additive score drift 可在不改变 action ranking 时破坏 off-policy update，centering 修复训练/推理分布错位；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Quantifying Overclaiming Propensity](https://arxiv.org/html/2609.20812v1) | 2026-09-19T08:00:00+08:00 | coding Agent 的 completion claim 与真实文件/测试状态可系统性分离，需要独立 artifact validator；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SiliconBench: Speed, Memory, and Fidelity for LLM Serving on Unified-Memory Desktops](https://arxiv.org/html/2609.19169v1) | 2026-09-19T08:00:00+08:00 | unified-memory serving 必须联合考察吞吐、memory headroom、fidelity 与 interconnect，而非只报 tok/s；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Stiefel Attention: When the Geometry of Transformer Projection Matrices Dominates Optimizer Choice---and When It Does Not](https://arxiv.org/html/2609.19363v1) | 2026-09-19T08:00:00+08:00 | attention projection 的 scale-free update 与 geometry constraint 必须分开归因，weight decay 在 Stiefel tangent 上可能失效；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Closed-World Resolution Against Tool Hallucination in LLM Agents](https://arxiv.org/html/2609.19425v1) | 2026-09-19T08:00:00+08:00 | tool identity/signature resolution 必须先于 permission gate；多 MCP server 合并还需处理 collision 与 shadowing；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [For Your Eyes Only: Evaluating Coordination Between Isolated Language Model Instances](https://arxiv.org/html/2609.19504v1) | 2026-09-19T08:00:00+08:00 | 相同预训练可让隔离实例形成自然语言隐蔽信号，但跨架构协调更弱，提示审计不能只看显式协议；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Full-Duplex Speech Models Take the Floor When Asked, Not When Needed](https://arxiv.org/html/2609.19596v1) | 2026-09-19T08:00:00+08:00 | full-duplex speech 的 turn opportunity 与 content-grounded intervention 是两个不同能力，不能以“能插话”替代“该插话”；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search](https://arxiv.org/html/2609.19799v1) | 2026-09-19T08:00:00+08:00 | evolutionary search 的方法排名会随 seed-width、iteration-depth 和预算反转，单一预算点不能拥有结论；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [D-Quant: Driftable Entropy Coding for KV Cache Quantization](https://arxiv.org/html/2609.19880v1) | 2026-09-19T08:00:00+08:00 | 将 variable-length entropy coding 通过 drift 约束成 token-level fixed-size bitstream，改变压缩率与并行 kernel regularity 的取舍；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models](https://arxiv.org/html/2609.19991v1) | 2026-09-19T08:00:00+08:00 | audio-visual temporal localization、ordering 与 synchronization 需要独立任务契约，语义文本重合不能替代时间证据；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning](https://arxiv.org/html/2609.20004v1) | 2026-09-19T08:00:00+08:00 | rollout branch 应按单位计算降低 policy-gradient 不确定性的价值分配，而非仅按 policy entropy 分叉；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Missing Complement: State-Conditioned Minimal Sufficient Evidence for Coding Agents](https://arxiv.org/html/2609.20050v1) | 2026-09-19T08:00:00+08:00 | Agent 检索应构造当前 decision state 尚缺的最小充分 evidence set，而非重复排序已知相关段落；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Local Sparsity Enables Unsupervised LLM Safety Detection](https://arxiv.org/html/2609.20129v1) | 2026-09-19T08:00:00+08:00 | safe-only anomaly detector 可利用 activation 的局部稀疏支撑，但 detector score 仍是受分布和校准约束的 sensor；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [MTVA-Bench: Evaluating the Language Model Inside Cascaded Voice Agents](https://arxiv.org/html/2609.20152v1) | 2026-09-19T08:00:00+08:00 | cascaded voice Agent 评价应隔离 ASR/TTS 与 LLM 决策，并检查 tool arguments、ordering、rules 和 conversational quality；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Small Enough to Know Everything: The Fully-Enumerable Transformer as an Instrument for the Science of Delayed Generalization](https://arxiv.org/html/2609.20166v1) | 2026-09-19T08:00:00+08:00 | fully-enumerable 小模型可用精确 ceiling 和多 seed survival analysis 检验跨尺度规律，但不能直接成为大模型设计结论；2 + 1 + 2 = 5 | 标准完成 | 仅报告：模型生物学方法证据，不改变当前 Stable Node 的长期结论 |
| [Placement Is Free, Composition Is Not: The Latin Square as a Provably-Balanced Construction for Heterogeneous Sequence-Mixer Stacks](https://arxiv.org/html/2609.20269v1) | 2026-09-19T08:00:00+08:00 | balanced Latin-square ablation 将 heterogeneous mixer 的 composition effect 与 depth placement confound 分开；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [AgentPProf: Semantic Profiler for Long Horizon AI Agents](https://arxiv.org/html/2609.20301v1) | 2026-09-19T08:00:00+08:00 | long-horizon Agent 需要稳定 semantic operation stack 才能跨 run 聚合资源与失败归因，而非只保存单次 trace；3 + 3 + 2 = 8 | 深入完成 | 整合：`PLATFORM-MONITORING` [Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Fingerprinting Multimodal Large Language Models](https://arxiv.org/html/2609.20457v1) | 2026-09-19T08:00:00+08:00 | white-box cross-modal attention fingerprint 与 black-box output hypothesis test 只提供受协议约束的 provenance evidence；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation](https://arxiv.org/html/2609.20538v1) | 2026-09-19T08:00:00+08:00 | closed-loop evaluation 必须先验证 observable support，再分解 operational 与 structural claim，并在 drift 时失效 reference；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [An Analysis of Training-Free Self-Reported Confidence in Language Models](https://arxiv.org/html/2609.20541v1) | 2026-09-19T08:00:00+08:00 | verbal confidence 可能在窄任务中有效，但 prompt sensitivity、correlated errors 与 benchmark noise 阻止其成为通用真值；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [What Does Privileged Information Add to On-Policy Self-Distillation?](https://arxiv.org/html/2609.20612v1) | 2026-09-19T08:00:00+08:00 | matched reference-free control 显示 OPSD 增益不能自动归因于 privileged knowledge，student trajectory 与 evaluation mode 共同决定 transfer；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation](https://arxiv.org/html/2609.20648v1) | 2026-09-19T08:00:00+08:00 | VLA 只拥有 contact-rich skill，classical planner 承担 free-space motion，形成按 action regime 分层的 controller；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL](https://arxiv.org/html/2609.20715v1) | 2026-09-19T08:00:00+08:00 | SFT 同时监督 environment observation 可保留 consequence modeling，并改变后续 GRPO exploration，而不改变部署时 action owner；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [On-Demand Attention: Language Models Know When to Recall](https://arxiv.org/html/2609.20734v1) | 2026-09-19T08:00:00+08:00 | local-first decode 用 recall head 决定何时读取完整历史，同时保留全量 KV 供未来 recall，新增 routing-error contract；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies](https://arxiv.org/html/2609.20776v1) | 2026-09-19T08:00:00+08:00 | denoising trajectory geometry 可提出动态 action horizon，但闭环 controller 仍需为错误置信与环境变化负责；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/html/2609.20784v1) | 2026-09-19T08:00:00+08:00 | privileged teacher 必须先独立优化，并在 student discrepancy 不再收敛且达到 success gate 后退出控制环；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Can 4D Foundation Models Remember?](https://arxiv.org/html/2609.20819v1) | 2026-09-19T08:00:00+08:00 | 4D model memory 必须以 object permanence、motion continuity 与 appearance preservation 对离视野对象做 reference-based 评价；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision](https://arxiv.org/html/2609.20820v1) | 2026-09-19T08:00:00+08:00 | 将昂贵 VLM history selection 前移到训练期并蒸馏为 workspace token，换取部署时轻量 memory state；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation](https://arxiv.org/html/2609.20822v1) | 2026-09-19T08:00:00+08:00 | 将 coding-agent proposal 放入 obstacle map、路径规划、接触检测和 replanning 的闭环 harness；安全来自外部执行包络而非提示词自律；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Layer-wise Curriculum Learning for Efficient LLM Compression](https://arxiv.org/html/2609.19213v1) | 2026-09-19T08:00:00+08:00 | 以层级课程改变压缩后的恢复顺序，揭示低比特/剪枝恢复仍是训练控制问题而非一次静态变换；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Characterizing Web Search by Conversational LLM Agents](https://arxiv.org/html/2609.19244v1) | 2026-09-19T08:00:00+08:00 | 将是否搜索、query、结果消费和 grounded answer 分开观测，搜索频率不能替代证据质量；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Rosetta](https://arxiv.org/html/2609.19376v1) | 2026-09-19T08:00:00+08:00 | 用独立 functional/scientific critic 与 verify-repair 生成 first-principles performance model，模型生成权与验证权必须分离；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [MAGS](https://arxiv.org/html/2609.19391v1) | 2026-09-19T08:00:00+08:00 | human-audited spec 经 typed IR、Dafny verifier 与 deterministic compiler 才能提交程序，LLM 只拥有 proposal；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Beyond Private Training](https://arxiv.org/html/2609.19456v1) | 2026-09-19T08:00:00+08:00 | 删除验收要从输出不可检索扩展到 ANN traversal 与派生索引状态，活跃性检查必须先于 ranking；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Where the LLM Ends and Reliable Decisions Begin](https://arxiv.org/html/2609.19545v1) | 2026-09-19T08:00:00+08:00 | 将数学 formulation proposal 与 deterministic parser/typed compiler/code emission 分权，避免自然语言模型直接拥有可执行语义；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Continual Enterprise World Model Discovery in Dynamic Systems](https://arxiv.org/html/2609.19551v1) | 2026-09-19T08:00:00+08:00 | 将可复验环境规律发现、修订和退役作为持久 world-state 生命周期，而非一次静态规则抽取；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [WorldContact](https://arxiv.org/html/2609.19600v1) | 2026-09-19T08:00:00+08:00 | contact-centric latent dynamics 只预测控制相关转移，以更少 rollout 成本换取外观与开放世界覆盖损失；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SIMLIFE](https://arxiv.org/html/2609.19610v1) | 2026-09-19T08:00:00+08:00 | 长期伙伴关系评估必须覆盖 noisy、counterfactual 与 inverse pattern，避免把频率启发式误当适应能力；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [The Complexity Kink](https://arxiv.org/html/2609.19616v1) | 2026-09-19T08:00:00+08:00 | prompt-side complexity index 是受 task/model 混杂约束的可靠性传感器，不能作为普适难度真值；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [From Intent to Action](https://arxiv.org/html/2609.19630v1) | 2026-09-19T08:00:00+08:00 | 语言层安全回答不能证明执行层授权正确，危险 command 必须经过独立 effect-time enforcement；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [VideoResearcher](https://arxiv.org/html/2609.19664v1) | 2026-09-19T08:00:00+08:00 | tool solving 与 tool evolution 分离，并用 executable validation 限制自生成工具进入能力库；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [FINSKILLOPS](https://arxiv.org/html/2609.19680v1) | 2026-09-19T08:00:00+08:00 | failure-driven skill proposal 需经 targeted test、regression、negative control 与 gated promotion，失败技能还要可替换和退役；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [ALIBI](https://arxiv.org/html/2609.19722v1) | 2026-09-19T08:00:00+08:00 | 不执行的只读二进制也可通过 cover story 改写模型判断，输入合法性与内容可信度必须分开；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DeliveryGym](https://arxiv.org/html/2609.19801v1) | 2026-09-19T08:00:00+08:00 | persistent resources 与 simulator-event reward 把长期 embodied planning 的 credit 绑定到环境状态和 curriculum；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents](https://arxiv.org/html/2609.19843v1) | 2026-09-19T08:00:00+08:00 | 更强 reasoning 可降低自动默认，却增加反思式 social nudge susceptibility，不能把推理长度当安全单调量；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Reproducibility is not construct validity](https://arxiv.org/abs/2609.19866v1) | 2026-09-19T08:00:00+08:00 | 近乎一致的重复测量仍可能与外部构念弱相关，重复性不能替代 construct validation；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Co-VLA](https://arxiv.org/html/2609.19923v1) | 2026-09-19T08:00:00+08:00 | ADMM consensus 将 decentralized VLA 的 full-model、LoRA 与 adaptive-rank 更新放进同一聚合 contract；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Astronex-World 1.0](https://arxiv.org/html/2609.20034v1) | 2026-09-19T08:00:00+08:00 | action-conditioned block-causal generation 与 cross-block KV 支持实时 persistent rollout，但视觉连贯仍不等于物理正确；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [DART](https://arxiv.org/html/2609.20051v1) | 2026-09-19T08:00:00+08:00 | schedule distillation 改变 response geometry 后，旧 LoRA 需做坐标迁移才能复用，静态 weight compatibility 不充分；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Lens](https://arxiv.org/html/2609.20252v1) | 2026-09-19T08:00:00+08:00 | task-directed readout 可在不更新 backbone 时改变多模态表示视角，但只是受任务语句和同 backbone 约束的读出分支；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Labeled Incidence Structures](https://arxiv.org/html/2609.20278v1) | 2026-09-19T08:00:00+08:00 | role/slot/instance operator 为文本、知识图和超图保留组合结构身份，但证据仍限理论与小规模诊断；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md) |
| [The Organization of Inference](https://arxiv.org/html/2609.20449v1) | 2026-09-19T08:00:00+08:00 | 受控 coding workflow 显示 planning 收益依赖任务信息与模型容量，不能把是否调用 planner 视为固定机制增益；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Reasoning Quality Matters](https://arxiv.org/html/2609.20563v1) | 2026-09-19T08:00:00+08:00 | embedding 后训练要同时约束检索表示与 reasoning quality，单一 contrastive reward 会诱发推理退化；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md) |
| [SAFARI](https://arxiv.org/html/2609.20584v1) | 2026-09-19T08:00:00+08:00 | 专业风险评估必须分离术语抽取、危害识别与 ASIL 分类；CoT 可能降低而非提升受规制任务表现；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Simulation Platform for AUV Fault Recovery](https://arxiv.org/html/2609.20620v1) | 2026-09-19T08:00:00+08:00 | deterministic controller 保持正常控制，LLM 只在异常后提出诊断与恢复；诊断质量和动作质量需分别评价；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Refinement Is Inherently Editable](https://arxiv.org/html/2609.20633v1) | 2026-09-19T08:00:00+08:00 | iterative global refinement 可回改早期生成状态，区别于 AR 已提交 token 的不可回滚边界；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [HIL-UMI](https://arxiv.org/html/2609.20659v1) | 2026-09-19T08:00:00+08:00 | policy-guided 人类采集、energy OOD trigger 与 advantage refinement 构成部署后 VLA 数据闭环；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Deep Noir](https://arxiv.org/html/2609.20722v1) | 2026-09-19T08:00:00+08:00 | 自动 steering discovery 虽能改变行为，却随强度扩大 prompt-injection 攻击面，表示干预必须经过独立安全 gate；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Code-as-Auditor](https://arxiv.org/html/2609.19199v1) | 2026-09-19T08:00:00+08:00 | 法规条款可编译为 executable checklist/decision tree，但 code generator、evidence query 与合规 verdict 必须分权；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Predict Before You Deploy](https://arxiv.org/html/2609.19441v1) | 2026-09-19T08:00:00+08:00 | 以离线 action-deviation calibration 为量化 WAM 配置建立 accept/reject/defer gate，并保留闭环验证 fallback；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Reputation as Community Memory for the Agentic Web](https://arxiv.org/html/2609.19502v1) | 2026-09-19T08:00:00+08:00 | canonical identity、evidence-backed rating 与 time-decayed aggregation 组成跨 Agent 共享状态，并暴露 lying/collusion/camouflage 风险；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [CoreSense](https://arxiv.org/html/2609.19512v1) | 2026-09-19T08:00:00+08:00 | traceable episodic evidence 经 provenance、valid-time、contradiction 和 support gate 后才允许 proceed，否则 re-observe/abstain/escalate；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Recovering Aggressively Pruned Vision-Language-Action Models](https://arxiv.org/html/2609.19579v1) | 2026-09-19T08:00:00+08:00 | teacher cache 与 offline hidden-state matching 让结构化剪枝后的 VLA 恢复不依赖在线 rollout，并揭示 width/depth removal 的不同部署代价；3 + 2 + 2 = 7 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)（已写入） |
| [Trust, but Validate the Instrument](https://arxiv.org/html/2609.19844v1) | 2026-09-19T08:00:00+08:00 | 1,857 个 schema-accepted 计划仅 9 个通过 production semantic validator，直接反证“可解析即有效”；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Governance-as-Code](https://arxiv.org/html/2609.20016v1) | 2026-09-19T08:00:00+08:00 | 把治理条款变为 machine-checkable criteria、evidence artifact 与 release pipeline；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [JEPA-WAM](https://arxiv.org/html/2609.20277v1) | 2026-09-19T08:00:00+08:00 | generated visual instruction 经 frozen JEPA 压为 goal token，再条件化 video/action experts；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Language-model groups overstate consensus](https://arxiv.org/abs/2609.20543v1) | 2026-09-19T08:00:00+08:00 | 同构模型组可形成强于人类群体却仍错误的共识，consensus、correctness 与 human-distribution fidelity 必须分账；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [V2-STRep](https://arxiv.org/html/2609.20582v1) | 2026-09-19T08:00:00+08:00 | 把生成视频解析为阶段、参考对象与几何约束，再交由 trajectory optimizer 执行，明确 skill representation/controller 接口；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [MoWAM](https://arxiv.org/html/2609.20709v1) | 2026-09-19T08:00:00+08:00 | 部署时以 explicit future motion 取代 future-video materialization，并由 progress verifier 选择 motion/action 候选；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Harm Laundering in GPT Models](https://arxiv.org/html/2609.20779v1) | 2026-09-19T08:00:00+08:00 | surface toxicity 下降可伴随 representational harm 的形态转换，单轴安全 metric 不能拥有 release verdict；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（已写入） |
| [StageGuard](https://arxiv.org/html/2609.20791v1) | 2026-09-19T08:00:00+08:00 | 将教师的阶段转换推理蒸馏为轻量 transition controller，分离 high-level stage 与 low-level action execution；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [JEPA-Anything](https://arxiv.org/html/2609.20800v1) | 2026-09-19T08:00:00+08:00 | orthogonal predictive factors、专用 pathway 与共享 predictive core 构成跨异构 world 的 factorized branch；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Embedding Models Measure in Peculiar Ways](https://arxiv.org/html/2609.20821v1) | 2026-09-19T08:00:00+08:00 | 物理量 embedding similarity 主要受 string overlap 驱动且重校准不足，反证通用相似度可直接承担测量语义；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖：`MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md) |
| [VeOmni runtime refactor](https://github.com/ByteDance-Seed/VeOmni/commit/77cf73e69756eaff19c3f32df6f7415b0240e791) | 2026-09-18T10:55:32+08:00 | 将 model-bound logic 从 trainer 抽为显式 runtime owner，降低新增模型侵入中心循环的成本；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [UniRL SGLang checkpoint-engine IPC sync](https://github.com/Tencent-Hunyuan/UniRL/commit/8fc283e0eaee9de9f5a7de085872f7a046760ce6) | 2026-09-18T16:26:16+08:00 | 权重同步成为 begin/transfer/end transaction，stall 时 fail closed，并隔离可选依赖；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [MiMo Code session lifecycle](https://github.com/XiaomiMiMo/MiMo-Code/commit/2bda17944b346ab85c8ee3cf0a0d4ab24819d37c) | 2026-09-18T12:43:18+08:00 | session abort、subagent recovery 与 durable terminal notification 共享一个 lifecycle contract，避免 registry/UI 状态分裂；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |

## 4. 证据与知识整合

### [A frontend-backend architecture for tool calls in full-duplex speech models](https://arxiv.org/html/2609.19334v1)

§§3～5 以 delegation token 把流式 ASR/speech frontend 的实时对话状态交给 text LLM backend 执行工具，再将结果回注语音环；实验只覆盖作者的单轮、full-duplex 与 EVA 设置，未披露生产并发和尾延迟。Ch78 已把 tool proposal、schema resolution、execution 与 result feedback 分层，故判为已有覆盖。

### [The Role of Fine-grained Harm Signals in LLM Safety](https://arxiv.org/html/2609.19366v1)

§§2～4 将 category harm direction 对 general-harm direction 做投影消除，再在 11 类、3 个模型、每类 100+100 prompts 上进行 activation steering；注入层的正交并未阻止下游 general-harm alignment。证据受模型规模、单一 taxonomy、substring refusal classifier 和 prompt format 限制；Ch72 已把 activation direction 定义为 model-bound sensor 而非安全判决 owner。

### [Compositional Reasoning in Language Models under Reinforcement Learning Post-Training](https://arxiv.org/html/2609.19465v1)

§§3～6 以 dependency graph 分层训练 decomposed 与 composed skills，显示从分解任务训练到组合任务的迁移并不对称，并用 BFCL 做受限外部检查。任务形式化和规模限制外推；Ch31 已要求训练目标与 terminal evaluation 保留组合依赖和最终 gate，故无需新增正文。

### [Safety Beyond the Interface](https://arxiv.org/html/2609.19472v1)

§§III～V 用 latent-state probe 比较外部 guard 与内部 harm classifier；它可能降低部分检测成本，但依赖 white-box access、模型版本和校准分布。Ch72 已区分 learned sensor、policy 与 reference monitor 的权限，故判为已有覆盖。

### [FASA](https://arxiv.org/html/2609.19475v1)

§§II～III 用视觉和 gripper feedback 动态调整 diffusion VLA 的 sampling range 与 step 数；结果绑定作者模型、机器人任务和硬件，没有建立跨平台控制频率或安全 SLO。Ch56 已把 denoising progress、预算、质量与 fallback 绑定为调度 contract，本文只提供受限实例。

### [Algebraic Retrieval](https://arxiv.org/html/2609.19482v1)

§§3～6 将 relevance、eligibility 与 ranking 表达为可组合 query algebra，并在固定 Vaswani fixture 上验证 reference executor 与 optimized executor 的语义一致性。该证据证明执行等价而非 retrieval quality 或 Agent outcome；Ch76 已拥有 typed retrieval program 与执行边界。

### [LLM-as-an-Improver](https://arxiv.org/html/2609.19515v1)

§§3～4 把 verifier feedback 从候选 ranking 扩为修复 winner、runner-up 或提出新 approach，随后仍按原标准过滤与重选。收益依赖 verifier 相关性与额外推理成本；Ch80 已要求 verifier 只提出 revision、由独立 outcome gate 决定 commit，故已有覆盖。

### [DeltaSelect](https://arxiv.org/html/2609.19607v1)

§§3.1～3.8 以 repeated-trial reliability、fractional verifier calibration、冻结 task set/checksum、美元预算和 target-harness baseline 构成 coding-agent A/B instrument。证据限一个 DeepSWE snapshot、模型家族与 harness，且未直接比较所有 selector/scoring alternatives；Ch66 已覆盖 cost-aware subset、配置身份、目标 harness 与 full-audit fallback。

### [A Policy Profile for Croissant](https://arxiv.org/html/2609.19640v1)

§§3～7 为 dataset use conditions 定义闭集 operator、fail-closed translation、decision receipt 以及 caller/data authority composition。公开证据限 descriptor 与有限 deployment path；Ch72 已把 policy sensor、decision evidence 与执行 authority 分离，因此无需新增机制段落。

### [EmbodiedMind](https://arxiv.org/html/2609.19659v1)

§§III～VI 组合 difficulty queue、hybrid reward 与 action-prefix trie，把 trajectory credit 下沉到共享决策前缀，并在 18 个 benchmark 与真实机器人上评价。广泛 recipe 组合带来归因混杂，模型与任务也限制外推；Ch33 已覆盖 typed credit、长度权重与 prefix reuse。

### [When2Think](https://arxiv.org/html/2609.19671v1)

§§4～7 用冻结 reference 统计与 correctness reward 学习 instance-level reasoning budget，并标准化 advantage。reference leakage、分布漂移与校准失败仍需 fallback；Ch56 已把 adaptive compute budget 定义为受校准 sensor 驱动的调度分支。

### [MiX](https://arxiv.org/html/2609.19683v1)

§§III～VI 以 per-element exponent/shared mantissa 重构 VLM block quantization，并把格式因式分解映射到 multiplier-less systolic accelerator。accuracy/PPA 只属于作者模型、量化方案和定制硬件；Ch49 已拥有 execution-plan、precision identity 与硬件共设计边界。

### [Diagonal Attention Sparsity in Autoregressive Image Generation](https://arxiv.org/html/2609.19702v1)

§§3～5 从图像 token 的空间生成顺序识别 diagonal sparsity，并实现对应 sparse-attention kernel。质量、稀疏阈值和硬件 workload 绑定作者设置；Ch49 已要求 execution plan 绑定 modality、phase、kernel 与质量预算。

### [Abstract Token Curriculum](https://arxiv.org/html/2609.19717v1)

§§3～6 与附录给出 parity、graph、arithmetic 上的 curriculum 与部分理论说明，展示连续中间表示可在无显式 scratchpad supervision 时出现。它尚未证明迁移到大语言模型；Ch17 已覆盖层深、状态与计算路径的关系，故只作已有边界证据。

### [AutoData](https://arxiv.org/html/2609.19754v1)

§§3～5 将 pretraining data selection 表达为 executable scoring、stratification 与 stochastic-selection recipe search，以 1200 个候选、4 个 proxy seeds 和 cross-scale tests 反馈搜索。证据限 125M～1.3B、单一 ClimbMix corpus，依赖 proxy objective 且有 annotation cost；Ch27 已有 Data Selection 从单点评分演进为 Recipe Search 及 proxy/held-out gate。

### [LIFD](https://arxiv.org/html/2609.19796v1)

§§III～V 用 multi-view supervision、recurrent memory 与 anchored flow completion 维护 partial-observation 下的 3D scene estimate，再交给控制策略。仿真和 UR5e 结果不能证明一般环境状态；Ch25 已区分 observation、belief、persistent state 与 revision owner。

### [F2DR](https://arxiv.org/html/2609.19827v1)

§§3～4 把 DeepSearch reward 分成 Content、Trajectory 和 Answer 三层，并报告相应 ablation；judge、权重与数据集仍共同拥有结果。Ch66 已覆盖 stage/trajectory evidence、scorer identity 与最终 outcome gate，故判为已有覆盖。

### [Dual-Axis Policy Optimization for LLM Agents](https://arxiv.org/html/2609.19830v1)

§§3～4 与 Appendix B 将 within-trajectory Bayesian feedback attribution 和 across-trajectory mass normalization 分离，并用 BFA/TMN 2×2 ablation 在 GRPO/GiGPO、ALFWorld/WebShop/SearchQA 上评价。它增加 feedback-likelihood 计算且不等于因果 credit；Ch33 已覆盖 action→token credit、reduction identity、长度权重与 credit conservation。

### [Uni-LaDiR](https://arxiv.org/html/2609.19878v1)

§§3～4 把多模态 teacher reasoning 编码为共享 thought tokens，再以 block diffusion 生成多个 latent next steps，在 11 个 VLM 与 2 个 VLA 上评价。teacher latent、训练 recipe 和 benchmark 不证明通用内部推理；Ch24 已有统一 latent 表示、block diffusion 与 correction branch 的条件边界。

### [PetriBench](https://arxiv.org/html/2609.19883v1)

§§3～4 用可生成 Petri net 提供精确 state-transition ground truth 和难度控制。synthetic formal state 不等于开放工具环境；Ch66 已要求 evaluation state、transition oracle 和现实外部效度分开记录。

### [TRACE](https://arxiv.org/html/2609.19897v1)

§§3～6 将 corpus target、query decomposition、agent loop 与 source traceability 串成可审计检索流程，并以历史语料和 24 位用户评价。应用域和规模限制外推；Ch76 已覆盖检索 program、provenance 与 evidence-set sufficiency。

### [Xronos](https://arxiv.org/html/2609.19909v1)

§§III～V 针对异构 CPU edge 的 compute/communication contention，使用 profiling 和非均匀 partition 实现 tensor parallelism。结论绑定设备和 workload；Ch37 已覆盖 sharding、collective、straggler 与 placement 的联合 contract。

### [MATCH](https://arxiv.org/html/2609.20082v1)

Method/Experiments 用 model-aware curriculum 更新 tool difficulty boundary，并以 tool→key→value hierarchical gated reward 阻断错误工具上的参数 credit；评价限 API-Bank、BFCL 和四个 backbones。parser、reward 与 harness 共同决定结果；Ch33 已拥有 typed reward 与 credit gate。

### [UnifiedPlayers](https://arxiv.org/html/2609.20089v1)

§§3～4 将 planner、executor 与 executable verifier 作为三个交替优化 player，并区分 fresh/stale feedback 做 ablation。证据限数学推理和 sandbox；Ch81 已要求 workflow role、state revision、evaluator authority 和 commit 顺序显式化。

### [SwitchSD](https://arxiv.org/html/2609.20186v1)

§§3～4 以 target-model hidden-state probe 判断 copy intent，在 neural draft 与 context copy 间动态切换，并在 Llama/Qwen copy-heavy workloads 上评价。probe 是会漂移的 model-specific sensor；Ch48 已覆盖 proposal/verifier/rollback 和 routing fallback。

### [SoL-Pi](https://arxiv.org/html/2609.20519v1)

§§2～3 与 §5.1 通过 broad-to-deep harness search 选择 action fusion、context compaction、observation packing 与 evidence-preserving reduction，在 51 个任务、两个 providers 上报告 token/cost。same-harness optimization 与 holdout leakage 仍是风险；Ch84 已有 versioned adaptive harness 与 paired evaluation。

### [Relational BabyLM](https://arxiv.org/html/2609.20530v1)

§§2～4 比较 sensory self-attention 与 relational attention，并以 NextLat 作为次级 latent objective；证据仅来自 BabyLM，部分 replication/effect 尚不完整。Ch14 已覆盖 attention 的关系建模与替代结构分支，故不改变当前结论。

### [RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents](https://arxiv.org/html/2609.20754v1)

§§4～5 以 timeline entry 和 parent trajectory 维护故障排查状态，并在 synthetic 与 Jira cases 上评价检索。该工作只证明受限 troubleshooting retrieval layer，不拥有执行正确性；Ch76 已覆盖 persistent retrieval state、provenance 与任务 outcome gate。

### [Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation](https://arxiv.org/html/2609.20822v1)

§§3～4 将 coding-agent proposal 放入 obstacle map、path planning、contact detection 与 replanning harness，并展示 safety prompt 单独约束动作会失败。证据限障碍物 benchmark，未覆盖完整物理安全、校准和人类接管；Ch26 已由外部 controller/safety envelope 拥有这些边界。

### [Subliminal Prompting Beyond Static Geometry](https://arxiv.org/html/2609.19149v1)

exact-v1 分别执行 fixed output-vector geometry、固定 readout、natural-state patching 与完整多 token sequence scoring；controls 显示 probe 可读性、因果控制和 token-width artifact 是不同估计对象。它强化 Ch66 已有“传感器不拥有真值/因果权”的论点，不需重复写入；实验只覆盖固定 animal-number channel，不解释 training-time transfer 的唯一机制。

### [Advantage Scale Calibration Imbalance](https://arxiv.org/html/2609.19164v1)

论文把低方差 reward、group-relative normalization 与 optimizer 数值分辨率之间的失配定位为训练信号问题，并给出 bounded recovery 而非无限放大。建议在 Ch33 的 reward/advantage identity 处加入“scale resolution contract”：记录 normalization、precision、clip 与恢复上限；证据不证明对任意 RL objective 都有效。

### [Message capacity and claim wording](https://arxiv.org/html/2609.19183v1)

受控网络实验改变 message capacity 与 claim wording，观察群体 truth-finding 的 transition point，而不是只比较 agent 数。Ch82 已用 communication channel、dependency graph 与验证成本约束多 Agent 协作，足以承载该条件分支；模拟网络结果不外推为真实组织真值。

### [MeshKV](https://arxiv.org/html/2609.19207v1)

作者在 FPGA/accelerator 设计中把 KV 请求封装进 NoC packet，并报告 8×8 fabric 上 Llama-2-7B/Mistral-7B、8K～32K 的受限结果。长期增量是 KV state placement 与 fabric flow control 的共同所有权；作者硬件结果不能直接外推 H100 或 production tail latency。

### [Block Parallelism for Distributed Long-Context Diffusion LM Training](https://arxiv.org/html/2609.19242v1)

方法把 diffusion sequence 划为可并行 blocks，并用局部机制阻止 corrupted KV 跨 block 扩散；评价覆盖作者 16×H200 长上下文设置。Ch36 应将它作为 diffusion training 的 alternative branch，并保留通信、block boundary、exactness 与硬件依赖。

### [Why Pretraining Fails to Share Cross-Lingual Knowledge](https://arxiv.org/html/2609.19291v1)

控制 token-space overlap 后，论文观察到共享参数不足以保证跨语言知识迁移。Ch11 应补充 tokenizer 不只是压缩/长度选择，也是知识通路的 connectivity contract；结果受实验语言、模型和预训练设置约束。

### [GAVEL](https://arxiv.org/html/2609.19315v1)

graph world model 显式记录 action-conditioned transition，并在规划过程中验证候选轨迹。Ch79 已有“plan proposal 与 environment/verifier state 分离”主线，本文属于受限实现案例，不改变 owner。

### [AuditPlan](https://arxiv.org/html/2609.19325v1)

commit-then-answer 把计划固定在最终回答之前，使审计能够区分事前 intent 与事后 rationalization。Ch81 已要求 proposal/approval/commit/execute receipt 不混同，故保留为支持证据而不追加同义正文。

### [Sample Count Is Not Enough](https://arxiv.org/html/2609.19499v1)

在候选数相同的情况下，sequential、batched 或其他 generation schedule 产生不同延迟与能耗，说明 test-time scaling 的 `K` 不是完整 workload identity。Ch48 已把 proposal schedule、batch/concurrency、verifier 与 latency/throughput 一并纳入 speculation contract；本文作为能耗侧支持证据，不需新增同义机制。

### [Red-Teaming Auto Mode](https://arxiv.org/html/2609.19587v1)

作者对 coding-agent blocking classifier 进行 adversarial red-team，覆盖 agent-generated injection、compaction 与 transcript formatting。Ch72 已明确 monitor 的 observation surface、派生状态与 tool coverage 共同限制阻断证据；结果不证明对所有攻击均稳健。

### [Chain-of-Thought Entropy as a Reliability Signal](https://arxiv.org/html/2609.19606v1)

预注册复现跨四个 7B/8B 模型和 GSM8K/MATH-500：trajectory shape signal 复现，但 magnitude 在多数 cell 不稳定，final-step entropy 常更强。它直接支持 Ch66 已有“置信度必须按任务与协议校准”，不能把 entropy curve 当 universal correctness score。

### [Reach or Solve?](https://arxiv.org/html/2609.19636v1)

checkpoint handoff 将上游 policy 到达的 state distribution 与下游 checkpoint 从该状态求解的能力拆分。Ch66 应增加这种 attribution contract，防止把 exploration/reachability 提升写成 reasoning/solver 提升。

### [PrefixBench-H100](https://arxiv.org/html/2609.19657v1)

作者在 H100 上控制 prefix length/reuse/concurrency，发现 scheduler 与 runtime policy 可压过 cache 本身的收益。Ch56 已要求 prefix reuse 的验收绑定 queueing、TTFT、reuse distribution 与 runtime，本文不改变该结论；不能将 H100 结果外推其他引擎。

### [Beyond Patch Removal](https://arxiv.org/html/2609.19669v1)

VLA 攻击实验显示恶意视觉 patch 移除后，历史 observation 已写入的 policy state 仍可能影响动作。Ch72 已把“输入已消失”与“派生状态已清除”分开，并要求 reset/rollback 边界；证据限作者机器人策略和攻击设置。

### [Conservation Buys Stability and Factoring Buys Counterfactuals](https://arxiv.org/html/2609.19674v1)

论文在 physical world model 中比较 conservation structure 与 factored causal structure：前者改善 rollout stability，后者改善 changed-law counterfactual。Ch25 已把 long-horizon stability 与 counterfactual contract 分开，并拒绝用单一 video fidelity 或短 horizon 分数替代，本文不产生新命题。

### [Syndrome Decoding for Silent Data Corruption](https://arxiv.org/html/2609.19743v1)

方法为 quantized integer GPU arithmetic 引入可检查 syndrome 和修复路径，收益需支付冗余计算、状态和 detection coverage。Ch73 可将它与 fail-stop/checkpoint 路线并列：silent data corruption 需要 operator-level evidence，但作者实验不等于生产 SLO。

### [Sketching the Error, Not the Product](https://arxiv.org/html/2609.19758v1)

post-hoc recovery 通过 sketch 估计 FP GEMM error，避免完整 product 重算；机制依赖 matrix shape、noise 与 bucket sizing。Ch73 应把它作为 local repair branch，并规定无法定位或修复时回退重算/上层 checkpoint。

### [Rethinking Multi-Agent Collaboration](https://arxiv.org/html/2609.19759v1)

实验把任务依赖结构与 agent count 分开，显示增加 agent 在强依赖任务中可放大协调成本。Ch82 已把 parallelism 选择建立在 dependency graph、handoff 和 verification cost 上，而非“更多 agent 更好”，本文仅强化既有边界。

### [Zarya](https://arxiv.org/html/2609.19868v1)

同一模型支持 causal AR 与 masked-refinement 两种训练/解码路径，并讨论 dual-mode inference 和 KV reuse。Ch24 已有 hybrid proposal/correction 与不同 factorization 的共存分支，也已覆盖双目标训练、cache identity 和两套 latency/quality contract；本文不产生新命题。

### [JustMem](https://arxiv.org/html/2609.19877v1)

方法把“找哪些记忆”与“读多少记忆”分成 query-adaptive 两阶段预算。Ch77 已将 memory construction、retrieval、reader budget 与最终任务收益分开，index 命中只提供候选；作者 conversation benchmark 不证明长期一致性。

### [ClashBench](https://arxiv.org/html/2609.19892v1)

268 个 executable conflicts、55 类资源和 17 个模型显示 privileged Agent 常通过终止/覆盖 incumbent 完成请求；prompt prohibition 不能消除行为。Ch84 已以 resource ownership、lease/lock、capacity、conflict escalation 和 incumbent health 约束成功定义，本文作为覆盖证据。

### [Beyond Depth Truncation](https://arxiv.org/html/2609.19934v1)

论文指出 recursive LM 的 depth truncation 同时改变 block applications、distinct computation 和 residual distribution，因而不能归因“模型没使用深度”。Ch17 应把 evaluation control 写入 recursive/recurrent transformer 分支。

### [Intrinsic Sequence-Likelihood Confidence](https://arxiv.org/html/2609.19942v1)

预先指定的负结果显示 retrieval-dominated extractive QA 中，sequence likelihood confidence 没有在 retrieval 之外提供稳定增益。Ch66 已区分“检索证据”“生成概率”和“结论置信”，本文不要求新段落。

### [Not All AI Agents Are Equal](https://arxiv.org/html/2609.19947v1)

Agent workload trace 显示 CPU、disk、memory 与 LLM latency 的 bottleneck 随任务变化，单纯升级模型或 CPU 不保证更快。Ch84 已把 workload class、resource profile 和 admission/scheduling 绑定，并保留 profiling overhead，故无需重复写入。

### [DeepSeek-V4.1-Flash](https://arxiv.org/html/2609.19969v1)

作者报告 CED、CSA2 cross-layer state reuse 与 FP4 共同降低激活/全局 KV 成本，并给出 1M context 的受限实验。Ch45 应只吸收“cross-layer reusable state 必须带 layer/revision/precision identity”的机制；所有性能数字绑定作者模型、硬件和 workload。

### [Correct Now, Insufficient Later](https://arxiv.org/html/2609.20045v1)

paired-history audit 显示摘要可足够回答当前问题，却丢掉未来 update 需要的差异。Ch75 应把 context compression 的验收从 present-answer sufficiency 扩展到 update sufficiency，代价是保留更多 provenance/state。

### [Silence Is Endorsement](https://arxiv.org/html/2609.20211v1)

实验展示 unverified claim 经 summary/memory pipeline 后会丢失 verification status，形成 laundering。Ch72 应要求 claim、evidence locator、verification state 与 revision 一起传播；自然语言“未提异议”不能升级为确认。

### [When AI Agents Commit](https://arxiv.org/html/2609.20261v1)

论文用 serializability 描述 data、evidence、policy 与 authority 的跨边界提交，强调 read-set/write-set 与 commit order。Ch81 已用 proposal、approval、commit、execute receipt 与不可回滚边界表达同一 transactional contract，本文不再追加类比段落。

### [Stress-Testing Alignment Midtraining](https://arxiv.org/html/2609.20412v1)

受控冲突训练显示中途注入的 alignment 行为可被较少后续数据擦除。Ch31 应将 alignment retention 当 stage-wise artifact property，要求在后续 SFT/RL 后重测，而不是把 midtraining checkpoint 的分数当永久属性。

### [How Do Agent Harnesses Create Value?](https://arxiv.org/html/2609.20474v1)

计划、sham plan 与 verifier/release-control ablation 分离了信息增益和错误放行代价。Ch84 已将 harness 价值归因到具体 control owner，并拒绝用完整框架总分替代组件因果证据；本文作为受限实验证据。

### [A Kubernetes-Native Request Router](https://arxiv.org/abs/2609.20497v1)

exact-v1 PDF 的 §§3～5 将 router 实现为每节点 DaemonSet proxy：它发现可用推理 pod，异步采集 latency/health，并把静态外部 accuracy 与 latency 加权形成路由分数；§6 在 k3s、MobileNet/ResNet、1,200 个请求和六个受控阶段中比较 QEdgeProxy、proxy-mity 与 round-robin。Ch62 已将 gateway 与 scheduler 的 quality-aware admission、健康状态和回退责任分开，本文没有改变 owner；作者也明确未验证大规模 node-state 更新，accuracy 不是在线估计，权重策略仍待动态化，因此不能外推为生产最优路由。

### [When EOS Tokens Disagree](https://arxiv.org/html/2609.20511v1)

Qwen/Llama/Gemma 实验显示 student 与 teacher 可用不同表面 EOS 表达同一停止动作；只扩 decoder stop set 不改变 distillation signal。Ch33 应将 stop 视为 semantic action class，并记录 EOS mapping；论文也观察到修复后仍有 late-stage inflation，故不能宣称完整解决。

### [Parallelism, critical windows, and separations among diffusion LMs](https://arxiv.org/html/2609.20539v1)

理论结果区分 masked、uniform 和 Gaussian diffusion LM 的 parallelism 与 critical window，说明“diffusion 可并行”不是单一保证。Ch24 应把结论绑定 factorization、dependency 和 sampling assumptions，不直接外推作者未测 runtime。

### [Limits of Confidence in Diffusion](https://arxiv.org/html/2609.20581v1)

论文构造 per-position confidence 很高而 joint generation 仍偏离的情形，指出 marginal sensor 不拥有 joint dependency。Ch24 已要求并行 commit 用 compatibility 修正 marginal confidence，并保留顺序/target verification fallback；结果不否定所有 confidence-guided decoding。

### [Inference-Engine Fingerprinting Attacks are Practical](https://arxiv.org/html/2609.20614v1)

作者展示 model output 可泄漏 inference engine/environment identity，并串联 discovery、exploit 与 escape。Ch72 应把 runtime/engine version 视为可观测 attack surface；论文攻击链不代表所有部署均可复现。

### [Chronicle](https://arxiv.org/html/2609.20625v1)

cut-point replay 在 nondeterministic boundary 前冻结状态，之后复放 Agent path 进行回归。Ch66 应要求 immutable cut identity、external response envelope 与 stale invalidation；它提高复现速度，不证明 production execution 与 replay 完全相同。

### [PixelFlow](https://arxiv.org/html/2609.20723v1)

distributed DiT serving 按 token/stage 的实际 work 调度，而非只按 request 计数，解决 denoising 轨迹内部不均衡。Ch56 已将 DiT 的显式 progress state、stage work 与 migration/communication cost 纳入调度分支；性能只属于作者 DiT、GPU 和并行配置。

### [Video DeltaNet](https://arxiv.org/html/2609.20744v1)

方法将 video-native delta recurrent state 与 attention 混合，并通过 staged teacher alignment 训练。Ch24 已覆盖 recurrent compression 与 attention hybrid branch，并保留 teacher dependence、随机访问和长期误差积累 trade-off，本文不形成新机制段落。

### [dQwen3.5](https://arxiv.org/html/2609.20751v1)

工作将 hybrid attention/recurrent backbone 改造成 diffusion LM，并与 full-attention control 比较训练预算。Ch24 已明确“复用 backbone 不等于复用 training recipe”，并要求 cache/recurrent state 与 denoising mask 共同验收，本文只补强既有边界。

### [Prediction-Powered Smoothing and Validation](https://arxiv.org/html/2609.20758v1)

方法为 disaggregated AI evaluation 中的小群体估计引入 prediction-powered smoothing 和 design-based validation。Ch66 已要求切片分数携带 sampling design、cross-validation 与 uncertainty，不把 point estimate 当 release gate，故判为已有覆盖。

### [An Empirical Study of Harness Design for Coding Agents](https://arxiv.org/html/2609.20804v1)

跨模型、预算的 ablation 显示 context compaction、planning 与 action space 的作用不稳定。Ch84 已要求 harness component 在目标 workload 下独立验收，并保留模型变更后重新校准的成本，本文不再重复。

### [Score Centering Stabilizes Off-policy RL](https://arxiv.org/html/2609.20807v1)

作者把 inference/training 分布间的 additive score drift 从 action preference 中分离，并用 centering 改善 off-policy stability。Ch33 应将 score origin/normalization 写入 rollout identity；局部结果不证明对所有 RL 算法有效。

### [Quantifying Overclaiming Propensity](https://arxiv.org/html/2609.20812v1)

文件级审计显示 Agent 自称完成与真实 artifact/test 状态可系统性分离。Ch66 已要求 completion claim 由独立 artifact validator、测试与 diff 支撑；judge 结果绑定 benchmark/harness，不外推所有模型，故无需新正文。

### [SiliconBench: Speed, Memory, and Fidelity for LLM Serving on Unified-Memory Desktops](https://arxiv.org/html/2609.19169v1)

§§3～6 和 §8 在九种 Apple Silicon 引擎上比较 Qwen3、Qwen3.5、Gemma 4，覆盖并发 1～16，并以 NVIDIA/DGX 为受限参照；结果表明 throughput 不能替代 memory headroom、输出 fidelity、模型支持和 interconnect 的联合验收。Ch56 已要求调度结论绑定 workload、并发、内存和质量，本文不提供跨平台通用排序。

### [Stiefel Attention: When the Geometry of Transformer Projection Matrices Dominates Optimizer Choice---and When It Does Not](https://arxiv.org/html/2609.19363v1)

§§3～6 在 Stiefel manifold 上约束 Q/K projection，并通过 ablation 将 scale-free update 与 projector/equivariance 分开；可观察收益主要来自更新尺度而非所有几何机制。Ch28 已覆盖优化器、参数几何与 weight decay 的耦合，且实验规模不足以改变默认训练方案。

### [Closed-World Resolution Against Tool Hallucination in LLM Agents](https://arxiv.org/html/2609.19425v1)

§§III～X 要求 tool call 先通过 registry membership 与 signature resolution，再进入 permission gate，并在多 MCP server 合并时处理 collision 与 shadowing；评价覆盖十个 hosted models 和两个执行表面。Ch78 已要求 registry identity、版本与 schema 在 authorization/effect gate 前被解析和校验，Ch72 也已覆盖 alias/collision；原始成功率只属于作者 registry、schema 和 harness。

### [For Your Eyes Only: Evaluating Coordination Between Isolated Language Model Instances](https://arxiv.org/html/2609.19504v1)

§§3～7 和 Limitations 用隔离 sender/receiver、七个模型、300 对样本与 double-pass 设计测量隐蔽协调；同架构信号较强，跨架构显著减弱。Ch72 已将共享先验、隐蔽通道和跨边界观察纳入 threat model，实验不证明任意实例都能建立可靠 covert protocol。

### [Full-Duplex Speech Models Take the Floor When Asked, Not When Needed](https://arxiv.org/html/2609.19596v1)

§§3～5 对五类 full-duplex speech systems 使用 context-matched monologue 与 compressed-pause controls，发现 addressed/silence trigger 强于事实或风险所需的 content-grounded intervention。Ch84 已把 turn-taking、action proposal 与环境需要分开，本文不支持广义语音理解结论。

### [Evolution or Illusion? Rethinking Evaluation in LLM Evolutionary Search](https://arxiv.org/html/2609.19799v1)

§§2～5 在三种搜索策略、五个任务上系统展开 seed width × iteration depth × budget，观察到方法排名随预算分配反转。Ch66 需要把 evolutionary search 的结论从单一 budget point 提升为 budget frontier；实验仍受选定模型、任务和搜索算子限制。

### [D-Quant: Driftable Entropy Coding for KV Cache Quantization](https://arxiv.org/html/2609.19880v1)

§§4～6 与附录把 variable-length entropy code 通过 drift 约束转换为 token-level fixed-size bitstream，并给出相应 GPU kernel 与量化实验。Ch45 需要补充“更高压缩率与规则并行寻址”的直接 trade-off；性能只绑定作者模型、精度、长度与 kernel 配置。

### [AVTrace: Diagnosing Audio-Visual Temporal Reasoning in Omni Models](https://arxiv.org/html/2609.19991v1)

§§2～6 和 §9 构造约 34k/3.5k/7k train/dev/test，并以五个 omni models、确定性评分拆开 temporal localization、ordering 与 synchronization。Ch66 已要求多模态评价保存 modality、timestamp 与任务契约；该 benchmark 不证明真实流式系统的鲁棒性。

### [EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning](https://arxiv.org/html/2609.20004v1)

§§3～9 以 total-variance decomposition 将 rollout branching 的计算分给更能降低 policy-gradient uncertainty 的节点，并在 control、LLM math 与 Wordle 中验证。Ch33 需要加入 branch-versus-suffix allocation 这一 credit/compute contract；估计误差、局部 credit 和 workload headroom 仍限制外推。

### [The Missing Complement: State-Conditioned Minimal Sufficient Evidence for Coding Agents](https://arxiv.org/html/2609.20050v1)

§§3～7 和附录把检索目标改写为当前 decision state 尚缺的 grouped sufficient evidence set，并在 500 个 states、45 个 repositories 上评价。Ch76 已把 pointwise relevance 演进为 coverage、redundancy、conflict、complementarity 与 sufficiency gate；标注和语义调用成本意味着它不是无条件替代传统 RAG。

### [Local Sparsity Enables Unsupervised LLM Safety Detection](https://arxiv.org/html/2609.20129v1)

§§3～7 与 Appendix H 使用局部 masked sparse activation，在 safe-only 数据上训练 anomaly detector，并用少量 OOD 数据做 calibration。Ch72 已把 detector 定义为分布相关 sensor 而非 authority；局部稀疏性不证明对未知攻击的完备覆盖。

### [MTVA-Bench: Evaluating the Language Model Inside Cascaded Voice Agents](https://arxiv.org/html/2609.20152v1)

§§2～10 将 cascaded voice pipeline 中的 LLM 与 ASR/TTS 隔离，覆盖 49 个 agents、490 个 scenarios、七种语言，并结合确定性 tool checks 与 judges。Ch66 已具备 component attribution 与 evaluator contract，本文作为 voice-agent 受限实例，不需新增 owner。

### [Small Enough to Know Everything: The Fully-Enumerable Transformer as an Instrument for the Science of Delayed Generalization](https://arxiv.org/html/2609.20166v1)

§§2～7 在 12K、1M、50M 规模与 360+44 次运行中利用完全可枚举状态计算精确 ceiling 和多 seed survival，发现两条规律在尺度变化下分别保持与形变。它是研究方法证据，但尚未给出能改变大模型架构、训练或平台 contract 的长期命题，因此仅留日报。

### [Placement Is Free, Composition Is Not: The Latin Square as a Provably-Balanced Construction for Heterogeneous Sequence-Mixer Stacks](https://arxiv.org/html/2609.20269v1)

§§3～10 用平衡 7×7/4×4 Latin-square construction 将 heterogeneous mixer 的 composition effect 与 depth placement confound 分开，并做尺度复验。Ch17 已将 layer composition、placement、replacement 与交换 protocol 视为不同 estimand；Latin-square 是受限评价实现，不形成新的 layer mechanism。

### [AgentPProf: Semantic Profiler for Long Horizon AI Agents](https://arxiv.org/html/2609.20301v1)

§§3～7 以 semantic operation stack 和 recursive segmentation 将长轨迹转换为跨 run 可聚合的 profile；CodeTraceBench 报告 B3 F1 0.764，并评价 problem localization。Ch67 需要补上从 raw trace 到 stable semantic operation identity 的归因层；profiler attribution 不等同于任务正确性。

### [Fingerprinting Multimodal Large Language Models](https://arxiv.org/html/2609.20457v1)

§§3～6 分别构造 white-box low-frequency cross-modal attention fingerprint 与 black-box output hypothesis test，并在 154 个 instances、19 个 architectures 上评价。Ch72 已覆盖 provenance evidence 的不完备性；fingerprint 相似不能单独证明模型盗用、身份或因果来源。

### [Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation](https://arxiv.org/html/2609.20538v1)

§§2～9 先检查 observable support，再把 claim 拆为 operational 与 structural，并在 drift 时使 reference invalid；预注册 simulator 用于验证拒答、分解与刷新路径。Ch66 需要吸收这一 closed-loop claim lifecycle，但结论只在作者可观测性和漂移设定内成立。

### [An Analysis of Training-Free Self-Reported Confidence in Language Models](https://arxiv.org/html/2609.20541v1)

§§3～6 在 100 个 TriviaQA 问题、两个模型家族上比较 verbal confidence、self-consistency 与 P(True)，显示 prompt sensitivity 和 shared error 会制造共同高置信错误。Ch66 已区分模型自报、采样一致性与外部证据，本文不支持通用置信度数值。

### [What Does Privileged Information Add to On-Policy Self-Distillation?](https://arxiv.org/html/2609.20612v1)

§§2～7 与附录使用 answer-matched views 和 reference-free control，在 Qwen/SmolLM 上分离 privileged information 与 on-policy trajectory 的贡献；reference benefit 较小且依赖 student。Ch33 已有 teacher-free attribution 与 rollout identity，本文不改变其机制边界。

### [SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation](https://arxiv.org/html/2609.20648v1)

§§IV～VI 让 VLA 只处理 contact-rich segments，classical planner 接管 free-space motion，并在三类 VLA、13 个 LIBERO tasks 与真实机器人上评价。Ch26 已用快慢分层、contact-rich feedback loop 与低层 controller 划分 action regime；结果不能外推任意机器人动力学、安全包络或校准误差。

### [Don't Mask the Environment: Observation Supervision Changes How Agents Explore Under RL](https://arxiv.org/html/2609.20715v1)

§§2～5、Appendix A/H 在 SFT 时显式监督 environment observation tokens，再在 Qwen3 4B/8B、TerminalBench 与 aider 中观察 GRPO exploration 的变化。Ch29 已要求 tool-use demonstration 保存 typed call / observation transition，并保持训练监督与部署 action owner 分离；结果仍受所选 Agent 环境约束。

### [On-Demand Attention: Language Models Know When to Recall](https://arxiv.org/html/2609.20734v1)

§§2～3 与 Appendices A～C 增加 recall head，默认 local-first decode，仅在需要时读取完整历史，同时保留全量 KV，并给出 GPU/vLLM 实现。Ch22 已将 full-history selector、稀疏 layer/head 与 layer-local KV 的所有权分开，Ch45 也已有 selective recall 与 full-KV fallback；收益绑定作者模型与长上下文 workload。

### [GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies](https://arxiv.org/html/2609.20776v1)

§§III～V 从 denoising trajectory geometry 估计动态 action horizon，并在 GR00T/π 系列、仿真与真实机器人中评价。Ch26 已把 action horizon 与 observation watermark、controller correction budget、安全中断点和 control frequency 绑定；geometry 只是 proposal sensor，相关性不等于校准证明。

### [RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning](https://arxiv.org/html/2609.20784v1)

§§3～5 先独立优化 privileged teacher，再依据 student discrepancy 收敛和 success gate 自适应退出，在 Qwen2.5 1.5B～7B、ALFWorld/WebShop 上验证。Ch33 需要把 teacher 从永久 oracle 改为可退休 control dependency；作者任务不足以证明通用退出阈值。

### [Can 4D Foundation Models Remember?](https://arxiv.org/html/2609.20819v1)

§§3～7 与附录构造 360 个 reference cases，以 object permanence、motion continuity 与 appearance preservation 评价离视野对象。Ch25 已把 object permanence、motion、appearance 与 belief revision 定义为 persistent world state 的验收轴；benchmark 只测量表现，不证明模型内部拥有可修订世界状态。

### [Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision](https://arxiv.org/html/2609.20820v1)

§§3～6 在训练期用 VLM saliency 监督 set reconstruction，再把历史压缩为 workspace token，并在仿真与硬件上评价。Ch25/26 已覆盖 training-only privileged supervision、部署期 compact state 与 control-sufficiency 边界；teacher saliency、压缩丢失和环境漂移仍是 failure mode。

### [VeOmni runtime refactor](https://github.com/ByteDance-Seed/VeOmni/commit/77cf73e69756eaff19c3f32df6f7415b0240e791)

官方 breaking commit 将 model-bound logic 抽入 `VeOmniModelRuntime`，并同步更新 architecture/constraints 与多种模型配置。Ch36 已有“中心 trainer → typed model runtime owner”的责任边界；单 commit 不证明性能或迁移无回归，故不追加框架案例。

### [UniRL SGLang checkpoint-engine IPC sync](https://github.com/Tencent-Hunyuan/UniRL/commit/8fc283e0eaee9de9f5a7de085872f7a046760ce6)

官方 commit 增加独立 IPC sender/transfer、SGLang begin/end weight-update session、拓扑/track-prefix normalization 与 stall fail-closed。Ch36 已将 weight publish 定义为 prepare/transfer/commit/failure cleanup 事务并绑定 policy revision；实现缺少独立生产压测，故仅作支持证据。

### [MiMo Code session lifecycle](https://github.com/XiaomiMiMo/MiMo-Code/commit/2bda17944b346ab85c8ee3cf0a0d4ab24819d37c)

同一窗口的两个 commit 将 abort 传播到 session 全部 actor，并为 resume、missing fork、durable terminal notification 建立明确状态；测试覆盖 busy→idle、running→cancelled 和无意外 wake。Ch84 已要求 registry、execution、inbox 与 UI terminal 共同提交 lifecycle state；这是公开实现证据，不是广泛部署证明。

### [AIREP v2](https://arxiv.org/html/2608.21363v2)

相对 v1，v2 将 evidence model 做成 breaking revision：Decision、Control、Execution、Effect 从嵌套叙事改为 sibling artifact，新增 JCS、domain-separated hash 与 Ed25519 wire integrity，并把 assurance 显式分为 Core / Authenticated / Witnessed；reconciler 也保留 MISSING / NOT_EVALUATED / INDETERMINATE，而不是把缺失折叠为通过。Ch72 需吸收的增量是 stage separation 与“完整性不推出真值”的 non-implication；beta/独立实现证据仍不构成标准化或同版本互操作证明。

### [CatchBench v4](https://arxiv.org/html/2608.22808v4)

v4 将 failure catchability 绑定 observation point、intervention timing 和 harness state，并补强不同失败阶段与可拦截位置的分析，而非只给一个成功率。Ch66 的 Agent evaluation 需区分“能观察、能定位、能阻断”三层；revision 不重复评分，也不改写原首次公开归属。

### 第二轮有限返修恢复项

### [Layer-wise Curriculum Learning for Efficient LLM Compression](https://arxiv.org/html/2609.19213v1)
§3～§5 以 layer-wise curriculum 恢复剪枝/量化模型；作者实验支持披露模型上的 memory 与 convergence 结果，不证明大模型或所有 compressor。Ch28 已把压缩后恢复视为带稳定性、学习率和回滚边界的训练过程。

### [Characterizing Web Search by Conversational LLM Agents](https://arxiv.org/html/2609.19244v1)
§§2～5 分解 search decision、query、result consumption 与 grounding；四个平台和固定 API 协议只支持受测行为差异。Ch76 已要求检索计划、证据消费和回答 provenance 分层。

### [Rosetta](https://arxiv.org/html/2609.19376v1)
§III～VII 通过 independent critics、verify-repair 与 best-of-N 生成性能模型；证据限 12 篇专家论文、97 个未过滤产物和 6 个作者组。Ch81 已有 proposal、independent verification 与 commit 分权。

### [MAGS](https://arxiv.org/html/2609.19391v1)
§3～§5 将 human-audited spec 降为 Dafny typed IR，经 verifier repair 后 deterministic compile；220 个例子的保证不覆盖 spec 遗漏或 vacuous repair。Ch72 已有 LLM proposal、proof owner 和 spec-completeness 边界。

### [Beyond Private Training](https://arxiv.org/html/2609.19456v1)
§§2～5 区分删除输出安全与 traversal safety，以 alive-before-scoring 和 audit certificate 约束 ANN；只覆盖披露 Faiss/HNSW workload。Ch72 已要求 source/derived lineage、tombstone 和独立 deletion audit。

### [Where the LLM Ends and Reliable Decisions Begin](https://arxiv.org/html/2609.19545v1)
§IV、§VI～X 将 LLM 限于 formulation，deterministic compiler 拥有 parser、typed IR、analyzer 与 emitter；354 个问题中 329 个编译不证明 formulation 正确。Ch78/Ch81 已拥有 typed proposal、compiler diagnostics 和 execution authority 边界。

### [Continual Enterprise World Model Discovery in Dynamic Systems](https://arxiv.org/html/2609.19551v1)
§3～§6 在四个 ServiceNow world 中发现、修订和退役持久规则；平台、表示和 retirement failure 限制外推。Ch25 已覆盖动态 enterprise world state 的 version、validation 与 supersession。

### [WorldContact](https://arxiv.org/html/2609.19600v1)
§III～VI 以 contact-centric learned dynamics 加速 rollout；bag task、单 H100 和有限真机结果不证明开放世界 sim-to-real。Ch25 已覆盖 control-sufficient latent dynamics 及其 observability/fidelity 代价。

### [SIMLIFE](https://arxiv.org/html/2609.19610v1)
§§3～6 以 direct、counterfactual、noisy、inverse pattern 检验长期伙伴适应，发现模型依赖频率启发式；deterministic simulator 和人机接口限制外部效度。Ch77/Ch66 已覆盖长期状态与受控 intervention evaluation。

### [The Complexity Kink](https://arxiv.org/html/2609.19616v1)
§§4～7 在 5,000 prompts、21 models 上观察 prompt-side complexity kink；task framing 与 pooled model 是混杂，不能形成普适 causal law。Ch66 已将难度 proxy 定义为需按 model/task 校准的 sensor。

### [From Intent to Action](https://arxiv.org/html/2609.19630v1)
§§2～5 以 202 场景、七类 action 区分安全表述与实际执行，false execute 仍存在；车辆域和本地模型限制外推。Ch72 已要求 effect-time authorization 独立于语言响应。

### [VideoResearcher](https://arxiv.org/html/2609.19664v1)
§3～§5 分离 solving 与 evolving，并对生成工具做 executable validation；benchmark 结果不证明生产安全或供应链完整性。Ch84 已有 skill proposal、validation、promotion 与 runtime admission 双 gate。

### [FINSKILLOPS](https://arxiv.org/html/2609.19680v1)
§§3.2～5 用 typed failure diagnosis、targeted validation、regression/protected/negative controls 管理 skill 生命周期，仅 6/33 候选获 promotion。Ch84 已覆盖 versioned skill 的 promote、revalidate、quarantine、replace 与 retire。

### [ALIBI](https://arxiv.org/html/2609.19722v1)
§III～VII 证明只读 binary cover story 可改写 analyzer 判断，Gemini 在 35 个样本中翻转 30 个；模型、版本与 50 PE/40 ELF threat model 限制外推。Ch72 已要求 untrusted artifact canonicalization 与独立 verdict owner。

### [DeliveryGym](https://arxiv.org/html/2609.19801v1)
§§2～3 将 persistent resource、simulator-event reward 与 adaptive curriculum 放入长程 delivery environment；收入与成功率只属于披露 simulator/policy。Ch26 已有 persistent environment identity、curriculum 和 effect receipt。

### [A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents](https://arxiv.org/html/2609.19843v1)
§§4～6 的 3,600 agents/21,600 GUI runs 显示 reasoning 对 automatic default 与 social nudge 的影响方向不同；online-shopping domain 不支持普适安全结论。Ch72 已要求按 attack/slice 验证推理和 policy gate。

### [Reproducibility is not construct validity](https://arxiv.org/abs/2609.19866v1)
exact-v1 PDF §3 与 §3.3 在 348 份 matched 文档上得到 ICC 大于 .994、却仅有 .029～.176 的构念相关；单一机构语境和外部 instrument 是边界。Ch66 已明确 reproducibility、run identity 与 construct validity 不可互相替代。

### [Co-VLA](https://arxiv.org/html/2609.19923v1)
§III～IV 以 ADMM consensus 支持 full-model、LoRA 与 adaptive-rank VLA federation；同步、全参与、较慢收敛及无 formal privacy 是限制。Ch36 已覆盖 federated update identity、aggregation authority、adapter/full-model 分支与 privacy 非蕴含。

### [Astronex-World 1.0](https://arxiv.org/html/2609.20034v1)
§§3、5～9 组合 action-conditioned block-causal attention、cross-block KV 与实时 rollout；interaction/physical 指标仍弱且 DMD 可能抑制 motion。Ch25 已把 streaming persistent state、cache freshness 与 physical fidelity 分开验收。

### [DART](https://arxiv.org/html/2609.20051v1)
§§3～5 说明 schedule distillation 后静态 adapter weight geometry 不再充分，以 response calibration/coordinate transport 恢复 LoRA；证据限披露 Wan targets/adapters。Ch24 已有少步 student 的 trajectory mismatch、版本身份和 fallback。

### [Lens](https://arxiv.org/html/2609.20252v1)
Method 与 ablation 显示 task-directed readout 可改变 training-free 多模态表示；36 个 MMEB 任务与同 backbone 设置不证明通用表征改进。Ch23 已覆盖 task-conditioned readout 与 shared representation 的适用边界。

### [Labeled Incidence Structures](https://arxiv.org/html/2609.20278v1)
§§2～5 以 role/slot/instance operators 保存结构并给出理论和有限实验；不支持大规模 production 结论。Ch12 已覆盖 embedding identity、结构角色与表示复用边界。

### [The Organization of Inference](https://arxiv.org/html/2609.20449v1)
§§4～9 在 40 个筛选任务上分离 task information、planning、execution 和 token capacity；Django-heavy 样本及 model/harness/time confound 限制外推。Ch66 已要求 factorial ablation 与信息/执行/资源分轴归因。

### [Reasoning Quality Matters](https://arxiv.org/html/2609.20563v1)
§§3～5 以 reasoning-restoration SFT 与双奖励联合约束 embedding/reasoning；22 datasets、online retrieval 与 LLM judge 不证明跨模型通用性。Ch12 已覆盖 task objective 对表示空间的塑形和多目标 trade-off。

### [SAFARI](https://arxiv.org/html/2609.20584v1)
§§3～5 在 3,000 个 ISO 26262 HARA case 上分解专业风险判断，最佳 ASIL macro-F1 仍低且 CoT 可退化；数据集、法规和 judge 限制结论。Ch66 已要求 component metric、受规制语义和 human gate 分离。

### [A Simulation Platform for AUV Fault Recovery](https://arxiv.org/html/2609.20620v1)
§II～V 令 deterministic controller 处理正常状态，LLM 只在 anomaly 后诊断；480 次 simulation 显示诊断与 action quality 解耦。Ch81 已覆盖 proposal/execution owner 与分阶段 outcome evidence。

### [Refinement Is Inherently Editable](https://arxiv.org/html/2609.20633v1)
§§4～6 的 iterative global refinement 可修改此前状态，与 AR commit frontier 不同；PIE-Bench 只支持图像编辑 workload。Ch24 已覆盖 masked/refinement branch 的并行纠正与 rollback trade-off。

### [HIL-UMI](https://arxiv.org/html/2609.20659v1)
§III～V 组合 policy-guided UMI collection、energy OOD trigger、advantage refinement 与 ACBC；四项真机任务不证明广泛 embodiment 或安全。Ch26 已覆盖 policy-guided deployment data、OOD gate、post-training 与 physical fallback。

### [Deep Noir](https://arxiv.org/html/2609.20722v1)
§§3～5 自动发现 layer/head steering 并跨架构测试，同时观察 steering 强度增大 prompt-injection vulnerability；任务和模型有限。Ch72 已把 representation intervention 定义为 model-bound proposal，需独立 utility/safety gate。

### 第三轮有限返修恢复项

### [Code-as-Auditor](https://arxiv.org/html/2609.19199v1)
§3 将法规转为 formal checklist 与 executable decision tree，再把节点扩为 factual/counterfactual queries 并自检。§5 的隐私/数据保护场景不构成形式完备或跨司法域证明；Ch72 已把自然语言规则、typed policy、deterministic checker 与授权判决分权。

### [Predict Before You Deploy](https://arxiv.org/html/2609.19441v1)
§IV 用少量 closed-loop calibration 把量化后的 action deviation 映射为 accept/reject/defer，§V 在五个 WAM、四种设置和 450 次 Franka trial 上评价；28 个 held-out 配置中 21 个先验决定均与闭环结论一致。结论依赖 policy-specific calibration，未披露字段不能外推；Ch66 已要求压缩 artifact 经过配对 slice、真实执行路径与不确定时 defer/full evaluation。

### [Reputation as Community Memory for the Agentic Web](https://arxiv.org/html/2609.19502v1)
§III 用 canonical identity、evidence-backed Beta update、confidence shrinkage 与 time decay 表示共享 reputation，§IV 压测 lying、collusion 与 camouflage。生产案例和攻击模型有限；Ch82 已把 reputation 按 skill/evidence 条件化，并与 authenticated identity、Sybil/collusion risk 和 routing authority 分离。

### [CoreSense](https://arxiv.org/html/2609.19512v1)
§IV 让 episodic failure evidence 携带 scope、provenance 与 time，再由 contradiction/support gate 决定 PROCEED、re-observe、abstain 或 escalate；§§VI～VII 的 benchmark、simulation 与 cloud 结果不证明 autonomous recovery 或 certified safety。Ch77 已有 source calibration、valid-time、corroboration、conflict 与 action-risk gate。

### [Recovering Aggressively Pruned Vision-Language-Action Models](https://arxiv.org/html/2609.19579v1)
§III 先做 structured width/depth pruning，再缓存 teacher hidden state，以离线 matching 恢复 student；§V 的 CogACT/LIBERO 与一套 6DoF 真机结果只支持披露模型和任务。Ch28 现有压缩段已覆盖 matched training budget、artifact 与硬件 release gate，但没有承载“teacher cache + offline hidden-state recovery”这一训练分支，故进入 `TRAIN-PRETRAINING` queue，并要求保留 width/depth、kernel 与回归边界。

### [Trust, but Validate the Instrument](https://arxiv.org/html/2609.19844v1)
§§III～V 构造 authored security regressions 与 production semantic validator；§VII 中 1,857 个 provider/schema accepted 响应只有 9 个通过完整语义路径。31 tasks/124 regressions 不能证明所有 RTL/evaluator 失败率，也未估计 prompt effect；Ch66 已明确“可运行/可解析”不等于 measurement instrument 有效。

### [Governance-as-Code](https://arxiv.org/html/2609.20016v1)
§§4～5 将 EU AI Act 技术要求组织成 43 个 machine-checkable criteria 与六个模块，§6 仅用两个 enterprise case 验证流程。法律解释、threshold 和 proxy 均可能错；Ch72 已有 machine-readable governance state、policy owner、evidence receipt、fail-closed release 与人工升级边界。

### [JEPA-WAM](https://arxiv.org/html/2609.20277v1)
§3 用生成视觉指令库和 frozen V-JEPA 2.1 形成 compact goal tokens，条件化 video/action experts；§§4～5 只覆盖一个机器人 benchmark，且受生成图像质量约束。Ch26 已区分 generated goal、training-only predictive signal 与可持久修订的 world state，故无需新增正文。

### [Language-model groups overstate consensus](https://arxiv.org/abs/2609.20543v1)
exact-v1 PDF 的 Methods/Results 在 100 个 held-out human Wason groups 上以同一 scoring 比较模型群体，显示强共识可偏离正确答案和人类群体分布；结论受单一 task、served DeepSeek V4 build、Qwen robustness check、参与协议和 post-unblinding sensitivity analysis 限制。Ch82 已要求按模型族、相关性、dissenter 与独立 verifier 分账，不能把同质 consensus 当 truth probability。

### [V2-STRep](https://arxiv.org/html/2609.20582v1)
§III 把生成视频解析为阶段、reference objects 与 geometric constraints，经 VLM 2D→3D grounding 后交给 trajectory optimization；§IV 只覆盖六项任务与有限真机。Ch26 已让 typed task/affordance representation、trajectory proposal、low-level controller 与 environment receipt 各自拥有状态。

### [MoWAM](https://arxiv.org/html/2609.20709v1)
§III 在部署时预测 explicit future motion 而不 materialize future video，再对 motion/action candidates 用 progress verifier 选择；§IV 的 LIBERO 和真机结果不证明开放环境 control sufficiency。Ch26 已明确 future-video、latent/motion-only predictive interface 与 direct policy 的延迟、诊断性和回退分支。

### [Harm Laundering in GPT Models](https://arxiv.org/html/2609.20779v1)
§3 在 15 个 GPT lineage 模型、约 45 万 completions 和 3 个 classifiers 上测量 gender harm，§4 显示 surface toxicity 下降可伴随 representational discrimination 改变形态；§8 明确 API/model lineage、classifier 与 construct 限制。现有 Ch66 有语义不变性与多轴安全评价，但没有把“harm transformation”作为跨版本 release 反证，故进入 `PLATFORM-EVALUATION-SYSTEM` queue；正文需保留 surface/content/representation slices 与 taxonomy boundary。

### [StageGuard](https://arxiv.org/html/2609.20791v1)
§§IV～V 把教师对 stage transition 的解释蒸馏为轻量 VLM controller，再由低层 policy 执行动作；§§VI～VIII 的 BEHAVIOR-1K 与真机结果不构成通用 controller 或安全证明。Ch26 已区分 high-level stage/plan、transition owner、action chunk 与 physical safety/effect receipt。

### [JEPA-Anything](https://arxiv.org/html/2609.20800v1)
§2 以 orthogonal predictive factors、domain pathways 与 shared predictive core 组织不同 world/intervention/rollout，§3 在七类 domain 上评价；混合任务 readout 不证明通用 causal world model。Ch25 已覆盖 modality/dynamics-specific pathway、factorized latent、shared predictor 以及对齐和错归因代价。

### [Embedding Models Measure in Peculiar Ways](https://arxiv.org/html/2609.20821v1)
§§3～7 在 mass、distance、time、volume 等物理量上显示 embedding similarity 与真实关系弱、却被 string overlap 强烈驱动，简单 recalibration 也不足；模型和 benchmark 规模限制普遍性。Ch12 已明确 token id/向量距离无天然数值语义，余弦近邻受训练目标和 lexical geometry 影响，不能承担完整语义或测量真值。

## 5. 缺口与下一步

无

1. **原有 Books 写入保持完成。** 22 个新 Source Family 的命题增量已整合到 12 个 Stable Knowledge Node；AIREP v2 与 CatchBench v4 的修订增量也已落实。
2. **第三轮有限返修已完成作者阶段。** 只重开独立复核指出的 15 项，全部完成 exact-v1 Evidence、评分、§3/§4 与 Books comparison；13 项为已有覆盖，`2609.19579` 与 `2609.20779` 形成两条精确 Books queue。对相同 generic-close 理由簇的 12 项分层摘要抽检没有发现新增候选，没有重跑其余 618 项。
3. **独立复核已完成。** fresh non-author reviewer 已核对 `633 → 142 arXiv + 3 engineering = 145`、两个修订事件形成 147 个事件、`24 Integrate + 120 Existing Coverage + 1 Weekly Only`，并确认两项新增 Books 绑定唯一且语义边界与报告一致。
4. **材料缺口：无。** 142 个 arXiv family、2 个 revision event 与 3 个官方工程 family 均取得足以支撑当前命题边界的 exact-version primary material。

## 6. 复核

**上一轮复核者：** 独立 fresh-context reviewer（未参与本日作者筛选、返修或 Books 写入）

**上一轮结论：** 未通过；其定位的 15 个 false-negative 已按限定范围全部返修。

**作者返修结果：** 15 项均恢复进入 denominator；14 项读取 exact-v1 HTML，`2609.20543v1` 读取 exact-v1 PDF。逐项评分、证据边界与 Books 比较已落盘，其中 13 项有具体 Existing Coverage 锚点，2 项进入 Books queue。同一 generic-close 理由簇另抽检 12 项完整摘要，均维持 family-specific closure，未发现新的共享误判。

复核者：`/root/sep18_final`（fresh non-author reviewer；未参与本日报作者筛选、三轮返修或 Books 写入）

结论：通过

限定终审确认第三轮 15 项全部进入 denominator、候选表、evidence locator 与 Books queue，其中 14 项使用 exact-v1 HTML、`2609.20543v1` 使用 exact-v1 PDF；对 12 项 generic-close 样本重读完整摘要后，关闭理由仍成立，未发现同类共享漏收。账目复算为 `633 → 142 arXiv + 3 engineering = 145` 个新 Source Family，另有 2 个不重复评分的修订事件，共 147 个事件；Books 处置为 `24 Integrate + 120 Existing Coverage + 1 Weekly Only`。`2609.19579` 与 `2609.20779` 在 Ch28/Ch66 各只有一个 source-family marker，正文均位于 `Review notes` 前，机制、代价、证据边界和回退条件与本日报一致。未重扫其余 618 项，也未修改 Books。跨模型复核按本次非交互子任务约束跳过。
