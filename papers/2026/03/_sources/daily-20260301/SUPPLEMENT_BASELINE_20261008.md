# Daily Research — 2026-03-01

**规范：** V3
**窗口：** 2026-02-28T09:00:00+08:00 ～ 2026-03-01T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T20:02:03+08:00

## 1. 结论

确定落窗候选为1家族，按安全部署约束变化完成窄深入审阅后仅报告；必要 Books 整合为0。14每日源均有限检查；OpenAI官方RSS恢复了本窗公告确时，其他目录/日期限制见§2/§5。非作者最终复核通过，普通待办为0；外部保留项不算正面覆盖或证据通过。

arXiv 常规日程在本窗无批次；Submitted、DOI registration、旧宽月份库存均不能补造 first-public。特殊延期/非例行批次历史不能排除。旧 EffectiveDate 豁免、9分、分母、Complete 标签不作为本轮判断，没有参考 Weekly。

OpenAI 2/28 公告披露云端部署及厂商保留安全栈控制权。RSS原字段给出02/28T12:30GMT，即北京时间20:30，落窗；当前正文以更新分隔线区分3/2后加措辞，后者不回填。本次只确认厂商公开的配置/责任声明，没有技术有效性证据，不形成Books机制增量。

## 2. 来源覆盖

实际主题、查询、首次响应和停止点见 [V3 查询记录](../_sources/daily-20260301/V3_QUERY_STOPPOINTS.md)；原始响应为本日 V3_RAW 文件。搜索空返、首页与年份表均不证明无遗漏，“已检查”仅指具名有限日期目录段。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| [SRC-OPENAI](https://openai.com/research/) | Research/Index失败后root实际curl[官方RSS](https://openai.com/news/rss.xml)，本窗1公告，pubDate原值见[日期恢复](../_sources/daily-20260306/V3_OPENAI_RSS_ROOT_RECOVERY.md)；原文更新分隔线下2/28正文与FAQ必要段已核 | 已检查 | RSS公开日期段已恢复；D1仅保留未列入feed的隐藏历史事件，不能授全机构无遗漏 |
| [SRC-ANTHROPIC](https://www.anthropic.com/research) | Research首10项，See more仍返回同页；窗口日期域查询首批 | 受阻 | D2历史分页不可枚举，不能由无搜索命中推零研究。 |
| [SRC-GOOGLE-AI](https://deepmind.google/research/) | DeepMind blog page3跨二～三月，2/19及2/26 card；publications page12实际仍当前六月以上；Google Research pubs年级2026表及窗口域查询 | 受阻 | D3论文目录日级历史未恢复；年级表不扩成全文队列。 |
| [SRC-META-AI](https://ai.meta.com/research/) | 原入口提取0行，窗口域查询首批仅恢复旧主题页 | 受阻 | D4动态research历史目录；空提取不是零事件。 |
| [SRC-QWEN](https://qwenlm.github.io/) | 旧博客redirect至qwen.ai/blog，新站提取0行；日期域查询首批 | 受阻 | D5新站动态历史目录；旧站2025页不代替2026覆盖。 |
| [SRC-DEEPSEEK](https://www.deepseek.com/en/news/) | root补开官方Research & News；Research Index可见10项至2025/05/14，2/25 DualPath→6/24 V4跨过本窗；原updates两次timeout保留 | 已检查 | 可见研究目录本窗段无条目；D6仅保留News隐藏View All与API updates历史限制，不外推全机构。 |
| [SRC-MOONSHOT](https://www.kimi.com/en/blog/) | root补开官方Research完整可见19项至2024/06/26，2/9 Agent Swarm→4/20 K2.6跨过本窗 | 已检查 | 当前可见研究目录无本窗条目；原platform博客止于2025不再充当2026目录不可恢复依据，撤销D7。 |
| [SRC-TENCENT-HUNYUAN](https://hunyuan.tencent.com/research) | 网页/浏览器失败后root按官方脚本生产publicList/renderType0,page1,size20恢复；total11/返回11，全可见目录已读；显示日期2/13→4/23跨过本窗，见[原始恢复](../_sources/V3_HUNYUAN_LIST_RECOVERY.md) | 已检查 | 当前可见目录无本窗条目，不证明未删除条目/全机构历史。D8撤销；browser失败过程保留。 |
| [SRC-ZAI](https://www.zhipuai.cn/zh/research) | Research全部可见列表8/26→2025/12/09，2/21 GLM-5报告→3/15 GLM-5-Turbo；release notes读至2025/07/15 | 已检查 | 可见窗口段无条目，停止已越过本窗，不宣称全机构无遗漏。 |
| [SRC-BYTEDANCE-SEED](https://seed.bytedance.com/en/research) | research可见表1/27→4/11；public_papers首20项/Page1of13；日期域查询首批 | 受阻 | D9完整论文历史分页未恢复，首页不证明全部研究无命中。 |
| [SRC-BAIDU-ERNIE](https://ernie.baidu.com/blog/zh/) | 中文博客可见日期4/15 ERNIE-Image跨到2/6 ERNIE5.0与1/29 PaddleOCR-VL | 已检查 | 官方博客窗口段无条目，停止已越过本窗，不外推全机构。 |
| [SRC-XIAOMI-MIMO](https://mimo.xiaomi.com/) | Paper完整8项，2/3 HySparse→3/13 ARL-Tangram；Blog可见15项及More；日期域查询首批 | 受阻 | D10 Paper本窗段无条目；Blog历史无日期且More未恢复。 |
| [SRC-MINIMAX](https://www.minimax.io/blog) | 英文与中文重定向minimax.cn/blog可见完整目录；Forge英文2/14、中文2/12原值分别保留，均窗外；M2.7为3/18 | 已检查 | 可见窗口段无条目，没有把财报算研究，不外推全机构。 |
| [SRC-ARXIV](https://info.arxiv.org/help/availability.html#announcement-schedule) | 实读公告日程/2026节假日；本窗2/27 20:00 EST→2/28 20:00 EST；二/三月cs各首1～2000身份页无日批次即止；窗口announced_date_first主题查询首请求cache miss | 受阻 | AX1无常规slot，但非例行/延期历史不能排除；失败查询不记零命中。 |

没有扫描每周来源或额外按需发现源。arXiv 主线主题为 CL/LG/AI/DC 的 LLM/Transformer/MoE/训练优化/Agent，CV/RO 的生成基础模型/World Model/VLA，AR/PL/OS/PF 的 kernel/runtime，IR/MA 的 RAG/记忆/协作。无例行批次可浏览；宽月表只作身份查漏，不是逐项题摘/全文队列。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Our agreement with the Department of War](https://openai.com/index/our-agreement-with-the-department-of-war/) | 2026-02-28T20:30:00+08:00 | 云端部署/厂商安全栈控制权形成具体版本配置声明，但未披露可迁移机制；1 + 2 + 1 = 4 | 深入完成 | 仅报告：Version Fact / Mechanism Not Disclosed，无长期机制增量 |

只有这个唯一家族，3/2追加措辞不是本窗事件；窗外及明确范围外材料保留在筛选记录，不冒充当窗已审家族。

## 4. 证据与知识整合

### [Our agreement with the Department of War](https://openai.com/index/our-agreement-with-the-department-of-war/)

精确范围为更新分隔线下的2/28说明“Deployment architecture”、人员参与及FAQ，不采用3/2新增条款。原文公开cloud-only而非edge部署，由厂商运行/更新安全栈及classifier，特定人员参与；这能确认公开声明的控制权归属，不能证明检查完整性、真实执行路径或禁止行为不可能发生。其“可以独立验证”和绝对防止滥用的保证缺少威胁模型、实现与效果证据，不予采用。

root与mar02_v3独立读取上述必要正文及官方RSS原字段。对读`PLATFORM-SECURITY` [Ch72资产/信任边界与部署残余风险循环](../../../../books/part-06-ai-infrastructure/72-security.md)：该章解释主体、控制位置、mitigation验证和决策责任；本公告没有足以新增或修正它的机制证据。因此仅报告版本事实，不声称某专属架构“已覆盖”，也不修改Books。2/28旧响应保留，RSS日期纠正原日期隔离，未删除反证。

保留旧有效原文与账本；[旧日报快照](../_sources/daily-20260301/V3_LEGACY_REPORT_SNAPSHOT.md)仅用于恢复，不定义当前日期、分母或完成标准。本日未修改共享 Books、索引或 LEARNING_STATE。

## 5. 缺口与下一步

普通待办为0。以下为本窗终态保留项，不支持候选、正面证据、Books、无遗漏断言、安全或性能保证；材料到达后定点重开。

- **OP1原日期请求已解决**：官方RSS给出带时区发布时间，原2/28说明可由更新分隔线限定。仅当后续提供具体部署实现、验证协议或反证时，才重开本家族的机制/有效性判断；当前厂商保证不支持正面安全采用。
- **D1～D6、D9～D10 — 历史子目录**：来源身份、具体URL和停止点在 §2 对应行；D6仅为News隐藏分页/API updates。所需为本窗主线相关事件的可枚举dated archive/原发布/release列表或可访问动态历史过滤。当前原入口、有限搜索及必要浏览器尝试未恢复相应历史段；没有取得确定线索不等于零事件。D7的Kimi研究目录与D8的混元目录已实际恢复，不再索取。只重开具名受阻子入口与本窗，不扩全年/全机构全文队列。
- **AX1 — arXiv 非例行/延期历史**：常规日程无slot；官方窗口主题查询cache miss，月表不提供日批次。可接受覆盖本窗的官方公告/延期status邮件及相关精确身份。只重开该批次与当前主线主题，不以DataCite/Submitted补造first-public。

窗外线索（仅用于排除复核，不扩本任务）：ZAI GLM-5报告2/21；MiMo HySparse2/3、ARL-Tangram3/13；MiniMax Forge英文2/14、中文2/12；Google Gemini3.1 Pro/FlashImage card2/19和2/26。MiMo New Materials R&D 的标题明确为材料应用，属 ROADMAP 暂缓 AIforScience，未见需重开的当前纠错/安全/修订信号，不穷追其日期。

## 6. 复核

复核者：root（原报告非作者）；mar02_v3（新增公告窄审阅非作者）
结论：通过

2026-10-01 root 实读 OP1 官方核心说明，同意潜在贡献日期隔离，不能按 Company 标签关闭或反填3/2修订；抽检 ZAI/MiMo/MiniMax 窗外身份和 AIforScience 范围退出理由成立。该批为1潜在贡献隔离及五组具名负侧身份的分层校准，不称全机构目录全量验证。

root最终检查14/14来源行及有限停止记录、北京时间周末窗口与公告节奏、唯一候选OP1及五组具名负侧（ZAI GLM-5；MiMo HySparse/ARL-Tangram；MiniMax Forge中英日期；MiMo材料研发；Google两张2月card）。OpenAI RSS恢复后仅重开OP1日期及处置，mar02_v3实际再读原说明/FAQ与RSS，批准1+2+1、窄深入和仅报告边界，不采用未证安全保证；普通待办0，无必要Books改动。未无差别审阅窗外全文或验证隐藏历年目录。混元、DeepSeek和Kimi用真实官方入口修正原访问边界；MiniMax中英日期分别保留。依据见[官方目录恢复](../_sources/V3_OFFICIAL_DIRECTORY_RECOVERY.md)及[混元只读目录](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)。外部保留项与采用链路隔离；格式检查不代替语义验收。未stage、commit或push。

