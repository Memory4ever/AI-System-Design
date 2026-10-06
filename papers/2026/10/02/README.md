# Daily Research — 2026-10-02

**规范：** V3
**窗口：** 2026-10-01T09:00:00+08:00 ～ 2026-10-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T09:34:38+08:00

## 1. 结论

本次有两个确定落窗的材料家族，均来自 MiniMax 官方公开工程源：一个修正模型安全拒绝被自动重试的边界，一个放宽 CI Agent 的执行环境。前者已在第84章的状态机论证中补齐拒绝、暂态错误与输出提交点的区别；后者只记录版本化配置事实，不推断实际泄露或防护效果。

两个家族的受影响内容均深入审阅（安全变化不因低分免审），1项整合、1项仅报告。原始目录和旧公告只作发现线索，不计成当日论文数量；OpenAI两项落窗新闻及Anthropic领域科研稿已读核心说明并贡献前关闭。本窗未建立确定 arXiv 候选，原因是主题接口受限、替代目录仍显示旧批次，**不是确认本日没有相关论文**。Google、Meta、Qwen等有限来源缺口在§5隔离，不支持无遗漏断言。没有扫描每周组、创建本周Weekly或启动旧历史cursor。

## 2. 来源覆盖

检查于北京时间09:00后执行，实际查询与原始字段见[全球来源](../_sources/daily-20261002/GLOBAL.md)、[中国来源](../_sources/daily-20261002/CHINA.md)、[arXiv停点](../_sources/daily-20261002/ARXIV.md)。以下范围不是全站逐篇验收。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research Index](https://openai.com/research/index/)首屏9项；[News RSS](https://openai.com/news/rss.xml)头12项，核至首个早于窗起点项；两项本窗core | 已检查 | 不声称Research Index覆盖全部新闻或机构所有研究 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)首屏10项，最新Oct1→Sep30；Oct1科研稿core | 已检查 | 该稿时区/时刻未披露，不影响范围排除 |
| SRC-GOOGLE-AI | [DeepMind publications](https://deepmind.google/research/publications/)近期部分与[Blog](https://deepmind.google/blog/)首屏；[Research pubs](https://research.google/pubs/)1–15/11569、[Blog](https://research.google/blog/)首屏12项；Argon原日期定点去重 | 受阻 | pubs正式发表年份不能定位本窗首公开；日期入口恢复受限 |
| SRC-META-AI | [Blog](https://ai.meta.com/blog/)第1页、真实[Publications结果](https://ai.meta.com/results/?content_types%5B0%5D=publication)第1页前12近年项；之后混旧年份，未点Next | 受阻 | Research主入口无可读正文，结果排序不能证明日期覆盖 |
| SRC-QWEN | [旧首页](https://qwenlm.github.io/)官方迁移→[Research](https://qwen.ai/research)动态壳；一次公开asset恢复、两次浏览器超时后停止 | 受阻 | 未取得本窗研究列表、日期和core，不以空响应记零命中 |
| SRC-DEEPSEEK | [研究与动态](https://www.deepseek.com/news/)动态5项/研究10项；最新V4.1 Flash原日期Sep10，部署Sep14，均窗外 | 已检查 | 限于该公开目录，不重审旧机制/性能 |
| SRC-MOONSHOT | [Platform Blog](https://platform.kimi.com/blog)可见22项；[组织](https://github.com/MoonshotAI)首屏10/42仓库按Updated，首位Sep30后更旧，停止 | 已检查 | Updated仅定位线索，不等首公开；不逐PR扫描全组织 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)真实publicList，renderType=0/page1/pageSize20，zh11/11、en9/9已穷尽；官方组织/T1首屏 | 已检查 | 首查超时已由API恢复；不把窗外正文送入深审 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)全部/时间排序首屏15项至2025/12/09；[release](https://docs.z.ai/release-notes/new-released)和组织首屏；最新Aug26 | 已检查 | 在旧日期停，不扩历史查看更多 |
| SRC-BYTEDANCE-SEED | [Publications](https://seed.bytedance.com/en/public_papers)Newest→oldest，Page1的1–20/242至May14；[Research](https://seed.bytedance.com/en/research)5博客与SeedRealtime原页（Aug5） | 已检查 | 未遍历13页旧论文，范围外领域科研不扩池 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)第1页10篇，最新May9；[ERNIE README](https://github.com/PaddlePaddle/ERNIE)更新/release栏 | 已检查 | 不扩Paddle其他仓库；旧榜单数字不重归本日 |
| SRC-XIAOMI-MIMO | [首页](https://mimo.xiaomi.com/)Paper8/Blog15；最新无日期卡片恢复原页Sep27，V2.6 iframe Sep22，Code landing及组织首屏 | 已检查 | Code landing无日期，隔离；没有据此确认站内零研究 |
| SRC-MINIMAX | [en Blog](https://www.minimax.io/blog)12项、中文Blog13项；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)公开llms.txt→Agent Team；组织首屏10库触发4个release精确core/安全定点 | 已检查 | Agent Team正文日期不明，隔离；普通版本不扩为整库审计 |
| SRC-ARXIV | 四主题API start0/max20、Submitted发现缓冲202609301800～202610011800；CL/DC/LG/CV new与CL/DC/LG recent旧批次边界；有限AI/AR/RO替代及辅助搜索 | 受阻 | 429/timeout/替代失败；可读目录仍Thursday Oct1，不能冒充本窗公告 |

## 3. 候选与判断

本窗按唯一家族计数。Code0.6.1的诊断补齐不另加家族；OpenAgentCore0.0.3/0.0.4共同记录配置发布演进，不计两项贡献。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [MiniMax Code v0.6.0](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.6.0) | 2026-10-01T21:56:17+08:00 | BYOK宽重试需排除安全拒绝，拒绝说明不得污染状态码分类；1 + 1 + 2 = 4 | 深入完成 | 整合：`AGENT-PLATFORM`，[Ch84状态机](../../../../books/part-07-agent/84-agent-platform.md#agent-runtime-state-machine) |
| [OpenAgentCore v0.0.3（含v0.0.4同窗演进）](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.3) | 2026-10-01T16:30:10+08:00 | 版本化CI Agent放宽工具/环境秘密边界，不能用main合入代替运行隔离；1 + 1 + 1 = 3 | 深入完成 | 仅报告：具体配置事实，无新增防护机制或已测安全结果 |

## 4. 证据与知识整合

### [MiniMax Code v0.6.0](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.6.0)

Release API原字段 `published_at="2026-10-01T13:56:17Z"`，绑定[精确commit 9150441](https://github.com/MiniMax-AI/minimax-code/commit/9150441bfbd81d7f59ac88d222878c3a532f34a4)；代码提交时刻只作artifact身份，不替代公开事件。初校曾拟按普通局部修复关闭，独立复核指出这是实际拒绝/恢复边界纠错，已改判保留。

关键证据是 `llm-error-classifier.ts` 的拒绝优先返回、`llm-retry.ts` 中BYOK retry-all拒绝例外，以及对应单测：拒绝说明含500仍只一次尝试并归content_filter；TLS record错误在输出前可恢复、可见输出后不透明重放。只深入这些受影响路径，不遍历35文件无关变化。证据是公开实现及测试断言，**本任务未运行测试或验证真实服务**，不证明所有provider分类正确、零重复计费或安全拒绝质量。没有性能数字；模型、硬件、精度、长度、batch、并发与SLO不是这项静态路径判断的评价对象，真实负载验证Not Disclosed。

现有Ch84解释run状态与可恢复transition，但该位置尚未明确拒绝覆盖重试兜底和输出提交点。已在“Agent Runtime State Machine”的transition说明后、Observation节前融入两段：调用失败≠继续许可；拒绝≠整个任务终态；错误语义及部分输出影响恢复选择。保留暂态重试的成立条件、adapter维护成本、未知信号停止/人工fallback；唯一owner是`AGENT-PLATFORM`，未在Security章重复写机制。非作者实际写后复核已通过，不是仅登记“已吸收”。

### [OpenAgentCore v0.0.3（含v0.0.4同窗演进）](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.3)

Release原字段 `published_at="2026-10-01T08:30:10Z"`、[后续v0.0.4](https://github.com/MiniMax-AI/OpenAgentCore/releases/tag/v0.0.4)为`09:10:13Z`。两tag内的[workflow](https://github.com/MiniMax-AI/OpenAgentCore/blob/v0.0.3/.github/workflows/ci-review.yml)实际含c4402变化，因此使用本窗release里的版本化源状态；不把commit时间当首次push，也不声称Linux分发包会运行该CI。

定点读取精确workflow：main push/core-check完成触发、固定head_sha、checkout不保存credentials、GitHub token仍read scope；但子进程环境scrub关闭并扩大工具集合，原提示/网络限制被撤除。这是具体边界变化，不能因普通分发标签跳过。源码可证明配置，不能证明执行中秘密确实泄露、模型被注入或已获得GitHub写权限。没有对照安全评价和真实执行trace，不推定此策略安全或不安全的发生率。仅报告这个发布事实，不用单项配置变化为书稿制造新安全定律。

## 5. 缺口与下一步

本窗普通可执行扫描、候选审阅、Books与独立复核待办为0。以下是**外部终态保留项**，不算Coverage/Evidence通过，不支持正面证据、Books采用或无遗漏断言；不能据此判断“没有重要论文”。各项定点重开条件如下：

- **arXiv本窗公告批次**：[主题API](https://export.arxiv.org/api/query)、[CL目录](https://arxiv.org/list/cs.CL/new)等失败或仍显示旧批次。需要2026-10-02官方公告切片/可用Atom及相关完整题摘，才能完成本窗主题发现与落窗核验。官方目录/接口恢复或用户提供该批次导出即可；只重开本窗四主题及相关标题补检，不扫旧日库存。
- **Qwen动态Research**：[官方入口](https://qwen.ai/research)仅取得壳，有限浏览器恢复超时。需要可读公开列表、相关日期与核心原文；官方feed/API或保存该列表HTML可替代。只重开本窗切片。
- **Google Research pubs首公开定位**：[默认目录](https://research.google/pubs/)只有出版年份，不能确定本窗；需要本窗主题的首次公开排序/日期过滤结果，或具体原论文及作者公告。已有Blog/DeepMind切片不受影响，不重跑全部年份。
- **Meta研究目录时间定位**：[Publications结果](https://ai.meta.com/results/?content_types%5B0%5D=publication)混旧年份且未核完整排序。需要带可验证首公开字段的本窗结果或具体材料；可读官方列表/导出可替代。只恢复受影响条目。
- **无日期官方材料**：[MiMo Code landing](https://mimo.xiaomi.com/coder/index.html?lang=en)、[MiniMax Agent Team](https://agent.minimax.io/docs/techblog)：必要公开/重要修改日期未披露。当前不当作确定本窗家族；官方带时间公告或精确事件可恢复身份后再判断，不以发现日期补造时刻。

以上不要求用户提供整个机构历史数据。当前无已识别候选必要正文缺失；以后材料恢复只重开对应保留项。

## 6. 复核

复核者：oct02_review（独立非作者智能体）；root对全球贡献前排除做非作者定点初校。

结论：通过

已实际完成两安全项准入校准：纠正把Code拒绝修复按普通版本排除、把OpenAgentCore配置放宽按无新机制跳过的理由；因此两个家族均定点深入。全部2/2候选的精确日期、必要原core与受限结论已核，Code的Ch84两段及邻接、Ch83交接非作者写后通过。

独立复核完整读取正式六部分及三份本日来源记录、14来源停止与五组隔离限制。普通负侧原源分层抽检4项：OpenAI观点、零售采用两core，Anthropic暂缓科学应用，Code0.6.1诊断补齐；另定点核安全/修改信号Argon 1项的current core与原datePublished/dateModified，不能由元数据变化推出重要修订。arXiv独立只核旧批次头；其他明确窗外目录只核记录与停止边界，没有声称全部题摘或全站原文复核。

完成态V3、四份新增Markdown的本地引用/围栏/空白及限定diff检查通过，脚本不代替上述语义判断。本轮Books实际增量仅Ch84两段，未改旧章节结论。既有March/Books/进度的staged与其他工作树修改均保留；本轮没有stage、commit或push。周五不生成Weekly，最新历史checkpoint已完成，不恢复旧cursor。
