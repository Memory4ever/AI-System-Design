# Daily Research — 2026-05-03

**规范：** V3

**窗口：** 2026-05-02T09:00:00+08:00 ～ 2026-05-03T09:00:00+08:00

**补充窗口：** 2026-05-02 ～ 2026-05-02

**窗口说明：** 用户明确要求保留原候选、日期、评分、原小时窗及连续原 §4，只按前一北京时间完整自然日补遗漏；旧完成与复核仅为原检查存档，不代替本轮验收。

**冻结候选日期：** [原报告](../_sources/daily-20260503/baseline-before-supplement-20261016.md)

**状态：** 完成

**阶段：** 本轮独立 DAY 通过；来源限制安全隔离，Evidence 与 Books 按零确定候选完成处置，无普通待办

**Books：** 纳入本次

**检查时间：** 2026-10-16T10:56:19+08:00

## 1. 结论

本轮独立补查 05-02 北京时间自然日的十四个每日来源，确定新增候选 0，与原 0 合计 0；没有需要评分、标准/深入审阅或写入 Books 的确定新家族，Books Decision 为 `No Change`。这只针对列明来源切片中已确认的本窗集合，不证明受阻的历史目录没有有价值材料。原始检索/metadata 数不计作当日论文数，也不沿用旧提交时间账本的 512/274/36 数量。

arXiv 官方公告规则确认该日没有计划公告，不能把提交时间命中当首次公开；机构入口仍独立检查。实际恢复 OpenAI RSS 1294 日期项、Qwen API 40 日期项、Seed 目标 paper/blog 20/15 项，均无本窗身份；其余机构按下表的有限可核切片处理。Google 日级出版目录、Meta 目标日出版分页、Kimi 2026 历史 Blog 段、MiMo Blog 日期仍精确隔离，不授完整 Coverage/Evidence、Books 或无遗漏。必要依据与来源资格负侧校准在[唯一补查记录](../_sources/daily-20260503/SUP_SOURCES_20261016.md)。本轮保存后的完整六部分已经独立 DAY 实际通过，不复用旧通过标签；普通可执行工作为0。

## 2. 来源覆盖

本轮只检查每日来源，不扫 Weekly。实际入口与停止点见[补查记录 A2](../_sources/daily-20260503/SUP_SOURCES_20261016.md#a2-实际来源入口范围和停止点)；表中“已检查”仅指列明切片，搜索空结果与目录首页不证明全渠道零事件。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 首查 [Research](https://openai.com/research/)与 index；历史 Load More 未恢复后，复用[官方RSS](https://openai.com/news/rss.xml)同日原件全部1294 item日期，2026-10-15到2015-12-11，Apr30→May4无May2 | 已检查 | 只授RSS可见slice；不证明已删条目或所有发布渠道无遗漏 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)直接HTML内80个publishedOn，Apr30→May7，全部日期无May2 | 已检查 | 首10卡及See more不当历史全表；范围为实际embedded日期切片 |
| SRC-GOOGLE-AI | [News page3](https://deepmind.google/blog/page/3/)跨Apr/May，实核AlphaEvolve May7、Pointer May12；[Publications](https://deepmind.google/research/publications/)与[Research](https://research.google/pubs/)部分年/月；Research Blog恢复失败 | 受阻 | 出版目录未恢复日级目标窗，不授完整Coverage；保留恢复条件于§5 |
| SRC-META-AI | [Results](https://ai.meta.com/results/)与实际Next的[page2](https://ai.meta.com/global_search/?page=2)，混人物/论文/dataset，非全局日期排序；定日辅助搜索未恢复本窗身份 | 受阻 | 两可见页不是目标日完整出版分页，旧表日期边界不沿用 |
| SRC-QWEN | 旧入口/新Blog后转[官方API](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)，全部40非排序extra.date，无May2；Apr30 Scope、May19/20、May29均窗外 | 已检查 | 仅英语API可见slice，无分页字段；不声称全org其他渠道已覆盖 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/)与[更新日志](https://api-docs.deepseek.com/updates/)，实际Apr24→Jul31跨窗 | 已检查 | 限官网与更新日志，不把普通活动当新研究 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)可见25篇旧目录、页脚2025，未恢复目标2026段；[官方组织](https://github.com/MoonshotAI)API42个项目创建身份，Apr20 FlashKDA→May22 kimi-code | 受阻 | 创建日期不能补齐2026历史Blog/release/论文；该Blog段限制隔离 |
| SRC-TENCENT-HUNYUAN | 首查[Research](https://hunyuan.tencent.com/research)后改官方publicList POST全部类型page1/size100；实际9/9均en，Apr30 15:00→Jul8，无May2 | 已检查 | 只支持实际All可见slice；不沿用旧8/8、不用中文文件名证明中文已读或另设假想语言Gate |
| SRC-ZAI | 首查[Research](https://www.zhipuai.cn/zh/research)超时后直接HTML恢复首15卡，Apr29 Scaling Pain→May20 ZCube | 已检查 | 已跨目标窗口后停止，不扩更早目录或把createdAt改名为公开时间 |
| SRC-BYTEDANCE-SEED | [论文目录](https://seed.bytedance.com/en/public_papers)官方API paper offset20实际20项，May16→May4→May1两项→Apr30→Apr15，next40；Blog offset0实际15英语项，Jun19→Apr23，next20 | 已检查 | 两目标可见slice无May2且已跨窗停止，不把total246/96扩成队列；按PublishDate的BJT；不为假想隐藏材料另设Gate |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)完整可见4卡，Apr30榜单→May9发布 | 已检查 | 只本目录；榜单不是自动准入理由 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/) web与直接HTML，Paper Mar13→Jun29；Blog15卡缺日级日期 | 受阻 | Paper切片已处理；Blog无日期不当零事件 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)/[中文](https://www.minimax.cn/blog)完整SSR12/13卡，英Mar18→May26/27、中Apr27→May25；[Agent Tech Blog](https://agent.minimax.io/docs/techblog)可见3篇Sep/Oct | 已检查 | 双语日期差异均窗外，不拼接或重定日期；仅公开目录 |
| SRC-ARXIV | [官方公告日程](https://info.arxiv.org/help/availability.html#announcement-schedule)实际172、182–186，May2 BJT为Friday EDT无公告；前Thu公告在May1 BJT、下Sun在May4 BJT | 已检查 | 无本日计划公告不排除作者在机构站先发；未按Submitted或DOI created扩队列 |

## 3. 候选与判断

日期归属、跨来源去重、项目范围和贡献判断后没有留下候选。候选为零时不生成空评分，也不把受限入口或窗外提交记成零分候选。

2026-10-16补充自然日新增0，原0合0；本轮未从旧512提交库存或旧36家族反推当日候选。逐项来源资格负侧在[补查记录 A3](../_sources/daily-20260503/SUP_SOURCES_20261016.md#a3-首批校准确定候选与books)，不称窗外材料已经完成贡献或Evidence审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

本窗没有候选进入 Evidence Review，因此没有需要与 Books 命题比较的机制增量，也没有 Stable Knowledge Node owner。Books Decision 为 `No Change`，没有修改 `books/`。

这一判断只表示“本窗没有确认的贡献候选”，不是说旧过程材料中的论文都没有价值。旧 36 个候选若在后续 owner day 按当前贡献标准仍然成立，应由真实首次公开窗口承担证据审阅与 Books 处置；05-03 不沿用其旧评分、旧 Books 结论或已完成状态，也不删除其他日期已经有合法证据支持的 Books 正文。

补充自然日判断：以上连续两段是运行前原 §4，原文完整保留；本轮不是据此跳过检查。实际机构日期资格与 arXiv 日程检查后仍无确定新增候选，因此没有新增必要Source、评分或Stable Node owner比较，Books新写0。受阻切片不获No Change的证据保证，也不写入Books。Seed May1两项/May4视频生成、Qwen Apr30/May19等具名窗外材料只作日期负侧，不扩大本日报到其实际归属日。

## 5. 缺口与下一步

本轮可执行研究扫描、确定候选、Books写回与独立复核待办0，完整六部分已获本轮独立DAY。以下外部历史发现限制已在当前可用入口的有限恢复后隔离，不用于正面Coverage/Evidence、Books或无遗漏。

**终态保留项：** 下列限制均不支持正面证据、Books 或无遗漏断言；每项只在对应的官方日级时间或唯一材料身份恢复时定点重开。

- `SRC-GOOGLE-AI`：Research出版目录缺目标日日级日期，Blog定点恢复失败；需要官方可查询日级目录或具体May2模型/系统原文，不用年份/月代替。
- `SRC-META-AI`：Results两页与真实Next混合类型且非全局日期排序；需要可核目标日的出版分页或具名官方事件，只重开对应slice/家族，不用当前首屏保证历史无遗漏。
- `SRC-MOONSHOT`：现可见Blog旧目录与页脚2025，目标2026历史段未恢复；需要可核该段的官方归档或具名May2原文，repo创建身份不能补齐release/论文公开史。
- `SRC-XIAOMI-MIMO`：Paper已查，Blog15卡无日级日期；需要官方Blog时间或唯一材料metadata。未恢复前不记零贡献。

Qwen迁移缺口在本轮由官方API40个日期项恢复到该英语可见slice，不继续沿用旧“无日级列表”说法；不因此声称所有其他渠道已覆盖。OpenAI的LoadMore限制由同日官方RSS原件恢复，不把精选目录失败写成整源受阻。

窗外恢复项：旧 `screening-ledger-v2.1` 的 512 个提交时间命中不归 05-03；它们需要在实际公开公告所属日期执行去重、撤回检查和贡献判断，不能整体搬成下一日候选，也不阻塞本窗作者侧结束。

## 6. 复核

复核者：`/root`（本轮非报告作者）

结论：通过

root实际完整读回本轮保存README六部分及唯一SUP，检查14源限定查询、停止与非队列范围。独立来源资格负侧实际覆盖arXiv官方公告、Qwen全部40非排序metadata、Seed两原件20/15项PublishDate→BJT、MiniMax英语SSR边界及OpenAI RSS1294日期项；其余明确来源记录按合同范围检查，不称全量正文复核。确认具名窗外项不搬移到May2；原0候选、小时窗及连续原§4保持，新增0、Books No Change，无拟入选所以不造Evidence或Books POST。Google/Meta/Kimi2026/MiMo Blog四发现限制精确隔离，Hunyuan/Seed不增设假想语言Gate。V3、8本地引用0缺、围栏/冻结、README/SUP限定cached与unstaged diff，以及本轮42窗口测试均实际通过。实际DAY与保存完成态行政读回见[唯一SUP验收段](../_sources/daily-20260503/SUP_SOURCES_20261016.md#a6-root实际day通过与完成态保存)；机器检查不替代上述语义复核。
