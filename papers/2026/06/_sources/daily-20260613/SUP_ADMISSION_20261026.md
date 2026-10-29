# Jun13 补遗漏：首批准入校准（作者待独核）

新增窗口仅 `2026-06-12 ～ 2026-06-12` BJT。原小时窗与空候选有效层保留；旧零命中不证明新增窗覆盖。作者 `supp_jun13`，独立复核由 root 执行，本记录不预授复核完成。

## A1 首批实际完整题摘

完整 exact-v1 题摘/history 已保存在各 `SUP_RAW_ABS_<ID>_20261026.raw`；不是从新版DataCite摘要反推。1274条DataCite注册窗记录只作导航，P1=1000/P2=274，meta total1274/totalPages2，未继续P3，不把它们当全类逐篇关闭队列。

| 身份 | 原有约束 → 原文实际增量 → 待重考虑选择 | 作者初判 |
| --- | --- | --- |
| [2606.13392v1 MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392v1) | GQA长上下文成本 → 每GQA组独立block Top-k与KV-outer/exp-free执行协同 → 是否稀疏率能转为真实prefill/decode速度及保留质量 | 准入，2+2+3=7；日期bounded Jun12；不得把此前M3发布与本次技术论文当同事件。 |
| [2606.12688v1 M*](https://arxiv.org/abs/2606.12688v1) | serving假设固定模型结构 → Walk Graph将复合模型表示为可分配/调度的组件遍历 → 多模态共享runtime的接口及放置边界 | 准入，2+3+2=7；bounded Jun12；v2 Jun13不自动视重要修订，检查明示信号。 |
| [2606.13501v1 GF-DiT](https://arxiv.org/abs/2606.13501v1) | 每请求固定并行 → trajectory task与group-free collectives支持在线GPU重分配 → DiT并行度成为调度资源的成本/成立条件 | 准入，2+3+2=7；bounded Jun12。 |
| [2606.13591v1 Confidence Composition](https://arxiv.org/abs/2606.13591v1) | 单agent confidence不可直接当系统置信度 → 跨模型信号校准后soft vote/Bayesian fusion，分开检查AUARC与F1 → 多agent输出可靠度是否能组合及歧义边界 | 准入，2+2+2=6；bounded Jun12，待核fusion假设/校准数据隔离。 |
| [2606.13176v1 Mental-R1](https://arxiv.org/abs/2606.13176v1) | GRPO整段统一探索 → stage-wise entropy由早探索转向后确定并显式阶段约束 → 推理阶段探索日程的可复用机制及是否只依赖领域标签 | 准入，2+2+2=6；bounded Jun12，不因医疗领域标题拒绝其优化机制，健康应用效果不外推。 |
| [2606.12487v1 PhaseQuant](https://arxiv.org/abs/2606.12487v1) | 静态旋转/缩放难处理residual phase jump → JumpRatio/HistoricalSNR定位并只提敏感层A8 → 动态残差变化是否要求混合激活精度 | 潜在贡献明确但日期不确定：唯一v1 Submitted Jun10 09:25:45Z，最早Jun11 00Z，registered Jun12 01:50:28Z，跨BJT Jun11–12；不列确定候选、不评分/Books，待具名直接公告。 |
| [2606.12881v1 DPO empirical study](https://arxiv.org/abs/2606.12881v1) | DPO较RLHF简化pipeline → 仅复用DPO与BLEU/ROUGE/cosine评价并报告训练不稳，无新的控制变量/成立边界 → 题摘没有改变既有设计选择的实际增量 | 贡献前N；不是因低分、未开源或实验局部。当前history v2不单独等于实质修订。 |
| [2606.13370v1 small Llama repeated-measures](https://arxiv.org/abs/2606.13370v1) | endpoint不足展示训练过程 → 4.26M TinyStories六seed/21间隔呈现早降后升与波动，建议看轨迹 → 实际题摘仅常见过拟合/回退现象的描述，尚无新机制、反直觉边界或可区分的训练条件 | 初判贡献前N，供独核校准；不是因为小模型/CPU/负面结果而排除。若已有具体条件改变通用选择需重开决定点。 |

日期原件为两页 `SUP_RAW_DATACITE_NAV_P*_20261026.json` 的同精确DOI记录，均arxiv.content/findable。前五条唯一v1与registered联合界全部限定Jun12且reasons=[]；12487明确cross_bjt_dates。created不作公开证据，日程只作最早界，登记只与发号规则联用作最晚界，不宣称全球首公开。

下一步：root独立校准首批拟入选与两项代表性贡献排除；作者可继续有限来源core与无关主题导航，不在校准前扩Methods队列。

## A2 后续题摘首备（未开展Methods）

以下20项完整exact-v1 AB已实际读取；只准备准入，不称证据审阅或Books完成。题摘是原件文件同命名规则；评分为作者拟定，待独核，不由主题映射直接授贡献。

| 身份 | 原文具体增量与会改变的选择 | 初判 |
| --- | --- | --- |
| 2606.12556 ITME | 将确定性weights/prefix访问映射为CXL-hybrid byte-addressable远端内存主动搬运；比较DPU/JBOF软件开销及容量边界 | 潜贡献/需核日，拟7但未授分 |
| 2606.12638 Eidola | 用真实annotated timing驱动最小GPU eidolon复现P2P写/轮询通信，支持fused-overlap瞬态交通隔离而非只有流量均值 | 潜贡献/需核日，拟6 |
| 2606.12703 SMSR | HMAC写时provenance与随机memory ablation的hypergeometric certificate分开，指出string-vote minority攻击；认证写入不等于内容可信 | 准入拟7，安全命题深入要求 |
| 2606.12747 Prefill Awareness | 把foreign-style检测与preference回退消融分开，prefill不是中性干预，影响alignment/control评价成立条件 | 准入拟7 |
| 2606.12753 GPU portability | gPLUTO天体流体应用OpenMP/OpenACC比较发现striding/register spill，未建立与foundation/LLM计算的新连接或新架构机制；通用portability常识不足 | 贡献前N，不因理论/编译主题拒绝，只限原实证范围 |
| 2606.12765 Rigel | 对Metal4.1 M4Max的FP8路径作checksum/provenance/功耗三信号实测，区分接口支持与硬件加速，影响精度选择 | 准入拟6，文档与实现反证深入要求 |
| 2606.12876 Drop-by-Drop | 单一有序additive codebook checkpoint的前缀子集跨bitwidth重建与Matryoshka监督，避免每精度独立产物 | 准入拟6 |
| 2606.12935 MARS | 部分trace探测当前答案，将switch概率与落点adversarial不确定性分开，约束提前停止不改变full vote | 准入拟7，保证依赖true概率须收窄 |
| 2606.12950 Maestro | stage语义预测length/memory，并联动node模型共置/cluster cold start/global workflow priority，改变多agent SLO资源预留 | 准入拟7，trace仿真与prototype不得合并 |
| 2606.13003 Illusion of MAS | 对自动生成MAS加入CoT-SC成本对照及可分解交互诊断，expert与auto architecture反侧，揭示复杂度不等于功能utility | 准入拟7，限制自动生成系统而非所有MAS |
| 2606.13054 TWLA | ternary-friendly旋转/流形重定位及相邻层二阶bit分配处理跨层误差，改变W1.58A4混合精度条件 | 准入拟7 |
| 2606.13174 TRACE | 将用户correction抽成原子规则编译为任务完成前runtime check，实测access-memory不等compliance，改变个性化约束执行边界 | 准入拟6，不能由仿真用户外推真实可靠性 |
| 2606.13233 ReSET | 区分低entropy错采样与高entropy过集中，以step/token熵调温；另small-M CUDA-core kernel，两个贡献分别核条件 | 准入拟7 |
| 2606.13276 Module manifold | Stiefel-attention/DGram-MLP与反置对照，attention奇异值膨胀→logit/softmax饱和，改变统一流形约束假设 | 准入拟6，shared超参的局部结果 |
| 2606.13280 Generalization | 扩展log-bilinear文本生成分布下推deep-transformer generalization与vocab/doc-count/doc-length依赖 | 准入拟6，需定理假设，不泛化为真实文本scaling规律 |
| 2606.13361 KV CDN | exact-load局部验证并测KV不可压缩/egress超过prefill省算成本，provider-side才去掉egress，改变跨供应方KV分发成本判断 | 准入拟5，作者估价和跨token-exact适用性待核 |
| 2606.13426 SpecDiff block | 连续residual sampling支持原speculative机制与block verification，Free Drafter分析改善acceptance | 准入拟6，不因6.3%局部收益排除 |
| 2606.13496 BudCache | 固预算下离线search cache schedule并对齐time discretization，不以阈值反推不可控runtime；同预算quality对照 | 准入拟6 |
| 2606.13657 OPD sparsity | dense teacher不等dense参数改写，实际小subnetwork恢复收益；SGD稀疏性与AdamW收益反侧，spectral集中不等low rank | 准入拟7 |
| 2606.13663 HyperTool | 原schemas下code block本地串联tools并训练compositional trajectories；代码执行/折叠trace本身已有，题摘未明确超既有code-tool机制的长期差额 | 决定点需窄读，尚不N/不评分；只核接口/对照是否新增条件 |

A1之后AB新增20，累计28份完整题摘；不是28全文或28候选。所有可能准入日期还需同精确DOI联合界核实，潜贡献明确与合法落窗分层保留。没有把未做的Methods改成外部保留项。

A2日期补核：上表除明确N的12753未为不影响处置额外请求外，其余19项同精确DOI的arxiv.content/findable/唯一v1 Submitted/registered联合界已全部实际复算为bounded `2026-06-12`、reasons=[]。原字段仍在本日两页DataCite原件中；12556/12638日期待核标记据此解除，不表示证据或准入独核已完成。created未作界。

## A3 具名去重与拟分 reconciliation（不删除校准过程）

root §1–3 已实际校准原28题摘的贡献判断，但候选还必须通过事件去重。定点查Jun11/Jun12正式候选表发现：A1/A2中16拟准入（12556/12638/12688/12703/12747/12765/12935/12950/13003/13174/13361/13392/13426/13496/13501/13591）、13663决定点与12487日期潜贡献，均为Jun12原候选同精确v1，旧窗口、日期、评分/有效证据保留，不列Jun13新候选、不重评分，不因本轮题摘校准替代旧有效层。已读必要证据保存在本日N2，仅为有限依赖核验，不凭“读得更多”新增Book段落。

因此原28AB实际为：7个未在旧Jun11/12列项的新增准入（12876/13054/13176/13233/13276/13280/13657）、3贡献前N、18同事件具名重复（含13663与12487）。不是23新增候选、不是28全文。对上述七精确ID另在2026既有Daily README（排除_sources/Weekly）具名检索无候选表命中，未做全年重审。

## A4 新模型/训练/多模态题摘（待root校准）

后续先按精确ID去重，B3取20份中12963/13053/13092是Jun12同事件，只到身份停止，未展开题摘/Methods；13400一次timeout未当零或排除。其余16完整exact-v1 AB实际读完；原件同命名规则，不取DataCite新版摘要。

| 身份 | 原有约束 → 原文实际增量 → 待改变选择 | 作者初判 |
| --- | --- | --- |
| 2606.12505 DPOP | 静态chosen/rejected忽略reference-greedy输出 → 仅policy仍偏rejected时启惩罚reference-greedy → preference gate与负样本人群 | 潜贡献明确/先核日，拟6但不授分 |
| 2606.12883 LoRA-alpha | alpha被视作LR等价 → signal-drift分析与实测alpha不能由LR替代，rank平方根尺度 → LoRA参数化与调参选择 | 准入拟7，不授普遍最优law |
| 2606.13106 SWITCH | 连续latent动作难定义普通RL比率 → discrete enter/exit anchors与latent递归反传 → on-policy身份及可因果probe接口 | 准入拟7，需核latent内部determinism/ratio边界 |
| 2606.13125 Select/Improve | RL是否仅选已知策略 → controlled SFT多样性/RL难度分解selection/improvement → 能力变化诊断与训练人口 | 准入拟6，机制行为证据非全模型推理定律 |
| 2606.13240 Jeffrey | guidance只给隐式能量/采样rule → 明确margin目标、保conditional结构并最小扰joint → sampling目标与控制权限 | 准入拟6，有限图像特征评价不认证全部fairness |
| 2606.13303 DuET | 每步source conditioning妨碍大编辑 → 暂转text-only再回edit → preservation/edit fidelity取舍，未改权重/步数 | 准入拟6，保source保存反退 |
| 2606.13655 Flex4D | dense multi-view生成依显式geometry先验 → 五轴RoPE加入view/SE3 relative pose、clean history rollout训练 → 空间/时间坐标与推理历史接口 | 准入拟6，human/animal训练混合非零shot任意几何 |
| 2606.13289 HYDRA-X | image/video tokenizer重建与semantic有冲突 → frame causal temporal/hierarchical压缩对照、decompressor教师语义、编辑在latent交互 → codec与LLM分责 | 准入拟7，多个部件分开核 |
| 2606.13674 RepWAM | reconstruction codec未对齐instruction动作 → representation visual/action tokenizer与joint future/action预测再adapt → visual fidelity不等控制latent适合性 | 准入拟6 |
| 2606.13672 WEAVER | worldmodel fidelity/long consistency/efficiency三方冲突 → multi-view latent+reward flow与受限真实policy评估/改进/planning证据 → model选择看下游闭环而非视频指标 | 准入拟6，摘要尚未给各设计消融，属证据审阅而非以细节不足拒绝 |
| 2606.13376 MoVerse | 单窄视角游走需持续空间状态 → panorama补FOV/持久Gaussian scaffold/causal renderer蒸馏分工 → world构建与观察生成状态归属 | 准入拟6，不将幻觉补景作原始环境证据 |
| 2606.13035 TetherCache | 固budget历史丢失与self-generated漂移 → gate relevance/diversity再statistical对齐新召回tokens → cache选择与context污染两独立机制 | 准入拟6，不授任意长保真 |
| 2606.12859 AIR-VLA+ | 平台与机械臂action scale耦合 → 单向cascade/gradient隔离与feature-level dense soft experts → 移动/操作条件方向和稀疏计算区分 | 准入拟6，非由VLA标题/score准入 |
| 2606.13679 InterleaveThinker | 长trajectory25+generator calls难训练 → single-step accuracy/stepwise reward训练critic，再planner/critic串联现有generator → reward是否保留跨步utility的受限接口 | 准入拟6，成熟planner+critic组合本身不计差额，不授single-step对整轨迹保证 |
| 2606.13565 A2D2 | anylength discrete diffusion含插入与unmask路径 → joint path RN导数/质量式schedule/AJD目标 → reward-tilted目标是否同身份 | 准入拟7，理论假设与实践近似必须分开 |
| 2606.12689 causal-geometric LRM | 可decode/BFS图案被当推理解释 → 无recurrence/curriculum的matchedcontrol也出现、干预graded effect → interpretability需要因果对照 | 准入拟6，负面结果不因无新模型拒绝 |

A4十六个精确ID及前述七项已在2026既有Daily候选表做具名检索（排除_sources/Weekly），未命中；未扩为历年候选池。新十六日期仍逐项核，不把AB本身当日期证明。

A4日期补核：十五个非12505身份同精确DOI原字段实际复算全部bounded Jun12/reasons=[]；12505唯一v1最早公告界Jun11 00Z、registered在Jun12，整个可能区间跨Jun11–12，保持潜贡献/日期保留，不评分/Book/确定表。此前原件time-out的13400只在导航保留，尚无题摘判断，不伪称排除或外部穷尽。

## A5 两个贡献决定点（窄读后交root）

root A4一次AB/日证校准已通过十三项（12883/13106/13125/13240/13303/13655/13289/13674/13376/13035/12859/13565/12689）及12505日期隔离；13672/13679暂只贡献决定点，不因好指标先准入。以下不是全部pipeline证据完成。

- **13672 WEAVER**：实际只读exact-v1 §3与§5.1：§3.1明确在wrist/exterior视觉latents之外jointly预测proprio token（arm/gripper），相对于Ctrl-World只预测views，这让消费`(views,q)`的冻结policy能在同一imagined rollout继续生成action，改变worldmodel输出/consumer闭环合同；不是凭“worldmodel三目标”映射。稀疏每k历史+最近两帧memory明确继承Ctrl-World，不把它单独算新机制。§3.3把RoboMeter外部reward蒸馏成latent+language rewardhead并用共享设计critic估截断horizon，避免每个candidate解码图像/调用外部VLM，改候选评价费用接口；teacher reward仍是可错label。§5.1仅直接确认同NFEs/单H100与DROID256/OOD100的视觉质量/时间及reward相关性，尚未读完下游真实评价或proto/state消融，不宣称新增state必然因果或真实安全。作者建议基于joint-state consumer接口准入6，后续只核该采用命题的直接消融/反侧，不泛审所有模型。
- **13679 InterleaveThinker**：实际只读exact-v1 §3.2–3.3、§4.3/T5，找到具体数据/奖励决定点：高质量teacher生成物易使critic全True，混入弱FLUX形成negative；steps先按Gemini评分的稳定高/改善曲线过滤，迭代分数variance高分RL、低分SFT（2:1），再balance binaryjudgment。Reward将判定误差`-|pred-J|`和实际一次regeneration后的Gemini score delta分开，两者并非同一信用。T5去任一reward均低于完整，unfiltered critic出现constant True（但过滤与balance未独立隔离，variance split无单独消融）；OneAgent把planner混入critic的效果更低，也不是同调用budget因果。原文“固定预计划→每个stage独立→local success guarantees global”没有由这些证据成立，前一生成图仍被后段消费；不采用该保证或single-step=fulltrajectory等价。作者建议只以判定/改进两个反馈接口的局部成立条件准入6，或由root判其仍属成熟组合后N；不因实验细节不足放H，不继续泛读25call生成器。

A5独核更新：root§11已实际读上述指定决定点并授两项2+2+2=6准入。13672只jointfuture proprio+views消费状态/latent reward接口，memory继承；13679只强generator正例偏置/判断vsregendelta及必要对照，过滤/balance/variance归因未独立、fixedplan不证local→global。已读核心可复用，仅补setup/直接限制，不第二全pipeline首备。至此当前新增准入22，不是22实证/Books完成。

## A6 后续模型与Agent完整题摘（待root校准）

本批22精确ID先在2026既有Daily候选行具名检索（排除_sources/Weekly），无命中后取AB；12789一次timeout尚普通恢复，另外21完整exact-v1 AB已实际读。不是22份完成，未Methods。

| 身份 | 原文具体增量 → 待重考虑的选择 | 初判 |
| --- | --- | --- |
| 2606.12629 Bag of Dims | 标准basis的sign/magnitude读写、跨Qwen/Gemma/Mistral比较 → SAE/decoder训练是否必要及axis-aligned解释边界 | 准入拟7，不先认binary独立寄存器/无coupling普遍保证 |
| 2606.12666 CAPED | 任务条件phone侧pre-upload选择暴露与seeded trajectory测量 → 屏幕utility与incidental privacy边界可否同时验收 | 准入拟6，非仅all-or-nothing masking常识 |
| 2606.12716 PaperGuard | figure PGD与text GCG/promptinj共同攻击review targetscore → text-only审阅安全评估的具体跨模态盲区 | 准入拟6，不因科学文档任务等同科学应用研究；只评估/攻击机制 |
| 2606.12730 Psychometric | task-specific intention vs Big5、shared/separate context/persona对照 → selfreport是否能代理部署行为的成立人口 | 准入拟6，非人类心理人格诊断 |
| 2606.12744 GRIP | 以LMM反馈utility训练vision retriever并跨consumer迁移 → 视觉相似例不等ICL有效、retrieval复用资格 | 准入拟5，若只既有utilityretrieval组合由root定点校准 |
| 2606.12818 Anchoring | edge vs node circuit faithfulness、within-model双anchor方向与posttraining跨variant反侧 → 解释路径迁移资格 | 准入拟6 |
| 2606.12830 PERIA | Observation-Relaxed Group-in-Group更新与工具证据 → multi-tool credit/observation人口接口 | 准入拟6，工具组合本身非差额 |
| 2606.12841 TimeROME | temporal indirect effect定位denoise后果、低rank residual memory每forward应用 → AR locate-edit迁到MDLM的时间坐标与冻结backbone边界 | 准入拟6，unlearning安全命题深入，logprob降非已删除 |
| 2606.12854 Biomedical shortcut | QLoRA/小模型对照本身是领域应用，但matched-size双向迁移揭示SciFact结构artifact，题摘未给实际artifact | 决定点窄读；不能凭biomedical标题拒绝潜评价混杂，也不能用“未报shortcut”四字授机制 |
| 2606.12871 DailyReport | 150tasks/3546cascade rubrics与分维归因、17systems未达期待 → 当前题摘只任务/量表扩展，无具名新混杂或可改变设计的失败条件 | 初判贡献前N，非因benchmark类型自动排除；供独核 |
| 2606.12898 AGAR | localization attention与正确性解耦，patch映回word再局部放大干预 → 视觉文字读取容量与attention作为proposal非使用证明 | 准入拟6 |
| 2606.12900 HCPD | weightedcriteria动态分解、弱semantic-consistency reward/理论reliability，未明新feedback身份或可靠条件 | 决定点窄读objective/theory具体差额，不提前N或因无细节H |
| 2606.12903 X-MADAM | 规则在模板冲突benchmark完美、去template后两类系统反转且oracle仍好 → extraction瓶颈/benchmark混杂的反侧 | 准入拟6，负结果保留 |
| 2606.12917 TabPFN causal | toyregression patch/ablation强head定位，contrastive steering不跨sample → LM稳定方向假设不能搬tabular ICLconsumer | 准入拟6，不以toy规模拒绝 |
| 2606.12942 PRISMR | fluent排序遗漏候选不是只格式错，parallel hypernet为candidate生成instanceLoRA → in-context list结构转parametric conditioning的代价 | 准入拟7 |
| 2606.12979 EPM-JEPA | prereg operator-v-operand null与buffercycle/EMA/LoRA transient分解 → shift曲线不能叫平衡收敛，经验载体选择须控动态 | 准入拟6，secondary1.9%不篡改primary null |
| 2606.13006 Emo-LiPO | fixed transcript内global intensity order作listwise preference → 声学强度与semantic文本条件的目标对齐 | 准入拟6，非把数据/任务新名当机制 |
| 2606.13040 RoboProcess | 58kQA/12过程类别/260task与SFT改善，题摘未识别具体新confound或新成立条件，主要细分类别/监督扩展 | 初判贡献前N，非因为机器人或benchmark拒绝，供独核 |
| 2606.13061 LaME | Kreason tokens固定capacity bottleneck与两弱监督分离contrastive/AR目标 → 低延时embedding不依显式CoT数据的替代接口 | 准入拟6 |
| 2606.13095 ASR/diarization | 双encoder interleave、lengthaware speakerID loss和overlap ASR threshold → 字内容与speaker监督权重分责 | 准入拟6 |
| 2606.13097 FCGraft | validated function skeleton的KV stitching/patching复用 → 代码局部控制结构与prompt cache身份组合条件 | 准入拟6，验证骨架不认证新policy或KV exactness |

本批同精确DOI联合日期尚需逐项复算，拟准入不先当正式Jun12候选。后续只按校准后的实际增量必要阅读，不把导航剩余标题变逐篇关闭配额。

A6日证更新：21份已读AB身份的同精确DOI/arxiv.content/findable/唯一v1 Submitted/registered联合界实际全部复算为bounded Jun12、reasons=[]，原字段在本日两页原件。日期层通过不替代贡献准入；12789timeout尚不在本批已读/已核数量。

## A7 两个一次timeout的有限恢复（待root校准）

仅各重试一次后13400/12789均200，完整exact-v1 AB实际读完，前述timeout待办解除，不继承失败为零或终态。两精确ID在2026既有Daily候选行具名检索无旧归属；同精确DOI联合界均bounded Jun12/reasons=[]。

- **2606.13400 PolyFlow**：posthoc投影会耗时/改分布 → discrete-time flow与constraint embedding/projection-free architecture直接约束polytope支持 → 生成路径可行性及离散执行误差合同。作者拟准入2+2+2=6，安全保证受影响须深入精确假设，不先认任意constraints/finiteprecision零违反。
- **2606.12789 HieraRAG**：合成5872QA、单BM25+Falcon3-10B，在三维/2–4–8类中以同配置各类生成质量std定义granularity区分度，增加CoherenceRatio与110人工检查；只报告taxonomy/proxy峰值，没有具名可改变模型系统评价有效性的新增混杂或成立边界，std跨类别本身也不是跨系统排序区分度。作者初判贡献前N，不因为benchmark/单模型实验自动排除，不为不影响处置扩Methods；交root校准，若proxy实际新增可验条件应重开决定点。

## A8 最后一组主题补检题摘（待root校准）

本组23份exact-v1完整AB均已实际读；先在2026既有Daily正式候选行具名检索，无旧命中，不含_sources/Weekly。原件为本日SUP_RAW_ABS_2606.<ID>，同精确DOI全为arxiv.content/findable，唯一v1 Jun11截止前，公告最早界Jun12 00Z至各registered上界Jun12 01:58:17Z–02:16:06Z，逐项复算bounded Jun12/reasons=[]。这不是23份必要审阅完成；以下仍交root准入校准。作为本窗RAG/Agent/评价主题有限补检，不把导航剩余标题转全类队列。

| 身份 | 原文实际增量及影响选择 | 初判 |
| --- | --- | --- |
| 12852 WISE | event memory加入causal why/which图关系、task条件检索与机会式调度，影响what/where记忆是否足以支撑长程controller | 拟6，因果图标签不先当真实因果 |
| 12924 e-commerce agents | rolling memory与intent抽取在同buyer人口比较、过程judge与结果judge不一致，影响会话压缩与评价代理 | 拟6，只采用受控成立条件，不因商店应用入选 |
| 12983 STG | deterministic结构化RTL testbench、false-pass/coverage评价与curated oracle，影响代码agent verifier资格而非只Pass率 | 拟6 |
| 13100 LEDGER | 年报/KPI数据、OCR标注、retrieval/extract基线和市场案例；题摘未给新机制/可修正系统选择的具体confound | 前N，非因金融领域/benchmark自动拒绝 |
| 13104 AuthorityBench | claim真假×citation真假平衡2x2、无citation控制，揭示正确claim+伪权威的独立幻觉效应 | 拟6，事实性与权威线索解耦 |
| 13141 CARVE/VideoRAG | 可不看视频答旧题的盲区、chunk证据triplet解耦检索/生成及granularity-aware reranking | 拟6，具体证据依赖而非视频benchmark数量 |
| 13168 BlockAttnRes causal | inference包裹recency控制能复现平均routing，而routing mass不等causal necessity | 拟6，不把routing图当结构解释 |
| 13175 End of Code Review | position主张agent更快/便宜、human gate过时，完整AB未给新增机制或可核的成立边界 | 前N，不因position类型排除 |
| 13197 ARMOR-MAD | PAR预一致/EASE早停/SOD语义离群联合debate；AB只成熟组件组合与总收益，尚无改变何种选择的具体成立条件 | 前N，若root见具名新条件可决定点，不因已知缩写拒绝 |
| 13204 CoDeR | coverage encoder+compatibility encoder，以lexical polarity构造满足/违反负约束对照，推理不用LLM | 拟6，负约束匹配与主题覆盖分责 |
| 13262 ProFact | 单policy分解/证据/回答/verdict及stage-aware reward，AB未明相对既有stage RL的credit新身份 | 单决定点，非笼统因缺实验细节拒绝 |
| 13316 ReSum | 自发summary位置mask phrase与非summary位置插入phrase的匹配反事实分支、summary-aware advantage | 拟6，summary效果不是仅短输出关联 |
| 13435 GIVE | skeleton/ray叠图与gesture文本两路增强既有VLA，AB好指标之外未给新原语/具体组合收益条件 | 前N，非因手势/VLA应用排除 |
| 13507 audio filtering | 轻ranker伪label再distill audioLLM keep/drop，AB仅成熟两阶段监督迁语音对 | 前N，不以数据规模/小收益排除 |
| 13533 OneRetrieval | identifier属性字词对齐+codebook reserved slots部署后绑定新词免重训，影响GR实时editable资格 | 拟6，部署/订单结果仍待配置核 |
| 13537 QueryMix | controlled embedding-mix比例、English-index非对称与typology反侧，影响混合语query是否总应单语化 | 拟6，embedding插值不是自然code-switch句 |
| 13544 ModeratorLM | assigned-role条件/CoT与合成多方会话，AB仅成熟role prompting迁turn-taking加总体分数 | 前N，非因语音/数据集排除 |
| 13550 UMG-RAG | score entropy专家融合、多granularity与parent promotion，AB目前仅已知confidence融合/父chunk组合，无具名新增成立边界 | 前N，不把所有融合公式自动当长期差额 |
| 13607 pattern reasoning | specific heads驱动LLM与预测human irrelevant-detail错误，修正human/model推理对比与头重要性解释 | 拟6，不先接受人脑同机制因果 |
| 13668 Influcoder | 题名指decoder gradient influence ranking蒸馏encoder，但完整AB仅声称快/便宜，未说明teacher/student身份/保序条件 | 单决定点，机制若清楚即准入，不泛审效率pipeline |
| 13669 Agents-K1 | scientific schema/4B GRPO抽取/graph CLI组合与大科学图谱，未给一般模型系统新接口或效应条件 | 前N，科学应用暂缓且不借Graph/RAG节点重引 |
| 13673 SpatialClaw | stateful Python逐cell+反馈/visual观察，AB仅把成熟REPL工具执行用于空间工具，多benchmark总收益非新接口 | 前N，不把code本身等成熟机制排除所有接口研究 |
| 13680 RA-RFT | gold relevance distill以expected reasoning benefit排序，再retrieved analogy做outcome RL，对semantic overlap替代目标及互补策略人口 | 拟6，utility label构造与泄漏反侧待证据核 |

A8作者初判12拟C/9前N/2贡献决定点；仅当前批局部计数，不覆盖旧批/不预定最终候选比例。

## A9 原三个决定点实际窄读

- **12830 PERIA**：仅exact-v1 §4.3 OR-GIGPO段与Appendix C.3。原GIGPO要求同anchor state，视觉tool-agent文本即使同tool/等价参数也可文字顺序不同；本项保持episode组不变，只在同prompt内先hash exact observations，再对文本代表用SequenceMatcher≥0.9合并，image-return exact；仅多于一个entry组计算step advantage、回填相应token span，ω1/γ.99。新增是组资格/observation约束放宽而非创造两层advantage。SequenceMatcher是序列字串相似，不保证同latent state或语义等价，后续需核误merge/returns与控制。具体增量已明，作者建议准入6，足即停，未泛审视觉工具pipeline。
- **12854 Biomedical shortcut**：仅exact-v1 §4.2。SciFact全部NEI evidence空，而supports/refutes全部有evidence，因此仅evidence-length即可完全分离NEI而无须读claim，fine-tune macroF1会混入输入结构shortcut；不是一般的“跨领域掉分”或医学应用。该具体标注/输入接口混杂支持一般claim-verifier评价修正，作者建议准入6；真实数量、实际prompt是否暴露该字段与迁移对照待证据核，未因小模型/负结果拒绝或展开QLoRA全流程。
- **12900 HCPD**：仅exact-v1 §4.3–4.4/4.6。具体仍是自主生criteria/weights/scores加权、BLEURT参考相似度离散1–10后absolute-error reward、i.i.d bounded-score Hoeffding均值，ranking式预先假设truth单调proxy且uniform bias bound；该假设不是已验证新可靠条件，也不由训练对齐推出truth可靠。没有区别于既有rubric分解、弱标签回归和多样本均值的新feedback身份/具体反侧。作者由决定点改贡献前N，不因既有组件名字或需Methods费时排除；保留已读公式/假设，若root见具体新增条件可指出窄层，不泛审全部hallucination pipeline。

A9未新增AB，原67数量不变；建议两C一N待root实际核，不先改正式计数或把潜在C当已证实。

## A10 Kimi Code Jun12具体runtime修复（待root校准）

官方 `https://www.kimi.com/code/docs/en/kimi-code-cli/changelog.html` exact0.14.1/0.14.2两个日期均Jun12，已实际读两版完整核心，raw `SUP_RAW_KIMI_CHANGELOG_20261026.raw`。恢复展示时读到了邻日变更文本，但不把它们纳入本窗或扩审，所用事件只有0.14.1/2。

具体不是版本标签：0.14.1取消session shutdown时active turns，使foreground shell不越过prompt退出，默认stop backgroundtasks，并修正overlapping interactive requests使用错误activeagent的绑定；媒体fallback/Responses instructions/env透传/ACP兼容等其余短说明可见，但不外推出已实现安全。0.14.2恢复compaction的completed/cancelled展示和terminalprogress capability guard，以及若干config/streamUI维护；这些不另造长期模型机制。

作者建议将**Kimi Code CLI lifecycle fixes**作为一个材料家族、窗内两release事件，贡献仅当前版本的shutdown/agent-request正确性边界，拟1+2+1=4、关闭判断/仅报告（版本事实，不改变长期Book机制），非引成熟cancellation原则抬分。原文可支持“官方称修正这些行为”，不支持代码已验证、全subprocess已回收或无跨session泄漏；没有具体实现/新条件，不为泛审整个repo造深度。若root按“仅现有约束的普通修复、无可保留新增”判贡献前N也应保上述确切原因，不把本源改零发布。此项尚未独核，不混入当前38计数。

## A11 A8两贡献决定点窄读

- **13262 ProFact**：只actual§3.3。Question与Search两stage用goldquestion / goldQA字符串的METEOR矩阵做maxweight一对一bipartite matching，除goldset大小；Verdict给最终labelmatch，空/invalid为0。是既有gold中间监督指标与stage credit组合，未给区别于成熟过程监督的新feedback身份、资格或具体原方案失效条件；一对一匹配本身不是新长期机制。作者建议贡献前N，保已读公式，不展开整个factchecking RL pipeline；不是因摘要缺细节/事实核验领域排除。
- **13668 Influcoder**：只actual§4.1–4.2和Relatedwork中Distillation-based段/Contribution。targetdecoder收response-only LoRA gradients（排head/embedding），CountSketch后预算pool×query cosine影响矩阵；encoder分别编码sample、同cosine预测，Pearson全batch与每query softmaxKL联合distill，以低存储/免每query梯度替代。相对AirRep distill true loss且interdependent sample architecture，本项distill gradient-influence ranking并保持独立可缓存sample编码；IProX全grad proxy不同target人口，未先认对方可比或加速全费。实际新增teacher identity/独立producer与rankingconsumer接口已清楚，作者建议准入6；后续仅必要核模型/投影/heldout/速度全费和teacher不是causaltruth，不泛审全DA。

A11未新增AB，只解决A8原两决定点，拟一C一N，待root核；原AB90保持，不将source预取当必要完成。

## 发现/准入最终收束（保留上文分批历史停点）

root§24/30/32已实际独核A8/A9/A10/A11所指原件/精确日证与准入：90完整AB最终为53新候选、18具体贡献前N、18旧Jun12同精确v1事件、12505跨日日期隔离；另Kimi两Jun12release同一家族4分关闭，正式54families。此后没有新窗/新候选或重评分；PERIA具名current-v2澄清只恢复该家族受影响层。原23等局部拟准入数与待校准句是历史过程，不替代这一最终分母。后续必要证据/实际owner/Book写后检查按NECESSARY和root唯一canonical保留，53准入从不等于53篇强结论已证。
