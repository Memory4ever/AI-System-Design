# Daily Research — 2026-09-01

**规范：** V3
**窗口：** 2026-08-31T09:00:00+08:00 ～ 2026-09-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T16:07:51+08:00

## 1. 结论

本轮从用户认可的初筛预览继续，不沿用旧稿721项候选、旧评分或完成声明。原始缓存815个去重身份中，814条已读标题、454条进一步完整读摘要；原62项拟留已全部完成非作者题摘准入，后续撤回检查关闭1项。当前PUFFER与Parametric Multimodal User Memory贡献通过但日期冲突暂挂，GPU Retrieval因招聘检索组合尚不足以构成当前主线重要机制而退出；58项arXiv纳入本轮证据队列。另恢复Anthropic本窗安全更新1个机构事件，合计59项，不是已证实贡献数或Books改动数；具体事件与采用范围见下方逐项记录。

59项作者采用范围审阅及非作者核验均已结束：58项形成受限判断，1项中心测量争议冻结。13个材料家族落实必要Books增量，42项已有覆盖，3项仅报告；13个家族涉及10个章节，角色绑定两篇共用Ch5段落，不重复追加。增量连接表示测量与角色绑定、训练归因与逻辑参数块、KV/推测状态边界、生成坐标和物理控制接口。普通单篇待审与Books待写均为0；日期、来源和争议项已隔离为不支持正面结论或Books写入的本窗终态保留项，材料到达时只定点重开。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS原始缓存按UTC过滤本窗3项；原核心说明审阅保留逐项关闭理由 | 已检查 | California policy支持、Polimill客户案例、Ads商业进展无本窗重要新机制；Astra Sep1 13Z属于Sep02，不移入本日 |
| SRC-ANTHROPIC | [官方News](https://www.anthropic.com/news/improving-alignment-security-efforts) `publishedOn`恢复Aug31 23:00安全更新；作者与非作者核官方正文及Ch72 | 受阻 | 安全更新本身已验收；独立companion reward-seeker仅有August月份，首次公开时刻未定，见§5 |
| SRC-GOOGLE-AI | DeepMind/Research既有缓存与六项残余身份定点恢复；不重新遍历全年目录 | 受阻 | 四项贡献退出；116安全hardening与118HCRG的首次公开日期未定，Sep04可读观察不能关闭本窗，见§5 |
| SRC-META-AI | 官方publication目录两页的成功读取记录：当前Sep06后接Aug04/Jul29/Jul17，第二页May12；旧Sep05观察首页从Aug04开始 | 已检查 | 本窗无目录事件；Sep06卡片同族arXiv公开Sep04，不能倒移入Sep01 |
| SRC-QWEN | 英文API与中文API各37条，本轮解析全部`extra.date` | 已检查 | 74双语记录无缺日期且本窗零命中；邻近为Aug26 20:30与Sep03 08:00，不是74篇新论文 |
| SRC-DEEPSEEK | 官网/news原始目录15项最高Apr24；Sep07重开[官方更新日志](https://api-docs.deepseek.com/zh-cn/updates/)最新Aug21、Aug13、Jul31 | 已检查 | 已观察入口本窗无事件；没有用空渲染推断无更新 |
| SRC-MOONSHOT | 官方43个release端点恢复中38空、5非空；本轮定点读取kimi-cli完整分页与Kimi Code 73条，按本窗UTC过滤；Blog缓存已观察条目为2025年及更早 | 已检查 | 本窗无release命中：kimi-cli Sep01 16:53:20Z晚于截点，前项Jul16；Kimi Code相邻Sep02/Aug28，其他非空端点最新Jul04/Aug28/2024-12-24。未声称全部commit/RFC被扫 |
| SRC-TENCENT-HUNYUAN | 本轮共享检查：用户截图“全部”列表最上方Aug28 | 受阻 | 工具未取到全部卡片链接，不把空响应当无入口 |
| SRC-ZAI | 共享检查：研究目录最新Aug26，随后Aug14/Jun16 | 已检查 | 该目录本窗无命中，不外推所有渠道 |
| SRC-BYTEDANCE-SEED | 共享检查：Research/Blog/论文目录 | 已检查 | 已观察目录无本窗命中 |
| SRC-BAIDU-ERNIE | 共享检查：官方技术博客最新May09 | 已检查 | 已观察目录无本窗命中 |
| SRC-XIAOMI-MIMO | 共享检查：Paper最新Jun29；Blog已按官方frontmatter/iframe恢复为六月及更早；Code独立release归Sep03 | 已检查 | 无；没有把首页NEW标记当首次公开 |
| SRC-MINIMAX | 共享检查：中英文研究最新Aug13；Agent TechBlog官方Markdown目录唯一条目May13 | 已检查 | 无；原HTML外壳读取缺口已恢复 |
| SRC-ARXIV | 四个官方Sep1列表缓存及815项逐项初筛；62拟留独立准入、逐项当前日期/撤回检查 | 受阻 | 58项确认本窗采用范围；2项日期冲突暂挂，另2项贡献/撤回退出。暂挂项见§5，不继续重跑宽列表 |

只检查每日与实际触发来源；没有重新扫描每周来源。

## 3. 候选与判断

以下59项是本轮贡献与事件检查后的材料家族，不包括日期冲突暂挂项。arXiv公开时刻由主分类首次公告列表与官方20:00 EDT公告时制组合推定为北京时间09-01 08:00；提交时间单独保留在§4，不把周末submitted时刻当公开时间。原始日期与准入依据见初筛预览；旧721项评分不属于本轮。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Anthropic alignment/security update](https://www.anthropic.com/news/improving-alignment-security-efforts) | 2026-08-31T23:00:00+08:00 | `2+2+3=7`；`PLATFORM-SECURITY`。环境事实、行动授权与外部执行隔离需分别验证 | 深入完成 | 已有覆盖：[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)已有逐run配置、联网例外、不可解退出和成本边界 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SemKV](https://arxiv.org/html/2608.28911v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-KV-CACHE`。固定预算下区分量化码率插值与importance选择；确认长期解释缺口，触发深入Books判断 | 深入完成 | 整合：[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)已写，非作者写后复核通过 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [The Hallucination Signal Is a Mean Shift](https://arxiv.org/html/2608.28930v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`WORLDVIEW-REPRESENTATION`。正则与协方差估计影响probe排序，静态pair结果不能迁移为生成verifier | 标准完成 | 已有覆盖：Ch5表示证据阶梯与Ch8部署分布校准，不写线性普遍充分 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Recognition–Refusal Misalignment](https://arxiv.org/html/2608.29109v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`WORLDVIEW-LLM-INTELLIGENCE`。结构不可答识别与安全拒答/实际行为是不同命题 | 标准完成 | 已有覆盖：Ch8内部risk signal→行为决策与Ch5 probe/causal use分离 — `WORLDVIEW-LLM-INTELLIGENCE` [Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) |
| [Locked at the Entrance, Open Inside](https://arxiv.org/html/2608.29188v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`TRAIN-GRPO`。解法入口选择与进入后的条件执行应分别诊断；长期解释缺口触发深入审阅 | 深入完成 | 整合：[Ch33](../../../../books/part-04-training-system/33-grpo.md)已写，非作者写后复核通过 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Tail-Replay](https://arxiv.org/html/2608.30310v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-KV-CACHE`。FA hidden suffix重放替代密集recurrent checkpoint，但精确FA KV不使recurrent恢复自动精确 | 标准完成 | 已有覆盖：Ch45已有分组重放、hidden驻留、误差与精确checkpoint替代分支 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Faithfulness Is Not Free](https://arxiv.org/html/2608.30996v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-KV-CACHE`。压缩验收不能只看答案指标，需要证据行为与拒答/退化 | 标准完成 | 已有覆盖：Ch45 offline RAG量化段已给出固定round-trip与多维consumer验收 — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [RouteSparse](https://arxiv.org/html/2608.29058v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`INFER-PREFILL`。稀疏pattern/budget路由须联测probe、实际kernel及fallback | 深入完成 | 已有覆盖：Ch43的条件稀疏plan与worst-slice边界 — `INFER-PREFILL` [Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [Localizing Emergent Failures in Agentic AI](https://arxiv.org/html/2608.29228v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`AGENT-MULTI-AGENT`。最小修复集合族区分联合必要与替代充分 | 深入完成 | 已有覆盖：Ch82的counterfactual replay；不是只映射Workflow即完成 — `AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Manacá-1B](https://arxiv.org/html/2608.30114v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`MODEL-TOKENIZER`。artifact转换丢normalizer可改变输入而非权重能力 | 标准完成 | 已有覆盖：Ch11 normalization/round-trip及训练Serving handoff — `MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [Verification-Aware Training](https://arxiv.org/html/2608.30135v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-SPECULATIVE-DECODING`。draft学习信号对齐首拒绝survival | 标准完成 | 已有覆盖：Ch48 acceptance objective→prefix survival，不新增方法名段落 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Strong Drafts Need Compact Memories](https://arxiv.org/html/2608.30252v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-SPECULATIVE-DECODING`。draft近似memory与target精确分布分开 | 标准完成 | 已有覆盖：Ch48 proposal/verification职责与成本，Ch45承载压缩机制 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [DASC](https://arxiv.org/html/2608.30386v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`INFER-KV-CACHE`。state horizon、最重TP rank与replay共同决定容量 | 深入完成 | 已有覆盖：Ch45 state-unit retention与bounded replay — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [What It Costs to Compose, Rebuild, and Correct Precomputed Memory](https://arxiv.org/html/2608.30647v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`AGENT-MEMORY`。组合、重建与旁路纠错不是同一生命周期成本 | 深入完成 | 已有覆盖：Ch77已区分derived-state失效/重建，Ch75/77联合成本与consumer评估；root差异复核确认无需新段落 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [TrainSDC](https://arxiv.org/html/2608.30769v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`TRAIN-DISTRIBUTED-TRAINING`。silent fault保护匹配forward/backward/commit责任 | 深入完成 | 已有覆盖：Ch36分层保护到minibatch commit — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [A Universal Context-Reuse Layer for Cross-Model KV Sharing](https://arxiv.org/html/2608.30963v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`INFER-KV-CACHE`。跨模型state翻译须有identity、quality与break-even门 | 深入完成 | 已有覆盖：Ch45跨model state translation与native fallback — `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Stick to What You Know](https://arxiv.org/html/2608.30987v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`TRAIN-SFT`。监督目标应区分parametric recall与evidence/abstain | 深入完成 | 已有覆盖：Ch29 Base Knowledge Boundary — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Does On-Policy Distillation Really Distill?](https://arxiv.org/html/2608.31046v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`TRAIN-GRPO`。teacher-free与负advantage对照限制知识蒸馏归因 | 深入完成 | 整合：Ch33 teacher-signal节已补归因control，非作者写后通过 — `TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Measure Before You Manage](https://arxiv.org/html/2608.31057v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`AGENT-CONTEXT`。stored/delivered/management/outcome分账避免排名误归因 | 标准完成 | 已有覆盖：Ch75成本与consumer评价、Ch77construction/retrieval归因 — `AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [When Do Larger Batches Help Scale LLM RL](https://arxiv.org/html/2608.29296v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`TRAIN-DISTRIBUTED-TRAINING`。训练接纳batch、生成并发与time-to-target分别计量 | 标准完成 | 已有覆盖：Ch36收敛语义与Ch33 rollout/learner admission足承载；root差异复核不增加recipe段落 — `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Safe to Resume](https://arxiv.org/html/2608.29381v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`AGENT-WORKFLOW`。真实checkpoint也会失去跨域安全依赖 | 深入完成 | 已有覆盖：Ch81联合恢复点、event replay、外部effect协调与barrier — `AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Cloud-Edge Collaborative Decoding Privacy](https://arxiv.org/html/2608.29111v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`PLATFORM-SECURITY`。不上传原文不等于概率/token通道保密 | 深入完成 | 已有覆盖：Ch72全observable-flow隐私边界及经验测试/正式DP分工 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Layer Skipping under Matched Rigor](https://arxiv.org/html/2608.28846v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-EVALUATION-SYSTEM`。搜索state与pure/total时间口径须一致，内部矛盾触发深审 | 争议 | 暂缓：中心测量矛盾未解决，见§5材料请求 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Selective Disclosure](https://arxiv.org/html/2608.29070v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`PLATFORM-SECURITY`。词汇隐藏、语义识别与compliance不可互代 | 深入完成 | 已有覆盖：Ch72四种CoT命题与独立authority — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [APIFlow-Bench](https://arxiv.org/html/2608.29128v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`PLATFORM-EVALUATION-SYSTEM`。执行provenance与交付评分分离，链评分改变乘法null解释 | 深入完成 | 已有覆盖：Ch66分阶段/端到端与可执行证据；Ch81承载副作用重试 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Quantifying Error Tolerance in Synthetic Data](https://arxiv.org/html/2608.29144v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`TRAIN-DATA`。保函数的counterfactual与破坏监督映射不能统称同一噪声 | 标准完成 | 已有覆盖：Ch27多维质量、选择偏差与training-effect验收；不取消事实检查 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [HalluPrism](https://arxiv.org/html/2608.29193v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-EVALUATION-SYSTEM`。失败类别诊断不等于correctness排序 | 标准完成 | 已有覆盖：root差异复核确认Ch66诊断/probe、校准与held-out release原则足够，不追加同义短句 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Hub of Short Rows Inflates Intrinsic Dimension Estimation](https://arxiv.org/html/2608.29702v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`MODEL-EMBEDDING`。邻距估计受短norm hub影响，不直接测模型能力 | 深入完成 | 整合：Ch12几何段已补测量敏感性，不删除模型token或推断真实维度；非作者写后通过 — `MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md) |
| [Higher-Dimensional RoPE](https://arxiv.org/html/2608.29715v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`MODEL-POSITION-ENCODING`。固定正交换基保relative closure，不自动扩大函数类别 | 标准完成 | 已有覆盖：Ch13相对位置不变量与Ch22外推边界；不按名称扩章 — `MODEL-POSITION-ENCODING` [Ch13](../../../../books/part-02-model/13-position-encoding.md) |
| [Semantic Specificity of Representation Steering](https://arxiv.org/html/2608.29431v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`WORLDVIEW-REPRESENTATION`。目标修复必须区别同label原有能力与oracle gating | 深入完成 | 已有覆盖：Ch5因果阶梯、连带影响与跨context控制 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [FACE-Eval](https://arxiv.org/html/2608.29464v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-SECURITY`。cue channel与声明/行为/检测不能混为faithfulness | 深入完成 | 已有覆盖：Ch72四命题、条件检测与authority分离 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Token Counts Are Not Model Lineage](https://arxiv.org/html/2608.29930v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-MODEL-REGISTRY`。token-count proxy不能认证weight/family身份 | 标准完成 | 已有覆盖：Ch59行为指纹仅触发重评而非身份/所有权证书 — `PLATFORM-MODEL-REGISTRY` [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [ReTrace](https://arxiv.org/pdf/2608.29748v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-SPECULATIVE-DECODING`。已拒hidden仅作下一轮proposal条件，不作已提交KV | 深入完成 | 整合：Ch48已窄补辅助state与commit边界，root写后通过 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Ceiling-Clipped Acceptance Histograms](https://arxiv.org/html/2608.30427v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-SPECULATIVE-DECODING`。满块率是删失提示，双向horizon扩展会改变旧位置proposal | 深入完成 | 整合：Ch48删失诊断/扩块分布边界已写，独立写后通过 — `INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Which LLM for Which Work?](https://arxiv.org/html/2608.29560v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-EVALUATION-SYSTEM`。选择偏差与scorer偏差分离，确定分配不要求系数全精确 | 标准完成 | 已有覆盖：Ch66错误分布/scorer、evidence预算与Ch56分配职责 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PruneShift](https://arxiv.org/html/2608.29765v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-EVALUATION-SYSTEM`。广域proxy拟合、搜索邻域与最终决策不能互证 | 标准完成 | 已有覆盖：Ch66分布/selection bias/独立确认及Ch49部署验收 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Influence Is Not Authority](https://arxiv.org/html/2608.29942v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-SECURITY`。局部守卫条件性能不等于整条行动路径的风险 | 深入完成 | 已有覆盖：Ch72来源影响/授权/行动后果与Ch66阶段、端到端验收 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Reachability-Based Capability Confinement](https://arxiv.org/html/2608.30041v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-SECURITY`。削减capability改变可达性，证明受registry、envelope与禁态集合限制 | 深入完成 | 已有覆盖：Ch72完整中介、受限可达模型、sink授权与效应时序 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Beyond the Payload](https://arxiv.org/html/2608.30686v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-SECURITY`。攻击失败、显式发现与任务效用不能混同 | 深入完成 | 已有覆盖：Ch72环境事实不提供行动授权、Ch66harness及效用条件验收 — `PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Intervention Gap in Latent World Models](https://arxiv.org/html/2608.29998v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`MULTIMODAL-WORLD-MODELS`。测量捕获失败与imagined传播失败需分离 | 深入完成 | 整合：Ch25测量前置与uncertified边界已写，独立写后通过 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Motus2](https://arxiv.org/html/2608.30237v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`MULTIMODAL-WORLD-MODELS`。可见性mask与监督用途门不能互相替代 | 深入完成 | 已有覆盖：Ch25共享状态职责经Ch27失败轨迹用途、Ch29loss mask承载；root差异确认不新增段落 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [CAER](https://arxiv.org/html/2608.30897v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`MULTIMODAL-WORLD-MODELS`。动作条件敏感度重分监督，不是因果识别 | 标准完成 | 已有覆盖：Ch25外观/可控信息分离与Ch27加权目标、偏差 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Knowledge-Gated Tasks](https://arxiv.org/html/2608.30322v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-EVALUATION-SYSTEM`。知识依赖与完整harness能力分开测 | 标准完成 | 已有覆盖：Ch66 model/system层与Skill真实control path — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Beyond Consensus](https://arxiv.org/html/2608.30373v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`PLATFORM-EVALUATION-SYSTEM`。judge收敛与参考对齐分开 | 标准完成 | 已有覆盖：Ch66相关错误与judging控制 — `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PRM maximin search](https://arxiv.org/html/2608.30051v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`AGENT-PLANNING`。selection可以放大同簇评分误差 | 标准完成 | 已有覆盖：Ch79 search/pruning边界与Ch66 verifier/selection偏差 — `AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [Compression-Aware Abstention](https://arxiv.org/html/2608.29934v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`TRAIN-SFT`。证据压缩后的拒答与答案正确性分验 | 深入完成 | 已有覆盖：Ch29受控证据链及Ch45 cache品质/拒答 — `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [CoJEPA](https://arxiv.org/html/2608.30974v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`MULTIMODAL-WORLD-MODELS`。删EMA不等于删target职责 | 标准完成 | 仅报告：受限机制；Ch25已有防坍塌原则，未达新增长期结论门槛 — `MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Sycophantic Agreement Transfer](https://arxiv.org/html/2608.31079v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`TRAIN-DPO`。pair来源的相对分布可携带隐性行为信号 | 深入完成 | 整合：Ch34来源/行为验收已写，独立写后通过 — `TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [Token-Prediction Geometry](https://arxiv.org/html/2608.30072v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`MODEL-EMBEDDING`。目标与几何联系依赖曲率/稀有token条件 | 标准完成 | 已有覆盖：Ch12目标塑造关系及Ch5归纳偏置 — `MODEL-EMBEDDING` [Ch12](../../../../books/part-02-model/12-embedding.md) |
| [Singular ReLU Curvature](https://arxiv.org/html/2608.30960v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`WORLDVIEW-WHY-MODELS-LEARN`。离散轨迹趋近不保证导数趋近连续flow | 标准完成 | 仅报告：理论背景；Ch4未宣称连续/离散导数等价，不造优化器修复 — `WORLDVIEW-WHY-MODELS-LEARN` [Ch4](../../../../books/part-01-worldview/04-why-models-learn.md) |
| [Recursive Watermark Estimator](https://arxiv.org/html/2608.31091v1) | 2026-09-01T08:00:00+08:00 | `2+1+2=5`；`TRAIN-DATA`。固定误判未必保持来源标签的样本收益 | 标准完成 | 仅报告：理论背景；Ch27真实来源与lineage原则不变 — `TRAIN-DATA` [Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Tensor-Product Perspective](https://arxiv.org/html/2608.29034v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`WORLDVIEW-REPRESENTATION`。概念集合与角色绑定不同 | 深入完成 | 整合：联合29530写Ch5角色绑定短段，独立写后通过 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Emergent Symbolic Structure](https://arxiv.org/html/2608.29530v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`WORLDVIEW-REPRESENTATION`。表示可组合不等于行为泛化 | 深入完成 | 整合：联合29034写Ch5同一机制段，独立写后通过，不重复增补 — `WORLDVIEW-REPRESENTATION` [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Q-Strata](https://arxiv.org/html/2608.30564v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`INFER-TENSORRT-LLM`。局部proxy搜索后仍需组装模型评价 | 标准完成 | 已有覆盖：Ch49 expert校准、physical palette与部署质量 — `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [TuringLLM](https://arxiv.org/html/2608.30567v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`MODEL-MOE`。期望fanout不等于硬容量，训练与部署可分支 | 标准完成 | 已有覆盖：Ch21 population cutoff、dropless与capacity；Ch22混合状态 — `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) |
| [CARVE](https://arxiv.org/html/2608.30922v1) | 2026-09-01T08:00:00+08:00 | `2+2+2=6`；`MULTIMODAL-GENERATIVE-PARADIGMS`。插槽后坐标、canvas与logits必须同代绑定 | 深入完成 | 整合：Ch24长度admission条件分支已写，独立写后通过 — `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Qwen3.8-Next](https://arxiv.org/html/2608.30320v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`TRAIN-PRETRAINING`。物理fused tensor不应决定Muon数学块边界 | 深入完成 | 整合：Ch28逻辑matrix/head边界与物理fusion区别已写，独立写后通过 — `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Agentic Data Cracking](https://arxiv.org/html/2608.31082v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`AGENT-MEMORY`。已加载文档的机会性结构缓存需计预热/更新成本 | 深入完成 | 已有覆盖：Ch77 write-time/late-construction与provenance已有覆盖，独立绑定通过 — `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [SUN](https://arxiv.org/html/2608.31167v1) | 2026-09-01T08:00:00+08:00 | `2+2+3=7`；`MULTIMODAL-EMBODIED-VLA`。controller/reward/predicate共享语义而非共享数值函数 | 深入完成 | 整合：Ch26 canonical residual跨训练/控制短段已写，独立写后通过 — `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

## 4. 证据与知识整合

旧证据保留于原笔记及旧稿快照，只复用可核实且命题/版本未变化部分，不能用旧“深读完成”直接授予当前Books结论。

当前59项均已完成所述采用范围的正文检查：58项形成受限命题，1项因内部性能矛盾保持Disputed，不能说59项Evidence通过。其中12项复用已保存的exact-v1非作者审阅，并本轮重核官方abs与当前Books；没有将复用说成再次完整阅读全文。13项Source Family对应的Books增量已完成独立证据与实际写后验收：SemKV、RLVR、OPD归因、短范数hub测量、ReTrace、ceiling诊断、Intervention Gap、角色绑定两篇、CARVE、偏好来源、逻辑优化器块与共享残差接口；角色绑定两篇共用Ch5一段，不重复增补。Data Cracking已独立确认Ch77现有内容足以承载；其余已有覆盖及仅报告项均已完成当前非作者绑定验收。详细正文位置、控制与未证明内容见本轮证据笔记与本轮独立复核。

PUFFER已重读缓存exact-v1的机制、结果与限制，并重新打开官方HTML；immutable dataset-owned keys、compaction与withdrawal的机制可核验，但当前官方摘要页和HTML同时显示Jul29的v1日期，与Sep1列表标签冲突。日期未解决前不归入本窗确定候选，也不据此重写Books。

跨材料主线：位宽插值、重要性排序与实现证据不是同一件事

SemKV先比较uniform码点，再在相同平均预算下互换分配指标。其主Llama工作点的相近结果支持收益可能来自新平均码率，而非更准确的语义排序；Mistral和另一quantizer的结果又给出反例，所以不能写成通用“指标无关”。质量断崖随model、codec和生成协议变化，n.s.并非等价；跨界混合也不是不可能。质量实验使用fake quantization后FP16计算，真实packed容量单独验，未证明生产并发/SLO。详细条件和采用范围见证据笔记。

对应改动为[Ch45量化目标](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)：把上述联系插在统一精度校准与在线双精度分支之间，保留FullKV、统一较高精度及eviction独立分支的适用条件；没有新增孤立论文节。

### [Anthropic alignment/security update](https://www.anthropic.com/news/improving-alignment-security-efforts)

[官方正文](https://www.anthropic.com/news/improving-alignment-security-efforts) 的external-partner safeguards、environment/state-of-knowledge及脚注直接核验；`publishedOn=2026-08-31T15:00:00.000Z`的原始字段见作者定点缓存。环境事实、行动授权和外部执行隔离分权有原文支持，motivated reasoning仍是调查假设，classifier效果不能从部署公告推得。实际重读Ch72约1465–1485及相邻隔离/事故边界，逐run配置核验、联网例外、权限内不可解退出、成本和披露限制均已存在。深入采用范围与NoChange通过；companion reward-seeker仍为独立日期缺口，未并入本事件。

事件依据：`publishedOn=2026-08-31T15:00:00Z`，北京时间Aug31 23:00。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)已有逐run配置、联网例外、不可解退出和成本边界。归属 `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [SemKV](https://arxiv.org/html/2608.28911v1)

固定预算下区分量化码率插值与importance选择；确认长期解释缺口，触发深入Books判断。深入完成；非作者证据通过。作者实验，不是生产实现证明；当前采用范围非作者核验通过。

事件依据：官方主分类Sep1公告批次；v1提交Aug28，二者分开记录。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)已写，非作者写后复核通过。归属 `INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [The Hallucination Signal Is a Mean Shift](https://arxiv.org/html/2608.28930v1)

root直接核exact §3.1–3.2、LayerMix方法、适用边界及Limitations。mean direction的移除与单方向保留是两个控制，不能把必要写成充分；静态paired oracle到自然生成的pilot迁移接近随机，主收益是去掉held-out oracle层选择而非巨大精度增益。实际Ch5“相关/预测/因果”及Ch8内部signal→deployment calibration→answer/abstain已承载这一边界，采用范围/NoChange通过。不认证全部scaling附录。

事件依据：CL Sep1公告；v1 Aug28 23:01:21UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch5表示证据阶梯与Ch8部署分布校准，不写线性普遍充分。归属 `WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。

### [Recognition–Refusal Misalignment](https://arxiv.org/html/2608.29109v1)

root直接核exact §3、4.2–4.4与Limitations。A-null PCA/MeanDiff、same-space控制和gated干预支持结构不可答信号与安全拒答轴分离；4-anchor LLM-assisted因果标签、Qwen候选标签直通与小gate使fact/open-world不得外推。11模型probe、4-anchor干预与16模型breadth不合并成一组因果证据。Ch5证据阶梯、Ch8 signal与回答授权决策已有明确分工，NoChange通过；未因当前HTML的“v2 grid”措辞推造版本史。

事件依据：CL Sep1公告；v1 Aug29 07:38:17UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch8内部risk signal→行为决策与Ch5 probe/causal use分离。归属 `WORLDVIEW-LLM-INTELLIGENCE`，[Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)。

### [Locked at the Entrance, Open Inside](https://arxiv.org/html/2608.29188v1)

解法入口选择与进入后的条件执行应分别诊断；长期解释缺口触发深入审阅。深入完成；非作者证据通过。有限采样未出现不等于零支持，入口干预不替代自然条件分布；当前采用范围非作者核验通过。

事件依据：官方Sep1主分类公告批次；v1提交Aug29。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：[Ch33](../../../../books/part-04-training-system/33-grpo.md)已写，非作者写后复核通过。归属 `TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)。

### [Tail-Replay](https://arxiv.org/html/2608.30310v1)

root本轮另直接核exact方法与Table3，当前Ch45 full-attention hidden suffix→zero recurrent replay→quality fallback；重建是近似，不推广5–10%比例。当前段及相邻sparse exact-checkpoint分支区分清楚，NoChange通过。

事件依据：LG Sep1公告批次；v1提交Aug31 06:27:07UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch45已有分组重放、hidden驻留、误差与精确checkpoint替代分支。归属 `INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [Faithfulness Is Not Free](https://arxiv.org/html/2608.30996v1)

root本轮另直接核exact固定retrieval/prompt/decode与低精度round-trip、refusal/degeneration控制；当前Ch45 answer-accuracy与evidence-faithfulness双门段已有覆盖。一模型/两QA/三K与judge混杂不支持通用精度结论，NoChange通过。

事件依据：CL Sep1公告批次；v1提交Aug31 15:47:23UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch45 offline RAG量化段已给出固定round-trip与多维consumer验收。归属 `INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [RouteSparse](https://arxiv.org/html/2608.29058v1)

Ch43稀疏cost之后conditional pattern/budget与probe/regroup/launch/dense fallback、局部attention-output保证段；只限披露模型/hardware，不传播通用6.5x。NoChange通过。

事件依据：CL Sep1主类公告；v1 Aug29。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch43的条件稀疏plan与worst-slice边界。归属 `INFER-PREFILL`，[Ch43](../../../../books/part-05-inference-system/43-prefill.md)。

### [Localizing Emergent Failures in Agentic AI](https://arxiv.org/html/2608.29228v1)

Ch82 Failure中声明DAG/domain/q/共同seed的全部inclusion-minimal repair families与Unknown；联合必要不同于替代充分，隐边不获闭世界保证。NoChange通过。

事件依据：AI Sep1主类公告；v1 Aug29。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch82的counterfactual replay；不是只映射Workflow即完成。归属 `AGENT-MULTI-AGENT`，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)。

### [Manacá-1B](https://arxiv.org/html/2608.30114v1)

Ch11 normalization/可逆性、逐ID reference与tokenizer/checkpoint/Serving handoff；不宣称Megatron/HF logits等价。NoChange通过。

事件依据：CL Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch11 normalization/round-trip及训练Serving handoff。归属 `MODEL-TOKENIZER`，[Ch11](../../../../books/part-02-model/11-tokenizer.md)。

### [Verification-Aware Training](https://arxiv.org/html/2608.30135v1)

Ch48首拒绝后依赖suffix失效、accepted-prefix survival及draft/verify成本；survival监督不改变target verification。NoChange通过。

事件依据：CL Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch48 acceptance objective→prefix survival，不新增方法名段落。归属 `INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。

### [Strong Drafts Need Compact Memories](https://arxiv.org/html/2608.30252v1)

Ch48 proposal approximation与target verification分权、完整成本；draft memory压缩不是target state精确恢复，额外prefill不能忽略。NoChange通过。

事件依据：LG Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch48 proposal/verification职责与成本，Ch45承载压缩机制。归属 `INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。

### [DASC](https://arxiv.org/html/2608.30386v1)

Ch45 recurrent state-unit horizon、TP最重rank与bounded replay/full-state fallback已有连续论证；只限hybrid/TP8近似。NoChange通过。

事件依据：LG Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch45 state-unit retention与bounded replay。归属 `INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [What It Costs to Compose, Rebuild, and Correct Precomputed Memory](https://arxiv.org/html/2608.30647v1)

Ch77派生索引dependency、失效/重建与consumer控制，Ch75 assembly/Prefill/storage-read分账；joint/warm/correction区别是现有生命周期的实例，不给单8B/24K合成结果普遍阈值。NoChange通过。

事件依据：CL Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch77已区分derived-state失效/重建，Ch75/77联合成本与consumer评估；root差异复核确认无需新段落。归属 `AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)。

### [TrainSDC](https://arxiv.org/html/2608.30769v1)

Ch36 silent fault之后forward guard、activation gain、backward exponent/collective与optimizer commit分权；注入故障不是自然发生率/检测完备证明。NoChange通过。

事件依据：LG Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch36分层保护到minibatch commit。归属 `TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。

### [A Universal Context-Reuse Layer for Cross-Model KV Sharing](https://arxiv.org/html/2608.30963v1)

Ch45 prefix identity后source→frozen target translator，translation/transfer/assembly break-even、quality/native fallback；不计source prefill的小样本不能证明Universal。NoChange通过。

事件依据：LG Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch45跨model state translation与native fallback。归属 `INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)。

### [Stick to What You Know](https://arxiv.org/html/2608.30987v1)

Ch29 base-knowledge boundary冻结probe下parametric/evidence/abstain三分监督与false-refusal成本；不把行为probe当全量参数知识oracle。NoChange通过。

事件依据：CL Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch29 Base Knowledge Boundary。归属 `TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)。

### [Does On-Policy Distillation Really Distill?](https://arxiv.org/html/2608.31046v1)

teacher-free与负advantage对照限制知识蒸馏归因。深入完成；非作者Evidence通过。C.3是近似匹配推理长度，不是严格训练预算matching；当前采用范围非作者核验通过。

事件依据：LG Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch33 teacher-signal节已补归因control，非作者写后通过。归属 `TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md)。

### [Measure Before You Manage](https://arxiv.org/html/2608.31057v1)

Ch75 relevance/selection/placement/faithfulness与assembly/Prefill/storage-read，Ch77派生状态消费者对照；8完整/16中断block不支持held-out策略排名。NoChange通过。

事件依据：AI Sep1主类公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch75成本与consumer评价、Ch77construction/retrieval归因。归属 `AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md)。

### [When Do Larger Batches Help Scale LLM RL](https://arxiv.org/html/2608.29296v1)

root直接核exact §2、3.3协议/GRPO/PPO/固定LR与group控制、§5 tuning。retained-response而非生成并发为optimizer样本轴；±1点只是描述带，PPO排除critic warmup，actor/critic的critical scale不相同。当前Ch36 Global Batch与Scaling Efficiency、Ch33 learner admission已承载吞吐与到目标样本共同决定时间、改batch须重验学习率；NoChange通过。未采用硬件加速常数或平方根LR普遍保证。

事件依据：LG Sep1公告；v1 Aug29 14:32:09UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch36收敛语义与Ch33 rollout/learner admission足承载；root差异复核不增加recipe段落。归属 `TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。

### [Safe to Resume](https://arxiv.org/html/2608.29381v1)

root直接核III-B/C、IV-A–E、VI-B与VII。五种故障分开缺状态、非共同因果切面、外界变化、随机重试和未记录effect；攻击者不能篡改checkpoint。347轨迹/五框架/1735执行不构成生产失败率或完整安全认证。当前Ch81 Context与Environment同generation、event frontier、idempotency/compensation/reconciliation和action前barrier已覆盖，NoChange通过。

事件依据：AI Sep1列表；v1 Aug29 17:40:13UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch81联合恢复点、event replay、外部effect协调与barrier。归属 `AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md)。

### [Cloud-Edge Collaborative Decoding Privacy](https://arxiv.org/html/2608.29111v1)

root直接核§2.3、4.1–4.3、5.1及Limitations。cloud上传probability与edge同步token是两种observer channel；分布差utility proxy不是epsilon预算，同族词表和有限prompt inversion不能保证异词表/最强攻击。Ch72 observable data flow→observer→joint attacker→calibration与紧接DP privacy-unit段实际对读通过，NoChange。

事件依据：AI Sep1列表；v1 Aug29 07:40:14UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch72全observable-flow隐私边界及经验测试/正式DP分工。归属 `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Layer Skipping under Matched Rigor](https://arxiv.org/html/2608.28846v1)

root直接核exact §6.2 Table3与6.2.1。CNN/0.5B ConfLayers pure10889ms大于total10231.4ms；GSM/0.5B9194与10338.5不对应2.2%；四cell total中SWIFT慢两项而正文称三项。不能选择一个数字默认为正确，性能/排名冻结成立。所需材料是相同query序列的同步pure/total原始日志、search-state复用配置或官方更正表；不请求无关附录，不据此否认Ch48/66既有成本口径。此项争议未解决，不计全日Evidence通过。

事件依据：CL Sep1公告；v1 Aug28 20:33:40UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：暂缓：中心测量矛盾未解决，见§5材料请求。归属 `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Selective Disclosure](https://arxiv.org/html/2608.29070v1)

root实读exact§3.1–3.2/4.3/5.4末段/Limitations。植入prompt directive、显式自述detector、trace-only semantic monitor与行为是不同测量；无directive控制才有false-positive底线，词汇隐去不证明训练诱导隐瞒仍可检。Ch72 CoT policy-bound sensor已分controllability/monitorability/faithfulness/outcome且外置authority，NoChange通过，不使用通用隐藏vector主张。

事件依据：LG Sep1公告；v1 Aug29 05:50:54UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch72四种CoT命题与独立authority。归属 `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [APIFlow-Bench](https://arxiv.org/html/2608.29128v1)

root实读exact§4 Gate1/3、§5 provenance/state与typed answer、§6及§8.4/9scope。465/467gold replay、28solo无state signature、LLM verifier advisory、world而非run是cluster单位均限制认证范围；不采用“有provenance就不怕污染”。Ch66 Agent/outcome与可执行证据已要求执行/副作用/版本/独立evaluator，Ch81拥有有副作用retry。NoChange通过。

事件依据：AI Sep1公告；v1 Aug29 08:12:11UTC；不称benchmark本日首发。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch66分阶段/端到端与可执行证据；Ch81承载副作用重试。归属 `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Quantifying Error Tolerance in Synthetic Data](https://arxiv.org/html/2608.29144v1)

root实读exact§3.1定义、§4/5/7.2/Limitations。operand同时变x/y保留映射，与固定x破坏operator不是同种事实噪声；oracle过滤上界不提供部署识别器，四模型/合成与有限任务不能推出通用容错率。Ch27多维quality/选择偏差/held-out能力与Training Effect的实际段落已承载，NoChange通过。

事件依据：CL Sep1公告；v1 Aug29 08:41:58UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch27多维质量、选择偏差与training-effect验收；不取消事实检查。归属 `TRAIN-DATA`，[Ch27](../../../../books/part-04-training-system/27-data.md)。

### [HalluPrism](https://arxiv.org/html/2608.29193v1)

root实读exact§3–5正文及Limitations，未把所链接全46附表或理论定理算已审。visual扰动/blank confidence/relation signature是联合行为诊断而非三个互斥因果源；dataset/model控制、仅VSR有relation、三手写scalarizer与fix/break/no-intervention比较限定结论。Ch66 failure taxonomy、目标校准与Ch8 sensor/决策分离已覆盖；不把诊断优势变成拒答排序或通用纠错优势，NoChange通过。

事件依据：LG Sep1公告；v1 Aug29 11:06:37UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：root差异复核确认Ch66诊断/probe、校准与held-out release原则足够，不追加同义短句。归属 `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [A Hub of Short Rows Inflates Intrinsic Dimension Estimation](https://arxiv.org/html/2608.29702v1)

邻距估计受短norm hub影响，不直接测模型能力。深入所采用测量反证；非作者证据通过；当前采用范围非作者核验通过。

事件依据：CL Sep1公告；v1 Aug30 10:19:11UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch12几何段已补测量敏感性，不删除模型token或推断真实维度；非作者写后通过。归属 `MODEL-EMBEDDING`，[Ch12](../../../../books/part-02-model/12-embedding.md)。

### [Higher-Dimensional RoPE](https://arxiv.org/html/2608.29715v1)

root实读exact§3.1公式7/8、3.2、4.1/4.4与Limitations。固定正交共轭保relative/norm；basis和frequency grouping改变参数化，不独自证明更大函数类别（固定Q可吸收到Q/K投影，是本次限定推断）。650M/1.3B、50B主试/30B消融不支持通用吞吐或长窗保证。Ch13 RoPE相对不变量与频率外推边界已有覆盖，NoChange通过。

事件依据：LG Sep1公告；v1 Aug30 10:46:24UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch13相对位置不变量与Ch22外推边界；不按名称扩章。归属 `MODEL-POSITION-ENCODING`，[Ch13](../../../../books/part-02-model/13-position-encoding.md)。

### [Semantic Specificity of Representation Steering](https://arxiv.org/html/2608.29431v1)

root实读exact§4.3、5.1/5.4/5.6与Limitations。label-outcome confound与有原生能力的cross-rule collateral test有效，但“过阈值即generalized repair”不是充分证明；相同少量accuracy也不推出函数等价，oracle gating不是部署识别器。Ch5 localized intervention→downstream→cross-context及连带影响已有覆盖，NoChange通过；不采用全域steering无效等强主张。

事件依据：CL Sep1公告；v1 Aug29 20:31:32UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch5因果阶梯、连带影响与跨context控制。归属 `WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。

### [FACE-Eval](https://arxiv.org/html/2608.29464v1)

root直接核exact§2.2/2.4/Limitations。相同cue跨channel仍同时换role和预填tool exchange，explicitness同时换格式/推断负担；VCR在cue-following条件下、UAR还受following影响，不能说读出了因果faithfulness。judge和eligible-set影响排名，非完整自主tool选择。Ch72 CoT sensor段实际已有四轴与channel/长度/正例支持量，NoChange通过，不用相关性命名内部机制。

事件依据：CL Sep1公告；v1 Aug29 23:07:08UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch72四命题、条件检测与authority分离。归属 `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Token Counts Are Not Model Lineage](https://arxiv.org/html/2608.29930v1)

root直接核exact§4.2/4.3/6.2/8。常数offset的usage fingerprint混合tokenizer/template/accounting；未达到20有效/0.8覆盖或任一repeat不合格返回null。12holdout仅6eligible且有2FN，named family不是weight lineage。Ch59 fingerprint只触发revalidation、不得证明provider/权重/所有权的当前正文已完整覆盖，NoChange通过。

事件依据：CL Sep1公告；v1 Aug30 17:58:49UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch59行为指纹仅触发重评而非身份/所有权证书。归属 `PLATFORM-MODEL-REGISTRY`，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md)。

### [ReTrace](https://arxiv.org/pdf/2608.29748v1)

已拒hidden仅作下一轮proposal条件，不作已提交KV。深入状态边界完成；HTML404已PDF恢复，dense/lowrank评价分开；非作者通过；当前采用范围非作者核验通过。

事件依据：CL Sep1公告；v1 Aug30 12:20:54UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch48已窄补辅助state与commit边界，root写后通过。归属 `INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。

### [Ceiling-Clipped Acceptance Histograms](https://arxiv.org/html/2608.30427v1)

满块率是删失提示，双向horizon扩展会改变旧位置proposal。深入采用与非作者通过；in-sample/约5独立drafter、EOS过滤、n.s.非等价；不采硬件不明速度；当前采用范围非作者核验通过。

事件依据：CL Sep1公告；v1 Aug31 08:23:14UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch48删失诊断/扩块分布边界已写，独立写后通过。归属 `INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)。

### [Which LLM for Which Work?](https://arxiv.org/html/2608.29560v1)

root直接核exact§3.1–3.2与Limitations。随机readout只修selection；独立interval box和成本已知时两solve判当前方案仍最优，tie不变/真值在box内/center sampling误差不获保证。Ch66 scorer误差与sampling分离、自适应evidence预算已有覆盖，Ch56拥有最终计划；NoChange通过，不把离线replay当生产认证。

事件依据：LG Sep1公告；v1 Aug30 05:00:43UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch66错误分布/scorer、evidence预算与Ch56分配职责。归属 `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [PruneShift](https://arxiv.org/html/2608.29765v1)

root直接核exact§3.2、4.1反例、4.5与Discussion。交换两个最优rank即可保持近完美总体相关却选错；finite-pool regret仅global下界，零不证全局最优。logical mask、OPT125M/encoder、小固定域与保守coverage界不支持部署加速。Ch66 intended population/selection/独立确认及Ch49实际执行质量分层已有覆盖，NoChange通过。

事件依据：LG Sep1公告；v1 Aug30 12:52:16UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch66分布/selection bias/独立确认及Ch49部署验收。归属 `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Influence Is Not Authority](https://arxiv.org/html/2608.29942v1)

[exact](https://arxiv.org/html/2608.29942v1) §3/4.2/5.4/8已直接核。24匹配case只搬参数来源，teacher-forced unauthorized不是部署率；gate admission与最终authorized outcome分开。实际Ch72“谁获得行为控制权”及Ch66分stage/effect评价已有覆盖，NoChange通过，不采固定实现的通用防御排行。

事件依据：AI Sep1公告；v1 Aug30 18:16:04UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch72来源影响/授权/行动后果与Ch66阶段、端到端验收。归属 `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Reachability-Based Capability Confinement](https://arxiv.org/html/2608.30041v1)

[exact](https://arxiv.org/html/2608.30041v1) §3.3–3.6/5.5直接核。registry正确、envelope sound、trusted harness、完整forbidden set及effect前mediating是保证前提；输出检查不撤销已提交effect。adaptive case可不进B却Harm，表明声明模型与现实后果不同。实际Ch72 canonical action/effect-time gate及有限效果路径证明已承载，NoChange通过，不用min-cut冒充开放安全。

事件依据：AI Sep1公告；v1 Aug30 20:57:47UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch72完整中介、受限可达模型、sink授权与效应时序。归属 `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Beyond the Payload](https://arxiv.org/html/2608.30686v1)

[exact](https://arxiv.org/html/2608.30686v1) §3.4/4.1/5.2直接核。HTTP实际secret receipt与LLM alert是两个oracle；低ASR可能仅因执行较少，有限case不能推出措辞中和攻击。20repo不替代多seed/聚类，partial/full配置不能混排。Ch72运行环境/authority/effect和Ch66 utility-security分层已有覆盖，NoChange通过，不采用主文冲突的机制归因或部署安全排名。

事件依据：CL Sep1公告；v1 Aug31 12:26:01UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch72环境事实不提供行动授权、Ch66harness及效用条件验收。归属 `PLATFORM-SECURITY`，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [The Intervention Gap in Latent World Models](https://arxiv.org/html/2608.29998v1)

测量捕获失败与imagined传播失败需分离。深入采用与非作者通过；两环境/五步/固定query与support，不采架构排名；当前采用范围非作者核验通过。

事件依据：Sep1官方列表；v1 Aug30 19:47:51UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch25测量前置与uncertified边界已写，独立写后通过。归属 `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。

### [Motus2](https://arxiv.org/html/2608.30237v1)

[exact](https://arxiv.org/html/2608.30237v1) §3.2/3.3及§7直接核。action-first visibility不同于loss gate，失败动作可作为transition条件而不作模仿目标；value是相对进度而非校准成功概率。规划改变selection、MBRL另改action参数而固定simulator/evaluator。实际Ch25 shared world/policy/value owner与Ch26 WAM三接口、训练期监督/部署成本分支，结合Ch29 mask不删除条件输入的既有正文，已承载采用责任；NoChange通过。不把未隔离mask×gate收益、可穿戴触觉跨形态迁移或未来场景作为已证普遍能力。

事件依据：Sep1官方列表；v1 Aug31 04:44:33UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch25共享状态职责经Ch27失败轨迹用途、Ch29loss mask承载；root差异确认不新增段落。归属 `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。

### [CAER](https://arxiv.org/html/2608.30897v1)

[exact](https://arxiv.org/html/2608.30897v1) §2.2–2.3及§3.1–3.2直接核。same-noise action/null差含未来noisy latent，文中也承认不是do识别；归一化仅在均值超过epsilon才严格单位质量。两个额外no-grad forward使matched-step不等于matched-time，四场景聚合改善不保各项control指标。Ch25外观/可控信息分开、Ch27加权改变风险与数据选择偏差已有覆盖；NoChange通过，不采用无条件优化/永久可修复保证。

事件依据：Sep1官方列表；v1 Aug31 14:49:56UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch25外观/可控信息分离与Ch27加权目标、偏差。归属 `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。

### [Knowledge-Gated Tasks](https://arxiv.org/html/2608.30322v1)

[exact](https://arxiv.org/html/2608.30322v1) §3.1/3.4/3.6、§4.1及§5.3–5.4。instruction不变而提供/移除artifact可定位知识依赖；静态泄漏检查、公开子集和有限模型+harness不能证明全部私有任务无泄漏，也不能归因为训练收益。Ch66 model/system/Agent与完整控制路径分层、独立任务契约已覆盖；标准采用范围与NoChange通过。

事件依据：AI Sep1公告；v1 Aug31 06:39:27UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch66 model/system层与Skill真实control path。归属 `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Beyond Consensus](https://arxiv.org/html/2608.30373v1)

[exact](https://arxiv.org/html/2608.30373v1) §2–4及limitations。strict/lenient配对、neutral与score-masked控制显示收敛不等于参考对齐，但只覆盖披露的六模型、两任务和有限交互协议；角色/协议条件不能外推为所有Multi-Agent必然退化。Ch66低熵共同错误、独立truth与judge控制已有覆盖；标准范围与NoChange通过。

事件依据：CL Sep1公告；v1 Aug31 07:28:55UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch66相关错误与judging控制。归属 `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [PRM maximin search](https://arxiv.org/html/2608.30051v1)

[exact](https://arxiv.org/html/2608.30051v1) §5.1与§6设置、Table1及§6.2–6.4。RKHS半径的样本proxy不是真实误差上界；保持多样prefix改变selection而不修复PRM真值。matched trajectory数不等于matched wall time，Table1与正文个别数字/总括不一致，故不采用17–35%、14/16或统一开销的headline。小子集Gaussian扰动不等于真实相关误差。实际Ch79 search/pruning与共同盲点、Ch66 evaluator/selection偏差已有覆盖；有限机制判断与NoChange通过，强性能宣传仍未获认证。

事件依据：AI Sep1公告；v1 Aug30 21:25:03UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch79 search/pruning边界与Ch66 verifier/selection偏差。归属 `AGENT-PLANNING`，[Ch79](../../../../books/part-07-agent/79-planning.md)。

### [Compression-Aware Abstention](https://arxiv.org/html/2608.29934v1)

[exact](https://arxiv.org/html/2608.29934v1) §2、§5.4–5.5及limitations。mask/短span控制的证据存活不等于语义充分oracle，桥接事实标注仍可能错误；压缩prompt与全prefill后实际KV eviction是不同实验。随机/等长控制不证明完整自省，有限MuSiQue/Qwen设置不能推出通用阈值。实际Ch29受控证据链、缺桥接/无支持/冗余控制和false-abstention成本，以及Ch45 cache质量/拒答分验已有覆盖；深入采用范围与NoChange通过。

事件依据：CL Sep1公告；v1 Aug30 18:02:15UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch29受控证据链及Ch45 cache品质/拒答。归属 `TRAIN-SFT`，[Ch29](../../../../books/part-04-training-system/29-sft.md)。

### [CoJEPA](https://arxiv.org/html/2608.30974v1)

[exact](https://arxiv.org/html/2608.30974v1) §3.1–3.3、§4–5及§6所采局部结果。shared backbone的full-view stop-gradient target仍存在，contrastive梯度另承担表示约束；移除EMA不等于移除target责任。三种训练配置与linear probe不隔离EMA的唯一因果收益，也无直接坍塌度量。私有音乐数据与小模型下游结果不证明规模可替代。实际Ch25 next-embedding prediction的encoder identity/target drift/collapse及任务验证已承载一般边界；该机制实例仅报告通过，不新增长期结论。

事件依据：LG/AI Sep1公告；v1 Aug31 15:36:13UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：仅报告：受限机制；Ch25已有防坍塌原则，未达新增长期结论门槛。归属 `MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)。

### [Sycophantic Agreement Transfer](https://arxiv.org/html/2608.31079v1)

独立exact §3.2–3.4/5.1–5.3、Discussion及所采评测附录；实际重读Ch34数据质量→offline→相对质量前后及notes。chosen/rejected相对teacher来源可传递隐性行为，不将经验log-ratio写成DPO普遍定理，也不承诺反转来源无能力代价。通过。

事件依据：LG Sep1公告；v1 Aug31 16:52:57UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch34来源/行为验收已写，独立写后通过。归属 `TRAIN-DPO`，[Ch34](../../../../books/part-04-training-system/34-dpo.md)。

### [Token-Prediction Geometry](https://arxiv.org/html/2608.30072v1)

[exact](https://arxiv.org/html/2608.30072v1) §2.1–2.3及§5受控设置。目标到表示几何的联系受条件分布、曲率和稀有token权重影响，48token过程的可精确枚举实验不等于LLM保证；不据此认证全文的所有动力学推论。实际Ch12目标塑造关系与坐标/测量边界、Ch5表示与泛化证据阶梯已有覆盖；标准采用范围与NoChange通过。

事件依据：LG Sep1公告；v1 Aug30 22:33:15UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch12目标塑造关系及Ch5归纳偏置。归属 `MODEL-EMBEDDING`，[Ch12](../../../../books/part-02-model/12-embedding.md)。

### [Singular ReLU Curvature](https://arxiv.org/html/2608.30960v1)

[exact](https://arxiv.org/html/2608.30960v1) §2及§6–8。有限时域、分离横穿、确定性full-batch条件下，轨迹逼近和其导数逼近应分开；不包含任意grazing/sliding或SGD，亦不意味着离散AD本身算错。当前Ch4实际梯度更新/mini-batch/链式法则没有宣称连续flow与离散导数等价。仅报告理论背景通过，不构造优化器修复或新Books结论。

事件依据：LG Sep1公告；v1 Aug31 15:26:59UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：仅报告：理论背景；Ch4未宣称连续/离散导数等价，不造优化器修复。归属 `WORLDVIEW-WHY-MODELS-LEARN`，[Ch4](../../../../books/part-01-worldview/04-why-models-learn.md)。

### [Recursive Watermark Estimator](https://arxiv.org/html/2608.31091v1)

[exact](https://arxiv.org/html/2608.31091v1) §II与§IV-A Proposition1及证明所用有限类别/混合与检测条件。来源检测误差改变可利用样本的估计误差边界，固定误判不能自动保留oracle标签收益；不把该模型的渐近尺度变成LLM水印生产阈值，也不认证全文所有minimax情形。Ch27真实来源/lineage的原则未被改变；标准采用范围、仅报告通过。

事件依据：LG Sep1公告；v1 Aug31 17:00:09UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：仅报告：理论背景；Ch27真实来源与lineage原则不变。归属 `TRAIN-DATA`，[Ch27](../../../../books/part-04-training-system/27-data.md)。

### [Tensor-Product Perspective](https://arxiv.org/html/2608.29034v1)

概念集合与角色绑定不同。深入采用及非作者证据通过；人工roles/受控干预非唯一机制；当前采用范围非作者核验通过。

事件依据：CL Sep1公告；v1 Aug29 04:00:46UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：联合29530写Ch5角色绑定短段，独立写后通过。归属 `WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。

### [Emergent Symbolic Structure](https://arxiv.org/html/2608.29530v1)

表示可组合不等于行为泛化。深入采用及非作者证据通过；部分token替换，holdout不指target预训练；当前采用范围非作者核验通过。

事件依据：CL Sep1公告；v1 Aug30 03:32:13UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：联合29034写Ch5同一机制段，独立写后通过，不重复增补。归属 `WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)。

### [Q-Strata](https://arxiv.org/html/2608.30564v1)

root直接核exact§3.1–3.3、4.1与Limitations。inner ILP只解可加block proxy，outer assembled-model objective非可加，lazy需未获保证的DR条件、不是全局最优。共享GPTQ格式不消除rotation/RFT差异，离线search不能当推理开销。Ch49校准、组合artifact与实际执行质量验收已承载主要判断，NoChange通过，不写两层优化普遍保证。

事件依据：LG Sep1公告；v1 Aug31 10:39:01UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch49 expert校准、physical palette与部署质量。归属 `INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)。

### [TuringLLM](https://arxiv.org/html/2608.30567v1)

root直接核exact§2.4/5.2及两种impact。population quantile只控期望fanout；pretrain dropless防packed未来token竞争，完整prompt的capacity截断是另一执行分支。capacity实验多指标有退化，latency对照同时换routing/capacity，不独立归因且非实机VLA安全。Ch21 cutoff/fanout/burst/train-deploy gap当前段已覆盖，NoChange通过。

事件依据：AI Sep1公告；v1 Aug31 10:42:35UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch21 population cutoff、dropless与capacity；Ch22混合状态。归属 `MODEL-MOE`，[Ch21](../../../../books/part-02-model/21-moe.md)。

### [CARVE](https://arxiv.org/html/2608.30922v1)

独立exact §3.2/Algorithm及C–F；实际重读Ch24固定长度admission→插槽→知识树交接。坐标映射、canvas版本与对应logits绑定明确，平均JS不被写成逐位置、target distribution或延迟保证；always-expand对照的额外forward混杂留在notes。通过。

事件依据：CL Sep1公告；v1 Aug31。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch24长度admission条件分支已写，独立写后通过。归属 `MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。

### [Qwen3.8-Next](https://arxiv.org/html/2608.30320v1)

[exact](https://arxiv.org/html/2608.30320v1) §3.1独立直接实读，未认证全部架构报告。拼接前后奇异方向及shape scale改变，head与gate/up分块再合回布局；矩阵重建、owner分配和小kernel成本均在源中。实际顺读Ch28 Matrix-aware Step及参数化/optimizer symmetry相邻内容，新两句只补数学operator与物理fusion边界，非普遍性能或收敛保证。通过。

事件依据：CL Sep1公告；v1 Aug31 06:35:07UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch28逻辑matrix/head边界与物理fusion区别已写，独立写后通过。归属 `TRAIN-PRETRAINING`，[Ch28](../../../../books/part-04-training-system/28-pretraining.md)。

### [Agentic Data Cracking](https://arxiv.org/html/2608.31082v1)

[exact](https://arxiv.org/html/2608.31082v1) §3/4/6直接实读。文档已入context后才fork有界结构提取，catalogue miss回原文，list completeness与source region显式；shared prefix并不证明旁路不争抢硬件。预热相关问题和主问账目不同，静态corpus不能证明更新/删除/ACL。Ch77“Write-time Summary→Query-conditioned Late Construction”及provenance段已覆盖预计算/逐问构建的成本分支与raw fallback；本项机会性预构建不改变该长期判断。No Change通过，不追加论文段落。

事件依据：AI Sep1公告；v1 Aug31 16:53:45UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：已有覆盖：Ch77 write-time/late-construction与provenance已有覆盖，独立绑定通过。归属 `AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md)。

### [SUN](https://arxiv.org/html/2608.31167v1)

[exact](https://arxiv.org/html/2608.31167v1) III-A/B、III-C所采监督段、III-D与IV-D/V直接实读。统一relation residual/单位/tolerance/stage snapshot编译不同消费者，不是三函数数值相同；g_ext虽不提供给LLM，却参与terminal reward，不称未用于训练的测试。最终DP3无SUN program。实际顺读Ch26 typed handoff新段及下游quality交接、notes，未将训练期程序校验外推到部署保证。通过。

事件依据：AI Sep1公告；v1 Aug31 17:59:16UTC。精确版本、关键控制与证据位置见单篇证据笔记及当前非作者复核；只采用这里列明的有限命题，不认证未采用附件、整篇定理或生产复现。

Books：整合：Ch26 canonical residual跨训练/控制短段已写，独立写后通过。归属 `MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。

## 5. 缺口与下一步

1. **普通审阅与整合待办为0**：59项已作者审阅及非作者核验；58项受限判断、1项争议。13项整合均已写后验收。以下均为本窗终态保留项，不支持正面证据、Books或无遗漏断言；材料到达时按所列身份定点重开，不再扩初筛或重复证据审读。
2. **PUFFER日期冲突**：[官方摘要](https://arxiv.org/abs/2608.28622)与[HTML v1](https://arxiv.org/html/2608.28622v1)当前均写Jul29；本地列表写Sep1。需要官方announcement/version依据，不能把提交日期或目录标签任一方直接当首次公开结论。
3. **reward-seeker首次公开时刻**：[官方companion](https://alignment.anthropic.com/2026/reward-seeker/)正文可读，但仅有August月份；Aug31被安全公告链接不能证明当时首发。需要官方RSS/frontmatter/发布metadata，建议`anthropic-reward-seeker-first-public.json`；不计入59项确定准入队列，不跨月扩查。
4. **Parametric Multimodal User Memory日期冲突**：[官方abs](https://arxiv.org/abs/2608.28609) v1为Jul08 10:46:45UTC，[HTML v1](https://arxiv.org/html/2608.28609v1)亦写Jul08，与Sep1列表冲突。需要同一identity的官方announcement/revision依据；不计入59项队列，不扩七月，不把已读开头当本日Evidence完成。
5. **Layer Skipping测量冲突**：[2608.28846v1](https://arxiv.org/html/2608.28846v1)需要作者更正Table2/3与正文排序、pure/total分界，以及同query序列的同步时间日志/搜索state复用配置；建议`2608.28846v1-timing-correction.md`或对应官方commit。现有相互冲突的值无法唯一支持速度结论，已停止该结论写入。

6. **Google两项首次公开日期**：[Securing Multi-Agent Systems](https://research.google/pubs/securing-multi-agent-systems-an-empirical-analysis-of-security-prompt-hardening-and-residual-risks/)与[HCRG code migration](https://research.google/pubs/beyond-vector-similarity-hierarchical-context-aware-graph-rag-vs-standard-rag-in-enterprise-code-migration/)只有年份字段；Sep04首次成功读取不证明当时首次公开，也不能排除本窗。需匹配标题的官方定时发布记录、arXiv/DOI原身份或此前公开快照，建议`google-116-118-first-public.json`；共享定点恢复已列失败与排除项，不重复索取或扩扫全年。
7. **浑元Research完整目录**：[官方入口](https://hunyuan.tencent.com/research)用户截图确认存在“全部”列表且顶项Aug28，但当前工具仍取不到卡片身份/链接；需可读取的目录API、完整HTML或包含日期和链接的官方导出，建议`hunyuan-research-listing.html`。只恢复目录后按本窗筛选，不把空响应或截图顶部视作已完整枚举。当前重试及共享结果见中国来源记录。

已关闭的初筛缺口：`2202.06853`本轮从官方abs恢复完整题摘，为North Carolina医疗设施患者流动的传统ABM，不是LLM Agent研究；只有2022年v1/v2，本窗AI列表明确cross-list。`2608.21719` PowerSlider本窗AI列表明确cross-list from cs.DC、主分类本日列表无新项，官方历史仅Aug22的v1，不是本窗重要修订；不为该晚交叉上架重新评分或展开全文。MiMo/MiniMax先前的目录日期读取问题已由原始字段恢复，见共享检查。

## 6. 复核

复核者：`/root/screen_sep02`完成62/62题摘准入；`/root`完成本轮59项采用范围、实际Books承载和13项整合写后核验。见准入记录、早批证据与写后记录及本轮独立复核。

结论：通过

可执行的单篇审阅与Books落实已完成。中心争议和日期/来源限制均已明确隔离，不用于正面证据、Books或无遗漏断言，并保存定点重开条件，因此本窗闭环通过。初筛复核不替代证据；非作者只核采用范围，不冒充所有附件复现。此前721项分母和评分不沿用。
