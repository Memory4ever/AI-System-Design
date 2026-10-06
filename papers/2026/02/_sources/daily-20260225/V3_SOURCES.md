# 02/25 有限来源停止与原始排除

执行日期：2026-10-05；窗口：[2026-02-24T09:00:00+08:00,2026-02-25T09:00:00+08:00)。本记录只处理每日14源及同身份必要日期/正文恢复，不借其他日期材料，不继承旧完成标签。目录当前保留范围不等于历史全集，HTTP200、零搜索或空分页不证明无事件。全部保存的 V3_NATIVE_* 为本日原响应；日期缺口为本窗终态隔离，不支持正面候选、Books 或无遗漏。

## 来源与实际停止

| 来源 | 实际入口、范围与停止位置 | 结果与缺口 |
| --- | --- | --- |
| SRC-OPENAI | Research/RSS（V3_NATIVE_openai.txt），1245条日期跨2015–2026；窗口筛出 Feb25 00:00GMT 的恶意使用报告。官方文章→同身份37页PDF只必要p1–6。 | 原始贡献排除见下文；本窗未纳候选。Feb24 HR任命非研究，Feb23 SWE-bench/Frontier Alliance 窗外。 |
| SRC-ANTHROPIC | Research SSR embedded publishedOn，174记录/166唯一，2021–2026；实际解析日期，近窗Feb23 fluency/persona早于下界、Feb25 20:02Z deprecation晚于上界。 | 所保留带日期研究目录本窗无命中，不声称未保留历史材料不存在。 |
| SRC-GOOGLE-AI | Research实际导航 /blog/2026→/blog/2026/02；月页7条，Feb17→Feb3已读标题/日期，无Feb24。Publications年页及DeepMind当前研究页另核。 | Research月Blog已检查；Publications/DeepMind缺本窗带日期发布批次，受阻终态，不把当前页或搜索0作无研究。 |
| SRC-META-AI | 官方Research当前页与本窗定向补检，当前Muse等公开内容不能恢复Feb24历史批次。 | 受阻终态：需目标窗官方dated研究列表/可信快照。 |
| SRC-QWEN | qwenlm旧页5条止2025-07/09；跟实际qwen.ai bundle到 /api/v2/article/retrieval?type=qwen_ai&language=en-US；40篇日期2025-11→2026-09，全部日期读完，本窗无记录。旧page_config research60/news17只是更早目录，非零命中依据。 | V2保留目录已检查，本窗无保留命中；不宣称未保留发布不存在。 |
| SRC-DEEPSEEK | 官网当前V4.1；官方org repos按created倒序一页100，未发现Feb新建repository。 | 受阻终态：repository created/updated不等研究首公开，缺本窗dated官方研究发布/快照。不遍历commit史。 |
| SRC-MOONSHOT | Kimi Platform Blog现保留25条，2025-11→2024-05；官方org repos created倒序一页100，Feb6 kimi-agent-rs只是creation。 | 受阻终态：缺2026本窗dated研究/技术博客历史列表或快照；不把旧Blog最后日期当无新研究。 |
| SRC-TENCENT-HUNYUAN | 官方Research动态页→实际JS公开 /api/blog/publicList，page1/pageSize1000/render0；total9且9条题名日期已读。 | 已检查现保留9条，无Feb24记录；不把该保留目录称完整机构历史。 |
| SRC-ZAI | 官方Research保留15条，2025-12→2026-08；近窗Feb21 GLM5→Feb11→Feb2；Release Notes辅助同身份/版本。 | 已检查现保留研究/说明，本窗无保留命中；不展开组织全部release。 |
| SRC-BYTEDANCE-SEED | 实际JS /api/get_article_list_v2；paper type1/publish_year2026/count20/page_token60，19条Feb27→Jan27；offset100空但total82，不拿空证明无事件。Blog type2当页12条，最近Feb14/13/12跨过窗口；total23/has_more与offset20空表示语言/保留限制，不宣称23全读。 | 两篇catalog Feb25日标签只日期hold，见下文；其他保留目录无本窗新增。完整首次公开身份需dated原页/快照，不能用April UpdateTime倒造February首公开。 |
| SRC-BAIDU-ERNIE | 官方技术Blog当前10条，近窗Feb6 ERNIE5→Jan29后到2025；标题日期到跨过窗口停止。 | 已检查现保留目录，无本窗记录，不扩旧页。 |
| SRC-XIAOMI-MIMO | 官网Paper8条，Jun29/Mar13→Feb3 HySparse→Jan8；Blog15标题，实际JS读取可用frontmatter日期（Jun/May/Sep→2025-12），若干自定义model页面无日期；官方org一页18 repos辅助。 | Paper保留目录已检查；部分Blog exact publication缺失，受阻终态，repo creation不修复发布日期。 |
| SRC-MINIMAX | EN Blog12、CN13；近窗Feb14 Forge/Feb12 M2.5→Jan27跨过窗口，技术题名/日期实际读。 | 已检查这两种语言现保留目录，无本窗记录；不遍历机构历年或把产品版本当贡献。 |
| SRC-ARXIV | 本日库存相关标题命名查漏；CL/LG/DC/AI及CV/RO/AR/PL/OS/PF/IR/MA的模型训练、表示、attention/MoE、cache/precision/hardware、RAG/memory/Agent执行验证、生成/world/VLA主题。官方cs月份skip8000/10000/12000只补相关命名，914 inventory及13905月总数不是逐项关闭队列。首批33潜力+代表EX、后批67选题摘、末批相关题摘三文件保留实际停止。 | 34同身份日期桥成立并必要审阅完；其余明确贡献排除与日期hold分开。官方历史按日公告不能恢复，隔离为无遗漏覆盖断言缺口，不抹掉有效34证据。 |

动态入口没有重复announced_date查询、全月候选扩扫、完整版本史或为证明“无事件”遍历全站。只恢复已观察到的页面/API与同身份时间字段，得到有限判断即停。

## 原始贡献排除：OpenAI February 2026 malicious use report

原始：[官方文章](https://openai.com/index/disrupting-malicious-ai-uses/) / [同身份PDF](https://cdn.openai.com/pdf/df438d70-e3fe-4a6c-a403-ff632def8f79/disrupting-malicious-uses-of-ai.pdf)。RSS pubDate=2026-02-25T00:00:00GMT（BJT08:00，窗内）。作者与非作者root实际必要p1–6，非37页案件全读。

多模型、多平台协作、分发/参与度与拒绝后离站活动是恶意workflow观测案例；原报告依据用户自述status和limited OSINT，不能把refusal后改用其他工具称受控实验的阻断效果，也不能把分发条件差异引起的engagement归为AI内容因果。核心未新增可检验的系统执行、检测或控制机制，仅案例与成熟分发配合；本项目贡献明确排除，不评分/不进候选或Books。保留安全观察来源与权限限制，不以“没有production”或缺LLM关系排除。必要核心足够即停，不建逐案件队列。

## Seed 两条日期保留（不授本窗候选）

- [World Guidance / 2602.22010v1](https://arxiv.org/abs/2602.22010v1)：完整题摘可潜在改变未来条件表示与动作推断接口；catalog PublishDate=1771948800000（2026-02-24T16:00:00Z，BJT25日00:00），UpdateTime=1776933055000（April23）。精确abs v1 Submitted=2026-02-25T15:27:09Z，已晚于本窗结束；catalog日标签不证明此版本在窗内首公开。保留原文对应身份，缺dated原project/paper首公开或可信snapshot。
- [FlowPortrait / 2603.00159v1](https://arxiv.org/abs/2603.00159v1)：完整题摘为MLLM分项评价+composite reward/GRPO的音视频后训练潜力，仍需贡献/关键对照核；catalog相同PublishDate，UpdateTime=1776928463000（April23），精确abs v1 Submitted=2026-02-25T22:08:15Z。同样缺原版本更早dated首公开证据；不从更新时刻、ID月份或目录回填授2月窗内事件。

只重开可恢复的首次正文事件，不为这两条日期hold开展Evidence/Books，也不顺带启动其他日期。

## arXiv 同身份桥

原字段来自本日已有同身份DataCite快照，只按34精确ID抽取，不接受旧inventory的announcement/Updated授日期。官方[availability](https://info.arxiv.org/help/availability.html) Fri14→Mon14 ET提交批在Mon20 ET公告，前批最晚Fri14；因此 Submitted:v1 晚于2026-02-20T19:00:00Z排除更早公共批次，且同ID Registered早于2026-02-25T01:00:00Z给予窗内公共上界。Submitted不等public，Registered只给上界，不补下界；Created/Updated绝不替代。报告范围从2026-02-24T09:00:00+08:00至Registered原秒的下一秒（仅为半开范围容纳原字段秒精度，并非虚构发表时刻），完全落窗。

早Submitted首批20+18511需dated公告；后批49、末批所列与once线索晚Registered需确切公开上界。具体身份与原贡献见 V3_ADMISSION.md / V3_ADMISSION_BATCH2.md / V3_ADMISSION_BATCH3.md。所有datehold隔离，不支持候选、Books或“已经全量去重审完”声明；有相应dated官方公告/可信历史快照时只重开该身份。

