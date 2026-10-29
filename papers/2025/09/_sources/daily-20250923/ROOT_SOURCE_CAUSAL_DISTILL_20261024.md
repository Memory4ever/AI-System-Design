# Causal Fingerprints / EDGE：有限必要证据

Singer A242/A243及后续停点明确15406/15472首次必要域未开始、无GET在途；root本轮明确接受后首次捕获/准备。只转首必要，不转既成日门、原分、README、current-owner或Books写权。Singer须作为唯一另一角色回以下有限原域实际采用，Sartre随后仅角色复用，不第三同一Methods/直接控制。

## Causal Fingerprints of AI Generative Models — 2509.15406v1

[精确稿](https://arxiv.org/html/2509.15406v1)、[raw](ROOT_CORE_CAUSAL_15406_20261024.raw)/[请求](ROOT_CORE_CAUSAL_15406_20261024.request.json)：UTC2026-10-24T11:18:55.066303至11:18:57.163752，200/exit0，128099B/SHA256 `834936dec50738c31000136d05976f4f4dd768adca1166538600c8614b0e79a3`。

actual完整读§2.1–2.4/Eq1–9、§3.1–3.2/完整T1–2/必要F1–4 caption及§4；未图像素、代码/数据重制或实验复现，不执行文中扰动。局部机制/直接对照/关键反侧与全费已足，不因“causal”名称扩查全部因果/法证文献。

机制是原图减DIRE扩散重建图的residual，再读RGB/DCT/灰度FFT低频、ImageNet ResNet101、ViT class token、DINO ResNet50等六空间特征并加权融合；先成128维fingerprint，再以VAE压到64维、重构128维并用MSE/L1/KL训练。64维reshape为8×8只是可视化，不是物理空间图或独立因果分区。分类端描述CLIP ViT-B/32加attention/交叉熵，结果段又称CNN优KNN/SVM，完整特征→分类接口/训练recipe并未完全明确，不自行补实现。Eq2写求和，文字又称加权concatenate，异宽特征如何投影到共同128维未闭，不能照成任意shape已对齐的配方。

**“可预测来源”不等“识别生成因果”。** 设content/style/artifact彼此独立且F只由artifact决定，是所提出causal graph的假设，不是实验已证。图中对共同结果X条件化的相关性论述，不能反推减重建就自动去除了content/style；DIRE保语义也不保证重建误差只有模型特有伪影，语义/风格重建偏差仍可进residual。六空间中RGB/监督语义encoder本身不天然semantic-invariant。分类/FDR能支持本人口来源信号和可分性，不识别唯一artifact cause、完全解耦或生成模型的内在真身份。文中所谓counterfactual为对图像作受限扰动改变分类反应，未对真实生成机制做受控干预；局部分类可被改变不认证内容/风格完全不变、因果隔离或隐私安全，不补未披扰动预算/成功率分母。

GM-GenImage来自BigGAN/ProGAN/Glide/SD各10k=40k生成图，是四已知类来源分类，不授未知生成器/新revision、真实图混入、JPEG/裁切/重编码或跨内容style鲁棒法证。split比例、同prompt/原图跨split、图片分辨率/压缩与模型间数据支持、训练seed/CI、精确模型revision/优化预算未披，不能保证排除内容/来源dataset shortcut。T1 98.04%对81.87/84.04等支持该闭集局部结果；所称平均22.78%实际各差33.61/16.17/14/15.91/33.42/23.54约为百分点口径，表与prose有一项15.97/实际15.91差，不把它们当相对提升或重造平均。

**融合不是全指标支配。** T2单RGB99.54/DFT99.75/SSL99.67均高于empirical融合98.04；未权94.33和crossattention88.83更低。FDR融合357.01比若干单空间高，不等分类准确率更高/通用稳健性。QFT64.62而FDR291.89也说明分离代理与真实分类结果分账。权重按先前结果经验选，验证/测试选择隔离与等训练参数/预算未完整交代；不得将更多空间或更高FDR认作已证因果增益。三大高单空间/较弱fusion与摘要高分同时保留，原贡献不因反侧自动排除。

全DIRE多步重建、六空间/所有预训练权重、特征缓存和投影、VAE/分类训练、融合权重搜索、评价与独立来源/编辑鲁棒检查均计费。复用生成图免训练四生成器不让前置训练免费；hardware/precision/完整墙钟/峰memory/并发SLO未披不补。只能作为所测已知来源的候选证据，不能单独指控内容来源或签隐私；来源/内容漂移、编辑或接口不合时，保原图/可审计来源元数据、简单detector和独立人审，不让“causal fingerprint”名称批准真实因果/安全。原日门/评分/候选保持，具体owner和采用资格下一层独立判断。

## Efficient Multimodal Dataset Distillation via Generative Models — 2509.15472v1

[精确稿](https://arxiv.org/html/2509.15472v1)、[raw](ROOT_CORE_DISTILL_15472_20261024.raw)/[请求](ROOT_CORE_DISTILL_15472_20261024.request.json)：UTC2026-10-24T11:20:19.759756至11:20:32.435977，200/exit0，221576B/SHA256 `9a210a663467a83cb538dc25ce838dc20b09dd3761ec37459b973d1b07d2ee33`。

actual完整读§3.1–3.4/Eq1–6、§4.1–4.5/完整T1–10与T12及T11必要文字caption、§5、A训练细节/B影响。未C全部qualitative图/像素、代码/数据/复现；文本引用若错指T12/T5，按真正caption/内容定位，不用引用数字替实际读表。

EDGE改变的是**小训练集的生产方式**：微调预训练扩散生成器，使去噪估计与原caption embedding做双向contrastive，再对图文拼接表示加多样性项；从原dataset选caption采图后，再让MLLM读生成图补caption。训练下游NFNet+BERT image-text retrieval，BERT evaluation encoder冻结，不是把旗舰模型答案蒸馏进学生参数、也不是原分布已被精确求出。Diffusion仍需原数据适配；合成caption只描述派生图片，不增加独立真实观察，教师的错误/旧prior可能一起传给小集。

完整执行shape/语义须另核：文中直接用去噪image latent与768维text embedding内积，未交清pooling/投影，Eq3又混用I/T与z/y记号，不能默认latent tensor已等维。Eq5的×称similarity matrix但目标需标量聚合，norm/配对处理不完整，Eq4与Eq6的lambda角色复用；A只说微调小部分参数并给Eq6 lambda1，没有完全列可训练子模块/其它参数。原dataset允许一图多caption/一caption多图，而Eq3只对角正样本，若同图多caption同batch可能是假负样本，未给multi-positive mask/采样方案，不补成已解决。更远的embedding/更高CLIP/FID不保证小集覆盖、真实标签或下游泛化。

预算单位为image-text pairs，CPI增加时在固定pair数下降unique images；不能把500pairs当500独立图/独立知识。表中1.7%/3.4%等压缩比与原图像数/多caption的完整pair分母不同，不能一律当按全部原pair计算的节省。CC3M真实可取2.3M/原3.3M，validation只抽1000pairs；T3明确1000合成pairs，正文后段却说500，同处0.3‰/表引用也不完全一致，不能默合成一个确定人口。保具体表口径，不称覆盖全部CC3M或生产检索。

单RTX A5000、image224²/text768；主评NFNet+BERT预训权重，文中原训练资产非零。A Flickr16epoch/COCO8epoch、batch8/lr1e-4，只给这两数据；CC3M完整适配与全部采样/teacher参数、随机重复/CI、precision/模型API版本未披不补。T1 500pairs Flickr EDGE各IR/TR均低LoRS，COCO仅TR@1 2.9略高2.8、其余大多低；T2 1000pairs COCO全面好于所列LoRS，但Flickr IR各仍差，TR略好，不能由结论“outperform”授所有预算全胜。T8只contrastive时TR@5 8.3/TR@10 13.7低SD8.7/14.9，加diversity后TR@10 14.4仍低14.9，所有模块非处处改善。

T10 CPI2最好而CPI5明显差：例如IR@1 2.8→1.2，TR@1 3.9→2.0；caption增多同时unique图减少，不是单调知识增广或每图越多越好。该表数值CPI2同1000pair主表，但prose称500pair，保两口径差，不将它与T8直接拼成严格同人口消融。T12 LLaVA高GPTmini/Llama，同时postimage caption与preimage改写策略/模型改变，不识别唯一LLM优劣或caption时序的全部因果。T7换ResNet/RegNet保持BERT，对LoRS迁移更好只限这些视觉架构/本任务，不授任意模型独立或全能力迁移。

T6给distillation GPU小时，COCO500pair EDGE7.7/LoRS151.6/MTT162.3仅该制备口径；Flickr500 13.6/54.2/77.8不同预算不是统一9倍，CC3M31.7–33.2h又高于部分Flickr EDGE时间。T9 .4h/1.6h仅SD1.5/SD3采500图，不是含训练/MLLMcaption/评估的总费。参数、质量目标/硬件/前置预训预算未全配平，OOM只这些基线实现/设置，不证明所有其它方法原则不可用。计生成器预训/适配、全部采图/失败重试、MLLMcaption/API、人/标签核查、每CPI/模型/小集选择、下游训练和留出回归费；免存大dataset不等免访问原数据/无版权/隐私或安全保证。小集遗漏长尾、虚构caption或净费用失配时保真实配对/coreset/原训练集和独立质量验收，不由拟真图片批准“分布已保全”。原分/日门保持，具体owner/Books是下一层，不预NC/I/DAY。

两次请求与exec均已真实结束；root首备只以上有限必要域，等待Singer唯一另一角色实际采用后角色闭合。
