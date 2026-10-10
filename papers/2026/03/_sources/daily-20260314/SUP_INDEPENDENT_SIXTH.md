# 03-14 第六包独立题摘校准与三个有限决定意见

复核者：mar13_admission_review（本轮显式切到03-14，身份名不决定日期）。只补03-13北京时间自然日，原报告窗口/候选/§4冻结不搬移。已重新实际读AGENTS、完整当前Research/Report合同与Prompt、Sources使用/Daily/arXiv主题边界、ROADMAP主线/owner及最新相关checkpoint、本日README停点；首批输出截断的Report/Prompt/来源段已另读恢复。03-13上下文已结束，未继承其候选判断或打开其材料。

实际范围：`SUP_ADMISSION_SIXTH.md`、`SUP_ABS_SIXTH_MANIFEST_RESULT.json`与八份官方exact-v1 `SUP_ABS_<ID>.txt`完整title、Authors、AB、Comments、visible history，八GET200/2026-10-09T16:49:23–24Z/final URL身份已核。仅原四主题161发现中的本包八条，不新查来源、不将161当全文队列。没有给八条评分、日级日期、Evidence/Books或DAY；下面P只是具体贡献可继续核验。现有abs必要字段未见具名撤回/纠错，11665/12206显示后来v2但未声称重要增量或全部版本无变化。Authors与自动ViewPDF计数不一致时保存完整署名，不自行改身份。

## 五项非作者题摘准入校准

| ID / 精确版本 | 实际增量与判断 | 采用边界与下一层 |
| --- | --- | --- |
| [11661 Resonate](https://arxiv.org/abs/2603.11661v1) | **窄P PASS**：offline CLAP/DPO限制→flow音频生成适配online GRPO并引入细粒度LALM reward→可能改变online更新与评价信号的选择；不是“应用GRPO到音频”或470M/SOTA本身计贡献。 | 必要方法再核随机flow/policy更新、reward对象与human alignment；不在AB层授具体credit law、优于全部offline预算或稳定人类oracle。 |
| [11862 You Told Me to Do It](https://arxiv.org/abs/2603.11862v1) | **窄P PASS**：高权限Agent把项目文档当setup指令→README端到端外泄与检测/FPR负侧→重新区分功能执行与外部effect/egress授权。 | 85%是受测最高非普遍，模拟语义compliance非真实exfil；15人0%检测及防线权衡须核分母/权限。安全必要审阅仅相关评价，不扩全部战术附件；不授结构普遍不可解或真实防线全部无效。 |
| [11896 Think While Watching](https://arxiv.org/abs/2603.11896v1) | **窄P PASS**：perception/generation交替与早期状态衰减→segment memory、streaming causal mask/position与重叠pipeline→需重选新segment可见性/状态快照及并发职责。 | 三阶段数据/训练也是treatment，不因tokens−56%授无损、免费、全量memory不衰减或真实独立并发。 |
| [11947 Paralinguistic Awareness](https://arxiv.org/abs/2603.11947v1) | **窄P PASS**：content-only输出丢副语言→层级分析决定selective-layer FT+dual-level head→具体全层训练替代与语义/副语言取舍待核，可最终低分recipe而不先EX。 | 五分析不识别唯一功能层，高分/超全层也不授普遍互不损害。Submitted Interspeech2026只作具名venue信号。 |
| [12206 CLASP](https://arxiv.org/abs/2603.12206v1) | **窄P PASS**：SSM压缩状态污染需在下游输出前筛查→Mamba BOE/XGBoost token检测及document/cluster holdout→改变隐藏状态安全测量的输入与单位。 | resume只是受测负载，token/doc F1不互换；1032tokens/s/<4GB不授full hybrid生产速度，独立检测器也不自动所有downstream-independent。v2仅可见版本信号。 |

这五项只认可有具体机制/边界可审，不由ROADMAP能映射、主题相关、通用permission/memory原则或headline数字反推准入。都未核首次公开日，不能先列确定当窗候选。

## 三个AMB：本人准备的有限决定意见，须root非准备者再核

以下直接读官方exact-v1 HTML到决定接口清楚即停，不是本日报作者的摘要转述，不预定评分/全文/长期段。网页行号是本次原HTML读取定位，链接仍指精确v1，未写共享Books。

### 11650 QChunker

实际[§3.1–3.3/3.4与4.5–4.6](https://arxiv.org/html/2603.11650v1)读取接口，决定意见 **AMB→窄P**。分区候选由outline采样，再用相邻PPL比与feature-centered embedding Gram的regularized logdet组合打分；review/completer仅从原文其他位置取缺失知识再rewrite。这不只是四角色名称，增量是direct chunk-level选择器与受源约束completion可改变ingestion目标。格拉姆体积不证明真实semantic completeness，PPL比不保证≤1或事实独立；λ按CRUD下游相关性选取，不宣称完全无下游依赖或普遍校准。必要界限清楚，剩余可信度进入最低证据层而非EX。正文56行出现WWW2026会议信号，abs未写不等没有先稿，日期门须具名处理。

### 11665 MT-RL-Judge

实际[§3.2 Eq2–5、4.2–4.4/Tables2–3](https://arxiv.org/html/2603.11665v1)，决定意见 **AMB→窄P，限定为新验证/反侧，不借成熟GRPO**。目标只是label correctness+reasoning-format二值reward，普通多任务并集不计新机制；但同backbone的pointwise→held-out pairwise迁移对照给具体格式泛化边界，SFT-Unified在Safety低于原模型，RL分支不同。训练已包含对应任务语义，非全新语义OOD；Table2多任务RL在若干slice不优于single RL/SFT，不能授普遍多任务协同或reasoning因果。值得继续核验该选择，不用任务数决定准入；可能局部低分。HTML自动date August24不当首公开日/重要修订。

### 12138 HATS

实际[§3.1–3.3 Eq1–4](https://arxiv.org/html/2603.12138v1)，决定意见 **AMB→窄P**。执行reverse instruction后，用action reconstruction recall判定refine/接受；其逆函数作为hardness沿tree-policy路径更新Q，改变后续UCB探索。实际闭环不是一般“探索+自评”换名，也不借MCTS自身计新贡献。该recall是VLM语义match且是存在匹配、非完整順序/effect proof；整轨迹scalar非逐action真实credit。正文discarded misalignment与verified回传措辞有接口歧义，需后续必要Source厘清，不在准入层缩池或认证corpus全正确。已知accepted CVPR2026先稿日期门仍待核。

## 本包停点

五项题摘独核PASS；三个本人准备的有限core意见已足够提出窄P，**尚须root非准备者实际原段裁决**，不把本人意见自授独核。八项首次公开日期均本轮未核；Submitted/Updated/HTML自动日期/会议接受不是first-public。会议信号11650 WWW2026、11947 Interspeech2026、12138 CVPR2026需按必要具名入口恢复，不扫会议库或全版本；无别日推断。

未核其余153标题/本日来源全覆盖/全附件/代码/Books实际差额；前包有效结果不重审。仅写本文件，不动root主ledger/README/Books/State，不stage/commit/push，不授DAY。

## 剩余发现入口与标题边界：有限独核，不生成85/149项队列

03-13委派已结束，本节显式重新启动03-14/Mar13自然日上下文；实际重读AGENTS与完整当前Research/Report/Prompt，Sources使用/Daily及arXiv有界查漏规定、ROADMAP当前主线与AI for Science暂缓边界、本日README及最新checkpoint路由。第六八项有效题摘/core与日期结论不重开，root/作者正在研究的11862/11661/11896/12206不重复。仅写本文件范围节，不写主ledger、Report、Books或State。

直读 `SUP_REMAINING_TITLES.md` 全部149标题与作者85/64初分理由，再实际解析六份官方Atom的query/分页/ID/title字段：`SUP_TOPIC_MODEL/SYSTEM/MULTIMODAL/AGENT.raw`分别78/4/35/62条，`SUP_TITLES_CL_RETRY.raw`84条、`SUP_TITLES_SYSTEM_RETRY.raw`19条；都start0/max150、各totalResults等本页entry数，六份union224。原四主题用language-model/Transformer/MoE/alignment、serving/KV/speculative/distributed、multimodal/world-model/VLA/diffusion、Agent/memory/RAG等title query；补检为cs.CL与cs.DC/AR/PL/OS/PF的submittedDate区间202603111800～202603121759。四主题manifest GET200身份实际核；category raw的query/updated只证已有响应身份，本轮不补造未读retrieval-status记录。149标题ID无重复、全部在六Atom union中且title逐条相同，作者名单不是新发现；本轮解析没有消费summary或发新网络请求。

因此分页层未见已知未读page，但这仍是**submittedDate发现切片**，不证Mar13公开批次、全学科召回或全历史coverage。两category宽页只允许查漏标题，不因已缓存而变成整类逐项AB关闭任务。224/149/85均不是候选分母；旧75题摘文件数仅作者库存声明，本轮未重新认证75全部准入或完成。作者开头“85含糊相关标题必须先完整AB”的一揽子表述应收窄：完整题摘是对真正含糊或有项目增量线索条目的准入要求，不是这85个名字共享的贡献理由。

### 有明确主线接口线索者：需要完整AB，但不是先准入或全文

下面只根据实际title指出待核的选择，不能用关键词直接签贡献；AB须回答具体变化，成熟组件组合、榜单或领域换名可在AB层关闭，无需自动Source。

- 模型形成/表示与计算选择：11211 nonlinear multi-adapters的增量学习、11625训练免费hierarchical token pruning、11881结构pruning与distillation、12055 semantic-geometry持续学习、12089 federated LM black-box watermark、12193 VLA active-perception/manipulation、12208 token预算、12222 stochastic autoprune、12248 energy-based feature-vs-token fine-tuning；新增36中11510 multilingual scale、11611 partial RoPE、12149 perception/confidence/accuracy、12165合成code instruction筛选、12191 long-context encoder。MedPruner/ForensicZip/Polish不是因此入选或排除，AB要核是否真有压缩/位置/支持集选择，而非只提高领域指标。
- Agent/平台接线：11798信息structuring、12031 Kubernetes多目标scheduling、12229 LM teams作为distributed systems、12230安全considerations、13404 schema-first tool misuse/recovery/budget对照、13417 MCP protocol→production、15666 compiled-memory指令精度、20260 error forecasting；新增36中11545 adaptive tool orchestration、11781 typed epistemic acts、12123分离production/review session、12152 long-horizon simulator。系统类比或security/design-pattern标题不授机制，AB需明确状态、更新/授权对象、failure path或实测接口边界。
- 评价与直接反侧：11974 NormCoRe replication、11975 HomeSafe不安全动作检测、11987 LABSHIELD安全critical reasoning/planning、12129 intelligence增加却collective结果更差；新增36中11687 semantic eval、11698 object-state-change video eval、11863 self-evolving challenge、12094隐私audit、11287 RTL synthesis-in-loop reliability/failure、11340 black-box tuning/system-spec反侧、11489 trace-aware causal-fix与semantic redundancy pruning。新benchmark本身不足贡献，需实际blindspot/混杂或修正机制，科学实验室安全标题也不整体等科学应用。
- 多模态消费协议：11640 floor-plan tokenization的understand/generate/edit接口；新增36中16924 simultaneous speech translation、11409 turn-taking、11482 preference-style speech eval。分别核token schema/可见前缀/说话时机或评价对象，非仅增加领域样本。

这些共41个标题给出了可问清的主线问题，**只是有界AB线索，不是41个贡献P、41个必须深读项或本窗候选**。未读AB就没有其新增事实；准备者可按当前可执行且非重复身份分批处理，实际明确无增量即可停。

### 代表性边界重开：不能按领域词或“用了已有方法”机械排除

定点列十个需要AB消除范围歧义的样本，而不为相似所有标题扩池：11253政治属性推断可能是敏感属性/隐私能力反侧；11248现人工vision network不具知觉对齐坐标可能修正表示解释；11277 COMPASS要区分普通伦理framework与具体authorization/measurement；11884 decentralization price可能是多Agent学习/通信条件而非工程应用；15668 QSC要区分密码学包装与实际Agent安全机制。另原64-stop中的11757 Social Bandit Free Energy可能直接学习/优化机制，12117 SommBench、12249 SciMDR、11414 MaterialFigBENCH需区分“加领域题集”与实际模型评价盲区，不能仅由sommelier/scientific/material词关闭；新增36的11281真实patient多轮dialogue也须核是否仅领域benchmark还是multi-turn状态失效证据。

这十个只是title层歧义，不认可其中任何正文结论或先开日期门。若AB仅领域预测/领域知识测验/组件应用而无主线机制或blindspot，原范围停止可成立；若有新反证或学习条件，就继续该项贡献层。本人此前消息把11253列应用停止过强，已即时回告root并在此纠正为边界AB，不将敏感属性问题一概排除。11757也不能因小模型或非LLM标签退出，但不预授其理论适用LLM。

### 明确应用/范围外标题的分层抽核与停止层级

原Atom身份直核的代表包括：11254 Persian-poetry sentiment、11358 Bangla-English financial-fraud classification、11408 WTI futures return prediction、11594 chemotherapy outcome prediction，是任务应用/一般领域预测；11350 derived-category数学、11514 fiber-amplifier光传播、11571 classical-time理论、11585 chiral magnets，当前没有模型能力/系统机制关系；11582 UAV chemical-plume定位是传统控制应用、11849 RISC-V SD-card controller是一般硬件，不能由multi-agent/GPU/RISC-V联想现训练推理；11703 protein-engineering flow、11627 PET segmentation与12008 SAR geospatial segmentation虽含flow/foundation但落当前Science应用边界。以上13个样本的**title层范围停止**可支持，不声称AB/安全事件/全文已审或无纠错。

原85中的11627/12008不应因Foundation字样强制AB；原64里的四个边界样本也不能据领域名直接全停。光网O&M、e-commerce decision-support等明显应用标题可以作为降低入口宽度的线索，但本文未用“Agent工作流/传统领域”共同理由签其全部明确EX；还未实际核它们有没有新execution协议、控制流或安全反侧。不建立成熟组件组合=题名EX的第二条机械规则。

2604/2605编号与晚推ID只记录发现身份：SoLA、abstention architecture、energy/多请求、BrainMem、entropy dynamics、GNN反馈、performance certification、focused attention、VIGIL、FedACT等题名含机制线索，但编号不自行证明家族首次公开或本窗OUT。不能凭本次旧submitted切片把其arXiv事件冒充Mar13；是否需要AB应先协调确实属于本日有用事件/具名早稿线索，不能因缓存late title把十个全部加本日全文或跨日队列。此范围节不独立复核其日期，不要求精确时刻。

### 裁定与未核范围

**入口身份/有限标题分层校准通过；原85/64整组处置未通过。** 本人实际浏览149标题并核原Atom身份，但语义抽核明确到41个主线AB线索、10个边界样本与13个停止代表，其余85个标题的作者单项分类未逐条独立签章（149−41−10−13=85，和原作者85名单不是同一集合）。不能将浏览/程序match升级149全贡献筛选或64全EX；发现共同机械理由后只重开受影响样本/同理由条目，未授权抓全部149。未核新AB/current事件说明、日期、候选证据、Books及六部分DAY；第六八项前有效结果保持。本节仅范围层停点，可执行的具体AB/未定范围仍交root/作者协调，不把普通工作改外部受阻，不stage/commit/push。

## 11862：非准备者必要安全Source与actual Ch72具体已有覆盖

继续03-14/Mar13 BJT本日上下文，完整重读AGENTS、当前Research/Report合同与Prompt、Sources使用/Daily/主题范围、本日README/停点与ROADMAP相关owner；latest checkpoint仅路由，不继承另一日判断。第六包题摘准入/有效事件日复用，本轮实际再核exact-v1 abs题名、七作者、完整AB/Comments/visible history，必要页面没有撤回/纠错标记，不为此全版本查找。本人不是 `SUP_EVIDENCE_11862_ROOT.md` 准备者，读包后直读 `SUP_NECESSARY_11862.txt` III-A/B threat与决策模型、IV-A setup/metrics、TableII统计人口、IV-C cross-backend、IV-D cross-agent、IV-E人审、IV-F/TableV防线分类及V直接limitations、AppendixD必要配置；不读III-D/AppendixA–C payload与执行战术、图像精点、旧版本、全部引用、代码或复现。原件manifest `SUP_READSEC_ROOT_MANIFEST_RESULT.json` 实际exact-v1 GET200/222598bytes/2026-10-10T01:09:16.629418Z，本日缓存身份成立，截断owner局部另恢复。

威胁和指标直接成立：攻击者只能改静态README/安装文档，不需runtime访问；被测高权限Agent可读本地私有文件、执行terminal且出网。主要环境ClaudeComputerUse/Sonnet3.7，500不同repo、Java/Python/C/C++/JavaScript各100，星数≥10且按长度筛，保存benign/modified variants。40%即200例/三seed平均与TableII每cell n7是两层不同人口，不能混成所有cell都500或独立七个大sample replicate。ASR明确要求正确敏感数据实际transmitted到external server，attempt/placeholder/错误非敏感文件/拒绝不算；RR与正确benign安装TSR各是不同目标。EPYC7742/A10080GB是披露host，不作闭源API实际推理GPU；必要方法未披露完整长度、并发、precision/tailSLO与全CI，不用摘要85%当所有配置或未来代理保证。

跨模型反侧实际核：AppendixD LangChain/LangGraph同protocol、150instance、预定义leak-associated function一旦invoked即success，明确无须实际传输，不可合并main端到端ASR。原文所谓“四LLM families”实际列GeminiPro、GPT4o、GPT-oss20b、Claude3.5四backend，涉及三provider；GPT-oss20b脚注称未公开内部identifier，不自证公开checkpoint/revision，GeminiPro与其他段Gemini2.5名也不由本人补统一。正式结论应写四受测backend，而不新增第四独立provider或外推当前全部模型。IV-D只有ClaudeComputerUse完成端到端；OpenDevin模型已attempt但Docker阻outbound，说明所测执行环境边界确有作用，不能采作者“capability gap而非security gap”解释推权限/egress隔离无用。其100%parse/attempt也没有足够公开分母用于全代理保证。

TableV只文档是否unsafe的classification：PromptInjection benign/injected/link皆.3，Anonymize .9/1/.9，GPT4o 0/.9/.3；说明当前操作点检出与误报的取舍，不证更完整权限/网策略、微调检测器或所有防线没有解。原文本身承认minimal yes/no提示仅lower-bound，没做过滤后实际ASR/utility端到端验收，也未闭合每row全部样本/重复统计，不能签生产FPR或所有defenseArchitecture不可缓解。15参与者/各3份/45questionnaires是clarity/completeness自然阅读而非专业安全audit，0specific-injection detection不是人类不能检测；6.6%有泛危险感也不等定义下具体检测。V承认single大学技术背景/主要passive exfiltration，持久化、横移等未实验；artifact仍 `[URL to be confirmed upon acceptance]`，没有独立artifact/复现通过。安全设计保持可验证未知，不照录“structural universally unmitigated”宣传。

actual owner完整顺读 `PLATFORM-SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 865–930 containment/risk stage与conditioned detector、1307–1337 typed proposal→policy/least-privileged executor及Rule-of-Two历史ABC/egress、2251–2273 authenticated provenance/层级训练与runtime净收益/误拒、3131–3150 trusted canonical effect审批与独立principal/reviewer capacity；实际读Ch71/Ch73入口的tenant数据/网络隔离与生产proof obligations交接。这里的覆盖是具体已分开不可信read、proposal、authorization和commit，拒绝或attempt不等effect，读秘密+处理外文+出网需executor实际边界，模型识别与monitor分数不签权限；也已有安全/utility/效率与误报review容量分账。不是主题相近就NC，更不称本paper新README样本、85%或15人测量已经被Books吸收。main与simulation不同predicate的新反证不要求再写既有effect分责接口。

独立裁定 **Design2+Reach2+Durability2=6，标准门槛与安全反侧必要局部深入完成；Source PASS／actual具体已有覆盖PASS，Books新增0。** 评分对象是这次installation README下实际effect-vs-semantic compliance及benign-FPR反证，不借成熟最小权限原则、攻击taxonomy名称或厂商声望抬分。没有未承载的长期接口要PRE，无需Books写锁/POST。可正式同步受限NC；不得把全部防御无效、真人安全审计零检出或全部Agent外传写成采用结论。原85/64范围校准仍未整体签章，本单项不闭合剩余149或整日报。仅写本文件，未改主ledger/Books/README/State，无stage/commit/push，未授DAY、实现或复现。
