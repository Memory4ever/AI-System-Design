# Daily Research — 2025-12-15

**规范：** V3
**窗口：** 2025-12-14T09:00:00+08:00 ～ 2025-12-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T22:52:59+08:00

## 1. 结论

十四每日来源、四arXiv主题检索与六个官方分类有界段已处理。DreamRAM、EEG voice、AnyMC3D及数据选择12932的误排撤销后，当前111个唯一精确v1/官方家族保留潜力；原18关闭撤销DreamRAM后17，再补Kimi CLI0.64核心及TRACER/ICD9实际题摘判断3项，共20。原题名14项中5项已有实际题摘/必要判断，剩9title-only；这是原有限集合修正而非新增论文发现。这不是本窗新论文数量：没有同时通过贡献与首次公开落窗依据的确定候选，不评分、不以日期缺失改成无贡献。

必要局部保留LLRC的rank calibration/压缩artifact差额，sandbox的本地rollback与外部effect边界，协商的selector/judge混杂，Memoria的recency/真值及成本分账，SignRAG的实时延迟反证和SoT的条件理论反例。模型表示/稀疏执行的Q-NeRF与TwinFormer未因领域标题排除；SFT/RL与loop负侧未删除。摘要完成不是Evidence完成。

LLRC条件草案对应`INFER-TENSORRT-LLM`；sandbox、协商、recency的拟保留边界实际正文已有覆盖，均仍受日期隔离，不冒称Books整合。root接手八项作者修正，已同步误排、Alignment/CLI来源段、Guardrail指标、RAMBO身份与同类题名局部校准；Popper来源边界和最终一致性回核通过，实际范围与限制见§6，不以旧ready或机器通过授内容完成。

## 2. 来源覆盖

本日实际原始请求、字段语义、纠正和停止位置见[SOURCE_SCREEN](../_sources/daily-20251215/SOURCE_SCREEN.md)。没有扫描周级来源，不从邻日结论或月级表套完成；有限历史缺段不是覆盖通过或机构零事件。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原RSS XML：Dec12 BBVA/Codex-SoraAndroid/BNY→Dec16 Images1.5/StayAhead及science的00/08/09GMT邻接 | 已检查 | 只所见Feed段，不授整机构召回；午夜字段不补精度 |
| SRC-ANTHROPIC | Research字段Dec4T17Z→Dec18T10:33Z→Dec19T19:45Z；增补实际Alignment December六项Dec19/16/12/8至November相邻段 | 已检查 | created/updated与子目录日字段不授firstpublic，只有限邻接，不授整机构零 |
| SRC-GOOGLE-AI | Research2025 Blog Dec12→Dec15STOC反馈→Dec18核心关闭；DeepMind page4/具名原字段；原生pubs category2025 checked，1–15/675、45页；Dec14/15两主题日期文本搜索200/0行，无后页 | 受阻 | pubs历史首公开切片未恢复，文本0非空日/覆盖；Blog不替论文入口，May18改名不冒充2025机制，月标签非日证据 |
| SRC-META-AI | 原Publications page4：Dec12 TIE→Dec16 audiovisual，下邻Dec1 RIFL | 已检查 | 收录非first-public，不扩无关版本/仓库 |
| SRC-QWEN | 新Blog skeleton/route home，本窗Dec14/15官方域有限替代 | 受阻 | 2025原目录缺段终态保留，不授零事件 |
| SRC-DEEPSEEK | 官方完整Change Log：Dec1 V3.2→2026Apr24 V4 | 已检查 | 只release日期段，未将普通仓库提交扩为Daily |
| SRC-MOONSHOT | 原平台Changelog Nov7/6→Oct27→Sept5至2024；已触发CLI0.64 Dec15原始CHANGELOG core定点复用实际校准，会话选择/MCP管理具体贡献前关闭 | 已检查 | 日标签非精确release；不授机构全部Github历史或新状态/授权语义 |
| SRC-TENCENT-HUNYUAN | 首查Research skeleton，浏览器不可用；原publicList code0/total9/list9，逐项publishedAt全部2026，有限官方域替代 | 受阻 | 2025动态All缺段终态隔离，不用当前九项推历史零 |
| SRC-ZAI | Research RSC本日15个含日期独立对象，2025 AutoGLM145/ASR149/TTS147三邻项；release后邻Dec22 | 已检查 | createAt午夜编码非first-public，release不替代Research历史召回 |
| SRC-BYTEDANCE-SEED | 2025 Paper/Blog各18条、next20/has_more；Paper1323→875，Blog1817→1504，pinned2141/1815单核 | 已检查 | 未扩94/45库存；Paper1323日编码相交未授公开，Blog1817精确Dec16T18:47:38是不同事件 |
| SRC-BAIDU-ERNIE | 原Blog实际Page2/2，Dec9 ERNIE5.0-1103→Dec23 ERNIE5.0-1203，下邻Nov21 | 已检查 | 排名题名不自动构成架构贡献，只目录段 |
| SRC-XIAOMI-MIMO | Paper八项May12/Jun4/Sep19/Oct21→2026Jan8/Feb3/Mar13/Jun29；Blog15标题/More及官方域限定替代 | 受阻 | 2025Blog必要旧链接/日期未恢复，终态保留 |
| SRC-MINIMAX | English Blog Oct27 M2→Dec23 M2.1；中文redirect边界，Agent Tech当前2026页 | 已检查 | Agent Tech2025相邻段未恢复，独立外部隔离，不拿当前页认证旧事件 |
| SRC-ARXIV | submitted_date_first Dec14–15，四主题model91/system27/multimodal44/agent20各单页；CL425/LG975/DC100/AI400/CV1400/AR50各show25，共150题名；相关/含糊exact-v1及必要局部，四误排已恢复、两标题具体关闭 | 受阻 | 当前111潜力first-public与日级历史召回未授；月ID/Submitted/常规排期非落窗证明，实际分层非当天新论文数量 |

补检：四组限定官方机构域Dec14/15日期查询、四组arxiv主题英文日标签查询未增新线索；三项首批ID官方域公告查询亦空。它们只是有限替代，不证明无事件。错误order/漏advanced返回失败或表单、初轮月列表引号解析0均已纠正，不记为空日，也未把宽目录变成全文库存任务。

## 3. 候选与判断

没有确定落窗候选。111潜在家族逐项身份与“原判断→具体增量→选择边界”见[ADMISSION](../_sources/daily-20251215/ADMISSION.md)，保留日期缺口，不降分删项，不以已读摘要授证据完成；共同标题误排理由已只在具名集合修正，未扩宽发现池。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

以下是日期未授材料的**必要准入/边界笔记**，不是正面当窗Evidence，也不是全部潜在材料已深审。详细实际打开位置、关键反证、现有段落与局部草案见[CORE_AND_BOOKS](../_sources/daily-20251215/CORE_AND_BOOKS.md)。

### [LLRC](https://arxiv.org/html/2512.13733v1)

实际§4.1–4.4/§5.1–5.2/§6.2/§7.1：训练mask而非原权重、蒸馏activation、二值后处理与低收益层dense回退；fine-tuning-free不等零训练，质量不等执行加速。`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)静态SVD/SoLA和动态rank前后段已实际读；现有论证不承载此mask calibration→artifact路径，条件插入草案已交root，日期恢复/独立核前暂缓，不称整合。

### [Fault-tolerant sandboxing](https://arxiv.org/html/2512.12806v1)

实际§4.2–4.3/§6.2–6.4/§7.5：copy模拟COW、exit code触发回滚/commit，只本地文件；80例全过、CLI auth摩擦不能授一般隔离，原文14.5%与4.69/6.51s不一致不采用。`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md)Preventive/Evidential Gate与staged filesystem段明确不可逆网络/进程effect，Ch81相邻COW成本/外部barrier已读。针对该责任边界是具体已有覆盖，整家族仍暂缓。

### [DeliberationBench](https://arxiv.org/html/2601.08835v1)

实际§3.1–3.3/§4.4/§5.4，强baseline selector与评价judge有重合、三弱council协议/QA/三seed局部；不把局部负面升级为协商无效。`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md)90–160实际含候选覆盖、可靠selector、judge/预算冻结与相关共识，Ch81/83交接已读。该拟保留归因边界已有覆盖，不因此排除新反证，当前Books暂缓。

### [Memoria](https://arxiv.org/html/2512.12686v1)

实际IV-E/VI-A–B：age/指数权重偏新，不授事实更新；148条QA和judge、同embedding下single retrieval对照更快，不能采普遍优势。`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)recency score后明确source/time/confidence/supersession与recency非真值，Ch76 ingestion identity/Ch78 effect commit已对读；该边界已有覆盖，Hindsight题摘不等四网已核，均暂缓。

### [SignRAG](https://arxiv.org/html/2512.12885v1) 与 [SoT](https://arxiv.org/html/2512.12777v1)

SignRAG实际III-A–D/IV-C：303项描述目录/top5匹配，100次latency含32.06s尾部，作者明确不适合实时；潜在表示/代价增量不因成熟pipeline关闭。SoT实际§3–5在pure-function/种子固定条件下给中间状态不唯一决定计算、编码与人类表面语义分离反例，明确承认derived KV；不是已观测所有LLM内部编码。Popper已核必要范围及潜力边界，first-public仍未授，不评分或正面采用。

Vision-enhanced LLM与annotation pipeline经各自HTML失败后必要PDF成功，实际核心仍为成熟模块/概念标签，未得可区分的新机制或评价协议，具体贡献前关闭见ADMISSION；这不是因有限访问或欠实验预算降分。Google STOC反馈原核心也已实际判，不留普通阅读待办。

DreamRAM12106的NN映射/DLOMAT/3D-HBM设计空间与EEG voice22146的EEG-to-mel、L1/CTC及spoken-to-imagined初始化恢复潜力：通用硬件或医学题名不能代替机制判断。分别不授实机LLM速度/能耗、安全或时间对齐消失/临床有效性。GuardrailAutoTune15782的良性侧指标是“输出被分类器判有害”，并非拒绝率；同分类器兼filter/judge及grid/Optuna样本预算不同，不能认证等预算加速或通用安全。15778当前原v1页为RAMBO，原COBRA抓取异名保留但不当历史版本事实。root复用Popper同身份/窄命题实际原源层，只同步上述差额，不冒称root阅读全文或运行实验。

同类标题误排的有限扩查又恢复AnyMC3D12887的in-plane/through-plane分工、各向异性/coverage与query pooling条件，以及12932的subset ERM/flatness、empirical Fisher近似和influence/coverage数据选择机制。它们分别改变表示融合和训练数据选择判断，不引入临床/BioFM科学应用，不授3D普遍优势或严格曲率等价；12932的晚于右端Submitted只排该v1本窗正文，不能猜更早first-public。TRACER12795和ICD9则按实际完整题摘/必要引导的领域既有方法关闭，不再凭医学标签排除。原源位置见[独立记录](../_sources/daily-20251215/ROOT_ADMISSION_REVIEW.md)，root仅复用同身份/窄命题校准。

## 5. 缺口与下一步

**普通作者与非作者内容差额：0；最终日级核验见§6。** 旧ready不作为完成依据；root已同步ADMISSION、来源与正式§1–5，独立§6由Popper维护。同类题名四项有限校准已同步，不扩全池或附件，不等待未知日期。

**外部终态保留：** ADMISSION当前111潜在家族均缺exact事件的first-public公告或完全落窗的正文公众可用区间。首批2601.08835/2512.13733/2512.12806官方域定点替代空，实际重读[ARXIV_DATE_RECOVERY](../_sources/ARXIV_DATE_RECOVERY.md)固定2025公告/Git、OAI字段和历史list/catchup/API有限失败；不重复同接口、不按月份ID或常规日程授实际公告。恢复需逐篇v1官方new RSS/email/list及标签时区/实际slot，或首次正文可用范围完全落窗；若确为EST20:00=次日BJT09:00，归再下一Daily而非右端内。材料到达仅重开对应家族，再真实评分、必要证据与Books核验。

Seed Paper1323 `PublishDate=1765728000000`是Dec15BJT午夜日编码，不补时刻；arxiv13507v1提交15日16:36:52UTC只排除此版本本窗，不否认早期Seed正文。Blog1817 `1765882058000`=Dec16BJT18:47:38为不同事件，窗外线索不扩任务。需要Paper1323原正文first-public区间，不能由Blog或Submitted替代。请求已与同家族合并，不重复。

Google pubs本窗历史首公开切片、Qwen/Hunyuan/MiMo原2025相邻历史目录、MiniMax Agent Tech旧段和arXiv日级公开召回均在有限原源/限定替代后隔离。pubs正确2025过滤及两主题日期文本搜索已实际处理，但文本0不是日粒度公开覆盖，不继续45页库存。接受原始历史目标段或具名相关事件及完全落窗公开区间，只定点重开受影响来源/家族。保留项不支持正面结论、Books、无遗漏、性能/安全保证，也不是Coverage/Evidence通过。晚于右端的个体提交下界与范围外题名只在ADMISSION保留，不授其他Daily归属、不阻塞本窗。

## 6. 复核

复核者：Popper（主线程委派的独立agent；非报告作者Gibbs/root、非Books写入者，不以共同chatID代表身份）
结论：通过

检查时间：2026-10-02T22:48:43+08:00。实际回读本日正式六部分、SOURCE_SCREEN/ADMISSION_CALIBRATION/ADMISSION/CORE_AND_BOOKS及作者八项同步；原109个新增完整v1题摘/字段逐段核验，15个身份/命题未变条目复用原始校准，再对EEG误排共同理由所涉12887/12932/12795/2601.09709实读完整题摘/必要局部，EEG另复用16日实际校准。实际表行111潜力、20关闭（18 arXiv及Google/CLI各1）、9只题名一致，未增加原发现identity，不当作本窗新论文或Evidence完成。

四原advanced查询实际完整单页91/27/44/20及无Next、六分类各25条固定切片首尾已核；Alignment December六条至November与CLI0.64完整core再核。Google pubs另独立原生核三URL：2025 checked、1–15/675/45页，两本窗日期主题文本搜索200/0/无Next；不把文本0授日覆盖、不扩675库存。必要原源边界、具名安全/反证、owner/相邻实际范围与位置见[独立记录](../_sources/daily-20251215/ROOT_ADMISSION_REVIEW.md)。负侧分层覆盖原arXiv关闭题摘及Vision-enhanced/Annotation必要正文；安全/纠错抽检Guardrail/FiFA/OneLeak/Laminar/RAMBO/CODEACROSTIC/Loops/SparseAnchoring，恢复DreamRAM/EEG/AnyMC3D/数据选择最小潜力，TRACER/ICD9按实际范围关闭，八项已落实，不引入临床/BioFM路线。LLRC的mask-calibration/artifact链不同于Ch49既有SVD/SoLA；sandbox/协商/recency的窄命题实际owner已覆盖，不把主题相似当整家族覆盖；所有日期hold仍暂缓Books，本日无Books写入需POST。

未全读潜力正文/附录/代码或复现实验，剩9题名未逐项取摘要；未认证整机构召回、全年历史或公开字节快照。日期/历史切片终态保留不用于正面证据、不进入Books、不支撑无遗漏或性能/安全保证，按§5精确定点条件重开，不等Coverage/Evidence通过。内容普通差额0，日级独立复核已通过；2026-10-02T22:52:59+08:00按root最新交接完成metadata，22:54:33已实际回核root收束的作者§1/4/5三句，仅引用本节实际通过，不改变本次判定，不重开内容或原源。最终完成态V3/本地引用一致性实际exit0，限定README/独立记录的diff空白及含未跟踪文件的逐行尾部空白检查均exit0；机器不替代本次语义验收。
