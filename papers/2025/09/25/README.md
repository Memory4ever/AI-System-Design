# Daily Research — 2025-09-25

**规范：** V3
**窗口：** 2025-09-24T09:00:00+08:00 ～ 2025-09-25T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T20:06:00+08:00

## 1. 结论

本日正式候选1家族：Gemini Robotics 1.5。非作者局部FIRST通过2+2+2=6；动作前多级自然语言推理与动作交错、已训练ALOHA/Franka/Apollo之间的技能迁移是有限增量，不是成熟ER planner与VLA组合。作者标准必要方法/对照及受影响安全反侧深入完成；可见thought不证明faithfulness，目标任务只在源本体训练不等于目标硬件从未训练，Motion Transfer具体architecture/recipe未披露，不能制造算法或普遍安全结论。Books为Ch26具体已有覆盖加未披露MT仅报告，root独立Evidence/Books及DAY已通过。

原本日12分类主题提交发现226个对象不是226个当窗公开事件。162完整当前题摘已实际读；原64题名排除中13项需完整题摘，实际补读后8项重开潜在贡献/必要反侧，余51仍仅按明确领域题名范围关闭。合计175完整当前题摘读域，不冒称175精确首次公开版本。少量明确无增量/领域应用按具体理由关闭，其余潜力及后版差异在实际官方日路径400、月/advanced只有月精度的公开身份限制下隔离：不评分、不进入本窗正面证据或Books，不靠提交时刻补造公开。Qwen3-Max、Pulse/Germany三个代表贡献关闭已独立校准；14源有限停点已恢复，不授全网召回。独立日级复核通过，范围与未抽检项见§6。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research403；官方RSS窗口3项，Pulse/Germany完整官方核心及非作者原主体独读，ENEOS标题/完整RSS描述范围关闭 | 已检查 | RSS非Research全集；三项不授执行/安全能力；两个代表关闭FIRST通过 |
| SRC-ANTHROPIC | 实际Research结构化publishedOn字段按本窗核，当前无落窗对象 | 已检查 | 不保证Research未列入事件 |
| SRC-GOOGLE-AI | Research/Google9月Blog首12跨09-23至11；DeepMind真实page5历史切片、Robotics原主体/62页报告必要方法与直接反侧 | 已检查 | Robotics准入通过，作者必要审阅完成；Publications年精度不判窗，健康应用范围关闭 |
| SRC-META-AI | Research后真实results page4/5；CWM/CaT/Preparedness/MetaEmbed完整题摘、原HTML日期字段和CWM截点前commit/历史README | 受阻 | CWM/CaT09-24 date-only；Preparedness列表09-23/正文09-24冲突；MetaEmbed09-23时区不明。commit不是公开，未采用风险/性能保证 |
| SRC-QWEN | 60官方对象严格ISO过滤一项Max；原tokens完整Introduction/Base/Instruct/Thinking/Develop/References | 已检查 | 贡献关闭FIRST通过；未披露named pipeline，不授所有发布无遗漏 |
| SRC-DEEPSEEK | 官方主页/updates29→22夹窗 | 已检查 | 22日Terminus非本窗新事件，不以更新日混入 |
| SRC-MOONSHOT | Blog可见单页11月→09-16/05跨窗 | 已检查 | 非GitHub全部事件目录 |
| SRC-TENCENT-HUNYUAN | Research首查；publicList page1 size100 renderType0实际9/total9，最早display/public字段2026年 | 受阻 | 当前“全部”无2025历史；不作9月零事件或历史完备 |
| SRC-ZAI | Research首列表15项，实际page2累计18并显示没有更多，最早2025-12-07 | 受阻 | 当前目录不恢复9月，非按最早一项推全站无事件 |
| SRC-BYTEDANCE-SEED | Research/Papers；2025 type2 page0 count20实际15/49，has_more=true；非置顶已跨07-15，停第一页；type1及CN补请求total94缺列表 | 已检查 | pinned非单调排序，有限夹窗不授全集；论文列表缺失隔离，不记0论文 |
| SRC-BAIDU-ERNIE | Blog实际1/2与2/2跨09-12 | 已检查 | 有限目录非全网保证 |
| SRC-XIAOMI-MIMO | 同日首页Paper8、Blog15；Paper10-21→09-19→06-04跨窗，Blog当前条目与More路由有限 | 已检查 | Blog未给历史时刻，不授first-public/完整历史；Paper09-19非本窗 |
| SRC-MINIMAX | 英文首页/page2同12dated项；中文13项10-27→01-15夹窗；Agent与llms当前1篇2026-05-13 | 已检查 | 英文page2非分页；有限中文目录与无历史Agent路由不授2025全集 |
| SRC-ARXIV | 原12分类模型/多模态/world/Agent/GPU主题提交发现100+100+26读完；175当前完整题摘/51明确题名范围；本日官方day400，advanced/月只支持月精度 | 受阻 | 不用API published/提交排期当首公开；潜力与必要风险/版本保留见§5；新四辅助查询不扩大原池、不授全分类召回 |

原首查[fetch-results.json](../_sources/daily-20250925/fetch-results.json)、[窄补](../_sources/daily-20250925/narrow-fetch.json)、[分页](../_sources/daily-20250925/arxiv-pages-fetch.json)、[恢复记录](../_sources/daily-20250925/scan.md)保留。恢复时发生大小写文件名别名问题，17个原tracked来源已逐一按Git原件字节完全恢复，原件与新实际内容分别保存在`original-before-resume/`与`resume-check/`，见[恢复依据](../_sources/daily-20250925/case-alias-recovery.json)。没有丢弃原请求或用新内容反推2025事实。额外四主题查询模型/Agent各返回60但总量220/136，不能称已读完；不扩大原池或把追加发现变成全类逐项队列。

## 3. 候选与判断

按[非作者局部FIRST](../_sources/daily-20250925/INDEPENDENT_FIRST.md)保留Gemini1家族。FIRST只授准入/最低投入与三个代表关闭，未授Evidence、Books或DAY。arXiv未确认公开归属的潜力不列确定当窗候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Gemini Robotics 1.5](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/) | 2025-09-25T08:00:00+08:00 | 直接指令→动作的多阶段/跨本体约束→多级thought/action交错与训练覆盖内MT→重考虑监督/迁移边界；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)三时钟、Plan/Think、grounded-language与action-schema；未披露MT仅报告，root独立裁决通过 |

## 4. 证据与知识整合

### [Gemini Robotics 1.5](https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/)

原HTML `article:published_time`及JSON-LD `datePublished`均`2025-09-25T00:00:00+00:00`，北京25日08:00在窗内；不以2026修改时间取消或反推原正文。原主体完整核心及具名62页[技术报告](https://storage.googleapis.com/deepmind-media/gemini-robotics/Gemini-Robotics-1-5-Tech-Report.pdf)§2.1–2.3、§3.1–3.3、§6风险与模型卡、B3/B4/B5.3必要读域已实际读取；PDF p9/p56图像像素已实际核。PDF metadata Creation/Mod只辨识所取版本，不证明公开时间；视频未播放、实现未核、未复现。

§2.1的Thinking-VLA先生成任务/skill/primitive自然语言trace，追加context再生成动作；trace可观察不证明忠实因果解释。§3.3/B4的复合多阶段指令Thinking On/Off按本体分开：进度ALOHA .55/.26、Franka .60/.55、Humanoid .67/.51；B5.3/Fig36成功率分别.38/.09、.44/.42、.40/.26。Franka有限优势/图误差条重叠不能被总体“robust improvements”覆盖，也不由单次开关独立证明所有收益来自正确推理。任务数/同workcell A/B/n与大多数开发阶段MuJoCo评价已披露；完整重复运行、不确定性计算、inference hardware/precision、思维长度/频率、端到端latency/control deadline/batch/concurrency/SLO为 `Not Disclosed`，TPUv4/v5p/v6e与JAX/Pathways训练事实不等运行配置。

§2.2/§3.2/B3：三个本体都在pretraining，held-out目标任务只在源本体动作数据出现；Franka→ALOHA10任务及ALOHA/Humanoid→Franka11任务是跨已训练硬件新技能，不是任意新机器人零数据适配。多本体no-MT及single-body基线提供局部对照；ALOHA数据充裕、Franka中等、humanoid稀少时收益组成不同，humanoid MT增量较小。GRoD对照数据更少/早checkpoint/non-multi，原文明确非apples-to-apples，不能作为匹配预算因果。Motion Transfer只具名novel architecture/training recipe，未披露action-space实现、loss/采样/总预算，报告保留迁移观察，不造retarget算法或所有本体普遍净收益。

受影响安全域§6：低层碰撞/硬件安全、语义与对话安全分层；ASIMOV2补NEISS伤害tail、风险/severity/effect及视频last-intervention-time，synthetic视频和共享模型的attacker/target/auto-rater不是独立真实安全ground truth。只保留这些评测职责/局限，不采用“robustness”为开放动作或部署安全证明，不扩大重读无关benchmark附件。伙伴权限与API发布不是实物执行验收。

实际Books差额读到Ch26三时钟/闭环114–130、数据演进593–647及grounded-language1246–1273，并读Ch25 world-state/action-authority交接1112–1150及Ch27开篇。Ch26已有episode-level Plan/chunk-level Think按时间尺度监督，teacher trace非物理真值、错误Plan污染后续chunk、fresh observation/controller/safety envelope及直接BC回退；grounded-language已区分显式CoT低频辅助与硬实时critical path成本。因此有限公开thinking接口已有具体论点承载，不为发布名重复写。跨本体action-schema/provenance/target真实示教边界已在593–607承载；未披露MT不能落新长期算法。该已有覆盖/仅报告组合已由root完成非作者独立证据与owner裁决，详见§6；作者未改Books。

### 代表贡献关闭：[Qwen3-Max](https://qwen.ai/blog?id=qwen3-max)

本日60对象仅原`2025-09-24T04:00:00.000Z`落窗，北京24日12:00。实际[完整核心](../_sources/daily-20250925/qwen3-max.core.md)读完Base/Instruct/Thinking/Develop/References。延用Qwen3 MoE/global-batch、旧ChunkFlow，未披露PAI-FlashMoE多层pipeline或SanityCheck/EasyCheckpoint新执行算法。30%相对MFU、3倍吞吐与故障时损1/5缺具体hardware/parallel/workload/可比基线预算；这些named方案不自动证明本次新机制或新的资源可行性边界。关闭理由是实际增量未披露，不是大规模、产品发布或未开源。旧ICML/Qwen3引用不扩成旧全文扫描；非作者FIRST已通过。

Pulse/Germany完整官方主体与独立原主体读域见[FIRST](../_sources/daily-20250925/INDEPENDENT_FIRST.md)。前者nightly memory/history/feedback、默认off可撤销connector、一天临时卡片/保存为chat和已完成项目仍推荐，不披露新恢复/时效识别机制；后者计划2026 SAP/Delos/Azure及4000GPU，主权/隐私/韧性是承诺而非新隔离执行证据。两个贡献关闭通过，但不授安全有效性。ENEOS完整RSS描述为制造/HR企业应用，范围关闭，不冒称读全文。

## 5. 缺口与下一步

本窗可执行工作已处理完：Gemini必要证据与具体Books已有覆盖已独立裁决，不需要新增书稿写入。以下为本窗终态保留项，不支持正面证据、Books或无遗漏断言，不能视为Coverage/Evidence通过；替代材料到达后只定点重开。

外部终态保留：

- arXiv原主题API100+100+26已返回/读完；官方25日路径实际400，advanced明确announcement只支持年月，月目录无日归属。当前175题摘中的潜在项（如EditVerse、Language Models that Think/Chat Better、CaT、FastEagle、Amoeba、BurstEngine、Frame-stacked speech）及必要安全/反侧（FreezeVLA19870、Gaslighting19858、LatentGuard19839、bi-GRPO19775、Supply-chain20277、EchoBench20146的明确领域边界、Bias-in-Picture19659、AnySafe19555）不以submitted/API published授当窗。后版/2510别名也不反投9月机制；现有原API材料只作恢复身份，未采用其性能/安全数字。需要官方具名日级公告、当时事件存档或完全落窗公开区间；取得后只重开对应ID精确事件/版本、准入和必要证据，非重扫全部分类。贡献前明确关闭代表及13项原题名误排恢复理由在scan，独立风险/负侧实际核验范围见§6。
- Meta CWM/CaT24 date-only、Preparedness23/24冲突及MetaEmbed23时区不明：原题摘/HTML与CWM历史README、截点前commit已实际取得，但repo创建/commit/HF首次登记不证明公开。不采用CWM“无额外frontier风险”或CaT收益；官方原公告带时区或完全落窗区间到达时只重开相应家族。HF commits401只影响可选artifact历史，不阻塞现有文本限定。
- Hunyuan当前全部9对象仅2026、Z.ai18对象最早12月、Seed论文type1及CN响应total94缺sub_article_list、Google Publications只有年、MiMo/MiniMax有限历史目录：不支撑本窗零事件、正面覆盖或无遗漏。历史列表/具名原事件到达才重开对应入口/家族；当前动态页面/list翻页可执行停点已用尽，不把空列表当0研究。

## 6. 复核

复核者：root（非报告作者；首批准入由sept07_10_author独立校准）

结论：通过

准入校准身份/版本/窗口未变化，复用FIRST及Max/Pulse/Germany完整核心关闭，不重新无差别审阅。实际核Gemini精确报告§2.1～2.3、§3.2～3.3、§6受影响安全职责、B3及模型卡：思维先入context再出action、所有目标本体已预训练、跨本体任务隔离与MT差异成立条件均保留；不由thought证明faithfulness或由ASIMOV认证开放动作安全。实际对读Ch26闭环三时钟、episode Plan/chunk Think、teacher trace非物理真值及grounded-language的成本/回退，接受具体已有覆盖；MT算法未披露仅报告，不增孤立发布摘要。

七项安全/纠错/设计反侧题摘19870/19858/19839/19775/20277/19659/19555全部独核保留，日期未解且不采用其性能/安全主张，未称必要正文审阅完成。普通退出分层实际题摘20418/19952/19779/19524/19485及风险退出20146；EchoBench因具体跨模型评价反侧恢复潜力，旧领域标签不能代替贡献判断。未抽检51明确领域题名和其他普通退出仍为作者范围判断，不称独立全量复核。读域及重开理由见[本日scan](../_sources/daily-20250925/scan.md)。

核14源请求/有限停止及大小写别名恢复，175为完整当前题摘读域，不是175首次公开版本或贡献；四辅助主题不扩池，日期/目录终态保留不支撑Coverage/Evidence或无遗漏。没有普通待办或未落实Books写入。V3、引用和diff检查通过；不把格式通过当研究质量证明。
