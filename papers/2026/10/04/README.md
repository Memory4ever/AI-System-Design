# Daily Research — 2026-10-04

**规范：** V3
**窗口：** 2026-10-03T09:00:00+08:00 ～ 2026-10-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T15:44:37+08:00

## 1. 结论

本窗确认并完成受影响内容审阅的材料为 **3 个唯一家族**：DeepSeek Harness 的插件兼容契约，MiniMax OpenAgentCore 的部署入口、TLS 与管理密钥边界，以及 MiMo-Code 保留实例的 provider 刷新。它们提供具体版本变化，不提供训练收益、端到端性能或生产安全保证。三项均决定**仅报告**，没有 Books 写入或结构候选；这里不是“本次仅报告”任务，而是纳入 Books 判断后不把单版本实现差额直接提升为长期结论。

14 个日级来源均进行了本窗有界检查。目录条目、仓库更新时间及搜索结果只作为线索，不计为当天新论文；未统一归并原始命中数，因此不报告命中总量。正式候选 3、作者证据审阅完成 3、Books 改动 0。Qwen 文档翻译同步按具体贡献关闭；AutoClaw Law 在官方完整核心中未披露可采用的新增机制，按贡献关闭，不依搜索缓存日期准入。独立准入校准与报告写后总复核通过；外部覆盖限制仍按第 5 节隔离，不等于来源全部恢复。

arXiv 本窗没有常规公告批次：已经实查 12 个相关分类的当前列表与官方公告规则，不以提交时间冒充公开时间，也没有据此推断其他官方来源“零进展”。官方常规公告为美国东部时间周日至周四 20:00；本窗对应东部夏令时周五 10/2 21:00 至周六 10/3 21:00，下一常规批次为北京时间 10/5 08:00，窗外。动态目录、年粒度出版目录与不可达入口的限制见第 5 节；这些保留项不支持无遗漏断言。

## 2. 来源覆盖

检查限定于大模型架构、训练/后训练、推理/运行时、多模态/World Model/VLA、平台及 Agent；宽目录不转为逐项队列。首页面可见日期早于窗口时停止向历史分页扩展；不把未来出版年份或仓库最后提交日期直接认作首公开时间。当前官方页的撤回、纠错、安全与兼容提示作为必要反侧检查，未开展全站历史审计。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) → [研究索引](https://openai.com/research/index/) 当前首批 9 条；最新为 9/29 模型及安全附录，后续可见日期至 9/3；在 Load more 前停止。[原始检查](../_sources/daily-20261004/WEB_CHRONOLOGY.txt) | 已检查 | 不声称未加载条目或全站无遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 当前首批 10 条，最新 10/1，次为 9/30、9/29；See more 前停止；窗外不扩展核心库存。[记录](../_sources/daily-20261004/WEB_INITIAL.txt) | 已检查 | 仅当前首批，不外推全站 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) 当前 Latest news 与 publications 入口；[Google publications](https://research.google/pubs/) 首批 1–15/11587，年排序含 2027/2026，不当作每日队列；补 [Research blog](https://research.google/blog/) 首批 12 条最新 10/2。`query=language model` 原入口及带年份尝试不可达，有限官方域日期/模型主题补检未恢复日级公告。[初查](../_sources/daily-20261004/WEB_INITIAL.txt)、[博客](../_sources/daily-20261004/WEB_GOOGLE_RECOVERY.txt)、[替代入口停止点](../_sources/daily-20261004/WEB_ROUTE_RECOVERY.txt) | 受阻 | 年粒度论文目录不能证明本窗新增；终态保留 G1 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 返回空正文；[Publications](https://ai.meta.com/research/publications/) 不可达；[Blog](https://ai.meta.com/blog/) 当前一页 10 篇及 featured/latest 区，最新可见日为 7/27，非严格日期排序，Next 前停止；官方域 10/3、10/4 模型/研究补检未恢复对应事件。[博客与失败](../_sources/daily-20261004/WEB_FINAL_RECOVERY.txt)、[目录替代](../_sources/daily-20261004/WEB_ROUTE_RECOVERY.txt) | 受阻 | 不能把空目录/旧博客证明为零；终态保留 G2 |
| SRC-QWEN | [旧博客](https://qwenlm.github.io/) 可见首批 5 条最新 2025-09-23，导向新站；新 [Blog](https://qwen.ai/blog)/Research 均空正文；[QwenLM](https://github.com/QwenLM) pinned/overview 前 10 个更新仓库作线索，仅定点恢复窗内 qwen-code-docs 翻译同步；其 releases 无条目、窗口 commits 返回 1 条。新站官方域日期补检未恢复研究公告。[入口](../_sources/daily-20261004/WEB_RECOVERY.txt)、[组织页](../_sources/daily-20261004/NATIVE_GITHUB.json)、[定点事件](../_sources/daily-20261004/TARGETED_GITHUB.json) | 受阻 | 旧博客不能替代新站全列表；终态保留 G3 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/) 当前入口；更新/新闻原入口及中英文有限替代不可达；[官方组织](https://github.com/deepseek-ai) overview 前 10 个仓库定位 harness；该项目最新 3 个 releases 与窗口过滤的首批 commits，只采用 release `published_at` 与完整发布核心，不逐项审查普通 PR。[入口](../_sources/daily-20261004/WEB_NATIVE.txt)、[定点发布](../_sources/daily-20261004/TARGETED_GITHUB.json) | 已检查 | 仓库有界替代不等于新闻全量恢复；终态保留 G4 |
| SRC-MOONSHOT | [Kimi blog](https://platform.kimi.com/blog) 首查与有限重开均超时；[MoonshotAI](https://github.com/MoonshotAI) pinned/overview 前 10 个更新仓库，最新可见 kimi-code 10/2，其余更早；相关官方域日期/模型/Agent 补检未恢复本窗研究事件。[失败](../_sources/daily-20261004/WEB_RECOVERY.txt)、[组织页](../_sources/daily-20261004/NATIVE_GITHUB.json)、[最后有限替代](../_sources/daily-20261004/WEB_FINAL_RECOVERY.txt) | 受阻 | 组织更新时间不能排除未恢复博客发布；终态保留 G5 |
| SRC-TENCENT-HUNYUAN | [Research 首查](https://hunyuan.tencent.com/research) 空正文，有限原入口替代失败，浏览器创建该入口等待 30 秒超时/reset，未循环重试；[Tencent-Hunyuan](https://github.com/Tencent-Hunyuan) pinned/overview 前 10 个仓库，可见最新 UniRL 10/5、其后 9/25 等，不将未来更新算本窗；相关官方研究日期补检未恢复“全部”目录。[失败](../_sources/daily-20261004/WEB_RECOVERY.txt)、[官方仓库范围](../_sources/daily-20261004/NATIVE_GITHUB.json) | 受阻 | 浏览器失败不是零命中；终态保留 G6 |
| SRC-ZAI | [Research 首查](https://www.zhipuai.cn/zh/research) 及英文原入口不可达；[官方发布说明](https://docs.z.ai/release-notes/new-released) 当前最新 8/26；[zai-org](https://github.com/zai-org) overview 前 10 个仓库，最新 GLM-V 10/2；官方域日期补检定位 AutoClaw Law，完整官方核心后按贡献排除。搜索缓存 10/3 与当前页面 10/5 不混用。[恢复](../_sources/daily-20261004/WEB_RECOVERY.txt)、[排除核心](../_sources/daily-20261004/WEB_LAW.txt)、[组织页](../_sources/daily-20261004/NATIVE_GITHUB.json) | 受阻 | Law 非候选，不另追不影响处置的日期；目录终态保留 G7 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)、[论文目录](https://seed.bytedance.com/en/public_papers) 首批 1–20/242、page 1/13，最新 8/18，Next 前停止；Research 未标日的 SeedRealtime 由 [主页 Latest updates](https://seed.bytedance.com/en) 恢复为 8/5，窗外关闭；不因宽目录存在扩扫其他领域。[目录](../_sources/daily-20261004/WEB_NATIVE.txt)、[日期恢复](../_sources/daily-20261004/WEB_SEED_DATE_RECOVERY.txt) | 已检查 | 非全年论文覆盖 |
| SRC-BAIDU-ERNIE | [技术博客](https://ernie.baidu.com/blog/zh/) page 1/2、首批 10 条，最新 2026-05-09，Next 前停止；[ERNIE](https://github.com/PaddlePaddle/ERNIE) 官方 README Recent updates 最新标注 2025-11；官方域 10/3、10/4 相关主题补检无可采用的本窗发布。[博客](../_sources/daily-20261004/WEB_NATIVE.txt)、[官方 README](../_sources/daily-20261004/WEB_GITHUB_FALLBACK.txt) | 已检查 | 不外推所有开发历史 |
| SRC-XIAOMI-MIMO | [主页](https://mimo.xiaomi.com/) Paper 区 8 条最新 6/29，Blog 区 15 个未标日链接仅作线索；代表最新 tool-call repetition 官方正文恢复为 9/27，非本窗；[XiaomiMiMo](https://github.com/XiaomiMiMo) overview 前 10 个仓库定位 MiMo-Code，最新 releases 返回 2 条（9/22、9/23），窗口过滤 commit 1 条，再恢复 PR #2603 官方核心与合并时刻。[入口](../_sources/daily-20261004/WEB_NATIVE.txt)、[窗外日期](../_sources/daily-20261004/WEB_MIMO_META.txt)、[版本事件](../_sources/daily-20261004/NARROW_EVENT_CORE.json) | 已检查 | 不把其余未标日链接当候选或声称全已排除；终态保留 G8 |
| SRC-MINIMAX | [英文博客](https://www.minimax.io/blog) 首批 13 条最新 8/13，[中文博客](https://www.minimaxi.com/blog) 首批 10 条同类公告；[Agent Tech Blog](https://agent.minimax.io/docs/techblog) 当前可见 3 个入口；[MiniMax-AI](https://github.com/MiniMax-AI) overview 前 10 个仓库定位 OpenAgentCore。定点读取最新 3 个 releases、窗口过滤首批 30 commits 仅作版本/安全线索，停止后不扩普通 PR；三个发布合为 1 家族，必要配置与安全/纠错信号已核对。[入口](../_sources/daily-20261004/WEB_NATIVE.txt)、[发布](../_sources/daily-20261004/TARGETED_GITHUB.json)、[精确配置](../_sources/daily-20261004/PRECISE_VERSION_FILES.json) | 已检查 | 不声称首批 30 commits 等于该项目全窗口历史；未运行发布包 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html) 与 cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA 的 `/list/<category>/recent` 首页面，均实际 GET 200，日期段最新 10/5，容量较小分类后接 10/2；web 列表可见相关标题仅作日期/主题查漏。每类在首批 ≤50 处停止，不扩 10/5 窗外候选；三组 arxiv.org 域日期主题补检返回旧材料，无可采用当窗事件。[实际日期段](../_sources/daily-20261004/NATIVE_ARXIV_DATES.json)、[可见列表](../_sources/daily-20261004/WEB_ARXIV_AND_LAW.txt)、[补检限制](../_sources/daily-20261004/ARXIV_BOUNDED_SEARCH.txt) | 已检查 | native 标题字段解析为空，只采用其日期段，不将其称完整题摘筛选；不是全学科或所有站外首次公开召回 |

无需启动周级或会议全站扫描。表内官方 GitHub 只是已列日级来源的有限替代与候选必要原源，没有另增每周发现任务。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [DeepSeek Harness v0.2.1-alpha.1](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.1-alpha.1) | 2026-10-03T14:42:19+08:00 | 插件子路径元数据、诊断导出与扩展入口的破坏性兼容契约；1 + 1 + 1 = 3 | 深入完成 | 仅报告：alpha 版本迁移事实，不建立长期兼容机制结论 |
| [OpenAgentCore v0.0.7–v0.0.9](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.9) | 2026-10-03T12:38:03+08:00 | 将发布入口移至 Web、撤去容器内托管 TLS/Docker socket 与 host Core admin port，并调整 URL/密钥契约；1 + 2 + 1 = 4 | 深入完成 | 仅报告：版本拓扑与操作者责任，不证明生产安全或新授权理论 |
| [MiMo-Code：Provider Refresh Without Instance Disposal，PR #2603](https://github.com/XiaomiMiMo/MiMo-Code/pull/2603) | 2026-10-03T19:11:41+08:00 | 保留 Instance 的 provider refresh：idle admission、先准备后统一发布、忙时不排队、closing-owner sampling 拒绝；1 + 1 + 2 = 4 | 深入完成 | 仅报告：局部 SDK/运行时契约及可复用约束的实现例证，不扩大为通用热更新保证 |

三项虽低于标准审阅分档，兼容、部署/安全和生命周期纠错信号均按合同深入核对受影响内容。评分按 Design Delta + System Reach + Durability；深读深度不反向抬高评分。

## 4. 证据与知识整合

### [DeepSeek Harness v0.2.1-alpha.1](https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.2.1-alpha.1)

采用官方该 tag 的完整中英文发布核心，[原始 `published_at` 与正文](../_sources/daily-20261004/TARGETED_GITHUB.json)为 `2026-10-03T06:42:19Z`，加 8 小时落窗；提交或发现日不用来代替这个发布时间。同页的 **Chores/其他变更** 明确移除 runtime invariant 插件与包的 `./invariant` 导出，依赖它的扩展/custom profile 必须迁移；子路径插件不再读独立 `package.json`，文本/图标从子路径导出；旧 `stats` 注册 ID 拆成 `activity`、`usage`。

反侧限制决定采用范围：所谓 Claude Code Mods compatibility layer 是实验性 API 能力子集验证，发布方明确不是实用完整兼容；HMR 修复入口/依赖映射及启停后的残留不等于已安装包任意热替换，替换版本仍需重启。任务 stop/resume/stop 后排队消息恢复是该版本修复，不据此宣称 durable task 或 exactly-once。模式默认值只影响新默认，既有会话保留模式；reminder tools 的 Standard/Creator/PTC 与 Minimal/subagent 可用性不同。

这些事实足以关闭本次兼容事件，不需要展开发布页每个 UI 修复、全 changelog 或旧版附录。没有可比较的性能实验，也不把官方预期当本地验证。当前发布核心未见撤回/纠正该采用范围的提示；这只是该页轻量检查。Books 判断是“单版本迁移契约”，不是“已有章节已覆盖”，不伪造 owner 证据、不改书。

### [OpenAgentCore v0.0.7–v0.0.9](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.9)

三个官方 release 的 `published_at` 依次为 `2026-10-03T04:38:03Z`、`05:43:53Z`、`11:49:56Z`；发布核心分别绑定源码 `5b0da47b…`、`b4e5d8e…`、`99ba9b48…`，不把它们算 3 个家族。release 只有 Linux amd64 distribution 描述，因此必要证据进入对应精确源码，而不是靠一句摘要推安全结论。

版本变化的实证来自 [受影响部署 diff](../_sources/daily-20261004/AFFECTED_DEPLOY_PATCH.json) 与 [v0.0.9 精确配置](../_sources/daily-20261004/PRECISE_VERSION_FILES.json)：移除 gateway/Caddy、托管 HTTPS 与 domain 控制入口；服务为 init/database/core/web，Web 将 `/v1`、`/api/v1`（v0.0.9 还包括 `/docs`）原样送 Core，不另加它自己的凭据。Core 的授权责任并未消失；`/core/v1` 仍是在 console sign-in/same-origin 后用 Core key 转发。Core admin 的 host loopback port 被去掉，Web 是唯一 published entry，容器不再挂 Docker socket。TLS 由操作者的反代或托管平台终止，不是取消 TLS 的需要。

必要反侧已核对，[v0.0.7/.8 ports 及安全变化](../_sources/daily-20261004/MINIMAX_SECURITY_AFFECTED.json)：两版本均只发布 Web；v0.0.9 把 ports 合进 compose，旧 `ports.yaml` 404 是文件布局变化，不是证据缺失。`ValidateCoreURL` 不再要求非 loopback 必须 HTTPS，HTTP/HTTPS 都允许，但仍要求无 path/credentials/query/fragment；地址合法不能保证传输机密性。`oac_admin_` 前缀便于辨认，随机源仍为 32 字节，不把前缀推成额外随机安全。标为“Fix Compose admin key validation”的 `c7f087…` 实际只是 smoke-test 的格式断言从长度 64 改为匹配前缀+64hex，并非授权漏洞修复。

还须保留部署可复现性边界：精确 tag 的 compose 仍使 Core/Web 默认使用浮动 `:latest`（可用 `OAC_IMAGE_*` 覆盖）；源码版本与实际运行镜像不自动等同。只核了必要代码、配置与作者契约，未启动 Compose、验证实际网络隔离、秘密轮换或公网 TLS。有限窗口首批 commit 安全/纠错线索已处置，不宣称审阅所有提交。Books 不把某套产品的拓扑简化当普遍最安全架构；本窗仅报告其具体版本责任移动。

### [MiMo-Code：Provider Refresh Without Instance Disposal，PR #2603](https://github.com/XiaomiMiMo/MiMo-Code/pull/2603)

采用已合并 commit `6babeb0b98f9b4818bddf04a4331edfee04dbf85`。官方 PR 创建/合并事件 [API 原字段与完整核心](../_sources/daily-20261004/NARROW_EVENT_CORE.json) 均落窗；这证明 PR 公共事件时间，不等于某二进制正式发布。PR 描述仍写“draft for human review”，与 API 显示已经 merged 分开记录，不能用该句否定实际合并，也不能据此宣称 Desktop 已交付。

原约束是 provider/model 配置更新通过 dispose directory Instance 同时损失会话、订阅与待交互状态。新 `POST /global/provider/refresh` 与 `client.global.refreshProviders()` 用 [精确 `refresh.ts`/spec S1–S6](../_sources/daily-20261004/PRECISE_VERSION_FILES.json) 的 `Instance.updateIdle` 守住现有上下文：全部 candidate/model view 先准备，再发布 commit callbacks；准备失败保留旧 view，busy 返回 `pending` 且不后台排队，调用方须检查状态并重试，不能把保存配置称为已生效。

[必要 Instance/MCP diff](../_sources/daily-20261004/MIMO_LIFECYCLE_PATCH.json) 核对了生命周期反证：`updateIdle` 检查 requests/executions/closing/pending/failed，更新期阻止新 claim，并让 disposal 等待；MCP sampling 用 `acquireUseRelease` 覆盖实际异步操作，不仅计入口请求；`expected` owner 在 closing、cache 不存在或 context 身份已变化时拒绝，避免陈旧 callback 误认新实例。这支持局部 admission/publication 机制，并不证明所有插件副作用都可回滚或跨进程一致。

spec 的明确边界限制长期采用：只刷新 model/provider fields，cold Config/plugin 不被初始化，已有 plugin hooks 复用；MCP/skill/plugin 配置变化仍需显式重启；旧 SDK 对象不立即撤销，原 auth/OAuth 语义未改，不是 credential revocation 新协议，也非任意 SDK/package 热替换。没有 Desktop 改动或 DB migration。作者记录的 110 affected regression tests、独立进程 6+7 refresh tests 及 Node smoke 未由本次复现，外部 OAuth/第三方插件副作用仍不受这些 fixture 保证。当前必要材料未见撤回该局部实现的标记。

将其作为版本相关运行时契约完成处置，而不是沿 API 名字新建“热更新章节”；没有充分跨实现或真实负载证据把它提升为默认平台设计。Books 本窗不改，未声称已有具体正文全面承载这个实现。

## 5. 缺口与下一步

**尚可执行的本窗工作：** 无。全部 3 个候选已获得必要证据及 Books 判断，非作者写后总复核通过；无本日未落实的 Books 修改。

**本窗终态保留项（已隔离）：** 以下当前入口已做有限原始替代、官方仓库/公告或日期主题检索；继续同一空响应/超时不能产生证据，停止无界追查。它们不进入候选，不支持正面证据、Books 或无遗漏断言，也不支持性能/安全保证。恢复后只定点重开对应源的本窗事件，不重扫历史。

- **G1 — Google publications 日级归属。** 首批 15 条以出版年排序且含未来年份；普通模型主题 query 原入口及有限替代不能访问。缺的是该窗口公开/重要修订的模型系统条目与原始时刻；可接受官方可读 dated research feed、论文页首次公开记录或归属明确的作者公告。恢复位置为 `research.google/pubs/` 对该窗口的主题切片，不以 `2026` 年标签或会议年份猜日。
- **G2 — Meta Research/Publications。** Research 空正文、Publications 不可达，博客页与官方域补检未恢复本窗论文目录。缺该窗口的模型架构/训练原始公告及日期；可接受官方 dated publication export 或完整研究事件页，先恢复窗口条目再判断贡献，不把旧博客分页扩为历年筛选。
- **G3 — Qwen 新 Blog/Research。** 新站空正文，旧站与组织首批只能提供有限替代。缺新站本窗相关发布列表/首公开日；可接受官方可读 feed、带日期的技术公告或原始报告，不用文档翻译提交代替研究公告。
- **G4 — DeepSeek 新闻/模型公告入口。** 原更新入口及中英文有限替代不可达；harness release 已有独立确定性证据，仍不能据此恢复官网全部模型事件。缺本窗模型/训练/推理公告及公开时刻；可接受官方 dated release feed/模型卡发布记录，恢复只影响这部分覆盖，不重复审阅已关闭的 harness 家族。
- **G5 — Kimi Platform Blog。** 原博客有限尝试均超时，组织当前首批与官方域补检不能补全。缺本窗长上下文/模型/Agent 原始文章列表及日期；可接受官方 dated blog feed、对应原文缓存或作者正式发布记录。仅重开该窗口，不把组织 last updated 当首公开。
- **G6 — Hunyuan Research“全部”。** reader 空正文、有限替代不可达、浏览器 30 秒超时/reset；官方组织首批与相关官方发布补检不能替代完整动态目录。缺该窗口语言/多模态/生成/后训练/效率条目；可接受可读“全部”导出、官方 dated research feed 或具体官方论文发布记录。不得从这次访问失败推出零命中。
- **G7 — Z.ai Research。** 中英文研究入口不可达，release notes/组织首批/具体 Law 核心只能有限恢复。缺本窗相关论文事件和首公开日；可接受官方可读目录导出或 dated 原始技术报告。AutoClaw Law 已因具体贡献不足关闭，无须为其不影响处置的日期另开请求；不采用页面法规/个案真实性结论。
- **G8 — MiMo Blog 索引日级日期。** 主页其余未标日链接没有形成可证明的本窗列表；已恢复的 9/27 repetition 和 #2603 不代表 15 个链接全量归属。缺能限定到本窗的 dated 博客列表，而不是要求逐篇读全部旧文。可接受官方 dated feed/公告；恢复窗口线索后才读具体核心，不把未标日标题凑成候选。

**不属于本窗：** MiMo tool-call repetition 的当前官方日期为 2026-09-27，仅记录真实归属，不移动到发现日，也不在本日启动 9/27 补跑。arXiv 10/5 公告批次属于其他日期，本日未为其中宽列表建立候选库存。

## 6. 复核

复核者：root（非作者）。

结论：通过

作者为 oct04_daily；本记录由 root 实际完成报告写后复核后更新。

已完成的独立准入校准：root 实际重开 DeepSeek release 完整核心、OpenAgentCore 精确配置/路由和 MiMo PR 核心及 refresh/spec 必要内容；认可上述窄版本贡献与仅报告处置。代表排除项 AutoClaw Law 的完整官方核心经 root 独校，排除理由是数据库/GLM 分工、四个演示和引用/人工复核建议没有新的检索、权限或可比较评价机制，不是“法律题名即范围外”。这不等于报告全量写后验收，也不包含未恢复目录的语义复核。

总复核覆盖全部 3 个准入家族的日期、评分、必要原源与仅报告理由；实际读了 MiniMax 密钥/HTTP 安全 patch、三版本入口配置，以及 MiMo stale-owner/异步 sampling 与刷新 admission 的受影响 patch，未把 smoke-test 改动说成授权漏洞修复，也未把 busy/pending 写成后台排队。对 14 行查询与停止范围、8 项外部保留条件逐行核对；代表性非候选抽检为 AutoClaw Law 的完整核心、Seed 未标日条目的 8/5 官方日期、arXiv 公告日期及窗外批次。未逐项重读全部旧条目、普通提交和不可达目录，故不宣称全量无遗漏。Books 实际写入 0；仅报告是完成 Books 判断后的处置，不是省略 Integration 流程。

机器校验：`python3 scripts/validate_research.py --report papers/2026/10/04/README.md` 已通过 V3 schema/consistency 检查；目标范围 `git diff --check` 无错误；引用的本地文件均存在，9 个 JSON 原始记录均可解析。只确认格式/可判定一致性，不替代语义复核。未 stage、commit 或 push；只写本日 README 与本日 `_sources`。
