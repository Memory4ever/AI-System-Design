# Daily Research — 2026-08-26

**规范：** V3
**窗口：** 2026-08-25T09:00:00+08:00 ～ 2026-08-26T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T18:20:00+08:00

## 1. 结论

按 arXiv 官方首次公告批次冻结 503 个唯一身份，逐篇完成标题与完整摘要语义筛选，最终保留 55 个具有明确系统责任、状态边界或 evaluation contract 增量的候选；其余身份以题摘语义理由在分母前关闭。此前 930 项 submission-time 集合包含窗口外版本活动，不能用作本日报分母。厂商入口没有独立新增家族，Hugging Face 只作身份补检且不改写 arXiv 首发归属。

本窗的长期变化集中在五条线：KV 从“删除或统一量化”演进为可核算的 residency、动态 reclaim、mixed-format 与 page-wise low-rank state；masked-diffusion、CPU decode、远程 GPU 和 accelerator dataflow 要求 serving/architecture/hardware 联合度量；训练端把 data mixture、有效步长、geo sharding 与同步/热稳定性置于统一运行合同；Agent 把 termination certificate、tool lifecycle、context compression 与 durable memory 分开；evaluation/security 则区分 reader-facing evidence、deployment-time steering、belief confidence 与真实 action quality。55 项均已回到精确版本 primary source 核对机制、评价、限制与 withdrawal 状态，并完成 Books 对读。独立回放恢复了 10 个此前被错误关闭或静默遗失的候选，同时将 12 个重复整合建议收敛为已有覆盖；必要的 Books 机制已写入 canonical owner 并通过写后复核。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 列表检查到窗口边界，无独立本窗技术正文 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 列表检查到窗口边界，无独立本窗技术正文 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind 与 Google Research 列表越过窗口，并与 arXiv 去重 | 已检查 | 无 |
| SRC-META-AI | 官方 Research/Results 越过窗口，并与 arXiv 去重 | 已检查 | 无 |
| SRC-QWEN | 官方论文与模型列表越过窗口，并与 arXiv 去重 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究入口与仓库发布面越过窗口 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与官方仓库/Release 越过窗口 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research/官方仓库与当窗论文身份核对，无额外家族 | 已检查 | 无 |
| SRC-ZAI | Research、发布说明与仓库越过窗口 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research/论文目录越过窗口，并与 arXiv 去重 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与仓库越过窗口 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官方论文/博客与仓库越过窗口 | 已检查 | 无 |
| SRC-MINIMAX | 中英文 Research/Blog 与仓库越过窗口 | 已检查 | 无 |
| SRC-ARXIV | 官方首次公告批次冻结 503 个唯一身份；跨分类去重后逐篇读标题与完整摘要，保留 55 项；其余逐项作 pre-denominator closure；旧 submitted/revision 字段只用于身份核对 | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression](https://arxiv.org/abs/2608.23962) | 2026-08-26T08:00:00+08:00 | 在同一 workload/SLO 下比较 TP 通信成本与 KV 质量损失；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 与 TRAIN-TENSOR-PARALLEL，[Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [RAGSentinel: Certifiable Geometric Consensus for Robust RAG](https://arxiv.org/abs/2608.23965) | 2026-08-26T08:00:00+08:00 | retrieval-time 几何共识可作异常传感器，但不能替代 authorization；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的检索入口防御与 hard policy |
| [Hybrid Semantic Tool Discovery for Enterprise MCP Gateway](https://arxiv.org/abs/2608.23992) | 2026-08-26T08:00:00+08:00 | 将大规模 tool catalog 的 discovery 与 execution/authorization 分离；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MCP，[Ch83](../../../../books/part-07-agent/83-mcp.md) 的 discovery、identity 与 invocation contract |
| [AgentSpec: Speculative Decoding for Batch Inference of LLM Agents](https://arxiv.org/abs/2608.24004) | 2026-08-26T08:00:00+08:00 | 在 batched Agent workload 中联合调节 drafter、acceptance 与调度；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 的 batch-aware speculation |
| [VisCache: Visual KV Cache Pruning for Efficient Vision LLM Inference](https://arxiv.org/abs/2608.24063) | 2026-08-26T08:00:00+08:00 | 多模态 KV 应按 layer/token utility 分层裁剪而非统一删除；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 的 modality-aware state policy |
| [Simthesizer: An Agent-Driven Simulation Framework for LLM Serving Systems](https://arxiv.org/abs/2608.24650) | 2026-08-26T08:00:00+08:00 | 将模拟器扩展从手工改代码演进为带验证边界的模块化机制合成；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的 execution-plan/evaluation boundary |
| [ResiSpec: Enhancing Multi-Candidate Speculative Sampling](https://arxiv.org/abs/2608.24411) | 2026-08-26T08:00:00+08:00 | 以 residual distribution shaping 解释多候选 proposal 的 acceptance bottleneck；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 的 exact verification 与 candidate diversity |
| [A Judge Should Know What Changed](https://arxiv.org/abs/2608.24419) | 2026-08-26T08:00:00+08:00 | 将 judge 可靠性拆为对等价编辑不变与对实质编辑敏感，避免单一 agreement；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 construct validity 与 slice audit |
| [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](https://arxiv.org/abs/2608.24658) | 2026-08-26T08:00:00+08:00 | 区分可依赖拆分的 subtask parallelism 与独立 trial parallelism；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-PLANNING，[Ch79](../../../../books/part-07-agent/79-planning.md) 的依赖图、并行探索与 verifier |
| [On-policy Distillation with Verifiable Reward](https://arxiv.org/abs/2608.24696) | 2026-08-26T08:00:00+08:00 | teacher token signal 只调节通过 outcome gate 的 on-policy trajectory；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 teacher amplitude 与 verifier direction |
| [StepGuard: Learning Step-Level Guardrails](https://arxiv.org/abs/2608.24777) | 2026-08-26T08:00:00+08:00 | pre-execution action monitor 提供风险证据但不能成为最终权限 owner；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 与 AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL](https://arxiv.org/abs/2608.24870) | 2026-08-26T08:00:00+08:00 | 修正 trajectory centering 与 token-mean actor loss 的尺度错配；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的异步 credit/normalization contract |
| [Do Robotic World Models Really Follow Actions?](https://arxiv.org/abs/2608.24885) | 2026-08-26T08:00:00+08:00 | 将 world model 评价从画面质量推进到 off-expert action-following 与可控 transition；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 的 action-conditioned evaluation |
| [Elastic KV Cache for LLM Serving](https://arxiv.org/abs/2608.23658) | 2026-08-26T08:00:00+08:00 | 用 CUDA VMM 实证 reclaim 可行，同时以负结果证明 chunked prefill 常已关闭收益空间；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)；将 reserve reclaim 与更简单 chunk-size baseline 联合决策 |
| [Memory-Sovereign Inference](https://arxiv.org/abs/2608.23805) | 2026-08-26T08:00:00+08:00 | 将 semantic demand、资源 authority、async reuse 与 output exactness horizon 做成可证伪证书；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)；加入 resource-authority 与 exactness-horizon accounting |
| [Serving Masked Diffusion LLMs](https://arxiv.org/abs/2608.23807) | 2026-08-26T08:00:00+08:00 | 真实并发硬件表明 dLLM 的离散 step difficulty、CPU dispatch 与 batch 语义不同于 AR；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；补充 dLLM serving 的 admission/batching 边界 |
| [Minima-KV](https://arxiv.org/abs/2608.23834) | 2026-08-26T08:00:00+08:00 | 用 FP8 anchor/recent、TQ3 stale 与全局 softmax merge 实现不删除 live page 的混合格式 attention；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；与 INFER-PAGED-ATTENTION Ch47 handoff mixed-format lifecycle |
| [Pipeline-Native Transformers](https://arxiv.org/abs/2608.23841) | 2026-08-26T08:00:00+08:00 | 为 CPU bandwidth-bound decode 联合设计模型依赖图、stage-major schedule 与 weight tiling；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；加入 architecture/runtime co-design 的适用边界 |
| [Data Mixing as Mixture Experiment](https://arxiv.org/abs/2608.23922) | 2026-08-26T08:00:00+08:00 | 把 domain mixture 选择改写为 response surface 与最优实验设计，而非只拟合 predictor；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)；在 mixture controller 前加入 interaction-aware experimental design |
| [More Rejective, Not More Discriminative](https://arxiv.org/abs/2608.23941) | 2026-08-26T08:00:00+08:00 | 证明 pre-execution monitor 的 review unit 会同步提高 catch 与 false rejection，不能只看拦截率；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；加入 clean twin、informedness 与 review-unit identity |
| [WebMCP-Phalanx](https://arxiv.org/abs/2608.24017) | 2026-08-26T08:00:00+08:00 | 将 browser tool provenance、semantic quarantine 与 privileged execution 分层，并暴露 call-timing bypass；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MCP，[Ch83](../../../../books/part-07-agent/83-mcp.md)；与 PLATFORM-SECURITY Ch72 handoff effect-time gate |
| [Maia 200](https://arxiv.org/abs/2608.24664) | 2026-08-26T08:00:00+08:00 | 以软件定义局部数据流和显式 data-movement engines 重构 accelerator execution plan；2 + 3 + 2 = 7 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；仅吸收 dataflow/placement 机制，不吸收厂商性能外推 |
| [Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining](https://arxiv.org/abs/2608.24814) | 2026-08-26T08:00:00+08:00 | 以 LR/parameter-norm 的有效学习率统一 schedule、norm control 与 loss dynamics；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)；在 layer/group update contract 前加入 ELR coordinate |
| [RENDER: Controlling Reader-Facing Evidence in LLM Memory Evaluation](https://arxiv.org/abs/2608.23568v1) | 2026-08-26T08:00:00+08:00 | 固定 memory history、只改变 reader-facing artifact 即显著改变评测结果，要求 artifact identity 进入 memory evaluation；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)；在 memory evaluation 中加入 reader projection identity |
| [When May an Agent Stop?](https://arxiv.org/abs/2608.23623v1) | 2026-08-26T08:00:00+08:00 | 用 evidence-carrying termination certificate 取代模型自报 complete，分离轨迹证据与外部事实真值；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) 的 completion admission 与 evidence certificate |
| [Callability Is Not Operability](https://arxiv.org/abs/2608.23628v1) | 2026-08-26T08:00:00+08:00 | 揭示 tool call 已提交但 response 丢失时 schema-valid 调用仍无法安全重试，要求 lifecycle/postcondition 接口；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) 的 postcondition、幂等与 retry state |
| [ToolRobustBench](https://arxiv.org/abs/2608.23635v1) | 2026-08-26T08:00:00+08:00 | 按 observation、selection、argument、execution 与 response stage 注入故障，显示混合失败不可由单项成功率相加；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 layered fault injection 与 failure attribution |
| [Feedback That Backfires](https://arxiv.org/abs/2608.23651v1) | 2026-08-26T08:00:00+08:00 | 失败 tool-call 的原始 transcript 会诱导小模型重复同一动作，反馈表面形式进入 retry state；3 + 2 + 2 = 7 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)；在 error normalization 中加入 failed-call representation |
| [AgentRoom](https://arxiv.org/abs/2608.23740v1) | 2026-08-26T08:00:00+08:00 | 以 CRDT-backed shared workspace 分离 concurrent edits、coordination 与 final verification；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) 的 shared artifact、merge owner 与 verifier |
| [ShardMeter](https://arxiv.org/abs/2608.23840v1) | 2026-08-26T08:00:00+08:00 | 联合模型状态、显存、bandwidth、failure domain 与 geo topology 选择 sharding，而非只看参数量；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 的 topology、failure-domain 与 estimator fallback |
| [PuzzleKV](https://arxiv.org/abs/2608.23843v1) | 2026-08-26T08:00:00+08:00 | 以 logical page 作为 low-rank KV 压缩、增量更新与解码的共同生命周期单元；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；与 INFER-PAGED-ATTENTION Ch47 建立 page-wise low-rank handoff |
| [Beyond the Mandate](https://arxiv.org/abs/2608.23858v1) | 2026-08-26T08:00:00+08:00 | AP2 分析暴露 payment authorization、delegation 与 settlement 之间未被协议口号覆盖的信任边界；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 delegated effect authorization 与 settlement owner |
| [Semantic Overlays](https://arxiv.org/abs/2608.23873v1) | 2026-08-26T08:00:00+08:00 | 将不可信内容标注为 token 之外的 typed overlay，避免 prompt 文本同时承担 data 与 authority；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 provenance/taint metadata 与 effect-time gate |
| [Paritok-4B](https://arxiv.org/abs/2608.24188v1) | 2026-08-26T08:00:00+08:00 | intent-conditioned extractive compression 优先保存 coding-agent 的 identifier、path 与 edit evidence；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md)；在 typed compaction 中加入 task-intent projection |
| [MemUse](https://arxiv.org/abs/2608.24189v1) | 2026-08-26T08:00:00+08:00 | 将 memory evaluation 从直接问答改为自然会话中是否正确使用且不过度提及，改变 memory utility contract；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)；在 recall 指标后加入 natural-integration slice |
| [WiCi: Wireless GPU Computing Infrastructure](https://arxiv.org/abs/2608.24204v1) | 2026-08-26T08:00:00+08:00 | 把移动端 LLM 的 compute state 远程映射到邻近 GPU，引入网络、compatibility、privacy 与 failover 新边界；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION，[Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) 的 remote-compute branch 与 failover contract |
| [Can a Dynamic Internal Field Govern a Transformer's Cognition?](https://arxiv.org/abs/2608.24319v1) | 2026-08-26T08:00:00+08:00 | 为 dynamic compute governor 提供 runtime stability certificate，并明确 certifiability 不等于能力提升；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 的 adaptive compute stability/quality/SLO 三层 Gate |
| [Thermal Tuning Overhead in Wafer-Scale Optical Interconnects for LLM MoE Training](https://arxiv.org/abs/2608.24637v1) | 2026-08-26T08:00:00+08:00 | 揭示 MoE 流量会诱发 optical thermal retuning stall，通信模型必须包含物理控制环；3 + 3 + 2 = 8 | 深入完成 | 整合：TRAIN-TENSOR-PARALLEL，[Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md)；在 topology cost 中加入 thermal-control stall |
| [The Invisible Editorial Layer](https://arxiv.org/abs/2608.24662v1) | 2026-08-26T08:00:00+08:00 | 形式化同一 weights 可被 deployment-time steering 改写行为，黑盒输出不能唯一归因模型本体；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 model-plus-inference-policy subject identity |
| [Confident at the moment of action](https://arxiv.org/abs/2608.24691v1) | 2026-08-26T08:00:00+08:00 | action-time stated confidence 与隐藏信息下真实 belief quality 可错配，outcome-only evaluation 无法发现；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；加入 belief/action/outcome 三层校准 |
| [LAION-BVD](https://arxiv.org/abs/2608.24845v1) | 2026-08-26T08:00:00+08:00 | 提供 10M-hour 视频预训练数据的采集、过滤与合成 caption pipeline，改变大规模视频 data provenance 边界；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) 的 multimodal provenance、deduplication 与 synthetic-caption contract |
| [BrowserForge](https://arxiv.org/abs/2608.24848v1) | 2026-08-26T08:00:00+08:00 | 以并行 browser sandbox 扩展 web episode，同时把 environment image、seed、network 与 cleanup 纳入 artifact identity；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) 的 reproducible environment lifecycle |
| [Recursive Experiential-Working Memory Evolution](https://arxiv.org/abs/2608.24876v1) | 2026-08-26T08:00:00+08:00 | 分离短期 working memory 与经验证后晋升的 experiential memory，明确递归演化和污染风险；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) 的 admission、promotion、quarantine 与 rollback |
| [What FID Hides](https://arxiv.org/abs/2608.24881v1) | 2026-08-26T08:00:00+08:00 | 揭示单一聚合 FID 隐藏 deviation 类型与排序不稳定，要求检测、排序和诊断分离；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；在 multimodal metric 中加入 deviation decomposition |
| [Latent Action as Intention Enables Efficient Future Imagination for World Action Models](https://arxiv.org/abs/2608.24882v1) | 2026-08-26T08:00:00+08:00 | 用 latent action 保留 future imagination 的控制意图，形成 latency 与 generalization 的新分支；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；在 action-conditioned rollout 中加入 latent-action interface |
| [What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions](https://arxiv.org/abs/2608.24022v1) | 2026-08-26T08:00:00+08:00 | 以 attention activation 定位真正影响 tool decision 的 context spans，再按来源 authority 判定；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 behavior-guiding span sensor 与外部 authorization 边界 |
| [Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering](https://arxiv.org/abs/2608.24271v1) | 2026-08-26T08:00:00+08:00 | 以 OpenTelemetry trace 对齐 Agent step、通信、tool 与 LLM call，并在相同位置注入故障；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-MONITORING，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) 的跨组件 trace context 与 fault-injection comparison |
| [FARCA: Fact-Aligned Reliability-Aware Credit Assignment for Reinforcement Learning with Factual Supervision](https://arxiv.org/abs/2608.24350v1) | 2026-08-26T08:00:00+08:00 | 将事实验证定位到 token credit，并以 counterfactual evidence dependence 调节不可靠 verifier signal；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 verifier reliability、credit granularity 与 policy update 分层 |
| [When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness Study](https://arxiv.org/abs/2608.24492v1) | 2026-08-26T08:00:00+08:00 | 评估监督组合 UQ signals 在样本量、域迁移与 generation regime 变化下的条件收益；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 UQ sensor calibration 与 transfer boundary |
| [Joint Optimization of Tool Creation and Use for Large Language Model Agents](https://arxiv.org/abs/2608.24571v1) | 2026-08-26T08:00:00+08:00 | 将 tool schema/code creation 与 held-out invocation 放进同一 policy，并分离三类 reward；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) 的 schema、artifact、execution 与 outcome 验收链 |
| [Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency](https://arxiv.org/abs/2608.23831v1) | 2026-08-26T08:00:00+08:00 | 将已提交动作与 mid-inference observation 写入状态，修复 VLA 延迟破坏的 Markov 假设；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；加入 inference-latency-aware control state |
| [TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models](https://arxiv.org/abs/2608.24232v1) | 2026-08-26T08:00:00+08:00 | 将 prompt、reasoning trace 与 final response 分别标注风险并绑定 source-span evidence；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；加入 reasoning-trace safety evaluation unit |
| [PeakBench: Benchmarking Resource-Aware Tool Invocation in LLM Agents](https://arxiv.org/abs/2608.24509v1) | 2026-08-26T08:00:00+08:00 | 分离 tool dependency planning 与 resource-constrained physical scheduling，避免逻辑正确掩盖资源溢出；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md)；加入 logical-plan/physical-schedule 双层验收 |
| [When “Must” Becomes “Maybe”: Constraint Weakening in LLM Agent Workflows](https://arxiv.org/abs/2608.24569v1) | 2026-08-26T08:00:00+08:00 | 证明摘要、计划与 handoff 可保留内容却削弱 action-binding constraint，需显式保留 authority/fallback/consequence；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md)；加入 operational-state preservation 与下游 containment |
| [Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with AtlasNav](https://arxiv.org/abs/2608.24764v1) | 2026-08-26T08:00:00+08:00 | 将 evidence availability 分解为 surfacing、opening 与 decisive-fragment realization，并复用持久 corpus structure；3 + 3 + 2 = 8 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)；加入 finite-budget evidence realization 与 persistent navigation |

## 4. 证据与知识整合

### [More GPUs or a Smaller Cache? Tensor Parallelism versus KV Compression](https://arxiv.org/abs/2608.23962)

论文用 profiled simulator 把 TP degree 与 KV bit-width/keep-ratio放入同一容量与成本选择。它支持先判断 weight-bound 或 KV-bound，再在质量目标下比较设备、通信和压缩；没有自有 GPU 实测、质量评价或 held-out simulator validation，不能输出通用成本倍数。Ch37 与 Ch45 已保留该联合选择及回退条件。

### [RAGSentinel: Certifiable Geometric Consensus for Robust RAG](https://arxiv.org/abs/2608.23965)

在 honest-majority 与 representation separation 假设成立时，surrogate embedding shift、geometric median 和 topic removal 可降低检索投毒影响。攻击者可适配 surrogate、诚实文档不占多数或 topic cluster 漂移时保证会破裂；它是 retrieval sensor，不是 action authorization。Ch72 已明确这层边界。

### [Hybrid Semantic Tool Discovery for Enterprise MCP Gateway](https://arxiv.org/abs/2608.23992)

材料以 BM25、dense retrieval 与 RRF 从约 2,000 tools 中先选择小集合，再执行精确 tool identity。49-query 测试和生产 telemetry 只支持产品架构可行性，索引滞后、描述质量和 query set 限制外推。长期结论是 discovery confidence 不能替代 permission，Ch83 已承载。

### [AgentSpec: Speculative Decoding for Batch Inference of LLM Agents](https://arxiv.org/abs/2608.24004)

工作指出单请求 acceptance 最优不等于 batch throughput 最优，并联合调整 speculation depth、candidate 与调度。收益绑定模型、batch、长度分布和硬件；verification exactness 仍由 target model 拥有。Ch48 已按 proposal、verify、commit 与 batch pressure 组织机制。

### [VisCache: Visual KV Cache Pruning for Efficient Vision LLM Inference](https://arxiv.org/abs/2608.24063)

VisCache 对视觉 token 做 layer-aware coarse-to-fine 选择，说明多模态 KV 的价值分布不能被统一 keep-ratio 表达。作者实验不证明跨模型、任务和视觉分辨率无损，也没有给出生产 concurrency/SLO。Ch45 已用 modality/phase/quality budget 约束 eviction。

### [Simthesizer: An Agent-Driven Simulation Framework for LLM Serving Systems](https://arxiv.org/abs/2608.24650)

该系统把 workload、engine component 与 metric contract 模块化，再让 Agent 生成或连接新机制；simulation 仍必须通过 trace/calibration 与真实运行验证。它减少模拟器演进的人工作业，不证明生成代码正确或模拟结果等同生产。Ch49 已把 execution plan、measurement model 和 validation boundary 分离。

### [ResiSpec: Enhancing Multi-Candidate Speculative Sampling](https://arxiv.org/abs/2608.24411)

ResiSpec 观察到多候选共享头部概率质量会让 proposal diversity 没有转化为 acceptance，因而整形 residual distribution。收益依赖 drafter/target、候选数与 verifier cost；exact target verification 仍是正确性边界。Ch48 已覆盖 candidate diversity 与 verification budget 的关系。

### [A Judge Should Know What Changed](https://arxiv.org/abs/2608.24419)

论文把 construct validity 表为 invariance 与 construct sensitivity 两个独立维度，说明高 agreement 可能同时对真正变化不敏感。结果支持成对对照与 slice reporting，不证明任何 judge 成为真值 owner。Ch66 已将 evaluator evidence 与 release decision 分离。

### [Parason: Revealing Subtask and Trial Parallelism in LLM Reasoning](https://arxiv.org/abs/2608.24658)

Parason 区分需要显式依赖图的 subtask parallelism 和对同一问题进行独立探索的 trial parallelism，并由最终 verifier 汇合。它能减少关键路径，却增加重复计算、merge error 与 verifier cost；任务不可拆时串行 reasoning 仍成立。Ch79 已拥有该分支。

### [On-policy Distillation with Verifiable Reward](https://arxiv.org/abs/2608.24696)

当前修订版将 teacher 的密集 token guidance 与 verifiable task outcome 组合：outcome 决定更新方向，teacher 只在 student on-policy trajectory 上调节幅度。它不消除 teacher bias，也不扩大 student 未探索状态。Ch33 已明确这一 authority split。

### [StepGuard: Learning Step-Level Guardrails](https://arxiv.org/abs/2608.24777)

StepGuard 在 tool action 执行前给风险判断，并用可扩展监督平衡安全与 utility。该 learned monitor 面对 adaptive attack、distribution shift 与误拒仍可能失败，不能拥有不可逆动作的最终 authority。Ch72/Ch78 已要求 policy/reference monitor 在 effect boundary 决策。

### [SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL](https://arxiv.org/abs/2608.24870)

SPO++ 指出按 trajectory 中心化一个 advantage 后再用 token mean 更新，会与 actor 实际消费的 token-weighted quantity 错配；修正 normalization 使异步单流样本更可比较。作者结果不证明它在所有 reward、长度分布与 staleness 下优于 group-relative baseline。Ch33 已覆盖 token/trajectory weighting 与 behavior-policy identity。

### [Do Robotic World Models Really Follow Actions?](https://arxiv.org/abs/2608.24885)

WorldEcho 扩展到 off-expert action 分布，检查生成未来是否真正随动作变化，而不是仅复现专家视频中的相关性。visual integrity 与 action-following 必须分开；它不证明生成模型已具备真实物理因果或安全控制。Ch25 已以 action-conditioned transition、intervention 与 persistent state 组织评价合同。

### [Elastic KV Cache for LLM Serving](https://arxiv.org/abs/2608.23658)

作者用 CUDA VMM 在 decode 阶段把 prefill reserve 借给 KV pool，并在下一 prefill 前回收；机制能安全工作，但对照发现降低 `max_num_batched_tokens` 往往回收更多 KV、TTFT 差异约 1%，且 reserve 随 TP 增大而稀释。该负结果改变设计顺序：先测简单 chunked-prefill baseline，再为剩余窗口引入动态 VMM。建议 Ch54 吸收这一 alternative/evolution，而非只记录新 allocator。

### [Memory-Sovereign Inference](https://arxiv.org/abs/2608.23805)

论文区分 representation、semantic demand、scheduler request 与实际 traffic，并明确 RSS、page cache、board-wide memory 各自由谁计量；异步路径的 exactness 只覆盖预先声明的 64-token/logit/route horizon。结果绑定单一主实验模型、设备和 runtime，不能证明 recurrent/upstream state 完全相等。建议 Ch54 把资源 authority、reuse transition、fault cell 与 exactness horizon 作为 storage-backed inference 的发布证书。

### [Serving Masked Diffusion LLMs](https://arxiv.org/abs/2608.23807)

LLaDA-8B + D2F LoRA 在单 H200、GSM8K/HumanEval 上呈现离散 denoising step level、低可预测性和显著 CPU dispatch；batching 的主要收益是共享每个 denoising step 的一次 forward，而非 AR token queue 的简单移植。短 output budget 会遮蔽方差，质量不随 batch 变化还依赖作者列出的独立性假设。建议 Ch24 补充 dLLM serving contract，并 handoff Ch46 的 batching owner。

### [Minima-KV](https://arxiv.org/abs/2608.23834)

Minima-KV 保留每个 live logical page 的可寻址性，只把 recent/anchor 置于 FP8、stale 置于 TQ3，并用 format-specific kernel 的全局 online-softmax 合并避免 cache-sized dense shadow。作者主动分开 accounting、quality 和 single-pair throughput profiles；硬件只是一张 96GB Blackwell，部分 byte/dtype 记录未完全绑定。建议 Ch45 吸收 fidelity/retention 分离，Ch47 只承载 mixed-format page mapping。

### [Pipeline-Native Transformers](https://arxiv.org/abs/2608.23841)

这一路线不是单独换 kernel，而是改变 inter-layer dependency，使 CPU runtime 能以 vertical stage-major 顺序复用 L2-sized weight tiles，并只流过 top-k experts。TinyStories 与 30.9B CPU/disk-tier结果支持 bandwidth co-design 的可能性，但不能外推主流 GPU、模型质量或任意 MoE。建议 Ch49 作为受限 architecture/runtime branch，保留传统 layer-major 路径用于模型不可重训或 GPU compute-bound 场景。

### [Data Mixing as Mixture Experiment](https://arxiv.org/abs/2608.23922)

工作将 domain share 视为 simplex 上的 mixture components，以 sparse second-order Scheffé surface 表达 pairwise interaction，再用 model-robust I-optimal design选择 proxy runs。RegMix case 与校准 simulation 说明弱 additive domain 可能因交互变得有价值，但不证明跨 tokenizer/scale 的固定最优 mixture。建议 Ch27 在自动 controller 前补上 experiment-design identity、interaction term 与 scale-transfer check。

### [More Rejective, Not More Discriminative](https://arxiv.org/abs/2608.23941)

作者用只差一个 environment-accepted write 的 clean/error twin，在五种 nested review length 下隔离 verification unit；窗口增长同时提高 catch 和 false rejection，informedness 在受测六个 judge、两个 domain 中于一至两步附近最好。它不证明短窗口普遍最优，而证明安全 case 必须冻结 review unit 并报告 clean control。建议 Ch66 将 catch-only 指标升级为 paired informedness contract。

### [WebMCP-Phalanx](https://arxiv.org/abs/2608.24017)

系统以 capability credential 绑定 web tool 与 registering principal，再让无执行权的 Q-LLM 检查 metadata/output，P-LLM 才能调用。适应性攻击利用恶意 tool name 在检查前触发调用，说明 provenance 与 semantic filtering 均不能替代 call-timing/effect-time gate。建议 Ch83 吸收 browser tool lifecycle 与 quarantine handoff，最终 authorization 仍由 Ch72 owner 决定。

### [Maia 200](https://arxiv.org/abs/2608.24664)

厂商论文提出 software-defined locally accessed dataflow，以显式可编程 dataflow/memory-movement engine 代替 thread-centric 执行。公开正文可支持架构机制与 placement/data-movement 思路，但 10,145 TFLOP/s FP4、7 TB/s HBM、750W 等规格和节能结论均是厂商披露，未构成跨系统优势证明。建议 Ch49 只把它作为 execution-plan 与 accelerator co-design 的受限案例。

### [Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining](https://arxiv.org/abs/2608.24814)

论文观察到多个 LR 与 parameter-norm 组合只要 `ELR = LR / ||theta||` 匹配，loss trajectory 就高度重合，并用 optimizer、architecture、dataset、scale 与 norm-control ablation 检查边界。collapse 仍受 normalization design 和 LR/norm 变化时间尺度限制，不能把单一标量当作所有 layer 的充分优化状态。Ch28 已在 layer-wise trust/update 主干前加入 ELR coordinate，并保留何时仍需 group/layer-specific scale 的边界。

### [RENDER: Controlling Reader-Facing Evidence in LLM Memory Evaluation](https://arxiv.org/abs/2608.23568v1)

固定 memory history 后，仅改变给 evaluator 看的 rendering 就让受测分数变化 24.6～48.8 个百分点，说明 memory object 与 reader-facing artifact 不是同一身份。数值只适用于作者任务/model/harness，不证明任意 rendering 都会同幅影响；Ch77 已把 projection 纳入 memory evaluation contract。

### [When May an Agent Stop?](https://arxiv.org/abs/2608.23623v1)

方法在 COMPLETE 边界附带 typed evidence certificate，并以故障注入检查证据链是否支持终止。证书只证明已记录 trace 满足声明谓词，不证明外部事实真实或任务目标完整；Ch81 已以 completion admission 与 evidence certificate 替代模型自报完成。

### [Callability Is Not Operability](https://arxiv.org/abs/2608.23628v1)

受控接口干预显示 effect 已提交但 response 丢失时，重试可能重复不可逆动作；只有 schema 与 endpoint 可调用不足以安全运行。lifecycle/postcondition 查询增加服务实现和状态保留成本，幂等 tool 仍可走简单路径；Ch78 已承载 operability state machine。

### [ToolRobustBench](https://arxiv.org/abs/2608.23635v1)

15,456 个受控实例在多个 tool stage 注入扰动，output/observation failure 是受测系统的主要瓶颈，混合错误呈非加性。数据不证明生产故障分布；Ch66 已有 stage-wise fault matrix、trace 和 repair-scope attribution。

### [Feedback That Backfires](https://arxiv.org/abs/2608.23651v1)

小模型 Agent 在看到失败 call 的原始 transcript 后更易重复同一 action，而自然语言规范化反馈可消除多数重复。结果受模型和 tool task 限制；Ch78 已将 error representation 纳入 retry state，而非把失败文本原样回灌。

### [AgentRoom](https://arxiv.org/abs/2608.23740v1)

CRDT-backed workspace 让多个 coding agents 可并行编辑共享 artifact，并显式暴露 conflict/merge/verification owner。它减少文本聊天协调，却增加 CRDT semantics 与最终验证成本；Ch82 已把并发执行与正确合并分开。

### [ShardMeter](https://arxiv.org/abs/2608.23840v1)

工具联合模型 state、GPU memory、link bandwidth、island 与 geo failure domain 估计 sharding operating point。作者结果依赖其 cost model 和拓扑输入，不证明自动选择对未知集群最优；Ch36 已承载 estimator、measurement revision 与 fallback。

### [PuzzleKV](https://arxiv.org/abs/2608.23843v1)

方法在 logical page 内维护 low-rank factors，使 compression、append 与 decode 都围绕可寻址 page 生命周期运行。结果不支持跨模型统一 rank 或无损结论；Ch45 已绑定 page identity、rank metadata 与 reconstruction kernel，并 handoff Ch47 的物理映射。

### [Beyond the Mandate](https://arxiv.org/abs/2608.23858v1)

AP2 威胁分析将 mandate、delegation、payment authorization、merchant response 与 settlement 分开，指出 protocol compliance 不等同 end-to-end safety。它是设计分析而非生产攻击率证明；Ch72 已承载 payment side-effect 的独立 commit owner。

### [Semantic Overlays](https://arxiv.org/abs/2608.23873v1)

overlay 将网页片段的 trust/provenance 标签置于普通 token 之外，让模型内容与 policy metadata 不再共享同一可注入文本通道。overlay 生成器若被欺骗仍会误标，且不能替代 effect-time authorization；Ch72 已承载该 taint representation 分支。

### [Paritok-4B](https://arxiv.org/abs/2608.24188v1)

intent-conditioned extractive compression 为 coding task 保留 identifier、path、edit 与局部证据，而不是统一摘要全部历史。它以 task-intent classifier 和不可恢复删除换 context 预算，意图漂移时必须回退 raw evidence；Ch75 已补入这条 projection 分支。

### [MemUse](https://arxiv.org/abs/2608.24189v1)

评测不再直接询问已存事实，而检查长期会话中是否在适当时机自然使用且不越界泄露。受测 dialogue 与 judge 只支持其 protocol，不是真实用户满意度；Ch77 已补入 recall、utility 与 overuse 三分评价。

### [WiCi: Wireless GPU Computing Infrastructure](https://arxiv.org/abs/2608.24204v1)

系统把移动设备 inference 请求与 state 发送到邻近 GPU，目标是在本地资源不足时保留交互延迟。收益取决于网络、model transfer、privacy、availability 与兼容性，不能外推所有 edge；Ch55 已将它定位为 remote-compute branch，而非 PD 的同义替换。

### [Can a Dynamic Internal Field Govern a Transformer's Cognition?](https://arxiv.org/abs/2608.24319v1)

论文为 adaptive compute field 的动态稳定性给出可检查条件，同时明确没有证明能力优于固定 compute。该证据只支持 runtime 不发散的 certificate；Ch56 已把 stability、task quality 与 SLO 分成三个 Gate。

### [Thermal Tuning Overhead in Wafer-Scale Optical Interconnects for LLM MoE Training](https://arxiv.org/abs/2608.24637v1)

跨层 proxy simulation 显示 MoE traffic 可触发 optical tuning/thermal stall，使名义 bandwidth 无法直接转化训练 step time。它没有真实 wafer-scale 端到端训练证明；Ch37 已仅吸收 physical control-loop cost 与验证要求。

### [The Invisible Editorial Layer](https://arxiv.org/abs/2608.24662v1)

形式化结果说明相同 weights 经不同 inference-time policy 可产生不可区分的外部行为分布，黑盒观察不能唯一归因模型本体。它不量化现实厂商使用频率；Ch66 已把 model、system prompt、router、sampler 与 safety policy 共同纳入 subject identity。

### [Confident at the moment of action](https://arxiv.org/abs/2608.24691v1)

隐藏信息游戏中，模型在 action 时的 verbal confidence 与内部 belief quality、最终 outcome 会错配。作者任务不代表开放世界，但支持把 belief calibration、action choice 与 outcome 分开；Ch66 已加入这一三层测量。

### [LAION-BVD](https://arxiv.org/abs/2608.24845v1)

作者公开 10M-hour 视频集合的采集、过滤、去重与合成 caption 流程。它证明数据资产及披露 pipeline，不证明数据规模本身带来模型能力或不存在版权/内容偏差；Ch27 已承载 multimodal provenance 与 hour-scale duplication contract。

### [BrowserForge](https://arxiv.org/abs/2608.24848v1)

并行 browser sandboxes 扩展 web episodes，并要求 environment image、seed、network snapshot、credential 与 cleanup 可复现。其任务成功率受网站版本和 simulator fidelity 限制；Ch84 已承载 browser environment lifecycle。

### [Recursive Experiential-Working Memory Evolution](https://arxiv.org/abs/2608.24876v1)

方法分离当前任务 working memory 与跨任务 experiential memory，并只把经评价的经验递归晋升。自动 evaluator 会放大污染且 promotion 可能不可逆；Ch77 已承载 admission、version、quarantine 与 rollback。

### [What FID Hides](https://arxiv.org/abs/2608.24881v1)

论文展示相同或相近 FID 可隐藏不同 deviation 类型与排序，提出分离 detection、ranking、diagnosis 的替代度量。它不证明新指标在所有生成模态更好；Ch66 已吸收 metric decomposition 与 counterexample slice。

### [Latent Action as Intention Enables Efficient Future Imagination for World Action Models](https://arxiv.org/abs/2608.24882v1)

latent action 在不生成完整高维 observation 的情况下保留未来 rollout 的控制意图，形成 latency/generalization trade-off。证据只覆盖作者 World Action Model 和任务，latent interface 也可能丢失物理细节；Ch25 已将其作为 action-conditioned imagination 的受限分支。

### [What Guides the Agent? Adjudicating Unauthorized Behavior via Localizing Behavior-Guiding Instructions](https://arxiv.org/abs/2608.24022v1)

AttnLocate 将真正影响 tool-calling decision 的 context span 作为 attention-feature 上的一维检测对象，再按 provider authority 做 adjudication。五个模型家族、十种 Agent 配置的结果只证明该 sensor 在受测攻击上可迁移，不能把 attention localization 当作最终权限；Ch72 已保留 sensor 与 reference monitor 的分工。

### [Observability and Fault Injection for LLM-Based Multi-Agent Systems in Software Engineering](https://arxiv.org/abs/2608.24271v1)

llmmas-otel 用 OpenTelemetry 将 workflow phase、agent step、通信、tool call 和 LLM invocation 对齐，并允许在同一 interaction point 注入故障。初步验证只有 demo 与一个软件工程系统，不能证明通用诊断效果；Ch67 已拥有 trace context、故障对照和 run artifact 的观测合同。

### [FARCA: Fact-Aligned Reliability-Aware Credit Assignment for Reinforcement Learning with Factual Supervision](https://arxiv.org/abs/2608.24350v1)

FARCA 将事实判断对齐到 token-level credit，并以 counterfactual evidence dependence 作为 verifier reliability proxy 调节 reward 和 advantage。多个 factual reasoning benchmark 支持该分层，但 proxy 仍可能与真实可靠性错配；Ch33 已将 verifier direction、reliability 与 update granularity 分开。

### [When Do Supervised UQ Ensembles Improve LLM Hallucination Detection? A Robustness Study](https://arxiv.org/abs/2608.24492v1)

作者在四个 LLM、九个数据集和三种 generation regime 下研究监督组合 UQ signals，并报告小样本与部分域迁移的条件收益。它只做 closed-book hallucination classification，不能提供事实证据或开放世界 truth confidence；Ch66 已把 UQ ensemble 定位为需校准、需监测迁移的 sensor。

### [Joint Optimization of Tool Creation and Use for Large Language Model Agents](https://arxiv.org/abs/2608.24571v1)

SMITH 在同一 policy 中交替训练 tool build 与 held-out use，并以 schema、code 和 outcome 三条 reward 轴分别归因失败。13 个 procedural task 的结果不证明生成工具可直接安全上线；Ch78 已以 schema validation、artifact isolation、execution sandbox 与 outcome verifier 承载该生命周期。

### [Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency](https://arxiv.org/abs/2608.23831v1)

ARLI 把 inference 期间已经 committed 的 action 与 mid-inference observation 写回 RL state，修复异步 VLA 执行使环境转移不再近似 Markov 的问题。模拟与有限真实 manipulation 支持该机制，不证明任意 latency 可被 state augmentation 消除；Ch26 已加入 action queue、observation timestamp 与 latency-aware policy handoff。

### [TRACE: An Evidence-Grounded Benchmark for Safety Evaluation of Large Reasoning Models](https://arxiv.org/abs/2608.24232v1)

TRACE 将 prompt、reasoning trace 与 final answer 分别标注风险，并为每个 judgment 绑定 source-text evidence，以暴露“最终回答安全但中间推理不安全”的漏测。两种语言、九类风险和 18 个 guardrail model 仍是有限 slice；Ch66 已加入 reasoning-trace evaluation unit 与 evidence-localization 责任边界。

### [PeakBench: Benchmarking Resource-Aware Tool Invocation in LLM Agents](https://arxiv.org/abs/2608.24509v1)

PeakBench 以 executable dependency annotation 与 measured resource profile 分离 logical planning 和 physical scheduling，显示逻辑正确并不保证并行执行不会溢出资源。benchmark 的资源模型不等同生产 scheduler；Ch81 已把 DAG validity、capacity admission、schedule execution 和 overflow attribution 分成连续 Gate。

### [When “Must” Becomes “Maybe”: Constraint Weakening in LLM Agent Workflows](https://arxiv.org/abs/2608.24569v1)

1,296 个受控 episode 显示摘要、计划同化与 handoff 能保留 blocker 文本，却把 prerequisite 从 action-binding state 弱化成普通 caveat。合成环境不提供生产故障率，但直接证明 semantic availability 不等于 operational preservation；Ch81 已要求 authority、fallback、execution consequence 和下游 containment 可独立验证。

### [Evidence Blindness in Direct Corpus Interaction: Persistent Navigation with AtlasNav](https://arxiv.org/abs/2608.24764v1)

AtlasNav 将有限预算下的 evidence realization 分为 surfaced、opened 与 decisive-fragment exposed，并以一次构建的 persistent corpus atlas 代替每次查询在线重建结构。BrowseComp-Plus、PhantomWiki 与企业语料结果不证明所有 corpus 都适合相同索引；Ch76 已把可访问性、导航状态、证据实现和最终 sufficiency 分离。

## 5. 缺口与下一步

无

503 个唯一身份已经按完整题目与摘要完成语义准入，最终分母为 55；55/55 均已完成 exact-v1 HTML/PDF、机制、评价、限制与 withdrawal 核验，当前页面未见 withdrawn 标记。最终处置为：29 项已有覆盖，26 项完成 Books 整合，没有仅报告或待审项。其余身份以范围外、单领域应用、局部指标改进或重复现有长期命题等具体理由在分母前关闭。

此前漏失的 10 项已经全部恢复到候选表与 Source Review。智谱 Research 页的 `GLM-5.3-Flash` 事件为 `2026-08-26T14:00:00Z`（北京时间 22:00），归属 08-27 Daily，不扩张本窗；当前没有待补材料、待审证据或待写 Books 条目。

## 6. 复核

复核者：fresh-context 独立智能体
结论：通过

独立回放确认窗口为 `2026-08-25 09:00～2026-08-26 09:00`（Asia/Shanghai），503 个 arXiv 唯一身份按 official-announcement owner 归属本日；55 个候选均属于该批次，表格与 55 个 Source Review 一一对应，V2 加总和审阅路由一致。55/55 的 exact-v1 HTML 或 PDF 可访问，未见 withdrawn 标记。`2608.24115` PonderPounce 与 `2608.24214` MetaRAG 不在本日批次，未被错误纳入；`2608.24070` Compression Trinity 没有独立于既有组合压缩结论的新 canonical 机制，分母前关闭合理。

false-negative 复核恢复了 10 项；false-positive 复核将 12 个重复写作建议降为已有覆盖。26 个 `Integrate` 均在正确 canonical owner 的机制正文中形成可定位的 Why/Mechanism/Trade-off/Evidence boundary，29 个 `Existing Coverage` 也逐项回到现有具体命题，没有用抽象 owner 名称替代对读。

本日报的来源、候选分母、证据、Books 写回与写后语义审计均已闭合。
