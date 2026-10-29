# Sep23补Sep22：ToFU与Tensor Defense首次必要证据

Singer A162明确两必要域未开始且无CORE/请求在途，root本轮明确接受后首次capture与有限首备。原AB、日期、2+1+2=5分别复用，不第三审，不改旧候选字段。下文是准备者记录；须Singer唯一另一角色回必要原域实际采用，Sartre随后只复用已闭角色链。尚无本两项Books处置、写入或整日报验收。

## 原件与实际范围

- [ToFU exact-v1](https://arxiv.org/html/2509.15861v1)：[raw](REPAIR_20261024_ROOT_CORE_TOFU_15861.raw)/[request](REPAIR_20261024_ROOT_CORE_TOFU_15861.request.json)，GET 2026-10-24T05:43:19.417451Z～05:43:20.338985Z，200/exit0，361996B，SHA256 `2a0d482d6751d00919276b08377c2de19dfc82c9fc5c27c1d2973525a64b62d4`。实际结构化完整读§2–4、§5.1含整T1–2、§5.2含T3、§5.3含T4/直接F3–5文字caption、§7、A.1/A.2证明、C整配置/指标/T5/Alg2、D、E1–2整T6–7与F讨论/caption。未核全部背景、B曲线像素、实现或复现，不以全文件下载冒全文核验。
- [Tensor Defense exact-v1](https://arxiv.org/html/2509.16163v1)：[raw](REPAIR_20261024_ROOT_CORE_TENSORDEFENSE_16163.raw)/[request](REPAIR_20261024_ROOT_CORE_TENSORDEFENSE_16163.request.json)，GET 2026-10-24T05:43:59.149187Z～05:43:59.877751Z，200/exit0，103788B，SHA256 `1f03c6c3a731b14a78f3d38c64a3c795bfdeb4998fa99278427ea154ef67b2ca`。实际完整读§3–7、整T1与F2–5文字caption；未读图像素、核实现或复现实验，不把其他攻击或架构列为必须扩展配额。

## ToFU 15861：把可遗忘性前移，不等价于已经证明删除

### 两阶段机制与真正被优化的对象

此ToFU是Transformation-guided Federated Unlearning，不是同名LLM虚构实体benchmark。初始FL训练先按batch内相对loss排序：低loss样本取更多顺序图像增强，强度上限随通信round渐增；原图/增强图输出或表示的一致性KL与分类目标共同训练。删除请求到来后只在retain set fine-tune，可与既有FU方法组合。它不是事后对任何已训练模型免费插入变换，初始训练协议与数据可见性是先决条件。

相对loss不是无关信息量的已校准估计；同分/最大loss按严格大于计数可以取零变换。Alg2使用固定顺序八类增强的前缀，而不是任意独立变换家族。增强可能删掉真实任务信息；§4已承认过强增强导致欠拟合和收敛困难，MUFAC实际反侧与此相容。语义不变性和训练可遗忘性仍须分别验证。

§4 prose使用最新global模型排序，Alg1 LocalTraining则用正在更新的local θ算loss；Eq6已将KL纳入ell，Alg1第14行再次写ell+KL，是否重计不闭合；latent KL的概率化/归一与stop-gradient边界、M渐进更新变量记号未给完整可执行定义。记录这些差异，不私补复现recipe，也不因此否定有限实验。

### 理论主张的具体缺口

Def4把 `p_theta(x|y)` 与 `p_theta'(y|x)` 称为marginals，乘积却一般不是joint sample space上归一的参考分布，故Eq1不是已闭合的标准mutual information定义。可核反例：二元x=y且各取值概率1/2，两条件概率乘积在(0,0)/(1,1)均为1、总和2；以joint各1/2代入该印式得到负log2，而标准MI非负。此为对**定义**的有限反证，不称全部实验失效。

A.1用 θ→T1(θ)→T2(T1(θ))的数据处理链，只能在适当随机变量/Markov条件下给相对于中间节点T1的界，不能由“similar argument”自动得到同时不大于独立T2(θ)的另一侧。完整训练还重新读取数据；参数空间变换、实际输入增强和再训练之间的随机变量/独立性桥未建立。组合次序印式与随后的展开也相反。因而不正面采用“任意增强次序/强度单调改善遗忘”“证明全信息删除”或法律保证；A.2沿用这一前提，不修成自己的新定理。

### 评价人口、反侧与成本

实验为ResNet18、CIFAR10/100与MUFAC、10 clients、Dirichlet κ=1、50轮初始FL、20轮FU。主文local epochs5与C的10 epochs口径未闭。C：Schedule-free AdamW、b128、lr3e-4、每client留10%validation，两RTX4090/EPYC9654P/192GB、PyTorch/Flower；precision/独立seed数/CI与所有选择集ND，不把F3跨设置±当独立训练可靠性证书。

MIA Efficacy为forget被估作non-training的比例，越大越好，不是攻击成功率；LiRA shadows取最后5通信round，不能视为独立多seed或覆盖所有攻击。forget/test loss KS相近也不证明参数分布等价于干净重训、重构/重学习不可恢复或成员身份彻底隐去。

T1 CIFAR10 retain .8955仍低于FedPGD .8959；T2三数据ToFU的MIA Efficacy均低于exact retraining（.3239<.4645、.4560<.5007、.4651<.5375），CIFAR10 overall也低于exact。T3非删除MUFAC .8451→.8165，不能照录“无损”。T4三组件overall最高不等全部指标最高：SDT+TIR的MIA .5851高于full .4560，其他配置retain更高。T6负γ导致近随机utility却较高non-member比例，提醒隐私proxy与效用须联验；main γ.01不在T6网格内，不能称该表直接验证.01最优。

771.2s、24–28%下降仅后续unlearning阶段。E2实际初始训练0变换1277s、4变换1655s、8变换2027s，作者报约29.6%平均/58.7%最坏额外训练；是否摊销取决于真实删除次数，不能把后阶段下降当端到端降本。全client训练/增强与双路前向、通信、retain fine-tune、shadow攻击、择参和独立恢复/效用检查均计费，不给跨模型SLO或总墙钟保证。

原5与局部可组合设计/实际正侧保留；理论争议、具体owner与是否只采用受限机制，交唯一另一角色必要采用后再判断。不得降分、删候选或借已有覆盖洗掉这些争议。

## Tensor Defense 16163：低秩表征重构的受限防御与配置成本

在CLIP ViT-B/32的vision encoder中用forward hooks截取final norm/attention/MLP表征，CP/Tucker/TT低秩分解后重构，按 `T_final=alpha*T+(1-alpha)*T_hat` 混合。alpha小意味着更多**重构**权重；与PGD更新的同名step-size alpha不是同一个量，rank降低也不是自动删掉所有有害方向。输入/输出维度不变不等模型函数或语义无损，“无需重训”不等无运行图干预、无分解成本。

攻击为CLIP图文cosine匹配的白盒PGD，epsilon8/255、step6/255、10steps。Eq3最小化相似度与负cos损失梯度上升方向可对应，不因符号不同误报相反。必要威胁边界是：正文没有闭合攻击是否通过当前hooks/分解/随机初始化自适应反传、迭代分解是否可微、是否采用适当估计规避梯度遮蔽的验证。不能由未防御模型攻击的transfer表现授adaptive白盒安全；这是一项未证权限，不是已证存在gradient masking。

COCO/Flickr30K，参数分析1000对、综合3000对，样本独立/选择集分离、retrieval候选全集与多caption协议、重复seed/CI、GPU/precision ND。TensorLy/PyTorch，random init/50iterations/tolerance1e-4；未给被分解tensor完整axis/reshape及跨样本batch耦合，不能随意写成每图相同独立变换的已核recipe。rank设置prose16–256与F3实际8–512不合，区分实际读数与概括。

F2/F3单final-norm TT/rank32或alpha.2约10.6/10.7与6.2/6.3–6.4；F4最佳last5norm TT的19.8与11.9相对被攻击baseline7.5与3.8是12.3/8.1**百分点**，不是恢复到clean质量或相对12.3%提升。正文未给足独立clean防御前后质量，不据recall升证明语义完整保留；低rank可去有用信息，攻击也不必只在高频/低能量方向，作者“验证高频假设”的归因超过所给rank对照。

T1效率为rank64/alpha.2：无防御87.07ms/batch/367.51img/s，TT单层106.48ms/300.54（1.22x时间、约82%吞吐），TT两层171.11/187.02（1.96x），TT五层342.63/93.39（3.93x、约25%吞吐）；CP/Tucker单层1.83x/2.76x。效率rank64不等质量rank8–32，不能把最佳五层recall与单层22%开销拼成同配置结论。未核硬件/完整流量，数值仅原条件作者结果，不授实时或生产SLO。

全层截取/随机分解迭代/重构与额外驻留、rank/alpha/层位搜索、干净与攻击质量及独立威胁验证均付费。§7承认只有CLIP/PGD、其他架构与advanced attacks未测、多层实时开销。失配时保原模型/更轻预处理、独立攻击与效用验证/访问隔离，不把小模型检索提升外推生成VLM/LLM安全。原5不降删，具体owner新层待后续；未运行攻击代码/实现/复现。

## 交接与停止位置

两项首次有限必要首备到此，支持、直接反侧、理论/实现未闭与全费均保留。Singer只回上述必要原域完成唯一非准备者实际采用；完成后Sartre只角色复用，不第三Methods。当前没有本两项书稿授权/写入/PRE/POST或日级完成。其余日期/准入/有界来源层不因本包自动结束。
