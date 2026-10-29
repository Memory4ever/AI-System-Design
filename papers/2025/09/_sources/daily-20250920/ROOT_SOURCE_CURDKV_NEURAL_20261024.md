# Sep20 补充：CurDKV 与 NEURAL 的必要证据

作者§106确认未开始/无在途后，root明确接受两项唯一首次必要Source。原完整题摘/准入、各6分和§106日证不在本层重做；日期仍由Einstein一次实际采用，作者负责本包唯一非准备者实际采用，再比较当前Books。本文不是实现验证或整日验收。

## 原件与实际范围

两精确v1均于2026-10-24 UTC00:19:59～00:20:01实际结束，200/exit0、无在途；原件和同base `.request.json` 均持久保存：

- [CurDKV 2509.15038v1](https://arxiv.org/html/2509.15038v1)，`ROOT_CORE_15038_20261024.raw`，466510 bytes，SHA256 `d60f2a538f9f2175921148ffcf306d11af4ab9180558a7a2f28cabd137c596ed`。实际读§3/Alg1/全部Lemma3.1与AppendixA证明、§4～5/Tables1～4、C.3/C.4及完整Table17。B任务模板与C其它全榜未读，不设全表配额；Fig3～5只caption/正文，不补曲线上精确值。
- [NEURAL 2509.15036v1](https://arxiv.org/html/2509.15036v1)，`ROOT_CORE_15036_20261024.raw`，130495 bytes，SHA256 `39f4feafffa9d67f9782df2ec3953704edf89a2c1228a9e49de92f86e602a500`。实际读§III～VI、Alg1、TablesI～III、必要图caption/正文。未核全部图像素、Verilog、综合/FPGA运行或复现。

## CurDKV：query-free的选择代理不等attention输出无损

§3对每个GQA group分别读取完整K/V，投影到r=20维，算各token投影后平方范数，K/V分数相乘、归一化，再保留最初s=4个sink及其余top-(k−s)个token；Ada版本再跨head分预算且至少保.2份额。输入是已有K/V而不是当前问题query，因此不需为选择显式物化完整attention矩阵，但也无法从该分数保证今后任意query需要的token仍在。结论明确当前实现是prefill静态选择，dynamic generation压缩为未来方向；不能把§3“可用于生成阶段”当已验证在线动态更新。

它保留原token行而非返回一般SVD基底，表示接口有实际区别；但印式不构成完整CUR分解保证：未构造C/U/R重建目标或证明所选行最小化真实attention output。原Alg1先就地把K/V改成KG/VG，最后从同名矩阵取行，却声明输出维度仍d；投影r与原d不同时不相容。若实现保存原K/V并只用投影算分数可另有合理路径，但本次未审代码，不能把该修正倒写成原伪码已闭。zero分数归一、k≥s和位置/时间索引映射也需另给合同。

理论与实际选择须分开：Lemma3.1对同形矩阵、删行位置以0填回，给出粗界 `sqrt(n)||V−V'||F + 2sqrt(n)||V'||F`。证明称row-stochastic矩阵operator norm“恰sqrt(n)”不对，例如均匀矩阵为1；但其上界≤sqrt(n)足够完成不等式，**不据这一表述错误否定该粗界**。第二项没因压缩比例高就一般变小，界也未识别所选K/近似query条件，不能认证某代理近最优。0填回的K仍占softmax分母，真正删除行会改变归一化；取零query、两行value为1/2，只留第一行时0填回输出.5、删除后输出1，是两不同算子，不把此界直接当实际短cache误差证书。

§3的leverage解释另有具体断点：薄SVD的U/V各r个正交列时，全部行平方norm之和为r，不一般为n/d；所印按n/d归一也不一般成为概率分布。直接Gaussian投影的行范数期望保留的是原矩阵行能量，不等白化后U的leverage。有限代数例A=diag(100,1)：完整rank2的U=I，两行leverage同为1，而投影能量期望为10000与1。未给whitening/预条件或适用谱假设时，不能借所引随机线性代数结果签“实际计算了可靠leverage近似”。以上只限定理论/recipe权限，不证明实际code错或局部实验无效。

§4在Llama3.1-8B-Instruct/Mistral7B-v0.3、LongBench16任务/Ruler八NIAH且最高16K，问题不参与压缩。所有baseline由作者重跑，单A10080GB上H2O因其实现不兼容FlashAttention而OOM，不是H2O算法的一般内存下界；GQA/FA兼容声明也不能替具体kernel/位置映射运行验证。LongBench的F1/ROUGE/分类等任务score不合称同一种真实正确概率。

直接反侧：Table2中Mistral90% eviction时CurDKV平均29.1低SnapKV32.6和AdaSnap33.2；主文相应文字却用33.2/32.7等不合表。30%时Mistral AdaCur46.4高Cur45.6，而文字称45.2；Llama AdaCur48.9与文字49.1不同。只保原表/原文差额，不择漂亮值或全任务“始终优”。Table4在Mistral90%时Cur7.8/AdaCur3.9明显低Chunk19.2，若干子任务为0；sliding-window是作者解释，未有隔离实验不能当已识别唯一原因。Llama30%98.7不等full99.6无损。

Table17直接消融也不支持“加random/组合最可靠”的全句：30%平均K38.7、K+random40.6、KV48.0、KV+random47.2、V48.3、V+random48.0；90%分别23.3/25.0/32.3/31.8/35.2/33.7。V分支总体可更高，random在KV/V上反退；部分格另有反序。没有完整随机重复/CI，不用Friedman omnibus及打印p=0签特定两方法处处显著优或统计概率真为0。

§4.4/C.4效率文字亦须隔离：128K的80% eviction，cache从15.6/约16GB到under3或under2两口径未齐；prefill约10→14～15秒有新增选择费，decode叙述一处约10→under6，另一处约12→4.5、Snap全量基线又15。未披一致output length/采样、batch、精度和测量边界，不拼成40%端到端加速；prefill增量甚至可抵decode收益。质量实验最高16K与128K运行时不是同一已验质量人口。r20投影、完整K/V读取、随机矩阵/排序、sink/metadata/indices、gather/缓存更新及独立query/多任务回归全付费，逻辑KV减少不等进程峰值显存或并发goodput。

有限支持为“value及key能量可以成为不依赖当前query的token保留代理，代理/预算分配、真正短cache计算与完整质量—延迟需分别验收”；不采精确leverage/CUR最优、任意query保真或统一净加速。失败时保fullKV、较低压缩、已验sink/locality与原实现，不把理论名词替丢失证据签字。

## NEURAL：分离稀疏检测与神经元执行，不把单timestep当单时钟

§III～IV将两种负担拆开：PipeSDA从有效spike坐标生产受影响卷积窗口/事件索引，EPA以S-FIFO/W-FIFO配对供给计算；PE内按event FIFO读权重、更新LIF membrane potential并判阈值。架构层data-ready、神经元层event-driven，不是传统dense矩阵只换一种消息名称，也不保证任何稀疏度都净快；索引、窗口扩散、FIFO/backpressure/权重offchip调度仍是工作。

QKFormer分支在写回路径按Q的channel bitwise-OR生成activation mask，再门控K写回，不是softmax(QK^T)V的等价实现，不能直接迁移“兼容Transformer attention”或用于任意LLM权重。加入该块同时改变网络架构/层深及spikes，算法质量与硬件运行需要分开验证。

W2TTFS把pool窗口的spike计数映射为时间/权重比例，再由FC core以1/window²的unit权重重复累加计数次，避免每次任意比例乘法。它是输入编码/执行时间的交换，不是压掉工作：model的一个timestep内部仍有编码、多个累加和pipeline周期。Alg1的二维位置印h*w而非通常flatten，h=0的不同w会同索引；长度window²却用最大可达window²的spike count直接索引，后loop仅到window而非window²，无法据印式闭合所有计数。这里只指出伪码边界，未运行硬件、不能宣称实际RTL必然如此；不私补代码成已验证recipe。量化/溢出/舍入也限制pool值与FC精确等价。

训练先ANN ResNet34 teacher，再KD训SNN，融合/量化后做KD-QAT，推理再替换AP；因此质量收益不是硬件调度单因果，单timestep不等零teacher/额外训练费。CIFAR10/100、VGG11/ResNet11/19/QKFResNet11、τ.5/timestep1，RTX2080Ti、batch128/300epochs；FPGA为Virtex7 XC7V2000T/200MHz，Verilog/Synplify/Vivado实现流程由作者报告。正文fixed-point量化和TableIII FP8的具体format/运算合同未完整交代，不自行统一。

TableII是关键直接取舍：CIFAR10 ResNet→QKFResNet，spikes76K→72K减少，accuracy91.87→92.01略升，但latency7.3→9.7ms、energy5.56→8.14mJ均更差；CIFAR100为83K→84K、66.94→68.53、7.5→9.9ms/6.44→8.26mJ。故少事件不保证净快/省能，新增attention/深度的成本必须入账，不能只摘1.59个百分点或spike suppression。

TableIII跨平台同时换FPGA系列、架构、模型和precision，不是相同模型/质量的隔离比较。ResNet行91.87对旧MobileNet91.90少.03pp、136对90 FPS多46，但normalized efficiency .65/.37约1.76；1.97倍来自另一VGG行.73/.37，其93.45/FPS68不同，不能把三项拼成同一配置。.65/.73是按kLUT归一的指标，不是总服务能效；原表SiBrain84.16 GSOPS/W还高于NEURAL46.65/52.37，只有资源归一后排名改变。prose某平台power1.34与表1.53亦保口径，未给完整仪表/估功方法、host/外存/IO与温度边界，不认证整板实测优势或真实端侧续航。

全费包括ANN teacher/全部KD-QAT/模型选择、量化融合与memory images、稀疏检测/索引FIFO、全部weight/activation搬移、LIF状态、QK写回与W2TTFS重复累加、独立质量/功耗/时延回归。未核全accuracy曲线像素、完整多seed/CI和真实traffic/SLO，不从不同模型榜推任意输入/稀疏性普适；spiking LLM明列未来，不当本篇已验部署。有限支持为“稀疏发现、供给/调度、实际神经元和读出编码各有成本，算法表示与执行路线需联合验收”；dense/原ResNet、较简单event路径和已验pool/FC仍有合理退路。

两篇支持与关键反侧足够即停，原各6与候选不因理论/表格限制删除或降分；未审全部代码/曲线不虚构外部阻塞。交作者唯一实际采用后再做具体owner判断，不由本包预NC/I/DAY。
