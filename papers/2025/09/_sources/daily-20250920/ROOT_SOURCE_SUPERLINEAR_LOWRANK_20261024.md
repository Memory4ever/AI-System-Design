# Super-Linear / astralora：有限必要证据

作者280确认两项日门及原各5分已独核，必要CORE/Methods尚未开始、无请求在途；root明确接受后首次捕获并准备。只转必要首域，不转日期、评分、README、owner或Books写权。作者唯一另一角色须回下列精确原域实际采用，Einstein随后仅角色复用，不第三相同必要域。

## Super-Linear — 2509.15105v1

[精确稿](https://arxiv.org/html/2509.15105v1)、[raw](ROOT_CORE_SUPERLINEAR_15105_20261024.raw)/[请求](ROOT_CORE_SUPERLINEAR_15105_20261024.request.json)：UTC2026-10-24T11:00:38.344538至11:01:29.210639，200/exit0，722083B/SHA256 `db36da0185529608e82d2367231053b5b2199b49b5efc52a0c0811b299797b57`。标题为 Super-Linear: A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting。

实际完整读§3/Eq1–6及内嵌T1，§4.1–4.3/T2–3、§5条件性界、C.3、F/T12–13、G限制、A.4/A.6整T8与A.7/Alg1。未读B完整证明、全部full-shot/TTM表、权重或图像素/代码，不复现。支持有限机制、直接控制、关键反侧与全费已足，不要求其它附件。

机制是**以人为指定的频率支持预训不同线性预测器，再冻结它们、训练谱路由与补充专家**，不是所有模型MoE都天然会按频率分工。输入每channel作为一元序列，learnable expert为RevIN→`X[B,T] W[T,H]+b[H]`→逆归一；37频率专家、12补充专家及last-value/mean两启发式共同组成池。输入去均值后的normalized periodogram再线性投影到expert scores，训练加Gaussian噪声.1、top-k/softmax组合到`[B,H]`；raw文字说per-column，但`[B,N]`和删除`B(N-k)`的语义要求每样本选expert，不能默修原式/声称已核代码。恒定输入的谱L1为0、M=2500与512输入的padding/谱网格细节未给完整闭合，不自行补guard。频率标签来自采样率和人工谱分析，再插值重采样训练；专家是按这些支持学函数，不是已证明硬频带滤波器或唯一可解释知识部件。stage1各专家独训，stage2只训router/补充分量；两阶段共用训练数据，不能把冻结专家叫零预训费。

长lookback处理另有成本和语义：短于512先插值上采样、输出再缩回，ceil比例与精确512裁切的细节不补；长输入比较scales{2,4,6}的谱能量损失与router entropy，选重采样后再预测，改变真实时间/频率坐标，不恢复额外观察或丢掉的高频。**Alg1第19–21行接受更好score后未更新`score_best`**，所以印刷算法可能选择最后一个优于初始值的候选，而非遍历候选最小值：初始10，先1再5，两者都低于10，会最终返回5。`E_total`、边界空集及omega_min说明亦未全闭合；不将该printed接口作为可靠完整搜索recipe。能量保留/低entropy不等预测最优或无损时域。

单RTX3090 24GB/PyTorch/Adam/MSE，无aux loss；lookback512、训练horizon96、更长预测自回归。stage每数据最多100k/总1M样本、按频率均采，80/20时间split；30epoch/patience5，ZS top12，full-shot验证选择不同k。外部模型训练语料、量/采样分布、lookback及预算并不完全匹配；T1 dash含已见训练集或未报告，不能按缺项判胜。2.5M参数对84M等不是墙钟、FLOPs或显存同倍数收益；原作者head计数与表尾计数口径不拼成统一新统计，headline均值百分比不外推所有任务。

直接反侧保留：T1 ETTh1平均MSE .402弱于Time-MoE Large .394，ETTm1 .382弱于Timer .373；T2 ETT2-12h .509弱于TimesFM .456/Chronos .483，ETT2-D .586弱于Timer .536/TimeMoE .557。T3总体去两阶段较差，但去complementary的GIFT MASE仍.857同full，T8 ETTh1去complementary .365优于full .369、ETTm1 .314/.350亦优于.317/.352；不是每部件/任务均获益。A.4补充专家更多可退，k的重训与推断变更因数据而异；固定频率不适配罕见/瞬变、非线性相互作用及512以外完整context。§5界要求输入/输出相同周期、理想权重和受控expert范数等，不是频率支持自动完备、router必收敛或通用ERM泛化保证；B完整证明未核，不授其定理全通过。

费用计全部数据整理/人工谱分析、所有插值与独立expert预训、stage2、互补/启发式与FFT/router、每scale搜索/全部候选前向、top-k和长horizon递归、验证选k及独立质量回归。完整墙钟/推断延迟/precision/并发/峰memory和跨配置seedCI未披不补。固定采样率/简单依赖可保普通线性/naive/shared MoE；频率漂移、谱归一或重采样接口不可靠时保原时间坐标/可信数据与原模型，不能用少参数/解释性激活批准普遍快或语言模型迁移。

## Low-rank surrogate modeling and stochastic zero-order optimization — 2509.15113v1

[精确稿](https://arxiv.org/html/2509.15113v1)、[raw](ROOT_CORE_LOWRANK_15113_20261024.raw)/[请求](ROOT_CORE_LOWRANK_15113_20261024.request.json)：UTC2026-10-24T11:04:42.399729至11:04:58.760743，200/exit0，286815B/SHA256 `cb68cab4daf90241d9623d86f29731456bd1544be1bf990cf2dd794fe5d83907`。

actual完整读§2.1–2.3/Eq1–4/Alg1–2、§4全部模拟层资格、§5.1–5.3/T1–3及必要图caption、§6。误先按编号读取的§3是related work，不拿所引工作/宣传数字作已核原始结论；不扩其参考论文。未图像素/代码、真实光学硬件或训练复现。

核心分三种更新：真实forward调用可调参数omega的BB；对输入的反传用在线低秩surrogate `A≈USV^T`，`U[d_out,r] S[r,r] V[d_in,r]`，将下游v映为`VS^TU^Tv`；BB自己的参数更新则另用扰动查询估计，不是对不可微硬件直接autograd。BB更新后I-PSI通过`ΔA V0`、随机探针估计`ΔA^T U1`及QR更新surrogate；低秩的是局部反向桥，不是把整个模型换成低秩、普通LoRA或压缩了全部设备参数。需要可编程/可扰动omega及前后配置查询；一个只能调用且不能改底座参数的闭源LLM API不因此获得训练权限。若BB输入本身线性且surrogate恰等真实A，输入VJP可以准确；rank截断/估计不准时是有偏反向近似，非自动无损梯度。

**印式与可执行训练必须分开。** Eq3与Alg2第14行把参数gradient写为若干内积标量的平均，遗漏与方向`u_i[d_bb]`相乘，结果是标量而不是`[d_bb]`参数梯度；在零点的最简单标量线性函数`f_w=w`、v=1、对称Gaussian方向下，原期望为E[u]=0但真导数1，也不能直接沿印式训练。通常的方向加权公式能解释拟机制，但这里不代作者静默修正或指控未读代码照错实现。Eq4/Alg1随机transpose-action把M_sm项直接求和、未除M_sm；Gaussian期望下其期望是M_sm倍的`ΔA^T U`，不是原称目标。Alg1还用U而未明确U1绑定；保持rank流形/QR稳定也不证明这份随机近似的正确比例或全网收敛。这里保局部印式争议，有限模拟结果仍是作者报告，不作整篇贡献EX。

每BB参数VJP作者记M_BB+1次调用，surrogate更新脚注明确`2r+2M_sm`，正文“r/M次”只差分probe个数，不应漏两份omega查询。批次能否物理并行、读出/传输/配置切换与更新digital参数还另计。向量输出oracle可在d_in次基向量查询得到完整矩阵，不能把文中`O(d_out*d_in)`元素规模直接当不可避免的同口径query下界；比较需写明oracle一次返回什么、是否缓存和总数据量。初始化surrogate、随机估计质量与实际设备噪声/漂移仍需独立检查，不以online一词跳过制备/校准。

**仅软件模拟，不是真实光学训练或净硬件加速。** 五类转移矩阵含matvec/MRR/SLM/Monarch/MZI系列；输入线性而参数映射可非线性，SLM假设可读复场实部。whole-MLP实验又把非线性整个block视作BB，不能自动沿全局线性`A_omega`证明或原I-PSI等价。MZI模拟太贵，audio/LM排除；实际硬件无这些数字模拟开销是作者展望，不提供读写/能耗/墙钟测量。

CIFAR一层替换，r∈{1,3,5,7,10,50,100}/M∈{1,10,100,1000}各五seed，曲线只文字/caption，未图像素不认证具体接近幅度。UrbanSound8K ECAPA替6144×192、M_BB=M_sm=1000，五次均值未给表CI：数字baseline78.50，MRR r10为77.07、r50退75.53、r10076.53，SLM77.94→77.78→77.89亦不随rank单调；Monarch79.75只该实验。FineWeb子集/GPT2-like417M从末层起替换：linear12层PPL30.26–30.87对23.80，wholeMLP12块30.87–32.13，能训练不等近乎无损/实际能力保持；数字可梯度更新参数190M不等所有设备参数/常驻资产变190M。LM M_BB100/M_sm1000，重复seed/训练token/全部配置/硬件precision与统计不确定性未披不补。

全部真实BB/扰动查询、前后配置评估、随机探针、QR/因子驻留、digital前后层反传、设备校准/通信及端到端独立任务回归都付费。既没有生产吞吐/SLO，也没有凭低rank保证任何非线性模块的精确Jacobian。可微模型仍用原反传；不可得参数访问、surrogate失配或质量/总查询费不可接受时，保冻结硬件/可信数字替代、已标定接口或原训练路径。原5与拟局部反向桥分责保留，是否已有覆盖/暂缓及Books采用由作者具体owner下一层判断。

两次原件请求已全部真实结束，无root在途。待作者唯一另一角色回上述有限原域实际采用；原日期/评分/全部正反侧保持，不预标准完成、NC/I或DAY。
