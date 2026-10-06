# Jan06 评价与生成必要停点

仅既有潜在线索，未冻结或日级验收，不默认继续库存。下面新增对象评分保持送核值，不因必要审阅工作量或Books已有而降分。

## Spatial4D 2601.00092v1

实际§3.1–3.3及h5 construction/evaluation、§4.4两h5（Temporal Context与Visual Ablation），保存core00092；模型与引用baseline均实际读。route room标签人工预处理、点云仅QA建设不进模型；约40K不是直接human baseline，1000题human最高分是另子集/聚合对象。MCA exact/fuzzy、NA MRA不同协议不合并真值。Qwen3VL30BA3B 64frames视频/随机1frame/无visual，八task text胜single和route video近blind是可用受限反证；不能由此识别语言prior唯一因果。5/10/30min是420/426/200不同subset，未paired同sample或同难度，不能证明时长导致退化、aliasing饱和或必须streaming。拟2+1+2=5的有限sampling/可见证据干预边界，不把dataset size本身计贡献，具体Books待root。

## InfoSynth 2601.00575v1

actual§3.1–3.3/4.1–4.2/5及5.1/5.3/5.4/5.6/5.8必要范围，缓存core00575。新增廉价benchmark surrogate：encoder/UMAP embedding的kNN KL与differential entropy，k-farthest选择+mutation/crossover+codefeedback；潜在2+1+2=5。3.2已披露负KL估计和subset/superset偏差，entropy用matched N抽样，UMAP10run的不确定性不是原空间语义coverage证明；R^d没有无条件均匀最大entropy分布，不能授‘perfect diversity’。不同embedding相对次序类似仅这些数据。

GPT4o co-generates solution/tests、执行通过只证明二者局部一致，postprocess修改statement配合tests也改变eval身份；100/benchmark human样本97%左右不证明全部gold correct。复杂crossover/numerical题更易filter，仍拿失败题作seed，不能称无selection bias或未污染。人工hours不同于GPU成本，modelquant/evaluator/原始与postprocessed分母保留，不采所有新benchmark真实更难/更独立。是否可作具体已有coverage/仅报告或窄owner缺口待root，不因访问或题材关闭。

## FreeText 2601.00535v1

actual§3.1.1–3.1.3/3.2.1–3.2.3、4.1.1–4.1.3/4.4/4.5/5，cachecore00535。候选2+1+2=5：attention sink anchors定位与glyph raster/VAE/noise-aligned LogGabor信号的masked采样分支，非只换文本指标。3.1.2用reference Y的IoU选timelayer，采用完全intrinsic deployment定位须说明Y来源/校准与heldout隔离；不能猜其自监督获得。mask来自attention不是已证明因果region。新glyph channel不改weights不等没有预处理/状态/成本；对不同model支持语言/长prompt truncation限制明确。

Table6 removingSGMI NED/VQA下降但Flux Aes full5.342低Base5.365，不能称所有quality不变。A6000/bf16/928²/50step公开，仅该有限配置开销；OCR/CLIP/Aes/VLM分别proxy不等humantruth，不能授通用SLO或semantic leakage完备抑制。reference-mask部署条件/具体Books决定仍普通必要核，不以缺实现直接堵整篇。

## Talk Less 2601.00224v1

完整v1题摘/本窗身份字段已读。新增Q* reverse code→intent match与Feedback+execution反馈的局部generator-discriminator recipe拟1+1+2=4，不把成熟independent validation原则计原创；不采用三数据集性能或企业级trust保证。HTML一次404只是访问记录，不证明贡献关闭/全文不可恢复；只有决定准入的新增边界不明才定点PDF，明确局部recipe则不为不采用性能遍历全文。root准入/评分校准待返回。

## 最终处置同步（2026-10-02，日级Gate待root）

当前最终处置：Spatial5具体已有覆盖Ch66；InfoSynth5标准仅报告；FreeText5标准仅报告并隔离未知deployment Y来源/定位正确保证；TalkLess4局部recipe关闭。root实际必要源/owner或关闭校准通过，不采时长因果、semantic覆盖、通用glyph定位或headline性能。
