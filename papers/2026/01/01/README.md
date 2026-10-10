# Daily Research — 2026-01-01

**规范：** V3
**窗口：** 2025-12-31T09:00:00+08:00 ～ 2026-01-01T09:00:00+08:00
**窗口说明：** 用户授权只补遗漏；保留原窗口、已有候选及其日期归属、评分与有效审阅。
**补充窗口：** 2025-12-31 ～ 2025-12-31
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T13:29:21+08:00

## 1. 结论

2026-10-07 增量补查已处理 14 个每日来源的有限原始切片和停止点：新增候选 0、有效同事件去重 1、重评分 0、Books 写入 0。[补查依据](../_sources/daily-20260101/supplement-20261007.md)区分实时调用与原字段复用。DeepSeek 官方研究索引明确标 mHC 公开日期为 2025-12-31，解除旧时区/时刻请求；该 exact-v1 已在 [01-02](../02/README.md)有效审阅并融入 Ch17，保留原候选归属，不重复计分或制造书稿产出。以下原窗口记录保留；本轮剩余具体限制见 §5，不表示全年补查已完成。

本窗没有已确认落窗、可采用的长期知识增量；不修改 Books。这个结论不是“所有来源无重要进展”：机构历史目录和 arXiv 修订公开事件仍有已隔离限制。

[arXiv 官方跨年公告](https://blog.arxiv.org/2025/11/21/temporary-changes-to-announcement-schedule-due-to-end-of-year-holidays-2025/)明确取消美国东部时间 12 月 30 日的公告，并把下一批新投稿公开推迟到 12 月 31 日 20:00 EST，即北京时间 1 月 1 日 09:00，恰为本窗不含的终点。因此本窗常规新投稿首次公告为零；这不证明作者镜像或已有论文的修订也为零。

实际检查每日 14 个来源入口及有界日期补检；没有扫描每周来源。定点读完 12 个 arXiv 家族的完整 v1 题摘，识别具体潜在贡献，但首次 arXiv 公告落在窗前或不早于终点，未作为本窗候选；mHC 目录日期、作者更早正文与两项修订事件的日期问题另行隔离。另有 2 篇应用论文、Qwen-Image-2512 和 Kimi CLI 0.70 在贡献前关闭。正式当窗候选 0、完成证据审阅的当窗家族 0、Books 写入 0；上述题摘阅读不冒称全文证据审阅。原始缓冲查询有重叠且不对应公开日期，不用原始命中数当漏斗分母。查询、停止点与初筛见[过程记录](../_sources/daily-20260101/screening.md)。

## 2. 来源覆盖

共同补检：各机构在官方域名下查询 2025-12-31 / 2026-01-01 的日期表达，只检查第一批搜索结果，未分页；搜索可能忽略域名和日期，社区帖、其他日期与普通产品介绍不作研究事件。精确查询保留在[日期补检](../_sources/daily-20260101/final-date-queries.md)。必要历史目录不可恢复均记录“受阻”，不是覆盖通过。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)首屏后独立恢复[官方 RSS](https://openai.com/news/rss.xml)，只解析日期定位本窗：1243 条 metadata 中 UTC 2025-12-31T01:00～2026-01-01T01:00 命中 0；邻接 Dec22 00:00 GMT→Jan2 10:00 GMT，未读全年正文。[日期切片](../_sources/daily-20260101/institution-date-recovery.jsonl)。 | 已检查 | 仅当前官方 feed 保存的事件；不保证已删除/未列事件或全机构无遗漏。 |
| SRC-ANTHROPIC | 独立恢复[官方 Research](https://www.anthropic.com/research) HTML 中 publishedOn，174 个日期字段只定位本窗邻接：2025-12-19T19:45:00Z bloom→2026-01-08T00:00:00Z critical-infrastructure-defense，无本窗日期记录；没有遍历旧文全文。[原字段切片](../_sources/daily-20260101/institution-date-recovery.jsonl)。 | 已检查 | 限官方页面现存目录，非已删除历史文章或全机构完整性保证。 |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/)与[Google Research](https://research.google/pubs/)当前入口/出版目录首屏及本窗日期补检；未遍历通用科学论文。原记录 [0](../_sources/daily-20260101/official-entry-0.txt)。 | 受阻 | 当前目录未恢复目标历史切片；不能称全站无相关事件。 |
| SRC-META-AI | [FAIR Research](https://ai.meta.com/research/)正文抽取为空；官方域日期补检，无可确认事件。原记录 [1](../_sources/daily-20260101/official-entry-1.txt)。 | 受阻 | 历史 Research 列表不可恢复；不把空抽取当零论文。 |
| SRC-QWEN | 旧博客与 Qwen-Image-2512 card 原记录保留，card 的具体贡献前关闭复用。本轮 root 直接读取[官方 research-list API](https://qwen.ai/api/page_config?code=research.research-list)返回的 60 个研究 metadata，按实际 date 字段定位 Dec31，无该日期项，止于此原始目录；[本次原响应](../_sources/daily-20260104/supplement-20261007/qwen.raw)。 | 已检查 | 只授此目录切片，不宣称所有机构历史事件均在其中；不再请求秒级时间。 |
| SRC-DEEPSEEK | 本轮实际重开[官方 News](https://www.deepseek.com/news/)研究索引 10 项，Jan12 Engram→Dec31 mHC→Dec2 V3.2；exact-v1 与 Jan02 已采用命题定点去重核验，见[补查依据](../_sources/daily-20260101/supplement-20261007.md)。 | 已检查 | mHC 公开日期已核；同事件已有有效审阅，不重复入选。不由目录枚举推断全机构无遗漏。 |
| SRC-MOONSHOT | [平台 Blog](https://platform.kimi.com/blog)实际可见 26 个日期条目，最新 2025-11-07/06、至 2024 年 5 月，无可见下一页；补检到官方 [CLI CHANGELOG](https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/CHANGELOG.md)只读 Dec29→Dec31 v0.70→Jan4 相邻版本核心。原记录 [2](../_sources/daily-20260101/official-entry-2.txt)、[初筛](../_sources/daily-20260101/screening.md)。 | 已检查 | 所见 Blog 列表与定点 CLI 版本已处置；不宣称组织全部仓库/作者镜像无遗漏。 |
| SRC-TENCENT-HUNYUAN | 原浏览器记录保留；本轮 root 核官方 publicList API（pageNum=1/pageSize=100/renderType=0），code=0、totalNum=9、list=9，逐条日期 metadata 最早为 2026-02-03，止完整当前公开列表；[本次原响应](../_sources/daily-20260104/supplement-20261007/hunyuan.raw)。 | 已检查 | 仅授当前目录的目标日期切片，不证明隐藏/删除事件不存在，也不为这种穷尽性保证索取历史档案。 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)当前首段 14 项，包含 Jan19 GLM4.7-Flash、Jan13 多模态、Dec10 GLM-TTS、Dec9 GLM-ASR，停于查看更多；本窗日期补检。原记录 [2](../_sources/daily-20260101/official-entry-2.txt)。 | 受阻 | 可见时间桥接但未恢复历史完整目录；不将查看更多之外视为读完。 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)与[论文目录](https://seed.bytedance.com/en/public_papers)之后恢复官方 API。2025/type1、2 倒序 token0、20；2026/type1、2 正序 token0，分别已越过本窗两端，见[字段原记录](../_sources/daily-20260101/seed-api-date-slice.jsonl)。2025 最新论文 Dec15、博客 Dec24；2026 最早论文 Jan20、博客 Feb12。 | 已检查 | API 的 PublishDate 是目录日期标签，不伪装真实首公开秒级时刻；结论仅为恢复目录无本窗条目，非作者镜像无遗漏。 |
| SRC-BAIDU-ERNIE | [中文 Blog](https://ernie.baidu.com/blog/zh/)当前可见日期从 2026-05-09 到 2025-12-23/09；官方域日期补检返回 Jan8、Jan15、Feb6 等窗外文章，停于该结果批。原记录 [3](../_sources/daily-20260101/official-entry-3.txt)、[补检](../_sources/daily-20260101/final-date-queries.md)。 | 受阻 | 当前列表不能证明目标日历史全部事件；未扩扫旧文全文。 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)论文 8 标题，Jan8 2026 MiMo-V2-Flash report→Oct21 2025 router-RL；博客 15 标题多无日期；本窗日期补检。原记录 [4](../_sources/daily-20260101/official-entry-4.txt)。 | 受阻 | 无日期博客和历史变更无法归窗；不把 paper 日期桥接推广至所有博客。 |
| SRC-MINIMAX | [英文 Blog](https://www.minimax.io/blog)可见列表从 2026 年 8 月到 Jan27、Dec23 2025 M2.1、Oct27 M2；[中文入口](https://www.minimaxi.com/blog)重定向 minimax.cn/blog；本窗日期补检为空。原记录 [4](../_sources/daily-20260101/official-entry-4.txt)。 | 受阻 | 未恢复全历史分页；空补检不证明目标日无研究。 |
| SRC-ARXIV | 依 ROADMAP 主线检查学习/后训练、长上下文、训练推理系统/kernel、多模态/World Model/VLA、RAG/Agent 主题；四个 Submitted 缓冲查询 start0/max150，均未满页；仅定点题摘初筛，不建全分类队列。长格式月份小段标题只作身份补检；实际假期公告证明本窗新投稿首次公告零。[日期依据](../_sources/daily-20260101/arxiv-holiday-date.md)、[查询/初筛](../_sources/daily-20260101/screening.md)。 | 受阻 | 新稿批次已确定，但 catchup 历史替换/修订公告不可恢复，TTT-E2E v2、KernelEvolve v2 的公开事件及潜在更早作者正文未确认；不把 Submitted/Updated 当 public。 |

按需来源未触发；定点采用作者模型卡、官方 CLI 日志、DataCite 身份字段只为具体材料恢复，不增加固定扫描任务。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无已确认落窗的正式候选，不评分，也不把不确定日期的材料放入候选表。12 个题摘所揭示的潜在增量与精确版本逐项保留在[初筛记录](../_sources/daily-20260101/screening.md)；日期归属与贡献判断分开。

## 4. 证据与知识整合

本轮 mHC 是日期限制解除与有效研究复用，不是新实验结论：`MODEL-TRANSFORMER-LAYER` [Ch17「多流混合还要保留哪些几何约束」](../../../../books/part-02-model/17-transformer-layer.md#多流混合还要保留哪些几何约束)已经具体解释 read/carry/write、双随机 carry 对均匀方向/流均值的守恒、差异方向可收缩、完整 Jacobian 与局部 carry 的区别，以及有限 Sinkhorn/I/O 代价。正文和 exact-v1 Review notes 实际可核，本轮 No Change；不重算 Jan02 的原评分，也不把目录日期当 arXiv 公告时刻。

本次采用的确定结论是公开事件边界，依据为具体假期公告，而不是当前星期表：冬季 EST=UTC−05，Dec30 20:00 是本窗起点，Dec31 20:00 是排除的终点。官方公告只约束新投稿公开与邮件，不扩大到所有 revision 或作者站点。[原始公告与推导](../_sources/daily-20260101/arxiv-holiday-date.md)保留恢复入口。

对 mHC、iCLP、RISE、原子技能泛化诊断以及 Trellis、Yggdrasil、Infini-Attention、TTT-E2E、LiveTalk、DreamTacVLA、AKG、KernelEvolve，已先确认具体潜在增量并独立校准，不因负面结果、小模型或推荐负载删除贡献。AKG 在准入事实含糊时补读 v1 HTML §3.2.1 Unified Sketch、§3.2.3 数值校验、§3.2.4 错误路由及 §3.6 动态形状/评测漏洞；这只解决“是否有具体机制”，不代表性能与跨后端可迁移性证据已经审阅完成。KernelEvolve 的作者 correctness 数字仅能指其选定测试集，不证明任意输入正确。

本窗没有采用上述技术命题，没有借“章节相关”声称已有覆盖；Books 为 No Change。没有进入书稿的正文、评分或性能保证。后续真归属日取得日期及必要核心证据后，才按 ROADMAP 唯一 owner 作具体 Books 差异判断。

## 5. 缺口与下一步

无尚未处理的可执行工作；非作者终审已通过。以下仅为本窗终态保留项，取得明确的新原始材料时按所列位置定点重开。

已隔离的本窗外部终态保留项，不支持正面证据、Books 或无遗漏断言，不支撑候选、Coverage 无遗漏或 Evidence 通过：

- 机构历史目录：SRC-GOOGLE-AI、META-AI、QWEN、TENCENT-HUNYUAN、ZAI、BAIDU-ERNIE、XIAOMI-MIMO、MINIMAX 的限制分别在覆盖表列明。恢复条件为其官方有日期的历史目录/批次，或明确落于本窗且披露机制的原始文章。只重开对应机构本窗切片；不扫描全年。
- 修订事件：[TTT-E2E 2512.23675v2](https://arxiv.org/abs/2512.23675v2)、[KernelEvolve 2512.23236v2](https://arxiv.org/abs/2512.23236v2) 的 Submitted/Updated 不能证明实际 public 时间。需要具体版本的公告/公开记录或可核实作者 first-public 说明，且显示本窗实质修订；当前仅隔离日期，不将版本号当重要修订，不把元数据 Jan1 更新反推此前没有正文。定点重开其版本与受影响命题，不重跑全部论文。
- 更早作者正文：除下述 mHC 外，初筛记录中其余 11 个可能相关家族的首次 arXiv 归属不等于作者镜像首次公开。已采用当前原页和有限官方域检索，没有可验证的本窗首公开正文；若提供明确时区/区间的作者原稿发布记录，只重开对应家族。当前不把这类未知记成“本窗零命中”。

- mHC 原时区/时刻请求已解除：本轮采用 DeepSeek 官方公开日期，定点关联 Jan02 exact-v1 已完成审阅及实际书稿覆盖，不再索要其秒级公开记录，不移动原候选。Qwen/Hunyuan 也已恢复当前有限目录，不再要求证明全机构无隐藏历史。其余具名机构入口及两项 revision 的必要公开日期仍按[补查记录的具体限制](../_sources/daily-20260101/supplement-20261007.md)隔离；没有具名线索的所有先行镜像不形成穷尽性请求。旧原始证据不删除。

窗外路由，不阻塞本窗：[iCLP](https://arxiv.org/abs/2512.24014v1)、[RISE](https://arxiv.org/abs/2512.23988v1)、[Generalization](https://arxiv.org/abs/2512.24063v1)、[Trellis](https://arxiv.org/abs/2512.23852v1)、[Yggdrasil](https://arxiv.org/abs/2512.23858v1)、[Infini-Attention](https://arxiv.org/abs/2512.23862v1)、[DreamTacVLA](https://arxiv.org/abs/2512.23864v1) 的首次 arXiv 公告不早于 2026-01-01T09:00+08，即应由 Jan02 或更后窗口核实际公告/更早作者原文后处理；这里仅转交身份和已校准准入理由，未声称相邻日已完成。TTT-E2E、LiveTalk、AKG、KernelEvolve 的 v1 arXiv 身份/DOI已在 Dec30 注册，结合 ID 首公告分配规则仅可界定其 arXiv v1 在窗前；不以 Registered 字段冒充公开时刻。没有依赖旧 Report 候选或评分。

## 6. 复核

本轮增量独立复核：root（非补查作者 supp_jan01）已通读 14 行实际入口/止点、全部新判断与具体限制；实际打开 DeepSeek 索引确认 Dec31 标签，定点核 Jan02 同 exact-v1 候选及 Ch17 正文/末注，确认没有重评分、搬日期或重复书稿产出。root 另 fresh 读取 OpenAI RSS 1251 个 metadata（Dec31 日期切片无条目）、Qwen API 60 项与 Hunyuan API 9 项，修正动态目录旧受阻；Anthropic、Seed/ZAI/ERNIE/MiniMax 的有限切片按作者原记录核对，Google/Meta/MiMo 与两个 revision 的具体限制不升级为无遗漏。抽查原有 card/CLI 贡献前关闭理由，本轮没有新增入选或 Books 修改，无写后代码/实验验收。本日补查通过到合同允许的安全终态，不是全年或全机构无遗漏证明。

复核者：root（非报告作者 jan01_v3）
结论：通过

实际独立复核覆盖：14 个每日来源的当前入口、主题查询/停止点与有限历史缺口；12 个潜在家族的完整精确 v1 题摘；官方 holiday 公告及 availability 规则的日期校准；本日明列的 4 个贡献前关闭项中，2 篇应用论文的完整题摘、Qwen card 核心和 Kimi CLI 0.70 官方变更段均已实际抽核。root 要求补核 AKG 的可迁移控制增量、收窄 KernelEvolve correctness 为 selected-suite pass，并要求恢复 OpenAI RSS、Anthropic embedded 日期及 DeepSeek News 日期切片；作者已落实。mHC 的 Dec31 目录标签、2 项修订日期和机构不可恢复历史入口保留精确重开条件，不作正面证据。

最终验收确认正式本窗候选 0、当窗证据审阅完成 0、Books 写入 0；无剩余可执行工作。原始宽列表未转成逐项关闭队列，外部限制已到安全终态，而非 Coverage/Evidence 无遗漏通过；抽核范围为上述具名材料及报告范围，不是全量互联网/所有原始宽列表负例验证。作者未自称独立复核者。

机器校验：`python3 scripts/validate_research.py --report papers/2026/01/01/README.md` 与 `git diff --check` 已通过；只证明格式与可判定一致性，不替代语义验收。
