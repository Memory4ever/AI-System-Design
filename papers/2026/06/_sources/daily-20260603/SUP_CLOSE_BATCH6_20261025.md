# Jun03两决定性定义的必要层与具体owner

02358前root已读必要不冒本文先前已完成：本writer现在实际回读I–III/T1–2才写packet。00289亦实际读v1核心及必要附录，不以题摘准入代替。本包尚未独核/写Books；两项当前官方abs有限notice核只见v1未见撤回/纠错，不作全网保证。首公开联合日证沿本日有效记录，不改原候选归属。

## 02358 CHIMERA — 必要完成，原Ch49单段差额提案

[v1](https://arxiv.org/html/2606.02358v1) / [原件](SUP_CLOSE_2606.02358v1_20261025.html)。已读完整短正文I–III/T1–2/全部figure captions，未核图像素/RTL或实物复现。2+2+2=6：原有峰算力/单cluster局部tile判断→本芯片的两bank交错shared L2及narrow-control/wide-bulk联合仲裁→扩cluster时须把bank冲突与control等待单列，而非加物理总带宽。不是把成熟QoS原则本身当新增，也不因MCU小而排除Transformer系统consumer。

22nm实芯，12mm² die但本研究子系统3.19mm²/60%logic utilization；表拿3.19对别人die面积不可泛称100×同边界效率。TAC16×64INT8 dot、2048op/cycle，8通用核+1DMA核，128KiBTCDM，2KiBweightdoublebuffer，256KiBshared L2的2×128KiBbank；512bitbulk与32bit控制通路。多clusterMATMUL扩展/约2×是**仿真**、物理带宽相同的interleaving对照，不是多cluster实芯吞吐全测。20,000host narrow reads与并发DMA同region/burst sweep为实测QoS；正文34-cycle worst-case但图caption为measured average，仲裁bounded-priority额度未披露，不能授形式WCET或任意持续narrow流量的硬界。固定narrow priority还须system regulation，否则wide starvation。

3.1TOPS/W在200MHz/.6V，896GOPS/600mW在550MHz/.88V不可拼为同点；563Gb/s为aggregate物理L2合同，不是模型端到端。L1→L2doublebuffer能效只少7%属局部workload；TableII **derived from silicon measurements**的MobileBERT/WhisperTinyEncoder/DINOv2S吞吐/能耗不是完整app latency、识别质量或AR LLM decode。INT8“minimal accuracy loss”借已有[9]，本短稿无模型精度表，未采无损。softmax/激活/核管理灵活性与所有DMA/bank/仲裁/制备/模型验收仍计费，inactiveclusters clockgated不能忽略全系统边界。

actual完整读[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)“专用加速器首先是一份Workload Contract”开篇、electro-optic单元组、MTIA闭环及KV packetized fabric两段；另读software-defined placement与chipletL2任务亲和/完成计数组。现文承担workload/精度/状态/平台身份与NoC backpressure，却没有**同一shared L2中bank交错与窄控制流有界优先共同决定扩cluster可行性**。唯一`INFER-TENSORRT-LLM`，拟在本节第一完整段结束“理论峰值可能无法转化为production goodput。”之后、现“专用单元也可以只接管attention的非线性…”之前补单段，不新标题，不拆原文，尚未写Books：

> 多cluster的专用化还会把控制流与bulk tensor流量带到同一shared memory。只增加端口标称带宽，不能消除多个cluster撞同bank；两bank交错先减少这种冲突，窄控制通路再以优先仲裁降低同步消息被长DMA burst阻塞的代价，而持续高优先流量必须受预算限制以免饿死bulk。[CHIMERA的受限实芯与仿真](https://arxiv.org/html/2606.02358v1#S2)分别支持窄读延迟与多cluster扩展，不能合称全系统已测：仲裁额度未完整披露，有限读延迟不授任意流量的WCET，局部TOPS/W也不替完整模型质量和端到端能耗。Bank映射、burst、仲裁与double-buffer费用须共同进入执行计划；容量/控制流不受约束或模型支持越界时，保留较少cluster、受控静态调度与通用路径，而不由峰带宽批准实时SLO。<!-- source-family:SF-2026-ARXIV-2606-02358 -->

## 00289 Inner Product Aware Quantization — 必要完成，Ch49原表示组单段差额提案

[v1](https://arxiv.org/html/2606.00289v1) / [原件](SUP_CLOSE_2606.00289v1_20261025.html)。实际读§1–5、Defs1.1–2/3.1–2、B/C完整证明、D.3/D.3.1及Table1、F.8/Alg11/LemmaF.23；不冒D全部精确/近似证明、F1–7全部proof或代码/复现。2+1+3=6：平均重构误差→固定无偏独立舍入下的平均/最坏方向方差两个不同codebook目标，并给出数据适配预处理的可行算法选择→不能用相同MSE或最坏方差签尾部输入/模型质量。

固定Q、每坐标无偏独立相邻点舍入，坐标方差v_i=(q_up−w_i)(w_i−q_down)；单位球worst input variance=max_i v_i，已知输入分布average variance=sum E[x_i²]v_i，仅在此独立舍入类成立；一般相关舍入有covariance项，C reduction证明优化一般average rounding distribution困难，不是单个weighted MSE必NP-hard。B用单位球+一维最小方差与basis-vector下界证明独立舍入是worst-case minimizer，**非唯一**。原§1.1两个概率写反（Q={0,1},w=.25按印式均值.75），Def3.1漏单位球、§3.3上界把MDV/ADV记号混用；B明确“概率选到无偏”与单位球足以支撑上述窄数学对象，不能把原印公式照做recipe或无说明自修作者实现。

Weighted MSE结构借1D clustering/Concave Monge DAG solver；实用Wilber用s/s+1近似cost差提出Lagrange multiplier窄窗，找不到回全域，非近似估计自动授exact。D.3不同估计器有时间反侧，m4s/200s与10trial LogNormal M4桌面/16GB Cython预处理计时，不是GPU训练/推理加速。F.8区间端点coreset+variance guess/check并随hi缩细bucket；Alg11与LemmaF.23分别写1+eps、1+O(eps)，不采无常数统一界/所有零cost边界已实现。最坏coordinate目标在很多分布上**最坏1%输入事件反弱于average目标**，故不能泛称tail更强。向量检索仅初步证据，每vector码本须另存；量化制备/排序/估计、随机状态、全部codebook/packing和consumer支持计费，未测LLM任务/PPL/SLO或同bit完整驻留，不给不存在的Serving hardware配置。

actual完整读Ch49“先定义低比特表示”affine定义/手算outlier例与后固定非零水平组、“粒度与校准”首段与输入二阶/随机probe组、单Hadamard+dither无偏段及CAT方向对齐完整组；另Ch36只定点核通信压缩未见相同codebook目标。已有MSE/activation敏感、无偏与codebook格式不自动承担**同一无偏舍入类的worst-unit-direction vs input-secondmoment-average两种优化目标及其tail反侧**，不重复泛“局部误差非质量”。唯一`INFER-TENSORRT-LLM`，拟在手算outlier例完整段结束“而不是只寻找最小文件的原因。”之后、现“低位码也可以表示…”之前补单段，不动既有格式定义：

> 当允许为每个向量准备自适应码本时，误差目标还可区分输入方向。固定码本并采用每坐标独立、无偏的相邻水平随机舍入，单位范数输入下最坏内积方差等于最大坐标舍入方差；已知输入分布下的平均内积方差则成为按输入二阶矩加权的方差和。[受限ASQ分析与算法](https://arxiv.org/html/2606.00289v1#S1.SS1)据此分别选择码本，而不是把最小普通MSE称为所有输入最优；最坏方向目标也可能在分布的最坏1%事件上弱于平均目标。独立性、无偏规则与单位球是条件，一般相关舍入、clipping或整网非线性不能沿用这些式子。自适应求解可用近似cost差缩小搜索窗，但失配须回完整搜索；桌面向量预处理更快不等低bit kernel或服务更快，每向量码本、随机状态、制备与完整质量/执行回归仍计费。分布、格式支持或摊销不合时，原固定网格、成熟PTQ与较高精度继续成立。<!-- source-family:SF-2026-ARXIV-2606-00289 -->

## 交付

二项ready交root首次必要/actualowner独核，仅请求Ch49上述两个不相邻单段+各自一注；未获授不写。所有印式缺陷和实测/仿真人口保留，不把可补限定本身当准入理由。CRAM/ProtoAda必要主体与A–C已实际读，具体包另交，不扩其它题目。
