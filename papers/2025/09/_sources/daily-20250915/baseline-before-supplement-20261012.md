# Daily Research — 2025-09-15

**规范：** V3
**窗口：** 2025-09-14T09:00:00+08:00 ～ 2025-09-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-06T21:27:59+08:00

## 1. 结论

本日0个确认当窗正式候选，不表示0事件。arXiv有限发现96唯一当前版本，一页96标题、原82完整题摘由非作者实际独核；对两含糊标题22673/11131定点补完整摘要后明确关闭，最终84完整题摘=70具体潜力/14贡献或范围关闭，另12范围明确标题关闭。Meta CyberSOCEval另1完整摘要，合计85唯一题摘家族；GPT-5-Codex官方说明/当前七页卡片另1必要说明，RSS事件与PDF版本日期存在反侧。没有把上述材料算86篇全文或当日新论文。

具体潜力包括eager operator变化下swap、query维度attention近似、PowerSGD收敛反例、optimizer moment模型合并、typed memory、composite-null检验；11213从泛称组合排除中恢复自然图像编辑的语义/保真权重控制潜力，必要公式与局部CLIP反侧亦保留。攻击、隐私预算与局部负面证据不因“没改变通用原则”缩池。全部采用事件的日期/精确版本仍不支持完全落窗，不评分、不采用性能/安全保证；0正式候选证据审阅完成/0Books新增，条件化NoChange提案不等于正面Books通过。非作者FIRST/必要风险及DAY已完成，无普通待办，外部材料精确终态隔离。

## 2. 来源覆盖

本日33初始原始请求见[transport](../_sources/daily-20250915/transport.json)，五次相关目录日期/邻段请求见[date-probes](../_sources/daily-20250915/date-probes.json)，OpenAI说明与PDF请求另存。本日独立恢复响应，不沿用别日材料结论。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方RSS1247，实际Sep12T12Z→Sep15T00Z/03Z/10Z原pubDate；card00Z对应08BJT，其他两项窗外。落地页HTTP403后web正文恢复；官方PDF7页293503B实际读取 | 受阻 | 当前PDF CreationDate/ModDate Sep15T16:58:52Z、CDN Last-Modified17:00:07Z均晚于本窗；RSS不单独授这份精确版本首公开。§5隔离 |
| SRC-ANTHROPIC | Research Flight JSON字符串实际结构解析172 publication；publishedOn Sep5T00Z→Sep15T09Z/20:33Z跨窗，原值保留 | 已检查 | 当前数组有限历史，不授已删材料覆盖 |
| SRC-GOOGLE-AI | DeepMind page5 24标题Nov→Jul，三个原文published_time FSF Sep22T00Z、ICPC17T00Z、Robotics25T00Z均窗外，科学应用标题范围关闭。Research2025/09 1→2/2共13标题Sep30→9 | 已检查 | Vault仅Sep12无timezone，但不能移到Sep14起点；不把月份标签当原公开时刻，不授全站无遗漏 |
| SRC-META-AI | Blog?page3混排12条；真实publications results/page5主12条Nov18→Sep15，接results/page6主12条Sep8→Sep2→Jun13。CyberSOCEval原页完整摘要实际读取 | 受阻 | CyberSOCEval仅Sep15无timezone，可能相交但未确认完全落窗；不是因无贡献而排除，§5隔离 |
| SRC-QWEN | 官方config原JSON十个2025-09对象实际读取，Next Sep10T20Z/ASR8T06:38Z→Sep21–24发布；均窗外 | 已检查 | 不复用其他日core以凑本日候选，不授历史删项覆盖 |
| SRC-DEEPSEEK | 官网及官方API更新日志实际Sep29→22→Aug21跨窗，读取对应标题/变更范围 | 已检查 | 当前日志有限事件，不全扫GitHub普通修复 |
| SRC-MOONSHOT | 官方Blog实际26标题/日期，Nov7→2024May29；Sep16→5→Aug22跨窗，原25计数已按本日原文纠正 | 已检查 | 仅官方可见目录，不授全仓库无事件 |
| SRC-TENCENT-HUNYUAN | Research+正确publicList POST page1,size100,renderType0；total9逐条title/displayPublishTime实际Feb3→Sep21 2026 | 受阻 | 2025历史目录缺口，当前9不是历史0；恢复原发布后只重开目标邻段 |
| SRC-ZAI | Research+?page2/3实际响应，派生正文同18条Aug26 2026→Dec7 2025且没有更多；官方release notes Sep30→Aug11跨窗 | 受阻 | Research2025-09未恢复，已执行分页不能误记未执行；不授零事件 |
| SRC-BYTEDANCE-SEED | Research/type2 year2025 page0 count20 desc实际15/total49/has_more；置顶单列，非置顶Oct22→Aug20/13→July跨9月。type1 US/CN page0 total94缺数组；独立沿20→40→60→80实际执行，20仅June SwiftSpec、40/60缺数组，80 has_more=false/next空。[有限恢复](../_sources/daily-20250915/INDEPENDENT_FINITE_RECOVERY.json) | 受阻 | 已至真实有限停止但历史条目不完整，total94不是0论文；需官方目标历史数组/原发布 |
| SRC-BAIDU-ERNIE | 官方中文Blog1→2/2实际16标题，May9 2026→Sep12PLAS→Aug14→June30 2025跨窗 | 已检查 | 不重读窗外PLAS必要core；目录日期有限，不授全历史覆盖 |
| SRC-XIAOMI-MIMO | 官方8Paper/15Blog实际读取；fresh home chunk的More为已有array slice/状态切换；Paper Sep19→June4→May12 | 受阻 | Blog无日期；current Paper边界不授Blog历史0，需具体原发布区间 |
| SRC-MINIMAX | EN12条止Oct27，?page2派生正文相同；CN13止Jan15才跨9月；Agent index仅2026-05-13当前文章 | 已检查 | EN不能独自授跨窗；当前Agent入口不授历史不适用或0事件 |
| SRC-ARXIV | 12分类×八组主线术语，submittedDate Sep13T18Z→Sep14T18Z，start0/max200/total96，一页96标题、最终84完整摘要。catchup400实际仅90日限制；show200原为非法值，不是正确外部终态，现同skip800改合法250得200、250/2214、15549→19344，仅本日19325/19326/19329月身份匹配、无日公告heading；未扩250为题摘队列。[恢复记录](../_sources/daily-20250915/INDEPENDENT_FINITE_RECOVERY.json) | 受阻 | 可修停点已处理，仍无完全落窗首公开/重要修订区间；70潜力隔离，不授全分类召回 |

只扫描Daily组和实际触发的原发布/必要卡片，无Weekly、其他月或全站附件队列。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

0正式当窗家族，未评分。70 arXiv潜力、Meta与OpenAI两家族因必要日期/版本不确定留于§5，不提前写确定候选。与Books主题相似、局部实验或访问成本不构成排除依据。

## 4. 证据与知识整合

### [GPT-5-Codex system-card addendum](https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/)

官方落地核心与当前[七页PDF](https://cdn.openai.com/pdf/97cc5669-7a25-4e63-b15f-5fd5bdc4d149/gpt-5-codex-system-card.pdf)实际读取；仅保存条件化潜力，不授当窗采用。§2 pp3–4说明malware/双用途训练及coding注入评估，§4 pp6–7区分cloud隔离容器、local sandbox和可放宽网络/unsandboxed配置；模型行为概率不是执行授权。内部Table4两模型均0.98，但样本、CI和真实副作用分母未披露，不能推出所有泄漏/后门/破坏被防住；Table1退步类别的“自然噪声”只是厂商解释。卡片未披露完整实现/控制流审计，本次未运行攻击或复现。

RSS00Z不抹除PDF16:58:52Z创建/17:00:07Z修改反侧，后两项也不是首公开时刻；精确版本与落地事件分开。完整校准请求与实际owner论点见[FIRST_BATCH](../_sources/daily-20250915/FIRST_BATCH.md)。Ch72 `PLATFORM-SECURITY` 实际1245–1273已有独立policy/effect-time最小权限executor，764–812已有完整run/attempt与发布门禁分责；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)104–118固定eligible population/scorer/uncertainty，邻接Ch71/73的隔离/发布责任另读。作者建议日期解决后机制NoChange、接口版本事实仅报告，不新增产品小节；root尚未独核，所以当前Books暂缓，不自授已有覆盖。没有必要长期差额证据则不制造自然段落或Books diff。

### [CyberSOCEval](https://ai.meta.com/research/publications/cybersoceval-benchmarking-llms-capabilities-for-malware-analysis-and-threat-intelligence-reasoning/)

官方完整摘要及原26页PDF必要pp6–10/12–14实际读取：默认provider thinking配置、不同模型/systemprompt对照不建立同模型同预算test-time scaling因果；只保留该任务配置的局部评价反侧，不采用训练scaling law或真实SOC能力保证。原页Sep15无timezone仍不能授落窗，不遍历其余附件。

root校准触发的九个精确v1必要安全/设计反侧已实读，连同Codex和Meta共11必要core家族；精确位置、实际读取角色、成立条件和未证明内容见[NECESSARY_CORE](../_sources/daily-20250915/NECESSARY_CORE.md)。11128v1为ENJ而非新版ERIS；11254反例的任意初始化/零向量QR有证明争议，均明确隔离，不因datehold免读，也不把局部core计为当窗采用或82篇全文。

原82题摘与最新局部修正见[SCREEN](../_sources/daily-20250915/SCREEN.md)和[独立验收](../_sources/daily-20250915/INDEPENDENT_DAY_REVIEW.md)。11191随机adversarial sampling训练成本、11284三维GMM directmap PoC、11337弱攻击/大batch理论边界保留，非因小实验或理论排除。11213精确v1 I/III-B原文明确perceptual/triplet权重随训练sigmoid切换并用discriminator维持保真，足以恢复自然图编辑的局部控制潜力；TableI部分CLIP反降、预算/样本未披露、Eq6/11推导符号争议不授普遍收益或正确证明。[定点原件](../_sources/daily-20250915/INDEPENDENT_SLIDERS_CORE.json)。22673仅Cox/浅survival tree临床流程、11131既有NCA综述/未来类比，完整摘要后关闭，不建立全宽标题队列。11076 swap与11250 GUI攻击的Chameleon不合并；v2–v5不默认重要修订或替代v1。0Books实际修改，日期隔离项不授已有覆盖；作者条件化owner提案留作材料恢复后的对读起点。

## 5. 缺口与下一步

尚可执行工作：无。非作者FIRST、必要支持/反侧和DAY实检已完成；合法show邻段与Seed下一页已实际有限恢复，普通未读附件不伪装外部阻断。

本窗终态保留项：OpenAI当前七页卡片的当窗原版本/公开区间，Meta CyberSOCEval原时区/区间，70 arXiv潜力精确公告/原发布或重要修订（身份见SCREEN最新修正），Hunyuan/ZAI目标历史、Seed论文完整数组、MiMo无日期Blog。缺少这些影响事件采用与来源恢复，不否定具体潜力。重开条件接受官方当窗原版本/更正、指定ID精确发布或完全落窗区间；历史目录接受官方目标条目数组/原发布，MiMo接受具体Blog时间，不一律请求秒级。它们不用于正面证据、Books 或无遗漏断言，不授正面Coverage/Evidence、零事件、性能或安全保证。取得材料后仅重开对应ID与必要core/owner或来源2025-09目标邻段，不重扫整类/月或以题摘库存变全文队列。

PDF当前创建/修改在窗外只是归属反侧，不反向假定首次公开必为16日；不扩张本窗恢复别日。明确关闭项日期未核但不影响贡献处置，不为它们另造日期请求。

## 6. 复核

复核者：sept07_10_author（本日报非作者，作者Bacon；独立FIRST/必要风险及DAY）。

结论：通过

本日独立加载当前合同/窗口/停点，实际完整复核原82题摘+两含糊标题摘要（最终70潜力/14关闭、12标题范围关闭）；Meta另1完整题摘、当前Codex卡片完整七页及九v1必要方法/限制、Meta必要评价原件实读。11213误关闭已恢复局部潜力，不授日期；安全关闭11078/11136/13352/11369的实际摘要权限/控制/归因边界另核，不采用隐私、production身份、UAV闭环或普遍provenance保证。十四来源有限原响应、show合法修复、Seed真实停止、PDF/RSS分离、全部采用项（正式0）、Books0和六部分已验收，未重读无关附件/核代码/复现。详情与最终V3/限定diff结果见[独立验收](../_sources/daily-20250915/INDEPENDENT_DAY_REVIEW.md)，机器检查不替代语义。
