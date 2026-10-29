# MemTrain 03197 必要Source / actualowner / 最小两段PRE

作者supp_20260604_author。复用R27准入/Jun03联合日证及2+1+2=5，不第三AB/date。HTMLfirst exact-v1 §3–6/式1–4/表1–3/A文本必要域已读，支持/关键反侧足够停止。完整剥标保mathannotation TEXT55890字符实存SUP_CORE_2606.03197v1_TEXT_20261024.txt，无工具截断。A有模板图未核像素，只有其可见说明与正文定义足够支持本稿，未声称完整prompt模板/实现/复现已核；没有为非采用recipe读代码/refs。首次fetch异步session实际等exit0再采用。

## 必要证据与不采用范围

§3.1–3.3：固定m_t与当前action/input迭代，nonterminal输出memory、最后只用memory答题。Wikipedia pivot+相关+random passages随机次序，目标y在全文所有occurrences均[MASK]；终态恢复不能copy但未隔离参数先验或语义猜测贡献，不证明必须长程memory才可解。IMR从完成E轨迹选中间k和更早l<k，输入是当前memory+遮目标的历史chunk，并非memory独立重构整篇。A文本说明IMR[TARGET]区别原任务[MASK]，未核图中指令不抄具体模板。只一随机k/l及entityEM不证明全部中间memory完整/保真。

§3.4 exactmatch R_I，R_E=finalEM+lambda*mean(IMR)，对E每轮广播trajectory advantage；DrGRPO unnormalized groupcenter，不是memoryspan-only信用/逐轮因果。Decoupled仍有IMR训练但不加进E reward，故能区分回忆训练与间接写入压力；未有同状态反事实memorycausality。式4印面outeri到G1+G2而总collection应涉及G1G2、分支索引r与统一o_i表述不齐；filter all0/all1与复合R范围也未解释清楚，本项不采用完整optimizer/精确过滤实现，不从算式照录可复现recipe。

§4.1 corpus30k documents24k–40k（后文32k–40k口径略不同），每pivot top29related+120random，spaCyNER。8k context allocation1024instructions+5120chunk+1024memory+1024response，上限约8chunks，非无限历史零开销；batch32、G1=8/G2=8、300steps/lr1e-6、lambda.5/KL1e-3、veRL但versions/GPUs/precision/GPUhours NotDisclosed。后训MemAgent500steps/rollout32/update8/lr1e-6/3seeds；searchMEM1 200steps/max6turn/各response及retrieval1k，未明确同样3seed。longQA7k–896k：basefullcontext与memorychunkpipeline不同，不把basevsMemTrain总差额全归具体reward，单MemAgent与初始化后同下游协议较窄可比，但额外300step预算未匹配。T1Qwen3 448k MemTrain+MemAgent61.72低于MemAgent64.06，反驳主文allcontextconsistent；7B总体收益不抹此反侧。T2search双objective平均EM，仅任务输出不是完整事实或tool可靠性；MemTrainonly未见tool环境不参search，不授零样本tool迁移。

§5.1去IMR平均70.31→63.28/Decoupled长侧退支持该配方局部代理价值，但图像未核不造逐长度曲线。§5.2多300下游steps（500→800）最佳约700仍差2.64pp，只固定steps额外训练对照不等token/GPU或G1G2调用总费，不能排除全部compute替代。§5.3/T3 case方向明确内部冲突：表头MemAgent列保location并最终GreenwichVillage，MemTrain+列丢location/Cannotbedetermined，§5.3文字却称反向；不采用该case作正面机制归因，也不自行交换表头。主表/机制有限命题仍可采用，未因一case中心争议泛化整论文否定。全语料/NER/retrieval、E长rollouts/G1G2回忆、评分/更新、后训与原episode/独立heldout都计费。

## actualowner与最小差额

ROADMAP唯一AGENT-MEMORY Ch77。actual完整读开篇状态边界、163–218 pendingfailure/typedwrite/contentcredit整组，尤其MemPO/InfoMem/VideoEMem/共同writer-reader/GRUMem的实际完整论证与衔接；Ch76/78开篇职责定点核。现MemPO/InfoMem依gold QA与likelihood评分，VideoEMem冻结writer再训reader但非entityreconstruct，已有contentcredit也非source构造E/IMR两proxy和广播credit的额外初始化阶段。因此不是仅主题同就NC；通用GRPO实现由Ch33拥有，本处只保memory目标/credit消费者差额，不重复优化器推导。三Bookscontext/ROADMAP当前轮前已读可复用。

建议仅InfoMem完整两段/marker后、VideoEMem完整段前原两段+本人trueH2注。无本项Books新授，尚未写；待同reader首次必要Source/actualowner/PRE。

完整上锚：

终态记忆还可以用另一份训练代理评价：在同一问题上，比较模型对 gold answer 的逐 token 平均似然在有最终记忆与空记忆时的差额，再只对已通过答案匹配的轨迹区分其记忆支持度。一条[受限奖励分支](https://arxiv.org/html/2606.03329v1)先在同组成功轨迹内归一这一分数，再与 outcome reward 组合；这一步不是 GRPO 对最终奖励的组归一。没有成功项时不加此分数，只有一项时保留 raw 值，故不能称所有组都受到同等尺度控制。奖励虽然读取最终记忆，产生的轨迹 advantage 却作用于记忆更新和答案的全部生成 token，不提供逐条记忆或逐步写入的因果信用。<!-- source-family:SF-2026-ARXIV-2606-03329 -->

这里测得的是带 gold、模型与提示条件的点似然代理，不是分布级 mutual information 或事实真值；仅用 query 似然甚至可能奖励复制问题，而不是保存答案证据。局部错侧监督退化、成功侧更稳的对照也不证明所有失败轨迹都无学习价值，更不能把训练期的正确答案偷带进部署。长 Context rollout、额外答案评分、归一与独立任务验证均需计费；gold、匹配规则或评分器资格不可靠时，应保留原 episode、outcome-only 与可靠内容检查，不让较高 likelihood 或受选成功人口批准无损压缩、永久删除与线上事实写入。<!-- source-family:SF-2026-ARXIV-2606-03329 -->

拟增两段：

没有现成任务 QA 标注时，还可以先用原始文本构造两种不同的记忆训练代理：把长文中的目标实体全部遮住，多轮压缩后只凭最终记忆恢复；另从一条已完成轨迹抽取中间记忆，把更早片段中的另一个目标遮住，再让模型用该片段与记忆共同重构。后一条测试的是有提示的历史可用性，不是无提示完整回放；前一条也可能借助参数先验，答对不单独证明证据被保存在记忆里。

[受限自监督训练](https://arxiv.org/html/2606.03197v1#S3)把中途重构奖励加入终态奖励，再向记忆更新的各轮广播轨迹 advantage，同时训练回忆分支；它不提供 memory-token 局部因果信用，也不让 source 文本或 exact match 成为事实权威。这个额外阶段可作为任务后训练的初始化，但多采样回忆、语料检索/实体处理、完整 rollout 与后训练都要付费；追加相同步数并非匹配 token、分支调用或 GPU 总预算，有限 QA 提升也不证明所有长度均受益。代理歧义、源文错误或 held-out 回归时，应保留原 episode 和来源回读，回退任务 outcome-only/固定压缩；不要以恢复一个实体批准永久丢弃历史、任意未来可答或生产可靠性。<!-- source-family:SF-2026-ARXIV-2606-03197 -->

完整下锚：

未来query未知时，writer还可先按source保留而非开发QA成功来演化：逐级压缩caption并回查遗漏、另选与text互补的原帧，冻结memory后才用QA失败调整reader的定位和组织。[Video-EMem的受限控制](https://arxiv.org/html/2610.24537v1#S3.SS4)把memory缺失与reader漏读分开，前者不能算后者的定位错误；但caption和语义match仍是proxy，source未观察到的事实不能由更多压缩容量补回。分阶段优于jointQA的局部差额未独自证明overfit因果，query-time或持久payload变小也未包含全部构建/演化费用。caption、原帧、全部候选/审核、索引和query调用都计费；source保留、版本或后query回归不合时保原episode、curatedmemory与完整读取，不由writer分数或低存储批准完整事实和任意未来可答。
<!-- source-family:SF-2026-ARXIV-2610-24537 -->

本人trueH2注拟：`SF-2026-ARXIV-2606-03197`：Daily2026-06-04补Jun03，exact-v1 §3–6/式1–4/表1–3/A文本必要，2+1+2=5因E/IMR双proxy与credit具体gap深入。只文本构造/有提示重构与trajectory广播，非无标注真值/完整memory或局部因果；保参数先验、额外G1G2/后训全费、step非matchedcompute、448k反退/原T3case方向冲突不采。不采用印式4完整optimizer/全过滤recipe；未核模板图像素/代码/复现。待PRE/新授/实际POST。

