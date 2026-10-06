# Neighborhood Blending — 2602.12943v1

仅Gumbel top-m集合分布与单次ε预算证明争议入口，3+2+2=7，具体推断发布privacy命题深入完成；root actual Lemma4.1/Theorem4.2与独立反例已核，中心暂缓处置通过。不评分成熟neighbor blending。

原源 https://arxiv.org/html/2602.12943v1 ; V3_EVIDENCE_12943_LEMMA.txt B72–85与V3_ADMISSION_12943_CORE.txt。B73限制bounded feature、substitution adjacency、固定index候选集；这些不是整个classifier训练数据/label机制ε-DP的自动保证。B77正确部分是Gumbel top-m可作PL sequential withoutreplacement，随后‘thus exponential mechanism over subsets’身份一般错误；B81 theorem实证的是单次product-weight subset sampling law，不直接涵盖实际PL law。

独立解析N3,m2,positiveweights(2,1,1)：P{1,2}=2/4·1/2+1/4·2/3=5/12；P{1,3}=5/12；P{2,3}=1/4·1/3+1/4·1/3=1/6。product-subset weights(2,2,1)归一为(2/5,2/5,1/5)。这是标准有限概率反例，不是复现作者实验；不要求整个classifier性能试验就能否定分布同一性。

不由此宣称PL机制永不DP或全部privacy保护无效；当前证据只是原proof不能给实际top-m选择授同一单次ε集合预算，更不授无条件label/输出发布privacy保证。non-DP局部utility或same-prediction behavior不一并否定，但不是本项长期采用命题，不补全classifier benchmark。current abs明确v1、未返回withdraw/correction；Submitted/Created共同落窗原字段同ID见V3_PRIMARY_DATE_FIELDS.json。

Books：暂缓 PLATFORM-SECURITY（Ch72），不把中心positiveDP写入。重开只需定义实际sampling law、candidate adjacency和释放对象，补相应privacy预算证明或改成product-subset sampler后证明；不等完整revision史，不泛API恢复，不把中心冲突降分/删除反例。root此必要有限原源/反例及安全隔离实际独核已通过。
