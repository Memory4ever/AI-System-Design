# 02436 GIM-World：必要证据、六分与Ch25最小PRE

仅Daily2026-06-03补Jun02 BJT。已恢复AGENTS/当前研究与Report合同、来源使用/Daily/arxiv恢复、统一入口、ROADMAP及当日停点；开始owner比较前读项目背景/学习理念/写作指南。R62完整题摘/准入与联合Jun02日证有效复用。当前[官方abs](https://arxiv.org/abs/2606.02436)唯一v1，所见无撤回/纠错；Jun01 16:08:43Z提交不直接当公开日。未见具名更早正文新信号，不扩假想渠道。

## 实际读取及采用范围

实际读[exact-v1 HTML](https://arxiv.org/html/2606.02436v1)§3.1–3.5/式1–20、§4.1–4.3/T1–4及直接图注、§5；HTML正文后无需要支持本采用的附录。未看图像像素/全部视频、核代码或运行复现。必要支持及直接反侧足，停止。

固定learnable queries与带camera embedding的历史patch一起经过两块encoder，输出首Nm个memory tokens供DiT读；attention分支compact而FFN保持全分辨率。Nm等于20个latent frames的patch-token数，不是20个token。它不是不看历史即可递归更新的已证状态机；固定输出容量不免形成memory的历史读取/筛选和原始history存储。

固定slot不再一一对应frame/patch，因此不把VGGT特征直接逐slot对齐。训练每步均匀抽一个历史camera，将ray origin/direction与grid位置作query，geometry head跨读memory后预测该视图VGGT patch features，以cosine loss联合训练encoder/head/生成器；frozen VGGT作teacher。均匀单帧抽样对固定all-frame平均目标的无偏性不证明长期几何正确或teacher真值。推理丢geometry head和teacher，camera-indexed history/encoder仍需运行；辅助读出约束的是训练记忆保留的方向，不授公开可执行几何地图或真实transition。

剪枝在pose/forward-direction/time的GP kernel下选最多K=200历史帧，使保留与丢弃集合的模型MI较大；这是camera-time proxy，不是图像语义或遮挡后的真实信息量。完整kernel/候选搜索与保留原件另有成本，不能由K或固定Nm推出整个历史维护常数。论文由submodular直接称greedy near-optimal未给本有限集合单调等条件；自己的边界检查是F(空)=F(全集)=0，非退化相关时中间集合F>0，故不凭submodular一词补标准单调greedy保证。此不否认所测启发式结果，也不为未采用最优保证扩全部引用证明。

Wan2.1、MIND UE5视频，100 first/100 third clips各50/50训练测试，前约1/4观察后3/4按同actions生成；720p评价，Nm=20latent-frame patch数/s2/K200/lambda.05/8ksteps/LR1e-5/batch32。精确GPU、完整precision/生成采样/全部训练预算与重复区间/SLO未披露。Matrix/MIND数字外借，其余具名基线重训，不能把所有表项当统一完整matched budget；“four retrained”与三种具名重训分支口径未补造第四项。RPE由ViPE估计再Sim3对齐，reprojection由DepthAnything3估计，不是真实物理控制误差或无偏全场景几何oracle。

T1 first-person translation .0247劣于CaM .0235，不能采所有action项均不退。T2直接memory监督较generator-feature监督改善有限几何指标，不证明此分工普遍必要。T4 full attention MSE .0608/reproj81.85仍好于默认.0614/81.70；默认LPIPS更好，不能说完全无损上界。0.26%只是所测encoder/DiT相对runtime，不含teacher造标、训练、全部历史筛选/存储、quality回归及服务SLO；不补硬件或净端到端常数成本。千帧单场景图例不证全世界全局一致/长期无漂移。

## 评分与实际owner差额

拟2+2+2=6：只计非frame-indexed固定记忆通过camera-query辅助读出接几何监督，以及训练消费者/推理消费者的分责，不借普通distillation/世界模型名或大幅指标加分。actual长期小gap定点深入。

actual完整读Ch25“World Model不必保存全部Observation”query closure组、Memory开头ZipMap两段、其后Mem3R两段及recent/view-indexed/MemCam完整组。ZipMap解释观察导出的fast-weight场景查询，Mem3R解释camera与geometry不同状态消费者；它们尚未承载压缩后无逐frame身份的生成记忆如何用历史camera重新建立几何监督对应、推理去掉辅助teacher/head的接口，不靠没marker认gap。Ch24生成因子化/commit与Ch26物理controller开篇交接已读，不重复其算法或给记忆授行动。唯一`MULTIMODAL-WORLD-MODELS`/Ch25。

拟位ZipMap完整第二成本/边界段后、Mem3R“固定容量场景状态还可按消费者拆分”完整首段前。只原两段及本人注，待独立必要/正式分/actual gap/PRE，不预SAVE/I/DAY。

## 原两段PRE

固定容量也可以服务于生成记忆，而不直接成为可查询的几何场。当压缩slots不再逐一对应历史frame/patch时，强行与teacher特征逐slot对齐会重新引入任意位置对应；另一分支保留历史camera作为训练查询，从同一memory读出该视图的patch特征，再与冻结几何teacher的输出比较。[受限的camera-query监督](https://arxiv.org/html/2606.02436v1#S3)将这个辅助head与memory encoder、生成器联合训练，推理只保留条件memory与encoder，不再运行辅助head/teacher。它改变的是记忆被要求保留哪些可读方向，而不是把teacher估计变成真实地图、可逆历史或已验证transition。

固定输出slots仍不等历史维护常数：编码前的候选筛选、pose/time kernel、原件存储和读取都需付费，有限预算的相关性代理也不证明真实可见性或最优保留。局部对照中直接约束memory优于只约束generator，但camera误差仍有反退，更强attention压缩会损质量；相对DiT很小的encoder计时不含完整训练、筛选和回归。应分别验memory读出、生成质量与实际运行预算；teacher/相机、场景或长程保持失配时，保显式view/geometry bank、较短可信context与新观测校正，不由几何一致分数批准无限无漂移、真实状态或物理行动。<!-- source-family:SF-2026-ARXIV-2606-02436 -->

拟本人注：`SF-2026-ARXIV-2606-02436` — Daily2026-06-03补Jun02，exact-v1 §3–4/Eq1–20/T1–4，2+2+2=6。仅非frame-indexed memory的camera-query训练监督及推理去辅助head/teacher；保teacher/pose代理、完整历史维护与剪枝费用、greedy保证未闭、translation/compact反退和单场景千帧边界。未核图像素/代码或复现，不授真实地图、全局最优、恒定总内存/净SLO或行动安全。PRE/SAVE/POST按实际后记，不预I/DAY。

## root实际采用

R169首次必要/正式6/actual owner与原两段PRE通过后，root在ZipMap完整第二段后/Mem3R完整首段前实际保存，R170唯一actualPOST通过。已行政同步本日Report与本人注，指定位I生效，未授整日验收或新性能/安全结论。
