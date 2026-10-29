# 2026-06-10 增量补查（2026-10-25）

当前行政状态：新增36I均唯一实际POST通过、普通扫描/筛选/必要/Books待办0；jun10_review唯一日级语义验收§81已实际存为通过，作者仅据其同步README完成。最终完成态V3机器与限定diffcheck通过；原窗口/候选日期评分保护，八日期未决/七中心H及UltraFlash局部H精确隔离，不授全部来源恢复/无遗漏。下文准备阶段待核与‘最终还须验收’是保留过程，不替代当前六节与唯一§81事实。

## 范围与恢复

本日独立读取 AGENTS、当前 RESEARCH_CONTRACT、RESEARCH_SOURCES 使用说明/每日/arXiv、REPORT_CONTRACTS、统一 Prompt、ROADMAP；State仅路由。保留原 `[2026-06-09 09:00,2026-06-10 09:00) BJT` 与两既有发布家族及有效正文，新增检查Jun09 BJT自然日。日报作者仅写本日README/本目录；共享Books另按root逐篇具体窄位授权保存，未获授权不写，不扫描Weekly/Live/2025/缺失日，不stage/commit/push。

旧52项 DateHold不是自动候选、全篇或日期请求队列。用具名正控2606.09863验证当前联合日证：唯一v1 Submitted=2026-06-01T00:13:23Z、registered=2026-06-10T01:52:41Z、findable/arxiv.content，最早—最晚跨日，故仍不证明其在某个单一自然日公告。原件 `SUP_DATACITE_POSITIVE_20261025.json`；不能将Created改名registered或硬搬入本次Jun09。

## 发现查询与停止范围

DataCite `https://api.datacite.org/dois` 使用独立参数 `client-id=arxiv.content`、`query=registered:[2026-06-08T16:00:00Z TO 2026-06-09T15:59:59Z]`，先正控再查询。跨学科宽标题请求total=2312、首1000且next存在，只作查漏线索，未声称遍历2312或1000逐项关闭；首次全字段请求35秒下载不完整（`SUP_DATACITE_REGISTERED_JUN09_20261025.json`）无分析权限，以后续有效主题请求取代，不把截断JSON算零。

针对本项目收窄四个title主题入口，均page[size]=250、page1、next=null；原件保留日期/题摘，当前元数据可能是后版，证据审阅使用exact-v1：

- MODEL：`titles.title:("language model" OR "foundation model" OR transformer OR "mixture of experts" OR pretraining OR "pre-training" OR "post-training" OR "reinforcement learning" OR attention)`，105返回。
- SYSTEM：`titles.title:("LLM" OR "GPU" OR "KV cache" OR "distributed training" OR "inference" OR "kernel" OR "accelerator" OR "communication")`，145返回。
- AGENT：`titles.title:("agent" OR "reasoning" OR "RAG" OR "retrieval" OR "memory")`，171返回。
- MULTI：`titles.title:("multimodal" OR "vision-language" OR "world model" OR "diffusion" OR "video generation" OR "robot" OR "VLA")`，138返回。

四组跨源按DOI去重483，其中部分“inference/kernel/diffusion/agent”是统计、数学、领域应用或传统控制，不能全变项目逐篇关闭队列。下一层围绕真正涉及模型计算、训练、执行、评价和动作闭环的语义线索补读；关键词只发现，不决定准入。不会机械排除小模型、局部、负面或理论结果。

## 首批题摘准入校准（原拟判历史；当前层见下）

题摘已完整读取，以下拟入选的贡献理由已交root独立校准。各项exact DataCite原件与v1 HTML/abs均保留；四项当前组合日证均为Jun09，最终采用须同时检查v1及撤回/修订信号。

| 身份 | 具体增量与拟评分 | 当前证据范围 |
| --- | --- | --- |
| 2606.09613 AgentServeSim | request流无法表达turn依赖、tool gap与跨turn KV；program orchestrator/router/residency模型用于受限counterfactual；2+2+2=6 | 当前元数据标题/摘要已是后版；v1真标题为*A Hardware-aware Simulator for Multi-Turn LLM Agent Serving*，不采用后版自动policy search命题 |
| 2606.09080 Beyond FLOPs | 统一GEMM M/N/K和一致实现，使剪枝FLOPs减少与真实速度/质量Pareto可分；2+2+2=6 | 待核v1设置/直接反侧 |
| 2606.08761 APEX4 | 同W4A4 g128在不同GPU发生速度反转，intra-SM TC/CC失衡和粒度适配可改量化执行选择；3+2+2=7 | 待核v1控制变量/瓶颈及端到端边界 |
| 2606.08635 SpectrumKV | PD KV传输由保留/丢弃改为token级精度分配，模型INT4灾难必须有fallback；2+2+2=6 | 待核probe盲区、transfer timing非完整部署SLO |

代表明确排除：JAX-AMG 2606.09001是通用稀疏线性solver；SynIM 2606.07759是天文自适应光学interaction/tomography矩阵。两者未由题摘提供大模型训练/推理的具体计算增量，不能仅GPU/kernel词语准入。医学、材料、气象等已有方法应用不因foundation model术语重新进入暂缓AI-for-Science。

上表原拟判保留；独立校准APEX4为2+2+2=6，硬件相关/速度反转本身非D3，未因此减少必要域。首4已完成必要与实际owner独核，前三已真实保存且唯一POST通过，Spectrum预算/对照身份中心争议隔离。后续累计36新增I已唯一非作者POST通过；完成层、具体E与尚未完成层以README六节及唯一`SUP_REVIEW_20261025.md`当前内容为准，不继承上表“待核”历史进度。

理论/反证边界项已读题摘，不因未测GPU而排除：2606.07713 MoA attention宣称memory-minimal theorem、性能数只是模型projection；2606.07600 Gaussian Transformer reachability有明确Gaussian/mean-field/affine条件。其submitted→registered跨日时应保留日期未决，而不是把registry登记日直接当公告日。已知先前正文/实质修订信号仍须具体处理。

## 来源目录进展

- Qwen新官方article retrieval分别en-US/zh-CN，40/40完整响应，内容内published time可读到2026；两语言均有Qwen3.7-Plus Jun01T10:00+08，故目标邻接为Jun01→Jun16无Jun09（原May29说明经独核机械纠正）。解除旧“最新仅2025”的特定故障，不宣称机构未收录材料不存在。
- Hunyuan官方publicList POST pageNum1/pageSize100/renderType0、accept-language zh：code0,totalNum11,list11，已核原publicAt/publishedAt分账；publicAt Jul06与May21/Apr30之间无Jun09。显示/正文日期不替代事件字段。
- Anthropic listing415768字符内137条可解析title/publishedOn，Jun11/12附近；default/2实际NotFound不是第二页覆盖。Jun09 Fable已定点完整核心/当前card必要域恢复与具体E核，不扩全317页/版本史；后修不能倒填Jun09。
- Google Publications实际首15/11637只有year无日级排序；旧GenAI/NLP/ML各12线索有效保留，官网Jun09主题/日期补检未给原批次，不拿DeepMind教育RCT Blog替代Publications日级覆盖。该批次具名外部隔离，不签零研究。
- Meta publications直接网络reset，web入口仅“content unavailable”；这是实际故障，不是已检查零研究。
- Seed当前page1/13首20/246，Jun11→Jun04→Jun03→May29已越本窗，无Jun09；不扩13页。
- Z.ai Research首14项Jun16→May20已越本窗。Baidu首10/page1-of2最新May09，越过本窗。
- Moonshot Blog27条止2025-11、旧Kimi两事件可核实复用；不继承Blog全历史覆盖。
- MiniMax英/中文目录均Jun09 MaxProof→Jun01→May27/25，旧家族有效必要证据复用；AgentTech实际可见5篇为Oct20两篇/Oct08/Sep22/Sep19，停止完整可见列表，解除旧两壳故障但不授全部历史覆盖。
- MiMo官方model release页Sep22→Jun02→Apr23无Jun09，主页Paper8/Blog15有限检查；UltraSpeed原Jun08与Jun09 trial不能互换，历史zone/dated批次仍隔离，不制造新候选。

官方arXiv分类标题有界补检原件为`SUP_ARXIV_API_{CORE,SYS,MULTI,AGENT}_20261025.xml`：submittedDate窗口[202606051800 TO202606081800]仅发现不当公告证，CORE(CL/LG/AI+语言模型等)首50/365；SYS(DC/AR/PL/OS/PF+LLM/GPU等)19/19；MULTI(CV/RO+foundation/world/VLA)首50/60；AGENT(IR/MA+LLM/language)30/30。实际读这些返回标题、跨主题按ID去重，再对可能贡献读完整题摘；不称149唯一身份，也不因有XML将365/60后页变整分类关闭队列。四主题DataCite的有限完整页与此相关标题browse互补，不授全学科召回。

## 续跑

本文件不是终态复核，作者不自签。当前36I已POST，所有具名标准必要/actualowner及Books普通0；第6批七限定I均已POST，Uni-E中心H已独核，UltraFlash同家族的controller/perf子命题仍隔离不重复计数。七精准gate与原四gate已收束：成熟recipe preN、SEMJ/PPV4分关闭、DCPM/09388继续6、08162新定量claim6/H分层；原拟判/新依据见BATCH5，不以工作量缩池。八个日期未决潜贡献（补回B2既见07726）已作有限必要替代，准确月目录`/list/cs.LG/2606?skip=0&show=2000`本轮实际HTTP404（`SUP_DATE_MONTHLG_20261026.headers/html`），不是空批次；作者页/正式会议/OpenReview可得日证仍不闭合，07726/07527更早正文信号保留，交reader确认具名隔离，不以任何单字段或第三方日期搬日。没有把宽483或旧52逐项冻结成全文队列；目前仅剩最终六节机器与一次日级验收，不将实际普通未做改名外阻。

## 最终来源/筛选边界交核（技术层仍按单篇进行）

到期14来源实际边界为上文与README §2，Google Research目标日批次、Meta历史目录及MiMo UltraSpeed日期/zone缺口只具名隔离，不支撑零研究、正面Coverage或新Books；旧两发布家族有效证据保留，旧小时窗通过不充本轮验收。Moonshot当前Blog有限切片与已有release证据也不充完整机构历史。无新按需全站/Weekly扫描。

非候选明确排除已分层：范围层JAX-AMG09001/SynIM07759为通用PDE/天文AO（reader首批已核）；模型描述层09287仅短prompt几何差异/未改变选择、09646仅family/layer/probe排序，均代表独核；Agent/训练局部recipe层08543/08158/08151/08348/07950/09315/07904/08588/07846/08661与VLA09827/对齐08788均按各具名决定点经reader核，不因小模型、观测/理论或局部负面一律排。该样本覆盖范围、无新重要增量、成熟模块配方及含糊后关闭的理由；不称全483排除全核。原排除文本、拟判→纠偏、反证原件都保留。原候选SEMJ/PPV有小原比较增量，4分关闭，与贡献门前N分开。

四主题DataCite各已完整有限页、官方相关分类browse实际返回149条非唯一标题；CORE50/365与MULTI50/60后页未逐项读、未覆盖所有分类或所有语言同义命名。这个停止点在当前主题有界补检范围内，不将宽目录/旧52转队列；已见具名范围的完整AB、日期与准入在本文件及BATCH2–6/本日独核复用。最终日级还须实际六节/机器与唯一非writer日级验收，不因本节形成即通过。07726漏同步已补原字段/精确候选potential与ICML后发表/作者yearonly/OpenReview更早信号及403阻断，不重抓全部日期家族；完整见BATCH6末节。
