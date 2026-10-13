# IOMM16139：必要原证、唯一 owner 差额与受限 PRE

仅本19既有具名家族，resume_mar17准备、非本日报作者；2+2+2=6保持。压缩恢复实际重读AGENTS、研究/Report合同、统一prompt、完整ROADMAP、来源使用/每日及arXiv主题、本19README/STOP与LS最新相关路由。只准备本项，不改Books/Report/LS，不扩发现或下一日。Books背景沿用本19未变有效上下文；真正写入前再加载适用Books约束并协调窄锁。

## 身份、日期与必要 Source

标题为Rethinking UMM Visual Generation: Masked Modeling for Efficient Image-Only Pre-training。精确来源[2603.16139v1 HTML](https://arxiv.org/html/2603.16139v1)；日期复用SUP_LATER_METADATA_20261011.json:851起的arxiv.content findable、created/registered 2026-03-18T02:25:15Z夹证，与本19已校准availability日下界共同限定03/18归属，不以Submitted03/17T05:41:48Z充公开时刻。当前[官方事件页](https://arxiv.org/abs/2603.16139)实际header/Comments/history仅v1、Comments为代码入口；没有所见撤回/具体勘误，不遍全站或版本史。

必要实际范围：完整题摘及§3.1–3.4/概率路径与目标/Alg1（HTML约105–180），§4.1–4.4/Tables1–3及直接反侧（181–306），§5（307–309）；B.1–3/Tables4–6（418–479）核架构/优化/数据/适配边界，C.3/Table9（541–556）核六配方对照。工具开页带出的C.1/2/4/5部分文字不冒全附录/图像逐项阅读；不拟合图、不读全部prompt附件、代码或旧版，不复现。机制及直接反侧已够拟采用有限命题，停止原证扩读。

## 核心接口及不能混淆的身份

§3.2–3.4/Alg1：新阶段图像x既作重建目标，也通过冻结ViT成为条件。先对干净图像的条件embedding作二元乘法遮蔽，连固定通用辅助文本prompt；RQA用256个learnable query产生附加序列，与原条件concat后进入冻结MLLM g，输出h供新训练的flow generator。训练x_t=(1−t)x+t z、回归z−x的稠密L2目标；不是只在缺失位置算loss，更不是生成器masked-token提交/删token省算。随机初始化的是generator与RQA，不是完整MLLM。RQA在g之前追加条件，而非把残差加到g内部hidden或输出。冻结权重不消除g、ViT与codec的消费成本，也不自动切断学习RQA所需的计算链；不声称已核具体autograd实现。

本文image-only只限定新增预训练图像语料不使用对应caption，仍继承预训练InternVL3-2B/ViT的语义先验，存在固定文本prompt，之后另消费paired或mixed语言对齐。不能写成无历史配对监督、整个UMM从零获得理解、冻结理解路径就认证所有下游能力保持。§3.4文字称patch token mask，公式却给P²×D逐entry Bernoulli；本次只采用条件embedding遮蔽的位置与目的，不采唯一token级抽样实现或精确最优rate。

§4.1使用1.6B/2.7B MM-DiT，XL 6B改Z-Image体系，冻结InternVL3-2B为特征抽取。主文宣称B/L AdamW和全部EMA，B表实际L预训练Muon、L/XL不设EMA；以附录实际配置保留这个不一致，不据正文做严格跨尺寸因果。B.1约11M图像、512预训练；B.2约210K高质量图像、512/1024对齐，B/L遮蔽.85、XL.45，混合比例.5。B.3 OpenUni全调connector/generator，Qwen20B LoRA rank/alpha64，均冻结理解模块；只证明所测微调分支，不当20B从零image-only预训练复现。

## 关键评价、反侧与全费用

- C.3/Table9固定约5预训练epochs/11M图像、10微调epochs/210K图像，pair-pretrain后image/pair/mix的GenEval为.78/.86/.88，image-pretrain后为.61/.87/.89。图像预训练接图像微调反而差，不能继承§4.3“任意微调都至少相当”式普遍外推；可保留paired/mixed对齐之后的有限收益，1point小差没有所读范围置信区间，不能唯一归因mask/RQA或所有UMM。
- Table2 OpenUni基线.85/.52，image微调.74/.49，paired .88/.62，mix .88/.59；mixed非全部指标胜paired。Qwen512 image-only GenEval .42低于base .85，paired/mix .88/.89；1024部分slice仍退。NFE OpenUni20×2、Qwen50×2，不能跨底座把分数当同算力比较。Table2 Qwen512 paired WISE.63与C.5/Table10 .62不一，不采该精确数差作为因果证据。
- Table1 B512 GenEval/DPG/WISE .89/82.95/.55，B1024 .87/80.71/.50，L部分结果更低；容量、分辨率和预算并非单调。BAGEL的Table1 .88带rewritten-prompt标记、WISE.52与摘要.82/.55不一，BLIP3-o也有数据/数字差异；不依摘要或异协议榜单授SOTA全质量支配。
- Table3 image-only-pretrained B编辑整体2.82高于同类paired2.61，但低于BAGEL3.20等、Remove仅1.30。zero-shot只说没editing专项训练，不是整个模型免训练。WISE生成评价及编辑分数不认证完整理解/事实正确/安全或任何world-model闭环。
- §4.4同256query与数据的RQA/MetaQuery对照、遮蔽过大与纯图像微调反退支持条件难度和阶段边界；mask .45最佳属于XL局部实验，不挪给B .85；mix .5作者局部稳定性不授全模型最优。未逐像素核Figure4，不提供自行拟合斜率/精确误差条。
- 作者B约1050 H800 GPUh（1000新阶段+50对齐）不覆盖历史MLLM/ViT/codec预训练、数据/合成caption生产及全部sweep/evaluation，不能称完整生命周期降本。所读必要范围未披露该计时完整precision、GPU数量/利用率与模型比较同预算、全部训练/推理硬件和实际end-to-end serving SLO；标Not Disclosed，不补造。batch/尺寸/epochs只支持对应配置，fixed epochs不等fixed compute。

## actual 唯一 owner 与具体差额

sole `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24：实际1078–1140顺读typed unified generation、any-to-any、理解先验监督与双条件桥。1122–1135已有冻结expert从noised生成中间表示重述caption/回归feature的辅助梯度；1136–1138已有冻结MLLM的prompt增强/flow桥＋T2I注入。都没有“先遮蔽干净图像条件，再经可学习附加query/冻结MLLM训练新的稠密flow重建目标，随后另对齐文本条件”的阶段接口，不能仅同understanding prior主题记NC。建议紧接当前1138双条件桥边界后、1140 Discrete/Continuous双流标题前单段，不改旧有效正文。

Ch23实际387–412的codec/noise、causal prefix与CompressV重构→语言对齐拥有压缩producer与理解consumer，不是本项新generator目标；不在Ch23重写相同分期原则。Ch24 1916–1921明确生成路径/目标由本章、PartIV Ch28接训练优化。Ch25实际1–28区分视频生成与action-conditioned dynamics，本项不获WorldModel身份。Ch28只交接数据/训练执行，不另建第二owner。

## 逐字 PRE（尚未授权 Books，待 root 非准备者独核）

成对图文稀缺时，理解先验与生成目标也可以分阶段交接，而不只在已训T2I上增加条件桥。一个[受限图像预训练分支](https://arxiv.org/html/2603.16139v1)先遮蔽干净图像的条件embedding，连同固定辅助文本与可学习附加query送入冻结MLLM，再以其输出条件训练新的flow生成器重建同一图像；遮蔽改变的是条件信息量，不是只预测缺失token或删除生成器计算。随后再用成对或混合数据学习语言条件对齐，因而image-only只限定新预训练阶段，不能抹掉继承的语义先验或后续paired监督。条件encoder、query、codec、生成目标与阶段数据应一起版本化，重建通过不代文本遵循或完整理解验收。作者六配方对照中纯图像微调仍有明显反退，mixed也不在所有指标胜paired；局部rate、榜单和新阶段GPU小时不授普遍最优或全费用更低。冻结模型消费、历史预训练、数据生产、适配与完整评价均须分账；条件shortcut、语义偏差、对齐或总预算回归时，保留成对训练、原生文本条件或独立理解/生成模型，不由重建分数批准发布。<!-- source-family:SF-2026-ARXIV-2603-16139 -->

静态注：`SF-2026-ARXIV-2603-16139` — [exact-v1](https://arxiv.org/html/2603.16139v1)§3.1–3.4/Alg1、§4.1–4.4/Tables1–3、B.1–3/Tables4–6及C.3/Table9；仅条件遮蔽→稠密flow重建→语言对齐的有限接口，不采唯一mask实现、普遍最优/SOTA或全生命周期费用保证；未核代码执行或复现。

## 停止与独核请求

root 实际非writer POST：顺读新Ch24 1140完整段、1128–1153的辅助监督→双条件桥→新阶段接口→离散/连续双流交接及2450–2455自身来源注/邻注，原单段和静态注逐字一致。条件遮蔽与稠密flow、历史先验/后续paired监督、反退/全部费用及退路均留正文；机制不在Review notes后，无名称列表或通用旧原则冒新差额。限定diff检查无输出，实际POST通过，释放Ch24窄锁；可计本日受限整合，不授DAY、实现核验或复现。

root 非准备者必要Source/actual owner/PRE：实际 exact-v1完整题摘、§3.1–3.4/Alg1、§4必要T1–3与设置、B.1–3/T4–6及C.3/T9直接反侧，确认mask在干净图像条件embedding、RQA追加在g之前、冻结MLLM条件配新稠密flow目标，不能混作masked生成或免paired历史。实际Ch24 1078–1145完整统一生成/理解先验/双条件桥交接，缺少本阶段接口且非仅主题关联；原单段在双条件桥后成立。纯图像微调.61对.78、OpenUni mixed WISE.59对paired.62与局部配置/费用边界近文，未采SOTA、唯一mask实现、理解无损或全生命周期预算。2+2+2=6及sole MULTIMODAL-GENERATIVE-PARADIGMS原逐字PRE/静态注通过；只授准备者这一段/自身注窄锁，root非writer实际POST仍待，不计safe/DAY。

请root非准备者独核上述必要Source、actual sole差额与原一段PRE是否充分。建议受限整合而非中心隔离或主题NC，但未批准前不改Books、不计safe/DAY。仅一次重开需求：实验对应mask实现与配置/EMA勘误、独立held-out理解与生成质量、同数据与全部生命周期预算/不确定性；用最小artifact、受限对照或作者勘误即可，不因未采外推要求遍全代码/全附件。普通必要支持已足，当前只待具名独核/ownership，不称外部受阻。
