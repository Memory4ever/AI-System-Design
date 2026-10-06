# Daily Research — 2025-09-14

**规范：** V3
**窗口：** 2025-09-13T09:00:00+08:00 ～ 2025-09-14T09:00:00+08:00
**窗口说明：** 用户授权仅增量补查，原窗口、旧候选/日期/评分及连续§4冻结，不迁日或重算。
**补充窗口：** 2025-09-13 ～ 2025-09-13
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-12T01:58:35+08:00

## 1. 结论

原有效层冻结：0正式家族、0正式候选证据审阅、0 Books新增；69唯一当前版本中57完整题摘最终39日期潜力/18贡献关闭，另12明确范围的标题关闭。六风险精确v1必要支持与反侧、原日期与评分不重算，后续版本不倒填首次版本；[baseline](../_sources/daily-20250914/SUP_BASELINE_README_20261012.md)保留原文，旧复核不自动证明本次补查完成。

新增Sep13完整BJT自然日四主题94跨组命中，73唯一身份与原层交叉为48旧/25新。25份精确v1完整题摘、25当前comments/history轻层与10个必要局部实际读；7项准入歧义已经作者/独核方法和关键对照判为5P/2C，合计19明确潜力/6关闭。只有日期未知的19P不扩全文、不评分或冒充正式候选；submitted不是public。原39加新19共58日期潜力精确隔离。新增0正式、0正式Evidence完成、0 Books新写，不是零事件或全部Coverage/Evidence通过。

原10651/19322关闭、10860量词局部反侧恢复及风险采用边界见[旧初筛](../_sources/daily-20250914/SCREEN.md)和[旧独核](../_sources/daily-20250914/INDEPENDENT_DAY_REVIEW.md)。新增值得保留的潜力包括预训练多中心ID/OOD反退、MoE重组、GRPO探索、近似attention、shared control、输入格式失败归因盲区、辅助模态easy/hard反退、状态空间finetune冻结条件、小模型局部反侧与图语义核验scope；各不等于普遍性能/安全保证。[首批校准](../_sources/daily-20250914/SUP_FIRST_20261012.md)与[必要core](../_sources/daily-20250914/SUP_NCORE_SCREEN_20261012.md)保留实际位置/未读边界。普通研究已处理，Cicero本轮实际六部分DAY§5通过后同步日级安全终态；未把保留项授正面证据或覆盖。

## 2. 来源覆盖

原请求/停止依据见[transport](../_sources/daily-20250914/transport.json)、[原日期请求](../_sources/daily-20250914/date-probes.json)。新增请求与实际停止见[补充来源](../_sources/daily-20250914/SUP_SOURCES_20261012.md)：85请求/原件byte与SHA256逐项一致，81×200/2×400/1×404/1域名笔误无HTTP状态且已按当前script纠正重试；失败不授覆盖。以下为本日补充自然日范围，原来源有效层保留，不继承别日材料队列。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | RSS目标9月标题/description/pubDate实际读；Sep12T12Z CAISI/AISI→Sep15 Codex三事件跨Sep13 | 已检查 | 限定RSS，不授全站无删项 |
| SRC-ANTHROPIC | Next Flight JSON实际174 publication，Sep5biorisk→Sep15经济报告两个publishedOn/摘要跨窗 | 已检查 | 当前有限数组，不授已删发布覆盖 |
| SRC-GOOGLE-AI | Research 2025/09页1→2/2实际13标题；VaultSep12、cascades/NucleoSep11、scienceSep9。DeepMind页5/6标题/月读，原具名FSF/ICPC/Robotics日期Sep22/17/25有效复用 | 已检查 | Vault在新Sep13自然日窗外，旧hourhold冻结，不追小时或迁日 |
| SRC-META-AI | pubs5主序12项Nov18→Sep15、pubs6主序12项Sep8→Sep2→Jun13；Blog2/3混排逐条title/date读，page3主链Oct24→Aug27/14→July31，旧pin另列 | 已检查 | 非严格顺序目录，不授完整历史 |
| SRC-QWEN | config60对象，9月10条title/time实际读；NextSep10T20Z(BJTSep11)、ASRSep8、后批Sep21–24，均窗外 | 已检查 | 有限公开配置，不重复未变化core |
| SRC-DEEPSEEK | 官网及API updates目标链Sep29/22→Aug21跨窗 | 已检查 | 当前可见日志，不授首页全部历史 |
| SRC-MOONSHOT | Blog26条title/date实际读，Nov7→2024May29；Sep16→Sep5→Aug22跨窗 | 已检查 | 未扫全部PR/release |
| SRC-TENCENT-HUNYUAN | Research/runtime定位accept-language；publicList POST page1/size1000/renderType0，EN9与正确ZH11/total11全部title/displayPublishTime读，最早均Feb3 2026 | 受阻 | 四次Locale尝试仍返回EN9不冒充中文；2025历史未恢复，须官方历史目录/原发布，当前不是历史0 |
| SRC-ZAI | Research15普通卡片及page2=18题名/date读，page2无更多且最早Dec7 2025；当前release最早Sep30，不能沿用旧Aug11 | 受阻 | 2025-09历史未恢复，不是未执行分页，不记零事件 |
| SRC-BYTEDANCE-SEED | type2/year2025/page0/count20实际15/49及完整短摘，非pinOct23BJT→Aug21→Aug14→July，Sep9Seedream pin单列。type1 total94无数组，实际20→40→60→80；20仅June SwiftSpec，40/60空，80morefalse/next空 | 受阻 | 已到真实停止但论文数组不完整，不称94已读或0论文；需官方历史条目/原发布 |
| SRC-BAIDU-ERNIE | 页1→2/2实际16题名/摘要与footer原日期，May9 2026→Sep12PLAS→Aug14→Jun30 2025 | 已检查 | Sep12不含新窗，不扩旧PLAS/core |
| SRC-XIAOMI-MIMO | 8Paper/15Blog标题/描述读，PaperSep19→Jun4→May12；当前home6159 chunk的slice及state切换实读，More为本地展开 | 受阻 | Blog无日期，Paper不替Blog首公开日；需具体原发布日期 |
| SRC-MINIMAX | EN12最早Oct27，?page2同12派生正文；CN13最早Jan15。Agent当前三条2026Oct8/Sep22/Sep19及llms.txt三techblog说明实际读 | 已检查 | EN单独未跨窗；当前目录不证明2025无删项，不授历史不适用 |
| SRC-ARXIV | 12分类四主线主题，submitted Sep12T16Z→Sep13T16Z仅发现；start0/max200各组total=returned，共94跨组/73unique，48旧25新。25exactv1完整题摘/current轻层与10必要core读；Sep13 CL/LG日路径400是invalid period，不当外部访问故障；原同日合法monthly show250恢复层复用，仅month membership无日公告heading，不扩题摘队列 | 受阻 | 首公开日缺口，19新P精确隔离；6新C有贡献理由不另追日期，非法参数不授已穷尽；不授全部召回/安全/性能/Evidence |

本日未扫描Weekly、catchup或月库存；原三个具名metadata有效层复用，新按需仅动态目录必要runtime及10423精确v1 PDF fallback，没有普通仓库全扫。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

0正式家族，未评分。原39日期P、新19日期P不冒充当窗候选，6新C具体理由在首批与必要core。原57题摘/12标题及六风险有效层复用；新增25完整exactv1题摘已首批独核，7N实际方法/关键对照判5P2C，另3强正确性/控制/故障主张实际收窄，不按普通排除跳过。

## 4. 证据与知识整合

本日来源目录、原发布时间metadata与57完整题摘保留；六风险项精确v1必要方法/限制已实际读取并恢复校准，原HTML/派生txt和请求在同日_sources，[范围与反侧](../_sources/daily-20250914/NECESSARY_CORE.md)保留具体位置。PrivateDFL只支持累计Gaussian方差补足，不证明多次发布联合transcript DP；MetaSeal提取签名验证不等于绑定当前图像，原文仅supplementary内容检查，保留replay争议；GUI监督采用预录video非live控制；shutdown是可改写关闭script下的存在性反侧，非普遍自我保存；fault injection是有限synthetic PoC；diffusion smoothing半径限定Gaussian平滑图像classifier。未读代码或复现实验，不采用安全/性能保证。DeepMind三条published_time均窗外；Vault仅可见日期，不赋午夜或用别日core制造已审候选。

ROADMAP仅作潜力路由：MinatoLoader→TRAIN-DATA，JudgeQ→INFER-KV-CACHE，Kalman/goal-reaching→TRAIN-PRETRAINING，ToMA→MULTIMODAL-GENERATIVE-PARADIGMS，OpenHA/NavR1→MULTIMODAL-EMBODIED-VLA，评估负侧→PLATFORM-EVALUATION-SYSTEM，安全/隐私→PLATFORM-SECURITY。10651未建立该训练主线桥，已关闭；10748只保留VFM候选反馈/工具pointer的grounding接口条件，不采用手术/临床保证。没有完全落窗的采用事件，所有日期保留项不进入Books，未虚构owner实读、已有覆盖或整合段落；共享Books未改。

## 5. 缺口与下一步

尚可执行工作：无。Cicero本轮六部分DAY§5及完成态FINAL§6实际通过，作者据真实结果同步日级安全终态。来源/筛选及必要准入core实际完成，没有把普通未读正文、可修参数或未执行分页伪装成外部终态。下列本窗终态保留项不用于正面证据、Books、Coverage/Evidence或无遗漏断言。

本窗终态保留项：原39项arXiv首公开/重要修订日期（SCREEN身份冻结）、原VaultGemma小时口径hold不迁；新19日期P为2509.10369/10371/10372/10377/10396/10401/10406/10408/10416/10417/10423/10426/10439/10441/10446/10452/10694/10784/12267精确v1。缺指定版本官方公开日不是贡献被否定，非法日路径400不作为外部故障；本日原合法monthly有限恢复仍只有身份而无日级公告，submitted/current history不能证明public。不新扩月库存，接受指定ID官方公告或原始首次公开日期，仅按日判落窗，不要求时分秒；取得后定点重开该身份必要Evidence/评分/owner，不重扫整类/全文或迁旧归属。

来源终态保留项：Hunyuan/ZAI2025-09历史、Seed论文实际完整数组、MiMo无日期Blog；对应实际有限入口/停止见§2与来源笔记。接受官方历史条目数组及原发布、MiMo具体Blog原日期，定点重开本日来源缺段。它们不支持零命中、正面Coverage/Evidence、Books、性能或安全保证。明确6关闭项不为未知日期另发请求；窗外条目未审全部core不属于本窗待办。

## 6. 复核

复核者：Cicero（本轮作者Meitner之外）；原sept07_10_author/Bacon有效层冻结复用。

结论：通过

原独核全部57题摘/12标题与六风险、10860恢复/19322及10651关闭有效，不重复附件；本轮Cicero实际25精确v1完整题摘/current首批准入及7N关键方法/对照裁决，19P6C收敛，10426仅表示预训练条件不授World闭环。10必要局部记录支持与反侧，另48旧版本/AB一致与current comments窄核，无撤回/纠错信号，不授全历史。14源停止、日期/准入、证据层、Books未采用及完整六部分实际DAY§5和完成态FINAL§6通过，见[本轮独核](../_sources/daily-20250914/SUP_INDEPENDENT_20261011.md)。0正式/0Books不等owner已读或已有覆盖；6Markdown18本地引用0anchors、85原件SHA/bytes与原窗口/§4冻结、V3和限定unstaged/cached diff检查实际通过，cached空。未核代码、复现或全附件，机器层不代语义验收；最终行政回填只承接实际FINAL，不变更研究。
