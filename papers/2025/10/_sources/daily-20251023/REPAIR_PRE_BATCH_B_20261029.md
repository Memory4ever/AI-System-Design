# Batch B 整体PRE：四项具体长期差额

writer Locke / sole reader Chandrasekhar。仅以下各一完整段、独立marker及唯一H2 Review notes下本人注。现有正文/marker/他注全部保留，未写入。相关owner、完整直接邻接和相邻章职责已实际读；本人注由reader一并核磁盘注位邻接，不授全章锁。四项均2+1+2=5，具体知识缺口触发拟采用域深入；支持与直接反侧见本日EVIDENCE及R14。

## B1 APT / MULTIMODAL-REPRESENTATION / Ch23

文件：`books/part-03-multimodal-world-models/23-multimodal-representation.md`。已有codec原语稀疏和encoder后token压缩不含输入像素按局部熵生成多尺寸patch及dense读出的网格回映。Ch22接长context，Ch24接生成，不占输入codec责任。

### 完整前邻接

前者仍把选中区域解码为 RGB，兼容已有 vision encoder，却可能漏掉 codec metadata 未显著标记的语义变化；
后者减少重复 decode/encode work，却把 codec、GOP、motion vector、residual layout 与 tokenizer 一起变成模型
输入协议。Transcoding、随机 seek、corrupted stream、不同 codec/profile 与 frame-rate conversion 都可能改变
token identity。Dense frames 在格式多样、证据完整性优先或 codec path 不可信时仍成立。

### 完整新增与 marker

单幅已解码图像也可以在进入视觉encoder前减少patch数，而不先付完整dense前向：按像素熵递归细分区域，平坦处用大patch、复杂处用小patch，将各尺寸缩放后接入共同embedding；原高分辨率的局部补充则通过额外投影保留。[APT的受限分支](https://arxiv.org/html/2510.18091v1)还须为变长序列packing保存图像隔离mask，并在密集预测时按原空间支持将大patch特征回映到网格，不能把较短序列直接当成原dense输出。像素熵不是问题语义重要度，小纹理区域也可能含关键证据；切分、缩放、位置/回映、packing与适配训练均计费。基线后端改造和指定GPU/任务的局部吞吐不证明全链零开销或无损；细节、网格消费者或净预算失配时，保留固定patch、更密输入与原encoder，不由输入token少批准所有任务加速。

<!-- source-family:SF-2025-ARXIV-2510-18091 -->

### 完整后邻接

稀疏编码还可以携带一份完整参考feature，而不要求后续帧每次独立经过全部视觉计算：按固定间隔完整编码I-frame，随后各P-frame只取当前少量patch，将同一I-frame feature线性映射成residual tokens，与当前观测一起交给冻结ViT。[受限跨帧分支](https://arxiv.org/html/2509.13255v1)复用的是本组I锚点，不是递归把上一个P当新锚，也不是直接复用完整KV；组号、原frame/patch位置、锚点与tokenizer版本须共同定义表示身份。它把当前细节与参考上下文分责，不能由补入旧feature推断未读区域没有新证据。压缩流motion选择若平均了未来帧，就另有lookahead和驻留费用，不能因P-frame到达顺序签严格在线；小运动、拥挤、帧距扩大和镜头变化仍可漏失，更多省算也伴任务退步。完整I编码、教师/线性tokenizer训练、motion制备、两次前向与全部下游回归都付费；大batch局部吞吐不覆盖小batch反而更慢或完整服务SLO。锚点或当前证据失配时，缩短组、增加当前patch或回逐帧dense编码，因果场景另用无lookahead且独立验收的选择器，不把重锚建议写成作者已实现的自适应恢复，更不将feature复用当环境状态预测。

### 本人注

本人注：`SF-2025-ARXIV-2510-18091` — Locke，Daily2025-10-23补Oct22；exact-v1 §3/4.1–4.2/4.4/B必要，2+1+2=5，quadtree输入patch/packing与dense grid消费者差额深入。保熵非语义、resize细节/回映费用、baseline FA改造和指定A100/A6000人口，不授全任务无损或pipeline零费。未核实现/复现；PRE/真实SAVE/全自读/sole actualPOST仅按本日实际层。

## B2 Hydra / MODEL-MULTI-HEAD-ATTENTION / Ch15

文件：`books/part-02-model/15-multi-head-attention.md`。已有head冗余/共享KV，不含把head分组组织为ensemble成员并共享MLP后的函数/uncertainty双验收。Ch14仍单head读取，Ch16仍逐位置MLP；这里不重复推导MLP或另立ensemble章。

### 完整前邻接

因此，多头结构提供的是**可分化的表达路径**，不是 `H` 份必然有效的独立能力。已有剪枝研究表明，特定训练模型和任务中的一些 heads 可在较小质量变化下移除；这能证明冗余可能存在，却不能推出所有层、所有输入都有同一组“无效 heads”，也不能把 post-hoc 分析直接等同于生产加速。真正跳过 head 需要训练期 pruning、gating 或稀疏执行 contract，并让 checkpoint、kernel 与评估共同支持。

### 完整新增与 marker

Head轴还可以被组织成多个ensemble成员的计算接口，而不只是删掉冗余头：从共同基座剪出不同head集合，以分组投影保各成员的读取路径，再让它们消费共享的MLP，并在序列或深度布局中保留member身份。[Hydra的受限对照](https://arxiv.org/html/2510.18358v1)用这种计算共享减少重复，但平均MLP与共同预训练并不保持各独立模型的原函数，也不能把成员分歧当作独立、已校准的不确定性。应分别验分类质量、分歧/校准和完整执行成本；所测BERT的ensemble基线还共享预训练，有限BF16计时不是所有硬件的单模型费用。剪枝、成员恢复训练、分组activation与全部分支均计费；多样性、质量或净预算失配时，保留原MHA、真正独立成员或单个已验模型，不由一次forward名称批准独立证据与普遍鲁棒性。

<!-- source-family:SF-2025-ARXIV-2510-18358 -->

### 完整后邻接

固定总容量H之外，还可以让输入决定当前启用多少head、以及启用哪些head：用globalpooling分别产生预算标量与head排序，训练先加权全部head，推理再只消费硬选集合。预算与身份是两项接口，不由较小权重证明对应计算已跳过，也不由平均pooling获得token级难度真值。[BudgetFormer的受限encoder提案](https://arxiv.org/html/2604.22583v1)恰有soft训练与hard推理的资格差：原文entropy项符号与探索/稀疏解释相反，最少一head与纯floor写法也冲突，未核实现前不照录完整recipe。全部训练head、selector、Q/K/V/O及FFN仍计费，按head比例估FLOPs/碳不代表真实时延、显存或能耗；测试兼作validation及任务退步也限制泛化。预算、mask、稀疏kernel或质量未验时，保留固定MHA/GQA与已验静态剪枝，不让head少或热图更集中签发全模型加速及语义必要性。<!-- source-family:SF-2026-ARXIV-2604-22583 -->

### 本人注

本人注：`SF-2025-ARXIV-2510-18358` — Locke，Daily2025-10-23补Oct22；exact-v1 §4.2–4.3/5.1–5.3必要，2+1+2=5，仅member/head轴与共享MLP差额深入。保共同基座不等独立ensemble、函数非严格保持、分类反退及训练/所有分支全费，不采普适noise定理或通用单模型时延；未核实现/复现。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## B3 LRP / WORLDVIEW-REPRESENTATION / Ch5

文件：`books/part-01-worldview/05-what-neural-networks-learn.md`。现有段已否定守恒即faithfulness；新稿用函数相同但计算括号不同的最小反例，补implementation invariance与指定LOO的第三义务。Ch4拥有学习/优化，Ch6拥有架构历史，不分叉归因owner。

### 完整前邻接

候选定位还可以改变反向传播的局部规则，而不重新定义部署模型的真实forward。先保原输入与反事实输入的activation差，再将普通局部梯度换成按层分配的relevance系数，以两者点积估计待核组件；例如把归一化分母或非线性系数在这次诊断反传中视为常量，可以改变信号分配，却不证明它就是模型真实Jacobian。[受限relevance-patching对照](https://arxiv.org/html/2508.21258v1#S4)支持这个候选筛选分支，不把相关性更高或relevance守恒认证为因果faithfulness：规则依赖架构，某些attention切片反退，模板配对与单token指标也不能代表自由生成。应同时保存原/patch人口、metric、局部规则、SAE重构残差与筛选阈值，再以真实activation替换、保留/移除候选和留出任务验收行为；这些独立验收不是换ρ就自动完成。规则适配、两次前向/一次反向、SAE/候选搜索和真正干预都付费，调用数少不等完整时延或成本更低；反事实、残差或近似失配时，保留普通AtP/IG与更窄精确patch，不由一张较清晰的电路图签发唯一内部算法。
<!-- source-family:SF-2025-ARXIV-2508-21258 -->

### 完整新增与 marker

守恒之外还要核解释是否依赖计算图的任意分解。对同一乘积函数`f=x1*x2*x3`，若每个乘法节点将relevance等分，`(x1*x2)*x3`与`x1*(x2*x3)`在输出24时会分别给出`(6,6,12)`和`(12,6,6)`；两者都守恒，却不满足函数等价实现下的归因不变性，将任一输入置零的LOO又都是24。[这一受限LRP反例](https://arxiv.org/html/2510.18810v1)因此把总量守恒、implementation invariance与指定干预的一致性拆成三项义务，不证明所有LRP规则都失败，也不把LOO选定的zero/mask基线当唯一语义因果真值。实际softmax Attention不能随意按线性乘积重括号；旁路softmax和bilinear传播同时变化的对照亦不唯一定位softmax原因。等价实现检查、解释与真实干预均付费；规则或基线敏感时，保留原函数、明确干预定义和更窄行为验证，不从守恒热图宣布唯一机制。

<!-- source-family:SF-2025-ARXIV-2510-18810 -->

### 完整后邻接

Jacobian-adjusted lens 一类方法提供了一个具体例子：它不直接把中间 activation 投影到
最终词表，而是用该 activation 对后续 residual 的局部 Jacobian 近似 layer-to-output
影响，再配合 activation swap、ablation 或 modulation 检查候选方向是否被计算使用。
这个方法的重要性不在于给出又一种“可视化”，而在于把 readout 与 intervention 放进同一
实验链。其局部一阶近似、跨 context averaging、token-indexed representation 与模型范围
仍限制外推，因此它是证据阶梯的实例，不是模型内部知识的最终字典。

### 本人注

本人注：`SF-2025-ARXIV-2510-18810` — Locke，Daily2025-10-23补Oct22；reader R14首次必要§3.1–3.2/4.1复用，2+1+2=5，为守恒/函数等价不变性/指定干预三义务差额深入。保标量等分规则范围、softmax重括号不许可、CP-LRP联合旁路混杂及LOO基线非唯一因果；未核实现/复现。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。

## B4 CovMatch / TRAIN-DATA / Ch27

文件：`books/part-04-training-system/27-data.md`。已有joint embedding覆盖与各边缘数据分布，不等明确用跨协方差矩阵承载图文配对统计；新稿不移走Ch23模态表示定义，Ch26仍负责动作语义，Ch28接实际预训。

### 完整前邻接

这条路线用更小训练集换取更高的 expert-training、embedding 选择和跨模态校验成本。现有结果绑定作者使用的表示空间、数据集、IPC/trajectory baseline 与 expert pool；joint-space 距离可能遗漏细粒度视觉证据或文本歧义，也不能证明规模扩大后成本仍占优。几何覆盖与 downstream slice 不一致时，应回退原始 data mixture、分模态校验和可重放的 trajectory matching，而不是把 embedding proximity 当成语义充分性的证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-23482:end -->

### 完整新增与 marker

配对压缩还可显式保留两模态之间的二阶统计，而不只分别匹配各自feature：在冻结encoder、仅优化线性projection的受限内层，可把目标联系到图文cross-covariance；实际合成时用矩阵距离约束真实与合成的跨协方差，再加各模态feature matching，避免只匹配跨关系而丢掉边缘支持。[CovMatch的有限检索对照](https://arxiv.org/html/2510.18583v1)支持这条统计选择，不把局部线性推导当真实非线性InfoNCE全局最优，也不让相同二阶矩认证逐pair语义或高阶依赖。真实数据更新encoder还会改变统计坐标，须绑定两encoder、配对人口和合成版本；旧基线冻结文本而新法可训练的差额也不能全归一个loss。全真实特征提取、online更新、合成优化及下游双encoder训练均计费；统计、尾部语义或净预算失配时，保留真实pair、原mixture与独立检索验收，不由较少pair宣布无损数据蒸馏。

<!-- source-family:SF-2025-ARXIV-2510-18583 -->

### 完整后邻接

若下游只消费图文配对数据，压缩也可以发生在生成器的制备链，而不匹配一份学生模型的参数轨迹：适配图像生成器时同时鼓励图文相关和图间多样性，用原caption采图，再让另一模型描述生成图，形成交给独立检索模型训练的pair。[EDGE的有限对照](https://arxiv.org/html/2509.15472v1)支持这种producer–consumer分工，但同一图配更多caption会在固定pair预算下减少不同图像，更多配对不等于更多独立视觉观测；批内语义重复还可能成为假负例，原mask与目标shape未闭的部分不能补成已核训练recipe。相关性、图像覆盖、caption事实与下游检索质量应分别验收，500-pair的一些结果弱于已有压缩法，更多配对/单个loss也有退步，不授全指标最优。预训生成器/编码器、原语料与caption、适配目标、实际图像/pair成员和每个下游recipe须共同留在lineage；制备、采样、后caption、全部检索训练及真实持出评价均付费，局部采样或训练GPU时数不代表全成本。覆盖、caption支持或质量/预算失配时，保留真实pair、原mixture、简单采样与分模态核验，不让生成语义取得事实授权。

### 本人注

本人注：`SF-2025-ARXIV-2510-18583` — Locke，Daily2025-10-23补Oct22；exact-v1 §3.1–3.2/4.1–4.3必要，2+1+2=5，跨协方差/边缘feature两约束差额深入。保局部线性内层非完整InfoNCE最优、online encoder统计坐标、冻结文本基线混杂和真实/合成/下游全费；未核实现/复现，不采通用无损。整体PRE/SAVE/全自读/sole actualPOST仅本日实际层。
