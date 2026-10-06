# Daily Research — 2025-12-22

**规范：** V3
**窗口：** 2025-12-21T09:00:00+08:00 ～ 2025-12-22T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T22:17:50+08:00

## 1. 结论

本窗从原始来源独立重建，不继承21日或旧Weekly。14个每日源均已实际访问；四组窄查询剩余页、新增题摘/必要v1与Meta正确入口现已补完，五项具体误排已修正。普通待办0，非作者Nash最终日级验收通过，见§6。历史目录/首公开限制不能当覆盖通过或零事件。确定落窗的准入家族1项：OpenAI Atlas防护Blog，官方RSS为Dec22 08BJT。2+2+2=6及安全变化必要深入已由Feynman实际独立校准通过，单篇证据、Books写后复核与整日日报验收分别完成。

具体增量是RL attacker取得defender特权推理/动作trace，在反事实续跑反馈上继续test-time长程攻击搜索，再分别驱动checkpoint训练与部署外围防护修补；不证明生产攻击者同等能力，不替代执行授权与独立release gate。唯一owner为PLATFORM-SECURITY Ch72，root已在Safety Control的on-policy trajectory repair后、CDI前实际整合两自然段并增加同家族末注；Feynman21:32:35实际非写入者POST通过，不复制现成run identity、failure repair或tool分责。

arXiv宽入口40项加四组窄主题完整页尾查漏，107条窄查询命中去重95，与首批合并120个发现ID，不是120项当窗公开论文。经具名局部改判后67项保留可能机制/边界增量，53项范围或贡献前关闭；其中新增70项的53个相关/含糊ID已读完整v1题摘，17个标题明确范围外未声称摘要已读。另GLM-4.7与MiMo Flash共2个机构potential已读必要core。69个potential缺本窗首公开/必要原始版本证明，其中DPSR另有具体隐私证明异议；均不评分、不入确定候选分母、不作为证据完成或Books正面采用。代表负侧customers核心已实际关闭；未做运行或安全实验。

## 2. 来源覆盖

原始查询、返回、分页停点、v1校正及分层筛选见[WINDOW_REVIEW](../_sources/daily-20251222/WINDOW_REVIEW.md)，首批准入见[ADMISSION](../_sources/daily-20251222/ADMISSION.md)。已检查仅指所列入口和主线切片，不授全机构召回。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1243项，局部邻接Dec18 12GMT→Dec22 00GMT两项；Atlas/customers核心各节 | 已检查 | 只此研究/安全入口，不授全站无遗漏 |
| SRC-ANTHROPIC | Research RSC publishedOn：Bloom Dec19 19:45Z→下一Jan8 2026，下邻Vend2 Dec18 | 已检查 | 不把完整历年payload转成本日队列，不相交不等全机构零事件 |
| SRC-GOOGLE-AI | Research真实2025 Blog page1/9 Dec18至Nov12；DeepMind真实page4跨Dec2025，原文year-review Dec23/Scope2 Dec19，page5止Nov–Jul；pubs year query返回2026 page1/772 | 受阻 | Blog两侧邻接已查；pubs历史过滤/clock未恢复，不授其Coverage |
| SRC-META-AI | 纠正旧失败路径后实际results publication page3：200/284065 bytes，局部Dec26安全对齐→Dec18四篇watermark→Dec16 SAM Audio，止此窗邻接 | 已检查 | 仅此原始目录主线邻接；后部混入旧推荐卡片不当日期排序，不授全机构零事件 |
| SRC-QWEN | 旧Blog止Sep23，迁移Research/Blog94344 bytes shell，旧feed404；Qwen3官方README定点替代未恢复本窗 | 受阻 | 新站2025目录/具名release；空响应不证明零事件 |
| SRC-DEEPSEEK | API Docs完整Change Log399行，Dec1 2025→Apr24 2026相邻 | 已检查 | 仅release入口，未扫全提交，Dec15到期不当本窗release |
| SRC-MOONSHOT | 官方Blog完整26项至2024May29，最新Nov7；changelog159行核心最新Nov6/Oct27/Sep5 | 已检查 | 不授全机构零事件，迁移文档不代替2025历史 |
| SRC-TENCENT-HUNYUAN | Research shell→官方JS/API read-only publicList，page1/20/全部，11/11全2026；T1 README定点替代 | 受阻 | 当前列表读完却无2025历史；浏览器不可用，未声称动态UI核验 |
| SRC-ZAI | Research page2 RSC18 article object至Dec7，143完整core；release notes日精度Dec22、HF完整card及model API | 受阻 | CMS午夜/迁移字段不授firstpublic，HF createdAt Dec22 07:45Z窗外不能替代Blog日期 |
| SRC-BYTEDANCE-SEED | Paper publish_year2025 page1：20/94，Seedance1.5 Dec15→GR-RL Dec2；官方API Blog type2：20/49，Prover1.5 Dec24→Seed1.8 Dec18→SeedanceDec16→GR-RL Dec2 | 已检查 | 止本窗邻接，不遍历全年，不把current updateTime当首公开 |
| SRC-BAIDU-ERNIE | 官方Blog实际2/2页：Dec23→Dec9→Nov21，第二页止Jun30，无下一页 | 已检查 | 本release目录未见相交条目，不展开窗外排行榜 |
| SRC-XIAOMI-MIMO | 首页8 Paper/15 Blog；官方chunk HSS Dec19/Safety Dec18；More返回Flash正文，Flash核心及README/repo信息已读 | 受阻 | Flash初始/重要修订原件与clock、More历史；Jan8 report不倒归本日 |
| SRC-MINIMAX | 英文12项/中文13项无Next，邻接Dec23 M2.1→Oct27 M2，中文止Jan15 | 已检查 | 两原始目录限定主线，不扩未触发Agent Tech Blog |
| SRC-ARXIV | 原始API发现40项；4组本窗title query首5+start5/max40实际10/24/20/33至15/29/25/38页尾，107→95窄主题ID、合并120；新增53个必要完整v1题摘与17个明确范围外标题处理完成，首批7项及新增5项具名局部修正已同步 | 受阻 | 67个potential的公告/更早作者正文未确认；DPSR另有安全证明争议，只约定主题的实际页尾，不授所有分类召回、不把Submitted当firstpublic |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Hardening Atlas against prompt injection](https://openai.com/index/hardening-atlas-against-prompt-injection/) | 2025-12-22T08:00:00+08:00 | 静态单次测试难覆盖长程恶意工作流→RL attacker用完整defender trace反事实续跑反馈继续搜索→需区别特权feedback与生产能力、训练与部署修补；2 + 2 + 2 = 6，Feynman独立准入/必要安全深入通过 | 深入完成 | 整合：`PLATFORM-SECURITY`，[Ch72 Safety Control](../../../../books/part-06-ai-infrastructure/72-security.md#safety-control-从生成后过滤前移到候选与失败轨迹)，root实际写在on-policy repair后/CDI前两段及末注；Feynman非写入者POST通过 |

仅此项已取得落窗证据且准入校准通过；69个日期/版本及具名争议potential在§5，不列确定当窗候选或评分。四组窄查询新增题摘已处理；当前确定候选集合为Atlas 1家族，保留项日期/必要证明恢复后只重开受影响家族。

## 4. 证据与知识整合

### [Hardening Atlas against prompt injection](https://openai.com/index/hardening-atlas-against-prompt-injection/)

家族SF-2025-OPENAI-ATLAS-HARDENING；公开时刻依据官方RSS `Mon, 22 Dec 2025 00:00:00 GMT`，不是从网页日精度补造。实际采用官方2025-12-22 Blog，必要核心为open challenge、RL discovery、proactive rapid response、outlook及用户限制；安全变化触发加深。Feynman21:24:39实际独立原源校准通过，21:32:35实际写后POST通过，记录见[独立结果](../_sources/daily-20251222/INDEPENDENT_REVIEW.md)。厂商能支持其公开机制和自身已rollout声明，不能支持独立评估、本地部署或实验复现。

单次输出/工具调用测试能低成本定位已知失败，仍应保留；浏览器多步攻击目标使反馈稀疏且延迟。RL attacker在推理中提出候选、调用外部simulator反事实续跑，取得defender完整reasoning/action trace继续迭代后才提交最终攻击。test-time compute属于攻击搜索，不是defender在线学习；该特权可见性须写入威胁模型，不能假定生产攻击者也有。

失败响应分为当前攻击训练checkpoint和monitoring、安全指令/外围system safeguards两条，修补对象不同，不提升执行授权。恶意inbox/辞职信例子及更新后识别只支持具名演示；视频未播放、攻击未执行。没有受控总体ASR、训练/搜索预算、独立测试或统计不确定性；hardware/precision、sampling、可比总查询成本为`Not Disclosed`。不采用普遍风险降低、deterministic guarantee或“confirmation已可靠”的主张。

具体Books对读已完成：Ch72的Safety Evaluation run保存预算与attacker/judge身份；failure repair要求独立验证、训练分责并保留poisoning/overfit；Red-team archive/integration保存coverage与effect identity，incident loop承接响应/revision。Ch78 ToolContract/Proposal实际拥有执行授权，Ch71四隔离平面不接管攻击发现，Ch73 Readiness Gates拥有发布/rollback。现成内容并非空白，局部差额仅是“特权完整trace→反事实续跑→继续攻击搜索”和训练/部署防护两个反馈出口。root已在Ch72上述Safety Control的on-policy trajectory repair后、CDI guidance前实际写入两自然段及同家族Review note；作者实际对读新增正文及前后段，Feynman实际原源→两段→repair/CDI及Ch71/73非写入者POST通过。预算记录、各自回归、敏感轨迹治理是本书工程要求，不冒称厂商实现已审计；本作者没有修改Books。

代表负侧[One in a million customers](https://openai.com/index/one-in-a-million-customers/)与Atlas同RSS时刻，核心为客户采用和75%自报新任务，没有新模型/执行机制或可归因评价协议，贡献前关闭；未无差别读客户附件。arXiv67个potential及53个负侧的具体题摘/理由见[原始记录](../_sources/daily-20251222/WINDOW_REVIEW.md)，首批初始27/23、独立改判29/21与新增修正后的38/32分开保留。新增MEEA、XG-Guard、AI Code in the Wild、committee OWASP等安全信号，以及M3-Verse、tie-out、ICAC训练挑战等反证保留具体评价/安全限制；局部、负面、小模型结果没有自动排除，后来v2/v6的新机制不偷渡v1。

新增五项不能只按传统RL、SNN或时间序列标签关闭：GMM-QF18763的非对角协方差表示与紧集连续/非紧L2假设，DGCRL18670的回报选示范前缀及逐步缩短引导，SNN Memory18575的跨模态评价混杂，EOB18610的协方差平稳条件下联合/因子化目标，以及DR-MARL18558冻结旧策略最坏情形估计器的有效性边界，均保留有限潜力。Feynman已实际读取各自exact-v1必要局部，root复用同身份、版本及窄命题同步，不冒称重读全文。分别不采用通用收敛、等条件curriculum因果、603倍硬件效率、正交即任意独立或新策略最坏情形已知；位置与原源见[五项修正](../_sources/daily-20251222/WINDOW_REVIEW.md#新增五项具体误排修正)。首公开日期仍缺，不评分、无新增Books。

Feynman实际exact-v1必要局部后重开CAN18750（时空分支/通道分组与融合顺序对照）、EEG-CSANet18689（pooling稀疏损失、residual及结构差异不显著）、VizDefender18853（图像变化证据不等攻击意图）；SchedTwin18894的32 Docker/单AMD、150合成node/walltime作业与FCFS/WFP/SJF仅为通用HPC类比，具体关闭。MCP-BIM2601.00809保留server/adapter职责、Artifact/Diff与tool-success不等model-success及并发限制；MDToC18841保留concept/探索宽度的质量成本和geometry递减收益，不以成熟组合排除。以上复用本日同身份/v1/采用命题的独立局部原源结果，不冒称作者重新读了这些全文。

DPSR18932保留潜力但不采用ε-DP正证：Feynman实际§3.3.1/3.5/3.9式9–18指出全局均值校准使其他entries分布不变的前提不足，不同Laplace scale密度比缺归一化因子、2ε直接转ε组合界等具体异议；post-processing不能修补不合法Stage1，base-budget rescale不单独证明数据依赖scale的likelihood ratio。需要合法邻接/校准权限和完整概率证明后才可采用隐私命题，不能只补日期就授安全。

## 5. 缺口与下一步

普通待办：0。非作者Nash对已修正作者层完成最终日级验收及完成态校验，见§6；Feynman新增安全/反证必要局部及五项误排修正已实际完成并同步。四组具名arXiv查询剩余页已至页尾，新增53个必要完整v1题摘和17个明确范围外标题已处理；Meta正确results page3、Google pubs有限恢复和18725v1校正均已记录。Atlas准入、必要源审、两段整合与非写入者写后复核已闭环，无其他新增Books待办；不以作者同步或机器通过代替独立内容验收。

以下外部终态保留不用于正面证据、Books、Coverage/Evidence通过或零事件/无遗漏；材料恢复仅重开相应家族，不重扫整月：

- **GLM-4.7 / Research143**：[原始Research](https://www.zhipuai.cn/zh/research?page=2)及官方card已读interleaved/preserved/per-turn thinking、τ²额外prompt/domain fix。CMS createAt Dec21 16Z是日编码且记录于2026迁移，release notes日精度跨09截点，HF createdAt Dec22 07:45:52Z仅artifact且窗外。需Dec22 01Z前可校验公开Blog/card或同窗重要修订原件才重开143，不先评分。
- **MiMo Flash**：[官方原文](https://mimo.xiaomi.com/blog/)已读GA/SWA、轻量MTP与多teacher on-policy核心；More失去列表、route无date，Jan8报告/repo不能证明本窗正文或重要修订。需精确初始/修订版本和clock；不以日期受阻省略core，不采用宣传效率、不写正面Books。HSS Dec19/Safety Dec18仅窗外日期线索。
- **67个arXiv potential**：首批经具名改判29和新增38的逐项ID/v1与机制见[具名记录](../_sources/daily-20251222/WINDOW_REVIEW.md)。API published/Submitted非firstpublic，历史公告路径400，官方日历仅支持公告日程推定而非已恢复历史列表；四组窄查询已读到页尾但只完成这些发现/题摘。Reflection OpenReview note API403；LessIsMore repo创建Sep3不能证明当时README。需具名家族本窗announcement或可核的作者初始正文/cdate/pdate；DPSR还须解决§4具体邻接/密度比/组合证明异议，不只补日期。不无限恢复所有作者渠道，不冒称已读全文或已证实，日期未知不是普通题摘豁免。
- **历史目录**：迁移Qwen Research、Hunyuan2025全部列表、Google pubs2025历史过滤、MiMo More。§2和原始记录保留实际失败/替代/停止位置；future-only列表/ignored-query不足以授覆盖。Meta旧路径失败已由正确publication页邻接恢复，不再保留为未恢复源。其余官方历史目录或具名release及原始公开字段恢复后只补相应源/时段，不扩历年组织库存。

日历及Jan/Dec-ID所支持的较晚arXiv公告只是窗外恢复线索，不排除此前作者公开；没有把晚发现挪成本窗候选，未开启其他归属日/Weekly。

## 6. 复核

复核者：Nash（非22作者；原作者Mill，root仅接手具名作者同步/Books写入；Feynman前批独立原源与POST结果按同identity/v1/窄命题复用）。

结论：通过

实际重读当前AGENTS、研究/Report合同、每日14源/arxiv边界、Prompt、ROADMAP/state路由及本日正式/ADMISSION/WINDOW_REVIEW/独立记录。逐行核14源入口、有限邻接/分页停止与外部范围；四既有窄query首5后各10/24/20/33到15/29/25/38页尾，107→95、与首50合并120身份，不把宽253、Submitted或后月ID授本日公开/全分类召回。Meta正确publication页邻接已恢复；Google/Qwen/Hunyuan/MiMo历史缺口只隔离。

Atlas唯一拟入选项的官方RSS时刻、具体2+2+2=6、安全必要深入、Ch72唯一owner实际两段及Feynman非writer POST均核实相符。本轮定点对读repair→Atlas→CDI与末注，未发现采用漂移；复用厂商原源只支持公开设计/rollout声明，不采用总体ASR、等预算性能、生产授权或确定性安全保证。

负侧按主题/理由分层：Nash本轮20个完整v1题摘，Feynman前后36个，重叠去重覆盖41个具名身份而非56个；样本ID与位置见[独立记录](../_sources/daily-20251222/INDEPENDENT_REVIEW.md)。复用CAN/EEG/Viz/SchedTwin/MCP-BIM/MDToC/DPSR必要局部及新增安全/反证源；本轮补读8份安全/反证HTML局部并核实际限制。共同领域标签错误只扩查受影响集合，GMM-QF/DGCRL/SNN Memory/EOB/DR-MARL五项原件及限制由非作者原源支持，root作者层已同步保留、不采用边界及计数；未代写作者修正再自验。其余明确负侧分层样本可接受，17 title-only没有声称读全摘要，未逐项复读所有无关附件或全120正文。

现值120=67 arXiv potential+53closed，新增70=38/32，首50=29/21；另GLM/MiMo2项，共69具名日期/版本/证明争议保留，确定候选Atlas1、实际Books整合1。全部必要可执行来源/准入/安全反证/作者同步与本节最终复核已闭环，当前ordinary0、无Books待办。§1/§5所列“待Nash最终验收/完成态校验”为验收前工作，本节现已执行并结束，不再是当前待办。真外部缺口不授Coverage/Evidence/Books或零事件、无遗漏、性能安全保证；只按原始公告/完全落窗范围、精确历史材料与DPSR合法概率证明定点重开。

2026-10-02T22:20:28+08:00实际运行本日完成态V3校验通过；两授权文件局部diff-check通过。因文件仍未跟踪，另逐文件以`--no-index --check`检查，均无空白诊断（exit1只表示相对空文件存在内容）；本日报及本日Markdown原始记录的本地链接目标存在。机器检查不替代上述实际语义复核。未运行攻击/模型、未部署或复现实验，未stage、commit、push，未改共享Books/state或作者§1–5。
