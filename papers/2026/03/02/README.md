# Daily Research — 2026-03-02

**规范：** V3
**窗口：** 2026-03-01T09:00:00+08:00 ～ 2026-03-02T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T20:14:00+08:00

## 1. 结论

当前没有已确认首次公开落窗的贡献候选，不能将其表述为“本窗没有新研究”。14 个每日来源均已实际访问并作有界检查；可读的历史段落未发现可确定落窗的新事件，其他目录/批次缺口明确隔离。没有扫描每周来源，也没有用 Weekly 反推 Daily。

有界 arXiv 主题补检发现 4 个 2603 唯一论文身份，均已读取精确 v1 完整题摘，TARSE 另定点读了方法消歧。按官方标识按首公告月份分配及周末公告边界，这些身份的常规 arXiv 首公告不属于本窗；没有独立提前公开的原文项目记录，因此不把 Submitted 日期或搜索范围变成本日日期缺口。它们只保留为 §5 窗外查漏线索，不评分、不计本窗候选、证据完成或 Books 产出。Qwen3.5 小尺寸发布读取官方核心说明后进入贡献前关闭；这不是以版本号、型号或低分替代审阅。

本窗处于周末：arXiv 常规下一次 Sunday 20:00 EST 对应 03/02 09:00 北京时间，恰为不含的右端；2603 身份的常规首公告不能更早落入本窗。这支持常规 arXiv 新批次为 0，不指定四篇具体哪一批首公告，也不排除未取得的更早作者/project公开。旧 DataCite+日程恢复、Effective Date 机构豁免及旧完成标签均不作为本轮证明。

确定候选 0，必要 Books 正文改动 0；未声称已有覆盖已对读或 Evidence 全部通过。非作者日级验收通过，普通待办为0；其他必要外部材料见 §5。旧材料未删除，[原日报快照](../_sources/daily-20260302/V3_LEGACY_REPORT.md)及原 raw 保留，当前判断由本报告和[有限来源停点](../_sources/daily-20260302/V3_SOURCE_NOTES.md)维护。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/Index历史cursor失败后root实际curl[官方RSS](https://openai.com/news/rss.xml)，仅提取本窗pubDate，0 item；原GMT字段见[日期恢复](../_sources/daily-20260306/V3_OPENAI_RSS_ROOT_RECOVERY.md) | 已检查 | 已恢复当前官方feed的目标日期段；不证明未列入feed或更早挂出的页面不存在，Index隐藏分页仍受限 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)页面嵌入 Publications 日期段；提取相邻 publishedOn：02/25T20:02Z、03/05T19:59:21.508Z；本窗无条目 | 已检查 | 只对该公开研究目录段成立，不覆盖未列出的事件 |
| SRC-GOOGLE-AI | [DeepMind Blog p3](https://deepmind.google/blog/page/3/)目标相邻段，Flash-Lite 原文 03/03、Nano Banana 2 为 02 月；[Research 2026/03](https://research.google/blog/2026/03/)p1，尾端03/06；[Pubs](https://research.google/pubs/)年度目录 | 受阻 | Research 月目录 p2 Internal Error，年度论文目录仅年粒度，不足以确认首公开落窗；不遍历全年 372 项 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)实际返回0行；03/01～02官方域定点补检 | 受阻 | 目标历史研究目录/精确发布记录不可恢复，搜索结果不足以证明零命中 |
| SRC-QWEN | 旧[入口](https://qwenlm.github.io/)指向新 Blog；[Qwen3.5官方repo](https://github.com/QwenLM/Qwen3.5)的03/02 news；[0.8B card](https://huggingface.co/Qwen/Qwen3.5-0.8B)、[9B card](https://huggingface.co/Qwen/Qwen3.5-9B)核心说明/配置/评价 | 受阻 | 新Blog动态目录0行；一项明确贡献前关闭不代表全目录零命中，03/02日期未核时区或时刻 |
| SRC-DEEPSEEK | [Research & News](https://www.deepseek.com/en/news/)直读Research Index10项，相邻02/25 DualPath～06/24 V4；[Updates](https://api-docs.deepseek.com/updates)直接HTTP200读Change Log相邻2025/12/01～2026/04/24 | 已检查 | 两个可见目标段无项；News首页View All未展开，不外推隐藏News分页/全机构历史无遗漏 |
| SRC-MOONSHOT | 旧platform Blog过旧后恢复并直读[Kimi Research Blog](https://www.kimi.com/en/blog/)19项至2024/06/26；相邻02/09 Agent Swarm～04/20 K2.6，无可见未完成分页 | 已检查 | 可见Research历史段无本窗项；不声明全机构历史完整，旧platform停止点不再视为必要2026缺口 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)空壳后由root恢复官方页面实际publicList；全部renderType=0、p1、size20，total11/11；[原值](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)对读显示日期相邻02/13～04/23、当前publishedAt亦无03月 | 已检查 | 只声明当前公开全部目录的本窗无项；display日期和publishedAt不互当首次公开，不外推全机构历史无遗漏 |
| SRC-ZAI | 首查[Research全部](https://www.zhipuai.cn/zh/research)时间排序，覆盖相邻02/21 GLM-5报告～03/15 GLM-5-Turbo段 | 已检查 | 无本窗目录事件；只对该公开目录成立 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)、[Public papers](https://seed.bytedance.com/en/public_papers)；目录实际停止p1，1–20/242、13页；03/01～02定点日期补检 | 受阻 | 动态历史页段未恢复；p1不能证明03/01～02无项，也不把242目录变成全文队列 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)相邻02/06 ERNIE5～04/15 ERNIE-Image；Publication入口HTTP200；目标段无可读条目 | 已检查 | 对可见Blog研究发布段成立，未声称全站召回 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper相邻02/03 HySparse～03/13 ARL-Tangram；Blog标题当前无日期；03/01～02定点补检 | 受阻 | Paper段无项；Blog缺历史日期/cursor，不能以当前标题反推本窗归属 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)、[中文](https://www.minimaxi.com/blog)可读列表均跨02月～03/18，邻项Forge为02/14或中文02/12；[TechBlog](https://agent.minimax.io/docs/techblog)、llms.txt目录 | 已检查 | 可见Blog段无项；TechBlog只有当前无日期索引，对其历史覆盖受限，保留目录恢复条件 |
| SRC-ARXIV | 官方[availability](https://info.arxiv.org/help/availability.html)周末规则与ID按首公告月份分配；[cs.DC月列表](https://arxiv.org/list/cs.DC/2026-03?show=2000)只作身份查漏；4组主题日期补检命中4个2603身份并读精确v1题摘 | 已检查 | 常规首公告在窗内0批，4项为窗外查漏；历史日列表不可达，不声称全量特殊事件/更早作者公开均已覆盖，不以Submitted代替公开日期 |

所有“已检查”只声明表内明确边界；受阻或历史检索限制不是 Coverage 通过。按需来源未出现具体触发，无额外常规扫描。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

没有确定落窗且通过贡献筛选的候选。四个 2603 身份不属于本窗常规 arXiv 首公告，放入 §5 窗外查漏记录，不为填表伪造时间或评分。

## 4. 证据与知识整合

本窗没有可采用的候选，因此没有深入完成计数、性能数字采用或 Books 写回。作者未把四篇完整摘要当作证据审阅；TARSE 的有限方法消歧也只回答准入，不验证其所有实验。

Qwen3.5 小尺寸 release 为准入前关闭：官方 repo 只给 03/02 日期；0.8B/9B 卡的核心机制继承该家族既有 hybrid attention、早期多模态融合和后训练，新增尺寸配置与分数表未给出足以修正本项目设计选择的可比资源/质量边界。0.8B 卡通用 Highlights 的 sparse-MoE措辞与具体 dense FFN配置并列，不能借宣传措辞扩大新增机制。小模型并非按规模排除；若出现尺寸特有机制或严格可比边界证据再定点重开。详见[准入记录](../_sources/daily-20260302/V3_SOURCE_NOTES.md)。

## 5. 缺口与下一步

普通待办为0。以下具体缺口为本窗终态保留项，不用于正面证据、Books或无遗漏断言；材料到达后按所列身份定点重开。

窗外查漏发现（不属于本窗，不阻塞本日；没有授予其他具体日期归属）：

| 身份 | 已读取的贡献线索 | 窗外处置与边界 |
| --- | --- | --- |
| [2603.00846v1 Tiny-Critic RAG](https://arxiv.org/abs/2603.00846v1) | Submitted 2026-03-01T00:16:31Z；完整题摘指向LoRA小critic、约束解码/非thinking二值routing，把评价执行成本从大生成器中解耦 | 2603身份的常规首公告在本窗右端或之后；无更早独立原文公开信号。仅作以后真实归属日报的查漏入口，未采用质量/延迟/噪声结论 |
| [2603.00873v1 MC-Search](https://arxiv.org/abs/2603.00873v1) | Submitted 2026-03-01T02:25:57Z；完整题摘指向hop级模态/证据链与过程评价，可能揭示终答准确率遮蔽的规划/检索失配 | 同上；ICLR标签不授日期或贡献成立。以后实际归属日报若触发，核HAVE与process evaluator |
| [2603.01160v1 Semantic XPath](https://arxiv.org/abs/2603.01160v1) | Submitted 2026-03-01T15:56:08Z；完整题摘指向树结构memory寻址/更新，潜在改变flat-RAG检索单位 | 同上；未采用摘要收益数字。以后实际归属日报若触发，核树查询/更新与flat baselines预算 |
| [2603.01241v1 TARSE](https://arxiv.org/abs/2603.01241v1) | Submitted 2026-03-01T19:31:23Z；完整题摘并定点读[§3～5及§7.2/A.1](https://arxiv.org/html/2603.01241v1)，experience适配→provisional chain→step-aware skill gate；不是因medical标题排除，math与joint adaptation分支需核边界 | 同上；方法定点读只完成准入消歧，不是Evidence完成。以后实际归属日报若触发，再核适配监督/每步验证/联合batch噪声/归因 |

四个精确v1页面未见撤回/删除标记，不声称完整版本史检查，也未核代码。该轻量观察仅随窗外线索保留，不建立本窗安全保证。

本窗外部终态保留项一次请求（不用于正面证据、Books或无遗漏）：OpenAI Index历史cursor；Meta历史Research记录；Google Research月目录p2与相关论文首公开记录；Qwen新Blog历史日期目录；Seed目标历史页；MiMo Blog历史日期目录；MiniMax TechBlog历史日期目录。可接受官方归档、当时公告/邮件、精确版本发布日志或有时区作者首公开正文；新材料只重开对应源/身份，不重新扫描整月。未恢复部分不支持全站无遗漏，外部材料长期缺失本身不要求永久进行中。

## 6. 复核

复核者：root（非作者）
结论：通过

root实际核14来源行及原始停点、arXiv常规公告右端、全部4个具名窗外身份与Qwen小尺寸完整核心的关闭理由；具名分层抽检Anthropic相邻publishedOn（直接HTTP原字段）、DeepSeek/Kimi/混元/ZAI/ERNIE/MiniMax目录日期段。恢复OpenAI官方RSS本窗0item，但不由feed缺项认证全机构无遗漏；§5原Index请求仅保留未列入feed的隐藏历史事件。0候选不作Evidence或Books已覆盖断言，外部限制不承担正面采用；没有普通未执行工作。未重新审阅窗外全文，未检查隐藏未恢复目录内容。以下作者机器检查为格式证据，最终格式和diff-check另由root执行。

作者 mar02_v3 只完成上述实际访问、有界补检、四篇窗外精确题摘与一项准入方法消歧，不能授自己的日级 Gate。拟验范围：14来源停点/过宽入口、周末右端与ID首公告月份边界、4窗外查漏身份、Qwen具名负侧（已获root首批准入校准）、可见相邻日期排除分层样本、零必要Books与旧raw保留。本地检查：`python3 scripts/validate_research.py --report papers/2026/03/02/README.md` 通过（1份V3）；本日README与两份V3记录的 `git diff --check` 通过；README/来源记录7个本地Markdown链接均存在（随后目录恢复只新增官方网页链接）。工作树同时有其他作者日期/共享文件修改，已保留，作者只写本日README及V3_*两份记录。格式通过不替代语义复核。未 stage、commit、push。
