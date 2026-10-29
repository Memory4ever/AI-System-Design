# Daily Research — 2026-06-17

**规范：** V3
**窗口：** 2026-06-16T09:00:00+08:00 ～ 2026-06-17T09:00:00+08:00
**窗口说明：** 按用户“保留已有候选日期、评分和小时窗，仅补遗漏”的授权保留原窗口及有效旧候选；原51项中一项经官方撤回后清除采用链，现保留50项，不搬移其余归属。
**补充窗口：** 2026-06-16 ～ 2026-06-16
**冻结候选日期：** [原51候选档案](../_sources/daily-20260617/baseline-before-supplement-20261026.md)
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-29T11:45:10+08:00

**补查检查时间：** 2026-10-26（Asia/Shanghai）

## 1. 结论

本轮补充候选逐项处理已落实，root§136独立整日报DAY验收通过；不依赖旧完成标签。[本轮准入与去重](../_sources/daily-20260617/SUP_ADMISSION_20261026.md)、[必要证据与书稿决定](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。随后发现一项旧采用的官方撤回信号，已按研究合同定点清除其候选、评分、证据与唯一书稿依赖，由不同角色`jun18_supp_author`在本日独核§139完成实际写后确认；其他有效研究不重开。现139家族＝有效旧50＋新增89；新增处置仍为74真实整合、10具体已有覆盖、5中心争议隔离（14883/14997/16541/16883/15897），普通研究与技术POST待办为0。有限来源/准入层与新增实际POST沿root§62–63及§136有效范围复用，不再扩源或号段。代表N为分层抽检并非全量复读，14715/16730/15669具体理由已纠正。另10项精确旧Jun16 retained链保原日期/原9，本日不迁日、重评分或计新家族。

本轮主线增量是把训练信号、内部状态与实际消费者逐一分责：局部优化/适配的低loss不等query或后续任务收益；生成器改变权重、条件人口或中间表示后须重新核对终态，不能只检查原标签和sampler；motion与action共用生成接口仍需兼容标签、坐标和独立物理执行验收。机制、失败条件和全部成本已在相应owner正文就近保留。五个中心冲突仅隔离被反证的采用主张，不由未审阅或访问成本制造暂缓，也不让局部实验取得通用保证。

以下为旧窗口有效基线，保留其历史范围；本轮补查验收另见上述当前结论和§6，不由旧标签推定：

旧记录当时对534个arXiv身份形成50项候选与484项排除，再加入GLM-5.2一项。经本次撤回清理后，有效旧候选为50项＝14项实际整合、36项具体已有覆盖；原始档案保留历史排除与纠错依据，不再把撤回版本算入选或正面证据。其他旧候选的原日期、评分及有效研究层未变。

## 2. 来源覆盖

以下为2026-10-26本轮实际入口和停止范围，原小时窗来源证据保留在[旧档案](../_sources/daily-20260617/baseline-before-supplement-20261026.md)；不以旧来源标签授补充自然日覆盖。完整查询/原件定位见[本次来源记录](../_sources/daily-20260617/SUP_SOURCE_20261026.md)。尚未处理的普通工作与已隔离的历史目录限制分开列出。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1318项只取Jun14–18邻段，Jun16 Deployment Simulation完整核心/限制已读；root§20/24/28/30必要与真实Book POST通过，未将later论文2607.07184迁日 | 已检查 | 无；只所述主题切片，不授尾风险覆盖 |
| SRC-ANTHROPIC | Research listing page2共24项Jul28→Apr23，目标Jun16 Claude Code expertise完整核心为使用方式/职业经验统计，不新增模型或执行机制，N；已越窗不翻后页 | 已检查 | 无；只对所述研究主题切片 |
| SRC-GOOGLE-AI | DeepMind page2 Jun18→Jun16 UK planning→Jun11，Jun16完整核心为应用工作流，N；Research June博客12条一页，Jun16 Earth AI为暂缓科学应用 | 受阻 | Blog切片已处理；Publications历史日级目录未恢复，隔离且不授零研究或全Google覆盖 |
| SRC-META-AI | Research仅壳；Blog可见Jun29→Apr8无本日卡片；Publications page1/2前部2026条目后混2016–2020旧记录，page2可见Jun29→Jun5越窗 | 受阻 | 可见邻段已核；混排页不证明连续历史Research日级档案，无全覆盖/零发布保证 |
| SRC-QWEN | 英/中文官方retrieval各40项无nextpage，Jun1→Jun16 RobotNav/World/Manip/Suite→Jun23；Nav/Manip完整core与日证已root§20准入，World旧同v1去重，Suite无独立增量 | 已检查 | Nav/Manip证据/具体Books处置及实际POST已闭，见§4/root§20/24/28/30；API/HTML明确+08日期，SSR June15显示差不泛化成全源H |
| SRC-DEEPSEEK | 官方主入口模型导航及updates Jul31→Apr24越窗，无Jun16具名项；未扩普通commits | 已检查 | 无；不宣称互联网无遗漏 |
| SRC-MOONSHOT | Blog仅到2025Nov07；官方org42个repo的created_at本窗无新身份，定点本日主题补检未恢复具名原始发布，不用updated_at充首公开 | 受阻 | 2026历史Blog档案未恢复；旧页面/搜索无命中不支持零发布 |
| SRC-TENCENT-HUNYUAN | Research publicList POST中文/renderType0，page1 size100,total11/list11，无nextpage；Jul6→May21越窗无Jun16 | 已检查 | 无；未把显示日冒全球首次公开 |
| SRC-ZAI | Research首查Jun16 GLM5.2→May20 ZCube，GLM5.2为本日报旧51之一，精确同官方事件去重 | 已检查 | 无；原日期/评分与有效证据保留 |
| SRC-BYTEDANCE-SEED | public_papers page1共20/247，Jun19→Jun11→Jun4/3越窗；五类Blog完整可见12/12/5/3/9卡片均越过Jun16，无next/page导航；未扩科学应用正文 | 已检查 | 无；范围为本项目研究主题与具名入口 |
| SRC-BAIDU-ERNIE | blog/zh首屏最新May9文心5.1，已早于窗口，不翻更旧第二页 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 首页Paper Jun29→Mar13；ModelRelease Sep22→Jun2→Apr23；具名官方bundle恢复Blog日期Jun10/Jun8，无Jun16项 | 已检查 | 无；不从无日期卡片猜日 |
| SRC-MINIMAX | 英/中文Blog完整单页Jun9→Jun1越窗；AgentTech独立4项Sep19→Oct20均晚于本窗，不展开无关正文 | 已检查 | 无 |
| SRC-ARXIV | 四主题DataCite导航410/74/168/137，合并568身份/76旧表命中，5/1/1/1页到total；六类官方月分页只取14700–17050固定号段相关标题，1060跨类唯一/与主题nav重492，均到末页；实际首5/后29/最后63相关题摘见来源记录末节，已停止扩源，registered/号段不单独当公告日 | 已检查 | 有界题摘/准入与最后窄决定点经root§62–63闭合，86个新arxiv家族逐一核exact-v1/合法联合日界；1060/nav/初303非逐项关闭队列，不授全网无遗漏。具名跨日日期保留隔离，不支持当窗候选/Books或该范围Coverage |

旧窗口分母前关闭记录、22个恢复项和原精确v1证据继续保留；这些旧审计结果不代替本轮准入。当前按完整题摘/官方核心的具体机制、边界或反证筛选，不按章节映射、模块组合名称或领域指标扩池。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [GLM-5.2](https://www.zhipuai.cn/zh/research/161) | 2026-06-16T16:00:00+08:00 | 官方页披露跨四个稀疏层共享一个 query-aware indexer 的 `IndexShare`，具体改变 selector state 的刷新与复用边界；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[owner](../../../../books/part-02-model/22-long-context.md)；命题锚点：Sparse Attention 的两个 ownership 轴 |
| [The Price of Anarchy in Disaggregated Inference](https://arxiv.org/html/2606.17081v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-PD-DISAGGREGATION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-PD-DISAGGREGATION，[owner](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；正文锚点：从静态 Pool Ratio 到耦合的 SLO Control State |
| [Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work](https://arxiv.org/html/2606.17099v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Handoff 必须保留约束的 Action-binding Strength |
| [Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators](https://arxiv.org/html/2606.17104v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-PD-DISAGGREGATION 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-PD-DISAGGREGATION，[owner](../../../../books/part-05-inference-system/55-pd-disaggregation.md)；命题锚点：局部加速必须通过完整部署账本 |
| [Models Take Notes at Prefill: KV Cache Can Be Editable and Composable](https://arxiv.org/html/2606.17107v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：双向更新会撤销“共享 Prefix 永远不可变”的前提 |
| [Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs](https://arxiv.org/html/2606.17110v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：模型内部路由、训练数据与 Weight Repair 都进入攻击面 |
| [TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations](https://arxiv.org/html/2606.17122v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 TRAIN-DATA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；正文锚点：另一分支把可撤销表示封装在带 passport 的 adapter / LoRA 中 |
| [Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems](https://arxiv.org/html/2606.17182v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；命题锚点：声明式协议约束 Transition，而不是相信参与者会协调 |
| [MemTrace: Probing What Final Accuracy Misses in Long-Term Memory](https://arxiv.org/html/2606.17328v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：用干预矩阵定位写入、检索与阅读失败 |
| [RISE: Relay Inference and Online Scheduling for Efficient Edge-Device Collaborative Diffusion Model Services](https://arxiv.org/html/2606.17378v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；正文锚点：迭代生成与流式会话需要显式 Progress State |
| [Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation](https://arxiv.org/html/2606.17383v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Confidence 要在 Belief、Action 与 Outcome 三层校准 |
| [Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving](https://arxiv.org/html/2606.17421v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：隐私不是一个开关，而是明文边界的重新分配 |
| [PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents](https://arxiv.org/html/2606.17467v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；正文锚点：RAG 安全必须覆盖完整状态生命周期 |
| [SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation](https://arxiv.org/html/2606.17518v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；命题锚点：Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission |
| [Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery](https://arxiv.org/html/2606.17519v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-TOOL-CALLING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[owner](../../../../books/part-07-agent/78-tool-calling.md)；命题锚点：Tool Discovery 与选择 |
| [AoiZora: Topology-Aware Auto-Parallel Optimization for Inference of Diffusion Transformers](https://arxiv.org/html/2606.17566v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-TENSORRT-LLM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[owner](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；正文锚点：分布式 DiT Plan 必须经过编译后拓扑复排 |
| [Cordon: Semantic Transactions for Tool-Using LLM Agents](https://arxiv.org/html/2606.17573v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-WORKFLOW 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[owner](../../../../books/part-07-agent/81-workflow.md)；命题锚点：Durable Execution 与 Replay |
| [Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning](https://arxiv.org/html/2606.17591v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MEMORY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY，[owner](../../../../books/part-07-agent/77-memory.md)；命题锚点：从原始轨迹到派生策略：Memory 的演进不是无限追加 |
| [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/html/2606.17730v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：Persistent world state |
| [LUMEN: Coordinated Failure Recovery for Distributed LLM Serving](https://arxiv.org/html/2606.17787v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-SCHEDULING 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：MoE Failure Recovery 必须拥有 Request 与 Expert Generation |
| [AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor](https://arxiv.org/html/2606.17872v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 INFER-KV-CACHE 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[owner](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；命题锚点：压缩后的答案正确不等于证据仍被保留 |
| [How Inference Compute Shapes Frontier LLM Evaluation](https://arxiv.org/html/2606.17930v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：生成迭代次数不能代替实际计算预算 |
| [RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving](https://arxiv.org/html/2606.17949v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-GATEWAY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-GATEWAY，[owner](../../../../books/part-06-ai-infrastructure/62-gateway.md)；命题锚点：Gateway、EPP 与 Engine Scheduler |
| [ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents](https://arxiv.org/html/2606.18037v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-RAG 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-RAG，[owner](../../../../books/part-07-agent/76-rag.md)；命题锚点：视觉证据也必须有可追踪的 Claim–Evidence 生命周期 |
| [On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization](https://arxiv.org/html/2606.18121v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 AGENT-MULTI-AGENT 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MULTI-AGENT，[owner](../../../../books/part-07-agent/82-multi-agent.md)；正文锚点：Coordination Failure |
| [All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code](https://arxiv.org/html/2606.18168v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-EVALUATION-SYSTEM 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Harness Optimization 的 Test Boundary 必须对优化器不可见 |
| [Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners](https://arxiv.org/html/2606.18198v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 PLATFORM-SECURITY 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Skill Poisoning 的真值是 Side Effect，而不是是否被调用 |
| [Looped World Models](https://arxiv.org/html/2606.18208v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-WORLD-MODELS 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：Persistent world state |
| [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/html/2606.18247v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | exact-v1 提供面向 MULTIMODAL-EMBODIED-VLA 的具体机制或边界，V3 题摘复筛确认属于大模型/Infra 主线；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；正文锚点：Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限 |

<!-- full-raw-recovered-candidate-rows:start -->
| [Towards Distributed Inference of LLMs on a P2P Network](https://arxiv.org/html/2606.17059v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；已实际写入正文；正文锚点：低带宽拓扑要联合预算 Hops、Bytes 与 Steps |
| [Statistical Foundations of LLM-based A/B Testing: A Surrogacy Framework for Human Causal Inference](https://arxiv.org/html/2606.17165v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已实际写入正文；正文锚点：Canary / A/B |
| [Rethinking Groups in Critic-Free RLVR](https://arxiv.org/html/2606.17250v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；命题锚点：Verifiable Reward 不等于每个样本都可学习 |
| [OTRO: Oblivious Tokenization Path with Square-Root ORAM](https://arxiv.org/html/2606.17358v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；已实际写入正文；正文锚点：Partial TEE 协议的秘密随机性不得跨请求复用 |
| [Dissecting model behavior through agent trajectories](https://arxiv.org/html/2606.17454v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-PLATFORM，[owner](../../../../books/part-07-agent/84-agent-platform.md)；命题锚点：Agent harness 必须把 model intent、实际 tool payload、environment result 与回送 context 做成双向可观测接口 |
| [Online LLM Selection via Constrained Bandits with Time-Varying Demand](https://arxiv.org/html/2606.17489v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-SCHEDULING，[owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)；命题锚点：多轮 Routing 是带剩余预算的序列决策 |
| [MagicSim: A Unified Infrastructure for Executable Embodied Interaction](https://arxiv.org/html/2606.17511v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；命题锚点：Batched Environment 需要持久且可寻址的状态池 |
| [DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack](https://arxiv.org/html/2606.17574v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Cross-layer Evaluation 不允许下游成功掩盖上游故障 |
| [TivTok: Broadcasting Time-Invariant Tokens for Scalable Video Tokenization](https://arxiv.org/html/2606.17590v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已实际写入正文；正文锚点：Codec-aware tokenization：稀疏性可以在视觉 Encoder 之前暴露 |
| [The Benchmark Illusion: Pruned LLMs Can Pass Multiple Choice but Fail to Answer](https://arxiv.org/html/2606.17609v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；已实际写入正文；正文锚点：压缩模型的 release gate 也不能停留在平均 perplexity |
| [Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering](https://arxiv.org/html/2606.17799v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：Evaluation Identity 必须包含 Harness 与 Environment |
| [Beyond Native Success: Auditing Deployment-Interface Exposure of CLIP Backdoors](https://arxiv.org/html/2606.17815v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Embedding 也是可执行数据供应链的一部分 |
| [Small Initialization Matters for Large Language Models](https://arxiv.org/html/2606.17945v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；命题锚点：Optimizer 不是与参数化无关的旋钮 |
| [SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs](https://arxiv.org/html/2606.17952v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-MOE，[owner](../../../../books/part-02-model/21-moe.md)；命题锚点：从固定 Top-k 到受总预算约束的 Variable-k |
| [VoidPadding: Separate Padding from Semantic Termination in Masked Diffusion Language Models](https://arxiv.org/html/2606.17999v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；已实际写入正文；正文锚点：固定长度 Diffusion 把长度预测变成 Admission 决策 |
| [Recursive Scaling in Masked Diffusion Models](https://arxiv.org/html/2606.18022v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER，[owner](../../../../books/part-02-model/17-transformer-layer.md)；命题锚点：Parameter Depth 与 Execution Depth 可以分离 |
| [Latency Prediction for LLM Inference on NPU Systems](https://arxiv.org/html/2606.18042v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；命题锚点：从直接 Grid Search 到 Floor-first Diagnosis |
| [Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping](https://arxiv.org/html/2606.18120v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[owner](../../../../books/part-06-ai-infrastructure/72-security.md)；命题锚点：Instruction Hierarchy 必须携带 Authenticated Provenance |
| [Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers](https://arxiv.org/html/2606.18206v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MODEL-TRANSFORMER-LAYER，[owner](../../../../books/part-02-model/17-transformer-layer.md)；命题锚点：Parameter Depth 与 Execution Depth 可以分离 |
| [Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification](https://arxiv.org/html/2606.18249v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；已实际写入正文；正文锚点：统一架构不等于双向可用的统一语义空间 |
| [Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/html/2606.18250v1) | 2026-06-17T08:00:00+08:00 ～ 2026-06-17T09:00:00+08:00 | 全量 raw 反向审计恢复；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[owner](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；命题锚点：从 RGB Rollout 到 Projective 4D Predictive State |
| [Learned Image Compression for Vision-Language-Action Models（SPARC）](https://arxiv.org/html/2606.16253v1) | 2026-06-16 | 通用codec的视觉保真不等VLA控制效用；以历史latent mask和tilted-rate目标分配线上观测码率；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26压缩容忍度](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#压缩容忍度应由动作敏感性定义)；root§4实际POST通过 |
| [Adaptive inference and function vectors in deep transformers](https://arxiv.org/html/2606.16694v1) | 2026-06-16 | 固定通信预算下MLP依据已有统计选择下一测量，Gaussian与tree prior给出深度适用反侧；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Ch17条件算法解释](../../../../books/part-02-model/17-transformer-layer.md#层堆叠可以被解释成迭代优化但不是-hidden-state-真理)；root§7实际POST通过 |
| [Generated, Parallel, Scalable? A Study of Agentic AI-Generated Julia Code on Supercomputers](https://arxiv.org/html/2606.16534v1) | 2026-06-16 | 自生成harness与小输入可运行不能保证目标规模并行语义/资源，暴露deadlock/oversubscription/OOM；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；shape/runtime与隐藏配置验收，root§8具体NC |
| [Shift-and-Sum Quantization for Visual Autoregressive Models](https://arxiv.org/html/2606.16131v1) | 2026-06-16 | 粗尺度attention会放大Value量化误差，以对称移位副本/同格式预算及校准边际重采样分责；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49量化补偿](../../../../books/part-05-inference-system/49-tensorrt-llm.md#量化为什么不自动带来加速)；root§14实际POST通过 |
| [Understanding Cross-Modal Contributions in Continual Vision-Language Models: A Theoretical Perspective](https://arxiv.org/html/2606.14883v1) | 2026-06-16 | 跨模态贡献/CBF优化的定义域与中心等价推导存在具体未闭条件；2 + 1 + 2 = 5 | 争议 | 暂缓：Def4.7/Th4.11中心证明未闭，root§15安全隔离；见§5重开条件 |
| [Inference-time Policy Steering via Vision and Touch](https://arxiv.org/html/2606.14981v1) | 2026-06-16 | 预测长视觉选mode、短触觉编辑分horizon消费；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 action chunk](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§21实际POST |
| [Beyond Layer Importance in Layer-wise Sparsity: An Inter-Layer Perturbation-Absorption Perspective](https://arxiv.org/html/2606.15161v1) | 2026-06-16 | 剪枝扰动幅度与后层吸收共同约束layer预算；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49 扰动传播](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；root§49实际POST |
| [VLALeaks: Membership Inference Attacks against Vision-Language-Action Models](https://arxiv.org/html/2606.15165v1) | 2026-06-16 | 白盒分区attention统计形成监督membership sensor，中心因果与低FPR另验；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72 Membership Signal](../../../../books/part-06-ai-infrastructure/72-security.md)；root§18有限sensor，不采用中心因果/防御失效 |
| [Adaptive Inference-Time Scaling via Early-Step Latent Verification for Image Editing](https://arxiv.org/html/2606.15188v1) | 2026-06-16 | 早步latent activation/空mask Gate与最终像素选择分责；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24 Draft/Verify](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§21实际POST |
| [Semantic DLM+: Improving Diffusion Language Models through Bias-variance Trade-off in Transition Kernel Design](https://arxiv.org/html/2606.15327v1) | 2026-06-16 | semantic邻域困陷、全局跳转与精确/邻域频率反馈分责；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24 Uniform corruption](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§21实际POST |
| [Robots as Tokens: Unified Diffusion Transformer for Coordinated Multi-Robot Trajectory Generation](https://arxiv.org/html/2606.15550v1) | 2026-06-16 | joint robot-chunk与已知轨迹条件，训练地图head/部署移除；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 协同proposal](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§26实际POST |
| [Distilling Drifting Transformers with Representation Autoencoders](https://arxiv.org/html/2606.15553v1) | 2026-06-16 | RAE几何与distribution-level drifting蒸馏目标配对；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24 RAE漂移目标](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§58实际POST |
| [Localizing Credit at the Divergence: Path-Conditioned Self-Distillation for LLM Reasoning](https://arxiv.org/html/2606.15576v1) | 2026-06-16 | 成功peer rollout按轨迹分歧定位dense credit，不另采新轨迹；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO，[Ch33 peer teachercontext](../../../../books/part-04-training-system/33-grpo.md)；root§49实际POST |
| [MoECa: Aligning Feature Reuse with Expert Decomposition in Diffusion Transformers](https://arxiv.org/html/2606.15615v1) | 2026-06-16 | 以expert branch而非整个token定义DiT-MoE跨步复用资格；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24 branch cache](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§55实际POST |
| [The Reservoir Attention Network: Cross-Pass State in Pretrained Transformers via Content-Addressable Reservoir Injection](https://arxiv.org/html/2606.15678v1) | 2026-06-16 | 固定随机reservoir提供跨forward可重置状态；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22 跨pass状态](../../../../books/part-02-model/22-long-context.md)；root§58实际POST |
| [Learning New Tasks via Reusable Skills: Skill-Compositional Experts for Embodied Continual Learning](https://arxiv.org/html/2606.15685v1) | 2026-06-16 | 将可复用skill执行与skill间transition专家分开，检验闭环遗忘；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 skill双分支](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§61实际POST |
| [RoboPIN: Grounded Embodied Reasoning via Pinned Chain-of-Thought](https://arxiv.org/html/2606.15753v1) | 2026-06-16 | 显式entity anchor与跨步/视角identity process reward；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；Ch26 VLMcontroller总论后/导览仲裁前，root§67真实POST |
| [Wasserstein Convergence of ODE-Based Samplers in Decentralized Diffusion Model via Velocity Field Decomposition](https://arxiv.org/html/2606.15835v1) | 2026-06-16 | 按状态时刻posterior随机local velocity及其route方差/参考过程条件；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24 随机field](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§41实际POST |
| [Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization](https://arxiv.org/html/2606.16111v1) | 2026-06-16 | Pareto dominance rank替代标量化advantage的policy更新；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；08545后/FGRPO前，root§73真实POST |
| [The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematical Reasoning](https://arxiv.org/html/2606.16152v1) | 2026-06-16 | 高reward teacher样本不等student效用，style/logic修复控制；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md)答案质量/学生效用与共同正确人口对照 |
| [A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization](https://arxiv.org/html/2606.16154v1) | 2026-06-16 | advantage符号/分布对entropy更新的分解及正advantage clipping；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO，[owner](../../../../books/part-04-training-system/33-grpo.md)；06650后/negative-only前，root§73真实POST |
| [Cascaded Sparse Autoencoders Learn Multi-Level Visual Concepts in Multimodal LLMs](https://arxiv.org/html/2606.16193v1) | 2026-06-16 | 对一级decoder atoms作二级稀疏抽象并joint反传，非再压sample code；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5 字典抽象](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；root§29实际POST |
| [Latent Thought Flow: Efficient Latent Reasoning in Large Language Models](https://arxiv.org/html/2606.16222v1) | 2026-06-16 | 随机连续可变长轨迹匹配quality/cost后验目标；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-DECODER-ONLY，[owner](../../../../books/part-02-model/18-decoder-only.md)；Ch18 GLR后/fusion前，root§69真实POST |
| [Data Augmentations for Data-Constrained Language Model Pretraining](https://arxiv.org/html/2606.16246v1) | 2026-06-16 | 固定语料多epoch增强/组合的过拟合条件；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-PRETRAINING，[owner](../../../../books/part-04-training-system/28-pretraining.md)；Ch28 TokenSuperposition后/双语配对前，root§67真实POST |
| [KeepLoRA++: Continual Learning with Layer-Scaled Residual Gradient Adaptation](https://arxiv.org/html/2606.16256v1) | 2026-06-16 | 预训练与旧任务双子空间保留、按深度缩放更新；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-LORA，[Ch30 固定basis/support/scale](../../../../books/part-04-training-system/30-lora.md)；root§56有限NC，强recipe隔离 |
| [Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate](https://arxiv.org/html/2606.16360v1) | 2026-06-16 | 文本步骤与typed latent operator/预算选择的计算接口；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-DECODER-ONLY，[owner](../../../../books/part-02-model/18-decoder-only.md)；25745后/工作状态H3前，root§73真实POST |
| [CacheMuon: Using Temporal Preconditioning To Approximate Polar Factor](https://arxiv.org/html/2606.16371v1) | 2026-06-16 | 缓存polar preconditioner并分别控制staleness/solver误差；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28 跨步transform](../../../../books/part-04-training-system/28-pretraining.md)；root§49实际POST |
| [LOCUS: Local Visual Cue Search for Enhancing Fine-Grained Perception in Multimodal Large Language Models](https://arxiv.org/html/2606.16586v1) | 2026-06-16 | 训练crop→full-image support定位奖励，推理保原接口；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23 训练局部搜索](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root§61实际POST |
| [Diffusion Flow Matching: Dimension-Improved KL Bounds and Wasserstein Guarantees](https://arxiv.org/html/2606.16610v1) | 2026-06-16 | KL误差人口/截断与另有曲率条件的W2保证分开；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24 误差人口/参考/截断](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§39具体NC |
| [Predicting model behavior before release by simulating deployment](https://openai.com/index/deployment-simulation/) | 2026-06-16 | 旧prefix单响应重采、同模型fidelity与发布后population shift分账；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66 人口代表性](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root§30实际POST |
| [Qwen-RobotNav: A Scalable Navigation Model Designed for an Agentic Navigation System](https://qwenlm.github.io/blog/qwen-robotnav/) | 2026-06-16 | 训练随机化四轴、部署显式taskmode/观测配置的policy条件接口；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 训练内显式观测配置](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§46实际POST |
| [Qwen-RobotManip: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://qwenlm.github.io/blog/qwen-robotmanip/) | 2026-06-16 | 有效slot/相机坐标与history条件分责的跨embodiment对齐；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 slot/frame/history](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§46实际POST |


| [Scaling Short-Term Memory of Visuomotor Policies for Long-Horizon Tasks](https://arxiv.org/html/2606.16178v1) | 2026-06-16 | inputfeature条件化postattention gate与static scalar/sink反侧；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26 memory消费](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§46实际POST |
| [Relational Structural Causal Models](https://arxiv.org/html/2606.14892v1) | 2026-06-16 | 可变对象组合中观察/因果查询识别的额外假设；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Books](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；root§106实际POST通过 |
| [Simplifying the Modeling of Arbitrary Conditionals in Natural Language](https://arxiv.org/html/2606.14943v1) | 2026-06-16 | 保LTR/NTP的causalTransformer任意past/future条件采样接口；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-DECODER-ONLY，[Books](../../../../books/part-02-model/18-decoder-only.md)；root§105实际POST通过 |
| [AI Engram: In Search of Memory Traces in Artificial Intelligence](https://arxiv.org/html/2606.14997v1) | 2026-06-16 | 约束逆问题提取参数trace及有限线性组合/擦除条件；2 + 1 + 2 = 5 | 争议 | 暂缓：root§77中心命题冲突隔离，不入Books；具体反例及重开条件见§4 |
| [Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale](https://arxiv.org/html/2606.15079v1) | 2026-06-16 | 架构迁移既有base、混合attention与异步环境rollout的实际状态条件；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Books](../../../../books/part-02-model/22-long-context.md)；root§109实际POST通过 |
| [AdaMame: A Training Recipe for Adaptive Multilingual Reasoning](https://arxiv.org/html/2606.15080v1) | 2026-06-16 | queryconditioned语言约束随RL阶段从探索到利用改变；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-GRPO，[Books](../../../../books/part-04-training-system/33-grpo.md)；root§105实际POST通过 |
| [Spokes: Optimizing for Diverse Pretraining Data Selection](https://arxiv.org/html/2606.15216v1) | 2026-06-16 | 对集合多样性而非独立样本proxy作概率选择/联合质量优化；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：TRAIN-DATA，[owner](../../../../books/part-04-training-system/27-data.md)；集合关系/质量联合与proxy实训效用，root§75具体NC |
| [FARM: Find Anything using Relational Spatial Memory](https://arxiv.org/html/2606.15476v1) | 2026-06-16 | VLM语义与显式object关系/几何谓词的空间memory检索分责；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；17351完整两段后/2510.01519前，root§86真实POST |
| [PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents](https://arxiv.org/html/2606.16215v1) | 2026-06-16 | prompt-only rollout与仅优化时privilegedtrace监督/anchor分责；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)；peer15576后/PromptRobustness前，root§81真实POST |
| [HiMPO: Hindsight-Informed Memory Policy Optimization for Less-Entangled Credit in Long-Horizon Agents](https://arxiv.org/html/2606.16285v1) | 2026-06-16 | 固定prewrite state比较memory信息可恢复性以形成memorytoken信用；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)；MemPO00680后/03329前，root§81真实POST |
| [PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/html/2606.16449v1) | 2026-06-16 | appearance/depth memory的editaware更新与复用失效资格；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；22622后/33589前，root§84真实POST |
| [The Faithfulness Gap: Certifying Semantic Equivalence Between Natural-Language and Formal Mathematical Statements](https://arxiv.org/html/2606.16541v1) | 2026-06-16 | 双向consequence/probe检查typecheck不保证的NLformal语义一致；2 + 1 + 2 = 5 | 争议 | 暂缓：root§77中心命题冲突隔离，不入Books；具体反例及重开条件见§4 |
| [DCP-Prune: Ultra-Low Token Pruning with Distribution Consistency Preservation](https://arxiv.org/html/2606.16633v1) | 2026-06-16 | 删除前context传递与distribution-shift代理控制代表token重选；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；PCA15621后/TREN前，root§79真实POST |

| [Sensor-Conditioned Representation Learning via Scene-Relevant Observation Quotients](https://arxiv.org/html/2606.16210v1) | 2026-06-16 | 重建/任务准不能决定sensor支持哪些scene区分 → nuisancecanonicalization后的observationquotient与falsemerge/distinction控制 → 改变可表示/不可观测差别的验收；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Books](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root§109实际POST |
| [Upper Bounds on the Generalization Error of Deep Learning Models via Local Robustness and Stability](https://arxiv.org/html/2606.16883v1) | 2026-06-16 | globalrobustnessterm抹去各子域稳/不稳样本结构导致vacuous → 按子域stablecount重权的data/modeldependent界 → 改变何种鲁棒性统计支持generalization声称；2 + 1 + 2 = 5 | 争议 | 暂缓：总体条件质量/训练计数混同、近零残差删去；root§107中心反例，重开条件见§4/5 |
| [Can Neural Networks Achieve Optimal Computational-statistical Tradeoff? An Analysis on Single-Index Model](https://arxiv.org/html/2606.15219v1) | 2026-06-16 | SQ下界不等梯度网络可达 → 标签变换/landscape smoothing与稀疏weightperturbation实现相应Gaussian模型featurelearning复杂度 → 修正计算/统计可达性关系；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN，[Books](../../../../books/part-01-worldview/04-why-models-learn.md)；root§116实际POST |
| [GRASP: Gradient-Aligned Sequential Parameter Transfer for Memory-Efficient Multi-Source Learning](https://arxiv.org/html/2606.14900v1) | 2026-06-16 | 多source同时融合须多模型驻留 → 逐source并入当前target、按target梯度方向逐参数准入后再适配 → 改变迁移state/negative transfer与内存前沿；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-LORA，[Books](../../../../books/part-04-training-system/30-lora.md)；root§98实际POST |
| [Representation Costs in Data Science: Foundations and the Quasi-Banach Spaces of Deep Neural Networks](https://arxiv.org/html/2606.14954v1) | 2026-06-16 | 参数weightdecay不一定诱导函数空间norm → 深度ReLU representationcost的quasiBanach/p=2/L结构与param/function优化连接 → 修正把深度归纳偏置当凸norm正则的解释；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN，[Books](../../../../books/part-01-worldview/04-why-models-learn.md)；root§106实际POST |
| [MVEB: Massive Video Embedding Benchmark](https://arxiv.org/html/2606.14958v1) | 2026-06-16 | 同一audio输入在不同标签来源不等更完整groundtruth → 成对videoonly/AV、按annotation provenance出现方向相反收益 → 改变是否启用音频与多模态embedding评价人口；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Books](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root§94实际POST |
| [FastMix: Fast Data Mixture Optimization via Gradient Descent](https://arxiv.org/html/2606.14971v1) | 2026-06-16 | 搜mixture多proxy贵 → 单proxy把sourceweight置入双层目标，验证feedback交替更新mixture/model → 改变样本人口、外层梯度与搜索成本，非‘自动选比’命名；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)；validation局部方向与BLISS proxy/hypergradient，root§87具体NC |
| [An Integrable Token Mixing Layer from the Generalized Yang Baxter Equation](https://arxiv.org/html/2606.15085v1) | 2026-06-16 | 顺序混合/变budget可能改函数 → 由局部代数约束构正交map及commutingtransfer、circulant长度扩展 → 潜在改变order/budget是否同一函数的架构解释；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER，[Books](../../../../books/part-02-model/17-transformer-layer.md)；root§111实际POST |
| [Beyond Accuracy: Measuring Bias Acknowledgment in Chain-of-Thought Reasoning for Responsible AI Evaluation](https://arxiv.org/html/2606.15127v1) | 2026-06-16 | finalanswer不变掩盖trace未提示外部bias → 同注入人口分susceptibility与rubric表面acknowledgment，模型分离 → 改变trace可审计性与answeraccuracy的评价合同；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；书面承认/最终行为/条件人口分验，root§87具体NC |
| [GeoStream: Toward Precise Camera Controlled Streaming Video Generation](https://arxiv.org/html/2606.15162v1) | 2026-06-16 | 首帧固定3Dcache越frustum失效，自生成cache又递归带错 → 在线从生成帧重建/投影几何，并在训练也消费studentgenerated几何条件 → 改变二阶conditioningfeedback的人口/刷新合同；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Books](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§111实际POST |
| [FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing](https://arxiv.org/html/2606.15186v1) | 2026-06-16 | 编辑目标与背景共享attention会互扰 → inversion后按时程解耦attention/区域限制，再按任务加noise → 改变何时允许局部条件改写背景；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；source保留/后段释放与音频再生分责，root§110具体NC |
| [StarOR: Synergizing Tree Search and Test-Time Reinforcement Learning for Optimization Modeling](https://arxiv.org/html/2606.15197v1) | 2026-06-16 | fixedpolicy MCTS反复同偏差、只terminal credit稀 → 每非终结node用siblings比较组更新临时LoRA/GRPO → 改变searchstate/参数state与局部reward信用；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-PLANNING，[Books](../../../../books/part-07-agent/79-planning.md)；root§116实际POST |
| [Rethinking Implicit Spatial Representation in Visuomotor Policy Learning](https://arxiv.org/html/2606.15232v1) | 2026-06-16 | 相同encoder局部pooling与downsample会丢精细位置 → 受控spatialsoftmax比较+multiscale topdown crossattn保空间表示 → 改变低分辨率精密动作的表示瓶颈；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Books](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§94实际POST |
| [When to use what Schatten-$p$ norm in deep learning?](https://arxiv.org/html/2606.15268v1) | 2026-06-16 | Muon式几何并非所有regime最好 → 低维/Chinchilla与noise/batch条件可使小p最优，SODA加速界 → 改变选范数/批量的适用域；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-PRETRAINING，[Books](../../../../books/part-04-training-system/28-pretraining.md)；root§116实际POST |
| [Ricci-Filtration: Boosting Retrieval-Augmented Generation Reranker to Query-Answer Tasks by Discrete Ricci Flow](https://arxiv.org/html/2606.15482v1) | 2026-06-16 | embedding近邻混入无关chunk → query/chunk图的curvatureflow过滤后再rerank → 需核结构community定理何时足以批准queryrelevance；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-RAG，[Books](../../../../books/part-07-agent/76-rag.md)；root§116实际POST |
| [Model Stealing Through the Lens of Model Multiplicity](https://arxiv.org/html/2606.15493v1) | 2026-06-16 | targetfidelity相近被误当部署可替代 → 同Rashomon surrogate集比较ambiguity/discrepancy与groupfairness差异 → 改变抽取模型的兼容/经济推断，不采医学应用结论；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Books](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root§105实际POST |
| [Selective Synergistic Learning for Video Object-Centric Learning](https://arxiv.org/html/2606.15527v1) | 2026-06-16 | encoder/decoder全patch对齐传播各自噪声且成对二次费 → encoder只供边界/decoder只供内部pseudo监督并transitive合slot → 改变两个表示读者的监督准入和冗余身份；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Books](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root§118实际POST通过 |
| [Track2View: 4D-Consistent Camera-Controlled Video Generation via Paired 3D Point Tracks](https://arxiv.org/html/2606.15534v1) | 2026-06-16 | perframepose/pointcloud不显式跨view跨time连续对应 → source/target配对3Dtracks与几何transfer/时间聚合 → 改变video viewpoint conditioning的可见对应；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§119实际POST通过 |
| [A Decision-Theoretic View of Test-Time Training: When, How Far, and Which Directions to Adapt](https://arxiv.org/html/2606.15569v1) | 2026-06-16 | 固定step/subspace在shift下会错配promptSNR → kernel/GP条件下spectralmatched更新、prompt evidence选步和方向 → 改变何时/多远/沿哪方向适配；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN，[Books](../../../../books/part-01-worldview/04-why-models-learn.md)；root§121实际POST通过 |
| [Schattor: Schatten-family methods for deep learning optimization](https://arxiv.org/html/2606.15702v1) | 2026-06-16 | matrix/vector混合和noise需不同geometry → Schattenfamily+matrix martingale stationarity、多block平衡 → 改变优化norm/参数块进展约束；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-PRETRAINING，[Books](../../../../books/part-04-training-system/28-pretraining.md)；root§124实际POST通过 |
| [SILAGE: Memory-Efficient, Full-Gradient-Free Nonconvex Optimization for Nested Finite Sums](https://arxiv.org/html/2606.15832v1) | 2026-06-16 | globalfullgradient refresh或perexample controlvariate状态昂贵 → 利用nested groups保O(n) state/单localgroup更新与两层heterogeneity界 → 改变datasetpartition/refresh人口和训练state成本；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)；root§127实际POST通过 |
| [Topological Flow Matching](https://arxiv.org/html/2606.15897v1) | 2026-06-16 | 欧氏reference忽略structured-domain连接 → Laplaciandrift改referenceprocess并保条件FM训练接口 → 改变生成路径/几何假设，不采用fMRI/海洋等暂缓科学应用；2 + 1 + 2 = 5 | 争议 | 暂缓：打印谱control与本节ODE/条件路径端点冲突，root§125中心隔离，重开见§4 |
| [On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents](https://arxiv.org/html/2606.15912v1) | 2026-06-16 | student多轮小错进入teacher不熟悉state → 同rollout按turn混teacher/student并将interventionprob退到0 → 改变采样state/撤指导的部署分布合同；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-SFT，[Books](../../../../books/part-04-training-system/29-sft.md)；root§94实际POST |
| [You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences](https://arxiv.org/html/2606.15956v1) | 2026-06-16 | augmentation/mask的最优强度随data改变 → 对照biasstrength×datascale，再用frameembedding+encodedmotion预测下一表示 → 改变表征inductivebias随预算条件；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Books](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root§129实际POST通过 |
| [Active Learning with Low-Rank Structure for Data Selection](https://arxiv.org/html/2606.16045v1) | 2026-06-16 | cluster几何不代表全局低秩结构 → residualsampling/rowsubset与带加性rankerror的losscoreset → 改变数据选择误差对象/权重条件；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-DATA，[Books](../../../../books/part-04-training-system/27-data.md)；root§131实际POST通过 |
| [EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video](https://arxiv.org/html/2606.16202v1) | 2026-06-16 | 每object逆物理优化昂贵/难迁移 → 将逆解蒸馏进codebook预测dense springstiffness，对未见物体免perspringTTO → 改变RGBworldmodel初始化与可识别物理参数权限；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Books](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)；root§103实际POST |
| [Training-free sparse attention based on cumulative energy filtering](https://arxiv.org/html/2606.16317v1) | 2026-06-16 | fixedTopk/Top-p只保预算或mass一侧 → 以recall目标动态threshold/融合FA执行 → 改变mask预算与保真代理的耦合；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Books](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；root§100实际POST |
| [What Should a Streaming Video Model Remember?](https://arxiv.org/html/2606.16353v1) | 2026-06-16 | indiscriminatehistory稀释当前scene → 原currentobs直供、history只受queryconditionedlatentbudget暴露，write/consolidate/retrieve分责 → 改变current原证据与压缩memory消费权限；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Books](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root§99实际POST |
| [Taylor-Calibrate: Principled Initialization for Hybrid Linear Attention Distillation](https://arxiv.org/html/2606.16429v1) | 2026-06-16 | copyteacher projections未定GDNdecay/write/outputdynamics → 用teacherattention统计定时标/gates/value并短layeralign → 改变hybrid转换初态与distill成本；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Books](../../../../books/part-02-model/22-long-context.md)；root§94实际POST |
| [ResEdit: Residual embeddings for precise generative image editing](https://arxiv.org/html/2606.16457v1) | 2026-06-16 | inversionnoise含冲突imagefeatures → 额外residualcondition补重建，并gradientreversal使其不携编辑condition → 改变identity保持与编辑通路的分责；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Books](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§103实际POST |
| [Robots that Collaborate: Sequential Asymmetric Imitation for Learning Coupled Robot Policies](https://arxiv.org/html/2606.16490v1) | 2026-06-16 | 两policy独立示教没见真实partner错相 → A与human学/B对deployedA学/再以失败附近介入修A → 改变合作策略curriculum的人口和耦合控制；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Books](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§99实际POST |
| [Direction-Conditioned Policies via Compositional Subgoal Scoring for Online Goal-Conditioned Reinforcement Learning](https://arxiv.org/html/2606.16515v1) | 2026-06-16 | rawgoal远离访问域使条件无几何信息 → train选visitedsubgoal/方向幅度actor，deploy换最终goal并移除score，明确controllablesubspace失效 → 改变goalconditioning与train/deploy支持条件；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Books](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§103实际POST |
| [Assessing Reliability of Symbol Detection in Concept Bottleneck Models](https://arxiv.org/html/2606.16535v1) | 2026-06-16 | CBM高taskaccuracy/同conceptvocab不保证语义兼容 → 独立detector/head互换与减concept监督的受控collapse，多head可靠性约束 → 改变解释符号的compatibility验收，不以新metric命名准入；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；04364完整两段后/07184前，root§90真实POST |
| [SCAR: Semantic Continuity-Aware Retrieval for Efficient Context Expansion in RAG](https://arxiv.org/html/2606.16661v1) | 2026-06-16 | parent/staticwindow多拿上下文、fixedthreshold不跨embedding标度 → relevance相对主chunk加continuitypenalty决定邻块扩展 → 改变扩展资格/近似scaleinvariance条件；2 + 1 + 2 = 5 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md)；11552后/00529前，root§91真实POST |
| [Decision-Weighted Flow Matching for Contextual Stochastic Optimization](https://arxiv.org/html/2606.16790v1) | 2026-06-16 | uniformfit误差不对应下游决策regret → endpoint决策权重改velocityregression/adjoint传输联系 → 改变generative训练loss人口与消费目标；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Books](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；root§133实际POST通过 |
| [Unified Motion-Action Modeling for Heterogeneous Robot Learning](https://arxiv.org/html/2606.16917v1) | 2026-06-16 | 异构动作/视频缺共同条件接口 → 3Dobjectmotion与robotaction共同maskedobjective，mask决定监督/部署模式 → 改变world/action目标的可消费角色；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Books](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；root§135实际POST通过 |
| [Probing Low Frame Rate Degradation in Neural Audio Codecs](https://arxiv.org/html/2606.16969v1) | 2026-06-16 | 6.25Hz质量cliff被归音素碰撞/codebooksaturation → controlledframerate下改trainingclip/context token支持后cliff消失 → 改变低帧率表示容量/训练人口的归因；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Books](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；root§86实际POST通过 |
| [Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models](https://arxiv.org/html/2606.16999v1) | 2026-06-16 | 选择/修复常被当免费超BoN → leakagefree/matchedcompute的26operators负结果与extractor/signature修复正对照 → 改变coverage、selection信号与expressionharness分责；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；pool覆盖/选择/harness表达三分责，root§87具体NC |
| [The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers](https://arxiv.org/html/2606.17037v1) | 2026-06-16 | 输入Fourierphase规律不自动说明hiddenidentity → hidden层跨样本phase/sign/magnitude干预，ReLU前后/DConly对照 → 改变readoutbasis与CNN/attention机制解释；2 + 1 + 2 = 5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Books](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)；root§94实际POST |
| [Adaptive and Explicit safe: Triggering Latent Safety Awareness in Large Reasoning Models](https://arxiv.org/html/2606.16808v1) | 2026-06-16 | P提案：初次unsafe回答与重读自己trace后的risk识别不同 → 从自身重呈现生成训练材料，显式safe tag在初始reasoning后触发安全分析，SFT后DPO保持该条件 → 可改变何时消费自生分析及训练/部署条件；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-SFT，[Books](../../../../books/part-04-training-system/29-sft.md)；root§99实际POST |

| [V2P-Manip: Learning Dexterous Manipulation from Monocular Human Videos](https://arxiv.org/html/2606.16436v1) | 2026-06-16 | 几何拟合不等接触可行 → 先仿真稳定资格、仅不稳定帧接触wrench修正 → 改变视频动作参考的修正条件；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[owner](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；24093后/20894前，root§76真实POST |
| [Redirecting the Flow: Image Customization through Attention Distribution Shift](https://arxiv.org/html/2606.16866v1) | 2026-06-16 | 多reference共享attention竞争损身份 → clean独立alignment后消费refKV，对照区分文本与身份 → 改变reference消费选择；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；24085后/DreamOmni2前，root§76真实POST |
| [TuneJury: An Open Metric for ImprovingMusic Generation Preference Alignment](https://arxiv.org/html/2606.17006v1) | 2026-06-16 | 新generator在训练cutoff外产生systembias → 固定RM拟anchor相对BToffset并分验跨月支持 → 改变局部校准与重训选择；2 + 1 + 2 = 5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；anchor维护后/合成anchor前，root§76真实POST |
| [Closed-Loop Triplet Synergistic Generation for Long-Form Video](https://arxiv.org/html/2606.16184v1) | 2026-06-16 | 同名entity不等当前appearance → state/view变化创建linkedentry并限制ref复用，postvideo回写改变下shot条件 → 改变合成记忆的版本资格；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[owner](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；12496后/35001前，root§76真实POST |

<!-- full-raw-recovered-candidate-rows:end -->

## 4. 证据与知识整合

### [DCP-Prune: Ultra-Low Token Pruning with Distribution Consistency Preservation](https://arxiv.org/html/2606.16633v1)

[必要§46](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)、root§78/79：删前semantic×spatial残差回灌与最终κ阈值触发重选分开；κ非严格divergence/语义保持，原inputpool未闭不补早丢信息自动恢复，相关不授唯一因果。保任务反退和895/884秒口径非单请求/全法最优，全部聚合/统计/原池驻留/聚类及下游费。原5具体缺口深入，[MULTIMODAL-REPRESENTATION Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)PCA15621后/TREN前真实一段/注实际POST通过。

### [AI Engram: In Search of Memory Traces in Artificial Intelligence](https://arxiv.org/html/2606.14997v1)

[必要§45](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)、root§77：Prop4.1硬reference约束与给出的软伪逆式不相容。取一维X+=X-=1、ΔW=1，式得W+=0.5却不满足W+X-=0，可行值只能0；数值复算非模型复现。保原文软filter解释但不改名为已证因果独立trace。原5/争议/暂缓，不入Books，不否定所有经验编辑；重开需可核修正/附加假设，或作者明定软目标并给相应保留/擦除验证。未读附件/实现不获正面采用。

### [The Faithfulness Gap: Certifying Semantic Equivalence Between Natural-Language and Formal Mathematical Statements](https://arxiv.org/html/2606.16541v1)

[必要§47](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)、root§77：Prop4.2 probe在等价关系下闭不保证包含N类或分离见证；只取恒真类时，两个不等价独立命题仍可同forward/backward指纹。Alg1当前只消费F→P，不补P→F，Unknown非反证。原5/争议/暂缓，中心certification不入Books；有限诊断不被全盘否定。重开需更正支持/分离假设、实际双向算法与标签/校准证据；未运行Lean/核实现，不将条件witness概率界当实际NL标签保证。

### [V2P-Manip: Learning Dexterous Manipulation from Monocular Human Videos](https://arxiv.org/html/2606.16436v1)

[必要§40](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)复用root§63有限决定域，§74/76：几何对齐后由固定仿真pose稳定资格决定哪些帧需要contact-wrench修正；不是全轨动力学、arm可达或真机安全。保rigid/floating-base支持与全部重建/优化/仿真/策略费。原5，[MULTIMODAL-EMBODIED-VLA Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)24093后/20894前一段及本人注实际POST过。

### [Redirecting the Flow: Image Customization through Attention Distribution Shift](https://arxiv.org/html/2606.16866v1)

[必要§41](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)复用§63，root§74/76：各clean reference独立形成层对齐条件再读KV，共享attention替换下文本与身份代理方向相反；不采max-entropy新定理、无污染/任意兼容。全部参考与完整采样付费。原5，[MULTIMODAL-GENERATIVE-PARADIGMS Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)24085后/当前DreamOmni2前真实一段/本人注POST过。

### [TuneJury: An Open Metric for ImprovingMusic Generation Preference Alignment](https://arxiv.org/html/2606.17006v1)

[必要§42](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)复用§63有限§6/D9/D11，root§74/76：冻结RM/encoder，对新generator拟anchor相对system BT offset；校准不修表示，同月/跨月人口与小K反退限制迁移。保标注/拟合/独立回归费，不授25倍普遍省费或任意新模型校准。原5，[PLATFORM-EVALUATION-SYSTEM Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)anchor维护后/合成anchor前实际一段/注POST过。

### [Closed-Loop Triplet Synergistic Generation for Long-Form Video](https://arxiv.org/html/2606.16184v1)

[必要§43](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)复用§63精确v1 CoTriSyGen非current EvoState，root§74/76：view/state/appearance变化建立linked entry并改变ref复用资格；关键帧前合成注册与视频后回写分producer。预算耗尽择最好非accept，合成memory不是真实观察，所有生成/检查/重试全付费。原6，[MULTIMODAL-GENERATIVE-PARADIGMS Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)12496后/当前35001诊断前真实一段/注POST过。

### [Spokes: Optimizing for Diverse Pretraining Data Selection](https://arxiv.org/html/2606.15216v1)

[必要§44](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)、root§75：质量与集合谱熵联合、连续权重后top-k是有限操作点，simplex非防集中/离散最优，proxy/JL overlap非全距谱保证；末层校准/评分截断与训练文档长度分开。保固定LLaMA1B/100Btoken、单任务反退与全部selector/预训费。原5/标准完成，[TRAIN-DATA Ch27](../../../../books/part-04-training-system/27-data.md)20644/06892/PGE/18361具体承载集合关系、联合质量及proxy实训验证，无同义新增。

### [Tyler: Typed Latent Reasoning for Language Models -- When to Think, What to Compute, and How Much to Allocate](https://arxiv.org/html/2606.16360v1)

[必要§36](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)、root§70/73：下一动作中的typed operator以不同query/projection调用共享synthesizer，不是可形式验证的角色语义；成功且超预算惩罚不是硬上限，调用位置复用轨迹advantage不是独立credit。保θ更新口径冲突、小模型/单run与计时排除及全部latent/生成费。原6，[MODEL-DECODER-ONLY Ch18](../../../../books/part-02-model/18-decoder-only.md)25745完整段后、新工作状态H3前一段/marker/本人注实际POST通过。

### [Towards Pareto-Optimal Tool-Integrated Agents with Pareto Ranking Policy Optimization](https://arxiv.org/html/2606.16111v1)

[必要§38](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)复用root§65，§72/73：scalar先取策略、后以组内非支配rank主导信用、同层有界细分。Archive成功最少调用仅观察参照，HV变化调scalar非学习目标权重向量，不授每目标单调/全局收敛，保全阶段/工具/rollout费。原5因具体差额深入，[TRAIN-GRPO Ch33](../../../../books/part-04-training-system/33-grpo.md)08545后/FGRPO前一段与本人注已实际POST。

### [A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization](https://arxiv.org/html/2606.16154v1)

[必要§39](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)复用root§66 officialPDF，§72/73：全组采样中心化后截零并保ratio/clip、全组与固定T分母，区别positive-set分支。连续奖励正项不等正确，近on-policy一阶非完整optimizer保证；保模型/低k反退及失败生成全费。原5因具体差额深入，[TRAIN-GRPO Ch33](../../../../books/part-04-training-system/33-grpo.md)06650后/negative-only前一段与本人注实际POST通过。

### [The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematical Reasoning](https://arxiv.org/html/2606.16152v1)

[必要§37](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)复用root§65首次必要，root§71实际owner核：同一约34k正确问题人口下，评分质量、润色与student SFT/DFT效用不是同一测量；保Table3非单调、3543配对参照人口、3–7B数学与全部teacher/筛选/训练费用。不采强teacher普遍有害或空格唯一因果。原5/标准完成，[TRAIN-SFT Ch29](../../../../books/part-04-training-system/29-sft.md)01702答案/模仿分责、08880未蒸馏基线/共同正确人口及23041教师降分而student改善已具体覆盖所采有限命题，不补同义正文，不声称已记录其独有RM/unigram实验。

### [Data Augmentations for Data-Constrained Language Model Pretraining](https://arxiv.org/html/2606.16246v1)

[必要§33](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§64/67：固定语料重复时改变输入—target对、部署恢复普通AR，噪声×offset并非天然协同；FIM非完全无改善，正文排名/组合总括不替表数。保单规模/不同选点及WSD续步、未额外near-dedup、NLL不等下游/净省费。原5，Ch28 06546后实际一段/两肩与本人注POST过。

### [RoboPIN: Grounded Embodied Reasoning via Pinned Chain-of-Thought](https://arxiv.org/html/2606.15753v1)

[必要§34](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§64/67：entityID/view/point推理引用及分项process奖励，不是外部tracker或物理真值；A3正确answer参与teacher生成，删泄漏措辞不认证独立推导。保无RFT/point/RealWorldQA反退、两任务各5真机和全部制备/控制费。原6，Ch26 VLMcontroller总论后实际一段/两肩与本人注POST过。

### [Latent Thought Flow: Efficient Latent Reasoning in Large Language Models](https://arxiv.org/html/2606.16222v1)

[必要§35](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§68/69：随机可变长latent、quality×长度utility的有限SubTB拟合；prefix即时停止答案评分和所有chain必须计费。有限训练不授精确后验/语义entropy阈值，Eq20不私补KL、prior单项反退保留。原5，Ch18 GLR后实际一段/两肩与本人注POST过。

### [Distilling Drifting Transformers with Representation Autoencoders](https://arxiv.org/html/2606.15553v1)

root§51唯一必要/[采用§30](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：RAE几何、flow初始化与realpositive/generatednegative分布target配对，不是沿旧ODE逐点蒸馏。保sphere非真实VAE定律、softmax/noise/正负batch反侧、detachednegative前向/RAE全费，不混后版数字。Ch24 TFD07327后/关系蒸馏前真实一段，root§56PRE/§58实际POST；原5，不授单步无损/净省费。

### [The Reservoir Attention Network: Cross-Pass State in Pretrained Transformers via Content-Addressable Reservoir Injection](https://arxiv.org/html/2606.15678v1)

root§52唯一必要/[采用§31](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：fixedrandomcore不等免训练，additive/prefix消费分验、wipe后carry/reset与emitmetric分开。保GRUcontrol、容量/量化/LR共因与silence分母误导、falsepositive及持续tick全费，不授TC0/agency/stockHF或生产。Ch22 LiveMem两完整段后/派生状态前一段，root§56PRE/§58实际POST；原5。

### [Learning New Tasks via Reusable Skills: Skill-Compositional Experts for Embodied Continual Learning](https://arxiv.org/html/2606.15685v1)

exact-v1 §3/4/T2–3/5必要与[采用§28](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：派生skill标签、execution单expert与transition densemixture分责，不是外部postcondition。保5replay/容量/标注共因、NBT非逐项最好、anchor漂移非唯一因果与少量真机/全费。Ch26 fastslow/replay第二完整段后/NestedVLA前一段，root§59PRE/§61实际POST；原6，不授免遗忘/安全。

### [LOCUS: Local Visual Cue Search for Enhancing Fine-Grained Perception in Multimodal Large Language Models](https://arxiv.org/html/2606.16586v1)

exact-v1 §3/4/T1–7/Limits/B/C/D7必要与[采用§29](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：训练crop定位IoU代理、部署仍普通全图。保blackcontext非唯一因果、textcue准确升但AIB降、tinyonly/部分OCR或MathVerse退步、teacher特权与训练/编码全费。Ch23 01914完整诊断后/同表layout前一段，root§59PRE/§61实际POST；原5，不授已看即懂或SLO。

### [KeepLoRA++: Continual Learning with Layer-Scaled Residual Gradient Adaptation](https://arxiv.org/html/2606.16256v1)

root§53唯一必要/[具体NC§32](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与§56actualowner通过。有限方向合同已由Ch30 TLoRA固定A/rowspace、supportselector/PALoRA保护代理、alpha与placement/optimizer分责的完整论点承载；不是本篇dualrecipe已证。Eq2/4/M右奇异维度/fullrank、GD不自动覆盖AdamW等强配方未闭，明确隔离，不采无干扰/免遗忘。原5标准完成/已有覆盖，无Book改动；重开需精确算法/实现与对应新旧任务证据，不以不可用的大截断HTML代原件或宣称外部H。

### [Scaling Short-Term Memory of Visuomotor Policies for Long-Horizon Tasks](https://arxiv.org/html/2606.16178v1)

精确v1 III-B/C、V-Q4/Q5、VI、IX/XI必要复用root§40，[采用§21](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。当前feature条件化postattention gate与static scalar/sink反侧有具体差额，summary压缩仍有损；29/42与28/45不同人口、86/90M非严同参，sharp非单调，不授伪相关唯一因果、长期Agent事实或SLO。Ch26首帧12730完整后段/marker后一段，root§45PRE/§46实际POST；未核代码/复现。

### [Wasserstein Convergence of ODE-Based Samplers in Decentralized Diffusion Model via Velocity Field Decomposition](https://arxiv.org/html/2606.15835v1)

唯一首次必要root§31/35，[actualowner/采用§20](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。当前state/time posterior抽localfield才给conditionalmean匹配，另有route方差；fixedδ参考ODE界与D1另给rawdata截断界分账，不将训练L2替全域误差或少分支授隐私/异步/净速。Ch24 15009完整两段/marker后真实一段，root§39PRE/§41实际POST。原5保留，未认证全部附录/精确headline或实现复现。

### [Diffusion Flow Matching: Dimension-Improved KL Bounds and Wasserstein Guarantees](https://arxiv.org/html/2606.16610v1)

root§31有限必要、[具体NC对照§19](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与§39独核：H1理想轨迹人口和H5生成轨迹误差不能互换，earlystop目标非原data，W2另有曲率/score/矩条件与大常数。Ch24 12597/12617实际训练/生成支持、19740 reference/学习/solver及09639指定population/metric条件完整论点已承载本次有限误差合同；不称已有本篇新维度率定理。原5标准完成/已有覆盖，无Book改动；精确新率/复杂度以后有明确采用需要才重开。

### [Qwen-RobotNav: A Scalable Navigation Model Designed for an Agentic Navigation System](https://qwenlm.github.io/blog/qwen-robotnav/)

只Jun16官方Blog完整core、API带offset原日期，root§38唯一必要/[采用§22](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。训练逐sample随机四轴观测条件，部署显式taskmode/预算/history接口；不授anyconfig/全SOTA，四轴未独立消融、planner与navigationmodel分责，编码/训练/采样/控制全费。Ch26 12129完整段/marker后真实一段，root§45PRE/§46实际POST；真实Paper链接恢复不冒PDF已审或代码复现。

### [Qwen-RobotManip: Alignment Unlocks Scale for Robotic Manipulation Foundation Models](https://qwenlm.github.io/blog/qwen-robotmanip/)

root§38唯一Blog有限必要/[采用§23](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。有效slot/mask、cameraframe与history本体条件分开；80D统一维度非语义/动力学兼容，context有反退、数据合成/配比/SFT共因，少量真机不授通用本体/安全或完整SLO。Ch26数据阶段完整‘后一步没有否定前一步’后/TerraTransfer++前一段，root§45PRE/§46实际POST；未读PDF/核代码/复现。

### [Selection Without Signal, Recovery Through Expression: A Measurement Study of Post-Hoc Falsification Operators for Frozen Small Code Models](https://arxiv.org/html/2606.16999v1)

[必要§53](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§87：共享frozenpool只支持coverage、selector信号与extract/harness表达三分责；有限负证非所有operator无效，M1 rename非模型语义新能力，matched调用非全费。Ch66 Pass@k/BoN、25503可恢复records/readout与20479 offset实际完整论点已承载，原5标准完成/已有覆盖，不写Book，不正面认证DNH/全部26operator或强零风险理论。

### [Beyond Accuracy: Measuring Bias Acknowledgment in Chain-of-Thought Reasoning for Responsible AI Evaluation](https://arxiv.org/html/2606.15127v1)

[必要§55](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§87：同500题三bias配对，S原对→新错、A书面rubric与A|S不同分母；19/18失败小人口、书面CoT非内部因果、matchednonbias缺口与全费保留。Ch66 28070/00476及oversight三项实际完整论点已承载trace承认与行为分验，原5标准完成/已有覆盖，无Book改动，不采TG命名为新因果。

### [FastMix: Fast Data Mixture Optimization via Gradient Descent](https://arxiv.org/html/2606.14971v1)

[必要§66](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§87：单proxy短步validation梯度调sourceweight，期望loss等价非有限SGD轨迹相等、Eq7非额外正则完整配方；工业proxy/长度与长反传/离散指标限制、全搜索训练费保留。Ch27 21492/BLISS06048完整局部方向、hypergradient/代理状态与独立实训已有覆盖，原6标准完成，不授跨尺度普效或全部倍率。

### [Assessing Reliability of Symbol Detection in Concept Bottleneck Models](https://arxiv.org/html/2606.16535v1)

[必要§56](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§88/90：同词表独立detector×冻结head交叉消费，弱监督合成collapse与完整CUB小swapdrop分域；head/dropout混杂、可靠性损任务、ensemble/置换非全因果、额外训练费均保留。Ch5 04364完整两段后/07184前原完整稿、marker/本人注和两肩实际POST通过，原5，不由同概念名批准任意兼容。

### [MVEB: Massive Video Embedding Benchmark](https://arxiv.org/html/2606.14958v1)

[本日必要原稿](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)及root§92–94：同clip音频消费须按labelproducer模态分层，跨组混杂/原生预算与全费保留。原分/Jun16归属不变；[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)限定一段与本人注已真实保存、完整自读并经sole实际POST通过，不授全表、实现或复现。

### [Rethinking Implicit Spatial Representation in Visuomotor Policy Learning](https://arxiv.org/html/2606.15232v1)

[本日必要原稿](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)及root§92–94：终层空间池化失细节与多stage消费分责，保ToolHang/实机无相对增益与全费。原分/Jun16归属不变；[MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)限定一段与本人注已真实保存、完整自读并经sole实际POST通过，不授全表、实现或复现。

### [On-Policy Distillation with Curriculum Turn-level Guidance for Multi-turn Agents](https://arxiv.org/html/2606.15912v1)

[本日必要原稿](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)及root§92–94：整turn实际producer决定KL方向，保mixedoccupancy非纯轨迹二项等价、partialscore/SR反向与全费。原分/Jun16归属不变；[TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md)限定一段与本人注已真实保存、完整自读并经sole实际POST通过，不授全表、实现或复现。

### [Taylor-Calibrate: Principled Initialization for Hybrid Linear Attention Distillation](https://arxiv.org/html/2606.16429v1)

[本日必要原稿](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)及root§92–94：复制projection不继承recurrent dynamics，统计初始化/局部对齐/整体恢复分验，保长ctx缺口与全费。原分/Jun16归属不变；[MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md)限定一段与本人注已真实保存、完整自读并经sole实际POST通过，不授全表、实现或复现。

### [The Importance of Phase in Neural Representations: An Internal Oppenheim-Lim Test of Image Classifiers](https://arxiv.org/html/2606.17037v1)

[本日必要原稿](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)及root§92–94：donor sign/phase须绑定坐标与实际reader，保ReLU/DC/CLS不可读支集及幅值反侧。原分/Jun16归属不变；[WORLDVIEW-REPRESENTATION](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)限定一段与本人注已真实保存、完整自读并经sole实际POST通过，不授全表、实现或复现。

### [GRASP: Gradient-Aligned Sequential Parameter Transfer for Memory-Efficient Multi-Source Learning](https://arxiv.org/html/2606.14900v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：梯度同向不授source参数位移下降；保scalar/group与零范数版本缺口、有限heuristic及全费。原分/Jun16归属不变；[TRAIN-LORA](../../../../books/part-04-training-system/30-lora.md)一段/marker/本人注已真实保存、完整自读，经root§98唯一实际POST通过，不认证完整实现或复现。

### [EgoPhys: Learning Generalizable Physics Models of Deformable Objects from Egocentric Video](https://arxiv.org/html/2606.16202v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：每对象粗anchor与共享state-conditioned stiffness correction分责，保localhelper/持出、post-anchor计时与openloop限制。原分/Jun16归属不变；[MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)一段/marker/本人注已真实保存、完整自读，经root§103唯一实际POST通过，不认证完整实现或复现。

### [Training-free sparse attention based on cumulative energy filtering](https://arxiv.org/html/2606.16317v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：tilemax–runningLSE仅逐项质量上界判门，保block/累积与重归一反例、已付QK探测及全费。原分/Jun16归属不变；[INFER-TENSORRT-LLM](../../../../books/part-05-inference-system/49-tensorrt-llm.md)一段/marker/本人注已真实保存、完整自读，经root§100唯一实际POST通过，不认证完整实现或复现。

### [What Should a Streaming Video Model Remember?](https://arxiv.org/html/2606.16353v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：当前原visual独立于派生latent历史，N/B/M三预算与reader校准分账，保Recall非内容和全费。原分/Jun16归属不变；[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)一段/marker/本人注已真实保存、完整自读，经root§99唯一实际POST通过，不认证完整实现或复现。

### [ResEdit: Residual embeddings for precise generative image editing](https://arxiv.org/html/2606.16457v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：反演前逐图残余/probe与可编辑空间condition分责，保先适配、probe非独立证书和完整优化采样费。原分/Jun16归属不变；[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)一段/marker/本人注已真实保存、完整自读，经root§103唯一实际POST通过，不认证完整实现或复现。

### [Robots that Collaborate: Sequential Asymmetric Imitation for Learning Coupled Robot Policies](https://arxiv.org/html/2606.16490v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：部署伙伴诱导人口与A-centric纠正分账，保更新A再改B人口、targeted片段与真实控制分母/全费。原分/Jun16归属不变；[MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)一段/marker/本人注已真实保存、完整自读，经root§99唯一实际POST通过，不认证完整实现或复现。

### [Direction-Conditioned Policies via Compositional Subgoal Scoring for Online Goal-Conditioned Reinforcement Learning](https://arxiv.org/html/2606.16515v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：visitedsubgoal训练/方向距离接口/部署最终goal交接，保onpath非选器保证、方向非距离动作等价与全费。原分/Jun16归属不变；[MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)一段/marker/本人注已真实保存、完整自读，经root§103唯一实际POST通过，不认证完整实现或复现。

### [Adaptive and Explicit safe: Triggering Latent Safety Awareness in Large Reasoning Models](https://arxiv.org/html/2606.16808v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：保原think1接safe/newanswer2而舍二次重推理；选择性监督非外部再提示/硬门，保safe-only人口/反退与全费。原分/Jun16归属不变；[TRAIN-SFT](../../../../books/part-04-training-system/29-sft.md)一段/marker/本人注已真实保存、完整自读，经root§99唯一实际POST通过，不认证完整实现或复现。

### [Relational Structural Causal Models](https://arxiv.org/html/2606.14892v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：跨关系父域/聚合与混杂支持，OR/XOR反例限定无条件any，有限maxmin非证书。原分/Jun16归属不变；[MULTIMODAL-WORLD-MODELS](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)一段/marker/本人注已真实保存、完整自读，经root§106唯一实际POST通过，不认证完整实现或复现。

### [Simplifying the Modeling of Arbitrary Conditionals in Natural Language](https://arxiv.org/html/2606.14943v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：合法future条件副本与原LTR隔离，保跨层泄漏、singlepass评价非生成和joint非保证。原分/Jun16归属不变；[MODEL-DECODER-ONLY](../../../../books/part-02-model/18-decoder-only.md)一段/marker/本人注已真实保存、完整自读，经root§105唯一实际POST通过，不认证完整实现或复现。

### [AdaMame: A Training Recipe for Adaptive Multilingual Reasoning](https://arxiv.org/html/2606.15080v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：正确性门控query-language预定倍率与全组mean，非反馈或硬约束，保β正确率反侧和全费。原分/Jun16归属不变；[TRAIN-GRPO](../../../../books/part-04-training-system/33-grpo.md)一段/marker/本人注已真实保存、完整自读，经root§105唯一实际POST通过，不认证完整实现或复现。

### [Upper Bounds on the Generalization Error of Deep Learning Models via Local Robustness and Stability](https://arxiv.org/html/2606.16883v1)

[必要§78](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§107：条件风险分解缺人口质量、总体条件权重不可直接替训练计数；近零stable残差不能删除后仍称精确上界，原数值反例已独核。原5保留，中心界争议隔离，不进Books/不作正面generalization证据，也不否定全部经验诊断。重开只需精确修订分解与缺失权重/采样或集中项、保非零残差并核其对拟采用bound的影响；不要求复读所有附件或代码。

### [Representation Costs in Data Science: Foundations and the Quasi-Banach Spaces of Deep Neural Networks](https://arxiv.org/html/2606.14954v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：等价参数化inf/闭包、非biascost的2/L齐次与函数几何，保最优存在非SGD可达。原分/Jun16归属不变；[WORLDVIEW-WHY-MODELS-LEARN](../../../../books/part-01-worldview/04-why-models-learn.md)一段/marker/本人注已真实保存、完整自读，经root§106唯一实际POST通过，不认证完整实现或复现。

### [Model Stealing Through the Lens of Model Multiplicity](https://arxiv.org/html/2606.15493v1)

[本日有限必要与具体owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：固定合格模型家族后，两种max/平均次序不同，dropout邻域非独立训练/完整枚举。原分/Jun16归属不变；[PLATFORM-EVALUATION-SYSTEM](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)一段/marker/本人注已真实保存、完整自读，经root§105唯一实际POST通过，不认证完整实现或复现。

### [Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale](https://arxiv.org/html/2606.15079v1)

[有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：静态Norm校准不是逐输入RMS等价，转换与warmup/CPT分责，保PPL反侧/公开mask未闭和全费。原分/Jun16归属不变；[MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md)原三件真实保存、完整自读，经root§109唯一实际POST通过，不授完整实现/复现。

### [Sensor-Conditioned Representation Learning via Scene-Relevant Observation Quotients](https://arxiv.org/html/2606.16210v1)

[有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：声明sensor/C/noise可分对再分scene/nuisance；oracle标签/阈值非exact商，真实仅raw重构不授商结构。原分/Jun16归属不变；[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)原三件真实保存、完整自读，经root§109唯一实际POST通过，不授完整实现/复现。

### [FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing](https://arxiv.org/html/2606.15186v1)

[必要§82](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§110：音频反演/sourceKV与早期mask/noise、末段释放仅有限编辑条件；targetQ及最终全局协调不授未编辑输出严格相等，同NFE/听评也有反退。[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)15533早窗保留→后段撤、21466条件/输出分责及17097/05256/21818音频再生与逐流preservation已具体覆盖所采机制。原5标准完成/已有覆盖，无Book改动，不称现文有本篇KV公式或已听demo/复现。

### [Can Neural Networks Achieve Optimal Computational-statistical Tradeoff? An Analysis on Single-Index Model](https://arxiv.org/html/2606.15219v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：label/oracle改造与多随机权重探针改变梯度信息；SQ检测非普通SGD/预测全最优。原分/Jun16归属不变；[WORLDVIEW-WHY-MODELS-LEARN](../../../../books/part-01-worldview/04-why-models-learn.md)原三件真实保存/完整自读，经root§116唯一实际POST通过，不认证完整实现或复现。

### [An Integrable Token Mixing Layer from the Generalized Yang Baxter Equation](https://arxiv.org/html/2606.15085v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：同K正交路径/固定总s换序不授全MLP/residual或免费anytime。原分/Jun16归属不变；[MODEL-TRANSFORMER-LAYER](../../../../books/part-02-model/17-transformer-layer.md)原三件真实保存/完整自读，经root§111唯一实际POST通过，不认证完整实现或复现。

### [GeoStream: Toward Precise Camera Controlled Streaming Video Generation](https://arxiv.org/html/2606.15162v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：自产frame→depth→reprojection双反馈与短cache替换，不等真实世界或全部漂移消失。原分/Jun16归属不变；[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)原三件真实保存/完整自读，经root§111唯一实际POST通过，不认证完整实现或复现。

### [StarOR: Synergizing Tree Search and Test-Time Reinforcement Learning for Optimization Modeling](https://arxiv.org/html/2606.15197v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：sameprefix补全反馈更新实例transientgenerator，tree值/参数状态分账，补全非因果credit。原分/Jun16归属不变；[AGENT-PLANNING](../../../../books/part-07-agent/79-planning.md)原三件真实保存/完整自读，经root§116唯一实际POST通过，不认证完整实现或复现。

### [When to use what Schatten-$p$ norm in deep learning?](https://arxiv.org/html/2606.15268v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：有限p>2几何与dualnoise/radius/budget分责；凸上界非LLM赢家或切换recipe。原分/Jun16归属不变；[TRAIN-PRETRAINING](../../../../books/part-04-training-system/28-pretraining.md)原三件真实保存/完整自读，经root§116唯一实际POST通过，不认证完整实现或复现。

### [Ricci-Filtration: Boosting Retrieval-Augmented Generation Reranker to Query-Answer Tasks by Discrete Ricci Flow](https://arxiv.org/html/2606.15482v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：candidategraph有限flow预过滤→原reranker；理想图非relevance/少候选非净省费。原分/Jun16归属不变；[AGENT-RAG](../../../../books/part-07-agent/76-rag.md)原三件真实保存/完整自读，经root§116唯一实际POST通过，不认证完整实现或复现。

### [SCAR: Semantic Continuity-Aware Retrieval for Efficient Context Expansion in RAG](https://arxiv.org/html/2606.16661v1)

[必要§54](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§89/91：邻块query相关、对主块连续性罚与相对主块门槛分责，非相邻即可信。保非零罚非普遍scaleinvariance、弱主块低门槛、召回反退/续行与非相邻缺口、有限人工人口及全费。Ch76 11552独立marker后/00529前完整一段、本人注与两完整肩实际POST过，原5，不授zero-regret或生产SLO。

### [PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/html/2606.16449v1)

[必要§50](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)，root§82/84：RGB/depth按global/local edit不同失效，pose/time/globalversion/footprint约束检索；depth自产与纯外观/区域前提不是现实证据。保RGB-only同时改modality/filter的混杂、global画质反侧、增长archive与全部训练/编辑费。Ch24 22622后/当前33589前完整一段及本人注实际POST过，原6，不授constantmemory或SLO。

### [FARM: Find Anything using Relational Spatial Memory](https://arxiv.org/html/2606.15476v1)

[必要§51](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)，root§83/86：语言编query、softgeometry binding、topview VLM分工，target-anchor star限制与anchor-anchor未支持；rerank不补召回、各embedding/任务反侧、几何/异步caption新鲜度与全费。Ch26 17351完整两段后/2510.01519前真实一段及本人注POST过，原6，不授逻辑完备、物理安全或建图帧率等同全链SLO。

### [Probing Low Frame Rate Degradation in Neural Audio Codecs](https://arxiv.org/html/2606.16969v1)

[必要§52](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)，root§85/86：固定秒窗在低rate仅余少量latent，改固定K训练对cliff归因是关键控制；rate同时改bitrate、延长waveform/曝光与等iterations非等compute、码本利用率非全部容量与残余质量损失均保留。Ch23 10934第二完整caveat后/07185前真实一段及本人注POST过，原5，不授无限低rate无损、唯一decoder因果或生成净速。

### [PACT: Privileged Trace Co-Training for Multi-Turn Tool-Use Agents](https://arxiv.org/html/2606.16215v1)

[必要§48](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§80/81：prompt-only rollout与privileged-context ratio优化分责，v1 Eq13–14已有prompt-only anchor，不倒填后版。保改条件surrogate非原目标无偏、toolresponse只context、semanticprefix与完整call退火、q/任务反侧和teacher/全费，不采latentjoint已实现或执行许可。Ch33 peer15576后/PromptRobustness前完整段、marker/本人注及两肩真实POST过，原6。

### [HiMPO: Hindsight-Informed Memory Policy Optimization for Less-Entangled Credit in Long-Horizon Agents](https://arxiv.org/html/2606.16285v1)

[必要§49](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§80/81：同prewrite context替换old/new memory槽，目标答案平均loglikelihood与hindsight boundedfilter，辅助只作用memoryspan；v1 Eq5实际明确，不从v3倒填。保sibling历史不同、sigmoid非硬gate/绝对放大、successmask非真实credit、三次评分与复训/计时波动全费。Ch77 MemPO00680后/03329前完整段、marker/本人注及两肩真实POST过，原5，不授事实/永久删除或完整causal证明。

### [Localizing Credit at the Divergence: Path-Conditioned Self-Distillation for LLM Reasoning](https://arxiv.org/html/2606.15576v1)

root§42唯一必要/[采用§24](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。同当前group成功peer仅进teachercontext，对原student rollout按KL(T||S)评分；acceptedpeer非逐步真值、firstdiv非语义错误、无peer hardtail和onesample不稳，长teacher/fullvocab全费。Ch33 05787完整两段后/PromptRobustness前真实一段，root§48PRE/§49实际POST；不采理想teacher、普遍无偏或免费信用。

### [Beyond Layer Importance in Layer-wise Sparsity: An Inter-Layer Perturbation-Absorption Perspective](https://arxiv.org/html/2606.15161v1)

root§43唯一必要/[采用§25](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。固定方向的幅度扫与后层相对范数/cosine区别微扰和实际剪枝量级；baseprofile修正/重预算和搜索付费，分母变化/非线性因果未隔离、PPL或accuracy仍有反退，不授语义修复/manifold或kernel净速。Ch49 LayerwiseErrorAttribution完整段后/Distribution-conditioned前一段，root§48PRE/§49实际POST。

### [CacheMuon: Using Temporal Preconditioning To Approximate Polar Factor](https://arxiv.org/html/2606.16371v1)

root§44唯一必要/[采用§26](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。复用累计lefttransform仍乘当前momentum，probe非Gramstaleness/理论条件证明；miss/refresh和hostdevice同步全费，FLOPs不等墙钟，激进阈值伤质量。Ch28 19619完整end后/SignStep H4前一段，root§48PRE/§49实际POST；原5，不认证精确新率/未测devicefusion或实现复现。

### [MoECa: Aligning Feature Reuse with Expert Decomposition in Diffusion Transformers](https://arxiv.org/html/2606.15615v1)

精确v1 §3/4/5.1–3/8.2–4必要/[采用§27](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。当前router按expertidentity匹配branch，未匹配重算；部分MoE/attention协调非全网同步，weightdrift/EMA熵只proxy。tau0文字与阈值式反向、L40显存与latency分母未闭，不照录完整recipe/倍率。保部分质量退步、路由/匹配/统计/驻留/全生成费；Ch24 24195完整第二段后/10312空间传播前一段，root§54PRE/§55实际POST，原6不改。

### [Semantic DLM+: Improving Diffusion Language Models through Bias-variance Trade-off in Transition Kernel Design](https://arxiv.org/html/2606.15327v1)

精确v1必要见[本轮必要§6](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。只采semantic basin、global support与两种频率反馈分责；保entropy筛选、混baseline、数值反退和训练/采样共因，不采用KL/几何排序或普遍contraction。Ch24 LUDI完整两段后/binary前真实一段，root§16PRE/§21实际POST通过。

### [VLALeaks: Membership Inference Attacks against Vision-Language-Action Models](https://arxiv.org/html/2606.15165v1)

精确v1 III–V/VI及有限split决定点见[必要§7](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。白盒分区attention统计+有标签RF/MLP仅是有限监督sensor；frame/CV人口不授heldout trajectory或训练记忆唯一因果，DP/去重失效缺合同，均不正面采用。Ch72实际VLA trajectory-unit与监督logit-sensor两完整段足承载权限、matchedcontrol/Unknown与全费；root§18标准完成/具体已有覆盖，不改Book，不将当前code冒v1已证bug。

### [Adaptive Inference-Time Scaling via Early-Step Latent Verification for Image Editing](https://arxiv.org/html/2606.15188v1)

精确v1 III/Alg1、IV必要见[§8](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。早clean-latent与source方向差生成mask、空mask先拒，仍需原图叠mask的judge及K个完整终态图；预算耗尽不保证质量。保joint instruction共因、质量反退、平均NFE非最坏与全部judge/API费用。Ch24 30043 probe后/11564前实际一段，root§17PRE/§21POST通过。

### [Inference-time Policy Steering via Vision and Touch](https://arxiv.org/html/2606.14981v1)

精确v1 §3–6/B/Alg1/D3见[必要§9](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。先长程decoded视觉选anchor，再短前缀预测触觉gradient edit；不是最新真实触觉residual。保phase/worldmodel误差、anchor非硬mode保持、视觉decode全费、三任务有限trial/非同compute与均值非SLO。Ch26 T-WLA后/Chronos前实际一段，root§19PRE/§21POST通过。

### [Cascaded Sparse Autoencoders Learn Multi-Level Visual Concepts in Multimodal LLMs](https://arxiv.org/html/2606.16193v1)

精确v1 §3/5/A/E必要见[§12](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。二级重构一级decoder atoms并joint反传，不是sample code再压；只支持有限抽象接口/局部steering，不采真实语义本体或全stack失败。保HMS主文/附录口径、activegroup选择、随机单atom非完整匹配、targetSG仍有inputgradient、一级质量与全费。Ch5 meta-SAE03436后/nullbaseline前一段，root§27PRE/§29POST通过。

### [Robots as Tokens: Unified Diffusion Transformer for Coordinated Multi-Robot Trajectory Generation](https://arxiv.org/html/2606.15550v1)

唯一必要首备直接复用root§20/22，[actualowner与原稿§11](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)。joint robot-chunk/known trajectory条件与训练地图head有具体接口贡献；occupancy改善不授waypoint单调，2D/最多10pad、小感知失败、safetyshield和全部去噪费用保留。Ch26 DG-MAP完整段/marker后、VLA-Fabric前一段，root§25PRE/§26实际POST通过；未重复Methods或补未核padding实现。

### [Understanding Cross-Modal Contributions in Continual Vision-Language Models: A Theoretical Perspective](https://arxiv.org/html/2606.14883v1)

[必要§10](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)仅核CBF中心：Def4.7无非平凡预算，闭域all-one最大、开域一般仅sup，零梯度未定义；Th4.11/Eq35–43没有修复同域argmax/平均可行性。root§15争议/暂缓安全终态，原5保留，不入Book或作正面理论；不扩大为全文错误或由经验指标补证明，精确重开见§5。

### [Predicting model behavior before release by simulating deployment](https://openai.com/index/deployment-simulation/)

只Jun16官方Blog，不把July论文迁日。唯一必要首备root§24，[本轮采用§13](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：旧prefix重采一个响应，同model真/模拟fidelity与发布后prefix人口变化分账。保tail/CoT前提与只读工具模拟非liveeffect，近chance不证明等价。Ch66代表性完整段后/人口权重段前真实一段，root§28PRE/§30实际POST通过。

### [Shift-and-Sum Quantization for Visual Autoregressive Models](https://arxiv.org/html/2606.16131v1)

精确v1 §3–4/Eq6–20/T1–4、AppA–E/H/I必要范围，[完整边界与实际owner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md#5-260616131v1-shift-and-sum--必要完成pre待root)。只采用Value对称移位副本/同格式额外工作与calibration边际分责；AppC无限网格界不授有限clip/整网，低相关不证明独立。保4/6、4/8质量反退和W8A8真CPU低于BRECQ，不从BOP或8bit运行推4bit/完整服务收益。原5分因具体补偿执行差额深入；Ch49 ARCQuant完整机制及caveat之后补一自然段，root§13 PRE→真实SAVE→§14实际完整POST通过。未核代码/复现。

### [Adaptive inference and function vectors in deep transformers](https://arxiv.org/html/2606.16694v1)

精确v1 §II/III与VI.1及必要公式，原6因具体长期gap深入；[必要证据](../_sources/daily-20260617/SUP_NECESSARY_20261026.md#2-260616694v1-adaptive-inference--必要完成pre待root)。固定M=dL通信预算的受限linear-attention回归中，已有function-vector统计决定下一测量：Gaussian与层级tree prior呈不同深度价值。保同带噪统计、大样本、受限非adaptive搜索与非同FLOPs条件；8seed与key patch不授生产softmax LLM的Bayes最优或加速。Ch17旧optimizer解释及caveat完整保留后补两自然段，root§6PRE→真实SAVE→§7实际完整POST通过；不重审未变层。

### [Generated, Parallel, Scalable? A Study of Agentic AI-Generated Julia Code on Supercomputers](https://arxiv.org/html/2606.16534v1)

root作为本日唯一nonwriter首读v1 §3–6并完成actualowner比较，[§8必要与具体NC](../_sources/daily-20260617/SUP_REVIEW_20261026.md#8-16534-juliahpc-必要首备与具体已有覆盖)。只取小输入/自生成harness通过不保证目标规模的反例；每配置一次generation、五次运行重复不是独立生成统计，不能把所有失败唯一归因LLM或并行框架。Ch66已有kernel benchmark的shape/runtime与四verdict、配置迁移、失败回执及隐藏配置分责，足承载这个有限证据，不声称已写完整Julia实现。标准完成，已有覆盖，无Book修改/POST。

### [Learned Image Compression for Vision-Language-Action Models（SPARC）](https://arxiv.org/html/2606.16253v1)

采用精确v1 §3–5/Eq2–5/Table1、§7和AppA/C–F必要范围，不采用后来版本或摘要数字。[完整必要判断及书稿位置](../_sources/daily-20260617/SUP_NECESSARY_20261026.md#1-260616253v1-sparc--必要完成pre待root)。它把动作质量约束前移到视觉通信codec：发送稀疏latent+hyperlatent、对端按selector/history重建mask，幂次重权局部熵代价以缓和稀有动作关键细节的训练删除压力。该proxy不是实际码长或安全保证；单seed、codec部件时延、无language grounding、极差链路未测和精细操作收益较小限制外推。Ch26原有内部token动作敏感性论证尚未承载这个带对端状态的wire-codec分支，已在其JND段后、平均动作偏差不保证物理安全段前实际写入一自然段，并保留成本/回退。未核代码或复现；root§4实际POST已通过。

### [The Price of Anarchy in Disaggregated Inference](https://arxiv.org/html/2606.17081v1)

**2606.17081 — The Price of Anarchy in Disaggregated Inference**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：PD disaggregation controller应联合感知P/D pool、hierarchical KV cache与routing congestion的externality，并在saturation knee后切换cache affinity/load balance。

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17081v1 §§3–6 coupled games, PoA estimator and adaptive controller`；evaluation locator 为 `arXiv:2606.17081v1 §§7–8 three-node B200 Dynamo evaluation`；counterevidence locator 为 `arXiv:2606.17081v1 §9.2 analytical-only P/D game; topology/model/grid-point limitations`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** controller以13% throughput换饱和期PoA/尾延迟改善；证据仅3-node B200、两模型与特定P:D topology，不是通用阈值。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17081v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-PD-DISAGGREGATION` owner 为 [books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。Review notes 前正文 `从静态 Pool Ratio 到耦合的 SLO Control State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work](https://arxiv.org/html/2606.17099v1)

**2606.17099 — Software Delegation Contracts: Measuring Reviewability in AI Coding-Agent Work**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：software delegation contract应把task、bounded authority、returned evidence bundle与acceptance context作为reviewable work package，而非只看hidden tests通过。

**State / data / control owner。** `AGENT-WORKFLOW` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17099v1 §§3–4 contract conditions and review protocol`；evaluation locator 为 `arXiv:2606.17099v1 §5 64-run/192-review pilot`；counterevidence locator 为 `arXiv:2606.17099v1 §6 limitations and small TypeScript/model-reviewer scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 显式contract以13% tokens和38% wall time换reviewability；pilot不证明correctness提升。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17099v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Handoff 必须保留约束的 Action-binding Strength`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators](https://arxiv.org/html/2606.17104v1)

**2606.17104 — Prefill/Decode-Aware Evaluation of LLM Inference on Emerging AI Accelerators**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：accelerator evaluation必须拆开Prefill TTFT与Decode TPOT/throughput，并把batch/network条件带入heterogeneous PD placement决策。

**State / data / control owner。** `INFER-PD-DISAGGREGATION` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17104v1 §§3–4 phase-aware cross-accelerator methodology`；evaluation locator 为 `arXiv:2606.17104v1 §5 Llama2-7B GPU/Groq evaluation`；counterevidence locator 为 `arXiv:2606.17104v1 §6 limitations and common-model/unsupported-batching/network scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 单模型与特定accelerator不构成采购排名；decode低TPOT可在batch throughput下反转。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17104v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-PD-DISAGGREGATION` owner 为 [books/part-05-inference-system/55-pd-disaggregation.md](../../../../books/part-05-inference-system/55-pd-disaggregation.md)。Review notes 前命题级锚点为 `局部加速必须通过完整部署账本`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Models Take Notes at Prefill: KV Cache Can Be Editable and Composable](https://arxiv.org/html/2606.17107v1)

**2606.17107 — Models Take Notes at Prefill: KV Cache Can Be Editable and Composable**

**问题、旧路径与机制。** 旧路径在输入、workload 与 trust boundary 稳定时仍合理；该 exact-v1 改变的是：KV cache应被视为prefill写入的memoized downstream conclusions；edit需append erratum，compose需RoPE reposition与identity-compatible splice。

**State / data / control owner。** `INFER-KV-CACHE` 持有该机制的 authoritative state 与 control decision；论文项目名不取得跨章节 owner。跨 owner handoff 必须绑定 identity、version、failure 与 fallback semantics。

**Evaluation：proof / non-proof。** Method locator 为 `arXiv:2606.17107v1 §§3–5 causal note model, editing and composition`；evaluation locator 为 `arXiv:2606.17107v1 §6 twelve-model/vLLM evaluation`；counterevidence locator 为 `arXiv:2606.17107v1 §7 limitations and CoT/model/layout/cache-compatibility scope`。证据只支持作者披露的 workload/model/hardware/metric，不证明生产 SLO 或跨模型、跨硬件普遍优越。

**Trade-off / failure / coexistence / evolution。** 无CoT edit可能被忽略，splice依赖model/layout/position identity；高hit与latency结果不证明任意context可安全改写。


**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.17107v1` 的 exact-v1 正文与本 report benchmark contract；later version/artifact 不参与本结论，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `双向更新会撤销“共享 Prefix 永远不可变”的前提`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs](https://arxiv.org/html/2606.17110v1)

**2606.17110 — Loss Landscape Poisoning: Targeted Extraction of Unseen Training Data from LLMs**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：攻击者可通过 loss-landscape poisoning 使后续 fine-tuning 提取未见训练数据；data provenance 与 update admission 必须联合审计。

**State / data / control owner。** `PLATFORM-SECURITY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17110v1 §2 Assumptions and Threat Models; §3 LLP Attack Principles`；`arXiv:2606.17110v1 §§4–7 direct-model, federated, data-poisoning and DP-evasion evaluations`；counterevidence `arXiv:2606.17110v1 Appendix C Defenses Against Poisoning Attacks in FL; threat-model scope in §2`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** LLP 展示特定 poisoning 可诱导未见数据提取，不证明任意微调都会泄漏；provenance/admission 增加训练摩擦，可疑 update 应隔离并回退可信 checkpoint。


仅使用 `https://arxiv.org/html/2606.17110v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `模型内部路由、训练数据与 Weight Repair 都进入攻击面`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations](https://arxiv.org/html/2606.17122v1)

**2606.17122 — TrustErase: Auditable Instant Machine Unlearning with Passport-Embedded Representations**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：instant unlearning 可把 passport 嵌入 LoRA 表示并以 authority-mediated verification 验证配置，但 deactivate credential 不自动证明所有信息删除。

**State / data / control owner。** `TRAIN-DATA` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17122v1 §3 Method (§3.2 auditable unlearning; §3.3 passport composition; §3.4 verification/tolerance)`；`arXiv:2606.17122v1 §4 Experiments (§4.1 setup/metrics; §4.2 single/multi-class); Appendices D–H`；counterevidence `arXiv:2606.17122v1 §5 Discussion (§5.1 Scope and limitations); Appendix B.2 scaling limits; Appendix H reconstruction attack`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** passport 验证只证明配置/凭证状态，不等价于所有信息已从 backbone 删除；hypernetwork 与密钥管理增加复杂度，重构攻击或 retain gate 失败时回退重训/隔离。


仅使用 `https://arxiv.org/html/2606.17122v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `TRAIN-DATA` owner 为 [books/part-04-training-system/27-data.md](../../../../books/part-04-training-system/27-data.md)。Review notes 前正文 `另一分支把可撤销表示封装在带 passport 的 adapter / LoRA 中` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems](https://arxiv.org/html/2606.17182v1)

**2606.17182 — Verified Detection and Prevention of Concurrency Anomalies in Multi-Agent Large Language Model Systems**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：并发 MAS 需要显式 happens-before、shared-state conflict 与 side-effect serialization，并在运行前后验证 anomaly-free execution。

**State / data / control owner。** `AGENT-MULTI-AGENT` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17182v1 §II Runtime Model; §III Anomaly Catalog; §IV Consistency Lattice; verified runtime sections`；`arXiv:2606.17182v1 formal witnesses, TLAPS checks and Verus spec/runtime refinement in §§III–IV; implementation/evaluation appendices`；counterevidence `arXiv:2606.17182v1 §II-B simplifying assumptions; §III-D split-view outside single-store model; realizability frontier §IV-C`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 形式化 detector 只覆盖论文 single-store runtime 与列出的 anomaly，不证明 split-view 等外部一致性；序列化牺牲并行度，模型假设不成立时回退单写者或事务存储。


仅使用 `https://arxiv.org/html/2606.17182v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前命题级锚点为 `声明式协议约束 Transition，而不是相信参与者会协调`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [MemTrace: Probing What Final Accuracy Misses in Long-Term Memory](https://arxiv.org/html/2606.17328v1)

**2606.17328 — MemTrace: Probing What Final Accuracy Misses in Long-Term Memory**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：long-term memory 评价应在 final accuracy 之外对 construction/retrieval/injection 节点做 counterfactual attribution。

**State / data / control owner。** `AGENT-MEMORY` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17328v1 §3 MemTrace (§3.1 data; §3.2 probes; §3.3 metrics; §3.4 diagnostic views)`；`arXiv:2606.17328v1 §4 Experiment and Findings (§4.1–4.5 maintenance, evidence conflict and failure attribution)`；counterevidence `arXiv:2606.17328v1 Appendix C Failure-Origin Checks; Appendix D judge reliability; Appendix E sensitivity`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** MemTrace 的 retrieval-versus-use 归因已由 Ch77 现有 memory pipeline counterfactual owner 覆盖，不证明 judge 与接口敏感性已经消失；因此回退既有 owner，本次 No Change 而非重复写入。


仅使用 `https://arxiv.org/html/2606.17328v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `用干预矩阵定位写入、检索与阅读失败`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [RISE: Relay Inference and Online Scheduling for Efficient Edge-Device Collaborative Diffusion Model Services](https://arxiv.org/html/2606.17378v1)

**2606.17378 — RISE: Relay Inference and Online Scheduling for Efficient Edge-Device Collaborative Diffusion Model Services**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：edge collaborative diffusion serving 需要 relay placement、partial denoising state 与 online queue/SLO scheduler 共同决策。

**State / data / control owner。** `INFER-SCHEDULING` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17378v1 §III Proposed Methodology (§III-A motivation; §III-B relay); §IV Algorithm Design (§IV-A–C formulation, LinUCB and reward)`；`arXiv:2606.17378v1 §V Experiment (§V-A setup; §V-B relay; §V-C sensitivity; §V-D scheduling; §V-E ablation)`；counterevidence `arXiv:2606.17378v1 §V-C parameter sensitivity; §V-E ablation; §VI Conclusion`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** RISE 的 relay/scheduler 收益只绑定所测 diffusion、设备和 network，不证明其他链路同样获益；partial denoising state 迁移失败会同时伤质量和 SLO，回退本地完整推理或静态 placement。


仅使用 `https://arxiv.org/html/2606.17378v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前正文 `迭代生成与流式会话需要显式 Progress State` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation](https://arxiv.org/html/2606.17383v1)

**2606.17383 — Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation**

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：Agentic AI model validation 应分别检查 belief-state filter、forecast transition 与 policy action，并以 POMDP identity 绑定三层误差。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.17383v1 §2 POMDP Representation; §3 Validation Framework (§3.1 belief; §3.2 forecast; §3.3 policy; §3.4 utility)`；`arXiv:2606.17383v1 §5 Portfolio Case Study; §6 Empirical Validation (§6.1–6.12 design, calibration, drawdown, ablation and sensitivity)`；counterevidence `arXiv:2606.17383v1 §4 Model Risk (§4.1–4.7); §6.11 assumptions; §6.12 interpretation`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** POMDP 三层 validation 在单一 portfolio case 演示，不能升级为一般 Agent 合规证明；latent-state/model risk 未闭合时回退规则策略与人工风险限额。


仅使用 `https://arxiv.org/html/2606.17383v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Confidence 要在 Belief、Action 与 Outcome 三层校准`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Bifrost: Hybrid TEE-FHE Inference for Privacy-Preserving Transformer and LLM Serving](https://arxiv.org/html/2606.17421v1)

**2606.17421 — Bifrost: Hybrid TEE–FHE Inference for Privacy-Preserving Transformer and LLM Serving**

**问题与机制变化。** 机密推理不能把 TEE 与 FHE 当互斥标签；应按算子泄漏面、密文代价与 PD 数据路径划分 trust boundary，并记录跨边界转换和 fallback。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17421v1 §3 Bifrost System Design; §4 Implementation`；Evaluation=`arXiv:2606.17421v1 §5 Evaluation`；Counterevidence=`arXiv:2606.17421v1 §6.2 Limitations`。Workload=`privacy-preserving transformer/LLM serving across hybrid TEE–FHE partitions`；Model=`GPT-2 (124M) and Qwen3 (0.6B)`；Hardware=`One server with 24 vCPUs, 128 GiB RAM, Intel TDX and one NVIDIA H20 96 GiB GPU`；Evaluator=`latency, communication and privacy/security analyses in §5`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 混合边界减少 FHE 覆盖却扩大 TEE TCB 与转换面；实验不证明 host I/O、side channel 或任意模型部署安全。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17421v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `隐私不是一个开关，而是明文边界的重新分配`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents](https://arxiv.org/html/2606.17467v1)

**2606.17467 — PARSE: Provenance-Aware Retrieval Sanitization for Professional Domain LLM Agents**

**问题与机制变化。** 专业文档 RAG 的 ingestion 需保留 provenance-aware sanitization、可追溯 rejection 与 utility check，不能把 paraphrase 或通用文本过滤当作 indirect-instruction 清除证明。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17467v1 §3 PARSE provenance-aware sanitization pipeline`；Evaluation=`arXiv:2606.17467v1 §4–§5 122-task, five-domain evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17467v1 has no dedicated limitations section; exact-v1 counterevidence is localized at limitations discussion on real-document/domain coverage and paraphrase failure`。Workload=`122 adversarial-document tasks: financial 24, legal 25, medical 23, scientific 25, DevOps 25`；Model=`Claude Sonnet 4.5 task generator; Haiku and Sonnet Parse calls; Llama Guard 4 baseline`；Hardware=`Not Disclosed`；Evaluator=`attack success rate, task utility and ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更强 sanitization 会删除有用内容并依赖 parser/provenance quality；受测文档与攻击不证明开放语料安全。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17467v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前正文 `RAG 安全必须覆盖完整状态生命周期` 已形成 owner-level 机制链；本项已实际 Integrate。

### [SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation](https://arxiv.org/html/2606.17518v1)

**2606.17518 — SpecGen: Accelerating Agentic Kernel Optimization with Speculative Generation**

**问题与机制变化。** Agentic kernel search 可在主 reasoning 继续时 speculative 生成候选，并行执行 validation/profile；控制面还必须协调 GPU pool、候选 lineage 与远端 KV/temporary state。

**State / data / control owner。** `INFER-TENSORRT-LLM` 是唯一知识 owner；`Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17518v1 §3 SpecGen design; §4 speculative generation and resource coordination`；Evaluation=`arXiv:2606.17518v1 §5–§6 kernel-optimization evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17518v1 has no dedicated limitations section; exact-v1 counterevidence is localized at discussion of spare-GPU, remote-KV and workload/hardware dependence`。Workload=`10 KernelBench Level-1 tasks and 10 Level-2/3 tasks; 100 search iterations per task; 40 timed runs after 10 warmups`；Model=`GLM-5.1 served by vLLM; DeepSeek-V4-Pro official API in high-reasoning mode`；Hardware=`Up to 18 NVIDIA H200 GPUs with NVLink and RoCEv2; Intel Xeon Platinum 8558 host`；Evaluator=`kernel correctness, optimization time and throughput/speedup comparisons`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 投机扩大并行度也制造无效候选、额外显存和验证争用；H200 kernel-search结果不是任意 compiler/runtime 加速保证。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17518v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前命题级锚点为 `Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery](https://arxiv.org/html/2606.17519v1)

**2606.17519 — Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery**

**问题与机制变化。** 大工具目录的 routing loss 应拆成 retrieval gap 与 confusion gap；平台需分别治理 candidate recall、semantic overlap、排序偏置与 clarification fallback。

**State / data / control owner。** `AGENT-TOOL-CALLING` 是唯一知识 owner；`Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17519v1 §3 Experimental Setup; §4.1 two-component decomposition`；Evaluation=`arXiv:2606.17519v1 §5.1–5.5 shortlisting, production validation and error analysis`；Counterevidence=`arXiv:2606.17519v1 Limitations after §7; single enterprise catalog and interface differences`。Workload=`4,105 synthetic queries and 1,435 human-labelled production queries over a catalog of 110 agents and 584 tools`；Model=`GPT-5.1, GPT-5.4 and Claude Sonnet 4.5`；Hardware=`Not Disclosed`；Evaluator=`multi-label F1, retrieval/confusion oracle gaps, bootstrap CIs and annotation agreement`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** shortlisting降低 prompt 与 miss，却引入 retriever latency和约 9% shortlist miss；30-agent elbow 不是通用阈值。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17519v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-TOOL-CALLING` owner 为 [books/part-07-agent/78-tool-calling.md](../../../../books/part-07-agent/78-tool-calling.md)。Review notes 前命题级锚点为 `Tool Discovery 与选择`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [AoiZora: Topology-Aware Auto-Parallel Optimization for Inference of Diffusion Transformers](https://arxiv.org/html/2606.17566v1)

**2606.17566 — AoiZora: Topology-Aware Auto-Parallel Optimization for Inference of Diffusion Transformers**

**问题与机制变化。** 分布式 DiT compiler planner 需先在 pre-compilation IR 高召回剪枝，再用 compiled HLO 与物理互连拓扑排序 sharding/placement；logical mesh 不是最终性能身份。

**State / data / control owner。** `INFER-TENSORRT-LLM` 是唯一知识 owner；`Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17566v1 §4 AoiZora, especially §§4.1–4.5; §5 implementation`；Evaluation=`arXiv:2606.17566v1 §6.1–6.6 methodology, latency, fidelity, ablation and planning cost`；Counterevidence=`arXiv:2606.17566v1 TPU v5e sub-slice, rectangular-topology and Wan 2.1 scope in §§2,6`。Workload=`Wan 2.1 one-step video-DiT denoising at 480p and 720p with 21, 41 and 81 frames`；Model=`Wan 2.1`；Hardware=`TPU v5e-4, v5e-8 and v5e-16 sub-slices`；Evaluator=`end-to-end denoising latency, search fidelity, ablations and planner cost`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 编译候选减少能省 planning cost，却可能漏掉好计划；1.42x 是指定 TPU/DiT denoising step，不是普遍加速。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17566v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-TENSORRT-LLM` owner 为 [books/part-05-inference-system/49-tensorrt-llm.md](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。Review notes 前正文 `分布式 DiT Plan 必须经过编译后拓扑复排` 已形成 owner-level 机制链；本项已实际 Integrate。

### [Cordon: Semantic Transactions for Tool-Using LLM Agents](https://arxiv.org/html/2606.17573v1)

**2606.17573 — Cordon: Semantic Transactions for Tool-Using LLM Agents**

**问题与机制变化。** 多步 tool execution 需要 task-scoped semantic transaction：shadow state、effect outbox、result lineage、delegated authority 与 recovery log 在一次 validate 后统一 commit/abort。

**State / data / control owner。** `AGENT-WORKFLOW` 是唯一知识 owner；`Books/part-07-agent/78-tool-calling.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17573v1 §3 Semantic Transaction Model; §4 Runtime Architecture; §5 Implementation`；Evaluation=`arXiv:2606.17573v1 §6.1–6.4 security, performance and benchmark correctness`；Counterevidence=`arXiv:2606.17573v1 §6.5 Limitations and Future Work`。Workload=`45 risk workflows from nine boundary categories by five risk families; five deterministic rollback trajectories; tau-bench and Terminal-Bench`；Model=`DeepSeek-V4-Pro`；Hardware=`Not Disclosed`；Evaluator=`pre-commit interception, rollback latency, task time/tokens and benign correctness`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 延迟外部 effect 提高 rollback/audit，却引入 approval latency、补偿语义与事务管理 TCB；45 个风险 workflow 不是完备安全证明。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17573v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-WORKFLOW` owner 为 [books/part-07-agent/81-workflow.md](../../../../books/part-07-agent/81-workflow.md)。Review notes 前命题级锚点为 `Durable Execution 与 Replay`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning](https://arxiv.org/html/2606.17591v1)

**2606.17591 — Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning**

**问题与机制变化。** Verbal RL 的持久状态应分 rules、episode evidence 与 compositional skills，并支持置信更新、冲突处理、停用和重新激活，而非单调追加经验摘要。

**State / data / control owner。** `AGENT-MEMORY` 是唯一知识 owner；`Books/part-07-agent/81-workflow.md; Books/part-07-agent/82-multi-agent.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17591v1 §2.2 requirements; §3.1 three-layer architecture; §3.2 curation loop`；Evaluation=`arXiv:2606.17591v1 §4 financial-forecasting validation`；Counterevidence=`arXiv:2606.17591v1 §5 Limitations and non-stationary financial-case boundary`。Workload=`AAPL, AMZN, FB, GOOGL and MSFT; 2013-2016 learning period and 2017 test period`；Model=`Qwen3-VL-235B; Claude Sonnet 4.6 proposer, critic and curator`；Hardware=`Not Disclosed`；Evaluator=`accuracy and risk-adjusted return under zero-shot, partial and full curation loops`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 治理能减 stale transfer 却增加 evidence ledger、curator误判与上下文成本；金融案例不证明跨域收益。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17591v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MEMORY` owner 为 [books/part-07-agent/77-memory.md](../../../../books/part-07-agent/77-memory.md)。Review notes 前命题级锚点为 `从原始轨迹到派生策略：Memory 的演进不是无限追加`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/html/2606.17730v1)

**2606.17730 — ActWorld: From Explorable to Interactive World Model via Action-Aware Memory**

**问题与机制变化。** 交互式 world model 的 memory 必须把 action-conditioned transition、event frame 与 object identity 跨 rollout 保存；只缓存视觉帧不足以复现可干预因果状态。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 是唯一知识 owner；`Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md; Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17730v1 §3 ActWorld action-aware hierarchical/persistent memory`；Evaluation=`arXiv:2606.17730v1 §4–§5 interactive world-model experiments and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17730v1 has no dedicated limitations section; exact-v1 counterevidence is localized at environment/action coverage and long-horizon generalization limitations`。Workload=`I-Bench: 300 prompts in 30 sequences of 10 prompts; each prompt has three action verbs and two or three camera primitives`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`interaction fidelity, long-horizon consistency and memory ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 持久 action memory减少状态遗忘却增加写入、检索与错误累积；有限环境不证明开放世界因果 fidelity。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17730v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前命题级锚点为 `Persistent world state`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [LUMEN: Coordinated Failure Recovery for Distributed LLM Serving](https://arxiv.org/html/2606.17787v1)

**2606.17787 — LUMEN: Coordinated Failure Recovery for Distributed LLM Serving**

**问题与机制变化。** Serving failure recovery 应联合决定 KV checkpoint placement、interrupted-request redistribution 与 model-reload期间的 draft capacity，而非各自局部优化。

**State / data / control owner。** `INFER-SCHEDULING` 是唯一知识 owner；`Books/part-05-inference-system/55-pd-disaggregation.md; Books/part-06-ai-infrastructure/63-gpu-scheduler.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17787v1 §4 LUMEN Design, §§4.2–4.4; §5 implementation`；Evaluation=`arXiv:2606.17787v1 §6.1–6.4 four/eight-worker prototype and up-to-64-worker simulation`；Counterevidence=`Not Disclosed — arXiv:2606.17787v1 has no dedicated limitations section; exact-v1 counterevidence is localized at worker-failure/full-reload assumptions and prototype/simulator scope`。Workload=`Splitwise-Conv traces under one to five simultaneous worker failures and request rates from 12 to 21 QPS`；Model=`Qwen3-32B and Qwen3-14B prototypes; Llama-3-70B simulation`；Hardware=`Not Disclosed`；Evaluator=`mean TTFT, TPOT and recovery time versus restart and fixed-checkpoint baselines`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 持续 checkpoint占 host memory/network，speculative recovery增加 draft state；结果不覆盖 correlated fabric failures或 production failover。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17787v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-SCHEDULING` owner 为 [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md)。Review notes 前命题级锚点为 `MoE Failure Recovery 必须拥有 Request 与 Expert Generation`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor](https://arxiv.org/html/2606.17872v1)

**2606.17872 — AnchorKV: Safety-Aware KV Cache Compression via Soft Penalty with a Refusal Anchor**

**问题与机制变化。** KV compression policy 要把 safety-critical refusal state 作为 offline anchor，并以 soft retention penalty约束 eviction；平均 attention/quality proxy 不能拥有安全状态。

**State / data / control owner。** `INFER-KV-CACHE` 是唯一知识 owner；`Books/part-05-inference-system/43-prefill.md; Books/part-05-inference-system/48-speculative-decoding.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17872v1 §3 AnchorKV refusal-anchor construction and soft-penalty compression`；Evaluation=`arXiv:2606.17872v1 §4–§5 safety/utility/cache evaluations and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.17872v1 has no dedicated limitations section; exact-v1 counterevidence is localized at anchor/task/model/compression-ratio scope and refusal-proxy boundary`。Workload=`AdvBench harmful-behaviors split: 312 train, 104 validation and 104 test prompts; LongBench utility evaluation`；Model=`Llama-3.1-8B-Instruct target; Mistral-NeMo-Instruct-2407 attacker; DeepSeek-V3 paraphraser`；Hardware=`Not Disclosed`；Evaluator=`refusal/safety rate, task utility, memory reduction and ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 保留安全 anchor 会牺牲压缩率与普通 utility，anchor 失配还会给虚假安全感；不替代 end-to-end safety gate。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17872v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `INFER-KV-CACHE` owner 为 [books/part-05-inference-system/45-why-kv-cache-speeds-up.md](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。Review notes 前命题级锚点为 `压缩后的答案正确不等于证据仍被保留`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [How Inference Compute Shapes Frontier LLM Evaluation](https://arxiv.org/html/2606.17930v1)

**2606.17930 — How Inference Compute Shapes Frontier LLM Evaluation**

**问题与机制变化。** Frontier capability 必须报告为 inference-compute curve，并冻结 serial/parallel allocation、submission次数、feedback、compaction 与 matched budget；单点分数不能比较 generations。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17930v1 §2.1–2.5 models, scaling techniques, feedback, benchmarks and budgets`；Evaluation=`arXiv:2606.17930v1 §3.1–3.3 seven-benchmark scaling curves; Appendix A protocols`；Counterevidence=`arXiv:2606.17930v1 §4.4 Limitations; judge-noise and plateau interpretation in Appendix A.5`。Workload=`Seven benchmarks spanning software engineering, mathematics, medicine and cybersecurity; five trajectories per task`；Model=`Up to 12 frontier language models; six-model fully crossed main suite`；Hardware=`Not Disclosed`；Evaluator=`cumulative score versus tokens, serial/parallel allocation, plateau/reach/reliability analyses`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 大预算提高 elicitation也放大成本与 benchmark-specific scaffolding；tested plateau 不是模型能力上限。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17930v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `生成迭代次数不能代替实际计算预算`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving](https://arxiv.org/html/2606.17949v1)

**2606.17949 — RouteBalance: Fused Model Routing and Load Balancing for Heterogeneous LLM Serving**

**问题与机制变化。** 异构 serving gateway 应联合选择 model 与具体 replica，把质量/成本约束和 queue/load state 放入同一 routing decision；先选模型再盲目 LB 会丢失耦合。

**State / data / control owner。** `PLATFORM-GATEWAY` 是唯一知识 owner；`Books/part-05-inference-system/53-kserve-llm.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.17949v1 §3 RouteBalance formulation; §4 fused routing/load-balancing mechanism`；Evaluation=`arXiv:2606.17949v1 §5 evaluation on heterogeneous serving pool`；Counterevidence=`Not Disclosed — arXiv:2606.17949v1 has no dedicated limitations section; exact-v1 counterevidence is localized at model-quality estimates, arrival distribution and cluster-size limitations`。Workload=`3,534 prompts per evaluation cell over three budget-tightness mixes and request rates including 8, 12, 16 and 24`；Model=`Not Disclosed`；Hardware=`28 GPUs in a 13-instance serving pool`；Evaluator=`quality/cost constraints, load balance, latency and throughput comparisons`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 联合控制增加全局 state 与估计误差；28-GPU/13-instance结果不证明跨 provider 或 workload 优越。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.17949v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-GATEWAY` owner 为 [books/part-06-ai-infrastructure/62-gateway.md](../../../../books/part-06-ai-infrastructure/62-gateway.md)。Review notes 前命题级锚点为 `Gateway、EPP 与 Engine Scheduler`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents](https://arxiv.org/html/2606.18037v1)

**2606.18037 — ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents**

**问题与机制变化。** MCP factuality verifier 必须把 source block identity、claim-to-source relation 与 final answer 分开评分；高 block F1 不能证明 provenance relation正确。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18037v1 §3 ProvenanceGuard source-aware verification pipeline`；Evaluation=`arXiv:2606.18037v1 §4–§5 MCP factuality experiments and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18037v1 has no dedicated limitations section; exact-v1 counterevidence is localized at source-ID stability, domain/tool and verifier-model limitations`。Workload=`281 medical MCP-agent traces; 266-trace claim subset with 2,325 labels; 40-trace held-out split with 361 claims`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`block retrieval F1, source-relation accuracy and answer factuality`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更细 provenance验证增加 calls 与 latency，source relation judge仍会漂移；不替代 authoritative source access。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18037v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-RAG` owner 为 [books/part-07-agent/76-rag.md](../../../../books/part-07-agent/76-rag.md)。Review notes 前命题级锚点为 `视觉证据也必须有可追踪的 Claim–Evidence 生命周期`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization](https://arxiv.org/html/2606.18121v1)

**2606.18121 — On the Reliability of Networks of AI Agents: Density Evolution, Stopping Sets, and Architecture Optimization**

**问题与机制变化。** 多 Agent reliability 需把 proposer abstention、verifier abstention 与 message loss 作为不可互换的 factor-graph channels，并审计 certificate-stopping set 而非只扩 agent 数。

**State / data / control owner。** `AGENT-MULTI-AGENT` 是唯一知识 owner；`Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/66-evaluation-system.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18121v1 §IV role-typed Boolean-verifier model; §§V–X density evolution, stopping sets and optimization`；Evaluation=`arXiv:2606.18121v1 §XI calibration; §XII numerical validation; §XIII applications`；Counterevidence=`arXiv:2606.18121v1 §XIV-A limitations: correct surviving certificates, erasure-only and weak-dependence assumptions`。Workload=`Monte Carlo and deterministic-graph validation plus theorem/code/debate application mappings`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`density-evolution predictions, stopping sets and cost-constrained architecture optimization`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 理论可定位 topology瓶颈却依赖 sound verifier和局部树状假设；不覆盖 confidently-wrong/correlated failure。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18121v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `AGENT-MULTI-AGENT` owner 为 [books/part-07-agent/82-multi-agent.md](../../../../books/part-07-agent/82-multi-agent.md)。Review notes 前正文 `Coordination Failure` 已形成 owner-level 机制链；本项已实际 Integrate。

### [All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code](https://arxiv.org/html/2606.18168v1)

**2606.18168 — All Smoke, No Alarm: Oracle Signals in Agent-Authored Test Code**

**问题与机制变化。** Agent-authored tests 的 verifier strength 不能用“创建 test 文件”代理；release gate 应解析 assertion/oracle signal、执行路径与 failure discriminativeness。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18168v1 §3 oracle-signal taxonomy and test-code analysis method`；Evaluation=`arXiv:2606.18168v1 §4 analysis of roughly 86,000 patches/tests`；Counterevidence=`Not Disclosed — arXiv:2606.18168v1 has no dedicated limitations section; exact-v1 counterevidence is localized at repository/language/benchmark and static-analysis limitations`。Workload=`Approximately 86,000 agent-authored coding patches and associated test artifacts`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`presence and strength of explicit oracle signals, test execution and patch outcome`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更强 oracle审计增加解析与 mutation成本，仍可能漏掉语义空洞 assertion；统计比例不是所有 coding agents 的常数。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18168v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-EVALUATION-SYSTEM` owner 为 [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。Review notes 前命题级锚点为 `Harness Optimization 的 Test Boundary 必须对优化器不可见`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners](https://arxiv.org/html/2606.18198v1)

**2606.18198 — Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners**

**问题与机制变化。** Skill scanner 必须把 docs/code/resources/visual layers 与 execution simulation联结，因视觉隐藏指令可绕过纯文本/静态扫描后影响运行行为。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18198v1 §3 multimodal hidden-instruction threat model; §4 ExecScan pipeline`；Evaluation=`arXiv:2606.18198v1 §5–§6 attack/defense evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18198v1 has no dedicated limitations section; exact-v1 counterevidence is localized at skill formats, visual encodings, model/scanner and simulation-fidelity limits`。Workload=`multimodal agent skills containing document, code, resource and visual hidden instructions`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`attack success, scanner recall/precision and execution-grounded ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** execution-grounded扫描成本高且仍有模拟落差；受测 hidden channels 不证明未知编码被覆盖。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18198v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `PLATFORM-SECURITY` owner 为 [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md)。Review notes 前命题级锚点为 `Skill Poisoning 的真值是 Side Effect，而不是是否被调用`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Looped World Models](https://arxiv.org/html/2606.18208v1)

**2606.18208 — Looped World Models**

**问题与机制变化。** Looped world model 以共享 recurrent block、spectral stability、adaptive early exit 与 deferred latent decoding形成 iterative-depth 分支；Ch25 已保存该 exact family 与机制边界。

**State / data / control owner。** `MULTIMODAL-WORLD-MODELS` 是唯一知识 owner；`Books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md; Books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18208v1 §3.1–3.5 looped dynamics, variable-depth training, early exit and deferred decoding`；Evaluation=`arXiv:2606.18208v1 §4.1–4.3 ScienceWorld, AlfWorld and deferred-decoding analysis`；Counterevidence=`arXiv:2606.18208v1 no dedicated limitations section; task-scale, parameter-efficiency and real-time claims bounded by §§4–6`。Workload=`ScienceWorld and ALFWorld world-model prediction and control`；Model=`LoopWM variants and exact-v1 baselines`；Hardware=`Not Disclosed`；Evaluator=`task performance, prediction quality, parameter efficiency and depth/deferral ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 已有 Ch25 已覆盖 recurrent transition、state tiering与受限 workload；100x 参数效率不等于 wall-clock、开放世界或物理 fidelity。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18208v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-WORLD-MODELS` owner 为 [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。Review notes 前命题级锚点为 `Persistent world state`；该锚点已经覆盖长期机制，本项为 `No Change — Existing Coverage`。

### [Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement](https://arxiv.org/html/2606.18247v1)

**2606.18247 — Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement**

**问题与机制变化。** Visual verifier 可在 inference 时对 policy proposal 评分/重采样，并把 verified rollouts作为下一轮 policy data；verifier只拥有 proposal/evidence，不拥有物理安全。

**State / data / control owner。** `MULTIMODAL-EMBODIED-VLA` 是唯一知识 owner；`Books/part-03-multimodal-world-models/25-multimodal-world-models.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18247v1 §3 visual-verifier training and inference-time steering; §4 autonomous improvement loop`；Evaluation=`arXiv:2606.18247v1 §5 robot-policy evaluations and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18247v1 has no dedicated limitations section; exact-v1 counterevidence is localized at verifier calibration, task/robot/camera and sim-to-real limitations`。Workload=`robot manipulation trajectories with visual verification, steering and self-training`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`task success under steering and policy improvement from verified rollouts`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 多 proposal与视觉 judge增加 actuation latency且会自强化 verifier偏差；有限任务不证明真实机器人安全。


**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18247v1` 的 exact-v1 正文，已通过该 exact-v1 HTML/PDF 正文完成复核且无剩余获取缺口；later revision/artifact 不参与，ordinary pending=`0`。

**V3 Books 复验。** 当前 `MULTIMODAL-EMBODIED-VLA` owner 为 [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。Review notes 前正文 `Reason–Imagine–Act 把内部 Rollout 变成 Proposal，而非执行权限` 已形成 owner-level 机制链；本项已实际 Integrate。

<!-- full-raw-recovered-evidence:start -->

### [Towards Distributed Inference of LLMs on a P2P Network](https://arxiv.org/html/2606.17059v1)

**问题、机制与 owner。** 去中心化 prefix-cache routing 以本地 radix tree 和周期性 anti-entropy 维护 peer cache 估计；stale metadata 只损失命中率、不破坏输出正确性，因此 weak consistency 可以成为路由正确性边界。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 System Design；§3 Safety Conditions and Failure Handling；§4–5 Experimental Setup/Results`。收益只在低通信延迟、prefix 分布偏斜的模拟 MMLU workload 中成立；affinity hotspot、高 RTT、peer failure 与估计过期会降低收益，不能外推生产 tail SLO。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 在 Review notes 前已写入 weak-consistency cache metadata、目标节点 identity 验证、anti-entropy 与普通负载均衡 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Statistical Foundations of LLM-based A/B Testing: A Surrogacy Framework for Human Causal Inference](https://arxiv.org/html/2606.17165v1)

**问题、机制与 owner。** 用 LLM 输出替代人类 outcome 做 A/B 推断时，必须把 surrogacy、treatment comparability、overlap 与 falsification test 写进 causal contract；模型评分相关性不等于人类 treatment effect 可识别。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Setup；§3 Surrogacy Framework；§4 Stochasticity`。作者识别结论依赖 surrogacy/comparability 假设和可观测 overlap；39% effect recovery 只属于所测数据，不能把单次 LLM 代理分数当作人类因果真值。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已写入 surrogate observation、experiment owner、识别假设与真人样本/随机实验 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Rethinking Groups in Critic-Free RLVR](https://arxiv.org/html/2606.17250v1)

**问题、机制与 owner。** critic-free RLVR 中 group 的关键作用之一是避免把所有失败 token 一起当作负证据；negative-token filtering 允许 single-rollout update，但会失去 group 内校准与探索覆盖。 唯一知识 owner 为 `TRAIN-GRPO`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2.1–2.4 grouping/negative-token analysis；§3 Methodology`。只在作者 RLVR 任务与模型上验证；single rollout 降低同步成本，却放大 verifier error、采样方差和错误正例，不能普遍替代 group sampling。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-04-training-system/33-grpo.md](../../../../books/part-04-training-system/33-grpo.md) 在 Review notes 前的 `Verifiable Reward 不等于每个样本都可学习` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [OTRO: Oblivious Tokenization Path with Square-Root ORAM](https://arxiv.org/html/2606.17358v1)

**问题、机制与 owner。** CPU/GPU TEE 保护模型执行时，tokenizer 的词表访问路径仍可泄露 prompt；OTRO 用 square-root ORAM、只读表副本与 epoch rotation 隐藏访问序列，并把 KV/计算 overlap 纳入 TTFT 路径。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§III Leakage/Threat Model；§IV Reconstruction；§V–VI OTRO Design/Evaluation`。安全性依赖 TEE/ORAM threat model、访问模式实现与随机性更新；额外带宽、stash/epoch 管理和 tokenizer-specific layout 会增加 TTFT，未覆盖所有 tokenizer 与 side channel。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前已写入 tokenizer access-path threat、oblivious access、token identity owner 与普通 tokenizer/可信边界 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Dissecting model behavior through agent trajectories](https://arxiv.org/html/2606.17454v1)

**问题、机制与 owner。** 轨迹分解显示 Agent 行为由模型与 harness 共同形成；tool boundary、parser 和 feedback path 的失真会制造 intent–execution gap，因此 model/harness revision 与 component receipt 必须共同进入评估身份。 唯一知识 owner 为 `AGENT-PLATFORM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 SSA Architecture；§3 Refinements；§4–5 trajectory metric/evaluation`。作者 harness 与任务不能代表所有 Agent；轨迹差异是诊断证据，不等同模型内在能力或生产成功率。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-07-agent/84-agent-platform.md](../../../../books/part-07-agent/84-agent-platform.md) 在 Review notes 前的 `Agent harness 必须把 model intent、实际 tool payload、environment result 与回送 context 做成双向可观测接口` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Online LLM Selection via Constrained Bandits with Time-Varying Demand](https://arxiv.org/html/2606.17489v1)

**问题、机制与 owner。** 在线模型选择在需求变化和 packing/covering 约束下应把 model pool、成本、质量估计与剩余资源作为同一 constrained-bandit state，而不是每次请求独立贪心。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§III System Model；§IV Formulation；§V Algorithm`。regret/constraint bounds依赖需求与反馈假设；partial feedback、模型版本漂移、冷启动和 tail latency 未被一般性解决，固定路由在流量稳定时仍更可审计。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-05-inference-system/56-inference-scheduling.md](../../../../books/part-05-inference-system/56-inference-scheduling.md) 在 Review notes 前的 `多轮 Routing 是带剩余预算的序列决策` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [MagicSim: A Unified Infrastructure for Executable Embodied Interaction](https://arxiv.org/html/2606.17511v1)

**问题、机制与 owner。** 可执行 embodied interaction 应以 episode/MDP transition 为单位，由 runtime 持有 simulator、robot、planner、seed 与 record state；批处理只是共享 execution contract，不能把各 environment 状态混成 frame 流。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§1.2–1.4 Design；§3 Parallel Episode Runtime/MDP Boundary`。确定性与吞吐来自作者 simulator/runtime，不证明 sim-to-real 或硬实时控制；状态池增加 reset 泄漏、隔离和故障恢复成本。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 在 Review notes 前的 `Batched Environment 需要持久且可寻址的状态池` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack](https://arxiv.org/html/2606.17574v1)

**问题、机制与 owner。** Physical AI 评估把 task、resource、result 抽象和 episode driver 统一，令 framework、simulator、model 与 hardware outcome 可用同一 run identity 关联；统一接口不能抹平各层 truth owner。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.1–3.4 System Design；§4 Evaluation`。跨框架 alignment 只覆盖所测 physical-AI stack；adapter 语义、真实机器人故障和生产 tail 未闭合。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Cross-layer Evaluation 不允许下游成功掩盖上游故障` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [TivTok: Broadcasting Time-Invariant Tokens for Scalable Video Tokenization](https://arxiv.org/html/2606.17590v1)

**问题、机制与 owner。** 视频 tokenizer 可把 time-invariant scene content 与 time-varying motion 分成不同 token owner，并通过 attention-scope factorization 和 invariant-token broadcasting 避免重复编码；复用必须保留时间与场景 identity。 唯一知识 owner 为 `MULTIMODAL-REPRESENTATION`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3 Method；§4 Experiments；Appendix ablations`。压缩率与质量只绑定作者视频数据、codec/tokenizer 与模型；镜头切换、遮挡和快速运动会使 invariant 判断过期，广播错误会跨帧传播。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 在 Review notes 前已写入 TIV/TV scope、tokenizer/decoder ownership、过期传播 failure 与 dense-token fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [The Benchmark Illusion: Pruned LLMs Can Pass Multiple Choice but Fail to Answer](https://arxiv.org/html/2606.17609v1)

**问题、机制与 owner。** 剪枝后的模型可能保留 multiple-choice recognition 却失去 open-generation access；release gate 必须在同一知识 slice 上配对 recognition、free generation、answerability 与形式变换，区分知识存在和生成可达性。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Diagnostic Framework；§3 Demotion, Not Erasure`。作者结论来自所测 pruning/model/QA 和 multilingual stress test；恢复 prompt 或选项提示不证明部署生成能力已恢复，也不能外推所有压缩。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前已写入 paired recognition/free-generation、evaluator/release authority、额外评测成本与开放生成 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering](https://arxiv.org/html/2606.17799v1)

**问题、机制与 owner。** coding-agent benchmark 若只冻结题目和单一 reference solution，会把需求不完备、harness/环境差异与模型执行混成总分；评估身份必须保存 task、harness、environment、tool budget 与 artifact verifier。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`position paper；problem analysis and proposed alignment principles`。该文是 position paper，不提供统一 benchmark 或生产因果验证；其论点只能支持 measurement contract 边界。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `Evaluation Identity 必须包含 Harness 与 Environment` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Beyond Native Success: Auditing Deployment-Interface Exposure of CLIP Backdoors](https://arxiv.org/html/2606.17815v1)

**问题、机制与 owner。** CLIP backdoor 的风险要沿实际 deployment interface 审计：component readout、trigger、target label、reference set 与 downstream wrapper 共同决定可利用 exposure，而非只看 native benchmark success。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`Method/interface audit；deployment-facing evaluations`。结果绑定 CLIP、触发器与所测接口；暴露率不是真实攻击发生率，component sensor 不能替代 end-to-end policy/effect gate。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前的 `Embedding 也是可执行数据供应链的一部分` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Small Initialization Matters for Large Language Models](https://arxiv.org/html/2606.17945v1)

**问题、机制与 owner。** 初始化尺度会改变早期表示、梯度和最终 basin；训练 identity 必须绑定 parameterization、initialization、optimizer state、schedule 与 data order，不能把同一 loss 轨迹解释成同一 learned function。 唯一知识 owner 为 `TRAIN-PRETRAINING`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Result；§3 Discussion`。理论和实验只覆盖论文设定；更小初始化不是跨架构通用最优，过小会削弱信号并增加 warmup/precision 风险。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-04-training-system/28-pretraining.md](../../../../books/part-04-training-system/28-pretraining.md) 在 Review notes 前的 `Optimizer 不是与参数化无关的旋钮` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs](https://arxiv.org/html/2606.17952v1)

**问题、机制与 owner。** SoftMoE 将离散 top-k 改为可微的 expert allocation，并学习 active-expert budget；router 仍拥有选择语义，runtime 必须把可变 expert 数转成 capacity/placement/communication 计划。 唯一知识 owner 为 `MODEL-MOE`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3–4 differentiable routing；§5 Experiments`。训练可微不等于部署成本可控；可变 active set 会扩大 All-to-All、容量和 kernel shape 波动，作者结果不证明普遍优于硬 top-k。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-02-model/21-moe.md](../../../../books/part-02-model/21-moe.md) 在 Review notes 前的 `从固定 Top-k 到受总预算约束的 Variable-k` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [VoidPadding: Separate Padding from Semantic Termination in Masked Diffusion Language Models](https://arxiv.org/html/2606.17999v1)

**问题、机制与 owner。** masked diffusion LM 中同一 EOS 同时承担语义终止与 padding 会让长度状态混淆；独立 VOID token 把空白 canvas 与终止语义分离，使 length/admission、denoising 与 final commit 拥有不同状态。 唯一知识 owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2 Masked Diffusion；§3 EOS Overflow；§4 VoidPadding/Experiments`。额外 token 与 adaptive canvas 增加 tokenizer、training objective 和 sampler compatibility；作者任务不证明所有 dLLM 或 runtime 都改善，AR termination 仍是独立分支。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 在 Review notes 前已写入 VOID/EOS 状态分离、length/denoising/commit owners、runtime compatibility 代价与自回归 fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Recursive Scaling in Masked Diffusion Models](https://arxiv.org/html/2606.18022v1)

**问题、机制与 owner。** masked diffusion 的 recursive depth 通过共享参数反复执行，把 parameter count 与 test-time execution depth 分离；每轮 state 必须保持可修订，停止规则不能由迭代次数冒充正确性。 唯一知识 owner 为 `MODEL-TRANSFORMER-LAYER`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`Method/recursive scaling analysis；Experiments`。收益绑定 masked-diffusion 模型与任务；更多 recursion 可能积累错误和延迟，不能等同新参数容量或普遍 scaling law。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-02-model/17-transformer-layer.md](../../../../books/part-02-model/17-transformer-layer.md) 在 Review notes 前的 `Parameter Depth 与 Execution Depth 可以分离` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Latency Prediction for LLM Inference on NPU Systems](https://arxiv.org/html/2606.18042v1)

**问题、机制与 owner。** 闭源 NPU microarchitecture、compiler rewrite 与 bucket nonlinearity使纯算子相加失效；LENS 用少量端到端测量校准分桶 latency surrogate，但 estimator 只拥有候选预测，不拥有部署 SLO。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§2–3 NPU challenges；§4 LENS；Evaluation`。两次测量/分桶的准确性绑定目标 NPU、compiler、model shape 与软件版本；版本漂移、queueing 和 host overhead 要求重校准及真实 replay。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/66-evaluation-system.md](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 在 Review notes 前的 `从直接 Grid Search 到 Floor-first Diagnosis` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping](https://arxiv.org/html/2606.18120v1)

**问题、机制与 owner。** Handlebars triple-brace 等模板路径可让不可信文本越过预期 escaping，并把数据放进结构性 role；delimiter/HTML escaping 只处理字符族，不能替代 typed role、source label 与 effect-time authorization。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`attack construction and template analysis；evaluations across prompt layouts`。攻击依赖具体模板、parser 与模型；修复一个 delimiter family 不证明其他 rendering path 安全，结构化 prompt 也不能独自授予或撤销权限。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-06-ai-infrastructure/72-security.md](../../../../books/part-06-ai-infrastructure/72-security.md) 在 Review notes 前的 `Instruction Hierarchy 必须携带 Authenticated Provenance` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Fixed-Point Reasoners: Stable and Adaptive Deep Looped Transformers](https://arxiv.org/html/2606.18206v1)

**问题、机制与 owner。** looped Transformer 以共享 block 增加 execution depth，并用 pre-norm/residual scaling维持 fixed-point 稳定，再按收敛状态自适应停止；执行深度不等于参数深度。 唯一知识 owner 为 `MODEL-TRANSFORMER-LAYER`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.1 pre-norm；§3.2 residual scaling；experiments`。收敛阈值可能误停或拖延，稳定 fixed point 不保证任务正确；论文设置不证明所有 architecture/length 可迁移。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-02-model/17-transformer-layer.md](../../../../books/part-02-model/17-transformer-layer.md) 在 Review notes 前的 `Parameter Depth 与 Execution Depth 可以分离` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

### [Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification](https://arxiv.org/html/2606.18249v1)

**问题、机制与 owner。** 理解与生成若分别使用不兼容 visual token，shared backbone 仍无法共享状态。UniAR 以 shared context–visual tokenizer、parallel bitwise prediction 与独立 decoder 建立共同 token identity，同时保留生成 artifact 边界。 唯一知识 owner 为 `MULTIMODAL-REPRESENTATION`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.1 Unified Visual Tokenizing；§3.2 AR Modeling；§4 Experiments`。统一 token 降低接口分裂却引入 rate/distortion、bitwise independence 与 decoder 版本耦合；作者结果不证明单一表示对所有理解/生成任务最优。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/23-multimodal-representation.md](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 在 Review notes 前已写入统一 token identity、tokenizer/decoder owner、目标竞争代价与双 tokenizer bridge fallback 的完整机制链；独立写后复核通过，本项已实际 Integrate。

### [Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion](https://arxiv.org/html/2606.18250v1)

**问题、机制与 owner。** 未来 3D state 要把 ego-motion 与 world-motion 分离，才能让相机位姿成为 action proxy、场景变化成为 environment transition；视觉重建质量不能替代可控 dynamics。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻章节只消费带版本的 handoff。

**Evidence 与边界。** exact-v1 locator：`§3.2 Future 3D Prediction；§3.3 Ego/World Motion；§4 Evaluation`。结果绑定作者 driving/video 数据与几何假设；ego-motion proxy 不是完整 action，遮挡和动态对象仍会制造不可观测状态。

**Trade-off、failure 与 fallback。** 新路径只有在上述 exact-v1 前提成立时可用；收益以额外状态、校准、运行成本或新 failure mode 为代价。身份、版本、可观测性或预算越界时回退 owner 章节的既有路径，不把作者 benchmark 外推为生产保证。

**Books Decision。** [books/part-03-multimodal-world-models/25-multimodal-world-models.md](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) 在 Review notes 前的 `从 RGB Rollout 到 Projective 4D Predictive State` 已完整承载该长期命题，结论为 `No Change — Existing Coverage`。

<!-- full-raw-recovered-evidence:end -->


### [GLM-5.2](https://www.zhipuai.cn/zh/research/161)

**问题、旧路径与约束变化。** Query-aware sparse attention 常让每个稀疏层独立维护 selector/indexer。它保留 layer-specific routing fidelity，但长上下文下 selector 计算和索引状态会随层数重复增长。GLM-5.2 的官方技术页披露 `IndexShare`：每四个稀疏注意力层复用同一 indexer，把逐层独立选择改成有边界的跨层 selector-state reuse。

**Mechanism 与 owner。** Indexer 输出只拥有候选 token selection，attention layer 仍拥有最终读写和残差更新；复用范围、刷新周期、model revision 与 fallback 必须显式绑定。唯一知识 owner 是 `MODEL-LONG-CONTEXT`，不是模型版本本身。

**Evidence 与边界。** 官方页给出精确时间 `2026/06/16 16:00`，并披露四层共享一个 indexer、1M context 与 per-token FLOPs 等作者主张。页面没有完整公开 hardware、precision、sequence composition、batch、concurrency、SLO、训练细节和实现 artifact，因此只能证明 creator-primary 所述设计，不能把 `2.9x` FLOPs 或 MTP acceptance `up to 20%` 外推为跨模型生产结论。

**Trade-off、failure 与 fallback。** 共享 indexer 减少 selector FLOPs 与状态，却假设相邻稀疏层的检索分布可复用；新增 stale selection、layer-specific recall loss、head imbalance、版本迁移和局部故障放大。分布漂移或召回审计失败时，应缩小 reuse scope 或回退逐层 indexer。

**Books Decision。** [MODEL-LONG-CONTEXT](../../../../books/part-02-model/22-long-context.md) 在 Review notes 前的 `Sparse Attention 的两个 ownership 轴` 已明确 selector refresh owner、跨层复用范围、stale-selection/head-imbalance 代价与回退边界；本项为 `No Change — Existing Coverage`。

### Books / semantic audit

原审计以level-2 `Review notes`为正文边界；本次撤回清理后有效旧arXiv为49项（14实际整合/35具体已有覆盖），加GLM-5.2具体已有覆盖，共旧50。未变的有效证据和实际写后层按原范围复用；撤回依赖修复的独立确认另记本日canonical，不把原完成标签用于证明该修复已经验收。

### [Selective Synergistic Learning for Video Object-Centric Learning](https://arxiv.org/html/2606.15527v1)

[必要§86](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§115/118：encoder边界教decoder、decoder内部教encoder，重标连通组pseudoidentity而不删实际slot。局部一致可共错，component非全pair同物，欠分/过分和质量反退仍保；固定S复杂度与FP16显存口径不授全网线性或普遍省费。原5因具体差额深入，[MULTIMODAL-REPRESENTATION Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)16689后/11745前原三件已真实SAVE/完整自读，经root§118实际POST通过，不授真实实体、因果或SLO；未核全附录/像素/实现或复现。

### [Track2View: 4D-Consistent Camera-Controlled Video Generation via Paired 3D Point Tracks](https://arxiv.org/html/2606.15534v1)

[必要§87](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§117/119：同点索引上source采样、跨时聚合、目标scatter形成双view条件，非warp帧或scatter可逆；训练两camera追踪与部署source重投影不同源，几何无参数非整个conditioner免训。保pose/对应代理、部分query/depth/flicker反退、遮挡内容由prior补和全部跟踪/适配/采样费，原6因该差额深入。[MULTIMODAL-GENERATIVE-PARADIGMS Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)15162后/29931前完整段、marker/本人注已真实SAVE/完整自读，root§119实际POST通过，不授任意相机、全4D真值或SLO；未核像素/demo/实现或复现。

### [A Decision-Theoretic View of Test-Time Training: When, How Far, and Which Directions to Adapt](https://arxiv.org/html/2606.15569v1)

[必要§88](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§120/121：局部平方promptkernel的修正仍经querycoupling读取，选收缩/步数与选更新方向分责；辅助残差evidence非query最优，Gaussian条件、任意rank投影非greedyhead保证及平均更多步/全费均保。原5因具体差额深入，[WORLDVIEW-WHY-MODELS-LEARN Ch4](../../../../books/part-01-worldview/04-why-models-learn.md)13942后/15219前真实原三件经实际POST通过，不采用普遍Bayes/PAC/非线性LLM保证；未核全证明/实现或复现。

### [Schattor: Schatten-family methods for deep learning optimization](https://arxiv.org/html/2606.15702v1)

[必要§89](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)与root§123/124：ball/regularized同方向不同dualnorm幅度，outermixednorm另分配跨block预算；globalmixed光滑/无偏covariance/独立batch与常数/全费不消失，dimensionfree非LLM净速/泛化。原5因具体差额深入，[TRAIN-PRETRAINING Ch28](../../../../books/part-04-training-system/28-pretraining.md)15268后/工程state前原三件真实SAVE/fullselfread，经实际POST通过，不采精确新率/全§6证明/实现或复现。

### [Topological Flow Matching](https://arxiv.org/html/2606.15897v1)

[必要§91](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)、root§122/125具名原件反证：打印heat谱control在a1、y0=0/y1=1配其ODE只到exp(-2)=.135335，Prop3 sinh路径却到1；不私补指数、分母或用另一正确式覆盖冲突。原5/中心争议暂缓，不入Books，不否定heat参考先验或全部有限经验。CIFAR10十run微小FID差额不认证普遍胜出，科学应用不纳本项目；重开需可核更正统一control/路径/ODE与实际采用/评价绑定，未读全证明或网络fetch失败不是本H原因。

### [SILAGE: Memory-Efficient, Full-Gradient-Free Nonconvex Optimization for Nested Finite Sums](https://arxiv.org/html/2606.15832v1)

[必要§90](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)、root§126/127：每数据组一份估计，以单coin耦合localreset、相邻两点差分和组多时active共享drift，避免周期globalrefresh但不免局部完整梯度/n份d维状态。保平均光滑/二层差分相似、Alg2字面状态触碰、合成logistic无墙钟/显存实测且全梯度诊断计费。原5具体差额深入，[TRAIN-PRETRAINING Ch28](../../../../books/part-04-training-system/28-pretraining.md)14562后/multiOptimizer H3前真实原三件经实际POST通过；未采精确率/PL/LLM实测、D1等价实现或复现，网络缓存timeout已由同版本官方HTML恢复，不记材料H。

### [You Don't Need Strong Assumptions: Visual Representation Learning via Temporal Differences](https://arxiv.org/html/2606.15956v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：必要§92，root§128/129；frame+RGBdiff条件残差匹配nextframe EMAteacher，不把时间变化全压成不变性。保future差分非past因果、EMA/CE非普遍反塌缩、联变配方与分割/光流/mean深度反侧、较大视频未必改善和两帧/teacher/motion/适配全费。原日期/分数不变，具体差额深入；[MULTIMODAL-REPRESENTATION](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)33223后/CalibCLIP前原三件真实SAVE/fullselfread，经root§129 sole实际POST通过，未核完整证明/全部图像素/实现或复现。

### [Active Learning with Low-Rank Structure for Data Selection](https://arxiv.org/html/2606.16045v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：必要§93，root§130/131；landmark目标loss、cheapembedding系数/残差组成非均匀分数，逆概率权重估固定currentloss，不授后续训练无损。保basis/KRR/合法文本不同、额外regularity与部分task/ratio弱于聚类/full、过大residual偏outlier和全选样/重训费，forward估算非墙钟。原日期/分数不变，具体差额深入；[TRAIN-DATA](../../../../books/part-04-training-system/27-data.md)11636后/20644前原三件真实SAVE/fullselfread，经root§131 sole实际POST通过，未核完整证明/全部图像素/实现或复现。

### [Decision-Weighted Flow Matching for Contextual Stochastic Optimization](https://arxiv.org/html/2606.16790v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：必要§94，root§132/133；同velocity label的endpoint重权改变条件target为E[wΔ|Y]/E[w|Y]。固定reference是proxy，fit/tilt/路径覆盖分责，不是importancecorrection或必降regret；保可微/正则条件、一步积分/有限CVaR与smoke非主运行、全部梯度/采样/solver费，不授金融/交通安全。原日期/分数不变，具体差额深入；[MULTIMODAL-GENERATIVE-PARADIGMS](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)基本FM条件均值后/31981前原三件真实SAVE/fullselfread，经root§133 sole实际POST通过，未核完整证明/全部图像素/实现或复现。

### [Unified Motion-Action Modeling for Heterogeneous Robot Learning](https://arxiv.org/html/2606.16917v1)

[本日有限必要与actualowner](../_sources/daily-20260617/SUP_NECESSARY_20261026.md)：必要§95，root§134/135；camera3Dmotion/action互换given/target，仅兼容label计actionloss，motiononly tasklatent适配仍借已有robot/sim动作知识。保新本体compatiblehead/标定、given仍调制/sharedattention、contrastive非纯intent、派生GT/20trial/失败内分母及15Hz非deadline和全费，不授精确joint、跨本体零数据或物理安全。原日期/分数不变，具体差额深入；[MULTIMODAL-EMBODIED-VLA](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)04009后/UniWALM前原三件真实SAVE/fullselfread，经root§135 sole实际POST通过，未核完整证明/全部图像素/实现或复现。

## 5. 缺口与下一步

本窗终态保留项：下述外部目录/日期缺口及五项中心争议均已隔离，不支持正面证据、Books采用、无遗漏断言或性能/安全保证；普通可执行工作为0。只有取得各项指定的当期原始目录、精确日期材料或可核更正时，才按下列定点重开条件恢复受影响项，不重跑全日或扩大来源。

本轮可执行研究工作：无。新增89家族已逐项闭合为74真实整合/10具体已有覆盖/5具名中心争议，普通必要、Books写入与唯一实际POST均为0；全部已验窄位释放。最后TDV15956、LowRank16045、DWFM16790、UMA16917分别经root§129/131/133/135实际POST通过；此前已成层依本日canonical复用，不第三审。整日报经root§136 DAY验收通过；以后仅在下述指定材料或更正到达时重开受影响项，不扩源或号段。

五项中心争议14883/14997/16541/16883/15897均有具名原件冲突、采用隔离与定点重开条件，见各§4；不入Books、不作正面Evidence/Coverage，不把普通未读改H，也不否定整份材料所有有限经验。它们与下列外部日期/目录范围为本窗保留项，不代替未完成研究归零。

已与普通工作隔离的外部范围：Google Publications、Meta连续历史Research及Moonshot 2026 Blog档案未恢复；已核博客/可见分页不补成这些范围的零发布或Coverage通过。各需目标日官方日级目录/历史快照重开，而非全站当前首页。BACON2606.14782v1与MMLongEmbed2606.14747v1有潜在贡献，但合法公告界分别跨Jun11–16、Jun08–16；作者项目/具名README或当前月列表未给精确v1公告日，本窗不评分、不进入确定候选/Books。重开只需当期arXiv公告/日列表或可核作者带日期正文档案；不将submitted、registered、repo创建或第三方日期单字段当公开日。具体已查入口见来源记录末段。Joy14777官网当前页自标June10，构成更早正文信号；June20 full release是另一事件，论文精确公开归属仍缺口。不认证June10历史逐字内容，不评分/本窗采用、不另开日期或新日报；重开仅当期公告或可核作者带日期的精确原稿/历史档案，既有root§36事实复用。

补充日期保留：14831 PlayingDead跨Jun15–16、14752 XTokenizer跨Jun09–16；已查精确ID/作者、具名项目/README，均无可用日级作者正文/当期公告。14721 DCMotion跨May29–Jun16、14723 Disagreement routing跨Jun02–16，有限精确检索只返回submitted/修订/第三方口径，亦不能缩成Jun16。均不评分/不列确定本日候选/不入Book，重开仅精确v1当期公告/日列表或作者dated原稿；各已有一次具名请求，不无限假想渠道。详情与原件见来源末节。

精确旧链恢复：原7项16332/17005/16494/15099/15405/15874/16364由root/Jun16唯一reader定点核旧retained原日期/原9；实际必要/原稿和真实Book POST均已root§10/12/34/37完成供旧owner复用，Jun17不重计。新发现15306/15345/16190也确为旧Jun16 retained（原June13/June13/June15，原9），由Jun16作者/reader继续必要与actual层，本日仅dup；15345不再算本日新候选。旧trace一行本身不证明正文已写。

## 6. 复核

补查原独立复核者为root，当时非README/Books作者，§136 DAY与§137终存的历史有效范围继续复用：74项新真实POST、10具体NC、5中心争议及具名旧链身份核；六项N分层样本与六决定点检查不冒全N复读。随后撤回纠错由root担任writer、不同角色`jun18_supp_author`作为唯一非writer，在§139确认真实移除及其余旧50整行/原日期分数和小时窗保护；不以root原签字自证root的新修复。当前139行＝有效旧50＋新增89；旧有效§4只去除已撤回依赖，其余不重写，不再声称完整旧51/旧§4逐字不变。记录与精确排除依据统一见[本日canonical §138–139](../_sources/daily-20260617/SUP_REVIEW_20261026.md)。当前V3与此次Report/Ch59限定diffcheck通过；原新增89实际POST及19目标章检查未因这项清理重做，机器不代语义或日级验收。

以下为撤回前的旧窗口审计历史，只在未失效范围复用，不代表当前仍有旧51项或被撤回的采用继续有效：

复核者：独立 fresh-context reviewer（非作者侧）

结论：通过

原复核重新检查 534=50 Candidate+484 audited Close、50 项 Books disposition（15 Integrate/35 Existing）、13 项本轮新增 binding 中属于本日的 8 项，以及两套 validator 与限定 diff。8/8 marker 均位于首个顶层 Review notes 前，正文均覆盖旧约束→机制→owner→trade-off/failure→fallback。不同 reviewer 又核对了 Z.ai 官方页的 `2026/06/16 16:00`、每四个稀疏层共享一个 indexer 的公开机制与证据限制，并对读 Ch22 `Sparse Attention 的两个 ownership 轴`；确认该增量属于 Existing Coverage，Books writeback queue 仍为 0。
