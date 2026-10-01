# 2026-09-27 每日机构来源核查 B

## 1. 范围与结论

- 主窗口：北京时间 `[2026-09-26 09:00, 2026-09-27 09:00)`，即 UTC `[2026-09-26T01:00:00Z, 2026-09-27T01:00:00Z)`。
- 缺日复用窗口：北京时间 `[2026-09-25 09:00, 2026-09-26 09:00)`，即 UTC `[2026-09-25T01:00:00Z, 2026-09-26T01:00:00Z)`。两窗分别判断，不用主窗口结果推导缺日结果。
- 访问日期：2026-09-27。收束时工具时钟为 `2026-09-27 01:37:14 UTC`（北京时间 09:37:14），已过主窗口截点；此前部分请求在截点前，最终目录补检在截点后。窗口不随运行延迟移动。
- 本 lane 只核六个机构的正式 Research / Blog 目录及有界官方发布补检；不负责 arXiv 批次，也不声称机构全部作者稿均已覆盖。
- 在下列实际可读目录与选定正式 release 中，两窗分别均未识别需准入的新 Source Family。没有将仓库 `pushed_at`、目录 `updated_at`、网页最后修改时间当成新公开研究事件。
- 这是来源核查材料，不是整日日级 Gate 或 Books 验收结论。本 lane 没有普通待审候选，也没有必要 Books 提案；全日报仍由日期 owner 汇总其他来源和独立复核。

## 2. 来源结果

| Source ID | 结果 | 实际入口与停止范围 | 主窗口结果 | 缺日复用结果 / 边界 |
| --- | --- | --- | --- | --- |
| SRC-TENCENT-HUNYUAN | 已检查 | Research 页面对应官方 publicList，pageNum=1、pageSize=100、renderType=0，totalNum=9 / list=9；另读近期官方组织仓库前两页及选定 releases | 列表最新显示日 09/22、publicAt 09/23；选定 release 无当窗事件 | 相同九条全列表及 release 均排除 09/25 09:00→09/26 09:00；仓库普通 push 不准入 |
| SRC-ZAI | 已检查 | 中文 Research「全部」首屏 15 条，最新 08/26，按日期向旧排列；官方 release notes；ZCode releases | 可见研究 / 版本目录无当窗事件 | 相同可见有序停点覆盖缺日；不把「查看更多」未展开等同所有历史论文已扫 |
| SRC-BYTEDANCE-SEED | 已检查 | 官方 Publications + public list API，US locale；论文 type=1 首批 18 条 / total242，博客 type=2 首批15条 / total95 | 最新论文 08/18、博客 08/05；所有首批实际 PublishDate 均早于窗 | 两类首批日期整体均早于缺日起点；未拿 UpdateTime 或置顶身份代替公开时间 |
| SRC-BAIDU-ERNIE | 已检查 | 文心中文 Blog 第1页，最新05/09、末条2025/11/21；ERNIE 官方 release | 无当窗目录条目或选定 release | 同一有序第1页和 release 早于缺日起点；不扫普通 Paddle commits |
| SRC-XIAOMI-MIMO | 已检查 | 首页 Paper8条 / Blog14可见卡片；逐项恢复相关卡片官方 header / iframe 目标；MiMo Code 官方 changelog 与 releases | 最新可核模型文章 V2.6=09/22，最新选定 release=09/22；无当窗事件 | 日期 header、月份范围与 release 均整体早于缺日起点；材料科学卡片因项目范围排除，不追加日期追溯 |
| SRC-MINIMAX | 已检查 | 英文 Blog12条、中文 Blog13条；Agent Docs llms.txt→techblog.md 目录1条；minimax-code / cli 等选定 releases | 普通 Blog 最新08/13，Agent TechBlog目录条目05/13；release 均早于窗口 | 同一目录与 release 有界停点覆盖缺日；未以初次返回只有导航认定零条目 |

## 3. 逐源证据与界限

### 3.1 腾讯混元

入口：[Research](https://hunyuan.tencent.com/research)。页面抓取曾超时，随后使用其官方只读目录接口：

```text
POST https://api.hunyuan.tencent.com/api/blog/publicList
{"pageNum":1,"pageSize":100,"renderType":0}
```

实际响应 code=0、`data.totalNum=9`、`list.length=9`，不是空响应。九条目录全部读到，停止条件是 total 与 list 一致，而不是首页刚好没有新日期。最新条目为 `id=100116`，题名 *When Do Larger Batches Help Scale LLM Reinforcement Learning?*：

- `displayPublishTime=1790006400`：UTC 09/21 16:00，即北京时间 09/22 00:00；
- `publicAt=1790150728`：UTC 09/23 08:05:28，即北京时间 09/23 16:05:28。

这两个字段语义不同，不能机械当同一 first-public 秒级事实；但两者都完整早于本次两个窗口。其余条目是 Hy4、ELR、Hyra、Hy3、Context、RLVR 等此前公开记录；没有为这些旧内容重开深审或 Books。

发布补检：[Tencent-Hunyuan 仓库目录](https://api.github.com/orgs/Tencent-Hunyuan/repos?sort=updated&direction=desc&per_page=30&page=1)读前两页，每页30条。第2页首条 updated 为09/24 09:04:40Z，已经早于两窗并集起点；未识别并集中新建仓库。当前组织中的 UniRL、AuK 有当窗普通 push，但以下正式 release 返回有效空列表：

- [UniRL releases](https://api.github.com/repos/Tencent-Hunyuan/UniRL/releases?per_page=10)
- [AuK releases](https://api.github.com/repos/Tencent-Hunyuan/AuK/releases?per_page=10)
- [Hunyuan T1 releases](https://api.github.com/repos/Tencent/llm.hunyuan.T1/releases?per_page=10)

普通代码 push 本身没有足够公开研究 / 重要版本事件身份，本 lane 不扩展成所有 commit 审查。

### 3.2 智谱 / Z.ai

实际读 [中文 Research](https://www.zhipuai.cn/zh/research)「全部」区的15条可见记录，首条 **2026/08/26 GLM-5.3-Flash**，后续为08/14、06/16、05/20、04/29等，直到2025/12/09；「查看更多」可见。最新记录已早于两窗，当前有序范围提供停止点，不必为了两天窗口展开全年旧项。

另读 [官方 release notes](https://docs.z.ai/release-notes/new-released)，最新08/26，之后08/18、06/16等，无两窗事件。官方组织近期仓库第一页30条没有并集中新建身份；[ZCode releases](https://api.github.com/repos/zai-org/ZCode/releases?per_page=10)实际1条，最新公开时间 `2026-09-24T10:54:12Z`，早于并集起点。其他仓库 star / update 不能作为新发布。

浏览器方式在本次环境不可用，具体原因是电脑锁屏导致 native surfaces 不可访问；本次 Research 页面本身经文本浏览实际可读，故该限制不等于 Research 目录未读取。

### 3.3 字节 Seed

实际读 [官方 Publications](https://seed.bytedance.com/en/public_papers)首批、新到旧，并用官方页面数据接口补核完整首批记录：

```text
GET https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=0
Header x-tt-locale: US
```

响应 `BaseResp.StatusCode=0`、`total=242`、`has_more=true`、`next_page_token=20`，实际 `sub_article_list=18`。已逐条看首批 `ArticleMeta.PublishDate`（Unix 毫秒）与英文题名，不把请求 count=20 误写成收到20条。最新 *Chain of Experience* 为 `2026-08-18T12:00:00Z`，末条 `2026-05-13T16:00:00Z`；首批实际公开日期全部早于并集起点。

同接口 `article_type=2` 读 Blog：StatusCode0、total95、首批15条、next20、has_moretrue。最新 Seed Realtime 为 `2026-08-04T16:00:00Z`（北京时间08/05），之后 Seedance2.5、SeedAudio、Seedream、EdgeBench、Seed2.1等，直到2025/12/23。置顶项与非置顶项均核 PublishDate；09月 UpdateTime 不作为新文章公开日。[Blog](https://seed.bytedance.com/en/blog)文本抓取曾只有空内容，不能单独证明零事件，已用上述有效官方目录替代。

官方 ByteDance-Seed 仓库第一页30条没有两窗并集中新建仓库；近期普通 push 早于并集起点。这个补检不宣称所有作者原始稿、所有版本发布已被全局枚举。

### 3.4 百度文心

实际读 [中文 Blog](https://ernie.baidu.com/blog/zh/)第1页：最新 **2026/05/09 文心5.1**，之后04/30、04/15、02/06等，末条2025/11/21，第2页导航可见。第1页有序停止点整体早于两个窗口，不翻旧页来制造当窗候选。

[ERNIE 官方 releases](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=10)实际只有1条 `ERNIE4.5Open-source` / tag `ernie4.5`，`published_at=2025-06-30T01:15:24Z`。未识别两窗重要版本事件；不把 Paddle 全组织普通工程变更扩入本轮。

### 3.5 小米 MiMo

实际读 [首页](https://mimo.xiaomi.com/)：Paper8条，最新 MOPD 为2026/06/29，之后03/13、02/03及2025记录；Blog14条可见卡片最初没有日期，不能据此直接判零。

本次从官方页面静态 route 与 iframe 恢复卡片文章，读取其日期 header，不把壳页 / sitemap 的200或404当研究目录结果：

| 可见身份 | 实际官方目标 / 时间 | 本轮处置 |
| --- | --- | --- |
| Introducing MiMo-V2.6 series | [官方文章](https://mimo.xiaomi.com/mimo-v2-6/article)，header **September 22nd, 2026** | 早于两窗；不把当前页面出现算成09/26或09/27新发表 |
| Scaling Coding Agent for Long Horizon Tasks | [官方 Blog](https://mimo.xiaomi.com/blog/mimo-code-long-horizon)，`dateTime=2026-06-10` | 旧机制材料，不在两窗 |
| V2.5-Pro UltraSpeed / 1000TPS | [官方 Blog](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps)，`dateTime=2026-06-08` | 旧文，不采用宣传 TPS |
| Full-Pipeline Inference Optimization | [官方 Blog](https://mimo.xiaomi.com/blog/mimo-v2-5-inference)，显示May30,2026；属性仅2026-05 | 日/月精度均早于两窗，不补造时区或时刻 |
| V2.5-Pro | [iframe 正文](https://mimo.xiaomi.com/mimo-v2-5-pro)，April27th,2026 | 旧版本事实 |
| V2.5 | [iframe 正文](https://mimo.xiaomi.com/mimo-v2-5/index.html)，`datetime=2026-04-22` | 旧版本事实 |
| V2.5-ASR / V2.5-TTS | [ASR](https://mimo.xiaomi.com/mimo-v2-5-asr/index.html)、[TTS](https://mimo.xiaomi.com/mimo-v2-5-tts/index.html)，两页均 **April2026** | 月份区间整体早于两窗，不伪造日级精度 |
| V2-Pro / V2-Omni / V2-TTS | 各 `/mimo-v2-pro/index.html`、`/mimo-v2-omni/index.html`、`/mimo-v2-tts/index.html`，均`datetime=2026-03-18` | 旧版本事实 |
| V2-Flash / HSS / Safety | [Flash](https://mimo.xiaomi.com/mimo-v2-flash/index.html)显示December16,2025；[HSS](https://mimo.xiaomi.com/blog/mimo-v2-flash-hss)、[Safety](https://mimo.xiaomi.com/blog/mimo-v2-flash-safety)显示December22,2025 | 旧文；Safety是定点路径补检，不冒充首页14条之一 |
| 材料研究案例 | 首页材料研究卡片 / `/blog/mimo-v2-6-material-research` | 项目当前暂不覆盖 AI for Science；按实际任务贡献范围前分母关闭，不为日期追溯扩大本轮 |

[MiMo Code changelog](https://mimo.xiaomi.com/mimocode/changelog)明确转交 GitHub Releases；[MiMo-Code releases](https://api.github.com/repos/XiaomiMiMo/MiMo-Code/releases?per_page=10)实际2条，最新 `2026-09-22T14:58:45Z`，早于两窗。mimoagent releases为有效空列表。MiMo-Code及verl fork两窗内普通push不能代替公开版本事实，不评分也不自动采用。

### 3.6 MiniMax

实际读 [英文 Blog](https://www.minimax.io/blog)12条和[中文 Blog](https://www.minimax.cn/blog)13条（minimaxi.com/blog重定向到后者）：最新均 **2026/08/13 Music3.0**，之后07/31、06/09、06/01等旧项。两语言旧条目的日期差异不涉及本轮窗口，不重开旧身份历史。

Agent TechBlog 页面初次文本只有导航，不能称零条目。改读 [官方文档索引](https://agent.minimax.io/docs/llms.txt)→[技术博客 Markdown](https://agent.minimaxi.com/docs/techblog.md)，实际目录1条：*MiniMax Agent Team：为长程任务，持续进化而生*，目录日期 **2026-05-13**；[正文](https://agent.minimaxi.com/docs/techblog/agent-team.md)身份吻合。目录可用且日期早于两窗，不追整篇旧论文或新增 Books。

官方发布补检：minimax-code releases实际5条、最新 `2026-09-24T06:50:13Z`；cli首批10条、最新 `2026-09-19T15:01:22Z`，已早于并集起点；ProviderVerifier、MiniApps返回有效空 release 列表。组织近期仓库第一页30条无并集中新建仓库。minimax-code / ProviderVerifier / MiniApps普通push存在，但未形成正式重要公开版本事件，不作为当窗候选。

## 4. 09/26 缺日恢复的独立复用判断

以下是用同一实际读取范围，对缺日 `[09/25 09:00,09/26 09:00)` 单独判断，不是因为09/27无候选便推断缺日无候选：

1. 浑元九条全目录的最新显示时间 / publicAt均在09/25 09:00以前；AuK在缺日有普通push，正式release列表有效为空，未识别可准入的发布身份。
2. 智谱 Research、官方release notes及ZCode release的最新日期都在缺日起点以前。
3. Seed论文与博客首批所有实际PublishDate早于缺日起点，更新字段不改其公开归属。
4. 百度Blog第1页及ERNIE release整体早于缺日起点。
5. MiMo恢复后的模型 / Blog日期及MiMo-Code正式release早于缺日起点；未把无日期卡片直接归为缺日。材料科学案例由贡献范围关闭，与日期无关。
6. MiniMax英中Blog、恢复后的Agent TechBlog及所选正式release整体早于缺日起点；ProviderVerifier / MiniApps普通push不是正式研究公开事实。

因此本六源在缺日可复用范围内同样没有识别新可准入Family。缺日其他机构、arXiv与工程来源仍由对应lane恢复，不能由本文件替代。

## 5. 精确限制与补检终态

- Native browser无法使用：电脑锁屏，cua返回无可用browser / app surface。没有绕过锁屏。六源实际文本或官方API均恢复可读；这一环境限制不被写成这些来源全无更新。
- 官网目录只证明其公开列出的条目；未列作者稿可能由当窗arXiv来源补获，本lane不证明机构全部论文零遗漏。
- 机构GitHub补检仅新repo身份与selected important release，不枚举每次commit；`pushed_at/updated_at`不作为候选日期。没有以Github活动量要求无限扩池。
- 小米卡片壳页和MiniMax Agent导航页初次无有效日期 / 条目的问题均已用其官方正文或目录恢复；未保留为普通pending，也未凭空响应认定无命中。
- 日级日期precision不足且跨窗口的材料才应隔离；本次恢复到的MiMo日/月字段均整体早于两窗，故没有仅凭低精度制造当窗候选。
- 有界补检还使用六域当日日期检索；检索未命中仅作弱backstop，不参与上述无当窗目录事件的事实依据。未来发现目录之外的正式当窗公告，应按对应Source Family定点重开，不推倒已读目录。
- 本文件没有评分对象、没有正文Books写入，也不宣称整日日报Complete。六源覆盖范围交日期owner用于总报告与独立语义Gate。
