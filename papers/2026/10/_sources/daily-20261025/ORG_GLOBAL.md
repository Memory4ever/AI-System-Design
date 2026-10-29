# 2026-10-25 Live Daily：全球机构来源

窗口：2026-10-24 ～ 2026-10-24（北京时间）。检查：2026-10-25 11:58～12:13 +08:00；执行者 `live1025_org_global`。仅 own 本文件。

已重读 AGENTS、Research/Report 合同、Research Sources 使用说明与 Daily 组、Prompt、ROADMAP 和本轮路由 checkpoint；未接历史六月任务。下列是有界入口检查，不是机构全网或全年逐项审计。目录中窗外条目不自动转成待审队列。搜索无结果、抽取空白均不作为零事件证明。

## 1. 来源入口、停止位置和结果

| ID | 实际入口及停止位置 | 结果 | 限制与重开点 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/) → [Research index](https://openai.com/research/index/) 最新首屏；见 10-23 training-environment security、10-21 biological-data agents、10-19 low-resource coding，止于已跨窗条目，不点 Load more。补查 `site:openai.com "October 24, 2026" research` 与 `site:openai.com/index/ after:2026-10-23 before:2026-10-25 -site:community.openai.com` 第一批结果。 | 已检查该有界入口；未发现确定本窗新候选。 | 搜索返回社区/帮助站噪声，未当研究正文；不证明隐藏更新或全网无遗漏。 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) Most recent 首段：10-23 AISI incident assessment → 10-20 protein binders → 10-16 economics/science → 10-13 source-control；止于明显早于窗口。日期查询 `site:anthropic.com "Oct 24, 2026" research` 和 `site:anthropic.com/research after:2026-10-23 before:2026-10-25`。 | 已检查该有界入口；未发现确定本窗新候选。 | 10-23安全项是窗外，不搬到10-24；仅目录识别，不冒充已深入审阅该文。 |
| SRC-GOOGLE-AI | [DeepMind Research](https://deepmind.google/research/) → [News](https://deepmind.google/blog/) 2026-10相关模型项，止于9月；[Google Research Blog](https://research.google/blog/) 第1页最新10-23，止于10-02；[Publications](https://research.google/pubs/) 仅定位1–15/11636及按年目录性质，不把全年变题摘队列。日期/主线查询见下文；EMNLP具名线索定点恢复。 | 已检查新闻/博客；论文目录为检索受限，未建立当窗全目录覆盖。确定新候选0。 | 年份/会议发表年并非首次公开日；新闻部分月份标签已定点恢复日期。重开需10-24相关官方公开事件或可按公开日检索的论文批次，不扩大到11636条。 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 抽取0行，改走[Blog](https://ai.meta.com/blog/)及其[Publications](https://ai.meta.com/results/?content_types%5B0%5D=publication)链接。Publications头部为10-20 retrieval-programming、10-19 on-device model，后为10-14科学应用及历史2019/2020混序，止于该混序信号。补检 `site:ai.meta.com "October 24, 2026"` 首批。 | 检索受限；替代入口未发现确定当窗候选。 | Blog可见最新7月，Publications混序，不能证明10-24零论文。Research主体或有日期过滤的官方相关列表恢复后定点重开；不遍历科学应用。 |
| SRC-QWEN | [旧博客](https://qwenlm.github.io/) 明示迁移至[新 Research](https://qwen.ai/research)；新Research与[Blog](https://qwen.ai/blog)均抽取0行。`iab`浏览器创建失败（Browser is not available）。改查[官方GitHub组织](https://github.com/QwenLM) Updated首10/60，识别10-24 qwen-code/docs，10-23 MM-Plugins，止于10-05及9月旧更新；只对qwen-code读[release](https://github.com/QwenLM/qwen-code/releases)及API前8条。 | Research/Blog受阻；GitHub替代部分已检查。1个版本事实家族通过具体兼容/安全边界准入，4分深入核读后仅报告，见§3。 | 无法用旧站2025内容或搜索空结果证明新站10-24无事件。新站可读原文/官方当日研究列表是定点恢复条件。 |
| SRC-DEEPSEEK | [主页](https://www.deepseek.com/) → [研究与动态](https://www.deepseek.com/news/) 最新动态9-10、研究索引6-24；主页10-17模型更新引至[官方更新日志](https://api-docs.deepseek.com/updates/)，最新10-17后9-10，止于跨窗。补查 `site:deepseek.com "2026-10-24"` 和 `site:api-docs.deepseek.com "2026/10"` 首批。 | 已检查该有界入口；未发现确定本窗新候选。 | 不从首页无更新推全GitHub无更新；无具体研究线索不扫描全部仓库/普通PR。 |
| SRC-MOONSHOT | [平台Blog](https://platform.kimi.com/blog)最新2025-11-07，不能单独代表2026；[官方组织](https://github.com/MoonshotAI) Updated首10/42，10-24 kimi-code，10-22 checkpoint-engine，10-12 MoonEP后旧项；定点[代码release](https://github.com/MoonshotAI/kimi-code/releases)最新2.3.1为10-23，读Patch Changes及资产日期；止于旧版本。补查 `site:moonshot.ai "October 24" "2026"` 和 `site:moonshot.ai "2026-10-24"`。 | 已检查公开Blog/GitHub有界入口；未发现确定本窗研究/机制新候选。 | 组织Updated只是活动，不等于release/论文公开；Blog滞后限制保留，不声称整个机构10-24零更新。 |

查询均读工具实际返回的第一批结果，没有未读分页被写成已读；未将空检索反推零。Google补检为 `site:research.google "October 24, 2026" model`、`site:deepmind.google "24 October 2026"`、`site:research.google "2026-10-24" ("language" OR "training" OR "inference" OR "agent")`、`site:deepmind.google "October 24, 2026" ("model" OR "research")`。Qwen补检为 `site:qwen.ai "2026-10-24"`、`site:qwen.ai (research OR blog) after:2026-10-23 before:2026-10-25`、`site:qwen.ai "2026" "October" research`。停止于这组窗口/主线查询，不向一般AI新闻扩池。

## 2. 日期、排除与轻量去重

- [Google at EMNLP 2026](https://research.google/conferences-and-events/google-at-emnlp-2026/)标10-24～29是会议日，不是31篇论文首次公开日。只恢复一条可能误收的主线线索[2605.12483](https://arxiv.org/abs/2605.12483)：完整题摘已读，原记录v1提交5-12、最新v5提交10-12，无10-24修订记录。因此不能因开会日在窗内重收，也不为会议页整31篇建新队列；不声称核遍全部论文首次公开日。
- DeepMind月份项定点原文日期：[Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)10-13、[安全说明](https://blog.google/innovation-and-ai/technology/safety-security/gemini-4-model-safety-security/)10-13、[Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/)10-13、[EmbeddingGemma 2](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2/)10-06。均窗外，不作本窗机制审阅或候选。
- Qwen release的[手动压缩PR15104](https://github.com/QwenLM/qwen-code/pull/15104)与[恢复PR15131](https://github.com/QwenLM/qwen-code/pull/15131)核心说明和风险/验证边界已定点读；精确查[10-23报告](../../23/README.md)§3/§4已有该家族审阅与Books结果。本次tag重新列出不是独立新机制，不重评分/再写Books。未用旧日报替代本轮source发现。
- Qwen [nightly 20261023](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.0-nightly.20261023.5a0be33432) API `published_at=2026-10-23T22:33:02Z`，BJT10-24；与本家族release重叠，不另计。前一nightly UTC10-22 22:30落BJT10-23，停止。Desktop-v0.26.1 UTC10-24 17:06:46落BJT10-25，属下一窗口，非本窗候选。
- Moonshot Kimi Code 2.3.1 GitHub release UTC10-23 07:31（资产同日），Patch Changes为工作区信任/崩溃锁恢复等维护；无本窗发布证据，组织Updated10-24不能替代。未扫描普通commit。
- 轻量notice检查限于已读目录、release breaking changes、PR核心及风险段；未发现需要把本文以外旧结论重新打开的撤回/安全公告。Qwen明确breaking scope变化已经核读，不因低分略过。未宣称遍历各机构全站notice。

## 3. 当窗候选：Qwen Code v0.26.1 的 QQ scope兼容边界

### 身份、准入与日期

官方[release v0.26.1](https://github.com/QwenLM/qwen-code/releases/tag/v0.26.1)，tag短SHA `b475278`；[release API](https://api.github.com/repos/QwenLM/qwen-code/releases/tags/v0.26.1)返回 id `422824160`、`published_at=2026-10-24T15:47:58Z`、`created_at=2026-10-24T15:34:10Z`、target `release/v0.26.1`。采用published_at，转BJT为10-24 23:47:58，日期落窗；created_at不替公开。网页只有24 Oct15:47不是唯一日期依据。

准入链：旧QQ部署把scope和本地channel认知混在一起 → [PR13882](https://github.com/QwenLM/qwen-code/pull/13882)在该release实际改变缺省scope和群审批权限边界 → 升级不能继续假设“默认每发送者私有、能发送就能批准工具”。这是具体兼容/安全事实，不把通用隔离、幂等或持久化原则包装成新理论。评分 `1 + 2 + 1 = 4`；root首批准入校准认可按该有限理由继续，不借通用原则提分。

### 实际核读与支持范围

已读release完整变更说明、PR13882的What/Why/Risk与Migration、[文档diff](https://github.com/QwenLM/qwen-code/pull/13882/files)相关QQ段；raw及blob访问失败后，以GitHub contents API的 `?ref=v0.26.1` 成功恢复精确tag文件（解码读取，不执行）：

- [QQ plugin](https://github.com/QwenLM/qwen-code/blob/v0.26.1/packages/channels/qqbot/src/index.ts)：声明 `defaultSessionScope: thread`。
- [config-utils](https://github.com/QwenLM/qwen-code/blob/v0.26.1/packages/cli/src/commands/channel/config-utils.ts) `effectiveSessionScope` L646–655：显式配置优先；否则multiSession选user，再取plugin default，最后user。因此“所有QQ无条件变thread”错误。
- [SessionRouter](https://github.com/QwenLM/qwen-code/blob/v0.26.1/packages/channels/base/src/SessionRouter.ts) L374–386：thread取channel加chat/thread，user保留sender和chat，single取channel全局key；支持同群共享/跨群分开的键域差异，不证明实际QQ云端端到端行为。
- [QQChannel](https://github.com/QwenLM/qwen-code/blob/v0.26.1/packages/channels/qqbot/src/QQChannel.ts) L598–657：不再静默强制scope，full-message与非thread组合只warn；共享scope启用群访问但operators空则warn无人可审批/控制。L4384–4389、4569起：purgeLegacySessions默认不删除，启用后先救援记录。默认值变化不是删除授权。
- [tag QQ文档](https://github.com/QwenLM/qwen-code/blob/v0.26.1/docs/users/features/channels/qqbot.md) Session Isolation：thread群内上下文共享，群控制/审批看operators，非allowedUsers；群场景要member_openid，DM user_openid不能混用。DM-only thread/user仍各自私有。

旧态仅采用PR Why的精确区分：构造器改的是自己的配置副本，并未同步已配置的router，所以“所有旧full-message都真实变成single”并不成立；真实跨群/DM全局共享需显式single。tag文档upgrade段仍有“此前forced single”的简化措辞，与PR Why不完全一致；本记录不据该措辞扩大旧漏洞范围。完整旧代码未作历史重演。

PR列出operators未设时审批pending可能占用session直至300s timeout，且真实QQ凭据端到端未跑CI；300s是作者描述，不是本轮测量。代码只核了上述相关调用/分支；未复现、未运行测试，不把PR测试数量当本轮实验，也不对所有channels作安全保证。没有benchmark主张，硬件/吞吐/质量协议不适用。

### 处置

4分版本事实，相关安全/兼容影响域深入核读后关闭；Books建议“仅报告”。Owner路由为 `AGENT-PLATFORM`（Ch84）及权限交接 `PLATFORM-SECURITY`（Ch72），不据主题相似声称“已有覆盖”，也未修改Books。该事件不能支持新通用隔离原则或性能结论；是否存在具体旧Books断言冲突由报告作者核，当前未提出需要改书的冲突。

## 4. 收束与外部保留

本文件确认1个当窗家族（Qwen Code release）需报告，已给限定证据和仅报告建议；Google会议重呈现、Qwen既审PR/release重叠不增加家族。Google论文目录、Meta混序目录、Qwen新站主体的覆盖限制已隔离：不支持“7机构当日零新增/无遗漏”、Books采用或安全保证。可接受替代是对应机构10-24原始日期列表/公告或本次具名材料的官方原文，不要求无限查历史。

本文件无未完成的必要正文审阅；整体Daily是否完成、独立语义复核及Books决定归root。没有改Report、Books、State、索引、脚本或Git暂存状态。
