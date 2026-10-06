# 第二十三包：AB13 两项必要证据与具体 owner（待非作者复核）

35safe不增；以下只是作者必要审阅与拟处置，没有PRE/Books lease。原始精确v1、支持/直接反侧足即停，不遍历artifact或默认revision差分。

## 23333 SemanticVocoder：拟 2+2+2=6，Ch23 连续表示一段

[v1](https://arxiv.org/html/2602.23333v1)必要blocks24–68/69–89实际读。声学VAE负责细节重建，语义encoder负责任务判别，两者不天然给生成端同一优化难度；本稿以pretrained MAE音频mel-patch latent作中间anchor，把text→latent与latent→waveform独立训练，后者以Flow2GAN式clean-data prediction、能量缩放和三分辨率STFT→iSTFT平均生成波形。新增取舍是把文本端难以预测的声学细节推给条件生成器，而不是把semantic latent当可逆codec或现场细节真值。MAE原来学mask reconstruction，推理不mask；768维表示仍可能留声学信息，不说纯语义/已解耦。

直接对应控制Appendix A同AudioCaps训练text-to-latent三分支：semantic、EzAudio VAE及mel→BigVGAN；Table4 semantic六指标均优于该两个控制，但representation维度/预训练encoder与decoder不同，不唯一证明“语义属性”因果。Appendix B固定同text-to-semantic模型，VAE式重建decoder vsflow生成decoder，FAD4.781→1.709支持生成职责的局部替代；同时变训练策略和decoder架构，不是同网唯一objective干预。HEAR只为冻结latent外加MLP三个任务，可判别不等已统一理解/生成LLM。Table3重构ViSQOL3.239明显低于EzAudio4.550，Mel/STFT/Waveform也有相反排名，不能照录“无损重建”；Table1部分CLAP/IS仍低于其他系统。预训练与不同生成预算限制跨模型headline归因。

dasheng_base，AudioSet270epoch、1.6s、batch1440、24kHz；conditioner四层512，三支八层768/512/384、hop320/160/80。ScaledAdam3.5e−3→3.5e−2、warmup500/Eden27500。文中vocoder“Euler step size200”有表述歧义，不自行改成200步；text DiT24层1024、FlanT5large、WavCaps+AudioCaps40epoch再AudioCaps300epoch、batch32、AdamW5e−5、Euler100steps/CFG3.5。硬件、precision、运行并发/端到端墙钟ND；多次生成/三支waveform预测、encoder预训练和长迭代训练仍付费。78明确依赖encoder能力、不能long-form、客观指标不足且未有必要人评，图示sampling步数局部稳定不认证所有预算。

actual `MULTIMODAL-REPRESENTATION` Ch23 176–238完整邻接读：拥有连续feature需独立decoder、离散codec、semantic/acoustic分工、STACodec语义监督与重建冲突；未显式承载 **连续语义anchor将细节重建责任转给条件生成器，并据重建质量/两个阶段难度选择latent**。拟在连续表示处一段，保生成补细节不是恢复原细节、指标/预算混杂、长音频与声学fidelity反侧；若需原声保真则保留声学VAE/专用codec，不授通用音频统一。不另建Ch24重复owner。

日期：Submitted2026-02-26T18:38:17Z，same-ID registered2026-02-27T03:08:18Z；结合已核官方announcement下界，arXiv首次事件区间02/27 09:00～11:08:19+08。current必要说明无相关撤回/纠错。

### 23333 独立必要复核与 Books 处置

非原 packet 作者 feb28_ch23_finish 独立阅读 exact-v1/本地 primary blocks24–89：限采用命题的方法、对应实验、设置和直接反侧，不扩全 proof/artifact 或 revision 对比。旧 packet 只作材料，评分2+2+2=6保留。actual owner 为 Ch23 MULTIMODAL-REPRESENTATION：continuous latent/codec rate-distortion已有，但没有语义锚把部分不可逆细节交给条件waveform generator、两消费者分别优化的分支，因此 Books Decision 是具体深入而非泛化 No Change，已在相关机制主干写一窄段。encoder/decoder比较多变量、HEAR三任务不认证统一MLLM、ViSQOL3.239 vs Ez4.55重建反侧、预训练/波形多路采样成本与声学codec回退近文。必要原证/actual owner PRE完成；作者正文/完整邻接/自身末注已顺读，root 非写入者已实际独读正文、完整邻接与自身末注，POST通过，窄锁释放，未复现、非日级Gate。

## 23349 FlashOptim：拟 2+2+3=7，Ch28 mixed precision 一段

[v1](https://arxiv.org/html/2602.23349v1)必要blocks24–58/60–92/115–120实际读。成熟mixed precision保FP32 master以累积弱更新、8bit状态按absmax均匀量化；新增是按BF16权重ULP半区间存signed residual，再对momentum用softsign、variance先sqrt再分组量化，从而分开 **master累积精度与moment估计分布** 两种失败路径。每步局部解码、正常AdamW更新、重新编码，forward/backward用BF16，FSDP仅allgatherBF16权重，residual/state仍local。非lossless FP32或改变优化器objective；不把24bit所谓effective precision说成24mantissa bits。

Eq1正文N=2^b−1与Alg1 signed INT8 N127/INT16 N32767冲突，采用Alg1操作分支，不把255用于INT8，也不授正文统一公式保证。32 residual的exponent可由权重“推断”只是误差尺度上界，任意小residual实际exponent不同；只能按ULP范围编码。Alg2/3零初始化组absmax=0所写m/s或sqrt(v)/s未给零组guard，不能声明伪码全输入有效或实际实现必有bug；实现未核。phi_m(±1)=±1，实际是扩大零附近bin密度，不照录44“端点推到中心”。可逆companding函数不使最终整数rounding可逆。

必要直接对照：同hyperparameter、data ordering，reference另做同类fused Triton kernel，3seeds/H100/PyTorch2.8/CUDA12.8，测steady-state；但reference FP32gradient、Flash BF16gradient也同时变化。GPT2-124M/FineWeb10B、context1024、20ksteps、约.5Mtoken/step、warmup700/cosine/clip1，AdamWlr6e−4/betas.9/.95；limited quality落在所报方差附近，不认证任意LLM不退。固定FP32训练轨迹量化NMSE控制和Figure5线性variance量化发散 vscompanding稳定，提供状态分布影响稳定性的局部反侧；不是所有8bit优化器必发散。

Table4 Llama3.1-8B OpenMathInstruct2 SFT/FSDP+activationcheckpoint，峰值175.2→112.9GiB、optimizer step12.5→11.5ms，不能以optimizer step等价整训墙钟/throughput。Table8 GPT2 AdamW5.7→5.9ms直接慢侧。Parameter/state/activation分账；G32额外FP16scale每状态每参数1/16byte，正文57“5 bytes checkpoint”省略两个scale，实际该格式至少5.125 bytes/param（未计padding/metadata），不能照抄35GB为全产物字节。Grad release只无gradientaccumulation，不能任意开启。90–92留activation主导收益小、敏感任务可关压缩/排层、更新低于表示分辨率仍消失；没有普遍稳定、精确FP32或生产恢复保证。

actual `TRAIN-PRETRAINING` Ch28 926–991完整mixed-precision邻接读，拥有master/state/accumulation各自precision、误差传播分区与条件policy；未显式承载 **ULP residual master与分布companded moments的分账、local residual通信身份和实际总费/弱更新边界**。拟紧接951 precision policy一段，保格式/scale/checkpoint身份、全成本、有限seed控制与高精度fallback。不在Ch35/39/49重复整合；checkpoint/ZeRO只是交接影响，不能由映射多章抬Reach3。

日期：Submitted2026-02-26T18:52:22Z，registered2026-02-27T03:08:41Z，arXiv事件09:00～11:08:42+08。后续March v2不默认比较；current无具体相关纠错信号。

## 23334 窗外旧家族，不作为本窗候选

原arXiv current注明Accepted ISQED2025及Related DOI `10.1109/ISQED65160.2025.11014376`。此次定点恢复[作者机构出版页](https://cfaed.tu-dresden.de/publications?pubId=3808)同全题名、Liu/Ullah/Kumar、页1–9、year2025，并有PDF下载；[IEEE写入的Crossref DOI元数据](https://api.crossref.org/works/10.1109/ISQED65160.2025.11014376)同身份、published/issued2025-04-23，created2025-05-30T17:43:30Z、deposited2025-05-31T05:01:06Z、indexed2025-06-01T04:08:28Z。published为日精度，不补首公开时刻；2025出版事实+当时注册身份上界足以排除2026本窗首次家族事件，不单以Accepted当public。

实际返回/执行时间见[V3_FETCH_AB13_23334_FAMILY.json](./V3_FETCH_AB13_23334_FAMILY.json)，原值保存在V3_IEEE_23334_METADATA.txt与V3_23334_AUTHOR_PUBLICATION.txt。未有具体本窗重要修订信号；2026 arXiv上传不产生新的首次公开，不评分、不读无关core、不写Books，也不声称2025真实归属日已处理。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：23349：原必要blocks37–51/80–92与actual owner独核；Ch28正文961/完整942–973/own1815 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。
