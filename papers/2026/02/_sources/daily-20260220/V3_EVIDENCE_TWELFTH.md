# 02/20 第十二有限必要包：16609 / 16642 / 16660 / 16682

只保实际读到的精确v1核心、必要对照与反侧及actual owner差额。当前官方完整题摘/Comments/history已轻量核：16609/16660 current v1；16642 current v4（后版ICLR状态）、16682 current v2改题为SAW-Bench，无明确纠错/撤回声明，不倒填后版内容或遍历历史。root四项必要PRE通过，16609/16642/16660实际正文/完整邻接/自身末注POST通过，三锁释放；16682标准仅报告通过，不授整日。位置为 `V3_extract_html.py < V3_REVIEW_2602.<ID>v1.html | awk 'NF' | nl -ba`。

| ID | v1 Submitted UTC | 同ID DOI Registered UTC | 北京公开范围（官方bridge推定，含起不含止） |
| --- | --- | --- | --- |
| 16609 | 2026-02-18T17:03:32Z | 2026-02-19T02:50:28Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:50:29+08:00 |
| 16642 | 2026-02-18T17:32:43Z | 2026-02-19T02:51:17Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:51:18+08:00 |
| 16660 | 2026-02-18T18:01:23Z | 2026-02-19T02:51:45Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:51:46+08:00 |
| 16682 | 2026-02-18T18:22:52Z | 2026-02-19T02:52:19Z | 2026-02-19T09:00:00+08:00 ～ 2026-02-19T10:52:20+08:00 |

Registered作为arXiv公开事件上界推定，沿首包两官方桥接/1秒精度；Created只保raw，不把字段本身定义为正文公开。没有搬后来发表状态。

## [ColBERT-Zero: To Pre-train Or Not To Pre-train ColBERT models](https://arxiv.org/html/2602.16609v1)

2+1+2=5，具体接口条件/owner差额深入。§2（58–76）从同ModernBERT MLM起点比较dense unsup+dense sup+multi-vector KD、dense unsup+multi sup+KD、multi unsup+multi sup+KD；改变多向量目标适配的阶段，不是只换推理scorer。Table1（84–106）unsup/sup/KD分别368/32/8 GH200 GPUh、batch16384/64/128，10个LR NanoBEIR选择；已dense预训练的成本是sunk，不从reuse路线推出全生命周期99.4%无代价。§3.1（303–307）作者BEIR nDCG@10与同数据路线支持局部阶段选择；闭源GTE等不是完全匹配因果控制，三阶段预算不相等，未核独立seed不确定性。

§3.2/Table3（310–486）实际对照dense/multi unsup with/without search_query/search_document prompts，再with/without prompts做sup+KD；prompt各7token、训练长度另外补7，存在长度×prompt效应。匹配已有prompt条件帮助局部路线，但非通用“prompt必要”：§4（489–490）明确更强NV-Retriever/更长微调能适配新prompt，multi-pretrain小残余优势也可能来自额外scale，larger KD尚待检验；implicit query expansion只是conjecture。未采headline性能/延迟，precision/seeds/生产SLO Not Disclosed；未核实现/复现。

actual `AGENT-RAG` Ch76:231–254已多向量表达能力与搬运代价、domain/relevance mismatch与微调负侧、SAE联合检索适配；未承载**dense起点切换late-interaction训练目标时的阶段选择，以及继承prompt×微调强度决定是否需要保持接口**。拟在域迁移段后/SAE分支前一自然段：多向量不是免费KD转头；旧dense+multi监督/KD与完整multi预训练并存，继承prompt有限可用但强微调可重学，训练阶段/查询长度/索引重建成本一并保存。不是为缺ColBERT名字造gap。

## [Optimizer Choice Matters For The Emergence of Neural Collapse](https://arxiv.org/html/2602.16642v1)

2+1+2=5，必要理论权限与owner差额深入。§2（163–201）NC1–4与raw classifier row-sum NC0不同，不把NC0当充分证书。Prop2.1从normalized alignment到absolute row-sum的桥接未在本包授通用必要性（W scale需要额外控制），所以不采用“所有AdamW不能NC”抽象保证。拟采用的是finite empirical boundary：§3.1–3.2（207–274）ResNet9/VGG9、MNIST/F-MNIST/CIFAR10、200epoch/b128/两次LR衰减的3888网格，先排low-train-accuracy runs；momentum在类似fit条件下仍影响NC，有限未见no-WD不排asymptotic。

§3.4（294–324）固定total decay .0005/momentum .9插值coupled/decoupled，NC变化而validation基本不变；不是自动更泛化。SignGD/SignGDW理论只fixed UFM、H固定M*、只训W与特定zero-init/步长，SGD另有linear-head CE/all-parameter decay/0<ηλ条件，不升级actual adaptive/deep/LLM定理。§4（329–378）NC4训练几乎100%可与NC1–3分离，AdamW可partial NC1/2，ViT只是preliminary。D.1/2（729–735）优化器LR/WD网格不同、5RTX4090 24GB、8–16min/run；precision/独立seed Not Disclosed，3900网格不等3900独立重复。

actual `TRAIN-PRETRAINING` Ch28:337–355已有effective step、optimizer×augmentation/normalizer、covariance/mean/readout诊断；未具体承载**相近拟合/validation下coupled decay与momentum仍可改变class-representation geometry，以及NC不同指标不能互相替代**。拟在optimizer recipe前一自然段，以局部classifier证据要求fit与几何诊断分账，不以NC更低替held-out质量、不建议普遍换AdamW；受限sign理论仅标权限，不写NC0无条件必要性。若root认为既有联合geometry论点已足承载，可具体仅报告，不能为无NC配方强写。

## [Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM Safety Alignment](https://arxiv.org/html/2602.16660v1)

2+2+2=6，安全/表示训练边界深入。§3（119–185）同义prompt翻译后取选定层last-prompt-token，用联合训练linear extractor、unit normalization与stacked Z；softmax singular-value auxiliary追求collinearity，主monolingual SFT/DPO/SimPO/ORPO loss仍负责response anchor。rank-one允许反向共线，不等语义同向、hidden-state完全共享或输出安全保证；learned extractor也可改变proxy。所谓single forward是跨语言batch，不是只付一条语言forward，仍有m语言activation/SVD与extractor成本。

§4.1/Table1（190–200、263–290）10语言PKU heldout/OOD MultiJail，Qwen2.5-7B DPO与DPO+MLC局部安全/PAG比较；PAG agreement不是truth/safety。§4.3（588–591）MLC约1.8M vsbase .59Mtokens，其他方法更不同，不做等预算独立归因。§4.5–4.7（746–770）多目标路线/层与λ反侧，deepest layer安全提高但utility可能更坏；Gram20case不授因果。D.1/2（1159–1172）full-param 8H10080GB、GPT4o翻译过滤2835train/180test、English responses，失败低质翻译被排；D.4（1194–1234）GPT4o greedy judge，两个安全协议不同。E.3/4（1400–1421）λ≥.8 utility负侧、GPT4/NLLB/30%noise受测翻译下安全稳定但utility变化。不采headline安全率/跨语保证，precision/seed不确定性 Not Disclosed；未核实现/复现。

actual `TRAIN-SFT` Ch29:80–98已有CE/entropy目标与correctness分权、多语confidence与accuracy分离/label smoothing；未承载**只翻译prompt、不额外标注多语response的表示辅助目标与monolingual行为loss的责任分工**。拟在多语calibration段后一自然段：prompt geometry auxiliary是条件分支，不是训练response免费、也不把共线性当安全；保层/λ/translation quality与utility、matched安全judge/cost及普通verified CE/DPO回退。单一owner29，不重复推导Ch34。

## [Learning Situated Awareness in the Real World](https://arxiv.org/html/2602.16682v1)

2+1+2=5，标准完成拟仅报告。v1标题/AB含未展开宏 `\ours/\videonum/\qanum`，不倒填current v2的786/2071。§3.1–3.3（365–407）6类observer-centric题、15核心scene、每scene40–60 continuous clips，memory题拼before/after；参与者已知轨迹/配置作为annotation，visibility差或rapidheadmotion样本discard/refilm。§4.1（662–707）24MFMs zero-shot，blind/socratic GPT5.2、2graduate humans无time约束；regex失败由GPT4omini抽取，不当GT认证，model/human预算不等。

关键control §5.1（712–723）straight/stable-head、同straight/frequent-head-rotation、真正zigzag，受测模型混淆中间条件；这是观察者旋转干扰路径读出的局部负证，不识别唯一内部原因。AppB（1437）system prompt还让model把camera movement当own head AND body，需要保protocol可能混杂。§5.3/4（776–792）离屏物体不等不存在、户外clutter与尺寸confound；AppA（1248–1253、1418–1430）API/unequalthinking/contextoverflow，frame/FPS有限讨论不授全模型budget invariance。未采准确率/样本 headline，未核实现/复现。

actual `MULTIMODAL-WORLD-MODELS` Ch25:377–379已camera-invariant trajectory与object/camera分责，408已known-self inverse-transform vsunknown-object dynamics/观测条件；本benchmark局部控制是有意义验证，但并无新的可恢复几何变量/模型执行接口。拟仅报告真实observer视频负例与annotation/protocol混杂，不声称整个SAW task已被Books完全覆盖；不为更多camera题堆新段。保现有calibrated/state-reset路径，不把能力盲区解释为世界状态安全保证。
