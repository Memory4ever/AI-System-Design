# Daily Research — 2026-06-09

**规范：** V3
**窗口：** 2026-06-08T09:00:00+08:00 ～ 2026-06-09T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-26T01:48:10+08:00
**窗口说明：** 用户授权仅补遗漏，保留旧候选日期、评分、小时窗与有效证据；旧窗口不迁移。
**补充窗口：** 2026-06-08 ～ 2026-06-08

## 1. 结论

本轮按Jun08北京时间自然日补每日来源，最终52个唯一家族＝旧n-days整合1项＋新增实际整合43项＋具体已有覆盖7项＋中心争议暂缓1项。52项均已完成各自所需审阅与处置，43项新增正文均实际保存并经root唯一非writer写后复核；审阅完成不等全部原主张成立。有限发现与题摘贡献分层已停止，不把1022导航、261主题命中或95份题摘缓存转为全量审阅队列。普通研究/写入/独立复核待办为0，root已通过完整日级验收；外部目录、日期缺口与中心争议仍隔离，不授其Coverage/Evidence通过。原件、具体筛选/改判与必要证据见[本轮补充记录](../_sources/daily-20260609/SUPPLEMENT_20261025.md)。

本轮恢复一项可靠落窗的机构研究：n-days。它把已公开漏洞上的 crash PoC、原生攻击效果和完整权限链分开评价，提示补丁公开到运行实例实际修复之间的时间压力。必要机制、关键对照与反证已深入审阅；[PLATFORM-SECURITY / Ch72](../../../../books/part-06-ai-infrastructure/72-security.md#生命周期威胁)已实际补入两个连贯段落，并经非作者来源到实际 owner、写后及邻接复核通过。不把最快受控试验写成典型生产攻击时延或全链攻击概率。

旧2026-10-01小时窗恢复当时确定1个唯一家族、深入/整合1项，非作者验收通过、普通待办为0；此为历史完成事实，不是本轮新增层现状。旧4项读核心后贡献前关闭（OpenAI三项及暂缓的biology研究）的有效依据保留，不因厂商名或应用热度准入。新贡献涵盖可学性条件、表示/生成接口、数据与训练目标、运行时控制及评价盲区；局部理论与小模型并未因缺工业LLM消费者被排除，成熟组合与单域recipe也未仅因能映owner入选。

旧报告曾将112个arXiv工作家族整体隔离于日期门；原具名记录保留。本轮已用合法Jun08组合日证恢复的同ID以当前表为准，其余仍是日期缺口，不能据旧完成标签称112项审阅/Books通过。旧1,235个宽发现身份不是本轮强制全文队列；旧题摘、必要证据、11处真实书稿及2处中央争议均保留在[本日唯一恢复材料](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)。日期问题不自动推倒其他有效机制，但它们不能据旧时间推定算成本日报采用。原报告全文已在同一材料中保存，未经本轮验收的旧评分和完成标签不再作为现状。

## 2. 来源覆盖

旧小时窗的来源/原始字段保留在[原恢复材料](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md)；下表反映本轮 Jun08 BJT 自然日的实际补查，不以当前目录证明历史绝无删除项。完整查询/原件及停止说明见[本轮材料](../_sources/daily-20260609/SUPPLEMENT_20261025.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方RSS](https://openai.com/news/rss.xml)实际按Jun07 16Z至Jun08 16Z取3项：ERA 00Z、Built 01:30Z、S-1 14Z；ERA读官方核心后贡献前关闭，后两项复用旧有效层；前后界不读窗外正文 | 已检查 | RSS当前保留不证明删除项 |
| SRC-ANTHROPIC | [Research listing page2](https://www.anthropic.com/listing/research/default/2)原HTML hydration Jun08 n-days/agents-in-biology、前邻Jun05及更早；n-days旧同事件去重，biology复用范围排除 | 已检查 | 目录日字段不重算旧精确21:00；保留局限 |
| SRC-GOOGLE-AI | [DeepMind page2](https://deepmind.google/blog/page/2/)目标月段，再点官方Gemma4 12B Jun03、Europe Robotics Jun09、Sierra Leone Jun09精确日形成前后边界，不读窗外全文；[Research pubs](https://research.google/pubs/)仍只有年度/月份；Blog日目录不替Publications覆盖 | 受阻 | DeepMind可见目标相邻已查；Google Publications目标公开日仍缺；Research Blog官方年月入口本轮root实际web失败、独立curl20秒超时exit28/0bytes，无可读响应；不借前日观察推零发布。精确目录/官方具名日期到达后重开 |
| SRC-META-AI | [publication page1](https://ai.meta.com/results/?content_types%5B0%5D=publication&page=1)新访问超时/连接重置；复用旧实际可见06/29→06/05→05/27降序片段，不遍历后部乱序旧年 | 受阻 | 到期primary历史目录/公开日必要内容本次未恢复；仅旧可见片段有效，不据其授本轮覆盖或机构零。原目标日目录/具名官方事件到达时定点重开 |
| SRC-QWEN | [GET en-US](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)/[zh-CN](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN)各实际40条，全部extra.date及前后Jun01→Jun16读完，无Jun08；原响应保存 | 已检查 | extra.date与HTML公开日可能不同，不能把字段互换或覆盖未返回条目；无空参伪零 |
| SRC-DEEPSEEK | [News](https://www.deepseek.com/news/)当前可见research Jun24→Feb25、news Sep10→Apr24区段跨窗；仅metadata，不读窗外正文 | 已检查 | 未展开“查看全部”，只限可见区段，不宣称全机构零材料 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)Overview仍止2025；[kimi-code releases](https://api.github.com/repos/MoonshotAI/kimi-code/releases?per_page=100)和[kimi-cli releases](https://api.github.com/repos/MoonshotAI/kimi-cli/releases?per_page=100)各100项，前者Jun05 10:26:45Z→Jun09 03:56:11Z，后者Jun05 10:35:01Z→Jun22 12:50:45Z跨窗，仅读metadata | 受阻 | release实际片段无Jun08；Platform历史Blog目标日仍缺，不能由release推出机构零 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) publicList POST pageNum1/pageSize100/renderType0、accept-language:zh，实际total11/list11；全部publicAt/display字段读完，Jul06→May21跨窗，无Jun08；原响应保存 | 已检查 | 中文11不是旧英文9；publicAt/displayDate不同，不反推全球first-public；目录保留局限 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)实际卡片Jun16→May20目标相邻区段，停止窗前，不拿图片上传时间当公开日 | 已检查 | 仅可见卡片，更多/删除项未证明 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)page1/13、20/246，Jun11→Jun04→Jun03→May29跨窗；[Research/Blog](https://seed.bytedance.com/en/research)当前首5为Aug05→Jul07，不提供本窗历史区段；不读窗外正文 | 受阻 | 论文可见目标段已查，Blog历史目标日仍缺，两者不互相代证 |
| SRC-BAIDU-ERNIE | [Blog zh](https://ernie.baidu.com/blog/zh/)page1/2当前最晚May09及更早，停止窗前，不读page2/正文 | 已检查 | 当前保留目录不证明删除项 |
| SRC-XIAOMI-MIMO | [官网](https://mimo.xiaomi.com/)Paper8日期Jun29→Mar13；[release](https://mimo.mi.com/docs/en-US/updates/model)Jun02→Sep22无Jun08，不替blog；官方前端route元数据逐项日期及undated读完，UltraSpeed官方Jun08核心/合作方同日技术说明已必要审阅，具体NC | 受阻 | 具名UltraSpeed自然日已解决，不继续追旧09:00；其余无日期route历史公开日仍隔离，不能推出整个blog无遗漏 |
| SRC-MINIMAX | [EN Blog](https://www.minimax.io/blog)/[ZH](https://www.minimaxi.com/blog)实际Jun09→Jun01→May27跨窗；MaxProof为Jun09非补充窗；[Agent techblog](https://agent.minimax.io/docs/techblog)已实际取得页面，最新Oct22/Oct20/Oct08/Sep22等，不含目标历史段 | 受阻 | 官方Blog可见边界已查；Agent techblog历史目标日仍缺，不再称整个入口访问失败 |
| SRC-ARXIV | 正控07881核独立client-id有效后，DataCite注册窗Jun07 16Z至Jun08 15:59:59Z导航两页1000+22仅标题/类别线索，有限主题联合检索实际261；只对已见主线潜在材料读完整精确v1题摘和必要核心。同DOI/arxiv.content/findable的registered上界与唯一v1/官方日程下界组合，完整同BJT日才入选 | 已检查 | 有限发现与已见具名贡献分层/必要层已完成；跨BJT潜在项及旧112按各自原字段隔离，不把1022视全量正文队列、不用created授公开日 |

本日不扫描每周组；只打开已见候选需要的原始证据，没有扩展机构全站或旧新版本全文。外部保留项不支持正面采用或“无遗漏”；普通待办与外部缺口分开见§5。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Measuring LLMs’ impact on N-day exploits](https://www.anthropic.com/research/n-days) | 2026-06-08T21:00:00+08:00 | 补丁公开不等running fleet已修复；受限利用的准备时间改变安全交付窗口与激活验收，不能只登记新制品结束：3+2+3=8 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72生命周期威胁](../../../../books/part-06-ai-infrastructure/72-security.md#生命周期威胁)，实际两段已写、非作者写后通过 |
| [MiMo-V2.5-Pro-UltraSpeed](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) | 2026-06-08 | 低延迟执行以Experts-only FP4、SWA并行草稿与persistent engine联合控制访存/验证/launch费用，不以1000TPS本身准入：2+2+2=6 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM / [Ch49持续执行](../../../../books/part-05-inference-system/49-tensorrt-llm.md#从逐-kernel-launch-到-persistent-executor)，联合产物/执行合同；Ch48另拥有draft/verify/commit |
| [The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment](https://arxiv.org/abs/2606.06667v1) | 2026-06-08 | 共享模板K/V可承载窄微调外溢，选位参照正则与全部位置正则取舍不同，且carrier依模型变化：2+2+2=6 | 深入完成 | 整合：TRAIN-SFT / [Ch29](../../../../books/part-04-training-system/29-sft.md#catastrophic-forgetting-与能力回退)，通用缓解后两个自然段 |
| [StageFrontier: Synchronization-Aware Stage Accounting for Distributed ML Training](https://arxiv.org/abs/2606.06751v1) | 2026-06-08 | rank-local累计frontier的增量提供精确additive会计，但同粗计时不可唯一识别同步等待或并行co-critical：2+2+3=7 | 深入完成 | 整合：PLATFORM-TRACE / [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md#从请求阶段走到gpu执行证据)，Mycroft与SigmaTrace之间 |
| [PCCL: Process Group-Aware Scalable and Generic Collective Algorithm Synthesizer](https://arxiv.org/abs/2606.07019v1) | 2026-06-08 | 参与组与可用中继域分开综合collective，组外资源仍需授权与并发准入：2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING / [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，语义合同末、Alpha-Beta前两个自然段 |
| [Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws](https://arxiv.org/abs/2606.06888v1) | 2026-06-08 | 唯一数据为binding而compute-rich时，MIR额外正则及SoftQ耦合项改变优化后loss envelope，而非固定compute免费增益：2+2+3=7 | 深入完成 | 整合：WORLDVIEW-SCALING-LAW / [Ch7](../../../../books/part-01-worldview/07-scaling-law.md)，固定数据段后一自然段，不复制Ch28 |
| [The Effect of Training Task Diversity on In-Context Learning through the Lens of Low-Dimensional Subspaces](https://arxiv.org/abs/2606.06814v1) | 2026-06-08 | 受限linear-attention构造区分task span内零密度泛化与span外漂移，task标签数不等有效多样性：2+1+3=6 | 深入完成 | 整合：WORLDVIEW-LLM-INTELLIGENCE / [Ch8](../../../../books/part-01-worldview/08-why-llms-show-intelligence.md)，tangent前一自然段 |
| [Towards Tight Bounds for Streaming Attention](https://arxiv.org/abs/2606.07205v1) | 2026-06-08 | norm/precision/dimension条件下的streaming sketch推进static coreset边界，adaptive AR反馈仍是open问题：2+1+3=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT / [Ch22](../../../../books/part-02-model/22-long-context.md)，static coreset后一自然段 |
| [Sparsely gated tiny linear experts](https://arxiv.org/abs/2606.07414v1) | 2026-06-08 | factorized top-k可将专家缩为线性neuron；固定gate下线性不等整体线性，isoflop不等实际墙钟：2+1+3=6 | 深入完成 | 整合：MODEL-MOE / [Ch21](../../../../books/part-02-model/21-moe.md)，atomic vector后、树前一自然段 |
| [A Four-Condition Diagnostic Protocol for Evidence Utilization in Long-Context and Retrieval-Augmented Language Models](https://arxiv.org/abs/2606.06758v1) | 2026-06-08 | 同模型/题目四条件分离无证据先验、oracle可恢复、全文与retrieved利用，正分母/raw范围不可省：2+2+2=6 | 深入完成 | 整合：AGENT-RAG / [Ch76充分性](../../../../books/part-07-agent/76-rag.md#relevance-不等于-sufficient-context)，三分后一个自然段 |
| [RECAP: Regression Evaluation for Continual Adaptation of Prompts](https://arxiv.org/abs/2606.06698v1) | 2026-06-08 | proactive delta-only更新中shadow旧规范暴露回弹/非目标回归，full-set信息反侧不支持全部主动适配失败：2+2+2=6 | 深入完成 | 整合：AGENT-PROMPT / [Ch74可逆删除](../../../../books/part-07-agent/74-prompt.md#追加规则容易可逆地删除规则很难)，小节末一个自然段 |
| [Evidence Graph Consistency in Retrieval-Augmented Generation: A Model-Dependent Analysis of Hallucination Detection](https://arxiv.org/abs/2606.06748v1) | 2026-06-08 | 固定encoder/阈值/QA人口中图分数诊断方向按generator族反转，事后校正不是独立detector：2+1+2=5 | 深入完成 | 整合：AGENT-RAG / [Ch76幻觉](../../../../books/part-07-agent/76-rag.md#rag-不消除-hallucination)，干预成本后一个自然段 |
| [Re-Centering Humans in LLM Personalization](https://arxiv.org/abs/2606.06614v1) | 2026-06-08 | 属性抽取/当前相关/响应收益三阶段及LLM judge与外部人评共识错位，非用户本人偏好：2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY / [Ch77](../../../../books/part-07-agent/77-memory.md)，MemBubble后一个自然段 |
| [Principles of Concept Representation in Sentence Encoders](https://arxiv.org/abs/2606.06994v1) | 2026-06-08 | 监督需匹配composition-type；pair discrimination与R@K分验，ROC-AUC不等概率calibration：2+1+2=5 | 深入完成 | 整合：AGENT-RAG / [Ch76度量](../../../../books/part-07-agent/76-rag.md#度量选择先诊断几何再验收任务收益)，multi-positive后一个自然段 |
| [From Sampled Outcomes to Capability Distributions: Rethinking Supervision for LLM Routing](https://arxiv.org/abs/2606.06924v1) | 2026-06-08 | 重复改写/解码观测替代单shot路由label，均值/整体risk监督仍需语义/成本资格：2+2+2=6 | 深入完成 | 整合：PLATFORM-GATEWAY / [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md)，TRouter后/硬资格前一个自然段 |
| [On the Geometry of On-Policy Distillation](https://arxiv.org/abs/2606.07082v1) | 2026-06-08 | 早期累计位移右子空间对OPD后续训练有限充分、同约束损SFT，非通用低秩保证：2+2+2=6 | 深入完成 | 整合：TRAIN-SFT / [Ch29](../../../../books/part-04-training-system/29-sft.md)，EffOPD后一个自然段 |
| [The Fine-Tuning Trap: Evaluating Negative Transfer and the Role of PEFT in Sub-1B Mathematical Reasoning](https://arxiv.org/abs/2606.06920v1) | 2026-06-08 | 小模型recipe局部负迁移需区分regime/预算，不采用500M禁令、LoRA安全sandbox或数学分数=安全崩溃：2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-SFT / [Ch29可训练子空间](../../../../books/part-04-training-system/29-sft.md#trainable-subspace-也是-continual-sft-的评估变量)与forgetting边界 |
| [AgileOS: A GPU Operating System Layer for Protected CUDA Services](https://arxiv.org/abs/2606.06697v1) | 2026-06-08 | trusted context/API/handle/ptr/PTX保护分开，debug与unsupported路径不能冒同一隔离：2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，devicepage后一个自然段 |
| [Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://arxiv.org/abs/2606.07362v1) | 2026-06-08 | 分解engine-init CPU/weight/compile/profile/graph成本，warm cache测量不等全链coldstart：2+2+2=6 | 标准完成 | 已有覆盖：INFER-VLLM / [Ch50恢复执行状态](../../../../books/part-05-inference-system/50-vllm.md#从重建进程到恢复执行状态)，非通用CPU-bound/预测SLO |
| [MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills](https://arxiv.org/abs/2606.07131v1) | 2026-06-08 | task/instruction/script联合审查与campaign分布改变detector评判，verified恶意不等effect都成功：2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，Skill visibility后一个自然段 |
| [Breaking the Lock-in: Diversifying Text-to-Image Generation via Representation Modulation](https://arxiv.org/abs/2606.06813v1) | 2026-06-08 | 生成锁定的条件信息可由内部表示调制改变，但干预并非通用因果或全域多样性保证：2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，指定单段已实际写入并经非作者POST |
| [HKVM-RAG: Key-Value-Separated Hypergraph Evidence Organization for Multi-Hop RAG](https://arxiv.org/abs/2606.07218v1) | 2026-06-08 | 检索key与交付value可分离组织，证据聚合不等全库召回或支持已验证：2+1+2=5 | 深入完成 | 整合：AGENT-RAG / [Ch76](../../../../books/part-07-agent/76-rag.md)，指定单段已实际写入并经非作者POST |
| [Towards Retrieving Interaction Spaces for Agentic Search](https://arxiv.org/abs/2606.06880v1) | 2026-06-08 | 检索工作空间可保留可再交互的空间接口，不把静态返回文本当全部状态：2+1+2=5 | 深入完成 | 整合：AGENT-RAG / [Ch76](../../../../books/part-07-agent/76-rag.md)，指定单段已实际写入并经非作者POST |
| [Beyond Linear and Overcomplete Regimes: A Mean-Field Analysis of Bottleneck Autoencoders](https://arxiv.org/abs/2606.07120v1) | 2026-06-08 | 固定标量bottleneck的耦合mean-field学习轨迹在有限时可被SGD风险跟踪，表达存在性不等可学性：2+1+2=5 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN / [Ch4](../../../../books/part-01-worldview/04-why-models-learn.md)，指定单段已实际写入并经非作者POST |
| [Generalization in Deep Neural Networks: Minimax Rates for Gradient Methods](https://arxiv.org/abs/2606.06772v1) | 2026-06-08 | 受限光滑激活深网络GD/SGD可继承kernel统计速率，资源仍含指数深度因子：2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，指定单段已实际写入并经非作者POST |
| [Optimal Rates for Generalization of Gradient Descent Methods with Deep Neural Networks](https://arxiv.org/abs/2606.06764v1) | 2026-06-08 | ReLU深网络的有限宽kernel桥可把深度纳入高次多项式，但不等可用宽度推荐：2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION / [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，指定单段已实际写入并经非作者POST |
| [CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning](https://arxiv.org/abs/2606.07304v1) | 2026-06-08 | action-conditioned状态学习可改为结果辨别目标并行预测，而非仅重建future embedding：2+1+2=5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS / [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，指定单段已实际写入并经非作者POST |
| [Flatland: The Adventures of Gradient Descent with Large Step Sizes](https://arxiv.org/abs/2606.06722v1) | 2026-06-08 | 局部线段条件的非单调线搜索与早达最小sharpness仍优化失败修正flatness解释：2+1+2=5 | 深入完成 | 整合：WORLDVIEW-WHY-MODELS-LEARN / [Ch4](../../../../books/part-01-worldview/04-why-models-learn.md)，指定单段已实际写入并经非作者POST |
| [How Language Models Fail: Token-Level Signatures of Committed and Persistent Reasoning Failures](https://arxiv.org/abs/2606.06635v1) | 2026-06-08 | 单trace检测能力依观察窗口，事后按同曲线定义类型不等独立先验验证：2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，指定单段已实际写入并经非作者POST |
| [From Correctness to Utility: Gain-Based Prefix Evaluation for LLM Reasoning](https://arxiv.org/abs/2606.07190v1) | 2026-06-08 | 同题有无prefix的后续成功率差刻画依solver人口的utility，而非步骤正确即价值：2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，指定单段已实际写入并经非作者POST |
| [Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests](https://arxiv.org/abs/2606.07379v1) | 2026-06-08 | 隐藏独立随机cap提供作弊检测contract，低于cap不证明无作弊：2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，指定单段已实际写入并经非作者POST |
| [Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation](https://arxiv.org/abs/2606.06712v1) | 2026-06-08 | student轨迹终点为冻结AR teacher提供clean prefix，teacher与masked student条件不相同：2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，指定单段已实际写入并经非作者POST |
| [OffQ: Taming Structured Outliers in LLM Quantization by Offsetting](https://arxiv.org/abs/2606.07116v1) | 2026-06-08 | 先集中outlier方向再转组内共享offset，由非对称zero-point承接功能：2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，指定单段已实际写入并经非作者POST |
| [Your UnEmbedding Matrix is Secretly a Feature Lens for Text Embeddings](https://arxiv.org/abs/2606.07502v1) | 2026-06-08 | 冻结unembedding中段子空间可作sentence readout投影，非协方差whitening或语义无损：2+1+2=5 | 深入完成 | 整合：AGENT-RAG / [Ch76](../../../../books/part-07-agent/76-rag.md)，指定单段已实际写入并经非作者POST |
| [AdaTok: Self-Budgeting Image Tokenization with Quality-Preserving Dynamic Tokens](https://arxiv.org/abs/2606.07185v1) | 2026-06-08 | 可停止的有序图像token前缀需同时训练预算与重建资格，短前缀非无损：2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，指定单段已实际写入并经非作者POST |
| [A Held-Out Transition-Pair Falsifier for Long-Horizon Non-Abelian State Tracking](https://arxiv.org/abs/2606.07254v1) | 2026-06-08 | 非交换状态任务中的held-out转移对为长程跟踪提供定点falsifier，而非一般能力证书：2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，指定单段已实际写入并经非作者POST |
| [Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling](https://arxiv.org/abs/2606.07404v1) | 2026-06-08 | clone-family早期饥饿要求同时保function与capacity，参数复制不等稀疏训练状态连续：2+2+2=6 | 深入完成 | 整合：MODEL-MOE / [Ch21](../../../../books/part-02-model/21-moe.md)，指定单段已实际写入并经非作者POST |
| [GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios](https://arxiv.org/abs/2606.06967v1) | 2026-06-08 | 可逆增广pair的固定det支持ratio，未裁剪期望边际一致不使PPO clipping等价：2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA / [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，指定单段已实际写入并经非作者POST |
| [Don't Pause: Streaming Video-Language Synchrony for Online Video Understanding](https://arxiv.org/abs/2606.06991v1) | 2026-06-08 | 逐frame chunk仲裁继续旧句/新触发/沉默，预算截断不能追回已超deadline：2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，指定单段已实际写入并经非作者POST |
| [AsyncPatch Diffusion: spatially-flexible image generation](https://arxiv.org/abs/2606.07079v1) | 2026-06-08 | 空间noise-time tensor需共同训练覆盖均值/异质性，条件sampling不使learned路径精确：2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS / [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，指定单段已实际写入并经非作者POST |
| [SpectCount: Spectrotemporal Counting via Synthetic Signals Improves Large Audio Language Models](https://arxiv.org/abs/2606.06907v1) | 2026-06-08 | 弱点targeted纯合成音频迁移是局部数据选择证据，不以benchmark涨分独立准入：2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-DATA / [Ch27](../../../../books/part-04-training-system/27-data.md)，具体论点与边界见§4 |
| [Explicit Evidence Grounding via Structured Inline Citation Generation](https://arxiv.org/abs/2606.07130v1) | 2026-06-08 | 联合生成claim/docid/verbatim片段仍须区分格式、词面与独立support：2+1+2=5 | 标准完成 | 已有覆盖：AGENT-RAG / [Ch76](../../../../books/part-07-agent/76-rag.md)，具体论点与边界见§4 |
| [Hierarchical Certified Semantic Commitment for Byzantine-Resilient LLM-Agent Collaboration](https://arxiv.org/abs/2606.07316v1) | 2026-06-08 | 原安全/coverage命题在v2有实质纠错，合法攻击人口、谓词与实现须匹配：2+2+2=6 | 争议 | 暂缓：AGENT-MULTI-AGENT / [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，不采用中心安全/coverage与实现证明主张，见§5 |
| [When Recovery Matters: The Blind Spot of Surrogate Privacy in MLLM Editing](https://arxiv.org/abs/2606.07171v1) | 2026-06-08 | 替身图的云编辑结果还须回到private source验本地恢复，不能只验中间结果：2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，具体处置已非作者复核 |
| [Clairvoyant: Predictive SJF Scheduling to Mitigate Head-of-Line Blocking in Serial LLM Backends](https://arxiv.org/abs/2606.07248v1) | 2026-06-08 | 输出长度分类的人口支持与跨域退化限制预测式SJF，不以diagonal训练内结果授泛化：2+1+2=5 | 标准完成 | 已有覆盖：INFER-SCHEDULING / [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)，具体处置已非作者复核 |
| [Online Pandora's Box for Contextual LLM Cascading](https://arxiv.org/abs/2606.07392v1) | 2026-06-08 | query只揭output/cost，selected部署才reward，reservation index与reward evaluator须分开学习：2+2+2=6 | 深入完成 | 整合：PLATFORM-GATEWAY / [Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md)，具体处置已非作者复核 |
| [GRASP: Geometry-aware Residual Alignment for Scalable Pretraining Data Attribution](https://arxiv.org/abs/2606.06892v1) | 2026-06-08 | 子集更新向量二次交互可作重训效用surrogate，不能把文件分数直接相加：2+2+2=6 | 深入完成 | 整合：TRAIN-DATA / [Ch27](../../../../books/part-04-training-system/27-data.md)，具体处置已非作者复核 |
| [The Masked Advantage: Uncovering Local-Language Access to Cultural Knowledge in LLMs](https://arxiv.org/abs/2606.07422v1) | 2026-06-08 | 文化题语言差减文化无关题语言差提供受限访问诊断，Rasch差分非内部知识因果：2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体处置已非作者复核 |
| [Defending Jailbreak Attacks on Large Language Models via Manifold Trajectory Kinetics](https://arxiv.org/abs/2606.07335v1) | 2026-06-08 | 跨层相对anchor邻域rank可替单层坐标监控，层轴不等时间或已识别意图：2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，具体处置已非作者复核 |
| [Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning](https://arxiv.org/abs/2606.06976v1) | 2026-06-08 | 行为reward提高可使correct/wrong PPL更重叠，准确率与错误区分须分验：2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，真实保存与root§43唯一POST通过 |
| [Diagnosing Visual Ignorance in Vision-Language Models](https://arxiv.org/abs/2606.06890v1) | 2026-06-08 | 中层可读与后层prior竞争提示提取/消费不同失效面，probe不认证唯一因果：2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION / [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，具体处置已非作者复核 |
| [Translate-R1: Cost-Aware Translation Tool Use via Reinforcement Learning](https://arxiv.org/abs/2606.06835v1) | 2026-06-08 | 偶发no-tool成功会使groupcost压制必要tool，自增强反馈需惩罚资格门：2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，真实保存与root§43唯一POST通过 |

公开原字段为官方Research hydration `publishedOn=2026-06-08T13:00:00.000Z`、slug `n-days`，转为北京时间21:00，完全落窗。厂商Research列表与原实验共同支持同一家族，不重复计数。旧112层按原日期缺口保留；其中已另用合法Jun08组合日证恢复的具名同ID只在新增层计唯一家族，不搬移或重算旧archive分数。

本轮官方Jun08日历日期已支持新增自然日的UltraSpeed，不补造09:00时刻。新增arXiv均用精确v1、arxiv.content/findable的registered上界与提交/公告日程下界组成同一BJT日区间；字段、必要证据、直接反侧及具体owner差额见[本轮补充记录](../_sources/daily-20260609/SUPPLEMENT_20261025.md)。本表按唯一家族最终归并；root首备必要包由作者另一角色实际采用，不重复Methods。

## 4. 证据与知识整合

### [Measuring LLMs’ impact on N-day exploits](https://www.anthropic.com/research/n-days)

实际审阅2026-06-08官方原文Setup、Results、Figures1–5及Conclusion，精确网页版本与日期字段在[恢复材料](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)。作者控制已知漏洞、环境与成功判据：Firefox148/149已修复且公开至少90天的18个SpiderMonkey漏洞，离线Linux jsshell不是完整浏览器；漏洞/补丁build经ASan，diff去掉regression test。每模型每漏洞3 trial、每trial最多3M token。Crash只证明PoC触发，native exploit另检随机secret只在脆弱build泄露。图1取3次最快而非均值/典型时延；PoC与exploit各自最快相加未必来自同一条执行。50次一致性测试是另一个分母，不混成前组全部稳定成功。

另一实验采用21个模型cutoff后的Windows kernel CVE，WinServer2025新VM、低权限起点、离线网络、无源码、提前约2小时decompile准备；18 PoC/8完整SYSTEM链只限对应模型和协议，nonce/whoami及新编译由独立grader验证。公开模型的safeguards关闭，因此不能直接预测默认公开服务的攻击成功率。它没有测真实目标投递、evasion或完整campaign；API费用不是包括准备、人工、构建与部署的完整成本，硬件等未披露字段记Not Disclosed，Serving batch/concurrency/SLO在此不是测量对象，不写成吞吐结论。

长期可吸收的是安全交付的时间与状态差额，而非漏洞利用操作细节：实际[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md#生命周期威胁)原有identity/integrity/authorization解释生命周期边界，却没有区分patch-public、制品登记与全部running instance修复激活。新增两段接在单一WAF结论之后、匿名凭据分支之前，明确暴露窗口、运行build与剩余实例/例外、policy时限、隔离/最小权限的能力边界及canary/兼容/SLO/rollback代价，并handoff到[PLATFORM-PRODUCTION / Ch73](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)。风险还取决于可达性、权限和漏洞；受控最快时延不等生产概率。apr29_close实际亲读primary与现有owner，纠正“risk由跨度决定”后批准窄写，再独立读实际两段与相邻内容，写后通过。没有自签采用、扩大到其他漏洞附件或重写安全章。


新增层各项以下列精确原件为依据；完整必要位置、比较条件、直接反侧与实际owner差额见[本轮证据](../_sources/daily-20260609/SUPPLEMENT_20261025.md)，非作者分批实际范围见[独立复核](../_sources/daily-20260609/SUP_REVIEW_20261025.md)。没有运行artifact或复现实验，已过单篇层不预授日级完成。

### [MiMo-V2.5-Pro-UltraSpeed](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)

官方Jun08 §4.1–4.3及合作方同日说明支持experts-only FP4 QAT、其余FP8、SWA-only DFlash/GPU-local mask/block8和persistent engine的联合实现取舍。acceptance按coding/math/agent不同，普通聊天不继承；8GPU node未披露GPU SKU、长度/batch/concurrency/SLO，1200TPS demo不当可比生产保证。Ch49已有artifact/precision/sparsity与常驻执行共同编译、launch-bound/资源及fallback；Ch48另有draft/verify成本、factorization和target commit。具体已有覆盖通过，不新增产品摘要或免费无损结论。

### [The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment](https://arxiv.org/abs/2606.06667v1)

§4.2/4.3对选定模板位置K/V的base替换支持所测模型的内部载体通路，不证唯一原因；Qwen3 prefix无效/postfix有效是直接边界。§5选位base-KV正则不同于全部位置约束，后者可压制域内学习；LoRA/judge、模板版本及参照/回归全费保留。Ch29通用forgetting缓解后两个自然段已实际写并POST，不用patch/恢复率签全模型安全。

### [StageFrontier: Synchronization-Aware Stage Accounting for Distributed ML Training](https://arxiv.org/abs/2606.06751v1)

§3/4在aligned logical step、同schema、非重叠/residual-closed向量上，以累计rank duration逐stage取max再差分，telescoping只给max rank-local累计会计，不给跨host span或自动根因。(10,0)/(0,10)矩阵可对应等待或独立co-critical；异步GPU暴露、混role/prefetch须降级再查。有限DDP top2与降成同矩阵的profiler比较不授生产因果。Ch69 Mycroft/SigmaTrace之间实际两段及POST通过。

### [PCCL: Process Group-Aware Scalable and Generic Collective Algorithm Synthesizer](https://arxiv.org/abs/2606.07019v1)

root首次实际读§3–6必要，本作者另一角色采用记录并实际核当前Ch36及交接，未重复Methods。参与组不等可路由中继域，TEN/BFS路径及占用启发式不授全局最优；组外scratch/链路授权是部署推断，不是数学可达自动保证。主要性能模拟与有限MSCCL正确性分开，组数增多会耗尽可借资源。Ch36语义合同末两个自然段已POST。旧06-08 trace/DateHold及旧7分不迁移，本日合法Jun08/6分命题只计一家族。

### [Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws](https://arxiv.org/abs/2606.06888v1)

§2–4采用固定unique-data、compute不绑定时调epochs/LR/WD后的L*(N,U)损失包络及非可加容量—数据耦合，不替固定6ND预算最优点。MIR保AR目标但需两forward；72M–1.4B有限配对/留出与拟合渐近线不授frontier效率常数，NLL/ELBO也不混等。Ch7固定数据段后单段已写并POST，不在Ch28重复objective。

### [The Effect of Training Task Diversity on In-Context Learning through the Lens of Low-Dimensional Subspaces](https://arxiv.org/abs/2606.06814v1)

§4 Th1–3限定单层linear attention、Gaussian低秩任务与正交子空间、最优weights、epsilon和训练/测试prompt依次极限：span内零密度测试不等span外方向漂移。GF ansatz与GPT2合成验证不升级所有LLM的泛化定律。Ch8 tangent构造前单段已POST，保任务方向而非标签数的条件与原OOD验收。

### [Towards Tight Bounds for Streaming Attention](https://arxiv.org/abs/2606.07205v1)

Def2.1–2.2/Th2.1–2.2/7.1–7.2给norm、dimension、precision与固定query概率条件下的streaming sketch/空间界；误差按softmax与value范数缩放，不是文本正确率或通用relative-output保证。§3 adaptive AR stream仍open，更新/query费用与物理HBM不同。Ch22 static coreset后单段已POST，不授实际GPU KV淘汰或SLO。

### [Sparsely gated tiny linear experts](https://arxiv.org/abs/2606.07414v1)

§2–4 factorized top-k配rank-one linear neuron；每channel固定gate rank≤k，input-dependent gate仍使整层非线性。有限isoflop语言对照和非线性消融不等GPU墙钟，全部专家权重与dense attention仍在；TinyStories解释性不外推整网透明。Ch21 atomic-vector后/树分支前单段已POST，保原粗专家和dense回退。

### [A Four-Condition Diagnostic Protocol for Evidence Utilization in Long-Context and Retrieval-Augmented Language Models](https://arxiv.org/abs/2606.06758v1)

§4.6–4.9/6.1固定同模型/题/协议的no/full/retrieved/oracle；ONCU只在oracle高于no的正分母组解释回收收益，其余保原始无分母指标，raw越界不裁成正确率。oracle非上限、四条件非内部因果；controlled利用失败与real multi-hop检索链漏失可不同，dense/hybrid@16不普遍消除。Ch76充分性三分后单段已POST，未回填后版摘要。

### [RECAP: Regression Evaluation for Continual Adaptation of Prompts](https://arxiv.org/abs/2606.06698v1)

§2/4只测adapt得当前delta、无真实test反馈的proactive prompt更新；old spec留shadow不发solver，检查edit/删除回弹与非目标回归。四backbone/72条件适配未明显胜active-set baseline；给adapt全规则可恢复大部差额但2.8×tokens，反驳“全部主动适配不可能”的过推。Ch74可逆删除小节末单段已POST，self-play内部fit不授真实可靠。

### [Evidence Graph Consistency in Retrieval-Augmented Generation: A Model-Dependent Analysis of Hallucination Detection](https://arxiv.org/abs/2606.06748v1)

§III–VI使用固定MiniLM/阈值/QA响应集图信号，generator族的诊断方向可相反；875 test的事后方向翻转与同数据tau sweep只作解释，不是独立训练的部署gate。response二值label丢claim粒度，单域/少错误人口及embedding相近不等支持保留。Ch76 hallucination干预成本后单段已POST，不写强模型普遍反转。

### [Re-Centering Humans in LLM Personalization](https://arxiv.org/abs/2606.06614v1)

root首次必要§2–5/6/8由本作者另一角色采用：抽取属性、当前相关与响应收益分开，即使人工选属性，LLM judge偏好与三位外部标注者共识可错位；不是用户本人偏好，也不证明显式提属性的唯一因果。前两阶段训练提升不保证最终效用，英文筛选/分歧及全费保留。Ch77 MemBubble后单段已POST，不补造长期更新治理实现。

### [Principles of Concept Representation in Sentence Encoders](https://arxiv.org/abs/2606.06994v1)

root首次必要§4/5.4–5.6由本作者另一角色采用：hard negatives改善pair discrimination未改善R@K；ROC-AUC不是概率calibration。监督可利部分intersective/subsective而使relational下降，modal/privative未明显获益，不混作普遍损伤；单backbone/seed及合成/规则NP不授only-if定理。Ch76 multi-positive后单段已POST。

### [From Sampled Outcomes to Capability Distributions: Rethinking Supervision for LLM Routing](https://arxiv.org/abs/2606.06924v1)

§4/5同router用重写/重复decode的均值与整体std替单shot监督；原query线上只选一模型，重复test观测不供router看。100次single-shot抽样与一次DARS、rewrite语义sanity而非保证、MATH局部退和token-price非延迟保留，全池采样/评分/重训均付费。Ch62 TRouter后单段已POST，utility不越硬资格。

### [On the Geometry of On-Policy Distillation](https://arxiv.org/abs/2606.07082v1)

§4/5早期累计位移右奇异空间投影后续gradient，有限Qwen3对照保持OPD却损SFT；objective混合比小runtime扰动更改变谱轨迹。BF16可见更新/ULP、stable rank与三gate解释不证数学零或完整因果，也不授所有蒸馏rank16。Ch29 EffOPD后单段已POST，SVD/checkpoint/teacher/rollout全费与解除约束回退近文。

### [The Fine-Tuning Trap: Evaluating Negative Transfer and the Role of PEFT in Sub-1B Mathematical Reasoning](https://arxiv.org/abs/2606.06920v1)

§2/4/5的五小模型/10K OrcaMath局部反退保留，但full/PEFT不同LR且无匹配超参sweep，Qwen各数学任务正负并存。范数次乘性不保证LoRA安全sandbox，SVAMP0不证明安全alignment崩溃，500M禁令不采用。Ch29 trainable-subspace/EvalSpec及forgetting已实际承载regime/task/budget依赖和独立回归，不改变同一长期选择，具体已有覆盖。

### [AgileOS: A GPU Operating System Layer for Protected CUDA Services](https://arxiv.org/abs/2606.06697v1)

§III/IV/V的trusted worker实际context、API/虚拟handle/live pointer核验与PTX global-access guard是设计原型，不是完整CUDA兼容或生产隔离证明。unsupported hostfallback会绕过边界，trap可需退役context，sink/remap/report不保同样隔离；host/driver可信、sidechannel/perf未证。Ch72 devicepage后单段已POST，旧06-08 DateHold/trace不迁移或双计。

### [Breaking the Ice: Analyzing Cold Start Latency in vLLM](https://arxiv.org/abs/2606.07362v1)

§2–5以v0.10.1.1/22模型/5runs测engine init，warm Linux buffer/compile cache与cold cache另测，后两profile/graph阶段GPU相关；不把整体CPU主导写成全阶段或全系统。profile混compile、nonMoE预测/环境重训、日志噪声保留；不含image/network/container、未集成生产autoscaler。Ch50已有weightcache/compile/context/runtime与readiness/restore边界，版本系数不形成新长期选择，具体已有覆盖。

### [MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills](https://arxiv.org/abs/2606.07131v1)

§3–4/Discussion区分task/instruction/script关系；3944含生成/wild/tooltest，benign只是平台筛查/热门池。IOC OR judge≥.7且PI拒绝也positive，runtime恶意标签不等effect都执行成功；300样本人工label核不授全体effect。wild被少数campaign/账户主导，OR/AND的recall-FPR取舍不证任何组合数学不可能。Ch72 Skill visibility后单段已POST，真实effect仍需独立授权，旧DateHold/trace保留不双计。


### [Breaking the Lock-in: Diversifying Text-to-Image Generation via Representation Modulation](https://arxiv.org/abs/2606.06813v1)

§3/4.1–4.2/5.1/5.5把空间token逐channel均值DC与剩余差异分开，只在早期选定block衰减均值，不做PCA或改solver。SD3.5/FLUX/SANA有限对照中，早期强于中后期但过强会破坏结构，Recall增伴Precision下降；20+20prompt选层不授任意域通用或唯一根因。层/时段/强度校准与生成回归全费；Ch24 PCA后、Self-revision前一段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [HKVM-RAG: Key-Value-Separated Hypergraph Evidence Organization for Multi-Hop RAG](https://arxiv.org/abs/2606.07218v1)

§IV/V/VI–VIII先缓存局部h-r-t tuple，再按共享bridge确定性组高阶检索key，映回原passage value；extractor confidence不是真实关系。固定candidate substrate/reader预算的多跳对照中，support覆盖增仍可F1不升，ColBERT候选重排非全库召回；cache/controller收益不能全归高阶结构。抽取、建图、检索/展开和reader全费；Ch76 tablemarker后、SI-LLM前一段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Towards Retrieving Interaction Spaces for Agentic Search](https://arxiv.org/abs/2606.06880v1)

§3/4/5.1–5.3/8每次search将BM25有限候选硬链接入per-query外置目录，跨turn追加union，top10 preview非完整集合，shell/range read可重探已导入原文。有限封闭语料的TOC/prefilter/workspace对照不完整，低API费也可伴wall timeout；未导入不等无证据，集合边界非ACL。预处理、存储、所有calls和停止成本保留；Ch76 mapmarker后、SearchWeaver前一段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Beyond Linear and Overcomplete Regimes: A Mean-Field Analysis of Bottleneck Autoencoders](https://arxiv.org/abs/2606.07120v1)

root§21首次必要包由作者实际另一角色采用：紧凸/有界/C²及宽度步长条件，时间误差增长；Th3以global最优为前提，不证全局收敛。Representable链后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Generalization in Deep Neural Networks: Minimax Rates for Gradient Methods](https://arxiv.org/abs/2606.06772v1)

平方损失、source regularity、有效维数、对称初始化及停时/宽度条件；对n,d多项式不消除Cσ^L，不授现代LLM处于lazy regime。与06764同段、不同家族。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Optimal Rates for Generalization of Gradient Descent Methods with Deep Neural Networks](https://arxiv.org/abs/2606.06764v1)

对称初始化/平方损失/regularity限定泛化速率；非对称§5只kernel浓缩，不能推广完整泛化定理。与06772同段仍各计唯一家族。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning](https://arxiv.org/abs/2606.07304v1)

§3–4的共享终点positive、动作/轨迹negative与初始视觉context+causal action queries；swap不保证真实不同物理结果，并行非递归回灌，保MPC真实闭环/全部搜索成本。representation contract末单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Flatland: The Adventures of Gradient Descent with Large Step Sizes](https://arxiv.org/abs/2606.06722v1)

§2/3/5指定历史参考线搜索，C1/下有界/紧levelset只保梯度趋零；fullbatch/MSE有限对照不授SGD/Adam或更快。完整EoS监控后、loss-field前单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [How Language Models Fail: Token-Level Signatures of Committed and Persistent Reasoning Failures](https://arxiv.org/abs/2606.06635v1)

root§26必要包实际采用；top-K logprob窗口分类非内部commit定位，SC部分增益CI跨0，保长度难度混杂/接口与追加采样费用。single-call2605-11334后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [From Correctness to Utility: Gain-Based Prefix Evaluation for LLM Reasoning](https://arxiv.org/abs/2606.07190v1)

root§26实际采用；组均值非policy-independent因果，solver加权改变排序，同prefix池比较不匹配另监督PRM预算。2605-15529后、TD前单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Do Coding Agents Deceive Us? Detecting and Preventing Cheating via Capped Evaluation with Randomized Tests](https://arxiv.org/abs/2606.07379v1)

root§26实际采用；r(E pass)非E r(pass)，case-binomial近似/多轮适应反馈不沿一次显著性，不能授GRPO收敛或普遍防作弊。ALIAS2610-29767后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation](https://arxiv.org/abs/2606.06712v1)

§4/5及Table4：student终点重随机mask与轨迹mask相近，主要收益不能独归后者；block/confidence换质量，teacher/rollout/curriculum全费，非等质量墙钟。anchor末后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [OffQ: Taming Structured Outliers in LLM Quantization by Offsetting](https://arxiv.org/abs/2606.07116v1)

§3–5保多consumer逆变换/RoPE与门控融合限制，4-bit代码另有scale/zero metadata；无实部署延迟、原生低比特支持未授。CentriQ后、RotationScope前单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Your UnEmbedding Matrix is Secretly a Feature Lens for Text Embeddings](https://arxiv.org/abs/2606.07502v1)

§3–5与A/B：压缩坐标只等已投影距离，不等原向量；proxy最优非理论上界，拒采错误identity证明，保谱窗/模型prompt及SVD重嵌入索引费用。margin marker后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [AdaTok: Self-Budgeting Image Tokenization with Quality-Preserving Dynamic Tokens](https://arxiv.org/abs/2606.07185v1)

§4.1–4.2/5/Table2先tailmask训练有序前缀，再配长度bucket的decoder轻量调制，冻结codec后枚举同图8个预算训练allocator。只tailmask会损重建、配decoder才恢复；确定枚举非每图RD最优。固定target118长度的2.1×不证明无目标图自主EOS，padding及所有budget重构/训练/下游回归都付费。2602-10934完整两段后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [A Held-Out Transition-Pair Falsifier for Long-Horizon Non-Abelian State Tracking](https://arxiv.org/abs/2606.07254v1)

§3.3–4.3/5–8禁止指定相邻有序pair训练、要求测试出现，配projection-matched反侧；被留出的跨factor pair本身可交换，非交换性由完整状态任务另验。train200/len8与百万长度有限群结果，不排全部记忆/插值；额外局部动作监督、单baseline及未公开carrier阻止架构唯一归因，2604-27340后、Kamon前单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Reversible Foundations: Training a 120B Sparse MoE through State-Preserving Scaling](https://arxiv.org/abs/2606.07404v1)

root§31实际采用§5.4–5.5/7.2–7.4；clone transcript与released drop-upcycling logs是不同证据，不能授普遍无collapse。2604-13508两段后、DOT前单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [GenPO++: Generative Policy Optimization with Jacobian-free Likelihood Ratios](https://arxiv.org/abs/2606.06967v1)

root§34机制包+作者§5/F.2补缺：小solver系数逆误差、epoch/EMA差异与有限实机分开，保pair/solver/chunk身份及全部逆算费用。09580后、DROL前单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [Don't Pause: Streaming Video-Language Synchrony for Online Video Understanding](https://arxiv.org/abs/2606.06991v1)

root§34+作者VI-A/B：PPL/pacer为代理，SR累计同步非逐帧成功率，rFPS/触发timestamp非同定义首token，保弱时间监督/固定chunk反侧及全费用。02872两段后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [AsyncPatch Diffusion: spatially-flexible image generation](https://arxiv.org/abs/2606.07079v1)

root§34+作者§3.2：共同score只更新missing/observed保持clean，ELBO印式方向未闭不作配方或证明；保路径质量/全网络费用及generation退步。09125后单段。 必要/actual owner及真实POST均经root分批独核通过；不是复现。

### [SpectCount: Spectrotemporal Counting via Synthetic Signals Improves Large Audio Language Models](https://arxiv.org/abs/2606.06907v1)

§2/3规则纯合成pulse专门覆盖AudioFlamingo3的时频计数弱点，联合encoder/LLM优于单侧、过易/难及不同模型最佳pulse条件不同。MMAU-test用于选checkpoint不作独立迁移；MMAR/MMSU/AIR-Bench未参与选点仅支持较窄迁移，SpeakerCounting反退。具体已有覆盖：Ch27 Failure-driven Curriculum、Policy-relative Sweet Spot与Coverage Contract已承载弱点targeted合成、难度/模型身份和独立迁移验收；本篇有效局部验证不产生统一音频配方。 root具体NC复核通过。

### [Explicit Evidence Grounding via Structured Inline Citation Generation](https://arxiv.org/abs/2606.07130v1)

具体已有覆盖：Ch76 visited-v-supporting/claim-level citation/独立entailment已承载；FSA保取词不保支持，重试预算、filtered人口及joint相似内生膨胀保留；不为数据集加摘要段。 root具体NC复核通过。

### [Hierarchical Certified Semantic Commitment for Byzantine-Resilient LLM-Agent Collaboration](https://arxiv.org/abs/2606.07316v1)

Jun08原v1与[Aug13精确v2](https://arxiv.org/html/2606.07316v2)重要纠错分账：v1的verdict-flip攻击被排除在honest候选组之外，core零攻击率不是语义防御；静态与rushing人口混杂，component谓词不是原ball谓词，未加gate的margin tie-break与所述修复也不等shipped实现。matched validity containment对照未显示coverage优势；typed digest存在本身不是已测贡献。作者和root已深入受影响必要域，不遍历完整v2或把Aug修订另算Jun家族。Ch82实际无依赖该v1安全正结论，不造warning段，也不冒称generic责任链已完全覆盖具体H-CSC。保6分、审阅完成、Books暂缓；中心主张不作正面证据，重开条件见§5。详见本轮记录“07316处置纠正”与root§35。

### [When Recovery Matters: The Blind Spot of Surrogate Privacy in MLLM Editing](https://arxiv.org/abs/2606.07171v1)

§3/4.1/6的source/surrogate编辑对与本地恢复；CLIP方向伪标签和同SmartEdit reference非独立隐私/因果证据，SDXL替换非隐私保证。视觉匿名化后单段，root§42真实POST。

### [Clairvoyant: Predictive SJF Scheduling to Mitigate Head-of-Line Blocking in Serial LLM Backends](https://arxiv.org/abs/2606.07248v1)

19lexicalfeatures/P(Long)；Long≥800仅4/52002与3/20000，offdiagonal52–66%，训练内diagonal不作holdout；4090/Ollama串行backlog100/5runs非一般continuous batching或τ保证。Ch56已有点估计SJF/aging及FuelGauge模型/数据/策略身份和独立校准，root§40具体NC。

### [Online Pandora's Box for Contextual LLM Cascading](https://arxiv.org/abs/2606.07392v1)

§2/3/5条件独立请求/候选、同request-output共享效用、GLM与阈值支持；期望累计regret非每请求正确/SLO，未选reward不补造。2610-30076后单段，root§42真实POST。

### [GRASP: Geometry-aware Residual Alignment for Scalable Pretraining Data Attribution](https://arxiv.org/abs/2606.06892v1)

§3/4/Limitations与A/B：sequencepool/KFAC/log压尾及product→拼接sketch为近似；单步smoothness非完整重训下界，LCB公式未恢复不采用。dev冻结/同池重训、近全删除限制及全部构建费用保留；2504-20644后单段，root§42真实POST。

### [The Masked Advantage: Uncovering Local-Language Access to Cultural Knowledge in LLMs](https://arxiv.org/abs/2606.07422v1)

§3/4/5.3/6.3–6.4/D.2的共享difficulty/翻译等难/局部独立与跨池熟练度假设；13locale/筛选约80model、题源countrycue和likelihood-v-generation混杂；θ恢复准确率非独立验证。2509-03162后单段，root§42真实POST。

### [Defending Jailbreak Attacks on Large Language Models via Manifold Trajectory Kinetics](https://arxiv.org/abs/2606.07335v1)

§3/5/6/7：benign/malicious各800、最近10benign rank、benignbank含25%伪恶意；adaptive只若干surrogate，rank不可微非鲁棒证明，ASR与TPR异分母不乘作joint风险。group monitor后单段，root§42真实POST。

### [Exploring Agentic Tool-Calling Decisions via Uncertainty-Aligned Reinforcement Learning](https://arxiv.org/abs/2606.06976v1)

§3/4.1–4.5：四action/PPL组margin系数，Fig3 IoU非ECE/Brier，policy改变正确/错误人口，关键turn标签来自读全轨迹labeler。ensemble-artifact后单段已保存，root§43唯一实际POST通过。

### [Diagnosing Visual Ignorance in Vision-Language Models](https://arxiv.org/abs/2606.06890v1)

§3.1权重层/finalnorm替换非activation，suffix层数/兼容混杂；§3.2 probe只用已答对count1–9人口训练，再跨VLMBias人口，不能推encoder充分。Ch23的2610.29241/2606.01914两完整段已承载提取vs消费、probe/干预资格与修复面选择；不声称已覆盖新count实验，root§41具体NC。

### [Translate-R1: Cost-Aware Translation Tool Use via Reinforcement Learning](https://arxiv.org/abs/2606.06835v1)

§4.3/5.3/6.3/AppC/G：N8整组内至少6个no-toolcorrect且CT非空；binomial缺CT条件，非实际fire概率/能力校准。有限λ与同训练人口反证不授所有任务collapse；judge协议、训练steps与全部tool费用保留。18037后单段已保存，root§43唯一实际POST通过。

### 贡献前关闭及窗外停止边界

[Built to benefit everyone](https://openai.com/index/built-to-benefit-everyone-our-plan)RSS06/08 01:30Z的战略/分发路线、[Confidential S-1](https://openai.com/index/openai-submits-confidential-s-1)06/08 14Z的证券公告、[Industrial policy](https://openai.com/index/industrial-policy-for-the-intelligence-age)06/09 00Z的政策建议，实际核心说明没有新增本项目机制或可改变设计的评价证据，具体贡献前关闭；不拿机构声望评分。[agents-in-biology](https://www.anthropic.com/research/agents-in-biology)13:20Z的核心是暂缓的AI for Science，保范围理由，不展开领域全文。四项均不计候选；它们的准确原始标题与URL可在恢复材料内核对。

Economic Research Exchange06/08 00Z属于新增Jun08自然日；本轮已读官方核心，经济影响研究征案/项目没有新增模型或系统机制/修正证据，故具体贡献前关闭，不再沿旧小时窗理由称窗外。Notion/Nextdoor06/09 10Z/12Z、Kimi0.11/0.12和MaxProof的精确日期在补充窗外，只作停止边界，不深读或计作本日已审重复候选。arXiv代表排除及SIGIL安全强主张实际审查、TEVI等从potential改判的核心理由保留在本轮原始记录与独核§7/§18/§24/§36；抽检不是1022全量验证。

### 旧材料的必要纠正与保留

112旧arXiv身份及原README全文保存在[唯一packet](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)。本轮纠正CHAP09751的atomic persistent transition+entry与rollback追加而非BFT真值保证；07623实际有9系统23个确定certificate probes，不能写成“没有真实模型实验”。另07881版本delay、08761 APEX4混合精度/SM成本、09686的84-Format/6Tier1范围、07631诊断干预边界也已保存。仅恢复具体必要内容，不将它们或其余未读附件冒称112篇当前Evidence全通过。

旧11处书稿实际改动有独立写后核，2中央争议的原反证仍在；这些事实不证明112事件归属当前窗。没有据日期缺口删除其他来源仍支持的正文，也不再以旧“112全部已有覆盖”覆盖本次报告状态。

## 5. 缺口与下一步

普通扫描、贡献筛选、必要审阅、owner判断、正文保存、逐项写后复核及非作者整日验收待办为0。43新增I/7具体NC/H-CSC1均已有逐项独核，代表排除及共同错误理由的受影响集合已校准，未把抽检称1022或95缓存全量验收。下列是隔离的外部/中心争议保留项，不以改名消除普通工作。

本窗外部缺口作为终态保留项隔离，不用于正面证据、Books采用或无遗漏断言；定点重开条件如下：

- 旧112层及本轮具名跨日arXiv：ID/精确版本/旧有效内容见[原packet](../_sources/daily-20260609/V3_RECOVERY_BLOCKERS.md#2026-10-01-当前日期隔离与有限恢复结果)和本轮记录。其余未恢复项不据Submitted/月份或created授公开日；可接受官方公告/正文公开快照，或研究合同认可的同DOI、arxiv.content/findable registered与唯一v1/公告日程合法组合。已经合法组合恢复的同ID只在新增层计一家族，不迁旧评分；06523/06521/06539/06529/06545/06560/06574/06564现有可能区间跨前日，未作本日确定候选或继续深读，须上界/直接公开日缩窄后才重开。不重扫旧1235或本轮1022导航身份。
- Google Research Publications公开日粒度、[Research Blog官方2026/06目录](https://research.google/blog/2026/06/)与Meta到期primary历史目标日目录：本轮实际失败与旧可见边界见§2；web与独立curl都未恢复Blog响应，不能借前日“12篇”观察推本日零。需可读目标日列表或具名官方事件/日期再定点重开，不以Blog代Pubs。
- Kimi Platform Blog、Seed Blog、MiMo无日期route及MiniMax Agent techblog的历史目标段仍缺。可接受目标区段原始列表/准确官方事件与可核公开日期；只重开相应段。UltraSpeed自然日已解决，不再为旧09:00追加请求；Qwen、Hunyuan和其他可见边界的实际已查结论不被本段静默撤回，也不因此获得全站无遗漏保证。
- H-CSC 07316：中心安全、coverage和证明/实现匹配主张已因当前官方v2纠错隔离，不用于正面证据或Books。重开需相同人口下合法攻击进入实际被测分支、ball/组件谓词及gate/修复实现一致，另有独立验证；typed digest存在或版本号变化不够。原6分与已读有效证据保留，撤回主张不等整篇arXiv撤回。

材料到达前保持明确隔离；本次普通工作完成后可达安全终态，但不会宣称全部Coverage/Evidence通过。没有自动重开相邻日报、Weekly或其他月份。

## 6. 复核

复核者：root（本轮新增层的独立非作者；作者supp_jun09）。[实际记录§1–43](../_sources/daily-20260609/SUP_REVIEW_20261025.md)覆盖全部新增51家族的日期/准入/必要证据/Books决定，以及43新增I实际正文、直接完整邻接与trueH2来源注；旧n-days有效深入/写后层复用apr29_close（非旧作者）既成验收。root实际检查查询范围/主题边界，纠正理论/小模型及明确目标增量的共同false-negative，仅重开受影响集合；SIGIL安全强主张和H-CSC官方实质纠错单独处理。其余排除按来源/主题/理由分层抽检，具名范围见§7/18/24/31/36/41，不称全部缓存验证。

结论：通过

root已实际检查当前六部分、52唯一候选及对应证据/处置、14来源和停止范围，并复用全部有效必要/实际POST，完整日级验收见[§44](../_sources/daily-20260609/SUP_REVIEW_20261025.md#44-jun09完整日级验收)。旧小时窗apr29_close只作有效历史层；本次验收没有把隔离目录/日期/中心争议变成正面证据，也不认证全网无遗漏或实验复现。

作者最终本地检查：V3校验（含本地引用存在性）通过；52个候选与52个原件证据小标题对应，14个Daily来源行齐全；限定本日Report/sources与实际整合22个Books文件的working diffcheck通过。机械归并为I44（旧1/新增43）、NC7、H1，不是原始命中或全缓存审阅量；检查不代替语义验收或复现，不声明全仓清洁。

以下仅为原小时窗既成复核范围：apr29_close当时读完正式六部分，逐行核14源、n-days原字段/评分/primary/Ch72两段及四项机构排除；其普通0与安全终态是旧范围事实。本轮原窗口、旧分数/日期和archive有效证据均保留，旧完成声明未沿用。当前V3/本地引用与限定diffcheck结果附本轮最终交接；这些只检查可判定一致性，不替代root语义验收。未stage、commit或push。
