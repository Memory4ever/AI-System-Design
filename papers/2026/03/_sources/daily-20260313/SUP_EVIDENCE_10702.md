# UniCom 2603.10702v1：必要 Source / actual Ch23 差额 / 两段 PRE ready

仅03-13补充窗口2026-03-12 BJT自然日。本家族完整exact-v1题摘准入§19有效；root本次已实际读SUP_DATE3_10702.raw全部字段与本ID完整v1题摘，补正§23漏列。SubmittedMar11T12:14:26Z不作public，正常公告批次下界与arxiv.content/findable registeredMar12T02:07:50Z（created02:07:49）上界支持本arxiv当日事件；UpdatedMar12T00:46:14Z与Available月份不用于公开证明。当前可见v1无Comments/venue/撤回/纠错信号，不声称全网无早稿。

官方https://arxiv.org/html/2603.10702v1，SUP_CORE_10702.raw/txt及SUP_CORE_10702_MANIFEST_RESULT.json，GET200/452730bytes/UTC2026-10-10T02:51:10.550283。实际读§3.1–3.3完整机制/Eq1–5、§4.1/4.2 decoder与完整Table1、§4.3.1–4.4全部消融/完整Tables4–5、§5、AppA1–A3/Table6训练预算和AppG直接限制。Figure4/6–8只读caption/作者解释，不认证图像像素或曲线精确加速；主SOTA生成/编辑Tables2–3、附录全样本/代码未展开，不采其全榜优势或部署/复现。必要支持与直接反侧够即停，不遍历附件/旧codec。

## 实际增量与评分

现有连续语义feature可给理解却让生成prior承担高维分布→本稿在冻结SigLIP2上先联合训练channel compressor/decompressor与重建diffusion decoder，再固定codec训练prior，并把空间token数与channel维数分开对照→需要分别决定生成目标压缩轴和理解消费者是否绕过压缩，而不是把统一backbone或相同encoder当无损统一证书。

拟2+1+2=5。D2只计受局部控制对照支持的压缩轴/消费者边界，R1是表示组件，Durability2是可复用的producer/consumer操作点条件；不把成熟MHA/MLP、Transfusion/Flow目标、VAE-free标签、SOTA或能映射多章抬分。当前Ch23有具体长期知识差额，触发受影响内容必要深入已实际完成；准备者不自授Source/PRE/Books/POST/DAY。

## 原机制及不可补造之处

§3.1分解P(x|c)=∫P(z_tilde|c)P(x|z_tilde)dz_tilde；§3.2冻结语义encoder产生N×D表示，浅MHA与decoder共同重建，随后§3.3明确compressor和diffusion decoder都冻结，prior预测其固定latent。SigLIP2-SO400M-Patch16-NaFlex D1152→d64、动态N最高1024，维数缩18倍不是token序列缩18倍，更不是完整attention/FLOPs下降18倍。压d并不改变N²注意力项；实际runtime/precision/totalFLOPs未给，不替作者推精确费用。

§3.3 PathI文本causal、同image latent双向，全Transformer可训；**理解直接输入未压缩Z**，编辑输入压缩latent。它同时写后者reduce context length，但Eq1形状N×d与同N对照并不支持仅压d就减少序列位置数，本包不静默补拼接实现。PathII是frozen MLLM/MetaQueries/trainable connector，与全训PathI梯度/容量不同；共享codec不足证明其差异唯一归因空间query瓶颈或某架构。§4.3.2另评纯compressed/concat理解，不改称最终部署理解端已全部压缩。

## 关键局部对照与直接反侧

完整Table4 ImageNet50k：1024×1152原.40/23.26/.69；256×1152 .72/20.29/.56；1024×256 MLP .62/21.73/.66；1024×64 MLP .55/22.17/.66；同形MHA .56/22.61/.69（rFID/PSNR/SSIM）。这一有限不同操作点支持保N、压d的选择，不是同总bit/FLOP预算实验：256×1152与1024×64的scalar数294912/65536不同，也没有latent量化bit率。MHA的rFID .56比MLP .55略退，不说所有重建指标严格胜出。Table1另一full模型人口原d1152 .38/22.60/.61、d64 .42/22.28/.61；不同512分辨率FLUX-VAE .06/33.65/.93，不能跨分辨率证明接近无损/保真等价。

完整Table5（GQA/RWQA/SEED/MMMU/ChartQA/OCR）：baseline65.25/64.31/74.63/44.56/69.04/55.40；MLP62.80/60.39/69.92/43/56.8/31.7；MHA64.01/63.14/71.75/44.11/62.12/36。MHA比MLP局部均好，但**纯compressed仍全部低于uncompressed baseline，OCR55.40→36不是无损**。Seq concat65.03/64.58/73.62/43.33/69.24/55.50混合升退，增加完整feature不能作compressed-only证据，双表示context/投影费用另计。t-SNE六类别×150图的聚类不认证通用语义同一或可逆。

§4.3.1正文约5×、Fig6caption3.8×训练收敛口径不一致；只读caption没核曲线，不采用任一精准端到端加速。§4.4控制init VLM-vsLM与PathI-vsPathII的作者现象可以保为局部描述，不证明semantic feature是唯一原因或Frozenquery普遍逊。无平均延迟、concurrency、SLO、总GPU小时/功耗/硬件/precision、完整数据规模/seed/CI，均Not Disclosed；理论可逆、所有域保真或生产能力均未授。

AppA1 frozen视觉encoder、FLUX.1-dev初始化，codec+decoder内部高质量数据、33aspect buckets1:4到4:1/1024基准，global batch256，10K作者说较快收敛但实际训50K细节；AppA2 Qwen2.5-7B-Instruct、两层投影，alignment阶段MLP和LLM都训，非仅小connector适配。Table6 alignment/PT/CT/SFT steps20K/115K/60K/7K，AdamWβ.9/.95 eps1e-6，LR2e-5/1e-4/1e-4/1e-5；后3阶段diff:text5:1，数据sampling分别变化，不合并codec与prior训练为免费复用。AppA3消融用reduced内部图像/filtered T2I，不能自动代表全统一任务。AppG细粒度信息损失与高分辨率资源限制保留。

## actual唯一 owner / 具体 gap / handoff

ROADMAP唯一MULTIMODAL-REPRESENTATION Ch23。实际顺读连续表示245–256完整上下游：原段解释continuous局部信息/无离散vocabulary/decoder/encoder几何；SemanticVocoder段解释音频semantic anchor→waveform生成器细节责任与重建负侧。另实际337–355统一视觉责任与rate/distortion/capacity图的完整局部：现文已有结构/语义/纹理分工和总rate联合成本，**没有本稿固定N压d的局部操作点与理解raw bypass/纯compressed OCR退步证据**。不是主题缺口，拟在SemanticVocoder完整段后、离散表示标题前插两段，仍保音频分支与离散回退。Ch24只交接FM/prior采样，不再新增owner；Ch28只消费训练混合费用，Ch66只消费回归人口。

## 逐字两段 PRE（仅提案，root协调写）

连续语义表示用于生成时，压缩轴也要先分清：减少空间 token 数会删去位置容量，降低每个 token 的 channel 维数则保留位置数量，但仍改变局部可携带的信息。一条受限图像分支在冻结视觉 encoder 上，先联合训练 attention compressor/decompressor 与重建 decoder，再固定两者训练 latent prior；它在所测操作点选择保留空间序列、压低 channel，而不是证明注意力层天然无损，或 channel 缩减等于序列/端到端计算同比缩减。生成目标、理解输入和重建 decoder 因而应分别携带形状、冻结版本与训练责任。

共享语义 encoder 也不能消除消费者分流：[UniCom 的受限对照](https://arxiv.org/html/2603.10702v1#S4.SS3)中，纯压缩 MHA 比 MLP 的局部理解分数更好，却仍全部低于未压缩 baseline，OCR 从55.40降到36；正文 Pathway I 的理解路径直接消费原 feature，编辑/生成使用压缩 latent，拼接完整 feature 的回补也不等纯压缩证据。不同空间/channel 操作点没有匹配总表示预算，重建指标仍有反退，精确收敛倍数口径不一，不能授语义保真或普遍加速。Codec/decoder 预训练、prior 多阶段训练、双表示投影和实际 decode 均计费；细节任务或总成本回归时，保留原连续 feature、理解/生成双表示与原 codec 操作点，不以统一 backbone 自签接口可逆。<!-- source-family:SF-2026-ARXIV-2603-10702 -->

当前最小停点：5分受影响内容必要深入ready；等待非准备者实际Source/现owner/逐字PRE核。通过后root仅此两段窄写、非writer实际POST；当前Books新写0，未formal/未DAY。
