# Daily Research — 2026-04-21

**规范：** V3
**窗口：** 2026-04-20T09:00:00+08:00 ～ 2026-04-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-27T18:22:39+08:00

## 1. 结论

本日已按当前合同重建并通过独立日级验收，旧 V2.1 的完成标签、分母和 Books 断言均不继承。旧正文完整保存在 [原始报告副本](../_sources/daily-20260421/V2_1_README_BEFORE_V3.md)，有效证据没有删除。

原始身份库存是 1,260 条混合 OAI / 元数据恢复线索，不是当天新论文数量；577 条 v1 Updated 早于 UTC 01:00 也只是公开批次处理链线索。作者实际阅读十五批 **270 个完整题摘**，逐家族记录具体准入、关闭或最小消歧判断，见 [初筛记录](../_sources/daily-20260421/V3_SCREENING_NOTES.md)。这不是270个正式候选；最终候选分母为下述146家族，已通过非作者日级验收，未声称全库存摘要/全文已读。

必要方法/评价及最小消歧实际推进到175家族（含撤回、日期隔离和贡献关闭，并非175候选）。146项逐项终态对账：33真实整合、14已有覆盖、81仅报告、18窄争议保留，普通Books0。原有10项有效实际记录和本轮23项[root正文/相邻交接写后复核及最终日级验收](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)共同支持33项采用，source→owner提案本身不计整合。撤回、早发身份、日期与历史目录缺口继续具名处置，不因Books落实变为零更新。冻结分母146已通过最终非作者日级验收；不宣称全库存题摘/全文已读或全网零遗漏。

## 2. 来源覆盖

历史停点和 artifact 缺口不据网页可读或空响应宣称“无更新”。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [News RSS](https://openai.com/news/rss.xml) 1,230项，本窗 `2026-04-21T00:00:00Z` 企业Codex合作核心说明已读，采用/咨询/伙伴扩展前分母关闭 | 受阻 | Research/Index当前可读，但4月历史分页停点未闭；RSS不替代Research |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 原始publishedOn邻界04/14T13:01Z→04/22T14:12Z/14:27Z | 已检查 | 限官方公开研究目录，本窗无条目 |
| SRC-GOOGLE-AI | [Research Blog](https://research.google/blog/) 4月九条，ReasoningBank链接旧家族2509.25140，无已识别重要修订；[DeepMind page3](https://deepmind.google/blog/page/3/) 04/15→04/22跨窗 | 受阻 | [Publications](https://research.google/pubs/) 年度入口未形成历史日停点，不能据此说本窗零论文 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 无有效历史提取；Blog page1/2实际04/06、04/08→03/27 | 受阻 | Blog不替代Research历史目录，后者未闭 |
| SRC-QWEN | 官方研究页page_config静态60项+retrieval动态40项，04/18 10:00+08→04/22 10:00+08 | 受阻 | 可见研究目录无本窗条目；组织新仓库/重要release历史停点未闭 |
| SRC-DEEPSEEK | [官方主页](https://www.deepseek.com/) News04/24→12/01、Research06/24→02/25的可见邻界 | 受阻 | 研究目录已检查，GitHub artifact停点未闭 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 26条，所见最新2025-11-07 | 受阻 | 不能证明2026本窗完整目录；组织artifact停点未闭 |
| SRC-TENCENT-HUNYUAN | 官方POST publicList，pageNum1/pageSize100/renderType0，9/9；displayPublishTime邻界04/23→02/13 | 受阻 | 全部可见目录无本窗项；组织artifact停点未闭，不宣称未列原文不存在 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) 15条04/29→04/07→04/01；[release notes](https://docs.z.ai/release-notes/new-released) 06/16→04/07→02/12 | 受阻 | 可见目录无本窗项；组织artifact停点未闭 |
| SRC-BYTEDANCE-SEED | 官方get_article_list_v2，type1/count20/page_token20，header US；total242,next40，04/22→04/20→04/16；ID1635指向2604.18292；官方abs/项目页及仓库替代已定点核 | 受阻 | Agent-World目录仅日历日，项目页无精确首发，仓库公开说明为08/10；v1 Updated跨截点不单证定晚发。日期精确隔离，组织artifact历史停点未闭 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/) 首十项04/30→04/15→02/06→2025-11，停止于左边界之前 | 已检查 | 仅官方可见技术博客，不声称作者论文全覆盖 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) Paper八条06/29→03/13→02/03；Blog十四条没有充分历史日期 | 受阻 | Paper已检查；Blog日期与组织artifact停点未闭 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog) 十二条05/26→03/18、[CN](https://www.minimaxi.com/blog) 十三条04/27→03/18、[Agent Tech](https://agent.minimax.io/docs/techblog) 一条05/13 | 受阻 | 可见技术目录跨窗；组织artifact停点未闭 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html) +已有OAI/永久ID分配/v1 processing组合；宽库存只作主题查漏，270完整题摘的原有有限信号已逐家族裁决，175家族必要/最小处理 | 已检查 | 组合推断非submitted/Updated孤证；有具体更早正文或跨截点例外均具名隔离，不宣称全网无遗漏 |

八机构GitHub有界API各两次403，替代网页200只给lastUpdated与当前分页，没有created/重要release历史停止点；不能补造零更新。实际14源与首批15个完整题摘的作者外复核见 [独立有界审计](../_sources/daily-20260421/V3_SOURCE_ADMISSION_INDEPENDENT.md)。

## 3. 候选与判断

作者侧冻结146个候选家族，每项有必要证据与真实处置；最终独立复核若发现具体误收/漏收则定点重开，不继承旧101项。公开范围来自官方永久ID公告分配规则、相邻批界与本家族v1 processing/OAI组合，有限推断04/21早批08:00～09:00，不把submitted或Updated单证改名首发；例外单独隔离。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [BASIS: Balanced Activation Sketching with Invariant Scalars for "Ghost Backpropagation"](https://arxiv.org/html/2604.16324v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 激活sketch的dX/dW分离及范数校准改变梯度误差选择；2+1+2=5 | 深入完成 | 暂缓：中心方差最优保证争议，不写Books |
| [Cross-Family Speculative Decoding for Polish Language Models on Apple Silicon: An Empirical Evaluation of Bielik 11B with UAG-Extended MLX-LM](https://arxiv.org/html/2604.16368v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | cross-tokenizer/共享带宽的高acceptance反收益；2+2+2=6 | 标准完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)净成本/状态生命周期 |
| [Same Verdict, Different Reasons: LLM-as-a-Judge and Clinician Disagreement on Medical Chatbot Completeness](https://arxiv.org/html/2604.16383v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | completeness阈值与分流效用分离的受限反证；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)inventory/risk-coverage |
| [GraphRAG-Router: Learning Cost-Efficient Routing over GraphRAGs and LLMs with Reinforcement Learning](https://arxiv.org/html/2604.16401v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | GraphRAG-first与LLM-first受控顺序对照；2+1+2=5 | 标准完成 | 仅报告：固定组件池的窄控制顺序，不外推普遍最优 |
| [Functional Similarity Metric for Neural Networks: Overcoming Parametric Ambiguity via Activation Region Analysis](https://arxiv.org/pdf/2604.16426v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | activation-region模型匹配的canonical/stability保证需纠错；2+1+2=5 | 深入完成 | 暂缓：固定同hash签名距离的中心声明冲突，原方法经验不全否定 |
| [Beyond Feature Fusion: Contextual Bayesian PEFT for Multimodal Uncertainty Estimation](https://arxiv.org/html/2604.16615v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | global音频条件化Bayesian低秩latent而非head拼接；2+1+2=5 | 标准完成 | 仅报告：posterior机制可支持，AUC未证明错误概率校准 |
| [Cross-Modal Bayesian Low-Rank Adaptation for Uncertainty-Aware Multimodal Learning](https://arxiv.org/html/2604.16657v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | token/frame cross-attention条件化latent及shared-KV成本分支；2+1+2=5 | 标准完成 | 仅报告：与16615不同家族，局部AUC/MC成本不构成通用可靠性保证 |
| [How Robustly do LLMs Understand Execution Semantics?](https://arxiv.org/html/2604.16320v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | canonical高分与输入邻域/等价程序反证；2+1+2=5 | 标准完成 | 仅报告：限定原输入等价与宽松extraction，不证明内部世界模型 |
| [Steerable Instruction Following Coding Data Synthesis with Actor-Parametric Schema Co-Evolution](https://arxiv.org/pdf/2604.16322v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 可行witness/checker与难度actor分开的curriculum；2+1+2=5 | 标准完成 | 仅报告：有限checker不提供全程序语义保证，预算未完全分离 |
| [Benchmarking Real-Time Question Answering via Executable Code Workflows](https://arxiv.org/html/2604.16349v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | execution-time oracle与修复版本的动态评价对象；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)run/snapshot/repaired-harness边界 |
| [SaFeR-Steer: Evolving Multi-Turn MLLMs via Synthetic Bootstrapping and Feedback Dynamics](https://arxiv.org/html/2604.16358v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | prefix min/mean形成全轨迹reward的条件分支；2+2+2=6 | 标准完成 | 仅报告：历史shaping非因果credit或发布安全保证 |
| [CSF: Black-box Fingerprinting via Compositional Semantics for Text-to-Image Models](https://arxiv.org/pdf/2604.16363v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | query-only组合语义探针与归属频率区间；2+2+2=6 | 标准完成 | 仅报告：Beta投票比例不是identity posterior/OOD错误率 |
| [CoLLM: A Unified Framework for Co-execution of LLMs Federated Fine-tuning and Inference](https://arxiv.org/html/2604.16400v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | shadow/active adapter双缓冲和两时间尺度共执行；2+2+2=6 | 标准完成 | 仅报告：原子交换未证明整请求/KV版本一致性 |
| [GRAB-ANNS: High-Throughput Indexing and Hybrid Search via GPU-Native Bucketing](https://arxiv.org/html/2604.16402v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | scalar bucket×GPU graph布局与append更新；2+2+2=6 | 标准完成 | 仅报告：限定scalar-range与受限执行配置，不采用任意过滤导航保证 |
| [StressWeb: A Diagnostic Benchmark for Web Agent Robustness under Realistic Interaction Variability](https://arxiv.org/html/2604.16385v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | GUI规则/执行扰动与自报成功的独立结果分账；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)规则与观察对象配对、独立Outcome Witness |
| [Breaking Validity-Induced Boundaries to Expand Algorithm Search Space: A Two-Stage AST-Based Operator for LLM-Driven Automated Heuristic Evolution](https://arxiv.org/html/2604.16420v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | invalid AST种群对象→合法repair子程序fitness的搜索分支；2+1+2=5 | 标准完成 | 仅报告：有限heuristic任务，不采用合法搜索空间必然断裂/普遍逃逸保证 |
| [Measuring Representation Robustness in Large Language Models for Geometry](https://arxiv.org/html/2604.16421v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 等价表示评价的invariance/consistency对象及中心关系需纠错；2+1+2=5 | 深入完成 | 暂缓：同版PDF Table7与Property3矛盾，不采用其指标保证 |
| [ICAT: Incident-Case–Grounded Adaptive Testing for Physical-Risk Prediction in Embodied World Models](https://arxiv.org/html/2604.16405v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 可核风险初态×动作触发×严重后果的预测评价；2+1+2=5 | 标准完成 | 仅报告：grounded risk-chain诊断不是实际闭环安全认证 |
| [Matched-Learning-Rate Analysis of Attention Drift and Transfer Retention in Fine-Tuned CLIP](https://arxiv.org/html/2604.16410v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | matched-LR反证区分LoRA欠拟合与transfer保持；2+1+2=5 | 标准完成 | 仅报告：受限优化grid，attention drift非因果解释 |
| [Safety, Security, and Cognitive Risks in State-Space Models: A Systematic Threat Analysis with Spectral, Stateful, and Capacity Attacks](https://arxiv.org/pdf/2604.16424v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | SSM时变transfer平均扩展的保证与pilot证据范围需纠错；2+1+2=5 | 深入完成 | 暂缓：平均transfer不能直接承接LTI界，不采用预训练安全保证 |
| [Dimensional Criticality at Grokking Across MLPs and Transformers](https://arxiv.org/html/2604.16431v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 快照avalanche/FSS与shadow-probe的受限泛化诊断；2+1+2=5 | 标准完成 | 仅报告：事后g对齐与无split XOR不构成部署早停门禁 |
| [Sampling for Quality: Training-Free Reward-Guided LLM Decoding via Sequential Monte Carlo](https://arxiv.org/html/2604.16453v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 形式sequence target与混合SMC/MH实现保证须分账；2+2+2=6 | 深入完成 | 暂缓：整体target/MC状态保持未建立，不正面写Books |
| [EchoChain: A Full-Duplex Benchmark for State-Update Reasoning Under Interruptions](https://arxiv.org/html/2604.16456v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | onset固定中断与配对half-duplex分离状态改写；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)uptake/旧约束/目标与配对更新 |
| [B-PASTE: Beam-Aware Pattern-Guided Speculative Execution for Resource-Constrained LLM Agents](https://arxiv.org/html/2604.16469v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 单工具推测改为有状态分支的效用/干扰调度；2+2+2=6 | 标准完成 | 仅报告：具体方案可描述，完整评价与非干扰保证尚未验证 |
| [Semantic Channel Theory: Deductive Compression and Structural Fidelity for Multi-Agent Communication](https://arxiv.org/html/2604.16471v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 有限知识库closure保真与异构proxy条件需要区分；2+1+2=5 | 深入完成 | 暂缓：仅隔离Remark5.16单proxy存在性保证，强H1定理未随之否定 |
| [Spike-driven Large Language Model](https://arxiv.org/html/2604.16475v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 整数count展开为稀疏脉冲累加的表示/执行取舍；2+2+2=6 | 标准完成 | 仅报告：理论算术能耗不是实测Serving节能，质量与展开成本保留 |
| [Dynamic Eraser for Guided Concept Erasure in Diffusion Models](https://arxiv.org/html/2604.16483v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | feature-anchor触发的闭式校正改变runtime保护行为；2+2+2=6 | 深入完成 | 仅报告：二次surrogate最优不等语义安全，保留benign drift |
| [DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks](https://arxiv.org/html/2604.16484v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 真实观测TTT与预测working state分离、执行期间预denoise；2+2+2=6 | 标准完成 | 仅报告：固定state不证明无界可靠，换条件稳定性未建立 |
| [Geometry-Aware CLIP Retrieval via Local Cross-Modal Alignment and Steering](https://arxiv.org/pdf/2604.16487v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | annotation条件下object matching与局部steering的组合反证；2+1+2=5 | 标准完成 | 仅报告：Hungarian/FGW排序与语义真值分权，不采用结构term普优 |
| [LayerCache: Exploiting Layer-wise Velocity Heterogeneity for Efficient Flow Matching Inference](https://arxiv.org/html/2604.16492v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | timestep×layer-group×JVP span的刷新预算分配；2+2+2=6 | 标准完成 | 仅报告：具体schedule分支，预算/速度对照不足以证明全Pareto支配 |
| [Positive-Only Drifting Policy Optimization](https://arxiv.org/html/2604.16519v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | positive-advantage action drift及中心噪声/梯度解释需纠错；2+2+2=6 | 深入完成 | 暂缓：RV方向、协方差与完整target stopgrad未澄清，不正面采用 |
| [CAMP: Cumulative Agentic Masking and Pruning for Privacy Protection in Multi-Turn LLM Conversations](https://arxiv.org/pdf/2604.16521v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | session累计PII与retroactive masking的泄漏对象需纠错；2+2+2=6 | 深入完成 | 暂缓：未来history改写不清除已发API logs，不能采用累计零暴露 |
| [Anumati: Proof of Adherence as a Formal Consent Model for Autonomous Agent Protocols](https://arxiv.org/html/2604.16524v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | version/hash/capability绑定的per-clause consent与skill gating；2+2+2=6 | 深入完成 | 仅报告：模型内生命周期保证不证明实际理解/遵从，现效应authority不改变 |
| [SCATR: Simple Calibrated Test-Time Ranking](https://arxiv.org/html/2604.16535v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | model/domain-specific hidden-state scorer与BoN质量/选择成本分账；2+1+2=5 | 标准完成 | 仅报告：scorer局部延迟不等总多采样推理成本，有限校准不可自证真值 |
| [LLM as a Tool, Not an Agent: Code-Mined Tree Transformations for Neural Architecture Search](https://arxiv.org/html/2604.16555v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 算法粗搜索与LLM残余决策的受限对照；2+1+2=5 | 标准完成 | 仅报告：小图像NAS条件，不采用算法挖掘100%正确/更大LLM必更差 |
| [S-GRPO: Unified Post-Training for Large Vision-Language Models](https://arxiv.org/html/2604.16557v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 全失败组GT替换与mixed sampling目标一致性；2+2+2=6 | 深入完成 | 暂缓：专家确定性注入不能沿πold纯on-policy保证，不否定全部bootstrap经验 |
| [Conjunctive Prompt Attacks in Multi-Agent LLM Systems](https://arxiv.org/html/2604.16543v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 独立benign片段×路由合流的组合激活评价；2+2+2=6 | 深入完成 | 仅报告：marker激活不是独立特权效果，保留router控制与授权边界 |
| [Reasoning on the Manifold: Bidirectional Consistency for Self-Verification in Diffusion Language Models](https://arxiv.org/html/2604.16565v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | mask/reconstruct稳定性作为conditional selector；2+2+2=6 | 标准完成 | 仅报告：同源稳定性非truth，RL仍需要GT correctness gate |
| [EquivFusion: Unifying Hardware Equivalence Checking from Algorithms to Netlists via MLIR](https://arxiv.org/html/2604.16571v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | common IR miter的跨抽象verification对象与位宽边界；2+2+2=6 | 标准完成 | 仅报告：integer/static subset工具，不作全LLM浮点正确性保证 |
| [On the Robustness of LLM-Based Dense Retrievers: A Systematic Analysis of Generalizability and Stability](https://arxiv.org/html/2604.16576v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 几何相关性与正则/attention转换干预的鲁棒性反证；2+1+2=5 | 标准完成 | 仅报告：有限英语模型/扰动协议，不建立通用encoder因果目标 |
| [Certified Program Synthesis with a Multi-Modal Verifier](https://arxiv.org/html/2604.16584v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | spec验证与证明模式分工的预算/参考缺陷受限证据；2+1+2=5 | 标准完成 | 仅报告：形式spec证明不替代NL意图、有限PBT或端到端成本 |
| [The Global Neural World Model: Spatially Grounded Discrete Topologies for Action-Conditioned Planning](https://arxiv.org/html/2604.16585v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | topological训练加grid-snap的离散rollout责任分支；2+1+2=5 | 标准完成 | 仅报告：保持锐度不保证物理转移/开放因果发现，有限可行条件不外推 |
| [Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning](https://arxiv.org/html/2604.16591v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | gradient检索两集合与归一化sketch保证的责任分离；2+2+2=6 | 深入完成 | 暂缓：归一化cosine无偏/MSE保证缺桥，不否定全部检索经验 |
| [Spotlights and Blindspots: Evaluating Machine-Generated Text Detection](https://arxiv.org/html/2604.16607v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | novel-human、类别比例与阈值选择的受限排序反证；2+1+2=5 | 标准完成 | 仅报告：有限检测配置，不推开放来源归属可靠性 |
| [Lower Bounds and Proximally Anchored SGD for Non-Convex Minimization Under Unbounded Variance](https://arxiv.org/html/2604.16620v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 距初始化增长的方差约束改变batch/anchor与oracle复杂度；2+1+2=5 | 标准完成 | 仅报告：条件理论而非Transformer优化器/真实运行时保证 |
| [Agentic Frameworks for Reasoning Tasks: An Empirical Study](https://arxiv.org/html/2604.16646v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 有限共同配置下context/retry失控的运行证据；2+1+2=5 | 标准完成 | 仅报告：跨题库分母及控制混杂不支持框架因果排名 |
| [Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs](https://arxiv.org/html/2604.16659v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 冻结音频encoder后语义/声学选样与模态路径仍改变安全；2+2+2=6 | 深入完成 | 仅报告：具体安全反证，架构因果/普遍修复未建立 |
| [Rewind-IL: Online Failure Detection and State Respawning for Imitation Learning](https://arxiv.org/html/2604.16683v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | chunk一致性触发与恢复action/queue/slot状态分开；2+2+2=6 | 深入完成 | 仅报告：有限物理恢复实例，不把旧action重放当精确state复位 |
| [DARLING: Detection Augmented Reinforcement Learning with Non-Stationary Guarantees](https://arxiv.org/html/2604.16684v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 强制探测与episode边界reset的可检测性约束；2+1+2=5 | 标准完成 | 仅报告：reachability/分段长度条件理论，非开放Agent保证 |
| [Evaluating Tool-Using Language Agents: Judge Reliability, Propagation Cascades, and Runtime Mitigation in AgentProp-Bench](https://arxiv.org/html/2604.16706v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | stage与judge分账的评价反证及中心统计外推需纠错；2+2+2=6 | 深入完成 | 暂缓：不显著相关不证明独立，同judge不自动抵消干预偏差 |
| [How to Approximate Inference with Subtractive Mixture Models](https://arxiv.org/html/2604.16714v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 合法signed密度与期望差估计分开、抵消增加方差；2+1+2=5 | 标准完成 | 仅报告：条件近似推断分支，不作为现代模型采样通用方案 |
| [Scalable and Adaptive Parallel Training of Graph Transformer on Large Graphs](https://arxiv.org/html/2604.16715v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 稀疏节点AG与head-A2A的graph/activation复制成本分离；2+2+2=6 | 标准完成 | 仅报告：具体稀疏训练路线，非dense causalLM普遍最优 |
| [Active World-Model with 4D-informed Retrieval for Exploration and Awareness](https://arxiv.org/html/2604.16733v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | query-local动静态支持与生成观察的事实边界；2+2+2=6 | 标准完成 | 仅报告：有限camera代理配方，不作为物理transition或闭环policy保证 |
| [Reducing Peak Memory Usage for Modern Multimodal Large Language Model Pipelines](https://arxiv.org/html/2604.16734v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | prefill内append/evict的瞬态峰值与质量延迟分账；2+1+2=5 | 标准完成 | 仅报告：局部有用配方，不能推广严格M峰值/普遍minimal loss |
| [Why Training-Free Token Reduction Collapses: The Inherent Instability of Pairwise Scoring Signals](https://arxiv.org/html/2604.16745v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 信号选择/反馈失真中心理论的必要条件纠错；2+2+2=6 | 深入完成 | 暂缓：单调非减不足推出超线性，不否定具体CATIS经验 |
| [Don't Start What You Can't Finish: A Counterfactual Audit of Support-State Triage in LLM Agents](https://arxiv.org/html/2604.16752v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | typed deferral与scalar confidence的首动作诊断；2+1+2=5 | 标准完成 | 仅报告：同会话gold泄漏，不推真实部署分类/内部自知保证 |
| [StageMem: Lifecycle-Managed Memory for Language Models](https://arxiv.org/html/2604.16774v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | confidence准入与strength保留深度的压力控制分解；2+1+2=5 | 标准完成 | 仅报告：控制harness的具体机制，不推生产长期可靠性 |
| [When Informal Text Breaks NLI: Tokenization Failure, Distribution Shift, and Targeted Mitigations](https://arxiv.org/html/2604.16787v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | UNK丢失与in-vocabulary噪声的差异干预；2+1+2=5 | 标准完成 | 仅报告：有限词表/变换及额外训练预算，不推普遍语义保持 |
| [LongBench: Evaluating Robotic Manipulation Policies on Real-World Long-Horizon Tasks](https://arxiv.org/html/2604.16788v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 可观测长执行与历史歧义分开的受限memory反证；2+1+2=5 | 标准完成 | 仅报告：不同任务/policy比较，不作memory开关因果保证 |
| [Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering](https://arxiv.org/html/2604.16790v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 相同代码的presentation/判定程序改变与judge稳定性分账；2+1+2=5 | 标准完成 | 仅报告：有限代码judge反证，不推全部排名稳定或反转 |
| [Continuous Limits of Coupled Flows in Representation Learning](https://arxiv.org/html/2604.16801v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 谱隙/非零投影到完整主rowspace的理论桥需纠错；2+1+2=5 | 深入完成 | 暂缓：rank保留反例限制alignment保证，不否定所有流分析 |
| [A Mechanism Study of Delayed Loss Spikes in Batch-Normalized Linear Models](https://arxiv.org/pdf/2604.16809v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | norm/scale/方向的effective LR反馈造成受限晚发spike；2+1+2=5 | 标准完成 | 仅报告：白化线性BN条件，不推现代Transformer训练普遍保证 |
| [SafeDream: Safety World Model for Proactive Early Jailbreak Detection](https://arxiv.org/html/2604.16824v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 累积风险与灰区双池latent预测用于提前保护；2+2+2=6 | 深入完成 | 仅报告：单backbone拒绝cone与共享labelers的安全原型，不采用最优或生产保证 |
| [The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Distillation](https://arxiv.org/html/2604.16830v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 特权teacher成功率与无特权部署student的识别桥需核；2+2+2=6 | 深入完成 | 暂缓：中心joint概率与不同generation-policy对应缺桥，经验协议仍保留 |
| [Towards Deep Encrypted Training: Low-Latency, Memory-Efficient, and High-Throughput Inference for Privacy-Preserving Neural Networks](https://arxiv.org/html/2604.16834v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | downsample空slots的密文accumulator与stage key驻留；2+1+2=5 | 标准完成 | 仅报告：HE-friendly CNN执行配方，不当encrypted training或LLM低时延保证 |
| [DART: Mitigating Harm Drift in Difference-Aware LLMs via Distill-Audit-Repair Training](https://arxiv.org/html/2604.16845v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | label正确与rationale副产物的paired audit/repair分离；2+2+2=6 | 深入完成 | 仅报告：明确transductive repair范围，不采用独立heldout或普遍安全结论 |
| [Refinement of Accelerated Demonstrations via Incremental Iterative Reference Learning Control for Fast Contact-Rich Imitation Learning](https://arxiv.org/html/2604.16850v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 逐速reference warm-start与tracking反馈修复加速示范；2+1+2=5 | 标准完成 | 仅报告：有限接触任务/ACT控制实例，不推一般高速VLA安全 |
| [When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization](https://arxiv.org/html/2604.16855v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 共享range使弱边界zeroization及token-group约束；2+1+2=5 | 标准完成 | 仅报告：QDQ模拟质量分支，不推原生INT4或LLM端到端收益 |
| [Governed MCP: Kernel-Level Tool Governance for AI Agents via Logit-Based Safety Primitives](https://arxiv.org/html/2604.16870v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 强制kernel入口与semantic gate可靠性分账；2+2+2=6 | 深入完成 | 仅报告：WASM/host假设与有限作者labels，不是完整MCP安全证书 |
| [PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations](https://arxiv.org/html/2604.16909v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | reasoning SFT跨维收益/退化的受限反证；1+2+2=5 | 标准完成 | 已有覆盖：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)匹配轨迹、目标/retain切片与能力回退 |
| [The Cognitive Penalty: Ablating System 1 and System 2 Reasoning in Edge-Native SLMs for Decentralized Consensus](https://arxiv.org/html/2604.16913v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 同权重think切换的invalid/时延反收益；1+2+2=5 | 标准完成 | 仅报告：21提案局部配对，不推内部知识真值或System1普遍安全 |
| [x1: Learning to Think Adaptively Across Languages and Cultures](https://arxiv.org/html/2604.16917v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | language trajectory选择/训练与知识边界分账；1+2+2=5 | 标准完成 | 仅报告：受限双阶段recipe，gold选择与训练预算不证明固定知识或跨语言普律 |
| [Noise-Adaptive Diffusion Sampling for Inverse Problems Without Task-Specific Tuning](https://arxiv.org/html/2604.16919v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | noise-space生成与accepted-only控制流采样保证的冲突；2+1+2=5 | 争议 | 暂缓：Alg1拒绝后缩步直到接受，缺对应posterior-invariant transition证明 |
| [Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy](https://arxiv.org/html/2604.16923v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | base/aligned分布差与检测统计/条件理论分账；1+2+2=5 | 标准完成 | 仅报告：具体统计与受限slice，不是一般作者身份或无条件ROC保证 |
| [No One Fits All: From Fixed Prompting to Learned Routing in Multilingual LLMs](https://arxiv.org/html/2604.16937v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | native/translate双生成后选择的语言×任务条件；1+2+2=5 | 标准完成 | 仅报告：response selector不是低成本生成前路由，因果与部署成本未证 |
| [Better with Less: Tackling Heterogeneous Multi-Modal Image Joint Pretraining via Conditioned and Degraded Masked Autoencoder](https://arxiv.org/html/2604.16952v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 条件化loss对象与跨传感器重建信息的受限分支；2+1+2=5 | 标准完成 | 仅报告：保留目标/残差机制，不将领域配方或梯度屏蔽宣传采为普遍结论 |
| [Open-TQ-Metal: Fused Compressed-Domain Attention for Long-Context LLM Inference on Apple Silicon](https://arxiv.org/html/2604.16957v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | int4 KV融合执行及角度误差中心保证的受限纠错；2+2+2=6 | 深入完成 | 仅报告：执行路径可用，普遍score误差/跨层保证缺条件，不写Books宣传 |
| [Training for Compositional Sensitivity Reduces Dense Retrieval Generalization](https://arxiv.org/html/2604.16351v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 结构负例训练的目标域收益/跨域代价与near-miss拒绝；2+2+2=6 | 深入完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)hard-negative域迁移与relevance≠support |
| [NWCAD](https://arxiv.org/html/2604.16686v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 同当前prefix条件下显式token回退与持续contrastive tilt分流；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)prior/context gate，真实写后已独立通过 |
| [TensorHub](https://arxiv.org/html/2604.17104v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | bit sketch/ratio预测/新base成本共同决定物理存储规划；2+2+2=6 | 深入完成 | 整合：`PLATFORM-MODEL-REGISTRY` [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md)逻辑身份与physical layout分层，真实写后已独立通过 |
| [Annotation Entropy Predicts Per-Example Learning Dynamics in LoRA Fine-Tuning](https://arxiv.org/html/2604.16332v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | item分歧、rank与loss验收分账；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)，真实写后独立通过 |
| [Stream2LLM: Overlap Context Streaming and Prefill for Reduced TTFT](https://arxiv.org/html/2604.16395v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | arrival分析/资源分配分权与LCP后缀失效；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，真实写后独立通过 |
| [POLAR: Online Learning for LoRA Adapter Caching and Routing in Edge LLM Serving](https://arxiv.org/html/2604.16583v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 质量路由与residency内生反馈/cold probe；2+2+2=6 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，真实写后独立通过 |
| [Crowded in B-Space: Calibrating Shared Directions for LoRA Merging](https://arxiv.org/html/2604.16826v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | B谱premerge与gauge-sensitive proxy边界；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)，真实写后独立通过 |
| [D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation](https://arxiv.org/html/2604.16940v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | sunk FullFT后sign/residual SVD资产压缩；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)，真实写后独立通过 |
| [In-Context Learning Under Regime Change](https://arxiv.org/html/2604.16988v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 变点条件下prefix统计/候选切分与head资源分支；2+1+2=5 | 标准完成 | 仅报告：有条件构造，不作GD学习或一般变化点恢复保证 |
| [SPS](https://arxiv.org/html/2604.16995v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | rollout分布重塑的中心目标与算法方向须纠错；2+2+2=6 | 深入完成 | 暂缓：负forward KL与minimize不一致，需目标/实现必要说明 |
| [Utility-Preserved Speech Anonymization](https://arxiv.org/html/2604.17000v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 匿名化数据再训练用途与攻击知识条件改变隐私评价；2+1+2=5 | 深入完成 | 仅报告：声纹/内容PII分账，不作开放匿名性或不可逆保证 |
| [Semantic Equivalence Self-Play](https://arxiv.org/html/2604.17010v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 生成标签先经等价proof或非等价witness验证，再训练evaluator；2+1+2=5 | 标准完成 | 仅报告：受限Haskell/验证吞吐分支，不作全代码语义保证 |
| [Mini-BEHAVIOR-Gran](https://arxiv.org/html/2604.17019v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 同场景instruction粒度×语言必要性与成功率反弹分账；2+1+2=5 | 标准完成 | 仅报告：离散任务受限反证，不推真机或通用U形规律 |
| [When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano](https://arxiv.org/html/2604.17040v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 稀疏activation未降低实际launch/执行工作；2+1+2=5 | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)执行路径/稀疏硬件消费 |
| [SIF: Semantically In-Distribution Fingerprints for Large Vision-Language Models](https://arxiv.org/html/2604.17041v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 冻结LVLM的输入水印distillation/黑盒反指纹与校准边界；2+2+2=6 | 深入完成 | 仅报告：有限calibration max不保证总体零FP，ownership sensor非证明 |
| [RLM-on-KG: Heuristics First, LLMs When Needed](https://arxiv.org/html/2604.17056v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 共现图探索与排序分流的条件质量/成本反证；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)typed检索state/探索排序/静态fallback |
| [Sarus Suite: Cloud-native Containers for HPC](https://arxiv.org/html/2604.17064v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | scheduler/namespace/site-hook/image职责分层与实测条件；2+2+2=6 | 标准完成 | 仅报告：具体HPC integration不推广全AI平台runtime |
| [Trajectory-Restricted Optimization Conditions and Geometry-Aware Linear Convergence](https://arxiv.org/html/2604.17067v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 访问集合限制的PL/EB与tail-rate条件；2+1+2=5 | 标准完成 | 仅报告：trajectory containment不是自动识别或Transformer收敛保证 |
| [Stability-Weighted Decoding for Diffusion Language Models](https://arxiv.org/html/2604.17068v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | temporal KL下界被用作依赖安全预算上界，中心桥须纠错；2+2+2=6 | 深入完成 | 暂缓：小KL不排除剩余依赖，且算法KL方向与理论不同 |
| [Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL](https://arxiv.org/html/2604.17073v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 可回答惩罚/拒答/关键缺失澄清reward分权；2+1+2=5 | 标准完成 | 仅报告：reference语义匹配不证明开放事实可靠或概率校准 |
| [Understanding and Enforcing Weight Disentanglement in Task Arithmetic](https://arxiv.org/html/2604.17078v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 内部正交惩罚到任务间独立随机条件的保证桥；2+2+2=6 | 深入完成 | 暂缓：保留独立均匀零均值/TFS/CLIP；集中及绝对cosine与优化采样桥未证，但惩罚不建立跨任务独立性 |
| [EvoComp: Learning Visual Token Compression for Multimodal Large Language Models via Semantic-Guided Evolutionary Labeling](https://arxiv.org/html/2604.17087v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | gold-response离线标签搜索与非特权compressor部署分权；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)；具体机制已入正文，root实际写后通过 |
| [HarmChip: Evaluating Hardware Security Centric LLM Safety via Jailbreak Benchmarking](https://arxiv.org/html/2604.17093v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | hardware安全语言响应、筛难度与实际effect验证分账；1+2+2=5 | 深入完成 | 仅报告：单judge/选择分母不证明可制造攻击或普遍安全排行 |
| [From Natural Language to Silicon: The Representation Bottleneck in LLM Hardware Design](https://arxiv.org/html/2604.17097v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | IR/lowering/testbench/FPGA目标与幸存者分母分账；1+2+2=5 | 标准完成 | 仅报告：具体NL→hardware受限协议，不外推IR永久排名/芯片现实效果 |
| [Configuration Over Selection: Hyperparameter Sensitivity Exceeds Model Differences in Open-Source LLMs for RTL Generation](https://arxiv.org/html/2604.17102v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 默认decoder与task-tuned selection预算不是同一对象；1+2+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)完整对象、预算诱发上界和pipeline分账 |
| [Latent-Compressed Variational Autoencoder for Video Diffusion Models](https://arxiv.org/html/2604.16479v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 训练期频带支持与decoder适配改变codec身份；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)训练支持与部署过滤分支 |
| [From Inheritance to Saturation: Disentangling the Evolution of Visual Redundancy for Architecture-Aware MLLM Inference Acceleration](https://arxiv.org/html/2604.16462v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 视觉更新与视觉读取责任分离、backbone反向结果；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)更新/读取分账 |
| [Motif-Video 2B: Technical Report](https://arxiv.org/html/2604.16503v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 零输出初始化与跨注意力KV投影兼容责任不同；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)Fusion接口分支 |
| [HiveMind: OS-Inspired Scheduling for Concurrent LLM Agent Workloads](https://arxiv.org/html/2604.17111v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | API集中重试与准入组合的受限恢复消融；1+2+2=5 | 标准完成 | 仅报告：mock不证明云端或全AgentRun恢复保证 |
| [Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification](https://arxiv.org/html/2604.17112v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | self/cross similarity分解与共同错误盲区；2+2+2=6 | 标准完成 | 仅报告：有限估计器非真实概率分解，成本与slice反例保留 |
| [Prompt Sensitivity in Vision-Language Grounding: How Small Changes in Wording Affect Object Detection](https://arxiv.org/html/2604.17126v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 固定proposal下选择变化与等价语义/质量分母分账；2+1+2=5 | 标准完成 | 仅报告：PCA不是selector唯一因果或总体质量证明 |
| [Please refuse to answer me! Mitigating Over-Refusal in Large Language Models via Adaptive Contrastive Decoding](https://arxiv.org/html/2604.17132v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | prompt contrast的保护行为与greedy/概率身份分离；2+2+2=6 | 深入完成 | 仅报告：signed score可greedy但非合法概率，不采用保持安全保证 |
| [The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration](https://arxiv.org/html/2604.17139v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 共享前缀轮转与相关污染下的保护边界；2+2+2=6 | 深入完成 | 仅报告：条件收缩模型不证明实际LLM真值收敛，保留失败与切换成本 |
| [SeekerGym: A Benchmark for Reliable Information Seeking](https://arxiv.org/html/2604.17143v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | corpus-relative覆盖分母与离线/在线校准分权；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)Inventory与覆盖假设 |
| [Negative Momentum for Convex-Concave Optimization](https://arxiv.org/html/2604.17145v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 交替梯度和负momentum的条件性收敛分支；2+1+2=5 | 标准完成 | 仅报告：确定凸凹条件/平均梯度结论不外推LLM或训练wall-clock |
| [ScenarioControl: Vision-Language Controllable Vectorized Latent Scenario Generation](https://arxiv.org/html/2604.17147v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 密集控制到稀疏scene tokens的双分支conditioning；2+1+2=5 | 标准完成 | 仅报告：受限条件生成对照不建立真实transition或通用注意力首选 |
| [Systematic Capability Benchmarking of Frontier Large Language Models for Offensive Cyber Tasks](https://arxiv.org/html/2604.17159v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 环境×提示方向翻转与非对称角色成本反证；2+2+2=6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)subject/harness/environment身份 |
| [CCCL: In-GPU Compression-Coupled Collective Communication](https://arxiv.org/html/2604.17172v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 局部无损编码下沉collective的实现与allreduce反收益；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)codec/overlap/端到端验收 |
| [Decomposing the Depth Profile of Fine-Tuning](https://arxiv.org/html/2604.17177v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 等化逐层相对更新的depth诊断与功能影响不同；2+1+2=5 | 标准完成 | 仅报告：受限表示干预不形成可靠layer-placement处方 |
| [BranchBench: Aligning Database Branching with Agentic Demands](https://arxiv.org/html/2604.17180v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | branch creation与query execution capacity的预算反向取舍；2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)；具体机制已入正文，root实际写后通过 |
| [Layer-wise MoE Routing Locality under Shared-Prefix Code Generation: Token-Identity Decomposition and Compile-Equivalent Fork Redundancy](https://arxiv.org/html/2604.17182v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | token/context分层画像不证明expert输出可exact共享；2+2+2=6 | 标准完成 | 已有覆盖：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)router语义与sharing proposal分权 |
| [React-ing to Grace Hopper 200: Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend](https://arxiv.org/html/2604.17187v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 推理标记混入文件路径的具体parser失效；1+2+2=5 | 标准完成 | 仅报告：受限interop反例不证明模型排名或普遍修复 |
| [Partitioning Unstructured Sparse Tensor Algebra for Load-Balanced Parallel Execution](https://arxiv.org/pdf/2604.17198v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | sparse coiteration访问cost与dense坐标分区责任不同；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)；具体机制已入正文，root实际写后通过 |
| [Demystifying the unreasonable effectiveness of online alignment methods](https://arxiv.org/html/2604.17207v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | reward-selector 与 soft-policy regret 的评价对象分离；2+1+2=5 | 标准完成 | 仅报告：强 gap/精确 ERM 条件结果不作 LLM 成本保证 |
| [Guardrails in Logit Space: Safety Token Regularization for LLM Alignment](https://arxiv.org/html/2604.17210v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | frozen-base 选择性 logit 锚与序列安全分权；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体机制已入正文，root实际写后通过 |
| [EmbodiedHead: Real-Time Listening and Speaking Avatar for Conversational Agents](https://arxiv.org/html/2604.17211v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 以音频 provenance 替代非因果双流 look-ahead；2+2+2=6 | 标准完成 | 仅报告：受限 motion 路由不升级语义 uptake/完整对话 SLO |
| [Continual Safety Alignment via Gradient-Based Sample Selection](https://arxiv.org/html/2604.17215v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | median-gradient 选择改变监督支持而非全部更新 clipping；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体机制已入正文，root实际写后通过 |
| [PAC-Bayes Bounds for Gibbs Posteriors via Singular Learning Theory](https://arxiv.org/html/2604.17219v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 后验平均风险与 RLCT/population integral 的条件复杂度；2+1+2=5 | 标准完成 | 仅报告：不作 SGD/Transformer 可计算发布证书 |
| [Bilinear Input Modulation for Mamba: Koopman Bilinear Forms for Memory Retention and Multiplicative Computation](https://arxiv.org/html/2604.17221v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | state-input/selectivity 两路径与 scan-compatible 替代的职责分离；2+2+2=6 | 标准完成 | 仅报告：受限动力学对照，不作普遍 SSM/语言模型选型 |
| [Revisiting Auxiliary Losses for Conditional Depth Routing: An Empirical Study](https://arxiv.org/html/2604.17228v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | future-policy oracle 与 gate 实际预算错位的受控反证；2+2+2=6 | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)；具体机制已入正文，root实际写后通过 |
| [HeadRank: Decoding-Free Passage Reranking via Preference-Aligned Attention Heads](https://arxiv.org/html/2604.17237v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | preference-aligned attention 读出与执行截层的联合责任；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)；具体机制已入正文，root实际写后通过 |
| [DORA Explorer: Improving the Exploration Ability of LLMs Without Training](https://arxiv.org/html/2604.17244v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | token 随机性与整 action 探索控制的受限对照；2+2+2=6 | 标准完成 | 仅报告：序列 proxy 不作环境 uncertainty 或普适探索保证 |
| [VIBE: Voice-Induced open-ended Bias Evaluation for Large Audio-Language Models via Real-World Speech](https://arxiv.org/html/2604.17248v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 开放真实语音生成与 MCQ 偏差测量对象的区别；2+1+2=5 | 标准完成 | 仅报告：条件分布偏移非全部公平性/声学因果保证 |
| [Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining](https://arxiv.org/html/2604.16391v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 无动作标签 forward/inverse 预训练与丢重建 decoder 的适配责任；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；具体机制已入正文，root实际写后通过 |
| [Shifting the Gradient: Understanding How Defensive Training Methods Protect Language Model Integrity](https://arxiv.org/html/2604.16423v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 训练 forward trait-vector 与输入 prompt 的梯度职责分离；2+2+2=6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)；具体机制已入正文，root实际写后通过 |
| [Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models](https://arxiv.org/html/2604.16481v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 主动扰动基座与擦除模块恢复的 artifact 依赖；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体机制已入正文，root实际写后通过 |
| [BARD: Bridging AutoRegressive and Diffusion Vision-Language Models Via Highly Efficient Progressive Block Merging and Stage-Wise Distillation](https://arxiv.org/html/2604.16514v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | AR next-token 与同位置腐化状态蒸馏的支持身份；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)；具体机制已入正文，root实际写后通过 |
| [Real-Time Visual Attribution Streaming in Thinking Model](https://arxiv.org/html/2604.16587v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 离线视觉干预标签摊销成异步 span sensor；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体机制已入正文，root实际写后通过 |
| [Defragmenting Language Models: An Interpretability-based Approach for Vocabulary Expansion](https://arxiv.org/html/2604.16656v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | item 选择与初始化/added-token 匹配责任联验；2+2+2=6 | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)；具体机制已入正文，root实际写后通过 |
| [KAIROS: Stateful, Context-Aware Power-Efficient Agentic Inference Serving](https://arxiv.org/html/2604.16682v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 降频、Agent寿命与context驻留重算的反馈链；2+2+2=6 | 深入完成 | 整合：`PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)；具体机制已入正文，root实际写后通过 |
| [Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://arxiv.org/html/2604.16812v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 跨behavior-adapter变体训练报告sensor的身份；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体机制已入正文，root实际写后通过 |
| [HieraSparse: Hierarchical Semi-Structured Sparse KV Attention](https://arxiv.org/html/2604.16864v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | dense/semi-structured KV 与阶段重压缩的格式身份；2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；具体机制已入正文，root实际写后通过 |
| [Symphony: Taming Step Misalignments in the Network for Ring-based Collective Operations](https://arxiv.org/html/2604.16880v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | switch进度proxy的额外ECN与真实归约分权；2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)；具体机制已入正文，root实际写后通过 |
| [SinkRouter: Sink-Aware Routing for Efficient Long-Context Decoding in Large Language and Multimodal Models](https://arxiv.org/html/2604.16883v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 本轮KV跳读与缓存驻留保留的责任分离；2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)；具体机制已入正文，root实际写后通过 |
| [When Choices Become Risks: Safety Failures of Large Language Models under Multiple-Choice Constraints](https://arxiv.org/html/2604.16916v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 全不安全候选与候选外拒绝/有害协助的独立分母；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体机制已入正文，root实际写后通过 |
| [Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning](https://arxiv.org/html/2604.16918v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | priority寿命、采样IS与behavior-ratio三对象；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；具体机制已入正文，root实际写后通过 |
| [Different Perspectives of Memory System Simulation](https://arxiv.org/html/2604.16965v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 组件时钟换算与依赖请求因果提交分账；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；具体机制已入正文，root实际写后通过 |
| [On Safety Risks in Experience-Driven Self-Evolving Agents](https://arxiv.org/html/2604.16968v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 固定backbone良性外部经验读取的行为安全切片；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；具体机制已入正文，root实际写后通过 |
| [MCPO: Mastery-Consolidated Policy Optimization for Large Reasoning Models](https://arxiv.org/html/2604.16972v1) | 2026-04-21T08:00:00+08:00 ～ 2026-04-21T09:00:00+08:00 | 零相对信号过滤与已掌握行为保持的不同职责；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)；具体机制已入正文，root实际写后通过 |

## 4. 证据与知识整合

### [Disentangled Robot Learning via Separate Forward and Inverse Dynamics Pretraining](https://arxiv.org/html/2604.16391v1)

当前采用：**整合** — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3/Table4～9/AppA3/A5～6：forward/inverse的action-free预训练职责不同，下游固定forward、丢inverse重建decoder并训练inverse/action adapter；全更新对照不是唯一gradient因果，未来观测预测不等真机transition。6知识缺口深入，apr02必要源/真实Ch26已核，普通实际Books未写；有效记录见[证据笔记](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)。

### [Shifting the Gradient: Understanding How Defensive Training Methods Protect Language Model Integrity](https://arxiv.org/html/2604.16423v1)

当前采用：**整合** — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§2～4.2/Eq2/Table1与Ch29比较：训练forward trait-vector与输入prompt具有不同梯度职责，neutralize近默认不支持唯一因果或trait彻底清除，coherence可退步。6知识缺口深入、apr02 source→owner通过；普通写入未落实，见[证据笔记](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)。

### [Erasing Thousands of Concepts: Towards Scalable and Practical Concept Erasure for Text-to-Image Diffusion Models](https://arxiv.org/html/2604.16481v1)

当前采用：**整合** — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3.4/Eq6～7/D2/F4/I：projector腐化→模块恢复依赖是受限tamper分支，仅移除模块但保腐化基座不等对手无法恢复原projector。UD残余/训练成本保留。6保护/缺口深入、apr02真实Ch72 gap通过，未写入；见[证据笔记](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)。

### [BARD: Bridging AutoRegressive and Diffusion Vision-Language Models Via Highly Efficient Progressive Block Merging and Stage-Wise Distillation](https://arxiv.org/html/2604.16514v1)

当前采用：**整合** — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际Alg1/§3/Table4：固定block anchor向同腐化、同位置学生蒸馏不是clean-prefix next-token目标，额外阶段与教师预算、ChartQA退步保留。6知识缺口深入、apr02必要源与Ch24对读通过，普通书稿待落实；见[证据笔记](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)。

### [KAIROS: Stateful, Context-Aware Power-Efficient Agentic Inference Serving](https://arxiv.org/html/2604.16682v1)

当前采用：**整合** — `PLATFORM-COST` [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3.3～3.4/6.2～6.3/7～8：降频→寿命/context→evict/recompute反馈与β/γ admission是Ch70窄缺口；P5累计token/s、3小时请求回放不证明request-tail或真实task success，PD未测。6深入、apr02源/owner通过，尚未真实写后；见[必要记录](../_sources/daily-20260421/V3_BATCH_16659_16684.md)。

### [HieraSparse: Hierarchical Semi-Structured Sparse KV Attention](https://arxiv.org/html/2604.16864v1)

当前采用：**整合** — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§III～V/phase路径：signed dense/semi-structured pools与按阶段重压缩共同定义KV artifact，稀疏格式不天然省驻留或不损质量。L40S48GiB/PyTorch2.10/CUDA12.8已披露，不能误写hardware ND。6缺口深入、apr02 source→Ch45通过，实际Books未写；见[必要记录](../_sources/daily-20260421/V3_BATCH_16855_16883.md)。

### [Symphony: Taming Step Misalignments in the Network for Ring-based Collective Operations](https://arxiv.org/html/2604.16880v1)

当前采用：**整合** — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§III～V/prototype与simulation：switch可见进度proxy驱动额外ECN，不执行归约，也不拥有collective完成真值；模拟与双流原型不能合并成生产规模结论。6缺口深入、apr02对Ch36采用范围通过，普通书稿未落实；见[必要记录](../_sources/daily-20260421/V3_BATCH_16855_16883.md)。

### [SinkRouter: Sink-Aware Routing for Efficient Long-Context Decoding in Large Language and Multimodal Models](https://arxiv.org/html/2604.16883v1)

当前采用：**整合** — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3～5：sink信息用于本轮group跳读，未读块仍保留供未来查询，40% read/compute预算不等40%驻留容量。RTX PRO6000/bf16已披露，单次update不升全生成保证。6缺口深入、apr02对Ch45通过，普通写后未落实；见[必要记录](../_sources/daily-20260421/V3_BATCH_16855_16883.md)。

### [When Choices Become Risks: Safety Failures of Large Language Models under Multiple-Choice Constraints](https://arxiv.org/html/2604.16916v1)

当前采用：**整合** — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3～5/配对协议：固定全部不安全候选与direct/CoT格式可放大内容安全失败，应把候选admissibility、候选外拒绝、格式和有害协助分账；加拒绝选项不是保证修复。6保护/缺口深入、apr02对Ch66真实gap通过，尚未书稿写后；见[必要记录](../_sources/daily-20260421/V3_BATCH_16902_16917.md)。

### [Freshness-Aware Prioritized Experience Replay for LLM/VLM Reinforcement Learning](https://arxiv.org/html/2604.16918v1)

当前采用：**整合** — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3～5：priority可按advantage/TD重算，仍须分priority寿命、buffer采样IS和behavior-policy ratio；Standard默认IS而Fresh默认无IS的对照不能藏。6深入、apr02对Ch33窄gap通过，实际书稿未写；见[必要记录](../_sources/daily-20260421/V3_BATCH_16918_16940.md)。

### [Different Perspectives of Memory System Simulation](https://arxiv.org/html/2604.16965v1)

当前采用：**整合** — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§2～3.5/Listing1/§4～5：ps时钟推进消除换算误差，不追回two-phase immediate-response已错误重叠的依赖请求；组件统计正确不保证应用load-to-use因果。残余饱和误差与未建模PHY/IO保留。6深入、apr02对Ch66gap通过，未写后；见[必要记录](../_sources/daily-20260421/V3_BATCH_16952_16972.md)。

### [On Safety Risks in Experience-Driven Self-Evolving Agents](https://arxiv.org/html/2604.16968v1)

当前采用：**整合** — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3～5/Table3：固定backbone良性外部经验也可改变未来安全分布；memory-enabled/disabled/length-matched及经验类型切片不同于恶意载体清洗。attention×gradient非完整IG或因果，长度对照也改指令。6保护/缺口深入、apr02对Ch72通过，未真实写入；见[必要记录](../_sources/daily-20260421/V3_BATCH_16952_16972.md)。

### [MCPO: Mastery-Consolidated Policy Optimization for Large Reasoning Models](https://arxiv.org/html/2604.16972v1)

当前采用：**整合** — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§4～6/Eq7～15：全正确组零相对梯度与其他prompt更新时的行为保持不同；mastery hinge只约束所采token drift，p1须独立分支，少量AMC/AIME反向slice和过滤补采成本保留。6缺口深入、apr02对Ch33通过，普通Books未写后；见[必要记录](../_sources/daily-20260421/V3_BATCH_16952_16972.md)。

### [HeadRank: Decoding-Free Passage Reranking via Preference-Aligned Attention Heads](https://arxiv.org/html/2604.17237v1)

当前采用：**整合** — `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际 v1 §2～3/Limitations/AppE/F：有标签的 head 选择、attention 偏好训练与最深选中层截断共同定义排序 artifact；不等完整 LM/QA 或解释 faithful。211 query 派生多对训练、8 H20、top40/batch16 的配置成本及 slice 退步保留；格式成功不是排名正确。6知识缺口深入，拟 Ch76 reranking 段补训练—读出—执行停点分支，未经采用核/实际写后不计整合，见[必要记录](../_sources/daily-20260421/V3_BATCH_17237_17249.md)。

### [DORA Explorer: Improving the Exploration Ability of LLMs Without Training](https://arxiv.org/html/2604.17244v1)

实际 v1 §3～5/Alg1：决策探索、生成列表、过滤已用行动、序列统计 proxy 与 λ 采样分开；额外调用、MAB不全胜与Jericho退步保留。分数可负，不作 [0,1] confidence，仍可softmax。6标准仅报告，有限 action 控制证据不推出一般 epistemic/ regret 保证，不声称 Ch20 已写全部算法，见[必要记录](../_sources/daily-20260421/V3_BATCH_17237_17249.md)。

### [VIBE: Voice-Induced open-ended Bias Evaluation for Large Audio-Language Models via Real-World Speech](https://arxiv.org/html/2604.17248v1)

实际 v1 §2～4：11模型、人声开放输出→属性抽取→nTVD/置换，测的是任务合同下条件分布偏移；小样本Advisory人工核非全部 extractor/任务真值，跨数据MCQ幅度不可合并，任务排名不稳定。5标准仅报告，保留测量协议及说话人/声学混杂边界，不写普遍公平性或性能保证，见[必要记录](../_sources/daily-20260421/V3_BATCH_17237_17249.md)。

### [PAC-Bayes Bounds for Gibbs Posteriors via Singular Learning Theory](https://arxiv.org/html/2604.17219v1)

实际§2～3/Theorem5、§4.2/5：Gibbs后验平均与population-risk积分/RLCT刻画具体有条件复杂度，compact/先验/MGF/温度假设不能省。不是SGD点估计、任意Transformer或从训练损失可算的发布保证。5标准仅报告，保留条件理论而非硬件benchmark，见[必要记录](../_sources/daily-20260421/V3_BATCH_17219_17228.md)。

### [Bilinear Input Modulation for Mamba: Koopman Bilinear Forms for Memory Retention and Multiplicative Computation](https://arxiv.org/html/2604.17221v1)

实际II-B～D/III-C/IV-C/V：BIM的state-conditioned selectivity与shared-state分开；GM删该路径并改input-only sigmoid gate可scan，不是精确替代。memory与乘法任务排序/退步和RTX3080Ti/compile成本保留；v1仅两分支，库存后来三分支未回填。6标准仅报告，不称Ch22已承载全部方法，见[必要记录](../_sources/daily-20260421/V3_BATCH_17219_17228.md)。

### [Revisiting Auxiliary Losses for Conditional Depth Routing: An Empirical Study](https://arxiv.org/html/2604.17228v1)

当前采用：**整合** — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际§3～6：future-all-full teacher与50% gate策略不同，移除utility/rank在本配置改善，不证明唯一off-policy因果或全部aux有害。157.5M冻结backbone、三seed/BF16/seq256/V100条件与proxy/壁时分开；0.005非等效检验，25%补充方向反转。6知识缺口深入，拟`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)auxiliary proxy段补标签future-policy合同与移除对照，尚未采用核/实际写入，见[必要记录](../_sources/daily-20260421/V3_BATCH_17219_17228.md)。

### [Demystifying the unreasonable effectiveness of online alignment methods](https://arxiv.org/html/2604.17207v1)

实际 §2～4.3/§5 与必要 B/C：argmax reward 的决策 regret 不等软策略 KL regret；compact/可实现 BT、统一 gap、参考支持和全局 ERM 限定不可省，模拟的 current/reference 配对又不同理论 iid current slate。5 标准仅报告，不把有限 probe 或条件 O(1) 外推 LLM 训练成本，见[必要记录](../_sources/daily-20260421/V3_BATCH_17207_17215.md)。

### [Guardrails in Logit Space: Safety Token Regularization for LLM Alignment](https://arxiv.org/html/2604.17210v1)

当前采用：**整合** — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际 §3 Eq2～3/Alg1、§4/官方 PDF-v1 同机制交叉：同 context 对少数拒绝词 logits 加 frozen-base 锚，不能固定完整 softmax 或序列行为；额外 base forward、选择模板/λ 成本与不如 base 的 slice 保留。6 保护/缺口深入，拟 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) Safety Repair 后窄补锚与行为验收分权，未写入/采用通过。HTML 标题后缀差异已以官方 abs/PDF 身份定点核，见[必要记录](../_sources/daily-20260421/V3_BATCH_17207_17215.md)。

### [EmbodiedHead: Real-Time Listening and Speaking Avatar for Conversational Agents](https://arxiv.org/html/2604.17211v1)

实际 §3.3/Alg1、§3.4/§4：队列单调消费与麦克风滚动尾部产生逐帧来源 state，修正 dual-stream future-audio 依赖；不等同时说话的语义 uptake 或 effect authority。部分 motion/节拍退步，RTX3090 渲染 FPS 不含完整 LLM/网络/SLO。6 标准仅报告，Ch23已有在线 channel/commit 主线不代表本篇算法全覆盖，见[必要记录](../_sources/daily-20260421/V3_BATCH_17207_17215.md)。

### [Continual Safety Alignment via Gradient-Based Sample Selection](https://arxiv.org/html/2604.17215v1)

当前采用：**整合** — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际 §3～5/E.4/E.6/限制：loss 预筛+median gradient 选择与 clipping 有不同监督支持，范数不等内容安全或方向因果；LoRA/三 seed 的能力退步与单 H100 约1.5倍 epoch 开销保留。6 保护/缺口深入，拟 `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) Safety Repair 后补 selector proposal/coverage/训练成本边界，未写入/采用通过，见[必要记录](../_sources/daily-20260421/V3_BATCH_17207_17215.md)。

### [React-ing to Grace Hopper 200: Five Open-Weights Coding Models, One React Native App, One GH200, One Weekend](https://arxiv.org/html/2604.17187v1)

§2/3/6已实际读：aider whole-file parser把含推理结束标记的解释行当文件路径，产物不bundle；单任务/单seed、不同sampling与dynamic quant、原artifact仅on request，不能推模型总排名、温度零必hang或universal语料缺口。5标准仅报告，Ch78当前parse/canonicalization/authorization已有长期责任边界，本症状不强造新正文。配置/未证明项与精确日期原字段见[四项必要记录](../_sources/daily-20260421/V3_BATCH_17187_17200.md)。

### [Partitioning Unstructured Sparse Tensor Algebra for Load-Balanced Parallel Execution](https://arxiv.org/pdf/2604.17198v1)

当前采用：**整合** — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

官方PDF-v1 §2～5必要范围已实际读：多operand/层级稀疏的访问量由monotone/hierarchically-consistent cost建模，outer intersection跳子树需发现/重映射有效坐标；proxy均衡不等wall-clock最优，partition/assembly/sort成本和SpGEMM退步保留。6gap深入，当前`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)已有双稀疏format/decoder/accumulation，但缺访问cost分区责任；拟其后窄补、尚未写入或采用通过。具体配置、Δ限定与共存边界见[必要记录](../_sources/daily-20260421/V3_BATCH_17187_17200.md)，不是LLM端到端收益。

### [CCCL: In-GPU Compression-Coupled Collective Communication](https://arxiv.org/html/2604.17172v1)

官方abs/PDF/HTML精确v1一致为CCCL，旧库存UCCL-Zip/split-send不回填；实际§4～6.5核局部exponent表、NCCL路径融合、对齐raw尾及matched4SM反例。6分标准已有覆盖，`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)压缩critical path/codec/overlap现文承担长期边界；all_reduce和小payload退步不被峰值带宽覆盖。应用正文是PD的KV transfer，不造权重迁移；model/length/batch/precision/SLO缺口不支持通用吞吐。详[四项必要记录](../_sources/daily-20260421/V3_BATCH_17172_17182.md)。

### [Decomposing the Depth Profile of Fine-Tuning](https://arxiv.org/html/2604.17177v1)

实际v1§3～6用等化每层相对参数更新干预表示变化，但CKA/Procrustes不是功能、参数norm不是Fisher影响；小Transformer控制不涵盖全部15模型/6.9B，encoder训练epoch也非全matched。Table1与抽象parallel二分不同，保留目标×架构×规模及弱梯度噪声混杂。5分标准仅报告具体诊断；Ch29现trainable-subspace身份原则不冒称此算法全已有，但本篇§5/6不支持可靠placement recipe，无新增Books采用。

### [BranchBench: Aligning Database Branching with Agentic Demands](https://arxiv.org/html/2604.17180v1)

当前采用：**整合** — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际v1§3.3～5.5将branch lifecycle与query selectivity/active concurrency/whole-loop成本拆开。共享content-addressed branch快fork并不快range read，独立compute branch承担provisioning/配额；单branch读不随总branch数下降，多活跃分支争固定resource。6分知识缺口深入提案拟`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md)外部状态分支成本段后，补creation vs execution预算而非排行榜；现COW/state身份已在正文，不称从无到有。云与selfhostresource不matched，full/mini、2h截断、storage统计偏差限制普遍结论。待非作者采用/实际落笔，不先标整合。

### [Layer-wise MoE Routing Locality under Shared-Prefix Code Generation: Token-Identity Decomposition and Compile-Equivalent Fork Redundancy](https://arxiv.org/html/2604.17182v1)

实际v1III～V按token identity/O0 group核route交集；Qwen FP8/GH200/SGLang、thinking skip、30min截断与完成/编译分母条件保留。Jaccard非hidden/output等价，compile相同非通用正确性，原文未验证offload吞吐；top3的67%是691compiled分母而非851completed。6分标准已有覆盖，`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)batch sharing proposal不能覆盖token-router语义，现文承担该长期边界，不称全部分层测量已存在。

### [ScenarioControl: Vision-Language Controllable Vectorized Latent Scenario Generation](https://arxiv.org/html/2604.17147v1)

exact-v1 §3.1～3.3/§5.1～5.3/Table3已读。直接cross-attention与共享K/V的latent全局汇总经零初始化gate相加，为dense-to-sparse条件生成提供受限选择对照；5分标准Only。生成initial scene、simulator rollout与视频投影职责分开，不能将控制相关性当实际物理transition保证，碰撞等列也非全面最优；无端到端SLO证据，不强写通用首选。

### [Systematic Capability Benchmarking of Frontier Large Language Models for Offensive Cyber Tasks](https://arxiv.org/html/2604.17159v1)

exact-v1 III-A工具发现段/III-B～C、IV-A～C/V必要部分已读。Gemini3Pro八配置各200任务显示环境×提示收益方向翻转；Kali工具与discovery一起变，非单OS因果；单trial、API/parser、10min与轮数预算限制排名和planner/executor比较。6分按安全能力评价合同受影响的必要边界深入完成，已有覆盖处置不变；不是因安全关键词抬分。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)subject identity与Harness/Environment现文真实承载长期命题，不冒称具体CTF流程均已实现。apr02已实际独立核这些必要正文与owner，见[八项审计](../_sources/daily-20260421/V3_APR02_LATE_EIGHT_17143_17187_INDEPENDENT_AUDIT.md)；本批配置及两关闭理由见[有限裁决](../_sources/daily-20260421/V3_BATCH_17147_17163.md)。

### [The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Majorities via Token-Level Collaboration](https://arxiv.org/html/2604.17139v1)

exact-v1 §3.3～7、AppendixB/D.1/D.2必要部分已读。每K token交接共同前缀改变相关污染下的干预位置，因此6分保护深入；少数污染退步、强污染Qwen失败与M增大不单调均保留。谱隙本身不建立AppendixB的潜势收缩，该额外假设未校准到实际LLM；不反驳收缩条件下的代数，也不采用一般真值保证。decode步匹配不含switch-prefill/调度，不写同成本，仅报告受限替代证据。

### [SeekerGym: A Benchmark for Reliable Information Seeking](https://arxiv.org/html/2604.17143v1)

exact-v1 §2～3、AppendixD.1/F/G.3必要部分已读。冻结单article的goal passages与oracle skeleton可测corpus-relative遗漏，但不证明开放事实完整；离线合成belief的conformal校准不能直接保证真实相关trajectory或adaptive停止。6分标准已有覆盖，`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)“验证没有遗漏必须先建立应出现事实的Inventory”与“不确定性必须绑定覆盖假设”已有对应长期命题，不称全算法已实现。

### [Negative Momentum for Convex-Concave Optimization](https://arxiv.org/html/2604.17145v1)

exact-v1 §1.1～4/Lemma4.1及§5机制必要部分已读。y更新使用新x，两步状态进入Lyapunov；平均平方梯度范数与强凸凹距离结果需分别读，不能改写为一般last-iterate loss或随机非凸训练保证。5分标准仅报告明确假设下的优化分支，不以无LLM实验拒绝，也不凭条件理论改训练选型。本批完整原字段、配置边界及日期例外见[有限审阅](../_sources/daily-20260421/V3_BATCH_17139_17145.md)，非作者尚待核。

### [HiveMind: OS-Inspired Scheduling for Concurrent LLM Agent Workloads](https://arxiv.org/html/2604.17111v1)

exact-v1 §3–5/Table5–7/7.2已实际读；condition-counter动态准入与集中retry的消融可以报告，但mock首错即死、重试预算、同场景18%与零的差异不支持生产因果或完全恢复。透明SSE不是已发布prefix幂等证据，本地零失败不替代云端stampede。5分标准仅报告，不由OS类比制造新长期章。

### [Complementing Self-Consistency with Cross-Model Disagreement for Uncertainty Quantification](https://arxiv.org/html/2604.17112v1)

exact-v1 §3 Eq1–4/§4–5/A.8–A.10必要范围已读：TU消去self项等于1−cross，相似度非真值或已识别概率分解。同规模不同厂商不能证明idealensemble，逐slice反例/单GPU多checkpoint成本与相同采样预算分开。6分标准仅报告具体估计器；Ch66同源错误与sensor分权已具体承载长期判断，不称全部算法现已实现。

### [Prompt Sensitivity in Vision-Language Grounding: How Small Changes in Wording Affect Object Detection](https://arxiv.org/html/2604.17126v1)

exact-v1 §2–4/5.3实际读。DETR固定proposal可以观察CLIP选框变化，但woman/boy-with-hat并非等价提示、GT仅用于筛选；PCA相关性不证明argmax唯一因果，IoU总体质量评价尚未做。5分标准仅报告受限接口诊断，不声称一般grounding必失败，也不将定性示例升级为ensemble质量保证。

### [Please refuse to answer me! Mitigating Over-Refusal in Large Language Models via Adaptive Contrastive Decoding](https://arxiv.org/html/2604.17132v1)

exact-v1 §3.2–3.3/4/Limitations和AppendixH Alg1实际读。extreme/raw同历史两forward与rank/confidence切换改变首k步保护行为，6分深入；正文概率加减不归一且可负，但Alg1是argmax，有限signed scores仍可执行排序，不能据符号问题否定全部经验。WildGuard/固定参数、Llama恶意拒答退步与双forward代价限制“保持安全”，仅报告、不写Books。

四项完整必要依据、原字段与未披露条件见[有限本批](../_sources/daily-20260421/V3_BATCH_17111_17132.md)，作者侧终态不替代非作者或日级验收。

### [Latent-Compressed Variational Autoencoder for Video Diffusion Models](https://arxiv.org/html/2604.16479v1)

exact-v1 §4.2 Eq5–7、§4.3和Tables1/3/4支持固定四频带→逆变换→learned decoder的训练责任，不能以部署后过滤或少channel替代codec身份。WebVid部分rFVD及Sky/UCF生成FVD反向结果、额外变换/训练代价均保留。已在Ch23 rate–distortion与Codebook交接实际整合；apr02真实原文、正文及相邻衔接写后通过，实验未复现。

### [From Inheritance to Saturation: Disentangling the Evolution of Visual Redundancy for Architecture-Aware MLLM Inference Acceleration](https://arxiv.org/html/2604.16462v1)

exact-v1 §3/Table2、AppA.1 Eq8–11支持停止visual更新但仍全token计算K/V供文本读取，与删除读路径不同；Qwen/LLaVA的反向结果限制架构迁移，几何熵不是可删或前端因果证明。已在Ch23视觉删改协议之后真实补更新/读取成本与恢复边界，handoff Ch45生命周期；apr02实际必要源和真实正文写后通过。

### [Motif-Video 2B: Technical Report](https://arxiv.org/html/2604.16503v1)

exact-v1 §3.3 Eq2–4/Fig5、§6.2/§7.2支持零Wo只保持起始函数、post-SA视频新Q读取同层pre-SA文本K/V的投影复用。Fig5联合改变Q/KV，不能将稳定性唯一归因KV，更不等整attention免费或后续训练函数不变。已在Ch23模块化Fusion→Full-duplex交接真实窄写，代价/回退就近；apr02必要原文、正文及邻接写后通过。三项详细记录见[写后独立复核](../_sources/daily-20260421/V3_APR02_CH23_THREE_WRITE_AFTER.md)，非日级Gate。

### [BASIS: Balanced Activation Sketching with Invariant Scalars for "Ghost Backpropagation"](https://arxiv.org/html/2604.16324v1)

实际读exact-v1 Eq1–7、Alg1、实验表。未缩放独立随机符号sketch无偏不等于norm-calibrated estimator无偏或任意weighted variance最小；Eq6 bin-label置换不能改变固定residue碰撞，Alg1 B长度assignment permutation须另行解释，不能据前者否定整算法。中心保证窄争议，不写Books；T4小模型/batch1/短序列实验不证明端到端VRAM或收敛。详细 [证据笔记](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)，最终日期与评分待闭。

### [Training for Compositional Sensitivity Reduces Dense Retrieval Generalization](https://arxiv.org/html/2604.16351v1)

实际读§2–4及必要附录。同wall-clock结构负例改善near-miss拒绝却损失NanoBEIR跨域检索，MaxSim relevance不等相同命题身份核验。root再对读当前 `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)：检索表示段已明确hard-negative目标域收益与原域退化分账，query/evidence gate已区分relevance与support。采用的长期判断已有具体正文承载，故6分深入完成、已有覆盖，不追加论文名称；原near-miss受控基准不是书稿已经实现的系统或全部已写细节。

### [Cross-Family Speculative Decoding for Polish Language Models on Apple Silicon: An Empirical Evaluation of Bielik 11B with UAG-Extended MLX-LM](https://arxiv.org/html/2604.16368v1)

实际读方法/两算法/评价/成本。M2 Pro32GB、int8 target/int4 drafts、短输出仅支持acceptance、draft重同步和共享带宽一起评价；TPS排除prefill，并发/SLO未披露。拟与 `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) 的净成本/状态生命周期正文作具体已有覆盖裁决；OAI current为04/22，日期仍须结合v1记录，不孤证定owner。

### [Same Verdict, Different Reasons: LLM-as-a-Judge and Clinician Disagreement on Medical Chatbot Completeness](https://arxiv.org/html/2604.16383v1)

实际读§3–4数据、groundtruth、threshold/ranking。human omissions与model-graded ideal-answer rubric证据权限不同；few-shot阈值F1增益不替代ranking，90%recall几乎全面人工审查的条件保留。拟与 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的expected-fact inventory和risk-coverage比较，不外推所有judge无效。

### [GraphRAG-Router: Learning Cost-Efficient Routing over GraphRAGs and LLMs with Reinforcement Learning](https://arxiv.org/html/2604.16401v1)

实际读§4.1/§5.1/§5.3–5.5及必要附录。先选择GraphRAG及预期粒度、再选generator，**之后**才实际检索，不是已经获取真实evidence再选模型。Table3在固定五类GraphRAG/五generator与Qwen2.5-3B router下比较三种顺序；代理cost1/2/4不覆盖router、graph构建或实际API成本。保留受限顺序对照，不称普遍最优，也不因新router名称改书。

### [Functional Similarity Metric for Neural Networks: Overcoming Parametric Ambiguity via Activation Region Analysis](https://arxiv.org/pdf/2604.16426v1)

因HTML日期可能后发，实际核官方PDF v1首页及§10.4/§11.2–11.3，不宣称92页全读。对同一固定hash签名的Hamming平均，逐坐标indicator本身满足三角不等式；与其“fixed realization可能违反”声明不一致。两toy网络/16k samples不证明参数扰动后的canonical稳定性。采用范围争议隔离，重开需精确距离定义/证明修正及稳定性对照；不由此否定所有匹配实验。

### [Beyond Feature Fusion: Contextual Bayesian PEFT for Multimodal Uncertainty Estimation](https://arxiv.org/html/2604.16615v1)

实际读§2.2/§4。共享pooled audio经逐层head条件化低秩随机矩阵E，A/B和backbone角色不混。rank8/两轮/十次MC及任务AUC只支持这个参数条件化分支；未直接证明audio噪声驱动variance具有校准错误概率的意义，rare-positive切片有fusion反收益。因此仅报告，不把临床任务本身作为范围排除理由。

### [Cross-Modal Bayesian Low-Rank Adaptation for Uncertainty-Aware Multimodal Learning](https://arxiv.org/html/2604.16657v1)

实际读§2.2/§4。逐token text query读取audio frames，再生成低秩E posterior，shared-KV是成本替代；与16615不同家族，不是独立可靠性复现。rank8/50轮/十次MC、speaker-separated五折，AUC不是概率校准；Table3不是token-level全面胜利。具体机制可以报告，但不能横比前篇的两轮预算或采用“更可靠”通用结论。

### [How Robustly do LLMs Understand Execution Semantics?](https://arxiv.org/html/2604.16320v1)

输入mutation是新执行实例，MPT只在原输入核输出相同，两者为分开实验；PSR要求十实例全正确，与canonical accuracy是不同对象。684程序/14模型/default API的受限反证值得报告，但any-match/substring及多断言任一正确的oracle放宽，不能识别内部世界模型或跨架构因果。必要原文及非作者窄核已实际完成。

### [Steerable Instruction Following Coding Data Synthesis with Actor-Parametric Schema Co-Evolution](https://arxiv.org/pdf/2604.16322v1)

每加约束先适配witness并核全部新旧checker，再由actor两类passrate决定继续/终止；checker拥有可行性、actor拥有难度信号，是条件化生成机制。27初始schema/三代/4241问题与若干后代反收益保留；有限AST/test不证明任意语义和无泄漏。必要PDF方法/评价与非作者窄核已完成；仅报告，不把整个sampler称已有覆盖。

### [Benchmarking Real-Time Question Answering via Executable Code Workflows](https://arxiv.org/html/2604.16349v1)

相对日期执行时解析，DOM当前结果作oracle，320中文/12域，初始流程经过文本/截图和人工核。Repair仅由error/null触发，不检测静默语义漂移，time-anchor对照更换日期也不是纯anchor因果实验。Ch66 run identity/snapshot/repaired-harness revision已承载本次采用的长期有效性边界；不是称所有实现均已写进书。必要源/owner非作者已核。

### [SaFeR-Steer: Evolving Multi-Turn MLLMs via Synthetic Bootstrapping and Feedback Dynamics](https://arxiv.org/html/2604.16358v1)

Tutor同产下一攻击及评分，prefix min/mean累加再给全轨迹advantage；不是逐token因果credit。QwenVL3/7B、BF16、8A800、5rollout/batch64的TCSR/feedback消融可报告；共享judge、长短return和threshold后turn-average分母不支持开放安全保证。必要原文作者外已核，标准6分，不因标题安全自动全升Deep。

### [CSF: Black-box Fingerprinting via Compositional Semantics for Text-to-Image Models](https://arxiv.org/pdf/2604.16363v1)

官方PDF前八页已恢复并实际双人审阅。组合prompt生成类别分布、Wasserstein最近base和Beta计数区间支持有限探针归属，后验对象是probe argmin投票比例，不是归一化identity/OOD概率。42prompt×30图、6family/13variant、共享CLIP误差与独立probe假设保留；标准6分，仅报告query-only实现，不重复Ch59的一般指纹保证。

### [CoLLM: A Unified Framework for Co-execution of LLMs Federated Fine-tuning and Inference](https://arxiv.org/html/2604.16400v1)

训练写shadow、推理读active、步后原子交换及异步回拷是具体双缓冲方案，但pointer atomic不单独证明跨token请求/KV/kernel的整版本快照。8A30 24GB、两LLM、六instruction数据集/Azure traces、CE质量与忽略global通信仅支持受限共执行；不采用普遍deterministic或3×宣传。原文§III–VI已读，标准6分Only，不据未证明条件否定全部经验。

### [GRAB-ANNS: High-Throughput Indexing and Hybrid Search via GPU-Native Bucketing](https://arxiv.org/html/2604.16402v1)

Scalar bucket连续存储、local/remote定长边和append更新是实际执行分支；Alg2过滤区间外候选，remote边存在不证明任意诱导过滤子图可导航。四百万规模数据集/uniform scalar/随机区间/batch100/Recall@10×QPS、i9/3090Ti，不推任意布尔ACL、删除/高churn或snapshot。必要方法/评价及apr02有限非作者复核已实际完成，标准6分Only，不是日级Gate。

### [StressWeb: A Diagnostic Benchmark for Web Agent Robustness under Realistic Interaction Variability](https://arxiv.org/html/2604.16385v1)

实际读exact-v1 §3.1–3.3、§4.1–4.5/Table1。相同任务集分开视觉/DOM、交互规则与执行扰动，显式RemapE提示不能与隐式Remap混同；100步预算、checkpoint pass与整任务成功、claimed DONE与独立页面状态各有对象。八API模型/149任务/七条件只支持受限行为反证，不证明模型内部不存在在线适应机制。Ch66已实际承载观察×规则配对、执行失效及独立Outcome Witness，自报成功不取代结果；本项已有覆盖的是这些长期判断，不是称整套benchmark在书中实现。§4.5的自报错位还受早停/预算影响，不作校准错误的唯一因果。

### [Breaking Validity-Induced Boundaries to Expand Algorithm Search Space: A Two-Stage AST-Based Operator for LLM-Driven Automated Heuristic Evolution](https://arxiv.org/html/2604.16420v1)

必要§3/Alg1–2与§4/Table1–2已读。无效AST原对象可留种群，但fitness由修复后合法子程序执行得到；搜索proposal、repair产物和被评价程序身份必须分开。固定pop/轮数的EoH/ReEvo等变体有局部token节约，但没有独立repair消融或合法空间断裂证明，iOBP/TSP部分配置反收益保留。标准5分仅报告该具体搜索分支；不冒称Ch81已有整算法，也不据局部经验强加普遍搜索保证。

### [Measuring Representation Robustness in Large Language Models for Geometry](https://arxiv.org/html/2604.16421v1)

实际读exact-v1 HTML §3 Eq1–6/§4–5与官方PDF第16页Table7。三种表示均正确和三种原答案字符串一致不是天然同一对象，尺度变换需要规范化身份桥。更直接地，Table7多行Invariance大于Consistency，违反原文Property3；官方PDF复核同样如此，不只是HTML缓存问题。5分纠错深入暂缓，保留受控表示评价的价值，不据有矛盾的关系采用任何能力排序保证。apr02已独立核两种答案空间解释均无法同时支持保证与表格，窄隔离通过；恢复需同家族原始预测、normalizer/metric代码及更正定义/表格，该家族保持本窗终态隔离。完整证据见[必要审阅](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)。

### [ICAT: Incident-Case–Grounded Adaptive Testing for Physical-Risk Prediction in Embodied World Models](https://arxiv.org/html/2604.16405v1)

实际§2–3与limits区分真实事故和标准派生pseudo-case，人工核初态后仅给动作，grounded风险解释由三人判视频；best-of3依RCCC选样，不能解释为在线风险概率。909项/六video生成模型的risk-chain诊断有具体价值，但severity近似、环境覆盖和oracle选择不允许真实闭环安全保证。5分标准仅报告，不声称Ch66已有全部实现，也不因安全标题自动深入所有附件。

### [Matched-Learning-Rate Analysis of Attention Drift and Transfer Retention in Fine-Tuned CLIP](https://arxiv.org/html/2604.16410v1)

实际§3–6与§7.2/9：四LR×五seed、CLIP ViT-B/32、EuroSAT/Pets和adapter-active CIFAR100 transfer。LoRA低LR欠拟合不代表低秩固有不能适配；同LR也不等同有效update或总compute。Attention entropy/CKA与transfer相关不是原因，有限grid不代表所有backbone/PEFT最优。5分标准仅报告受控优化条件反证，不重复写Ch30的一般heldout transfer原则。

### [Safety, Security, and Cognitive Risks in State-Space Models: A Systematic Threat Analysis with Spectral, Stateful, and Capacity Attacks](https://arxiv.org/pdf/2604.16424v1)

官方HTML/PDF必要§3.4、§8.1、§9/AppA已对读，apr02已实际独立核必要原文与反例。LTI H∞界不自动延伸为time-varying transfer先平均的界：memoryless y_t=b_tu_t，b=(1,-1)均值transfer为零，但同向u给非零输出，小幅缩放亦然。5分纠错深入仅隔离Remark3.2这条保证，不否定LTI或全部经验。S4-lite合成序列pilot的greedy位置攻击不证明频率攻击机制，预训练Mamba Table16仍pending；不采用安全认证/实际预训练防御有效性。恢复需合法时变bound及对应协议结果，不扩全版本史。

### [Dimensional Criticality at Grokking Across MLPs and Transformers](https://arxiv.org/html/2604.16431v1)

II Methods/III.1–III.4/IV实际核gradient snapshot→BA阈值cascade→跨widthFSS，shadow-probe和ungrok/不同prime对照；ModAdd有80/20split，XOR四pattern不分训练/测试。用观测泛化时点g事后对齐，不证明可线上预测任意g或D=1为通用门禁；Gaussian也给D≈1。5分标准仅报告具体诊断协议，保留null与适用范围；不将当前Ch5一般probe约束冒充已收录整套算法。硬件/precision未披露。

### [Sampling for Quality: Training-Free Reward-Guided LLM Decoding via Sequential Monte Carlo](https://arxiv.org/html/2604.16453v1)

§3.1–3.4/Eq4–17/Alg1与§4已实际核，apr02已独立实际定点核中心分布桥。形式full future sum可定义精确marginal，实际改为有限rollout；Eq17确含importance ratio，不据误读造反例。SMC TargetI-prefix转MH TargetII-lookahead及选择性低reward duplicate rejuvenation未说明整体一致target重权，独立估计ratio也未给extended-state保持，故6分纠错深入只隔离实现exact声明。三7B/3072max、unit-test/PRM成本与继承baseline，不证明优于训练方案或相同总预算；硬件/precision未披露。不否定形式目标/全部经验，重开需相应分布桥和验证协议，不扩附件。

### [EchoChain: A Full-Duplex Benchmark for State-Update Reasoning Under Interruptions](https://arxiv.org/html/2604.16456v1)

§1/4–7实际核speech-onset offset、同context/barge-in、人工rubric及half-duplex配对。48对话×4endpoint的失败差不等全部200对话代表性效应；flag后人工筛选和judge漏检影响分母，未测声学延迟/生产SLO。6分标准已有覆盖具体对应Ch66 duplex的continue/adapt/yield与uptake evidence，以及途中修订配对轨迹对原目标/旧约束的保留，不为taxonomy名字重复写书。

### [B-PASTE: Beam-Aware Pattern-Guided Speculative Execution for Resource-Constrained LLM Agents](https://arxiv.org/html/2604.16469v1)

实际读§3–9/Alg1，branch假设绑定局部state、资源与commit，效用同时算关键路径、后续unlock和干扰；先保护authoritative工作，再分配slack给safe-prefix。不同于只按概率预取单调用，但COW/staged-write不自动证明外部副作用隔离。Thor内部观测没有充分model/workload/precision/tail配置，完整评价明示future work。6分标准仅报告提出的调度分支，不采用1.4×普遍时延或无干扰保证，不冒称整个算法已在Ch78。

### [Semantic Channel Theory: Deductive Compression and Structural Fidelity for Multi-Agent Communication](https://arxiv.org/html/2604.16471v1)

只实际核有限知识库定义、Theorem5.1的coding/closure proof和Remark5.15–5.16，未声称全部理论审查。sender完整剩余KB仍存在，redundant消息的替换才可能保closure，不等开放自然语言恢复。Remark5.16从a可由receiver推导推出单receiver元素能替代a，缺条件：规则b∧c→a，sender{a}、receiver{b,c}满足weak coverage却无单元素替代保sender closure。5分纠错Deep仅隔离该扩展，apr02已实际定点核原文与反例，不否定强H1定理/所有capacity结论；重开需proxy输出集合或正确条件/证明，不写Books普遍通信保证。

### [Spike-driven Large Language Model](https://arxiv.org/html/2604.16475v1)

实际读§4/Eq5–22、§5/Table3–12与能耗AppA：γ-SQP后整数count展开为二元/三元脉冲，以稀疏累加替换MAC，clipping再换质量。Theorem1 κ是平方幅度而非实际quantization-error；45nm算术常数不含完整内存/控制流，非实测power。所测Llama/Qwen INT4/6复杂任务有退步，展开D更大亦增工作，异步单步依硬件。6分标准仅报告这条表示分支，不采用15×实测节能或Serving吞吐/SLO。

### [Dynamic Eraser for Guided Concept Erasure in Diffusion Models](https://arxiv.org/html/2604.16483v1)

§4.1–4.3/Eq3–15、§5/Table1–4已实际核。PCA/KDE中心及prompt融合anchor指导敏感score触发的单方向closed-form校正；Eq13–14只优化固定方向二次surrogate，不等语义安全最优或全部benign输入保持。阈值不证明两分布分离，所测FID/AES/CLIP有退步。SD1.4/2.1、50步DPM/CFG7.5、九概念/I2P/RAB只限定保护行为；6分定点深入仅报告，不以91%升级安全证明或另写通用发布规则。

### [DexWorldModel: Causal Latent World Modeling towards Automated Learning of Embodied Tasks](https://arxiv.org/html/2604.16484v1)

§3.1–3.3/Eq9–16、§4/§5.2–5.3实际核。真实observations/executed actions更新长期TTT，预测latent只更新working副本，ODE内冻结；背景pre-denoising到真实观测后换条件。固定state是存储量条件，不是无损历史或无限可靠控制；history augmentation没有稳定性定理，flow-time方向说明也未统一。64H100/20天/Wan5B、模拟与受限真机未独立分离各组件/预算。6分标准仅报告具体职责组合；Ch25已有真实authority/权重漂移原则，未把该实现泛称已有覆盖，不采efficiency law或生产50%收益。

### [Geometry-Aware CLIP Retrieval via Local Cross-Modal Alignment and Steering](https://arxiv.org/pdf/2604.16487v1)

官方PDFv1 §4.2–4.4/§6.1–6.2/AppD已实际核，HTML同题名/机制并非仅因FGW与旧摘要Hungarian措辞差异就判污染。scene annotation构造object text vectors，在top-k作Hungarian/FGW；pairwise embedding geometry不自动是空间关系真值。naive steering有反收益，Hungarian常优于FGW、增大候选非单调改善。Recall与200query VLM nDCG非同一oracle，annotation不是免费感知，端到端成本未披露。5分标准仅报告局部组合反证，不把结构ranking普优写书。

### [LayerCache: Exploiting Layer-wise Velocity Heterogeneity for Efficient Flow Matching Inference](https://arxiv.org/html/2604.16492v1)

实际读v1 §3.1–3.5/§4.1–4.4/Table1与必要消融。group history与JVP span共同决定刷新schedule，是具体执行分支；Related Work自己包含token/attention粒度方法，不能采用“旧cache全为整网决策”。3prompt profiling、20prompt评估、Qwen-Image/A10080GB/BF16/50步/1024²/CFG4，不证明跨负载稳定性。§4.1 B25与Table1 B30不一致，1.37×低于MeanCache1.54×，不得采用同预算且同时更快的宣传。标准6分仅报告，不冒称全算法已有覆盖，也不推端到端SLO。

### [Positive-Only Drifting Policy Optimization](https://arxiv.org/html/2604.16519v1)

III.B–C/Alg1/III.C.5及IV–V实际核。positive advantage筛选后对同观测多action做drift，是可研究的更新分支；但RV=均值平方/二阶矩是signal fraction，固定均值下降噪声应令它上升，同actions多temperature场的总方差也不能省略covariance。Alg1的stop-gradient V与文字整target stopgrad不一致：前者若x两侧求导会抵消，不能据此断言作者实现必然零梯度。6分纠错深入暂缓中心保证；Genesis GO2/4096或16384并行环境/G4崩溃和G16较慢经验仍保留，不采普遍6.7%增益。恢复仅需RV/协方差解释及完整target实现，不扩全部附件。

### [CAMP: Cumulative Agentic Masking and Pruning for Privacy Protection in Multi-Turn LLM Conversations](https://arxiv.org/pdf/2604.16521v1)

PDFv1 III.D–F/IV.B–G/V.C–E/VI实际核，HTML中心一致但标题措辞不同，必要证据采用PDF。非hardblock类别阈值前请求PII原样送远端、之后改写本地历史，无法清除威胁主体已持有的API日志；hardblocked类别从turn0保护仍成立。TableIV四scenario零real-PII暴露若是累计日志对象，就与该pipeline不相容。ClaudeSonnet4.6/Azure/四合成scenario/alpha.3/三阈值只支持局部机制，不证明重识别概率校准或全utility不降。6分纠错深入暂缓中心零泄漏声明；重开需逐轮payload/计数对象与真实删除责任，不否定未来请求脱敏用途。apr02已独立核这一窄保证范围。

### [Anumati: Proof of Adherence as a Formal Consent Model for Autonomous Agent Protocols](https://arxiv.org/html/2604.16524v1)

v1 §3.1–3.6/§4.1/4.3–4.4/§6.1–6.2实际核。PolicyDocument→ConsentRecord→AdherenceEvent与capability变化触发重新同意，是可审计协议分支；TLC中的S1–S7不证明真实模型理解和行为遵从，fingerprint与reasoning依赖caller self-report。微基准不含network/TLS、签名验证未实现，两Gemini2.5Flash agents demo/35tests未本轮复现。6分保护行为深入仅报告，不将结构审计称合规证明，也不冒称Ch84/72已写完整ACAP算法；现有独立effect authority不因此改变。

### [SCATR: Simple Calibrated Test-Time Ranking](https://arxiv.org/html/2604.16535v1)

实际读v1 §4/§5.1–5.2/Table1–3/§6。逐model/domain小MLP读取倒数第二层最后有效token状态，以unit-test/答案标签校准BoN；N16/三calibration样本/heldoutearlystop是具体条件。Table2小Qwen HumanEval退步及数学budget增大退化保留。0.15–0.20ms仅selector，不含生成/hidden export/训练和发布；硬件、precision、并发/SLO未充分披露。5分标准仅报告，不把其算法全称已有覆盖，也不写内部自知或端到端1000×。

### [LLM as a Tool, Not an Agent: Code-Mined Tree Transformations for Neural Architecture Search](https://arxiv.org/html/2604.16555v1)

实际核§3/§4.3及AppC.2/3/5必要对照。算法确定operation/node/module、LLM补残余参数，E(exec,const,intend)通过才训练计分；随机粗选择优于LLM主导的局部反例有据。Qwen3-8B、≤1.5M/2M图像模型、100/500架构与主要one-epoch消融不证明大模型搜索普遍更好；代码挖掘100%正确和更大LLM因memorization必差不采用。5分标准仅报告，Ch81已有typedmutation/外部执行评估仍合理，不冒称本树算法已全覆盖。

### [S-GRPO: Unified Post-Training for Large Vision-Language Models](https://arxiv.org/html/2604.16557v1)

实际核§4.1–4.3/Eq4–7和§5/Table1–2。全失败替换一条GT使group产生contrast，但确定性专家不服从Eq7仍声明的πold采样；称纯on-policy/无偏行为克隆缺proposal与权重桥。6分纠错深入暂缓这一保证，不否定conditionalbootstrap全部经验。QwenVL7B/Qwen4Bsemanticverifier与δ=1 general退步保留，硬件/precision/总训练预算未充分披露；不采用SFT一定灾忘。恢复需真实mixedproposal/目标或改称heuristic，不索全部实现。

### [Conjunctive Prompt Attacks in Multi-Agent LLM Systems](https://arxiv.org/html/2604.16543v1)

exact-v1 §3–5与AppC必要路由/反证已读：key×远端template四条件可检查组合激活，但ASR是`__ACTIVATED__` marker，不能由allowlist后的marker推真实未授权效果。rho优化与固定真实router的映射仍有限，授权与效果authority不变；6分保护深入仅报告，不称攻击已突破所有系统防御。条件与成本见[证据笔记](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)。

### [Reasoning on the Manifold: Bidirectional Consistency for Self-Verification in Diffusion Language Models](https://arxiv.org/html/2604.16565v1)

exact-v1 §3–5/Alg1/Eq14/Tables1–3：同模型mask/reconstruct的六score可作受限selector，GT gate仍控制RL reward，不是无监督自证。Dream GPQA guided低于BoN、部分RL切片低于OutcomeRL；每次检查额外16步去噪重构、encoder评分及最多10次生成重试，K=16不是16条独立重构样本，不能由sample-count宣称端到端免费。Ch66同源一致性非truth与accepted-selector分账保持，6分标准仅报告，不冒称算法全部已有覆盖。

### [EquivFusion: Unifying Hardware Equivalence Checking from Algorithms to Netlists via MLIR](https://arxiv.org/html/2604.16571v1)

exact-v1 §3–5/AppC/E.2的MLIR/CIRCT共同逻辑与miter可在静态integer/bitvector、有限sequential范围检查前端和硬件artifact；8bit dot对32bit输出有sign-extension反例。FP、任意动态控制和全协议正确性不在现保证，lowering语义本身仍须验收。6分标准仅报告当前工具分支，不向Ch49写普遍LLM kernel证书，完整边界见证据笔记。

### [On the Robustness of LLM-Based Dense Retrievers: A Systematic Analysis of Generalizability and Stability](https://arxiv.org/html/2604.16576v1)

exact-v1 §3/5–8.1/Limitations区分英语query扰动、white-box和direct-transfer；Qwen3-.6B角均匀正则与双向转换的受控实验未一致提高鲁棒性，不以几何相关性定encoder目标。不同checkpoint比较不单因果归reasoning，ASR@20非答案安全。有限独立反证以5分标准仅报告，不把具体方法全称现Ch76已有、不推广到所有encoder，条件见证据笔记。

### [NWCAD](https://arxiv.org/html/2604.16686v1)

实际读§3.2–3.3、§4/6/Table3/AppB：JS与no-context margin触发显式baseline logits回退，不等持续contrastive tilt；仅same-current-prefix/greedy的被选步一致，全串须每步回退，confidence不等正确。`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)prior/context gate后已真实补入控制分支、两forward/阈值代价及有益context共存边界，source-family `SF-2026-ARXIV-2604-16686`。root已实际核原文、正文及两侧交接，写后通过；6分缺口深入、整合，不外推所有context不退化。

### [TensorHub](https://arxiv.org/html/2604.17104v1)

官方abs/HTML/PDF同identity，旧TStore保留alias；实际读§4.1–4.4、§6.1–6.4/Table3。bit sketch→ratio预测→online base/split须把新增base完整保存成本计入；ZipLLM也使用bit距离，不能把旧法描述成只依赖metadata。`PLATFORM-MODEL-REGISTRY` [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md)逻辑artifact身份之后已真实补physical layout规划及恢复风险，source-family `SF-2026-ARXIV-2604-17104`。2,890模型/40.11TB trace和192线程全内存无I/O不证明下载SLO、全局最优或hash认证。root实际源/正文/相邻交接写后通过；6分缺口深入、整合。

### 早期提案的当前落实情况

- `2604.16479v1` [LC-VAE](https://arxiv.org/html/2604.16479v1)：训练期固定四组wavelet支持与decoder适配，不是部署后剪latent或仅缩channel；重建和生成质量分别验收，若干rFVD/生成FVD退步保留。6分gap深入，`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)具体codec分支已获apr02实际来源→owner复核，已落实真实正文并通过apr02写后复核，当前为整合。
- `2604.16423v1` [PPS/IP](https://arxiv.org/html/2604.16423v1)：训练forward的trait-vector偏置与输入prompt改变具有不同梯度职责，不能把activation-gradient当参数更新、IP接近默认当完整因果解释。6分gap深入，`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)实际retention/teacher-trait段缺这条训练责任分支；apr02已核§2–4.2/Table1与当前正文，真实正文已落实并通过root写后复核，当前为整合。
- `2604.16391v1` [DeFI](https://arxiv.org/html/2604.16391v1)：forward/inverse分别用无动作标签视频预训练、固定forward表示，下游丢弃inverse重建decoder后训练inverse与action adapter，是Ch26未来观测→action主线的具体训练责任分支。6分gap深入的§3/Table4–9/AppA3/A5–6与真实owner已获apr02有限非作者支持；真机最多20连续尝试、模块延迟非SLO、全更新对照不是唯一gradient因果。真实正文已落实并通过root写后复核，当前为整合。
- `2604.16462v1` [HalfV](https://arxiv.org/html/2604.16462v1)：§3/Table2/6–7/AppA实际读，深层视觉更新冻结但读路径保留与继续更新少量token，在所测backbone有相反失效；Ch23现有geometry≠functional deletion原则下拟补更新责任/读路径分账。6分gap提案已获apr02实际源→owner核，已落实正文并通过apr02写后复核；不采普遍三阶段/前端唯一因果，质量退步和selector成本保留，AppB.4硬件字符串未作为已证设备，不能据FLOPs推生产时延。
- `2604.16481v1` [ETC](https://arxiv.org/html/2604.16481v1)：§3.4/Eq6–7、D2/F4/I的主动projector扰动→模块恢复依赖，使保留corrupted基座而只移除模块的对手遇到质量损失，不证明持有原projector的白盒对手无法恢复。Ch72现module integrity/erasure责任缺这条artifact恢复边界，6分保护行为/gap深入提案已获apr02实际非作者源→owner核；已落实正文并通过root写后复核，不采永久删除或tamper-proof，保留UD攻击残余与训练成本。

本小批日期依据保留在原始库存与[证据笔记](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)：16324/16351/16368/16383/16401/16426/16615/16657的v1 processing依次为04/21 UTC `00:00:40/00:01:13/00:01:43/00:02:01/00:02:25/00:27:48/00:08:50/00:11:59`；不改称公开时点。多数OAI新记录为04/21，16368 current为04/22，不用current datestamp孤证定owner。结合相邻批次/永久ID公告分配及[官方EDT公告槽](https://info.arxiv.org/help/availability.html)作上表有限区间推断；submitted早于4月可因hold而成立，不直接回拨。

上述五项及`2604.16503v1` [Motif-Video](https://arxiv.org/html/2604.16503v1)、`2604.16514v1` [BARD](https://arxiv.org/html/2604.16514v1)的早期提案均已落实。当前以§3及各具名§4正文的实际整合位置为准：LC-VAE/HalfV/Motif-Video为Ch23，PPS/IP为Ch29，DeFI为Ch26，ETC为Ch72，BARD为Ch24，必要正文与相邻交接均已通过具名非作者写后复核，不再是普通待办。早期提案的机制和反例仍由相应证据笔记保留。

### [Certified Program Synthesis with a Multi-Modal Verifier](https://arxiv.org/html/2604.16584v1)

实际读v1 §4.2–4.4/5.2/6.1–6.4/7。spec先type/LLM/PBT，再不同proof mode；无反例不等certificate，Lean只证形式spec而非NL意图。GPT5.2的50算法题含15开发/35评估，$5只code/proof、四题Lean胜而Velvet只部分、额外Aristotle与spec预算独立。Ch66 reference/oracle与vacuous equivalence责任没有因这组受限工具实例改变，具体分阶段实现不冒称完整Existing，5标准Only，未复现。

### [The Global Neural World Model: Spatially Grounded Discrete Topologies for Action-Conditioned Planning](https://arxiv.org/html/2604.16585v1)

实际读v1 §3公式/代码、§4–6。L2-normalized Softmax/batch均匀方向/WTA与predictive alignment组织离散网格，argmax snapping减少连续模糊，不证明所选未来state真实。单/双球、四action、40词合成语法与有限网格支持局部机制，不采用任意D训练已达唯一全局最小、开放因果发现或无限可靠rollout。lower-bound可达需均匀onehot可行，不能据p=z子集直接否定全可行域。5标准Only；Ch25 observation authority仍成立，不将算法全称Existing。

### [POLAR: Online Learning for LoRA Adapter Caching and Routing in Edge LLM Serving](https://arxiv.org/html/2604.16583v1)

实际读v1 §2–3/Alg1–2、§4.2/§5.1–5.4。resident set改变cold探测成本，router选择改变future反馈，forced exploration+epoch doubling是联合cache学习的具体分支。`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)现已在Calibration/placement交接真实补入快质量路由、慢驻留与cold-probe分账，6分缺口深入且root实际源→owner和写后非作者通过。15 Qwen2.5-7B adapters/RTX5080 load校准与synthetic linear-utility模拟不等生产trace；IID/full-rank/hot-margin/exact-cache条件与greedy区别保留，不采用无条件regret或SLO保证。

### [Real-Time Visual Attribution Streaming in Thinking Model](https://arxiv.org/html/2604.16587v1)

当前采用：**整合** — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

实际读v1 §3–4、B.8–B.9、Alg1–2/E.2/F.3.1。DINO region/attention以32mask干预logprob标签训练Pearson排序器，按completed span异步输出，是amortized干预sensor而非attention天然解释。`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) Interpretability Graph尚无这个模拟器分支，6gapDeep提案已获apr02必要source→owner支持，仍待锁/真正正文。correct-answer选择与排序不提供绝对effect/开放faithfulness，A100 attribution局部时延不覆盖DINO/标签/attention导出/queue及总Serving；保留实际backend/错误答案shift验收，不采用117×端到端加速。

### [Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning](https://arxiv.org/html/2604.16591v1)

v1 §3/Alg1、§4/Table2和AppB Step6已实际核。归一化projection不继承无偏：k1/q=(1,0)/g=(1,2)下两Rademacher分量的sign乘积期望0，真实cosine=1/√5；因此不采用基于该桥的MSE保证，更新符号另待明确、不由此断言全部实现错误。两有限Alpaca场景/LoRA注入和F/R trade-off经验保留；6分纠错深入暂缓，恢复需估计保证/更新约定勘误。见[必要证据](../_sources/daily-20260421/V3_BATCH_16591_16656.md)，apr02已独立窄核通过，不是日Gate。

### [Spotlights and Blindspots: Evaluating Machine-Generated Text Detection](https://arxiv.org/html/2604.16607v1)

v1 §3–5/AppA实际核，后发v2不继承。七英语集/22变体、novel-human切片、0.5与独立1000样本EER阈值分别说明类别率/threshold×domain改变排序；human-only accuracy不是生成recall或开放来源证明。5标准仅报告，保留具体受限反证、不采用通用检测不可能结论。当前OAI后发须与本家族v1processing/公告组合分清，见[必要证据](../_sources/daily-20260421/V3_BATCH_16591_16656.md)。

### [Lower Bounds and Proximally Anchored SGD for Non-Convex Minimization Under Unbounded Variance](https://arxiv.org/html/2604.16620v1)

v1 Assumptions1–3、§3–5主要算法/条件实际核，未重建所有证明。BG-0距初始化增长的variance下，epoch-anchor/PAGE与单epoch动态batch为不同分支；β=0也可满足受限smoothness复杂度，不能说anchor普遍必要。5标准仅报告条件oracle结果，不把它改成现代Transformer/GPU运行保证；理论hardware/SLO不适用。见[必要证据](../_sources/daily-20260421/V3_BATCH_16591_16656.md)。

### [Agentic Frameworks for Reasoning Tasks: An Empirical Study](https://arxiv.org/html/2604.16646v1)

v1 §3.4–3.7/§4.1/§5实际读，同GPT5.2双Agent、temperature0、1200/1024上限与retry/timeout只是一个执行配置。跨benchmark不同缺失分母及SEM不等重复运行统计，context/retry失败是具体运行反证但不能因共同prompt宣称纯架构因果。5标准仅报告，host P40/L4不是GPT服务硬件，不采产品长期排行。见[必要证据](../_sources/daily-20260421/V3_BATCH_16591_16656.md)。

### [Defragmenting Language Models: An Interpretability-based Approach for Vocabulary Expansion](https://arxiv.org/html/2604.16656v1)

当前采用：**整合** — `MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

v1 §3–6/Table1/AppA实际核；词/affix可组合readout→Procrustes/RMS初始化→embedding-only LAPT与added-token优先路径带来的短项反收益构成具体分支。`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md)现有联合迁移没有item selection×初始化/优先匹配反收益这组责任，拟6分gap深入；仅提案，无共享锁/实际采用。十四语言有限模型、Latin FVT优势/不支持语言退步/4Bthinking负例保留，token减少不等端到端省时或内部语义保证。见[必要证据](../_sources/daily-20260421/V3_BATCH_16591_16656.md)，apr02实际source→owner已通过，未写后。

### [Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs](https://arxiv.org/html/2604.16659v1)

v1 §3–5.5/AppA已实际读：benign选样的语义/声学距离与text/audio对照揭示冻结encoder不等安全保持。三个架构方向相反、Qwen远筛仍退步，refusal方向的comply分母仅1，架构比较不是因果干预；系统prompt受限结果不证明开放防御。Ch72已有benign更新与分布外安全slice责任，本次具体模态实验仅报告，不称全部机制已有覆盖。2+2+2=6保护深入；必要配置/成本见[证据](../_sources/daily-20260421/V3_BATCH_16659_16684.md)，待非作者有限核。

### [Rewind-IL: Online Failure Detection and State Respawning for Imitation Learning](https://arxiv.org/html/2604.16683v1)

v1 IV-B–D/V/VI实际读：TIDE触发、模板slot选址与物理action重放分权，clear queue/ensemble而保slot。经验成功frame阈值不证明time-uniform风险，旧action不恢复完整scene；single disturbance、6真机+3模拟限制，scene验证/collision-free恢复仍future。具体恢复recipe有价值，但不据局部计时/成功率升级Ch26通用安全机制，6保护深入Only，见[证据](../_sources/daily-20260421/V3_BATCH_16659_16684.md)，待非作者必要核。

### [DARLING: Detection Augmented Reinforcement Learning with Non-Stationary Guarantees](https://arxiv.org/html/2604.16684v1)

v1 §3–5/Assumptions4.7/4.10/Theorem4.11实际核：forced probes监测reward/transition后在episode末reset。探测rank不足使正交变化不可见，reachability/静稳长度为理论前提；Remark5.1说明实验不满足这些前提，经验不替代证明。5分标准Only，不将条件RL结果写成现代Agent/Transformer保证；未重建全部附件证明，见[证据](../_sources/daily-20260421/V3_BATCH_16659_16684.md)，待非作者有限核。

### [Evaluating Tool-Using Language Agents: Judge Reliability, Propagation Cascades, and Runtime Mitigation in AgentProp-Bench](https://arxiv.org/html/2604.16706v1)

官方abs/v1、HTML及PDF首页/必要方法一致支持当前2,300traces而非旧库存规模；§4–6已定点核。九模型非显著Spearman不能证明独立，且两臂同启发式judge不证明误判偏差自动抵消；100项主要单人标、仅7项双标重叠，不能沿旧双人一致性口径。暂缓中心独立性/净mitigation保证，保留有限协议与经验而非全部否定；恢复需适当独立性设计及两臂人工outcome/abstention分母。6分纠错深入，不写Books，见[必要证据](../_sources/daily-20260421/V3_BATCH_16706_16725.md)。

### [How to Approximate Inference with Subtractive Mixture Models](https://arxiv.org/html/2604.16714v1)

§2–4/6实际核：负权不能作latent categorical采样；平方构造与可积normalizer保证合法密度，正负期望差可用两组ancestral samples估计。抵消处小q造成大权重，safe component与初始化/预算改变取舍；不采用无条件最优proposal或把估计样本当目标生成样本。5分标准Only，条件推断基础贡献可保留，未验证Transformer/Serving收益，见[必要证据](../_sources/daily-20260421/V3_BATCH_16706_16725.md)。

### [Scalable and Adaptive Parallel Training of Graph Transformer on Large Graphs](https://arxiv.org/html/2604.16715v1)

§2.2–5实际核：AG复制K/V与A2A交换head后每卡存全图，graph storage与activation/collective成本不同。SDDMM/SpMM使边E与节点N分账，profile近似不保证任意拓扑选型最优；两8-GPU单机、hidden128/heads8、warmup2+10runs限定，fullgraph与聚类不同训练口径。6分标准Only，不把稀疏图路线直接推广dense causalLM，也不由微kernel数字写普遍训练倍率，见[必要证据](../_sources/daily-20260421/V3_BATCH_16706_16725.md)。

### [Active World-Model with 4D-informed Retrieval for Exploration and Awareness](https://arxiv.org/html/2604.16733v1)

§3–5实际核：camera sensing不是物理actuation，query-local点云的同时间完整/跨时间静态mask支持与生成缺区分开。Waymo/GEN3C支持受限观察proxy，GT不可得区只测证据区域和temporal指标，不能推未知区域truth、POMDP训练或controller安全；实际对读Ch25 memory/observed authority，6分标准Only，不强写有限recipe。见[必要证据](../_sources/daily-20260421/V3_BATCH_16733_16752.md)。

### [Reducing Peak Memory Usage for Modern Multimodal Large Language Model Pipelines](https://arxiv.org/html/2604.16734v1)

Alg1/§3–5实际核：block结构prefill后SnapKV/KeyDiff降低物化峰值，但append-before-evict有M+b瞬态，workspace另算。A100/InternVL3.5/Qwen2.5VL的block256受限结果保留小预算质量下降、较高TTFT和未测曲线估计；Table2部分delta不一致不外推。Ch45已承担临时容量/物理预算责任，5分标准Only不是宣称该算法已完整写入，见[必要证据](../_sources/daily-20260421/V3_BATCH_16733_16752.md)。

### [Why Training-Free Token Reduction Collapses: The Inherent Instability of Pairwise Scoring Signals](https://arxiv.org/html/2604.16745v1)

§3.1/Eq1/Assumption1/Prop1及§4–5必要理论与机制已读：常数epsilon符合单调非减却仅线性Delta，故不能推普遍固有超线性collapse；alpha>0额外分支、受限CATIS经验不随之否定。总扰动求和量到ranking-risk仍需条件桥。A100图像与VideoMAE吞吐成本不同，后者CATIS慢于简单baseline。6分纠错Deep暂缓普遍保证，不写Books；PDF工具失败未冒称已读，HTML中心式可核，恢复需明确加强假设/支持范围。见[必要证据](../_sources/daily-20260421/V3_BATCH_16733_16752.md)。

### [Don't Start What You Can't Finish: A Counterfactual Audit of Support-State Triage in LLM Agents](https://arxiv.org/html/2604.16752v1)

§3–6/10实际核：32条配对first-action诊断区分Clarify/Support/Abstain，但同会话含gold、关键词scoring不等API隔离或trajectory。Action-Only与PSC同分不证模型内部自知；删除动作类别的ablation不独立证明taxonomy普遍完整。Ch66 rule/estimate/decision已有基本职责，不冒称所有typed算法已覆盖；5分标准Only保留诊断材料，见[必要证据](../_sources/daily-20260421/V3_BATCH_16733_16752.md)。

### [StageMem: Lifecycle-Managed Memory for Language Models](https://arxiv.org/html/2604.16774v1)

官方abs/v1、HTML与PDFv1身份一致，旧库存后发题名/摘要不继承。§3–5的confidence准入/strength保留与压力settlement在同symbolic harness中提供控制分解；Mem0-style等近似不是生产实现完整对照，HotpotQA适配也不证长期可靠性。Ch77已保留Retention/Admission与多阶段生命周期职责，但不冒称本算法全已有；5分标准仅报告，见[必要证据](../_sources/daily-20260421/V3_BATCH_16774_16809.md)。

### [When Informal Text Breaks NLI: Tokenization Failure, Distribution Shift, and Targeted Mitigations](https://arxiv.org/html/2604.16787v1)

§3–4区分UNK不可逆丢失与in-vocabulary噪声错误权重，分别预处理/augmentation；emoji多对一与额外50%训练步骤不允许宣称语义保持或matched成本。ELECTRA14M/RoBERTa355M、有限SNLI/MNLI设置不是拒绝小模型的理由，也不推出普遍部署选择。对读Ch11基础表示边界，5分标准仅报告；[必要证据](../_sources/daily-20260421/V3_BATCH_16774_16809.md)保留具体配置与未证项。

### [LongBench: Evaluating Robotic Manipulation Policies on Real-World Long-Horizon Tasks](https://arxiv.org/html/2604.16788v1)

§3–5的完全可观测与历史歧义两regime揭示memory不总改善长执行，但六policy训练/架构及任务不同，不是同policy记忆开关因果比较。双臂20Hz、16-step chunk、每任务十次阶段分数与示范规模分开，不把千条示范当千个成功评测。5分标准仅报告受限反证，不用benchmark名称改变Ch66长期发布判断；见[必要证据](../_sources/daily-20260421/V3_BATCH_16774_16809.md)。

### [Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering](https://arxiv.org/html/2604.16790v1)

§3–4相同代码的A/B顺序和cue改变judge结果，执行oracle与judge合同分开；CoT/refined prompt改变判定程序，不能把每种变化都称无语义style。5352条、三judge、两个fresh sessions的受限consistency不证明长运行稳定性或完整代码语义。实际Ch66 judge identity/校准切片仍合理，5分标准仅报告这组反证，见[必要证据](../_sources/daily-20260421/V3_BATCH_16774_16809.md)。

### [Continuous Limits of Coupled Flows in Representation Learning](https://arxiv.org/html/2604.16801v1)

Theorem3/AppB.4 Theorem11与ODE已定点核。后者确有top-m非零初始投影假设，但取Σ=diag(3,2,1)、m2、两行同为(1,1,0)，谱隙和非零投影均满足，ODE保持rank1，不能得到2维principal rowspace。仅隔离非零投影充分推出完整主空间的扩展，不否定Lyapunov局部条件或典型满rank分支。5分纠错深入、暂缓；恢复需加强rank/初始化条件及对应证明，精确反例见[必要证据](../_sources/daily-20260421/V3_BATCH_16774_16809.md)。

### [A Mechanism Study of Delayed Loss Spikes in Batch-Normalized Linear Models](https://arxiv.org/pdf/2604.16809v1)

实际PDF主文§3–5/Lemma7而非全50页附件：白化线性square loss中scale追赶改变effective LR，方向离轨后的norm增长又产生负反馈；两个充分阈值不是完整相图。logistic部分每例active margin强条件只支撑有限方向前兆，不推一般loss spike。Ch17的Norm与LR联合职责不因此成为causalLM保证；5分标准仅报告有条件机制，[必要证据](../_sources/daily-20260421/V3_BATCH_16774_16809.md)保留条件和成本未披露范围。

### [Introspection Adapters: Training LLMs to Report Their Learned Behaviors](https://arxiv.org/html/2604.16812v1)

当前采用：**整合** — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

续跑独立状态：apr02源→Ch66实际缺口通过，尚无共享写入/写后；以下作者原提案的‘待源/owner’阶段已由此定点核替代，其他边界不变。

§2–4/§6实际核：冻结共同base的behavior LoRA变体，跨变体联合训练同一报告adapter，SFT/DPO抑制错报；Ch66 model-specific claim sensor尚缺这一训练身份分支。AuditBench十预测any-correct不等一次query检测率，sandbag替代指标与高FPR/构造成本不能变成内部自知或自动发布权。6gap深入，拟在Ch66 sensor主线补身份与诊断权边界，尚待非作者源/owner、锁与真实写后；不是已整合，详[必要证据](../_sources/daily-20260421/V3_BATCH_16812_16830.md)。

### [SafeDream: Safety World Model for Proactive Early Jailbreak Detection](https://arxiv.org/html/2604.16824v1)

§3–4/AppB必要协议已读：冻结Qwen layer19状态、69维projection、累积风险与灰区两池imagined rollout，是实际保护原型。48个latent预测步及原模型hidden前向不因1.2M模块变免费；alignment拒绝回读与guard内容分类不是完全matched，共享labelers不等独立真值。6安全深入仅报告，不把经典CUSUM最优性、提前lead或虚拟用户分布升级生产安全保证；[必要证据](../_sources/daily-20260421/V3_BATCH_16812_16830.md)。

### [The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Distillation](https://arxiv.org/html/2604.16830v1)

§2/3/4/8与AppA.1实际核：同joint条件期望塔律有效，但teacher混合成功率到另一无特权generation policy缺识别桥；teacher .4/.8混合.6而student .2可同时发生，不能不加条件推出部署投影。K8估prompt-marginal成功率，不自动校准本条答案；仅改位置loss不隔离共享参数。6纠错深入、窄理论暂缓，不否定全部经验；恢复需一致概率桥/收窄声明而非更多benchmark，见[必要证据](../_sources/daily-20260421/V3_BATCH_16812_16830.md)。

### [Towards Deep Encrypted Training: Low-Latency, Memory-Efficient, and High-Throughput Inference for Privacy-Preserving Neural Networks](https://arxiv.org/html/2604.16834v1)

§V–VIII实际读：downsample空出CKKS slots后mask/rotation合并中间ciphertext，提高后层effective batch；rotation/bootstrap keys按block group驻留/替换。具体新执行分支5标准Only，摊销不等单请求尾延迟，HE-friendly ResNet/CIFAR的布局与非线性复用不证明encrypted training或Transformer直接兼容；[必要证据](../_sources/daily-20260421/V3_BATCH_16834_16850.md)保留配置与未证范围。

### [DART: Mitigating Harm Drift in Difference-Aware LLMs via Distill-Audit-Repair Training](https://arxiv.org/html/2604.16845v1)

§2–3及AppA.2–A.3实际核：gold条件label改善可与rationale harm漂移共存，paired audit/加权repair保留两种责任。AppA明确testprompts/gold用于transductive repair，Table2同test最终结果不是独立heldout；外部query各自协议不能自动替换主结果。6保护/评价DeepOnly，保留修复已知cases可能有效，不用“不背诵原rationale”声称未见prompt，更不泛化accuracy/safety无冲突；[必要证据](../_sources/daily-20260421/V3_BATCH_16834_16850.md)。

### [Refinement of Accelerated Demonstrations via Incremental Iterative Reference Learning Control for Fast Contact-Rich Imitation Learning](https://arxiv.org/html/2604.16850v1)

§III.B–D/Alg1与§IV实际核：加速demo改变contact dynamics，逐速已修reference warm-start再用真实tracking误差修复，ACT训练继承这些实际轨迹。两方案插孔都100%而force不同，擦除未全优于直接回放；5StdOnly保留具体调度反证与采集成本。reference只是proposal，compliance controller仍拥物理提交权，不采用通用10倍安全或跨任务VLA保证；[必要证据](../_sources/daily-20260421/V3_BATCH_16834_16850.md)。

### [When W4A4 Breaks Camouflaged Object Detection: Token-Group Dual-Constraint Activation Quantization](https://arxiv.org/html/2604.16855v1)

§3–4/5.1–5.3及S1.2实际读：token-local group抑制背景range影响，step/zeroization目标改善弱边界表达；但QDQ反量化后仍浮点Linear/Conv，不能把W4A4标签当原生四位执行证据。两CODbackbone/四测试集的具体反证以5标准仅报告，未推LLM或端到端收益，见[必要审阅](../_sources/daily-20260421/V3_BATCH_16855_16883.md)。

### [Governed MCP: Kernel-Level Tool Governance for AI Agents via Logit-Based Safety Primitives](https://arxiv.org/html/2604.16870v1)

§3–6实际必要核：WASM唯一host→kernel六层gateway是执行身份，ProbeLogits的作者101条labels是另一证据对象；ring0不使classifier成为真值。effective v1恢复后不采用旧快照latency/line-count；并发TOCTOU、恶意model、执行后output检查与provenance缺口明确。6安全深入仅报告，不推所有native MCP无旁路或生产安全保证，见[必要审阅](../_sources/daily-20260421/V3_BATCH_16855_16883.md)。

### [PRISM: Probing Reasoning, Instruction, and Source Memory in LLM Hallucinations](https://arxiv.org/html/2604.16909v1)

§2.2–3.1/4.1/Table3/4.2实际核。同Llama3.1-8B一shot下reasoning SFT改善RE却损害KE/KM/IFE；任务taxonomy及attention图不成为内部知识oracle。5标准已有覆盖，Ch29能力回退与匹配轨迹/多切片回归已具体承载收益不豁免退化，不说完整新benchmark已存在。采样grid/训练预算限制见[必要笔记](../_sources/daily-20260421/V3_BATCH_16902_16917.md)。

### [The Cognitive Penalty: Ablating System 1 and System 2 Reasoning in Edge-Native SLMs for Decentralized Consensus](https://arxiv.org/html/2604.16913v1)

§3–4/Table1–3实际核：21提案各20重复，think切换、T.6/max8000、JSON final verdict，共同输入可比较该配置invalid与时延，但重复不是独立提案，token truncation不证明能力归零或参数知识因果。5标准Only，不采用100%安全/System1普律，具体边界见[必要笔记](../_sources/daily-20260421/V3_BATCH_16902_16917.md)。

### [x1: Learning to Think Adaptively Across Languages and Cultures](https://arxiv.org/html/2604.16917v1)

§2.1–2.2/3.1/Table1–2实际读：自trace多语言翻译后按答案/文化judge选优、丢平局再训；step1除32B外full-param、step2全LoRA，不将全流程误称低成本LoRA。5标准Only，五backbone/8×A80080GB/Mean@3/max32768是实验身份；gold选择/训练不等绝对知识固定，部分compliance退步、总训练/生成成本未matched，不推通用语言选择规律。详[必要笔记](../_sources/daily-20260421/V3_BATCH_16902_16917.md)。

### [Noise-Adaptive Diffusion Sampling for Inverse Problems Without Task-Specific Tuning](https://arxiv.org/html/2604.16919v1)

实际核§2.2/§3.1–3.3/Alg1、§4/§5与A.9必要成本。确定性DDIM定义noise posterior有具体机制，但Alg1拒绝后缩δ并重抽momentum，直到accept才计迭代；accepted-only jump chain不能自动继承普通MH holding/invariance。5分纠错深入、中心posterior保证暂缓，不否定100图重建或所有经验；一般对称三态核的move率(.2,.5,.5)给必要反证而非其具体HMC数值复现。恢复需实际transition/合法adaptive proof，见[必要证据](../_sources/daily-20260421/V3_BATCH_16918_16940.md)。

### [Alignment Imprint: Zero-Shot AI-Generated Text Detection via Provable Preference Discrepancy](https://arxiv.org/html/2604.16923v1)

§3–4及B.1实际必要核：base/aligned差×信息权重×perturbation标准化是具体检测统计；主文1–2条件不能掩盖B.1的variance/CLT额外4–5，理想SFT tilt不等实际神经训练恒等式。5标准Only，默认Llama2 pair、domain/edit/length与300条batch1 timing受限，XSum weighted score低于Δ的反例保留；不把统计分类升级作者身份保证。见[本批证据](../_sources/daily-20260421/V3_BATCH_16918_16940.md)。

### [No One Fits All: From Fixed Prompting to Learned Routing in Multilingual LLMs](https://arxiv.org/html/2604.16937v1)

§3–7/Table1–3实际读：两路响应都生成后才classifier择优，GlobalMMLU10%train/90%test与跨格式评价是有限协议，不是生成前便宜router。5标准Only，prompt自路由反收益/语言任务依赖值得报告，但overlap importance、resource/翻译质量相关不识别唯一因果；any-correct oracle与双生成开销分开，不推普适部署。见[必要证据](../_sources/daily-20260421/V3_BATCH_16918_16940.md)。

### [Better with Less: Tackling Heterogeneous Multi-Modal Image Joint Pretraining via Conditioned and Degraded Masked Autoencoder](https://arxiv.org/html/2604.16952v1)

exact-v1 III-C/D Eq3–6、IV-A/B TableII与IV-C实际核：条件化残差承接contrastive loss，灰度重建目标减少难以跨传感器预测的谱信息，5分标准仅报告。base residual仍有梯度路径，互信息最大化不自动令conditional entropy归零，不采用‘原表示已完全不受约束’保证。79M HiViT/DINOv3-Sat、1M样本、8×4090D、batch2048、不同epoch预算只支持受限目标选择，不将遥感配方泛化为全部VLM或只因领域标签拒绝。必要证据与未披露配置见[本批笔记](../_sources/daily-20260421/V3_BATCH_16952_16972.md)。

### [Open-TQ-Metal: Fused Compressed-Domain Attention for Long-Context LLM Inference on Apple Silicon](https://arxiv.org/html/2604.16957v1)

exact-v1 §§3.1–3.4/Alg1、§4/Tables1–6与§7实际核：register内dequant、online-softmax及split-K partial/reduce有具体执行路径，但一般q/k夹角下Eq6误差公式缺条件，层相关系数乘方也不是完整误差证明。6分纠错深入仅报告，不否定融合实现。M1Max64GB/32core、4bit weights/int4KV、具体Gemma/Llama设置下kernel与容量收益不等总生成，128K+未测RULER/NIAH/PPL，局部top1不等exact概率；Ch49图依赖/Ch45量化布局和查询联验已有长期原则，不追加Metal宣传。详细边界见[本批笔记](../_sources/daily-20260421/V3_BATCH_16952_16972.md)。

### [In-Context Learning Under Regime Change](https://arxiv.org/html/2604.16988v1)

实际读§2.1–2.2/3.1–3.2/5：Gaussian prior/noise、单变点、有界输入标签下，用prefix统计与候选segment subtraction构造posterior averaging；未知切分的head资源不等已知切分常数资源。存在性不保证GD学得或一般变点恢复，训练已含变点支持范围，相关regime旧context仍可经prior有用。2+1+2=5标准仅报告，不新增Ch5普律；必要条件与局部合成实验见[本批证据](../_sources/daily-20260421/V3_BATCH_16988_17022.md)，有限非作者复核已通过，见§6。

### [SPS](https://arxiv.org/html/2604.16995v1)

实际核§3.1–4.2/Eq4、§5/Table1、AppC/Alg1及[官方PDFv1](https://arxiv.org/pdf/2604.16995v1)第5/15页（工具零基索引4/14）：负forward KL与算法明确minimize方向不一致。q=(1,0)、p=(a,1-a)时loss=log a，最小化趋a=0而非匹配q；PDF相同所以不是HTML孤证排版。2+2+2=6纠错深入暂缓，只隔离中心目标，不推全部代码/实验错误；700步内Avg128择优不等独立发布评价，反收益slice保留。恢复需目标方向与实际实现必要说明，详[本批证据](../_sources/daily-20260421/V3_BATCH_16988_17022.md)，root已完成该窄反例的非作者复核。

### [Utility-Preserved Speech Anonymization](https://arxiv.org/html/2604.17000v1)

实际读III-B/C、IV-A/B、V-A/B、VI/TablesIII/VI/VII：声纹匿名化与内容PII替换拥有不同保护对象；utility在匿名数据上重训ASR/TTS/SER后测原数据，而非只固定模型打分。ignorant与lazy-informed attack的EER差距不能外推开放匿名性；5个inference seeds不是5次重训。2+1+2=5安全深入仅报告，保留NER四类/C-ASV分母、训练与runtime成本，不新增平台privacy保证。配置与限制详[本批证据](../_sources/daily-20260421/V3_BATCH_16988_17022.md)，待非作者有限核。

### [Semantic Equivalence Self-Play](https://arxiv.org/html/2604.17010v1)

实际读§3.1–3.4/4/5.3–5.4/8：等价variant要LiquidHaskell proof、非等价要divergent input，先验证generator label再训练evaluator；实现为rejection-sampling SFT，不是已经RL。受限可反射/终止片段、低proof yield与约150对的volume-control不证明全程序语义或匹配总compute，CodeXGLUE recall/F1有退步。2+1+2=5标准仅报告这个证据类型/验证吞吐分支，不冒称精确配方书稿已有；详[本批证据](../_sources/daily-20260421/V3_BATCH_16988_17022.md)，待非作者有限核。

### [Mini-BEHAVIOR-Gran](https://arxiv.org/html/2604.17019v1)

实际读§3/4.1–4.4/Table5/7：同场景改变instruction粒度，粗端成功率反弹与language grounding增强是不同判断；弱化language与visual-only predictor只支持受限shortcut解释。20离散任务、每任务50训练/10评价、width来自symbolic plan且分组用阶段一相关性，不能作在线难度或唯一因果；width≥4仅3任务覆盖和attention非因果保留。2+1+2=5标准仅报告，不推广真机U形规律，详[本批证据](../_sources/daily-20260421/V3_BATCH_16988_17022.md)，待非作者有限核。

### [Annotation Entropy Predicts Per-Example Learning Dynamics in LoRA Fine-Tuning](https://arxiv.org/html/2604.16332v1)

§3–5与Limitations已实际读，ChaosNLI逐item分歧与AULC在受限模型对照中改变rank/loss验收的诊断责任；四encoder有FullFT而decoder没有，soft-label并非已证修复。实际Ch30 rank段后已写item分布与容量配置分账，保留高分歧不自动等错误数据、关联不识别唯一rank原因与静态rank共存；root实际源→owner及写后非作者PASS。 2+2+2=6、知识缺口深入、真实整合 `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)，不预支日级Gate。

### [Stream2LLM: Overlap Context Streaming and Prefill for Reduced TTFT](https://arxiv.org/html/2604.16395v1)

§4.1–4.4/6.1–6.4已读。prompt append/update到达先触发只计划的分析，第二阶段才分配/抢占；真实token LCP确定GPU/CPU KV后缀失效。Ch56 FlowPrefill邻接正文已实际整合，保留H100/H200、Llama3.1-8B TP2、PD-prefill-only，DefaultStream median改善/P99退步，不承诺TPOT或生产SLO。root实际源与正文/邻接写后PASS。 2+2+2=6、知识缺口深入、真实整合 `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，不预支日级Gate。

### [Crowded in B-Space: Calibrating Shared Directions for LoRA Merging](https://arxiv.org/html/2604.16826v1)

§2～5/Table1～3及必要附录已读；B拼接SVD的energy shrink/norm restore是premerge proposal，再交原merger。Ch30 ACT-Mat之后已实际写B-spectrum与决策分布目标分权，BA不变的gauge变换仍改变B能量，故proxy不证明共享语义能力；TIES finance退步与范数恢复slice反例保留，静态/完整delta合并仍共存。root实际源/owner与写后PASS。2+2+2=6、知识缺口深入、真实整合 `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)，不预支日级Gate。原必要记录仍见[日内证据](../_sources/daily-20260421/V3_BATCH_16812_16830.md)，没有删除有效证据。

### [D-QRELO: Training- and Data-Free Delta Compression for Large Language Models via Quantization and Residual Low-Rank Approximation](https://arxiv.org/html/2604.16940v1)

§3–5及必要表已读；FullFT已产生训练成本，均值绝对尺度的sign delta再加residual SVD只压缩后续派生资产。Ch30 Merge/资产主线已真实写入，不误称训练LoRA、退还训练成本或统一byte cap，保留dtype/packing/rank/离线SVD成本与质量反收益。root实际源/owner及写后PASS。 2+2+2=6、知识缺口深入、真实整合 `TRAIN-LORA` [Ch30](../../../../books/part-04-training-system/30-lora.md)，不预支日级Gate。

### [When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano](https://arxiv.org/html/2604.17040v1)

实际读§3～5/Table1/2。五种子VS-WNO/dense WNO在Jetson eager batch1比较：模型稀疏未使dense卷积与DWT forward构造/launch减少；参考100测试质量与部署8样本sanity分母不同，不能说dense所有质量均更优。Ch49现执行图/launch成本与稀疏模式kernel消费已承载长期判断，5标准已有覆盖；板级能耗/unified RAM、seed20 trace不推通用GPU收益。 具体公开链、条件、代价与反证见[四项必要证据](../_sources/daily-20260421/V3_BATCH_17040_17056.md)，有限非作者及日级验收已通过，见§6。

### [SIF: Semantically In-Distribution Fingerprints for Large Vision-Language Models](https://arxiv.org/html/2604.17041v1)

实际读§3/4/5/6.1/11～12：冻结LVLM，对image用水印/CE目标及两pass表示扰动优化，避免query/output语义异常被reference替换。每query有限unrelated-model最大z校准只使该校准集无命中，不证明未来总体零FP；LLaVA剪枝slice也非全面最优。6保护深入仅报告，Ch59黑盒provenance已有版本/阈值/误检与非ownership证书边界，不说精确算法全已写；不采零latency/零FP宣传。 具体公开链、条件、代价与反证见[四项必要证据](../_sources/daily-20260421/V3_BATCH_17040_17056.md)，有限非作者及日级验收已通过，见§6。

### [RLM-on-KG: Heuristics First, LLMs When Needed](https://arxiv.org/html/2604.17056v1)

实际读§3/4/5/6必要对照：mention图只co-mention，LLM发现collected候选后vector排序；heuristic可用工具更少、检索budget显著不同，gold mapping同embedding亦有confound。主Gemini vs GraphRAG非显著、小MuSiQue反收益，不能推普遍更优或唯一controller因果。5标准已有覆盖，Ch76 typed retrieval state/query policy与探索-排序-证据Gate分权和静态fallback已有具体论点。 具体公开链、条件、代价与反证见[四项必要证据](../_sources/daily-20260421/V3_BATCH_17040_17056.md)，有限非作者及日级验收已通过，见§6。

### [Sarus Suite: Cloud-native Containers for HPC](https://arxiv.org/html/2604.17064v1)

实际读§2～4必要架构/namespace/失败路径、§5.1/5.4/5.5及§6/7：每节点Podman namespace与rank setns、共享只读SquashFS、site CDI/hooks保留Slurm lifecycle ownership，rootless不等强sandbox。GH200/Slingshot/Slurm的Megatron mockpretrain与冷cache Pynamic分别验收，不把Kubernetes YAML本地执行当完整K8s controller，未披露precision/序列长度/SLO不补造。6分标准仅报告；具体HPC runtime integration有贡献，不把单site结果推广成默认方案或冒称算法全已有覆盖。详[必要记录](../_sources/daily-20260421/V3_BATCH_17064_17073.md)。

### [Trajectory-Restricted Optimization Conditions and Geometry-Aware Linear Convergence](https://arxiv.org/html/2604.17067v1)

实际读§2.2/2.4/3.1～3.2及§4限定：L-smooth f+凸g、步长1/L、每步restricted PL及tail containment才给局部收缩，PL→EB还要不变/closed K；并不证明自动进入良好集合。5标准Only，不因无LLM实验否定有条件理论，也不向现代Transformer/Adam写一般保证。证明附件未逐行复核，必要范围/具体数学条件在[本批证据](../_sources/daily-20260421/V3_BATCH_17064_17073.md)。

### [Stability-Weighted Decoding for Diffusion Language Models](https://arxiv.org/html/2604.17068v1)

§3～4/Alg1、§5.1/5.6/5.7及AppA已实际核。旧context为空、目标B与未揭示C相同Bernoulli(.5)、这一轮揭示独立A：temporal KL为0而剩余MI为log2，故理论下界小不能给§4.2声称的总依赖预算上界；不否定理想一致joint下的新context CMI恒等或全部heuristic经验。Alg1和理论的KL方向也不同。6纠错深入暂缓、无Books正面写入；LLaDA/Dream、4A100、256/512输出/EB.1与λ选择为受限评价，NFE非SLO、λ1有退步。恢复只需一致方向与合法上界/模型近似桥，详[窄记录](../_sources/daily-20260421/V3_BATCH_17064_17073.md)，待非作者定点核。

### [Abstain-R1: Calibrated Abstention and Post-Refusal Clarification via Verifiable RL](https://arxiv.org/html/2604.17073v1)

§3～6/Limitations与AppA实际核：answerable符号正确/错误拒答惩罚、unanswerable拒答与reference澄清reward分权；Qwen3B全参SFT/GRPO、4A100、4.6k合成SFT/50k SUM、训练judge与评价judge不同但不保证独立真值。按Abstain-Test-SUM选SFT checkpoint与发布heldout须分开，错误拒答反向slice及LLM语义匹配缺口保留。5标准Only，名称calibrated不等概率证明；不冒称本篇完整算法已有覆盖，不强写新机制段。详[必要记录](../_sources/daily-20260421/V3_BATCH_17064_17073.md)，未复现实验。

### [Understanding and Enforcing Weight Disentanglement in Task Arithmetic](https://arxiv.org/html/2604.17078v1)

§4.3/§5/Table1/G.4.2–G.4.3实际核：每个任务内部列正交惩罚都为0，仍可有两更新均I、cross-task cosine1，不能由惩罚建立跨任务独立采样。追加独立核指出G.4.3 Lemma3只给m≥d、d≥1，m=d=1时独立均匀Stiefel样本A/B为±1，内积期望0但绝对cosine恒1；因此独立均匀采样的零均值结论保留，高维集中及绝对cosine近零还需明确维数/集中界，不能外推到优化所得更新。作者亦定点重开官方该Lemma与Part2确认条件。6纠错深入暂缓这两条保证桥，不否定TFS充分条件、可能的受限高维分支或全部CLIP经验；不写Ch30正面保证。恢复需分布条件证明、量化维度/集中界或收窄声明，详[本批记录](../_sources/daily-20260421/V3_BATCH_17078_17093.md)。

### [EvoComp: Learning Visual Token Compression for Multimodal Large Language Models via Semantic-Guided Evolutionary Labeling](https://arxiv.org/html/2604.17087v1)

当前采用：**整合** — `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。上文保存的早期拟稿时态由本处覆盖；必要机制已融入正文、root实际正文及邻接写后通过（[具名记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)），未复现实验、非日级Gate。

§3.1–3.3/Alg1与§4.1–4.3实际核：gold response loss离线搜索binary mask，之后训练不读gold的compressor，部署按query/visual概率选择；无反传仅指标签搜索，不是免训练，48候选×10代forward计成本。6缺口深入，拟`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)视觉selector段补标签特权/amortized部署验收，待非作者采用/写后。LLaVA质量反向slice和手机额外selector成本保留，gold loss不是真实证据充分性；详[本批记录](../_sources/daily-20260421/V3_BATCH_17078_17093.md)。

### [HarmChip: Evaluating Hardware Security Centric LLM Safety via Jailbreak Benchmarking](https://arxiv.org/html/2604.17093v1)

§III-B/C/§V/§VII实际核：六模型筛难度后十六模型评价含原六，Gemini3Flash judge亦被评；语言响应配合不等RTL真实恶意effect，EDA执行验证future。5保护深入仅报告；正文计数口径未一致、OpenRouter默认解码与选择分母不作总体安全排行，不向Ch66添加硬件攻防保证。具体边界见[本批记录](../_sources/daily-20260421/V3_BATCH_17078_17093.md)，未复现实验。

### [From Natural Language to Silicon: The Representation Bottleneck in LLM Hardware Design](https://arxiv.org/html/2604.17097v1)

III/IV-B/C/E/V-A实际核：lowering、simulation、FPGA不同幸存分母，conditional fit不是全任务交付；repair在Verilog级不证明原IR接口保持。三模型六IR/202教学任务、有限两FPGA、默认API无repeat/CI；HLS在小目标passing却大目标失败提示backend语义不能当仅容量控制。ECP5约47%是三模型条件率非加权均值，合并幸存者则18/33≈54.5%，不混用这两个口径。5标准Only，保IR/witness的受限贡献、不强写硬件指南，详[必要记录](../_sources/daily-20260421/V3_BATCH_17097_17108.md)。

### [Configuration Over Selection: Hyperparameter Sensitivity Exceeds Model Differences in Open-Source LLMs for RTL Generation](https://arxiv.org/html/2604.17102v1)

III/IV-B TablesI–III实际核：pilot选三模型扫108配置，best-grid与默认排名预算不matched，pass@5/HQI上界不等单次交付；弱rank相关不等完全无预测力。5标准已有覆盖，`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)完整subject明确runtime/decoding/adapter，ObservedCapability/ElicitationCeiling与pipeline分母已有正文。仅新增受限RTL证据，不泛化全部最佳温度或服务吞吐因果；详[必要记录](../_sources/daily-20260421/V3_BATCH_17097_17108.md)。

## 5. 缺口与下一步

**可执行普通工作：** 无。有限题摘、必要证据、Books及非作者日级验收均已收口；146=33整合+14已有覆盖+81仅报告+18窄争议，普通Books0。33项均有真实正文与具名写后记录。阶段数字与运行中断记录保存在[对账前日志](../_sources/daily-20260421/V3_SECTION5_STAGE_LOG_BEFORE_RECONCILIATION.md)，不是当前状态。

本轮23項实际采用覆盖Ch11/21/23/24/26/29/33/36/45/49/66/70/72/76/81，具体机制、条件和反例见§4与[root写后复核](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)。EvoComp仅细化selector构造/训练/部署；BranchBench仅细化creation与active execution capacity，不重复计原有机制。评分未抬升，未扩大270题摘/175必要范围或重读未变化附件。

**外部覆盖保留项：** OpenAI Research四月分页、Google Publications历史日停点、Meta Research历史目录、Kimi2026 Blog、MiMo无日期Blog及八机构GitHub创建/重要release历史停点。原始替代路径已在[来源独立审计](../_sources/daily-20260421/V3_SOURCE_ADMISSION_INDEPENDENT.md)有界检查；具体范围见§2。恢复需相应官方历史列表、可核日期与完整停止边界，或同事件artifact metadata；缺口不支持“零更新”“无遗漏”或候选/Books采用，不扩全年反复重扫。

**单家族日期/早发身份隔离：** PriceBlind16515、Agentic Coding Scaling16529、Unlearning Testing16536、HQA-VLAttack16499、UniCon16678、Visual Inception16966、17022、mEOL17054、Local Inconsistency17140、LASER17224、17249与Seed Agent-World18292不列确定的当窗候选、不评分、不写Books。各具体元数据/更早正式正文线索已保留在[日内证据](../_sources/daily-20260421/V3_EVIDENCE_NOTES.md)及§4/原始筛选记录：

- 16515/16529/16536/16966/17022/17249：提交或后日处理字段不能单独证明首次公开；需官方首次可用区间和对应版本。17249的01:00:06Z处理上界不足支持截点前组合，不等于证明晚首发。
- 16499/16678/17054/17140/17224：同家族已有正式出版或公开正文线索，精确first-public或本窗重要修订未恢复；只请求对应note/公告时间和正文身份，不凭新arXiv ID重复采用、不追完整发表史。LASER还保留旧Z/新Q坐标桥的具体风险，不给日期未明事件评分。
- 18292：官方目录仅04/20日历标签，v1 Updated跨截点、项目页无精确可用范围，仓库另为08/10公开说明；恢复官方首次正文公开组合，不把目录日期或仓库后发时间冒充本窗首发。

**中心声明窄隔离：** 16324、16426、16421、16424、16453、16471、16519、16521、16557、16591、16706、16745、16801、16830、16919、16995、17068、17078均在§4保留精确争议对象、反例/假设与重开条件；只隔离未成立的保证，不否定其他有效机制或全部经验、不进入Books正面采用。重开需要该命题的作者澄清/勘误、一致目标与实现/评价桥或相应证明，不需补读全部引用。已有有效独立反例核验复用；17068/17078的晚批必要独立复核及17078精确修正也已完成，不能据此跳过其余采用/Books/日级验收。

**撤回关闭：** 16502、17238官方撤回不保留selected、评分或Books采用；16902 v2官方Comments明确data error affects main results，原版采用关闭，v3恢复属于另一事件不回填，也不称当前全家族仍撤回。本日原始筛选保留必要处置依据，未发现需要清理的现存正面采用链，不删除其他有效证据。

146分母已冻结并通过最终非作者日级验收，普通Books0；本节外部限制与争议是终态保留项，不支持正面证据、Books或无遗漏断言，定点重开条件见各项。历史协调运行中断已恢复，不是primary材料缺失，不改变日期、范围和完成条件。

## 6. 复核

复核者：root（非报告作者）
结论：通过

最终146家族：33真实整合、14已有覆盖、81仅报告、18窄争议，普通Books0；审阅66深入完成、79标准完成、1争议。23项本轮落实均由root逐组实际顺读正文及邻接通过，原有10项有效实际记录复用。最终日级复核实际核对14来源及限制、日期组合与例外、逐项终态和33真实写后，并按执行、保护行为、路由、训练、记忆、编译理由分层打开16625/16762/16694/16804/16778/16498六项官方完整题摘，维持具体前分母关闭；不冒充270题摘或1260宽身份的全量非作者阅读。详细范围见[root最终日级记录](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)。

本轮最后有界采用复核已收口，作者已实际读完整审计并同步必要修正：

| 独立记录 | 实际范围与结果 | 不代表什么 |
| --- | --- | --- |
| [晚批七项](../_sources/daily-20260421/V3_LATE_SEVEN_17097_17139_INDEPENDENT_AUDIT.md) | 17097/17102/17111/17112/17126/17132/17139：6仅报告、1已有覆盖；17097非加权模型均值与合并幸存者比例已区分，两个保护行为反例独立通过 | 不验收全日来源、日期或实验复现 |
| [晚批八项](../_sources/daily-20260421/V3_APR02_LATE_EIGHT_17143_17187_INDEPENDENT_AUDIT.md) | 17143/17145/17147/17159/17172/17177/17182/17187：4已有覆盖、4仅报告；17159按安全评价边界实际深入，仍6分Existing | 不新增Books，不把厂商/环境排名当weights能力 |
| [此前晚批六项](../_sources/daily-20260421/V3_LATE_SIX_INDEPENDENT_AUDIT.md) | 17064/17067/17073/17093仅报告，17068/17078窄争议；17082具体前分母关闭；17078候选表/正文/笔记修正已由非作者核对 | 不由局部反例否定全部条件理论或经验 |
| [六项加日期例外](../_sources/daily-20260421/V3_APR02_BOUNDED_SIX_17087_17228_INDEPENDENT_AUDIT.md) | 17087/17180/17198/17228四窄gap写前通过，17219/17221仅报告，17224日期隔离字段；BranchBench现有机制正文不重计本轮新写 | source→owner不是实际整合 |
| [最后七项加元数据](../_sources/daily-20260421/V3_APR02_BOUNDED_SEVEN_17207_17248_INDEPENDENT_AUDIT.md) | 17210/17215/17237三个gap写前通过，17207/17211/17244/17248仅报告；17238撤回关闭、17249日期隔离 | 不以Updated证明截点或真实晚首发 |

未变化证据复用：root核16686/17104、16332/16826/16940、16395/16583的来源、owner、真实正文及邻接，七项通过；[Ch23三项写后审计](../_sources/daily-20260421/V3_APR02_CH23_THREE_WRITE_AFTER.md)支持16479/16462/16503。这10項继续有效，本轮另23项见[root实际写后复核](../_sources/daily-20260421/V3_ROOT_ACTUAL_WRITE_AFTER.md)，累计33真实整合。16351是现Ch76具体硬负例跨域代价和relevance/support已有覆盖，不声称原near-miss基准全已写。16988～17022及17040/17041/17054/17056有界采用核继续有效，不用历史阶段数作当前状态。

此前具名范围仍有效，包括[21项](../_sources/daily-20260421/V3_APR02_BOUNDED_21_INDEPENDENT_AUDIT.md)、[九项](../_sources/daily-20260421/V3_APR02_BOUNDED_9_INDEPENDENT_AUDIT.md)、[四项](../_sources/daily-20260421/V3_APR02_BOUNDED_4_16733_16752_INDEPENDENT_AUDIT.md)、[14项](../_sources/daily-20260421/V3_APR02_BOUNDED_14_16774_16850_INDEPENDENT_AUDIT.md)、[Hiera等五项](../_sources/daily-20260421/V3_APR02_BOUNDED_5_16855_16883_INDEPENDENT_AUDIT.md)、[撤回等五项](../_sources/daily-20260421/V3_APR02_BOUNDED_5_16902_16917_INDEPENDENT_AUDIT.md)、[FreshPER等五项](../_sources/daily-20260421/V3_APR02_BOUNDED_5_16918_16940_INDEPENDENT_AUDIT.md)、[Memory等七项](../_sources/daily-20260421/V3_APR02_BOUNDED_7_16952_16972_INDEPENDENT_AUDIT.md)。各记录的实际采用命题、数学反例、披露配置及不采用范围由对应笔记承载，不能把具名单篇核验相加冒充全部原始库存深审或零遗漏保证。

[14来源及首批准入有界审计](../_sources/daily-20260421/V3_SOURCE_ADMISSION_INDEPENDENT.md)和[最小消歧校准](../_sources/daily-20260421/V3_MINIMAL_DISAMBIGUATION_INDEPENDENT.md)可复用原始停点与具体裁决；§2及§5所列历史目录/artifact、日期与版本缺口依然精确保留。来源复核与部分否定侧抽查不等全1260题摘/全文已读。原复核阶段日志完整保存在[阶段副本](../_sources/daily-20260421/V3_SECTION6_STAGE_LOG_BEFORE_RECONCILIATION.md)，避免恢复时继承旧0/27/待审数字。

最终非作者日级核验已通过，Books与证据普通待办0。§5保留项以后只按精确材料重开受影响家族，不扩整日或其他日期；格式校验不替代实际研究和日级验收。
