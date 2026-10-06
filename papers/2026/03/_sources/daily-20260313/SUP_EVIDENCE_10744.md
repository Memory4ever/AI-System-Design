# 10744 JiT：稀疏anchor速度与维度扩展target的Source/PRE

仅Mar12 BJT补充自然日。第二完整exact-v1题摘/非作者准入、Mar12日级夹证及CVF具名同作者June发行/原arxivlink日期信号已有效核过，不重跑日期。官方 https://arxiv.org/html/2603.10744v1，SUP_CORE_10744.raw/txt与LAST_SECOND manifest/result GET200319870bytes、UTC2026-10-09T16:26:01.297434。实际完整§3.1–3.4/Eq1–10/Alg1、§4.1–4.5/Tables1–3/§5、AppendixA全必要分解/一致性证明、B.1–B.5/Alg2/Table4、C.1–C.2/D扩展正文。图仅正文/caption，不授pixels/视觉质量亲验、视频运动或curve精点，无代码/复现/current v2。

## 实际新增命题、最低投入

完整latent每步全tokens重算贵、直接coarse resize/新token瞬时注入可错配→保持完整latent状态，只把逐级增多anchors送原DiT，由速度插值更新未计算位置；扩anchor时重造该位置的clean-prior加noise target→改变“哪些位置实际求值、哪些状态仍演进，以及何时重置为可计算子空间”。不借成熟interpolation/variance salience/Flow本身抬分。拟2+1+2=5：具体空间sampler状态接口2、单生成路径1、可复用subset/target/原state分责2。当前Ch24有具体gap故必要深入已完成，拟两段受限整合；强full-field精确/统计正确/无损/7倍通用SLO不采用。待非作者Source/actual owner/PRE，未formal未写Books。

## 机制与强保证隔离

§3.1 nestedΩK→Ω0全位置，Skselector/Pk/Qk新位置投影；§3.2 Eq5只计算uθ(Skᵀy,t)，Π=嵌回active+inactive插值，完整y仍更新，不是只保小state或旧层KV缓存。Eq7/AppendixA.4仅保证lifter在anchor不改**已少上下文的computed velocity**，不是它等full-model Sᵀuθ(y,t)。A.2明确sparse input与inactive extrapolation均近似；主文“continuously full context/correct statistics”不能由投影恒等式推出。active消失上下文可能改变attention，即使保持原二维坐标也非原fullvelocity证明。

§3.3 target Qk[TkΦk(Skᵀyhatclean)+(1−Tk)ε]，yhat=y_prev+(1−t_prev)v_prev是approx endpoint proposal，Φ从旧anchors插值。Gaussian噪声幅度匹配不证明真实joint/conditional intermediate law；cleanprior偏差/与noise依赖及新位置相关仍未核，不能说一般统计正确或artifact-free。Eq9 finite-time hitting：target固定且t<Tk时线性逼近，existinganchors冻结；末点定义limit而非直接除0。**Alg1实际line18直接assign new positions为target**，不是披露一个有限δ逐步integration的连续代码路径；不能由理想micro-flow称实现从不跃变/自动稳定。旧anchor未更新与newstate重造应分别标身份。

ITA正文用uθ/full输入符号，Alg1line10实际用上一步**近似完整v_prev**的3×3poolvariance，再top inactive位置补集，不能补成每次额外full-model probe或calibrated error/semantic importance。B.1初始stride2+boundary，但budget超时随机drop可删边界，所以不能签“全部边界硬保”；randomfill/drop是额外随机身份，不因DMF称整sampler无随机。

B.2 nearest-neighbor+Gaussianblur，ρ=m/N被文称sparsity但实际是保留密度，L≈ρ^−.5/σ=.4L；Alg2把anchors原值与其他位置blur组合，Π的I应只inactive而Φ可full。这保原anchor输入值，不认证inactive manifold/统计保真；数值kernel大小整数/padding等未详，不自行补唯一实现。三stage18NFEs 7/4/7保留35/62/100%，11NFEs4/3/4保32/60/100%；完整state/插值/pool/rank/随机索引和最终VAE均有费用。B.4 Beta inverseCDFα1.4β.42，t0noise→t1data且通常此形状量化点晚区较密，作者“early/high-noise denser”解释口径需审，不借引用证明它；实际schedule/transition必须冻结，不更改原公式。

## 必要评价、人口、直接反侧

§4单A800/FLUX.1-dev，实际table只NFE/latency/FLOPs及质量，无checkpointrevision/precision/batch/resolution/fulltextencoder/VAE边界、CI/repeat/seeds共享策略，不能补生产SLO。T1 baseline50NFE25.25s/2990.96TFLOP。JiT18NFE6.02s/706.17(表Speed4.24为FLOP比，墙钟约4.19)，11NFE3.67s/423.26(表7.07为FLOP比，墙钟约6.88)，非可互换。11NFE CLIP-IQA .6139→.5397、ImageReward1.004→.9746、HPS30.39→29.02、GenEval.6565→.6457均退，仅T2IComp .4836→.4961增；18NFE HPS/GenEval也退，不照录nearly lossless/allartifacts无。不同baseline NFE/FLOP近但walllat不同，不能据FLOP匹配授同请求总费用。

B.5 553GenEval×4seed=2212、2400T2I×1=2400合4612images，非20participants/1000独立生成trial。§4.4 20people×50prompts共1000preferencevotes，多baseline表却未细分每row票数/同受试相关，且不与50NFEvanilla做该人审表，不能由偏好较加速基线优授原50NFE无损/CI。T3 HPSv2 .2690口径不同T1 29.77，T2I .3727也不同.4991，未公开匹配population/schedule/normalization，分别保存不混；去SAG inactivevelocity0、去ITA固定grid、去DMFtarget忽noise均退受限两proxy，没有matchedfullcost或component独占因果。

C仅caption/text：2stage大突变/4stage过晚全grid残噪、20/50%激进语义退 vsdefault35/62、50/75较保守质量但贵，非已读pixel/最优schedule证明。D Qwen-image26.95→6.51s、HunyuanVideo1830.21→423.52/268.12s仅作者延迟和定性展示，没有独立视频quality/temporal指标与完整3D interpolation配置，不认证motion consistency或所有modality。训练free仅无需新权重训练，profile/schedule调参/quality回归照计；原fulltokens/fullNFE与static已验schedule合理退路。

## actual唯一owner、已有与真实差额

ROADMAP `MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。实际1242–1314完整mismatch/离散sampler/representationguidance→dynamicpatch(2602.16968)→nonuniformlearnedrepresentation(2603.06351)→少步student边界。现dynamicpatch需要embedding/LoRA适配，nonuniformbranch先full-gridencoder后短denoiser再full-griddecoder；已有质量/全部费用分责。**未含原frozen DiT跨step nestedanchor、inactive仍以插值velocity演进、newanchor clean/noise target重造**，不以一般sparse/Flow近似NC。Ch54生成 serving优化只cost交接，不另写owner；Ch26 DepthCache观测token压缩不生成Flow state亦不是同family。拟放nonuniformrepresentation两段后、因此直接缩步/少步student段前两段，保新旧约束与回退链。

### 逐字PRE

另一条空间加速分支不先训练新patch接口，而在原生成器上维护完整latent与逐级扩大的anchor集合：每步只将当前anchors送入DiT，将其velocity嵌回原位置，再为空缺位置插值，使未实际求值的状态仍沿近似场演进。准备加入新anchors时，由上步预测clean latent的空间prior与当前noise幅度构造该位置target，再转入较大集合。Selector保原位置，lifter不改已计算anchor值；这只保证与少上下文的计算结果一致，不等原完整attention场或真实中间分布。Clean proposal、noise/seed、active集合、插值与transition schedule须和完整state一起标识，不能把少tokens或相同noise幅度当作语义/统计无损证书。

[JiT的有限必要原证](https://arxiv.org/html/2603.10744v1)支持这一training-free sampler选择，但有限时间micro-flow的limit与伪代码直接target赋值不是已核连续实现，局部velocity variance也只提名新增位置。单A800/FLUX对照的FLOP倍率不等墙钟或完整请求收益，较激进分支的多项质量指标仍低于50NFE，晚加入细节与过稀初始集合亦会退步。完整latent、邻域插值、排序、状态重造和VAE都计费，profile与schedule校准也不因无训练而免费；细节/结构、target分布或真实quality-cost验收失配时，增加保留集合、提前全网格或回退原full-token sampler与已验steps，而不由投影恒等式签发artifact-free生成。<!-- source-family:SF-2026-ARXIV-2603-10744 -->

## 精确停点

5分必要Source/actualCh24/PRE ready，等待非作者真实原件/owner/PRE裁后root窄写；未formal/POST/DAY。没有读取v2/外部扩池、图视频pixels或执行代码，未披露普通artifact不标外部阻塞。
