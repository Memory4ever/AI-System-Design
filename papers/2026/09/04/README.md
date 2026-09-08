# Daily Research — 2026-09-04

**规范：** V3
**窗口：** 2026-09-03T09:00:00+08:00 ～ 2026-09-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T16:25:00+08:00

## 1. 结论

继续用户认可的初筛尺度，不继承旧177/91分母或完成标签。47项原拟留与8项排除侧恢复已由Root读真实题摘独立准入。对齐正式报告时发现04105在本窗官方primary-new、active v1且有直接执行/训练边界，却未出现在初筛输出，已单项恢复并由Root认可；没有据此重开全池。当前56项是工作集合，不是56项已证明长期贡献。

原850个去重缓存含窗外、普通revision、跨类；546首次公告身份与四主类366属于不同来源范围，不把任一原始规模称作项目贡献。56项对应缓存均为本日首次公告active v1，不启动旧新版本比较。

56项均已完成当前采用范围的作者审阅与非作者核验：50项可作有限采用、6项中心证据争议暂缓。五项整合在Ch20、Ch33、Ch36、Ch49、Ch72的实际正文及相邻交接已核验，另45项由具体已有论点承载。02899等有限采用项仍有明确不采用的经验争议，不以局部通过认证所有数字。普通审阅、Books落实和独立待办为零；以下具名来源/日期限制与中心争议已作为不支持正面结论或Books的终态保留项。评分按当前Design Delta/System Reach/Durability路由，不复制旧分数。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本窗Legora/Playco/Daybreak核心说明，机构记录 | 受阻 | 三公告贡献退出；关联Defense Factory缺独立first-public，不借公告时刻纳入 |
| SRC-ANTHROPIC | 本窗官方Research快照及Fable/Mythos与更早AWS归属，原始记录 | 已检查 | 无确认本窗独立新贡献 |
| SRC-GOOGLE-AI | WeatherNext范围退出、GeoX logging patch退出，机构记录 | 受阻 | Security Prompt Hardening与Hierarchical Context-Aware Graph RAG两页只有年精度，未锚定本窗 |
| SRC-META-AI | 本窗定点核查，依据 | 已检查 | 后发卡不重置arXiv first-public；无确认本窗新增独立机构事件 |
| SRC-QWEN | 英中目录与ECommerce博客，机构记录 | 已检查 | 博客对应2608.30730已于Sep01 arXiv公告，不重复纳入 |
| SRC-DEEPSEEK | 官方本窗发布入口，快照 | 已检查 | 无确认本窗新事件 |
| SRC-MOONSHOT | 本窗release/changelog，机构记录 | 已检查 | KimiCode0.40归Sep03，未确认本窗独立新贡献 |
| SRC-TENCENT-HUNYUAN | Research下方“全部”用户截图仅显示9行，最上方Aug28；共同记录 | 受阻 | 可点击目录/具体论文链接仍有提取缺口，不把空响应当无更新 |
| SRC-ZAI | 官方Research目录，共同记录 | 已检查 | 所取目录未命中本窗，不宣称全站无遗漏 |
| SRC-BYTEDANCE-SEED | 官方Research/论文目录，共同记录 | 已检查 | 所取目录未命中本窗 |
| SRC-BAIDU-ERNIE | 官方博客/论文入口，共同记录 | 已检查 | 所取目录未命中本窗 |
| SRC-XIAOMI-MIMO | Paper/Blog与publisher route/frontmatter已恢复，共同记录 | 已检查 | 所取blog窗外，MiMoCode0.1.14归Sep03 |
| SRC-MINIMAX | llms.txt/techblog/changelog，共同记录 | 已检查 | 所取AgentTeam为May13、最新changelog Aug27，未确认本窗事件 |
| SRC-ARXIV | 官方primary-new与已存相关题摘，546首次公告身份；初筛、日期/状态、独立准入 | 已检查 | 56项工作集合，不代表全学科召回；50项有限采用与6项争议均已明确处置 |

只处理每日来源及实际触发，不重扫每周来源。arXiv公开时间以官方primary-new批次及公告时制20:00 EDT换算本日08:00；RSS午夜日期只是标签，submitted不当公开时刻。中国新增来源与机构边界共享一次记录，不在每日报复制全年审计。

## 3. 候选与判断

下表是本窗56个唯一候选的最终处置；有限命题通过不等于整篇所有结论成立。安全、纠错和实质Books缺口即使不足7分也按采用范围深入。独立依据见Root记录、精确证据复用与实际Books及其余31项独立复核。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Modern Transformers Are Implicit Hybrids: From Functional Differentiation to Principled Hybrid Architecture Design](https://arxiv.org/abs/2609.02986v1) | 2026-09-04T08:00:00+08:00 | 区分 Transformer 头的检索与局部混合角色，重新组织全注意力和线性注意力；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md) |
| [BASP: Communication-Efficient Batch-Aware Sequence Parallelism for LLM Training](https://arxiv.org/abs/2609.03151v1) | 2026-09-04T08:00:00+08:00 | 调度单元从 microbatch 下沉至序列组以改善训练执行；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Speculative Macro Commit for Faster Tool-Using Agents](https://arxiv.org/abs/2609.03236v1) | 2026-09-04T08:00:00+08:00 | 隔离快照内行动提议与宏动作提交分离；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory](https://arxiv.org/abs/2609.03340v1) | 2026-09-04T08:00:00+08:00 | 事实最新不等于依赖旧事实的计划有效，执行前只核验相关依赖；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving](https://arxiv.org/abs/2609.03494v1) | 2026-09-04T08:00:00+08:00 | 页满时动态选择压缩或增加请求总KV容量；不是修改物理page粒度；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation](https://arxiv.org/abs/2609.03515v1) | 2026-09-04T08:00:00+08:00 | 淘汰分数的时间聚合与排序保持可能比局部 scorer 改动重要；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [The Attention Triangle in Audio-Video Models](https://arxiv.org/abs/2609.03586v1) | 2026-09-04T08:00:00+08:00 | 音视频跨模态路径会把参数先验带入另一模态并压过提示条件；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Spurious Advantage Hidden in GRPO](https://arxiv.org/abs/2609.04063v1) | 2026-09-04T08:00:00+08:00 | 有限答案空间的猜中会获得 GRPO 伪高优势；2 + 2 + 3 = 7 | 争议 | 暂缓 — `TRAIN-GRPO`，当前版本关键命题未澄清，不进入Books |
| [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](https://arxiv.org/abs/2609.04098v1) | 2026-09-04T08:00:00+08:00 | 递归状态的量化误差可能被门控和覆写抑制，融合核还要求 scale 一致；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Rethinking On-Policy Distillation of Large Language Models II: One Training Example](https://arxiv.org/abs/2609.04172v1) | 2026-09-04T08:00:00+08:00 | 少量提示可能覆盖 OPD 的大部分状态，数据数量与状态覆盖脱钩；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](https://arxiv.org/abs/2609.04198v1) | 2026-09-04T08:00:00+08:00 | 共享 endpoint 的模型名称不等于固定测量仪器，服务噪声影响排序；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors](https://arxiv.org/abs/2609.02959v1) | 2026-09-04T08:00:00+08:00 | unembedding 的 unigram 方向可分解并干预先验依赖；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation](https://arxiv.org/abs/2609.02998v1) | 2026-09-04T08:00:00+08:00 | 先验证教师在当前提示的可靠性，再分流 OPD 或 verifier RL；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [ObserverBench: Testing Mechanistic Estimates for Intervention and Control](https://arxiv.org/abs/2609.03026v1) | 2026-09-04T08:00:00+08:00 | 内部估计精度与基于估计的行动损失必须分别测量；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [It's the Problem, Not the Path: Budget and Difficulty Confounds in LLM Reasoning Trajectories](https://arxiv.org/abs/2609.03436v1) | 2026-09-04T08:00:00+08:00 | 同预算重启与题目难度控制会改变对推理突破和早期预判的结论；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LeanGRPO: Eliminating Redundant Recomputation in Diffusion RL](https://arxiv.org/abs/2609.03528v1) | 2026-09-04T08:00:00+08:00 | 同后端 on-policy diffusion RL 可复用 rollout 图或事后重加权梯度；3 + 2 + 3 = 8 | 深入完成 | 整合 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [</think> Doesn't Stop Reasoning: Analysis of Spurious CoT Termination](https://arxiv.org/abs/2609.03633v1) | 2026-09-04T08:00:00+08:00 | 注入结束标记不保证消除reasoning-like续写，不等于硬停止；2 + 1 + 2 = 5 | 深入完成 | 整合 — `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Free Pause Tokens](https://arxiv.org/abs/2609.03807v1) | 2026-09-04T08:00:00+08:00 | 共享权重的并行预测流提供额外思考而不增加序列或 KV 长度；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors](https://arxiv.org/abs/2609.03884v1) | 2026-09-04T08:00:00+08:00 | 生命周期 hook 在模型不可见时以宿主权限执行，绕过仅防提示的边界；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Headroom-Drift Replay: A Primitive for Principled Replay Control in GRPO](https://arxiv.org/abs/2609.03941v1) | 2026-09-04T08:00:00+08:00 | 回放的剩余学习价值与当前策略兼容性分开控制；2 + 2 + 2 = 6 | 争议 | 暂缓 — `TRAIN-GRPO`，当前版本关键命题未澄清，不进入Books |
| [Representational alignment yields generalizable safety in language models](https://arxiv.org/abs/2609.04022v1) | 2026-09-04T08:00:00+08:00 | 相同标注下表征结构对齐与行为对齐可能产生不同对抗泛化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR](https://arxiv.org/abs/2609.04108v1) | 2026-09-04T08:00:00+08:00 | 检验OPD与RLVR分阶段/联合训练的目标和预算条件；机制归因仍待澄清；2 + 2 + 2 = 6 | 争议 | 暂缓 — `TRAIN-GRPO`，当前版本关键命题未澄清，不进入Books |
| [Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views](https://arxiv.org/abs/2609.04180v1) | 2026-09-04T08:00:00+08:00 | 检验辅助知识视图相对文档重复的增量；语料账和因果归因仍有争议；2 + 2 + 2 = 6 | 争议 | 暂缓 — `TRAIN-DATA`，当前版本关键命题未澄清，不进入Books |
| [Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning](https://arxiv.org/abs/2609.04194v1) | 2026-09-04T08:00:00+08:00 | CoT文本可读性与续写原答案概率的条件变化分开测量；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Routing Is Not Enough: Diagnosing Intra-Adapter Subspace Contention in MoE+LoRA Fine-Tuning](https://arxiv.org/abs/2609.03150v1) | 2026-09-04T08:00:00+08:00 | MoE 路由分开仍会发生低秩适配器子空间竞争；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings](https://arxiv.org/abs/2609.03376v1) | 2026-09-04T08:00:00+08:00 | 二值检索表示与双服务器 MPC 联合设计以降低私有搜索通信；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Latency-Aware Orchestration for Multi-Agent LLM Workflows on Heterogeneous GPUs](https://arxiv.org/abs/2609.03335v1) | 2026-09-04T08:00:00+08:00 | 代理工作流逻辑依赖与异构 GPU 物理执行图分开优化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Every Kernel Is a Join: Automatic Multi-GPU Parallelism for AI Computations in Einsummable](https://arxiv.org/abs/2609.03905v1) | 2026-09-04T08:00:00+08:00 | 以关系 join-aggregation 分解和专用 exchange 代替固定并行策略菜单；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [LeanStream: A Speculate-and-Refine Streaming Framework for Efficient on-Device LLM Inference](https://arxiv.org/abs/2609.03079v1) | 2026-09-04T08:00:00+08:00 | 存储卸载时利用部分 GPU 结果渐进修正稀疏加载，平衡早预测与准决策；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [RecurTrace: Adaptive Latent Reasoning with Loop-Time Memory](https://arxiv.org/abs/2609.03379v1) | 2026-09-04T08:00:00+08:00 | 循环层引入 loop-time 历史记忆及监督停机；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.03383v1) | 2026-09-04T08:00:00+08:00 | 跨策略保存转移图作为统计参考而非重放到 policy loss；2 + 2 + 3 = 7 | 深入完成 | 整合 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Inferred Generative-Process Diversity Predicts Correlated Failure Across Language Models](https://arxiv.org/abs/2609.03422v1) | 2026-09-04T08:00:00+08:00 | 模型差异需按相关失败而非语义差异衡量；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Extracting Forgotten Prompts from Targeted Unlearned Models](https://arxiv.org/abs/2609.03662v1) | 2026-09-04T08:00:00+08:00 | 遗忘后的拒答痕迹还能暴露被遗忘提示自身，而非只泄露已知提示答案；3 + 2 + 3 = 8 | 深入完成 | 整合 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [High-Dimensional Learning Dynamics of Attention-Indexed Models](https://arxiv.org/abs/2609.03858v1) | 2026-09-04T08:00:00+08:00 | 注意力矩阵直接、绑定及非绑定参数化产生不同对称破缺学习动力学；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) |
| [Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010v1) | 2026-09-04T08:00:00+08:00 | 保留 AR 分布同时用扩散并行采样，挑战草稿模型与扩散模型的常规边界；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Towards a Statistical Understanding of Mixture-of-Experts](https://arxiv.org/abs/2609.03501v1) | 2026-09-04T08:00:00+08:00 | 局部聚合框架分离专家学习、路由估计和计算预算误差；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [The Head Complexity of Boolean Functions in Single-Layer Attention](https://arxiv.org/abs/2609.04046v1) | 2026-09-04T08:00:00+08:00 | 单层注意力的 head 数下界不能由无限宽度或精度补偿；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md) |
| [WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models](https://arxiv.org/abs/2609.03681v1) | 2026-09-04T08:00:00+08:00 | 按交互状态调用有限可信想象，而非每步完整 rollout；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.03602v1) | 2026-09-04T08:00:00+08:00 | 因果 mask 让未来视频仅参与训练监督，部署删除视频生成分支；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Do Video Generators Track the World Across Segments? A Benchmark and Method for World-State Reasoning in Video Continuation](https://arxiv.org/abs/2609.03673v1) | 2026-09-04T08:00:00+08:00 | 历史图像记忆与当前可修改实体状态分离，显式维护跨段世界状态；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping](https://arxiv.org/abs/2609.03919v1) | 2026-09-04T08:00:00+08:00 | 动态稀疏 octree 融合生成观测为可重访三维状态；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States](https://arxiv.org/abs/2609.04196v1) | 2026-09-04T08:00:00+08:00 | 相机重力/朝向条件与几何、外观共同生成，不等于完整动力学；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Principia: Relational Physics Tests for Video Models](https://arxiv.org/abs/2609.04200v1) | 2026-09-04T08:00:00+08:00 | 相对物理关系用于消除视频帧率尺度和标定干扰；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Interface-Induced Trajectory Censoring](https://arxiv.org/abs/2609.03966v1) | 2026-09-04T08:00:00+08:00 | 模板和解析器的交互可静默截断工具调用，模型能力与接口测量须分离；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Contamination Inflates Scores but Rarely Reorders Large Language Model Leaderboards](https://arxiv.org/abs/2609.02899v1) | 2026-09-04T08:00:00+08:00 | 污染导致绝对分数上升不等于模型排名改变，需要差异污染对照；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Inferring Hidden User Models from the Behavior of Personalized LLM Agents](https://arxiv.org/abs/2609.03815v1) | 2026-09-04T08:00:00+08:00 | 即使记忆文本不可读，个性化行为仍泄露压缩用户模型；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation](https://arxiv.org/abs/2609.03557v1) | 2026-09-04T08:00:00+08:00 | 动作轨迹录制与离线渲染分阶段以维持时序监督并容纳不同引擎约束；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://arxiv.org/abs/2609.04102v1) | 2026-09-04T08:00:00+08:00 | 常开audio encoder与foundation model共享DRAM预算，通过共同pre-quantizer接口蒸馏压缩；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval](https://arxiv.org/abs/2609.03201v1) | 2026-09-04T08:00:00+08:00 | 稀疏supersession/merge/contradiction随atomic evidence交付，替代全图维护与反思；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [LLMs Learn Better In-Context from Rules than from Examples](https://arxiv.org/abs/2609.03213v1) | 2026-09-04T08:00:00+08:00 | 同任务规则/样例与base/instruct条件对照限制ICL输入选择；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖 — `AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [CoFiE: Coarse-to-Fine Evidence Selection for Efficient Streaming Video Understanding](https://arxiv.org/abs/2609.03675v1) | 2026-09-04T08:00:00+08:00 | encoder前query-agnostic过滤与prefill内query-specific选择分工改变端到端成本；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `INFER-PREFILL` [Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070v1) | 2026-09-04T08:00:00+08:00 | 离散tokenizer训练后部署连续latent与frozen decoder，改变action输出路径；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Judging LLM-as-a-Judge: Concerning Rubric Artifacts in LLM-based Automated Text Generation Evaluation](https://arxiv.org/abs/2609.02942v1) | 2026-09-04T08:00:00+08:00 | rubric-only和response/rubric反转检验judge对实际回答的敏感性；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FailBench: How Reliable are VLMs at Judging Robot Task Success?](https://arxiv.org/abs/2609.03611v1) | 2026-09-04T08:00:00+08:00 | 跨域finetune退化与不可见contact证据分层限制VLA失败检测器的使用；2 + 1 + 3 = 6 | 争议 | 暂缓 — `PLATFORM-EVALUATION-SYSTEM` 当前材料实质冲突未澄清 |
| [Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents](https://arxiv.org/abs/2609.02889v1) | 2026-09-04T08:00:00+08:00 | iso-budget槽位优化与WebShop全null分开搜索预算不足和无可优化收益；2 + 1 + 3 = 6 | 争议 | 暂缓 — `AGENT-PLATFORM` 当前材料实质冲突未澄清 |
| [Hardware-Aware FP4 FlashAttention-4](https://arxiv.org/abs/2609.04105v1) | 2026-09-04T08:00:00+08:00 | 概率量化与TMEM生命周期约束分开，受测FP4 P/V训练发散限制forward到training推广；3 + 2 + 3 = 8 | 深入完成 | 整合 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |

## 4. 证据与知识整合

### [Speculative Macro Commit for Faster Tool-Using Agents](https://arxiv.org/abs/2609.03236v1)

exact-v1§3–5/Algorithm1，actor只确认首动作，executor提交后缀改变策略；AppWorld同资源比较有任务质量下降，非无损或等资源普遍加速。实际重读Ch78 Tool Admission与Interaction Latency前后，已有近似分支、隔离/不可逆副作用、成本和回退。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory](https://arxiv.org/abs/2609.03340v1)

exact-v1§3.3–6/Appendix C，fresh事实不保证计划重推导；依赖少报/过报和多owner非原子边界保留。实际重读Ch77 Derived Graph及前后，parent ID、工具依赖、effect-time check及Ch78/81事务handoff完整。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [GrowPage: On-Demand KV Budgeting for Efficient LLM Reasoning Serving](https://arxiv.org/abs/2609.03494v1)

复用独立exact-v1§1–7及必要附录：Hold压缩释放slot但不归还page，Grow由全局allocator决定；单次attention界不保证未来query/答案。实际重读Ch45排序/刷新→总容量→深度残差交接，page持有、共享prefix、临时副本、fallback/preempt完整，NoChange；不是page-size演进。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [What Matters for Aggressive Decoding-Time KV Eviction? Temporal Aggregation and Ranking Preservation](https://arxiv.org/abs/2609.03515v1)

独立exact-v1§3–5/Limitations/AppE-F只支持有限score-refresh/ranking实验；EMA逐层同时改变层权重和时间，Score-Free未证明scorer无用。实际重读Ch45第439段及前后，刷新频率/容量检查、新token初始化、质量损失/物理内存区分均在，NoChange。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [LeanGRPO: Eliminating Redundant Recomputation in Diffusion RL](https://arxiv.org/abs/2609.03528v1)

exact-v1§3–5/Appendix B/C/G，retained graph或逐轨迹单位advantage临时梯度，先乘真实权重再同步；相同prompt布局不共享不同生成激活。实际重读Ch36 Long-context RL前后两段，policy/backend/objective前提、OOM和实数/逐位等价区别完整，既有整合核实。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [TIGPO: Temporal Instance-Graph Policy Optimization for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.03383v1)

exact-v1§3–5/Eqs1–9，历史图/outcome只作detached reference，loss仍消费当前rollout；estimator/重访分布却改变。实际重读Ch33 Hierarchy of Groups→历史参照→Delayed Correction，task/state条件、配额与图成本、group-size混杂完整，既有整合核实。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [Extracting Forgotten Prompts from Targeted Unlearned Models](https://arxiv.org/abs/2609.03662v1)

exact-v1§2–5/§7/AppC.1，攻击用retained prompts构造实体/模板候选，target leakage与content leakage不同。实际重读Ch72 Unlearning到Deployed Precision，有限候选/主题匹配、双轨验收与非通用不可区分保证完整，既有整合核实；搜索空间数字冲突不采用。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [Hardware-Aware FP4 FlashAttention-4](https://arxiv.org/abs/2609.04105v1)

独立exact-v1§1–8.6/Eqs1–29/Tables1–18，仅采用Direct-P自洽近似和指定D128 TMEM score/P/输出最后使用时刻；barrier不增加容量，受测MXFP4 P/V训练发散。实际重读Ch49 TMA→TMEM两段→跨Block共享，forward/training精度、质量与硬件形状限制完整，既有整合核实。 采用范围与原非作者精确证据定位见本轮复用/当前Books记录。不声称代码运行或整份附录复现，当前采用命题与实际Books绑定已独立通过。

### [The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors](https://arxiv.org/abs/2609.02959v1)

精确独立v1§3–7/AppB-C核实中心化OLS频率方向：logit拟合唯一不等于hidden方向总唯一，分解成拟合prior与残差是代数表示，不证明网络完整执行Bayes；PCA/正交不等于统计独立。采用有限表征与干预边界，不采用标题式‘知道无知’。实际顺读Ch5‘Probe、Causal Intervention与机制解释’前后，readout≠use、干预与跨场景泛化分离已有完整覆盖，NoChange。 采用范围及精确非作者来源见当前证据与Books记录，不是新的全文复现声明。

### [Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation](https://arxiv.org/abs/2609.02998v1)

精确独立v1§2–4.6/Algorithm1/AppB-D核实K=3教师试答门控：合格走OPD，否则group-centered verifier reward，未做std归一化；统一reward可能零信号。已先计算的teacher反馈被拒用不等于节省调用，probe和eager分支并非免费。实际顺读Ch31‘Teacher与未来Reward Model都是反馈回路中的状态’及前后，teacher reliability决定反馈能否进更新、采样/不确定性/错误放大边界均已承载；Ch33蒸馏路由是handoff，NoChange。 采用范围及精确非作者来源见当前证据与Books记录，不是新的全文复现声明。

### [The Attention Triangle in Audio-Video Models](https://arxiv.org/abs/2609.03586v1)

独立v1§3–6/Eqs1–5/AppC-F/H3区分audio→video values与row-rollout方向，attention路径关联不能冒充全网络因果传输。预筛失败样本的修复率不是自然失败发生率，排除不明确样本后的条件归因不是总体正确率；额外推理/分割并非无成本。实际顺读Ch23早/晚/cross-attention融合前后，跨模态查询与K/V信息方向、联合耦合和隔离边界已有覆盖；该受限诊断方法没有改变该设计判断，NoChange。 采用范围及精确非作者来源见当前证据与Books记录，不是新的全文复现声明。

### [Rethinking On-Policy Distillation of Large Language Models II: One Training Example](https://arxiv.org/abs/2609.04172v1)

精确独立v1§2–5/§9/AppB仅支持query+student-prefix状态比问题条数更接近OPD采样粒度；PCA/K-means相对teacher-hidden参考的覆盖率不是所有部署状态覆盖。固定64轨迹回放可继续提升，不证明唯一优化原因。复用原非作者Books审阅并实际重读Ch31‘后训练分支的本质差异是State Distribution’、反馈预算/覆盖floor及独立Evaluation前后，state分布/policy与teacher revision/rollout代价均已承载；NoChange，不归通用Pretraining。 采用范围及精确非作者来源见当前证据与Books记录，不是新的全文复现声明。

### [Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR](https://arxiv.org/abs/2609.04108v1)

v1§2–6/Limitations/AppA-C和固定reference单文件已有独立实读。完整trajectory reverse-KL不能无条件化简为即时detached-token advantage梯度；paper统一EOS-mask与reference接口不一致，且reference不是产生数字的runtime forks。all-wrong触发实际用binary correctness，不能据原记号说teacher永不触发。保留有限sequential/joint比较，但这些目标/运行合同争议未澄清，Disputed，不进入Books。 精确证据与争议定位见本轮记录。

### [Headroom-Drift Replay: A Primitive for Principled Replay Control in GRPO](https://arxiv.org/abs/2609.03941v1)

v1§3–5/A.3/B/C/F/G已有独立实读。按原定义benchmark等权macro，matched naive五项Mean@32重算.3545并非.3117，HD为.35326，不能采用原文数学基线全面优势；不擅自选分项为真实实验更正。headroom只是概率空间proxy，drift只是所采动作log-ratio，均非完整梯度/KL或缓存排序保证。保留有限机制记录，等待表项/汇总澄清，Disputed，不写Books。 精确证据与争议定位见本轮记录。

### [Spurious Advantage Hidden in GRPO](https://arxiv.org/abs/2609.04063v1)

v1§3.1/3.4/§4/AppB-D-F已有独立代数审阅：忽略epsilon且两类存在时平方根比率是优势标量权重，不是完整梯度范数或猜测标签。SignBalance负类幅度仍依赖组组成，stop-gradient不使所有rollout composition-free；同类单独归一Eq9为零无法支持非零count幅度解释，但不能据此否定完整loss可能含KL。原公式/声明争议保留，Disputed，不把新方法写Books。 精确证据与争议定位见本轮记录。

### [Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views](https://arxiv.org/abs/2609.04180v1)

v1§3–9/Limitations/AppA-B-D-E已有独立审阅。仅为CPT数据构造变化；作者knowledge-bearing token-match不是已核事实曝光/语义量一致。Table7语料分领域1815份与总1764份、token总量账不一致；Table3不支持全指标词面重叠更低，Table12 prerequisite bigram frequency反高于对照。有限probe改善不抹去语料账/归因矛盾，Disputed，等待原语料统计及说明，不写Books。 精确证据与争议定位见本轮记录。

### [MemoryLACE: Memory Lifecycle-Aware Consolidation and Evidence Retrieval](https://arxiv.org/abs/2609.03201v1)

精确独立v1§I–VII及公式/表I–IV采用稀疏生命周期关系与active-anchor有界展开：atomic是带来源的模型重述，不自动为真；linked merge保留原条目，compact merge另为丢弃细节分支，query允许partial evidence units，故不保证完整冲突消费。实际顺读Ch77 typed write状态转移与anchor→bounded expansion→evidence assembly，scope/provenance/supersession、查询预算和缺失anchor等边界已有覆盖；NoChange，不把生命周期命名当并发事务保证。 精确证据定位见当前记录。

### [Interface-Induced Trajectory Censoring](https://arxiv.org/abs/2609.03966v1)

独立exact-v1§3/4/6确认emission、template/envelope、parser、execution/observation是不同测量层；有限2×2组合表支持具体适配交互，tool_calls=0不能单独归因模型无调用意图。7B样本有bare JSON但训练OOM无gradient step，未证明修复后RL改善；也不能倒推1.5B失败全因接口。实际顺读Ch78 raw output→parse→validation→execution→observation及Ch66 adapter semantic equivalence、raw trajectory/component receipts，当前已能承载分层测量/归因判断，NoChange。 精确证据定位见当前记录。

### [FailBench: How Reliable are VLMs at Judging Robot Task Success?](https://arxiv.org/abs/2609.03611v1)

独立v1§3–7/AppB/Table7确认source/signal条件、macro/micro分母与crop有限收益。原文top3‘any’仅134错误若指并集，将给BA至少.9344，冲突Table1约.76；不能擅自改成共同错误交集。5组finetune跨域退化不是所有机器人微调有害，观察信号不足不等物理不可观测普遍定律。真实计数/语义冲突待澄清，Disputed，暂不写Books。 精确证据定位见当前记录。

### [Where Does Harness-Optimization Value Live? Localized Gains and the Budget-Splitting Trap in Self-Evolving LLM Agents](https://arxiv.org/abs/2609.02889v1)

独立v1§3–9/Algorithm1/AppA确认iso-budget槽位搜索与reach-a-validated-candidate成本应分开，空选择不证明所有harness优化无价值。但论文声明相同rendered inputs byte-identical rollouts，多个空harness/stock却有不同结果；未交代环境reset/seed/backend等差异，不能以不显著修复identity矛盾。22:6为16净胜非22，McNemar .617有可解释未截断连续性校正，不能说算术必错。保留有限预算机制，Disputed，不写Books。 精确证据定位见当前记录。

### [Free Pause Tokens](https://arxiv.org/abs/2609.03807v1)

独立v1§2–7/AppA-B核实state流写KV、prediction流只查询且由LM head读出；无新增KV位置不等于无新增FLOPs。共享gated-FFN变体的state依赖prediction，不能把基本版state-only prefill与共享版低训练成本拼成同一已证部署点。实际顺读Ch17 parameter/execution depth、内部state/readout分离及Ch19缓存handoff：这里是另一种局部计算分配实例，现有‘额外内部计算引入状态与成本、固定结构仍合理’判断足够；NoChange，不采免费推理标题或所有变体等价。 具体证据见本轮记录。

### [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.03602v1)

独立exact-v1方法/mask消融/AppE-G核实action query不能读future-video K/V，未来视频loss塑形共享权重但非部署action依赖。DAC只是基于轨迹/可行区域的soft regularizer，不是collision shield。实际顺读Ch25‘World Model也可以只在训练期承担表示约束’及相邻Pixels/latent、closed-loop correction，训练期辅助分支与部署依赖已明确分开；NoChange，不把H20/H800跨表或预处理外延迟说成端到端加速。 具体证据见本轮记录。

### [Do Video Generators Track the World Across Segments? A Benchmark and Method for World-State Reasoning in Video Continuation](https://arxiv.org/abs/2609.03673v1)

独立exact-v1§2–5/AppA/D区分历史视频解析state、prompt更新的估计、预测未来帧与renderer；未来帧不是观测真值。SES、条件SCS、sample级SCS-All不同分母，不能直接相乘；同模型parser/updater/judge有共同偏差。实际顺读Ch25 observed→derived→imagined与mutable hidden-state/controlled intervention前后，当前状态和预测目标、可见画面与状态追踪分开已有覆盖；NoChange，不声称实现强制schema隔离或真实物理因果。 具体证据见本轮记录。

### [Modern Transformers Are Implicit Hybrids: From Functional Differentiation to Principled Hybrid Architecture Design](https://arxiv.org/abs/2609.02986v1)

RFIS/RPD分别检验频率贡献与rotation依赖，head-wise hybrid是有限结构归纳偏置，不证明完整两类taxonomy。受测2K训练/有限NIAH及不同scale边界保留；Ch15头分化的诊断、干预与实际能力分离已有覆盖，NoChange。 本轮实际精确读取范围与条件见定点证据/Books对读，采用范围已由Root独立核验通过。

### [BASP: Communication-Efficient Batch-Aware Sequence Parallelism for LLM Training](https://arxiv.org/abs/2609.03151v1)

B序列分到N/B子组，保持每GPU BS/N token分摊，局部化attention all-to-all；模型/optimizer跨组同步仍存在，B=1或非整除不享同样机制。Ch36 DP×CP有界pool和step identity已有覆盖，NoChange，不采任意临时buffer/梯度逐位等价。 本轮实际精确读取范围与条件见定点证据/Books对读，采用范围已由Root独立核验通过。

### [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](https://arxiv.org/abs/2609.04098v1)

模块校准global/local scales必须与fused kernel消费方式一致；FP32 reference扰动实验不能直接等同部署BF16数值floor。仅单GDN模型/32K误差观察，不采全架构quantization-proof或通用4bit配方。Ch49scale/权重编码/kernel及验收路径已完整承载，NoChange。 本轮实际精确读取范围与条件见定点证据/Books对读，采用范围已由Root独立核验通过。

### [ObserverBench: Testing Mechanistic Estimates for Intervention and Control](https://arxiv.org/abs/2609.03026v1)

中间估计准确度不等最终action loss，同action/budget/observer信息边界才可比较；线性fixed-direction证书不保证任意Transformer可控。Ch66风险代价与测量estimand已承载，NoChange。 本轮采用范围/未证明边界见定点证据，本轮采用命题已独立核验。

### [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](https://arxiv.org/abs/2609.04198v1)

相同model/fingerprint、request与temperature0不保证输出逐位相同；near-tie gap与noise floor决定rank可分辨性，模拟加采样不等真实追加调用。Ch66 measured-null、预先power与immutable subject已有覆盖，NoChange。 本轮采用范围/未证明边界见定点证据，本轮采用命题已独立核验。

### [It's the Problem, Not the Path: Budget and Difficulty Confounds in LLM Reasoning Trajectories](https://arxiv.org/abs/2609.03436v1)

prefix带来的预算节省和不可替代信息分开；matched generated tokens非matched FLOP/latency，early signal应对题目难度基线而非只看pool AUROC。小模型有限null不证明普遍无用；Ch66/Ch20当前合同已有覆盖，NoChange。 本轮采用范围/未证明边界见定点证据，本轮采用命题已独立核验。

### [A Blind Trust, the Bloody Thrust: When Attacker-Controlled Hook Updates Steer AI Agent Harnesses towards Malicious Behaviors](https://arxiv.org/abs/2609.03884v1)

安装/更新已被接纳后，hook可由harness直接用宿主授予权限执行，而非新的LLM决定；marketplace adoption、sandbox escape和真实发生率未证。Ch72既有durable control cell及load/trigger admission完整承载，NoChange。 本轮采用范围/未证明边界见定点证据，本轮采用命题已独立核验。

### [</think> Doesn't Stop Reasoning: Analysis of Spurious CoT Termination](https://arxiv.org/abs/2609.03633v1)

强制纠错审阅：硬停止生成与注入EoT尝试转answer不同，后者不保证消除reasoning-like续写，也不证明不可见内部推理状态。已修Ch20 budget forcing段并由Root独立实读§3/6.7/7/A.6、写后顺读通过；不采用EAB速度或普适优越结论。 采用范围与实际Books对读。

### [Representational alignment yields generalizable safety in language models](https://arxiv.org/abs/2609.04022v1)

ReSO以人类类别关系的triplet排序约束各层表示，并保留reference KL；DPO比较臂虽同标注却没有同一显式preservation loss，checkpoint目标也不同，不能归因为表示结构的唯一因果效应。PDF pp20–23机制与pp12–15限制支持受限alternative branch，不证明普遍安全或DPO必然更差。Ch31目标/表征干预与Ch66独立对抗评估已承载，不追加方法目录。 采用范围与实际Books对读。

### [Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning](https://arxiv.org/abs/2609.04194v1)

Self-advantage衡量固定模型续写同原答案的条件概率差，不等正确性或删除该步的必要性。50rollout和change-point标签仍有噪声，较好文本judge也不等因果传感器；thinking模式只保留不超过600步的轨迹。Ch31有限过程证据与Ch66 prefix-resampling/faithfulness分离已有覆盖。 采用范围与实际Books对读。

### [Routing Is Not Enough: Diagnosing Intra-Adapter Subspace Contention in MoE+LoRA Fine-Tuning](https://arxiv.org/abs/2609.03150v1)

固定router下扩展门控adapter路径与扩rank不同，增加每token条件容量和spawn状态；近正交梯度本身不是干扰因果证明。小规模两域PPL、code exposure控制与cap/imbalance失败只支持诊断，不能推通用性能或代码正确率。Ch30逐module条件容量、rank/任务预算及可回滚artifact已有覆盖。 采用范围与实际Books对读。

### [Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings](https://arxiv.org/abs/2609.03376v1)

二服务器semi-honest/non-colluding下先秘密共享短hash过滤，再由可信client重建candidate embeddings/rerank和PIR取密文。隐藏最终top-k不隐藏full-scan候选集合及跨查询co-occurrence；表中部分大规模成本是外推，TCP限速不是实际跨云试验。Ch76分阶段检索和Ch72明文/访问模式边界已有覆盖，不认证协议安全证明。 采用范围与实际Books对读。

### [Latency-Aware Orchestration for Multi-Agent LLM Workflows on Heterogeneous GPUs](https://arxiv.org/abs/2609.03335v1)

已确定分支的ready/near-ready逻辑窗口与load/prefetch/reclaim物理图分开；deployment identity可共享replica而每invocation状态隔离，active lease禁止回收。启发式tick只提交可执行前缀并重排未发suffix，不证明全局最优或未解控制分支预测。Ch56外层DAG与engine分权、lease/reserve及预测误差已有覆盖。 采用范围与实际Books对读。

### [Every Kernel Is a Join: Automatic Multi-GPU Parallelism for AI Computations in Einsummable](https://arxiv.org/abs/2609.03905v1)

Join→aggregate→recompose由operator声明合法分解，logical通信proxy与physical拓扑交换分层；共享DAG切成树后只局部最优。Ch36 collective语义/ownership与Ch49候选plan正确性优先已覆盖；不把单Transformer block结果当完整训练集群吞吐。 精确采用范围与实际Books对读。

### [LeanStream: A Speculate-and-Refine Streaming Framework for Efficient on-Device LLM Inference](https://arxiv.org/abs/2609.03079v1)

逐块计算反馈修正下一层权重预取，离线MPC查表在运行时选协调频率；预测错仍有IO与同步开销，重排不证明稀疏化相对dense精确。Ch54 proposal/ready-state与实际权重身份、miss下界已覆盖；两小时温度稳定不等所有手机能耗收益。 精确采用范围与实际Books对读。

### [RecurTrace: Adaptive Latent Reasoning with Loop-Time Memory](https://arxiv.org/abs/2609.03379v1)

循环同位置窗口memory加sequence级halting，固定backbone与direct-answer训练只支持有界latent计算；相对loop位置可定义到更深不代表能力单调。Ch17 parameter/execution depth与readout/停止状态已覆盖，不引入runtime性能结论。 精确采用范围与实际Books对读。

### [Inferred Generative-Process Diversity Predicts Correlated Failure Across Language Models](https://arxiv.org/abs/2609.03422v1)

字节压缩减去permutation可解释部分得到的有符号残差不是metric或真实内部机制；38model-node bootstrap处理dyadic依赖，结果为pairwise关联，不证明选远模型能提升ensemble。Ch82独立误差/同证据边界已有覆盖。 精确采用范围与实际Books对读。

### [High-Dimensional Learning Dynamics of Attention-Indexed Models](https://arxiv.org/abs/2609.03858v1)

Gaussian extensive-rank极限下population loss有限order parameters不等训练动态也有限闭合；tied/untied参数化改变逃逸路径，只是受限onlineSGD结论。Ch14表达结构不保证优化使用、Ch15等价参数化不保证同训练轨迹已覆盖，未采用sample-complexity数字。 精确采用范围与实际Books对读。

### [Towards a Statistical Understanding of Mixture-of-Experts](https://arxiv.org/abs/2609.03501v1)

Top-1适合局部单专家，需凸组合的目标可能需要多expert；shared收益是固定learning-rule/已知partition下残差更易学的条件比较，不是全MoE最优证明。Ch21 selection与contribution分离、joint coadaptation/容量成本已覆盖。 精确采用范围与实际Books对读。

### [Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010v1)

冻结AR verifier与diffusion LoRA proposal分权，拒绝时residual校正，TV对齐接受率但不消除draft/verify成本。1K/8K吞吐测试用预估TPF控制接受长度，不是所有真实请求的测量；Ch48 exact verification/overlap目标及吞吐合同已有覆盖。 精确采用范围与实际Books对读。

### [The Head Complexity of Boolean Functions in Single-Layer Attention](https://arxiv.org/abs/2609.04046v1)

一层attention-only、固定query和线性读出下，清除正softmax分母后k阶项无法表示k+1位parity；不外推含FFN/深层Transformer。Ch15多头表达路径与宽度取舍、Ch16非线性跨通道组合已有承载，不把受限下界当实际head配置推荐。 精确采用范围与实际Books对读。

### [WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models](https://arxiv.org/abs/2609.03681v1)

交互相关scheduler只决定何时想象，world model两次rollout一致性筛选也不是环境真值；只监督真实context的首action chunk，不把全部想象状态当真实轨迹。Ch26 imagination proposal/执行权限与Ch25预测偏差已覆盖，不认证物理安全。 精确采用范围与实际Books对读。

### [OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping](https://arxiv.org/abs/2609.03919v1)

OctMap按投影像素尺度细分octree，融合生成RGB-D后渲染成下一块条件；不是永久真值或固定容量记忆。静态场景、深度误差与GPU节点持续增长边界保留。Ch25持久状态、层级记忆及freshness已承载，No Change。 精确采用范围与实际Books对读。

### [Puffin-World: Scaling a Unified Multimodal Model with Native 3D World States](https://arxiv.org/abs/2609.04196v1)

共同VAE与role/view identity联合生成外观/深度，参考重力经已知相对旋转传播；physics在此不等于完整动力学。训练8视图、同模型相机重估的evaluator依赖及长时动态场景限制保留。Ch25联合几何分支和视觉/几何/控制证据分离已有覆盖。 精确采用范围与实际Books对读。

### [Principia: Relational Physics Tests for Video Models](https://arxiv.org/abs/2609.04200v1)

匹配装置下用同视频相对量检验物理不变量，先筛基本运动合格视频，故是条件分母；不把VBench与物理分数跨尺度等同，也不采用近chance→架构缺陷或抗污染的强结论。Ch66对象/分布/scorer与Ch25物理一致性边界已有覆盖。 精确采用范围与实际Books对读。

### [Compressing Streaming Neural Audio Encoders via Latent-Space Distillation](https://arxiv.org/abs/2609.04102v1)

共同pre-quantizer latent的蒸馏支持复用离散quantizer或连续bridge，不等于token精确一致或联合训练stage必然同收益。六teacher/student组合中stage1结果有退化，前端压缩不能代替完整下游验收；Ch23representation/interface与rate–distortion已有覆盖。 精确采用范围与实际Books对读。

### [LLMs Learn Better In-Context from Rules than from Examples](https://arxiv.org/abs/2609.03213v1)

同任务规则、minimum-coverage示例、二者合用对照显示条件化选择，不支持永久删除示例或‘不同机制必有叠加收益’。规则反复澄清且非token等预算，五任务base/instruct观察不外推。Ch74三类输入职责与Ch75上下文选择已有覆盖。 精确采用范围与实际Books对读。

### [CoFiE: Coarse-to-Fine Evidence Selection for Efficient Streaming Video Understanding](https://arxiv.org/abs/2609.03675v1)

encoder前廉价histogram novelty与prefill中query-conditioned frame选择节省不同阶段成本；前者可能不可逆漏证据，后者不能收回已编码成本，attention打分也非免费真值。Ch43选择成本/状态同步与Ch23编码前稀疏/端到端账本已有覆盖。 精确采用范围与实际Books对读。

### [Continuous Actions from Discrete Minds: Latent-Aligned Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.04070v1)

VQ-VAE先学trajectory prior，部署连续latent经冻结decoder输出、无需未来action token串行采样；不是连续物理安全证明。nuScenes采用oracle BoN20而AlpaSim确定性无BoN，成功率与碰撞率trade-off分开；Ch26latent接口、decoder校准和闭环控制已有覆盖。 精确采用范围与实际Books对读。

### [Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation](https://arxiv.org/abs/2609.03557v1)

Stage I物理轨迹与Stage II固定状态重放渲染分离，trajectory manifest拥有时序监督；node-local执行和异步上传隔离生产瓶颈。图像审美过滤尚未用下游world-model效果校准，产出小时不等于训练收益。Ch27采集合同/lineage与Ch25仿真边界已有覆盖。 精确采用范围与实际Books对读。

### [Judging LLM-as-a-Judge: Concerning Rubric Artifacts in LLM-based Automated Text Generation Evaluation](https://arxiv.org/abs/2609.02942v1)

rubric-only能预测judge标签只证明关联，不能排除题目难度或正确规则本身的可预测性；paired answer/rubric reversal更直接检查criterion sensitivity，但依赖反转构造正确。Ch66rubric形成/criterion执行/排名分层已有覆盖，不采用所有合法rubric必须p(y|r)=0.5的主张。 精确采用范围与实际Books对读。

### [Inferring Hidden User Models from the Behavior of Personalized LLM Agents](https://arxiv.org/abs/2609.03815v1)

普通个性化任务行为可暴露未直接读取的用户语义；固定state、自适应请求、请求已指定值不计恢复，恢复语义与预测行为分开测。真实服务结果conditional-on-retention，防护utility下降；Ch72完整observable-channel/组合攻击与privacy边界已承载。 精确采用范围与实际Books对读。

### [Contamination Inflates Scores but Rarely Reorders Large Language Model Leaderboards](https://arxiv.org/abs/2609.02899v1)

只采用绝对分数、相对排名、检测灵敏度需分开的测量原则；原文原题/改写题差异仍受model-specific难度影响。clean-base与公共中位数参照写法及74模型/表内42计数未解，headline与3/188定量保持争议，不宣称rank一致是无污染证书。Ch66污染/provenance与scorer适用域已有覆盖。 精确采用范围与实际Books对读。

## 5. 缺口与下一步

普通作者、Books落实及非作者审阅待办为零。下列具名限制均为本窗终态保留项，不支持正面证据、Books或无遗漏断言；材料到达时只定点重开。已有精确证据只有采用范围未变才复用，并重新核实际Books段落，不从review文件存在直接推完成。

| 材料 | 缺少什么及为什么必要 | 可接受材料与定点续跑 |
| --- | --- | --- |
| [04108 Sequential Beats Joint](https://arxiv.org/html/2609.04108v1) | 完整trajectory RKL与即时detached-token梯度的关系、EOS mask及实际runtime分歧未解释 | 作者勘误或产生实验的固定代码/配置；只核目标和执行合同，建议`2609.04108v1-runtime-clarification.md` |
| [03941 Headroom-Drift Replay](https://arxiv.org/html/2609.03941v1) | matched naive的逐benchmark等权平均与汇总不一致，影响中心比较 | 对应逐任务结果与明确aggregation或更正表，建议`2609.03941v1-results-correction.csv` |
| [04063 Spurious Advantage](https://arxiv.org/html/2609.04063v1) | 优势标量被解释为完整梯度/猜测标签；类内归一式与非零count幅度声明冲突 | 公式勘误、完整loss及必要假设，建议`2609.04063v1-objective-clarification.md`；不请求无关附录 |
| [04180 Auxiliary Views](https://arxiv.org/html/2609.04180v1) | 语料分领域份数/token账与总量不一致，无法判定匹配曝光和归因 | 对应语料manifest、统计脚本或官方修正统计，建议`2609.04180v1-corpus-accounting.csv` |
| [03611 FailBench](https://arxiv.org/html/2609.03611v1) | top3错误的any/共同交集语义与表中准确率不一致 | per-item三个judge标签或明确集合定义与更正表，建议`2609.03611v1-error-set-correction.csv` |
| [02889 Harness-Optimization](https://arxiv.org/html/2609.02889v1) | 同rendered input逐位相同rollout声明与stock/空harness结果不一致 | 冻结input、reset/seed/backend配置及相应trace或官方解释，建议`2609.02889v1-run-identity.md` |
| Google两项日期 | Security Prompt Hardening与HCRG code migration只有年份，不能确认本窗 | 官方带时间发布记录、匹配arXiv/DOI或更早快照；与Sep01–05共享`google-116-118-first-public.json`请求，不重扫全年 |
| [Defense Factory](https://openai.com/the-defense-factory/) | 关联公告不证明架构页自身首次公开时刻 | 官方RSS/frontmatter/发布记录，建议`defense-factory-first-public.json`；恢复日期后才判断本窗归属 |
| [浑元Research目录](https://hunyuan.tencent.com/research) | 截图可见行在窗外，但可点击完整列表仍取不到 | 完整目录HTML、API或带日期链接的官方导出；复用七天共享请求，不重复索要七份 |

02899另有clean-base/public-median参照和controlled cohort分组的未采用定量争议，详见该节；它不阻碍已明确的测量分层原则及NoChange判断。若日后采用headline，需先取得相应更正，不将可选强主张变成本轮额外待办。

已排除的其他旧候选不自动进入56项，也不清理其已有证据或Books。若发现具体身份/贡献错误，只定点恢复。

## 6. 复核

复核者：`/root`与`/root/screen_sep01`，独立于Sep04原作者。

结论：通过

55项题摘准入及有界排除风险已独立检查；04105经真实题摘与本窗身份确认后单项恢复。全部56项采用范围的非作者审阅、实际Books承载与五项整合写后核验已完成；Root负责25项、另一复核者负责31项，复用和直接新读范围分别可定位。当前无普通待办；六项中心争议和具名来源/日期限制均已隔离为不采用、不写Books的终态保留项，且有精确重开条件，因此整日闭环通过。格式检查只证明可判定的一致性，不替代语义审阅。
