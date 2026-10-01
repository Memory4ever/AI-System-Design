# 2026-04-26 V3 独立来源发现与续跑停点

作者：apr20_resume。固定窗口 `[2026-04-25T09:00:00+08:00, 2026-04-26T09:00:00+08:00)`，即 UTC `[04-25T01:00Z, 04-26T01:00Z)`。当前是**准备与审阅进行中**，不等于 04/20 已经通过日级 Gate，也不构成 04/26 候选冻结或报告完成。本次实际重新读取仓库 `AGENTS.md`、当前研究/来源/报告合同、统一 Prompt、ROADMAP、4 月 checkpoint 以及旧 04/26 报告；只处理本日期独占来源文件，不写共享 Books。

## 旧结论不能继承

`papers/2026/04/26/README.md` 仍为 V2.1 旧稿，表内 `Complete/Passed` 仅历史说法，首部已经标记 V3 复核中。其 DataCite `created` 为空和 `arxiv-api-enumeration.json` 中按 `submittedDate` 枚举的 419 个身份都不能证明本窗首公开为零或 419。保留旧证据与脏工作树，不删除、不覆盖旧正文，正式六部分 V3 须另按当前合同生成。

[arXiv 官方 availability](https://info.arxiv.org/help/availability.html) 的正常公告日为美东周日至周四；北京时间周六 09:00—周日 09:00 对应的常规公告槽不存在。此事实只排除**常规**新稿公告批次，不推断异常公告或其它官方来源零命中。邻日 04/25 与 04/27 的已核停点可用来限定本日补查范围，不能直接替代本日 14 来源行。

## Seed：当前目录标注本窗的题摘线索，历史首公开未判定

当次查询官方 `GET https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=20`，header `x-tt-locale: US`，读到 `ArticleMeta.ID=1605` / `ArticleID=1782376464879` 的 [MegaScale-Omni 官方页](https://seed.bytedance.com/en/public_papers/megascale-omni-a-hyper-scale-workload-resilient-system-for-multimodal-llm-training-in-production)。原始 `PublishDate=1777132800000` 毫秒，即 `2026-04-25T16:00:00Z`、北京时间 `2026-04-26T00:00:00+08:00`，**当前官方目录标注的时间落在本窗**；官方页显示 2026-04-26。这是须处理的本窗目录线索，但单靠现存 CMS 字段尚未证明卡片在当时实际对公众可见，更不自动支持论文全文当时可读。

完整官方题摘的具体设计信号：动态模态配比和长度分布下，encoder 用 long/short sequence parallelism、LLM backbone 用 5D parallelism，统一 encoder–LLM representation/联合 pipeline，并以去中心化 grouped reordering 与 encoder→LLM rank adaptive resharding 处理负载。作者声称在自有大规模动态工作负载上，相对四个系统的吞吐提升为 `1.27×–7.57×`；这仍是**作者题摘主张**，不是已核实验合同或通用生产保证。它显然值得题摘贡献审查，不能因非 arXiv 常规批次而漏掉。

当前 Seed API 的 `ExternalLinks` 仅指向 [arXiv 2605.08962](https://arxiv.org/abs/2605.08962)。其官方 v1 历史为 `2026-05-09T13:59:27Z` 提交；当前 API `UpdateTime=1782897736000` 即 `2026-07-01T09:22:16Z`，表明现存卡片确曾后续更新，**不能**将后来可见外链当作 04/26 已有正文。官方 [EuroSys 2026 accepted-papers](https://2026.eurosys.org/papers.html) 列出同题，仅证会议身份；[Crossref DOI 元数据](https://api.crossref.org/works/10.1145%2F3767295.3803587) `10.1145/3767295.3803587` 的 `created=2026-04-24T20:20:04Z` 是记录建立，不是首公开。其 `published` 只有 2026-04-26 的日级精度，换算出的可能区间横跨本窗口 04/26 09:00 截止，不能凭日期或许可证起日造出精确时刻。本轮 ACM PDF 直连返回 HTTP 403；当前官方 Seed 页只呈现题摘与后来 arXiv 外链，未取得可证明 04/26 09:00 前已有论文正文的原始时间链。

额外核了该 API 同一分页的邻项原字段：MegaScale-Omni `ArticleID=1782376464879`，而 Context Unrolling、AgentWorld 等条目的 `ArticleID` 也和 2026-06/07 的 `UpdateTime` 聚集，`PublishDate` 却回指四月。`ArticleID` 数值长得像毫秒 epoch（本项若如此解释为 06/25T08:34:24.879Z），但官方未说明它的语义，**不能把此解码当创建时间或先前不存在的证明**。它只加强“当前目录经后续整理，历史可见时刻须独立证实”的风险提示。

**暂定处置：**Seed 官方当前目录给出本窗题摘时间，已发现不能记作“零线索”，但历史实际公开与论文正文 first-public owner 均未独立证实。04/26 当时可用的确切版本及必要方法/实验也待有界核实；在此之前不冻结论文候选、不评分、不写 Books，不把以后全文倒灌。恢复所需材料为 ACM/作者/会议可核的全文首公开时刻，或证明卡片/原始全文在本窗内已可公开访问的时间记录；若最后只能证当前 CMS 标注，则将目录时间线索与论文首次正文事件分账，隔离未证明的机制/评价。本轮针对该卡片的 Internet Archive CDX 窄查询连接超时，无历史快照结果，不能把超时说成无快照。

为查作者可见全文线索，再定点读第一作者 [GitHub 主页](https://github.com/DicardoX) 与该主页源仓库的[提交历史 API](https://api.github.com/repos/DicardoX/DicardoX/commits?path=README.md)：当前页面列同题 EuroSys 接收与 ACM Paper 链接，但承载 Publications/News 的 README 改写发生在 2026-05-24T04:40:55Z 之后；本窗前最后可见 README 提交 `76e4f714ee`（03/16T02:50:51Z）[原始内容](https://api.github.com/repos/DicardoX/DicardoX/contents/README.md?ref=76e4f714ee)只有简短个人介绍、没有该论文/链接。故不能把**现时**作者主页的“2026.01 已接收”与 ACM 链接倒证 04/26 前全文公开；这个阴性仅针对该 GitHub README 历史，不证明别处未发。官网 CMS、作者主页、会议目录三线目前仍没有当窗公众可读全文的时间锚，保留具名隔离，不再扩查全作者仓库。

## 本次确实重新检查的其它日源切片

**Google DeepMind Publications 补得一条具名日级歧义：**[官方目录](https://deepmind.google/research/publications/) 的 2026 年可见邻域在 04/23 *Dynamic Reflections* 与 05/06 下一项之间列出 04/25 的 [*ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation*](https://deepmind.google/research/publications/238239/)，官方题摘描述预训练 GP surrogate、Bayesian quadrature 性能估计与 superlevel-set failure sampling，属于 Evaluation 主线的具体设计线索。[所链 arXiv 2604.23099](https://arxiv.org/abs/2604.23099) v1 历史显示 `Sat, 25 Apr 2026 01:33:57 UTC` **提交**，恰在本窗内；但按官方常规公告时隙不能把提交视为公众可读。DeepMind 页只有 04/25 **日级**日期，无时区和精确公开时刻，也未取得本窗内的原始页面快照/全文访问记录。故本轮只登记为 04/26 的独立正线索与 first-public 具名隔离；不得凭当前官网日级日期或 arXiv 提交时间冻结候选、评为 Deep 或倒灌后续 v2。若得 DeepMind/作者本窗精确公开链，再读 exact-v1 的必要方法/评价/反证及 Ch66 owner，不扫其它 Google Publications 全库。

| 来源 | 当前实际入口和邻域停点 | 未证明部分 |
| --- | --- | --- |
| SRC-OPENAI | [官方 News RSS](https://openai.com/news/rss.xml) 原始 `pubDate`：04/25T00Z 的 *Modeling an AI jobs transition* 在本窗 UTC 起点 04/25T01Z 之前；下一项 *Our principles* 04/26T16Z 在本窗之后。RSS 可见邻域无本窗 News 条目。 | News RSS 不是 [Research](https://openai.com/research/) 历史目录；不能宣称 OpenAI 研究入口零发布。 |
| SRC-ANTHROPIC | 当次读取 [Research](https://www.anthropic.com/research) HTML 的 `publishedOn` 邻域：04/22T14:12:30.673Z、04/22T14:27:03.434Z → 04/29T20:26:00Z，当前可见目录跳过本窗。 | 只覆盖官网 Research 可见目录，不证明作者所有投稿/发布。 |
| SRC-QWEN | 当次查询 [官方动态研究列表 API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)，相关 `extra.date` 04/22T10:00+08 Qwen3.6-27B → 04/28T10:00+08 FlashQLA，当前可见目录跳过本窗。 | 官方 GitHub 发布和未列论文未由此入口覆盖。 |
| SRC-TENCENT-HUNYUAN | 当次按前端同源查询 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，参数 `{"pageNum":1,"pageSize":100,"renderType":0}`，实际 `totalNum=9` 且读完九条；`displayPublishTime` 相邻 1776873600（04/23 Hy3 preview）→1777532400（04/30 Real life），本窗无列表条目。 | 仅官方 Research 公共列表，不能覆盖组织所有代码发布/作者论文。 |
| SRC-BYTEDANCE-SEED | 当次 papers type1/page_token20 命中上文 ID1605；另查同一 [官方 API](https://seed.bytedance.com/api/get_article_list_v2?article_type=2&count=20&order_desc=true&page_token=0) 的 Blog type2/page_token0，`total=95`、本页15条，最近的 04/22T16Z Seed3D 2.0 随后到 04/08T16Z，Blog 页内没有本窗条目。 | Publications 的题摘事件不等于论文全文首公开；Blog 分页/外链、官方仓库亦须分账。 |
| SRC-GOOGLE-AI | 当次打开 [Google Research 2026 年 4 月 Blog 档案](https://research.google/blog/2026/04/)，完整当前可见月页从 04/22 下一条直至 04/29，博客目录无本窗条目。续读 [DeepMind Publications](https://deepmind.google/research/publications/) 当前可见 2026 邻域，04/25 有上文 ProEval（目录日级日期未证本窗首公开）。[Google Research Publications](https://research.google/pubs/) 可读，但当前首页为庞大年度索引，不能以首页无 04/25 字符串作阴性。 | DeepMind Blog 历史分页及 Google Research Publications 的窗口精确停点未完成；ProEval first-public 隔离，不以 Google Research Blog 无项推出 Google 两方全零。 |
| SRC-META-AI | 当次打开 [Meta AI Blog](https://ai.meta.com/blog/) 首个可见页：04/08 Muse Spark/构建测试条目与后续 06/29 Brain2Qwerty 等卡片，没有看到 04/26；官方 Research/Publications 直开本轮未得到可用历史页。 | Blog 首屏并非 Publication 全档且列表非严格单调；此行只保留已查切片，Publications 作为具名覆盖缺口，不宣称零论文。 |
| SRC-DEEPSEEK | 当次打开 [Research & News](https://deepseek.com/en/news/)；News 可见 04/24 V4 Preview→09/10 V4.1，Research Index 可见 02/25 DualPath→06/24 V4 技术报告，两个当前目录均无本窗独立条目。 | V4 Preview 的日级日期与本窗起点不同，后来的六月报告不回填四月；其它技术资产/仓库仍未由该列表证明零更新。 |
| SRC-ZAI | 当次打开 [官方 Research](https://www.zhipuai.cn/zh/research)，可见列表在 04/07 GLM-5.1 后直接到 04/29 Scaling Pain；续查[官方 New Released](https://docs.z.ai/release-notes/new-released)，可见 04/07 GLM-5.1→06/16 GLM-5.2。两个当前可见目录的日期邻域均跳过本窗。 | 仍只覆盖这两种官方列表；重要既有仓库更新与作者论文不因此判零。 |
| SRC-BAIDU-ERNIE | 当次打开 [ERNIE 中文技术博客](https://ernie.baidu.com/blog/zh/)，可见 04/15 ERNIE-Image→04/30 ERNIE-5.1 Preview；续查 [PaddlePaddle/ERNIE 官方 Releases API](https://api.github.com/repos/PaddlePaddle/ERNIE/releases?per_page=100)，当前仅 1 条 `ernie-4.5`、`published_at=2025-06-30T01:15:24Z`。这两个可见入口均无本窗事件。 | Blog 与已发布 GitHub release 不替代论文目录、仓库无 tag 提交或删改历史。 |
| SRC-XIAOMI-MIMO | 当次打开 [MiMo 首页 Paper 列表](https://mimo.xiaomi.com/)，按可见日期从 03/13 ARL-Tangram 直接到 06/29 MOPD，本窗无 Paper 卡片。 | 同页 Blog 卡片无日期；不能据 Paper 空档否定 Blog、GitHub 或作者其它正文。 |
| SRC-MINIMAX | 当次查询 [官方 CLI Releases API](https://api.github.com/repos/MiniMax-AI/cli/releases?per_page=100)，最近 v1.0.12 原始 `published_at=2026-04-26T01:40:29Z`，在本窗截止后 40 分 29 秒，属 04/27。续读[英文 Research/Blog 当前完整可见列表](https://www.minimax.io/blog)，03/18 M2.7 后下一条为 05/26 sparse-token forgetting，列表本窗无项；[中文 Blog](https://www.minimaxi.com/blog) 本次仅提取导航，不能作阴性。[Agent Tech Blog](https://agent.minimax.io/docs/techblog) 的当前 HTML 只出现 `/docs/techblog/agent-team` 与 `2026-05-13`，其 `llms.txt` 也只列这一篇。 | 这些当前可见列表和单一仓库 release 不证明隐藏/删改历史、其它仓库或作者论文均无本窗事件；Agent Tech Blog 的单条当前目录仅是有界停点。 |
| SRC-MOONSHOT | 本轮对 [kimi-cli 1.39.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.39.0) 与 [1.40.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.40.0) 分别定点重开，`published_at` 为 04/24T06:22:19Z 与 04/28T13:51:04Z；04/25 日内曾实际核完整 100 release 的相邻停点。该仓库 release 层没有本窗事件。续读[平台 Blog 当前列表](https://platform.kimi.com/blog)，可见文章止于 2025-11，**并无 2026 历史档**可据其判阴性。 | 本轮全量 release API 请求超时截断，**没有**以截断响应自行作阴性推断；此行复用邻日有效完整停点加两个原始 tag 日期，不能覆盖 Platform Blog 2026 缺档或其它仓库。 |
| SRC-ARXIV | 当次核 [官方 Availability / Announcement Schedule](https://info.arxiv.org/help/availability.html)：周日—周四美东晚常规公开，周五/周六无公告。本窗从北京时间周六 09:00 至周日 09:00，没有落入正常公告槽；旧 419 `submittedDate` 线索不得作为本窗 419 篇公开。 | 仍需按官方实际历史批次/异常公告线索确认；日历规则不是所有特殊公告“不存在”的证明，亦不代替机构先发项目页。 |

Moonshot `kimi-cli` Releases API 本轮分页请求超时截断，直接按 tag 定点读取两个端点并复用 04/25 有效全量邻域记录，不能将失败请求本身当作阴性证据。

另对 GitHub 官方当前 Search API 的八个相关组织 `QwenLM`、`Tencent-Hunyuan`、`zai-org`、`ByteDance-Seed`、`PaddlePaddle`、`XiaomiMiMo`、`MiniMax-AI`、`MoonshotAI`，分别查询 `org:<name> created:2026-04-25..2026-04-26`，八次实际 `total_count=0`。这个查询日历日略宽于本窗，**只证明当前 API 可见的新仓库创建层未命中**；不能反证当时删除/转私有仓库，也不覆盖既有仓库的 tag、release、无 tag 提交或站外研究材料。不能用八个零替代上表具名缺口。

为避免把新仓库零命中误作既有仓库零更新，又对少量主线相关 repo 的官方 Releases API 作**有界**定点查：`ByteDance-Seed/VeOmni` 当前17条的 04/15T10:40:08Z v0.1.9a1 → 04/27T08:21:57Z v0.1.9a2 跨本窗；`ByteDance-Seed/Triton-distributed` 当前3条、`QwenLM/FlashQLA` 当前2条、`Tencent/llm.hunyuan.T1` 当前0条、`zai-org/GLM-5` 当前0条、`XiaomiMiMo/MiMo-V2.5-ASR` 当前0条，所见 release 层均无本窗事件。选择这些 repo 只因现有来源主线与相邻日触发，不暗示八组织其它既有仓库都已穷尽；无 tag commit、历史删改仍是限定。

## 下一执行位置

继续逐个核 14 个每日来源的跨窗口真实停点，优先寻找本窗正命中与具名日期歧义，不扫 Weekly 或旧 419 SubmittedDate 库。Seed 与 ProEval 两项先查上述狭窄 first-public 链，获得 owner 后才读相应当时 exact-v1 必要正文；已有 04/27 MiniMax CLI v1.0.12 `2026-04-26T01:40:29Z` 即北京时间 09:40:29，在**下一日**窗口，04/27 V3 已作局部修复前关闭，不重复本日。04/20 整日独立 Gate 尚待 root，不能提前签 04/26 完成。

## 2026-09-28 续跑：两个首公开隔离项与 release 边界

已重新读取当前合同、ROADMAP 和本日旧稿，不继承 V2.1 的零候选或完成判定。固定本窗 UTC `[2026-04-25T01:00:00Z,2026-04-26T01:00:00Z)`。以下只补决定日期归属的最窄原始链，未取得当时页面快照或当时可读全文，故两条保持**日期隔离**，并非贡献前关闭或得分候选。

- [Seed 官方目录](https://seed.bytedance.com/en/research?view_from=homepage_tab)仍列 *MegaScale-Omni* 为 04/26；同源 `get_article_list_v2`、papers `page_token=20` 返回 `ArticleMeta.ID=1605`、`PublishDate=1777132800000`（本窗内 04/26 00:00 北京）、`UpdateTime=1782897736000`（07/01 更新），当前外链为 [arXiv 2605.08962](https://arxiv.org/abs/2605.08962)。再核 [Crossref 原始 DOI 记录](https://api.crossref.org/works/10.1145%2F3767295.3803587)：`created.date-time=2026-04-24T20:20:04Z`、`published-online.date-parts=[2026,4,26]`、`published-print=[2026,4,27]`。前者仅是 DOI 建立，后者只有自然日精度，覆盖本窗截点两侧；不能拼接成 04/26 09:00 北京前公众可读全文。当前 Seed 目录时间也未证明卡片在该时刻已实际可访问。停止条件是这三条同源/出版方记录都不能给出当窗可读的原始正文时刻；需要原站历史快照、ACM/会议实际上线时间或等效作者原始正文记录才定点重开。
- [Google DeepMind ProEval 页面](https://deepmind.google/research/publications/238239/)显示 04/25，当前 HTML `ScholarlyArticle.datePublished=2026-04-25T00:00:00+00:00`，但与页面日级日期相同且零时分秒，未见原始上传时刻；它不能单独把发布压到 04/25 UTC 零点。对照同站 [04/22 的另一条出版页](https://deepmind.google/research/publications/240658/) 也将日级 04/22 写为 `datePublished=2026-04-22T00:00:00+00:00`，支持这是 CMS 日期归一化而非个案精确上线钟。所链 [arXiv 2604.23099v1](https://arxiv.org/abs/2604.23099v1) 的 `Sat,25 Apr 2026 01:33:57 UTC` 是提交而非公告；按[arXiv 官方公告规则](https://info.arxiv.org/help/availability.html)，本窗无正常公告槽。再核[作者机构代码仓库](https://api.github.com/repos/google-deepmind/proeval)：仓库 `created_at=2026-04-17T23:59:55Z` 只证明 GitHub 仓库身份，当前 54 条可见 commit 的最早 `2026-04-27T18:13:15Z`，当窗前 `commits?until=2026-04-26T01:00:00Z` 为空且 Releases 为空。它不证明官网 04/25 页面当时没有公开，也不能代替论文全文首公开。需可核官网历史发布钟/快照或 arXiv 实际公告批次身份；当前保留于本日日期隔离，不从后来的 v2 倒灌机制/表格。
- 官方 GitHub release 层再核相邻边界：[`QwenLM/qwen-code` p338](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=1&page=338) `v0.15.2` 于 04/24T12:11:44Z， [p337](https://api.github.com/repos/QwenLM/qwen-code/releases?per_page=1&page=337) `v0.15.3` 于 04/26T06:49:56Z；[`MiniMax-AI/cli`](https://api.github.com/repos/MiniMax-AI/cli/releases?per_page=100) `v1.0.12` 于 04/26T01:40:29Z；[`MoonshotAI/kimi-cli` 1.39.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.39.0) 于 04/24T06:22:19Z、[1.40.0](https://api.github.com/repos/MoonshotAI/kimi-cli/releases/tags/1.40.0) 于 04/28T13:51:04Z；[`ByteDance-Seed/VeOmni`](https://api.github.com/repos/ByteDance-Seed/VeOmni/releases?per_page=100) 04/15T10:40:08Z→04/27T08:21:57Z。均非本窗 release；这只覆盖所查仓库的当前可见 release 层，不作组织级零发布保证。

本日作者侧下一步：将 14 来源可见停点与具名历史入口限制写成 V3 六部分报告；对两条日期隔离只保留题摘贡献线索，不评分、不做 Books 正面采用。随后请非作者核来源停止范围、两个首公开隔离和零确定候选分母；格式校验不能代替日级 Gate。
