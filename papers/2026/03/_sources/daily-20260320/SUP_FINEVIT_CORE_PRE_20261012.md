# FineViT2603.17326：03-20补03-19必要证据与最小PRE准备

准备者：resume_review17_18。只本日已准入family，原2+2+2=6保持；此文件是准备，不自授Source/PRE PASS、实际Books整合或DAY。尚未获root Ch23窄锁，不写Books/Report/LS。

## 1. 身份、窗口与实际必要读取

- [FineViT: Progressively Unlocking Fine-Grained Perception with Dense Recaptions exact-v1](https://arxiv.org/html/2603.17326v1)，[官方abs](https://arxiv.org/abs/2603.17326)。本日原有限尾准入/date有效复用；本次actual current abs完整AB/十三作者/history仍单v1，Submitted03/18不当firstpublic。原必要DOI匹配title/url、created03/19T02:29:30Z/registered31Z已实际读回，结合本日日级夹证而非独拿注册作公告。
- actual精确HTML初次网页读取失败，PDF24MB超过网页工具上限；一次PDF恢复超时所得不完整文件未作为证据、未读PDF页或图片。随后同一官方exact-v1 HTML经下载HTTP200完整恢复，方法与必要评价可读，不需要外部缺口、反复试站或另找版本。
- actual必要HTML：§3.1–3.3/Eqs1–3/Tables1–2；§4.1/Table3训练设置；§4.2/Tables4–6；§4.3/Tables7–8与checkpoint/frozen说明；§5限制；B.1–B.2决定性下游训练协议。恢复HTML原行322–481、488–1275、2272–2318对应这些范围。无全references、AppA图集、代码或所有图片，未复现。
- 本次恢复实际重读AGENTS、Research/Report合同、Sources使用/Daily/arXiv、统一Prompt、ROADMAP、本日README窗口/STOP及Books写作上下文。只本20；共享章节邻接不重开邻family原证。

## 2. 支持的机制与不能直推的桥

§3把vision encoder的训练从原始视觉目标，经全局图文pair，转向显式局部地址与文字目标，而不是仅把caption延长：

1. 28层0.86B、patch14、2D RoPE、输入尺寸按28倍数调整。第一阶段75% masking/256²，重建DINOv3 teacher在masked patches的feature MSE（Eq1）。视觉权重从零初始化不等没有预训练先验：DINOv3、SigLIP2 Giant文本encoder及LLM都提供已有监督或能力。
2. 第二阶段由前一visual checkpoint初始化，SigLIP-style image–global-caption pair分类目标（Eq2）；文本encoder先冻结后联合更新，native aspect/resolution贯穿此阶段，max336²→448²、文本64→256。它建立图文检索对齐，不给每一区域发出语义真值证书。
3. 第三阶段max1K，projector把视觉表示接入LLM，用AR target联合global与region QA（Eq3），包括bbox→string、string→bbox、bbox→OCR、OCR→bbox。Table3此阶段vision/projector/LLM均trainable，不能冒充固定encoder的纯readout训练。
4. 局部描述由global nouns→GroundingDINO候选box→置信过滤/NMS/频率采样，再向Qwen3-VL同时提供crop和整图context；rich-text/document OCR用PaddleOCR替换或补充。它改变监督对象及空间地址，不是局部裁剪天然可靠，也不是caption/box/OCR都是真值。

数据单位必须分开：1.8B unlabeled source images，第二阶段1.56B unique recaptioned samples与Table3的9.3B samples-seen不同；第三阶段63M global-caption images，226M local regions、142M rich-text OCR与86M document OCR共454M region records，不能改写为450M独立图像/对象或同数量独立正确标签。实际primary主张只采用训练接口，不采精确全配方、无偏监督或组件唯一因果。

## 3. 决定性评价、直接反侧与费用

- Table4全局分类/检索有混合表现：FineViT ImageNet-v2 75.5低于两SigLIP2比较项78.7/79.8，ImageNet-val84.2也低于g1B的85.0；更好的部分retrieval不授全部task更好。Table5长caption检索的模型/数据/预算并非全匹配，不给统一同预算收益。
- Table6主MLLM结果还包含第三阶段后80M QA SFT，模型和人口与其他系统不同；Hallusion/MMVet/MMMU/OCR等有反退，不能归因于视觉encoder一种目标，异质任务的平均也不是统一truth率。
- Table7/B.2是真实较受控的**冻结encoder下游消费比较**：同max1000²、10M InfinityMM训练两层projector，再6M SFT训练projector+Qwen3 LLM（1.7B或8B），encoder保持冻结。1.7B general平均51.78 vs50.93但若干任务更差；8B general平均59.78低于SigLIP2-naflex60.30，local平均73.49 vs67.15也不覆盖每个local任务（AI2D77.23<77.49）。有局部效果，不宣全消费端无损。
- Table8/B.2的阶段checkpoint比较**不是同样的冻结probe**：各checkpoint先10M projector训练，再8M global caption联合vision/projector训练，最后6M SFT全参数训练。阶段效果混有后续适配；不能把表8叫原checkpoint独立因果或仅局部QA带来的变化。Stage II相对I的RefCOCO/+/g从77.93/66.47/76.59退到72.93/63.18/69.51；Stage III局部平均改善但MMVet36.65→35.83退步。支持全局与局部目标分验，而不是“所有阶段单调增强”。
- native resolution、数据/目标、训练时长和下游读出同时变化；未提供能将所有收益分解给单一组件的匹配消融。teacher feature、合成caption、detector/OCR均非独立事实grounding。静态图像证据不授video temporal、行动或安全能力。
- Table3披露BF16、DeepSpeed ZeRO2、AdamW/cosine和阶段batch（4096/49152/4096）；B.1的80M SFT两阶段batch1024/512、maxlen4096/10240。必要范围未给完整GPU配置、训练与标注总墙钟/成本、consumer concurrency/SLO、推理端到端预算和CI，记Not Disclosed而不是便宜/免费。MIM teacher、三模型global recaption、region检测/OCR与过滤、三阶段训练、高分辨率tokens、后续projector/LLM SFT和独立回归均需结算。

## 4. 实际唯一owner、现有覆盖与两段逐字PRE

sole owner：`MULTIMODAL-REPRESENTATION` / [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。actual完整局部740–798已读：concept/readout分支→Caption辅助/scene IR→DeBias-CLIP长caption首句与位置偏差→三种alignment目标→DCR监督接入空间。现有DeBias段已分开全局检索与细节覆盖，DCR和后续patch监督也解释多目标，但尚无这里**全局image-caption pair→显式bbox/文字双向QA空间地址**的训练目标差额及**frozen consumer比较和继续训练checkpoint比较不同权限**。因此拟最小两段，不重复整个数据管线或长caption原则。

拟位置：当前DeBias-CLIP完整段及marker后（现L771）/“跨模态alignment至少包含三种不同目标”前。actualCh23开篇1–28、完整740–798；Ch24开篇1–38仅生成范式交接；Ch27 collection protocol55–79及ROADMAP训练系统分责已读。Ch27拥有采集/标注治理，不复制teacher/DINO和数据管线；Ch24接生成概率路径，不把本文caption训练改叫world/action或生成范式替代。

### 正文PRE 1

全局图文配对足以支持类别与检索时，不必为每个区域追加地址监督；但把caption写得更密，仍不保证视觉encoder保留了可供语言模型定位和描述的小区域信息。一条受限训练分支先用masked-patch教师特征初始化视觉表示，再训练全局image–caption配对，最后经projector接入语言模型，以区域框到文字、文字到区域框及OCR的双向任务直接监督空间地址与描述，同时保留全局目标。局部caption还读取整图context，框与OCR来自模型生成和筛选，不能把这些target当独立视觉真值；从零初始化视觉权重也没有取消教师与语言预训练先验。改变的是监督粒度、输入分辨率和consumer接口，不是证明长caption、对比目标或冻结encoder已经过时。<!-- source-family:SF-2026-ARXIV-2603-17326 -->

### 正文PRE 2

这条分支须把全局检索、区域定位/OCR与语言回答分别验收。[有限原证](https://arxiv.org/html/2603.17326v1)既比较冻结encoder后的相同下游读出，也比较继续更新视觉模型和语言模型后的阶段checkpoint；后者不能作为未经适配表示的独立因果证据。全局阶段出现grounding退步，局部阶段与更大语言consumer也仍有任务反退，平均改善不签发全部细节、事实或行动能力。教师与caption/检测/OCR制备、多阶段训练、高分辨率tokens及后续SFT和回归都付费，完整硬件与端到端预算未披露；局部标签失真、任务回归或预算不允许时，保留原全局encoder、冻结读出、真实区域监督与专用OCR，而不让新增训练目标代替独立质量验证。

### 静态来源注PRE

- [FineViT2603.17326 exact-v1](https://arxiv.org/html/2603.17326v1)：必要§3.1–3.3/Eqs1–3/Tables1–3、§4.2–4.3/Tables4–8、§5与B.1–B.2。只采用全局pair到显式区域/文字地址QA的表示训练分支及frozen readout/继续训练checkpoint权限区别；保合成监督、数据/分辨率/后续SFT混杂、任务反退与全费用，不授全部下游无损、独立因果、完整recipe、时序行动或部署SLO。未核代码、图片或复现。<!-- source-family:SF-2026-ARXIV-2603-17326 -->

## 5. 非准备者裁决待执行

请resume_mar17实际必要Source、上述actual owner/两literal PRE/static有限核。通过后才由root协调Ch23唯一family窄锁；没有actual写入、不预计I或DAY。原证支持与直接反侧已够此次拟命题，停止扩大附件读取。

## 6. resume_mar17 非准备者有限 Source / PRE 裁

2026-10-12：实际精确v1 HTML网页本次可恢复，独读§3 L89–138、§4/T3–8 L139–271、§5 L272–279及B1–2 L428–445，未核全部图、PDF或复现。两literal/static有限PASS：MIM teacher→全局pair→bbox/string/OCR双向QA地址监督，以及Table7冻结consumer和Table8后续更新vision/projector/LLM的权限差额真实。Eq1–3、151的trainable模块和442–445后续协议核对准确；T4 ImageNet-v2反退、T7更大consumer general/AI2D反退、T8 StageII grounding与III MMVet反退均真实，近文不能称单阶段单调或组件唯一因果。合成局部caption确读crop和整图，新增框/OCR target非独立真值。

实际Ch23完整740–798/开篇、Ch24开篇和Ch27 collection55–79顺读。DeBias完整段已承载caption首句/位置偏差，却未承载区域地址与文本双向QA训练及两种下游验证权限；原拟DeBias完整marker后/三alignment目标前两段差额成立。原6/date复用，不全recipe、从零无先验、时序/行动或无损部署外推。root授新sole锁后写，一次非writer实际正文/完整邻接/本人静态注POST才计I，不授DAY。

## 7. root授权后的实际writer落实（非POST）

2026-10-12 root已接纳§6author非准备者有限PASS并授resume_review17_18 sole Ch23家族窄锁。writer实际读当前758–799完整前后及末14行后，仅按原两literal实写773/775、static1782；写后758–800与1774–1782本人/S-VGGT/Identity/MoBa邻注完整顺读，DeBias→区域QA分支→三种alignment及DCR的衔接保留。两正文与static逐字回原PRE不变，章numstat102/0→108/0只新增本family六行，限定diff-check无输出；未改其他正文/注、未stage/commit/push。

以上只有writer读回，不授actualPOST/I/DAY。请resume_mar17一次nonwriter实际773/775、完整758–800及1774–1782静态本人/邻注回有效原证/PRE，root接纳后释放，不改书注过程身份。

## 8. resume_mar17 一次非writer actualPOST

2026-10-12：实际完整Ch23 758–800、新773/775和1774–1782本人/邻注回读，逐字回原§4两literal和有效必要Source；有限POST PASS。DeBias caption首句/位置偏差→新增地址QA监督/两种下游权限→原三alignment/DCR链顺读成立，未替代全局encoder或签发独立真值、全部任务无损/单组件因果。源注静态范围与已核v1准确，反退/预算近文；限定diff-check无输出，不更改Books过程身份。root接纳后释放soleCh23并计I；此非报告作者DAY验收。
