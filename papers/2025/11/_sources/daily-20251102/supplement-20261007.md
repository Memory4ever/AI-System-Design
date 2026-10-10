# 2025-11-02 增量补查

作者：Darwin（本轮分工，落盘署Codex本会话）。启动已重新读取AGENTS规定的研究/Report合同、Source使用说明与每日14源/arXiv范围、Prompt、ROADMAP及State路由，只加载Nov02原报告、STOP、DAY_REVIEW与PLOTCRAFT_POINT_REVIEW。旧窗口、0确定候选及有效审阅冻结，新增窗口2025-11-01自然日；不从其他日报复制发现、候选或完成声明。

原报告完整档案：[原报告](original-report-before-supplement-20261007.md)。原始材料不覆盖。可复用root旧PlotCraft exact-v1指定章节/直接表与反侧及具体owner比较；潜力不能改回范围关闭，具体公开日仍需核验，已有证据不无差别重读。旧原报告完成仅指原轮，不授本轮日级通过。

本轮每日源实际查询已完成有界处理，请求及执行时刻保存于独立`supplement-20261007/`，每个请求的身份/HTTP/分页停止自足。禁止catchup；Advanced公告仅年月的条目按日期潜力隔离，不用submitted填公开日。原始命中、完整题摘、候选、必要证据分别计；宽列表不作强制题摘/全文队列。当前Bernoulli最终DAY PASS与作者完成态同步见文末；首批FAIL、返修READY及执行快照保留为历史，不作为最新待办。

只拥有Nov02 README和同日_sources，不改Oct02、State、Books、合同、索引，不执行Git写操作。共享Books若出现长效差额先交必要证据与唯一owner提案，由root写；准备的新增准入/代表排除先交独立校准，作者不自授DAY。

## 实际来源与停止

实际请求执行2026-10-07T18:16:50～18:39:38+08:00，逐请求UTC开始/结束、URL、method/body、HTTP、字节与redirect在[supplement-20261007](supplement-20261007/)每份receipt，均为本日新请求，不复制其他日响应。Google/Meta浏览来源实际响应另存`web-google-meta.json`。十四每日源均已实际有限检查；以下状态只是实际范围，不授全源历史完整性。

| 来源 | 本轮实际检查、分页停止 | 结果与权限 |
| --- | --- | --- |
| SRC-OPENAI | 官方RSS HTTP200，1251 item全解析；BJT10/30三项→11/03 14:00 AWS→11/04 06:30 IndQA邻接，11/01自然日0 item。 | 返回feed有限检查；不证明历史删除或全部论文/修订。 |
| SRC-ANTHROPIC | Research HTTP200，当前实际RSC publicationList的posts为171（不是其他日172）；逐publishedOn，10/29 introspection→11/05 deprecation（UTC11/04 16:00）跨补窗，11/01无条目。 | 当前返回结构化目录已检查；不把CMS created/updated当公开或证明删除史。 |
| SRC-GOOGLE-AI | Nov月Blog直接fetch失败，但官方web实际读10条Nov21→Nov04至末，无继续列表；pubs默认页可读，年份/正式发表非首次公开。DeepMind Publications实际p1/p2各30精选卡，p2首Oct30，只有有限selection。 | Blog已检查；Research首次公开日仍具体限制，不把默认页/两真实页整体记不可达，也不排队年度库存。 |
| SRC-META-AI | 官方Research web真实提取0行。 | 未恢复目标历史段，受阻隔离；不将空提取当0论文，未扩其他日Rule of Two候选。 |
| SRC-QWEN | 官方page_config接口HTTP200，60项date/title/id，日期范围2022-11-14～2025-12-23；目标邻接Sep24 Max与BJTNov13 DeepResearch，无分页字段；11/01无返回项。 | 原迁移接口普通恢复已做；不能再沿用“未读取API”，当前返回不证明删改史。 |
| SRC-DEEPSEEK | 官方首页及updates实际HTTP200；updates Dec01→Sep29跨补窗，页面延至2024旧段、无继续分页。 | 有限发布切片已检查；更新说明不是全机构研究目录。 |
| SRC-MOONSHOT | Kimi Blog实际26条，Nov07/Nov06→Sep16；尾May29_2024、无Next。 | 当前完整返回Blog有限检查；无补窗条目，不扫组织普通PR。 |
| SRC-TENCENT-HUNYUAN | Research HTTP200动态壳；CUA本轮iab不可用，浏览器清单为空，并非已浏览成功。对原已确认官方publicList独立POST page1/size1000/renderType0，code0、totalNum9/list9，publicAt/displayPublishTime/publishedAt分开，最早2026-Feb03。 | API有限恢复真实成功；2025目标历史段仍受阻，不将未读论文称外部故障，不授旧库存0事件。 |
| SRC-ZAI | Research实际首/page2，两页200；page2 nextPage3/hasMore=false/“没有更多”，末Dec07_2025。 | 当前末段已核；11月研究段仍缺，不能用hasMore=false授历史零发布。 |
| SRC-BYTEDANCE-SEED | 实际type1/type2、US locale、year2025/count20/order_desc=true/token0，各18条；total94/45，next20/has_more=true。papers返回Dec01与Oct22邻接，Dec01 GR-RL ID875的IsPinned=true/PinTab=[10,3]；Blog Nov27→Oct23，至Jun26/25；未请求token20。 | 未验证PinTab页面呈现，不称非置顶锚点；不借旧p20响应充本轮分页，置顶/排序和删改限制不授全目录。 |
| SRC-BAIDU-ERNIE | 中文Blog首/末2页实际200，末页Nov11→Nov07→Oct16，尾Jun30，2/2停止。 | 有限目录已检查；版本名1103/1022不是发布日期，不变候选。 |
| SRC-XIAOMI-MIMO | 首页Paper8/Blog15，路线JS与本页preload实际映射的8557/6159组件200；More为initialVisibleCount8、本地slice后7、state切换，无分页。实际八无日期card原链接7～14全HTTP200，ASR/TTS仅April2026、V2.5/Pro Apr22/27、V2-Pro/Omni/TTS Mar18、Flash Dec16_2025。其余具名Blog元数据Jun08/10、May30、Sep27_2026及HSS Dec19_2025，安全路由Dec18_2025。 | 原More普通核查关闭，不声称全部删除史；V2.6系列链接实际只返回动态壳，未确认该具名页日期，记录真实限制而非由版本名补造日期。 |
| SRC-MINIMAX | 英文Blog实际200，Dec23_2025→Oct27_2025跨目标日；Agent TechBlog md实际200，重定向minimax.cn，唯一May13_2026条目到末。 | 有限返回切片已检查，非全部隐藏/删改/仓库历史。 |
| SRC-ARXIV | 下节四独立Advanced响应176次/175唯一；另cs.DC November首25/338标题补检，停skip0；26新完整题摘及两项撤回定点回源。 | 有界主题发现已实际推进，不用catchup；公告年月不授权Nov01具体日，首批独立校准已到、R1～R3已写回待窄核，未授日级覆盖。 |

## arXiv 有界发现和计数

首试`arxiv-model.html`把OR串放在同一all term并把“originally announced November 2025”当全文短语，实际HTTP200空结果；没有通过正对照，不用于零发布/排除。随后复用现有解析工具代码，但不载入他日候选或数据，按本日新请求执行Advanced：`announced_date_first`、from Nov01/to Dec01、size50/start0、升序，多个独立title term用OR（具体URL在每份新receipt及本日arxiv-query.mjs）。返回实际身份首公告字段均November2025；这只界定发现月份，不判具体日，也不查全月。

- 模型：MoE/SSM/reward model/preference optimization/test-time scaling/model merging，1～50/120，有Next，停首段。
- 系统：speculative decoding/prefill/disaggregated/distributed training/inference serving/LLM compiler，1～26/26，无Next，到末。
- 多模态：video generation/vision language model/flow matching/embodied/world model，1～50/312，有Next，停首段。
- Agent：RAG/agent memory/prompt injection/computer use/multi-agent language，1～50/66，有Next，停首段。

四响应共176次，按无版本ID去重175，唯一跨组重复为Reg-DPO。176标题浏览与metadata/标记机械提取不是176题摘审阅。不能相加120/26/312/66作为“当天贡献”。首段与Next是有限查询停止，不变成月级逐项全文义务；本日不宣称全分类召回。

题摘定点选择先用v1提交邻近/更早作为发现路由（不是公开日期或准入规则），并轻量处理已见纠错；本次实际完整读23个唯一题摘：[解析身份与完整摘要](supplement-20261007/parsed-discovery.json)的selected_for_complete_abstract可逐ID核，原HTML保持。更晚提交的其余月身份不称已审或范围关闭；迟公告的04700/05494/08600等未凭编号顺序漏掉。原175发现不含PlotCraft，原材料在本日已知，当前abs只为版本/纠错检查，不增加发现/候选或把v2自动当重要修订。

官方[cs.DC November](https://arxiv.org/list/cs.DC/2025-11?skip=0&show=25)实际首25标题、全月338；只浏览本段，不将其余313变队列。定点新读EPARA/AReaL-Hex/FREESH三份完整题摘及版本史，原abs各保存，三项不在175查询池。共26个新身份完整题摘（23+3），不含原PlotCraft证据复用。不是26当窗候选/必要证据完成。没有新增已确认当窗候选或评分、没有新arXiv全文读取、没有Books采用/写入。

## 26 项题摘处置：独立校准交接

下表全部已读完整题摘，身份为arXiv对应ID，官方URL均为`https://arxiv.org/abs/<ID>`；23项原文在parsed-discovery/四raw HTML，另三项在具名abs。潜力/准入事实未决不先列候选；当前版本题摘不倒填2025-v1。

| ID / 家族 | 拟处置及具体差额/必要反侧 |
| --- | --- |
| 2511.00447 DRIP | 必要安全潜力：token-wise embedding编辑与residual instruction分支针对数据/指令混淆；“不可覆盖”、adaptive成功率及utility保持不当安全保证。 |
| 2511.00505 Zero-RAG | 潜力：按模型知识mastery剪语料、query router/noise-tolerant tuning改变索引与内知识边界；删知识可造成更新/可靠性代价，30%/22%不采用。 |
| 2511.00678 ReDeFix | C贡献关闭，复用Bernoulli校准：SO知识+RLF context提示生成CSS补丁，题摘仅应用组合/修复准确率，未给新的修复规则或可复用失效条件；不凭CSS领域标签关闭。 |
| 2511.04700 WinnowRAG | 潜力：query-aware分群、多agent答案、critic winnowing与merge保留有用文档，区别于简单增检索数量；成本/有效性归因未核。 |
| 2511.05494 CRAGRU | P维持/中心争议：Bernoulli已读v1 §III-B/IV及V开头，三策略不再全部未知。直接检索过滤未消除底模参数→Top-K候选/辅助信息→生成的依赖侧路，不推出全链条件独立/重训练等价，不授完全遗忘或合规保证；详见文末R2。 |
| 2511.08600 SLP vignettes | C贡献关闭，复用Bernoulli校准：领域RAG+模板教育病例可行性与rubric，未披露改变主线的新一般机制或评价盲区证据；专业验证尚需进行不是已证实系统安全反证。不授临床/隐私保证。 |
| 2511.00040 SSPO | 理论/训练潜力：少量paired+unpaired与reward threshold伪标注；需要假设、概率与伪标签误差边界，不因小样本或缺benchmark细节排除；当前2026版本不能代v1。 |
| 2511.01450 Reg-DPO | 官方撤回排除，见下节，不评分/采用。 |
| 2511.01868 fMRI SSM | C贡献关闭，复用Bernoulli校准：领域脑信号可懂度跨条件解码，题摘未给基础模型SSM的新通用组件/边界；不因理论或小模型自动排除。 |
| 2511.02854 SELF-REDRAFT | 必要设计反侧潜力：无interpreter时重起草探索/自refine利用权衡、反馈质量与脆弱判别是边界；同最大轮数不是等成本/普遍收敛。 |
| 2511.00067 latent-domain prompts | 潜力：无domain label时latent clustering与输入相关文本融合，改变域标签依赖；跨域收益及条件未证实。 |
| 2511.00090 LeMiCa | 生成/执行机制潜力：cache schedule有误差加权图与lexicographic minimax路径，针对全局累积误差；“bounds”和LPIPS/加速仍需必要数学/对照，不采用数字。 |
| 2511.00107 MOVAI | P受限：复用Bernoulli必要v1 §III/IV～VI，时间标注graph与多尺度refinement接口已见，消融表存在不等归因/预算有效已核；不授新算子、SOTA或端到端成本。 |
| 2511.00108 Pelican-VL | P受限：复用Bernoulli必要v1 §2.2，rollout难度/饱和→弱项、关联、生成数据SFT切换已见；pass@k语义与GRPO简式不授理论/实验有效，不采用near-zero模式跃迁或无遗忘。 |
| 2511.00423 BOOM | World Model潜力：planner产生行为与policy偏差，likelihood-free alignment与value权重bootstrap回路；不是仅因非LLM或小模型关闭，不授训练稳定性。 |
| 2511.00511 ID-Crafter | 潜力：分级identity attention/VLM guidance/online RL针对多主体语义冲突；各模块与新数据收益须分开，不采用SOTA。 |
| 2511.00710 Ariadne RLVR | 必要反侧潜力：可控maze难度、base pass@k零与RLVR后成功对能力边界提出修正；有限零采样不证明base概率为0或真正能力扩张，当前2026摘要不当v1证据。 |
| 2511.01310 MWM-MARL | 官方撤回排除，见下节，残留完整摘要不恢复准入。 |
| 2511.01894 LGCC | 生成潜力：局部噪声coupling/content consistency loss针对初始化与编辑破坏；质量/步数/速度联合条件待证据，不授无损。 |
| 2511.02097 robotic WM survey | R1 C→P：功能资格/定义边界争议，宽LLM/VLA动作预测不证明动作条件动力学/因果能力；保留具体memory-path-loss（记忆路径失效及loss/评价约束）盲区，原文与作者待核推断分开，详见文末。拟owner仅路由MULTIMODAL-WORLD-MODELS，不评分/Books采用。 |
| 2511.00351 PAD | 必要设计反侧潜力：从精确分布保持转utility保持、pivot token判别/拒绝放松；正是sampling保证变化，不可借SD已有覆盖排除，不称lossless或等价质量保证。 |
| 2511.00606 SpecDiff-2 | 潜力：离散diffusion并行drafter与AR verifier校准针对两瓶颈；要核分布保持/接受与成本，accuracy相当非全部分布等价。 |
| 2511.07422 inference survey | C贡献关闭，复用Bernoulli校准：题摘解释通用PD拆分和SLO资源权衡，未给新增机制/成立条件或可纠错证据；不是只因Books已有主题而关闭。 |
| 2511.00603 EPARA | 系统潜力：按latency/frequency/GPU需求联合request/service分配与state-aware placement；原v1提交BJTNov02 00:09，不能给Nov01 arXiv首公开，其他原始作者事件若有仍待核，2.1倍不采用。 |
| 2511.00796 AReaL-Hex | 训练runtime潜力：异构GPU上的三阶段异步RL、staleness约束、MILP+图分割，不能只因现有异步RL关闭；v1提交Nov02 UTC，非Nov01确定事件，1.50/1.46不采用。 |
| 2511.00807 FREESH | 系统潜力：GPU功耗-吞吐特征/时空碳强度、routing/parallelism/DVFS/LLF与公平/SLO；v1提交Nov02 UTC，首公开未核，节能/碳数字不采用。 |

当前终态分组20潜力/准入未决（17查询潜力+3个晚提交DC恢复线索）、4贡献关闭、2官方撤回。26身份不增；Bernoulli全部26题摘首批校准有效复用，R1～R3实际写后与最终DAY已通过。日期未核不抹掉机制、安全/反侧潜力，不预评分或由作者自授DAY，不要求重读175月条目。

## 必要撤回与旧证据复用

两篇实际官方abs均HTTP200；Reg-DPO当前v3，官方v3 history为2025-11-10T03:10:25Z withdrawn，原因需进一步修订/核实验，不凭未来resubmit承诺恢复。MWM-MARL当前v2，官方v2 history为2025-11-11T01:34:30Z withdrawn，代码偏离Algorithm1使全部实验与结论失效。Search按显示时区分别记Nov09/10，不能将其显示日期冒称UTC日期；以实际abs原字段分别保存。这是撤回排除，非PDF不可达，也不追首公开日强行入选。

PlotCraft当前abs实际为v2（2026-01-15提交）；无已见撤回/纠错说明，不因版本号自动要求重读整篇或回填日期。root旧有效exact-v1指定章节/表/直接反侧与唯一owner比较仍复用；不冒称v2已证据审阅或版本差额已经证实。本轮0旧候选冻结，具体首公開日未恢复，仍不评分/采用。当前原件及旧定点记录均保留。

## 首包历史checkpoint（已由文末返修READY取代）

当前为**首批准入校准READY，非最终作者READY/日级通过**：原确定候选0，新增确定候选0；26新完整题摘的19/5/2处置及14源有界实际范围准备交独立非作者校准。普通待办是校准反馈、受影响必要补读/日期事件恢复及报告最终复核；不能称为外部故障。不存在新Books实际写入或POST等待；必要Evidence只有旧PlotCraft定点有效结果可复用，不把新题摘潜力写成Books提案。

具体日及机构历史限制按README第5节定点请求。三DC晚提交条目不当Nov01候选，不启动另一日；更多月Next与未展开152查询身份不强制进入全文队列。Nov02只运行本日；Oct02归Helmholtz。root可据本记录安排独立校准，本作者不冒称已向不可见线程成功发送或获通过。

18:46:53+08:00普通恢复追加：实际解析MiMo系列壳的iframe src为`/mimo-v2-6/article.html`，只打开该原路径，HTTP200/21320 bytes，原文明确September22nd2026；核心为本次V2.6系列发布/RL scaling，明确窗外，不采用其benchmark/成本或启动2026日报。旧“动态壳日期/核心尚待”仅为恢复前进度，现在已关闭；More及本页15有限card的日期恢复不留下已做普通待办，亦不授历史删除无遗漏。总实际请求执行范围更新至18:46:53。

18:49:23+08:00本轮机器检查：实际README V3通过1份，本报告及作者记录本地链接/尾空白0错误；14来源、六节、冻结旧0候选/原窗口与新增Nov01自然日检查通过。原件重算176返回/175唯一、23定点完整题摘+3查询池外DC身份，所有175首公告November字段与46份新receipt JSON解析通过，限定只读diff无诊断。非新评分/Evidence/Books或独立DAY。当前普通剩余仅独立校准及据其反馈的具名必要处理/最终复核；不重新留下MiMo已关闭恢复。

## R1～R3实际写回与作者READY历史

2026-10-07T19:29:08+08:00作者返修记录：本次重读AGENTS规定当前合同/每日Source/arXiv/Prompt/ROADMAP与State的Nov02路由，读取[Bernoulli首批FAIL](review-supplement-20261007.md)及本日作者两文件；不重抓十四源、不重读26题摘/175库存、不启动其他日。独立身份为本轮分工Bernoulli，作者Darwin/Codex本会话；复核原文、旧原件/报告完整档案不覆盖。

**R1已写回。** World Model 2511.02097从C恢复P；26身份20P/4C/2撤回，17查询P+3给定DC，原176/175发现、23+3完整题摘与0确定候选均不变。复用Bernoulli v1 Table I/§II-C/D/VI/VIII-B的功能资格与定义冲突校准，不将综述类型作为关闭理由。用户另点名memory-path-loss；现存review R1未细列这一术语，故作者仅定点打开[同一v1](https://arxiv.org/html/2511.02097v1#S5.SS7)§V-D3/V-G、VI Memory及VIII-B Evaluation Protocols（19:28～19:29，官方HTML可读），不泛读引用。

原文有历史记忆/稀疏采样及proxy评价限制；作者的具体待核盲区是：历史信息经存储/抽帧/检索进入状态预测或动作选择，路径丢失/读取失效可能影响长程预测，而视觉proxy/任务均分不能单独证明记忆保真，训练loss对这条依赖路径的约束尚未核实。此memory-path-loss问题不是论文已验证的失效实验、所有模型均失效或新loss定理。准确公开日恢复后，只核对应原版本记忆路径、loss/评价定义、路径干预对照与互相冲突资格，不泛读整survey/所引全部模型；拟owner MULTIMODAL-WORLD-MODELS（Ch25）仅路由，不给root书稿采用授权。

**R2已写回。** CRAGRU 2511.05494保留P，复用Bernoulli已读v1 §III-B/IV及V开头的三策略/core，不继续笼统记策略未明。中心争议同时保留原主张与独立反侧：原底模Top-K候选/辅助信息仍进LLM，§IV-D的filtered-data依赖/条件独立不能仅由直接检索排除推出；底模参数→候选集合→输出的侧路可能保留删除数据影响。不是作者实验证实泄露，不采用完全遗忘/合规/重训练等价，不降分或改C。可接受恢复是原版本底模训练与候选/辅助路径非影响条件、修正删除合同或对应可核验证；无须重读整篇/代码才保存当前争议终态。

**R3已写回。** 本日原Seed JSON只定点核ID875，IsPinned=true、PinTab=[10,3]与独核一致。两作者文件准确写返回Dec01/Oct22邻接含置顶限制，删除“非置顶”锚点描述，不猜PinTab页面呈现；两token0各18、total94/45、next20/has_more=true不变，未请求token20或重抓目录。

**六节终态交接：作者READY，非DAY。** 首批26校准与四篇必要core已经实际到达；MOVAI/Pelican受限准入和采用禁止一并纳入，未变4关闭/2撤回/其他潜力及旧PlotCraft证据复用。日期、具体机构历史段与R1/R2中心争议逐项隔离，不用于正面证据、不进入Books、不支撑零发布/无遗漏/性能或安全保证；Books零写入、无遗漏的必要Books普通待办，非全网无遗漏或Evidence通过。晚DC仅真实归属恢复线索，不属于本窗，不阻塞本窗完成。

当前可执行剩余仅Bernoulli R1～R3窄写后与最终DAY：核两文件实际差额、20/4/2及17+3分账、冻结窗口/0候选/不评分/Books零写入、六节采用禁止与精确重开条件、实际V3/链接/限定diff；不重审26/175、四篇全篇、旧PlotCraft或十四源。README仍进行中/结论未通过，最终独立结果到达前不改完成或自署PASS。root协调接回此交接；不写State/Books/index/合同/Oct02/其他日报，不stage/commit/push。

2026-10-07T19:33:03+08:00修后实核：README V3退出0/1份；作者两文件18本地链接存在、尾空白0、围栏闭合，六节/14源/冻结原窗与补窗/0确定候选通过；26表行/26唯一身份与Bernoulli首包一致，20/4/2及17+3分账写回。176个保护对象与返修前摘要一致（含独立review、旧原件/档案），没有覆盖；限定只读diff-check无诊断。机器不授语义通过或最终DAY，准确停点仍为Bernoulli具名窄写后+最终日级裁决。

## 最终DAY通过与完成态同步

2026-10-07T19:52:46+08:00作者仅同步元数据：实际读取[Bernoulli最终裁决](review-supplement-20261007.md)§7，2026-10-07T19:40:31+08:00独立窄写后及最终DAY PASS；19:41:57落盘实核已记录。首批FAIL R1～R3与返修READY历史不删除，最终裁决接续历史，不冒用旧root或作者身份作独立通过。

Nov02 README完成态/§1、§5、§6已同步：独立复核者Bernoulli，独立行“结论：通过”，限制另行；普通待办0。新26身份20P/4C/2撤回及17查询P+3给定DC、原/新0确定候选、窗口/日期/评分和有效旧审阅均冻结。未新增来源扫描、题摘或必要全文读取，未新增评分、Books采用/写入或POST。§2～4研究正文保持本次同步前不变，首包阶段表述由最终裁决接续。

日期/身份、Google首次公开字段、Meta/Hunyuan/Z.ai历史段与World Model/CRAGRU中心争议继续为具名终态保留项；不用于正面证据、不进入Books、不支撑零发布/无遗漏/性能或安全保证，具体恢复条件仍按README §4～5定点执行。20P不是Evidence完成，宽月库存不转全量队列，3个晚DC线索不属于Nov01补窗、不阻塞本日完成。

当前精确停点：Nov02独立DAY通过、作者完成态已同步；检查后即停，不启动Nov03。仅作者两文件写入；State由root计数，Books/合同/index/Git不写，独立review、旧原件和完整档案不覆盖。

2026-10-07T19:54:51+08:00完成态实核：V3通过1份；作者两文件19本地引用存在、尾空白0、围栏闭合；六节/14源、独立行“结论：通过”、26身份不变/冻结0确定候选检查通过。README §2～4与本次同步前逐字一致，176个保护对象未变；限定只读diff-check无诊断。首批FAIL、独立最终PASS及所有原件保留，不stage/commit/push；本次任务到此停止。
