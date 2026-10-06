# SemTok16373：必要原证、实际 owner 差额与受限 PRE

仅本19既有具名材料，resume_mar17准备、非日报作者；2+1+2=5保持，具体codec差额及loss/消费者边界需局部深入。复用本19刚实际重载的AGENTS、研究/Report合同、统一prompt/ROADMAP、每日与arXiv来源主题；本篇实际重载README/STOP，Books背景、目标及相邻交接已读。只准备packet，不改Books/Report/LS，不扩FrameRepeat或其他发现。IOMM root一次实际POST已通过/释放，不重开其原证或静态身份注。

## 身份、日期与必要 Source

标题Semantic One-Dimensional Tokenizer for Image Reconstruction and Generation；完整题摘原SUP_AB_16373_20261011.json。日期复用SUP_LATER_METADATA_20261011.json:890的arxiv.content findable、created/registered 2026-03-18T02:30:49Z与已校准availability下界，非Submitted03/17T11:01:08Z=公开时刻。[当前官方事件页](https://arxiv.org/abs/2603.16373)实际header/Comments/history仅v1、18 pages/12 figures，没有所见撤回/具体勘误信号；不全站/全版本追查。

必要实际[exact-v1 HTML](https://arxiv.org/html/2603.16373v1)：完整题摘、§3.1–3.3/Eq1–8（约117–193），§4.1–4.4/Tables1–6及§5（194–309），A.1–2/Tables8–9的实际decoder/位置/生成消费者（389–420），B.1/Tables10–12直接反侧（423–446）及B.3限制（480–484）。另工具带出B.2/Tables13–14等文字只保实际看见的局部bit classifier/random-order观察，不冒全部B.2图像/最优sampling复核。未读全部可视化/代码/旧版，未复现；支持与直接反側够有限采用，停止扩读。

## 方法身份及采用边界

§3.1/A.1：SD3.5-VAE先把图像降采样8×，MMDiT encoder同时消费2D latent patches与K个learnable 1D slots，通过双分支交互形成离散瓶颈。两路仍使用2D/1D RoPE，不能把1D称为无位置、逐token语义坐标天然唯一或空间信息不需恢复。SigLIP预训练特征向2D encoder输出提供空间对齐蒸馏；其pooled表示与量化后一维分支的投影形成同图对比约束。本文不是只在量化前监督，也不是先冻结紧凑encoder、再把内部target给另一个codec的GAE接口；所读范围不明确teacher/StageII全部冻结集合，不自行补造。

§3.1采用BSQ/sign/STE、二值球面量化，码本组合数2^d不等实际有效语义容量/独立bit或无需存储全部模型。§4.1却写FSQ，Tables1/10和方法写BSQ；Eq2打印positive log-ratio后纳入min，与文字对比语义有符号桥，Eq3 bit index的字面端点也不适合作精确实现recipe。本次采用文字清楚的双分支语义约束及codec训练接口，不采用这些精确loss/code索引、复现承诺或teacher完全无偏。问题保留一次请求，不因未采用精确recipe遍全代码/附件。

§3.2：第一阶段以quantized 1D tokens为条件、noisy VAE latent为目标学习flow decoder，同时联合更新encoder/quantizer/decoder目标。第二阶段将decoder原2D noise输入换成learnable masked slots，以像素MSE/感知/GAN目标细化重建；A.1明确decoder预测latents后仍经VAE decoder返回pixels。decoder继承SD3.5参数、约2236M，encoder约113M，非整个codec从零、非无外部teacher/prior。后阶段的一次refiner是重建消费接口，不是所有图像生成一次完成。

§3.3/§4.1/A.2下游消费者是class-conditioned ImageNet256 masked AR：双向LlamaGen派生Transformer，默认64steps填256tokens、random positions/cosine schedule、bitwise classifier和CFG/top-p sweep。1D shape不排除因果factorization，也不由其形式推出天然语义解耦；本文选择双向建模并不证明所有1D都须同样依赖。采用scope为固定K=256，未见可变K、prefix截断或跨分辨率验证；不把初筛“核可变token”变成已证事实。

## 对照、直接反侧与总费用

- Table1同0.070 bpp比较FlowMo-Lo与SemTok：rFID .95→.88、PSNR22.07→22.19，但SSIM .649→.639、LPIPS .113→.128退；2^32版本rFID.67伴随rate升至.125 bpp。256个token并不比全部256-token grid基线更短，不把“1D”直接写成token数或端到端compute下降。Bits-per-pixel是名义码容量×K/HW，不是已实现entropy bitstream、模型分发或全部存储成本。
- Table3同AR framework的codec替换支持有限消费者差额：gFID4.62/6.68→2.77，但Precision .84/.82→.78，Recall .49/.45→.60。不同codec继承prior和训练费不完全相同，不授1D本身唯一因果或全质量支配。Table2各AR容量/预处理/预算不同，不按榜单宣称普遍SOTA。
- Table4两路约束均启用时rFID1.08→.88、gFID3.83→2.77，支持局部语义约束接口；distill-only的IS264.9低于不加约束271.4，不能说任何配置所有指标改善，feature clustering非语义真值或通用理解证明。
- Table5 Raster→Global同时重构rFID1.22→.88和generation gFID3.08→2.77，不是仅改推理采样顺序的唯一因果试验，不能由此证明1D没有causal dependency。Table6 flow decoder→refiner的局部重构指标改善，支持阶段消费变化，不等无细节幻觉或完整质量保持。
- B.1 Table11联合LPIPS+ResNet的rFID .88较好，但PSNR22.19/SSIM .639低于LPIPS-only22.73/.649；perceptual proxy与像素目标仍竞争。Table12两阶段 .88对仅finetune1.80支持额外阶段有用，不是等总训练预算分离唯一机制；StageI200k×batch256、StageII100k×64、下游AR800k×2048都属额外训练消费，不能取消继承SD3.5/SigLIP/VAE训练费。
- B.3明示约2.3B generative reconstruction模块限制推理速度、只测ImageNet256重构/类条件生成，VLM理解、text-conditioned image generation和video尚未验证。一次refiner减少此decoder迭代，不消除latent-to-pixel/VAE decode或下游64step生成。继承pretraining、teacher、两阶段codec、AR、CFG/top-p搜索及真实encoder+decoder全费用均需计入；所读范围hardware/precision、完整延迟/峰值内存/重复运行区间和统一总预算Not Disclosed，不冒生产SLO或完整降本。

## actual owner / 具体差额

sole `MULTIMODAL-REPRESENTATION` Ch23。实际297–307已有channel-global code与nested prefix顺序，不是本篇固定learned slots；369–391完整责任分配→rate/distortion链，371讲topology关系/value语义/residual texture，389–391的GAE采用先训练/冻结compact teacher再给pixel瓶颈target。都未承载本篇“2D teacher蒸馏＋量化后1D对比、先条件flow重建再把decoder noise branch换learnable slots作像素一次细化”的接口，不按语义token主题记NC。建议375既有family marker后、377 Rate标题前原单段；保持相邻责任拆分及容量论证，不重复BSQ成熟原理。

实际Ch23 264–312和447–467已有离散teacher/consumer治理、rate与容量验收；本篇新增的是具体约束位置与codec阶段consumer切换，不授这些旧原则为论文独创。Ch24 1239–1247拥有generative pixel decoder的预算Gate，Ch23 1193–1201明确表示→Ch24生成交接；本项只写codec责任与接口，不在Ch24再解释flow公式/AR采样。Ch22入口1–18拥有通用长序列状态，非codec owner，不新增第二节点。

## 逐字 PRE（未授 Books，待 root 非准备者裁）

表示责任也可以沿训练阶段分配，而不只拆成并行的结构、语义与纹理通道。一个[受限二维到一维codec分支](https://arxiv.org/html/2603.16373v1)用二维视觉分支读取空间信息、可学习的一维slots汇聚离散表示；预训练视觉teacher分别约束二维特征和量化后一维表示，使语义抽取与瓶颈保存拥有不同监督接口。随后先用条件flow重建学习codec，再将decoder的噪声分支换成可学习slots、用像素目标细化为一次重建器；这是重建消费阶段的变化，不等于下游masked图像生成也只需一步。一维序列仍携带位置和decoder版本，固定256-token实验不授任意长度、可截断顺序或通用理解能力。局部语义约束与阶段对照支持这个分支，却仍有重建细节、生成precision和其他指标反退；不能由更低rFID或名义码率批准全质量支配。大重建器、继承的视觉/生成先验、teacher、两阶段训练与下游采样均计费，语义偏差、细节或完整预算回归时，应保留网格codec、单阶段重建、独立理解表示或原消费路径，而非让语义聚类和一次decoder自签可部署保证。<!-- source-family:SF-2026-ARXIV-2603-16373 -->

静态注：`SF-2026-ARXIV-2603-16373` — [exact-v1](https://arxiv.org/html/2603.16373v1)§3.1–3.3/Eq1–8、§4.1–4.4/Tables1–6、A.1–2/Tables8–9、B.1/Tables10–12及B.3；仅双分支语义约束位置与flow重建→一次pixelrefiner的codec消费接口。不采精确loss/量化索引recipe、可变长度、通用理解/生成质量或总费用保证；未核代码或复现。

## 停止与独核请求

## root 非准备者裁决（2026-10-11）

实际独读exact-v1 §3.1–3.3/Eqs1–8、§4/Tables1–6、A.1–2配置与B.1/Tables10–12；实际Ch23 369–391及Ch24相邻责任交接已核。双分支约束、量化后对比、flow重建到一次pixelrefiner的接口有独立原证，五分不变，差额深入充分。Table1细节指标、T3 precision、T4 distill单独IS与T11/12反侧均已保留；公式/量化名词不一致不进入执行recipe，不由聚类或rFID推理解真值、普遍质量或费用。原一段PRE及静态注PASS，只准在责任分配→rate/distortion之间写这一受限codec接口；不授实际POST/safe/DAY。支持及直接反证足够，不再扩附件、版本史或代码。

建议受限整合而非主题NC；原证支持与关键反側足，当前待root非准备者独核必要Source/actual唯一owner/原单段PRE，未授写/未POST/未safe/DAY。一次精确重开请求只针对未采外推：实验loss/量化名词与索引勘误、teacher及两阶段更新集合、独立理解/文本生成或变K消费者、含全部预训练/codec/AR与decode的同预算质量—成本及不确定性。受限正文、作者勘误或最小artifact可替代，不要求全代码/全附件。普通尚未批准不称外部受阻，不自开下一材料。

## root写后非writer actualPOST（resume_mar17，2026-10-11）

root写后本人实际顺读Ch23 369–395完整表示责任→rate/distortion交接（新正文377）、1716–1722尾部自身静态源注及Camera/f-CBM/FrameRepeat相邻注，并逐字回对已独核必要Source/原PRE。新段与PRE一致，二维/量化后一维监督位置、flow重建后一次pixelrefiner的codec消费接口准确；固定256-token、下游生成非一步、细节/precision反退及teacher/大decoder/训练/采样全费用近文，未采精确loss或量化歧义recipe。静态注只写来源/范围/边界，不复制验收身份，无代码/复现/普遍能力与质量保证。一次局部actualPOST PASS，可交root接纳并释放窄锁；本项五分保留，不授整日DAY，不需再次更改Book源注或重读核心。
