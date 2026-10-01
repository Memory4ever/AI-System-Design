# Daily 2026-09-21 screening ledger

## 口径与窗口（09/21机构侧原快照，不是当前全日分母）

本文件保留原机构侧有效身份/单篇证据。原 arXiv ‘周末无公告/raw 0’推断已被官方 Mon21 批次与公告时钟反证，不能复用为当前覆盖结论。当前十二类 New/Cross 475 去重身份及有界主题/题摘处理见 [官方题名恢复](./arxiv-mon21-titles.md)、[当前题摘判断](./arxiv-title-abstract-screening.md)及[唯一证据/处置](./arxiv-evidence-restoration.md)；历史 Replacement 原清单与12748公开日期仍精确隔离，不支持零遗漏。正式全日分母以 [Daily 六部分](../../21/README.md)最终冻结为准。

- 窗口：`[2026-09-20T09:00:00+08:00, 2026-09-21T09:00:00+08:00)`。
- 检查时间：`2026-09-21T09:40:00+08:00`。
- Daily 发现面为 `docs/RESEARCH_SOURCES.md` 的 14 个每日来源；未触发额外按需来源。
- 机构仓库只补充明确 research artifact、release/RFC/model/system card，或实际改变 correctness、security、interface contract 的重要事件。普通 commit/PR 活动不进入 raw denominator，也不逐 commit 建关闭记录。
- 论文按官方公开事件与版本去重，再以 title + 完整 abstract 筛选；原快照的‘本窗没有 arXiv 公告 identity’已失效，现以 Mon21 官方恢复为准。无 abstract 的 release/artifact 读取官方 README、完整 commit/release explanation 与直接相关 diff/tests。

## 漏斗闭包

| 层级 | 数量 | 说明 |
| --- | ---: | --- |
| raw identity | 9 | 5 个明确 artifact/release/open-source event + 4 个合并后的 MiMo Code contract family |
| 去重后唯一 Source Family | 9 | merge commit 与同机制 follow-up 不重复计数 |
| 通过贡献筛选 | 6 | Qwen-Image-2.1、RecreationWorld、MoonEP、三个仍可解析的 MiMo contract family |
| 已关闭 | 2 | ZCode open-source、MiniMax-Code-MiniApps initial artifact |
| 已撤回/删除 | 1 | MiMo provider prompt family；终审时官方 commit URL、main history 与 Git object 均不可解析 |
| Evidence 完成 | 6 | 深入 4，标准 2 |
| Books 整合 | 2 | Ch24、Ch36，均进入共享写回 queue |
| Existing Coverage | 4 | Ch66、Ch78/83/84 |
| Structural Candidate | 0 | 无 |

闭包为 `9 raw = 6 retained + 2 contribution closure + 1 deleted/withdrawn exclusion`。删除项只保留排除依据，不进入候选、评分、Evidence 或 Books；其恢复条件是官方重新发布可解析的 commit/release 与对应 diff/tests。

## Raw identities 与处置

| Source Family | 官方时间字段与窗口归属 | 原始说明 | 处置 |
| --- | --- | --- | --- |
| `SF-2026-09-21-QWEN-IMAGE-2.1` | 官方博客只给 `2026-09-20`；仓库 Atom 的 release-related artifact 从 `2026-09-20T02:25:10Z`（10:25:10+08）起，完全落入窗口 | Qwen-Image-2.1 模型、博客与代码 artifact | 保留；深入；7 分 |
| `SF-2026-09-21-RECREATIONWORLD` | `QwenLM/RecreationWorld@948e567` Atom `2026-09-20T09:50:10Z` = 17:50:10+08 | 首次公开跨平台 computer-use recreation/evaluation artifact | 保留；标准；6 分 |
| `SF-2026-09-21-MOONEP-2609` | `MoonshotAI/MoonEP@33327eb` Atom `2026-09-20T04:48:05Z` = 12:48:05+08 | `Public Release 26/09` | 保留；深入；9 分 |
| `SF-2026-09-21-ZCODE-OPEN-SOURCE` | 初始提交 `2026-09-20T12:06:58Z`，`feat: open source` `2026-09-20T21:14:32Z` = 09-21 05:14:32+08 | ZCode coding workbench 开源 | 关闭；产品/harness packaging，无独立机制证据或可比较 evaluation |
| `SF-2026-09-21-MINIMAX-CODE-MINIAPPS` | 初始官方仓库 commit `65a75bf` Atom `2026-09-20T07:53:24Z` = 15:53:24+08 | 官方 community repo；MiniApps 是 self-contained MiniMax plugins，手工安装 | 关闭；catalog/packaging artifact，未提供改变长期系统结论的机制与验证 |
| `SF-2026-09-21-MIMO-PROVIDER-PROMPT` | 作者阶段记录 `71d0cba` 12:28:50+08、`0fa4888` 12:56:58+08、`8a0b439` 13:53:34+08；终审时三者均不在官方 main history，代表 URL `8a0b4398…` 返回 404，Git object fetch 返回 `not our ref` | DashScope、SiliconFlow、Mistral adapters 保留 system prompts | 删除/撤回排除；不入候选、不评分、不作 Evidence/Books 判断 |
| `SF-2026-09-21-MIMO-MCP-HOST-STATE` | `e95db7a` 15:49:22+08、`db95b68` 16:25:52+08、`d1a72ba` 21:35:15+08 | host-owned admission、residual stale-state closure、in-flight presentation persistence | 保留；深入；8 分 |
| `SF-2026-09-21-MIMO-SESSION-STATE` | `05fa8d1` 16:02:21+08、`30e55a4` 19:49:32+08、`1592084` 23:52:40+08 | orphan tool-part terminalization、exclusive resume admission、bounded retry/error identity | 保留；深入；7 分 |
| `SF-2026-09-21-MIMO-SKILL-ROOTS` | `1a7a747` Atom `2026-09-20T08:58:32Z` = 16:58:32+08 | 默认 skill discovery roots、scan order 与 dotted namespace exclusion | 保留；标准；6 分 |

MiMo main feed 中其余 viewport、performance、artifact download、CI、issue labels 等普通活动均做来源级检查后停止，没有被扩成 raw identity。MiniMax Code 0.5.0 的 version bump/release packaging 同理不另建 raw family；本窗唯一保留的 MiniMax 原始事件是明确初始化的 MiniApps artifact，随后按贡献门槛关闭。

## 来源覆盖与停止点

| 来源 | 实际检查入口/停止点 | raw identity | 结果与边界 |
| --- | --- | ---: | --- |
| SRC-OPENAI | `openai.com/research` 官方目录可见最新卡片，停止于早于窗口的 09-10 发布 | 0 | 无当窗 scoped research event |
| SRC-ANTHROPIC | `anthropic.com/research` publications，停止于 09-17 最新可见条目 | 0 | 无当窗 scoped event |
| SRC-GOOGLE-AI | DeepMind publications 最新可见 09-01；Google Research 官方目录做窗口日期定点查询 | 0 | 未见当窗 dated scoped card；动态目录不支持绝对零断言 |
| SRC-META-AI | Meta AI/FAIR Research 最新可见条目，停止于 09-07 | 0 | 无当窗 scoped event |
| SRC-QWEN | `qwen.ai/blog`、Qwen-Image-2.1 与 RecreationWorld 官方仓库/feed | 2 | 两项保留；博客日级时间限制单独记录 |
| SRC-DEEPSEEK | 官方 Research/News 最新项 | 0 | 未见当窗 research/release/card |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 明确 release；MoonEP master Atom | 1 | 保留 public release `33327eb` |
| SRC-TENCENT-HUNYUAN | Hunyuan Research 与明确 release/RFC/contract event | 0 | UniRL 普通 main activity 不扩 denominator |
| SRC-ZAI | 官方 Research/release 与 `zai-org/ZCode` initial/open-source activity | 1 | open-source event 记录后按贡献门槛关闭 |
| SRC-BYTEDANCE-SEED | Seed Research/papers 与明确发布 artifact；EdgeBench/VeOmni 定点核对 | 0 | EdgeBench 指向旧论文、VeOmni 为普通活动；来源级关闭 |
| SRC-BAIDU-ERNIE | ERNIE 官方技术博客与明确发布 artifact | 0 | 无当窗 scoped event |
| SRC-XIAOMI-MIMO | MiMo Paper/Blog；MiMo-Code main Atom 只抽取 contract-level events | 4 | 三个合并 family 保留；provider prompt family 因官方提交已删除而排除；普通 commits 不扩池 |
| SRC-MINIMAX | Research/Blog、MiniMax-Code-MiniApps repo/feed 与明确 release | 1 | MiniApps initial artifact 记录后关闭；普通 minimax-code activity 不扩池 |
| SRC-ARXIV | 原快照十二分类 recent 可见 `Fri, 18 Sep 2026`；该水位不是本窗无公告证明 | 原0失效 | Mon21于09/21 08:00北京时间公开，New/Cross475身份已恢复；当前处理与外部 Replacement限制见上方链接 |

## arXiv 水位（原快照，仅保留反证前读到的页面）

| 分类 | 最新官方 recent header | 页面可见计数 |
| --- | --- | ---: |
| cs.CL | Fri, 18 Sep 2026 | first 50 of 104 |
| cs.LG | Fri, 18 Sep 2026 | first 50 of 198 |
| cs.DC | Fri, 18 Sep 2026 | 25 |
| cs.AI | Fri, 18 Sep 2026 | first 50 of 215 |
| cs.CV | Fri, 18 Sep 2026 | first 50 of 125 |
| cs.RO | Fri, 18 Sep 2026 | first 50 of 133 |
| cs.AR | Fri, 18 Sep 2026 | 13 |
| cs.PL | Fri, 18 Sep 2026 | 11 |
| cs.OS | Fri, 18 Sep 2026 | 1 |
| cs.PF | Fri, 18 Sep 2026 | 13 |
| cs.IR | Fri, 18 Sep 2026 | 22 |
| cs.MA | Fri, 18 Sep 2026 | 17 |

这些仅是原快照的可见页面水位，不是窗口 raw identity 数量，也不能推导周末无新批次。后来恢复的 Mon21 公告已推翻该推断；原表保留用于说明纠错，而非当前 Coverage 通过依据。

## 跨日去重

- 09-20 Daily 的两个 UniRL Source Family（`07ac948`、`a77575a`）公开时刻均早于本窗口起点，未重复纳入。
- 09-19 Daily 的 MiMo session lifecycle（`2bda179`、`50cd713`）拥有 abort cascade/subagent recovery；本窗的 session family处理 exclusive admission、orphan terminalization 与 bounded retry，identity 和语义增量不同。
- Qwen-Image-2.1 的日级博客日期不单独再计一个 identity；博客、README 与 release-related repo activity 合并为同一 Source Family。
- MiMo 的 merge commits 与其 underlying/follow-up commits 按一个长期机制 family 去重；provider prompt family 的删除处置不改变其 raw identity，只清除采用链路。

## 审计交接

fresh non-author reviewer 已复核：`9 = 6 retained + 2 closure + 1 deleted/withdrawn exclusion`；Qwen 博客日期与仓库时刻的窄窗口声明；RecreationWorld 首次公开 identity；MoonEP release SHA；三个保留 MiMo family 的合并边界；ZCode/MiniApps 候选前关闭理由；UniRL 两项仅作为前一日 identity 去重；以及 Ch24/Ch36 两项 Books Integration 的唯一 owner。唯一实质修正是清除已删除 MiMo provider prompt family 的候选、评分、Evidence 与 Books 链路。
