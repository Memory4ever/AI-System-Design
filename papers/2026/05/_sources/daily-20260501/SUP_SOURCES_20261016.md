# 2026-05-01 来源遗漏补查（唯一续跑记录）

## A1 范围、冻结与合同

作者：`supp_may01_author_fresh`；独立复核者：`root`（待实际分批复核，不由作者自签）。2026-10-16 重新完整读取本日适用 AGENTS、研究合同、Report V3、Prompt、每日14源/arXiv主题、ROADMAP及最新相关LS路由。使用 using-agent-skills 的范围纪律与证据核验要求，不改合同、LS、索引、2025，不stage/commit/push。

用户授权只补遗漏：原窗口 `2026-04-30T09:00:00+08:00 ～ 2026-05-01T09:00:00+08:00`、原47候选整行/日期评分和连续原§4冻结，baseline见同目录 `baseline-before-supplement-20261016.md`。补充窗口仅北京时间 `2026-04-30 ～ 2026-04-30`。旧556全量池、旧脚本与旧Weekly不作为本轮发现或复核来源。

新增发现先按本窗模型/训练/推理/Agent/多模态主题检索并浏览相关原始标题；完整题摘决定贡献门槛，宽月表不形成全类逐项队列。新增具体ID先程序定点检查2026现有Daily全六节；只读取命中单条的精确版本/命题/反证/未决，保留旧归属、有效层不重审、不重评分。

## A2 原始入口与本窗停止范围（执行中）

arXiv官方规则 https://info.arxiv.org/help/availability.html （2026-10-16 actual读取）明确ID在公告时赋予、可早提交晚公告；提交日不作公开边界。官方2026-04月表原始缓存仅复用原文，不复用前日完成标签/筛选池；目录 `papers/2026/04/_sources/daily-20260429/SUP_MONTH_{CL,LG,AI,DC,CV,RO,AR,PL,OS,PF,IR,MA}_{HEAD,TAIL}_20261016.raw.html`。本日仍需核定公告边界、主题浏览停止与具体身份日期。

首批定点发现 COPUS 2604.26687、FaaSMoE 2604.26881，无2026 Daily ID命中；官方abs完整题摘已读，无当前撤回/更正标记，拟P，日期仍待合证。CL-bench Life官方研究发布100039的publicAt/display日期Apr30，publishedAt为内部Apr27不能代替公开；本文完整官方核心说明已读，论文必要构造/评价待补读后决定具体增量。

## A3 待办

此为启动时历史停点，当前状态以A11/A12收口为准。

有限来源检查、日期核验、首批P/代表EX独立校准、必要Source、具体Books决定、六节融入与非作者复核均尚普通可执行。未把准备好、写出README或旧完成标签当作闭合。

## A4 首批实际准入与COPUS写前提案

**此段过程提案已由A6纠正，不是当前准入或Books状态。**

root独立已实际读取26687/26881完整题摘并准入校准：COPUS P7（2+3+2），FaaSMoE P6潜力（2+2+2），后者须先核早公开资格。随后root实际读两项必要Source，受限机制可支持但不替代作者Source/owner判断。作者实际读26687 §3.1–3.3、§4、§6.2/6.5/6.6、§8，26881 §3–5；原始HTML `SUP_V1_26687_20261016.raw.html` / `SUP_V1_26881_20261016.raw.html`。

FaaSMoE：官方作者机构[Apr28新闻](https://www.tu.berlin/en/3s/news-details/paper-accepted-at-edgesys-26)已经公开stateless专家/多tenant中心机制并明示PDF available under Publications；正定点核同稿直接链接。不得将Apr30 arXiv收录自动当首次正文。尚未定日级候选或写书。

COPUS日期：官方赋号规则＋April原始月表＋DataCite exact-v1 Updated `2026-04-30`及created同日合证；不是submitted `Apr29`作边界。相邻25918的v1 Updated Apr29、25919为Apr30；26952为Apr30、26953为May1，形成此次有界目录25919–26952。26953/26961/26962虽早提交，官方赋号与v1公告身份落May1，不计补窗。原始合证 `SUP_DATE_{25918,25919,26951,26952,26953,26961,26962,26963,26687,26881}_20261016.raw.json`。DataCite只辅助身份，不能单独证明首公开。

Books作者差额：已读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE、ROADMAP/相关LS路由、Ch36实际Variable-length Batch完整段与Compound Section交接、Ch35/37邻章交接。Ch36已有‘length→并行计划并守globalbatch语义’，尚缺‘优化统计自身演进→globalbatch与3D共同选择’。拟在该节最后一句‘长期原则是 **runtime adaptability 必须守住训练语义不变量**。’后、Compound Section标题前插入下段；仅申请此位置与本人末注，未获root窄lease不写。

逐字PRE：

固定 global batch 时按吞吐选择并行布局，或只调整 batch 而固定布局，在统计需求和硬件最优点稳定时仍合理；若训练中的梯度噪声尺度变化让目标 batch 跨过吞吐拐点，两项决策就应共同提出。一个受限控制环从 gradient-accumulation micro-batches 的范数与同步平均梯度估计噪声/信号，再把当前统计效率、batch 所配学习率和离线 throughput 表组合，选择 `(global batch, micro-batch, DP/TP/PP)`；它复用 goodput 原理，不由 tokens/s 单独提交训练配方。统计聚合须保留独立样本和参数分片身份，样本数不足或估计 signal 非正时不能直接作除法并切换。Batch-only 更新可留在当前运行时，布局变化则在 optimizer-step 边界暂停、经 host 暂存并重分片 weights 与 optimizer state；这不是故障原子恢复的证明。切换 margin、GNS 校准、EMA 和历史时间摊销只是控制启发式，必须支付 profiling 与30–56秒局部切换成本；[COPUS必要证据](https://arxiv.org/html/2604.26687v1)只覆盖四组3B–32B、8–32张H100/MI210与受限token预算下的同loss目标，含局部退步，不证明下游质量或完整pretraining通用提速。统计失准、布局收益不足或状态不能一致迁移时，保留已验固定配方与checkpoint/restart。<!-- source-family:SF-2026-ARXIV-2604-26687 -->

拟本人Review note：`SF-2026-ARXIV-2604-26687` — Daily2026-05-01补Apr30；exactv1 §3–4/6/8、A1，P7。采用GNS/throughput/LR-awaregoodput联合batch与3D选择的局部分支；30–56s切换/局部-0.5%/offlineprofile/GNS有效条件/无ZeRO-CP-SP-activationcheckpoints/同loss非quality近正文。原始Source与实际owner写前/写后只据root实际检查记录，不自签；未运行artifact或复现。

## A5 代表性候选前关闭（完整题摘已读，待root抽检）

- 2604.26615 TDD Governance：abstract明确把既有TDD phase/gate/bounded repair/atomic mutation编码为prompt与workflow，未给改变控制职责的新增执行机制、失败条件或可比反证；不是因Agent主题或无实验泛化排除。原始 `SUP_ABS_26615_20261016.raw.html`。
- 2604.26211 OMEGA：meta-prompt＋code生成在20分类数据集优于sklearn，未指出超出既有自动研究流程的算法/归因/可靠性条件；领域指标与end-to-end组合不足准入。原始 `SUP_ABS_26211_20261016.raw.html`。
- 2604.26591 MappingEvolve：planner/evolver/evaluator用于logic technology mapping，报告area-delay领域收益，未提供改变模型或Agent系统机制的独立增量；不把使用LLM优化领域工具当主线机制。原始 `SUP_ABS_26591_20261016.raw.html`。
- 2604.25922 DenialBench：自述/创意prompt的相关性不能支持已训练‘误报一切功能状态’的广泛因果结论；题摘明确因果方向未决。本项拟判断需最小core核是否有实质新自评可靠性反证，尚不以标题或意识措辞关闭。

## A6 COPUS实际owner漏读纠正与有效层复用

首次作者只读Variable-length Batch局部，漏了当前Ch36:992–1008完整‘并行策略的目标不能停在最短单步时间’。该原文已经承载当前gradient-noise estimate×measured throughput的跨batch/3D选择、LR/checkpoint状态、reshard/optimizer迁移费用、time-to-quality与固定方案回退；原Apr30 `V3_ARXIV_SCREENING_NOTES.md:366` 对同exactv1、同具体命题已有具名前关。此次未出现可推翻原裁决的新事实，不能用已投入Source时间强保P7，不能以更细术语制造新Books差额。

作者报告漏读后，root实际读完整原owner及具名前关并同意复用；此前PRE/窄lease过早，不代表新的准入通过。作者已仅撤回本次新增单段与本人末注，保留旧992–1008与原EX记录不动。当前COPUS **同事件有效前关复用，不评分、不新增候选/Books**。raw必要Source保留，不重读相同技术层。

下一有限消歧身份的完整AB均在同目录 `SUP_ABS_<五位ID>_20261016.raw.html`，对应精确v1在 `SUP_V1_<五位ID>_20261016.raw.html`：26297/26341/26348/26419/26492/26503/26521/26553/26587/26830/26898/25984。只是决定准入的最小core集合，不是全文或候选队列；先核实际owner机制词/ID与既有单条裁决，再决定是否审阅。

## A7 本窗来源实际推进（2026-10-16；尚待root日级核）

原始官方缓存复用仅限原文/目录，不复用别日标签。以下多数缓存位于 `../../../04/_sources/daily-20260429/`；本日补取文件位于本目录。所有结论只限所列切片，不代表所有机构全org/删除页或互联网绝无遗漏。

| 每日来源 | 实际入口/本日日期段与停止 | 当前结果与限制 |
| --- | --- | --- |
| SRC-OPENAI | 官方RSS原文 `SUP_OPENAI_20261016.raw`完整item集合按Apr30北京时间日期过滤，Apr30 account-security与Apr29 20:00GMT Goblins两项；邻Apr29 compute-infrastructure/cybersecurity，不作本窗首次候选 | account-security为账户产品认证非模型/系统研究；Goblins同事件已有Apr30具名贡献前EX，按精确事件复用；不从RSS缺项推所有deleted研究为零 |
| SRC-ANTHROPIC | 官方Research嵌入数据 `SUP_ANTHROPIC_20261016.raw`，Apr29 20:26Z BioMysteryBench；Apr30 16:35Z personal-guidance已属May1北京时间 | BioMysteryBench同事件既有具名EX，具体生物信息应用/已有reward-reference纪律不转新系统贡献；personal-guidance不扩补窗；当前索引不证明删除页 |
| SRC-GOOGLE-AI | DeepMind Blog page3原始列表 `SUP_DEEPMIND_P3_20261016.web.txt` 从May穿April7卡到March，Apr30 co-clinician→Apr27 Korea→Apr23 DiLoCo；本日取co-clinician完整官方核心；Google Research `2026/04/`完整9卡至Apr3（上邻Apr29） | co-clinician是临床医疗应用/评测initiative，已读临床triadic-care/98query医生评价核心，未披露新的模型机制或跨系统可复用控制条件，贡献前EX。Research Publications交互历史过滤未恢复，作为该子入口发现保留项，不由Blog推出全Pub零事件。co-clinician原始HTTP体为gzip（本日SUP_DEEPMIND_CLINICIAN raw），实际解压读取，不把乱码当空页 |
| SRC-META-AI | 官方Research本日curl30秒HTTP000/0byte；官方域Apr30定点检索无结果 | 必要Research历史目录未恢复，隔离发现保留，不称零命中；恢复条件为可读Apr30官方目录/具名事件；不扫全org |
| SRC-QWEN | 官方完整Blog数据 `SUP_QWEN_20261016.raw`，FlashQLA Apr28→Qwen-Scope列Apr30；嵌入canonical内容却datePublished Apr29，旧qwenlm博客具体页本日404并提示迁移qwen.ai | Qwen-Scope完整核心/日期消歧仍普通待办，不从迁移404推零 |
| SRC-DEEPSEEK | 官方Research首页缓存完整footer的V4.1/V4/V3.2/V3.1/R1/V3研究入口，无Apr30可复查历史目录 | 只完成可见入口审查；不能恢复必要本窗历史目录，发现层终态保留；不以当前home证明无Apr30事件 |
| SRC-MOONSHOT | 官方Kimi Platform Blog完整已渲染列表 `SUP_MOONSHOT_20261016.raw`，最新可见2025-11-07/06、尾到2024；不是2026目录 | 不把陈旧列表当2026无更新；必要Apr30研究/selected-repo历史入口未恢复，发现保留，具名事件到达才定点重开 |
| SRC-TENCENT-HUNYUAN | 官方英文renderType1研究JSON totalNum=6/list=6读至Feb3，唯一Apr30 id100039完整body，邻Sep23/Aug20/Jul20与Feb13/Feb3；本轮另type0 total9/list9，详A11；不把内部publishedAt Apr27代公开 | CL-bench Life决定性core/actual owner已具名前关，见A11，不以405任务/5348rubric/低TSR自动P；blog12model与exactApr30PDF10model不同不拼版本；Apr30commit d52a与Apr14 file信号只用于身份线索，不授全语言/已删除历史 |
| SRC-ZAI | 当前Research完整159节点 Scaling Pain与Apr7 GLM5.1邻界，release-notes visible06/16→04/07；raw `SUP_ZAI_20261016.raw` / `SUP_ZAI_NOTES_20261016.raw` | Scaling Pain是已在Apr30原候选与实际Books采用的同事件，保旧归属与有效原层，不因当前UTC/display差重排评分或日期；未见具体重要修订，不扩全版本史 |
| SRC-BYTEDANCE-SEED | 官方API page20 raw `SUP_SEED_P20_OK_20261016.raw.json`完整20卡，A13重算BJT：非pinned May15→May1的1654/1665→Apr30的1637→Apr23，读至Apr15尾项，pinned不当时间排序 | 旧UTC/date解读共同错已修。1654/1665是May1简述窗外；Apr30 ID1637 Edit-R1/2604.27505完整AB有潜在verifier/GCPO贡献，但无独立当日正文/publicAt，arxiv赋号May1，精确资格隔离，不倒灌后日正文或计候选；见A13 |
| SRC-BAIDU-ERNIE | 官方Blog完整列表 May9→Apr30 ERNIE5.1Preview LMArena榜→Apr15Image→Feb6；raw `SUP_BAIDU_20261016.raw` | Apr30只有榜单/排名更新核心，未给模型新机制/评价盲点或可比系统边界，明确贡献前EX；不推所有repo release为零 |
| SRC-XIAOMI-MIMO | 官方Paper8项 June29 MOPD→March13 ARL-Tangram→Feb3 HySparse直至2025；Blog当前15卡未显示日期；raw `SUP_MIMO_20261016.raw` | Paper可见日期段已检查；Blog必要历史日期不可恢复，发现终态保留，不拿无日期当前cards证明本窗零事件 |
| SRC-MINIMAX | 中英文Blog当前完整13/12卡均读至2025，无next链接；中文May25→Apr27 AgentTeam→Mar18 M2.7；英文‘?page=2’实返同一集合，未伪装完成下一页；本日AgentTechblog完整3卡Oct8→Sep22→Sep19 | 可见中英文研究Blog范围已闭；AgentTechblog在Apr30是否存在及旧历史目录无法证明，单列发现保留，不从3个晚日期断言当时不适用 |
| SRC-ARXIV | 官方April12分类相关标题有界浏览：CL tail skip532/2000，LG tail skip1900/2000，AI tail skip3030/2000，CV tail skip1262/2000均覆盖25919–26952；AR227/DC388/IR512/MA348/OS37/PF69/PL138/RO976的全月原文列表仅作标题发现，过26952即停止本窗 | 不把全月库存计当日论文/全文队列；主题范围为模型/优化/生成/Agent/并行/内存/kernel/执行，跨类去重。已独立发现ID再定点复用同事件原层；当前普通项仅本SUP具名小集合，后续新命中必须照此身份去重 |

### 26503纠错深入：独立必要层已通过，Books暂缓

[SAMG exactv1](https://arxiv.org/html/2604.26503v1) §3.1–3.3 Eq4–12/Alg1实际方法为每步双CFG输出差的通道均方E、空间minmax、再映到任意经验正区间[ωmin,ωmax]。作者与root均实际读相应必要层：Eq10固定切线的凸函数lower bound不能授权Eq11–12任意affine重参数仍严格服从Eq9几何界；空间E恒a>0时，归一图全零而ω=ωmax与a无关，理论容许界却随a^-1/2收缩；κ、δ、c_t也不进入实际mapping，Δε切向/anchor在manifold另需假设。此反例只否定该严格桥，不否定局部生成结果。2+2+2=6，纠错深入，受影响严格保证/Books隔离。

作者又实际读§4.1–4.4/Tables1–4：SD1.5/SDXL50步、SD3.5M28步，CogVideoX2B/ModelScope1.7B50步；四图像集与ChronoMagic150，HPS/ImageReward/FID/CLIP等为局部proxy。Table1 SD1.5 Pick-a-Pic ImageReward .053→.043反退，不能写全指标无损；经验bounds随任务/模型换，不是由κ测出。mapping不增模型forward不等零成本，原uncond/cond两次调用及reduction仍付费；硬件、precision、并发、完整latency/SLO未在必要评价披露（Not Disclosed），不补造或从proxy推生产保证。暂缓owner `MULTIMODAL-GENERATIVE-PARADIGMS`/Ch24，不写正面机制段；重开条件为把经验mapping连接到有效κ/δ/c_t/切向域的证明或明确撤回严格保证，只恢复该桥。

## A8 最小core裁决与root实际复核层

以下均先独立题摘发现，再定点核同ID现有Daily/具名原层，不拿别日池作发现；清楚即停。前关不评分，不将已付阅读成本当准入理由。

- **26297 NeuroPlastic，EX**：作者实际§3；activity=EMA|g|、memory=EMA g/√EMA g²，均为gradient统计，加权clip/warmup/RMSgain仍是局部optimizer recipe，默认LR controller关闭，未给改变既有优化选择的新有效条件或实质反证。root实际§3.2–3.4抽检通过；不是按模型小/非LLM排除。
- **26348 ACPO，EX**：作者实际§3；冻结IQA（CLIP语义+structure）给reward，late-step LoRA更新同时受base-noise/original-denoise锚约束，属于成熟reward adaptation组合；没有额外归因/新控制条件，局部视觉proxy提升不独立改变设计判断。root已读完整AB分层抽检，未独立core，不冒充全核。
- **26419 VisualIdk，EX**：作者实际§3，强VLM视觉过滤InfoSeek后，以10次采样、τ=.7构known/unknown，再用标准SFT/DPO/CPO/ORPO配refusal对。新增任务人口不是新拒答机制；视觉清晰/答案明确不隔离parametric knowledge因果。root实际§3.1/3.2/4.3高风险core通过前关：强制refusal模板logprob差不能认证内在知识，PMC-VQA默认全拒不是真值。上述反侧不正面采用。
- **26830 RandomCloud，EX**：作者实际§2–4；随机初始化50个网，以训练accuracy为proxy逐层截短、保留参数子块，再backprop选中拓扑。具体新增仍是training-free NAS随机搜索操作点，没有新proxy有效性/失败条件理论；不能用7个低维表格和快于部分完整训练对照自动准入。MNIST 1k样本约17pp反退、5k差距缩小是局部数据依赖；不是以小模型排除。root实际Alg1/§4通过。
- **25984 Occam ELBO，EX**：完整AB与决定范围的BLR/Gaussian covariance结构核心；diagonal/low-rank+diagonal低估SNR、rank-only高估的结论属于一般贝叶斯模型选择。尚无foundation训练/表示迁移的机制桥，不靠能映射优化章节绕过范围。root完整AB抽检，未独立全core。
- **25922 DenialBench，复用有效EX**：独立发现后定点读Apr30 `V3_ARXIV_SCREENING_NOTES.md`具名299项：同exactv1，自述/创意prompt相关性不能给内部状态真值或训练干预因果。保留其中心限制；非仅意识措辞排除，不重新评分。

root分批actual必要Source（非作者自签）：26889 §4/5/6.1–6.3，支持doorbell最终提交→USERD最新GP_PUT→GPFIFO/PB的测量边界；A40/Xeon6338/PCIe4，log/performance分离，root/patched kernel与扰动、整套CUDA/driver混杂及单次设备计时边界保留。26940 §4.1–4.4/5.1/5.4/Table3，teacher仅给student候选排序；Local另付K augmented prefixes batched forward、LoRA/readout训练，teacher token不是真值。26951 §2/AppendixC/D，reverseBCE=KL+H(student)且H依θ，bounded coefficient依ε，不把低ps认证参数梯度小；同原争议层保留。26889/26940/26951完整AB与exactv1 Apr30日期合证root已actual核，日期解开不擦除TIDE反证。

26521作者actual机制/划分/训练最小core，rootactual Results/Limitations：ground-only one-shot与iterative+每步GT+test追加axiom共同变化，局部差额不唯一证明grounding不充分。26553作者actual§3/4，rootactual§3.1/3.2/4.2/4.4/Limitations：first-confusion、topN确定候选、k=3 lookahead、probability-weighted advantage限定可局部定位监督；不是任意sequence correctness或语言神经元因果。26587作者actual§III/IV，rootactualIII/IV-A–D/V：CSC压缩驻SRAM、densePE前解压，不跳MAC；28nm synthesis/estimate，density≥.7与极稀疏ESE反侧、BERT剪枝质量下降保留。以上潜在项仍须actual owner后决定，不以读过Source自动强保。

COPUS撤回后root实际检查新正文/本人注已消失、原Ch36 joint链保留，窄lease释放；技术层不重读。FaaS两份TU缓存root实际读到官方Apr28 PDF available新闻及匹配出版物，只支持早于Apr30信号，不证明Apr28不可变正文；日期资格保留、不计候选。

## A9 准备好的三个Books最小PRE（未写，待root actual owner与窄lease）

作者actual Ch49:215–237、583–605完整邻接，机制词/ID定点查无同doorbell或compressed-SRAM→densePE承载；Ch29:310–330、490–548承载目标、occupancy、位置选择和词表保护，但没有student-candidate ranking蒸馏。拟26889/26587/26940各2+1+2=5，为具体owner差额必要深入。无代码执行或复现。

**26889 → INFER-TENSORRT-LLM / Ch49，在TaxBreak段后、浏览器后端段前：**

分层profile若仍把CUDA runtime视为黑盒，可以再向实际提交边界下探，而不把API调用返回当设备已执行。一个受限观测分支在CPU写GPU doorbell时暂停提交线程，从对应channel的USERD读取最新GP_PUT，再沿GPFIFO恢复被提交的pushbuffer；RAMFC旧副本不总能代表这次提交。这样保留的是命令流与提交位置身份，不是请求完成或全部GPU状态的原子快照。[直接命令观测的必要证据](https://arxiv.org/html/2604.26889v1)依赖root、修改kernel及watchpoint/shadow-doorbell机制，记录与性能测量分开，扰动和工具维护也计费。其A40/PCIe4对照只说明特定软件栈下的命令及设备计时差异，CUDA11.8与13的整套driver差异不能唯一归因command footprint；raw DMA单次设备时间更不等服务端到端加速。需要不可扰动生产观测、权限不可得或异步写入身份不能解释时，保留vendor profiler与较粗分层trace，分别验收执行正确性和完整请求成本。<!-- source-family:SF-2026-ARXIV-2604-26889 -->

**26587 → INFER-TENSORRT-LLM / Ch49，在稀疏pattern/kernel fallback段后、‘选择可执行稀疏pattern之前’段前：**

参数以稀疏格式保存，也不要求乘法阵列跳过零值：在SRAM中保留CSC压缩，在进入dense systolic PEs前才解压，可以减少存储与搬运，同时保留规则计算和输出顺序。它放弃零乘法跳过，用少掉的index matching、scatter与互联面积配置更多dense PEs；因此要比较相同面积下的吞吐和能耗，不能只比较MAC数量。[Sparse-on-Dense的受限对照](https://arxiv.org/html/2604.26587v1)是28nm综合与cycle/energy估计，不是实芯或GPU服务测量；density≥.7时原dense基线能耗更好，极稀疏时ESE的吞吐/面积又占优，BERT剪枝本身还有质量损失。压缩索引、解压带宽、buffer、面积和质量恢复都须计费；不能把存储节省写成少执行同样比例的计算。密度、形状或存储瓶颈不合时，保留dense存储/计算，或已验证的真正sparse kernel，由同质量与完整费用选择。<!-- source-family:SF-2026-ARXIV-2604-26587 -->

**26940 → TRAIN-SFT / Ch29，在位置选择完整两段后、‘扩展输出词表’标题前：**

蒸馏还可以只学习‘在student能提出的候选中怎样选’，而不强迫学生复现teacher完整词表分布。先保留student生成的prefix与TopK候选，让teacher在同一prefix上给这些候选评分；teacher自己的最高概率token不在集合时是候选覆盖缺口，在集合却没被选中才是选择缺口。一个受限分支再用LoRA与专门readout，把各候选追加成不同prefix，蒸馏它们的相对排序，并以原text词表分布约束保护base。[S2T Local的必要证据](https://arxiv.org/html/2604.26940v1)支持这条候选选择接口，不把teacher argmax当答案真值；部署的trigger也须由可得信号预测，不能借用teacher KL oracle。K条augmented prefixes可batch成额外一次forward，但不等零成本或只改logits，还须支付teacher标注、selector训练及语言回归。候选缺覆盖、teacher排序不可靠或质量—执行费用退步时，保留原student/full-vocabulary蒸馏与外部验证，不用更高teacher-token命中签发真实任务正确。<!-- source-family:SF-2026-ARXIV-2604-26940 -->

实际落地仅校正root为权限、Sparse-on-Dense为架构非TensorRT原生、S2T为候选集合而不强制TopK（§5.5部署可采样）；作者实际读回Ch49:227/597与本人2502/2504、Ch29:544与本人1361。root非writer已实际逐段读正文/完整上下邻接/本人注，POST通过，三个lease释放；不授日级。作者本轮补完26889§4/6.1–6.3、26940§5.1–5.5、26951§3.1–3.4必要评价：S2T Local Table3同student慢9.3→10.2s/15.5→18.0s而AIME因输出短30.7→21.0，非普遍同速；TIDE共享tokenizer普通KL30.55低于未蒸馏32.67，不能说所有蒸馏都提高，fixedprompt256token H100 BF16学生6.25s慢于未蒸馏6.08s，不把小student对大teacher直接当优化因果。

## A10 其余机制差额与写前单段

**26341 SpatialFusion：改为P5（2+1+2）**。root实际§3/4.5/Table5与Ch23 GeoSense/GeoSR完整局部，指出作者初拟‘成熟组合’EX会漏掉semantic→可监督metric-depth→generation的具体中介选择；作者接受纠正并实际读Table5全对照。w/oInjection/Concat/Addition分别GenSpace T2I35.22/42.81/46.19、editing29.80/32.76/35.40，支持局部接口选择；18.5%新增参数/训练一起变化不能证明完全排除overfit，H200 300run局部开销不能授生产。拟标准完成、仅报告：受限生成模型的加和比concat反证，不把同一比较提升为任意语义—几何架构通则；Ch23实际geometry consumer接口继续承载一般原则，不为单实现强写新段。

**26492 SATC：EX**。作者/root实际§III，component-specific KLT/whitening、MAP GMM modeindex、水填充/LloydMax与arithcode继承成熟mixture transform coding，未给超出原语的codec成立条件或修正foundation表示选择的新证据；不因面向feature应用自动准入。

**26521 iLTN：P5（2+1+2）标准，已有覆盖拟案**。新受控视觉逻辑对照把可读grounding accuracy与constraint reasoning分离，故不以toy/非LLM排除。作者actual构造/训练与rootactual结果限制共同支持局部negative；one-shot与iterative/每步GT/test新增axiom共同变化，不能唯一因果推出所有grounding不足或LM不可能涌现推理。当前WORLDVIEW-LLM-INTELLIGENCE Ch8:283–295完整原子事实/bridge-state与组合泛化段，已经承载局部识别正确不等可组合推理、迭代非免费及行为失败不识别唯一电路；本篇没有新授权/状态责任，已有覆盖不强写。请root actual owner后核此决定。

**26898：P6（2+1+3）必要理论层已足够**。作者actual官方PDF p2–10，rootactual p2–9；HTML转换中止不能当全文，已改读完整PDF而不遍历证明。固定attention、iid初始化MLP、球面LN，attention T/L而MLP√(T/L)产生不同来源的共享噪声；有限N、固定T近似不等任意长期/训练动态。三limit全交换另需C∞，ReLU不无条件继承；nonodd与barλ=(d−1)κ′−(d−3)κ<0（需d>3），再有attention能量增长ε+barλ′<0才期望interaction energy指数降，Tanh odd可两点吸引。新差额是旧Ch17 attention-only定理不授的MLP来源/缩放与同步条件，不覆盖旧边界。

拟在Ch17当前attention-only两段后、‘不计算归一化’标题前插入：

MLP也会产生共享扰动，但不能直接沿用上面的Attention-only定理。另一个受限初始化模型固定Attention映射、令各层MLP独立随机，采用球面归一化；当Attention残差按T/L、MLP残差按√(T/L)缩放，前者进入确定性相互作用drift，后者进入由各token共同读取的随机field，而不是逐token独立噪声。[联合深宽极限的必要结果](https://arxiv.org/pdf/2604.26898v1)只在相应初始化、正则与有限时间条件下成立，三种极限全部交换另需更强光滑性。噪声是否促使表示合并，还取决于其协方差、激活与Attention反向扩张是否足够弱；仅在nonodd及负能量增长率等条件下，才有期望interaction energy指数下降。Odd的Tanh实例可保留两点吸引，故不能把MLP更宽或随机性更强直接当防collapse。有限网络、训练后相关权重、causal decoder与任务质量仍独立验收；条件不符时，保留已验Norm/residual配方和有限扰动诊断，不用初始化极限替训练checkpoint签证。<!-- source-family:SF-2026-ARXIV-2604-26898 -->

**26553 TLPO：P5（2+1+2），拟在Ch33静态first-failure段后、think/answer分loss段前插入：**

若目标错误能在输出中局部识别，还可以在首个违规位置重新比较词表候选，而不借终局reward猜整条轨迹的根因。语言混杂的受限分支先生成完整回答，定位first-confusion，再取该prefix下的确定TopN；每个候选追加短lookahead后由语言检测器评分，以旧概率加权的局部advantage作clipped更新。[TLPO必要对照](https://arxiv.org/html/2604.26553v1)只支持这种可定位、短程可评分属性，不授数学推理或整序列correctness；所有候选同分、归一信号不可用时不能直接除零并批准更新。它不需另训critic，却仍支付完整rollout、各候选lookahead、检测与训练，loss只落该位置也不隔离共享参数或TopN之外的概率变化。英语算中性还是违规会显著改变验收人口，严格口径下准确率仍有退步，不能写‘纠错而零能力损失’。定位/语言身份不可信或任务回归时，保留普通sequence训练、可靠过程监督与原checkpoint，分开验属性合规和答案质量。<!-- source-family:SF-2026-ARXIV-2604-26553 -->

实际两段落在Ch17:381/Ch33:287，各本人注已读回；root非writer实际正文、完整两侧及本人注POST通过，lease释放。五项本人注现已仅行政同步到实际通过，不授DAY。26521 Ch8实际owner的已有覆盖与26341标准Only亦经root独核通过。

## A11 发现封口与63身份的可追溯归并

**冻结新增10家族**：26341/26503/26521/26553/26587/26889/26898/26934/26940/26951；5I（26553/26587/26889/26898/26940）+1已有覆盖26521+2Only26341/26934+2中心争议26503/26951。原47与这些无重叠，合计57，但不改变原归属/评分。全部新必要Source/实际owner及五处POST的非作者root分批检查已发生，不冒充最终日级。

63为本次独立主题发现后实际读取完整AB的唯一arXiv身份（同目录63个SUP_ABS文件），不是月表全部1034/724库存或召回率。逐ID定点2026 Daily六部分身份索引后，只读命中原裁决：4个旧候选26130/26167/26340/26694按Apr30 README具名候选与§4复用，中心争议/Only/真实I均保留；1个26881按A4/A8/README§5早公开信号/原同稿EX处理；48个EX如下；另10新增。63=4+1+48+10。当前official abs轻检未见需要重开这些具体裁决的撤回/重大更正；部分当前API/v1标题不同（25930/26689）仅用原精确v1，不以新API值改旧命题。

初期标题路由曾暂取24765–26962的较宽ID段（724个去重标题线索），官方公告/相邻身份合证后已收窄为25919–26952；较早标题不形成题摘关闭队列、不计本窗命中。上述63个完整AB均在收窄后Apr30段内，没有按早Submitted把26953/26961/26962移入；不以旧日库存或724标题声称本窗题摘全量完成。

下表 **N** 指 `papers/2026/04/_sources/daily-20260430/V3_ARXIV_SCREENING_NOTES.md` 的具名单条行；**R50** 指同目录 `V3_APR29_INDEPENDENT_SOURCE_OWNER.md:50` 的四项actual负侧复核，另见 `V3_ROOT_DAILY_GATE_20260430.md:12`接受范围。只复用身份、exact-v1、实际命题/反证与有效独立层未变的单项；旧临时P/待核绝不等于EX。

| ID（2604.*） | 具体EX/有效原层与保留反侧 |
| --- | --- |
| 25921 | N290：逐字跨轮completion累计状态已属Ch72完整trajectory guard；词表union/预算与judge-defined probe不独立识别因果 |
| 25922 | N299+A8：自述/主题相关不提供内部状态真值或训练因果，root本轮实际身份复用通过 |
| 25923 | N87：evaluation concerns scoping taxonomy，无新增可执行评价gate |
| 25930 | N293：显式slot/pointer修复小关联回忆，Ch22已有exact-readout可寻址state；32slot/8keys、80/200step/慢Python不改现有选择 |
| 25975 | N234+R50：Gaussian logdet/leverage近似没给同预算真实future-query保留反转；O(Nd²+d³)与FullKV回退保留 |
| 25982 | 本轮完整AB：Open Problems in Frontier AI Risk Management明确agenda-setting、不提出具体解法；风险框架/actor分类未新增模型或平台执行机制 |
| 25984 | A8：BLR covariance→SNR局限一般VI模型选择，无foundation机制桥；不是按数学/模型小排除 |
| 26103 | N236+R50：attention-only HBM-PNM的局部数据流/MLA反胜已核，未反转现有compute-memory-fabric计划；非因模拟自动EX |
| 26148 | N271：UI视频三级标注没给同动作/state的成对失败或新控制接口 |
| 26173 | N304：entropy时间mask centroid排序实现，既有候选/总费用原则不变，非外部truth |
| 26182 | N272：冻结世界模型+waypoint→joint action直接policy/搜索属Ch25已有分支，人体任务误差不新增通用选择 |
| 26211 | A5/N159：meta-prompt/codegen分类排名，无独立算法/归因/可靠性条件；root完整AB校准 |
| 26243 | N306：must/nice/irrelevant memory人口切片，既有recall/use/overuse及Read Gate不变 |
| 26258 | N273：外workflow/内call textual gradients实现，Ch81 artifact/heldout/部署owner已承载 |
| 26297 | A8：EMA梯度‘activity/memory’加权clipping/warmup局部recipe；root实际§3.2–3.4 |
| 26326 | N338最终改判：按entropy拒绝整条advantage rollout是既有更新流actuator，未计同总拒绝采样/验证成本而反转排序 |
| 26348 | A8：IQA/CLIP+structure reward、LoRA与denoise anchors成熟组合，无新控制条件；root AB分层抽检 |
| 26355 | N312：supertoken+SFT 8.1%短trace，15组2等价/11不定/2退步，无新token/cache identity，非无损 |
| 26360 | N128：合成annotator uncertainty的分母仅在正value下更保守，负value反侧保留；未给foundation后训练桥，不采通用安全 |
| 26382 | N313：parser未操纵、共generator、r=.02非因果独立，completeness与stated-fact accuracy已有分责 |
| 26388 | N129：cutlayer+LoRA rank不是activation压缩，test accuracy反馈非heldout；既有split合同不变 |
| 26412 | N365最终改判：KV/hidden drafter5.01→5.04伴5–10%draft latency，既有target-KV/总账未反转 |
| 26419 | A8：10samples τ=.7人口+标准偏好训练；画质过滤不隔离知识因果，refusal logprob非内在认知；root高风险core |
| 26460 | N132：LUAR/judge/function words相关.013/.026是代理不一致实例，非作者身份真值或新release合同 |
| 26470 | N134：嵌入式classifier两层cascade配方，EMA频率/部署未新增LLM控制条件，保5.82ms反慢5.66ms |
| 26483 | N324：8memorytokens/rerank局部压缩实现，230GB离线索引及长query无速度收益不改既有双目标/总账 |
| 26492 | A10：GMM/KLT/MAP模式号/水填充/LloydMax继承成熟mixture codec原语，root actual最小core |
| 26506 | N224仅曾送独立负侧，不能借旧七项样本授全核；本轮root补actual§3.2/4.1/4.4/5.2/Limitations及Ch72:1068–1081，标准GRPO攻击/DPO闭环新review应用无新授权机制，具体EX通过。PromptGuard全拒/38.2%FPR33.7%FNR与accepted subgroup不认证confident-writing因果安全，保全部反侧 |
| 26522 | N176：CPG/ILP/NTP的RetroQuest组合无单项归因或真实world-transition责任，完整AB前关 |
| 26573 | N341最终改判：partial verified reference可见量/token选择共同变化，未隔离两knob推翻旧privileged teacher选择 |
| 26591 | A5：MappingEvolve planner/evolver/evaluator领域映射area-delay收益，无新模型/Agent控制；root AB校准 |
| 26615 | A5：TDD phases/gates/bounded repair编码既有workflow，未新增执行/失败条件；root AB校准 |
| 26653 | 本轮exactv1§3/6：AgentSim: A Platform for Verifiable Agent-Trace Simulation；DS>.4人审/grounding<.3重检、Kmeans/MMR/novelty与配置化trace，无新增独立真实性或执行权；root actual§3.3最小核通过 |
| 26666 | N339最终改判：CUTLASS catalog的既有typedIR/cost计划，FP16/TF32不匹配、无跨session/编译摊销证据 |
| 26687 | N366+A6：同joint batch/3D/GNS/goodput/reshard决策已有真实owner与有效EX，本轮重复段/注撤回，root实际验证 |
| 26689 | N75：exactv1 Atomic-Probe Governance而非API后发别名；margin筛选未替组合回归，mixed oracle与75%/45.8%局部取舍不成新通用准入 |
| 26707 | N199：videoQA curriculum/self-evolution组合、evaluator score无新独立真值/训练条件 |
| 26733 | N367最终改判：future label/冻结rollout已有witness责任，丢unresolved 35.65%/20%人口偏差未被消除 |
| 26752 | N342最终改判：视觉MTP placeholder仅0.5B auxiliary loss，无任务/真实跨stage成本反转；Apr1已更早官方身份 |
| 26768 | N428+R50：task/document LoRA资产已有Ch30/77承载，A/B gauge软罚不认证语义独立，硬投影裁有用方向 |
| 26805 | 本轮exactv1§3.3–3.4：Bian Que: An Agentic Framework with Flexible Skill Arrangement for Online System Operations；schema/prompt/meta及三次字段验证/反馈分流无新增effect/rollback权，协同因果作者留未来；root actual最小核通过 |
| 26821 | N238+R50：真实bank-placement模拟分支但非商品3D实测/可执行计划反转；保row-buffer/prefill/decode差异，不按模拟硬拒 |
| 26830 | A8：50随机网训练accuracy筛拓扑后backprop，training-free NAS局部操作点，proxy条件未新；root Alg1/§4 |
| 26841 | N218：条件entropy/恢复probe非逐样本mem判定或隐私保证，uniform-state理论不授完整生成真值 |
| 26844 | N216：typology curriculum领域inductive bias，无新的foundation curriculum选择条件 |
| 26866 | N220：known/unknown混合×epoch与SAE steering较相关更强，但dev同事实任务校准，不认证知识完整保留或唯一因果存储 |
| 26904 | N284：persona/skill生成mockworkspace+checker/rubric+strong-small过滤改变200题人口，非新truth owner |
| 26923 | N331：class-level题/coverage/ensemblejudge既有验证器组合，90%coverage不证明行为充分 |

三项原临时层已正确消歧：26653/26805不借旧标签，本轮最小core如上；26934旧N279临时P5在本轮补actual§3.2–3.4/4.1/4.4/T2–4，由作者/root均独核正式P5标准Only。Ch25:36 training-only teacher与347–354 forward/inverse完整原层已有原则；camera transitions/boxes非真实物体动作，局部反退与完整生命周期成本未控见README§4，不强造Books。

机构最终贡献前关补件：Qwen-Scope完整发布核心为14SAE/7backbones、0.5B训练及feature steering/seed标签/合成/targeted SFT/eval coverage四类用途，没有给新增objective、干预识别或有效性条件；Ch5现有SAE/steering/独立验证纪律不变，不拼May technical report。外层Apr30/内文Apr29日期冲突不影响明确EX。CL-bench Life作者actual exactApr30 PDF p3/4/7/12、root另p1–4/7–12，10model/13.8avg/19.3best不拼当前blog12model/14.5/22.2；self-contained/strict rubrics/role taxonomy属该人口测量，lengthbins非配对干预、role频次非独立因果。实际Ch75:38–70 acceptedlength≠find/understand/use、Ch66:252–254识别/来源/应用分责已经承载拟修正判断；root实际owner同意EX，没为读过PDF强保候选。Apr14 file添加信号只留身份恢复，不无限追历史。

Hunyuan发现范围纠正：本轮又actual POST `https://api.hunyuan.tencent.com/api/blog/publicList`，pageNum1/pageSize100，renderType0返回total9/list9，renderType1 total6/list6，实际均`lang=en`。own文件名`SUP_HUNYUAN_ZH_{ALL,RESEARCH}_20261016.raw.json`中的ZH是请求尝试标签，不是响应语言证据；lang/langVersion body字段未改变英文响应。type0当前9卡仅100039公开/display在Apr30，邻100061的display Apr23但publicAt实际更晚，不能用display造其早公开；type1研究6卡Apr30→Feb13邻界。root撤回此前‘中文9项’误推，不为此继续追JS或造中文Gate。本次只声称英文可见type0/type1切片，不证明所有语种、已删除历史或全org。

2026-10-16 发现/具名准入/证据/Books普通工作为0；仅六部分机器/冻结检查和root日级验收待执行。README已经融合57家族，原47/旧小时窗/连续原§4不动，终态外部保留单独列§5。

## A12 作者最终检查（非日级自签）

2026-10-16（北京时间）：本轮README V3校验通过、scoped diff--check通过、本日报本地链接无断链。原baseline47行逐字一致、原§4为当前连续前缀、原小时窗口未变；57唯一ID、新10日期均Apr30；SUP表48EX及63=4复用旧候选+1FaaS资格+48EX+10新增机械一致。五个SF各恰有一个实际正文标记与一个本人note，POST行政状态已读回。校验初次所报原47窗口错误缘于缺冻结日期baseline引用，不改旧日期/窗口，补引用后通过；新6个别名标题改匹配官方表标题，未改机制。没有stage/commit/push、LS/索引/合同/校验器或其他日期写入。

root已经actual读本轮README全部10项/§1–6与全部必要独核/五POST；最终A11身份closure、Hunyuan英文type0/type1停止与机器结果尚待其日级确认。现在普通研究/写书工作为0，仅此非作者DAY/完成态FINAL待办，不由作者自签。TIDE性能必要评价未取得固定prompt输入长度、batch、concurrency、SLO，均Not Disclosed；不为补字段扩无关附件。

## A13 Seed日期共同错误的受影响切片纠正

root/May2独立reader指出后，作者实际仅重新换算同一P20的20卡日期，不扩大入口。ArticleMeta.PublishDate=1777564800000是UTC Apr30T16/BJT May1，故1654（2605.00503）与1665（CARD）不是Apr30。此前A7/README把epoch的UTC日期当BJT是元数据解读错误，并非‘目录Apr30与SubmittedMay1冲突’；现已纠正当前来源表/§5，旧错误不继续支撑任何候选日期。Page20非pinned May15→May1两项→Apr30 ID1637→Apr23，尾项Apr15；pinned Charon实际BJT May16、MegaScaleApr26等只作独立条目不改非pinned停止。无需精确时刻筛选。

真正Apr30项为1637，标题Leveraging Verifier-Based Reinforcement Learning in Image Editing、arxiv2604.27505（Edit-R1），PublishDate1777478400000，只有完整ArticleSubContentEn.Abstract与PDF外链。作者actual完整AB：principle-by-principle CoT verifier，经GCPO人类pairwise偏好训练pointwise RRM，再GRPO编辑，潜在贡献清楚；必要Apr30完整正文公开身份没有合证，arxiv27505公告赋号落May1、SubmittedApr30不作公开日。现隔离为§5材料/日期资格，不读取后日全文倒灌、不评分/候选/Books；可接受替代为Apr30已公开完整作者稿/官方项目正文或明确公开身份合证。

27505独立发现后，作者actual2026 Daily六部分精确身份索引无命中；仅定点读本日旧screening-ledger.json同ID对象（没有加载旧大池）：原EX为‘AB未披露独立evaluation/artifact/failure’及未改MULTIMODAL-REPRESENTATION modality/alignment/generation/serving contract，缺本机制的actual reward-owner/core，不用泛旧Completed代此资格/准入。旧对象与原47/连续§4不改。此项属机构发现，不改变A11的63个Apr30 arxiv主题AB身份分母，也不把64/556库存混计。

May2 reader `supp_may02_review_fresh`已确认：只路由May1简述1654/1665，不重复27505 Source或Books。root又actual P20 ID1637 ArticleMeta与27505 exact官方完整AB，确认GCPO潜在增量、旧泛EX失效，接受Apr30简述不证明exact paper当日公开的精确资格隔离，不等后日全文。无候选日期/评分变化。26506安全前关闭的root本轮最小负侧复核已补入A11该行，不以旧七样本泛化其scope。

## A14 非作者实际DAY与完成态行政同步

2026-10-16 10:37北京时间，root明确DAY通过，限定本轮授权补查增量：actual读README六部分新增10项及A11–13；此前全部必要Source/actual owner与5处正文/完整上下邻接/本人注POST已独核。冻结47整行、旧窗及原连续§4保留，新10=5I/1已有覆盖/2Only/2中心争议，总57；root本地63引用0缺、围栏、V3及限定cached/unstaged diff检查通过，无普通可执行工作。A13 Seed1637仅Apr30必要正文/日期资格Hold，1654/1665窗外May1；Hunyuan9/6为renderType差异而非语言，英文可见slice，不授全语言/已删除历史。终态隔离不等Coverage/Evidence通过或生产保证。

作者只据已经发生的root DAY同步README完成态、§1/5/6和本段，不再重审Source、不等May2；旧/无关改动未动，不stage/commit/push。完成态最后V3、scoped diff--check与47行/连续原§4冻结检查通过，作者已实际读回完成字段、普通待办无、root当次复核与本段。机器曾要求§5显式‘终态保留项’，已补名称及逐项重开/禁止采用边界，没有改动语义或校验器。parent root可执行最小FINAL；本agent完成后释放May1 ownership，不自行跨日。
