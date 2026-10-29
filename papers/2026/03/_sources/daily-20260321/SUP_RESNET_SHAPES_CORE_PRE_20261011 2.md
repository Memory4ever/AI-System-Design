# ResNets of All Shapes18168：必要原证/actual owner/最小PRE

resume_mar18准备，仅本21补BJT03/20；原65完整题摘与root准入校准复用，不扩query。非准备者尚未裁，不写Books或计safe/DAY。

## 身份与新增命题

实际[官方exact-v1 AB/currentheader/history](https://arxiv.org/abs/2603.18168v1)唯一v1Submitted03/18T18:07:02Z，无已见accepted/withdraw/correction信号。[真实DataCite](https://api.datacite.org/dois/10.48550/arxiv.2603.18168)created03/20T02:06:21Z、registered22Z/statefindable/AvailableMar；v1Updated是03/23T00:56:55Z，明确是另一个字段，不把它冒充first-public或依据其时刻移动归属。本批注册夹证仅支持BJT20 arXiv事件限定推断，不证明别处无先稿。HTML封面August24与[exact-v1 PDF](https://arxiv.org/pdf/2603.18168v1)封面March20,2026不同；实际定理/假设与实验采用PDF，不用HTML内部日期推laterrevision/先稿。

深度、MLP宽度和残差表示维度往往合并为“规模”→在特定有限步MLU残差网中，D增大一边降低有限表示误差、另一边提高D/(LM)耦合项→不能只按参数总量或单轴加宽判断逼近同一训练动态。拟2+1+2=5，仅残差块形状/动态误差接口，不给成熟参数化原则/普遍模型Scaling基础加分。拟改变长期解释，必要假设与组合推导定点深入。

## 必要原证与直接反侧

实际PDF用户页3–7：Eq1/GD、Theorem1.1和全部四remark、§1.3/Fig1–2实验设置及optimal-shape讨论；定点Theorem2.5用户页17、Theorem1.1组合证明用户页49–50（PDF行10279–10545）的条件概率/union与triangle步骤。未遍85页证明、所有lemmas、附录、代码或复现；不宣全部证明无误。必要方法、结论权限与关键反侧已足。

- Eq1层更新为h+Vρ(Uᵀh/D)/(ML)，输出Woutᵀh/D；M是两层MLP隐宽、D是residual state、L层数，P=D(din+dout)+2LMD，不等三者相同“width”。U/V初值centered subgaussian方差Dσ²、梯度步率ηLMD；embed/readout另ηD。MLU局部非零feature更新不同于lazy ODE/kernel，不授现实Transformer都处此regime。
- Theorem1.1要求ρ的一至五阶导数有界、loss-gradient Lipschitz、所列scaled初始化与ClippedGD；ηin/out=0简化。大L部分的clu/clb要有界且一至四阶导数有界，不能因本篇大D分析忽略clip就授普通unclippedGD。logL∨D≤C0M、右侧须<c2；固定step k及失败概率δ时，输出/耦合hidden RMS误差上界含1/L+√(D/(LM))+(1+log(1/δ))/√D。hidden极限是独立随机过程拷贝，output极限为确定向量，不把二者同称确定性hidden轨迹。
- 组合路径是有限ResNet→finite-D MeanODE旧误差，再finite-D→infinite-D新1/√D，经union/triangle结合；不是loss→global optimum证明。§5.2末式排版用∧而Theorem1.1用∨，不采该符号为额外保证，正文仅作者定理有条件上界；不借未读lemma认证全rigor。
- N=1实际写证明、N>1由作者说明adaptation；常数对k和N可superexponential，不证明长训练/越来越大dataset统一误差。ρ本身不必有界（线性/光滑ReLU允许），需至多线性增长；LayerNorm/RMS projection未包含，不以此替换Norm。D/(LM)→0、logL=O(M)、D=O(M)是充分形状条件，作者只认为第一可能必要，后两必要性未解，不当普遍必要定律。
- §1.3以(50,2000,2000)finite reference作极限proxy且约.1误差floor；din/out5/N10 Gaussian、tanh/MSE、15GDsteps/5repetitions。h误差手调(.8,2.5)拟合并忽略1/L项，output另(.15,.9)拟合，均非真实LLM质量对照。output改D/(LM)非平方根是conjecture，P^-1/5与L~P^1/5宽~P^2/5建议依赖猜想；“更浅更并行”没有硬件/通信/峰显存/运行时间试验，不采用选型recipe或实测加速。
- 定理P^-1/6是最小化所选上界（LM~P^2/3,D~P^1/3,L≥P^1/6），非任务质量/容量/泛化最优；固定QK维attention的扩展只在所述有限维ρ表示条件，不授普通softmax/多head/全Transformer训练。训练数据、Norm、AdamW、长horizon和真实质量另需核验，数学误差不代替系统成本。

## Actual sole owner与最小差额

本21Books上下文已重载；actual `MODEL-TRANSFORMER-LAYER` Ch17完整348–391，已有Keel联合norm/residual/depth-width/LR/data、饱和导数/APJN初始化非全部训练、迭代算法解释权限。actual Ch28 374–393有hyperparameter transfer与非lazy feature learning分责，不承载三形状轴的finite-limit误差竞争；参数化训练细则仍归Ch28，不另写。Ch16/18开篇交接已实际读。建议Ch17 Keel共存段完整后/“不计算归一化…”前一段：承接联合形状但不称现文原论点被纠错。若非preparer认为实际已覆盖此具体误差链可裁NC，不强造diff。

## 一段literal PRE（待非preparer）

联合形状还有一条需要分开的解释：残差表示维度D、每层MLP隐宽M与层数L，并不是可互换的三个“规模”。[一项受限残差网分析](https://arxiv.org/pdf/2603.18168v1)在特定初始化/步长缩放、光滑激活导数与loss-gradient条件以及有界平滑的梯度截断下，给出固定训练步数时逼近同一极限动态的误差上界，包含1/L、√(D/(LM))和1/√D三项（省略固定失败概率的因子）。增大D会降低有限表示误差，却可能提高它相对深度和MLP宽度的耦合项；因此相同参数量不能只凭更宽就声称更接近该极限。这里的“收敛”是有限模型与极限动态之间的近似，不是任务loss到全局最优，也不是形状更好就更会学习；常数对训练步数和样本数的依赖又限制了长程外推。输出侧更快的形状律仍是猜想，Norm、真实任务质量、完整训练费用与硬件并行效率没有由这条误差界得到认证。比较实际模型时，继续验收残差缩放、传播、收敛和质量，保留已验证的Norm/宽深配方，而不按极限误差公式自动选型。<!-- source-family:SF-2026-ARXIV-2603-18168 -->

静态注：- `SF-2026-ARXIV-2603-18168`：[ResNets of All Shapes exact-v1 PDF](https://arxiv.org/pdf/2603.18168v1)，必要Eq1/GD、Theorems1.1/2.5与§1.2–1.3及§5.2组合证明；仅三形状轴在指定ClippedGD/光滑条件下的有限步极限动态误差分责。保clip/shape门、k/N常数、finite-reference/手调系数、output猜想和未含Norm；不授全证明认证、全局优化/泛化、通用形状或硬件加速，未核代码/复现。

## root 非准备者必要原证与 PRE 裁定

实际重新打开 exact-v1 PDF Eq1/GD、Theorem1.1 的全部假设与误差项、全部 remarks、§1.3 的 finite-reference/手调拟合及 output conjecture；实际读取 Ch17 348–405 的 Keel→无归一化传播→算法解释完整交接。DataCite created/registered/state/Submitted/Updated 原字段独立读回，与准备者区分 first-public 日级夹证和 v1 Updated 的判断一致；不授不存在其他先稿的断言。

有限 PASS：三形状轴的误差竞争在现有 Norm/残差联合设计之后形成具体差额，5分与局部深入深度成立。literal PRE须把“特定初始化/步长缩放”后补为“在定理的 log(L)∨D≤C₀M、误差上界足够小且固定随机输入/读出层的简化设定下”，避免删去关键 shape gate。其他 literal 边界和静态注保留。仅采用有条件近似界，不认证85页全部证明、最优质量形状或硬件效率。允许作者在 Keel 共存段后、无归一化标题前窄写一段，写后由 root 非 writer 实际回读；当前未写、未计 safe 或 DAY。

## 作者实际窄写与回读（非POST验收）

root授soleCh17一段/static锁后，作者已在actual371插原PRE，唯一条件补充落实为“特定初始化/步长缩放（另须满足定理的log(L)∨D≤C₀M、误差上界足够小且固定随机输入/读出层的简化设定）”；其余原段/static不改。actual完整358–392的Keel共存→新增→无Norm传播及末五行本人/邻注实际读回准确，marker/static各唯一，限定diff-check通过。待root一次nonwriter完整实际POST，当前不计safe/DAY、不在Books注记动态验收身份。

## root 非 writer 实际 POST

实际读取 Ch17 355–391 的完整 Keel 成立/共存边界→新增371→无归一化传播→后续算法解释起段，以及末五行本人889与相邻两项静态注；回原通过的 literal PRE、必要定理及约定条件补充，正文与注一致。关键 shape gate、固定随机输入/读出简化、clip、固定步数、误差近似≠优化/质量、常数依赖与 output 猜想均近文保留，没有把 shape prescription 或硬件效率采成保证。原段未删，机制在 Review notes 前，限定 diff-check 无输出。有限 POST PASS，root接纳为实际整合、释放 Ch17 窄锁；只单篇安全处置，不授本日 DAY。
