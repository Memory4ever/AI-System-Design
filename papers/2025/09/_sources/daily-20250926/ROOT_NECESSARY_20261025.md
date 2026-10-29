# Sep26：已准入候选的有限必要审阅

root明确接受作者17两项尚未开始的必要首域后执行；14/17已成日期/准入/分数复用，不第三。只交有限证据，不预Books owner、整合或日报完成。原件均exact-v1 URL、HTTP200/exit0，实际请求/UTC/字节/SHA保各同名 `.request.json`，无在途。

## 2509.19592v1 Frame-Stacked Local Transformers

[精确v1](https://arxiv.org/html/2509.19592v1)，`ROOT_CORE_2509_19592_20261025.raw`，107334B/SHA256 `bdeafe8c748a7d3bfd94aa02a88499ea2823a7e94cd779175b5b8d1e130a4509`，2026-10-25T04:57:18.186699+00:00至04:57:18.826188+00:00。root实际完整读§2–4、F1说明/F2全部table与caption/评测协议；未核曲线像素、代码/合成音频、主观人评或复现。未追读Koel/NanoCodec原论文，不补其本篇未给的超参。

**具体机制：** codec给 `[T,N]` 离散声学码，N=8、21.5frames/s的NanoCodec；同帧各codebook并非必独立，RVQ本身依赖前层残差，FSQ训练也未强制独立。主encoder-decoder按时间帧自回归；local transformer消费该帧主hidden，再按codebook因果AR，或从mask出发以非因果attention做P轮逐步unmask。一次unmask多个code时同轮关系未条件化，故MaskGIT是不同近似joint factorization，不是把原AR无损并行执行；P可小于N，不意味着计算费为零。

Frame stacking让主decoder一步产生S帧条件，LT处理S×N个code，按frame index/codebook使用分开的embedding表、与主decoder共享，主输入对frame/codebook平均。这需要按stacked接口训练模型，不是任意已训TTS上改一个采样开关；也不需要重新训练低framerate codec。主网络更少长历史/cross-text steps，工作转到短local路径。§2.4又称LT长度至多N+1，与其S×N描述在S>1时不齐；保接口歧义，不补完整tensor recipe或宣所有stack都只有9个LT位置。

**直接控制与反侧：** baseline主decoder16层；LT模型主12+local4，总层数16，各width768/12heads，同18k小时、220k AdamW steps，stack1/2/4；同层数不自动同参数/FLOPs，220k步也不等所有版本每步有效frames/tokens或全部训练费匹配。CFG/top-k/temp借Koel设置，本文必要域不含具体数，写未披露不私补；MaskGIT固定3步/purity选择。LibriTTS seen/unseen各180utterances，WER为Parakeet ASR、SSIM为TitaNet speaker-cosine（不是图像结构相似度）、UTMOSv2为神经MOS估计非听众人评；FD在codec32维frames上比较分布，不证明跨帧顺序、长语音一致或全部感知等价。表报95%CI，区间重叠不等效性证明；未给训练复跑seed/独立训练不确定性。

Stack1 LT在speaker/MOS/FD上改善但WER点估计略差；stack2 AR/MaskGIT作者相对baseline约2.1x/3.1x，stack4约2.9x/5.5x，同时unseen speaker SSIM由baseline .765降至AR .642或MaskGIT .624，MaskGIT MOS3.57→3.41。WER区间重叠不能抵消speaker/自然度反退；FD仍好也不证明所有质量维度保留。作者猜3步不足采32codes，未实证增加P已修复，不能写成已解决。默认parallel stacking反退与LT改善是真实对照，不由此声称每种codec/语言/任务都需该LT。

测速度的baseline为公平总层数加到16层；脚注明确若baseline仅12层会约快14%，所报相对倍数将降低。本文未披露实际测速hardware、precision、batch/concurrency、具体时延分解、流式首包与音频实时SLO，不补“任意GPU/全部E2E”。全部主模型/LT训练、codec编解码、local AR或3轮、CFG与采样/评测开销都计费；stack增大只是移动历史路径到local路径。**可支持的长期命题**是时间帧推进与同帧code依赖可分层，stack/迭代数在不同质量轴与执行费之间做选择；不是消除依赖或AR错误。未知说话人/质量不合时用较低S/AR LT或原parallel路径；提高迭代只是待验分支。当前owner由writer实际比较，不预NC/I。

## 2509.19836v1 BurstEngine

[精确v1](https://arxiv.org/html/2509.19836v1)，`ROOT_CORE_2509_19836_20261025.raw`，343894B/SHA256 `d47a36005fa9d15828b4db571dd28900f97ef5a167154cb879a6f8f1cef366b2`，2026-10-25T04:57:14.897206+00:00至04:57:18.105701+00:00。实际完整读§2.2、§3.1–3.4/Eq4–14/Alg1–3、§4.1–4.5/T1–5与直接F3–14 caption/作者解释；MathML alttext逐式读。未看像素/实现或运行，未取得训练质量/梯度回归验证。以下局部数学核验只限定打印解释，不自动判真实实现错误，也不私修整套recipe。

### 通信对象、拓扑与保留状态

Q/K/V沿序列切为各 `[N/G,d]`。前向Q驻留、K/V绕环，用online LSE合并局部attention，不持完整N²概率；这仍需准确mask、scale和全行归一。后向替换在环中移动的对象：固定K/V及各自梯度，把Q/dQ/dO与每行两个标量D/LSE绕环；减少一组宽向量搬运。作者简化计数由4Nd到3Nd+2N，约25%只限大d的**后向payload**，不是整轮训练/链路时间25%；加上前向2Nd，比例不同，真实G-1跳、数据类型、GQA非等宽、latency和通信实现也须另算。不是改变梯度目标或把所有rank都机械装入一个global ring。

节点内NVLink/节点间IB分层ring、独立inter/intra/compute三buffer配合多stream；activation可直接重叠，gradient须先warmup算出再发送，不能在生产依赖尚未满足时提前消费。buffer轮换/复用寿命、等待与各NIC映射是条件，“almost fully overlap”不等任意小tile/不同拓扑零通信；buffer与launch、warmup/drain都付费。FSDP的额外流量会与context ring争用，单attention kernel收益不能直接推全训练倍率。

**打印Eq7/8与Alg2的关键区别：** Alg2的D是 `rowsum(dO⊙O)` 行标量，足以支持上述payload设计；prose/Eq7/8却把它写成完整 `O dO^T` 再与P矩阵乘，混入跨query行，不是一般row-softmax Jacobian。root独立有理数例：两query、d=1、QK全0，P每行(.5,.5)，V=(1,2)、O=(1.5,1.5)、dO=(1,0)。逐行正确dS为第一行(-.25,.25)、第二行(0,0)；打印完整矩阵乘式给第二行(-.75,-.75)。因此不能以Eq7/8“证明”通用准确梯度；有限采用只据清楚的Alg2逐行统计/对象交接，具体实现与梯度对照仍未验证，不把本例扩成整篇不可用或所有benchmark作废。

### 重算和head/loss融合不能只认标签

Sequence-selective checkpoint按因果序列不同位置重算负担，存较贵后段、重算前段；它减白名单内attention-output保留而增加重算，不取消FlashAttention backward、其余activation或FSDP状态。mask/load也改变这份收益。LM head的 `[N,V]` logits在大词表下可主导memory；按sequence和vocab tiles流式做CE有明确的存储动机，但本文“前后融合且不重算”的**完整可执行桥未闭**：

- Alg3在第一个vocab loop反复覆盖Logits_ij，第二个loop在得完整LSE后又使用每个旧ij；若既不保存全所需块也不重算，旧块如何存在没有交代。可实现的额外tile存储或重新计算是不同费用，不能替作者默补。
- 所印CE梯度用P+E（E是真标签one-hot），通常应核对符号。最小N1/V2、H=1、W=0、标签1时，CE对W梯度为(-.5,.5)，打印加号给(1.5,.5)，二者不等；不能签其loss/gradient等价。
- W_j已定义 `[B_v,d]`，dH行却乘W_j^T，另E写N维，和所述tile shape不齐。upstream loss normalization/gradient消费也没有由打印伪码完整给定。不据此猜代码行为，亦不把它当验证过的融合算子。

上述只隔离无重算/精确梯度配方及其因果保证；序列级减少巨大logits驻留的方向、作者测量和可单独支持的通信对象仍保留。§2.2的 `Softmax(M⊙S)` 也不能按普通0/1 mask照抄，因为被mask处仍有exp(0)质量；必须保持实际合法可见性，不私补为已核实现。稀疏causal/zigzag/striped按真实位置重排任务，block sparse要求blocksize为G倍数，不是任何mask都自动均衡/无idle；更稀疏已改变可见图，不能当原dense模型无损加速。

### 实验人口、直接反侧和全部费

- 32/64 A800-SXM4-80GB，8GPU/node、NVLink400GB/s、每node8个200Gb/s IB NIC；7B(32层/32heads/d4096/V32K)、14B(40层/40heads/d5120/V120K)。BMTrain FSDP、NCCL multi-stream、GCP/部分optimizer offload组合。attention-only §4.3写32A100而总setup A800，保分域差额不擅统一；precision、global/microbatch、优化目标/训练token预算、完整kernel版本、重复运行/CI与质量回归在必要域未披露。
- E2E长序列：32A800下7B2M/14B1M，64卡7B4M/14B2M；作者对LoongTrain-USP约1.19x/1.15x。基线是否具FSDP/offload、头数能否被设备数整除均不一致：Megatron-CP OOM不证明相同状态管理也一定OOM，40heads对32卡Ulysses不可切不等其所有配置不可用；不得全因果归新attention。峰allocated memory不是所有进程/host/网络/总成本。
- T2 sequential ablation：fusion后TGS95.06→94.81略退、memory48.97→41.45；sequence checkpoint后TGS108.82/memory45.93，selective++为117.83/53.91。这是吞吐与memory选择，不是新项单调同时更快更省。94.81→108.82的同时memory上升，更不能把每个相对节省比例连乘。无优化83.79/48.47到108.82/45.93按表只约5.24%总memory减少，与正文“至少15%”口径未闭；不修原表或编隐藏baseline。
- T3无负载优化mask/full工作量对causal/SWA32K改变有效工作与可见性，1.72x/3.68x不是同dense模型质量等价。T4/T5设备与总长度同比增加、MFU较稳定是**弱扩展**，每GPU TGS下降，不能写fixed-length强扩展线性加速。node内开启offload/node间关闭，也不合并为一条同配置扩展律。
- 真实FSDP/DP与context流量、三buffers、head临时量或重算、锚点、optimizer/offload、稀疏重排、kernel配置/验证及数据训练全费均需结算。长序列可跑不等模型会用，未给loss/任务质量/梯度一致的必要对照，不能授exactness、学习收益、任意scale或服务SLO。支持/质量/拓扑或净费不合时，普通Ring/DoubleRing、较简单checkpoint和已核正确的head/loss分块仍是合理退路。

**可支持的有限命题：** 分布式反传可以在不改变梯度归属的前提下重选驻留/传输对象，再用拓扑和生产依赖安排重叠；activation/logits的不同寿命应分别预算。本文打印归一/梯度/fused无重算解释不能作为完整正确性证明，正侧和争议分别保留。writer应依实际owner内容决定具体新增/已有覆盖/必要争议，勿降6或用“已覆盖”删掉这些反侧；不预整篇I/D。

## 实际交接

root首包→Aristotle实际回上述必要原域作为唯一另一角色采用，准备层闭合后Einstein只角色/采用范围复用，不第三相同Methods。Books owner与原三项PRE属后续新层，必须实际比较；共享新位仍先协调。材料可支持命题与打印冲突严格分开，未用像素/代码不是普通未读债或外部终态，不因包写出就计Evidence/Books或日级完成。

## 第二批首域：19702与20020

作者31明确两项Methods尚未开始且无GET在途，root明确接受后首次准备。作者31/Einstein26已成的精确AB、日期和首次5/6复用；不是再做日期或扩大候选。两原请求已实际结束，均HTTP200/exit0，原件及同名`.request.json`保留。后由writer唯一另一角色实际消费必要原域；reader只复用真实采用范围，不第三相同Methods。以下没有预先决定Books、整篇真伪或日完成。

### 2509.19702v1：受约束线性Transformer与提取的迭代算法分开

[精确v1](https://arxiv.org/html/2509.19702v1)，`ROOT_CORE_2509_19702_20261025.raw`，754816B/SHA256 `05cfacb7549fccf922ac4d879b10b1f750628796409f2d51ae6ef3698078ef60`；实际UTC2026-10-25T06:11:05.724517～06:11:17.840952。实际完整读§3–6、A.1–A.5、B.1–B.4、C、D.1–D.3、E.1–E.2，MathML逐式/关键图caption；Alg1为图片，其像素未读，不声称已核图中伪码，必要更新直接以B.3/E.1/E.2可读公式为依据。未读实现/权重、其余引用论文、曲线像素或复现实验。

**问题、机制与对象。** 输入是合成低秩矩阵的三个可见block与置零的D，固定可见性mask、无softmax的attention-only residual层，以D的MSE训练；不是自然语言next-token模型。默认20×20矩阵、rank10、各向异性Gaussian、半数加variance.01噪声；Adam lr.001/batch1024/20k步约2048万独立任务，每次重采样，10训练seed。所学权重经阈值稀疏、两/三值聚类与乘积解释，近block-diagonal结构才给出连续调节A/B条件数并累积C/D更新的算法；本身不是参数在ICL时再训练，也不由一张权重图证明所有Transformer等价求解器。T1比较的是抽取算法与网络逐层activation的平均平方Frobenius差，非严格相等；十seed和独立样本只是本文人口。

三种架构分别训练：完整可见、低rank投影、按machine限制Q/K的multihead。后者projection通信原本可全连，出现只交换共享C/D更新的稀疏结构是观察；不是已运行真实多机NCCL系统。单轮传O((d+d')n')浮点数，不能写A.4的O(|D|)bits，也不等通信latency/E2E速度。低rank sketch改变单层费与所需轮数，不等任意任务可无损降维；S4给A S而5.3写S^T A，非方阵一般不能直接互换；主/附录维度与代价在n=d时被掩盖。保有限代数方向，不补一份全shape可执行配方。

**抽取、证明和经验参数不能混签。** 观测权重按batch最大谱估计归一，文称eta约1/gamma约1.9；正式Theorem1/E.1用每个iterate的精确谱范数、eta=1/3/gamma=1。A.2实际loss spike来自未见大谱outlier；E.1末也明说power iteration只线性精度、严格全费会破二阶率，宽松误差理论留待后续。B.4却写eta1/gamma3并称同Theorem1，A.5有自指`alpha1 alpha3≈1.92 alpha1 alpha3`，B.3的plus/residual与E.1分块符号也须核，不把打印式连成已证网络全域二阶收敛。E.1对明确写出的迭代可保局部谱收缩/条件数改善的论证；证明对象、步长、rank支持、Nyström目标与真实任务误差分别验。

主文的diversity定义是`alpha=lambda_min((1/M)sum P_mu)`，但“子空间正交则alpha=1”不由此成立。root以有理数直接算M2/d2，P1=diag(1,0)、P2=diag(0,1)，平均I/2，alpha=.5而condition number1；相反所有P=I时alpha1。因此不能用“alpha≈1表示正交”或inverse-alpha恒等于极限condition number转译设计。E.2给的上界/有共享top方向时的紧性与此处一般等式是不同主张；证明另需共同初始谱归一、无噪声一致W*、C在全局column span、有关支持上的正下界。未归一/机器gamma不同的情形作者留待后续。D.2用`min_mu`误差过阈就停所有worker，不能认证每台均已条件化；矩形/秩亏identity还需支持和尺度，不能照抄成通用freeze判据。只界定这些采用边界，不由此判实现必错或整篇没有机制价值。

**控制、反侧和全费。** §5主要评的是提取后的显式solver，在d=n240/或1920、合成数据、50次平均上与GD/CG/lstsq比较，不是训练网络在所有尺度的同预算泛化。主文torch.linalg.lstsq/QR与附录NumPy LAPACK命名不齐；CG在rank不足被省略、GD可加ridge，目标不完全一样。noise下早停可比GD、长迭代Nyström并不一定最稳；sketch小r可失去wall-clock优势，图8只称r≥n/4。21/16/7/5ms与“up to7x”也不宜混成固定总体倍率。hardware、dtype、并发/物理网络、全部训练/提取/谱估计/通信时间/独立CI未充分披露；epsilon1e-20未说明是何误差尺度，不能据此授浮点解精度。全部任务生成、网络训练、权重解释/稀疏聚类、每步矩阵乘与谱估计、message/同步、solver验证/失败重试均计费。数值稳定kappa>1e8与非线性扩展未测。支持的是**先固定任务与资源可见图，再用权重简化和逐层预测验证提出可解释算法，分别验证抽取保真/数学条件/净计算**；不授自然语言模型已发明通用算法或硬件加速。owner及是否已有覆盖仍由writer实际比较。

### 2509.20020v1：等价重写须保索引作用域和代数域

[精确v1](https://arxiv.org/html/2509.20020v1)，`ROOT_CORE_2509_20020_20261025.raw`，454672B/SHA256 `683aa54d98d1b81dfdf67ce3ecc7c41ed7f621df6b624981f3c1b4303a050303`；实际UTC2026-10-25T06:11:53.694704～06:11:56.358544。实际完整读§2–8全部定义、定理和证明、直接实例及F1caption；未核图像素、任何框架当前实现/测试或复现，不把此v1当所有library现行规范。当前HTML模板的Volume/publyear不替代已成公开日。

**机制。** tensor定义为有限multi-index到值的函数，不依赖dense array/layout。值域假定commutative semiring；每个label统一axis length、输出label必须来自输入、输出顺序显式，可重复输出label，空输出为scalar。语义按全局索引赋值，以固定输出位置为条件作有限sum-of-products；重复输出导致不在对角约束上的位置取0。本文`i->ii`可造对角阵，不能直接当NumPy/PyTorch/TensorFlow支持；与常用库另一区别是强制显式输出。operand交换必须连同其index string交换，不是AB=BA。求导须保不再显式出现的axis信息，可补ones，且结果可能需多个einsum的elementwise sum；不是任意semiring都有通常微积分。

**有限可支持规则与打印关联条件反例。** §6.1 Restricted nesting正确边界是内外共享label全部留在中间输出，且对应的内输出/外operand字符串一致；内层已求和丢弃而外层仍要用的label不能直接压平。独立局部整数核算：T1=[1]、T2=[[1,0]]、T3=[[0,1]]，I1=i/I2=ij/I3=ij，I=I4=I5=i。满足§5.3所印`σ(I)=σ(I4)∪σ(I5)`、每式shape合法；平式`i,ij,ij->i`为0，但先`i,ij->i`再与T3按`i,ij->i`得到1。打印Theorem5.3独立条件没有保跨边界j，不能宣布它自动满足6.1或当无条件任意括号重写。这里隔离该一般关联声明，不否定满足6.1的合法contraction path或sum-of-products语义。

§6.2把内外非共享label先alpha-rename，重复边界label通过连接分量/符号映射匹配，证明用delta-split→受限denest→delta-merge保持等式。可采用的是按实际边界相等约束形成的分量，不是随意把无关分量再合一；打印general声明“respects restrictions”不能外推为任何多对一映射。示例6.2首个式子自带operand/format-string笔误，不私补为某库可执行代码。§7.1 identity还要求label无重复，`ii->ii`只保对角；删ones须不引入新label，否则新自由求和会乘维度，delta/constant消除也须保必要axis/ones。只依可明确限定的语义和规则，不授整套打印无条件定理。

**取舍、费用和未证明内容。** ABv的contraction path可避免先做大矩阵AB，但语义可重写不等给出了最佳path；作者明确optimal contraction path NP-hard且不解决。没有新benchmark/hardware/dtype或大模型吞吐对照，不能用形式证明签实际加速、最小workspace或自动TP最优切分。实现还要付parse/shape校验、alpha-renaming/连通分量、path搜索、intermediate materialization/layout/通信、AD和数值回归的费用。有限精度也不是这里的精确semiring：root实际float例`(1e16 + -1e16)+1=1`而`1e16+(-1e16+1)=0`，所以代数等价不认证bitwise或误差预算；实际backend支持、overflow/NaN、舍入/累积顺序和gradient分别验。成立的长期命题是**在选择快的执行顺序前，先明确索引、作用域、重复label与代数条件，合法候选和成本选择分层**。是否改变现有owner解释由writer比较，不能只因新形式语言/缺marker而写书。

第二批准备已完成，无root在途。Aristotle按具名两个原域作为唯一另一角色实际采用后更新自己的canonical/报告；Einstein仅复用该真实采用角色，不第三原件。打印反例保留，不由“已有覆盖”或降分抹去；书写前仍需实际owner判断与独立复核。

## 作者50新增首必要：19480 OmniVLA

root明确接受未开始的有限必要域，46→Einstein39日门/准入及原2+1+2=5沿用。[精确v1](https://arxiv.org/html/2509.19480v1)原件 `ROOT_NECESSARY_19480_HTMLv1_20261025.raw` / request，2026-10-25T08:00:55～08:00:56Z真实200/exit0，185789B，SHA256 `540a7b13616d2b204c42ec798e44ccd333731305a99e5228c8fe59582e964604`。实际完整读§III–VI、Appendix VI-A～E、TII–VI和直接图caption，另定点完整读S2.T1数据表；未全Related Work、图像素/视频、代码或机器人复现，不预任意机器人部署。

机制是把当前图像及可用目标模态（文字/2D pose/目标图像）投到共同token接口，独立随机选择可用目标并mask未选/缺失部分，让非配齐标签的数据也可混训；OpenVLA加并行线性action head输出chunk，edge另用50M ViNT式early fusion/5帧历史。它不是所有传感器天然共坐标、目标token天然相容或无需action适配：位姿目标由GPS相对变换，远图像目标依赖预先录制topological memory/节点定位，实际机器人API仍接线/角速度。动作表示、归一/时域、平台运动学与输入可见信息是训练及执行契约，不因统一token免除它们。

BDD-V汽车与小机器人速度/频率不同，论文重新训练MBRA产生可行合成轨迹，线速0～.5m/s、角速±1rad/s并限两轴运动学；车内dashboard会误触视觉碰撞，故其碰撞损失只施于GNM。此为有代价且有支持域的重标注，不是保真实汽车动作或证明真实动力学安全。§III主目标是监督模仿，另LeLaN物体接近与平滑项；不是RL探索或形式安全filter。Appendix E将p_obj与末action相减的单位/执行解释不足以独立补全所有robot adapter配方。

T1四组小时62/128.7/700/8680合9570.7，正文约9500是汇总口径，非每个模态各有9500小时配齐数据；BDD-V占大头。实际4:1:1:1按LeLaN/GNM/Frodo/BDD采样不等按小时比例，合成标签噪声与各数据支持不同。OpenVLA用8H100、perGPU7×accum4=global224，LoRA约5%；梯度累计不补物理batch相同的数值轨迹。总训练token/step、全部precision/独立seedCI/总GPUh和端到端资源费未充分披露，其余部分配置转引原实现不算本轮已核。

真实测试有语言40环境/目标5–30m、障碍子集17；图像近目标≤3m及8环境topological memory；pose25–100m、7环境×3次并受GPS抖动。图II平台为远程RTX4090推理经网络发速度，不能叫edge本地低延迟已验。TII图像1.00与MBRA-image持平，复杂语言成功.65不等无失败；TIV文字+pose同时输入时SR.80、行为.60是两个指标，不能由到达成功代语言遵循。edge行为.10与大模型不同，不把50M效率和7.5B质量合为同一工作点。TIII固定edge架构但数据来源/信息量随模态改变，不独立识别dropout因果；大VLA/小VLA预训练和容量都不同。NaVILA提示接口不匹配的零分不是算法普遍无效。

新卫星模态通过冻结多数参数/换encoder再训练，另新环境收1.2小时数据；不是未训练模态zero-shot理解。VizBot/Go1只具名演示，完整跨本体SR/动力学分布与安全统计未披露。训练数据汇集/重标注、目标模态编码与dropout、LoRA/全训、图记忆录制/定位、网络控制及各平台独立质量/安全回归都付费。可保长期接口为**缺失模态的训练mask与目标条件组合必须连同动作归一/重标注和执行适配共同设计**，不能从多模态成功率推出任意传感器或机器人通用控制；支持域或成本不足时保专业导航、明确adapter和受控目标方式。当前owner/具体已有覆盖仍writer新层，不预I。

## 作者50新增首必要：19555 AnySafe

[精确v1](https://arxiv.org/html/2509.19555v1)原件 `ROOT_NECESSARY_19555_HTMLv1_20261025.raw` / request，2026-10-25T08:00:56～08:00:58Z真实200/exit0，323214B，SHA256 `00a1d8a0783ae1fd34f0eaff05a18ae76b0f2c1a6b6312b004fb3eae5f281f7b`。实际完整读§III–VII、Appendix VIII-A/B/C及Theorem1证明、T I–VII和直接caption；未全Related Work、图像素、源码/机器人复现。39原6/day有效复用；安全受影响有限深入，不遍历无关附件。

原固定failure classifier换为constraint-image条件化接口：world encoder产生原latent，另有标签训练failure projector，投影空间cosine的负值定义相似失败margin；条件化value/备用policy仍消费原latent与constraint，不能把仅保失败位置特征的投影latent当完整动力学state。TII将两者都投影时safe-rate .504，对原latent .924，说明此分责真实重要，不是“embedding越对齐所有下游越好”。runtime预测任务动作的下一latent，value不过阈值则备用policy介入；这是一条额外filter，不更改任意原任务模型即可保证物理安全。

CP式6只校准**同类正图像对的failure-similarity召回**。有限样本保证依赖交换性/校准人口与正类定义；反复从同轨迹/图像采对、在线policy改变访问人口或新constraint并不自动保这些条件。它不是每个固定constraint的条件保证、value函数误差界、真实物理失败概率或整条轨迹零失败。分位数第ceil((1-alpha)(N+1))若超N还须扩展分位数/保守约定，不能任意截到最大有限分数冒原保证。正文明确把此δ直接施于近似value，假设solver误差可忽略，却没有给误差上界；world model、encoder、DDPG、动作/网络延迟误差同样未被CP删除。

Appendix C的有限Theorem1是**常数平移的等价性**：在有界margin、gamma<1和合法归一转移期望/动作最大值条件下，backup是gamma-contraction，T_delta(V-delta)=TV-delta，故精确固定点V_delta=V-delta；这支持后置阈值与重新平移margin求值的一致，不证明其真实unsafe set已校准或近似solver精确。另须收窄§III的“V非负即存在永不失败动作”：discounted打印backup对短时正margin会有正偏。例如无控制确定链A→B→C→C，l(A)=l(B)=1、l(C)=-.1、gamma=.5，则V(C)=-.1、V(B)=.45、V(A)=.725；A的下一value也为正，但所有轨迹都到失败C。此为直接代入的有限模型反侧，不是运行作者实现；常数平移定理仍成立，而不能据有限discount符号直接授任意长度viability。随机动力学处又是期望而非全路径最坏情形，更不能无条件升级sure safety。

Dubins仿真4k随机轨迹、3k校准图、groundtruth位置标注、alpha.005；50constraint监控/250safe初态回放等不同评价对象须分清。AnySafe recall .966、safe-rate .924，均非.995全链保证；fixed基线只测中央区域与Any多constraint也不是完全同任务人口。TIII距离半径/平方距离阈值口径不一致，最小距离还是轨迹平均，不能当每一步均越界概率上界。图像空间/视角变化、未来不可见风险和未出现constraint都未由同类校准解决。

真实Franka3扫物，仅末端x/y/yaw、DINO-WM/DINOv2、1300轨迹（300teleop+1000random）、failure projector另300标注轨迹/4000校准图、alpha.1，30动作回放及保守性15回放组；任务policy是人遥操作/回放而非任意LLM policy。论文§VI的244图像与TableV224、projector维数512与TableVII32/patch norm描述等配置差额不私补成可运行recipe。硬件曲线caption/正文对距离above/below措辞有差，不从<2%文字补一条统一物理失败率；像素未核，独立任务/固定filter配平与全seedCI/实时控制延迟/安全介入率总费未足。§VII明确只假设world训练所见图像约束，unseen约束泛化仍开放，不写“任何失败图片即安全”。

全部真实交互与失败标签、projector/encoder/world训练、64万步DDPG想象/回放、图像对校准、runtime预测/value/备用动作、网络控制和独立物理安全/任务回归计费。可保的是**失败语义度量、动态可恢复性与动作介入三者分责，运行时约束变化也需特定表示及独立验收**；强统计安全/任意约束/近似误差可忽略不采。数据支持、动力学或时延不合时应限制运行域、保可核硬约束/安全控制及人审，不由latent相似度或Theorem1平移公式签动作许可。

两首必要请求已真实结束；交Aristotle唯一另一角色回有限原域实际采用及反侧，Einstein随后角色复用，不第三相同Methods/GET。原分/日期不由此改变，当前具体owner/Books仍writer新层；后若拟采用命题确实扩出此域才具名补读，不把未读附件全转待办或预整日验收。

## 第四批首域：Q-Palette 与 graph circuit tracing

root明确接受writer79/Einstein71已准入的20214、20336未开始标准必要域，原6/5分及日期层不重做。以下首次有限准备交Aristotle唯一另一角色actual采用；Einstein随后仅角色复用，不第三Methods。两exact-v1请求已结束200/exit0，无root网络或命令在途，当前owner/Books仍writer责任，不因本包准备成而预授I/NC/DAY。

### 2509.20214v1：表示位预算与实际执行计划应共同选择

[精确v1](https://arxiv.org/html/2509.20214v1)，`ROOT_NECESSARY_20214_HTMLv1_20261025.raw`及同名request；UTC2026-10-25T10:48:02.836811～10:48:06.559848，809766B，SHA256 `3467f97a76ce3632e5b99ebb16e5c3565cf476291dbd2f719a5fc528dd563ce8`。root实际完整读S2–5/T1–4/E1–4/Theorem3.1、A/B完整证明和gap分析/T5–6、D实现说明/T7、E、G.1/G.2.2–4/T8–10与H限制，直接F2–4caption已读。未C全部quantizer/Viterbi细节、G.2.1全部额外模型表、F图设全项/图像素、代码/真实GPU或复现；没有把当前仓库新增功能倒填v1。

**机制。** 单一bitwidth或只按量化误差选格式，可能不匹配实际解码/算子开销。论文在近Gaussian权重上提供NUQ、2D VQ、bitshift TCQ与half-TCQ，以有限码本和平均位宽组合细化选择；八个二维码字编码两个标量为3bit，即平均1.5bit/weight，不是每个独立标量有半个物理bit。TCQ滑窗复用bits，half-TCQ把不同行分区用相邻格式并在同kernel解码；尾部/scale/码本/对齐等元数据不能被平均位数自动豁免。Input-only rotation、per-output scale及同输入q/k/v或gate/up共享rotation，将作者每block在线旋转14→4；旋转/补偿的shape、精度和兼容输入必须保持，不是任意层都可共享。低位压缩后仍在register解码、shared memory复用activation、映射mma fragments或half2 FMA，既非所有fractional格式被GPU原生GEMM直接执行，也非只要码更短就更快。

E1以逐层敏感度加权归一量化误差近似全模型loss。理想连续Gaussian rate-distortion、非负敏感度、给定位预算和下限eta时，KKT解类似受下限约束的water-filling，依赖a_l/该层参数数目；只在此surrogate内最优，未证明任意有限权重、下游准确率、端到端latency或QAT最优。a_l=0有log/非唯一边界，应明确处理，不照抄作任意输入完整求解器。Gaussianized不等精确iidGaussian，32个4096²随机Gaussian低方差也不证明所有真实旋转权重达率失真界。B把gap拆为distortion与allocation的**总和**可在理想条件下非负，不是每层allocation括号都非负：两同权同大小层理想各2bit，实际3/1bit同总预算，其中3bit层的2^-6−2^-4为负；这是代数边界，不否定合计gap或实测。

有限候选以MCKP/ILP选(layer,quantizer)，fusion-aware改选(fusible-group,quantizer)，C1精确覆盖每层一次，C2加总profiled cost。只把同输入的qkv、up/gate等合法拼接；扩大可行域可以改善该估计问题，但不同量化器或fusion会改变真实kernel/旋转/误差。加总latency含从若干整模型torch.compile测时反推、平均分摊的公共overhead，并随fusion修bias，不是任意并发/shape/通信下的可加定律。SCIP60s上限也不授任何规模已获全局最优证明。M是量化权重预算，不能替总HBM中的KV、workspace、LUT/scale、allocator和reserve。

**条件与反侧。** 全部为无重训PTQ，主要Llama3.1/3.2、Llama2与Qwen2.5；WikiText2序列Llama2 4096/Llama3 8192，五zero-shot任务、lm_eval0.4.4。GPU为4090/3090、CUDA12.4，batch1/8；QTIP大batch用重复单batch kernel模拟，故其明显退速不等所有现代batched量化实现都如此。HIGGS结果从论文引用而非本机统一重跑，部分best-PPL配置码本非power-of-two，不能说全部baseline同runtime或同费用。T2 CC常在batch1较快、TC常在8较快，T7的3090差额不同；选择须绑定硬件/shape，不是Tensor Core越多必优。

T3 8B三位单TCQ PPL6.78优于QTIP6.81却accuracy66.0低66.9；四位3B MSQ accuracy63.2低单TCQ63.4，故PPL排序不等所有下游质量排序。T4 Llama2-13B三位accuracy67.0持平而非严格更优；FP16 13B在4090 OOM不能作同显存运行时速比。T8固定接近223–224tok/s时无fusion PPL20.33对fusion7.79、TC+CC7.69，是该可行域/目标下局部取舍；不是把更准归因fusion本身在相同位数/每层格式下不改误差。T9 actual/linearity PPL与accuracy次序不完全一致。G.2.4无IP、group64、一个8B的Gaussian proxy相近true distortion仅初步条件证据，不解除Gaussian理论前提或认证任意outlier数据。

**全费与未闭。** “data-free”不等不采数据/不用forward：E1生成128K自模型tokens，对每层16级噪声多次KL计算后拟合a_l；data-aware linearity用1M RedPajama，actual用256K及QTIP既有6144×4096 Hessian，均保制备身份。E1 n_li定义已含||W||，扰动式再乘一次||W||与后拟合n²的单位表述有歧义，不私补完整复现recipe。Sensitivity可跨预算复用但模型/层/目标漂移不能免费继承，H明确其一次性费用可能大。量化/codebook/rotation、profiling、SCIP、所有选择/校准、驻留、完整Prefill/Decode/质量回归全计。未充分披露完整I/O长度、并发、计时重复CI与生产SLO，不把局部decode吞吐签端到端净加速。Activation量化、QAT和INT8-only硬件适配为未验方向，不写已实现。

最小可支持命题是：**平均位数、量化误差与实际kernel/fusion是不同约束，按目标硬件/workload联合选表示和执行计划，再独立验质量与总资源。** 明确已验简单格式、小候选集及原FP16/普通PTQ仍是兼容或profile失配时退路；具体知识owner差额由writer实际比较，不为每个码本另添一节，原6不改。

### 2509.20336v1：已记图边与当前输入图应分开验证

[精确v1](https://arxiv.org/html/2509.20336v1)，`ROOT_NECESSARY_20336_HTMLv1_20261025.raw`及同名request；UTC2026-10-25T10:48:06.647209～10:48:07.569582，156686B，SHA256 `b3e178785b18e43991c055091cb432bf748b1b0ff5d5cb744063202d894a4a61`。root实际读S1–2/S4、A/B、C全部文字caption/T3及D限制，含T1–2设置；未相关工作全史、图像素、transcoder代码/权重、被引框架全部假设或复现。原5分保持。

随机生成一张backbone graph，再采其子图形成路径、带属性路径和子结构任务；5层GPT2变体用RoPE、通常hidden96，另比较96/192，单RTX A6000。训练后拟合跨层transcoders并合成attribution graph，在token/edge阈值及选取比例下观察信息汇合，名为token merging。它不是推理runtime删除token、KV共享或已经找到了唯一真实算法；transcoder是学习得到的替代读出，论文没有给足原模型/替代模型faithfulness、跨seed稳定性或独立patch/ablation证据以证明这些图就是全部因果机制。局部图解释应保为诊断假说，不把“core/unified”直接升级全部LLM推理定律。

N_select/N_pred的S_E以trace选出的token为条件分母，更像所选证据命中率，不是所有真正必要边的召回或内部机制完备度。T3 selected ratio.9时S_E.94，只支持该attributed graph观测；三类task的阈值/架构/graph尺寸各有定制，不把trace好看跨任务平均成统一可靠性。层3汇合较多/密图较深为本设置观察，不证明实际神经元存一条独立边、层数与任务复杂度普遍映射。Table2还区分Transformer hidden与transcoder hidden192，不能把每个192都读成backbone容量；正文96/192比较与具体trace配置须保身份，未配齐训练参数/优化预算便不唯一归宽度因果。

更直接的反侧在B：Local Accuracy要求输出边在当前给定子图内，Exist Accuracy只要求在训练backbone中，Global Accuracy只给起止节点、让模型调用已记backbone。小10节点图的Global较早高、Local随后上升；50节点时Exist可高于Local，说明历史图的合法边可能在当前上下文不存在。3–5hop监督后产生>10hop可行路径不等仍遵守最短路径目标，也不证明跨新backbone泛化或最优搜索。单node ID能读出近邻是该训练图上的行为，不能因此说模型在参数空间显式建了可逐条查阅的数据库。Train/test子图共享母图，任务held-out不等图/node-heldout；这在既定记忆实验中不自动叫泄漏，但须避免泛化外推。

Table2的basic accuracy .99/.96/.94/.92只有限四设置，没有完整sample/seedCI/训练token与调参预算说明；F4/5/8/10caption和正文qualitative不替图像素精确数值，本文不声称从未读曲线复算了precision/recall。数据/图制备、原模型训练、各层transcoder、稀疏化/阈值/trace及heldout/干预验证均计费，低维小模型不授大LLM同机制或低线上开销。若graph identity、输入约束或trace fidelity不足，应保当前显式图/可执行路径检查、独立干预与Unknown，不由trace或已有边记忆批准任务解。

最小可支持命题是：**回答可以同时借当前输入结构与参数里已学的图规律，评价必须分别核当前子图合法、母图存在及无上下文记忆；可视化只是需验证的解释。** 是否已有具体正文承载由writer当前owner比较，不能因主题相似一概NC，也不为“token merging”新名另建优化章节。首包不自签全部机制/Books或日完成。

## 第五批首域：Video models 的任务读出与选择预算

writer97明确20328首次必要未开始/无CORE或在途，root本轮明确接受后首备；79→Einstein71精确v1准入、原2+1+2=5及既成日期层不重做。交Aristotle唯一另一角色回下列有限原域actual采用，Einstein后只角色/范围复用，不第三Methods或全部演示。当前owner与Books决定仍writer新层，不预I/NC/DAY。

[2509.20328v1](https://arxiv.org/html/2509.20328v1)，`ROOT_NECESSARY_20328_HTMLv1_20261025.raw`/同名request，UTC2026-10-25T12:07:27.433899～12:07:35.418292，HTTP200/exit0、562880B，SHA256 `c039f478a7bdbdf712d83ca892e7cf0db8c17a00d6cce330102baa89991f23f2`。root实际完整读S2–5、B全部七项定量任务/评价与采样/T1、C提示研究/T2、D失败caption；未A全部62定性任务、图像素/音视频、代码/API真实调用或复现。不把current-v2补成历史v1，日期限定沿root第四日期包/作者78/独核71有效层。

**被测对象。** Methods只prompt公开VertexAI：输入首帧+指令，生成16:9/720p/24FPS/8s视频。Veo3为veo-3.0-generate-preview；Veo2主文ID veo-2.0-generate-001而B各任务写veo-2.0-generate-preview-001，保呈现差额不补统一revision。API含LLM prompt rewriter，作者明确按重写器+视频生成器的黑盒系统评价，Sudoku等可能主要来自LLM；独立Gemini2.5Pro从图解maze/symmetry较弱，不能代“关闭或固定重写器”的同系统消融，更不能唯一归视频主干因果。本文未针对这些任务自行微调，可称该协议zero-shot；未公开完整预训数据/目标，不由此认证任务、图片或相近监督绝未出现。

**候选、帧、阈值与最终答案分责。** 定性62任务各12样本/744video、成功由作者判，是所选示例条件下的行为；n>0支持有样本能做，不是全部任务/seed稳定或人口发生率。定量七类任务明确best frame与last frame，前者从生成帧中按真实目标指标取最佳、后者预定最后帧；进一步best-of-k又按目标挑尝试。192帧的一段视频及最多10段，不等普通一次可交付解。能在采样集合中挑到好结果不证明线上有合格selector/stop signal，生成继续改坏也使末帧退化；可视完成点仍需独立检查。OIS/mIoU等连续分数上的best-of-k不要读成统一的二元成功概率。更多尝试的oracle max会单调，不能把这一数学性质当通用推理scaling证据；B7实际多数选择反而可随k下降。

**逐项人口与直接限制。** Edge用BIPEDv2全部50test；先NMS/16阈值/细化，允许图对角线.75%约11pixel位移后求映射，OIS是每图最佳F1阈值，再择帧/尝试。Veo3所述.77与专模.90是该有oracle选择的测量；更细轮廓可能是GT未标，也可能是新增错误，不能凭一幅解释判全部false positive都正确。Segmentation只LVIS随机50张、1–3个且各至少5000pixel的大对象，颜色histogram找mask，再按每个GT选最高IoU、背景不计均值；未明确一对一匹配的余mask/错分罚，不能当完整实例AP/全部object recall。green与white提示.74/.66及NanoBanana.73为best-frame/pass10局部值，不能说端到端取代SAM或所有图像模型。

Object extraction用NanoBanana先造再人筛54图、每count6，最后帧灰度threshold200/连通分量计数；计数对不证明每个原对象身份/纹理保留，无重叠先验与chance1/9改变人口。Editing30Emu-edit随机样本、3human分别判fidelity与无额外改变precision，B说每图造2样本取第1人评；T1计60更像评价样本而非全部生成量，不能据表免除被弃生成。Maze矩形每size50、irregular10手工图翻转/旋转为40，不是40独立新布局；framewise checker须核墙穿越/goal移动，而Nano图解允许小断点、Gemini坐标连续性是不同输出协议/预算。5x5 pass10 78%对14%只本协议观察，不证明可执行机器人导航、真实几何或generative world dynamics。

Symmetry两split各25，10x16grid与CIELAB cell平均色差15判全格正确；平均格色可漏局部细纹/保真，不能把阈值当精确像素。C的10prompt在同人口比较最佳/最差40/64pp，明确提示/所选人口与输出方式能大改结果；T2部分pass1如42/65不是25样本一次二元等权的4pp粒度，实际采样/汇总口径需澄清，不补多次生成/CI或断全部结果无效。Analogy每transformation50、四类200；裁最后帧目标给Gemini2.5Pro对三candidate判近似，judge还得知目标feature/条件值，order打乱，空或错类随机给三个选项之一；>88% agreement只是各condition25例与作者一致，不授真值/全部独立人审。Reflection/rotation低于1/3且多数越多可更差，是稳定错mode反侧；不能把color/resize正侧抹掉或把高passN当已解决selection。

**分母/因果与全费。** T1 maze写4split×50×10×2却列8000（直乘4000），irregular正文又40，完整表合计17640并不能解决这一项人口冲突；保原数字而不私造额外四split。表每类k/模型/实际生成与评价使用量分开，不从合计倒推足够统计独立性或严谨总账。多prompt/同母图变换/同一作者judge与同provider模型相互依赖，本文没有给足跨模型主干大小/训练预算的控制、全部CI或可独立复查人口来签能力演进唯一归因。Veo2→3发布同时改变系统，单个较弱Gemini对照不能证明chain-of-frames是必要计算机制；整个video输出也不由帧展示次序证明内部逐帧自回归推理。

本文不量化physics modeling，D还明确depth/normal/force-motion、rigid-body/puzzle等失败；逼真画面不是action-conditioned可控预测或物理安全。S5“performance lower bound”只能按所选模型/输入/搜索协议的已观察表现理解，不是随机部署人口成功率的统计下界，oracle选择和提示选比还可能乐观。LLM推理费用下降的外部估算不证明video费用必然同速下降/专模必被替代。完整source图制备/人工筛、重写器、全部video/失败尝试、192帧抽取/评分与阈值选择、候选裁决、人审和独立最终任务回归均计费；硬件/权重量化/总API费/墙钟并发SLO未披露，不由8秒产物长度当生成耗时或实时性。

最小可支持接口是：**生成器可作为非原训练任务的候选生产分支，但可见结果、可自动读出的任务输出、oracle候选/帧上界与可交付正确性须分开验收。** 即使不作新Books写入，局部正侧/系统重写器角色、失败和测量选择仍完整保报告。无可靠读出、成本过高、输入支持或质量不合时，保专用视觉模型、可信parser/verifier、固定输出时点与人工/Unknown；不能把无自做微调写成无数据、无费用或基座真实智能已证。

本首备已完成、root唯一请求真实结束，无网络/exec在途；writer只上述支持/反侧所需原域实际采用/具名纠正，不要求先看A全部演示/所有视频。reader后角色复用，原5不降、不因有限/可能NC撤候选；具体owner仍下一新层，未预日完成。
