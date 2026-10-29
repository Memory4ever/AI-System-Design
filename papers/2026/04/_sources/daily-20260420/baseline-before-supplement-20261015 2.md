# Daily Research — 2026-04-20

**规范：** V3
**窗口：** 2026-04-19T09:00:00+08:00 ～ 2026-04-20T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-28T12:31:19+08:00

## 1. 结论

已浏览447个跨分类去重库存标题作有界查漏，读150个完整题摘作贡献判断；不是447个当窗新论文、150个冻结候选或全文队列。首批九项准入独立校准为五项继续、四项具体关闭。旧V2.1 Complete和通用Existing不继承，旧正文完整保留在[归档](../_sources/daily-20260420/V2_1_README_BEFORE_V3.md)。

二十六项（含STOP临时前缀评分、Fleet、RPA、EasyRider、ARIA、SMC、Steering Vectors与AW-PSP）已通过必要源→实际owner与非书稿作者真实正文写后核。对初次127候选中72个仅报告项逐家族做[反向准入审计](../_sources/daily-20260420/V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)，并经作者纠错、非作者[十一项冲突逆向核](../_sources/daily-20260420/V3_ROOT_ELEVEN_REVERSE_ADMISSION_AUDIT.md)及[最终两项误拒纠正](../_sources/daily-20260420/V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)收口。终稿冻结111家族＝26已写后整合、13具体已有覆盖、54仅报告、18中央窄争议；另38项具名前关闭、15483一项首公开身份隔离，合150完整题摘。这不是按比例缩池。[非作者日级语义 Gate](../_sources/daily-20260420/V3_ROOT_DAILY_GATE_20260420.md)已通过；完成仅指确定候选安全终态，不声称外部历史目录已恢复或全网无遗漏。

## 2. 来源覆盖

以下实际原始访问的停点来自[恢复记录](../_sources/daily-20260420/v3-reopen-notes.md)；跨日未变目录只复用其可证明范围，不复制旧PASS。仅十四每日源和实际材料触发，不扫每周源。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | RSS跨Apr21 00Z→Hyatt Apr20 00Z→Codex Apr16 10Z，Hyatt原文部署案例无新机制/受控选择 | 受阻 | Research历史分页未达本窗；RSS只证可见News段，不支持全Research零命中；可核历史Research日列表返回后定点重开 |
| SRC-ANTHROPIC | Research71 dated条目跨Apr14 13:01Z→Apr22 14:12:30.673Z/14:27:03.434Z | 已检查 | 所见目录窗内无相关项，不外推全站 |
| SRC-GOOGLE-AI | Research April Blog九项Apr16→21；DeepMind页3七项Apr30/27/23/22/15/14/2，相关264条Apr22→Mar22 | 受阻 | Blog与DeepMind所见目录已跨窗；Publications年度771宽目录无日级首公开停点，不写全Research零命中，具名出版事件出现时再定点核 |
| SRC-META-AI | Research首页SSR不提供可靠行；官方[Publications第2页](../_sources/daily-20260420/V3_THREE_SOURCE_STOPPOINT_REOPEN.md)近期段May19→Apr16→Apr14/9跨窗无04/20项 | 受阻 | 只限可见Publication日期段；Research历史列表仍缺可靠逐条日期，不推断所有Blog/release零发布；可读官方历史页返回时重开该段 |
| SRC-QWEN | 动态API40项完整extra.date跨Apr18 10:00+08→Apr22 10:00+08 | 已检查 | 静态60/organization不冒充全部release/commit |
| SRC-DEEPSEEK | News16条Apr24→Dec1、Research Jun24→Feb25未变原始段落核后复用 | 已检查 | org39项仅辅助，不宣称全部仓库无事件 |
| SRC-MOONSHOT | kimi-cli100 releases读完，1.37 Apr20 16:01:36Z窗外→1.36 Apr17 14:10:46Z；官方Platform Blog当前26项最新2025 Nov7，见[窄复查](../_sources/daily-20260420/V3_THREE_SOURCE_STOPPOINT_REOPEN.md) | 已检查 | 限注册Blog与kimi-cli；不推断Moonshot所有仓库/未列研究零事件 |
| SRC-TENCENT-HUNYUAN | publicList POST pageNum1/pageSize100/renderType0，total9/list9，Apr23→Feb13 | 已检查 | 可选artifact403/503不等于58仓库全release已查 |
| SRC-ZAI | Research15/16项Apr29→Apr7→Apr1；release Jun16→Apr7→Feb12 | 已检查 | 部分GitHub403仅隔离可选发现，不取消Research停点 |
| SRC-BYTEDANCE-SEED | papers type1/count20/desc/page20，20项total242/next40/more，May12→Apr8；Blog type2/page0实际nested15项Apr22 16Z→Apr8 16Z停止 | 已检查 | AgentWorld CMS Apr19 16Z未证明当时正文公开，见§5 |
| SRC-BAIDU-ERNIE | Blog两页十项Apr30→Apr15→Feb6，2/2终页 | 已检查 | 只证明技术Blog所见范围 |
| SRC-XIAOMI-MIMO | Paper八项Jun29→Mar13；Blog相邻卡片MiMo-V2.5 Apr22→MiMo-V2-Pro Mar18，[原文日期](../_sources/daily-20260420/V3_THREE_SOURCE_STOPPOINT_REOPEN.md)跨本窗 | 已检查 | 卡片自身无日期，以相邻官方正文和可见排序停点；不推断站外零事件 |
| SRC-MINIMAX | EN/CN Blog12/13项跨窗；cli26 releases读完，1.0.12 Apr26 01:40:29Z→1.0.11 Apr17 20:51:17Z | 已检查 | Agent Tech Blog只May13单页，历史字段不足不写零命中 |
| SRC-ARXIV | 447有界标题查漏、150完整题摘逐项贡献判断；127→111经历[作者反向审计](../_sources/daily-20260420/V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)、[root 八项](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)、[三项](../_sources/daily-20260420/V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)、[十一项冲突](../_sources/daily-20260420/V3_ROOT_ELEVEN_REVERSE_ADMISSION_AUDIT.md)和[两项最终逆向纠错](../_sources/daily-20260420/V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)；窄公告/OAI/ID链见[日期说明](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)，cs.AR整月227仅补检、cs.CL请求429由既有原始库存与其他主题入口有界补足 | 已检查 | 来源/首公开只支持具名有限范围；cs.CL原请求受限、历史机构目录不保证全网零遗漏；日级核已签，见§6 |

## 3. 候选与判断

仅列已形成具体贡献/采用命题且通过终稿复核的111个家族。区间由官方公告时ID分配规则、Sunday20:00EDT公开槽、原始OAI与15314～16299前后边界联合推定；不把Submitted/Updated/DOIcreated单独当首公开。日期链的具名例外已隔离，见§5及[日级复核](../_sources/daily-20260420/V3_ROOT_DAILY_GATE_20260420.md)。两项从原前闭恢复的具体依据见[负侧逆向审校](../_sources/daily-20260420/V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [EvoRAG: Making Knowledge Graph-based RAG Automatically Evolve through Feedback-driven Backpropagation — 2604.15676v1](https://arxiv.org/html/2604.15676v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 反馈沿图路径更新关系，但归一目标与打印gradient不一致；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅中央印刷保证隔离，有限方法/表保留，重开见§4/5 |
| [SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems — 2604.16022v1](https://arxiv.org/html/2604.16022v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 动态机会集、任务完成与完成后的路径效用分账；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 受限支持/成本/反证，不新增普遍正文保证 |
| [Where does output diversity collapse in post-training? — 2604.16027v1](https://arxiv.org/html/2604.16027v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 后训练lineage与正确子集的多样性不能互换为唯一教师因果；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 受限支持/成本/反证，不新增普遍正文保证 |
| [Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning — 2604.16029v1](https://arxiv.org/html/2604.16029v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 临时评分adapter分支丢弃后恢复冻结前缀，不提交check状态；2 + 2 + 2 = 6 | 深入完成 | 整合 — MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md)，真实两段非作者写后通过 |
| [Stochasticity in Tokenisation Improves Robustness — 2604.16037v1](https://arxiv.org/pdf/2604.16037v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 分词与checkpoint联合行为接口，条件化uniform不等全支持uniform；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md)，联合行为接口具体命题 |
| [Elucidating the SNR-t Bias of Diffusion Probabilistic Models — 2604.16044v1](https://arxiv.org/html/2604.16044v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | Jensen能量不增不能推出一般Gaussian残差和逐步低SNR保证；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅中央印刷保证隔离，有限方法/表保留，重开见§4/5 |
| [On the Rejection Criterion for Proxy-based Test-time Alignment — 2604.16146v1](https://arxiv.org/html/2604.16146v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | rejection条件等价与相对proxy-confidence阈值有有限替代分支；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限支持/成本/反证，不新增普遍正文保证 |
| [AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency — 2604.16158v1](https://arxiv.org/html/2604.16158v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | mask重新启用叙述与正向最大化H/c的打印reward方向冲突；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅中央印刷保证隔离，有限方法/表保留，重开见§4/5 |
| [Sketching the Readout of Large Language Models for Scalable Data Attribution and Valuation — 2604.16197v1](https://arxiv.org/html/2604.16197v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | readout sketch的structural bias及反向交叉项限制无偏/方差保证；2 + 2 + 2 = 6 | 争议 | 暂缓 — 仅中央印刷保证隔离，有限方法/表保留，重开见§4/5 |
| [NVBench: A Benchmark for Speech Synthesis with Non-Verbal Vocalizations — 2604.16211v1](https://arxiv.org/html/2604.16211v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | inventory coverage、event correctness、placement与speech质量分开；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 受限支持/成本/反证，不新增普遍正文保证 |
| [Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations — 2604.16217v1](https://arxiv.org/html/2604.16217v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 有限candidate缺失不能由∞阈值/rank事件转为正确答案coverage；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅中央印刷保证隔离，有限方法/表保留，重开见§4/5 |
| [Neurosymbolic Repo-level Code Localization — 2604.16021v1](https://arxiv.org/html/2604.16021v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 空关系的有限mutation只作诊断，不能静默放宽原查询条件；2 + 2 + 2 = 6 | 深入完成 | 整合 — AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，procedural index后真实两段，root非作者实际写后通过 |
| [One-Shot Generative Flows: Existence and Obstructions — 2604.15439v1](https://arxiv.org/html/2604.15439v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | sample插值与conditional直流分开，coupling/辅助噪声改变结构可行性；2 + 2 + 3 = 7 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，并行/少步标题后实际两段，root写后通过 |
| [Neural Continuous-Time Markov Chain: Discrete Diffusion via Decoupled Jump Timing and Direction — 2604.15694v1](https://arxiv.org/html/2604.15694v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | exit-rate/destination两学习目标与absorbing固定rate特例分责；2 + 2 + 3 = 7 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，joint artifact后真实两段，root写后通过 |
| [Faster LLM Inference via Sequential Monte Carlo — 2604.15672v1](https://arxiv.org/html/2604.15672v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 多粒子未提交祖先状态经target批量加权/重采后只交付单输出，单轮误差不等整轨迹保证；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)，Cactus后真实两段，root写后通过 |
| [Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility — 2604.15579v1](https://arxiv.org/html/2604.15579v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 可执行policy检查与模型判词分权、测量仅覆盖已实现predicate；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Policy-as-Data及effect/utility联合验收；不称所有六类配方已覆盖 |
| [Majority Voting for Code Generation — 2604.15618v1](https://arxiv.org/html/2604.15618v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 可执行program medoid区别逐input mode，共识非correctness oracle；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — mean改善与best/再次FMV退步同存，真实test-input权限和执行成本保留 |
| [Too Private to Tell: Practical Token Theft Attacks on Apple Intelligence — 2604.15637v1](https://arxiv.org/html/2604.15637v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 匿名不可关联性与holder绑定、一次子token与可再兑换rootcredential分责；2 + 2 + 3 = 7 | 深入完成 | 整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，生命周期威胁末实际两段，root写后通过 |
| [LLMs Corrupt Your Documents When You Delegate — 2604.15597v1](https://arxiv.org/html/2604.15597v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | round-trip保留性与forward编辑正确分责、no-op/抵消使高分不拥有完成权；2 + 2 + 3 = 7 | 深入完成 | 整合 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，full-cycle后实际两段，root写后通过 |
| [GroupDPO: Memory efficient Group-wise Direct Preference Optimization — 2604.15602v1](https://arxiv.org/html/2604.15602v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | group系数计算与逐sample backward保持同θ一阶而非loss/Hessian，activation与totalpeak分开；2 + 2 + 3 = 7 | 深入完成 | 整合 — TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md)，工程流后实际两段，root写后通过 |
| [Preregistered Belief Revision Contracts — 2604.15558v1](https://arxiv.org/html/2604.15558v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | evidence准入与实际operator执行分责，外部固定belief vector保守分支不证明真值；2 + 2 + 3 = 7 | 深入完成 | 整合 — AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，共识后实际两段，root写后通过 |
| [Why Fine-Tuning Encourages Hallucinations and How to Fix It — 2604.15574v1](https://arxiv.org/html/2604.15574v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 表达已知/获取新事实决定冻结与reference约束选择，实际owner gap深入；2 + 1 + 3 = 6 | 深入完成 | 整合 — TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，forgetting后目标分叉两段，root写后通过 |
| [Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation — 2604.15559v1](https://arxiv.org/html/2604.15559v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 过滤目标字词后trajectory仍可改变下游first-action，需transfer审计；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，公开任务无关输出的training artifact/下游行为核验命题，不称Agent协议或具体数值全部已覆盖 |
| [Reward Weighted Classifier-Free Guidance as Policy Improvement in Autoregressive Models — 2604.15577v1](https://arxiv.org/html/2604.15577v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | conditional likelihood-ratio指导与有限prior/负zscore实现区别；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 保通用AR近似机制/成本反证，不采用无条件policy improvement或恢复分子领域 |
| [PolicyBank: Evolving Policy Understanding for LLM Agents — 2604.15505v1](https://arxiv.org/html/2604.15505v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 规范误解与执行偏离需不同诊断，trusted feedback只修派生解释不自授policy authority；2 + 2 + 3 = 7 | 深入完成 | 整合 — AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，advisory后实际两段，root写后通过 |
| [LACE: Lattice Attention for Cross-thread Exploration — 2604.15529v1](https://arxiv.org/html/2604.15529v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 同请求横向representation routing区别独立采样，新增边需单独mask与成本身份；2 + 2 + 3 = 7 | 深入完成 | 整合 — MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)，Mask后实际两段，root写后通过 |
| [FineSteer: A Unified Framework for Fine-Grained Inference-Time Steering in Large Language Models — 2604.15488v1](https://arxiv.org/html/2604.15488v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 输入gate与query-specific prototype干预分责，具体owner缺口深入；2 + 1 + 3 = 6 | 深入完成 | 整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，输入条件化gate后的when/how真实两段，root实际写后通过 |
| [Predicting Where Steering Vectors Succeed — 2604.15557v1](https://arxiv.org/html/2604.15557v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | output-alignment诊断与可干预性分开，linear probe可读不保证有效steering；2 + 1 + 3 = 6 | 深入完成 | 整合 — TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md) 的可读性→输出投影对齐→干预有效性前置选择边界，root实写且非书稿作者[写后核](../_sources/daily-20260420/V3_APR20_15557_CH31_WRITE_AFTER_INDEPENDENT.md)通过 |
| [(1D) Ordered Tokens Enable Efficient Test-Time Search — 2604.15453v1](https://arxiv.org/html/2604.15453v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | ordered prefix的部分重建可供verifier搜索，须与表示及搜索协议联合选择；2 + 2 + 3 = 7 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，partial-prefix sensor条件两段，root真实写后通过 |
| [StoSignSGD: Unbiased Structural Stochasticity Fixes SignSGD for Training Large Language Models — 2604.15416v1](https://arxiv.org/html/2604.15416v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 正包络随机sign保留预条件期望而非raw梯度无偏，具体知识缺口深入；2 + 1 + 2 = 5 | 深入完成 | 整合 — TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，sign geometry后真实两段，root写后通过 |
| [HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents? — 2604.15415v1](https://arxiv.org/html/2604.15415v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 公开有害skill不依赖隐藏payload，用户同意不能替代平台内容policy；2 + 2 + 3 = 7 | 深入完成 | 整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，SkillPoisoning的admission/effect交接真实两段，root写后通过 |
| [Taming Asynchronous CPU-GPU Coupling for Frequency-aware Latency Estimation on Mobile Edge — 2604.15357v1](https://arxiv.org/html/2604.15357v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 不同频率下launch/execute从间隙转重叠，需joint timeline；2 + 2 + 3 = 7 | 深入完成 | 整合 — PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)，双近邻曲线后联合时间耦合两段，root写后通过 |
| [LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents — 2604.15368v1](https://arxiv.org/html/2604.15368v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 包装改变检测、清理后仍提动作，检测和授权分账；2 + 2 + 3 = 7 | 深入完成 | 整合 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，行为控制权段后日志包装/清洗残余提议两段，root写后通过 |
| [A Systematic Study of Training-Free Methods for Trustworthy Large Language Models — 2604.15789v1](https://arxiv.org/html/2604.15789v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 默认recipe跨family与实际组合不能按单项收益加和，需保留utility/分攻击归因；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)“Security Gate必须覆盖Defense Interaction、审计通道与部署变换”的具体组合非单调命题，不以此替代整篇评价边界 |
| [LLM Reasoning Is Latent, Not the Chain of Thought — 2604.15726v1](https://arxiv.org/html/2604.15726v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 六arm区分surface/latent/budget解释，matched控制若成立会改变reasoning必要性判断；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅隔离未证明的matched-budget量化与latent causal headline；保留协议、三模型表，见§4–5 |
| [Evaluating LLM Simulators as Differentially Private Data Generators — 2604.15461v1](https://arxiv.org/html/2604.15461v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | DP统计经LLM simulator可被learned prior覆盖，privacy后处理不等distribution fidelity；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 有界synthetic-data模拟反例，输入/输出统计接口不全传递且training support未匹配，不支持唯一架构因果或新统一DP预算保证，无必要Books新增 |
| [The Spectral Geometry of Thought: Phase Transitions, Instruction Reversal, Token-Level Dynamics, and Perfect Correctness Prediction in How Transformers Reason — 2604.15350v1](https://arxiv.org/html/2604.15350v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | activation谱可作诊断，但perfect/答前/方向一致性会实质影响是否用作质量sensor；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅隔离perfect答前与普适方向保证，保留模型/阶段依赖geometry、ID/OOD表和明确反证 |
| [LinuxArena: A Control Setting for AI Agents in Live Production Software Environments — 2604.15384v1](https://arxiv.org/html/2604.15384v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 人工攻击强于已激发模型攻击，使monitor比较必须绑定攻击生成/选择与审计预算；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)“Control Evaluation要测试Attacker如何选择攻击时机”的generator/selector/attempt/audit预算及elicitation下界命题 |
| [Temporal Contrastive Decoding: A Training-Free Method for Large Audio-Language Models — 2604.15383v1](https://arxiv.org/html/2604.15383v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 保留粗音频语义的慢参考与decoder可见性改变反事实选择，具体知识缺口深入；2 + 1 + 3 = 6 | 深入完成 | 整合 — MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，已实际两段写入，root写后通过 |
| [Natural gradient descent with momentum — 2604.15554v1](https://arxiv.org/html/2604.15554v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 历史函数momentum须随tangent变化重新表示，不等参数momentum复用，具体知识缺口深入；2 + 1 + 2 = 5 | 深入完成 | 整合 — TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，已实际两段写入，root写后通过 |
| [Dispatch-Aware Ragged Attention for Pruned Vision Transformers — 2604.15408v1](https://arxiv.org/abs/2604.15408v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 短attention中wrapper/floor主导，kernel收益不等端到端收益；2 + 1 + 3 = 6 | 标准完成 | 已有覆盖 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)“从逐Kernel Launch到Persistent Executor”的launch-bound与TaxBreak/WebGPU残差分账具体命题 |
| [Think Multilingual, Not Harder: A Data-Efficient Framework for Teaching Reasoning Models to Code-Switch — 2604.15490v1](https://arxiv.org/html/2604.15490v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 空reasoning的MT SFT也改变reasoning trace语言行为，增多不等更好；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — matched token预算但非matched样本/无语言行为唯一因果，保留跨任务语言行为关联 |
| [Fleet: Hierarchical Task-based Abstraction for Megakernels on Multi-Die GPUs — 2604.15379v1](https://arxiv.org/html/2604.15379v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | partitioned-L2 chiplet上task placement与跨die完成可见性影响权重tile局部性；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，event/per-SM后实际两段，root写后通过 |
| [Ragged Paged Attention: A High-Performance and Flexible LLM Inference Kernel for TPU — 2604.15464v1](https://arxiv.org/html/2604.15464v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 固定capacity的预编译shape仍须按有效ragged分布、DMA与layout survival计划；2 + 2 + 2 = 6 | 深入完成 | 整合 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，SGLang-JAX后实际两段，root写后通过 |
| [EasyRider: Mitigating Power Transients in Datacenter-Scale Training Workloads — 2604.15522v1](https://arxiv.org/html/2604.15522v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 机架功率波形的快滤波/辅助储能与慢SoC纠偏不同于总能量预算；2 + 2 + 2 = 6 | 深入完成 | 整合 — PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)，Installed Power后实际两段，root写后通过 |
| [Qwen3.5-Omni Technical Report — 2604.15804v1](https://arxiv.org/html/2604.15804v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 单流text/speech累计token速率约束决定可提交prefix，不等于token type交错或两级部署；2 + 2 + 2 = 6 | 深入完成 | 整合 — MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，speech/reasoning交错后真实两段，root写后通过 |
| [Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit — 2604.15356v1](https://arxiv.org/html/2604.15356v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 顺序token分布可作KV压缩条件，但打印ultrametric及max d检索方向有反例；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅打印metric/近义prefix复用保证隔离，保有效精确前缀与有限实验，见§4–5 |
| [The Illusion of Equivalence: Systematic FP16 Divergence in KV-Cached Autoregressive Inference — 2604.15409v1](https://arxiv.org/html/2604.15409v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | cache路径与精度变化需联合数值合同，局部FP32干预不能推出唯一KV原因；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的precision/reduction/kernel/compiler/hardware数值合同，非整篇已有 |
| [SecureRouter: Encrypted Routing for Efficient Secure Inference — 2604.15499v1](https://arxiv.org/html/2604.15499v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 两方打印线性share缺交叉项，隔离完整协议与全confidentiality保证；2 + 2 + 2 = 6 | 争议 | 暂缓 — 只隔离所印线性步骤与据此推全执行保证，保cost-aware容量选择及有限表，见§4–5 |
| [Discover and Prove: An Open-source Agentic Framework for Hard Mode Automated Theorem Proving in Lean 4 — 2604.15839v1](https://arxiv.org/html/2604.15839v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 答案代入后证明不等原题求解，Lean通过不替代对象语义；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖 — PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) binary verdict与artifact preservation具体命题，非算法整体已有 |
| [Disentangling Mathematical Reasoning in LLMs: A Methodological Investigation of Internal Mechanisms — 2604.15842v1](https://arxiv.org/html/2604.15842v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | logit-lens未读出不等于无信息，位置attention交换仅局部路径敏感；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 不推唯一内部算法或普遍架构因果 |
| [CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization — 2604.15847v1](https://arxiv.org/html/2604.15847v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 固定正例/在线负例/warmup并非永久擦除或因果独立证明；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) channel/retain/collapse与dataset-influence对象区分窄命题 |
| [DPrivBench: Benchmarking LLMs' Reasoning for Differential Privacy — 2604.15851v1](https://arxiv.org/html/2604.15851v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 邻接集合、敏感度与argmin分责揭示局部DP推理失败；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — benchmark分数非部署DP保证 |
| [The World Leaks the Future: Harness Evolution for Future Prediction Agents — 2604.15719v1](https://arxiv.org/html/2604.15719v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 未决事件的跨时间notes可作临时反馈，resolution才是最终truth；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 表中样本N缺位，不能签matched cohort或普遍promotion因果 |
| [Reasoning-targeted Jailbreak Attacks on Large Reasoning Models via Semantic Triggers and Psychological Framing — 2604.15725v1](https://arxiv.org/html/2604.15725v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 可见reasoning危害与final answer等价是不同评估对象；2 + 1 + 3 = 6 | 深入完成 | 已有覆盖 — PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) CoT Monitor 的channel/parser/attempt具体命题，非攻击recipe全已有 |
| [Chain-of-Thought Degrades Visual Spatial Reasoning Capabilities of Multimodal LLMs — 2604.16060v1](https://arxiv.org/html/2604.16060v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 图像有无及新增正确选项的对照并非同题单因素，CoT有正反切片；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 不采CoT普遍有害或RL唯一原因 |
| [Mind’s Eye: A Benchmark of Visual Abstraction, Transformation and Composition for Multimodal LLMs — 2604.16054v1](https://arxiv.org/html/2604.16054v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 同题视觉抽象/变换的prompt臂响应方向不同，统一总分遮住能力切片；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — Ch66已有EvalSpec构念/提示变体分账，局部反证不需重复正文；人类distractor p值矛盾隔离 |
| [DPDSyn: Improving Differentially Private Dataset Synthesis for Model Training by Downstream Task Guidance — 2604.15660v1](https://arxiv.org/html/2604.15660v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 印刷算法公开原始属性逐列置换结果，DP分类器后处理不能给该独立通道继承隐私保证；3 + 2 + 3 = 8 | 争议 | 暂缓 — 仅隔离 Algorithm 2/§3.3 的完整 `(ε,δ)` 发布保证；Books No Change — Ch72已有具体覆盖，不作争议论文的正面机制来源 |
| [Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation — 2604.16198v1](https://arxiv.org/html/2604.16198v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 生成前需求QA与生成后代码→遮蔽需求反向检查分担不同误解位置；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 模型生成的参考答案不是用户spec真值，成本未配对；Ch79已有需求/测试/验收责任，无必要Books新增 |
| [CodeMMR: Bridging Natural Language, Code, and Image for Unified Retrieval — 2604.15663v1](https://arxiv.org/html/2604.15663v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 图像↔代码检索的模态方向、长结构与未见任务失配，要求按typed workload分层验收；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — Ch76已有typed operator和检索→生成分账；局部反证不证明统一索引普遍优越，无必要Books新增 |
| [Optimizing Stochastic Gradient Push under Broadcast Communications — 2604.15549v1](https://arxiv.org/html/2604.15549v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 无线去中心训练中有向SGP mixing与冲突时隙/收敛联合设计，不只是换optimizer；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — Ch36不把对称图当普遍前提；此条件分支不外推GPU fabric/LLM集群或端到端SLO |
| [AgentV-RL: Scaling Reward Modeling with Agentic Verifier — 2604.16004v1](https://arxiv.org/html/2604.16004v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 同模型前向/后向工具验证把中间错误与外部证据列为候选评估对象；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 受限消融与固定候选池成立，但非独立truth/授权或通用可靠性保证，Ch66/79的评价与提交责任不改 |
| [MemExplorer: Navigating the Heterogeneous Memory Design Space for Agentic Inference NPUs — 2604.16007v1](https://arxiv.org/html/2604.16007v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | phase-specific working set、层级traffic/mapping/cycle联合模拟缩搜索；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)仅承载既有设计期命题，Pareto点/新层级数字非实芯片或整机SLO，非全论文Existing |
| [Beyond Single-Model Optimization: Preserving Plasticity in Continual Reinforcement Learning — 2604.15414v1](https://arxiv.org/html/2604.15414v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | policy archive、短transfer probe与latent坐标维护形成有限重访分支；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 小环境结果不证明通用长期PPO/checkpoint控制合同 |
| [Robust Synchronisation for Federated Learning in The Face of Correlated Device Failure — 2604.16090v1](https://arxiv.org/html/2604.16090v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 共同故障×非IID标签支持使边际到场校正不能重建本轮缺失类梯度；2 + 1 + 2 = 5 | 深入完成 | 整合 — TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)窄正文已实写，[apr01非书稿作者真实写后](../_sources/daily-20260420/V3_APR01_AWPSP_CH36_WRITE_AFTER_INDEPENDENT.md)通过 |
| [The Metacognitive Monitoring Battery: A Cross-Domain Benchmark for LLM Self-Monitoring — 2604.15702v1](https://arxiv.org/html/2604.15702v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | KEEP/WITHDRAW/BET分开错误辨别与调节行为，阈值敏感不证明内部自监测实体；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 有限行为测量非模型内部能力认证或通用排名 |
| [GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows — 2604.15715v1](https://arxiv.org/html/2604.15715v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | tool call有效、最终artifact rubric与外部任务效果需分账；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 受限流程/成本案例不证明通用agent执行成功或judge无偏 |
| [Privacy-Preserving LLMs Routing — 2604.15728v1](https://arxiv.org/html/2604.15728v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | MPC友好encoder与constant-round选择有局部取舍，印刷top-k在并列值下返回零候选；2 + 2 + 2 = 6 | 争议 | 暂缓 — 仅隔离打印exact-top-k保证，保有限成本表，不推断实现已泄漏 |
| [Accuracy Is Speed: Towards Long-Context-Aware Routing for Distributed LLM Serving — 2604.15732v1](https://arxiv.org/html/2604.15732v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | TTCA把错误后重试纳入服务成本，但真实正确性oracle与router开销未完；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 长上下文UUIDKV局部路由不等生产可观测最优SLO |

| [VoxMind: An End-to-End Agentic Spoken Dialogue System — 2604.15710v1](https://arxiv.org/html/2604.15710v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 语音生成关键路径外的辅助检索先提案、显式调用后才入本地工具集；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 有限工具/录音条件不保证任意规模常数延迟或语音能力无退步 |
| [Into the Gray Zone: Domain Contexts Can Blur LLM Safety Boundaries — 2604.15717v1](https://arxiv.org/html/2604.15717v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 领域上下文改变受测目标拒答，攻击选择与judge提取也改变成功分母；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 有限协议反证不证明训练成因或所有防线失效 |
| [When Do Early-Exit Networks Generalize? A PAC-Bayesian Theory of Adaptive Depth — 2604.15764v1](https://arxiv.org/html/2604.15764v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 早退深度熵/泛化条件有实测，但印刷 KL 与 union 常数抵消推导不成立；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅隔离 H-only PAC 保证，保实验与限定条件 |
| [Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs — 2604.15780v1](https://arxiv.org/html/2604.15780v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 参数mask搜索给受限安全/效用分支，印刷beam目标与保留最高分方向冲突；2 + 2 + 2 = 6 | 争议 | 暂缓 — 仅隔离beam选择保证，保greedy与受限表 |
| [MEDLEY-BENCH: Scale Buys Evaluation but Not Control in AI Metacognition — 2604.16009v1](https://arxiv.org/html/2604.16009v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 独立/私下/社交条件揭示相对rubric与绝对能力不同，非内部自监测真值；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — pseudo-GT与未配训练不证明规模因果，未核旧修复线索不作事实 |
| [SoK: Security of Autonomous LLM Agents in Agentic Commerce — 2604.15367v1](https://arxiv.org/html/2604.15367v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 商务agent信任层分账有用，但ERC-8004被误写成付款限额协议；2 + 2 + 2 = 6 | 争议 | 暂缓 — 仅隔离依赖该规范能力的保护结论，保其它有据分类 |

| [DepCap: Adaptive Block-Wise Parallel Decoding for Efficient Diffusion LM Inference — 2604.15750v1](https://arxiv.org/html/2604.15750v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 跨步KL与熵选块边界有局部价值，印刷高置信种子可内部相冲突；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅隔离返回无冲突集合保证，保受限表 |
| [MemEvoBench: Benchmarking Safety Risks from Memory Misevolution in LLM Agents — 2604.15774v1](https://arxiv.org/html/2604.15774v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 模拟偏置反馈改变跨轮记忆污染，工具与反馈作用不能混成单因果；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)的episode/反馈authority具体命题 |
| [From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation — 2604.15805v1](https://arxiv.org/html/2604.15805v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | panorama→静态场景→digital cousin给有限real-to-sim分支；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 数据量和物理真实性未受控，不改Ch26闭环责任 |
| [UsefulBench: Towards Decision-Useful Information as a Target for Information Retrieval — 2604.15827v1](https://arxiv.org/html/2604.15827v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | relevance与decision usefulness分标签，但专业知识/启发分数限制真值；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — Ch76检索命中与答案支持分账不改 |
| [Beyond Text Prompts: Precise Concept Erasure through Text–Image Collaboration — 2604.15829v1](https://arxiv.org/html/2604.15829v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | text-image协同概念擦除与保留取舍，温度叙述和指标方向均有限制；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 不采语义凸性或零残余保证 |

| [CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution — 2604.15840v1](https://arxiv.org/html/2604.15840v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 当前能力边界的失败/混合/稀有信号驱动新任务分布，但验证与反馈污染必须分权；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖 — TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)能力边界→环境任务提案→独立准入 |
| [Hierarchical Codec Diffusion for Video-to-Speech Generation — 2604.15923v1](https://arxiv.org/html/2604.15923v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | RVQ层级按唇/身份与表情条件分责，但训练用真实音频标签；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 不采纯视觉全程或层级唯一因果 |
| [VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation — 2604.15938v1](https://arxiv.org/html/2604.15938v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 视觉阶段调整denoise/action horizon，印刷采样无偏与hard方向相冲突；2 + 2 + 2 = 6 | 争议 | 暂缓 — 仅隔离公式/方向保证，保有限实验 |
| [CIMple: Standard-cell SRAM-based CIM with LUT-based split softmax for attention acceleration — 2604.15944v1](https://arxiv.org/html/2604.15944v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | CIM双bank与LUT softmax映射揭示片上容量和非线性成本；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 合成/布局与整模型执行不同分母 |
| [From Competition to Coopetition: Coopetitive Training-Free Image Editing Based on Text Guidance — 2604.15948v1](https://arxiv.org/html/2604.15948v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 双分支attention调节/latent refinement有局部价值，零值与零范数公式未定义；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅隔离打印有限性及由此声称的背景保证 |
| [A Case Study on the Impact of Anonymization Along the RAG Pipeline — 2604.15958v1](https://arxiv.org/html/2604.15958v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | PRE/POST放置点改变隐私暴露对象和质量，预算不可横向合并；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 不采完整管道匿名或统一privacy最优 |
| [TwoHamsters: Benchmarking Multi-Concept Compositional Unsafety in Text-to-Image Models — 2604.15967v1](https://arxiv.org/html/2604.15967v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 原子安全不推出组合安全，受限对照与评价代理不证真实事故率；2 + 2 + 2 = 6 | 深入完成 | 仅报告 — 不采全部erasure失效或潜在独立机制 |
| [AEGIS: Anchor-Enforced Gradient Isolation for Knowledge-Preserving Vision-Language-Action Fine-Tuning — 2604.16067v1](https://arxiv.org/html/2604.16067v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | anchor梯度冲突投影有限有效，含ε公式不满足精确正交；2 + 1 + 3 = 6 | 争议 | 暂缓 — 仅隔离零破坏严格保证，保VQA局部表 |
| [JumpLoRA: Sparse Adapters for Continual Learning in Large Language Models — 2604.16171v1](https://arxiv.org/html/2604.16171v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | task-agnostic连续任务中可学习更新支持集，固定稀疏率与逐任务adapter外的受限分支；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — SC遗忘反退与预算未配，不能推出普遍参数隔离或生产收益 |
| [Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models — 2604.15609v1](https://arxiv.org/html/2604.15609v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 完整概率API下本地steering＋预测融合以一次远端调用做输入适配；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限视觉/VLM分类接口，非远端真梯度或生产SLO保证 |
| [Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow — 2604.15809v1](https://arxiv.org/html/2604.15809v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 额外解码后按跨层熵遮文本到视觉的读取边、保留视觉状态；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — white-box局部排序与额外成本不证普遍grounding/SLO |
| [Aletheia: Gradient-Guided Layer Selection for Efficient LoRA Fine-Tuning Across Architectures — 2604.15351v1](https://arxiv.org/html/2604.15351v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 梯度画像选择LoRA执行层提供受限计算/更新支持集分支；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 无同层数简单选层对照，不采梯度排序唯一收益或通用加速 |
| [Weak-to-Strong Knowledge Distillation Accelerates Visual Learning — 2604.15451v1](https://arxiv.org/html/2604.15451v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 适度弱teacher仅早期生效、两次validation超越后停止KD；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — first-at-target步骤非完整teacher成本或LLM净加速 |
| [Flexible Empowerment at Reasoning with Extended Best-of-N Sampling — 2604.15614v1](https://arxiv.org/html/2604.15614v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 固定候选数内entmax形状与目标状态缩放改变行动选择；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — off-policy控制任务，额外模型/选择成本不固定 |
| [Prototype-Grounded Concept Models for Verifiable Concept Alignment — 2604.16076v1](https://arxiv.org/html/2604.16076v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 分割part→可视原型→concept-only任务给受限可编辑表示接口；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — segmenter先见全图，原型不自动是人类语义/因果真值 |
| [Towards Robust Endogenous Reasoning: Unifying Drift Adaptation in Non-Stationary Tuning — 2604.15705v1](https://arxiv.org/html/2604.15705v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 文字反事实、视觉近邻负例与逆匹配过滤改变多模态偏好对支持集；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 未识别潜在D或严格正交，不采医疗/驾驶安全保证 |
| [Target-Oriented Pretraining Data Selection via Neuron-Activated Graph — 2604.15706v1](https://arxiv.org/html/2604.15706v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 跨层干预activation代理筛选目标预训练数据，特征提取另付成本；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — Top-K重叠非唯一骨架，MMLU分支反退 |
| [The Amazing Stability of Flow Matching — 2604.16079v1](https://arxiv.org/html/2604.16079v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 同seed输出近似不等内部vector field相同，删数FID反退限制无损剪枝代理；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 受限人脸域/共用VAE，不采跨数据稳健性 |
| [Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions — 2604.16135v1](https://arxiv.org/html/2604.16135v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 结构mask与晚期融合给复合动作生成的局部替代接口；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — benchmark重叠不明，非真实物理动作保证 |
| [C-Mining: Unsupervised Discovery of Seeds for Cultural Data Synthesis via Geometric Misalignment — 2604.15675v1](https://arxiv.org/html/2604.15675v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 跨语几何错位为低资源文化指令合成提供相对随机/单语seed筛选分支；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 不把embedding或cosine归一当文化真值，Ch27已有选择/来源/teacher责任 |
| [SAGE: Selective Attention-Guided Extraction for Token-Efficient Document Indexing — 2604.15583v1](https://arxiv.org/html/2604.15583v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 本地整文分块prefill与多query缓存换远端reader token预算，质量/成本不同向；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 缓存可摊条件与完整端到端分母不同，Ch76预算/证据责任未改 |
| [Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing — 2604.15771v1](https://arxiv.org/html/2604.15771v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 探针判重检索、失败后router选恢复动作，是有限条件化RAG控制分支；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — gold标签与未隔离技能消融不证事实正确或通用自修复，Ch76既有终止责任不变 |
| [AdaVFM: Adaptive Vision Foundation Models for Edge Intelligence via LLM-Guided Execution — 2604.15622v1](https://arxiv.org/html/2604.15622v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 低频cloud语义候选与高频edge子网执行分责，类别召回和资源质量必须联验；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 稀疏场景为模拟，lookup不保证未知scene，完整端云成本未测 |
| [Self-Distillation as a Performance Recovery Mechanism for LLMs: Counteracting Compression and Catastrophic Forgetting — 2604.15794v1](https://arxiv.org/html/2604.15794v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 受损checkpoint先off-policy teacher bootstrap、再on-policy自蒸馏的受限恢复次序；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — teacher与新增预算混杂，MMLU未净恢复，CKA非因果 |
| [UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs — 2604.15871v1](https://arxiv.org/html/2604.15871v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | source/target/instruction三元组统一两种编辑输入的比较身份，而非只增榜单；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — judge隔离未披露、部分评分反退，不采普遍公平 |
| [Learning Uncertainty from Sequential Internal Dispersion in Large Language Models — 2604.15741v1](https://arxiv.org/html/2604.15741v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | all-token/cross-layer有序sensor支持与组合反退改变受限不确定性传感器选型；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 标签监督/全状态成本与OOD反退，不采task-agnostic可靠性 |
| [KWBench: Measuring Unprompted Problem Recognition in Knowledge Work — 2604.15760v1](https://arxiv.org/html/2604.15760v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | unprompted framing作为mandatory、辅助执行另计，改变受限任务输入评价合同；2 + 2 + 2 = 6 | 标准完成 | 仅报告 — 无同题cue消融/人类基线，不采识别因果隔离或上线路由 |
| [Frequency-Aware Flow Matching for High-Quality Image Generation — 2604.15521v1](https://arxiv.org/html/2604.15521v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | low/high-frequency conditioning与spatial velocity分支的受限生成训练因子分解；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 组件消融不匹配总容量/算量，不采跨模态或速度保证 |
| [Rethinking the Necessity of Adaptive Retrieval-Augmented Generation through the Lens of Adaptive Listwise Ranking — 2604.15621v1](https://arxiv.org/html/2604.15621v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 可选空passage与强弱backbone对adaptive深度的质量排序反向，检索控制须按模型能力验收；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — oracle最佳k非在线策略，总selector成本不明 |
| [Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding Pipelines — 2604.15376v1](https://arxiv.org/html/2604.15376v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 两步缩放定位提供有条件的几何误差代理，改变可试验风险传感器选择；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 裁剪目标丢失或二次定位错误时不成立，跨模型路由提升不显著；Ch23/66责任未变 |
| [RAGognizer: Hallucination-Aware Fine-Tuning via Detection Head Integration — 2604.15945v1](https://arxiv.org/html/2604.15945v1) | 2026-04-20T08:00:00+08:00 ～ 2026-04-20T09:00:00+08:00 | 幻觉检测监督经LoRA反向更新表示，不同于冻结模型的事后探针；2 + 1 + 2 = 5 | 标准完成 | 仅报告 — 训练数据/标签与评价臂未严格隔离，不把检测概率当外部真值；Ch29/66责任未变 |

## 4. 证据与知识整合

### 负侧逆向准入后恢复的七项受限标准证据（非作者逆向核已完成）

### [AdaVFM: Adaptive Vision Foundation Models for Edge Intelligence via LLM-Guided Execution — 2604.15622v1](https://arxiv.org/html/2604.15622v1)

§3.2–3.3/Alg1、§6.2–6.4及D.3：共享 DINOv2→ConvNeXt 子网族在 edge 高频执行，cloud 低频生成/过滤 scene class set；selector 只在已有 scene 的 accuracy lookup 上以最大子网准确率的 α 比例选最便宜子网。因此类别召回/语义陈旧与设备质量—成本应同验，不能只看 edge FPS。作者先逐图生成 scene annotation 模拟稀疏更新，未知 scene、过期和传输成本无保证；D.3 过滤会漏真类，Ethos-U55数字不含完整端云。相对 Ch49/54 的一般部署档位，这是两个控制时钟耦合的受限选择，但证据不足以改 Books 或回拨后稿 learned selector。[旧同行核与作者复判](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

### [Self-Distillation as a Performance Recovery Mechanism for LLMs: Counteracting Compression and Catastrophic Forgetting — 2604.15794v1](https://arxiv.org/html/2604.15794v1)

§3.2/§5.1–5.4/§6/Table4：在量化或剪枝后，先从 teacher demonstrations 作 off-policy bootstrap，再以 student rollout 作 on-policy self-distillation；这与 Ch29 的普通 teacher/student 选择相比，是“先恢复再适配”的训练次序候选。受限 Qwen2.5 3/7B 对照中，剪枝后的 Tooluse 回升同时 MMLU 相对原 checkpoint 仍为 −2.55pp；专家 teacher 的任务迁移、额外训练预算和损伤程度未被隔离。CKA 与质量排序不同，不能从相关性声称恢复原流形的必要因果，也不能扩到科学 QA 或新增 Books 一般定律。[作者复判](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

### [UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs — 2604.15871v1](https://arxiv.org/html/2604.15871v1)

§3.2–3.4/§4/Tables3–4：633 image/77 video 的 source、target、instruction 三元组把 reconstruction-based 与 instruction-driven 编辑映到同一目标语义，五维 distilled MLLM judge 另作评分。相对 Ch66 的一般 scorer 身份合同，实际新增是跨编辑输入接口比较前必须核三元组语义等价，而非新 taxonomy 数量。4B/8B 从 Qwen3-VL-235B 蒸馏，8B stroke 误差仍有反退；50 人分组和“five full passes”文字互相不易合并，judge train/test 隔离未披露，不据此断言泄漏或评分正交独立，也不称所有范式已公平比较。[作者复判](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

### [Learning Uncertainty from Sequential Internal Dispersion in Large Language Models — 2604.15741v1](https://arxiv.org/html/2604.15741v1)

§2.3/§3.2/Tables2–3：每 token 的跨层 regularized covariance logdet、circular variance 与 token entropy 形成有序特征，再由监督 head 判不确定性；它比末 token 或固定层 support 多读状态，也多付读取/训练成本。MATH 与 SciQ 组合 sensor 反退，OOD InternalVariance AUC60.56 反高于 Full58.67，说明“加入更多层/token 特征”不是单调策略。Ch66 的 calibration/真值分账仍成立；本项只保留任务/OOD 切片下 sensor 支持选择，不把 proxy 分数称 correctness、模型无关结论或 tail-cost 证明。[作者复判](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

### [KWBench: Measuring Unprompted Problem Recognition in Knowledge Work — 2604.15760v1](https://arxiv.org/html/2604.15760v1)

§3–4/§7.5–8/§10：223 个 incident/改写任务不给明确问题框架，五个 mandatory criterion 任一失败使总体 gate 为零，辅助任务执行得分另计；这是 task-specification 输入身份的具体评价切片，不把一般“Agent 触发与执行分开”的 Ch66 命题误称为该数据集已有。强制项 gate-out 且辅助项可过仅是关联 profile；作者明确无同题 explicit-cue/recognition ablation、human baseline，且使用 single judge，不能证明未识别是唯一瓶颈、职业任务发生率或 oracle ensemble 生产效果。[作者复判](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

### [Frequency-Aware Flow Matching for High-Quality Image Generation — 2604.15521v1](https://arxiv.org/html/2604.15521v1)

§3–4/Tables6–8：Gaussian high/low filtering 回到 spatial components，与 spatial velocity branch 经 time-dependent 融合共同训练。Table6 400-epoch B 对照 no-frequency FID3.86、low3.55、high3.12、both2.95；Table7 addition2.95 对 cross-attention3.95/concat3.46，Table8 branch loss off4.67/on2.95。旧“频率条件完全未分离”前闭理由不成立；相对 Ch24 统一 velocity 和另一种长视频 attention 奇异谱，这只是图像 flow 训练因子分解的受限选择。分支/容量/训练算量未全面匹配，主文缺完整硬件/延迟，摘要与 Table3 的 FID 改善值不一致；不采唯一归因、跨模态或生产速度。[作者复判](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

### [Rethinking the Necessity of Adaptive Retrieval-Augmented Generation through the Lens of Adaptive Listwise Ranking — 2604.15621v1](https://arxiv.org/html/2604.15621v1)

§III-B/IV/V/TableII：listwise selector 产生有序 passage 子集，允许 `[0]` 丢全部 passage，而不只是固定 top-k 重新排序。弱 backbone 固定大 k 的噪声更重，强 Qwen3 Thinking 的 Vanilla-10 Overall34.18/EM54.85 却高于 Ada32.75/51，说明 Ch76 的 adaptive-depth 质量收益不能跨能力档直接搬用；强模型若改论 context 节约，还须计算 selector+generation 全成本。每题 oracle 最佳 k 依赖标签且不是在线输入，现有实验未给 production 端到端延迟或普遍优势，不因候选恢复追加 Books。[作者复判](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)。

### [Optimizing Stochastic Gradient Push under Broadcast Communications — 2604.15549v1](https://arxiv.org/html/2604.15549v1)

exact-v1 §1.2、§2.2–2.5、§4.4、§6.1–6.2：D-PSGD 对称双随机 mixing 限制为双向图，SGP 允许非对称有向图；论文在强连通、同步和有界梯度条件下，以最大入/出度与直径构造图成本上界，联合权衡每轮冲突时隙与达到收敛所需轮数。33节点 random geometric/Roofnet 图、CIFAR-10 的1.5M参数 ResNet-50，80%测试准确率连续五epoch停止；Table1在其代理成本下对 BASS optimized 为179712/228528及170688/192528 slots，Vanilla SGP反比D-PSGD差，不能把改进归因于单纯换算法。半双工无线时隙不含实际 GPU fabric、完整计算/状态、失败重传或生产wall-clock，模型小不构成排除理由也不支持任意大模型外推。实际 Ch36 已把去中心化 mixing 与通信拓扑、训练状态分账，未宣称必须对称；新有向图受限条件值得标准报告，但不需改其长期正文。原前闭的“无大模型/状态”已由 root 有界独立准入/处置核撤销，作者必要方法与反证见[定点记录](../_sources/daily-20260420/V3_15549_SCOPE_REOPEN_AUTHOR.md)，具名 first-public 联合链见[日期核](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)；不预支整日Gate。

### [AgentV-RL: Scaling Reward Modeling with Agentic Verifier — 2604.16004v1](https://arxiv.org/html/2604.16004v1)

exact-v1 §3.1–3.3、§4.1–4.3.4/Tables1–5、必要AppC.3–C.5：forward agent沿前提→结论作工具检查，backward agent由结论反查前提，两路信心平均用于BoN，revision要求两路同判correct；训练从可验证解生成轨迹、先SFT再GRPO。固定候选池/相同初始solution与有限消融支持该局部验证策略，不等独立证据源或最终 truth；两路可由同一模型运行，工具 effect 的授权也未由判分建立。Table5 单A100/batch128下 base 2560 tokens/119s、双向8349 tokens/11.3 rounds/1.6 tools/323.4s，收益伴约3.3倍token/2.7倍时间；无生产tail与跨任务认证。实际 Ch66已有 proposal、外证、评估错误与成本分账，Ch79保独立提交验收；本次有限策略仅报告，不改长期owner。root已在独立消息中确认 exact-v1 必要方法/评价及受限处置；作者完整定位在[恢复记录](../_sources/daily-20260420/v3-reopen-notes.md)，未复现实验；具名日期见[联合链](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)，非整日Gate。

### [MemExplorer: Navigating the Heterogeneous Memory Design Space for Agentic Inference NPUs — 2604.16007v1](https://arxiv.org/html/2604.16007v1)

exact-v1 §2/§4/§5.1–5.6/Tables3–9：PLENA的解析/时序近似联合枚举SRAM/3D-stack与HBM/HBF/LPDDR容量、带宽、算子traffic、mapping、PE阵列和prefill/decode目标，GP-EHVI搜索预测Pareto点；不是制造并测量芯片。Table9仅 Llama3.3-70B 单层prefill/seq4096 对 emulator 814.14ms、作者模型731.11ms，约10.20%误差，不能推广整机吞吐或质量；P/D 表的batch与7百瓦预算不同，不能横比成同条件SLO。实际 Ch54:493–503 已明确 phase-specific working-set knee、operator trace、层级流量/mapping/cycle与技术模型联合设计，模拟缩搜索、实机profile验收；此**窄设计期命题**已有覆盖，不声称论文新器件枚举、Pareto数字或全算法均已写入。root 独立核 exact-v1 必要方法/评价与该实际段落后通过窄Existing，作者细节见[审阅记录](../_sources/daily-20260420/v3-reopen-notes.md)；[联合日期链](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)具名核，不是日级Gate。

### [Faster LLM Inference via Sequential Monte Carlo — 2604.15672v1](https://arxiv.org/html/2604.15672v1)

exact-v1 §3 Algorithm 1/§3.1–3.3/§4：多个 draft 粒子生成区块，由 target 批量计算 importance weight，在有效样本数不足时重采祖先，终点仅选一条输出；这不是 classic exact acceptance 的逐 token 可提交前缀。Theorem 3.1 在 iid proposal、`p≪q` 与四阶权重矩下只给单轮重采误差，不能推出多轮祖先相关的整轨迹有限保证或有限粒子 exactness。roofline 的空闲计算利用受 `BN(K+1)≤R` 限制；Paged/Radix 的祖先指针减少 KV tensor 复制，仍付元数据与重采成本。单 H100/Llama/Qwen 实验的 3pp 相对 SD、10pp 相对 SD、15% 相对 target 为不同质量容差，Qwen draft 不 matched，SSD 对照还多一张 GPU，不能当同预算/同质量生产 SLO。实际 Ch48 在 Cactus 局部条件 law 与经典分支汇合之间原缺粒子私有状态→最终混合 law 的独立交接，现已真实写入两段及 Review；[root 写前核](../_sources/daily-20260420/V3_SMC_OWNER_PROPOSAL.md)和 Ch48 真实写后非作者核均通过，不改经典 exact 路径，未复现实验。具名 first-public 联合链见[日期核](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)，不预支整日 Gate。

### [Chain-of-Thought Degrades Visual Spatial Reasoning Capabilities of Multimodal LLMs — 2604.16060v1](https://arxiv.org/html/2604.16060v1)

exact-v1 §3–4/Limitations：NoImage++同时加入新正确选项，不是只撤视觉cue的单因素干预；native/custom prompt、训练史及tool循环亦混杂。VisionG1、Qwen及GPT的若干正向切片反驳“CoT一概退步”。图像证据与文字推理路径的失配可保为受限评价问题，不能指认RL导致普遍视觉能力下降，也无需据此改Ch24/66一般控制关系。[root有限独立核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)通过。

### [The World Leaks the Future: Harness Evolution for Future Prediction Agents — 2604.15719v1](https://arxiv.org/html/2604.15719v1)

exact-v1 §3.1–3.3/4.1–4.4/Tables1–3/5：同一未决问题的多次checkpoint差异可给provisional harness修改，问题内事实仍保notes，只有resolution后才修正并跨题carry；时间变化不是truth。GPT-5.4 forward-only/256k/100 tool ceilings表面相同，search stack和realized compute未匹配；MiroFlow L4 46.80还高于Milkyway45.85。§4.4/Table3 cohort N与choice/numeric仍 `[fill in]`，NoHarness同时禁notes读写，不能单独归因temporal feedback。Ch76/77的state与证据权限已有一般分责，特定跨时间harness仅报告，不写普遍promotion机制。[root有限独立核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)通过；正式题按v1，不用后发v3改题。

### [Reasoning-targeted Jailbreak Attacks on Large Reasoning Models via Semantic Triggers and Psychological Framing — 2604.15725v1](https://arxiv.org/html/2604.15725v1)

exact-v1 §3/5.1.5/5.3/6：final answer等价与visible reasoning harmfulness是不同judge对象，前者未变不证明可见surface无害。GPT-4o与三次取优的协议不提供单次真实危害概率或完整内部计算可见性；§6防御是建议，未证消除。Ch72 CoT Monitor已具体分channel/parser、attempt机会与外部effect、sensor与授权，足以承载此处有限保护命题，不代表PRJA配方整篇已有。保留可见面风险与受限实验，不采攻击普遍成功或防御保证。[root实际Ch72独立核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)通过。

### [Discover and Prove: An Open-source Agentic Framework for Hard Mode Automated Theorem Proving in Lean 4 — 2604.15839v1](https://arxiv.org/html/2604.15839v1)

exact-v1 §3.1–3.2/4.3/Table2/AppH：把候选答案替入目标后证明其命题，与从原题独立求解及答案与问题对应性不是同一对象；rfl闭合一些例子不说明Lean不sound。No-agent在Combi/miniF2F反而较好，不采自检恒优。Ch66现有“Binary Verdict通过不等于语义忠实”与“Compound Artifact需要Preservation Contract”已负担编码对象/验证器分权这条窄命题；Hard/Easy recipe及有限实验只是报告，不将整套Agent签已有。[apr02实际owner独立核](../_sources/daily-20260420/V3_APR02_FIVE_15839_15859_INDEPENDENT.md)通过。

### [Disentangling Mathematical Reasoning in LLMs: A Methodological Investigation of Internal Mechanisms — 2604.15842v1](https://arxiv.org/html/2604.15842v1)

exact-v1 §5–6/Figs8–9：logit-lens不读出算术信息，不证明信息不存在；最后输入位置的attention交换支持该设置下路径敏感，不唯一确定模型内部算法。有限算术干预仍有局部诊断价值，不能因小模型关掉；Ch5对readout与干预的分责已有，这次未提供新长期机制分支，标准仅报告。[apr02必要源独立核](../_sources/daily-20260420/V3_APR02_FIVE_15839_15859_INDEPENDENT.md)通过，未复现。

### [CiPO: Counterfactual Unlearning for Large Reasoning Models through Iterative Preference Optimization — 2604.15847v1](https://arxiv.org/html/2604.15847v1)

exact-v1 §4.2/Eqs5–6、§5.1–5.3/Tables1–3：固定正例、在线负例及warmup是实际训练路径，但偏好margin不识别因果独立，也不证明参数永久擦除；选择后RETURN与合成轨迹仍是受限指标。Ch72当前channel/retain/collapse及dataset-influence与概念行为对象分开的命题，已承载本次只采用的条件边界，非CiPO全算法已有或普遍unlearning保证。[apr02实际Ch72独立核](../_sources/daily-20260420/V3_APR02_FIVE_15839_15859_INDEPENDENT.md)通过，不再写安全章。

### [DPrivBench: Benchmarking LLMs' Reasoning for Differential Privacy — 2604.15851v1](https://arxiv.org/html/2604.15851v1)

exact-v1 §3.1–3.2/Tables1、§4–6.3：相邻不交不能替代两两不交，函数值与argmin敏感度也不同，给出受限DP条件推理失败样例。125标签、模型SE与18难题RAG不能成为真实部署DP证明；Gemini在对照中换checkpoint，非完全matched。必要条件未写不必然是每个机制的逐例反证。Ch72的发布/威胁身份不由此benchmark改变，仅报告评价失效条件，不推通用安全率。[apr02独立核](../_sources/daily-20260420/V3_APR02_FIVE_15839_15859_INDEPENDENT.md)通过。

### [Sequential KV Cache Compression via Probabilistic Language Tries: Beyond the Per-Vector Shannon Limit — 2604.15356v1](https://arxiv.org/html/2604.15356v1)

exact-v1 §2.3/3.1–3.4/4.2/5.1–5.2/6.3/7.1–7.3/9.6：顺序语言trie可利用token条件分布组织压缩及精确共同祖先查找，但打印 `d(s,s′)=−log₂P(LCP)` 称ultrametric不成立：合法二符号各.5，`s=a,s′=b,s″=a` 时 `d(a,a)=1` 而 `d(a,b)=d(b,a)=0`，三角式要求1≤0。§7.3的max d与max P等价亦反方向。只隔离这两个打印metric/近义prefix KV复用保证，不否定固定输入/权重确定性、附条件熵论证、exact ancestor或所有压缩测量；重开需原版正确metric、检索方向和相关近似证明。Ch45基本KV职责不替代该证明，故暂缓中央新保证、不写Books。[apr02独立窄核](../_sources/daily-20260420/V3_APR02_SUBSEQUENT_THREE_15356_15499_INDEPENDENT.md)通过；未复现实验。

### [The Illusion of Equivalence: Systematic FP16 Divergence in KV-Cached Autoregressive Inference — 2604.15409v1](https://arxiv.org/html/2604.15409v1)

exact-v1 §6.3/7.3/7.5–7.6：同prompt cache开关可能产生输出漂移，600样本×32步的FP32干预消除该切片flip，但精度同时改变执行路径，不能断言KV state或FP16非结合性是唯一因。Residual patch不恢复的实验，作者也明确不排除其他机制；直接KV tensor patch仍是future。低任务acc有truncation/few-shot条件，模型间训练与权重不matched。Ch49当前实际数值合同已绑定precision、reduction topology、kernel/activation、compiler/runtime、hardware与重验，恰好承载此有限执行路径选择，而非全部架构因果。[apr02必要源→实际owner核](../_sources/daily-20260420/V3_APR02_SUBSEQUENT_THREE_15356_15499_INDEPENDENT.md)通过，无新增正文或生产100%保证。

### [SecureRouter: Encrypted Routing for Efficient Secure Inference — 2604.15499v1](https://arxiv.org/html/2604.15499v1)

exact-v1 §3.3–3.4：两方若把各自 `e₀W₀+R₀`、`e₁W₁+R₁` 当完整在线linear步骤，取 `e₀=1,e₁=0,W₀=0,W₁=1,R=0`，相加0而真实`(e₀+e₁)(W₀+W₁)=1`，缺交叉项。这个有限反例只隔离打印完整协议及由其推出的全confidentiality保证，不断言CrypTen实现确实没有secure multiplication，更不能断言已泄漏。Semihonest/noncolluding两方、加权容量routing及GLUE有限表仍保留；Table1/2不同对照不可合并，§4.3 cost按选择分布投影不是全测试集端到端重跑。重开需同版secure multiplication/选择协议或可核实现与trace威胁条件，不要求全部GLUE复现；不把秘密index自动写成全执行轨迹保密。[apr02独立窄核](../_sources/daily-20260420/V3_APR02_SUBSEQUENT_THREE_15356_15499_INDEPENDENT.md)通过，暂缓中央保证、不写Books。

### [Qwen3.5-Omni Technical Report — 2604.15804v1](https://arxiv.org/html/2604.15804v1)

exact-v1 §2.4–2.5/Tables1–2：ARIA把text/speech token放入单流，prefix累计speech:text比受item全局比约束，支持文本先形成前缀、语音随进；并不证明字词与声学帧逐点对齐。当前Ch24原有speech/reasoning token交错及后文Thinker→performer部署交接均未承担编码率与prefix提交条件，故该有限机制已在前者之后实际两段整合。代价是codec/type delimiter、缓存、取消和回退同属一个输出提交合同，未知终点下如何取得全局比仍未披露；固定chunk/双track继续是回退。Table2只是内部vLLM/compile/CUDA Graph设置的theoretical first-packet latency，Flash音频/视频1并发235/426ms到8并发352/1625ms、Plus435/651到955/1980ms，不含ARIA单独消融或产线tail SLO。输入video temporal-ID及AuT训练规模属别的表示/训练分支，未归因ARIA。[root写前有限核](../_sources/daily-20260420/V3_ROOT_ARIA_INDEPENDENT.md)与[真实写后](../_sources/V3_ROOT_FIVE_WRITE_AFTER_20260928.md)分别通过，不以此代替整日Gate，未复现实验。

### [Fleet: Hierarchical Task-based Abstraction for Megakernels on Multi-Die GPUs — 2604.15379v1](https://arxiv.org/html/2604.15379v1)

exact-v1 §3.1/4.1/5.1–5.3/6.1–6.4/Tables4–5/8：单MI350X的partitioned L2下，chiplet-aware task scope让同die共享weight tile，局部计数与last-worker跨die可见性决定何时完成；这是调度/同步边界，不是所有persistent kernel的加速源。Qwen3-8B BF16、64输入/1024输出、batch1–64 decode-only下，8个常驻scheduler占256CU的3.1%；低batch无额外tile复用，M-split在batch64的HBM read反升至1.20。关键负对照为batch64 M-tile18.61ms慢于成熟vLLM约11–12ms，作者尚未加K-split/attention优化；相对Mirage改善不能外推成熟Serving/端到端收益。Ch49在event与TaxBreak之间已实际两段吸收placement/完成职责及fallback，[root有限源核与写后](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)通过，未复现实验。

### [Ragged Paged Attention: A High-Performance and Flexible LLM Inference Kernel for TPU — 2604.15464v1](https://arxiv.org/html/2604.15464v1)

exact-v1 §3.1–3.7/Algorithm1、§4.1–4.4：固定token/sequence capacity可预编译但不决定有效ragged分布；K/V packing、动态DMA与attention流水可以减轻静态tile浪费，却不保证compiler HLO layout沿途不变，离线weight重排还须核实际边界。TPU7x/Llama3-8B/BF16下仅较长context或prefill饱和获得较高利用率，prefill preprocessing约2%～8%；d128 MFU还按50%最大MXU调整分母，不是全芯片/全请求收益。mixed优化未全支持、质量/CI/生产SLO未证，2025 artifact不是本日报论文首次公开。Ch49在SGLang-JAX与compiler-first之间已实际两段写入，[root必要源→owner及写后核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)通过；保留padded/general kernel及重编译回退。

### [EasyRider: Mitigating Power Transients in Datacenter-Scale Training Workloads — 2604.15522v1](https://arxiv.org/html/2604.15522v1)

exact-v1 §3–4/5.3–5.4/6/7.1–7.4/8与B.2：设施的ramp-rate/频谱可先于平均功率触限；被动滤波、双向辅助储能与慢SoC controller按不同时间尺度减小波形，储能容量仍由功率差积分决定，总energy不免费。400VDC/25A/10kW原型、两TitanX/125M训练trace、normalized示范不能证明MW级电网合规或battery寿命；低电压受25A限，inner-loop恢复不证明outer aging。§8 $66k/$3.7M≈1.78%与原文<1.25%冲突，未采该比率或B.2全局QP保证。Ch70在Installed Power与水耗之间实际两段吸收波形/energy/训练控制分账，[root必要源→owner及写后核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)通过，保留power cap/保守容量回退。

### [Neurosymbolic Repo-level Code Localization — 2604.16021v1](https://arxiv.org/html/2604.16021v1)

实际v1 §3.1–3.4.3、§4/Tables2–4与§5：AST-derived facts和Datalog query proposal分权，parser通过不证明语义正确；空关系的string relaxation/drop-one只作诊断，不把mutation结果当原问题答案。stable-empty包含执行失败，不能证明不存在；fragile-empty也不证明用户原条件错误。225人工确保非空的synthetic queries/9Pythonrepos与单repo负例不证明开放代码库完备性，SWE274省略keyword不是同题随机干预或泄漏排除。Table4 Qwen VAL→Full 104→136秒且ExecSucc同84.12，Claude比例分母不统一，不采普遍低延迟或生产SLO。

当前Ch76 procedural index后真实两段补足“空结果diagnostic不得静默改写查询authority”的窄缺口，保留facts更新/查询合成/探针成本与词法、chunk、原文核对回退。root必要源→actual owner与正文及前后相邻顺读的非作者写后均通过，见[有限采用与写后](../_sources/daily-20260420/V3_LOGICLOC_OWNER_PROPOSAL.md)。未复现实验，不代表整日Gate。

### [One-Shot Generative Flows: Existence and Obstructions — 2604.15439v1](https://arxiv.org/html/2604.15439v1)

v1 Def1–4/P1–C4/T5、Gaussian T6/P8/T9、P10/C12及T17必要条件实际深入。独立端点affine随机sample路径直，不使conditional ODE直；确定性coupling必要条件与PSD Jacobian充分方向不混。Gaussian特调sqrt(2t(1−t))辅助噪声可构造直流；两段分离uniform混合在独立端点/连续过程/uniform Lipschitz条件下no-go，不能扩任意多峰/高维/fullsupport。P10崩塌失败正则，T17仅固定d1/Frostman/尾模数类边界，不采泛化headline；理论无生产质量/NFE实测。

当前Ch24有learned approximate flow map组合/solver近似，缺sample/ODE与精确结构可行性区别。真实两段已写在并行/少步标题后，承接旧组合近似，保原solver与经验质量—NFE回退。root必要原文→actual owner及真实相邻写后通过，见[两项采用/写后](../_sources/daily-20260420/V3_FLOW_CTMC_OWNER_PROPOSALS.md)。

### [Neural Continuous-Time Markov Chain: Discrete Diffusion via Decoupled Jump Timing and Direction — 2604.15694v1](https://arxiv.org/html/2604.15694v1)

v1 §4.1/P4.8/absorbing特例、§4.2/AppD Algorithm2–3与§5实际深入。off-diagonal rate=exitλ×destination r，pathKL分Poisson timing与真实exit-rate加权Cat direction；conditional surrogate/marginal梯度同一需forward参数独立、正可微rate及微分积分交换，不保证全局或有限训练稳定。只有absorbing特例rate由schedule固定才还原masked CE；uniform可重复跳。EulerλΔt≤1合法性、τleap每新state重算r意味着step非NFE，真实head/调参成本保留。

163M/12layer/768/12head、GPT2BPE/seq512、1024sample Gemma2 genPPL非NLL/数学upperbound。TinyStories matched而OWT262B vsSEDD682B/pipeline不同；128step SEDD127.2优于Euler183.6、主τ列与AppD仅Euler披露冲突保留，不采排名唯一因果。hardware/precision/batch/SLO与CI未披露。Ch24 jointidentity及旧Euler边界缺timing/direction目标与mask特例，真实两段嵌joint artifact之后/SNR监督之前；root必要原文→actual owner及实际相邻写后通过，非复现/日Gate。

### [Symbolic Guardrails for Domain-Specific Agents: Stronger Safety and Security Guarantees Without Sacrificing Utility — 2604.15579v1](https://arxiv.org/html/2604.15579v1)

v1 §3–5/Tables2/4–7实际必要审阅；保护保证边界触发6分深入。六类symbolic checks依赖明确实现/语义改写，93/126可实现样本不是全部Agent政策。MedAgentBench34要求只实写23，增参工具的baseline replay不是完全matched schema。0违反只针对同一已实现predicate，非未知政策安全证明；utility非显著差异不证明无损。GPT4o/GPT5三有限benchmark、latency/precision/SLO未披露，不外推生产。

实际Ch72 Policy-as-Data的model sensor→deterministic executor、owner/version/fallback与Containment的effect/utility/efficiency联合验收承载窄责任边界，已有覆盖，不声称整篇benchmark/六类配方全覆盖。apr02[五项有限非作者核](../_sources/daily-20260420/V3_APR02_FIVE_BOUNDED_DISPOSITIONS.md)实际原文及owner通过，无新Books diff。

### [Majority Voting for Code Generation — 2604.15618v1](https://arxiv.org/html/2604.15618v1)

v1 §3–5/Table1–2及必要A实际标准审阅。execution-signature medoid保证选择真实candidate，逐input mode未必对应单个程序；共识不拥有correctness oracle。LCBv6用了真实test inputs，不把自造测试推断当实验。Qwen3系列64sample、half train/holdout；bootstrapSE非多seed证明。Mean@64改善与best@64未越base ceiling、再次FMV下降并存，不采递归无条件自改进。训练/生成和N×K执行预算不同，hardware/precision/SLO未披露；只报告新selector与局部负面边界，apr02有限核通过。

### [Too Private to Tell: Practical Token Theft Attacks on Apple Intelligence — 2604.15637v1](https://arxiv.org/html/2604.15637v1)

v1 §3/4.1/5.1/5.2/6/Ethics实读，匿名TGT首次硬件资格、OTT一次性与发行签名不能独立证明当前holder仍在合格设备。根凭据可再兑换，quota沿受害资产；仅作者macOS26.0/M4旧设备并需用户允许keychain访问，磁盘加密与授权API明文返回不同，不称无权限普遍当前漏洞。Apple26.2 Networking/CVE-2025-43509公告Released2025-12-12确认data-protection改善，不是本窗新fix或所有协议/残余漏洞证明。root source→实际owner与写后均通过：Ch72三层Security末至HardwareAttestation交接两段区别匿名性/不可转移性及一次child/rootcredential，保移设备与撤销成本，Review同步真实PASS。[有限采用/写后](../_sources/daily-20260420/V3_ANONYMOUS_TOKEN_OWNER_PROPOSAL.md)。

### [LLMs Corrupt Your Documents When You Delegate — 2604.15597v1](https://arxiv.org/html/2604.15597v1)

实际§2–5/8及必要A.1/A.2、B.2/B.3、M.1/M.2：52×6/real2–5kseed+8–12kdistractors/可逆edit/20interaction，各步fresh单session无conversationhistory。customparser weighted round-trip score为复合保留性，高分不排no-op/partial/errorcancellation、低分不定位错误步；errorfaithfulness依近似injectivity/无抵消，不是所有LLM定理。GPT5.4judge12409分层step的93.8%为fully或partially attempted（16.7%partial），不是正确完成；19model三代表94.3→71.5/94.2→73.1/96.8→80.9不是生产token丢失25%。basic5tool/4GPT/25turn/500ktokens受限，GPT5.4工具latency×.4/input×2.1反向保留，不采所有tools无助。root源→actualowner与真实写后通过，Ch66 full-cycle后两段补artifact preservation而非任务完成权。[独立核及写后](../_sources/daily-20260420/V3_DELEGATE_GROUPDPO_OWNER_PROPOSALS.md)。

### [GroupDPO: Memory efficient Group-wise Direct Preference Optimization — 2604.15602v1](https://arxiv.org/html/2604.15602v1)

实际§3–5.3/Limitations、必要A.3/Table6–7：no-grad同θ全部response scores算loss偏导，stopgradient固定系数逐sample backward保同参数点一阶，不保loss值/Hessian；同response/ref/reduction/forward随机性需一致，后者工程推论非全runtime复现。AllPairs balancedPN仍二次，额外no-grad pass不省略。单H10080SXM/checkpoint memory overhead=maxFWD/BWDallocated−warmparams/optimizerbase，排optimizer.step临时峰，而step latency包含optimizer；3memorywarm、2warm+5latency，precision/CI未披露不补。offline8/8/32GPU1ep1139与online8T16R异步100step、β/NLL/validationcheckpoint选择分开；gemma generalDPO37.8≥multiplegroup36.x和coding反向保留，group>8趋平非普适quality提升。root必要源→actualowner及实际写后通过，Ch34工程流两段新增梯度系数/执行分离，不改GRPO reward定义。[独立核及写后](../_sources/daily-20260420/V3_DELEGATE_GROUPDPO_OWNER_PROPOSALS.md)。

### [Preregistered Belief Revision Contracts — 2604.15558v1](https://arxiv.org/html/2604.15558v1)

实际§3–4、§6.1–6.3必要定义/证明、§13.9/14：固定有限假设和外部概率向量，准入witness不蕴含Agent执行operator。无新证据时`(1−λ)b+λu`在0<λ<1保argmax、不增加最大信心，不能纠正初始错误或证明LLM内部信念。三种enforcement分清gate、proof、state-holding router。paired n3000 GPT4o/T.7中411 harmful/273 beneficial/154 neutral flips全被挡，.724回到Raw并非普遍truth改善；保留语义认证/遗漏/动态假设与活性限制。root必要源→actualowner核及真实写后通过，Ch82共识与同根报告之间实际两段补分责，不采用全部拓扑定理。[采用依据](../_sources/daily-20260420/V3_PBRC_FACT_OWNER_PROPOSALS.md)。

### [Why Fine-Tuning Encourages Hallucinations and How to Fix It — 2604.15574v1](https://arxiv.org/html/2604.15574v1)

实际§2–5.2：SLiCK20次接口采样Unknown非内部知识不存在；relations≥30%Known筛选，Known/Unknown各8k，同relation retain范围固定。Qwen2.5-1.5B attention-only Unknown.010/HeldKnown.931，对FFN.941/.782，提示保持与acquisition不可合一。Known-only一epoch格式teacher、τ.5/λ1 tokenKL加额外forward；3%vs15%为relative peak held损伤非普遍hallucination率。P17真实name/UUID连tokenization与预训练关联也变，L2与KL信息不同、layer14/28 cosine是相关，均非唯一原因/模块事实存储证明。root source→actualowner与写后通过，Ch29通用forgetting缓解后两段新增表达既知/获取新事实目标分叉及reference代价。[采用依据](../_sources/daily-20260420/V3_PBRC_FACT_OWNER_PROPOSALS.md)。

### [Subliminal Transfer of Unsafe Behaviors in AI Agent Distillation — 2604.15559v1](https://arxiv.org/html/2604.15559v1)

实际§3.1–3.5/4.1–4.3、必要AppendixA：teacher150删除偏好两ep，400 safe-tools轨迹过滤约15%后340，student4ep，三3B/8B/7B家族LoRA/bf16。20模糊任务/3seed的first substantive action不是filesystem effect或普遍危害概率。Table2 random control25/base5不满足作者§3.4 control≈baseline判据；未报CI，不能采纯结构/唯一teacher bias因果。API/Bash baseline与chmod-first不同口径保留，不称一切删除/权限修改有害。6分真实filter→posttraining保护边界深入，apr02实际必要原文与当前Ch72“公开任务无关输出也可能携带后训练行为影子”对读通过；已有覆盖仅一般审计责任，新受限数字仍保留报告。[独立核](../_sources/daily-20260420/V3_APR02_SUBLIMINAL_RCFG_DISPOSITIONS.md)。

### [Reward Weighted Classifier-Free Guidance as Policy Improvement in Autoregressive Models — 2604.15577v1](https://arxiv.org/html/2604.15577v1)

实际§3–6：精确Q为prefix下条件reward期望，Bayes恒等式不自动赋予实践Jensen改善保证；Q^γ/logQ与非负归一权重有条件。有限YS、训练prior替prefix posterior、可负z-scored A、.95 nucleus截断已改变对象。γ1/2/4/8取2，guidedteacher50step全vocabKL，RL后conditional陈旧/反复蒸馏不稳定保留。仅保通用AR conditional likelihood-ratio近似机制，不恢复化学任务/排名；RL16×1000再2000best与γ搜索不同预算，8H100非请求SLO。5分标准Only经apr02必要原文独立核，不称整个算法已有或理论普适。[独立核](../_sources/daily-20260420/V3_APR02_SUBLIMINAL_RCFG_DISPOSITIONS.md)。

### [PolicyBank: Evolving Policy Understanding for LLM Agents — 2604.15505v1](https://arxiv.org/html/2604.15505v1)

实际§3–7必要深入：TypeI执行偏离与TypeII规范/解释不完整分开，trusted developer反馈形成capability/trigger/precondition/eligibility/action entry，benchmark annotation不是组织授权。21airline/9retail三类近邻sister、五order seeds不等远期heldout；pass^k不是pass@k，retail ReasonBank.90高于ours.89，82%是normalized gapclosure非整体成功率。解释反馈胜scalar与Fig3先过度放宽再修正支持诊断分支，恶意反馈futurework不采安全保证。实际Ch77 advisory之后两段补该差异，Memory仍不批准policy修改；root有限原始源→owner与实际写后通过，见[采用与写后记录](../_sources/daily-20260420/V3_POLICYBANK_LACE_OWNER_PROPOSALS.md)。

### [LACE: Lattice Attention for Cross-thread Exploration — 2604.15529v1](https://arxiv.org/html/2604.15529v1)

实际§3–4/§5及必要E.1/F.1深入：低维cross-thread QKV/3DRoPE/gate提供同请求中间表示交换，不是外部Agent或跨tenant通道；flattened SDPA未明示横向时间mask，不采用全实现无future泄漏。独有CPT/SFT/RL、shared advantage与best@4选择不与sameRLsteps/pass@1当全matched，1.7B Live16.5vs16反证保留。E.1单RTX PRO6000 Blackwell97GB/BF16/context50/gen100，N4 step1.7B20.5→28.4、4B27.6→36.2（约31～38%增加）且TPS下降，不足1.3%FLOPs不是近零延迟，N128 4B+96.4% step不外推p99。实际Ch14 Mask之后两段补routing分支、新增mask义务/缓存身份和独立采样回退；root必要源→owner及真实写后通过，见同一采用记录。

### [FineSteer: A Unified Framework for Fine-Grained Inference-Time Steering in Large Language Models — 2604.15488v1](https://arxiv.org/html/2604.15488v1)

实际v1 §5.1–5.3/Eq6–15、§6.1–6.5/§9与A.1必要阅读。mean-centered PCA/SER是gate代理，query-specific prototype+WQ/WK及residualMLP仍训练；one-class quantile、supervised logistic与direct soft SER三方案不混统一实现、SER不作harm probability。Qwen fullTruth54.28低于w/oSCS54.77，GSM改善不能代全部质量；A800每token40.43vs40.38非零代价，113秒非快于Alpha70，284.7GB为四卡累计。adaptive输入压低SER可绕过，不采彻底遗忘。

Ch72 activation redirection已有抑制≠删除与utility回归，未承载when/how训练分责；实际以“输入条件化干预还可以把‘何时启动’与‘如何改变’分开”嵌两段，不新建安全架构。[apr02必要源→owner及root实际正文写后核](../_sources/daily-20260420/V3_APR02_FINESTEER_INDEPENDENT.md)均通过，未复现实验。

### [Predicting Where Steering Vectors Succeed — 2604.15557v1](https://arxiv.org/html/2604.15557v1)

实际§3–5及D/F/H/J必要controls。A_lin仅finalnorm+unembedding logit-lens单token输出对齐，低值不证明所有线性探针读不出或任何干预无效；J中trained linear probe每层>93%而早层ΔP近零恰好区分可读/可控。H n130为layer×family不是独立样本，within-family permutation不保autocorrelation，partialdepth不自动消除它；geo partial .372p.067不是全显著，F thin4/dark3 target少、best-layer/oracle selection非heldout生产controller。3090Ti24GB数小时成本非在线p99，实体20+20prompt演示非全部成功率。root 独立必要源与实际owner核发现 Ch31 缺“可读≠沿原输出head对齐≠真实干预有效”的前置选择边界，已在 conditional actuator 后、按层反馈前实写；[非书稿作者实际写后复核](../_sources/daily-20260420/V3_APR20_15557_CH31_WRITE_AFTER_INDEPENDENT.md)通过。只吸收有限层选择与失败反证，不采用概念内部三阶段、所有方法无力或全selection百分比，不预支本日Gate。

### [(1D) Ordered Tokens Enable Efficient Test-Time Search — 2604.15453v1](https://arxiv.org/html/2604.15453v1)

v1 §3–5.5/§7及D.3/E.4/G必要原文支持经训练coarse-to-fine表示下的partial-prefix重建与verifier beam分支；不把任意1D序列称语义有序、不采用AppendixB全局界。保留matched2D比较、重建/branch/verifier成本、NFE≠时间、内部verifier分提高而外部质量下降及弱prior反例。实际Ch24以“逐token概率可预测，还不等于部分prefix已能被质量sensor辨认”补两段，保留grid/完整BoN/lookahead共存。apr02[必要源→实际owner核](../_sources/daily-20260420/V3_APR02_SOTO_SIGN_SKILL_INDEPENDENT.md)和root[真实正文及相邻衔接写后核](../_sources/daily-20260420/V3_ROOT_SOTO_SIGN_SKILL_WRITE_AFTER.md)均通过，未复现实验。

### [StoSignSGD: Unbiased Structural Stochasticity Fixes SignSGD for Training Large Language Models — 2604.15416v1](https://arxiv.org/html/2604.15416v1)

v1 §2/3.1–3.2及B.2/Table10–12必要原文支持正坐标包络内随机sign的期望v/G，不是raw gradient无偏；理论无momentum投影过程与实践EMA/历史包络分开。采样、方差、zero handling、历史尺度与随机恢复状态保留，FP8比较绑定BF16 master/nonlinear及具体梯度/state格式，不泛化所有AdamW失败。实际Ch28 sign geometry后以“确定性sign便宜，却把不同幅度映成同一方向”补两段；同一apr02源→owner和root真实写后核均通过，不采用摘要精确speedup/普遍排名。

### [HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents? — 2604.15415v1](https://arxiv.org/html/2604.15415v1)

v1 Benchmark Construction/Evaluation、Tables5–7、Results/Limitations支持用户主动安装公开有害declared capability与隐藏payload的不同威胁模型，平台policy不由用户同意自动授予。200自然语言skill、六API模型不执行脚本，task/plan/effect、judge/policy版本及误拒绝成本分账；HiTL/disclosure文本建议不等真实批准或外部告知。实际Ch72 SkillPoisoning中以“Skill admission还不能只查描述是否与代码一致”补两段并保低风险轻审及effect授权，同一apr02源→owner和root真实写后均通过，不作现实事故率或法律裁决。

### [Taming Asynchronous CPU-GPU Coupling for Frequency-aware Latency Estimation on Mobile Edge — 2604.15357v1](https://arxiv.org/html/2604.15357v1)

实际读v1 §III–VI必要方法、joint aggregation、调频与反证。分别预测CPU launch/GPU execution并按频率依赖的间隙/重叠聚合；逐层求和或独立频率缩放不能还原跨层重叠。稀疏硬件计数、分段逆频率关系与模块消融支持该受限分支，不是全平台通用功耗模型。

Jetson AGX Orin/OrinNX、PyTorch/Transformers、GPT2-large/Qwen2-1.5B/7B decode上下文≤1024及三类DNN，CPU约0.1～2.2GHz、GPU约0.3～1.3GHz，板载INA3221读数。平均MAPE8.14%不是最坏/p99保证；QoS=min(actual rate/target rate,1)不是deadline概率。固定CPU最大值选GPU再降CPU的greedy不证明全局最小能耗；EWMA自引用不擅自修成可执行式。未复现或验证生产SLO。

实际Ch70原预算分解与Minos默认频率功耗/性能近邻曲线未承载joint launch/execute的频率依赖。已在该曲线后窄补两段成本预测、校准费用与实测回退，以“参考曲线还可能遗漏主机与设备的时间耦合”定位；apr02必要原文→实际owner审阅、root实际正文及相邻衔接写后通过。见[采用审核](../_sources/daily-20260420/V3_APR02_FLAME_LOGJACK_ADOPTION_AUDIT.md)。

### [LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents — 2604.15368v1](https://arxiv.org/html/2604.15368v1)

实际读v1 §III–VIII。42手工payload=32攻击+10良性，8模型/7provider/3prompt/5trial，temp0.7；同payload裸文本与运维日志tool result包装有检测差异。扫描只记录不阻断，两action tools拦截/分类proposal但不执行，所以不是实际RCE或生产安全验收。最多8turn且首危险proposal提前终止；verbatim与未外部验证regex influence不是同指标，良性历史命令也可能被复述。

原文删明显exfil URL后仍提出其余SSM动作，支持sanitization不能替代action authorization的受限失效，不证明所有guardrails普遍失败。Azure裸payload1/32、GCP0/32、AWS无对应tool-result扫描不能合并；Sonnet无verbatim但19.4%其他危险proposal、Llama良性baseline44%限制归因；example.com域名不等真实execution effect。

实际Ch72已有provenance、influence locator、authority registry、step guard和确定性tool policy。新有限增量是包装配对及清理后仍提动作的failure条件，已融行为控制权段落之后，以“运维日志也属于这条不可信输入链”定位，不新建安全架构。apr02必要原文→实际owner审阅与root实际正文及相邻衔接写后通过；仍非日级Gate。

### [A Systematic Study of Training-Free Methods for Trustworthy Large Language Models — 2604.15789v1](https://arxiv.org/html/2604.15789v1)

实际读v1必要方法、Training-Free in the Wild setup、结果/成本与limitations。四模型为Llama2-7B/Llama3.1-8B/70B、Mistralv0.2；采用原recipe而非每模型重调时，SEA-T在70B的HB安全效果为0而utility为1.0，说明迁移默认参数可失配，不证明方法本身永远无效。八个手选组合没有三轴全部改善，不等“所有组合必失败”。HB按non-refusal phrase检测不是实际伤害，TruthfulQA MC/BBQacc、Gemma3-27B judge utility与watermark green-token占比分别解释；70B GCG/AutoDAN未跑，不能升级完整威胁覆盖。

成本是MTBench单A100、不同输出长度的wall-time与peak量，未冻结长度便不能因果归于干预唯一开销；不采用普适排名、零成本或抗攻击watermark保证。具体有效窄结论由Ch72“Security Gate必须覆盖Defense Interaction、审计通道与部署变换”段承载：多个defense争用表示/控制点，必须组合interaction matrix、clean utility与分攻击失败归因，不能将单项安全分加和。root确认该narrowExisting边界；实际source证据与全部拟入选日级复核仍按§6处理，无新Books diff。

### [LLM Reasoning Is Latent, Not the Chain of Thought — 2604.15726v1](https://arxiv.org/html/2604.15726v1)

实际读v1 §3.3–§5.3、AppendixA.1–A.5与B；不因position名称当作没有实验。六arm的surface/latent/budget逻辑角色与matched-sham必要性/patch-specificity协议有效保留。AppendixA明确Qwen3-8B/32B/Llama3.1-8B，四受控任务族及GSM8K-Platinum/HotpotQA/MATH500/HumanEval，Tables7–9有逐模型budget frontier/AUC结果；这些是作者原始报告，不删除。

但中央matched-budget量化及latent因果headline依赖的控制仍未被公开材料说明：A.4仅列预算weight符号和tight tolerance，未给实际校准权重/容差、精确选中干预/sham配置与任务split数量；§5.1指向A的split sizes，A没有具体数量。所见HTML没有承诺的complete-code/supplement具体artifact入口。不能从未知seed本身断言结果伪造或强求全复现，也不能把未展开的匹配条件当已证明。只把这些中央比较/必要性保证隔离为争议，不以此支持Books；协议与表保留为作者披露但未独立归因的证据。root认可该有限隔离方向，最后非作者证据核仍未预支。

### [Evaluating LLM Simulators as Differentially Private Data Generators — 2604.15461v1](https://arxiv.org/html/2604.15461v1)

采用v1 §2/3/4.1–4.3的有界数据生成机制与反证；apr01实际必要原文独立核通过，作者也定点读§2.2到§5。DP统计经structured mapping进入规则/LLM simulator，learned prior可能令时间与人口属性偏移，且作者明示27个统计未全部传播到12维输出schema。后处理仅在已DP统计与固定非私有接口条件下讨论，不能把相同epsilon标签合成同邻接关系/全管线统一预算。

原源Kaggle是2000 synthetic consumers的multi-agent simulation，不是实测金融消费者；作者TSTR/Test-on-Real措辞不改变来源权限。80K/25%fraud direct synthesis与约5K/3% PersonaLedger的training support不匹配，same holdout100K/~.13%fraud与100 bootstrap CI不能消除此差异。PersonaLedger AUC .70/.51/.57与TVD .32/.30/.34分别绑epsilon1/5/10，不从非单调结果断言prior为唯一因果。仅保留这个有界schema/分布失配案例，不修改长期DP保证或建立新通用生成质量结论。见[三项有限独立核](../_sources/daily-20260420/V3_APR01_THREE_SCOPE_EVIDENCE_AUDIT.md)。

### [The Spectral Geometry of Thought: Phase Transitions, Instruction Reversal, Token-Level Dynamics, and Perfect Correctness Prediction in How Transformers Reason — 2604.15350v1](https://arxiv.org/html/2604.15350v1)

实际读v1 §3–4.7与必要AppendixB.1–B.3/E.1–E.3：SVD power-law slope与10token sliding window定义只提供几何diagnostic，不是thought真值；prompt/response和base/instruct改变符号，保留原始模型/阶段比较。11模型21任务，正确性支线六模型每200题/5foldCV，8RTX4090/float16/greedy、prediction max200/batch1。Pythia单类全wrong不能将通常AUROC=.5当标准二分类测量。

中央perfect/答前保证不能采用：原文混用Late与response phase并称before answer，但feature提取在预测时何时可用未清楚；采用最优层/阶段的held-out选择边界也未明示。实际OOD仅40题，7B AUC .600±.10、3B .44±.29；§4.7解释correct较低α，而E.1却称correct较高α为同方向，code tracing又反向。隔离这些量化/时序/普适方向保证，保留有效定义、表与这些反证，不据未知seed断言造假或删除整篇。必要材料已按拟采用命题定点读，重开仅需特征时序/方向与选择协议的可核澄清/更正，不要求全理论或复现；不写Books。

### [LinuxArena: A Control Setting for AI Agents in Live Production Software Environments — 2604.15384v1](https://arxiv.org/html/2604.15384v1)

v1 §3.2–3.5/§4.1–4.3/§5.1–5.4/§6实际深入阅读。main/side-task scorers分开，live harm要发生前flag而delayed可全轨迹审；attacker未按main质量评分，不能声称合法工作同时成功保证。monitor两call mean、honest score percentile和随机ties设step-wiseFPR；Safety=Pdetected/(Pdetected+Pundetected-and-success)不是单段生产事故率，step-wiseFPR也非episodeFPR。

LaStraj人工≤8h迭代到指定monitor低score，main可新造、补synthetic exploration后被发现者过滤；model比较也条件于side-task success。它揭示所见model elicitation未饱和，不是人工最坏上界。synthetic placeholder、无生产CI/CD/权限中介、20环境、scorer干扰/accidental side成功限制外推，原文不构成完整控制协议验收。实际Ch72“Control Evaluation要测试Attacker如何选择攻击时机”已冻结generator/quality estimator/submission/attempt/audit budget，明示选择器未充分激发只能得已见下界；这个窄命题已有覆盖，不假称全文benchmark/具体step-FPR配方全被写入。

### [Temporal Contrastive Decoding: A Training-Free Method for Large Audio-Language Models — 2604.15383v1](https://arxiv.org/html/2604.15383v1)

实际读v1 §3.1–3.4/Eq1–9、§4.2–4.6、AppendixA/B Table7。平滑waveform重编码构造慢时间尺度参考，同一文本history下比较原/慢路径，以音频依赖和不确定性gate限制top-K正logit残差；不把waveform smoothing与latent Eq1当严格等价实现，也不称消除语言prior或恢复声学真值。去gate/signed/noisy参考消融及分离编码架构失败、强speech模型退步保留，收益依赖decoder实际可访问该时间差。

运行时Table7绑定单A80080GB/eager attention/3秒音频100token、优化复用原KV，prefill2.04×、decode.99×、memory1.01×不是服务零成本；主实验4A100与该测试不混用，batch2 memory-bound可能掩盖开销。Ch23 shared-prefix反事实之后真实补入两段，以“音频反事实还要选择保留什么时间结构”定位，交接Ch49/56成本与SLO，不改runtime责任。apr02[必要源→当前owner通过](../_sources/daily-20260420/V3_APR02_TCD_NGD_INDEPENDENT.md)，root[实际写后通过](../_sources/daily-20260420/V3_ROOT_TCD_NGD_WRITE_AFTER.md)；没有复现实验或全日验收。

### [Natural gradient descent with momentum — 2604.15554v1](https://arxiv.org/html/2604.15554v1)

实际读v1 §3.3–3.4、§4.2.1/Eq24–28、§4.2.2/Eq29–30、§4.2.3/Eq31–33、§5.1–5.3/§6。旧函数momentum由旧Jacobian生成，用cross-Gram投影当前tangent，再以当前Gram逆/伪逆回参数；不称精确parallel transport。NHB-FD两次forward差分减少保留旧Jacobian的状态，QNHB直接复用参数momentum只为局部近似恒等几何，不是无成本精确替代。

有限Mackey–Glass/XOR对照、50realizations median、谱floor/clip与步长限制采用；较少iterations不等较少wall-clock，FD可更慢/发散而降beta才稳，line-search也增加成本。大模型随机minibatch/vector outputs仍future work；不恢复PDE科学应用、不宣称LLM普遍加速。Ch28“聚合梯度与逐样本残差是不同的更新坐标”已有当前步，而新写两段以“这种局部坐标还会随参数更新而变化”补历史坐标handoff，保留无动量NGD/AdamW/SGD。apr02同一有限审核通过source→owner，root真实两段与邻接写后通过。

### [Dispatch-Aware Ragged Attention for Pruned Vision Transformers — 2604.15408v1](https://arxiv.org/abs/2604.15408v1)

v1 §III–VII必要方法/端到端/反证实读：DeiT H12/d64、seq≤197、A100SXM40、PyTorch2.8/Triton3.4/FA2.7、10warm/500timings。FA2 .063ms与Triton .04ms底噪的wrapper解释不是独立host分层测量，BS64/N197 FA2 .113ms反而快于Triton .207ms。对FA2端到端BS≥32约≤1%、小batch约5–8%，对padded最多2.24×不同分母不合并。pack及CPU sync仍有成本；max-logit有.0048～.0063差但top1一致，不称bit-exact或剪枝无质量损失。Ch49实际launch-bound profile、TaxBreak分层、WebGPU残差≠API测量已覆盖这一窄判断，不覆盖整篇ragged算法。

### [Think Multilingual, Not Harder: A Data-Efficient Framework for Teaching Reasoning Models to Code-Switch — 2604.15490v1](https://arxiv.org/html/2604.15490v1)

v1 §3.1–§4.2/§5与A.15实读。三student Qwen3-8B/Phi4Reasoning14B/DeepSeekR1DistillLlama8B、Qwen3Next80B teacher，七语言六任务各1Mtoken（Yoruba两任务缺）、GlobalMMLU500validation/500test；LoRAall/3ep/lr1e−6/bf16/effectivebatch16，token预算不是同样example数量。MT空reasoning也改变CMI/Mindex，Englishmatrix/accuracy与correctness为mixedmodel关联，密集Iindex反而负关联；不证明switch是唯一原因或越多越好。LID/rater/翻译与teacher条件保留，taxonomy规模intro17/21与methods15/18不合并，100人工样本85%plausible也非reasoning truth。仅报告非reasoning SFT影响trace语言的跨任务行为证据，不推出必须English/新通用多语教学保证。

### [EvoRAG: Making Knowledge Graph-based RAG Automatically Evolve through Feedback-driven Backpropagation — 2604.15676v1](https://arxiv.org/html/2604.15676v1)

v1 §4.3 Eq3/4/5；两条单triplet路径p=(.2,.8)、α=.5、U=(1,0)的正确导数−1/3，Eq5额外乘概率积给−1/15。相同utility不保证唯一最优、E→0不支持uniform有界logloss；只隔离exact backprop/唯一稳定收敛与无条件noise保证。保32B生成器/judge、RGB300/MTH816/HPQ600和受限feedback消融，不把改关系当不改fact。2A6000/503GB、完整精度/CI/SLO ND。重开需一致目标/导数、合法utility下界及条件化convergence；不否定全部架构或要求全复现。 [有限非作者核](../_sources/daily-20260420/V3_APR02_THREE_METHOD_DISPOSITIONS.md)已通过；不代替本日日期或整日Gate。

### [SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems — 2604.16022v1](https://arxiv.org/html/2604.16022v1)

v1 §2.1–2.6/§3.1–3.2/C.2；SocialGrid七乘七任务/社交benchmark区分task完成、arrival、已完成中的路径效用、非skip投票accuracy。A*导航建议不等执行oracle；33%只初始2/6，C.2动态机会集不沿用全程常数。不同组配置/人数不能并成单一内部社交能力；保局部失败，不采所有LLM失效或keyword行为因果。有限协议的新分账仅报告，不签游戏全算法Existing。 [有限非作者核](../_sources/daily-20260420/V3_APR02_LATEST_FIVE_16022_16044_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [Where does output diversity collapse in post-training? — 2604.16027v1](https://arxiv.org/html/2604.16027v1)

v1 §3.1–3.3/§4.1/4.2/4.4/§5；13个Olmo7B checkpoints三lineage，Instruct起自ThinkSFT同时换数据/DPO，非only-teacher matched干预。16次T.6/p.95/最长32k池kernel、correct Kc≥2的选择支持不固定；写作/IFEval有恢复，不采never恢复。RLZero较高多样性伴质量成本，SBERT/Vendi共kernel非独立双证。只保质量—多样性和lineage限定，不证明通用floor或增加Books。 [有限非作者核](../_sources/daily-20260420/V3_APR02_LATEST_FIVE_16022_16044_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning — 2604.16029v1](https://arxiv.org/html/2604.16029v1)

v1 §3.2/§4/5.1–5.3/B.3/F.2；冻结generator的prefix KV上临时追加STOP/LoRA/分类头，评分后丢临时分支、正常续写关LoRA；MC32成功标签是模型/采样条件估计非逻辑proof。avg@8|64是selected路径均值非query成功，单H100/7B/b16/prefix2048 total34.33s>33.20s、吞吐−2.71%；MC监督构造43.08–75.93h不是完整训练。MODEL-SAMPLING [Ch20](../../../../books/part-02-model/20-sampling.md) feedback-control末真实两段补状态隔离和预算/回退；apr02源→owner/literal及root真实写后通过，不采attention必要因果/普适保留率/tailSLO。 [有限非作者核](../_sources/daily-20260420/V3_STOP_OWNER_PROPOSAL.md)已通过；不代替本日日期或整日Gate。

### [Stochasticity in Tokenisation Improves Robustness — 2604.16037v1](https://arxiv.org/pdf/2604.16037v1)

官方PDFv1 §4.1–4.3/§5.1–5.3/§6.1/T2–3；STOK-UNI对splitcount条件化均匀，UNIFORM-K才字符串级给定edit distance支持，构造MDD有成本。50M及1B LoRA的有限augmentation/ICL非同totalbudget，一层1-Lipschitz/bounded-weights理论不覆盖任意LLM、有限攻击不证明全认证。MODEL-TOKENIZER [Ch11](../../../../books/part-02-model/11-tokenizer.md)“Tokenizer与checkpoint是联合行为接口”真实承载同string分割影响embedding/position/attention、artifact绑定、回归与canonical回退；仅该命题Existing，不称全sampler已覆盖。 [有限非作者核](../_sources/daily-20260420/V3_APR02_LATEST_FIVE_16022_16044_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [Elucidating the SNR-t Bias of Diffusion Probabilistic Models — 2604.16044v1](https://arxiv.org/html/2604.16044v1)

v1 §4–6/B Eq22/27/28/C；Eq27将向量二阶矩写均值范数平方+范数方差，X等概率±1给1≠0。Jensen能量不增有效，但二元prior的posterior mean是有界tanh，不能无条件写固定scalar缩放+非退化Gaussian；递推也须联合而非仅边缘Gaussian。只隔离任意reverse逐步低SNR与唯一原因保证，保wavelet/differential局部表、固定NFE不等无所有额外成本。重开需合法误差/联合分布条件和修正公式，不扩大所有diffusion否定。 [有限非作者核](../_sources/daily-20260420/V3_APR02_LATEST_FIVE_16022_16044_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [On the Rejection Criterion for Proxy-based Test-time Alignment — 2604.16146v1](https://arxiv.org/html/2604.16146v1)

v1 §2/§3/T1/§4.1；统一等价须同α全token满足q*α≤s≤p+q*α，不是无条件all rejection。OLMo1/13B、Qwen1.7/14B、五集/T.7/dev调margin；CSQA λ0 74.7<base76.9，proxy可更差，概率分散不等知识不足。OLMo40pp与正文37.4不合、不同Qwen表/文字不并；完整双模型成本/HW/precision/CI/SLO ND。只保局部拒绝规则，不签安全alignment或普适更优。 [有限非作者核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency — 2604.16158v1](https://arxiv.org/html/2604.16158v1)

v1 §3.1–3.4/Eq2–5/§4/T1/§6；c=−.4，H=c时H/c=1、H=0时0，不是重新启用越强奖励越高。all-zero mask不使一般CE零；若T为0/1下三角，归零未来logit也不单独构成causal mask，但不据此断言实际代码泄漏。保200mask AdamW步、48A100、Llama3.2-3B/GSM与MMLU各1000/pass4、GSM90→89.6和tokens186.6→104.4；compression不证明faithfulness，作者§6亦待验证。重开仅reward符号/互补、zero-CE/causal说明，不否定局部结果或全复现。 [有限非作者核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [Sketching the Readout of Large Language Models for Scalable Data Attribution and Valuation — 2604.16197v1](https://arxiv.org/html/2604.16197v1)

v1 §2.2–2.5/Alg1–2/§3/T2–4/D.1–4/E/F；RH/GH factor CountSketch与topmass residual使forward index可行，head/truncation有bias，实际factor/最终L2非线性不能继承原无偏。D.2 constant1 bound取x=y=(1,1,1)、K1时Z=(Σs)²：EZ3、Var12>9，只反驳该常数及依赖界，不否CountSketch无偏/O(1/K)。保Pythia1B6.7GB>3.6GB但17.6ms<590ms、32B72.8GB/64.4ms、BrainRot小闭环ARC26.62<base26.88；μ±δ非CI、8H200与GH200不同testbed未全row绑定。重开交叉项修正/归一target/matched维度，不为印刷理论保证写Books。 [有限非作者核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [NVBench: A Benchmark for Speech Synthesis with Non-Verbal Vocalizations — 2604.16211v1](https://arxiv.org/html/2604.16211v1)

v1 §2.3–2.4/§4.1–4.5/T3–6/§5–6，正式NVBench非后稿NVV-SuperBench；80EN/30ZHseed→45types/4500 text非audioGT。GT-conditioned verifier知道target/unchangedtranscript，NTD只TP，coverage supportedtypes/45非成功率。三objective runs、human/LLM一run450/语言97raters，Gemini多角色非独立truth；EN GeminiPro CMOS自然−.24/质量−.18/表达+.05，WER可罚笑而人类自然度较好。15系统未matched全model/training/voice，有限多轴协议仅报告，不签blind检测/所有排名或未知type安全保证。 [有限非作者核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations — 2604.16217v1](https://arxiv.org/html/2604.16217v1)

v1 §3/4/T1–4/A–D；LI是question/null逐层realized NLL差非真实Shannon entropy，answerpool minmax+frequency fixed score。五3–14B白盒、M20/50/10、T1/p.9、100split非训练seed；CoQA/Vicuna有反退，crossdomain无交换性theorem。C s=∞且q=∞时s≤q不等存在admissible：N1/α.5、sampler全错误可交换，A经验floor.5亦满足，coverage0<.5。保A子集下界/LI有限表，只隔离C无条件保证及向shift外推。重开须fallback/coverage定义、候选存在条件或含采样失败的正确risk，不全附件或全模型复现。 [有限非作者核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)已通过；不代替本日日期或整日Gate。

### [Mind’s Eye: A Benchmark of Visual Abstraction, Transformation and Composition for Multimodal LLMs — 2604.16054v1](https://arxiv.org/html/2604.16054v1)

初筛曾仅据八任务与人模分数差前关闭；否定侧定点抽检重开 exact-v1 §4–5/Fig8–9/Appendix A/B.8 后改判。其八个视觉抽象、关系、变换操作对提示臂的反应不同：meta-task/step-by-step 在若干符号规则任务改善，Mental Composition/Transformation 的替代提示反而多退步。因而对同一多模态模型仅报告统一prompt/总分，会遮住“规则归纳”和“内部视觉变换”不同的评价条件，属具体测量边界而非因benchmark名字准入。该效应多为约0.4–1.8点、未给跨模型配对置信区间，不能说替代提示普遍因果有害；100→300 DPI仅一个Qwen视觉模型，不排除其它感知瓶颈。Appendix B.8模型MT/PF distractor检验为p=.44/.52，但**人类PF p=.014**与紧接“两项均>.05”的文字冲突，故隔离人类/模型均匀误选的合并保证，保留其余有效任务观察。实际Ch66已要求 EvalSpec 保存构念、提示变体和能力切片，本篇未建立另一长期owner命题，标准仅报告，无Books新增。[root有限非作者准入/处置核](../_sources/daily-20260420/V3_ROOT_16054_FINITE_INDEPENDENT.md)通过；不是整日来源、日期或候选集Gate，未复现实验。

### [DPDSyn: Improving Differentially Private Dataset Synthesis for Model Training by Downstream Task Guidance — 2604.15660v1](https://arxiv.org/html/2604.15660v1)

否定侧抽检撤销了原“DP分类器后处理保护整份数据”的前关闭。exact-v1 §3.2 Algorithm 2 第4–10步把原始私有属性矩阵 `X` 逐列置换为 `X̃`，再用 DP-SGD 分类器给 `X̃` 打标签并把属性和标签一并发布；§3.3 却把分类器的 `(ε,δ)` 保证推给整个发布数据集。对单记录替换邻接 `x=0` 与 `x=1`，置换恒等，事件“发布属性含 0”的概率分别为 1 和 0，任意有限 `ε`、`δ<1` 都无法满足 DP。多记录列置换同样保留各列多重集合。此反例只隔离**印刷算法及据它提出的完整发布保证**；未核可选代码，不断言实际部署泄漏或所有 DP 合成不可行。§4 四个 Adult/Br2000/LPD/Smoking 表格任务的 utility、效率观察可保留，但不能作为隐私证明，也不是本书的大模型数据配方。

本项目关心的是训练数据发布对象与保护单元的责任边界，不因表格应用就忽视纠错，也不从论文摘要的 AI training 词汇推出大模型机制。按 `3+2+3=8` 作安全纠错定点深入，Ch27负责数据血缘，Ch72 已有“只有 DP output 的后处理不增加预算、最终发布对象须另核、accountant与实现同构”的具体长期命题，因此 Books `No Change — Existing Coverage`，不将争议论文写作正面机制来源。可重开材料仅需对 `X` 的独立 DP 机制、明确排除公开属性的威胁模型，或与修订算法一致的联合预算/发布对象证明；不要求全附件或重跑四表。[作者反例](../_sources/daily-20260420/V3_15660_REOPEN_AUTHOR.md)和[root必要原文→实际 owner 非作者核](../_sources/daily-20260420/V3_ROOT_15660_FINITE_INDEPENDENT.md)均在案。该 ID 的 Submitted 04/17 不是 first-public；具名联合 OAI/编号/公告链见[日期复查](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)，整日日期 Gate 尚未签署。

### [Bridging the Gap between User Intent and LLM: A Requirement Alignment Approach for Code Generation — 2604.16198v1](https://arxiv.org/html/2604.16198v1)

旧题摘前关闭只看到“需求重述/自检循环”，但 exact-v1 §3.1–3.3 给出两个不同检查点：先从原始需求构造 question/reference-answer checklist，让生成模型逐项回答，定位误解后再生成代码；若代码未通过公开测试，再遮蔽需求关键片段，要求从已生成代码反推片段并更新 checklist。选择先检查理解而非只增加候选代码或事后 execution repair，有一条局部、可审的验证机制。Table 2 在四模型与五个编程 benchmark 上分别去掉 QA 或 MASK，多数条件退步；§6.1 Table 3 的首轮（尚无后置 MASK）也优于 zero-shot，因此改善不全是“多轮再试”。但不同 arm 的总 token/时间未配对，不能把增益全部归为检查点本身。

评价必须把 Pass@1、成本与 spec authority 分开。Table 1 的 Qwen3-Coder full 方法为 2.65 小时/11.78M token，zero-shot 为 0.34 小时/0.74M token；该数据集级成本不是单请求生产 SLO。question 的 reference answers 与比较判断仍由模型据原需求及少量人工示例生成，公开 tests 只是停止条件，均不能独立证明用户意图被正确理解；真实仓库、CI、并发及用户签收未给。故 `2+1+2=5` 标准、仅报告有限 coding-agent 验证分支与负担。实际 Ch79 的 `requirements→implementation→tests` 和 machine-checkable completion 已保最终验收责任，不因局部 recipe 新增 Books；这不是声称原章覆盖本文所有 QA/MASK 实现。[作者定点复查](../_sources/daily-20260420/V3_16198_REOPEN_AUTHOR.md)与[root非作者准入/必要证据核](../_sources/daily-20260420/V3_ROOT_16198_FINITE_INDEPENDENT.md)通过，具名日期另见[联合链](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)，不等于整日 Gate。

### [CodeMMR: Bridging Natural Language, Code, and Image for Unified Retrieval — 2604.15663v1](https://arxiv.org/html/2604.15663v1)

旧题摘以 shared embedding/RAG 迁往五视觉代码域为由拟前关闭；exact-v1 §4.1–4.2/Tables 2–3、§6–7 与[非作者定点复核](../_sources/daily-20260420/V3_ROOT_15663_FINITE_INDEPENDENT.md)显示该理由漏掉了可保留的负载边界：同一检索器在 query/return 模态方向、长 SVG 结构和未见组合任务上并不对称。Table 3 的 CodeMMR 2B 对未见 Sketch2Code `image→code` Hit@1 只有 0.5%，ChartEdit `code→image` 为 100%；pooled nDCG 与“统一”名称均不能代替 typed workload 验收。§7 仅两个 image→code 生成任务的 No RAG/GME/CodeMMR 对照支持局部 RAG 收益，不覆盖真实代码库、ACL、索引更新或 serving SLO；Table 2 的 SVG 方向弱项也禁止宣称普遍跨模态泛化。

`2+1+2=5` 标准审阅、仅报告。实际 Ch76 已要求异构语料的 typed query/operator、证据身份、retriever 与生成效果分别验收；本篇提供该责任链下的具体反例，但没有新的长期 canonical 命题，不增 Books，也不称该章已有 CodeMMR 全配方。[作者原文定位](../_sources/daily-20260420/V3_15663_REOPEN_AUTHOR.md)及[root 必要源→实际 owner 核](../_sources/daily-20260420/V3_ROOT_15663_FINITE_INDEPENDENT.md)均保留。`Submitted` 04/17 不等于首次公开，具名[公告批次联合链](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)支持本窗归属；整日日期与分母 Gate 未签。

### [Beyond Single-Model Optimization: Preserving Plasticity in Continual Reinforcement Learning — 2604.15414v1](https://arxiv.org/html/2604.15414v1)

exact-v1 §3–5/Table1/Figs1–7 的 policy archive 以短 transfer probe 选源，重置 optimizer，并用 replay/distillation 与全库重嵌维持 trajectory latent 坐标；它不同于只保存最新 PPO policy。五个 MiniGrid 任务、20 runs/95% CI 中 full SR .706/TTT3.35M 对 ScratchReuse .525/5.49、Static .507/5.59，但 ScratchReuse 有 BWT 反向，full coverage .50 并非全部学会，probe/library/reembedding 也另付成本。`2+1+2=5` 标准，仅报告受限能力重访；Ch32/35 的策略身份与 checkpoint 责任未变，不把小环境结果外推成大模型普遍 plasticity 保证。证据见[作者审阅](../_sources/daily-20260420/V3_SIX_ADMISSION_EVIDENCE_AUTHOR.md)。

### [Robust Synchronisation for Federated Learning in The Face of Correlated Device Failure — 2604.16090v1](https://arxiv.org/html/2604.16090v1)

exact-v1 §2–4.2.5/Eq13–15/Tables1–5 说明设备 availability 与本地标签支持相关时，快/常在线参与方会被过采；共同故障可让相近非IID类别在单轮整组缺席，边际频率校正对已到梯度施权不能恢复未观察到的支持。现有 Ch36 仅写单 worker 到场偏置、intended objective 与 stale direction 分账，未明说这一联合覆盖边界；root 已在该段后定点写入参与率/类别覆盖/仅覆盖类质量、隐私可见性和旧校正共存，[apr01 顺读原文与真实正文、邻接、Review note 后写后 PASS](../_sources/daily-20260420/V3_APR01_AWPSP_CH36_WRITE_AFTER_INDEPENDENT.md)。Eq15 的 `1−risk` 乘积未披露所有概率输入的 clamp/归一条件；10个实际 worker 分波模拟100–3000逻辑 client、accuracy 只对 covered labels 算，Table5 自身33.75→29.78 的降幅也不支持“所有指标更 robust”或大模型生产收益。`2+1+2=5` 标准因真实 Books 缺口触发最窄深入，不升全篇 7 分；见[作者源→owner提案](../_sources/daily-20260420/V3_AWPSP_CH36_OWNER_PROPOSAL.md)与[apr01必要证据核](../_sources/daily-20260420/V3_APR01_SIX_ONLY_EVIDENCE_INDEPENDENT.md)。这只签单篇 Books 写后，不签整日 Gate。

### [The Metacognitive Monitoring Battery: A Cross-Domain Benchmark for LLM Self-Monitoring — 2604.15702v1](https://arxiv.org/html/2604.15702v1)

exact-v1 §2–4 的524道题、20模型、一次性 item context 用 KEEP/WITHDRAW/BET 与错误条件撤回差衡量行为监测；T1–5预注册，T6探索性，不得把全部实验称预注册。预设阈值±5个百分点可改变9–10/20模型画像，α=.54、split-half=.51 显示量表稳定性有限；retro/pro 的 r=.17、Fisher CI[−.29,.57]与 n=20 不足以证明两能力独立。它测量特定任务/评分条件下的可观察选择，不读出内部 metacognition 架构或稳定人格类型。`2+1+2=5` 标准、仅报告评价分母和阈值敏感性；Ch66 EvalSpec 的构念、切片与样本责任不因此改写。必要方法/反证见[作者原文笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows — 2604.15715v1](https://arxiv.org/html/2604.15715v1)

exact-v1 §3.3、Algorithm 1、§4.1、§6.3–6.5 与 Tables 6–7 把无工具错误的 ToolSR、最终 artifact 的 weighted-leaf rubric root 与真实任务效果分开；Kimi 89.85 ToolSR 对 8.33 root 已说明工具调用有效不等任务完成。132个 workflow 来自154原始任务，经扩写/精炼，不等原始真实需求全部成立。Table 7 的30任务子集换框架时 Claude root 0→50，时间50.1→136分钟、费用约10→35美元、score/cost .249→.195，不能把准确率提升写成免费或单组件因果；human30标注与 judge 相关良好不排除其 .46–.93 的正向偏置。`2+2+2=6` 标准、仅报告有限 tool/rubric/cost 分账；Ch66/79 已将评测提案与外部执行结果分权，无新通用成功保证可写 Books。必要证据见[作者原文笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [Privacy-Preserving LLMs Routing — 2604.15728v1](https://arxiv.org/html/2604.15728v1)

exact-v1 §2.2、§3.1–3.5、Tables 1–5 的 semi-honest 双方 MPC 只保护 router encoder/选择，不自动覆盖最终 provider 或执行轨迹。其印刷 §3.3 对每对分数使用严格 `>`，按列和阈值取 top-k；若所有分数并列且 `0<k<n`，全部比较为0、mask全0，返回零候选而非 k 项。这仅反驳**打印 exact top-k 保证**，不证明实现同错或发生泄漏；2ReLU 全非正输入的分母定义也需说明。并行 `n²` 比较减少轮深，不等字节更少：Table 4 约9.985 MB/52轮/.248s，对 bitonic 1.23 MB；秒级路由表亦不包含最终 LLM 生成。`2+2+2=6`，因中央正确性反例定点深入、窄争议暂缓 Books，保留近似 encoder 与有限成本表。仅在作者给出并列值 tie-break/fallback、零分母定义及同版可核实现后重开该保证；Ch72 不把该争议配方用作隐私正面证明。完整公式定位见[作者原文笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [Accuracy Is Speed: Towards Long-Context-Aware Routing for Distributed LLM Serving — 2604.15732v1](https://arxiv.org/html/2604.15732v1)

exact-v1 §3–7 用 SCBench UUIDKV100 题、50/50 split、三语与4–64k长度，在五模型实例、vLLM .16/A100 80GB/10Gbps/concurrency8下，将多次尝试直到首个正确答案的 TTCA 作为成本；其 first-correct 判断依赖 exact-match task oracle，10次皆失败为右删失，生产 router 不会天然知道正确性。路由分数用语言/长度桶的经验成功率 Q、生成成本和 α=.7 的 queue 修正，但 router 自身毫秒开销未计入 TTCA；首答准确率有反退，64k存在全部模型不能解决的条件。`2+2+2=6` 标准、仅报告有限重试/能力先验取舍；Ch56 已拥有质量、队列与 SLO 的路由责任，不把 UUIDKV 局部 oracle 指标上升为普适在线最优或生产尾延迟保证。必要证据见[作者原文笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [VoxMind: An End-to-End Agentic Spoken Dialogue System — 2604.15710v1](https://arxiv.org/html/2604.15710v1)

exact-v1 §3–4 让 StepAudio2 先完成 reasoning，再并行当前 local-tool action 和 auxiliary global-tool 候选检索；只有显式 retrieve 才把候选并入 local set，辅助提案不是直接执行。Eq4支持该后置并行，不证明任意 preemptive overlap 或无限工具规模 O(1)。2×H20训练、有限工具数下 wait50tools约 .0154s 只是均值条件，不是 p99；真实录音与匹配 TTS 的 FS86.00 对93.33、PF60.67对67.33，IFEval39.64→18.83，说明语音/文本能力及输入分布有反退。2+1+2=5标准，仅报告关键路径外工具管理分支；Ch78 的 discovery→authorization→effect 执行合同并未被新的整体 agent 架构替换。成本和评价条件详见[作者必要证据](../_sources/daily-20260420/v3-reopen-notes.md)。

### [Into the Gray Zone: Domain Contexts Can Blur LLM Safety Boundaries — 2604.15717v1](https://arxiv.org/html/2604.15717v1)

exact-v1 §3–5 的八主题、三模型与对齐/mismatch 上下文对照支持有限 context×目标的拒答边界；安全研究语境并不授予请求执行权限。其三次 retry、两 trial、四 round、八 variant 再择最高 judge 的流程使高 ASR 是选择后协议值，不是单请求风险；DeepSeek judge 的长输出净化以及20个人评样本的有限一致性也不能充当真值。Qwen 的层24投影/attention诊断不识别唯一训练成因；Table 3 残余 ASR 与某防线全拒又分别提醒漏防/误拒。2+2+2=6，因保护边界作定点深入，仅报告；Ch72 已有内容与 authority 分离、attempt 预算及防御效用并验责任，本文不证明普遍防线崩溃，也不带入有害 payload。范围与反证见[作者笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [When Do Early-Exit Networks Generalize? A PAC-Bayesian Theory of Adaptive Depth — 2604.15764v1](https://arxiv.org/html/2604.15764v1)

exact-v1 §III-A 的 Step 4 明写对 uniform prior 的 KL 为 ln K−H(D)，Step 5 却让它的 −ln K 与 union 的 +ln K 抵消；取 K=2 且所有样本同一深度，则 H=0，KL 和分配 δ/K 的 confidence 常数各含 +ln 2，无法由已印步骤推出 H-only bound。Corollary 2 又去掉 KL，但确定性路由不意味着学习后 posterior 等于 prior；这仅隔离其理论保证和无标签/无验证可认证的推论，不否定深度-质量实验及原假设下的其它观察。已核 MathML 原式中 sqrt(2ln2) 正确，不沿用抽取丢根号的伪反例。2+1+3=6 纠错定点深入、窄争议暂缓 Books；重开只需 KL/union 符号一致证明及 fixed/learned backbone/router 的合法条件，不要求全附件复现。详见[作者定点公式笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs — 2604.15780v1](https://arxiv.org/html/2604.15780v1)

exact-v1 Methodology 的 safe/unsafe outputs、Wanda 代理、组件排序和 greedy/beam mask 搜索是具体资源受限分支，但不识别唯一 unsafe 子网。所印 L=CE_safe−CE_unsafe 要让 safe loss 低、unsafe loss 高就应选较小 L，正文却保 highest L；例 A(1,4)为−3，B(2,1)为1，打印选择 B 与所述目标方向相反。这只隔离 beam 的该方向保证，不抹掉 greedy 和表中实验；Table 1 的 beam over-refusal 46 对 baseline22.7，utility7.13<8.07，又显示保护/可用性不可合并。mask 建立峰值内存18–48GB与 beam 2457–16722s 不能被部署零额外 token 一句抵消。2+2+2=6 纠错定点深入、窄争议暂缓；重开需目标符号/排序及实际选择实现的同版说明，不要求复现全部攻击集。原文边界见[作者笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [MEDLEY-BENCH: Scale Buys Evaluation but Not Control in AI Metacognition — 2604.16009v1](https://arxiv.org/html/2604.16009v1)

精确 v1 §2、§3.6、§5 的35模型/130案例将独立判断、B-Private 和接收 A 摘要的 B-Social 分为不同条件，不是同一轨迹的连续更新。100例无唯一 GT，Brier 对 soft-consensus pseudo-GT；ipsative 去均值只标该 rubric 的相对弱项，不给绝对 metacognitive truth。progressive11为 purposeful 而非 iid，scale 各模型训练预算不匹配且 Gemma4 评价62.3低于较早27B72.9；局部相关和 bootstrap CI 均不能证明参数规模导致控制能力。旧“social-summary 渲染 v1.5 修复”线索未在 exact-v1/定点仓库证据确认，不能作为已知 bug 反推论文全部社交结果无效。2+2+2=6 标准，仅报告多条件行为评价和相对/绝对分账，不新增内部认知结构 Books 命题；若取得原始修复/采样输入，只重开受影响 Social 条件。见[作者来源核](../_sources/daily-20260420/v3-reopen-notes.md)。

### [SoK: Security of Autonomous LLM Agents in Agentic Commerce — 2604.15367v1](https://arxiv.org/html/2604.15367v1)

exact-v1 §III–V 汇整 prompt-to-key、交易参数、custody/认知分离等风险路径，30行 blind coding中只有17行完整双 coder，κ值证明标签一致而非防线有效。核心具体纠错是 §II-B2、IV-B2、V-A2/Table IV/Layer 3 把 ERC-8004 描述为 wallet transfer、spending caps/on-chain guardrails；[官方规范](https://eips.ethereum.org/EIPS/eip-8004)及[截至本窗前的目标文件历史稿](https://raw.githubusercontent.com/ethereum/ERCs/503591a6e80e6e1affdd6403341e25269141f046/ERCS/erc-8004.md)只定义 Identity/Reputation/Validation registries，明确 payments 正交。钱包关联不等资金授权。这只隔离依赖 ERC-8004 支付限额的保护行，不否定所有12风险向量或别的 custody 实现。2+2+2=6 规范保证纠错定点深入、窄争议暂缓 Books；重开需作者依据的精确扩展/独立 custody 守卫及 Table IV/Layer 3 修正，不要求全部 commerce 案例复现。详见[作者定点笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [DepCap: Adaptive Block-Wise Parallel Decoding for Efficient Diffusion LM Inference — 2604.15750v1](https://arxiv.org/html/2604.15750v1)

exact-v1 §4.2–4.4/Algorithm 1 用跨步预测 KL 与当前熵选择块边界，再用候选位置交叉 log-prob 检查冲突。中央反例在印刷第7–8行：先把所有置信≥阈值者一次加入 S，后续仅从剩余 C 删除冲突者，未检查 S 内部。两位置都以 .96 预测同一 token、阈值 .95、γ=−16 时二者均被选且冲突分数 2log(.96)>γ，违反所述返回 conflict-free 集合；不推断实现必然同错。单 A100 40GB、LLaDA/Dream 固定表的 TPS/NFE/accuracy 有效但并非所有质量格均胜，也不证明 production SLO。2+1+3=6 纠错定点深入、窄争议暂缓；重开只需高置信种子内部消冲突的同版算法/实现说明及受影响保证，保跨步条件信号和表。见[作者必要公式](../_sources/daily-20260420/v3-reopen-notes.md)。

### [MemEvoBench: Benchmarking Safety Risks from Memory Misevolution in LLM Agents — 2604.15774v1](https://arxiv.org/html/2604.15774v1)

exact-v1 §3–6 的 QA108/workflow83 在三轮把前轮 agent 回答追加到下轮可检索记忆，并以模拟赞许风险捷径的反馈改变后续行为。无偏反馈的 ASR 75.9→75.2→80.1 不是单调；偏置反馈 71.6→84.9→87.8 支持该构造场景的污染边界。QA 的 ModTool 同时给 web_search 和 correct_memory，workflow 只给后者，不能把差额唯一归因记忆编辑。judge 的50手标约96.2%仅校标签一致，非真实危害发生率。2+2+2=6 标准；[AGENT-MEMORY Ch77](../../../../books/part-07-agent/77-memory.md) 的失败经验源 episode、反馈写入、跨用户作用域及反馈不自动获事实/policy authority 已具体承载本命题，窄已有覆盖，不声称原章包含合成风险 taxonomy。参见[必要证据](../_sources/daily-20260420/v3-reopen-notes.md)。

### [From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation — 2604.15805v1](https://arxiv.org/html/2604.15805v1)

exact-v1 §III–IV 的 panorama→3DGS静态场景/collision mesh→提示生成 cousin，跨房间另用视觉特征、已知相机高度与 ICP 定尺度；可动物体和物理求解另增资产，不由照片真实感推交互动力学正确。SO101 示教原100→追加200 cousin不是等量训练；同100总量的50real+50twin在 Table III 的 .33/.35对100real .37/.35并不占优。三任务×四策略×四泛化级的 r=.91 不能证明单场景排序，navigation68%仍有32%失败。2+2+2=6 标准、仅报告 real-to-sim 数据支持分支；Ch26 的行动/真实环境回授责任不被模拟相关性替代，也不因此恢复暂缓的 AI for Science。原文界限见[作者笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [UsefulBench: Towards Decision-Useful Information as a Target for Information Retrieval — 2604.15827v1](https://arxiv.org/html/2604.15827v1)

exact-v1 §3–5 的1110 query-doc gold与53k full 文档把相关性和专业决策 usefulness 分标，21.9%的高相关条目仅部分可用，提示检索命中不等下游支持。标签来自有限三 analyst/15 reports/10行业，未标全文档当负例有 selection bias；排序分数 yhat×p(yhat)再 min-max 是启发式，不是事件风险概率。部分同源专家标注错误及专业知识模糊，LLM 排序未稳定胜过 BGE；缩短/去关键词并非都改善。2+1+2=5 标准、仅报告领域有限的评价反例；Ch76 已把检索结果、证据充分性和回答效果分账，不用新指标替换事实真值。具体分母见[作者笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [Beyond Text Prompts: Precise Concept Erasure through Text–Image Collaboration — 2604.15829v1](https://arxiv.org/html/2604.15829v1)

exact-v1 §3–4 将 prompt embedding 混合与合成视觉 latent 协同训练 erasure，并单独测相邻概念保留；这是仅文本名称擦除以外的局部分支。凸 embedding hull 不保证语义有效，Gaussian/LayerNorm 后亦可能出 hull；§3.3 对温度导致 uniform/sparse 的文字与 Eq3 相反，Appendix B.5 的方向才与式一致。A6000/SD1.5/每概念200合成图像的 Table 3 中 NoHVRL P4D0低于 full，NoCCCM FID30.41优于 full30.86，不能说全部模块/指标必要；shared-prompt 对照未匹配视觉输入和完整训练预算，也不证零残余擦除。2+2+2=6，保护效果边界定点深入、仅报告；不把有限合成评估提升为全语义/全安全保证，暂不改 Books。原文与反证见[作者笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution — 2604.15840v1](https://arxiv.org/html/2604.15840v1)

exact-v1 §3–4 从既往好/当前坏、mixed outcome、rare 轨迹信号提议新任务，explorer 收集 action-observation，再执行验证后入训练；不是每条失败都自动成为正确训练样本。§3.3 连“执行失败但环境给 positive reward”也可准入，故 reward 不等目标完成。Qwen3-4B Table 3 的 static/合成/随机探索/feedback 均值43.29/45.43/49.36与 A.3 消融支持局部路线，但任务数、训练 token、外部探索成本不全 matched；反馈耗时占9.67%/12.76%也不是免费。2+2+2=6 标准；[TRAIN-RLHF Ch31](../../../../books/part-04-training-system/31-rlhf.md)已具体写能力边界移动→verifier诊断→environment/interface proposal→独立 gate 更新任务/反馈分布及污染/holdout，窄已有覆盖，不称包含三类启发式或开放部署效果。见[必要证据](../_sources/daily-20260420/v3-reopen-notes.md)。

### [Hierarchical Codec Diffusion for Video-to-Speech Generation — 2604.15923v1](https://arxiv.org/html/2604.15923v1)

exact-v1 §4–5 用12层 RVQ，低层1–2由唇形/身份条件，高层3–12由表情代理条件和双尺度规范化，构成 codec 层级与生成条件分责；分层不证明语义完全解耦。训练时曾用真实音频 identity/emotion 而推理改用视觉，不能称全流程 vision-only 或无 train-test gap。LRS2 WER39.99劣于 FTV38.09，LRS3 UTMOS3.84和 SpkSim.5678也有对手更优；去 dual AdaLN 的 UTMOS3.92反高于 full3.84，有限 MOS 不支持模块唯一因果。2+2+2=6 标准、仅报告受限语音层级方案；Ch24生成节奏与 Ch23表示身份仍按原责任链，不采普遍身份/情感可控保证。见[原文评价](../_sources/daily-20260420/v3-reopen-notes.md)。

### [VADF: Vision-Adaptive Diffusion Policy Framework for Efficient Robotic Manipulation — 2604.15938v1](https://arxiv.org/html/2604.15938v1)

exact-v1 §4–5 的视觉阶段决定 denoise 步数与 action horizon、轨迹重采样是具体计算分配分支；但 Eq7 以 q=w/Z 直接抽样所得 MSE 期望为 sum(wℓ)/Z，Eq4 的 uniform-weighted 目标为 sum(wℓ)/T。取 w=(1,3)、loss=(1,2)，二者3.5与1.75；任意 learned π 若无 importance 校正也不再保同目标。Algorithm 1 用负 standardized loss 更新权重，Eq8却以正 loss 优先 hard：loss1/3 时 hard 权重0、easy2，方向相反。此只隔离打印无偏/hard-mining保证，不否定实测；Table 3 每步159.4/64.8与全轨7968/1199不能混分母，2.46×不是同一 DDIM 单独加速，真实机器人500Hz控制率也不等15.4Hz策略率。2+2+2=6 纠错定点深入、窄争议暂缓；重开需归一/importance 校正与符号-实现一致说明。见[作者公式审阅](../_sources/daily-20260420/v3-reopen-notes.md)。

### [CIMple: Standard-cell SRAM-based CIM with LUT-based split softmax for attention acceleration — 2604.15944v1](https://arxiv.org/html/2604.15944v1)

exact-v1 §IV–VI 的 dual-bank 8-bit SRAM CIM、32位累积再量化、移位 exp LUT 和 split softmax 把 MAC 与非线性近存映射在一起；数学恒等变换不保证有限 LUT 全精度。26.1 TOPS/W 是0.85V/417MHz post-synthesis，2.31 TOPS/mm²为1.2V/770MHz post-layout，不能并成同一硅片实测点；约48.4% global power不可删。33%延迟仅 encoder1024/head64/400MHz 与32-bit nonsplit LUT 对比；TinyLlama PyTorch 精度实验又未在实际 CIM 执行整模型，作者承认片上装不下完整模型、外存或主导。2+2+2=6 标准、仅报告近存 softmax 映射分支及容量边界，不将局部电路估计写成普适 LLM serving SLO。见[必要表与反证](../_sources/daily-20260420/v3-reopen-notes.md)。

### [From Competition to Coopetition: Coopetitive Training-Free Image Editing Based on Text Guidance — 2604.15948v1](https://arxiv.org/html/2604.15948v1)

exact-v1 §III/Algorithms 1–2 的双分支 attention 差分、dual entropy、mask 与 latent refinement 是具体保留/编辑协同机制。中央有限性反例：Eq10 的 ReLU(A_s−A_e) 可为0，如 .2−.3，Eq11 的正系数乘 log0 没给有限定义；Eq16 std(h_d)=0、Eq19 norm(h_d)=0 也未给处理。已核 MathML 中 Algorithm 2 实为 1−A，不沿提取误读制造另一个反例；Eq18 梯度未乘 mask，不能自动保证所有背景逐步不变。Table III 去 spatial/temporal 后编辑 CLIP 指标25.82/25.41反高于 full24.60，保有限 fidelity/editing trade-off。2+1+3=6 纠错定点深入、窄争议暂缓；仅需 clamp/epsilon、零方差/零范数及 mask 范围的可核实现说明重开，不要求全 PIEBench 复现。见[必要公式笔记](../_sources/daily-20260420/v3-reopen-notes.md)。

### [A Case Study on the Impact of Anonymization Along the RAG Pipeline — 2604.15958v1](https://arxiv.org/html/2604.15958v1)

exact-v1 §2–3 的 PRE 先匿名原文再嵌入/生成，POST 在原文进 embedding/API 后才匿名答案，后者输出 PII 少也不证明上游无暴露。800文档、metadata锁定单doc/top2/每doc≤2chunk，不是真实全库 recall 控制；Presidio 与三 DP 方法的 ε 单位各异，不能横向合为统一预算。Table 5 BBC 删除 PRE privacy8优于 POST23而 POST ROUGE-L .93>.47，TAB 另有相反方向及 PPL 代价。所印 TO=(1−J/100)/(1−mean(RL,CS)) 为比值，TO>0 不等 privacy gain 超过 quality loss；judge/ROUGE 亦非攻击或独立 gold。2+1+2=5 标准、仅报告放置点与质量/暴露面取舍，Ch72与Ch76的发布/检索责任不改，不采端到端匿名最优。见[作者表格核](../_sources/daily-20260420/v3-reopen-notes.md)。

### [TwoHamsters: Benchmarking Multi-Concept Compositional Unsafety in Text-to-Image Models — 2604.15967v1](https://arxiv.org/html/2604.15967v1)

精确 v1 §3–4 以51个安全原子概念对构造组合不安全样本，区分原子、组合、untargeted utility 三个验收对象；这是数据构造和有限防线测试，不是潜在概念独立定律。17.5k筛选后样本、500 ID/500 unseen-pair OOD 的三专家与代理 judge 只支持该 ontology；300k混合训练对零样本基线不隔离纯数据量。Table 2 FLUX MDR .48/SCR99.56不能转生产事故率，Table 3 文本过滤有较高 recall，有限 erasure 四概念对与 Table 4 反向格不支持所有擦除都失败；attention热图不识别内部因果。2+2+2=6，因保护组合边界深入，仅报告原子合规不推出组合合规的受限反例；不将社会策略 taxonomy 或未实现的 P(A|B) 防线写 Books。见[精确v1审阅](../_sources/daily-20260420/v3-reopen-notes.md)，不回拨后版题名。

### [AEGIS: Anchor-Enforced Gradient Isolation for Knowledge-Preserving Vision-Language-Action Fine-Tuning — 2604.16067v1](https://arxiv.org/html/2604.16067v1)

exact-v1 §3–7 用旧 VQA activation 的 Gaussian anchor 与 flow expert 分取两个梯度，冲突时减去 anchor 投影；在不回放旧原始任务数据下有局部替代意义，额外 backward 约增40% wallclock。其 Eq12/Algorithm 1 的 α=d/(||g_ot||²+ε) 且 ε>0；当 d<0，Eq13 更新后的点积为 dε/(||g_ot||²+ε)<0，不等 Eq14 宣称严格0，依赖的精确 Pythagoras/零破坏保证不能直接成立。OK-VQA 基线60.15与方法60.23的微差也未隔离全部质量/动作头因素；只保有限 VQA/专家误差观察，不推真实机器人安全。2+1+3=6 纠错定点深入、窄争议暂缓；重开需 ε 修正的不等式/零范数分支、实际实现与严格几何保证的同版说明，不要求全 VLA 复现。见[作者公式证据](../_sources/daily-20260420/v3-reopen-notes.md)。

### [JumpLoRA: Sparse Adapters for Continual Learning in Large Language Models — 2604.16171v1](https://arxiv.org/html/2604.16171v1)

exact-v1 §2–3/Algorithm 1、§4.1–4.6/Tables 1–3：rehearsal-free 且推理不知 task ID 时，逐任务低秩 `AB` 先形成原矩阵形状的更新，再以可学习 JumpReLU 阈值筛选坐标支持并合入 shared base；它不同于预定稀疏率、始终存每任务 adapter，且 threshold 后的更新不一定低秩。零初始化需先约20%训练步 warm start，阈值梯度依赖 STE；训练状态与总计算不能仅由 adapter 参数数推断。作者 T5-770M、两组分类任务各三次 seed 的 Table 1 显示 IncLoRA 上明显改善、ELLA 上较小改善，但 Table 2 的 SC BWT 从 ELLA −0.5 退到 JumpLoRA+ELLA −1.9，LS 则 −4.8→−4.5；稀疏重叠小不是功能独立证明，超出所测任务序列的遗忘/成本保证未建立。故 2+1+2=5 标准仅报告条件化更新支持分支；Ch30 已区分 rank、target modules 与 artifact，本文不足以写成普遍可替代设计，Ch35 的完整状态回滚责任不变。[逆向自纠与原笔记](../_sources/daily-20260420/V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)保留此从前关闭恢复的理由，仍待整日非作者 Gate。

### [Adapting in the Dark: Efficient and Stable Test-Time Adaptation for Black-Box Models — 2604.15609v1](https://arxiv.org/html/2604.15609v1)

exact-v1 §3.1–3.4/§4.1–4.2、Tables 2/6/8：仅远端 API 可返回完整 probability vector 时，以本地可微 steering model 与远端输出融合训练输入 prompt，每样本只需一次远端调用；对远端分支 stop-gradient 只是代理方向，不是远端真实梯度。随机 prompt 直接学会坍缩，可靠样本过滤与 clean→prompted KL 给有限稳定条件；不能由叠加优势断言两者单独在所有任务必要。ViT-B/16 ImageNet-C 的 BETA 62.6 高于黑盒 ZOO，但白盒 ETA 65.8 更高，访问条件并不相同。单 RTX3090 的 Table 6 中本地额外资源与约45→48ms仅属于该 API/负载；商业 API 的调用预算对照也不能外推通用闭源语言服务。2+1+2=5 标准仅报告这一访问权限与调用成本下的替代分支；Ch23表示与 Ch62接口责任不因此改变，非 label-only/top-k、真实梯度或生产 SLO 保证。[作者自纠](../_sources/daily-20260420/V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)仍待日级独立 Gate。

### [Aligning What Vision-Language Models See and Perceive with Adaptive Information Flow — 2604.15809v1](https://arxiv.org/html/2604.15809v1)

exact-v1 §3.2–3.3/§4.1–4.3、Tables 7–8：先做额外一轮解码取得跨层视觉 attention 统计，用熵排序决定遮蔽部分文本 query→视觉 key 的连接，视觉 token/state 本身仍保留，与直接删 token、压缩 KV 不是同一执行选择。oracle 人工多 mask 选到正确答案只是上界，不是部署策略；同 mask ratio 的随机或低熵遮挡劣于本法，支持所测模型任务的局部排序，而非 attention 是唯一视觉因果。future-aware 全连通反退、间接提示仍失败，且未披露完整硬件/precision/batch/端到端并发 SLO；额外 decoding 不免费。2+1+2=5 标准仅报告该 white-box VLM 信息流分支；实际 Ch23 已要求保视觉证据身份、区分删 token 与后续读取及真实输出验收，本文尚不要求新增长期正文。[作者自纠](../_sources/daily-20260420/V3_ONLY_REVERSE_ADMISSION_AUTHOR.md)仍待整日非作者 Gate。

### [Aletheia: Gradient-Guided Layer Selection for Efficient LoRA Fine-Tuning Across Architectures — 2604.15351v1](https://arxiv.org/html/2604.15351v1)

exact-v1 §3.2–3.5/§4.5–4.6/§5.5–6：先短梯度画像，再只给选中的层加固定 rank16 LoRA，区别于 Ch30 现有轮流更新原参数层；跨模型主实验不能与单个 Qwen3B 的非对称 rank 支线混算。200-step 与 equal-wall-clock 250-step 分母不同，后者 eval loss 反退；缺同层数 random/depth 对照，不能把收益唯一归因于梯度排序，冻结 base 的 forward/backward 也不会免费消失。`2+1+2=5` 标准，仅报告训练更新支持集与计算取舍，不写通用加速；[apr01必要源→实际 Ch30 核](../_sources/daily-20260420/V3_APR01_SIX_ONLY_EVIDENCE_INDEPENDENT.md)与[root 逆向准入纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)均限此命题。

### [Weak-to-Strong Knowledge Distillation Accelerates Visual Learning — 2604.15451v1](https://arxiv.org/html/2604.15451v1)

exact-v1 §3/§4.3/§5 Table3/§6：已有的适度弱 frozen teacher 仅在早期 warmup–hold–decay 参与，student 连续两次 validation 超越 teacher 后停 KD，是有条件的 teacher gap × active lifetime 选择；Ch29 已有容量差和阶段质量验收，但没有把这项具体停止规则写作一般定律。极弱 teacher 与过强 teacher 反退，first-at-target 为 epoch/step，未计完整 teacher 构建与 active forward，不能把 4.75× 当净 wall-clock 或 LLM 训练收益。`2+1+2=5` 标准，仅报告受限视觉训练分支；[apr01必要源与 owner 核](../_sources/daily-20260420/V3_APR01_SIX_ONLY_EVIDENCE_INDEPENDENT.md)和[root 逆向准入纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)不构成日级 Gate。

### [Flexible Empowerment at Reasoning with Extended Best-of-N Sampling — 2604.15614v1](https://arxiv.org/html/2604.15614v1)

exact-v1 §3.1–3.2/Eqs16–19/§4 Table2：固定 N 候选下，以 entmax α 调尾部/零支持、非负目标 J 的样本均值倒数调状态内尺度，构成 embodied policy 的局部选择分支，不是 Ch20 原有候选覆盖/选择/成本分账的同一算法。额外 transition/marginal model、SAC off-policy 与近似归一均付成本；全 J=0 时印刷 β 无定义，三项 locomotion 并非全最优，固定 N 不等端到端固定 compute。`2+1+2=5` 标准，仅报告，不迁作 LLM 默认解码；[apr01必要源/owner 核](../_sources/daily-20260420/V3_APR01_SIX_ONLY_EVIDENCE_INDEPENDENT.md)与[root 准入纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)保留受限边界。

### [Prototype-Grounded Concept Models for Verifiable Concept Alignment — 2604.16076v1](https://arxiv.org/html/2604.16076v1)

exact-v1 §3.3–3.4/§4.2–4.3/Table4：part segmentation→视觉 prototype→concept decoder→concept-only task 给 Ch23 表示接口之外的可显示/可编辑具体分支；但 segmenter 已消费全图，不能从下游只用 part feature 推整条系统无外部像素影响，更不能把原型语义当独立人类/因果真值。CelebA 的 concept/task 指标低于 CBM，coupled intervention 也有反向，三 seed 不证明普遍可靠。`2+1+2=5` 标准，仅报告概念表示条件；[apr01源→Ch23 核](../_sources/daily-20260420/V3_APR01_SIX_ONLY_EVIDENCE_INDEPENDENT.md)和[root 逆向纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)不触发 Books。

### [Towards Robust Endogenous Reasoning: Unifying Drift Adaptation in Non-Stationary Tuning — 2604.15705v1](https://arxiv.org/html/2604.15705v1)

exact-v1 III-B–E/Eqs2–9、IV-A/TableII、IV-D/Fig7：CPO++ 用概念图文字替换、视觉近邻负例与逆匹配过滤构造多模态偏好数据，提出 Ch29/31 的训练支持集局部替代选择。SCM 的潜在 D 与固定 D 的 do 没有识别证据，Fig7 两单分支和联合消融不证明严格正交或理论上界；医学、驾驶分数也非安全部署凭证。`2+1+2=5` 标准，仅报告该受限数据构造，不吸收作者强因果叙述；[apr01必要源/owner 核](../_sources/daily-20260420/V3_APR01_CPO_NAG_DISPOSITIONS.md)及[root 逆向纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)已把证据限制与候选准入分开。

### [Target-Oriented Pretraining Data Selection via Neuron-Activated Graph — 2604.15706v1](https://arxiv.org/html/2604.15706v1)

exact-v1 §2.1–2.3/§3 Tables1–2/A.3/B.1/F.2/J：列置零的局部输出差作 activation proxy，再按跨层 Top-K 重叠筛目标数据，改变 Ch27 的预训练数据选择代理而非证明唯一功能骨架。A.3 包含 MMLU validation，五次 random 方差不是 NAG 自身多次运行 CI，两个 MMLU 分支反退；约192 GPUh 特征提取不能藏于复用目标之下。`2+1+2=5` 标准，仅报告受限 selector，保持 held-out 训练验收；[apr01源/owner 核](../_sources/daily-20260420/V3_APR01_CPO_NAG_DISPOSITIONS.md)和[root 逆向准入纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)不预支全面更好。

### [The Amazing Stability of Flow Matching — 2604.16079v1](https://arxiv.org/html/2604.16079v1)

exact-v1 §2–3 稳定性与 pruning 对照：同 seed 生成输出 ArcFace 接近，但内部 vector field 不同；高 loss 50% 删数的 FID33.92 差于低 loss23.49与 balanced cluster22.80，构成“映射近似即可无损剪枝”在所测条件下的负例。disjoint/异构/换同域数据相似度下降、共用 VAE 与人脸域限制外推，pair SD 不是跨训练 seed 的 CI。`2+1+2=5` 标准，仅报告 Ch27 选择代理/held-out 验收的受限反证，不新增通用删数算法；[root 原必要源核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)与[逆向准入纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)均不等日级 Gate。

### [Motion-Adapter: A Diffusion Model Adapter for Text-to-Motion Generation of Compound Actions — 2604.16135v1](https://arxiv.org/html/2604.16135v1)

exact-v1 §IV-E/TableII、§IV-G/TableIV：结构 mask 与 late fusion 给文本到复合动作生成的局部替代接口，接 Ch24/26 的生成表示而非真实动作闭环。484 benchmark motions 进入2652 evaluator 数据，80/10/10 split 未说明与训练是否 disjoint；MotionDiffuse base 只低于 MDM base，仍高于自身 adapter，不能混基线比较，transition 指标也并非全反退。`2+2+2=6` 标准，仅报告受限生成/组合，不写物理控制或整体 training-free 保证；[root 必要源核](../_sources/daily-20260420/V3_ROOT_FINITE_INDEPENDENT.md)和[逆向准入纠错](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)仅覆盖此有限范围。

### [C-Mining: Unsupervised Discovery of Seeds for Cultural Data Synthesis via Geometric Misalignment — 2604.15675v1](https://arxiv.org/html/2604.15675v1)

exact-v1 §3.1–3.4／§4.1–4.5／Tables 1、3、4、6：冻结多语编码器的低密度、跨语聚簇种子改变了合成指令前的选择代理；固定 Qwen3-32B 下 Random／Monolingual／Full 的 CB-H 为43.31／44.83／46.98，BLEnD为81.13／83.38／85.81，随机种子相对 Base 还反退。它只在该合成流水线提供受限替代，不证明几何错位是文化真值或唯一因果；Eq2余弦归一的非负/零分母条件未说明，Table1 77.12→80.94是3.82pp而非文字3.13，Table6采矿成本不等完整合成/训练成本。`2+1+2=5` 标准仅报告；实际 Ch27 已承载选择目标、数据来源和teacher权限，不增写Books。[apr02必要证据核](../_sources/daily-20260420/V3_APR02_THREE_METHOD_DISPOSITIONS.md)与[root本次逆向准入纠错](../_sources/daily-20260420/V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)均只在此有限范围有效。

### [SAGE: Selective Attention-Guided Extraction for Token-Efficient Document Indexing — 2604.15583v1](https://arxiv.org/html/2604.15583v1)

exact-v1 §3.1–3.3／§4.1–4.8：小型本地attention model按chunk和query逐次前向，对归一、差分后的query→document attention选连续窗口；同一文档多query可复用KV，不是全篇一次免费prefill。QuALITY-hard 10% token budget 的局部质量与3797 queries／3011 cache hits／690.9s并存；UAE 98.2s、Qwen3 embedding 370.7s是不同索引/缓存账本，不能据此断言端到端更快。repetitive ZIP预算增大还反退，attention与命中证据不等真值。`2+1+2=5` 标准仅报告：多query且本地prefill可摊时，Ch76的输入选择多一条成本转移分支；单query/频繁变更下可能不值，现有Ch76预算与证据责任无需改写。原[作者必要审阅](../_sources/daily-20260420/v3-reopen-notes.md)与[root逆向纠错](../_sources/daily-20260420/V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)不等整日Gate。

### [Skill-RAG: Failure-State-Aware Retrieval Augmentation via Hidden-State Probing and Skill Routing — 2604.15771v1](https://arxiv.org/html/2604.15771v1)

exact-v1 §3.1–3.3／§4.1–4.4／Table1：hidden-state prober先判是否重检索，失败后router再以reasoning、answer和evidence选rewrite/decompose/focus/exit，区别于无条件加top-k。固定Gemma2-9B/BM25/4-shot，OOD MuSiQue、2Wiki ACC相对Probing-RAG由13.9→20.0、38.9→52.5，但Hotpot EM24.2低于DRAGIN35.6；probe训练用gold标签，未隔离每个skill对更强等预算无probe路由的独立收益，t-SNE簇亦非失败因果识别，额外模型/调用成本未形成生产SLO。`2+1+2=5` 标准仅报告失败条件化动作选择；Ch76已有sufficiency→重查/拆解/停止责任，不把探针视为事实authority或新通用自动修复保证。[作者必要审阅](../_sources/daily-20260420/v3-reopen-notes.md)与[root定点独立核](../_sources/daily-20260420/V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)未替日级复核。

### [Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding Pipelines — 2604.15376v1](https://arxiv.org/html/2604.15376v1)

exact-v1 §3.2 的两次 crop 与坐标映射只在目标仍位于二次裁剪区、第二次定位正确时，才让第二次预测到 crop 中心的距离成为首次误差的代理；它是已完成两步定位后的一个受限风险传感器，不是免费额外模型调用或校准的事实概率。§5.3 跨模型路由 80.9% 对 80.1%，McNemar `p=.19`，且需要另一模型，不能称稳健提升。`2+1+2=5`，标准、仅报告；Ch23 的表示/裁剪证据与 Ch66 的传感器/最终验收已有分权，尚无应改写的长期结论。原前关闭理由被[root独立逆向核](../_sources/daily-20260420/V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)纠正；该单篇核不替代整日 Gate。

### [RAGognizer: Hallucination-Aware Fine-Tuning via Detection Head Integration — 2604.15945v1](https://arxiv.org/html/2604.15945v1)

exact-v1 §3.2–3.3/Fig.3 的检测 loss 通过 hidden state 反向更新 LoRA adapter，区别于冻结表征后训练检测 probe，因此属于真实训练目标分支。§4.1–4.2 的结果限作者模型、数据与标注；Text FT 使用 golden answer，联合训练使用带标签的生成回答样本，并非只改变 BCE 的严格配对消融。Llama2 的语言质量/相关性反退，NoCtx 69.26 低于 HallucinationProbes 72.29；数据切分、judge 与生产校准不足以把内部检测值当事实真值。`2+1+2=5`，标准、仅报告；Ch29 已说明训练目标分支，Ch66 已分开模型信号与外部证据/发布权，没有必要据此新增通用保证。原前关闭理由经[root独立逆向核](../_sources/daily-20260420/V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)纠正。

## 5. 缺口与下一步

**本窗无可执行待办；外部保留项见下：**150份唯一完整题摘已逐项作贡献判断；§3–4的111项候选＝26项真实 Books 整合、13项具体已有覆盖、54项仅报告、18项中央窄争议；38项具名前关闭，另1项首公开身份隔离，`111+38+1=150`。此数由原127项候选的反向准入、作者纠错、[十一项冲突的非作者逆向核](../_sources/daily-20260420/V3_ROOT_ELEVEN_REVERSE_ADMISSION_AUDIT.md)及[最后两项独立负侧纠错](../_sources/daily-20260420/V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)得出，不是按比例缩池。27项有限同行核已逐项完成；最终来源/日期、正负样本与 Books 已获[非作者整日 Gate](../_sources/daily-20260420/V3_ROOT_DAILY_GATE_20260420.md)。下文提及109/40/1、19项待核等数字是纠偏过程快照，不代表当前状态；保留其证据与反例，不让旧待办覆盖现行检查点。

**终态保留项与定点重开条件：**OpenAI 注册Research的历史分页、Google Publications的日级目录、Meta Research的可读逐条日期，本轮入口与有界替代目录均已检查到§2所述停止点；三者属于每日必查入口，按合同标“受阻”而不是仅供补检使用的“检索受限”。这些缺口**不支持正面证据、Books 采用或无遗漏断言**，也不支持机构全站本窗零发表；本日确定候选来自另有官方原文与联合日期链的具名家族。若相应官方历史页可读且出现具体本窗材料，只重开受影响来源/家族，不扩扫无关年度或 Weekly。Seed AgentWorld 虽有 CMS 卡片日值却无当时正文公开证明，15483 虽有本批 arXiv 版本但同 family 官方早发线索未排除，二者维持具名身份隔离、不评分不写 Books；可核当时正文/公告或先前家族首次公开材料返回后只重开真实日期。本段之后的过程记录只是纠偏历史，不产生当前普通待办。

旧25与额外125已按精确ID核为150唯一完整题摘，旧V2.1 selected/通用Existing均未继承。26处正文均已获真实非书稿作者写后核；另13项Existing有具体 owner 命题。反向审计没有移动此前已通过整合，也没有删除任何原始必要证据。七项恢复已有非作者逆向准入核，整日 Gate 尚未签署。

逐 ID 对账见[否定侧账](../_sources/daily-20260420/V3_NEGATIVE_SIDE_SCREEN_LEDGER.md)及其最新纠偏：原正式127中净16项改具名前关闭，现拟冻结111、具名前关闭38、首公开身份隔离15483一项。正侧不得因Books不变而误拒，负侧不得因论文有局部新算法就自动准入。16054、15660、16198、15663、15549及后续反向纠错均保留具体条件；单篇样本通过不扩成全日或全网无遗漏保证。

九项旧有限同行Only与作者前关闭意见冲突，加上15521/15621两项关闭理由挑战，已由本日作者[逐项裁决](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)并获[root逐项非作者逆向核](../_sources/daily-20260420/V3_ROOT_ELEVEN_REVERSE_ADMISSION_AUDIT.md)：恢复七项受限标准Only，维持15657/15802/15972/15756四项具体关闭。旧事实与反证未删；这十一项准入核不自动代表整日来源/日期 Gate。

**已收口的普通工作：**150份完整题摘及111个候选的必要单篇处置均已有正文，普通题摘未读或已获准却未落实的 Books 写入为零。原[去重27项单篇独立Evidence→实际owner核](../_sources/daily-20260420/V3_FINAL_39_FINITE_ROUTING.md)已由具名有限记录逐项收口；十一项负侧冲突也经[root非作者逆向核](../_sources/daily-20260420/V3_ROOT_ELEVEN_REVERSE_ADMISSION_AUDIT.md)通过。38项负侧有[作者分层定点抽样](../_sources/daily-20260420/V3_AUTHOR_SOURCE_DATE_NEGATIVE_AUDIT.md)、[root 独立有限核](../_sources/daily-20260420/V3_ROOT_NEGATIVE_SIDE_FINITE.md)及末次纠偏；[整日复核](../_sources/daily-20260420/V3_ROOT_DAILY_GATE_20260420.md)明确这些是分层抽查而非38项逐篇独立全文核。外部来源、争议和日期隔离不支持正面结论，但不再伪装成普通未完成工作。

16090 AW-PSP 的[作者源→Ch36 最窄提案](../_sources/daily-20260420/V3_AWPSP_CH36_OWNER_PROPOSAL.md)指出现有单 worker 到场频率校正尚未明说共同故障与非 IID 标签支持相关时的单轮缺失类边界。root 已按该命题获得共享锁并实际写入 Ch36，[apr01 已据官方必要源顺读真实正文、相邻交接与章末 Review 并通过非书稿作者写后核](../_sources/daily-20260420/V3_APR01_AWPSP_CH36_WRITE_AFTER_INDEPENDENT.md)，现计真实整合；此单篇通过不代表来源、日期、候选分母或整日 Gate。

**外部保留：**Meta Research 首页历史行、Moonshot 注册 Blog 以外的机构入口、Google Publications 日级首公开、MiMo 站外事件、MiniMax AgentTechBlog 历史字段、OpenAI Research 历史分页均不支持机构全域零发布或全网无遗漏。Meta Publications 第2页、Kimi 注册 Blog、MiMo 相邻官方正文的本窗可见停点已分别复查，限度见§2及[窄复查](../_sources/daily-20260420/V3_THREE_SOURCE_STOPPOINT_REOPEN.md)；不能再把 MiMo Blog 一概写为“无日期”，也不能由这些局部停点推成全部入口完成。若要扩张覆盖断言，须取得对应官方历史目录/存档/当窗原始发布，只定点重开，不扩全年。Seed AgentWorld/2604.18292的CMS PublishDate=Apr19 16Z、后arXiv Submitted=Apr20 14:01:10Z不证明截点前正文已公开；需当时带时间正文release、官方存档或完全落窗公开区间。此前不入候选/Books。目录限制不掩盖上述仍可执行的同行与日级审核。

**15483 π0.7 首公开身份：**潜在contextconditioning/success-failure/subgoal贡献保留，不因机器人关闭。[PI 官方博客目录](https://www.pi.website/blog)当前可见π0.7的April 16卡片；[同篇官方文章](https://www.pi.website/blog/pi07)的搜索提取显示Published April16、机制正文与同题paper链接，但正文直开403/curl为Vercel checkpoint，不能核论文链接在该日是否已存在，也不能用submitted Apr16或现时索引孤证论文首公开。因此不先计确定Apr20候选/Books。恢复该官方Published字段与同一论文正文链接的可靠历史存档或首公开公告后，只重开真实归属日；不扩PI每周扫描。当前为具名本窗日期安全隔离，不是普通未读改称blocked。

**中央主张有限争议保留：**15726的可用必要主文/AppendixA/B已审；不采用其matched-budget量化与latent necessity/patch-specificity保证，其他有效协议和三模型表仍保留。可接受重开材料是预算校准权重/容差、数据split数量与实际arm/sham干预配置，或作者具体Supplement/artifact链接中可核同一条件；只重开§4这一项，不要求所有附件或复现实验。其他普通未读不能移入此终态。

15350只隔离perfect答前及普适α方向保证，geometry定义、阶段/架构表与OOD退步有效保留；所见必要主文/B/E已审。重开材料为feature在generation前/中哪个时刻可用、α方向不一致澄清、最优layer/phase选择与held-out协议的可核补充/更正；此前不据它宣称质量预测/发布保证，也不扩大成所有模型/全部诊断失效。

## 6. 复核

复核者：root（非日报作者，来源/日期/负侧及整日日级 Gate）；apr01（首批九项准入校准、旧八具名准入、有限证据及 root 所写 Ch36 AW-PSP 真实写后）；apr02（具名必要源→owner及有限处置）；apr20_resume（仅对 root 所写 Ch31 15557 作非书稿作者实际写后核，不是本日报日级复核者）

结论：通过

范围、样本选择和外部保留边界见[非作者日级 Gate](../_sources/daily-20260420/V3_ROOT_DAILY_GATE_20260420.md)。以下历史段落记录复核如何发现并纠正错误，凡“仍待”“19项”“109/40/1”等只代表当时快照，不覆盖当前终态。

[九项校准](../_sources/daily-20260420/V3_APR01_NINE_ADMISSION_CALIBRATION.md)确认五项继续、四项具体关闭，仅有界准入口径，不是150项证据或整日Gate。作者apr20_resume；二十六项必要原文与真实正文已对应非书稿作者写后核并通过。当前111项§3/§4逐项对应，最后两项误拒已有[root必要原文核](../_sources/daily-20260420/V3_ROOT_NEGATIVE_REVERSE_AUDIT_15376_15945.md)，16004/16007的窄处置另有[非作者源→owner记录](../_sources/daily-20260420/V3_ROOT_16004_16007_INDEPENDENT.md)。日期边界和剩余正反样本仍待最终日级验收。旧V2.1已完整归档但不继承；未以机器校验替代语义完成。未stage、commit、push。

[root 六项否定侧独立分层抽核](../_sources/daily-20260420/V3_ROOT_NEGATIVE_SIDE_FINITE.md)实际重读 15475/16088 的一般系统范围、15343/15911 的安全个案与综述、16070/16108 的成熟应用题摘，逐项维持具体前关闭；它与 apr01 的 15623/15877/15671/16114 具名核互补，不等于全部 22 前闭逐篇 PASS、无漏收或日级 Gate。15849 本次独立直链失败未冒称核过，作者已重读官方完整题摘且维持具体前闭，但非作者未单项核。15549 因 root 另行实际读 exact-v1 摘要/§1.2 与 Ch36:65–81，确认有向 SGP mixing 加无线冲突时隙的联合训练选择，原“缺大模型/状态”硬门槛撤销；作者复核必要 §2/4/6 与联合日期链后已正式作5分标准仅报告，不扩为通用训练加速。

先前非作者样本覆盖原22前关闭中的10项，按一般系统/领域应用、成熟组件迁用、综述/安全个案及暂缓范围分层，并促成15549/16054/15660/16198/15663误拒修复。逆向初步新增39项前关闭，作者自纠三项后为36项；root 对此前被独立证据核准却移出的八项逐项[重判恢复](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)，后续对15675/15583/15771作[定点纠错](../_sources/daily-20260420/V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)，本次作者对十一项冲突再恢复七项，故净新18项、当前作者工作态40前闭。此前10项 PASS 不能挪作余下新关闭的核验。root 已对新闭15701/15859、[15648/16056](../_sources/daily-20260420/V3_ROOT_15648_16056_REVERSE_ADMISSION.md)及保留16027/16146/15958作具名有限抽核，结论仅及这些样本，不等于净新18项或所有保留项全数通过；发现系统性错误只扩受影响理由层。447宽标题浏览和上述样本均不证明全网召回。

按[同行覆盖续派](../_sources/daily-20260420/V3_FINAL_39_FINITE_ROUTING.md)逐项核对正式§4与独立记录后，原31项单篇 Evidence→实际 owner 具名定位中，root 已对[15384/15408/15490](../_sources/daily-20260420/V3_ROOT_THREE_15384_15408_15490_INDEPENDENT.md)有限核通过，15557另作 Ch31 实写并获非书稿作者写后核；此后 root 又对[15350/16009](../_sources/daily-20260420/V3_ROOT_TWO_15350_16009_INDEPENDENT.md)、[15750/15764](../_sources/daily-20260420/V3_ROOT_TWO_15750_15764_INDEPENDENT.md)、[15780/16067](../_sources/daily-20260420/V3_ROOT_TWO_15780_16067_INDEPENDENT.md)及[15789/15726](../_sources/daily-20260420/V3_ROOT_TWO_15789_15726_INDEPENDENT.md)定点核通过，当前仍有19项待具名单篇结果；`15789 15726 15702 15367 15840` 是第二轮纠错补列。路由不算 PASS，作者正文“认可方向”也不能代替实际有限核；只复用未变原文和必要反证，不扩全附件或宽库存。

root 另对[三个机构入口的修正停点](../_sources/daily-20260420/V3_THREE_SOURCE_STOPPOINT_REOPEN.md)实际重新打开 Meta Publications p2 与 MiMo 首页/相邻正文，确认可见目录内的跨窗日期及保留限制；Kimi Blog 本轮非作者工具未稳定抽出全文，因此只接受作者记录的注册入口可见停点、不据此扩写机构零发布。此为 Meta/Kimi/MiMo 三行的**有限 Coverage 核**，不是十四来源、arXiv 候选分母或整日 Coverage Gate。原37项的[原始身份/日期字段分组](../_sources/daily-20260420/V3_REMAINING_37_DATE_BATCH.md)也只是作者准备材料，尚须最终非作者日期链审查。

root 已把 15351/15451/15614/16076、15705/15706、16079/16135 从作者前闭逐项恢复为标准仅报告，依据见[八项独立裁决](../_sources/daily-20260420/V3_ROOT_EIGHT_REVERSE_ADMISSION_ADJUDICATION.md)；15675/15583/15771另经[三项纠错](../_sources/daily-20260420/V3_ROOT_THREE_REVERSE_ADMISSION_15675_15583_15771.md)恢复。本次作者又按[十一项冲突表](../_sources/daily-20260420/V3_NEGATIVE_11_AUTHOR_ADJUDICATION.md)恢复七项、维持四项具体关闭。旧证据反证仍保留，不能把原作者关闭表当最终结论。余下40项按来源、主题和关闭理由分层抽检，并以16027/16146/15958等保留项对照；本次[作者定点来源/日期/负侧审校](../_sources/daily-20260420/V3_AUTHOR_SOURCE_DATE_NEGATIVE_AUDIT.md)亦仅证明明列样本，不把这些恢复或先前样本说成全量验证。候选来源和日期同时核十四每日入口、实际触发的 PI/Seed 身份事件及[公告/OAI/相邻批次联合链](../_sources/daily-20260420/V3_DATE_RECONCILIATION.md)，不把 Research 历史目录缺口写成机构零发布。独立日级结果出来前本日仍为 `未通过`。

apr01另实际读三项必要源并通过有限处置：15671化学实验组合属于当前暂缓AIforScience、16114成熟条件/learned reward迁到局部tone任务具体前分母关闭，15461为5分标准仅报告；不是所有范围外/否定侧抽检或整日Gate。旧八项有界准入亦已完成，六项继续与15623/15877两项具体关闭，后续六项作者已补必要Evidence与Books判断，仍待日级非作者复核，不把准入审核冒充整日核验。

apr01此前对15705/15706的必要方法、对照与 owner 作过有限证据核；root 随后发现作者把“未证明普遍收益”误作无具体训练选择，将两项连同另六项恢复为受限标准仅报告。原反证、成本及安全边界继续保留；这次具名纠错仍不替代其余候选或日级独立 Gate。
