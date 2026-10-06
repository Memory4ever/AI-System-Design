# Daily Research — 2026-01-05

**规范：** V3
**窗口：** 2026-01-04T09:00:00+08:00 ～ 2026-01-05T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T11:06:26+08:00

## 1. 结论

14个每日来源已作本日有限检查。确认窗内KimiCLI两个release事件、同一材料家族，完整核心说明初筛经独立校准贡献前关闭；0正式候选、0候选证据审阅完成、0 Books整合/已有覆盖，No Change。目录、日期字段和变更说明初筛不计候选证据审阅。root非作者日级验收通过，无普通可执行工作。

arXiv元旦延迟批次的官方计划公告时刻恰好在本窗不含的右端点，不按Submitted日期吸收下一批。机构历史及公开revision/mirror限制已单列；以上0候选不代表互联网无相关论文，也不表示Coverage/Evidence没有缺口。

## 2. 来源覆盖

仅Daily组；不扫描Weekly源，不继承旧日报候选、评分或摘要。只跨日定点接Kimi两release身份/日期线索，本日重新取得核心原文和日期决定。[实际查询与停止](../_sources/daily-20260105/queries-and-screening.md)、[机构原日期字段](../_sources/daily-20260105/official-date-slices.jsonl)、[arXiv与Kimi原记录](../_sources/daily-20260105/arxiv-and-kimi.jsonl)、[日期搜索原查询](../_sources/daily-20260105/date-search.txt)、[补充官方入口](../_sources/daily-20260105/supplemental-official.txt)保留；原入口五批记录在同目录official-entry-0～4.txt。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research当前首屏→官方RSS1243 title/link/pubDate，仅本窗/邻接Grove Jan2T10Z、Health Jan7T00Z，窗内0，止metadata切片 | 已检查 | 有限官网/RSS不证明所有镜像或隐去发布 |
| SRC-ANTHROPIC | Research首屏→原HTML174 publishedOn，窗内0，邻接Bloom Dec19T19:45Z/Constitutional Classifiers Jan8T00Z，止metadata不读全年正文 | 已检查 | 仅官方Research当前目录，不授全机构覆盖 |
| SRC-GOOGLE-AI | DeepMind当前news止May2026；Publications page1 30行/265 total/9页，Jan9→Dec3跨窗止page1；GoogleResearch当前年过滤首屏与官方域Jan4/5主题日期query首组 | 受阻 | DeepMind有限dated目录未见本窗行；GoogleResearch日级首公开/历史revision未恢复 |
| SRC-META-AI | Research原入口0行，官方域Jan4/5主题日期query首组空，止此 | 受阻 | 空提取/搜索不是历史目录或零发布证明 |
| SRC-QWEN | 旧Blog当前Sep23 2025→July，实际新qwen.ai/blog0行；官方域日期query首组空，止有限入口 | 受阻 | 本窗历史dated目录缺失，不按版本名定公开 |
| SRC-DEEPSEEK | /news/研究10项Jan12→Dec31桥接，动态5/查看全部，无本窗行，止有限官方日期目录 | 已检查 | date-label不是first-public时刻，非全部机构/隐藏历史 |
| SRC-MOONSHOT | Platform26 dated Nov7 2025→May2024；fresh两ReleaseAPI与exact-tag0.72 CHANGELOG完整0.71/0.72核心，确认两个本窗release拟负侧；止两事件不扫PR | 受阻 | release已核，不替代完整模型研究/重要revision历史目录 |
| SRC-TENCENT-HUNYUAN | 首查Research超时→fresh官方POST publicList page1/pageSize1000/renderType0，成功code0,total9/list9，原public/published/display/updated分列，最早display Feb3T03:54:58Z，止metadata | 受阻 | 当前九条不是Jan05历史；未证明删除/隐藏材料不存在 |
| SRC-ZAI | Research本次15 dated行止Dec9 2025/查看更多；release说明Jan14→Dec22桥接无本窗行，止当前目录+日期query首组 | 受阻 | 有限release不能替代必要研究历史目录 |
| SRC-BYTEDANCE-SEED | Research/public_papers→API type1/2，各2026ASC/2025DESC page_token0/count20，19/14/18/18 metadata行，最早Jan20/Feb12、最晚Dec15/Dec24，窗内0，按日期而非pinned止 | 已检查 | token/has_more保留；当前API locale/status不保证历史完整，不读全年摘要 |
| SRC-BAIDU-ERNIE | Blogpage1 Jan8→Dec23桥接，无本窗行，下一页2/2更旧，止page1及日期query首组 | 已检查 | 仅官方Blog有限目录，不授所有机构发布 |
| SRC-XIAOMI-MIMO | 当前8 Paper日期Jan8→Oct21跨窗及15 Blog/More，止入口与官方域日期query首组 | 受阻 | Blog历史日期/More范围不可核，不拿当前标题当本窗事件 |
| SRC-MINIMAX | English12 dated Jan27→Dec23跨窗；CN跳minimax.cn/blog仅68行壳，AgentTechBlog15行导航；止三入口及日期query首组 | 受阻 | CN/Agent必要历史dated目录缺失 |
| SRC-ARXIV | freshavailability与holiday；本窗四主题lastUpdatedDate+起点前submittedDate/start0/max20各0；Jan05 catchup cachemiss/实际HTTP400、cs.CL月首25cachemiss，止此不扩分类/月 | 受阻 | 计划常规公告本窗无；API0非公开revision/mirror全量证明，历史标题补检目录未恢复 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无正式候选，不评分。两Kimi版本只保留完整核心说明初筛及具体排除理由，不把同家族两个release算两篇候选；贡献前关闭已通过独立校准。

## 4. 证据与知识整合

无候选证据审阅或Books写入。以下为已确认发布的初筛与日期边界，不冒称深入完成：

- [KimiCLI0.71官方release](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.71) published_at=2026-01-04T05:08:41Z（BJT13:08:41）；[0.72](https://github.com/MoonshotAI/kimi-cli/releases/tag/0.72)=2026-01-04T06:01:07Z（14:01:07），均本窗。created_at分别04:59:46Z/05:55:57Z另存，不作为公开日期。[精确tag变更说明](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/0.72/CHANGELOG.md)完整核心：0.71将file/shell通过ACP client同步并增加model/skill/info/terminal功能，未提出新的失效/控制契约或验证边界，拟不改变长期机制判断；0.72只修Python3.14安装兼容。不是因为框架名或fix标签排除；未发现这些核心说明中的安全、撤回或本书设计反证信号，不扩普通PR。
- [arXiv Availability](https://info.arxiv.org/help/availability.html) L172常规Fri/Sat不公告，L175/176首次公告才分ID且不backdate；[官方假期全文](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/) L17/21/32计划Jan4ET20公告=Jan5BJT09，恰好本窗不含右端。只支持计划边界，不伪装具体材料的实际first-public证明，不排除作者镜像或非标准变化。
- ROADMAP主线仍是模型/训练/推理/多模态/Agent机制，AI for Science暂缓；无纯主题映射占位。No Change只针对本次已确认与可判断材料，不证明所有历史研究无贡献。

## 5. 缺口与下一步

尚可执行：0；来源检查、筛选、报告及root非作者日级验收已完成。以下是本窗终态保留项，不是普通可执行工作，也不等于原始来源无缺口。

本窗终态保留项为8组机构历史限制（GoogleResearch日级公开、Meta、Qwen、Moonshot完整研究/重要revision、Hunyuan历史、Z.ai完整研究、MiMo Blog日期、MiniMax CN/Agent）及arXiv非标准公开revision/author mirror/历史标题补检。具体入口、停点、缺少什么见§2；所需替代是同窗官方dated历史目录、真实公告批次、指定版本原始公告或可核作者first-public。当前有限官方入口/API与首组辅助查询已执行，仍不足历史完整性，恢复只重开对应源/事件，不扩整月。

隔离项不用于正面证据、Books、无遗漏或性能/安全保证，不算Coverage/Evidence无缺口。官方延迟批次仅为右端以后恢复的排期线索，未把该批Submitted标题池搬进本日，也未称已审重复。

## 6. 复核

复核者：root（非报告作者jan01_v3）

结论：通过

root实际完整读取README、queries-and-screening、本日两fresh ReleaseAPI body及exact-tag完整0.71/0.72核心、四窄主题查询0、全部source-date字段（Hunyuan九项多日期、Seed四slice/pagination）与入口关键日期桥接，另重开availability L170–186与holiday全文L17/21/29/32。两个release完整核心负侧准入通过，不是机械fix排除；未见这些核心中的设计反证/安全深审触发。确认0正式候选/0 Books/No Change、无普通待办，8组机构及arXiv public revision/mirror/title-backstop外部限制安全隔离。不把这一有限实际范围称全机构、全部公开修订或互联网无遗漏验证。

机器校验：最终V3 validator通过，本日本地引用、限定git diff --check及README/_sources全部新增文件noindex空白检查通过；机器结果不能替代实际独立复核。未stage、commit或push。
