# Daily Research — 2026-06-07

**规范：** V3
**窗口：** 2026-06-06T09:00:00+08:00 ～ 2026-06-07T09:00:00+08:00
**窗口说明：** 用户授权只补遗漏；原小时窗、原有材料归属与有效证据保留，不移动旧候选。
**补充窗口：** 2026-06-06 ～ 2026-06-06
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-25T17:32:27+08:00

## 1. 结论

本轮对 14 个每日来源补查 6 月 6 日北京时间自然日，没有确认新增候选；因此没有新增评分、证据审阅或 Books 修改。Google 的 Blog 范围已检查，但 Publications 的日级公开日期目录未恢复，作为来源终态保留项隔离，不授予其正面覆盖或“零研究”结论。机构来源以官方目录目标相邻日期和当前公开元数据为边界，不把搜索零命中或旧空候选表当作覆盖证明。arXiv 无常规周末公告批次，当前 DataCite 精确登记区间也未返回条目；这只支持本次有界检查，不证明全球当天没有作者早稿或未被目录保存的发布。

旧报告空候选及旧 submission-date packet 的迁出关系保留。本轮经 root 非作者独立复核达到安全终态；Google Publications 的日级目录缺口仍明确隔离，不授全面 Coverage 或零研究保证，旧 `fresh-context` 声明没有被用来代替本轮验收。[本日入口、查询与停止依据](../_sources/daily-20260607/SUP_SOURCE_CHECK_20261025.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 RSS](https://openai.com/news/rss.xml) 当前单次响应 1318 项，按原 `pubDate` 转 BJT 定位目标：06-04 后下一公开项为 06-08，无 06-06 项；到早于目标日停止日期选择，不扩读旧正文 | 已检查 | 无具名缺项；RSS 不证明已删除历史事件不存在 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) → [官方历史目录第 2 页](https://www.anthropic.com/listing/research/default/2)，24 项、覆盖 07-28～04-23；目标邻段 06-08 → 06-05 → 06-03，无 06-06 项，越过目标即停，不继续第 3 页 | 已检查 | 无 |
| SRC-GOOGLE-AI | 已检查 Blog 范围：[DeepMind 目录第 2 页](https://deepmind.google/blog/page/2/) 的目标相邻原件日期为 06-03 Gemma 4 12B → 06-09 欧洲机器人项目；[Research 六月 Blog](https://research.google/blog/2026/06/) 一页 12 项、无分页，06-10 → 06-05，无 06-06 项。[Publications](https://research.google/pubs/) 只取得年级元数据导航，未恢复目标日公开列表，不虚构首次公开日 | 受阻 | Blog 范围已检查；Publications 的 2026-06-06 日级日期与原目录未能恢复，不授其正面 Coverage 或零研究断言，按 §5 隔离 |
| SRC-META-AI | [Research](https://ai.meta.com/research/) 与 [Blog](https://ai.meta.com/blog/) 可见研究条目；Blog 第一页含目标两侧 06-29 与 04-08 等日期，无 06-06 项；官方域内目标日期补检无相关原始发布线索，停止于该页及该查询 | 已检查 | 目录并非完整历史快照；不外推为全站绝无发布 |
| SRC-QWEN | 旧站明示迁往 [qwen.ai](https://qwen.ai/research)；按当前页面调用的 [article retrieval](https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US)，`type=qwen_ai`、`language=en-US/zh-CN` 各返回 40 项，无分页字段；目标邻段 06-01 → 06-16，无 06-06 项，停止于两响应 | 已检查 | 无；未采用无参数空响应或仅含 2025 条目的旧配置授零 |
| SRC-DEEPSEEK | [官网研究入口](https://www.deepseek.com/) 与 [官方 Change Log](https://api-docs.deepseek.com/updates) 目标邻段 04-24 → 07-31，无 06-06 发布说明；不扩普通提交 | 已检查 | 无具名缺项 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog) 完整可见目录最新 2025-11-07；[官方组织目录](https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated) 补查，没有 06-06 新建研究仓库线索；没有据 `updated_at` 推定论文首次公开 | 已检查 | 旧博客不是 2026 全量发布档案；未发现需定点恢复的本日事件 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research) 的“全部”调用 `POST https://api.hunyuan.tencent.com/api/blog/publicList`，`pageNum=1,pageSize=100,renderType=0`，按官方请求头 `accept-language:zh` 返回 `totalNum=11,list=11`；目标邻段 07-06 → 05-21，无 06-06 项，响应已尽 | 已检查 | 无；默认英语 9 项未冒充中文“全部” |
| SRC-ZAI | [官方 Research](https://www.zhipuai.cn/zh/research) 首屏日期降序，06-16 GLM-5.2 → 05-20 ZCube，目标区间已越过，不点更早“查看更多” | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | [官方 Publications](https://seed.bytedance.com/en/public_papers) 第一页 1～20 / 246，06-11 → 06-04 → 06-03，目标区间已越过，停止第 1 页；不把窗外科学应用条目引入候选 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | [官方技术 Blog](https://ernie.baidu.com/blog/zh/) 首屏最新 05-09，已早于目标；不进入更早第 2 页 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | [官方 Paper/Blog](https://mimo.xiaomi.com/)：Paper 06-29 → 03-13；官方路由 metadata 的有日期技术 Blog 为 05-30 inference → 06-08 TileRT → 06-10 Code。[官方 Model Release](https://mimo.mi.com/docs/en-US/updates/model) 单页目标邻段 09-22 → 06-02 ASR → 04-23 V2.5，补齐无日期模型卡片的发布日；没有 06-06 项，目标区间已越过即停 | 已检查 | 部分博客 CSR 仍只返壳，未将其正文当作已读；模型发布日期采用可读官方更新目录 |
| SRC-MINIMAX | [官方 Research/Blog](https://www.minimax.io/blog) 同页目标邻段 06-09 MaxProof → 06-01 M3，无 06-06 项；日期已越过即停 | 已检查 | 无 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html)：美东周五/周六不公告，2026-06-06 BJT 无常规批次（含 replacement、withdrawal）；[DataCite](https://api.datacite.org/dois) 使用参数 `client-id=arxiv.content`、query `registered:[2026-06-05T16:00:00Z TO 2026-06-06T15:59:59Z]`，`total=0,totalPages=0`；来源与日期字段均已用正控制核对。旧迁出 packet 只作去重，不形成题摘队列 | 已检查 | 不把登记零条目或无常规批次外推为所有早稿/特殊延迟事件零；本次未发现具名恢复线索 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

无。本轮新增候选为 0；原报告候选表仍为空。目录邻段和日期不明的一般卡片不算通过贡献筛选的候选，也不评分。

## 4. 证据与知识整合

本轮没有新增采用命题，因而不触发分数、证据深审或 Books 写回。当前查询范围、原始字段摘录、相邻日期和访问局限见[补查记录](../_sources/daily-20260607/SUP_SOURCE_CHECK_20261025.md)。明确区分“指定入口没有本日条目”与“整个互联网没有新公开材料”。

旧 [261/23 submission-date packet](../_sources/daily-20260607/README.md) 不是本轮新增分母；其 23 个家族已由旧归属记录迁出，本轮未移动、改分或重新采用。原有 Evidence 仅作可复用 provenance。旧记录把 DataCite `created` 单独写成公开日期证明的措辞不作为本轮依据；本轮只用已核官方公告规则和明确标名的 `registered` 查询结果，不将两者改称逐篇实际首公开时刻。没有新的长期知识差额，不为制造改书记录另加警句。

## 5. 缺口与下一步

无普通可执行待办。本轮实际入口与停止点、空新增候选判断、来源局限及无 Books 修改已由非作者复核。

本窗终态保留项：`SRC-GOOGLE-AI / Google Research Publications`（[官方入口](https://research.google/pubs/)）。当前只取得年级元数据导航，无法确认 2026-06-06 的日级公开目录；Blog 已检查的事实不能替代论文目录覆盖。本项不用于正面证据、Books 或无遗漏断言，不支持“Google 当天零研究”或该部分 Coverage 通过。可接受替代为包含该自然日的有日期官方发布列表、明确对应本日事件的具名作者/机构正文，或可读且保留发布日期的当日目录快照。取得任一种后，仅重开本日 Publications 入口与其中相关材料的日期、题摘准入及必要审阅，不扩成全年论文队列。

来源局限已在覆盖表隔离：当前机构目录不是完整历史快照，Meta/Kimi 的有限目录不能支持无限制“零发布”断言；arXiv 周末规则与登记零条目也不证明无作者早稿。MiMo 无日期模型卡片已通过官方 Model Release 补齐，不再作为日期缺口。当前没有具名、必要证据缺失的当窗候选，因此不建立未知材料请求。若取得公开日期明确为 2026-06-06 的相关官方事件、作者正文，或指向上述未保存事件的精确链接，仅重开该来源及材料，重新执行题摘准入与必要日期核验。

## 6. 复核

复核者：root（非报告作者；报告作者为 supp_jun07）

结论：通过

实际检查本轮六节、14源的入口/日期邻段/分页与停止，未把整月标题或旧迁出材料变成待审队列。独立读取中英Qwen各40项原始响应及中文Hunyuan全部11项，按原日期/身份核目标邻段；无参数空响应、英语9项和只到2025的配置均未冒充当前覆盖。核本日 DataCite 保存原响应的有效 `client-id` 参数、完整BJT登记区间、0条/0页/无next，并检查作者正控制及无效查询废弃记录；root复取API的工具访问失败不抹除可读原响应，也不改称所有路径受阻。root另实际打开官方公告规则，确认美东周五/周六不公告的BJT换日含义，但不据此保证全球没有早稿或特殊公开。

无新增候选，故没有需独核的评分、必要证据或Books采用；没有以原空表证明无漏，亦未更改旧材料归属。日级核纠正Google Blog已查不等Publications日级覆盖，缺口现已具名隔离并保替代/定点重开，不授正面Gate。“完成”仅指本次处理安全终态，不表示该保留项证据已经补齐。V3、Markdown/本地引用及限定差异检查按实际工具结果执行；机器结果不替代语义复核，未stage、commit或push。
