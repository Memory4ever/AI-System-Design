# Sep26：具名线索的首次日期准备

本文件按实际接受顺序记录作者6、28、42各自让出的五项日期域，采用状态分开。只准备身份、版本、已见早稿线索与S/L/U，不接管题摘贡献、分数、Methods、owner或报告。目标补充日2025-09-25 BJT；旧候选不移动。

## 原件和日期判断

首次十GET于2026-10-25T04:22:09.111901+00:00至04:22:17.983385+00:00真实完成，均HTTP200/exit0；本目录 `ROOT_DATE_2509_<五位ID>_ABS_20261025.raw` 与 `..._DOI_20261025.raw` 及各自同名 `.request.json` 保存精确URL/UTC/状态/字节/SHA。root已实际回读身份、history/comments和DataCite完整日期/关系字段并复算字节/SHA。发现元数据沿作者6已存MODEL/SYSTEM SCOPED原件复用，不重取同一列表。

五份DataCite均为同一精确 `10.48550/arxiv.2509.<ID>`，client `arxiv.content` / type `clients`，provider `arxiv`，state `findable`。U只用registered，不把created、Updated/v1、月份或Submitted改名为公开时刻。按合同已核2025纽约EDT公告规则复用L，不重新调查共同规则。

| 身份 | v1提交S（UTC） | 最早可能公告L（UTC） | registered U原字段 | 有限结论 |
| --- | --- | --- | --- | --- |
| [19729](https://arxiv.org/abs/2509.19729v1)：DataCite题名Amoeba；当前所取ABS/HTMLv1题名Gyges，详见下节 | 2025-09-24T03:15:37Z | 2025-09-25T00:00:00Z | 2025-09-25T01:51:48.000Z | L≤U，全区间BJT Sep25 08:00～09:51:48；只限该arXiv公告日 |
| [19836 BurstEngine](https://arxiv.org/abs/2509.19836v1) | 2025-09-24T07:27:40Z | 2025-09-25T00:00:00Z | 2025-09-25T01:54:18.000Z | 全区间BJT Sep25 08:00～09:54:18 |
| [19781 Task-Aware Expert Merging](https://arxiv.org/abs/2509.19781v1) | 2025-09-24T06:04:10Z | 2025-09-25T00:00:00Z | 2025-09-25T01:53:01.000Z | 全区间BJT Sep25 08:00～09:53:01 |
| [19368 PPSD](https://arxiv.org/abs/2509.19368v1) | 2025-09-19T04:51:41Z | 2025-09-20T00:00:00Z | 2025-09-25T01:43:24.000Z | 跨日，不能由组合限定Sep25，不能截取U日或S日 |
| [19592 Frame-Stacked Local Transformers](https://arxiv.org/abs/2509.19592v1) | 2025-09-23T21:31:00Z | 2025-09-25T00:00:00Z | 2025-09-25T01:48:36.000Z | Sep23已过18Z截止，下一可公告为Sep25 00Z；全区间BJT Sep25 08:00～09:48:36 |

前三项及19592仅得到精确arXiv v1公告日的有界推断，不证明全球首次正文、实际秒或当前HTML逐字等于2025正文。19368保潜力与具体缺口，不自动准入/评分或以跨日抹去贡献。

## 身份变化和已见具体发布入口

- 19729同一ID、v1 S和六作者与DataCite一致，但DataCite保留题名 **Amoeba: Runtime Tensor Parallel Transformation for LLM Inference Services**，当前精确v1路径ABS及HTML返回 **Gyges: Dynamic Cross-Instance Parallelism Transformation for Efficient LLM Inference**。为核此具名差额实际取 `ROOT_DATE_2509_19729_HTMLv1_20261025.raw/request.json`，200/exit0、216801B。只读题名/作者身份及外链，不审Methods或将改名自判重要修订；当前history可见v2于2026-04-22T06:30:11Z，comments 12 pages/15 figures，无具名更早发布日。此题名/版本呈现差异必须在作者准入和精确正文采用时保留，不能把DataCite旧题名与当前正文默称历史逐字一致；不否定稳定ID所支持的公告日期界。
- 19836唯一v1；已见[官方代码仓库](https://github.com/thunlp/BurstEngine)实际定点日期检查。`ROOT_DATE_BURST_REPO_20261025.raw/request.json` 200，created_at=2025-09-23T11:37:28Z、pushed_at=2025-09-25T02:42:22Z、default_branch=main；仓库创建不是论文正文公开证据。raw README一次连接重置（exit35/HTTP0/0B），未记空页面；随后官方Contents API `ROOT_DATE_BURST_CONTENTS_20261025.raw/request.json` 200取得README，blob `4fdd5a24c857a857eb08b337a69de84515818ca8`，实际base64解码后查看日期/论文链接/页尾：链接同一arXiv ID，无明确dated news/首次正文日期。仅有限当前README检查，不运行代码/不追全部commit或由当前链接回推Sep23已公开正文。
- 19781当前所见v2提交2026-01-23T03:46:38Z；ABS题名与同DOI一致，无comment、具名项目或更早日期线索。19592 v2提交2026-01-22T19:37:17Z；IEEE submitted评论不证明正式发表或更早正文。所见字段未提示撤回/勘误，不声称已读全版本内容。
- 19368当前所见仅v1，comments 17 pages/7 figures、六作者及同DOI一致，无直接项目链接。为查看具名日期/早稿入口，实际取 `ROOT_DATE_2509_19368_HTMLv1_20261025.raw/request.json`，200/exit0、373156B；所见题名前加PPSD，作者一致，未见作者项目外链或明确公告日期字段。只核身份/日期线索，未读Methods。另在2026-10-25定点搜索 `"2509.19368" "25 Sep 2025"`、`"2509.19368" "24 Sep 2025"`（arxiv.org）和完整题名+September2025（arxiv.org/teleai.com.cn），返回同一arXiv身份/提交日及无关文献，没有直接官方公告日；搜索时间/索引日期不作证据。官方Advanced日参数的已成[最小原证](../daily-20250919/ROOT_ADVANCED_DATE_20261023.md)复用：月精度入口不授历史单日零命中，不catchup、不重GET共同规则。当前具名入口有限检查已做；仍需官方可核公告/public日期或作者明确dated正文，才能只重开此日期判断。不能从Updated/v1 Sep25或登记日单独补成Sep25公开。

以上均不建立全网无早稿保证；无具体新线索时不无限追假想发布渠道。当前官方撤回、纠错、安全或实质修订轻量检查仍由作者在实际准入层处理。

## 输入定位和交接

首次十原件实际字节/SHA：

| ID | ABS bytes / SHA256 | DOI bytes / SHA256 |
| --- | --- | --- |
| 19729 | 42107 / `3781f882ae5b8051bb706251e98b69db6892bbaf6dd27686efc2a62955e8f3c9` | 9128 / `d320eeb05d827e27dbe89773305861c2f0e86cc9097d29fcc0574bd69f0a5094` |
| 19836 | 42902 / `14c29c9939854236556903c8237a2cb3b3d489288316c2149262bd199ef4b4cd` | 10099 / `5cb37eea5f4dae949256437b4f30fb376402e9024ef9bf4f63407f7de386000a` |
| 19781 | 43689 / `c59a66d40f25212b6d92cb6f825f49a70a3045ad112e5ec2a37c60de8233dcce` | 10549 / `5c54f2cd9e09794294bef3146113dc6ca36cf5f7f5538edfd5baf94ceee75e2e` |
| 19368 | 43949 / `b857a527ff77bfcee0960ca6c7de78b17443ad3f7e245f993916c0d064434432` | 10973 / `3514bd0761d72ad0b10293234dbdbb923cdfe7d152d4b7705dc603b8c7a66eb1` |
| 19592 | 43320 / `3251455230cfb8c3dd40994620e2317495aa51305fd345eddd1090b1721a4489` | 12596 / `0f95fc067d744211a7af34ee24112e41def050cf9819e20a9e3e0da0246e731d` |

作者实际读本包及必要原件后采用一次，Einstein仅角色/范围复用，不第三同域日期取证；新AB贡献/分数/必要/owner均仍作者首次域。此包不预四篇正式准入，不把19368或题名差异批量改为整篇终态，不授Coverage/Evidence、Books或日报完成。此首批后来已由作者15实际采用；不由它预授下列新批日期域。

## 作者28新增五日期域：首次准备已真实完成

root明确接受19702/19839/19858/19893/20020日期首域后，十个精确ABS/DOI GET真实完成于2026-10-25T05:49:48.169205+00:00至05:50:00.435080+00:00，均200/exit0/无在途。原件仍按本目录 `ROOT_DATE_2509_<ID>_ABS_20261025.raw` / `..._DOI_20261025.raw` 与各同名request定位；root实际完整读身份/header、Comments/Submission history和DOI的原日期/relationship，复算各字节/SHA。没有题摘贡献/Methods首读，不以日期完成预候选或分数。

五精确DOI身份/title/可见作者/v1 S能对上同family，client均arxiv.content/clients、provider arxiv/providers、state findable。19893题名呈现差异另记下。各S均Sep24周三14EDT截止前，适用已成2025规则给L=Sep25T00Z；每个L≤U且整个区间为BJT Sep25 08:00至下列U的09时，故各自只限定arXiv v1公告日2025-09-25，不把S/registered/Updated或端点改名实际公开时刻，不认证全球first/历史同bytes。

| 精确v1身份 | 原S（2025-09-24 UTC） | 原registered U（2025-09-25 UTC） | ABS bytes / DOI bytes |
| --- | --- | --- | --- |
| [19702 Linear Transformers Implicitly Discover Unified Numerical Algorithms](https://arxiv.org/abs/2509.19702v1) | 02:19:04 | 01:51:11.000Z | 41104 / 8782 |
| [19839 LatentGuard](https://arxiv.org/abs/2509.19839v1) | 07:31:54 | 01:54:23.000Z | 43001 / 10961 |
| [19858 Benchmarking Gaslighting Attacks Against Speech Large Language Models](https://arxiv.org/abs/2509.19858v1) | 07:57:10 | 01:54:50.000Z | 43597 / 11077 |
| [19893 Future Policy Aware Preference Learning for Mathematical Reasoning](https://arxiv.org/abs/2509.19893v1) | 08:44:12 | 01:55:39.000Z | 43425 / 9928 |
| [20020 The Syntax and Semantics of einsum](https://arxiv.org/abs/2509.20020v1) | 11:36:02 | 01:58:38.000Z | 40386 / 9853 |

各DOI原created分别为U前一秒，唯20020为与U同秒；都只行政创建字段。Updated/v1分别Sep25T00:18:53/00:30:51/00:32:46/00:35:35/00:43:40Z，Available均2025-09，不用它们代公开日。relatedIdentifiers均空。精确v1唯一提交S与同DOI dates Submitted/v1一致；19702四作者、19839三作者、19858六作者、19893四作者、20020当前header四作者与DOI creators相合，未由PDF导航的“other authors”简句重建历史名单。

实际已见版本/comments/具体入口范围：

- 19702仅所见v1，comment To appear at NeurIPS2025，不由录用/将发表证明另日早正文。
- 19839仅所见v1，comment详细列NeurIPS preprint template/页图表/编译材料，无具名更早日期；模板不等会议正式接收或安全已验证。
- 19858 v2提交2026-05-22T14:38:31Z，v1 comments 5pages/2figures/3tables；本次不以版本号自判重要修订或倒填后版实验。
- 19893精确v1路径header是 **Future Policy Aware Preference Learning for Mathematical Reasoning**，DataCite仍题为 **Future Policy Approximation for Offline Reinforcement Learning in LLM Reasoning**；同ID/四作者/v1 S相合，保此呈现差异供作者精确AB与必要采用，不默认只改名/历史全文逐字同版。v2 Apr3、v3 Aug19 2026分别后事件，不给本窗新版贡献。comments仅9pages。
- 20020 v2提交2025-10-06T14:35:42Z、v3 Oct20T13:29:52Z；comment给21pages/1figure与形式定义/证明/nesting范围，不独立证明任何保证成立。当前v1 header作者列表可读，导航“2 other”简句不覆盖它，未由这些字段认证历史逐字作者/全文。

五篇当前所取ABS的作者正文区域没有项目/代码/会议forum/第三方早稿DOI外链，只有各自arXiv DOI；辅助页脚工具链接不算作者发布渠道。原comments/history未见撤回、勘误或明确早稿日；这里不等完整新版内容轻查已由root完成，更不证明全渠道无早稿。无具名早稿信号时有限停止，不追假想所有作者主页/代码史；若作者后续在AB/current事件发现真实纠错、修订或早正文线索，仅定点恢复。

十原件实际SHA256（完整请求字段在同名request）：

| ID | ABS | DOI |
| --- | --- | --- |
| 19702 | `67d1208e364f13936f9ee8a34ea575b3362ba4615463c22b4fe0710091352688` | `81ac7424e95938de59db26fcb825d3ef20cafb8fd73c3584d8859142bf3bac52` |
| 19839 | `d2c9c7ad3aef4879d656186d279c3ea5d03f378c35e0052022a19527457f72cf` | `fba7fd30219948ef0b0a4222f82a17fd7287e40d533646d3579345c35b9e5f86` |
| 19858 | `988e42dc6090ac486c3697e47dc85162170d8db57e7524049650d2f5d270375b` | `1e3027f9a15c4efdc78f0c12ffcd2de68370fc66d5004ace27ff65b52f530fdc` |
| 19893 | `106194cd63d65d86fda228991921c0610593c84fcbb1c8faa4a9fb97c7caf063` | `c959f369239b3e45f5034d1585ad4bd440ba367239299a050f8b932bd3d2985d` |
| 20020 | `d2748521ab943e6a6c42c481cf42d8ed9b5fbcb39ef1e1ff06d0dc9c405b1f4b` | `19c9fe7b0d8db1197e941595218ff7ea4efd751a08783e8ea20b86156087a957` |

本新批首次日期准备已真存，交Aristotle唯一另一角色实际采用后才闭合，Einstein随后只角色/组合范围复用，不第三date GET/首备。原metadata题摘P不被它自动变成exact-v1准入、首次分/必要完成或Books；五项这些新层仍writer责任。旧材料日期/分数/原小时窗不改，未DAY/FINAL。

## 作者42新增五项：跨日区间及具名原始出口

root明确接受19322/19325/19358/19360/19364的未开始日期域；十份精确ABS/同DOI原件已经真实取得、实际读回身份/history/comments及登记字段，2026-10-25再复算字节与SHA均相合。原件仍用本目录 `ROOT_DATE_2509_<ID>_ABS_20261025.raw` / `..._DOI_20261025.raw` 及同名request，不另复制。19322 ABS请求开始于07:09:25Z，其余九次于07:10:29～07:10:42Z结束，均200/exit0。只接身份、公开日期和具体早稿线索，不接作者的贡献/评分/必要审阅域。

五项精确ID、题名、v1 S和可见作者与同DOI对应，client为arxiv.content、provider arxiv、state findable。2025 EDT日程复算时，周五14点后的提交进入周一截止、周一晚公告；周五截止对应周日晚公告。以下L只是最早可能公告界，审核可延后；U仍是登记上界，不是实际公开时刻。

| 精确身份 | v1 S（UTC） | L（UTC） | registered U（UTC） | 结论 |
| --- | --- | --- | --- | --- |
| [19322 Readme_AI](https://arxiv.org/abs/2509.19322v1) | 2025-09-12T20:34:58Z | 2025-09-16T00:00:00Z | 2025-09-25T01:42:19.000Z | 跨多个BJT自然日；另有下述七月早披露 |
| [19325 How Much of Your Data Can Suck?](https://arxiv.org/abs/2509.19325v1) | 2025-09-13T18:55:52Z | 2025-09-16T00:00:00Z | 2025-09-25T01:42:24.000Z | 跨日，不能截取Sep25 |
| [19358 Personalized Generation/PERG](https://arxiv.org/abs/2509.19358v1) | 2025-09-18T13:56:14Z | 2025-09-19T00:00:00Z | 2025-09-25T01:43:10.000Z | 跨日，不能截取Sep25 |
| [19360 Semantic Representation Attack](https://arxiv.org/abs/2509.19360v1) | 2025-09-18T15:06:46Z | 2025-09-19T00:00:00Z | 2025-09-25T01:43:13.000Z | 跨日，不能截取Sep25 |
| [19364 Offline LLM Evaluations](https://arxiv.org/abs/2509.19364v1) | 2025-09-18T20:41:20Z | 2025-09-22T00:00:00Z | 2025-09-25T01:43:19.000Z | 跨日，不能截取Sep25 |

19322/19325/19358/19364当前只见v1；19360另有Oct20 v2，不倒填其贡献。19358评论是first draft/first camera-ready，19364是forthcoming Patterns；这些都不是单日公开记录。19358的Updated/v1为2026-08-06，不能代替2025首公开或仅凭此认定历史全文相同。

本批有限恢复实际还处理了以下入口，未遍历作者全部主页、提交史或假想渠道：

- **19322早披露。** 官方[NIST摘要集入口](https://www.nist.gov/document/2025-surf-abstract-book)已真实重定向至[2025年7月29日路径的PDF](https://www.nist.gov/system/files/documents/2025/07/29/2025-SURF-Abstract-Book-final.pdf)，请求07:27:51～07:28:14Z、200/exit0，70826806B，SHA256 `779990a117b72fd3ee382fa8fe143a932c28cb9e27b75ef1fbf2297e501a18e3`，原件 `ROOT_DATE_19322_NIST_ABSTRACT_20261025.raw`。175页只机械搜索具名标题定位，实际完整读封面/前言、物理页7/72的日程与标题及**物理页80**的完整具名摘要。该页明确July29–31,2025、Millie Vyas/Purdue、导师Timothy Blattner及Readme_AI标题，并披露JSON规格、数据owner提供内容、git下载、FastMCP和网页/PDF入口及Hedgehog演示；因此这些机制有七月官方摘要披露，不能作为Sep25全新机制。PDF创建/修改字段及URL路径不单独充当网络公开日，也未证明九月论文全文当时已存在。当前GitHub README另以官方Contents API实际取得并完整解码读回，200/exit0、2945B，SHA256 `394f12db07a450e94de2cc7c25d18a7519488722703a8fcfbd109dc7fab5d4ff`；它没有dated news或精确早正文日，安装说明未执行。作者须区分具体拟准入增量，不能因此把整篇论文自动W或自动first。
- **19325作者机构入口。** 2026-10-25实际读[Invisible官方Research](https://invisibletech.ai/research)的本篇条目及原始论文链接；它确认身份，但没有发布日期。没有把页脚2026、搜索抓取日期或转载日期改成论文日，也不扩扫全机构。
- **19358出版方与作者项目。** 实际读[ACL条目](https://aclanthology.org/2025.findings-emnlp.870/)的题名/六作者/日期元数据，正式卷期为November2025，不限定九月arXiv单日。另实际查看作者[项目README](https://github.com/MichiganNLP/Benchmark_Improve_LLM_Robustness_in_Personalization)的标题、目录及有无日期/论文入口，未见dated news；没有把当前代码存在、121 commits或后来的正式发表当早稿时间，也未首审其方法。
- **19360作者项目。** 实际查看[官方SRA仓库](https://github.com/JiaweiLian/SRA)的完整README、citation与公开入口；同题/六作者、NeurIPS2025引用均能对应，但没有精确公开日期。未运行安装、攻击或评测，未遍历提交史，不用当前引用回推Sep18或Sep25。
- **19364作者实验室。** 实际完整读[RegLab具名条目](https://reglab.stanford.edu/publications/the-inadequacy-of-offline-llm-evaluations-a-need-to-account-for-personalization-in-model-behavior/)：三作者一致，日期仅ArXiV, September2025，Read More指同一arXiv。月份不补成单日；不扩扫全部实验室出版物。

官方 `https://arxiv.org/list/cs.CL/2509?show=2000` 的一次请求07:13:10～07:13:11Z返回429/exit0、14B；原件 `ROOT_DATE_ARXIV_CL_MONTH_20261025.raw`，SHA256 `467622e2f17f01d302d6c790b13078569f17d71cd83910558535019a594e07c1`，web入口也明确429。不重试绕过限流、不把它作零篇/全部月份已读或这五项日期证据。Advanced已成月精度限制直接复用，不catchup。

上述有限日期域已准备完成，交作者实际采用；新贡献判断仍须看完整精确题摘。四项目前仍缺能缩短跨日区间的官方公告/作者dated正文，19322还须按早披露限定拟采用命题。若贡献明确不准入，可按合同停在具体理由，不为无关日期无限恢复；若仍拟准入且现有具名入口不能限定日，则将这一项具体隔离并留下重开条件，不能把普通可执行工作一起归零。无全球first、历史逐字、覆盖无遗漏或日级完成保证。

## 作者72新增五项：公告限日与两个具名早披露线索

root本轮明确接受20208/20214/20317/20328/20336未开始的日期首域后，十个精确ABSv1/同DOI请求于UTC2026-10-25T10:18:06.302350～10:18:16.316022真实结束，全部200/exit0；原件为本目录 `ROOT_DATE_2509_<ID>_ABS_20261025.raw`、`..._DOI_20261025.raw`与同名request。root实际读完整身份/header、comments、subjects、submission history、作者正文区全部原始外链与DOI身份/creators/所有dates/relationships，重新核对字节与SHA。没有重做完整题摘贡献层或首Methods，不替作者打分。

五项精确ID/题名/作者数3、2、8、9、6及唯一v1 S均与同DOI相合，登记方均arxiv.content/clients、provider arxiv/providers、findable。S在NY周三14EDT截止前且晚于前一截止，已成2025规则给最早可能公告界L=2025-09-25T00Z。各L≤registered U，整个区间BJT Sep25 08:00至下列09/10时都在同日，故仅各arXiv v1公告限Sep25；不是S或登记的实际公开时刻，也不自动是全球first。Updated、created与月份Issued/Available均保原字段，不作独立公开日。

| 精确v1身份 | 原S（Sep24 UTC） | registered U（Sep25 UTC） | ABS bytes / SHA256 | DOI bytes / SHA256 |
| --- | --- | --- | --- | --- |
| [20208 Type Rules](https://arxiv.org/abs/2509.20208v1) | 15:02:33 | 02:03:06.000Z | 40862 / `52a2432d9a382349478427c5c04dc4f9f784ae9408f33e9acdc898c7cc260772` | 8841 / `3624132a37e24d8d5f91e0415e79ba1c28467e4eb652c35d55ef6da6a1120b27` |
| [20214 Q-Palette](https://arxiv.org/abs/2509.20214v1) | 15:10:44 | 02:03:14.000Z | 44173 / `de82f69c688cadcf84caada1802a7fe9537873b7da14ccc1acf106a28ef154c8` | 9751 / `9796ad14e4c14aad6d470288bc502fc99339c6373716438fd8e1e05a6d220b19` |
| [20317 SIM-CoT](https://arxiv.org/abs/2509.20317v1) | 17:01:32 | 02:05:39.000Z | 43418 / `33fa6f4d1e00f62d83398831994dc3ca51856907479976af61ea2f84be0f7517` | 11754 / `5370b4d21c5cff60d77260594fef0555964530ae61710e91cbb74bbd45d18377` |
| [20328 Video models](https://arxiv.org/abs/2509.20328v1) | 17:17:27 | 02:05:54.000Z | 43530 / `1b48a51cd902f455e46c2bcaf528aeb832fb66f0f9d6187f71943a479586579d` | 11281 / `9ba03fa9bf05d46ff4747c661827152727fdd809daac6dcd950ee0983fad3d63` |
| [20336 Circuit Tracing](https://arxiv.org/abs/2509.20336v1) | 17:25:05 | 02:06:06.000Z | 41923 / `0407e2c8ceed1187644c7f7bc2e1721b1aa49b21a414ad493652d61ad2fdb2f7` | 9042 / `93bc015a0fb44f4d8df3eee2016139c3ba16ea27305f1b14aded1f84fa59b711` |

20208与20336只见v1；20214另Oct22v2，20317另Sep25T12:17:01Z v2，20328另Sep29v2，均不把后版贡献倒填v1。20214 comments NeurIPS2025、20336 Workshop on Efficient Reasoning NeurIPS2025仅为会议信息，不是独立早正文日期。精确ABS未见撤回、勘误或安全更正标记；这里不证明全部新版机制已审。20317精确v1 ABS无作者项目外链，已有metadata给的官方InternLM项目是本次具名恢复入口，不假装来自ABS正文。

**20208已有早机制披露。** 实际从[作者官方仓库](https://github.com/parkervg/blendsql)News进入具名[Language Models, SQL, and Types, Oh My!](https://parkervg.github.io/misc/2025/05/05/sql-llms.html)。Blog原件 `ROOT_DATE_20208_BLOG_20261025.raw`/request于10:27:11.628520～10:27:12.311112Z、200/exit0、35661B，SHA `bcb3c65b3438ee5121f18683e80bac8e7e27ad5bfbf5f39b4e153e4dbd0c40ad`；实际读日期原属性/开篇、Type Constraints完整段及查询优化与bench上下文，未核源码/图像素/运行。显示May5,2025，article:published_time和time datetime均2025-05-05T00:00:00+00:00，仓库News写5/6/25，虽差一天都明确早于本窗。它已披露由周围SQL AST推断生成约束及先做便宜SQL缩小LLM输入，不可把这一整个接口首次归Sep25。当前仓库后列Nov7“新论文”不否定已取得九月arXiv公告，也不把五月正文所有细节等同九月论文。新论文是否仍有不同机制/评价增量交writer具体判断；不自动排整篇，不先用宣传数字入选。

**20317具体早发布声明。** 官方[InternLM/SIM-CoT](https://github.com/InternLM/SIM-CoT)README的News明确 `[2025/9/24] Code and Paper are released`，paper指同ID的无版本PDF；代码链接当前为空，不由勾选完成或当前代码存在认证历史artifact。Contents API原件 `ROOT_DATE_20317_REPO_20261025.raw`/request于10:27:12.395360～10:27:12.931215Z、200/exit0、8736B，SHA `5e6f05eed184e3f6ffedf2f5bb5f6d721abf4777aa2055144d698825a9c4ac05`，decoded README blob `ff54059d0a81fe0a910f660f36da43249795a974`。root实际读作者/题名/资源、News完整两条/日期上下文和citation；未Methods或全commit。此是具名Sep24作者发布声明，不能因arXiv同ID Sep25公告便抹去，也不能给date-only私补时区/秒，把两事件说成互相证伪。需区分作者早披露与arXiv公告事件；在没有本窗实质新增证据前不授“Sep25全球首次”，但保已成arXiv限日层。唯一另一角色可按该具体线索核其归属与拟准入增量，不要求遍历全站/所有渠道。

**其他具名出口的有限停止。** Q-Palette官方README由Contents API取回 `ROOT_DATE_20214_REPO_20261025.raw`/request，10:27:12.998202～10:27:13.648244Z、200/exit0、10311B，SHA `e9c7f4136b0f873c394bbe4b2fa01e16ba094a91176314b8e698de1fd44bdbab`，blob `e6264e0d405868c26abd2f30d938d33a913ae51d`；实际读标题/News/引用与日期行，仅Sep2025录用，没有具体早日。20328作者[项目页](https://video-zero-shot.github.io/)原件 `ROOT_DATE_20328_PROJECT_20261025.raw`/request，10:30:22.130715～10:30:23.801134Z、200/exit0、59173B，SHA `5be9031710b536420404d233099aebf56296bf6d166d11722446fc796e9402d4`；实际读标题/九作者/GoogleDeepMind、所有heading、页尾citation和全time/date-meta属性，无日期属性或dated news，year2025不补日。未看视频/音频像素/真实模型，不从演示内容签能力。20336无具名早项目或正文日期出口，不为排假想渠道无限查。

五项日期首备完成，无root请求在途。交Aristotle作为唯一另一角色回上述有限原件actual采用/具名纠正，Einstein随后只角色复用，不第三date GET。题摘校准、原候选保护、首次评分/必要/Books仍各自独立，不预五项全准入或日完成。20208早机制与20317早声明各保具体反证，普通能做的贡献比较不得由此整批改称外部受阻。
