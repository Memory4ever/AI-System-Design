# 10444 Averis：mean/residual训练图与actual Ch28具体已有覆盖

仅补Mar12 BJT自然日，第二包完整exact-v1 AB/独立窄准入与已通过arxiv日级夹证复用。官方 https://arxiv.org/html/2603.10444v1，`SUP_CORE_10444.raw/txt`及manifest/result GET200 UTC2026-10-09T15:56:08.361039、268219bytes。作者实际读§2–6全部必要定义/机制/直接评价，§8结论，§4 Theorems1–3及本节证明、Appendix A与B.1–B.3完整必要证明。Figure1–5只正文/caption，不认证实际像素、loss差数值或图内统计；RelatedWork只作者positioning，不补引用论文证明。不读v2/no code/复现/硬件运行。

## 新增命题与三维最低投入

block extreme定标使共享均值挤压residual数值分辨率，SVD热路径贵→本文按activation与output-gradient列均值做rank1/residual独立量化、保留GEMM补偿项→影响低精度训练数值分解的对象与更新图。这不是一般中心化、FP4标签或成熟SVD思想本身。拟`2+1+2=5`，重要numerical interface2、单训练算子路径1、可复用张量role/补偿资格2。理论/训练图资格与actual长期owner已读，必要深入完成。**拟已有覆盖Books新写0**只对应下述实际稳定接口，强主导因果/概率定理和硬件效率不采用；没有把新实验叫旧报告已处理或从候选删掉。待非作者受限终态/actual owner裁，不提前formal。

## 精确机制：减除不是删除，均值也被量化

§2把X(b×s×m reshape为l×m、l=bs)写成列均值rank1 M=1muT与residual。§5 Averis对muX、XR与W分别Qb，forward Eq11为broadcast(Q(muX)Q(W))+Q(XR)Q(W)，均值独立scale但不默认高精度，也不是改变网络输出丢掉mean。Backward对D=∂L/∂Y同样分muD/DR，inputgradient两项；weightgradient Eq12保留XRᵀDR及XRᵀ1muD、(1muX)ᵀDR、(1muX)ᵀ1muD四项。原fullprecision decomposition代数成立；量化residual后均值可不再精确零，不能自行删cross terms。不物化完整mean matrix并非免额外mean-vector matmul/reduction/融合成本。

没有公开blocksize/scale-code精度、accumulation/master/moments、是否全部GEMMs采用、kernel/backend/分布式mean边界或完整token masking；主文“only2means/2subtractions”不完整表达额外项代价。不称已核实际kernel、精确weak-gradient无偏或W4A4G4代表全部状态4bit。mu随microbatch/sequence composition变，身份与trace/restart条件应保留，是审阅者工程推断而非作者部署实测。

## 必要评价及直接负侧

§6唯一Qwen3 .6B，DCLM English/Unicode过滤、拼接/分段，称训练100Btokens；下游表仅10Bcheckpoint。FP4 W4A4G4为E2M1 NVFP4、所有FP4默认stochastic rounding；对照BF16/vanillaFP4/Averis，SR本身与split不同。未给hardware/precision accumulation/总wallclock、LR/optimizer/seed/repeat和完整匹配轨迹，不补造原生Blackwell或实测速度。Figure5正文称loss仍略高BF16、优于vanilla；未读像素，不授数值差/统计显著。

Table1 BF16→Averis平均.4564→.4661，但ARC-C .2534→.2491、ARC-E .5126→.5072、Hella .3768→.3751、PIQA .6730→.6670退；BoolQ/LAMBADA/RACE增。七指标表没有vanillaFP4下游列、误差或多seed，不能把均值上升称所有能力恢复、100B终局更好或普遍优于BF16。仅有这组checkpoint支持受限可行性，不由小模型标签排除具体接口。

## 强中心理论的隔离（不是否定splitting实验）

§2 leading singular alignment只在dominant σ1与u1符号低抵消条件下成立；Figure1 .99/Layer27 FFN只是作者profile，not arbitraryX。§3 Eq3把非odd激活一般写Eφ(z)>0不成立（例如−ReLU；SwiGLU gate乘独立零均值value亦可零均值），Eq4 additive residual也允许Δmu=−mu，不能由加法宣称“prevents cancellation”。‖mu‖增长是整体范数，不自动推出某单坐标最大值压过noise。所profileQwen early10k/late170k、embedding/layers3/15/27不是全部架构/层/分布的因果干预。

§4 Eq6–7全矩阵Frobenius正交能量分解有效，但Eq8在top .1%单元素的平方ratio不必sum1，cross terms也不必minor：M=2、residual=−1给X=1时ratio4与1，和5。这是审阅者反例，只否定无交叉项的局部能量份额/唯一来源认证，不指控Figure4读数不存在。若不读像素，不采用top .1%“near-total”量化比例。

Theorems1–2的reverse-triangle与subGaussian/期望count界可以保留其给定条件；mean足够超阈值/σ才有非平凡下界，仅mu>t时界可为负。variance-only在fixed t/σ也有O(l) expected count，不能据此一般说关于l比mean更稀疏；稀有度还依threshold/σ，真实token相关/重尾也不是假设已验。

**Theorem3 q分位数与概率方向不一致。** 原q=σΦ⁻¹((1−δ)^(1/l))。Proof实际P(maxYi<q)=1−δ，故从Mj≥|mu|+maxYi只能推出该threshold概率≥δ，不是≥1−δ。取l1/σ1/mu0/δ.05（原明确允许mu0），q=Φ⁻¹(.95)，实际P(|Z|≥q)=.10<.95，直接否定写出的普遍下界；不是只说proof松。所写P(M≥|mu|)=1−2^-l也把lower-bound事件当equal：mu0时概率1而所式1−2^-l；mu≠0两侧Gaussian尾也增加概率。variance-only upper union-bound仍可有效，不一起推倒；不自行把更正后的quantile写成作者定理或普遍mean主导证明。

## actual唯一owner与Books决定

唯一 `TRAIN-PRETRAINING` [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)。实际完整958–999 mixedprecision/operand-role邻接，1000–1115 sensitivity/softmax matched-delta→scale lifecycle→Averis→transposedblock→traininggraph完整局部已读。**1056–1070已经具体承载activation或outputgradient共享mean/residual分开quantize、GEMM cross-terms重建、reduction/subtraction/fusion、microbatch漂移，以及Averis有限可行性≠所有层dominance/硬件吞吐、vanillaFP4与FP8/BF16回退**。这是真实机制覆盖，不是主题映射或成熟数值原则代替新材料。Ch49是部署artifact/kernel硬件交接，不能因FP4标签抢训练owner；Ch27/29相邻训练数据/SFT不承载此计算图。

本稿强主导理论、具体下游结果和未披露硬件身份不冒称现文已全部吸收；采用命题只是上述受限source-aware split，已确切覆盖，**无新增书稿PRE/写锁**。不因为Books有覆盖把5分/必要投入降成免审或EX，也不宣告本日DAY。重开仅拟采用强定理时的真实概率条件/局部cross-term统计、独立因果干预与matched长horizon/原生完整cost；普通未披露代码不另伪造外部阻塞。

## 正式受限终态

mar13_admission_review实际必要原件/Thm3断点与Ch28具体NC已独核落ledger，root已实际读并许可formal。5分必要深入完成、具体已有覆盖Books0；不当Report去重、不降池、不称本稿新实验或强定理已吸收。上文拟状态是过程记录；当前无需书稿PRE/POST或写锁，Report已正式同步本条，仍不授DAY。
