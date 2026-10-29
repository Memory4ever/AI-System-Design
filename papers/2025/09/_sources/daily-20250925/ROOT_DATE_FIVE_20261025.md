# Sep25：五篇具名线索的首次日期准备

2026-10-25，root按作者A4明确让出的五个日期域执行；本文件只交接日期，不接管题摘贡献、评分、必要方法审阅或Books owner。补充日为2025-09-24 BJT；旧候选日期不改。

## 原件与联合约束

十个请求实际完成于2026-10-25T03:45:14.196008+00:00至03:45:22.462585+00:00，均HTTP200、curl exit0。每份原件同名 `.request.json` 保留URL、起止UTC、HTTP状态、字节与SHA；root已重新计算字节/SHA并核对身份、v1提交记录及DataCite原字段。

以下S均为2025-09-23的UTC v1提交时刻，**不是公开时刻**。按研究合同已核验的2025公告规则与纽约EDT，这五个S的最早可能公告界L均为2025-09-24T00:00:00Z，即BJT09-24 08:00。同一精确DOI的登记方均为 `arxiv.content`、state为 `findable`；U采用 `registered` 原字段，不采用 `created`、Available月份或Updated字段代替。

| 精确v1身份 | S：Sep23 UTC | U：registered原字段 | U：Sep24 BJT | 联合判断 |
| --- | --- | --- | --- | --- |
| [2509.18847v1](https://arxiv.org/abs/2509.18847v1)，Failure Makes the Agent Stronger: Enhancing Accuracy through Structured Reflection for Reliable Tool Interactions | 09:35:49 | 2025-09-24T02:08:14.000Z | 10:08:14 | L≤U，整个可能区间在BJT09-24 |
| [2509.19199v1](https://arxiv.org/abs/2509.19199v1)，Online Process Reward Leanring for Agentic Reinforcement Learning | 16:15:42 | 2025-09-24T02:16:27.000Z | 10:16:27 | 同上；保留v1标题原拼写Leanring |
| [2509.19080v1](https://arxiv.org/abs/2509.19080v1)，World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation | 14:38:15 | 2025-09-24T02:13:41.000Z | 10:13:41 | 同上；已定点查看已见项目页日期线索 |
| [2509.19212v1](https://arxiv.org/abs/2509.19212v1)，Steering Multimodal Large Language Models Decoding for Context-Aware Safety | 16:32:25 | 2025-09-24T02:16:44.000Z | 10:16:44 | 同上 |
| [2509.18824v1](https://arxiv.org/abs/2509.18824v1)，Hyper-Bagel: A Unified Acceleration Framework for Multimodal Understanding and Generation | 09:12:46 | 2025-09-24T02:07:40.000Z | 10:07:40 | 同上 |

这里只将各精确arXiv v1公告日限定为2025-09-24；不将区间端点改名为实际发布时间，不证明全球首次公开或历史逐字正文。

## 可复查本地输入

各行ABS/DOI后均有同名前缀的 `.request.json`，DataCite URL为 `https://api.datacite.org/dois/10.48550/arxiv.<ID>`，精确URL也保存在请求记录。

| ID | 原始ABS / 原始DOI | 字节（ABS / DOI） | SHA256（ABS / DOI） |
| --- | --- | --- | --- |
| 2509.18847 | [ABS](ROOT_DATE_2509_18847_ABS_20261025.raw) / [DOI](ROOT_DATE_2509_18847_DOI_20261025.raw) | 43423 / 11965 | `e20c52d8ff1e0b0ce11323d0406bf2e84a7d906cd783f0f141220033fba024a2` / `5c7b8ef826da94ca262327e1fd35f63f01c655b9a365c95d87e27086fe87836e` |
| 2509.19199 | [ABS](ROOT_DATE_2509_19199_ABS_20261025.raw) / [DOI](ROOT_DATE_2509_19199_DOI_20261025.raw) | 44643 / 11975 | `334be1d7df4b25d1ab8dc93f1c326c5cfc156e7e459882769702c092fc817f91` / `d11ade12a42f121a3ed7bf3fb8fdbf5552a70718ca0991eb1827f2353013b44f` |
| 2509.19080 | [ABS](ROOT_DATE_2509_19080_ABS_20261025.raw) / [DOI](ROOT_DATE_2509_19080_DOI_20261025.raw) | 44737 / 12044 | `251eebe6e75dd81e670fc6c62eff5839a5caa97f1bd952a0ed0cc23b13caf3d9` / `cd0c3f36a069d811941b49666b54c42cb66019bf874b72f159185d805b8b11d9` |
| 2509.19212 | [ABS](ROOT_DATE_2509_19212_ABS_20261025.raw) / [DOI](ROOT_DATE_2509_19212_DOI_20261025.raw) | 42986 / 10331 | `64145290d7af85e4fabf686553b41f0827d3d05469b7788d6e7f2c181e016a70` / `64e4e08aaa7f81ee2eb09a783898e480ccb4be773c8d0930afe7102120405fbf` |
| 2509.18824 | [ABS](ROOT_DATE_2509_18824_ABS_20261025.raw) / [DOI](ROOT_DATE_2509_18824_DOI_20261025.raw) | 42660 / 10331 | `c46da3fd9c69712e77f2941aaef7c1fdeef3d260b19e5bdda395874a7366b2f9` / `6b0a78603c046338c7e0679e3f0970defc1ab90ed751f182f018ec1af8695451` |

## 已见版本和更早正文线索的有限检查

已实际读精确v1身份、可见metadata/comments/history及链接字段；五份DOI的relatedIdentifiers均为空。这不等于全版本内容或全网发布史已审。

- 18847可见v2提交2025-09-25T14:17:18Z、v3提交2026-04-15T06:57:52Z；9 pages评论未给更早正文日期。
- 19199可见v2提交2025-09-24T01:27:23Z、v3提交2025-09-28T06:47:55Z；preprint评论未给更早渠道日期。v2提交发生在本次v1登记前，不使其自动成为v1首次公开；也不证明v2为重要修订。
- 19080可见v2提交2026-03-19T21:24:09Z。精确v1给出[World4RL项目页](https://world4rl.github.io/)，root定点打开并读返回145行中的身份及日期栏目：标题一致，正文、演示、结果与页尾未见明确dated news/release/posted day。当前页包含匿名代码链接，但没有具体更早正文日期线索，未追取或执行代码。工具返回的是当前网页文本，不是历史快照或本地raw HTML；不把当前结果反投到v1，也不声称取得页面HTTP状态/隐藏metadata。
- 19212可见v2提交2026-08-28T16:48:24Z；框架描述评论不构成公开日期。
- 18824当前所见仅v1，Technical Report评论不提供更早日期。

所观察v1字段未给出撤回/勘误标记或其它具名更早正文日期；不声称已审当前最新版本全文。没有具体早稿线索时按合同有限停止，不为排除所有假想渠道展开代码/全史抓取。作者仍需在实际准入时处理当前官方事件已有的实质修订、撤回、安全或纠错信号。

## 交接边界

本包已真实保存后交Singer实际采用一次，再由Sartre检查角色、原件与组合边界；不重抓同一日期材料。五篇完整题摘贡献、首次评分及必要审阅仍归作者，不因本包变成候选/完成/Books整合。旧候选日期、评分、窗口和连续原证不修改。

## 第二批：20360具名日期负下界

作者A54提出20360/20357两个尚未开始的本日日期域；root只明确接受20360。20357已有09-26作者首持，后按同一event定点复用其真实结果，不另重复GET或建立平行账。首批五日期A10已实际采用有效，不第三。

[EditVerse精确v1 ABS](https://arxiv.org/abs/2509.20360v1)的首次日期原件为`ROOT_DATE_2509_20360_ABS_20261025.raw`，43580B/SHA256 `eaf44b05fc4bfc1b2d243039a10c754e9bec24ab743624f65a994549c2ef7b2e`；同名request真实HTTP200/exit0，UTC2026-10-25T06:54:23.132724～06:54:23.440558，无在途。root实际读完整title/14位authors、dateline、comments/主体元数据、全部history与leftcolumn实际链接；只作身份/日期，不新授贡献/分数或Methods。当前页显示v1、后v2/v3日期及最新version提示，未见withdraw/erratum字段；不称已读v3内容或证明不存在更早作者稿。

唯一v1提交S=`Wed, 24 Sep 2025 17:59:30 UTC`，按`America/New_York`当日为EDT13:59:30，位于周二14:00后/周三14:00前。此前集中核过的适用2025官方公告日程给最早L=`2025-09-25T00:00:00Z`，即BJT09-25 08:00。L已经晚于本日新增窗口09-24，因此该arXiv v1公告不可能是09-24；只作这个负下界，不为已能排出本窗的arXiv事件继续抓U/DOI，也不补造实际公告时刻、精确最终公告日或全球首次公开日。

history可见v2=`Thu,25Sep2025 22:11:13 UTC`、v3=`Sat,18Apr2026 01:38:10 UTC`；版号和提交不证明本窗重要修订。leftcolumn完整HTTPS链接只有arXiv作者搜索、自身版本/HTML/DOI，未给具名project/更早正文链接，未扩全网absence搜索。若本日旧材料另有具体更早作者稿信号，由writer按那个原入口有限恢复；这个负界不否定已读题摘的潜力，也不把原候选迁日。精确v1 AB与旧currentv3的内容差异、准入、必要及owner不由本包认证。

交Singer作为唯一另一角色实际回上述原域采用后，Sartre只复用真实采用角色/负界范围，不第三日门。没有新formal/score/Books或日报完成声明；旧窗口、日期/评分与连续证据不变。
