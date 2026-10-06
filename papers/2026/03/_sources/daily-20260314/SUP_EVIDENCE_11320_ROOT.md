# 11320 UniCompress：必要证据与表示 owner 差额

root；精确[2603.11320v1](https://arxiv.org/html/2603.11320v1)。本次实际打开HTML并读§3全部机制/Eq1–8、§4.1–4.5/Tables1–4、§5及Appendix A System/Ng；不读引用论文全集、代码或复现。日期复用本日`SUP_DATE_SECOND.md`和`SUP_DATE_11320.raw`的官方日程下界＋owning/findable精确DOI/URL注册上界，两端同Mar13北京时间日，不以Submitted或注册单独充当首公开。

## 实际机制与最低投入

原dense visual grid同时作理解条件与生成目标，输入侧选择式压缩不能自动缩短生成序列。这里保留learned global queries提取的G及spatial average-pooled local features；理解直接消费连续G/local，生成预测其量化indices，外部masked autoregressive decompressor再以global/local为条件展开原dense grid、交image decoder。压缩的是LLM接口，dense重建工作转交另一个consumer；局部token T/s²之外还加Ng和specials，不把4×局部缩短说成全接口4×。pool发生在feature而不是离散ID。§3一处共享codebook措辞与另处Eg/Ex记号不一致，不认定已核唯一代码配方。

训练stage1冻结LLM并适配外部模块，stage2冻结tokenizer后finetune LLM；architecture/interface不改不等LLM weights不变或training-free。实际delta为双向视觉接口的压缩/展开责任分离，**2+2+2=6**，仅该长期owner差额深入，不给pooling、resampling或rate-distortion成熟原则另计分。

## 可采用的边界与反侧

§4.1六架构均用Llama3.2-1B版本，不是六原厂已发布模型的无训练热插拔。非diffusion主要256image-token/s2/Ng4；OpenUni/BAGEL对diffusion输入输出采用略不同方案，不外推全接口matched。Appendix A单node Ubuntu22.04、Xeon8468V、8×H10080GB、multiGPU DP；precision、serving concurrency及SLO未披露。JDB+ShareGPT4V_PT一epoch bs128/LR5e-5，再ShareGPT4V一epoch bs256/LR1e-4，不是只少量codec预训练成本。

Tables1–2否定普遍minimal loss：UniTok GQA55.71→53.07、MME1162.5→1036.05；BAGEL MMMU34.05→27.80；OpenUni FID16.45→24.29/CLIP26.7→22.3。UniTok compressed CLIP Table2为25.0而§4.3写22.0，记录数字冲突不拼合。Table3理解/生成训练分别测，不等joint training总费；UniTok generation32.25→18.96min而understanding5.41→5.25min，VARGPT理解5.45→5.43，不能按输出token数推各负载普遍提速。Ng/dense autoregressive reconstruction有额外串行/训练费用，Fig5定性消融不证明唯一因果与所有细节无损；Table4 learned pooling/strided conv某指标还优于AvgPool。不采无损、免费、全部更快或实时保证。

## Actual owner / PRE proposal

已实际顺读Ch23「统一Visual Tokenizer也可以拆分表示责任」至rate–distortion开头与407–418 artifact合同。现文有semantic/topology/residual texture分责和latent→consumer容量联合，尚未具体解释理解continuous入口与生成compressed indices、另一个AR decompressor接管dense展开的接口分支；不能以主题相同认定NC。owner为`MULTIMODAL-REPRESENTATION`，Ch24只交接生成范式，不重复压缩协议。

拟在Ch23 rate–distortion段的联合四轴框架后、传统codec共存段前插入以下两段，独立Source/PRE通过才写：

> 同一视觉表示既供理解、又作为生成目标时，压缩还要分配两种消费者的责任。输入侧删减 token 能让理解模型少读，却不能自动让生成模型少写；一种替代分支把稠密网格压成少量全局摘要与按空间池化的局部特征，理解路径直接读取连续表示，生成路径预测对应离散码，再由独立的条件自回归解压器展开稠密特征、交给图像 decoder。统一的是压缩接口，而不是两侧消费协议完全相同；全局查询、局部布局、码本和展开顺序需共同进入 artifact identity。

> 这条分支把大模型的长序列工作转交给重建模块，并非消灭细节生成成本。外部模块预训练与下游模型适配仍需计费，接口不改也不等权重不变；生成端缩短序列的收益，不能推成理解端同幅降时延。[受限统一视觉实验](https://arxiv.org/html/2603.11320v1)中，不同理解指标和生成质量均有反退，额外全局 token 与自回归展开也改变总预算。应分别验收理解、生成和包含解压的实际延迟；细节损失、展开瓶颈或无法重新适配时，保留稠密表示、理解/生成双 codec 或原压缩操作点，不把稀疏接口写成无损热插拔。<!-- source-family:SF-2026-ARXIV-2603-11320 -->

未写Books、未授单项POST或DAY；独立复核应检查差额是否真正未被具体正文承载，不能为增量而重复现文。
