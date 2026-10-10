# 10379：MoE expert/attention allocation必要Source与frontier争议

仅补充Mar12 BJT自然日，第二包完整精确v1题摘/独立准入及日级arxiv夹证复用。官方`https://arxiv.org/html/2603.10379v1`，原件`SUP_CORE_10379.raw/txt`/manifest-result GET200 UTC2026-10-09T15:33:54.426471。作者实际读§2–4/所有公式与Table1、§6–7、A.1–A.2完整推导、B.1–B.3/Table2完整、C.1–C.4完整FLOP口径、D.1–D.3/Table3完整。Figure1–5只采用实际caption/正文说明，不认证像素点值或可视误差；E仅补图不影响以下决定断点，没有扩全代码/引用或复現。

## 实际贡献/评分/必要深入

固定总/active参数或sparsity不足以决定内部计算布局→本文将expert对attention FLOPs ratio与激活比例作为scaling fit坐标→若真实frontier可靠可改固定预算架构设计。这是具体预算分配命题，不以MoE/scaling标签或重复Chinchilla原理准入。拟`2+1+2=5`：重要架构预算资格2、单模型资源配置1、可复用frontier/fitting资格2。新公式/经验frontier直接影响设计，反证必要深入已执行；拟中心争议/暂缓Books0，等待非作者实际独核，不正式计候选或把争议删池。

## 原方案/方法/人口

§2的`r=C_E/C_A`是ratio，不是摘要模糊的“fraction”；fraction应是`r/(1+r)`。`S=(E−E_act)/E`，B.1固定每token1shared+2routed，E17/33/65/129→S82.35/90.91/95.38/97.67%。同benchmark label守per-tokencompute、改变attention/expert维度，depth/heads同label不变，r∈[.2,1.5]。总参数100M–5B、最大training FLOPs1e21，称六benchmark sizes但Table2仅五active labels20/30/55/100/200M，A100cluster、ctx4096、vocab128k；各label batch96/160/224/320/512，LR.0015/.0013/.0011/.0009/.0008。未给cluster大小/precision、实际完整tokens/optimizer与seed/repeat、数据清洗/split身份或rawloss grid。

B.2只有中文15%/英文60%/code25%与web/code/books/math领域比例，没有精确公开训练语料artifact；text+code不是图像/音频多模态实验证据。作者6.2也限AR-LM固定sparsity，无adaptive routing或硬件通信成本，不能授端到端cost-optimal/SLO。

§3从各budget loss谷选r*再拟合`alpha_r=6.7e−5(1−S)^−1.23`、`beta_r=.24(1−S)^.21`及r*=alphaC^beta；Eq2拟合N/D/S/r extendedloss，Table1给九参数。Caption Figure3 held-out仅S97.67整组没用于fit，Figure4单30M-active/550M-total/S95.38曲线。没有像素点/误差数值/CI/多seed身份，不把“smooth valley”等于无噪声真frontier、holdout一组等于所有规模外推。

## 决定断点与直接反侧

1. **B.3按预期单调性换掉实测minimum。** 原文明确实际r*随FLOPs增加却下降时，若其与符合预期的suboptimal点loss差<.001，选择后者为“theoretical optimal point”。小差值可用于不确定性集合或预先定义的regularization，但不能又把选择后的单调趋势当独立经验认证“最优r*必上升/不是randomvariation”。需要分别报告raw minima、误差/near-optimal集合与受约束frontier，不擅自指控数据造假，也不否定所有近最优配置。
2. **A.2的普遍精确幂律不由给定FOC推出。** 令p=gamma_A mu_A、q=gamma_E mu_E，A.1的loss是`a C_A^−p+b C_E^−q`。固定C=C_A+C_E的FOC给`a p/C_A^(p+1)=b q/C_E^(q+1)`，代入后应是`r^(q+1)(1+r)^(p−q)=(bq/ap) C^(p−q)`，不是Eq4所给alpha/指数`(q−p)/(p+q+1)`。一般含(1+r)不能抽成该精确C幂律，符号方向亦可相反；例如a=b=1,p=1,q=2（取mu=.5/gamma2,4满足其mu范围），真实关系`r³/(1+r)=2/C`随C增而r降，Eq4却给正指数1/4。这个反例否定给定假设→其精确closedform，不证明全部empirical近似幂律不可能；特殊p=q可常ratio、asymptotic也需另定义条件。
3. **资源/拟合身份未闭合，不能原系数当配置器。** §2/Figure2/§3说per-token C，§3.1/§4又说total training compute；B的同per-tokenlabel与1e21total都在，C单位/normalization须具体绑定，alpha有单位依赖。Eq2使用capital R而必要定义没有提供它与r/r*的明确变换；不能自行补成misallocation距离或直接实现。C.1的value应用写成`2 n_ctx d_hidden²`而常规attention权矩阵乘V应`2 n_ctx² d_hidden`，后者并非output projection同式；C.4 backward factor2/3与checkpoint混合口径还需绑定total而非擅自更正原实验。不同实现可能自有实测口径，当前不从FLOP文本断言实际计算都错。

原Fig3 S97.67 heldout 与Fig4有限曲线仍保留为作者的验证设计，不认证完整数值/真实统计显著。D.2称r/(1+r)有界和单调能表达饱和，但这些性质不单独证明实际allocation loss、r=0无人工penalty也不是可训练MoE模型合理终点。D.3比较旧fit只caption/正文，没有同预算原点与unseen误差，不据此宣布所有旧scaling公式失效。

## actual唯一owner / Books边界

唯一 `WORLDVIEW-SCALING-LAW` [Ch7](../../../../../books/part-01-worldview/07-scaling-law.md)：作者实际完整60–133联合N/D/compute预算、Kaplan/Chinchilla/架构exponent及joint surface/原grid→holdout资格。这里负责frontier与拟合/实验身份，不因论文名字默认Ch21。另实际Ch21 224–266完整compute leverage与总/active预算/稀疏单位前后，用作MoE设计交接；现文已有branch ratio、top-k、dense-core/communication与模型/executor分责，不授通用ratio常数。

Ch7当前真实保存grid geometry/objective/optimizer/uncertainty、经验局部fit不等真实frontier；新中心公式/最优单调性尚未成立，**争议/暂缓，新Books0，不冒称已经吸收本稿新公式/实验或用主题coverage缩池**。没有书稿PRE/写锁请求。重开只针对raw minimum与near-optimal集合/先验选择分层、FOC到formula的实际条件、C/R/FLOP/artifact身份及独立heldout统计误差；不追无关完整实现/全部附件。维持5分反证必要深入投入。

## 非作者实际终态通过

mar13_admission_review已直接精确v1必要范围、manifest及actual Ch7 45–142/Ch21 224–269完整邻接回核，独核ledger末10379具名记录支持2+1+2=5、必要深入完成/争议暂缓Books0。作者实读该裁决、root确认后正式同步本日报第16项；唯一owner为WORLDVIEW-SCALING-LAW Ch7，不是Ch56。没有Books写/POST请求，不授DAY。
