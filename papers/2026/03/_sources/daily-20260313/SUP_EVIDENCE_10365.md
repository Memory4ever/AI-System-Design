# GAE 10365：紧凑语义teacher与pixel bottleneck的Source/PRE

仅03-13补Mar12 BJT。第三完整exact-v1题摘/准入及日级夹证有效复用；本日 `SUP_ABS3_10365.txt` 题名/三作者/完整AB/Comments/history直接再核，无当前可见撤回/纠错说明，不证明全版本史。v2 Submitted Mar12T12:00:55不自行认证重要公开修订，本包只v1。`SUP_CORE_10365_MANIFEST_RESULT.json` 官方 https://arxiv.org/html/2603.10365v1 GET200/290090bytes/UTC2026-10-09T16:42:44.588266Z，raw/txt本日留存。

## 具体增量与投入

重构导向低维codec与高维VFM的语义监督维度不同，监督encoder中间层不保最终压缩接口→先由frozen DINOv2训练可学紧凑feature encoder/辅助feature decoder，再丢弃后者、冻结前者，用同维输出监督pixel AE的normalized bottleneck→改变语义target生产者、pixel codec与后续生成消费者的接口身份。不是借semantic alignment、RMSNorm、噪声鲁棒或rate-distortion成熟原则本身计新贡献。

拟Design2+Reach1+Durability2=5：重要的紧凑teacher/监督位置替代设计，单codec及受测生成路径，teacher/codec/消费者版本与训练代价可复用。标准门槛，actual Ch23具体缺口及“RMSNorm等Gaussian KL/防collapse”强保证反侧需必要局部深入，已读足拟采用两段；不采普遍最优/无KL统计正确/10倍全费用。Source/PRE ready待非作者，不formal/不写Books。

## 实际读到哪里

直接精确v1 title/AB、§3.1–3.2/Eq1–3完整、§4.1–4.2/Eq4/Table1–2完整、§5setup/§5.1–5.4.3/Tables3–8与§6完整、直接相关D/Table11、E/Table12、F/Alg1、G/Table13完整、H完整、I/Table14完整。图只正文/caption，未看pixels/curve精点，A/B/C无关视觉/扩展附录未遍历，无代码/复现，也未做v2差分。早先多段大输出截断部分已定点补读，必要main Table3和G/H/I现在读足，不沿未读附件造外部受阻。

## 机制与关键反侧

§3 ViT-L pixel encoder→linear Ap→parameter-free RMSNorm产生μ，decoder读z=μ+|σ|ε；σ∼N(0,Cσ)由原文称noise scale/latent std，记录原notation，不混成每样本posterior variance估计。L1+LPIPS+GAN与MSE(μ,Esp(fDINO(x)))，λrec/lpips/gan=1/1/.5，去KL直接改变训练目标与latent prior，非Gaussian KL的等价求解。

§4.2 frozen DINOv2-L patch→attention/patch-wise joint channel projection得到32/64dim；4-layer Llama-style feature decoder用negative cosine重建原feature方向，先预训练Esp/Dsp后discard Dsp/freeze Esp用于pixel AE supervision。AppendixF window partition→(w²C)×(w²d)投影→window reverse仍是H×W×d，不把“downsampler”补成缩空间token数。Cosine recovery不保feature幅度/所有信息；冻结teacher仍继承原VFM盲点，非语义truth。

§4.1同ViT-L/frozenDINO、64k样本SVD、60epochs pilot：pre/post/latent rFID .40/.48/.51，LP20.9/60.8/63.2。较好compact LP以较差reconstruction换，不授所有维度最优。Table1 DINO83.7与compact LP的评价池化不同：I明确低维flatten、高维GAP，Table14 GAE32 flatten69.4/GAP43.9，DINO1024 flatten77.5/GAP83.7。Table2 PatchConv flatten75.6胜SingleAttn62.8，但Table14 GAP48.9低SingleAttn51/AttnLinear52.3；不是所有readout下“spatial-aware必需”。教师DINO vs MAE Table11 gFID2.36 vs4.20，DINO重构.45劣MAE.36，有限对照不唯一识别语义分数因果。

原文§3声称RMSNorm投unit hypersphere/防collapse，必要数学资格：常规parameter-free RMSNorm把v除sqrt(mean(v²)+ε)，非零且忽ε时norm为sqrt(d)，非unit除非另1/sqrt(d)；定norm的所有样本可同向同值，不能凭norm排collapse/证well-distributed。拟只采用数值尺度接口，不采用该强主张；无需因此推全部有限机制失效。Table7无semantic loss、KL单weight.1与RMSNorm比较rFID .977/.764、gFID16.72/12.55，缺同等调参Gaussian objective，不授全部VAEs或KL无效。

§5.2 Cσ增强时gFID可降，但Table4 GAE32 .05/.1/.2 rFID.37/.45/.57、PSNR/LPIPS/SSIM均趋差；不是无代价鲁棒。Table6 λsp0/.5/1/2 LP5.74/63.5/69.2/71.4，gFID12.55/2.35/2.36/2.45，不单调；λ1对.5部分reconstruction更差。T8 ViT-L rFID.45劣B.41，gFID2.36略好B2.43，非更大处处更优。T5 GAE64 LP78.3胜VTP73.9、rFID .38劣VTP.36，不写重构全面SOTA。

## 条件、评价与费用

ImageNet1K256×256/32或64channels，pixel AE200epochs/batch1024/AdamW；G Table13 pixel约250k iters/teacher10k/batch2048/4layer51.41M辅助decoder，generation1M迭代/batch1024/675.26M。pretrained DINO、teacher训练/全feature forward、pixel AE与denoiser训练全部计费，80vs800denoiser epochs不是端到端10倍降本。hardware/precision/repeat seeds/CI/full wallclock/总GPU-hours **Not Disclosed**；paramcount/iter不能补这些值。

LightningDiT-XL LR2e-4/EMA.9999，800run启QKNorm而80run关闭；32dim main800 timeshift.4/CFGinterval.3/weight3.3，80 .4/.25/2.5；64 timeshift.5。main无CFG用SDE、有CFG用ODE，250steps/class-uniform/50k eval；ablation AE100epochs/Cσ.1、80epoch DiT无QK、无CFG ODE250steps/timeshift.7/random labels，与main Cσ.2/SDE并非同population。报告各协议，不混不同guidance与epochs。

Table3无CFG800gFID1.31、CFG1.13有限作者结果，RAE1.13星号用AutoGuidance且839M（GAE675M），不能宣称相同预算下普遍领先；80gFID1.82对VAVAE800只体现所报优化阶段而非全部费用。评价generation precision .80对若干.82/.83更低，CFG.79也非各项统治；E是原CFG搜索额外费用，不以最优gFID消除多重配置/real quality验收。

## actual唯一owner与具体差额

ROADMAP `MULTIMODAL-REPRESENTATION` [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。actual 174–208共享codes/语义与重构分责、320–380从统一visual责任至rate/distortion/consumer/noise codec、383–423完整Artifact与decoder/generator验收近文直接顺读；Ch24 45–66完整RAE-AR表示→autoregressive消费者边界只交接。Ch23已有codec/noise误差人口、teacher/index与reconstruction分账，但未含**独立预训练compact semantic target、discard辅助feature decoder/freeze生产者、pixel bottleneck同维监督**；新分支不是把已有关联重新贴GAE。RMSNorm/noise原则已有，故不另把它们算新系统层；归属Ch23，Ch24只消费生成接口，不二次owner。

拟放Ch23 rate/distortion图后、现“同一视觉表示既供理解…”全局/局部压缩接口之前两段，保原联合容量链与后续解压选择；不拆已有段落。root协调窄锁后才实际写入。

### 逐字PRE

高维视觉teacher能读出语义，却不保证像素codec压缩后的瓶颈仍携带同一信息；在encoder中间层监督和把短latent再展开后监督，拥有的是不同接口。一条受限分支先用冻结VFM的patch features训练紧凑feature encoder与辅助feature decoder，再丢弃辅助decoder、冻结紧凑encoder，把它输出的同维target直接用于pixel autoencoder瓶颈。这里的patch-wise投影压缩channel而保留空间网格，cosine feature recovery只提供训练代理，不签语义真值或无信息损失。Teacher/downsampler、pixel encoder/decoder、normalization/noise与后续生成器须分别版本化，不能因同shape就当consumer兼容。

[GAE的有限必要对照](https://arxiv.org/html/2603.10365v1)支持这一监督位置分支，却同时显示语义probe、像素重构与生成质量并不处处同向；flatten与pooling可改变probe排序，较强噪声或监督也会牺牲重构。去KL、固定RMS尺度与随机noise是改变codec目标，不等Gaussian prior、防collapse或任意generator都好学的证明。预训练teacher、feature/pixel训练、denoiser与guidance搜索均计费，较短denoiser训练和局部gFID不能当全费用下降；下游generation、细节或真实质量—成本验收失败时，保留原VAE、静态alignment/原高维teacher或原codec操作点，而不由定norm与probe通过批准新表示。<!-- source-family:SF-2026-ARXIV-2603-10365 -->

## 精确停点

必要Source、actual唯一Ch23差额及逐字两段PRE ready待非作者。五分/深入是拟实际投入，未计确认formal、未写Books、未自授PRE/POST/DAY；无外部正文阻塞。可直接核上述必要原件与owner，不重读有效AB/day/第三全池。

### 后续已核终态（覆盖上述ready停点）

mar13_admission_review非作者必要v1/actual Ch23/两段PRE PASS，第二段仅采用“原高维teacher”；root实际联合rate/distortion图后两段及本人注。本作者非Books writer实际完整332–360局部/348与350新段/1289本人注回源POST PASS见SUP_POST_10365.md，root已同步本人注PASS并释放锁。5分必要局部深入、受限Ch23整合已正式同步本日报第26项；不授DAY。
