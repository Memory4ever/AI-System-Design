# QuantFL17507：初始化与更新量化分责，root 必要准备

仅03-20补03-19；本日已独核的日期/贡献准入与2+1+2=5复用，不另扩公开日。root是本包准备者，不自授Source/PRE/整合或DAY。当前[官方abs](https://arxiv.org/abs/2603.17507)及[exact-v1 HTML](https://arxiv.org/html/2603.17507v1)实际可读，无当前撤回信号。

## 必要原证

root实际读v1 III–IV/Eqs1–9/Alg1（L100–198）、TII/III、V与结论/直接未来限制（L199–253），另II L88–98仅辨与EF/PTQ已有路线；未核代码、实际通信或energy、所有图像像素或复现。网页references传输不计审阅。

通信对象是相对广播base的每轮本地参数差Δw，不是initial weight PTQ或单minibatch gradient。客户端训练后按layer bucket encode，server midpoint decode后作简单等权平均；non-IID数据、client权重和本地epoch仍属于objective。BU等宽/BQ等频与QSGD随机unbiased comparator不同，确定midpoint不自动unbiased或一般MSE-optimal（只有特定区间条件分布/目标才成立）。Warm start可能减小range，fixed L下uniform bin宽R/L变小，但局部metric改善不是预训练可以取代EF的定理。

Codebook资格本身有未闭合recipe：IVA说layer范围由update估计，IVD却从pretrained snapshot估范围；IVC又称server广播/early-round bootstrap以及L+1边界与式9的L计费。不能替作者补出overflow/clip、client与server一致版本或精确实现；有限采用只要求这些条件必须明确，不照抄recipe。不能从index bit数签实际网络字节/时间或碳减排。

实验：RTX6000 48GB/i9-10980，MNIST浅CNN与CIFAR100 ResNet18，100模拟clients每轮10、local2epoch，L64/128、boundary16bit；batch/precision、seed与重复不确定性、具体T、完整pretraining数据和费用、实际网络/能耗及服务SLO本必要范围不完整。TII未给同pretrained未压缩NQ对照（NQ是NP），因此不能分别归因pretraining与compression，MNIST BU89低于NQ90.01；CIFAR BQ25.78/QSGD28.90低于NQ47，不能普遍称matching质量。TIII skew变强BU68.28→52.1。图2明确simulated illustration，不是实测更新分布或预训练因果证据。TII CIFAR NQ与BU同5,891,001/6,046,446，却填40.62%/39.05%减少，数值不自洽；只隔离减排/严格pareto数量，不拿数字支撑正文。未来明确需大模型/realcrossdevice以及biasedcompressor/EFformalanalysis，非通用LLM通信改善证明。

## 唯一owner与有限PRE

`TRAIN-DISTRIBUTED-TRAINING`，[Ch36](../../../../../books/part-04-training-system/36-distributed-training.md)实际完整432–465，typed encode/merge/decode→同/异client expert更新集合→training collective。现有共识/EF/error state在81–83及后文，Ch35 checkpoint管持久恢复；Ch37 actual开头管tensor shard不接本地更新compressor。具体差额是warm-start统计作为量化配置成立条件，而非无损/EF替代理论；拟一段位于federated type完整限制后、同架构MoE参与集合前，不另新标题。

相同的 `encode → merge → decode` 协议还要明确被编码的是本轮相对哪份 base 的更新，而不是把已预训练 weight 较小的文件直接当训练通信收益。Warm start 若确实收窄更新分布，可以让固定 bucket 数下的量化步长变小；但 sender 与 receiver 必须共同持有 layer range、codebook revision、刷新周期和越界处置，预训练本身不能替代有偏误差累积或 error-feedback 的验收。[有限更新量化对照](https://arxiv.org/html/2603.17507v1)仍混合初始化与压缩选择，图示集中度只是模拟，等频与等宽方案又有质量反退；索引、边界、全精度下行、本地训练及预训练成本须共同计入，不能从 uplink bit 数推出实际能耗或全网提速。分布漂移、码本失配或质量预算无法满足时，保留更高精度更新、已验误差补偿与同步 base，不让较窄的初始 range 签发后续所有轮次。<!-- source-family:SF-2026-ARXIV-2603-17507 -->

静态源注拟稿：

- `SF-2026-ARXIV-2603-17507` — [QuantFL exact-v1](https://arxiv.org/html/2603.17507v1)必要III–V/Eqs1–9/Alg1/TII–III与结论限制；仅warm-start统计/更新base/码本身份作为量化条件，保NQ未匹配初始化、质量反退、simulated concentration、CIFAR bit账不一致和codebook recipe缺口。不采预训练替代EF、midpoint一般最优、严格pareto/碳减排或LLM普适收益；未核代码、实际网络/能耗或复现。

## 待非准备者裁

作者或reader有限核必要原证/实际owner与这一literal，也可判具体已有覆盖或中心不可分采；准备稿不等Books已写。没有Source/PRE实际通过与root共享锁授权，不写Ch36。

## resume_mar17 非准备者有限裁

2026-10-12：实际独读exact-v1 II L88–98及III–IV 100–198/Eqs1–9/Alg1、TII–III/§V/结论199–253，支持与直接反側足即停止，未读代码/全部图或复现。原one literal/static有限PASS：编码对象明确是相对每轮广播base的更新，窄range只作为固定bucket条件，不把未控warm-start效应授EF替代/无偏/普遍通信或能耗收益。实际NQ非pretrained、MNIST/其他量化反退、CIFAR NQ/BU相同bit却给减少比例、Fig2 simulated都与正文近文隔离一致。IVC 187–194同时L+1、‘L internal’和端点计费的口径未全闭合（L intervals真实内部边界为L−1）；不替作者补编码recipe，完整边界/下行/预训练费需实账。

实际顺读Ch36 425–471及81–87，Ch35/37开头。原一轮typed协议与已有EF/optimizer状态边界不承载初始化统计变化怎样限制update量化配置；拟federated type完整marker后/MoE参与集合前只这一受限条件段成立。不把小数据、缺代码或未证明强桥当EX，不改原5/date。本裁仅有限条件和反证采用，原准确率/能耗与浓缩因果未得正面认证；root窄写后作者一次非writer实际正文/完整邻接/本人static POST再计I，未授DAY。

## resume_mar17 一次非writer actualPOST

2026-10-12：root实际窄写后，非writer实际完整Ch36 425–471、新445及本人静态源注2198/前ProRL、AcceRL邻注逐字回本包原one literal和已核必要Source；有限POST PASS。完整一轮typed协议→新增相对base的update/range/码本条件→原MoE多参与集合和assigned expert分责衔接成立，不把量化warm start冒充原type可表达任意协议，也未抹去原error-feedback或全下行成本。质量反退、simulated concentration、初始化/压缩混杂与recipe缺口近文，静态注不复制验收流程。限定diff-check无输出；root接纳后释放本family Ch36并计I，此非本日报DAY。
