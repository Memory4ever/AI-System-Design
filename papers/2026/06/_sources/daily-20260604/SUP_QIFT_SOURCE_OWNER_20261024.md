# Qift 02823 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author；R27题摘/准入/Jun03联合日证与2+1+2=5复用，不第三AB/date。exact-v1 [HTML](https://arxiv.org/html/2606.02823v1) HTMLfirst完整剥标/保mathannotation原TEXT72253字符实存[原件](2606.02823v1.fulltext.txt)，无工具truncation。必要实际读§3全部/Eq5–18、§4.1–4.2/T3、§4.3/T5、§4.4 layerheuristic与同method差额相关段、§4.5.1–4/T13–15及§4.6/5。止于支持/直接关键反侧，未核所有下游taskcell、图像素、代码、量化产物或实机复现，不把整表/refs强制队列。

## 必要机制、对照和关键反侧

§3.1–3.3固定QuaRot-style Hadamard/scale/GPTQ或GPTAQ/A4/KV4，只替全局四个W2重构level。标准SYM-INT={-2,-1,0,1}；MNZ={±.5,±1.5}，可写{±1,±3}乘s/2。2bit仅四code的标识，不等decode后signedINT2可直接存下±3/4。codeordering由实现选，不补唯一packing。所有layer/module/channel共享grid，**每outputchannel scale仍需clip/MSE搜索**，非免校准或免metadata；无group-grid选择/学习codebook/每channelzero-point。

§3.2/4.2源假设是近零均值且更Gaussian-like，不是旋转创造zeromean；T3两模型224modulemean|mu|/sigma约.01基本不变，标准化kurtosis/skew/Q-Q改善，未证严格Gaussian/全新模型。Lloyd-Max仅源设计prior/reference，不当已验全网最优。§3.3 fractional midpoint z=1.5的四level可等于MNZ，不证明所有asymmetric量化等价或后端可直接支持。

§3.4/4.5.3 G(r)={-1,-r,r,1}；global scale自由时{-3a,-a,a,3a}的a会被吸入s，非独立geometry。r内外比例才是形状参数。100K Llama2rotatedweight按标准perchannel scale归一后pooled，**每r仅搜一个global beta**，不是production每channel重复优化。0.005扫描r约.30，MNZ1/3、PoT1/4、Far1/2；.25–.33是该诊断好区间非普适最优band。T14精确Lloydratio.2998 NMSE.117718稍好scan.30 .117719有离散解释，不拼矛盾或优于自身optimum神话。

§3.6 PoT={±1,±4} decode后符号/移位结构，scale可epilogue；**没有targetkernel实现/latency/TPS实测**，硬件友好是表示/潜在算术，不授GPU整数指令/无解包/端到端加速。MNZ虽无zero，不能由名字推稀疏执行。

§4.1 Llama2-7B/3.1-8B，128WikiText2calibration、seq2048/seed0、single-seed，WikiText2PPL及ARC-C/E/HellaSwag/PIQA/WinoGrande。weightperoutputchannel无group/clipsearch；Asym额外perchannelz；A4symclip.9、KV4asymK/Vclip.95、固定Hadamard，GPTQdamp.01/GPTAQ同校准加activationcorrection。Python3.10.13/Torch2.2.1/CUDA12.1/RTXA6000 48GB GPUs；总卡数/实际量化和请求运行时间、batch/concurrency/SLO、完整evalshot/CI Not Disclosed。FP16 W16A16/KV16是参考非严格所有任务不可超上界。

T5 Llama2KV4GPTQ sym53.849/asym33.533/MNZ20.297/PoT18.580/Lloyd14.856 PPL；说明改level有局部收益，**仍远弱FP16 5.471**，不授pureW2近无损。GPTAQ同列MNZ9.294/PoT9.577排序不同，不能以PoT“硬件友好”签质量最优。

§4.4按逐层单独W4升级PPLgain排序选topL，忽略联合交互；32层nominal avgbit=2+L/16，L16=3只位宽均值，不含scale/packing/rotation/runtimebytes保证。作者同method iso-bit比较：Llama2GPTQ symL16 7.825→MNZ7.318仍差uniformW3A4 6.897；GPTAQ sym7.719→MNZ7.122仍差W3 6.509，不混两method算净因果。Llama3.1GPTAQ在L16可比GPTQ更差，故GPTAQ非通用改善，不用mixedheuristic代新普适allocator。

§4.5.1 RTN bucket诊断与GPTQ/task分账；每channelMSEclip，bucketerr%只grid内部错误分配，不是总error差额。T13总平方误差MNZ降20.7%是实权重重构，不等PPL/质量同比。§4.5.2最靠近zero区域标准grid可更好，MNZ总收益来自全局centroidallocation，**非每weight局部都赢/zero bucket更好**。§4.5.4 T15L16 FarMNZ r=.5 PPL7.982>sym7.825/residual1.020>1；无zero不充分。MNZresidual.778低于Lloyd.794但PPL7.318差于Lloyd7.278，residual不严格排序task。原图像细节未核不据此额外图结论。

全旋转/scale/clipping、128calibration/Hessian补偿、code-to-leveldecode/packing、A/KV转换/实际kernel/任务回归均计费；training-free不免准备，W2字面不等residentbytes/总费。源分布变化、尺度或consumer不匹配时原整数/高精度与普通校准仍成立。

## actualowner与完整锚

唯一INFER-TENSORRT-LLM Ch49。ROADMAP/三Bookscontext本轮完整重读，State2026路由；实际读Ch49开篇、1101–1131表示/PoT/粒度完整相关论证、1491–1558分布/rotation相关及2622完整transform-format段，Ch48/50开篇职责。exact02823/Qift/nozero检索未见本family旧owner，不另建。现有已讲affine grid、PoT算术不等加速、transform与format共同选型，**没有固定同W2bits/rotation/scalepipeline改四level与scale-invariant ratio的分支**；已有通用principle不是NC充分条件。本段不接管runtime量化kernel实测或新结构。

拟仅PoTAcc完整段/marker后、粒度与校准真H3前两段，加本人trueH2注。尚无新授/未写，待首次独立Source/actualowner/PRE。

完整上锚：

低位码也可以表示带符号的单个或多个二次幂项，使乘法改由移位与加减实现；此时权重码宽不等于中间乘积宽。输入整数位宽、最大移位量、零值与符号处理共同决定真实 PE，累加还须另留范围。导出也不只是把原浮点值换成指数：若先经过普通 int8 转换，再恢复目标幂次码，必须按原 quantizer 还原码值、修正 weight scale，并同步重定标 bias，最后才 packing 给匹配的 consumer。[PoTAcc 的受限端到端实例](https://arxiv.org/html/2605.06082v1)还把全部权重预置于 DMA buffer，准备时间与持久容量都不能省去；只支持部分算子的 accelerator 会在跨层 CPU 回退与搬运中损失收益，较少乘法不保证更低延迟。CNN 的转换精度也不能给采用合成权重测时的 Transformer 补上质量证书，扣除 idle 的能耗不等全板总能耗。格式、scale/bias 或实际路径未验时，保留普通整数/浮点 kernel，分别验完整任务质量、准备成本和请求执行。 <!-- source-family:SF-2026-ARXIV-2605-06082 -->

拟增两段：

固定了位宽、旋转和校准流程，重构水平本身仍是独立的设计选择，而不是二进制码天然等于有符号整数。对近零中心、旋转后更接近高斯形状的权重，一条[受限 W2 分支](https://arxiv.org/html/2606.02823v1#S3)把四个码映到对称的非零水平 `{±0.5, ±1.5}`，仍按输出通道选择 scale；也可将它写成 `{±1, ±3}·s/2`，或选择 `{±1, ±4}` 的符号与移位解码。前者改变四个重构位置，后者进一步约束算术结构；两者都不要求学出逐组 codebook，却仍需量化、校准与匹配的解码 consumer，不能把码宽直接当作解码值或累加器位宽。

去掉零水平并非普遍更优：自由 scale 会吸收整组水平的共同倍数，真正不同的是内外水平之比；在所测源上，比例过大仍会比原整数网格差，最靠近零的权重也可由保留零的网格重构得更好。全局重构误差或 GPTQ 残差下降，不严格排序最终任务质量，混合 W2/W4 的名义平均三位也不等同实际三位格式的存储与执行。应共同保存旋转、码到水平映射、scale/clip、补偿算法和 W/A/KV 身份，独立验任务质量与真实 kernel；旋转、校准、补偿、packing/解码及回归全计费。分布、质量或后端支持失配时，保留原整数网格、较高精度与成熟执行路径，不以固定水平或 shift-friendly 名称批准近无损和服务加速。<!-- source-family:SF-2026-ARXIV-2606-02823 -->

完整下锚：

### 粒度与校准决定谁共享同一份误差预算

Per-tensor 用一个 scale 覆盖整块张量，接口最简单；per-channel 沿指定轴使用不同 scale，避免幅度大的通道拖累所有通道；group/block-wise 再把轴上的元素分成更小的共享组。粒度越细，通常越容易贴近局部分布，却需要更多 scale、可能的 zero-point、解包和 kernel 索引。轴、group size 与物理 layout 必须一同约定，不能把同为“4-bit”的 artifact 直接互换。若每组 `g` 个 `b`-bit 值另存 `m` bits metadata，忽略 padding 时每值实际成本为 `b + m/g` bits；例如每 128 个 4-bit 值保存一个 FP16 scale，是 `4.125` bits/value，而非恰好 4 bits。这只是容量算式，不是吞吐结论。

本人trueH2注拟：

- `SF-2026-ARXIV-2606-02823`：Daily2026-06-04补Jun03；exact-v1 §3–4.2/4.3T5、4.4必要比较、4.5.1–4/T13–15与§4.6/5，2+1+2=5因固定W2重构水平与ratio具体差额深入。只采同pipeline的levelgeometry/自由scale分责；保FarMNZ反退、nearzero局部反侧、残差非task排序、pooledratio非production最优与完整费；不授Gaussian严格模型、pureW2近无损或shift硬件加速，未核全taskcell/图像、代码/量化产物或复现。待首次PRE/新授/唯一实际POST。

