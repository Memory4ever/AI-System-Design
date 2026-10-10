# 收窄十项：非准备者 arXiv 事件日独核

复核者：mar13_admission_review；准备者：mar14_supplement。2026-10-10 执行，仅 Daily 2026-03-14 补充 2026-03-13 北京时间自然日。只拥有本文件，不写 Report、Books、State 或主 ledger；不加载 03-13 研究材料。

## 实际范围与原件

换日后实际重读 AGENTS、当前研究/Report 合同、统一 Prompt、来源说明/Daily 组/arXiv 范围、ROADMAP 与本日路由/README §1、§5 停点。按 context-engineering 技能隔离前日与本日判断，保留既有有效结果；本日进行中与宽标题不是全文队列。本包只核十个 arXiv 日级事件，不授候选贡献、评分、必要 Source、Books 或 DAY。

完整读 [SUP_DATE_NARROW.md](./SUP_DATE_NARROW.md)；直接读 `SUP_DATE_NARROW_MANIFEST.json` / `_RESULT.json`，逐份解析以下十份实际 `SUP_DATE_<ID>.raw` 的 `data.id`、`doi`、official abs URL、client relationship、state、publisher、title/creators、created/registered/current metadata updated、**全部 dates** 与 relatedIdentifiers。十 DOI 均为 `10.48550/arxiv.2603.<ID>`，URL 均为 `https://arxiv.org/abs/2603.<ID>`，publisher=`arXiv`、client=`arxiv.content`、state=`findable`；十份 GET200，UTC2026-10-10T01:35:41–45，final URL 均对应原精确 DOI。

另实际读十份 `SUP_ABS_<ID>.txt` 的精确 v1 题名、全部署名、当前 Comments/相关 DOI 与完整可见 submission history，对回 DataCite；`SUP_NARROW_AB_MANIFEST_RESULT.json` 十份原 URL/final URL 均为对应 `https://arxiv.org/abs/2603.<ID>v1`，GET200 / UTC01:28:06–09。有效完整摘要准入判断复用，本包不重做贡献或正文审阅。页面所读说明未显示撤回/纠错标签；后 v2 的存在不自动证明重要修订，不遍历旧版或后版正文。

## 十项原字段与日级结论

下列时刻只保留原字段用于复查，不是新的小时级筛选。`Updated v1` 是 dates 中的版本元数据字段，不能独立作公开；registered 也只作结合官方规则的上界。

| ID | v1 Submitted（UTC） | dates Updated v1（UTC） | registered（UTC） | 本 arXiv 事件日 |
| --- | --- | --- | --- | --- |
| 11611 | Mar12 07:05:13 | Mar13 00:29:28 | Mar13 01:59:32 | 2026-03-13，通过 |
| 12248 | Mar12 17:57:50 | Mar13 01:05:49 | Mar13 02:14:13 | 2026-03-13，通过 |
| 12149 | Mar12 16:47:42 | Mar13 01:01:08 | Mar13 02:11:59 | 2026-03-13，通过 |
| 12089 | Mar12 15:57:32 | Mar13 00:57:28 | Mar13 02:10:36 | 2026-03-13，通过 |
| 11253 | Mar11 19:26:04 | Mar13 00:06:51 | Mar13 01:51:17 | 2026-03-13，通过 |
| 11248 | Mar11 19:13:54 | Mar13 00:06:36 | Mar13 01:51:10 | 2026-03-13，通过 |
| 11757 | Mar12 10:04:05 | Mar13 00:38:37 | Mar13 02:02:59 | 2026-03-13 arXiv 通过；家族门保留 |
| 11414 | Mar12 01:04:32 | Mar13 00:16:24 | Mar13 01:55:01 | 2026-03-13，通过 |
| 11975 | Mar12 14:25:44 | Mar13 00:51:33 | Mar13 02:08:02 | 2026-03-13，通过 |
| 12249 | Mar12 17:57:52 | Mar13 01:05:50 | Mar13 02:14:15 | 2026-03-13，通过 |

十份 `dates` 均还含 Available=`2026-03`（v1）与 Issued=`2026`，没有日精度，不能补造日期。六份仅 v1 日期组；四份可见后 v2 组及 abs history 一致：

| ID | dates Submitted v2（UTC） | dates Updated v2（UTC） |
| --- | --- | --- |
| 12248 | Mar16 16:07:55 | Mar17 02:31:01 |
| 11253 | Mar13 16:15:23 | Mar16 00:58:05 |
| 11975 | Mar13 10:53:52 | Mar16 00:41:53 |
| 12249 | Apr29 04:59:09 | Apr30 00:24:04 |

created 全部 Mar13 UTC，registered 最晚 Mar13 02:14:15 UTC；current metadata updated 中四后 v2 项较晚，只是元数据后更新，不改变 v1 事件日。本复核实际读了这些字段，不把注册/更新时间或晚 v2 当论文首次公开。

## 夹证为何成立

复用本日已有效独核的 `SUP_AVAILABILITY.raw/txt`；本轮再直接读 txt134–187 的原说明与日程：最终 ID 在公告流程中分配、ID/DOI 不可预先提供，提交经历 moderation 后才公开；Wednesday14→Thursday14 Eastern 的最早正常公告是 Thursday20 Eastern。十个 v1 submission 全明确晚于 Wednesday 截止、早于 Thursday 截止，没有本日11161的等号歧义。由这份已核正常公告规则得到最早 Mar13 北京时间下界，结合同日官方 arXiv owning DOI 的注册上界，夹到 Mar13 自然日；若有 moderation 延后，上界仍把这些十项限制在同一天。

这不是宣称精确公告时分秒，也不是“submitted 就公开”“registered 就首次公开”或官方月 ID 能独立证明日级。所授范围仅十项的 arXiv 本事件日，不代表各家族全球首次公开或全部来源都无早稿。

12149 当前 Comments 仅 `Accepted by CVPR2026`，没有在这些原件中指向具名已知早公开正文；不为纯接受信号构造证明全网无早稿的日期请求。12089 `Work in progress`、11253 的页数说明、11414 的页数/图表说明不是本包日期纠错证据。未扫描会议、作者全站或全版本。

## 两项特定边界

**12249 题名差异保留。** 当前 DOI registry 是 `SciMDR: Advancing Scientific Multimodal Document Reasoning`，精确 v1 abs 是 `SciMDR: Benchmarking and Advancing Scientific Multimodal Document Reasoning`。实际同官方 ID/URL 与六署名顺序 Ziyu Chen、Yilun Zhao、Chengye Wang、Rilyn Han、Manasi Patwardhan、Arman Cohan 一致，可识别同家族/精确 v1；不能写成逐字同 title，也不能由改题名推断已核重要修订。

**11757 arXiv 通过不消 TechRxiv 家族门。** 本 ID 的 DataCite `IsVersionOf` 指向 `10.1109/tcds.2025.3648042`；实际 v1 abs 也显示该 Related DOI。直接读 `SUP_VENUE_11757_CROSSREF.raw`：IEEE 记录同题、五作者同序，resource 为 `https://ieeexplore.ieee.org/document/11313796/`，关系 `has-preprint` 具名指向 `10.36227/techrxiv.171177240.03554657/v1`。这与纯投稿/接受不同，确实存在必要同稿先公开身份/日期线索。

Crossref created=`2025-12-24T18:47:28Z` 不是 first-public；published/issued/print 仅2026年8月，published-online 无日值，不能把后出版日移作首次公开或宣称已经2025公开。本次按 parent 范围不扩大恢复，精确需求仍是该 TechRxiv v1 官方可读同题/署名完整摘要或正文身份及原 posted/publication date（或 IEEE/TechRxiv 官方 exact DOI 元数据配原题摘）。未消解前不以 Mar13 arXiv 事件自动授家族当窗候选/评分/Source/Books，不提前判 OUT。合格材料到达只重开该具名同稿事件与必要增量，不遍历 IEEE/作者全站。

## 结论

有限十项的 **Mar13 arXiv 日级夹证通过（10/10）**；其中11757家族首次公开门仍保留，12249题名差异已记录。有效准入与正文独核各自复用/继续，不因日期通过增设全文队列。只完成本日期小包；不授 Source、评分、Books 或 DAY。
