# Daily Research — 2025-09-15

**规范：** V3
**窗口：** 2025-09-14T09:00:00+08:00 ～ 2025-09-15T09:00:00+08:00
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-10-06T14:27:41+08:00

## 1. 结论

本日0个确认当窗正式候选，不表示0事件。arXiv有限发现96唯一当前版本，一页96标题、82完整题摘实际读完，69潜力/13关闭建议，另14仅范围明确标题关闭；Meta CyberSOCEval另1完整摘要，合计83唯一题摘家族。另1 GPT-5-Codex官方说明/当前七页卡片实际读取，其RSS与PDF版本日期有必要反侧。没有把上述材料算84篇全文或当日新论文。

具体潜力包括eager operator变化下swap、query维度attention近似、PowerSGD收敛反例、optimizer moment的模型合并、typed memory操作、语义无关扰动的composite-null检验。攻击、隐私预算与局部负面证据保留，不用“没改变通用原则”缩池。公开日期/精确版本未落窗，不评分、不采用性能/安全保证。作者侧研究已ready交root；首批准入、必要采用及最终非作者DAY未授。Books无作者改动，条件化NoChange提案不等于已通过Books。

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
| SRC-MOONSHOT | 官方Blog25标题/日期，Nov7→2024May29；Sep16→5→Aug22跨窗 | 已检查 | 仅官方可见目录，不授全仓库无事件 |
| SRC-TENCENT-HUNYUAN | Research+正确publicList POST page1,size100,renderType0；total9逐条title/displayPublishTime实际Feb3→Sep21 2026 | 受阻 | 2025历史目录缺口，当前9不是历史0；恢复原发布后只重开目标邻段 |
| SRC-ZAI | Research+?page2/3实际响应，派生正文同18条Aug26 2026→Dec7 2025且没有更多；官方release notes Sep30→Aug11跨窗 | 受阻 | Research2025-09未恢复，已执行分页不能误记未执行；不授零事件 |
| SRC-BYTEDANCE-SEED | Research/type2 year2025 page0 count20 desc实际15/total49/has_more；置顶单列，非置顶Oct22→Aug20/13→July跨9月。type1同请求US/CN都total94/next20/has_more无sub_article_list | 受阻 | Blog有界停点已读；论文响应不完整，不记0，需实际条目/原发布 |
| SRC-BAIDU-ERNIE | 官方中文Blog1→2/2实际16标题，May9 2026→Sep12PLAS→Aug14→June30 2025跨窗 | 已检查 | 不重读窗外PLAS必要core；目录日期有限，不授全历史覆盖 |
| SRC-XIAOMI-MIMO | 官方8Paper/15Blog实际读取；fresh home chunk的More为已有array slice/状态切换；Paper Sep19→June4→May12 | 受阻 | Blog无日期；current Paper边界不授Blog历史0，需具体原发布区间 |
| SRC-MINIMAX | EN12条止Oct27，?page2派生正文相同；CN13止Jan15才跨9月；Agent index仅2026-05-13当前文章 | 已检查 | EN不能独自授跨窗；当前Agent入口不授历史不适用或0事件 |
| SRC-ARXIV | 12分类×八组主线术语，submittedDate Sep13T18Z→Sep14T18Z，start0/max200/total96，一页96标题、82完整摘要。catchup目标日400；正确month邻段skip800/show200原HTTP400、web Cache miss | 受阻 | 提交/current published/月份ID不授首公开；69潜力精确公告/版本区间隔离，不授全分类召回 |

只扫描Daily组和实际触发的原发布/必要卡片，无Weekly、其他月或全站附件队列。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

0正式当窗家族，未评分。69 arXiv潜力、Meta与OpenAI两家族均因必要日期/版本不确定留于§5，不提前写确定候选。与Books主题相似或访问成本不构成排除依据。

## 4. 证据与知识整合

### [GPT-5-Codex system-card addendum](https://openai.com/index/gpt-5-system-card-addendum-gpt-5-codex/)

官方落地核心与当前[七页PDF](https://cdn.openai.com/pdf/97cc5669-7a25-4e63-b15f-5fd5bdc4d149/gpt-5-codex-system-card.pdf)实际读取；仅保存条件化潜力，不授当窗采用。§2 pp3–4说明malware/双用途训练及coding注入评估，§4 pp6–7区分cloud隔离容器、local sandbox和可放宽网络/unsandboxed配置；模型行为概率不是执行授权。内部Table4两模型均0.98，但样本、CI和真实副作用分母未披露，不能推出所有泄漏/后门/破坏被防住；Table1退步类别的“自然噪声”只是厂商解释。卡片未披露完整实现/控制流审计，本次未运行攻击或复现。

RSS00Z不抹除PDF16:58:52Z创建/17:00:07Z修改反侧，后两项也不是首公开时刻；精确版本与落地事件分开。完整校准请求与实际owner论点见[FIRST_BATCH](../_sources/daily-20250915/FIRST_BATCH.md)。Ch72 `PLATFORM-SECURITY` 实际1245–1273已有独立policy/effect-time最小权限executor，764–812已有完整run/attempt与发布门禁分责；[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)104–118固定eligible population/scorer/uncertainty，邻接Ch71/73的隔离/发布责任另读。作者建议日期解决后机制NoChange、接口版本事实仅报告，不新增产品小节；root尚未独核，所以当前Books暂缓，不自授已有覆盖。没有必要长期差额证据则不制造自然段落或Books diff。

### [CyberSOCEval](https://ai.meta.com/research/publications/cybersoceval-benchmarking-llms-capabilities-for-malware-analysis-and-threat-intelligence-reasoning/)

官方完整摘要及原26页PDF必要pp6–10/12–14实际读取：默认provider thinking配置、不同模型/systemprompt对照不建立同模型同预算test-time scaling因果；只保留该任务配置的局部评价反侧，不采用训练scaling law或真实SOC能力保证。原页Sep15无timezone仍不能授落窗，不遍历其余附件。

root校准触发的九个精确v1必要安全/设计反侧已实读，连同Codex和Meta共11必要core家族；精确位置、实际读取角色、成立条件和未证明内容见[NECESSARY_CORE](../_sources/daily-20250915/NECESSARY_CORE.md)。11128v1为ENJ而非新版ERIS；11254反例的任意初始化/零向量QR有证明争议，均明确隔离，不因datehold免读，也不把局部core计为当窗采用或82篇全文。

其余82题摘逐项贡献与明确关闭理由见[SCREEN](../_sources/daily-20250915/SCREEN.md)。11191随机adversarial sampling的训练成本机制、11284三维GMM的directmap PoC、11337弱攻击/大batch的理论边界均保留，非因小模型/局部实验或理论而排除。11076 swap与11250 GUI攻击虽摘要都叫Chameleon，身份与命题不同，未合并。后续v2–v5不默认为重要修订，更不替代v1归属。

## 5. 缺口与下一步

尚可执行：root首批准入/日期/必要采用校准与非作者DAY，见[HANDOFF](../_sources/daily-20250915/HANDOFF.md)。作者研究ready不是独立验收。

外部隔离：OpenAI当前七页卡片的当窗原版本/公开区间，Meta CyberSOCEval原时区/区间，69 arXiv潜力的精确公告/原发布或重要修订，Hunyuan/ZAI目标历史、Seed论文完整数组、MiMo无日期Blog。重开接受官方原版本/更正、精确发布或完全落窗区间；不是一律请求秒级。日期/版本解决前不进入正式候选/Books，不授正面Coverage/Evidence、零事件、无遗漏、性能或安全保证。取得材料后仅重开对应ID与必要source/core，不重扫整类/月或以全部题摘变全文队列。

PDF当前创建/修改在窗外只是归属反侧，不反向假定首次公开必为16日；不扩张本窗恢复别日。明确关闭项日期未核但不影响贡献处置，不为它们另造日期请求。

## 6. 复核

复核者：root（首批准入/必要证据与Books），待指派非作者DAY。

结论：未通过。没有本日独立准入/DAY，未把作者core算非作者通过。建议首批11076/11155/11254/11167/11145/10963与10931/11128/11250风险，代表关闭10935/10937/11071/11198/12282，风险关闭11078/11136/13352/11369另核。所有潜力与未读/关闭范围见SCREEN，最终十四有限停点、日期隔离、候选/Books与六部分均需DAY；无须无差别重读全部附件。作者必要core窄补11家族已完成，见NECESSARY_CORE；结构检查先前通过，增补后重新校验，不替代语义验收。
