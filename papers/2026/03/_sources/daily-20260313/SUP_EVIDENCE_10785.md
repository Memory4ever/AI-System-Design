# 2603.10785v1 SGA：必要Source、理论边界与Ch24窄PRE

仅03-13补查，Mar12 BJT日期/首包准入复用。初拟2+1+2=5保持；必要数学转接/预算深入完成。作者只写本日包，不写Books，Source/owner/逐字PRE待非作者核；不授全日。

## 实际必要原件

精确v1 [官方HTML](https://arxiv.org/html/2603.10785v1) `SUP_CORE_10785.raw`：实际读§3.1–3.5/4.1–4.5/6、Tables1–2、AppendixA–E推导/实现、F训练预算与预处理、G消融讨论、I完整Algorithms1–2及notes；H社区模型表仅上下文，不采用这些发布版本新事实。TXT/去标签公式文本仅定位，未复现或运行GitHub。必要采用只限数据/采样/更新粒度的接口，不正面采用未知NTK可被校准控制或33%端到端效率。

## 数学能支持什么，不支持什么

AppendixA的Gaussian conditional path+有限经验数据把marginal target分成同(x,t)的密度加权各组均值。A.3明确随机partition也成立；是代数身份，不认证语义crop独立性或语义质量。B将同(x,t)残差加权和平方展开为Gram quadratic，E.3–4链式规则得到同位置`Δξᵀ J Jᵀ Δη`，不能把成熟MSE/chainrule/NTK身份单独计新增。

E.5实际自承PSD kernel不保inner-product符号、非isotropic、无法在本文规模测/控制kernel。故output残差较对齐不自动意味parameter梯度不冲突；不同crop/time训练样本实际涉及不同Jacobian，不能由同位置身份推导组间实测梯度。E.6的scaling-law分支明确speculative。数据/tuple/scale操作是启发式输入干预，本文没有提供同预算实测gradient-innerproduct、NTK/conditionnumber或明确losslandscape因果对照。Figure2/6正负残差叫constructive/destructive不是一般优化保证。

§3.4 Eq6平均各group loss，不含显式cross-term penalty；same-marginal co-sampling可能改同一更新中的协方差/顺序，但不能说给loss加了不存在的pairwise term。Algorithm2通过root-group连续metadata和deferred optimizer实现动态K_g accumulation，不一定一physical batch装下整tuple；与Eq6的1/K平均/gradient normalization有未显示交接，完整可执行loss不认证。K_g=1/2/3与不同aspect buckets的cross-root批处理也需要实际loader资格，不能凭伪代码补实现。

## 实现：有窄可采用接口

Algorithm1以detector得到Macro/Meso/Micro crop，保留原图root r与granularity ξ；IoU过滤、aspectratio/downsample/bucketing并可能ESRGAN超分，得到`(crop, ξ, root)`。这扩大有效训练样本，不是获得独立的新真实图；检测/裁剪/超分会引入漏检、错误part–whole和伪细节。Root标识供联合更新，不能直接借crop数作为数据多样性。

Algorithm2以root group的各granularity subbatches在一次optimizer step前累积梯度；保留resolution bucket但不以每subbatch单独step。FLUX按ξ改变logitnormal shift（Macro+.5/Meso0/Micro−.5），再resolution flowshift；SDXL按ξ改变Min-SNR clamp（4/5/7）。两种不是同一sampler：前者改p(t|ξ)，后者改w(t,ξ)，都改变effective训练强调；没有inverseweight时不宣告原目标无偏。主文FLUXt高=噪声，Ch24自身s高=数据，拟文不混方向。预算/recipe身份应绑定crop/root、比例、time方向、采样/权重、accumulation normalization与optimizer步。

## 实验与可推断边界

FLUX1-dev/DoRA rank32 alpha16，AdamW1e−4 batch8、1280²；AnimagineXL3.1/LoCon linear64/32 conv16/8、Lion U-Net3e−5/textencoder3e−6 batch2；同single RTXPro6000 Blackwell96GB。6/3 domains各100到数百图，不是大通用benchmark；8 domain prompts×至少5generation seeds≥40 outputs/variant，不等5次训练seed。20 blind human participants及GPT5.2 judge rank四variant，1st-place是相对四者排名，不是calibrated correctness。

Table1平均CLIP-I/T/DINO-I有限改善，不证明每domain无退步；Table2三way 1stplace sum100提供tuple/scale操作联合方案的有限相对质量，非实测稳定性或唯一架构因果。FLUX batch8 vsSDXL2、不同adapter/optimizer/数据domain与backbone同时变化，G的“globalattentionvsCNN造成消融差异”是解释，非single-variableproof；LoRA/DoRA额外对照是qualitative。未测general能力回归/forgetting、NTK/梯度方差、训练multi-seed/CI、deployment precision或完整solver/NFE。静态图像限定，video/multimodal mixing只是future。

F预算FLUX N1=8–14h、N2=1.5N1；SDXLN1=1.5–2h，gamma N2=2.5h而非严格1.5×1.5，checkpoint nearest偏差≤30min。F.5 **实际披露** H-SD 15–30min同卡/数据集，不能叫未披露；SDXL1.5h时约17–33%额外阶段，不当然negligible。≤30min checkpoint误差相对短run也大，故SGA N1优于baseline N2排名不能直接授精确33%总费用节省。检测/ESRGAN、caption/数据构建、update内forward次数、evaluation费用须分账；现报告只有estimated训练GPUtime+oneoff范围，保留有限效率观察不授端到端SLO。

## 实际owner对回与拟采用差额

唯一owner需ROADMAP精确 `MULTIMODAL-GENERATIVE-PARADIGMS`（发送前核ID）。实际顺读现Ch24 125–158噪声schedule/time/πw在线分箱及207–238完整FlowMatching接口/solver交接：已有采样改变effectiveobjective、proxy非真值、CFM的平均target/同gradient和训练/solver分账；没有root-linked semantic crops的一次更新group粒度，或同crop粒度改变timesampling与lossweight的不同接口。不能把一般πw原则再计新差额，也不让新篇重写已有CFM数学。

建议在FlowMatching基本路径/目标/solver两段之后、现“数据有效维数较低”之前追加两段，窄差额是数据变换→grouped update→conditional time/weight的共同identity，理论争议靠近接口隔离。成熟代数不写成新定理。若非作者认为此启发式不足形成长期差额，应No Change并明确是无采用的新理论/观察，而不是“已吸收”含糊标签。

## 逐字PRE提案（未通过，不写书）

> 少样本图像微调还可以联合改变数据视图与一次更新的组成：从同一原图裁出整体、部件与细节，保留root和粒度标签，在aspect-ratio buckets之间累积同root各视图的梯度，再统一做optimizer step。粒度标签还可决定训练time分布或loss权重；两者是不同接口，与更新中的group大小和归一化共同定义effective objective，不是自动保持原目标的无偏采样。这把语义相关视图放在同一次更新中，而不是给原MSE凭空增加pairwise penalty。<!-- source-family:SF-2026-ARXIV-2603-10785 -->
>
> 这条分支以检测、裁剪/超分、数据provenance与分组调度换更集中且可协调的监督；多个crop仍来自同一图，不能算独立新数据，错误part–whole或伪细节也会被共同强化。残差Gram与Jacobian链式恒等式不保证未知NTK下的梯度冲突减少，需另测梯度与独立质量/旧能力回归。[有限FLUX/SDXL对照](https://arxiv.org/html/2603.10785v1)中的相对人审/judge排名支持启发式探索，不认证普遍优化稳定；预算使用估计训练时长与附近checkpoint，另有预处理费用，不能把较短checkpoint优势直接称精确端到端节省。分组归一化、语义视图或质量/费用失配时，保留原完整图、标准bucketing与已验收的time/weight方案；原Flow Matching目标和solver责任仍分别验收。

未有共享Books lock/writer/POST；强kernel/scale定理转接、未明确recipe normalization与精确效率主张若将来采用，仅定点重开；不为当前窄接口索要完整附件。
