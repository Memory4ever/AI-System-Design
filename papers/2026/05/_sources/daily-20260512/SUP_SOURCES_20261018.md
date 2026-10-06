# 2026-05-12 Daily — 遗漏补充来源记录

## A1. 范围、冻结与当前停点

- 作者 `/root/may12_supp_author`，独立复核 `/root/may12_supp_reader`（仅写 `SUP_REVIEW_20261018.md`）。2026-10-18恢复本日时总路由130/279，随后全球路由由root维护；本文件不另计跨日进度，不继承尾部旧cursor。
- 用户仅授权补遗漏。保留原124候选整行、日期评分、小时窗口及连续旧§4和有效证据/Books；新增只检查北京时间 **2026-05-11完整自然日**。原件 `baseline-before-supplement-20261018.md` 与运行前README逐字节相同，SHA256 `cb28320b811200334bd5a542d2d1717ab0a4a592d30ca513c57cd95a26def809`。
- 唯一写入范围为本日报、本文件、必要baseline及真实原件；共享Books/LS/index均未授权，提出窄稿后交root协调。不得以结构校验替代Source、owner/PRE、真实POST、六节DAY与保存态FINAL。
- 启动时普通待办为本日来源历史切片、49旧小时窗外事件、51未命中ledger的有界核实与Source/Books独核；后续真实完成及有限外部保留按A6/A7与末尾当前A5，不沿用本启动清单。未执行工作不能改称外部，旧124层不重审。

## A2. 已实际执行的发现范围

执行自2026-10-18 19:34 +08:00起，均为检查时刻而非发布时间。原件为本目录 `SUP_<简称>_20261018.raw` 及 `.headers.raw`；失败请求的文件只证明实际失败。

- 14每日源均首查：OpenAI403；Anthropic200；DeepMind200；Google pubs35秒超时（含一次重试）；Meta连接重置；Qwen旧站明确指向`qwen.ai/research`后当前站200；DeepSeek/Kimi/Hunyuan/ZAI/Seed/ERNIE/MiMo/MiniMax均200。200壳或首页不授历史零命中。
- 机构有界补搜：OpenAI/Anthropic官方`May 11, 2026`研究；Qwen/DeepSeek/MiMo/Hunyuan`2026-05-11`；Seed/MiniMax/Kimi`May 11 2026 model`；Google blog/Seed的精确日查询。命中OpenAI Signals的Q1 adoption和Campus interest表，系使用统计/活动而非模型系统机制，标题范围排除；阿里云DeepSeek V4 Pro上架是第三方托管发布，不能当DeepSeek新机制。二手WebWorld线索只作线索，尚待原始日期/身份处理。
- arXiv最初MODEL查询 `submittedDate:[202605071800 TO 202605081800] AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:pretraining OR all:"reinforcement learning")`，start0/max150，total442，未分页；这是未完成宽发现线索，不按442逐项关闭。API回显日期引号本身不证明范围失真；实际存在后月ID/May提交的hold信号，须逐身份定点，不用ID月份倒推公告。
- 双编码`*_VALID`四请求均HTTP500 errors，未计任何结果。后改窄主题，真实四原件均start0/max200、全部返回完：MODEL_NARROW94、MULTIMODAL_NARROW65、SYSTEM_NARROW10、AGENT_NARROW97，共233唯一ID；published提交字段均落上述辅助提交区间，**不把其称May11已公开233篇**。主题表达见原feed title/link：模型标题language model/transformer/MoE/pretraining；多模态world model/vision language/diffusion/VLA；系统LLM inference/GPU kernel/distributed training/model serving；Agent标题agent及tool calling/agent memory/retrieval augmented。分类历史补检`list/cs.CL/2605?show=2000`及带skip形式均404，不能授分类列表已覆盖。
- 精确去重只把上述233个ID定点比对前日报现存记录，不拿相邻池做发现：47在May11原候选101内，身份/事件无变化复用其有效层；86命中旧preclosed记录，只可复用仍成立的具体贡献理由；49为`owner_event_recovery_closed`，此前只说明旧小时窗外或未有revision信号，**不等于首次公开已审**，本次自然日必须处理；51不在该ledger，须本日判断。该分组不是候选配额，也不是批量关闭。
- DataCite错误参数`client.client-id`返回0，不计零命中。正确`client-id=arxiv.content`＋registered区间返回total1417；max1000请求超时半JSON，保留失败原件，不解析为完整覆盖；随后max25返回可解析25条/57页，只作已知精确日期线索，非全学科逐条队列。精确DOI的独立原件另存`SUP_DC_<ID>`。

## A3. 首批准入校准与日期收窄

reader已完整读四题摘并校准：CoBit（精确v1标题不同，不能套当前v2收益）、Priming08301、FlashSVD08314、WebTrap08310都具有可核验机制/直接安全反证，不因题目映射或数字选入；ProtSent06830与SCALAR06772是明确科学应用暂缓代表排除。

| 身份 | 旧判断 → 实际增量 → 重考虑选择 | 本次日期资格/停止位置 |
| --- | --- | --- |
| 2605.07013 CoBit | 词表维连续diffusion输出成本随V增长且质量/多样性需共同控制 → bitstream、解析独立位后验与残差学习及entropy-gated stochastic corrections → 重新核验表示维度/采样预算与质量熵的取舍 | exact-v1 abs与同DOI findable/arxiv.content/registered=2026-05-11T02:09:55Z；v1提交May7 22:50:51Z按当期规则最早May11 BJT，联合区间同May11。v1正文已请求，待Source。 |
| 2605.08301 Priming | hybrid架构探索被从头预训练成本约束 → pretrained Transformer短对齐迁移并同条件比较SSM → 重考虑Attention/SSM替换与迁移预算 | v1 May8提交最早May11，registered May12 03:46:10Z，跨北京时间日；Updated/ID不代公告，尚不能确认May11。已下载core仅作恢复，不宣称Source通过。 |
| 2605.08314 FlashSVD | 低秩FLOP节约不保证prefill/decode服务收益 → factorized统一runtime与phase-specific执行 → 重考虑压缩与kernel/runtime共设计 | 同上，registered May12 03:46:28Z，跨日；必要官方公告/早正文日期仍未定，不先评分采用。 |
| 2605.08310 WebTrap | final user-task完成不代表无恶意副作用 → mid-task injection执行攻击后恢复用户流程 → 重考虑成功/隐蔽性与过程安全评价 | 同上，registered May12 03:46:23Z，跨日；不能用May8 Submitted当May11公开。 |

DACA16342、LoopQ16343、Orth-Dion16341的当前题摘有可核验具体贡献；但registered均May19且v1 May7/8，组合跨日，先隔离日期资格，不因访问到了全文而授当窗采用。LaWM08279同样May11最早/May12登记，未得到直接日公告。它们不是贡献排除，也不是本日确定候选；没有具名早稿信号不为所有假想渠道无限恢复。

## A4. 后续本日判断与证据

以下按研究与窄授权实际发生顺序保留过程；早先“待/拟/尚未写”只表示该时点，不推倒后续已有效Source/PRE/POST。当前结局为新46=34实际整合/12具体已有覆盖，均经独立实际复核并root接纳；机器检查与日级验收按A7及当前A5区分。

### A4.1 07013 — Source已核，owner/PRE待实际确认

- 精确版本：`arXiv:2605.07013v1`，标题 **Towards Closing the Autoregressive Gap in Language Modeling via Entropy-Gated Continuous Bitstream Diffusion**。当前v2的CoBit/462M新增不能回填v1。日期采用A3的unique-v1/当期公告规则/同DOI `arxiv.content`、findable和registered联合区间，不用created替代。
- 贡献与评分：词表维连续diffusion的V输出边界及质量/多样性混杂 → bitstream输出、解析独立位posterior与context residual、网格决定effective churn → 重新考虑表示与sampler共同配置；2+2+3=7，深入。
- 作者及reader已实际读exact-v1 §3.1–3.6、§4.1–4.4/Tables1–3、§6、直接D.5–6与F.1/F.5。原件 `SUP_CORE_2605.07013v1_20261018.raw` 完整HTML。token bits按semantic patch进同长度Transformer，输出边界由O(TV)变O(T logV)，不是所有trunk计算同降。解析Gaussian bit posterior只担local denoising，network担context residual；不是免训练语义编码。固定checkpoint/NFE下churn对照与training ablation区分；entropy grid让恒定raw churn对应非均匀effective correction，但D.5明确只是小步极限，非有限步精确恒等。
- 质量证据限130M、LM1B/OWT、128/1024 token blocks、GPT2-large的GenPPL+token unigram entropy、10 sampling seeds；不认证长文语义多样性或frontier LLM。F.1 synthetic GH200、BF16、关闭compile/SC、128NFE profiling排除tokenization/decoding/scoring/transfer，不能与256NFE质量结果拼成生产端到端加速；作者未复现/核代码。
- owner比较：Ch24 `MULTIMODAL-GENERATIVE-PARADIGMS`当前“连续高斯去噪迁往离散文本时，采样路径也要重验”中LangFlow两段已有categorical posterior/entropy调度及GenPPL区别；“预测空间也可以从Flat Vocabulary改为树”是离散层次状态分支。二者未承载bitstream解析posterior输出接口及grid↔effective churn耦合，拟一段整合，不新章。Ch23保codec身份/表示，Ch25保world dynamics；本处只解释生成objective/path。
- **逐字PRE草稿，尚未写Books：** 在LangFlow第二段之后、LangDiT段之前插入下段（root协调共享owner，reader实际PRE后才写）。

> 连续文本生成还可以保留语义token长度，却把每个token展开为固定宽度二进制patch：主干仍处理T个位置，输出与loss边界由O(TV)词表logits换成O(T log V)位logits；Gaussian加噪下独立位的解析posterior负责局部去噪，网络只学习上下文残差。这不是消除词表编码或全部计算，更不自动保持生成分布；噪声网格还会改变恒定raw churn对应的有效随机修正，二者需共同验收，其Langevin解释仅为小步极限而非有限步恒等。[受限bitstream对照](https://arxiv.org/html/2605.07013v1)在130M、LM1B/OWT上联合检查GenPPL与unigram entropy，适量随机修正改善所测质量—多样性前沿，过强仍退步；synthetic GH200/BF16的128NFE边界profiling排除了tokenization、decoding与传输，不能与256NFE质量实验拼成生产加速。编码、训练、self-conditioning与完整去噪均付费；质量、多样性或净费用失配时，保留flat/token-space、离散diffusion与AR，不由小输出头批准无损替代。<!-- source-family:SF-2026-ARXIV-2605-07013 -->

### A4.2 请求/计数的行政纠正

233只是发现线索；49旧小时窗外身份只是未处理事件；截至首批核对，作者完整读exact-v1题摘40（不是49文件数），另06772/06969/07544/07649曾读current API题摘，不能冒v1。首批14具体P已由reader准入校准；其他作者P尚待校准，不由下载或主题映射自动入选。86旧preclosed只复用仍成立的具体理由，generic blanket不作共同证据。

作者曾错误发出35个并发core请求，超出必要投入顺序且导致33半件/失败（先前31为计数笔误）；已停止并发、透明保留原件，半件不作为Source。其后改≤3精确请求，同时仅推进已校准或明确含糊的单项；`SUP_CORE_RETRY_2605.06869/2605.06933/2605.07001`真实完整，作者随后已读足必要层，不能由reader已读替代作者待办。06890与07574原core完整，前者作者已读§3–6；后者后续准入/Source已独核，实际范围见reader R5/R9；不按文件存在授通过。其后只有root指定窄授权的07001/07013实际Books写入（见下），无新扩批。

普通可执行工作继续，本文尚不授DAY/FINAL。

### A4.3 06890 — Source通过；具体NC待独核

- exact-v1 `SUP_ABS_2605.06890`与`SUP_DC_2605.06890`身份匹配，findable/arxiv.content，registered May11 02:07:02Z，unique-v1提交May7按当期日程最早May11 BJT；区间同日。只读helper复算bounded，不代原件核验。
- 原来tool failure主要在外部执行后看见 → last32 pre-action hidden states经SAE再读tool-need/risk两个linear probes → 可在执行前为漏调用/动作风险提出告警；2+1+2=5，标准完成，必要反侧额外读足。作者与reader实读完整原件`SUP_CORE_2605.06890v1_20261018.raw` §3.1–3.5/§4/T2–10、§5/T11与§6。
- 只支持GPT-OSS20B/Gemma3 27B在Nemotron/BFCL上的受限sensor：risk标签由tool类别heuristic产生，BFCL还混入协议/格式变化；SAE latent ablation仅改变probe输出，不证明policy因果使用。T11 unnecessary-call56.3/98.5%是runtime expected-vs-actual，不能写成probe独立误报率。未核实现/复现或原生monitor总费。
- **拟已有覆盖：PLATFORM-MONITORING Ch67**“四个黄金信号”后原生draft-activation风险probe段与紧接的native-vs-prompted/SAE读出段（当前153–157），已经明确activation sensor、model/layer/SAE/checkpoint/标签人口、另一次forward与原请求identity分开、SAE域外并非一致改善/全费；“输出Watermark与Hidden State都只是受限Sensor”段（285–290）已写white-box/阈值/domain shift、probe只触发review/stop proposal、独立policy仍拥有authority。Ch78“Tool Necessity与Execution Admission是两个Gate”750–755还具体分开调用sensor和执行许可。本篇新局部task/risk读出不推翻这些判断，未证明新的通用因果或安全门；不为新SAE名称重复正文。NC需reader实际核owner，未声明完成Books。

### A4.4 06869 — Source通过；具体NC待独核

- Agentick exact-v1，原件`SUP_CORE_RETRY_2605.06869v1_20261018.raw`完整；ABS与DC registered May11 02:06:32Z/unique-v1/规则联合同May11，已有原件非Submitted单证。
- 各Agent范式通常只在自身输入/harness中比较 → same seeded任务同时暴露五观测格式和可组合harness/类别分解 → 重考虑把模型与接口收益混成范式排序；2+2+2=6，标准完成。作者/reader已读§3.1–3.3、4.1–4.5、5及必要AppA。
- 37个2D turn-based任务×四难度×25seed，27configuration/初评非VLM、fine-tuned或旗舰全景；PPO pixel与LLM ASCII不是信息/总预算等价。ONS oracle只是strongest reference，可能>1；不能写绝对上界或“同seed即公平范式”。按当前初评scope，不采用不可控排名/未来方向作事实。
- **拟已有覆盖：PLATFORM-EVALUATION-SYSTEM Ch66**“Evaluation Runtime”已有`model × benchmark × harness × environment × scorer`完整identity及adapter语义等价责任（当前约365–380），工具权限独立treatment与同turn非同API/token/time预算的AgentVista段（423–425）已承载接口/预算分账；Ch23开头“tensor compatibility不是semantic compatibility”解释相同shape不等同信息。Agentick提供新可用substrate及本地反例，而本次采用命题不改变这条设计选择；不把具体37任务或ONS榜单写成长期知识。NC待readeractual owner核实。

### A4.5 07001 — Source通过；具体owner/PRE草稿待核

- SmellBench exact-v1，`SUP_CORE_RETRY_2605.07001v1_20261018.raw`完整；ABS与DC registered May11 02:09:39Z联合同May11。贡献：原先以detector消失/测试通过衡量修复 → expert FP/partial/TP、direct/cascading repair与net新smell分账 → 重新考虑修复收益oracle/负回归而不按单个“resolved”排名；2+2+3=7，深入。
- 双方已读§3/4/5.1–5.7/6/7：单scikit-learn1.7.2+PyExamine、65hard tasks（11TP/41FP/13partial），无重复trials，nativeCLI混杂模型/scaffold；全suite无偏离不证明所有功能正确，63.1%FP不是工具通用误报率。消失含跨任务cascading/order效应；netdelta把新smell等权、不代人工架构质量。GEPA static+judge proxy未验证真实outcome；top8 pairwise无显著差异，不采用榜单和47.7%作通用修复率。
- actual owner Ch66当前413–415已分开测试执行路径、baseline与开发者oracle，以及局部code变体；417起进入环境clone。这里尚缺“detector目标本身可能是有意设计/部分合理，目标减少可同时新增其他smell”的具体评价接口，拟在code-test段后、环境clone前一段。Ch65是scheduler而Ch67是monitor，不接管评价oracle；Ch68持有日志而非质量判定。
- **逐字单段PRE草稿，未写Books：**

> 修复型Agent的目标检测器还可能把有意设计报成缺陷，因此应先以独立需求或专家判断区分真实问题、误报与部分合理的取舍，再分别记录目标指标减少、跨任务连带消失、其他位置新增问题和功能回归。一个smell不再被检出，不证明该处结构已改善；测试仍通过也不替代这份架构oracle。[受限代码修复评价](https://arxiv.org/html/2605.07001v1)中，单一仓库/检测器的激进修复可减少更多目标却引入更多新smell，连带修复还受任务顺序影响；不能把其误报比例、净计数或nativeCLI榜单推广为通用质量率。专家校准、全库重检、测试和重复运行均付费；oracle含糊、净影响恶化或证据不足时，保留原设计、范围更小的补丁与人工审阅，不以检测器消失或单一pass批准合并。<!-- source-family:SF-2026-ARXIV-2605-07001 -->

日期helper已对40份精确DC复算为May11 bounded，另7份跨日unresolved；40不是候选数，07202/07358等贡献排除不评分，07632仍须补作者exact题摘。raw身份、状态、版本及早稿信号仍由人核，不由脚本决定贡献或独核。

### A4.6 已发生的独核与行政同步

- reader R7已经实际核06890的Ch67与Ch78、06869的Ch66具体NC，**两项已有覆盖成立**，不是按主题相似。07001具体Source/owner/PRE亦通过，root随后授Ch66指定单段及本人纯来源注；作者已真实保存Ch66当前417正文与6581末注，实际读完整新增/直接两侧/本人注并通过限定diff-check。此时真实非writer POST尚待，未先宣称本项生效；原124/旧§4未变。
- 后续reader R8已真实完整新增/直接两侧/本人注POST通过，root已实际消费并接纳07001整合、释放指定窄位；本人注仅同步既成状态。07013也已依root后续授权真实保存Ch24当前555单段与Review notes开头本人注2364，作者完整读回与限定diff-check通过，现等reader真实POST；未碰May09新段或其他书稿内容。
- 07481此前被作者误称为May11旧101候选，已定点核对纠正：它实际在旧ledger的generic preclosed，现README无该ID；不能去重冒已有效审阅。reader R6/R8检查发现07481/07088/07105/07191/07276/07915等的完整题摘有具体机制/安全反证，触发仅恢复相同错误理由实际影响的本次发现集合；不把86全部自动P。07726具体HPCrecipe关闭及06830科学范围排除仍成立。07481/07105/07191的exact-v1 ABS作者/reader已完整读、准入通过，才≤3定点core；日期DC已请求，未先计确定候选。其余三身份仍先exact题摘/日期，不先批量全文。
- Hunyuan动态目录已按来源要求尝试浏览器：首create在66秒超时并reset；随后inventory可见research?page=1，但getTab25秒仍超时；Mac locked是native观测错误，不把该列表存在当已读取11条或补窗无事件。必要历史切片恢复仍普通工作，未以锁屏提前冻结整日报。

### A4.7 07076 — 作者Source读足，独核已读，具体owner/PRE待核

- SCoL exact-v1完整 `SUP_CORE_RETRY_2605.07076v1_20261018.raw`；ABS/DC联合包络May11（registered02:11:23Z）。贡献：固定更新位置或外部context难兼顾累计保持 → 当前已漂移模型提出where-update、逐候选inner LoRA评acquisition/retention后commit，再用整流偏好对round-start而非最终drifted模型做outer IPO → 重新考虑在线更新policy与被写入参数是同一状态的反馈；2+2+3=7，深入。
- 双方已读§3/§4/T1–2、§5/T3、§6与直接A.10/A.13；作者另定点读A.11–12/A.14和B.1–B.3必要部分，不把它们扩大为reader范围。K10候选/复制与reward训练不同于SQuAD eval K1；Fisher是分析关联而非selector因果说明。固定last10在§4.2正文的retention20.10接近20.46、LongBench长流BatchTTT41.5高于SCoL37，是关键替代与反侧，不能称全胜/无遗忘。A13表/文字full-vs-no-forget归属冲突，不能照录精确长程趋势/配方，仅采mode concentration风险；AppA11 retention明示不是正文指标，不拼分母。
- 原稿监督/无监督reward、顺序inner copy/适配/score、outer IPO与评估10answers的费用分开；H200长流/HW并非生产场景，未核实现/复现。正文拟只采用闭环update-location接口，不采用完整算法收敛/通用无遗忘保证。
- actual owner `TRAIN-SFT` Ch29：目前1024“Trainable Layer选择要区分Necessity与Plasticity”只讲静态selection/causal ablation与architecture内适配；1030“Trainable Subspace也是Continual SFT评估变量”承载trainable set/depth/state/task order，但尚缺当前模型决定其下次写入位置、inner commit与round-start outer反馈。Ch30只own LoRA参数化，Ch77 derived外部memory不接管参数更新。已读Ch28/30开篇与Ch29上述完整局部，拟在两个heading之间一段，待readeractual owner/PRE。

> 连续到来的上下文还可以让当前模型提出“下一次更新哪些层”，而不固定同一adapter位置：每个提案在当前权重副本上做受限适配，分别测新信息取得与旧信息保持，再提交一个候选；这次commit又改变下一次提出位置的模型，因此选择policy与被更新参数处在同一反馈环。外层若用流中候选形成的偏好改进round-start初始化，必须与继续更新最终漂移权重分开。[受限自巩固对照](https://arxiv.org/html/2605.07076v1)支持这份where-update接口，却不证明Fisher相关性是选择原因、静态后层无效或长流优于batch访问；副本、inner LoRA、候选reward与顺序更新都付费，更多outer rounds还可使选择集中。保持依据、解析或预算失配时，保留固定更新集合、独立adapter、可信replay或可回滚context/RAG，不让一次局部取得替持续知识保持签字。<!-- source-family:SF-2026-ARXIV-2605-07076 -->

reader已实际读Ch29两个heading及完整两侧/Ch28–30交接，R11已确认07076具体gap与本段逐字PRE。尚待root共享窄位授权；不由prepared自写。固定last10反侧位于§4.2正文（不是Fisher Table2，前记表号已纠正）。

### A4.8 06933 — 正式Source/owner与逐字PRE草稿

- MAGIQ exact-v1完整 `SUP_CORE_RETRY_2605.06933v1_20261018.raw`；ABS/DC registered May11 02:08:02Z组合同日。传统PQ-TLS只认证传输而任务消息预算仍可跨session复用 → user签名的session-bound hash chain逐task-msg消耗、Merkle聚合one-to-many子预算、provider discovery ACL与接收方时钟分责 → 重考虑加密安全/联系授权/总预算/内容语义应分别验收；2+2+3=7，深入受影响机制。
- 双方必要§2.3/3、4.1、5 theorem/证明sketch、6.1–2与6.8已读；作者另§4.2–4.4必要流程/6.3–6.7。没读完整F证明，不称全proof已核。UC结论只按static-corruption、trusted CA/user protected software/hardware、可用honest-but-curious provider、PQ-TLS/globalRO/clock的条件引用，不批准实现安全。至少一honest端才有有效预算执法，both-evil/语义安全/DoS不在结论；状态型签名/nonce、session绑定/时钟和拒绝规则须保留身份。
- performance只作成本边界：XMSS一次约36s预计算，SAGA与MAGIQ使用smolagents/AutoGen不同框架，network模型与providercost为有限测量/估算。6.8的0.336与文字identical0.176冲突，不采用constant/零负担/任意拓扑扩展结论。未核实现/复现。
- actual owner `AGENT-MCP` Ch83“从调用能力到委派远端任务”245–273已有身份/权限、task/message/artifact映射、可选幂等/效果对账及workspace/TTL协议边界，但未有每个task-msg与总预算的可核销cryptographic token。Ch82决定委派策略，Ch81处理真实执行/补偿，Ch72拥有通用安全，不另复制该具体协议。拟在workspace协议原型两段后、本章边界总结前单段；待readeractual owner/PRE。

> 加密会话还不能自动限制一次委派能发送多少任务消息：用户可以签署绑定session的hash-chain终值，每发送一个task-msg消耗一个可验证前像，再以Merkle根承诺多个子session的预算分配；发现服务核联系ACL，接收端另核消息顺序与时钟预算。这把传输认证、联系授权和可核销额度分开，不让新连接重置同一session总额。[受限协议设计](https://arxiv.org/html/2605.06933v1)依赖受信用户软件/密钥状态、CA、同步时钟、可用provider及至少一诚实执行端，不能约束双方恶意、证明消息内容安全或防DoS。签名预计算、证明、状态与每次验收仍付费，one-to-many还需显式分配而非复制总额度；身份、时钟或余额不能确认时拒绝该session并回到显式小额度/本地许可，不以PQ-TLS成功替业务授权或最终effect验收签字。<!-- source-family:SF-2026-ARXIV-2605-06933 -->

### A4.9 07574 — 正式Source/owner与逐字PRE草稿

- PolarVLM exact-v1完整 `SUP_CORE_2605.07574v1_20261018.raw`；ABS/DC registered May11 02:23:13Z组合同日。RGB在反射/透明场景缺物理判别信息 → 真正新增偏振观测、分路尺度归一/分阶段新模态对齐 → 重考虑把sensor补证与放大同一RGB模型混为一谈；2+2+2=6，具体长期接口差额深入。
- 双方已实际读§3–6/T1–2、§7与AppC/E T3–4。只采双路/训练与测量合同，不照抄AoLP arctan/近零DoLP/S0未闭合处为精确无损recipe。frozen RGB encoder不等LoRA LLM整个函数或旧通用能力不变；attention ratio非因果routing证明。GPT4o-mini参与合成标注、text-only reference judge与重复次数未披露，不能认证真实物理/动作安全；特定编码reflection4.09低于raw-angle4.44，不授所有任务最优。两个RTX5880 Ada48GB/4bit NF4+BF16只是受限训练设置；新sensor、branch/token、两阶段训练/生成标签及独立原任务回归都付费，未核实现/复现。
- actual owner `MULTIMODAL-REPRESENTATION` Ch23“Fusion：在哪里让模态相遇”690–696的两段已写异质sensor dense/global选择性对齐及冻结局部不等全模型保持；随后Early fusion只有强模态可能支配梯度/位置。这里缺真实新增物理观测、周期/尺度接口及先单独对齐新branch避免RGBshortcut的具体分工。Ch22/24开篇交接分别为状态与生成path，不拥有观测融合；拟在该sensor两段后、Early fusion前一段，待readeractual owner/PRE。

> 当RGB本身无法区分反射与透明表面时，继续放大同一视觉encoder未必补回缺失信息；新增偏振测量则改变可观察证据，接口须声明物理量、角度周期、配准与尺度，而不把它们当额外RGB通道。一条受限分支保留冻结RGB路径，让新分支先单独建立语义对齐，再归一后拼接两路tokens并适配共享读出，以减少强RGB捷径掩盖新信号；冻结局部权重不保证共享LLM或旧任务保持。[有限双流对照](https://arxiv.org/html/2605.07574v1)支持这份阶段/消费分工，但单一text-reference judge、合成标注和个别编码切片反退不证明物理真值、因果路由或全任务最佳。新传感器、配对、两路编码、额外tokens和训练/原任务回归均付费；标定、质量或总预算失配时，保留原RGB/专用物理接口与独立场景核验，不从更高VQA均值批准真实动作。<!-- source-family:SF-2026-ARXIV-2605-07574 -->

### A4.10 07210 — Source/具体owner与逐字PRE

- DiffRetriever exact-v1，完整`SUP_CORE_RETRY_2605.07210v1_20261018.raw`，ABS/DC findable/arxiv.content/unique-v1与当期日程联合May11。原先AR显式生成扩展会串行付费或单一pooling折叠意图 → K个mask在同一次双向pass上读hidden multi-vector与词表logit sparse，再hybrid → 重考虑表示producer与索引/搜索预算共同配置；2+2+2=6，具体接口标准深入必要对照。
- 双方实读§3/4、5.1–5.4/T2–3、6.3–4/7与Limitations（作者另6.1–6.2，未称全AppA）。same pass不等same FLOPs；Kp16 index为Kp4的4倍、Kq带多次search。AR cap zero-shot20与SFT4不同，15×headline不搬trained配置；Dream从Qwen另加diffusion训练，不采“只改解码”严格因果。DenseFT和Hybrid零样本不是同一winner，test-label per-query oracle不可部署。synthetic随机token/index、单H100、5warmup/20runs与BEIR7边界、训练和索引成本保留，未核代码/复现。
- actual owner Ch76“检索表示决定可表达的匹配”341–410：已有完整MaxSim/硬选单view近似、训练阶段与SAE词典倒排、向量数据面，但未承载共享bidirectional masked pass同时产生多向量/词表稀疏读出的producer接口；不是只再教MaxSim。Ch75输入设计、Ch77 derived memory不接管检索表示，Ch23/24只own通用表示/生成路径。拟在multi-vector总论后、局部多模态重排前单段，待reader实际owner/PRE。

> 检索表示的producer也可以复用双向生成模型：在query或passage后接多个mask，让同一次forward的各mask hidden states成为多向量，再将mask位置的词表logits聚合为稀疏权重；dense的MaxSim与sparse索引可以分别消费同一编码结果。这避免为每个扩展逐token自回归生成，却不使多个mask成为独立语义真值，也不消除K份表示、索引和query搜索的费用。[有限扩散检索对照](https://arxiv.org/html/2605.07210v1)支持这个共享producer接口；diffusion额外训练、AR输出cap和zero-shot/微调配置同时变化，不能把所有收益只归因同pass，更不能把使用test label的逐query oracle当上线混合器。模型、mask数、pooling、索引revision与检索预算须共同验收；训练、重编码、K路搜索和hybrid调参全付费，迁移或净预算失配时保留专用encoder、单向量/完整late interaction和已验lexical/hybrid，不由更高检索均值授答案事实或生产延迟。<!-- source-family:SF-2026-ARXIV-2605-07210 -->

### A4.11 07220 — Source/具体owner与逐字PRE

- Guidance-support exact-v1，完整`SUP_CORE_RETRY_2605.07220v1_20261018.raw`，ABS/DC联合May11。旧误读可能把过强guidance离开density当永远离开support，或把support保证当条件分布保证 → 指定几何/精确score下固定strength的终点support距离收敛 → 重考虑终点集合、密度与有限步安全三种结论；2+1+3=6，必要理论条件已读。
- 双方§1.1/2、§3.1 Thm3.1/3.2与Remarks3.2–3.3、§4.1 Thm4.1/4.2、§5/6实读。compact convex各component有interior、positive target weight与density下界、exact score/guidance、γ≥1固定；每个strength有可更紧的κ0。离散tk→T无限网格在step condition下，不是固定NFE硬约束。support距离→0不等条件density/likelihood匹配或物理正确；前向L2 score-error不控制guidance shift人口，非凸仅2D toy。未遍历完整附录proof或实现/复现。
- actual owner Ch24 561–587现有局部score敏感性/函数-导数误差、h estimator/MC与tilt oracle边界，缺“固定guidance在理想条件可趋目标support，同时仍不取得目标density/有限网格资格”的区别。拟在h estimator之前、Blind denoiser段之后一段；Ch23是表示、Ch25是动态预测，均不拥有guided生成路径。待reader实际owner/PRE。

> 引导后的路径还要区分“落入目标support”与“按目标密度采样”：在各分量compact convex且有interior、目标权重和密度下界为正、score与guidance精确等条件下，一条[受限终点理论](https://arxiv.org/html/2605.07220v1)允许固定的guidance strength不小于1，使连续反向过程趋近目标support；离散结果要求网格趋终点、步长随剩余时间收紧，不能当有限NFE的硬约束证书。strength越大，允许的步长常数还可能越紧；到support也不证明条件分布、likelihood或真实物理正确。实际learned score在前向人口上的小L2误差，未必控制guidance移位后的查询，因此score校准、网格、完整生成和独立终态评价都付费。几何、估计或预算不成立时保留较保守guidance、原sampler及可核的输出约束，不让理想support结论替真实质量或动作安全验收。<!-- source-family:SF-2026-ARXIV-2605-07220 -->

A4.8/A4.9逐字PRE已由reader actual owner通过，root随后授两指定窄位；作者已保存原稿单段与本人注并完整读回，待真实非writer POST。07076同样已依窄授权保存，未用prepared自授生效。07013 reader R10 actual POST与root接纳已完成，指定窄位已释放。

### A4.12 07481 — 安全反证Source与具体NC

- Vaporizer exact-v1，`SUP_CORE_2605.07481v1_20261018.raw`完整；不是旧101有效候选，而是generic误闭后重新准入。2+1+3=6，安全边界必要深入。作者与reader实读§3–6/Tables2–7；v1 ABS/DC日期原件另核，不以Submitted单证。
- 旧单一检测命中会混淆信号退化与内容保持 → lexical/translation/paraphrase扰动共同测removal和BERT/readability/grammar → 重考虑双目标及detector operating point，不复述“密码水印彻底破解”。仅100 ChatGPT写作prompts，未逐样本人工语义等价；PRW以Z<0、SynthID g<0.5，没有匹配FPR校准，生成model/关键水印配置未闭，协议不同的100/23/14不合并scheme排名。4070Super12GB、512chunk与minutes/sample不授生产通用费用；hybrid quality检测仅提议，未证有效。未核代码/复现或附录图像点值。
- **拟已有覆盖：Ch72安全**当前244的regeneration transformation class与content/identity代理分责、263的posthoc text rewrite功能正确人口/生成检测预算及266–270的soundness/unforgeable recovery/Hamming每块边界，已经明确原制品/派生物、transform、key/null、模型/阈值、效用分别验收，paraphrase不自动满足密码假设；Ch67 281–292仍只授sensor。本文在未匹配FPR/未闭watermark配置下不能推翻这些具体选择，也未验证新mitigation，因此保留反证在报告，不把作者强宣传写回书。不是主题式generic排除，待reader actual具体NC。

### A4.13 07191 — Source与具体NC

- Attention Transfer exact-v1完整`SUP_CORE_2605.07191v1_20261018.raw`，generic误闭后准入；2+2+2=6，必要设计反证。作者与reader实际§2–6/T1–6/Fig3–6必要文本，reader另AppC；作者未称AppC已读。
- 旧少数ViT family attention-only transfer可恢复teacher收益 → 20teacher/11family复制或distill attention时4family低于scratch，补随机初始化的native LayerScale/PreLN/relative bias后逆转 → 重考虑路由权重、归一/scale/位置的共同计算context。matched-size softmax ViT classification、3seeds/20epoch+部分100epoch，不迁往任意feature FT/LLM或linear attention。v1 §5.2 standard student实际晚层KL spike，不能写“全部attention已精确matched仍无效”或借v2 intrinsicquality结论；native-scratch更差支持interaction而不是新模块容量单独更强，单因素recipe反例也非穷尽因果。未核代码/复现。
- **拟已有覆盖：TRAIN-SFT Ch29当前358–370**已完整要求teacher/student层计算责任、空间对齐指标不代held-out行为、跨架构末层也不授可迁移、未蒸馏student基线和蒸馏teacher/student配对budget。Ch23开篇的tensor≠semantic compatibility及内部language block改mask/position即改变原函数（93）也守这份计算context。此文的native ViT rescue是该条件的新具体证据，不改变本次已采用的“匹配计算责任并以真实行为/原student验收”选择；不另把norm/LayerScale名称堆进长期链。待reader actual具体NC；如实际owner仍有接口差额可重考虑，非按旧generic关闭。

### A4.14 07161 — Source/具体owner与逐字PRE

- SREGym exact-v1完整`SUP_CORE_RETRY_2605.07161v1_20261018.raw`，ABS/DC组合同May11。旧静态故障与最终诊断混合评价 → 可组合fault/noise、隔离injector plane、诊断checklist与state/client mitigation两oracle及metastable持续probe → 重考虑环境恢复时点与系统健康的区别；2+2+2=6，具体接口必要深入。
- 双方§2/3 setup/T3–5/§5已实读；reader另AppB/H，作者不冒该额外范围。90curated不是3623组合全验证；3runs/problem、1800s失败封顶计均值。噪声可改善某些slice，不授单调恶化；LLM诊断仅抽100专家核非全gold。largest40services/简化噪声/少agent，不能授生产安全/全部fault真实，未核代码或复现。
- actual Ch66 1218已区分fault定位/目标恢复/健康regression，5000–5030区分firstharm/observe-locate-intervene和数值fault；尚缺trigger停止后故障自维持、需独立client持续probe，不从注入器恢复推断服务恢复的具体动态环境合同。拟在Failure Catchability两段后、数值Fault前单段。Ch65管调度、Ch67管线上telemetry，不拥有benchmark恢复oracle，现有静态Cornetto不重复搬写。待reader实际owner/PRE。

> 运维Agent的环境还可能在注入trigger撤去后继续失效，因此“注入器已复原”不等于服务恢复。故障与背景噪声应能独立组合，控制注入的plane要与被测系统隔离；诊断按故障层级/服务/类型单独检查，mitigation再由系统状态和真实client请求的健康probe验收。对metastable故障，probe需在trigger结束后继续观察，而不把一份正确诊断或动作执行回执计成恢复。[SREGym的受限环境](https://arxiv.org/html/2605.07161v1)支持这份评价分工，不使全部可组合故障都获验证，也不证明噪声必然降低成绩；诊断judge仍有人工抽验与覆盖限制。环境部署、隔离、重复运行、持续client负载和超时失败全计费，真实故障或健康oracle不匹配时保留独立事件复盘、人工确认及原隔离测试，不由benchmark成功批准生产修复。<!-- source-family:SF-2026-ARXIV-2605-07161 -->

07076/06933/07574已由reader R13真实完整正文/两侧/本人注POST通过，root已消费接纳并释放三指定窄位；累计五本轮整合及两具体NC有效。07210/07220 R14 actual Source/owner/PRE通过，未获root窄授权前不写。新generic07088/07276/07915双方exact-v1题摘校准P后才≤3请求必要core。

### A4.15 07105 — Source/具体owner与逐字PRE

- Exact-v1完整`SUP_CORE_2605.07105v1_20261018.raw`；generic误闭后题摘准入，2+2+3=7，理论边界深入。双方§2/3.1/3.2/4.1/4.2、§5/6、AppD与AppE/T2–3已actual读足；未称完整appendix证明或实现/复现通过。精确KL正则exponential tilt optimum才gain=λ Jeffreys，base样本的self-normalized covariance估计需normalizer/integrability，不是有限样本无偏保证。bounded rewards、iid且pointwise unbiased ensemble才有期望O(n^-1/2)，不涵盖共享偏差/相关judge。
- 旧KL移动量只作保守约束 → 在固定objective/理想optimum下可用base样本估reward-KL reference frontier → 重考虑算法优化缺口与reward目标错配的分账。BoN近frontier仅Zephyr7B/BeaverTails和Pythia1B/TLDR两组经验，不授通用最优/同费用；10k/base samples和全部reward/搜索计费。E明确highest+smooth选run，TLDR PPO更高两run因noisy未画，不能叫纯best-run最大；small λ方差放大、gold代理不等真实安全。
- actual Ch31“从Reward到Policy objective”355–398已有KL目标/beta/冻结reference与过优化，但未有理想optimum收益的可计算reference frontier；“改变输出分布是目标”407有tilt不等人类行为，461–489有独立reward验收。拟在beta过强/过弱段后、样本选择/anchor reset前一段，不改变Ch32/33实际训练算法，待reader actual owner/PRE。

> 固定reward与reference以后，还可以把“这个目标允许的收益”与“训练器实际取得的收益”分开。对精确求解的KL正则目标，最优分布是reference按exp(reward/beta)倾斜；其期望reward增量等于beta乘双向KL之和。将它改写成base样本上的归一化协方差，可在训练前估计一条reward–KL参考前沿，但normalizer和必要矩必须有限，self-normalized估计也不是有限样本无偏证书。[受限理论与两任务对照](https://arxiv.org/html/2605.07105v1)不授BoN通用或同费用最优；图中RL run还按收益与平滑性共同选择，不能当穷尽最强训练器。小beta会放大高reward尾部方差，独立同分布、逐点无偏且有界的reward ensemble才继承所述收敛率，共享偏差不会因平均自动消失。全部base生成、reward评分和搜索都付费；目标、估计或预算失准时保留冻结reference、较强KL和独立人评/任务verifier，不以接近proxy前沿认证真实安全。<!-- source-family:SF-2026-ARXIV-2605-07105 -->

### A4.16 07243 — Source/具体owner与逐字PRE

- SpecBlock exact-v1完整`SUP_CORE_RETRY_2605.07243v1_20261018.raw`；双方§3.1–3.4、§4/T1–2、A.3/A.5、D1–2/F actual。2+2+3=7。K个dependent positions经layer shift，target→selfcached cross-block、valid-prefix loss与rank branching具体贡献；并非detached rankhead使joint token训练完全不变。A5仅抽象M.verify(tree)，没有完整非独立proposal rejection/correction/cache proof，不采exact sampler已证。
- 旧固定drafter更新集合/总是update会吞掉省下时间 → verifier信号/interval实测净throughput让skip/head/full成为per-query action、两copy异步sync与退步rollback → 重考虑在线adaptation更新面而非只更新频率。A10080GB batch1/HF3targets/2temps；短MTBench/HumanEval不测adapt、NQ/MT静态部分落EAGLE，accepted length非速度；sameGPU共享SM/dual同步不免费，2Kmix重复8epochs不是freshstream泛化。
- actual Ch48当前470–504已有独立trainer/候选revision/异步同步与回退，422等已有block dependency/训练分布；尚缺head-only/full update面按净费用选择。拟在online drafter第二分支完整两段后、跨进程提交协议前一段；Ch47管KV分页/Ch49管执行plan，不接管更新policy。待reader actual owner/PRE。

> 在线刷新drafter还可把“是否训练”与“训练哪些参数”一起选，而不把更新集合永久固定：用target在拒绝位置已给出的token及drafter对该token的概率提出漂移信号，在skip、仅更新输出/rank heads和更新完整drafter之间，按后续测量区间的净throughput决定动作。两份副本把训练与当前提议分开，同步到新revision及连续退步回滚仍是显式状态，不能让bandit取得target接受权。[SpecBlock的有限对照](https://arxiv.org/html/2605.07243v1)支持这份成本/更新面分工，不使更长accepted prefix自动更快；短请求流可能无法摊销训练，同卡stream仍争用SM、双卡仍付同步费。其tree verifier只给抽象接口，不能据此宣称非独立block proposals已有完整等分布证明。特征捕获、两copy、反传、测量与同步全计费；信号、验证合同或净收益不成立时保留固定更新集合、离线drafter和target-only，不由局部吞吐批准生产SLO或概率正确性。<!-- source-family:SF-2026-ARXIV-2605-07243 -->

### A4.17 07308 — Source与具体NC

- AT-VLA exact-v1完整`SUP_CORE_RETRY_2605.07308v1_20261018.raw`；双方§3–5/T1–3 actual。2+2+2=6。新接触信号由gate决定state↔tactile query切换，复用slow视觉/语言K/V并以fast tactile3:1动作；inactive同接口不等fine-tuned权重/原能力未变。六任务30–50demo/15trials同Genie1，VTLA/RDP只contact片段且人工理想初态，Unscrew强于AT，不做全局排名；40ms只是作者声明，未闭完整硬件/tail。T1 GO1 Stamp.13/T3 Ex0.33不混统一基线；heatmap只是hypothesis，missing modality仅两noncontact+Stamp，不涵盖任意sensor failure。sensor/contact人工标签、训练/gate误判和陈旧slow状态全费，未核代码/复现。
- **拟已有覆盖：Ch26当前577–598**已有slow-KV/fast fresh observation与更新比例/预测年龄、TacVLA接触flag控制模态参与/不授动作安全、随后慢预测与快真实触觉消费者分责。AT用query替换而非mask额外tokens是具体架构分支，但本次采用的“接触时才消费新触觉、按双时钟验收freshness、局部同接口不保证全功能/物理安全”的设计选择已实际承载；不必为另一query-switch实例重复同链。Ch23 fusion的模态消费权与局部冻结边界也不因此改变。待reader actual具体NC，非仅因为视觉应用。

### A4.18 07326 — Source与具体NC

- GEM exact-v1完整`SUP_CORE_RETRY_2605.07326v1_20261018.raw`；双方§3–5/T1–6 actual，2+2+2=6。range-map VQ tokenizer与frame-diff/temporalmean cues引导dynamic/static/generic三路bounded-offset scan/interpolation+Mamba再gate fuse；这些是未标注变化线索，不是已识别真实object/运动因果，ego/遮挡可混杂，不照录Eq4索引与Eq5边界未闭recipe。GT futureego与integratedplanner(AR)分责，BEV what-if图不授物理counterfactual真值。nuScenes3s AbsRel低于Copilot，KITTI MMD2.18>2.07、KITTI360 FRID94>Text2LiDAR72.3且MMD2.71>Weather2.59，未全胜；mean/median稳定proxy非tail/跨seed保证。8H20/80epoch+1.2Msteps与4090FPS不是完整自主系统SLO，tokenizer/三路径/diffusion/planner全费，未核代码/复现。
- **拟已有覆盖：Ch25当前226–245**已分开ego propagation/变化proxy、静态补全与动态预测、非语义change不得充作真实object motion、latent动力学分工不授物理因果，及futureego/真实观察/独立controller权限。GEM的按cue改scan path是另一个局部实现，受测优势与指标反侧不改变“变化线索须有对应producer/consumer身份、预测/分布相似非物理/动作验收”的本次长期选择；Ch23仍拥有codec/几何表示，Ch26拥有真实control。拟具体NC，不将三路Mamba名称作为新长期owner；待reader actual判断是否仍有可复用接口差额。

### A4.19 07088 — Source/具体owner与逐字PRE

- VLA membership exact-v1完整`SUP_CORE_2605.07088v1_20261018.raw`；generic误闭后双方题摘准入，2+2+3=7，安全反侧深入。双方§3–6/T1–3及AppA1–3/T4–6已实际读足。action-error黑盒仍要candidate GT action+原instruction；无GT时temporal smooth/curvature仍查询候选obs/instruction，OpenVLA强、pi0-fast/pi0.5近随机/弱，不授全VLA。trajectory membership fraction rho是定义，不是自然provenance真值。
- 旧文本loss/概率访问限制 → action误差与整段生成轨迹的时间差分也泄漏fine-tune成员线索 → 重考虑privacy sensor的访问与sample unit。A1 sample10k各类但存在轨迹相关，trajectory仅100member+100nonmember，经验FPR分辨率1%，表0.1%不授独立低误报校准。LIBERO LoRA微调不是pretraining个人数据/真实robot，perturbation降低AUC非DP；mitigation只OpenVLA Spatial，action效用与安全可退。训练、query/episodes和defense全费，未核代码/复现。
- actual owner Ch72“Membership Signal必须先通过可识别性审计”361–389已绑定corpus/revision/control/访问与低FPR边界，但当前以text/PII和概率/feature为对象，未表达action-output与trajectory unit；Ch26只拥有动作闭环，不能接管privacy verdict。拟在现有membership两段及marker后、PII提示线索前单段，待reader actual owner/PRE。

> 动作输出也可能携带训练成员线索，不必向调用者开放token概率。对VLA，比较生成动作与候选示教动作的误差仍要求已知候选ground truth；跨时刻的smoothness或curvature则可只读生成动作，但必须查询对应观察与instruction，且这种信号可在另一架构上接近随机。审计对象应分别声明transition tuple、整条trajectory及成员定义，不能把相关时间步当独立样本放大低误报证据。[有限LIBERO微调审计](https://arxiv.org/html/2605.07088v1)每类仅100条trajectory，经验误报刻度为1%，不从表列0.1%授可部署阈值，更不据高AUC判定真实用户数据或法律归属。查询、示教身份、训练与防御校准都付费；给动作加噪虽可能降低泄漏，也会伤控制效用，不构成DP或安全保证。成员真值、对照或攻击接口不可核时保留Unknown，继续provenance/canary和明确邻接的隐私审计，真实动作仍交独立controller验收。<!-- source-family:SF-2026-ARXIV-2605-07088 -->

### A4.20 07276 — Source/具体owner与逐字PRE

- Signal-reshaping GRPO exact-v1完整`SUP_CORE_2605.07276v1_20261018.raw`；generic误闭后双方题摘准入，2+2+3=7。双方§3/4、B、C2/C4/C5、D2必要实读。layered outcome/step权重/三资源execution opportunity而非新GRPO；C5 fullmasked仍R0进入groupmean/variance，只不直接gradient，不能称完全不影响训练。context/max_tokens可能policy相关，不照录全无因果宣称；R.5含judge failure/skipped，Missing≠semantic failure。
- 旧同prompt默认比较机会一致 → inference/sandbox/compile分资源、按exitprovenance处置并分开参与statistics/直接loss → 重考虑mask和group population的控制责任。C2 400人审按checkpoint/judge正负各50分层，不是自然人口，2pp净偏差及Rogan–Gladen校正/CI不采用，sharedjudge不能自动排除差异偏差。单model/internal C++1110train/400eval、singlefork且未逐项governance消融；D2 privilegedhint masked-sum KL入reward改advantage，非直接reverseKL/所有OPD无效。总时长非等预算，processjudge非oracle，零分保护/完整精确recipe未闭；全费/未复现保留。
- actual owner Ch33 111–140 groupmean/std与不同人口、399–430 processcredit分责已有，但缺异常/执行资源导致无有效机会与真实policy失败、zero loss mask仍改组统计这一控制接口；Ch31 own reward定义、Ch35 own资源执行，Ch33 own group comparison。拟在sample-relative baseline解释后、SPRO段前单段，待reader actual owner/PRE。

> 同prompt的rollout还必须得到可比较的执行机会：GPU生成、sandbox操作与编译若共用一个并发额度，排队和资源失败就可能被误记成策略失败，应分别保留资源预算与exit provenance，再决定哪些结果可进入组比较。逐步process分数只重分一条轨迹的直接更新权重，不等于改变其outcome或识别真实因果；零loss mask也不意味着不影响训练，若异常样本仍以零reward进入group mean/std，其他样本的advantage已经改变。[受限compile-fix分支](https://arxiv.org/html/2605.07276v1)还把judge失败/跳过与语义失败合在partial reward，因而本项目要求另存Missing状态，显式规定它参与哪些统计，不能照抄为已校准语义排序。资源隔离、完整失败rollout、judge/step标注与训练都付费；无有效执行机会、judge或分组失准时保留可信outcome-only、可重放完整组与环境复核，不让mask或更多过程标签自行批准稳定、无偏或真实修复安全。<!-- source-family:SF-2026-ARXIV-2605-07276 -->

### A4.21 07915 — Source/具体owner与逐字PRE

- PAE exact-v1完整`SUP_CORE_2605.07915v1_20261018.raw`；generic误闭后双方准入，2+2+2=6。双方§3/4/T1–3、F、B1/C3/D1必要层已实际读；不称全Appendix proof/实现已核。frozenVFM+detailmodulator/projector，SSR空间Gram、stopgrad邻域级MCR及pooled/patch SCR和fixed refinedprior，把重建与下游diffusion learnability分责。Eq1 fusion后LayerNorm，不照字面H_z=raw VFM unchanged；SSR axis须绑定，不补完整recipe。
- 旧只在anchor重建或继承强feature → 另约束邻近latent逐级decode consistency及结构/语义target → 重考虑codec邻域与生成消费者。singleImageNet256classcond、A100/50tokenizer epochs、80/800generator epochs、250steps/50k；CFG/unguided换ODE/SDE与schedule，不以gFID降签IS/recall/细节/同总费用全胜。SSC用GTsegment数定K、LPC小可因decoder不敏感、GSQ只100类×5subset，变换后Pearson相关非因果/生成保证。prior预训、teacherfeatures/DAM、三loss扰动decode与全采样费保留，未核代码/复现。
- actual owner Ch23连续表示439–469已区分channel/空间容量、重建/理解/生成，缺anchor以外邻域一致性target与decoder敏感性的具体合同。拟在串行bottleneck完整两段后、共享语义主干细节旁路前一段，Ch24仍own训练后采样/solver，不接管codec损失；待reader actual owner/PRE。

> 重建anchor之外，连续codec还要为生成器提供可学习的邻域：可在冻结视觉prior旁补细节，再压成latent，同时用空间关系与语义target约束布局，并让相邻扰动幅度的decoded结果逐级接近、较近一级停止梯度，而不是强迫所有扰动都回到同一原图。它改变codec的训练目标，不保证真实语义流形已恢复；decoder过于不敏感也能让局部变化很小，必须与重建、语义和下游生成联合验收。[PAE的有限图像对照](https://arxiv.org/html/2605.07915v1)支持这份分工，但依赖refined VFM prior与单一固定分辨率，几何proxy或相关性不构成生成质量保证。Prior准备、细节分支、扰动decode、codec与后续generator训练/完整采样全付费，CFG与solver变化也须分账；细节、语义或净预算失配时保留原VAE/representation codec、普通重建目标与独立生成验收，不由较低gFID批准任意分辨率、视频或无损表示。<!-- source-family:SF-2026-ARXIV-2605-07915 -->

### A4.22 07237 — Source与具体NC

- ThinC exact-v1完整`SUP_CORE_RETRY_2605.07237v1_20261018.raw`；双方§3–5/T1 actual，2+2+2=6。single strategic NL→code/output loop→answer，12.2k正确/无错误蒸馏+SFT+GRPO/DAPO；解释器执行不使hardcoded/建模/逻辑正确，99.2%只answer出现于任一output的proxy而非因果依赖或全步验证。Recovery@k是先k步自然错误条件子集，k5降33.3，不当故障注入/恢复因果；SFT先退、RL/筛选/budget联合，ASTER非全控制格式单因果。avg@16不是bestof16/pass16，32K同cap非同总费，baseline各推荐temperature；1.7B/4B竞赛数学不授其他domain。
- **拟已有覆盖：Ch78当前71–76**已有模型生成program在受控interpreter消费中间回执、保留原逐步接口、joint训练/工具/harness混杂不能单归控制流、self claimed_verified非externalproof；819另把AST执行与语义/授权分责。Ch29/33分别own训练target/GRPO，不因流程短就新建推理owner。ThinC是受限数学任务的程序中间计算分支，不改变上述解释器只验证执行而不认证推理/任务的长期选择；拟具体NC待reader actual，不按工具调用题名泛排除。

### A4.23 07177 — Source/具体owner与逐字PRE

- HyperEyes exact-v1 `SUP_CORE_RETRY_2605.07177v1_20261018.raw`；双方实际§2.1/2.3、§3、§4/T2–5、A/E/F4–5必要域读足，2+2+2=6。把bbox作为搜索参数融合grounding/retrieval，同turn并发查询；TRACE同时约束round与总invocation，failed-only reverseKL只是loss mask，不使共享参数下成功行为不变。旧串行crop→search接口 → 原子grounded query及同轮多查询改变动作粒度 → 重考虑轮次和实际调用预算的联合验收。
- Main表accuracy取原papers、turns本地测；AppE native tool/summary/temp/checkpoint不同，不能从混合协议授Pareto或5.3×真实延迟；CAS是手工权重非实测秒/钱。E的19turn/18calls与F4训练配置分开，不拼统一budget。Table5 matched teacher仍FVQA/LiveVQA小退；minsuccessful reference不是goldoptimal，全部teacher/搜索/训练费保留。未核代码/复现。
- 作者actual读Ch78当前工具架构完整总论与后续harness反例（约793–801），已有粒度/版本/harness责任但缺bbox直接作retrieval参数、并行round和调用数分账的具体分支；Ch77 memory不接管动作表示，Ch79仍own多步plan。拟在该总论marker后、专用harness反例前唯一段，待reader实际owner/逐字PRE。

> 视觉检索的动作粒度可以从“先crop、再search”改成携带image identity与局部bbox的grounded query，让后端消费同一观察坐标，并在一轮内并发多个实体查询；这减少串行交接，却不证明框已正确或检索证据真实。同轮并发仍发生多次外部调用，预算要同时记录model rounds与total invocations，不能把少轮次当少费用或真实延迟同比下降。[HyperEyes的有限图像/文本对照](https://arxiv.org/html/2605.07177v1)还联合冷启动数据、效率reward与teacher训练，不能将总收益只归接口；不同原生工具/摘要器和主表混合测量也不签发统一Pareto排名。观察revision、bbox变换、搜索/teacher/训练与失败重试全付费；grounding、证据或预算失配时保留串行crop/search、原图回读与已验证窄工具，逐项权限和effect-time检查仍由executor持有，不由更短轨迹批准任务真值或安全。<!-- source-family:SF-2026-ARXIV-2605-07177 -->

### A4.24 07327 — Source/具体owner与逐字PRE

- Teacher-Feature Drifting exact-v1 RETRY；双方actual§3–5/Limitations、T1–2、AppC/T7、AppA训练预算到precision/clip必要层读足，2+2+2=6。旧drift需另学/依赖表征encoder → 直接以冻结diffusion teacher的中间feature作距离，并给弱覆盖anchor加density-relative margin → 重考虑metric producer与正向/反向覆盖责任。p=q⇒field0只单向，不授识别性/分布相等；teacher feature不认证pixel/semantic真值，maxpairSSIM只重复proxy。Eq12 M/N索引未闭不搬精确recipe。
- ImageNet64 EDM U-Net TFD1.58仍不及DMD2 1.51；SDXL FID18.39但CLIP.332低于DMD2.336/Turbo.337，不采“无牺牲alignment”。AppC加入U1明显退，U-Net未验证DiT，noise/layer需校准。AppA FP16、正样本不足时teacher50stepCFG6生成、完整codec/feature/训练费；单次FP不等训练/端到端免费。未核代码/像素图/复现。
- 作者actual Ch24 958–970完整FlowConsist及drift/vectorfield两段到SnapFlow已读；现有正文已区分scalar loss/非保守场，但缺teacher内部metric与anchor侧覆盖目标。拟在drift两完整段后、SnapFlow前单段；Ch23保持codec表示owner，Ch24拥有此generator训练目标；待reader实际owner/逐字PRE。

> Drifting的距离空间也可以由冻结diffusion teacher自身提供，而不额外引入表征encoder：给真实/生成样本适度加噪，读取teacher多层feature，在该空间构造吸引—排斥目标，并以anchor侧的相对density缺口补充生成样本未覆盖的邻域。这改变metric producer与监督方向，不让“两个分布相同则field为零”的单向命题反过来认证样本分布相同；teacher feature或较少重复也不是真实语义与完整coverage证明。[TFD的有限U-Net对照](https://arxiv.org/html/2605.07327v1)显示layer/noise选择敏感，更多层可明显变差，较低FID也伴CLIP分数弱于其他少步基线。Teacher准备、正样本不足时的完整teacher生成、feature前向、anchor比较与student训练全付费，单步推理不抹去这些代价；metric漂移、覆盖或质量回归时保留外部encoder/普通drift、原score/flow目标与较多步teacher验收，不由内部feature自签DiT迁移、无损或全预算优势。<!-- source-family:SF-2026-ARXIV-2605-07327 -->

### A4.25 07399 — Source/具体owner与逐字PRE

- GPO-V exact-v1 RETRY，双方§3.1–3.5/§4/T1–3、A6/T6和A8文本actual；2+2+3=7，安全/设计反证必要深入。旧固定prefix代理AR拒绝 → bidirectional masked refinement可在后续填入拒绝 → 重考虑全sequence/steps及完整decoder的红队验收。默认latent whitebox不等pixel BB，crossmodel pixel transfer另协议；两模型/A80080GB/128tokens/150×anchor优化，FPO人为100%prefix不是实跑GCG公平排名。Eq7负词prose与R+公式/方向未闭，不采精确lossrecipe。
- A6 tokeninjection仍有JSR18.7/24.3，未自适应重攻/良性效用，不授可靠防线；A8人/AI同rubric、人数CI缺口，JSR/FPT非真实harm。未核A8图片prompt/代码/像素复现。全优化/完整decode/teacherjudge费用保留。
- 作者actual Ch72 790–808白盒无指令token攻击与后续良性反事实两完整域已读，旧prefix≠harm/预算分母责任有效，但缺masked后向上下文引发progressive refusal的时间机制。拟该白盒prefix段/marker后→良性反事实段前唯一段，需root按May13共享章顺序协调；待reader实际owner/PRE。

> Masked语言生成还会改变拒绝的时间接口：早期固定prefix看似服从，后续双向refinement仍可在其他位置补入否定、终止或新的拒绝，因此prefix命中既不是最终服从，也不是完整有害输出证据。红队应绑定整个sequence、refinement/commit轨迹与最终policy judge，而不是直接复用自回归prefix成功率。[GPO-V的有限视觉模型反侧](https://arxiv.org/html/2605.07399v1)支持这个区别，却主要用latent白盒优化，跨模型pixel转移是另一攻击协议；人为强制FPO前缀也不构成等预算攻击排名。优化、全步解码、外部harm判断与良性效用回归都计费，词频和同源rubric不替真实危害；简单token干预仍有残余命中、未经过自适应重攻时不能自称防线。轨迹、威胁接口或judge不可核时保留Unknown、完整输出/effect gate及已核红队suite，不由局部拒绝或服从给发布签安全保证。<!-- source-family:SF-2026-ARXIV-2605-07399 -->

### A4.26 07333 — Source/具体owner与逐字PRE

- Softmax ICTD exact-v1 RETRY，双方§2.2/3–6/8、F5/F6必要实际读；2+2+3=7。完整proof/代码未核。固定prompt两memory行与temporal predecessor shift实现batch weighted TD；dualhead→singlehead+TSM只对构造参数/初始化精确，非任意Transformer删头。有限ergodic MRP/fixedpolicy/确定reward、context遍历每state、每state kernel diagonal≥(1+γ)/2+margin才能contract；不是kernel均值大即可。NEU globalmin为context先∞再depth，非SGD必学/唯一算法；L(2+γ)^(2L)/n项不能授任意联合极限。
- Boyan shared3layer/sparsemask、5seeds/maxemergencecheckpoint；F5放松mask另加diagonalbias，F6float64只是数值构造identity非真实LLM验收。旧attention构造feature后在线least squares → 明确reward/value memory与时移实现TD递推 → 重考虑attention前向可承载的算法状态及收敛条件。
- 作者actual Ch14 230–248单层能力与featurizer/least-squares两完整段已读，缺state-value memory+TD递推/每state contraction边界。拟featurizer两完整段后、可解码不等单点控制标题前唯一段；Ch13 position不接管RL value语义，Ch15不把特定重参数化变成通用删头。待reader实际owner/逐字PRE。

> Attention前向也可承载value更新而不修改权重：在prompt保留reward与两行可写value memory，用固定kernel聚合同一context的TD误差，再把一份聚合量时移到predecessor位置，让层深充当递推次数。这是特定softmax参数与初始化的构造，双head换singlehead+temporal shift的等价只限该构造，不能据此删去任意训练模型的head。[有限MRP分析](https://arxiv.org/html/2605.07333v1)还要求固定policy、遍历每state的context及每state足够的kernel对角占优；平均对角升高、toy训练出现相似权重或global minimum存在，都不证明通用LLM已学会TD或有限context已收敛。Context、memory、层计算与预训练费用仍在，深度/样本极限次序也不能互换；条件或任务行为不符时保留显式TD/外部solver与普通context读取，以真实value误差验收，不把可构造性当训练可达或策略改进保证。<!-- source-family:SF-2026-ARXIV-2605-07333 -->

### A4.27 07463 — Source/具体owner与逐字PRE

- Hölder approximation exact-v1 RETRY，双方actual§3、§4Thm4.1/4.2/Cor4.3及构造概览、§5/6完整、B5讨论；2+1+3=6，必要proof未全核。固定width/ReLU+softmax+residual+PE，α∈(0,1], d0>2α bounded Hölder类L2存在性通过quantize→单attention contextID→深value map；维度指数未消。Upper/lower有4倍exponentgap/log项，非工程D×W等价或单attention部署配方。B5称LN可吸收不能直接迁移真实LN/GELU/SwiGLU，§6 optimization tau未控且rate自认suboptimal，bound形状不证明实际risk先降后升。
- 作者actual Ch14 230–244单attention能力限制/后层非线性与构造featurizer完整已读，Ch17 366–400深宽动态/Norm分责无此quantize-contextID-value存在性边界。旧全局可见≠全局函数 → 构造中一attention仅负责离散context可分、深FFN仍承担value map → 重考虑用attention层数推断整个模型表达复杂度。拟Ch14单层能力段marker后、featurizer标题前唯一段；不采用精确regression theorem或最优工程深度。待reader actual owner/PRE。

> “一个attention层足够”还必须说明其余计算藏在哪里：对有界Hölder函数，一种存在性构造先用深ReLU残差前馈量化输入，再用单softmax attention生成可区分的context identity，最后靠深value map赋予目标值；attention负责可分，不是独自完成任意全局函数。[受限逼近界](https://arxiv.org/html/2605.07463v1)要求固定width、特定smoothness/维度与位置结构，深度仍随目标误差及输入维度增长，上下界也未闭合。它不是训练算法、通用删attention配方，省略Norm的构造更不批准删除真实模型的Norm或替换激活。表示误差、有限样本误差与优化残差须分账，构造与完整训练/验证均付费；任务、可训练性或预算条件不符时，保留多层attention/MLP与已验Norm宽深配方，不由存在性或上界形状认证工程最优与实际risk曲线。<!-- source-family:SF-2026-ARXIV-2605-07463 -->

### A4.28 07509 — Source/具体owner与逐字PRE

- MASPrism exact-v1 RETRY，作者actual§3.1–3.3.4/§4.1–4.5 Tables1–5/§5.1–5.3读足；2+2+2=6，reader必要Source待核。Prefix每step保宽度→NLL选symptom/attention提上游→恢复完整候选与症状第二prefill→NLL对比/多症状consensus排名，只有diagnostic routing非causal estimator；不解码不等不调用model。旧fulltrace长context/summary → 两pass选择性复原 → 重考虑观测代理与实际因果/告警的权限。
- 两benchmark全是已失败trace：Who&When HC51.60steps/AG8.72，TRAIL多span且LocationAcc是最多10预测location的recall，不拼Top1accuracy。HC27.59%、AG36.51仍低于A2P43.65；w/oFiltering GAIA73/117 OOM意味着memory与质量混杂，不能只归相关信号。Qwen3.0.6B/RTX5090/PyTorch2.7cu128；2.66s本地对17.82s hosted API和不同输入量，不授纯算法6.69×/生产SLO；deterministic repeat不等人口CI。Mixed成功/失败trace校准/falsepositive未做，head/layer/完整trace及模型访问前提、全部prefill/attention存储/人工核验费保留。未核代码/复现。
- 作者actual Ch69 177–235结构guidedgraph、Rootcausehypothesis→repair完整域已读，缺openweight内部NLL/attention的双prefill producer，但candidate≠cause/repair权限已有有效。拟structure-guided attribution完整段后、Root-cause graph之外ruleauditor前唯一段；Ch68保日志capture、Ch70保计费owner，Ch82不复制观测归因。待reader必要Source/actual owner/PRE。

> 原trace暂缺可靠dependency graph时，诊断也可以先用两次prefill提出待检查的step：第一遍给每step保有界prefix，以NLL异常找symptom、attention提名上游候选；第二遍恢复这些候选与症状的完整内容，重算信号并按多症状一致性排序。这避免先生成长诊断文本，却不把“不解码”变成零推理费用，也不让attention或surprise成为因果估计器。[MASPrism的受限失败trace对照](https://arxiv.org/html/2605.07509v1)只支持该诊断view，短trace另法更好，混合成功/失败人口的误报校准仍缺；本地SLM与hosted API的时延差不能单归算法。Openweight信号访问、prefix遗漏、attention驻留、两遍完整计算与人工复原都付费；关键内容漏选、内部信号或校准不可得时保留fulltrace/显式graph和人工调查，候选rank不取得修复执行权，真实原因仍需受控重放与独立outcome验证。<!-- source-family:SF-2026-ARXIV-2605-07509 -->

### A4.29 07632 — Source与具体NC

- Psych201 exact-v1 `SUP_CORE_2605.07632v1_20261018.raw`，双方actual主文Psych201→Discussion、MaterialsMethods与S1/S2文本读足，2+2+3=7。旧assistant preference提升是否意味着更像人 → 三family base/post同family行为NLL/choice accuracy负面证据、persona个体预测微小差异 → 重考虑normative assistant与humanresponse fidelity的验收目标。不是所有posttraining必损：Centaur面向behavior训练在heldout novel tasks提升为直接反侧。
- teacher-forced完整历史，只humanresponse spans，多token先sum再response平均；跨tokenizer绝对NLL不直接比较。报告同family d后跨experiment平均非参与者总体risk；10%或max100participant test、lightweight格式review不证zero contamination/全人口代表。无template因为该格式效果最佳，S1 caption未读像素；S2choiceaccuracy不支持sole determinism解释但不隔离唯一因果。Persona字段可缺、微小range不证明个体不可建模；模型/训练recipe混杂、engagement成因是解释而非受控验证。全部数据准备/评分/训练费，未核原data/代码/复现。
- **拟已有覆盖：作者actual Ch31 407–425**已有p_H行为分布vsr_P助手偏好、KL-tilt不使两者相等、heldout humanresponse likelihood/生成分布与prompt采样协议须独立验收。新负面验证支持这一具体判断，但未提供改变当前验收/后训练选择的新接口；不按心理应用或主题泛C。待reader实际owner NC。

### A4.30 07579 — Source/具体owner与逐字PRE

- POISE exact-v1 RETRY；双方actual§2–5/8、Alg1及B4–5。作者核leave-one-out value target与cross-rollout baseline；Alg1先固定历史probe对当前独立两rollout算adv/更新actor，后训练probe。2+2+3=7。旧critic额外模型/同题group费 → prompt+reasoning hidden/entropy轻probe用另一rollout估prompt value → 重考虑baseline的信息依赖与冻结/更新时序。固定历史f、独立rollout、stopgradient时raw scorefunction无偏，不继承PPOclip/tokenlength平均/multiinnerepoch。§2.3固定b covariance分解不能自动用于互耦crossrollout与随采样重训b。
- MAE/Var(A)不是全gradient variance，gradnorm低不唯一证明降噪；online critic可更准，跨domain只是probe非RL。B4主文batch数字与T5/T6配置须分开，表中512vs128prompt、120vs100steps、2vs8rollout与dynamic sampling齐变，不能纯probe倍率。4B Avg32 .500<.508、Avg32非pass32，B200/BF16未完整披露处不补；hook/buffer/probe、完整rollout/训练与长horizon缺口保留，未核代码/复现。
- 作者actual Ch32 66–97 promptscalar/SPPO→GenAC→视觉critic→固定critic LOO完整域已读，已有固定critic/action独立条件但缺actor内部other-rollout value predictor及先更新actor后拟合probe接口；Ch31定义reward、Ch33保groupbaseline而不重复本段。拟promptscalar结尾后→GenAC前唯一段，待reader actual owner/PRE。

> 不另训练policy规模的critic，还可以用actor已有hidden state与entropy训练轻量value probe，但“来自模型自己”不能取消baseline的独立性条件。每题采两条独立rollout，让一条的baseline读取另一条的features；先用历史冻结probe形成stop-gradient advantage并更新actor，再以当前交叉reward训练probe和维护短buffer，才避免用当前受更新rollout的reward反向泄漏入它自己的baseline。[POISE的有限RLVR对照](https://arxiv.org/html/2605.07579v1)支持这个producer接口，不把raw score-function条件无偏扩大为clipped PPO、多inner epoch或token长度平均的完整保证。Probe预测误差、advantage方差和gradnorm也不是同一个降噪量，promptbatch/rollout数/训练步数齐变时不能只归probe。Hooks、buffer、probe与完整actor采样/训练均付费；policy漂移、独立性或校准失准时保留独立scalar/token critic、可信group baseline与真实rollout验收，不由较少sample或较低gradnorm签发稳定、无偏或通用credit。<!-- source-family:SF-2026-ARXIV-2605-07579 -->

### A4.31 07594 — Source/具体owner与逐字PRE

- MemCompiler exact-v1 RETRY，双方actual§3–5/T1–5、C1–3；2+2+2=6。episode初memorypool按runtime taskprogress/environmentbelief编译；memory advice与briefstate更新独立四case、text后UNKhidden→Gaussianprojection→executor软token，旧static memory injection→状态条件消费接口→重考虑“什么时候读经验/什么时候改派生state”。主文fixedpool与C2逐stepretrieve、SFT训练Executor与C3始终冻结冲突，不采完整训练/检索recipe或原能力完全保持；Eq6 tilde来源/密度与C3目标不齐不补精确式。
- attention pre-softmax logit≠归一attention/utility因果，cosine/TSNE不证明独有信息。T1 55.67vsprose55.83/closedGPT身份不一不采排名；Table5 compiler2081.4+executor1003.2不等总token减半，.093+.12局部均值非tail。8H20/teacher/sim/SFT/RL/gate/latent全费；benchmark隔离声明未独验zero leak/真实动作安全，未核代码/复现。
- 作者actual Ch77 862–901 current transition guidance→stateconditional retrieval及完整两侧已读，已有局部经验/事实权威分责，缺advice vs briefstate两独立写出与text/latent消费接口。拟“更细粒度提高局部检索密度…”完整段后→repository temporal boundary前唯一段；Ch76保检索索引、Ch78仍own当前action executor。待reader actual owner/PRE。

> 取回的经验还可按当前子目标与环境belief重新编译，而不在episode开头一次塞满：compiler分别决定是否交付advice、是否更新brief state，允许只给建议、只改派生状态、两者都做或都不做；文本后追加的latent soft tokens则是另一消费通道，不是新环境观察。这个接口把读取建议与维护状态拆开，不能让自述完成进度变成事实，也不让latent和text在cosine或可视化上分离就证明信息互补。[MemCompiler的有限模拟对照](https://arxiv.org/html/2605.07594v1)支持状态条件消费，原文检索时点/Executor冻结描述不一致时不搬完整recipe。Teacher、模拟轨迹、compiler/softtoken训练、状态维护和每step额外前向全付费，executor输入变短不等总token减半或尾延迟保证；belief漂移、经验条件/净预算不符时保留原轨迹、text-only提示、简单状态规则或不注入记忆，当前action仍由独立executor与真实反馈验收。<!-- source-family:SF-2026-ARXIV-2605-07594 -->

### A4.32 06969 — Source/具体owner与逐字PRE

- FuScore exact-v1 `SUP_CORE_2605.06969v1_20261018.raw`；双方actual§3/4/T1–4/5、作者A4/A7/B3–4/C1–5，reader另A1/A3。2+2+2=6。维度均值分歧proxy→每image softlabel宽度，监督期望分数/within-sourcepair与cross-sourcepair Thurstone排序分别处理；旧单mean/固定labelsharpness→目标shape与pair比较人口分责→重考虑uncertainty label来源和排序有效域。Main已含scalar mean跨scene监督，不能说跨scene完全无监督。四属性std不是rater uncertainty；5expert/100sourcepair pilot Pearson.42仅相关，EVAFusion mean-only且overall=维度均值，不能拆aggregation与真实ambiguity。
- highdelta窄range不数学限制SRCC，11方法plateau与B4人为固定highdelta.21构造.78均非理论上限。sigma-conflict单独ranking几乎不增，crossfid pooled改善而within未全胜；singlecalibration vs50split ECE协议不同不相减，有限b*=0不认证所有scale。3seedensemble/跨method single seed非同费；A7只prep摊销，encoder+LM每adapter重跑，原latency表无ViT row不搬prose精确倍率。fullreference三图、A100batch1/100image不授实时SLO，冻结vision不保全模型函数；全部标注/LoRA/ensemble费，未核代码/原data/复现。
- 作者actual Ch66 484–504逐judge scale/低秩共识两完整段至candidatepool/currentprompt校准已读，已有judge相关分歧/共识非真值，但缺per-item属性冲突作为监督width、以及within/cross内容组两排序目标的具体分支。拟低秩分解完整两段后→“校准之外…”前唯一段，Ch31仍own reward优化、Ch67 monitor不接管label truth。待reader实际owner/逐字PRE。

> 监督数据只保总体mean时，score的期望、label分布形状与pairwise排序也可分开训练：用属性分数之间的冲突提出每item的softlabel宽度，维持其mean，再分别对同一内容组内的候选和跨内容组的候选施加排序目标。它给出了训练shape的代理，不是恢复了真实rater分布；属性权衡也会产生分歧，不能直接叫作人类不确定性。[FuScore的有限图像融合对照](https://arxiv.org/html/2605.06969v1)中，宽度监督单独几乎不改善rank，pooled排序改善也不等各内容组都更准；高冲突切片多方法接近，不证明理论性能上限。应保留原始rater/属性人口、组内组间比较和独立calibration协议，标注、训练与多adapter完整前向均付费；代理失配或真实rater方差缺失时保留Unknown、固定softlabel/直接回归与人工anchor，不由窄scale fit、相关性或ensemble名次给质量和安全签证。<!-- source-family:SF-2026-ARXIV-2605-06969 -->

### A4.33 07721 — Source/具体owner与逐字PRE

- MELT exact-v1 RETRY；双方actual§3.1–3.3/§4/T1–4/§5/C/F1–2必要，2+2+3=7。旧loop参数共享但仍逐loop KV → 每layer gated latent在loop覆写并投影KV、后token消费前token final-loop → 重考虑计算深度与cache增长的耦合/训练并行约束。对loop常数不是对context常数；chunk训练用fidelity换并行、interpolation+各loop KD+postattention alignment专门训练，非任意checkpoint无损dropin。
- memory是vLLM KV数+weights简单和非完整实测VRAM，Qwen更小且1.6vs1.4B不同权重，MQA命名不继承。T1非全胜、T4 phase2某pass10退且移KD部分更好，逐进消融非factorial。F2仅作者查代码/配置下earlyexit选logit未减compute，非本人验实现；MELT adaptiveexit未来。1040H100GPUh+所有teacher/loop/训练费；未核E完整稳定证明/代码/复现。
- 作者actual Ch19 211–237 logicalKV结构/HLA两完整段到Position已读，已有跨loop低维writer/reader/局部exact窗口，缺当前token循环覆写并把final-loop交后token的更新次序与chunk-training依赖。拟HLA两完整段后→Position标题前唯一段；Ch17 owns sharedlayer参数、Ch45 owns部署lifecycle，不复制本状态contract。待reader actual owner/PRE。

> Loop深度不扩cache还有一条不同于汇集历史loop的路径：每个layer维护一份latent memory，当前token在各loop以gate覆写，再投影为K/V；新token只有一行位置，但下一token必须消费前token完成最终loop后的状态。这把保存逐loop历史换成学习到的压缩更新，对loop常数不等对context常数，也不继承原模型函数。[MELT的受限迁移](https://arxiv.org/html/2605.07721v1)因而需要chunk-wise训练在并行与部署次序间折中，再用插值和teacher alignment适配；较低KV加weights估计不等完整VRAM或同质量SLO。所有loop、teacher与重训/回归都计费，部分质量仍低于原逐loop缓存，被比较的Ouro在作者所查默认配置下，early-exit只影响所选logit，并不省掉后续loop；MELT的adaptive depth仍未验；更新次序、训练或质量不成立时，保留逐loop显式KV、HLA式已验共享布局与普通decoder，不让固定memory名义批准任意adaptive depth。<!-- source-family:SF-2026-ARXIV-2605-07721 -->

### A4.34 07339 — Source/具体owner与逐字PRE

- FlowAgent exact-v1 RETRY，作者actual§3–6/T1–5，reader另A1–4/B4理论直接反侧；2+2+2=6，只采conditional flow生成完整latentanchors→embedding-distance tooldecode→strict firsttool commit、弃尾replan的表示/执行接口，不采原理论保证。主文smoothmanifold/strictmargin/Lipschitzutility/contractivefeedback很强；reader已核A1 square-vs-unsquared margin、A3缺训练proxy residual、A4自定义openloop envelope，不能从caption/remark授unseen/generalization/错误必衰减。
- executable重点retail、mainoverall混合source、database statechange .3529显著低oracle.7059；RAG PredExec1.0高于Flow.9619，不采全指标胜。三H80012.29min训练未闭全stage/等预算，§3.5含planRL而§5归功无simulation不能全归flow；多ODEsteps额外latency未量化SLO，seed/CI未披露。训练、latent编码/flow积分/工具与grounding全费，未核代码/复现。
- 作者actual Ch79 68–101教程prior→校准→commitment→learnedtransition真实观察交接已读，已有plan/事实/观察authority，但无连续latent整计划producer与firsttool丢尾的接口组合。拟commitment完整段后→“学习到的Transition…”标题前唯一段，Ch78保schema/真实effect验证，Ch24不接管Agent工具plan。待reader actual owner/PRE。

> Plan的表示也可先是完整连续latent路径：把rationale、tool embedding和observation编码成训练anchors，条件flow提议未来anchors，再按与当前可用tool的embedding距离解码；执行器只消费第一个tool，拿到真实返回后丢弃剩余anchors并重规划。这是一种receding-horizon proposal接口，不使embedding距离成为语义等价、参数合法或真实状态证明。[FlowAgent的有限工具对照](https://arxiv.org/html/2605.07339v1)支持该表示分支，但其理论需强manifold/margin/contractive假设且论证未闭，不能授未见工具保证或必然抑制错误。状态修改仍明显弱于oracle，部分parse/执行指标旧检索更好；多次ODE积分、编码、训练/搜索及全部工具执行均付费。Latent、grounding或净预算失配时，保留离散计划/逐步tool选择、已验retrieval与真实observation闭环，不因生成了全路径批准整条执行或替代effect-time检查。<!-- source-family:SF-2026-ARXIV-2605-07339 -->

### A4.35 07728 — Source/具体owner与逐字PRE

- SARC exact-v1 RETRY；作者actual§3.5–3.6/4/5、9.2–4/9.8、10.1–5必要域，reader另13.2/13.4，2+2+2=6。不是四Gate名字或hard≠reward作为新贡献；旧child缺少predicate所需state时可能丢检查 → deepest-decidable rescue/预算拒绝+spec-trace覆盖/authority chain intersection → 重考虑委派的约束状态依赖与检查归属。
- audit O(T*C)须finite spec/真实完整trace/每predicate bounded且可决定，不证明隐路径无bypass、规则真值/法律合规/物理安全。Classic reference-monitor实例化非新定理，rescued state可stale，Algorithm2仅orch rescue与正文deepest不是同一完整实现。1000orders×50seed synthetic exactpred已知，baseline刻意少某class响应；同throttle policy-as-code应近效，21ms是model参数非实测，fig2/3解析illustration非运行。FN/bypass仍受机会人口影响，单环境sweep不证明与机会rate独立；M/M/c meanwait<窗口不授hardtaildeadline，LLMchecker也非一概结构错误。未集成真实runtime/自适应attack/shadowdeploy，未核repo/复现；全predicate/trace/队列/审计费。
- 作者actual Ch82 586–628 identity/leastprivilege delegation与Spawn两完整段已读，已有authority收窄但缺继承predicate在child state不充分时的确定检查owner。拟“Delegation不能把…”完整段后、Spawn标题前唯一段；Ch83保协议objects、Ch72保policy来源、Ch69保trace取证，不复制本传播控制。待reader actual owner/PRE。

> 委派还必须传播约束的state依赖，而不只复制规则文字：若child没有计算某predicate所需的当前state，不能把“不可判断”静默当作通过，应在最接近执行且具备所需state的层检查、记录结果与时效；没有可在预算内完成的检查则拒绝或升级。沿call chain的authority只能取交集缩小，子任务回执保留实际适用约束、检查位置和结果，才能把spec与trace逐action对账。[SARC的受限架构说明](https://arxiv.org/html/2605.07728v1)支持这份归属合同，却不证明trace覆盖全部隐藏路径、predicate忠实表达规范或原state始终新鲜；synthetic exact-rule零违规和模型化毫秒数都不是部署安全/SLO证明。State传递、predicate、完整trace、审计与升级队列全付费，平均等待短也不保证每次赶上不可逆期限；state、检查或authority失配时保留最小权限、default-deny与人工/确定性当前检查，不让规则继承或可审计标签批准真实effect。<!-- source-family:SF-2026-ARXIV-2605-07728 -->

### A4.36 07649 — Source/具体owner与逐字PRE

- ODD sensor exact-v1 CLARIFY；澄清后双方P，作者/readeractual§III–V/TI–III读足，2+2+3=7（安全/评价反侧必要深入）。Coarse Mapillary类别高score不能替细ODD taxonomy readiness；upstream roadlabel/retrieval可能漏后续必要类别，falsepositive可触发多余fallback。旧只看平均视觉指标 → 绑定标签粒度/标注完备度与漏检/误触发两侧人口 → 重考虑sensor接controller的验收边界。
- ODD232concept×10、每图只predominant label，非穷尽multilabel不能算classificationFP；静态昼间EU/UK/US且排moving。Mapillary另task/label人口，centerdistance非IoU。Prompt组合非factorial、GPT4o选best后转移，prompt-only费用漏输出/5次image；chainedCoT .68不能称dependentpipeline必坏。原文.73不足是风险意见非认证threshold，离线合规/监管用途未验；模型revision/统计/预训练成因未闭，不采用模型推荐。全prompt/多图调用/独立标注与fallback费，未核repo/复现。
- 作者actual Ch66 300–315 CFHR joint/conditional、目标选择vs定位完整段与GUI段已读，已有conditionedpopulation但缺标签未穷尽的falsepositive资格及coarse/fine taxonomy迁移边界。拟CFHR完整段后→目标选择/定位段前唯一段；Ch26继续own controller/safety envelope不由视觉score获authority，Ch65不接管sensor真值。待reader actual owner/PRE。

> 感知指标还要绑定标签粒度与标注完备度：每图只标一个主要概念时，可以测该概念的recall，却不能把其他输出一律判为false positive；粗粒度常见类别的检测高分也不替细粒度风险taxonomy的覆盖。[有限ODD视觉评估](https://arxiv.org/html/2605.07649v1)显示这些人口的差别，上游先判road type或只检索少数标签还可能提前排除后续必要类别，更多分阶段提示并不自动改善。但策略组合未完全控制，不能由此判全部级联必坏或推荐某个部署模型。漏掉危险条件与误触发fallback须在各自真实标注人口另验，prompt/多图重复、标注与独立controller回归全付费；标签、动态环境或operating point不可核时保留Unknown、专用sensor/完整标签检查与安全接管，不从静态recall、中心点命中或平均F1批准上线、合规或物理动作。<!-- source-family:SF-2026-ARXIV-2605-07649 -->

### A4.37 07990 — Source与具体NC

- Toollinear exact-v1 RETRY；作者actual§3、§4.1–4.4与§5.1–5.2关键controls、Limitations，reader另§4.5完整必要域，2+2+3=7。固定menu residualmean-difference steering、prefix-vs5tokenexact、schema prefill与unembedding controls是具体贡献而非因工具主题入选。Matched-topic PCA同样低维，不授tool-specific压缩；natural parallel仅3%/0而matchednorm93–100，只说明输出方向可覆盖，不证明原mean唯一机制或instructiontuning学routing的因果。Basecos.998/.999微小argmax、ITreadout低于generation/strictparser3vs26%差额，不能称清晰原生子空间或唯一预训练故事。
- Schema prefill可同率、可fabricatearguments；Sports近同义0%、multi-turn n20/model -30..+10pp、不同工具描述长度/各模型域限制。14–21倍宣传与14%vs0、17%vs1口径不闭不采；lowgap只是局部sensor非可授权routing替代。全feature/query/方向calibration/steering和真实effect验证费，未核代码/像素/复现。
- **拟具体已有覆盖：作者actual Ch78 129–139**已把toolname选择时点/prefix改变参数续写与provisional routing分开；748–760 necessity-margin steering只改proposal、权限/effect独立；Ch67 149–158已有nativeactivation/probe与独立标签/evaluator、域移和全部费用。本文受限fixedmenu干预/低gap sensor不改变这些采用选择，不能把schema转换当完整任务或安全责任；不因为主题相似直接关，保以上新验证/反侧在报告。待reader actual owner NC。

### A4.38 07725 — 复用必要Source后具体owner与逐字PRE

- 精确v1必要§4–6/T1–2沿reader实际Source复用，不冒作者通读新收据。2+2+2=6：原将多turn teacher指导视为每步同质量→toolstate drift下以sampled-token mean absolute logratio提议step distillation weight、排除tool observation→重考虑teacher指导的时间资格。Eq7权重连乘可望远镜化，不称独立历史累积；不采未取得D4/5理论保证，sampled ratio非真实KL或可靠性证书。Qwen3.6/1.7学生、4/14B teacher、Python、avg32×5runs的有限证据；大teacher普通OPD反退、错后全mask损恢复信息、全部teacher/logprob/训练/工具费保留，C1费用域未取得不填倍率。
- 作者actual Ch33 1298–1330完整OPD总论、peer-conditioned指导、ratio及frozen-support两侧，Ch32/34交接已读；现有失配总论缺跨tool-response时间的权重接口。拟OPD三段总论后、peer-conditioned semantic marker前唯一段；唯一TRAIN-GRPO，不复制tool执行权到训练owner。待reader逐字PRE。

> 工具交互还会改变同一条rollout内teacher指导的资格：新tool observation到来后，teacher与student可能处于不同的状态分布，不能仅因teacher更大便让所有response等权蒸馏。一条[受限多turn分支](https://arxiv.org/html/2605.07725v1)在各response的已采token上读取平均绝对log-ratio，以此调节step指导权重，tool observation本身不进入该token蒸馏项，outcome reward仍单独拥有任务结果。但这份差额只是model-relative proxy，不是完整KL或teacher正确性；所写相邻权重乘积可望远镜化，也不等于保留独立的全路径历史。该Python与有限teacher/student配置中，大teacher的普通指导仍可退步，错误后全mask也会丢掉恢复信息。所有teacher forward、概率读取、工具与训练都付费；状态或proxy失配、质量净收益未过独立验收时，保留普通OPD、outcome RL与原verifier，不由step权重认证泛化、收敛或零成本。<!-- source-family:SF-2026-ARXIV-2605-07725 -->

### A4.39 08083 — 复用必要Source后具体owner与逐字PRE

- 精确v1原件已有完整必要§2–5/T1–3/§7，reader实际Source复用，不要求HTML闭尾或重读全部附件。2+2+2=6：原在线为每候选controller重复生成→冻结branch/probe replay pool供explorer编程并读全trace→重考虑离线搜索与真实执行验收的分界。128预采/model/problem、500tokens、64子集复用并非独立线上人口，未揭示probe不入state，池外prompt/state/branch不可回放成真反事实；离线零generation probe不授线上免费。五轮discovery39.9$/160min不含precollect/model/storage/真实服务；AIME24用于selection非heldout，4B更多tokens仍有AIME25退步、8B62.7低SC62.8及.6B反侧，不采全Pareto。AppD完整controller recipe未取得，不补EMA或tail/SLO。
- 作者actual Ch20 370–405完整entropy分叉、token tree、程序重采、selector、adaptive SC及completed-trace完整链，Ch19/21交接已读；这些控制线上追加而缺固定环境先搜controller/留出真实执行的阶段接口。拟distinct-leaf两完整段后→程序重采段前唯一段；唯一MODEL-SAMPLING，Ch56保服务资源budget。待reader逐字PRE。

> 预算策略本身还可先在固定的离线环境中搜索，而不为每个controller反复生成全部候选：预采并冻结branch与probe结果，让explorer根据已揭示状态和完整交互trace写出controller，再把冻结策略交给留出任务与真实运行验收。[受限replay搜索](https://arxiv.org/html/2605.08083v1)减少的是这份池内试验的重复generation，不把未揭示probe交给当前state，也不使池外新prompt、工具状态或分支成为已验证反事实。重复抽取同池不增加独立人口；搜索用AIME24不算held-out，更多token在部分配置仍降低质量，不能由单个trade-off宣称全Pareto。预采、模型、存储、搜索、全部在线probe/生成与验证均付费，离线零generation成本不继承到线上。Pool、任务或model失配时保留固定预算、普通self-consistency与独立verifier，外层deadline和服务SLO仍须实测，不让搜索得分批准真实提交。<!-- source-family:SF-2026-ARXIV-2605-08083 -->

### A4.40 07985 — 必要Source复用、具体owner与逐字PRE

- Dooly exact-v1 RETRY；reader实际§2–8/T2/B/C/D/E/G/H必要Source原域直接复用，2+2+2=6。旧逐model/config重复profile→op/model-tainted符号及module primitive attributes签名与动态维度sweep分开→重考虑跨配置profile的可复用单位。Hash不证明物理同latency，保hardware/software/precision/topology；unresolved维度⊥、值碰撞、custom dispatcher fallback及phasebranch假设，random MoE路由均值非真实负载，noop collective非实测通信。DoolySim只vLLM，不把SGLang taint/profiling移成全E2E；36配置/12相似7–8B/3backend与ShareGPT4 .5req/s有限，未核像素点值/代码/复现，不采全MAPE/SLO。全trace/context/dedup/profile/regression/通信费。
- 作者actual Ch49 18–82完整计算图/typedstate/候选族复用/图优化原理→WebGPU→冷启动链、Ch48/50交接；缺的是实测profile签名的静态/动态分层，不是新代数等价。拟图优化第一性原理段后→WebGPU marker前唯一段。唯一INFER-TENSORRT-LLM，不让Ch67重新own执行计划。待reader actual PRE。

> 性能测量的复用单位也不必等于完整model名称：可以追踪实际operation及其model依赖，把影响kernel选择的符号和module属性纳入签名，再对仍会改变执行费用的动态维度独立sweep。[受限trace/profile系统](https://arxiv.org/html/2605.07985v1)借此减少相似配置重复测量，但hash一致只说明声明签名相同，不证明任意输入、backend或设备有相同latency；未解析维度、值相关分支与自定义dispatcher须保留未决或fallback。Profile仍绑定hardware、software、precision与topology，随机MoE路由均值和no-op collective不能替真实负载不均与通信。Taint/profiling支持某backend也不自动支持其端到端simulator；trace、去重、参数sweep、回归与真实通信都付费。跨架构、branch或实测误差失配时重采原始profile、回成熟backend和真实请求验收，不从少量相似模型的复用率批准生产SLO。<!-- source-family:SF-2026-ARXIV-2605-07985 -->

### A4.41 06835 — 必要Source复用、具体owner与逐字PRE

- exact-v1 CLARIFY；reader实际§3–5/B/C/E/H必要Source直接复用，2+2+3=7，隐私测量直接反侧深入。原以closest-record质量heuristic作隐私替代/强假设攻击不可得→ClavaDDPM单表训练/知识/分布/compute不完备黑白盒MIA仍有信号，DCR平而TPR变化→重考虑synthetic数据发布的威胁与metric资格。固定FPR为0.1=10%绝非0.1%；balanced rowlevel非user，Berka每人多record；10target×200/Diabetes3×1000不当大量独立用户。DCR依Euclidean onehot/train-holdout规模，Ensemble distance组合仍可有效，不推所有distance失效。TF可单shadow但Ensemble1primary+16RMIA/background800k/70k；feature2100timesteps/Optuna/所有训练全费，不采单模型零aux或跨A40/A100费用倍率，未核代码/数据/图像/复现，不采噪声索引recipe/未来DP缓解。
- exactABS uniquev1 ThuMay7 18:42:35Z，sameDOI arxiv.content/findable registeredMay11 02:05:44Z与Sunday最早界联合May11，双方实际核。作者actual Ch72 352–383完整可执行probe→MIA identifiability→actionprivacy→PII，缺synthetic closest-distance与有效攻击知识不完备的对账。拟MIA原完整段/marker后→actionoutput段前唯一段；唯一PLATFORM-SECURITY，Ch27继续own数据合成。待reader actual PRE。

> 合成数据的“离训练记录不近”也不是隐私证明：closest-record距离受编码、train/hold-out规模和总体分布影响，审计应把它与已声明访问权限、辅助知识和预算下的成员攻击并列，而不让质量heuristic代签泄漏风险。[单表diffusion的受限审计](https://arxiv.org/html/2605.06835v1)中，不完备攻击知识仍可产生成员信号，DCR近似不变而攻击成功变化；这不证明所有distance攻击失效，组合distance的攻击本身也可能有效。原实验FPR为10%，balanced row-level challenge不等真实用户隐私，尤其一人多record时要另声明privacy unit；阴性也不认证无泄漏。Shadow/reference、背景合成数据、多个噪声特征、classifier与搜索训练全部付费，单shadow配置不代表其他攻击无需辅助模型。人口、编码或权限不可比时保留Unknown、匹配held-out/canary与明确邻接的正式保护，不从较远的近邻、低攻击分数或未来缓解提议批准敏感数据发布。<!-- source-family:SF-2026-ARXIV-2605-06835 -->

### A4.42 07994 — 必要Source复用、具体owner与逐字PRE

- SemanticSmoothing exact-v1；reader实际§II–VII/VIII-D/F关键证明必要层复用，2+1+3=6。独立count估计→真实logit-Lipschitz假设使语义邻近分布可作KL side information，插值上界与uniform sideinfo特定lower界→重考虑何时借邻居统计可有证据。必须真实process同L/eps/outputnorm条件，不由任意embedding距离推KL证书；IV2 min界proof仅择source端点，不认证实际softmin/1/x混合必达min。fixed-d o(1/n)非任意d/n，lower仅uniform与Delta<1/4；IV4+log2不丢，Eq19启发距离漏项不当精确recipe。WikiText100k/10k bigram/tokenizer与test-vocab、GPT2只作embedding、synthetic oracle trueP与重复row条件保留，不横比现代LM PPL；全部neighbor/count/embedding/calibration费，未核实现/复现或全lowerproof。
- 作者actual Ch12 95–108几何近邻→矩阵表示→跨checkpoint行及355–369诊断完整链、Ch11/13交接；缺的是以真实logit光滑性明确限定统计共享，而非cosine代表语义。拟距离近不能等语义完整定义段后→矩阵表示段前唯一段；唯一MODEL-EMBEDDING，Ch20不重复计数估计论证。待reader actual PRE。

> 邻近几何若要支持共享统计，还需给出预测分布的条件：当真实process的logits确实满足已知Lipschitz、近似误差与读出范数约束时，邻近项的分布才可能成为有界KL side information，帮助稀疏count估计；任意embedding最近邻不自动满足这份合同。[受限语义平滑分析](https://arxiv.org/html/2605.07994v1)给出这种有条件的共享边界，但取较好source端点的上界不证明实际启发式混合权重达到同一界，固定维度的渐近率也不外推任意大维度/小样本。小规模bigram与部分oracle构造不替现代LM端到端perplexity或加速验收。近邻搜索、embedding、计数、尺度/权重校准都付费；真实分布、常数或support不可核时保留独立count、成熟平滑与留出likelihood，不把距离、共享参数或一个上界批准语义真实性和部署收益。<!-- source-family:SF-2026-ARXIV-2605-07994 -->

### A4.43 07773 — 必要Source复用与具体NC

- Shortboard exact-v1 reader实际§2.1–2.3/3/4.1–4.2复用，2+2+2=6，受限组合反侧按具体命题深入。MetaGPT五角色SOP/Snake单任务/ENGQA最多5轮/~10rep；替role同时改model/行为/style/费，递增weak替换非全组合，ENG0 product平凡、曲线无独立holdout/CI，不采乘法因果/真实团队管理律。LOC/1000token与T/LOC效率方向冲突，不继承精确排名；sixfunction完成proxy非软件生产正确性，未读S1–S4/价格/像素/代码/复现，不为此补无关附件。
- 拟具体NC：作者actual Ch82 18–36费用baseline、38–87独立观察/责任与coordination税、136–155异构worker/固定routing完整链，已要求model/role/scaffold和总预算共同比较、task-dependent topology、正确性与协调费分责。其非最弱role也影响受限结果/少debug虚高效率，是这些既有选择的局部验证，不新增可执行的product或最弱role替换规则；报告保反证及未识别因果，不因Books主题相同自动关闭。待reader actual NC。

### A4.44 07984 — 必要Source复用与具体NC

- exact-v1 RETRY reader实际§2–5/A/D baselines/all-layer/fullposition必要域复用，2+1+3=6，解释直接反侧深入。三family rhyme任务readable vsintervenable：Gemma27B newline patch，Qwen/Llama仍lastword，不能外推同层/scale；5promptpairs×20samplings非100独立prompt、clusterbootstrap无全peak/topk选择校正，Pile21k tokens相关；Claude1200+CMU选择偏差。Top5路径patch足改输出≠native必要/唯一planning模块，作者Conclusion明确还需scrub/ablation区分自然读出与人工注入；D Wilson忽略pair相关不采精确CI/90%fraction。全部forward/feature/multiprobe/patch/search费，未核像素/代码/复现。
- 拟具体NC：作者actual Ch66 289–301完整内部可分性/容量null/同条件干预前基线、非目标行为与解释文本↔组件交换两完整链；Ch67 143–159 native vs重排调用/独立标签/校准。已有“内部可分≠控制，干预有效≠完整因果架构”的选择，本文受限押韵位置差异并不要求删除probe或批准native必要性，具体新反证保报告；不因仅机制解释论文泛排。唯一PLATFORM-EVALUATION-SYSTEM已有覆盖，Ch67只作监测交接。待reader actual NC。

### A4.45 07800 — 必要Source复用、具体owner与逐字PRE

- exact-v1 RETRY：reader实际§3–4.5/T1–3/§5、AppC rubric文本/F训练/G反侧直接复用，2+2+2=6。旧global feature alignment不区分text目标entity关系→entity-separated特征与text-conditioned AND/OR/XOR pair-weight路由（OR包括FGFG/FGBG）→重考虑distillation对齐哪些局部关系。K+2mask BCE/embedding InfoNCE训练aligner，再冻aligner供mTRD，不称普通featurematching改名。500K/800 topentity内部人口/mask-caption噪声、三VLM mean/vote非独立，sharedjudge偏差不自动constantoffset；32GPUstage1/40batchstage2/allteacherrewriter费用。High-noise专家训练与low专家shift未干预隔离，不称joint必fix；T2 HumanFidelity85.07<pre86.04/Physics48.50<SFT51.09，single stage2seed1024/200clips userstudy缺raterCI，未核像素/代码/复现，不采全优/realvideo严格upperbound。
- 作者actual Ch24 954–976从drift场/归一化→TFD teacher metric→SnapFlow完整链，Ch23/25交接已读；TFD保metric producer却未明确text条件选择哪个entity pair。拟TFD完整段后→SnapFlow前唯一段；唯一MULTIMODAL-GENERATIVE-PARADIGMS，Ch23继续own观测表示。待reader actual PRE。

> 特征蒸馏还应区分“用谁的metric”与“对齐哪种关系”：可先学习分离entity的表示，再由文字条件决定foreground/background之间哪些pair参与监督，使AND、OR或XOR式目标不被单一全局相似度混合；OR也可能同时需要foreground–foreground与foreground–background关系。[受限视频蒸馏](https://arxiv.org/html/2605.07800v1)冻结训练好的aligner供生成器消费，并不免除mask、caption、aligner与teacher的训练费。内部top-entity数据与共享VLM judges仍可能引入model相关偏差，不能当作不改排名的常数；部分fidelity/physics指标还低于参照，单seed与有限userstudy不授全任务更优。高噪声expert的改进也不证明低噪声expert天然兼容。Pair路由、数据和跨阶段支持失配时保留global/较保守alignment、原teacher与多步路径，并独立验最终质量、关系保真及全预算，不由局部表征分数批准物理真实性或无退步迁移。<!-- source-family:SF-2026-ARXIV-2605-07800 -->

### A4.46 07931 — 必要Source复用、具体owner与逐字PRE

- exact-v1 RETRY，reader实际§4/5/T1–8/6/D/F/H复用，2+2+2=6。原未来world feature高token负担→每frame/view worldmodule仅一个token、joint latent/action flow→重考虑未来监督的带宽及动作consumer，而非取消原visionencoder/allVLA tokens。Beta fusion是fixed scalar、tokenweight才动态，Beta(1.5,1)近1不近0，L1不等完整density/物理状态。T5 MetaWorld标题却LIBERO列/T7与T1冲突/avg不闭不采精确gainrank；H5gain高H30不单调、1token最好限30KLoRA且fulltoken OOM/timeout混杂，各suite validation选AH/replan不等同config，PCA Fisher非信息保留/因果。Piper三任务20trial扰动无seedCI，8A800/teacher/编码/未来ODE费用，4.81FPS局部非SLO，未核实现/复现。
- 作者actual Ch26 184–202 occupancy单token/路径depth/状态估计器→闭环、238–250 latent计划consumer及其两侧，Ch25/27交接已读；现有压缩分支缺future condition与action共同flow的producer/consumer差额。拟occupancy完整段后→路径深度段前唯一段。唯一MULTIMODAL-EMBODIED-VLA，Ch25不把learned future升为observed state。待reader PRE。

> 未来条件的带宽也可单独限制：让每帧、每视图的future-world module只输出一个token，再以联合latent/action flow学习它与动作的关联；这不删除原视觉encoder，也不是把整条VLA输入压成一token。[受限未来条件接口](https://arxiv.org/html/2605.07931v1)改变的是预测condition的生产与消费，固定的fusion系数不能写成动态view权重，latent回归更不认证完整世界分布或真实未来。最佳token数依训练预算与配置，full-token的OOM/超时不等纯信息瓶颈证据；表格口径冲突和按suite选择配置也不支持统一收益或随horizon单调改善。Teacher、编码、pooling、联合训练与未来ODE全付费，局部FPS不替完整控制deadline。压缩、预测或动作质量失配时保留原观测、较宽/显式condition与独立controller，短horizon重观测或停机，不由单token或联合生成授权物理动作。<!-- source-family:SF-2026-ARXIV-2605-07931 -->

### A4.47 07971 — 必要Source复用、具体owner与逐字PRE

- DVD exact-v1 RETRY reader实际§3/4/T1–3/5/C/E1–2/I/H knowncategory必要域复用，2+2+2=6。原masked不可改提交或连续binary近似→native categorical binary stage1、uniform corruption反复更新及BSP clean/noisyblocks训练匹配→重考虑修订对象与knowncontext在哪一层保真。Stage2仍TRELLIS连续latent不称全3D离散。Entropy currentmodel/time/threshold proxy非校准uncertainty/固有shape；Eq5 log0/proseweightedmean与MDM staysmasked矛盾不搬recipe。450K/64A800/trainschedule、GT voxel对齐、train2500评估、BSP额外100K/halfspace人口均保，Toys FIDpc4.64>4.51/textCLIP小退非全优；known voxel回写不保decodedmesh/语义。256NFE20sA800只是stage1，secondstage/align/render/entropy/oversample/train全费，未核代码/复现。
- 作者actual Ch24 797–815 reverse核相关性、uniform corruption两完整段/训练locality邻接，前masked 690–720提交/entropy条件段已读，Ch23/25交接复用；缺binary stage与下游mesh decoder之间的保真边界。拟uniform corruption完整两段后→locality标题前唯一段。唯一MULTIMODAL-GENERATIVE-PARADIGMS，非Ch25物理world真值。待reader PRE。

> 原生binary状态也可以直接作为categorical生成对象，而非先把0/1放进连续Gaussian近似：uniform corruption允许已取值位置继续更新，训练再混合clean context与noisy blocks，使局部修订见过相应条件。[受限3D两阶段分支](https://arxiv.org/html/2605.07971v1)只在第一阶段这样生成，后续仍经连续latent与decoder，回写known voxel只保持该离散接口，不能保证最终mesh或原语义完全不变。按当前entropy分配修订预算也是model/time/threshold相关proxy，不是校准的固有形状不确定性；不同训练规模、GT voxel对齐和额外block训练不允许把全部差额归为corruption。部分CLIP与点云指标反退，stage1秒数还未包含后续生成与render。全部训练、反复去噪、扫描、对齐与下游decode都付费；known-context支持、解码保真或总成本失配时保留原连续/保守masked路径和真实输出检查，不由binary精确回写批准无缝编辑、实时或物理正确。<!-- source-family:SF-2026-ARXIV-2605-07971 -->

### A4.48 07926 — 必要Source复用与具体NC

- exact-v1 RETRY，reader实际§2/3/T1/4.1/4.3/T3/A5–6/B1/D必要域复用，2+2+2=6。具体增量DAG deterministicflag/incremental disclosure、partialresolved/discovered/endtask分账、premature调用与真实upstream provenance；nodecount非pathdepth，不采superlinear或唯一reasoning bottleneck。人类每item至少一solver声明与同interface一次solve80–98%有冲突，不授全可解；graph reachability非自然文本充分/OOD无污染。capDifficulty20=160actions与T3call214等单位未闭、prose最少calls与表冲突不采效率rank/精确fees；singletrial/不同thinking实际token不等同预算，rulemapping taxonomy非生产因果。未核实现/复现，全部生成/验证/调用费保留。
- 拟具体NC：作者actual Ch66 4974–4986 Constraint Graph完整两段/marker与Release交接，已使versioned graph共同约束case、合法解、disclosure schedule与deterministic state predicates，且区分generator/simulator与真实outcome；Ch79 140–170 ready dependency/merge/checkpoint完整链和Ch78 contract/真实effect分责配合。本文resolved/discovered计数与premature指标细分在报告保留，但不改变当前graph/state oracle和依赖完成后才执行的选择，不把synthetic图count当生产reasoning因果。唯一PLATFORM-EVALUATION-SYSTEM已有覆盖，待reader actual NC。

### A6. 日期/来源有限恢复收口（2026-10-19；不授无遗漏）

#### 日期能力与24具名保留

- `SUP_ARXIV_CS_MONTH_20261019.raw`8218B为404，正文Invalid Year:2605；错误入口不作能力缺失。已纠正`https://arxiv.org/list/cs/2026-05?show=2000`，`SUP_ARXIV_CS_MONTH4Y_20261019.raw`3191012B实际200、total18979/当前1–2000，按ID序，仅年月无日组/公告日字段。这里只核其日期恢复能力与目标身份，不读整月候选，不继续十页做无效日组搜索。
- 定点复用root提供的[真实官方Advanced表单能力原件](../daily-20260513/sup-raw-20261018/arxiv-advanced-date-form.html)，只读日期接口说明，不读邻日候选：date_type有original-submission/announcement，443–460与549–558明确announcement及排序仅year/month，不能伪造day参数。原四exact OAI metadata May12也不提供首公开下界；Submitted仅日程下界。46已入选项是同一可用联合方式确实把完整区间限定May11的成功校准，不因个别字段独立不足否定组合。
- 2026-10-19实际辅助查询`site:arxiv.org/list "2605.08301" OR "2605.08314"`与`site:arxiv.org "Polestar" "May 11" "2026"`返回空，只证明此有限搜索未恢复dated官方公告，不是零命中证明。已有exact ABS/DOI/OAI、月列表与官方表单均未给这批日级下界，当前未识别可继续产生该历史日公告的原始入口；不为所有假想channel无限抓取。后续须真实dated首公告/历史new listing目标身份、或其他官方可复查约束把整个区间限定同BJT日；只重开受影响项。此为外部日期材料保留，不采正文/评分/Books/无遗漏，未说窗外。
- 第一组16：2605.08279/08301/08310/08314/16341/16342/16343；2606.20582/2605.30359；2605.08292/08300/08322/08268/08271/10966/13874。精确v1/同DOI上界分别May12、May19、June23/June1或May13/15，均跨May11。原件身份/状态/registered保在本目录；OAI仅加强metadata线索不消去跨日。
- 原233中UNMATCHED51的最后13含糊主线题摘已实际读，不是新池：2607.14107/14108/14110/14112、2607.00011/00012、2608.20342、2605.08334/08258/08288/08257、2606.00051/18259。`SUP_DC_UNMATCHED_REMAIN13_20261019.raw`精确OR13查询actual total13/pages1/list13，全部sameDOI/findable/arxiv.content；不是13当窗候选。5贡献前C：MAPS14110为domain profile+GRU/attention组合与认知标签，未有可改变主线的新接口/条件；CEAD08258为成熟SOA/约束职责reference architecture未指出新执行机制；ARSM08257为固定加权损失与医用多模块联动，未指可复用安全边界，不把8.7%当保证；BusinessEDA00051为已有mean/CV/condition sensitivity在业务模拟上的组合，无新增模型/系统机制；Caring18259综述把affect作coordination layer，未给新的可执行控制/成立条件。均完整题摘而非按题材拒，不为无关日期另追材料，reader已分层实际核通过。
- 其余8是具名潜贡献/版本恢复线索：2607.14107 Polestar drift-cache/commit、14108 EtaGivenDelta marginal tool utility、14112 Information-Theoretic Limits、00011 SkillSelect bundle/QoS、00012 PRA-RAG aggregation、2608.20342 PrimeAgentOrchestrator、2605.08334 SalesSim、08288 UMEDA。精确v1 ABS均已恢复并完整题摘/history actual读（`SUP_ABS_<ID>_20261019.raw`）；14108/14112/00011/08334不能继承当前v2/v3题目/收益，特别SalesSim v1非CustomerSim v2。Uniquev1均May7/8，但sameDOI registered上界分别Jul17、Jul2、Aug24或May12；完整区间跨日，不按未来ID月份排除/不先core、不计确定新增46。和前16一起保留24日期请求；上述日期能力边界同适用，不将public registration改名实际公告日。

#### 机构本次00:00–09:00边界与停止位

- 原已有效小时窗Source保持，重用其中May11 09:00–24:00，不重跑原有效候选/事件。本次新增重点是May11 00:00–09:00及具名日期含糊事件，既有当前网页不补造历史slice。每日14ID全部实际首查和定点替代见A2原件；未建立可日定位的历史目录者保留来源限制，不能凭200壳/当前最近条目签历史零命中。
- OpenAI Research和Signals raw均403挑战壳，未取得必要正文；只有官方辅助搜索题名显示adoption/Campus interest，可在范围前关闭该统计/活动线索，不能称正文已审。Anthropic当前Research首10非历史归档；精确官方date搜索的Frontier Safety Roadmap Updates中May11是旧deadline、actual更新May5，非当日新研究（https://www.anthropic.com/responsible-scaling-policy/updates）。DeepMind200是当前research，Google Publications两次35秒超时，尚缺日级pub slice；Google May11官方blog查询未恢复目标日事件，不授年级pubs零遗漏。
- Meta官方入口connection reset，无可读目标日片段。Qwen旧入口redirect/current research200为当前shell；WebWorld二手线索未取得原始dated说明，本次`site:qwen.ai "WebWorld" "May 11" 2026`无结果，仅隔离该原始身份/日期而不补想象正文。DeepSeek200产品首页，阿里云V4Pro第三方托管非官方新机制。Kimi Blog当前最新2025-11-07，不据此证明May2026不存在研究；旧有效GitHub维护闭合仍复用。
- Hunyuan真实JS/API已恢复：当前en total9/list9、zh11/11，renderType0/all与displayPublishTime||publishedAt||createdAt已双方actual核；May21→Apr30之间无May11显示项，只支持当前集合此片段，不证明发布历史。ZAI SSR中的May11 updatedAt对应Apr20 createdAt旧条，不能拿更新当发布；当前研究集合不等历史全量。Seed research/public_papers是当前集合，无日级完整重建。ERNIE实际dated目录可见May9→Apr30段，未见其中May11新条，限定可见列表。MiMo8papers/15blog缺公开日，仅身份线索不授窗口零。
- MiniMax EN当前12条、May26→March18区间及CN官方redirect/Agent Tech Blog真实原件已恢复，当前集合没有目标日匹配不授历史全站完备。其他机构受限slice后续只有官方目标日归档、dated正文或已识别具体paper/event可提供时定点重开；没有正面Evidence/Books/全Coverage或无遗漏权限。辅助搜索无结果归检索受限，必要日期/历史片段不可得归受阻并终态隔离，不再把这些声明为尚未执行的普通任务。

#### 注册GitHub早9小时实际请求身份

统一官方endpoint `https://api.github.com/search/commits`，Accept `application/vnd.github+json`，page1（默认首面）、`per_page=100`；每条q如下，均实际total_count0/items[]/incomplete_results=false，零即该精确索引查询无下一页，不补造commit公开日或组织全研究覆盖。各原件 `SUP_GH_<简称>_EARLY_20261019.raw`/headers与下表一一对应。

| 简称 | 精确q |
| --- | --- |
| MOONSHOT | `org:MoonshotAI committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |
| HUNYUAN | `org:Tencent-Hunyuan committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |
| T1 | `repo:Tencent/llm.hunyuan.T1 committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |
| ZAI | `org:zai-org committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |
| SEED | `org:ByteDance-Seed committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |
| ERNIE | `repo:PaddlePaddle/ERNIE committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |
| MIMO | `org:XiaomiMiMo committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |
| MINIMAX | `org:MiniMax-AI committer-date:2026-05-10T16:00:00Z..2026-05-11T00:59:59Z` |

ZAI注册`https://docs.z.ai/release-notes/new-released`真实200，`SUP_ZAI_RELEASE_EARLY_20261019.raw`257316B；完整可见Models/目录仅Aug26、Aug18、June16、Apr7、Feb12、Jan14、2025Dec22、Sep30，一直到页尾反馈与Mintlify footer已读；无下一页，June16→Apr7之间无May11显示条目。仅该当前发布列表读完，不扩成Research归档。

### A7. 归并与机器检查（2026-10-19T03:29:47+08:00之后）

- README六节已归并170=原124+新46；新增34I12NC均root已接纳，不借历史完成声明。初次V3发现46个日期单元附注/标题带“补充”不被接口识别，已仅将新增日期规范为YYYY-MM-DD、46标题改为相同title+URL，表内空行也移除；不补造时刻、不改旧124行。07574长期gap/07481安全反证的已足必要Source分类同步“深入完成”，未重复审原件。
- V3重新实跑通过；当前README457个本地引用零缺失；baseline SHA仍cb28320b811200334bd5a542d2d1717ab0a4a592d30ca513c57cd95a26def809，124原行均exact、原§4连续块exact，候选实际170。限定Markdown/diffcheck通过，不代DAY语义验收。
- 已接纳Books本人旧note仅追加真实后续POST/root接纳/lease释放行政时态，未重正文/Source；本日全部窄位已释放。未stage/commit/push。下一为独立reader完整六节DAY与实际保存态FINAL，状态仍进行中。

### A5. 当前普通停点（R49 DAY已过；03:59:32完成态已保存待FINAL）

- 原46已确定当窗家族全部Books闭合：34实际正文/完整邻接/本人注非writer POST通过并root接纳，12具体NC实际owner通过并接纳；所有窄位释放。原124/日期评分/原小时窗与连续旧§4保留，不重有效层。
- 四窄主题233只是发现，不是全文队列。49旧小时窗未处理题摘已判断，受共同generic误闭影响七项定点重开，51未命中ledger按主题/理由有界补检；最后13完整题摘=5具体C+8潜贡献日期保留，不纳确定46。46准入/日期/必要Source独核已完成；作者35原阅读范围如实保留，其他直接复用reader精确版本/必要域/边界，不补双份附件计数。
- 24具名跨日与机构历史slice按A6实际能力边界隔离，不授正面Evidence/Books/全Coverage。注册GitHub早9小时8查询与ZAI release notes已实际执行（下条），不以首页失败遗漏可执行入口。
- 新补注册窄入口：GitHub官方search/commits固定committer-date UTC May10 16:00→May11 00:59:59、per_page100；MoonshotAI、Tencent-Hunyuan、repo Tencent/llm.hunyuan.T1、zai-org、ByteDance-Seed、repo PaddlePaddle/ERNIE、XiaomiMiMo、MiniMax-AI各actual total0/items0/incomplete_results=false。原件SUP_GH_<ID>_EARLY_20261019.raw及headers保留，零只授该索引查询不授所有public release。ZAI注册new-released实际200/257316B，全Models日期段Aug26/Aug18/June16/Apr7/Feb12/Jan14/2025Dec22/Sep30读完，June16→Apr7无May11列表项；当前listing不替历史Research全量。未扩每周机构或历年仓库。
- README现170候选=原124+新46；§1–6已归并当前结果与具体外部请求，原Source有效09–24复用、本次00–09真实范围逐到期ID自包含。独立R49已实际完整DAY通过，V3/457refs/124行和连续旧§4/diff检查通过；2026-10-19T03:59:32+08:00仅保存真实完成态/结论/复核和机器事实，外部请求完整保留。此时只待同reader实际保存态FINAL，不预签、不重Source/正文；后续实际结论见A8，不改LS/index、不stage/commit/push、不接新日。

### A8. 实际FINAL后行政闭合（不改已验README/Books）

独立reader于2026-10-19 04:04:44+08真实保存[R50 FINAL](SUP_REVIEW_20261018.md#r50--实际保存完成态final通过本日结束)，作者随后实际读回该完整结论：完成态六节/外部24日期及机构限制与R49一致，170unique/170证据、新46=34I12NC、旧124按序及161669字符连续旧§4exact，457本地refs0缺/V3/限定diff通过。reader记录实际完成态README SHA256 b32cffc02dd0bb846671e92b41350790327ac140949f0ab2cd725633359fa827，仅辨识保存稿，不替语义。当前普通待办0；该状态覆盖A5当时“待FINAL”。

本次仅同步实际发生的独核结果，不更改R50已验README或任何Books、不增研究/请求、不stage/commit/push。所有窄位与本日作者ownership释放；May12本日结束，不接其他日期。后续只在报告§5真实重开条件或具体新反例出现时恢复受影响层。
