# Daily Research — 2026-09-22

**规范：** V3  
**窗口：** 2026-09-21T09:00:00+08:00 ～ 2026-09-22T09:00:00+08:00  
**状态：** 完成
**Books：** 纳入本次  
**检查时间：** 2026-10-01T00:34:35+08:00

## 1. 结论

本窗公开批次是 arXiv recent Tue22→2026-09-22 08:00 北京时间。1746个身份发现线索=1003 New+183 Cross-only+560 Replacement-only，不是贡献候选或逐项深审分母。旧暂列68中的67个v1归09/21；原误置09/23的38个家族已将有效单篇证据及33项既有Books整合、5项已有覆盖迁入本日报，日期校正不推倒未变化的机制证据，也不继承旧Complete。H-Spec先在Harvard网页09/22 03:00公开核心机制，同日arXiv只是证据升级，独立家族计1。最初42工作池处理理论、Cross、重要revision、版本正确性及MiMo后为53家族；非作者同一19个分层排除样本发现7个具体漏收，局部改判并完成必要源/Books写后后，最终冻结60家族，也未把1746发现变全文队列。

真正已可复用的长期判断包括数值路径身份对齐后仍须验收FP8 objective偏差、检索权重量化须配对验收证据身份、视觉artifact存储与实际像素可见性分离等；证据和具体Books位置见§4。NSP/SPLASH/SPECTRA/CKDA已实际写入Ch36/54/49/22并获root非作者写后通过，22547/23570/13718v2/MiMo及局部重开七项均已实际窄写且获sep21非作者写后通过；最终49家族实际整合、8家族具体已有覆盖、2仅报告、1中心争议暂缓。16639v2官方撤回信号已触发Ch29唯一采用段移除，相邻有效来源保留，非作者写后通过。Exactness一般必要性未证，不正面采用。作者普通扫描、审阅、Books与独立复核待办均为0，sep21最终日级独立Gate通过，日报完成；详细证据见[唯一接续包](../_sources/daily-20260922/V3_RECONCILIATION_20260930.md)、[有限独立Gate](../_sources/daily-20260922/V3_SEP21_DAILY_GATE_20260922.md)和[官方身份恢复](../_sources/daily-20260922/arxiv-recovery-20260927.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 本轮官方News RSS实际1238项，逐`pubDate`过滤本窗得5条：第三方评估09/22 00UTC、标准09/21 10UTC、Higgsfield/数学顾问12UTC、Academy07UTC；前三核心说明实读后关闭，后二标题范围外；Sol/Luna与cache09/22 18/21UTC在窗后 | 已检查 | 旧机构记录漏5条，已局部补齐；第三方评估是范围/独立性原则提案，未发布新检测机制或实证；标准为治理倡议、Higgsfield为客户应用声明。Astra card仅09/22日级更正日期仍隔离，不由RSS断言card无更新 |
| SRC-ANTHROPIC | Research最新09/17；Newsroom Opus5.5公告与card仅09/22日级 | 已检查 | Opus5.5时刻不明，隔离且不评分；日级不能分配09:00两侧 |
| SRC-GOOGLE-AI | DeepMind Blog最新相关09/15、publications09/01；Research Blog09/18；Research publications 2026过滤304项只有year/venue，sort/year尝试未补日级 | 受阻 | 年级目录无法支持日级覆盖；隔离这一路，不把可见文章stop升级全机构零论文 |
| SRC-META-AI | 官方results共2980，Publication首屏日期倒序09/07、09/06；Blog最新07/27，早于窗口即停止 | 已检查 | 有界官方替代入口，不宣称所有独立仓库无变更 |
| SRC-QWEN | Research GET200约94KB SPA无可提取列表；搜索侧栏最新09/20仅旁证；[Code v0.24.3](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.3) API `published_at=09/21 14:17:28Z`，正文31PR实读后候选前关闭 | 受阻 | 动态目录隔离，不支持无遗漏；Code中JDBC/session/lease等未改变已承载的状态与权限合同 |
| SRC-DEEPSEEK | 官网News最新已辨识V4.1 Flash09/10，早于窗口停止 | 已检查 | 无当前可继续的指定入口工作，不宣称所有外部渠道绝无更新 |
| SRC-MOONSHOT | Kimi Blog最新2025/11/07；org43仓库有界release前10；CLI1.51.0 `published_at=09/21 16:02:35Z`，两个PR为CLI归档/installer入口，候选前关闭 | 已检查 | 仓库push只作有界线索，不等于全org release证明 |
| SRC-TENCENT-HUNYUAN | Research“全部”官方publicList API page1,size30,render0：total8，一页闭合；最新publicAt1787896874为08/28 | 已检查 | 复用相同列表身份/内容的可核实结果；不扩读普通仓库活动 |
| SRC-ZAI | Research动态列表索引首项08/26、08/14，只作旁证；New Released官方列表首项08/26；ZCode3.14.1/3.14.3为09/22日级 | 受阻 | Research动态列表不支持完整日级覆盖；ZCode时刻不明隔离 |
| SRC-BYTEDANCE-SEED | Research/Blog与public papers最新可见08/18，早于窗口停止 | 已检查 | 约定模型/系统主题；不扩入暂缓的AI for Science |
| SRC-BAIDU-ERNIE | 博客共2页，倒序第一页05/09、04/30即止；指定ERNIE release最新06/30 | 已检查 | 官方指定入口闭合；不将全Paddle org push视作模型发布 |
| SRC-XIAOMI-MIMO | Paper完整1–8最新06/29；Blog01–14新V2.6仅09/22日级；MiMo-Code2456/2463/2455 PR API与核心代码实读，均本窗；0.1.15 release晚于本窗 | 受阻 | 模型公告日期隔离，不借Code时刻回填；工具控制family必要源/owner非作者通过，已写Ch78且非作者写后通过 |
| SRC-MINIMAX | 中英Blog完整列表最新08/13；Code0.5.1 `published_at=09/21 11:01:44Z`，全文仅构建/checksum/Node22 Linux/macOS离线测试，候选前关闭 | 已检查 | 安装包与测试声明不等于新模型机制或本地复现实验 |
| SRC-ARXIV | 十二目标分类官方Tue22 New/Cross/Replacement公告，1746去重身份线索；既有主题/同义词查询、有界相关标题补检与分页停止点见原始恢复§7.1–7.8 | 已检查 | 宽列表不作全学科逐项审阅；5首发日期待定隔离，具名重要修订处置及必要非作者核已完成；不将silent Replacement当全正文已读 |
| 表外：[Harvard Systems Group](https://systems.seas.harvard.edu/seminar/2026-09-22-weifan-jiang/) | H-Spec 官方研讨会页面原始发布时间元数据为本窗 09-22 03:00 北京时间；同家族后续 [arXiv v1](https://arxiv.org/html/2609.24197v1) 用于机制审阅 | 已检查 | 元数据证明网页标注的发布时间，不证明更早渠道绝无公开 |

机构入口与停止点复用依据为[原始机构记录](../../_sources/daily-20260923/institution-screening.md)，只复用身份/内容/判断未变的单条检查，过滤其晚于本窗事件，不继承旧完成标签；本轮三个本窗release和MiMo PR另按官方API/正文核。OpenAI旧记录漏项不复用其零命中判断，本輪按[官方RSS](https://openai.com/news/rss.xml)精确pubDate与三篇核心正文局部补齐，原字段与排除理由见[接续说明](../_sources/daily-20260922/V3_RECONCILIATION_20260930.md#openai本窗漏项局部纠正)。来源隔离项不支持候选、Books或“无遗漏”断言。Weekly不在本日范围。

## 3. 候选与判断

38项单篇结果按身份/精确版本/采用命题复用；官方Tue22公告时间修正为本日08:00。H-Spec以更早官方网页03:00为事件归属。最终表冻结60个唯一家族，包含5个重要revision与MiMo同family修正；原53逐项结果有效，末7因具体漏收恢复并完成必要源→actual owner与实际写后。最终54深入完成、5标准完成、1争议；49整合/8已有覆盖/2仅报告/1暂缓。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870) | 2026-09-22T08:00:00+08:00 | FP8 比值误差可使负优势 token 被虚假下界裁剪；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md)（已落实并通过写后复核） |
| [The Undetected Damage of Quantization on Retrieval and How to Fix It](https://arxiv.org/abs/2609.24322) | 2026-09-22T08:00:00+08:00 | encoder 权重量化可损害检索 top-1 稳定性，而分类准确率/平均 nDCG 不足以验收；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)（已落实并通过写后复核） |
| [Explicit State and Resource Contracts for Low-Precision Pipeline Parallel Training under Captured Graphs](https://arxiv.org/abs/2609.23536) | 2026-09-22T08:00:00+08:00 | split-backward + FP8 捕获图需要明确隐藏数值状态、tape 世代、cache epoch 和双向 completion；3 + 2 + 2 = 7 | 深入完成 | 整合：`TRAIN-PIPELINE-PARALLEL` [Ch38](../../../../books/part-04-training-system/38-pipeline-parallel.md)（已落实并通过写后复核） |
| [Algebraic Consistency Alone Does Not Certify Temporal Structure in Latent Action Models](https://arxiv.org/abs/2609.23478) | 2026-09-22T08:00:00+08:00 | 重构诱导的特征差分可在错乱时间配对上满足代数约束，低 add/reverse error 不认证真实 action/temporal content；2 + 2 + 3 = 7 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（已落实并通过写后复核） |
| [VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning](https://arxiv.org/abs/2609.24362) | 2026-09-22T08:00:00+08:00 | 图像证据的存储身份与本次可见像素分离，active visual context 有界且可显式回读；2 + 2 + 3 = 7 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md)（已落实并通过写后复核） |
| [What Matters in Designing World Action Models: An Empirical Study](https://arxiv.org/abs/2609.24048) | 2026-09-22T08:00:00+08:00 | 将 future→action 因果读取、时间先验位置与 auxiliary objective 时序分开对照；3 + 2 + 2 = 7 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（已落实并通过写后复核） |
| [Replication Without Persistence in Hosted LLMs: Measurement Sensitivity in Action-Time Belief Evaluation](https://arxiv.org/abs/2609.22478) | 2026-09-22T08:00:00+08:00 | 将 fresh-data 复现、同 identifier 的 instrument 敏感性和跨 identifier 持久性分开；1 + 2 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Rare Event Estimation via Iterative Unalignment](https://arxiv.org/abs/2609.24969) | 2026-09-22T08:00:00+08:00 | 固定输入下原模型输出事件率与采样 proposal 分权，surrogate 不取代事件定义；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（已落实并通过写后复核） |
| [WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models](https://arxiv.org/abs/2609.23033) | 2026-09-22T08:00:00+08:00 | 共享权重的跨 token×递归深度波前将 draft/verify 同批推进，代价是跨深度 KV 流量；2 + 1 + 2 = 5 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)（已落实并通过写后复核） |
| [Multiple latent orderings better predict language model preferences](https://arxiv.org/abs/2609.22170) | 2026-09-22T08:00:00+08:00 | 固定模型的重复二选一仍可呈结构化非传递性；单一聚合排序可能漏掉可预测差异；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（已落实并通过独立写后复核） |
| [Dexterous Robot Manipulation from Human Demonstrations via Contact-Anchored Retargeting and Residual Policy Learning](https://arxiv.org/abs/2609.24093) | 2026-09-22T08:00:00+08:00 | 跨手型示教的可迁移约束可从关节轨迹改为接触次序和表面位置，目标手仍需动力学修复；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（已落实并通过独立写后复核） |
| [Shared Execution-Clock Drifting Policy for Dynamic Precision Manipulation](https://arxiv.org/abs/2609.23305) | 2026-09-22T08:00:00+08:00 | 固定控制频率下显式分离动作曲线与 chunk 内执行进度，联合对齐的代价是参数化歧义；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（已落实并通过独立写后复核） |
| [RopeFormer: Cross-Trial Adaptation from Interaction History for Dynamic Rope Manipulation](https://arxiv.org/abs/2609.23432) | 2026-09-22T08:00:00+08:00 | 物理试验重置与隐藏动力学 episode 重置不必相同，冻结 policy 可利用同条件的短历史；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（已落实并通过独立写后复核） |
| [ZoAQ: Adaptive Zeroth-Order Querying via Query-Reuse Coupling](https://arxiv.org/abs/2609.22115) | 2026-09-22T08:00:00+08:00 | 前向预算受限时复用扰动响应自适应查询，节省query不等于wall-clock收益；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)（独立复核） |
| [On Mitigation of Subliminal Learning in Large Language Models](https://arxiv.org/abs/2609.22215) | 2026-09-22T08:00:00+08:00 | 冻结base锚定的早期KL可抑制蒸馏附带trait迁移，但与目标学习存在权衡；2 + 1 + 2 = 5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)（独立复核） |
| [The Corroboration Illusion: When More News Makes LLM Forecasts Less True](https://arxiv.org/abs/2609.22246) | 2026-09-22T08:00:00+08:00 | 同源多篇检索可造成虚假交叉印证，篇数不能替代独立支持；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)、`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)（独立复核） |
| [Resist, Update, Reject: Preference Optimization Installs a Prior-Dependent Reliability Switch](https://arxiv.org/abs/2609.22359) | 2026-09-22T08:00:00+08:00 | 联合先验强度与声称来源可靠度的偏好标签，分开抵抗、更新与拒绝；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)（独立复核） |
| [FIRM-WM: State-factorized factual-interventional recurrent modeling for reward-free visual planning](https://arxiv.org/abs/2609.22816) | 2026-09-22T08:00:00+08:00 | 将目标可比较configuration与动态fiber分开，训练reset特权不延伸至部署；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)（独立复核） |
| [Are Coreset Selection Methods Worth Their Cost?](https://arxiv.org/abs/2609.22894) | 2026-09-22T08:00:00+08:00 | 共同wall-clock预算纳入数据选择全量扫描成本，修正仅比选后准确率的结论；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)（独立复核） |
| [Scout: Open-World Species Recognition on the Edge](https://arxiv.org/abs/2609.22897) | 2026-09-22T08:00:00+08:00 | 站点条件的经验证端侧类集更新减少云回退，云提名不拥有标签真值；2 + 3 + 2 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（独立复核） |
| [When Should a VLM Look? Paying Only for Visual Calls That Were Needed and Used](https://arxiv.org/abs/2609.22910) | 2026-09-22T08:00:00+08:00 | 固定调用前状态，用不看图/真实crop/随机crop分离必要性与像素增量；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md)（独立复核） |
| [Latent Telepathy: Multi-Robot Communication with Self-Supervised Perceptual Latents](https://arxiv.org/abs/2609.23269) | 2026-09-22T08:00:00+08:00 | 冻结感知latent消息的可解码性、payload有效性与接收方任务收益分别验收；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（独立复核） |
| [When Does Communication Help? Beyond Spectral Descriptions of Collective Intelligence](https://arxiv.org/abs/2609.23310) | 2026-09-22T08:00:00+08:00 | 相同通信谱不认证任务方向对齐，须核个体/社区/全局读出及分群损失；2 + 2 + 2 = 6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)（独立复核） |
| [What Can a Recurrent State Safely Forget?](https://arxiv.org/abs/2609.23366) | 2026-09-22T08:00:00+08:00 | 局部正则与可访问未来域条件下，以未来分布不变性定义可遗忘方向；2 + 1 + 3 = 6 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)（独立复核） |
| [Are Human-Aligned Models Models of Humans? A Turing-Test Gap in Preference Alignment](https://arxiv.org/abs/2609.23640) | 2026-09-22T08:00:00+08:00 | 偏好奖励与人写回答分布拟合是不同目标，非恒定奖励可造成分布张力；2 + 1 + 3 = 6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)（独立复核） |
| [Marginal Calibration Does Not Compose: Hidden Dependence in Modular Robot Navigation](https://arxiv.org/abs/2609.23731) | 2026-09-22T08:00:00+08:00 | 边际校准不合成联合未来coverage，控制提交须识别依赖或相关上界；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（独立复核） |
| [Anticipatory Robot Goalkeeping via Monotone Optimal Stopping](https://arxiv.org/abs/2609.23976) | 2026-09-22T08:00:00+08:00 | 比较立即行动与继续观察，并在强制deadline内选择提交与保守回退；2 + 2 + 3 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（独立复核） |
| [Incremental Consistency Execution for Autonomous Intelligent Systems](https://arxiv.org/abs/2609.24090) | 2026-09-22T08:00:00+08:00 | 字段依赖和保守不变域可缩小后缀重算，但副作用提交仍查最新证书；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)（独立复核） |
| [You Can Tell Who's Asking: What the Web's Questions Are Made Of, and Where They Come From](https://arxiv.org/abs/2609.24106) | 2026-09-22T08:00:00+08:00 | 网页问句occurrence、publisher类别与实际用户需求次数不能互换；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)（独立复核） |
| [When Residualization Helps an Audit: Format Effects, Slice Gains, and Their Limits](https://arxiv.org/abs/2609.24194) | 2026-09-22T08:00:00+08:00 | cross-fit格式残差化仅支持声明切片诊断，不是无损自动去偏；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（独立复核） |
| [Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation Enforcement](https://arxiv.org/abs/2609.24243) | 2026-09-22T08:00:00+08:00 | 答案准确率、CoT可监控性与局部activation干预收益可以分离；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)、`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)（独立复核） |
| [Information-Time Proximal Policy Optimization](https://arxiv.org/abs/2609.24380) | 2026-09-22T08:00:00+08:00 | 旧策略token熵作为信息时间调整trace/clip，不能等同因果credit；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-PPO [Ch32](../../../../books/part-04-training-system/32-ppo.md)（独立复核） |
| [On Emergent Capabilities and Model Merging](https://arxiv.org/abs/2609.24504) | 2026-09-22T08:00:00+08:00 | LoRA-space合并须验收未训练行为及parent/merge lineage，非全参数定理；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md)（独立复核） |
| [Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788) | 2026-09-22T08:00:00+08:00 | 冻结流式backbone的因果控制分支不读取未来帧，近正交更新减干扰；2 + 1 + 2 = 5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)（独立复核） |
| [The Copy Ceiling: An Input-Exposure Control for Ontology-Grounded Generation over Curated Corpora](https://arxiv.org/abs/2609.24885) | 2026-09-22T08:00:00+08:00 | 同matcher复制输入baseline分开暴露项恢复与模型新增推断，不是理论上界；2 + 2 + 2 = 6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（独立复核） |
| [Human-LLM Deliberation as Interactive Proof: Conditions for Verifiability Without Transparency](https://arxiv.org/abs/2609.24895) | 2026-09-22T08:00:00+08:00 | 多轮质询的条件false-accept界依赖外部可界定错误率和真实检查率；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)（独立复核） |
| [DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](https://arxiv.org/abs/2609.24976) | 2026-09-22T08:00:00+08:00 | 当前触觉条件与未来contact latent预测是不同状态合同，须分别校准；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)（独立复核） |
| [Learning Beyond What Humans Can Demonstrate](https://arxiv.org/abs/2609.24996) | 2026-09-22T08:00:00+08:00 | 示教与部署复用可执行guardrail并记录proposed/executed动作，不能声称普遍安全；2 + 3 + 2 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（独立复核） |
| [H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache](https://systems.seas.harvard.edu/seminar/2026-09-22-weifan-jiang/) | 2026-09-22T03:00:00+08:00 | 用target已提交KV的只读复用加有界recurrent summary，置换独立drafter随prefix增长的KV；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)（既有写后复核复用） |
| [NSP: Accelerating Variable-Length LLM Training via Nested Sequence Parallelism](https://arxiv.org/abs/2609.22755v1) | 2026-09-22T08:00:00+08:00 | 共享GPU上的laminar nested-SP tree分配长短序列并分层流式执行，避免disjoint-group失衡；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)（root写后通过） |
| [SPLASH: Co-Designing Sparse Attention with High-Bandwidth Flash for Efficient Long-Context Inference](https://arxiv.org/abs/2609.23816v1) | 2026-09-22T08:00:00+08:00 | 将query-dependent稀疏选择映射整页与flash plane，program后commit horizon保证单writer可见性；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)（root写后通过） |
| [SPECTRA: Adaptive Execution of Speculative Decoding on a Runtime-Reconfigurable Tiled Architecture](https://arxiv.org/abs/2609.24847v1) | 2026-09-22T08:00:00+08:00 | 同PE资源切vector/systolic kernel mode，按离线profiled recipe选择tile划分与通信；2 + 1 + 2 = 5 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)（root写后通过） |
| [Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention](https://arxiv.org/abs/2609.24797v1) | 2026-09-22T08:00:00+08:00 | signed channel reflection与单delta反射组合打开nonexpansive二维旋转，表示能力与可学习性仍分开；2 + 1 + 3 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)（root写后通过） |
| [Exactness at Inference: A Representational Criterion for Out-of-Distribution Generalization](https://arxiv.org/abs/2609.24942v1) | 2026-09-22T08:00:00+08:00 | 挑战表示近似对OOD组合的充分性，但一般necessary criterion未证且存在明确限制/反例；2 + 1 + 2 = 5 | 争议 | 暂缓：必要性未证，不正面采用、不写Books；重开条件见§5 |
| [RLVR is a Kernel, Not a Function: Statistical Inference for pass@k Crossovers](https://arxiv.org/abs/2609.22547v1) | 2026-09-22T08:00:00+08:00 | paired simultaneous bands区分可见交叉与已建立的早益晚损，conditional kernel区分同base能力下的异质变化；2 + 1 + 3 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（sep21必要源/owner及实际写后通过） |
| [VibeMemBench: Evaluating Memory Systems for Coding Agents on Real Repository Coding Tasks](https://arxiv.org/abs/2609.23570v1) | 2026-09-22T08:00:00+08:00 | reference solver下oracle验证有用的同记录仍会转移失效，memory usefulness是条件关系而非内在属性；2 + 1 + 2 = 5 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)（sep21必要源/owner及实际写后通过） |
| [HybridFlow: A 2-NFE Generative Policy for Real-Time Robotic Manipulation](https://arxiv.org/abs/2602.13718v2) | 2026-09-22T08:00:00+08:00 | 重要修订：共享average/diagonal flow的global jump→re-noise→local修正控制消融与实机；不重复评分 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)（sep21必要源/owner及实际写后通过） |
| [MiMo-Code tool-flow control #2456/#2463](https://github.com/XiaomiMiMo/MiMo-Code/pull/2456) | 2026-09-21T18:37:32+08:00 | whole-batch finish前不执行、step-local FIFO/只读重叠、失败级联取消明确admission与execution分界；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)（sep21必要源/owner及实际写后通过） |
| [Silent Failures at the 2^32 Boundary: A Technical Report on Large-Tensor Matrix Multiplication in PyTorch's Apple MPS Backend](https://arxiv.org/abs/2609.22991v1) | 2026-09-22T08:00:00+08:00 | 对09/19已公开bug新增input-wrap/11版本/shape与guard false-positive范围证据；2 + 1 + 2 = 5 | 深入完成 | 仅报告：版本/shape/dtype事实，不将单硬件probe泛化数值安全 |
| [Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents](https://arxiv.org/abs/2606.08151v4) | 2026-09-22T08:00:00+08:00 | 重要修订：R@10未优于BM25，early ranking/代理效用不能称recall或task success增益；不重复评分 | 深入完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)排名/召回/答案效用分账 |
| [Compared to What? A Human-Anchored Security Benchmark for LLM-Generated Infrastructure-as-Code](https://arxiv.org/abs/2608.28021v2) | 2026-09-22T08:00:00+08:00 | 重要修订：prompt prescriptiveness与人类corpus不匹配，不能从pooled密度推unprompted default；不重复评分 | 深入完成 | 仅报告：此版本修正受限IaC比较，未识别通用安全机制 |
| [Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents](https://arxiv.org/abs/2601.15322v3) | 2026-09-22T08:00:00+08:00 | 重要修订：历史names-only/binary fixture未测grounding，低相关不认证独立或架构取舍；不重复评分 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际过程证据/结果分账 |
| [SocialOmni: Benchmarking Audio-Visual Social Interactivity in Omni Models](https://arxiv.org/abs/2603.16859v3) | 2026-09-22T08:00:00+08:00 | 重要修订：固定gold-positive分母的coverage×条件质量暴露低响应的排名错位；不重复评分 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)Response Rate/无条件质量与reach/solve |
| [TreeSpark: Calibrated, Load-Adaptive Draft Trees for Semi-Autoregressive Speculative Decoding](https://arxiv.org/abs/2609.22098v1) | 2026-09-22T08:00:00+08:00 | 树接受率须按ancestors-accepted人口校准，抽样兄弟顺序与残余必须匹配；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)（已落实，sep21实际写后通过） |
| [Context Poisoning as Extreme-Value Attention Interference in Long-Context Language Models](https://arxiv.org/abs/2609.22101v1) | 2026-09-22T08:00:00+08:00 | faithful softmax抽象内有效干扰数给margin压力，gate还须承担recall miss；2 + 1 + 3 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)（已落实，sep21实际写后通过） |
| [A Shared Learning Rate Is Not a Neutral Control in Selective On-Policy Distillation](https://arxiv.org/abs/2609.22109v1) | 2026-09-22T08:00:00+08:00 | arm×rate与frozen scoring分开数值更新/selector反馈，修正同LR等于中性控制；3 + 1 + 2 = 6 | 深入完成 | 整合：`TRAIN-RLHF` [Ch31](../../../../books/part-04-training-system/31-rlhf.md)（已落实，sep21实际写后通过） |
| [Read-Best Is Not Steer-Best: A Probing–Steering Layer Dissociation in Omni-Modal Large Language Models](https://arxiv.org/abs/2609.22135v1) | 2026-09-22T08:00:00+08:00 | norm/random matched层扫显示probe最佳层不等于干预最佳层，跨模型控制有null；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)（已落实，sep21实际写后通过） |
| [Paragraph Boundaries Are Not White Space: Compression Depth as the Signature of Hierarchical Structure](https://arxiv.org/abs/2609.23551v1) | 2026-09-22T08:00:00+08:00 | 固定token/精确距离/random轴对照区分层级结构与mere compression；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-POSITION-ENCODING` [Ch13](../../../../books/part-02-model/13-position-encoding.md)（已落实，sep21实际写后通过） |
| [AdaMem: Adaptive Memory Token Allocation for Soft Compression in Retrieval-Augmented Generation](https://arxiv.org/abs/2609.22100v1) | 2026-09-22T08:00:00+08:00 | 共享query forward的分数分配固定memory预算，候选bank成本不随最终token消失；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)（已落实，sep21实际写后通过） |
| [Memory That Looks Forward: A Zero-Inference Prospective Term for Personal Memory Retrieval](https://arxiv.org/abs/2609.22091v1) | 2026-09-22T08:00:00+08:00 | open/resolved dated-trigger ledger离线链接转乘法rank，完美ledger不能替真实抽取；2 + 1 + 2 = 5 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)（已落实，sep21实际写后通过） |

## 4. 证据与知识整合

### [NSP: Accelerating Variable-Length LLM Training via Nested Sequence Parallelism](https://arxiv.org/abs/2609.22755v1)

`SF-2026-ARXIV-2609-22755`：官方Tue22 New事件落本日08:00，提交字段不是公开时刻。[exact-v1 PDF](https://arxiv.org/pdf/2609.22755v1) pp5–13/§3.3–6.4已实际读。旧固定SP degree简单，而dynamic-SP的disjoint GPU groups仍可能组间失衡；NSP让对齐power-of-two group形成laminar tree共享GPU，以phase队列、rank-uniform save/remat和训练入口/输出的两次layout all-to-all保留loss语义。Algorithm1 greedy tail在没有满足Btok的unit时仍选least-token unit，是目标约束不认证全部heuristic输出可行的反例；执行前容量validate/不满足时replan或回退是本书工程推断。计时限同栈64匿名NVIDIA、Qwen3MoE30/235B、2M-token iteration、192K/384K context、FSDP64，235B另EP8/CPUoptimizer，mixed dtype细项Not Disclosed，50warmup/50–100计时均值；不证明收敛、bitwise或生产故障恢复。Ch36 Attention Workload Pool后实际新增树/队列/保存合同三段，root必要源和写后非作者核通过。

### [SPLASH: Co-Designing Sparse Attention with High-Bandwidth Flash for Efficient Long-Context Inference](https://arxiv.org/abs/2609.23816v1)

`SF-2026-ARXIV-2609-23816`：官方Tue22 New落本日08:00。[exact-v1 HTML](https://arxiv.org/html/2609.23816v1)§4–8.5实际读。read-only weight是flash自然基线，KV则需query驱动选择、整页读与plane并发；mean query/centroid只是平均logit代理，不保证完整attention选择exact，per-plane cap还改变被选set。单writer等待program完成才推进horizon、step开始latch可读快照，不能延伸任意multiwriter/GC。商业HBF不可得，serving来自OpenHBF/Vidur模拟加Blackwell measured kernels；五模型BF16、128K–1M、B1–128/TP1–8性能不等于五模型实测质量，quality仅受限Llama3.1-8B/页策略。48needle、64K/10%下SPLASH.50低于dense.86，WA1.15未实测且寿命依赖uniform wear/30min retention，不能背书通用精度或五年硬件。Ch54 Persistent Near-memory后实际补page translation/commit/质量代价三段，root必要源和写后核通过。

### [SPECTRA: Adaptive Execution of Speculative Decoding on a Runtime-Reconfigurable Tiled Architecture](https://arxiv.org/abs/2609.24847v1)

`SF-2026-ARXIV-2609-24847`：官方Tue22 New落本日08:00。[exact-v1 HTML](https://arxiv.org/html/2609.24847v1)§3.1–4.4实际读。同8×8PE/64MAC控制与memory indexing在M1 vector和M>1 systolic间切换，不重载bitstream；离线FPGA-profiled costmodel选kernel tile数、MNK划分、reduce/multicast recipe，收益换来control/routing资源成本。XCVU19P100MHz、20tiles中14accelerator，受测70–774M三模型family；LUT约82%/FF79%大涨。原型MAC dtype/量化/accumulation Not Disclosed，roofline例中的32-bit weight不是实验精度；Jetson数据来自文献，不是samehardware对照。target-only和spec按同prompt/实际完成长度比较仍只支持受限kernel/系统分支。Ch49 FILCO后补same-PE mode与profiled recipe两段；root必要源、实际写后核通过。

### [Complex KDA: Understanding and Enhancing the Expressivity of Kimi Delta Attention](https://arxiv.org/abs/2609.24797v1)

`SF-2026-ARXIV-2609-24797`：官方Tue22 New落本日08:00。[exact-v1](https://arxiv.org/html/2609.24797v1)§3–6/Theorem1–5与E/G.2实际读。列状态的`A=(I-beta kk^T)Diag(alpha)`在unit-key、beta[0,2]、alpha[-1,1]下nonexpansive；signed coordinate reflection与Householder可在实数状态产生二维旋转而不加第二delta rank。齐次不扩张不保证持续forcing总state有界；有限SO(3)子群tracking表示定理不保证learnability，A5构造不能随机学会，single-layer S5反证有finite-reachability等条件。WFA beta>2/exact arithmetic是另一条件。实际signed scan变换、state/gradient还原增加接口；H100BF16 kernel计时不含projection/optimizer/finalstate，语言1.3B/100Btoken与bounded KDA接近，GRU周期任务更强且hybrid Attention配方混杂。Ch22原有delta写入几何未解释rotation分支，本次在“写入几何与时间惯性”前实际三段整合；root必要源/owner核及实际写后均通过。

### [Exactness at Inference: A Representational Criterion for Out-of-Distribution Generalization](https://arxiv.org/abs/2609.24942v1)

`SF-2026-ARXIV-2609-24942`：官方Tue22 New落本日08:00。[exact-v1](https://arxiv.org/html/2609.24942v1)§2.3/3.6/4.5/5.2–5.3/9/A.4实际读。文章把部分OOD组合失败与表示近似联系，潜在修正“插值拟合即可外推”的解释，故保留贡献候选而非因无大模型实验暗删；但作者明示criterion不是定理，一般necessary未证明。连续分析限unbounded-output regression，关系分析限free per-entity参数；normalized MLP、binding/indirection、symmetry是其承认的边界。A.4误差上界不能反推实际误差非零或必随组合增长，抵消/额外约束也未排除。root认可深入争议终态：不以该主张改写长期模型结论，不正面采用、不入Books；精确重开条件见§5。

### [H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache](https://systems.seas.harvard.edu/seminar/2026-09-22-weifan-jiang/)

`SF-2026-ARXIV-2609-24197`：Harvard 官方研讨会页面原始 HTML 同时标注 `datePublished` 与 `article:published_time=2026-09-21T15:00:00-04:00`，即北京时间 09-22 03:00，本窗内；这是网页发布时间元数据，不是 09-22 12:45 的研讨会活动时间。摘要在本窗已公开“复用 target KV + 最后位置 hidden + Mamba”的核心机制，故 同日 arXiv Tue22 New 不是该 family 的首次公开。未证明 03:00 前没有其他渠道；当前有界检查未找到更早同机制官方发布。后续[精确 v1 全文](https://arxiv.org/html/2609.24197v1) §2–5、Appendix C/D 提供完成深入审阅所需的 Method、反事实与实验细节，属于同家族证据升级，不另记新候选。传统 block-diffusion drafter 从逐位置 target hidden 投影自有 KV，条件充分但缓存随 prefix/并发增长；直接只读 target KV 省副本，却在后续 draft 位置损失接受率。本文用最后位置 hidden 初始化 Mamba 的有界 recurrent state，同时由 attention 读取已提交 target prefix KV；target 仍独占 verification、accepted prefix 与自身 KV commit。固定 backbone 消融表明两种条件信息不能简单互换；所测 Llama3.1-8B-IT、Qwen3-4B/8B、八任务与单 A100 80G 的 vLLM 并发 8–128 支持受限的 KV/吞吐收益，`C<32` 或短于约 512 输入 token 时混合 backbone 可能较慢。KV 维度、RoPE/层映射、target 版本是复用的接口代价，作者重实现的 DFlash-2 对照与缺少可锁定的 H-Spec artifact 不能证明跨集群 SLO 或独立复现。Ch48 已在并行 drafter 主线吸收“用只读已有 prefix KV + 有界 recurrent summary 换额外 KV 容量”的条件性分支，保留原 KV-injection 的低并发、短前缀和接口宽松优势；非作者对 exact-v1 及 Books 写后语义复核通过。本家族单篇复用不替代本日其他候选与来源的 V3 闭环。


### [Towards Full Pipeline FP8 Reinforcement Learning for LLMs](https://arxiv.org/abs/2609.22870)

`SF-2026-ARXIV-2609-22870`：官方 09-22 New 公告批次按 arXiv 时刻表推定 09-22 08:00 北京时间；v1 的 09-19 提交字段不能当公开时刻。已读取[精确 v1 PDF](https://arxiv.org/pdf/2609.22870v1) 的 §2–5、Figure 5/7 与相关附录，独立复核确认准入和证据范围。旧的 BF16 baseline 使数值路径最清楚，统一 FP8 rollout/training 可收窄两端不一致；论文进一步指出两端均为 FP8 时，old/current log-prob 的误差在概率比中复合，负优势 token 会被虚假下界裁剪而失去应有梯度。作者用周期性 BF16 shadow forward 估计分位数，并平衡正负更新幅度；代价是参考前向与重新校准。实验只覆盖所述 GRPO/DAPO 模型、数学/代码任务及配置，无独立多 seed 的普遍收敛证据。Figure 7 的最高 1.5 倍是排除 BF16 校准开销的离线训练阶段吞吐，不是端到端 RL 加速。相对于 Ch33 原有的 precision graph identity 段，这一材料补足“身份对齐之后 objective 仍可能失真”的下一重压力；已将机制嵌入该段，非章末论文罗列。详见[定点证据笔记](../../_sources/daily-20260923/arxiv-2609.22870-evidence.md)。

### [The Undetected Damage of Quantization on Retrieval and How to Fix It](https://arxiv.org/abs/2609.24322)

`SF-2026-ARXIV-2609-24322`：官方 09-22 New 批次按 arXiv 时刻表推定 arXiv 首次公开于 09-22 08:00 北京时间，不以 v1 提交字段断言作者其他渠道的首发。已读取[精确 v1 HTML](https://arxiv.org/html/2609.24322v1) 的 §3–6 及 A.2/A.3/A.5/A.6/A.8。论文比较的是检索 encoder 的 W4/W3 weight-only PTQ，不是索引 embedding 压缩。score 误差最多 `ε` 且 top-1/top-2 gap 至少 `2ε` 时，top-1 对该误差预算稳定；gap 小只表示有翻转风险。作者在 ViT、Qwen3-Embedding、CLIP、cross-encoder 与披露的分类/检索任务中发现分类准确率或平均 nDCG 可掩盖查询级 top-1 身份及相关证据流失，并按逐层 gap 敏感度分配精度。其 conformal 接受条件给的是同分布校准下 `P(接受且翻转) ≤ α` 的边际联合保证，不是逐请求安全证书；检索请求的小 gap 也使可接受比例偏低。论文未验证动态语料、ANN、不同硬件/并发/SLO。Ch76 已有 margin→扰动→稳定性原则，本次只补上低精度检索上线应配对验收身份、相关文档留存和 gap 分布的具体合同；详见[定点证据笔记](../../_sources/daily-20260923/arxiv-2609.24322-evidence.md)。


### [Explicit State and Resource Contracts for Low-Precision Pipeline Parallel Training under Captured Graphs](https://arxiv.org/abs/2609.23536)

`SF-2026-ARXIV-2609-23536`：09-22 `cs.DC/new` 官方公告属于本窗；v1 的 09-20 投稿时间不等于公开时间，且未发现更早作者公开事件。exact-v1 §III–VI 将 FP8 amax/scale 的 effect ordering、`TapeKey` 与物理 `TapeRef(slot,generation)`、optimizer commit 后的 cache epoch，以及 caller↔graph 双向 completion 分成四种独立关系。旧 1F1B/full-backward 在较简单的栈式生命周期下合理；拆分 `dI/dW` 且捕获图固定地址重放时，单一 token 不再证明 retained work 没有被错绑。Ch38 原有 stage schedule、activation lifetime、weight version 与 send/recv completion，此次补入这些隐藏数值/资源状态在执行层的所有权和可验证释放条件。论文实测限单节点 H800 PCIe/RTX 5880 Ada、短序列 `seq=256`、`microbatch=1` 等开销主导负载；完整 step 结果混合多项实现变化，不可将收益归因于 CUDA Graph 单项，额外显存和 setup 也不可忽略。公开代码 artifact 未核实，不宣称独立复现。详见[定点证据笔记](../../_sources/daily-20260923/arxiv-2609.23536-evidence.md)；Books 写后语义复核通过。

### [Algebraic Consistency Alone Does Not Certify Temporal Structure in Latent Action Models](https://arxiv.org/abs/2609.23478)

`SF-2026-ARXIV-2609-23478`：官方 09-22 `cs.CV` 公告落入本窗，不能以 v1 的 09-20 投稿时间机械前移。已读[精确 v1 HTML](https://arxiv.org/html/2609.23478v1) §III–V，非作者独立证据复核确认准入。旧的 action-free 视频 latent action 训练和加性约束能够低成本利用无动作标注数据，在内部测量时仍合理；问题是重构推动 `dec(z_ab)` 接近 `φ(b)-φ(a)`，差分对任意配对都近似望远镜相消，无法靠低 additivity/reversibility error 认证真实 successor 或动作内容。Proposition 1 的上界属于 decoded-space 分子，code-space 还需线性满列秩 decoder；归一化或非线性/量化 decoder 不直接由该定理保证。作者以五源域、三 seed 的无约束重构与破坏配对后重训作对照，再在自建、非 released system 的 LIBERO 仿真 pipeline 以 13 seed/每任务 50 episode 检查动作内容和 success；低代数 error 与两者未呈单调关系，但不能推论所有 latent action 方法失败或破坏配对总是有益。Ch25 已有代数 surrogate 与真实物理不同的总原则，Ch26 原句却容易把训练目标写成完成状态；本次在 Ch26 内把它改成条件命题与 architecture-matched、destroyed-pair retrain、action/outcome probe 的评价合同，保留代数指标作便宜诊断。详见[证据笔记](../../_sources/daily-20260923/arxiv-2609.23478-evidence.md)；Books 写后语义复核通过。

### [VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning](https://arxiv.org/abs/2609.24362)

`SF-2026-ARXIV-2609-24362`：官方 `cs.AI/recent` 归入 09-22 公告批次，属于本窗；`abs` 的 09-21 字段是提交时间，不能冒充公开时刻。exact-v1 §3 把视觉工具生成的 crop/mask/overlay 注册为带 ID 和 provenance 的图像 artifact，模型显式 Promote 才进入下一请求的两个 active slots，未选图的 inline payload 可驱逐而文件仍在。旧的 append-only 在短任务简单、透明，但会重复注入视觉 token；只存文件又使模型不能有针对性地重新看图。§4.2 的 1,260 样本 GPT-4.1-mini compiler-matched `2×2` 对照支持完整方案相对 auto-all 的 token 节省，但同为两槽时显式选择相对 recent-2 的准确率差异未达显著，不能把收益全部归于 Promote。七 benchmark/四模型的总体比较与 GPT-4.1-mini 302 rescue/142 regression 均属静态图像任务；本地时延只限 Qwen3.5-9B、vLLM、8×H20、TP8、并发 1，不能外推生产 SLO。Ch75 原有通用 Context/Artifact 分权，这次只补图像像素可见性的状态转换、错误选择和旧方案共存边界。详见[定点证据笔记](../../_sources/daily-20260923/arxiv-2609.24362-evidence.md)；独立证据及 Books 写后复核通过，按反馈收窄了非活跃 payload 的描述。

### [What Matters in Designing World Action Models: An Empirical Study](https://arxiv.org/abs/2609.24048)

`SF-2026-ARXIV-2609-24048`：官方 `cs.RO/recent` 归入 09-22 公告批次，属于本窗，不能把 v1 09-21 投稿字段当公开时刻。exact-v1 §III–V 不是发明第四种 WAM，而是在 matched 架构/训练条件下分开比较 future→action 路由、frozen latent 中时间关系与 policy 中时间建模、BC/IDM/FDM/VG 辅助目标。Separately trained policy 的结构差异不能证明推理期因果，作者进一步固定同一 policy 干预两个 future slot：强内容扰动下 action change <1%，时间顺序反转则导致动作/闭环成功明显下降，尤其 LIBERO-Plus OOD；这不证明未来视觉内容普遍无用。Inter-frame 与 framewise latent 在 RoboCasa-GR1 ID 和 LIBERO-Plus OOD 呈相反排序，BC+VG 在部分 OOD 视觉偏移改善、早期合训全部目标可能干扰 BC，均限于本文预算与分布。DROID 只做真实采集数据的离线动作预测，不是实机闭环成功。Ch26 原有 explicit/joint/direct 路线，本次补的是如何用同 policy 干预和 ID/OOD 切片决定实际用哪条通路，保留 direct VLA、控制器权限与预测失效回退。详见[定点证据笔记](../../_sources/daily-20260923/arxiv-2609.24048-evidence.md)；独立证据及 Books 写后复核通过。

### [Replication Without Persistence in Hosted LLMs: Measurement Sensitivity in Action-Time Belief Evaluation](https://arxiv.org/abs/2609.22478)

`SF-2026-ARXIV-2609-22478`：官方 arXiv New 批次属于本窗，v1 09-18 投稿字段不是公开时刻。exact-v1 §2–9 把三个常被混同的问题拆开：原 H 配置在新数据上能否复现、同服务标识同日改用 R 测量配置端点如何变化、共同 R 配置下后续标识是否仍保留发现。其 H/R 对照一次改变六项测量/推理配置，不能归因任一项；跨标识的 A/C 虽在同窗交错执行，release 与产品档位、交互轨迹仍同时变化，不是纯模型版本因果实验。主格 4K/16K ceiling 未实际绑定，不能声称 token-budget 效应；D cell 先于规则冻结，E/F 是探索性，不能混成相同证据等级。Ch66 已在“可复现评估身份”与“数值可复算不等于复现了同一个实验”要求锁定模型、harness、环境、scorer、cohort、调用和标注来源；本篇在单一隐藏状态游戏里提供谨慎的实例，但未改变长期设计判断。详见[定点证据笔记](../../_sources/daily-20260923/arxiv-2609.22478-evidence.md)。

### [Rare Event Estimation via Iterative Unalignment](https://arxiv.org/abs/2609.24969)

作者仓库首个可见代码提交的 2026-09-23T03:10:00+08:00 晚于本窗 arXiv Tue22→09-22 08:00 公告，不能作为更早首次公开；仓库创建时间和 commit 时间本身也不证明当时公开可见。

`SF-2026-ARXIV-2609-24969`：官方 `cs.LG/recent` 的 09-22 公告属于本窗，不能用 v1 09-21 投稿时间前移。exact-v1 §3–7 令原模型 `p` 的固定 prompt 随机续写事件率保持估计目标，用权重扰动语言模型 `q` 增加稀有事件样本，再以逐 token 似然比 `p/q` 回权；二值事件定义与训练 proposal 的可微 surrogate 分权。proposal 命中率提高不保证目标估计稳健，未覆盖的事件模式和重尾权重仍会造成极大方差。321 个实验组合限 GPT-2 Small/Gemma-2 的 token/profanity 类事件；`>800×` 只属于披露的 GPT-2 Small Token Presence 深尾、长度和误差条件，作者明确未在真实 Agent tool failure 上验证，也未给出生产 release upper bound。Ch66 原有 CEM、audit floor 与 SCARCE 上界路线，本次补的是“原模型风险率不等于 proposal 命中率”及事件、搜索与发布 authority 的分权，保留旧采样方案的适用边界。详见[定点证据笔记](../../_sources/daily-20260923/arxiv-2609.24969-evidence.md)；独立证据及 Books 写后复核通过。

### [WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models](https://arxiv.org/abs/2609.23033)

`SF-2026-ARXIV-2609-23033`：官方 arXiv 09-22 New 批次落入本窗；v1 的 09-19 Submitted 不是公开时刻，目前未找到更早可证的同机制原始发布。已读[精确 v1 全文](https://arxiv.org/html/2609.23033v1) §2–4、Appendix B/C。旧的浅递归 draft→整段完整递归验证把 state/回滚边界分清楚，在固定深度或短候选下合理；looped LM 重复读取同一共享权重，使“串行调用数”而非单 token FLOPs 形成低 batch decode 压力。该文让不同 token 处在不同递归深度的 state 同批进入同一 recurrent block：浅层继续提议，较早 token 深化到 full-depth verifier；未通过时只 flush 未提交的在途后缀。每个已提交 token 的 target 语义仍由完整深度决定，wavefront 不授权浅层直接输出。代价是宽度 `ceil(T/T_d)` 个在途位置和各自深度 KV 读取；长上下文/大 batch 会削弱权重重用收益。跨递归 KV sharing 是另外的近似分支，会让 mixed-depth 读到不同更新阶段，不能与不共享时的 exact 行为合并宣称。作者只在 Ouro-2.6B 与 Huginn-3.5B、单张 A6000、BF16、greedy、所列 Spec-Bench task、通常 batch 1/至多 1024 输入及 512 输出条件下测得整体 2.42×/3.54× 对普通 AR；Appendix B 的 CUDA Graph spot check 显示 eager baseline 含显著 launch idle，倍数不能外推已优化 engine。无共享 KV 的 FP32 100 条 GSM8K prompt token 序列匹配不等于 BF16 逐 token 重放相同，也不证明 sampling/distributed serving。Ch48 原有自推测 target commit 和 hybrid state rollback，但没有跨递归深度同权重调度与 KV 压力；已在相邻机制段补条件性路线，不把论文速度写成通用结论。

对 WFD 的深入复核再检查 §3.1 scheduler、§3.2 全接受成本式及拒绝 flush 上界、§4.3 共享 KV 的非 exact 对照与 Appendix B/C：`T_d` 增大虽提高 draft 接受率，却缩小波前并行宽度；Ouro 的 eager AR 有显著 launch idle，CUDA Graph 后相对加速缩水，不能只引用 eager 倍数。作者对无跨递归 KV 共享的 FP32 前 100 条 GSM8K prompt 观察到相同 token 序列；BF16 的 batch/reduction 重排及跨递归 KV 共享不在该保证内。论文未给本次锁定的代码 commit，也没有 sampling、分布式或生产尾延迟实验。Books 只采用“共享权重可改变 token×depth 调度边界”这一机制，不采用速度倍数作通用结论。

### [Multiple latent orderings better predict language model preferences](https://arxiv.org/abs/2609.22170)

`SF-2026-ARXIV-2609-22170`：官方 09-22 arXiv New 公告落本窗，`v1 Submitted 26 Aug` 不是首发证据，更早的作者公开正文仍待核。已读 [v1 全文](https://arxiv.org/html/2609.22170v1) §4–9：作者在七个开源权重模型、四组各 50 item 的固定模型重复 pairwise choice 中控制展示顺序、措辞和标签，观察到单一随机排序难解释的非传递性；按 item pair 整组留出的五折比较表明 mixture Bradley–Terry 对部分任务的 held-out pairwise 预测可改善。相关噪声与混合成分尚不能单独识别，部分拟合不收敛，不能把统计成分称为内部偏好电路或直接更换 RLHF 训练目标。Ch66 原有 judge 局部校准与跨群体切片，此次只补固定模型、固定候选集内的重复选择诊断，保留单一排序在稳定、近单峰条件下的价值。详见[证据笔记](../../_sources/daily-20260923/arxiv-2609.22170-evidence.md)；独立来源与写后复核通过。

### [Dexterous Robot Manipulation from Human Demonstrations via Contact-Anchored Retargeting and Residual Policy Learning](https://arxiv.org/abs/2609.24093)

`SF-2026-ARXIV-2609-24093`：官方 09-22 arXiv New 公告落本窗，`v1 Submitted 21 Sep` 不替代公告时刻。已读 [exact-v1 HTML](https://arxiv.org/html/2609.24093v1) §3.2–4.3：旧的 joint-angle retarget 在同构手型上简单，但形态差异会破坏抓取接触。作者先在模拟中恢复人类示教的接触/力，再以接触表面与时间次序约束目标手姿态，目标手 residual policy 修复动力学；四种手型和四项真实双手任务只支持该组受限条件，仍需目标手适配。高迭代 retarget 仅约 5.5 frame/s，是离线转换而非实时控制周期；作者实机反馈是关节状态与物体位姿，不证明触觉/力反馈为实验条件。Ch26 原有 latent-goal 跨本体路线，此次补的是 contact-rich 分支及其仿真误差、目标手适配和安全边界，不取代简单任务的运动学映射。详见[证据笔记](../../_sources/daily-20260923/arxiv-2609.24093-evidence.md)；独立来源与写后复核通过。

### [Shared Execution-Clock Drifting Policy for Dynamic Precision Manipulation](https://arxiv.org/abs/2609.23305)

`SF-2026-ARXIV-2609-23305`：官方 arXiv 09-22 New 公告落本窗，`v1 Submitted 20 Sep` 不能当首发时刻。已读 [exact-v1 HTML](https://arxiv.org/html/2609.23305v1) §III–V：旧 direct-output policy 也能生成非匀速动作，但时间分配隐含在逐时刻命令内。作者把 progress-indexed action curve 与从固定执行时刻映射进度的单调时钟联合生成，以示教动作变化锚定非唯一分解；20 Hz 控制接口不变，时钟每 chunk 重置。四项实机操作共 300 trial、Jetson AGX Thor 推理；同数据、预算和部署的输送带对照为固定时钟 79/100 杯、完整方案 91/100 杯，但两者同时改变可学习时钟与对齐目标，只支持联合表示。Square 模拟最终五 checkpoint 均值还低于固定时钟+MSE，不证明所有任务都受益。作者未给训练 seed 方差、生产 tail latency 或物理 deadline 保证。Ch26 在 action timing/deadline 主线增加这一受限分支，低层 controller 仍拥有执行权。详见[证据笔记](../../_sources/daily-20260923/arxiv-2609.23305-evidence.md)；独立审阅提出的旧方案措辞已修正，写后复核通过。

### [RopeFormer: Cross-Trial Adaptation from Interaction History for Dynamic Rope Manipulation](https://arxiv.org/abs/2609.23432)

`SF-2026-ARXIV-2609-23432`：官方 09-22 arXiv New 公告属于本窗，v1 的投稿字段不能作更早公开日期。已读 [exact-v1 HTML](https://arxiv.org/html/2609.23432v1) 的方法、实验和限制：同一根绳的连续试验可在规定初始条件复位后保留有限动作—观测响应历史，policy 权重不变；换绳或动力学 episode 更换时应清空上下文，训练 bootstrap 边界则仍可在每次 trial 截断。这把物理 reset、policy memory 和学习目标三种状态寿命分开。受控模拟的同权重 retain/reset 比较支持有限历史的作用，但硬件三次重复只展示可行性，没有 matched reset 对照；不能把成功提升全归因于记忆，也不能推导跨绳泛化。Ch26 原有 episode-scoped latent memory，此次补足动态物体在 trial 边界的延续条件；传感器或校准条件变化时失效旧记忆属于工程推断。详见[证据笔记](../../_sources/daily-20260923/arxiv-2609.23432-evidence.md)；独立来源及写后章节复核通过。

### [ZoAQ: Adaptive Zeroth-Order Querying via Query-Reuse Coupling](https://arxiv.org/abs/2609.22115)

反向传播仍是可微场景的低成本基线；前向评估受限时，固定查询预算又忽略迭代难度。exact-v1 通过复用扰动响应调节零阶查询，节省的 43–46% 仅相对作者四查询基线、OPT-1.3B/13B LoRA 设置，不是 wall-clock 收益；旧响应变陈旧会使方向代理偏移。Ch29 只补查询预算分支，详见[证据笔记](../../_sources/daily-20260923/arxiv-2609.22115-evidence.md)。

### [On Mitigation of Subliminal Learning in Large Language Models](https://arxiv.org/abs/2609.22215)

过滤可见文本不能证明蒸馏过程没有迁移教师的附带偏好。exact-v1 在受测模型与数字/GSM8K 蒸馏中以冻结 base 为锚、前期较强的 KL 抑制 trait 转移，但权重过大也损害目标学习，作者未识别内部作用机制。Ch29 增补训练中途 trait 轨迹与任务收益并验，不能读成通用安全防护；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.22215-evidence.md)。

### [The Corroboration Illusion: When More News Makes LLM Forecasts Less True](https://arxiv.org/abs/2609.22246)

exact-v1 在模拟语料中注入多篇同源新闻并测概率预测移动，证明“检索到多篇”不等于独立事实支持；不证明现实新闻站点已被污染。Ch76 的来源独立性、Ch72 的语料投毒与 Ch66 的概率校准已形成对应合同，故 Books 为已有覆盖；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260922246v1--伪多源新闻对概率预测的干扰)。

### [Resist, Update, Reject: Preference Optimization Installs a Prior-Dependent Reliability Switch](https://arxiv.org/abs/2609.22359)

单轴“抵抗迎合”会同时抑制可信纠错。exact-v1 的偏好标签联合先验强度与**声称**的来源可靠度，形成保留、更新、拒绝的条件分支；模型却会跟随虚假的可靠度数值，不能担当来源核验器。Ch31 补标签合同，外部证据 owner 仍验证实际 track record；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.22359-evidence.md)。

### [FIRM-WM: State-factorized factual-interventional recurrent modeling for reward-free visual planning](https://arxiv.org/abs/2609.22816)

统一视觉 latent 便于预测，却可能让外观差异污染目标比较。exact-v1 将 goal-comparable configuration 与动态 fiber 分开，并在训练期利用环境公开 reset 接口收集 action branch；Push-T 接触任务并未优于匹配基线，部署也无 simulator 特权状态。Ch25 补状态分权与受限反事实数据合同；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.22816-evidence.md)。

### [Are Coreset Selection Methods Worth Their Cost?](https://arxiv.org/abs/2609.22894)

只比较选后训练准确率会漏掉全量扫描、特征计算和排序成本。exact-v1 将选择与训练纳入共同 wall-clock 预算；其图像分类实验有 test-peak 选优和部分单 seed 边界，不能推广成“LLM 数据选择无效”。Ch27 补选择成本的摊销条件，见[证据笔记](../../_sources/daily-20260923/arxiv-2609.22894-evidence.md)。

### [Scout: Open-World Species Recognition on the Edge](https://arxiv.org/abs/2609.22897)

固定端侧类集遇到反复出现的新类时持续依赖云回退。exact-v1 采用云 VLM 提名、站点条件数据、经验证的 compact classifier 更新；云输出不拥有标签真值或部署权限。30 站点回放、Jetson Orin Nano 15W 与通信能耗估算不证明现场总体节能。Ch26 补版本化端云能力更新及断网回退；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260922897v1--端侧开放类更新)。

### [When Should a VLM Look? Paying Only for Visual Calls That Were Needed and Used](https://arxiv.org/abs/2609.22910)

工具调用发生不代表证据被使用。exact-v1 固定调用前状态，比较不看图、看真实 crop 和看随机同尺寸 crop，将调用必要性与像素信息增量分开；K 个随机参考加两条评分分支产生额外训练评估成本。Ch78 补视觉只读工具的反事实判据，不外推至有副作用的工具；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.22910-evidence.md)。

### [Latent Telepathy: Multi-Robot Communication with Self-Supervised Perceptual Latents](https://arxiv.org/abs/2609.23269)

只共享位置消息传不出他者摄像头见到的危险。exact-v1 发送冻结感知 encoder 的 64D latent 与位置锚点，接收方学习路线，但固定带宽/一步延迟实验和真机 102/102 hazard 解码都不证明真实协作任务成功。Ch26 补消息身份、payload 有效性与 receiver 行动能力的分权；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260923269v1--多机共享感知-latent)。

### [When Does Communication Help? Beyond Spectral Descriptions of Collective Intelligence](https://arxiv.org/abs/2609.23310)

相同通信谱并不保证信息方向对齐最终任务读出。exact-v1 的受控线性构造和小规模任务提示应同时验个体、社区及全局读出；社区保护实验存在严格违规，零观察违规也不是安全证明。Ch82 在协调成本之后补任务投影和分群损失合同，不推断开放式 Agent 收益；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.23310-evidence.md)。

### [What Can a Recurrent State Safely Forget?](https://arxiv.org/abs/2609.23366)

状态向量的几何相近不能认证未来行为等价。exact-v1 在局部正则、秩与可访问未来实验的条件下，定义不会改变未来条件分布的可压缩方向；有限 probe 只覆盖声明的 domain。Ch22 补“冗余状态”与“未来语义”分界，不给任意 LLM 遗忘正确性的保证；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.23366-evidence.md)。

### [Are Human-Aligned Models Models of Humans? A Turing-Test Gap in Preference Alignment](https://arxiv.org/abs/2609.23640)

“人更喜欢助手给出的回答”不等于“人自己会这样回答”。exact-v1 的 KL 正则最优形式表明非恒定偏好奖励通常改变人写回答分布，作者的受限数据实验亦观察到 preference fit 与 human-response likelihood 的张力；这不是所有实际训练必然收敛的证明。Ch31 补监督目标分岔和支持集条件；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.23640-evidence.md)。

### [Marginal Calibration Does Not Compose: Hidden Dependence in Modular Robot Navigation](https://arxiv.org/abs/2609.23731)

位置与速度各自校准不保证组合未来位置校准，因为风险还含协方差项。exact-v1 在保持边际不变的模拟中改变依赖结构，未来 coverage 显著偏移；300,000 预测样本与 30,000 闭环 trial 仍不是硬件安全认证。Ch26 补联合依赖或相关上界与控制提交的分权；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.23731-evidence.md)。

### [Anticipatory Robot Goalkeeping via Monotone Optimal Stopping](https://arxiv.org/abs/2609.23976)

固定出手时刻简单，却可能等到证据足够时已经错过拦截。exact-v1 将立即行动价值与继续观察成本比较，并受强制 deadline 约束；量化收益来自仿真，实机只是 feint 演示，理论依赖充分决策态等条件。Ch26 补等待/提交的时限取舍与保守回退；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260923976v1--观察还是出手的时间选择)。

### [Incremental Consistency Execution for Autonomous Intelligent Systems](https://arxiv.org/abs/2609.24090)

输入变化后重算整个后缀是正确但昂贵的基线；exact-v1 以字段依赖和保守不变域缩小重算，而最终外部副作用仍需核对最新 read certificate。Ch81 已明确“已知依赖缩小重算、未知依赖扩大失效”和提交前版本检查，故 Books 为已有覆盖；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.24090-evidence.md)。

### [You Can Tell Who's Asking: What the Web's Questions Are Made Of, and Where They Come From](https://arxiv.org/abs/2609.24106)

网页问句出现次数可以形成大规模训练材料，却不是实际用户需求次数。exact-v1 的 13.4B 次问句统计依赖主机标注与采样；来源分类器不认证单条问句为真人需求。Ch27 在重复数据问题后补 occurrence、publisher 与真实交互需求的分离；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.24106-evidence.md)。

### [When Residualization Helps an Audit: Format Effects, Slice Gains, and Their Limits](https://arxiv.org/abs/2609.24194)

分数与格式相关不证明格式就是无关噪声。exact-v1 的 cross-fit 残差化只在预声明切片显示局部收益，其他切片和整体对齐可能下降；Ch66 将它限定为审计诊断，而非自动“去偏”或替代原始发布分数。受控代码注释改写及其他任务边界见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260924194v1--评估分数的表面残差化)。

### [Taming CoT Obfuscation in VLMs: From Mechanistic Evidence to Activation Enforcement](https://arxiv.org/abs/2609.24243)

受测 VLM 上答案准确率和可从 CoT 观察到的证据可分离；局部 activation 干预不证明任何输出 CoT 都忠实。Ch66/Ch72 已将内部解释、监控过程、外部结果和安全保证分账，故 Books 为已有覆盖；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260924243v1--cot-可监控性与答案质量分离)。

### [Information-Time Proximal Policy Optimization](https://arxiv.org/abs/2609.24380)

token-time 折扣简单，但会让长序列终局奖励在大量低信息 token 上衰减。exact-v1 用冻结旧策略的 token 熵作为信息时间代理调整 trace 与 clipping；熵不等于因果 credit，额外计算和尺度漂移需验收。Ch32 加入条件分支，并保留普通 GAE/固定 clip 基线；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260924380v1--信息时间-ppo)。

### [On Emergent Capabilities and Model Merging](https://arxiv.org/abs/2609.24504)

只回归 adapter 明确训练的任务不足以验收合并后的未训练行为。exact-v1 在冻结 base 的 LoRA-space 合并中观察到不同保留曲线，但并非全参数合并定理；Ch59 补 parent/merge/digest lineage 及目标行为与涌现行为分账。作者测试床和 judge 限制见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260924504v1--lora-合并中的未训练行为)。

### [Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788)

双向扩散能利用未来帧但不能原样用于实时提交。exact-v1 在冻结双向和流式 backbone 上训练无未来帧泄漏的控制分支，并用近似正交更新减少干扰；单 H100 的视频编辑吞吐不等于生产 SLO。Ch24 补流式控制的因果边界，离线质量优先仍可用双向方案；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.24788-evidence.md)。

### [The Copy Ceiling: An Input-Exposure Control for Ontology-Grounded Generation over Curated Corpora](https://arxiv.org/abs/2609.24885)

输入已经完整暴露 gold item 时，恢复它不应直接算模型新增推理。exact-v1 以同一 matcher 比较原样复制输入与模型答案，获得受限的 exposure-recall 参考；冗长复制与词面判分可能误导，Copy Ceiling 不是理论上界。Ch66 补该 baseline 与净增量抵消风险；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260924885v1--copy-ceiling)。

### [Human-LLM Deliberation as Interactive Proof: Conditions for Verifiability Without Transparency](https://arxiv.org/abs/2609.24895)

多轮人机质询只有在每轮错误通过率、人的实际检查率和自然语言到形式命题映射可外部界定时才有条件性 false-accept 界；自由文本辩论不提供这些前提。Ch84 现有 independent verifier/anytime acceptor 合同已经覆盖，Books 不重复增写；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260924895v1--交互式证明的条件边界)。

### [DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](https://arxiv.org/abs/2609.24976)

当前触觉条件化与预测接触演化是两种不同状态合同。exact-v1 在特定视觉触觉手任务中预测未来 contact latent 供动作专家读取，同输入消融支持该系统内的作用；样本和硬件条件不足以证明其他本体或失败恢复。Ch25 补预测触觉的条件分支及校准/时钟边界；见[证据笔记](../../_sources/daily-20260923/arxiv-2609.24976-evidence.md)。

### [Learning Beyond What Humans Can Demonstrate](https://arxiv.org/abs/2609.24996)

不可执行的示教会污染训练，部署期再单独过滤也可能与采集分布不一致。exact-v1 的代码 Agent 根据反馈生成 `G(s,a)`，在示教与动作过滤中复用；三项真机任务每条件仅十次，且有无 guardrail 反而更好的设置，不能声称普遍安全。Ch26 补 guardrail 版本和 proposed/executed lineage，独立安全与人工接管仍保留；见[证据笔记](../../_sources/daily-20260923/arxiv-additional-evidence.md#260924996v1--示教与部署共用-guardrail)。

### [RLVR is a Kernel, Not a Function: Statistical Inference for pass@k Crossovers](https://arxiv.org/abs/2609.22547v1)

官方Tue22 Cross中精确v1的arXiv公开事件08:00落本窗；Fri18 20:03UTC投稿过cutoff只作辅助，不把Cross标签理解成旧公开。[exact-v1](https://arxiv.org/html/2609.22547v1)§3–6/8/B.4已读：同prompt paired multiplier在k间保留covariance，early lower>0且late upper<0才建立crossover；固定K/iid prompt/正方差CLT不提供任意相关prompt保证。DeepScaleR对R1-distill-Qwen1.5B、1060prompt/128答、T.6/top-p.95、新32K预算的first-loss CI11–61，截断率为实测，按假定概率修复截断的敏感性分析是反事实。相同base p对应异质post-RL q，answer-halves复验不是新prompt泛化或pretraining-scale控制。Ch66原pass@k层仅解释coverage/selector分界，未说明整条sampling-budget曲线显著性；本次在Snapshot pass@k段后实际补paired simultaneous band/conditional kernel两段；sep21必要源/owner核通过，实际写后通过。

### [VibeMemBench: Evaluating Memory Systems for Coding Agents on Real Repository Coding Tasks](https://arxiv.org/abs/2609.23570v1)

官方Tue22 Cross精确v1公开事件本日08:00，Sun20投稿不能替代。[exact-v1](https://arxiv.org/html/2609.23570v1)§3.1–3.4/4.3–4.4/5–6实读。target gold不进入记录构造，却进入offline oracle筛选：reference Deepseek-v4-flash以四seed平均outcome，在memory combinations中选最高正收益且base<1的组合，是有利选择不等于线上可得监督。五solver转移CI都跨0，11/12 memory系统不优于off，唯一+2也CI跨0；42%的retrieval pairings在memory-off下已经4/4成功，是受测配对headroom限制而非oracle ceiling，固定同记录仍有25.7% target pair受损。内容属性/粗stage标签与词面anchor低kappa不识别强因果失败比例。Ch77既有组件干预矩阵分开write/retrieve/read，本次在组件干预矩阵后实际补reference solver/target/seed验证关系和迁移失效两段；strip/random不证明instruction pollution唯一原因，sep21必要源/owner核通过，实际写后通过。

### [HybridFlow: A 2-NFE Generative Policy for Real-Time Robotic Manipulation](https://arxiv.org/abs/2602.13718v2)

重要v2由官方Tue22 Replacement公告在本日08:00公开，不重复计算家族分数。[exact-v2](https://arxiv.org/html/2602.13718v2)§III–V/TablesI–IV实际读：r=t diagonal instantaneous与fullinterval average共用MeanFlow网络，global jump→re-noise→local diagonal field是在有限采样预算中分工，不是单纯多NFE。RoboMimic同checkpoint每任务100episode，plain1/2/4/16NFE78/78/72/60，noRN24、Reflow58/ReflowRN82、ours95/95.5；re-noise衰减coarse error不证明等同training marginal，传播上界也不反推更多step必坏。real Thor、300demo共享encoder/controller/backbone的三任务PPID69/80、CT43/63等支持受限实时分支；19ms是feature-ready后动作推理、排除95ms camera，WM182/300是score非成功率，Transport82低于STEP86/DDIM88。Ch24已有路径/组合正则器却无这条两field采样分工，本次在少步组合一致性后实际补共享average/diagonal场采样分工两段；sep21必要源/owner核通过，实际写后通过。

### [MiMo-Code tool-flow control #2456/#2463](https://github.com/XiaomiMiMo/MiMo-Code/pull/2456)

官方PR API的2456 `created_at=2026-09-21T10:37:32Z`即18:37:32BJT为初次事件，2463 `16:43:55Z`即次日00:43:55为同family重要修正，均落窗；不能借后窗0.1.15 release重新计数。body、2456 gate.ts全文及[2463](https://github.com/XiaomiMiMo/MiMo-Code/pull/2463) gate/processor/flooding核心实读：finish前buffer≤16、第17取消整未执行batch，EOF/error无finish也不执行，progress不是tool执行。step/agent FIFO只read/grep/glob重叠，non-read failure或invalid name取消queued/late；optout flag使合同有条件，跨agent/guest不共享gate。已完成副作用不rollback，retrySafe=false回执提醒不能安全盲重试。Ch78 partial-record不授权执行已有覆盖，但whole-batch admission与step-local执行排序边界已在Ch78 partial-record合同后实际新增两段；2455 completed-result不重放/主actor checkpoint归现有Ch84及前窗session family，不另计。sep21必要源/owner核通过，实际写后通过，不宣称作者tests为本地复现。

### [Silent Failures at the 2^32 Boundary: A Technical Report on Large-Tensor Matrix Multiplication in PyTorch's Apple MPS Backend](https://arxiv.org/abs/2609.22991v1)

本窗Tue22 arXiv v1是对[09/19已公开Issue197636](https://github.com/pytorch/pytorch/issues/197636)的范围证据升级，不是首次漏洞。[exact-v1](https://arxiv.org/html/2609.22991v1)§3/4.3/5/6.2已读。单M2Ultra192GB/macOS27、PyTorch2.4.1–2.14共11版、f32/f16 bmm sweep与CPUf64 oracle；CUDA A100只48项control，CUDA arange自身也失败，不能当另一真值。`numel>=2^32` host guard阻481wrong也阻630correct；host-before-device chunk建议未验证device view大型storage-offset。fused SDPA的MPS实际math dispatch与CUDA不同，2.13局部修复不证明Flash/sdpa全安全。Ch49数值验收已有“已测通过≠未测正确”和故障注入具体合同，本文保留backend/version/shape/dtype与guard边界，只报告不新增书；root准入校准与sep21必要§4.3/6.2有限证据复核均通过，不将其当整日验收。

### [Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents](https://arxiv.org/abs/2606.08151v4)

本窗Tue22 Replacement重要v4纠正retrieval recall，不重复评分。[exact-v4](https://arxiv.org/html/2606.08151v4)§3/5 Tables3–7实读：50SWE-Bench file instances、BM25top50→Qwen3.6 rerank的Hit1 .78vs.58/MRR.790vs.634，但R10 .714vs.716不改善recall。2500parseable judgment、deterministic代理/模拟utility和小样本RepoBench不证明patch success或压缩机制独立收益。Ch76 Query-side段已明确排名/召回与答案支持/效用分别验收；这个纠错与当前正文一致，无采用此family的正面旧断言，Books已有覆盖，不为制造diff重复写。

### [Compared to What? A Human-Anchored Security Benchmark for LLM-Generated Infrastructure-as-Code](https://arxiv.org/abs/2608.28021v2)

本窗Tue22 Replacement重要v2修正prompt-class解释，不重复评分。[exact-v2](https://arxiv.org/html/2608.28021v2)§III-E/F/IV-B TableII及limits实读：52insecure prescriptive/33secure/15functional vs独立49/41/10仅75%一致；1196generated对634human、999size-matched pool的3.50x仍不是prompt/任务匹配的因果差。functional类密度仍高于human，幅度与分层解释对分类敏感，并非方向反转，执行明确unsafe指令不等于unprompted default。只报告本版本纠正，不给安全排名或模型默认posture背书；Ch66已有输入/输出风险、framing和judge身份合同，本文未识别额外通用安全机制，不新增Books。

### [Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents](https://arxiv.org/abs/2601.15322v3)

本窗Tue22 Replacement重要v3纠正历史解释，不重复评分。[exact-v3](https://arxiv.org/html/2601.15322v3)§1/3.1–3.4及历史表/结论实读：历史v2只capture tool names无arguments、binary fixture-label不是evidence grounding，v3 intended评价不能替过去未执行实验。4705run/21config的r=-.11还含后来排除portfolio fixture，只是历史描述，不证明独立、预测无用或架构determinisim-accuracy tradeoff。Ch66过程指令段已有self-report不能代真实trace/effect、process compliance与outcome success分账；当前无依赖此family旧强结论，Books已有覆盖。

### [SocialOmni: Benchmarking Audio-Visual Social Interactivity in Omni Models](https://arxiv.org/abs/2603.16859v3)

本窗Tue22 Replacement重要v3评价protocol/results变化，不重复评分。[exact-v3 PDF](https://arxiv.org/pdf/2603.16859v3)pp1–9/§3–4.4/Tables2–5已实际读。prefix-bounded query不测实际stream latency；128gold-positive分母下Cov=Rm/128、Quality只对TP非空、Joint=Cov×Quality使漏答0，FP仍另看when precision，不能当完整效用。GPT4o cond76.5/Cov30.47/Joint23.31与Vita49.93/88.28/44.08是coverage-quality取舍；视觉cascade与native omni也非完全匹配条件。三个固定judge的leave-family rank≤1仍不消偏，individual rank最多5、pair MAE17–28；gold/shuffled AUC只测有限construct。Ch66 Response Rate/条件和无条件质量、reach与conditional solve两处已完整承载分母分解，无需改书；不采用其通用model排名。

### 七项分层漏收的局部必要审阅

七项exact-v1完整题摘及必要方法/评价/反证已实际读，官方Tue22 New/Cross身份见原始恢复；HTML内作者稿日期或Submitted不代替本日公告时钟。得分5–6但actual长期差额已确认，按合同深入受影响内容。具体必要节号、配置/未披露项及actual owner拟两段位置见[唯一必要包](../_sources/daily-20260922/V3_RECONCILIATION_20260930.md#有限七项重开必要源--actual-owner0930恢复)，七项独立源→owner及实际两段写后均已通过，不继承旧关闭理由或自签通过：

### [TreeSpark: Calibrated, Load-Adaptive Draft Trees for Semi-Autoregressive Speculative Decoding](https://arxiv.org/abs/2609.22098v1)

`SF-2026-ARXIV-2609-22098` exact-v1 §3–6：parent Markov head、ancestors-accepted人口与draw-order residual；top-k bias反例、校准跨温度未隔离mismatch、chain fallback，A100成本模拟与H200 matched harness不合并生产收益。Ch48 VerifyLength只有一般prefix survival/预算，缺条件人口和树slot/draw-order合同；已在旧block限制后新增两段，sep21源→owner及actual Ch48:243/245写后通过。

### [Context Poisoning as Extreme-Value Attention Interference in Long-Context Language Models](https://arxiv.org/abs/2609.22101v1)

`SF-2026-ARXIV-2609-22101` exact-v1 §3/A/C/D/F：iid-Gaussian/ρ-faithful-decoder/γ logit-bound内accuracy上界及有效N；真实模型不满足分布假设，512K gate CI触0/p=.092，recall miss不被hit-subset收益掩盖。Ch22原TAM/linear memory非同定理；已在TAM后加入受限softmax压力与gate penalty两段，sep21源→owner及actual Ch22:111/113写后通过。

### [A Shared Learning Rate Is Not a Neutral Control in Selective On-Policy Distillation](https://arxiv.org/abs/2609.22109v1)

`SF-2026-ARXIV-2609-22109` exact-v1 §2–6/A/B：arm×rate、Adam displacement与frozen scoring（非冻结mask）；entropy/MATH未复现和FullFT无frozen对照，posthoc/unpaired不证明普遍selector失效。Ch31一般data/step/LR matching未承载selector直接反馈的诊断；sep21必要源→owner通过，已在22600后/23740前实际写入 Ch31:945/947 两段，sep21实际文字及邻接写后通过。

### [Read-Best Is Not Steer-Best: A Probing–Steering Layer Dissociation in Omni-Modal Large Language Models](https://arxiv.org/abs/2609.22135v1)

`SF-2026-ARXIV-2609-22135` exact-v1 III/V/VI/VIII：norm与random matched单层扫图peak-gap标准，不用未过r阈值偷换；MiniCPM多层joy null、H1/机制预测失败、judge/文本输出/小模型限制，不拿多层vs单层26x归纯位置收益。Ch23泛probe≠语义缺within-model layer选择；sep21源→owner通过，已在26411 marker后/30210前实际写入 Ch23:753/755 两段，sep21实际文字及邻接写后通过。

### [Paragraph Boundaries Are Not White Space: Compression Depth as the Signature of Hierarchical Structure](https://arxiv.org/abs/2609.23551v1)

`SF-2026-ARXIV-2609-23551` exact-v1 §3/4.3/5/7/B/C：fixed token+p1干预与exact token distance消旧bin混杂，random轴也压缩；OWT real-random CI跨0、flat小validation成本；compression depth非完整几何/下游收益。Ch13一维RoPE/连续二维身份未承载文本层级的随机轴null；sep21源→owner通过，已在RoPE例后/连续二维前实际写入 Ch13:176/178 两段，sep21实际文字及邻接写后通过。

### [AdaMem: Adaptive Memory Token Allocation for Soft Compression in Retrieval-Augmented Generation](https://arxiv.org/abs/2609.22100v1)

`SF-2026-ARXIV-2609-22100` exact-v1 Method/Eval/A–D：detached rankteacher、largest-remainder总budget、candidatebank先编码；同16x预算比OSCAR更慢/更耗memory，utility最优只假定log模型，bank cap可行性不在连续proof内；substring与judge不认证事实。Ch76一般controller缺同query-forward固定B的passage分配/成本，sep21源→owner通过，已在compression controller末/Iterative Stop前实际写入 Ch76:649/651 两段，sep21实际文字及邻接写后通过。

### [Memory That Looks Forward: A Zero-Inference Prospective Term for Personal Memory Retrieval](https://arxiv.org/abs/2609.22091v1)

`SF-2026-ARXIV-2609-22091` exact-v1 §3–6：open+firing ledger/乘法rank，不删除也不授权执行；oracle抽取层未建、resolved53仅有限negative、13/16 paraphrase触发，小W ceiling/负cos仍有边界。Ch77一般intervention/cue与15405尾trace未承载dated/resolved ledger离线链接与query算术rank；sep21源→owner通过，已在主动controller末/关联回忆前实际写入 Ch77:212/214 两段，sep21实际文字及邻接写后通过。

## 5. 缺口与下一步

普通可执行工作：无。最终60家族已冻结，七项必要源→actual owner与实际两段写后均获sep21通过，全部指定锁已按授权落实，最终日级独立Gate通过，不新增扫描。原53全positive复用/风险negative与同19具名分层抽核保留，不重复展开；未将1746 discovery变全文队列。

本窗终态保留：22125已由TyDe08/27官方同题报告证明更早公开，不作本窗first-public；若恢复PDF正式上线归属，仅重开该family早期owner。22195、22819、24144、24812的官方页/精确commit可读，但无first-public公开时钟，release API为空不能证明从未发布；有限官方入口尝试已止，不评分、不正面采用、不写Books、不支持零遗漏。接受作者正式公告/可信归档的精确范围后重开，24144还须区分核心paired-rollout与后续gradient事件。链接、现有证据和请求见[日期停点](../_sources/daily-20260922/V3_RECONCILIATION_20260930.md#日期停点有限终态0930本轮实际检查)。

Exactness24942中心必要性争议是本次安全终态，不阻止其他工作：只接受在明确task/误差语义下的necessary证明或可匹配反证后重开，不用另一个未控制实例或误差上界支撑正面采用。Google年度目录、Qwen/ZAI动态研究列表与MiMo模型公告时刻无法恢复的部分均隔离；Astra更正、Opus5.5、ZCode、MiMoV2.6只有09/22日级，跨09:00边界，不评分或回填时刻。重开需官方事件时间/可靠档案，或者可读带日级发布时间及分页停止点的研究目录；§2可核入口之外不宣称无遗漏。

风险negative已必要核：16639v2官方withdrawn已删除Ch29唯一采用链，保留其他有效来源；15795v2 title typo/content unchanged与09646v2 reference/results unchanged候选前关闭。22419v3当前§5已核engine1.8.0三项修复及09/21验证，但fix在09/15，正文实验未变，普通数据库版本验证不提供本窗新AI机制；临床应用本身不因此准入，保留原workaround不再必要的纠正，无采用链待删。以上风险negative均已获sep21非作者必要核通过，实际清除16639依赖链已获root写后通过。

窗外/归属未定：旧67个Mon21 v1归09/21，已交该日作者，保留原证据而不扩本窗。12748v2撤回传播因果解释，不是整篇withdrawn；v2 Fri18提交和目标Tue22公告未命中不能确定公开owner，有限archive恢复已止，日期隔离，不支持本日候选/新增Books。非作者实际命中Ch84既有段：共同substrate/启动波次不证明传播，缺read log不能推消费、缺outcome不能推效用；它仅承载事件身份、可见性≠消费≠因果合同，与v2纠正一致，不是新增v2正面采用，也无需删除该有效边界。v2 request仍不证明delivery或causal use；收到官方replacement archive后只重开该项。16639v3提交在本窗后，不凭其存在恢复本窗正面采用。跨日只核去重/归属，不扫描其他日报或Weekly。

## 6. 复核

复核者：root（已完成的必要源、owner和写后范围）；sep21_resume_v3（原53正向结果复用、具名重要revision/风险negative、19分层样本与七项必要源/owner及实际写后及最终日级汇总已通过）。
结论：通过

最终60家族处置、实际Books与普通0均获独立确认；完整限定范围见[独立Gate](../_sources/daily-20260922/V3_SEP21_DAILY_GATE_20260922.md)。
旧38逐篇证据与Books写后复核仅在身份、版本和采用命题未变时复用；日期归属错误已局部纠正，不继承旧整份完成标签。root已核NSP/SPLASH/SPECTRA/CKDA必要源、owner与实际写后及撤回清理，Exactness争议/MPS准入已校准。OpenAI本窗漏项补查、三核心说明贡献前关闭亦获校准，第三方评估只保留原则提案。22547/23570/13718v2/MiMo及22098/22101实际写后通过；七漏收必要源→owner及实际两段写后均获sep21通过，所有具体漏判已局部闭合；最终变化包与日级汇总已获sep21通过。当前表54深入完成、5标准完成、1争议，共60；实际49整合/8已有覆盖/2仅报告/1争议暂缓，作者普通待办0。未核全1746题摘、silent Replacement全正文或完整版本史，不能把抽样说成全量无遗漏。

本轮V3格式/一致性校验及本日报、唯一接续包、独立Gate和指定Books的差异检查通过；完成字段同步后再次校验。机器检查不能替代这些语义检查，也不证明全日来源和Books已验收。未stage、commit或push，已有暂存/无关修改保留。
