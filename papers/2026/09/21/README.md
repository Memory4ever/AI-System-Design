# Daily Research — 2026-09-21

**规范：** V3
**窗口：** 2026-09-20T09:00:00+08:00 ～ 2026-09-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T13:44:41+08:00

## 1. 结论

本窗最终冻结142个唯一材料家族（136 arXiv、6机构）：116深入完成、24标准完成、2中心争议精确隔离；Books为112实际整合、26具体已有覆盖、2仅报告、2暂缓。单篇必要证据、采用判断和必要实际段落/邻接非作者写后已齐；扫描/筛选/证据/Books与独立复核普通待办0，sep22_resume_v3已于2026-10-01T13:42:53+08:00完成非作者日级Gate并通过，不由作者自签。原134摘要计数108/24已按真实§3纠正为109/23；不是改评分/审阅或采纳命题。

主要变化集中于证据身份与实际消费、训练/部署分工、生成/验证/提交分离，以及硬件执行与资源收益的成立条件。Qwen mixed-mask cache与MoonEP冗余预取保留已有效正文；本轮把同任务历史与实际状态、派生几何与物理执行、teacher credit与真值、量化/融合与完整请求收益的缺口落在各自唯一owner，不给局部实验普遍安全、无损或SLO权限。26项已有覆盖仅绑定具体已承载命题，不声称整个recipe已写入；TinyCeNN/MDL局部配方仅报告。SURE效率项与优化解释、CaLR penalty/update mask各有中心冲突，不正面采用。

官方Mon21标签对应09/20 20:00 EDT=09/21 08:00北京时间，落在本窗；十二分类475个去重New/Cross身份是有界查漏库存，不是逐项全文队列。原‘周末无公告/arXiv0’已纠正。139 working信号的完整题摘具体贡献分流、首批及后续有限独立校准完成；最后6个具名负侧样本发现4误关，只重开21953/21629/21749/21259后补足必要机制/反证及实际处置，不扩475、不按保留率接受。来源/日期保留范围仍不支持零遗漏。身份、原准入/改判与证据链见[题摘判断](../_sources/daily-20260921/arxiv-title-abstract-screening.md)和[唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 官方目录按窗口检查；最近可见发布早于窗口 | 已检查 | 无当窗候选 |
| SRC-ANTHROPIC | Research 官方目录按窗口检查；最近可见条目为 09-17 | 已检查 | 无当窗候选 |
| SRC-GOOGLE-AI | Google DeepMind publications 与 Google Research 官方入口按窗口定点检查 | 已检查 | 动态目录不提供可复算的完整时间增量；结论限于可见官方卡片与窗口查询 |
| SRC-META-AI | Meta AI/FAIR Research 官方目录按窗口检查；最近可见研究条目早于窗口 | 已检查 | 无当窗候选 |
| SRC-QWEN | Qwen 官方文章与明确研究 artifact；保留 Qwen-Image-2.1 与 RecreationWorld | 已检查 | Qwen-Image-2.1 博客仅给日级日期，窗口归属由仓库 Atom 的窗内 artifact activity 锚定 |
| SRC-DEEPSEEK | 官方 Research/News 入口按窗口检查 | 已检查 | 无当窗候选 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 明确发布事件；保留 MoonEP public release | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Hunyuan Research 与官方仓库的明确发布/契约事件；普通 UniRL 活动不扩池 | 已检查 | 无当窗候选 |
| SRC-ZAI | 官方 Research/release 与 ZCode 开源事件 | 已检查 | ZCode 在候选前关闭 |
| SRC-BYTEDANCE-SEED | Seed Research、论文目录与明确仓库发布事件 | 已检查 | 无当窗候选 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客与明确研究/发布事件 | 已检查 | 无当窗候选 |
| SRC-XIAOMI-MIMO | MiMo Paper/Blog 与 MiMo-Code 契约级事件；普通 main 活动不扩池 | 已检查 | 三个合并后的 contract Source Family 保留；provider prompt family 因官方提交已删除而排除 |
| SRC-MINIMAX | Research/Blog 与明确 artifact/release；记录 MiniMax-Code-MiniApps 初始公开 artifact | 已检查 | MiniApps 在候选前关闭 |
| SRC-ARXIV | 十二分类official recent Mon21 New/Cross目标组全读至末，09/21 08:00北京时间落窗，去重475身份；按合同主线有界题名/完整题摘处理并完成136 arXiv家族处置 | 已检查 | 历史Replacement原批次未恢复、12748v2公告日期隔离；只支持已处理的有限New/Cross主题面，不声明无修订或全网零遗漏 |

机构入口/实际停止点与原快照边界见 [screening ledger](../_sources/daily-20260921/screening-ledger.md)。这些记录支持“合同定义的发现面已处理”，不支持“互联网或各组织所有页面绝对没有其他活动”的强断言。

## 3. 候选与判断

评分顺序为 Design Delta / System Reach / Durability；按唯一Source Family归并，公开时刻依据官方批次而非Submitted。评分对象仅原文新增且拟支持的命题；真实长期差额、安全/纠错受影响范围深入，不以评分强造Books diff。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Qwen-Image-2.1](https://qwen.ai/blog?id=qwen-image-2.1) | 2026-09-20T10:25:10+08:00 | mixed-granularity attention 下 condition prefix 跨 denoising step 复用；2 + 2 + 3 = 7 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)（已落实） |
| [RecreationWorld](https://github.com/QwenLM/RecreationWorld) | 2026-09-20T17:50:10+08:00 | 以冻结 reference artifact 和 programmatic + visual assertions 验证跨平台 computer-use 重建；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MoonEP public release 26/09](https://github.com/MoonshotAI/MoonEP/commit/33327eb9c4a8c95a158c3417d5e15ed2311a5849) | 2026-09-20T12:48:05+08:00 | 在线冗余专家预取、固定 receive shape、zero-copy permute 与 home-rank gradient ownership；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)（已落实） |
| [MiMo Code：MCP host-owned admission](https://github.com/XiaomiMiMo/MiMo-Code/commit/e95db7a80004edfe23617ed2160ff6db8163efef) | 2026-09-20T15:49:22+08:00 ～ 2026-09-20T21:35:15+08:00 | 把 host revision、异步 connect/auth identity、commit-before-release 与 in-flight presentation 变成显式状态合同；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-MCP` [Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [MiMo Code：session admission and bounded retry](https://github.com/XiaomiMiMo/MiMo-Code/commit/1592084b2e1fa64dc5a115708d0b5124bb9a3581) | 2026-09-20T16:02:21+08:00 ～ 2026-09-20T23:52:40+08:00 | exclusive resume admission、orphan-part terminalization 与 phase-sensitive bounded retry 共同维护 session state authority；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [MiMo Code：skill external-root boundary](https://github.com/XiaomiMiMo/MiMo-Code/commit/1a7a7478f58f8123d5cb5cf5abae688e5599e078) | 2026-09-20T16:58:32+08:00 | 将默认 discovery surface 收窄为 MiMoCode + `.agents`，brand roots opt-in，并排除 dotted private namespaces；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [HE-Guardrail v1](https://arxiv.org/html/2609.21484v1) | 2026-09-21T08:00:00+08:00 | 密文response/refusal选择引入近似gate残余与gated-noise边界；2 + 2 + 2 = 6（保护约束深入例外） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) `隐私不是一个开关`（已落实，非作者写后通过） |
| [ServeGuard v1](https://arxiv.org/html/2609.21515v1) | 2026-09-21T08:00:00+08:00 | 指定monitor的blind-space confinement、结构证明与admitted-byte检查分工；2 + 2 + 2 = 6（保护约束深入例外） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) `从文件哈希到可执行来源链`（已落实，非作者写后通过） |
| [MintAct v1](https://arxiv.org/html/2609.22083v1) | 2026-09-21T08:00:00+08:00 | mixed-group后的有效domain贡献、消费quota与生产admitted-count/q背压分权；2 + 2 + 2 = 6（长期缺口深入例外） | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) mixture control段后（已落实，非作者写后通过） |
| [Reviser: Revision-Capable Text Generation via Autoregressive Cursor Actions](https://arxiv.org/html/2609.20830v1) | 2026-09-21T08:00:00+08:00 | 动作历史trunk与可变text canvas分开，revision不是append-only输出；2 + 2 + 2 = 6（长期缺口深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)（既有实际正文，root必要源/写后通过） |
| [How Much of a Real Workload Can LLM-Generated GPU Kernels Actually Reach?](https://arxiv.org/html/2609.21058v1) | 2026-09-21T08:00:00+08:00 | wall-clock addressable fraction与相对数值/完整写入纠正kernel采用；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)（既有实际正文，root必要源/写后通过） |
| [DLB: Distributed Load Balancing at Scale for Generative AI Inference](https://arxiv.org/html/2609.21079v1) | 2026-09-21T08:00:00+08:00 | P2P probing/在线latency model与异构多阶段routing分权；2 + 2 + 2 = 6（长期缺口深入） | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)（既有实际正文，root必要源/写后通过） |
| [Decomposing Predictive Kubernetes Autoscaling for Large Language Model Serving Under Long Startup Delays](https://arxiv.org/html/2609.20874v1) | 2026-09-21T08:00:00+08:00 | delay lookahead/token需求/margin与预测器分因素控制，复杂预测器局部不占优；2 + 2 + 2 = 6（长期缺口深入） | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) cold-readiness之后（已落实，root写后通过） |
| [Reading Less While Writing: A Closed-Form Bandwidth Dial for Streaming Multimodal Decoders](https://arxiv.org/html/2609.20845v1) | 2026-09-21T08:00:00+08:00 | 单调可见prefix日程区分fixed全输入head/stream arrived-prefix与runtime授权；2 + 2 + 2 = 6（长期缺口深入） | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) Streaming Identity首段后（已落实，root写后通过） |
| [Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding](https://arxiv.org/html/2609.20888v1) | 2026-09-21T08:00:00+08:00 | soft logit gate的exp0floor与hard support不等价，理论界/quantile surrogate/实际block union分开；3 + 2 + 2 = 7 | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) Sparse Support之后（已落实，root写后通过） |
| [Quantization-Aware Kalman Estimation for Diffusion Sampling](https://arxiv.org/html/2609.21407v1) | 2026-09-21T08:00:00+08:00 | 同quantized latent处估FP输出window并联合修history交solver，不是原FP整轨迹；2 + 2 + 2 = 6（长期缺口深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) reverse-covariance之后（已落实，root写后通过） |
| [Enhancing Audio Reasoning via Semantic Summary Prediction](https://arxiv.org/html/2609.20849v1) | 2026-09-21T08:00:00+08:00 | train-only final-answer register监督/部署撤aux与音频grounding因果分开；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) PEARL实际承载train-only目标与撤aux不证真实执行（root独立通过）；局部REG recipe仅报告 |
| [TinyCeNN-LM: Quality-Gated Conversion of Pretrained Attention with CeNN-Inspired Cellular-Recurrent Layers](https://arxiv.org/html/2609.21139v1) | 2026-09-21T08:00:00+08:00 | 当前student逐层替换与已测NLL/局部表示门不等价；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部四阈值转换未建立新的质量/运行选择边界；不抹除已测诊断 |
| [DiaVLo: Diagnosing Behaviours of Vision-Language Models](https://arxiv.org/html/2609.22008v1) | 2026-09-21T08:00:00+08:00 | scene reference与self-rationale分离，干预估计不授予内部真值；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 权威provenance/self-report与rationale≠真实链（root通过）；非全诊断recipe |
| [An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency](https://arxiv.org/html/2609.22043v1) | 2026-09-21T08:00:00+08:00 | heuristic几何与semantic reliability分离，整体/risk-weighted hallucination方向不同；2 + 1 + 2 = 5 | 标准完成 | 仅报告：未校准四action配置不建立可迁移控制条件；提取预算及残余保留 |
| [The Weight Is Over - Interactive Diffusion on Consumer GPUs](https://arxiv.org/html/2609.21849v1) | 2026-09-21T08:00:00+08:00 | 非critical encoder影响denoiser working-set fit，减容量可避分页cliff而全fit streaming更慢；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) expert residency后/occupancy前两段（实际写后root通过） |
| [CodeMidas: Scaling Agentic Coding RL Environments from Code Itself](https://arxiv.org/html/2609.22068v1) | 2026-09-21T08:00:00+08:00 | source-only任务来源分离public行为scope/reference与private assertion权限；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) repository fail→pass后/Builder前两段（root实际写后通过） |
| [Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models](https://arxiv.org/html/2609.21113v1) | 2026-09-21T08:00:00+08:00 | drift/readout、局部干预重要性与跨task transfer不可互推；3 + 1 + 2 = 6（设计反证深入） | 深入完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 表示/干预/跨任务分账（sep22独立通过）；非全EAP配方 |
| [Accelerating Dense LLMs via L0-regularized Mixture-of-Experts](https://arxiv.org/html/2609.21672v1) | 2026-09-21T08:00:00+08:00 | 独立expert形成、shared interface与token-router/部署domain语义分开；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) formation/router exposure与deployment合同（sep22独立通过）；非全L0/CCM配方 |
| [When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success](https://arxiv.org/html/2609.21187v1) | 2026-09-21T08:00:00+08:00 | gold-history下一步能力不等自主建立/维持workflow历史；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) isolated/cumulative与合法替代路径分账（sep22独立通过） |
| [Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models](https://arxiv.org/html/2609.20846v1) | 2026-09-21T08:00:00+08:00 | 正效率奖励公式与立即停解释方向冲突；2 + 1 + 2 = 5（受影响纠错深入） | 争议 | 暂缓：仅中心process效率因果机制，不正面采用Books；Table1局部经验保留，root独立冲突核通过 |
| [LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers](https://arxiv.org/html/2609.21492v1) | 2026-09-21T08:00:00+08:00 | 自动前提忠实性/solver有效性及force-forward未决标签分权；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`AGENT-REFLECTION` [Ch80](../../../../books/part-07-agent/80-reflection.md) feedback表后两段，root实际写后通过 |
| [OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue](https://arxiv.org/pdf/2609.21465v1) | 2026-09-21T08:00:00+08:00 | accepted render参考≠script，fixed history≠live执行；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)（sep22独立窄E通过，非全recipe） |
| [Can Small Language Models Know What They Don’t Know? Semantic Entropy as a Confidence Signal for Sub-3B Parameter Models](https://arxiv.org/html/2609.20824v1) | 2026-09-21T08:00:00+08:00 | entropy feature≠校准正确率，低熵一致错不授resolver真值；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（sep22独立窄E通过，非全recipe） |
| [VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models](https://arxiv.org/html/2609.21246v1) | 2026-09-21T08:00:00+08:00 | shift gate与有限horizon failure risk分账；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（sep22独立窄E通过，非全recipe） |
| [Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies](https://arxiv.org/html/2609.21659v1) | 2026-09-21T08:00:00+08:00 | 位置几何相近≠任务质量/grounding或policy互换；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（sep22独立窄E通过，非全recipe） |
| [When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap](https://arxiv.org/html/2609.21662v1) | 2026-09-21T08:00:00+08:00 | 可读、局部表示位移、下游语言控制分账；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)（sep22独立窄E通过，非全recipe） |
| [GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions](https://arxiv.org/html/2609.21562v1) | 2026-09-21T08:00:00+08:00 | 途中invariant/终局与正确接受/错误拒绝两侧oracle分权；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（sep22独立窄E通过，非全recipe） |
| [Evolving Procedural Memory from User Traffic for Agentic Graphic Design](https://arxiv.org/html/2609.22086v1) | 2026-09-21T08:00:00+08:00 | 更新提案与晋升分权，matched局部证书不授权全流量；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)（sep22独立窄E通过，非全recipe） |
| [FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision–Language–Action Models](https://arxiv.org/html/2609.21228v1) | 2026-09-21T08:00:00+08:00 | 训练teacher/future target与部署当前条件、aux通路分开；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（sep22独立窄E通过，非全recipe） |
| [DRT: Dense Reasoning Trace for Efficient and Grounded Multimodal Reasoning](https://arxiv.org/html/2609.21675v1) | 2026-09-21T08:00:00+08:00 | typed过程压缩与错误答案reference partial credit分开格式/grounding权限；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 实际207/209两段（root必要源/写后通过） |
| [Brain API: An Intent-Aware Control Plane for Policy-Governed Agentic Systems](https://arxiv.org/html/2609.21299v1) | 2026-09-21T08:00:00+08:00 | 跨backend default polarity、per-element guard scope与supported fragment不能字段重命名；3 + 2 + 2 = 7 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) 实际711/713两段（root必要源/写后通过） |
| [Boosting Deepresearch and LongContext Ability with Self-Generated Deepresearch Rollouts Traces](https://arxiv.org/html/2609.20844v1) | 2026-09-21T08:00:00+08:00 | 工具rollout→无tool LongQA转换需展开页面与failed补证lineage；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) 实际432/434两段（root必要源/写后通过） |
| [MT-WAM: Reorienting the One-Pass Predictive Representation Toward Action Generation](https://arxiv.org/html/2609.21474v1) | 2026-09-21T08:00:00+08:00 | 同一aux stream训练收益不授予部署action读取权，两种控制不可混同；2 + 2 + 2 = 6（实际缺口深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 实际293/295两段，root写后通过 |
| [SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation](https://arxiv.org/html/2609.21223v1) | 2026-09-21T08:00:00+08:00 | native success后观察窗口与first critical stage分账，成功不结束物理验收；2 + 1 + 2 = 5（实际缺口深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 实际763/765两段，root写后通过 |
| [CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution](https://arxiv.org/html/2609.21908v1) | 2026-09-21T08:00:00+08:00 | chunk内dependent动作hold/局部relation residual与fresh checkpoint复核分权；2 + 1 + 2 = 5（实际缺口深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 实际785/787两段，root写后通过 |
| [Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction](https://arxiv.org/html/2609.21392v1) | 2026-09-21T08:00:00+08:00 | source/addressee决定demand admission，negative false trigger与positive内容恢复不同分母；2 + 1 + 2 = 5（实际缺口深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 实际391/393两段，root写后通过 |
| [How Many Humans Is a Judge Panel Worth?](https://arxiv.org/html/2609.21277v1) | 2026-09-21T08:00:00+08:00 | spectral residual与distribution-recovery等效人数方向可反转；2 + 1 + 2 = 5（实际缺口深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 实际2410/2412两段，root写后通过 |
| [Verify, Don’t Trust: Agentic Model Development for Video Discovery Retrieval at Scale](https://arxiv.org/html/2609.21257v1) | 2026-09-21T08:00:00+08:00 | realized comparison treatment而非两个成功run决定科学比较准入；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 实际216/218两段，root写后通过 |
| [The Stochastic Shift: A New Evaluation Paradigm for Text-to-SQL with AI Operators](https://arxiv.org/html/2609.21133v1) | 2026-09-21T08:00:00+08:00 | 关系/AI语义分别验收且分解器须忠实性审计，整query EX可两侧误判；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 实际1118/1120两段，root写后通过 |
| [ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL](https://arxiv.org/html/2609.21378v1) | 2026-09-21T08:00:00+08:00 | tournament过程credit与skill utility只调节优化/写读proposal，不授因果真值；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 与 `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) 具体credit/admission合同（root独立通过），非整公式已有 |
| [OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems](https://arxiv.org/html/2609.21527v1) | 2026-09-21T08:00:00+08:00 | 相近baseline不等错误吸收/worker失效表现，quality最优不等resource效率最优；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) task/topology/error absorption与资源分账（root通过）；非四干预recipe |
| [An Approximate Queueing Model of LLM Inference Serving for SLO-Driven Autoscaling](https://arxiv.org/html/2609.20957v1) | 2026-09-21T08:00:00+08:00 | 用ITL校准decode capacity不等未来延迟target，mean occupancy proposal须实际SLO验收；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) capacity/iteration work与SLO权限分账（root通过）；三参数配方仅报告 |
| [Same World, Different Knowledge: When Isolated Audits Misjudge World-Model Repairs](https://arxiv.org/html/2609.21155v1) | 2026-09-21T08:00:00+08:00 | 同源错误使isolated repair排序反转；3 + 1 + 2 = 6（实际差额/受影响深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 实际68/70两段，root必要源/写后通过 |
| [Benchmarking World Models for Continual Learning on Compositional Tasks](https://arxiv.org/html/2609.22055v1) | 2026-09-21T08:00:00+08:00 | expert冻结不阻shared encoder漂移，保存/复用速度/新增容量分开；2 + 2 + 2 = 6（实际差额/受影响深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 实际165/167两段，root必要源/写后通过 |
| [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](https://arxiv.org/html/2609.21712v1) | 2026-09-21T08:00:00+08:00 | common ray字段不授common encoder，native grids与投影adapter分权；2 + 2 + 2 = 6（实际差额/受影响深入） | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 实际695/697两段，root必要源/写后通过 |
| [AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](https://arxiv.org/html/2609.21940v1) | 2026-09-21T08:00:00+08:00 | interaction归纳互补抽取schema前移写入，不须新增query router；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) 实际344/346两段，root必要源/写后通过 |
| [MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems](https://arxiv.org/html/2609.21533v1) | 2026-09-21T08:00:00+08:00 | 内容组合×消费格式排序反转，独立边际score丢配对交互；2 + 2 + 2 = 6（实际差额/受影响深入） | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) 实际273/275两段，root必要源/写后通过 |
| [Proxifield: Decentralized Multi-Agent Communication through Semantic Proximity](https://arxiv.org/html/2609.20889v1) | 2026-09-21T08:00:00+08:00 | 每round重建need/plan/complementarity通信图与effect commit分权；2 + 2 + 2 = 6（实际差额/受影响深入） | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) 实际230/232两段，root必要源/写后通过 |
| [Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision–Language Models](https://arxiv.org/html/2609.21363v1) | 2026-09-21T08:00:00+08:00 | 发布前高层视觉线索变换与refusal不同控制点，距离/utility独立验收；2 + 2 + 2 = 6（实际差额/受影响深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 实际212/214两段，root必要源/写后通过 |
| [RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models](https://arxiv.org/html/2609.20971v1) | 2026-09-21T08:00:00+08:00 | relativecut救援可能删base，两独立masks union保原候选；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) 实际284/286两段，root必要源/写后通过 |
| [Information-Gain Rewards over Diversity-Pruned Tests: GT-Anchored Verifier Co-Training for Reliable Code Generation](https://arxiv.org/html/2609.21208v1) | 2026-09-21T08:00:00+08:00 | test producer按GT锚定区分信息/cov gate训练，非passrate自证；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 实际485/487两段，root必要源/写后通过 |
| [Scaling Discovery through Test-Time Communication](https://arxiv.org/html/2609.21032v1) | 2026-09-21T08:00:00+08:00 | verified可转移连续进展共享与独立best-k不同，终态grader非忠实中间反馈；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) 实际97/99两段，root必要源/写后通过 |
| [Layerwise Decoupling for Stable Structured Sparsification of Fully Connected Layers](https://arxiv.org/html/2609.21126v1) | 2026-09-21T08:00:00+08:00 | 正齐次gauge改变单边结构惩罚，目标最优等价不授有限迭代轨迹；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 实际Ch49:458/460两段，root必要源/写后通过 |
| [On the Limits of Maximal Coding Rate Reduction for Out-of-Distribution Generalisation](https://arxiv.org/html/2609.21001v1) | 2026-09-21T08:00:00+08:00 | coding几何稳定不授label读出稳定，near/exact/support三反证分账；3 + 1 + 2 = 6（实际差额/受影响深入） | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 实际Ch5:131/133两段，root必要源/写后通过 |
| [Brownian Heads for Deep ReLU Representations: Activation Mass and the Cost of Same-Sample Selection](https://arxiv.org/html/2609.21422v1) | 2026-09-21T08:00:00+08:00 | 固定表示的conditional经验界不抵消same-sample representation选择成本；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 实际Ch5:143/145两段，root必要源/写后通过 |
| [Beyond Gaussian Worlds: Latent Geometry Matters for JEPAs](https://arxiv.org/pdf/2609.21656v1) | 2026-09-21T08:00:00+08:00 | intrinsic pair与density/embedding/慢谱几何相容提供非Euclidean恢复分支；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 实际Ch25:858/860两段，root必要源/写后通过 |
| [COAL-SQL: Coverage-Guided Augmentation and Failure-Driven Learning for Text-to-SQL Post-Training](https://arxiv.org/html/2609.20842v1) | 2026-09-21T08:00:00+08:00 | 结构覆盖与current-policy失败分权、全错教师监督/相对强化分流；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) Ch27:572–599/987–1007与Ch33:434–436；root必要源/actual通过 |
| [ForeTac-VLA: A Forecasting-Based Tactile-Vision-Language-Action Model for Contact-Rich Robotic Manipulation](https://arxiv.org/html/2609.20980v1) | 2026-09-21T08:00:00+08:00 | GTfuture→forecast线上action prefix需条件producer与误差交接；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) Ch26:285/287；root必要源/actual通过 |
| [Attention-Aware Routing: Coupling Routing and Attention in MoEs](https://arxiv.org/html/2609.20974v1) | 2026-09-21T08:00:00+08:00 | attention-history logits与router耦合、冻结参数不等行为冻结；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) Ch21:413/415；root必要源/actual通过 |
| [Recursive Language Models Generalize Out of Domain](https://arxiv.org/pdf/2609.20831v1) | 2026-09-21T08:00:00+08:00 | activeframe观测限定hypothesis，覆盖正确规则不保证选择；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) Ch5:86/88；root必要源/actual通过 |
| [When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation](https://arxiv.org/html/2609.20942v1) | 2026-09-21T08:00:00+08:00 | 受控recursive exposure的分布漂移与参数继承/真实质量分账；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) Ch27:334–355；root必要源/actual通过 |
| [WM-VS: Progress-Aligned World Models for Closed-Loop Visual Servoing](https://arxiv.org/html/2609.20892v1) | 2026-09-21T08:00:00+08:00 | 预测nextlatent须保存signed task-error，modelconsequence与真实onpolicy分权；2 + 1 + 2 = 5（实际差额/受影响深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) Ch25:271/273；root必要源/actual通过 |
| [CaLR: Causal Latent Revision for Robust Diffusion Reasoning](https://arxiv.org/html/2609.20981v1) | 2026-09-21T08:00:00+08:00 | teacher CTM约束latent revision的strictflow/optimalmemory中心论断待核；2 + 1 + 2 = 5（中心冲突受影响深入） | 争议 | 暂缓：central Eq4/14/15 mask方向冲突；精确隔离见§5 |
| [Voice-Light: A Full-Duplex Cascaded Voice Agent with Causal Turn-Taking and Speculative Generation](https://arxiv.org/html/2609.20995v1) | 2026-09-21T08:00:00+08:00 | 私有PCM候选晋升与客户端rendered ACK消费commit分权；2 + 2 + 2 = 6（实际差额深入） | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) Ch81:874/876；sep22必要源/actual通过 |
| [MAGIC: Marginal-Guided Compression with Optimal Transport for Efficient Visual Document Retrieval](https://arxiv.org/html/2609.21018v1) | 2026-09-21T08:00:00+08:00 | source winner-demand与balanced OT分别校准有限MaxSim索引；2 + 1 + 2 = 5（实际差额深入） | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) Ch76:369/371；sep22必要源/actual通过 |
| [Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs](https://arxiv.org/html/2609.21022v1) | 2026-09-21T08:00:00+08:00 | 慢planner near-final chunk→高频新视觉finaldenoise交接；2 + 1 + 2 = 5（实际差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) Ch26:1071/1073；sep22必要源/actual通过 |
| [Loopjacking: Hijacking Human-in-the-Loop Approval](https://arxiv.org/html/2609.21081v1) | 2026-09-21T08:00:00+08:00 | 审批表示与effect-time完整对象绑定的阳阴性验证；2 + 2 + 2 = 6（安全深入） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 2253–2263/2775–2785具体命题；sep22源/actual通过 |
| [Stiefel-AdamW: Geometry-Aware AdamW for Linear Factorization Blocks](https://arxiv.org/html/2609.21039v1) | 2026-09-21T08:00:00+08:00 | 约束行正交收束fixed-W尺度fiber，不授旋转不变或轨迹收敛；2 + 1 + 2 = 5（实际差额深入） | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) 169/171；sep22必要源/actual通过 |
| [Physically Based Rendering in the Latent Space](https://arxiv.org/html/2609.21054v1) | 2026-09-21T08:00:00+08:00 | 已知scene模拟生成signed VAE features，分scene残差与decoder角色；2 + 1 + 2 = 5（实际差额深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 817/819；sep22必要源/actual通过 |
| [Detecting Hallucination in LLMs: Tracing the Topological Signatures of Impaired Context Sharing](https://arxiv.org/html/2609.21096v1) | 2026-09-21T08:00:00+08:00 | attention topology是受model/label人口校准的诊断feature，非truth或causal correction；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1870–1885/1913–1919/1933–1947/2098–2133；sep22必要源/actual通过，仅该命题非全recipe |
| [A Multi-Engine Dataflow for MoE Decoding on Scratchpad-Based Tensor Accelerators](https://arxiv.org/html/2609.21137v1) | 2026-09-21T08:00:00+08:00 | 共享input格式与路由后private供给分权、异engine overlap及全图成本；2 + 2 + 2 = 6（实际差额深入） | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 894/896；root必要源/actual通过 |
| [TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](https://arxiv.org/html/2609.21172v1) | 2026-09-21T08:00:00+08:00 | decode前length proposal驱动exact/low-rank/full-flash位置预算，overflow不修旧SVD失真；2 + 2 + 2 = 6（实际差额深入） | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 728/730；root必要源/actual通过 |
| [Implicit Rule Induction with Test-Time Task Embeddings in ARC-like Tasks](https://arxiv.org/html/2609.21181v1) | 2026-09-21T08:00:00+08:00 | joint动executor可让latent失去可比坐标，task定位/execution两阶段分别验；2 + 1 + 2 = 5（实际差额深入） | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 81/83；root必要源/actual通过 |
| [I’ll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance](https://arxiv.org/html/2609.21183v1) | 2026-09-21T08:00:00+08:00 | 四种监督机会分开漏onset补发/history通知去重；2 + 1 + 2 = 5（实际差额深入） | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 741/743；root必要源/actual通过 |
| [SWE-Proof: Can Language Models Resolve Real-World Issues with Machine-Checked Proofs?](https://arxiv.org/html/2609.21190v1) | 2026-09-21T08:00:00+08:00 | 逐函数proof与整个issue行为覆盖/axiom/patch correspondence三外部接缝分权；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1585/1587；sep22_resume_v3必要源/actual写后通过 |
| [Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies](https://arxiv.org/html/2609.21216v1) | 2026-09-21T08:00:00+08:00 | 冻结few-step candidate后demo监督endpoint residual直接执行，不是改初始状态；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 174/176；sep22_resume_v3必要源/actual写后通过 |
| [Safe Real-Time Policy Steering via Noise-Space Trajectory Optimization for One-Step Generative Policies](https://arxiv.org/html/2609.21220v1) | 2026-09-21T08:00:00+08:00 | 在线noise particle搜索保policy函数image，不授Gaussian先验或实际安全；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 977/979；sep22_resume_v3必要源/actual写后通过 |
| [Hallucination-R1: Robustness-Oriented Paraphrase Generation for Factual Consistency](https://arxiv.org/html/2609.21227v1) | 2026-09-21T08:00:00+08:00 | meaning/diversity先稳定，再在原答对QA人口制造failure pressure；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) 321/323；sep22_resume_v3必要源/actual写后通过 |
| [SafeStyle: Calibrated Style Residual Injection for Controllable Style-Leakage Trade-off in Diffusion Stylization](https://arxiv.org/html/2609.21242v1) | 2026-09-21T08:00:00+08:00 | style支持方向保留、内容衰减/粒度放置/总norm cap三权分开；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 123/125；root必要源/actual写后通过 |
| [Geometry-Aware Diffusion Guidance via Curvature-Adaptive Tubular Correction](https://arxiv.org/html/2609.21251v1) | 2026-09-21T08:00:00+08:00 | normal一阶/tangent曲率二阶非抵消预算与实际目标acceptance分权；2 + 1 + 3 = 6（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 414/416；root必要源/actual写后通过 |
| [Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study](https://arxiv.org/html/2609.21264v1) | 2026-09-21T08:00:00+08:00 | 三memory domain独立roofline决定score驻留及fusion停止条件；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 765/767；root必要源/actual写后通过 |
| [Efficient Benchmarking in Production: A Study of an Evolving LLM Agent](https://arxiv.org/html/2609.21267v1) | 2026-09-21T08:00:00+08:00 | fixedweighted/adaptiveIRT重构/historical cache三支控制和证据不同；2 + 2 + 2 = 6（实际知识差额深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1130/1132；root必要源/actual写后通过 |
| [Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing](https://arxiv.org/html/2609.21268v1) | 2026-09-21T08:00:00+08:00 | source token支持drop条件替换与late-release不同于固定logit nudging；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 1379/1381；root必要源/actual写后通过 |
| [Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution](https://arxiv.org/html/2609.21284v1) | 2026-09-21T08:00:00+08:00 | root cut/local sinkbarrier与备选/合取support、跨leaf token闭合分权；3 + 3 + 2 = 8（实际知识差额深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 1422/1424；root必要源/actual写后通过 |
| [GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development](https://arxiv.org/html/2609.21293v1) | 2026-09-21T08:00:00+08:00 | source declaration/check mean/strict applicable合同分账，不wholegame接口；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 50–74/CompoundArtifact；root必要源/actual通过，仅具体命题 |
| [Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](https://arxiv.org/html/2609.21340v1) | 2026-09-21T08:00:00+08:00 | 候选pool miss与marginal ambiguity set/个体重识别风险分开；2 + 2 + 2 = 6（实际知识差额深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 212/214；root必要源/actual写后通过 |
| [IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts](https://arxiv.org/html/2609.21346v1) | 2026-09-21T08:00:00+08:00 | 参数参与/实际block执行/派生materialization三预算；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) 109/111；root必要源/actual写后通过 |
| [FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models](https://arxiv.org/html/2609.21358v1) | 2026-09-21T08:00:00+08:00 | 归一化统计固定身份与physical-range覆盖分账；3 + 2 + 2 = 7（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 69/71；root必要源/actual写后通过 |
| [Beyond Atomic Tokens: Factorizing Syllables for Language Model Pretraining](https://arxiv.org/html/2609.21362v1) | 2026-09-21T08:00:00+08:00 | 音节component词表/position/信息可逆三预算；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) 146/148；root必要源/actual写后通过 |
| [ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation](https://arxiv.org/html/2609.21369v1) | 2026-09-21T08:00:00+08:00 | offline earliest-failure onset与终态分类/在线guard不同权限；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 791/793；root必要源/actual写后通过 |
| [Prediction Dynamics in Depth-Recurrent Language Models](https://arxiv.org/html/2609.21383v1) | 2026-09-21T08:00:00+08:00 | 固定候选的相对gap/有符号终点变化与retrospective诊断分权；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) 570/572；sep22_resume_v3必要源/actual写后通过 |
| [A Scene Language Model for Open-Vocabulary Scene Mapping](https://arxiv.org/html/2609.21400v1) | 2026-09-21T08:00:00+08:00 | text map稀疏操作与每对象corruption的修订/保留分工；2 + 2 + 2 = 6（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 396/398；sep22_resume_v3必要源/actual写后通过 |
| [DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement](https://arxiv.org/html/2609.21423v1) | 2026-09-21T08:00:00+08:00 | same-parent尝试树与recovery重审继承issue，不以历史通过关闭当前父任务；2 + 2 + 2 = 6（实际知识差额深入） | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) 436/438；sep22_resume_v3必要源/actual写后通过 |
| [GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](https://arxiv.org/html/2609.21432v1) | 2026-09-21T08:00:00+08:00 | 新OPD正权诱导分布/组内中心化平方损失与原PG无偏不同目标；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 924/926；sep22_resume_v3必要源/actual写后通过 |
| [Weave: Fine-Grained Dynamic SM Scheduling in an MoE Megakernel for Compute-Communication Overlap](https://arxiv.org/html/2609.21483v1) | 2026-09-21T08:00:00+08:00 | routing后每层每GPU的SM通信/计算与GEMM/combine分块共同选择；2 + 2 + 2 = 6（实际知识差额深入） | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 119/121；root必要源/actual写后通过 |
| [Adaptive World Memory 3D Foundation Model for Scalable 3D Mapping, Localization, and Rendering](https://arxiv.org/html/2609.21502v1) | 2026-09-21T08:00:00+08:00 | 学习候选memory与runtime变化融合、local submap与global loop分责；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 404/406；root必要源/actual写后通过 |
| [The Communication Bottleneck: A Round-Trip Study of Tree-Structured Expression Serialization in Language Models](https://arxiv.org/html/2609.21509v1) | 2026-09-21T08:00:00+08:00 | sender×receiver方向矩阵与无损结构接口对照的角色测量；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 728/730；root必要源/actual写后通过 |
| [Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer](https://arxiv.org/html/2609.21514v1) | 2026-09-21T08:00:00+08:00 | human/robot共享骨架future接口与robot-only action supervision；2 + 2 + 2 = 6（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 485/487；root必要源/actual写后通过 |
| [VidOmni-Bench: A Benchmark for Fine-Grained Video Understanding via Spatio-Temporal Event Verification across Complexity and Duration](https://arxiv.org/html/2609.21521v1) | 2026-09-21T08:00:00+08:00 | natural captioner claims与人验视频支持/Unknown分开；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 570/572；sep22_resume_v3必要源/actual写后通过 |
| [What Must Survive? Exact Task-Information--State Frontiers for Resource-Sufficient Learning](https://arxiv.org/html/2609.21523v1) | 2026-09-21T08:00:00+08:00 | precompression task-advice任务分组联合rank与postcompression未知query不同；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) 448/450；sep22_resume_v3必要源/actual写后通过 |
| [From Retrieval to Recognition:How Vision--Language Models Become OCR Specialists](https://arxiv.org/html/2609.21543v1) | 2026-09-21T08:00:00+08:00 | OCR专门化matched头identity/strength与因果贡献分别核；2 + 2 + 2 = 6（实际知识差额深入） | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 790/792；sep22_resume_v3必要源/actual写后通过 |
| [On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation](https://arxiv.org/html/2609.21561v1) | 2026-09-21T08:00:00+08:00 | 双privileged context attraction/repulsion与correctness verifier不同；2 + 1 + 2 = 5（实际知识差额深入） | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 1022/1024；sep22_resume_v3必要源/actual写后通过 |
| [ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling](https://arxiv.org/html/2609.21449v1) | 2026-09-21T08:00:00+08:00 | future video/touch/action联合stream与observed mask明确producer而非预测真值；2 + 2 + 2 = 6（实际知识差额/保护深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 301/303；root必要源/actual写后通过 |
| [CompAdapt: Adaptable Composite Motion Modeling for Physics-Consistent Text-to-Video Generation](https://arxiv.org/html/2609.21455v1) | 2026-09-21T08:00:00+08:00 | 不相交并行位移、时间串接与接触jump的组合接口分权；2 + 1 + 2 = 5（实际知识差额/保护深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 1258/1260；root必要源/actual写后通过 |
| [Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](https://arxiv.org/html/2609.21450v1) | 2026-09-21T08:00:00+08:00 | 固定量化输入列空间中可补偿误差与正交不可消残余分账；2 + 1 + 2 = 5（实际知识差额/保护深入） | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 934/936；root必要源/actual写后通过 |
| [Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training](https://arxiv.org/html/2609.21482v1) | 2026-09-21T08:00:00+08:00 | epistemic截断改变训练gradient-depth课程不授部署认证；2 + 1 + 2 = 5（实际知识差额/保护深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 299/301；root必要源/actual写后通过 |
| [Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](https://arxiv.org/html/2609.21573v1) | 2026-09-21T08:00:00+08:00 | joint-context与来源独立性补局部passage检查盲区；2 + 2 + 2 = 6（实际知识差额/保护深入） | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) 849/851；root必要源/actual写后通过 |
| [GestureFAR: Streaming Co-Speech Gesture Generation with Flow Autoregression](https://arxiv.org/html/2609.21576v1) | 2026-09-21T08:00:00+08:00 | causal AR历史与continuous flow head预算/蒸馏分别验收；2 + 1 + 2 = 5（实际知识差额/保护深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 361/363；root必要源/actual写后通过 |
| [HyperParallel-FSDP: Topology-Aware Fully Sharded Training with Layout-Driven Muon on Ascend SuperPods](https://arxiv.org/html/2609.21594v1) | 2026-09-21T08:00:00+08:00 | 同module placement plan的验证DTensor与生产local/compiled collective双mode；2 + 2 + 2 = 6（实际知识差额/保护深入） | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 634/636；root必要源/actual写后通过 |
| [Trading Depth for Time in Recurrent Transformers](https://arxiv.org/html/2609.21605v1) | 2026-09-21T08:00:00+08:00 | continuous thought追加位置/KV与same-position recurrence是不同计算/状态预算；2 + 1 + 2 = 5（实际知识差额/保护深入） | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md) 501/503；root必要源/actual写后通过 |
| [Calibrating Teacher--Student Discrepancy for On-Policy Distillation](https://arxiv.org/html/2609.21619v1) | 2026-09-21T08:00:00+08:00 | 有限teacher prompt干预区间与student超区间差额监督；2 + 1 + 2 = 5（实际知识差额/保护深入） | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 1026/1028；sep22_resume_v3必要源/actual写后通过 |
| [SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations](https://arxiv.org/html/2609.21650v1) | 2026-09-21T08:00:00+08:00 | privileged成功示范覆盖作为RL初始化不同于teacher在线正则；2 + 1 + 2 = 5（实际知识差额/保护深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 232/234；sep22_resume_v3必要源/actual写后通过 |
| [GUARD: Natural Forgetting in Large Reasoning Models via Guided Answer-Reasoning Distillation](https://arxiv.org/html/2609.21677v1) | 2026-09-21T08:00:00+08:00 | non-disclosing reasoning/boundary safe-exit行为替代不是知识擦除证书；2 + 2 + 2 = 6（实际知识差额/保护深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 2456/2458；sep22_resume_v3必要源/actual写后通过 |
| [CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](https://arxiv.org/html/2609.21686v1) | 2026-09-21T08:00:00+08:00 | selected units与observer recoverability、any/full/unique泄漏分母分账；2 + 2 + 2 = 6（实际知识差额/保护深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 321/323；sep22_resume_v3必要源/actual写后通过 |
| [Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models](https://arxiv.org/html/2609.21740v1) | 2026-09-21T08:00:00+08:00 | 冻结JEPA接口的residual适配与校正表示目标分账；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 274/276；root必要源/actual写后通过 |
| [World Modeling in Transformers](https://arxiv.org/html/2609.21748v1) | 2026-09-21T08:00:00+08:00 | 地图可解码、定位、局部合法与目标方向需分别验收；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 68/70；root必要源/actual写后通过 |
| [Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models](https://arxiv.org/html/2609.21787v1) | 2026-09-21T08:00:00+08:00 | future-response低rank局部image不授固定closed latent；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 72/74；root必要源/actual写后通过 |
| [CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation](https://arxiv.org/html/2609.21793v1) | 2026-09-21T08:00:00+08:00 | 串行rewrite不交换、组合子集比较不认证全局Pareto；2 + 2 + 2 = 6（真实知识差额深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 551/553；root必要源/actual写后通过 |
| [When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence](https://arxiv.org/html/2609.21942v1) | 2026-09-21T08:00:00+08:00 | 观测可诊断性、model可利用性与人的答复权限分层；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 811/813；sep22_resume_v3必要源/actual写后通过 |
| [GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments](https://arxiv.org/html/2609.21948v1) | 2026-09-21T08:00:00+08:00 | 共享bimanual几何transition监督与native action head分权；2 + 2 + 2 = 6（真实知识差额深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 200/202；sep22_resume_v3必要源/actual写后通过 |
| [Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective](https://arxiv.org/html/2609.21888v1) | 2026-09-21T08:00:00+08:00 | loss–entropy条件control-variate而非membership裁决；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 250/252；root必要源/actual写后通过 |
| [ExpBoN: Exponential-Noise Best-of-n for Efficient Test-Time LLM Alignment](https://arxiv.org/html/2609.21899v1) | 2026-09-21T08:00:00+08:00 | finite-n mixture与conditional hit授权提前停止评分；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) 310/312；root必要源/actual写后通过 |
| [End-to-End Hard-Label Cryptanalytic Model Extraction Using Efficient Sign Recovery](https://arxiv.org/html/2609.21941v1) | 2026-09-21T08:00:00+08:00 | 已恢复局部map与competitor signature下分离hard-label sign；2 + 2 + 2 = 6（真实知识差额深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 2854/2856；sep22_resume_v3必要源/actual写后通过 |
| [Schedule optimization for tau-leaping in masked discrete diffusion](https://arxiv.org/html/2609.21960v1) | 2026-09-21T08:00:00+08:00 | learning与factorization KL分账及profile schedule成立条件；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 238/240；sep22_resume_v3必要源/actual写后通过 |
| [Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention](https://arxiv.org/html/2609.22005v1) | 2026-09-21T08:00:00+08:00 | abstention与noise filtering算子尺度/失效不同；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) 260/262；root必要源/actual写后通过 |
| [$λ$-Controlled GRPO: Turning Flow-Matching Ratio Instability into a Budgeted Resource](https://arxiv.org/html/2609.22041v1) | 2026-09-21T08:00:00+08:00 | 真实条件律ratio与训练budget surrogate分账；2 + 2 + 2 = 6（真实知识差额深入） | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 1224/1226；root必要源/actual写后通过 |
| [Available Guardrails: Certifying Selective Prediction across ML Systems](https://arxiv.org/html/2609.22048v1) | 2026-09-21T08:00:00+08:00 | certificate validity与finite-data availability不同；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 3009/3011；root必要源/actual写后通过 |
| [Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring and Abstention](https://arxiv.org/html/2609.22056v1) | 2026-09-21T08:00:00+08:00 | support completeness与answer正确分权/CWAR争议不采用；2 + 1 + 2 = 5（真实知识差额深入） | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) 544/546；root必要源/actual写后通过 |
| [RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding](https://arxiv.org/html/2609.21827v1) | 2026-09-21T08:00:00+08:00 | 树形选择并非只能在确定性 top-k 与完全随机扩展之间二选一；一个受限混合分支先保留 top-m，再从归一化 tail 抽一个 token，最后补不重复的高概率候选；供树排序的 proxy 与用于 target 验证的真实 proposal 必须分开；2 + 2 + 2 = 6（真实缺口深入） | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) `251/253`（root必要source→actual及实际POST通过） |
| [Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](https://arxiv.org/html/2609.21858v1) | 2026-09-21T08:00:00+08:00 | 保持 target 分布之外，带 key 的采样还需要让 drafter 只决定推进长度，不决定 watermark 可见的 token；一个条件分支按完整 context 索引共享 Poisson clocks，将同一底层过程分别映射到 target 与 draft 分布；target 的第一个 winner 始终提交，只有它也在 draft 的多候选集合内时才沿树继续，否则提交该 target token 后结束本轮；2 + 2 + 2 = 6（真实缺口深入） | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) `119/121`（sep22_resume_v3必要source→actual及实际POST通过） |
| [SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation](https://arxiv.org/html/2609.21983v1) | 2026-09-21T08:00:00+08:00 | 冻结 source policy 并不自动使异构机器人共享 action space；一个受限分支把 arm centerline、TCP pose 与 jaw 状态编码成共同的 25 维接口，并将视觉中的机器人移除、补齐背景，使 observation 与 action targets 落在同一 canonical 空间；当前观测形成条件，future geometry 只用于训练；2 + 2 + 2 = 6（真实缺口深入） | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) `75/77`（root必要source→actual及实际POST通过） |
| [A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](https://arxiv.org/html/2609.21996v1) | 2026-09-21T08:00:00+08:00 | 三层验收还可以增加一个受条件的内部识别 assay：在模型拒绝报告答案时，用正确候选与 decoys 的表示差形成方向，再比较当前模型对这些候选的内部反应与其 base checkpoint；标签来自 honest-correct 行为，free-form 的候选仍须由 elicitation 或部署输出构造；reference-free 只是不读取外部 reference model，不代表无候选、标注或基准；2 + 2 + 2 = 6（真实缺口深入） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) `2560/2562`（root必要source→actual及实际POST通过） |
| [Extending Decoupled Attention to Dense Prediction and Masked Training for Multi-Channel Images](https://arxiv.org/html/2609.21629v1) | 2026-09-21T08:00:00+08:00 | 同一个 compact token index 未必还代表同一空间位置；多通道图像按 channel 分开 spatial attention、再在对应位置跨 channel 交互，可以减少联合 attention 的规模；但独立 patch masks 会使各 channel 留下不同位置，直接按压缩后的索引对齐就破坏了这个接口；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) `286/288`（root必要source→actual及实际POST通过） |
| [Racer: Role-Aligned Competence Estimation for Human-AI Routing](https://arxiv.org/html/2609.21953v1) | 2026-09-21T08:00:00+08:00 | Route/defer 的分数还要区分‘倾向把任务交出去’与‘该专家对当前 query 有多大正确率’；一个受限接口在每个候选 class role 下，只从该专家 context 中相同 role、与 query 接近的已标注正确/错误实例汇聚证据，再由共享的 competence head 估计条件正确率；不用绝对 class embedding，使 labels、专家预测与 classifier posterior 一起重命名时保持一致；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) `260/262`（root必要source→actual及实际POST通过） |
| [GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills](https://arxiv.org/html/2609.21749v1) | 2026-09-21T08:00:00+08:00 | 图还可以约束 Skill 的优化空间，而不只是展开执行步骤；对固定模型与 harness，可把共享的 global guidance、可复用 node instructions 和带 applicability condition 的路径分别保存：guidance crossover 保留一方 graph，graph crossover 保留一方 guidance；mutation 则分别修订 guidance 或 nodes/paths；2 + 1 + 2 = 5（真实缺口深入） | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) `1045/1047`（sep22_resume_v3必要source→actual及实际POST通过） |
| [CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition](https://arxiv.org/html/2609.21259v1) | 2026-09-21T08:00:00+08:00 | 预测人群response分布与模型重复采样是不同estimand；均值拟合不代variability；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) `能描述分布，不等于逐次调用会从该分布采样`（sep22_resume_v3必要source→actual窄命题通过） |

## 4. 证据与知识整合

### [Qwen-Image-2.1](https://qwen.ai/blog?id=qwen-image-2.1)

官方博客与仓库说明该 7B image generation component 使用 32 层 single-stream DiT，把文本/系统/指令放在 token-level causal mask 下，把图像 token 放在 chunk-level mask 下；condition image 与 editing instruction 作为 static context，在首个 denoising step 计算后可复用 prefix KV。仓库还披露 Qwen3-VL 8B text encoder、RGBA VAE 与 flow-matching 实现。这支持的长期命题不是“某模型全面更强”，而是：condition prefix 只有在 mask layout、condition 顺序、codec/model revision、resolution、sampler 与 timestep contract 共同保持一致时才可跨 denoising step 复用。

官方页面提供作者 benchmark，但没有足够硬件、batch/concurrency、SLO、独立复现和不确定性披露，因此不采用 headline superiority。收益是减少重复 condition compute；代价是更强 cache identity 与失效管理。condition、mask、顺序或 revision 变化时必须重算；fallback 是每个 denoising step 重新 materialize condition context。该语义在 Ch24 的通用 cache/exactness 讨论中尚未明确，故进入共享 Integration queue。

### [RecreationWorld](https://github.com/QwenLM/RecreationWorld)

官方 artifact 覆盖 Ubuntu、macOS、Windows、Android 与 Web，每个平台 50 个 held-out tasks；Agent 反复执行 explore–implement–verify，最终候选由已验证 reference program 派生的 programmatic + visual assertions 判定，评分对象是 observable behavior 而非 source similarity。该证据支持 verifier-first recreation environment 的存在，不证明所有 GUI 任务可被断言完整表达，也不证明作者榜单在其他模型、cache/cost 假设或真实用户环境中保持。

Ch66 已明确要求先验证 reference artifact，再比较 Agent，并把 programmatic/visual judge、behavior-over-source 与 artifact maintenance 分开，因此为 Existing Coverage。checker 与 reference 不一致时应回放 reference、定位 assertion coverage，并对不可表达的视觉/交互后置状态保留人工审阅 fallback。

### [MoonEP public release 26/09](https://github.com/MoonshotAI/MoonEP/commit/33327eb9c4a8c95a158c3417d5e15ed2311a5849)

官方 README 与 release commit 描述一种 dynamic redundant experts 通信路径：根据当前 router outputs 在线规划小规模 redundant experts，在 expert compute 前由 owner 推送权重；每个 rank 接收固定 `S × K` tokens，zero-copy fused permute/unpermute 直接写入最终 expert-grouped 位置，backward 再把 gradients reduce 回 authoritative home rank。release 同时更新 weight-prefetch kernel、VMM buffer handling 与 returned token padding。

仓库 benchmark 只覆盖作者披露的 H20、EP=8 与 router-imbalance sweep；model、hidden size、precision、multi-node fabric、batch/concurrency、SLO 和独立复现并未完整披露，所以只采用机制与 artifact existence，不采用普遍性能优势。它相对 Ch36 现有 reactive overflow spill 增加一个独立分支：在 compute 前主动复制热点 experts，以固定 receiver shape 换取 weight prefetch、额外显存、gradient reduction 和 replica lifecycle。冗余预算不足、topology 成本过高或 planner/prefetch 赶不上 compute 时，fallback 是现有 static EP 或 reactive spill。该差异进入 Ch36 共享 Integration queue。

### [MiMo Code：MCP host-owned admission](https://github.com/XiaomiMiMo/MiMo-Code/commit/e95db7a80004edfe23617ed2160ff6db8163efef)

`e95db7a` 的完整 commit message、diff 与 regression tests 把 host-owned name 的 config snapshot 与 per-name generation 绑定，在 connect/add/store/auth 的异步边界重复 admission；新 client 先 commit，再按 identity release previous client，以防 remove/restore ABA、late OAuth 或 stale connect 覆盖当前 registry。`db95b68` 继续关闭 cold-init 与 fabricated-connected 状态缺口；`d1a72ba` 把工具执行中的 presentation progress 持久化到正确 subpart。这些材料支持 host 对 connection identity、admission 与 presentation state 的所有权，不证明任意 MCP server 本身可信、effect 已提交或生产并发正确。

Ch83 已明确 Host 是 aggregation/isolation boundary，protocol adapter 只负责 version/lifecycle，workflow owner 仍拥有 durable state、retry 与 effect commit，故为 Existing Coverage。代价是 generation、pending-attempt、close ordering 与 progress persistence 的额外状态；revision 不匹配、late completion 或 presentation drain 失败时应拒绝 stale publish，并回退到 pinned config、显式 reconnect 或 disabled state。

### [MiMo Code：session admission and bounded retry](https://github.com/XiaomiMiMo/MiMo-Code/commit/1592084b2e1fa64dc5a115708d0b5124bb9a3581)

该 family 合并同一 session-state evolution：`05fa8d1` 在 idle 前按 execution ownership 清理 orphan tool parts，`30e55a4` 为 trailing-user resume 加 exclusive admission，`1592084` 保留 error identity/HTTP status，并让 `UnknownError` 按 request/stream phase 进入有界预算，耗尽后 terminal。官方 diff 附带 status、resume、retry 与 containment regression tests。它支持“retry 必须消费 typed failure state，resume/idle/terminal 必须由 session owner 原子裁决”，不证明默认 4 次/30 秒或 8 次/15 分钟适合任意 provider 和 workload。

Ch84 已把 AgentRun 定义为携带 retry 与 terminal evidence 的 authoritative state，并要求 resume 成为带前置条件的 transition；Ch78 也已规定 structured retry state，故为 Existing Coverage。过宽 retry 会放大成本或重复副作用，过窄 admission 会拒绝可恢复工作；fallback 是将未知错误终止为可观察 failure、要求人工/新 run 恢复，并对非幂等 effect 禁止自动重放。

### [MiMo Code：skill external-root boundary](https://github.com/XiaomiMiMo/MiMo-Code/commit/1a7a7478f58f8123d5cb5cf5abae688e5599e078)

官方 commit 将默认 skill discovery 面收窄为 MiMoCode roots 与开放的 `.agents` roots，`.claude/.codex/.opencode` 改为 opt-in，并让 external scan 不匹配 dotted path segments，从而不把 `skills/.system` 等 host-private namespace 纳入 catalog；README、spec 与 discovery tests 同步更新。它支持“discovery root、scan order、name collision 与 private namespace exclusion 都是版本化 admission contract”，不证明目录内 artifact 已经安全或授权。

Ch84 已把 skill 的 registry identity、permission、pre-admission、digest 与 runtime admission 分开，因此为 Existing Coverage。收窄默认面降低意外能力暴露，却会漏掉旧目录；fallback 是显式 opt-in 单一 brand root、固定 digest 并重新验收，而不是恢复全盘递归扫描。

### [HE-Guardrail v1](https://arxiv.org/html/2609.21484v1)

实际读精确v1 III-A/B的Eq1–7、III-C/D实现与IV-A/B/C/D。输入/输出保持HE密文使服务端不能明文检查guard，密文decision改为选择response或refusal；近似sign/CKKS门并非精确零，压制token坐标仍可残留，故作者增加gated noise。pre-guard双模型packing与intra-guard复用隐状态是不同成本路径。Llama3-8B、CKKS/desilofhe、两H200、输入2048/预算200属于作者局部实验，不证明生产SLO；semi-honest server及可选输入但遵守HE协议的client是必要假设。单次noise示例没有重复查询不可恢复界，decision一致也不等guard语义正确。Ch72原FHE/MPC明文owner段未承载密文返回控制/近似残余，已在`隐私不是一个开关`后整合这一分支并保留普通明文guard的信任/成本区间；root非作者源/owner/实际写后核通过。

### [ServeGuard v1](https://arxiv.org/html/2609.21515v1)

实际读精确v1 §3、§5 Theorem1–4、§6/6.1 Theorem6–7、§7、§9。对指定deployed fixed-point linear monitor M，受限LoRA read factor A=C M使新增value update不读取ker M；commitment/证明、package身份与consumer integer-lattice admitted-byte检查分别承担关系与装载一致性。公开base residual floor仍存在，Q/K/O/MLP及未认证模块不被value/read证书覆盖；§9明确admitted bytes到actually executed kernel不在proof/attested boundary。base预处理、证明与load-check有额外成本，浮点执行不因编码等式而自动正确。Ch72原provenance/behavior probe未区分这种monitor-relative结构证据与执行绑定，已在`从文件哈希到可执行来源链`行为probe段后整合两段；没有替代sandbox/来源验证或宣称全部后门安全。root非作者源/owner/实际写后核通过，未独立复现实验。

### [MintAct v1](https://arxiv.org/html/2609.22083v1)

实际读精确v1 §3.4.1–3.4.3/Table2及§4.3/Table6–7。异步domain的有效训练贡献由生成速度与mixed-outcome group filter通过率共同决定，trainer消费按integer quota接纳domain-tagged groups，producer根据累计admitted-count/q对快域施加backpressure，避免先生成再丢弃。bounded wait后cap relaxation恢复进度却改变目标mixture；该对象不同于policy freshness/importance correction。mobile/desktop与Qwen3-VL2B/4B/8B结果没有独立消融证明quota/backpressure各自因果收益，Table6某域退步保留；硬件/SLO/不确定性未充分披露，不采用headline速度。Ch33原mixture control只声明需要控制，未说明有效贡献/两侧职责/fallback，已在该段后整合两段并保留固定同步/单域基线。root非作者源/owner/实际写后核通过，未独立复现实验。

### [Reviser: Revision-Capable Text Generation via Autoregressive Cursor Actions](https://arxiv.org/html/2609.20830v1)

exact-v1 §6–8支持autoregressive动作历史驱动可变text canvas，不把动作序列与当前文本状态混同；实验未使用可选canvas encoder，KV/rollback的identity要求是工程交接而非作者已交付实现。actual Ch24“Autoregressive 不必等于 Append-only Final Text”保留可修改文本与append-only普通输出的适用分支、state/cursor代价和重新核验要求。旧完成标签不作为复核依据：root已独立必要源/真实body与邻接核通过，不追加重复段。单篇证据详见[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#本次重新对账的既有三项)。

### [How Much of a Real Workload Can LLM-Generated GPU Kernels Actually Reach?](https://arxiv.org/html/2609.21058v1)

exact-v1 §2–6将operator在真实wall-clock中的addressable share与单kernel speedup分开；绝对误差oracle可接受小尺度全零或局部未写输出，不能把compile/run通过当正确。actual Ch49 addressable fraction与correctness admission两段已采用相对数值身份、完整写入和真实shape replay；sentinel属于工程加强，不假称作者实验已执行该全部检查。A100/BF16局部测量不推出生产SLO或所有operator可优化；root必要源与实际写后通过，保留更强verifier成本和critical-path不足时停止搜索的fallback。

### [DLB: Distributed Load Balancing at Scale for Generative AI Inference](https://arxiv.org/html/2609.21079v1)

exact-v1 §2–3支持cell root/leaf层次、P2P探测及在线时延模型，以boulder离散与sand渐进分配处理不同请求；drain是Little型近似，不是任一当前队列的恒等式。actual Ch56异构多阶段routing保留observed-state freshness、模型输入身份、endpoint admission与保守回退，内部22个月部署不证明任意负载的通用SLO。root独立必要源与当前body/邻接复用核通过，不按旧Done免审，也不重复增加同义段。

### [Decomposing Predictive Kubernetes Autoscaling for Large Language Model Serving Under Long Startup Delays](https://arxiv.org/html/2609.20874v1)

exact-v1 III/Eq1–3、II-C、IV、V、VII把token需求、startup horizon lookahead、有限margin和plant observation分为控制因素；所测重尾模拟中Kalman未稳定改善EWMA取舍，不证明预测器普遍无用。五seed/TTFT>2s模拟absolute时延相对另一simulator约两倍偏差；真实A10040GB/vLLM0.11/Qwen2.5-7B/TP1/1–4副本、人为60秒启动、5→15→5QPS只核running+waiting demand下timing，并非full token policy/五seed复现。Static是hindsight-tuned对照，colocated同构假设不覆盖异构或PD拆分。Ch56 cold-readiness后两段实写保controller提案/ready-only routing和capacity premium/fallback；root必要源及actual写后通过。

### [Reading Less While Writing: A Closed-Form Bandwidth Dial for Streaming Multimodal Decoders](https://arxiv.org/html/2609.20845v1)

exact-v1 §2–3/§5/Table3–4/AppendixE/Limitations支持单调可见prefix日程，fixed head读取完整可用输入，而stream只从arrived prefix预测长度；异步因果性是条件证明，非实测deadline。29M四层decoder、冻结CLIP/C3D/Whisper、单T4只测window-synchronized；wait-k head职责不完全对称，single-run test-clip bootstrap非训练重复。AppendixE三seed改变ActivityNet最佳区域，LibriHeavy差距在seed spread内。Ch23 Streaming Identity首段后两段补模型可见日程/到达条件，runtime commit/cancel为已有工程交接；root必要源和actual写后通过，不采用跨任务质量优胜。

### [Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding](https://arxiv.org/html/2609.20888v1)

exact-v1 §3–4、§5.2/5.3/5.8/Table4/G/K：低logit乘sigmoid趋0仍有exp0背景，部署hard pruning改support；gate≈1指数近似不证明output误差。full-cov条件界与diagonal-variance quantile surrogate不同，false negatives/数字top1 rescue不保语义；GQA物理block读取由query-head union决定。H100/FP16质量点约38% head-density/fixedb64在不同batch/length只有.72–1.12倍dense，2.5倍是b128/10%的另一点。Ch14 support-normalization之后两段实写算子/理论/实际成本差额，actual缓存/kernel交Ch45/49；root必要源及写后通过。作者1.45B/42Btoken与未来7–70B计划分开，不证明通用长上下文保持。

### [Quantization-Aware Kalman Estimation for Diffusion Sampling](https://arxiv.org/html/2609.21407v1)

exact-v1 §2–3/4/B.3/C–F估同quantized latent x处的FP denoiser输出window，同时改当前与history交原solver，而非恢复原FP整条采样轨迹。FP轨迹配对step/channel校准、逐element广播不估cross-channel/spatial covariance；非Gaussian LMMSE仍需有限二阶矩及噪声互相/时间和initial state不相关，不是任意Bayes最优。W4A4/20步/两个solver对照中UniPC FLUX/sDCI KID QDrift .168优于QuAKE .180，IR也有退步；FID/KID参照FP生成不是真实数据。A10040GB单image BF16 CPU-offload不支持通用加速，.25MiB仅校准统计，offline总成本未披露。Ch24 reverse-covariance后两段实写输出/history修正与失败回退；root必要源及actual写后通过，详见[完整必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-21407-quake校准理论成本必要范围补齐)。

### [Enhancing Audio Reasoning via Semantic Summary Prediction](https://arxiv.org/html/2609.20849v1)

exact-v1 §2–4/T1–2/Fig2–3/§5：train-only单向REG读context对齐最终conclusion SBERT，部署撤REG/head；attention更向音频只是观察，不证明grounding因果。SALMONN13B/AF-Think160k+40k，硬件/precision/steps/搜索预算及表±单位未给；attention six seeds不当训练重复。Table2两variant非均55.43，Chapters52.18±8.95保留。ISCA同族官方页无上线时刻，Accepted/会期不推更早公开，归属沿Mon21。actual Ch23 PEARL承载train-only目标/撤aux≠环境或真实执行这一命题，root必要源/actual对读E通过；REG mask与局部recipe仅报告，不声称已有书涵盖所有SPARE机制。

### [TinyCeNN-LM: Quality-Gated Conversion of Pretrained Attention with CeNN-Inspired Cellular-Recurrent Layers](https://arxiv.org/html/2609.21139v1)

exact-v1 IV–IX：当前student校准、接受层冻结、失败rollback、四门并验；已测layer3 NLL通过但NMSE/cos不通过是有效的诊断不等价证据，不因forced-accept因果实验尚未来做而否认。受限Qwen四任务各50、200题sanity不作排名；reference kernel更慢、research wrapper use_cache=False，不宣称部署加速。实际Ch17 Layer冗余/表示相似/剪枝接口已区分干预、局部表示与完整任务验收；当前四阈值配方未形成新的质量或运行选择边界，因此仅报告，不给全配方已有覆盖。root必要源→actual owner有限核通过，完整边界见[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [DiaVLo: Diagnosing Behaviours of Vision-Language Models](https://arxiv.org/html/2609.22008v1)

exact-v1 §4.1–4.3/§5–6：SK经生成、人验、expert修正，RK由self-rationale提取；internal fidelity作者留作future，遮蔽/DML不证明完整真实链。四7–8B VLM/四切片、两A10/greedy/max256、每样本单annotator，1996组合丢242约12%不得省略coverage；阈值依encoder，100random splits不是100训练seed。actual Ch66:148–151权威provenance/受控cue/self-report角色及714–718 rationale≠隐藏真实链承载采用命题，root必要源/actual E通过；局部诊断recipe仅报告，不称全SK/RK类别已有覆盖。

### [An Interpretable Memory Decision Controller for LLM Agents Based on Three-Signal Complementarity: Decoupling Confidence and Consistency](https://arxiv.org/html/2609.22043v1)

exact-v1 §3/5/必要Tables/§6–7：orthogonal三signal和四action heuristic未被校准为语义可靠性；risk-weighted收益不能抹去overall hallucination高于RAG。high-risk/high-relevance117项、decision55.6%和Active residual8%不支持普遍近零；不学参数不等零提取预算，0.14ms仅作者路径而非end-to-end SLO。actual Ch76已有geometry/任务验收、prior/authority/confidence分权，不代表四action配方覆盖；本项仅报告受限heuristic operating point。root必要源→actual owner及采用边界通过，不因Only删去贡献候选。

### [The Weight Is Over - Interactive Diffusion on Consumer GPUs](https://arxiv.org/html/2609.21849v1)

exact-v1 §3–5/Table1/3/Figure3：共享tokenizer的小encoder/translator替换冻结FLUX主干；24PartiPrompts/matchedseed质量只支持受限检查，小translator会semantic drift/style collapse。§4/Fig3的4070Ti12GB超过约11.2GB预算分页、作者测denoising latency退化约40倍，0.6B+187M路径25%residency约6.7GB/3%step代价；96GB PRO6000全fit时streaming反慢。Table3相同BF16总.47s/step105ms不变，encoder不在critical path却改变共享容量；不能把FP8/NVFP4主干量化加速归给translator，MPS与RTX-TRT平台不合并。作者`2Wmax+Amax`是双缓冲配置非通用下界，UMA不省总池；扩大matched质量是建议不是已测。root纠正原Only为actual Ch54:368/370真实gap两段：component time与pipeline working-set不同、fit/non-fit逆转与fallback，必要源/actual写后通过并释放窄锁。

### [CodeMidas: Scaling Agentic Coding RL Environments from Code Itself](https://arxiv.org/html/2609.22068v1)

exact-v1 §3–5.2/AppA：公共entrypoint/observable scope在无issue/commit/tests时定义任务，原实现只提供声明固定行为的reference，不是通用正确性真值；未规定细节只验constraint，private assertion无法转公共行为则拒收。fresh-start两次base fail/四次reference pass、四solver review与adversarial查shortcut须与frontier mixed-outcome training适配分开。§5.1 cleaning/consistency/三filter联合差别不支持逐filter因果；同训练config/step不等总token/tools/构造预算，§5.2行为关联不能代替独立验证。实际 Ch27:532/534 两段保留人工canonical、PR基线及PolicyRelative邻接；root必要源→actual/literal与523–545写后通过并释放锁，5分因真实gap深入，未复现实验。

### [Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models](https://arxiv.org/html/2609.21113v1)

exact-v1 §3–5/D.2/AppJ/Table8：drift与EAP一阶重要性不等；top400 corrupted activation intervention比随机损害更大、冻结shared组件在九pair局部恢复，因此不能否认已有干预。异task预算、corruption程度、pair依赖、冻结容量改变和缺不确定性限制唯一中介/通用transfer解释。actual Ch5表示几何、干预阶梯、跨任务充分性非唯一已有采用命题，sep22独立source→actual窄E通过；不称全部EAP实验已覆盖。

### [Accelerating Dense LLMs via L0-regularized Mixture-of-Experts](https://arxiv.org/html/2609.21672v1)

exact-v1 §3.1–3.3/4：CCM domain人口、同base冻结nonMLP的独立L0 FFN，再router/token联合训练，两个训练loop不是部署domain selector。active2.8B不等resident23.3B，same SGLang不等预算/运行公平；expert冗余和sequence/token exposure限制保留。actual Ch21 formation/shared interface/router暴露与deployment合同承载窄命题，sep22必要source→actual E通过；L0/CCM公式与速度数字仍局部报告。

### [When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success](https://arxiv.org/html/2609.21187v1)

exact-v1 §3.1–3.2/Table1/§4/Limitations：gold-history isolated和self-history累计执行是不同对象，84 conversations与77 tool-workflows不合并，8/77不是整体84；Gemma4B tool-exact 3→0反侧保留。共享生成/过滤judge、有限精确参考路径、预算与训练重复未充分披露，不推出生产失败概率。Ch66 isolated/cumulative与合法替代路径已有明确合同，sep22独立窄E通过，具体五协议与五epoch配方仅报告。

### [Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models](https://arxiv.org/html/2609.20846v1)

exact-v1 §6.1 Eq2正αeff=.5乘Eq3 e=(n−k)/n，固定k时对n导数正、固定n时对k导数负，与紧随解释“减n/增k”相反；root独立亲读确认，不能自行补1−e或负α。AppC只first1000token过程评分、generation4096及noEOS选择也不能修正公开公式。Table1局部长度/answerability经验与实验配置保留，但不支持奖励立即停的中心因果解释；暂缓该主张、不正面采用Books、不记E。官方公式纠正、精确实现确认实际objective或匹配控制到达时仅重开本项，详见[必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-entropy20824--sure20846-有限必要结果)。

### [LogicTrack: Auditing Reasoning Trajectories of Large Language Models with Formal Logic Solvers](https://arxiv.org/html/2609.21492v1)

exact-v1 §2–3/AppA.1–2/B.2–3：Z3验证收到的断言，自动翻译/额外常识仍需fidelity且可共有judge错误；有限重试耗尽的force-forward、beam恢复best或partial返回不能继承整链verified。VU主文名称与附录联合分母区分，最终正确率/核验率与某些任务反退保留，无solver SFT不继承证明。实际Ch80:58/60两段补入feedback表后、修复≠归因交接前，保额外调用成本、高风险停止与未决标记；root必要源→actual/literal及fresh写后通过、窄锁释放，非日Gate。

### [OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue](https://arxiv.org/pdf/2609.21465v1)

exact-v1 必要p2–10/D.3/E.1–3；效率奖励降低长度而no-eff质量分反高。Ch23 content/transform identity与Ch66:277–280/375–378 cohort→render→call及history干预承载窄E；360真人仅single-turn，不测interrupt。共同judge不作human truth，whole Studio/reward recipe及latency未采用。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [Can Small Language Models Know What They Don’t Know? Semantic Entropy as a Confidence Signal for Sub-3B Parameter Models](https://arxiv.org/html/2609.20824v1)

exact-v1 必要§2 Eq1/§3–5/7.1；原文写after softmax normalization，未核实现是否再对top-k重归一，top-k不等full vocabulary。Ch66:2078–2086/2213–2219/508–512承载feature/calibration、相关错误与fallible resolver窄E。N5/阈值、额外expert预算与多task退步保留，不称通用省算。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models](https://arxiv.org/html/2609.21246v1)

exact-v1 必要III-A–C/IV-B–F；gate排除216含45 failures，current/ever alarm人口时钟不同，fixed type不检测后续shift。Ch26双级error/history risk与Ch66 resolver承载窄E，cached-input成本不当端到端latency，不把53D recipe或risk升级安全权限。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies](https://arxiv.org/html/2609.21659v1)

exact-v1 必要III–IV配对/common-state/repeat及反侧；保SS/SF/FF条件化、轨迹相依与survival选择，比例随表征变化，endpoint调整非因果控制。Ch26:703–707/742–761与Ch66对象identity/reach-conditional分账承载窄E，整DTW/control协议仅报告。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [When Steering Fails in Latent Reasoning: A Latent-to-Language Transition Gap](https://arxiv.org/html/2609.21662v1)

exact-v1 必要§3末位±单位方向/odd gain与§4；Llama2比例反侧不支持所有family仅1–5%，不同权重/后续路径混杂，不归因唯一训练cause，无已成功修复。Ch5:182–214证据阶梯与跨context接口承载窄E，非whole COCONUT recipe。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [GameLogicBench: Evaluating Coding Agents on Runtime Game Logic with Tick-Level State Assertions](https://arxiv.org/html/2609.21562v1)

exact-v1 必要§2/3/4.6/4.7；36-task audit与五配置污染实验仅局部，不能签72任务语义完备、pass@3或scaffold榜单为部署可靠性。Ch66:1412–1426/1637–1646 runtime checkpoint/state assertions及behavior-preserving/deliberate mutants双侧审计承载窄E，Godot recipe仅报告。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [Evolving Procedural Memory from User Traffic for Agentic Graphic Design](https://arxiv.org/html/2609.22086v1)

exact-v1 必要§3/4/5/AppF Eq5；Eq1 prompt与Eq5 record gate未统一，R4 regression、shared judge与成功generation条件人口保留。Ch77 proposal/heldout/local certificate及Ch84双gate、matched WITH/WITHOUT和library-time承载窄E，整widen/deepen配方不称已覆盖或零退步。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision–Language–Action Models](https://arxiv.org/html/2609.21228v1)

exact-v1 必要III/IV/IV-C/V；teacher看完整input后mask pooling，current-index motion feature受future跨chunk影响，不是部署真实future。Ch26:71–88/250–291已承载privileged teacher、future-to-action与aux塑形分工。subtask pooling/两query recipe、scope消融和额外teacher预算仅报告，非wholeFOCAL。 sep22_resume_v3必要primary→actual owner独立通过，不需新增Books；具体证据与边界见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。

### [DRT: Dense Reasoning Trace for Efficient and Grounded Multimodal Reasoning](https://arxiv.org/html/2609.21675v1)

exact-v1 §3.1–3.3/奖励Eq/Table1与关键反侧；typed visual/priors/deduction和符号压缩只支持可定位陈述，wrong-answer reference-completeness局部credit不等正确或因果faithfulness。shared teacher/verifier、judge/解析预算、MathVista/GSM单项反退和bonus长度取舍保留。原Ch33 process judge caveat只窄E、不覆盖此新增分支；按root必要primary→actual/literal裁决，实际Ch33:207/209两段后root写后PASS，锁释放。 单篇通过不替代日级Gate。

### [Brain API: An Intent-Aware Control Plane for Policy-Governed Agentic Systems](https://arxiv.org/html/2609.21299v1)

exact-v1 §6–7/11.1–11.7：default polarity与conjunctive guard需明确，受限admission default-allow不推全部admission；unsupported 24/35 statements、allows7/10不能被78/81 aggregate掩盖。外部reference标签、受支持fragment42/42非49全可编码，context/ranking、多步真实execution未测。Ch84 Policy列后两段实际711/713，root必要源→actual与写后PASS，精确source绑定、NIST后续边界保留，锁释放。 单篇通过不替代日级Gate。

### [Boosting Deepresearch and LongContext Ability with Self-Generated Deepresearch Rollouts Traces](https://arxiv.org/html/2609.20844v1)

exact-v1 Prelim/Algorithm1/LongQA转换、KL与Table3/4反侧：compact snippets/Visit summaries展开同URL内容，failed噪声人口补同题successful证据，不把失败动作当示范或答案正确当sufficiency。DR→LongQA→DR目标切换/realignment分开，same RLsteps不匹配token/tools/judge/构造预算；Table4 Search均增不报省查询，百万长度构造不当能力证实。Ch27 source24850后两段实际432/434，root必要源→actual/literal及写后PASS、锁释放；精确公开身份按本日Mon21公告记录，不用Submitted Aug字段倒推首次公开。 单篇通过不替代日级Gate。

### [MT-WAM: Reorienting the One-Pass Predictive Representation Toward Action Generation](https://arxiv.org/html/2609.21474v1)

exact-v1 III–V/AppA–B/TablesV–VII：motion直接条件action、visual仅经梯度塑形共享backbone；删除visual处理分支改变容量/目标，另保two streams/params/objectives只多读visual的attention对照，不能混称同参数消融。两选择均有总体退化、Noise反向，teacher bias、copy tail/训练成本与313.480ms不同质量点保留，不给普遍禁用或deadline保证。Ch26:293/295实际区分训练收益与部署读取权，root必要源/actual/literal及写后独立通过，锁释放。

### [SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation](https://arxiv.org/html/2609.21223v1)

exact-v1方法/评价及D/E必要：native goal后固定robot pose继续sim五秒、privileged稳定性谓词与first critical stage归属，成功/安全交集/违规同rollout分母，conditional success另记。三scene SD不作训练seed CI，specific提示少unsafe success伴随成功下降不称安全改善；仿真/阈值、人工视觉一致性不升级成真机安全。Ch26:763/765实际接Evaluation ladder→Readiness；root必要源与写后通过，保观察/传感成本、延长重标定及独立controller fallback。

### [CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution](https://arxiv.org/html/2609.21908v1)

exact-v1 III/IV必要：chunk内只hold dependent通道、冻结base继续有效动作，状态/base条件低秩residual与有序候选gain只是局部预测选择，跨checkpoint仍fresh实际证据。task分母、个别退步/overshoot、局部regrasp≠最终成功、observer分类非物理真值及额外训练/在线校准成本保留。Ch26:785/787实际接readiness通用contract→训练控制漂移，root源/actual/literal与写后通过，未赋全局最小干预或安全证明。

### [Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction](https://arxiv.org/html/2609.21392v1)

exact-v1 §3–5/D1–3/E2/E4：fixed history final clip、媒体重建参考意图，demand检测/negative false trigger与positive关键点分开；reference demand/context干预不是已训练线上gate。200配对103胜/80平/17负，85.8%只decisive120，judge重评也非14模型全部重推或live真值。Ch66:391/393两段实际保存source/addressee与分母、oracle信息和澄清fallback；root必要source与写后通过，锁释放。

### [How Many Humans Is a Judge Panel Worth?](https://arxiv.org/html/2609.21277v1)

exact-v1 §3/4/Limitations/C4：normalized Gram PR忽略energy/averaging direction，频率MSE另依赖两者；hard-label equal-energy/nonnegative-correlation构造中PR增而MSE恶化，非不可实现的任意矩阵反例。条件独立human参考抽样的匹配依目标/人口，empirical100-label分布不授真值；相关panels/additions不作独立重复。Ch66:2410/2412实际补双等效人数、成本与参考不足fallback，root必要源与写后通过，不称通用人力替代率。

### [Verify, Don’t Trust: Agentic Model Development for Video Discovery Retrieval at Scale](https://arxiv.org/html/2609.21257v1)

exact-v1 §4–6：commonbase/allowed treatment/metric semantics经两arm artifact提取realized配置准入；Spec readonly非密码学不可变，self-report不拥有科学比较权限。−22pp由evaluator输出深度失配解释，+4.8 bundled/3.2 matched/0.66% online各自estimand，post-study mutation不倒填现场自动拒错；9 retained rounds/29 terminal非all workflow attempts。Ch66:216/218真实分comparison invalid/operational failure/valid non-improvement，root必要源与写后通过。

### [The Stochastic Shift: A New Evaluation Paradigm for Text-to-SQL with AI Operators](https://arxiv.org/html/2609.21133v1)

exact-v1 §2–6：确定关系合同与AI predicate语义不同，整query EX可误拒relaxed语义/误收data-dependent multiplicity错误；few-shot LLM splitter非verified AST。共源Gemini生成/拆分/1–5 autorating不能自证faithfulness或人工reference真值；55跨系统不补造两engine各55分母，97.2/93.3局部准确率与剩余误收误拒、额外LLM/执行成本保留。Ch66:1118/1120实际分层及拆分忠实性/fallback，root必要源与写后通过，原set/multiset正文未删。

### [ArenaFlow: From Trajectory Ranking to Hierarchical Credit Propagation for Open-Ended Agent RL](https://arxiv.org/html/2609.21378v1)

exact-v1 §3–4/AppB：tournament group advantage只对正A追加depth启发式局部credit，skill utility从相对归因提读写/退activepool，非pivotal因果或事实删除。AppB该设置token/calls/time增加，其他baseline起点/SFT预算不全匹配；人类归因一致不等干预真值、top6及过大utility反退。Ch33:193–213 process-credit/verifier分权与Ch77:142–148/609后utility、版本与admission实际承载窄采用命题，root原方法与actual独立核通过；非整A+max(A,0)g/skill公式已有，局部recipe与数字仅报告。

### [OpenMAS-GCom. A Diagnostic Benchmark for Graph-enhanced Multi-Agent Systems](https://arxiv.org/html/2609.21527v1)

exact-v1 §2.2/3–4/A.4–A.8/B.5–B.6：rewire保度不等删role保持资源，污染eligible消息不等实际消费，失效保last state不证明通用恢复；相近baseline在污染/worker失效下不同退化，accuracy冠军不等单位token冠军。相同预算cap非realized usage，统计口径混有sample/run SD、加权估计与binomial SE，不全作paired CI。B.6 matched controls明确未来工作。actual Ch82:58–98 task/topology matching、error absorption/amplification、质量及资源账具体承载此窄E，root必要源/actual通过；非四干预recipe完整覆盖。

### [An Approximate Queueing Model of LLM Inference Serving for SLO-Driven Autoscaling](https://arxiv.org/html/2609.20957v1)

exact-v1 IV–X：Poisson/独立mean lengths/mean-field occupancy的三参数近似只在稳态ρ<1使用，fit排饱和与高rate点，训练集均值偏差不是heldout tail保证。两个44min固定shape profile每arm单run，7/127与27/128为cycle-mean超目标率，非请求P90；少replicas对延迟成本明确。IX实测ITL参与decode supply calibration不等施加ITL target，无queue仍可能active batch迭代变慢。Ch56:43–68/386–390/649后capacity/iteration work与实际SLO验收具体承载窄E，root必要源/actual通过；均值方程、online配方及未测startup forecast不作为完整Existing或生产保证。详细限定见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-queueing20957-三参数近似与容量延迟目标分账)。

### [Same World, Different Knowledge: When Isolated Audits Misjudge World-Model Repairs](https://arxiv.org/html/2609.21155v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用同源错误使isolated repair排序反转；instant residual不识别真实wind或证明longhorizon/所有offset。root独立必要source→actual/literal及实际Ch25:68/70两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [Benchmarking World Models for Continual Learning on Compositional Tasks](https://arxiv.org/html/2609.22055v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用expert冻结不阻shared encoder漂移，保存/复用速度/新增容量分开；看全task demos的privileged冻结encoder不是无先验在线优势，三seed minmax非CI。root独立必要source→actual/literal及实际Ch25:165/167两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](https://arxiv.org/html/2609.21712v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用common ray字段不授common encoder，native grids与投影adapter分权；无独立adapter消融、长期policy闭环或安全证明；memory/distill已有分支不重复。root独立必要source→actual/literal及实际Ch23:695/697两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [AutoViewMem: Self-Configuring Orthogonal Views for Conversational Long-Term Memory](https://arxiv.org/html/2609.21940v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用interaction归纳互补抽取schema前移写入，不须新增query router；低重叠不等正交/真值，同querybudget非生命周期预算；较大backbone完整history仍强。root独立必要source→actual/literal及实际Ch77:344/346两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [MACE: Memory-Agent Co-Evolution with Adaptive Memory Graphs for Multi-Agent Systems](https://arxiv.org/html/2609.21533v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用内容组合×消费格式排序反转，独立边际score丢配对交互；每calibration观察四pairing、extra成本/有限重复，不是单选无成本在线最优或usedunit因果。root独立必要source→actual/literal及实际Ch77:273/275两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [Proxifield: Decentralized Multi-Agent Communication through Semantic Proximity](https://arxiv.org/html/2609.20889v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用每round重建need/plan/complementarity通信图与effect commit分权；确定选择仍global metadata/pair成本，coverage可超sender k；全Accept不授effect/网络安全。root独立必要source→actual/literal及实际Ch82:230/232两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy Leakage in Vision–Language Models](https://arxiv.org/html/2609.21363v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用发布前高层视觉线索变换与refusal不同控制点，距离/utility独立验收；近距离非零/粗粒度残余、多图25m/25km范围冲突、局部utility不等匿名化或无损。root独立必要source→actual/literal及实际Ch72:212/214两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models](https://arxiv.org/html/2609.20971v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用relativecut救援可能删base，两独立masks union保原候选；βattenuation非upperbound，130诊断paired差CI含0；density/selector成本与prefill非decode。root独立必要source→actual/literal及实际Ch14:284/286两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [Information-Gain Rewards over Diversity-Pruned Tests: GT-Anchored Verifier Co-Training for Reliable Code Generation](https://arxiv.org/html/2609.21208v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用test producer按GT锚定区分信息/cov gate训练，非passrate自证；不同列非统计独立/严格低方差，16selected suite漏alias；完整pool执行与72vs46GPUh成本。root独立必要source→actual/literal及实际Ch33:485/487两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [Scaling Discovery through Test-Time Communication](https://arxiv.org/html/2609.21032v1)

必要原文精确版本、方法/对照与关键反侧已在[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)逐项持久：采用verified可转移连续进展共享与独立best-k不同，终态grader非忠实中间反馈；stage/transfer/独立续搜仅假设，89Terminal少trial team不胜best2；prompt非gate/共享资源与oracle选择分账。root独立必要source→actual/literal及实际Ch82:97/99两段与邻接写后通过、窄锁释放；实际段落包含新增机制、成本和原方案fallback，不是整recipe审计或日级Gate。

### [Layerwise Decoupling for Stable Structured Sparsification of Fully Connected Layers](https://arxiv.org/html/2609.21126v1)

exact-v1必要机制、证明/评价及关键反证已在[唯一证据记录理论组](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-理论有限组21126--21001--21422--21656)限定实际读取范围：采用正齐次gauge改变单边结构惩罚，目标最优等价不授有限迭代轨迹。once/block与every-step投影不同，incoming-row对照非同joint目标；80%预算SSS反侧、runtime未测与非齐次激活范围保留。root独立必要source→actual/literal及实际Ch49:458/460两段与邻接写后通过、窄锁释放；不是完整附件/实现复現或日级Gate。

### [On the Limits of Maximal Coding Rate Reduction for Out-of-Distribution Generalisation](https://arxiv.org/html/2609.21001v1)

exact-v1必要机制、证明/评价及关键反证已在[唯一证据记录理论组](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-理论有限组21126--21001--21422--21656)限定实际读取范围：采用coding几何稳定不授label读出稳定，near/exact/support三反证分账。完整支持正噪声仅near-optimal失败；exact optimum配不受限source-optimal classifier反而零target风险，noiseless exact失败改变支持；密度比不受控与Waterbirds局部人口保留。root独立必要source→actual/literal及实际Ch5:131/133两段与邻接写后通过、窄锁释放；不是完整附件/实现复現或日级Gate。

### [Brownian Heads for Deep ReLU Representations: Activation Mass and the Cost of Same-Sample Selection](https://arxiv.org/html/2609.21422v1)

exact-v1必要机制、证明/评价及关键反证已在[唯一证据记录理论组](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-理论有限组21126--21001--21422--21656)限定实际读取范围：采用固定表示的conditional经验界不抵消same-sample representation选择成本。union selection须保留，auxsign前固定候选族不是训练读sign；worst empirical capacity非population/minimax证书，受限head与固定n反侧保留。root独立必要source→actual/literal及实际Ch5:143/145两段与邻接写后通过、窄锁释放；不是完整附件/实现复現或日级Gate。

### [Beyond Gaussian Worlds: Latent Geometry Matters for JEPAs](https://arxiv.org/pdf/2609.21656v1)

exact-v1必要机制、证明/评价及关键反证已在[唯一证据记录理论组](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-理论有限组21126--21001--21422--21656)限定实际读取范围：采用intrinsic pair与density/embedding/慢谱几何相容提供非Euclidean恢复分支。观测可逆、Gaussian-potential限制、嵌入Laplacian相容及完整最慢坐标显式保留；exact分布匹配不可用finite MMD替代，优化成功数冲突不采用。root独立必要source→actual/literal及实际Ch25:858/860两段与邻接写后通过、窄锁释放；不是完整附件/实现复現或日级Gate。

### [COAL-SQL: Coverage-Guided Augmentation and Failure-Driven Learning for Text-to-SQL Post-Training](https://arxiv.org/html/2609.20842v1)

exact-v1必要范围、机制/对照与直接反证见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)，只采用结构覆盖与current-policy失败分权、全错教师监督/相对强化分流。具体buffer/全局quota与双时钟recipe仅报告；Spider noepoch略优、教师/语义gate与cost局部边界保留。root直接必要primary与fresh actual Ch27:572–599/987–1007与Ch33:434–436对读，窄E通过，不指整篇机制已有。

### [ForeTac-VLA: A Forecasting-Based Tactile-Vision-Language-Action Model for Contact-Rich Robotic Manipulation](https://arxiv.org/html/2609.20980v1)

exact-v1必要范围、机制/对照与直接反证见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)，只采用GTfuture→forecast线上action prefix需条件producer与误差交接。非独立课程/2×2因果，预测MAE非接触安全，dark/clutter与deadline边界保留。root独立必要source→actual/literal与实际Ch26:285/287两段、前后衔接写后PASS，锁释放。

### [Attention-Aware Routing: Coupling Routing and Attention in MoEs](https://arxiv.org/html/2609.20974v1)

exact-v1必要范围、机制/对照与直接反证见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)，只采用attention-history logits与router耦合、冻结参数不等行为冻结。retrieval反退/层位局部性、sink非唯一因果、物化权重不能FlashAttention与SLO未测保留。root独立必要source→actual/literal与实际Ch21:413/415两段、前后衔接写后PASS，锁释放。

### [Recursive Language Models Generalize Out of Domain](https://arxiv.org/pdf/2609.20831v1)

exact-v1必要范围、机制/对照与直接反证见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)，只采用activeframe观测限定hypothesis，覆盖正确规则不保证选择。ideal MDL≠optimizer、已见visibleframe且足够定义目标、parent可反解shortcut反例和非全compute匹配保留。root独立必要source→actual/literal与实际Ch5:86/88两段、前后衔接写后PASS，锁释放。

### [When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation](https://arxiv.org/html/2609.20942v1)

exact-v1必要范围、机制/对照与直接反证见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)，只采用受控recursive exposure的分布漂移与参数继承/真实质量分账。one-step共享M1/official非purehuman、embedding与agreement代理非真quality；不称全steering recipe已有。root直接必要primary与fresh actual Ch27:334–355对读，窄E通过，不指整篇机制已有。

### [WM-VS: Progress-Aligned World Models for Closed-Loop Visual Servoing](https://arxiv.org/html/2609.20892v1)

exact-v1必要范围、机制/对照与直接反证见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)，只采用预测nextlatent须保存signed task-error，modelconsequence与真实onpolicy分权。日志action outcome只BC邻域local label、learned contraction非物理稳定、ever/final分母与externaltag stop保留。root独立必要source→actual/literal与实际Ch25:271/273两段、前后衔接写后PASS，锁释放。

### [CaLR: Causal Latent Revision for Robust Diffusion Reasoning](https://arxiv.org/html/2609.20981v1)

exact-v1必要范围、机制/对照与直接反证见[唯一证据记录](../_sources/daily-20260921/arxiv-evidence-restoration.md)，只采用teacher CTM约束latent revision的strictflow/optimalmemory中心论断待核。sep22独立PDF原文/视觉确认penalty用于update方向反向，不自行修1−P；保局部实验，未进Books，重开须官方统一机制/证明说明。本项由sep22_resume_v3非作者独立核Eq4/14/15与精确PDFp4/p11，不是作者自签；中心采用终态暂缓、非Evidence正面通过。

### [Voice-Light: A Full-Duplex Cascaded Voice Agent with Causal Turn-Taking and Speculative Generation](https://arxiv.org/html/2609.20995v1)

exact-v1 §3–11重点§7 generation/cancel/sample-position、private speculation/词法晋升及browser每80ms rendered-range ACK。消费侧durable audible history不是服务端已发送、更不是用户理解或任务effect；turn-taking head未经概率校准。历史locked V1 checkpoint step3500不等部署step750 validation-only；V2 gate未过/test sealed，36turn/3session/1operator热态serverPCM不是heard/populationSLO，promoted人口有难度混杂。原Ch81一般interrupt/commit未含这条消费ACK差额，实际两段已在[Ch81:874/876](../../../../books/part-07-agent/81-workflow.md)接Continuous-time末→Testing，保buffer/ACK成本和稳定transcript/关speculation回退。sep22必要源与actual独立PASS；初稿checkpoint误作样本量已按非作者硬纠错。详见[唯一证据包](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-voice-light20995--magic21018--feedback21022-actual-闭合)。

### [MAGIC: Marginal-Guided Compression with Optimal Transport for Efficient Visual Document Retrieval](https://arxiv.org/html/2609.21018v1)

exact-v1 §3–5/Prop1、B2–4/B6/D1–2以离线winner-demand加权source marginal、balanced soft OT再Lloyd readout，保持fixed onlineMaxSim。unitvectors/‖q‖≤1/真实population w的Prop1只bound期望positive score decrease，不bound绝对误差/虚增/排名；softbalance≠hardcluster等大，1000querytokens可能仅几十queries，rare/rebuild与transport成本不能省略。same2kpages/ColQwen2.5/oneH20 batch1穷举有较宽预算切片反退，perpage费用不是globaldictionary/端到端RAG。原indexbudget不含该需求分配，实际[Ch76:369/371](../../../../books/part-07-agent/76-rag.md)两段保population/估计、完整index/source回退；sep22必要源与actual独立PASS，不称任意query证据保全。

### [Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs](https://arxiv.org/html/2609.21022v1)

exact-v1 §3–5/A1–3冻结已收敛planner，near-finalchunk/actionfeatures每chunkcache、高频新hand-view做对应action最后velocityupdate；不同于全planner重跑或完成后残差。初始chunk合理与近接触不可恢复边界，约2ms模型feedback不包含camera/IPC等总71.01ms；10Hz/16chunk无intrachunkreplan，Table2 uniformarrival反应估计不是实测SLO。真实每任务50demos/20rollouts与仿真静态Object反退分开，异horizon/LoRA对照非纯architecture，GPU/precision未披露。实际[Ch26:1071/1073](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)两段填Fast/slow末步handoff差额，guard/缩chunk/replan/stop工程回退保留，sep22必要源与actual独立PASS。

### [Loopjacking: Hijacking Human-in-the-Loop Approval](https://arxiv.org/html/2609.21081v1)

exact-v1 §2–7按真实审批A→完整sinkB及directB/wrongscope/unchangedA/safecontrol核，canonical rendering与最后effect-time重建比较分权；不以sameID/resume继承新effect许可。阳性Agno七release不补中间range且wrapper非vendorfix，LangGraph仅InMemory+customAuth允许update（deny-update安全，Postgres未测），OpenClaw2026.2.23/24 paired；OpenAIordinaryfunction-per-call0.22.0/.22.2阴性不等所有SDK/sticky安全。脚本approval先assertview，不测human理解/发生率。实际[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md):2253–2263完整descriptor/SUDP freshconsume与deliveryfence、2775–2785可信反渲染/approval-effect receipt确覆盖窄长期命题，故已有覆盖；六条件taxonomy/版本matrix仅报告，不声称整篇已有正文。sep22独立必要source→fresh actual窄E PASS，无新Books写入。


### [Stiefel-AdamW: Geometry-Aware AdamW for Linear Factorization Blocks](https://arxiv.org/html/2609.21039v1)

精确v1必要机制/关键反侧见[本日唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。A仍可训练但行正交，B自由；fixed-W compact fiber不保证变化W轨迹或entrywise Adam剩余旋转不变。受限凸性/有界量/moment定理不授一般LLM收敛，QR/任务反退与projection/retraction成本保留。 sep22独立必要source→actual/literal与真实两段/邻接写后通过，实际整合 `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md) 169/171；非全recipe/日级验收。

### [Physically Based Rendering in the Latent Space](https://arxiv.org/html/2609.21054v1)

精确v1必要机制/关键反侧见[本日唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。已知geometry/materialtypes/emitter/camera，scene-specific signedfeatures/residual，非未知scene重建或latent物理能量。Eq6 visibility方向冲突不采用、不改mask；latent无偏不授nonlinear RGB无偏，Fig8 decoded RGB反慢及校准/训练成本保留。HTML称planned，当前官方abs已列GitHub链接但本轮未核代码。 sep22独立必要source→actual/literal与真实两段/邻接写后通过，实际整合 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 817/819；非全recipe/日级验收。

### [Detecting Hallucination in LLMs: Tracing the Topological Signatures of Impaired Context Sharing](https://arxiv.org/html/2609.21096v1)

精确v1必要机制/关键反侧见[本日唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。III–VI/TI–II必要核：FRC/entropy仅uniform extrema相关非逐例等价；Phi/Qwen模式不通用，QwenTruthfulQA t1 73.53<lap75.17及Mistral反退、改EigenScore协议、GPT4judge/manual100非真值、Eager materialization成本和未披露严格probe split/seed保留。窄E仅诊断feature须经model/可靠label/部署切片校准、不能当truth/causal correction，正文实际承载；新feature配方仅报告，不称整FRC已有。 sep22独立必要source→actual通过，具体已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 1870–1885/1913–1919/1933–1947/2098–2133；非全recipe/日级验收。

### [A Multi-Engine Dataflow for MoE Decoding on Scratchpad-Based Tensor Accelerators](https://arxiv.org/html/2609.21137v1)

精确v1必要机制/关键反侧见[本日唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。§3–5.5/必要5.6/5.7核shared B/D DMA、routing后input projection/private加载、异engine overlap/down输入不同与PSUM反例。Trainium3 B1 TP4/8局部不外推GPU/batch/SLO，PPL恢复仍四task至−3.2pp；equalstorage selection、PSUM单步快而全图慢和scratchpad/gather/KD成本保留。 root独立必要source→actual/literal与真实两段/邻接写后通过，实际整合 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 894/896；非全recipe/日级验收。

### [TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](https://arxiv.org/html/2609.21172v1)

精确v1必要机制/关键反侧见[本日唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。§3–4/Alg1–2、§5.1–5.5/T4/6–12/§7：length只容量proposal，profile/candidate solver非最优或质量证书；overflow不修旧SVD，H2D未隐藏，OnePlus12 FP16 B1平均prefill不替decode（Llama平均.71×）及Table8质量反退/prefix未测保留。 root独立必要source→actual/literal与真实两段/邻接写后通过，实际整合 `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 728/730；非全recipe/日级验收。

### [Implicit Rule Induction with Test-Time Task Embeddings in ARC-like Tasks](https://arxiv.org/html/2609.21181v1)

精确v1必要机制/关键反侧见[本日唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。§3–4.4/5/T1–2/Fig5：现有frozenexecutor latent搜索不重写；仅新增joint executor改动可能忽略latent/坐标不可比，先固定backbone校准latent再冻结latent更新executor，induction/execution分别验。重复任务/多解latent、probe非完整rule、pair非完整task、插值不授新算子/OOD与搜索成本保留。 root独立必要source→actual/literal与真实两段/邻接写后通过，实际整合 `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) 81/83；非全recipe/日级验收。

### [I’ll Keep an Ear Out: Teaching AudioLLMs Proactive Audio Assistance](https://arxiv.org/html/2609.21183v1)

精确v1必要机制/关键反侧见[本日唯一证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)。§3–5/T1/streaming/I2：四监督补错过onset及history去重；ESC clean高分不替Epic低S1/I2且S2未测。固定事件拼接流平均3.5s非实机/用户SLO，history真实notice是runtime工程交接、不称paper自证送达；数据/history/校准成本和eventrouter fallback保留。 root独立必要source→actual/literal与真实两段/邻接写后通过，实际整合 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 741/743；非全recipe/日级验收。

### [SWE-Proof: Can Language Models Resolve Real-World Issues with Machine-Checked Proofs?](https://arxiv.org/html/2609.21190v1)

exact-v1 必要范围 §2–5/T1–3、E.3–E.4、F.4/H.3；逐函数proof与整个issue行为覆盖/axiom/patch correspondence三外部接缝分权。known-correct patch仅离线构造特权；提供spec可能泄露localization/H.3超issue条件，Claim1依赖soundness/admissibility与I-P等价，§5明确非证明。Axiom fuzzing、Docker shadow与adversarial tests只给反证搜索；85→58.2为26.8百分点非相对26.8%。自写spec不改善，main单repetition，不能认证自动忠实intent。 sep22_resume_v3独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch66:1585](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md:1585) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies](https://arxiv.org/html/2609.21216v1)

exact-v1 必要范围 §3.1–3.3/§4.1–4.7/§5、A1–A3/TI–VII；冻结few-step candidate后demo监督endpoint residual直接执行，不是改初始状态。prefix KV、candidate/source noise输入corrector，target=a*−sg(aθ)，backbone/AE冻结且不rerunAE；跨NFE复用不等跨backbone。Smol无noise独立checkpoint反更好，不能认证noise必要；13/50任务退步，Hard差−.56pp CI[−2.71,1.64]。额外residual forward/训练、A10080/40两个panel不能拼，b1/SDPA无compile的同步p50只model-forward不含执行。 sep22_resume_v3独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch26:174](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:174) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Safe Real-Time Policy Steering via Noise-Space Trajectory Optimization for One-Step Generative Policies](https://arxiv.org/html/2609.21220v1)

exact-v1 必要范围 III–VI/Eq3–10/Alg1/TI–IV；在线noise particle搜索保policy函数image，不授Gaussian先验或实际安全。shell-radius penalty只限范数。Alg1旧A检查→更新x→重算返回action无freshcheck，旧候选通过不保新候选；π(x)=x,c=x−.2≤0,dim1,λ=η=1,x=.1经reggrad−.396更新.496即反例（字面工程分析，未核代码）。空feasible fallback未给。fullH成本/短Te早停、NFE1不含particles/多轮gradient，real10trials仍2collision，fresh-return验收/failclosed属工程要求。 sep22_resume_v3独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch26:977](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:977) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Hallucination-R1: Robustness-Oriented Paraphrase Generation for Factual Consistency](https://arxiv.org/html/2609.21227v1)

exact-v1 必要范围 §3–7/T1–4/Limitations、A1–A4/C1–C5/E/F；meaning/diversity先稳定，再在原答对QA人口制造failure pressure。DeepSeekV3 meaning gate非严格等价；human500pairs/100questions83%与LLM87.46%只是各通过率非pairagreement/消bias。ER/WER限original-correct，而后续SFT未同样过滤，不能称纯知识稳定因果。T4 AnyAcc全下降而RobustAcc上升。Diversity squarednorm非标准cos，单例/空retained边界未认证，8A800仅generator训练不等全SFT预算。 sep22_resume_v3独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch27:321](../../../../books/part-04-training-system/27-data.md:321) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [SafeStyle: Calibrated Style Residual Injection for Controllable Style-Leakage Trade-off in Diffusion Stylization](https://arxiv.org/html/2609.21242v1)

exact-v1 必要范围 §2–3/Eq1–5、ablation/stress；style支持方向保留、内容衰减/粒度放置/总norm cap三权分开。Us方向移除后orth内容基、overlap↑α↓非语义解耦；fine/mid/coarse residual汇总后cap，ηλγ只relativefeature-change。Dc不同reference appearances与sets一次复用适配边界未解，不造universal。SDXL/InstantStyle冻结，50ref20prompt/24×10stress/9baseline同seed/1RTX4090；SemLeakCLIP差是代理，cleanstyle0leak丢style、cap降DINO，成本precision/steps/SLO ND。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch24:123](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md:123) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Geometry-Aware Diffusion Guidance via Curvature-Adaptive Tubular Correction](https://arxiv.org/html/2609.21251v1)

exact-v1 必要范围 §2/§4 Theorems2–4/Eq8–14/Alg1、§5.3–5.4/CFG；normal一阶/tangent曲率二阶非抵消预算与实际目标acceptance分权。host prior不变；regular levelset+tubular+thirdderivative下rN+.5K rT²≤R与高阶余项，learnedscore/Jacobian不是真manifold。Armijo period>1 reuse不是每stepaccept。Armijo-alone强而full更好、不唯一geometry因果；同100FFHQ4090 N1000 memory3612/time132 vsDPS3490/38，N200time26不是同预算gratis。COCO1000固定promptseed SD2.1局部CFG非posterior/semantic保证；AIscience extension不采用。评分Durability3限有限geometry/acceptance选择长期界，不扩大reach。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch24:414](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md:414) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Programming AMD XDNA NPUs with Open-source Compiler Tools: A FlashAttention Case Study](https://arxiv.org/html/2609.21264v1)

exact-v1 必要范围 §4.1–4.4/§5.1–5.3/§6.1–6.6/§7；三memory domain独立roofline决定score驻留及fusion停止条件。scoresDDR→MemTile→computeTile，QK同DMA/V另路/cascade；instruction-count attainable ceiling非hardwarepeak。XDNA1stagedcomputeboundfusion益小，XDNA2highridge需tilelocal，compiler/buffering同步混杂非纯fusion；BF16IO与内部bfp16cast分开。attention时间含dispatch/softmax，numerator只GEMM；warm10/20 minimum非tail，Gaussianvariance误差/相关性不证wholeLLM任务无损。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch49:765](../../../../books/part-05-inference-system/49-tensorrt-llm.md:765) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Efficient Benchmarking in Production: A Study of an Evolving LLM Agent](https://arxiv.org/html/2609.21267v1)

exact-v1 必要范围 §2/§3.2–3.4/§4–7；fixedweighted/adaptiveIRT重构/historical cache三支控制和证据不同。574runs52days/cal287(D1–28)→heldout287(D29–52)，valid≥80%reference只valid人口/519题。Fisher selected rawmean非fullscore；gpIRTbias/d用cal切分不偷heldout。固定难度虽非accuracy最佳却并行/predictable；自适应顺序依赖/cachefreshness代价分开。IRTcluster局部劣random，1day14runs仅成熟窗口，5familytransfer有限；绝对/排名fidelity不互换，历史replay非生产延迟，HWprecisionconc/evaluator ND。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch66:1130](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md:1130) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing](https://arxiv.org/html/2609.21268v1)

exact-v1 必要范围 §3–5/T1–2、B/I/L必要机制/效率/failure；source token支持drop条件替换与late-release不同于固定logit nudging。Eq2 b=max(gamma−p_src(source),0)，p_edit(source)+b对editargmax；gamma0无bias不必改token、2必保。Sstop25后自由细节，attention只区域proxy。末2scale residual提议同mask剪QKV/attn/FFN但仍logitshead。InfinityStar8B81frames480p/BF16/1A800/seed41/160cases，prune50%alignment.972/.976低无prune.979/.980，85→64只decoupled两pass，130→64联合改动不单因；大structure/edit失败，未生产SLO。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch24:1379](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md:1379) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution](https://arxiv.org/html/2609.21284v1)

exact-v1 必要范围 §3 A1–A11/§4–5/§6.1/§7–8、A.3 Th10–11完整proof；root cut/local sinkbarrier与备选/合取support、跨leaf token闭合分权。cut冻结issue/expand非远程瞬时fence；postcut prebarrieraccepted要local-orderpre-fence receipt/futurelineage闭合。{{A},{B}}当前witness exact-operation/envelope原子rebind非自动B，{{A,B}}不得删A洗权限。完整manifest是assurance前提非checker证明；samecut/epoch/profile SEND=ACK唯一tokenprojectionmultiset非总counter；已知blocker N、opaque/conflict U、局部Q不global。Th10 A1–9与liveness A10–11分开；provider-free child/fileledger17cases/44mutations未本轮run，不vendorMCP/A2A/OAuth/physicalundo。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch72:1422](../../../../books/part-06-ai-infrastructure/72-security.md:1422) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [GameASG-Bench: Benchmarking Autonomous Software Generation for Game Development](https://arxiv.org/html/2609.21293v1)

exact-v1 必要范围 §2–4/§6/T1–9；source declaration/check mean/strict applicable合同分账，不wholegame接口。L1pattern非behavior/L1fail不skipL2，legalprepare不得直接给outcome；P1 NOT_APPLICABLE当前runner缩合同非whole需求。47tasks/1221checks/ref47positive，一次cleanrun/config；93.2mean≠26/47strict，预算planned47/evaluated10/32/47分母不同。两harness18各交10/各8/21neither，high19/max18单run非因果。仅Ch66交集/冻结predicate及双侧oracle已承载，game接口与配方仅报告不造diff。 root独立核必要source→fresh owner的窄采用通过。actual Ch66具体承载该命题，不是whole game interface已有覆盖；不新增Books。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](https://arxiv.org/html/2609.21340v1)

exact-v1 必要范围 §3–5/Th5.2/Cor5.3 assumptions/proofsketch、§6–7.1/Limitations；候选pool miss与marginal ambiguity set/个体重识别风险分开。declaredpool/attacker/querybudget/releaseddistribution/exchangeability下APS伪posterior/频数→marginal truthsetcoverage；1/max(1,card)proxy非probability/DP。openworld conditionalinclusion+missrho总体≥(1−rho)(1−alpha)，不可报cond替global。K50 miss.16/cond1/global.84 vsK200miss0/.97；driftTAB.965→.923/Blog.940→.835/LLM帮助不uniform，cal50/100/150非单调。索引/多采样校准成本、未知attacker不涵盖，membershipfuture/HWprecisionND。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch72:212](../../../../books/part-06-ai-infrastructure/72-security.md:212) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts](https://arxiv.org/html/2609.21346v1)

exact-v1 必要范围 §3 Eq3/§4.1–4.7 Eq4–16、§5.6/T3–4/A3；参数参与/实际block执行/派生materialization三预算。token-independent codebook每层全基底有符号组合两路径，token仅topkblock；非f(sumW)=sumf、每基底语义/非零贡献不保。cache只fixedweights/config共用，updates重新合成，小E派生cache可能更大；18layerMiniPile1epoch1.523B/15Mheldout parameter-matched仍整模块/route，ImageNetcache非LLMruntime/通信/SLO。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch21:109](../../../../books/part-02-model/21-moe.md:109) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models](https://arxiv.org/html/2609.21358v1)

exact-v1 必要范围 III Eq2–4/IV 3C/8traj预校准、V T1/width2.5反例；归一化统计固定身份与physical-range覆盖分账。state/action联合非action-only；未来demo不用，motion预任务同统计冻结training/replay/inverse。过宽放大physicalerror，BI1 ANSII97.2>FAN95.7，部分BWT负，4stream10rollout不普遍安全。改stats而weight固定改变action不将所有forget归weights；nextembodiment范围新校准/联合policy验收。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch26:69](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:69) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Beyond Atomic Tokens: Factorizing Syllables for Language Model Pretraining](https://arxiv.org/html/2609.21362v1)

exact-v1 必要范围 §3–4 Eq2/8/11–14、§5.1–5.3/T1/§7.2 T15–18；音节component词表/position/信息可逆三预算。onset/rime/tone并列一个position，concatprojection/完整tuplemask三CEhead不漏分量。Chinesephrase lookup/default/polyphony与同音碰撞不可逆，多位fallback/UNK。Chinesecontrolled全pipeline非纯tokenizer，Viheterodata，WSC/OCNLI/CMRC部分反退，decoder-only未测/HWprecisionSLO ND。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch11:146](../../../../books/part-02-model/11-tokenizer.md:146) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation](https://arxiv.org/html/2609.21369v1)

exact-v1 必要范围 III sensorSign+PELT/modalHamming/greedyframebudget与规则narrative、V TI–V；offline earliest-failure onset与终态分类/在线guard不同权限。retrospective整段+最终fail，不含恢复transient；MAE只correctlydetected failure、binary高非onset准；长horizonMAE变差/reflection50→100不更好，GPT5judge说明不因果proof/规则不保sensortruth。运行alarm不同信息budget，CPD/VLM/annotation、采样漏/timeout成本须分账。 root独立核必要source→fresh owner及真实两段/邻接写后通过。实际唯一owner [Ch26:791](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:791) 对应正文保旧方案/反证/fallback；非作者已释放窄锁。详见[本批必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式96有限同步)。

### [Prediction Dynamics in Depth-Recurrent Language Models](https://arxiv.org/html/2609.21383v1)

exact-v1 必要范围：固定候选margin/终点诊断与prefix检验、A1–A2；固定候选的相对gap/有符号终点变化与retrospective诊断分权。当前唯一winner a、g_b=s_t,a−s_t,b>0、δ=s_T−s_t、u_b=δ_b−δ_a，终点严格保留当且仅当每个g_b−u_b>0；共同平移不改比较，osc(δ)只给最坏相对变化，不能最大update配最小gap宣称实际翻转。δ读取未来，是completed-trajectory诊断非online stopper，答案保留非真值；固定多选/quarter grid T32vs4不外推开放生成，prefix quotient逊mean-centering，2.54%高于2.5%目标不作有限样本保证。A1–A2固定revision的32题F3与独立128题F1不同人口，Huginn/Ouro BF16 recurrence/FP32 head、5000whole-question bootstrap，几何百分点不是执行latency。 sep22_resume_v3独立必要source→fresh owner/literal与实际两段及邻接写后PASS，root授权窄锁已释放。实际owner [Ch17:570](../../../../books/part-02-model/17-transformer-layer.md:570)；uniqueSF与旧机制/fallback保留，非整日报Gate。详见[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式100有限同步)。

### [A Scene Language Model for Open-Vocabulary Scene Mapping](https://arxiv.org/html/2609.21400v1)

exact-v1 必要范围：text-state/ADD–EDIT–REMOVE方法、受限mapping/检索评价与G2.3/G3；text map稀疏操作与每对象corruption的修订/保留分工。对象label/description/world position为text state，pose/depth选可见entries、RGB→ADD/EDIT/REMOVE与2Danchor回投3D；每对象独立corruption训练修订，未提及保持。文本丢细节、有限纠错误触正确entry，同A100 mapping843/965ms高于258/275ms约三倍，memory较小不是更快；机器人移动≥.5m才处理frame，不逐frameSLO/动态长期安全。point-in-box与原IoU协议分开，pose uncertainty/移动人更多duplicate。Jetson BF16/NVFP4 vLLM.19与FP8 v.13不能纯归precision。 sep22_resume_v3独立必要source→fresh owner/literal与实际两段及邻接写后PASS，root授权窄锁已释放。实际owner [Ch25:396](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md:396)；uniqueSF与旧机制/fallback保留，非整日报Gate。详见[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式100有限同步)。

### [DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement](https://arxiv.org/html/2609.21423v1)

exact-v1 必要范围：子目标树/repair方法、same-source/reset对照、A3/B2；same-parent尝试树与recovery重审继承issue，不以历史通过关闭当前父任务。连续action–observation子目标nested tree，只同parent压缩重复attempt并保source，后继recovery重审issue；完成分支压缩/unfinished展开obligation，构建动作保留供fresh重建，derived analyst判断非hidden verifier或FS事实。固定同run0信息源，posthoc outcome仅评价端，recipient环境/context重置；3重复TerminalBench只same-task retry，privilegedVF修复更多但丢历史成功。A3 7308outcomes/1782仅completedcalls，未知usage不补0；B2明确run0+feedback+rerun合计2.96USD，36.6%只feedback+run1相对run0，不说论文无总cost或完整workflow同等省。 sep22_resume_v3独立必要source→fresh owner/literal与实际两段及邻接写后PASS，root授权窄锁已释放。实际owner [Ch77:436](../../../../books/part-07-agent/77-memory.md:436)；uniqueSF与旧机制/fallback保留，非整日报Gate。详见[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式100有限同步)。

### [GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](https://arxiv.org/html/2609.21432v1)

exact-v1 必要范围：V-B新OPD公式/证明、V-C符号反例、VII实验；新OPD正权诱导分布/组内中心化平方损失与原PG无偏不同目标。每response正f、partition存在且same support，P∝exp(f logπ)，P_student=P_teacher仍指向原π相等；中心化f log(student/teacher)平方损失消prompt partition ratio，不需token对齐但需共同response/scoring/support。无importance ratio因为不同loss，不是离线无偏原PG；global zero-loss不保有限参数/样本/截断decoder或Adam收敛。长度f=|y|^-alpha最佳随teacher变化。V-C student>teacher却log比<0符号反向不采；仅新OPD，不重复NeurIPS2025 GVPO核心。VII各法LR三值grid/k4/256prompt及mini256/2epochs，OPD seed/HWdtype完整成本未披露，不移借旧10seeds。 sep22_resume_v3独立必要source→fresh owner/literal与实际两段及邻接写后PASS，root授权窄锁已释放。实际owner [Ch33:924](../../../../books/part-04-training-system/33-grpo.md:924)；uniqueSF与旧机制/fallback保留，非整日报Gate。详见[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式100有限同步)。

### [Weave: Fine-Grained Dynamic SM Scheduling in an MoE Megakernel for Compute-Communication Overlap](https://arxiv.org/html/2609.21483v1)

exact-v1必要范围：routing后SM/chunk方法、硬件profile与受限prefill评价；routing后每层每GPU的SM通信/计算与GEMM/combine分块共同选择。dispatch不chunk，comm完成dispatch后steal GEMM、combine全SM；dispatch远端token去重不等combine贡献合并。K上升小GEMMthroughput跌，α/throughput依硬件profile。4H10080G SXM NVSwitch EP4 BF16 batch1 ShareGPT2/4/8K prefill（消融16K），配置距实测最优平均8.2%，1.33E2E≠2.89layer；未验decode/SLO/恢复，codeuponacceptance不是复现。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch49:119](../../../../books/part-05-inference-system/49-tensorrt-llm.md:119)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [Adaptive World Memory 3D Foundation Model for Scalable 3D Mapping, Localization, and Rendering](https://arxiv.org/html/2609.21502v1)

exact-v1必要范围：GRU/runtime regulator方法、Apartment消融及五条真实轨迹；学习候选memory与runtime变化融合、local submap与global loop分责。GRU reset/update先候选M，sigmoid temporal×spatial二次blend非校准prob/严格零更新；decoder本帧point/pose在最终memory融合前，不称所有head用finalM。active M/keyframe/pose/pointmap/Gaussian，inactive保留/低overlap新anchor/globalSL4校正另owner；detached geometryconfidence不真值。单RTX4090/五轨迹平均ATE非每条最好，precision/controlSLO ND。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch25:404](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md:404)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [The Communication Bottleneck: A Round-Trip Study of Tree-Structured Expression Serialization in Language Models](https://arxiv.org/html/2609.21509v1)

exact-v1必要范围：树表达式serialization/符号oracle、guard分母与受限16×16实验；sender×receiver方向矩阵与无损结构接口对照的角色测量。2450表达式16model greedy/no thinking，原符号oracle只相同接口；完整suite guardfail0、missing/duplicate另记。任一成功非文本无歧义/全部失败非独立sender错误，guardfalse-negative抬高score不是保守下界；73.6% fault归因不采。same-semantic树拓扑微调与fewshot跨域不能泛transfer，共享oracle范围保。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch66:728](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md:728)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer](https://arxiv.org/html/2609.21514v1)

exact-v1必要范围：III共同keypoint/三expert分阶段方法，Tables2–3/OOD反侧；human/robot共享骨架future接口与robot-only action supervision。human估计与robotURDF/标定拓扑坐标/valid/time不同producer，human无robotactions；actionhead训练读GTfuture/部署generated。额外human/阶段/训练预算混杂，sim任务及backgroundOOD反退。8A800训练，real13frames384²stride6/73steps、simstride3/37steps，30Hzaction非video/keypoint/actionfull采样SLO，precisionconcurrencyND。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch26:485](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:485)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [VidOmni-Bench: A Benchmark for Fine-Grained Video Understanding via Spatio-Temporal Event Verification across Complexity and Duration](https://arxiv.org/html/2609.21521v1)

exact-v1必要范围：§3–4/B3–4/C1/D1–2；natural captioner claims与人验视频支持/Unknown分开。negative来自五captioner自然错误非gold规则hardnegative；timestamp错位≠事件不存在/重复随视频重新核。500video/五复杂度/多时长，pair macroF1；5annotator pool但每pair至少2/作者裁定、κ.50不真值；30video certificate限定，不拼T6/T8不同帧预算成matched因果，更高帧率不单调/audio效果相反。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch66:570](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md:570)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [What Must Survive? Exact Task-Information--State Frontiers for Resource-Sufficient Learning](https://arxiv.org/html/2609.21523v1)

exact-v1必要范围：§2 Th2.2 proof/Cor2.3/2.4/Th2.5proof、§3.1/§5；precompression task-advice任务分组联合rank与postcompression未知query不同。完整x可见、有限线性任务/≤Kadvice先state后具体task、continuousenc/dec单位球最坏精确p*=minpartitionmaxstackedrank。私有子空间直和等维才闭式，continuouscoordinate不是finitebit/KV/learnability；approx上下界group大小/singularvalues，strongNP-hard分组，固定keys有限query attention非自由continuation淘汰算法。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch22:448](../../../../books/part-02-model/22-long-context.md:448)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [From Retrieval to Recognition:How Vision--Language Models Become OCR Specialists](https://arxiv.org/html/2609.21543v1)

exact-v1必要范围：§3–6/AppA/B/D/Fig9–10关键counter；OCR专门化matched头identity/strength与因果贡献分别核。自由生成prefix replay，只合法未截断/完整reference匹配且有imageevidence tokens，independentpage split/layer matchedrandomhead controls。Qwen2/3VL2B top20大部分保留不证明features/circuit全部不变，deployprompt共同改变；Qwen3base table非全面胜random/文本非单调。固定QK/attention Vpatch仅logit差不翻winner，mass/Vdiffnorm未match不单独充分。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch23:790](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md:790)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [On Repulsive and Attractive Teachers: Separating Correctness from Behavior in Self-Distillation](https://arxiv.org/html/2609.21561v1)

exact-v1必要范围：§3–6/A2–3/B1–3；双privileged context attraction/repulsion与correctness verifier不同。balancedreverseKL algebra消student半logcorrect/incorrect，sharedstyle能否取消另验；actual sampled-token generalizedJSD非精确sameformula。Qwen3-4B数学288/Anagrams400，仅incorrectrollout且group双context/frozenEMA0/noGRPO；repulsion激活但不胜thinkingbaseline后lengthcollapse，Anagrams已thinkingattraction也有增益/tokenpoolshuffle反侧。mean@4非pass@4，trainseed/HWdtypeND。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF与旧机制/fallback保留，窄锁释放。唯一owner [Ch33:1022](../../../../books/part-04-training-system/33-grpo.md:1022)；不采用整recipe/部署保证，不代日级Gate。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式108有限同步)。

### [ME-Dex 1.0: Bringing Heterogeneous Tactile Sensing into World Action Modeling](https://arxiv.org/html/2609.21449v1)

exact-v1必要范围：§3.1–3.5/§4.1–4.5 Tables1–5/§5；future video/touch/action联合stream与observed mask明确producer而非预测真值。30layervideoWan2.2-5B3072/action1024/tactile512三expert，中间H-Bridge共享attn投影兼容，早晚独立；独立每modal噪声/σ,currentcondition clean,futureGT trainonly,jointflow推理读未来tac latent不是独立forecastprefix。异构normal+2tangent3×H×W/deadzone/asinh/normclip、canonical左/右finger/palm/observedmask；unobserved不同observedno-contact。冻结deterministictactileAE contact+force+transition/per-source归一化，source-specific forceMAE不跨平台直接比较。Engine simulationactionreplay加sensor相同window是模拟标注不真physical。RoboTwin27500CleanRandom50tasks另2500Clean→Random；DexJoCo1100demo11tasks/ManiFeel50each4singletrain，单trainingseed；DP-T/pi quoted/DECOofficial发布非uniformretrain。T1VA86.90Random→TacCond89.54→FullJoint90.60→HBridge91.92，不能各独立唯一因果；zero-current91.74接近observed91.92仍保tac训练/未来预测。FastTac小好piTac57.66<60.74；DexPhoto48<DECO76、ManiGear60<66。realSO101/PX/Xynova只qualitative不新量化闭环；§5明确高频触觉localfeedback未来工作，当前chunk间obs/replan。hardwareprecisionconcurrency/end2endSLO未披露，不借video30层训练推安全。actual现FuturetoAction/ForeTac有预测prefix与教师切换，缺三modal jointgeneratedfuturetouch和observedmask的接口角色。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch26:301](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:301)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [CompAdapt: Adaptable Composite Motion Modeling for Physics-Consistent Text-to-Video Generation](https://arxiv.org/html/2609.21455v1)

exact-v1必要范围：§3.1–3.5 Eq1–14、§4.1–4.3 Tables1–4、AppB/C/E/G（必要parser/成本与耦合反例，非全D/H）；不相交并行位移、时间串接与接触jump的组合接口分权。10D2Dcentroid/v/rotation/scale/area+mass，dualQwenparser motionseq12types/parameterdecoding separated numericverbatim vsadjectiveslabels vsabsentnone+deterministic sampling(AppB)非估计真质量。Eq6同initial state displacement加massmask，只有disjointcomponents exact/严格交换，coupled pure rolling v=ωr不可；temporal chainingterminalstate→nextinit，threshold contact separatelylearnedelastic2bodyjump resetsstate不通用contactmechanics。trajectory+warppatchrotation/scale与adaptiveblendWanMove生成解耦，不是guaranteedphysicalallfeatures。PriorMatching12pretrainmodule最低referenceMSE再L2anchorregularized100epoch5e-3AdamW/84frame;reference1of10其余9/5referencechoices，first28→84only12/34drop<.02，near22 .888/mid5 .854/far5 .515/adversarial2 .730。C saturationg980 PIS约.83但trajectoryerr爆，PIS只invariantstd/mean不是轨迹正确与真law辨识；三publicvideosSAM2tracking/derivedreference不能无跟踪偏。G pure rolling .784–.794 vsuncoupledslope .978–.982是additive边界，不采Eq3.4 guaranteedphysics。单RTXA6000/fixedrandomseeds非multi-seed；code/dataset releaseuponacceptance未核artifact，完整render steps/dtype/latencySLO ND。AppB2000parserlabel accuracy不是真实质量数值准确。actual13006 kinematicplan/localgradientrouter只proposal，不含continuous parallel/sequential和contact jump分开的generator接口。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch24:1258](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md:1258)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [Understanding LLM Quantization through Activation-Guided Compensation and Orthogonal Residuals](https://arxiv.org/html/2609.21450v1)

exact-v1必要范围：§3/§4.1–4.6/§5–6，B.1 Theorem1完整证明 Eq41；固定量化输入列空间中可补偿误差与正交不可消残余分账。固定P、Z=XP、V=WP^-T，量化A=Ztilde−Z，Vstar^T=V^T−Ztilde†AV^T。精确J=||Ztilde(Vtilde−Vstar)^T||F²/T+||(I−Π)AV^T||F²/T，Π=ZtildeZtilde†；固定输入下正交残余不由任意weightchoice消除，unrestricted最优不意味着lowbit可实现。作者明确CoreQ full-columnrank先例，不能说投影恒等式首次新发现；这里只保与actual原始target不同的compensable/orthogonal职责。CO+regular不是新的精确加项，是上界分解启发；L2缩放来自Frobenius/CauchySchwarz放宽、L∞另放宽，实践fullX代Xreg。理论dynamic per-token uniform无clipping，W4A4KV4实验clip.9/.95/GPTAQ128WT2train/scaling512不能照搬无clipping证书。8模型1–13B更低PPL非所有6task最好：Llama3.2-3B低SpinQuant1.09pp；RTN10候选top3GPTAQ与WT2val选择增加calibration预算，100seeds子采样不等部署SLO，未核code/复现、HW完整runtimeND。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch49:934](../../../../books/part-05-inference-system/49-tensorrt-llm.md:934)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [Adaptive Rollout Truncation Based on Epistemic Uncertainty for Efficient Offline World Model Training](https://arxiv.org/html/2609.21482v1)

exact-v1必要范围：III/IV/V/VI/VII、TablesI–II、AppA/B/E/F；epistemic截断改变训练gradient-depth课程不授部署认证。这是训练期gradient-depth curriculum而非部署planning-gate。sharedGRU+5bootstrapMLP或MCdropout10pass，50single-step warmup+10full32；hmin4后batchmean epistemic≥T首次stop，仅已生成步收gradient。anchor@k是阈值参照horizon不是actual长度；warmup末10次median/≥3runs均值frozen同reportedseeds。ANYmalD31 250segments max200 mean192≈6M45obs12actions/Ant6000×1000约6M105/8；offlinePPO行为走向更强policy非onlineRL。segment-level .1val，32history+32forecast stride32/zscoretrain-only。Fixed32 RMSE32 .314、160 .429/3250steps，Fixed8 .274/.458/1090，Adaptive2 .288/.389/924（三seed）；短期不是最好。AppE含GRUhistoryFLOPs Fixed32 60.2PF vsAdaptive18.0但前者ownconvergence后者fixed32accuracy，不是纯同停点GPUtime。AppF明确无coverage calibration，来自每seedadaptive运行的scripted length replay复现withinseednoise，不能将unique uncertainty causal收益外推；schedule oracle是post-run非deployablemanual。MCdropout参数对lengthgrowth敏感，额外uncertainty/head/candidate/warmup开销须计；HWprecision与真实physicsSLO未披露。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch25:299](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md:299)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [Micro-Collaborative Poisoning: A Distributed Attack on RAG Systems](https://arxiv.org/html/2609.21573v1)

exact-v1必要范围：多片段联合方法、双数据库实验与DPAR/OLS边界；joint-context与来源独立性补局部passage检查盲区。这项检查增加联合阅读、支持关系与 provenance 维护成本。受限攻击实验中的 DPAR 是启发式 proxy，OLS 关联不构成通用 detector 或 defense 证书；top-k 增大也不总是更安全，不能只用一个成功率决定检索预算。应沿 exposure、selection、use 到 answer effect 分别记录攻击路径，并用真正独立的支持与 utility 回归复测。组合证据不可信或风险无法隔离时，回退单一可信来源、缩小 Context 或人工核对，而不是从局部正常文本推定联合安全。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch76:849](../../../../books/part-07-agent/76-rag.md:849)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [GestureFAR: Streaming Co-Speech Gesture Generation with Flow Autoregression](https://arxiv.org/html/2609.21576v1)

exact-v1必要范围：head-only distillation与cached conditioning方法、BEAT2质量/FGD冲突；causal AR历史与continuous flow head预算/蒸馏分别验收。one-NFE 只计该 head，不包含 AR、decoder、buffer 与条件缓存成本。训练缓存的条件与部署自产生的 motion history 可能失配，须另验 streaming 累积误差及端到端延迟；BEAT2 的受限主 speaker 结果不认证任意角色、时长或实时 SLO，FGD 两表的尺度冲突也不拼接为同一质量点。缓存身份或生成质量不成立时，应刷新条件、增加 head 求值或保留原多步 sampler；较轻 head 不自动获得整个 pipeline 的质量与时延保证。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch24:361](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md:361)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [HyperParallel-FSDP: Topology-Aware Fully Sharded Training with Layout-Driven Muon on Ascend SuperPods](https://arxiv.org/html/2609.21594v1)

exact-v1必要范围：module-boundary layout及双mode方法、一步gradient/16Ascend60-step评价；同module placement plan的验证DTensor与生产local/compiled collective双mode。这种分工把语义检查和 hot path 成本分开，却增加 compiler、边界 coverage 与 fallback 的维护。opaque 域、具体 collective 或尚未支持的布局不能因同一 plan 就标已验证；一步 gradient 对照和 16 Ascend 上有限 60-step 运行，也不证明所有 optimizer 状态 bitwise 一致或长程收敛等价。不同 mode 的速度对照不能把全部差异唯一归因于原生 DTensor metadata。边界无法表达、梯度/状态不符或收益不足时，保留验证执行、显式通信与成熟分布式 runtime。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch36:634](../../../../books/part-04-training-system/36-distributed-training.md:634)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [Trading Depth for Time in Recurrent Transformers](https://arxiv.org/html/2609.21605v1)

exact-v1必要范围：continuous thought appended position方法、parallel-training/sequential-decode与compute反例；continuous thought追加位置/KV与same-position recurrence是不同计算/状态预算。训练可以并行 refinement，decode 却按这些连续位置顺序展开，二者的依赖图和实际成本不能互换。block application 数不等 FLOPs、KV 占用或 latency：同 block count 的物理加深仍可更好，vanilla baseline 也未按全部训练 FLOPs 匹配；分别训练的 K 不授予推理时任意切换预算。受限结果只支持参数容量与内部计算的一个取舍。串行等待、cache 增长或质量回退时，固定深层、原共享 loop 或可审查的显式 CoT 仍合理，不能把 continuous thought 写成免费计算。 root独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch17:501](../../../../books/part-02-model/17-transformer-layer.md:501)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [Calibrating Teacher--Student Discrepancy for On-Policy Distillation](https://arxiv.org/html/2609.21619v1)

exact-v1必要范围：§2–4 Eq1–11/T1–3、A2/A6/A8/A9 T12–13；有限teacher prompt干预区间与student超区间差额监督。这个区间来自有限 prompts，不是统计覆盖保证、token correctness verifier 或知识/风格的可识别分解；放宽系数和 probe 内容会过滤有用信号，reference-solution probe 在受限结果中甚至低于初始 student。两组 Qwen 数学训练的平均收益与全局优势缩放、同稀疏度随机 mask 对照提供局部支持，但强 TSD 阈值对照已接近该结果，未披露跨训练 seed 不确定性，不能据此签发“只学能力”的因果结论。每 token 两次额外 teacher 评分并非免费：同硬件计时只在较小 teacher pair 更快，30B teacher 两种 student 反而更慢，长度变化也参与总成本。probe 不可信、保留量过小或端到端预算不合算时，保留普通 OPD、已验证的其他选择性监督或不更新；正确性仍由独立 outcome/holdout 验收。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch33:1026](../../../../books/part-04-training-system/33-grpo.md:1026)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations](https://arxiv.org/html/2609.21650v1)

exact-v1必要范围：III–IV Tables/provenance及V真实路径；privileged成功示范覆盖作为RL初始化不同于teacher在线正则。这种覆盖来自额外 ground-truth pose/depth/segmentation、LLM 失败后调参、轨迹筛选与 SFT；fixed PPO compute 不是整个 pipeline 等预算。SynthDemo-RL 的 57 个 perturbed LIBERO-PRO 任务中，直接 PPO 在所给预算下救回原先未观察成功的 27 项中的 10 项，synthetic SFT 则三 seed 都取得每任务至少一次成功；coverage 仍随 50 次 trial 和成功次数门槛变化，初始化覆盖与最终收益的相关性没有隔离难度与整套介入。SFT 会降低部分原已解任务，RoboTwin 的 place_cup 又未获 RL 增益；人化 teacher 运动并未消除 SFT gap。Teacher synthesis 和 PPO 都依赖目标仿真，真实 closed-loop 初试失败后，四条件各 20 次 open-loop 只证明匹配初态的轨迹可执行，不证明闭环迁移或安全。无可靠仿真/成功支持时保留人工示教、离线数据或保守策略，并分别验收数据成本、target coverage、训练回归与真实闭环。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch26:232](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md:232)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [GUARD: Natural Forgetting in Large Reasoning Models via Guided Answer-Reasoning Distillation](https://arxiv.org/html/2609.21677v1)

exact-v1必要范围：§3–5/T1–6/A1–3/B1/C1–4；non-disclosing reasoning/boundary safe-exit行为替代不是知识擦除证书。改写审核、checkpoint 选择和蒸馏都付出额外离线成本，top-k 重新归一的 forward KL 也不等于完整词表行为不变。有限 R-TOFU/STAR 与两种 distilled LRM 中，分块/完整 safe-exit 对照支持联合约束 reasoning 与答案，但改写审计仍有残余披露和幻觉，改写、选点与主要质量 judge 复用了同类模型；小规模人审与跨 judge 一致只校准对应输出切片。攻击改写、jailbreak、多轮后仍有残余泄漏，retained reasoning 切片也会退化，其他方法在部分 forgetting 指标更强，不能称全面占优或永久删除。应分别测 reasoning/answer 披露、结构质量、unsupported substitutes 与 retained utility；NFRS/格式 gate 不替代内容恢复攻击，域外或证据不足时保留访问限制、独立再测或重训，不用连贯拒答签发 erasure。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch72:2456](../../../../books/part-06-ai-infrastructure/72-security.md:2456)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents](https://arxiv.org/html/2609.21686v1)

exact-v1必要范围：§3–6 Eq1–6/Prop2/T2–4、C4(T-C7)、E1–3；selected units与observer recoverability、any/full/unique泄漏分母分账。Canonical exact matching 阴性也可能只是未恢复完整 unit，而可用敏感值已出现；补充盲化于 provider/attack 标签的 reference–visible-output 人审，区分无恢复、部分有用与操作等价的完整恢复，但 semantic layer 只有在确实包含 exact recovered set 时才有集合支配关系，不能凭名称给普遍 recall 保证。作者五 provider、有限查询与分层 200 输出审计支持该局部盲区，不代表所有流量的泄漏频率；naive dump 在 RAG 上可超过主 recipe，provider/表面/检索设置也会改变排序。完整事件定义要求 U 非空，而公开 CER 汇总式省了该 guard，不能据此宣称空选择 trial 实现已正确；工程验收应另核 empty-selection/extractor 行为并保留 Unknown，而非补造作者修复。审计增加敏感 trace、标注与组合攻击成本，不能转换成 DP、自然发生风险或部署安全证书；边界不可校准时缩可见通道、访问范围或不发布，并在相同 observation contract 下重测。 sep22_resume_v3独立必要source→fresh owner/pre及真实两段/邻接写后PASS，uniqueSF、旧binding与fallback保留，窄锁释放。唯一owner [Ch72:321](../../../../books/part-06-ai-infrastructure/72-security.md:321)；不采用整recipe或部署保证。[必要记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-正式120有限同步)。

### [Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models](https://arxiv.org/html/2609.21740v1)

exact-v1必要frozen JEPA四接口residual/最近五步one-step及Red-Density/Cube反例；局部残余把更新限制在较少参数，却仍支付梯度、缓存、适配与规划成本，参数高效不等总 compute 更低。受限 Sandwich-Residuals 结果中，Red-Density 与 Cube 仍有反例，不支持任意变化都可由这组接口吸收或通用稳定闭环。表征目标可能随 adapter 移动，one-step 改善也不证明长 horizon 校准。观测身份、身体状态或适配质量失配时，应回到冻结基座、更短预测与真实观测，而不是以较小更新签发物理模型正确性。 深入知识差额仅冻结JEPA接口的residual适配与校正表示目标分账。已实际写入 `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 274/276 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [World Modeling in Transformers](https://arxiv.org/html/2609.21748v1)

exact-v1必要map probe/causal teleport/localization/legal move/goal compass及Taxi深远OOD；有限 Taxi 分布外实验在更深更远位置、包括未训练位置 99 上暴露这些分离，连续正确位置输入只用于诊断，不是已部署传感器。模型大小与 map 可读性、采样行为之间的局部差异不形成“小模型普遍更好”的结论；受限 probe 与干预也不证明所有环境拥有同一坐标。位置/地图审计、行为干预与约束编码付费，localization 不可信时应回真实观测、显式地图和合法 action gate，不用可解码的 latent 自动认证导航。 深入知识差额仅地图可解码、定位、局部合法与目标方向需分别验收。已实际写入 `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 68/70 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models](https://arxiv.org/html/2609.21787v1)

exact-v1必要§5及A9–A14 factual Jacobian chain/moving image、GRU rank4/LSTM rank6与全幅反例；这种诊断增加 Jacobian、SVD、重启与未来观测成本。受限两对象 GRU 的 rank-four 结果与 LSTM 的 privileged counterfactual anchor rank-six 是不同设置；全幅干预的部分失败阻止把局部 rank 解释成任意幅度或任意 recurrent state 的缩维保证。子空间漂移、局部线性近似失效或未来响应无法核验时，应保留较完整 latent、缩小干预或回到真实观测；表示压缩、因果方向和响应大小仍需分别验收。 深入知识差额仅future-response低rank局部image不授固定closed latent。已实际写入 `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 72/74 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [CASCADE Against Jailbreaks: Combination Across Stages with Controlled Attack-Defense Evaluation](https://arxiv.org/html/2609.21793v1)

exact-v1必要rewrite/filter顺序、utility top-k筛选攻击、matched population与资源边界；ASR 与 utility 若来自不同模型人口，就不能拼成一个质量—安全点；少数 modern model 的 matched 回归也只支持局部结论。Parameter count 只是资源 proxy，不是 VRAM，H100 平均时间不是 tail SLO，单轮攻击不覆盖 adaptive、多轮或全部威胁。组合新增 rewrite、guard、校准与攻击成本，某些处理次序还会降低 utility 或扩大攻击面。规则稳定、风险隔离时成熟单 guard 仍是较清楚的低成本分支；跨域或组合退化时缩回已验收路径，并保留确定性 enforcement。 深入知识差额仅串行rewrite不交换、组合子集比较不认证全局Pareto。已实际写入 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 551/553 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence](https://arxiv.org/html/2609.21942v1)

exact-v1必要III–VII/A/C/F、sensor shuffle/held-out、25校准与35–36测试及改措辞反例；这个审计和代价参考来自注入式 tabletop 仿真，部分 grasp 原因本就不被 renderer 描绘；六种受限 VLM 的选项顺序、遗漏 force telemetry 与融合退化表明，问人率不能单独当可靠自知。模型可从 telemetry 受益但仍远低于 classifier，且一条 token-logprob 通道有局部选择价值，不能推广为所有 confidence 必然无用。校准仅 25、test 35–36 episodes/family，成本是指定单位、oracle 只作离线参照；脚本人答复不随问句变化，换非菜单措辞后部分 model 收益大跌，未验证真实多轮对话或物理恢复。额外 sensor 读取、审计与校准付费，model/环境/成本改变须重测；无法判断或状态已危险时先停到可信 safety checkpoint，再使用显式人工/保守流程，不让统计最优参考授予安全执行。 深入知识差额仅观测可诊断性、model可利用性与人的答复权限分层。已实际写入 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 811/813 两段；sep22_resume_v3独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments](https://arxiv.org/html/2609.21948v1)

exact-v1必要III–V Eq1–13/TI–V及官方appendix A–F必要三页；手部重建、URDF/MJCF 状态转换、pair normalization、validity 与双流训练增加成本，也会继承几何误差或丢失任务证据；motion probe 和三类跨 embodiment retrieval 只检验局部可读信息，不证明 universal action semantics。受限 GR-1-only 对照同数据/优化预算支持该分支，但 UEMR 同时移除三个设计，不能隔离唯一收益；多 embodiment 训练又同时增加 batch 与步数，不能把对 GR-1-only 的增益全归因于数据可迁移性。四项 XHand 真机各 50 次只支持所测闭环，部分 baseline 还读不同相机且 backbone 不同，平均领先不代表全面优越或物理安全；附录对 Stage-2 监督 token 数的正文/表口径不一致，不继承精确该配置为已验证实现。几何/坐标失配、码语义不稳或预算不足时保留 RGB latent、显式原生 action labels 或独立 embodiment policy，重新做动作闭环与回归，而不是以重建/retrieval 分数授权执行。 深入知识差额仅共享bimanual几何transition监督与native action head分权。已实际写入 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 200/202 两段；sep22_resume_v3独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [Detecting Pretraining Data in Large Language Models from a Free-Energy Perspective](https://arxiv.org/html/2609.21888v1)

exact-v1必要§3/§4.1–4.4 Th1–2/§5.1–5.4/§6、AppA/B必要全证明、D2/E1与H少量明确反侧；理论的随机训练、平滑/近最优及 population 条件不是实际 LLM 的优化证书；方差降低也不保证任意 score distribution 的 AUROC 或低 FPR recovery 改善。实际 first-occurrence token 聚合、固定 λ 与时间/同来源对照仍要单独验证，受限 MIMIR 的部分来源/规模不如普通 loss 或其他基线，受控继续训练只说明对应 exposure 切片。额外 logits、entropy 读取和 corpus/control 校准付费，不是有语料身份的合规 verdict；条件不可核、模型/语料变更或信号失准时，保留原始 loss、matched controls、provenance/canary 与 Unknown，而不由一个较高总体 AUC 断言某文本进入过训练集。 深入知识差额仅loss–entropy条件control-variate而非membership裁决。已实际写入 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 250/252 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [ExpBoN: Exponential-Noise Best-of-n for Efficient Test-Time LLM Alignment](https://arxiv.org/html/2609.21899v1)

exact-v1必要§2/§3.1 Th3.1–3.2/§4 Alg1 Th4.1/§5.1–5.2/§6、7.1 Lemma7.1及Th3.1proof、7.5Th4.1proof、7.7implementation；这些权限依赖有限 support、独立样本/噪声、真实 score 上界与固定评分规则，不是任意 judge threshold 的提前停止保证。加入截断的 draft–target likelihood ratio 会改变目标，更多候选只能缩小有限-n误差，不能消掉 clipping bias；另加 reward gate 或 base fallback 也不自动继承前面的 sampling law。候选若已全部预生成，提前退出省的是 target/reward 评分而非这些生成；受限实验的 token-compute估计与每步墙钟也有不同分母。support、上界或成本不可靠时保留完整候选评价、标准 BoN/target sampling，正确性仍由独立 verifier 验收，不用分布定理证明所有任务质量或免费提速。 深入知识差额仅finite-n mixture与conditional hit授权提前停止评分。已实际写入 `MODEL-SAMPLING` [Ch20](../../../../books/part-02-model/20-sampling.md) 310/312 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [End-to-End Hard-Label Cryptanalytic Model Extraction Using Efficient Sign Recovery](https://arxiv.org/html/2609.21941v1)

exact-v1必要§2–3.7/Prop1/Alg1/T2、§4.1–4.3/T3；前层误差、未恢复项、不可达权重和伪 signature 会传播；按 normal-span violations 迭代修正只是有限数值程序，不能升级为完整参数精确恢复。受限 MNIST/Fashion-MNIST 的宽16、4/6隐藏层实验先支付数十亿至数百亿取点查询，仍排除 dead/almost-dead neurons，persistent 分支未测；高 agreement 来自指定 standard-Gaussian 输入，不证明全输入、自然数据或大型语言模型等价。Hard labels 本也不能唯一识别共同 logit 平移/缩放，故参数精度与指定分布上的行为 fidelity 要分开。防护继续在实际接口、输入能力与全阶段跨身份预算上验收，保留 access control、受限输出与人工调查，不因局部恢复成功或单一查询率断言普遍可盗取/不可盗取。 深入知识差额仅已恢复局部map与competitor signature下分离hard-label sign。已实际写入 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 2854/2856 两段；sep22_resume_v3独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [Schedule optimization for tau-leaping in masked discrete diffusion](https://arxiv.org/html/2609.21960v1)

exact-v1必要Alg1–2/§2.2/§3 Cor1/§4 Th2及AppB/C必要证明/§5–6；最优 stationarity 不自动保证唯一解：shooting/bisection 要另有单调条件；profile 随长度一致收敛到连续严格正极限、且使用固定递增光滑 schedule 时，优化只改变 N/K 的 leading constant。特定退化的 exchangeable-mixture profile 才展示同 logarithmic 步数下不同 factorization 阶，不能转成通用 LM 质量定律；随机块大小也不等同固定逐位置计划。完整 profile 要付离线估计与优化成本，模型条件误差、有限样本及 coefficient 差分会污染它，toy exact-target 检查不是已部署语言模型或真实 latency/SLO 证据。profile、独立分块或成本条件不成立时保留原 confidence schedule、固定块或逐位置 sampler，并以实际输出质量、生成预算与墙钟独立验收。 深入知识差额仅learning与factorization KL分账及profile schedule成立条件。已实际写入 `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 238/240 两段；sep22_resume_v3独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [Abstention and Noise Filtering: Two Missing Primitives of Softmax Attention](https://arxiv.org/html/2609.22005v1)

exact-v1必要query零option/valuegate机制及FineWebEdu/projection attack反例；更强过滤会损失有用证据：受限 FineWeb-Edu 模型中的 norm gate 在较多 junk 时反而退步，投影对齐的攻击又可绕过特征过滤。模型规模、训练切片与有限 seed 不认证任意 pretrained Transformer，未测吞吐也不支持更高生产效率。零 option、特征门与旧 null/sink 都应按相同任务、预算及可观察输出验收，并计新增参数、校准和 kernel 成本；判断失准时保留成熟 softmax、显式 null 与外部输入检查，不能用一个 gate 自签鲁棒性。 深入知识差额仅abstention与noise filtering算子尺度/失效不同。已实际写入 `MODEL-SELF-ATTENTION` [Ch14](../../../../books/part-02-model/14-self-attention.md) 260/262 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [$λ$-Controlled GRPO: Turning Flow-Matching Ratio Instability into a Budgeted Resource](https://arxiv.org/html/2609.22041v1)

exact-v1必要Gaussian ratio/mean reduction、LambdaNormT/detached λ/ESS及GenEval反例；选择 λ、校准 surrogate 与监测 ESS 增加成本；启发式有效样本量不认证 support、无偏或训练安全。作者 single-seed pilot 与 GenEval 退步的反例只支持局部稳定性/质量取舍，不能将 ratio 数值更温和写成所有任务更优。应分别保留真正条件律、归一化 convention、阻尼前后信号及总采样/更新成本；失配、质量下降或 proxy 无法校准时，缩短 replay、增加当前采样或回退已验收目标，不让预算参数替代独立 outcome 验收。 深入知识差额仅真实条件律ratio与训练budget surrogate分账。已实际写入 `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) 1224/1226 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [Available Guardrails: Certifying Selective Prediction across ML Systems](https://arxiv.org/html/2609.22048v1)

exact-v1必要独立IIDcert与固定ordering连续partition DP及held-out选择收益；规划、选点与独立 certification 各付数据成本。受限 held-out 改善主要来自 selection，不证明结构化 family 本身普遍更强；较高取得证书的机会也不降低证书原来绑定的分布、预测器与条件。部署 shift、分组或阈值变化后，旧证书不能直接复用，应取得 fresh labels、重新认证或 abstain。数据不足时保留简单固定 groups、人工升级与明确未认证，而不是以 planner 的 expected support 代替实际风险证据。 深入知识差额仅certificate validity与finite-data availability不同。已实际写入 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 3009/3011 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [Predictable Failure in Multi-Hop Retrieval: Score-Distributional Confidence Scoring and Abstention](https://arxiv.org/html/2609.22056v1)

exact-v1必要top5gold support/ANNfeatures、§5.3CWAR/§8Bayesbest争议与MuSiQue校准；Logistic 输出并不天然 calibrated，有限 MuSiQue 上的 MLP、tie 与 ECE 对照也不是所有 query 的风险证书。不能采用‘经验 CWAR 必随 threshold 单调’、空选择集合默认风险零，或将 Bayes 最佳规则的结论直接授予训练得到的 scorer；这些断言不由局部 feature 效果补齐。标注完整 support、校准 gate 与维护 regime 增加成本，需并报 coverage、support completeness、answer quality 与实际 retrieval/生成预算。目标或校准不可信、域移或 evidence 不全时，回退扩大检索、独立 verifier、已有联合校准/abstention，而不由廉价分数签发安全回答。 深入知识差额仅support completeness与answer正确分权/CWAR争议不采用。已实际写入 `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) 544/546 两段；root独立必要source→fresh owner及actual两段/邻接POST通过，旧机制/source binding保留。详细依据见[唯一必要证据](../_sources/daily-20260921/arxiv-evidence-restoration.md)，非日Gate。

### [RheoSampling: Resolving the One-Hot Dilemma in Stochastic Dynamic-Tree Speculative Decoding](https://arxiv.org/html/2609.21827v1)

采用精确v1，必要范围：§3.1–3.3/Alg1、§4 Th1/3、§5.1–5.4/Table2/AppendB sparse支持与C1–4全部关键losslessness/slot proof。m≥1 proxy=min(q_m,z)≥q_(m+1)、constant in Y但是constant alone不足；sample-before-fill固定第m+1slot；global score产品/shallower→left tie祖先闭合，C4固定保留父/前k equivalence→新slot决定性，后sampletail不变。Verification 用actual tempered tail不是treeproxy；min1p/qtilde及positive residual，samplepruned则target补足。m0正文q1+epsilon vs C3 z=1身份不一致且epsilon未给≤1，不采用其普遍祖先monotone/全m保证。3targets6tasks各80题，A6000/EAGLE3原checkpoint/noFT/tree60depth8/3seedsT1，Llama τ5.04→5.25 vs速度2.84→2.93不同分母；m1局部最好/低T优势收窄/m≥3stochasticpruned；Top128仅91.0%massFull100%，4.84vs4.89AAT/Full18.8msPyTorchnative未优化，不完整QoS。HWprecision未披露precision，不补。actual22098 only generalpre-draw/无放回与selectionbias，没有proxy与realproposal dualrole必要rankingbound，窄gap支持I拟两段。不采用OT approximate‘almostalways’为普遍优势，无code复现。

Books：整合 `INFER-SPECULATIVE-DECODING` [实际正文](../../../../books/part-05-inference-system/48-speculative-decoding.md) `251/253`；root独立必要source→fresh owner及真实两段/两侧POST通过。差额与最小两段见[唯一最终证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不是全recipe采用。

### [Watermarkable Multi-Draft Speculative Sampling via Poisson Processes](https://arxiv.org/html/2609.21858v1)

采用精确v1，必要范围：§3–5/Alg1–4/Def4.3/Prop4.4/Th5.1、A4Alg6–7/ThA5–6完整有限实现proof、B1acceptance完整proof/C1.1stopping-time全proof/C2definitions、§6/Limitations与D1、D5(T14–15)必要population/计时/quality。每context keyed Poisson base过程，target P映射first arrival始终emit；Q MPFR list相同process mapped有iidQ marks可能重复，mergecontext multiplicity。targetwinner在draftset才continue，否则emitwinner后stop；原定目标law由context-independentidealExp clocks链式证明，不要求Psupport⊆draft但各对referenceμ AC。finiteKsupportAlg6 K×BExp arrivals选topB exakt iid；A6只有idealindepclocks证明PRF实keypseudorandom不真独立。Th5.1在singlecontextiidQ list acceptance下界≠totalrate/latency。sharedkey/fullcontext/randomness相同时tokenchain由target侧定义、drafter改变stoplength非content；statement仅commonpositive supportτ给conditioning，非普通PRNGseed顺序消耗自动不变。Watermarkunbiased是keys/randomness marginal非每fixedkey纯target；detector依赖key/prefix不是法律provenance/adaptive attack resistance。MainT1 caption Llama3.1 vsD1/D4正文Vicuna secondpair未统一，窄采用不拼该身份；D1 float16 singleH100 topk50topp1T1max128/1000prompts/多seeds但mean±std acrossprompts vsmain3seeds口径不要替换。D5 .990minpair notactualalloutputsbyteidentical，LPPLparity不是distributionproof。当前couplingbookkeeping slightlyslow作者承认，通信/水印/efficiency根本tradeoffunclear。No fullcode inspection/reproduction，不採每B‘breakingno-go’普遍结论。freshactual经典qratio/residual/targetlaw有，缺targetkeyedsampler独立draftstop角色及多Poissonarrival预算，拟I精确机制Ch48不复制Ch72水印审计。

Books：整合 `INFER-SPECULATIVE-DECODING` [实际正文](../../../../books/part-05-inference-system/48-speculative-decoding.md) `119/121`；sep22_resume_v3独立必要source→fresh owner及真实两段/两侧POST通过。差额与最小两段见[唯一最终证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不是全recipe采用。

### [SkelWAM: A Skeleton-Guided World-Action Model for Zero-Shot Cross-Embodiment Manipulation](https://arxiv.org/html/2609.21983v1)

采用精确v1，必要范围：root实际exact-v1 §III–V/TableII；作者fresh归一化/协方差→privileged3D邻接。25D六centerline15offset/TCP3/rot6/jaw共同视觉/action；机器人视觉遮罩背景补齐同canonical空间；future仅训练；source统计/weights冻结≠target标定/decoder零工程。rigid保priorbodyintent+measuredTCP/jaw，continuum还orientation≠fullbody真值。w/oA同时w/oD混杂、wrist43.0近43.3；1k simulation/source467，真机仅3任务定性，43.3不授普遍zero-shot。HWprecision/SLO ND，无code复现。

Books：整合 `MULTIMODAL-EMBODIED-VLA` [实际正文](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) `75/77`；root独立必要source→fresh owner及真实两段/两侧POST通过。差额与最小两段见[唯一最终证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不是全recipe采用。

### [A Lie Detector Test for Language Models: Reading Knowledge a Model Won't Reveal](https://arxiv.org/html/2609.21996v1)

采用精确v1，必要范围：root实际exact-v1 §3.2 Eq1–3/§4–5；作者fresh16890→运行期身份邻接。PIRcorrect-minusdecoys，honestcorrect定义标签；部署assay需该模型basecheckpoint，referencefree≠无候选标签基准；freeform来自elicited+deployed样本，peak/divergence不同对象；steeringsufficient非necessary，necessitynegative；单seed strictrotation样本条件；anti-probe保capability让readout失效，insample保证撤回。静默不可分neverknown/removed，无永久erasure。

Books：整合 `PLATFORM-SECURITY` [实际正文](../../../../books/part-06-ai-infrastructure/72-security.md) `2560/2562`；root独立必要source→fresh owner及真实两段/两侧POST通过。差额与最小两段见[唯一最终证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不是全recipe采用。

### [Extending Decoupled Attention to Dense Prediction and Masked Training for Multi-Channel Images](https://arxiv.org/html/2609.21629v1)

采用精确v1，必要范围：exact-v1完整摘要/§3.1–3.2 Eq1–7/§4协议/§5.2对照与mask-ratio反例。纠正原仅microscopy/science拒收：independentmask保留后同compactindex不再同grid身份，genericattention接口实际变化。equal-k二channelHungarian squaredgridcost；多channelstarreference C−1 assignments仅starcost精确非allpairjoint；randomref平衡perchannelerror mean.87不变；row/Hilbert平均距离改善不解释质量、sharemask100%对应但失diversity，heavy.75趋同。ViTS16/RTX3090/sixlimitedtasks，precision/seed/latencyND；不复现。重要反证：原§5.2‘shared retainedpatch必自身因0distance最优’不成立：同一行A{0,2},B{2,3}，匹配0→2,2→3成本5，小于0→3,2→2成本9。只不采用此普遍自配保证，必要pairing机制可局部I。

Books：整合 `MULTIMODAL-REPRESENTATION` [实际正文](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) `286/288`；root独立必要source→fresh owner及真实两段/两侧POST通过。差额与最小两段见[唯一最终证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不是全recipe采用。

### [Racer: Role-Aligned Competence Estimation for Human-AI Routing](https://arxiv.org/html/2609.21953v1)

采用精确v1，必要范围：exact-v1完整摘要/§2.2–2.6/§3.1–3.9 Prop1–3/Th1–2完整主文证明、§4.1–4.7/T3–7/AppendF与G1必要目标/更新协议。纠正原医疗humanAI仅应用拒收，query+classrole正确率对象和coherentrelabelinvariant接口实际新增。Γ=P(M=Y|X,Y=y,C),q=sumηΓ依赖Y⊥C|X；BCE只conditionalgivenU，sufficiency另条件；routing softmax不是q。equal-role/query-near pooledcorrectness/sharedMLP,no absoluteclass embedding，support0fallbackglobal(.5empty)。Thregret0-1noadditionaldefercost非AURSBAC/budgetranking。jointtraining头梯度隔离≠sharedfeature/calibration不变；sparseB/K负收益、Path highBIFD ECE更低但utility弱，CIFAR nominalOOD保持populationlaw非真shift，pairedcellsdependent/descriptive；realgroundtruth二readeragreementmaskeddisagreement非clinicaltruth，CheXpertselectedexperts calibration不同人口。noinference significance/codewillrelease/HWprecisionSLO ND。

Books：整合 `PLATFORM-EVALUATION-SYSTEM` [实际正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) `260/262`；root独立必要source→fresh owner及真实两段/两侧POST通过。差额与最小两段见[唯一最终证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不是全recipe采用。

### [GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills](https://arxiv.org/html/2609.21749v1)

采用精确v1，必要范围：§2.1/3.1–3.2、§4(T1/T2)、§5.1–5.3(T3/T4)、B.2/B.3/Alg1 validator。peer独立necessary/fresh owner/literal PRE PASS，graph stripping保guidance/nodeinstructions五任务均退、mutation/crossover matchedbudget3repeats；validschemanotcommit/LiveMath退/ALFWorldcost更高/重生成无固定cap

Books：整合 `AGENT-WORKFLOW` [实际正文](../../../../books/part-07-agent/81-workflow.md) `1045/1047`；sep22_resume_v3独立必要source→fresh owner及真实两段/两侧POST通过。差额与最小两段见[唯一最终证据](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不是全recipe采用。

### [CogGym: Towards Large-Scale Comparative Evaluation of Human and Machine Cognition](https://arxiv.org/html/2609.21259v1)

采用精确v1，必要范围：exact-v1 fullabs、§2/3 sharedEML renderer/modelprompt/同trialIDs、§4 replication/limitations、E.1–E.2关键counter/F必要。原无internalmechanism关闭错误；Gemini10-run sampling vs verbalized同spec提供分布对象反证，Gemma5→50固定prompt/temp/trials只稳定mean。15replication521study participations非521uniquepeople；reference172exports/179eligible差异不合ceiling。actualCh66该标题两段确覆盖窄命题，整CogGym schema/模型taxonomy/内部认知非E。peer必要source→actual PASS，无运行/代码复现。

Books：已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [实际正文](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) `能描述分布，不等于逐次调用会从该分布采样`；sep22_resume_v3独立必要source→fresh owner窄命题通过。仅承载两种分布对象/均值与variability分账，整benchmark配方不称已有覆盖。

## 5. 缺口与下一步

本窗可执行扫描、筛选、必要审阅、Books与独立复核普通待办0；最终142已冻结，非作者日级Gate通过。下列外部材料/中心争议是本窗终态保留项，不用于正面证据、Books或无遗漏断言；每项保留精确定点重开条件，不因现状缺失反复扩大入口。

- **历史Mon21 Replacement批次**：十二类New/Cross与已具名事件已处理，但当前recent页不能还原本窗Replacement完整历史清单；现有原始入口/日期恢复记录未取得该批次，不宣称‘没有重要修订’。只有官方历史mailing/公告archive给出该批次精确ID、版本、公开时刻或明确等价原始记录时，定点恢复相应事件/依赖，不重扫全月。
- **[2609.12748v2](https://arxiv.org/abs/2609.12748v2)公开日期**：Submitted/updated字段不能证明Replacement首次公开落窗，缺的是本窗官方公告身份/版本/公开时刻。其撤回旧因果解释不是整篇withdrawn，也不作为本日确定候选或正面证据；需要官方历史批次、mailing或该版本明确公开依据，届时仅重开受影响判断与已有依赖，不以提交时刻回填。
- **已删[MiMo provider-prompt family](https://github.com/XiaomiMiMo/MiMo-Code/commit/8a0b4398ba1dcc629a5c40159c863aa4ead1bfbd)**：71d0cba/0fa4888/8a0b439当前官方main历史与URL/Git对象不能解析，404/`not our ref`原始结果保留。该版本从候选、评分、Evidence/Books采用链排除，只有官方重新发布可解析SHA/release及对应diff/tests后局部重开；不删除其他三个有效MiMo家族。
- **目录/证据权限**：Google Research动态目录只覆盖实际可见卡片/窗口定点查询，不能复算整个历史增量；需要可恢复的官方历史目录才扩相应时段。Qwen-Image-2.1博客只给日级日期，窗内时刻来自官方仓库artifact Atom，不把它当博客首发精确时刻；RecreationWorld作者报告/artifact非独立复现。上述限制不支持全网零遗漏或未披露性能结论。
- **[SURE20846v1](https://arxiv.org/html/2609.20846v1)中心争议**：§6.1 Eq2–3正α效率项与e=(n−k)/n，固定k对n导数正、固定n对k导数负，与‘减n/增k、奖励立即停止’解释方向冲突；不自行补1−e。Table1局部经验保留，需官方勘误或原始说明统一reward/优化解释，方可局部重开中心机制；不采用为E/Books。
- **[CaLR20981v1](https://arxiv.org/html/2609.20981v1)中心争议**：Eq4的非允许penalty mask在AppC Eq14被当更新selector，与Eq15仅允许边更新相反；strict-flow/circuit-memory/O(w)桥接保证不正面采用。需官方精确修正或明确实现+证明如何统一mask、target/latent角色和比较协议后定点重开；局部teacher schema与实验不被删去，也不自行改1−P。

各候选段中的局部未证明结论/非采用公式已明确收窄，不是被隐藏的全recipe待办；不以‘完整全文/代码复现’作为额外配额。当前无新增窗外任务，不恢复其他日期或Weekly。

## 6. 复核

复核者：sep22_resume_v3（最终非作者日级Gate，2026-10-01T13:42:53+08:00）；root及sep22_resume_v3的单篇独立必要source→fresh owner/PRE与实际写后有效复用。日级复核者未参与本报告或Books作者写入。

结论：通过

最终日级复核实际读取六部分、唯一packet最终142、14来源有限停止/日期与具名风险隔离、恢复checkpoint当前头；逐family核§3/§4均142且无漏/多，112I目标身份存在，争议与删除版本无正面Books采用链，普通可执行0。未变分批PRE/POST合法复用，不把有限覆盖、抽样或机械通过外推为475全审、全排除验证或全网无遗漏。

全部142拟入选项的必要证据/Books决定已分批独立复核，未变身份、exact-v1、采用命题与反证复用；112实际I各有正文与两侧写后核，26E只核具体已承载命题，2Only保原新增为何不改长期书，2D确认精确争议隔离、不授正面证据。完整分批PRE/POST范围见[唯一证据最终142与此前有效分批记录](../_sources/daily-20260921/arxiv-evidence-restoration.md#2026-10-01-最终142冻结快照待非作者日级gate)，不重复无差别附件/运行核验。最后八：root核21827、21983、21996、21629、21953必要primary/fresh owner及实际正文/双侧；sep22_resume_v3核21858、21749必要primary/fresh owner与真实两段/双侧，以及21259窄E source→actual。各actual唯一SF/exactlink、旧机制/反证/fallback与衔接均保留，窄锁已释放。

纠错实质与解决：DRT不能用judge caveat关闭typed压缩差额；Weight不能用局部operating point漏working-set fit反转；Voice-Light的3500/750是checkpoint step而非样本数；GRU移动entry rank为4不是3。21629共同patch必须自配的原文断言已用平方成本反例隔离，未删局部assignment机制；最后4误关21953/21629/21749/21259均按具体贡献重开并补足审阅/Books，不因医疗、科学、小模型、benchmark或成熟模块借用直接关闭。

来源/准入边界：14每日来源的实际入口/停止范围由机构原始记录、十二类官方Mon21目标组及本日题摘/恢复记录支撑；475宽库存只是有界查漏，不是全文队列。首批root题摘校准/后续第五组41+2条具体增量校准及风险具名事件沿未变证据复用；删MiMo SHA、SURE/CaLR中心冲突、12748v2日期与历史Replacement范围仅终态隔离，不抹目录缺口。

最后分层negative样本6：角色/query估计21953、独立mask对应21629、图/search scope21749、认知描述/采样分布21259四误关具体纠正；21468成熟verified-loop领域使用、20873领域XOR certifying-case无新模型/执行机制两关闭独立通过。样本覆盖模型表示/attention、路由测量、Agent workflow及benchmark/领域组合理由；未把本6或此前具名抽核说成全部原排除全量再审。原明确范围/成熟组合关闭按[题摘具体理由](../_sources/daily-20260921/arxiv-title-abstract-screening.md)保留，未改理由者未扩大成全文/附件审阅；发现实际新反证才重开受影响项。

机器校验：最终V3通过；§3实际142=136唯一arXiv+6机构，审阅116/24/2、Books112/26/2/2与汇总一致，本地Markdown链接存在，最后七个新增实际I的source-family标记各唯一，限定`git diff --check`通过。机器检查仅作格式/一致性补充，不替代上述非作者语义Gate。作者未stage、commit或push，运行前dirty/staged与无关内容保留。
