# Jun03 具名第三批：连续状态、可撤销采样与近似KV / 待独核

作者`supp_jun03_close`，仅Jun02 BJT补窗。原完整题摘、R26/R28准入/联合日证有效复用，不第三；当前三官方abs均唯一v1，所见无撤回/纠错/更早正文信号。owner前本轮完整上下文有效，实际比较Ch24以下完整机制组，邻Ch23表示/Ch25worldstate职责沿ROADMAP和开篇已读。未写Books/State/index，三项尚不预I/DAY。

## 01024 DSL-LLaDA — 2+1+2=5，真正差额在既有MDLM到连续输入的兼容桥

[v1](https://arxiv.org/html/2606.01024v1) / [原件](SUP_CLOSE_2606.01024v1_20261025.html)。已实际读§3–4/T1–2、§6–7/Limitations、A/Alg1–2、B1–2。保noise100维单位球embedding与backboneembedding两份身份，`z=gamma*e+sqrt(gamma)*epsilon`经全词表softmaxconverter形成backbone输入，监督仍clean token CE，不是把已有LLaDA不训练就当连续solver。训练更新backbone/converter/noiseembeddings；90% per-sequence LogNormal+10% per-token ROAR，不说已实现任意独立tokenSNR schedule。推理cleanprompt clamp，response连续state经top512 posterior-embedding近似、Heun双求值与噪声更新，最后argmax/EOS；top512/learneddenoiser/自选eta不保证原离散联合分布或精确DSL采样。无显式denoisertime不等runtime无gamma schedule；per-tokenadaptive未来工作。

LLaDA8B/FineWebEdu1000steps、8A10080G/bf16/ZeRO2/seq2048/batch32、AdamW2e-5，converter额外25倍LR；同数据/steps/compute的binaryMDMCPT与randomtokenXDLM用于分解输入暴露，但训练/部署consumer不同，不把全差额归一种噪声。100Wiki103文本Fix/Clean诊断，semantic/factual替换主要保持原context，不授事实纠错；XDLM有更高Fix、DSL有更高Clean两者不得合成全优。200open prompts与4×1000summarization/seed42、GPT2Large GenPPL、ROUGE/BERTScore/GPT5.4 judge；较低NFE主收益局限anchored短输出，longref高NFE原LLaDA可更优，creative24%degenerate/1024token重复28%，不签通用长文能力。

B2称NFE=N=两次求值×N/2，但Alg2末尾另列一次freshforward解码；未核代码不补复用或实际N+1计数，不能据名义NFE授精确同费用。全词表converter/top512、continuationtrain、Heun/eta/schedule扫描和独立质量成本不消失；未核服务并发/SLO或复现。当前必要域已足支持兼容路线，不采用未读完整E8计时或全摘要数字。

actual完整读Ch24“连续高斯去噪迁往离散文本”原失败/solver分支、LangFlow CE→expectedembedding、RePlaid等预算扩容两段与球面endpoint段；另读blinddenoiser/schedule分工与selfconditioning期望状态组。既有新训练连续模型和离散支持上SC状态迭代，不承担**改造现成MDLM输入噪声/嵌入converter、以cleanCE续训后才交continuous sampler**；不是再讲delaycommit本身。唯一`MULTIMODAL-GENERATIVE-PARADIGMS`。拟在RePlaid完整第二段（结束“而非按范式名称迁移。”）后、现“连续文本的端点还可以与生成器一起学习”前补一段：

> 连续路线也可从已有masked语言模型适配，而不从零重训：给token的单位范数噪声embedding加入按SNR缩放的Gaussian扰动，再经可训练converter形成backbone可读的软token混合，仍以原clean token的CE续训。[受限DSL-LLaDA桥](https://arxiv.org/html/2606.01024v1#S3)随后让response连续状态反复消费预测embedding，cleanprompt保持固定，末步才读出硬token；这不是直接替换原离散sampler，训练状态、converter与solver须成套验收。Top词表近似、有限Heun/噪声日程和延迟commit不认证原联合分布，名义NFE还须核最终解码求值；短源约束生成的局部优势不授事实修复，长参考/高步数与开放创作仍可退步。续训、全词表转换和全部求值/搜索都付费，质量、长度/多样性或预算不合时保留原MDLM、离散重掩码或AR，不由少量适配steps宣布连续路线普遍更优。<!-- source-family:SF-2026-ARXIV-2606-01024 -->

## 01026 D3IM/SCOPE — 2+1+2=5，clean-slate选择与self-error监督的配对

[v1](https://arxiv.org/html/2606.01026v1) / [原件](SUP_CLOSE_2606.01026v1_20261025.html)。实际读§3–4/T1–5、A4、B1–3、C4/C5与直接反侧；未全prompt/图像素/代码或复现。D3IM每步重预测currentblock所有位置，以当步candidate confidence topK重建state，没入选的置mask，不因先前visible而copy；已完成前block仍冻结，最后一步无条件接全block，fullydecoded非correct。EOS/EOT仅非末步confidence−infty，不是改logit到0/彻底删除输出词表。

SCOPE先no-grad从带mask输入采样，用tau1概率给tau1.5采样候选选toprho，再第二pass只对committed+remainingmasked以goldCE；原正确visible不参与loss，一半标准MDM混合。原错误visible可被直接覆盖不等全部误差一定定位/修正。A4的三路mixture/noiseconservation只是理想边际框架，deterministic confidence topK与贪心候选尚未证明完整学习联合分布保持，不借corrector名授exact。

LLaDA8B/qkvoLoRAr64、500FineWebsteps/单A100约20min，batch1×acc4/lr1.5e-4；64/128/256steps、output256/512、四bench固定protocol，precision和完整serve费用未齐不补。原模型+D3IM四任务全有害，SCOPE+std在code亦退；matchedMDMCPT不胜D3IM，支持配对而非额外训练自动有益。MBPP256steps 36.6低于原std39.2，不能称更多steps单调/全任务优；ReMDM在SCOPE上退、Tolerator近中性，不能泛化为任何revokable解码。Focusedloss/commit消融在固定超参下支持组件，但自产错误只模拟一步、topK有选择偏差；更低ECE非实际全部轨迹correctness，LLMjudge局部useful标签非gold内部语义。训练两pass、全部revision/回退和质量回归计费。

actual完整读Ch24 Self-revision下跨步分布dynamic、permanentlock、dualview验证、DMax的provisional表示/code/训练selfnoise/oscillation整组、后randomremask分支。现文已有“runtime不保证纠错、训练须见自产noise”，不能再靠这句制造增量；但**不继承旧visibletoken的clean-slate每步重选，以及只监督selfcommit错误人口的配对**是独立于softprovisional/选择重开策略的具体选择。唯一Ch24，不拆到SFT/LoRA重复参数化。拟在DMax完整末段（结束“其batch-1双卡结果不能写成servinggoodput。”）后、现随机remask完整段之前加一段：

> 可撤销状态还可采用不继承旧visibletoken的clean-slate规则：每步对当前block重新提出所有candidate，只让本轮confidence top-K存活，其他位置回mask，因而同时允许直接换token与撤回。[受限D3IM/SCOPE配对](https://arxiv.org/html/2606.01026v1#S3)先以no-grad自产一批带高置信错误的可见状态，再只对自产commit及剩余mask用gold监督；这不同于把所有干净位置等权重训。未适配模型直接换此sampler反而退步，训练收益也不自动转给其他重掩码规则；top-K、最终强制接收与EOS政策均属sampler身份，不由corrector框架继承精确联合分布或正确性。部分code任务更多步仍反退，训练双pass、所有重预测与独立质量回归计费；错误排序或预算不稳时保原单调揭示、较小block和完整验收，不把允许修改等同会正确修改。<!-- source-family:SF-2026-ARXIV-2606-01026 -->

## 00724 WaveFilter — 2+1+2=5，现步query提出旧prompt KV稀疏读取

[v1](https://arxiv.org/html/2606.00724v1) / [原件](SUP_CLOSE_2606.00724v1_20261025.html)。实际读§3–4/T1–3、A算法、B设置；未核图像素/代码或复现。Haar沿旧prompt K序列做低频层次，currentactivequery先在压缩K上提候选区域，再回原K索引细筛，最终读取原分辨率KV并拼generationKV。丢弃高频作proxy不证明“去语义噪声”，非denseattention等价；响应条件会改prompt表示，身份固定也不授AR式exactprefix。

Eq8称columnsum但下标上界是压缩prompt长度非Q行；A中B递减/下一层重置未明、稀疏V赋值误写K变量。不给可执行配方或替作者修正，保文字两层selector与有限观测，不用算法形式自签实现已核。单A80080G/LLaDA8B与Dream7B、统一confidence .9、maxgen256、B2/Haar；比例各dataset .3–1调整，不称无调参/统一最优。Precision、batch/并发和SLO未披。TPS到EOS与实际输出数量/steps相关，T1很多Fast+Wave速度约半且TREC/TrQA质量退，Ruler一些还慢于dense；Elastic不同任务有好坏，不能把baseline-relative倍率当对同cache组合继续提速。B增深或保留更少均非单调、长8K仍远未恢复dense，聚焦两任务热图不代表普遍最优。DWT、权重矩阵、gather/索引与更多steps/全部校准成本都付费。

actual完整读Ch24“双向cache可变”两近似分支、credit/softembedding与刷新组、“Cache误差沿生成轨迹演化”及double-sparse修正完整组；前较早的image均值pooled稀疏/MCsparse分支也读。现文已承担cache近似/质量与全费，但没有**沿旧prompt K作多尺度代理、由当前Q先粗选再回原KV细筛**的读取选择；不用“wavelet很新”或“缓存不免费”准入，准入依这条具体质量—读取替代设计。唯一Ch24。拟在“双向cache”中原第二近似段及其独立08086 marker之后、现“跨轮复用还可以保存尚未提交预测分布”前加一段：

> 对长prompt还可把“刷新哪些状态”与“本步读取哪些旧KV”分开：先将旧prompt的K沿序列形成多尺度低频代理，用当前activequery粗选候选区域，再回原索引细筛并读取原分辨率K/V，与generation状态共同计算。[WaveFilter的受限替代](https://arxiv.org/html/2606.00724v1#S3)不把低频相关当语义真值，也不使双向prompt缓存成为exactprefix；压缩代理可能漏关键位置。有限cache组合有质量恢复却明显降低吞吐的情形，部分任务质量也退，更多层次或更少保留不单调；DWT、索引gather、选参及变化后的生成steps都计费。公式索引/伪代码不闭时不照录可执行recipe，质量、状态或净费用不合时扩大读取、密集刷新或回原cache/fullattention，不把相对dense的加速当作相对原cache的继续收益。<!-- source-family:SF-2026-ARXIV-2606-00724 -->

## 当前交付

三项拟5分必要与actual-owner gap即交root，三位置无Books写入。余MODEL7：00722/01774/02544/02241及01839/01065/00866；另02358/00289/02502/02576与有限发现收束普通。四定义/前批与已成层不第三审，不待整日才交就绪证据。
