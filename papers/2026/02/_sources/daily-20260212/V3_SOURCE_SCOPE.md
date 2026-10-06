# 02/12 实际有限来源范围与停点

执行日：2026-10-04。窗口为北京时间 `[2026-02-11T09:00+08:00,2026-02-12T09:00+08:00)`。当前仍进行中；本文件只保留实际入口、查询和停止，不继承 legacy inventory 的来源完成、分母或筛选。没有把机构全年目录与分类月目录做逐项 mandatory queue。

## 机构入口

| ID | 实际入口/查询与停止 | 已取得结果及边界 |
| --- | --- | --- |
| SRC-OPENAI | `https://openai.com/research/`及官方 Research/news；官方域 Feb11 research 查询，实际research news 141行 | Forum活动无原机制；registered入口重定向未作历史完整目录。该段与有限查询已处理，目录历史召回检索受限，不授整个官网零事件。 |
| SRC-ANTHROPIC | `https://www.anthropic.com/research`当前10条、官方域February2026 research查询 | 当前Sep/Oct首屏不能恢复历史；Feb5 Opus线索窗外，停止而非扫全部发布史。历史目录缺段隔离，不支撑无遗漏。 |
| SRC-GOOGLE-AI | DeepMind研究入口/Google2026 pubs与官方域Feb11定点查询；最后精确`variable capacity scheduling`→官方Feb11 Blog | 1947条pubs仅日期/主题线索，不逐项读。Aletheia/DeepThink数学科学暂缓；调度Blog核心已读，是SPAA2025理论的重释而非本窗新的LLM机制，贡献关闭。Node pubs请求connect timeout、web exactyear internal error，保留有限检查边界。 |
| SRC-META-AI | Research空提取后 `https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3`日期夹窗；UniT官方页面完整AB | page3从Feb27/26/13到Feb11 UniT、Feb10 AIRS再Jan2，停止此历史段，不扫全部publication。UniT日期仅Feb11，arXiv2602.12279v1晚于窗口，Meta正文先行时刻待核；直连PDF web click internal error。该家族日期隔离，不记零。 |
| SRC-QWEN | qwenlm重定向qwen.ai；官方域Feb2026查询；`https://github.com/QwenLM`当前overview十仓库有限替代；GitHub org限定Feb11/12 language model查询 | 只见当前profile和Qwen-code普通周报线索，无本窗新增机制证据；当前repository update不等公开事件。历史目录缺段隔离，不作全GitHub commit/PR扫描。 |
| SRC-DEEPSEEK | 官网/官方news有限日期段 | news从Jun24 V4经Feb25 DualPath、Jan28OCR2、Jan12Engram到Dec31mHC夹窗，该可读段未见本窗新入口；不以此授官网全部无遗漏。 |
| SRC-MOONSHOT | Kimi Blog26条Nov2025及更早；官方域Feb2026查询；`https://github.com/MoonshotAI`研究/infra profile与十仓库首段；限定orgFeb11/12 language model查询 | stale Blog与当前profile不是历史release ledger，有限替代未得窗内原始新增说明，目录历史缺段隔离。K3/AttnRes等当前材料不反灌本窗。 |
| SRC-TENCENT-HUNYUAN | 官方Research空提取；IAB create/goto两次真实timeout；`https://github.com/Tencent-Hunyuan`pinned与十仓库overview；限定orgFeb11/12 language model查询 | 动态“全部”历史目录不能取得，GitHub当前首屏不足代替本窗，因此此必要覆盖缺段隔离，重开须可读本窗全部条目或官方本批记录；不把timeout写零。 |
| SRC-ZAI | Research400/timeout；官方release notes可读；`https://z.ai/blog/glm-5`官方indexed core，exactweb open0行 | GLM5 launch原增量仅规模/DSA复用/异步RL标签/成绩，未公开具体新异步机制，贡献关闭。后来2602.15763技术报告不反灌launch。Research历史目录缺段仍隔离。 |
| SRC-BYTEDANCE-SEED | public_papers page1/13当前Aug–May段；官方域Feb11查询；精确Seedance2 launch核心L23–124 | Seedance2仅功能、AV架构标签与demo/榜单，未辨识新增factorization/objective/sampler或可控物理证据，贡献关闭；未读其后来April报告以寻找本launch增量。13页不全量逐项扫描，历史目录缺段隔离。 |
| SRC-BAIDU-ERNIE | ERNIE中文Blog首屏11条May9至Nov21，Feb6/Jan29夹窗 | 已处理该可读历史段，本窗未见研究入口；不外推所有Paddle/ERNIE发布。 |
| SRC-XIAOMI-MIMO | MiMo主页Paper Mar13/Feb3/Jan8夹窗；当前Blog15条至More，标题段177–295实际读 | 已处理可读Paper历史段；Blog15当前条目无日期、不支持本窗完整历史，More非可读链接，历史目录缺段隔离而非普通未读或零命中。不以paper段代替全部Blog，不倒灌当前V2.5/V2.6。 |
| SRC-MINIMAX | 英中官方Blog及窗口定点查询，[M2.5 Feb12 launch](https://www.minimax.io/news/minimax-m25)核心与[中文Forge原稿](https://minimax.cn/blog/forge-scalable-agent-rl)精确字段恢复 | launch规模/标签未提供具体新机制而关闭；独立Forge核心§3.1有WindowedFIFO，不合并关闭。root实际原页L64–66 Feb12 date-only，与news Feb13/英文Blog Feb14冲突，整天不完全落窗，缺最早正文public时刻/完整包络而单独日期终态隔离，不计58、不支持Books。正文可读，不称机制未披露；取得时间界只重开此family，不倒灌后发稿。目录边界仅当前可读段。 |

## arXiv 主题与查询

已实际读cs.CL月列表1935条/17456行与cs.DC 287条/2384行中的本窗ID/相关标题切片，仅据ROADMAP主题取首批16及第二批45完整AB，不把545旧库存作强制队列。ID只是发现切片，归属仍逐项首公开包络，不称该ID范围都是本日新论文。两批AB在本目录独立保留；跨分类同家族只计一次。

2026-10-04本轮有界补检：web官方域查询`"2026-02-11" transformer runtime`、`"2026-02-11" world model foundation`、`"2026-02-11" retrieval agent memory`未返回结果，搜索零不证明分类零。API按submitted排程proxy `[202602091900 TO 202602101900]`，`start=0/max_results=60/sortBy=submittedDate/ascending`；这不是实际公开时间条件。四组实际查询：

- cs.LG/cs.AI：title或abstract的language model / transformer / foundation model / agent / reasoning；HTTP429 Rate exceeded。
- cs.CV/cs.RO：multimodal / world model / vision-language-action / VLA / diffusion transformer；请求失败，未取得结果。
- cs.AR/cs.PL/cs.OS/cs.PF：language model / LLM / GPU / inference / transformer；请求失败，未取得结果。
- cs.IR/cs.MA：language model / LLM / agent / retrieval augmented / memory；HTTP429 Rate exceeded。

Exact web list补检 `cs.LG/2026-02?skip=900&show=100`、`cs.AR/cs.OS/cs.MA/2026-02?show=200`均Cache miss；不得写已检查无命中。一次官方Node month列表恢复实际成功：AR118、PL74、OS17、PF39、IR453、MA256条；只取发现ID09063–10116的相关标题（IR19、MA8）作有界查漏，不把ID当日期判据、不把全部分类或月表变成题摘队列。AR的09410仅领域PQC硬件应用、09554一般异构数据、09174一般PIM图；PL09197一般协议、PF09473微服务LB，标题范围明确不服务大模型计算，简记关闭；OS09345为已读家族，不重复。

同轮LG `skip=2000&show=2000`实际2000/4672条（发现ID片段57标题）、AI `skip=0&show=2000`实际2000（片段30）、CV `skip=0&show=2000`实际2000（片段97）、RO `skip=0&show=2000`实际1081（片段51）。这四份只浏览ROADMAP生成/基础模型/物理VLA/Agent机制相关标题以查漏，没有全分类题摘关闭。实际定点读8个IR/MA与12个LG/AI完整题摘，保存在[V3_BOUND_TITLE_FULL_AB.md](./V3_BOUND_TITLE_FULL_AB.md)，root已独立读20原文：7具体关闭、13窄增量继续必要审阅；没有因标题潜力先保留或打分。另已读09112/09286/09485/09794/10063完整AB作明确工具组合/社会统计/未辨识新可靠性条件关闭线索，保留其原字段后抽检，不算候选。

**停止位置：** root于本次20题摘校准后明确终止来源补检；不追加上述相关标题为强制队列，不循环新同义查询，不声称全部月表已逐项审阅或互联网无遗漏。有限主题/API尝试与这次官方标题补检均已执行；API失败和未覆盖月页限制保留。新增13与原45的必要日期/证据/处置已独立核到安全终态，最终冻结58，不用取题名行数充候选分母；整日最终稿仍待root验收。
