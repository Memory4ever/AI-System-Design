# FIFTH四N最低决定事实

作者Kierkegaard，4窄P提案待root实际核；不是论文first/评分/Evidence/Books。只四个明确含糊门，未重FIFTH完整AB，不因medical/geography领域名决定。

本日精确v1 HTML：09056 HTTP200/exit0、194484bytes；08741 200/exit0、314672bytes。09513 HTTP200/exit28、465488/1283379，08668同200/exit28、402325/576303，均18秒partial不称完整原件；必要方法/结果/limits在截点前完整可读。最初09513/08741联合输出中段截断，09513 3.4/4.2与08741 S3直属规则另完整读回，不把打印截断作全读。所有session结束，未执行模型/代码。

## 09056 LesionAwareLDM：N→窄P，仅latent/decoded/region损失的不同消费者

实际2.1/2.2 Eq4–8、3.2 Quantitative/LossWeights/OtherLDM及完整Tables2/3。既有decoded image-space posttraining已有先例，不把成熟weightedL2本身当创新；具体潜力是latent noise-MSE不能保证小区域decoded误差，通过单步estimated-z0解码损失增加全image与binaryGT-lesion两个不同消费者。这个训练单步不是部署一轮生成/恢复CT缺失信息证明。

Table2实际反侧能改变采用判断：λimage=.01/λlesion=0时DWI全局MAE .073→.074但region .222→.202；.01/.01全局更差.078而region更好.198；.05/.2 ADC region .083却全局.086较baseline.072更差，且PSNR退。这是global/rare-ROI质量不能合并为同一无损目标的条件，不采817病人诊断/全部指标优越。Table3cBBDM-PT有限另一latentprocess，效果不授所有generative架构或所有噪声/precision/费用。区域GT/decoder结构、另posttraining预算必须保留；窄P只生成目标资格与实际tradeoff，不扩临床Science效果。

## 09513 OSIRIS：N→窄P，仅生成/判别表示耦合的missingview资格

实际3.1双latent/Eq1–6及所带Table2、3.3/3.4预测与imputation、4.2/5。G以linearFA重建views并承载label-generativeview，Z从observedviews linear-weight到tasklatent，输出由ZU与GVY共同产生，两组ARD稀疏；missingfeatures作为randomvariables从G posterior重建，再用于下游classification，而非只外部预处理imputation。这是具体表示消费者分工，不因Bayesian名字收入，也不是“FM embedding可在未来使用”授主线。可保留窄一般表示/缺view推断条件，临床应用结论不采用。

4.2实际比较internal imputation与外部mean/KNN/missForest/MICE/GAIN/HyperImpute六方法，再分类BACC；10随机masks/正文5–30%人为missing，不证明MNAR/真实missing整模态无偏。Tadpole高inherentmissing被排、Fashion/Digit不变亦未图列，VAE/ReMasker因初步较差未纳，不能称所有baselines/populations胜。G依赖labelview，结构上与Z分开不证明统计disentanglement/无classificationbias；线性/mean-field近似限制保留。3.3 Eq16noise variance项写Eη而η此前precision、公式与文字referencedEq175/180/181不齐；3.4 Eq17积分变量/conditioning不齐，不静默修公式或采无偏/安全uncertainty保证。5承认不能直接处理image/text、需precomputedembedding且解释性降低，predictionmean不因Gaussian就trustworthy。窄P只这个耦合/消费者资格，中心强保证保留争议，不自动深审全附录。

## 08668 HuluMed：N→窄P，仅plane内外预算策略与3D/video消费差额

实际Methods RotaryPositionAdaptiveEncoder/Projector、AnalysisModelDesign与Discussion必要部分。SigLIP/2DRoPE/GELUprojector是成熟组件不单算贡献；所有visual变2Dplanes，单2D不pool，3D/video先2×2bilinearmerge降4倍，再邻slice/frame embedding的L1<.1 pruning。可保留是相同token省法按2D/3D/video消费人口不能互用，以及跨plane相似并非细微时空结构安全证明。

原Analysis声称surgicalvideo减55%近似不变而M3D/3DRAD有退，Discussion/Methods另写最高60%，不同分母保留不修好；混数据模型对比single-modality同时有data增量，不授统一架构独立因果。3:1医/通用、1:1text/multimodal只是所测mix，不普遍最优；4100/38000GPUh绑定model/trainingpopulation且正文常称fromscratch又组合pretrainedencoder/LLM，不称无需预训练预算。开源/公有数据不保证全copyright/privacy安全、benchmark/judgecase不代临床validation，Discussion末明确还需临床验证。当前只selector/预算消费必要准入，不读全部extendedfig/附件来预授Evidence/临床安全。

## 08741 Geocoding：N→窄P，仅oracle信息、实际tool与geometry评价分责

实际S3原knowledge/reasoning规则、3.1/3.2/Table1、4.2/4.3/Tables2–4、5.3与limits。Knowledge给明确位置名和country去歧义、Reasoning不给目标名而给描述/mentioned geo-entity的OSM gold center coordinates，信息与题目不同，不等同任务下model内部reasoning因果；geoparser-augmented先取mentionedlocationcenter再让LLM推bbox，oracle替实际tool会改变accuracy/coverage评价消费者。

具体新反侧：Table2oracle也非总胜，Llama8B distance4427.8→7658.5、405B directF1.245→oracle.235，FT8B oracle28km→实际152.2km；Table3FTQwen14B oracle135.9km→真实240.9km但AreaF1 .248→.266。Table4LLM-onlycoverage95.9高于tool90.8而distance627.5比240.9差，不能一个coverage代总能力。5.3看到模型用所有mentionedcenter extrema作bbox，面积扩大/precisionvsrecall失配；工具真实坐标也需相关性消费，不能用可用事实证明推理会用对。正文reasoning“all<35km”与Table1 36.2/82.9/92.4不齐，不补数字；英国/全球Wikipedia抽样单English1000与未控制长度/实体frequency限制保留。仅RAG输入资格和point/box/area分母的可迁移边界，不借坐标任务收益或部署地图可信度准入。
