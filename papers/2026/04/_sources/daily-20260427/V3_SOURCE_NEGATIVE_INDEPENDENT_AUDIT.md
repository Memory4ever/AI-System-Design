# 2026-04-27 V3 来源、日期与否定侧有限独立审计

复核者：`apr27_source_gate_audit`（非日报作者）；2026-09-28。范围仅为日报 V3 的日期链、14 个到期来源的已记录入口/停点及分层否定样本；不是整日 Coverage/Evidence/Books Gate，也未重跑 14 个网站或复现实验。实际读取了当前 `AGENTS.md`、三份研究/来源/报告合同、`CODEX_RESEARCH_PROMPT.md`、`ROADMAP.md`、[日报 §2](../../27/README.md#2-来源覆盖)、[来源发现记录](V3_SOURCE_DISCOVERY.md)、[筛选记录](V3_SCREENING_NOTES.md)、04/27 与 04/28 原始 owner receipt 及本日 OAI cs XML；另独立打开下列 arXiv 原始页面与少量实际 Books 段落。先写审计结论，不改日报或书稿。

## 1. 日期链：有界推断 PASS，不能升级为逐篇确证

[arXiv 官方可用性/公告规则](https://info.arxiv.org/help/availability.html)明确：提交和公告分开，最终 arXiv ID 在公告过程赋予，正常 Thursday 14:00–Friday 14:00 ET 提交于 Sunday 20:00 ET 公告，且存在延期可能。2026-04-26 为周日且纽约为 EDT（UTC−4）；正常 Sunday 20:00 ET = 2026-04-27 00:00Z = 北京时间 04/27 08:00，落在本日报 `[04/26 09:00, 04/27 09:00)`。这只是常规时刻，不能据 submitted 字段反推公开。

具名复核：[SSG `2604.22438v1`](https://arxiv.org/abs/2604.22438v1) 原始 submission history 是 `2026-04-24T10:55:50Z`；04/27 owner receipt 的 `v1_updated=2026-04-27T00:34:20Z`、`DataCite initial_created=2026-04-27T01:37:27Z` 与本日 OAI `datestamp=2026-04-27` 各有不同语义。[ArmSSL `2604.22550v1`](https://arxiv.org/abs/2604.22550v1) 分别为 submitted `04/24T13:40:25Z`、v1_updated `04/27T00:40:48Z`、DataCite created `04/27T01:40:14Z`、OAI `04/27`。04/27 receipt 中相邻 `22436/22439/22442` 与 `22549/22551` 同批更新/DOI 序列，04/28 receipt 从 `2604.22754` 开始（其 [arXiv abs](https://arxiv.org/abs/2604.22754v1) 甚至显示 02/19 提交，而 04/28 receipt 才有 ID 对应更新）。这些组合支持两项按正常 04/27 08:00–09:00 BJT 公告批次的**有据推断**，不能证明每篇独立 first-public 时刻；尤其 DataCite 01:37/01:40Z 已晚于本窗 01:00Z 终点，绝不可单独用作落窗证明。若取得官方逐篇公告/延期记录与此相反，只重开受影响 ID 的日期与日报归属。当前日报的范围写法和推断说明合格；不要再把范围缩成无证据的精确时刻。

## 2. 14 源实际停点：入口审阅通过，Coverage Gate 未通过

下面审的是[正式 §2](../../27/README.md#2-来源覆盖)与[原始停点](V3_SOURCE_DISCOVERY.md)是否相称，不是重新访问每个历史目录。额外现开 Google Research 2026/04 官方博客，确见 04/22→04/29；现开 Anthropic Research 的普通网页只露 09 月首屏，**不能**用这次首屏替代原记录中 `publishedOn` 的 04/22→04/29 历史邻界。Qwen 与 MiniMax 两个 GitHub release 页面亦只作发布身份抽检，秒级 `published_at` 复用原 API 收据，未假称本次重验全部分页。

| ID | 已记录的可核入口与停点 | 本次边界判断 |
| --- | --- | --- |
| `SRC-OPENAI` | News RSS `pubDate` 与 Symphony/Choco/原则文章具名；Research 直开 403 | RSS 阳性处理可复用；Research 历史目录 403 可具名隔离，但不能称无研究。 |
| `SRC-ANTHROPIC` | Research `publishedOn` 04/22→04/29 | 原记录给相邻停点；本次未独立再现历史列表，仅可复用、不可扩成全站阴性。 |
| `SRC-GOOGLE-AI` | Research Blog 04/22→04/29、DeepMind 韩国合作自然日 | 博客负例可信；Google Research/DeepMind Publications 仍无历史停点，不能替代为论文目录已查。 |
| `SRC-META-AI` | Research/Blog 已开、Blog 04/08→06/29 | Research 分页未到本窗；首屏负例不够。 |
| `SRC-QWEN` | 研究 API 40/60 条邻界；qwen-code 单项分页 p335–339，两个本窗 release | 研究列表与该 repo release 层可复用；组织其它已触发仓库/重要发布仍是限定范围待查，非组织阴性。 |
| `SRC-DEEPSEEK` | News 04/24→09/10、Research 02/25→06/24 | 两个公开目录具名停点成立；PDF 内印 04/27 不能制造新的公开事件。 |
| `SRC-MOONSHOT` | Kimi Blog 静态首页仅见 2025；kimi-cli release 04/24→04/28 | CLI 具名阴性成立；博客没有 2026 停点，不能说整个来源已闭。 |
| `SRC-TENCENT-HUNYUAN` | Research `publicList` 9/9、04/23→04/30；T1 repo releases 空 | Research 子入口完成；注册表还列 Tencent-Hunyuan 组织，T1 单 repo 不等于组织历史发布已检查，正式整行 `已检查` 需收窄或补停点。 |
| `SRC-ZAI` | Research 04/07→04/29、release notes 04/07→06/16、GLM-5/4.5 releases 0 | 两目录与两 repo 成立；其它已触发 repo/无 tag 重要变化仍缺可复核范围。 |
| `SRC-BYTEDANCE-SEED` | Publications 242 页20 05/12→04/08；Blog 95 首页 04/22→04/08；四具名 repo releases | 目录停点成立；四个 repo 不能概括 ByteDance-Seed 组织。 |
| `SRC-BAIDU-ERNIE` | 官方中文 Blog 04/15→04/30、注册表指定 ERNIE repo release 2025 单项 | 指定两入口可记 `已检查`，不能外推其它论文/提交。 |
| `SRC-XIAOMI-MIMO` | Paper 03/13→06/29；Blog 卡片无时刻；两具名 repo releases 0 | Paper 与两 repo 有边界；Blog/组织其它重要发布仍未到历史停点。 |
| `SRC-MINIMAX` | 英文/中文 Blog、Agent Tech Blog 定点 Agent Team 窗外；CLI v1.0.12 本窗 | CLI 阳性已具名关闭；中文历史 Blog、Agent Blog 与组织其它重要发布未有完整本窗停点。中英 Agent Team 日期冲突均不落本窗，不为它虚造精确首发。 |
| `SRC-ARXIV` | 339 DataCite 身份 + 69 OAI 差集 = 408 宽线索；相邻 ID 04/28 从 22754 开始 | 日期链可用，但 OAI 包含修订，408 非候选分母；负侧分层复核未闭，正式 `未完成` 正确。 |

正式表当前 4 行 `已检查`、9 行 `受阻`、1 行 `未完成`。关键修正不是把所有 9 行删去，而是按 Report 合同区分：已有原站 403/历史目录不可取得且穷尽可用入口的**精确子入口隔离**，与尚可通过注册表入口、有界分页或具名主线仓库继续做的**普通可执行补查**。当前记录明说“其余未闭子入口继续检查”，因此不能把 9 个 `受阻` 一揽子当作终态保留项，也不能让 Tencent 的整行 `已检查` 覆盖未查组织入口。若作者已穷尽某子入口，应在 §2/§5 写出具体尝试、可接受的替代原始目录和重开条件；否则保留 `未完成` 并继续有界补查。无需扫描每家组织全部仓库或逐 PR。

## 3. 否定侧分层抽样：两项已恢复；其余样本只给有限结论

选择原则是跨来源/主题/共享关闭理由取最可能漏掉纠错、安全或设计反证的样本，不按关键词机械抽。独立打开 exact-v1 arXiv abs 的完整题摘：`22438/22550`（旧同一泛化关闭理由）、`22220/22335`（watermark 邻域）、`22085`（Agent memory 系统 headline）、`22452/22446`（多 Agent 负面/形式保证）、`22597`（评价纠错）及正向控制 `21964`（安全评议）；其中还读了 `22085` HTML §IV-B/§V-E、`22446` HTML §2.2.3–2.2.4/保证段、`22597` HTML §3/§4.2，以及 Ch72 watermark、Ch76 条件解码/答案 gate、Ch77 写入与表示、Ch82 topology、Ch81 workflow、Ch66 reference/matcher 相关现文。**只覆盖 9 个具名 ID（8 个否定侧/恢复 + 1 正向控制），绝非 408 项全量语义验收。**

| 样本 | 读到的关键信号与有限裁决 |
| --- | --- |
| [`22438v1` SSG](https://arxiv.org/abs/2604.22438v1)、[`22550v1` ArmSSL](https://arxiv.org/abs/2604.22550v1) | exact-v1 题摘直接给出低熵 token 概率质量/注入强度、以及盗用 SSL encoder 经下游黑盒接口的归属与 OOD 密簇攻击；旧 receipt 同一句“局部优化无 state/data/control”不对题。作者已恢复为工作候选是必要修正；本审计不代替两项标准/深入证据及 Books 写后。 |
| [`22220v1` FMDiffWA](https://arxiv.org/abs/2604.22220v1) | 题摘是扩散图像的频域水印移除与保真取舍，属安全/攻击信号，不能仅凭“CV”关掉；但 Ch72 已把 embedded signal 遭变换失效与签名/原始记录分权。当前有限抽检未见改变主线决策的额外条件，具名前关闭可维持；若全文给出跨生成链的不同保护失效条件，定点重开。 |
| [`22335v1` CFB](https://arxiv.org/abs/2604.22335v1) | 题摘明确有/无 context 分布差、attention/语义支持的 token logit bias，不是纯格式修补；但所测 summarization/QA 的 faithfulness operating point 不给 token boost 事实授权，Ch76 已有条件 token 分支与 answer gate。只核题摘与现章，维持有限前关闭；若受控实验改变现有回退/授权选择再重开。 |
| [`22085v1` Memanto](https://arxiv.org/html/2604.22085v1) | §IV-B 主要逐级改 k、prompt、reader；§V-E 自认会话 benchmark、非会话 Agent 未测。它是主线内系统研究，不能以“厂商”或“已有 Ch77”硬拒；但上述对照不足以把 vector-only 普适替代 graph 升为长期原则，当前有具体缺口的前关闭可维持。若出现同 reader/候选/成本匹配的 graph 对照并改变 Ch77 选择，再重开。 |
| [`22452v1` Superminds](https://arxiv.org/abs/2604.22452v1) | 题摘确有“数量不能自然产生群智”的负例，但对象是 MoltBook 浅交互，未分离 topology/任务匹配/参与机会；Ch82 已要求这些独立分母。维持有限前关闭，不把 2M 用户当协作机会分母。 |
| [`22446v1` OMC](https://arxiv.org/html/2604.22446v1) | 原文自称动态任务树终止/无死锁；§2.2.4 同时允许 `failed/blocked`、budget `pause` 并设 deadlock detector，不能把宣称升级为无条件活性保证。Ch81 已有 task state/effect/retry/terminal 分权；前关闭可维持，但若后续给出动态扩图上界及失败/暂停状态的完整证明，须重开保证部分。 |
| [`22597v1` math judge](https://arxiv.org/html/2604.22597v1) | §3 先独立解题再审 dataset GT，§4.2 的 640 人工标注回答揭露 symbolic matcher 错误，不能轻率叫 formatter；Ch66 已分 reference coverage、semantic matcher、parser identity 与人工复核。现有证据只支持数学域裁决实现，前关闭可维持；若它证明现有分层在匹配样本上不足，重开。 |
| [`21964v1` safety-case review](https://arxiv.org/abs/2604.21964v1) | 题摘明确外部评议发现原 safety case scope/决策适用性的实质疑点；它虽在 cs.CY 且无新模型架构，保留候选符合反证准入口径。作为正向控制，没有发现“领域窄即排”的错误。 |

此次抽样足以确认旧**泛化“局部方法/无 ownership”理由**系统性不可靠：同理由命中的水印家族至少已漏 `22438/22550`。作者已定点恢复这两项，但这不证明其它共享该理由的 408 宽线索都安全。应仅复查该共享理由中标题/题摘涉及模型来源、检测、纠错、安全、关键设计反例的受影响部分；先完整题摘，必要时再查 exact-v1 正文与真实 owner。不同范围/理由且已核的独立结果可复用，不扩成 408 篇全文队列。所有拟入选项及有纠错/安全/设计反证/重要修订信号的排除项仍须由日级非作者覆盖；本文件不能代替 root 的整日签署。

## 结论与重开条件

**日期组合推断 PASS；来源 Coverage 和否定侧整日 Gate 未通过。** 要求作者把 §2 的“受阻”逐子入口与普通待查分清，并为 Tencent 组织入口、Google/Meta publications、Moonshot/MiniMax 历史 blog、Qwen/ZAI/Seed/MiMo 已触发的具名重要仓库等留下能执行的有限停点或真正终态隔离；不能以新仓库创建零结果或某一 repo Releases 空数组替代整个组织。负侧须对同一错误关闭理由做有界扩查与独立校准，记录实际样本/未查范围。待来源处理、候选分母冻结、必要 Books 真实写入及非作者整日报告复核后，才可由 root 判 `完成`。本审计没有对 37 项正式分母或 Books Gate 签字。
