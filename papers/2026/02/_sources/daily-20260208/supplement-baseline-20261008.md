# Daily Research — 2026-02-08

**规范：** V3
**窗口：** 2026-02-07T09:00:00+08:00 ～ 2026-02-08T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-03T15:08:31+08:00

## 1. 结论

本窗确定候选 1 家族：[nanobot v0.1.3.post5](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5) 的分发发布改变工具防护的版本采用边界，已深入核受影响的精确 tag 与直接安全反侧，决定仅报告；Books 整合与已有覆盖均为 0。当前维护者警告此版 WhatsApp 存在漏洞，不应安装；这个后来页面警告不能倒填成本窗首次事件。14 个每日来源与 1 个表外线索完成本轮有限检查；部分历史目录与 Anthropic 更正的精确日期仍不可恢复，它们是被隔离的终态保留项，不是正面 Coverage/Evidence 或“全网没有新研究”的证据。

[arXiv 官方排程](https://info.arxiv.org/help/availability.html#announcement-schedule)在美东周五、周六没有常规公告；本窗对应 2026-02-06T20:00:00-05:00 ～ 02-07T20:00:00-05:00。因此常规新稿与替换批次为零，没有把提交日、注册日或整月分类元数据变成逐项题摘队列。这个判断不排除作者外站周末先公开或特殊公告。

发现 [Anthropic Healthcare 更正](https://www.anthropic.com/news/healthcare-life-sciences)：厂商澄清 HIPAA-ready 产品的适用对象，可能改变服务表面的合规判断，但更正只给出 February 7, 2026，未披露时区与时刻，无法确定归本窗。保留该事实及精确重开条件，不把它评分、收入确定候选或写入 Books；也不把医疗场景作为自动排除理由。当前扫描、题摘、正文、Books 与独立复核普通待办均为 0；root 独立日级验收通过。

本轮独立从原始入口重建，不继承旧 V2.1 的零候选、来源注册表生效日排除或全月完成标签，不使用旧 Weekly 候选与评分。详细入口、字段、停止范围与具名初筛理由见[本日停点](../_sources/daily-20260208/STOP.md)。

## 2. 来源覆盖

检查范围为 ROADMAP 七个 Part 的模型、学习/表示/优化、训练、推理、平台、Agent、多模态、World Model 与 VLA 主线；AI for Science 暂缓。下表“已检查”只描述实际可恢复范围，搜索无结果、当前首页和未知历史片段均不证明无遗漏。没有扫描每周来源；日期补检缓存触发 nanobot 具名发布与安全说明定点恢复，不扫描该机构或项目全库。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 首查后恢复[官方 RSS](https://openai.com/news/rss.xml)，XML 的 2 月日期片段跨 Feb06 10:00 GMT → Feb09 11:00 GMT，无本窗条目；保留[原字段](../_sources/daily-20260208/feb08_stage2_0.txt)。只核窗口邻接，不审全年目录。 | 已检查 | RSS 支持其收录发布范围，不证明所有独立项目页或未收录更正完整。 |
| SRC-ANTHROPIC | Research 页实际嵌入 174 条 publishedOn/title，2 月邻接 Feb05 → Feb16，见[目录字段](../_sources/daily-20260208/feb08_stage3_0.txt)；日期域限定补检找到 Healthcare 更正，定点读实际说明。 | 受阻 | 更正无时区/时刻；原发布日期与 8 月整页 dateModified 不能代替更正事件时间。 |
| SRC-GOOGLE-AI | DeepMind Research → Publications 第一显示页实际跨 Feb05 → Feb12；Blog 只显示近期页。Google Research/pubs 第一页按年份，不具日级首公开字段；Feb07/08 官方域补检及 Blog 原生恢复停止，见[目录返回](../_sources/daily-20260208/feb08_webI.txt)与[有限范围](../_sources/daily-20260208/STOP.md)。 | 受阻 | DeepMind Blog 与 Google Research 本窗历史首公开片段未完整恢复；没有遍历 773 页或全年论文，也不据当前年份列表断言零发布。 |
| SRC-META-AI | Research 返回 0 行；Feb07/08 官方域检索无确定事件，月度定点补检打开 Audiobox 原文的 demo 停用声明，见[原文](../_sources/daily-20260208/feb08_webJ.txt)。 | 受阻 | 0 行与空搜索不是历史零发布证据。Audiobox 声明按具体增量关闭，不算论文撤回。 |
| SRC-QWEN | Legacy 页停于 2025-09，转向官方 qwen.ai 后动态页无日期列表；原生 HTML 及本窗日期官方域补检有限停止。Qwen-Image 2.0 显示 02/10，Qwen Code 周更显示 02/03 与 02/09，均非本窗，见[原目录与日期](../_sources/daily-20260208/feb08_webF.txt)、[恢复](../_sources/daily-20260208/feb08_stage3_2.txt)。 | 受阻 | 未恢复完整本窗模型事件片段，不把周更总结重置成窗口事件。 |
| SRC-DEEPSEEK | 首页与官方 GitHub overview，官方域 Feb07/08 定点补检，无确定落窗材料，见[原入口](../_sources/daily-20260208/feb08_webA.txt)、[官方组织](../_sources/daily-20260208/feb08_webG.txt)。 | 受阻 | 当前项目列表不是历史版本时间线；未全扫普通 PR，不能据无检索命中判零发布。 |
| SRC-MOONSHOT | Platform Blog 显示 25 项、最新 2025-11-07；官方组织当前 overview 和指定日期补检，见[原目录](../_sources/daily-20260208/feb08_webB.txt)、[组织范围](../_sources/daily-20260208/feb08_webJ.txt)。 | 受阻 | 不把 repo 当前 Updated 当首次公开；无法恢复完整本窗研究/重要版本片段。 |
| SRC-TENCENT-HUNYUAN | 首查 Research 为 0 行；浏览器有限尝试依次超时、子线程不支持 visibility、取消该选项后仍超时；root 独立浏览器恢复也超时。原生页面与真实公开脚本只恢复路由，不含论文列表；官方域日期补检停止，见[有限恢复](../_sources/daily-20260208/feb08_hunyuan_finite.txt)及[双方停止点](../_sources/daily-20260208/STOP.md)。 | 受阻 | 无法读取研究“全部”历史列表；不能称已浏览全部、零命中或正面 Coverage。 |
| SRC-ZAI | 首查 Research 实际跨 02/02 GLM-OCR → 02/11 GLM-5；官方 release notes 跨 02/03 → 02/12。停止于本窗两侧邻接，见[Research 原列表](../_sources/daily-20260208/feb08_webB.txt)、[停点中的发布字段](../_sources/daily-20260208/STOP.md)。 | 已检查 | 只覆盖这两个显示列表，不声称机构所有更新。 |
| SRC-BYTEDANCE-SEED | Research/论文首查后依真实前端恢复 get_article_list_v2；论文 offset20/40/60，60 的 next=80 已跨本窗附近 02/09 → 02/05；Blog offset0（US locale）14 条、has_more=false，最早 02/12。保留[实际页](../_sources/daily-20260208/feb08_seed_pages.txt)、[末段与 Blog](../_sources/daily-20260208/feb08_seed_tail.txt)。 | 已检查 | 未称 242 条全部题摘。PublishDate 是目录日字段，不是首次公开瞬间；locale/显示数量不一致保留，空的非 US 页不作为覆盖证据。 |
| SRC-BAIDU-ERNIE | 技术 Blog 第一页实际跨 02/06 ERNIE5 → 04/15 ERNIE-Image，停止于本窗邻接，见[原列表](../_sources/daily-20260208/feb08_webB.txt)。 | 已检查 | 仅此官方 Blog 发布范围，不外推全部项目版本。 |
| SRC-XIAOMI-MIMO | Paper 当前列表跨 02/03 HySparse → 03/13 ARL-Tangram；Blog 当前 15 项无日期，官方域精确日补检未有确定事件，见[页面](../_sources/daily-20260208/feb08_webF.txt)、[原生范围](../_sources/daily-20260208/feb08_native2.txt)。 | 受阻 | 不以论文邻接证明整个 Blog 覆盖；未知日期的更多历史片段隔离。 |
| SRC-MINIMAX | 英文 Blog 当前 12 项跨 01/27 M2-her → 02/12 M2.5；中文替代重定向 minimax.cn。Agent Tech Blog 只返回导航，官方域日期补检有限停止，见[原目录](../_sources/daily-20260208/feb08_webF.txt)。 | 受阻 | Agent techblog 必要历史目录不可恢复；其他可见列表无当窗记录不是所有研究零发布保证。 |
| SRC-ARXIV | 官方排程覆盖本窗美东周五晚至周六晚，无常规新稿/替换公告；13 机构源定点补检未发现应归本窗的具名事件，见[排程原文](../_sources/daily-20260208/feb08_webA.txt)及[停止边界](../_sources/daily-20260208/STOP.md)。不把整月元数据变成逐项队列。 | 已检查 | 常规公告为空不证明作者外站或特殊临时公告无事件；不宣称全学科/全网召回。 |
| 表外：[HKUDS/nanobot](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5) | 从初始搜索的 Intellio-Labs 镜像 News 链接恢复上游 release API，published_at 精确落窗；只核该 tag 工具护栏、文件限制传递、依赖声明、安全说明与当前 WhatsApp 反侧，见[发布及事件字段](../_sources/daily-20260208/feb08_nanobot_exact.txt)、[精确 tag](../_sources/daily-20260208/feb08_nanobot_tag.txt)。 | 已检查 | 静态审阅，没有安装、攻击复现或运行验收；当前安全警告首加日期未知，不倒填本窗。 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [nanobot v0.1.3.post5](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5) | 2026-02-08T02:08:44+08:00 | 工具安全修补从已公开 PR 进入本窗分发版本，需要重核采用前提而非由 release 标签授安全；2 + 2 + 1 = 5 | 深入完成 | 仅报告 |

确定落窗候选 1 家族、深入审阅 1 家族。评分只针对本窗分发采用命题，Durability=1 是版本相关工程事实；不把 provider 名称、4,000 行代码或成熟安全原则抬分。机构目录与搜索返回只作本窗线索，不计为当日新论文。Anthropic 更正因为必要日期字段未决放在第五部分，不先占确定候选席位。

## 4. 证据与知识整合

### [nanobot v0.1.3.post5](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5)

官方 release API `published_at=2026-02-07T18:08:44Z`，转换为北京时间 02/08 02:08:44，确实落窗；`created_at=18:01:14Z` 不是发布依据。当前 body 的 `updated_at=2026-02-18T15:06:22Z` 不能定位 WhatsApp 警告首次加入时间。[#77](https://github.com/HKUDS/nanobot/pull/77) 的安全报告与合并分别为 02/04、02/06，不能重置成本窗首次发现；本次处理的是这些修改进入指定分发版本的采用前提。

[精确 tag 静态字段](../_sources/daily-20260208/feb08_nanobot_tag.txt)支持的边界很窄：`shell.py` 仍执行 `create_subprocess_shell`，护栏自称 best-effort，按危险模式及可选 allow-pattern 检查；`ToolsConfig.restrict_to_workspace` 默认 false，`AgentLoop._register_default_tools` 只有启用时才给四个文件工具传 `allowed_dir`，并向 ExecTool 传该开关。`filesystem._resolve_path` 使用 resolved path 的字符串前缀判断，并非独立 OS 沙箱。`pyproject.toml` 仍是 `litellm>=1.0.0`，不能把原 PR 推荐的固定 patched 版本当作实际安装依赖，也不采纳其 `CVE-2024-XXXX` 占位符为真实 CVE。上述是 artifact 静态核验与作者说明，不是漏洞复现、依赖安全审计或生产能力证明；本轮不引用未经独立重放的 PoC 成功数。

同 tag SECURITY 的 Limited Command Filtering、无自动 session expiry 与生产配置要求，及[当前 release 警告](../_sources/daily-20260208/feb08_nanobot_release.txt)，直接限制“安全修复即隔离成立”的解读。维护者要求不要安装 post5；post7 的 WhatsApp 修补说明只用于识别此版本的直接反侧，不把窗外修补记为本窗贡献，也不证明 post7 全面安全。因此本项仅保留发布采用边界和未证明内容，不推荐该版本。新公开贡献是这一版本的分发事实，不是首次提出命令/文件权限隔离；没有可由本次证据支持的新长期机制差额，Books 决定为仅报告，而非主题式“已有覆盖”。

未新增书稿，未把零改动包装为已有覆盖。

范围与准入的具名负侧保存在[本日停点](../_sources/daily-20260208/STOP.md)：Qwen Code 周更事件窗外；Interconnects tracked-models 变动只是旧模型收录；Muin 工作日志是应用上线/营销组合，未有新执行机制或可靠性评价；Google Year-in-Review 命中的 February 7 实为 2023 年。它们没有被拼成必须逐篇深审的工作量。

[Meta Audiobox 原文](https://ai.meta.com/blog/audiobox-generating-audio-voice-natural-language-prompts/)仅新增 2026 年 2 月 demo 不再可用的通知。已定点检查该声明与相关 responsible implementation，未看到论文撤回、方法纠错或水印/认证安全失效说明；本日报也没有依赖该 demo 的采用命题。此访问生命周期变化没有新增或修正拟保留的模型机制与可靠性判断，贡献前关闭；不伪装成 withdrawn 论文，也不为不影响关闭的月精度继续追时刻。

## 5. 缺口与下一步

普通可执行材料与复核待办：无。以下外部终态保留项不用于正面证据或 Books，不算正面 Evidence/Coverage 通过，不支持无遗漏断言或性能/安全保证；各项保留定点重开条件。

- **Anthropic Healthcare 更正事件日期。** [原页](https://www.anthropic.com/news/healthcare-life-sciences)的 Changelog 只有 February 7, 2026，无时区与时刻。潜在增量是 HIPAA-ready 适用服务表面从个人 health integrations 中明确分开，不是新的内部保护机制。已读更正、对应两类产品分区及隐私说明；原 datePublished=2026-01-11T16:00:00.000Z、dateModified=2026-08-27T15:12:44.000Z，后者不能定位 2 月 7 日更正。因为原日范围不能确认完全落窗，不评分、不作候选、不整合。官方更正专属时间戳、当时可验证公开日志或可信时区明确的快照到达时，只重开此更正的日期与贡献判断，不遍历旧版或逐个 connector。root 已独立读原页并同意这条隔离边界。
- **历史目录切片。** Google Research/DeepMind Blog、Meta、Qwen 动态模型目录、DeepSeek、Moonshot、Hunyuan 研究“全部”、MiMo Blog 和 MiniMax Agent 目录，实际首查、日期补检、可用原生恢复与停止点在[本日停点](../_sources/daily-20260208/STOP.md)。缺少能绑定本窗口的完整相关历史发布片段；当前首页、空搜索、路由脚本或 repo Updated 不足代替。已有限恢复，未知部分隔离，不声称该范围零发布。出现官方历史分页/公开列表快照、明确本窗相关材料或可恢复的动态目录时，只重开对应来源与具名材料，不扩扫机构历年论文。Hunyuan 浏览器已有限失败，不无限重复超时。

Seed、Z.ai、ERNIE、MiMo Paper、MiniMax 主 Blog 的明确窗外邻接仅说明实际目录范围，不创建窗外审阅任务，也不阻塞本日安全终态。

## 6. 复核

复核者：root（独立非作者）。
结论：通过

root 实际顺读完整六部分及 14 来源的实际邻接/有限恢复范围，确认宽列表没有转成逐项队列；混元双方浏览器恢复失败与其余历史切片限制明确隔离。复核覆盖 1/1 确定候选：独立 GET 官方 post5 API 核精确 published_at，实际核指定 tag 的 shell/filesystem、config/loop 传递、SECURITY 限制和当前 release 警告。2 + 2 + 1 = 5 的版本采用命题、安全受影响深入审阅及仅报告决定通过；不重置旧 PR 日期或后来警告，不授强沙箱、已修补依赖、复现或生产安全保证。没有新长期机制差额，因此仅报告而非主题式已有覆盖；实际 Books 写入 0，无写后未办。

纠错/修订负侧另核 Anthropic introduction、Enterprise/personal 分区及 Changelog 和 Meta Audiobox 停用声明的贡献关闭：前者实质澄清保留日期未决，不能按医疗场景退出或外推个人合规；后者不伪装论文撤回。普通具名筛选的核验样本为 Qwen Code 周更、Interconnects 旧模型收录、Muin 工作日志、Google 2023 Year-in-Review 与 nanobot provider refactor；后者定点读说明只支持代码组织和接入维护便利，没有新增执行可靠性机制或评价，贡献前关闭，见[实际说明](../_sources/daily-20260208/feb08_nanobot_provider.txt)。复核不声称全部搜索命中、全年目录题摘或所有附件复读；原始范围与未查历史片段继续保留。

完成态 V3 校验、31 个本地引用和 Markdown 检查通过，本日报与本日来源范围的 cached/unstaged `git diff --check` 通过；机器检查不替代上述语义验收。普通待办 0，本日结束，不自行开始下一日。作者未修改 Books、索引或 LEARNING_STATE，未 stage、commit、push。

