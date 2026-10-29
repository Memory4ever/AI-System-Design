# 2509.07252v1 GCond：唯一首必要Source与owner提案

## 角色与范围

Darwin104明确让出07252v1必要Source，作者/Bacon仅持92/129完整题摘与128公告资格，无Methods首读；root收到明确让出才开始。按本日Sep10BJT独立上下文重读AGENTS、当前Research/Report合同、Sources使用/Daily/arXiv、Prompt、ROADMAP与本日停点；不加载别日候选，不重已过题摘/查询。本文拟采用只一般多目标优化/训练状态，不研究CT医学结果或临床效力。root首准备交Darwin一次不同角色实际采用，不自己签通过，Bacon不第三Source。

## 原件、精确事件与已读层

正常唯一GET exact-v1与notice：`REPAIR_STEM_ROOT_SOURCE_07252V1_R20261023_20261021.raw.html`200/212136B/SHA256 `db6991f4af02f32de8fb4cd96d90655120e777a0c7ad004cec5a30fb0f0b583e`；notice同前缀`ROOT_NOTICE_07252`200/46568B/`f93d2be3cefab93225468a60b9118a01656ddc5b29718fd33f7742b8e0495bb2`。执行Oct23T02:19:30/32Z，真实bytes/SHA与request均相合；末后20261021只是复用捕获器命名，非实际检查日。

实际完整Methods的accumulation/arbitration/winner与实验设置、Results stochastic/optimization/效率/optimizer组合及对应Tables1–5、Discussion原理/PCGrad/limitations、AppendixA配置；其中CT专有数值和视觉结果不采用，不看CT图像/全部supplement曲线。只ImageNet masked reconstruction的一般优化条件和实现语义，不把ImageNet认作分类能力评测或模型质量全面验证。未运行code、训练、DDP或复现。

notice实际history v1 Sep8T22:02:22Z、v2 Apr1,2026T20:57:56Z；当前IEEE2026出版/版权说明不回填v1或另做本窗事件。精确`REPAIR_FORMS_MODEL_P1_20261023.raw`同DOI/arxiv.content/findable、v1 S相同、registered Sep10T01:36:56Z，适用L Sep10T00Z至U整个同Sep10BJT；后版dates不能冒v1。未见必要页具名撤回/勘误，无全球first保证。

### 具名更早artifact与有限实现核验

原v1 Data Availability明确Zenodo17041808；已一次取其API元数据，原件`REPAIR_STEM_ROOT_ARTIFACT_07252_R20261023_20261021.raw.json`200/6787B，metadata为同题软件/实验数据、version1.0.0、publication_date Sep2、created Sep3T09:08:20Z。该record已公开accumulate-then-resolve的软件说明，因此**不能称GCond机制或code首次在Sep10出现**；本次事件只处理新arXiv论文及其评价，先前软件/日志是不同事件角色，不把created改名首发、也不把软件发布日期替论文首正文日。

文件表只有scripts.zip、GCond.zip及两份TensorBoard日志包，没有论文PDF/正文；未下载约174MB/596MB实验日志或全Git历史。只为必要归一/次序疑点，取该精确record的14432B `GCond.zip`，原件`REPAIR_STEM_ROOT_CODE_07252_R20261023_20261021.raw.zip`正常200/1.049251s，未解压写入/执行；ZIP目录仅README.md与grad_conductor.py。README只实际检索机制/accumulation/stochastic相关说明，不冒全文已读。code用标准ZIP/AST读取，不运行其中指令。

实际代码段：`_accumulate_for_loss`256–307、`_resolve_conflict`309–367、`_run_arbitrator`369–422、`_project`424–555、`_momentum_update`557–602、`_write_to_model`604–616、`step`619–719。只这些必要callsite，不授整个包/完整训练脚本/实验对应实现或可生产性。其归一明确stochastic每loss用K/N batch并除K/N，sequential每loss用K并除K；任务权重在求导前乘入。Smooth分支与旧hard分支不同，critical时旧分支直接zero loser，不能把它们说成同一策略；本文推荐smooth才是所述正弦modulator。当前默认/各实验真正调用参数尚未核训练脚本，不用archive一个实现认证全部作者曲线。

## 拟正式评分与必要证据

拟 **2+1+2=5**，仅优化组件的“先形成每目标稳定估计，再仲裁/平滑并交optimizer”的替代设计；不借PCGrad成熟原理、并行潜力、ImageNet规模或自己的批评加分。原准入P保持，标准必要域已准备，具体owner缺口可在这些原域内深入，不为分数强读全附件。

旧weighted sum在目标相容时简单低费；逐microbatch投影则可能把采样噪声当稳定任务冲突。本文先固定同一参数状态θ，对每项loss分别保梯度buffer，累积后比较最负cosine。噪声方差精确1/K需独立等分布、固定θ/有限方差；有相关性须加协方差，不能由大batch直接授角度已可靠或真实下降方向。梯度投影是非线性的，平均后投影与逐batch投影后平均不是同一更新目标/轨迹。

多区间仲裁用阈值将cosine映到角度，再以sin形成对winner/loser不同校正；winner由与上一步梯度的cosine稳定度及相对EMA范数加权选择。主实验dominance_window=0，不能借可选反连续胜规则证明全部task被公平更新。循环/threshold/max_iters和zero-normguard都影响输出，没有全任务共同下降、Pareto最优、无饥饿或收敛保证。内部EMA在投影后、AdamW adaptive denominator之前；外部beta1设0与普通AdamW组合是不同优化器，不把更好曲线唯一归因投影。

Stochastic把K分成N块，每loss只用独立K/N microbatches但不先更新θ。原archive除以实际K/N说明每loss均值，而非每loss各看完整batch；即使任务均值估计条件下无偏，经选择/投影/EMA后的完整更新也不因此无偏或等价sequential。连续有序数据、loss人口不同、K不可整除N或BN/Dropout状态改变都须另验；code的freeze_bn若启用实际切model.eval，也关闭dropout，不能说只是优化同一随机forward的内存。head/buffer数据支持、norm EMA、历史梯度、momentum、AMP和更新step共同是训练状态。

实现每目标在fresh detached leaf上functional_call/autograd.grad，retain_graph=False后立即放入bf16 buffer，最后FP32相加、按策略写p.grad；它避免跨目标保留共同graph，却仍需N组参数梯度/历史和momentum状态，不是零graph成本或显存与任务数无关。可选DDP在rank-local投影/平滑后再AllReduce；一般`mean(project(local_g))`不等`project(mean(local_g))`，所以不授集中全局目标的等价多卡recipe或分布式正确性已验。代码只静态核，未运行。

### 一般训练评价与直接反侧

ImageNet1K重构使用MAE/MobileNetV3Small、2层decoder/d256、256²、mask.75、L1与SSIM loss（不是SSIM similarity越高越好）、15epoch/2warmup、AdamW2e−4/.05、K24与batch256；Appendix称seed11/42/2025的mean/CI，但未给足CI构造或等效检验。Table2 ImageNet baseline L1 .41542±.00716/SSIM loss .34845±.00764，stochastic .31655±.00287/.24704±.00262，sequential .31493±.00056/.24485±.00093，只这些受限协议观察。区间相交/差不显著不证明两个算法等效；未测下游分类、语言模型、长期质量或全预算最优。L1/SSIM尺度还刻意分z-normalized与[0,1]以加重冲突，不假设任意目标人口同态。

Table3 ImageNet GCond 8739.54MB/1415.66sample/s，baseline6888.98/1421.73，PCGrad7515.89/1322.73：它并非所有模型更省memory，也没有超过简单baseline吞吐。RTX4080/16GB/PyTorch2.7/Python3.12/CUDA12.8与大模型H200/PyTorch2.5.1/Python3.10/CUDA12.4分开，不把跨机差额当单机制收益。大ConvNeXt可行性/不同batch表属于作者实现条件，PCGrad等也可重写functional_call，不能证明它们理论上必须永久retain graph或不能跑大模型。

效率段称固定K而按16GB填不同B“保持每epoch相同更新数”，但固定数据量时更新数约样本数/(B×K)，改变B并不保持它；Table4更直接列不同effective batch。这只是指出比较计量不闭，不把CT数值当主线性能证据或给更快训练的因果结论。Hybrid Lion/LARS还改optimizer/LR/state，原文承认未全面对照，不能借它证明方向优于幅度或所有方法融合。更宽activation分布不是已验证无collapse/更好泛化。数据/超参搜索、每loss前反向、buffers/历史/投影/EMA、重算与完整收敛验收均付费；persistent anti-parallel、过大batch、分布漂移与阈值失配可退，原固定scalar loss/常规optimizer仍成立。

## 唯一知识owner与最小提案

实际读当前Ch28的Batch计量837–885完整节、ML-FOP-SOAP两段/完整绑定、其后GridUMM两段和streaming auxiliary-update投影交接；另读598–623 optimizer组合次序/硬件状态分责。唯一拟owner `TRAIN-PRETRAINING` [Ch28](../../../../../books/part-04-training-system/28-pretraining.md)，不是Ch36把同batch梯度分布式执行成同一更新的owner，也不在Ch4复制一般backprop。

现有ML-FOP-SOAP是曲率/Fisher投影加folding及模态方差state，GridUMM明确低冲突不等质量；现文尚未具体承载“对每loss保独立平均/同θ稀疏采样→先估计后非线性仲裁→momentum交接”的first-order替代接口。拟小gap仅这一顺序与支持，不复制权重/阈值/benchmark目录或把GCond作所有训练替代。原论文/代码早artifact角色与数值边界保报告。

拟正文严格一自然段：

> 不采用曲率估计时，也可先把每项loss在同一参数状态上的梯度分别累积，再处理方向冲突，而不是对每个噪声较大的micro-batch先投影后平均；非线性仲裁与平均不可任意换序。一条[受限的一阶分支](https://arxiv.org/html/2509.07252v1)用累积后的cosine、历史方向及相对范数提出校正，再把结果交给平滑和optimizer；还可将不同loss分给不重叠的micro-batch窗口，以较少重复前反向换取较少的逐目标样本支持。这要求共同绑定参数版本、每loss人口/实际均值归一、buffer精度、历史与momentum次序，不由均值估计无偏推出完整更新无偏，也不能把rank-local仲裁后的归约当成全局梯度先归约再仲裁。独立buffer、额外求导、投影/EMA与全部调参都付费；小模型ImageNet重构的观察不授大语言模型收敛，释放共同反向图也不保证所有配置显存更低。数据相关、持久反向冲突或质量/成本失配时，保留固定weighted loss、普通gradient accumulation与已验optimizer，以真实held-out质量和完整更新预算而非较低冲突自签收益。

拟独立marker：`<!-- source-family:SF-2025-ARXIV-2509-07252 -->`

拟作者自身末注：

> - `SF-2025-ARXIV-2509-07252` — Daily2025-09-11补Sep10；root唯一首准备exact-v1 Methods、Results必要ImageNet/效率/optimizer反侧、Discussion/AppendixA及Zenodo1.0.0精确归一/顺序callsite，拟2+1+2=5。只采用同θ每loss平均后仲裁与optimizer-state交接的条件分支；保非线性/分布式非等价、不同batch/optimizer混杂、额外buffers/全费及原weighted-loss退路。只静态读具名archive函数，未训练/核全代码/复现或采用CT医学结果；Sep2软件与Sep10新论文事件分开，2026v2不倒填。实际非准备者采用/PRE/保存/POST只按后续已发生事实记录。

拟插入ML-FOP-SOAP完整两段/结束binding之后、以“投影能减少梯度方向冲突，仍不等于冲突量已被校准为任务取舍的诊断器。”开头的完整GridUMM首段之前；全部直接两侧及bindings保持。这里只首Source/分/owner/稿提案，不是已过独核、root新写位或整合；Darwin一次采用后准备自己的实际当前完整邻接，Bacon只原稿PRE/真实POST，不第三Source。
