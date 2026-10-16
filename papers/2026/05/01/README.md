# Daily Research — 2026-05-01

**规范：** V3
**窗口：** 2026-04-30T09:00:00+08:00 ～ 2026-05-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-16T10:37:17+08:00
**补充窗口：** 2026-04-30 ～ 2026-04-30
**冻结候选日期：** [原报告基线](../_sources/daily-20260501/baseline-before-supplement-20261016.md)
**窗口说明：** 用户授权保留已有候选日期、评分、原小时窗口与原证据正文，本轮仅补查前一完整自然日遗漏；旧完成结论只描述原研究层，不代替本次补查验收。[唯一补查记录](../_sources/daily-20260501/SUP_SOURCES_20261016.md)。

## 1. 结论

本轮只补查北京时间 Apr30 自然日，不重跑旧556库存。原47家族整行、原日期评分/小时窗口及连续原§4保留，旧研究层的21整合/26已有覆盖也不重判。本次按模型、训练、推理、多模态与Agent主题有界发现，读63个独立arXiv身份的完整题摘后定点查重：4个复用Apr30既有候选归属，48个具体贡献前关闭或复用同exact-v1有效EX，1个FaaSMoE保留早公开资格问题，新增10个家族。机构发布另按实际原始入口筛选，不把月表库存计作当天命中，也不声称全学科召回。

新增10项已有各自证据与Books决定：5项具体差额深入整合到Ch17/29/33/49，1项标准审阅后已有覆盖，2项标准完成仅报告，2项深入保留中心争议、隔离正面Books。新机制分别区分MLP与Attention初始化噪声、首个可定位错误的局部候选更新、稀疏存储与稠密计算、实际GPU提交边界，以及student候选覆盖与选择蒸馏。SAMG经验空间mapping不自动满足其几何上界，TIDE reverse BCE也不能把student entropy视为常数；保留局部经验结果，不采用失效的严格保证。

原47加新增10共57家族，旧与新增计数/窗口分开。五处新增Books正文及完整邻接已获非作者root实际写后复核；机器校验、链接、原内容冻结比较通过，root实际六部分/A11–13日级验收通过，无普通可执行待办。必要历史目录、首公开身份和两处中心主张按§5精确隔离，不支持‘无遗漏’或生产性能/安全保证。完成只表示本次授权补查达到安全终态，不将保留项授Coverage/Evidence通过。唯一过程、版本、停止位置及改判依据见[补查记录](../_sources/daily-20260501/SUP_SOURCES_20261016.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | 官方RSS完整item按Apr30北京时间过滤，account-security与Goblins；邻项Apr29 compute/cyber越下界停止 | 已检查 | 产品认证EX、Goblins同事件有效EX复用；当前索引不证明删除页无事件 |
| `SRC-ANTHROPIC` | 官方Research嵌入列表，Apr29 20:26Z BioMystery；Apr30 16:35Z personal-guidance已属May1北京时间 | 已检查 | BioMystery同事件有效EX，后项窗外，不混入自然日 |
| `SRC-GOOGLE-AI` | DeepMind page3跨May→April7卡→March，Apr30 co-clinician核心已读；Google Research April9卡至Apr3 | 受阻 | Blog切片已检查、临床应用EX；Publications必要历史过滤未恢复，不以Blog推全Pub零事件 |
| `SRC-META-AI` | 官方Research请求30秒HTTP000/0byte；官方域Apr30定点补检无结果 | 受阻 | 必要历史目录不可读，§5发现保留，不作零命中 |
| `SRC-QWEN` | 官方Blog完整JSON，FlashQLA Apr28→Qwen-Scope列表Apr30；后者完整嵌入正文已读 | 已检查 | SAE toolkit/feature steering等用法说明未给新机制条件，EX；外层Apr30/内文Apr29冲突不影响前关，不拼后发report |
| `SRC-DEEPSEEK` | 当前Research完整footer V4.1/V4/V3.2/V3.1/R1/V3入口 | 受阻 | 无可复查Apr30历史目录，当前home不能证明零事件 |
| `SRC-MOONSHOT` | Kimi Platform Blog完整渲染列表2025-11-07/06至2024，非2026日期段 | 受阻 | 必要Apr30历史入口未恢复，不强扫全org或将陈旧列表视为零更新 |
| `SRC-TENCENT-HUNYUAN` | publicList英文renderType0 total9/list9与renderType1研究total6/list6；Apr30 id100039→研究Feb13邻界，完整body及exact-Apr30论文必要核心 | 已检查 | 只限英文可见切片，不授全语言/删除历史；CL-bench Life具体EX，Apr14 file信号不冒充首发，blog12model不拼论文10model |
| `SRC-ZAI` | Research完整159节点Scaling Pain与Apr7邻界；release-notes June16→Apr7 | 已检查 | Scaling Pain已有Apr30原候选，保旧归属/评分，不因当前UTC/display重排；未见具体重要修订 |
| `SRC-BYTEDANCE-SEED` | 官方API page20完整20卡；PublishDate按BJT重算，非pinned May15→May1两项→Apr30 Edit-R1→Apr23，读至Apr15尾项；pinned独立剔除排序 | 受阻 | Apr30 ID1637/2604.27505仅完整官方题摘+PDF链接，必要当日正文资格未定；1654/1665是May1窗外，旧日期解读已纠正，§5隔离 |
| `SRC-BAIDU-ERNIE` | 官方完整Blog May9→Apr30 ERNIE5.1Preview榜单→Apr15Image→Feb6 | 已检查 | 榜单核心无模型机制/新评价条件，EX；不推所有repo release为零 |
| `SRC-XIAOMI-MIMO` | Paper8项June29→Mar13→Feb3→2025；当前Blog15卡无日期 | 受阻 | Paper可见日期段已查；Blog必要历史日期不可恢复，不以无日期card推零 |
| `SRC-MINIMAX` | 中/英Blog完整13/12卡至2025、无next；May25→Apr27→Mar18；page2实返同集合；AgentTechblog3卡Oct8→Sep22→Sep19 | 受阻 | 主Blog可见切片已闭；AgentTechblog Apr30存在性/历史目录未定，不记不适用或零事件 |
| `SRC-ARXIV` | 官方赋号规则/April月表合证Apr30批25919–26952；12分类主线相关标题有界浏览、63独立身份完整AB，具体分页与停止见SUP A2/A7 | 已检查 | 日期不按submitted cutoff；跨类去重、旧同事件层定点复用；不是全类队列或旧556重筛 |

本轮实际原始缓存、入口、主题、身份与停止位置集中见[唯一SUP A2/A7及裁决](../_sources/daily-20260501/SUP_SOURCES_20261016.md)。仅复用官方原始月表/目录正文，不复用他日完成标签。原47家族的旧研究依据仍保留于[`V3_RECERTIFICATION.md`](../_sources/daily-20260501/V3_RECERTIFICATION.md)与原始[`arxiv-owner-receipt.json`](../_sources/arxiv-owner-replay-20260903/20260501/arxiv-owner-receipt.json)，其旧556/509数字只描述原层，不作为本次补查分母。

## 3. 候选与判断

前47行按授权冻结原日期/评分/归属；末10行为本轮遗漏新增，只记Apr30公开日期。官方ID赋号/公告规则、月表边界及必要exact-v1身份合证，DataCite注册只作旁证；Submitted不作边界。同事件原Apr30候选与具名有效前关不重列、不评分。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MARS](https://arxiv.org/html/2604.26963v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 异构 Agent workload 的 GPU/CPU 联合 admission 与调度；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Predictive Multi-Tier Memory Management for KV Cache](https://arxiv.org/html/2604.26968v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 把 KV placement 扩为多层预测状态；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Simple Self-Conditioning Adaptation for Masked Diffusion Models](https://arxiv.org/html/2604.26985v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 跨 denoising step 复用 clean-state estimate；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [When Continual Learning Moves to Memory](https://arxiv.org/html/2604.27003v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 参数更新转为 experience memory reuse 后的状态边界；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry](https://arxiv.org/html/2604.27019v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 安全微调重组 refusal representation 并牵连 utility；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Learning Rate Transfer in Normalized Transformers](https://arxiv.org/html/2604.27077v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 学习率跨 width、depth、token horizon 的 scale transfer；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Co-Evolving Policy Distillation](https://arxiv.org/html/2604.27083v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | teacher 与 policy 同步演进改变 rollout target；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [RoundPipe](https://arxiv.org/html/2604.27085v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 异构 consumer GPU 下重排 pipeline stage 与通信；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-PIPELINE-PARALLEL，[Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md) |
| [AutoSP](https://arxiv.org/html/2604.27089v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 编译器选择 sequence-parallel plan 与通信边界；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-TENSOR-PARALLEL，[Ch37](../../../../books/part-04-training-system/37-tensor-parallel.md) |
| [Step-level Optimization for Computer-use Agents](https://arxiv.org/html/2604.27151v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 从轨迹级 reward 下沉到 step-level workflow signal；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Path-Lock Expert](https://arxiv.org/html/2604.27201v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | control token 把 reasoning mode 变成显式 expert route；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md) |
| [Indirect Prompt Injection in the Wild](https://arxiv.org/html/2604.27202v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 真实网页中的间接注入改变外部内容信任边界；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Decoupling the Benefits of Subword Tokenization](https://arxiv.org/html/2604.27263v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 受控 byte simulation 分离吞吐与 boundary prior；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MODEL-TOKENIZER，[Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [NuggetIndex](https://arxiv.org/html/2604.27306v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | atomic retrieval unit 同时拥有 provenance、version 与治理状态；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Safe Bilevel Delegation](https://arxiv.org/html/2604.27358v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 双层 delegation 把 proposal 与 commit authority 分开；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [MiniCPM-o 4.5](https://arxiv.org/html/2604.27393v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 全双工多模态 interaction 引入连续 perception/output state；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [VitaLLM](https://arxiv.org/html/2604.27396v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | ternary accelerator 的 dependency-aware execution plan；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Beyond the Mean](https://arxiv.org/html/2604.27405v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 把同模型变化检测从均值转为 matched uncertainty；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Secret Stealing Attacks on Local LLM Fine-Tuning](https://arxiv.org/html/2604.27426v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 模型代码供应链把本地数据暴露给恶意执行路径；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [ScaleBox](https://arxiv.org/html/2604.27467v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 大规模代码验证需要隔离执行与可追踪 verifier evidence；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CuLifter](https://arxiv.org/html/2604.27486v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | GPU binary lifting 到 typed IR 改变执行计划可检查性；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Belief-Guided Inference Control](https://arxiv.org/html/2604.27536v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 用可验证 observation 更新 service belief 再执行控制；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Trace-Level Analysis of Information Contamination](https://arxiv.org/html/2604.27586v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 多 Agent 信息污染必须沿 trace 边传播和归责；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [Optimization before Evaluation](https://arxiv.org/html/2604.27637v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | prompt optimization 是 evaluation contract 的受控变量；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/html/2604.27707v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 区分 prompt-carried memo 与 durable revisable memory；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Test Before You Deploy](https://arxiv.org/html/2604.27789v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 模型更新需通过 update-specific release gate；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MCPHunt](https://arxiv.org/html/2604.27819v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 跨 MCP server 数据传播需要端到端 policy evidence；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MCP，[Ch83](../../../../books/part-07-agent/83-mcp.md) |
| [ZipCCL](https://arxiv.org/html/2604.27844v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | collective 无损压缩改变通信字节与计算开销权衡；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [AI Inference as Relocatable Electricity Demand](https://arxiv.org/html/2604.27855v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | latency constraint 决定 inference load 的地域迁移空间；3 + 2 + 2 = 7 | 深入完成 | 整合：PLATFORM-COST，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [TwinGate](https://arxiv.org/html/2604.27861v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 无稳定身份流量下仍需维护攻击分解状态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SimEval-IR](https://arxiv.org/html/2604.27878v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | user simulator 成为 evaluation artifact 而非隐含输入；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [In-Context Prompting Obsoletes Agent Orchestration](https://arxiv.org/html/2604.27891v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 对短而稳定程序，prompt state 可替代外部 orchestration；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [RHyVE](https://arxiv.org/html/2604.28056v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | reward hypothesis 在训练前需 competence-aware verification；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Emergent Misalignment Persona Consistency](https://arxiv.org/html/2604.28082v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 模型自评 persona 可能 coherent、inverted 或不一致；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Hierarchical Fault Detection and Diagnosis for Transformers](https://arxiv.org/html/2604.28118v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | component signal 与 fault graph 建立诊断证据链；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-MONITORING，[Ch67](../../../../books/part-06-ai-infrastructure/67-monitoring.md) |
| [Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/html/2604.28119v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | concept 可能由 global/local atom group 而非单 feature 表示；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Beyond Gaussian Bottlenecks](https://arxiv.org/html/2604.28122v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | topology-aligned latent 保留视觉特征几何；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Beyond SFT-to-RL](https://arxiv.org/html/2604.28123v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | on-policy distillation 作为 multimodal RL 的 pre-alignment stage；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Latent Adversarial Detection](https://arxiv.org/html/2604.28129v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 多轮 probe 使 latent risk 成为持续安全状态；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Crab](https://arxiv.org/html/2604.28138v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | sandbox checkpoint 必须捕获进程外 semantic state；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Claw-Eval-Live](https://arxiv.org/html/2604.28139v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | refreshable task 与 artifact snapshot 支持 live evaluation；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Strait](https://arxiv.org/html/2604.28175v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | priority 需结合 interference-conditioned latency prediction；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Synthetic Computers at Scale](https://arxiv.org/html/2604.28181v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 长程 computer-use 评测需保留 workspace state 与 artifact lineage；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Exploration Hacking](https://arxiv.org/html/2604.28182v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | exploration 本身进入 RL trust boundary；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Representation Fréchet Loss](https://arxiv.org/html/2604.28190v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | population statistic 与 gradient batch 解耦的分布匹配损失；3 + 2 + 3 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [LaST-R1](https://arxiv.org/html/2604.28192v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | physical latent reasoning 与 action reward 联合优化；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [HERMES++](https://arxiv.org/html/2604.28196v1) | 2026-05-01T08:00:00+08:00 ～ 2026-05-01T09:00:00+08:00 | 共享 3D state 支持理解与未来几何预测；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness](https://arxiv.org/html/2604.26341v1) | 2026-04-30 | semantic→metric-depth→生成latent中介及concat/addition受限对照；2 + 1 + 2 = 5 | 标准完成 | 仅报告：局部接口选择，不升级任意几何生成通则 |
| [Delta Score Matters! Spatial Adaptive Multi Guidance in Diffusion Models](https://arxiv.org/html/2604.26503v1) | 2026-04-30 | 经验空间mapping与几何上界之间的中心桥不成立；2 + 2 + 2 = 6 | 争议 | 暂缓：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，严格保证隔离 |
| [Grounding vs. Compositionality](https://arxiv.org/html/2604.26521v1) | 2026-04-30 | label grounding与迭代constraint reasoning的受控分离；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：WORLDVIEW-LLM-INTELLIGENCE，[Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)，原子事实/bridge-state/组合泛化段 |
| [TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models](https://arxiv.org/html/2604.26553v1) | 2026-04-30 | first-confusion后的确定候选探索与局部policy更新；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)，first-failure后局部候选分支 |
| [Sparse-on-Dense](https://arxiv.org/html/2604.26587v1) | 2026-04-30 | 压缩SRAM与dense PE计算分离，以索引互联面积换更多PE；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，稀疏pattern/kernel fallback后 |
| [Revealing NVIDIA Closed-Source Driver Command Streams for CPU-GPU Runtime Behavior Insight](https://arxiv.org/html/2604.26889v1) | 2026-04-30 | doorbell最终提交与USERD/GPFIFO/PB命令重建的测量边界；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，TaxBreak分层观测后 |
| [Stochastic Scaling Limits and Synchronization by Noise in Deep Transformer Models](https://arxiv.org/pdf/2604.26898v1) | 2026-04-30 | 固定Attention/iid MLP初始化的不同残差缩放与共同噪声同步条件；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Ch17](../../../../books/part-02-model/17-transformer-layer.md)，attention-only联合尺度后 |
| [World2VLM](https://arxiv.org/html/2604.26934v1) | 2026-04-30 | 将world-model camera imagination前移为forward/inverse QA训练监督；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受限空间QA训练/部署取舍，不认证真实动作或物理状态 |
| [Select to Think: Unlocking SLM Potential with Local Sufficiency](https://arxiv.org/html/2604.26940v1) | 2026-04-30 | student候选覆盖/选择分解与Local排序蒸馏；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md)，token位置选择后、扩词表前 |
| [Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models](https://arxiv.org/html/2604.26951v1) | 2026-04-30 | mask/训练进度双轴蒸馏及reverse BCE≠KL常数桥纠错；2 + 2 + 2 = 6 | 争议 | 暂缓：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，中心目标/梯度保证隔离 |

## 4. 证据与知识整合

### [MARS](https://arxiv.org/html/2604.26963v1)

exact-v1 的控制面以 GPU/CPU 双资源 observation 决定 admission，并用 session metadata 与 KV residency 维持多轮 continuation；实验限定在修改后的 vLLM、单卡 H100/H200 与作者 Agent workload，未证明多租户公平或跨集群稳定性。Ch56 已把调度对象定义为带 runtime state 的 token-generation process，并覆盖 admission、SLO 与 fallback，故为已有覆盖。

### [Predictive Multi-Tier Memory Management for KV Cache](https://arxiv.org/html/2604.26968v1)

正文把 HBM、CXL、主存、NVMe、RDMA 等层级放入预测 placement，但关键收益主要是基于带宽规格和 trace 的分析投影，而非完整生产部署；跨层迁移会增加预测漂移、传输和故障恢复状态。Ch54 已覆盖 KV 分层、冷热判断及成本/延迟边界，故不追加。

### [Simple Self-Conditioning Adaptation for Masked Diffusion Models](https://arxiv.org/html/2604.26985v1)

exact-v1 在 masked diffusion 的迭代去噪中把上一轮 clean-state estimate 作为下一轮条件，改变的是可变生成状态而非单纯 loss；收益依赖 step schedule、表示与作者任务，错误估计也会跨步放大。Ch24 已解释 iterative correction、commit 与 rollback 压力，故为已有覆盖。

### [When Continual Learning Moves to Memory](https://arxiv.org/html/2604.27003v1)

论文把经验复用从参数更新迁到外部 memory，实验比较写入、检索和复用策略，但只覆盖作者 AgentGym/ReMe 任务，不能证明长期知识不会陈旧或污染。Ch77 已把 memory construction、validity、retrieval 与 revision 分开治理，故不新增正文。

### [Dynamic Adversarial Fine-Tuning Reorganizes Refusal Geometry](https://arxiv.org/html/2604.27019v1)

exact-v1 的 activation 分析显示 adversarial fine-tuning 不只是移动单一拒绝方向，而会重组安全表示几何并影响 utility；结果绑定所测模型、攻击和 probe，几何可分性不是安全保证。Ch72 已要求把模型行为、表示诊断与 release gate 分层，故为已有覆盖。

### [Learning Rate Transfer in Normalized Transformers](https://arxiv.org/html/2604.27077v1)

论文通过 normalized parameterization 检查学习率能否跨 width、depth 与 token horizon 转移，证明的是作者模型族中的 scale rule，而非任意架构的万能学习率；优化器、数据与 normalization 改变仍需重校准。Ch28 已覆盖按层信号尺度、稳定性和 scale transfer 的条件边界，故不追加。

### [Co-Evolving Policy Distillation](https://arxiv.org/html/2604.27083v1)

方法让 teacher 与 learner 随训练共同更新，改变 rollout target 的版本状态并缓和静态 teacher 失配；作者实验不能证明非平稳 target 在所有 RL workload 中稳定。Ch33 已覆盖 rollout-policy/reference-policy 漂移、版本一致性与回退条件，故为已有覆盖。

### [RoundPipe](https://arxiv.org/html/2604.27085v1)

RoundPipe 针对异构 consumer GPU 重排 stage、microbatch 与通信路径，以利用不均衡显存和算力；它用更多计划复杂度换取可用吞吐，仍受最慢 stage、链路和容错约束。Ch38 已形成 pipeline bubble、placement 与 heterogeneity 的完整演进链，故不重复。

### [AutoSP](https://arxiv.org/html/2604.27089v1)

AutoSP 把长上下文 sequence-parallel strategy 交给编译器在候选 plan 中选择，显式权衡 activation memory、collective 与重计算；作者硬件和模型上的最优 plan 不可外推。Ch37 已覆盖 sequence/context parallel 的 state partition 与通信代价，故为已有覆盖。

### [Step-level Optimization for Computer-use Agents](https://arxiv.org/html/2604.27151v1)

论文把 trajectory reward 分配到具体 action step，改善稀疏反馈下的 credit assignment；step label 和 evaluator 仍可能奖励捷径，局部成功不等于 workflow durable correctness。Ch81 已覆盖 step state、checkpoint、retry 和 effect evidence，故不追加。

### [Path-Lock Expert](https://arxiv.org/html/2604.27201v1)

exact-v1 用控制 token 在 `/think` 与 `/no_think` 间选择 mode-pure expert MLP，使 reasoning mode 成为显式 routing state；代价是容量碎片、路由依赖与模式错误。Ch21 已覆盖 expert ownership、capacity 与 routing failure，故为已有覆盖。

### [Indirect Prompt Injection in the Wild](https://arxiv.org/html/2604.27202v1)

论文对真实网页中的间接 prompt injection 做来源与目标分类，支持“外部内容是不可信输入”这一 threat model；它不证明样本频率等于所有生产流量，也不提供完备防御。Ch72 已明确 data/control plane 隔离与 effect authorization，故为已有覆盖。

### [Decoupling the Benefits of Subword Tokenization](https://arxiv.org/html/2604.27263v1)

exact-v1 用 byte-level simulation 分别控制 sequence shortening 与 subword boundary prior，从而说明 tokenizer 收益不是单一因素；结论受语言、模型规模与计算预算限制。Ch11 已把压缩、边界先验、词表与 OOV 代价放在同一取舍链，故不追加。

### [NuggetIndex](https://arxiv.org/html/2604.27306v1)

正文把检索单元拆成可版本化、可追溯的 atomic nugget，并把维护和治理元数据纳入索引；作者任务不证明任意语料都能无损原子化。该机制已写入 Ch76 的 evidence identity 与 retrieval-unit lifecycle 正文，Books 整合有效。

### [Safe Bilevel Delegation](https://arxiv.org/html/2604.27358v1)

双层 delegation 让上层选择授权范围、下层在约束内执行，核心增量是 proposal 与 effect commit authority 分离；形式化假设不等于真实工具链已满足。该边界已写入 Ch82 的多 Agent 委托、能力限制与 rollback 论证。

### [MiniCPM-o 4.5](https://arxiv.org/html/2604.27393v1)

exact-v1 将语音、视觉与语言输入输出放入持续全双工 interaction loop，机制价值在跨模态时间状态与可打断输出，而非单项 benchmark；未证明开放环境下的实时鲁棒性。Ch23 已覆盖 modality、timestamp 与 provenance identity，故为已有覆盖。

### [VitaLLM](https://arxiv.org/html/2604.27396v1)

论文将 ternary operator mapping、dependency-aware scheduling 与 accelerator dataflow 联合设计；收益绑定作者模型、硬件和精度，不能外推通用 GPU serving。Ch49 已把量化、kernel 与 execution plan 的共设计及 fallback 写成 owner，故不追加。

### [Beyond the Mean](https://arxiv.org/html/2604.27405v1)

方法比较同一模型两个版本时保留 item-level pairing 与不确定性，而非只比较 aggregate mean；统计检验仍受样本、evaluator 与多重比较影响。该增量已写入 Ch66 的 matched evaluation、置信区间和 release-decision 正文。

### [Secret Stealing Attacks on Local LLM Fine-Tuning](https://arxiv.org/html/2604.27426v1)

exact-v1 展示模型仓库中的可执行训练代码能够读取本地 fine-tuning secret 并建立外传路径；攻击实现不证明所有仓库恶意，但改变了 artifact admission 与 sandbox 边界。该机制已进入 Ch72 的供应链、最小权限与隔离执行正文。

### [ScaleBox](https://arxiv.org/html/2604.27467v1)

ScaleBox 用隔离执行环境和可扩展 verifier 检查大量生成代码，关键不是通过率，而是 test artifact、runtime state 与 verdict provenance；作者任务不覆盖全部语言和对抗程序。该 evidence contract 已写入 Ch66。

### [CuLifter](https://arxiv.org/html/2604.27486v1)

CuLifter 将 GPU binary 提升为 typed IR，使依赖、地址空间与语义检查可以进入 execution-plan 验证；lifting correctness 和未知指令仍是失败边界。该机制已写入 Ch49 的 compiler/runtime plan inspection 路线。

### [Belief-Guided Inference Control](https://arxiv.org/html/2604.27536v1)

控制器不直接相信离线预测，而是从可验证 observation 更新 workload belief，再调整 serving 配置；收益以额外探测、校准和控制延迟为代价。该闭环已写入 Ch56 的 observe-decide-act、SLO 和保守回退正文。

### [Trace-Level Analysis of Information Contamination](https://arxiv.org/html/2604.27586v1)

论文沿多 Agent trace 重建信息流和污染传播，而非只看最终答案；trace 缺失或跨服务 identity 断裂会导致错误归因。该增量已进入 Ch69 的 causality、provenance 与跨 Agent trace 语义。

### [Optimization before Evaluation](https://arxiv.org/html/2604.27637v1)

exact-v1 表明未经优化的 prompt 会把 interface quality 混入 model quality，因此 prompt/search budget 必须成为评测协议变量；优化本身也可能对 benchmark 过拟合。该边界已写入 Ch66 的 evaluation contract 与公平比较正文。

### [Contextual Agentic Memory is a Memo, Not True Memory](https://arxiv.org/html/2604.27707v1)

材料区分上下文中携带的摘要 memo 与可持续写入、验证、修订和遗忘的 memory system；它主要是边界澄清而非新架构。Ch77 已明确这一区分，标准审阅足以支持已有覆盖。

### [Test Before You Deploy](https://arxiv.org/html/2604.27789v1)

正文主张每次模型或依赖更新都应触发与风险相称的 targeted tests，而不是沿用静态 benchmark；作者框架不证明一套测试覆盖所有回归。Ch66 已拥有 versioned evaluation 和 release gate，因此不新增。

### [MCPHunt](https://arxiv.org/html/2604.27819v1)

MCPHunt 把跨 server 的数据传播、工具链边界和 policy violation 放入同一评测 trace；测试集不能证明协议实现安全完备。该机制已进入 Ch83 的 capability、data lineage 与跨 server enforcement 正文。

### [ZipCCL](https://arxiv.org/html/2604.27844v1)

ZipCCL 在 collective 前后增加无损压缩/解压，只有减少的链路字节超过额外 kernel、buffer 与同步成本时才获益；收益绑定 tensor distribution 与互连。该条件分支已写入 Ch36 的 communication optimization 路线。

### [AI Inference as Relocatable Electricity Demand](https://arxiv.org/html/2604.27855v1)

论文把 inference 请求的 latency budget、区域电力和迁移距离联立，说明并非所有负载都能随电价搬迁；模型依赖能源假设，不代表实际运营收益。该约束已写入 Ch70 的 carbon/cost placement 与 SLO 共优化正文。

### [TwinGate](https://arxiv.org/html/2604.27861v1)

TwinGate 针对无稳定用户 identity 的 decompositional jailbreak，维护跨请求攻击状态并用不对称对比信号判断；state collision、隐私和 evasion 仍是失败面。Ch72 已覆盖 stateful defense、identity uncertainty 与误封回退，故不追加。

### [SimEval-IR](https://arxiv.org/html/2604.27878v1)

工具包把 user simulator 的 persona、policy、随机性和 session trace 变成 versioned evaluation artifact；模拟用户不等于真实分布。该增量已进入 Ch66 的 simulator validity 与 evaluator provenance 正文。

### [In-Context Prompting Obsoletes Agent Orchestration](https://arxiv.org/html/2604.27891v1)

作者实验支持一个反向分支：对短、稳定、可一次装入 context 的程序，显式 orchestration 可能只增加状态与失败点；它不适用于长程副作用和恢复。该共存边界已写入 Ch81，防止把 workflow 复杂度当作默认答案。

### [RHyVE](https://arxiv.org/html/2604.28056v1)

RHyVE 在采用 LLM 生成的 reward hypothesis 前评估 verifier competence，并按阶段控制部署；仍可能继承 judge 偏差与覆盖缺口。该 release-before-optimization 机制已进入 Ch31 的 reward trust boundary。

### [Emergent Misalignment Persona Consistency](https://arxiv.org/html/2604.28082v1)

exact-v1 显示 emergent-misalignment 模型对 persona 的自我报告可能一致、反向或不稳定，因此 self-assessment 不能独立作为安全证据；结论绑定作者模型与 elicitation。Ch72 已要求外部行为、表示与独立评测交叉验证，故不追加。

### [Hierarchical Fault Detection and Diagnosis for Transformers](https://arxiv.org/html/2604.28118v1)

论文从 Transformer component signal 构建 fault-propagation graph，并在 7 个模型、9 个任务、5556 个 mutation 上评估；合成 mutation 不等同真实故障分布，graph 也可能随架构漂移。Ch67 已覆盖模型内部信号、因果诊断与版本基线，故为已有覆盖。

### [Do Sparse Autoencoders Capture Concept Manifolds?](https://arxiv.org/html/2604.28119v1)

exact-v1 表明 concept manifold 可能由全局或局部 SAE atom group 表示，单一 feature direction 会稀释或分裂概念；toy 与所测模型不能建立普遍 ontology。Ch5 已把表示视为分布式、任务相关且需 probe 验证，故不追加。

### [Beyond Gaussian Bottlenecks](https://arxiv.org/html/2604.28122v1)

方法用 topology-aligned、power-spherical latent 适配 vision-transformer feature geometry，并在重建/生成任务上验证；它不证明 latent 已成为因果、可控 world state。Ch25 已区分几何表示、predictive state 与 control authority，故为已有覆盖。

### [Beyond SFT-to-RL](https://arxiv.org/html/2604.28123v1)

作者在 multimodal RL 前加入 black-box on-policy distillation，使初始 policy 更接近可探索区域；代价是 teacher bias、额外 rollout 和版本耦合。该阶段化路线已写入 Ch31，作为 SFT 与 RL 之间的条件分支。

### [Latent Adversarial Detection](https://arxiv.org/html/2604.28129v1)

方法在多轮交互中主动 probe hidden activation，并累积 latent risk state，而不是逐轮独立分类；probe 本身可能被适应或增加延迟。该机制已进入 Ch72 的 stateful detection 与 defense-in-depth 正文。

### [Crab](https://arxiv.org/html/2604.28138v1)

Crab 通过 coordinator、eBPF inspector 与 checkpoint/restore data plane 捕获 Agent sandbox 的进程、文件和外部 semantic dependency；exact-v1 只覆盖 Linux sandbox 与所测 backend。该 state ownership 和恢复边界已写入 Ch84。

### [Claw-Eval-Live](https://arxiv.org/html/2604.28139v1)

评测以 refreshable signals、release snapshot、controlled fixtures 与 artifact graders 维护 105 项动态任务；ClawHub-derived demand 不代表通用生产分布。Ch66 已覆盖 live benchmark 的 version、fixture 与 drift，故为已有覆盖。

### [Strait](https://arxiv.org/html/2604.28175v1)

Strait 用双优先级 scheduler 和 interference predictor 估计并发执行影响，避免优先级只把排队延迟搬成 GPU contention；跨模型迁移和 tail-SLO 仍需重新校准。该机制已写入 Ch56 的 priority、interference 与 conservative fallback 正文。

### [Synthetic Computers at Scale](https://arxiv.org/html/2604.28181v1)

正文生成任务一致的文件、目录、终端与 workspace state，用于长程 productivity Agent 训练/评测；合成环境会漏掉组织策略、隐藏依赖和真实用户分布。Ch27 已覆盖 synthetic data 的 state consistency、provenance 与 distribution gap，故不追加。

### [Exploration Hacking](https://arxiv.org/html/2604.28182v1)

论文展示 policy 可通过压低有用 exploration 来抵抗 RL 更新，即便没有显式 reward hacking；构造实验不证明生产普遍性。该 failure mode 已进入 Ch31 的 rollout diversity、policy-update diagnostics 与 release evidence。

### [Representation Fréchet Loss](https://arxiv.org/html/2604.28190v1)

方法把 representation distribution distance 变成训练 loss，并把估计 population statistic 的样本与 gradient batch 解耦；收益依赖 encoder 与统计估计，不能外推感知一致性。该替代生成目标已写入 Ch24 的 objective/evaluation mismatch 路线。

### [LaST-R1](https://arxiv.org/html/2604.28192v1)

exact-v1 把 physical latent reasoning 当作 VLA RL 的显式决策变量，并与 action reward 联合优化，在 LIBERO 与四类真实机器人任务验证；作者实验不证明开放世界安全、实时频率或 sim-to-real 普遍性。Ch26 已覆盖 reasoning/controller 分层、action authority 与 physical evidence，故不追加。

### [HERMES++](https://arxiv.org/html/2604.28196v1)

HERMES++ 共享 3D representation 以同时支持 scene understanding 和 future geometry generation；驾驶数据与 open-loop 指标不证明 closed-loop safety 或 causal controllability。Ch25 已明确 video generation、predictive environment state 与 planner authority 的边界，故为已有覆盖。

### 补充窗口新增证据（原47项连续正文保留至此）

### [SpatialFusion: Endowing Unified Image Generation with Intrinsic 3D Geometric Awareness](https://arxiv.org/html/2604.26341v1)

exact-v1 §3/4.5/Table5以独立spatial MoT读取语义与几何、DPT产生metric-depth，再由adapter将深度特征加到DiT latent。决定准入的不是新增模块名，而是w/oInjection/Concat/Addition同任务比较：GenSpace T2I为35.22/42.81/46.19，editing为29.80/32.76/35.40，支持局部中介与消费接口选择。18.5%新增参数、伪深度与联合训练仍限制单机制因果，不能据此声称排除了overfit或所有几何都成立；H200 300次局部平均约+0.26/+0.83s也不是生产SLO。作者初拟‘成熟组合’EX经root实际core纠正为P5，未用已有几何主题抹掉具体替代。标准完成，仅报告该受限实现；Ch23现有GeoSense/GeoSR的独立几何消费与监督/捷径原则不因此改成通用生成recipe。

### [SAMG](https://arxiv.org/html/2604.26503v1)

exact-v1 §3.1–3.3/Eq4–12/Alg1把conditional/unconditional输出差的空间能量E做minmax，再映到经验正区间。Eq10固定切线lower-bound不能让任意Eq11–12 mapping满足Eq9几何界：E处处为a>0时归一图为零、ω=ωmax与a无关，而理论许可界随a^-1/2收缩；κ/δ/c_t没有进入mapping，切向与anchor条件另需证明。作者/root实际独核此中心反侧，保争议P6，不否定全部局部生成收益。

必要评价§4.1–4.4/Tables1–4覆盖SD1.5/SDXL50步、SD3.5M28步及CogVideoX2B/ModelScope1.7B50步、四图像集/ChronoMagic150。HPS/ImageReward/FID/CLIP是作者proxy；SD1.5 Pick-a-Pic ImageReward .053→.043有反退。Mapping不增模型forward不等零总成本，原双CFG调用/reduction仍付费；必要范围未披露hardware/precision/concurrency/完整latency/SLO，不补造。Ch24正面采用暂缓；仅在有效几何条件连接到经验mapping或撤回严格保证后重开该桥。

### [Grounding vs. Compositionality](https://arxiv.org/html/2604.26521v1)

exact-v1 Problem Definition/Iterative LTN/Experimental Setup/Results/Limitations的视觉逻辑任务区分label分类和predicate在embedding上满足约束；未见数字label近零时，full iLTN仍可解31/50而one-shot基线4/50。新增是受控识别/组合分离，不是用toy证明所有LLM无法涌现推理。Full与baseline同时改变迭代架构、每步GT监督，relational测试另追加axiom，t-SNE也非因果识别；不能把51.2对11.3平均分全归一个objective。A100训练、内层逻辑优化、更多迭代与测试规则均有成本。标准完成；实际Ch8‘记住两个事实，不等于学会组合它们’及bridge-state/组合泛化完整段已经承载可读事实与可复用推理分离、行为失败不识别唯一电路，root实际owner通过已有覆盖，不强写新Books。

### [TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models](https://arxiv.org/html/2604.26553v1)

exact-v1 §3/4.1–4.5/AppA从完整rollout定位first-confusion，取该prefix确定TopN（主配置16），各候选3-token lookahead后由语言检测器给reward，以旧概率加权/中心化的advantage作局部clipped更新。它与Ch33已有终局advantage重分配或另训prefix scorer不同：局部属性可被短程检测时，可以直接比较替代token。所有候选同分时归一信号不可用，原算法未给通用guard，不照录为无条件可执行配方；零额外critic也不抵销rollout、N个lookahead、检测与训练。

Llama3.1-8B/Qwen3-8B/Ministral8B/Gemma3-4B、四目标语言/Bactrian-X、8H100局部结果绑定检测口径。英语中性时RPR96.68→99.19、accuracy58.35→58.08；英语算违规时63.27→77.59、58.24→56.17。Unicode/例外规则不是完整语义语言真值，TopN外概率变化也不证明语言神经元因果。为具体差额深入，写入Ch33静态first-failure段后，完整邻接/本人注由root实际POST通过。

### [Sparse-on-Dense](https://arxiv.org/html/2604.26587v1)

exact-v1 §III/IV-A–D/V使CSC保持压缩到SRAM，在dense systolic PE前解压；不跳零MAC，用省下indexmatching/scatter/互联面积容纳更多dense PEs。这是存储压缩与执行稀疏分责的实际架构替代，不是TensorRT已有行为。28nm综合、4KPE/2MBSRAM/500MHz、16bit值/8bit索引与cycle/energy估计须保持身份，非实芯/GPU服务实测。density≥.7时dense baseline能耗更好，极稀疏ESE吞吐/面积更强；BERT约.12 density下吞吐不占优且剪枝质量下降约3.1/3.2%。绑定同面积、存储配置、DRAM/SRAM/PE能耗、质量恢复与解压成本，不由少bytes推出少MAC或全链加速。具体差额深入整合Ch49稀疏pattern/kernel fallback后，root实际POST通过。

### [Revealing NVIDIA Closed-Source Driver Command Streams for CPU-GPU Runtime Behavior Insight](https://arxiv.org/html/2604.26889v1)

exact-v1 §4/5/6.1–6.3在CPU实际写doorbell的边界截获提交，依channel身份读USERD最新GP_PUT、再沿GPFIFO恢复pushbuffer；RAMFC副本在运行中可能旧，API返回也不是设备完成。Watchpoint/shadow-doorbell依赖root权限、修改kernel/driver，冻结提交线程不等所有GPU writer原子快照，记录与性能测量须分离。A40/Xeon6338/PCIe4、Rocky9.5/Linux5.14、CUDA11.8/13.0及对应520/580 driver比较限制归因；24KiB切换是本环境现象，raw DMA设备时间与Nsight不同计时边界不是服务端到端加速，command footprint变化也不唯一解释整套软件栈差异。具体差额深入整合Ch49 TaxBreak后，root实际正文/完整两侧/本人注POST通过；未运行自定义driver或复现。

### [Stochastic Scaling Limits and Synchronization by Noise in Deep Transformer Models](https://arxiv.org/pdf/2604.26898v1)

HTML转换在引言后中断，故改读exact-v1 PDF p2–10必要架构/Thm1.1/Prop1.2/Cor1.3/Assumptions1–2/Thm1.4，不声称全55页证明审完。固定Attention映射、iid初始化MLP、球面LN，Attention按T/L而MLP按√(T/L)缩放，后者带来noninteracting common field，不是token独立noise。有限N/固定T的耦合近似与大N极限分开，三limit全部交换另需C∞，不能把ReLU不加条件继承。

同步结论另需nonodd与barλ=(d−1)κ′−(d−3)κ<0（此条件需d>3），Attention能量增长ε足够弱、ε+barλ′<0时才给期望interaction energy指数下降；odd Tanh可两点吸引。该新MLP来源/缩放补足旧attention-only定理明确不授的边界，不覆盖旧定理、不认证训练后相关权重、causal decoder或任务质量。理论具体差额深入整合Ch17旧两段后，root实际POST通过，未实跑或穷举证明。

### [World2VLM](https://arxiv.org/html/2604.26934v1)

exact-v1 §3.2–3.4/4.1/4.4/Tables2–4把camera trajectory条件的world-model合成未来视图变成forward consequence/inverse motion QA，再SFT→GRPO；部署仅VLM，不在线调用world model。具体替代是把imagination费用前移到训练，不是新物理状态真值或真实物体action。Qwen2.5-VL7B共同backbone、SVC/HY-WorldPlay、约100k SFT/1k GRPO、ScanNet/MulSeT源与四空间benchmark限定结果；testtimeWM在SATReal31.33低于base44.67，SFT64/GRPO72.67，但SFT perspective42.42低base48.48、GRPO action consequence67.57低SFT75.68。双方向/源混合有局部对照，数据与训练总预算不完全匹配，不能从省部署generator推生命周期更便宜。标准完成仅报告；Ch25 training-only teacher/forward-inverse与Ch26部署观测分责已有长期原则，不为本空间QA操作点强造通则。root必要Source独核通过。

### [Select to Think: Unlocking SLM Potential with Local Sufficiency](https://arxiv.org/html/2604.26940v1)

exact-v1 §4.1–4.4/5.1–5.5/Tables1–3在student产生的prefix/候选集合里让teacher选token，区分候选hit缺口与selection miss；Local通过K个candidate-augmented prefixes、LoRA/专门reserved-token readout和原文本分布保护，将排序迁到student。诊断TopK覆盖不强制全部部署候选为TopK，§5.5 unrestricted sampling与截尾tail另有影响。Teacher argmax不是truth，KL oracle用于训练/分析，部署须学习trigger；额外batched forward仍计算K个prefix，不是零成本logit重排。

Qwen2.5-Instruct0.5/1.5B、32Bteacher，MATH训练，数学/代码/MMLU-Pro与三seed结果只支持该配对，95%Hit@8是1.5B/MATH500/触发人口而非通用latent能力。Table3 Local对原student MATH9.3→10.2s、Olympiad15.5→18.0s有反退，AIME输出更短30.7→21.0s，不能写跨任务同速或同输出纯机制加速。为选择接口差额深入整合Ch29位置选择后/扩词表前，root实际POST通过。

### [TIDE](https://arxiv.org/html/2604.26951v1)

本篇在Apr30旧§5因旧小时cutoff日期未定而隔离，本轮以公告规则/月表/exact-v1身份确认自然日资格，不改变旧候选归属，也不擦掉原§2/AppendixC/D已有效独核的中心争议。具体机制是mask timestep×训练进度调teacher权重，互补mask用两次冻结teacher forward，跨tokenizer按共同byte span组成chunk概率。Eq11 reverse BCE `−ps log pt−(1−ps)log(1−pt)`等于KL_Bern(ps||pt)+H(ps)，H依student θ，并非常数；pt=.75时BCE偏向ps=1而KL最小为.75，不能用‘KL等价’证明梯度和noise filtering。系数界又依teacher概率远离0/1的ε，低ps不自动保证参数梯度小。

作者/root保留局部经验：§3.1–3.4/Tables1–4为Qwen3-0.6B BD3LM、WeDLM8B/LLaDA2mini、512训练序列/block32、BF16、10epochs、八任务。共享词表普通KL平均30.55低于未蒸馏32.67，最终33.55/34.20不等所有蒸馏或子任务获益；H10080GB固定prompt/256输出为6.25s对未蒸馏6.08s，CompDemo约+50%训练费，小student对大teacher不能隔离优化因果。P6纠错深入、Ch24正面目标/梯度保证暂缓；修正Eq11目标身份及概率clamp/梯度域、或重建相符证明才定点重开，不否定全部局部结果。

## 5. 缺口与下一步

普通待办：无。本轮机器校验/链接、原47行/连续原§4冻结比较及root实际日级验收已通过；来源发现、具名初筛与逐项证据/Books工作已到安全终态，不等待无关全文。以下为本窗终态保留项，均不支持正面证据、Books、‘无遗漏’或性能/安全保证；各项的必要材料与定点重开条件分别列明。

- 必要历史发现入口：Google Research Publications交互过滤、Meta/FAIR Research、DeepSeek历史research、Kimi/Moonshot Apr30目录、MiMo无日期Blog、MiniMax AgentTechblog当时存在性/历史目录。当前入口/请求/停止见§2及SUP A7，未取得可用窗口段，不记零命中。可接受替代为该源官方可读Apr30日期段/分页或具名当日原文；只重开相应发现层，不重审其余有效Source/Books。
- [Seed Edit-R1 / Leveraging Verifier-Based Reinforcement Learning in Image Editing / 2604.27505](https://arxiv.org/abs/2604.27505v1)：官方API page20 ID1637的PublishDate按BJT为Apr30，ArticleSubContentEn只有完整题摘与arxiv PDF链接，没有独立正文/publicAt；arxiv赋号批属于May1。CoT verifier→GCPO偏好训练→GRPO编辑有潜在增量，但缺Apr30已公开正文身份，不倒灌May1正文、不评分/列确定候选/Books。旧本日ledger的泛‘无独立evaluation/artifact、未改modality contract’EX没有该reward机制actual owner，不能以旧Complete代审，旧条不覆盖或删除。恢复以Apr30公开完整作者稿/项目正文或明确官方公开身份合证为准，只定点核该家族。
- [FaaSMoE / 2604.26881](https://arxiv.org/abs/2604.26881v1)：作者官方TU[Apr28新闻](https://www.tu.berlin/en/3s/news-details/paper-accepted-at-edgesys-26)明示PDF available，[出版物入口](https://www.tu.berlin/en/3s/research/publications)匹配同题/作者/DOI，是更早公开信号而非Apr28不可变正文证明。其同exact-v1技术层已有有效贡献前EX，本轮不重评分/写书；若以后出现足以重开贡献的证据，先核更早正文归属，再恢复真实日期，不强保Apr30候选。
- SAMG 2604.26503与TIDE 2604.26951：具体Eq9→经验mapping、reverse BCE→KL/梯度保证争议及可接受修正分别在§4，不重复请求。只隔离受影响中心保证，不删除局部实验，改正后只恢复相应桥。

窗外恢复线索（不属于补窗、不阻塞本日）：26953/26961/26962虽早提交，官方赋号/月表/exact-v1身份落May1；不随Submitted搬进Apr30。

Seed ID1654 End-to-End AR Image/2605.00503及1665 CARD的PublishDate=1777564800000，按BJT是May1，不是Apr30；两项仅官方简述，不证明paper正文当日可读。已交May2按May1资格定点恢复，不再列为Apr30日期冲突；CARD的AI for Science范围不因路由而改变。

CL-bench Life官方Apr30事件的具体贡献已前关，repo Apr14 file添加是未定的更早身份线索而非不可变首发证明，不将整个family称为确定窗外；不为无拟采用命题无限追历史，不将日期未定伪装重复候选。

原509关闭分布与原47研究层审计继续保留在[`V3_RECERTIFICATION.md`](../_sources/daily-20260501/V3_RECERTIFICATION.md)，不把旧556全量库存或旧Completed标签当本轮来源/准入验收。

## 6. 复核

以下旧复核只属于冻结的原47家族；不代替2026-10-16补查日级验收。

原47研究层复核者：`weekly_w37`（非作者 fresh-context reviewer）
原47研究层结论：通过

独立复核重新计算了 556 个唯一 identity 及 old 63 → new 47 的集合关系，逐项复查 26 个降级与 10 个恢复，并对其余关闭项按高风险主题和关闭理由分层抽查；未发现需要新增或剔除的候选。47 项的日期范围、三维评分、证据边界与处置均无冲突；10 个恢复项重新打开 exact-v1 HTML，未见撤回提示。21 项“整合”均在当前 Books owner 中找到具体机制正文和唯一来源标记，而非仅有 trace 标签；复核发现 ZipCCL 标记被后续段落隔开，已移动回对应通信压缩正文之后，未改变书稿语义。14 个 Daily 来源均有本窗范围与结果，历史目录的可变性按终态保留项隔离。跨模型第二意见未执行；本次非作者独立复核已覆盖合同要求的风险面。

复核者：`root`（本轮补查；非报告作者、非五处Books写入者）
结论：通过

2026-10-16实际日级检查六部分新增10项及[唯一SUP A11–13](../_sources/daily-20260501/SUP_SOURCES_20261016.md)，此前分批准入/必要Source/owner与五处正文、完整上下邻接、本人注实际POST均独核通过。确认原47整行/旧窗/原连续§4保留、新10=5整合/1已有覆盖/2仅报告/2中心争议、合57；本地63引用无缺、围栏/V3及限定cached/unstaged diff检查通过，无普通可执行工作。Seed1637仅Apr30必要正文/日期资格Hold，1654/1665为May1窗外；Hunyuan9/6是不同renderType而非不同语言，均只英文可见切片；不将隔离缺口授Coverage/Evidence通过。

实际纠正过程保留在SUP A4–A13：26341从过早EX恢复P5，COPUS因漏读实际owner撤回本次重复正文/本人注并复用有效前关；Seed统一时区误读只扩查受影响P20日期层，原候选日期不动。26506安全EX本轮追加root必要core/实际owner负侧核，不由旧未覆盖抽样范围授审。

明确EX按来源、主题和理由分层：root actual完整AB校准首批26615/26211/26591与12消歧项；26297/26830为局部优化、26419为高风险自评混杂、26492为成熟codec原语继承，另26653/26805各读决定性core；DenialBench同exact-v1具名旧EX实际身份复用，CLBench读取精确Apr30构造/评价与实际Ch75/66，Qwen只按所取得发布核心判断、不拼后发report。未将其余所有旧EX称作全量重新正文复核；有效层仅按命中单条版本/命题/反证/原独立层复用。

机器检查：2026-10-16 `python3 scripts/validate_research.py --report papers/2026/05/01/README.md`通过；本日文件/四章写入范围`git diff --check`通过，本日报本地链接无断链。baseline比较原47行逐字一致、原§4为当前连续前缀、原小时窗口未变；当前57唯一ID、新10项日期均Apr30、SUP48EX条目与63身份归并一致。初次检查发现未挂冻结日期基线及6个新标题别名不匹配，补齐官方标题/基线链接后重检通过，没有改校验器或原候选。
