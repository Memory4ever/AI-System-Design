# MUD17970：必要Source与有限PRE（03-20补03-19）

作者resume_mar17，2026-10-11。fresh03-20实际重载AGENTS、Research/Report合同、Sources使用/每日/arXiv主题、prompt、ROADMAP、本日README/STOP及最新LS路由。只本日，不继承03-19队列；原窗口/Monitor评分日期/连续§4保持。此packet只准备原证/actualowner/PRE，未写Books、未授Source/PRE独核或POST/DAY。

## 身份与采用范围

[Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training exact-v1](https://arxiv.org/html/2603.17970v1)，SF-2026-ARXIV-2603-17970。完整AB/当前官方说明与日级DOI夹证已由本日独核§2通过，公开日期03/19；Submitted03/18不是公开日期。2+2+2=6不变。仅采用替换matrix momentum的有限一pass数值接口及质量—成本边界，不采普遍更快、全局收敛或与polar等价。

## 必要原证实际读到

精确v1 HTML实际§2–3.4（Eq6–22/Alg1–2/T1）、§4.1.1–4.1.4（T2–5/F1–7正文条件）、§4.2（T6直接反侧）、§5采用边界已读。reader指出同v1 Appendix A mud_whiten已给Q递推，作者遂实际定点读取L541–574必要内嵌实现；不遍后续Optimizer完整实现。未精确拟合plot，不核repo artifact/运行或复现；工具返回的§4.3蛋白实验不作为当前Science范围采用依据，不展开全部附录/证明。足支撑以下有限命题即停。

- §2 Eq6–9：full-row-rank时polar是Frobenius最近row-orthonormal方向；有限NS polynomial保留奇异向量但并非exact。矩阵按小维度转置，非矩阵/embedding/head仍AdamW；不能把MUD说成所有参数的新通用优化器。
- §3.1/3.2 Eq16/Alg2 L218–242：不做真实Cholesky分解，而先行norm、Gram、取含对角的tril、forward TRSM、再行norm。三角路径依row次序，不继承symmetric polar的旋转不变/最近方向。只拟一pass。
- §3.3 Th3/Cor4 L286–334：初始Gram unit diagonal且I+E、E足够小，局部Gram误差二次收敛；不是随机外层loss/global/convergence certificate。任意缺秩矩阵在可逆左变换下仍缺秩，不能变成满秩I。
- 直接数值边界：Alg2只向行norm分母加epsilon，零行仍令Gram/tril对角为零，TRSM不能由这个guard保证可解。Appendix A内嵌实现使用Q初始化后每pass更新Q，float32 TRSM、rownorm clamp_min(eps)而非加epsilon；因此Alg2未M←Q是其数学伪代码省略，不能忽略A已有多pass递推而称整篇对应关系未闭合。零行在A仍令T对角0；这是对声明接口的本书推断，不声称作者正常run必失败。这里只拟一pass接口，不从伪代码或未运行实现授所有输入/多pass数值稳定与外层收敛。
- T1成本把GEMM按2乘加FLOP计而TRSM写0.5k²d并说counting multiply-adds，计量不齐；不照录12×/6×精确算术比。TRSM较GEMM实际吞吐可能低，理论运算减少不直接授training-wallclock。
- §3.4 L337–345：作者多数配置一pass时间到目标最好，二pass特例有益，三pass未提升；减NS至3在这些单GPU配置未取得有意义净收益/部分不稳，仅作者对照描述。缓存三角算子虽局部step便宜但到固定验证perplexity无净改进，不能由缓存免费推优势。
- §4.1：OWT/WikiText103/FineWebEdu GPT2 small/medium/large约125/355/775M；单A100 PCIe40GB/MI250/GH200，同图同硬件；torch.compile、BF16 autocast；GPT2 BPE；默认lr1e-3/WD1e-2/β矩阵.95、clip1、warmup500+cosine，三个seed[1203,3721,7865]并rolling7平滑。部分AdamW低LR3e-4因不稳，而Muon/MUD约1e-3，非所有条件同一LR。
- T3–5 peak tokens/s AdamW最高，MUD中间；短context/Muon开销比例更大，随长context摊薄。F1 OWT medium B12/T2048/GH200 Muon/MUD6000 vsAdam9000steps；训练墙钟排除evaluation time。F3 OWT small B24/T4096/GH200低perplexity区域MUD1落后，Muon低perplexity更稳；不授所有质量阈值MUD最优。F7 FineWeb large B8/T2048/GH200只能本配置，A100/MI250放不下，不补造对应迁移实验。
- §4.2 T6替换NS而保原AIRBench recipe，20runs mean/std：8epoch Muon3 .9402/2.9690s，MUD1 .9334/2.9795s；13epoch+momentum.7 Muon3 .9445/4.7565s，MUD1 .9407/4.7498s。小matrix卷积regime时间近似而质量退，三pass更慢。保此直接反侧，不将减少算术等于通用更快。
- §5分布式/更大规模为future。全搜索预算、数据准备/编译/评价/保存恢复、energy、长horizon/真实downstream/generalization成本及完整不确定性Not Disclosed；单GPU训练time-to-quality不授整个生命周期加速。

## actualowner具体差额

actual Ch28 `TRAIN-PRETRAINING`完整L450–617已顺读，特别562–588既有whitening-regime、variance order、idealpolar batch条件、two-sided precondition、scalar/columnscale、headgroup与几何因果纠错；它们已有矩阵更新/数值map身份和费用，但没有把多轮NS换成当前Gram的含对角tril solve、一passrow-normalized并保次序/零行/局部条件的具体分支。不是泛主题NC。

Ch27开头1–72拥有数据分布/经验风险与采样，不拥有矩阵方向算子；Ch29开头1–90拥有demonstration目标/条件最大似然。无新node。拟插Ch28现L576 scalar/column幅度段后、原head-group semantic marker前，两段保持原段绑定，root先协调共享窄ownership。

## 逐字PRE（未写/待独核）

多轮 Newton–Schulz 并非取得矩阵去相关的唯一路径。当正交化开销占训练 step 的明显比例时，一条受限分支先沿较小矩阵维度逐行归一化 momentum，形成 Gram，取其含对角的下三角部分，用前向三角求解变换方向，再逐行归一化；它省去多轮 Gram 应用，但不是实际 Cholesky 分解，也不继承 symmetric polar 的最近方向或旋转不变性。Row 次序、转置约定、pass 数和数值 guard 因而属于 optimizer/checkpoint 身份，非矩阵参数仍可保留 AdamW。<!-- source-family:SF-2026-ARXIV-2603-17970 -->

[必要方法与直接反侧](https://arxiv.org/html/2603.17970v1)只支持披露的单 GPU、小型 GPT-2 训练中的质量—成本分支：局部 Gram 收敛要求接近单位阵，不保证外层训练或任意缺秩输入；行归一的 epsilon 也不等于三角求解的可逆性保护。这里采用一 pass 接口，原内嵌实现虽给出多 pass 递推，也不因此获得全部输入的数值稳定保证。Triangular solve 的硬件吞吐、额外求解和调参仍计费，训练计时排除了评价时间；较低 perplexity 区间与小矩阵视觉对照均有退步，缓存算子也未改善到目标质量的净时间。应按相同数据、实际数值 map、目标质量与完整预算验收，而不是用算术比替代墙钟；求解 guard、次序或质量—费用失配时，保留已验证的 Muon/AdamW 与成熟恢复路径。

本人静态注：`SF-2026-ARXIV-2603-17970` — Daily2026-03-20补03-19；[MUD exact-v1](https://arxiv.org/html/2603.17970v1)§2–3.4/Eq6–22/Alg1–2、§4.1/T2–5及§4.2/T6，必要Appendix A mud_whiten递推。仅一pass rownorm→tril Gram solve→rownorm接口/有限quality-cost；localGram非外层训练证书，不忽略A已有多pass递推，也不授零行数值guard或精确成本比。保小perplexity/CIFAR反退、单GPU/BF16/质量目标与全fee界；未核repo或复现。

## 停止与待办

实际落实：root授Ch28本两PRE/静态注窄ownership后，作者写新578/580、完整568–595及本人1875/邻注读回，scoped diffcheck0；resume_review17_18一次非writer实际568–595/1870–1878 POST有限PASS已落本日独核§4，root接纳释放。只此采用已安全整合，不改Books验收身份，不授全输入稳定/普遍速度或DAY。以下拟写状态为原准备历史。

支持与直接反側足支撑最小两段，停止新增附件/版本史。待非preparer必要Source/PRE裁定；未写/未POST不计安全处置。若需要采用全输入稳定解法/12×成本，重开时只请求zero-row/damping的实际trace、统一FLOP定义及匹配质量全費，不再索取A已披露的多pass递推，不为本文无限遍proof。
