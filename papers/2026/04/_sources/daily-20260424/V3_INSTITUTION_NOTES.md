# 04/24 每日机构有界入口

作者 apr01，访问日2026-09-27；目标窗口 `[2026-04-23T09:00:00+08:00,2026-04-24T09:00:00+08:00)`。记录实际读取及停止范围，不以当前网站能读证明历史无遗漏。公开目录日期、仓库created、RSS pubDate、arXiv首次公告分别解释；原目录外未列论文不作零更新断言。

| Daily来源 | 本轮实际读取的入口与停止范围 | 本窗结果/限制 |
| --- | --- | --- |
| SRC-OPENAI | [News RSS](https://openai.com/news/rss.xml)实际1230条，原`pubDate`：GPT5.5公告/card Thu23Apr11:00GMT、Academy指南10:00GMT；邻04/22→04/25。公告、Deployment Safety HTML及46页PDF的Intro/Change log和§7.2必要段已读。 | 两条GPT材料合一模型/card家族；原始19:00BJT发布落窗。当前card明示04/24 API补充、08/19局部评价纠正，不能把后发API变化回填；§7.2协议单独核原版有效范围。Academy核心指南已读主文并具体前分母关闭，见下文；RSS不覆盖Research/Index历史分页缺口。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)原始HTML的`publishedOn`邻04/22T14:12:30.673Z、14:27:03.434Z→04/29T20:26Z。 | 此公开研究目录未命中；不代其他未列事件。 |
| SRC-GOOGLE-AI | [Research April](https://research.google/blog/2026/04/)实际9个条目04/29→04/22→04/21→04/16...04/03；DeepMind April页3实际7个日期04/30/27/23/22/15/14/02；进入[Decoupled DiLoCo](https://deepmind.google/blog/decoupled-diloco/)核心原文。 | Research博客本窗无条目；DeepMind April23 DiLoCo与21428同family，日历日不能单证本窗。原文区分模拟与Gemma4真实系统；Pub目录year2026历史停点尚不能确认，保留精确限制，不扫全年论文。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)网页工具空正文；已有April Blog邻界记录但不是Research目录完整停点。 | 研究历史目录本窗覆盖受限，不能称零论文；需可验证本窗Research/artifact目录恢复。 |
| SRC-QWEN | 官方`api/page_config?code=research.research-list`60静态项均≤2025，加`api/v2/article/retrieval?type=qwen_ai&language=en-US`40动态项；04/22T10+08 Qwen3.6-27B→04/28T10+08 FlashQLA。 | 此concat公开研究列表本窗无条目；组织新仓库检查见下，不能覆盖所有旧repo release。 |
| SRC-DEEPSEEK | [News](https://www.deepseek.com/news/)实际News Sep10→April24V4→2025Dec1；Research June24V4paper→Feb25DualPath→Jan28OCR2。V4-preview原文web/raw均实际可读。 | April24 V4-preview只给日历日，raw HTML无`datePublished/dateCreated`，不足确认09:00前；DATE-DEEPSEEK-V4-PREVIEW-APR24已安全隔离，见下文重开条件。June24技术论文不倒灌April预览机制。 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)26条最新2025Nov7，组织新repo API实际43条。 | Blog列表不能证明2026本窗完整；目录历史覆盖隔离。没有本窗新repo不等于已有repo无release。 |
| SRC-TENCENT-HUNYUAN | 官方POST`https://api.hunyuan.tencent.com/api/blog/publicList` JSON pageNum1/pageSize100/renderType0，9/9全部；Hy3-preview `displayPublishTime=1776873600`即04/23T00+08，下一04/30T15+08。 | 该公开全部目录无本窗条目，Hy3早于09:00起点，不能因April23页面日把它计入。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)web超时但raw200~1MB恢复，15 rendered cards：May20→April29ScalingPain→Apr7GLM5.1→Apr1GLM5VTurbo→Mar15。 | 公开Research列表本窗无条目；createAt/媒体时间不冒充发布。组织新repo53条见下。 |
| SRC-BYTEDANCE-SEED | 官方GET`api/get_article_list_v2` header`x-tt-locale: US`；type1 Publications/page0+20/count20,total242,next40：MegaScaleOmni04/26T00+08→ContextUnrolling04/23T00+08→Seed3D2Apr22T00+08。type2Blog/page0+20,total95,next40，嵌套ArticleMeta.PublishDate与ArticleSubContentEn.Title实际读取：Jun19→Seed3D2Apr23T00+08→Apr9T00+08→Apr1T00+08，页20已到2025。 | 置顶项不能当排序停点，实际两页各条元数据已检查。公开Blog无本窗条目；Publications ContextUnrolling21921有窗前目录线索，需family-specific公开日期隔离，不按arXiv库存硬归本日。API午夜可能是页面日期粒度，不称精确首发。 |
| SRC-BAIDU-ERNIE | [中文Blog](https://ernie.baidu.com/blog/zh/)web超时，raw200恢复首10条，ISO邻04/30T00Z→04/15T00Z→Feb6。 | 该日期列表本窗无条目；不推全部作者/仓库无论文。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)实际Paper8：June29→Mar13→Feb3；Blog14未给日期。 | Paper目录本窗无项，Blog缺日期不继承Paper零命中。两个本窗created新repo已读必要说明并具体前分母关闭，不再追不影响处置的完整公开史。 |
| SRC-MINIMAX | ENblog12日期：May27/26→Mar18；CN重定向minimax.cn/blog13日期：Apr27→Mar18；AgentTech单May13可见项。 | 这些公开日期列表本窗无项，组织35新repo范围见下，不推所有artifact。 |

## 组织新仓库的有限补查

本轮官方GitHub `GET /orgs/<org>/repos?sort=created&direction=desc&per_page=100` 八组织均HTTP200、无next Link。实际条目数：QwenLM58、deepseek-ai39、MoonshotAI43、Tencent-Hunyuan83、zai-org53、ByteDance-Seed63、XiaomiMiMo18、MiniMax-AI35。仅按本窗created定位新artifact线索，不遍历普通PR/旧repo全部release；私有仓库转公开未必等created，历史完整性仍受此限制。

- [MiMo-V2.5-ASR](https://github.com/XiaomiMiMo/MiMo-V2.5-ASR) `created_at=2026-04-23T12:59:55Z`。
- [MiMo-Skills](https://github.com/XiaomiMiMo/MiMo-Skills) `created_at=2026-04-23T12:10:40Z`。
- [SimArt](https://github.com/ByteDance-Seed/SimArt) `created_at=2026-04-23T03:25:52Z`。

三项在发现时只是原始线索，不是已准入候选或首次公开证明；随后各README核心贡献已按下节具名关闭，不再保留普通待核队列。旧repo release/私有转公开仍是未覆盖的外部历史限制，不扩为八组织所有历史内容。

## 本轮命中核心处置

- [Everyday work with ChatGPT Work](https://openai.com/academy/how-to-use-chatgpt-work-for-everyday-tasks/)：本轮重新取官方 RSS，确切 `pubDate=Thu, 23 Apr 2026 10:00:00 GMT`、URL与标题相符。实际读页面主文与工作流说明；内容是把现有calendar/messages/docs等上下文转成brief、plan、audit等产物，再人工查证/编辑的产品使用指南，没有新状态机制、评价协议或大模型设计反证，前分母关闭。当前页面已把早期Codex标签改成ChatGPT Work，不将后发产品措辞作为April技术事实，亦不为此追全部版本史。
- [MiMo-V2.5-ASR](https://github.com/XiaomiMiMo/MiMo-V2.5-ASR) README Introduction/Abstract/Results/API 与其实际 Blog 链接 [mimo-v2-5-asr](https://mimo.xiaomi.com/mimo-v2-5-asr) 主文和表格均重新打开。mid-training/SFT及“novel RL algorithms”未披露目标/采样/更新机制，WER表与场景展示不能独立建立训练设计增量；本次仅原始发布事实线索，前分母关闭，不评分或写Books。不以repository created冒充精确公开，不把“更强方言/lyrics”或榜首当跨模型机制证明。
- [MiMo-Skills](https://github.com/XiaomiMiMo/MiMo-Skills) 实际 README Skills/Installation/Environment：TTS API voices/cloning/style/dialect控制与skill分发是产品接入组合，未给新的授权执行或模型训练合同；前分母关闭，读源中的安装命令未执行。
- [SimArt](https://github.com/ByteDance-Seed/SimArt) 实际 Overview、coordination alignment、inference接口及引用：sparse3D VQ-VAE、part decomposition/kinematic预测和URDF输出属于已关联 `2603.23386` 家族实现，repo创建不是论文新首发。README的新接入步骤未增加独立恢复/physics有效性保证，本次artifact组合关闭，不将“sim-ready”当物理真值；未运行下载或安装命令。

## 命中模型家族与终态范围

### OpenAI GPT-5.5：版本事实与受限评价协议合并为一族

[公告](https://openai.com/index/introducing-gpt-5-5/)与[System Card](https://deploymentsafety.openai.com/gpt-5-5)的RSS `pubDate=Thu, 23 Apr 2026 11:00:00 GMT`，即本窗04/23T19:00+08，合为 SF-2026-OPENAI-GPT-5-5。发布事实不证明内部架构；不回填04/24 API safeguards或08/19生物评价纠正。当前页明确这些更新，采用范围只取模型/card的受限评价协议，未声明取得原版不可变全文。

2+2+2=6，保护评价深入必要审阅完成，拟已有覆盖 PLATFORM-EVALUATION-SYSTEM Ch66。实际重开§7.2–7.2.1：固定真实coding-prefix后，以当时code state/原轨迹支持外部工具模拟，成对重采样再经monitor及人工分组。模拟难辨只检一类realism，不证明真实副作用；去掉已知类别后的severity-threshold漏检说明已知故障高recall不能当未知故障发现率。只是内部风险信号，不外推外部部署保证。Ch66实际“Offline/Replay/Shadow”区分未记录状态和反事实、“评测环境自身也必须成为被验证对象”绑定simulator/scorer身份，“Confidence/Calibration”按verifier与风险分布切片重校准，已承载本次长期边界。额外simulation/monitor/human成本与内部样本选择保留；不声称现章已包含厂商全部分类或比例，不新增Books。待非作者核此具体Existing及日期，不用产品榜单/参数宣传代替机制。

### DeepSeek V4-preview：日期保留项，不先评分或采用

[官方预览](https://deepseek.com/en/news/v4-preview/)、[Transparency](https://www.deepseek.com/en/transparency/)及[官方model card](https://fe-static.deepseek.com/chat/transparency/deepseek-V4-model-card-EN.pdf)本轮定点补检均只给April24 release date；已有raw HTML无发布时间字段。它与本窗相交但不能证明09:00前首次可得，因此保留 DATE-DEEPSEEK-V4-PREVIEW-APR24，不进入确定候选/评分/Books。June24论文及当前更新后的card不能补造April24 09:00前机制。定点重开材料是官方带时区的发布日志、当时可验证public commit/release时间或同家族公告记录；当前仅页面日期不足，不要求重扫整个机构或全部发表史。此项日期已安全隔离，不再称普通未读。

## 来源外部保留项与普通待办分开

OpenAI Research/Index历史分页、Google Research Publications本窗可验证停止点、Meta Research空正文、Moonshot2026公开目录、MiMo Blog14条缺日期，以及组织旧repo release/私有转公开未覆盖，均不支持本窗零更新/全站无遗漏。已有公开入口与恢复尝试在上表；重开只需相应本窗可验证目录/日期清单，不扩历年。Academy及三个新repo已具体关闭；DeepSeek单项已日期隔离。2026-09-30恢复时，arXiv必要证据与29项本窗书稿及写后核已经形成，普通书稿待办为0；最终候选准入/日期和非作者日级复核仍是可执行工作，不能借外部限制标整个日报已完成。
