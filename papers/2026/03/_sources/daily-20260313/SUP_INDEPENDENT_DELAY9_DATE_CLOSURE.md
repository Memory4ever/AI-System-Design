# 延迟九项：必要日期终态隔离非准备者复核

仅03-13既有日报补Mar12北京时间完整自然日；非准备者 mar13_admission_review，准备者root。启动实际重读AGENTS/current适用合同、Sources Daily/arXiv边界、Prompt、ROADMAP和本日停点；有效§23日期定义/原准入复用。只核这九项必要日期，不重建贡献或Source，不加载异日候选，也不以宽发现变全文队列。

## 实际读取范围

实际读[准备包](./SUP_ROOT_DELAY9_DATE_CLOSURE.md)、[九份OAI请求结果](./SUP_ROOT_DELAY9_DATE_MANIFEST_RESULT.json)、[venue请求结果](./SUP_ROOT_DELAY_VENUE_MANIFEST_RESULT.json)、九份具名 `SUP_ROOT_OAI_<ID>.raw` 的identifier/id/title/header datestamp、全部version date/comments；九份 `SUP_DATE3_<ID>.raw` 的官方DOI/URL、arXiv identifiers、client=arxiv.content/state=findable、created/registered、完整dateType/date/dateInformation及title/creator；九份缓存精确v1 abs title/作者/Comments/history与这些身份对应。

实际核 `SUP_THIRD_DATE_MANIFEST_RESULT.json` 中对应九个DataCite GET200 URL，原GET为2026-10-09T12:53:36–40Z；九OAI为2026-10-10T04:13:13–16Z GET200，metadataPrefix=arXivRaw，request与identifier均为对应精确2603.ID。没有将OAI网络读取时刻当原公开时刻。

另实际读取CVF/project/forum原raw身份/日期相关可见正文、meta与BibTeX（并核文本缓存）：[COT-FM CVF](./SUP_ROOT_COT_CVF.raw)、[作者项目](./SUP_ROOT_COT_PROJECT.raw)、[SERUM forum返回原件](./SUP_ROOT_SERUM_FORUM.raw)。SERUM API403由实际结果记录，不编造note内容。既有正常公告与不可预分配ID规则有效复用，不能从无日级分组的月导航或有界检索无结果推断九件日期。

## 九项逐件日期裁决

| 精确v1身份 | v1 Submitted日期（UTC，不是公开） | DataCite registered | OAI header datestamp | 裁决 |
| --- | --- | --- | --- | --- |
| 2603.13378 Do Large Language Models Get Caught in Hofstadter-Mobius Loops? | Mar10 | Mar17 | Mar17 | 必要日期隔离 |
| 2603.13385 VisualLeakBench | Mar11 | Mar17 | Mar17 | 必要日期隔离 |
| 2603.13389 Distribution-Conditioned Diffusion Decoding | Mar11 | Mar17 | Mar17 | 必要日期隔离 |
| 2603.13391 WebVR | Mar11 | Mar17 | Mar17 | 必要日期隔离 |
| 2603.13394 Language-Guided Token Compression with Reinforcement Learning | Mar11 | Mar17 | Mar17 | 必要日期隔离 |
| 2603.19296 TTQ | Mar11 | Mar23 | Mar25 | 必要日期隔离，更新不改注册上界 |
| 2603.18034 Semantic Chameleon | Mar10 | Mar20 | Mar20 | 必要日期隔离 |
| 2603.13395 COT-FM | Mar11 | Mar17 | Mar17 | arXiv日缺口；同稿CVPR dated公开原件未得 |
| 2603.13396 SERUM | Mar11 | Mar17 | Mar17 | arXiv日缺口；具名ICLR note原公开日未得 |

九份DataCite Available都仅2026-03、Issued仅2026，不能给Mar12；其Updated是Mar17/20/25 v1元数据时间，也非firstpublic。所有OAI只给v1提交记录，没有额外公开公告日期字段；header是记录元数据变更日期。较早Submitted和正常公告日程只给可能范围，较晚注册只给上界，跨窗不能当确定Mar12，也不能据晚注册宣称确定窗外。九项题摘当前可见history仅v1，无所读Comments中的撤回/纠错信号；不为排除标记遍历版本史。

## Venue与停止范围

13395 CVF同题五作者、pp11515–11524、直接2603.13395链接；Bib June2026及citation_publication_date=2026只支持会议身份。作者项目同题/五作者、直接2603.13395v1、Accepted at CVPR2026，meta没有原published-day，Bib只有2026。原作者姓名连字符差异与直接ID身份一致，但该单篇恢复未给早公开日期；不把后会议出版当论文首次公开，也不要求证明全网没有早稿。

13396原abs/OAI Comments为Accepted as ICLR2026 Poster。指定forum `AiBUm6iKBf` GET200实际final URL是challenge redirect，原件标题/正文为Verifying your browser；API2 notes?id同ID记录403。challenge的redirect目标能核访问对象，**不能认证note正文、作者身份或原公开日期**。索引/PDF线索只作具名恢复入口；恢复条件必须兼有同稿身份与官方公开日期，不能由会议年或搜索抓取年龄签章。未绕过挑战或反复追查完整会议库。

本日既有合法月列表有限导航原件 `SUP_ARXIV_11137_HIST_LG.raw/txt` 与其请求结果支持的是skip0/show25的月份入口，非历史日公告、非全4527条覆盖；本次定点回读入口显示该粒度，复用此前有效历史恢复限制。未把它扩成全月扫描，也不说它证明这九项绝无Mar12公告。现有有限原始入口未恢复决定落窗的日期，继续读论文全文不能补这一必要门。

## 精确终态、请求与重开

**九项必要日期终态隔离通过；不是日期PASS、窗外排除、贡献EX或普通全文未读转外部受阻。** 它们保留此前完整题摘潜力，不计确定本窗候选、不评分、不授Source/Evidence通过、不入Books、不支撑无遗漏。未审普通项不能援用本包清除。

同一请求只需一次：提供包含对应精确ID的当期官方arXiv公开公告/历史日列表快照，或能验证同稿身份的原作者dated首次公开正文。13395可用同稿作者/CVPR原始公开记录；13396可用AiBUm6iKBf官方note同稿身份与原公开日期。只需日，不追时分秒。先解决哪个ID就只重开哪个日期；确认Mar12新事件才继续必要评分/证据，确证早稿或窗外再按具体事件去重/排窗，不重扫月份/年份。

该裁决只接受有限恢复后的安全隔离，未授权正式Report同步、Source/Books或DAY；无共享文件改动或stage/commit/push。
