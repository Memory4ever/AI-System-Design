# 中国六个每日官方源 — 2026-10-02

窗口：`[2026-10-01T09:00:00+08:00, 2026-10-02T09:00:00+08:00)`。本记录独立从原始入口发现，不继承旧月份候选或结论；仅归属此文件，不修改 Report、Books、Learning State。实际检查约 `2026-10-02T09:00～09:31+08:00`，以下时间字段保留原值和精度，不将页面日期补成发布时间。使用来源注册表每日切片；没有扫描 Weekly 组。网页/公开 API 读取是静态来源核验，不是运行或复现实验。

## 漏斗与当前交接

六个源有限发现已到停点。MiniMax Code `v0.6.0` 的安全拒绝分类/重试修正、OpenAgentCore `v0.0.3/0.0.4`带入的CI权限约束放宽经独立初校为2个局部安全变化家族；本窗普通诊断/分发变化不另成候选。没有把跨年度目录、仓库更新时间或 API 的提交时间计为本窗研究家族。

## 来源覆盖与停点

| 来源 | 实际入口、范围和停点 | 本窗结果 | 限制 |
| --- | --- | --- | --- |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) 首查，web 提取超时，curl 公共 HTML → 官方 JS → 公开 `publicList` API，`renderType=0` 全部，zh/en 各 Page 1、pageSize=20：zh `totalNum=11` 返回 11，en `totalNum=9` 返回 9，目录已穷尽。补 [Tencent-Hunyuan](https://github.com/Tencent-Hunyuan) 首屏10仓库、[T1](https://github.com/Tencent/llm.hunyuan.T1) README，未遍历 commits | 目录所有 `publicAt/updatedAt/publishedAt/displayPublishTime` 均窗外；无本窗候选 | web 首查超时已由真实 API 恢复，不把 shell 当零命中。仅声明此公开目录及有限仓库入口处理完成 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research) “全部、时间排序”最新首屏，读至 `2025/12/09` 的 15 项/查看更多前；补[官方 releases](https://docs.z.ai/release-notes/new-released)最新至旧日期、[zai-org](https://github.com/zai-org)首屏 | Research 最新原日期 `2026/08/26`，release 最新 `2026-08-26`，无本窗命中 | 不点查看更多考古；仓库更新时间不作研究发布日期。仅已访问目录范围的结论 |
| SRC-BYTEDANCE-SEED | [Publications](https://seed.bytedance.com/en/public_papers) `Newest → oldest` Page 1，`1-20 of 242`、`Page 1 of 13`，读至 May 14 2026 后停；[Research/Blog](https://seed.bytedance.com/en/research) 首屏5博客，首位缺日期故进入 SeedRealtime 原页；补[ByteDance-Seed](https://github.com/ByteDance-Seed)最新10仓库 | Publications 最新 `Aug 18, 2026`；首位 SeedRealtime 原日期 `2026-08-05`；无本窗研究 | 未扫描13页历史论文；AI for Science 明确标题只作范围外线索，不构成逐项队列 |
| SRC-BAIDU-ERNIE | [中文 Blog](https://ernie.baidu.com/blog/zh/) Page 1，10篇至2025/11/21，见下一页2/2后按日期停止；[ERNIE](https://github.com/PaddlePaddle/ERNIE)官方 README 的最新更新及 release 栏 | Blog 最新原日期 `2026年5月9日`；README更新均旧，未发现本窗候选 | 不按2.4T/榜单/成本数字收录；不扩扫 Paddle 库 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/) Paper 8条、Blog首屏15条；从公共 bundle恢复首位无日期文章路径；[复读诊断原页](https://mimo.xiaomi.com/blog/mimo-v2-6-tool-call-repetition)、[V2.6 iframe原文](https://mimo.xiaomi.com/mimo-v2-6/article)、[MiMo Code iframe](https://mimo.xiaomi.com/coder/index.html?lang=en)、[XiaomiMiMo](https://github.com/XiaomiMiMo)最新10仓库 | 最新Paper原日期 `June 29, 2026`；最新复读博客 `September 27, 2026`，V2.6 `September 22nd, 2026`，本窗未确认新增研究 | 首页其他无日期产品/能力页不视为本窗事件；MiMo Code landing无日期、未给本窗机制改变依据，仅保留日期未核实，不据此宣称站内零遗漏 |
| SRC-MINIMAX | [en Blog](https://www.minimax.io/blog)12项、[中文 Blog](https://www.minimaxi.com/blog)重定向[minimax.cn](https://www.minimax.cn/blog)13项；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)→公开 [llms.txt](https://agent.minimax.io/docs/llms.txt)→唯一 Agent Team 正文；[MiniMax-AI](https://github.com/MiniMax-AI)首屏10库，定点 releases/必要commit | Blog最新日期 `2026-08-13`；本窗 OpenAgentCore0.0.3/0.0.4、minimax-code0.6.0/0.6.1。Code0.6.0局部安全修正和OpenCore CI权限放宽经初校准入；普通分发/诊断变化不独立准入 | Agent Team正文无明确date，与Blog中旧Agent Team家族名称关联不能作为日期证明，安全隔离。2家族Report/Books接受交root |

## Hunyuan 全部目录真实恢复

首查 HTML 的主脚本：`https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-I3I3bCf9.js`。主脚本真实 `Ji()` 将站域映射为 `https://api.hunyuan.tencent.com`，Research `/blog` 动态块为 `index-CUQAWQeM.js`；该块调用 `index-cEoitnb7.js` 中公开读取接口 `/api/blog/publicList`，不是猜测 URL。调用：

```text
POST https://api.hunyuan.tencent.com/api/blog/publicList
Content-Type: application/json
accept-language: zh   （再以 en/default核语言目录）
{"pageNum":1,"pageSize":20,"renderType":0}
code=0; zh totalNum=11/list length=11; en totalNum=9/list length=9
```

API 返回文章正文及目录字段，但只核日期与本窗身份，不把窗外正文送去深审。signed图片链接、用户名等无关返回字段不保存。本日窗口 UTC 为 `[2026-10-01T01:00:00Z,2026-10-02T01:00:00Z)`；Epoch秒原字段经UTC+08转换。zh全列表原值：

| 原目录身份/标题 | publicAt | updatedAt | publishedAt | displayPublishTime | 处置 |
| --- | ---: | ---: | ---: | ---: | --- |
| 100119 Hy Image3.5 preview 发布 | 1790053389 | 1790053389 | 1789959110 | 1790006400 | 最新publicAt=`2026-09-22T13:03:09+08:00`，窗外 |
| 100116 Batch Size Scaling | 1790049600 | 1790049600 | 1789749798 | 1790006400 | publicAt=`2026-09-22T12:00:00+08:00`，窗外 |
| 100100 Hy4 preview 发布 | 1787896858 | 1787984179 | 1787896648 | 1787846400 | 窗外 |
| 100091 From LR to ELR | 1787231078 | 1786592588 | 1786592588 | 1786377600 | 窗外 |
| 100087 Hyra: 简单有效的科学发现智能体 | 1784563048 | 1784563048 | 1784110327 | 1784599200 | 窗外；不从科学应用回引候选 |
| 100064 Hy3 正式发布 | 1783348867 | 1783348867 | 1782959528 | 1783320600 | 窗外 |
| 100041 Hy-MT2 | 1779357326 | 1781525719 | 1779340747 | 1779346800 | 窗外 |
| 100039 Real life is where context gets hard | 1777554405 | 1777554405 | 1777228775 | 1777532400 | 窗外 |
| 100061 Hy3 preview | 1783244694 | 1776873600 | 1782308557 | 1776873600 | 字段并不相等/同序，均窗外，不把display反推首次公開 |
| 100015 Stabilizing RLVR | 1770971794 | 1770971794 | 1770971794 | 1770971794 | 窗外 |
| 100025 Learning from context is harder than we thought | 1770112929 | 1770092288 | 1770092288 | 1770092288 | 窗外 |

en额外检查全部9项，最新100116 `publicAt=1790150728`、`updatedAt=1790150728`（`2026-09-23T16:05:28+08:00`）、`publishedAt=1789707529`、`displayPublishTime=1790006400`；其余8项也均早于窗起点。没有本窗需进入原paper审阅的事件，不把列表新发现/收录等价为本窗首次公開。

## MiMo 无日期卡片恢复与范围关闭

官方公共 bundle `https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js` 的 routePath/frontmatter 保留 `mimo-v2-6-tool-call-repetition`、`date:"2026-09-27"`；原页显示 `September 27, 2026`，且明确 API 部署 `September 25 at 06:00 (UTC+8)`，均窗外。原核心：RL 的32调用阈值未处罚较低洪泛，严格阈值训练代价及泛化不足，以专门单轮RL教师经MOPD转移停止行为；不将当前访问日期当更新事件，也不在本日评分。V2.6 iframe文头 `September 22nd, 2026`，窗外。

“How Xiaomi MiMo-V2.6-Pro Boosts Productivity in New Materials R&D”卡片清楚是PFAS材料研发应用，按AI for Science暂缓在标题级排除；无日期不影响该贡献前关闭。MiMo Code landing核心是coding agent产品能力、工作流、安装/使用，未发现明确带日期的新机制或对照，不只因出现computation/memory/evolution词语而准入；本日不评分。其他更旧模型卡片只作有界线索，未将15卡片变为无日期全文队列。

## MiniMax 本窗事件、贡献前关闭与安全校准

GitHub组织首屏的`Updated Oct 1, 2026`触发定点release检查，不能本身证明发布。MSA API `pushed_at="2026-10-01T03:35:24Z"`，但default branch最新commit为`80434d7`，committer `2026-07-30T06:11:11Z`（CuTe-DSL API修复），并非本窗新机制；不把push timestamp入选。

### 本窗发布身份与普通变化（安全项另列，不整版排除）

| 材料 | 精确日期原值 | 核心语义与关闭理由 |
| --- | --- | --- |
| [OpenAgentCore v0.0.3](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.3) | `published_at="2026-10-01T08:30:10Z"`＝16:30:10+08 | Linux amd64 distribution from commit `cc7e1aad3bde47598d161d6372e2e211bb61d9cd`；发布转GHCR，分发通道不单独证明新Agent机制；tag包含的CI权限放宽另列安全家族 |
| [OpenAgentCore v0.0.4](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.4) | `published_at="2026-10-01T09:10:13Z"`＝17:10:13+08 | Linux amd64 distribution from `03fe9a4e7eb0ba29375d04672808956290356cd6`；同runner构建并行传输是普通release工程；包含同一CI权限放宽，不增加家族数 |
| [MiniMax Code v0.6.1](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.6.1) | `published_at="2026-10-01T14:22:09Z"`＝22:22:09+08 | `ef2f43d3d1b3c0cd29f5a0a3f8eef738f7535e44`核心允许side `/btw`对话中的`/doctor`、`/feedback`，不改变parent/side Session，`/quit`仍禁；局部诊断操作补齐，没有值得长期保留的新机制，贡献前关闭 |

release核心中的Linux/macOS离线CLI/BYOK验收、未做Windows/live-service、npm updater通道及安装条件只支持厂商披露的分发事实，本任务不运行安装，也不外推生产接受。公开release页未显示本项撤回/删除/勘误标识；不全站遍历安全历史。窗口前基线只用于必要delta：OpenAgentCore v0.0.2 `2026-09-30T06:59:16Z`；Code v0.5.10 `2026-09-30T08:55:18Z`，均窗外，不继承旧日报结论。

### MiniMax Code v0.6.0：校准后准入的局部安全边界修正

[release v0.6.0](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.6.0)，API原 `published_at="2026-10-01T13:56:17Z"`，北京时间 `2026-10-01T21:56:17+08:00`，落窗。[精确commit](https://github.com/MiniMax-AI/minimax-code/commit/9150441bfbd81d7f59ac88d222878c3a532f34a4)为 `9150441bfbd81d7f59ac88d222878c3a532f34a4`（committer `2026-10-01T13:45:11Z`；用于代码身份，不替代release日期）。当前页可读，未见撤回/纠错标记。

准入理由：**BYOK为兼容异常网关采用所有pre-output错误可重试的旧策略 → 新增provider safety refusal的确定性终止分类，且其解释正文不再被误解析为网络/状态码 → 必须重新考虑把错误可重试性与文本启发式混为一体的恢复选择。** 这不是仅主题相关或版本标签；修正可具体落到安全拒绝覆盖“retry all”的例外和不可信解释文本边界。

初判断曾想以成熟拒绝原则的局部补齐关闭；独立 `oct02_review` 于本日打开精确commit后纠正：实际错误分类/安全终止约束修正应准入，局部结果也可改变重要边界。保留此改判理由，不因深审投入而缩池。root已获消息。评分仅为交接建议 `1 + 1 + 2 = 4`（局部实现改动、单Agent runtime/adapter、可复用终止分类约束）；安全信号无论分数都要求受影响内容深入核验及Books判断，不用评分反推拒绝。

已定点读取的证据（同commit patches）：

- `third_party/pi-mono/packages/ai/src/providers/anthropic.ts`：在message_delta遇`stop_reason=refusal`保存可选category/explanation，生成含稳定`stop_reason: refusal`token的错误；未给出的`stop_details`只作可选字符串，不据此声称SDK已正式支持。
- `packages/shared/src/llm-error-classifier.ts`：先用`PROVIDER_REFUSAL_MESSAGE_RE`识别稳定token；添加`refusal`与`content_filter`后提前返回，不让provider-controlled explanation进入status/network启发式；metric与retry decision统一终态；`classifyLLMErrorToCode`对拒绝返回null。
- `packages/agent-core/src/pi-turn-runner/llm-retry.ts`：BYOK `retryAllErrors`分支增加`!normalized.facts.signals.has('refusal')`，防绕过普通non-retry decision。
- `packages/agent-core/test/unit/pi-turn-runner/llm-retry.test.ts`：两个provider身份注入带`stop_reason: refusal`、`see 500 {"x":1}`的解释，静态断言`attempts=1`、无retry observer、final outcome error/content_filter；不是本任务运行的测试证据。另一组TLS record错误在throw/stream、visible output前允许2次并恢复；visible output后只1次并返回error。不能把这条扩成全部证书错误可retry。
- compaction受影响core：`llm.ts`中无尾部real user的continuation采用`tail`，保存durable replacement，避免retry反复放弃已完成compaction；本日候选只采用refusal边界，不扩为所有Goal/TUI/模型默认值变化。

可支持：公开artifact实现与测试断言确实区分确定性拒绝、文本误导和可恢复传输错误；不能支持全部厂商/自定义网关都正确归类、不会再billing、安全拒绝质量、攻击抵抗、生产零重复效果。只核公开精确diff，未安装、运行测试或复现实验。拟owner须由Report作者选择唯一节点：`AGENT-PLATFORM`(Ch84)的恢复/终止contract，或`PLATFORM-SECURITY`(Ch72)的不可信文本与策略结果分类；此文件不宣称已有覆盖或Books完成。

### OpenAgentCore CI 权限变化：校准后准入，精确tag证据支持落窗

[精确commit c4402c6](https://github.com/MiniMax-AI/OpenAgentCore/commit/c4402c60cab2b5e7791c18f77154523670c66926)，committer原 `2026-10-01T05:06:04Z`，对应本窗实现变更，但commit时间不是发布artifact首次公开证明。为安全校准读 `.github/workflows/ci-review.yml`，不审整库：

- 旧版限定Bash子命令、Read/Grep/Glob，network及不可执行代码边界；新版设置`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=0`供子进程读GH token和飞书webhook，开放Write/Edit/WebFetch/WebSearch，去除strict MCP/setting-source限制。
- 原core将事件限定`workflow_run.event == 'push'`且`head_branch == 'main'`；“main已合入即可信”是代码注释里的原作者假设，不作为本报告安全证明。未公开对恶意仓库内容、CI日志、子进程秘密泄露的对照或失败评价。
- 必要当前变化检查 [d865b6b](https://github.com/MiniMax-AI/OpenAgentCore/commit/d865b6bc5388647e170bc0042ce72d51a4b2a441) `2026-10-01T06:31:23Z`只改通知prompt/轮数，并未在patch恢复权限隔离；不声称此状态永远保留。

初倾向“普通CI通知开放权限，没有提供新的长期机制/安全证据”关闭；`oct02_review`独立读取c4402完整workflow纠正：真实运行安全约束放宽不能以无安全评价关闭，评价缺失用于限定可采用范围而非贡献倒推。因此改为局部安全约束改变家族。准入链：**旧CI Agent通过工具/网络约束及子进程secret scrub限制观察与动作 → 新版关闭scrub并扩工具可写与外网访问 → operator必须重新考虑将main已合入内容作为可信基础的凭证暴露/执行边界。** 只支持“公开版本约束放宽”，不支持发生泄露、越权写GitHub或该选择安全。

落窗证据追加：

- `GET https://api.github.com/repos/MiniMax-AI/OpenAgentCore/compare/c4402c60cab2b5e7791c18f77154523670c66926...cc7e1aad3bde47598d161d6372e2e211bb61d9cd?per_page=1`：原 `status="ahead"`、`ahead_by=19`、`behind_by=0`、`merge_base_commit.sha=c4402c60cab2b5e7791c18f77154523670c66926`；只读取祖先字段，不再扩history。
- [v0.0.3精确workflow](https://github.com/MiniMax-AI/OpenAgentCore/blob/v0.0.3/.github/workflows/ci-review.yml)与[v0.0.4精确workflow](https://github.com/MiniMax-AI/OpenAgentCore/blob/v0.0.4/.github/workflows/ci-review.yml)通过GitHub contents API实际读取：11～14行token仍`contents/actions/pull-requests:read`；18行main push触发；24行`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB:'0'`；29行checkout触发的head_sha；31行`persist-credentials:false`；78行开放Bash/Read/Write/Edit/Glob/Grep/WebFetch/WebSearch。
- 故对应release `published_at`已经证明本窗发布版本的源配置包含该约束变化，无需补造commitfirstpush；不把初始提交时间当首次公開，也不声称Linux发行包在用户运行时执行此CI workflow。

`oct02_review`独立建议评分 `1 + 1 + 1 = 3`，仅该CI Agent权限策略的局部版本事实，安全变化须深入受影响workflow；已静态核全部相关触发/凭证权限/工具参数，未实际执行CI或调用token。Books由root判断（建议仅报告版本事实；若长期论点改变再选`PLATFORM-SECURITY`唯一owner），不得从源码约束变化推导攻击已发生或生产无泄露。一次release比较返回112commits、files capped300，只作为有界线索，其余不形成队列，也不在本文件计为已审。

## 精确未决与隔离

可执行交接：2个MiniMax家族的Report评分/Books owner具体论点对照和独立接受。`oct02_review`已完成安全准入校准，MiniMax Code采取确定性拒绝终态边界，OpenCore采取约束放宽版本事实；以上不谎称Report/Books完成。

外部保留项：MiMo Code landing及MiniMax Agent Team Tech Blog未给明确发表日期/重要修订日期；当前没有可支持的本窗身份，不纳入正面证据、评分或Books，不支撑站内零遗漏。重开只需相应官方原页的明确date或公开announcement/精确版本事件，不能用导航索引时间、发现时间、git org更新时间替代；不据此无限追历史。Agent Team正文已读到运行时state/Verifier/context成本核心，描述Leader/Worker/Verifier和producing/verifying/done，但没有本窗增量身份，暂不移入候选。

校验：本文件Markdown/链接目标结构已检查，`git diff --check -- papers/2026/10/_sources/daily-20261002/CHINA.md`无输出通过；该文件是新untracked文件，已另实际读取修正范围，git检查不替代独立语义接受。只写本文件；不stage/commit/push。
